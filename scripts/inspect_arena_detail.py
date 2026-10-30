import asyncio
import json
import urllib.request
import websockets

async def check():
    raw = urllib.request.urlopen("http://127.0.0.1:9222/json").read().decode("utf-8")
    tabs = json.loads(raw)
    arena_tab = next((t for t in tabs if "arena.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)
    if not arena_tab:
        print("No arena tab")
        return
    async with websockets.connect(arena_tab["webSocketDebuggerUrl"]) as ws:
        js = """(() => {
            const stopBtn = document.querySelector('button[aria-label*="Stop" i], button[title*="Stop" i], button.stop, [data-testid="stop-button"]');
            const prose = Array.from(document.querySelectorAll('.prose, [data-message-author-role="assistant"]'));
            const msgs = Array.from(document.querySelectorAll('[class*="message"]'));
            const textarea = document.querySelector('textarea, [contenteditable="true"]');
            const body = document.body ? document.body.innerText.slice(-1500) : '';
            return {
                url: window.location.href,
                hasStopBtn: Boolean(stopBtn),
                proseCount: prose.length,
                msgsCount: msgs.length,
                textareaVal: textarea ? (textarea.value || textarea.innerText || '').slice(0, 200) : 'None',
                lastBodySnippet: body
            };
        })()"""
        await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
        res = json.loads(await ws.recv())
        print(json.dumps(res.get("result", {}).get("result", {}).get("value"), indent=2))

if __name__ == "__main__":
    asyncio.run(check())
