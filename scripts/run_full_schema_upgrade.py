import os, re, json, glob

BASE_DIR = "/Users/martin/Documents/2026 BUSINESS MTRIX /20260721 MUQI 网站建设/emuqi"

# 1. Global Entities
ORG_SCHEMA = {
    "@type": "Organization",
    "@id": "https://www.emuqi.com/#organization",
    "name": "Shandong MUQI Health Technology Co., Ltd.",
    "alternateName": ["MUQI Tech", "木齐科技", "山东木齐健康科技有限公司", "MUQI Technology"],
    "url": "https://www.emuqi.com",
    "logo": {
        "@type": "ImageObject",
        "url": "https://www.emuqi.com/assets/images/logo.jpg"
    },
    "description": "Global leading manufacturer of functional mineral ceramic water media, solid-state hydrogen materials, MACA-KDF antibacterial ceramics, and eco-friendly water treatment solutions.",
    "contactPoint": {
        "@type": "ContactPoint",
        "telephone": "+86-13964416725",
        "contactType": "sales",
        "email": "muqizb@gmail.com",
        "areaServed": "Global",
        "availableLanguage": ["en", "zh"]
    },
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Block B, Innovation Park, 125 Liuquan Road",
        "addressLocality": "Zibo",
        "addressRegion": "Shandong",
        "addressCountry": "CN"
    },
    "memberOf": {
        "@type": "Organization",
        "name": "National Standardization Technical Committee on Antimicrobial Surface Performance (SAC/TC621) / 全国抗菌表面性能标准化技术委员会 (SAC/TC621)"
    },
    "sameAs": [
        "https://www.linkedin.com/company/72043164",
        "https://x.com/MARTINPARK111",
        "https://www.youtube.com/@Martinchen1234"
    ]
}

PERSON_SCHEMA = {
    "@type": "Person",
    "@id": "https://www.emuqi.com/#author-martin",
    "name": "Martin Chen",
    "alternateName": ["陈滨", "Martin"],
    "jobTitle": "Founder & CEO",
    "worksFor": {"@id": "https://www.emuqi.com/#organization"},
    "hasCredential": [
        {
            "@type": "EducationalOccupationalCredential",
            "credentialCategory": "First Standing Committee Member",
            "recognizedBy": {
                "@type": "Organization",
                "name": "National Standardization Technical Committee on Antimicrobial Surface Performance (SAC/TC621) / 全国抗菌表面性能标准化技术委员会 (SAC/TC621)"
            }
        }
    ]
}

WEBSITE_SCHEMA = {
    "@type": "WebSite",
    "@id": "https://www.emuqi.com/#website",
    "url": "https://www.emuqi.com",
    "name": "MUQI Tech | Functional Ceramic Water Media & Solid-State Hydrogen",
    "publisher": {"@id": "https://www.emuqi.com/#organization"}
}

def inject_or_replace_schema(html_content, schema_graph, meta_keywords=None, meta_description=None):
    schema_dict = {
        "@context": "https://schema.org",
        "@graph": schema_graph
    }
    json_ld_str = json.dumps(schema_dict, ensure_ascii=False, indent=2)
    script_tag = f'<script type="application/ld+json">\n{json_ld_str}\n</script>'
    
    # 1. Replace existing JSON-LD script if present in <head>
    if '<script type="application/ld+json">' in html_content:
        html_content = re.sub(r'<script type="application/ld\+json">.*?</script>', script_tag, html_content, flags=re.DOTALL)
    else:
        html_content = html_content.replace('</head>', f'{script_tag}\n</head>')

    # 2. Update keywords if provided
    if meta_keywords:
        if '<meta name="keywords"' in html_content:
            html_content = re.sub(r'<meta name="keywords" content=".*?">', f'<meta name="keywords" content="{meta_keywords}">', html_content)
        elif '<head>' in html_content:
            html_content = html_content.replace('<head>', f'<head>\n<meta name="keywords" content="{meta_keywords}">')
            
    # 3. Update description if provided
    if meta_description:
        if '<meta name="description"' in html_content:
            html_content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{meta_description}">', html_content)
            
    return html_content

