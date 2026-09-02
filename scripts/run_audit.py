import os
import re
import json
from pathlib import Path
from bs4 import BeautifulSoup
from collections import defaultdict

SITE_DIR = Path("/Users/martin/Documents/2026 BUSINESS MTRIX /20260721 MUQI 网站建设/emuqi")
OUTPUT_FILE = SITE_DIR / "scripts" / "deep_audit_report.json"

html_files = [p for p in SITE_DIR.rglob("*.html") if "node_modules" not in str(p)]

report = {
    "total_html_files": len(html_files),
    "seo_metrics": {
        "missing_title": [],
        "short_title": [],
        "long_title": [],
        "missing_description": [],
        "short_description": [],
        "long_description": [],
        "missing_canonical": [],
        "missing_hreflang": [],
        "missing_og_tags": [],
        "missing_twitter_card": [],
        "h1_issues": {
            "missing_h1": [],
            "multiple_h1": []
        },
        "images_missing_alt": []
    },
    "geo_ai_metrics": {
        "missing_json_ld": [],
        "invalid_json_ld": [],
        "has_faq_page": [],
        "has_organization": [],
        "has_article": [],
        "has_product": [],
        "schema_types_count": defaultdict(int),
        "llms_txt_status": {},
        "robots_txt_status": {}
    },
    "technical_metrics": {
        "broken_internal_links": [],
        "broken_internal_assets": [],
        "mailto_links_count": 0,
        "tel_links_count": 0,
        "external_links_without_noopener": [],
        "mixed_content_http": [],
        "missing_viewport": [],
        "missing_charset": [],
        "missing_favicon": []
    }
}

# 1. Check robots.txt & llms.txt
robots_path = SITE_DIR / "robots.txt"
if robots_path.exists():
    with open(robots_path, 'r', encoding='utf-8') as f:
        robots_content = f.read()
        report["geo_ai_metrics"]["robots_txt_status"] = {
            "exists": True,
            "has_sitemap": "sitemap:" in robots_content.lower(),
            "has_llms_txt": "llms.txt" in robots_content.lower(),
            "has_ai_crawlers": any(bot in robots_content for bot in ["GPTBot", "ClaudeBot", "PerplexityBot", "Applebot-Extended"])
        }
else:
    report["geo_ai_metrics"]["robots_txt_status"] = {"exists": False}

llms_path = SITE_DIR / "llms.txt"
if llms_path.exists():
    with open(llms_path, 'r', encoding='utf-8') as f:
        llms_content = f.read()
        report["geo_ai_metrics"]["llms_txt_status"] = {
            "exists": True,
            "char_count": len(llms_content),
            "line_count": len(llms_content.splitlines()),
            "mentions_muqi": "muqi" in llms_content.lower() or "emuqi" in llms_content.lower()
        }
else:
    report["geo_ai_metrics"]["llms_txt_status"] = {"exists": False}

# 2. Parse HTML files
all_html_paths = set(str(p.resolve()) for p in html_files)

