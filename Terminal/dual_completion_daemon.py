"""
Terminal/dual_completion_daemon.py
Unified dual-tab completion watcher for Arena.ai AND Z.ai.
Monitors both Chrome tabs concurrently via CDP, archives responses to
docs/trade_plans/ARENA_LATEST_RAW.md and docs/trade_plans/ZAI_LATEST_RAW.md,
and exits with code 0 to wake up Antigravity the exact second both responses complete.
"""
import argparse
import asyncio
import json
import os
import pathlib
import sys
import time
import urllib.request
from datetime import datetime, timezone
import websockets

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARENA_RAW_FILE = ROOT / "docs" / "trade_plans" / "ARENA_LATEST_RAW.md"
ZAI_RAW_FILE = ROOT / "docs" / "trade_plans" / "ZAI_LATEST_RAW.md"
ARENA_STATUS_FILE = ROOT / "Data" / "arena_completion_status.json"
ZAI_STATUS_FILE = ROOT / "Data" / "zai_completion_status.json"


def get_chrome_tabs():
    try:
        with urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=3) as resp:
            return json.loads(resp.read().decode())
    except Exception:
        return []


async def probe_arena_tab(tab_ws_url: str):
    try:
        async with websockets.connect(tab_ws_url, max_size=20_000_000) as ws:
            js = """
            (() => {
                const stopBtn = document.querySelector('button[aria-label="Stop generating"], button:has(svg.lucide-square)');
                const isGenerating = !!stopBtn;
                const copyBtn = document.querySelector('button[aria-label="Copy"], button:has(svg.lucide-copy)');
                const hasCopy = !!copyBtn;
                const yesNo = Array.from(document.querySelectorAll('button')).some(b => b.innerText.includes('Keep working') || b.innerText.includes('Yes'));
                const proses = Array.from(document.querySelectorAll('.prose')).filter(p => !p.classList.contains('tiptap'));
                const lastText = proses.length > 0 ? proses[proses.length - 1].innerText : '';
                return {
                    connected: true,
                    isGenerating: isGenerating,
                    hasCopy: hasCopy,
                    hasYesNo: yesNo,
                    textLen: lastText.length,
                    text: lastText
                };
            })()
            """
            await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
            res = json.loads(await ws.recv())
            return res.get("result", {}).get("result", {}).get("value", {})
    except Exception:
        return {"connected": False}


async def probe_zai_tab(tab_ws_url: str):
    try:
        async with websockets.connect(tab_ws_url, max_size=20_000_000) as ws:
            js = """
            (() => {
                const stopBtn = document.querySelector('button[aria-label*="Stop" i], button:has(svg.lucide-square), .stop-generating');
                const isGenerating = !!stopBtn;
                const msgs = Array.from(document.querySelectorAll('.prose, div[class*="markdown"], div[class*="message-content"]'));
                const lastMsg = msgs.length > 0 ? msgs[msgs.length - 1].innerText : '';
                return {
                    connected: true,
                    isGenerating: isGenerating,
                    textLen: lastMsg.length,
                    text: lastMsg
                };
            })()
            """
            await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
            res = json.loads(await ws.recv())
            return res.get("result", {}).get("result", {}).get("value", {})
    except Exception:
        return {"connected": False}


async def run_dual_watcher(timeout_s: float = 600.0, poll_interval: float = 2.5):
    print(f"[DualWatcher] Started unified watcher for Arena.ai AND Z.ai (timeout={timeout_s}s)...", flush=True)
    start_ts = time.time()
    arena_done = False
    zai_done = False

    while (time.time() - start_ts) < timeout_s:
        await asyncio.sleep(poll_interval)
        tabs = get_chrome_tabs()
        arena_tab = next((t for t in tabs if "arena.ai" in t.get("url", "")), None)
        zai_tab = next((t for t in tabs if "chat.z.ai" in t.get("url", "")), None)

        # Check Arena
        if arena_tab and not arena_done:
            ws_url = arena_tab.get("webSocketDebuggerUrl")
            if ws_url:
                astate = await probe_arena_tab(ws_url)
                if astate.get("connected") and not astate.get("isGenerating") and (astate.get("hasCopy") or astate.get("hasYesNo")) and astate.get("textLen", 0) > 300:
                    ARENA_RAW_FILE.parent.mkdir(parents=True, exist_ok=True)
                    ARENA_RAW_FILE.write_text(astate.get("text", ""), encoding="utf-8")
                    arena_done = True
                    print(f"[{time.strftime('%H:%M:%S')}] 🔔 Arena.ai response complete ({astate.get('textLen')} chars) -> saved ARENA_LATEST_RAW.md", flush=True)

        # Check Z.ai
        if zai_tab and not zai_done:
            ws_url = zai_tab.get("webSocketDebuggerUrl")
            if ws_url:
                zstate = await probe_zai_tab(ws_url)
                if zstate.get("connected") and not zstate.get("isGenerating") and zstate.get("textLen", 0) > 300:
                    ZAI_RAW_FILE.parent.mkdir(parents=True, exist_ok=True)
                    ZAI_RAW_FILE.write_text(zstate.get("text", ""), encoding="utf-8")
                    zai_done = True
                    print(f"[{time.strftime('%H:%M:%S')}] 🔔 Z.ai response complete ({zstate.get('textLen')} chars) -> saved ZAI_LATEST_RAW.md", flush=True)

        if arena_done and zai_done:
            print("\n🎉 BOTH ARENA.AI AND Z.AI RESPONSES COMPLETE! Triggering unified wakeup.", flush=True)
            return 0

    print("[DualWatcher] Timeout reached.", file=sys.stderr, flush=True)
    return 0 if (arena_done or zai_done) else 1


