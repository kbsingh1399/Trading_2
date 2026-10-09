#!/usr/bin/env python3
"""
Terminal/copilot_studio_bridge.py
=================================
Automated Chrome DevTools Protocol (CDP) Bridge for Microsoft Copilot Studio (Claude Opus 5.5).

Replaces legacy Arena.ai bridge:
- Connects directly to Copilot Studio running in Chrome (debug mode on port 9222).
- Automatically posts prompts, dispatches native inputs, monitors reasoning/thinking states,
  and extracts completed quantitative rulings.
- Strictly embeds the Mandatory Pre-Flight Session History Review & Second Brain Directive:
  * .agents/memory/session_chat_history.md (Trajectory, avoided traps, operator directives)
  * .agents/rules/ACTIVE_CONTEXT.md (Live account state, floor cushion)
  * docs/specs/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md (Thinking Chain V2.0)
- Seamlessly updates docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md.
"""

import os
import sys
import json
import time
import asyncio
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Tuple, Dict, Any

try:
    import websockets
except ImportError:
    print("Error: websockets library required. Install with: pip install websockets", file=sys.stderr)
    sys.exit(1)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CDP_HTTP_URL = "http://127.0.0.1:9222"

PRIMARY_ASSETS = [
    "BTC", "ETH", "SOL", "DOGE", "ADA", "TRX", "LINK", "DOT", "LTC", "BCH", "AVAX", "NEAR",
    "USWTI", "GOLD", "SILVER", "EURUSD", "GBPUSD", "USDJPY", "SP500", "NAS100", "DJ30", "GER40"
]


def get_copilot_studio_ws_url() -> Optional[str]:
    """Find the Copilot Studio tab via Chrome remote debugging JSON endpoint."""
    try:
        req = urllib.request.Request(f"{CDP_HTTP_URL}/json")
        with urllib.request.urlopen(req, timeout=3) as resp:
            tabs = json.loads(resp.read().decode("utf-8"))
        for t in tabs:
            url = t.get("url", "")
            title = t.get("title", "")
            if t.get("type") == "page" and ("copilotstudio.microsoft.com" in url or "Agents" in title):
                return t.get("webSocketDebuggerUrl")
    except Exception as e:
        print(f"Error fetching Chrome tabs: {e}", file=sys.stderr)
    return None


