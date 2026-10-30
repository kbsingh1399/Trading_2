import asyncio
import json
import urllib.request
import websockets

async def inspect():
    raw = urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=5).read().decode("utf-8")
    tabs = json.loads(raw)
    ws_url = None
    for t in tabs:
        if "arena" in t.get("url", "").lower():
            ws_url = t.get("webSocketDebuggerUrl")
            break
    if not ws_url:
        print("No Arena tab")
        return
    async with websockets.connect(ws_url, max_size=10*1024*1024) as ws:
        expr = """
        (() => {
            const msgs = Array.from(document.querySelectorAll('[data-message-author-role], .prose, div[class*="message"]')).map(e => ({
                tag: e.tagName,
                role: e.getAttribute('data-message-author-role') || 'none',
                cls: e.className,
                len: (e.innerText || '').length,
                preview: (e.innerText || '').slice(0, 100).replace(/\\n/g, ' ')
            }));
            const buttons = Array.from(document.querySelectorAll('button')).map(b => ({
                aria: b.getAttribute('aria-label'),
                text: (b.innerText || '').trim(),
                cls: b.className
            })).filter(b => b.aria || b.text);
            return { msgs: msgs.slice(-10), buttons: buttons.slice(-15) };
        })()
        """
        msg = {"id": 1, "method": "Runtime.evaluate", "params": {"expression": expr, "returnByValue": True}}
        await ws.send(json.dumps(msg))
        res = json.loads(await ws.recv())
        val = res.get("result", {}).get("result", {}).get("value")
        print(json.dumps(val, indent=2))

if __name__ == "__main__":
    asyncio.run(inspect())
