#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Submit all production URLs to Bing, Yandex, Naver, and Seznam via the IndexNow API.
Key location: https://www.emuqi.com/531ba2233ce04366bbfc10fa232651b5.txt
"""

import os
import json
import urllib.request
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP_PATH = os.path.join(BASE_DIR, "sitemap.xml")
KEY = "531ba2233ce04366bbfc10fa232651b5"
HOST = "www.emuqi.com"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

def get_sitemap_urls():
    tree = ET.parse(SITEMAP_PATH)
    root = tree.getroot()
    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = []
    for u in root.findall('ns:url', ns):
        loc = u.find('ns:loc', ns)
        if loc is not None and loc.text:
            urls.append(loc.text.strip())
    return urls

def submit_indexnow(endpoint_name, endpoint_url, urls):
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        endpoint_url,
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "IndexNow-MUQI-Tech/1.0"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print(f"[{endpoint_name}] HTTP {resp.status} {resp.reason}")
            return resp.status
    except urllib.error.HTTPError as e:
        print(f"[{endpoint_name}] HTTPError: {e.code} {e.reason} - {e.read().decode('utf-8', errors='ignore')}")
        return e.code
    except Exception as e:
        print(f"[{endpoint_name}] Failed: {e}")
        return None

if __name__ == "__main__":
    urls = get_sitemap_urls()
    print(f"Loaded {len(urls)} URLs from {SITEMAP_PATH}")
    
    endpoints = [
        ("IndexNow Official Hub", "https://api.indexnow.org/indexnow"),
        ("Microsoft Bing", "https://www.bing.com/indexnow")
    ]
    
    for name, url in endpoints:
        print(f"Submitting {len(urls)} URLs to {name} ({url})...")
        submit_indexnow(name, url, urls)