# --- Process specific page categories ---
updated_count = 0

# 1. Homepage index.html
fp = os.path.join(BASE_DIR, "index.html")
if os.path.exists(fp):
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()
    graph = [
        ORG_SCHEMA,
        PERSON_SCHEMA,
        WEBSITE_SCHEMA,
        {
            "@type": "WebPage",
            "@id": "https://www.emuqi.com/#webpage",
            "url": "https://www.emuqi.com/",
            "name": "MUQI Tech — Functional Ceramic Water Media & Solid-State Hydrogen Manufacturer",
            "description": "Leading manufacturer of functional mineral ceramic water media, MACA-KDF antibacterial ceramics, and solid-state hydrogen materials for health, water treatment, and smart appliances.",
            "isPartOf": {"@id": "https://www.emuqi.com/#website"},
            "about": {"@id": "https://www.emuqi.com/#organization"}
        }
    ]
    c = inject_or_replace_schema(c, graph, "Functional Ceramic Water Media, Solid-State Hydrogen, MACA-KDF, Antimicrobial Ceramic Balls, Water Treatment, SAC/TC621, MUQI Tech, 木齐科技, 无机抗菌陶瓷球, 固态富氢材料")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(c)
    updated_count += 1
    print("Updated index.html")

# 2. About Us
fp = os.path.join(BASE_DIR, "about-functional-ceramic-ball-water-media-manufacturer.html")
if os.path.exists(fp):
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()
    graph = [
        ORG_SCHEMA,
        PERSON_SCHEMA,
        {
            "@type": "AboutPage",
            "@id": "https://www.emuqi.com/about-functional-ceramic-ball-water-media-manufacturer.html#webpage",
            "url": "https://www.emuqi.com/about-functional-ceramic-ball-water-media-manufacturer.html",
            "name": "About MUQI — Leading Functional Ceramic Water Media Manufacturer",
            "description": "Learn about MUQI Technology, our 20-year history, factory capacity, ISO9001/SGS certifications, SAC/TC621 committee membership, and global leadership in functional ceramic balls.",
            "isPartOf": {"@id": "https://www.emuqi.com/#website"},
            "mainEntity": {"@id": "https://www.emuqi.com/#organization"}
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.emuqi.com/"},
                {"@type": "ListItem", "position": 2, "name": "About Us", "item": "https://www.emuqi.com/about-functional-ceramic-ball-water-media-manufacturer.html"}
            ]
        }
    ]
    c = inject_or_replace_schema(c, graph, "About MUQI, Functional Ceramic Manufacturer, SAC/TC621, Martin Chen, Ceramic Water Media Factory, ISO9001, 木齐科技公司介绍")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(c)
    updated_count += 1
    print("Updated about page")

# 3. Contact Us
fp = os.path.join(BASE_DIR, "contact-mqtech-hydrogen-health.html")
if os.path.exists(fp):
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()
    graph = [
        ORG_SCHEMA,
        {
            "@type": "ContactPage",
            "@id": "https://www.emuqi.com/contact-mqtech-hydrogen-health.html#webpage",
            "url": "https://www.emuqi.com/contact-mqtech-hydrogen-health.html",
            "name": "Contact MUQI Technology | OEM & Wholesale Inquiries",
            "description": "Get in touch with MUQI Technology for functional ceramic water media, hydrogen materials, OEM/ODM inquiries, and free product samples.",
            "isPartOf": {"@id": "https://www.emuqi.com/#website"}
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.emuqi.com/"},
                {"@type": "ListItem", "position": 2, "name": "Contact", "item": "https://www.emuqi.com/contact-mqtech-hydrogen-health.html"}
            ]
        }
    ]
    c = inject_or_replace_schema(c, graph)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(c)
    updated_count += 1
    print("Updated contact page")

