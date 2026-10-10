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
        snap_path = ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
        if snap_path.exists():
            snap = json.loads(snap_path.read_text(encoding="utf-8"))
            acc = snap.get("account", {})
            equity = acc.get("equity_usd", 4896.55)
            balance = acc.get("balance_usd", 4896.55)
            margin = acc.get("margin_usd", 0.0)

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
    cushion = equity - 4775.0
    buffer_cushion = equity - 4795.0
    positions = broker["positions"]
    orders = broker["orders"]

    lines = []
    lines.append("=" * 80)
    lines.append("🏛️ INSTITUTIONAL MULTI-PERSONA QUANTITATIVE COUNCIL: UNIFIED WAKE-UP AUDIT & ORDER MANAGEMENT")
    lines.append("=" * 80)
    lines.append("")
    lines.append("TELEMETRY STREAM & MANDATORY GITHUB GROUND TRUTH LINKS:")
    lines.append("- GitHub Repository: https://github.com/kbsingh1399/Trading_2 (Branch: main, synchronized with arena/537c1eb8-trading-2)")
    lines.append("- Live Telemetry Snapshot: https://github.com/kbsingh1399/Trading_2/blob/arena/537c1eb8-trading-2/docs/telemetry/live_snapshot_latest.json")
    lines.append("- Raw Telemetry Endpoint: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json")
    lines.append("- Session Chat & Narrative History: https://github.com/kbsingh1399/Trading_2/blob/main/.agents/memory/session_chat_history.md")
    lines.append("  (Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md)")
    lines.append("- Active Context & Operating Mission Card: https://github.com/kbsingh1399/Trading_2/blob/main/.agents/rules/ACTIVE_CONTEXT.md")
    lines.append("  (Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md)")
    lines.append("- Thinking Chain Council Protocol: https://github.com/kbsingh1399/Trading_2/blob/main/docs/specs/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md")
    lines.append("  (Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md)")
    lines.append("- Round 2 Thinking Chain Audit: https://github.com/kbsingh1399/Trading_2/blob/main/docs/reviews/ROUND2_THINKING_CHAIN_AUDIT.md")
    lines.append("  (Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/reviews/ROUND2_THINKING_CHAIN_AUDIT.md)")
    lines.append("- Decision Gates v3 Specification: https://github.com/kbsingh1399/Trading_2/blob/main/Terminal/decision_gates_v3.py")
    lines.append("  (Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/decision_gates_v3.py)")
    lines.append("- Live Collaborative Order Desk: https://github.com/kbsingh1399/Trading_2/blob/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md")
    lines.append("  (Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md)")
    lines.append("- Repository Commit HEAD: main (synchronized with arena/537c1eb8-trading-2)")
    lines.append("")
    lines.append("ACCOUNT & CAPITAL RISK BENCHMARK:")
    lines.append(f"- Broker: Blueberry Markets SVG LLC (MetaTrader 5 Account #5064568)")
    lines.append(f"- Balance: {broker['balance']:.2f} USD | Equity: {equity:.2f} USD | Margin Used: {broker['margin']:.2f} USD")
    lines.append(f"- G-1 Hard Floor Defense: 4,775.00 USD hard floor | 4,795.00 USD buffer")
    lines.append(f"- Live Floor Cushion: +{cushion:.2f} USD above hard floor (+{buffer_cushion:.2f} USD above operating buffer)")
    lines.append("")
    lines.append("=" * 80)
    lines.append("COUNCIL PERSONAS CONVENED:")
    lines.append("1. Orderflow & Microstructure Analyst: Evaluates CVD delta divergence, volume absorption, L2/L3 whale wall persistence (microstructure_state.py), and broker spread in bps.")
    lines.append("2. Structural Price Action & Regime Specialist: Evaluates Session VWAP & SD bands, 200-EMA slope, Fair Value Gaps, and structural swing highs/lows.")
    lines.append("3. Liquidation & Stop Hunt Forensic: Analyzes reconstructed liquidation cascade bands, discount/premium stop sweep clusters, and resting liquidity magnets.")
    lines.append("4. Macro Risk & Portfolio Governor: Enforces G-1 floor defense, orthogonal cluster diversification, Tier-1 calendar blackouts, and positive Net EV expectancy.")
    lines.append("=" * 80)
    lines.append("")
    lines.append("STEP 1 (MANDATE 1): SCREEN FOR NEW POTENTIAL CANDIDATES FOR LIMIT ORDERS")
    lines.append("Inspect and evaluate all 24 assets across Crypto, Metals, Energy, Indices, and Forex directly from `docs/telemetry/live_snapshot_latest.json`:")
    lines.append("  * Real Telemetry on Disk: docs/telemetry/live_snapshot_latest.json (synced every 60s via git daemon)")
    lines.append("  * GitHub Upstream: https://github.com/kbsingh1399/Trading_2/blob/arena/537c1eb8-trading-2/docs/telemetry/live_snapshot_latest.json")
    lines.append("Screen for:")
    lines.append("  * Model 1 (Extreme Mean Reversion): |Z| >= 2.0 SD flushes into Value Area Low / High with verified CVD absorption and resting whale backing.")
    lines.append("  * Model 2 (VWAP Trend-Continuation Pullbacks): |Z| < 2.0 SD in confirmed trend regimes pulling back to Session VWAP / Value Area with resting whale backing.")
    lines.append("For any qualifying candidate, deliver exact limit order parameters: Asset, Symbol, Order Type (BUY/SELL LIMIT), Volume (Lots), Entry, SL, TP, Risk (USD), R:R, and 5-Pillar Confluence.")
    lines.append("")
    lines.append("=" * 80)
    lines.append("STEP 2 (MANDATE 2): AUDIT RUNNING TRADES & RATCHET MANAGEMENT")
    if positions:
        lines.append(f"We have {len(positions)} ACTIVE OPEN POSITION(S) floating on MT5:")
        for p in positions:
            lines.append(f"  * Ticket #{p['ticket']}: {p['symbol']} {p['type']} {p['volume']} lots @ {p['price_open']} USD | Current: {p['price_current']} USD | Floating PnL: {p['profit_usd']:+.2f} USD | SL: {p['sl']} USD | TP: {p['tp']} USD | Comment: {p['comment']}")
        lines.append("AUDIT QUESTIONS FOR ARENA COUNCIL:")
        lines.append("  1. Are the market metrics, CVD orderflow, and price action progressing in our favor?")
        lines.append("  2. Should SL be trailed to Phase 0 Break-Even (+0.80R gain) to lock in profit and liberate committed risk to 0.00 USD?")
        lines.append("  3. Should SL be trailed to Phase 1 Profit Lock (+1.50R) or Phase 2 Trailing Lock (+2.00R)?")
        lines.append("  4. Can Take Profit be expanded into newly formed liquidation cascade pools, stop clusters, or orderbook liquidity vacuums?")
    else:
        lines.append("- Active Market Positions Count on MT5: 0 (No active positions currently floating).")
        lines.append("- Operating Protocol: Invariant standby. When open positions exist, council actively audits trailing ratchets (Phase 0 BE @ +0.80R, Phase 1 @ +1.50R, Phase 2 @ +2.00R) and TP liquidity expansions.")
    lines.append("")
    lines.append("=" * 80)
    lines.append("STEP 3 (MANDATE 3): AUDIT RESTING LIMIT ORDERS (ORDER PERSISTENCE & PRUNING SENTRY)")
    if orders:
        lines.append(f"We have {len(orders)} ACTIVE PENDING LIMIT ORDER(S) resting on MT5:")
        for o in orders:
            lines.append(f"  * Ticket #{o['ticket']}: {o['symbol']} {o['type']} {o['volume']} lots @ {o['price_open']} USD | Spot: {o['price_current']} USD | SL: {o['sl']} USD | TP: {o['tp']} USD | Comment: {o['comment']}")
        lines.append("AUDIT QUESTIONS FOR ARENA COUNCIL:")
        lines.append("  1. Does the structural thesis for each resting order STILL PREVAIL so we should keep it resting and wait for fill?")
        lines.append("  2. Is the supporting resting L2/L3 whale wall backing intact with verified persistence?")
        lines.append("  3. Has spot price drifted beyond 2.0x ATR or has adverse regime change degraded the thesis, warranting PRUNING/CANCELLATION?")
        lines.append("  4. Can Take Profit be adjusted into fresh overhead liquidity vacuums?")
    else:
        lines.append("- Active Pending Limit Orders on MT5: 0 (Book is flat; resting orders previously pruned or filled).")
        lines.append("- Operating Protocol: Invariant standby. When pending orders are resting, council verifies thesis validity, whale persistence, and ATR drift to prevent stale order fills.")
    lines.append("")
    lines.append("=" * 80)
    lines.append("STEP 4 (MANDATE 4): POSITION CAPACITY & CAPITAL FLOOR DEFENSE GOVERNANCE")
    lines.append("- Dynamic Capacity Policy: NO ARTIFICIAL RIGID POSITION CAP.")
    lines.append(f"- Capital Hard Floor: 4,775.00 USD | Operating Buffer: 4,795.00 USD | Live Cushion: +{cushion:.2f} USD.")
    lines.append("- Concurrency Rule: Multiple concurrent positions across orthogonal asset clusters (Crypto, Metals, Energy, Indices, Forex) are actively permitted.")
    lines.append("- Mandatory Constraint: Total joint worst-case stopout risk across all exposed orders and positions must unconditionally preserve >= 20.00 USD cushion above the 4,775.00 USD hard floor at all times.")
    lines.append("- Risk Recirculation: Any position reaching Phase 0 Break-Even reduces its risk commitment to 0.00 USD, immediately freeing capital and risk budget to stage additional limit orders.")
    lines.append("=" * 80)
    lines.append("")
    lines.append("Deliver your unified, exhaustive multi-persona verdict addressing all 4 Steps.")
    lines.append("=" * 80)

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
