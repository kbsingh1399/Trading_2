"""
Terminal/arena_bridge.py
Autonomous Arena.ai Collaborative Bridge and 48-Hour Orderflow Prompt Dispatcher.
Extracts 48-hour multi-timeframe footprint candle data (4H, 1H, 15m) along with CVD,
orderbook depth, L2/L3 whale walls, liquidation levels, and account state,
then dispatches the prompt directly into Arena.ai via Chrome DevTools Protocol (CDP)
and evaluates Arena's recommendations against strict quantitative orderflow gates.
"""

from __future__ import annotations
import asyncio
import importlib.util
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import polars as pl
import websockets

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
CANDLES_DIR = PROJECT_ROOT / "Data" / "Candles"
TELEMETRY_SNAPSHOT = PROJECT_ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"

CDP_HTTP_URL = "http://localhost:9222"

PRIMARY_ASSETS = [
    # 14 Institutional Binance Perpetuals (Crypto)
    "BTC", "ETH", "SOL", "BNB", "XRP", "ADA", "DOGE", "TRX", "DOT", "LINK", "BCH", "LTC", "AVAX", "NEAR",
    # 3 Commodities & Metals
    "GOLD", "SILVER", "USWTI",
    # 3 Forex Majors
    "EURUSD", "GBPUSD", "USDJPY",
    # 4 Global Indices
    "SP500", "NAS100", "DJ30", "GER40"
]


