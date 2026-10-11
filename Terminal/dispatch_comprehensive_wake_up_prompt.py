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
    lines.append("\t1. Session history: .agents/memory/session_chat_history.md")
    lines.append("\t   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md")
    lines.append("\t   Read the full narrative, past rulings, operator feedback, and position trajectory. Cite the timestamp of the newest `### Turn [...]` header.")
    lines.append("\t2. Active context and mission card: .agents/rules/ACTIVE_CONTEXT.md")
    lines.append("\t   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md")
    lines.append("\t   Confirm the mission, the G-1 floor defense cushion, capacity rules, and current desk status.")
    lines.append("\t3. Live order desk: docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md")
    lines.append("\t   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md")
    lines.append("\t   Confirm the blackboard, prior rulings, and trade performance ledger.")
    lines.append("\t4. Council protocol: docs/specs/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md")
    lines.append("\t   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md")
    lines.append("\t   Confirm the 7-stage verification chain, formulas, and Heuristic Trap Rebuttals 1 through 9 (esp. Traps 7, 8, and 9).")
    lines.append("\t5. Round 2 audit: docs/reviews/ROUND2_THINKING_CHAIN_AUDIT.md")
    lines.append("\t   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/reviews/ROUND2_THINKING_CHAIN_AUDIT.md")
    lines.append("\t6. Decision gate code: Terminal/decision_gates_v3.py and Terminal/dg_context.py")
    lines.append("\t   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/decision_gates_v3.py")
    lines.append("\t   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/dg_context.py")
    lines.append("\t   Verify the exact implementations of classify_regime, model1_checklist, model2_checklist, and Option A' cross-venue basis translation.")
    lines.append("\t7. Live telemetry: docs/telemetry/live_snapshot_latest.json")
    lines.append("\t   Local: docs/telemetry/live_snapshot_latest.json (auto-synced every 60 seconds)")
    lines.append("\t   Upstream: https://github.com/kbsingh1399/Trading_2/blob/arena/537c1eb8-trading-2/docs/telemetry/live_snapshot_latest.json")
    lines.append("\t   Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json")
    lines.append("\t   Perform a complete schema census of all top-level keys and the entire 24-asset matrix.")
    lines.append("")
    lines.append("Ingestion output requirement: Your response must begin with a DOCUMENT INGESTION & GROUND TRUTH CITATION block listing each file above with its verified state and latest timestamp. Any conclusion reached without reading all seven sources is invalid.")
    lines.append("")
    lines.append("PART B: ACCOUNT AND RISK BASELINE")
    lines.append("\t• Broker: Blueberry Markets SVG LLC, MetaTrader 5 account #5064568")
    lines.append(f"\t• Balance / Equity: Read live values from account block in live_snapshot_latest.json (Baseline: {balance:.2f} USD / {equity:.2f} USD)")
    lines.append(f"\t• Margin used: {margin:.2f} USD (100% Cash)")
    lines.append("\t• Hard floor (G-1): 4,775.00 USD")
    lines.append("\t• Operating buffer: 4,795.00 USD")
    lines.append(f"\t• Live cushion: Must be >= +20.00 USD above 4,775.00 USD hard floor at all times (Baseline: +{cushion:.2f} USD above floor, +{buffer_cushion:.2f} USD above buffer)")
    lines.append("\t• Joint Stopout Stress Rule: Stressed equity across all open and pending tickets combined must unconditionally preserve >= 4,795.00 USD.")
    lines.append("")
    lines.append("PART C: COUNCIL PERSONAS (REASONING MANDATE AT EVERY LEVEL)")
    lines.append("Each persona must present detailed mathematical reasoning, empirical calculations, and clear justification:")
    lines.append("\t1. Orderflow and Microstructure Analyst: CVD delta divergence, volume absorption, L2/L3 whale wall persistence (>= 150k USD, >= 180s persistence, gate_g7_eligible=true), broker spread in bps (<= 20.00 bps), and relative friction (<= 10.0% of 1.5 ATR).")
    lines.append("\t2. Structural Price Action and Regime Specialist: Session VWAP and SD bands, 200-EMA slope, Fair Value Gaps, structural swing highs/lows, and multi-timeframe regime classification (classify_regime on 15m, 1h, 4h).")
    lines.append("\t3. Liquidation and Stop Hunt Forensic: Reconstructed liquidation cascade bands, discount and premium stop sweep clusters, and resting liquidity magnets. Anchor TP to real pools, never into thin air.")
    lines.append("\t4. Macro Risk and Portfolio Governor: G-1 floor defense, orthogonal cluster diversification, Tier-1 calendar blackouts, and positive net EV expectancy hurdle: EV_lower / R = p_lower * (RR - c) - (1 - p_lower) * (1 + c + s) > 0.")
    lines.append("")
    lines.append("PART D: TASKS")
    lines.append("Step 1: Screen for new limit order candidates")
    lines.append("Evaluate the full 24-asset universe from live_snapshot_latest.json (assets_matrix_24). Perform a full schema audit with mathematical reasoning, not a selective sample:")
    lines.append("\t• Asset Matrix Breakdown (24 Total Assets):")
    lines.append("\t  - Cluster 1: 14 Crypto Perpetuals (BTC, ETH, SOL, BNB, XRP, ADA, DOGE, TRX, DOT, LINK, BCH, LTC, AVAX, NEAR) -> 24/7 continuous trading. Active on every cycle.")
    lines.append("\t  - Cluster 2: 4 Equity Indices (SP500, NAS100, DJ30, GER40) -> Broker market hours only (Closed weekends).")
    lines.append("\t  - Cluster 3: 3 Commodities (GOLD, SILVER, USWTI) -> Broker market hours only (Closed weekends).")
    lines.append("\t  - Cluster 4: 3 Forex Pairs (EURUSD, GBPUSD, USDJPY) -> Broker market hours only (Closed weekends).")
    lines.append("\t  * Operating Rule: On weekends, confirm closed broker status for the 10 CFD assets; screen the 14 Crypto Perpetuals actively. On weekdays, screen all 24 assets.")
    lines.append("")
    lines.append("\t1. Directional Orderflow Tilt: Classify live tilt from real-time volume, CVD series (cvd_1m_buckets), and book imbalance. (Note: hyperdash_flow_intelligence.summary.macro_orderflow_tilt is an unanchored historical scrape aggregate; do not confuse it with live market tilt). Flag any candidate running against prevailing orderflow tilt.")
    lines.append("\t2. Execution Specs: Audit min_lot, step_lot, max_lot, contract_size, stops_level, digits, tick_size. Prove that proposed lot size is discrete, meets broker minimums, and that stop distance exceeds broker stops_level.")
    lines.append("\t3. Order Book Depth: Inspect all 20 levels of bids_top20 and asks_top20, total bid and ask notional, book_imbalance, and skew_ratio. Never rely on top-of-book alone.")
    lines.append("\t4. Funding and Basis: Check funding_rate_bps, mark_price, index_price.")
    lines.append("\t5. Whale Trades: Separate genuine directional whale activity from algorithmic HFT grids (e.g. multi-level ladder wallets).")
    lines.append("\t6. Quotes: Live MT5 bid, ask, mid, spread_bps (<= 20.00 bps), and broker_tick_age_s (must be under 5.0 s).")
    lines.append("\t7. Causal Indicators: session_vwap_utc, session_sigma (>= 0.8 * ATR floor), session_bars (mature at 16 or more), vwap_z_score, atr_14, rsi_14, trend_regime.")
    lines.append("")
    lines.append("Stale data quarantine:")
    lines.append("\t• Do not cite hyperdash_flow_intelligence as live evidence. Its rows are dated September 27 to 28 (about 13 days stale), have corrupted relative-time strings, and have zero BNB coverage.")
    lines.append("\t• Use only real-time blocks inside assets_matrix_24: reconstructed_liquidations, structural_stop_clusters, orderbook_live_depth, cvd_1m_buckets, quotes.")
    lines.append("")
    lines.append("Cross-venue basis & Option A' (Gate G-7 / A3 / B5):")
    lines.append("\t• Ground truth: MT5 entry fills at broker quote, while whale walls sit on Binance/Hyperliquid. Raw MT5 distance side * (entry_mt5 - wall_price) / atr mixes venue scales.")
    lines.append("\t• Option A' Formulation (Ratified Architecture in Terminal/dg_context.py):")
    lines.append("\t  - Effective Wall Price: w_effective = wall_price + b_hat, where b_hat is recent median basis (mid_mt5 - mid_binance).")
    lines.append("\t  - Venue-Adjusted Distance: d_adj = side * (entry_mt5 - w_effective) / atr = side * (entry_mt5 - wall_price - b_hat) / atr.")
    lines.append("\t  - Drift Circuit Breaker: |b_now - b_hat| <= max(0.25 * atr, 2.0 * tick_size).")
    lines.append("\t  - Tick Quantization Guard: max(0.25 * atr, 2.0 * tick_size) prevents spurious false rejection on micro-ATR assets (e.g. TRX).")
    lines.append("\t  - Evaluation Rule: If basis is stable (|b_now - b_hat| <= drift_tol), admit wall if 0 <= d_adj <= 0.25 ATR. If basis dislocates, circuit breaker trips and suppresses wall.")
    lines.append("\t  - Never conclude \"no whale exists\" when persistent backing sits on Binance/Hyperliquid but is offset by basis; distinguish venue basis skew from absent whale depth.")
    lines.append("")
    lines.append("Setup screens:")
    lines.append("\t• Model 1 (Extreme mean reversion): |Z| >= 2.0 SD flush into Value Area Low or High, verified CVD absorption, resting whale backing within 0.25 ATR under Option A'.")
    lines.append("\t• Model 2 (VWAP trend continuation): |Z| < 2.0 SD in a confirmed trend regime (TREND_UP/TREND_DOWN), pullback to Session VWAP or Value Area shelf, resting whale backing within 0.25 ATR under Option A'.")
    lines.append("\t• Mandatory Dual-Engine Dialectic: Reason through BOTH models for each candidate. If regime is UNDEFINED or neither setup passes all gates, standing aside is the mandatory disciplined action.")
    lines.append("\t• Output for each qualifying candidate: Asset, symbol, order type (BUY or SELL LIMIT), volume (lots), entry, SL, TP, risk (USD), R:R, and 5-pillar confluence.")
    lines.append("")
    lines.append("Step 2: Audit running trades and ratchets")
    if positions:
        lines.append(f"\t• Current open positions on MT5: {len(positions)} active position(s):")
        for p in positions:
            lines.append(f"\t  - Ticket #{p['ticket']}: {p['symbol']} {p['type']} {p['volume']} lots @ {p['price_open']} USD | Current: {p['price_current']} USD | Floating: {p['profit_usd']:+.2f} USD | SL: {p['sl']} USD | TP: {p['tp']} USD")
        lines.append("\t• Audit ratchet phases with reasoning: Phase 0 break-even at +0.80R, Phase 1 Profit Lock at +1.50R, Phase 2 at +2.00R, plus TP liquidity expansion.")
    else:
        lines.append("\t• Current open positions on MT5: 0 (or read live from active_positions).")
        lines.append("\t• Status: STANDBY when 0 positions.")
        lines.append("\t• When positions exist, audit ratchet phases with reasoning: Phase 0 break-even at +0.80R, Phase 1 Profit Lock at +1.50R, Phase 2 at +2.00R, plus TP liquidity expansion.")
    lines.append("")
    lines.append("Step 3: Audit resting limit orders")
    if orders:
        lines.append(f"\t• Current pending orders on MT5: {len(orders)} active order(s):")
        for o in orders:
            lines.append(f"\t  - Ticket #{o['ticket']}: {o['symbol']} {o['type']} {o['volume']} lots @ {o['price_open']} USD | Spot: {o['price_current']} USD | SL: {o['sl']} USD | TP: {o['tp']} USD")
        lines.append("\t• Audit order persistence with reasoning: verify thesis validity, whale persistence, and ATR drift (< 2.0x ATR). If whale wall thinned > 50% or thesis degraded, immediately recommend DELETE/PRUNE.")
    else:
        lines.append("\t• Current pending orders on MT5: 0 (or read live from pending_orders).")
        lines.append("\t• Status: STANDBY when 0 pending orders.")
        lines.append("\t• When orders rest, verify thesis validity, whale persistence, and ATR drift (< 2.0x ATR). If whale wall thinned > 50% or thesis degraded, immediately recommend DELETE/PRUNE.")
    lines.append("")
    lines.append("Step 4: Capacity and capital floor governance")
    lines.append("\t• Capacity: Maximum 4 concurrent tickets across filled positions and pending orders combined.")
    lines.append("\t• Hard constraint: Total joint worst-case stopout risk across all exposed orders must keep at least 20.00 USD of cushion above the 4,775.00 USD floor at all times (stressed equity >= 4,795.00 USD).")
    lines.append("\t• Risk recirculation: A position that reaches Phase 0 break-even drops its risk commitment to 0.00 USD, freeing budget for new limit orders.")
    lines.append("")
    lines.append("PART E: OUTPUT FORMAT")
    lines.append("\t1. DOCUMENT INGESTION & GROUND TRUTH CITATION (listing all 7 files from Part A with verified state and timestamp)")
    lines.append("\t2. Council deliberation from all four personas with explicit mathematical reasoning at every level (covering Steps 1 to 4)")
    lines.append("\t3. Option A' cross-venue basis evaluation table (reporting raw MT5 distance, venue-adjusted distance, live basis, and drift stability)")
    lines.append("\t4. Trade table for qualifying candidates (or explicit mathematical stand-aside justification across all 24 assets)")

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
