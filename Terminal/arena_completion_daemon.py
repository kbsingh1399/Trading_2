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
CDP_URL = "http://localhost:9222/json"
ARENA_AGENT_ID = "01a1311e-fda5-7fa9-9b2b-a0f35c05910e"
STATUS_FILE = ROOT / "Data" / "arena_completion_status.json"
LATEST_RAW_FILE = ROOT / "docs" / "trade_plans" / "ARENA_LATEST_RAW.md"
ZAI_STATUS_FILE = ROOT / "Data" / "zai_completion_status.json"
ZAI_LATEST_RAW_FILE = ROOT / "docs" / "trade_plans" / "ZAI_LATEST_RAW.md"

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


def _find_zai_ws_url() -> str | None:
    try:
        raw = urllib.request.urlopen(CDP_URL, timeout=5).read().decode("utf-8")
        tabs = json.loads(raw)
        for t in tabs:
            if "chat.z.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl"):
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
        const allProses = Array.from(document.querySelectorAll('.prose'));
        const proseCount = allProses.length;
        const nonEmptyProses = allProses.filter(e => (e.innerText || '').trim().length > 0);
        const lastProse = nonEmptyProses.length > 0 ? nonEmptyProses[nonEmptyProses.length - 1] : null;
        const lastText = lastProse ? (lastProse.innerText || '').trim() : '';
        const recentSnippets = nonEmptyProses.slice(-3).map(e => (e.innerText || '').trim().slice(0, 220));

        let turnEl = lastProse;
        for (let i = 0; i < 4 && turnEl && turnEl.parentElement; i++) {
            turnEl = turnEl.parentElement;
        }
        const hasCopyButton = Boolean(turnEl && turnEl.querySelector('button[aria-label="Copy"]'));
        const turnFooter = turnEl ? (turnEl.innerText || '').slice(-160) : '';
        const hasDurationFooter = /\\d+[ms]\\s*\\|\\s*(just now|\\d+[smh]\\s+ago)/i.test(turnFooter);

        const bodyText = document.body ? (document.body.innerText || '') : '';
        const hasKeepWorkingBtn = Array.from(document.querySelectorAll('button')).some(b => (b.innerText || '').trim() === 'Keep working');
        const hasYesNoBanner = bodyText.includes('Was this task successful?') || hasKeepWorkingBtn;

        return {
            connected: true,
            isGenerating,
            proseCount,
            nonEmptyProseCount: nonEmptyProses.length,
            lastLen: lastText.length,
            lastText,
            recentSnippets,
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


async def probe_zai_state() -> dict:
    ws_url = _find_zai_ws_url()
    if not ws_url:
        return {"connected": False, "error": "Z.ai tab not found on CDP 9222"}

    js = """(async () => {
        const stopBtn = document.querySelector('button[aria-label*="Stop"], button[title*="Stop"], button.stop-button');
        const stopSquare = document.querySelector('button span.size-3.rounded-xs');
        const sendBtn = document.querySelector('button#send-message-button');
        const thinkingBtn = Array.from(document.querySelectorAll('button')).find(b => (b.innerText || '').includes('Thinking'));
        const isGenerating = Boolean(stopBtn) || Boolean(stopSquare) || !sendBtn || Boolean(thinkingBtn);
        const allChatMsgs = Array.from(document.querySelectorAll('.chat-assistant.markdown-prose'));
        const proseCount = allChatMsgs.length;
        const lastProse = proseCount > 0 ? allChatMsgs[proseCount - 1] : null;
        const chatText = lastProse ? (lastProse.innerText || '').trim() : '';

        let workspaceFileName = '';
        let workspaceFileText = '';
        if (!isGenerating && lastProse) {
            const outer = lastProse.parentElement && lastProse.parentElement.parentElement ? lastProse.parentElement.parentElement : lastProse;
            const wroteBtns = Array.from(outer.querySelectorAll('button')).filter(b => (b.innerText || '').includes('Wrote'));
            for (const wb of wroteBtns) {
                const container = wb.parentElement && wb.parentElement.parentElement ? wb.parentElement.parentElement : wb.parentElement;
                if (container && !container.querySelector('.ToolCallTraceList')) {
                    wb.click();
                    await new Promise(r => setTimeout(r, 300));
                }
            }
            const createBtns = Array.from(outer.querySelectorAll('.ToolCallTraceList button, button')).filter(b => (b.innerText || '').includes('Create File') && (b.innerText || '').includes('.md'));
            if (createBtns.length > 0) {
                const latestCreateBtn = createBtns[createBtns.length - 1];
                const rawLabel = (latestCreateBtn.innerText || '').trim();
                const match = rawLabel.match(/([A-Za-z0-9_.-]+\\.md)/);
                const targetFile = match ? match[1] : '';
                const curHeader = Array.from(document.querySelectorAll('.text-sm.flex-1.truncate.line-clamp-1')).map(e => (e.innerText || '').trim()).find(t => t.endsWith('.md')) || '';
                if (targetFile && curHeader !== targetFile) {
                    latestCreateBtn.click();
                    await new Promise(r => setTimeout(r, 500));
                }
                if (targetFile) workspaceFileName = targetFile;
            }
            if (!workspaceFileName) {
                const curHeader = Array.from(document.querySelectorAll('.text-sm.flex-1.truncate.line-clamp-1')).map(e => (e.innerText || '').trim()).find(t => t.endsWith('.md')) || '';
                if (curHeader) workspaceFileName = curHeader;
            }
            const cm = document.querySelector('.cm-content');
            if (cm && cm.cmView) {
                let v = cm.cmView;
                while (v && !v.state && v.parent) v = v.parent;
                if (v && v.view && v.view.state) workspaceFileText = v.view.state.doc.toString();
                else if (v && v.state) workspaceFileText = v.state.doc.toString();
            }
            if (!workspaceFileText) {
                const wsProse = document.querySelector('.workspaceContent .markdown-prose, .workspace .markdown-prose, .workspaceContent pre');
                if (wsProse) {
                    workspaceFileText = (wsProse.innerText || '').trim();
                }
            }
        }
        const combined = workspaceFileText
            ? (chatText + "\\n\\n================================================================================\\nZ.AI ATTACHED OUTPUT FILE: " + workspaceFileName + " (" + workspaceFileText.length + " chars)\\n================================================================================\\n\\n" + workspaceFileText)
            : chatText;
        return {
            connected: true,
            isGenerating,
            proseCount,
            lastLen: combined.length,
            lastText: combined,
            workspaceFileName,
            workspaceFileLen: workspaceFileText.length,
            workspaceFileText
        };
    })()"""

    try:
        async with websockets.connect(ws_url, max_size=50_000_000, open_timeout=5, close_timeout=3) as ws:
            await ws.send(json.dumps({
                "id": 2,
                "method": "Runtime.evaluate",
                "params": {"expression": js, "returnByValue": True, "awaitPromise": True}
            }))
            resp = json.loads(await asyncio.wait_for(ws.recv(), timeout=10))
            val = resp.get("result", {}).get("result", {}).get("value")
            if isinstance(val, dict):
                text = val.get("lastText") or ""
                val["textHash"] = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16] if text else ""
                return val
    except Exception as e:
        return {"connected": False, "error": str(e)}
    return {"connected": False, "error": "Empty Z.ai CDP evaluation response"}



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