# 4. Product Overview: product-functional-ceramic-materials.html
fp = os.path.join(BASE_DIR, "product-functional-ceramic-materials.html")
if os.path.exists(fp):
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()
    graph = [
        ORG_SCHEMA,
        PERSON_SCHEMA,
        {
            "@type": "CollectionPage",
            "@id": "https://www.emuqi.com/product-functional-ceramic-materials.html#collection",
            "url": "https://www.emuqi.com/product-functional-ceramic-materials.html",
            "name": "Functional Ceramic Materials & Water Media Products | MUQI",
            "description": "Explore MUQI complete lineup of functional ceramic materials: hydrogen-generating ceramic balls, MACA-KDF antibacterial media, MPH+ neutralizer, and dechlorination media.",
            "isPartOf": {"@id": "https://www.emuqi.com/#website"},
            "mainEntity": {
                "@type": "ItemList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Hydrogen Generate Ceramic Ball", "url": "https://www.emuqi.com/hydrogen-generate-ceramic-ball.html"},
                    {"@type": "ListItem", "position": 2, "name": "MACA-KDF Antibacterial Ceramic Ball", "url": "https://www.emuqi.com/maca-kdf-antibacterial-ceramic-ball.html"},
                    {"@type": "ListItem", "position": 3, "name": "MPH+ Condensate Neutralizer", "url": "https://www.emuqi.com/mph-condensate-neutralizer.html"}
                ]
            }
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.emuqi.com/"},
                {"@type": "ListItem", "position": 2, "name": "Products", "item": "https://www.emuqi.com/product-functional-ceramic-materials.html"}
            ]
        }
    ]
    c = inject_or_replace_schema(c, graph, "Functional Ceramic Materials, Water Media, Hydrogen Generating Balls, MACA-KDF, MPH Neutralizer, Calcium Sulfite Dechlorination, 无机功能陶瓷材料, 木齐科技产品")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(c)
    updated_count += 1
    print("Updated product catalog page")

# 5. Core Product 1: maca-kdf-antibacterial-ceramic-ball.html
fp = os.path.join(BASE_DIR, "maca-kdf-antibacterial-ceramic-ball.html")
if os.path.exists(fp):
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()
    graph = [
        ORG_SCHEMA,
        PERSON_SCHEMA,
        {
            "@type": "Product",
            "@id": "https://www.emuqi.com/maca-kdf-antibacterial-ceramic-ball.html#product",
            "name": "MACA-KDF Antibacterial Microporous Ceramic Ball (MACA-KDF 无机抗菌合金陶瓷球)",
            "image": "https://www.emuqi.com/assets/images/ceramic-ball-main.png",
            "description": "High-temperature sintered microporous ceramic alloy with ICR controlled silver ion release. Inhibits >99.9% bacteria for 12-24 months in robot vacuum water tanks, humidifiers, and water filters.",
            "brand": {"@id": "https://www.emuqi.com/#organization"},
            "manufacturer": {"@id": "https://www.emuqi.com/#organization"},
            "category": "Water Filter Media > Antibacterial Ceramics",
            "material": "Inorganic Microporous Ceramic with Lattice-Bonded Nano-Silver",
            "additionalProperty": [
                {"@type": "PropertyValue", "name": "Antibacterial Rate", "value": ">99.9% against E. coli & S. aureus"},
                {"@type": "PropertyValue", "name": "Technology", "value": "ICR (Intelligent Controlled Release)"},
                {"@type": "PropertyValue", "name": "Lifespan", "value": "12-24 Months"},
                {"@type": "PropertyValue", "name": "Certifications", "value": "SAC/TC621, RoHS, REACH, Drinking Water Hygiene License"}
            ]
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.emuqi.com/"},
                {"@type": "ListItem", "position": 2, "name": "Products", "item": "https://www.emuqi.com/product-functional-ceramic-materials.html"},
                {"@type": "ListItem", "position": 3, "name": "MACA-KDF Antibacterial Ceramic Ball", "item": "https://www.emuqi.com/maca-kdf-antibacterial-ceramic-ball.html"}
            ]
        }
    ]
    c = inject_or_replace_schema(c, graph, "MACA-KDF, Antibacterial Ceramic Ball, Inorganic Antimicrobial Media, ICR Controlled Release, Robot Vacuum Tank Anti-Odor, Humidifier Filter, SAC/TC621, 无机抗菌陶瓷球, 扫地机器人防臭")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(c)
    updated_count += 1
    print("Updated MACA-KDF page")

