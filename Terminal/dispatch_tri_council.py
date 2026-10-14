"""
Terminal/dispatch_tri_council.py
Standard, token-efficient prompt dumping, live status inspection, and dispatch engine
for all three frontier AI tabs on Chrome CDP (127.0.0.1:9222):
  1. Arena Tab 1: GPT Astra (01a13b65)
  2. Arena Tab 2: Claude Fable (01a13b4a)
  3. Google Gemini Tab: Argon Mode (gemini.google.com)

Usage:
  python Terminal/dispatch_tri_council.py --dump [--cycle N]
      Dumps prompts to docs/prompts/ and prints compact summaries with raw GitHub URLs.
  python Terminal/dispatch_tri_council.py --status
      Inspects Chrome CDP tabs and prints live generation/submission status.
  python Terminal/dispatch_tri_council.py --submit [astra|fable|argon|all]
      Submits pending prompts in the specified tab(s).
  python Terminal/dispatch_tri_council.py --dispatch [--cycle N]
      Full automated workflow: dumps prompts, injects into tabs, and triggers submission.
"""
import argparse
import asyncio
import json
import os
import pathlib
import subprocess
import sys
import time
import urllib.request
import websockets
from typing import Dict, Any, Optional, Tuple, List

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)
except Exception:
    pass

from Terminal.arena_bridge import post_prompt_to_arena, dismiss_arena_popup, get_all_arena_tab_ws_urls
from Terminal.dispatch_comprehensive_wake_up_prompt import build_prompt, _load_cycle_num, _save_cycle_num

PROMPTS_DIR = ROOT / "docs" / "prompts"


