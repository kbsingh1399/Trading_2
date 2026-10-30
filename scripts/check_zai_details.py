import asyncio
import json
import urllib.request
import websockets

async def check():
    raw = urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=5).read().decode("utf-8")
    tabs = json.loads(raw)
    zai = next((t for t in tabs if "chat.z.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)
    if not zai:
        print("No Z.ai tab found")
        return
    async with websockets.connect(zai["webSocketDebuggerUrl"], max_size=50_000_000) as ws:
        js = """(() => {
            const stopBtn = document.querySelector('button[aria-label*="Stop"], button[title*="Stop"], button.stop-button, button:has(span.size-3.rounded-xs)');
            const sendBtn = document.querySelector('button#send-message-button, button[aria-label="Send"], button[aria-label*="Send"], button[type="submit"]');
            const chatInput = document.getElementById('chat-input');
            const messages = Array.from(document.querySelectorAll('.chat-assistant, .chat-user, div.prose'));
            return {
                isGenerating: Boolean(stopBtn),
                sendBtnDisabled: sendBtn ? sendBtn.disabled : null,
                inputValLen: chatInput ? chatInput.value.length : 0,
                numMessages: messages.length,
                lastMsgSnippet: messages.length ? messages[messages.length - 1].innerText.slice(-200) : ''
            };
        })()"""
        await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
        resp = json.loads(await ws.recv())
        val = resp.get("result", {}).get("result", {}).get("value", {})
        print(json.dumps(val, indent=2))

if __name__ == "__main__":
    asyncio.run(check())
