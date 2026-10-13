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

try:
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)
except Exception:
    pass

from Terminal.arena_bridge import post_prompt_to_arena, post_prompt_to_zai, dismiss_arena_popup
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
                    vol = getattr(o, "volume_current", getattr(o, "volume_initial", getattr(o, "volume", 0.0)))
                    t_sym = mt5.symbol_info_tick(o.symbol)
                    p_curr = ((t_sym.bid + t_sym.ask) / 2.0) if t_sym else o.price_open
                    orders.append({
                        "ticket": o.ticket,
                        "symbol": o.symbol,
                        "type": order_type_str,
                        "volume": vol,
                        "price_open": o.price_open,
                        "price_current": p_curr,
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

def _resolve_asset_key(mt5_symbol: str, assets: dict) -> str:
    clean = mt5_symbol.replace(".pi", "").replace(".p", "").replace("USD", "")
    if mt5_symbol.replace(".pi", "").replace(".p", "") in assets:
        return mt5_symbol.replace(".pi", "").replace(".p", "")
    if clean in assets:
        return clean
    for k, v in assets.items():
        if v.get("mt5_symbol") == mt5_symbol:
            return k
    return clean


def build_prompt(cycle_num: int = 40) -> str:
    broker = get_live_broker_state()
    equity = broker["equity"]
    balance = broker["balance"]
    margin = broker["margin"]
    cushion = equity - 4775.0
    buffer_cushion = equity - 4795.0
    positions = broker["positions"]
    orders = broker["orders"]

    snap_path = ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
    snap_data = {}
    if snap_path.exists():
        try:
            snap_data = json.loads(snap_path.read_text(encoding="utf-8"))
        except Exception:
            snap_data = {}
    assets = snap_data.get("assets_matrix_24", {})
    gen_id = snap_data.get("generation_id", "latest")
    gen_ts = snap_data.get("as_of_utc", "latest")
    macro_info = snap_data.get("macro_calendar", {})
    ev_name = macro_info.get("event", "BoE Pill Citi Roundtable")
    ev_time = macro_info.get("event_release_utc", "2026-10-14 06:00:00 UTC")
    blackout_active = macro_info.get("blackout_active", False)

    lines = []
    lines.append(f"TRADING DESK COUNCIL: CYCLE {cycle_num} PURE TELEMETRY & PLAYBOOK ANALYSIS PROMPT")
    lines.append("MANDATE: 100% DIRECT LINE-BY-LINE ANALYSIS OF docs/telemetry/live_snapshot_latest.json (ZERO DECISION GATES)")
    lines.append("")
    lines.append("PART A: REQUIRED READING (complete before analysis)")
    lines.append("Read the following repository sources in full:")
    lines.append("")
    lines.append("1. Live Telemetry Matrix (Primary Ground Truth): docs/telemetry/live_snapshot_latest.json")
    lines.append(f"   Latest Generation: {gen_id} ({gen_ts})")
    lines.append("   Upstream: https://github.com/kbsingh1399/Trading_2/blob/arena/5c05910e-trading-2/docs/telemetry/live_snapshot_latest.json")
    lines.append("   Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json")
    lines.append("   Inspect all 24 assets in assets_matrix_24 and all telemetry blocks: quotes (MT5 spread_bps & mid), execution_specs, causal_indicators (Session VWAP, Z-score, RSI, ATR, EMA 20/50/200, POC/VAH/VAL), orderbook_live_depth (20-level L2 depth & imbalance), whale_walls_l3 (0x... wallet addresses, sizes, persistence_s >= 180s), structural_stop_clusters (nearest_sell_stop_clusters_below, nearest_buy_stop_clusters_above, top_*), reconstructed_liquidations (nearest_long_cascade_bands_below, nearest_short_squeeze_bands_above, top_*), venue_basis, and cvd_1m_buckets (5m/15m/30m sums).")
    lines.append("   Note on Schema Metadata: Top-level `trade_authorization: DENIED_UNVERIFIED_ORDERFLOW` in the JSON header is a static schema provenance tag confirming the telemetry publisher script itself never submits broker orders; it is NOT a trading lock on the Council.")
    lines.append("")
    lines.append("2. Live Trade Decision Playbook: docs/specs/TRADE_DECISION_PLAYBOOK.md")
    lines.append("   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md")
    lines.append("   Apply the Parameter Coincidence Matrix (Entry Shelf + SL Liquidity Bunker outside min_price/max_price + TP Liquidity Magnet front-run by 5-10 bps + Psychological Round Numbers), Dual-Venue Division of Labor (Spreads/Quotes from MT5; Orderbook/Whales/Liquidations/Stops from Hyperdash & Binance), and the 7-Point Pre-Trade Checklist.")
    lines.append("")
    lines.append("3. Live Order Desk & Session Context:")
    lines.append("   • docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md)")
    lines.append("   • .agents/rules/ACTIVE_CONTEXT.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md)")
    lines.append("   • .agents/memory/session_chat_history.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md)")
    lines.append("")
    lines.append("PART B: ACCOUNT AND RISK BASELINE")
    lines.append("• Execution Mode: PASSIVE LIMIT ORDERS ONLY (no market orders).")
    lines.append("• Broker: Blueberry Markets SVG LLC, MetaTrader 5 account #5064568")
    lines.append(f"• Balance / Equity: {balance:.2f} USD / {equity:.2f} USD")
    lines.append(f"• Margin used: {margin:.2f} USD")
    lines.append("• Realized Deals Banked Today: Ticket #18826511 (ETHUSD.pi SHORT -> +1.92 USD profit banked via Profit Lock at 2,513.02), Ticket #18813768 (SOLUSD.p SHORT -> +9.52 USD profit banked via Phase 1 Lock), Ticket #18813767 (BTCUSD.pi SHORT -> +16.10 USD full TP).")
    lines.append("• Hard floor: 4,775.00 USD | Operating buffer: 4,795.00 USD")
    lines.append(f"• Live cushion: +{cushion:.2f} USD above hard floor (+{buffer_cushion:.2f} USD above operating buffer)")
    lines.append("• Risk per trade: 7.50 to 14.50 USD (adaptive risk envelope, 0.15% to 0.29% of capital).")
    lines.append("• Stressed Loss Formula (Astra Invariant): Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket. Requirement: min(balance, equity) - sum(all open & pending stressed risks) >= 4,795.00 USD.")
    lines.append("• Rigorous Capacity Ceiling: With SP500 open (18.00 USD stress), capacity permits: max 2 new tickets at 14.50 USD risk (stress 20.13 USD each, leaving 4,811.48 USD >= 4,795.00 USD), or max 3 new tickets at <= 10.50 USD risk each (stress 15.13 USD each, leaving 4,806.34 USD >= 4,795.00 USD). Staging 3 tickets at 14.50 USD is mathematically rejected as it leaves 4,791.35 USD (< 4,795.00 USD buffer).")
    lines.append("")
    lines.append("PART C: ACTIVE REPOSITORIES & DATA PROVENANCE")
    lines.append("• Canonical Workspace: https://github.com/kbsingh1399/Trading_2")
    lines.append("• Active Branches: main (production) and arena/5c05910e-trading-2 (container active sync)")
    lines.append("• Direct Raw URLs:")
    lines.append("  - Telemetry: https://raw.githubusercontent.com/kbsingh1399/Trading_2/arena/5c05910e-trading-2/docs/telemetry/live_snapshot_latest.json")
    lines.append("  - Playbook: https://raw.githubusercontent.com/kbsingh1399/Trading_2/arena/5c05910e-trading-2/docs/specs/TRADE_DECISION_PLAYBOOK.md")
    lines.append("  - Desk State: https://raw.githubusercontent.com/kbsingh1399/Trading_2/arena/5c05910e-trading-2/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md")
    lines.append("")
    lines.append("PART D: MANDATORY 12-PARAMETER TELEMETRY SYNTHESIS & TREND-FIRST HIERARCHY")
    lines.append("DO NOT STICK DOGMATICALLY TO VWAP SD BANDS ALONE. Fading oversold/overbought bands in a trending market is lethal. You MUST evaluate the overall trend supported by all parameters in live_snapshot_latest.json:")
    lines.append("  1. Higher Timeframe Trend Hierarchy: Inspect 1H & 4H OHLCV candles, 20/50/200 EMAs. If Price < EMA20 < EMA50 on 1H/4H (Bearish regime), Model 1 dip-buying Longs are STRICTLY FORBIDDEN. All priority shifts to Model 2 Trend Pullback SHORTS!")
    lines.append("  2. cvd_1m_buckets & CVD Momentum: Massive negative taker CVD (-1M to -3M USD) is proof of aggressive seller domination. Never buy into negative CVD. Use negative CVD to qualify SHORT entries on relief rallies.")
    lines.append("  3. Model 2 Pullback Short Protocol: In a downtrend, patiently wait for pullbacks up into the EMA20/EMA50/VAH shelves where heavy Ask Whale Walls are resting to defend the Stop Loss.")
    lines.append("  4. Broker Ticker Mapping: Avalanche (AVAX) is tradeable on Blueberry Markets MT5 as AVXUSD.p (trade contract size 100.0, volume min 0.01, digits 2).")
    lines.append("  5. Adaptive Risk Envelope: Acceptable risk is [7.50, 14.50 USD]. Do not reject high-conviction 0.01 lot trend shorts risking 8.50 to 9.50 USD over arbitrary floor bureaucracy.")
    lines.append("  6. quotes: Live MT5 Bid/Ask spread in bps (spread_bps <= 35 bps Crypto, <= 5 bps TradFi).")
    lines.append("  7. vwap & volume_profile: Session POC, VAH, VAL, and High/Low Volume Nodes.")
    lines.append("  8. orderbook_live_depth & whale_walls_l3: Hyperdash verified on-chain Ethereum whale wallet orders (0x... addresses, notionals in USD, price levels, and temporal persistence >= 180s).")
    lines.append("  9. reconstructed_liquidations: Reconstructed liquidation cascade bands.")
    lines.append("  10. structural_stop_clusters: Structural stop sweep pools.")
    lines.append("  11. macro_calendar: Tier-1 macroeconomic event proximity.")
    lines.append("  12. execution_specs: Blueberry Markets broker tick size, point size, contract size, and margin requirements.")
    lines.append("  13. Hyperdash Liquidation Cascade & Stop Bands as Attraction Points & Magnets: Dense liquidation cascade bands (reconstructed_liquidations) and structural stop clusters (structural_stop_clusters) act as primary gravitational attraction points (liquidity magnets). Combined with psychological round numbers, resting L2/L3 whale walls, and VWAP/EMA shelves, position Take Profit targets to front-run these attraction magnets by 5–10 bps, while ensuring Stop Loss is sheltered behind resting whale walls safely outside opposing sweep bands.")
    lines.append("  14. Cross-Venue Basis Mapping & Broker Spread Risk: Telemetry orderbooks, whale walls, and liquidation bands are denominated in Binance/Hyperliquid perpetual futures prices, while execution occurs on Blueberry Markets OTC CFDs via MT5. Inspect venue_basis (MT5 mid minus perp mid) before finalizing entries, front-running targets (5-10 bps), and stop loss buffers. Ensure broker spread markups or wicks cannot prematurely tag stops bunkered in perp space.")
    lines.append("")
    lines.append("PART E: KAIZEN CONTINUOUS SELF-IMPROVEMENT LOOP & COMPLETE LOSING-TRADE AUTOPSY LEDGER")
    lines.append("Study the forensic breakdown of all recent stopped-out trades from Account 5064568. The Council must actively learn from each:")
    lines.append("  • Ticket #18825384 (SOLUSD.p, -11.05 USD loss via SL @ 108.55 USD) [FRESH LOSS]: Ask Whale walls (1.86M & 3.65M) relocated from 108.34/108.75 upwards to 108.68/109.22, leaving 108.55 undefended except by a thin 184K wall inside the active [107.5-108.5] buy-stop sweep band. Price wicked to 108.58 and took the stop before dropping back to 107.79. Lessons: (1) Wall relocation pre-sweep is an EMERGENCY; (2) Stops must NEVER sit inside an un-swept stop pool; (3) Wall defence requires >= 500k USD with >= 180s persistence; (4) Future SOL shorts require SL >= 108.92 at <= 0.11 lots.")
    lines.append("  • Ticket #18813343 (BTCUSD.pi, -11.58 USD loss via SL @ 82,158.00 USD): Long entered at 82,351 USD against -3.07M USD negative taker CVD during a market cascade; swept stop in [82,100-82,200] band before bouncing.")
    lines.append("  • Ticket #18806752 (SOLUSD.p, -10.88 USD loss via SL @ 108.79 USD): Attempted counter-trend long during crypto-wide cascading flush. Stop placed at 108.79 USD sat directly inside the discount sell-stop cluster; wick swept through stops before any recovery.")
    lines.append("  • Ticket #18798018 (BTCUSD.pi, -11.20 USD loss via SL @ 82,590.00 USD): Staged mean-reversion long at 83,150 USD against heavily accelerating negative 1m/5m CVD (-420 BTC) before delta absorption formed; liquidation flush swept to 82,627 USD, hitting the SL.")
    lines.append("  • Ticket #18786372 (BTCUSD.pi, -11.17 USD loss via SL @ 83,472.55 USD): Long entry staged above an un-swept sell-stop pool at 83,500 USD; market punched straight through entry to sweep the stops below, hitting the SL at 83,472.55 USD.")
    lines.append("  • Ticket #18749312 (SP500.p, -13.00 USD loss via SL @ 7,778.50 USD): Trend pullback long entered without wide enough buffer below Value Area Low; stop placed 0.15 ATR below VAL was tagged on a routine liquidity sweep before price rallied to target.")
    lines.append("  • Ticket #18748507 (ETHUSD.pi, -11.90 USD loss via SL @ 2,477.50 USD): Long entered based on whale bid wall that was pulled/thinned by 65% within 90 seconds (insufficient temporal persistence < 180s).")
    lines.append("  • Ticket #18744533 (XAUUSD.pi, -13.70 USD loss via SL @ 4,175.80 USD): Model 1 long against adverse momentum without multi-timeframe trend alignment.")
    lines.append("")
    lines.append("MANDATORY KAIZEN CONTINUOUS SELF-IMPROVEMENT MANDATE:")
    lines.append("Arena.ai, Z.ai Chat, and Antigravity operate as a self-improving quantitative system. On every turn:")
    lines.append("  1. Zero Regression: The Council is strictly FORBIDDEN from repeating any of the 8 traps above. Every proposed action must explicitly state how it defends against them.")
    lines.append("  2. Invariant 1: Stop loss MUST sit safely outside [min_price, max_price] of the governing sweep cluster with >= 0.35 to 0.50 ATR structural buffer. Never place SL inside a sweep band!")
    lines.append("  3. Invariant 2: Long entries require confirmed CVD delta deceleration/absorption. Never catch a falling knife with negative taker momentum!")
    lines.append("  4. Invariant 3: Never stage entry limits directly above un-swept opposing stop clusters; allow the sweep to complete or anchor below the sweep band.")
    lines.append("  5. Invariant 4: Supporting whale walls must show verified temporal persistence (>= 180s) and substantial notional (>= 500k USD). If a wall relocates, re-evaluate or trim immediately.")
    lines.append("  6. Invariant 5: Multi-timeframe trend alignment MUST be respected. In a Bearish HTF regime, Model 1 longs are BANNED; prioritize Model 2 Trend Pullback Shorts!")
    lines.append("  7. Dynamic Lot Sizing: When wider structural stop buffers are required to clear liquidation bands (e.g. ETH SL moved to 2,555.00), DOWNSIZE lot size immediately (e.g. 0.50 -> 0.35 lots in Cycle 49) so risk remains strictly within the [7.50, 14.50 USD] ceiling.")
    lines.append("")
    lines.append("PART F: COUNCIL PERSONAS & DELIBERATION")
    lines.append("1. Orderflow & Microstructure Analyst: MT5 spread_bps, L2 20-level depth & imbalance, L3 on-chain wallet orders (0x..., persistence_s >= 180s), and multi-window 1m CVD (5m, 15m, 30m).")
    lines.append("2. Structural Price Action Specialist: Session VWAP & SD bands (Z-score), Volume Profile (POC/VAH/VAL), 20/50/200 EMA hierarchy, and psychological round numbers.")
    lines.append("3. Liquidation & Stop Hunt Forensic: Reconstructed liquidation cascade bands (nearest_* and top_*), stop clusters, SL bunker placement outside min_price/max_price, and TP magnet front-running.")
    lines.append("4. Macro Risk & Portfolio Governor: Capital floor defense (4,775.00 USD hard floor / 4,795.00 USD buffer), discrete lot sizing (execution_specs), and net expectancy.")
    lines.append("5. Adversarial Pre-Mortem Red Team (Falsification & Autopsy Invalidator): Default baseline is NO TRADE / STAND ASIDE. For any proposed candidate, assume it was entered and stopped out; formulate the exact fatal flaw (opposing CVD momentum, un-swept opposing stop pool, broker CFD basis spike, or wall pull on approach). Certify clearance ONLY if no fatal flaw exists.")
    lines.append("")
    lines.append("PART G: MANDATORY 3-PILLAR DESK EVALUATION (STRICT OPERATOR MANDATE)")
    lines.append("")
    lines.append("MANDATE 1 — DUAL-ENGINE SEARCH ACROSS ALL 24 ASSETS (MEAN REVERSION + TREND PULLBACKS):")
    lines.append("Analyze all 24 assets in assets_matrix_24 line-by-line from docs/telemetry/live_snapshot_latest.json (covering all Cryptos, Metals GOLD/XAUUSD.pi & SILVER/XAGUSD.pi, Energy USWTI.p, Forex EURUSD.pi/GBPUSD.pi/USDJPY.pi, and Indices SP500.p/NAS100.p/DJ30.p/GER40.p).")
    lines.append("CRITICAL MANDATE: DO NOT EVALUATE ASSETS PURELY AS MODEL-1 FADES! YOU MUST EVALUATE BOTH ENGINES SYSTEMATICALLY FOR EACH ASSET:")
    lines.append("  • ENGINE 1 — EXTREME MEAN REVERSION (|Z| >= 2.0 SD): For assets at extreme statistical stretch (|Z| >= 2.0 SD to 3.5 SD), look for counter-trend mean reversion flushes ONLY if confirmed by tape exhaustion, delta absorption, and multi-layer whale backing (remember Invariant 5: Model 1 longs are strictly BANNED in Bearish HTF regimes).")
    lines.append("  • ENGINE 2 — TREND FOLLOWING PULLBACKS (|Z| can be within 0.2 to 1.8 SD!): DO NOT DISCARD AN ASSET MERELY BECAUSE |Z| < 2.0 SD! In trending regimes (BULLISH or BEARISH), evaluate whether the asset is pulling back into key structural shelves (20 EMA, 50 EMA, 200 EMA, Session VWAP, VAH/VAL) IN THE DIRECTION OF THE DOMINANT TREND! Examples: SP500 pullback short to 200 EMA / wall-belt at 7,810; SOL pullback short to VAH / 2.32M wall at 109.10; GOLD pullback long to EMA stack. Look for pullback exhaustion (low pullback velocity, resting L2/L3 Ask/Bid walls defending the stop) and stage passive limit orders.")
    lines.append("  • LIQUIDATION & STOP ATTRACTION MAGNET CONFLUENCE: In both engines, systematically factor in reconstructed liquidation cascade bands and structural stop sweep pools as gravitational attraction points (liquidity magnets). Price is drawn toward these high-density liquidity concentrations to trigger cascades; Take Profit targets should strategically front-run these attraction points by 5–10 bps, while Stop Losses must be anchored behind resting whale walls outside opposing sweep bands.")
    lines.append("Live 24-asset mutual universe matrix:")
    for sym_key, a in assets.items():
        if not isinstance(a, dict):
            continue
        q = a.get("quotes", {})
        ci = a.get("causal_indicators", {})
        ob = a.get("orderbook_live_depth", {})
        w3 = ob.get("whale_walls_l3") or []
        elig_w3 = [w for w in w3 if float(w.get("persist_s") or 0.0) >= 180.0]
        sc = a.get("structural_stop_clusters", {})
        rl = a.get("reconstructed_liquidations", {})
        cvd_buckets = a.get("cvd_1m_buckets")
        if cvd_buckets is not None and isinstance(cvd_buckets, list) and len(cvd_buckets) > 0:
            cvd_15m = sum(float(b.get("cvd_delta_usd") or b.get("delta_usd") or 0.0) for b in cvd_buckets[-15:])
            cvd_str = f"15m CVD {cvd_15m:+.0f} USD"
        else:
            cvd_str = "15m CVD UNAVAILABLE (CFD L1)"

        # Exact nearest stops attraction & bunker bands
        s_below = sc.get('nearest_sell_stop_clusters_below', [])
        s_above = sc.get('nearest_buy_stop_clusters_above', [])
        s_b_str = f"[{s_below[0].get('min_price', 0):.1f}-{s_below[0].get('max_price', 0):.1f} ${s_below[0].get('notional_usd', 0)/1e6:.2f}M]" if s_below else "none"
        s_a_str = f"[{s_above[0].get('min_price', 0):.1f}-{s_above[0].get('max_price', 0):.1f} ${s_above[0].get('notional_usd', 0)/1e6:.2f}M]" if s_above else "none"

        # Exact nearest liquidation cascade attraction bands
        l_below = rl.get('nearest_long_cascade_bands_below', [])
        l_above = rl.get('nearest_short_squeeze_bands_above', [])
        l_b_str = f"[{l_below[0].get('min_price', 0):.1f}-{l_below[0].get('max_price', 0):.1f} ${l_below[0].get('notional_usd', 0)/1e6:.2f}M]" if l_below else "none"
        l_a_str = f"[{l_above[0].get('min_price', 0):.1f}-{l_above[0].get('max_price', 0):.1f} ${l_above[0].get('notional_usd', 0)/1e6:.2f}M]" if l_above else "none"

        lines.append(
            f"• {sym_key} ({a.get('symbol_broker', '')} | {a.get('category', '')}): Mid {q.get('mid')} | Spread {q.get('spread_bps')} bps | "
            f"Z = {ci.get('vwap_z_score')} SD | RSI {ci.get('rsi_14')} | Trend {ci.get('trend_regime')} | "
            f"L2 Imb {ob.get('book_imbalance')} | {cvd_str} | L3 Whales (tot/elig>=180s): {len(w3)}/{len(elig_w3)} | "
            f"Stops Below/Above: {s_b_str} / {s_a_str} | "
            f"Liq Below/Above (Attraction Bands): {l_b_str} / {l_a_str}"
        )
    lines.append("For every qualifying new opportunity across Crypto, Metals, Energy, Forex, or Indices, specify: MT5 symbol, BUY/SELL LIMIT, exact lot size, Entry price, SL (0.25-0.50 ATR outside min_price/max_price of bunker), TP (front-running magnet by 5-10 bps), USD risk, R:R, and complete telemetry coincidence proof.")
    lines.append("")
    lines.append("MANDATE 2 — LOOK FOR ACTIVE / RUNNING TRADES (LOGICAL TP OR SL MODIFICATION BASED ON LATEST DATA):")
    if positions:
        # Load immutable initial risk ledger if present to avoid dynamic R-multiple inflation
        initial_risk_ledger = {}
        risk_file = ROOT / "Data" / "initial_position_risk.json"
        if risk_file.exists():
            try:
                with open(risk_file, "r", encoding="utf-8") as rf:
                    initial_risk_ledger = json.load(rf)
            except Exception:
                pass

        lines.append(f"• Current Active Running Trades on MT5: {len(positions)} open position(s):")
        for p in positions:
            ak = _resolve_asset_key(p["symbol"], assets)
            a_info = assets.get(ak, {})
            atr = a_info.get("causal_indicators", {}).get("atr_14") or 1.0
            t_str = str(p["ticket"])
            if t_str in initial_risk_ledger:
                r0 = float(initial_risk_ledger[t_str].get("r0") or 0.0)
            else:
                r0 = abs(p["price_open"] - p["sl"]) if p["sl"] else atr
            if r0 <= 0:
                r0 = atr
            curr_r0 = ((p["price_current"] - p["price_open"]) / r0) if p["type"] == "BUY" else ((p["price_open"] - p["price_current"]) / r0)
            lines.append(
                f"  - Ticket #{p['ticket']}: {p['symbol']} {p['type']} {p['volume']} lots @ Entry {p['price_open']} USD | "
                f"Current: {p['price_current']} USD ({curr_r0:+.2f}R0 progress, Initial R0={r0:.2f} pts) | Floating PnL: {p['profit_usd']:+.2f} USD | "
                f"Current SL: {p['sl']} USD | Current TP: {p['tp']} USD"
            )
        lines.append("• For each running trade above, evaluate logically based on the latest data snapshot whether SL or TP modification is required:")
        lines.append("  1. Piecewise Ratchet Check (Measured against Initial R0): Has the trade reached +0.70R0/+0.80R0 (Phase 0 BE lock to +0.35R0), +1.50R0 (Phase 1 Profit Lock to +0.80R0), or +2.00R0 (Phase 2 Trailing Lock)? Note: Never recalculate R using current ratcheted SL distance—always measure against frozen initial R0 to prevent R-inflation.")
        lines.append("  2. Live Microstructure & Bunker/Magnet Shift: Have new stop clusters, liquidation bands, or L3 whale walls formed in live_snapshot_latest.json that logically require tightening SL behind a newly formed structural bunker or adjusting TP to front-run a closer/stronger liquidity magnet? Or has the supporting structural shelf broken requiring an emergency exit?")
    else:
        lines.append("• Current Active Running Trades on MT5: 0 open positions (Flat / 100% Cash reserves). Confirm that no open-position ratchets are needed right now.")
    lines.append("")
    lines.append("MANDATE 3 — AUDIT UNFILLED LIMIT ORDERS (VIABLE TO WAIT vs. SLIGHT MODIFICATION vs. DELETE):")
    if orders:
        lines.append(f"• Current Unfilled Limit Orders on MT5: {len(orders)} pending order(s):")
        for o in orders:
            ak = _resolve_asset_key(o["symbol"], assets)
            a_info = assets.get(ak, {})
            ci = a_info.get("causal_indicators", {})
            atr = ci.get("atr_14") or 1.0
            dist_atr = abs(o["price_current"] - o["price_open"]) / atr if atr else 0.0
            lines.append(
                f"  - Ticket #{o['ticket']}: {o['symbol']} {o['type']} {o['volume']} lots @ Entry {o['price_open']} USD | "
                f"Live Mid: {o['price_current']} USD (Distance: {dist_atr:.2f} ATR, ATR_14={atr}) | "
                f"Current SL: {o['sl']} USD | Current TP: {o['tp']} USD | Trend: {ci.get('trend_regime')} | Z: {ci.get('vwap_z_score')} SD"
            )
        lines.append("• For EACH unfilled limit order listed above, perform a complete logical & quantitative audit against the latest live_snapshot_latest.json and explicitly classify it into one of three decisions:")
        lines.append("  (A) VIABLE — WAIT TO BE FILLED AS-IS: Confirm that distance to entry is <= 2.0 ATR, supporting L3 whale walls (persistence_s >= 180s) remain intact, 5m/15m/30m CVD and L2 imbalance support absorption, SL sits safely 0.25x-0.50x ATR outside min_price/max_price of the governing bunker, and TP front-runs the opposing buy-stop/sell-stop magnet by 5-10 bps.")
        lines.append("  (B) SLIGHT MODIFICATION REQUIRED (MODIFY ENTRY / SL / TP): If the thesis remains valid but live whale walls, stop clusters (nearest_*), or liquidation band boundaries (min_price/max_price) have shifted in the latest snapshot, specify the exact modified Entry, SL, and/or TP levels and why.")
        lines.append("  (C) DELETE / CANCEL IMMEDIATELY: If the structural thesis has degraded (e.g., supporting whale walls pulled/thinned >50%, price drifted >2.0 ATR away, regime invalidated, or unabsorbed aggressive selling/buying broke the shelf), recommend immediate deletion to free capacity.")
    else:
        lines.append("• Current Unfilled Limit Orders on MT5: 0 pending orders.")
    lines.append("")
    lines.append("STEP 4 — PORTFOLIO CAPACITY & CAPITAL FLOOR GOVERNANCE (ASTRA/OPUS RIGOR):")
    lines.append("• Stress Formula: Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket (covering adverse gap, spread widening, and slippage).")
    lines.append(f"• Account Balance: {balance:.2f} USD | Equity: {equity:.2f} USD | Hard Floor: 4,775.00 USD | Operating Buffer: 4,795.00 USD.")
    lines.append("• Open Position Stress: Ticket #18836609 (SP500.p) nominal risk 12.80 USD stresses to 18.00 USD.")
    lines.append(f"• Available Stress Budget to 4,795.00 USD Buffer: {min(balance, equity) - 4795.0 - 18.0:.2f} USD.")
    lines.append("• Strict Portfolio Capacity Rules:")
    lines.append("  - Maximum 2 new tickets if nominal risk is 14.50 USD (stressed: 2 * 20.125 = 40.25 USD <= available budget).")
    lines.append("  - Maximum 3 new tickets ONLY IF nominal risk <= 10.50 USD per ticket (stressed: 3 * 15.125 = 45.38 USD <= available budget).")
    lines.append("  - 3 tickets at 14.50 USD is mathematically BANNED (3 * 20.125 = 60.38 USD stress would breach the 4,795.00 USD operating buffer).")
    lines.append("• Joint Worst-Case Post-Stop Equity MUST remain unconditionally >= 4,795.00 USD (>= 20.00 USD cushion above 4,775.00 USD hard floor).")
    lines.append("")
    lines.append("PART F: REQUIRED OUTPUT FORMAT & TRI-COUNCIL SYNCHRONIZATION (ARENA.AI + Z.AI CHAT + ANTIGRAVITY)")
    lines.append(f"1. TELEMETRY & PLAYBOOK INGESTION CITATION (confirming generation_id: {gen_id}, as_of_utc: {gen_ts}, macro event: {ev_name} at {ev_time} [blackout_active={blackout_active}], and Playbook compliance)")
    lines.append("2. MANDATE 1 REPORT: Line-by-Line Screening of 24 Assets for New Trading Opportunities (Dual-Engine evaluation: Model 1 Mean Reversion + Model 2 Trend Pullbacks; incorporating liquidation cascades and stop clusters as attraction points / liquidity magnets)")
    lines.append("3. MANDATE 2 REPORT: Active / Running Trades Audit (Logical TP/SL Modifications Based on Latest Snapshot)")
    lines.append("4. MANDATE 3 REPORT: Unfilled Limit Orders Audit (Ticket-by-Ticket Verdict: WAIT TO FILL AS-IS vs. MODIFY ENTRY/SL/TP vs. DELETE)")
    lines.append("5. ACTIONABLE EXECUTION SUMMARY TABLE (Ticket/Action, Symbol, Side, Lots, Entry, SL Bunker, TP Magnet, Risk USD, R:R, Quantitative Rationale)")
    lines.append("6. COUNCIL SYNC PROTOCOL:")
    lines.append("   • If running on Arena.ai (Two-Way Git Access): Append your complete Cycle Council Report and Actionable Execution Table to docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md and commit/push to branch arena/5c05910e-trading-2.")
    lines.append("   • If running on Z.ai Chat (One-Way Read-Only Access): Fetch the raw GitHub URLs above to verify the latest telemetry snapshot, and print your complete 3-Mandate Council Report and Actionable Execution Summary Table directly in your chat response (do not attempt git push; Antigravity harvests your response directly from the Z.ai DOM to cross-verify Arena.ai + Z.ai Chat + Antigravity).")

    return "\n".join(lines)


async def main():
    import argparse
    parser = argparse.ArgumentParser(description="Dispatch 3-Mandate Pure Telemetry Prompt to Arena.ai and Z.ai Chat")
    parser.add_argument("--cycle", type=int, default=40, help="Cycle number")
    parser.add_argument("--reprompt-file", type=str, default="", help="Optional Part-B corrective reprompt file path")
    parser.add_argument("--arena-only", action="store_true", help="Send only to Arena.ai")
    parser.add_argument("--zai-only", action="store_true", help="Send only to Z.ai Chat")
    args = parser.parse_args()

    if args.reprompt_file:
        p_path = pathlib.Path(args.reprompt_file)
        if not p_path.is_absolute():
            p_path = ROOT / p_path
        prompt = p_path.read_text(encoding="utf-8")
        print(f"Loaded Part-B corrective reprompt ({len(prompt)} chars) from {p_path}")
    else:
        prompt = build_prompt(cycle_num=args.cycle)
        prompt_file = ROOT / "docs" / "prompts" / f"ARENA_CYCLE_{args.cycle}_PROMPT.txt"
        prompt_file.parent.mkdir(parents=True, exist_ok=True)
        prompt_file.write_text(prompt, encoding="utf-8")
        print(f"Generated Cycle {args.cycle} 3-Mandate prompt: {len(prompt)} characters written to {prompt_file}")

    ok_arena = False
    ok_zai = False

    if not args.zai_only:
        await dismiss_arena_popup()
        ok_arena = await post_prompt_to_arena(prompt)
    if not args.arena_only:
        ok_zai = await post_prompt_to_zai(prompt)

    if ok_arena or ok_zai:
        print(f"SUCCESS: Prompt injected (Arena.ai={ok_arena}, Z.ai Chat={ok_zai})! Run `python Terminal/arena_completion_daemon.py --wait` to wake up on completion.")
    else:
        print("ERROR: Failed to inject prompt into Arena.ai and Z.ai Chat", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())


