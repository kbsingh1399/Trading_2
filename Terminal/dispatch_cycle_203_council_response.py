#!/usr/bin/env python3
"""
Terminal/dispatch_cycle_203_council_response.py
===============================================
Dispatches docs/prompts/ARENA_CYCLE_203_COUNCIL_RESPONSE.md to the active Arena.ai tab
via Edge/Chrome CDP port 9222 using native CDP Input.insertText and submit button click.
"""

import asyncio
import json
import pathlib
import sys
import time
import urllib.request
import websockets

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROMPT_FILE = ROOT / "docs" / "prompts" / "ARENA_CYCLE_203_COUNCIL_RESPONSE.md"


async def main():
    if not PROMPT_FILE.exists():
        print(f"[-] Prompt file not found: {PROMPT_FILE}")
        return False

    prompt_body = PROMPT_FILE.read_text(encoding="utf-8").strip()
    print(f"[*] Prepared Council Clarification Prompt ({len(prompt_body)} characters)...")

    try:
        tabs = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=5).read().decode())
    except Exception as e:
        print(f"[-] Could not connect to Edge CDP: {e}")
        return False

    arena_tab = None
    for t in tabs:
        u = t.get("url", "")
        if "arena.ai" in u:
            arena_tab = t
            break

    if not arena_tab:
        print("[-] Arena.ai tab not found on port 9222!")
        return False

    ws_url = arena_tab.get("webSocketDebuggerUrl")
    print(f"[+] Found Arena tab: {arena_tab.get('title')} (ID: {arena_tab.get('id')})")
    print(f"[+] URL: {arena_tab.get('url')}")

    async with websockets.connect(ws_url, max_size=25_000_000) as ws:
        cur_id = 100

        async def send_cmd(method: str, params: dict = None):
            nonlocal cur_id
            cur_id += 1
            payload = {"id": cur_id, "method": method}
            if params:
                payload["params"] = params
            await ws.send(json.dumps(payload))
            while True:
                raw = await asyncio.wait_for(ws.recv(), timeout=5.0)
                msg = json.loads(raw)
                if msg.get("id") == cur_id:
                    return msg

        # 1. Bring page to front
        await send_cmd("Page.bringToFront")
        await asyncio.sleep(0.3)

        # 2. Focus editor and clear existing text
        await send_cmd("Runtime.evaluate", {
            "expression": "document.querySelector('.tiptap.ProseMirror').focus()"
        })
        await asyncio.sleep(0.2)

        # Ctrl+A
        await send_cmd("Input.dispatchKeyEvent", {
            "type": "rawKeyDown", "windowsVirtualKeyCode": 65, "code": "KeyA", "key": "a", "modifiers": 2
        })
        await send_cmd("Input.dispatchKeyEvent", {
            "type": "keyUp", "windowsVirtualKeyCode": 65, "code": "KeyA", "key": "a"
        })
        await asyncio.sleep(0.1)

        # Backspace / Delete
        await send_cmd("Input.dispatchKeyEvent", {
            "type": "rawKeyDown", "windowsVirtualKeyCode": 8, "code": "Backspace", "key": "Backspace"
        })
        await send_cmd("Input.dispatchKeyEvent", {
            "type": "keyUp", "windowsVirtualKeyCode": 8, "code": "Backspace", "key": "Backspace"
        })
        await asyncio.sleep(0.2)

        # 3. Insert prompt text in chunks to prevent protocol buffer overrun
        chunk_size = 2000
        for i in range(0, len(prompt_body), chunk_size):
            chunk = prompt_body[i:i + chunk_size]
            await send_cmd("Input.insertText", {"text": chunk})
            await asyncio.sleep(0.05)

        await asyncio.sleep(0.3)

        # 4. Check submit button readiness
        check_res = await send_cmd("Runtime.evaluate", {
            "expression": """(() => {
                const submitBtn = document.querySelector('button[aria-label="Send message"], button[type="submit"]');
                return {
                    found: submitBtn !== null,
                    disabled: submitBtn ? submitBtn.disabled : null
                };
            })()""",
            "returnByValue": True
        })
        btn_state = check_res.get("result", {}).get("result", {}).get("value", {})
        print(f"[+] Submit button state: {btn_state}")

        # 5. Click submit button
        submit_res = await send_cmd("Runtime.evaluate", {
            "expression": """(() => {
                const submitBtn = document.querySelector('button[aria-label="Send message"], button[type="submit"]');
                if (submitBtn && !submitBtn.disabled) {
                    submitBtn.click();
                    return { clicked: true };
                }
                return { clicked: false, reason: submitBtn ? 'disabled' : 'not_found' };
            })()""",
            "returnByValue": True
        })
        click_state = submit_res.get("result", {}).get("result", {}).get("value", {})
        print(f"[+] Submit click result: {click_state}")

        # 6. Verify generation triggered
        await asyncio.sleep(1.0)
        gen_res = await send_cmd("Runtime.evaluate", {
            "expression": """(() => {
                const stopBtn = document.querySelector('button[aria-label="Stop"], button[aria-label="Stop generating"]');
                const isSpinning = document.querySelector('svg.animate-spin') !== null;
                return { is_generating: (stopBtn !== null || isSpinning) };
            })()""",
            "returnByValue": True
        })
        gen_state = gen_res.get("result", {}).get("result", {}).get("value", {})
        print(f"[+] Arena Generation Status: {gen_state}")
        return gen_state.get("is_generating", False) or click_state.get("clicked", False)


if __name__ == "__main__":
    asyncio.run(main())
