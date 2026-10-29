import asyncio, json
import websockets
from Terminal.rock_hard_dual_watchdog import find_ws_url

async def main():
    ws_url = find_ws_url("chat.z.ai")
    async with websockets.connect(ws_url) as ws:
        js = """(() => {
            const stopBtn = document.querySelector('button[aria-label*="Stop"], button[title*="Stop"], button.stop-button');
            const stopSquare = document.querySelector('button span.size-3.rounded-xs');
            return {
                hasStopBtn: Boolean(stopBtn),
                hasStopSquare: Boolean(stopSquare),
                bodyLen: document.body.innerText.length
            };
        })()"""
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        res = json.loads(await ws.recv())
        print(res.get('result', {}).get('result', {}).get('value'))

if __name__ == '__main__':
    asyncio.run(main())
