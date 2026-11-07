#!/usr/bin/env python3
"""MUQI emuqi 全站审计 V2 —— 适配 /zh/ 分支迁移后架构 (2026-11-04)"""
import os, re, json, glob
from pathlib import Path, PurePosixPath
from urllib.parse import urlparse, unquote

import sys
ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
SKIP_DIRS = ('templates/', 'node_modules/', '.github/')
STUB = re.compile(r'http-equiv=["\']refresh["\'][^>]*content=["\']\s*\d+\s*;\s*url=', re.I)

# ---- .htaccess 301 规则 (源路径 -> 目标) ----
HT = (ROOT / '.htaccess').read_text(encoding='utf-8', errors='ignore') if (ROOT / '.htaccess').exists() else ''
rules = {}
for m in re.finditer(r'RewriteRule\s+\^([^\s$]+)\$?\s+(/[^\s]+)\s+\[R=301', HT):
    src = '/' + m.group(1).replace(r'\.', '.').replace(r'\$', '')
    if src.endswith('\\'):
        src = src[:-1]
    rules[src] = m.group(2)
# prefix rule: ^zh/h2-wellness-hub/(.+)$ -> /h2-wellness-hub/zh/$1
PREFIX_RULES = [('/zh/h2-wellness-hub/', '/h2-wellness-hub/zh/')]

def redirect_target(rel):
    p = '/' + rel
    if p in rules:
        return rules[p]
    for pre, tgt in PREFIX_RULES:
        if p.startswith(pre):
            return tgt + p[len(pre):]
    return None

# ---- 收集文件 ----
ALL = sorted(Path(f) for f in glob.glob(str(ROOT / '**' / '*.html'), recursive=True))
FILES = [p for p in ALL if not any(s in str(p.relative_to(ROOT)) for s in SKIP_DIRS)]
DOCS = {p: p.read_text(encoding='utf-8', errors='ignore') for p in FILES}

def rel_of(p): return p.relative_to(ROOT).as_posix()
DISALLOWED = ('templates/', 'distribution_packages/', 'scripts/', 'node_modules/')
def disallowed(rel): return rel.startswith(DISALLOWED)
def is_stub_page(p):
    d = DOCS[p]
    return bool(STUB.search(d[:4000])) and len(d) < 6000
def real_page(p):
    rel = rel_of(p)
    return not disallowed(rel) and not is_stub_page(p) and 'verify' not in rel.lower() and rel != '404.html'

def is_zh(rel): return rel == 'zh' or rel.startswith('zh/') or '/zh/' in '/' + rel
def cjk_count(t): return len(re.findall(r'[一-鿿]', t))

def visible(doc):
    t = re.sub(r'<script\b.*?</script>|<style\b.*?</style>|<head\b.*?</head>', '', doc, flags=re.S|re.I)
    t = re.sub(r'<[^>]+>', ' ', t)
    return t

out = {}
def log(sec, msg): out.setdefault(sec, []).append(msg)

# ================= A. 断链 / 指向 301 源的内链 =================
for p in FILES:
    rel = rel_of(p); base = p.parent
    for l in re.findall(r'(?:href|src)=["\']([^"\'#?]*)(?:[#?][^"\']*)?["\']', DOCS[p]):
        l = l.strip()
        if not l or l.startswith(('mailto:', 'tel:', 'javascript:', 'data:', '#')): continue
        pr = urlparse(l)
        if pr.scheme in ('http', 'https'):
            if 'emuqi.com' not in pr.netloc: continue
            path = unquote(pr.path)
        else:
            path = unquote(l)
            if not path: continue
            path = path if path.startswith('/') else PurePosixPath(base.relative_to(ROOT).as_posix(), path).as_posix()
        if path.endswith('/'): path = path + 'index.html'
        if not path.startswith('/'): path = '/' + path
        cand = [str(ROOT) + path, str(ROOT) + path + '.html', os.path.join(str(ROOT) + path, 'index.html')]
        if any(os.path.isfile(c) for c in cand): continue
        if redirect_target(path.lstrip('/')):   # 有 301 规则 -> 不算断链
            log('A2 内链指向301源(应改最终URL)', f'{rel} -> {l}')
            continue
        # webp rewrite 兜底
        if re.search(r'\.(jpe?g|png)$', path) and os.path.isfile(str(str(ROOT) + path).rsplit('.', 1)[0] + '.webp'): continue
        log('A 断链', f'{rel} -> {l}')

# ================= B. sitemap 双向 =================
sm = (ROOT / 'sitemap.xml').read_text(encoding='utf-8', errors='ignore')
urls = re.findall(r'<loc>\s*(.*?)\s*</loc>', sm)
in_sm = set()
for u in urls:
    path = unquote(urlparse(u).path)
    in_sm.add(path.lstrip('/'))
    if path.endswith('/'): in_sm.add(path.lstrip('/') + 'index.html')
    tgt = redirect_target(path.lstrip('/'))
    f = str(ROOT) + path
    ok = os.path.isfile(f) or os.path.isfile(str(f) + '.html') or os.path.isfile(os.path.join(str(f), 'index.html')) or tgt
    if not ok: log('B1 sitemap死URL', u)
