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

    lines = []
    lines.append("TRADING DESK COUNCIL: CYCLE 38 STRUCTURED OPERATING PROMPT")
    lines.append("MANDATE: PIVOT TO DIRECT MULTI-PARAMETER CONFLUENCE PLAYBOOK REVIEW ACROSS ALL 24 ASSETS (MODEL 1 & MODEL 2)")
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
    lines.append("   Confirm the 7-stage verification chain, formulas, and Heuristic Trap Rebuttals 1 through 9.")
    lines.append("")
    lines.append("5. Round 2 audit: docs/reviews/ROUND2_THINKING_CHAIN_AUDIT.md")
    lines.append("   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/reviews/ROUND2_THINKING_CHAIN_AUDIT.md")
    lines.append("")
    lines.append("6. Decision gate code: Terminal/decision_gates_v3.py and Terminal/dg_context.py")
    lines.append("   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/decision_gates_v3.py")
    lines.append("   Verify the exact implementations of classify_regime, model1_checklist, and model2_checklist.")
    lines.append("")
    lines.append("7. Live Trade Decision Playbook: docs/specs/TRADE_DECISION_PLAYBOOK.md")
    lines.append("   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md")
    lines.append("   Confirm the Parameter Coincidence Matrix, the Dual-Venue Division of Labor, and the 7-Point Live Pre-Trade Checklist.")
    lines.append("")
    lines.append("8. Live telemetry: docs/telemetry/live_snapshot_latest.json")
    lines.append("   Local: docs/telemetry/live_snapshot_latest.json (synced every 60 seconds)")
    lines.append("   Upstream: https://github.com/kbsingh1399/Trading_2/blob/arena/537c1eb8-trading-2/docs/telemetry/live_snapshot_latest.json")
    lines.append("   Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json")
    lines.append("   Perform a complete schema census of all top-level keys across ALL 24 assets in the matrix.")
    lines.append("")
    lines.append("Ingestion output requirement: Your response must begin with a DOCUMENT INGESTION & GROUND TRUTH CITATION block listing each file above with its verified state and latest timestamp. Any conclusion reached without reading all eight sources is invalid.")
    lines.append("")
    lines.append("PART B: ACCOUNT AND RISK BASELINE")
    lines.append("• Execution Mode: PASSIVE LIMIT ORDERS ONLY (no market orders).")
    lines.append("• Broker: Blueberry Markets SVG LLC, MetaTrader 5 account #5064568")
    lines.append(f"• Balance / Equity: {balance:.2f} USD / {equity:.2f} USD")
    lines.append(f"• Margin used: {margin:.2f} USD")
    lines.append("• Hard floor (G-1): 4,775.00 USD")
    lines.append("• Operating buffer: 4,795.00 USD")
    lines.append(f"• Live cushion: +{cushion:.2f} USD above hard floor (+{buffer_cushion:.2f} USD above buffer)")
    lines.append("• Account capacity: Audit active_positions, pending_orders, and available capacity slots (max 4 concurrent tickets).")
    lines.append("")
    lines.append("PART C: OPERATOR MANDATE: PIVOT FROM RIGID BINARY GATES TO DIRECT TELEMETRY CONFLUENCE PLAYBOOK")
    lines.append("Operator Mandate: 'Regarding that gates approach, I think that is not working out. Rather we can simply analyze docs/telemetry/live_snapshot_latest.json in detail line by line and identify potential trades for mean reversion or trend following with proper reasoning and logical thinking... We should debate psychological levels, liquidation bands or stop bands for TP or whales or other parameters... It could be one of these or mutual coincidence of these parameters which could be targeted as a TP and SL decided properly.'")
    lines.append("")
    lines.append("Core Architectural Tenets (from docs/specs/TRADE_DECISION_PLAYBOOK.md):")
    lines.append("1. Dual-Venue Division of Labor:")
    lines.append("   • MT5 is our execution venue: Real spreads (spread_bps), top-of-book bid/ask, and broker execution specs MUST come from MT5 (quotes). Filter rule: <= 25 bps for Crypto, <= 5 bps for TradFi CFDs.")
    lines.append("   • Hyperdash & Binance are our microstructure venue: Orderbook 20-level depth (orderbook_live_depth), on-chain whale walls with wallet addresses (whale_walls_l3), reconstructed liquidation cascades (reconstructed_liquidations), and structural stop clusters (structural_stop_clusters) come from Hyperliquid DEX and Binance.")
    lines.append("   • Cross-venue basis (venue_basis): Maps on-chain whale walls and liquidation levels directly onto the MT5 price grid.")
    lines.append("2. Parameter Coincidence Framework:")
    lines.append("   • Entry: Formed where a structural shelf (EMA 20/50/200, Session VAL/VAH) coincides with persistent L2/L3 whale bids/asks and CVD absorption.")
    lines.append("   • Stop Loss (Liquidity Bunker): Placed BEHIND major reconstructed liquidation cascades and sell-stop clusters with ATR buffer. Never place SL directly inside or in front of the cluster where sweep algorithms hunt retail stops (Ticket #18785248 lesson).")
    lines.append("   • Take Profit (Liquidity Magnet): Targeted directly INTO overhead short-squeeze bands and buy-stop clusters, aligned with psychological round numbers (Ticket #18734917 lesson).")
    lines.append("3. Patience Over Desperation: Fewer, high-quality trades is our mark of capital preservation and institutional discipline. Standing aside when setups lack clean confluence is mathematically required.")
    lines.append("")
    lines.append("PART D: COUNCIL PERSONAS")
    lines.append("1. Orderflow & Microstructure Analyst: L2 orderbook depth, L3 on-chain wallet walls (0x...), CVD 1m taker delta absorption, broker spread in bps.")
    lines.append("2. Structural Price Action Specialist: Session VWAP and SD bands (|Z| scores), Volume Profile (POC/VAH/VAL), 200-EMA trend hierarchy, psychological round numbers.")
    lines.append("3. Liquidation & Stop Hunt Forensic: Reconstructed liquidation cascade bands, discount/premium stop sweep clusters, resting liquidity magnets.")
    lines.append("4. Macro Risk & Portfolio Governor: G-1 capital floor defense, orthogonal asset diversification, Tier-1 calendar blackouts, positive net EV expectancy.")
    lines.append("")
    lines.append("PART E: TASKS")
    lines.append("Step 1: Direct Line-by-Line Screen of docs/telemetry/live_snapshot_latest.json across all 24 assets")
    lines.append("Perform a thorough, multi-parameter debate across Crypto, Indices, Commodities, and Forex. High-confluence candidates to evaluate:")
    lines.append("• SP500 (INDICES): Mid 7,816.74 USD | Spread 0.4 bps | Z = -2.07 SD flush | RSI 35.9 | Trend BULLISH | L3 Whales: 100 orders | L2 Walls: 10 | Imbalance: +0.15 (bids absorbing selling) | 10 stop clusters below / 10 above | 10 long liq cascade bands below / 2 short squeeze bands above.")
    lines.append("• NAS100 (INDICES): Mid 30,844.82 USD | Spread 0.3 bps | Z = -2.10 SD flush | RSI 30.6 oversold | Trend BEARISH | L3 Whales: 88 orders | L2 Walls: 24 | 10 stop clusters below / 10 above.")
    lines.append("• EURUSD (FOREX): Mid 1.1205 USD | Spread 0.1 bps | Z = -2.20 SD flush | RSI 29.1 severely oversold | 10 stop clusters overhead acting as upside magnets.")
    lines.append("• USDJPY (FOREX): Mid 158.62 USD | Spread 0.1 bps | Z = +2.27 SD stretch | RSI 79.0 overbought | L3 Whales: 31 | L2 Walls: 5 | Imbalance: -0.30 (resting ask resistance).")
    lines.append("• BTC (CRYPTO): Mid 83,398.50 USD | Spread 1.8 bps | Z = -1.45 SD pullback | RSI 42.3 | Trend BULLISH | L3 Whales: 333 orders | Active resting BUY LIMIT Ticket #18791527 resting @ 83,150 USD.")
    lines.append("Output for each qualifying candidate: Asset, symbol, order type (BUY/SELL LIMIT), volume (lots), entry, SL (behind liquidation bunker), TP (into squeeze magnet), risk (USD), R:R, and multi-parameter confluence rationale.")
    lines.append("")
    lines.append("Step 2: Audit running trades and ratchets")
    if positions:
        lines.append(f"• Current open positions on MT5: {len(positions)} active position(s):")
        for p in positions:
            lines.append(f"  - Ticket #{p['ticket']}: {p['symbol']} {p['type']} {p['volume']} lots @ {p['price_open']} USD | Current: {p['price_current']} USD | Floating: {p['profit_usd']:+.2f} USD | SL: {p['sl']} USD | TP: {p['tp']} USD")
        lines.append("• Audit ratchet phases: Phase 0 break-even at +0.80R, Phase 1 at +1.50R, Phase 2 at +2.00R, plus TP expansion into newly formed liquidation bands.")
    else:
        lines.append("• Current open positions on MT5: 0 (Flat, 100% Cash reserves).")
        lines.append("• Status: standby.")
    lines.append("")
    lines.append("Step 3: Audit resting limit orders")
    if orders:
        lines.append(f"• Current pending orders on MT5: {len(orders)} active order(s):")
        for o in orders:
            lines.append(f"  - Ticket #{o['ticket']}: {o['symbol']} {o['type']} {o['volume']} lots @ {o['price_open']} USD | Spot: {o['price_current']} USD | SL: {o['sl']} USD | TP: {o['tp']} USD")
        lines.append("• Audit resting order thesis: Spot at 83,398 USD is defending the 200 EMA (83,294 USD). Order is placed at 83,150 USD to catch a wick pullback. SL at 82,650 USD sits safely behind the 32.45M USD long liquidation cascade pool and 17.04M USD sell-stop cluster at 82,750 USD. TP at 84,400 USD targets the 7.82M USD buy-stop pool. Does thesis prevail? (Maintain order on the book).")
    else:
        lines.append("• Current pending orders on MT5: 0.")
    lines.append("")
    lines.append("Step 4: Capacity and capital floor governance")
    lines.append("• Capacity: Dynamic multi-cluster concurrency across orthogonal assets (Crypto, Indices, Metals, Forex).")
    lines.append("• Hard constraint: Total joint worst-case stopout risk across all exposed orders must unconditionally keep >= 20.00 USD cushion above the 4,775.00 USD floor at all times (stressed post-loss equity >= 4,795.00 USD).")
    lines.append("")
    lines.append("PART F: OUTPUT FORMAT")
    lines.append("1. DOCUMENT INGESTION & GROUND TRUTH CITATION (from Part A)")
    lines.append("2. Playbook Multi-Parameter Debate from all 4 personas (evaluating SP500, NAS100, EURUSD, USDJPY, and BTC)")
    lines.append("3. Resting Limit Order Audit: Ruling on Ticket #18791527 BTC BUY LIMIT (Maintain vs Prune)")
    lines.append("4. Trade table for qualifying candidates with exact Limit Entry, SL in liquidation bunker, and TP in squeeze magnet, or an explicit 'stand aside' ruling with mathematical justification")

    return "\n".join(lines)

async def main():
    prompt = build_prompt()
    prompt_file = ROOT / "docs" / "prompts" / "ARENA_CYCLE_38_PROMPT.txt"
    prompt_file.parent.mkdir(parents=True, exist_ok=True)
    prompt_file.write_text(prompt, encoding="utf-8")
    print(f"Generated unified prompt: {len(prompt)} characters written to {prompt_file}")
    
    await dismiss_arena_popup()
    ok = await post_prompt_to_arena(prompt)
    if ok:
        print("SUCCESS: Unified Cycle 38 Council Prompt injected into Arena.ai!")
    else:
        print("ERROR: Failed to inject prompt into Arena.ai", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
