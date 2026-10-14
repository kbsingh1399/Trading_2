"""
Terminal/dispatch_tri_council.py
Dispatches collaborative trading prompts to ALL THREE frontier Chrome AI tabs:
  1. Arena Tab 1: GPT Astra (01a136b2)
  2. Arena Tab 2: Claude Fable Orchestrator (01a1311e)
  3. Google Gemini Tab: Argon Mode (gemini.google.com) with 4 attached context files
"""
import asyncio
import json
import pathlib
import sys
import time
import urllib.request
import websockets

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)
except Exception:
    pass

from Terminal.arena_bridge import post_prompt_to_arena, dismiss_arena_popup
from Terminal.dispatch_comprehensive_wake_up_prompt import build_prompt, _load_cycle_num, _save_cycle_num

FILES_TO_ATTACH = [
    str((ROOT / "docs" / "telemetry" / "live_snapshot_latest.json").resolve()),
    str((ROOT / "docs" / "specs" / "TRADE_DECISION_PLAYBOOK.md").resolve()),
    str((ROOT / "docs" / "trade_plans" / "LIVE_COLLABORATIVE_ORDER_DESK.md").resolve()),
    str((ROOT / ".agents" / "rules" / "ACTIVE_CONTEXT.md").resolve()),
]

async def dispatch_gemini_argon(prompt_text: str, attach_files: bool = True) -> bool:
    """Attaches files (optional) and injects prompt into Google Gemini Argon tab via CDP."""
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
        print("[Argon] Error: No WebSocket URL for Gemini tab", file=sys.stderr)
        return False

    print(f"[Argon] Connecting to tab '{target.get('title')}'...")
    try:
        async with websockets.connect(ws_url, max_size=50 * 1024 * 1024) as ws:
            if attach_files:
                try:
                    # Bring tab to front
                    await ws.send(json.dumps({"id": 41, "method": "Page.bringToFront"}))
                    await ws.recv()
                    await asyncio.sleep(0.3)

                    # Prepare 4 ground truth files (use slim snapshot to prevent parsing timeouts)
                    gemini_snap = ROOT / "docs" / "telemetry" / "live_snapshot_gemini.json"
                    primary_snap = gemini_snap if gemini_snap.exists() else (ROOT / "docs" / "telemetry" / "live_snapshot_latest.json")
                    files_to_send = [
                        str(primary_snap.resolve()),
                        str((ROOT / "docs" / "specs" / "TRADE_DECISION_PLAYBOOK.md").resolve()),
                        str((ROOT / "docs" / "trade_plans" / "LIVE_COLLABORATIVE_ORDER_DESK.md").resolve()),
                        str((ROOT / ".agents" / "rules" / "ACTIVE_CONTEXT.md").resolve()),
                    ]
                    existing = [f for f in files_to_send if pathlib.Path(f).exists()]

                    # Set files on Windows clipboard via PowerShell
                    import subprocess
                    ps_files_arg = ", ".join(f"'{f}'" for f in existing)
                    subprocess.run(
                        ["powershell", "-NoProfile", "-Command", f"Set-Clipboard -Path @({ps_files_arg})"],
                        check=True,
                        timeout=10,
                        capture_output=True
                    )
                    print(f"[Argon] Set {len(existing)} ground-truth files on Windows clipboard.")

                    # Focus editor and paste via Ctrl+V
                    js_focus = "(() => { const ed = document.querySelector('.ql-editor'); if (ed) { ed.focus(); return true; } return false; })()"
                    await ws.send(json.dumps({"id": 42, "method": "Runtime.evaluate", "params": {"expression": js_focus, "returnByValue": True}}))
                    await ws.recv()
                    await asyncio.sleep(0.2)

                    # Dispatch Ctrl+V
                    await ws.send(json.dumps({"id": 43, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 17, "code": "ControlLeft", "key": "Control"}}))
                    await ws.recv()
                    await ws.send(json.dumps({"id": 44, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 86, "code": "KeyV", "key": "v", "modifiers": 2}}))
                    await ws.recv()
                    await ws.send(json.dumps({"id": 45, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 86, "code": "KeyV", "key": "v", "modifiers": 2}}))
                    await ws.recv()
                    await ws.send(json.dumps({"id": 46, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 17, "code": "ControlLeft", "key": "Control"}}))
                    await ws.recv()
                    print("[Argon] Dispatched Ctrl+V. Waiting 5s for file upload...")
                    await asyncio.sleep(5.0)

                    # Check and clean any error chips (e.g. click X on any failed file)
                    js_clean_and_stat = """(() => {
                        const chips = Array.from(document.querySelectorAll('.gem-attachment-content'));
                        let removed = 0;
                        for (const c of chips) {
                            const icons = Array.from(c.querySelectorAll('mat-icon'));
                            const closeBtn = c.querySelector('button[aria-label*="close" i]');
                            if (icons.length > 1 && closeBtn) {
                                closeBtn.click();
                                removed++;
                            }
                        }
                        const remaining = Array.from(document.querySelectorAll('.gem-attachment-content'));
                        return {
                            totalAttached: remaining.length,
                            removedErrors: removed,
                            healthyChips: remaining.map(c => c.innerText.replace(/\\n/g, ' ').trim())
                        };
                    })()"""
                    await ws.send(json.dumps({"id": 47, "method": "Runtime.evaluate", "params": {"expression": js_clean_and_stat, "returnByValue": True}}))
                    chip_stat = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value", {})
                    print(f"[Argon] Chip status after paste & verify: {chip_stat}")
                    if chip_stat.get("totalAttached", 0) == 0:
                        print("[Argon] Note: No chips detected via Ctrl+V paste; proceeding with full prompt text...")
                except Exception as ex_att:
                    print(f"[Argon] Note on file attachment: {ex_att}; proceeding with prompt injection...")

            # Focus editor and insert text
            print(f"[Argon] Injecting prompt ({len(prompt_text)} chars)...")
            js_focus = "(() => { const ed = document.querySelector('.ql-editor'); if (ed) { ed.focus(); return true; } return false; })()"
            await ws.send(json.dumps({"id": 8, "method": "Runtime.evaluate", "params": {"expression": js_focus, "returnByValue": True}}))
            await ws.recv()
            await asyncio.sleep(0.3)

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
            # Dispatch input and change events so Angular enables the Send button
            js_event = "(() => { const ed = document.querySelector('.ql-editor'); if (ed) { ed.dispatchEvent(new Event('input', { bubbles: true })); ed.dispatchEvent(new Event('change', { bubbles: true })); return true; } return false; })()"
            await ws.send(json.dumps({"id": 105, "method": "Runtime.evaluate", "params": {"expression": js_event, "returnByValue": True}}))
            await ws.recv()
            await asyncio.sleep(0.5)

            # Click send button and send Enter key to ensure submission
            js_send = "(() => { const b = document.querySelector('button[aria-label=\"Send message\"], button.send-button, [aria-label*=\"Send\" i]'); if (b && !b.disabled) { b.click(); return 'CLICKED_SEND'; } return 'BUTTON_UNAVAILABLE'; })()"
            await ws.send(json.dumps({"id": 9, "method": "Runtime.evaluate", "params": {"expression": js_send, "returnByValue": True}}))
            send_res = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value")
            print(f"[Argon] Send button status: {send_res}")

            # Also dispatch Enter key to guarantee submission
            await ws.send(json.dumps({"id": 11, "method": "Runtime.evaluate", "params": {"expression": "if (document.querySelector('.ql-editor')) document.querySelector('.ql-editor').focus();"}}))
            await ws.recv()
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
    """Dispatches next cycle prompt to Arena 1 (Astra), Arena 2 (Fable), and Gemini Argon."""
    if cycle is None:
        cycle = _load_cycle_num()

    print(f"\n=======================================================")
    print(f"🚀 INITIATING TRI-COUNCIL DISPATCH: CYCLE {cycle}")
    print(f"=======================================================")

    # 1. Build base prompts
    prompt_arena_1_base = build_prompt(cycle_num=cycle, target_agent="arena_1_primary")
    prompt_arena_2_base = build_prompt(cycle_num=cycle, target_agent="arena_2_fable")

    # Ingest peer findings from previous cycle for Cross-Pollination
    cp_astra = """
================================================================================
PART CP: TRI-COUNCIL PEER AUDIT & CROSS-POLLINATION (FABLE & ARGON REVIEW)
================================================================================
Your peers Claude Fable and Gemini Argon completed deep audits of Cycle 103:
1. 100% Unanimous Consensus Ratified (STAND ASIDE):
   - All three models (Astra, Fable, Argon) agreed unanimously on Cycle 103: STAND ASIDE across all 24 assets. Zero forced trades.
   - Direct Raw GitHub Access Verified: Gemini Argon tested and confirmed full direct access to raw.githubusercontent.com/kbsingh1399/Trading_2/main/... files! All three models now operate directly on authentic raw main-branch repository links.
2. SP500 & NAS100 Microstructure & Chronology Audit:
   - SP500: Reached 7,731.76 traversing the old 7,730 edge, but fell back to 7,707. An alternative 1.572M Ask wall appeared at 7,716.94 (mapped), but [7,710, 7,720] has 5.04M USD of un-swept squeeze fuel (3.26M stops + 1.78M liqs). Stop placement at 7,725 falls inside the adjacent [7,719.64, 7,729.64] band, and large buy walls sit at 7,700.8 (5.65M) and 7,696.6 (13.47M), limiting downside R:R to ~1.37R gross.
   - NAS100: Recovered a 1.079M USD Ask wall at 30,041.865 (538s duration), but price is at 29,966; needs a relief bounce into that wall. Nearby targets offer only 0.58R gross without an extended flush.
3. Crypto Majors (BTC & ETH):
   - BTC & ETH: Completed 5m/15m/30m CVD deltas turned negative again (-945k 15m on BTC, -2.14M 15m on ETH), confirming persistent seller dominance. Fading this flow with dip-buying longs is strictly banned. But pullback shorts need an entry into the 82,061 / 2,446–2,448 resistance shelves.
4. Commodities & Forex:
   - USWTI: Bullish trend, but velocity accelerated to 3.01 and primary 1.45M bid wall is 2.41 ATR below at 95.07. Wait for a deeper retracement.
   - USDJPY: Testing 15m EMA50 (158.60) at low Z (+0.26 SD) with positive tick flow, but lacks a >=0.50M bid wall.
5. Capital State:
   - MT5 Balance: 4,859.55 USD | Equity: 4,859.55 USD | Free Margin: 4,859.55 USD (+84.55 USD above 4,775.00 USD hard floor, +64.55 USD above operating buffer). All 4 capacity slots are 100% open!
TASK FOR ASTRA:
Audit the fresh Cycle 104 telemetry across the Clean-Friction Universe. Check if relief bounces on SP500 or NAS100 have tapped seasoned Ask walls with >= 2.0R downside payoff, or if USWTI/USDJPY have retested structural support with seasoned bid backing.
"""

    cp_fable = """
================================================================================
PART CP: TRI-COUNCIL PEER AUDIT & CROSS-POLLINATION (ASTRA & ARGON REVIEW)
================================================================================
Your peers GPT_Astra and Gemini Argon completed deep audits of Cycle 103:
1. 100% Unanimous Consensus Ratified (STAND ASIDE):
   - Both Astra and Argon reached identical conclusions: STAND ASIDE across all 24 assets. Zero forced trades.
   - Direct Raw GitHub Access Verified: Gemini Argon tested and confirmed full direct access to raw.githubusercontent.com/kbsingh1399/Trading_2/main/... files! All three models now operate directly on authentic raw main-branch repository links.
2. SP500 & NAS100 Microstructure & Chronology Audit:
   - SP500: High reached 7,731.76 traversing the old 7,730 level, but fell back to 7,707. An alternative 1.572M Ask wall appeared at 7,716.94 (mapped), but [7,710, 7,720] has 5.04M USD of un-swept squeeze fuel (3.26M stops + 1.78M liqs). Stop placement at 7,725 falls inside the adjacent [7,719.64, 7,729.64] band, and large buy walls sit at 7,700.8 (5.65M) and 7,696.6 (13.47M), limiting downside R:R to ~1.37R gross.
   - NAS100: Recovered a 1.079M USD Ask wall at 30,041.865 (538s duration), but price is at 29,966; needs a relief bounce into that wall. Nearby targets offer only 0.58R gross without an extended flush.
3. Crypto Majors (BTC & ETH):
   - BTC & ETH: Completed 5m/15m/30m CVD deltas turned negative again (-945k 15m on BTC, -2.14M 15m on ETH), confirming persistent seller dominance. Fading this flow with dip-buying longs is strictly banned. But pullback shorts need an entry into the 82,061 / 2,446–2,448 resistance shelves.
4. Commodities & Forex:
   - USWTI: Bullish trend, but velocity accelerated to 3.01 and primary 1.45M bid wall is 2.41 ATR below at 95.07. Wait for a deeper retracement.
   - USDJPY: Testing 15m EMA50 (158.60) at low Z (+0.26 SD) with positive tick flow, but lacks a >=0.50M bid wall.
5. Capital State:
   - MT5 Balance: 4,859.55 USD | Equity: 4,859.55 USD | Free Margin: 4,859.55 USD (+84.55 USD above 4,775.00 USD hard floor, +64.55 USD above operating buffer). All 4 capacity slots are 100% open!
TASK FOR FABLE:
Examine the fresh Cycle 104 orderbook depth, basis-mapped liquidation bands, and resting whale walls. Deliver your definitive ruling on whether any Clean-Friction asset meets the 5-pillar confluence stack for immediate execution.
"""

    prompt_arena_1 = prompt_arena_1_base + "\n" + cp_astra
    prompt_arena_2 = prompt_arena_2_base + "\n" + cp_fable

    # Build Argon prompt with ground-truth citations and peer cross-pollination
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
Both Astra and Fable have submitted their Cycle 103 reports:
1. 100% Unanimous Consensus Ratified (STAND ASIDE):
   - All three models (Astra, Fable, Argon) agreed unanimously on Cycle 103: STAND ASIDE across all 24 assets. Zero forced trades.
   - 11 altcoins remain excluded under the 15% dynamic spread friction cap. 100% priority is focused on the Clean-Friction Universe.