def save_zai_completion_artifacts(state: dict) -> None:
    ZAI_STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    ZAI_LATEST_RAW_FILE.parent.mkdir(parents=True, exist_ok=True)
    zai_attachment_file = ZAI_LATEST_RAW_FILE.parent / "ZAI_LATEST_ATTACHMENT.md"

    text = state.get("lastText") or ""
    if text:
        ZAI_LATEST_RAW_FILE.write_text(text, encoding="utf-8")

    ws_text = state.get("workspaceFileText") or ""
    ws_name = (state.get("workspaceFileName") or "").strip()
    if ws_text:
        zai_attachment_file.write_text(ws_text, encoding="utf-8")
        if ws_name and ws_name.endswith(".md") and "/" not in ws_name and "\\" not in ws_name:
            named_file = ZAI_LATEST_RAW_FILE.parent / ws_name
            named_file.write_text(ws_text, encoding="utf-8")

    payload = {
        "completed_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "completed_at_epoch": time.time(),
        "prose_count": state.get("proseCount", 0),
        "text_length": state.get("lastLen", 0),
        "workspace_file_name": ws_name,
        "workspace_file_length": state.get("workspaceFileLen", 0),
        "text_hash": state.get("textHash", ""),
        "is_generating": state.get("isGenerating", False),
        "latest_raw_path": str(ZAI_LATEST_RAW_FILE),
        "latest_attachment_path": str(zai_attachment_file) if ws_text else "",
    }
    ZAI_STATUS_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")