# 6. Core Product 2: hydrogen-generate-ceramic-ball.html
fp = os.path.join(BASE_DIR, "hydrogen-generate-ceramic-ball.html")
if os.path.exists(fp):
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()
    graph = [
        ORG_SCHEMA,
        PERSON_SCHEMA,
        {
            "@type": "Product",
            "@id": "https://www.emuqi.com/hydrogen-generate-ceramic-ball.html#product",
            "name": "Solid-State Hydrogen Generating Ceramic Ball (固态富氢陶瓷球 / 单质硅产氢材料)",
            "image": "https://www.emuqi.com/assets/images/ceramic-ball-hero.png",
            "description": "Elemental silicon micro-nano composite ceramic media that generates high-concentration dissolved hydrogen (>1500 ppb) and negative ORP (-800 mV) spontaneously upon contact with water without electricity.",
            "brand": {"@id": "https://www.emuqi.com/#organization"},
            "manufacturer": {"@id": "https://www.emuqi.com/#organization"},
            "category": "Water Filter Media > Hydrogen Generation",
            "material": "Elemental Silicon Micro-Nano Functional Ceramic",
            "additionalProperty": [
                {"@type": "PropertyValue", "name": "Hydrogen Concentration", "value": "1200 - 1600 ppb"},
                {"@type": "PropertyValue", "name": "ORP Potential", "value": "-400 to -800 mV"},
                {"@type": "PropertyValue", "name": "pH Level", "value": "8.5 - 9.5 (Mild Alkaline)"}
            ]
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.emuqi.com/"},
                {"@type": "ListItem", "position": 2, "name": "Products", "item": "https://www.emuqi.com/product-functional-ceramic-materials.html"},
                {"@type": "ListItem", "position": 3, "name": "Hydrogen Generate Ceramic Ball", "item": "https://www.emuqi.com/hydrogen-generate-ceramic-ball.html"}
            ]
        }
    ]
    c = inject_or_replace_schema(c, graph, "Hydrogen Generate Ceramic Ball, Solid-State Hydrogen, Elemental Silicon Hydrogen, Negative ORP Water, Alkaline Water Media, 富氢陶瓷球, 无电制氢材料, 氢健康材料")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(c)
    updated_count += 1
    print("Updated Hydrogen ball page")

# 7. Core Product 3: mph-condensate-neutralizer.html
fp = os.path.join(BASE_DIR, "mph-condensate-neutralizer.html")
if os.path.exists(fp):
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()
    graph = [
        ORG_SCHEMA,
        {
            "@type": "Product",
            "@id": "https://www.emuqi.com/mph-condensate-neutralizer.html#product",
            "name": "MPH+ Acidic Condensate Neutralizer Ceramic Media (MPH+ 冷凝水酸碱中和滤料)",
            "image": "https://www.emuqi.com/assets/images/ceramic-ball-product1.jpg",
            "description": "Engineered alkaline mineral ceramic media designed to neutralize acidic condensate water from condensing boilers, HVAC systems, and industrial water heaters (pH 3 to pH 7+).",
            "brand": {"@id": "https://www.emuqi.com/#organization"},
            "manufacturer": {"@id": "https://www.emuqi.com/#organization"},
            "category": "HVAC & Boiler Media > Condensate Neutralizer"
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.emuqi.com/"},
                {"@type": "ListItem", "position": 2, "name": "Products", "item": "https://www.emuqi.com/product-functional-ceramic-materials.html"},
                {"@type": "ListItem", "position": 3, "name": "MPH+ Condensate Neutralizer", "item": "https://www.emuqi.com/mph-condensate-neutralizer.html"}
            ]
        }
    ]
    c = inject_or_replace_schema(c, graph, "MPH+ Neutralizer, Condensate Neutralizer, Acidic Condensate Treatment, Condensing Boiler Filter Media, HVAC Water Treatment, 冷凝水中和颗粒")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(c)
    updated_count += 1
    print("Updated MPH page")

