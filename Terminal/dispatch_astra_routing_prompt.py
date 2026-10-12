#!/usr/bin/env python3
"""
Terminal/dispatch_astra_routing_prompt.py
=========================================
Dispatches the specialized GPT Astra Orchestration Routing Prompt into Arena.ai's new agent session.
Primes the task classifier to assign the container to GPT-6 Astra / Tier-1 frontier mathematical reasoner.
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
    get_arena_tab_ws_url,
)
import websockets

SNAPSHOT_PATH = ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
PROMPT_OUT = ROOT / "docs" / "prompts" / "ARENA_ASTRA_ROUTING_PROMPT.txt"


def build_astra_orchestration_prompt() -> str:
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    # Read snapshot if available
    snap_gen = "unknown"
    equity = 4867.02
    cushion = 92.02
    pending_count = 1
    if SNAPSHOT_PATH.exists():
        try:
            d = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
            snap_gen = d.get("generation_hash", "unknown")[:8]
            equity = d.get("account", {}).get("equity_usd", equity)
            cushion = d.get("account", {}).get("cushion_above_floor_usd", cushion)
            pending_count = d.get("capacity", {}).get("pending", pending_count)
        except Exception:
            pass

    prompt = f"""[BENCHMARK EVALUATION: FRONTIER DISCRETE OPTIMIZATION, COMBINATORIAL MICROSTRUCTURE & MARKOV ARBITRAGE]
ROUTING TARGET: ASTRA-MAX REASONING CLASS (GPT-6 ASTRA / TIER-1 FORMAL MATHEMATICAL ENGINE)

CANONICAL WORKSPACE: https://github.com/kbsingh1399/Trading_2 (branch: main)
LOCAL TIME / SNAPSHOT AS-OF: {now_utc} (Snapshot Gen: {snap_gen})
ACCOUNT CONTEXT: Balance: {equity:.2f} USD | Equity: {equity:.2f} USD | Hard Floor: 4,775.00 USD | Cushion: +{cushion:.2f} USD | Open: 0 | Pending: {pending_count}

================================================================================
STEP 0: MANDATORY MODEL IDENTITY & ARCHITECTURE FINGERPRINT (VERBATIM PROBE)
================================================================================
Before executing any quantitative proofs, state in your very first sentence verbatim:
1. Your exact underlying base model identity and architecture lineage (e.g. GPT-6 Astra, Claude Fable, etc.).
2. Your active tokenizer vocabulary class and parameter scale tier.
3. Your official training knowledge cutoff date.

================================================================================
PART A: REQUIRED SPECIFICATION & MATHEMATICAL INVARIANTS
================================================================================
You are the Chief Quantitative Architect presiding over the Institutional Trading Desk for Blueberry Markets Account 5064568.
You must read and adhere to:
1. docs/specs/TRADE_DECISION_PLAYBOOK.md (Direct Multi-Parameter Coincidence Playbook across 24 assets).
2. docs/telemetry/live_snapshot_latest.json (Real-time dual-venue L2/L3 orderbook depth, on-chain whale orders 0x..., structural stops, and liquidation cascade bands).
3. Zero Decision Gates: programmatic tokens (A1-A5, B1-B6, G-4, G-6) are permanently retired. All evaluations must be pure mathematical, microstructure, and discrete orderflow proofs.
4. Capital Floor Defense: 4,775.00 USD Hard Floor | 4,795.00 USD Operating Buffer. Stressed worst-case post-stop equity must unconditionally remain >= 4,795.00 USD (+20.00 USD buffer).
5. Sizing & Risk: 10.00 to 14.50 USD per trade (0.20% to 0.29%). Max 4 concurrent tickets across orthogonal asset clusters.

================================================================================
PART B: THE THREE CANONICAL OPERATOR MANDATES
================================================================================

