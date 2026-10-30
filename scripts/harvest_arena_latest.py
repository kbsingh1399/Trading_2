import asyncio
import json
import urllib.request
import websockets
import pathlib

ROOT = pathlib.Path(r"C:\Users\SIGMA\Documents\Trading_2")
OUTPUT_FILE = ROOT / "docs" / "trade_plans" / "ARENA_LATEST_RAW.md"
STATUS_FILE = ROOT / "Data" / "arena_completion_status.json"

async def harvest():
    raw = urllib.request.urlopen("http://127.0.0.1:9222/json").read().decode("utf-8")
    tabs = json.loads(raw)
    for t in tabs:
        if "arena.ai" in t.get("url", ""):
            ws = await websockets.connect(t["webSocketDebuggerUrl"], max_size=30*1024*1024)
            js = """(() => {
                const prose = Array.from(document.querySelectorAll('.prose, [data-message-author-role="assistant"]'));
                return (prose.length > 0 && (prose[prose.length - 1].innerText || prose[prose.length - 1].textContent)) ? (prose[prose.length - 1].innerText || prose[prose.length - 1].textContent) : '';
            })()"""
            await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
            res = json.loads(await ws.recv())
            val = res.get("result", {}).get("result", {}).get("value", "")
            if val:
                with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                    f.write(val)
                print(f"Successfully harvested Arena ({len(val)} chars) to {OUTPUT_FILE}")
                status = {"status": "COMPLETED", "length": len(val), "cycle": "Cycle_037"}
                with open(STATUS_FILE, "w", encoding="utf-8") as f:
                    json.dump(status, f, indent=2)
            await ws.close()
            break

if __name__ == "__main__":
    asyncio.run(harvest())
