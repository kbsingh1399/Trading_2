#!/usr/bin/env python3
"""
Terminal/council_split_view_surveillance_daemon.py
==================================================
Production Split-View Surveillance & Dual Council Health Daemon.

Responsibilities:
1. Connects to Chrome CDP (port 9222) and locates Arena.ai and Z.ai tabs.
2. Interrogates live DOM for active generation status (Stop button, stream indicators, length).
3. Takes high-resolution screenshots of both tabs via CDP Page.captureScreenshot.
4. Stitches both images horizontally into a synchronized side-by-side split view:
   `Data/screenshots/council_split_view_latest.png`.
5. Emits real-time JSON status to `Data/council_surveillance_status.json`.
6. Operates on a robust 10-minute (600s) cycle or single-pass mode (`--once`).
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import datetime
import io
import json
import logging
import os
import pathlib
import sys
import time
import urllib.request
from typing import Any, Dict, Optional, Tuple

from PIL import Image

try:
    import websockets
except ImportError:
    websockets = None

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
except Exception:
    pass

ROOT_DIR = pathlib.Path(__file__).resolve().parents[1]
SCREENSHOTS_DIR = ROOT_DIR / "Data" / "screenshots"
ARCHIVE_DIR = SCREENSHOTS_DIR / "archive"
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

STATUS_FILE = ROOT_DIR / "Data" / "council_surveillance_status.json"
PID_FILE = ROOT_DIR / "Data" / "council_surveillance_daemon.pid"
LOG_FILE = ROOT_DIR / "logs" / "council_surveillance_daemon.log"
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [CouncilSurveillance] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
    ],
)
log = logging.getLogger("CouncilSurveillance")

CDP_BASE_URL = "http://127.0.0.1:9222"


def get_target_tabs() -> Tuple[Optional[dict], Optional[dict]]:
    """Discovers Arena.ai and Z.ai tabs on Chrome CDP."""
    try:
        req = urllib.request.urlopen(f"{CDP_BASE_URL}/json", timeout=5)
        tabs = json.loads(req.read().decode("utf-8"))
        arena_tab = next(
            (t for t in tabs if t.get("type") == "page" and "arena.ai" in t.get("url", "") and t.get("webSocketDebuggerUrl")),
            None,
        )
        zai_tab = next(
            (t for t in tabs if t.get("type") == "page" and ("chat.z.ai" in t.get("url", "") or "z.ai" in t.get("url", "")) and t.get("webSocketDebuggerUrl")),
            None,
        )
        return arena_tab, zai_tab
    except Exception as e:
        log.warning(f"Error querying CDP tabs from {CDP_BASE_URL}: {e}")
        return None, None


async def probe_tab_state_and_screenshot(
    ws_url: str,
    tab_type: str,
) -> Tuple[Dict[str, Any], Optional[Image.Image]]:
    """Probes model status and captures a viewport screenshot via CDP."""
    status_info: Dict[str, Any] = {
        "connected": False,
        "is_generating": False,
        "char_count": 0,
        "snippet": "",
        "error": None,
    }
    img: Optional[Image.Image] = None

    if not websockets:
        status_info["error"] = "websockets library not available"
        return status_info, None

    try:
        async with websockets.connect(
            ws_url,
            max_size=30 * 1024 * 1024,
            open_timeout=5,
            close_timeout=2,
        ) as ws:
            status_info["connected"] = True

            # 1. Evaluate DOM status
            if tab_type == "arena":
                js = """(() => {
                    const isGen = document.querySelector('button[aria-label*="Stop" i], button[title*="Stop" i], button.stop, [data-testid="stop-button"]') !== null;
                    const prose = Array.from(document.querySelectorAll('.prose, [data-message-author-role="assistant"]'));
                    const lastText = prose.length > 0 ? (prose[prose.length - 1].innerText || prose[prose.length - 1].textContent || '') : '';
                    return {
                        is_generating: isGen,
                        char_count: lastText.length,
                        snippet: lastText.slice(0, 300)
                    };
                })()"""
            else:  # zai
                js = """(() => {
                    const stopBtn = document.querySelector('button[aria-label*="Stop"], button[title*="Stop"], button.stop-button, button:has(span.size-3.rounded-xs)');
                    const stopSquare = document.querySelector('button span.size-3.rounded-xs, button span.block.size-3');
                    const sendBtn = document.querySelector('button#send-message-button, button[aria-label="Send"], button[aria-label*="Send"]');
                    const thinkingBtn = Array.from(document.querySelectorAll('button, div, span')).find(b => (b.innerText || '').trim().startsWith('Thinking'));
                    const isGen = Boolean(stopBtn) || Boolean(stopSquare) || Boolean(thinkingBtn);

                    const allChatMsgs = Array.from(document.querySelectorAll('.chat-assistant.markdown-prose, div.prose, .chat-assistant'));
                    let chatText = '';
                    for (let i = allChatMsgs.length - 1; i >= 0; i--) {
                        const t = (allChatMsgs[i].innerText || '').trim();
                        if (t.includes('Cycle_') || t.includes('COUNCIL REPORT') || t.includes('EXECUTION RULING')) {
                            chatText = t;
                            break;
                        }
                    }
                    if (!chatText || chatText.length < 200) {
                        const body = document.body ? (document.body.innerText || '') : '';
                        const rIdx = body.lastIndexOf('# [COUNCIL REPORT');
                        if (rIdx !== -1) {
                            chatText = body.substring(rIdx);
                        } else {
                            const cIdx = body.lastIndexOf('Cycle_');
                            if (cIdx !== -1) {
                                chatText = body.substring(cIdx);
                            } else {
                                const execIdx = body.lastIndexOf('EXECUTION RULING');
                                if (execIdx !== -1) chatText = body.substring(Math.max(0, execIdx - 200));
                            }
                        }
                    }
                    return {
                        is_generating: isGen,
                        char_count: chatText.length,
                        snippet: chatText.slice(0, 300)
                    };
                })()"""

            req = {"id": 101, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}
            await ws.send(json.dumps(req))
            resp = await asyncio.wait_for(ws.recv(), timeout=5.0)
            res_data = json.loads(resp)
            val = res_data.get("result", {}).get("result", {}).get("value", {})
            if isinstance(val, dict):
                status_info["is_generating"] = bool(val.get("is_generating", False))
                status_info["char_count"] = int(val.get("char_count", 0))
                status_info["snippet"] = str(val.get("snippet", ""))

            # 2. Capture Viewport Screenshot
            shot_req = {"id": 102, "method": "Page.captureScreenshot", "params": {"format": "png"}}
            await ws.send(json.dumps(shot_req))
            shot_resp = await asyncio.wait_for(ws.recv(), timeout=8.0)
            shot_data = json.loads(shot_resp)
            b64_img = shot_data.get("result", {}).get("data", "")
            if b64_img:
                raw_bytes = base64.b64decode(b64_img)
                img = Image.open(io.BytesIO(raw_bytes))

    except Exception as e:
        status_info["error"] = str(e)
        log.warning(f"Error interrogating {tab_type} tab: {e}")

    return status_info, img


def stitch_and_save_split_view(
    img_arena: Optional[Image.Image],
    img_zai: Optional[Image.Image],
    cycle_id: str,
) -> Optional[pathlib.Path]:
    """Stitches Arena and Z.ai screenshots into a single split view."""
    if not img_arena and not img_zai:
        log.warning("No screenshot images available to stitch.")
        return None

    # Fallback placeholders if one image fails
    target_height = 900
    if img_arena and not img_zai:
        w = int(img_arena.width * (target_height / img_arena.height))
        stitched = img_arena.resize((w, target_height), Image.Resampling.LANCZOS)
    elif img_zai and not img_arena:
        w = int(img_zai.width * (target_height / img_zai.height))
        stitched = img_zai.resize((w, target_height), Image.Resampling.LANCZOS)
    else:
        # Both images exist: stitch side-by-side
        w_a = int(img_arena.width * (target_height / img_arena.height))
        w_z = int(img_zai.width * (target_height / img_zai.height))
        res_a = img_arena.resize((w_a, target_height), Image.Resampling.LANCZOS)
        res_z = img_zai.resize((w_z, target_height), Image.Resampling.LANCZOS)

        stitched = Image.new("RGB", (w_a + w_z, target_height), color=(20, 20, 20))
        stitched.paste(res_a, (0, 0))
        stitched.paste(res_z, (w_a, 0))

    # Save latest
    latest_path = SCREENSHOTS_DIR / "council_split_view_latest.png"
    stitched.save(latest_path, format="PNG")

    # Save archive with timestamp
    ts_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_path = ARCHIVE_DIR / f"split_view_{cycle_id}_{ts_str}.png"
    stitched.save(archive_path, format="PNG")

    log.info(f"📸 Split-view screenshot saved: {latest_path.name} ({stitched.size[0]}x{stitched.size[1]})")
    return latest_path


async def run_surveillance_pass(cycle_id: str, iteration: int) -> Dict[str, Any]:
    """Executes a single surveillance pass across both council seats."""
    now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    now_ist = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=5, minutes=30)).strftime("%Y-%m-%d %H:%M:%S IST")

    arena_tab, zai_tab = get_target_tabs()

    arena_status, img_arena = (
        await probe_tab_state_and_screenshot(arena_tab["webSocketDebuggerUrl"], "arena")
        if arena_tab
        else ({"connected": False, "is_generating": False, "error": "Arena tab not found"}, None)
    )

    zai_status, img_zai = (
        await probe_tab_state_and_screenshot(zai_tab["webSocketDebuggerUrl"], "zai")
        if zai_tab
        else ({"connected": False, "is_generating": False, "error": "Z.ai tab not found"}, None)
    )

    screenshot_path = stitch_and_save_split_view(img_arena, img_zai, cycle_id)

    # Determine status verdicts
    a_gen = arena_status.get("is_generating", False)
    z_gen = zai_status.get("is_generating", False)
    a_chars = arena_status.get("char_count", 0)
    z_chars = zai_status.get("char_count", 0)

    # If not generating and text is substantial (> 1000 chars), it has completed!
    arena_finished = not a_gen and a_chars > 1000
    zai_finished = not z_gen and z_chars > 1000
    both_finished = arena_finished and zai_finished

    payload: Dict[str, Any] = {
        "cycle_id": cycle_id,
        "iteration": iteration,
        "timestamp_ist": now_ist,
        "timestamp_utc": now_utc,
        "both_finished": both_finished,
        "any_generating": a_gen or z_gen,
        "arena": {
            "connected": arena_status.get("connected", False),
            "is_generating": a_gen,
            "finished": arena_finished,
            "char_count": a_chars,
            "snippet": arena_status.get("snippet", "")[:150],
            "error": arena_status.get("error"),
        },
        "zai": {
            "connected": zai_status.get("connected", False),
            "is_generating": z_gen,
            "finished": zai_finished,
            "char_count": z_chars,
            "snippet": zai_status.get("snippet", "")[:150],
            "error": zai_status.get("error"),
        },
        "screenshot_latest": str(screenshot_path.resolve()) if screenshot_path else None,
    }

    with open(STATUS_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    a_badge = "GENERATING" if a_gen else ("FINISHED" if arena_finished else "IDLE")
    z_badge = "GENERATING" if z_gen else ("FINISHED" if zai_finished else "IDLE")
    log.info(
        f"[Pass #{iteration}] Arena: {a_badge} ({a_chars} chars) | Z.ai: {z_badge} ({z_chars} chars) | Both Finished: {both_finished}"
    )
    return payload


def main():
    parser = argparse.ArgumentParser(description="Split-View Council Surveillance Daemon")
    parser.add_argument("--cycle", default="Cycle_037", help="Cycle ID (e.g. Cycle_037)")
    parser.add_argument("--interval", type=int, default=600, help="Interval in seconds (default: 600s = 10 minutes)")
    parser.add_argument("--once", action="store_true", help="Run a single pass and exit")
    args = parser.parse_args()

    # Record PID
    with open(PID_FILE, "w", encoding="utf-8") as f:
        f.write(str(os.getpid()))

    log.info("================================================================================")
    log.info(f"🏛️ COUNCIL SPLIT-VIEW SURVEILLANCE DAEMON INITIALIZED (PID: {os.getpid()})")
    log.info(f"Target: Arena.ai & Z.ai | Cycle: {args.cycle} | Interval: {args.interval}s")
    log.info(f"Status Output: {STATUS_FILE}")
    log.info(f"Split-View Path: {SCREENSHOTS_DIR / 'council_split_view_latest.png'}")
    log.info("================================================================================")

    iteration = 1
    try:
        while True:
            res = asyncio.run(run_surveillance_pass(args.cycle, iteration))
            if args.once:
                log.info("Single-pass mode complete. Exiting.")
                break

            if res.get("both_finished"):
                log.info("🎉 BOTH ARENA.AI AND Z.AI HAVE COMPLETED! Outputs are sealed and ready for harvest.")

            log.info(f"Sleeping for {args.interval} seconds (10 minutes) until next surveillance pass...")
            time.sleep(args.interval)
            iteration += 1

    except KeyboardInterrupt:
        log.info("Daemon interrupted by operator. Shutting down gracefully.")
    except Exception as e:
        log.error(f"Fatal error in surveillance loop: {e}", exc_info=True)
    finally:
        if PID_FILE.exists():
            try:
                PID_FILE.unlink()
            except Exception:
                pass


if __name__ == "__main__":
    main()
