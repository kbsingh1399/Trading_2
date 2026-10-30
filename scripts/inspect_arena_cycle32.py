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
        if 'arena.ai' in t.get('url', ''):
            ws = await websockets.connect(t['webSocketDebuggerUrl'])
            js = """(() => {
                const diff = document.querySelector('.diff, [class*="diff"], [class*="monaco"], pre');
                const diffStr = (diff && (diff.innerText || diff.textContent)) ? (diff.innerText || diff.textContent) : '';
                const prose = Array.from(document.querySelectorAll('.prose, [data-message-author-role="assistant"]'));
                const lastProse = (prose.length > 0 && (prose[prose.length - 1].innerText || prose[prose.length - 1].textContent)) ? (prose[prose.length - 1].innerText || prose[prose.length - 1].textContent) : '';
                return JSON.stringify({
                    prose: lastProse,
                    diffText: diffStr.slice(0, 3000)
                });
            })()"""
            await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
            res = json.loads(await ws.recv())
            print("RAW RES:", res)
            if 'result' in res and 'result' in res['result'] and 'value' in res['result']['result']:
                val = json.loads(res['result']['result']['value'])
                print("=== ARENA PROSE ===")
                print(val['prose'])
                print("\n=== ARENA DIFF ===")
                print(val['diffText'][:2000])
            await ws.close()

if __name__ == '__main__':
    asyncio.run(inspect())
