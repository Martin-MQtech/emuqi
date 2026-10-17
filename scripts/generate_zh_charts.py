#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate high-fidelity, professional Chinese infographics for the European Hydrogen Water Cases.
Features authentic market products on the cover, embedded brand thumbnails, clean modern card layouts,
and locator bounding-box screenshots (ZERO black bars or background artifacts).
"""

import os
import base64
from playwright.sync_api import sync_playwright

OUT_DIR = "assets/images/blog/european-hydrogen-water-cases"
os.makedirs(OUT_DIR, exist_ok=True)

PKG_DIR = "/Users/martin/Documents/2026 BUSINESS MTRIX /20260601 MQ TECH 国际业务/20260708 MQ TECH 国际市场市场划分/欧洲氢医学学术圈/发布包_20261017_氢水两个欧洲案例/03_图片素材"

BASE_STYLE_ZH = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Inter", sans-serif;
    background: transparent;
    margin: 0;
    padding: 0;
    -webkit-font-smoothing: antialiased;
  }
</style>
"""

def get_base64_img(rel_path):
    with open(rel_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def generate_zh_cover(page):
    b64_a = get_base64_img("assets/images/blog/european-hydrogen-water-cases/case_a_htoeau_product_cans.png")
    b64_b = get_base64_img("assets/images/blog/european-hydrogen-water-cases/case_b_aquastamina_product.png")

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      {BASE_STYLE_ZH}
      <style>
        .cover-container {{
          width: 1080px;
          height: 460px;
          background: linear-gradient(135deg, #070d1e 0%, #0d1b38 50%, #081e3a 100%);
          position: relative;
          overflow: hidden;
          padding: 40px 50px;
          display: flex;
          align-items: center;
          justify-content: space-between;
          border-bottom: 4px solid #1d4ed8;
        }}
        .bg-grid {{
          position: absolute;
          inset: 0;
          background-image: radial-gradient(rgba(59, 130, 246, 0.15) 1px, transparent 1px);
          background-size: 28px 28px;
          pointer-events: none;
        }}
        .glow-left {{
          position: absolute;
          top: -100px;
          left: -100px;
          width: 400px;
          height: 400px;
          background: radial-gradient(circle, rgba(29, 78, 216, 0.28) 0%, transparent 70%);
          pointer-events: none;
        }}
        .glow-right {{
          position: absolute;
          bottom: -100px;
          right: -100px;
          width: 450px;
          height: 450px;
          background: radial-gradient(circle, rgba(2, 132, 199, 0.25) 0%, transparent 70%);
          pointer-events: none;
        }}
        .left-col {{
          width: 550px;
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          height: 100%;
          position: relative;
          z-index: 2;
        }}
        .top-tag {{
          display: inline-flex;
          align-items: center;
          gap: 8px;
          background: rgba(30, 58, 138, 0.45);
          border: 1px solid rgba(96, 165, 250, 0.4);
          color: #93c5fd;
          padding: 5px 14px;
          border-radius: 20px;
          font-size: 12px;
          font-weight: 700;
          letter-spacing: 0.8px;
          width: fit-content;
        }}
        .title-group {{
          margin: 10px 0;
        }}
        .main-title {{
          font-size: 38px;
          font-weight: 900;
          line-height: 1.2;
          color: #ffffff;
          letter-spacing: -0.5px;
          margin-bottom: 8px;
        }}
        .sub-title {{
          font-size: 21px;
          font-weight: 700;
          line-height: 1.35;
          background: linear-gradient(90deg, #60a5fa 0%, #38bdf8 100%);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          margin-bottom: 12px;
        }}
        .desc-text {{
          font-size: 13.5px;
          line-height: 1.6;
          color: #94a3b8;
        }}
        .bottom-badges {{
          display: flex;
          gap: 12px;
          align-items: center;
        }}
        .badge-pill {{
          font-size: 12px;
          font-weight: 600;
          padding: 5px 12px;
          border-radius: 6px;
          display: flex;
          align-items: center;
          gap: 6px;
        }}
        .badge-a {{
          background: rgba(249, 115, 22, 0.15);
          border: 1px solid rgba(249, 115, 22, 0.35);
          color: #fdba74;
        }}
        .badge-b {{
          background: rgba(16, 185, 129, 0.15);
          border: 1px solid rgba(16, 185, 129, 0.35);
          color: #6ee7b7;
        }}
        .right-col {{
          width: 420px;
          height: 100%;
          position: relative;
          z-index: 2;
          display: flex;
          flex-direction: column;
          justify-content: center;
        }}
        .product-stage {{
          background: rgba(15, 23, 42, 0.7);
          backdrop-filter: blur(12px);
          border: 1px solid rgba(255, 255, 255, 0.12);
          border-radius: 16px;
          padding: 20px 22px;
          box-shadow: 0 16px 36px rgba(0,0,0,0.35);
          display: flex;
          flex-direction: column;
        }}
        .stage-title {{
          font-size: 11.5px;
          font-weight: 700;
          color: #94a3b8;
          text-transform: uppercase;
          letter-spacing: 0.8px;
          text-align: center;
          margin-bottom: 14px;
          padding-bottom: 8px;
          border-bottom: 1px solid rgba(255,255,255,0.08);
          display: flex;
          justify-content: center;
          align-items: center;
          gap: 6px;
        }}
        .products-grid {{
          display: flex;
          align-items: center;
          justify-content: space-around;
          position: relative;
        }}
        .product-card {{
          display: flex;
          flex-direction: column;
          align-items: center;
          text-align: center;
          width: 165px;
        }}
        .img-wrap {{
          height: 190px;
          width: 100%;
          display: flex;
          align-items: center;
          justify-content: center;
          margin-bottom: 10px;
        }}
        .img-wrap img {{
          max-height: 100%;
          max-width: 100%;
          object-fit: contain;
          filter: drop-shadow(0 10px 20px rgba(0,0,0,0.45));
        }}
        .prod-name {{
          font-size: 13.5px;
          font-weight: 700;
          color: #ffffff;
          margin-bottom: 2px;
        }}
        .prod-spec {{
          font-size: 11.5px;
          color: #94a3b8;
        }}
        .vs-circle {{
          width: 32px;
          height: 32px;
          border-radius: 50%;
          background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
          border: 1px solid rgba(255, 255, 255, 0.2);
          display: flex;
          align-items: center;
          justify-content: center;
          font-size: 11px;
          font-weight: 800;
          color: #38bdf8;
          box-shadow: 0 4px 12px rgba(0,0,0,0.4);
          position: absolute;
          top: 38%;
          left: 50%;
          transform: translate(-50%, -50%);
          z-index: 5;
        }}
      </style>
    </head>
    <body>
      <div class="cover-container">
        <div class="bg-grid"></div>
        <div class="glow-left"></div>
        <div class="glow-right"></div>

        <div class="left-col">
          <div class="top-tag">
            <span>🔬 欧洲前沿学术情报</span>
            <span style="color:rgba(255,255,255,0.3)">|</span>
            <span>NCT06788015 · NCT05799911</span>
          </div>

          <div class="title-group">
            <h1 class="main-title">氢水有没有用？</h1>
            <h2 class="sub-title">欧洲已经跑完两个真实案例，档案在这里</h2>
            <p class="desc-text">两个在售商业品牌，两所公立大学，两场双盲交叉人体试验。一个自述四项全能改善；一个实测仅快了 0.6% 并公开全部原始数据。</p>
          </div>

          <div class="bottom-badges">
            <div class="badge-pill badge-a">● 案例 A：英国 HtoEAU（10人入组 · 结果未公开）</div>
            <div class="badge-pill badge-b">● 案例 B：捷克 Aquastamina（14人入组 · 2篇论文+开源数据）</div>
          </div>
        </div>

        <div class="right-col">
          <div class="product-stage">
            <div class="stage-title">
              <span>🛒 欧洲货架流通的真实商业产品</span>
            </div>
            <div class="products-grid">
              <!-- Product A -->
              <div class="product-card">
                <div class="img-wrap">
                  <img src="data:image/png;base64,{b64_a}" alt="英国 HtoEAU 罐装富氢水">
                </div>
                <div class="prod-name">HtoEAU®（英国）</div>
                <div class="prod-spec">5 mg/L · 定价 £2.49/罐</div>
              </div>

              <!-- VS Badge -->
              <div class="vs-circle">VS</div>

              <!-- Product B -->
              <div class="product-card">
                <div class="img-wrap">
                  <img src="data:image/png;base64,{b64_b}" alt="捷克 Aquastamina-R 袋装富氢水">
                </div>
                <div class="prod-name">Aquastamina-R（捷克）</div>
                <div class="prod-spec">0.9 ppm · 420 ml/袋</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </body>
    </html>
    """
    page.set_viewport_size({"width": 1080, "height": 600})
    page.set_content(html)
    out_file = os.path.join(OUT_DIR, "fig5-cover.png")
    page.locator(".cover-container").screenshot(path=out_file)
    print("✓ Generated fig5-cover.png with real products!")

def generate_zh_comparison_table(page):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      {BASE_STYLE_ZH}
      <style>
        .table-container {{
          width: 1080px;
          background: #ffffff;
          color: #0f172a;
          padding: 40px 44px;
          border: 1px solid #e2e8f0;
          border-top: 5px solid #1d4ed8;
          border-radius: 12px;
          box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        }}
        .header-box {{
          border-bottom: 2px solid #0f172a;
          padding-bottom: 18px;
          margin-bottom: 22px;
          display: flex;
          justify-content: space-between;
          align-items: flex-end;
        }}
        .header-title {{
          font-size: 25px;
          font-weight: 800;
          color: #0f172a;
          line-height: 1.3;
        }}
        .header-sub {{
          font-size: 14px;
          color: #64748b;
          margin-top: 4px;
        }}
        .header-badge {{
          background: #eff6ff;
          border: 1px solid #bfdbfe;
          color: #1d4ed8;
          font-size: 12px;
          font-weight: 700;
          padding: 5px 12px;
          border-radius: 6px;
          letter-spacing: 0.5px;
        }}
        table {{
          width: 100%;
          border-collapse: collapse;
          font-size: 13.5px;
          line-height: 1.55;
        }}
        th {{
          background: #0f172a;
          color: #ffffff;
          padding: 12px 16px;
          text-align: left;
          font-weight: 700;
          letter-spacing: 0.3px;
        }}
        th:first-child {{ width: 20%; border-radius: 6px 0 0 0; }}
        th:nth-child(2) {{ width: 40%; background: #1e293b; }}
        th:nth-child(3) {{ width: 40%; background: #0284c7; border-radius: 0 6px 0 0; }}
        td {{
          padding: 11px 16px;
          border-bottom: 1px solid #e2e8f0;
          vertical-align: top;
        }}
        tr:nth-child(even) td {{
          background: #f8fafc;
        }}
        .dim-cell {{
          font-weight: 700;
          color: #334155;
          background: #f1f5f9 !important;
          border-right: 1px solid #e2e8f0;
        }}
        .case-a-cell {{
          color: #1e293b;
          border-right: 1px solid #e2e8f0;
        }}
        .case-b-cell {{
          color: #0f172a;
        }}
        .pill-warn {{
          display: inline-block;
          background: #fff7ed;
          border: 1px solid #ffedd5;
          color: #c2410c;
          font-weight: 600;
          padding: 2px 8px;
          border-radius: 4px;
          font-size: 12px;
        }}
        .pill-ok {{
          display: inline-block;
          background: #ecfdf5;
          border: 1px solid #d1fae5;
          color: #047857;
          font-weight: 600;
          padding: 2px 8px;
          border-radius: 4px;
          font-size: 12px;
        }}
        .pill-mono {{
          font-family: 'JetBrains Mono', monospace;
          font-size: 12.5px;
          font-weight: 700;
        }}
        .footer-note {{
          margin-top: 20px;
          padding-top: 14px;
          border-top: 1px solid #e2e8f0;
          display: flex;
          justify-content: space-between;
          font-size: 12px;
          color: #64748b;
        }}
      </style>
    </head>
    <body>
      <div class="table-container">
        <div class="header-box">
          <div>
            <h2 class="header-title">欧洲氢水两个真实案例：全要素档案横向深度对照</h2>
            <p class="header-sub">对照监管注册、研究设计、入组样本、终点指标与科学发表真实状态</p>
          </div>
          <div class="header-badge">档案全要素对照</div>
        </div>

        <table>
          <thead>
            <tr>
              <th>对比维度</th>
              <th>案例 A · 英国品牌 HtoEAU</th>
              <th>案例 B · 捷克品牌 Aquastamina</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="dim-cell">企业主体</td>
              <td class="case-a-cell">HtoEAU <span class="pill-warn">主体未公开</span><br><span style="color:#64748b;font-size:12px;">英国商业定价；无公司注册号与 Impressum 页面</span></td>
              <td class="case-b-cell"><strong>Nutristamina s.r.o.</strong> <span class="pill-ok">实体可查</span><br><span style="color:#64748b;font-size:12px;">实体位于捷克俄斯特拉发（Ostrava）</span></td>
            </tr>
            <tr>
              <td class="dim-cell">产品与规格</td>
              <td class="case-a-cell">罐装冰川氢水，标称 <strong>5 mg/L</strong>，pH 8.3<br><span style="color:#64748b;font-size:12px;">定价 £2.49/罐（约合人民币 23 元，单罐约 330 ml）</span></td>
              <td class="case-b-cell">铝塑袋装富氢水，标称 <strong>0.9 ppm</strong>，pH 7.9<br><span style="color:#64748b;font-size:12px;">420 ml/袋，负电位 ORP 实测 −652 mV</span></td>
            </tr>
            <tr>
              <td class="dim-cell">市场在售状态</td>
              <td class="case-a-cell">已在售（官网在售 4 款 SKU）</td>
              <td class="case-b-cell">已上市（专供科研 + 商业流通）</td>
            </tr>
            <tr>
              <td class="dim-cell">临床注册号</td>
              <td class="case-a-cell"><span class="pill-mono" style="color:#1d4ed8;">NCT06788015</span>（缩写 HYDRO2EAU）</td>
              <td class="case-b-cell"><span class="pill-mono" style="color:#0284c7;">NCT05799911</span>（蹼泳运动员研究）</td>
            </tr>
            <tr>
              <td class="dim-cell">申办机构</td>
              <td class="case-a-cell">塞尔维亚诺维萨德大学 体育学院（FSPE）<br><span style="color:#64748b;font-size:12px;">主持学者：Sergej M. Ostojić 教授（H指数 41）</span></td>
              <td class="case-b-cell">捷克帕拉茨基大学 体育文化学院（FTK）<br><span style="color:#64748b;font-size:12px;">核心学者：M. Botek 教授、B. Sládečková 博士</span></td>
            </tr>
            <tr>
              <td class="dim-cell">试验设计</td>
              <td class="case-a-cell">随机 · 双盲 · 交叉 · 安慰剂对照</td>
              <td class="case-b-cell">随机 · 双盲 · 交叉 · 安慰剂对照</td>
            </tr>
            <tr>
              <td class="dim-cell">登记入组人数</td>
              <td class="case-a-cell"><strong>10 人（官网称 12 人）</strong><br><span style="color:#64748b;font-size:12px;">训练三年以上高校运动员；相当于 20 人次</span></td>
              <td class="case-b-cell"><strong>14 人入组（12 人完成）</strong><br><span style="color:#64748b;font-size:12px;">国家级高水平蹼泳运动员（8 女 4 男）</span></td>
            </tr>
            <tr>
              <td class="dim-cell">登记主要终点</td>
              <td class="case-a-cell"><strong>跑台力竭时间（Running time to exhaustion）</strong></td>
              <td class="case-b-cell"><strong>400 米水面蹼泳计时（400 m swimming time）</strong></td>
            </tr>
            <tr>
              <td class="dim-cell">结果公开状态</td>
              <td class="case-a-cell"><span class="pill-warn">❌ 未公开 / 无论文</span><br><span style="color:#64748b;font-size:12px;">注册页无 Results 栏；各大数据库未检索到对应论文</span></td>
              <td class="case-b-cell"><span class="pill-ok">✅ 2 篇国际顶刊同行评议论文 + 1 专著章节</span><br><span style="color:#64748b;font-size:12px;">发表于《IJSPP》2026 与《Frontiers in Physiol》2024</span></td>
            </tr>
            <tr>
              <td class="dim-cell">核心研究发现</td>
              <td class="case-a-cell">官网宣称四项指标显著改善（<strong>品牌自述</strong>）：<br>最大跑速 vmax、无氧阈速度 vANT、心理健康、SF-36</td>
              <td class="case-b-cell"><strong>400 米提升 0.6%（P=0.003，d=−0.07 微不足道）</strong><br><span style="color:#64748b;font-size:12px;">50米冲刺、乳酸、主观疲劳、蛋白羰基均无差异；8人阳性/4人无反应</span></td>
            </tr>
            <tr>
              <td class="dim-cell">原始数据状态</td>
              <td class="case-a-cell">仅供向研究者书面申请</td>
              <td class="case-b-cell"><span class="pill-ok">✅ Zenodo 全球学术库完全开源</span><br><span style="color:#64748b;font-size:12px;">DOI: 10.5281/zenodo.20492716 及 18184954</span></td>
            </tr>
          </tbody>
        </table>

        <div class="footer-note">
          <div>数据源自 ClinicalTrials.gov 官方登记页、PubMed 文献库及各品牌官网公开档案</div>
          <div>木齐科技情报团队校准整理 · 2026年10月17日</div>
        </div>
      </div>
    </body>
    </html>
    """
    page.set_viewport_size({"width": 1080, "height": 1400})
    page.set_content(html)
    out_file = os.path.join(OUT_DIR, "fig1-case-comparison-table.png")
    page.locator(".table-container").screenshot(path=out_file)
    print("✓ Generated fig1-case-comparison-table.png with locator screenshot (ZERO black bars)")

def generate_zh_four_endpoints_grid(page):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      {BASE_STYLE_ZH}
      <style>
        .grid-container {{
          width: 1080px;
          height: 1120px;
          background: #f8fafc;
          padding: 44px 48px;
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          border: 1px solid #e2e8f0;
          border-radius: 12px;
          box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        }}
        .grid-header {{
          border-bottom: 2px solid #e2e8f0;
          padding-bottom: 18px;
          display: flex;
          justify-content: space-between;
          align-items: flex-end;
        }}
        .grid-title {{
          font-size: 26px;
          font-weight: 800;
          color: #0f172a;
          line-height: 1.25;
        }}
        .grid-sub {{
          font-size: 14px;
          color: #64748b;
          margin-top: 4px;
        }}
        .tag-pill {{
          background: #eff6ff;
          color: #1d4ed8;
          border: 1px solid #bfdbfe;
          font-size: 12px;
          font-weight: 700;
          padding: 5px 12px;
          border-radius: 20px;
        }}
        .cards-wrapper {{
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 22px;
          margin: 22px 0;
          flex: 1;
        }}
        .endpoint-card {{
          background: #ffffff;
          border: 1px solid #e2e8f0;
          border-radius: 12px;
          padding: 24px 26px;
          display: flex;
          flex-direction: column;
          box-shadow: 0 2px 10px rgba(0,0,0,0.03);
          border-top: 4px solid #cbd5e1;
        }}
        .card-top {{
          display: flex;
          justify-content: space-between;
          align-items: flex-start;
          margin-bottom: 14px;
        }}
        .card-badge {{
          font-size: 11px;
          font-weight: 700;
          letter-spacing: 0.5px;
          padding: 4px 8px;
          border-radius: 6px;
        }}
        .badge-phys {{ background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; }}
        .badge-subj {{ background: #fdf2f8; color: #db2777; border: 1px solid #fbcfe8; }}
        .metric-id {{
          font-family: 'JetBrains Mono', monospace;
          font-size: 12.5px;
          color: #94a3b8;
          font-weight: 700;
        }}
        .card-title {{
          font-size: 20px;
          font-weight: 700;
          color: #0f172a;
          margin-bottom: 10px;
        }}
        .card-definition {{
          font-size: 13.5px;
          color: #475569;
          line-height: 1.55;
          margin-bottom: 14px;
          flex: 1;
        }}
        .translation-box {{
          background: #f8fafc;
          border-left: 3px solid #1d4ed8;
          padding: 10px 12px;
          border-radius: 0 6px 6px 0;
          font-size: 13px;
          color: #1e293b;
          line-height: 1.5;
        }}
        .translation-box strong {{
          color: #0f172a;
        }}
        .grid-footer {{
          border-top: 1px solid #e2e8f0;
          padding-top: 16px;
          display: flex;
          justify-content: space-between;
          font-size: 12px;
          color: #64748b;
        }}
      </style>
    </head>
    <body>
      <div class="grid-container">
        <div class="grid-header">
          <div>
            <h2 class="grid-title">案例 A 涉及的四项指标通俗拆解</h2>
            <p class="grid-sub">将运动生理客观参数与主观心理健康量表翻译为读者日常可感知的实际体验</p>
          </div>
          <div class="tag-pill">四宫格指标解析</div>
        </div>

        <div class="cards-wrapper">
          <!-- Card 1 -->
          <div class="endpoint-card" style="border-top-color: #2563eb;">
            <div class="card-top">
              <span class="card-badge badge-phys">客观身体机能</span>
              <span class="metric-id">01 / vmax</span>
            </div>
            <h3 class="card-title">最大跑速（vmax）</h3>
            <p class="card-definition">在递增负荷跑台测试中，受试者在达到急性力竭极限那一瞬间所能跑出的绝对极限速度。</p>
            <div class="translation-box" style="border-left-color: #2563eb;">
              <strong>通俗翻译：</strong>全力冲刺时能跑到的最高速度——就像追赶即将关门的早班公交车那一瞬间的极速。
            </div>
          </div>

          <!-- Card 2 -->
          <div class="endpoint-card" style="border-top-color: #0284c7;">
            <div class="card-top">
              <span class="card-badge badge-phys">客观耐力门槛</span>
              <span class="metric-id">02 / vANT</span>
            </div>
            <h3 class="card-title">无氧阈速度（vANT）</h3>
            <p class="card-definition">身体从有氧氧化代谢平稳供能，切换到体内开始快速、大量堆积血乳酸的临界速度拐点。</p>
            <div class="translation-box" style="border-left-color: #0284c7;">
              <strong>通俗翻译：</strong>你能一直跑、还不喘的那个速度。爬五楼不喘、慢跑半小时不累，全靠这个临界点支撑。
            </div>
          </div>

          <!-- Card 3 -->
          <div class="endpoint-card" style="border-top-color: #d946ef;">
            <div class="card-top">
              <span class="card-badge badge-subj">主观心理韧性</span>
              <span class="metric-id">03 / 心理评分</span>
            </div>
            <h3 class="card-title">心理健康状态评分</h3>
            <p class="card-definition">标准化心理量表评估，量化受试运动员在严苛训练周期内的情绪稳定性、压力应对力与日常幸福感。</p>
            <div class="translation-box" style="border-left-color: #d946ef;">
              <strong>通俗翻译：</strong>高强度备赛期内心态稳不稳、精力好不好、疲劳感与压力能否在两场比赛之间快速消化。
            </div>
          </div>

          <!-- Card 4 -->
          <div class="endpoint-card" style="border-top-color: #f43f5e;">
            <div class="card-top">
              <span class="card-badge badge-subj">生活质量金标准</span>
              <span class="metric-id">04 / SF-36 量表</span>
            </div>
            <h3 class="card-title">SF-36 一般健康调查量表</h3>
            <p class="card-definition">全球医学临床广泛应用的 36 题健康问卷，涵盖生理机能、身体疼痛、日常活力、社交功能与情感角色 8 个维度。</p>
            <div class="translation-box" style="border-left-color: #f43f5e;">
              <strong>通俗翻译：</strong>三甲医院临床科研常用的生活质量总分，客观量化一个人每天生龙活虎的综合健康状态。
            </div>
          </div>
        </div>

        <div class="grid-footer">
          <div>注：最大跑速与无氧阈速度为官网重点宣传项，但在其官方 NCT06788015 注册终点列表中并未列入</div>
          <div>木齐科普档案 · 科学阅读指引</div>
        </div>
      </div>
    </body>
    </html>
    """
    page.set_viewport_size({"width": 1080, "height": 1200})
    page.set_content(html)
    out_file = os.path.join(OUT_DIR, "fig2-four-endpoints-grid.png")
    page.locator(".grid-container").screenshot(path=out_file)
    print("✓ Generated fig2-four-endpoints-grid.png with locator screenshot")

def generate_zh_axis_chart(page):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      {BASE_STYLE_ZH}
      <style>
        .axis-container {{
          width: 1080px;
          height: 760px;
          background: #ffffff;
          padding: 44px 50px;
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          border: 1px solid #e2e8f0;
          border-bottom: 4px solid #0284c7;
          border-radius: 12px;
          box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        }}
        .axis-header {{
          border-bottom: 2px solid #e2e8f0;
          padding-bottom: 18px;
          display: flex;
          justify-content: space-between;
          align-items: flex-end;
        }}
        .axis-title {{
          font-size: 26px;
          font-weight: 800;
          color: #0f172a;
        }}
        .axis-sub {{
          font-size: 14.5px;
          color: #64748b;
          margin-top: 4px;
        }}
        .chart-box {{
          position: relative;
          margin: 30px 0;
          padding: 40px 20px;
          background: #f8fafc;
          border: 1px solid #e2e8f0;
          border-radius: 12px;
        }}
        .axis-line {{
          position: relative;
          height: 10px;
          background: #e2e8f0;
          border-radius: 5px;
          margin: 90px 40px 70px;
        }}
        .axis-fill {{
          position: absolute;
          left: 0;
          width: 60%;
          height: 100%;
          background: linear-gradient(90deg, #93c5fd 0%, #3b82f6 100%);
          border-radius: 5px;
        }}
        .tick {{
          position: absolute;
          top: -8px;
          width: 2px;
          height: 26px;
          background: #94a3b8;
        }}
        .tick-label {{
          position: absolute;
          top: 28px;
          transform: translateX(-50%);
          font-size: 14px;
          font-weight: 700;
          color: #334155;
          text-align: center;
        }}
        .tick-sub {{
          font-size: 11.5px;
          font-weight: 500;
          color: #64748b;
          white-space: nowrap;
        }}
        .pointer-box {{
          position: absolute;
          top: -95px;
          transform: translateX(-50%);
          background: #0f172a;
          color: #ffffff;
          padding: 10px 16px;
          border-radius: 8px;
          text-align: center;
          box-shadow: 0 4px 14px rgba(15, 23, 42, 0.2);
        }}
        .pointer-box::after {{
          content: '';
          position: absolute;
          bottom: -7px;
          left: 50%;
          transform: translateX(-50%);
          border-width: 7px 7px 0;
          border-style: solid;
          border-color: #0f172a transparent transparent;
        }}
        .pointer-val {{
          font-size: 20px;
          font-weight: 800;
          color: #38bdf8;
        }}
        .pointer-p {{
          font-size: 12px;
          color: #94a3b8;
          font-family: 'JetBrains Mono', monospace;
        }}
        .info-cards {{
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 20px;
        }}
        .info-card {{
          background: #ffffff;
          border: 1px solid #e2e8f0;
          border-radius: 10px;
          padding: 18px 20px;
        }}
        .info-card h4 {{
          font-size: 15px;
          font-weight: 700;
          color: #0f172a;
          margin-bottom: 6px;
          display: flex;
          align-items: center;
          gap: 8px;
        }}
        .info-card p {{
          font-size: 13.5px;
          color: #475569;
          line-height: 1.55;
        }}
        .axis-footer {{
          border-top: 1px solid #e2e8f0;
          padding-top: 14px;
          display: flex;
          justify-content: space-between;
          font-size: 12px;
          color: #64748b;
        }}
      </style>
    </head>
    <body>
      <div class="axis-container">
        <div class="axis-header">
          <div>
            <h2 class="axis-title">0.6% 在最小有意义变化数轴上的真实位置</h2>
            <p class="axis-sub">基于捷克研究《IJSPP》2026 论文原文：竞技体育门槛与统计效应量的双重视角解读</p>
          </div>
          <div style="background:#f0fdf4;color:#166534;border:1px solid #bbf7d0;padding:5px 12px;border-radius:6px;font-size:12px;font-weight:700;">IJSPP 实测数据</div>
        </div>

        <div class="chart-box">
          <div class="axis-line">
            <div class="axis-fill"></div>

            <!-- Baseline 0.0% -->
            <div class="tick" style="left: 0%;">
              <div class="tick-label">0.0%<div class="tick-sub">安慰剂对照基线</div></div>
            </div>

            <!-- SWC Threshold 0.4% -->
            <div class="tick" style="left: 40%; background: #f97316;">
              <div class="tick-label" style="color: #c2410c;">+0.4%<div class="tick-sub">SWC 阈值（取两赛变异二分之一）</div></div>
            </div>

            <!-- Measured 0.6% -->
            <div class="tick" style="left: 60%; background: #0284c7;">
              <div class="pointer-box" style="left: 60%;">
                <div class="pointer-val">+0.6%</div>
                <div class="pointer-p">P = 0.003 · 达到 1.5 倍 SWC</div>
              </div>
              <div class="tick-label" style="color: #0284c7;">+0.6%<div class="tick-sub">富氢水实测提升（400米约快1.3秒）</div></div>
            </div>

            <!-- Max Reference 1.0% -->
            <div class="tick" style="left: 100%;">
              <div class="tick-label">+1.0%<div class="tick-sub">高水准竞技基准</div></div>
            </div>
          </div>
        </div>

        <div class="info-cards">
          <div class="info-card" style="border-left: 4px solid #0284c7;">
            <h4><span style="color:#0284c7;">●</span> 判据 A：竞技体育现实视角（SWC 判据）</h4>
            <p>国家级高水平蹼泳中，最小有意义变化阈值 SWC 为 <strong>0.4%</strong>。实测提升 <strong>0.6%</strong> 是该阈值的 <strong>1.5 倍</strong>，在统计学上显著（P = 0.003），且跨过了高水平竞技的有效分水岭。</p>
          </div>
          <div class="info-card" style="border-left: 4px solid #f97316;">
            <h4><span style="color:#f97316;">●</span> 判据 B：统计学效应量视角（Cohen's d）</h4>
            <p>从标准差度量，Cohen's <strong>d = −0.07</strong>，作者定性为<strong>微不足道（trivial）</strong>。绝对差值为 225.2 秒 vs 226.5 秒（相差约 1.3 秒），且血乳酸并无显著变化（P ≥ 0.12）。</p>
          </div>
        </div>

        <div class="axis-footer">
          <div>出处：Sladeckova B, et al. Int J Sports Physiol Perform. 2026;21(7):824-830. Table 2.</div>
          <div>木齐学术情报 · 严谨数据红线复核</div>
        </div>
      </div>
    </body>
    </html>
    """
    page.set_viewport_size({"width": 1080, "height": 850})
    page.set_content(html)
    out_file = os.path.join(OUT_DIR, "fig3-0-6-percent-axis.png")
    page.locator(".axis-container").screenshot(path=out_file)
    print("✓ Generated fig3-0-6-percent-axis.png with locator screenshot")

def generate_zh_timeline(page):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      {BASE_STYLE_ZH}
      <style>
        .timeline-container {{
          width: 1080px;
          height: 960px;
          background: #ffffff;
          padding: 44px 50px;
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          border: 1px solid #e2e8f0;
          border-bottom: 4px solid #1e293b;
          border-radius: 12px;
          box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        }}
        .timeline-header {{
          border-bottom: 2px solid #e2e8f0;
          padding-bottom: 18px;
          display: flex;
          justify-content: space-between;
          align-items: flex-end;
        }}
        .tl-title {{
          font-size: 26px;
          font-weight: 800;
          color: #0f172a;
        }}
        .tl-sub {{
          font-size: 14.5px;
          color: #64748b;
          margin-top: 4px;
        }}
        .timelines-split {{
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 36px;
          margin: 20px 0;
          flex: 1;
        }}
        .tl-column {{
          background: #f8fafc;
          border: 1px solid #e2e8f0;
          border-radius: 12px;
          padding: 24px 22px;
          display: flex;
          flex-direction: column;
        }}
        .col-header {{
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding-bottom: 14px;
          border-bottom: 1px solid #e2e8f0;
          margin-bottom: 18px;
        }}
        .col-title {{
          font-size: 17px;
          font-weight: 800;
          color: #0f172a;
        }}
        .step-item {{
          position: relative;
          padding-left: 28px;
          margin-bottom: 18px;
        }}
        .step-item:last-child {{ margin-bottom: 0; }}
        .step-item::before {{
          content: '';
          position: absolute;
          left: 7px;
          top: 6px;
          width: 10px;
          height: 10px;
          border-radius: 50%;
          background: #cbd5e1;
          border: 2px solid #ffffff;
          box-shadow: 0 0 0 2px #94a3b8;
        }}
        .step-item::after {{
          content: '';
          position: absolute;
          left: 11px;
          top: 20px;
          bottom: -12px;
          width: 2px;
          background: #e2e8f0;
        }}
        .step-item:last-child::after {{ display: none; }}
        .step-active::before {{ background: #2563eb; box-shadow: 0 0 0 2px #2563eb; }}
        .step-warn::before {{ background: #f97316; box-shadow: 0 0 0 2px #f97316; }}
        .step-ok::before {{ background: #10b981; box-shadow: 0 0 0 2px #10b981; }}
        .step-date {{
          font-family: 'JetBrains Mono', monospace;
          font-size: 12px;
          font-weight: 700;
          color: #64748b;
          margin-bottom: 2px;
        }}
        .step-title {{
          font-size: 14.5px;
          font-weight: 700;
          color: #1e293b;
          margin-bottom: 3px;
        }}
        .step-desc {{
          font-size: 13px;
          color: #64748b;
          line-height: 1.45;
        }}
        .tl-footer {{
          border-top: 1px solid #e2e8f0;
          padding-top: 14px;
          display: flex;
          justify-content: space-between;
          font-size: 12px;
          color: #64748b;
        }}
      </style>
    </head>
    <body>
      <div class="timeline-container">
        <div class="timeline-header">
          <div>
            <h2 class="tl-title">两个案例发表与公开时间线对照</h2>
            <p class="tl-sub">从临床试验设计、正式注册到数据披露与同行评议论文的真实推进轨迹</p>
          </div>
          <div style="background:#f1f5f9;color:#334155;border:1px solid #cbd5e1;padding:5px 12px;border-radius:6px;font-size:12px;font-weight:700;">时间线核验</div>
        </div>

        <div class="timelines-split">
          <!-- Column A -->
          <div class="tl-column" style="border-top: 4px solid #f97316;">
            <div class="col-header">
              <div class="col-title">案例 A：英国 HtoEAU</div>
              <span style="font-size:12px;font-weight:700;color:#c2410c;background:#fff7ed;padding:3px 8px;border-radius:4px;">NCT06788015</span>
            </div>

            <div class="step-item step-active">
              <div class="step-date">2024年11月15日</div>
              <div class="step-title">试验方案正式开始执行</div>
              <div class="step-desc">塞尔维亚诺维萨德大学启动 4 周双盲交叉试验，受试者为 10 名高校运动员。</div>
            </div>

            <div class="step-item">
              <div class="step-date">2025年01月10日</div>
              <div class="step-title">ClinicalTrials.gov 注册成功</div>
              <div class="step-desc">生成官方 NCT06788015 编号，锁定主要终点为跑台力竭时间（time to exhaustion）。</div>
            </div>

            <div class="step-item">
              <div class="step-date">2025年02月28日</div>
              <div class="step-title">主要终点指标测试完成</div>
              <div class="step-desc">完成全部受试者双盲交叉各阶段力竭指标与生理生化数据采集。</div>
            </div>

            <div class="step-item step-warn">
              <div class="step-date">2025年03月</div>
              <div class="step-title">品牌官网发布自述研究报告</div>
              <div class="step-desc">官网宣称四项指标显著改善（品牌自述），并冠以“亚洲以外首个临床研究”推广。</div>
            </div>

            <div class="step-item step-warn">
              <div class="step-date">2026年10月17日（核验时点）</div>
              <div class="step-title">官方注册无结果，公开库无论文</div>
              <div class="step-desc">官方注册页始终无 Results 栏，国际学术数据库中未检索到同行评议对应论文。</div>
            </div>
          </div>

          <!-- Column B -->
          <div class="tl-column" style="border-top: 4px solid #10b981;">
            <div class="col-header">
              <div class="col-title">案例 B：捷克 Aquastamina</div>
              <span style="font-size:12px;font-weight:700;color:#047857;background:#ecfdf5;padding:3px 8px;border-radius:4px;">NCT05799911</span>
            </div>

            <div class="step-item step-active">
              <div class="step-date">2023年04月11日</div>
              <div class="step-title">官方注册并启动入组测试</div>
              <div class="step-desc">帕拉茨基大学完成 NCT05799911 注册，Nutristamina 公司严格按双盲编码供样。</div>
            </div>

            <div class="step-item">
              <div class="step-date">2023年05月31日</div>
              <div class="step-title">试验顺利完成（12人完成分析）</div>
              <div class="step-desc">12 名国家级蹼泳运动员完成全部交叉测试，采集 400 米、50 米及全套生理生化数据。</div>
            </div>

            <div class="step-item step-ok">
              <div class="step-date">2024年04月12日</div>
              <div class="step-title">论文①发表于《Front Physiol》</div>
              <div class="step-desc">先行发表肌肉恢复机理方向论文（PMID: 38681143），同年刊载 Springer 专著章节。</div>
            </div>

            <div class="step-item step-ok">
              <div class="step-date">2024年06月</div>
              <div class="step-title">Zenodo 平台公开完整原始数据集</div>
              <div class="step-desc">按照欧洲开源科学标准，将全部脱敏原始矩阵公开并分配独立 DOI。</div>
            </div>

            <div class="step-item step-ok">
              <div class="step-date">2026年04月16日</div>
              <div class="step-title">论文②发表于《IJSPP》（披露0.6%）</div>
              <div class="step-desc">完整报告 400 米提升 0.6% 以及其余四项无差异的真实结果，坚持客观呈现阴性数据。</div>
            </div>
          </div>
        </div>

        <div class="tl-footer">
          <div>时间节点严格以 ClinicalTrials.gov 官方历史更新记录及已发表论文公开信息为准</div>
          <div>木齐学术情报 · 欧洲真实案例追踪</div>
        </div>
      </div>
    </body>
    </html>
    """
    page.set_viewport_size({"width": 1080, "height": 1050})
    page.set_content(html)
    out_file = os.path.join(OUT_DIR, "fig4-two-cases-timeline.png")
    page.locator(".timeline-container").screenshot(path=out_file)
    print("✓ Generated fig4-two-cases-timeline.png with locator screenshot")

def sync_to_package():
    # Sync to release package
    os.makedirs(PKG_DIR, exist_ok=True)
    mapping = {
        "fig1-case-comparison-table.png": "图1_档案对照表.png",
        "fig2-four-endpoints-grid.png": "图2_四项指标四宫格.png",
        "fig3-0-6-percent-axis.png": "图3_0.6%数轴.png",
        "fig4-two-cases-timeline.png": "图4_两个案例时间线.png",
        "fig5-cover.png": "图5_公众号封面.png",
    }
    for src, dst in mapping.items():
        src_path = os.path.join(OUT_DIR, src)
        dst_path = os.path.join(PKG_DIR, dst)
        with open(src_path, 'rb') as f_src, open(dst_path, 'wb') as f_dst:
            f_dst.write(f_src.read())
        print(f"✓ Synced {src} -> {dst}")

def main():
    print("Starting Playwright Chinese infographic generator with locator screenshots...")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=2) # 2x DPR for crisp retina display
        
        generate_zh_cover(page)
        generate_zh_comparison_table(page)
        generate_zh_four_endpoints_grid(page)
        generate_zh_axis_chart(page)
        generate_zh_timeline(page)
        
        browser.close()
    
    sync_to_package()
    print("All Chinese infographics successfully re-generated and synced!")

if __name__ == '__main__':
    main()
