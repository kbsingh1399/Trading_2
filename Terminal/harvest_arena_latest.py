#!/usr/bin/env python3
"""
Terminal/harvest_arena_latest.py
Harvests the latest completed response from Arena.ai via Chrome CDP port 9222.
"""
import asyncio, json, websockets, sys, os, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.arena_bridge import get_arena_tab_ws_url

async def harvest():
    ws_url = await get_arena_tab_ws_url()
    if not ws_url:
        print("[Harvest] Error: No active Arena tab WebSocket found on CDP port 9222.")
        return False
    
    js = """(() => {
        const stop = document.querySelector('button[aria-label="Stop generating"]');
        const prose = Array.from(document.querySelectorAll('.prose'));
        const lastProse = prose.length > 0 ? prose[prose.length - 1].innerText : "";
        return {
            isGenerating: !!stop,
            count: prose.length,
            text: lastProse
        };
    })()"""
    
    try:
        async with websockets.connect(ws_url, max_size=10_000_000) as ws:
            msg = {
                'id': 77777,
                'method': 'Runtime.evaluate',
                'params': {
                    'expression': js,
                    'returnByValue': True
                }
            }
            await ws.send(json.dumps(msg))
            resp = await ws.recv()
            data = json.loads(resp)
            val = data.get('result', {}).get('result', {}).get('value', {})
            is_gen = val.get('isGenerating', False)
            text = val.get('text', '')
            count = val.get('count', 0)
            
            print(f"[Harvest] isGenerating: {is_gen} | prose count: {count} | text length: {len(text)}")
            if len(text) > 50 and not is_gen:
                out_path = ROOT / "docs" / "trade_plans" / "ARENA_LATEST_RAW.md"
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"[Harvest] Successfully saved {len(text)} bytes to {out_path}")
                print(f"[Harvest] Preview:\n{text[:350]}")
                return True
            else:
                print(f"[Harvest] Still generating or text too short.")
                return False
    except Exception as e:
        print(f"[Harvest] WebSocket error: {e}")
        return False

if __name__ == "__main__":
    asyncio.run(harvest())
