import os, glob, re
from collections import Counter

html_files = glob.glob('emuqi/**/*.html', recursive=True)
root_dir = os.path.abspath('emuqi')

broken = Counter()
broken_details = []

for f in html_files:
    f_dir = os.path.dirname(os.path.abspath(f))
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    
    links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', content)
    for l in links:
        if l.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', '#')):
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
            rel_source = os.path.relpath(f, root_dir)
            broken[clean_l] += 1
            broken_details.append((rel_source, clean_l))

print("Total broken link occurrences:", len(broken_details))
print("\nTop 25 missing link targets:")
for target, count in broken.most_common(25):
    print(f"  {target}: {count} occurrences")
