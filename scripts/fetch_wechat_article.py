#!/usr/bin/env python3
"""
MUQI WeChat Article Fetcher
============================
A self-contained tool to fetch any WeChat Official Account article
(including the '千氢百战-木齐技术观察' account) via the public mp.weixin.qq.com
endpoint, then parse the article body into a structured JSON and
download all image assets locally.

Usage:
  python3 fetch_wechat_article.py "<wechat_url>" [--out <dir>]

Examples:
  python3 fetch_wechat_article.py "https://mp.weixin.qq.com/s?__biz=...&mid=...&idx=..."
  python3 fetch_wechat_article.py "https://mp.weixin.qq.com/s?__biz=..." --out ./tmp

Dependencies:
  Only Python 3.7+ stdlib (urllib, re, json, html, base64, os, argparse).
  No third-party packages required.
"""
import os
import re
import json
import time
import argparse
import urllib.request
import urllib.parse
import html as html_lib
from pathlib import Path

UA_DESKTOP = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)
UA_MOBILE = (
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
)


def http_get(url, ua=UA_DESKTOP, timeout=30):
    """Fetch URL using stdlib urllib with a friendly User-Agent."""
    req = urllib.request.Request(url, headers={
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read()
        enc = resp.headers.get_content_charset() or "utf-8"
        return raw.decode(enc, errors="replace")


def download(url, out_path, ua=UA_DESKTOP, timeout=30):
    """Download a binary asset (image) to disk."""
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Referer": "https://mp.weixin.qq.com/"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
    out_path.write_bytes(data)
    return out_path


def extract_meta(html_text):
    """Pull og:* / twitter:* / meta tags / __biz / title from article HTML."""
    out = {}

    # og:* meta tags
    for m in re.finditer(r'<meta\s+property=[\'"]og:([^\'"]+)[\'"]\s+content=[\'"]([^\'"]*)[\'"]', html_text):
        out["og_" + m.group(1)] = html_lib.unescape(m.group(2))
    for m in re.finditer(r'<meta\s+content=[\'"]([^\'"]*)[\'"]\s+property=[\'"]og:([^\'"]+)[\'"]', html_text):
        out["og_" + m.group(2)] = html_lib.unescape(m.group(1))

    # twitter:*
    for m in re.finditer(r'<meta\s+name=[\'"]twitter:([^\'"]+)[\'"]\s+content=[\'"]([^\'"]*)[\'"]', html_text):
        out["tw_" + m.group(1)] = html_lib.unescape(m.group(2))

    # plain description / keywords
    for m in re.finditer(r'<meta\s+name=[\'"]description[\'"]\s+content=[\'"]([^\'"]*)[\'"]', html_text):
        out["description"] = html_lib.unescape(m.group(1))
    for m in re.finditer(r'<meta\s+name=[\'"]keywords[\'"]\s+content=[\'"]([^\'"]*)[\'"]', html_text):
        out["keywords"] = html_lib.unescape(m.group(1))

    # __biz / __msgid for archival
    m = re.search(r'__biz\s*=\s*["\']([^"\']+)["\']', html_text)
    if m: out["__biz"] = m.group(1)
    m = re.search(r'var\s+__biz\s*=\s*["\']([^"\']+)["\']', html_text)
    if m: out["__biz"] = m.group(1)
    m = re.search(r'"appmsg_token"\s*:\s*"([^"]+)"', html_text)
    if m: out["appmsg_token"] = m.group(1)
    m = re.search(r'"fakeid"\s*:\s*"([^"]+)"', html_text)
    if m: out["fakeid"] = m.group(1)
    m = re.search(r'nickname\s*=\s*"([^"]+)"', html_text)
    if m: out["account_nickname"] = html_lib.unescape(m.group(1))

    # <title> fallback
    m = re.search(r'<title>(.*?)</title>', html_text, re.S)
    if m: out["title"] = html_lib.unescape(m.group(1)).strip()

    return out


def extract_body_html(html_text):
    """Extract the rich content div#js_content as raw inner HTML."""
    m = re.search(r'<div[^>]+id=["\']js_content["\'][^>]*>(.*?)</div>\s*<script', html_text, re.S)
    if m:
        return m.group(1)
    # fallback: look for the js_content div loosely
    m = re.search(r'id=["\']js_content["\']\s*style="[^"]*"\s*>(.*?)<script', html_text, re.S)
    if m: return m.group(1)
    return ""


def collect_images(body_html, base_meta=""):
    """Return a list of image URLs found in body (data-src preferred)."""
    urls = []
    for m in re.finditer(r'data-src=[\'"](https?://[^"\']+)[\'"]', body_html):
        urls.append(m.group(1))
    for m in re.finditer(r'<img[^>]+src=[\'"](https?://[^"\']+)[\'"]', body_html):
        if "data:image" in m.group(1): continue
        urls.append(m.group(1))
    # de-dup, preserve order
    seen, out = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u); out.append(u)
    return out


def text_only(body_html):
    """Strip tags to plain text (used for AI summarization)."""
    txt = re.sub(r'<br\s*/?>', '\n', body_html, flags=re.I)
    txt = re.sub(r'</p\s*>', '\n\n', txt, flags=re.I)
    txt = re.sub(r'<[^>]+>', '', txt)
    txt = html_lib.unescape(txt)
    txt = re.sub(r'\n{3,}', '\n\n', txt)
    return txt.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--out", default="./.wechat_cache")
    ap.add_argument("--no-download-images", action="store_true")
    args = ap.parse_args()

    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"[fetch] {args.url}")
    print(f"[out]   {out_dir}")

    raw_html = http_get(args.url, ua=UA_MOBILE)
    (out_dir / "raw.html").write_text(raw_html, encoding="utf-8")

    meta = extract_meta(raw_html)
    body = extract_body_html(raw_html)
    images = collect_images(body)
    text = text_only(body)

    (out_dir / "body.html").write_text(body, encoding="utf-8")
    (out_dir / "text.txt").write_text(text, encoding="utf-8")
    with open(out_dir / "meta.json", "w", encoding="utf-8") as f:
        json.dump({
            "url": args.url,
            "meta": meta,
            "image_count": len(images),
            "images": images,
        }, f, ensure_ascii=False, indent=2)

    print(f"[ok]   title : {meta.get('og_title') or meta.get('title')}")
    print(f"[ok]   author: {meta.get('og_article_author') or meta.get('account_nickname','-')}")
    print(f"[ok]   images: {len(images)}")
    print(f"[ok]   text  : {len(text)} chars -> {out_dir/'text.txt'}")

    if not args.no_download_images:
        img_dir = out_dir / "images"
        for i, u in enumerate(images, 1):
            ext = ".jpg"
            if "png" in u.lower(): ext = ".png"
            elif "gif" in u.lower(): ext = ".gif"
            elif "webp" in u.lower(): ext = ".webp"
            target = img_dir / f"img_{i:02d}{ext}"
            try:
                download(u, target)
                print(f"        downloaded {target.name}")
            except Exception as e:
                print(f"        ! failed {u} -> {e}")


if __name__ == "__main__":
    main()
