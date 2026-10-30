import asyncio
import json
import urllib.request
import websockets

CDP_URL = "http://127.0.0.1:9222/json"

def test_tabs():
    raw = urllib.request.urlopen(CDP_URL, timeout=5).read().decode("utf-8")
    tabs = json.loads(raw)
    for t in tabs:
        url = t.get("url", "")
        for kw in ["arena.ai", "z.ai"]:
            if kw in url and "preview-" not in url:
                print(f"Matched {kw}: {t.get('title')} -> {url} -> {t.get('webSocketDebuggerUrl')}")

if __name__ == "__main__":
    test_tabs()