for p in html_files:
    rel_path = str(p.relative_to(SITE_DIR))
    try:
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        continue

    soup = BeautifulSoup(content, 'html.parser')

    # Character set
    charset_tag = soup.find('meta', charset=True) or soup.find('meta', attrs={'http-equiv': re.compile(r'content-type', re.I)})
    if not charset_tag:
        report["technical_metrics"]["missing_charset"].append(rel_path)

    # Viewport
    viewport_tag = soup.find('meta', attrs={'name': re.compile(r'viewport', re.I)})
    if not viewport_tag:
        report["technical_metrics"]["missing_viewport"].append(rel_path)

    # Favicon
    favicon_tag = soup.find('link', rel=re.compile(r'icon', re.I))
    if not favicon_tag:
        report["technical_metrics"]["missing_favicon"].append(rel_path)

    # Title
    title_tag = soup.find('title')
    if not title_tag or not title_tag.get_text().strip():
        report["seo_metrics"]["missing_title"].append(rel_path)
    else:
        t_len = len(title_tag.get_text().strip())
        if t_len < 10:
            report["seo_metrics"]["short_title"].append({"file": rel_path, "title": title_tag.get_text().strip()})
        elif t_len > 70:
            report["seo_metrics"]["long_title"].append({"file": rel_path, "length": t_len})

    # Description
    desc_tag = soup.find('meta', attrs={'name': re.compile(r'description', re.I)})
    if not desc_tag or not desc_tag.get('content', '').strip():
        report["seo_metrics"]["missing_description"].append(rel_path)
    else:
        d_len = len(desc_tag.get('content', '').strip())
        if d_len < 50:
            report["seo_metrics"]["short_description"].append({"file": rel_path, "length": d_len})
        elif d_len > 170:
            report["seo_metrics"]["long_description"].append({"file": rel_path, "length": d_len})

    # Canonical
    canonical_tag = soup.find('link', rel='canonical')
    if not canonical_tag or not canonical_tag.get('href', '').strip():
        report["seo_metrics"]["missing_canonical"].append(rel_path)

    # Hreflang
    hreflangs = soup.find_all('link', rel='alternate', hreflang=True)
    if not hreflangs:
        report["seo_metrics"]["missing_hreflang"].append(rel_path)

    # OG Tags
    og_title = soup.find('meta', property='og:title')
    og_desc = soup.find('meta', property='og:description')
    og_image = soup.find('meta', property='og:image')
    if not (og_title and og_desc and og_image):
        report["seo_metrics"]["missing_og_tags"].append(rel_path)

    # Twitter Card
    twitter_card = soup.find('meta', attrs={'name': 'twitter:card'})
    if not twitter_card:
        report["seo_metrics"]["missing_twitter_card"].append(rel_path)

    # H1 check
    h1s = soup.find_all('h1')
    if len(h1s) == 0:
        report["seo_metrics"]["h1_issues"]["missing_h1"].append(rel_path)
    elif len(h1s) > 1:
        report["seo_metrics"]["h1_issues"]["multiple_h1"].append({"file": rel_path, "count": len(h1s)})

    # Images missing alt
    for img in soup.find_all('img'):
        src = img.get('src', '')
        alt = img.get('alt', None)
        if alt is None or not alt.strip():
            report["seo_metrics"]["images_missing_alt"].append({"file": rel_path, "src": src})

    # JSON-LD Schemas
    json_lds = soup.find_all('script', type='application/ld+json')
    if not json_lds:
        report["geo_ai_metrics"]["missing_json_ld"].append(rel_path)
    else:
        for s in json_lds:
            text = s.string or s.get_text()
            if not text:
                continue
            try:
                data = json.loads(text)
                items = data if isinstance(data, list) else [data]
                for item in items:
                    stype = item.get('@type', 'Unknown')
                    if isinstance(stype, list):
                        for st in stype:
                            report["geo_ai_metrics"]["schema_types_count"][st] += 1
                    else:
                        report["geo_ai_metrics"]["schema_types_count"][stype] += 1

                    if stype == "FAQPage" or (isinstance(stype, list) and "FAQPage" in stype):
                        report["geo_ai_metrics"]["has_faq_page"].append(rel_path)
                    if stype == "Organization" or (isinstance(stype, list) and "Organization" in stype):
                        report["geo_ai_metrics"]["has_organization"].append(rel_path)
                    if stype in ["Article", "BlogPosting", "TechArticle"]:
                        report["geo_ai_metrics"]["has_article"].append(rel_path)
                    if stype in ["Product", "IndividualProduct"]:
                        report["geo_ai_metrics"]["has_product"].append(rel_path)
            except Exception as ex:
                report["geo_ai_metrics"]["invalid_json_ld"].append({"file": rel_path, "error": str(ex)})

    # Internal links and Assets
    for a in soup.find_all('a', href=True):
        href = a['href'].strip()
        if href.startswith('mailto:'):
            report["technical_metrics"]["mailto_links_count"] += 1
            continue
        if href.startswith('tel:'):
            report["technical_metrics"]["tel_links_count"] += 1
            continue
        if href.startswith('#') or href.startswith('javascript:'):
            continue
        if href.startswith('http://') or href.startswith('https://'):
            if 'emuqi.com' not in href and '127.0.0.1' not in href and 'localhost' not in href:
                target = a.get('target', '')
                rel = a.get('rel', '')
                if target == '_blank' and 'noopener' not in rel:
                    report["technical_metrics"]["external_links_without_noopener"].append({"file": rel_path, "href": href})
                continue
            # Internal absolute link
            # Extract URL path without domain
            m = re.match(r'https?://(?:www\.)?emuqi\.com(/.*)?', href)
            if m:
                path_part = m.group(1) or '/'
                href = path_part
            else:
                continue

        # Check relative link existence
        clean_target = href.split('?')[0].split('#')[0]
        if not clean_target:
            continue
        if clean_target.startswith('/'):
            target_file = SITE_DIR / clean_target.lstrip('/')
        else:
            target_file = (p.parent / clean_target).resolve()

        if target_file.is_dir():
            target_file = target_file / 'index.html'

        if not target_file.exists():
            report["technical_metrics"]["broken_internal_links"].append({
                "source": rel_path,
                "target": href,
                "resolved": str(target_file)
            })

    # Assets (img, script, link)
    for tag, attr in [('img', 'src'), ('script', 'src'), ('link', 'href')]:
        for el in soup.find_all(tag, attrs={attr: True}):
            val = el[attr].strip()
            if val.startswith('data:') or val.startswith('http://') or val.startswith('https://') or val.startswith('//') or val.startswith('#'):
                if val.startswith('http://'):
                    report["technical_metrics"]["mixed_content_http"].append({"file": rel_path, "url": val})
                continue
            clean_asset = val.split('?')[0].split('#')[0]
            if not clean_asset:
                continue
            if clean_asset.startswith('/'):
                asset_file = SITE_DIR / clean_asset.lstrip('/')
            else:
                asset_file = (p.parent / clean_asset).resolve()
            if not asset_file.exists():
                report["technical_metrics"]["broken_internal_assets"].append({
                    "source": rel_path,
                    "tag": tag,
                    "asset": val
                })

