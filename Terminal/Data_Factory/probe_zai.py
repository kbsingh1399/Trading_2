#!/usr/bin/env python3
import asyncio
import json
import pathlib
import sys
import websockets
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
ZAI_RAW_FILE = ROOT / "docs" / "trade_plans" / "ZAI_LATEST_RAW.md"
ZAI_STATUS_FILE = ROOT / "Data" / "zai_completion_status.json"

async def main():
    try:
        raw = urllib.request.urlopen("http://localhost:9222/json", timeout=5).read().decode("utf-8")
        tabs = json.loads(raw)
        ws_url = None
        for t in tabs:
            if "chat.z.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl"):
                ws_url = t["webSocketDebuggerUrl"]
                break
        
        if not ws_url:
            print("[probe_zai] Z.ai tab not found on CDP!")
            return

        async with websockets.connect(ws_url, open_timeout=5) as ws:
            # Activate tab
            await ws.send(json.dumps({"id": 1, "method": "Page.bringToFront"}))
            await ws.recv()
            
            js = """
            (() => {
                const stopBtn = document.querySelector('button[aria-label*="Stop"], button[title*="Stop"], button.stop-button');
                const msgs = document.querySelectorAll('.chat-assistant.markdown-prose');
                const last = msgs.length > 0 ? msgs[msgs.length - 1] : null;
                const txt = last ? (last.innerText || '').trim() : '';
                return {
                    isGenerating: Boolean(stopBtn),
                    count: msgs.length,
                    len: txt.length,
                    text: txt
                };
            })()
            """
            await ws.send(json.dumps({"id": 2, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
            resp = await asyncio.wait_for(ws.recv(), timeout=5)
            val = json.loads(resp).get("result", {}).get("result", {}).get("value", {})
            print(f"[probe_zai] isGenerating: {val.get('isGenerating')}, count: {val.get('count')}, len: {val.get('len')}")
            
            if val.get("len", 0) > 0 and not val.get("isGenerating"):
                ZAI_RAW_FILE.write_text(val["text"], encoding="utf-8")
                status = {
                    "completed_at_utc": "2026-10-25 02:14:00 UTC",
                    "text_length": val.get("len", 0),
                    "is_generating": False
                }
                ZAI_STATUS_FILE.write_text(json.dumps(status, indent=2), encoding="utf-8")
                print(f"[probe_zai] Saved {val.get('len')} chars to {ZAI_RAW_FILE}")
    except Exception as e:
        print(f"[probe_zai] Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
