#!/usr/bin/env python3
"""MUQI emuqi 全站审计 V3.2 —— 生产页面审计与双语配对 (2026-11-27)"""
import os, re, json, glob, html, posixpath
from pathlib import Path, PurePosixPath
from urllib.parse import urlparse, unquote

import sys
ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
SKIP_DIRS = ('templates/', 'node_modules/', '.github/', 'scratch/', 'research/',
             'scripts/', 'distribution_packages/', 'emuqi/')
SKIP_FILES = ('404.html', 'baidu_verify_', 'ByteDanceVerify', 'sogousiteverification')
STUB = re.compile(r'http-equiv=["\']refresh["\'][^>]*content=["\']\s*\d+\s*;\s*url=', re.I)
# 这些英文页有意保留中文：双语视频、证书/公告原文、企业注册名与方法论双语提示。
INTENTIONAL_CJK = {
    'blog/hydrogen-ten-questions-video-series-en.html',
    'blog/muqi-solid-hydrogen-lab-icr-copyright-certificates-en.html',
    'blog/sac-tc621-national-antimicrobial-standard-committee-en.html',
    'h2-wellness-hub/enterprise-archive.html',
    'h2-wellness-hub/methodology.html',
}

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
FILES = [p for p in ALL if not any(s in str(p.relative_to(ROOT)) for s in SKIP_DIRS)
         and not p.name.startswith(SKIP_FILES)]
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
        trailing_slash = unquote(pr.path if pr.scheme in ('http', 'https') else l).endswith('/')
        if pr.scheme in ('http', 'https'):
            if 'emuqi.com' not in pr.netloc: continue
            path = unquote(pr.path)
        else:
            path = unquote(l)
            if not path: continue
            path = path if path.startswith('/') else PurePosixPath(base.relative_to(ROOT).as_posix(), path).as_posix()
        # 浏览器会把 ../ 折叠为父级；审计必须先做同样的 POSIX 规范化，
        # 否则 zh/blog/../h2-wellness-hub/ 会漏报为旧 /zh/h2-wellness-hub/ 301 源。
        path = posixpath.normpath('/' + path.lstrip('/'))
        if trailing_slash and path != '/':
            path += '/'
        if path.endswith('/'): path = path + 'index.html'
        if redirect_target(path.lstrip('/')):   # 即使存根文件存在，也应直接链接最终 URL
            log('A2 内链指向301源(应改最终URL)', f'{rel} -> {l}')
            continue
        cand = [str(ROOT) + path, str(ROOT) + path + '.html', os.path.join(str(ROOT) + path, 'index.html')]
        if any(os.path.isfile(c) for c in cand): continue
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
    if rel in ('404.html', 'h2report/reader/index.html'): continue
    if rel in in_sm or ( '/' + rel) in in_sm: continue
    stem = rel[:-5] if rel.endswith('.html') else rel
    if stem + '/' in in_sm or (rel == 'index.html') or (stem in in_sm): continue
    if real_page(p): log('B2 页面未收录sitemap', rel)

# ================= C/D. canonical / hreflang 完整性、互指与重复 =================
def attrs(tag):
    return {m.group(1).lower(): html.unescape(m.group(2))
            for m in re.finditer(r'([\w:-]+)\s*=\s*["\']([^"\']*)["\']', tag)}

def norm_path(path):
    path = unquote(urlparse(path).path or '/')
    if path != '/':
        path = path.rstrip('/')
        if path.endswith('/index.html'):
            path = path[:-10]
    return path or '/'

def rel_url_path(rel):
    return '/' + (rel[:-10] if rel.endswith('index.html') else rel)

