import asyncio, json, time
import websockets
from Terminal.rock_hard_dual_watchdog import find_ws_url

async def main():
    ws_url = find_ws_url("chat.z.ai")
    async with websockets.connect(ws_url) as ws:
        for i in range(10):
            js = """(() => {
                const stopSquare = document.querySelector('button span.size-3.rounded-xs');
                const last = document.querySelector('.chat-assistant:last-child, [data-message-author-role="assistant"]:last-child');
                const text = last ? last.innerText : '';
                return {
                    isGenerating: Boolean(stopSquare),
                    len: text.length,
                    hasReport: text.includes('[COUNCIL REPORT'),
                    hasEnd: text.includes('[END OF REPORT')
                };
            })()"""
            await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
            res = json.loads(await ws.recv())
            val = res.get('result', {}).get('result', {}).get('value')
            print(f"Tick {i}: isGen={val.get('isGenerating')}, len={val.get('len')}, hasReport={val.get('hasReport')}, hasEnd={val.get('hasEnd')}", flush=True)
            if not val.get('isGenerating') and val.get('hasEnd'):
                print("Z.ai FINISHED!", flush=True)
                return
            await asyncio.sleep(3.0)

if __name__ == '__main__':
    asyncio.run(main())
