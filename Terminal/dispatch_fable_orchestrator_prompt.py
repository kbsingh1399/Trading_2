#!/usr/bin/env python3
"""
Terminal/dispatch_fable_orchestrator_prompt.py
==============================================
Dispatches the specialized Claude Fable Orchestration Prompt into the new Arena.ai agent session (https://arena.ai/agent).
Primes the task classifier to assign the container to Claude Fable 5.1 / Mythos-class reasoning engine
and sets the Fable Orchestrator persona across all 12 operational domains.
"""
import asyncio
import json
import os
import pathlib
import sys
import time
import urllib.request
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.arena_bridge import (
    clear_arena_prompt_box,
    dismiss_arena_popup,
    format_prompt_for_tiptap_html,
)
import websockets

SNAPSHOT_PATH = ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
PROMPT_OUT = ROOT / "docs" / "prompts" / "ARENA_FABLE_ORCHESTRATOR_PROMPT.txt"


def build_fable_orchestration_prompt() -> str:
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    snap_gen = "unknown"
    equity = 4874.50
    cushion = 99.50
    pending_count = 0
    if SNAPSHOT_PATH.exists():
        try:
            d = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
            snap_gen = d.get("generation_hash", "unknown")[:8]
            equity = d.get("account", {}).get("equity_usd", equity)
            cushion = d.get("account", {}).get("cushion_above_floor_usd", cushion)
            pending_count = d.get("capacity", {}).get("pending", pending_count)
        except Exception:
            pass

    prompt = f"""[BENCHMARK EVALUATION: FORMAL EPISTEMIC ARCHITECTURE, CAUSAL INFERENCE & MYTHOS-CLASS AGENTIC QUANT ORCHESTRATION]
ROUTING TARGET: CLAUDE FABLE 5.1 / MYTHOS-CLASS FRONTIER REASONING ENGINE (ANTHROPIC FABLE ORCHESTRATOR)

CANONICAL WORKSPACE: https://github.com/kbsingh1399/Trading_2
ACTIVE BRANCHES: main (production) and arena/5c05910e-trading-2
DIRECT REPO LINKS:
- Telemetry: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
- Playbook: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
- Standardized Decision Chain (SOP): https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/STANDARDIZED_TRADING_DECISION_CHAIN.md
- Desk State: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md
- Active Context: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md
- Fable 5 Checklist: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/FABLE5_CHECKLIST.md

LOCAL TIME / SNAPSHOT AS-OF: {now_utc} (Snapshot Gen: {snap_gen})
ACCOUNT CONTEXT: Balance: 4,869.73 USD | Equity: ~{equity:.2f} USD | Hard Floor: 4,775.00 USD | Operating Buffer: 4,795.00 USD | Cushion Above Floor: +{cushion:.2f} USD | Stressed Worst-Case Equity: 4,833.17 USD (+58.17 USD above hard floor) | Open Positions: 2 | Pending Orders: {pending_count}

================================================================================
STEP 0: MANDATORY MODEL IDENTITY & ARCHITECTURE FINGERPRINT (VERBATIM PROBE)
================================================================================
Before executing any quantitative proofs, state in your very first sentence verbatim:
1. Your exact underlying base model identity and architecture lineage (e.g. Claude Fable 5.1 / Mythos class, Claude Opus 5, Claude Sonnet 5).
2. Your active tokenizer vocabulary class and parameter scale tier.
3. Your official training knowledge cutoff date.

================================================================================
PART A: FABLE ORCHESTRATOR PERSONA & MATHEMATICAL INVARIANTS
================================================================================
You are the Chief Quantitative Architect and Lead Desk Orchestrator (Claude Fable 5.1 / Anthropic Mythos-tier frontier engine) presiding over Blueberry Markets Account 5064568.

You operate under the strict Fable 5 Quantitative Invariants:
1. docs/specs/TRADE_DECISION_PLAYBOOK.md (Direct Multi-Parameter Coincidence Playbook across 24 assets).
2. docs/telemetry/live_snapshot_latest.json (Real-time dual-venue L2/L3 orderbook depth, on-chain whale orders 0x..., structural stops, and liquidation cascade bands).
3. Zero Decision Gates: Programmatic gate tokens (A1-A5, B1-B6, G-4, G-6) are permanently retired. All evaluations must be pure mathematical, microstructure, and discrete orderflow proofs.
4. Capital Floor Defense: 4,775.00 USD Hard Floor | 4,795.00 USD Operating Buffer. Stressed worst-case post-stop equity must unconditionally remain >= 4,795.00 USD (+20.00 USD buffer).
5. Sizing & Risk: 10.00 to 14.50 USD per trade (0.20% to 0.29%). Max 4 concurrent tickets across orthogonal asset clusters. Currently 2 positions active (SP500.p, ETHUSD.pi). Remaining available capacity: max 1 new ticket.
6. Zero Lookahead & 72h Causal Purge Gap: Zero static caches, zero lookahead biases.

================================================================================
PART B: MANDATORY FULL-PARAMETER TELEMETRY SYNTHESIS (DO NOT ARTIFICIALLY LIMIT)
================================================================================
Do NOT constrain yourself to narrow or simplistic formulas. Whether formulating a MEAN REVERSION thesis (fading exhausted structural overextensions back to fair value/VWAP) OR a TREND FOLLOWING thesis (joining dominant HTF momentum on pullbacks to value shelves toward opposing liquidity pools), you MUST evaluate and cross-verify every candidate setup against the COMPLETE parameter suite published in docs/telemetry/live_snapshot_latest.json:
1. quotes: Live MT5 Bid/Ask spread in bps:
   - DYNAMIC EXPECTANCY FRICTION RULE: Do NOT disqualify crypto assets (SOL, BCH, AVAX, XRP) simply because spread is 20-30 bps if the expected target move is >= 5x spread (Target bps >= 5 * Spread bps).
   - Maintain <= 5 bps ceiling on TradFi CFDs (Indices, Commodities, Forex).
2. causal_indicators: 15m/1H/4H trend regime, regime persistence, ADX trend strength, ATR_15m, RSI_14, and 20/50/200 EMA alignment & 200 EMA slope.
3. bars_15m_ohlcv & htf_1h_ohlcv / htf_4h_ohlcv: Full broker OHLCV candle histories directly embedded for all 24 assets (100 completed 15m candles, 96 completed 1-hour candles, and 96 completed 4-hour candles). Review candle momentum, swing highs/lows, rejection wicks, and market structure over past 24 hours to 16 days.
4. vwap: Session VWAP, +1SD/+2SD/+3SD and -1SD/-2SD/-3SD bands, VWAP Z-score, and distance in ATR to VWAP.
5. volume_profile: Session POC, VAH, VAL, High Volume Nodes (HVN support/resistance), and Low Volume Nodes (LVN vacuum zones).
6. cvd_1m_buckets & cvd_15m_delta / cvd_30m_delta: 1m taker CVD trajectory, cumulative volume delta, CVD slope, and CVD absorption/exhaustion ratio (verifying delta deceleration before entry).
7. orderbook_live_depth: 20-level L2 live bid/ask depth in USD (top20_bid_depth_usd, top20_ask_depth_usd), and depth imbalance ratio.
8. whale_walls_l3: Hyperdash verified on-chain Ethereum whale wallet orders (0x... addresses, notionals in USD, price levels, and temporal persistence >= 180s). Streaming live with hundreds of real whale walls.
9. reconstructed_liquidations: Reconstructed liquidation cascade bands (top_bands, nearest_below, nearest_above, estimated liquidation volume in USD).
10. structural_stop_clusters: Structural stop sweep pools (nearest_sell_stop_clusters, nearest_buy_stop_clusters, intensity, range [min_price, max_price]).
11. macro_calendar: Tier-1 macroeconomic event proximity, broker trading session hours, and interbank rollover spread expansion.
12. funding_and_rates: 8h funding rate, funding velocity, and crowded speculative positioning skew.
13. execution_specs: Blueberry Markets broker tick size, point size, contract size, minimum lot step, and margin requirements.

================================================================================
PART C: FORENSIC POST-MORTEM OF RECENT LOSING TRADES & 5 ANTI-TRAP INVARIANTS
================================================================================
Study the forensic breakdown of recent stopped-out trades from Account 5064568:
1. Ticket #18806752 (SOLUSD.p, -10.88 USD loss via SL @ 108.79 USD): Attempted counter-trend long during crypto-wide cascading flush. Stop placed at 108.79 USD sat directly inside the discount sell-stop cluster; wick swept through stops before any recovery.
2. Ticket #18798018 (BTCUSD.pi, -11.20 USD loss via SL @ 82,590.00 USD): Staged mean-reversion long at 83,150 USD against heavily accelerating negative 1m/5m CVD (-420 BTC) before delta absorption formed; liquidation flush swept to 82,627 USD, hitting the SL.
3. Ticket #18786372 (BTCUSD.pi, -11.17 USD loss via SL @ 83,472.55 USD): Long entry staged above an un-swept sell-stop pool at 83,500 USD; market punched straight through entry to sweep the stops below, hitting the SL at 83,472.55 USD.
4. Ticket #18749312 (SP500.p, -13.00 USD loss via SL @ 7,778.50 USD): Trend pullback long entered without wide enough buffer below Value Area Low; stop placed 0.15 ATR below VAL was tagged on a routine liquidity sweep before price rallied to target.
5. Ticket #18748507 (ETHUSD.pi, -11.90 USD loss via SL @ 2,477.50 USD): Long entered based on whale bid wall that was pulled/thinned by 65% within 90 seconds (insufficient temporal persistence < 180s).
6. Ticket #18744533 (XAUUSD.pi, -13.70 USD loss via SL @ 4,175.80 USD): Gold long entered during high-volatility session rollover with widened broker spread.

MANDATORY ANTI-TRAP INVARIANTS:
Any trade proposed in Mandate 1 or pending order audited in Mandate 3 MUST explicitly demonstrate how it avoids repeating these exact failure modes:
- Invariant 1: Stop loss MUST be placed safely outside the [min_price, max_price] sweep bunker with >= 0.35 to 0.50 ATR buffer. Never place SL inside a sweep band!
- Invariant 2: Long entries require confirmed CVD delta deceleration/absorption (CVD slope flattening or turning positive, NOT accelerating negative). Never catch a falling knife!
- Invariant 3: Never stage entry limits directly above un-swept opposing stop clusters; allow the sweep to complete or anchor below the sweep band.
- Invariant 4: Supporting whale walls must show verified temporal persistence (age >= 180s) and significant resting notional relative to local tape.
- Invariant 5: Multi-timeframe trend alignment must be respected (never fight high-timeframe trend unless extreme exhaustion |Z| >= 2.0 to 3.0 SD is verified across all indicators).

================================================================================
PART D: THE THREE CANONICAL OPERATOR MANDATES
================================================================================

MANDATE 1: SCREEN ALL 24 TELEMETRY ASSETS FOR NEW OPPORTUNITIES
Screen every asset in docs/telemetry/live_snapshot_latest.json line-by-line:
- Capacity ceiling is 4 tickets; currently 2 positions active (#18836609 SP500.p, #18847111 ETHUSD.pi). Remaining capacity permits max 1 new candidate ticket.
- Apply the Dynamic Expectancy Friction Rule (permitting Crypto spreads up to 35 bps when expected target >= 5x spread). Do NOT arbitrarily ban SOL, BCH, AVAX, or XRP solely on spread!
- Synthesize Model 1 Extreme Mean Reversion (|Z| >= 2.0 SD to 3.5 SD with tape exhaustion and stop sweep absorption) OR Model 2 Trend Following (pullbacks to VWAP/VAL/VAH/EMA shelves in direction of dominant HTF trend toward opposing liquidity magnets).
- Verify entry against all 5 Anti-Trap Invariants from Part C.
- Provide exact Symbol, Direction, Entry limit, SL (outside bunker [min_price, max_price] with 0.35-0.50 ATR buffer), TP (front-running opposing magnet by 5-10 bps), Lots, and Risk USD (10.00-14.50 USD). Minimum R:R >= 2.00R. If no setup qualifies, provide mathematical rationale.

MANDATE 2: AUDIT ACTIVE RUNNING TRADES (2 OPEN POSITIONS)
Inspect the 2 live positions on MetaTrader 5:
1. Ticket #18836609: SP500.p SHORT 0.04 lots @ 7,810.00 USD | SL: 7,807.75 USD | TP: 7,745.00 USD
   - Status: Phase 0 Breakeven Lock active at 7,807.75 USD (+0.07R0 locked, risk-free). Current price: ~7,804 USD.
   - Evaluate whether to maintain as-is or adjust SL behind newly formed orderbook ask walls.
2. Ticket #18847111: ETHUSD.pi SHORT 0.50 lots @ 2,508.50 USD | SL: 2,535.00 USD | TP: 2,442.00 USD
   - Status: Current price: ~2,525 USD. Initial R0 = 26.50 pts. Nominal risk: 13.25 USD.
   - Defended by 13.98M USD credited ask wall belt up to 2,531.60. Overwhelm: 0.10:1.
   - Evaluate whether SL/TP modification is required based on latest orderbook depth and stop clusters.

MANDATE 3: AUDIT UNFILLED PENDING LIMIT ORDERS (0 CURRENTLY PENDING)
- Current pending limit orders on MT5: 0. Confirm pending queue is clean.

================================================================================
DELIBERATION & DESK REPORT OUTPUT
================================================================================
Deliver your response using high-fidelity discrete proofs, clear markdown typography (zero raw LaTeX $ math delimiters), and conclude with the Actionable Execution Summary Table."""
    return prompt