def build_copilot_studio_prompt() -> str:
    """
    Construct the canonical quantitative prompt for Claude Opus 5.5 in Copilot Studio.
    Strictly embeds:
    - Mandatory Section 0: Context continuity, session history review, active context, and Thinking Chain V2.0.
    - Live MT5 account state (balance, equity, cushion, tickets).
    - Dual-engine review mandate (Model 1 Mean Reversion vs Model 2 Trend Pullbacks).
    - 24-asset orderflow and market structure telemetry.
    """
    # 1. Fetch live MT5 state
    balance = 4896.55
    equity = 4896.55
    margin_used = 0.0
    margin_free = 4896.55
    cushion = equity - 4775.0
    active_pos = []
    pending_ord = []

    try:
        import MetaTrader5 as mt5
        if mt5.initialize():
            acc_info = mt5.account_info()
            if acc_info:
                balance = float(acc_info.balance)
                equity = float(acc_info.equity)
                margin_used = float(acc_info.margin)
                margin_free = float(acc_info.margin_free)
                cushion = equity - 4775.0

            positions = mt5.positions_get()
            if positions:
                for p in positions:
                    direction = "LONG" if p.type == 0 else "SHORT"
                    r_mult = round((p.price_current - p.price_open) / max(abs(p.price_open - p.sl), 1e-6), 2) if p.sl else "N/A"
                    active_pos.append({
                        "ticket": p.ticket,
                        "symbol": p.symbol,
                        "type": direction,
                        "volume": p.volume,
                        "price_open": p.price_open,
                        "price_current": p.price_current,
                        "sl": p.sl,
                        "tp": p.tp,
                        "profit": round(p.profit, 2),
                        "r_multiple": r_mult
                    })

            orders = mt5.orders_get()
            if orders:
                for o in orders:
                    o_type = "BUY_LIMIT" if o.type == 2 else "SELL_LIMIT" if o.type == 3 else f"ORDER_{o.type}"
                    dist = round(abs(o.price_open - o.price_current), 4)
                    pending_ord.append({
                        "ticket": o.ticket,
                        "symbol": o.symbol,
                        "type": o_type,
                        "volume": o.volume_initial,
                        "price_open": o.price_open,
                        "price_current": o.price_current,
                        "sl": o.sl,
                        "tp": o.tp,
                        "dist_pts": dist
                    })
            mt5.shutdown()
    except Exception as e:
        print(f"Warning: Direct MT5 read fallback: {e}", file=sys.stderr)

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    lines = []
    lines.append("=" * 80)
    lines.append("QUANTITATIVE ORDER DESK COLLABORATIVE BRIEFING | COPILOT STUDIO (OPUS 5.5)")
    lines.append(f"CYCLE TIMESTAMP: {now_utc}")
    lines.append("=" * 80)
    lines.append("")
    lines.append("[SECTION 0: MANDATORY PRE-FLIGHT CONTEXT REVIEW & SECOND BRAIN ORIENTATION]")
    lines.append("You are Claude Opus 5.5, operating as the Elite Chief Quantitative Strategist and Second Brain for the Antigravity Autonomous Order Desk.")
    lines.append("MANDATORY GITHUB REPOSITORY LINK: https://github.com/kbsingh1399/Trading_2 (Branch: main)")
    lines.append("Before analyzing setups or proposing any order, you MUST study our live system trajectory and canonical specifications directly from GitHub:")
    lines.append("1. GitHub Repository Root: https://github.com/kbsingh1399/Trading_2")
    lines.append("2. Session Historical Memory: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md")
    lines.append("   - Review the complete session history to understand operator directives, historical setbacks, and avoided traps. Never evaluate in a vacuum!")
    lines.append("3. Active Operational Context: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md")
    lines.append("   - Review live account state, cash reserves, active tickets, and hard capital floor defense.")
    lines.append("4. Thinking Chain Protocol V2.0 Hardened: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md")
    lines.append("   - Strictly adhere to the 7-stage verification gates, EV over probability score, broker CFD spread mechanics, and 0-100 evidence arbitration rubric.")
    lines.append("5. Round 2 Thinking Chain Audit Report: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/reviews/ROUND2_THINKING_CHAIN_AUDIT.md")
    lines.append("6. Decision Gates V3 Reference Implementation: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/decision_gates_v3.py")
    lines.append("7. Master Agent Enforcement Rules: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/AGENTS.md")
    lines.append("8. Live 24-Asset Telemetry Snapshot JSON (Pushed to GitHub every 60s): https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json (Blob: https://github.com/kbsingh1399/Trading_2/blob/main/docs/telemetry/live_snapshot_latest.json)")
    lines.append("9. Live Collaborative Order Desk Blackboard (Pushed to GitHub): https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md")
    lines.append("")
    lines.append("[SECTION 1: LIVE MT5 ACCOUNT STATE & FLOOR DEFENSE]")
    lines.append(f"- Broker: MetaTrader 5 Account #5064568 (Blueberry Markets Demo Bridge)")
    lines.append(f"- Balance: {balance:.2f} USD | Equity: {equity:.2f} USD | Free Margin: {margin_free:.2f} USD (100% Cash Reserves | 0.00 Margin Used)")
    lines.append(f"- Hard Floor (G-1): 4,775.00 USD | Operating Buffer: 4,795.00 USD")
    lines.append(f"- Live Floor Cushion: +{cushion:.2f} USD above hard floor (+{equity - 4795.00:.2f} USD above operating buffer)")
    lines.append(f"- Capacity: Max 4 concurrent filled positions across orthogonal asset clusters (Forex, Metals/Energy, Equities, Crypto).")
    lines.append("")
    lines.append("[SECTION 2: ACTIVE POSITIONS & PENDING LIMIT ORDERS]")
    if active_pos:
        lines.append(f"ACTIVE POSITIONS ({len(active_pos)}):")
        for p in active_pos:
            lines.append(f"- Ticket #{p['ticket']}: {p['symbol']} {p['type']} {p['volume']} lots @ {p['price_open']} | Mark: {p['price_current']} | SL: {p['sl']} | TP: {p['tp']} | Floating: {p['profit']} USD ({p['r_multiple']}R)")
    else:
        lines.append("- Active Positions: NONE (0 Open Positions | 100% Cash Flat | 4 Slots Vacant)")

    if pending_ord:
        lines.append(f"RESTING PENDING LIMIT ORDERS ({len(pending_ord)}):")
        for o in pending_ord:
            lines.append(f"- Ticket #{o['ticket']}: {o['symbol']} {o['type']} {o['volume']} lots @ {o['price_open']} | Mark: {o['price_current']} | SL: {o['sl']} | TP: {o['tp']} | Dist: {o['dist_pts']} pts")
    else:
        lines.append("- Resting Pending Limit Orders: NONE (Queue clean)")
    lines.append("")
    lines.append("[SECTION 3: DUAL-ENGINE GATING & PRE-TRADE CHECKLIST MANDATE]")
    lines.append("You must rigorously evaluate both quantitative engines:")
    lines.append("1. MODEL 1: EXTREME MEAN REVERSION (|Z| >= 2.0 SD Fade)")
    lines.append("   - Price stretched to |Z| >= 2.0 SD from Session VWAP with RSI < 30 (Longs) or > 70 (Shorts).")
    lines.append("   - Orderflow: CVD divergence / aggressor selling exhaustion into resting bid absorption.")
    lines.append("   - Limit order resting at discount liquidity sweep level with structural SL.")
    lines.append("2. MODEL 2: TREND FOLLOWING (|Z| < 2.0 SD Volatility Pullbacks)")
    lines.append("   - Established trend regime (200 EMA slope, Variance Ratio VR > 1, Efficiency Ratio ER > 0.35).")
    lines.append("   - Pullback distance normalized by Price x Forecast Volatility (Yang-Zhang).")
    lines.append("   - Entry at verified geometric shelves (20/50 EMA, Value Area boundaries VAH/VAL).")
    lines.append("   - Anchored TP at overhead Short Squeeze Bands or Ask Whale Walls for >= 2.0R to 2.5R.")
    lines.append("3. MANDATORY MICROSTRUCTURE GATING:")
    lines.append("   - In MT5 CFDs, Buy Limits fill on Ask and exit on Bid. Maker orders DO NOT escape broker spread.")
    lines.append("   - Maximum allowable broker spread: 20.00 bps. Quarantine any symbol exceeding 20 bps.")
    lines.append("   - Positive conservative Expected Value (EV): P(win) x Net Gain - P(loss) x Max Loss - Frictions > 0.")
    lines.append("   - If neither engine produces positive EV with confirmed L2 depth, emit an unconditional STAND ASIDE.")
    lines.append("")
    lines.append("[SECTION 4: LIVE 24-ASSET ORDERFLOW & MARKET STRUCTURE TELEMETRY]")
    lines.append("Real-time telemetry across all 24 assets (Quotes, Spreads, VWAP Z-Scores, ATR, Orderbook Depths, Structural Bands):")
    lines.append("")
    snapshot_file = PROJECT_ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
    if snapshot_file.exists():
        try:
            with open(snapshot_file, "r", encoding="utf-8") as f:
                snap_data = json.load(f)
            matrix = snap_data.get("assets_matrix_24", {})
            for a_name, a_val in matrix.items():
                sym = a_val.get("symbol_broker", a_name)
                cat = a_val.get("category", "")
                q = a_val.get("quotes", {})
                mid = q.get("mid", 0.0)
                spr = q.get("spread_bps", 0.0)
                ind = a_val.get("causal_indicators", {})
                z = ind.get("vwap_z_score", "N/A")
                rsi = ind.get("rsi_14", "N/A")
                atr = ind.get("atr_14", "N/A")
                reg = ind.get("trend_regime", "N/A")
                ob = a_val.get("orderbook_live_depth", {})
                whales = ob.get("whale_walls_l3", [])
                lines.append(f"- {a_name} ({sym} | {cat}): Mid={mid} | Spread={spr:.2f} bps | VWAP_Z={z} SD | RSI={rsi} | ATR={atr} | Regime={reg}")
                if whales:
                    w_parts = [f"{w.get('side')} {w.get('notional_usd')} USD @ {w.get('price')}" for w in whales[:2]]
                    lines.append(f"  * L3 Whales: {', '.join(w_parts)}")
        except Exception as te:
            lines.append(f"Warning: Telemetry extraction fallback: {te}")
    lines.append("")
    lines.append("[SECTION 5: REQUIRED QUANTITATIVE DESK RULING]")
    lines.append("Provide your explicit quantitative ruling structured as:")
    lines.append("1. Existing Exposure Audit: Verdict on active tickets (HOLD, Ratchet, Resize, or Delete).")
    lines.append("2. Top 2 Candidate Orders (if any): Symbol, Direction, Entry Price, SL, TP, Lots, Risk USD, EV score.")
    lines.append("3. Or explicit STAND ASIDE / PUNCH NONE with mathematical justification.")
    lines.append("")
    return "\n".join(lines)


