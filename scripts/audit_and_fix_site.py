#!/usr/bin/env python3
import os
import re
import json
import xml.etree.ElementTree as ET

emuqi_dir = "/Users/martin/Documents/2026 BUSINESS MTRIX /20260721 MUQI 网站建设/emuqi"

print("=" * 60)
print("MUQI Global Website Comprehensive Technical Audit & Clean")
print("=" * 60)

# 1. Check sitemap vs physical files
sitemap_path = os.path.join(emuqi_dir, "sitemap.xml")
tree = ET.parse(sitemap_path)
root = tree.getroot()
ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
sitemap_urls = [elem.text.strip() for elem in root.findall(".//sm:loc", ns)]

print(f"Total URLs in sitemap.xml: {len(sitemap_urls)}")

# Check if each sitemap URL exists physically
missing_in_disk = []
for url in sitemap_urls:
    rel = url.replace("https://www.emuqi.com/", "").replace("https://emuqi.com/", "")
    if rel == "" or rel.endswith("/"):
        rel += "index.html"
    disk_path = os.path.join(emuqi_dir, rel)
    if not os.path.exists(disk_path):
        missing_in_disk.append((url, rel))

print(f"Sitemap URLs missing on disk: {len(missing_in_disk)}")
for url, rel in missing_in_disk:
    print(f"  ❌ 404 in sitemap: {url} -> {rel}")

# Check if physical HTML files are in sitemap
missing_in_sitemap = []
for root_dir, dirs, files in os.walk(emuqi_dir):
    if ".git" in root_dir or "node_modules" in root_dir or "templates" in root_dir:
        continue
    for f in files:
        if f.endswith(".html") and f != "404.html":
            rel_path = os.path.relpath(os.path.join(root_dir, f), emuqi_dir)
            if rel_path == "index.html":
                expected_url = "https://www.emuqi.com/"
            elif rel_path.endswith("/index.html"):
                expected_url = "https://www.emuqi.com/" + rel_path[:-10]
            else:
                expected_url = "https://www.emuqi.com/" + rel_path
            if expected_url not in sitemap_urls and (expected_url + "/") not in sitemap_urls:
                missing_in_sitemap.append((rel_path, expected_url))

print(f"Physical HTML files not in sitemap: {len(missing_in_sitemap)}")
for rel, exp in missing_in_sitemap[:10]:
    print(f"  ⚠️ Not in sitemap: {rel} ({exp})")

# 2. Fix duplicate JSON-LD in blogs
blog_fixes = 0
for root_dir, dirs, files in os.walk(os.path.join(emuqi_dir, "blog")):
    for f in files:
        if f.endswith(".html"):
            fpath = os.path.join(root_dir, f)
            with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
                content = fp.read()
            matches = list(re.finditer(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', content, re.DOTALL))
            if len(matches) > 1:
                print(f"Found {len(matches)} JSON-LD blocks in blog/{f}, consolidating to first valid block...")
                # Keep the first valid one and remove others
                first_block = matches[0].group(0)
                # Remove all blocks
                new_content = re.sub(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>.*?</script>', '', content, flags=re.DOTALL)
                # Insert back right before </head>
                new_content = new_content.replace('</head>', f'{first_block}\n</head>')
                with open(fpath, "w", encoding="utf-8") as fp:
                    fp.write(new_content)
                blog_fixes += 1
                print(f"  ✅ Fixed blog/{f}")

print(f"Total blog duplicate JSON-LD fixes: {blog_fixes}")
