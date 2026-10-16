#!/usr/bin/env python3
"""
MUQI Tech (emuqi.com) Site Health & Dead Link Auditor
Automated Pre-Flight Gate to prevent 404s, broken anchors, missing assets, and navigation drifts.
"""

import os
import re
import sys
from urllib.parse import urlparse, unquote

def run_audit():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(script_dir, '..'))

    print(f"🔍 Starting MUQI Site Health Audit in: {root_dir}")

    html_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        if 'scripts' in dirpath or '.git' in dirpath or 'templates' in dirpath:
            continue
        for f in filenames:
            if f.endswith('.html'):
                html_files.append(os.path.join(dirpath, f))

    link_regex = re.compile(r'<(?:a|link)[^>]+href=[\"\']([^\"\']+)[\"\']', re.IGNORECASE)
    img_regex = re.compile(r'<(?:img|script)[^>]+src=[\"\']([^\"\']+)[\"\']', re.IGNORECASE)

    broken_links = {}
    broken_imgs = {}
    relative_dots = {}

    for html_file in html_files:
        rel_html = os.path.relpath(html_file, root_dir)
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Check links
        links = link_regex.findall(content)
        for l in links:
            l_clean = l.strip()
            if not l_clean or l_clean.startswith(('mailto:', 'tel:', 'javascript:', '#', 'data:', '//')):
                continue
            
            # Check for relative dot in blog articles
            if ('/blog/' in rel_html or rel_html.startswith('blog/')) and l_clean in ('.', './'):
                relative_dots.setdefault(rel_html, []).append(l_clean)
                continue

            parsed = urlparse(l_clean)
            if parsed.scheme in ('http', 'https'):
                continue # External URL

            path = unquote(parsed.path)
            if not path and parsed.fragment:
                continue

            if path.startswith('/'):
                target = os.path.normpath(os.path.join(root_dir, path.lstrip('/')))
            else:
                target = os.path.normpath(os.path.join(os.path.dirname(html_file), path))

            if os.path.isdir(target):
                target_file = os.path.join(target, 'index.html')
                if not os.path.exists(target_file):
                    broken_links.setdefault(rel_html, []).append((l_clean, f"Missing directory index: {target_file}"))
            else:
                if not os.path.exists(target) and not os.path.exists(target + '.html'):
                    broken_links.setdefault(rel_html, []).append((l_clean, f"Missing file: {target}"))

        # Check images and scripts
        imgs = img_regex.findall(content)
        for img in imgs:
            img_clean = img.strip()
            if not img_clean or img_clean.startswith(('data:', 'http:', 'https:', '//', 'javascript:')):
                continue
            parsed = urlparse(img_clean)
            path = unquote(parsed.path)
            if not path:
                continue
            if path.startswith('/'):
                target = os.path.normpath(os.path.join(root_dir, path.lstrip('/')))
            else:
                target = os.path.normpath(os.path.join(os.path.dirname(html_file), path))
            if not os.path.exists(target):
                broken_imgs.setdefault(rel_html, []).append((img_clean, f"Missing asset: {target}"))

    total_errors = len(broken_links) + len(broken_imgs) + len(relative_dots)

    print(f"\n📊 Audit Summary:")
    print(f"   - Scanned HTML Pages: {len(html_files)}")
    print(f"   - Broken Internal Links: {sum(len(v) for v in broken_links.values())} across {len(broken_links)} files")
    print(f"   - Missing Assets (img/js): {sum(len(v) for v in broken_imgs.values())} across {len(broken_imgs)} files")
    print(f"   - Relative Dot Links in Blogs: {sum(len(v) for v in relative_dots.values())} across {len(relative_dots)} files")

    if total_errors > 0:
        print("\n❌ Errors Found:")
        for f, blist in broken_links.items():
            print(f"   [BROKEN LINK] {f}:")
            for link, reason in blist:
                print(f"      {link} -> {reason}")
        for f, blist in broken_imgs.items():
            print(f"   [MISSING ASSET] {f}:")
            for img, reason in blist:
                print(f"      {img} -> {reason}")
        for f, dots in relative_dots.items():
            print(f"   [RELATIVE DOT] {f}: {len(dots)} occurrences")
        sys.exit(1)
    else:
        print("\n✅ All internal links, assets, and blog paths are 100% healthy! Passed.")
        sys.exit(0)

if __name__ == '__main__':
    run_audit()
