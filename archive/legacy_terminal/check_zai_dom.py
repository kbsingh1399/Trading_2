import urllib.request, json, asyncio, websockets

async def check():
    tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json', timeout=5).read().decode())
    zai_tab = next((t for t in tabs if 'chat.z.ai' in t.get('url', '') or 'z.ai' in t.get('url', '')), None)
    if not zai_tab:
        print('No Z.ai tab found')
        return

    async with websockets.connect(zai_tab['webSocketDebuggerUrl']) as ws:
        expr = """
        (() => {
            const txt = document.body.innerText;
            const stopBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.includes('Stop') || (b.getAttribute('aria-label') && b.getAttribute('aria-label').includes('Stop')));
            const isGen = !!stopBtn || txt.includes('Stop generating') || txt.includes('Thinking...');
            const inputEl = document.querySelector('textarea, [contenteditable="true"]');
            return {
                inputTextLength: inputEl ? (inputEl.value || inputEl.innerText || '').length : 0,
                isGenerating: isGen,
                totalPageTextLength: txt.length
            };
        })()
        """
        await ws.send(json.dumps({'id': 1002, 'method': 'Runtime.evaluate', 'params': {'expression': expr, 'returnByValue': True}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 1002:
                val = msg.get('result', {}).get('result', {}).get('value')
                print('Z.ai Probe Result:', json.dumps(val, indent=2))
                break

if __name__ == '__main__':
    asyncio.run(check())
