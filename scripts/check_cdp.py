import urllib.request
import json

try:
    with urllib.request.urlopen("http://localhost:9222/json") as resp:
        tabs = json.loads(resp.read().decode())
    for t in tabs:
        if t.get("type") == "page":
            print(f"{t.get('title')} | {t.get('url')} | {t.get('id')}")
except Exception as e:
    print("CDP Error:", e)
