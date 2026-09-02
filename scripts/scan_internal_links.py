import os, glob, re
from urllib.parse import urlparse

root_dir = os.path.abspath('emuqi')
html_files = glob.glob('emuqi/**/*.html', recursive=True)

broken_links = []

for f in html_files:
    rel_path = os.path.relpath(f, root_dir)
    f_dir = os.path.dirname(os.path.abspath(f))
    
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    
    links = re.findall(r'(?:href|src)=[\'"]([^\'"]+)[\'"]', content)
    for l in links:
        if l.startswith(('mailto:', 'tel:', 'javascript:', '#')):
            continue
        
        if l.startswith(('http://', 'https://')):
            parsed = urlparse(l)
            if 'emuqi.com' in parsed.netloc:
                path = parsed.path
                if path:
                    target = os.path.normpath(os.path.join(root_dir, path.lstrip('/')))
                    target_html = target + '.html' if not os.path.splitext(target)[1] else target
                    target_idx = os.path.join(target, 'index.html')
                    if not (os.path.exists(target) or os.path.exists(target_html) or os.path.exists(target_idx)):
                        broken_links.append((rel_path, l, f"Broken internal full URL: {path}"))
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
            broken_links.append((rel_path, l, f"Broken relative path: {clean_l}"))

print(f"Total broken internal links: {len(broken_links)}")
for src, link, reason in broken_links:
    print(f"[{src}] -> '{link}' ({reason})")