# Convert defaultdict to regular dict
report["geo_ai_metrics"]["schema_types_count"] = dict(report["geo_ai_metrics"]["schema_types_count"])

# De-duplicate lists
report["seo_metrics"]["missing_og_tags"] = list(set(report["seo_metrics"]["missing_og_tags"]))
report["seo_metrics"]["missing_twitter_card"] = list(set(report["seo_metrics"]["missing_twitter_card"]))
report["geo_ai_metrics"]["has_faq_page"] = list(set(report["geo_ai_metrics"]["has_faq_page"]))
report["geo_ai_metrics"]["has_organization"] = list(set(report["geo_ai_metrics"]["has_organization"]))
report["geo_ai_metrics"]["has_article"] = list(set(report["geo_ai_metrics"]["has_article"]))
report["geo_ai_metrics"]["has_product"] = list(set(report["geo_ai_metrics"]["has_product"]))

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print(f"Deep Audit complete. Results saved to {OUTPUT_FILE}")
print(f"Total HTML: {report['total_html_files']}")
print(f"Missing Canonical: {len(report['seo_metrics']['missing_canonical'])}")
print(f"Missing Hreflang: {len(report['seo_metrics']['missing_hreflang'])}")
print(f"Missing Title: {len(report['seo_metrics']['missing_title'])}")
print(f"Missing Description: {len(report['seo_metrics']['missing_description'])}")
print(f"Missing H1: {len(report['seo_metrics']['h1_issues']['missing_h1'])}")
print(f"Multiple H1: {len(report['seo_metrics']['h1_issues']['multiple_h1'])}")
print(f"Images Missing Alt: {len(report['seo_metrics']['images_missing_alt'])}")
print(f"Missing JSON-LD: {len(report['geo_ai_metrics']['missing_json_ld'])}")
print(f"Invalid JSON-LD: {len(report['geo_ai_metrics']['invalid_json_ld'])}")
print(f"Broken Internal Links: {len(report['technical_metrics']['broken_internal_links'])}")
print(f"Broken Internal Assets: {len(report['technical_metrics']['broken_internal_assets'])}")