def load_parquet_candles(asset: str) -> Optional[pd.DataFrame]:
    """Load 15m candles from Data/Candles/{asset}_15m.parquet."""
    pq_path = CANDLES_DIR / f"{asset}_15m.parquet"
    if not pq_path.exists():
        return None
    try:
        pldf = pl.read_parquet(pq_path)
        df = pldf.to_pandas()
    except Exception:
        try:
            df = pd.read_parquet(pq_path)
        except Exception:
            return None

    # Standardize time
    time_col = None
    for c in ["datetime_utc", "datetime", "time", "timestamp"]:
        if c in df.columns:
            time_col = c
            break
    if not time_col:
        return None

    if pd.api.types.is_numeric_dtype(df[time_col]):
        df["std_dt"] = pd.to_datetime(df[time_col], unit="s", utc=True)
    else:
        df["std_dt"] = pd.to_datetime(df[time_col], errors="coerce", utc=True)

    df.dropna(subset=["std_dt"], inplace=True)
    df.sort_values("std_dt", inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Ensure numeric OHLCV
    for c in ["open", "high", "low", "close", "volume", "tick_volume"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0.0)

    # Compute bar orderflow delta if not present
    vol_col = "volume" if "volume" in df.columns and df["volume"].sum() > 0 else "tick_volume"
    spread = np.maximum(df["high"] - df["low"], 1e-9)
    norm_pos = (df["close"] - df["low"]) / spread
    df["bar_delta"] = df[vol_col] * (2.0 * norm_pos - 1.0)
    df["cum_cvd"] = df["bar_delta"].cumsum()

    return df


def resample_bars(df_15m: pd.DataFrame, freq: str) -> pd.DataFrame:
    """Resample 15m candles to 1H or 4H with OHLC, volume, delta, and CVD."""
    if df_15m.empty:
        return pd.DataFrame()

    df = df_15m.set_index("std_dt")
    vol_col = "volume" if "volume" in df.columns and df["volume"].sum() > 0 else "tick_volume"

    resampled = df.resample(freq).agg({
        "open": "first",
        "high": "max",
        "low": "min",
        "close": "last",
        vol_col: "sum",
        "bar_delta": "sum"
    }).dropna(subset=["open"])

    resampled.reset_index(inplace=True)
    resampled.rename(columns={vol_col: "volume"}, inplace=True)
    resampled["cum_cvd"] = resampled["bar_delta"].cumsum()
    return resampled


def compute_volume_profile(df: pd.DataFrame, n_bins: int = 16) -> Dict[str, float]:
    """Compute POC, VAH, VAL over a slice of candles."""
    if df.empty or len(df) == 0:
        return {"poc": 0.0, "vah": 0.0, "val": 0.0}
    low_min = df["low"].min()
    high_max = df["high"].max()
    if high_max <= low_min:
        return {"poc": low_min, "vah": high_max, "val": low_min}

    bin_edges = np.linspace(low_min, high_max, n_bins + 1)
    bin_mids = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    bin_vols = np.zeros(n_bins, dtype=float)

    for _, r in df.iterrows():
        c_low = r["low"]
        c_high = r["high"]
        c_vol = r["volume"]
        mask = (bin_edges[1:] >= c_low) & (bin_edges[:-1] <= c_high)
        n_overlap = np.sum(mask)
        if n_overlap > 0:
            bin_vols[mask] += c_vol / n_overlap

    total_vol = float(np.sum(bin_vols))
    if total_vol <= 0:
        return {"poc": low_min, "vah": high_max, "val": low_min}

    poc_idx = int(np.argmax(bin_vols))
    poc_px = float(bin_mids[poc_idx])

    target_va = 0.70 * total_vol
    accum = bin_vols[poc_idx]
    up_i = poc_idx
    down_i = poc_idx

    while accum < target_va and (up_i < n_bins - 1 or down_i > 0):
        up_v = bin_vols[up_i + 1] if up_i < n_bins - 1 else -1.0
        down_v = bin_vols[down_i - 1] if down_i > 0 else -1.0
        if up_v >= down_v and up_i < n_bins - 1:
            up_i += 1
            accum += up_v
        elif down_i > 0:
            down_i -= 1
            accum += down_v
        else:
            break

    val_px = float(bin_edges[down_i])
    vah_px = float(bin_edges[up_i + 1])
    return {"poc": round(poc_px, 4), "vah": round(vah_px, 4), "val": round(val_px, 4)}


def detect_mirrored_wall_leg(wall: Dict[str, Any], whales: List[Dict[str, Any]],
                             tol: float = 0.05) -> Optional[Dict[str, Any]]:
    """Return the size-matched opposite-side leg of a whale wall, if one exists.

    HyperDash L3 wallet orderbooks routinely show the SAME address quoting both
    sides of the market at (near) identical size -- a market-making grid or a
    bracket, not directional inventory. Rendering the ask leg alone reads as
    "21M USD sell wall overhead", which the operator then reasons about as a
    trapped-short liquidation magnet. That inference is wrong: a sell wall that
    is size-matched by an equal buy wall from the same wallet carries no net
    directional information. This surfaces the mirror so the prompt cannot
    present one leg of a bracket as a one-sided wall.
    """
    if not isinstance(wall, dict):
        return None
    side = wall.get("side")
    if side not in ("BUY", "SELL"):
        return None
    addr = wall.get("address")
    try:
        size = float(wall.get("size") or 0.0)
    except (TypeError, ValueError):
        return None
    if size <= 0:
        return None
    want = "SELL" if side == "BUY" else "BUY"
    for other in whales or []:
        if not isinstance(other, dict) or other is wall:
            continue
        if other.get("side") != want:
            continue
        if addr is not None and other.get("address") != addr:
            continue
        try:
            osize = float(other.get("size") or 0.0)
        except (TypeError, ValueError):
            continue
        if osize <= 0:
            continue
        if abs(osize - size) / size <= tol:
            return other
    return None


def _load_gate_classifier():
    """Load classify_regime from decision_gates_v3.py by file path.

    Resolved by path rather than package import so the briefing reports the
    enforced regime however arena_bridge is invoked (as a script, via -m, or
    imported). Returns None if the module cannot be loaded, in which case the
    renderer says so explicitly instead of silently dropping the gate.
    """
    path = PROJECT_ROOT / "Terminal" / "decision_gates_v3.py"
    try:
        spec = importlib.util.spec_from_file_location("dg_v3_for_briefing", path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules["dg_v3_for_briefing"] = mod
        spec.loader.exec_module(mod)
        return mod.classify_regime
    except Exception:
        return None


def enforced_regime(asset_data: Dict[str, Any], classify,
                    as_of_epoch: Optional[float] = None) -> str:
    """Render the ENFORCED gate verdict next to the cosmetic 200-EMA label.

    `causal_indicators.trend_regime` is a 200-EMA heuristic. It is NOT the gate.
    `model1_checklist` requires regime == MEAN_REVERT and `model2_checklist`
    requires regime in {TREND_UP, TREND_DOWN}, and both read `classify_regime()`.
    Publishing only the heuristic label let the desk argue "Regime = BULLISH"
    while the enforced gate returned UNDEFINED -- which mandates stand-aside for
    BOTH engines. This surfaces the verdict the checklist will actually assert.

    The staleness arguments are passed deliberately. Without them a weekend
    CFD classifies as MEAN_REVERT straight off its frozen Friday bars, which
    would advertise a tradeable regime for a market that is shut.
    """
    if classify is None:
        return "enforced_gate=UNAVAILABLE(module_load_failed)"
    if not isinstance(asset_data, dict):
        return "enforced_gate=UNAVAILABLE(no_asset_data)"

    def closes(key: str) -> List[float]:
        out = []
        for bar in asset_data.get(key) or []:
            if isinstance(bar, dict) and bar.get("close") is not None:
                try:
                    out.append(float(bar["close"]))
                except (TypeError, ValueError):
                    continue
        return out

    c15 = closes("bars_15m_ohlcv")
    c1h = closes("htf_1h_ohlcv")
    c4h = closes("htf_4h_ohlcv")

    kwargs: Dict[str, Any] = {}
    if as_of_epoch is not None:
        stamps = []
        for key in ("bars_15m_ohlcv", "htf_1h_ohlcv", "htf_4h_ohlcv"):
            for bar in asset_data.get(key) or []:
                if isinstance(bar, dict) and bar.get("close_ts") is not None:
                    try:
                        stamps.append(float(bar["close_ts"]))
                    except (TypeError, ValueError):
                        continue
        if stamps:
            kwargs["last_close_epoch"] = max(stamps)
            kwargs["as_of_epoch"] = float(as_of_epoch)
    try:
        verdict, stats = classify(c15, c1h, c4h, **kwargs)
    except Exception as exc:
        return f"enforced_gate=ERROR({type(exc).__name__})"
    if stats.get("stale"):
        age = stats.get("bar_age_s")
        tag = f"STALE_BARS_age={age:.0f}s" if isinstance(age, (int, float)) else "STALE_BARS"
    else:
        tag = "live"
    return f"enforced_gate={verdict}({tag})"


def build_48h_orderflow_prompt() -> str:
    """Build canonical council prompt strictly following TRADING DESK COUNCIL: STRUCTURED OPERATING PROMPT."""
    try:
        from Terminal.dispatch_comprehensive_wake_up_prompt import build_prompt as build_council_structured_prompt
        return build_council_structured_prompt()
    except Exception as exc:
        print(f"Warning: Falling back to internal prompt builder due to {exc}", file=sys.stderr)

    # Account and market facts are obtained by the council from canonical raw
    # telemetry. Never substitute historical balances or a partial MT5 query.
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    lines = []
    lines.append("=" * 80)
    lines.append(f"ANTIGRAVITY x ARENA.AI LIVE STRATEGY COUNCIL BRIEFING ({now_utc})")
    lines.append("MANDATE: DUAL-MODEL SCAN (TREND-FOLLOWING + MEAN-REVERSION) ACROSS ALL 24 ASSETS")
    lines.append("=" * 80)
    lines.append("")
    lines.append("[SECTION 1: REPOSITORY REFERENCES & MANDATORY HISTORICAL SESSION CONTEXT]")
    lines.append("- Primary GitHub Repository: https://github.com/kbsingh1399/Trading_2 (Branches: main & arena/537c1eb8-trading-2)")
    lines.append("  * Canonical source and telemetry: main. Commit review recommendations to arena/537c1eb8-trading-2; verify divergence before integration.")
    try:
        import subprocess
        head_sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True, cwd=str(PROJECT_ROOT), timeout=5).strip()
        lines.append(f"  * Local source HEAD: {head_sha}; verify published main before citing deployed behavior.")
    except Exception:
        pass
    lines.append("")
    lines.append("🛑 MANDATORY OPERATOR DIRECTIVE - LINE-BY-LINE INGESTION (ZERO SKIMMING, ZERO CONTEXT AMNESIA):")
    lines.append("Read EVERY document below IN FULL before any ruling. Open your reply with a 'DOCUMENT INGESTION & GROUND TRUTH CITATION'")
    lines.append("block citing the verified state + latest timestamp of EACH. An unread file is a fatal defect, not a minor omission.")
    lines.append("- Session chat history - full narrative, past rulings, operator feedback, avoided traps, position trajectory:")
    lines.append("  https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md")
    lines.append("  Cite the newest `### Turn [...]` timestamp to prove ingestion.")
    lines.append("- Master execution protocols & invariants: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/AGENTS.md")
    lines.append("- Live order desk ledger, prior rulings, performance ledger:")
    lines.append("  https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md")
    lines.append("- Active risk context, floor defense, capacity rules:")
    lines.append("  https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md")
    lines.append("- Thinking chain protocol V2.0 - 7-stage chain, formulas, ALL 9 Heuristic Trap Rebuttals (esp. 7/8/9):")
    lines.append("  https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md")
    lines.append("- Round 2 thinking chain audit: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/reviews/ROUND2_THINKING_CHAIN_AUDIT.md")
    lines.append("- Reference implementations - verify `classify_regime`, `model1_checklist`, `model2_checklist` in source, not memory:")
    lines.append("  https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/decision_gates_v3.py  and  Terminal/dg_context.py")
    lines.append("- Live telemetry snapshot - exhaustive schema census, every top-level key and all 24 assets:")
    lines.append("  https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json")
    lines.append("  *(Publisher attempts every 60s; verify generation_id, LIVE_OBSERVATION, freshness and provenance. Stale/missing = UNAVAILABLE.)*")
    lines.append("")
    lines.append("[SECTION 2: LIVE MT5 ACCOUNT STATE & OPERATOR MANDATE ALIGNMENT]")
    lines.append("- Fetch account, active_positions, pending_orders and capacity from the canonical main snapshot above. Confirm account #5064568, USD currency and observed inventory before any ruling.")
    lines.append("- Do not infer flat inventory from a missing/failed broker query, historical desk entry or absent telemetry. Reject stale, unknown, mismatched or unverified observations.")
    lines.append("- Hard floor: 4,775.00 USD; operating buffer: 4,795.00 USD. Compute cushion and simultaneous filled/pending stop risk from observed account state.")
    lines.append("")
    lines.append("OPERATOR MANDATES & UNIFIED SYSTEM PROTOCOLS (MANDATORY ARENA COMPLIANCE):")
    lines.append("0. MANDATORY COMPLETE SESSION CHAT HISTORY REVIEW:")
    lines.append("   - Covered by the line-by-line ingestion mandate in Section 1. Both agents must be on the exact same page regarding")
    lines.append("     historical rulings, operator feedback, avoided traps, and active account trajectory before any ruling.")
    lines.append("1. CANONICAL CAPACITY & JOINT RISK DEFENSE (MAX 4 POSITIONS):")
    lines.append("   - Maximum concurrent filled positions: 4 across orthogonal asset clusters.")
    lines.append("   - Total active filled positions + resting limit orders cannot exceed capacity (max 4 tickets).")
    lines.append("   - Every resting limit order reserves full contingent stop loss risk.")
    lines.append("   - Stressed worst-case equity across all filled and pending orders must strictly preserve the 4,795.00 USD operating buffer (>= +20.00 USD cushion above 4,775.00 USD hard floor).")
    lines.append("2. PASSIVE LIMIT ORDERS ONLY:")
    lines.append("   - Any valid candidate staged MUST be an executable LIMIT ORDER (BUY LIMIT or SELL LIMIT) resting at a verified structural orderflow shelf or resting whale wall. Market orders crossing the spread are strictly prohibited.")
    lines.append("3. CONTINUOUS ACTIVE SENTRY & PRUNING:")
    lines.append("   - Unfilled resting limit orders are actively audited on every cycle. If orderbook depth/shelves remain intact and drift < 2.0x ATR, KEEP them. If thesis degrades, price drifts > 2.0x ATR, or whale wall thins > 50%, the desk immediately drops/cancels the order.")
    lines.append("4. STRONG ORDERFLOW L2/L3 DECISION MAKING:")
    lines.append("   - Decisions must NOT be random trend following or naive mean reversion. Must be strictly grounded in L2 depth, resting whale walls (>=150k USD, >=180s persistence), and CVD delta absorption.")
    lines.append("   - Use observed persist_s and presence_frac; no persistence series means UNVERIFIED. Observation age never substitutes for wall persistence.")
    lines.append("   - GENUINE L3 walls require gate_g7_eligible=true. MIRRORED_LEG and TOP_OF_BOOK are NOT net directional inventory and cannot satisfy whale backing.")
    lines.append("5. TAKE PROFIT (TP) LOGICAL ANCHORING TO LIQUIDATIONS OR STOPS:")
    lines.append("   - TP must NOT be placed at arbitrary static multiples into empty air. TP MUST anchor directly to the next structural liquidation cascade (Short Squeeze for Longs, Long Flush for Shorts) or stop-loss sweep cluster (Buy Stops for Longs, Sell Stops for Shorts).")
    lines.append("6. CONTINUOUS KAIZEN SELF-IMPROVEMENT:")
    lines.append("   - Every cycle builds on the entire session history, learning from past setbacks and operator feedback to eliminate repeat errors and sharpen execution.")
    lines.append("7. MANDATORY DUAL-ENGINE GOVERNANCE: WHEN |Z| < 2.0 SD (IN-RANGE), ACTIVELY OPT FOR TREND FOLLOWING (MODEL 2):")
    lines.append("   - Operator Directive: in-range |Z| (0.2 to 1.7) is the prime Model 2 regime, NOT a reason to stand aside. Full")
    lines.append("     mechanics in Section 4. Debate BOTH engines every cycle; stand aside only if NEITHER yields a valid structural setup.")
    lines.append("8. OPERATOR MANDATE: INTENSIVE MULTI-PERSONA DELIBERATION PROTOCOL BEFORE REPLYING:")
    lines.append("   - Operator Directive: 'ask him to do intensive discussion before replying... you can add your techniques for him... rest you are free and good luck with profitable trading.'")
    lines.append("   - Conduct and DISPLAY the 4-persona dialectic (roster in OUTPUT FORMAT below) before the ruling. Show the debate, not just its conclusion.")
    lines.append("   - Persona 4 must state explicitly that maker limits avoid SLIPPAGE but still pay the full broker spread round trip (Buy Limits")
    lines.append("     fill on Ask and exit on Bid), so the 20.00 bps spread gate and the relative-friction ceiling stay binding, and that a premature")
    lines.append("     'stand aside' must be argued down with numbers before it is accepted as the default.")
    lines.append("")

    # Audit Active Positions & Pending Orders
    lines.append("[SECTION 3: ACTIVE POSITIONS & RESTING ORDERS REVIEW]")
    lines.append("- Read actual filled positions and pending orders from the same validated snapshot generation. Report generation_id and as_of_utc with the inventory audit; treat unavailable inventory as a blocking defect.")
    lines.append("")
    lines.append("ARENA REVIEW MANDATE FOR EXISTING ORDERS:")
    lines.append("- If positions exist: Evaluate whether to HOLD, apply piecewise ratchet (Phase 0 BE at +0.80R, Phase 1 Profit Lock at +1.50R, target at +2.50R), execute emergency shelf cut, or close at market.")
    lines.append("- If resting limit orders exist: Check if supporting whale wall has thinned >50% or price has drifted >2.0x ATR. Advise KEEP or DELETE immediately.")
    lines.append("")
    lines.append("[SECTION 4: DUAL-MODEL SCAN MANDATE: TREND-FOLLOWING & MEAN-REVERSION]")
    lines.append("Antigravity Trader and Big Brain Collaborative Directive:")
    lines.append("OPERATOR MANDATE ON DUAL-ENGINE STRATEGY DEBATE:")
    lines.append("You MUST actively evaluate and debate BOTH strategy families across ALL 24 assets on every cycle:")
    lines.append("- The 200-EMA label is cosmetic, NOT the gate. decision_gates_v3.classify_regime and the enforced model-specific gates are BINDING for both engines; unavailable or stale inputs block admission.")
    lines.append("1. MODEL 1 (EXTREME MEAN-REVERSION - |Z| >= 2.0 SD):")
    lines.append("   - Applicable when price stretches to extremes (|Z| >= 2.0 SD from Session VWAP with RSI < 30 or > 70).")
    lines.append("   - Look for CVD aggressor exhaustion and resting whale wall absorption (>= 150k USD, >= 180s persistence) fading the stretch back toward VWAP.")
    lines.append("2. MODEL 2 (TREND-FOLLOWING PULLBACK - |Z| < 2.0 SD IN-RANGE):")
    lines.append("   - When |Z| is inside range (|Z| < 2.0 SD, e.g. 0.2 to 1.7 SD), this is the NATURAL ENVIRONMENT for Trend Following!")
    lines.append("   - In established trending regimes (e.g. Bearish Crypto/Forex with negative 200 EMA slope, or Bullish Commodities/USDJPY):")
    lines.append("   - Look for shallow pullbacks (0.10 to 0.60 ATR) to 20/50 EMA, Value Area shelves (VAH/VAL), or session VWAP.")
    lines.append("   - Ride orderflow momentum toward resting liquidation cascade pools (Short Squeeze / Long Flush) and stop sweeps.")
    lines.append("   - DO NOT dismiss candidates simply because |Z| < 2.0 SD! In-range |Z| is the prime signal to switch to Trend-Following.")
    lines.append("")
    lines.append("Provide the explicit BOTH-engine dialectic before the verdict (format in Section 6). Determine capital, free margin and")
    lines.append("joint-fill capacity from verified observations; stage advice only when every execution gate passes.")
    lines.append("")
    lines.append("[SECTION 5: LIVE ORDERFLOW TELEMETRY & BIDIRECTIONAL REPO LINKS]")
    lines.append("OPERATOR MANDATE: FETCH TELEMETRY DIRECTLY VIA GITHUB REPOSITORY / RAW ENDPOINTS")
    lines.append("To eliminate token bloat and maintain high-density strategic reasoning, all raw multi-timeframe footprints,")
    lines.append("orderbook ladders, whale walls, and liquidation pools are published directly in the repository:")
    lines.append("")
    lines.append("1. LIVE TELEMETRY SNAPSHOT (raw endpoint in Section 1; republished every 60s). Curl or load it in bash/python yourself -")
    lines.append("   never rely on pasted data. All 24 assets carry quotes, spreads, VWAP Z, L3 walls with persistence, liquidation bands,")
    lines.append("   stop clusters and CVD series where available.")
    lines.append("")
    lines.append("🛑 EXHAUSTIVE TELEMETRY CENSUS (NO SELECTIVE 4-FIELD SAMPLING) - per asset, report:")
    lines.append("  `execution_specs` (min/step/max_lot, contract_size, stops_level, digits, tick_size - prove lot discreteness AND stop > stops_level);")
    lines.append("  `orderbook_live_depth` (full bids_top20/asks_top20 notional, book_imbalance, skew_ratio - never top-of-book alone);")
    lines.append("  `funding_and_rates` (funding_rate_bps, mark vs index basis); `quotes` (bid/ask/mid, spread_bps, broker_tick_age_s < 5.0s);")
    lines.append("  `causal_indicators` (session_vwap_utc, session_sigma, session_bars >= 16, vwap_z_score, atr_14, rsi_14, trend_regime);")
    lines.append("  `hyperdash_flow_intelligence.summary.macro_orderflow_tilt` (BEARISH_LONG_FLUSH / BULLISH_SHORT_SQUEEZE / BALANCED) -")
    lines.append("     flag any candidate facing the prevailing tilt. NOTE: no top-level `summary` key exists; this field is nested inside")
    lines.append("     the quarantined hyperdash block and is an all-time scrape aggregate, NOT a live tilt. Cite it as such or not at all.")
    lines.append("  `whale_trades` timestamps - separate genuine directional whale views from HFT inventory grids (multi-level ladder wallets).")
    lines.append("")
    lines.append("🛑 STALE SCRAPE QUARANTINE: DISREGARD `hyperdash_flow_intelligence` as market evidence - ~13-day-old rows, corrupted")
    lines.append("  relative-time strings, zero BNB coverage. Liquidation/stop ground truth is ONLY the real-time computed")
    lines.append("  `reconstructed_liquidations`, `structural_stop_clusters`, `orderbook_live_depth`, `cvd_1m_buckets`, `quotes`.")
    lines.append("")
    lines.append("🛑 CROSS-VENUE BASIS (G-7 / A3 / B5 WALL AUDIT): `entry` is the MT5 mid that fills; `wall_price` is Binance USDM /")
    lines.append("  Hyperliquid L2/L3. Comparing them raw mixes two price scales. Per wall report ALL THREE, computed live - never reuse a")
    lines.append("  prior cycle's multiples, the basis moves and changes sign:")
    lines.append("    (a) raw MT5      d_mt5   = side * (entry_mt5 - wall_price) / atr")
    lines.append("    (b) venue-adj    d_adj   = side * (entry_mt5 - wall_price - basis) / atr,  basis = mid_mt5 - mid_binance")
    lines.append("    (c) basis in USD and in units of 0.25 ATR, PLUS its drift range over recent snapshots.")
    lines.append("  Translate a large but STABLE basis; refuse a small but JUMPING one (a basis quantised to one tick can flip 0 <-> 0.5 ATR).")
    lines.append("  Never record 'no whale exists' when authentic persistent depth is merely shifted by venue basis - distinguish skew from absence.")
    lines.append("")
    lines.append("2. BIDIRECTIONAL COLLABORATION BRANCH (TWO-WAY ARENA <-> ANTIGRAVITY COMMUNICATION):")
    lines.append("   https://github.com/kbsingh1399/Trading_2/tree/arena%2F537c1eb8-trading-2")
    lines.append("   - Review branch `arena/537c1eb8-trading-2`; canonical source and telemetry remain `main`. Verify both refs, never assume")
    lines.append("     parity. Arena may push plans, forensic reports and code here; all of it needs independent source, observation and")
    lines.append("     execution-gate review before integration or broker action.")
    lines.append("")
    lines.append("3. CORE EXECUTION ENGINE & HISTORICAL CONTEXT IMPLEMENTATIONS:")
    lines.append("   - Decision Gates V3 and the Context Builder are linked in Section 1 - read them in source, not from memory.")
    lines.append("   - Flow Feed Engine: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/Data_Factory/hyperdash_flow_feed.py")
    lines.append("")

    lines.append("[SECTION 6: REQUIRED QUANTITATIVE RULING & DUAL-TRACK GATING RULES]")
    lines.append("CRITICAL DESK UPDATES & EVOLVING EXECUTION MANDATES:")
    lines.append("1. FOCUS CAPITAL ON TIGHT-SPREAD CRYPTO MAJORS (HIGH NET EXPECTANCY):")
    lines.append("   - Enforce the 20.00 bps spread ceiling and relative-friction ceiling using actual broker Bid/Ask quotes. Rank all 24 assets from current verified observations.")
    lines.append("   - Recompute Net EV from eligible empirical calibration and observed costs; historical spreads, rankings or win rates cannot certify an edge.")
    lines.append("2. INSTITUTIONAL VWAP-CENTRIC EXECUTION & MULTI-TIMEFRAME HARMONIZATION:")
    lines.append("   - VWAP IS THE GRAVITATIONAL ANCHOR: You MUST actively evaluate price location against Session VWAP and its +/-1SD and +/-2SD bands:")
    lines.append("   - MODEL 2 (TREND-FOLLOWING PULLBACK TO VWAP / VALUE AREA):")
    lines.append("     * When HTF (4H) is in a confirmed structural trend (e.g. 4H t-stat < -1.5, 4H ER > 0.25, or negative 200 EMA slope), the HTF trend is established as BEARISH.")
    lines.append("     * A pullback on 15m/1H up into Session VWAP, Value Area High (VAH), or 20/50 EMA shelf IS THE INSTITUTIONAL ENTRY.")
    lines.append("     * Do NOT demand that 1H be expanding downward during a pullback! The pullback is the pause before trend resumption.")
    lines.append("     * A pullback into VWAP or VAH requires verified resting Ask Whale resistance, CVD buying exhaustion and all trend gates before SHORT limit advice.")
    lines.append("   - MODEL 1 (EXTREME VWAP MEAN REVERSION - |Z| >= 2.0 SD):")
    lines.append("     * When price stretches to extreme |Z| >= 2.0 SD away from Session VWAP, look for absorption fading back toward VWAP.")
    lines.append("3. TAKE PROFIT (TP) LOGICALLY ANCHORED TO ON-CHAIN LIQUIDATION TARGETS & STOPS:")
    lines.append("   - Do NOT place TP into thin air. Anchor TP directly at the nearest real structural liquidation pool or stop sweep:")
    lines.append("   - For SHORTS: Anchor TP at an observed downside long liquidation band or sell stop cluster; report source and coverage.")
    lines.append("   - For LONGS: Anchor TP at Overhead Short Squeeze Band or Buy Stop Cluster.")
    lines.append("4. EXPANDED RISK BUDGET:")
    lines.append("   - Nominal risk remains subject to current risk policy and observed joint-loss headroom. Never assume a 100+ USD cushion or allocate risk from a historical balance.")
    lines.append("")
    lines.append("OUTPUT FORMAT & DELIBERATION PROTOCOL:")
    lines.append("Part 1: INTENSIVE 4-PERSONA DELIBERATION & DIALECTIC DEBATE:")
    lines.append("  - Persona 1 (Orderflow Analyst): Evaluate live L2 depth, resting L3 whale walls (persist >= 180s), CVD taker delta, and on-chain liquidation cascades.")
    lines.append("  - Persona 2 (Position Manager): Audit observed account equity, floor defense, filled and pending inventory, joint-fill capacity, and stressed post-loss simulations.")
    lines.append("  - Persona 3 (Macro Sentry): Verify broker market hours, quote freshness and Tier-1 calendar clearance; closed or stale CFD markets are unavailable.")
    lines.append("  - Persona 4 (Devil's Advocate & Execution Realist): Vigorously evaluate Model 2 VWAP pullbacks on tight-spread crypto majors (BTC, BNB, ETH) and Model 1 extremes. Synthesize a tradeable thesis if data supports it.")
    lines.append("Part 2: QUANTITATIVE DESK RULING:")
    lines.append("  - Active positions audit: HOLD, Ratchet SL, or Exit.")
    lines.append("  - Executable LIMIT ORDER stages (Symbol, Direction, Entry limit price, Stop Loss, Take Profit anchored to liquidations/stops, Lots, Risk USD).")
    lines.append("  - If no trade passes, provide explicit mathematical rationale.")
    lines.append("")
    return "\n".join(lines)


async def get_arena_tab_ws_url() -> Optional[str]:
    """Find the Arena tab via Chrome remote debugging JSON endpoint."""
    try:
        req = urllib.request.Request(f"{CDP_HTTP_URL}/json")
        with urllib.request.urlopen(req, timeout=3) as resp:
            tabs = json.loads(resp.read().decode("utf-8"))
        for t in tabs:
            if t.get("type") == "page" and "arena.ai" in t.get("url", ""):
                return t.get("webSocketDebuggerUrl")
    except Exception as e:
        print(f"Error fetching Chrome tabs: {e}", file=sys.stderr)
    return None


async def clear_arena_prompt_box(ws) -> bool:
    """Explicitly focus the editor, select all (Ctrl+A), and delete/clear any existing prompt in the box."""
    try:
        # Step 1: Focus editor and clean TipTap & React fiber state
        focus_and_clean_js = """
        (() => {
          const el = document.querySelector('.tiptap.ProseMirror');
          if (el) el.focus();
          let editor = null;
          let p = el;
          while (p) {
            if (p.editor) { editor = p.editor; break; }
            p = p.parentElement;
          }
          if (editor) {
            editor.commands.clearContent();
          }
          const submitBtn = document.querySelector('button[aria-label="Send message"], button:has(svg.lucide-arrow-up), button:has(svg.lucide-arrow-right)');
          if (submitBtn) {
            const fiberKey = Object.keys(submitBtn).find(k => k.startsWith('__reactFiber'));
            if (fiberKey) {
              let curr = submitBtn[fiberKey];
              while (curr) {
                if (curr.memoizedProps?.onChange) {
                  curr.memoizedProps.onChange('');
                  break;
                }
                curr = curr.return;
              }
            }
          }
          return { focused: !!el };
        })()
        """
        await ws.send(json.dumps({
            "id": int(time.time() * 1000) % 1000000,
            "method": "Runtime.evaluate",
            "params": {"expression": focus_and_clean_js, "returnByValue": True}
        }))
        try:
            await asyncio.wait_for(ws.recv(), timeout=3.0)
        except Exception:
            pass

        # Step 2: Dispatch Ctrl+A (Select All)
        msg_id = int(time.time() * 1000) % 1000000
        await ws.send(json.dumps({
            "id": msg_id,
            "method": "Input.dispatchKeyEvent",
            "params": {
                "type": "rawKeyDown",
                "windowsVirtualKeyCode": 65,
                "code": "KeyA",
                "key": "a",
                "modifiers": 2
            }
        }))
        try:
            await asyncio.wait_for(ws.recv(), timeout=3.0)
        except Exception:
            pass
        await ws.send(json.dumps({
            "id": msg_id + 1,
            "method": "Input.dispatchKeyEvent",
            "params": {
                "type": "keyUp",
                "windowsVirtualKeyCode": 65,
                "code": "KeyA",
                "key": "a",
                "modifiers": 2
            }
        }))
        try:
            await asyncio.wait_for(ws.recv(), timeout=3.0)
        except Exception:
            pass

        # Step 3: Dispatch Delete & Backspace
        await ws.send(json.dumps({
            "id": msg_id + 2,
            "method": "Input.dispatchKeyEvent",
            "params": {
                "type": "rawKeyDown",
                "windowsVirtualKeyCode": 46,
                "code": "Delete",
                "key": "Delete"
            }
        }))
        try:
            await asyncio.wait_for(ws.recv(), timeout=3.0)
        except Exception:
            pass
        await ws.send(json.dumps({
            "id": msg_id + 3,
            "method": "Input.dispatchKeyEvent",
            "params": {
                "type": "keyUp",
                "windowsVirtualKeyCode": 46,
                "code": "Delete",
                "key": "Delete"
            }
        }))
        try:
            await asyncio.wait_for(ws.recv(), timeout=3.0)
        except Exception:
            pass
        await asyncio.sleep(0.05)
        return True
    except Exception as e:
        print(f"Error in clear_arena_prompt_box: {e}", file=sys.stderr)
        return False


def format_prompt_for_tiptap_html(md: str) -> str:
    """
    Converts plain text/markdown prompts into structured HTML nodes
    that TipTap ProseMirror natively parses into headings, bullet lists,
    and distinct paragraphs, preventing unformatted single-paragraph collapse.
    """
    lines = md.split('\n')
    html_parts = []
    in_list = False
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            continue
        
        # Heading 1, 2, 3 or PART X / MANDATE X / STEP X
        if stripped.startswith('# '):
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            html_parts.append(f'<h2><strong>{stripped[2:]}</strong></h2>')
        elif stripped.startswith('## ') or stripped.startswith('### ') or stripped.startswith('PART ') or stripped.startswith('MANDATE ') or stripped.startswith('STEP ') or stripped.startswith('TRADING DESK'):
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            title = stripped.lstrip('#').strip()
            html_parts.append(f'<h3><strong>{title}</strong></h3>')
        # Bullets
        elif stripped.startswith('• ') or stripped.startswith('- ') or stripped.startswith('* '):
            if not in_list:
                html_parts.append('<ul>')
                in_list = True
            item_text = stripped[2:]
            html_parts.append(f'<li><p>{item_text}</p></li>')
        else:
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            html_parts.append(f'<p>{stripped}</p>')
            
    if in_list:
        html_parts.append('</ul>')
    return ''.join(html_parts)


async def post_prompt_to_arena(prompt_text: str) -> bool:
    """Clear any existing prompt in the box (Ctrl+A then Delete), inject prompt with rich HTML formatting, and hit enter."""
    ws_url = await get_arena_tab_ws_url()
    if not ws_url:
        print("ERROR: No active Arena tab found in Chrome at localhost:9222", file=sys.stderr)
        return False

    try:
        async with websockets.connect(ws_url, max_size=20_000_000) as ws:
            # 0. Bring tab to front to unthrottle execution
            await ws.send(json.dumps({"id": 100, "method": "Page.bringToFront"}))
            try:
                await asyncio.wait_for(ws.recv(), timeout=3.0)
            except Exception:
                pass

            # 1. MANDATORY CLEAR: Remove any previous prompt already in the box (Ctrl+A then Delete)
            await clear_arena_prompt_box(ws)
            await asyncio.sleep(0.1)

            prompt_html = format_prompt_for_tiptap_html(prompt_text)

            # 2. Inject structured HTML into TipTap editor and update React state
            js_set = f"""
            (async () => {{
              const submitBtn = document.querySelector('button[aria-label="Send message"], button:has(svg.lucide-arrow-up), button:has(svg.lucide-arrow-right)');
              if (!submitBtn) return {{ error: 'No submit button found' }};

              const fiberKey = Object.getOwnPropertyNames(submitBtn).find(k => k.startsWith('__reactFiber')) || Object.keys(submitBtn).find(k => k.startsWith('__reactFiber'));
              if (!fiberKey) return {{ error: 'No react fiber on submit button' }};

              let curr = submitBtn[fiberKey];
              let targetFiber = null;
              while (curr) {{
                if (curr.memoizedProps?.onSubmit && curr.memoizedProps?.onChange) {{
                  targetFiber = curr;
                  break;
                }}
                curr = curr.return;
              }}
              if (!targetFiber) return {{ error: 'Target fiber not found' }};

              const promptText = {json.dumps(prompt_text)};
              const promptHtml = {json.dumps(prompt_html)};
              targetFiber.memoizedProps.onChange(promptText);

              const el = document.querySelector('.tiptap.ProseMirror');
              let editor = null;
              let p = el;
              while (p) {{
                if (p.editor) {{ editor = p.editor; break; }};
                p = p.parentElement;
              }}
              if (editor) {{
                editor.commands.setContent(promptHtml);
              }}

              return {{ success: true }};
            }})()
            """
            msg_id = int(time.time() * 1000) % 1000000
            await ws.send(json.dumps({
                "id": msg_id,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": js_set,
                    "returnByValue": True,
                    "awaitPromise": True
                }
            }))
            resp_str = await ws.recv()
            resp = json.loads(resp_str)
            res_val = resp.get("result", {}).get("result", {}).get("value", {})
            if not res_val.get("success"):
                print(f"CDP prompt injection returned: {res_val}", file=sys.stderr)
                return False

            # Wait 200ms for React propagation
            await asyncio.sleep(0.2)

            # 3. Hit Enter via CDP key event
            await ws.send(json.dumps({
                "id": msg_id + 1,
                "method": "Input.dispatchKeyEvent",
                "params": {
                    "type": "rawKeyDown",
                    "windowsVirtualKeyCode": 13,
                    "code": "Enter",
                    "key": "Enter"
                }
            }))
            await ws.recv()
            await ws.send(json.dumps({
                "id": msg_id + 2,
                "method": "Input.dispatchKeyEvent",
                "params": {
                    "type": "keyUp",
                    "windowsVirtualKeyCode": 13,
                    "code": "Enter",
                    "key": "Enter"
                }
            }))
            await ws.recv()

            # Failsafe submit click / onSubmit trigger
            js_submit = """
            (async () => {
              const el = document.querySelector('.tiptap.ProseMirror');
              if (el) el.focus();
              const submitBtn = document.querySelector('button[aria-label="Send message"], button:has(svg.lucide-arrow-up), button:has(svg.lucide-arrow-right)');
              if (!submitBtn) return { error: 'No submit button' };

              if (!submitBtn.disabled) {
                submitBtn.click();
                return { submitted: true, method: 'click' };
              }

              const fiberKey = Object.keys(submitBtn).find(k => k.startsWith('__reactFiber'));
              if (fiberKey) {
                let curr = submitBtn[fiberKey];
                while (curr) {
                  if (curr.memoizedProps?.onSubmit && curr.memoizedProps?.onChange) {
                    try {
                      curr.memoizedProps.onSubmit();
                      return { submitted: true, method: 'fiber_onSubmit' };
                    } catch(e) {}
                  }
                  curr = curr.return;
                }
              }

              return { submitted: false, error: 'Disabled and no fiber onSubmit' };
            })()
            """
            await ws.send(json.dumps({
                "id": msg_id + 3,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": js_submit,
                    "returnByValue": True,
                    "awaitPromise": True
                }
            }))
            await ws.recv()

            await asyncio.sleep(0.3)
            print("Prompt posted successfully to Arena.ai (box cleared first with Ctrl+A Delete, prompt set, Enter hit)!")
            return True
    except Exception as e:
        print(f"Error posting prompt over CDP: {e}", file=sys.stderr)
        return False


