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
ARENA_AGENT_ID = "01a1311e-fda5-7fa9-9b2b-a0f35c05910e"
STATUS_FILE = ROOT / "Data" / "arena_completion_status.json"
LATEST_RAW_FILE = ROOT / "docs" / "trade_plans" / "ARENA_LATEST_RAW.md"

ARENA_FABLE_STATUS_FILE = ROOT / "Data" / "arena_fable_completion_status.json"
ARENA_FABLE_RAW_FILE = ROOT / "docs" / "trade_plans" / "ARENA_FABLE_LATEST_RAW.md"

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
            u = t.get("url", "")
            if ("arena.ai/agent" in u or "arena.ai" in u) and t.get("webSocketDebuggerUrl"):
                return t["webSocketDebuggerUrl"]
    except Exception:
        return None
    return None


def _find_arena_fable_ws_url() -> str | None:
    try:
        raw = urllib.request.urlopen(CDP_URL, timeout=5).read().decode("utf-8")
        tabs = json.loads(raw)
        for t in tabs:
            u = t.get("url", "")
            if ("01a16dcd" in u or "01a13c34-09c6" in u or "01a13bea" in u or "01a13b4a" in u or "01a1311e" in u or "01a13a13" in u or "af999588" in u) and t.get("webSocketDebuggerUrl"):
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


async def reload_arena_tab(target: str = "arena1") -> None:
    """Reloads the Arena tab via CDP Page.reload and waits for full DOM rehydration."""
    try:
        ws_url = _find_arena_ws_url() if target == "arena1" else _find_arena_fable_ws_url()
        if not ws_url:
            return
        async with websockets.connect(ws_url, open_timeout=5) as ws:
            await ws.send(json.dumps({"id": 9999, "method": "Page.reload", "params": {"ignoreCache": True}}))
            try:
                await asyncio.wait_for(ws.recv(), timeout=2.5)
            except Exception:
                pass
        await asyncio.sleep(4.0)
        print(f"[CouncilWatcher] Successfully refreshed {target} tab via CDP Page.reload", flush=True)
    except Exception as e:
        print(f"[CouncilWatcher] Error reloading {target} tab: {e}", file=sys.stderr)


async def reload_zai_tab() -> None:
    """Reloads the Z.ai tab via CDP Page.reload and waits for full DOM rehydration."""
    try:
        ws_url = _find_zai_ws_url()
        if not ws_url:
            return
        async with websockets.connect(ws_url, open_timeout=5) as ws:
            await ws.send(json.dumps({"id": 9998, "method": "Page.reload", "params": {"ignoreCache": True}}))
            try:
                await asyncio.wait_for(ws.recv(), timeout=2.5)
            except Exception:
                pass
        await asyncio.sleep(4.0)
        print(f"[CouncilWatcher] Successfully refreshed Z.ai tab via CDP Page.reload", flush=True)
    except Exception as e:
        print(f"[CouncilWatcher] Error reloading Z.ai tab: {e}", file=sys.stderr)


