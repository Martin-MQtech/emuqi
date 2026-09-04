import os
import xml.etree.ElementTree as ET

sitemap_path = "/Users/martin/Documents/2026 BUSINESS MTRIX /20260721 MUQI 网站建设/emuqi/sitemap.xml"

# Read sitemap.xml and remove entries for hub.html, h2-health-hub/index.html, h2-health-hub/zh/index.html
with open(sitemap_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

urls_to_remove = [
    "https://www.emuqi.com/hub.html",
    "https://www.emuqi.com/h2-health-hub/index.html",
    "https://www.emuqi.com/h2-health-hub/zh/index.html",
    "https://www.emuqi.com/h2-health-hub/",
    "https://www.emuqi.com/h2-health-hub/zh/"
]

new_lines = []
skip = False
for line in lines:
    if "<url>" in line:
        url_block = [line]
        skip = False
    elif "</url>" in line:
        url_block.append(line)
        block_str = "".join(url_block)
        if any(u in block_str for u in urls_to_remove):
            # Do not add to new_lines
            pass
        else:
            new_lines.extend(url_block)
        url_block = []
    elif 'url_block' in locals() and url_block:
        url_block.append(line)
    else:
        new_lines.append(line)

with open(sitemap_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Updated sitemap.xml to purge removed pages.")
