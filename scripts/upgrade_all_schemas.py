import os
import re
import json
import glob

BASE_DIR = "/Users/martin/Documents/2026 BUSINESS MTRIX /20260721 MUQI 网站建设/emuqi"

ORG_SCHEMA = {
    "@type": "Organization",
    "@id": "https://emuqi.com/#organization",
    "name": "Shandong MUQI Health Technology Co., Ltd.",
    "alternateName": ["MUQI Tech", "木齐科技", "山东木齐健康科技有限公司", "MUQI Technology"],
    "url": "https://emuqi.com",
    "logo": {
        "@type": "ImageObject",
        "url": "https://emuqi.com/assets/images/logo.jpg"
    },
    "description": "Leading global manufacturer of functional mineral ceramic water media, solid-state hydrogen materials, MACA-KDF antibacterial ceramics, and eco-friendly water treatment solutions.",
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
    "@id": "https://emuqi.com/#author-martin",
    "name": "Martin Chen",
    "alternateName": ["Martin"],
    "jobTitle": "Founder & CEO",
    "worksFor": {"@id": "https://emuqi.com/#organization"},
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
    "@id": "https://emuqi.com/#website",
    "url": "https://emuqi.com",
    "name": "MUQI Tech | Functional Ceramic Water Media & Solid-State Hydrogen",
    "publisher": {"@id": "https://emuqi.com/#organization"}
}

def inject_or_replace_schema(html_content, schema_dict, meta_keywords=None, meta_description=None):
    # Format JSON-LD nicely
    json_ld_str = json.dumps(schema_dict, ensure_ascii=False, indent=2)
    script_tag = f'<script type="application/ld+json">\n{json_ld_str}\n</script>'
    
    # 1. Replace existing JSON-LD script if present in <head>
    if '<script type="application/ld+json">' in html_content:
        html_content = re.sub(r'<script type="application/ld\+json">.*?</script>', script_tag, html_content, flags=re.DOTALL)
    else:
        # Inject before </head>
        html_content = html_content.replace('</head>', f'{script_tag}\n</head>')

    # 2. Update keywords if provided
    if meta_keywords:
        if '<meta name="keywords"' in html_content:
            html_content = re.sub(r'<meta name="keywords" content=".*?">', f'<meta name="keywords" content="{meta_keywords}">', html_content)
        else:
            html_content = html_content.replace('<head>', f'<head>\n<meta name="keywords" content="{meta_keywords}">')
            
    # 3. Update description if provided
    if meta_description:
        if '<meta name="description"' in html_content:
            html_content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{meta_description}">', html_content)
            
    return html_content

print("Script template ready.")
