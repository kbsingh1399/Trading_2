import asyncio, json
import websockets
from Terminal.rock_hard_dual_watchdog import find_ws_url

async def main():
    ws_url = find_ws_url("chat.z.ai")
    async with websockets.connect(ws_url) as ws:
        js = """(() => {
            const msgs = document.querySelectorAll('.chat-assistant, [data-message-author-role="assistant"]');
            const last = msgs.length > 0 ? msgs[msgs.length - 1] : null;
            if (!last) return 'no last assistant msg';
            const allElements = Array.from(last.querySelectorAll('*'));
            const textElements = allElements.filter(e => e.children.length === 0 && e.innerText && e.innerText.trim());
            return {
                totalElements: allElements.length,
                textSnippets: textElements.slice(-10).map(e => e.innerText.trim())
            };
        })()"""
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        res = json.loads(await ws.recv())
        val = res.get('result', {}).get('result', {}).get('value')
        print(val)

if __name__ == '__main__':
    asyncio.run(main())