async def dismiss_arena_popup() -> bool:
    """Send Escape key via CDP to dismiss any 'Was this task successful?' modal popup."""
    ws_url = await get_arena_tab_ws_url()
    if not ws_url:
        return False
    try:
        async with websockets.connect(ws_url, max_size=10_000_000) as ws:
            msg_down = {
                "id": int(time.time()),
                "method": "Input.dispatchKeyEvent",
                "params": {
                    "type": "rawKeyDown",
                    "windowsVirtualKeyCode": 27,
                    "code": "Escape",
                    "key": "Escape"
                }
            }
            await ws.send(json.dumps(msg_down))
            await ws.recv()
            msg_up = {
                "id": int(time.time()) + 1,
                "method": "Input.dispatchKeyEvent",
                "params": {
                    "type": "keyUp",
                    "windowsVirtualKeyCode": 27,
                    "code": "Escape",
                    "key": "Escape"
                }
            }
            await ws.send(json.dumps(msg_up))
            await ws.recv()
            return True
    except Exception as e:
        print(f"Error dismissing popup: {e}", file=sys.stderr)
        return False


async def dismiss_zai_popup() -> bool:
    """Send Escape key via CDP and execute DOM close to dismiss any high-traffic 'switch model' modal popup on Z.ai."""
    ws_url = await get_zai_tab_ws_url()
    if not ws_url:
        return False
    try:
        async with websockets.connect(ws_url, max_size=10_000_000) as ws:
            msg_id = int(time.time() * 1000) % 1000000
            for ktype, vk in [("rawKeyDown", 27), ("keyUp", 27)]:
                await ws.send(json.dumps({
                    "id": msg_id,
                    "method": "Input.dispatchKeyEvent",
                    "params": {
                        "type": ktype,
                        "windowsVirtualKeyCode": vk,
                        "code": "Escape",
                        "key": "Escape"
                    }
                }))
                msg_id += 1
                try:
                    await asyncio.wait_for(ws.recv(), timeout=2.0)
                except Exception:
                    pass
            js_close = """
            (() => {
              const modal = document.querySelector('div[role="dialog"], .modal, [class*="dialog"], [class*="popup"], [class*="modal"]');
              if (modal) {
                window.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', code: 'Escape', keyCode: 27, which: 27, bubbles: true }));
                window.dispatchEvent(new KeyboardEvent('keyup', { key: 'Escape', code: 'Escape', keyCode: 27, which: 27, bubbles: true }));
                const closeBtn = modal.querySelector('button[aria-label*="close" i], button.close, button[title*="close" i], button:has(svg.lucide-x)');
                if (closeBtn) closeBtn.click();
              }
              return true;
            })()
            """
            await ws.send(json.dumps({
                "id": msg_id,
                "method": "Runtime.evaluate",
                "params": {"expression": js_close, "returnByValue": True}
            }))
            try:
                await asyncio.wait_for(ws.recv(), timeout=2.0)
            except Exception:
                pass
            return True
    except Exception as e:
        print(f"Error dismissing Z.ai popup: {e}", file=sys.stderr)
        return False


