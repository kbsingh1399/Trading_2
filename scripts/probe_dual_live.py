import asyncio
import json
import urllib.request
import websockets

async def check_tabs():
    raw = urllib.request.urlopen('http://127.0.0.1:9222/json', timeout=5).read()
    tabs = json.loads(raw)
    for t in tabs:
        url = t.get('url', '')
        ws = t.get('webSocketDebuggerUrl')
        if not ws:
            continue
        if 'arena.ai' in url:
            print('=== ARENA.AI ===')
            async with websockets.connect(ws, max_size=20*1024*1024) as client:
                js = '''(() => {
                    const stopBtn = document.querySelector('button[aria-label="Stop"]') || 
                                    document.querySelector('button:has(svg.lucide-square)') ||
                                    Array.from(document.querySelectorAll('button')).find(b => (b.innerText || '').includes('Stop'));
                    const msgs = document.querySelectorAll('.prose, [data-message-author-role="assistant"], div[class*="message"]');
                    const lastMsg = msgs.length > 0 ? msgs[msgs.length - 1].innerText : '';
                    return {
                        isGenerating: !!stopBtn,
                        msgCount: msgs.length,
                        lastMsgLen: lastMsg.length,
                        first100: lastMsg.slice(0, 150),
                        last150: lastMsg.slice(-150)
                    };
                })()'''
                await client.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
                res = json.loads(await client.recv())
                val = res.get('result', {}).get('result', {}).get('value', {})
                print(json.dumps(val, indent=2))
                
        elif 'chat.z.ai' in url or 'z.ai' in url:
            print('=== Z.AI ===')
            async with websockets.connect(ws, max_size=20*1024*1024) as client:
                js = '''(() => {
                    const stopBtn = document.querySelector('button[aria-label="Stop"]') || 
                                    document.querySelector('.stop-button') ||
                                    Array.from(document.querySelectorAll('button')).find(b => (b.innerText || '').includes('Stop'));
                    const msgs = document.querySelectorAll('.message-bubble, .prose, [data-role="assistant"], div[class*="message"]');
                    const lastMsg = msgs.length > 0 ? msgs[msgs.length - 1].innerText : '';
                    return {
                        isGenerating: !!stopBtn,
                        msgCount: msgs.length,
                        lastMsgLen: lastMsg.length,
                        first100: lastMsg.slice(0, 150),
                        last150: lastMsg.slice(-150)
                    };
                })()'''
                await client.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
                res = json.loads(await client.recv())
                val = res.get('result', {}).get('result', {}).get('value', {})
                print(json.dumps(val, indent=2))

if __name__ == '__main__':
    asyncio.run(check_tabs())
