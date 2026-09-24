import urllib.request
import urllib.error
import json
import os

api_key = 'AQRPoPn4D81VWwBBkeR9CBPi'
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
article_path = os.path.join(base_dir, 'distribution_packages', '04_DEV_to', 'devto_clean_engineering.md')

with open(article_path, 'r', encoding='utf-8') as f:
    body = f.read()

payload = {
    'article': {
        'body_markdown': body
    }
}

req = urllib.request.Request(
    'https://dev.to/api/articles',
    data=json.dumps(payload).encode('utf-8'),
    headers={
        'api-key': api_key,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
    },
    method='POST'
)

try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print('SUCCESS!')
        print('ID:', res.get('id'))
        print('Title:', res.get('title'))
        print('URL:', res.get('url'))
        print('Canonical:', res.get('canonical_url'))
except urllib.error.HTTPError as e:
    print('HTTPError:', e.code, e.read().decode('utf-8'))
except Exception as e:
    print('Error:', e)
