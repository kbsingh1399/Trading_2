import asyncio
import json
import sys
import websockets
from pathlib import Path

sys.path.insert(0, ".")
from Terminal.rock_hard_dual_watchdog import find_ws_url

async def main():
    ws_url = find_ws_url("arena.ai")
    if not ws_url:
        print("Arena tab not found")
        return
        
    js = """(() => {
        const allProses = Array.from(document.querySelectorAll('.prose')).filter(p => (p.innerText || '').trim().length > 50);
        return allProses.map((p, idx) => ({
            idx,
            len: (p.innerText || '').length,
            sample: (p.innerText || '').substring(0, 150)
        }));
    })()"""

    async with websockets.connect(ws_url, max_size=10_000_000) as ws:
        await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
        res = json.loads(await ws.recv())
        print(json.dumps(res.get("result", {}).get("result", {}).get("value"), indent=2))

if __name__ == "__main__":
    asyncio.run(main())
