"""
Terminal/dispatch_dual_council_prompt.py
Dispatches collaborative trading prompts to BOTH Chrome AI tabs:
  1. Arena.ai (Claude 3.7 / Fable Agentic mode)
  2. Z.ai (GLM-5.3-Flash Frontier Agent)
Extracts and harmonizes recommendations from both models for unified council deliberation.
"""
import asyncio
import json
import os
import pathlib
import sys
import time
import urllib.request
import websockets

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.arena_bridge import post_prompt_to_arena, get_arena_tab_ws_url
from Terminal.dispatch_comprehensive_wake_up_prompt import build_prompt


def get_chrome_tabs():
    try:
        with urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=5) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"Error fetching Chrome CDP tabs: {e}")
        return []


async def post_prompt_to_zai(prompt_text: str) -> bool:
    """Injects prompt into Z.ai's #chat-input textarea and clicks #send-message-button."""
    tabs = get_chrome_tabs()
    zai_tab = next((t for t in tabs if "chat.z.ai" in t.get("url", "")), None)
    if not zai_tab:
        print("Warning: Z.ai tab not found in Chrome.")
        return False

    ws_url = zai_tab.get("webSocketDebuggerUrl")
    if not ws_url:
        print("Warning: No WebSocket debugger URL for Z.ai tab.")
        return False

    try:
        async with websockets.connect(ws_url, max_size=20_000_000) as ws:
            # 1. Focus #chat-input
            await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": 'document.getElementById("chat-input").focus()'}}))
            await ws.recv()

            # 2. Clear any existing text (Ctrl+A then Backspace)
            await ws.send(json.dumps({"id": 2, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 65, "code": "KeyA", "key": "a", "modifiers": 2}}))
            await ws.recv()
            await ws.send(json.dumps({"id": 3, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 65, "code": "KeyA", "key": "a", "modifiers": 2}}))
            await ws.recv()
            await ws.send(json.dumps({"id": 4, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 8, "code": "Backspace", "key": "Backspace"}}))
            await ws.recv()
            await ws.send(json.dumps({"id": 5, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 8, "code": "Backspace", "key": "Backspace"}}))
            await ws.recv()
            await asyncio.sleep(0.05)

            # 3. Insert text via CDP Input.insertText
            await ws.send(json.dumps({"id": 6, "method": "Input.insertText", "params": {"text": prompt_text}}))
            await ws.recv()
            await asyncio.sleep(0.15)

            # 4. Click #send-message-button
            js_click = """
            (() => {
                const btn = document.getElementById("send-message-button");
                if (btn && !btn.disabled) {
                    btn.click();
                    return { clicked: true };
                }
                const form = document.querySelector("form:has(#chat-input)");
                if (form) {
                    form.requestSubmit();
                    return { submitted: true };
                }
                return { error: 'Button disabled or not found' };
            })()
            """
            await ws.send(json.dumps({"id": 7, "method": "Runtime.evaluate", "params": {"expression": js_click, "returnByValue": True}}))
            res = json.loads(await ws.recv())
            val = res.get("result", {}).get("result", {}).get("value", {})
            print(f"Z.ai prompt dispatch result: {val}")
            return val.get("clicked") or val.get("submitted", False)
    except Exception as e:
        print(f"Error posting prompt to Z.ai: {e}")
        return False


async def harvest_zai_response() -> str:
    """Harvests the latest assistant response from Z.ai."""
    tabs = get_chrome_tabs()
    zai_tab = next((t for t in tabs if "chat.z.ai" in t.get("url", "")), None)
    if not zai_tab:
        return ""
    ws_url = zai_tab.get("webSocketDebuggerUrl")
    if not ws_url:
        return ""
    try:
        async with websockets.connect(ws_url, max_size=20_000_000) as ws:
            js = """
            (() => {
                const msgs = Array.from(document.querySelectorAll('div[class*="message-"]'));
                if (!msgs.length) return "";
                return msgs[msgs.length - 1].innerText;
            })()
            """
            await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
            res = json.loads(await ws.recv())
            return res.get("result", {}).get("result", {}).get("value", "")
    except Exception:
        return ""


async def dispatch_dual(cycle_num: int = 47):
    print(f"=== DISPATCHING DUAL COUNCIL PROMPT — CYCLE {cycle_num} ===")
    prompt = build_prompt(cycle_num=cycle_num)
    prompt_file = ROOT / "docs" / "prompts" / f"CYCLE_{cycle_num}_DUAL_PROMPT.txt"
    prompt_file.parent.mkdir(parents=True, exist_ok=True)
    prompt_file.write_text(prompt, encoding="utf-8")
    print(f"Generated Cycle {cycle_num} prompt ({len(prompt)} chars) -> {prompt_file.name}")

    # 1. Dispatch to Arena.ai
    print("Posting to Arena.ai...")
    arena_ok = await post_prompt_to_arena(prompt)
    print(f"Arena.ai dispatch: {'SUCCESS' if arena_ok else 'FAILED'}")

    # 2. Dispatch to Z.ai
    print("Posting to Z.ai...")
    zai_ok = await post_prompt_to_zai(prompt)
    print(f"Z.ai dispatch: {'SUCCESS' if zai_ok else 'FAILED'}")

    print("\nBoth tabs prompted! Unified watcher can now monitor both.")
    return arena_ok and zai_ok


if __name__ == "__main__":
    c_num = 47
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        c_num = int(sys.argv[1])
    asyncio.run(dispatch_dual(cycle_num=c_num))