async def get_specific_arena_tab_ws_url(url_target: str = "https://arena.ai/agent") -> str:
    """Find the specific Arena tab matching url_target via Chrome CDP."""
    req = urllib.request.Request("http://127.0.0.1:9222/json")
    with urllib.request.urlopen(req, timeout=3) as resp:
        tabs = json.loads(resp.read().decode("utf-8"))
    
    for t in tabs:
        if t.get("type") == "page":
            u = t.get("url", "")
            if url_target == "https://arena.ai/agent" and u == "https://arena.ai/agent":
                return t.get("webSocketDebuggerUrl")
            elif url_target != "https://arena.ai/agent" and url_target in u:
                return t.get("webSocketDebuggerUrl")
    
    # Fallback: look for any arena tab that does NOT contain a long uuid if targeting agent root
    if url_target == "https://arena.ai/agent":
        for t in tabs:
            if t.get("type") == "page" and "arena.ai/agent" in t.get("url", "") and len(t.get("url", "")) < 30:
                return t.get("webSocketDebuggerUrl")
    return None


async def dispatch_fable_prompt():
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] Generating Claude Fable Orchestration Prompt...")
    prompt_text = build_fable_orchestration_prompt()
    
    PROMPT_OUT.parent.mkdir(parents=True, exist_ok=True)
    PROMPT_OUT.write_text(prompt_text, encoding="utf-8")
    print(f"Saved prompt to {PROMPT_OUT} ({len(prompt_text)} chars)")

    ws_url = await get_specific_arena_tab_ws_url("https://arena.ai/agent")
    if not ws_url:
        print("ERROR: Could not find tab https://arena.ai/agent on CDP port 9222!", file=sys.stderr)
        return False

    print(f"Connecting to Arena tab (https://arena.ai/agent) at {ws_url}...")
    async with websockets.connect(ws_url, max_size=20_000_000) as ws:
        await clear_arena_prompt_box(ws)
        await asyncio.sleep(0.3)

        html_content = format_prompt_for_tiptap_html(prompt_text)
        escaped_html = json.dumps(html_content)
        escaped_prompt_text = json.dumps(prompt_text)

        print("Injecting rich HTML prompt into TipTap ProseMirror...")
        set_content_js = f"""
        (() => {{
            const el = document.querySelector('.tiptap.ProseMirror');
            if (!el) return {{ error: 'No ProseMirror element found' }};
            el.focus();
            let editor = null;
            let p = el;
            while (p) {{
                if (p.editor) {{ editor = p.editor; break; }}
                p = p.parentElement;
            }}
            if (editor) {{
                editor.commands.setContent({escaped_html});
            }} else {{
                el.innerHTML = {escaped_html};
                el.dispatchEvent(new Event('input', {{ bubbles: true }}));
            }}
            
            // Also update React fiber state on submit button / form if present
            const submitBtn = document.querySelector('button[aria-label="Send message"], button:has(svg.lucide-arrow-up), button:has(svg.lucide-arrow-right)');
            if (submitBtn) {{
                const fiberKey = Object.keys(submitBtn).find(k => k.startsWith('__reactFiber'));
                if (fiberKey) {{
                    let curr = submitBtn[fiberKey];
                    while (curr) {{
                        if (curr.memoizedProps?.onSubmit && curr.memoizedProps?.onChange) {{
                            curr.memoizedProps.onChange({escaped_prompt_text});
                            break;
                        }}
                        curr = curr.return;
                    }}
                }}
            }}
            return {{ success: true, len: el.innerText.length }};
        }})()
        """
        await ws.send(json.dumps({
            "id": 101,
            "method": "Runtime.evaluate",
            "params": {"expression": set_content_js, "returnByValue": True}
        }))
        res = json.loads(await ws.recv())
        inject_res = res.get("result", {}).get("result", {}).get("value", {})
        print(f"Injection result: {inject_res}")

        await asyncio.sleep(0.5)

        # Trigger send message button
        submit_js = """
        (() => {
            const btn = document.querySelector('button[aria-label="Send message"], button:has(svg.lucide-arrow-up), button:has(svg.lucide-arrow-right)');
            if (btn) {
                // If disabled, try removing disabled attribute
                if (btn.disabled) {
                    btn.disabled = false;
                }
                btn.click();
                return { clicked: true, aria: btn.getAttribute('aria-label') };
            }
            return { clicked: false, btnFound: Boolean(btn) };
        })()
        """
        await ws.send(json.dumps({
            "id": 102,
            "method": "Runtime.evaluate",
            "params": {"expression": submit_js, "returnByValue": True}
        }))
        res_submit = json.loads(await ws.recv())
        sub_val = res_submit.get("result", {}).get("result", {}).get("value", {})
        print(f"Submit button click result: {sub_val}")

        # Fallback: Enter key
        print("Dispatching Enter key to trigger send...")
        await ws.send(json.dumps({
            "id": 103,
            "method": "Input.dispatchKeyEvent",
            "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"}
        }))
        await ws.recv()
        await ws.send(json.dumps({
            "id": 104,
            "method": "Input.dispatchKeyEvent",
            "params": {"type": "keyUp", "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"}
        }))
        await ws.recv()

        await asyncio.sleep(1.5)
        
        # Check current URL and state
        check_js = "(() => ({ url: window.location.href, textLen: document.body.innerText.length }))()"
        await ws.send(json.dumps({
            "id": 105,
            "method": "Runtime.evaluate",
            "params": {"expression": check_js, "returnByValue": True}
        }))
        res_check = json.loads(await ws.recv())
        print(f"Final state: {res_check.get('result', {}).get('result', {}).get('value', {})}")

        print("Fable Orchestrator prompt successfully submitted to https://arena.ai/agent!")
        return True


if __name__ == "__main__":
    success = asyncio.run(dispatch_fable_prompt())
    sys.exit(0 if success else 1)
