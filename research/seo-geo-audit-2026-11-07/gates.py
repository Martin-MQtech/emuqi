#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""emuqi.com V2.0 刚性验收门禁 (2026-11-07) — 退出码 0 = 可交付
复跑: python3 research/seo-geo-audit-2026-11-07/gates.py
"""
import re, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SKIP = ('/templates/', '/scripts/', '/distribution_packages/', '/.git/', '/.freebuff/', '/emuqi/', '/research/')
VERIFY_FILES = ('baidu_verify_codeva-DhmQrr2FTg.html', 'baidu_verify_codeva-K8eoRfjsrG.html',
                'ByteDanceVerify.html', 'sogousiteverification.txt', '531ba2233ce04366bbfc10fa232651b5.txt')
INTENTIONAL_NO_H1 = {'h2report/reader/index.html'}          # 11-04 定性: 交互式阅读器
NO_SITEMAP_OK = {'h2report/reader'}                         # 交互式阅读器不参与收录 (11-04 定性)
INTENTIONAL_NO_MAIN = set()
INTENTIONAL_CANON = {'blog-list-hydrogen-health.html',        # 存根/桥接页
                     'solid-state-hydrogen-vs-pem-electrolysis-zh.html', 'hub.html', '404.html',
                     'h2report/reader/index.html'}            # 11-04 定性: canonical 指向 /h2report/

files, pages = [], {}
for dp, dn, fn in os.walk(ROOT):
    if any(s in dp.replace(ROOT, '') + '/' for s in SKIP): continue
    for f in sorted(fn):
        if f.endswith('.html'):
            rel = os.path.relpath(os.path.join(dp, f), ROOT)
            files.append(rel)
            pages[rel] = open(os.path.join(dp, f), encoding='utf-8', errors='ignore').read()

def is_stub(doc):
    return len(doc) < 6500 or bool(re.search(r'http-equiv=["\']refresh|location\.replace', doc[:4000], re.I))
def is_real(rel):
    return rel not in VERIFY_FILES and not is_stub(pages[rel]) and not rel.startswith('emuqi/')

real = [r for r in files if is_real(r)]
issues = {}
def flag(k, v):
    issues.setdefault(k, []).append(v)

# IDs per page for fragment resolution
ids = {rel: set(re.findall(r'\bid=["\']([^"\']+)["\']', doc)) for rel, doc in pages.items()}
def resolve(rel, href):
    clean = href.split('?')[0].split('#')[0]
    frag = href.split('#')[1] if '#' in href else None
    if clean.startswith('/'):
        target = clean.lstrip('/')
    else:
        target = os.path.normpath(os.path.join(os.path.dirname(rel), clean)).lstrip('./')
    cands = [target, target + '.html', os.path.join(target, 'index.html'), target.rstrip('/') + '/index.html']
    found = None
    for c in cands:
        if c in pages: found = c; break
        if os.path.isfile(os.path.join(ROOT, c)): found = c; break
    return found, frag

# ---- G1 内链/资源死链 + G2 断裂锚点 + G3 空锚 ----
for rel in real:
    doc = pages[rel]
    for m in re.finditer(r'(?:href|src)=["\']([^"\']+)["\']', doc):
        href = m.group(1).strip()
        if not href or href.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', 'data:', '#')): continue
        found, frag = resolve(rel, href)
        if found is None:
            flag('G1 死链', f'{rel} -> {href[:80]}'); continue
        if frag and found in ids and frag not in ids.get(found, set()) and frag not in ids.get(rel, set()):
            flag('G2 断裂锚点', f'{rel} -> {href[:80]}')
    if re.search(r'href="#"[\s>]', doc):
        flag('G3 空锚 href=#', rel)

# ---- G4 <main> / G5 meta desc 唯一 / G6 canonical / G7 H1 ----
for rel in real:
    doc = pages[rel]
    if rel not in INTENTIONAL_NO_MAIN and not re.search(r'<main[\s>]', doc, re.I):
        flag('G4 缺<main>', rel)
    if rel not in INTENTIONAL_CANON:
        n_can = len(re.findall(r'rel=["\']canonical["\']|["\']canonical["\'][^>]*rel=', doc))
        if n_can != 1: flag('G6 canonical 数', f'{rel}: {n_can}')
    n_desc = len([t for t in re.findall(r'<meta\b[^>]*>', doc, re.I) if re.search(r'''name=["']description["']''', t, re.I)])
    if n_desc != 1: flag('G5 description 数', f'{rel}: {n_desc}')
    if rel not in INTENTIONAL_NO_H1:
        n_h1 = len(re.findall(r'<h1[\s>]', doc, re.I))
        if n_h1 != 1: flag('G7 H1 数', f'{rel}: {n_h1}')

# ---- G8 无名按钮 / G9 无标签输入 ----
for rel in real:
    doc = pages[rel]
    for m in re.finditer(r'<button\b([^>]*)>(.*?)</button>', doc, re.S):
        attrs, inner = m.group(1), re.sub(r'<[^>]+>', '', m.group(2)).strip()
        if not inner and 'aria-label' not in attrs and 'title=' not in attrs:
            flag('G8 无名按钮', f'{rel}: {attrs[:50]}')
    for m in re.finditer(r'<(input|select|textarea)\b([^>]*?)/?>', doc):
        tag, attrs = m.group(1).lower(), m.group(2)
        if re.search(r'type=["\'](?:hidden|submit|button)\b', attrs): continue
        if re.search(r'aria-hidden=["\']true["\']', attrs): continue
        if tag == 'input' and not re.search(r'type=|id=', attrs): continue
        iid = re.search(r'\bid=["\']([^"\']+)', attrs)
        has_label = bool(iid and re.search(r'for=["\']' + re.escape(iid.group(1)) + r'["\']', doc))
        if not has_label and 'aria-label' not in attrs:
            flag('G9 无标签输入', f'{rel}: {iid.group(1) if iid else tag}')

# ---- G10 img 尺寸 ----
for rel in real:
    doc = pages[rel]
    for m in re.finditer(r'<img\b[^>]*>', doc):
        tag = m.group(0)
        src = re.search(r'\bsrc=["\']([^"\']+)', tag)
        if src and src.group(1).startswith(('http://', 'https://', 'data:')): continue
        if re.search(r'\bsrc=["\']["\']', tag): continue  # JS 动态占位 (lightbox 等)
        if not (re.search(r'\swidth=["\']?[\d]', tag) and re.search(r'\sheight=["\']?[\d]', tag)):
            flag('G10 img 缺尺寸', f'{rel}: {src.group(1)[:60] if src else "?"}')

# ---- G11/G12 WebMCP+GA4 全覆盖 ----
for rel in real:
    doc = pages[rel]
    if 'script.js' not in doc and 'muqi-webmcp' not in doc:
        flag('G11 WebMCP 覆盖', rel)
    if 'script.js' not in doc and 'analytics.js' not in doc:
        flag('G12 GA4 覆盖', rel)

# ---- G13 虚假回执/假成功残留 ----
FAKE = ['MQ-RFQ-', 'RECEIVED_AND_COMMITTED', 'Inquiry received!', 'Direct notification forwarded',
        '48 hours" tracking', 'tracking number forwarded']
for rel in real + ['llms.txt', 'llms-full.txt']:
    doc = pages.get(rel) or (open(os.path.join(ROOT, rel), encoding='utf-8').read() if os.path.exists(os.path.join(ROOT, rel)) else '')
    for f in FAKE:
        if f in doc: flag('G13 虚假声明', f'{rel}: {f}')

# ---- G14 twitter:card 指定页 ----
for rel in ['facts/index.html', 'zh/facts/index.html',
            'blog/muqi-hydrogen-geo-facts-20-qa-en.html', 'zh/blog/muqi-hydrogen-geo-facts-20-qa.html']:
    if 'twitter:card' not in pages.get(rel, ''): flag('G14 缺 twitter:card', rel)

# ---- G15 og:image 文件存在 ----
og_done = set()
for rel in real:
    for m in re.finditer(r'<meta\b[^>]*>', pages[rel], re.I):
        tag = m.group(0)
        if not re.search(r'(?:property|name)=["\']og:image["\'](?![\w:-])', tag): continue
        mc = re.search(r'content=["\']([^"\']+)', tag)
        if not mc: continue
        u = mc.group(1).replace('https://www.emuqi.com/', '').split('?')[0]
        if u in og_done: continue
        og_done.add(u)
        if not os.path.isfile(os.path.join(ROOT, u)): flag('G15 og:image 404', u)

# ---- G16 微字号 ----
for rel in real + ['style.css']:
    doc = pages.get(rel) or open(os.path.join(ROOT, rel), encoding='utf-8').read()
    for m in re.findall(r'font-size:\s*([0-9.]+)px', doc):
        if float(m) < 11: flag('G16 <11px 字号', f'{rel}: {m}px'); break

# ---- G17 表格 overflow 包裹 ----
for rel in real:
    doc = pages[rel]
    for m in re.finditer(r'<table\b', doc):
        back = doc[max(0, m.start() - 400):m.start()]
        if 'overflow-x' not in back and 'overflow:auto' not in back and 'table-wrap' not in back:
            flag('G17 表格未包裹', rel); break

# ---- G18 标签配平 ----
for rel in real:
    doc = pages[rel]
    for t in ('div', 'main', 'article', 'table', 'section'):
        o = len(re.findall(rf'<{t}[\s>]', doc, re.I)); c = len(re.findall(rf'</{t}>', doc, re.I))
        if o != c: flag('G18 标签不配平', f'{rel}: {t} {o}/{c}')

# ---- G19 sitemap 双向 ----
sm = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
locs = set(re.findall(r'<loc>\s*(.*?)\s*</loc>', sm))
sm_paths = {u.replace('https://www.emuqi.com/', '').replace('.html', '').rstrip('/') for u in locs}
page_paths = set()
for rel in real:
    if rel == '404.html': continue
    p = rel.replace('.html', '')
    if p.endswith('/index') or p == 'index':
        p = p.replace('/index', '').replace('index', '')
    page_paths.add(p.rstrip('/'))
missing = {p for p in page_paths if p not in sm_paths and p not in NO_SITEMAP_OK}
for p in sorted(missing):
    if p: flag('G19 sitemap 缺页', p)

# ---- G20 表单 honeypot + GA4 语义 ----
for rel, fid in [('contact-mqtech-hydrogen-health.html', 'b2bInquiryForm'), ('index.html', 'homeRfqForm')]:
    doc = pages[rel]
    if 'mq-hp-field' not in doc: flag('G20 表单 honeypot', rel)
    seg = doc[doc.find(fid):]
    seg = seg[:seg.find('</form>')] if '</form>' in seg else seg
    if re.search(r'generate_lead', seg) and seg.find('generate_lead') < seg.find('mailto:'):
        flag('G20 GA4 先于发送', rel)

# ---- G21 canonical 自指 ----
for rel in real:
    if rel in INTENTIONAL_CANON: continue
    doc = pages[rel]
    m = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*>', doc, re.I) or re.search(r'<link[^>]*href=["\'][^"\']+["\'][^>]*rel=["\']canonical["\'][^>]*>', doc, re.I)
    if m:
        mh = re.search(r'href=["\']([^"\']+)', m.group(0))
        if mh:
            tgt = mh.group(1).replace('https://www.emuqi.com/', '').replace('.html', '').rstrip('/')
            base = rel.replace('.html', '')
            if base == 'facts/index': base = 'facts'
            if base == 'index' or base.endswith('/index'): base = base.replace('/index', '').replace('index', '').rstrip('/')
            if tgt != base and not tgt.endswith(rel):
                flag('G21 canonical 非自指', f'{rel} -> {tgt}')

# ---- 汇总 ----
total = sum(len(v) for v in issues.values())
print(f'=== V2.0 GATES :: {len(real)} real pages / {len(files)} html files ===')
if issues:
    for k in sorted(issues):
        print(f'\n[{k}] = {len(issues[k])}')
        for v in issues[k][:12]: print(f'   {v}')
        if len(issues[k]) > 12: print(f'   ... +{len(issues[k]) - 12} more')
else:
    print('ALL GATES ZERO')
print(f'\nTOTAL ISSUES: {total}')
sys.exit(1 if total else 0)
