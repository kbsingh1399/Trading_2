import asyncio
import json
import urllib.request
import websockets

async def check():
    raw = urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=5).read().decode("utf-8")
    tabs = json.loads(raw)
    ws_url = None
    for t in tabs:
        if "z.ai" in t.get("url", "").lower() or "chat.z.ai" in t.get("url", "").lower():
            ws_url = t.get("webSocketDebuggerUrl")
            break
    if not ws_url:
        print("No Z.ai tab found")
        return
    async with websockets.connect(ws_url, max_size=10*1024*1024) as ws:
        expr = """
        (() => {
            const stopBtn = document.querySelector('button span.block.size-3.rounded-xs.bg-text-inverted, button[aria-label*="Stop"]');
            const allChatMsgs = Array.from(document.querySelectorAll('.chat-assistant.markdown-prose, .markdown-prose'));
            const lastMsg = allChatMsgs.length > 0 ? allChatMsgs[allChatMsgs.length - 1].innerText : '';
            return {
                hasStop: !!stopBtn,
                msgCount: allChatMsgs.length,
                lastMsgLen: lastMsg.length,
                lastMsgPreview: lastMsg.slice(0, 200).replace(/\\n/g, ' ')
            };
        })()
        """
        msg = {"id": 1, "method": "Runtime.evaluate", "params": {"expression": expr, "returnByValue": True}}
        await ws.send(json.dumps(msg))
        res = json.loads(await ws.recv())
        print(json.dumps(res.get("result", {}).get("result", {}).get("value"), indent=2))

if __name__ == "__main__":
    asyncio.run(check())
