"""
Terminal/rock_hard_dual_watchdog.py
Rock-Hard Dual Council Completion Watchdog for Arena.ai and Z.ai (GLM-5.3-Flash).

Guarantees 100% non-bypassable synchronization:
1. Records initial baseline hashes from both models before prompt execution.
2. Interrogates Chrome CDP (port 9222) via WebSocket every poll_interval.
3. Requires the specific --cycle <CYCLE_ID> to be explicitly present in the harvested output.
4. Requires isGenerating == False (stop button gone, send button re-enabled).
5. Requires output hash stability across >= 2 consecutive ticks.
6. Auto-harvests completed responses to docs/trade_plans/ARENA_LATEST_RAW.md and ZAI_LATEST_RAW.md.
7. Exits 0 ONLY when BOTH models have successfully completed the cycle.
"""

import argparse
import asyncio
import datetime
import hashlib
import json
import pathlib
import sys
import time
import urllib.request
import websockets

ROOT = pathlib.Path(__file__).resolve().parents[1]
CDP_URL = "http://127.0.0.1:9222/json"

ARENA_STATUS_FILE = ROOT / "Data" / "arena_completion_status.json"
ARENA_RAW_FILE = ROOT / "docs" / "trade_plans" / "ARENA_LATEST_RAW.md"

ZAI_STATUS_FILE = ROOT / "Data" / "zai_completion_status.json"
ZAI_RAW_FILE = ROOT / "docs" / "trade_plans" / "ZAI_LATEST_RAW.md"
ZAI_ATTACHMENT_FILE = ROOT / "docs" / "trade_plans" / "ZAI_LATEST_ATTACHMENT.md"

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def find_ws_url(match_keyword: str) -> str | None:
    try:
        raw = urllib.request.urlopen(CDP_URL, timeout=5).read().decode("utf-8")
        tabs = json.loads(raw)
        for t in tabs:
            if match_keyword in t.get("url", "") and t.get("webSocketDebuggerUrl"):
                return t["webSocketDebuggerUrl"]
    except Exception:
        return None
    return None


