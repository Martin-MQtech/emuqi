#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MUQI Tech — Chinese Search Engines & AI Submission Tool.

Credentials are read from environment variables or command-line options.
Never commit API tokens to this repository.
"""

import argparse
import json
import os
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP_PATH = os.path.join(BASE_DIR, "sitemap.xml")
DEFAULT_BAIDU_SITE = "https://www.emuqi.com"
INDEXNOW_KEY = "531ba2233ce04366bbfc10fa232651b5"

PRIORITY_CHINESE_URLS = [
    "https://www.emuqi.com/zh/blog/solid-state-hydrogen-foot-spa-consumables.html",
    "https://www.emuqi.com/zh/blog/",
    "https://www.emuqi.com/zh/",
    "https://www.emuqi.com/zh/solid-state-hydrogen-vs-pem-electrolysis.html",
    "https://www.emuqi.com/zh/blog/solid-state-hydrogen-facial-steamer-upgrade.html",
    "https://www.emuqi.com/zh/blog/sac-tc621-national-antimicrobial-standard-committee.html",
    "https://www.emuqi.com/zh/blog/hydrogen-water-plant-protein-green-modification.html",
    "https://www.emuqi.com/zh/blog/hydrogen-water-technology-comparison.html",
    "https://www.emuqi.com/zh/blog/gary-brecka-hydrogen-water-solid-state-breakthrough.html",
    "https://www.emuqi.com/zh/blog/antimicrobial-ceramic-balls-home-appliances-icr-technology.html",
    "https://www.emuqi.com/h2-wellness-hub/zh/",
    "https://www.emuqi.com/product-functional-ceramic-materials.html",
]


def get_sitemap_urls():
    if not os.path.exists(SITEMAP_PATH):
        return []
    tree = ET.parse(SITEMAP_PATH)
    root = tree.getroot()
    namespace = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = []
    for entry in root.findall("ns:url", namespace):
        location = entry.find("ns:loc", namespace)
        if location is not None and location.text:
            urls.append(location.text.strip())
    return urls


def push_to_baidu(token=None, urls=None, site=DEFAULT_BAIDU_SITE):
    token = (token or os.environ.get("BAIDU_PUSH_TOKEN", "")).strip()
    if not token:
        print("[Baidu] BAIDU_PUSH_TOKEN is not configured; skipping API submission.")
        print("Set BAIDU_PUSH_TOKEN or pass --baidu-token.")
        return False

    target_urls = urls or PRIORITY_CHINESE_URLS
    query = urllib.parse.urlencode({"site": site, "token": token})
    api_url = "http://data.zz.baidu.com/urls?" + query
    request = urllib.request.Request(
        api_url,
        data="\n".join(target_urls).encode("utf-8"),
        headers={"Content-Type": "text/plain", "User-Agent": "curl/7.68.0"},
    )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            result = json.loads(response.read().decode("utf-8"))
        print("[Baidu] HTTP", response.status)
        print("Submitted:", result.get("success", 0))
        print("Remaining today:", result.get("remain", 0))
        return True
    except urllib.error.HTTPError as exc:
        print("[Baidu] HTTP", exc.code, exc.read().decode("utf-8", errors="ignore"))
        return False
    except Exception as exc:
        print("[Baidu] Request failed:", exc)
        return False


def push_to_indexnow(urls=None):
    host = "www.emuqi.com"
    key_location = f"https://{host}/{INDEXNOW_KEY}.txt"
    target_urls = urls or get_sitemap_urls()
    payload = {
        "host": host,
        "key": INDEXNOW_KEY,
        "keyLocation": key_location,
        "urlList": target_urls,
    }
    request = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "IndexNow-MUQI-Tech/1.0",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            print("[IndexNow] HTTP", response.status, "URLs:", len(target_urls))
        return True
    except Exception as exc:
        print("[IndexNow] Submission failed:", exc)
        return False


def print_manual_submission_guide():
    print("=" * 70)
    print("Chinese search engines and AI platforms — manual submission guide")
    print("=" * 70)
    print("1. Baidu Webmaster: https://ziyuan.baidu.com")
    print("   Sitemap: https://www.emuqi.com/sitemap.xml")
    print("   API token: set BAIDU_PUSH_TOKEN; never store it in source control.")
    print("2. 360 Webmaster: https://zhanzhang.so.com")
    print("3. Sogou Webmaster: https://zhanzhang.sogou.com")
    print("4. ByteDance/Toutiao: https://zhanzhang.toutiao.com")
    print("5. Alibaba Shenma: https://zhanzhang.sm.cn")
    print("=" * 70)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="MUQI Tech Chinese Search Engines Submission Tool"
    )
    parser.add_argument("--baidu-token", help="Baidu API token (prefer BAIDU_PUSH_TOKEN)")
    parser.add_argument("--indexnow-only", action="store_true", help="Only submit IndexNow")
    parser.add_argument("--guide", action="store_true", help="Show manual submission guide")
    args = parser.parse_args()

    if args.guide:
        print_manual_submission_guide()
        raise SystemExit(0)

    print("Starting Chinese search engine and AI index submission...")
    indexnow_ok = push_to_indexnow(PRIORITY_CHINESE_URLS)
    baidu_ok = True
    if not args.indexnow_only:
        baidu_ok = push_to_baidu(token=args.baidu_token, urls=PRIORITY_CHINESE_URLS)
    print_manual_submission_guide()
    raise SystemExit(0 if indexnow_ok and baidu_ok else 1)
