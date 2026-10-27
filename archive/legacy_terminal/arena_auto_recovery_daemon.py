#!/usr/bin/env python3
"""
Terminal/arena_auto_recovery_daemon.py
======================================
Zero-Token Autonomous Auto-Recovery Daemon for Arena.ai.

Strict Operator Mandates:
1. NEVER touch or inject into the prompt box if the process is currently running!
   Detects all running states: Stop buttons, 'Running commands', active spinners, execution cards.
2. If the process has HALTED and an error banner is displayed:
   ("The AI service encountered an error. Please try again." or "Something went wrong. Please try again."):
   - First refreshes the page (Page.reload) to clear the broken session/modal.
   - Waits 5s for the page to stabilize.
   - Clears the editor box cleanly (Ctrl+A + Delete).
   - Submits strictly "continue" (never the full prompt or verbose error phrases).
"""
import sys

# ==============================================================================
# PERMANENTLY DEACTIVATED PER OPERATOR MANDATE
# Zero automated 'continue' injection daemons are permitted.
# ==============================================================================
if __name__ == "__main__":
    print("arena_auto_recovery_daemon is permanently disabled per operator mandate.")
    sys.exit(0)
import time
import urllib.request
import websockets

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "arena_auto_recovery_daemon.log"

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("ArenaAutoRecovery")

CDP_JSON_URL = "http://127.0.0.1:9222/json"
POLL_INTERVAL_SECONDS = 5.0
COOLDOWN_SECONDS = 45.0
RETRY_PROMPT = "continue"

last_retry_timestamps: dict[str, float] = {}

def get_arena_tabs() -> list[dict]:
    try:
        req = urllib.request.Request(CDP_JSON_URL, headers={"User-Agent": "ArenaAutoRecovery/1.0"})
        with urllib.request.urlopen(req, timeout=3.0) as resp:
            pages = json.loads(resp.read().decode())
        return [p for p in pages if "arena.ai/agent/" in p.get("url", "")]
    except Exception as exc:
        logger.debug("Failed to query CDP endpoints: %s", exc)
        return []

async def check_and_recover_tab(tab: dict) -> bool:
    url = tab.get("url", "")
    now = time.time()
    
    if url in last_retry_timestamps and (now - last_retry_timestamps[url]) < COOLDOWN_SECONDS:
        return False

    ws_url = tab.get("webSocketDebuggerUrl")
    if not ws_url:
        return False

    tab_name = "Fable" if "af999588" in url or "dde7" in url else "Astra"

    try:
        async with websockets.connect(ws_url, max_size=10 * 1024 * 1024, open_timeout=4.0) as ws:
            js_inspect = """
            (() => {
                // 1. Check for active Stop button / square icon
                const stopBtn = document.querySelector(
                    '.stop-generating-button, button[aria-label*="Stop" i], button:has(svg.lucide-square), [data-is-generating="true"], button[aria-label="Stop response"]'
                );
                if (stopBtn) return { isGenerating: true, hasError: false, reason: 'stop_button' };

                // 2. Check for active spinners
                const hasActiveSpinner = Array.from(document.querySelectorAll('.animate-spin, svg.animate-spin')).length > 0;
                if (hasActiveSpinner) return { isGenerating: true, hasError: false, reason: 'active_spinner' };

                // 3. Check for error alerts
                const alertEl = document.querySelector('div[role="alert"]');
                const alertText = alertEl ? (alertEl.innerText || '').trim() : '';
                const hasError = alertText.includes('The AI service encountered an error') || alertText.includes('Something went wrong');

                return { isGenerating: false, hasError: hasError, alertText: alertText };
            })()
            """
            await ws.send(json.dumps({"id": 100, "method": "Runtime.evaluate", "params": {"expression": js_inspect, "returnByValue": True}}))
            raw_res = json.loads(await ws.recv())
            status = raw_res.get("result", {}).get("result", {}).get("value", {})
            
            has_error = status.get("hasError", False)
            is_generating = status.get("isGenerating", False)

            # If generating, strictly DO NOTHING
            if is_generating:
                return False

            if has_error:
                alert_msg = status.get("alertText", "Unknown Error")
                logger.warning(f"[{tab_name}] Detected AI Service Error: '{alert_msg}'. Initiating clean refresh & 'continue'...")

                # Step 1: Reload page to clear error modal and reset websocket
                await ws.send(json.dumps({"id": 101, "method": "Page.reload", "params": {"ignoreCache": True}}))
                try:
                    await asyncio.wait_for(ws.recv(), timeout=3.0)
                except Exception:
                    pass

        # Step 2: Wait 5.0 seconds for reload to complete
        await asyncio.sleep(5.0)

        # Step 3: Fetch fresh websocket URL after reload
        fresh_tabs = get_arena_tabs()
        fresh_tab = next((t for t in fresh_tabs if t.get("url") == url), None)
        if not fresh_tab or not fresh_tab.get("webSocketDebuggerUrl"):
            logger.error(f"[{tab_name}] Could not find fresh tab after reload")
            return False

        fresh_ws_url = fresh_tab["webSocketDebuggerUrl"]

        # Step 4: Dispatch strictly "continue" via post_prompt_to_arena_single
        from Terminal.arena_bridge import post_prompt_to_arena_single
        logger.info(f"[{tab_name}] Injecting strictly '{RETRY_PROMPT}' after clean reload...")
        ok = await post_prompt_to_arena_single(fresh_ws_url, RETRY_PROMPT, tab_label=f"RECOVERY_{tab_name}")
        if ok:
            logger.info(f"[{tab_name}] Recovery '{RETRY_PROMPT}' successfully submitted!")
            last_retry_timestamps[url] = time.time()
            return True
    except Exception as exc:
        logger.debug(f"Error checking tab {tab_name} ({url}): {exc}")
    return False

async def main_loop():
    logger.info("=====================================================================")
    logger.info("[START] Arena Auto-Recovery Daemon Started")
    logger.info(f"Target: Detect AI Service Error | Action: Reload -> Send strictly '{RETRY_PROMPT}'")
    logger.info(f"Protection: Strictly IDLE when agent is running (never inject during generation)")
    logger.info(f"Log: {LOG_FILE}")
    logger.info("=====================================================================")

    while True:
        try:
            tabs = get_arena_tabs()
            for tab in tabs:
                await check_and_recover_tab(tab)
        except Exception as exc:
            logger.error("Error in recovery loop: %s", exc)
        await asyncio.sleep(POLL_INTERVAL_SECONDS)

if __name__ == "__main__":
    asyncio.run(main_loop())