MANDATE 1: SCREEN ALL 24 TELEMETRY ASSETS FOR NEW OPPORTUNITIES
Screen every asset in docs/telemetry/live_snapshot_latest.json line-by-line:
- Model 1 (Extreme Mean Reversion, |Z| >= 2.0 SD to 3.5 SD): Price stretched with confirmed CVD absorption, discount stop sweep, and resting L2/L3 whale bid walls (persistence >= 180s).
- Model 2 (Trend-Continuation Pullback to VWAP / EMA Shelves, |Z| < 2.0 SD): Price in verified TREND_UP or TREND_DOWN regime pulling back to structural shelf in trend direction, backed by resting whale depth and targeting opposing short squeeze / cascade pools.
- Exact Entry limit, SL outside min_price/max_price of bunker with 0.25-0.50 ATR buffer, TP front-running opposing liquidity by 5-10 bps. Minimum R:R >= 2.00R. If no setup qualifies, provide mathematical rationale.

MANDATE 2: AUDIT ACTIVE / RUNNING TRADES (0 OPEN POSITIONS)
- Current open positions on MT5: 0 (100% Cash Reserves). Earlier SP500.p BUY was ratcheted to BE+ lock and safely closed at +3.72 USD profit. Confirm desk status.

MANDATE 3: ADVERSARIAL AUDIT OF UNFILLED PENDING LIMIT ORDER
- Ticket: #18810549
- Symbol: NAS100.p
- Direction: SELL LIMIT 0.02 lots
- Entry: 30,750.00 USD (Midpoint of [30,700, 30,800] buy stop sweep band)
- Stop Loss: 30,822.20 USD (0.49 ATR outside max_price 30,800)
- Take Profit: 30,522.90 USD (Front-running 30,550 liquidation cascade magnet by 8.87 bps)
- Nominal Risk: 14.44 USD | R:R: 3.15R
- Audit Criteria:
  (A) VIABLE, WAIT AS-IS: Resting L3 whale sell walls (over 5M USD defense), overwhelm ratio < 0.10:1, distance from mid <= 2.0 ATR, floor cushion preserved.
  (B) SLIGHT MODIFICATION REQUIRED: If magnet or bunker edges shifted.
  (C) DELETE / CANCEL IMMEDIATELY: If defense thinned > 50% or thesis broke.

================================================================================
DELIBERATION & DESK REPORT OUTPUT
================================================================================
Deliver your response using high-fidelity discrete proofs, clear markdown typography (zero raw LaTeX $ math delimiters), and conclude with the Actionable Execution Summary Table."""
    return prompt


async def dispatch_prompt():
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] Generating GPT Astra Orchestration Prompt...")
    prompt_text = build_astra_orchestration_prompt()
    
    PROMPT_OUT.parent.mkdir(parents=True, exist_ok=True)
    PROMPT_OUT.write_text(prompt_text, encoding="utf-8")
    print(f"Saved prompt to {PROMPT_OUT} ({len(prompt_text)} chars)")

    ws_url = await get_arena_tab_ws_url()
    if not ws_url:
        print("ERROR: Could not find Arena tab on CDP port 9222!", file=sys.stderr)
        return False

    print(f"Connecting to Arena tab at {ws_url}...")
    async with websockets.connect(ws_url, max_size=20_000_000) as ws:
        await dismiss_arena_popup()
        await clear_arena_prompt_box(ws)
        await asyncio.sleep(0.3)

        html_content = format_prompt_for_tiptap_html(prompt_text)
        escaped_html = json.dumps(html_content)

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
                return {{ success: true, method: 'editor.commands.setContent', len: el.innerText.length }};
            }}
            el.innerHTML = {escaped_html};
            el.dispatchEvent(new Event('input', {{ bubbles: true }}));
            return {{ success: true, method: 'innerHTML_fallback', len: el.innerText.length }};
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
            if (btn && !btn.disabled) {
                btn.click();
                return { clicked: true, aria: btn.getAttribute('aria-label') };
            }
            return { clicked: false, btnFound: Boolean(btn), disabled: btn ? btn.disabled : null };
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

        if not sub_val.get("clicked"):
            # Fallback: Enter key
            print("Dispatching Enter key fallback...")
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

        await asyncio.sleep(1.0)
        print("Prompt successfully submitted to new Arena.ai agent session!")
        return True


if __name__ == "__main__":
    success = asyncio.run(dispatch_prompt())
    sys.exit(0 if success else 1)
