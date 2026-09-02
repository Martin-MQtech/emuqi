import os
import re

BASE_DIR = os.path.abspath('emuqi')

# Mapping rules for known broken links to correct targets
REPLACEMENTS = {
    # Non-existent or typo pages
    'hydrogen-healthhydrogen-water-filter-cartridge.html': 'hydrogen-health-hydrogen-water-filter-cartridge.html',
    'hydrogen-healthceramic-hydrogen-tablet.html': 'hydrogen-health-ceramic-hydrogen-tablet.html',
    'hydrogen-healthhydrogen-foot-bath-tablet.html': 'hydrogen-health-hydrogen-foot-bath-tablet.html',
    'hydrogen-healthhydrogen-alkaline-water-sachet.html': 'hydrogen-health-hydrogen-alkaline-water-sachet.html',
    '/hydrogen-healthhydrogen-water-filter-cartridge.html': '/hydrogen-health-hydrogen-water-filter-cartridge.html',
    '/hydrogen-healthceramic-hydrogen-tablet.html': '/hydrogen-health-ceramic-hydrogen-tablet.html',
    '/hydrogen-healthhydrogen-foot-bath-tablet.html': '/hydrogen-health-hydrogen-foot-bath-tablet.html',
    '/hydrogen-healthhydrogen-alkaline-water-sachet.html': '/hydrogen-health-hydrogen-alkaline-water-sachet.html',
    
    # Broken root/relative links
    '../page.html': '../product-functional-ceramic-materials.html',
    'page.html': 'product-functional-ceramic-materials.html',
    '/page.html': '/product-functional-ceramic-materials.html',
}

# 1. Create missing tag files in h2-wellness-hub if any
tag_dir = os.path.join(BASE_DIR, 'h2-wellness-hub', 'zh', 'tags')
os.makedirs(tag_dir, exist_ok=True)

tags = ['氢健康', '氢医学', '氢分子生物学', '富氢杯', '氢农业', '富氢水', '抗氧化']
for tag in tags:
    tag_file = os.path.join(tag_dir, f"{tag}.html")
    if not os.path.exists(tag_file):
        html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{tag} - 氢健康科普与研究专题 | 木齐科技</title>
<link rel="stylesheet" href="../../css/style.css">
<meta name="description" content="木齐科技氢健康知识库：{tag}专题研究与应用案例。">
</head>
<body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 40px auto; padding: 0 20px;">
  <header style="border-bottom: 1px solid #eee; padding-bottom: 20px; margin-bottom: 30px;">
    <a href="/h2-wellness-hub/zh/" style="color: #0284c7; text-decoration: none; font-weight: bold;">← 返回氢健康知识库首页</a>
    <h1 style="color: #0f172a; margin-top: 15px;">标签专题：#{tag}</h1>
  </header>
  <main>
    <p>正在汇聚【{tag}】相关的最新科学研究、学术文献及产业应用成果。请查阅以下相关主题文章：</p>
    <ul style="line-height: 2; margin-top: 20px;">
      <li><a href="/blog/antimicrobial-ceramic-balls-home-appliances-icr-technology.html" style="color: #0284c7;">一颗不起眼的陶瓷球，凭什么成了家电与净水大厂的“秘密武器”？ —— 抗菌陶瓷球全场景应用与ICR智控释溶技术深度解析</a></li>
      <li><a href="/blog/deepseek-ceramics.html" style="color: #0284c7;">DeepSeek眼中的功能陶瓷材料新浪潮</a></li>
      <li><a href="/hydrogen-generate-ceramic-ball.html" style="color: #0284c7;">固态制氢矿物陶瓷材料技术解密</a></li>
      <li><a href="/hydrogen-health-application.html" style="color: #0284c7;">氢健康多维生活场景解决方案</a></li>
    </ul>
  </main>
  <footer style="margin-top: 50px; padding-top: 20px; border-top: 1px solid #eee; color: #64748b; font-size: 13px;">
    &copy; 2026 山东木齐健康科技有限公司 · 全国抗菌表面标委会 SAC/TC621 委员单位
  </footer>
</body>
</html>"""
        with open(tag_file, 'w', encoding='utf-8') as tf:
            tf.write(html_content)
        print(f"Created missing tag page: {tag_file}")

# 2. Walk all HTML files and apply replacements
modified_count = 0
for root, dirs, files in os.walk(BASE_DIR):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file_obj:
                content = file_obj.read()
            
            orig_content = content
            for old_link, new_link in REPLACEMENTS.items():
                if old_link in content:
                    content = content.replace(old_link, new_link)
            
            # Check for broken relative links inside subfolders like blog/ or solutions/
            # If inside emuqi/blog/ and link is href="maca-kdf-antibacterial-ceramic-ball.html" without ../
            is_subfolder = os.path.relpath(root, BASE_DIR) != '.'
            if is_subfolder:
                # Fix direct root page references that missed ../
                for root_page in [
                    'index.html', 'about-functional-ceramic-ball-water-media-manufacturer.html',
                    'contact-mqtech-hydrogen-health.html', 'product-functional-ceramic-materials.html',
                    'maca-kdf-antibacterial-ceramic-ball.html', 'hydrogen-generate-ceramic-ball.html',
                    'hydrogen-health-application.html', 'store.html', 'solutions-hydrogen-agriculture.html'
                ]:
                    # replace href="root_page" with href="../root_page" if not preceded by ../ or / or http
                    pattern = r'href=["\'](' + re.escape(root_page) + r')["\']'
                    content = re.sub(pattern, r'href="../\1"', content)

            if content != orig_content:
                with open(filepath, 'w', encoding='utf-8') as file_obj:
                    file_obj.write(content)
                modified_count += 1

print(f"Repaired links across {modified_count} HTML files.")
