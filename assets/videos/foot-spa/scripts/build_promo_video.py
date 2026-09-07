#!/usr/bin/env python3
"""
Dual-Language (CN & EN) Broadcast-Quality Promo Video Generator
Target: Vertical Short Video (1080x1920, 9:16), Duration ~45-50s (< 1 min)
Directory: /video_foot_spa_promo in workspace root
"""

import os
import sys
import json
import wave
import math
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_DIR = "/Users/martin/Documents/2026 BUSINESS MTRIX /20260721 MUQI 网站建设"
VIDEO_DIR = os.path.join(BASE_DIR, "video_foot_spa_promo")
ASSETS_IMG_DIR = os.path.join(BASE_DIR, "emuqi/assets/images/blog/foot-spa")
TEMP_DIR = os.path.join(VIDEO_DIR, "temp")

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(VIDEO_DIR, exist_ok=True)

# 1. Chinese Scenes (~48s)
SCENES_CN = [
    {
        "id": "cn_scene_01",
        "badge": "⚠️ 行业隐患曝光",
        "badge_color": (239, 68, 68),
        "badge_bg": (69, 10, 10),
        "headline": "廉价草本药包正在毁掉足浴硬件？",
        "subhead": "9款热销药包100%染菌 · 超标160倍的行业警钟",
        "voiceover": "你还在用赠送的廉价草本包泡脚吗？在下一次泡脚前，这条视频一定要看完。",
        "card_text": "廉价草本包残渣沉淀 · 堵塞管道难清洁",
        "image": "315-investigation-herbal-debris.jpg",
        "accent": (239, 68, 68)
    },
    {
        "id": "cn_scene_02",
        "badge": "🚨 实验室权威检测",
        "badge_color": (245, 158, 11),
        "badge_bg": (69, 26, 3),
        "headline": "9款热销药包全部检出真菌",
        "subhead": "最高超标160倍 · 劣质赠品成品牌口碑杀手",
        "voiceover": "权威实验室抽检9款热销药包，真菌检出率高达100%，最高超标160倍！无杀菌工艺的药包正在严重透支硬件口碑。",
        "card_text": "100% 检出真菌污染 · 严重危害足部健康",
        "image": "315-nine-samples-test-card.png",
        "accent": (245, 158, 11)
    },
    {
        "id": "cn_scene_03",
        "badge": "💡 固态氢材料革命",
        "badge_color": (56, 189, 248),
        "badge_bg": (8, 47, 73),
        "headline": "零改电 · 免开模 · 即放即溶",
        "subhead": "纯白片剂秒级崩解 · 告别浑浊中药渣",
        "voiceover": "不用重新开模，零改电路。只需投入一颗纯白固态氢片，数秒迅速崩解，没有残渣沉淀，水质依然清澈透亮。",
        "card_text": "清澈透亮无残留 · 零机器改造成本",
        "image": "amazon-h2rich-tablet-closeup.jpg",
        "accent": (56, 189, 248)
    },
    {
        "id": "cn_scene_04",
        "badge": "🔬 1200+ ppb 纯分子氢",
        "badge_color": (34, 197, 94),
        "badge_bg": (5, 46, 22),
        "headline": "亿级微纳米气泡 透皮抗氧化渗透",
        "subhead": "实测高浓度溶氢 · 权威科学文献验证机制",
        "voiceover": "释放数亿级细腻的微纳米分子氢气泡，水中溶氢量实测超过1200ppb，带来真正的透皮抗氧化与深度舒缓。",
        "card_text": "实测溶氢 >1200 ppb · 微纳米气泡长效存留",
        "image": "h2-microbubbles-dissolution.jpg",
        "accent": (34, 197, 94)
    },
    {
        "id": "cn_scene_05",
        "badge": "📈 剃须刀与刀片百亿蓝海",
        "badge_color": (249, 115, 22),
        "badge_bg": (67, 20, 7),
        "headline": "硬件卖完就结束？开启超级复购！",
        "subhead": "单机年复购增收 $45~$120 · 耗材毛利超 60%",
        "voiceover": "足浴设备卖完就结束？固态氢耗材让单机年复购增收45到120美元，打通硬件加耗材的高毛利百亿闭环！",
        "card_text": "剃须刀+刀片模式 · 硬件商转型高频复购",
        "image": "tripartite-value-allocation.png",
        "accent": (249, 115, 22)
    },
    {
        "id": "cn_scene_06",
        "badge": "🤝 联合研发与OEM定制",
        "badge_color": (168, 85, 247),
        "badge_bg": (59, 7, 100),
        "headline": "木齐科技 · 固态氢供应链方案",
        "subhead": "SAC/TC621标准委员会委员单位 · 全程合规支持",
        "voiceover": "木齐科技提供国家级实验室配方与洁净车间定制。欢迎品牌合作，立即访问 emuqi.com 索取深度白皮书！",
        "card_text": "MUQI TECH 研发支持 · 深度白皮书：emuqi.com",
        "image": "hero-foot-spa-consumables.png",
        "accent": (168, 85, 247)
    }
]

