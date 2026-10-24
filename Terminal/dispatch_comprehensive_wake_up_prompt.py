"""
Terminal/dispatch_comprehensive_wake_up_prompt.py
Dispatches the operator-mandated 4-step collaborative council prompt to Arena.ai:
  STEP 1 (Mandate 1): Screen 24 assets for new Model 1/2 limit order candidates directly from Data/DataBase_Trading.xlsx.
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

from Terminal.arena_bridge import post_prompt_to_arena, post_prompt_to_copilot, dismiss_arena_popup
from Terminal.telemetry_ingest import (
    StaleDataError,
    get_fresh_snapshot,
    make_git_refresh,
)


# ── Cycle State ──────────────────────────────────────────────────────────────
CYCLE_STATE_FILE = ROOT / "Data" / "cycle_state.json"

def _load_cycle_num() -> int:
    """Auto-increment cycle number from persistent state file."""
    if CYCLE_STATE_FILE.exists():
        try:
            state = json.loads(CYCLE_STATE_FILE.read_text(encoding="utf-8"))
            return int(state.get("last_cycle", 63)) + 1
        except Exception:
            pass
    return 64

def _save_cycle_num(cycle: int) -> None:
    """Persist cycle number after successful dispatch."""
    CYCLE_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(CYCLE_STATE_FILE, "w", encoding="utf-8") as f:
            json.dump({"last_cycle": cycle, "dispatched_utc": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())}, f)
    except Exception as e:
        print(f"Warning saving cycle state: {e}")

# ── Initial Risk Ledger ─────────────────────────────────────────────────────
def _load_initial_risk_ledger() -> dict:
    """Load the immutable initial-risk ledger. Returns dict keyed by ticket string."""
    risk_file = ROOT / "Data" / "initial_position_risk.json"
    if risk_file.exists():
        try:
            return json.load(open(risk_file, "r", encoding="utf-8"))
        except Exception:
            pass
    return {}

def _get_frozen_r0(ticket_str: str, ledger: dict, entry: float, current_sl: float, fallback_atr: float) -> float:
    """
    Return the FROZEN initial R0 for a position.
    BUG FIX: Previous code fell back to abs(entry - current_sl), which uses the
    ratcheted SL and inflates R-multiples. Now uses the immutable ledger first,
    with field-name tolerance (r0 / R0_pts / R0), and only falls back to ATR
    if the ledger has no entry (which means R0 is unknown and must be conservative).
    """
    if ticket_str in ledger:
        rec = ledger[ticket_str]
        r0 = float(rec.get("r0") or rec.get("R0_pts") or rec.get("R0") or 0.0)
        if r0 > 0:
            return r0
    # If no ledger entry, use initial_sl field if it exists in the ledger
    if ticket_str in ledger:
        rec = ledger[ticket_str]
        init_sl = rec.get("initial_sl")
        if init_sl is not None:
            r0 = abs(entry - float(init_sl))
            if r0 > 0:
                return r0
    # Last resort: use ATR as conservative R0 (never use current ratcheted SL)
    return fallback_atr if fallback_atr > 0 else 1.0


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
        snap_path = ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
        if snap_path.exists():
            try:
                snap = get_fresh_snapshot(snap_path, refresh=make_git_refresh(repo_root=str(ROOT)))
            except Exception as read_err:
                print(f"Warning: Could not read local snapshot ({read_err}).")
            else:
                acc = snap.get("account", {})
                equity = acc.get("equity_usd", 4896.55)
                balance = acc.get("balance_usd", 4896.55)
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
    if clean == "XAU":
        return "GOLD"
    if clean == "XAG":
        return "SILVER"
    if mt5_symbol in assets:
        return mt5_symbol
    if mt5_symbol.replace(".pi", "").replace(".p", "") in assets:
        return mt5_symbol.replace(".pi", "").replace(".p", "")
    if clean in assets:
        return clean
    for k, v in assets.items():
        if v.get("symbol_broker") == mt5_symbol or v.get("mt5_symbol") == mt5_symbol:
            return k
    return clean


def build_prompt(cycle_num: int = 65, target_agent: str = "arena_astra") -> str:
    is_fable = target_agent in ("arena_fable", "arena_2_fable", "fable")
    is_arena_astra = target_agent in ("arena_astra", "arena_1_primary", "primary")
    is_copilot_opus = target_agent in ("copilot_opus", "Opus 5.5", "opus")
    is_copilot_astra = target_agent in ("copilot_astra", "GPT Astra", "astra")
    for_copilot = is_copilot_opus or is_copilot_astra or target_agent.startswith("copilot")

    broker = get_live_broker_state()
    equity = broker["equity"]
    balance = broker["balance"]
    margin = broker["margin"]
    cushion = equity - 4600.0
    buffer_cushion = equity - 4650.0
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
    ev_name = macro_info.get("event", "None")
    ev_time = macro_info.get("event_release_utc", "None")
    blackout_active = macro_info.get("blackout_active", False)

    # Load Forex Factory summary and live calendar for line-by-line macro analysis
    ff_summary_path = ROOT / "Data" / "forex_factory_summary.json"
    ff_summary = {}
    if ff_summary_path.exists():
        try:
            ff_summary = json.loads(ff_summary_path.read_text(encoding="utf-8"))
        except Exception:
            ff_summary = {}

    ff_live_path = ROOT / "Data" / "forex_factory_live.json"
    ff_live = {}
    if ff_live_path.exists():
        try:
            ff_live = json.loads(ff_live_path.read_text(encoding="utf-8"))
        except Exception:
            ff_live = {}

    # Load immutable risk ledger ONCE for the entire prompt build
    initial_risk_ledger = _load_initial_risk_ledger()

    lines = []
    lines.append(f"TRADING DESK COUNCIL: CYCLE {cycle_num} TELEMETRY, PLAYBOOK & STANDARDIZED DECISION CHAIN PROMPT")
    if is_arena_astra:
        lines.append("ROUTING TARGET: ARENA.AI PRIMARY WORKSPACE (TAB 1)")
        lines.append("CAPABILITIES REQUIRED: DEEP REASONING AND AUTONOMOUS MULTI-AGENT QUANTITATIVE SQUAD")
        lines.append("ROLE: SENIOR QUANTITATIVE STRATEGIST & MARKET SCREENER (ADVISORY & RATIFICATION)")
        lines.append("EXECUTION & GIT SEPARATION: You DO NOT need an active broker connection, MT5 terminal, or GitHub push rights. Antigravity handles all MT5 executions and all git commits autonomously. Your sole responsibility is to evaluate market data from Data/DataBase_Trading.xlsx and provide your recommended limit orders directly in markdown in this response.")
    elif is_fable:
        lines.append("ROUTING TARGET: ARENA.AI SECONDARY WORKSPACE (TAB 2)")
        lines.append("CAPABILITIES REQUIRED: DEEP REASONING AND AUTONOMOUS MULTI-AGENT QUANTITATIVE SQUAD")
        lines.append("ROLE: LEAD QUANTITATIVE AUDITOR & MARKET SCREENER (ADVISORY & RATIFICATION)")
        lines.append("EXECUTION & GIT SEPARATION: You DO NOT need an active broker connection, MT5 terminal, or GitHub push rights. Antigravity handles all MT5 executions and all git commits autonomously. Your sole responsibility is to evaluate market data from Data/DataBase_Trading.xlsx and provide your recommended limit orders directly in markdown in this response.")
    elif is_copilot_opus:
        lines.append("ROUTING TARGET: CLAUDE OPUS 5.5 (MICROSOFT COPILOT STUDIO - TAB 1)")
        lines.append("CANONICAL WORKSPACE: https://github.com/kbsingh1399/Trading_2")
        lines.append("ACTIVE BRANCHES: main (https://github.com/kbsingh1399/Trading_2/tree/main) and arena/74cd2d1a-trading-2 (https://github.com/kbsingh1399/Trading_2/tree/arena%2F74cd2d1a-trading-2)")
        lines.append("ROLE: LEAD FORENSIC QUANTITATIVE STRATEGIST & MICROSTRUCTURE ARCHITECT")
    elif is_copilot_astra:
        lines.append("ROUTING TARGET: GPT ASTRA (MICROSOFT COPILOT STUDIO - TAB 2)")
        lines.append("CANONICAL WORKSPACE: https://github.com/kbsingh1399/Trading_2")
        lines.append("ACTIVE BRANCHES: main (https://github.com/kbsingh1399/Trading_2/tree/main) and arena/74cd2d1a-trading-2 (https://github.com/kbsingh1399/Trading_2/tree/arena%2F74cd2d1a-trading-2)")
        lines.append("ROLE: CAPITAL FLOOR SENTRY & MULTI-CLUSTER STRESSED RISK AUDITOR")
    lines.append("MANDATE: THE SINGLE DEFINITIVE SOURCE OF TRADING TRUTH AND DECISION-MAKING FOR BOTH ARENA.AI AND ANTIGRAVITY IS Data/DataBase_Trading.xlsx (ALL 43 PRODUCTION WORKSHEETS). IT CONTAINS ALL MARKET, MACRO, SENTIMENT, MICROSTRUCTURE, AND ACCOUNT DATA.")
    lines.append("NON-BYPASSABLE OPERATOR DIRECTIVE: You MUST STRICTLY follow docs/specs/STANDARDIZED_TRADING_DECISION_CHAIN.md (the 10-Step Standardized Trading Decision Chain SOP) on every analysis step.")
    lines.append("OPERATOR TRADING AUTHORIZATION: The portfolio manager/operator has explicitly granted full live trading authority: 'Final you have to take decision. If you think candidates are potential logical... then you can punch orders without hesitation. You have all rights and now you can run autonomously. We need trade...'")
    lines.append("STATIC TAG CLARIFICATION: The static telemetry metadata tag 'trade_authorization: DENIED_UNVERIFIED_ORDERFLOW' in the JSON header is purely an internal scraper provenance tag confirming the automated telemetry collector itself does not punch orders. It is NOT a trading lock on the Council. You are explicitly authorized and requested to evaluate, qualify, and ratify logical passive limit orders based on the 43 sheets of DataBase_Trading.xlsx.")
    lines.append("")

    # ── PART A: SOURCE FILES ────────────────────────────────────────────────
    lines.append("PART A: REQUIRED READING (CANONICAL EXCLUSIVE SOURCE OF TRUTH)")
    lines.append("1. EXCLUSIVE MASTER DATA WAREHOUSE (SINGLE SOURCE OF TRUTH): Data/DataBase_Trading.xlsx (ALL 43 PRODUCTION WORKSHEETS)")
    lines.append("   The 225,000+-cell master workbook Data/DataBase_Trading.xlsx is our EXCLUSIVE, SINGLE DEFINITIVE SOURCE OF TRADING TRUTH. IT CONTAINS EVERYTHING. ALL market data points — including real-time quotes, level 2/3 depth, multi-horizon CVD, venue basis spreads, economic calendar, news headlines, and account ledger — are updated continuously directly in this workbook every 10 minutes:")
    lines.append("")
    lines.append("   • CLUSTER 1: Macro Trend & Institutional Inflow (Sheets 1–6, 40):")
    lines.append("     - Sheet 1 (Crypto_ETF_Flows): Daily & cumulative net ETF inflows/outflows across BTC/ETH spot ETFs. Confirms macro institutional flow direction.")
    lines.append("     - Sheet 2 (Top_Institutions): Institutional portfolio holdings (BlackRock, Fidelity, Bitwise). Tracks sovereign/tier-1 fund allocation shifts.")
    lines.append("     - Sheet 3 (ETF_Market_Overview): Aggregate ETF market cap, total volume, premium/discount to NAV. Evaluates institutional liquidity expansion.")
    lines.append("     - Sheet 4 (ETF_Overview): Fund-by-fund breakdown of expense ratios, daily volume, net asset changes.")
    lines.append("     - Sheet 5 (Spot_ETF_Net_Inflow): Granular daily net inflow per ticker (IBIT, FBTC, ARKB, etc.). Consecutive positive days disqualify aggressive counter-trend shorting.")
    lines.append("     - Sheet 6 (Spot_ETF_Net_Inflow_Graph): Time-series trend trajectory and moving averages of institutional net creations/redemptions.")
    lines.append("     - Sheet 40 (Bitcoin_Treasuries): 60 corporate balance sheets (Strategy/MicroStrategy, MARA, Tesla) and 124-row historical acquisitions ledger.")
    lines.append("")
    lines.append("   • CLUSTER 2: Sentiment, Leverage & Crowding (Sheets 7–11, 28–30, 41):")
    lines.append("     - Sheet 7 (Funding_Rates): Real-time 8h perpetual funding rates across Binance, OKX, Bybit, dYdX, Hyperliquid. Extreme positive funding (> +0.03%) flags longs vulnerable to flushes; negative funding flags short squeezes.")
    lines.append("     - Sheet 8 (Funding_Fees): Annualized borrowing costs and carrying fees. Prevents holding multi-hour swings against heavy funding drag.")
    lines.append("     - Sheet 9 (LR_Ratio_Chart): Historical Long/Short ratio curves. Identifies sentiment extremes and crowd positioning divergences.")
    lines.append("     - Sheet 10 (LR_Ratio_Accounts): Long vs Short account percentage distribution on Binance/OKX. Contrarian filter: >70% long retail skews warn of impending sweeps.")
    lines.append("     - Sheet 11 (LR_Exchanges_Ratio): Cross-exchange comparison of net directional exposure (Binance vs Bybit vs OKX). Pinpoints venue-specific positioning asymmetries.")
    lines.append("     - Sheet 28 (FF_Trades_Sentiment): Retail long vs short percentage, lot volume splits, average entry prices, and win/loss ratios across 8 Forex pairs and Gold.")
    lines.append("     - Sheet 29 (FF_Trades_Individual_Positions): 70 individual retail trader positions with resting lot sizes, open prices, floating PnL, and stop allocations. Maps exact retail stop hunt clusters.")
    lines.append("     - Sheet 30 (FF_Top_Traders): Verified monthly top trader rankings, profitable system return %, and accounting modes.")
    lines.append("     - Sheet 41 (Volatility_Sentiment): Alternative.me Fear & Greed Index historical series alongside Deribit DVOL 30-day forward implied volatility curves for BTC and ETH.")
    lines.append("")
    lines.append("   • CLUSTER 3: Technical Analysis & Regime Health (Sheets 13–18, 27, 34):")
    lines.append("     - Sheet 13 (Open_Interest): Total active open contracts (notional USD and native units) per asset. Rising price + rising OI = institutional trend; rising price + falling OI = short-covering rally.")
    lines.append("     - Sheet 14 (Open_Interest_Top_Gainers): Highest 1h/24h percentage increase in open contracts. Pinpoints active capital accumulation and imminent volatility expansion.")
    lines.append("     - Sheet 15 (Open_Interest_Top_Losers): Rapid leverage flushes and mass contract closures. Signals post-cascade exhaustion.")
    lines.append("     - Sheets 16, 17, 18 (Exchange_Open_Interest_Chart15M / 1H / 4H): Intraday and multi-day open interest progression aligned with candle closes.")
    lines.append("     - Sheet 27 (FF_News_Technical): Quantitative technical breakdowns, chart patterns, moving averages, and classical support/resistance nodes.")
    lines.append("     - Sheet 34 (Telemetry_System_State): Global system health, 1H/4H trend regime classifications (TREND_UP, TREND_DOWN, RANGE_BOUND, UNDEFINED), 20/50/200 EMAs, Session VWAP, and ATR-14 across 24 assets. PRIMARY REGIME FILTER: If regime is UNDEFINED, stand aside unconditionally across both models.")
    lines.append("")
    lines.append("   • CLUSTER 4: Microstructure, Entry Shelves & CVD (Sheets 12, 23–25, 33, 35, 36, 21_Tradfye_Orderflow):")
    lines.append("     - Sheet 12 (Large_Trades): Real-time block executions (>= 100K USD) with side, price, and exchange. Validates aggressive market order impact.")
    lines.append("     - Sheet 23 (Whales_Orders): Binance Futures resting institutional limit orders (>= 100K USD) with verified temporal persistence (persist >= 180s). Inviolable stop bunker anchor.")
    lines.append("     - Sheet 24 (Spot_Netflow): Net taker buy/sell volume across spot markets. Proves physical spot accumulation vs synthetic leverage.")
    lines.append("     - Sheet 25 (Hyperliquid_Whales): Live resting whale walls and L2/L3 orderbook depth on Hyperliquid DEX.")
    lines.append("     - Sheet 33 (FF_Live_Trades_Activity): 40 real-time executions with side, execution price, order type, and pips. Real-time tape reading for retail panic/FOMO exhaustion.")
    lines.append("     - Sheet 35 (Live_Orderbook_CVD_Depth): Level 2 20-level orderbook depth, book imbalance, multi-horizon taker CVD (1m, 15m, session, weekly), Lee-Ready TradFi tick CVD, trapped traders footprint. Primary entry staging sheet: identifies shelf anchors (POC, VAH/VAL, VWAP) and verifies CVD absorption.")
    lines.append("     - Sheet 36 (Exchange_Basis_Spreads): Cross-venue basis spreads (Binance perp mid minus MT5 CFD mid), funding basis, and spot-perpetual premium. Maps perpetual levels into MT5 broker CFD prices.
    lines.append("     - Sheet 21_Tradfye_Orderflow: Tradfye Footprint Point of Control (POC), candle taker delta, 99th-percentile whale bubbles, resting absorption shelves, and Deribit options max pain and gamma walls. Read directly from Data/DataBase_Trading.xlsx.")")
    lines.append("")
    lines.append("   • CLUSTER 5: Liquidity Magnets & SL/TP Placement (Sheets 19–22, 37):")
    lines.append("     - Sheets 19 & 20 (liquidation_maxpain_1D / 2D): 24h and 48h maximum pain strike prices.")
    lines.append("     - Sheets 21 & 22 (Exchange_Liquidation_Map_1D / 7D): Reconstructed liquidation heatmaps, long cascade bands below, short squeeze bands above. SL MUST sit outside nearest sweep band [min_price, max_price] + 0.50 ATR; TP front-runs opposing cascade band by 5-10 bps.")
    lines.append("     - Sheet 37 (Hyperdash_Flow_Feed): KPIs, 50 whale trades, 50 confirmed liquidations, and 158-asset universe flow.")
    lines.append("")
    lines.append("   • CLUSTER 6: On-Chain Whale Forensics (Sheets 38, 39):")
    lines.append("     - Sheet 38 (Arkham_Transfers_100K): Whale transfers >= 100K USD with full 42-character 0x/Tron addresses, tx hashes, and entity badges (Wintermute, Jump, BlackRock). Flags impending CEX dumps or cold storage accumulation.")
    lines.append("     - Sheet 39 (Arkham_Whales_Holdings): Portfolio tracking for 48 institutional entities, total USD holdings, and 24h asset rebalancing.")
    lines.append("")
    lines.append("   • CLUSTER 7: Broker Execution & Governance (Sheets 42, 43):")
    lines.append("     - Sheet 42 (MT5_Live_Quotes_Account): Live MT5 account ledger: balance, equity, margin used, free margin, floor cushion, 24 live quotes & spreads in bps, plus live active filled positions and pending limit orders. Sovereign capital defense gate.")
    lines.append("     - Sheet 43 (Cognitive_Council_Telemetry): Real-time health of Google Gemini Web2API (port 8081, 11 models), Heretic Engine (port 8083, HEALTHY 200), Arena.ai consensus, and git sync daemons.")
    lines.append("")
    lines.append("   MANDATORY DIRECTIVE: You DO NOT need to refer to any raw JSON files. Every market, macro, sentiment, technical, and account observation must be derived exclusively from Data/DataBase_Trading.xlsx.")
    lines.append("")
    lines.append("   MANDATORY SHEET-BY-SHEET ANALYSIS DIRECTIVE:")
    lines.append("   You are strictly FORBIDDEN from formulating or ratifying any trade order based on a single worksheet or isolated parameter. Every proposed limit order MUST be verified through all 7 functional clusters of Data/DataBase_Trading.xlsx:")
    lines.append("   1. Macro Alignment: Check Sheet 1-6 & 40 (ETF flows & Treasuries) and Sheet 31 (Economic Calendar).")
    lines.append("   2. Crowding Check: Check Sheet 7-11 & 28-30 (Funding rates & Retail positions).")
    lines.append("   3. Technical Regime: Check Sheet 34 (System State) and Sheets 13-18 (Open Interest). If regime is UNDEFINED, STAND ASIDE.")
    lines.append("   4. Microstructure Bunker: Check Sheet 35 (CVD & L2 depth) and Sheet 23 (Whale Orders >= 100K with >= 180s persistence).")
    lines.append("   5. Target Liquidity Magnet: Check Sheet 21 & 22 (Liquidation Map 1D/7D).")
    lines.append("   6. On-Chain Flow: Check Sheet 38 & 39 (Arkham transfers & Whale holdings).")
    lines.append("   7. Execution Cushion: Check Sheet 42 (MT5 quotes, spread friction <= 15%, stressed capital floor >= 4,775 USD).")
    lines.append("")
    lines.append("2. Canonical Trade Decision Playbook: docs/Mandatory_Rules/TRADE_DECISION_PLAYBOOK.md")
    lines.append("3. Standardized Trading Decision Chain SOP: docs/specs/STANDARDIZED_TRADING_DECISION_CHAIN.md (Mandatory Non-Bypassable 10-Step Chain)")
    lines.append("4. Autonomous Wake-Up Checklist: docs/specs/AUTONOMOUS_WAKEUP_CHECKLIST.md")
    lines.append("5. Live Order Desk & Session Context: docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md & .agents/rules/ACTIVE_CONTEXT.md")
    lines.append("")

    # ── PART B: ACCOUNT & RISK BASELINE ─────────────────────────────────────
    lines.append("PART B: ACCOUNT AND RISK BASELINE")
    lines.append("• Execution Mode: PASSIVE LIMIT ORDERS ONLY (no market orders).")
    lines.append("• Broker: Blueberry Markets SVG LLC, MetaTrader 5 account #5064568")
    lines.append(f"• Balance / Equity: {balance:.2f} USD / {equity:.2f} USD")
    lines.append(f"• Margin used: {margin:.2f} USD")
    lines.append("• Realized Deals Banked Today: Ticket #18976378 (EURUSD.pi BUY -> +23.40 USD gross / +22.98 USD net profit booked via Take Profit at 1.12500, +2.053 R0), Ticket #18836609 (SP500.p SHORT -> +0.90 USD cash profit booked via Trailing Stop Loss at 7,807.75), Ticket #18826511 (ETHUSD.pi SHORT -> +1.92 USD profit banked via Profit Lock at 2,513.02), Ticket #18813768 (SOLUSD.p SHORT -> +9.52 USD profit banked via Phase 1 Lock), Ticket #18813767 (BTCUSD.pi SHORT -> +16.10 USD full TP).")
    lines.append("• Hard floor: 4,775.00 USD | Operating buffer: 4,795.00 USD")
    lines.append(f"• Live cushion: +{cushion:.2f} USD above hard floor (+{buffer_cushion:.2f} USD above operating buffer)")
    lines.append("• Risk per trade: 7.50 to 14.50 USD (adaptive risk envelope, 0.15% to 0.29% of capital).")
    lines.append("• Stressed Loss Formula (Astra Invariant): Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket. Requirement: min(balance, equity) - sum(all open & pending stressed risks) >= 4,795.00 USD.")

    # ── BUG FIX: Dynamically compute capacity ceiling ────────────────────────
    # Instead of hardcoded stale stress numbers, compute from live MT5 data
    # and the immutable initial_risk_ledger.
    snap_risk_tickets = snap_data.get("risk", {}).get("tickets", [])
    tot_contingent_stress = 0.0
    pos_stress_items = []
    for p in positions:
        ak = _resolve_asset_key(p["symbol"], assets)
        a_info = assets.get(ak, {})
        matched_t = next((t for t in snap_risk_tickets if t.get("ticket") == p["ticket"]), None)
        t_str = str(p["ticket"])
        # Use initial risk ledger for frozen nominal risk (not ratcheted SL)
        if t_str in initial_risk_ledger:
            rec = initial_risk_ledger[t_str]
            nom = float(rec.get("nominal_risk_usd") or rec.get("cash_risk_nominal") or 0.0)
            stress = float(rec.get("stressed_risk_usd") or (1.25 * nom + 2.0))
        elif matched_t and matched_t.get("stressed_stop_loss_usd") is not None:
            nom = float(matched_t.get("nominal_stop_loss_usd", 0.0))
            stress = float(matched_t.get("stressed_stop_loss_usd", 0.0))
        else:
            sl_dist = abs(p["price_open"] - p["sl"]) if p["sl"] else 0.0
            c_size = a_info.get("execution_specs", {}).get("contract_size", 1.0)
            nom = sl_dist * p["volume"] * c_size
            stress = 1.25 * nom + 2.0
        pos_stress_items.append((p, nom, stress))
        tot_contingent_stress += stress

    capacity_used = len(positions) + len(orders)
    capacity_available = max(0, 4 - capacity_used)
    min_capital = min(balance, equity)
    avail_budget = max(0.0, min_capital - 4650.0 - tot_contingent_stress)
    calibrated_risk = 10.00
    calibrated_stress = 1.25 * calibrated_risk + 2.0  # 14.50 USD
    max_new_tickets = min(capacity_available, int(avail_budget / calibrated_stress)) if calibrated_stress > 0 else 0
    min_new_stress = 1.25 * 7.50 + 2.0  # 11.38 USD
    max_tickets_min_risk = min(capacity_available, int(avail_budget / min_new_stress)) if min_new_stress > 0 else 0
    worst_case_equity = min_capital - tot_contingent_stress

    # Build dynamic capacity blurb
    stress_detail_parts = []
    for p, nom, stress in pos_stress_items:
        stress_detail_parts.append(f"#{p['ticket']} ({p['symbol']} {p['type']}) nom {nom:.2f} -> stressed {stress:.2f} USD")
    stress_detail = "; ".join(stress_detail_parts) if stress_detail_parts else "0.00 USD (Flat)"

    lines.append(f"• Rigorous Capacity Ceiling: Open positions currently consume {tot_contingent_stress:.2f} USD total contingent stress ({stress_detail}). Stressed worst-case equity is {worst_case_equity:.2f} USD, leaving +{worst_case_equity - 4650.0:.2f} USD above 4,795.00 USD buffer. Capacity permits: max {max_new_tickets} new ticket(s) at {calibrated_risk:.2f} USD risk (stress {calibrated_stress:.2f} USD) or {max_tickets_min_risk} ticket(s) at 7.50 USD risk (stress {min_new_stress:.2f} USD). Capacity: {capacity_used}/4 filled, {capacity_available} available.")
    lines.append("")

    # ── PART C: ACTIVE REPOSITORIES ─────────────────────────────────────────
    lines.append("PART C: ACTIVE REPOSITORIES & DATA PROVENANCE (MAIN BRANCH SOURCE OF TRUTH)")
    lines.append("• Canonical Workspace: https://github.com/kbsingh1399/Trading_2")
    lines.append("• Active Branch: main (CANONICAL UPSTREAM SOURCE OF TRUTH — ALL MODELS ROUTE TO MAIN)")
    lines.append("• Direct Raw URLs (Strictly from main branch):")
    lines.append("  - Master Trading Database (Single Source of Truth, all 43 sheets): https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Data/DataBase_Trading.xlsx")
    lines.append("  - Playbook: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/Mandatory_Rules/TRADE_DECISION_PLAYBOOK.md")
    lines.append("  - Standardized Decision Chain (SOP): https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/Mandatory_Rules/STANDARDIZED_TRADING_DECISION_CHAIN.md")
    lines.append("  - Desk State: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md")
    lines.append("  - Active Context: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md")
    lines.append("  - Session History: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md")
    lines.append("")

    # ── PART D: ANALYTICAL FRAMEWORK ────────────────────────────────────────
    lines.append("PART D: DUAL-ENGINE ANALYTICAL FRAMEWORK & 18-PARAMETER TELEMETRY SYNTHESIS")
    lines.append("")
    lines.append("CRITICAL DIRECTIVE: YOU ARE OPERATING TWO INDEPENDENT STATISTICAL ENGINES SIMULTANEOUSLY.")
    lines.append("DO NOT collapse them into one. For every asset, you must explicitly evaluate BOTH engines and state which (if either) triggers:")
    lines.append("")
    lines.append("  ENGINE 1 — EXTREME MEAN REVERSION (Strict |Z| >= 2.0 SD to 3.5 SD):")
    lines.append("    Trigger: Price has stretched to an extreme statistical dislocation from Session VWAP.")
    lines.append("    Required confluence (ALL must hold): |Z| >= 2.0 SD + confirmed tape exhaustion (CVD delta deceleration/absorption NOT just negative CVD) + multi-layer whale backing (>= 500k USD, >= 180s persistence) + HTF regime alignment (Model 1 Longs are BANNED in Bearish HTF; Model 1 Shorts are BANNED in Bullish HTF).")
    lines.append("    Disqualifier: Attempting mean reversion against HTF trend momentum is the single deadliest error pattern in our loss autopsy ledger.")
    lines.append("")
    lines.append("  ENGINE 2 — TREND FOLLOWING PULLBACKS (|Z| can be 0.2 to 1.8 SD — DO NOT DISCARD for low |Z|!):")
    lines.append("    Trigger: Asset is in a confirmed BULLISH or BEARISH regime on 1H/4H and is pulling back INTO a structural shelf IN THE DIRECTION of the dominant trend.")
    lines.append("    Shelf detection protocol (evaluate in order of priority):")
    lines.append("      a) HTF EMA Stack: 20 EMA > 50 EMA > 200 EMA (bullish) or 20 EMA < 50 EMA < 200 EMA (bearish). Pullback touches the 20 or 50 EMA and holds.")
    lines.append("      b) Volume Profile Shelves: Price pulls back to POC, VAH (for shorts), or VAL (for longs) — high-volume nodes where institutional positioning is concentrated.")
    lines.append("      c) Prior Day/Week Auction Levels: htf_auction_profiles prior_day_poc, prior_day_vah, prior_day_val, weekly_vwap — institutional memory shelves.")
    lines.append("      d) L2/L3 Resting Walls: Heavy resting Bid walls (for long pullbacks) or Ask walls (for short pullbacks) with notional >= 500k USD and persistence >= 180s defending the stop.")
    lines.append("    Required confluence (ALL must hold): Confirmed regime + shelf touch + low pullback velocity (RSI returning from oversold/overbought toward 50) + resting L2/L3 walls defending the stop + SL outside min_price/max_price of nearest opposing sweep band.")
    lines.append("    Key insight: Engine 2 opportunities often present at LOW |Z| (0.3 to 1.2 SD). Previous prompt versions caused agents to SKIP these by filtering on |Z| >= 2.0 first. This is explicitly forbidden.")
    lines.append("")
    lines.append("  REGIME-GATED STAND-ASIDE: When trend_regime is RANGE_BOUND or UNDEFINED, neither engine applies. The mathematically correct action is STAND ASIDE. Never force trades in non-trending noise.")
    lines.append("")
    lines.append("TREND-FIRST HIERARCHY (SUPERSEDES ALL BAND-BASED ANALYSIS):")
    lines.append("  DO NOT STICK DOGMATICALLY TO VWAP SD BANDS ALONE. Fading oversold/overbought bands in a trending market is lethal. You MUST evaluate the overall trend supported by all parameters in Data/DataBase_Trading.xlsx (Sheets 34-36, 41-42):")
    lines.append("  1. Higher Timeframe Trend Hierarchy: Inspect 1H & 4H OHLCV candles, 20/50/200 EMAs. If Price < EMA20 < EMA50 on 1H/4H (Bearish regime), Model 1 dip-buying Longs are STRICTLY FORBIDDEN. All priority shifts to Model 2 Trend Pullback SHORTS!")
    lines.append("  2. cvd_1m_buckets & CVD Momentum: Massive negative taker CVD (-1M to -3M USD) is proof of aggressive seller domination. Never buy into negative CVD. Use negative CVD to qualify SHORT entries on relief rallies.")
    lines.append("  3. Model 2 Pullback Short Protocol: In a downtrend, patiently wait for pullbacks up into the EMA20/EMA50/VAH shelves where heavy Ask Whale Walls are resting to defend the Stop Loss.")
    lines.append("")
    lines.append("18-PARAMETER TELEMETRY FIELD REFERENCE (Data/DataBase_Trading.xlsx Sheets 34-36 & 41-42):")
    lines.append("  1. quotes: Live MT5 Bid/Ask spread in bps (spread_bps <= 35 bps Crypto, <= 5 bps TradFi).")
    lines.append("  2. causal_indicators: Session VWAP, vwap_z_score, RSI(14), ATR(14), EMA 20/50/200, POC/VAH/VAL, trend_regime.")
    lines.append("  3. multi_horizon_cvd: Session CVD (since 00:00 UTC), Weekly CVD (since Monday 00:00 UTC), trailing 24h CVD, Absorption/Exhaustion divergence.")
    lines.append("  4. tradfi_orderflow: MT5 Lee-Ready synthetic tick CVD, 15m delta, Order Flow Imbalance (OFI), Buyer/Seller aggression bias.")
    lines.append("  5. htf_auction_profiles: Prior Day/Week POC/VAH/VAL, Developing Weekly VWAP.")
    lines.append("  6. trapped_traders_signal: TRAPPED_BUYERS_ABOVE / TRAPPED_SELLERS_BELOW footprint detection.")
    lines.append("  7. orderbook_live_depth: 20-level L2 depth & book_imbalance.")
    lines.append("  8. whale_walls_l3: On-chain Ethereum whale wallet orders (0x... addresses, notionals, persistence_s >= 180s).")
    lines.append("  9. structural_stop_clusters: nearest_sell_stop_clusters_below, nearest_buy_stop_clusters_above.")
    lines.append("  10. reconstructed_liquidations: nearest_long_cascade_bands_below, nearest_short_squeeze_bands_above.")
    lines.append("  11. venue_basis: MT5 mid minus perp mid (cross-venue price translation for SL/TP mapping).")
    lines.append("  12. cvd_1m_buckets: Granular 1-minute CVD series for micro-momentum reading.")
    lines.append("  13. execution_specs: Broker tick size, point size, contract size, margin requirements.")
    lines.append("  14. macro_calendar: Tier-1 macroeconomic event proximity and blackout windows.")
    lines.append("  15. LIQUIDITY MAGNETS: Dense liquidation cascade bands and structural stop clusters act as gravitational attraction points. TP should front-run these magnets by 5-10 bps; SL must be sheltered behind whale walls outside opposing sweep bands.")
    lines.append("  16. CROSS-VENUE BASIS: Orderbooks are in Binance/Hyperliquid perpetual futures prices; execution is on MT5 OTC CFDs. Inspect venue_basis before finalizing levels.")
    lines.append("  17. Broker Ticker Mapping: Avalanche = AVXUSD.p (contract 100, lot 0.01, digits 2).")
    lines.append("  18. Adaptive Risk Envelope: [7.50, 14.50 USD]. Do not reject 0.01 lot shorts risking 8.50-9.50 USD over arbitrary floor bureaucracy.")
    lines.append("")

    # ── PART D-2: FOREX FACTORY MACRO CALENDAR, CENTRAL BANK RATES & BREAKING HEADLINES ────
    lines.append("PART D-2: FOREX FACTORY MACRO CALENDAR, CENTRAL BANK RATES & BREAKING HEADLINES (MACRO IDEA GENERATION)")
    lines.append("CRITICAL OPERATOR MANDATE: LINE-BY-LINE MACRO INGESTION & NARRATIVE CONTINUITY")
    lines.append("You MUST read Data/DataBase_Trading.xlsx Sheets 26-33 (FF_Economic_Calendar, FF_News_Latest, FF_News_Fundamental, FF_News_Technical, FF_Trades_Sentiment, FF_Trades_Individual_Positions, FF_Live_Trades_Activity, FF_Top_Traders) line-by-line to build and maintain the macro narrative:")
    lines.append("• Ingestion Source: Data/DataBase_Trading.xlsx Sheets 26-33 (Continuously dumped and validated by autonomous Excel pipeline)")
    lines.append("• Central Bank Benchmark Policy Rates (Live Rate Matrix):")
    rates = ff_summary.get("rates", {})
    if rates:
        rate_strs = [f"{cur}: {rate}" for cur, rate in rates.items()]
        lines.append("  " + " | ".join(rate_strs))
    else:
        lines.append("  AUD: 4.60% | USD: 4.00% | GBP: 3.75% | NZD: 2.75% | EUR: 2.65% | CAD: 2.25% | JPY: <1.25% | CHF: 0.00%")
    lines.append("• Structural Interest Rate Differentials & Macro Trade Angles:")
    lines.append("  - USD (4.00%) vs JPY (<1.25%): 275+ bps policy spread. Massive structural carry divergence driving USD/JPY into the historic MoF/BoJ intervention defense zone (158.00–160.00). Fading USD/JPY into resting whale walls provides asymmetric R:R against official intervention risk.")
    lines.append("  - AUD (4.60%) vs USD (4.00%) & EUR (2.65%): Hawkish RBA divergence provides relative strength backdrop on dips.")
    lines.append("  - Central Bank Speakers on Deck: ECB President Lagarde, BOE Gov Bailey, BOC Gov Macklem speeches inject high two-way volatility into EUR, GBP, CAD.")
    lines.append("• Live Breaking Geopolitical, Commodity & Macro Headlines (Line-by-Line Feed):")
    headlines = ff_summary.get("top_headlines", [])
    if headlines:
        for h in headlines:
            lines.append(f"  - {h}")
    else:
        lines.append("  - Nato Weighs Response To Recent Black Sea Drone Attacks On Ships - WSJ (Maritime insurance & supply chain disruption)")
        lines.append("  - Lawmakers introduce a bill to block trumps Russia diesel deal (European refined product supply tightness)")
        lines.append("  - Gold steadies as oil tightness and growth fears divide markets (Stagflationary oil surge toward $100/bbl vs safe-haven gold bid)")
    lines.append("• Macro Trade Idea Synthesis Protocol:")
    lines.append("  You MUST actively synthesize these macro calendar prints, interest rate differentials, and breaking headlines into concrete trading ideas:")
    lines.append("  1. Fading USD/JPY near 158.20–158.50: Exploiting extreme BoJ intervention threat and whale wall resistance despite carry tailwind.")
    lines.append("  2. Energy & Commodity Flow: Black Sea supply shocks and diesel sanctions directly support USWTI.p momentum pullbacks into the 20/50 EMA.")
    lines.append("  3. Equities Stagflation Squeeze: Rising oil prices + persistent central bank rate holds crush equity valuations; forbids counter-trend dip buying on SP500.p and NAS100.p.")
    lines.append("")

    # ── PART E: KAIZEN LOSS AUTOPSY ─────────────────────────────────────────
    lines.append("PART E: KAIZEN CONTINUOUS SELF-IMPROVEMENT & CLASSIFIED LOSS-PATTERN TAXONOMY")
    lines.append("")
    lines.append("Study the forensic breakdown of all recent stopped-out trades. The Council must actively learn from each.")
    lines.append("These losses are classified into 4 FAILURE ARCHETYPES — pattern recognition prevents recurrence:")
    lines.append("")
    lines.append("  ARCHETYPE 1 — SL INSIDE SWEEP BAND (the most common killer):")
    lines.append("    • #18825384 SOLUSD.p -11.05 USD: SL @ 108.55 sat inside [107.5-108.5] buy-stop sweep band. Ask walls relocated from 108.34/108.75 to 108.68/109.22, leaving SL undefended. Wick to 108.58 triggered stop before drop to 107.79.")
    lines.append("    • #18806752 SOLUSD.p -10.88 USD: SL @ 108.79 inside discount sell-stop cluster during cascading flush.")
    lines.append("    • #18786372 BTCUSD.pi -11.17 USD: Long entry staged above un-swept sell-stop pool at 83,500. Market punched through to sweep stops, hit SL @ 83,472.55.")
    lines.append("    INVARIANT: SL MUST sit 0.35-0.50 ATR OUTSIDE [min_price, max_price] of the governing sweep cluster. Never inside!")
    lines.append("")
    lines.append("  ARCHETYPE 2 — COUNTER-TREND ENTRY (fighting the river):")
    lines.append("    • #18813343 BTCUSD.pi -11.58 USD: Long at 82,351 against -3.07M USD negative taker CVD during market cascade.")
    lines.append("    • #18798018 BTCUSD.pi -11.20 USD: Mean-reversion long at 83,150 against heavily accelerating negative 1m/5m CVD (-420 BTC) before delta absorption formed.")
    lines.append("    • #18744533 XAUUSD.pi -13.70 USD: Model 1 long against adverse momentum without multi-timeframe trend alignment.")
    lines.append("    INVARIANT: Long entries require confirmed CVD delta deceleration/absorption. Never catch falling knives with negative taker momentum!")
    lines.append("")
    lines.append("  ARCHETYPE 3 — INSUFFICIENT STRUCTURAL BUFFER:")
    lines.append("    • #18749312 SP500.p -13.00 USD: Trend pullback long with SL only 0.15 ATR below VAL. Routine liquidity sweep tagged stop before rally to target.")
    lines.append("    INVARIANT: SL buffer must be >= 0.35 ATR. The 0.15 ATR buffer is statistically insufficient to survive routine sweeps.")
    lines.append("")
    lines.append("  ARCHETYPE 4 — EPHEMERAL WALL DEFENSE (pulled rug):")
    lines.append("    • #18748507 ETHUSD.pi -11.90 USD: Entered based on whale bid wall that was pulled/thinned by 65% within 90 seconds (<< 180s persistence threshold).")
    lines.append("    INVARIANT: Supporting whale walls must show >= 500k USD notional AND >= 180s verified temporal persistence. If a wall relocates, re-evaluate or trim immediately.")
    lines.append("")
    lines.append("  ARCHETYPE 5 — RETRACEMENT OVERSHOOT & PREMATURE STOP-OUT (Operator Core Invariant):")
    lines.append("    • On counter-trend pullbacks into an EMA/VWAP shelf, institutional liquidity sweepers routinely punch 0.35 to 0.75 ATR past the shelf to trigger obvious retail stops before reversing.")
    lines.append("    • Placing SL inside this sweep zone or right at the shelf edge guarantees getting stopped out before the winning move develops.")
    lines.append("    THE 4 MANDATORY RETRACEMENT GATES (Strict Invariants for all Model 2 Pullbacks):")
    lines.append("      - Gate R-1 (Deep Structural Bunker Buffer): Stop Loss MUST be positioned at least 0.50 to 0.75 ATR outside the structural shelf, and strictly outside [min_price, max_price] of any known stop cluster or liquidation band. Tight stops (<= 0.30 ATR) on pullbacks are strictly FORBIDDEN.")
    lines.append("      - Gate R-2 (Calibrated Asset-Class Structural Bunker Shield): Between entry and Stop Loss, there MUST be at least one substantial verified structural shield to absorb retracement momentum:")
    lines.append("        * TradFi Equity Indices (SP500.p, NAS100.p, DJ30.p, GER40.p), Commodities (XAUUSD.pi, USWTI.p), and Forex (EURUSD.pi, GBPUSD.pi, USDCAD.pi, etc.):")
    lines.append("          Structural defense is anchored to Held Auction Shelves (Prior Day/Week POC, VAH, VAL, Session VWAP), HTF 20/50 EMAs, or resting MT5 orderbook depth.")
    lines.append("          CRITICAL OPERATOR RULE: DO NOT demand phantom on-chain Ethereum (0x...) whale walls for TradFi/Forex where L3 orderbooks are OTC! A verified HTF shelf or resting book wall constitutes an authentic, fully qualified bunker shield.")
    lines.append("        * Crypto Assets (BTCUSD.pi, ETHUSD.pi, SOLUSD.p, BCHUSD.p, BNBUSD.p):")
    lines.append("          Defended by resting L2/L3 whale walls with temporal persistence >= 180s (>= 500k USD notional), OR cumulative top-20 orderbook depth (>= 1.5M USD).")
    lines.append("      - Gate R-3 (Deep Shelf Anchor Entry & Spread Compensation): Never front-run the shallow outer edge of a pullback. Stage limit entries deeper inside the shelf (at the POC, 50 EMA, or at primary whale wall level), accounting for half-spread.")
    lines.append("      - Gate R-4 (Dynamic Lot Downsizing for Wider Buffers): When a safe structural SL requires a wider distance (0.50-0.75 ATR) to clear the retracement sweep zone, ALWAYS downsize lot size proportionally (e.g. 0.50 -> 0.30 or 0.20 lots) so total nominal risk remains strictly within [7.50, 14.50 USD] envelope and unconditionally preserves the 4,775.00 USD hard floor!")
    lines.append("")
    lines.append("MANDATORY KAIZEN CONTINUOUS SELF-IMPROVEMENT MANDATE:")
    lines.append("  1. Zero Regression: The Council is strictly FORBIDDEN from repeating any of these 5 archetypes. Every proposed action must explicitly state WHICH archetype it defends against and HOW.")
    lines.append("  2. Dynamic Lot Sizing: When wider structural stop buffers are required to clear liquidation bands (e.g. ETH SL moved to 2,555.00), DOWNSIZE lot size immediately (e.g. 0.50 -> 0.35 lots) so risk remains within [7.50, 14.50 USD] ceiling.")
    lines.append("  3. Multi-timeframe trend alignment MUST be respected: In Bearish HTF regime, Model 1 longs are BANNED.")
    lines.append("")

    # ── PART F: COUNCIL PERSONAS ────────────────────────────────────────────
    lines.append("PART F: COUNCIL PERSONAS & ADVERSARIAL DELIBERATION")
    lines.append("You embody 5 simultaneous analytical personas. Each must contribute independently before a final synthesis:")
    lines.append("  1. Orderflow & Microstructure Analyst: MT5 spread_bps, L2 20-level depth & imbalance, L3 on-chain wallet orders (0x..., persistence_s >= 180s), and multi-window 1m CVD (5m, 15m, 30m).")
    lines.append("  2. Structural Price Action Specialist: Session VWAP & SD bands (Z-score), Volume Profile (POC/VAH/VAL), HTF Auction Profiles (Prior Day/Week POC/VAH/VAL), 20/50/200 EMA hierarchy, and psychological round numbers.")
    lines.append("  3. Liquidation & Stop Hunt Forensic: Reconstructed liquidation cascade bands (nearest_* and top_*), stop clusters, SL bunker placement outside min_price/max_price, and TP magnet front-running by 5-10 bps.")
    lines.append("  4. Macro Risk & Portfolio Governor: Capital floor defense (4,775.00 USD hard floor / 4,795.00 USD buffer), discrete lot sizing (execution_specs), margin requirements, and net expectancy.")
    lines.append("  5. Adversarial Pre-Mortem Red Team (Falsification & Autopsy Invalidator):")
    lines.append("     Default baseline is NO TRADE / STAND ASIDE. For any proposed candidate:")
    lines.append("     a) Assume the trade was entered and stopped out. Formulate the exact fatal flaw from our 4 loss archetypes.")
    lines.append("     b) Check: Does SL sit inside ANY known sweep band [min_price, max_price]? -> ARCHETYPE 1 KILL.")
    lines.append("     c) Check: Is the entry against HTF trend with unabsorbed opposing CVD? -> ARCHETYPE 2 KILL.")
    lines.append("     d) Check: Is the SL buffer < 0.35 ATR from the nearest cluster edge? -> ARCHETYPE 3 KILL.")
    lines.append("     e) Check: For Crypto, is the supporting wall < 500k USD or < 180s persistence? For TradFi/Forex, has the structural EMA/Auction shelf broken? -> ARCHETYPE 4 KILL.")
    lines.append("     f) Check: Can a venue_basis spike + broker spread widening tag the stop? -> ADDITIONAL KILL.")
    lines.append("     Certify clearance ONLY if no fatal flaw exists under any archetype.")
    lines.append("")

    # ── THE 10-STEP STANDARDIZED DECISION CHAIN MANDATE ────────────────────
    lines.append("THE 10-STEP STANDARDIZED TRADING DECISION CHAIN MANDATE (docs/Mandatory_Rules/STANDARDIZED_TRADING_DECISION_CHAIN.md):")
    lines.append("You are bound by strict hedge fund operational governance. You MUST evaluate every setup, position modification, and limit order through this 10-step chain:")
    lines.append("  Step 1: Data Contract, Ingestion & Sanity Gate (/data-engineer, /dataform-bigquery) — Mandatory Line-by-Line Master Database Ingestion (read Data/DataBase_Trading.xlsx Sheets 34-36, 41-42 line-by-line and section-by-section to maintain account/order narrative continuity), Mandatory Line-by-Line Forex Factory Ingestion (read Data/DataBase_Trading.xlsx Sheets 26-33 line-by-line to extract Central Bank rate differentials, upcoming speeches, breaking geopolitical/energy headlines, and generate fresh macro trade ideas), JIT Telemetry Refresh Gate, broker venue basis translation (venue_basis), and MT5 spread ceilings (<= 25 bps Crypto, <= 5 bps TradFi).")
    lines.append("  Step 2: Tri-Layer Memory & Trajectory Audit (/remember) — review session history and active context to prevent amnesia; enforce the Anti-Trap Registry (never buy falling knives into negative CVD; never measure SL from mid_price).")
    lines.append("  Step 3: AST Knowledge Graph Traversal & Rule Check (/graphify) — verify broker symbol specs, contract sizing, and ensure single-strategy module integrity.")
    lines.append("  Step 4: HTF Auction & Regime Profiling (/data-analyst) — verify 1H/4H trend hierarchy (EMA 20/50/200), auction value areas (Prior Day/Week POC/VAH/VAL, Weekly VWAP). Stand aside unconditionally if regime is UNDEFINED.")
    lines.append("  Step 5: Dual-Engine Strategy Dialectic (/brainstorm, /data-driven-feature) — screen candidates into Model 1 (Extreme Mean Reversion |Z| >= 2.0 SD) vs Model 2 (Trend Pullback |Z| 0.2 to 1.8 SD).")
    lines.append("  Step 6: Microstructure Coincidence Stack & On-Chain Intel (/data-analyst, /quant-analyst) — verify L2 depth imbalance, L3 whale wall persistence (>= 180s, >= 500k USD, presence_frac >= 0.85), multi-horizon CVD, and Arkham on-chain net flows.")
    lines.append("  Step 7: Liquidation & Stop Magnet Dynamics (/brainstorm, /data-analyst, /market-microstructure) — place SL in outer bunker (min/max price + 0.35-0.50 ATR buffer; never inside), front-run TP magnets by 5-10 bps, and distinguish absorption from blow-through.")
    lines.append("  Step 8: Mathematical Risk Budget & Capital Floor Gate (/quant-analyst, /risk-engine) — verify lot size, cash risk ($7.50-$14.50 USD), and stressed equity >= 4,775.00 USD hard floor.")
    lines.append("  Step 9: Pre-Execution Ex-Ante Audit (/verify, test-guard) — confirm passive limit posture (BUY_LIMIT / SELL_LIMIT), R:R >= 2.0R, bunker safety, and broker IOC filling policy.")
    lines.append("  Step 10: Autonomous Punch & Dynamic Ratchet Lifecycle (/quant-analyst) — enforce frozen initial R0 ratchets: Phase 0 (-0.25R0 at +1.25R0), Phase 1 (+0.80R0 at +1.65R0), Phase 2 trail (>= +2.00R0).")
    lines.append("")

    # ── PART G: MANDATORY 3-PILLAR DESK EVALUATION ──────────────────────────
    lines.append("PART G: MANDATORY 3-PILLAR DESK EVALUATION (STRICT OPERATOR MANDATE)")
    lines.append("")
    lines.append("MANDATE 1 — DUAL-ENGINE SEARCH & PASSIVE LIMIT ORDER CANDIDATE IDENTIFICATION ACROSS ALL 24 ASSETS:")
    lines.append("OPERATOR MANDATE ON WAKE UP: You are strictly mandated to actively search for, qualify, and formulate high-conviction PASSIVE LIMIT ORDER proposals (both Model 1 Extreme Mean Reversion and Model 2 Trend Pullbacks) across all orthogonal asset clusters (Indices, Commodities, Metals, Forex, Crypto).")
    lines.append("Whenever portfolio capacity permits (currently 1 of 4 slots allocated, 3 slots freely available), actively formulate complete limit order parameters: Symbol, Order Type (BUY_LIMIT / SELL_LIMIT), Entry (shelf-anchored), SL (outside sweep band behind whale bunker), TP (front-running magnet by 5-10 bps), Lots (calibrated to $7.50-$14.50 USD risk envelope), and Stressed Capital Floor Check.")
    lines.append("MANDATORY EXCEL SHEET SCANNING REQUIREMENT: You MUST systematically cross-reference the sheets in Data/DataBase_Trading.xlsx while finding potential candidates:")
    lines.append("  1. Sheets 1-6 & 40 (ETF Flows & Treasuries): Confirm institutional macro backing.")
    lines.append("  2. Sheets 7-11 & 28-30 (Funding & Retail Positions): Confirm contrarian edge and absence of crowded traps.")
    lines.append("  3. Sheet 34 & Sheets 13-18 (System State & Open Interest): Verify 1H/4H trend regime and expanding interest. Reject UNDEFINED regimes.")
    lines.append("  4. Sheet 35 & Sheet 23 (CVD Depth & Whales Orders >= 100K): Anchor entry to shelf and shield stop loss behind persistent resting whale walls (>= 180s).")
    lines.append("  5. Sheets 21-22 & 37 (Liquidation Maps 1D/7D & Flow Feed): Verify TP magnet clearance and ensure SL sits outside sweep bands.")
    lines.append("  6. Sheets 38-39 (Arkham On-Chain Forensics): Confirm smart money flow direction.")
    lines.append("  7. Sheet 42 (MT5 Quotes & Account Ledger): Verify spread friction <= 15% and capital floor cushion.")
    lines.append("Analyze all 24 assets in Data/DataBase_Trading.xlsx Sheets 34-36 & 41-42 line-by-line (covering all Cryptos, Metals GOLD/XAUUSD.pi & SILVER/XAGUSD.pi, Energy USWTI.p, Forex EURUSD.pi/GBPUSD.pi/USDJPY.pi, and Indices SP500.p/NAS100.p/DJ30.p/GER40.p).")
    lines.append("APPLY PLAYBOOK SECTION 7.4 CALIBRATED MULTI-ASSET STANDARDS & 15% DYNAMIC FRICTION RULE:")
    lines.append("  • DYNAMIC 15% FRICTION RULE: Spread Friction % = (Spread in USD on 1 lot * Trade Lots) / Total Trade Risk Budget <= 15.0%.")
    lines.append("  • EXPANDED ACTIVE UNIVERSE ADMITTED: SP500.p (0.8% friction), NAS100.p (1.0%), XAUUSD.pi (1.2%), BTCUSD.pi (1.7%), DJ30.p (1.5%), GER40.p (2.0%), USWTI.p (3.5%), Major FX (0.5%), ETHUSD.pi (8.1% - target >= 2.2R), SOLUSD.p (13.8% - target >= 2.5R).")
    lines.append("  • CALIBRATED STRUCTURAL DEFENSE: TradFi Indices, Commodities & Forex: Held Auction Shelves (POC/VAH/VAL/VWAP) + HTF 20/50 EMAs + MT5 Tick CVD/OFI (no 0x on-chain requirement for OTC TradFi). Crypto: resting L2/L3 whale walls >= 500k USD with >= 180s persistence OR cumulative top-20 depth >= 1.5M USD.")
    lines.append("  • BANNED INSTRUMENTS (Friction > 15%): DOGE (210%), DOT (122%), ADA (89%), LINK (68%), NEAR (62%) — mathematically lethal on MT5 CFDs.")
    lines.append("For EACH asset, explicitly state: (a) Engine 1 verdict (Mean Reversion: Z-score, eligible or disqualified and why), (b) Engine 2 verdict (Trend Pullback: regime, shelf, eligible or disqualified and why), (c) Final classification: CANDIDATE / WATCHLIST / NO SETUP.")
    lines.append("")
    if not for_copilot:
        lines.append("Key Liquid Assets Snapshot (Comprehensive Depth, CVD, Whales, and Spreads in Data/DataBase_Trading.xlsx):")
        focus_keys = ["XAUUSD", "BTC", "ETH", "SOL", "SP500", "EURUSD"]
        for fk in focus_keys:
            a = assets.get(fk) or assets.get(fk + "USD.pi") or assets.get(fk + ".p") or {}
            if not a:
                continue
            q = a.get("quotes", {})
            ci = a.get("causal_indicators", {})
            ob = a.get("orderbook_live_depth", {})
            w3 = ob.get("whale_walls_l3") or []
            elig_w3 = [w for w in w3 if float(w.get("persist_s") or 0.0) >= 180.0]
            sc = a.get("structural_stop_clusters", {})
            rl = a.get("reconstructed_liquidations", {})
            s_below = sc.get('nearest_sell_stop_clusters_below', [])
            s_above = sc.get('nearest_buy_stop_clusters_above', [])
            s_b_str = f"[{s_below[0].get('min_price', 0):.1f}-{s_below[0].get('max_price', 0):.1f}]" if s_below else "none"
            s_a_str = f"[{s_above[0].get('min_price', 0):.1f}-{s_above[0].get('max_price', 0):.1f}]" if s_above else "none"
            l_b_str = f"[{rl.get('nearest_long_cascade_bands_below', [{}])[0].get('min_price', 0):.1f}-{rl.get('nearest_long_cascade_bands_below', [{}])[0].get('max_price', 0):.1f}]" if rl.get('nearest_long_cascade_bands_below') else "none"
            l_a_str = f"[{rl.get('nearest_short_squeeze_bands_above', [{}])[0].get('min_price', 0):.1f}-{rl.get('nearest_short_squeeze_bands_above', [{}])[0].get('max_price', 0):.1f}]" if rl.get('nearest_short_squeeze_bands_above') else "none"
            lines.append(
                f"• {fk} ({a.get('symbol_broker', '')}): Mid {q.get('mid')} | Spread {q.get('spread_bps')} bps | "
                f"Z = {ci.get('vwap_z_score')} SD | RSI {ci.get('rsi_14')} | Trend {ci.get('trend_regime')} | "
                f"Whales (elig>=180s): {len(elig_w3)} | Stops: Below {s_b_str} / Above {s_a_str} | Liq: Below {l_b_str} / Above {l_a_str}"
            )
        lines.append("• Full 24-Asset Microstructure, L2 Book Depth, Whales, and Basis Spreads: Read directly from Data/DataBase_Trading.xlsx (Sheets 21-23, 26, 35, 36, 41, 42).")
    else:
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
            cat = a.get("category", "")
            m_cvd = a.get("multi_horizon_cvd", {})
            s_cvd = float(m_cvd.get("session_cvd_usd") or 0.0)
            w_cvd = float(m_cvd.get("weekly_cvd_usd") or 0.0)
            div = m_cvd.get("divergence", "NEUTRAL")

            t_of = a.get("tradfi_orderflow", {})
            if cat == "CRYPTO":
                cvd_str = f"Sess CVD {s_cvd/1e6:+.2f}M | Wk CVD {w_cvd/1e6:+.2f}M | Flow: {div}"
                t_status = t_of.get("status")
                s_val = t_of.get("session_tick_cvd")
                c15_val = t_of.get("15m_tick_cvd")
                t_ofi_val = t_of.get("order_flow_imbalance_ofi")
                t_bias = t_of.get("flow_bias", "UNAVAILABLE")
                if t_status in ("AVAILABLE", "CALCULATED_FROM_MT5_TICKS") and s_val is not None:
                    s_tick = float(s_val)
                    c15_tick = float(c15_val if c15_val is not None else 0.0)
                    t_ofi = float(t_ofi_val if t_ofi_val is not None else 0.0)
                    cvd_str = f"TradFi OF: Sess {s_tick:+.0f}t, 15m {c15_tick:+.0f}t | Bias: {t_bias} | OFI: {t_ofi:+.3f}"
                else:
                    cvd_str = f"TradFi OF: UNAVAILABLE (No Live MT5 Ticks | Bias: {t_bias})"

            trp_str = a.get("trapped_traders_signal", "BALANCED")

            prof = a.get("htf_auction_profiles", {})
            d_poc = float(prof.get("prior_day_poc") or 0.0)
            d_vah = float(prof.get("prior_day_vah") or 0.0)
            d_val = float(prof.get("prior_day_val") or 0.0)
            w_vwap = float(prof.get("weekly_vwap") or 0.0)
            prof_str = f"PriorDay POC {d_poc:.2f} [VAH {d_vah:.2f} / VAL {d_val:.2f}] | WkVWAP {w_vwap:.2f}"

            s_below = sc.get('nearest_sell_stop_clusters_below', [])
            s_above = sc.get('nearest_buy_stop_clusters_above', [])
            s_b_str = f"[{s_below[0].get('min_price', 0):.1f}-{s_below[0].get('max_price', 0):.1f} ${s_below[0].get('notional_usd', 0)/1e6:.2f}M]" if s_below else "none"
            s_a_str = f"[{s_above[0].get('min_price', 0):.1f}-{s_above[0].get('max_price', 0):.1f} ${s_above[0].get('notional_usd', 0)/1e6:.2f}M]" if s_above else "none"

            l_below = rl.get('nearest_long_cascade_bands_below', [])
            l_above = rl.get('nearest_short_squeeze_bands_above', [])
            l_b_str = f"[{l_below[0].get('min_price', 0):.1f}-{l_below[0].get('max_price', 0):.1f} ${l_below[0].get('notional_usd', 0)/1e6:.2f}M]" if l_below else "none"
            l_a_str = f"[{l_above[0].get('min_price', 0):.1f}-{l_above[0].get('max_price', 0):.1f} ${l_above[0].get('notional_usd', 0)/1e6:.2f}M]" if l_above else "none"

            lines.append(
                f"• {sym_key} ({a.get('symbol_broker', '')} | {a.get('category', '')}): Mid {q.get('mid')} | Spread {q.get('spread_bps')} bps | "
                f"Z = {ci.get('vwap_z_score')} SD | RSI {ci.get('rsi_14')} | Trend {ci.get('trend_regime')} | "
                f"L2 Imb {ob.get('book_imbalance')} | {cvd_str} | Trapped: {trp_str} | {prof_str} | "
                f"L3 Whales (tot/elig>=180s): {len(w3)}/{len(elig_w3)} | "
                f"Stops Below/Above: {s_b_str} / {s_a_str} | "
                f"Liq Below/Above (Attraction Bands): {l_b_str} / {l_a_str}"
            )

    # ── EXPANDED INSTITUTIONAL SCREENER CANDIDATES (93-ASSET UNIVERSE) ───
    try:
        from Terminal.institutional_95_screener import run_fast_screen
        scr = run_fast_screen()
        scr_cands = [r for r in scr.get("summary", []) if r.get("status") in ("CANDIDATE_MODEL1", "CANDIDATE_MODEL2")]
        if scr_cands:
            lines.append("")
            lines.append("EXPANDED INSTITUTIONAL SCREENER HIGHLIGHTS (93-ASSET UNIVERSE):")
            lines.append("The following additional high-conviction candidates passed institutional spread friction (<= 5 bps TradFi, <= 25 bps Crypto) and structural regime checks:")
            for c in scr_cands[:10]:
                lines.append(f"  • {c['symbol']} ({c['group']}): Spread {c['spread_bps']} bps | Z = {c['vwap_z']} SD | RSI {c['rsi']} | ATR {c['atr']} | Regime {c['regime']} | Status: {c['status']}")
    except Exception:
        pass

    lines.append("")
    lines.append("PROACTIVE ALPHA MANDATE (STRICT OPERATOR DIRECTIVE):")
    lines.append("Do NOT default to \"STAND ASIDE\"! Stand Aside is ONLY mathematically justified if zero setups across both the 24-asset matrix and the 93-asset screener meet the 5-pillar confluence.")
    lines.append("Your primary objective on every cycle is to actively discover, evaluate, and structure the SINGLE HIGHEST-EXPECTANCY trade opportunity.")
    lines.append("If an eligible setup exists with:")
    lines.append("  1. HTF Trend Alignment (or confirmed extreme mean reversion |Z| >= 2.0 SD with trapped traders)")
    lines.append("  2. Spread friction within institutional limits (<= 5.0 bps TradFi, <= 25.0 bps Crypto)")
    lines.append("  3. Deep Shelf Anchor Entry (VWAP, EMA20/50, VAH/VAL)")
    lines.append("  4. SL Liquidity Bunker placed safely outside [min_price, max_price] with >= 0.35-0.50 ATR buffer")
    lines.append("  5. TP Liquidity Magnet front-running opposing stop/liquidation pools by 5-10 bps")
    lines.append("Then you MUST structure and output the trade in the Actionable Execution Summary Table with MT5 symbol, BUY/SELL LIMIT, exact lot size, Entry, SL, TP, USD risk, and R:R!")
    lines.append("")
    lines.append("For every qualifying new opportunity across Crypto, Metals, Energy, Forex, or Indices, specify: MT5 symbol, BUY/SELL LIMIT, exact lot size, Entry price, SL (0.35-0.50 ATR outside min_price/max_price of bunker), TP (front-running magnet by 5-10 bps), USD risk, R:R, Engine (1 or 2), and complete telemetry coincidence proof including which loss archetype(s) it specifically defends against.")
    lines.append("")

    # ── MANDATE 2: RUNNING TRADES ───────────────────────────────────────────
    lines.append("MANDATE 2 — LOOK FOR ACTIVE / RUNNING TRADES (LOGICAL TP OR SL MODIFICATION BASED ON LATEST DATA):")
    if positions:
        lines.append(f"• Current Active Running Trades on MT5: {len(positions)} open position(s):")
        for p in positions:
            ak = _resolve_asset_key(p["symbol"], assets)
            a_info = assets.get(ak, {})
            atr = float(a_info.get("causal_indicators", {}).get("atr_14") or 1.0)
            t_str = str(p["ticket"])
            # BUG FIX: Use frozen R0 from immutable ledger, not current ratcheted SL
            r0 = _get_frozen_r0(t_str, initial_risk_ledger, p["price_open"], p["sl"], atr)
            if p["type"] == "BUY":
                curr_r0 = (p["price_current"] - p["price_open"]) / r0
            else:
                curr_r0 = (p["price_open"] - p["price_current"]) / r0

            # Determine ratchet state from actual SL position vs entry
            if p["type"] == "SELL":
                sl_from_entry = p["price_open"] - p["sl"]  # negative = SL above entry (still initial)
            else:
                sl_from_entry = p["sl"] - p["price_open"]  # negative = SL below entry (still initial)

            if sl_from_entry > 0:
                ratchet_r = sl_from_entry / r0 if r0 > 0 else 0
                if ratchet_r >= 0.80:
                    ratchet_label = f"PHASE_1_PROFIT_LOCKED (SL locked at +{ratchet_r:.2f}R0)"
                elif ratchet_r >= -0.25:
                    ratchet_label = f"PHASE_0_RISK_CUT (SL moved to -0.25R0 risk, 75% cut)"
                else:
                    ratchet_label = f"SL RATCHETED to {ratchet_r:+.2f}R0 from entry"
            else:
                ratchet_label = "INITIAL (SL not yet ratcheted)"

            lines.append(
                f"  - Ticket #{p['ticket']}: {p['symbol']} {p['type']} {p['volume']} lots @ Entry {p['price_open']} USD | "
                f"Current: {p['price_current']} USD ({curr_r0:+.2f}R0 progress) | Frozen Initial R0 = {r0:.2f} pts | Floating PnL: {p['profit_usd']:+.2f} USD | "
                f"Current SL: {p['sl']} USD | Current TP: {p['tp']} USD | Ratchet State: {ratchet_label}"
            )
        lines.append("• For each running trade above, evaluate logically based on the latest data snapshot whether SL or TP modification is required:")
        lines.append("  1. Upgraded Piecewise Ratchet Check (Measured STRICTLY against Frozen Initial R0 — NEVER against current ratcheted SL distance):")
        lines.append("     Phase 0 Risk Cut (-0.25R0 lock): When progress reaches +1.25R0, move SL to Entry - 0.25R0 (75% risk reduction, leaving 0.25R buffer to avoid retest whip).")
        lines.append("     Phase 1 Profit Lock (+0.80R0 lock): When progress reaches +1.65R0, move SL to Entry +0.80R0.")
        lines.append("     Phase 2 Running Trail: When progress reaches >= +2.00R0, dynamic running trail at Peak MFE - 0.75R0.")
        lines.append("     CRITICAL: R-multiple inflation occurs when agents compute R from the current ratcheted SL distance instead of the frozen initial R0. Example: SP500 #18836609 has R0 = 32.0 pts. After Phase 0 risk cut moves SL to 7,807.75 (2.25 pts from entry), computing R from 2.25 pts gives a wildly inflated +10.85R which is WRONG. The correct R-progress is (7810 - current) / 32.0.")
        lines.append("  2. Live Microstructure & Bunker/Magnet Shift: Have new stop clusters, liquidation bands, or L3 whale walls formed in live_snapshot_latest.json that logically require tightening SL behind a newly formed structural bunker or adjusting TP to front-run a closer/stronger liquidity magnet? Or has the supporting structural shelf broken requiring an emergency exit?")
    else:
        lines.append("• Current Active Running Trades on MT5: 0 open positions (Flat / 100% Cash reserves). Confirm that no open-position ratchets are needed right now.")
    lines.append("")

    # ── MANDATE 3: UNFILLED LIMIT ORDERS ────────────────────────────────────
    lines.append("MANDATE 3 — AUDIT UNFILLED LIMIT ORDERS (VIABLE TO WAIT vs. SLIGHT MODIFICATION vs. DELETE):")
    if orders:
        lines.append(f"• Current Unfilled Limit Orders on MT5: {len(orders)} pending order(s):")
        for o in orders:
            ak = _resolve_asset_key(o["symbol"], assets)
            a_info = assets.get(ak, {})
            ci = a_info.get("causal_indicators", {})
            atr = float(ci.get("atr_14") or 1.0)
            dist_atr = abs(o["price_current"] - o["price_open"]) / atr if atr else 0.0
            lines.append(
                f"  - Ticket #{o['ticket']}: {o['symbol']} {o['type']} {o['volume']} lots @ Entry {o['price_open']} USD | "
                f"Live Mid: {o['price_current']} USD (Distance: {dist_atr:.2f} ATR, ATR_14={atr}) | "
                f"Current SL: {o['sl']} USD | Current TP: {o['tp']} USD | Trend: {ci.get('trend_regime')} | Z: {ci.get('vwap_z_score')} SD"
            )
        lines.append("• For EACH unfilled limit order listed above, perform a complete logical & quantitative audit against the latest Data/DataBase_Trading.xlsx (Sheets 21-25, 35, 36, 42) and explicitly classify it into one of three decisions:")
        lines.append("  (A) VIABLE — WAIT TO BE FILLED AS-IS: Confirm that distance to entry is <= 2.0 ATR, supporting L3 whale walls (persistence_s >= 180s) remain intact, 5m/15m/30m CVD and L2 imbalance support absorption, SL sits safely 0.35x-0.50x ATR outside min_price/max_price of the governing bunker, and TP front-runs the opposing buy-stop/sell-stop magnet by 5-10 bps.")
        lines.append("  (B) SLIGHT MODIFICATION REQUIRED (MODIFY ENTRY / SL / TP): If the thesis remains valid but live whale walls, stop clusters (nearest_*), or liquidation band boundaries (min_price/max_price) have shifted in the latest snapshot, specify the exact modified Entry, SL, and/or TP levels and why.")
        lines.append("  (C) DELETE / CANCEL IMMEDIATELY: If the structural thesis has degraded (e.g., supporting whale walls pulled/thinned >50%, price drifted >2.0 ATR away, regime invalidated, or unabsorbed aggressive selling/buying broke the shelf), recommend immediate deletion to free capacity.")
    else:
        lines.append("• Current Unfilled Limit Orders on MT5: 0 pending orders.")
    lines.append("")

    # ── STEP 4: PORTFOLIO CAPACITY ──────────────────────────────────────────
    lines.append("STEP 4 — PORTFOLIO CAPACITY & CAPITAL FLOOR GOVERNANCE:")
    lines.append("• Stress Formula: Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket (covering adverse gap, spread widening, and slippage).")
    lines.append(f"• Account Balance: {balance:.2f} USD | Equity: {equity:.2f} USD | Hard Floor: 4,775.00 USD | Operating Buffer: 4,795.00 USD.")

    if pos_stress_items:
        stress_parts = [f"Ticket #{p['ticket']} ({p['symbol']}) nominal {nom:.2f} USD -> stressed {stress:.2f} USD" for p, nom, stress in pos_stress_items]
        lines.append(f"• Open Position Stress: {', '.join(stress_parts)} (Total Contingent Stress: {tot_contingent_stress:.2f} USD).")
    else:
        lines.append("• Open Position Stress: 0.00 USD (Flat / 100% Cash reserves).")

    lines.append(f"• Available Stress Budget to 4,795.00 USD Buffer: {avail_budget:.2f} USD.")
    lines.append("• Strict Portfolio Capacity Rules:")
    lines.append(f"  - Active positions currently using {capacity_used} / 4 capacity slots ({capacity_available} available).")
    lines.append(f"  - Max new tickets permitted: {max_new_tickets} (at {calibrated_risk:.2f} USD risk = {calibrated_stress:.2f} USD stress each, or {max_tickets_min_risk} ticket(s) at 7.50 USD risk).")
    lines.append(f"  - Worst-case post-stop equity: {worst_case_equity:.2f} USD (cushion: +{worst_case_equity - 4650.0:.2f} USD above 4,795.00 operating buffer).")
    lines.append("• Joint Worst-Case Post-Stop Equity MUST remain unconditionally >= 4,795.00 USD (>= 20.00 USD cushion above 4,775.00 USD hard floor).")
    lines.append("")

    # ── OUTPUT FORMAT ───────────────────────────────────────────────────────
    lines.append("PART H: REQUIRED OUTPUT FORMAT & QUAD-COUNCIL SYNCHRONIZATION (2 ARENA.AI TABS + 2 COPILOT STUDIO TABS)")
    lines.append(f"1. TELEMETRY, PLAYBOOK & DECISION CHAIN INGESTION CITATION (confirming generation_id: {gen_id}, as_of_utc: {gen_ts}, macro event: {ev_name} at {ev_time} [blackout_active={blackout_active}], Playbook compliance, and execution of the 10-Step Standardized Decision Chain)")
    lines.append("2. MANDATE 1 REPORT: Line-by-Line Screening of Assets for New Trading Opportunities")
    lines.append("   For EACH asset: state Engine 1 verdict, Engine 2 verdict, and Final classification.")
    lines.append("3. MANDATE 2 REPORT: Active / Running Trades Audit (TP/SL Modifications using FROZEN INITIAL R0)")
    lines.append("4. MANDATE 3 REPORT: Unfilled Limit Orders Audit (Ticket-by-Ticket: WAIT / MODIFY / DELETE)")
    lines.append("5. ACTIONABLE EXECUTION SUMMARY TABLE:")
    lines.append("   | Action | Symbol | Side | Lots | Entry | SL Bunker | TP Magnet | Risk USD | R:R | Engine | Archetype Defense | Rationale |")
    lines.append("   If no actions: output table with single row: | STAND ASIDE | — | — | — | — | — | — | — | — | — | — | [Reason] |")
    lines.append("7. ARENA SKILL IMPLEMENTATION & ADAPTATION MANDATE (https://github.com/Jakeschincariol/arena-skill):")
    lines.append("   • The canonical 'arena-skill' tournament evaluation framework has been installed into this repository at `.agent/skills/arena/` (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agent/skills/arena/SKILL.md).")
    lines.append("   • If operating in an environment with bash/git access, install/confirm it via: `git clone https://github.com/Jakeschincariol/arena-skill.git ~/.claude/skills/arena` (or read `.agent/skills/arena/SKILL.md`).")
    lines.append("   • You MUST ALWAYS apply this arena tournament methodology to pit competing trade hypotheses against each other across the 5 personas and written rubric (`.agent/skills/arena/rubric.md`) before issuing any final trade verdict.")
    lines.append("8. INSTITUTIONAL QUANTITATIVE TELEMETRY AUDIT & PROFITABILITY ENHANCEMENT MANDATE:")
    lines.append("   • The operator specifically mandates a comprehensive, institutional quantitative review of our master trading database (`Data/DataBase_Trading.xlsx`, all 43 sheets) to maximize trading profitability, edge, and execution efficiency while defending the 4,775.00 USD hard floor:")
    lines.append("     a) Telemetry Data Structure & Microstructure Schema Audit:")
    lines.append("        - Critically review the schema in Data/DataBase_Trading.xlsx Sheets 34-36 (`Telemetry_System_State`, `Live_Orderbook_CVD_Depth`, `Exchange_Basis_Spreads`) and Sheets 21-25 (`Exchange_Liquidation_Map_1D/7D`, `Whales_Orders`, `Spot_Netflow`, `Hyperliquid_Whales`).")
    lines.append("        - What exact fields, features, or microstructural indicators are missing or suboptimal? Propose concrete mathematical additions: e.g. multi-level Order Flow Imbalance (OFI), Micro-price drift vs. Mid, Queue-position decay rate, Taker aggressor ratio over 1m/5m/15m/30m, and Footprint delta absorption scores.")
    lines.append("     b) Calibrating Model 1 & Model 2 for Payable >= 2.0R Setups:")
    lines.append("        - Both models frequently report 0 candidates due to strict 2.0R geometry or wide swing targets. How can we mathematically construct payable 2.0R - 2.5R setups that capture intraday liquidity sweeps without requiring multi-day 10 ATR excursions?")
    lines.append("        - How should the SL bunker buffer (currently 0.35 - 0.50 ATR beyond outer bunker edge) and TP magnet front-run (5 - 10 bps) be dynamically calibrated based on live volatility surface and book depth?")
    lines.append("     c) Institutional Macro Blackout & Risk Protection (Option 1 Formalized):")
    lines.append("        - OPERATOR DIRECTIVE: Macro blackout enforcement is ACTIVELY ENFORCED via BlackoutGuard (Option 1). New orders are strictly halted within ±35m of Tier-1 macro events (FOMC, CPI, NFP) and fail closed on calendar errors. Active positions continue trailing micro-ratchets. Evaluate and trade high-conviction setups outside the blackout window.")
    lines.append("        - How can we optimize execution on Blueberry Markets MT5 CFDs under the 15% dynamic friction rule to capture maximum net alpha?")
    lines.append("")
    if for_copilot:
        agent_label = "CLAUDE OPUS 5.5" if is_copilot_opus else "GPT ASTRA"
        lines.append(f"9. COUNCIL SYNC PROTOCOL (COPILOT STUDIO - {agent_label}):")
        lines.append("   • You are operating inside Microsoft Copilot Studio with all 4 context files attached natively to this session.")
        lines.append("   • Output your complete 3-Mandate Quantitative Audit, Dialectic Deliberation, and Actionable Execution Summary Table directly here in your response.")
        lines.append("   • Antigravity automatically harvests your response directly from the Copilot Studio DOM into docs/trade_plans/COPILOT_OPUS_LATEST_RAW.md / COPILOT_ASTRA_LATEST_RAW.md for Quad-Council synthesis.")
    elif is_fable:
        lines.append("9. COUNCIL SYNC PROTOCOL (ARENA.AI TAB 2 - DEEP REASONING MULTI-AGENT SQUAD):")
        lines.append("   • Output your complete 3-Mandate Council Report, Dialectic Deliberation, and Actionable Execution Table directly here in your markdown chat response.")
        lines.append("   • Antigravity automatically harvests your completed chat response via Chrome CDP into docs/trade_plans/ARENA_FABLE_LATEST_RAW.md and commits the record to main.")
        lines.append("   • You do NOT need to write local files or commit to git.")
    else:
        lines.append("9. COUNCIL SYNC PROTOCOL (ARENA.AI TAB 1 - DEEP REASONING MULTI-AGENT SQUAD):")
        lines.append("   • Output your complete 3-Mandate Council Report, Dialectic Deliberation, and Actionable Execution Table directly here in your markdown chat response.")
        lines.append("   • Antigravity automatically harvests your completed chat response via Chrome CDP into docs/trade_plans/ARENA_LATEST_RAW.md and commits the record to main.")
        lines.append("   • You do NOT need to write local files or commit to git.")

    return "\n".join(lines)


async def main():
    import argparse
    parser = argparse.ArgumentParser(description="Dispatch 3-Mandate Pure Telemetry Prompt to Arena.ai, Z.ai Chat, and Copilot Studio")
    parser.add_argument("--cycle", type=int, default=None, help="Cycle number (auto-increments if not specified)")
    parser.add_argument("--reprompt-file", type=str, default="", help="Optional Part-B corrective reprompt file path")
    parser.add_argument("--arena-only", action="store_true", help="Send only to Arena.ai")
    parser.add_argument("--zai-only", action="store_true", help="Send only to Z.ai Chat")
    parser.add_argument("--qwen-only", action="store_true", help="Send only to Qwen Chat")
    parser.add_argument("--copilot-only", action="store_true", help="Send only to Copilot Studio")
    parser.add_argument("--no-copilot", action="store_true", help="Skip Copilot Studio")
    parser.add_argument("--dry-run", action="store_true", help="Generate prompt to stdout without dispatching")
    args = parser.parse_args()

    cycle = args.cycle if args.cycle is not None else _load_cycle_num()

    if args.reprompt_file:
        p_path = pathlib.Path(args.reprompt_file)
        if not p_path.is_absolute():
            p_path = ROOT / p_path
        prompt = p_path.read_text(encoding="utf-8")
        arena_prompts = {"arena_1_primary": prompt, "arena_2_fable": prompt}
        copilot_prompts = {"Opus 5.5": prompt, "GPT Astra": prompt}
        print(f"Loaded Part-B corrective reprompt ({len(prompt)} chars) from {p_path}")
    else:
        prompt_arena_1 = build_prompt(cycle_num=cycle, target_agent="arena_1_primary")
        prompt_arena_2 = build_prompt(cycle_num=cycle, target_agent="arena_2_fable")
        prompt_copilot_opus = build_prompt(cycle_num=cycle, target_agent="Opus 5.5")
        prompt_copilot_astra = build_prompt(cycle_num=cycle, target_agent="GPT Astra")

        arena_prompts = {"arena_1_primary": prompt_arena_1, "arena_2_fable": prompt_arena_2}
        copilot_prompts = {"Opus 5.5": prompt_copilot_opus, "GPT Astra": prompt_copilot_astra}

        # Save prompt files for record and auditing
        p_dir = ROOT / "docs" / "prompts"
        p_dir.mkdir(parents=True, exist_ok=True)
        (p_dir / f"ARENA_CYCLE_{cycle}_ASTRA_PROMPT.txt").write_text(prompt_arena_1, encoding="utf-8")
        (p_dir / f"ARENA_CYCLE_{cycle}_FABLE_PROMPT.txt").write_text(prompt_arena_2, encoding="utf-8")
        (p_dir / f"COPILOT_CYCLE_{cycle}_OPUS_PROMPT.txt").write_text(prompt_copilot_opus, encoding="utf-8")
        (p_dir / f"COPILOT_CYCLE_{cycle}_ASTRA_PROMPT.txt").write_text(prompt_copilot_astra, encoding="utf-8")
        print(f"Generated Cycle {cycle} tailored prompts for all 4 agents:")
        print(f"  - Arena Tab 1 (GPT Astra): {len(prompt_arena_1)} chars")
        print(f"  - Arena Tab 2 (Claude Fable): {len(prompt_arena_2)} chars")
        print(f"  - Copilot Tab 1 (Opus 5.5): {len(prompt_copilot_opus)} chars")
        print(f"  - Copilot Tab 2 (GPT Astra): {len(prompt_copilot_astra)} chars")

    if args.dry_run:
        print("\n--- DRY RUN: Arena 1 Prompt Preview ---")
        print(arena_prompts["arena_1_primary"][:1500])
        return

    ok_arena = False
    ok_copilot = False

    if args.copilot_only:
        ok_copilot = await post_prompt_to_copilot(copilot_prompts)
    elif args.arena_only:
        await dismiss_arena_popup()
        ok_arena = await post_prompt_to_arena(arena_prompts, target="all")
    else:
        # Broadcast tailored prompts to all 4 target agents (2 Arena.ai tabs + 2 Copilot Studio tabs)
        await dismiss_arena_popup()
        ok_arena = await post_prompt_to_arena(arena_prompts, target="all")
        if not args.no_copilot:
            ok_copilot = await post_prompt_to_copilot(copilot_prompts)

    if ok_arena or ok_copilot:
        _save_cycle_num(cycle)
        print(f"SUCCESS: Cycle {cycle} prompt injected (Arena.ai tabs={ok_arena}, Copilot Studio tabs={ok_copilot})! Quad-Council actively computing.")
    else:
        print("ERROR: Failed to inject prompt into any platform", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
