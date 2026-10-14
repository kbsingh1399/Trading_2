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
    CYCLE_STATE_FILE.write_text(
        json.dumps({"last_cycle": cycle, "dispatched_utc": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())}),
        encoding="utf-8",
    )

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
    ev_name = macro_info.get("event", "None")
    ev_time = macro_info.get("event_release_utc", "None")
    blackout_active = macro_info.get("blackout_active", False)

    # Load immutable risk ledger ONCE for the entire prompt build
    initial_risk_ledger = _load_initial_risk_ledger()

    lines = []
    lines.append(f"TRADING DESK COUNCIL: CYCLE {cycle_num} PURE TELEMETRY & PLAYBOOK ANALYSIS PROMPT")
    if is_arena_astra:
        lines.append("ROUTING TARGET: GPT_ASTRA (ARENA PRIMARY WORKSPACE - TAB 1)")
        lines.append("CANONICAL WORKSPACE: https://github.com/kbsingh1399/Trading_2")
        lines.append("ACTIVE BRANCH: arena/5c05910e-trading-2 (https://github.com/kbsingh1399/Trading_2/tree/arena/5c05910e-trading-2)")
    elif is_fable:
        lines.append("ROUTING TARGET: CLAUDE FABLE 5.1 / MYTHOS-CLASS FRONTIER REASONING ENGINE (ANTHROPIC FABLE ORCHESTRATOR - TAB 2)")
        lines.append("CANONICAL WORKSPACE: https://github.com/kbsingh1399/Trading_2")
        lines.append("ACTIVE BRANCH: arena/e3d7cc98-trading-2 (https://github.com/kbsingh1399/Trading_2/tree/arena/e3d7cc98-trading-2)")
    elif is_copilot_opus:
        lines.append("ROUTING TARGET: CLAUDE OPUS 5.5 (MICROSOFT COPILOT STUDIO - TAB 1)")
        lines.append("ROLE: LEAD FORENSIC QUANTITATIVE STRATEGIST & MICROSTRUCTURE ARCHITECT")
    elif is_copilot_astra:
        lines.append("ROUTING TARGET: GPT ASTRA (MICROSOFT COPILOT STUDIO - TAB 2)")
        lines.append("ROLE: CAPITAL FLOOR SENTRY & MULTI-CLUSTER STRESSED RISK AUDITOR")
    lines.append("MANDATE: 100% DIRECT LINE-BY-LINE ANALYSIS OF docs/telemetry/live_snapshot_latest.json (ZERO DECISION GATES)")
    lines.append("")

    # ── PART A: SOURCE FILES ────────────────────────────────────────────────
    if for_copilot:
        lines.append("PART A: ATTACHED LOCAL CONTEXT FILES (NATIVELY ATTACHED TO THIS CHAT SESSION)")
        lines.append("The 4 primary ground-truth source files are ATTACHED DIRECTLY TO THIS MESSAGE AS NATIVE ATTACHMENTS.")
        lines.append("You do NOT need to call GitHub or fetch external URLs — read the attached files directly:")
        lines.append(f"1. Attached File `live_snapshot_latest.json` (Generation: {gen_id}, {gen_ts}):")
        lines.append("   The complete 24-asset live microstructure snapshot (quotes, MT5 spread_bps & mid, execution_specs, causal_indicators [Session VWAP, Z-score, RSI, ATR, EMA 20/50/200, POC/VAH/VAL], multi_horizon_cvd [Session/Weekly/24h CVD & divergence], tradfi_orderflow [synthetic tick CVD & OFI], htf_auction_profiles [Prior Day/Week POC/VAH/VAL & Developing Weekly VWAP], trapped_traders_signal [TRAPPED_BUYERS_ABOVE/TRAPPED_SELLERS_BELOW], orderbook_live_depth [20-level L2 depth & imbalance], whale_walls_l3 [0x... wallet addresses, sizes, persistence_s >= 180s], structural_stop_clusters, reconstructed_liquidations, and venue_basis).")
        lines.append("   Note on Schema Metadata: Top-level `trade_authorization: DENIED_UNVERIFIED_ORDERFLOW` in the JSON header is a static schema provenance tag confirming the telemetry publisher script itself never submits broker orders; it is NOT a trading lock on the Council.")
        lines.append("2. Attached File `TRADE_DECISION_PLAYBOOK.md`:")
        lines.append("   Apply the Parameter Coincidence Matrix (Entry Shelf + SL Liquidity Bunker outside min_price/max_price + TP Liquidity Magnet front-run by 5-10 bps + Psychological Round Numbers), Dual-Venue Division of Labor (Spreads/Quotes from MT5; Orderbook/Whales/Liquidations/Stops from Hyperdash & Binance), and the 7-Point Pre-Trade Checklist.")
        lines.append("3. Attached File `LIVE_COLLABORATIVE_ORDER_DESK.md`:")
        lines.append("   Live order desk history, active tickets, preceding council rulings, and execution logs.")
        lines.append("4. Attached File `ACTIVE_CONTEXT.md`:")
        lines.append("   Real-time mission card, capital floor rules (4,775.00 USD hard floor / 4,795.00 USD operating buffer), and settled quantitative invariants.")
        lines.append("")
    elif is_fable:
        lines.append("PART A: REQUIRED READING (complete before analysis)")
        lines.append("Read the following repository sources in full:")
        lines.append("")
        lines.append("1. Live Telemetry Matrix (Primary Ground Truth): docs/telemetry/live_snapshot_latest.json")
        lines.append(f"   Latest Generation: {gen_id} ({gen_ts})")
        lines.append("   Upstream Main: https://github.com/kbsingh1399/Trading_2/blob/main/docs/telemetry/live_snapshot_latest.json")
        lines.append("   Upstream Branch: https://github.com/kbsingh1399/Trading_2/blob/arena/e3d7cc98-trading-2/docs/telemetry/live_snapshot_latest.json")
        lines.append("   Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json")
        lines.append("   Inspect all 24 assets in assets_matrix_24 and all telemetry blocks.")
        lines.append("2. Live Trade Decision Playbook: docs/specs/TRADE_DECISION_PLAYBOOK.md")
        lines.append("   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md")
        lines.append("3. Live Order Desk & Session Context:")
        lines.append("   • docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md)")
        lines.append("   • .agents/rules/ACTIVE_CONTEXT.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md)")
        lines.append("   • .agents/memory/session_chat_history.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md)")
        lines.append("")
    else:  # arena_astra
        lines.append("PART A: REQUIRED READING (complete before analysis)")
        lines.append("Read the following repository sources in full:")
        lines.append("")
        lines.append("1. Live Telemetry Matrix (Primary Ground Truth): docs/telemetry/live_snapshot_latest.json")
        lines.append(f"   Latest Generation: {gen_id} ({gen_ts})")
        lines.append("   Upstream Main: https://github.com/kbsingh1399/Trading_2/blob/main/docs/telemetry/live_snapshot_latest.json")
        lines.append("   Upstream Branch: https://github.com/kbsingh1399/Trading_2/blob/arena/5c05910e-trading-2/docs/telemetry/live_snapshot_latest.json")
        lines.append("   Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json")
        lines.append("   Inspect all 24 assets in assets_matrix_24 and all telemetry blocks.")
        lines.append("2. Live Trade Decision Playbook: docs/specs/TRADE_DECISION_PLAYBOOK.md")
        lines.append("   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md")
        lines.append("3. Live Order Desk & Session Context:")
        lines.append("   • docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/arena/5c05910e-trading-2/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md)")
        lines.append("   • .agents/rules/ACTIVE_CONTEXT.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md)")
        lines.append("   • .agents/memory/session_chat_history.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md)")
        lines.append("")

    # ── PART B: ACCOUNT & RISK BASELINE ─────────────────────────────────────
    lines.append("PART B: ACCOUNT AND RISK BASELINE")
    lines.append("• Execution Mode: PASSIVE LIMIT ORDERS ONLY (no market orders).")
    lines.append("• Broker: Blueberry Markets SVG LLC, MetaTrader 5 account #5064568")
    lines.append(f"• Balance / Equity: {balance:.2f} USD / {equity:.2f} USD")
    lines.append(f"• Margin used: {margin:.2f} USD")
    lines.append("• Realized Deals Banked Today: Ticket #18836609 (SP500.p SHORT -> +0.90 USD cash profit booked via Trailing Stop Loss at 7,807.75), Ticket #18826511 (ETHUSD.pi SHORT -> +1.92 USD profit banked via Profit Lock at 2,513.02), Ticket #18813768 (SOLUSD.p SHORT -> +9.52 USD profit banked via Phase 1 Lock), Ticket #18813767 (BTCUSD.pi SHORT -> +16.10 USD full TP).")
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
    avail_budget = max(0.0, min_capital - 4795.0 - tot_contingent_stress)
    max_new_stress = 1.25 * 14.50 + 2.0  # 20.125 USD per new ticket at max risk
    max_new_tickets = min(capacity_available, int(avail_budget / max_new_stress)) if max_new_stress > 0 else 0
    worst_case_equity = min_capital - tot_contingent_stress

    # Build dynamic capacity blurb
    stress_detail_parts = []
    for p, nom, stress in pos_stress_items:
        stress_detail_parts.append(f"#{p['ticket']} ({p['symbol']} {p['type']}) nom {nom:.2f} -> stressed {stress:.2f} USD")
    stress_detail = "; ".join(stress_detail_parts) if stress_detail_parts else "0.00 USD (Flat)"

    lines.append(f"• Rigorous Capacity Ceiling: Open positions currently consume {tot_contingent_stress:.2f} USD total contingent stress ({stress_detail}). Stressed worst-case equity is {worst_case_equity:.2f} USD, leaving +{worst_case_equity - 4795.0:.2f} USD above 4,795.00 USD buffer. Capacity permits: max {max_new_tickets} new ticket(s) at 14.50 USD risk (stress {max_new_stress:.2f} USD each). Capacity: {capacity_used}/4 filled, {capacity_available} available.")
    lines.append("")

    # ── PART C: ACTIVE REPOSITORIES ─────────────────────────────────────────
    lines.append("PART C: ACTIVE REPOSITORIES & DATA PROVENANCE")
    lines.append("• Canonical Workspace: https://github.com/kbsingh1399/Trading_2")
    lines.append("• Active Branches: main (production) and arena/5c05910e-trading-2 (container active sync)")
    lines.append("• Direct Raw URLs:")
    lines.append("  - Telemetry: https://raw.githubusercontent.com/kbsingh1399/Trading_2/arena/5c05910e-trading-2/docs/telemetry/live_snapshot_latest.json")
    lines.append("  - Playbook: https://raw.githubusercontent.com/kbsingh1399/Trading_2/arena/5c05910e-trading-2/docs/specs/TRADE_DECISION_PLAYBOOK.md")
    lines.append("  - Desk State: https://raw.githubusercontent.com/kbsingh1399/Trading_2/arena/5c05910e-trading-2/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md")
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
    lines.append("  DO NOT STICK DOGMATICALLY TO VWAP SD BANDS ALONE. Fading oversold/overbought bands in a trending market is lethal. You MUST evaluate the overall trend supported by all parameters in live_snapshot_latest.json:")
    lines.append("  1. Higher Timeframe Trend Hierarchy: Inspect 1H & 4H OHLCV candles, 20/50/200 EMAs. If Price < EMA20 < EMA50 on 1H/4H (Bearish regime), Model 1 dip-buying Longs are STRICTLY FORBIDDEN. All priority shifts to Model 2 Trend Pullback SHORTS!")
    lines.append("  2. cvd_1m_buckets & CVD Momentum: Massive negative taker CVD (-1M to -3M USD) is proof of aggressive seller domination. Never buy into negative CVD. Use negative CVD to qualify SHORT entries on relief rallies.")
    lines.append("  3. Model 2 Pullback Short Protocol: In a downtrend, patiently wait for pullbacks up into the EMA20/EMA50/VAH shelves where heavy Ask Whale Walls are resting to defend the Stop Loss.")
    lines.append("")
    lines.append("18-PARAMETER TELEMETRY FIELD REFERENCE (live_snapshot_latest.json schema):")
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
    lines.append("      - Gate R-2 (Calibrated Asset-Class Whale Bunker Shield): Between entry and Stop Loss, there MUST be at least one substantial verified resting whale wall (persistence >= 180s) standing in front of the SL to absorb retracement momentum, calibrated by asset class:")
    lines.append("        * Crypto Major (BTCUSD.pi, ETHUSD.pi): >= 5.0M USD resting wall")
    lines.append("        * TradFi Equity Indices (SP500.p, NAS100.p, DJ30.p, GER40.p): >= 1.0M USD primary wall (removes artificial 3M block on index CFDs)")
    lines.append("        * Commodities (XAUUSD.pi, USWTI.p): >= 0.75M USD primary wall")
    lines.append("        * Major Forex (EURUSD.pi, GBPUSD.pi, USDJPY.pi): >= 0.50M USD primary wall")
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
    lines.append("     e) Check: Is the supporting wall < 500k USD or < 180s persistence? -> ARCHETYPE 4 KILL.")
    lines.append("     f) Check: Can a venue_basis spike + broker spread widening tag the stop? -> ADDITIONAL KILL.")
    lines.append("     Certify clearance ONLY if no fatal flaw exists under any archetype.")
    lines.append("")

    # ── PART G: MANDATORY 3-PILLAR DESK EVALUATION ──────────────────────────
    lines.append("PART G: MANDATORY 3-PILLAR DESK EVALUATION (STRICT OPERATOR MANDATE)")
    lines.append("")
    lines.append("MANDATE 1 — DUAL-ENGINE SEARCH ACROSS ALL 24 ASSETS (MEAN REVERSION + TREND PULLBACKS):")
    lines.append("Analyze all 24 assets in assets_matrix_24 line-by-line from docs/telemetry/live_snapshot_latest.json (covering all Cryptos, Metals GOLD/XAUUSD.pi & SILVER/XAGUSD.pi, Energy USWTI.p, Forex EURUSD.pi/GBPUSD.pi/USDJPY.pi, and Indices SP500.p/NAS100.p/DJ30.p/GER40.p).")
    lines.append("APPLY PLAYBOOK SECTION 7.4 CALIBRATED MULTI-ASSET STANDARDS & 15% DYNAMIC FRICTION RULE:")
    lines.append("  • DYNAMIC 15% FRICTION RULE: Spread Friction % = (Spread in USD on 1 lot * Trade Lots) / Total Trade Risk Budget <= 15.0%.")
    lines.append("  • EXPANDED ACTIVE UNIVERSE ADMITTED: SP500.p (0.8% friction), NAS100.p (1.0%), XAUUSD.pi (1.2%), BTCUSD.pi (1.7%), DJ30.p (1.5%), GER40.p (2.0%), USWTI.p (3.5%), Major FX (0.5%), ETHUSD.pi (8.1% - target >= 2.2R), SOLUSD.p (13.8% - target >= 2.5R).")
    lines.append("  • CALIBRATED WHALE WALL DEFENSE: TradFi indices require >= 1.0M USD primary wall; Commodities >= 0.75M USD; Crypto >= 5.0M USD.")
    lines.append("  • BANNED INSTRUMENTS (Friction > 15%): DOGE (210%), DOT (122%), ADA (89%), LINK (68%), NEAR (62%) — mathematically lethal on MT5 CFDs.")
    lines.append("For EACH asset, explicitly state: (a) Engine 1 verdict (Mean Reversion: Z-score, eligible or disqualified and why), (b) Engine 2 verdict (Trend Pullback: regime, shelf, eligible or disqualified and why), (c) Final classification: CANDIDATE / WATCHLIST / NO SETUP.")
    lines.append("")
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
        else:
            t_status = t_of.get("status")
            s_tick = float(t_of.get("session_tick_cvd") or 0.0)
            c15_tick = float(t_of.get("15m_tick_cvd") or 0.0)
            t_bias = t_of.get("flow_bias", "NEUTRAL")
            t_ofi = float(t_of.get("order_flow_imbalance_ofi") or 0.0)
            if t_status == "AVAILABLE":
                cvd_str = f"TradFi OF: Sess {s_tick:+.0f}t, 15m {c15_tick:+.0f}t | Bias: {t_bias} | OFI: {t_ofi:+.3f}"
            else:
                cvd_str = f"TradFi OF: L1 Tick Stream Validated | Bias: {t_bias}"

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
        lines.append("• For EACH unfilled limit order listed above, perform a complete logical & quantitative audit against the latest live_snapshot_latest.json and explicitly classify it into one of three decisions:")
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
    lines.append(f"  - Max new tickets permitted: {max_new_tickets} (at 14.50 USD risk = {max_new_stress:.2f} USD stress each).")
    lines.append(f"  - Worst-case post-stop equity: {worst_case_equity:.2f} USD (cushion: +{worst_case_equity - 4795.0:.2f} USD above 4,795.00 operating buffer).")
    lines.append("• Joint Worst-Case Post-Stop Equity MUST remain unconditionally >= 4,795.00 USD (>= 20.00 USD cushion above 4,775.00 USD hard floor).")
    lines.append("")

    # ── OUTPUT FORMAT ───────────────────────────────────────────────────────
    lines.append("PART H: REQUIRED OUTPUT FORMAT & QUAD-COUNCIL SYNCHRONIZATION (2 ARENA.AI TABS + 2 COPILOT STUDIO TABS)")
    lines.append(f"1. TELEMETRY & PLAYBOOK INGESTION CITATION (confirming generation_id: {gen_id}, as_of_utc: {gen_ts}, macro event: {ev_name} at {ev_time} [blackout_active={blackout_active}], and Playbook compliance)")
    lines.append("2. MANDATE 1 REPORT: Line-by-Line Screening of 24 Assets for New Trading Opportunities")
    lines.append("   For EACH asset: state Engine 1 verdict, Engine 2 verdict, and Final classification.")
    lines.append("3. MANDATE 2 REPORT: Active / Running Trades Audit (TP/SL Modifications using FROZEN INITIAL R0)")
    lines.append("4. MANDATE 3 REPORT: Unfilled Limit Orders Audit (Ticket-by-Ticket: WAIT / MODIFY / DELETE)")
    lines.append("5. ACTIONABLE EXECUTION SUMMARY TABLE:")
    lines.append("   | Action | Symbol | Side | Lots | Entry | SL Bunker | TP Magnet | Risk USD | R:R | Engine | Archetype Defense | Rationale |")
    lines.append("   If no actions: output table with single row: | STAND ASIDE | — | — | — | — | — | — | — | — | — | — | [Reason] |")
    if for_copilot:
        agent_label = "CLAUDE OPUS 5.5" if is_copilot_opus else "GPT ASTRA"
        lines.append(f"6. COUNCIL SYNC PROTOCOL (COPILOT STUDIO - {agent_label}):")
        lines.append("   • You are operating inside Microsoft Copilot Studio with all 4 context files attached natively to this session.")
        lines.append("   • Output your complete 3-Mandate Quantitative Audit, Dialectic Deliberation, and Actionable Execution Summary Table directly here in your response.")
        lines.append("   • Antigravity automatically harvests your response directly from the Copilot Studio DOM into docs/trade_plans/COPILOT_OPUS_LATEST_RAW.md / COPILOT_ASTRA_LATEST_RAW.md for Quad-Council synthesis.")
    elif is_fable:
        lines.append("6. COUNCIL SYNC PROTOCOL (ARENA.AI TAB 2 - CLAUDE FABLE ORCHESTRATOR):")
        lines.append("   • Output your complete 3-Mandate Council Report, Dialectic Deliberation, and Actionable Execution Table directly here in your markdown response.")
        lines.append("   • CRITICAL DIRECTIVE: DO NOT execute `git push origin arena/e3d7cc98-trading-2` attempting to push 1.6 GB git packfiles! That times out in sandbox mode.")
        lines.append("   • Write your findings locally to docs/trade_plans/ARENA_COUNCIL_REPORT_*.md or append to docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md, but present your entire analytical proof directly in markdown in this chat response!")
    else:
        lines.append("6. COUNCIL SYNC PROTOCOL (ARENA.AI TAB 1 - GPT ASTRA):")
        lines.append("   • Output your complete 3-Mandate Council Report, Dialectic Deliberation, and Actionable Execution Table in your response.")
        lines.append("   • Push your council report to your active branch `arena/5c05910e-trading-2` and append to docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md.")

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