async def post_prompt_to_copilot_studio(prompt_text: str, ws_url: Optional[str] = None) -> bool:
    """
    Inject prompt text into Copilot Studio's chat box and submit via CDP.
    Uses native Input.insertText and Enter key dispatch.
    """
    if not ws_url:
        ws_url = get_copilot_studio_ws_url()
    if not ws_url:
        print("ERROR: Copilot Studio tab not found on Chrome port 9222", file=sys.stderr)
        return False

    async with websockets.connect(ws_url, max_size=10_000_000) as ws:
        # Step 1: Focus chat input
        focus_js = """
        (() => {
          const input = document.querySelector('[data-testid="chat-input-textarea"]');
          if (input) {
            input.focus();
            return true;
          }
          return false;
        })()
        """
        msg_id = int(time.time() * 1000) % 1000000
        await ws.send(json.dumps({
            "id": msg_id,
            "method": "Runtime.evaluate",
            "params": {"expression": focus_js, "returnByValue": True}
        }))
        res = json.loads(await ws.recv())
        focused = res.get("result", {}).get("result", {}).get("value", False)
        if not focused:
            print("ERROR: Failed to focus Copilot Studio chat input", file=sys.stderr)
            return False

        # Step 2: Clear any existing content in the input
        clear_js = """
        (() => {
          const input = document.querySelector('[data-testid="chat-input-textarea"]');
          if (input) {
            document.execCommand('selectAll', false, null);
            document.execCommand('delete', false, null);
          }
        })()
        """
        await ws.send(json.dumps({
            "id": msg_id + 1,
            "method": "Runtime.evaluate",
            "params": {"expression": clear_js, "returnByValue": True}
        }))
        await ws.recv()

        # Step 3: Insert text via CDP Input.insertText
        await ws.send(json.dumps({
            "id": msg_id + 2,
            "method": "Input.insertText",
            "params": {"text": prompt_text}
        }))
        await ws.recv()
        await asyncio.sleep(0.5)

        # Step 4: Click Send Button or fallback to Enter key
        submit_js = """
        (() => {
          const btn = document.querySelector('[data-testid="send-button"]') ||
                      document.querySelector('button[aria-label="Send"]') ||
                      document.querySelector('.fai-SendButton');
          if (btn && !btn.disabled) {
            btn.click();
            return { clicked: true, method: "button_click" };
          }
          return { clicked: false, method: "none" };
        })()
        """
        await ws.send(json.dumps({
            "id": msg_id + 3,
            "method": "Runtime.evaluate",
            "params": {"expression": submit_js, "returnByValue": True}
        }))
        submit_res = json.loads(await ws.recv())
        clicked = submit_res.get("result", {}).get("result", {}).get("value", {}).get("clicked", False)
        if not clicked:
            await ws.send(json.dumps({
                "id": msg_id + 4,
                "method": "Input.dispatchKeyEvent",
                "params": {
                    "type": "rawKeyDown",
                    "windowsVirtualKeyCode": 13,
                    "code": "Enter",
                    "key": "Enter"
                }
            }))
            await ws.recv()
            await ws.send(json.dumps({
                "id": msg_id + 5,
                "method": "Input.dispatchKeyEvent",
                "params": {
                    "type": "keyUp",
                    "windowsVirtualKeyCode": 13,
                    "code": "Enter",
                    "key": "Enter"
                }
            }))
            await ws.recv()
        return True


