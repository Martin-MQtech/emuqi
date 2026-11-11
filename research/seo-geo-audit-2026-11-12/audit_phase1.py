#!/usr/bin/env python3
"""Phase 1 技术审计脚本 — emuqi.com 全站静态扫描（2026-11-12）
复跑: python3 research/seo-geo-audit-2026-11-12/audit_phase1.py
输出: 本目录 phase1_results.json + stdout 摘要。只读，不改任何站点文件。
"""
import json, os, re, sys, glob
from collections import Counter, defaultdict
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
os.chdir(ROOT)
OUT = {"date": "2026-11-12", "root": ROOT}

EXCLUDE_DIRS = {'templates', 'distribution_packages', 'scripts', 'research', 'node_modules',
                '.git', '.zcode', '.freebuff', 'emuqi'}  # emuqi/ 仅存 assets 副本
META_PAGES = {'ByteDanceVerify.html', 'baidu_verify_codeva-DhmQrr2FTg.html',
              'baidu_verify_codeva-K8eoRfjsrG.html', 'sogousiteverification.txt'}

# ---------- 0. 页面清单 ----------
pages = []
for p in glob.glob('**/*.html', recursive=True):
    parts = p.split(os.sep)
    if any(d in EXCLUDE_DIRS for d in parts[:-1]):
        continue
    pages.append(p.replace(os.sep, '/'))
pages.sort()
OUT['page_count'] = len(pages)

# ---------- 1. robots.txt ----------
robots = open('robots.txt', encoding='utf-8').read()
AI_BOTS = ['GPTBot', 'OAI-SearchBot', 'ClaudeBot', 'PerplexityBot', 'Applebot-Extended',
           'Meta-ExternalAgent', 'meta-externalagent', 'Google-Extended', 'CCBot']
bot_status = {}
for b in set(AI_BOTS):
    m = re.search(rf'User-agent:\s*{b}\s*\n((?:[A-Za-z-]+:.*\n)+)', robots)
    if m:
        block = m.group(1)
        bot_status[b] = 'Allow: /' in block and 'Disallow: /' not in block
    else:
        bot_status[b] = None
OUT['robots'] = {
    'sitemap_declared': 'Sitemap:' in robots,
    'ai_bots': bot_status,
    'content_signal_line': bool(re.search(r'^Content-Signal:', robots, re.M)),
}

# ---------- 2. llms.txt ----------
llms_ok = os.path.exists('llms.txt')
llms_full_ok = os.path.exists('llms-full.txt')
OUT['llms'] = {'llms.txt': llms_ok, 'llms-full.txt': llms_full_ok,
               'llms.txt_bytes': os.path.getsize('llms.txt') if llms_ok else 0,
               'llms_full_bytes': os.path.getsize('llms-full.txt') if llms_full_ok else 0}

# ---------- 3. sitemap.xml ----------
tree = ET.parse('sitemap.xml')
ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
sm_entries = []
for u in tree.getroot().findall('s:url', ns):
    loc = (u.findtext('s:loc', '', ns) or '').strip()
    lm = (u.findtext('s:lastmod', '', ns) or '').strip()
    pri = (u.findtext('s:priority', '', ns) or '').strip()
    sm_entries.append({'loc': loc, 'lastmod': lm, 'priority': pri})
OUT['sitemap'] = {
    'url_count': len(sm_entries),
    'priority_gt09': sum(1 for e in sm_entries if e['priority'] and float(e['priority']) > 0.9),
    'no_lastmod': sum(1 for e in sm_entries if not e['lastmod']),
    'lastmod_range': (min((e['lastmod'] for e in sm_entries if e['lastmod']), default=''),
                      max((e['lastmod'] for e in sm_entries if e['lastmod']), default='')),
}
sm_paths = {urlparse(e['loc']).path for e in sm_entries}
# sitemap -> 本地文件缺失 / 本地页 -> 不在 sitemap
missing_local = [e['loc'] for e in sm_entries if not os.path.exists(urlparse(e['loc']).path.lstrip('/'))]
html_local = {'/' + p for p in pages}
# 构造线上路径：index.html -> /
def online_path(p):
    pp = '/' + p
    if pp.endswith('/index.html'):
        pp = pp[:-len('index.html')]
    return pp
local_online = {online_path(p): p for p in pages}
not_in_sitemap = sorted(lp for lp in local_online if lp not in sm_paths
                        and lp not in {'/404.html'} and local_online[lp] not in META_PAGES)
not_in_sitemap = [lp for lp in not_in_sitemap if lp not in sm_paths]
OUT['sitemap']['missing_local_files'] = missing_local
OUT['sitemap']['local_pages_not_in_sitemap'] = not_in_sitemap