async def run_wait_for_completion(poll_interval: float = 2.0, timeout_s: float = 1800.0) -> int:
    start_ts = time.time()
    initial = await probe_arena_state()
    initial_hash = initial.get("textHash", "")
    initial_generating = initial.get("isGenerating", False)
    saw_generating = initial_generating

    initial_zai = await probe_zai_state()
    zai_active = initial_zai.get("connected", False)
    initial_zai_hash = initial_zai.get("textHash", "")
    initial_zai_count = initial_zai.get("proseCount", 0)
    saw_zai_generating = initial_zai.get("isGenerating", False)

    print(
        f"[TriCouncilWatcher] Started wait-for-completion watcher "
        f"(Arena: gen={initial_generating}, hash={initial_hash}, prose={initial.get('proseCount')} | "
        f"Z.ai: connected={zai_active}, gen={saw_zai_generating}, hash={initial_zai_hash}, prose={initial_zai_count})",
        flush=True,
    )

    stable_ready_ticks = 0
    last_seen_hash = initial_hash
    arena_done = False
    arena_done_ts = 0.0

    zai_stable_ticks = 0
    last_seen_zai_hash = initial_zai_hash
    zai_done = not zai_active

    while (time.time() - start_ts) < timeout_s:
        await asyncio.sleep(poll_interval)

        # 1. Check Arena.ai
        if not arena_done:
            state = await probe_arena_state()
            if state.get("connected"):
                is_gen = state.get("isGenerating", False)
                if is_gen:
                    saw_generating = True
                    stable_ready_ticks = 0
                else:
                    curr_hash = state.get("textHash", "")
                    has_copy = state.get("hasCopyButton", False)
                    has_yes_no = state.get("hasYesNoBanner", False)
                    has_footer = state.get("hasDurationFooter", False)
                    last_len = state.get("lastLen", 0)
                    is_new_or_finished = (
                        saw_generating
                        or (curr_hash != initial_hash and last_len > 200)
                        or ((time.time() - start_ts) >= 8.0 and (has_copy or has_yes_no) and last_len > 200)
                    )
                    if not is_gen and (has_copy or has_yes_no or has_footer) and is_new_or_finished:
                        if curr_hash == last_seen_hash and curr_hash != "":
                            stable_ready_ticks += 1
                        else:
                            last_seen_hash = curr_hash
                            stable_ready_ticks = 1
                        if stable_ready_ticks >= 2:
                            save_completion_artifacts(state)
                            arena_done = True
                            arena_done_ts = time.time()
                            print(
                                f"\n🔔 ARENA.AI RESPONSE COMPLETE (len={last_len}, hash={curr_hash}) -> saved {LATEST_RAW_FILE.name}",
                                flush=True,
                            )
                    else:
                        last_seen_hash = curr_hash
                        stable_ready_ticks = 0

        # 2. Check Z.ai Chat (One-Way DOM Harvest + Attached Workspace Deliverable)
        if zai_active and not zai_done:
            zstate = await probe_zai_state()
            if zstate.get("connected"):
                z_gen = zstate.get("isGenerating", False)
                if z_gen:
                    saw_zai_generating = True
                    zai_stable_ticks = 0
                else:
                    z_hash = zstate.get("textHash", "")
                    z_len = zstate.get("lastLen", 0)
                    z_count = zstate.get("proseCount", 0)
                    z_is_new = saw_zai_generating or (z_hash != initial_zai_hash and z_len > 200) or (z_count > initial_zai_count and z_len > 200)
                    if not z_gen and z_is_new and z_len > 200:
                        if z_hash == last_seen_zai_hash and z_hash != "":
                            zai_stable_ticks += 1
                        else:
                            last_seen_zai_hash = z_hash
                            zai_stable_ticks = 1
                        if zai_stable_ticks >= 3:
                            save_zai_completion_artifacts(zstate)
                            zai_done = True
                            print(
                                f"\n🔔 Z.AI CHAT RESPONSE COMPLETE (len={z_len}, ws_file={zstate.get('workspaceFileName')}, ws_len={zstate.get('workspaceFileLen')}, hash={z_hash}) -> saved {ZAI_LATEST_RAW_FILE.name}",
                                flush=True,
                            )

        # Wake up when BOTH are done (or if Z.ai never started generating within 60s, or exceeded 720s grace timeout)
        zai_grace_limit = 720.0 if saw_zai_generating else 60.0
        if arena_done and (zai_done or (time.time() - arena_done_ts) >= zai_grace_limit):
            if zai_active and not zai_done:
                zstate = await probe_zai_state()
                if zstate.get("connected") and zstate.get("lastLen", 0) > 100:
                    save_zai_completion_artifacts(zstate)
                    print(f"[TriCouncilWatcher] Saved partial/latest Z.ai snapshot ({zstate.get('lastLen')} chars) at grace timeout.", flush=True)
            print("\n✅ TRI-COUNCIL WAKE UP TRIGGERED (Arena.ai + Z.ai Chat ready for Antigravity synthesis)!", flush=True)
            return 0

    print("[TriCouncilWatcher] Timeout reached while waiting for council completion.", file=sys.stderr, flush=True)
    return 1


