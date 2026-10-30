import asyncio, json, websockets, sys
sys.stdout.reconfigure(encoding='utf-8')
from Terminal.arena_bridge import get_arena_tab_ws_url

async def inspect():
    ws_url = await get_arena_tab_ws_url()
    js = """(() => {
        const pres = Array.from(document.querySelectorAll('pre, .cm-content, code, [role="tabpanel"]')).map(el => el.innerText.trim()).filter(t => t.length > 50);
        return {
            preCount: pres.length,
            preLens: pres.map(p => p.length),
            firstFew: pres.map(p => p.slice(0, 100))
        };
    })()"""
    async with websockets.connect(ws_url, max_size=10_000_000) as ws:
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        r = json.loads(await ws.recv())
        print(r.get('result', {}).get('result', {}).get('value'))

if __name__ == '__main__':
    asyncio.run(inspect())
