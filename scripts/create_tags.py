import os

tags = [
    ("氢健康.html", "氢健康", "Hydrogen Health"),
    ("氢医学.html", "氢医学", "Hydrogen Medicine"),
    ("氢分子生物学.html", "氢分子生物学", "Hydrogen Molecular Biology"),
    ("富氢杯.html", "富氢杯", "Hydrogen Water Bottle")
]

tag_dir = 'emuqi/h2-wellness-hub/zh/tags'
os.makedirs(tag_dir, exist_ok=True)

template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name_cn} - 氢健康知识与案例库 | 木齐科技 H2 Wellness Hub</title>
    <meta name="description" content="木齐科技 H2 Wellness Hub 汇集关于 {name_cn} ({name_en}) 的全球前沿研究、临床案例与创新产品解决方案。">
    <meta name="keywords" content="{name_cn}, {name_en}, 氢健康, 木齐科技, 富氢水, 固态氢">
    <link rel="canonical" href="https://www.emuqi.com/h2-wellness-hub/zh/tags/{filename}">
    <link rel="stylesheet" href="/assets/css/style.css">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@graph": [
        {{
          "@type": "CollectionPage",
          "@id": "https://www.emuqi.com/h2-wellness-hub/zh/tags/{filename}#webpage",
          "name": "{name_cn} - 氢健康知识与案例库",
          "isPartOf": {{ "@id": "https://www.emuqi.com/#website" }},
          "breadcrumb": {{
            "@type": "BreadcrumbList",
            "itemListElement": [
              {{ "@type": "ListItem", "position": 1, "name": "首页", "item": "https://www.emuqi.com/" }},
              {{ "@type": "ListItem", "position": 2, "name": "H2 Wellness Hub", "item": "https://www.emuqi.com/h2-wellness-hub/" }},
              {{ "@type": "ListItem", "position": 3, "name": "{name_cn}", "item": "https://www.emuqi.com/h2-wellness-hub/zh/tags/{filename}" }}
            ]
          }}
        }}
      ]
    }}
    </script>
</head>
<body class="bg-gray-50 text-gray-800 font-sans antialiased">
    <header class="bg-white border-b border-gray-200 sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <a href="/" class="flex items-center space-x-3">
                <span class="text-xl font-bold text-blue-600">MUQI TECH</span>
                <span class="text-xs text-gray-500 border-l pl-3 border-gray-300">H2 Wellness Hub</span>
            </a>
            <nav class="flex items-center space-x-6 text-sm">
                <a href="/h2-wellness-hub/" class="text-gray-600 hover:text-blue-600">Hub 首页</a>
                <a href="/blog/index.html" class="text-gray-600 hover:text-blue-600">技术博客</a>
                <a href="/product-functional-ceramic-materials.html" class="text-gray-600 hover:text-blue-600">核心产品</a>
                <a href="/contact-sales.html" class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition">联系我们</a>
            </nav>
        </div>
    </header>

    <main class="max-w-4xl mx-auto px-4 sm:px-6 py-12">
        <nav class="text-sm text-gray-500 mb-6">
            <a href="/" class="hover:text-blue-600">首页</a> / 
            <a href="/h2-wellness-hub/" class="hover:text-blue-600">H2 Wellness Hub</a> / 
            <span class="text-gray-900 font-medium">标签: {name_cn}</span>
        </nav>

        <header class="mb-10">
            <div class="inline-flex items-center gap-2 px-3 py-1 bg-blue-50 text-blue-700 rounded-full text-xs font-semibold uppercase tracking-wider mb-3">Tag Topic</div>
            <h1 class="text-3xl font-extrabold text-gray-900">{name_cn} ({name_en}) 专题聚合</h1>
            <p class="mt-3 text-gray-600">探索关于 {name_cn} 的前沿学术研究、全球商业案例、创新固态氢材料与健康应用技术。</p>
        </header>

        <section class="space-y-6">
            <article class="bg-white p-6 rounded-xl border border-gray-200 hover:shadow-md transition">
                <div class="text-xs text-blue-600 font-semibold mb-2">案例研究 · CASE STUDY</div>
                <h2 class="text-xl font-bold text-gray-900 hover:text-blue-600"><a href="/h2-wellness-hub/zh/cases/revive-hydrogen-generator-us.html">ReVive 美国富氢水杯商业化与品牌增长案例</a></h2>
                <p class="text-gray-600 text-sm mt-2">探讨固态氢陶瓷材料在北美便携式富氢水杯市场的应用实践与消费者认知。</p>
            </article>

            <article class="bg-white p-6 rounded-xl border border-gray-200 hover:shadow-md transition">
                <div class="text-xs text-blue-600 font-semibold mb-2">临床研究 · CLINICAL STUDY</div>
                <h2 class="text-xl font-bold text-gray-900 hover:text-blue-600"><a href="/h2-wellness-hub/zh/cases/keio-exercise-hydrogen-study.html">日本庆应义塾大学：富氢水在运动恢复与抗疲劳中的临床研究</a></h2>
                <p class="text-gray-600 text-sm mt-2">系统分析氢分子选择性抗氧化与清除自由基对运动机能改善的科学数据。</p>
            </article>

            <article class="bg-white p-6 rounded-xl border border-gray-200 hover:shadow-md transition">
                <div class="text-xs text-blue-600 font-semibold mb-2">行业标准 · INDUSTRY STANDARD</div>
                <h2 class="text-xl font-bold text-gray-900 hover:text-blue-600"><a href="/h2-wellness-hub/zh/cases/ahha-industry-standards.html">国际氢健康产业标准与技术规范深度解读</a></h2>
                <p class="text-gray-600 text-sm mt-2">全国抗菌表面标准化技术委员会 (SAC/TC621) 与全球氢产业规范对比分析。</p>
            </article>
        </section>
    </main>

    <footer class="bg-gray-900 text-gray-400 py-8 mt-16 text-center text-xs">
        <p>&copy; 2026 山东木齐健康科技有限公司 MUQI Tech. All rights reserved.</p>
    </footer>
</body>
</html>
"""

for fname, n_cn, n_en in tags:
    fpath = os.path.join(tag_dir, fname)
    with open(fpath, 'w', encoding='utf-8') as fp:
        fp.write(template.format(filename=fname, name_cn=n_cn, name_en=n_en))
    print(f"Created tag page: {fpath}")
