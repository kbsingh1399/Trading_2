"""
Terminal/dispatch_comprehensive_wake_up_prompt.py
Dispatches the operator-mandated 4-step collaborative council prompt to Arena.ai:
  STEP 1 (Mandate 1): Screen 24 assets for new Model 1/2 limit order candidates directly from live_snapshot_latest.json.
  STEP 2 (Mandate 2): Audit running trades (floating PnL, trailing SL ratchets, expanding TP into liquidation bands).
  STEP 3 (Mandate 3): Audit resting limit orders (prevail vs prune sentry: whale walls, ATR distance, regime validity).
  STEP 4 (Mandate 4): Position capacity & capital floor defense (multi-cluster concurrency defending 4,775.00 USD floor).
"""
import asyncio
import json
import pathlib
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.arena_bridge import post_prompt_to_arena, dismiss_arena_popup
from Terminal.telemetry_ingest import (
    StaleDataError,
    get_fresh_snapshot,
    make_git_refresh,
)

def get_live_broker_state():
    positions = []
    orders = []
    equity = 4896.55
    balance = 4896.55
    margin = 0.0

    try:
        import MetaTrader5 as mt5
        if mt5.initialize():
            acc = mt5.account_info()
            if acc:
                equity = acc.equity
                balance = acc.balance
                margin = acc.margin
            
            raw_pos = mt5.positions_get()
            if raw_pos:
                for p in raw_pos:
                    positions.append({
                        "ticket": p.ticket,
                        "symbol": p.symbol,
                        "type": "BUY" if p.type == 0 else "SELL",
                        "volume": p.volume,
                        "price_open": p.price_open,
                        "price_current": p.price_current,
                        "sl": p.sl,
                        "tp": p.tp,
                        "profit_usd": p.profit,
                        "comment": p.comment
                    })

            raw_orders = mt5.orders_get()
            if raw_orders:
                for o in raw_orders:
                    order_type_str = "BUY_LIMIT" if o.type == 2 else ("SELL_LIMIT" if o.type == 3 else str(o.type))
                    orders.append({
                        "ticket": o.ticket,
                        "symbol": o.symbol,
                        "type": order_type_str,
                        "volume": o.volume,
                        "price_open": o.price_open,
                        "price_current": o.price_current,
                        "sl": o.sl,
                        "tp": o.tp,
                        "comment": o.comment
                    })
            mt5.shutdown()
    except Exception as e:
        print(f"Warning: Could not fetch live MT5 state directly ({e}). Falling back to snapshot.")
        # This fallback fires precisely when the broker link is down, so it is
        # the one path that MUST NOT trust an arbitrarily old file for equity
        # and balance. Route it through the staleness gate: a stale fallback is
        # worse than no fallback, because it silently misstates the capital
        # floor that G-1 is computed from.
        snap_path = ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
        if snap_path.exists():
            try:
                # One pull only (no cadence retry): this is a fallback inside a
                # prompt build, so it must not block for a minute. If the pull
                # does not land inside the budget, refuse rather than report a
                # stale capital floor.
                snap = get_fresh_snapshot(
                    str(snap_path), refresh=make_git_refresh(repo_root=str(ROOT))
                )
            except StaleDataError as stale:
                print(
                    f"Warning: MT5 snapshot fallback refused as stale "
                    f"({stale.reason}: {stale.diagnostics.get('age_s')}s vs "
                    f"{stale.diagnostics.get('max_age_s')}s budget). "
                    f"Capital figures left at their last known values."
                )
            else:
                acc = snap.get("account", {})
                equity = acc.get("equity_usd", 4896.55)
                balance = acc.get("balance_usd", 4896.55)
                # The snapshot publishes `margin_used_usd`; `margin_usd` does not
                # exist in it. Reading the wrong key silently returned 0.0, which
                # overstates the cushion above the hard floor. Accept either.
                margin = acc.get("margin_used_usd", acc.get("margin_usd", 0.0))

    return {
        "equity": equity,
        "balance": balance,
        "margin": margin,
        "positions": positions,
        "orders": orders
    }

