import asyncio, json
import websockets
from Terminal.rock_hard_dual_watchdog import find_ws_url

async def main():
    ws_url = find_ws_url("chat.z.ai")
    async with websockets.connect(ws_url) as ws:
        js = """(() => {
            const stopSquare = document.querySelector('button span.size-3.rounded-xs');
            const body = document.body.innerText;
            const cycleIdx = body.lastIndexOf('Cycle_005');
            const cycleText = cycleIdx !== -1 ? body.substring(cycleIdx) : '';
            return {
                isGenerating: Boolean(stopSquare),
                cycleTextLen: cycleText.length,
                cyclePreview: cycleText.slice(-800)
            };
        })()"""
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        res = json.loads(await ws.recv())
        val = res.get('result', {}).get('result', {}).get('value')
        print(f"isGenerating: {val.get('isGenerating')}, len={val.get('cycleTextLen')}", flush=True)
        print("Tail:\n", val.get('cyclePreview'), flush=True)

if __name__ == '__main__':
    asyncio.run(main())
