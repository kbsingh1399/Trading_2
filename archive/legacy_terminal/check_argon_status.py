import json
import urllib.request
import asyncio
import websockets

async def check():
    pages = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json").read().decode())
    target = next((p for p in pages if "gemini.google.com" in p.get("url", "")), None)
    async with websockets.connect(target["webSocketDebuggerUrl"]) as ws:
        js = """
        (() => {
            const msgs = Array.from(document.querySelectorAll('.message-content, .model-response-text, [data-test-id="response-container"], message-content'));
            const isGenerating = !!document.querySelector('.stop-generating-button, [aria-label*="Stop" i], mat-progress-bar');
            const editorVal = document.querySelector('.ql-editor')?.innerText?.slice(0, 100) || '';
            return {
                isGenerating,
                editorVal,
                totalResponses: msgs.length,
                lastMsgSnippet: msgs.pop()?.innerText?.slice(0, 300) || ''
            };
        })()
        """
        await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
        resp = json.loads(await ws.recv())
        print(json.dumps(resp.get("result", {}).get("result", {}).get("value"), indent=2))

asyncio.run(check())
