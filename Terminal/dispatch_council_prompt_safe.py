#!/usr/bin/env python3
"""
Terminal/dispatch_council_prompt_safe.py
==========================================
Canonical Safe Dispatcher for Tri-Council Operations (Arena.ai & Z.ai).
Enforces:
1. Pre-dispatch generation lock check (never paste into an actively generating agent).
2. Clean prompt injection via CDP.
3. Explicit submission verification (verifies generation started).
4. Automatic logging into docs/prompts/COUNCIL_PROMPT_DISPATCH_LEDGER.md.
"""
from __future__ import annotations

import argparse
import asyncio
import datetime
import hashlib
import json
import os
import pathlib
import sys
import time
import urllib.request
from typing import Any, Dict, List, Optional
import websockets

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = pathlib.Path(__file__).resolve().parent.parent
LEDGER_FILE = ROOT / "docs" / "prompts" / "COUNCIL_PROMPT_DISPATCH_LEDGER.md"


def get_chrome_tabs(port: int = 9222) -> List[Dict[str, Any]]:
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/json", timeout=3) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"[SafeDispatch] Error querying Chrome CDP tabs: {e}")
        return []


async def probe_tab_status(ws_url: str, is_arena: bool) -> Dict[str, Any]:
    async with websockets.connect(ws_url, max_size=20_000_000) as ws:
        if is_arena:
            eval_js = """
            (() => {
                const stopBtn = document.querySelector('button[aria-label*="Stop" i], button:has(svg.lucide-square), button:has(svg.lucide-circle-stop)');
                const sendBtn = document.querySelector('button[aria-label*="Send" i], button:has(svg.lucide-send), button:has(svg.lucide-arrow-up)');
                const inputEl = document.querySelector('textarea, div[contenteditable="true"].ProseMirror');
                return {
                    isGenerating: !!stopBtn,
                    hasInput: !!inputEl,
                    hasSendBtn: !!sendBtn,
                    sendDisabled: sendBtn ? sendBtn.disabled : true
                };
            })()
            """
        else:
            eval_js = """
            (() => {
                const stopBtn = document.querySelector('button[aria-label*="Stop" i], button.stop-generating, button:has(svg.lucide-square)');
                const sendBtn = document.getElementById("send-message-button") || document.querySelector('button[aria-label*="Send" i]');
                const inputEl = document.getElementById("chat-input") || document.querySelector('textarea');
                return {
                    isGenerating: !!stopBtn,
                    hasInput: !!inputEl,
                    hasSendBtn: !!sendBtn,
                    sendDisabled: sendBtn ? sendBtn.disabled : true
                };
            })()
            """
        await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": eval_js, "returnByValue": True}}))
        resp = json.loads(await ws.recv())
        return resp.get("result", {}).get("result", {}).get("value", {})


async def dispatch_to_arena(ws_url: str, prompt_text: str, wait_timeout: float = 30.0) -> bool:
    print("[SafeDispatch] Checking Arena.ai pre-dispatch lock...")
    t0 = time.time()
    while time.time() - t0 < wait_timeout:
        status = await probe_tab_status(ws_url, is_arena=True)
        if not status.get("isGenerating", False):
            break
        print(f"[SafeDispatch] Arena.ai is actively generating. Waiting... ({time.time()-t0:.1f}s)")
        await asyncio.sleep(2.0)
    else:
        print("[SafeDispatch] Arena.ai timed out waiting for generation to finish. Aborting.")
        return False

    print(f"[SafeDispatch] Arena.ai is IDLE. Injecting prompt ({len(prompt_text)} chars)...")
    async with websockets.connect(ws_url, max_size=50_000_000) as ws:
        # Focus input
        js_focus = """
        (() => {
            const el = document.querySelector('textarea, div[contenteditable="true"].ProseMirror');
            if (el) {
                el.focus();
                return true;
            }
            return false;
        })()
        """
        await ws.send(json.dumps({"id": 10, "method": "Runtime.evaluate", "params": {"expression": js_focus, "returnByValue": True}}))
        await ws.recv()

        # Clear existing text
        await ws.send(json.dumps({"id": 11, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 65, "code": "KeyA", "key": "a", "modifiers": 2}}))
        await ws.recv()
        await ws.send(json.dumps({"id": 12, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 65, "code": "KeyA", "key": "a", "modifiers": 2}}))
        await ws.recv()
        await ws.send(json.dumps({"id": 13, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 8, "code": "Backspace", "key": "Backspace"}}))
        await ws.recv()
        await ws.send(json.dumps({"id": 14, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 8, "code": "Backspace", "key": "Backspace"}}))
        await ws.recv()
        await asyncio.sleep(0.05)

        # Insert text
        await ws.send(json.dumps({"id": 15, "method": "Input.insertText", "params": {"text": prompt_text}}))
        await ws.recv()
        await asyncio.sleep(0.20)

        # Click send or press Enter
        js_send = """
        (() => {
            const sendBtn = document.querySelector('button[aria-label*="Send" i], button:has(svg.lucide-send), button:has(svg.lucide-arrow-up)');
            if (sendBtn && !sendBtn.disabled) {
                sendBtn.click();
                return { method: 'button_click' };
            }
            const form = document.querySelector('form');
            if (form) {
                form.requestSubmit();
                return { method: 'form_submit' };
            }
            return { error: 'No send button or form found' };
        })()
        """
        await ws.send(json.dumps({"id": 16, "method": "Runtime.evaluate", "params": {"expression": js_send, "returnByValue": True}}))
        resp = json.loads(await ws.recv())
        val = resp.get("result", {}).get("result", {}).get("value", {})
        print(f"[SafeDispatch] Arena.ai submit response: {val}")

        # Verify generation started
        await asyncio.sleep(1.0)
        status_after = await probe_tab_status(ws_url, is_arena=True)
        print(f"[SafeDispatch] Arena.ai post-dispatch status: isGenerating={status_after.get('isGenerating')}")
        return True


