#!/usr/bin/env python3
import os
import glob
import json
import re
from bs4 import BeautifulSoup

def audit_file(filepath):
    issues = []
    warnings = []
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # 1. HTML lang
    html_tag = soup.find('html')
    if not html_tag or not html_tag.get('lang'):
        issues.append('Missing <html lang="...">')

    # 2. Title
    title_tag = soup.find('title')
    if not title_tag or not title_tag.text.strip():
        issues.append('Missing or empty <title>')
    else:
        title_len = len(title_tag.text.strip())
        if title_len < 15 or title_len > 95:
            warnings.append(f'Title length ({title_len}) outside standard range (15-90)')

    # 3. Meta Description
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if not meta_desc or not meta_desc.get('content', '').strip():
        issues.append('Missing or empty <meta name="description">')

    # 4. Canonical
    canonical = soup.find('link', rel='canonical')
    if not canonical or not canonical.get('href', '').strip():
        issues.append('Missing <link rel="canonical">')
    else:
        href = canonical.get('href')
        if not href.startswith('https://www.emuqi.com/'):
            issues.append(f'Canonical href ({href}) does not start with https://www.emuqi.com/')
        if '?' in href:
            issues.append(f'Canonical href ({href}) contains query params')

    # 5. H1 check
    h1s = soup.find_all('h1')
    if len(h1s) == 0:
        issues.append('Missing <h1>')
    elif len(h1s) > 1:
        issues.append(f'Multiple <h1> tags found ({len(h1s)})')

    # 6. OpenGraph check
    og_title = soup.find('meta', property='og:title')
    og_desc = soup.find('meta', property='og:description')
    if not og_title:
        warnings.append('Missing og:title')
    if not og_desc:
        warnings.append('Missing og:description')

    # 7. Schema.org / JSON-LD check (GEO)
    json_ld_scripts = soup.find_all('script', type='application/ld+json')
    if len(json_ld_scripts) == 0:
        warnings.append('Missing Schema.org JSON-LD structured data')
    else:
        for idx, s in enumerate(json_ld_scripts):
            try:
                data = json.loads(s.string)
            except Exception as e:
                issues.append(f'Invalid JSON-LD syntax in script #{idx+1}: {e}')

    # 8. WebMCP / Script relative paths check (AEO)
    scripts = soup.find_all('script', src=True)
    for sc in scripts:
        src = sc['src']
        depth = filepath.count('/') - 1
        if depth > 0 and (src.startswith('assets/') or src == 'script.js' or src == 'style.css'):
            issues.append(f'Potentially broken relative asset path: {src} in depth {depth}')

    # 9. AEO checks for blog articles (/blog/...)
    if '/blog/' in filepath and not filepath.endswith('/blog/index.html'):
        # Check TL;DR
        tldr = soup.find('aside', class_='tl-dr') or soup.find('div', class_='tl-dr') or soup.find('div', class_='article-tldr') or soup.find(class_=re.compile(r'tldr|direct-answer', re.I))
        if not tldr:
            warnings.append('AEO: Missing TL;DR / Direct Answer box in blog article')
        
        # Check citations or data callout
        citations = soup.find_all(attrs={'data-citation': True}) or soup.find_all(class_=re.compile(r'data-card|citation-card|metric-card', re.I))
        if not citations:
            warnings.append('AEO: Missing data-citation / metric cards in blog article')

    return issues, warnings

def main():
    html_files = [f for f in glob.glob('./**/*.html', recursive=True) if not f.startswith('./scripts/.cache') and not f.startswith('./templates')]
    html_files.sort()
    
    total = len(html_files)
    clean_count = 0
    issue_count = 0
    warning_count = 0
    
    print(f'=== Starting Full SEO / GEO / AEO Quality Audit on {total} HTML pages ===\n')
    
    reports = {}
    for fp in html_files:
        issues, warnings = audit_file(fp)
        if issues or warnings:
            reports[fp] = {'issues': issues, 'warnings': warnings}
            if issues:
                issue_count += 1
            if warnings:
                warning_count += 1
        else:
            clean_count += 1

    print(f'Audit Summary: {clean_count}/{total} pages 100% clean. Issues in {issue_count} pages, Warnings in {warning_count} pages.\n')
    
    for fp, res in reports.items():
        if res['issues']:
            print(f'🔴 [ISSUES] {fp}:')
            for iss in res['issues']:
                print(f'   - {iss}')
        if res['warnings']:
            print(f'🟡 [WARNINGS] {fp}:')
            for w in res['warnings']:
                print(f'   - {w}')
        if res['issues'] or res['warnings']:
            print()

if __name__ == '__main__':
    main()
