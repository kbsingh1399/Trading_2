import json
import urllib.request
import asyncio
import websockets

async def click_send():
    pages = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json").read().decode())
    target = next((p for p in pages if "gemini.google.com" in p.get("url", "")), None)
    async with websockets.connect(target["webSocketDebuggerUrl"]) as ws:
        js = """
        (() => {
            const btn = document.querySelector('button[aria-label="Send message"]') || document.querySelector('.send-button button') || document.querySelector('[aria-label*="Send" i]');
            if (btn && !btn.disabled && btn.offsetParent !== null) {
                btn.click();
                return "CLICKED: " + btn.getAttribute('aria-label');
            }
            return "NOT_CLICKED";
        })()
        """
        await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
        resp = json.loads(await ws.recv())
        print(resp.get("result", {}).get("result", {}).get("value"))

asyncio.run(click_send())
