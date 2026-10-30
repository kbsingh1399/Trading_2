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
            const body = document.body.innerText;
            const cIdx = body.lastIndexOf('Cycle_031');
            return {
                url: window.location.href,
                bodyLength: body.length,
                hasCycle031: body.includes('Cycle_031'),
                last500Chars: body.slice(-500),
                fromCycle031: cIdx !== -1 ? body.substring(cIdx, cIdx + 500) : ''
            };
        })()"""
        await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
        resp = json.loads(await ws.recv())
        val = resp.get("result", {}).get("result", {}).get("value", {})
        print(json.dumps(val, indent=2))

if __name__ == "__main__":
    asyncio.run(check())
