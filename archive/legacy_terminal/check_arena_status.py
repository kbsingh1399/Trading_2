import asyncio
import json
import pathlib
import sys
import websockets

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.arena_bridge import get_arena_tab_ws_url

async def check():
    ws_url = await get_arena_tab_ws_url()
    if not ws_url:
        print(json.dumps({"error": "No active Arena tab found"}))
        return
    async with websockets.connect(ws_url) as ws:
        expr = """(() => {
            const stopBtn = document.querySelector('button[aria-label="Stop generating"], button:has(svg.lucide-square)');
            const sendBtn = document.querySelector('button[aria-label="Send message"]');
            const prose = Array.from(document.querySelectorAll('.prose')).filter(el => !el.classList.contains('tiptap'));
            const lastEl = prose.length > 0 ? prose[prose.length - 1] : null;
            return {
                isGenerating: !!stopBtn,
                proseCount: prose.length,
                lastSnippet: lastEl ? lastEl.innerText.substring(0, 300) : '',
                lastLength: lastEl ? lastEl.innerText.length : 0
            };
        })()"""
        msg = {'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': expr, 'returnByValue': True}}
        await ws.send(json.dumps(msg))
        res = json.loads(await ws.recv())
        val = res.get('result', {}).get('result', {}).get('value', {})
        print(json.dumps(val, indent=2))

if __name__ == '__main__':
    asyncio.run(check())
