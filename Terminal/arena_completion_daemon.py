"""
Terminal/arena_completion_daemon.py
Always-on / reactive wakeup watcher for Arena.ai responses via Chrome CDP (port 9222).

Detects response completion the exact instant either:
  1. The 'Copy' button (button[aria-label="Copy"]) appears on the latest assistant message turn, OR
  2. The 'Was this task successful?' (Yes / No / Keep working) feedback banner appears,
while no 'Stop' generation button is active.

Modes:
  • Default / --wait: Waits for an in-flight or new Arena.ai response to complete, saves the
    full response to docs/trade_plans/ARENA_LATEST_RAW.md and Data/arena_completion_status.json,
    prints the completion wakeup notice, and exits 0 — immediately waking up Antigravity!
  • --daemon: Persistent background daemon (IsDaemon=true) that continuously monitors Arena.ai,
    auto-harvests every newly completed response to docs/trade_plans/ARENA_LATEST_RAW.md, and
    updates Data/arena_completion_status.json.
"""
import argparse
import asyncio
import hashlib
import json
import pathlib
import sys
import time
import urllib.request
from datetime import datetime, timezone

import websockets

ROOT = pathlib.Path(__file__).resolve().parents[1]
CDP_URL = "http://127.0.0.1:9222/json"
ARENA_AGENT_ID = "01a12432-7fb8-7f7b-82fa-b2cf537c1eb8"
STATUS_FILE = ROOT / "Data" / "arena_completion_status.json"
LATEST_RAW_FILE = ROOT / "docs" / "trade_plans" / "ARENA_LATEST_RAW.md"

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def _find_arena_ws_url() -> str | None:
    try:
        raw = urllib.request.urlopen(CDP_URL, timeout=5).read().decode("utf-8")
        tabs = json.loads(raw)
        for t in tabs:
            if ARENA_AGENT_ID in t.get("url", "") and t.get("webSocketDebuggerUrl"):
                return t["webSocketDebuggerUrl"]
        for t in tabs:
            if "arena.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl"):
                return t["webSocketDebuggerUrl"]
    except Exception:
        return None
    return None


async def probe_arena_state() -> dict:
    ws_url = _find_arena_ws_url()
    if not ws_url:
        return {"connected": False, "error": "Arena tab not found on CDP 9222"}

    js = """(() => {
        const btnStop = document.querySelector('button[aria-label*="Stop"], button[title*="Stop"]');
        const isGenerating = Boolean(btnStop);
        const proses = Array.from(document.querySelectorAll('.prose'));
        const proseCount = proses.length;
        const lastProse = proseCount > 0 ? proses[proseCount - 1] : null;
        const lastText = lastProse ? (lastProse.innerText || '').trim() : '';

        let turnEl = lastProse;
        for (let i = 0; i < 4 && turnEl && turnEl.parentElement; i++) {
            turnEl = turnEl.parentElement;
        }
        const hasCopyButton = Boolean(turnEl && turnEl.querySelector('button[aria-label="Copy"]'));
        const turnFooter = turnEl ? (turnEl.innerText || '').slice(-160) : '';
        const hasDurationFooter = /\\d+[ms]\\s*\\|\\s*(just now|\\d+[smh]\\s+ago)/i.test(turnFooter);

        const bodyText = document.body ? (document.body.innerText || '') : '';
        const hasYesNoBanner = bodyText.includes('Was this task successful?');

        return {
            connected: true,
            isGenerating,
            proseCount,
            lastLen: lastText.length,
            lastText,
            hasCopyButton,
            hasDurationFooter,
            hasYesNoBanner
        };
    })()"""

    try:
        async with websockets.connect(ws_url, max_size=50_000_000, open_timeout=5, close_timeout=3) as ws:
            await ws.send(json.dumps({
                "id": 1,
                "method": "Runtime.evaluate",
                "params": {"expression": js, "returnByValue": True}
            }))
            resp = json.loads(await asyncio.wait_for(ws.recv(), timeout=8))
            val = resp.get("result", {}).get("result", {}).get("value")
            if isinstance(val, dict):
                text = val.get("lastText") or ""
                val["textHash"] = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16] if text else ""
                return val
    except Exception as e:
        return {"connected": False, "error": str(e)}
    return {"connected": False, "error": "Empty CDP evaluation response"}


def save_completion_artifacts(state: dict) -> None:
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    LATEST_RAW_FILE.parent.mkdir(parents=True, exist_ok=True)

    text = state.get("lastText") or ""
    if text:
        LATEST_RAW_FILE.write_text(text, encoding="utf-8")

    payload = {
        "completed_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "completed_at_epoch": time.time(),
        "prose_count": state.get("proseCount", 0),
        "text_length": state.get("lastLen", 0),
        "text_hash": state.get("textHash", ""),
        "has_copy_button": state.get("hasCopyButton", False),
        "has_yes_no_banner": state.get("hasYesNoBanner", False),
        "has_duration_footer": state.get("hasDurationFooter", False),
        "is_generating": state.get("isGenerating", False),
        "latest_raw_path": str(LATEST_RAW_FILE),
    }
    STATUS_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")