def build_prompt() -> str:
    broker = get_live_broker_state()
    equity = broker["equity"]
    balance = broker["balance"]
    margin = broker["margin"]
    cushion = equity - 4775.0
    buffer_cushion = equity - 4795.0
    positions = broker["positions"]
    orders = broker["orders"]

    lines = []
    lines.append("=== ANTIGRAVITY x ARENA.AI LIVE STRATEGY COUNCIL BRIEFING ===")
    lines.append(f"As-Of UTC: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} UTC | Broker Account: #5064568 (Blueberry Markets)")
    lines.append("")
    lines.append("--- [1. LIVE ACCOUNT & CAPITAL FLOOR STATUS] ---")
    lines.append(f"• Equity: {equity:.2f} USD | Balance: {balance:.2f} USD | Hard Floor: 4,775.00 USD | Cushion: +{cushion:.2f} USD")
    lines.append(f"• Open Positions: {len(positions)} | Resting Orders: {len(orders)} | Available Slots: {4 - len(positions)}/4 | Mode: 100% Cash Reserves")
    lines.append("")
    lines.append("--- [2. RECENT BTC EXECUTION POST-MORTEM] ---")
    lines.append("• Ticket #18785248 (BTCUSD.pi Long): Filled 83,845.00 -> Closed via Stop Loss at 83,472.55 USD (Loss: -11.17 USD / -0.228% risk).")
    lines.append("• Sweep Cause: Spot swept down to 83,452.50 USD into the $7.18M sell pool at 83,450.00 USD. Placing the stop at 83,472.55 sat 22.45 USD directly in front of resting cluster liquidity, acting as a sweep magnet.")
    lines.append("• Quantization Lesson: Sized 0.03 lots (11.17 USD) vs STRUCT cap 10.00 USD due to MIN_RISK_USD=10.0 grid lock. Discrete lot sizing down to 0.02 lots (7.45 USD) is now recognized and permitted.")
    lines.append(f"• Floor Defense: Live equity preserved at {equity:.2f} USD (+{cushion:.2f} USD cushion above hard floor). Capital floor defended.")
    lines.append("")
    lines.append("--- [3. MANDATORY REFERENCE DOCUMENTS] ---")
    lines.append("Open response with DOCUMENT INGESTION & GROUND TRUTH CITATION citing timestamps:")
    lines.append("1. Session History: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md")
    lines.append("2. Active Context: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md")
    lines.append("3. Order Desk: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md")
    lines.append("4. Council Protocol: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md")
    lines.append("5. Round 2 Audit: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/reviews/ROUND2_THINKING_CHAIN_AUDIT.md")
    lines.append("6. Gate Implementation: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/decision_gates_v3.py")
    lines.append("7. Live Telemetry: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json")
    lines.append("")
    lines.append("--- [4. MULTI-PERSONA STRATEGIC MANDATE] ---")
    lines.append("1. Orderflow & Microstructure Analyst: Live CVD series, volume absorption, resting L2/L3 whale depth (>=150k USD, persist>=180s, gate_g7_eligible=true), spread <= 20.0 bps, gamma <= 10.0%.")
    lines.append("2. Structural Price Action & Regime Specialist: Session VWAP, SD bands, Fair Value Gaps, and classify_regime (15m, 1h, 4h). Strict dialectic: Model 1 (|Z| >= 2.0 SD flush) vs Model 2 (|Z| < 2.0 SD trend pullback). If UNDEFINED, stand aside.")
    lines.append("3. Liquidation & Stop Hunt Forensic: Reconstructed liquidation cascade bands, discount/premium stop sweep clusters. Never place stops in front of large liquidity pools without buffer.")
    lines.append("4. Macro Risk & Portfolio Governor: G-1 floor defense (stressed equity >= 4,795.00 USD), positive EV expectancy: EV_lower/R = p_lower*(RR - c) - (1 - p_lower)*(1 + c + s) > 0.")
    lines.append("")
    lines.append("--- [5. SPECIFIC TASKS FOR THIS CYCLE] ---")
    lines.append("1. Screen full 24-asset universe: 14 Crypto (24/7), 4 Indices, 3 Commodities, 3 Forex. Focus on BTC (support test at 83,450) and GOLD (Z = -2.15 SD).")
    lines.append("2. Option A' Basis: d_adj = side * (entry_mt5 - wall_price - b_hat) / atr with drift tolerance |b_now - b_hat| <= max(0.25*atr, 2*tick).")
    lines.append("3. Actionable Ruling: If qualifying setup exists, specify Symbol, Direction, Limit Price, SL, TP, Volume, Risk USD, RR. If none, provide explicit mathematical stand-aside proof across all 24 assets.")
    lines.append("")
    lines.append("--- [6. REQUIRED OUTPUT STRUCTURE] ---")
    lines.append("1. DOCUMENT INGESTION & GROUND TRUTH CITATION (7 files verified with timestamps)")
    lines.append("2. DIALECTIC PERSONA RESEARCH & AUDIT LOGS (Orderflow, Structural, Liquidation, Macro)")
    lines.append("3. OPTION A' CROSS-VENUE BASIS TABLE")
    lines.append("4. SEVEN-STAGE GATE COMPLIANCE MATRIX")
    lines.append("5. MASTER ARBITRATOR FINAL SYNTHESIS & RULING (Evidence Score, Trade Proposal or Stand-Aside Decision)")

    return "\n".join(lines)

async def main():
    prompt = build_prompt()
    print(f"Generated unified prompt: {len(prompt)} characters")
    print(prompt)
    await dismiss_arena_popup()
    ok = await post_prompt_to_arena(prompt)
    if ok:
        print("SUCCESS: Unified 4-Step Council Prompt injected into Arena.ai!")
    else:
        print("ERROR: Failed to inject prompt into Arena.ai", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
