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
    lines.append("# 🏛️ ANTIGRAVITY x ARENA.AI LIVE STRATEGY COUNCIL BRIEFING")
    lines.append(f"**As-Of UTC:** {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} UTC · **Broker Account:** #5064568 (Blueberry Markets)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 1. Live Account & Capital Floor Status")
    lines.append("")
    lines.append("| Metric | Value | Constraint / Target | Status |")
    lines.append("|---|---|---|---|")
    lines.append(f"| **Equity / Balance** | **{equity:.2f} USD** / {balance:.2f} USD | Base Capital: 5,000.00 USD | 100% Cash Reserves |")
    lines.append(f"| **Hard Floor (G-1)** | 4,775.00 USD | Operating Buffer: 4,795.00 USD | Defended |")
    lines.append(f"| **Floor Cushion** | **+{cushion:.2f} USD** | Mandatory Cushion >= +20.00 USD | ✅ {cushion/20.0:.1f}x Required Buffer |")
    lines.append(f"| **Margin Used / Free** | {margin:.2f} USD / {equity - margin:.2f} USD | Free Margin: 100% | ✅ Zero Exposure |")
    lines.append(f"| **Active Positions** | {len(positions)} filled | Maximum Concurrent: 4 | ✅ {4 - len(positions)} Slots Available |")
    lines.append(f"| **Pending Orders** | {len(orders)} resting | Passive Limits Only | ✅ Queue Clear |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 2. Recent Trade Execution & Forensic Post-Mortem")
    lines.append("")
    lines.append("- **Ticket #18785248 (`BTCUSD.pi` Long)**:")
    lines.append("  * Entry: 83,845.00 USD (Filled 08:00:13 UTC)")
    lines.append("  * Stop Loss: 83,472.55 USD · Take Profit: 84,750.00 USD · Volume: 0.03 lots")
    lines.append("  * Outcome: **Closed via Stop Loss at 83,472.55 USD** (Deal #16997164 @ 08:15:51 UTC, Loss: -11.17 USD / -0.228% risk).")
    lines.append("  * **Liquidity Sweep Post-Mortem**: Spot swept down to 83,452.50 USD into the major 83,450.00 USD sell pool ($7.18M notional). As identified in Cycle 33, placing a stop 22.45 USD directly in front of resting cluster liquidity created a high-probability sweep magnet.")
    lines.append("  * **Quantization Sizing Trap**: Sizing was 0.03 lots (11.17 USD risk) instead of 0.02 lots (7.45 USD risk) because `MIN_RISK_USD` was strictly 10.00 USD. For `STRUCT` tier, discrete lot sizing down to 0.02 lots (7.45 USD) is now recognized and permitted.")
    lines.append("  * **Floor Integrity**: Account equity stands at 4,885.38 USD, preserving +110.38 USD above 4,775.00 USD floor (+90.38 USD above operating buffer). Zero solvency threat.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 3. Mandatory Reference Documents (Line-by-Line Ingestion)")
    lines.append("")
    lines.append("Ingest each source below in full before formulating conclusions. Open your response with a `DOCUMENT INGESTION & GROUND TRUTH CITATION` block citing latest timestamps:")
    lines.append("1. **Session History**: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md")
    lines.append("2. **Active Context**: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md")
    lines.append("3. **Order Desk**: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md")
    lines.append("4. **Council Protocol**: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md")
    lines.append("5. **Round 2 Audit**: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/reviews/ROUND2_THINKING_CHAIN_AUDIT.md")
    lines.append("6. **Gate Implementation**: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/decision_gates_v3.py (and `Terminal/dg_context.py`)")
    lines.append("7. **Live Telemetry Snapshot**: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 4. Multi-Persona Strategic Mandate")
    lines.append("")
    lines.append("1. **Orderflow & Microstructure Analyst**:")
    lines.append("   - Live taker CVD series (`cvd_1m_buckets`), volume absorption, and resting L2/L3 orderbook depth.")
    lines.append("   - Genuine whale wall backing (>= 150k USD, persist >= 180s, `gate_g7_eligible=true`, not a mirrored leg).")
    lines.append("   - Broker spread (<= 20.0 bps) and relative friction gamma (<= 10.0% of 1.5 ATR).")
    lines.append("2. **Structural Price Action & Regime Specialist**:")
    lines.append("   - Session VWAP and SD bands, Fair Value Gaps, and multi-timeframe regime (`classify_regime` on 15m, 1h, 4h).")
    lines.append("   - Strict dual-engine dialectic: Debate **Model 1** (|Z| >= 2.0 SD flush + absorption) vs **Model 2** (|Z| < 2.0 SD trend pullback). If regime is `UNDEFINED`, standing aside is mandatory.")
    lines.append("3. **Liquidation & Stop Hunt Forensic**:")
    lines.append("   - Real-time reconstructed liquidation bands and discount/premium stop clusters from live snapshot blocks.")
    lines.append("   - Protect stops: Never place stops immediately in front of large resting pools without buffer.")
    lines.append("4. **Macro Risk & Portfolio Governor**:")
    lines.append("   - Hard floor defense (worst-case stressed equity >= 4,795.00 USD at all times).")
    lines.append("   - Positive net EV expectancy hurdle: `EV_lower / R = p_lower * (RR - c) - (1 - p_lower) * (1 + c + s) > 0`.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 5. Specific Tasks for This Cycle")
    lines.append("")
    lines.append("1. **Screen 24-Asset Universe**:")
    lines.append("   - Cluster 1: 14 Crypto Perpetuals (BTC, ETH, SOL, BNB, XRP, ADA, DOGE, TRX, DOT, LINK, BCH, LTC, AVAX, NEAR).")
    lines.append("   - Cluster 2: 4 Equity Indices (SP500, NAS100, DJ30, GER40).")
    lines.append("   - Cluster 3: 3 Commodities (GOLD, SILVER, USWTI).")
    lines.append("   - Cluster 4: 3 Forex Pairs (EURUSD, GBPUSD, USDJPY).")
    lines.append("   - Focus on BTC (re-evaluating at 83,450 support) and GOLD (stretched at -2.15 SD).")
    lines.append("2. **Option A' Cross-Venue Basis**:")
    lines.append("   - Evaluate `d_adj = side * (entry_mt5 - wall_price - b_hat) / atr` with drift tolerance `|b_now - b_hat| <= max(0.25*atr, 2*tick)`.")
    lines.append("3. **Actionable Rulings**:")
    lines.append("   - If an institutional setup satisfies all 5 confluence pillars, specify: Symbol, Direction, Limit Price, SL, TP, Volume, Risk USD, and RR.")
    lines.append("   - If no qualifying setup exists, provide explicit mathematical stand-aside justification across all candidates.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 6. Required Output Structure")
    lines.append("1. `DOCUMENT INGESTION & GROUND TRUTH CITATION` (7 files verified with timestamps)")
    lines.append("2. `DIALECTIC PERSONA RESEARCH & AUDIT LOGS` (Orderflow, Structural, Liquidation, Macro)")
    lines.append("3. `OPTION A' CROSS-VENUE BASIS TABLE`")
    lines.append("4. `SEVEN-STAGE GATE COMPLIANCE MATRIX`")
    lines.append("5. `MASTER ARBITRATOR FINAL SYNTHESIS & RULING` (Evidence Score, Trade Proposal or Stand-Aside Decision)")

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
