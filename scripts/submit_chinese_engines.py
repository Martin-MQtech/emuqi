#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MUQI Tech — Chinese Search Engines & AI Submission Tool
======================================================
Automated submission helper for:
1. Baidu Active Push API (百度主动推送 API)
2. Microsoft Bing & IndexNow (PC端必应 + AI Copilot)
3. 360 Search / Sogou / ByteDance (Toutiao & Doubao) submission guidelines & format generator
"""

import os
import sys
import json
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP_PATH = os.path.join(BASE_DIR, "sitemap.xml")

DEFAULT_BAIDU_TOKEN = "3GLlFkCFCw6d1bAo"
DEFAULT_BAIDU_SITE = "https://www.emuqi.com"

# 重点推荐优先推送的中文母站核心资产 (对齐 2026-09-08 独立 /zh/ 体系)
PRIORITY_CHINESE_URLS = [
    "https://www.emuqi.com/zh/blog/solid-state-hydrogen-foot-spa-consumables.html",
    "https://www.emuqi.com/zh/blog/",
    "https://www.emuqi.com/zh/",
    "https://www.emuqi.com/zh/solid-state-hydrogen-vs-pem-electrolysis.html",
    "https://www.emuqi.com/zh/blog/solid-state-hydrogen-facial-steamer-upgrade.html",
    "https://www.emuqi.com/zh/blog/sac-tc621-national-antimicrobial-standard-committee.html",
    "https://www.emuqi.com/zh/blog/hydrogen-water-plant-protein-green-modification.html",
    "https://www.emuqi.com/zh/blog/hydrogen-water-technology-comparison.html",
    "https://www.emuqi.com/zh/blog/gary-brecka-hydrogen-water-solid-state-breakthrough.html",
    "https://www.emuqi.com/zh/blog/antimicrobial-ceramic-balls-home-appliances-icr-technology.html",
    "https://www.emuqi.com/h2-wellness-hub/zh/",
    "https://www.emuqi.com/product-functional-ceramic-materials.html"
]

def get_sitemap_urls():
    if not os.path.exists(SITEMAP_PATH):
        return []
    tree = ET.parse(SITEMAP_PATH)
    root = tree.getroot()
    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = []
    for u in root.findall('ns:url', ns):
        loc = u.find('ns:loc', ns)
        if loc is not None and loc.text:
            urls.append(loc.text.strip())
    return urls

def push_to_baidu(token=None, urls=None, site="https://www.emuqi.com"):
    """
    百度搜索资源平台主动推送接口
    API: http://data.zz.baidu.com/urls?site=https://www.emuqi.com&token=YOUR_TOKEN
    """
    token = token or DEFAULT_BAIDU_TOKEN
    if not token or token == "YOUR_BAIDU_TOKEN":
        print("⚠️ [百度主动推送] 未配置有效的 Baidu Token，跳过实际请求。")
        print(f"👉 获取方式：登录 https://ziyuan.baidu.com -> 普通收录 -> API提交，获取专属 token 后运行：")
        print(f"   python3 scripts/submit_chinese_engines.py --baidu-token <YOUR_TOKEN>\n")
        return False

    target_urls = urls or PRIORITY_CHINESE_URLS
    api_url = f"http://data.zz.baidu.com/urls?site={site}&token={token}"
    data_payload = "\n".join(target_urls).encode('utf-8')

    req = urllib.request.Request(
        api_url,
        data=data_payload,
        headers={"Content-Type": "text/plain", "User-Agent": "curl/7.68.0"}
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            print(f"✅ [百度主动推送成功]: HTTP {resp.status}")
            print(f"   成功推送数: {result.get('success', 0)}, 当天剩余可推送额度: {result.get('remain', 0)}")
            return True
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode('utf-8', errors='ignore')
        print(f"❌ [百度主动推送失败]: HTTP {e.code} - {err_msg}")
        return False
    except Exception as e:
        print(f"❌ [百度推送异常]: {e}")
        return False

def push_to_indexnow(urls=None):
    """
    通过 IndexNow 协议主动推送到 Bing、Naver、Yandex 等引擎
    """
    key = "531ba2233ce04366bbfc10fa232651b5"
    host = "www.emuqi.com"
    key_location = f"https://{host}/{key}.txt"
    target_urls = urls or get_sitemap_urls()

    payload = {
        "host": host,
        "key": key,
        "keyLocation": key_location,
        "urlList": target_urls
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": "IndexNow-MUQI-Tech/1.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print(f"✅ [IndexNow 官方枢纽 (Bing/Naver/Yandex)]: HTTP {resp.status} OK (共提交 {len(target_urls)} 个 URL)")
            return True
    except Exception as e:
        print(f"❌ [IndexNow 提交失败]: {e}")
        return False

def print_manual_submission_guide():
    print("=" * 70)
    print(" 🇨🇳 中文各大搜索引擎与 AI 抓取平台手动登记与备份指南")
    print("=" * 70)
    print("1. 百度搜索资源平台 (Baidu Webmaster):")
    print("   - 官网: https://ziyuan.baidu.com")
    print("   - 登录方式: 百度账号/手机号登录")
    print("   - 验证站点: 添加 https://www.emuqi.com，选择 HTML 标签验证或文件验证")
    print("   - 提交入口: 普通收录 -> 资源提交 -> Sitemap 提交: https://www.emuqi.com/sitemap.xml")
    print("   - API 实时推送: 获取 Token 后使用本脚本一键推入\n")
    
    print("2. 360 搜索站长平台 (360 Webmaster):")
    print("   - 官网: https://zhanzhang.so.com")
    print("   - 作用: 360 浏览器与 360 AI 搜索的底层核心信源库")
    print("   - 提交入口: 站点管理 -> 添加网站 -> Sitemap 提交\n")
    
    print("3. 搜狗站长平台 (Sogou Webmaster):")
    print("   - 官网: https://zhanzhang.sogou.com")
    print("   - 作用: 搜狗搜索 + 微信生态部分外显数据联动")
    print("   - 提交入口: 网站收录 -> 提交 Sitemap\n")

    print("4. 今日头条 / 抖音搜索站长平台 (ByteDance):")
    print("   - 官网: https://zhanzhang.toutiao.com")
    print("   - 作用: 豆包 (Doubao) 与抖音、头条全系 AI 搜索的抓取引导平台")
    print("   - 提交入口: 网站验证与数据抓取频次管理\n")

    print("5. 夸克 / 神马搜索站长平台 (Alibaba):")
    print("   - 官网: https://zhanzhang.sm.cn")
    print("   - 作用: 夸克 AI 搜索与 UC 浏览器搜索底座")
    print("   - 提交入口: 接口提交与 Sitemap 提交\n")
    print("=" * 70)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="MUQI Tech Chinese Search Engines Submission Tool")
    parser.add_argument("--baidu-token", help="Baidu API Token for ziyuan.baidu.com", default=None)
    parser.add_argument("--indexnow-only", action="store_true", help="Only run IndexNow submission")
    parser.add_argument("--guide", action="store_true", help="Show manual platform submission guide")
    args = parser.parse_args()

    print("🚀 开始执行中文搜索引擎与 AI 引擎提交程序...\n")
    
    # 1. 运行 IndexNow (即时通知必应中国与接入生态)
    push_to_indexnow(PRIORITY_CHINESE_URLS)
    
    # 2. 百度推送
    push_to_baidu(token=args.baidu_token, urls=PRIORITY_CHINESE_URLS)

    # 3. 输出指引
    print_manual_submission_guide()
