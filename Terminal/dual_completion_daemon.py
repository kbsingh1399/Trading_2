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
                const stopBtn = document.querySelector('button[aria-label*="Stop" i], button:has(svg.lucide-square)');
                const isGenerating = !!stopBtn;
                const msgs = Array.from(document.querySelectorAll('div[class*="message-"]'));
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


def main():
    parser = argparse.ArgumentParser(description="Dual AI Completion Watcher")
    parser.add_argument("--timeout", type=float, default=600.0, help="Timeout in seconds")
    args = parser.parse_args()
    rc = asyncio.run(run_dual_watcher(timeout_s=args.timeout))
    sys.exit(rc)


if __name__ == "__main__":
    main()