async def run_persistent_daemon(poll_interval: float = 3.0) -> None:
    print("[ArenaDaemon] Persistent Tri-Council (Arena.ai + Z.ai) Completion Watcher Daemon started.", flush=True)
    last_recorded_hash = ""
    if STATUS_FILE.exists():
        try:
            last_recorded_hash = json.loads(STATUS_FILE.read_text(encoding="utf-8")).get("text_hash", "")
        except Exception:
            last_recorded_hash = ""

    last_recorded_zai_hash = ""
    if ZAI_STATUS_FILE.exists():
        try:
            last_recorded_zai_hash = json.loads(ZAI_STATUS_FILE.read_text(encoding="utf-8")).get("text_hash", "")
        except Exception:
            last_recorded_zai_hash = ""

    stable_ticks = 0
    candidate_hash = ""
    zai_stable_ticks = 0
    zai_candidate_hash = ""

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
                        f"🔔 Arena.ai completion detected (len={state.get('lastLen')}, hash={curr_hash}) -> saved {LATEST_RAW_FILE.name}",
                        flush=True,
                    )
            else:
                stable_ticks = 0
        else:
            stable_ticks = 0

        zstate = await probe_zai_state()
        if zstate.get("connected") and not zstate.get("isGenerating"):
            z_hash = zstate.get("textHash", "")
            if z_hash and z_hash != last_recorded_zai_hash and zstate.get("lastLen", 0) > 200:
                if z_hash == zai_candidate_hash:
                    zai_stable_ticks += 1
                else:
                    zai_candidate_hash = z_hash
                    zai_stable_ticks = 1
                if zai_stable_ticks >= 3:
                    save_zai_completion_artifacts(zstate)
                    last_recorded_zai_hash = z_hash
                    print(
                        f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] "
                        f"🔔 Z.ai Chat completion detected (len={zstate.get('lastLen')}, hash={z_hash}) -> saved {ZAI_LATEST_RAW_FILE.name}",
                        flush=True,
                    )
            else:
                zai_stable_ticks = 0
        else:
            zai_stable_ticks = 0

        await asyncio.sleep(poll_interval)


def main() -> None:
    parser = argparse.ArgumentParser(description="Tri-Council (Arena.ai + Z.ai Chat) Completion Watcher & Instant Wakeup Daemon")
    parser.add_argument("--daemon", action="store_true", help="Run as a persistent always-on daemon")
    parser.add_argument("--wait", action="store_true", help="Wait for current/next Arena + Z.ai response to finish and exit 0 to wake up agent")
    parser.add_argument("--poll-interval", type=float, default=2.0, help="Polling interval in seconds")
    parser.add_argument("--timeout", type=float, default=1800.0, help="Timeout in seconds for --wait mode")
    args = parser.parse_args()

    if args.daemon:
        asyncio.run(run_persistent_daemon(poll_interval=args.poll_interval))
    else:
        rc = asyncio.run(run_wait_for_completion(poll_interval=args.poll_interval, timeout_s=args.timeout))
        sys.exit(rc)


if __name__ == "__main__":
    main()

