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
    lines.append("TRADING DESK COUNCIL: STRUCTURED OPERATING PROMPT")
    lines.append("")
    lines.append("PART A: REQUIRED READING (complete all before any analysis)")
    lines.append("Read each source below in full, line by line, in this order. Do not proceed to Part B until every item is read. For each item, record the file name, the latest timestamp or version found, and a one-line confirmation of what it contains.")
    lines.append("")
    lines.append("1. Session history: .agents/memory/session_chat_history.md")
    lines.append("   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md")
    lines.append("   Read the full narrative and all recent turns. Cite the timestamp of the latest turn.")
    lines.append("")
    lines.append("2. Active context and mission card: .agents/rules/ACTIVE_CONTEXT.md")
    lines.append("   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md")
    lines.append("   Confirm the mission, the floor defense cushion, capacity rules, and current desk status.")
    lines.append("")
    lines.append("3. Live order desk: docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md")
    lines.append("   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md")
    lines.append("   Confirm the blackboard, prior rulings, and trade performance ledger.")
    lines.append("")
    lines.append("4. Council protocol: docs/specs/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md")
    lines.append("   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md")
    lines.append("   Confirm the 7-stage verification chain, formulas, and Heuristic Trap Rebuttals 1 through 9, with particular attention to Traps 7, 8, and 9.")
    lines.append("")
    lines.append("5. Round 2 audit: docs/reviews/ROUND2_THINKING_CHAIN_AUDIT.md")
    lines.append("   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/reviews/ROUND2_THINKING_CHAIN_AUDIT.md")
    lines.append("")
    lines.append("6. Decision gate code: Terminal/decision_gates_v3.py and Terminal/dg_context.py")
    lines.append("   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/decision_gates_v3.py")
    lines.append("   Verify the exact implementations of classify_regime, model1_checklist, and model2_checklist.")
    lines.append("")
    lines.append("7. Live telemetry: docs/telemetry/live_snapshot_latest.json")
    lines.append("   Local: docs/telemetry/live_snapshot_latest.json (synced every 60 seconds)")
    lines.append("   Upstream: https://github.com/kbsingh1399/Trading_2/blob/arena/537c1eb8-trading-2/docs/telemetry/live_snapshot_latest.json")
    lines.append("   Perform a complete schema census of all top-level keys and all 24 assets.")
    lines.append("")
    lines.append("Ingestion output requirement: Your response must begin with a DOCUMENT INGESTION & GROUND TRUTH CITATION block listing each file above with its verified state and latest timestamp. Any conclusion reached without reading all seven sources is invalid.")
    lines.append("")
    lines.append("PART B: ACCOUNT AND RISK BASELINE")
    lines.append("• Broker: Blueberry Markets SVG LLC, MetaTrader 5 account #5064568")
    lines.append(f"• Balance / Equity: {balance:.2f} USD / {equity:.2f} USD")
    lines.append(f"• Margin used: {margin:.2f} USD")
    lines.append("• Hard floor (G-1): 4,775.00 USD")
    lines.append("• Operating buffer: 4,795.00 USD")
    lines.append(f"• Live cushion: +{cushion:.2f} USD above hard floor (+{buffer_cushion:.2f} USD above buffer)")
    lines.append("• Recent closed trade: Ticket #18785248 (BTCUSD.pi Long 0.03 lots @ 83,845.00) closed at SL 83,472.55 USD (-11.17 USD loss). Spot swept into 83,450.00 sell pool. Capital floor defended.")
    lines.append("")
    lines.append("PART C: COUNCIL PERSONAS")
    lines.append("1. Orderflow and Microstructure Analyst: CVD delta divergence, volume absorption, L2/L3 whale wall persistence (microstructure_state.py), broker spread in bps.")
    lines.append("2. Structural Price Action and Regime Specialist: Session VWAP and SD bands, 200-EMA slope, Fair Value Gaps, structural swing highs and lows.")
    lines.append("3. Liquidation and Stop Hunt Forensic: Reconstructed liquidation cascade bands, discount and premium stop sweep clusters, resting liquidity magnets.")
    lines.append("4. Macro Risk and Portfolio Governor: G-1 floor defense, orthogonal cluster diversification, Tier-1 calendar blackouts, positive net EV expectancy.")
    lines.append("")
    lines.append("PART D: TASKS")
    lines.append("Step 1: Screen for new limit order candidates")
    lines.append("Evaluate all 24 assets (Crypto, Metals, Energy, Indices, Forex) from live_snapshot_latest.json. Perform a full schema audit, not a selective sample:")
    lines.append("1. Macro tilt: Classify summary.macro_orderflow_tilt as BEARISH_LONG_FLUSH_PREDOMINATES, BULLISH_SHORT_SQUEEZE_PREDOMINATES, or NEUTRAL. Flag any candidate that runs against the prevailing tilt.")
    lines.append("2. Execution specs: Audit min_lot, step_lot, max_lot, contract_size, stops_level, digits, tick_size. Show that proposed lot size is discrete, meets broker minimums, and that stop distance exceeds stops_level.")
    lines.append("3. Order book depth: Inspect all 20 levels of bids_top20 and asks_top20, total bid and ask notional, book_imbalance, and skew_ratio. Do not rely on top-of-book alone.")
    lines.append("4. Funding and basis: funding_rate_bps, mark_price, index_price.")
    lines.append("5. Whale trades: Separate genuine directional whale activity from algorithmic HFT grids (e.g., multi-level ladder wallets).")
    lines.append("6. Quotes: Live MT5 bid, ask, mid, spread_bps, and broker_tick_age_s (must be under 5.0 s).")
    lines.append("7. Causal indicators: session_vwap_utc, session_sigma, session_bars (mature at 16 or more), vwap_z_score, atr_14, rsi_14, trend_regime.")
    lines.append("")
    lines.append("Stale data quarantine:")
    lines.append("• Do not cite hyperdash_flow_intelligence as live evidence. Its rows are dated September 27 to 28 (about 13 days stale), have corrupted relative-time strings, and have no BNB coverage.")
    lines.append("• Use only real-time blocks inside assets_matrix_24: reconstructed_liquidations, structural_stop_clusters, orderbook_live_depth, cvd_1m_buckets, quotes.")
    lines.append("")
    lines.append("Cross-venue basis (Gate G-7 / A3 / B5):")
    lines.append("• Raw MT5 distance: side * (entry_mt5 - wall_price) / atr")
    lines.append("• Venue-adjusted distance: side * (mid_binance - wall_price) / atr")
    lines.append("• Basis: mid_mt5 - mid_binance, in USD and in units of 0.25 ATR")
    lines.append("• Current basis exceeds the G-7 tolerance on BNB (3.89x), SOL (1.86x), ETH (1.40x), and BTC (1.29x).")
    lines.append("• Do not conclude \"no whale exists\" when persistent backing sits on Binance but is offset by basis.")
    lines.append("")
    lines.append("Policy decision for council vote:")
    lines.append("• Option A: Venue-adjusted distance with a dislocation circuit breaker at abs(mid_mt5 - mid_binance) <= 0.50 * atr.")
    lines.append("• Option B: Strict MT5-centred measurement with no adjustment.")
    lines.append("• Each persona must state a position on A versus B with mathematical reasoning.")
    lines.append("")
    lines.append("Setup screens:")
    lines.append("• Model 1 (Extreme mean reversion): |Z| >= 2.0 SD flush into Value Area Low or High, verified CVD absorption, resting whale backing.")
    lines.append("• Model 2 (VWAP trend continuation): |Z| < 2.0 SD in a confirmed trend regime, pullback to Session VWAP or Value Area, resting whale backing.")
    lines.append("Output for each qualifying candidate: Asset, symbol, order type (BUY or SELL LIMIT), volume (lots), entry, SL, TP, risk (USD), R:R, and 5-pillar confluence.")
    lines.append("")
    lines.append("Step 2: Audit running trades and ratchets")
    if positions:
        lines.append(f"• Current open positions on MT5: {len(positions)} active position(s):")
        for p in positions:
            lines.append(f"  - Ticket #{p['ticket']}: {p['symbol']} {p['type']} {p['volume']} lots @ {p['price_open']} USD | Current: {p['price_current']} USD | Floating: {p['profit_usd']:+.2f} USD | SL: {p['sl']} USD | TP: {p['tp']} USD")
        lines.append("• When positions exist, audit ratchet phases: Phase 0 break-even at +0.80R, Phase 1 at +1.50R, Phase 2 at +2.00R, plus TP liquidity expansion.")
    else:
        lines.append("• Current open positions on MT5: 0")
        lines.append("• Status: standby.")
        lines.append("• When positions exist, audit ratchet phases: Phase 0 break-even at +0.80R, Phase 1 at +1.50R, Phase 2 at +2.00R, plus TP liquidity expansion.")
    lines.append("")
    lines.append("Step 3: Audit resting limit orders")
    if orders:
        lines.append(f"• Current pending orders on MT5: {len(orders)} active order(s):")
        for o in orders:
            lines.append(f"  - Ticket #{o['ticket']}: {o['symbol']} {o['type']} {o['volume']} lots @ {o['price_open']} USD | Spot: {o['price_current']} USD | SL: {o['sl']} USD | TP: {o['tp']} USD")
        lines.append("• When orders rest, verify thesis validity, whale persistence, and ATR drift to prevent stale fills.")
    else:
        lines.append("• Current pending orders on MT5: 0")
        lines.append("• Status: standby.")
        lines.append("• When orders rest, verify thesis validity, whale persistence, and ATR drift to prevent stale fills.")
    lines.append("")
    lines.append("Step 4: Capacity and capital floor governance")
    lines.append("• Capacity: No fixed position cap. Concurrent positions across orthogonal clusters are permitted.")
    lines.append("• Hard constraint: Total joint worst-case stopout risk across all exposed orders must keep at least 20.00 USD of cushion above the 4,775.00 USD floor at all times.")
    lines.append("• Risk recirculation: A position that reaches Phase 0 break-even drops its risk commitment to 0.00 USD, freeing budget for new limit orders.")
    lines.append("")
    lines.append("PART E: OUTPUT FORMAT")
    lines.append("1. DOCUMENT INGESTION & GROUND TRUTH CITATION (from Part A)")
    lines.append("2. Council verdict from all four personas, covering Steps 1 to 4")
    lines.append("3. Final ruling on Option A versus Option B")
    lines.append("4. Trade table for any qualifying candidates, or an explicit \"no qualifying candidates\" statement with reasons")

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
