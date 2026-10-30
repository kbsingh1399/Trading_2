import asyncio
import json
import websockets

async def inspect():
    ws_url = 'ws://127.0.0.1:9222/devtools/page/FDDB732749CF0371E914334A4F0AD4A7'
    async with websockets.connect(ws_url) as ws:
        # Check title and current URL
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': 'document.title + " | " + window.location.href'}}))
        resp = json.loads(await ws.recv())
        print('URL/Title:', resp.get('result', {}).get('result', {}).get('value'))
        
        js = """(() => {
            const body = document.body ? document.body.innerText : '';
            const spin = document.querySelectorAll('.ant-spin, [class*="loading"], [class*="spinner"]').length;
            const canvases = document.querySelectorAll('canvas').length;
            return {
                spinnersCount: spin,
                canvasCount: canvases,
                bodyPreview: body.slice(0, 300)
            };
        })()"""
        await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        resp2 = json.loads(await ws.recv())
        print('DOM state:', json.dumps(resp2.get('result', {}).get('result', {}).get('value'), indent=2))

asyncio.run(inspect())