async def check_arena_response() -> Tuple[bool, str]:
    """Check if Arena has completed responding and extract the full response text."""
    await dismiss_arena_popup()
    ws_url = await get_arena_tab_ws_url()
    if not ws_url:
        return False, "No active Arena tab"

    js_code = """
    (() => {
      // Check if generation is still active
      const stopBtn = document.querySelector('button[aria-label="Stop generating"], button:has(svg.lucide-square)');
      const isGenerating = !!stopBtn;

      // Extract all prose elements
      const proseElements = Array.from(document.querySelectorAll('.prose')).filter(el => !el.classList.contains('tiptap'));
      const lastText = proseElements.length > 0 ? proseElements[proseElements.length - 1].innerText : '';

      return {
        isGenerating: isGenerating,
        lastText: lastText,
        count: proseElements.length
      };
    })()
    """

    try:
        async with websockets.connect(ws_url, max_size=10_000_000) as ws:
            msg = {
                "id": int(time.time()),
                "method": "Runtime.evaluate",
                "params": {
                    "expression": js_code,
                    "returnByValue": True,
                    "awaitPromise": True
                }
            }
            await ws.send(json.dumps(msg))
            resp_str = await ws.recv()
            resp = json.loads(resp_str)
            val = resp.get("result", {}).get("result", {}).get("value", {})
            is_gen = val.get("isGenerating", False)
            text = val.get("lastText", "")
            return not is_gen and len(text) > 50, text
    except Exception as e:
        return False, str(e)


