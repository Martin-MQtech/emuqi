#!/usr/bin/env python3
"""
MUQI Tech (emuqi.com) Blog Header & Footer Unification Script
Ensures all Chinese (zh/blog/*.html) and English (blog/*-en.html) blog posts
strictly conform to the canonical silver metallic gradient Header and 5-column navy Footer.
"""

import os
import glob
import re

def unify_blogs():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, '..'))
    zh_blog_dir = os.path.join(base_dir, 'zh', 'blog')
    en_blog_dir = os.path.join(base_dir, 'blog')

    with open(os.path.join(base_dir, 'templates', 'canonical_header_zh.html'), 'r', encoding='utf-8') as f:
        tpl_header_zh = f.read()

    with open(os.path.join(base_dir, 'templates', 'canonical_footer_zh.html'), 'r', encoding='utf-8') as f:
        tpl_footer_zh = f.read()

    with open(os.path.join(base_dir, 'templates', 'canonical_header_en.html'), 'r', encoding='utf-8') as f:
        tpl_header_en = f.read()

    with open(os.path.join(base_dir, 'templates', 'canonical_footer_en.html'), 'r', encoding='utf-8') as f:
        tpl_footer_en = f.read()

    # 1. Process Chinese Blog Articles
    zh_files = glob.glob(os.path.join(zh_blog_dir, '*.html'))
    for filepath in zh_files:
        fname = os.path.basename(filepath)
        if fname == 'index.html':
            continue
        slug = fname[:-5]
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix legacy path deviations
        content = content.replace('/hydrogen-infused-membrane-dressings-womens-health.html', '/zh/blog/hydrogen-infused-membrane-dressings-womens-health.html')
        content = content.replace('/hydrogen-water-technology-comparison.html', '/zh/blog/hydrogen-water-technology-comparison.html')
        content = re.sub(r'href=[\"\']\./?[\"\']', 'href=\"/zh/\"', content)
        content = content.replace('https://www.instagram.com/', 'https://www.linkedin.com/company/72043164')

        # Matching English URL
        en_target = f'/blog/{slug}-en.html'
        if not os.path.exists(os.path.join(en_blog_dir, f'{slug}-en.html')):
            en_target = '/blog/index.html'

        curr_header = tpl_header_zh.replace('{EN_URL}', en_target)

        # Surgical Header & Footer Replacement
        content = re.sub(r'<header.*?</header>', curr_header, content, flags=re.DOTALL)
        content = re.sub(r'<footer.*?</footer>', tpl_footer_zh, content, flags=re.DOTALL)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    # 2. Process English Blog Articles
    en_files = glob.glob(os.path.join(en_blog_dir, '*-en.html'))
    for filepath in en_files:
        fname = os.path.basename(filepath)
        slug = fname[:-8]
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        zh_target = f'/zh/blog/{slug}.html'
        if not os.path.exists(os.path.join(zh_blog_dir, f'{slug}.html')):
            zh_target = '/zh/blog/index.html'

        content = re.sub(r'href=[\"\']\./?[\"\']', 'href=\"/\"', content)
        content = content.replace('https://www.instagram.com/', 'https://www.linkedin.com/company/72043164')

        curr_header = tpl_header_en.replace('{ZH_URL}', zh_target)

        content = re.sub(r'<header.*?</header>', curr_header, content, flags=re.DOTALL)
        content = re.sub(r'<footer.*?</footer>', tpl_footer_en, content, flags=re.DOTALL)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    print("✅ All blog headers and footers synchronized with canonical templates.")

if __name__ == '__main__':
    unify_blogs()