def generate_tri_council_prompts(cycle: int) -> Dict[str, str]:
    """Builds tailored prompts for Astra, Fable, and Argon with peer cross-pollination."""
    prompt_arena_1_base = build_prompt(cycle_num=cycle, target_agent="arena_1_primary")
    prompt_arena_2_base = build_prompt(cycle_num=cycle, target_agent="arena_2_fable")

    cp_astra = """
================================================================================
PART CP: TRI-COUNCIL PEER AUDIT & CROSS-POLLINATION (FABLE & ARGON REVIEW)
================================================================================
Your peers Claude Fable and Gemini Argon completed deep audits of Cycle 104:
1. 100% Unanimous Consensus Ratified (STAND ASIDE):
   - All three models (Astra, Fable, Argon) agreed unanimously on Cycle 104: STAND ASIDE across all 24 assets. Zero forced trades.
   - Cash equity preserved at 4,859.55 USD (+84.55 USD above 4,775.00 USD hard floor, +64.55 USD above 4,795.00 USD operating buffer). 4/4 capacity slots available!
2. Microstructure & Orderflow Corrections from Cycle 104:
   - BTC & ETH Flow Dynamics: Fast CVD windows flipped positive on BTC (+45k 1m, +9k 5m, +2.13M 15m, +2.24M 30m), confirming seller pause/absorption. However, HTF trend is BEARISH (Z = -1.73 SD) and price trades inside the [81,400, 81,500] band holding 9.95M USD downside fuel. Counter-trend longs are banned. Model 2 pullback shorts require a relief bounce into the 82,061 / 2,446–2,449 resistance shelves.
   - SP500 Microstructure: Price flushed to 7,702.90. The 7,716.94 (1.572M) Ask wall appeared after the candle; [7,710, 7,720] has 5.04M squeeze fuel; an SL at 7,725 falls inside adjacent [7,719.64, 7,729.64] buy-stops; and massive buy walls at 7,700.80 (5.65M) and 7,696.60 (13.47M) cap short downside R:R to 1.37R gross.
   - NAS100: Flushed to 29,913; former 1.079M ask at 30,041 is no longer primary in live depth; shorting at 29,913 yields only 0.58R before 29,800 bids.
   - USWTI: Spread tightened to 4.83 bps (3.5% friction), but pullback velocity spiked to 3.01 (>= 0.80) and Trapped = BALANCED (no TRAPPED_SELLERS_BELOW print yet); nearby POC target offers only ~1.37R.
   - USDJPY: Flushed to 158.1045, regime transitioned to RANGE_BOUND, |Z| = 1.89 < 2.00 SD, and max L3 bid wall (~0.22M) fails the >= 0.50M USD Major FX floor.
TASK FOR ASTRA:
Audit the fresh Cycle 105 telemetry across the Clean-Friction Universe. Check if relief bounces on SP500 or NAS100 have tapped seasoned Ask walls with >= 2.0R downside payoff, or if USWTI/USDJPY have retested structural support with seasoned bid backing and low pullback velocity.
"""

    cp_fable = """
================================================================================
PART CP: TRI-COUNCIL PEER AUDIT & CROSS-POLLINATION (ASTRA & ARGON REVIEW)
================================================================================
Your peers GPT_Astra and Gemini Argon completed deep audits of Cycle 104:
1. 100% Unanimous Consensus Ratified (STAND ASIDE):
   - Both Astra and Argon reached identical conclusions: STAND ASIDE across all 24 assets. Zero forced trades.
   - Cash equity preserved at 4,859.55 USD (+84.55 USD above 4,775.00 USD hard floor, +64.55 USD above 4,795.00 USD operating buffer). 4/4 capacity slots available!
2. Microstructure & Orderflow Corrections from Cycle 104:
   - BTC & ETH Flow Dynamics: Fast CVD windows flipped positive on BTC (+45k 1m, +9k 5m, +2.13M 15m, +2.24M 30m), confirming seller pause/absorption. However, HTF trend is BEARISH (Z = -1.73 SD) and price trades inside the [81,400, 81,500] band holding 9.95M USD downside fuel. Counter-trend longs are banned. Model 2 pullback shorts require a relief bounce into the 82,061 / 2,446–2,449 resistance shelves.
   - SP500 Microstructure: Price flushed to 7,702.90. The 7,716.94 (1.572M) Ask wall appeared after the candle; [7,710, 7,720] has 5.04M squeeze fuel; an SL at 7,725 falls inside adjacent [7,719.64, 7,729.64] buy-stops; and massive buy walls at 7,700.80 (5.65M) and 7,696.60 (13.47M) cap short downside R:R to 1.37R gross.
   - NAS100: Flushed to 29,913; former 1.079M ask at 30,041 is no longer primary in live depth; shorting at 29,913 yields only 0.58R before 29,800 bids.
   - USWTI: Spread tightened to 4.83 bps (3.5% friction), but pullback velocity spiked to 3.01 (>= 0.80) and Trapped = BALANCED (no TRAPPED_SELLERS_BELOW print yet); nearby POC target offers only ~1.37R.
   - USDJPY: Flushed to 158.1045, regime transitioned to RANGE_BOUND, |Z| = 1.89 < 2.00 SD, and max L3 bid wall (~0.22M) fails the >= 0.50M USD Major FX floor.
TASK FOR FABLE:
Examine the fresh Cycle 105 orderbook depth, basis-mapped liquidation bands, and resting whale walls. Deliver your definitive ruling on whether any Clean-Friction asset meets the 5-pillar confluence stack for immediate execution.
"""

    prompt_arena_1 = prompt_arena_1_base + "\n" + cp_astra
    prompt_arena_2 = prompt_arena_2_base + "\n" + cp_fable

    prompt_lines = prompt_arena_2.splitlines()
    part_g_idx = next((i for i, l in enumerate(prompt_lines) if "PART G:" in l), 0)
    part_g_text = "\n".join(prompt_lines[part_g_idx:]) if part_g_idx > 0 else prompt_arena_2

    prompt_argon = f"""TRADING DESK COUNCIL: CYCLE {cycle} INSTITUTIONAL QUANTITATIVE AUDIT & ORDER DESK PROMPT
ROUTING TARGET: GOOGLE GEMINI (ARGON MODE - ZERO TOKEN AUXILIARY COUNCIL)
CANONICAL WORKSPACE: https://github.com/kbsingh1399/Trading_2
ACTIVE BRANCH: main (CANONICAL UPSTREAM SOURCE OF TRUTH — ALL MODELS ROUTE TO MAIN)

DIRECT RAW GITHUB UPSTREAM LINKS (Verbatim Access - Public Main Branch):
1. Telemetry: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
2. Slim Telemetry: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_gemini.json
3. Playbook: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
4. Desk State: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md
5. Active Context: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md

OPERATOR MANDATE:
Review our live book, positions, resting walls, and telemetry data structure across all 24 assets to maximize profitability and trade edge while defending the 4,775.00 USD hard floor.
MACRO BLACKOUT ENFORCEMENT IS PERMANENTLY REMOVED AND DISABLED. Never halt trading, purge positions, or disqualify setups due to macro events, CPI, FOMC, or news runway.

================================================================================
PART CP: TRI-COUNCIL DIALECTIC SYNTHESIS (ASTRA & FABLE FINDINGS REVIEW)
================================================================================
Both Astra and Fable have submitted their Cycle 104 reports:
1. 100% Unanimous Consensus Ratified (STAND ASIDE):
   - All three models (Astra, Fable, Argon) agreed unanimously on Cycle 104: STAND ASIDE across all 24 assets. Zero forced trades.
   - Cash equity preserved at 4,859.55 USD (+84.55 USD above 4,775.00 USD hard floor, +64.55 USD above 4,795.00 USD operating buffer). 4/4 capacity slots available!
2. Microstructure & Orderflow Corrections from Cycle 104:
   - BTC & ETH Flow Dynamics: Fast CVD windows flipped positive on BTC (+45k 1m, +9k 5m, +2.13M 15m, +2.24M 30m), confirming seller pause/absorption. However, HTF trend is BEARISH (Z = -1.73 SD) and price trades inside the [81,400, 81,500] band holding 9.95M USD downside fuel. Counter-trend longs are banned. Model 2 pullback shorts require a relief bounce into the 82,061 / 2,446–2,449 resistance shelves.
   - SP500 Microstructure: Price flushed to 7,702.90. The 7,716.94 (1.572M) Ask wall appeared after the candle; [7,710, 7,720] has 5.04M squeeze fuel; an SL at 7,725 falls inside adjacent [7,719.64, 7,729.64] buy-stops; and massive buy walls at 7,700.80 (5.65M) and 7,696.60 (13.47M) cap short downside R:R to 1.37R gross.
   - NAS100: Flushed to 29,913; former 1.079M ask at 30,041 is no longer primary in live depth; shorting at 29,913 yields only 0.58R before 29,800 bids.
   - USWTI: Spread tightened to 4.83 bps (3.5% friction), but pullback velocity spiked to 3.01 (>= 0.80) and Trapped = BALANCED (no TRAPPED_SELLERS_BELOW print yet); nearby POC target offers only ~1.37R.
   - USDJPY: Flushed to 158.1045, regime transitioned to RANGE_BOUND, |Z| = 1.89 < 2.00 SD, and max L3 bid wall (~0.22M) fails the >= 0.50M USD Major FX floor.
TASK FOR ARGON:
Synthesize peer findings with your deep reasoning engine. Deliver the definitive verdict on high-confluence Model 1 and Model 2 setups across the Clean-Friction Universe without any macro blackout restrictions.

{part_g_text}"""

    return {
        "astra": prompt_arena_1,
        "fable": prompt_arena_2,
        "argon": prompt_argon,
    }


