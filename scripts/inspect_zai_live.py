import asyncio
import json
import websockets

async def inspect():
    ws_url = 'ws://127.0.0.1:9222/devtools/page/D059AE2A850B0EAC7734A3F6B8471786'
    async with websockets.connect(ws_url) as ws:
        js = """(() => {
            const msgs = Array.from(document.querySelectorAll('.message, [class*="message"], [data-message-author-role]'));
            const lastMsg = msgs.length ? msgs[msgs.length - 1].innerText : '';
            const textarea = document.querySelector('textarea, div[contenteditable="true"]');
            const textareaVal = textarea ? (textarea.value || textarea.innerText || '') : '';
            const sendBtn = document.querySelector('button[aria-label*="Send"], button[type="submit"], button.send, button[data-testid*="send"]');
            const stopBtn = document.querySelector('button[aria-label*="Stop"], button.stop, [data-testid*="stop"]');
            const modals = Array.from(document.querySelectorAll('[role="dialog"], .modal, [class*="modal"], [class*="popup"]')).map(m => m.innerText.slice(0, 100));
            return {
                messageCount: msgs.length,
                lastMessagePreview: lastMsg.slice(0, 300),
                textareaLength: textareaVal.length,
                textareaSnippet: textareaVal.slice(0, 200),
                hasSendButton: sendBtn !== null,
                sendButtonDisabled: sendBtn ? sendBtn.disabled : null,
                hasStopButton: stopBtn !== null,
                modals: modals
            };
        })()"""
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        resp = json.loads(await ws.recv())
        print(json.dumps(resp.get('result', {}).get('result', {}).get('value'), indent=2))

asyncio.run(inspect())
