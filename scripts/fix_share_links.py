import os
import re

emuqi_dir = "/Users/martin/Documents/2026 BUSINESS MTRIX /20260721 MUQI 网站建设/emuqi"
modified_count = 0

for root, dirs, files in os.walk(emuqi_dir):
    for f in files:
        if not f.endswith(".html"):
            continue
        path = os.path.join(root, f)
        with open(path, "r", encoding="utf-8", errors="ignore") as fp:
            content = fp.read()
        
        # Replace non-canonical emuqi.com share urls with www.emuqi.com
        new_content = content
        if "https://twitter.com/intent/tweet?url=https://emuqi.com/" in new_content:
            new_content = new_content.replace(
                "https://twitter.com/intent/tweet?url=https://emuqi.com/",
                "https://twitter.com/intent/tweet?url=https://www.emuqi.com/"
            )
        if "https://www.facebook.com/sharer/sharer.php?u=https://emuqi.com/" in new_content:
            new_content = new_content.replace(
                "https://www.facebook.com/sharer/sharer.php?u=https://emuqi.com/",
                "https://www.facebook.com/sharer/sharer.php?u=https://www.emuqi.com/"
            )
        if "https://www.linkedin.com/sharing/share-offsite/?url=https://emuqi.com/" in new_content:
            new_content = new_content.replace(
                "https://www.linkedin.com/sharing/share-offsite/?url=https://emuqi.com/",
                "https://www.linkedin.com/sharing/share-offsite/?url=https://www.emuqi.com/"
            )
        if "https://reddit.com/submit?url=https://emuqi.com/" in new_content:
            new_content = new_content.replace(
                "https://reddit.com/submit?url=https://emuqi.com/",
                "https://reddit.com/submit?url=https://www.emuqi.com/"
            )
            
        if new_content != content:
            with open(path, "w", encoding="utf-8") as fp:
                fp.write(new_content)
            modified_count += 1

print(f"Standardized share links in {modified_count} HTML files.")