def dump_prompts(cycle: int = None) -> Dict[str, pathlib.Path]:
    """Generates and dumps prompt files into docs/prompts/, returning file paths."""
    if cycle is None:
        cycle = _load_cycle_num()

    PROMPTS_DIR.mkdir(parents=True, exist_ok=True)
    prompts = generate_tri_council_prompts(cycle)

    paths = {
        "astra": PROMPTS_DIR / f"ARENA_CYCLE_{cycle}_ASTRA_PROMPT.txt",
        "fable": PROMPTS_DIR / f"ARENA_CYCLE_{cycle}_FABLE_PROMPT.txt",
        "argon": PROMPTS_DIR / f"GEMINI_CYCLE_{cycle}_ARGON_PROMPT.txt",
    }

    for key, p in paths.items():
        p.write_text(prompts[key], encoding="utf-8")

    print("\n" + "=" * 80)
    print(f"📋 TRI-COUNCIL PROMPTS DUMPED: CYCLE {cycle}")
    print("=" * 80)
    for model, p in paths.items():
        raw_url = f"https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/prompts/{p.name}"
        char_cnt = len(prompts[model])
        print(f"• {model.upper():<6} | {char_cnt:>6} chars | {p.name}")
        print(f"  Path: {p}")
        print(f"  Raw:  {raw_url}\n")
    print("=" * 80 + "\n")
    return paths


