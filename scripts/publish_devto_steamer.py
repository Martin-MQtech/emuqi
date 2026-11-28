import json
import os
import sys
import urllib.error
import urllib.request


def main():
    api_key = os.environ.get("DEVTO_API_KEY", "").strip()
    if not api_key:
        print("DEVTO_API_KEY is required. Set it in the environment or CI secrets.")
        return 2

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    article_path = os.path.join(
        base_dir,
        "distribution_packages",
        "04_DEV_to",
        "devto_clean_engineering.md",
    )

    with open(article_path, "r", encoding="utf-8") as handle:
        body = handle.read()

    payload = {"article": {"body_markdown": body}}
    request = urllib.request.Request(
        "https://dev.to/api/articles",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "api-key": api_key,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))
        print("SUCCESS!")
        print("ID:", result.get("id"))
        print("Title:", result.get("title"))
        print("URL:", result.get("url"))
        print("Canonical:", result.get("canonical_url"))
        return 0
    except urllib.error.HTTPError as exc:
        print("HTTPError:", exc.code, exc.read().decode("utf-8", errors="replace"))
        return 1
    except Exception as exc:
        print("Error:", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
