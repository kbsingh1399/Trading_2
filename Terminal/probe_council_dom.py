import urllib.request
import json
import asyncio
import websockets

async def check():
    raw = urllib.request.urlopen('http://127.0.0.1:9222/json', timeout=5).read()
    tabs = json.loads(raw)
    
    arena_tab = next((t for t in tabs if 'arena.ai' in t.get('url', '') and t.get('webSocketDebuggerUrl')), None)
    zai_tab = next((t for t in tabs if 'chat.z.ai' in t.get('url', '') and t.get('webSocketDebuggerUrl')), None)
    
    print('Arena Tab:', arena_tab.get('url') if arena_tab else None)
    print('Zai Tab:', zai_tab.get('url') if zai_tab else None)
    
    if arena_tab:
        async with websockets.connect(arena_tab['webSocketDebuggerUrl'], max_size=10_000_000) as ws:
            js = """(() => {
                const buttons = Array.from(document.querySelectorAll('button')).map(b => ({
                    text: (b.innerText || '').trim(),
                    ariaLabel: b.getAttribute('aria-label') || '',
                    title: b.getAttribute('title') || '',
                    classes: b.className,
                    svg: Boolean(b.querySelector('svg')),
                    innerHTML: b.innerHTML.slice(0, 100)
                }));
                const stopButtons = buttons.filter(b => 
                    b.ariaLabel.toLowerCase().includes('stop') || 
                    b.title.toLowerCase().includes('stop') || 
                    b.text.toLowerCase().includes('stop') || 
                    b.classes.includes('stop')
                );
                
                // Inspect input area buttons
                const footerButtons = Array.from(document.querySelectorAll('form button, div[class*="composer"] button, div[class*="input"] button')).map(b => ({
                    ariaLabel: b.getAttribute('aria-label') || '',
                    classes: b.className,
                    text: (b.innerText || '').trim(),
                    innerHTML: b.innerHTML.slice(0, 100)
                }));
                
                const hasCopy = Array.from(document.querySelectorAll('button[aria-label="Copy"]')).length;
                const hasTaskSuccessful = document.body.innerText.includes('Was this task successful?');
                
                return {
                    url: location.href,
                    allButtons: buttons.length,
                    stopButtons,
                    footerButtons,
                    hasCopy,
                    hasTaskSuccessful,
                    bodyLength: document.body.innerText.length
                };
            })()"""
            await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
            res = json.loads(await ws.recv())
            print('ARENA DOM PROBE:', json.dumps(res.get('result', {}).get('result', {}).get('value'), indent=2))
            
    if zai_tab:
        async with websockets.connect(zai_tab['webSocketDebuggerUrl'], max_size=10_000_000) as ws:
            js = """(() => {
                const buttons = Array.from(document.querySelectorAll('button')).map(b => ({
                    text: (b.innerText || '').trim(),
                    ariaLabel: b.getAttribute('aria-label') || '',
                    title: b.getAttribute('title') || '',
                    classes: b.className,
                    hasSquare: Boolean(b.querySelector('span[class*="size-3"][class*="rounded-xs"]')),
                    innerHTML: b.innerHTML.slice(0, 100)
                }));
                const stopButtons = buttons.filter(b => 
                    b.ariaLabel.toLowerCase().includes('stop') || 
                    b.title.toLowerCase().includes('stop') || 
                    b.hasSquare
                );
                const sendBtn = document.querySelector('button#send-message-button');
                const thinking = Array.from(document.querySelectorAll('*')).filter(e => (e.innerText || '').trim().startsWith('Thinking')).length;
                return {
                    url: location.href,
                    stopButtons,
                    sendBtnExists: Boolean(sendBtn),
                    thinkingFound: thinking > 0,
                    bodyLength: document.body.innerText.length
                };
            })()"""
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
            res = json.loads(await ws.recv())
            print('ZAI DOM PROBE:', json.dumps(res.get('result', {}).get('result', {}).get('value'), indent=2))

if __name__ == '__main__':
    asyncio.run(check())
