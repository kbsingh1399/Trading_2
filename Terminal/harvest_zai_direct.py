import asyncio
import json
import pathlib
import urllib.request
import websockets

ROOT = pathlib.Path(__file__).resolve().parent.parent

async def harvest():
    try:
        tabs = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=5).read().decode())
        z = next((t for t in tabs if t.get("url", "").startswith("https://chat.z.ai")), None)
        if not z:
            print("No chat.z.ai tab found")
            return
            
        async with websockets.connect(z["webSocketDebuggerUrl"], max_size=20_000_000) as ws:
            js = """
            (() => {
                const assistants = Array.from(document.querySelectorAll('.chat-assistant, .markdown-prose, div[class*="message-"]'));
                if (assistants.length > 0) {
                    return assistants[assistants.length - 1].innerText || '';
                }
                const allMarkdown = Array.from(document.querySelectorAll('.markdown-prose, .markdown-body, div[class*="markdown"]'));
                if (allMarkdown.length > 0) {
                    allMarkdown.sort((a, b) => (b.innerText || '').length - (a.innerText || '').length);
                    return allMarkdown[0].innerText || '';
                }
                return document.body.innerText || '';
            })()
            """
            await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
            res = json.loads(await ws.recv())
            txt = res.get("result", {}).get("result", {}).get("value", "")
            if len(txt) > 200:
                out = ROOT / "docs" / "trade_plans" / "ZAI_LATEST_RAW.md"
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text(txt, encoding="utf-8")
                print(f"Harvested {len(txt)} chars to {out}")
            else:
                print(f"Text too short ({len(txt)} chars)")
    except Exception as e:
        print(f"Error harvesting: {e}")

if __name__ == "__main__":
    asyncio.run(harvest())