async def probe_arena_state(target: str = "arena1") -> dict:
    ws_url = _find_arena_ws_url() if target == "arena1" else _find_arena_fable_ws_url()
    if not ws_url:
        return {"connected": False, "error": f"{target} tab not found on CDP 9222"}

    js = """(() => {
        function nodeToMd(node) {
            if (!node) return '';
            if (node.nodeType === Node.TEXT_NODE) return node.textContent;
            if (node.nodeType !== Node.ELEMENT_NODE) return '';

            const tag = node.tagName.toLowerCase();
            if (tag === 'pre') {
                const code = node.querySelector('code');
                const lang = code ? (code.className.match(/language-(\\\\w+)/) || ['', ''])[1] : '';
                return '\\\\n```' + lang + '\\\\n' + (code ? code.innerText : node.innerText) + '\\\\n```\\\\n';
            }
            if (tag === 'code' && node.parentElement.tagName.toLowerCase() !== 'pre') return '`' + node.innerText + '`';
            if (tag === 'h1') return '\\\\n# ' + node.innerText.trim() + '\\\\n\\\\n';
            if (tag === 'h2') return '\\\\n## ' + node.innerText.trim() + '\\\\n\\\\n';
            if (tag === 'h3') return '\\\\n### ' + node.innerText.trim() + '\\\\n\\\\n';
            if (tag === 'h4') return '\\\\n#### ' + node.innerText.trim() + '\\\\n\\\\n';
            if (tag === 'p') return '\\\\n' + Array.from(node.childNodes).map(nodeToMd).join('').trim() + '\\\\n';
            if (tag === 'br') return '\\\\n';
            if (tag === 'hr') return '\\\\n---\\\\n';
            if (tag === 'ul') return '\\\\n' + Array.from(node.children).map(li => '- ' + nodeToMd(li).trim()).join('\\\\n') + '\\\\n';
            if (tag === 'ol') return '\\\\n' + Array.from(node.children).map((li, idx) => (idx + 1) + '. ' + nodeToMd(li).trim()).join('\\\\n') + '\\\\n';
            if (tag === 'li') return Array.from(node.childNodes).map(nodeToMd).join('').trim();
            if (tag === 'strong' || tag === 'b') return '**' + Array.from(node.childNodes).map(nodeToMd).join('') + '**';
            if (tag === 'em' || tag === 'i') return '*' + Array.from(node.childNodes).map(nodeToMd).join('') + '*';
            if (tag === 'table') {
                const rows = Array.from(node.querySelectorAll('tr'));
                if (rows.length === 0) return '';
                const lines = [];
                let isHeader = true;
                for (const r of rows) {
                    const cells = Array.from(r.querySelectorAll('th, td')).map(c => nodeToMd(c).replace(/\\\\n/g, ' ').trim());
                    lines.push('| ' + cells.join(' | ') + ' |');
                    if (isHeader) {
                        lines.push('| ' + cells.map(() => '---').join(' | ') + ' |');
                        isHeader = false;
                    }
                }
                return '\\\\n' + lines.join('\\\\n') + '\\\\n\\\\n';
            }
            return Array.from(node.childNodes).map(nodeToMd).join('');
        }

        // Enhanced stop button detection matching exact live DOM
        const btnStop = document.querySelector('button[aria-label="Stop generating"], button:has(svg rect), button[aria-label*="Stop"], button[title*="Stop"], button.stop-button');
        const isGenerating = Boolean(btnStop);
        const allProses = Array.from(document.querySelectorAll('.prose'));
        const proseCount = allProses.length;
        const nonEmptyProses = allProses.filter(e => (e.innerText || '').trim().length > 0);
        const lastProse = nonEmptyProses.length > 0 ? nonEmptyProses[nonEmptyProses.length - 1] : null;
        const lastText = lastProse ? nodeToMd(lastProse).trim() : '';
        const recentSnippets = nonEmptyProses.slice(-3).map(e => (e.innerText || '').trim().slice(0, 220));

        let turnEl = lastProse;
        for (let i = 0; i < 4 && turnEl && turnEl.parentElement; i++) {
            turnEl = turnEl.parentElement;
        }
        const hasCopyButton = Boolean(turnEl && turnEl.querySelector('button[aria-label="Copy"]'));
        const turnFooter = turnEl ? (turnEl.innerText || '').slice(-160) : '';
        const hasDurationFooter = /\\\\d+[ms]\\\\s*\\\\|\\\\s*(just now|\\\\d+[smh]\\\\s+ago)/i.test(turnFooter);

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

    js = """(() => {
        const stopBtn = document.querySelector('button[aria-label*="Stop"], button[title*="Stop"], button.stop-button, button:has(span.size-3.rounded-xs), button:has(span.block.size-3)');
        const stopSquare = document.querySelector('button span.size-3.rounded-xs, button span.block.size-3');
        const sendBtn = document.querySelector('button#send-message-button, button[aria-label="Send"], button[aria-label*="Send"]');
        const thinkingBtn = Array.from(document.querySelectorAll('button, div, span')).find(b => (b.innerText || '').trim().startsWith('Thinking'));
        const isGenerating = Boolean(stopBtn) || Boolean(stopSquare) || !sendBtn || Boolean(thinkingBtn);
        const allChatMsgs = Array.from(document.querySelectorAll('.chat-assistant.markdown-prose'));
        const proseCount = allChatMsgs.length;
        const lastProse = proseCount > 0 ? allChatMsgs[proseCount - 1] : null;
        const chatText = lastProse ? (lastProse.innerText || '').trim() : '';

        let workspaceFileName = '';
        let workspaceFileText = '';
        const curHeader = Array.from(document.querySelectorAll('.text-sm.flex-1.truncate.line-clamp-1')).map(e => (e.innerText || '').trim()).find(t => t.endsWith('.md')) || '';
        if (curHeader) workspaceFileName = curHeader;
        
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
                "params": {"expression": js, "returnByValue": True}
            }))
            resp = json.loads(await asyncio.wait_for(ws.recv(), timeout=10))
            if "error" in resp:
                return {"connected": False, "error": str(resp["error"])}
            res_obj = resp.get("result", {})
            if "exceptionDetails" in res_obj:
                return {"connected": False, "error": f"JS Exception: {res_obj['exceptionDetails']}"}
            val = res_obj.get("result", {}).get("value")
            if isinstance(val, dict):
                text = val.get("lastText") or ""
                val["textHash"] = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16] if text else ""
                return val
            return {"connected": False, "error": f"Unexpected value: {type(val)} {str(val)[:200]}"}
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