def run_full_15m_cycle():
    """
    Execute the canonical 13th/15th minute cycle:
    1. Dismiss any existing popup.
    2. Generate fresh 48h footprint & telemetry prompt.
    3. Post to Arena.ai and hit submit.
    4. Sleep for 2 minutes (120s) while Arena computes.
    5. Dismiss completion popup via Escape.
    6. Extract response and evaluate against orderflow data.
    """
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] Initiating 13th-minute Arena.ai cycle...")
    asyncio.run(dismiss_arena_popup())

    p = build_48h_orderflow_prompt()
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] Posting 48h footprint prompt to Arena.ai ({len(p)} chars)...")
    posted = asyncio.run(post_prompt_to_arena(p))
    if not posted:
        print("ERROR: Failed to post prompt to Arena.ai", file=sys.stderr)
        return False

    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] Prompt submitted. Sleeping 120s (2 min) for Arena.ai Big Brain reasoning...")
    time.sleep(120)

    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] 15th-minute wake-up: Checking Arena.ai response...")
    asyncio.run(dismiss_arena_popup())
    done, resp_text = asyncio.run(check_arena_response())
    asyncio.run(dismiss_arena_popup())

    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] Arena Generation Done: {done} | Response Length: {len(resp_text)} chars")
    print("--- ARENA.AI FULL RESPONSE ---")
    print(resp_text)
    print("------------------------------")

    # Append to docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md
    desk_path = PROJECT_ROOT / "docs" / "trade_plans" / "LIVE_COLLABORATIVE_ORDER_DESK.md"
    if done and desk_path.exists() and len(resp_text) > 50:
        now_dt = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        
        # Determine next section number
        import re
        content = desk_path.read_text(encoding="utf-8")
        matches = re.findall(r"## Section (\d+):", content)
        next_sec = max([int(m) for m in matches]) + 1 if matches else 44

        section_entry = f"\n\n---\n\n## Section {next_sec}: Autonomous Arena.ai Big Brain Evaluation & Telemetry Audit | {now_dt}\n\n"
        section_entry += f"### 1. Cycle Trigger & Submission Details\n"
        section_entry += f"- **Mode**: Autonomous 13m/15m Collaborative Cycle (`arena_bridge.py`)\n"
        section_entry += "- **Status**: Completed council response received. Account, inventory, capacity and execution remain unverified by this dispatcher.\n\n"
        section_entry += f"### 2. Arena.ai Ruling & Quantitative Synthesis\n"
        section_entry += f"```text\n{resp_text}\n```\n\n"
        section_entry += f"### 3. Antigravity Verification & Action Plan\n"
        if "PUNCH NONE" in resp_text or "DEFENSIVE HOLD" in resp_text:
            section_entry += "- **Council Advice**: **PUNCH NONE / DEFENSIVE HOLD**; independent gate and account verification required.\n"
        else:
            section_entry += "- **Council Advice**: Review the response against observed data and execution gates before accepting any proposal.\n"

        with open(desk_path, "a", encoding="utf-8") as f:
            f.write(section_entry)
        print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] Appended Section {next_sec} to LIVE_COLLABORATIVE_ORDER_DESK.md.")

    return done, resp_text