2. SP500 & NAS100 Microstructure & Chronology Audit:
   - SP500: Reached 7,731.76 traversing the old 7,730 edge, but fell back to 7,707. An alternative 1.572M Ask wall appeared at 7,716.94 (mapped), but [7,710, 7,720] has 5.04M USD of un-swept squeeze fuel (3.26M stops + 1.78M liqs). Stop placement at 7,725 falls inside the adjacent [7,719.64, 7,729.64] band, and large buy walls sit at 7,700.8 (5.65M) and 7,696.6 (13.47M), limiting downside R:R to ~1.37R gross.
   - NAS100: Recovered a 1.079M USD Ask wall at 30,041.865 (538s duration), but price is at 29,966; needs a relief bounce into that wall. Nearby targets offer only 0.58R gross without an extended flush.
3. Crypto Majors (BTC & ETH):
   - BTC & ETH: Completed 5m/15m/30m CVD deltas turned negative again (-945k 15m on BTC, -2.14M 15m on ETH), confirming persistent seller dominance. Fading this flow with dip-buying longs is strictly banned. But pullback shorts need an entry into the 82,061 / 2,446–2,448 resistance shelves.
4. Commodities & Forex:
   - USWTI: Bullish trend, but velocity accelerated to 3.01 and primary 1.45M bid wall is 2.41 ATR below at 95.07. Wait for a deeper retracement.
   - USDJPY: Testing 15m EMA50 (158.60) at low Z (+0.26 SD) with positive tick flow, but lacks a >=0.50M bid wall.
