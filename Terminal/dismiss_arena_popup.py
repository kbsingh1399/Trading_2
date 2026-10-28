import urllib.request
import json
import asyncio
import websockets

async def dismiss():
    tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json', timeout=5).read())
    arena = next(t for t in tabs if 'arena.ai' in t.get('url', ''))
    async with websockets.connect(arena['webSocketDebuggerUrl']) as ws:
        # Method 1: Press Escape key
        await ws.send(json.dumps({'id': 1, 'method': 'Input.dispatchKeyEvent', 'params': {'type': 'rawKeyDown', 'windowsVirtualKeyCode': 27, 'code': 'Escape', 'key': 'Escape'}}))
        await ws.recv()
        await ws.send(json.dumps({'id': 2, 'method': 'Input.dispatchKeyEvent', 'params': {'type': 'keyUp', 'windowsVirtualKeyCode': 27, 'code': 'Escape', 'key': 'Escape'}}))
        await ws.recv()
        await asyncio.sleep(0.3)
        
        # Method 2: If still present, click button[aria-label="Close review panel"]
        js = """(() => {
            const btn = document.querySelector('button[aria-label="Close review panel"]');
            if (btn) {
                btn.click();
                return 'CLICKED_CLOSE_BUTTON';
            }
            const hasTask = document.body ? document.body.innerText.includes('Was this task successful?') : false;
            return hasTask ? 'STILL_PRESENT' : 'DISMISSED_VIA_ESCAPE';
        })()"""
        await ws.send(json.dumps({'id': 3, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        res = json.loads(await ws.recv())
        val = res.get('result', {}).get('result', {}).get('value')
        print('Dismiss Result:', val)
        return val

if __name__ == '__main__':
    asyncio.run(dismiss())
