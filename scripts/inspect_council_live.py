import asyncio
import json
import urllib.request
import websockets

async def check():
    tabs = json.loads(urllib.request.urlopen("http://localhost:9222/json").read().decode("utf-8"))
    
    # 1. Arena
    arena_tab = next((t for t in tabs if "arena.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)
    if arena_tab:
        async with websockets.connect(arena_tab["webSocketDebuggerUrl"]) as ws:
            js = """(() => {
                const isGen = Boolean(document.querySelector('button[aria-label*="Stop"], button[title*="Stop"]'));
                const msgs = document.querySelectorAll('[data-message-author-role="assistant"], .prose');
                const last = msgs[msgs.length - 1];
                return {
                    isGen: isGen,
                    count: msgs.length,
                    textLen: last ? last.innerText.length : 0,
                    preview: last ? last.innerText.slice(0, 300) : '',
                    tail: last ? last.innerText.slice(-300) : ''
                };
            })()"""
            await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
            res = json.loads(await ws.recv())
            print("--- ARENA.AI LIVE ---")
            print(json.dumps(res.get("result", {}).get("result", {}).get("value"), indent=2))

    # 2. Z.ai
    zai_tab = next((t for t in tabs if "chat.z.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)
    if zai_tab:
        async with websockets.connect(zai_tab["webSocketDebuggerUrl"]) as ws:
            js = """(() => {
                const stopBtn = Boolean(document.querySelector('button span.size-3.rounded-xs, button[aria-label*="Stop"], button[title*="Stop"]'));
                const msgs = document.querySelectorAll('[data-message-author-role="assistant"], .prose');
                const last = msgs[msgs.length - 1];
                return {
                    isGen: stopBtn,
                    count: msgs.length,
                    textLen: last ? last.innerText.length : 0,
                    preview: last ? last.innerText.slice(0, 300) : '',
                    tail: last ? last.innerText.slice(-300) : ''
                };
            })()"""
            await ws.send(json.dumps({"id": 2, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
            res = json.loads(await ws.recv())
            print("--- Z.AI LIVE ---")
            print(json.dumps(res.get("result", {}).get("result", {}).get("value"), indent=2))

if __name__ == "__main__":
    asyncio.run(check())
