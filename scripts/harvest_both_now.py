import asyncio
import json
import urllib.request
import websockets

async def harvest_both():
    raw = urllib.request.urlopen('http://127.0.0.1:9222/json', timeout=5).read()
    tabs = json.loads(raw)
    for t in tabs:
        url = t.get('url', '')
        ws = t.get('webSocketDebuggerUrl')
        if not ws:
            continue
        if 'arena.ai' in url:
            async with websockets.connect(ws, max_size=30*1024*1024) as client:
                js = '''(() => {
                    const msgs = document.querySelectorAll('.prose, [data-message-author-role="assistant"]');
                    if (msgs.length === 0) return '';
                    return msgs[msgs.length - 1].innerText;
                })()'''
                await client.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
                res = json.loads(await client.recv())
                arena_text = res.get('result', {}).get('result', {}).get('value', '')
                with open('docs/trade_plans/ARENA_LATEST_RAW.md', 'w', encoding='utf-8') as f:
                    f.write(arena_text)
                print(f'[Harvest] Arena.ai saved: {len(arena_text)} characters')

        elif 'chat.z.ai' in url or 'z.ai' in url:
            async with websockets.connect(ws, max_size=30*1024*1024) as client:
                # Extract text from latest message or preview or workspace
                js = '''(() => {
                    // Try to get artifact/preview content or last assistant message
                    const assistantMsgs = Array.from(document.querySelectorAll('[data-role="assistant"], .message-bubble, div[class*="message"]'));
                    let text = '';
                    if (assistantMsgs.length > 0) {
                        text = assistantMsgs[assistantMsgs.length - 1].innerText;
                    }
                    // Also check if there is an iframe or code block or preview modal
                    const preview = document.querySelector('.preview-content, .artifact-content, pre code');
                    let previewText = preview ? preview.innerText : '';
                    return {
                        msgText: text,
                        previewText: previewText
                    };
                })()'''
                await client.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
                res = json.loads(await client.recv())
                val = res.get('result', {}).get('result', {}).get('value', {})
                zai_text = val.get('previewText') or val.get('msgText') or ''
                with open('docs/trade_plans/ZAI_LATEST_RAW.md', 'w', encoding='utf-8') as f:
                    f.write(zai_text)
                print(f'[Harvest] Z.ai saved: {len(zai_text)} characters')

if __name__ == '__main__':
    asyncio.run(harvest_both())