async def check_copilot_studio_response(ws_url: Optional[str] = None) -> Tuple[bool, str]:
    """
    Extract the latest response from Copilot Studio and determine if generation is complete.
    Returns (done: bool, response_text: str).
    """
    if not ws_url:
        ws_url = get_copilot_studio_ws_url()
    if not ws_url:
        return False, "Copilot Studio tab not found"

    async with websockets.connect(ws_url, max_size=10_000_000) as ws:
        check_js = """
        (() => {
          const stopBtn = document.querySelector('button[aria-label*="Stop"], button[title*="Stop"]');
          const isGenerating = !!stopBtn;

          const bodyText = document.body.innerText;
          const isThinking = bodyText.trim().endsWith("Thinking") || bodyText.includes("Thinking...");

          // Find assistant response bubbles
          const allBubbles = Array.from(document.querySelectorAll('[class*="___1tekf1z"]')).map(el => el.innerText || "").filter(t => t.length > 0);
          
          // Filter out error banners
          const validBubbles = allBubbles.filter(t => !t.includes("blocked by content filtering"));
          const lastValidText = validBubbles.length > 0 ? validBubbles[validBubbles.length - 1] : "";

          return {
            isGenerating: isGenerating || isThinking,
            bubblesCount: allBubbles.length,
            validBubblesCount: validBubbles.length,
            lastText: lastValidText
          };
        })()
        """
        msg_id = int(time.time() * 1000) % 1000000
        await ws.send(json.dumps({
            "id": msg_id,
            "method": "Runtime.evaluate",
            "params": {"expression": check_js, "returnByValue": True}
        }))
        res = json.loads(await ws.recv())
        val = res.get("result", {}).get("result", {}).get("value", {})
        is_gen = val.get("isGenerating", False)
        last_text = val.get("lastText", "")
        done = not is_gen and len(last_text) > 100
        return done, last_text


