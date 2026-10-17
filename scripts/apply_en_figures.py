#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Apply English figures to blog/european-hydrogen-water-cases-en.html, blog/index.html,
and 08_英文博客与国际发布稿_EN.md.
"""

import re

# 1. Update blog/european-hydrogen-water-cases-en.html
with open('blog/european-hydrogen-water-cases-en.html', 'r', encoding='utf-8') as f:
    en_html = f.read()

replacements = [
    ('/assets/images/blog/european-hydrogen-water-cases/fig5-cover.png', '/assets/images/blog/european-hydrogen-water-cases/fig5-cover-en.png'),
    ('/assets/images/blog/european-hydrogen-water-cases/fig1-case-comparison-table.png', '/assets/images/blog/european-hydrogen-water-cases/fig1-case-comparison-table-en.png'),
    ('/assets/images/blog/european-hydrogen-water-cases/fig2-four-endpoints-grid.png', '/assets/images/blog/european-hydrogen-water-cases/fig2-four-endpoints-grid-en.png'),
    ('/assets/images/blog/european-hydrogen-water-cases/fig3-0-6-percent-axis.png', '/assets/images/blog/european-hydrogen-water-cases/fig3-0-6-percent-axis-en.png'),
    ('/assets/images/blog/european-hydrogen-water-cases/fig4-two-cases-timeline.png', '/assets/images/blog/european-hydrogen-water-cases/fig4-two-cases-timeline-en.png'),
]

for old, new in replacements:
    en_html = en_html.replace(old, new)

with open('blog/european-hydrogen-water-cases-en.html', 'w', encoding='utf-8') as f:
    f.write(en_html)
print("✓ Updated blog/european-hydrogen-water-cases-en.html")

# 2. Update blog/index.html
with open('blog/index.html', 'r', encoding='utf-8') as f:
    idx_html = f.read()

idx_html = idx_html.replace(
    '/assets/images/blog/european-hydrogen-water-cases/fig5-cover.png',
    '/assets/images/blog/european-hydrogen-water-cases/fig5-cover-en.png'
)

with open('blog/index.html', 'w', encoding='utf-8') as f:
    f.write(idx_html)
print("✓ Updated blog/index.html")

# 3. Update 08_英文博客与国际发布稿_EN.md
md_path = '/Users/martin/Documents/2026 BUSINESS MTRIX /20260601 MQ TECH 国际业务/20260708 MQ TECH 国际市场市场划分/欧洲氢医学学术圈/发布包_20261017_氢水两个欧洲案例/08_英文博客与国际发布稿_EN.md'
with open(md_path, 'r', encoding='utf-8') as f:
    md_content = f.read()

md_replacements = [
    ('fig5-cover.png', 'fig5-cover-en.png'),
    ('fig1-case-comparison-table.png', 'fig1-case-comparison-table-en.png'),
    ('fig2-four-endpoints-grid.png', 'fig2-four-endpoints-grid-en.png'),
    ('fig3-0-6-percent-axis.png', 'fig3-0-6-percent-axis-en.png'),
    ('fig4-two-cases-timeline.png', 'fig4-two-cases-timeline-en.png'),
]

for old, new in md_replacements:
    md_content = md_content.replace(old, new)

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(md_content)
print("✓ Updated 08_英文博客与国际发布稿_EN.md")
