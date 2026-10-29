import asyncio, json
import websockets
from Terminal.rock_hard_dual_watchdog import find_ws_url

async def main():
    ws_url = find_ws_url("chat.z.ai")
    async with websockets.connect(ws_url) as ws:
        js = """(() => {
            const allChatMsgs = Array.from(document.querySelectorAll('.chat-assistant.markdown-prose, div.prose'));
            return allChatMsgs.map((m, i) => ({
                idx: i,
                len: m.innerText.length,
                preview: m.innerText.slice(0, 100),
                has_Cycle: m.innerText.includes('Cycle')
            }));
        })()"""
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        res = json.loads(await ws.recv())
        val = res.get('result', {}).get('result', {}).get('value', [])
        print(f"Total prose elements: {len(val)}", flush=True)
        for item in val:
            print(f"  {item['idx']}: len={item['len']}, has_Cycle={item['has_Cycle']}, preview={repr(item['preview'])}", flush=True)

if __name__ == '__main__':
    asyncio.run(main())
