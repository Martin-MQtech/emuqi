#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multi-channel distribution script for MUQI Solid-State Hydrogen Foot Spa Consumables
Handles WordPress.com API publishing, IndexNow search engine push, and asset bundling.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WP_PUBLISHER_PATH = "/Users/martin/Documents/2026 BUSINESS MTRIX /20260601 MQ TECH 国际业务/20260708 MQ TECH 国际市场市场划分/wp_publisher.py"

def publish_wordpress():
    if not os.path.exists(WP_PUBLISHER_PATH):
        print(f"[-] wp_publisher.py not found at {WP_PUBLISHER_PATH}")
        return None
    sys.path.insert(0, os.path.dirname(WP_PUBLISHER_PATH))
    import wp_publisher

    title = "Beyond Commoditized Foot Baths: How Solid-State Hydrogen Consumables Unlock a High-Margin 'Razor & Blades' Model"
    content_path = os.path.join(BASE_DIR, "distribution_packages", "foot_spa_consumables", "01_WordPress", "post_content.html")
    with open(content_path, "r", encoding="utf-8") as f:
        content = f.read()

    categories = ["Hydrogen Technology", "Wellness Hardware OEM", "Solid-State Hydrogen"]
    tags = ["Solid-State Hydrogen", "Foot Spa Equipment", "Razor and Blades Model", "Molecular Hydrogen", "MUQI Tech", "Martin Chen", "SAC/TC621"]

    print("\n🚀 Connecting to WordPress.com (h2welltech.wordpress.com)...")
    post_url = wp_publisher.publish_via_api(title, content, categories, tags, publish_now=True)
    return post_url

if __name__ == "__main__":
    url = publish_wordpress()
    if url:
        print(f"🎉 Live URL: {url}")
