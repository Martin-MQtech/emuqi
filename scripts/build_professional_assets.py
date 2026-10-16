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

    print("\n=== Step 4: Generating Ultra-Premium 1200x630 Executive Hero Banners (CN & EN) ===")
    def make_circular_badge(pil_img, diameter=96):
        min_dim = min(pil_img.size)
        cx, cy = pil_img.width // 2, pil_img.height // 2
        r = min_dim // 2
        cropped = pil_img.crop((cx - r, cy - r, cx + r, cy + r))
        scale = 4
        mask = Image.new('L', (r * 2 * scale, r * 2 * scale), 0)
        mdraw = ImageDraw.Draw(mask)
        mdraw.ellipse([0, 0, r * 2 * scale - 1, r * 2 * scale - 1], fill=255)
        mask = mask.resize((r * 2, r * 2), Image.Resampling.LANCZOS)
        result = Image.new('RGBA', (r * 2, r * 2), (0, 0, 0, 0))
        result.paste(cropped, (0, 0), mask=mask)
        resized = result.resize((diameter, diameter), Image.Resampling.LANCZOS)
        b_draw = ImageDraw.Draw(resized)
        b_draw.ellipse([0, 0, diameter-1, diameter-1], outline=(244, 123, 32, 220), width=2)
        b_draw.ellipse([2, 2, diameter-3, diameter-3], outline=(255, 255, 255, 120), width=1)
        return resized

    def create_banner(is_en=False):
        w, h = 1200, 630
        banner = Image.new('RGBA', (w, h), (8, 17, 30, 255))
        draw = ImageDraw.Draw(banner)

        # Smooth luxury studio background glow (NO distracting grids)
        for r in range(680, 0, -8):
            factor = 1.0 - (r / 680.0)
            cr = int(8 + (22 - 8) * factor)
            cg = int(17 + (38 - 17) * factor)
            cb = int(30 + (68 - 30) * factor)
            draw.ellipse([600 - r, 270 - int(r*0.65), 600 + r, 270 + int(r*0.65)], fill=(cr, cg, cb, 255))

        # Center golden pedestal glow
        aura = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        adraw = ImageDraw.Draw(aura)
        for r in range(320, 0, -10):
            alpha = int(22 * (1.0 - r / 320.0))
            adraw.ellipse([600 - r, 345 - int(r*0.6), 600 + r, 345 + int(r*0.6)], fill=(244, 123, 32, alpha))
        banner = Image.alpha_composite(banner, aura)

        def paste_with_shadow(canvas, element, pos, blur_r=18, offset=(0, 10), shadow_opacity=150, border_color=None):
            ew, eh = element.size
            pad = blur_r * 2 + max(abs(offset[0]), abs(offset[1]))
            sh_img = Image.new('RGBA', (ew + pad*2, eh + pad*2), (0, 0, 0, 0))
            sdraw = ImageDraw.Draw(sh_img)
            s_box = [pad + offset[0], pad + offset[1], pad + offset[0] + ew, pad + offset[1] + eh]
            sdraw.rectangle(s_box, fill=(0, 0, 0, shadow_opacity))
            sh_img = sh_img.filter(ImageFilter.GaussianBlur(blur_r))
            canvas.paste(sh_img, (pos[0] - pad, pos[1] - pad), sh_img)
            if border_color:
                elem_border = element.copy()
                bdraw = ImageDraw.Draw(elem_border)
                bdraw.rectangle([0, 0, ew-1, eh-1], outline=border_color, width=1)
                canvas.paste(elem_border, pos, elem_border)
            else:
                canvas.paste(element, pos, element)

        nat_raw = Image.open(out_nat_png).convert('RGBA')
        prov1_raw = Image.open(os.path.join(img_dir, 'cert-solid-hydrogen-lab.png')).convert('RGBA')
        prov2_raw = Image.open(os.path.join(img_dir, 'cert-icr-technology.png')).convert('RGBA')
        badge_icr_raw = Image.open(os.path.join(img_dir, 'badge-icr-technology.png')).convert('RGBA')
        badge_lab_raw = Image.open(os.path.join(img_dir, 'badge-solid-hydrogen-lab.png')).convert('RGBA')

        badge_icr = make_circular_badge(badge_icr_raw, diameter=96)
        badge_lab = make_circular_badge(badge_lab_raw, diameter=96)

        nat_w = 480
        nat_h = int(nat_raw.height * (nat_w / nat_raw.width))
        nat_elem = nat_raw.resize((nat_w, nat_h), Image.Resampling.LANCZOS)

        prov_w = 345
        prov1_h = int(prov1_raw.height * (prov_w / prov1_raw.width))
        prov2_h = int(prov2_raw.height * (prov_w / prov2_raw.width))
        prov1_elem = prov1_raw.resize((prov_w, prov1_h), Image.Resampling.LANCZOS)
        prov2_elem = prov2_raw.resize((prov_w, prov2_h), Image.Resampling.LANCZOS)

        cx = (w - nat_w) // 2
        cy = 168
        lx = 50
        ly = 208
        rx = w - 50 - prov_w
        ry = 208

        # Paste Left & Right Provincial Certs
        paste_with_shadow(banner, prov1_elem, (lx, ly), blur_r=16, offset=(0, 8), shadow_opacity=130, border_color=(200, 215, 230, 180))
        paste_with_shadow(banner, prov2_elem, (rx, ry), blur_r=16, offset=(0, 8), shadow_opacity=130, border_color=(200, 215, 230, 180))

        # Paste Center National Cert (Elevated in front with prominent golden border & rich shadow)
        paste_with_shadow(banner, nat_elem, (cx, cy), blur_r=24, offset=(0, 12), shadow_opacity=190, border_color=(244, 123, 32, 220))

        # Paste Circular Badges in front at corners
        paste_with_shadow(banner, badge_icr, (cx - 48, cy + nat_h - 78), blur_r=12, offset=(0, 6), shadow_opacity=160)
        paste_with_shadow(banner, badge_lab, (cx + nat_w - 48, cy + nat_h - 78), blur_r=12, offset=(0, 6), shadow_opacity=160)

        f_pill = ImageFont.truetype(font_bold, 13)
        f_title = ImageFont.truetype(font_bold, 34)
        f_sub = ImageFont.truetype(font_reg, 15)
        f_lbl_gold = ImageFont.truetype(font_bold, 13)
        f_lbl_sub = ImageFont.truetype(font_bold, 12)

        draw = ImageDraw.Draw(banner)

        if not is_en:
            pill_str = '★ 中国版权保护中心 (CPCC) 直审 · 国家级文字作品版权 ｜ 山东省版权局 · 美术作品确权'
            title_str = '木齐科技 · 权威知识产权矩阵'
            sub_str = '国家级技术专论版权 ＋ 省级商业美术版权 ｜ 构筑全球B2B供应链信任壁垒'
            lbl_left = '省级美术确权 · 固态氢实验室'
            lbl_center = '★ 国家版权局直审 · 国作登字-2026-A-00190677 · 《ICR智控释溶技术》文字专论'
            lbl_right = '省级美术确权 · ICR智控释溶'
        else:
            pill_str = '★ Reviewed by CPCC · Stamped by National Copyright Administration of PRC'
            title_str = 'MUQI TECH · MULTITIER INTELLECTUAL PROPERTY FORTRESS'
            sub_str = 'National-Level Literary Work Copyright + Certified Commercial Artworks | Securing Global Tier-1 OEMs'
            lbl_left = 'Certified Artwork · Solid Hydrogen Lab'
            lbl_center = '★ National Copyright · Reg. 国作登字-2026-A-00190677 · ICR™ Literary Work'
            lbl_right = 'Certified Artwork · ICR Release Tech'

        # Pill Tag
        pw = draw.textlength(pill_str, font=f_pill) + 26
        px = (w - pw) // 2
        draw.rounded_rectangle([px, 22, px + pw, 50], radius=14, fill=(24, 38, 62, 220), outline=(244, 123, 32, 200), width=1)
        draw.text((px + 13, 28), pill_str, fill='#fed7aa', font=f_pill)

        # Title
        draw.text((w // 2, 63), title_str, fill='#ffffff', font=f_title, anchor='mt')

        # Subtitle
        draw.text((w // 2, 110), sub_str, fill='#cbd5e1', font=f_sub, anchor='mt')

        # Top labels directly above Left and Right Certificates
        vis_l_w = cx - 10 - lx
        tag_l_w = draw.textlength(lbl_left, font=f_lbl_sub) + 18
        tag_l_x = lx + (vis_l_w - tag_l_w) // 2
        draw.rounded_rectangle([tag_l_x, ly - 32, tag_l_x + tag_l_w, ly - 8], radius=5, fill=(18, 30, 50, 220), outline=(100, 130, 170, 120), width=1)
        draw.text((tag_l_x + 9, ly - 27), lbl_left, fill='#93c5fd', font=f_lbl_sub)

        vis_r_start = cx + nat_w + 10
        vis_r_w = (rx + prov_w) - vis_r_start
        tag_r_w = draw.textlength(lbl_right, font=f_lbl_sub) + 18
        tag_r_x = vis_r_start + (vis_r_w - tag_r_w) // 2
        draw.rounded_rectangle([tag_r_x, ly - 32, tag_r_x + tag_r_w, ly - 8], radius=5, fill=(18, 30, 50, 220), outline=(100, 130, 170, 120), width=1)
        draw.text((tag_r_x + 9, ly - 27), lbl_right, fill='#93c5fd', font=f_lbl_sub)

        # Center caption with gold pill backing below National Cert at Y = 550
        c_w = draw.textlength(lbl_center, font=f_lbl_gold) + 26
        c_x = (w - c_w) // 2
        c_y = cy + nat_h + 16
        draw.rounded_rectangle([c_x, c_y, c_x + c_w, c_y + 30], radius=6, fill=(30, 42, 65, 230), outline=(244, 123, 32, 190), width=1)
        draw.text((w // 2, c_y + 6), lbl_center, fill='#fcd34d', font=f_lbl_gold, anchor='mt')

        final_rgb = banner.convert('RGB')
        name_prefix = 'hero-copyright-certificates-en' if is_en else 'hero-copyright-certificates'
        out_jpg = os.path.join(img_dir, f'{name_prefix}.jpg')
        out_webp = os.path.join(img_dir, f'{name_prefix}.webp')
        final_rgb.save(out_jpg, 'JPEG', quality=95)
        final_rgb.save(out_webp, 'WEBP', quality=95)
        print(f"Saved executive hero banner ({name_prefix}):", out_jpg, out_webp)

    create_banner(is_en=False)
    create_banner(is_en=True)
    print("\nAll assets successfully generated!")

if __name__ == '__main__':
    build_all_assets()
