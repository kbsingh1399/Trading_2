import asyncio
import json
import urllib.request
import websockets

async def check():
    tabs = json.loads(urllib.request.urlopen("http://localhost:9222/json").read().decode("utf-8"))
    for t in tabs:
        u = t.get("url", "")
        if "arena.ai" in u and t.get("webSocketDebuggerUrl"):
            print("Arena URL:", u)
            async with websockets.connect(t["webSocketDebuggerUrl"]) as ws:
                expr = "Boolean(document.querySelector('button[aria-label*=\"Stop\"], button[title*=\"Stop\"]'))"
                await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": expr, "returnByValue": True}}))
                res = json.loads(await ws.recv())
                print("Arena generating?", res.get("result", {}).get("result", {}).get("value"))
        elif "chat.z.ai" in u and t.get("webSocketDebuggerUrl"):
            print("Z.ai URL:", u)
            async with websockets.connect(t["webSocketDebuggerUrl"]) as ws:
                expr = "Boolean(document.querySelector('button#send-message-button'))"
                await ws.send(json.dumps({"id": 2, "method": "Runtime.evaluate", "params": {"expression": expr, "returnByValue": True}}))
                res = json.loads(await ws.recv())
                print("Z.ai send button available?", res.get("result", {}).get("result", {}).get("value"))

if __name__ == "__main__":
    asyncio.run(check())
