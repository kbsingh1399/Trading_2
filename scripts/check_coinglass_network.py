import asyncio
import json
import websockets

async def check_console():
    ws_url = 'ws://127.0.0.1:9222/devtools/page/FDDB732749CF0371E914334A4F0AD4A7'
    async with websockets.connect(ws_url) as ws:
        # Check network requests or console messages via Runtime
        js = """(() => {
            const entries = window.performance ? window.performance.getEntriesByType('resource') : [];
            const failed = entries.filter(e => e.duration === 0 || (e.responseStatus && e.responseStatus >= 400));
            const recent = entries.slice(-15).map(e => ({ name: e.name.slice(0, 100), duration: Math.round(e.duration), status: e.responseStatus }));
            return {
                totalResources: entries.length,
                failedCount: failed.length,
                recent: recent
            };
        })()"""
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        resp = json.loads(await ws.recv())
        print(json.dumps(resp.get('result', {}).get('result', {}).get('value'), indent=2))

asyncio.run(check_console())
