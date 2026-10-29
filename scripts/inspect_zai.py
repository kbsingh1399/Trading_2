import asyncio
import json
import urllib.request
import websockets
import pathlib

ROOT = pathlib.Path(r"C:\Users\SIGMA\Documents\Trading_2")
OUTPUT_FILE = ROOT / "docs" / "trade_plans" / "ZAI_LATEST_RAW.md"

async def check_zai():
    tabs = json.loads(urllib.request.urlopen("http://localhost:9222/json").read().decode())
    zai_tab = None
    for t in tabs:
        if "chat.z.ai" in t.get("url", ""):
            zai_tab = t
            break
    if not zai_tab:
        print("No z.ai tab found")
        return
        
    ws_url = zai_tab["webSocketDebuggerUrl"]
    async with websockets.connect(ws_url, max_size=20*1024*1024) as ws:
        eval_script = """
        (() => {
            const prose = Array.from(document.querySelectorAll('.prose, [class*="prose"], [data-message-author-role="assistant"]'));
            const last = prose.length > 0 ? prose[prose.length - 1].innerText : document.body.innerText.slice(-2000);
            return {
                title: document.title,
                url: window.location.href,
                numProse: prose.length,
                lastProseLen: last.length,
                lastProseTail: last.slice(-1500)
            };
        })()
        """
        msg = {
            "id": 1,
            "method": "Runtime.evaluate",
            "params": {
                "expression": eval_script,
                "returnByValue": True
            }
        }
        await ws.send(json.dumps(msg))
        resp = await ws.recv()
        data = json.loads(resp)
        result = data.get("result", {}).get("result", {}).get("value", {})
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    asyncio.run(check_zai())
