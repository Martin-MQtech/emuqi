import os, glob, re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote

BASE_DIR = os.getcwd()

html_files = [f for f in glob.glob('**/*.html', recursive=True) if not f.startswith(('templates/', 'node_modules/', '.git/'))]

print(f"=== MUQI DEEP LINK AUDIT ===")
print(f"Total production HTML files to audit: {len(html_files)}")

# Cache parsed HTML files and their IDs
file_cache = {}
page_ids = {}

for rel_path in html_files:
    full_path = os.path.join(BASE_DIR, rel_path)
    with open(full_path, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    file_cache[rel_path] = content
    # Find all IDs and named anchors
    soup = BeautifulSoup(content, 'html.parser')
    ids = set()
    for tag in soup.find_all(True):
        if tag.get('id'):
            ids.add(tag['id'])
        if tag.get('name'):
            ids.add(tag['name'])
    page_ids[rel_path] = ids

issues = {
    'broken_internal_links': [],
    'broken_anchors': [],
    'redirected_internal_links': [],
    'malformed_hrefs': [],
    'broken_canonicals': [],
    'broken_hreflangs': [],
    'empty_hrefs': [],
    'http_insecure_links': [],
    'lang_switch_issues': []
}

# Load .htaccess 301 rules to detect redirect hops
redirect_map = {}
htaccess_path = os.path.join(BASE_DIR, '.htaccess')
if os.path.exists(htaccess_path):
    with open(htaccess_path, 'r', encoding='utf-8') as f:
        ht = f.read()
    for m in re.finditer(r'RewriteRule\s+\^?([^\$\s]+)\$?\s+([^\s]+)\s+\[(?:.*R=301.*)\]', ht):
        src_pattern, dest = m.group(1), m.group(2)
        # clean pattern
        src_clean = src_pattern.replace('\\.', '.').lstrip('^').rstrip('$')
        if src_clean: redirect_map[src_clean] = dest

# 1. Inspect every HTML file
for rel_path, content in file_cache.items():
    soup = BeautifulSoup(content, 'html.parser')
    dirpath = os.path.dirname(rel_path)
    
    # Check <a> tags
    for a in soup.find_all('a'):
        href = a.get('href')
        if href is None:
            continue
        href_raw = href.strip()
        
        # Check empty or javascript void
        if href_raw in ('', '#'):
            # Only flag if not a deliberate UI toggle with onclick/role
            if not a.get('onclick') and not a.get('role') and not a.get('class'):
                issues['empty_hrefs'].append((rel_path, str(a)[:100]))
            continue
            
        if href_raw.startswith(('javascript:', 'mailto:', 'tel:')):
            continue
            
        # Check insecure http
        if href_raw.startswith('http://') and not 'localhost' in href_raw:
            issues['http_insecure_links'].append((rel_path, href_raw))
            
        # Check malformed
        if 'https//' in href_raw or 'http//' in href_raw or '..' in href_raw.split('/')[-1]:
            issues['malformed_hrefs'].append((rel_path, href_raw))
            
        # Parse internal vs external
        parsed = urlparse(href_raw)
        is_internal = False
        path_part = parsed.path
        fragment = parsed.fragment
        
        if parsed.scheme in ('http', 'https'):
            if parsed.netloc in ('www.emuqi.com', 'emuqi.com'):
                is_internal = True
        elif not parsed.scheme:
            is_internal = True
            
        if is_internal:
            # Resolve target file
            if not path_part:
                target_rel = rel_path # self anchor like href="#section"
            elif path_part.startswith('/'):
                target_rel = os.path.normpath(path_part.lstrip('/'))
            else:
                target_rel = os.path.normpath(os.path.join(dirpath, path_part))
                
            if os.path.isdir(os.path.join(BASE_DIR, target_rel)):
                target_file = os.path.normpath(os.path.join(target_rel, 'index.html'))
            else:
                target_file = target_rel
                
            # Check existence
            if not os.path.exists(os.path.join(BASE_DIR, target_file)):
                issues['broken_internal_links'].append((rel_path, href_raw, target_file))
            else:
                # Check fragment / anchor
                if fragment and target_file in page_ids:
                    if fragment not in page_ids[target_file]:
                        issues['broken_anchors'].append((rel_path, href_raw, target_file, fragment))
                        
            # Check if this link hits a known 301 redirect
            check_key = path_part.lstrip('/')
            if check_key in redirect_map:
                issues['redirected_internal_links'].append((rel_path, href_raw, redirect_map[check_key]))
                
    # Check canonical & alternate
    for link in soup.find_all('link'):
        rel = link.get('rel')
        if not rel:
            continue
        rel_str = ' '.join(rel) if isinstance(rel, list) else str(rel)
        href = link.get('href', '').strip()
        if 'canonical' in rel_str and href:
            p = href.split('emuqi.com/')[-1].split('?')[0].split('#')[0] if 'emuqi.com/' in href else href
            if not p or p == '/': p = 'index.html'
            if p.endswith('/'): p += 'index.html'
            if not os.path.exists(os.path.join(BASE_DIR, p)):
                issues['broken_canonicals'].append((rel_path, href, p))
                
        if 'alternate' in rel_str and href and link.get('hreflang'):
            p = href.split('emuqi.com/')[-1].split('?')[0].split('#')[0] if 'emuqi.com/' in href else href
            if not p or p == '/': p = 'index.html'
            if p.endswith('/'): p += 'index.html'
            if not os.path.exists(os.path.join(BASE_DIR, p)):
                issues['broken_hreflangs'].append((rel_path, href, p))
                
    # Check language pill switcher
    lang_capsules = soup.find_all(class_=re.compile(r'lang-pill|lang-switch|lang-selector'))
    for lc in lang_capsules:
        for opt in lc.find_all('a'):
            l_href = opt.get('href', '').strip()
            text = opt.get_text().strip()
            # check if destination exists
            if l_href:
                p = l_href.split('emuqi.com/')[-1].split('?')[0].split('#')[0] if 'emuqi.com/' in l_href else l_href
                if p.startswith('/'): p = p.lstrip('/')
                elif 'emuqi.com' in l_href: pass
                else: p = os.path.normpath(os.path.join(dirpath, p))
                if os.path.isdir(os.path.join(BASE_DIR, p)): p = os.path.join(p, 'index.html')
                if not os.path.exists(os.path.join(BASE_DIR, p)):
                    issues['lang_switch_issues'].append((rel_path, text, l_href, p))

print("\n--- AUDIT RESULTS ---")
for k, v in issues.items():
    print(f"{k}: {len(v)}")
    for item in v[:10]:
        print(f"   {item}")
    if len(v) > 10:
        print(f"   ... and {len(v)-10} more")