PAGE_INFO = {}
PATH_PAGE = {}
checked_xdefault = set()
for p in FILES:
    rel = rel_of(p)
    if not real_page(p):
        continue
    doc = DOCS[p]
    links = [attrs(t) for t in re.findall(r'<link\b[^>]*>', doc, re.I)]
    canonical = next((a.get('href') for a in links if 'canonical' in a.get('rel', '').lower().split()), None)
    lang_m = re.search(r'<html\b[^>]*\blang=["\']([^"\']+)', doc, re.I)
    alts = {}
    duplicates = []
    for a in links:
        if 'alternate' not in a.get('rel', '').lower().split() or not a.get('hreflang') or not a.get('href'):
            continue
        lang = a['hreflang']
        if lang in alts:
            duplicates.append(lang)
        alts[lang] = a['href']
    info = {'canonical': canonical, 'lang': (lang_m.group(1) if lang_m else ''),
            'alts': alts, 'duplicates': duplicates}
    PAGE_INFO[rel] = info
    if canonical:
        PATH_PAGE[norm_path(canonical)] = rel

for rel, info in PAGE_INFO.items():
    doc = DOCS[ROOT / rel]
    canonical = info['canonical']
    if not canonical:
        log('C 缺canonical', rel)
    else:
        cp = urlparse(canonical)
        cpath = norm_path(canonical)
        if cp.netloc != 'www.emuqi.com':
            log('C canonical主机非www', f'{rel} -> {canonical}')
        if redirect_target(cp.path.lstrip('/')):
            log('C canonical指向301源', f'{rel} -> {canonical}')
        if rel != 'h2report/reader/index.html' and cpath != norm_path(rel_url_path(rel)):
            log('C canonical非当前页', f'{rel} -> {canonical}')
    if info['duplicates']:
        log('D hreflang重复声明', f"{rel}: {info['duplicates']}")
    for lang, href in info['alts'].items():
        hp = urlparse(href)
        path = norm_path(href)
        if hp.netloc != 'www.emuqi.com':
            log('D hreflang主机非www', f'{rel} [{lang}] -> {href}')
        if redirect_target(hp.path.lstrip('/')):
            log('D hreflang指向301源', f'{rel} [{lang}] -> {href}')
        target_rel = PATH_PAGE.get(path)
        if not target_rel:
            candidate = ROOT / path.lstrip('/')
            if path.endswith('/'):
                candidate = candidate / 'index.html'
            elif not candidate.suffix:
                candidate = Path(str(candidate) + '.html')
            if candidate.is_file():
                target_rel = rel_of(candidate)
        if not target_rel or target_rel not in PAGE_INFO:
            log('D hreflang目标非正式页面', f'{rel} [{lang}] -> {href}')
            continue
        if lang in ('en', 'zh-CN'):
            current_path = norm_path(rel_url_path(rel))
            if path == current_path:
                continue
            back_lang = 'zh-CN' if lang == 'en' else 'en'
            back = PAGE_INFO[target_rel]['alts'].get(back_lang)
            if not back or norm_path(back) != current_path:
                log('D hreflang未互指', f'{rel} [{lang}] -> {href}; 回链={back or "缺失"}')
        if lang == 'x-default':
            en_href = info['alts'].get('en')
            zh_href = info['alts'].get('zh-CN')
            if en_href and zh_href:
                pair = tuple(sorted((norm_path(en_href), norm_path(zh_href))))
                if pair not in checked_xdefault:
                    checked_xdefault.add(pair)
                    en_rel = PATH_PAGE.get(norm_path(en_href))
                    zh_rel = PATH_PAGE.get(norm_path(zh_href))
                    en_x = PAGE_INFO.get(en_rel, {}).get('alts', {}).get('x-default')
                    zh_x = PAGE_INFO.get(zh_rel, {}).get('alts', {}).get('x-default')
                    if not en_x or not zh_x or norm_path(en_x) != norm_path(zh_x):
                        log('D x-default双语不一致', f'{en_rel} [{en_x or "缺失"}] vs {zh_rel} [{zh_x or "缺失"}]')

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
    t = html.unescape(re.sub(r'\s+', ' ', t)).strip() if t else None
    d = html.unescape(re.sub(r'\s+', ' ', d)).strip() if d else None
    zh = is_zh(rel)
    if not t: log('E 缺title', rel)
    elif len(t) > (60 if zh else 65) or len(t) < (12 if zh else 25):
        log('E title长度', f'{rel} ({len(t)}) {t[:70]}')
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
def walk_json(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk_json(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_json(child)

for p in FILES:
    rel = rel_of(p); doc = DOCS[p]
    for m in re.finditer(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', doc, re.S|re.I):
        try:
            data = json.loads(m.group(1))
        except Exception as e:
            log('H JSON-LD解析失败', f'{rel}: {e}')
            continue
        if not real_page(p):
            continue
        expected = 'zh-CN' if is_zh(rel) else 'en'
        for node in walk_json(data):
            types = node.get('@type', [])
            types = [types] if isinstance(types, str) else types
            if any(t in ('Article', 'BlogPosting', 'TechArticle') for t in types):
                actual = node.get('inLanguage')
                values = actual if isinstance(actual, list) else [actual]
                valid = any(v == expected or (expected == 'en' and isinstance(v, str) and v.startswith('en-'))
                            for v in values)
                if actual and not valid:
                    log('H JSON-LD语言不符', f'{rel}: inLanguage={actual} 期望={expected}')
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
        if n > 30 and rel not in INTENTIONAL_CJK:
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
# 同名 slug 双语共存：仅语言、canonical 与互链都正确时视为合法双语对
zh_slugs = {f.stem for f in (ROOT / 'zh' / 'blog').glob('*.html')} if (ROOT / 'zh' / 'blog').exists() else set()
for s in sorted(zh_slugs):
    if s == 'index': continue
    old_rel, zh_rel = f'blog/{s}.html', f'zh/blog/{s}.html'
    old = ROOT / old_rel
    if not old.is_file() or redirect_target(old_rel) or is_stub_page(old):
        continue
    en_info, zh_info = PAGE_INFO.get(old_rel, {}), PAGE_INFO.get(zh_rel, {})
    en_ok = (en_info.get('lang') == 'en' and
             norm_path(en_info.get('canonical') or '') == norm_path(rel_url_path(old_rel)) and
             norm_path(en_info.get('alts', {}).get('zh-CN') or '') == norm_path(rel_url_path(zh_rel)))
    zh_ok = (zh_info.get('lang') == 'zh-CN' and
             norm_path(zh_info.get('canonical') or '') == norm_path(rel_url_path(zh_rel)) and
             norm_path(zh_info.get('alts', {}).get('en') or '') == norm_path(rel_url_path(old_rel)))
    if not (en_ok and zh_ok):
        log('L2 同slug双语对未正确隔离', f'{old_rel} vs {zh_rel}')

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

# ================= O. 可见语言切换器与 hreflang 一致性 =================
for rel, info in PAGE_INFO.items():
    doc = DOCS[ROOT / rel]
    zh = is_zh(rel)
    expected = info['alts'].get('en' if zh else 'zh-CN')
    if not expected:
        continue
    found = False
    for m in re.finditer(r'<a\b([^>]*)>(.*?)</a>', doc, re.S|re.I):
        a = attrs('<a ' + m.group(1) + '>')
        classes = a.get('class', '').split()
        if not a.get('href'):
            continue
        href = a.get('href', '')
        hp = urlparse(href)
        if hp.scheme in ('http', 'https') and 'emuqi.com' not in hp.netloc:
            continue
        label = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
        target_lang_label = (zh and ('EN' in label or 'English' in label)) or ((not zh) and '中文' in label)
        if not target_lang_label:
            continue
        if 'lang-pill-opt' in classes or 'hub-language-link' in classes or target_lang_label:
            if norm_path(a['href']) == norm_path(expected):
                found = True
            else:
                log('O 语言切换器错链', f'{rel}: {label} -> {a["href"]}; 应为 {expected}')
    if not found:
        log('O2 双语页缺可见语言切换', f'{rel}: 应显示指向 {expected} 的语言链接')

# ================= P. AI 知识库文章覆盖 =================
ai_indexes = {}
for name in ('llms.txt', 'llms-full.txt'):
    path = ROOT / name
    ai_indexes[name] = path.read_text(encoding='utf-8', errors='ignore') if path.exists() else ''
for rel, info in PAGE_INFO.items():
    if rel in ('blog/index.html', 'zh/blog/index.html'):
        continue
    if not (rel.startswith('blog/') or rel.startswith('zh/blog/')):
        continue
    canonical = info.get('canonical')
    if not canonical:
        continue
    for name, text in ai_indexes.items():
        if canonical not in text:
            log('P AI知识库缺文章', f'{name} 缺 {rel} -> {canonical}')

# ================= Q. 博客列表卡片语言 / 唯一性 / 时间顺序 =================
from datetime import datetime
month_map = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12,
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10,
    'november': 11, 'december': 12,
}
for rel in ('blog/index.html', 'zh/blog/index.html'):
    doc = DOCS.get(ROOT / rel, '')
    zh = rel.startswith('zh/')
    expected_prefix = '/zh/blog/' if zh else '/blog/'
    seen_slugs = set()
    previous_date = None
    for m in re.finditer(r'<a\b([^>]*)>(.*?)</a>', doc, re.S|re.I):
        body = m.group(2)
        if not re.search(r'<h3\b', body, re.I):
            continue
        a = attrs('<a ' + m.group(1) + '>')
        href = a.get('href', '').strip()
        if not href:
            log('Q 博客卡片缺链接', rel)
            continue
        path = href if href.startswith('/') else '/' + PurePosixPath(
            PurePosixPath(rel).parent.as_posix(), href
        ).as_posix()
        path = norm_path(path)
        if not path.startswith(expected_prefix):
            target_rel = PATH_PAGE.get(path)
            target_alts = PAGE_INFO.get(target_rel, {}).get('alts', {})
            expected_lang = 'zh-CN' if zh else 'en'
            if expected_lang in target_alts:
                log('Q1 博客卡片语言树错链', f'{rel}: {href} 应位于 {expected_prefix}')
        slug = PurePosixPath(path).name
        if slug in seen_slugs:
            log('Q2 博客卡片重复', f'{rel}: {slug}')
        seen_slugs.add(slug)
        card_text = html.unescape(re.sub(r'<[^>]+>', ' ', body))
        card_text = re.sub(r'\s+', ' ', card_text)
        date = None
        dm = re.search(r'(\d{4})年(\d{1,2})月(\d{1,2})日', card_text)
        if dm:
            date = datetime(int(dm.group(1)), int(dm.group(2)), int(dm.group(3))).date()
        else:
            dm = re.search(r'([A-Za-z]+)\s+(\d{1,2}),?\s+(\d{4})', card_text)
            if dm and dm.group(1).lower() in month_map:
                date = datetime(int(dm.group(3)), month_map[dm.group(1).lower()], int(dm.group(2))).date()
            else:
                dm = re.search(r'(\d{4})-(\d{2})-(\d{2})', card_text)
                if dm:
                    date = datetime(int(dm.group(1)), int(dm.group(2)), int(dm.group(3))).date()
        if not date:
            log('Q3 博客卡片日期缺失', f'{rel}: {slug}')
        elif previous_date and previous_date < date:
            log('Q3 博客卡片时间倒序', f'{rel}: {slug} {date} 晚于前卡 {previous_date}')
        if date:
            previous_date = date

# ================= 输出 =================
total = 0
print(f'扫描 HTML: {len(FILES)} | sitemap URL: {len(urls)} | 301 规则: {len(rules)}+prefix')
for k in sorted(out):
    print(f'\n### {k} — {len(out[k])} 项')
    for v in out[k][:25]: print('  ' + v)
    if len(out[k]) > 25: print(f'  ... 共 {len(out[k])} 项')
    total += len(out[k])
print(f'\n>>> 问题总数: {total}')
