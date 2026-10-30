import asyncio
import json
import urllib.request
import websockets

async def check():
    raw = urllib.request.urlopen('http://127.0.0.1:9222/json').read().decode('utf-8')
    tabs = json.loads(raw)
    for t in tabs:
        if 'chat.z.ai' in t.get('url', ''):
            ws = await websockets.connect(t['webSocketDebuggerUrl'])
            js = """(() => {
                const stopBtn = document.querySelector('button[aria-label*="Stop" i], button[title*="Stop" i], svg.lucide-square, .lucide-square');
                const isGen = !!stopBtn;
                const articles = document.querySelectorAll('article, .markdown-body, [data-message-author-role="assistant"]');
                const last = articles.length > 0 ? articles[articles.length - 1] : null;
                return JSON.stringify({
                    isGenerating: isGen,
                    hasStopBtn: !!stopBtn,
                    textLength: last ? last.innerText.length : 0,
                    snippet: last ? last.innerText.slice(-200) : ''
                });
            })()"""
            await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
            res = json.loads(await ws.recv())
            val = json.loads(res['result']['result']['value'])
            print('Z.ai status:', json.dumps(val, indent=2))
            await ws.close()

if __name__ == '__main__':
    asyncio.run(check())
