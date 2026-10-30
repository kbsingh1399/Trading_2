import asyncio
import json
import websockets

async def inspect_arena_dom():
    ws_url = 'ws://127.0.0.1:9222/devtools/page/B4F33872C7D13C093D32CB2AFF0055C0'
    async with websockets.connect(ws_url) as ws:
        js = """(() => {
            const bodyText = document.body ? document.body.innerText : '';
            const allBtns = Array.from(document.querySelectorAll('button')).map(b => ({
                text: b.innerText.slice(0, 30),
                aria: b.getAttribute('aria-label'),
                testid: b.getAttribute('data-testid')
            }));
            const codeBlocks = document.querySelectorAll('pre, code').length;
            return {
                bodyLen: bodyText.length,
                snippet: bodyText.slice(-1000),
                buttons: allBtns.slice(0, 15),
                codeBlocks: codeBlocks
            };
        })()"""
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        resp = json.loads(await ws.recv())
        print(json.dumps(resp.get('result', {}).get('result', {}).get('value'), indent=2))

asyncio.run(inspect_arena_dom())