def save_arena_fable_completion_artifacts(state: dict) -> None:
    ARENA_FABLE_STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    ARENA_FABLE_RAW_FILE.parent.mkdir(parents=True, exist_ok=True)

    text = state.get("lastText") or ""
    if text:
        ARENA_FABLE_RAW_FILE.write_text(text, encoding="utf-8")

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
        "latest_raw_path": str(ARENA_FABLE_RAW_FILE),
    }
    ARENA_FABLE_STATUS_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")


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


async def run_wait_for_completion(poll_interval: float = 2.0, timeout_s: float = 1800.0, refresh_limit_s: float = 300.0) -> int:
    start_ts = time.time()
    
    # Independent State Tracking & Timers
    arena_gen_start: float = 0.0
    zai_gen_start: float = 0.0
    arena_last_refresh: float = time.time()
    zai_last_refresh: float = time.time()
    
    stable_arena_ticks: int = 0
    stable_zai_ticks: int = 0
    
    last_arena_hash: str = ""
    last_zai_hash: str = ""
    astate: dict = {}
    zstate: dict = {}
    
    # Initial Probe
    init_a = await probe_arena_state("arena1")
    init_z = await probe_zai_state()
    
    arena_active = init_a.get("connected", False)
    zai_active = init_z.get("connected", False)
    
    arena_done = False
    zai_done = not zai_active  # If not connected, mark done immediately
    
    if init_a.get("isGenerating"):
        arena_gen_start = time.time()
    else:
        # If Arena already finished a turn before script started, save it as baseline
        if init_a.get("lastLen", 0) > 100 and (init_a.get("hasCopyButton") or init_a.get("hasYesNoBanner")):
            arena_done = True
            last_arena_hash = init_a.get("textHash", "")
            
    if init_z.get("isGenerating"):
        zai_gen_start = time.time()
        zai_done = False
    else:
        if init_z.get("lastLen", 0) > 100:
            zai_done = True
            last_zai_hash = init_z.get("textHash", "")

    print(
        f"[DualCouncilWatcher] Initialized: Arena (connected={arena_active}, gen={init_a.get('isGenerating')}, done={arena_done}) | "
        f"Z.ai (connected={zai_active}, gen={init_z.get('isGenerating')}, done={zai_done}) | "
        f"Auto-refresh threshold: {refresh_limit_s}s (5 minutes)",
        flush=True,
    )

    last_log_ts = time.time()

    while (time.time() - start_ts) < timeout_s:
        await asyncio.sleep(poll_interval)
        now = time.time()
        elapsed = int(now - start_ts)

        # -------------------------------------------------------------
        # 1. EVALUATE ARENA.AI
        # -------------------------------------------------------------
        if arena_active:
            astate = await probe_arena_state("arena1")
            if astate.get("connected"):
                is_a_gen = astate.get("isGenerating", False)
                a_hash = astate.get("textHash", "")
                a_len = astate.get("lastLen", 0)
                
                if is_a_gen:
                    if arena_gen_start == 0.0:
                        arena_gen_start = now
                    arena_done = False  # NEVER done while actively generating!
                    stable_arena_ticks = 0
                    
                    # Generation ongoing
                    pass
                else:
                    arena_gen_start = 0.0
                    has_copy = astate.get("hasCopyButton", False)
                    has_yes_no = astate.get("hasYesNoBanner", False)
                    has_footer = astate.get("hasDurationFooter", False)
                    
                    # Ready when generation stop button is gone and output exists
                    if a_len > 100 and (has_copy or has_yes_no or has_footer or not arena_done):
                        if a_hash == last_arena_hash and a_hash != "":
                            stable_arena_ticks += 1
                        else:
                            last_arena_hash = a_hash
                            stable_arena_ticks = 1
                            
                        if stable_arena_ticks >= 2:
                            save_completion_artifacts(astate)
                            arena_done = True
                    else:
                        stable_arena_ticks = 0

            # Operator Mandate: Auto-refresh Arena tab every 5 minutes until completed (only if generating for >= refresh_limit_s)
            gen_dur = (now - arena_gen_start) if arena_gen_start > 0 else 0.0
            if is_a_gen and gen_dur >= refresh_limit_s and (now - arena_last_refresh) >= refresh_limit_s:
                print(f"[DualCouncilWatcher] ⏱️ 5-Minute milestone reached without Arena completion -> Triggering CDP Page.reload refresh!", flush=True)
                await reload_arena_tab("arena1")
                arena_last_refresh = now
                arena_gen_start = now

        # -------------------------------------------------------------
        # 2. EVALUATE Z.AI
        # -------------------------------------------------------------
        if zai_active:
            zstate = await probe_zai_state()
            if zstate.get("connected"):
                is_z_gen = zstate.get("isGenerating", False)
                z_hash = zstate.get("textHash", "")
                z_len = zstate.get("lastLen", 0)
                
                if is_z_gen:
                    if zai_gen_start == 0.0:
                        zai_gen_start = now
                    zai_done = False  # NEVER done while actively generating!
                    stable_zai_ticks = 0
                    
                    # Generation ongoing
                    pass
                else:
                    zai_gen_start = 0.0
                    if z_len > 100:
                        if z_hash == last_zai_hash and z_hash != "":
                            stable_zai_ticks += 1
                        else:
                            last_zai_hash = z_hash
                            stable_zai_ticks = 1
                            
                        if stable_zai_ticks >= 2:
                            save_zai_completion_artifacts(zstate)
                            zai_done = True
                    else:
                        stable_zai_ticks = 0

            # Operator Mandate: Auto-refresh Z.ai tab every 5 minutes until completed (only if generating for >= refresh_limit_s)
            z_dur = (now - zai_gen_start) if zai_gen_start > 0 else 0.0
            if is_z_gen and z_dur >= refresh_limit_s and (now - zai_last_refresh) >= refresh_limit_s:
                print(f"[DualCouncilWatcher] ⏱️ 5-Minute milestone reached without Z.ai completion -> Triggering CDP Page.reload refresh!", flush=True)
                await reload_zai_tab()
                zai_last_refresh = now
                zai_gen_start = now

        # Periodic status logging every 10 seconds
        if now - last_log_ts >= 10.0:
            last_log_ts = now
            a_desc = f"GENERATING ({int(now - arena_gen_start)}s)" if astate.get("isGenerating") else ("COMPLETED" if arena_done else "IDLE")
            z_desc = f"GENERATING ({int(now - zai_gen_start)}s)" if zstate.get("isGenerating") else ("COMPLETED" if zai_done else "IDLE")
            print(f"[DualCouncilWatcher t={elapsed}s] Arena.ai: {a_desc} | Z.ai: {z_desc}", flush=True)

        # -------------------------------------------------------------
        # 3. CONVERGENCE CHECK: BOTH MUST BE DONE & NEITHER GENERATING
        # -------------------------------------------------------------
        a_is_still_working = astate.get("isGenerating", False) if arena_active and 'astate' in locals() else False
        z_is_still_working = zstate.get("isGenerating", False) if zai_active and 'zstate' in locals() else False

        if arena_done and zai_done and not a_is_still_working and not z_is_still_working:
            print("\n🎉 DUAL COUNCIL WAKE UP TRIGGERED: Both Arena.ai and Z.ai have finished and artifacts are harvested!", flush=True)
            return 0

    print("[DualCouncilWatcher] Timeout reached waiting for council completion.", file=sys.stderr, flush=True)
    return 1
    return 1


