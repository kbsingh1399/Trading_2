"""
Terminal/zai_completion_daemon.py
Dedicated always-on and reactive wakeup completion watcher for Z.ai (GLM-5.3-Flash) via Chrome CDP (port 9222).

Monitors Z.ai conversation tabs, detects when GLM-5.3-Flash completes generating,
auto-harvests output and workspace files to:
  - docs/trade_plans/ZAI_LATEST_RAW.md
  - docs/trade_plans/ZAI_LATEST_ATTACHMENT.md
  - Data/zai_completion_status.json

Modes:
  --wait:   Waits for in-flight or next Z.ai response to complete, auto-harvests, and exits 0 (waking up Antigravity).
  --daemon: Runs persistently in the background (IsDaemon=true), harvesting every completed turn.
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
STATUS_FILE = ROOT / "Data" / "zai_completion_status.json"
LATEST_RAW_FILE = ROOT / "docs" / "trade_plans" / "ZAI_LATEST_RAW.md"
LATEST_ATTACHMENT_FILE = ROOT / "docs" / "trade_plans" / "ZAI_LATEST_ATTACHMENT.md"

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def find_zai_ws_url() -> str | None:
    try:
        raw = urllib.request.urlopen(CDP_URL, timeout=5).read().decode("utf-8")
        tabs = json.loads(raw)
        for t in tabs:
            if "chat.z.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl"):
                return t["webSocketDebuggerUrl"]
    except Exception:
        return None
    return None


async def probe_zai_state() -> dict:
    ws_url = find_zai_ws_url()
    if not ws_url:
        return {"connected": False, "error": "Z.ai tab not found on CDP 9222"}

    js = """(async () => {
        const stopBtn = document.querySelector('button[aria-label*="Stop"], button[title*="Stop"], button.stop-button');
        const stopSquare = document.querySelector('button span.size-3.rounded-xs');
        const sendBtn = document.querySelector('button#send-message-button');
        const thinkingBtn = Array.from(document.querySelectorAll('button')).find(b => (b.innerText || '').includes('Thinking'));
        const isGenerating = Boolean(stopBtn) || Boolean(stopSquare) || !sendBtn || Boolean(thinkingBtn);

        const allChatMsgs = Array.from(document.querySelectorAll('.chat-assistant.markdown-prose, .chat-assistant, .prose'));
        const proseCount = allChatMsgs.length;
        const lastProse = proseCount > 0 ? allChatMsgs[proseCount - 1] : null;
        const chatText = lastProse ? (lastProse.innerText || '').trim() : '';

        let workspaceFileName = '';
        let workspaceFileText = '';

        if (!isGenerating && lastProse) {
            const outer = lastProse.parentElement && lastProse.parentElement.parentElement ? lastProse.parentElement.parentElement : lastProse;
            const wroteBtns = Array.from(outer.querySelectorAll('button')).filter(b => (b.innerText || '').includes('Wrote') || (b.innerText || '').includes('Explored'));
            for (const wb of wroteBtns) {
                const container = wb.parentElement && wb.parentElement.parentElement ? wb.parentElement.parentElement : wb.parentElement;
                if (container && !container.querySelector('.ToolCallTraceList')) {
                    wb.click();
                    await new Promise(r => setTimeout(r, 200));
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
                    await new Promise(r => setTimeout(r, 400));
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
                "id": 1,
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
    return {"connected": False, "error": "Empty Z.ai CDP response"}


def save_zai_artifacts(state: dict) -> None:
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    LATEST_RAW_FILE.parent.mkdir(parents=True, exist_ok=True)

    text = state.get("lastText") or ""
    if text:
        LATEST_RAW_FILE.write_text(text, encoding="utf-8")

    ws_text = state.get("workspaceFileText") or ""
    ws_name = state.get("workspaceFileName") or ""
    if ws_text:
        LATEST_ATTACHMENT_FILE.write_text(ws_text, encoding="utf-8")
        if ws_name and ws_name.endswith(".md"):
            named_file = ROOT / "docs" / "trade_plans" / ws_name
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
        "latest_raw_path": str(LATEST_RAW_FILE),
        "latest_attachment_path": str(LATEST_ATTACHMENT_FILE) if ws_text else "",
    }
    STATUS_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")


async def run_wait(poll_interval: float = 2.0, timeout_s: float = 3600.0) -> int:
    start_ts = time.time()
    initial = await probe_zai_state()
    initial_hash = initial.get("textHash", "")
    saw_generating = initial.get("isGenerating", False)

    print(
        f"[ZaiWatcher] Started wait-for-completion watcher (connected={initial.get('connected')}, gen={saw_generating}, hash={initial_hash}, timeout={timeout_s}s)",
        flush=True
    )

    stable_ticks = 0
    last_seen_hash = initial_hash

    while (time.time() - start_ts) < timeout_s:
        await asyncio.sleep(poll_interval)
        state = await probe_zai_state()
        if not state.get("connected"):
            continue

        is_gen = state.get("isGenerating", False)
        if is_gen:
            saw_generating = True
            stable_ticks = 0
        else:
            curr_hash = state.get("textHash", "")
            last_len = state.get("lastLen", 0)
            is_new = saw_generating or (curr_hash != initial_hash and last_len > 200)

            if not is_gen and is_new and last_len > 200:
                if curr_hash == last_seen_hash and curr_hash != "":
                    stable_ticks += 1
                else:
                    last_seen_hash = curr_hash
                    stable_ticks = 1

                if stable_ticks >= 2:
                    save_zai_artifacts(state)
                    print(
                        f"\n🔔 Z.AI (GLM-5.3-Flash) RESPONSE COMPLETE (len={last_len}, hash={curr_hash}) -> saved {LATEST_RAW_FILE.name}",
                        flush=True
                    )
                    return 0
            else:
                last_seen_hash = curr_hash
                stable_ticks = 0

    print("[ZaiWatcher] Timeout reached while waiting for Z.ai completion.", file=sys.stderr, flush=True)
    return 1


async def run_daemon(poll_interval: float = 3.0) -> None:
    print("[ZaiDaemon] Persistent Z.ai (GLM-5.3-Flash) Completion Watcher Daemon started.", flush=True)
    last_recorded_hash = ""
    if STATUS_FILE.exists():
        try:
            last_recorded_hash = json.loads(STATUS_FILE.read_text(encoding="utf-8")).get("text_hash", "")
        except Exception:
            last_recorded_hash = ""

    stable_ticks = 0
    candidate_hash = ""

    while True:
        await asyncio.sleep(poll_interval)
        state = await probe_zai_state()
        if state.get("connected") and not state.get("isGenerating"):
            curr_hash = state.get("textHash", "")
            last_len = state.get("lastLen", 0)
            if curr_hash and curr_hash != last_recorded_hash and last_len > 200:
                if curr_hash == candidate_hash:
                    stable_ticks += 1
                else:
                    candidate_hash = curr_hash
                    stable_ticks = 1

                if stable_ticks >= 2:
                    save_zai_artifacts(state)
                    last_recorded_hash = curr_hash
                    print(
                        f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] "
                        f"🔔 Z.ai completion detected (len={last_len}, hash={curr_hash}) -> saved {LATEST_RAW_FILE.name}",
                        flush=True
                    )
            else:
                stable_ticks = 0
        else:
            stable_ticks = 0


def main():
    parser = argparse.ArgumentParser(description="Z.ai (GLM-5.3-Flash) Completion Watcher Daemon")
    parser.add_argument("--wait", action="store_true", help="Wait for active or next response to complete then exit 0")
    parser.add_argument("--daemon", action="store_true", help="Run as persistent background monitoring daemon")
    parser.add_argument("--probe", action="store_true", help="Probe current Z.ai state and exit")
    args = parser.parse_args()

    if args.probe:
        state = asyncio.run(probe_zai_state())
        print(json.dumps(state, indent=2))
        sys.exit(0)
    elif args.daemon:
        asyncio.run(run_daemon())
    else:
        # Default is --wait
        rc = asyncio.run(run_wait())
        sys.exit(rc)


if __name__ == "__main__":
    main()
