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

        # 3. Focus and clear chat-input
        js_clear = """(() => {
            const el = document.getElementById("chat-input");
            if (!el) return false;
            el.focus();
            el.value = "";
            el.dispatchEvent(new Event('input', { bubbles: true }));
            el.dispatchEvent(new Event('change', { bubbles: true }));
            return true;
        })()"""
        await ws.send(json.dumps({"id": 3, "method": "Runtime.evaluate", "params": {"expression": js_clear}}))
        await ws.recv()
        await asyncio.sleep(0.3)

        # 4. Set value via prototype descriptor and fire events
        js_set = f"""(() => {{
            const el = document.getElementById("chat-input");
            if (!el) return {{ success: false, err: "no el" }};
            el.focus();
            const proto = Object.getPrototypeOf(el);
            const desc = Object.getOwnPropertyDescriptor(proto, 'value') || Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value');
            if (desc && desc.set) {{
                desc.set.call(el, {json.dumps(prompt_text)});
            }} else {{
                el.value = {json.dumps(prompt_text)};
            }}
            el.dispatchEvent(new Event('input', {{ bubbles: true }}));
            el.dispatchEvent(new Event('change', {{ bubbles: true }}));
            const btn = document.getElementById("send-message-button");
            return {{
                success: true,
                len: el.value.length,
                btnDisabled: btn ? btn.disabled : null
            }};
        }})()"""
        await ws.send(json.dumps({"id": 4, "method": "Runtime.evaluate", "params": {"expression": js_set, "returnByValue": True}}))
        res4 = json.loads(await ws.recv())
        val4 = res4.get("result", {}).get("result", {}).get("value", {})
        print(f"[ZaiDispatcher] Set text result: {val4}", flush=True)
        await asyncio.sleep(0.4)

        # 5. If button still disabled, force Svelte reactive update via synthetic key input
        if val4.get("btnDisabled"):
            await ws.send(json.dumps({"id": 5, "method": "Input.insertText", "params": {"text": " "}}))
            await ws.recv()
            await asyncio.sleep(0.2)
            await ws.send(json.dumps({"id": 6, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 8, "code": "Backspace", "key": "Backspace"}}))
            await ws.recv()
            await ws.send(json.dumps({"id": 7, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 8, "code": "Backspace", "key": "Backspace"}}))
            await ws.recv()
            await asyncio.sleep(0.4)

        # 6. Click Send button or trigger requestSubmit
        js_click = """(() => {
            const btn = document.getElementById("send-message-button") || document.querySelector('button#send-message-button, button[aria-label*="Send"]');
            const form = document.querySelector('form');
            if (btn && !btn.disabled) {
                btn.click();
                return { clicked: true, method: "button_click" };
            }
            if (form && form.requestSubmit) {
                form.requestSubmit();
                return { clicked: true, method: "requestSubmit" };
            }
            return { clicked: false, btnDisabled: btn ? btn.disabled : null };
        })()"""
        await ws.send(json.dumps({"id": 8, "method": "Runtime.evaluate", "params": {"expression": js_click, "returnByValue": True}}))
        res8 = json.loads(await ws.recv())
        val8 = res8.get("result", {}).get("result", {}).get("value", {})
        print(f"[ZaiDispatcher] Click result: {val8}", flush=True)

        if not val8.get("clicked"):
            print("[ZaiDispatcher] Fallback to Enter key...", flush=True)
            for ktype in ["rawKeyDown", "keyUp"]:
                await ws.send(json.dumps({"id": 9, "method": "Input.dispatchKeyEvent", "params": {"type": ktype, "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"}}))
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
