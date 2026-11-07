#!/usr/bin/env python3
"""
verify_blog_chronological_order.py
Strict Automated Chronological Order Hard Gate for MUQI Official Blogs
Ensures all blog post cards in both zh/blog/index.html and blog/index.html
are strictly monotonic descending by publication date.
Fails with non-zero exit code if any date is out of order, missing, or duplicated.
"""

import os
import sys
import re
from datetime import datetime
from bs4 import BeautifulSoup

def verify_file(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}", file=sys.stderr)
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    grid = soup.find("div", class_="blog-grid") or soup.find(
        "div", style=lambda s: s and ("grid-template-columns" in s or "display:grid" in s)
    )
    if not grid:
        print(f"❌ Could not find blog grid container in {file_path}", file=sys.stderr)
        return False

    cards = grid.find_all("a", recursive=False)
    if not cards:
        print(f"❌ No blog cards found in {file_path}", file=sys.stderr)
        return False

    month_map = {
        "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
        "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
        "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
        "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12
    }

    parsed = []
    seen_hrefs = set()

    for idx, card in enumerate(cards, start=1):
        href = card.get("href", "").strip()
        h3 = card.find("h3")
        title = h3.get_text(strip=True) if h3 else "Untitled"
        text = " ".join(card.stripped_strings)

        # Check duplicate href
        if href in seen_hrefs:
            print(f"❌ Duplicate blog card detected at Slot {idx}: {href}", file=sys.stderr)
            return False
        seen_hrefs.add(href)

        # 1. Chinese format: 2026年11月5日
        m_zh = re.search(r"(\d{4})年(\d{1,2})月(\d{1,2})日", text)
        if m_zh:
            d = datetime(int(m_zh.group(1)), int(m_zh.group(2)), int(m_zh.group(3))).date()
            parsed.append((d, title, href, idx))
            continue

        # 2. English format: Nov 5, 2026 or November 3, 2026 or Oct 17, 2026
        m_en = re.search(r"([A-Za-z]+)\s+(\d{1,2}),?\s+(\d{4})", text)
        if m_en and m_en.group(1).lower() in month_map:
            month = month_map[m_en.group(1).lower()]
            d = datetime(int(m_en.group(3)), month, int(m_en.group(2))).date()
            parsed.append((d, title, href, idx))
            continue

        # 3. ISO format: 2026-11-05
        m_iso = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
        if m_iso:
            d = datetime(int(m_iso.group(1)), int(m_iso.group(2)), int(m_iso.group(3))).date()
            parsed.append((d, title, href, idx))
            continue

        print(f"❌ Slot {idx} has NO identifiable publication date: {title} ({href})", file=sys.stderr)
        return False

    # Assert monotonic descending ordering
    has_error = False
    for i in range(len(parsed) - 1):
        d_curr, t_curr, h_curr, idx_curr = parsed[i]
        d_next, t_next, h_next, idx_next = parsed[i + 1]

        if d_curr < d_next:
            print(
                f"❌ CHRONOLOGICAL ORDER VIOLATION in {file_path}:\n"
                f"   Slot {idx_curr} [{d_curr}] '{t_curr[:35]}' ({h_curr})\n"
                f"   is OLDER than following Slot {idx_next} [{d_next}] '{t_next[:35]}' ({h_next})",
                file=sys.stderr
            )
            has_error = True

    if has_error:
        return False

    print(f"✅ {file_path}: All {len(parsed)} cards strictly verified in monotonic descending date order!")
    return True

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    zh_blog = os.path.join(root, "zh", "blog", "index.html")
    en_blog = os.path.join(root, "blog", "index.html")

    success_zh = verify_file(zh_blog)
    success_en = verify_file(en_blog)

    if not (success_zh and success_en):
        print("\n❌ CI/CD GATE FAILED: Blog order validation did not pass.", file=sys.stderr)
        sys.exit(1)

    print("\n🎉 ALL BLOG MATRICES PASSED CHRONOLOGICAL ORDER GATE!")
    sys.exit(0)

if __name__ == "__main__":
    main()