# ---------- 逐页 head 解析 ----------
HEAD_RE = re.compile(r'<head\b.*?</head>', re.S)
def head_of(html):
    m = HEAD_RE.search(html)
    return m.group(0) if m else html[:8000]

page_data = {}
issues = defaultdict(list)

for p in pages:
    try:
        html = open(p, encoding='utf-8').read()
    except UnicodeDecodeError:
        html = open(p, encoding='utf-8', errors='replace').read()
    h = head_of(html)
    d = {'path': p}
    d['title'] = (re.search(r'<title[^>]*>(.*?)</title>', h, re.S) or [None, ''])[1].strip() if re.search(r'<title[^>]*>(.*?)</title>', h, re.S) else None
    def tags_all(h, kind):
        return [dict(re.findall(r'([\w:-]+)="([^"]*)"', t)) for t in re.findall(rf'<{kind}\b[^>]*>', h)]
    metas = tags_all(h, 'meta'); links = tags_all(h, 'link')
    d['desc_count'] = sum(1 for t in metas if t.get('name') == 'description')
    d['desc'] = next((t.get('content', '') for t in metas if t.get('name') == 'description'), '')
    d['canonical'] = next((t.get('href') for t in links if t.get('rel') == 'canonical'), None)
    d['h1'] = re.findall(r'<h1\b', html)
    d['h1_count'] = len(d['h1'])
    d['h1_text'] = re.sub(r'<[^>]+>', '', (re.search(r'<h1\b[^>]*>(.*?)</h1>', html, re.S).group(1) if re.search(r'<h1\b[^>]*>(.*?)</h1>', html, re.S) else '')).strip()[:120]
    d['og_image'] = next((t.get('content') for t in metas if t.get('property') == 'og:image'), None)
    d['og_type'] = next((t.get('content') for t in metas if t.get('property') == 'og:type'), None)
    d['twitter_card'] = any(t.get('name') == 'twitter:card' for t in metas)
    d['hreflang'] = [(t.get('hreflang'), t.get('href')) for t in links if t.get('rel') == 'alternate' and 'hreflang' in t]
    d['ldjson_blocks'] = re.findall(r'<script\s+type="application/ld\+json">(.*?)</script>', html, re.S)
    d['ld_types'] = []
    for blk in d['ldjson_blocks']:
        try:
            j = json.loads(blk)
            if isinstance(j, dict):
                g = j.get('@graph', [j])
                d['ld_types'] += [e.get('@type', '?') for e in g if isinstance(e, dict)]
            elif isinstance(j, list):
                d['ld_types'] += [e.get('@type', '?') for e in j if isinstance(e, dict)]
        except Exception:
            issues['ldjson_parse_fail'].append(p)
    d['favicon'] = [t for t in links if 'icon' in (t.get('rel') or '')]
    d['speculation'] = 'speculationrules' in html
    imgs = re.findall(r'<img\b[^>]*>', html)
    d['img_total'] = len(imgs)
    d['img_no_dims'] = sum(1 for t in imgs if 'width=' not in t and 'height=' not in t)
    # NAP 线索
    d['tels'] = sorted(set(re.findall(r'href="tel:([^"]*)"', html)))
    d['mailtos'] = sorted(set(re.findall(r'href="mailto:([^"?]*).*?"', html))) or sorted(set(re.findall(r'href="mailto:([^"]*)"', html)))
    page_data[p] = d

OUT['pages'] = {p: {k: v for k, v in d.items() if k != 'h1'} for p, d in page_data.items()}

# ---------- 4. canonical ----------
for p, d in page_data.items():
    if d['canonical'] is None:
        if p != '404.html':
            issues['canonical_missing'].append(p)
    else:
        cpath = urlparse(d['canonical']).path
        exp = online_path(p)
        if cpath != exp:
            issues['canonical_mismatch'].append(f"{p} -> {cpath} (expected {exp})")

# ---------- 5. meta description / title ----------
for p, d in page_data.items():
    if d['desc_count'] != 1 and p != '404.html':
        issues['desc_count_ne_1'].append(f"{p}: {d['desc_count']}")
    if not d['title'] and p != '404.html':
        issues['title_missing'].append(p)
desc_dup = {}
dc = Counter(d['desc'] for d in page_data.values() if d['desc'])
for k, c in dc.items():
    if c > 1:
        desc_dup[k[:80]] = [pp for pp, dd in page_data.items() if dd['desc'] == k]
OUT['desc_duplicates'] = desc_dup
tc = Counter(d['title'] for d in page_data.values() if d['title'])
OUT['title_duplicates'] = {k[:80]: v for k, c in tc.items() if c > 1 for v in [[pp for pp, dd in page_data.items() if dd['title'] == k]]}
# 标题模板内卷：同模板不同页
tmpl = defaultdict(list)
for p, d in page_data.items():
    if d['title']:
        key = re.sub(r'\s*[-|–—]\s*.*$', '', d['title'])[:40]
        tmpl[key].append(p)