async def run_wait_for_completion(poll_interval: float = 2.0, timeout_s: float = 1200.0) -> int:
    start_ts = time.time()
    initial = await probe_arena_state()
    initial_hash = initial.get("textHash", "")
    initial_generating = initial.get("isGenerating", False)
    saw_generating = initial_generating

    print(
        f"[ArenaWatcher] Started wait-for-completion watcher "
        f"(initial_generating={initial_generating}, initial_hash={initial_hash}, "
        f"proseCount={initial.get('proseCount')}, hasCopy={initial.get('hasCopyButton')}, "
        f"hasYesNo={initial.get('hasYesNoBanner')})",
        flush=True,
    )

    stable_ready_ticks = 0
    last_seen_hash = initial_hash

    while (time.time() - start_ts) < timeout_s:
        await asyncio.sleep(poll_interval)
        state = await probe_arena_state()
        if not state.get("connected"):
            continue

        is_gen = state.get("isGenerating", False)
        if is_gen:
            saw_generating = True
            stable_ready_ticks = 0
            continue

        curr_hash = state.get("textHash", "")
        has_copy = state.get("hasCopyButton", False)
        has_yes_no = state.get("hasYesNoBanner", False)
        has_footer = state.get("hasDurationFooter", False)
        last_len = state.get("lastLen", 0)

        # Completion condition: not generating, Copy button or Yes/No banner present,
        # and either we observed generation during this wait OR the response hash changed
        # OR at least 15s elapsed and the turn already shows Copy + Yes/No completion signals.
        is_new_or_finished = saw_generating or (curr_hash != initial_hash and last_len > 200) or ((time.time() - start_ts) >= 8.0 and (has_copy or has_yes_no) and last_len > 200)

        if not is_gen and (has_copy or has_yes_no or has_footer) and is_new_or_finished:
            if curr_hash == last_seen_hash and curr_hash != "":
                stable_ready_ticks += 1
            else:
                last_seen_hash = curr_hash
                stable_ready_ticks = 1

            if stable_ready_ticks >= 2:
                save_completion_artifacts(state)
                print(
                    f"\n🔔 ARENA.AI RESPONSE COMPLETE — WAKE UP TRIGGERED!\n"
                    f"  • Signals: hasCopyButton={has_copy} | hasYesNoBanner={has_yes_no} | hasDurationFooter={has_footer}\n"
                    f"  • Prose Count: {state.get('proseCount')} | Length: {last_len} chars | Hash: {curr_hash}\n"
                    f"  • Saved full output to: {LATEST_RAW_FILE}\n",
                    flush=True,
                )
                preview = (state.get("lastText") or "")[:1200]
                print("--- PREVIEW OF COMPLETED ARENA RESPONSE ---")
                print(preview)
                print("--- END PREVIEW ---", flush=True)
                return 0
        else:
            last_seen_hash = curr_hash
            stable_ready_ticks = 0

    print("[ArenaWatcher] Timeout reached while waiting for Arena.ai completion.", file=sys.stderr, flush=True)
    return 1


async def run_persistent_daemon(poll_interval: float = 3.0) -> None:
    print("[ArenaDaemon] Persistent Arena.ai Completion Watcher Daemon started.", flush=True)
    last_recorded_hash = ""
    if STATUS_FILE.exists():
        try:
            last_recorded_hash = json.loads(STATUS_FILE.read_text(encoding="utf-8")).get("text_hash", "")
        except Exception:
            last_recorded_hash = ""

    stable_ticks = 0
    candidate_hash = ""

    while True:
        state = await probe_arena_state()
        if state.get("connected") and not state.get("isGenerating"):
            curr_hash = state.get("textHash", "")
            has_copy = state.get("hasCopyButton", False)
            has_yes_no = state.get("hasYesNoBanner", False)
            has_footer = state.get("hasDurationFooter", False)

            if curr_hash and curr_hash != last_recorded_hash and (has_copy or has_yes_no or has_footer) and state.get("lastLen", 0) > 200:
                if curr_hash == candidate_hash:
                    stable_ticks += 1
                else:
                    candidate_hash = curr_hash
                    stable_ticks = 1

                if stable_ticks >= 2:
                    save_completion_artifacts(state)
                    last_recorded_hash = curr_hash
                    print(
                        f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] "
                        f"🔔 Arena.ai completion detected (hasCopy={has_copy}, hasYesNo={has_yes_no}, "
                        f"len={state.get('lastLen')}, hash={curr_hash}) -> saved {LATEST_RAW_FILE.name}",
                        flush=True,
                    )
            else:
                stable_ticks = 0
        else:
            stable_ticks = 0

        await asyncio.sleep(poll_interval)


def main() -> None:
    parser = argparse.ArgumentParser(description="Arena.ai Completion Watcher & Instant Wakeup Daemon")
    parser.add_argument("--daemon", action="store_true", help="Run as a persistent always-on daemon")
    parser.add_argument("--wait", action="store_true", help="Wait for current/next Arena response to finish and exit 0 to wake up agent")
    parser.add_argument("--poll-interval", type=float, default=2.0, help="Polling interval in seconds")
    parser.add_argument("--timeout", type=float, default=1200.0, help="Timeout in seconds for --wait mode")
    args = parser.parse_args()

    if args.daemon:
        asyncio.run(run_persistent_daemon(poll_interval=args.poll_interval))
    else:
        rc = asyncio.run(run_wait_for_completion(poll_interval=args.poll_interval, timeout_s=args.timeout))
        sys.exit(rc)


if __name__ == "__main__":
    main()
