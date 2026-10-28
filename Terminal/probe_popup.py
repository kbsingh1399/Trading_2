import urllib.request
import json
import asyncio
import websockets

async def check_popup():
    tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json', timeout=5).read())
    arena = next(t for t in tabs if 'arena.ai' in t.get('url', ''))
    async with websockets.connect(arena['webSocketDebuggerUrl']) as ws:
        js = """(() => {
            const hasTaskSuccessful = document.body ? document.body.innerText.includes('Was this task successful?') : false;
            const allButtons = Array.from(document.querySelectorAll('button')).map(b => ({
                text: (b.innerText || '').trim(),
                aria: b.getAttribute('aria-label') || '',
                classes: b.className,
                html: b.innerHTML.slice(0, 100)
            }));
            const popupButtons = allButtons.filter(b => 
                b.text.includes('Yes') || 
                b.text.includes('No') || 
                b.text.includes('Keep working') ||
                b.text.includes('Esc') ||
                b.aria.toLowerCase().includes('close')
            );
            return {
                hasTaskSuccessful,
                popupButtons
            };
        })()"""
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        res = json.loads(await ws.recv())
        print(json.dumps(res.get('result', {}).get('result', {}).get('value'), indent=2))

if __name__ == '__main__':
    asyncio.run(check_popup())
