import asyncio
import json
import urllib.request
import websockets

async def nav():
    raw = urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=5).read().decode("utf-8")
    tabs = json.loads(raw)
    zai = next((t for t in tabs if "chat.z.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)
    if not zai:
        print("No Z.ai tab found")
        return
    async with websockets.connect(zai["webSocketDebuggerUrl"], max_size=50_000_000) as ws:
        target_url = "https://chat.z.ai/c/5a4ce502-bd77-4f90-b188-414142f93ed4"
        await ws.send(json.dumps({"id": 1, "method": "Page.navigate", "params": {"url": target_url}}))
        resp = await ws.recv()
        print("Navigated:", resp)
        await asyncio.sleep(4)
        
        # Check title and content
        js = "(() => ({ title: document.title, url: window.location.href, bodyLen: document.body.innerText.length }))()"
        await ws.send(json.dumps({"id": 2, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
        resp2 = json.loads(await ws.recv())
        print("Status after nav:", resp2.get("result", {}).get("result", {}).get("value"))

if __name__ == "__main__":
    asyncio.run(nav())
