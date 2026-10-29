import asyncio
import json
import urllib.request
import websockets
import pathlib

ROOT = pathlib.Path(r"C:\Users\SIGMA\Documents\Trading_2")
OUTPUT_FILE = ROOT / "docs" / "trade_plans" / "ARENA_LATEST_RAW.md"
STATUS_FILE = ROOT / "Data" / "arena_completion_status.json"

async def harvest_arena():
    tabs = json.loads(urllib.request.urlopen("http://localhost:9222/json").read().decode())
    arena_tab = None
    for t in tabs:
        if "arena.ai" in t.get("url", ""):
            arena_tab = t
            break
    if not arena_tab:
        print("No arena.ai tab found")
        return
        
    ws_url = arena_tab["webSocketDebuggerUrl"]
    print("Connecting to Arena WS:", ws_url)
    async with websockets.connect(ws_url, max_size=30*1024*1024) as ws:
        # Script to get the last assistant message
        eval_script = """
        (() => {
            // Find all prose blocks
            const prose = Array.from(document.querySelectorAll('.prose, [class*="prose"], [data-message-author-role="assistant"]'));
            if (prose.length > 0) {
                return prose[prose.length - 1].innerText;
            }
            // fallback: find all markdown or text containers
            const messages = Array.from(document.querySelectorAll('[class*="message"], [class*="markdown"]'));
            if (messages.length > 0) {
                return messages[messages.length - 1].innerText;
            }
            return document.body.innerText;
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
        text = data.get("result", {}).get("result", {}).get("value", "")
        print(f"Extracted Arena text length: {len(text)} characters")
        
        if len(text) > 0:
            OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Saved to {OUTPUT_FILE}")
            
            status = {
                "timestamp_utc": "2026-10-29 11:37:00 UTC",
                "status": "COMPLETED",
                "length": len(text),
                "cycle": "Cycle_009"
            }
            with open(STATUS_FILE, "w", encoding="utf-8") as f:
                json.dump(status, f, indent=2)

if __name__ == "__main__":
    asyncio.run(harvest_arena())