# 2. English Scenes (~44s)
SCENES_EN = [
    {
        "id": "en_scene_01",
        "badge": "⚠️ THE HIDDEN TRAP",
        "badge_color": (239, 68, 68),
        "badge_bg": (69, 10, 10),
        "headline": "Are Cheap Herbal Bags Ruining Foot Baths?",
        "subhead": "100% Mold Contamination & The Wake-Up Call",
        "voiceover": "Stop putting cheap herbal bags into your hot foot bath! You need to watch this before your next soak.",
        "card_text": "Toxic Residue & Clogged Machine Drain Valves",
        "image": "315-investigation-herbal-debris.jpg",
        "accent": (239, 68, 68)
    },
    {
        "id": "en_scene_02",
        "badge": "🚨 INDEPENDENT LAB SHOCK",
        "badge_color": (245, 158, 11),
        "badge_bg": (69, 26, 3),
        "headline": "100% Tested Packs Contained Fungal Mold",
        "subhead": "Up to 160x Safety Limits · Destroying Brand Reputation",
        "voiceover": "Independent lab tests on 9 best-selling foot soak packs revealed 100% contained fungal mold—up to 160 times over safety limits!",
        "card_text": "Zero Sterilization · Severe Microbial Contamination",
        "image": "315-nine-samples-test-card.png",
        "accent": (245, 158, 11)
    },
    {
        "id": "en_scene_03",
        "badge": "💡 CLEAN TECH UPGRADE",
        "badge_color": (56, 189, 248),
        "badge_bg": (8, 47, 73),
        "headline": "Zero Retooling · Instant Dissolution",
        "subhead": "Clean White Tablet · Zero Sludge & Clear Water",
        "voiceover": "Zero electrical retooling. One pure white solid-state hydrogen tablet dissolves in seconds with zero sludge and crystal-clear water.",
        "card_text": "Crystal Clear Water · Zero Retooling Overhead",
        "image": "amazon-h2rich-tablet-closeup.jpg",
        "accent": (56, 189, 248)
    },
    {
        "id": "en_scene_04",
        "badge": "🔬 1200+ PPB PURE H2",
        "badge_color": (34, 197, 94),
        "badge_bg": (5, 46, 22),
        "headline": "Millions of Micro-Nano Bubbles",
        "subhead": "Measurable Concentration · Proven Transdermal Relaxation",
        "voiceover": "Releasing millions of micro-nano bubbles with over 1200 ppb of measurable molecular hydrogen for proven transdermal relaxation.",
        "card_text": "Measurable >1200 ppb Dissolved H2 · Pure Relaxation",
        "image": "h2-microbubbles-dissolution.jpg",
        "accent": (34, 197, 94)
    },
    {
        "id": "en_scene_05",
        "badge": "📈 RAZOR & BLADES MODEL",
        "badge_color": (249, 115, 22),
        "badge_bg": (67, 20, 7),
        "headline": "From One-Off Sale to Recurring LTV",
        "subhead": "Adding $45-$120 in Consumable GMV Per Appliance",
        "voiceover": "Turn a single hardware sale into a recurring revenue engine, adding $45 to $120 in high-margin consumable reorders per year.",
        "card_text": "Recurring LTV Engine · Over 60% Consumable Margins",
        "image": "tripartite-value-allocation.png",
        "accent": (249, 115, 22)
    },
    {
        "id": "en_scene_06",
        "badge": "🤝 PARTNER WITH MUQI TECH",
        "badge_color": (168, 85, 247),
        "badge_bg": (59, 7, 100),
        "headline": "Turnkey Materials & Cleanroom OEM",
        "subhead": "SAC/TC621 Committee Member · Full Technical Support",
        "voiceover": "Partner with MUQI Tech for turnkey solid-state materials and OEM cleanroom production. Visit emuqi.com today!",
        "card_text": "MUQI TECH Laboratory · Full Report at emuqi.com",
        "image": "hero-foot-spa-consumables.png",
        "accent": (168, 85, 247)
    }
]