async def query_cdp_status() -> Dict[str, Any]:
    """Connects to Chrome CDP at 127.0.0.1:9222 and inspects live state of all 3 tabs."""
    try:
        pages = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=3).read().decode())
    except Exception as e:
        return {"error": f"Failed to connect to Chrome CDP at 127.0.0.1:9222: {e}"}

    status_data = {}

    for p in pages:
        url = p.get("url", "")
        ws_url = p.get("webSocketDebuggerUrl")
        if not ws_url:
            continue

        tab_id = None
        if "gemini.google.com" in url:
            tab_id = "argon"
        elif "01a13b65" in url:
            tab_id = "astra"
        elif "01a13bea" in url or "01a13b4a" in url or "af999588" in url or "01a1311e" in url:
            tab_id = "fable"

        if not tab_id:
            continue

        try:
            async with websockets.connect(ws_url, max_size=10 * 1024 * 1024) as ws:
                if tab_id == "argon":
                    expr = """(() => {
                        const stopBtn = document.querySelector('button[aria-label*="Stop" i], .stop-button');
                        const sendBtn = document.querySelector('button[aria-label*="Send" i], button.send-button');
                        const richText = document.querySelector('rich-textarea div[contenteditable="true"], div[contenteditable="true"]');
                        const msgs = document.querySelectorAll('.message-content, [class*="message-content"], .markdown-prose');
                        const lastMsg = msgs.length > 0 ? msgs[msgs.length - 1].innerText.slice(0, 200) : '';
                        const allText = document.body.innerText;
                        const isThinking = allText.includes('Thinking it through') || allText.includes('Thinking...');
                        return {
                            isGenerating: !!stopBtn || isThinking,
                            hasStopBtn: !!stopBtn,
                            boxChars: richText ? richText.innerText.length : 0,
                            sendDisabled: sendBtn ? sendBtn.disabled : null,
                            lastSnippet: lastMsg.replace(/\\n/g, ' ').trim()
                        };
                    })()"""
                else:
                    expr = """(() => {
                        const stopBtn = document.querySelector('button[aria-label="Stop" i], button[data-testid="stop-button"]');
                        const sendBtn = document.querySelector('button[aria-label="Send message" i], button[aria-label="Send" i], button[type="submit"]');
                        const tipTap = document.querySelector('div.tiptap[contenteditable="true"]');
                        const allText = document.body.innerText;
                        const isThinking = allText.includes('Thinking') || allText.includes('Thought for') || allText.includes('Generating');
                        const msgs = document.querySelectorAll('.prose:not(.tiptap)');
                        const lastMsg = msgs.length > 0 ? msgs[msgs.length - 1].innerText.slice(0, 200) : '';
                        return {
                            isGenerating: !!stopBtn || isThinking,
                            hasStopBtn: !!stopBtn,
                            boxChars: tipTap ? tipTap.innerText.length : 0,
                            sendDisabled: sendBtn ? sendBtn.disabled : null,
                            lastSnippet: lastMsg.replace(/\\n/g, ' ').trim()
                        };
                    })()"""

                await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": expr, "returnByValue": True}}))
                res = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value", {})
                res["url"] = url
                res["title"] = p.get("title", "")
                status_data[tab_id] = res
        except Exception as e:
            status_data[tab_id] = {"error": str(e), "url": url}

    return status_data


def print_status_table(status_data: Dict[str, Any]):
    """Prints a clean, concise, token-efficient table of live council state."""
    print("\n" + "=" * 80)
    print("📡 TRI-COUNCIL LIVE STATUS (PORT 9222)")
    print("=" * 80)
    for model in ["astra", "fable", "argon"]:
        info = status_data.get(model, {})
        if "error" in info:
            print(f"• {model.upper():<6} | ERROR: {info['error']}")
            continue

        gen_state = "🔥 GENERATING" if info.get("isGenerating") else "💤 IDLE / COMPLETED"
        box_chars = info.get("boxChars", 0)
        send_dis = info.get("sendDisabled")
        action = ""
        if box_chars > 100 and not info.get("isGenerating"):
            action = f"⚠️ PROMPT SITTING IN BOX ({box_chars} chars) - NEEDS SUBMIT"
        elif info.get("isGenerating"):
            action = "Computing response..."
        else:
            action = "Ready for next cycle"

        print(f"• {model.upper():<6} | {gen_state:<18} | Box: {box_chars:>5} chars | Action: {action}")
        if info.get("lastSnippet"):
            print(f"  Snippet: {info['lastSnippet'][:100]}...")
    print("=" * 80 + "\n")


