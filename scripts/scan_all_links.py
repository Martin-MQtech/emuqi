import os, glob, re
from urllib.parse import urlparse

root_dir = os.path.abspath('emuqi')
html_files = glob.glob('emuqi/**/*.html', recursive=True)

print(f"Total HTML files to scan: {len(html_files)}")

issues = []

for f in html_files:
    rel_path = os.path.relpath(f, root_dir)
    f_dir = os.path.dirname(os.path.abspath(f))
    
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    
    # Check all href and src
    links = re.findall(r'(?:href|src)=[\'"]([^\'"]+)[\'"]', content)
    for l in links:
        if l.startswith(('mailto:', 'tel:', 'javascript:', '#')):
            continue
        
        # Check if it points to emuqi.com
        if 'emuqi.com' in l:
            parsed = urlparse(l)
            path = parsed.path
            if path:
                target = os.path.normpath(os.path.join(root_dir, path.lstrip('/')))
                target_html = target + '.html' if not os.path.splitext(target)[1] else target
                target_idx = os.path.join(target, 'index.html')
                if not (os.path.exists(target) or os.path.exists(target_html) or os.path.exists(target_idx)):
                    issues.append((rel_path, l, f"Online URL target missing locally: {path}"))
            continue
            
        if l.startswith(('http://', 'https://')):
            continue
            
        clean_l = l.split('#')[0].split('?')[0]
        if not clean_l:
            continue
            
        if clean_l.startswith('/'):
            target = os.path.normpath(os.path.join(root_dir, clean_l.lstrip('/')))
        else:
            target = os.path.normpath(os.path.join(f_dir, clean_l))
            
        target_html = target + '.html' if not os.path.splitext(target)[1] else target
        target_idx = os.path.join(target, 'index.html')
        
        if not (os.path.exists(target) or os.path.exists(target_html) or os.path.exists(target_idx)):
            issues.append((rel_path, l, f"Relative link broken: {clean_l}"))

print(f"Total issues found: {len(issues)}")
for src, link, reason in issues[:30]:
    print(f"[{src}] -> '{link}' ({reason})")
