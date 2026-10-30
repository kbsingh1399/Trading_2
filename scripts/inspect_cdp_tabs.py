import urllib.request
import json

try:
    tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json', timeout=5).read().decode('utf-8'))
    print(f"Total tabs found on CDP: {len(tabs)}")
    coinglass_tabs = []
    for i, t in enumerate(tabs):
        url = t.get('url', '')
        title = t.get('title', '')
        tab_type = t.get('type', '')
        tab_id = t.get('id', '')
        print(f"[{i:02d}] Type: {tab_type} | ID: {tab_id} | Title: {title[:40]} | URL: {url[:80]}")
        if 'coinglass' in url.lower():
            coinglass_tabs.append(t)
            
    print(f"\n--- COINGLASS TABS COUNT: {len(coinglass_tabs)} ---")
    for cg in coinglass_tabs:
        print(f"  ID: {cg.get('id')} | Title: {cg.get('title')} | URL: {cg.get('url')}")
except Exception as e:
    print("CDP error:", e)