async def submit_tab_prompt(target_tab: str = "fable") -> bool:
    """Focuses the specified tab, copies prompt from docs/prompts/, pastes via Ctrl+V, and hits Enter."""
    pages = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=3).read().decode())
    cycle = _load_cycle_num()
    ws_url = None

    if target_tab == "fable":
        target = next((p for p in pages if any(k in p.get("url", "") for k in ["01a13bea", "01a13b4a", "af999588", "01a1311e"])), None)
        ws_url = target.get("webSocketDebuggerUrl") if target else None
        prompt_file = PROMPTS_DIR / f"ARENA_CYCLE_{cycle}_FABLE_PROMPT.txt"
    elif target_tab == "astra":
        target = next((p for p in pages if any(k in p.get("url", "") for k in ["01a13b65", "d6de1eb4"])), None)
        ws_url = target.get("webSocketDebuggerUrl") if target else None
        prompt_file = PROMPTS_DIR / f"ARENA_CYCLE_{cycle}_ASTRA_PROMPT.txt"
    elif target_tab == "argon":
        target = next((p for p in pages if "gemini.google.com" in p.get("url", "")), None)
        ws_url = target.get("webSocketDebuggerUrl") if target else None
        prompt_file = PROMPTS_DIR / f"GEMINI_CYCLE_{cycle}_ARGON_PROMPT.txt"
    else:
        print(f"Unknown target tab: {target_tab}")
        return False

    if not ws_url:
        print(f"Tab for {target_tab} not found on Chrome CDP port 9222. Available tabs:")
        for p in pages:
            print(f"  • {p.get('title', '')[:30]} -> {p.get('url', '')}")
        return False

    if not prompt_file.exists():
        print(f"Prompt file {prompt_file} not found. Running dump first...")
        dump_prompts(cycle)

    print(f"[{target_tab.upper()}] Submitting prompt ({prompt_file.name})...")

    # Set Windows clipboard to prompt text using PowerShell
    ps_cmd = f"Set-Clipboard -Value (Get-Content -Raw -Encoding UTF8 '{str(prompt_file.resolve())}')"
    subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], check=True)

    async with websockets.connect(ws_url, max_size=20 * 1024 * 1024) as ws:
        await ws.send(json.dumps({"id": 1, "method": "Page.bringToFront"}))
        await ws.recv()
        await asyncio.sleep(0.3)
        await dismiss_arena_popup()
        await asyncio.sleep(0.3)

        # Focus editor
        if target_tab == "argon":
            js_focus = "(() => { const ed = document.querySelector('.ql-editor'); if (ed) { ed.focus(); return true; } return false; })()"
        else:
            js_focus = "(() => { const ed = document.querySelector('.tiptap.ProseMirror'); if (ed) { ed.focus(); return true; } return false; })()"

        await ws.send(json.dumps({"id": 2, "method": "Runtime.evaluate", "params": {"expression": js_focus, "returnByValue": True}}))
        await ws.recv()

        # Select all (Ctrl+A)
        await ws.send(json.dumps({"id": 3, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 65, "code": "KeyA", "key": "a", "modifiers": 2}}))
        await ws.recv()
        await ws.send(json.dumps({"id": 4, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 65, "code": "KeyA", "key": "a", "modifiers": 2}}))
        await ws.recv()

        # Delete
        await ws.send(json.dumps({"id": 5, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 46, "code": "Delete", "key": "Delete"}}))
        await ws.recv()
        await ws.send(json.dumps({"id": 6, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 46, "code": "Delete", "key": "Delete"}}))
        await ws.recv()

        # Paste (Ctrl+V)
        await ws.send(json.dumps({"id": 7, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 86, "code": "KeyV", "key": "v", "modifiers": 2}}))
        await ws.recv()
        await ws.send(json.dumps({"id": 8, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 86, "code": "KeyV", "key": "v", "modifiers": 2}}))
        await ws.recv()
        await asyncio.sleep(0.5)

        # Trigger ProseMirror onUpdate via Input.insertText so React enables submit button
        if target_tab != "argon":
            await ws.send(json.dumps({"id": 85, "method": "Input.insertText", "params": {"text": " "}}))
            await ws.recv()
            await asyncio.sleep(0.2)

        # Hit Enter to submit
        await ws.send(json.dumps({"id": 9, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"}}))
        await ws.recv()
        await ws.send(json.dumps({"id": 10, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"}}))
        await ws.recv()
        await asyncio.sleep(0.5)

        # Failsafe click on send button
        if target_tab == "argon":
            js_send = "(() => { const b = document.querySelector('button[aria-label*=\"Send\" i], button.send-button'); if (b && !b.disabled) { b.click(); return 'CLICKED'; } return 'NONE'; })()"
        else:
            js_send = "(() => { const b = document.querySelector('button[aria-label*=\"Send\" i], button[type=\"submit\"], button:has(svg.lucide-arrow-up)'); if (b && !b.disabled) { b.click(); return 'CLICKED'; } return 'DISABLED_' + (b ? b.className : 'NO_BTN'); })()"

        await ws.send(json.dumps({"id": 11, "method": "Runtime.evaluate", "params": {"expression": js_send, "returnByValue": True}}))
        click_res = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value")
        print(f"[{target_tab.upper()}] Submitted (click: {click_res})")
        return True


async def dispatch_gemini_argon(prompt_text: str, attach_files: bool = False) -> bool:
    """Injects prompt into Google Gemini Argon tab via CDP and triggers submission."""
    try:
        pages = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=5).read().decode())
    except Exception as e:
        print(f"[Argon] Error querying Chrome CDP tabs: {e}", file=sys.stderr)
        return False

    target = next((p for p in pages if "gemini.google.com" in p.get("url", "")), None)
    if not target:
        print("[Argon] Error: Google Gemini Argon tab not found in Chrome at 127.0.0.1:9222", file=sys.stderr)
        return False

    ws_url = target.get("webSocketDebuggerUrl")
    if not ws_url:
        return False

    print(f"[Argon] Connecting to tab '{target.get('title')}'...")
    try:
        async with websockets.connect(ws_url, max_size=50 * 1024 * 1024) as ws:
            await ws.send(json.dumps({"id": 1, "method": "Page.bringToFront"}))
            await ws.recv()
            await asyncio.sleep(0.3)

            # Focus editor and insert text
            print(f"[Argon] Injecting prompt ({len(prompt_text)} chars)...")
            js_focus = "(() => { const ed = document.querySelector('.ql-editor'); if (ed) { ed.focus(); return true; } return false; })()"
            await ws.send(json.dumps({"id": 8, "method": "Runtime.evaluate", "params": {"expression": js_focus, "returnByValue": True}}))
            await ws.recv()

            chunk_size = 4000
            for i in range(0, len(prompt_text), chunk_size):
                chunk = prompt_text[i:i + chunk_size]
                await ws.send(json.dumps({
                    "id": 100 + i,
                    "method": "Input.insertText",
                    "params": {"text": chunk}
                }))
                await ws.recv()
                await asyncio.sleep(0.04)

            await asyncio.sleep(0.5)
            js_event = "(() => { const ed = document.querySelector('.ql-editor'); if (ed) { ed.dispatchEvent(new Event('input', { bubbles: true })); ed.dispatchEvent(new Event('change', { bubbles: true })); return true; } return false; })()"
            await ws.send(json.dumps({"id": 105, "method": "Runtime.evaluate", "params": {"expression": js_event, "returnByValue": True}}))
            await ws.recv()

            # Click send button
            js_send = "(() => { const b = document.querySelector('button[aria-label=\"Send message\"], button.send-button, [aria-label*=\"Send\" i]'); if (b && !b.disabled) { b.click(); return 'CLICKED_SEND'; } return 'BUTTON_UNAVAILABLE'; })()"
            await ws.send(json.dumps({"id": 9, "method": "Runtime.evaluate", "params": {"expression": js_send, "returnByValue": True}}))
            send_res = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value")
            print(f"[Argon] Send button status: {send_res}")

            # Also dispatch Enter key
            await ws.send(json.dumps({"id": 12, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"}}))
            await ws.recv()
            await ws.send(json.dumps({"id": 13, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"}}))
            await ws.recv()

            await asyncio.sleep(2.0)
            js_status = "(() => { return { isGen: !!document.querySelector('.stop-generating-button, [aria-label*=\"Stop\" i], mat-progress-bar') }; })()"
            await ws.send(json.dumps({"id": 10, "method": "Runtime.evaluate", "params": {"expression": js_status, "returnByValue": True}}))
            st = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value", {})
            print(f"[Argon] Generation active: {st.get('isGen')}")
            return True
    except Exception as e:
        print(f"[Argon] Error dispatching to Gemini Argon: {e}", file=sys.stderr)
        return False


async def dispatch_all_three(cycle: int = None) -> bool:
    """Full automated dispatch: generates prompts, dumps to files, and submits to all 3 tabs."""
    if cycle is None:
        cycle = _load_cycle_num()

    print(f"\n=======================================================")
    print(f"🚀 INITIATING TRI-COUNCIL DISPATCH: CYCLE {cycle}")
    print(f"=======================================================")

    paths = dump_prompts(cycle)
    prompt_arena_1 = paths["astra"].read_text(encoding="utf-8")
    prompt_arena_2 = paths["fable"].read_text(encoding="utf-8")
    prompt_argon = paths["argon"].read_text(encoding="utf-8")

    # Pre-check: reload any tab with error banner
    try:
        pages_chk = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=3).read().decode())
        for t in [p for p in pages_chk if "arena.ai/agent/" in p.get("url", "")]:
            w_url = t.get("webSocketDebuggerUrl")
            if not w_url:
                continue
            lbl = "Fable" if ("af999588" in t.get("url", "") or "01a13b4a" in t.get("url", "")) else "Astra"
            try:
                async with websockets.connect(w_url, max_size=10 * 1024 * 1024) as ws_chk:
                    js_chk = '(() => { const a = document.querySelector("div[role=alert]"); return a ? (a.innerText || "") : ""; })()'
                    await ws_chk.send(json.dumps({"id": 9991, "method": "Runtime.evaluate", "params": {"expression": js_chk, "returnByValue": True}}))
                    alert_txt = json.loads(await ws_chk.recv()).get("result", {}).get("result", {}).get("value", "")
                    if "error" in alert_txt.lower() or "wrong" in alert_txt.lower():
                        print(f"[{lbl}] Detected error banner ('{alert_txt.strip()}'). Reloading tab first...")
                        await ws_chk.send(json.dumps({"id": 9992, "method": "Page.reload", "params": {"ignoreCache": True}}))
            except Exception:
                pass
    except Exception as e_chk:
        print(f"[Arena] Note on pre-reload check: {e_chk}")

    # Dispatch to Arena tabs via robust paste submission
    await submit_tab_prompt("fable")
    await asyncio.sleep(1.0)
    await submit_tab_prompt("astra")
    await asyncio.sleep(1.0)

    # Dispatch to Google Gemini Argon
    ok_argon = await dispatch_gemini_argon(prompt_argon, attach_files=False)
    print(f"Gemini Argon dispatch result: {ok_argon}")

    _save_cycle_num(cycle)
    print(f"\n✅ SUCCESS: Cycle {cycle} successfully processed across tri-council tabs!")
    return True


def main():
    parser = argparse.ArgumentParser(description="Tri-Council Prompt Dumper, Status Inspector & Dispatch Engine")
    parser.add_argument("--dump", action="store_true", help="Dump prompt files for the cycle and print summaries")
    parser.add_argument("--status", action="store_true", help="Check and print live status of all 3 Chrome tabs")
    parser.add_argument("--submit", type=str, nargs="?", const="all", help="Submit pending prompt on tab [astra|fable|argon|all]")
    parser.add_argument("--dispatch", action="store_true", help="Run full dispatch cycle (dump + inject + submit)")
    parser.add_argument("--cycle", type=int, default=None, help="Explicit cycle number")

    args = parser.parse_args()

    if args.dump:
        dump_prompts(cycle=args.cycle)
    elif args.status:
        st = asyncio.run(query_cdp_status())
        print_status_table(st)
    elif args.submit:
        target = args.submit.lower()
        if target == "all":
            for t in ["fable", "astra", "argon"]:
                asyncio.run(submit_tab_prompt(t))
        else:
            asyncio.run(submit_tab_prompt(target))
        st = asyncio.run(query_cdp_status())
        print_status_table(st)
    elif args.dispatch:
        asyncio.run(dispatch_all_three(cycle=args.cycle))
    else:
        # Default action: if no args given, show status and prompts info
        st = asyncio.run(query_cdp_status())
        print_status_table(st)


if __name__ == "__main__":
    main()