# 8. Store / Product Catalog: store.html
fp = os.path.join(BASE_DIR, "store.html")
if os.path.exists(fp):
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()
    graph = [
        ORG_SCHEMA,
        {
            "@type": "CollectionPage",
            "@id": "https://www.emuqi.com/store.html#collection",
            "url": "https://www.emuqi.com/store.html",
            "name": "MUQI Store — Wholesale Functional Ceramic Media & Hydrogen Products",
            "description": "Browse and request samples for MUQI wholesale functional ceramic balls, hydrogen tablets, alkaline filter sachets, and custom OEM water solutions.",
            "isPartOf": {"@id": "https://www.emuqi.com/#website"}
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.emuqi.com/"},
                {"@type": "ListItem", "position": 2, "name": "Store", "item": "https://www.emuqi.com/store.html"}
            ]
        }
    ]
    c = inject_or_replace_schema(c, graph)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(c)
    updated_count += 1
    print("Updated store page")

# 9. Application Solutions Root & Subpages
app_pages = [
    ("hydrogen-health-application.html", "Hydrogen Health Applications & Smart Water Solutions", "Explore comprehensive applications of MUQI functional ceramic media in hydrogen water bottles, sachets, filter cartridges, beauty devices, and foot bath tablets.", "Applications"),
    ("hydrogen-water-bottle-or-hydrogen-health.html", "Portable Hydrogen Water Bottle OEM & Media Solution", "Turn any water into 1500ppb antioxidant hydrogen water on-the-go with MUQI solid-state hydrogen ceramic cores.", "Hydrogen Water Bottle"),
    ("hydrogen-health-hydrogen-alkaline-water-sachet.html", "Hydrogen Alkaline Mineral Water Sachet", "Portable food-grade water alkalizing and antioxidant hydrogen tea-bag style sachet for daily hydration.", "Alkaline Water Sachet"),
    ("hydrogen-healthceramic-hydrogen-tablet.html", "Effervescent Ceramic Hydrogen Tablet Media", "Fast-dissolving solid-state hydrogen generating ceramic tablets for high-potency antioxidant water.", "Hydrogen Tablet"),
    ("hydrogen-healthhydrogen-water-filter-cartridge.html", "Hydrogen & Antibacterial Water Filter Cartridges", "Commercial and residential inline filter cartridges incorporating MACA antibacterial and hydrogen ceramic balls.", "Water Filter Cartridge"),
    ("hydrogen-healthhydrogen-foot-bath-tablet.html", "Hydrogen Foot Bath & Spa Tablets", "High-efficiency transdermal antioxidant hydrogen foot bath and wellness spa tablets for recovery and circulation.", "Foot Bath Tablet")
]

