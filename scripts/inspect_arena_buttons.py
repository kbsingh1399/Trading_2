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
        expr = """
        (() => {
            const sendBtn = document.querySelector('button[aria-label="Send message"], button:has(svg.lucide-arrow-up), button:has(svg[data-icon="arrow-up"])');
            const stopBtn = document.querySelector('button[aria-label="Stop generating"], button:has(svg.lucide-square)');
            const errorBanners = Array.from(document.querySelectorAll('[class*="error"], [class*="alert"], [role="alert"]')).map(e => e.innerText);
            const copyBtns = document.querySelectorAll('button[aria-label="Copy"]');
            const prose = document.querySelectorAll('.prose');
            return {
                sendBtn: !!sendBtn,
                sendDisabled: sendBtn ? sendBtn.disabled : null,
                stopBtn: !!stopBtn,
                errorBanners: errorBanners,
                copyCount: copyBtns.length,
                proseCount: prose.length
            };
        })()
        """
        msg = {"id": 1, "method": "Runtime.evaluate", "params": {"expression": expr, "returnByValue": True}}
        await ws.send(json.dumps(msg))
        res = json.loads(await ws.recv())
        print(json.dumps(res.get("result", {}).get("result", {}).get("value"), indent=2))

if __name__ == "__main__":
    asyncio.run(check())
