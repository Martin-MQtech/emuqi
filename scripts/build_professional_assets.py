import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def build_all_assets():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, '..'))
    img_dir = os.path.join(base_dir, 'assets', 'images', 'blog', 'copyright-certificates')
    os.makedirs(img_dir, exist_ok=True)

    uploaded_dir = '/Users/martin/.gemini/antigravity/brain/2b676739-7daa-4138-91a0-91ad20da2377/.user_uploaded'
    raw_national_path = os.path.join(uploaded_dir, 'media_1792136999670_a6e2ceb0.png')
    raw_lab_path = os.path.join(uploaded_dir, 'media_1792136329559_3f3fe592.png')
    raw_icr_path = os.path.join(uploaded_dir, 'media_1792136342513_323f2d38.png')
    raw_diagram_path = os.path.join(uploaded_dir, 'media_1792137221910_5a59e583.png')

    font_bold = '/System/Library/Fonts/Hiragino Sans GB.ttc'
    font_reg = '/System/Library/Fonts/STHeiti Light.ttc'

    print("=== Step 1: Processing National Certificate (Perspective Rectification & Archival Restoration) ===")
    img_nat = cv2.imread(raw_national_path)
    
    # 4-point homography mapping outer guilloche border + margin
    border_src = np.float32([
        [28.62, 24.06],
        [1010.66, 16.70],
        [1016.04, 734.77],
        [34.00, 742.13]
    ])
    target_w, target_h = 1200, 880
    margin = 24
    border_dst = np.float32([
        [margin, margin],
        [target_w - margin, margin],
        [target_w - margin, target_h - margin],
        [margin, target_h - margin]
    ])

    M = cv2.getPerspectiveTransform(border_src, border_dst)
    warped = cv2.warpPerspective(img_nat, M, (target_w, target_h), flags=cv2.INTER_LANCZOS4)
    inside = warped[margin:target_h-margin, margin:target_w-margin]

    # LAB Illumination Normalization
    lab = cv2.cvtColor(inside, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (41, 41))
    bg = cv2.morphologyEx(l, cv2.MORPH_CLOSE, kernel)
    bg = np.maximum(bg, 1)
    l_norm = np.clip((l.astype(np.float32) / bg.astype(np.float32)) * 248.0, 0, 255).astype(np.uint8)
    
    p2, p98 = np.percentile(l_norm, (3, 98))
    l_stretched = np.clip((l_norm.astype(np.float32) - p2) / (p98 - p2) * 255.0, 0, 255).astype(np.uint8)

    enhanced_bgr = cv2.cvtColor(cv2.merge([l_stretched, a, b]), cv2.COLOR_LAB2BGR)

    # Boost red stamp saturation
    hsv = cv2.cvtColor(enhanced_bgr, cv2.COLOR_BGR2HSV)
    h_ch, s_ch, v_ch = cv2.split(hsv)
    mask_red = ((h_ch < 12) | (h_ch > 165)) & (s_ch > 30) & (v_ch > 50)
    s_ch[mask_red] = np.clip(s_ch[mask_red].astype(np.float32) * 1.35, 0, 255).astype(np.uint8)
    v_ch[mask_red] = np.clip(v_ch[mask_red].astype(np.float32) * 1.05, 0, 255).astype(np.uint8)
    vibrant_bgr = cv2.cvtColor(cv2.merge([h_ch, s_ch, v_ch]), cv2.COLOR_HSV2BGR)

    blur = cv2.GaussianBlur(vibrant_bgr, (0, 0), 1.2)
    final_inside = cv2.addWeighted(vibrant_bgr, 1.35, blur, -0.35, 0)

    # Framed institutional canvas (1260 x 940)
    canvas_nat = np.full((target_h + 60, target_w + 60, 3), 255, dtype=np.uint8)
    canvas_nat[:, :, 0] = 248  # Ivory paper
    canvas_nat[:, :, 1] = 252
    canvas_nat[:, :, 2] = 254

    y_off = 30 + margin
    x_off = 30 + margin
    canvas_nat[y_off:y_off+final_inside.shape[0], x_off:x_off+final_inside.shape[1]] = final_inside

    # Elegant subtle border lines
    cv2.rectangle(canvas_nat, (28, 28), (canvas_nat.shape[1]-28, canvas_nat.shape[0]-28), (210, 218, 225), 1, cv2.LINE_AA)
    cv2.rectangle(canvas_nat, (25, 25), (canvas_nat.shape[1]-25, canvas_nat.shape[0]-25), (235, 240, 245), 1, cv2.LINE_AA)

    out_nat_png = os.path.join(img_dir, 'cert-icr-technology-national-text.png')
    out_nat_webp = os.path.join(img_dir, 'cert-icr-technology-national-text.webp')
    cv2.imwrite(out_nat_png, canvas_nat)
    Image.fromarray(cv2.cvtColor(canvas_nat, cv2.COLOR_BGR2RGB)).save(out_nat_webp, 'WEBP', quality=92)
    print("Saved rectified National Certificate:", out_nat_png, out_nat_webp)

    print("\n=== Step 2: Processing Provincial Fine Art Certificates (2x Super-Resolution & Clarity Boost) ===")
    for slug, raw_path in [('cert-solid-hydrogen-lab', raw_lab_path), ('cert-icr-technology', raw_icr_path)]:
        im_prov = cv2.imread(raw_path)
        # Crop certificate page (Page 1)
        p1 = im_prov[8:505, 7:676]
        # 2x Upscale via Lanczos4
        up = cv2.resize(p1, (p1.shape[1] * 2, p1.shape[0] * 2), interpolation=cv2.INTER_LANCZOS4)
        
        # LAB CLAHE contrast boost
        lab = cv2.cvtColor(up, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=1.6, tileGridSize=(8, 8))
        l_clahe = clahe.apply(l)
        enhanced = cv2.cvtColor(cv2.merge([l_clahe, a, b]), cv2.COLOR_LAB2BGR)

        # Red stamp boost
        hsv = cv2.cvtColor(enhanced, cv2.COLOR_BGR2HSV)
        h_ch, s_ch, v_ch = cv2.split(hsv)
        mask_red = ((h_ch < 15) | (h_ch > 165)) & (s_ch > 40)
        s_ch[mask_red] = np.clip(s_ch[mask_red].astype(np.float32) * 1.3, 0, 255).astype(np.uint8)
        vibrant = cv2.cvtColor(cv2.merge([h_ch, s_ch, v_ch]), cv2.COLOR_HSV2BGR)

        blur = cv2.GaussianBlur(vibrant, (0, 0), 1.2)
        sharp = cv2.addWeighted(vibrant, 1.35, blur, -0.35, 0)

        # Framed canvas
        canvas_prov = np.full((sharp.shape[0] + 50, sharp.shape[1] + 50, 3), 255, dtype=np.uint8)
        canvas_prov[:, :, 0] = 248
        canvas_prov[:, :, 1] = 252
        canvas_prov[:, :, 2] = 254
        canvas_prov[25:25+sharp.shape[0], 25:25+sharp.shape[1]] = sharp
        cv2.rectangle(canvas_prov, (24, 24), (canvas_prov.shape[1]-24, canvas_prov.shape[0]-24), (210, 218, 225), 1, cv2.LINE_AA)

        out_png = os.path.join(img_dir, f'{slug}.png')
        out_webp = os.path.join(img_dir, f'{slug}.webp')
        cv2.imwrite(out_png, canvas_prov)
        Image.fromarray(cv2.cvtColor(canvas_prov, cv2.COLOR_BGR2RGB)).save(out_webp, 'WEBP', quality=92)
        print(f"Saved enhanced {slug}:", out_png, out_webp)

    print("\n=== Step 3: Generating Executive-Grade '立体知识产权护城河' Infographic Diagram ===")
    diag_w, diag_h = 1000, 1150
    diag_img = Image.new('RGB', (diag_w, diag_h), color='#0a1628')
    draw = ImageDraw.Draw(diag_img)

    # Ambient radial gradient effect in background
    for r in range(400, 0, -10):
        alpha = int(25 * (1 - r / 400))
        # Orange glow top right
        draw.ellipse([800 - r, 120 - r, 800 + r, 120 + r], fill=(244, 123, 32, alpha))
        # Blue glow bottom left
        draw.ellipse([200 - r, 950 - r, 200 + r, 950 + r], fill=(29, 78, 216, alpha))

    font_title = ImageFont.truetype(font_bold, 36)
    font_subtitle = ImageFont.truetype(font_reg, 16)
    font_node_title = ImageFont.truetype(font_bold, 20)
    font_node_desc = ImageFont.truetype(font_reg, 14)
    font_badge = ImageFont.truetype(font_bold, 12)
    font_arrow = ImageFont.truetype(font_reg, 12)

    # Header section
    draw.text((diag_w // 2, 45), "木齐科技 · 立体知识产权护城河", fill="#ffffff", font=font_title, anchor="mt")
    draw.text((diag_w // 2, 95), "MULTITIER INTELLECTUAL PROPERTY FORTRESS · 从硬核制造到商业溢价的全链路闭环", fill="#94a3b8", font=font_subtitle, anchor="mt")

    nodes = [
        {
            "tag": "物理制造硬核 · 发明专利",
            "tag_bg": "#1e3a5f",
            "tag_color": "#60a5fa",
            "title": "发明专利与高温微晶烧结工艺",
            "desc": "掌控纳米级微晶孔隙配方与高温相变核心制造技术，构筑底层物理防线",
            "border": "#2563eb",
            "bg": "#0f233d"
        },
        {
            "tag": "行业公认标杆 · 权威度量衡",
            "tag_bg": "#14532d",
            "tag_color": "#4ade80",
            "title": "SAC/TC621 委员单位与国家标准体系",
            "desc": "主导及参与制定抗菌与功能陶瓷国家标准，协同 200+ 项公用计量测试基准",
            "border": "#059669",
            "bg": "#062b1f"
        },
        {
            "tag": "商业视觉防伪 · 省级美术版权",
            "tag_bg": "#431407",
            "tag_color": "#fb923c",
            "title": "鲁作登字 · ICR 与固态氢实验室美术作品版权",
            "desc": "获山东省版权局核发，锁定商业流通官方认证印章与包装授权符号，严防山寨仿冒",
            "border": "#f47b20",
            "bg": "#2d1607"
        },
        {
            "tag": "国家级顶格直审 · 原理文字版权",
            "tag_bg": "#581c87",
            "tag_color": "#c084fc",
            "title": "国作登字 · ICR 智控释溶技术文字作品版权",
            "desc": "国家版权局直属中国版权保护中心 (CPCC) 直审，锁死机理推导、动力学算法与测试规程",
            "border": "#9333ea",
            "bg": "#290c4a"
        },
        {
            "tag": "商业终端落地 · 品牌溢价赋能",
            "tag_bg": "#7c2d12",
            "tag_color": "#fed7aa",
            "title": "赋予下游品牌：合规出海 ＋ 大厂秒过 ＋ 商业溢价",
            "desc": "海尔/美的等家电巨头法务免审 ｜ 伯尔尼公约 181 国出海护航 ｜ 支撑中高端终端溢价",
            "border": "#ea580c",
            "bg": "#371206"
        }
    ]

    card_w = 780
    card_h = 110
    start_y = 150
    spacing = 175

    for idx, node in enumerate(nodes):
        y = start_y + idx * spacing
        x = (diag_w - card_w) // 2

        # Card shadow
        draw.rounded_rectangle([x + 3, y + 4, x + card_w + 3, y + card_h + 4], radius=14, fill="#040912")
        # Card background
        draw.rounded_rectangle([x, y, x + card_w, y + card_h], radius=14, fill=node["bg"], outline=node["border"], width=2)

        # Tag pill
        tag_w = draw.textlength(node["tag"], font=font_badge) + 20
        draw.rounded_rectangle([x + 24, y + 16, x + 24 + tag_w, y + 38], radius=6, fill=node["tag_bg"])
        draw.text((x + 34, y + 21), node["tag"], fill=node["tag_color"], font=font_badge)

        # Title
        draw.text((x + 24, y + 48), node["title"], fill="#ffffff", font=font_node_title)

        # Description
        draw.text((x + 24, y + 78), node["desc"], fill="#cbd5e1", font=font_node_desc)

        # Downward connector arrow
        if idx < len(nodes) - 1:
            arrow_y1 = y + card_h + 8
            arrow_y2 = arrow_y1 + 45
            arrow_x = diag_w // 2
            # Draw dashed vertical line or solid line with arrow
            draw.line([arrow_x, arrow_y1, arrow_x, arrow_y2], fill="#f47b20", width=2)
            # Arrow head
            draw.polygon([
                (arrow_x, arrow_y2 + 8),
                (arrow_x - 6, arrow_y2 - 2),
                (arrow_x + 6, arrow_y2 - 2)
            ], fill="#f47b20")

    out_diag_png = os.path.join(img_dir, 'moat-architecture-flowchart.png')
    out_diag_webp = os.path.join(img_dir, 'moat-architecture-flowchart.webp')
    diag_img.save(out_diag_png, 'PNG', optimize=True)
    diag_img.save(out_diag_webp, 'WEBP', quality=95)
    print("Saved infographic moat flowchart:", out_diag_png, out_diag_webp)

    print("\n=== Step 4: Generating Ultra-Premium 1200x630 Executive Hero Banner ===")
    hero_w, hero_h = 1200, 630
    hero_img = Image.new('RGB', (hero_w, hero_h), color='#070e1a')
    hdraw = ImageDraw.Draw(hero_img)

    # Ambient radial lighting
    for r in range(500, 0, -15):
        alpha = int(22 * (1 - r / 500))
        hdraw.ellipse([1000 - r, 200 - r, 1000 + r, 200 + r], fill=(244, 123, 32, alpha))
        hdraw.ellipse([250 - r, 450 - r, 250 + r, 450 + r], fill=(29, 78, 216, alpha))

    # Grid background lines for tech feel
    for gx in range(0, hero_w, 60):
        hdraw.line([gx, 0, gx, hero_h], fill=(255, 255, 255, 6), width=1)
    for gy in range(0, hero_h, 60):
        hdraw.line([0, gy, hero_w, gy], fill=(255, 255, 255, 6), width=1)

    # Load the rectified national cert and provincial certs for compositing
    # National Cert thumbnail
    nat_pil = Image.open(out_nat_webp).convert('RGBA')
    # Resize national cert to fit left-center hero
    nat_thumb_w = 460
    nat_thumb_h = int(nat_pil.height * (nat_thumb_w / nat_pil.width))
    nat_thumb = nat_pil.resize((nat_thumb_w, nat_thumb_h), Image.Resampling.LANCZOS)

    # Add drop shadow behind national cert
    shadow_pad = 20
    shadow = Image.new('RGBA', (nat_thumb_w + shadow_pad*2, nat_thumb_h + shadow_pad*2), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    sdraw.rounded_rectangle([shadow_pad, shadow_pad, shadow_pad + nat_thumb_w, shadow_pad + nat_thumb_h], radius=10, fill=(0, 0, 0, 180))
    shadow = shadow.filter(ImageFilter.GaussianBlur(12))

    # Provincial Certs thumbnails
    prov1_pil = Image.open(os.path.join(img_dir, 'cert-solid-hydrogen-lab.webp')).convert('RGBA')
    prov2_pil = Image.open(os.path.join(img_dir, 'cert-icr-technology.webp')).convert('RGBA')
    prov_thumb_w = 270
    prov_thumb_h = int(prov1_pil.height * (prov_thumb_w / prov1_pil.width))
    prov1_thumb = prov1_pil.resize((prov_thumb_w, prov_thumb_h), Image.Resampling.LANCZOS)
    prov2_thumb = prov2_pil.resize((prov_thumb_w, prov_thumb_h), Image.Resampling.LANCZOS)

    # Composite images onto hero
    # Left side: National certificate (Hero centerpiece)
    pos_nat_x = 70
    pos_nat_y = 175
    hero_img.paste(shadow, (pos_nat_x - shadow_pad, pos_nat_y - shadow_pad), shadow)
    hero_img.paste(nat_thumb, (pos_nat_x, pos_nat_y), nat_thumb)

    # Right side: Two provincial certificates stacked or angled
    pos_p1_x = 560
    pos_p1_y = 175
    hero_img.paste(prov1_thumb, (pos_p1_x, pos_p1_y), prov1_thumb)

    pos_p2_x = 560
    pos_p2_y = 175 + prov_thumb_h + 15
    hero_img.paste(prov2_thumb, (pos_p2_x, pos_p2_y), prov2_thumb)

    # Floating Badges on the right
    badge_icr = Image.open(os.path.join(img_dir, 'badge-icr-technology.png')).convert('RGBA').resize((140, 140), Image.Resampling.LANCZOS)
    badge_lab = Image.open(os.path.join(img_dir, 'badge-solid-hydrogen-lab.png')).convert('RGBA').resize((140, 140), Image.Resampling.LANCZOS)
    
    hero_img.paste(badge_icr, (870, 200), badge_icr)
    hero_img.paste(badge_lab, (1020, 200), badge_lab)

    # Hero Typography
    font_hero_pill = ImageFont.truetype(font_bold, 13)
    font_hero_h1 = ImageFont.truetype(font_bold, 32)
    font_hero_sub = ImageFont.truetype(font_reg, 16)
    font_badge_caption = ImageFont.truetype(font_bold, 12)

    # Top pill
    pill_text = "国家版权局直审 · 国作登字-2026-A-00190677 ｜ 山东省版权局 · 鲁作登字-2026-F"
    pill_w = hdraw.textlength(pill_text, font=font_hero_pill) + 24
    hdraw.rounded_rectangle([70, 40, 70 + pill_w, 70], radius=15, fill="#1e293b", outline="#f47b20", width=1)
    hdraw.text((82, 47), pill_text, fill="#f47b20", font=font_hero_pill)

    # Main Title
    hdraw.text((70, 85), "木齐科技构建立体知识产权护城河", fill="#ffffff", font=font_hero_h1)
    # Subtitle
    hdraw.text((70, 130), "国家级文字专论版权 ＋ 省级商业美术徽标 ＋ SAC/TC621国家标准 赋能全球B2B大厂", fill="#94a3b8", font=font_hero_sub)

    # Captions below images
    hdraw.text((pos_nat_x + 10, pos_nat_y + nat_thumb_h + 12), "★ 国家版权局直属核发 · 《ICR智控释溶技术》文字作品证书", fill="#fcd34d", font=font_badge_caption)
    hdraw.text((pos_p1_x + 10, pos_p2_y + prov_thumb_h + 12), "★ 山东省版权局核发 · 《固态氢实验室》《ICR》美术作品证书", fill="#60a5fa", font=font_badge_caption)
    hdraw.text((870, 360), "商业流通防伪认证徽章", fill="#cbd5e1", font=font_badge_caption)
    hdraw.text((870, 385), "Equipped with ICR™ ｜ Solid Hydrogen Lab", fill="#94a3b8", font=font_badge_caption)

    # Bottom Trust Indicators Bar
    hdraw.line([70, 560, 1130, 560], fill=(255, 255, 255, 30), width=1)
    font_trust = ImageFont.truetype(font_reg, 13)
    trust_items = [
        "✔ 中国版权保护中心 (CPCC) 直审",
        "✔ 伯尔尼公约 181 成员国自动互认",
        "✔ SAC/TC621 委员单位与国家标准",
        "✔ 欧盟 RoHS · SGS 毒理 · FDA 食品接触"
    ]
    cur_x = 70
    for item in trust_items:
        hdraw.text((cur_x, 580), item, fill="#cbd5e1", font=font_trust)
        cur_x += 265

    out_hero_jpg = os.path.join(img_dir, 'hero-copyright-certificates.jpg')
    out_hero_webp = os.path.join(img_dir, 'hero-copyright-certificates.webp')
    hero_img.save(out_hero_jpg, 'JPEG', quality=95)
    hero_img.save(out_hero_webp, 'WEBP', quality=95)
    print("Saved executive hero banner:", out_hero_jpg, out_hero_webp)
    print("\nAll assets successfully generated!")

if __name__ == '__main__':
    build_all_assets()
