#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate professional English infographics for the European Hydrogen Water Cases blog post.
Rendered via Playwright with 2x Device Pixel Ratio for crystal-clear retina display.
Features authentic market products on the cover image alongside English title and clinical IDs.
"""

import os
import base64
from playwright.sync_api import sync_playwright

OUT_DIR = "assets/images/blog/european-hydrogen-water-cases"
os.makedirs(OUT_DIR, exist_ok=True)

# Common styling & font stack
BASE_STYLE = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: #0f172a;
    color: #f8fafc;
    -webkit-font-smoothing: antialiased;
  }
</style>
"""

def get_base64_img(rel_path):
    with open(rel_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def generate_cover(page):
    b64_a = get_base64_img("assets/images/blog/european-hydrogen-water-cases/case_a_htoeau_product_cans.png")
    b64_b = get_base64_img("assets/images/blog/european-hydrogen-water-cases/case_b_aquastamina_product.png")

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      {BASE_STYLE}
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
          border-bottom: 4px solid #2563eb;
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
          background: radial-gradient(circle, rgba(37, 99, 235, 0.25) 0%, transparent 70%);
          pointer-events: none;
        }}
        .glow-right {{
          position: absolute;
          bottom: -100px;
          right: -100px;
          width: 450px;
          height: 450px;
          background: radial-gradient(circle, rgba(2, 132, 199, 0.22) 0%, transparent 70%);
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
          background: rgba(30, 58, 138, 0.4);
          border: 1px solid rgba(96, 165, 250, 0.35);
          color: #93c5fd;
          padding: 5px 14px;
          border-radius: 20px;
          font-size: 11.5px;
          font-weight: 700;
          letter-spacing: 0.8px;
          text-transform: uppercase;
          width: fit-content;
        }}
        .title-group {{
          margin: 12px 0;
        }}
        .main-title {{
          font-size: 36px;
          font-weight: 900;
          line-height: 1.18;
          color: #ffffff;
          letter-spacing: -0.5px;
          margin-bottom: 8px;
        }}
        .sub-title {{
          font-size: 19px;
          font-weight: 700;
          line-height: 1.35;
          background: linear-gradient(90deg, #60a5fa 0%, #38bdf8 100%);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          margin-bottom: 12px;
        }}
        .desc-text {{
          font-size: 13.5px;
          line-height: 1.55;
          color: #94a3b8;
        }}
        .bottom-badges {{
          display: flex;
          gap: 12px;
          align-items: center;
        }}
        .badge-pill {{
          font-size: 11.5px;
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
          font-size: 11px;
          font-weight: 700;
          color: #94a3b8;
          text-transform: uppercase;
          letter-spacing: 1px;
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
          transition: transform 0.2s;
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
          font-family: 'JetBrains Mono', monospace;
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
            <span>🔬 Clinical Dossier</span>
            <span style="color:rgba(255,255,255,0.3)">|</span>
            <span>NCT06788015 · NCT05799911</span>
          </div>

          <div class="title-group">
            <h1 class="main-title">Does Hydrogen Water Work?</h1>
            <h2 class="sub-title">Two Real-World European Market Cases & Their Full Dossiers</h2>
            <p class="desc-text">Two commercial brands on shelves, two randomized crossover trials. One claimed universal gains; the other measured +0.6% alongside null endpoints and open data.</p>
          </div>

          <div class="bottom-badges">
            <div class="badge-pill badge-a">● UK HtoEAU · 10 Enrolled · Unpublished</div>
            <div class="badge-pill badge-b">● Czech Aquastamina-R · 14 Enrolled · Open Data</div>
          </div>
        </div>

        <div class="right-col">
          <div class="product-stage">
            <div class="stage-title">
              <span>🛒 Real Commercial Products on Shelves</span>
            </div>
            <div class="products-grid">
              <!-- Product A -->
              <div class="product-card">
                <div class="img-wrap">
                  <img src="data:image/png;base64,{b64_a}" alt="HtoEAU Canned Hydrogen Water">
                </div>
                <div class="prod-name">HtoEAU® (UK)</div>
                <div class="prod-spec">5 mg/L · £2.49 / Can</div>
              </div>

              <!-- VS Badge -->
              <div class="vs-circle">VS</div>

              <!-- Product B -->
              <div class="product-card">
                <div class="img-wrap">
                  <img src="data:image/png;base64,{b64_b}" alt="Aquastamina-R Hydrogen Water Pouch">
                </div>
                <div class="prod-name">Aquastamina-R (CZ)</div>
                <div class="prod-spec">0.9 ppm · 420 mL Pouch</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </body>
    </html>
    """
    page.set_viewport_size({"width": 1080, "height": 460})
    page.set_content(html)
    page.screenshot(path=os.path.join(OUT_DIR, "fig5-cover-en.png"))
    print("✓ Generated fig5-cover-en.png with real products!")

def generate_comparison_table(page):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      {BASE_STYLE}
      <style>
        .table-container {{
          width: 1080px;
          background: #ffffff;
          color: #0f172a;
          padding: 44px 48px;
          box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }}
        .header-box {{
          border-bottom: 2px solid #0f172a;
          padding-bottom: 20px;
          margin-bottom: 24px;
          display: flex;
          justify-content: space-between;
          align-items: flex-end;
        }}
        .header-title {{
          font-size: 26px;
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
          padding: 6px 14px;
          border-radius: 6px;
          text-transform: uppercase;
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
          padding: 13px 16px;
          text-align: left;
          font-weight: 700;
          letter-spacing: 0.3px;
        }}
        th:first-child {{ width: 22%; border-radius: 6px 0 0 0; }}
        th:nth-child(2) {{ width: 39%; background: #1e293b; }}
        th:nth-child(3) {{ width: 39%; background: #0284c7; border-radius: 0 6px 0 0; }}
        td {{
          padding: 12px 16px;
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
          margin-top: 24px;
          padding-top: 16px;
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
            <h2 class="header-title">Full Dossier Comparison: Two Real European Hydrogen Water Cases</h2>
            <p class="header-sub">Side-by-side verification of regulatory registration, study design, reported outcomes, and scientific publication</p>
          </div>
          <div class="header-badge">Evidence Matrix</div>
        </div>

        <table>
          <thead>
            <tr>
              <th>Dimension</th>
              <th>Case A · UK Brand HtoEAU</th>
              <th>Case B · Czech Aquastamina</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="dim-cell">Corporate Entity</td>
              <td class="case-a-cell">HtoEAU <span class="pill-warn">Legal Entity Undisclosed</span><br><span style="color:#64748b;font-size:12px;">UK retail pricing; no company registry details</span></td>
              <td class="case-b-cell"><strong>Nutristamina s.r.o.</strong> <span class="pill-ok">Verifiable Entity</span><br><span style="color:#64748b;font-size:12px;">Based in Ostrava, Czech Republic</span></td>
            </tr>
            <tr>
              <td class="dim-cell">Product Formulation</td>
              <td class="case-a-cell">Canned glacial H₂ water, <strong>5 mg/L</strong>, pH 8.3<br><span style="color:#64748b;font-size:12px;">Retail from £2.49 / can (~330 mL)</span></td>
              <td class="case-b-cell">Aluminum-plastic pouch, <strong>0.9 ppm</strong>, pH 7.9<br><span style="color:#64748b;font-size:12px;">420 mL / pouch, ORP −652 mV</span></td>
            </tr>
            <tr>
              <td class="dim-cell">Commercial Status</td>
              <td class="case-a-cell">Actively marketed online (4 SKUs listed)</td>
              <td class="case-b-cell">Commercially marketed (retail & research supply)</td>
            </tr>
            <tr>
              <td class="dim-cell">Trial Registry ID</td>
              <td class="case-a-cell"><span class="pill-mono" style="color:#1d4ed8;">NCT06788015</span> (HYDRO2EAU)</td>
              <td class="case-b-cell"><span class="pill-mono" style="color:#0284c7;">NCT05799911</span> (Fin-swimmers H₂)</td>
            </tr>
            <tr>
              <td class="dim-cell">Sponsoring Institution</td>
              <td class="case-a-cell">University of Novi Sad, FSPE (Serbia)<br><span style="color:#64748b;font-size:12px;">Lead Investigator: Prof. Sergej Ostojić</span></td>
              <td class="case-b-cell">Palacký University Olomouc, FTK (Czechia)<br><span style="color:#64748b;font-size:12px;">Lead Authors: M. Botek, B. Sládečková, J. Krejčí</span></td>
            </tr>
            <tr>
              <td class="dim-cell">Protocol Design</td>
              <td class="case-a-cell">Randomized · Double-blind · Crossover · Placebo</td>
              <td class="case-b-cell">Randomized · Double-blind · Crossover · Placebo</td>
            </tr>
            <tr>
              <td class="dim-cell">Subject Enrollment</td>
              <td class="case-a-cell"><strong>10 registered</strong> (12 claimed on website)<br><span style="color:#64748b;font-size:12px;">Collegiate athletes; 20 participant-periods</span></td>
              <td class="case-b-cell"><strong>14 enrolled</strong> (12 completed: 8 female, 4 male)<br><span style="color:#64748b;font-size:12px;">National-level competitive finswimmers</span></td>
            </tr>
            <tr>
              <td class="dim-cell">Primary Registered Outcome</td>
              <td class="case-a-cell"><strong>Treadmill time to exhaustion</strong></td>
              <td class="case-b-cell"><strong>400-meter finswimming time trial</strong></td>
            </tr>
            <tr>
              <td class="dim-cell">Outcome Transparency</td>
              <td class="case-a-cell"><span class="pill-warn">❌ Unpublished / No Results Posted</span><br><span style="color:#64748b;font-size:12px;">Registry lacks Results section; no paper found</span></td>
              <td class="case-b-cell"><span class="pill-ok">✅ 2 Peer-Reviewed Papers + Book Chapter</span><br><span style="color:#64748b;font-size:12px;">Published in IJSPP 2026 & Front Physiol 2024</span></td>
            </tr>
            <tr>
              <td class="dim-cell">Key Reported Findings</td>
              <td class="case-a-cell">Four metrics claimed improved (<strong>brand self-report</strong>):<br>vmax, vANT, mental health, SF-36 score</td>
              <td class="case-b-cell"><strong>+0.6% in 400 m (P = 0.003, d = −0.07 trivial)</strong><br><span style="color:#64748b;font-size:12px;">Zero difference in 50 m sprint, lactate, RPE, or protein carbonyls; 8 responders / 4 non-responders</span></td>
            </tr>
            <tr>
              <td class="dim-cell">Raw Dataset Status</td>
              <td class="case-a-cell">Available only upon private request</td>
              <td class="case-b-cell"><span class="pill-ok">✅ Fully Open on Zenodo</span><br><span style="color:#64748b;font-size:12px;">DOIs: 10.5281/zenodo.20492716 & 18184954</span></td>
            </tr>
          </tbody>
        </table>

        <div class="footer-note">
          <div>Data audited from ClinicalTrials.gov, PubMed, IJSPP, and respective brand websites</div>
          <div>Compiled by MQ Technology Research · Oct 17, 2026</div>
        </div>
      </div>
    </body>
    </html>
    """
    page.set_viewport_size({"width": 1080, "height": 1380})
    page.set_content(html)
    page.screenshot(path=os.path.join(OUT_DIR, "fig1-case-comparison-table-en.png"))
    print("✓ Generated fig1-case-comparison-table-en.png")

def generate_four_endpoints_grid(page):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      {BASE_STYLE}
      <style>
        .grid-container {{
          width: 1080px;
          height: 1120px;
          background: #f8fafc;
          padding: 48px;
          display: flex;
          flex-direction: column;
          justify-content: space-between;
        }}
        .grid-header {{
          border-bottom: 2px solid #e2e8f0;
          padding-bottom: 20px;
          display: flex;
          justify-content: space-between;
          align-items: flex-end;
        }}
        .grid-title {{
          font-size: 28px;
          font-weight: 800;
          color: #0f172a;
          line-height: 1.25;
        }}
        .grid-sub {{
          font-size: 14.5px;
          color: #64748b;
          margin-top: 6px;
        }}
        .tag-pill {{
          background: #eff6ff;
          color: #1d4ed8;
          border: 1px solid #bfdbfe;
          font-size: 12px;
          font-weight: 700;
          padding: 6px 14px;
          border-radius: 20px;
          text-transform: uppercase;
        }}
        .cards-wrapper {{
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 24px;
          margin: 24px 0;
          flex: 1;
        }}
        .endpoint-card {{
          background: #ffffff;
          border: 1px solid #e2e8f0;
          border-radius: 14px;
          padding: 28px;
          display: flex;
          flex-direction: column;
          box-shadow: 0 4px 16px rgba(0,0,0,0.03);
          border-top: 5px solid #cbd5e1;
        }}
        .card-top {{
          display: flex;
          justify-content: space-between;
          align-items: flex-start;
          margin-bottom: 16px;
        }}
        .card-badge {{
          font-size: 11.5px;
          font-weight: 700;
          text-transform: uppercase;
          letter-spacing: 0.5px;
          padding: 4px 10px;
          border-radius: 6px;
        }}
        .badge-phys {{ background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; }}
        .badge-subj {{ background: #fdf2f8; color: #db2777; border: 1px solid #fbcfe8; }}
        .metric-id {{
          font-family: 'JetBrains Mono', monospace;
          font-size: 13px;
          color: #94a3b8;
          font-weight: 700;
        }}
        .card-title {{
          font-size: 20px;
          font-weight: 700;
          color: #0f172a;
          margin-bottom: 12px;
        }}
        .card-definition {{
          font-size: 14px;
          color: #475569;
          line-height: 1.6;
          margin-bottom: 16px;
          flex: 1;
        }}
        .translation-box {{
          background: #f8fafc;
          border-left: 3px solid #1d4ed8;
          padding: 12px 14px;
          border-radius: 0 8px 8px 0;
          font-size: 13.5px;
          color: #1e293b;
          line-height: 1.5;
        }}
        .translation-box strong {{
          color: #0f172a;
        }}
        .grid-footer {{
          border-top: 1px solid #e2e8f0;
          padding-top: 18px;
          display: flex;
          justify-content: space-between;
          font-size: 12.5px;
          color: #64748b;
        }}
      </style>
    </head>
    <body>
      <div class="grid-container">
        <div class="grid-header">
          <div>
            <h2 class="grid-title">The Four Evaluated Endpoints in Plain English</h2>
            <p class="grid-sub">Deconstructing the athletic performance and subjective wellbeing markers evaluated in Case A</p>
          </div>
          <div class="tag-pill">Endpoint Analysis</div>
        </div>

        <div class="cards-wrapper">
          <!-- Card 1 -->
          <div class="endpoint-card" style="border-top-color: #2563eb;">
            <div class="card-top">
              <span class="card-badge badge-phys">Objective Physical Capacity</span>
              <span class="metric-id">01 / vmax</span>
            </div>
            <h3 class="card-title">Maximum Running Velocity (vmax)</h3>
            <p class="card-definition">The absolute peak sprinting velocity achieved during an incremental treadmill ramp test before acute physiological exhaustion sets in.</p>
            <div class="translation-box" style="border-left-color: #2563eb;">
              <strong>Everyday Translation:</strong> Your top burst speed—comparable to the all-out sprint to catch a closing subway door.
            </div>
          </div>

          <!-- Card 2 -->
          <div class="endpoint-card" style="border-top-color: #0284c7;">
            <div class="card-top">
              <span class="card-badge badge-phys">Objective Physical Capacity</span>
              <span class="metric-id">02 / vANT</span>
            </div>
            <h3 class="card-title">Anaerobic Threshold Velocity (vANT)</h3>
            <p class="card-definition">The highest sustainable velocity where aerobic cellular metabolism dominates before systemic blood lactic acid begins to accumulate exponentially.</p>
            <div class="translation-box" style="border-left-color: #0284c7;">
              <strong>Everyday Translation:</strong> The maximum pace you can maintain continuously without feeling breathless or legs cramping up.
            </div>
          </div>

          <!-- Card 3 -->
          <div class="endpoint-card" style="border-top-color: #d946ef;">
            <div class="card-top">
              <span class="card-badge badge-subj">Psychological Wellbeing</span>
              <span class="metric-id">03 / Mental Score</span>
            </div>
            <h3 class="card-title">Mental Health Assessment Score</h3>
            <p class="card-definition">Standardized psychometric questionnaire measuring subjective mood regulation, cognitive stress resilience, emotional stability, and overall vitality.</p>
            <div class="translation-box" style="border-left-color: #d946ef;">
              <strong>Everyday Translation:</strong> How recovered, mentally sharp, and stress-resilient an athlete feels between demanding competitive blocks.
            </div>
          </div>

          <!-- Card 4 -->
          <div class="endpoint-card" style="border-top-color: #f43f5e;">
            <div class="card-top">
              <span class="card-badge badge-subj">Quality of Life Instrument</span>
              <span class="metric-id">04 / SF-36 Score</span>
            </div>
            <h3 class="card-title">SF-36 General Health Survey</h3>
            <p class="card-definition">The gold-standard 36-item questionnaire assessing 8 domains: physical functioning, bodily pain, vitality, social functioning, and emotional role limitations.</p>
            <div class="translation-box" style="border-left-color: #f43f5e;">
              <strong>Everyday Translation:</strong> Comprehensive life quality index widely used in hospital clinical research to benchmark daily vitality.
            </div>
          </div>
        </div>

        <div class="grid-footer">
          <div>Note: vmax and vANT were featured on brand website but not registered as official primary endpoints on NCT06788015.</div>
          <div>MQ Research Dossier · Clinical Literacy</div>
        </div>
      </div>
    </body>
    </html>
    """
    page.set_viewport_size({"width": 1080, "height": 1120})
    page.set_content(html)
    page.screenshot(path=os.path.join(OUT_DIR, "fig2-four-endpoints-grid-en.png"))
    print("✓ Generated fig2-four-endpoints-grid-en.png")

def generate_axis_chart(page):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      {BASE_STYLE}
      <style>
        .axis-container {{
          width: 1080px;
          height: 760px;
          background: #ffffff;
          padding: 44px 50px;
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          border-bottom: 4px solid #0284c7;
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
            <h2 class="axis-title">Where Does +0.6% Stand on the SWC Number Axis?</h2>
            <p class="axis-sub">Evaluating Case B's 400 m time trial against Smallest Worthwhile Change & effect size thresholds</p>
          </div>
          <div style="background:#f0fdf4;color:#166534;border:1px solid #bbf7d0;padding:5px 12px;border-radius:6px;font-size:12px;font-weight:700;">IJSPP 2026 Audit</div>
        </div>

        <div class="chart-box">
          <div class="axis-line">
            <div class="axis-fill"></div>

            <!-- Baseline 0.0% -->
            <div class="tick" style="left: 0%;">
              <div class="tick-label">0.0%<div class="tick-sub">Placebo Baseline</div></div>
            </div>

            <!-- SWC Threshold 0.4% -->
            <div class="tick" style="left: 40%; background: #f97316;">
              <div class="tick-label" style="color: #c2410c;">+0.4%<div class="tick-sub">SWC Threshold (1/2 between-comp variation)</div></div>
            </div>

            <!-- Measured 0.6% -->
            <div class="tick" style="left: 60%; background: #0284c7;">
              <div class="pointer-box" style="left: 60%;">
                <div class="pointer-val">+0.6%</div>
                <div class="pointer-p">P = 0.003 · 1.5× SWC</div>
              </div>
              <div class="tick-label" style="color: #0284c7;">+0.6%<div class="tick-sub">Measured HRW Effect (~1.3s in 400m)</div></div>
            </div>

            <!-- Max Reference 1.0% -->
            <div class="tick" style="left: 100%;">
              <div class="tick-label">+1.0%<div class="tick-sub">Benchmark Boundary</div></div>
            </div>
          </div>
        </div>

        <div class="info-cards">
          <div class="info-card" style="border-left: 4px solid #0284c7;">
            <h4><span style="color:#0284c7;">●</span> Criterion A: Competitive Swimming Context</h4>
            <p>In national-level finswimming, the threshold for meaningful improvement is SWC = <strong>0.4%</strong>. The measured <strong>+0.6%</strong> improvement is <strong>1.5 times the SWC</strong> and statistically significant (P = 0.003).</p>
          </div>
          <div class="info-card" style="border-left: 4px solid #f97316;">
            <h4><span style="color:#f97316;">●</span> Criterion B: Population Effect Size (Cohen's d)</h4>
            <p>From the standard deviation scale, Cohen's <strong>d = −0.07</strong>, classified by authors as <strong>trivial</strong>. Absolute difference was 225.2 s vs 226.5 s (~1.3 s), and blood lactate showed zero difference (P ≥ 0.12).</p>
          </div>
        </div>

        <div class="axis-footer">
          <div>Sladeckova B, et al. Int J Sports Physiol Perform. 2026;21(7):824-830. Table 2.</div>
          <div>MQ Research Dossier · Clinical Integrity Rule</div>
        </div>
      </div>
    </body>
    </html>
    """
    page.set_viewport_size({"width": 1080, "height": 760})
    page.set_content(html)
    page.screenshot(path=os.path.join(OUT_DIR, "fig3-0-6-percent-axis-en.png"))
    print("✓ Generated fig3-0-6-percent-axis-en.png")

def generate_timeline(page):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      {BASE_STYLE}
      <style>
        .timeline-container {{
          width: 1080px;
          height: 960px;
          background: #ffffff;
          padding: 44px 50px;
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          border-bottom: 4px solid #1e293b;
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
            <h2 class="tl-title">Two Timelines, Two Outcomes: Progression from Protocol to Publication</h2>
            <p class="tl-sub">Tracing how both crossover studies evolved through registration, field execution, and scientific disclosure</p>
          </div>
          <div style="background:#f1f5f9;color:#334155;border:1px solid #cbd5e1;padding:5px 12px;border-radius:6px;font-size:12px;font-weight:700;">Audit Timeline</div>
        </div>

        <div class="timelines-split">
          <!-- Column A -->
          <div class="tl-column" style="border-top: 4px solid #f97316;">
            <div class="col-header">
              <div class="col-title">Case A: UK Brand HtoEAU</div>
              <span style="font-size:12px;font-weight:700;color:#c2410c;background:#fff7ed;padding:3px 8px;border-radius:4px;">NCT06788015</span>
            </div>

            <div class="step-item step-active">
              <div class="step-date">Nov 15, 2024</div>
              <div class="step-title">Study Protocol Commenced</div>
              <div class="step-desc">University of Novi Sad initiated 4-week double-blind crossover trial on 10 collegiate athletes.</div>
            </div>

            <div class="step-item">
              <div class="step-date">Jan 10, 2025</div>
              <div class="step-title">Registered on ClinicalTrials.gov</div>
              <div class="step-desc">Official NCT06788015 record created. Primary outcome locked as treadmill time to exhaustion.</div>
            </div>

            <div class="step-item">
              <div class="step-date">Feb 28, 2025</div>
              <div class="step-title">Primary Completion Date</div>
              <div class="step-desc">All participant data collection completed for registered primary endpoints.</div>
            </div>

            <div class="step-item step-warn">
              <div class="step-date">Mar 2025</div>
              <div class="step-title">Commercial Website Cites Report</div>
              <div class="step-desc">Brand website features "March 2025 full report", asserting 4 improved metrics (brand self-report).</div>
            </div>

            <div class="step-item step-warn">
              <div class="step-date">Oct 17, 2026 (Audited)</div>
              <div class="step-title">Results Withheld & Zero Papers</div>
              <div class="step-desc">Clinical registry has no Results section. No corresponding peer-reviewed publication indexed.</div>
            </div>
          </div>

          <!-- Column B -->
          <div class="tl-column" style="border-top: 4px solid #10b981;">
            <div class="col-header">
              <div class="col-title">Case B: Czech Aquastamina</div>
              <span style="font-size:12px;font-weight:700;color:#047857;background:#ecfdf5;padding:3px 8px;border-radius:4px;">NCT05799911</span>
            </div>

            <div class="step-item step-active">
              <div class="step-date">Apr 11, 2023</div>
              <div class="step-title">Registration & Protocol Launch</div>
              <div class="step-desc">Palacký University Olomouc registered NCT05799911 with Nutristamina s.r.o. providing blinded batches.</div>
            </div>

            <div class="step-item">
              <div class="step-date">May 31, 2023</div>
              <div class="step-title">Study Completion (12 Completed)</div>
              <div class="step-desc">12 competitive finswimmers completed full crossover trials with complete physiological biomarker panels.</div>
            </div>

            <div class="step-item step-ok">
              <div class="step-date">Apr 12, 2024</div>
              <div class="step-title">Paper ① in Frontiers in Physiology</div>
              <div class="step-desc">Published muscle recovery findings (PMID: 38681143); accompanied by Springer book chapter.</div>
            </div>

            <div class="step-item step-ok">
              <div class="step-date">Jun 2024</div>
              <div class="step-title">Raw Datasets Deposited on Zenodo</div>
              <div class="step-desc">Full anonymized trial matrices released publicly under open-access science mandates (DOIs assigned).</div>
            </div>

            <div class="step-item step-ok">
              <div class="step-date">Apr 16, 2026</div>
              <div class="step-title">Paper ② in IJSPP (+0.6% & Null Disclosed)</div>
              <div class="step-desc">Comprehensive reporting of +0.6% performance change alongside null lactate/RPE findings.</div>
            </div>
          </div>
        </div>

        <div class="tl-footer">
          <div>Comparative timeline derived from ClinicalTrials.gov registration histories and PubMed release records.</div>
          <div>MQ Research Dossier · Publication Hygiene</div>
        </div>
      </div>
    </body>
    </html>
    """
    page.set_viewport_size({"width": 1080, "height": 960})
    page.set_content(html)
    page.screenshot(path=os.path.join(OUT_DIR, "fig4-two-cases-timeline-en.png"))
    print("✓ Generated fig4-two-cases-timeline-en.png")

def main():
    print("Starting Playwright infographic generator...")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=2) # 2x DPR for ultra-crisp retina output
        
        generate_cover(page)
        generate_comparison_table(page)
        generate_four_endpoints_grid(page)
        generate_axis_chart(page)
        generate_timeline(page)
        
        browser.close()
    print("All English infographics successfully generated!")

if __name__ == '__main__':
    main()