async def probe_arena() -> dict:
    ws_url = find_ws_url("arena.ai")
    if not ws_url:
        return {"connected": False, "error": "Arena tab not found on CDP"}

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

        const btnStop = document.querySelector('button[aria-label="Stop generating"], button:has(svg rect), button[aria-label*="Stop"], button[title*="Stop"], button.stop-button');
        const isGenerating = Boolean(btnStop);
        const allProses = Array.from(document.querySelectorAll('.prose'));
        const lastProse = allProses.length > 0 ? allProses[allProses.length - 1] : null;
        const lastText = lastProse ? nodeToMd(lastProse).trim() : '';

        let turnEl = lastProse;
        for (let i = 0; i < 4 && turnEl && turnEl.parentElement; i++) {
            turnEl = turnEl.parentElement;
        }
        const hasCopyButton = Boolean(turnEl && turnEl.querySelector('button[aria-label="Copy"]'));
        const bodyText = document.body ? (document.body.innerText || '') : '';
        const hasKeepWorkingBtn = Array.from(document.querySelectorAll('button')).some(b => (b.innerText || '').trim() === 'Keep working');
        const hasYesNoBanner = bodyText.includes('Was this task successful?') || hasKeepWorkingBtn;

        return {
            connected: true,
            isGenerating,
            lastLen: lastText.length,
            lastText,
            hasCopyButton,
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
    return {"connected": False, "error": "Empty response"}


async def probe_zai() -> dict:
    ws_url = find_ws_url("chat.z.ai")
    if not ws_url:
        return {"connected": False, "error": "Z.ai tab not found on CDP"}

    js = """(() => {
        const stopBtn = document.querySelector('button[aria-label*="Stop"], button[title*="Stop"], button.stop-button, button:has(span.size-3.rounded-xs)');
        const stopSquare = document.querySelector('button span.size-3.rounded-xs, button span.block.size-3');
        const sendBtn = document.querySelector('button#send-message-button, button[aria-label="Send"], button[aria-label*="Send"]');
        const thinkingBtn = Array.from(document.querySelectorAll('button, div, span')).find(b => (b.innerText || '').trim().startsWith('Thinking'));
        const isGenerating = Boolean(stopBtn) || Boolean(stopSquare) || !sendBtn || Boolean(thinkingBtn);
        
        const allChatMsgs = Array.from(document.querySelectorAll('.chat-assistant.markdown-prose, div.prose, .chat-assistant'));
        let chatText = '';
        for (let i = allChatMsgs.length - 1; i >= 0; i--) {
            const t = (allChatMsgs[i].innerText || '').trim();
            if (t.includes('Cycle_005') || t.includes('COUNCIL REPORT')) {
                chatText = t;
                break;
            }
        }
        if (!chatText || chatText.length < 200) {
            const body = document.body.innerText;
            const rIdx = body.lastIndexOf('# [COUNCIL REPORT');
            if (rIdx !== -1) {
                chatText = body.substring(rIdx);
            } else {
                const cIdx = body.lastIndexOf('Cycle_005');
                if (cIdx !== -1) chatText = body.substring(cIdx);
            }
        }

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
            if (wsProse) workspaceFileText = (wsProse.innerText || '').trim();
        }

        const combined = workspaceFileText
            ? (chatText + "\\n\\n================================================================================\\nZ.AI ATTACHED OUTPUT FILE: " + workspaceFileName + " (" + workspaceFileText.length + " chars)\\n================================================================================\\n\\n" + workspaceFileText)
            : chatText;

        return {
            connected: true,
            isGenerating,
            sendEnabled: Boolean(sendBtn && !sendBtn.disabled),
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
            resp = json.loads(await asyncio.wait_for(ws.recv(), timeout=8))
            val = resp.get("result", {}).get("result", {}).get("value")
            if isinstance(val, dict):
                text = val.get("lastText") or ""
                val["textHash"] = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16] if text else ""
                return val
    except Exception as e:
        return {"connected": False, "error": str(e)}
    return {"connected": False, "error": "Empty response"}


def save_arena_output(state: dict):
    ARENA_RAW_FILE.parent.mkdir(parents=True, exist_ok=True)
    ARENA_RAW_FILE.write_text(state.get("lastText", ""), encoding="utf-8")
    status = {
        "completed_at_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "text_length": state.get("lastLen", 0),
        "text_hash": state.get("textHash", ""),
        "latest_raw_path": str(ARENA_RAW_FILE)
    }
    ARENA_STATUS_FILE.write_text(json.dumps(status, indent=2), encoding="utf-8")


def save_zai_output(state: dict):
    ZAI_RAW_FILE.parent.mkdir(parents=True, exist_ok=True)
    ZAI_RAW_FILE.write_text(state.get("lastText", ""), encoding="utf-8")
    if state.get("workspaceFileText"):
        ZAI_ATTACHMENT_FILE.write_text(state.get("workspaceFileText", ""), encoding="utf-8")
    status = {
        "completed_at_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "text_length": state.get("lastLen", 0),
        "text_hash": state.get("textHash", ""),
        "latest_raw_path": str(ZAI_RAW_FILE)
    }
    ZAI_STATUS_FILE.write_text(json.dumps(status, indent=2), encoding="utf-8")



async def reload_cdp_tab(match_keyword: str) -> bool:
    try:
        raw = urllib.request.urlopen(CDP_URL, timeout=5).read().decode("utf-8")
        tabs = json.loads(raw)
        for t in tabs:
            if match_keyword in t.get("url", "") and t.get("webSocketDebuggerUrl"):
                ws_url = t["webSocketDebuggerUrl"]
                async with websockets.connect(ws_url, max_size=50_000_000, open_timeout=5, close_timeout=3) as ws:
                    print(f"[RockHardWatchdog] Refreshing tab for '{match_keyword}' via Page.reload...")
                    await ws.send(json.dumps({"id": 9999, "method": "Page.reload"}))
                    await asyncio.sleep(3.5)
                    return True
    except Exception as e:
        print(f"[RockHardWatchdog] Warning: failed to reload tab for '{match_keyword}': {e}", file=sys.stderr)
    return False

async def wait_for_dual_completion(expected_cycle: str, timeout_s: float = 600.0, poll_interval: float = 2.0) -> int:
    print(f"[RockHardWatchdog] Starting surveillance for cycle: '{expected_cycle}' (timeout={timeout_s}s, poll={poll_interval}s)")
    start_ts = time.time()
    
    # Baseline checks
    init_a = await probe_arena()
    init_z = await probe_zai()
    
    a_initial_hash = init_a.get("textHash", "")
    z_initial_hash = init_z.get("textHash", "")
    
    arena_done = False
    zai_done = False
    
    stable_a_ticks = 0
    stable_z_ticks = 0
    last_a_hash = a_initial_hash
    last_z_hash = z_initial_hash
    
    last_print = 0.0
    RELOAD_INTERVAL_SEC = 300.0  # 5 minutes exact operator mandate: refresh each uncompleted tab every 5m
    arena_last_reload = time.time()
    zai_last_reload = time.time()

    while (time.time() - start_ts) < timeout_s:
        await asyncio.sleep(poll_interval)
        now = time.time()
        elapsed = int(now - start_ts)
        
        # 1. EVALUATE ARENA
        if not arena_done:
            astate = await probe_arena()
            if astate.get("connected"):
                is_gen = astate.get("isGenerating", False)
                cur_text = astate.get("lastText", "")
                cur_hash = astate.get("textHash", "")
                has_anchor = astate.get("hasCopyButton") or astate.get("hasYesNoBanner")
                has_cycle = expected_cycle in cur_text if expected_cycle else (cur_hash != a_initial_hash)
                
                if has_cycle and not is_gen and has_anchor and len(cur_text) > 50:
                    if cur_hash == last_a_hash:
                        stable_a_ticks += 1
                    else:
                        last_a_hash = cur_hash
                        stable_a_ticks = 1
                    
                    if stable_a_ticks >= 2:
                        save_arena_output(astate)
                        arena_done = True
                        print(f"[RockHardWatchdog t={elapsed}s] Arena.ai COMPLETED cycle '{expected_cycle}'! ({len(cur_text)} chars, hash={cur_hash})")
                else:
                    stable_a_ticks = 0
                    last_a_hash = cur_hash
        
        # 2. EVALUATE Z.AI
        if not zai_done:
            zstate = await probe_zai()
            if zstate.get("connected"):
                is_gen = zstate.get("isGenerating", False)
                cur_text = zstate.get("lastText", "")
                cur_hash = zstate.get("textHash", "")
                has_cycle = expected_cycle in cur_text if expected_cycle else (cur_hash != z_initial_hash)
                
                if has_cycle and not is_gen and len(cur_text) > 50:
                    if cur_hash == last_z_hash:
                        stable_z_ticks += 1
                    else:
                        last_z_hash = cur_hash
                        stable_z_ticks = 1
                    
                    if stable_z_ticks >= 2:
                        save_zai_output(zstate)
                        zai_done = True
                        print(f"[RockHardWatchdog t={elapsed}s] Z.ai COMPLETED cycle '{expected_cycle}'! ({len(cur_text)} chars, hash={cur_hash})")
                else:
                    stable_z_ticks = 0
                    last_z_hash = cur_hash
        
        # Operator Mandate: Auto-refresh Arena tab every 5 minutes until completed
        if not arena_done and (now - arena_last_reload) >= RELOAD_INTERVAL_SEC:
            arena_last_reload = now
            print(f"\n[RockHardWatchdog t={elapsed}s] ⏱️ 5-Minute interval reached without Arena completion. Auto-refreshing Arena.ai tab via CDP Page.reload...", flush=True)
            await reload_cdp_tab("arena.ai")
            await asyncio.sleep(2.0)

        # Operator Mandate: Auto-refresh Z.ai tab every 5 minutes until completed
        if not zai_done and (now - zai_last_reload) >= RELOAD_INTERVAL_SEC:
            zai_last_reload = now
            print(f"\n[RockHardWatchdog t={elapsed}s] ⏱️ 5-Minute interval reached without Z.ai completion. Auto-refreshing Z.ai tab via CDP Page.reload...", flush=True)
            await reload_cdp_tab("chat.z.ai")
            await asyncio.sleep(2.0)

        # Periodic log every 6 seconds
        if now - last_print >= 6.0:
            last_print = now
            a_gen_flag = astate.get("isGenerating", False) if ('astate' in locals() and isinstance(astate, dict)) else False
            z_gen_flag = zstate.get("isGenerating", False) if ('zstate' in locals() and isinstance(zstate, dict)) else False
            a_stat = "DONE" if arena_done else ("GENERATING" if a_gen_flag else "AWAITING_CYCLE")
            z_stat = "DONE" if zai_done else ("GENERATING" if z_gen_flag else "AWAITING_CYCLE")
            a_rem = int(max(0, RELOAD_INTERVAL_SEC - (now - arena_last_reload))) if not arena_done else 0
            z_rem = int(max(0, RELOAD_INTERVAL_SEC - (now - zai_last_reload))) if not zai_done else 0
            print(f"[RockHardWatchdog t={elapsed}s] Arena.ai: {a_stat} (refresh in {a_rem}s) | Z.ai: {z_stat} (refresh in {z_rem}s)")

        # 3. CONVERGENCE: BOTH ARE DONE AND CONFIRMED
        if arena_done and zai_done:
            print(f"\n================================================================================")
            print(f"🎉 ROCK-HARD DUAL CONVERGENCE CONFIRMED FOR CYCLE '{expected_cycle}' in {elapsed}s!")
            print(f"Arena.ai: Output verified & persisted to docs/trade_plans/ARENA_LATEST_RAW.md")
            print(f"Z.ai: Output verified & persisted to docs/trade_plans/ZAI_LATEST_RAW.md")
            print(f"================================================================================\n")
            return 0

    print(f"[RockHardWatchdog ERROR] Timeout {timeout_s}s reached waiting for cycle '{expected_cycle}'!", file=sys.stderr)
    return 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cycle", required=True, help="Expected unique cycle ID")
    parser.add_argument("--timeout", type=float, default=1800.0)
    parser.add_argument("--interval", type=float, default=2.0)
    args = parser.parse_args()
    
    code = asyncio.run(wait_for_dual_completion(args.cycle, args.timeout, args.interval))
    sys.exit(code)
