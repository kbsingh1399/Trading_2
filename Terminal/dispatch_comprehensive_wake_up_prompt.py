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

def build_prompt() -> str:
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
    lines.append("TRADING DESK COUNCIL: CYCLE 39 PURE TELEMETRY & PLAYBOOK ANALYSIS PROMPT")
    lines.append("MANDATE: 100% DIRECT LINE-BY-LINE ANALYSIS OF docs/telemetry/live_snapshot_latest.json (ZERO DECISION GATES)")
    lines.append("")
    lines.append("PART A: REQUIRED READING (complete before analysis)")
    lines.append("Read the following repository sources in full:")
    lines.append("")
    lines.append("1. Live Telemetry Matrix (Primary Ground Truth): docs/telemetry/live_snapshot_latest.json")
    lines.append(f"   Latest Generation: {gen_id} ({gen_ts})")
    lines.append("   Upstream: https://github.com/kbsingh1399/Trading_2/blob/arena/537c1eb8-trading-2/docs/telemetry/live_snapshot_latest.json")
    lines.append("   Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json")
    lines.append("   Inspect all 24 assets in assets_matrix_24 and all telemetry blocks: quotes (MT5 spread_bps & mid), execution_specs, causal_indicators (Session VWAP, Z-score, RSI, ATR, EMA 20/50/200, POC/VAH/VAL), orderbook_live_depth (20-level L2 depth & imbalance), whale_walls_l3 (0x... wallet addresses, sizes, distances), structural_stop_clusters (top_sell_stop_clusters_below, top_buy_stop_clusters_above), reconstructed_liquidations (top_long_cascade_bands_below, top_short_squeeze_bands_above), venue_basis, and cvd_1m_buckets.")
    lines.append("")
    lines.append("2. Live Trade Decision Playbook: docs/specs/TRADE_DECISION_PLAYBOOK.md")
    lines.append("   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md")
    lines.append("   Apply the Parameter Coincidence Matrix (Entry Shelf + SL Liquidity Bunker + TP Liquidity Magnet + Psychological Round Numbers), Dual-Venue Division of Labor (Spreads/Quotes from MT5; Orderbook/Whales/Liquidations/Stops from Hyperdash & Binance), and the 7-Point Pre-Trade Checklist.")
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
    lines.append("   • Do NOT disqualify setups using an arbitrary 4.0 ATR target cap if structural levels (Session VWAP, POC, VAH/VAL, EMA shelves, overhead buy-stop clusters, or psychological round numbers) provide logical targets with >= 1.8R to 2.5R reward.")
    lines.append("2. MULTI-PARAMETER COINCIDENCE DEBATE (per docs/specs/TRADE_DECISION_PLAYBOOK.md):")
    lines.append("   • Entry Level: Where a structural level (Session VWAP, VAL/VAH, POC, 20/50/200 EMA, or >= 2.0 SD band) coincides with resting L2 depth and L3 whale wallet orders (0x...), adjusted onto the MT5 price grid via venue_basis.")
    lines.append("   • Stop Loss (Liquidity Bunker): Placed safely BEHIND the nearest major reconstructed liquidation cascade band and sell-stop/buy-stop cluster with a 0.25x-0.50x ATR buffer, never inside the sweep zone.")
    lines.append("   • Take Profit (Liquidity Magnet): Placed directly INTO (or slightly front-running) opposing short-squeeze / long-liquidation bands, stop clusters, Session VWAP/POC, and psychological round numbers.")
    lines.append("")
    lines.append("PART D: COUNCIL PERSONAS")
    lines.append("1. Orderflow & Microstructure Analyst: MT5 spread_bps, L2 20-level depth & imbalance, L3 on-chain wallet orders (0x...), and crypto CVD taker absorption.")
    lines.append("2. Structural Price Action Specialist: Session VWAP & SD bands (Z-score), Volume Profile (POC/VAH/VAL), 20/50/200 EMA hierarchy, and psychological round numbers.")
    lines.append("3. Liquidation & Stop Hunt Forensic: Reconstructed liquidation cascade bands, stop clusters, SL bunker placement, and TP magnet front-running.")
    lines.append("4. Macro Risk & Portfolio Governor: Capital floor defense (4,775.00 USD hard floor / 4,795.00 USD buffer), discrete lot sizing (execution_specs), and net expectancy.")
    lines.append("")
    lines.append("PART E: TASKS")
    lines.append("Step 1: Pure Telemetry Analysis of docs/telemetry/live_snapshot_latest.json across all 24 assets")
    lines.append("Analyze all 24 assets line by line directly from docs/telemetry/live_snapshot_latest.json. Pay special attention to:")
    for sym_key in ["SP500", "NAS100", "EURUSD", "USDJPY", "BTC", "ETH", "SOL", "XAUUSD"]:
        a = assets.get(sym_key, {})
        if not a:
            continue
        q = a.get("quotes", {})
        ci = a.get("causal_indicators", {})
        ob = a.get("orderbook_live_depth", {})
        w3 = a.get("whale_walls_l3", [])
        sc = a.get("structural_stop_clusters", {})
        rl = a.get("reconstructed_liquidations", {})
        lines.append(
            f"• {sym_key} ({a.get('asset_class', '')}): Mid {q.get('mid')} | Spread {q.get('spread_bps')} bps | "
            f"Z = {ci.get('vwap_z_score')} SD | RSI {ci.get('rsi_14')} | Trend {ci.get('trend_regime')} | "
            f"L2 Imbalance {ob.get('imbalance')} | L3 Whales: {len(w3)} | "
            f"Stops (below/above): {len(sc.get('top_sell_stop_clusters_below', []))}/{len(sc.get('top_buy_stop_clusters_above', []))} | "
            f"Liq Bands (long/short): {len(rl.get('top_long_cascade_bands_below', []))}/{len(rl.get('top_short_squeeze_bands_above', []))}"
        )
    lines.append("For every qualifying setup (Mean Reversion or Trend Following), provide exact MT5 symbol, BUY/SELL LIMIT, volume (lots), Entry price, SL (behind bunker), TP (front-running magnet), USD risk, R:R, and the exact coincidence of parameters from live_snapshot_latest.json.")
    lines.append("")
    lines.append("Step 2: Audit running trades and ratchets")
    if positions:
        lines.append(f"• Current open positions on MT5: {len(positions)} active position(s):")
        for p in positions:
            lines.append(f"  - Ticket #{p['ticket']}: {p['symbol']} {p['type']} {p['volume']} lots @ {p['price_open']} USD | Current: {p['price_current']} USD | Floating: {p['profit_usd']:+.2f} USD | SL: {p['sl']} USD | TP: {p['tp']} USD")
    else:
        lines.append("• Current open positions on MT5: 0 (Flat, 100% Cash reserves).")
    lines.append("")
    lines.append("Step 3: Audit resting limit orders")
    if orders:
        lines.append(f"• Current pending orders on MT5: {len(orders)} active order(s):")
        for o in orders:
            lines.append(f"  - Ticket #{o['ticket']}: {o['symbol']} {o['type']} {o['volume']} lots @ {o['price_open']} USD | Spot: {o['price_current']} USD | SL: {o['sl']} USD | TP: {o['tp']} USD")
        lines.append("• Evaluate Ticket #18791527 purely under the Playbook: Spot is above the 200 EMA, limit is at 83,150 USD, SL is at 82,650 USD below the 82,700-82,800 liquidation cascade band, and overhead buy-stop clusters sit at 84,250-84,350 USD. Should we maintain as-is, or adjust TP to 84,250-84,340 USD to front-run the buy-stop clusters?")
    else:
        lines.append("• Current pending orders on MT5: 0.")
    lines.append("")
    lines.append("Step 4: Capacity and capital floor governance")
    lines.append("• Verify that all active + proposed limit orders keep stressed post-stop equity >= 4,795.00 USD (>= 20.00 USD cushion above the 4,775.00 USD hard floor).")
    lines.append("")
    lines.append("PART F: OUTPUT FORMAT")
    lines.append("1. TELEMETRY & PLAYBOOK INGESTION CITATION (confirming generation_id, generated_at_utc, and Playbook rules)")
    lines.append("2. Line-by-Line Multi-Parameter Debate across all 24 assets (focusing on SP500, NAS100, EURUSD, USDJPY, BTC, ETH, SOL, XAUUSD without any legacy gate vetoes)")
    lines.append("3. Resting Order Audit on Ticket #18791527 (including whether to front-run the 84,250-84,350 USD buy-stop magnet)")
    lines.append("4. Actionable Limit Order Table (Symbol, Side, Lots, Entry, SL Bunker, TP Magnet, Risk USD, R:R, Parameter Coincidence Rationale)")

    return "\n".join(lines)

async def main():
    prompt = build_prompt()
    prompt_file = ROOT / "docs" / "prompts" / "ARENA_CYCLE_39_PROMPT.txt"
    prompt_file.parent.mkdir(parents=True, exist_ok=True)
    prompt_file.write_text(prompt, encoding="utf-8")
    print(f"Generated unified prompt: {len(prompt)} characters written to {prompt_file}")
    
    await dismiss_arena_popup()
    ok = await post_prompt_to_arena(prompt)
    if ok:
        print("SUCCESS: Unified Cycle 39 Pure Telemetry Council Prompt injected into Arena.ai!")
    else:
        print("ERROR: Failed to inject prompt into Arena.ai", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
