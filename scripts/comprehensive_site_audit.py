import os
import re
import json
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote

ROOT_DIR = "/Users/martin/Documents/2026 BUSINESS MTRIX /20260721 MUQI 网站建设/emuqi"

report = {
    "total_html_files": 0,
    "broken_internal_links": [],
    "missing_images": [],
    "schema_issues": [],
    "language_mismatches": [],
    "navigation_issues": [],
    "canonical_hreflang_issues": []
}

html_files = []
for root, dirs, files in os.walk(ROOT_DIR):
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

report["total_html_files"] = len(html_files)

# Chinese character pattern
chinese_pattern = re.compile(r'[\u4e00-\u9fff]')

for file_path in html_files:
    rel_path = os.path.relpath(file_path, ROOT_DIR)
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    html_tag = soup.find("html")
    lang = html_tag.get("lang", "") if html_tag else ""

    # 1. Navigation / Blog button check
    # In English pages, does Blog point to blog-list-hydrogen-health.html or blog/index.html?
    nav_links = soup.find_all("a", href=True)
    for a in nav_links:
        href = a["href"].strip()
        text = a.get_text().strip()
        if text.lower() == "blog" and (lang.startswith("en") or not lang):
            if "blog-list-hydrogen-health.html" in href:
                report["navigation_issues"].append({
                    "file": rel_path,
                    "issue": f"English page top nav 'Blog' points to Chinese list '{href}' instead of 'blog/index.html'"
                })

    # 2. Check all <a href="..."> internal links
    for a in nav_links:
        href = a["href"].strip()
        if not href or href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:") or href.startswith("javascript:"):
            continue
        parsed = urlparse(href)
        # External links
        if parsed.scheme in ["http", "https"]:
            if parsed.netloc in ["emuqi.com", "www.emuqi.com"]:
                # Check internal equivalent
                target_path = parsed.path.lstrip("/")
                if not target_path or target_path.endswith("/"):
                    target_path += "index.html"
                disk_path = os.path.join(ROOT_DIR, target_path)
                if not os.path.exists(disk_path):
                    report["broken_internal_links"].append({
                        "file": rel_path,
                        "link": href,
                        "resolved_target": os.path.relpath(disk_path, ROOT_DIR)
                    })
            continue

        # Relative link
        link_target = unquote(parsed.path)
        if not link_target:
            continue
        if link_target.startswith("/"):
            disk_path = os.path.join(ROOT_DIR, link_target.lstrip("/"))
        else:
            current_dir = os.path.dirname(file_path)
            disk_path = os.path.normpath(os.path.join(current_dir, link_target))

        if os.path.isdir(disk_path):
            disk_path = os.path.join(disk_path, "index.html")

        if not os.path.exists(disk_path):
            report["broken_internal_links"].append({
                "file": rel_path,
                "link": href,
                "resolved_target": os.path.relpath(disk_path, ROOT_DIR) if disk_path.startswith(ROOT_DIR) else disk_path
            })

    # 3. Check all <img src="...">
    images = soup.find_all("img", src=True)
    for img in images:
        src = img["src"].strip()
        if not src or src.startswith("data:") or src.startswith("http://") or src.startswith("https://"):
            continue
        parsed = urlparse(src)
        img_target = unquote(parsed.path)
        if img_target.startswith("/"):
            disk_path = os.path.join(ROOT_DIR, img_target.lstrip("/"))
        else:
            current_dir = os.path.dirname(file_path)
            disk_path = os.path.normpath(os.path.join(current_dir, img_target))

        if not os.path.exists(disk_path):
            report["missing_images"].append({
                "file": rel_path,
                "img_src": src,
                "resolved_target": os.path.relpath(disk_path, ROOT_DIR) if disk_path.startswith(ROOT_DIR) else disk_path
            })

    # 4. Schema.org Validation
    ld_json_scripts = soup.find_all("script", type="application/ld+json")
    for script in ld_json_scripts:
        raw_json = script.string
        if raw_json:
            try:
                data = json.loads(raw_json)
                # Check for "Martin Liu" placeholder
                raw_str = json.dumps(data)
                if "Martin Liu" in raw_str:
                    report["schema_issues"].append({
                        "file": rel_path,
                        "issue": "Found 'Martin Liu' in JSON-LD schema (should be Martin Chen / Martin)"
                    })
            except Exception as e:
                report["schema_issues"].append({
                    "file": rel_path,
                    "issue": f"Invalid JSON-LD syntax: {str(e)}"
                })

    # 5. Language check: Stray Chinese in English pages
    if lang.startswith("en") or (not lang and not "zh" in rel_path and not "blog-list-hydrogen" in rel_path):
        # Look for stray Chinese in Header, Footer, and Meta Titles
        header = soup.find("header")
        if header and chinese_pattern.search(header.get_text()):
            # check what Chinese is in header
            zh_chars = "".join(chinese_pattern.findall(header.get_text()))
            report["language_mismatches"].append({
                "file": rel_path,
                "location": "header",
                "sample": zh_chars[:30]
            })

        footer = soup.find("footer")
        if footer and chinese_pattern.search(footer.get_text()):
            zh_chars = "".join(chinese_pattern.findall(footer.get_text()))
            report["language_mismatches"].append({
                "file": rel_path,
                "location": "footer",
                "sample": zh_chars[:30]
            })

with open("comprehensive_audit_result.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print(f"Audit Complete! Scanned {report['total_html_files']} HTML files.")
print(f"Broken Links: {len(report['broken_internal_links'])}")
print(f"Missing Images: {len(report['missing_images'])}")
print(f"Navigation Mismatches: {len(report['navigation_issues'])}")
print(f"Schema Issues: {len(report['schema_issues'])}")
print(f"Language Mismatches (English pages with Chinese text): {len(report['language_mismatches'])}")
