import asyncio, json
import websockets
from Terminal.arena_bridge import get_zai_tab_ws_url

async def main():
    ws_url = await get_zai_tab_ws_url()
    async with websockets.connect(ws_url, max_size=20_000_000) as ws:
        js = """
        (() => {
            const proses = document.querySelectorAll('div.prose');
            return Array.from(proses).map((p, idx) => ({
                idx: idx,
                len: p.innerText.length,
                head: p.innerText.slice(0, 150),
                tail: p.innerText.slice(-150)
            }));
        })()
        """
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        res = json.loads(await ws.recv())
        val = res.get('result', {}).get('result', {}).get('value', [])
        for item in val:
            print(f"Prose {item['idx']}: len={item['len']}")
            print("  Head:", repr(item['head']))
            print("  Tail:", repr(item['tail']))

        # Also get full text of last prose
        if val:
            last_idx = len(val) - 1
            js_last = f"document.querySelectorAll('div.prose')[{last_idx}].innerText"
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': js_last, 'returnByValue': True}}))
            res_last = json.loads(await ws.recv())
            last_text = res_last.get('result', {}).get('result', {}).get('value', '')
            with open('docs/trade_plans/ZAI_LATEST_RAW.md', 'w', encoding='utf-8') as f:
                f.write(last_text)
            print("Saved latest prose to docs/trade_plans/ZAI_LATEST_RAW.md! Len:", len(last_text))

if __name__ == '__main__':
    asyncio.run(main())
