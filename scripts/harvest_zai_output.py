import asyncio
import json
import urllib.request
import websockets
import pathlib
import time

ROOT = pathlib.Path(r"C:\Users\SIGMA\Documents\Trading_2")
OUTPUT_FILE = ROOT / "docs" / "trade_plans" / "ZAI_LATEST_RAW.md"
STATUS_FILE = ROOT / "Data" / "zai_completion_status.json"

async def check_and_harvest_zai():
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
    print("Connecting to Z.ai WS:", ws_url)
    async with websockets.connect(ws_url, max_size=30*1024*1024) as ws:
        eval_script = """
        (() => {
            const buttons = Array.from(document.querySelectorAll('button')).map(b => b.innerText || b.getAttribute('aria-label') || '');
            const hasStop = buttons.some(b => b.toLowerCase().includes('stop'));
            
            // prose elements
            const prose = Array.from(document.querySelectorAll('.prose, [class*="prose"], [data-message-author-role="assistant"]'));
            const last = prose.length > 0 ? prose[prose.length - 1].innerText : document.body.innerText.slice(-3000);
            
            return {
                title: document.title,
                url: window.location.href,
                hasStop: hasStop,
                numProse: prose.length,
                lastProseLen: last.length,
                lastProseHead: last.slice(0, 1000),
                lastProseTail: last.slice(-2000),
                fullLastProse: last
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
        print(f"Z.ai Status: hasStop={result.get('hasStop')}, numProse={result.get('numProse')}, lastLen={result.get('lastProseLen')}")
        
        full_text = result.get("fullLastProse", "")
        if len(full_text) > 0:
            OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                f.write(full_text)
            print(f"Saved full Z.ai response to {OUTPUT_FILE} ({len(full_text)} chars)")
            
            status = {
                "timestamp_utc": time.strftime("%Y-%m-%d %H:%M:%S UTC"),
                "status": "COMPLETED" if not result.get("hasStop") else "GENERATING",
                "length": len(full_text)
            }
            with open(STATUS_FILE, "w", encoding="utf-8") as f:
                json.dump(status, f, indent=2)
                
        print("\n--- Z.ai Latest Text Preview (End) ---")
        print(result.get("lastProseTail", "")[-1500:])

if __name__ == "__main__":
    asyncio.run(check_and_harvest_zai())
