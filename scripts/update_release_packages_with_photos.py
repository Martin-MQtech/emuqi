#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update release package markdown and HTML files with real-world photo evidence.
"""

import os

pkg_dir = '/Users/martin/Documents/2026 BUSINESS MTRIX /20260601 MQ TECH 国际业务/20260708 MQ TECH 国际市场市场划分/欧洲氢医学学术圈/发布包_20261017_氢水两个欧洲案例'

def update_zh_md():
    md_zh_file = os.path.join(pkg_dir, '07_公众号与博客全平台发布稿_中文版.md')
    with open(md_zh_file, 'r', encoding='utf-8') as f:
        zh = f.read()

    card_a1_md = '''
> 📸 **真实商业产品与品牌档案 · 案例 A**
>
> ![英国 HtoEAU 罐装富氢水真实在售实物](https://www.emuqi.com/assets/images/blog/european-hydrogen-water-cases/case_a_htoeau_product_cans.png)
> *图：英国市场流通的 HtoEAU 罐装冰川富氢水实物（标称 5 mg/L，定价 £2.49/罐，单罐约 330 ml）与品牌标识*
'''

    card_a2_md = '''
> 🎓 **真实主持学者与学术机构档案 · 案例 A**
>
> ![主持本项试验的 Sergej M. Ostojić 教授肖像](https://www.emuqi.com/assets/images/blog/european-hydrogen-water-cases/case_a_prof_sergej_ostojic.jpg)
> *图：主持研究学者 Sergej M. Ostojić 教授（塞尔维亚诺维萨德大学生物医学教授、MHI 科学顾问，发表论文 320+ 篇，H 指数 41）与诺维萨德大学主校区实景*
'''

    card_b1_md = '''
> 📸 **真实商业产品与企业档案 · 案例 B**
>
> ![捷克 Aquastamina-R 袋装富氢水实物](https://www.emuqi.com/assets/images/blog/european-hydrogen-water-cases/case_b_aquastamina_product.png)
> *图：Nutristamina 生产的 Aquastamina-R 铝塑袋装富氢水实物（规格 420 ml，实测浓度 0.9 ppm）与捷克 Nutristamina s.r.o. 企业标识*
'''

    card_b2_md = '''
> 🎓 **真实科研团队与实验室现场 · 案例 B**
>
> ![帕拉茨基大学 Michal Botek 教授与分子氢实验室](https://www.emuqi.com/assets/images/blog/european-hydrogen-water-cases/case_b_prof_michal_botek.jpg)
> *图：通讯作者 Michal Botek 教授、帕拉茨基大学 FTK 运动生理与分子氢科研团队实验现场与捷克帕拉茨基大学历史校区*
'''

    if 'case_a_htoeau_product_cans.png' not in zh:
        t_a1 = '定价 £2.49 一罐（按汇率估算约合人民币 23 元）。'
        zh = zh.replace(t_a1, t_a1 + '\n\n' + card_a1_md)

        t_a2 = '品牌官网称他是“亚洲以外第一个发表氢水临床研究的人”。'
        zh = zh.replace(t_a2, t_a2 + '\n\n' + card_a2_md)

        t_b1 = '包装外观完全一致，仅通过内部批号区分。'
        zh = zh.replace(t_b1, t_b1 + '\n\n' + card_b1_md)

        t_b2 = '连出资供样的厂家都无法在测试期间获知哪包是真品、哪包是安慰剂，这构成了真正严格的科研双盲。'
        zh = zh.replace(t_b2, t_b2 + '\n\n' + card_b2_md)

        with open(md_zh_file, 'w', encoding='utf-8') as f:
            f.write(zh)
        print('Updated 07_公众号与博客全平台发布稿_中文版.md successfully!')

def update_en_md():
    md_en_file = os.path.join(pkg_dir, '08_英文博客与国际发布稿_EN.md')
    with open(md_en_file, 'r', encoding='utf-8') as f:
        en = f.read()

    card_a1_en_md = '''
> 📸 **Real Commercial Product & Brand Dossier · Case A**
>
> ![HtoEAU Canned Hydrogen Water Commercial Product](https://www.emuqi.com/assets/images/blog/european-hydrogen-water-cases/case_a_htoeau_product_cans.png)
> *Figure: Commercial HtoEAU canned hydrogen water on UK market (£2.49/can, labeled 5 mg/L, approx. 330 mL/can) and official brand insignia.*
'''

    card_a2_en_md = '''
> 🎓 **Principal Investigator & Academic Institution Dossier · Case A**
>
> ![Prof. Sergej M. Ostojic MD PhD](https://www.emuqi.com/assets/images/blog/european-hydrogen-water-cases/case_a_prof_sergej_ostojic.jpg)
> *Figure: Principal Investigator Prof. Sergej M. Ostojić, MD, PhD (University of Novi Sad; MHI Advisory Panel; 320+ articles, H-index 41) and the central campus of University of Novi Sad, Serbia.*
'''

    card_b1_en_md = '''
> 📸 **Real Commercial Product & Enterprise Dossier · Case B**
>
> ![Aquastamina-R Hydrogen-Rich Water Pouch](https://www.emuqi.com/assets/images/blog/european-hydrogen-water-cases/case_b_aquastamina_product.png)
> *Figure: Aquastamina-R 420 mL aluminum-plastic pouch (0.9 ppm dissolved H₂) manufactured by Nutristamina s.r.o. (Ostrava, Czech Republic).*
'''

    card_b2_en_md = '''
> 🎓 **Research Team & Active Laboratory Dossier · Case B**
>
> ![Prof. Michal Botek PhD and Exercise Physiology Laboratory](https://www.emuqi.com/assets/images/blog/european-hydrogen-water-cases/case_b_prof_michal_botek.jpg)
> *Figure: Corresponding author Prof. PhDr. Michal Botek, Ph.D. and the molecular hydrogen research team testing athletes at Palacký University Olomouc, Czech Republic.*
'''

    if 'case_a_htoeau_product_cans.png' not in en:
        t_a1_en = 'It retails from £2.49 per can.'
        en = en.replace(t_a1_en, t_a1_en + '\n\n' + card_a1_en_md)

        t_a2_en = 'clinical research on hydrogen water."'
        en = en.replace(t_a2_en, t_a2_en + '\n\n' + card_a2_en_md)

        t_b1_en = 'distinguishable only by internal batch codes.'
        en = en.replace(t_b1_en, t_b1_en + '\n\n' + card_b1_en_md)

        t_b2_en = 'this study adhered to strict double-blind standards.'
        en = en.replace(t_b2_en, t_b2_en + '\n\n' + card_b2_en_md)

        with open(md_en_file, 'w', encoding='utf-8') as f:
            f.write(en)
        print('Updated 08_英文博客与国际发布稿_EN.md successfully!')

if __name__ == '__main__':
    update_zh_md()
    update_en_md()