for p in FILES:
    rel = rel_of(p)
    if rel in ('404.html',): continue
    if rel in in_sm or ( '/' + rel) in in_sm: continue
    stem = rel[:-5] if rel.endswith('.html') else rel
    if stem + '/' in in_sm or (rel == 'index.html') or (stem in in_sm): continue
    if real_page(p): log('B2 页面未收录sitemap', rel)

# ================= C. canonical / hreflang 落在 301 源 =================
for p in FILES:
    rel = rel_of(p); doc = DOCS[p]
    if STUB.search(doc[:3000]): continue
    for m in re.finditer(r'<link[^>]+rel=["\']canonical["\'][^>]*>', doc, re.I):
        h = re.search(r'href=["\']([^"\']+)', m.group(0))
        if h:
            path = urlparse(h.group(1)).path
            if redirect_target(path.lstrip('/')):
                log('C canonical指向301源', f'{rel} -> {h.group(1)}')
            if urlparse(h.group(1)).netloc not in ('www.emuqi.com',):
                log('C canonical主机非www', f'{rel} -> {h.group(1)}')
    for m in re.finditer(r'<link[^>]+rel=["\']alternate["\'][^>]+hreflang=["\']([^"\']+)["\'][^>]*>', doc, re.I):
        tag = m.group(1); h = re.search(r'href=["\']([^"\']+)', m.group(0))
        if not h: continue
        path = urlparse(h.group(1)).path
        if tag in ('en', 'zh-CN', 'x-default') and redirect_target(path.lstrip('/')) and tag == 'zh-CN':
            log('D hreflang指向301源', f'{rel} [{tag}] -> {h.group(1)}')

# ================= E/F/G. meta 质量 =================
def meta(doc, pat):
    m = re.search(pat, doc, re.I|re.S)
    return m.group(m.lastindex) if m else None

def meta_by_name(doc, name):
    # 逐标签解析, 防跨标签回溯误配 (2026-11-07 修复)
    for t in re.findall(r'<meta\b[^>]*>', doc, re.I):
        if re.search(r'name=["\']' + name + r'["\']', t, re.I):
            c = re.search(r'content=(["\'])(.*?)\1', t, re.S)
            if c: return c.group(2)
    return None
titles, descs = {}, {}
for p in FILES:
    rel = rel_of(p); doc = DOCS[p]
    if not real_page(p): continue
    t = meta(doc, r'<title[^>]*>(.*?)</title>')
    d = meta_by_name(doc, 'description')
    if not t: log('E 缺title', rel)
    elif len(t) > 65 or len(t) < 25: log('E title长度', f'{rel} ({len(t)}) {t[:70]}')
    if not d: log('E 缺description', rel)
    elif len(d) > 165: log('E desc过长', f'{rel} ({len(d)})')
    if t: titles.setdefault(t, []).append(rel)
    if d: descs.setdefault(d, []).append(rel)
for t, rs in titles.items():
    if len(rs) > 1: log('F title重复', f'{t[:60]} <= {rs}')
for d, rs in descs.items():
    if len(rs) > 1: log('F desc重复', f'{d[:60]} <= {rs}')

for p in FILES:
    rel = rel_of(p); doc = DOCS[p]
    if not real_page(p): continue
    need = [x for x in ('og:title', 'og:description', 'og:image', 'twitter:card') if x not in doc]
    if need: log('G OG/Twitter缺失', f'{rel} 缺 {need}')

