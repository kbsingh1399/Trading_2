import asyncio
import json
import urllib.request
import websockets

async def check():
    raw = urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=5).read().decode("utf-8")
    tabs = json.loads(raw)
    ws_url = None
    for t in tabs:
        if "arena" in t.get("url", "").lower():
            ws_url = t.get("webSocketDebuggerUrl")
            break
    if not ws_url:
        print("No Arena tab found")
        return
    async with websockets.connect(ws_url, max_size=10*1024*1024) as ws:
        expr = """
        (() => {
            const divs = Array.from(document.querySelectorAll('div')).filter(d => {
                const text = d.innerText || '';
                return text.includes('Active Skills Loaded') || text.includes('Mandatory Meta-Audit') || text.includes('Standardized Machine-Readable JSON');
            }).map(d => ({
                tag: d.tagName,
                cls: d.className,
                len: d.innerText.length,
                preview: d.innerText.slice(0, 150).replace(/\\n/g, ' ')
            }));
            return divs.slice(-10);
        })()
        """
        msg = {"id": 1, "method": "Runtime.evaluate", "params": {"expression": expr, "returnByValue": True}}
        await ws.send(json.dumps(msg))
        res = json.loads(await ws.recv())
        print(json.dumps(res.get("result", {}).get("result", {}).get("value"), indent=2))

if __name__ == "__main__":
    asyncio.run(check())
