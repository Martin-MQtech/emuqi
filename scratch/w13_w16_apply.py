#!/usr/bin/env python3
"""W-13 (descriptive logo alt) + W-16 (hero preload) + asset version bump.
One idempotent pass over all *.html. Does NOT touch canonical/hreflang/head links.
"""
import re, pathlib, sys

ROOT = pathlib.Path('.').resolve()
HERO_BG = '/assets/images/hero-bg.png'
AGRI_HERO = '/assets/images/agriculture/hydrogen-agriculture-hero.jpg'
NEW_VER = '20261114'

stats = {'alt_fixed': 0, 'alt_files': 0, 'preload_added': 0, 'ver_bumped': 0,
         'hub_ver_bumped': 0, 'skipped_have_preload': 0, 'skipped_fetchpri': 0,
         'missing_file': []}
preload_log = []

BG_URL_RE = re.compile(r'background[^;}]*url\(\s*[\'"]?([^\'")]+)[\'"]?\s*\)')
IMG_ALT_RE = re.compile(r'(<img\b[^>]*?)alt="MUQI"')
HERO_CLASS_RE = re.compile(r'(^|\s)(hero|page-hero|agriculture-hero)(\s|$)')

def resolve(url: str, page: pathlib.Path):
    url = url.strip().strip('"\'')
    if not url or url.startswith('data:') or 'gradient' in url:
        return None
    if url.startswith('/'):
        p = ROOT / url.lstrip('/')
    else:
        p = (page.parent / url).resolve()
    return url if p.exists() else None

for page in sorted(ROOT.rglob('*.html')):
    rel = page.relative_to(ROOT)
    if any(part.startswith('.') for part in rel.parts):
        continue
    t = page.read_text(errors='ignore')
    orig = t

    # ---- W-13: descriptive alt for logo images ----
    t, n = IMG_ALT_RE.subn(r'\1alt="MUQI Tech logo"', t)
    if n:
        stats['alt_fixed'] += n
        stats['alt_files'] += 1

    # ---- W-16: preload for CSS-background heroes ----
    if 'rel="preload"' in t:
        stats['skipped_have_preload'] += 1
    elif 'fetchpriority' in t:
        stats['skipped_fetchpri'] += 1  # index.html: <img> hero already prioritized
    else:
        class_attrs = re.findall(r'class="([^"]+)"', t)
        hero_target = None
        for c in class_attrs:
            if HERO_CLASS_RE.search(c):
                hero_target = AGRI_HERO if 'agriculture-hero' in c else HERO_BG
                break
        href = None
        if hero_target and (ROOT / hero_target.lstrip('/')).exists():
            href = hero_target
            src = 'class:' + ('agri' if hero_target == AGRI_HERO else 'hero-bg')
        else:
            m = BG_URL_RE.search(t)
            if m:
                u = resolve(m.group(1), page)
                if u:
                    href, src = u, 'inline'
                else:
                    stats['missing_file'].append(f'{rel}: {m.group(1)[:60]}')
        if href:
            tag = f'<link rel="preload" as="image" href="{href}" fetchpriority="high">'
            t = t.replace('</head>', tag + '\n</head>', 1)
            stats['preload_added'] += 1
            preload_log.append(f'{rel} <- {href} [{src}]')

    # ---- version bumps (style.css / hub.css) ----
    t, n = re.subn(r'style\.css\?v=[0-9a-z]+', f'style.css?v={NEW_VER}', t)
    stats['ver_bumped'] += n
    t, n = re.subn(r'hub\.css\?v=[0-9a-z]+', f'hub.css?v={NEW_VER}', t)
    stats['hub_ver_bumped'] += n

    if t != orig:
        page.write_text(t)

print(stats)
print('--- preload targets ---')
for line in preload_log:
    print(' ', line)