# ================= H. JSON-LD =================
for p in FILES:
    rel = rel_of(p); doc = DOCS[p]
    for m in re.finditer(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', doc, re.S|re.I):
        try: json.loads(m.group(1))
        except Exception as e: log('H JSON-LD解析失败', f'{rel}: {e}')
    if 'zh-Hans' in doc and real_page(p): log('H inLanguage旧码zh-Hans', rel)

# ================= I/J. lang 属性 & 混排 =================
for p in FILES:
    rel = rel_of(p); doc = DOCS[p]
    if not real_page(p):
        continue
    m = re.search(r'<html[^>]*\blang=["\']([^"\']+)', doc, re.I)
    lang = (m.group(1) if m else None) or ''
    exp = 'zh-CN' if is_zh(rel) else 'en'
    if lang and lang not in (exp,) and not (exp == 'zh-CN' and lang in ('zh', 'zh-Hans', 'zh-Hant')):
        log('I lang属性不符', f'{rel}: lang={lang} 期望={exp}')
    vis = visible(doc)
    if exp == 'en' and disallowed(rel):
        n = 0
    if exp == 'en':
        n = cjk_count(vis)
        if n > 30:
            samp = re.findall(r'[\u4e00-\u9fff]{2,12}', vis)[:4]
            log('J1 EN页含中文', f'{rel}: {n} 处 | 例: {samp}')
    else:
        n = len(re.findall(r'(?:Share this article|Read full analysis|Ad Space|Latest Articles|Home\b)', vis))
        if n > 3: log('J2 ZH页含英文功能栏', f'{rel}: {n} 处')

# ================= K. 列表登记 =================
en_list = (ROOT / 'blog' / 'index.html')
zh_list = (ROOT / 'zh' / 'blog' / 'index.html')
for src, lst, base_dir in ((DOCS.get(en_list, ''), en_list, ROOT / 'blog'),
                           (DOCS.get(zh_list, ''), zh_list, ROOT / 'zh' / 'blog')):
    for f in sorted(base_dir.glob('*.html')):
        if f == lst: continue
        if not real_page(f): continue
        if f.name not in src and f'/{f.name}' not in src and f.relative_to(ROOT).as_posix() not in src:
            log('K 文章未在所属列表登记', f'{f.relative_to(ROOT)} (列表 {lst.relative_to(ROOT)})')

# ================= L. 迁移残留重复 =================
for p in FILES:
    rel = rel_of(p)
    doc = DOCS[p]
    tgt = redirect_target(rel)
    if tgt and not is_stub_page(p):
        log('L 旧文件301但非存根页', f'{rel} -> {tgt}')
    if tgt and is_stub_page(p):
        m = re.search(r'http-equiv=["\']refresh["\'][^>]*content=["\']\s*\d+\s*;\s*url=([^"\']+)', doc[:4000], re.I); c = re.search(r'rel="canonical" href="([^"]+)"', doc)
        norm = lambda x: (x or '').replace('https://www.emuqi.com', '').replace('http://www.emuqi.com', '').split('#')[0].rstrip('/').removesuffix('/index.html').rstrip('/')
        if not c or 'noindex' not in doc or norm(c.group(1)) != norm(tgt) or (m and norm(m.group(1)) != norm(tgt)):
            log('L 存根页canonical/跳转不一致', rel)
# 同名 slug 双语共存但无规则
zh_slugs = {f.stem for f in (ROOT / 'zh' / 'blog').glob('*.html')} if (ROOT / 'zh' / 'blog').exists() else set()
for s in sorted(zh_slugs):
    if s == 'index': continue
    old = ROOT / 'blog' / f'{s}.html'
    old = ROOT / 'blog' / f'{s}.html'
    if old.is_file() and not redirect_target(f'blog/{s}.html') and not is_stub_page(old) and '/blog/index' not in s:
        log('L2 中文页无301且非存根(重复内容)', f'blog/{s}.html vs zh/blog/{s}.html')

# ================= M/N 迁移后遗症：CSS url() 断链 与 中文树标题语言 =================
import posixpath
for p_ in FILES:
    rel = rel_of(p_)
    doc = p_.read_text(encoding='utf-8', errors='ignore')
    for u in re.findall(r'url\(\s*[\'\"]?([^\'")]+)[\'"]?\s*\)', doc):
        if u.startswith(('http', '//', 'data:', '/', '#')): continue
        cand = (p_.parent / u.split('?')[0]).resolve()
        if not cand.exists() and not str(cand).endswith('.webp') and not Path(str(cand).rsplit('.', 1)[0] + '.webp').exists():
            log('M CSS url() 断链', f'{rel} -> {u}')
for p_ in FILES:
    rel = rel_of(p_)
    if not rel.startswith('zh/'): continue
    doc = p_.read_text(encoding='utf-8', errors='ignore')
    if is_stub_page(p_): continue
    t = re.search(r'<title>(.*?)</title>', doc, re.S)
    h = re.search(r'<h1[^>]*>(.*?)</h1>', doc, re.S)
    for tag, m in (('<title>', t), ('<h1>', h)):
        if m and not re.search(r'[\u4e00-\u9fff]', m.group(1)):
            log('N 中文树页面标题无中文', f'{rel} {tag}: {re.sub(chr(60)+"[^>]+"+chr(62), " ", m.group(1)).strip()[:50]}')

# ================= 输出 =================
total = 0
print(f'扫描 HTML: {len(FILES)} | sitemap URL: {len(urls)} | 301 规则: {len(rules)}+prefix')
for k in sorted(out):
    print(f'\n### {k} — {len(out[k])} 项')
    for v in out[k][:25]: print('  ' + v)
    if len(out[k]) > 25: print(f'  ... 共 {len(out[k])} 项')
    total += len(out[k])
print(f'\n>>> 问题总数: {total}')
