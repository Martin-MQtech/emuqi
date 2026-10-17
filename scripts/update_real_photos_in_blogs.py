#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update Chinese and English blogs, WeChat HTML, and Markdown files with real-world photo evidence:
- Case A: HtoEAU product cans, HtoEAU logo, Prof. Sergej Ostojic, University of Novi Sad
- Case B: Aquastamina product pouches, Nutristamina logo, Prof. Michal Botek, Palacký University laboratory, Palacký University historic campus
"""

import os
import re

CSS_BLOCK = '''
    /* Real photo evidence cards */
    .photo-evidence-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      overflow: hidden;
      margin: 24px 0 28px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.04);
    }
    .photo-evidence-header {
      background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
      padding: 10px 18px;
      font-size: 13.5px;
      font-weight: 700;
      color: #1e293b;
      display: flex;
      align-items: center;
      gap: 8px;
      border-bottom: 1px solid #cbd5e1;
    }
    .photo-evidence-body {
      padding: 16px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      align-items: stretch;
    }
    .photo-item {
      text-align: center;
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      align-items: center;
      box-sizing: border-box;
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .photo-item:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(0,0,0,0.06);
    }
    .photo-item img {
      max-height: 200px;
      width: auto;
      max-width: 100%;
      object-fit: contain;
      border-radius: 6px;
      margin-bottom: 10px;
    }
    .photo-caption {
      font-size: 13px;
      color: #475569;
      line-height: 1.5;
      margin-top: auto;
      text-align: left;
      width: 100%;
    }
'''

def update_chinese_blog():
    filepath = 'zh/blog/european-hydrogen-water-cases.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    if '.photo-evidence-card' not in html:
        html = html.replace('</style>', CSS_BLOCK + '\n  </style>')

    # 1. Case A Product card
    case_a_product = '''
    <div class="photo-evidence-card">
      <div class="photo-evidence-header">
        <span>📸</span> <span>真实商业产品与品牌档案 · 案例 A（英国 HtoEAU）</span>
      </div>
      <div class="photo-evidence-body">
        <div class="photo-item">
          <img src="/assets/images/blog/european-hydrogen-water-cases/case_a_htoeau_product_cans.png" alt="英国 HtoEAU 罐装富氢水真实在售实物" loading="lazy">
          <div class="photo-caption"><strong>真实在售实物</strong>：英国市场流通的 HtoEAU 罐装冰川富氢水（标称 5 mg/L，定价 £2.49/罐，单罐约 330 ml）。</div>
        </div>
        <div class="photo-item">
          <img src="/assets/images/blog/european-hydrogen-water-cases/case_a_htoeau_logo.png" alt="英国 HtoEAU 官方商业标识" style="max-height:90px;margin:auto 0;" loading="lazy">
          <div class="photo-caption"><strong>企业与商业标识</strong>：HtoEAU 商业标识（定位英国高端运动与机能饮用水，官网主打冰岛冰川水源）。</div>
        </div>
      </div>
    </div>
'''

    target_a1 = '定价 £2.49 一罐（按汇率估算约合人民币 23 元）。</p>'
    if target_a1 in html and 'case_a_htoeau_product_cans.png' not in html:
        html = html.replace(target_a1, target_a1 + '\n' + case_a_product)

    # 2. Case A Professor & University card
    case_a_prof = '''
    <div class="photo-evidence-card">
      <div class="photo-evidence-header">
        <span>🎓</span> <span>真实主持学者与学术机构档案 · 案例 A（塞尔维亚诺维萨德大学）</span>
      </div>
      <div class="photo-evidence-body">
        <div class="photo-item">
          <img src="/assets/images/blog/european-hydrogen-water-cases/case_a_prof_sergej_ostojic.jpg" alt="主持本项试验的 Sergej M. Ostojić 教授肖像" loading="lazy">
          <div class="photo-caption"><strong>主持研究学者</strong>：Sergej M. Ostojić 教授（塞尔维亚诺维萨德大学生物医学教授、MHI 科学顾问，发表论文 320+ 篇，H 指数 41）。</div>
        </div>
        <div class="photo-item">
          <img src="/assets/images/blog/european-hydrogen-water-cases/case_a_university_novi_sad.jpg" alt="塞尔维亚诺维萨德大学主校区实景" loading="lazy">
          <div class="photo-caption"><strong>试验执行机构</strong>：塞尔维亚诺维萨德大学（University of Novi Sad）主校区，由其体育与运动教育学院应用生物能量学实验室开展试验。</div>
        </div>
      </div>
    </div>
'''

    target_a2 = '品牌官网称他是“亚洲以外第一个发表氢水临床研究的人”。</p>'
    if target_a2 in html and 'case_a_prof_sergej_ostojic.jpg' not in html:
        html = html.replace(target_a2, target_a2 + '\n' + case_a_prof)

    # 3. Case B Product & Company card
    case_b_product = '''
    <div class="photo-evidence-card">
      <div class="photo-evidence-header">
        <span>📸</span> <span>真实商业产品与企业档案 · 案例 B（捷克 Nutristamina）</span>
      </div>
      <div class="photo-evidence-body">
        <div class="photo-item">
          <img src="/assets/images/blog/european-hydrogen-water-cases/case_b_aquastamina_product.png" alt="捷克 Aquastamina-R 袋装富氢水实物" loading="lazy">
          <div class="photo-caption"><strong>真实在售实物</strong>：Nutristamina 生产的 Aquastamina-R 铝塑袋装富氢水（规格 420 ml，实测浓度 0.9 ppm，专供科研与专业运动市场）。</div>
        </div>
        <div class="photo-item">
          <img src="/assets/images/blog/european-hydrogen-water-cases/case_b_nutristamina_logo.png" alt="捷克 Nutristamina s.r.o. 企业标识" style="max-height:85px;margin:auto 0;" loading="lazy">
          <div class="photo-caption"><strong>研发与供样企业</strong>：Nutristamina s.r.o.（坐落于捷克俄斯特拉发，专注分子氢水及运动营养机能补充剂的实体企业）。</div>
        </div>
      </div>
    </div>
'''

    target_b1 = '包装外观完全一致，仅通过内部批号区分。</p>'
    if target_b1 in html and 'case_b_aquastamina_product.png' not in html:
        html = html.replace(target_b1, target_b1 + '\n' + case_b_product)

    # 4. Case B Professor & University Laboratory card
    case_b_prof = '''
    <div class="photo-evidence-card">
      <div class="photo-evidence-header">
        <span>🎓</span> <span>真实科研团队与实验室现场 · 案例 B（捷克帕拉茨基大学）</span>
      </div>
      <div class="photo-evidence-body" style="grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));">
        <div class="photo-item">
          <img src="/assets/images/blog/european-hydrogen-water-cases/case_b_prof_michal_botek.jpg" alt="帕拉茨基大学 Michal Botek 教授肖像" loading="lazy">
          <div class="photo-caption"><strong>通讯作者与负责人</strong>：Michal Botek 教授（捷克帕拉茨基大学体育文化学院运动生理学教授，主攻分子氢生物医学效应与自主神经调节）。</div>
        </div>
        <div class="photo-item">
          <img src="/assets/images/blog/european-hydrogen-water-cases/case_b_palacky_university_lab.jpg" alt="帕拉茨基大学分子氢实验室研究现场" loading="lazy">
          <div class="photo-caption"><strong>真实科研现场</strong>：帕拉茨基大学 FTK 运动生理与分子氢科研团队正在进行受试者高负荷体能与生理指标检测。</div>
        </div>
        <div class="photo-item">
          <img src="/assets/images/blog/european-hydrogen-water-cases/case_b_palacky_university.jpg" alt="捷克帕拉茨基大学主校区历史建筑" loading="lazy">
          <div class="photo-caption"><strong>学术试验依托单位</strong>：捷克帕拉茨基大学（Palacký University Olomouc，始建于 1573 年的中欧顶尖公立研究型大学）。</div>
        </div>
      </div>
    </div>
'''

    target_b2 = '连出资供样的厂家都无法在测试期间获知哪包是真品、哪包是安慰剂，这构成了真正严格的科研双盲。</p>'
    if target_b2 in html and 'case_b_prof_michal_botek.jpg' not in html:
        html = html.replace(target_b2, target_b2 + '\n' + case_b_prof)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ Chinese blog updated successfully!")

def update_english_blog():
    filepath = 'blog/european-hydrogen-water-cases-en.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    if '.photo-evidence-card' not in html:
        html = html.replace('</style>', CSS_BLOCK + '\n  </style>')

    # 1. Case A Product card (EN)
    case_a_product_en = '''
    <div class="photo-evidence-card">
      <div class="photo-evidence-header">
        <span>📸</span> <span>Real Commercial Product & Brand Dossier · Case A (UK HtoEAU)</span>
      </div>
      <div class="photo-evidence-body">
        <div class="photo-item">
          <img src="/assets/images/blog/european-hydrogen-water-cases/case_a_htoeau_product_cans.png" alt="Commercial HtoEAU canned hydrogen water product" loading="lazy">
          <div class="photo-caption"><strong>Verifiable Product on Shelf</strong>: UK commercial HtoEAU canned hydrogen water (labeled 5 mg/L, retail £2.49/can, approx. 330 mL/can).</div>
        </div>
        <div class="photo-item">
          <img src="/assets/images/blog/european-hydrogen-water-cases/case_a_htoeau_logo.png" alt="HtoEAU official commercial brand logo" style="max-height:90px;margin:auto 0;" loading="lazy">
          <div class="photo-caption"><strong>Brand Identity</strong>: Official HtoEAU brand insignia, positioned in the UK premium functional beverage sector citing Icelandic glacial water.</div>
        </div>
      </div>
    </div>
'''

    target_a1_en = 'It retails from £2.49 per can.</p>'
    if target_a1_en in html and 'case_a_htoeau_product_cans.png' not in html:
        html = html.replace(target_a1_en, target_a1_en + '\n' + case_a_product_en)

    # 2. Case A Professor & University card (EN)
    case_a_prof_en = '''
    <div class="photo-evidence-card">
      <div class="photo-evidence-header">
        <span>🎓</span> <span>Investigator & Academic Institution Dossier · Case A (University of Novi Sad)</span>
      </div>
      <div class="photo-evidence-body">
        <div class="photo-item">
          <img src="/assets/images/blog/european-hydrogen-water-cases/case_a_prof_sergej_ostojic.jpg" alt="Prof. Sergej M. Ostojic MD PhD" loading="lazy">
          <div class="photo-caption"><strong>Principal Investigator</strong>: Prof. Sergej M. Ostojić, MD, PhD (University of Novi Sad; MHI Advisory Panel member; 320+ publications, H-index 41).</div>
        </div>
        <div class="photo-item">
          <img src="/assets/images/blog/european-hydrogen-water-cases/case_a_university_novi_sad.jpg" alt="University of Novi Sad Main Campus" loading="lazy">
          <div class="photo-caption"><strong>Executing Institution</strong>: University of Novi Sad Central Campus (Serbia), whose FSPE Applied Bioenergetics Lab executed the protocol.</div>
        </div>
      </div>
    </div>
'''

    target_a2_en = 'clinical research on hydrogen water."</p>'
    if target_a2_en in html and 'case_a_prof_sergej_ostojic.jpg' not in html:
        html = html.replace(target_a2_en, target_a2_en + '\n' + case_a_prof_en)

    # 3. Case B Product & Company card (EN)
    case_b_product_en = '''
    <div class="photo-evidence-card">
      <div class="photo-evidence-header">
        <span>📸</span> <span>Real Commercial Product & Enterprise Dossier · Case B (Czech Nutristamina)</span>
      </div>
      <div class="photo-evidence-body">
        <div class="photo-item">
          <img src="/assets/images/blog/european-hydrogen-water-cases/case_b_aquastamina_product.png" alt="Aquastamina-R hydrogen-rich water pouch" loading="lazy">
          <div class="photo-caption"><strong>Verifiable Product on Shelf</strong>: Aquastamina-R 420 mL aluminum-plastic pouch (tested at 0.9 ppm dissolved H₂, commercialized by Nutristamina).</div>
        </div>
        <div class="photo-item">
          <img src="/assets/images/blog/european-hydrogen-water-cases/case_b_nutristamina_logo.png" alt="Nutristamina s.r.o. corporate logo" style="max-height:85px;margin:auto 0;" loading="lazy">
          <div class="photo-caption"><strong>Manufacturing Enterprise</strong>: Nutristamina s.r.o. (based in Ostrava, Czech Republic, specializing in molecular hydrogen hydration & sports nutrition).</div>
        </div>
      </div>
    </div>
'''

    target_b1_en = 'distinguishable only by internal batch codes.</p>'
    if target_b1_en in html and 'case_b_aquastamina_product.png' not in html:
        html = html.replace(target_b1_en, target_b1_en + '\n' + case_b_product_en)

    # 4. Case B Professor & University Laboratory card (EN)
    case_b_prof_en = '''
    <div class="photo-evidence-card">
      <div class="photo-evidence-header">
        <span>🎓</span> <span>Research Team & Laboratory Dossier · Case B (Palacký University Olomouc)</span>
      </div>
      <div class="photo-evidence-body" style="grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));">
        <div class="photo-item">
          <img src="/assets/images/blog/european-hydrogen-water-cases/case_b_prof_michal_botek.jpg" alt="Prof. Michal Botek PhD" loading="lazy">
          <div class="photo-caption"><strong>Corresponding Author</strong>: Prof. PhDr. Michal Botek, Ph.D. (Faculty of Physical Culture, Palacký University Olomouc, specializing in exercise physiology & H₂).</div>
        </div>
        <div class="photo-item">
          <img src="/assets/images/blog/european-hydrogen-water-cases/case_b_palacky_university_lab.jpg" alt="Palacký University Exercise Physiology Laboratory" loading="lazy">
          <div class="photo-caption"><strong>Active Research Facility</strong>: The molecular hydrogen research team at FTK UPOL conducting exercise physiology and performance diagnostic testing.</div>
        </div>
        <div class="photo-item">
          <img src="/assets/images/blog/european-hydrogen-water-cases/case_b_palacky_university.jpg" alt="Palacký University Olomouc Historic Campus" loading="lazy">
          <div class="photo-caption"><strong>Executing University</strong>: Palacký University Olomouc (Czech Republic), established in 1573 as one of Central Europe's leading public research universities.</div>
        </div>
      </div>
    </div>
'''

    target_b2_en = 'the study adhered to strict double-blind standards.</p>'
    if target_b2_en in html and 'case_b_prof_michal_botek.jpg' not in html:
        html = html.replace(target_b2_en, target_b2_en + '\n' + case_b_prof_en)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ English blog updated successfully!")

if __name__ == '__main__':
    update_chinese_blog()
    update_english_blog()