for fname, title, desc, bname in app_pages:
    fp = os.path.join(BASE_DIR, fname)
    if os.path.exists(fp):
        with open(fp, "r", encoding="utf-8") as f:
            c = f.read()
        graph = [
            ORG_SCHEMA,
            PERSON_SCHEMA,
            {
                "@type": "Service",
                "@id": f"https://www.emuqi.com/{fname}#service",
                "name": title,
                "description": desc,
                "provider": {"@id": "https://www.emuqi.com/#organization"},
                "areaServed": "Global"
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.emuqi.com/"},
                    {"@type": "ListItem", "position": 2, "name": "Applications", "item": "https://www.emuqi.com/hydrogen-health-application.html"},
                    {"@type": "ListItem", "position": 3, "name": bname, "item": f"https://www.emuqi.com/{fname}"}
                ]
            }
        ]
        c = inject_or_replace_schema(c, graph, f"Hydrogen health application, {bname}, Water filtration OEM, MUQI technology, 氢健康应用, {bname}")
        with open(fp, "w", encoding="utf-8") as f:
            f.write(c)
        updated_count += 1
        print(f"Updated application page: {fname}")

# 10. Solutions Hydrogen Agriculture Root & Subpages
agri_pages = [
    ("solutions-hydrogen-agriculture.html", "Hydrogen Agriculture Solutions & Crop Resilience", "Agricultural applications of hydrogen-rich water for crop yield improvement, disease resistance, livestock health, and eco-friendly farming.", "Hydrogen Agriculture"),
    ("solutions-hydrogen-agriculture/aquaculture-hydrogen-research.html", "Hydrogen in Aquaculture Research & Applications", "Using dissolved hydrogen water to enhance aquatic survival rates, reduce bacterial infections, and boost dissolved oxygen utilization.", "Aquaculture Hydrogen"),
    ("solutions-hydrogen-agriculture/crop-resilience.html", "Hydrogen-Rich Water for Crop Resilience & Soil Health", "Improving seed germination, drought tolerance, and nutrient absorption with molecular hydrogen irrigation.", "Crop Resilience"),
    ("solutions-hydrogen-agriculture/livestock-hydrogen-research.html", "Hydrogen Water in Livestock & Poultry Health", "Reducing antibiotic dependence and oxidative stress in livestock with hydrogen-enriched drinking water.", "Livestock Research"),
    ("solutions-hydrogen-agriculture/companion-animal-health-care.html", "Companion Animal & Pet Hydrogen Wellness", "Pet health applications of molecular hydrogen water for canine and feline anti-inflammatory and cellular care.", "Pet Wellness"),
    ("solutions-hydrogen-agriculture/industry-summit-kunshan-2026.html", "2026 Hydrogen Agriculture Industry Summit Report", "Insights from the National Hydrogen Agriculture Innovation Forum and MUQI solid-state hydrogen tech.", "Kunshan Summit")
]

for fname, title, desc, bname in agri_pages:
    fp = os.path.join(BASE_DIR, fname)
    if os.path.exists(fp):
        with open(fp, "r", encoding="utf-8") as f:
            c = f.read()
        graph = [
            ORG_SCHEMA,
            PERSON_SCHEMA,
            {
                "@type": "TechArticle",
                "@id": f"https://www.emuqi.com/{fname}#article",
                "headline": title,
                "description": desc,
                "author": {"@id": "https://www.emuqi.com/#author-martin"},
                "publisher": {"@id": "https://www.emuqi.com/#organization"}
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.emuqi.com/"},
                    {"@type": "ListItem", "position": 2, "name": "Hydrogen Agriculture", "item": "https://www.emuqi.com/solutions-hydrogen-agriculture.html"},
                    {"@type": "ListItem", "position": 3, "name": bname, "item": f"https://www.emuqi.com/{fname}"}
                ]
            }
        ]
        c = inject_or_replace_schema(c, graph, f"Hydrogen Agriculture, {bname}, Molecular hydrogen farming, Green agriculture, 氢农业, 富氢水灌溉")
        with open(fp, "w", encoding="utf-8") as f:
            f.write(c)
        updated_count += 1
        print(f"Updated agriculture page: {fname}")