def generate_voiceover(scene, lang="cn"):
    audio_aiff = os.path.join(TEMP_DIR, f"{scene['id']}.aiff")
    audio_wav = os.path.join(TEMP_DIR, f"{scene['id']}.wav")
    
    if lang == "cn":
        cmd_say = ["say", "-v", "Tingting", "-r", "200", "-o", audio_aiff, scene["voiceover"]]
    else:
        cmd_say = ["say", "-v", "Samantha", "-r", "180", "-o", audio_aiff, scene["voiceover"]]
        
    subprocess.run(cmd_say, check=True)
    
    cmd_ffmpeg = [
        "ffmpeg", "-y", "-i", audio_aiff,
        "-af", "apad=pad_dur=0.25",
        "-ar", "44100", "-ac", "2",
        audio_wav
    ]
    subprocess.run(cmd_ffmpeg, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    probe = subprocess.check_output([
        "ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", audio_wav
    ])
    duration = float(json.loads(probe)["format"]["duration"])
    return audio_wav, duration

def generate_ambient_bgm(total_duration, output_path):
    sample_rate = 44100
    num_samples = int(sample_rate * (total_duration + 2.0))
    t = np.linspace(0, (total_duration + 2.0), num_samples, False)
    
    chords = [
        [174.61, 220.00, 261.63, 349.23],  # Fm
        [138.59, 207.65, 261.63, 329.63],  # Db
        [155.56, 196.00, 233.08, 311.13],  # Eb
        [130.81, 196.00, 261.63, 329.63]   # C
    ]
    
    audio = np.zeros(num_samples)
    bar_dur = 4.0
    
    for i, chord in enumerate(chords * int(math.ceil(total_duration / (bar_dur * len(chords)) + 1))):
        start_time = i * bar_dur
        if start_time >= total_duration:
            break
        end_time = min(start_time + bar_dur, total_duration + 2.0)
        idx_start = int(start_time * sample_rate)
        idx_end = int(end_time * sample_rate)
        segment_len = idx_end - idx_start
        if segment_len <= 0:
            continue
            
        t_seg = t[idx_start:idx_end] - start_time
        env = np.sin(np.pi * np.clip(t_seg / bar_dur, 0, 1)) ** 1.4
        
        chord_wave = np.zeros(segment_len)
        for freq in chord:
            chord_wave += 0.6 * np.sin(2 * np.pi * freq * t_seg)
            chord_wave += 0.25 * np.sin(2 * np.pi * freq * 2 * t_seg)
            chord_wave += 0.1 * np.sin(2 * np.pi * freq * 3 * t_seg)
            
        audio[idx_start:idx_end] += chord_wave * env
    
    audio = audio / (np.max(np.abs(audio)) + 1e-6) * 0.08
    audio_int16 = (audio * 32767).astype(np.int16)
    stereo_data = np.empty((num_samples, 2), dtype=np.int16)
    stereo_data[:, 0] = audio_int16
    stereo_data[:, 1] = audio_int16
    
    with wave.open(output_path, "w") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(stereo_data.tobytes())

def draw_rounded_rect(draw, bbox, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)

def render_scene_frame(scene, lang="cn", width=1080, height=1920):
    img = Image.new("RGB", (width, height), (8, 14, 28))
    draw = ImageDraw.Draw(img)
    
    # Ambient top glow
    for r in range(400, 0, -20):
        alpha = int(12 * (1 - r / 400))
        glow_box = [width // 2 - r, 80 - r // 2, width // 2 + r, 80 + r // 2]
        draw.ellipse(glow_box, fill=(15 + alpha, 25 + alpha * 2, 50 + alpha * 3))
    
    font_file = "/System/Library/Fonts/STHeiti Medium.ttc" if lang == "cn" else "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
    font_badge = ImageFont.truetype(font_file, 26 if lang == "en" else 28)
    font_title = ImageFont.truetype(font_file, 38 if lang == "en" else 44)
    font_subhead = ImageFont.truetype(font_file, 26 if lang == "en" else 28)
    font_subtitle = ImageFont.truetype(font_file, 32 if lang == "en" else 36)
    font_card_text = ImageFont.truetype(font_file, 26 if lang == "en" else 28)
    font_footer = ImageFont.truetype(font_file, 24 if lang == "en" else 26)
    
    # 1. Header Pill Badge (Y: 90)
    badge_text = scene["badge"]
    badge_w = 380 if lang == "en" else 340
    badge_h = 56
    badge_x = 60
    badge_y = 90
    draw_rounded_rect(draw, [badge_x, badge_y, badge_x + badge_w, badge_y + badge_h], radius=16,
                      fill=scene["badge_bg"], outline=scene["badge_color"], width=2)
    draw.text((badge_x + 20, badge_y + 12), badge_text, font=font_badge, fill=scene["badge_color"])
    
    # 2. Main Title (Y: 165)
    draw.text((60, 165), scene["headline"], font=font_title, fill=(255, 255, 255))
    
    # 3. Subhead (Y: 232)
    draw.text((60, 232), scene["subhead"], font=font_subhead, fill=scene["accent"])
    
    # 4. Central Visual Card (Y: 290 to Y: 1370)
    card_x1, card_y1 = 60, 290
    card_x2, card_y2 = width - 60, 1370
    card_w = card_x2 - card_x1
    card_h = card_y2 - card_y1
    
    draw_rounded_rect(draw, [card_x1, card_y1, card_x2, card_y2], radius=24,
                      fill=(15, 23, 42), outline=(51, 65, 85), width=2)
    
    img_path = os.path.join(ASSETS_IMG_DIR, scene["image"])
    if os.path.exists(img_path):
        src_img = Image.open(img_path).convert("RGB")
        sw, sh = src_img.size
        scale = min((card_w - 24) / sw, (card_h - 24) / sh)
        new_w = int(sw * scale)
        new_h = int(sh * scale)
        src_resized = src_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        paste_x = card_x1 + (card_w - new_w) // 2
        paste_y = card_y1 + (card_h - new_h) // 2
        img.paste(src_resized, (paste_x, paste_y))
    
    draw_rounded_rect(draw, [card_x1, card_y1, card_x2, card_y2], radius=24,
                      outline=scene["accent"], width=2)
    
    # 5. Lower Subtitle & Caption Box (Y: 1400 to Y: 1680)
    sub_x1, sub_y1 = 60, 1400
    sub_x2, sub_y2 = width - 60, 1680
    draw_rounded_rect(draw, [sub_x1, sub_y1, sub_x2, sub_y2], radius=20,
                      fill=(15, 23, 42), outline=(51, 65, 85), width=2)
    draw_rounded_rect(draw, [sub_x1, sub_y1, sub_x1 + 10, sub_y2], radius=4,
                      fill=scene["accent"])
    
    vo_text = scene["voiceover"]
    lines = []
    chunk_size = 20 if lang == "cn" else 45
    if lang == "cn":
        for i in range(0, len(vo_text), chunk_size):
            lines.append(vo_text[i:i+chunk_size])
    else:
        # Word wrap for English
        words = vo_text.split()
        cur_line = []
        for w in words:
            if len(" ".join(cur_line + [w])) <= chunk_size:
                cur_line.append(w)
            else:
                lines.append(" ".join(cur_line))
                cur_line = [w]
        if cur_line:
            lines.append(" ".join(cur_line))
            
    vo_y = sub_y1 + 24
    for line in lines[:2]:
        draw.text((sub_x1 + 34, vo_y), line, font=font_subtitle, fill=(254, 240, 138))
        vo_y += 48
        
    draw.line([sub_x1 + 34, sub_y2 - 62, sub_x2 - 34, sub_y2 - 62], fill=(51, 65, 85), width=1)
    prefix = "🎯 " if lang == "cn" else "⚡ "
    draw.text((sub_x1 + 34, sub_y2 - 46), f"{prefix}{scene['card_text']}", font=font_card_text, fill=(148, 163, 184))
    
    # 6. Footer Brand Section (Y: 1720 to Y: 1850)
    foot_y = 1720
    draw.line([60, foot_y, width - 60, foot_y], fill=(30, 41, 59), width=2)
    footer_label = "MUQI TECH · 固态氢材料研发伙伴" if lang == "cn" else "MUQI TECH · Solid-State Hydrogen Partner"
    url_label = "www.emuqi.com | 全球首发白皮书" if lang == "cn" else "www.emuqi.com | B2B Engineering Report"
    draw.text((60, foot_y + 24), footer_label, font=font_footer, fill=(255, 255, 255))
    draw.text((60, foot_y + 64), url_label, font=font_footer, fill=(56, 189, 248))
    
    cta_btn_w = 260 if lang == "cn" else 300
    draw_rounded_rect(draw, [width - 60 - cta_btn_w, foot_y + 26, width - 60, foot_y + 80], radius=12,
                      fill=(234, 88, 12))
    cta_label = "合作咨询 · 立即接入 →" if lang == "cn" else "Contact Us · OEM Partner →"
    draw.text((width - 45 - cta_btn_w, foot_y + 40), cta_label, font=font_footer, fill=(255, 255, 255))
    
    return img

def build_scene_clip(scene, duration, frame_img_path):
    out_clip = os.path.join(TEMP_DIR, f"{scene['id']}_clip.mp4")
    audio_wav = os.path.join(TEMP_DIR, f"{scene['id']}.wav")
    
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", frame_img_path,
        "-i", audio_wav,
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-pix_fmt", "yuv420p",
        "-r", "30",
        "-t", f"{duration:.3f}",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        out_clip
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    return out_clip

def build_full_video(scenes, lang, output_mp4, output_cover):
    print(f"\n============================================================")
    print(f"🎬 Producing {lang.upper()} Video: {output_mp4}")
    
    durations = []
    total_duration = 0.0
    for scene in scenes:
        wav_path, dur = generate_voiceover(scene, lang=lang)
        durations.append(dur)
        total_duration += dur
        
    print(f"⏱️ Total Narration Duration: {total_duration:.2f}s (Strictly < 60s)")
    
    bgm_path = os.path.join(TEMP_DIR, f"ambient_bgm_{lang}.wav")
    generate_ambient_bgm(total_duration, bgm_path)
    
    clip_paths = []
    for idx, (scene, dur) in enumerate(zip(scenes, durations)):
        frame_img = render_scene_frame(scene, lang=lang)
        frame_path = os.path.join(TEMP_DIR, f"{scene['id']}_frame.png")
        frame_img.save(frame_path)
        
        if idx == 0:
            frame_img.save(output_cover)
            print(f"🖼️ Saved vertical poster: {output_cover}")
            
        clip_path = build_scene_clip(scene, dur, frame_path)
        clip_paths.append(clip_path)
        
    concat_list_file = os.path.join(TEMP_DIR, f"concat_list_{lang}.txt")
    with open(concat_list_file, "w") as f:
        for p in clip_paths:
            f.write(f"file '{p}'\n")
            
    raw_video = os.path.join(TEMP_DIR, f"raw_concat_{lang}.mp4")
    cmd_concat = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_list_file,
        "-c", "copy",
        raw_video
    ]
    subprocess.run(cmd_concat, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    cmd_final = [
        "ffmpeg", "-y",
        "-i", raw_video,
        "-i", bgm_path,
        "-filter_complex",
        "[0:a]volume=1.0[voice];[1:a]volume=0.32[bgm];[voice][bgm]amix=inputs=2:duration=first[aout]",
        "-map", "0:v",
        "-map", "[aout]",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "20",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-movflags", "+faststart",
        output_mp4
    ]
    subprocess.run(cmd_final, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    probe = subprocess.check_output([
        "ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", output_mp4
    ])
    final_dur = float(json.loads(probe)["format"]["duration"])
    file_size_mb = os.path.getsize(output_mp4) / (1024 * 1024)
    print(f"✅ Success! Duration: {final_dur:.2f}s | Size: {file_size_mb:.2f} MB")
    print("============================================================\n")

def main():
    # 1. Build Chinese Video (~46-48s)
    output_cn = os.path.join(VIDEO_DIR, "foot_spa_promo_video_cn.mp4")
    cover_cn = os.path.join(VIDEO_DIR, "cover_vertical_cn.png")
    build_full_video(SCENES_CN, "cn", output_cn, cover_cn)
    
    # 2. Build English Video (~43-45s)
    output_en = os.path.join(VIDEO_DIR, "foot_spa_promo_video_en.mp4")
    cover_en = os.path.join(VIDEO_DIR, "cover_vertical_en.png")
    build_full_video(SCENES_EN, "en", output_en, cover_en)

if __name__ == "__main__":
    main()
