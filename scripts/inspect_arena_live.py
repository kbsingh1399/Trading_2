import asyncio
import json
import urllib.request
import websockets

async def check_arena():
    tabs = json.loads(urllib.request.urlopen('http://localhost:9222/json').read().decode())
    arena_tab = None
    for t in tabs:
        if 'arena.ai' in t.get('url', ''):
            arena_tab = t
            break
    if not arena_tab:
        print('No arena.ai tab found')
        return
        
    ws_url = arena_tab['webSocketDebuggerUrl']
    print('Connecting to Arena WS:', ws_url)
    async with websockets.connect(ws_url, max_size=25*1024*1024) as ws:
        eval_script = """
        (() => {
            const buttons = Array.from(document.querySelectorAll('button')).map(b => b.innerText || b.getAttribute('aria-label') || '');
            const hasStop = buttons.some(b => b.toLowerCase().includes('stop'));
            const hasCopy = buttons.some(b => b.toLowerCase().includes('copy'));
            
            // Get all user and assistant turns
            const turns = [];
            // Try different selectors
            const elements = document.querySelectorAll('[data-message-author-role], .prose, div[class*="message"]');
            
            // Also grab full text from the main container
            const main = document.querySelector('main') || document.body;
            
            return {
                title: document.title,
                url: window.location.href,
                hasStop: hasStop,
                hasCopy: hasCopy,
                buttons: buttons.filter(b => b.trim().length > 0).slice(0, 20),
                mainTextLen: main.innerText.length,
                mainTextTail: main.innerText.slice(-3000)
            };
        })()
        """
        msg = {
            'id': 1,
            'method': 'Runtime.evaluate',
            'params': {
                'expression': eval_script,
                'returnByValue': True
            }
        }
        await ws.send(json.dumps(msg))
        resp = await ws.recv()
        data = json.loads(resp)
        result = data.get('result', {}).get('result', {}).get('value', {})
        print(json.dumps(result, indent=2))

if __name__ == '__main__':
    asyncio.run(check_arena())
