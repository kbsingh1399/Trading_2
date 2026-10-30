import asyncio
import json
import urllib.request
import websockets

async def probe():
    tabs = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json").read().decode())
    arena = next((t for t in tabs if "arena.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)
    zai = next((t for t in tabs if ("z.ai" in t.get("url", "") or "chat.z.ai" in t.get("url", "")) and t.get("webSocketDebuggerUrl")), None)
    
    print("=== CDP TABS PROBE ===")
    if arena:
        async with websockets.connect(arena["webSocketDebuggerUrl"]) as ws:
            js = """(() => {
                const isGen = document.querySelector('button[aria-label="Stop generating"], button.stop, [data-testid="stop-button"]') !== null;
                const msgs = Array.from(document.querySelectorAll('.message, [class*="message"], [data-message-author-role="assistant"]'));
                const last = msgs.length ? msgs[msgs.length - 1].innerText : '';
                return { isGenerating: isGen, msgCount: msgs.length, lastLen: last.length, preview: last.slice(0, 400) };
            })()"""
            await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
            r = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value")
            print("Arena.ai:", r)
    else:
        print("Arena.ai tab not found")

    if zai:
        async with websockets.connect(zai["webSocketDebuggerUrl"]) as ws:
            js = """(() => {
                const isGen = document.querySelector('button[aria-label="Stop generating"], button.stop, [data-testid="stop-button"]') !== null;
                const msgs = Array.from(document.querySelectorAll('.message, [class*="message"], [data-message-author-role="assistant"]'));
                const last = msgs.length ? msgs[msgs.length - 1].innerText : '';
                return { isGenerating: isGen, msgCount: msgs.length, lastLen: last.length, preview: last.slice(0, 400) };
            })()"""
            await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
            r = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value")
            print("Z.ai:", r)
    else:
        print("Z.ai tab not found")

asyncio.run(probe())