OUT['title_template_collisions'] = {k: v for k, v in tmpl.items() if len(v) > 1 and len(k) > 6}

# ---------- 6. H1 ----------
for p, d in page_data.items():
    if d['h1_count'] != 1 and p not in {'404.html'}:
        issues['h1_count_ne_1'].append(f"{p}: {d['h1_count']}")
OUT['index_h1'] = page_data['index.html']['h1_text']

# ---------- 7. og:image ----------
og_missing = []
for p, d in page_data.items():
    if d['og_image']:
        m = re.match(r'https?://[^/]+(/.*)', d['og_image'])
        lp = m.group(1).lstrip('/') if m else d['og_image'].lstrip('/')
        if not os.path.exists(lp):
            og_missing.append(f"{p} -> {d['og_image']}")
    elif p != '404.html':
        og_missing.append(f"{p} -> (no og:image)")
OUT['og_image_missing_files'] = og_missing

# ---------- 8. JSON-LD ----------
def pages_with(t):
    return [p for p, d in page_data.items() if t in d['ld_types']]
OUT['schema'] = {
    'Organization': pages_with('Organization'),
    'Product_count': len(pages_with('Product')),
    'Article_count': len(pages_with('Article')),
    'FAQPage_count': len(pages_with('FAQPage')),
    'BreadcrumbList_count': len(pages_with('BreadcrumbList')),
    'ContactPage': pages_with('ContactPage'),
}
blog_pages = [p for p in pages if p.startswith('blog/') and p.endswith('.html') and 'index' not in p]
OUT['schema']['blog_without_faq'] = [p for p in blog_pages if 'FAQPage' not in page_data[p]['ld_types'] and 'Article' in page_data[p]['ld_types']]
OUT['schema']['blog_without_article'] = [p for p in blog_pages if 'Article' not in page_data[p]['ld_types']]
prod_pages = [p for p, d in page_data.items() if 'Product' in d['ld_types']]
OUT['schema']['product_pages'] = prod_pages

# NAP 收敛
tels = Counter()
mails = Counter()
for p, d in page_data.items():
    for t in d['tels']: tels[t] += 1
    for m in d['mailtos']: mails[m] += 1
OUT['nap'] = {'tels': dict(tels), 'mailtos': dict(mails)}
# 地址变体
addr_variants = set()
addr_pats = [r'[0-9]+[^,<]{0,40}(?:Road|Roads|Street|Ave|Avenue|Zone|Park|Building|Tower)[^,<]{0,60}',
             r'Zibo[^,<。]{0,80}', r'山东[^,<。]{0,60}', r'Shandong[^,<。]{0,80}']
for p in pages:
    html = open(p, encoding='utf-8', errors='replace').read()
    for pat in addr_pats:
        for m in re.findall(pat, html):
            s = re.sub(r'\s+', ' ', m.strip())
            if 8 < len(s) < 120:
                addr_variants.add(s)
OUT['nap']['address_variants'] = sorted(addr_variants)[:40]

# ---------- 9. hreflang ----------
for p, d in page_data.items():
    if p.startswith('zh/'):
        en_alt = [h for l, h in d['hreflang'] if l in ('en', 'x-default')]
        if not en_alt:
            issues['zh_page_no_en_alternate'].append(p)
    elif p.endswith('.html') and not p.startswith(('h2report', 'h2-wellness-hub', 'solutions-hydrogen-agriculture', 'facts', 'templates')):
        zh_alt = [h for l, h in d['hreflang'] if l == 'zh-CN']
        if not zh_alt and 'blog/' in p:
            issues['en_page_no_zh_alternate'].append(p)

# ---------- 10. 杂项 ----------
fav_src_bug = [f"{p}: {t}" for p, d in page_data.items() for t in d['favicon'] if 'src' in t]
OUT['favicon_src_bug'] = fav_src_bug[:10]
OUT['speculation_pages'] = [p for p, d in page_data.items() if d['speculation']]
img_no_dims_total = sum(d['img_no_dims'] for d in page_data.values())
img_total = sum(d['img_total'] for d in page_data.values())
OUT['images'] = {'total': img_total, 'no_width_height': img_no_dims_total,
                 'pct_missing': round(100 * img_no_dims_total / img_total, 1) if img_total else 0}
# 微字号
micro = Counter()
for p in pages:
    html = open(p, encoding='utf-8', errors='replace').read()
    for m in re.findall(r'text-\[(\d+)px\]', html):
        if int(m) <= 10: micro[m] += 1
    for m in re.findall(r'font-size:\s*(\d+)px', html):
        if int(m) <= 10: micro[m] += 1