def run_full_copilot_cycle(wait_sec: int = 180):
    """
    Execute full collaborative cycle with Copilot Studio (Claude Opus 5.5):
    1. Build fresh quantitative prompt with full context.
    2. Post prompt to Copilot Studio.
    3. Wait for inference / reasoning.
    4. Extract ruling and log to LIVE_COLLABORATIVE_ORDER_DESK.md.
    """
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] Initiating Copilot Studio collaborative cycle...")
    ws_url = get_copilot_studio_ws_url()
    if not ws_url:
        print("ERROR: Copilot Studio tab not found on Chrome port 9222", file=sys.stderr)
        return False

    prompt = build_copilot_studio_prompt()
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] Submitting prompt to Copilot Studio ({len(prompt)} chars)...")
    posted = asyncio.run(post_prompt_to_copilot_studio(prompt, ws_url))
    if not posted:
        print("ERROR: Failed to post prompt to Copilot Studio", file=sys.stderr)
        return False

    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] Prompt submitted. Waiting {wait_sec}s for Opus 5.5 reasoning...")
    time.sleep(wait_sec)

    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] Checking Copilot Studio response...")
    done, resp_text = asyncio.run(check_copilot_studio_response(ws_url))
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] Generation complete: {done} | Length: {len(resp_text)} chars")
    print("--- COPILOT STUDIO FULL RESPONSE ---")
    print(resp_text)
    print("-----------------------------------")

    append_ruling_to_order_desk(resp_text)
    return done


