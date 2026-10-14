import json
import urllib.request
import asyncio
import websockets
import time
from pathlib import Path

CDP_HTTP_URL = "http://127.0.0.1:9222"
RAW_FILE = Path("docs/trade_plans/ARGON_LATEST_RAW.md")

async def wait_for_argon():
    print("[ArgonWatcher] Listening for Google Gemini Argon completion in Chrome CDP...", flush=True)
    req = urllib.request.urlopen(f"{CDP_HTTP_URL}/json")
    pages = json.loads(req.read().decode())
    target = next((p for p in pages if "gemini.google.com" in p.get("url", "")), None)
    if not target:
        print("[ArgonWatcher] Gemini tab not found!", flush=True)
        return 1

    ws_url = target.get("webSocketDebuggerUrl")
    
    # Wait until generation finishes
    stable_count = 0
    last_len = 0
    
    while True:
        try:
            async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
                js_probe = """
                (() => {
                    const isGen = !!document.querySelector('.stop-generating-button, [aria-label*="Stop" i], mat-progress-bar');
                    const msgs = Array.from(document.querySelectorAll('.message-content, .model-response-text, [data-test-id="response-container"], message-content'));
                    const lastMsg = msgs.length ? msgs[msgs.length - 1].innerText : '';
                    return {
                        isGen,
                        totalMsgs: msgs.length,
                        lastLen: lastMsg.length,
                        snippet: lastMsg.slice(-200)
                    };
                })()
                """
                await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js_probe, "returnByValue": True}}))
                resp = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value", {})
                
                is_gen = resp.get("isGen", False)
                curr_len = resp.get("lastLen", 0)
                
                if is_gen:
                    print(f"[ArgonWatcher] Argon computing... length: {curr_len} chars", flush=True)
                    stable_count = 0
                else:
                    if curr_len > 1000 and curr_len == last_len:
                        stable_count += 1
                        print(f"[ArgonWatcher] Stable check {stable_count}/2 (len={curr_len})", flush=True)
                        if stable_count >= 2:
                            # Harvest full text
                            js_harvest = """
                            (() => {
                                const msgs = Array.from(document.querySelectorAll('.message-content, .model-response-text, [data-test-id="response-container"], message-content'));
                                return msgs.map(m => m.innerText).join('\\n\\n==================== NEXT TURN ====================\\n\\n');
                            })()
                            """
                            await ws.send(json.dumps({"id": 2, "method": "Runtime.evaluate", "params": {"expression": js_harvest, "returnByValue": True}}))
                            full_text = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value", "")
                            
                            RAW_FILE.parent.mkdir(parents=True, exist_ok=True)
                            RAW_FILE.write_text(full_text, encoding="utf-8")
                            print(f"\n🔔 GOOGLE GEMINI ARGON GENERATION COMPLETE ({len(full_text)} chars) -> Saved to {RAW_FILE.name}!", flush=True)
                            return 0
                    elif curr_len > 1000:
                        last_len = curr_len
                        stable_count = 0
        except Exception as e:
            print(f"[ArgonWatcher] Connection retry: {e}", flush=True)
            
        await asyncio.sleep(4.0)

if __name__ == "__main__":
    asyncio.run(wait_for_argon())