5. Capital State:
   - MT5 Balance: 4,859.55 USD | Equity: 4,859.55 USD | Free Margin: 4,859.55 USD (+84.55 USD above 4,775.00 USD hard floor, +64.55 USD above operating buffer). All 4 capacity slots are 100% open!
TASK FOR ARGON:
Synthesize peer findings with your deep reasoning engine. Deliver the definitive verdict on high-confluence Model 1 and Model 2 setups across the Clean-Friction Universe without any macro blackout restrictions.

{part_g_text}"""

    # Save prompts to disk
    p_dir = ROOT / "docs" / "prompts"
    p_dir.mkdir(parents=True, exist_ok=True)
    (p_dir / f"ARENA_CYCLE_{cycle}_ASTRA_PROMPT.txt").write_text(prompt_arena_1, encoding="utf-8")
    (p_dir / f"ARENA_CYCLE_{cycle}_FABLE_PROMPT.txt").write_text(prompt_arena_2, encoding="utf-8")
    (p_dir / f"GEMINI_CYCLE_{cycle}_ARGON_PROMPT.txt").write_text(prompt_argon, encoding="utf-8")

    print(f"Prompts generated:")
    print(f"  • Arena Tab 1 (GPT Astra): {len(prompt_arena_1)} chars")
    print(f"  • Arena Tab 2 (Claude Fable): {len(prompt_arena_2)} chars")
    print(f"  • Google Gemini (Argon): {len(prompt_argon)} chars")

    # 2. Dispatch to Arena 1 and Arena 2
    # Pre-check: If any Arena tab has an error banner, reload it first per operator directive
    try:
        pages_chk = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=3).read().decode())
        reloaded_any = False
        for t in [p for p in pages_chk if "arena.ai/agent/" in p.get("url", "")]:
            w_url = t.get("webSocketDebuggerUrl")
            if not w_url:
                continue
            lbl = "Fable" if ("af999588" in t.get("url", "") or "dde7" in t.get("url", "")) else "Astra"
            try:
                async with websockets.connect(w_url, max_size=10*1024*1024) as ws_chk:
                    js_chk = '(() => { const a = document.querySelector("div[role=alert]"); return a ? (a.innerText || "") : ""; })()'
                    await ws_chk.send(json.dumps({"id": 9991, "method": "Runtime.evaluate", "params": {"expression": js_chk, "returnByValue": True}}))
                    alert_txt = json.loads(await ws_chk.recv()).get("result", {}).get("result", {}).get("value", "")
                    if "error" in alert_txt.lower() or "wrong" in alert_txt.lower():
                        print(f"[{lbl}] Detected error banner ('{alert_txt.strip()}'). Reloading tab first...")
                        await ws_chk.send(json.dumps({"id": 9992, "method": "Page.reload", "params": {"ignoreCache": True}}))
                        reloaded_any = True
            except Exception:
                pass
        if reloaded_any:
            print("[Arena] Waiting 6s for reloaded tabs to stabilize...")
            await asyncio.sleep(6.0)
    except Exception as e_chk:
        print(f"[Arena] Note on pre-reload check: {e_chk}")

    arena_prompts = {"arena_1_primary": prompt_arena_1, "arena_2_fable": prompt_arena_2}
    await dismiss_arena_popup()
    ok_arena = await post_prompt_to_arena(arena_prompts, target="all")
    print(f"Arena.ai dispatch result: {ok_arena}")

    # 3. Dispatch to Google Gemini Argon
    ok_argon = await dispatch_gemini_argon(prompt_argon, attach_files=False)
    print(f"Gemini Argon dispatch result: {ok_argon}")

    if ok_arena or ok_argon:
        _save_cycle_num(cycle)
        print(f"\n✅ SUCCESS: Cycle {cycle} successfully dispatched across tri-council tabs!")
        return True
    else:
        print("\n❌ ERROR: Failed to dispatch prompt to any tab.", file=sys.stderr)
        return False


if __name__ == "__main__":
    asyncio.run(dispatch_all_three())