async def get_zai_tab_ws_url() -> Optional[str]:
    """Find the Z.ai Chat tab via Chrome remote debugging JSON endpoint."""
    try:
        req = urllib.request.Request(f"{CDP_HTTP_URL}/json")
        with urllib.request.urlopen(req, timeout=3) as resp:
            tabs = json.loads(resp.read().decode("utf-8"))
        for t in tabs:
            if t.get("type") == "page" and "chat.z.ai" in t.get("url", ""):
                return t.get("webSocketDebuggerUrl")
    except Exception as e:
        print(f"Error fetching Chrome tabs for Z.ai: {e}", file=sys.stderr)
    return None


async def inspect_zai_dom() -> Dict[str, Any]:
    """Inspect the Z.ai Chat tab DOM structure and extract current conversation text."""
    ws_url = await get_zai_tab_ws_url()
    if not ws_url:
        return {"error": "No active Z.ai tab found on port 9222"}
    js_code = """
    (() => {
      const inputs = Array.from(document.querySelectorAll('textarea, [contenteditable="true"], input[type="text"]')).map(el => ({
        tag: el.tagName,
        id: el.id,
        className: el.className,
        placeholder: el.getAttribute('placeholder') || el.getAttribute('aria-label') || '',
        valueLen: (el.value || el.innerText || '').length
      }));
      const buttons = Array.from(document.querySelectorAll('button')).map(b => ({
        id: b.id,
        text: (b.innerText || '').trim().slice(0, 40),
        aria: b.getAttribute('aria-label') || '',
        title: b.getAttribute('title') || '',
        type: b.getAttribute('type') || '',
        disabled: b.disabled,
        className: (b.className || '').slice(0, 80)
      }));
      const msgContainers = Array.from(document.querySelectorAll('.prose, .markdown-prose, [class*="markdown"], [class*="message-content"], [id^="message-"]')).map(el => ({
        tag: el.tagName,
        id: el.id,
        className: (el.className || '').slice(0, 80),
        textLen: (el.innerText || '').trim().length,
        textPreview: (el.innerText || '').trim().slice(0, 400)
      })).filter(m => m.textLen > 20);
      const allMessageDivs = Array.from(document.querySelectorAll('[id^="message-"]')).map(el => ({
        id: el.id,
        className: (el.className || '').slice(0, 80),
        textLen: (el.innerText || '').trim().length,
        textPreview: (el.innerText || '').trim().slice(0, 300),
        htmlPreview: (el.innerHTML || '').trim().slice(0, 1500)
      }));
      const ta = document.querySelector('textarea#chat-input') || document.querySelector('textarea');
      const formEl = ta ? (ta.closest('form') || (ta.parentElement && ta.parentElement.parentElement && ta.parentElement.parentElement.parentElement)) : null;
      const chatInputButtons = formEl ? Array.from(formEl.querySelectorAll('button')).map(b => ({
        id: b.id,
        text: (b.innerText || '').trim(),
        aria: b.getAttribute('aria-label') || '',
        title: b.getAttribute('title') || '',
        className: b.className || '',
        html: b.outerHTML.slice(0, 400)
      })) : [];
      return {
        title: document.title,
        url: location.href,
        inputs,
        chatInputButtons,
        buttons: buttons.slice(-30),
        msgCount: msgContainers.length,
        allMessageDivs: allMessageDivs.slice(-6),
        msgContainers: msgContainers.slice(-6),
        lastFullText: msgContainers.length > 0 ? (Array.from(document.querySelectorAll('.prose, .markdown-prose, [class*="markdown"], [class*="message-content"], [id^="message-"]')).filter(e => (e.innerText || '').trim().length > 20).pop().innerText || '') : (document.body ? document.body.innerText.slice(-4000) : '')
      };
    })()
    """
    async with websockets.connect(ws_url, max_size=20_000_000) as ws:
        await ws.send(json.dumps({
            "id": int(time.time()),
            "method": "Runtime.evaluate",
            "params": {"expression": js_code, "returnByValue": True, "awaitPromise": True}
        }))
        resp = json.loads(await ws.recv())
        return resp.get("result", {}).get("result", {}).get("value", {})