async def run_persistent_daemon(poll_interval: float = 3.0, refresh_limit_s: float = 300.0) -> None:
    print(f"[ArenaDaemon] Persistent Tri-Council Completion Watcher Daemon started (Auto-refresh watchdog: {refresh_limit_s}s / 5m).", flush=True)
    arena_gen_start: float = 0.0
    arena_last_refresh: float = time.time()
    zai_gen_start: float = 0.0
    zai_last_refresh: float = time.time()
    last_recorded_hash = ""
    if STATUS_FILE.exists():
        try:
            last_recorded_hash = json.loads(STATUS_FILE.read_text(encoding="utf-8")).get("text_hash", "")
        except Exception:
            last_recorded_hash = ""

    last_recorded_fable_hash = ""
    if ARENA_FABLE_STATUS_FILE.exists():
        try:
            last_recorded_fable_hash = json.loads(ARENA_FABLE_STATUS_FILE.read_text(encoding="utf-8")).get("text_hash", "")
        except Exception:
            last_recorded_fable_hash = ""

    last_recorded_zai_hash = ""
    if ZAI_STATUS_FILE.exists():
        try:
            last_recorded_zai_hash = json.loads(ZAI_STATUS_FILE.read_text(encoding="utf-8")).get("text_hash", "")
        except Exception:
            last_recorded_zai_hash = ""

    stable_ticks = 0
    candidate_hash = ""
    fable_stable_ticks = 0
    candidate_fable_hash = ""
    zai_stable_ticks = 0
    zai_candidate_hash = ""

    while True:
        now = time.time()

        # 1. Check Arena 1 Primary & Auto-Refresh Watchdog
        state = await probe_arena_state("arena1")
        if state.get("connected"):
            if state.get("isGenerating"):
                if arena_gen_start == 0.0:
                    arena_gen_start = now
                stable_ticks = 0
                gen_duration = now - arena_gen_start
                if gen_duration >= refresh_limit_s and (now - arena_last_refresh) >= refresh_limit_s:
                    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] ⚠️ Arena has been generating for {int(gen_duration)}s (>= 5m) -> Triggering CDP Page.reload refresh!", flush=True)
                    await reload_arena_tab("arena1")
                    arena_last_refresh = now
                    arena_gen_start = now
            else:
                arena_gen_start = 0.0
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
                        last_recorded_hash = state.get("textHash", curr_hash)
                        print(
                            f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] "
                            f"🔔 Arena 1 Primary completion detected (len={state.get('lastLen')}, hash={last_recorded_hash}) -> saved {LATEST_RAW_FILE.name}",
                            flush=True,
                        )
                else:
                    stable_ticks = 0
        else:
            stable_ticks = 0

        # 2. Check Arena 2 Fable Orchestrator
        fstate = await probe_arena_state("fable")
        if fstate.get("connected") and not fstate.get("isGenerating"):
            f_hash = fstate.get("textHash", "")
            f_has_copy = fstate.get("hasCopyButton", False)
            f_has_yes_no = fstate.get("hasYesNoBanner", False)
            f_has_footer = fstate.get("hasDurationFooter", False)

            if f_hash and f_hash != last_recorded_fable_hash and (f_has_copy or f_has_yes_no or f_has_footer) and fstate.get("lastLen", 0) > 200:
                if f_hash == candidate_fable_hash:
                    fable_stable_ticks += 1
                else:
                    candidate_fable_hash = f_hash
                    fable_stable_ticks = 1

                if fable_stable_ticks >= 2:
                    save_arena_fable_completion_artifacts(fstate)
                    last_recorded_fable_hash = f_hash
                    print(
                        f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] "
                        f"🔔 Arena 2 Fable Orchestrator completion detected (len={fstate.get('lastLen')}, hash={f_hash}) -> saved {ARENA_FABLE_RAW_FILE.name}",
                        flush=True,
                    )
            else:
                fable_stable_ticks = 0
        else:
            fable_stable_ticks = 0

        # 3. Check Z.ai Chat & Auto-Refresh Watchdog
        zstate = await probe_zai_state()
        if zstate.get("connected"):
            if zstate.get("isGenerating"):
                if zai_gen_start == 0.0:
                    zai_gen_start = now
                zai_stable_ticks = 0
                z_gen_duration = now - zai_gen_start
                if z_gen_duration >= refresh_limit_s and (now - zai_last_refresh) >= refresh_limit_s:
                    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] ⚠️ Z.ai has been generating for {int(z_gen_duration)}s (>= 5m) -> Triggering CDP Page.reload refresh!", flush=True)
                    await reload_zai_tab()
                    zai_last_refresh = now
                    zai_gen_start = now
            else:
                zai_gen_start = 0.0
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
    parser.add_argument("--refresh-limit", type=float, default=300.0, help="Seconds before auto-refreshing a tab that remains generating (default 300s / 5m)")
    args = parser.parse_args()

    if args.daemon:
        asyncio.run(run_persistent_daemon(poll_interval=args.poll_interval, refresh_limit_s=args.refresh_limit))
    else:
        rc = asyncio.run(run_wait_for_completion(poll_interval=args.poll_interval, timeout_s=args.timeout, refresh_limit_s=args.refresh_limit))
        sys.exit(rc)


if __name__ == "__main__":
    main()

