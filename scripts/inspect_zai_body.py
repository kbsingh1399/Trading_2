import asyncio
import json
import sys
import urllib.request
import websockets

sys.stdout.reconfigure(encoding='utf-8')

async def inspect():
    raw = urllib.request.urlopen('http://127.0.0.1:9222/json').read().decode('utf-8')
    tabs = json.loads(raw)
    for t in tabs:
        if 'chat.z.ai' in t.get('url', ''):
            ws = await websockets.connect(t['webSocketDebuggerUrl'])
            js = """(() => {
                const msgs = Array.from(document.querySelectorAll('div, p, span')).filter(e => e.innerText && e.innerText.includes('Cycle_032'));
                return JSON.stringify({
                    foundCycle32: msgs.length,
                    bodySnippet: document.body.innerText.slice(-1500)
                });
            })()"""
            await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
            res = json.loads(await ws.recv())
            val = json.loads(res['result']['result']['value'])
            print(val['bodySnippet'])
            await ws.close()

if __name__ == '__main__':
    asyncio.run(inspect())
