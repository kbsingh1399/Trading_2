import urllib.request, json, asyncio, websockets

async def check():
    tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json', timeout=5).read().decode())
    arena_tab = next((t for t in tabs if 'arena.ai' in t.get('url', '')), None)
    if not arena_tab:
        print('No Arena tab found')
        return

    async with websockets.connect(arena_tab['webSocketDebuggerUrl']) as ws:
        expr = """
        (() => {
            const inputEl = document.querySelector('.tiptap.ProseMirror');
            const txt = inputEl ? inputEl.innerText.trim() : '';
            const sendBtn = document.querySelector('button[aria-label="Send message"], button[aria-label*="Send"]');
            const btns = Array.from(document.querySelectorAll('button'));
            const stopBtn = btns.find(b => b.getAttribute('aria-label') && b.getAttribute('aria-label').includes('Stop'));
            const isGen = !!stopBtn || document.body.innerText.includes('Thinking...') || document.body.innerText.includes('Stop generating');
            return {
                inputTextLength: txt.length,
                inputSnippet: txt.slice(0, 80),
                hasSendBtn: !!sendBtn,
                sendBtnDisabled: sendBtn ? sendBtn.disabled : null,
                isGenerating: isGen,
                totalPageTextLength: document.body.innerText.length
            };
        })()
        """
        await ws.send(json.dumps({'id': 1001, 'method': 'Runtime.evaluate', 'params': {'expression': expr, 'returnByValue': True}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 1001:
                val = msg.get('result', {}).get('result', {}).get('value')
                print('Arena Probe Result:', json.dumps(val, indent=2))
                break

if __name__ == '__main__':
    asyncio.run(check())
