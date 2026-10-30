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
        const stopBtns = Array.from(document.querySelectorAll('button[aria-label="Stop generating"], button:has(svg rect), button[aria-label*="Stop"], button[title*="Stop"], button.stop-button'));
        const allBtns = Array.from(document.querySelectorAll('button')).map(b => ({
            text: (b.innerText || '').trim(),
            aria: b.getAttribute('aria-label'),
            title: b.getAttribute('title'),
            cls: b.className
        }));
        const copyBtns = Array.from(document.querySelectorAll('button[aria-label="Copy"]'));
        const bodyText = document.body ? document.body.innerText : '';
        const hasKeepWorking = Array.from(document.querySelectorAll('button')).some(b => (b.innerText || '').trim() === 'Keep working');
        const hasYesNo = bodyText.includes('Was this task successful?') || hasKeepWorking;
        
        return {
            stopBtns: stopBtns.map(b => ({ aria: b.getAttribute('aria-label'), text: b.innerText })),
            copyBtnsCount: copyBtns.length,
            hasKeepWorking,
            hasYesNo,
            buttonsSample: allBtns.filter(b => b.aria || b.text).slice(-15)
        };
    })()"""

    async with websockets.connect(ws_url, max_size=10_000_000) as ws:
        await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
        res = json.loads(await ws.recv())
        print(json.dumps(res.get("result", {}).get("result", {}).get("value"), indent=2))

if __name__ == "__main__":
    asyncio.run(main())