async def post_prompt_to_zai(prompt_text: str) -> bool:
    """Inject prompt into Z.ai Chat (textarea#chat-input) via CDP Input.insertText and click button#send-message-button."""
    ws_url = await get_zai_tab_ws_url()
    if not ws_url:
        print("WARNING: No active Z.ai Chat tab found in Chrome at 127.0.0.1:9222", file=sys.stderr)
        return False

    try:
        async with websockets.connect(ws_url, max_size=20_000_000) as ws:
            # 0. Bring tab to front to unthrottle execution
            await ws.send(json.dumps({"id": 99, "method": "Page.bringToFront"}))
            try:
                await asyncio.wait_for(ws.recv(), timeout=3.0)
            except Exception:
                pass

            msg_id = int(time.time() * 1000) % 1000000
            # Step 1: If a previous Z.ai generation is hung (Stop button active instead of #send-message-button), click Stop first, then focus and clear textarea#chat-input
            js_focus = """
            (async () => {
              const sendBtn = document.querySelector('button#send-message-button');
              if (!sendBtn) {
                const stopSquare = document.querySelector('button span.size-3.rounded-xs, button[aria-label*="Stop"], button[title*="Stop"]');
                const stopBtn = stopSquare ? (stopSquare.closest('button') || stopSquare) : null;
                if (stopBtn) {
                  stopBtn.click();
                  await new Promise(r => setTimeout(r, 700));
                }
              }
              const ta = document.querySelector('textarea#chat-input') || document.querySelector('textarea');
              if (!ta) return { error: 'No textarea#chat-input found on Z.ai' };
              ta.focus();
              const nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value')?.set;
              if (nativeSetter) {
                nativeSetter.call(ta, '');
              } else {
                ta.value = '';
              }
              ta.dispatchEvent(new InputEvent('input', { bubbles: true, data: '', inputType: 'deleteContentBackward' }));
              return { focused: true };
            })()
            """
            await ws.send(json.dumps({
                "id": msg_id,
                "method": "Runtime.evaluate",
                "params": {"expression": js_focus, "returnByValue": True, "awaitPromise": True}
            }))
            try:
                r1_str = await asyncio.wait_for(ws.recv(), timeout=5.0)
                r1 = json.loads(r1_str)
                v1 = r1.get("result", {}).get("result", {}).get("value", {})
                if v1.get("error"):
                    print(f"Z.ai focus error: {v1}", file=sys.stderr)
                    return False
            except Exception as e:
                print(f"Z.ai focus recv timeout/error: {e}", file=sys.stderr)

            # Step 2: Insert text via CDP Input.insertText so Svelte updates reactive state
            await ws.send(json.dumps({
                "id": msg_id + 1,
                "method": "Input.insertText",
                "params": {"text": prompt_text}
            }))
            try:
                await asyncio.wait_for(ws.recv(), timeout=5.0)
            except Exception:
                pass
            await asyncio.sleep(0.35)

            # Step 3: Verify value and click button#send-message-button with Esc/Retry resilience
            # Operator Invariant: Under high traffic, Z.ai pops up a "switch model" modal.
            # When that popup comes: hit Escape to dismiss the modal, wait 350ms, and hit Send again (2-3 attempts).
            registered = False
            for retry in range(4):
                js_send = f"""
                (async () => {{
                  const curTa = document.querySelector('textarea#chat-input') || document.querySelector('textarea');
                  // If textarea is already emptied, prompt was accepted and registered!
                  if (curTa && curTa.value.length === 0) {{
                    return {{ registered: true, remainingLen: 0 }};
                  }}

                  // Check if high-traffic "switch model" modal/popup is visible:
                  const modal = document.querySelector('div[role="dialog"], .modal, [class*="dialog"], [class*="popup"], [class*="modal"]');
                  if (modal) {{
                    window.dispatchEvent(new KeyboardEvent('keydown', {{ key: 'Escape', code: 'Escape', keyCode: 27, which: 27, bubbles: true }}));
                    window.dispatchEvent(new KeyboardEvent('keyup', {{ key: 'Escape', code: 'Escape', keyCode: 27, which: 27, bubbles: true }}));
                    const closeBtn = modal.querySelector('button[aria-label*="close" i], button.close, button[title*="close" i], button:has(svg.lucide-x)');
                    if (closeBtn) closeBtn.click();
                    await new Promise(r => setTimeout(r, 350));
                  }}

                  // Re-ensure textarea value is intact if lost
                  if (curTa && (!curTa.value || curTa.value.length < 20)) {{
                    const nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value')?.set;
                    if (nativeSetter) nativeSetter.call(curTa, {json.dumps(prompt_text)});
                    else curTa.value = {json.dumps(prompt_text)};
                    curTa.dispatchEvent(new InputEvent('input', {{ bubbles: true, data: {json.dumps(prompt_text[:64])}, inputType: 'insertText' }}));
                    curTa.dispatchEvent(new Event('change', {{ bubbles: true }}));
                    await new Promise(r => setTimeout(r, 200));
                  }}

                  const sendBtn = document.querySelector('button#send-message-button') || document.querySelector('button.sendMessageButton') || document.querySelector('button[type="submit"]');
                  if (sendBtn && !sendBtn.disabled) {{
                    sendBtn.click();
                    await new Promise(r => setTimeout(r, 450));
                  }}

                  const checkTa = document.querySelector('textarea#chat-input') || document.querySelector('textarea');
                  const isEmptied = checkTa ? checkTa.value.length === 0 : false;
                  return {{
                    registered: isEmptied,
                    remainingLen: checkTa ? checkTa.value.length : -1,
                    hadModal: !!modal
                  }};
                }})()
                """
                await ws.send(json.dumps({
                    "id": msg_id + 10 + retry * 4,
                    "method": "Runtime.evaluate",
                    "params": {"expression": js_send, "returnByValue": True, "awaitPromise": True}
                }))
                val = {}
                try:
                    resp_str = await asyncio.wait_for(ws.recv(), timeout=8.0)
                    resp = json.loads(resp_str)
                    val = resp.get("result", {}).get("result", {}).get("value", {})
                except Exception as e:
                    print(f"Z.ai send attempt {retry+1} error: {e}", file=sys.stderr)

                if val.get("registered"):
                    print(f"Prompt posted successfully to Z.ai Chat (click_send_verified, attempt {retry+1})!")
                    registered = True
                    break

                # If still not emptied, hit CDP Escape to dismiss any high-traffic popup and retry
                print(f"Z.ai traffic popup / un-registered prompt (remaining={val.get('remainingLen')}, hadModal={val.get('hadModal')}) - hitting Esc and retrying send button...", file=sys.stderr)
                for ktype, vk in [("rawKeyDown", 27), ("keyUp", 27)]:
                    await ws.send(json.dumps({
                        "id": msg_id + 100 + retry * 4,
                        "method": "Input.dispatchKeyEvent",
                        "params": {"type": ktype, "windowsVirtualKeyCode": vk, "code": "Escape", "key": "Escape"}
                    }))
                    try:
                        await asyncio.wait_for(ws.recv(), timeout=2.0)
                    except Exception:
                        pass
                await asyncio.sleep(0.4)

            if not registered:
                # Failsafe: dispatch Enter key via CDP
                await ws.send(json.dumps({
                    "id": msg_id + 99,
                    "method": "Input.dispatchKeyEvent",
                    "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"}
                }))
                try:
                    await asyncio.wait_for(ws.recv(), timeout=2.0)
                except Exception:
                    pass
                await ws.send(json.dumps({
                    "id": msg_id + 100,
                    "method": "Input.dispatchKeyEvent",
                    "params": {"type": "keyUp", "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"}
                }))
                try:
                    await asyncio.wait_for(ws.recv(), timeout=2.0)
                except Exception:
                    pass
            return True
    except Exception as e:
        print(f"Error posting prompt to Z.ai over CDP: {e}", file=sys.stderr)
        return False