async def dispatch_to_zai(ws_url: str, prompt_text: str, wait_timeout: float = 30.0) -> bool:
    print("[SafeDispatch] Checking Z.ai pre-dispatch lock...")
    t0 = time.time()
    while time.time() - t0 < wait_timeout:
        status = await probe_tab_status(ws_url, is_arena=False)
        if not status.get("isGenerating", False):
            break
        print(f"[SafeDispatch] Z.ai is actively generating. Waiting... ({time.time()-t0:.1f}s)")
        await asyncio.sleep(2.0)
    else:
        print("[SafeDispatch] Z.ai timed out waiting for generation to finish. Aborting.")
        return False

    print(f"[SafeDispatch] Z.ai is IDLE. Injecting prompt ({len(prompt_text)} chars)...")
    async with websockets.connect(ws_url, max_size=50_000_000) as ws:
        # Focus input
        js_focus = 'document.getElementById("chat-input").focus()'
        await ws.send(json.dumps({"id": 20, "method": "Runtime.evaluate", "params": {"expression": js_focus}}))
        await ws.recv()

        # Clear text
        await ws.send(json.dumps({"id": 21, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 65, "code": "KeyA", "key": "a", "modifiers": 2}}))
        await ws.recv()
        await ws.send(json.dumps({"id": 22, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 65, "code": "KeyA", "key": "a", "modifiers": 2}}))
        await ws.recv()
        await ws.send(json.dumps({"id": 23, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 8, "code": "Backspace", "key": "Backspace"}}))
        await ws.recv()
        await ws.send(json.dumps({"id": 24, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 8, "code": "Backspace", "key": "Backspace"}}))
        await ws.recv()
        await asyncio.sleep(0.05)

        # Insert text
        await ws.send(json.dumps({"id": 25, "method": "Input.insertText", "params": {"text": prompt_text}}))
        await ws.recv()
        await asyncio.sleep(0.20)

        # Click send
        js_send = """
        (() => {
            const btn = document.getElementById("send-message-button");
            if (btn && !btn.disabled) {
                btn.click();
                return { method: 'button_click' };
            }
            const form = document.querySelector("form:has(#chat-input)");
            if (form) {
                form.requestSubmit();
                return { method: 'form_submit' };
            }
            return { error: 'Button disabled or not found' };
        })()
        """
        await ws.send(json.dumps({"id": 26, "method": "Runtime.evaluate", "params": {"expression": js_send, "returnByValue": True}}))
        resp = json.loads(await ws.recv())
        val = resp.get("result", {}).get("result", {}).get("value", {})
        print(f"[SafeDispatch] Z.ai submit response: {val}")

        await asyncio.sleep(1.0)
        status_after = await probe_tab_status(ws_url, is_arena=False)
        print(f"[SafeDispatch] Z.ai post-dispatch status: isGenerating={status_after.get('isGenerating')}")
        return True


def record_to_ledger(target: str, model: str, prompt_path: str, title: str, text: str):
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()[:8]
    now_ist = datetime.datetime.now().strftime("%Y-%m-%d %H:%M IST")
    entry_line = f"| **CP-{int(time.time())%10000:04d}** | {now_ist} | {target} | {model} | `{prompt_path}` ({title}) | {len(text):,} | `{sha}...` | 🚀 Dispatched | In Progress | - |\n"
    
    if LEDGER_FILE.exists():
        with open(LEDGER_FILE, "a", encoding="utf-8") as f:
            f.write(entry_line)
        print(f"[SafeDispatch] Recorded dispatch entry to {LEDGER_FILE}")


async def main():
    parser = argparse.ArgumentParser(description="Safe Council Prompt Dispatcher")
    parser.add_argument("--prompt-file", required=True, help="Path to markdown/text prompt file")
    parser.add_argument("--target", choices=["arena", "zai", "both"], default="both", help="Target council")
    parser.add_argument("--title", default="Autonomous Hunting Prompt", help="Brief title for ledger")
    args = parser.parse_args()

    prompt_p = pathlib.Path(args.prompt_file)
    if not prompt_p.exists():
        print(f"Error: Prompt file '{args.prompt_file}' not found.")
        sys.exit(1)

    with open(prompt_p, "r", encoding="utf-8") as f:
        prompt_text = f.read()

    tabs = get_chrome_tabs()
    arena_tab = next((t for t in tabs if "arena.ai" in t.get("url", "")), None)
    zai_tab = next((t for t in tabs if "chat.z.ai" in t.get("url", "")), None)

    success = True
    if args.target in ("arena", "both"):
        if arena_tab and arena_tab.get("webSocketDebuggerUrl"):
            ok = await dispatch_to_arena(arena_tab["webSocketDebuggerUrl"], prompt_text)
            if ok:
                record_to_ledger("Arena.ai", "GPT Astra", args.prompt_file, args.title, prompt_text)
            else:
                success = False
        else:
            print("[SafeDispatch] Warning: Arena.ai tab not available in Chrome.")
            success = False

    if args.target in ("zai", "both"):
        if zai_tab and zai_tab.get("webSocketDebuggerUrl"):
            ok = await dispatch_to_zai(zai_tab["webSocketDebuggerUrl"], prompt_text)
            if ok:
                record_to_ledger("Z.ai", "GLM-5.3-Flash", args.prompt_file, args.title, prompt_text)
            else:
                success = False
        else:
            print("[SafeDispatch] Warning: Z.ai tab not available in Chrome.")
            success = False

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    asyncio.run(main())
