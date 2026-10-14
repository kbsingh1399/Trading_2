"""
Terminal/chrome_tabs_keepalive_daemon.py
Autonomous Zero-Token Keep-Alive & Sentry Daemon for Chrome CDP (Port 9222).

Purpose:
  1. Cycles through all 4 target trading agent tabs in Google Chrome:
     - Copilot Studio: Opus 5.5 (agent 98cead10)
     - Copilot Studio: GPT Astra (agent 3e9246b9)
     - Arena.ai (agent 01a1311e)
     - Z.ai Chat (session 575144c2)
  2. Brings each tab to front via CDP `Page.bringToFront` sequentially.
  3. Dispatches lightweight heartbeat events (`focus`, `mousemove`) to prevent Chrome
     from throttling, sleeping, or memory-discarding inactive tabs.
  4. Auto-Submit Sentry: Detects if an unsubmitted prompt is sitting in the input box
     with an enabled Send button, and automatically triggers submission.
  5. Runs continuously in background (IsDaemon=true) with ZERO LLM token consumption.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import os
import pathlib
import sys
import time
import urllib.request
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

import websockets

try:
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)
except Exception:
    pass

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "Data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
STATUS_FILE = DATA_DIR / "chrome_tabs_keepalive_status.json"

CDP_JSON_URLS = [
    "http://localhost:9222/json",
    "http://127.0.0.1:9222/json",
]

# Tab target definitions - prioritizes the 3 active trading desk tabs in debug Chrome
TARGET_SPECS = [
    {
        "id": "arena_1",
        "name": "Arena.ai Tab 1 (GPT Astra 01a136b2)",
        "match": lambda url, title: "arena.ai" in url and "01a136b2" in url,
        "is_copilot": False,
        "is_arena": True,
    },
    {
        "id": "arena_2",
        "name": "Arena.ai Tab 2 (Claude Fable 01a1311e)",
        "match": lambda url, title: "arena.ai" in url and "01a1311e" in url,
        "is_copilot": False,
        "is_arena": True,
    },
    {
        "id": "gemini_argon",
        "name": "Google Gemini (Argon Mode)",
        "match": lambda url, title: "gemini.google.com" in url,
        "is_copilot": False,
        "is_gemini": True,
    },
    {
        "id": "copilot_opus",
        "name": "Copilot Studio (Opus 5.5)",
        "match": lambda url, title: "copilotstudio" in url and "98cead10" in url,
        "is_copilot": True,
    },
    {
        "id": "copilot_astra",
        "name": "Copilot Studio (GPT Astra)",
        "match": lambda url, title: "copilotstudio" in url and "3e9246b9" in url,
        "is_copilot": True,
    },
]


def fetch_cdp_tabs() -> List[Dict[str, Any]]:
    """Fetch all open Chrome tabs from CDP endpoints."""
    for url in CDP_JSON_URLS:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "AntigravityKeepAlive/1.0"})
            with urllib.request.urlopen(req, timeout=3.0) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                if isinstance(data, list):
                    return [t for t in data if t.get("type") == "page"]
        except Exception:
            continue
    return []


async def cdp_eval_with_timeout(ws: websockets.WebSocketClientProtocol, expression: str, timeout_sec: float = 4.0) -> Any:
    """Safely evaluate JavaScript in a tab via CDP with response matching and timeout."""
    msg_id = int(time.time() * 1000) % 1_000_000
    await ws.send(json.dumps({
        "id": msg_id,
        "method": "Runtime.evaluate",
        "params": {
            "expression": expression,
            "returnByValue": True,
            "awaitPromise": True,
        }
    }))
    
    start = time.time()
    while time.time() - start < timeout_sec:
        try:
            raw = await asyncio.wait_for(ws.recv(), timeout=1.5)
            data = json.loads(raw)
            if data.get("id") == msg_id:
                return data.get("result", {}).get("result", {}).get("value")
        except asyncio.TimeoutError:
            continue
        except Exception:
            break
    return None


async def ping_tab(tab_spec: Dict[str, Any], tab_info: Dict[str, Any], dwell_sec: float = 1.5) -> Dict[str, Any]:
    """Connect to a single tab, bring it to front, touch DOM, and check for unsubmitted prompts."""
    ws_url = tab_info.get("webSocketDebuggerUrl")
    if not ws_url:
        return {"status": "error", "error": "No webSocketDebuggerUrl"}

    result: Dict[str, Any] = {
        "status": "ok",
        "tab_id": tab_spec["id"],
        "name": tab_spec["name"],
        "url": tab_info.get("url", ""),
        "title": tab_info.get("title", ""),
        "heartbeat_at": datetime.now(timezone.utc).isoformat(),
        "brought_to_front": False,
        "auto_sent": False,
    }

    try:
        async with websockets.connect(ws_url, max_size=20_000_000, ping_interval=None) as ws:
            # 1. Bring tab to front
            bring_id = int(time.time() * 1000) % 1_000_000
            await ws.send(json.dumps({"id": bring_id, "method": "Page.bringToFront"}))
            try:
                await asyncio.wait_for(ws.recv(), timeout=2.0)
                result["brought_to_front"] = True
            except Exception:
                pass

            # Dwell briefly so Chrome renders and acknowledges the tab as active
            await asyncio.sleep(dwell_sec)

            # 2. Dispatch lightweight focus/touch heartbeat
            js_heartbeat = """(() => {
                window.dispatchEvent(new Event('focus'));
                document.dispatchEvent(new MouseEvent('mousemove', { bubbles: true, clientX: 100, clientY: 100 }));
                return {
                    docState: document.readyState,
                    title: document.title,
                    textLen: document.body ? document.body.innerText.length : 0
                };
            })()"""
            hb_res = await cdp_eval_with_timeout(ws, js_heartbeat, timeout_sec=3.0)
            if hb_res:
                result["doc_state"] = hb_res.get("docState")
                result["body_len"] = hb_res.get("textLen")

            # 3. If Copilot Studio, check if an unsubmitted prompt is sitting
            if tab_spec.get("is_copilot"):
                js_sentry = """(() => {
                    const input = document.querySelector('[role="textbox"], .fai-EditorInput__input');
                    const sendBtn = document.querySelector('button[aria-label="Send"], button[title="Send"], .fai-SendButton');
                    const inputVal = input ? (input.innerText || input.value || '').trim() : '';
                    const hasFiles = Boolean(document.querySelector('[class*="attachment"], [class*="file"], [class*="badge"]'));
                    
                    if (inputVal.length > 50 && sendBtn && !sendBtn.disabled) {
                        // Unsubmitted prompt sitting in box! Trigger click
                        sendBtn.click();
                        return { action: "clicked_send", input_len: inputVal.length, has_files: hasFiles };
                    }
                    return { action: "none", input_len: inputVal.length, send_btn_found: Boolean(sendBtn) };
                })()"""
                sentry_res = await cdp_eval_with_timeout(ws, js_sentry, timeout_sec=3.0)
                if sentry_res and sentry_res.get("action") == "clicked_send":
                    result["auto_sent"] = True
                    result["auto_sent_details"] = sentry_res
            # 4. If Qwen Chat, check if unsubmitted prompt is sitting
            if tab_spec.get("is_qwen"):
                js_qwen_sentry = """(() => {
                    const ta = document.querySelector('textarea.message-input-textarea, textarea');
                    const sendBtn = document.querySelector('button.send-button, button[aria-label="Send"], button[class*="send"]');
                    const inputVal = ta ? (ta.value || '').trim() : '';
                    if (inputVal.length > 50 && sendBtn && !sendBtn.disabled) {
                        sendBtn.click();
                        return { action: "clicked_send", input_len: inputVal.length };
                    }
                    return { action: "none", input_len: inputVal.length, send_btn_found: Boolean(sendBtn) };
                })()"""
                qsentry_res = await cdp_eval_with_timeout(ws, js_qwen_sentry, timeout_sec=3.0)
                if qsentry_res and qsentry_res.get("action") == "clicked_send":
                    result["auto_sent"] = True
                    result["auto_sent_details"] = qsentry_res
                    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] [AUTO-SENT] Clicked Send button on Qwen! (len={qsentry_res.get('input_len')})")

    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)

    return result


async def run_single_keepalive_cycle(dwell_sec: float = 1.5) -> Dict[str, Any]:
    """Execute a single sweep across all 4 target tabs."""
    tabs = fetch_cdp_tabs()
    cycle_summary: Dict[str, Any] = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_cdp_tabs": len(tabs),
        "target_tabs_found": 0,
        "results": {},
    }

    if not tabs:
        cycle_summary["error"] = "No open page tabs found on CDP port 9222"
        return cycle_summary

    for spec in TARGET_SPECS:
        matched_tab = None
        for t in tabs:
            url = t.get("url", "")
            title = t.get("title", "")
            if spec["match"](url, title):
                matched_tab = t
                break

        if matched_tab:
            cycle_summary["target_tabs_found"] += 1
            res = await ping_tab(spec, matched_tab, dwell_sec=dwell_sec)
            cycle_summary["results"][spec["id"]] = res
        else:
            cycle_summary["results"][spec["id"]] = {
                "status": "not_found",
                "name": spec["name"],
                "heartbeat_at": datetime.now(timezone.utc).isoformat(),
            }

    # Save to status file
    try:
        STATUS_FILE.write_text(json.dumps(cycle_summary, indent=2, ensure_ascii=False), encoding="utf-8")
    except Exception:
        pass

    return cycle_summary


async def daemon_loop(interval_sec: float = 75.0, dwell_sec: float = 1.5):
    """Main infinite daemon loop."""
    print("=" * 70)
    print("🚀 Chrome Tabs Keepalive & Sentry Daemon Starting...")
    print(f"   CDP Endpoints: {', '.join(CDP_JSON_URLS)}")
    print(f"   Cycle Interval: {interval_sec}s | Dwell Per Tab: {dwell_sec}s")
    print("   Monitored Targets: Arena 1 (Astra), Arena 2 (Fable), Gemini (Argon), Copilot")
    print(f"   Status File: {STATUS_FILE}")
    print("=" * 70)

    cycle_count = 0
    while True:
        cycle_count += 1
        t_start = time.time()
        now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        
        try:
            summary = await run_single_keepalive_cycle(dwell_sec=dwell_sec)
            found = summary.get("target_tabs_found", 0)
            elapsed = time.time() - t_start
            
            auto_sends = [k for k, v in summary.get("results", {}).items() if v.get("auto_sent")]
            send_tag = f" [AUTO-SENT on {', '.join(auto_sends)}]" if auto_sends else ""
            print(f"[{now_str}] Cycle #{cycle_count}: Visited {found}/4 tabs in {elapsed:.1f}s.{send_tag}")

        except Exception as e:
            print(f"[{now_str}] Cycle #{cycle_count} Exception: {e}", file=sys.stderr)

        await asyncio.sleep(interval_sec)


def main():
    parser = argparse.ArgumentParser(description="Chrome Tabs Keepalive Daemon")
    parser.add_argument("--once", action="store_true", help="Run a single keepalive cycle and exit")
    parser.add_argument("--interval", type=float, default=75.0, help="Interval between cycles in seconds (default: 75.0)")
    parser.add_argument("--dwell", type=float, default=1.5, help="Dwell time per tab in seconds (default: 1.5)")
    args = parser.parse_args()

    if args.once:
        res = asyncio.run(run_single_keepalive_cycle(dwell_sec=args.dwell))
        print(json.dumps(res, indent=2))
    else:
        asyncio.run(daemon_loop(interval_sec=args.interval, dwell_sec=args.dwell))


if __name__ == "__main__":
    main()
