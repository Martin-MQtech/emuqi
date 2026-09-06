#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. UPDATE blog/index.html (English blog list)
en_index_path = os.path.join(BASE_DIR, "blog", "index.html")
with open(en_index_path, "r", encoding="utf-8") as f:
    en_index_content = f.read()

en_card = """      <!-- 0. NEW: The Nespresso Moment for Beauty Hardware: Facial Steamer Upgrade — 2026-09-06 -->
      <a href="solid-state-hydrogen-facial-steamer-upgrade-en.html" style="text-decoration:none;color:inherit;background:#fff;border-radius:14px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,0.06);transition:transform 0.2s,box-shadow 0.2s;display:flex;flex-direction:column;border:2px solid #f47b20" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 24px rgba(244,123,32,0.15)'" onmouseout="this.style.transform='';this.style.boxShadow='0 1px 4px rgba(0,0,0,0.06)'">
        <div style="aspect-ratio:16/10;overflow:hidden;background:#0a1628">
          <img src="../assets/images/blog/steamer/hero-steamer-concept.png" alt="The Nespresso Moment for Beauty Hardware: Solid-State Hydrogen Steamer Upgrade" style="width:100%;height:100%;object-fit:cover" loading="lazy">
        </div>
        <div style="padding:24px;flex:1;display:flex;flex-direction:column">
          <span style="font-size:12px;font-weight:600;color:#f47b20;letter-spacing:0.5px;text-transform:uppercase;margin-bottom:8px">★ NEW · Sep 6, 2026 · OEM Innovation</span>
          <h3 style="font-size:17px;font-weight:700;color:#0f172a;line-height:1.4;margin-bottom:8px">The 'Nespresso Moment' for Beauty Hardware: How Solid-State Hydrogen Unlocks High-Power Steamers Without Retooling</h3>
          <p style="font-size:14px;color:#64748b;line-height:1.6;flex:1">Bridging the 800W gap between heavy-mist output and pure molecular hydrogen. Zero electrical modification, external reaction chambers, and razor-and-blade economics for personal care appliances.</p>
          <span style="font-size:13px;font-weight:600;color:#f47b20;margin-top:14px">Read strategic whitepaper →</span>
        </div>
      </a>

"""

target_marker_en = "<!-- 0. NEW: Hydrogen-Rich Water as a Green Modification Tool for Plant Protein"
if target_marker_en in en_index_content and "solid-state-hydrogen-facial-steamer-upgrade-en.html" not in en_index_content:
    en_index_content = en_index_content.replace(target_marker_en, en_card + "      " + target_marker_en)
    with open(en_index_path, "w", encoding="utf-8") as f:
        f.write(en_index_content)
    print("✅ Successfully updated emuqi/blog/index.html")
else:
    print("ℹ️ emuqi/blog/index.html already contains entry or marker not found")


# 2. UPDATE blog-list-hydrogen-health.html (Chinese blog list)
zh_list_path = os.path.join(BASE_DIR, "blog-list-hydrogen-health.html")
with open(zh_list_path, "r", encoding="utf-8") as f:
    zh_list_content = f.read()

zh_card = """    <!-- 0. 熏蒸仪固态氢升级方案 — 2026-09-06 (最新重磅) -->
    <a href="blog/solid-state-hydrogen-facial-steamer-upgrade.html" style="text-decoration:none;color:inherit;background:#fff;border-radius:14px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,0.06);border:2px solid #fed7aa;transition:transform 0.2s,box-shadow 0.2s;display:flex;flex-direction:column" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 24px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='';this.style.boxShadow='0 1px 4px rgba(0,0,0,0.06)'">
      <div style="aspect-ratio:16/10;overflow:hidden;background:#0a1628"><img src="assets/images/blog/steamer/hero-steamer-concept.png" alt="熏蒸仪的胶囊咖啡机时刻：大功率热雾设备零改电升级分子氢" style="width:100%;height:100%;object-fit:cover" loading="lazy"></div>
      <div style="padding:24px;flex:1;display:flex;flex-direction:column">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
          <span style="font-size:12px;font-weight:700;color:#ea580c;letter-spacing:0.5px;text-transform:uppercase">2026年9月6日</span>
          <span style="font-size:11px;font-weight:700;background:#ffedd5;color:#c2410c;padding:2px 8px;border-radius:12px">最新发布</span>
        </div>
        <h3 style="font-size:17px;font-weight:700;color:#1a1a2e;line-height:1.4;margin-bottom:8px">熏蒸仪的“胶囊咖啡机”时刻：大功率热雾设备如何实现“零改电、免开模”升级高浓度分子氢</h3>
        <p style="font-size:14px;color:#64748b;line-height:1.6;flex:1">从海外客户的刚需痛点，看大功率熏蒸仪如何告别百元代工内卷，迈向“零模具风险出货 + 固态氢片/草本耗材高频复购”的万亿美业新生态。</p>
        <span style="font-size:13px;font-weight:600;color:#ea580c;margin-top:14px">阅读全文 (B2B 硬件创新深度) →</span>
      </div>
    </a>

"""

target_marker_zh = "<!-- 0. 固态氢 vs PEM 电解技术对比 — 2026-09-03"
if target_marker_zh in zh_list_content and "solid-state-hydrogen-facial-steamer-upgrade.html" not in zh_list_content:
    zh_list_content = zh_list_content.replace(target_marker_zh, zh_card + "    " + target_marker_zh)
    with open(zh_list_path, "w", encoding="utf-8") as f:
        f.write(zh_list_content)
    print("✅ Successfully updated emuqi/blog-list-hydrogen-health.html")
else:
    print("ℹ️ emuqi/blog-list-hydrogen-health.html already contains entry or marker not found")


# 3. UPDATE sitemap.xml
sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap_content = f.read()

sitemap_entries = """  <url>
    <loc>https://www.emuqi.com/blog/solid-state-hydrogen-facial-steamer-upgrade.html</loc>
    <lastmod>2026-09-06</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://www.emuqi.com/blog/solid-state-hydrogen-facial-steamer-upgrade-en.html</loc>
    <lastmod>2026-09-06</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
</urlset>"""

if "solid-state-hydrogen-facial-steamer-upgrade.html" not in sitemap_content:
    sitemap_content = sitemap_content.replace("</urlset>", sitemap_entries)
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("✅ Successfully updated emuqi/sitemap.xml")
else:
    print("ℹ️ emuqi/sitemap.xml already contains entry")