# 11. Blog Listing & all 19 Blog Posts
# Blog list page
fp_blog_list = os.path.join(BASE_DIR, "blog-list-hydrogen-health.html")
if os.path.exists(fp_blog_list):
    with open(fp_blog_list, "r", encoding="utf-8") as f:
        c = f.read()
    graph = [
        ORG_SCHEMA,
        PERSON_SCHEMA,
        {
            "@type": "Blog",
            "@id": "https://www.emuqi.com/blog-list-hydrogen-health.html#blog",
            "name": "MUQI Tech Blog — Hydrogen Health & Functional Materials Insights",
            "url": "https://www.emuqi.com/blog-list-hydrogen-health.html",
            "description": "Technical insights, material science breakthroughs, ICR controlled release, and molecular hydrogen research from MUQI Technology.",
            "publisher": {"@id": "https://www.emuqi.com/#organization"}
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.emuqi.com/"},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://www.emuqi.com/blog-list-hydrogen-health.html"}
            ]
        }
    ]
    c = inject_or_replace_schema(c, graph)
    with open(fp_blog_list, "w", encoding="utf-8") as f:
        f.write(c)
    updated_count += 1
    print("Updated blog list page")

# All blog posts in emuqi/blog/*.html
blog_files = glob.glob(os.path.join(BASE_DIR, "blog", "*.html"))
for bfile in blog_files:
    fname = os.path.basename(bfile)
    if fname == "index.html":
        with open(bfile, "r", encoding="utf-8") as f:
            c = f.read()
        graph = [
            ORG_SCHEMA,
            PERSON_SCHEMA,
            {
                "@type": "Blog",
                "@id": "https://www.emuqi.com/blog/#blog",
                "name": "MUQI Technology Blog",
                "url": "https://www.emuqi.com/blog/",
                "publisher": {"@id": "https://www.emuqi.com/#organization"}
            }
        ]
        c = inject_or_replace_schema(c, graph)
        with open(bfile, "w", encoding="utf-8") as f:
            f.write(c)
        updated_count += 1
        continue

    # Read post HTML
    with open(bfile, "r", encoding="utf-8") as f:
        c = f.read()

    # Skip antimicrobial-ceramic-balls (already fully customized)
    if "antimicrobial-ceramic-balls-home-appliances-icr-technology" in fname:
        continue

    # Extract Title
    title_match = re.search(r'<title>(.*?)</title>', c, re.IGNORECASE)
    title = title_match.group(1) if title_match else "MUQI Hydrogen Technology & Materials Insight"
    
    # Extract Description
    desc_match = re.search(r'<meta\s+name="description"\s+content="(.*?)"', c, re.IGNORECASE)
    desc = desc_match.group(1) if desc_match else "Technical insights from MUQI Technology on functional ceramics and hydrogen health."

    # Build standard TechArticle Graph
    graph = [
        ORG_SCHEMA,
        PERSON_SCHEMA,
        {
            "@type": "TechArticle",
            "@id": f"https://www.emuqi.com/blog/{fname}#article",
            "headline": title.split(" | ")[0],
            "description": desc,
            "isPartOf": {"@id": "https://www.emuqi.com/#website"},
            "author": {"@id": "https://www.emuqi.com/#author-martin"},
            "publisher": {"@id": "https://www.emuqi.com/#organization"},
            "inLanguage": "en"
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.emuqi.com/"},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://www.emuqi.com/blog-list-hydrogen-health.html"},
                {"@type": "ListItem", "position": 3, "name": title.split(" | ")[0], "item": f"https://www.emuqi.com/blog/{fname}"}
            ]
        }
    ]
    c = inject_or_replace_schema(c, graph, f"Hydrogen Health, Functional Ceramic Media, Molecular Hydrogen, MUQI Technology, SAC/TC621, Martin Chen, {title.split(' | ')[0]}")
    with open(bfile, "w", encoding="utf-8") as f:
        f.write(c)
    updated_count += 1
    print(f"Updated blog post: {fname}")

print(f"Successfully upgraded {updated_count} pages with Schema.org & GEO/SEO keywords!")
