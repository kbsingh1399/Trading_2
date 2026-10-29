"""
Terminal/dispatch_test_message.py
Dispatches a short, distinct test message with a unique CYCLE_ID to BOTH Arena.ai and Z.ai via Chrome CDP.
"""

import argparse
import asyncio
import datetime
import json
import pathlib
import subprocess
import sys
import urllib.request
import websockets

ROOT = pathlib.Path(__file__).resolve().parents[1]
CDP_URL = "http://127.0.0.1:9222/json"
ZAI_DISPATCHER = ROOT / "Terminal" / "dispatch_zai_prompt.py"


def build_test_prompt(cycle_id: str) -> str:
    utc_now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    prompt = f"""### DUAL COUNCIL HARD-SYNC VERIFICATION TEST - [CYCLE_ID: {cycle_id}]
Timestamp: {utc_now}

You are part of the Sovereign Dual-Council automated synchronization test harness.
Please respond directly with this exact verification block:

[VERIFICATION RECEIPT - CYCLE_ID: {cycle_id}]
- Status: OPERATIONAL_CONFIRMED
- Council Model: Verified
- Timestamp: {utc_now}
- Message: Synchronization handshake successful.
[END OF RECEIPT]
"""
    return prompt


async def dispatch_to_arena(prompt: str) -> bool:
    try:
        tabs = json.loads(urllib.request.urlopen(CDP_URL, timeout=5).read().decode())
        arena_ws = None
        for t in tabs:
            if ("arena.ai/agent" in t.get("url", "") or "arena.ai" in t.get("url", "")) and t.get("webSocketDebuggerUrl"):
                arena_ws = t["webSocketDebuggerUrl"]
                break
        if not arena_ws:
            print("[DispatchTest] Error: Arena.ai tab not found on CDP port 9222.")
            return False

        async with websockets.connect(arena_ws, max_size=50_000_000) as ws:
            # 1. Bring to front
            await ws.send(json.dumps({"id": 101, "method": "Page.bringToFront"}))
            await asyncio.sleep(0.5)

            # 2. Dismiss modal/escape
            await ws.send(json.dumps({"id": 102, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 27, "code": "Escape", "key": "Escape"}}))
            await ws.send(json.dumps({"id": 103, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 27, "code": "Escape", "key": "Escape"}}))
            await asyncio.sleep(0.2)

            # 3. Dismiss 'Was this task successful?' banner if active
            js_dismiss_banner = """(() => {
                const btns = Array.from(document.querySelectorAll('button')).filter(b => b.innerText.trim() === 'Yes' || b.innerText.trim() === 'No');
                if (btns.length > 0) {
                    const yesBtn = btns.find(b => b.innerText.trim() === 'Yes') || btns[0];
                    yesBtn.click();
                    return true;
                }
                return false;
            })()"""
            await ws.send(json.dumps({"id": 1031, "method": "Runtime.evaluate", "params": {"expression": js_dismiss_banner}}))
            await asyncio.sleep(0.5)

            # 4. Clear ProseMirror
            js_clear = """(() => {
                const el = document.querySelector('.tiptap.ProseMirror');
                if (!el) return false;
                el.focus();
                const range = document.createRange();
                range.selectNodeContents(el);
                const sel = window.getSelection();
                sel.removeAllRanges();
                sel.addRange(range);
                return true;
            })()"""
            await ws.send(json.dumps({"id": 104, "method": "Runtime.evaluate", "params": {"expression": js_clear}}))
            await asyncio.sleep(0.1)
            await ws.send(json.dumps({"id": 105, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 8, "code": "Backspace", "key": "Backspace"}}))
            await ws.send(json.dumps({"id": 106, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 8, "code": "Backspace", "key": "Backspace"}}))
            await asyncio.sleep(0.2)

            # 5. Insert text
            chunk_size = 2000
            for idx in range(0, len(prompt), chunk_size):
                chunk = prompt[idx:idx + chunk_size]
                await ws.send(json.dumps({"id": 107, "method": "Input.insertText", "params": {"text": chunk}}))
                await asyncio.sleep(0.04)
            await asyncio.sleep(0.5)

            # 6. Click send
            js_click = """(() => {
                const sendBtn = document.querySelector('button[aria-label="Send message"], button:has(svg.lucide-arrow-up), button[type="submit"], button[aria-label*="Send"]');
                if (sendBtn && !sendBtn.disabled) {
                    sendBtn.click();
                    return { clicked: true };
                }
                return { clicked: false, disabled: sendBtn ? sendBtn.disabled : null };
            })()"""
            await ws.send(json.dumps({"id": 108, "method": "Runtime.evaluate", "params": {"expression": js_click, "returnByValue": True}}))
            res = json.loads(await ws.recv())
            click_val = res.get("result", {}).get("result", {}).get("value", {})
            print(f"[DispatchTest] Arena.ai send result: {click_val}")
            if not click_val.get("clicked"):
                # Fallback to Enter key
                await ws.send(json.dumps({"id": 109, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"}}))
                await ws.send(json.dumps({"id": 110, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"}}))
            return True
    except Exception as e:
        print(f"[DispatchTest] Arena.ai error: {e}")
        return False


def dispatch_to_zai(prompt: str) -> bool:
    try:
        proc = subprocess.run(
            [sys.executable, str(ZAI_DISPATCHER), "--text", prompt],
            capture_output=True,
            text=True,
            timeout=30
        )
        print(f"[DispatchTest] Z.ai output: {proc.stdout.strip()}")
        if proc.stderr:
            print(f"[DispatchTest] Z.ai stderr: {proc.stderr.strip()}")
        return proc.returncode == 0
    except Exception as e:
        print(f"[DispatchTest] Z.ai error: {e}")
        return False


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cycle", required=True, help="Unique cycle ID")
    args = parser.parse_args()

    prompt = build_test_prompt(args.cycle)
    test_file = ROOT / "docs" / "trade_plans" / f"TEST_PROMPT_{args.cycle}.txt"
    test_file.parent.mkdir(parents=True, exist_ok=True)
    test_file.write_text(prompt, encoding="utf-8")
    print(f"[DispatchTest] Generated test prompt for {args.cycle} ({len(prompt)} chars)")

    # 1. Dispatch to Z.ai
    print(f"[DispatchTest] Sending prompt to Z.ai for cycle {args.cycle}...")
    z_ok = dispatch_to_zai(prompt)

    # 2. Dispatch to Arena.ai
    print(f"[DispatchTest] Sending prompt to Arena.ai for cycle {args.cycle}...")
    a_ok = await dispatch_to_arena(prompt)

    print(f"[DispatchTest] Dispatch summary: Z.ai={z_ok}, Arena={a_ok}")


if __name__ == "__main__":
    asyncio.run(main())
