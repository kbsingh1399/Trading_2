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
                "expression": "document.querySelectorAll('button[aria-label=\"Stop\"]').length > 0",
                "returnByValue": True
            }
        }
        await ws.send(json.dumps(msg))
        res = json.loads(await ws.recv())
        has_stop = res.get("result", {}).get("result", {}).get("value")
        print("Arena has stop button:", has_stop)
        
        msg2 = {
            "id": 2,
            "method": "Runtime.evaluate",
            "params": {
                "expression": "document.querySelectorAll('button[aria-label=\"Copy\"]').length",
                "returnByValue": True
            }
        }
        await ws.send(json.dumps(msg2))
        res2 = json.loads(await ws.recv())
        copy_count = res2.get("result", {}).get("result", {}).get("value")
        print("Arena copy button count:", copy_count)

if __name__ == "__main__":
    asyncio.run(check())
