import os
import re
from urllib.parse import urlparse, unquote

BASE_DIR = os.path.abspath('emuqi')

all_html_files = []
for root, dirs, files in os.walk(BASE_DIR):
    for f in files:
        if f.endswith('.html'):
            all_html_files.append(os.path.join(root, f))

print(f"Total HTML files to inspect: {len(all_html_files)}")

broken_links = []

for html_file in all_html_files:
    rel_source = os.path.relpath(html_file, BASE_DIR)
    source_dir = os.path.dirname(html_file)
    with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Find all hrefs
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
    for href in hrefs:
        href_clean = href.strip()
        if not href_clean or href_clean.startswith('#') or href_clean.startswith('mailto:') or href_clean.startswith('tel:') or href_clean.startswith('javascript:'):
            continue
        
        parsed = urlparse(href_clean)
        # Check if external or internal
        if parsed.scheme in ('http', 'https'):
            if 'emuqi.com' not in parsed.netloc:
                continue
            path = parsed.path
            if path.startswith('/'):
                target_path = os.path.join(BASE_DIR, path.lstrip('/'))
            else:
                target_path = os.path.join(BASE_DIR, path)
        else:
            # relative or root-relative
            path = parsed.path
            if path.startswith('/'):
                target_path = os.path.join(BASE_DIR, path.lstrip('/'))
            else:
                target_path = os.path.normpath(os.path.join(source_dir, path))

        target_path = unquote(target_path)
        
        # Check target
        exists = False
        if os.path.isfile(target_path):
            exists = True
        elif os.path.isdir(target_path):
            if os.path.isfile(os.path.join(target_path, 'index.html')):
                exists = True
        elif target_path.endswith('/') or not os.path.splitext(target_path)[1]:
            if os.path.isfile(target_path + '.html'):
                exists = True
            elif os.path.isfile(os.path.join(target_path, 'index.html')):
                exists = True

        if not exists:
            broken_links.append((rel_source, href_clean, target_path))

print(f"\nTotal broken link references found: {len(broken_links)}\n")
target_counts = {}
for src, href, target in broken_links:
    target_counts[href] = target_counts.get(href, 0) + 1

for href, count in sorted(target_counts.items(), key=lambda x: x[1], reverse=True)[:40]:
    print(f"[{count} times] {href}")
