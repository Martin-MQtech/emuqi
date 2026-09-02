import re, os
with open('/Users/martin/Documents/2026 BUSINESS MTRIX /20260721 MUQI 网站建设/emuqi/sitemap.xml') as f:
    sitemap_text = f.read()

sitemap_urls = set(re.findall(r'<loc>(https?://[^<]+)</loc>', sitemap_text))

all_files = set()
for root, _, files in os.walk('/Users/martin/Documents/2026 BUSINESS MTRIX /20260721 MUQI 网站建设/emuqi'):
    if '.git' in root: continue
    for file in files:
        if file.endswith('.html'):
            rel = os.path.relpath(os.path.join(root, file), '/Users/martin/Documents/2026 BUSINESS MTRIX /20260721 MUQI 网站建设/emuqi')
            all_files.add(rel)

print(f"Total HTML files: {len(all_files)}")
print(f"Total Sitemap URLs: {len(sitemap_urls)}")

# Convert sitemap URLs to rel paths
sitemap_rel = set()
for u in sitemap_urls:
    path = u.replace('https://www.emuqi.com/', '').replace('https://emuqi.com/', '')
    if not path or path == '':
        sitemap_rel.add('index.html')
    elif path.endswith('/'):
        sitemap_rel.add(path + 'index.html')
    else:
        sitemap_rel.add(path)

in_files_not_sitemap = all_files - sitemap_rel
in_sitemap_not_files = sitemap_rel - all_files
print(f"In files but not sitemap ({len(in_files_not_sitemap)}): {in_files_not_sitemap}")
print(f"In sitemap but not files ({len(in_sitemap_not_files)}): {in_sitemap_not_files}")