async def run_dual_daemon(poll_interval: float = 3.0):
    print(f"[DualCompletionDaemon] Running persistent daemon for Arena.ai & Z.ai...", flush=True)
    last_arena_len = 0
    last_zai_len = 0
    ARENA_STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)

    while True:
        try:
            await asyncio.sleep(poll_interval)
            tabs = get_chrome_tabs()
            arena_tab = next((t for t in tabs if "arena.ai" in t.get("url", "")), None)
            zai_tab = next((t for t in tabs if "chat.z.ai" in t.get("url", "")), None)

            # 1. Arena.ai Check
            if arena_tab:
                ws_url = arena_tab.get("webSocketDebuggerUrl")
                if ws_url:
                    astate = await probe_arena_tab(ws_url)
                    t_len = astate.get("textLen", 0)
                    is_gen = astate.get("isGenerating", False)
                    status_payload = {
                        "is_generating": is_gen,
                        "text_length": t_len,
                        "has_copy_button": astate.get("hasCopy", False),
                        "checked_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
                    }
                    if not is_gen and t_len > 300 and t_len != last_arena_len and (astate.get("hasCopy") or astate.get("hasYesNo")):
                        ARENA_RAW_FILE.write_text(astate.get("text", ""), encoding="utf-8")
                        last_arena_len = t_len
                        status_payload["completed_at_utc"] = status_payload["checked_at_utc"]
                        print(f"[{time.strftime('%H:%M:%S')}] 🔔 [Daemon] Harvested new Arena.ai turn ({t_len:,} chars)", flush=True)
                    ARENA_STATUS_FILE.write_text(json.dumps(status_payload, indent=2), encoding="utf-8")

            # 2. Z.ai Check
            if zai_tab:
                ws_url = zai_tab.get("webSocketDebuggerUrl")
                if ws_url:
                    zstate = await probe_zai_tab(ws_url)
                    t_len = zstate.get("textLen", 0)
                    is_gen = zstate.get("isGenerating", False)
                    status_payload = {
                        "is_generating": is_gen,
                        "text_length": t_len,
                        "checked_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
                    }
                    if not is_gen and t_len > 300 and t_len != last_zai_len:
                        ZAI_RAW_FILE.write_text(zstate.get("text", ""), encoding="utf-8")
                        last_zai_len = t_len
                        status_payload["completed_at_utc"] = status_payload["checked_at_utc"]
                        print(f"[{time.strftime('%H:%M:%S')}] 🔔 [Daemon] Harvested new Z.ai turn ({t_len:,} chars)", flush=True)
                    ZAI_STATUS_FILE.write_text(json.dumps(status_payload, indent=2), encoding="utf-8")

        except Exception as e:
            await asyncio.sleep(poll_interval)


def main():
    parser = argparse.ArgumentParser(description="Dual AI Completion Watcher")
    parser.add_argument("--timeout", type=float, default=600.0, help="Timeout in seconds for single wait mode")
    parser.add_argument("--daemon", action="store_true", help="Run continuously as background daemon")
    parser.add_argument("--wait", action="store_true", help="Wait for current in-flight generation then exit 0")
    args = parser.parse_args()

    if args.daemon:
        asyncio.run(run_dual_daemon())
        sys.exit(0)
    else:
        rc = asyncio.run(run_dual_watcher(timeout_s=args.timeout))
        sys.exit(rc)


if __name__ == "__main__":
    main()
