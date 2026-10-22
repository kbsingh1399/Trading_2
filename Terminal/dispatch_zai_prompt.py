"""
Terminal/dispatch_zai_prompt.py
Dispatches a prompt directly into Z.ai (GLM-5.3-Flash) via Chrome DevTools Protocol (CDP port 9222).

Usage:
  python Terminal/dispatch_zai_prompt.py --text "prompt text"
  python Terminal/dispatch_zai_prompt.py --file docs/trade_plans/LATEST_ARENA_PROMPT.txt
"""

import argparse
import asyncio
import json
import pathlib
import sys
import time
import urllib.request
import websockets

CDP_URL = "http://127.0.0.1:9222/json"

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def find_zai_tab() -> dict | None:
    try:
        raw = urllib.request.urlopen(CDP_URL, timeout=5).read().decode("utf-8")
        tabs = json.loads(raw)
        for t in tabs:
            if "chat.z.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl"):
                return t
    except Exception as e:
        print(f"[ZaiDispatcher] Error querying CDP tabs: {e}", file=sys.stderr)
        return None
    return None


async def post_prompt_to_zai(prompt_text: str) -> bool:
    tab = find_zai_tab()
    if not tab:
        print("[ZaiDispatcher] Error: No active Z.ai tab found on CDP port 9222.", file=sys.stderr)
        return False

    ws_url = tab.get("webSocketDebuggerUrl")
    if not ws_url:
        print("[ZaiDispatcher] Error: No WebSocket URL for Z.ai tab.", file=sys.stderr)
        return False

    async with websockets.connect(ws_url, max_size=50_000_000) as ws:
        # 1. Bring tab to front
        await ws.send(json.dumps({"id": 1, "method": "Page.bringToFront"}))
        try:
            await asyncio.wait_for(ws.recv(), timeout=2.0)
        except Exception:
            pass
        await asyncio.sleep(0.5)

        # 2. Check if currently generating
        js_check = """(() => {
            const stopBtn = document.querySelector('button[aria-label*="Stop"], button[title*="Stop"], button.stop-button');
            const stopSquare = document.querySelector('button span.size-3.rounded-xs');
            return Boolean(stopBtn) || Boolean(stopSquare);
        })()"""
        await ws.send(json.dumps({"id": 2, "method": "Runtime.evaluate", "params": {"expression": js_check, "returnByValue": True}}))
        resp = json.loads(await ws.recv())
        is_gen = resp.get("result", {}).get("result", {}).get("value", False)
        if is_gen:
            print("[ZaiDispatcher] Warning: Z.ai is currently generating a response. Aborting dispatch.", file=sys.stderr)
            return False

        # 3. Focus textarea#chat-input and set value
        js_insert = """(text) => {
            const ta = document.querySelector('textarea#chat-input, textarea');
            if (!ta) return false;
            ta.focus();
            ta.value = text;
            ta.dispatchEvent(new Event('input', { bubbles: true }));
            ta.dispatchEvent(new Event('change', { bubbles: true }));
            return true;
        }"""
        await ws.send(json.dumps({
            "id": 3,
            "method": "Runtime.callFunctionOn",
            "params": {
                "functionDeclaration": js_insert,
                "arguments": [{"value": prompt_text}],
                "executionContextId": None,
                "returnByValue": True,
                "userGesture": True
            }
        }))
        resp = json.loads(await ws.recv())
        inserted = resp.get("result", {}).get("result", {}).get("value", False)

        if not inserted:
            print("[ZaiDispatcher] Falling back to direct focus and input event...", flush=True)
            await ws.send(json.dumps({
                "id": 4,
                "method": "Runtime.evaluate",
                "params": {"expression": "(() => { const ta = document.querySelector('textarea#chat-input, textarea'); if(ta) { ta.focus(); return true; } return false; })()", "returnByValue": True}
            }))
            await ws.recv()
            await ws.send(json.dumps({"id": 5, "method": "Input.insertText", "params": {"text": prompt_text}}))
            await ws.recv()

        await asyncio.sleep(0.5)

        # 4. Click Send button or send Enter
        js_send = """(() => {
            const btn = document.querySelector('button#send-message-button, button[aria-label*="Send"], button[title*="Send"]');
            if (btn && !btn.disabled) {
                btn.click();
                return true;
            }
            return false;
        })()"""
        await ws.send(json.dumps({
            "id": 6,
            "method": "Runtime.evaluate",
            "params": {"expression": js_send, "returnByValue": True}
        }))
        resp = json.loads(await ws.recv())
        clicked = resp.get("result", {}).get("result", {}).get("value", False)

        if not clicked:
            print("[ZaiDispatcher] Send button disabled or not clicked, dispatching Enter key...", flush=True)
            for ktype, vk in [("rawKeyDown", 13), ("keyUp", 13)]:
                await ws.send(json.dumps({
                    "id": 7,
                    "method": "Input.dispatchKeyEvent",
                    "params": {"type": ktype, "windowsVirtualKeyCode": vk, "code": "Enter", "key": "Enter"}
                }))
                await ws.recv()

        await asyncio.sleep(1.0)
        print(f"[ZaiDispatcher] Successfully dispatched prompt to Z.ai ({len(prompt_text)} chars)!")
        return True


def main():
    parser = argparse.ArgumentParser(description="Dispatch Prompt to Z.ai via Chrome CDP")
    parser.add_argument("--text", type=str, help="Prompt text string")
    parser.add_argument("--file", type=str, help="Path to prompt text file")
    args = parser.parse_args()

    if args.file:
        p = pathlib.Path(args.file)
        if not p.exists():
            print(f"File not found: {p}", file=sys.stderr)
            sys.exit(1)
        text = p.read_text(encoding="utf-8")
    elif args.text:
        text = args.text
    else:
        print("Must specify --text or --file", file=sys.stderr)
        sys.exit(1)

    ok = asyncio.run(post_prompt_to_zai(text))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