OUT['micro_font_sizes'] = dict(micro)
# 移动导航
mob = Counter()
for p in pages:
    html = open(p, encoding='utf-8', errors='replace').read()
    if 'hamburger' in html.lower(): mob['hamburger'] += 1
    if 'mobile-menu' in html.lower() or 'mobile_nav' in html.lower(): mob['mobile-menu'] += 1
    if 'md:hidden' in html: mob['md:hidden'] += 1
    if 'nav-toggle' in html.lower() or 'menu-toggle' in html.lower(): mob['nav-toggle'] += 1
OUT['mobile_nav'] = dict(mob)
# 图片格式冗余 webp/jpg 同名
imgs_dir = 'assets/images'
dup_fmt = []
for f in glob.glob(imgs_dir + '/**/*.webp', recursive=True):
    base = f[:-5]
    for ext in ('.jpg', '.jpeg', '.png'):
        if os.path.exists(base + ext):
            dup_fmt.append(f)
            break
OUT['image_format_dupes'] = {'webp_with_jpg_png_same_name': len(dup_fmt), 'sample': dup_fmt[:10]}
img_sizes = []
for f in glob.glob('assets/images/**/*.*', recursive=True):
    if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        try:
            sz = os.path.getsize(f)
            if sz > 500_000: img_sizes.append((round(sz/1024), f))
        except OSError: pass
img_sizes.sort(reverse=True)
OUT['heavy_images'] = img_sizes[:15]

# ---------- 11. GA4 / 埋点 ----------
ga = {}
for jsf in ['assets/js/analytics.js', 'script.js']:
    if os.path.exists(jsf):
        s = open(jsf, encoding='utf-8', errors='replace').read()
        ev = re.findall(r"(?:gtag\('event'|trackEvent\(|push\(\{'event')\s*[,(]\s*['\"]([^'\"]+)", s)
        ga[jsf] = {'events': sorted(set(ev)), 'bytes': len(s)}
        ga[jsf]['generate_lead_ctx'] = [l.strip()[:160] for l in s.splitlines() if 'generate_lead' in l][:6]
OUT['ga4'] = ga
# 表单提交处理
form_js = []
for jsf in ['script.js', 'assets/js/analytics.js']:
    if os.path.exists(jsf):
        s = open(jsf, encoding='utf-8', errors='replace').read()
        for kw in ['homeRfqForm', 'contactForm', 'submit', 'finally', 'catch']:
            hits = [l.strip()[:150] for l in s.splitlines() if kw in l][:4]
            form_js.append({f"{jsf}:{kw}": hits})
OUT['form_js_grep'] = form_js

# contact/index 表单本体
for pg in ['contact-mqtech-hydrogen-health.html', 'index.html']:
    html = open(pg, encoding='utf-8', errors='replace').read()
    for kw in ['homeRfqForm', 'contact-form', '<form', 'mailto:', 'wa.me', 'whatsapp']:
        n = len(re.findall(re.escape(kw), html, re.I))
        if n: OUT.setdefault('form_presence', {})[f"{pg}:{kw}"] = n

OUT['issues'] = {k: v for k, v in issues.items()}

with open('research/seo-geo-audit-2026-11-12/phase1_results.json', 'w', encoding='utf-8') as f:
    json.dump(OUT, f, ensure_ascii=False, indent=1)

# ---------- 摘要 ----------
print(f"pages={OUT['page_count']}  sitemap={OUT['sitemap']['url_count']}  "
      f"pri>0.9={OUT['sitemap']['priority_gt09']}  no_lastmod={OUT['sitemap']['no_lastmod']}")
print("ISSUES:")
for k, v in sorted(issues.items()):
    print(f"  {k}: {len(v)}")
    for x in v[:6]: print(f"     - {x}")
print(f"desc_dups={len(desc_dup)} title_dups={len(OUT['title_duplicates'])} tmpl_collisions={len(OUT['title_template_collisions'])}")
print(f"schema: Org={len(OUT['schema']['Organization'])} Product={OUT['schema']['Product_count']} "
      f"Article={OUT['schema']['Article_count']} FAQ={OUT['schema']['FAQPage_count']} Breadcrumb={OUT['schema']['BreadcrumbList_count']}")
print(f"imgs: {img_total} total, {img_no_dims_total} no-dims ({OUT['images']['pct_missing']}%)  webp_dupes={OUT['image_format_dupes']['webp_with_jpg_png_same_name']}")
print(f"favicon_src_bug={len(fav_src_bug)}  speculation={len(OUT['speculation_pages'])}  micro_font={dict(micro)}")
print(f"nap tels={dict(tels)} mailtos={dict(mails)}")
