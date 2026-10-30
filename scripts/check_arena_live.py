import asyncio
import json
import websockets

async def check_arena():
    ws_url = 'ws://127.0.0.1:9222/devtools/page/B4F33872C7D13C093D32CB2AFF0055C0'
    async with websockets.connect(ws_url) as ws:
        js = """(() => {
            const isGen = document.querySelector('button[aria-label="Stop generating"], button.stop, [data-testid="stop-button"]') !== null;
            const msgs = Array.from(document.querySelectorAll('.message, [class*="message"], [data-message-author-role="assistant"]'));
            const last = msgs.length ? msgs[msgs.length - 1].innerText : '';
            return {
                isGenerating: isGen,
                messageCount: msgs.length,
                lastLength: last.length,
                preview: last.slice(0, 500)
            };
        })()"""
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        resp = json.loads(await ws.recv())
        print(json.dumps(resp.get('result', {}).get('result', {}).get('value'), indent=2))

asyncio.run(check_arena())
