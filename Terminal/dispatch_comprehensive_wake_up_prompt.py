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

    lines = []
    lines.append(f"TRADING DESK COUNCIL: CYCLE {cycle_num} PURE TELEMETRY & PLAYBOOK ANALYSIS PROMPT")
    lines.append("MANDATE: 100% DIRECT LINE-BY-LINE ANALYSIS OF docs/telemetry/live_snapshot_latest.json (ZERO DECISION GATES)")
    lines.append("")
    lines.append("PART A: REQUIRED READING (complete before analysis)")
    lines.append("Read the following repository sources in full:")
    lines.append("")
    lines.append("1. Live Telemetry Matrix (Primary Ground Truth): docs/telemetry/live_snapshot_latest.json")
    lines.append(f"   Latest Generation: {gen_id} ({gen_ts})")
    lines.append("   Upstream: https://github.com/kbsingh1399/Trading_2/blob/arena/537c1eb8-trading-2/docs/telemetry/live_snapshot_latest.json")
    lines.append("   Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json")
    lines.append("   Inspect all 24 assets in assets_matrix_24 and all telemetry blocks: quotes (MT5 spread_bps & mid), execution_specs, causal_indicators (Session VWAP, Z-score, RSI, ATR, EMA 20/50/200, POC/VAH/VAL), orderbook_live_depth (20-level L2 depth & imbalance), whale_walls_l3 (0x... wallet addresses, sizes, persistence_s >= 180s), structural_stop_clusters (nearest_sell_stop_clusters_below, nearest_buy_stop_clusters_above, top_*), reconstructed_liquidations (nearest_long_cascade_bands_below, nearest_short_squeeze_bands_above, top_*), venue_basis, and cvd_1m_buckets (5m/15m/30m sums).")
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
    lines.append("• Hard floor: 4,775.00 USD | Operating buffer: 4,795.00 USD")
    lines.append(f"• Live cushion: +{cushion:.2f} USD above hard floor (+{buffer_cushion:.2f} USD above operating buffer)")
    lines.append("• Risk per trade: 10.00 to 14.50 USD (0.20% to 0.29% of capital). Up to 4 concurrent tickets across orthogonal asset clusters provided joint worst-case post-stop equity >= 4,795.00 USD.")
    lines.append("")
    lines.append("PART C: STRICT OPERATOR MANDATE — PURE TELEMETRY REASONING (NO DECISION GATES)")
    lines.append("1. DO NOT RUN OR CITE decision_gates_v3.py OR LEGACY GATE TOKENS:")
    lines.append("   • Programmatic gate scripts (decision_gates_v3.py, A1-A5, B1-B6, G-4, G-6, MAX_TARGET_DIST_ATR = 4.0, A2_no_tape_fail_closed) are RETIRED from trade selection.")
    lines.append("   • Do NOT disqualify TradFi CFDs (SP500, NAS100, EURUSD, USDJPY, XAUUSD, USWTI) just because cvd_1m_buckets is 0; evaluate them using their MT5 spreads, VWAP Z-scores, EMA/VP shelves, Hyperliquid L2 orderbook imbalance, L3 whale wallet orders (0x...), structural stop clusters, and liquidation bands.")
    lines.append("2. MULTI-PARAMETER COINCIDENCE & BOUNDARY PRECISION (per docs/specs/TRADE_DECISION_PLAYBOOK.md):")
    lines.append("   • Entry Level: Must sit AT or BELOW the sell-stop sweep midpoint (for Longs) or AT or ABOVE the buy-stop sweep midpoint (for Shorts), directly backed by resting L3 whale wallet orders (0x..., persistence_s >= 180s), adjusted onto the MT5 price grid via venue_basis.")
    lines.append("   • Stop Loss (Liquidity Bunker): Must sit 0.25x-0.50x ATR OUTSIDE min_price (for Longs) or max_price (for Shorts) of the governing liquidation cascade band and stop cluster — NEVER measured from mid_price and NEVER placed inside the [min_price, max_price] band.")
    lines.append("   • Take Profit (Liquidity Magnet): Must front-run the opposing buy-stop / short-squeeze magnet (or sell-stop / long-cascade magnet) by 5-10 bps.")
    lines.append("")
    lines.append("PART D: COUNCIL PERSONAS")
    lines.append("1. Orderflow & Microstructure Analyst: MT5 spread_bps, L2 20-level depth & imbalance, L3 on-chain wallet orders (0x..., persistence_s >= 180s), and multi-window 1m CVD (5m, 15m, 30m).")
    lines.append("2. Structural Price Action Specialist: Session VWAP & SD bands (Z-score), Volume Profile (POC/VAH/VAL), 20/50/200 EMA hierarchy, and psychological round numbers.")
    lines.append("3. Liquidation & Stop Hunt Forensic: Reconstructed liquidation cascade bands (nearest_* and top_*), stop clusters, SL bunker placement outside min_price/max_price, and TP magnet front-running.")
    lines.append("4. Macro Risk & Portfolio Governor: Capital floor defense (4,775.00 USD hard floor / 4,795.00 USD buffer), discrete lot sizing (execution_specs), and net expectancy.")
    lines.append("")
    lines.append("PART E: MANDATORY 3-PILLAR DESK EVALUATION (STRICT OPERATOR MANDATE)")
    lines.append("")
    lines.append("MANDATE 1 — LOOK FOR NEW TRADING OPPORTUNITIES ACROSS ALL 24 MUTUAL UNIVERSE ASSETS (CRYPTO, METALS, ENERGY, FOREX & INDICES):")
    lines.append("Analyze all 24 assets in assets_matrix_24 line-by-line from docs/telemetry/live_snapshot_latest.json (covering all Cryptos, Metals GOLD/XAUUSD.pi & SILVER/XAGUSD.pi, Energy USWTI.p, Forex EURUSD.pi/GBPUSD.pi/USDJPY.pi, and Indices SP500.p/NAS100.p/DJ30.p/GER40.p) to identify any new high-confluence Model 1 (|Z| >= 2.0 SD Mean Reversion) or Model 2 (Trend Pullback to VWAP/VAL/VAH/EMA) limit order setups. Live 24-asset mutual universe matrix:")
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
        cvd_buckets = a.get("cvd_1m_buckets") or []
        cvd_15m = sum(float(b.get("cvd_delta_usd") or b.get("delta_usd") or 0.0) for b in cvd_buckets[-15:]) if cvd_buckets else 0.0
        lines.append(
            f"• {sym_key} ({a.get('symbol_broker', '')} | {a.get('category', '')}): Mid {q.get('mid')} | Spread {q.get('spread_bps')} bps | "
            f"Z = {ci.get('vwap_z_score')} SD | RSI {ci.get('rsi_14')} | Trend {ci.get('trend_regime')} | "
            f"L2 Imb {ob.get('book_imbalance')} | 15m CVD {cvd_15m:+.0f} USD | L3 Whales (tot/elig>=180s): {len(w3)}/{len(elig_w3)} | "
            f"Nearest Stops (below/above): {len(sc.get('nearest_sell_stop_clusters_below', []))}/{len(sc.get('nearest_buy_stop_clusters_above', []))} | "
            f"Nearest Liq (long/short): {len(rl.get('nearest_long_cascade_bands_below', []))}/{len(rl.get('nearest_short_squeeze_bands_above', []))}"
        )
    lines.append("For every qualifying new opportunity across Crypto, Metals, Energy, Forex, or Indices, specify: MT5 symbol, BUY/SELL LIMIT, exact lot size, Entry price, SL (0.25-0.50 ATR outside min_price/max_price of bunker), TP (front-running magnet by 5-10 bps), USD risk, R:R, and complete telemetry coincidence proof.")
    lines.append("")
    lines.append("MANDATE 2 — LOOK FOR ACTIVE / RUNNING TRADES (LOGICAL TP OR SL MODIFICATION BASED ON LATEST DATA):")
    if positions:
        lines.append(f"• Current Active Running Trades on MT5: {len(positions)} open position(s):")
        for p in positions:
            ak = _resolve_asset_key(p["symbol"], assets)
            a_info = assets.get(ak, {})
            atr = a_info.get("causal_indicators", {}).get("atr_14") or 1.0
            r_dist = abs(p["price_open"] - p["sl"]) if p["sl"] else atr
            curr_r = ((p["price_current"] - p["price_open"]) / r_dist) if p["type"] == "BUY" and r_dist > 0 else (((p["price_open"] - p["price_current"]) / r_dist) if r_dist > 0 else 0.0)
            lines.append(
                f"  - Ticket #{p['ticket']}: {p['symbol']} {p['type']} {p['volume']} lots @ Entry {p['price_open']} USD | "
                f"Current: {p['price_current']} USD ({curr_r:+.2f}R) | Floating PnL: {p['profit_usd']:+.2f} USD | "
                f"Current SL: {p['sl']} USD | Current TP: {p['tp']} USD"
            )
        lines.append("• For each running trade above, evaluate logically based on the latest data snapshot whether SL or TP modification is required:")
        lines.append("  1. Piecewise Ratchet Check: Has the trade reached +0.70R/+0.80R (Phase 0 BE lock to +0.35R), +1.50R (Phase 1 Profit Lock to +0.80R), or +2.00R (Phase 2 Trailing Lock)?")
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
    lines.append("STEP 4 — PORTFOLIO CAPACITY & CAPITAL FLOOR GOVERNANCE:")
    lines.append("• Verify that all kept/modified running trades + kept/modified resting limit orders + any newly proposed limit orders keep joint worst-case post-stop equity >= 4,795.00 USD (>= 20.00 USD cushion above the 4,775.00 USD hard floor).")
    lines.append("")
    lines.append("PART F: REQUIRED OUTPUT FORMAT & BILATERAL LEDGER PUSH")
    lines.append("1. TELEMETRY & PLAYBOOK INGESTION CITATION (confirming generation_id, as_of_utc, and Playbook compliance)")
    lines.append("2. MANDATE 1 REPORT: Line-by-Line Screening of 24 Assets for New Trading Opportunities")
    lines.append("3. MANDATE 2 REPORT: Active / Running Trades Audit (Logical TP/SL Modifications Based on Latest Snapshot)")
    lines.append("4. MANDATE 3 REPORT: Unfilled Limit Orders Audit (Ticket-by-Ticket Verdict: WAIT TO FILL AS-IS vs. MODIFY ENTRY/SL/TP vs. DELETE)")
    lines.append("5. ACTIONABLE EXECUTION SUMMARY TABLE (Ticket/Action, Symbol, Side, Lots, Entry, SL Bunker, TP Magnet, Risk USD, R:R, Quantitative Rationale)")
    lines.append("6. BILATERAL LEDGER SYNC: Append your complete Cycle Council Report and Actionable Execution Table to docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md and commit/push to branch arena/537c1eb8-trading-2 (while Antigravity merges and syncs to main).")

    return "\n".join(lines)


async def main():
    import argparse
    parser = argparse.ArgumentParser(description="Dispatch 3-Mandate Pure Telemetry Prompt to Arena.ai")
    parser.add_argument("--cycle", type=int, default=40, help="Cycle number")
    parser.add_argument("--reprompt-file", type=str, default="", help="Optional Part-B corrective reprompt file path")
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

    await dismiss_arena_popup()
    ok = await post_prompt_to_arena(prompt)
    if ok:
        print(f"SUCCESS: Prompt injected into Arena.ai! Run `python Terminal/arena_completion_daemon.py --wait` to wake up on completion.")
    else:
        print("ERROR: Failed to inject prompt into Arena.ai", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())