async def check_zai_response() -> Tuple[bool, str]:
    """Check if Z.ai Chat has finished generating and extract BOTH the chat response AND any attached output file / workspace preview."""
    ws_url = await get_zai_tab_ws_url()
    if not ws_url:
        return False, "No active Z.ai tab"

    js_code = """
    (async () => {
      const stopBtn = document.querySelector('button[aria-label*="Stop"], button[title*="Stop"], button.stop-button');
      const stopSquare = document.querySelector('button span.size-3.rounded-xs');
      const sendBtn = document.querySelector('button#send-message-button');
      const isGenerating = Boolean(stopBtn) || Boolean(stopSquare) || !sendBtn;

      const allChatMsgs = Array.from(document.querySelectorAll('.chat-assistant.markdown-prose'));
      const lastChatEl = allChatMsgs.length > 0 ? allChatMsgs[allChatMsgs.length - 1] : null;
      const chatText = lastChatEl ? (lastChatEl.innerText || '').trim() : '';

      let workspaceFileName = '';
      let workspaceFileText = '';

      if (!isGenerating && lastChatEl) {
        const outer = lastChatEl.parentElement && lastChatEl.parentElement.parentElement ? lastChatEl.parentElement.parentElement : lastChatEl;
        const wroteBtns = Array.from(outer.querySelectorAll('button')).filter(b => (b.innerText || '').includes('Wrote'));
        for (const wb of wroteBtns) {
          const container = wb.parentElement && wb.parentElement.parentElement ? wb.parentElement.parentElement : wb.parentElement;
          if (container && !container.querySelector('.ToolCallTraceList')) {
            wb.click();
            await new Promise(r => setTimeout(r, 300));
          }
        }
        const createBtns = Array.from(outer.querySelectorAll('.ToolCallTraceList button, button')).filter(b => (b.innerText || '').includes('Create File') && (b.innerText || '').includes('.md'));
        if (createBtns.length > 0) {
          const latestCreateBtn = createBtns[createBtns.length - 1];
          const rawLabel = (latestCreateBtn.innerText || '').trim();
          const match = rawLabel.match(/([A-Za-z0-9_.-]+\\.md)/);
          const targetFile = match ? match[1] : '';
          const curHeader = Array.from(document.querySelectorAll('.text-sm.flex-1.truncate.line-clamp-1')).map(e => (e.innerText || '').trim()).find(t => t.endsWith('.md')) || '';
          if (targetFile && curHeader !== targetFile) {
            latestCreateBtn.click();
            await new Promise(r => setTimeout(r, 500));
          }
          if (targetFile) workspaceFileName = targetFile;
        }
        if (!workspaceFileName) {
          const curHeader = Array.from(document.querySelectorAll('.text-sm.flex-1.truncate.line-clamp-1')).map(e => (e.innerText || '').trim()).find(t => t.endsWith('.md')) || '';
          if (curHeader) workspaceFileName = curHeader;
        }
        const cm = document.querySelector('.cm-content');
        if (cm && cm.cmView) {
          let v = cm.cmView;
          while (v && !v.state && v.parent) v = v.parent;
          if (v && v.view && v.view.state) workspaceFileText = v.view.state.doc.toString();
          else if (v && v.state) workspaceFileText = v.state.doc.toString();
        }
        if (!workspaceFileText) {
          const wsProse = document.querySelector('.workspaceContent .markdown-prose, .workspace .markdown-prose, .workspaceContent pre');
          if (wsProse) {
            workspaceFileText = (wsProse.innerText || '').trim();
          }
        }
      }

      return {
        isGenerating,
        proseCount: allChatMsgs.length,
        chatText,
        workspaceFileName,
        workspaceFileLen: workspaceFileText.length,
        workspaceFileText
      };
    })()
    """
    try:
        async with websockets.connect(ws_url, max_size=50_000_000) as ws:
            await ws.send(json.dumps({
                "id": int(time.time()),
                "method": "Runtime.evaluate",
                "params": {"expression": js_code, "returnByValue": True, "awaitPromise": True}
            }))
            resp = json.loads(await ws.recv())
            val = resp.get("result", {}).get("result", {}).get("value", {})
            is_gen = val.get("isGenerating", False)
            chat_text = val.get("chatText", "")
            ws_name = (val.get("workspaceFileName") or "").strip()
            ws_text = val.get("workspaceFileText", "")

            combined = chat_text
            if ws_text:
                combined += f"\n\n================================================================================\n"
                combined += f"Z.AI ATTACHED OUTPUT FILE: {ws_name} ({len(ws_text)} chars)\n"
                combined += f"================================================================================\n\n"
                combined += ws_text
                attach_path = PROJECT_ROOT / "docs" / "trade_plans" / "ZAI_LATEST_ATTACHMENT.md"
                attach_path.parent.mkdir(parents=True, exist_ok=True)
                attach_path.write_text(ws_text, encoding="utf-8")
                if ws_name and ws_name.endswith(".md") and "/" not in ws_name and "\\" not in ws_name:
                    named_path = PROJECT_ROOT / "docs" / "trade_plans" / ws_name
                    named_path.write_text(ws_text, encoding="utf-8")

            raw_path = PROJECT_ROOT / "docs" / "trade_plans" / "ZAI_LATEST_RAW.md"
            if combined:
                raw_path.parent.mkdir(parents=True, exist_ok=True)
                raw_path.write_text(combined, encoding="utf-8")

            return (not is_gen and len(chat_text) > 100), combined
    except Exception as e:
        return False, str(e)



async def inspect_zai_files() -> Dict[str, Any]:
    """Inspect file cards, download/preview buttons, and workspace panel on Z.ai Chat."""
    ws_url = await get_zai_tab_ws_url()
    if not ws_url:
        return {"error": "No active Z.ai tab"}
    js_code = """
    (async () => {
      // Find all file cards / download buttons / preview buttons
      const dlBtns = Array.from(document.querySelectorAll('button[title="Download file"], button[title="Open in Workspace"], a[download], [class*="file"], [class*="artifact"], [class*="workspace"]'));
      const btnDetails = dlBtns.slice(-20).map(el => ({
        tag: el.tagName,
        title: el.getAttribute('title') || '',
        text: (el.innerText || '').trim().slice(0, 100),
        href: el.getAttribute('href') || '',
        className: (el.className || '').slice(0, 80),
        parentText: el.parentElement ? (el.parentElement.innerText || '').trim().slice(0, 200) : '',
        grandParentHtml: el.parentElement && el.parentElement.parentElement ? el.parentElement.parentElement.outerHTML.slice(0, 600) : ''
      }));

      // Click the latest "Preview" / "Open in Workspace" button if present to open the file content in the DOM!
      const previewBtns = Array.from(document.querySelectorAll('button[title="Open in Workspace"]'));
      let clickedPreview = false;
      if (previewBtns.length > 0) {
        previewBtns[previewBtns.length - 1].click();
        clickedPreview = true;
        await new Promise(r => setTimeout(r, 800));
      }

      // Check if a workspace / preview drawer opened in the DOM
      const allProses = Array.from(document.querySelectorAll('.markdown-prose, .prose, pre, code, [class*="preview"], [class*="workspace"], [class*="editor"]')).map(el => ({
        tag: el.tagName,
        className: (el.className || '').slice(0, 80),
        len: (el.innerText || '').trim().length,
        preview: (el.innerText || '').trim().slice(0, 300)
      })).filter(x => x.len > 200);

      return {
        clickedPreview,
        previewBtnCount: previewBtns.length,
        btnDetails,
        largeBlocks: allProses.slice(-10)
      };
    })()
    """
    async with websockets.connect(ws_url, max_size=50_000_000) as ws:
        await ws.send(json.dumps({
            "id": int(time.time()),
            "method": "Runtime.evaluate",
            "params": {"expression": js_code, "returnByValue": True, "awaitPromise": True}
        }))
        resp = json.loads(await ws.recv())
        return resp.get("result", {}).get("result", {}).get("value", {})


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "prompt-only":
        p = build_48h_orderflow_prompt()
        print(p)
    elif len(sys.argv) > 1 and sys.argv[1] == "post":
        asyncio.run(dismiss_arena_popup())
        p = build_48h_orderflow_prompt()
        success = asyncio.run(post_prompt_to_arena(p))
        sys.exit(0 if success else 1)
    elif len(sys.argv) > 1 and sys.argv[1] == "check":
        asyncio.run(dismiss_arena_popup())
        done, text = asyncio.run(check_arena_response())
        asyncio.run(dismiss_arena_popup())
        print(f"Done: {done}\nText Length: {len(text)}\nResponse:\n{text}")
    elif len(sys.argv) > 1 and sys.argv[1] == "check-zai":
        done, text = asyncio.run(check_zai_response())
        print(f"Z.ai Done: {done}\nText Length: {len(text)}\nResponse:\n{text}")
    elif len(sys.argv) > 1 and sys.argv[1] == "inspect-zai":
        info = asyncio.run(inspect_zai_dom())
        print(json.dumps(info, indent=2))
    elif len(sys.argv) > 1 and sys.argv[1] == "inspect-zai-files":
        info = asyncio.run(inspect_zai_files())
        print(json.dumps(info, indent=2))
    elif len(sys.argv) > 1 and sys.argv[1] == "dismiss-popup":
        success = asyncio.run(dismiss_arena_popup())
        print("Popup dismissed:", success)
    elif len(sys.argv) > 1 and sys.argv[1] == "clear-box":
        async def do_clear():
            ws_url = await get_arena_tab_ws_url()
            if ws_url:
                async with websockets.connect(ws_url, max_size=10_000_000) as ws:
                    await clear_arena_prompt_box(ws)
                    print("Prompt box cleared successfully.")
            else:
                print("No Arena tab found.")
        asyncio.run(do_clear())
    elif len(sys.argv) > 1 and sys.argv[1] == "cycle":
        run_full_15m_cycle()
    else:
        print("Usage: python arena_bridge.py [prompt-only | post | check | check-zai | inspect-zai | inspect-zai-files | clear-box | dismiss-popup | cycle]")


if __name__ == "__main__":
    main()