def append_ruling_to_order_desk(resp_text: str) -> None:
    """Append harvested Opus 5.5 response to LIVE_COLLABORATIVE_ORDER_DESK.md."""
    desk_path = PROJECT_ROOT / "docs" / "trade_plans" / "LIVE_COLLABORATIVE_ORDER_DESK.md"
    if desk_path.exists() and len(resp_text) > 50:
        now_dt = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        import re
        content = desk_path.read_text(encoding="utf-8")
        matches = re.findall(r"## Section (\d+):", content)
        next_sec = max([int(m) for m in matches]) + 1 if matches else 45

        entry = f"\n\n---\n\n## Section {next_sec}: Autonomous Copilot Studio (Opus 5.5) Evaluation | {now_dt}\n\n"
        entry += f"### 1. Cycle Trigger & Context\n"
        entry += f"- **Council Engine**: Microsoft Copilot Studio (Claude Opus 5.5 - Chief Quantitative Strategist & Second Brain)\n"
        entry += f"- **Pre-Flight Context Review**: Mandatory Session Chat & Thinking Chain Protocol V2.0 Hardened\n"
        entry += f"- **Input Provenance**: Live 24-Asset Telemetry Snapshot & GitHub main\n\n"
        entry += f"### 2. Opus 5.5 Ruling & Quantitative Synthesis\n"
        entry += f"```text\n{resp_text}\n```\n\n"

        with open(desk_path, "a", encoding="utf-8") as f:
            f.write(entry)
        print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] Appended Section {next_sec} to LIVE_COLLABORATIVE_ORDER_DESK.md.")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Copilot Studio CDP Bridge")
    parser.add_argument("--post", action="store_true", help="Build and post prompt to Copilot Studio")
    parser.add_argument("--prompt", type=str, help="Post custom prompt text to Copilot Studio")
    parser.add_argument("--check", action="store_true", help="Check Copilot Studio response")
    parser.add_argument("--cycle", action="store_true", help="Run full cycle (post, wait, extract, log)")
    parser.add_argument("--wait", type=int, default=180, help="Wait time in seconds for cycle")
    args = parser.parse_args()

    if args.prompt:
        print(f"Posting custom prompt ({len(args.prompt)} chars)...")
        success = asyncio.run(post_prompt_to_copilot_studio(args.prompt))
        print("Success:", success)
    elif args.post:
        p = build_copilot_studio_prompt()
        print(f"Posting prompt ({len(p)} chars)...")
        success = asyncio.run(post_prompt_to_copilot_studio(p))
        print("Success:", success)
    elif args.check:
        done, text = asyncio.run(check_copilot_studio_response())
        print(f"Done: {done} | Length: {len(text)}")
        print(text)
        if done and text:
            append_ruling_to_order_desk(text)
    elif args.cycle:
        run_full_copilot_cycle(wait_sec=args.wait)
    else:
        ws = get_copilot_studio_ws_url()
        print("Copilot Studio WebSocket Debugger URL:", ws or "NOT FOUND")
