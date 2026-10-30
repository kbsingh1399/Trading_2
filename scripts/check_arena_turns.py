import asyncio
import json
import websockets

async def check_arena_latest():
    ws_url = 'ws://127.0.0.1:9222/devtools/page/B4F33872C7D13C093D32CB2AFF0055C0'
    async with websockets.connect(ws_url) as ws:
        js = """(() => {
            const agentTurns = Array.from(document.querySelectorAll('[data-role="assistant"], [class*="response"], [class*="message-assistant"], [class*="chat-message"]'));
            const lastTurn = agentTurns.length ? agentTurns[agentTurns.length - 1].innerText : '';
            const statusIndicator = document.querySelector('[class*="status"], [class*="badge"], [class*="loader"]');
            return {
                agentTurnsCount: agentTurns.length,
                lastTurnLen: lastTurn.length,
                lastTurnSnippet: lastTurn.slice(0, 1000),
                statusText: statusIndicator ? statusIndicator.innerText : ''
            };
        })()"""
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        resp = json.loads(await ws.recv())
        print(json.dumps(resp.get('result', {}).get('result', {}).get('value'), indent=2))

asyncio.run(check_arena_latest())
