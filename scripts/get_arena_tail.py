import asyncio
import json
import urllib.request
import websockets

async def check():
    raw = urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=5).read().decode("utf-8")
    tabs = json.loads(raw)
    ws_url = None
    for t in tabs:
        if "arena" in t.get("url", "").lower():
            ws_url = t.get("webSocketDebuggerUrl")
            break
    if not ws_url:
        print("No Arena tab found")
        return
    async with websockets.connect(ws_url, max_size=10*1024*1024) as ws:
        msg = {
            "id": 1,
            "method": "Runtime.evaluate",
            "params": {
                "expression": "(() => { const els = document.querySelectorAll('div[data-message-author-role=\"assistant\"], .prose'); return els.length > 0 ? els[els.length - 1].innerText : document.body.innerText.slice(-2000); })()",
                "returnByValue": True
            }
        }
        await ws.send(json.dumps(msg))
        res = json.loads(await ws.recv())
        text = res.get("result", {}).get("result", {}).get("value", "")
        print(f"Arena latest text length: {len(text)}")
        print("Tail of Arena text:")
        print(text[-1000:])

if __name__ == "__main__":
    asyncio.run(check())
