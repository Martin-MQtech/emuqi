import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
article_path = os.path.join(base_dir, 'distribution_packages', '04_DEV_to', 'devto_clean_engineering.md')

with open(article_path, 'r', encoding='utf-8') as f:
    body = f.read()

payload = {
    "article": {
        "body_markdown": body
    }
}

out_path = os.path.join(base_dir, 'distribution_packages', '04_DEV_to', 'payload.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(payload, f, ensure_ascii=False)

print("Generated payload.json successfully:", os.path.getsize(out_path), "bytes")
