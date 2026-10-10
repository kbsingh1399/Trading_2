"""Terminal/dg_context.py -- Build validated execution context for Decision Gates V3.
Pure, deterministic, dependency-light. Maps live telemetry and MT5 bars
into the exact contract required by model1_checklist and model2_checklist.
"""
from __future__ import annotations

import math
import time as _time_mod
from Terminal.policy import HTF_STRATEGY_MIN
from Terminal.Asset_Universe import canonical_asset
from typing import Dict, List, Optional, Tuple
import numpy as np

from Terminal.decision_gates_v3 import (
    yang_zhang_sigma,
    pullback_geometry,
    classify_regime,
    model1_checklist,
    model2_checklist,
    m1_range_override_ok,
    Verdict,
)


def _arr(x) -> np.ndarray:
    return np.asarray(x, dtype=float)


def _finite_number(value):
    return (not isinstance(value, bool) and isinstance(value, (int, float))
            and math.isfinite(value))


def _session_vwap(bars, quote):
    """Observed UTC-day VWAP; broker tick volume remains a volume proxy."""
    try:
        observed = float(quote["time_msc"]) / 1000.0
        if not math.isfinite(observed) or observed <= 0:
            return None, None, None, 0
        opened = np.asarray([float(bar["time"]) for bar in bars])
        if (not np.isfinite(opened).all() or np.any(np.diff(opened) <= 0)
                or np.any(opened+900 > observed)):
            return None, None, None, 0
        rows = [bar for bar, stamp in zip(bars, opened)
                if math.floor(observed/86400)*86400 <= stamp and stamp+900 <= observed]
        if not rows:
            return None, None, None, 0
        volume = np.asarray([float(bar.get("volume") or bar.get("tick_volume") or 0) for bar in rows])
        typical = np.asarray([(bar["high"]+bar["low"]+bar["close"])/3 for bar in rows])
        if (not np.isfinite(volume).all() or not np.isfinite(typical).all()
                or np.any(volume < 0) or volume.sum() <= 0):
            return None, None, None, len(rows)
        total = np.cumsum(volume)
        path = np.divide(np.cumsum(volume*typical), total,
                         out=np.full(len(rows), np.nan), where=total > 0)
        vwap = float(path[-1])
        sigma = float(np.sqrt(np.sum(volume*(typical-vwap)**2)/total[-1]))
        slope = (float(path[-1]-path[-2])/sigma
                 if sigma > 0 and len(path) > 1 and math.isfinite(path[-2]) else None)
        return vwap, sigma, slope, len(rows)
    except (KeyError, TypeError, ValueError, OverflowError):
        return None, None, None, 0


def build_dg_context(
    features: dict,
    payload: dict,
    pivots: Optional[dict],
    quote: dict,
    bars_15m: List[dict],
    bars_1h: Optional[List[dict]] = None,
    bars_4h: Optional[List[dict]] = None,
    entry: float = 0.0,
    sl: float = 0.0,
    tp: float = 0.0,
    sizing: Optional[dict] = None,
    regime: str = "UNDEFINED",
    symbol: str = "",
) -> Tuple[dict, List[str]]:
    """Build the dictionary context expected by decision_gates_v3.

    Returns (ctx, missing_fields).
    """
    missing = []
    if (not isinstance(features, dict) or not isinstance(quote, dict)
            or not isinstance(payload, dict) or (pivots is not None and not isinstance(pivots, dict))
            or (sizing is not None and not isinstance(sizing, dict))):
        return {}, ["context_input_invalid"]
    direction = str(features.get("direction", "LONG")).upper()
    if direction not in {"LONG", "SHORT"}:
        return {}, ["direction_invalid"]
    side = 1 if direction == "LONG" else -1

    if not bars_15m or len(bars_15m) < 16:
        missing.append("bars_15m_insufficient")
        return {}, missing

    if any(not isinstance(b, dict) or any(not _finite_number(b.get(k)) or b[k] <= 0
                                         for k in ("open", "high", "low", "close"))
           or b["high"] < max(b["open"], b["close"], b["low"])
           or b["low"] > min(b["open"], b["close"])
           for b in bars_15m):
        return {}, ["bars_15m_price_invalid"]
    if (any(not _finite_number(quote.get(k)) or quote[k] <= 0 for k in ("bid", "ask"))
            or quote["ask"] < quote["bid"]):
        return {}, ["broker_quote_invalid"]
    if any(not _finite_number(value) or value <= 0 for value in (entry, sl, tp)):
        return {}, ["entry_bracket_invalid"]
    if ("atr" in features and not _finite_number(features["atr"])):
        return {}, ["atr_invalid"]
    if sizing is None or any(not _finite_number(sizing.get(k)) or sizing[k] < 0
                             for k in ("risk_usd", "friction_usd")) or sizing["risk_usd"] <= 0:
        return {}, ["sizing_unavailable_or_invalid"]
    for b in bars_15m:
        volume = b.get("volume") if b.get("volume") is not None else b.get("tick_volume", 0)
        if not _finite_number(volume) or volume < 0:
            return {}, ["bars_15m_volume_invalid"]
    scalar_pivots = ("vwap", "P", "S1", "R1", "bull_fvg_ce", "bear_fvg_ce", "swing_high", "swing_low")
    if any((pivots or {}).get(key) is not None and not _finite_number(pivots[key]) for key in scalar_pivots):
        return {}, ["pivot_invalid"]

    o = [b["open"] for b in bars_15m]
    h = [b["high"] for b in bars_15m]
    l = [b["low"] for b in bars_15m]
    c = [b["close"] for b in bars_15m]
    v = [float(b.get("volume") or b.get("tick_volume") or 0.0) for b in bars_15m]

    atr = float(features.get("atr", 0.0))
    if atr <= 0.0:
        highs, lows, closes = map(_arr, (h[-15:], l[-15:], c[-15:]))
        tr = np.maximum(highs[1:] - lows[1:], np.maximum(abs(highs[1:] - closes[:-1]), abs(lows[1:] - closes[:-1])))
        atr = float(tr.mean()) if len(tr) > 0 else 1.0

    sig_yz = yang_zhang_sigma(o, h, l, c, n=min(32, len(c) - 1))
    if sig_yz is None or sig_yz <= 0:
        # Fallback log return volatility
        rets = np.diff(np.log(np.maximum(c, 1e-12)))
        sig_yz = float(rets[-32:].std(ddof=1)) if len(rets) >= 10 else 0.005
    sigma_bar = max(float(sig_yz), 1e-5)

    if any(quote.get(k) is not None and (not _finite_number(quote[k]) or quote[k] < 0)
           for k in ("tick_size", "point")):
        return {}, ["broker_tick_size_invalid"]
    tick = max(float(quote.get("tick_size") or 0.0), float(quote.get("point") or 0.0001), 1e-6)
    spread = float(quote.get("ask", 0.0) - quote.get("bid", 0.0))

    # Session VWAP & Sigma
    observed_vwap, observed_sigma, vwap_slope_sigma, session_count = _session_vwap(bars_15m, quote)
    vwap, vwap_sigma = observed_vwap, observed_sigma
    valid_session = vwap is not None and vwap > 0 and vwap_sigma is not None and vwap_sigma > 0 and vwap_slope_sigma is not None
    if not valid_session:
        missing.append("session_vwap_history_unavailable")
    if vwap is None or vwap <= 0:
        vwap = float(c[-1])
        vwap_sigma = atr
    if vwap_sigma is None or vwap_sigma <= 0:
        vwap_sigma = atr

    # Z-scores
    mid = float(c[-1])
    current_z = (mid - vwap) / max(vwap_sigma, 1e-12)

    # Sweep Z over recent 8 bars
    recent_k = min(8, len(c))
    if side == 1:
        # Long: extreme flush low
        sweep_low = min(l[-recent_k:])
        sweep_extreme = sweep_low
        sweep_z = (sweep_low - vwap) / max(vwap_sigma, 1e-12)
        reclaim_close = c[-1] > sweep_low
    else:
        # Short: extreme squeeze high
        sweep_high = max(h[-recent_k:])
        sweep_extreme = sweep_high
        sweep_z = (sweep_high - vwap) / max(vwap_sigma, 1e-12)
        reclaim_close = c[-1] < sweep_high

    # Delta Z over 4 bars
    z_4ago = (c[-5] - vwap) / max(vwap_sigma, 1e-12) if len(c) >= 5 else current_z
    dz4 = current_z - z_4ago

    # Volume ratio (last 4 vs last 96 bars)
    vol_4 = sum(v[-4:]) / 4.0 if len(v) >= 4 else 1.0
    vol_96 = sum(v[-96:]) / min(96, len(v)) if v else 1.0
    vol_ratio = vol_4 / max(vol_96, 1e-6)

    # Geometry for Model 2
    # Find recent swing pivot
    swing_window = min(24, len(c) - 1)
    impulse_start = len(c) - 1 - swing_window
    # The last candle is the proposed pullback, not an impulse pivot.
    previous = h[impulse_start:-1] if side == 1 else l[impulse_start:-1]
    swing_idx = impulse_start + int(np.argmax(previous) if side == 1 else np.argmin(previous))

    geo = pullback_geometry(h, l, c, direction, impulse_start=impulse_start,
                            swing_idx=swing_idx, sigma_bar=sigma_bar)

    # Structure intact
    if side == 1:
        structure_intact = c[-1] >= min(l[impulse_start:-1])
    else:
        structure_intact = c[-1] <= max(h[impulse_start:-1])

    # Shelf confluence
    shelf_price = None
    confluence = 0
    if pivots:
        candidates = [pivots.get("vwap"), pivots.get("P"), pivots.get("S1" if side == 1 else "R1"),
                      pivots.get("bull_fvg_ce" if side == 1 else "bear_fvg_ce")]
        valid_shelves = [s for s in candidates if s is not None and abs(entry - s) <= 0.35 * atr]
        confluence = len(valid_shelves)
        if valid_shelves:
            shelf_price = min(valid_shelves, key=lambda level: abs(entry - level))

    # First obstacle
    first_obstacle = None
    if pivots:
        first_obstacle = pivots.get("swing_high" if side == 1 else "swing_low")
    if first_obstacle is not None and side * (first_obstacle - entry) <= 0:
        first_obstacle = None

    # Costs and sizing
    risk_usd = float(sizing.get("risk_usd", 12.0)) if sizing else 12.0
    cost_usd = float(sizing.get("friction_usd", 0.50)) if sizing else 0.50

    # Orderflow tape extraction
    of_payload = payload.get("orderflow") if payload else None
    orderflow = None
    asset = canonical_asset(features.get("asset") or (payload or {}).get("coin") or symbol)
    allow_price_only = asset in {"GOLD", "SILVER", "USWTI", "SP500", "NAS100", "DJ30", "GER40", "EURUSD", "GBPUSD", "USDJPY"}

    if of_payload and isinstance(of_payload, dict):
        cvd_data = of_payload.get("cvd_divergence", {})
        try:
            orderflow = {
                "cvd_push1": float(cvd_data["push1"]), "cvd_push2": float(cvd_data["push2"]),
                "aggr_usd_sweep": float(of_payload["aggressor_sweep_usd"]),
                "aggr_usd_median_1m": float(of_payload["median_1m_flow_usd"]),
                "lambda_sweep": float(of_payload["lambda_sweep"]),
                "lambda_median_60m": float(of_payload["lambda_median"]),
                "bars_cvd_turned": float(of_payload["bars_turned"]),
                "pullback_cvd_share": float(of_payload["pullback_cvd_share"]),
                "exhaustion_gate_ok": of_payload["exhaustion_ok"],
                "liq_burst_toward_entry": of_payload["liq_burst"],
            }
            if (any(not math.isfinite(value) for value in orderflow.values())
                    or any(type(orderflow[key]) is not bool for key in ("exhaustion_gate_ok", "liq_burst_toward_entry"))
                    or not orderflow["bars_cvd_turned"].is_integer() or orderflow["bars_cvd_turned"] < 0
                    or not 0 <= orderflow["pullback_cvd_share"] <= 1
                    or any(orderflow[key] < 0 for key in ("aggr_usd_sweep", "aggr_usd_median_1m", "lambda_sweep", "lambda_median_60m"))):
                orderflow = None
        except (KeyError, TypeError, ValueError, AttributeError):
            orderflow = None

    p_win_lower = features.get("p_win_lower_bound")
    if (features.get("p_win_lower_bound_calibrated") is not True or isinstance(p_win_lower, bool)
            or not isinstance(p_win_lower, (int, float)) or not math.isfinite(p_win_lower)
            or not 0 <= p_win_lower <= 1):
        p_win_lower = None

    # Resting whale wall backing (Gates A3 & B5)
    wall_ctx = None
    if payload and isinstance(payload, dict):
        ob = payload.get("orderbook_live_depth", {}) or payload.get("orderbook", {})
        ob = ob if isinstance(ob, dict) else {}
        l3_walls = ob.get("whale_walls_l3") or payload.get("whale_walls_l3") or []
        l2_walls = ob.get("l2_wall_levels") or payload.get("l2_wall_levels") or []
        walls = (list(l3_walls) if isinstance(l3_walls, list) else []) + (list(l2_walls) if isinstance(l2_walls, list) else [])
        if walls:
            target_side = "BUY" if side == 1 else "SELL"
            eligible_walls = []
            for w in walls:
                if not isinstance(w, dict):
                    continue
                # A sampled span alone is not measured wall survival. Honor the
                # producer's authenticity veto rather than passing mirrored walls.
                if (w.get("gate_g7_eligible") is not True or w.get("wall_class") != "GENUINE"
                        or any(not _finite_number(w.get(k)) for k in
                               ("price", "notional_usd", "persist_s", "presence_frac"))):
                    continue
                w_side = str(w.get("side", "")).upper()
                w_price = float(w.get("price") or 0.0)
                if w_side == target_side and w_price > 0:
                    dist_pts = side * (entry - w_price)
                    dist_atr = dist_pts / max(atr, 1e-12)
                    if 0 <= dist_atr <= 0.25:
                        eligible_walls.append((dist_atr, w))
            if eligible_walls:
                eligible_walls.sort(key=lambda x: (not x[1].get("gate_g7_eligible", False), x[0]))
                best_dist_atr, best_w = eligible_walls[0]
                flow_usd = (of_payload.get("median_1m_flow_usd") if isinstance(of_payload, dict) else None)
                if not _finite_number(flow_usd) or flow_usd <= 0:
                    flow_usd = None
                wall_ctx = {
                    "usd": float(best_w.get("notional_usd") or 0.0),
                    "persist_s": float(best_w["persist_s"]),
                    "presence_frac": float(best_w["presence_frac"]),
                    "dist_from_entry_atr": float(best_dist_atr),
                    "median_1m_traded_usd": flow_usd,
                }

    m1_override = features.get("m1_range_override") or (payload.get("m1_range_override") if isinstance(payload, dict) else None)

    ctx = {
        "direction": direction,
        "regime": regime,
        "vwap_z": current_z if valid_session else None,
        "sweep_z": sweep_z if valid_session else None,
        "vwap_z_change_4bars": dz4 if valid_session else None,
        "atr": atr,
        "session_sigma": observed_sigma,
        "session_bars": session_count,
        "vwap_anchor_basis": "UTC_DAY",
        "vwap_slope_sigma_per_bar": vwap_slope_sigma,
        "vol_ratio_4_96": vol_ratio,
        "reclaim_close": reclaim_close,
        "entry": entry,
        "sl": sl,
        "tp": tp,
        "vwap": observed_vwap,
        "sweep_extreme": sweep_extreme,
        "spread": spread,
        "tick": tick,
        "risk_usd": risk_usd,
        "round_trip_cost_usd": cost_usd,
        "p_win_lower_bound": p_win_lower,
        "sigma_bar": sigma_bar,
        "geometry": geo,
        "structure_intact": structure_intact,
        "exhaustion_flags": {"vol_spike": vol_ratio > 2.2, "long_wick": False},
        "shelf": {"price": shelf_price, "confluence": confluence},
        "first_obstacle": first_obstacle,
        "allow_price_only_variant": allow_price_only,
        "orderflow": orderflow,
        "wall": wall_ctx,
        "m1_range_override": m1_override,
    }

    return ctx, missing


def evaluate_candidate_dg_v3(
    features: dict,
    payload: dict,
    pivots: Optional[dict],
    quote: dict,
    bars_15m: List[dict],
    bars_1h: Optional[List[dict]] = None,
    bars_4h: Optional[List[dict]] = None,
    entry: float = 0.0,
    sl: float = 0.0,
    tp: float = 0.0,
    sizing: Optional[dict] = None,
    symbol: str = "",
    as_of_epoch: Optional[float] = None,
) -> Dict[str, any]:
    """Execute complete Decision Gates V3 evaluation on candidate.

    Returns dict with regime, stats, passed (bool), failures, and metrics.

    `as_of_epoch` is the wall-clock reference used to judge bar staleness.
    When omitted it defaults to time.time(). Do NOT substitute the quote
    timestamp: quote["time_msc"] freezes along with a closed market, so
    (quote_time - last_bar_close) stays near one bar period no matter how many
    hours the instrument has been shut, and the staleness guard never fires.
    """
    if not isinstance(bars_15m, (list, tuple)) or not isinstance(quote, dict):
        return {"regime": "UNDEFINED", "stats": {}, "passed": False,
                "failures": ["context_input_invalid"], "metrics": {}}
    if (bars_1h and bars_4h and len(bars_15m) >= 97
            and len(bars_1h) >= HTF_STRATEGY_MIN and len(bars_4h) >= HTF_STRATEGY_MIN):
        try:
            as_of = float(quote["time_msc"])/1000
            for history, period in ((bars_15m, 900), (bars_1h, 3600), (bars_4h, 14400)):
                stamps = [float(bar["time"]) for bar in history]
                if (not math.isfinite(as_of) or as_of <= 0
                        or any(not math.isfinite(stamp) or stamp <= 0 or stamp+period > as_of for stamp in stamps)
                        or any(right <= left for left, right in zip(stamps, stamps[1:]))):
                    raise ValueError("noncausal history")
        except (KeyError, TypeError, ValueError, OverflowError):
            return {"regime": "UNDEFINED", "stats": {}, "passed": False,
                    "failures": ["regime_history_time_invalid_or_noncausal"], "metrics": {}}
        if any(not isinstance(b, dict) or not _finite_number(b.get("close")) or b["close"] <= 0
               for history in (bars_15m, bars_1h, bars_4h) for b in history):
            return {"regime": "UNDEFINED", "stats": {}, "passed": False,
                    "failures": ["regime_history_price_invalid"], "metrics": {}}
        c15 = [b["close"] for b in bars_15m]
        c1h = [b["close"] for b in bars_1h]
        c4h = [b["close"] for b in bars_4h]
        last_close = float(bars_15m[-1]["time"]) + 900.0
        # `as_of` above is the QUOTE timestamp and is correct for the causality
        # check, but wrong for staleness: a closed market's quote is frozen at
        # the same instant as its last bar, so their difference stays ~900s and
        # a 10-hour-old history reads as fresh. Staleness needs a real clock.
        if as_of_epoch is not None and (not _finite_number(as_of_epoch) or as_of_epoch <= 0):
            return {"regime": "UNDEFINED", "stats": {}, "passed": False,
                    "failures": ["as_of_epoch_invalid"], "metrics": {}}
        staleness_now = float(as_of_epoch) if as_of_epoch is not None else _time_mod.time()
        try:
            regime, rstats = classify_regime(
                c15, c1h, c4h,
                last_close_epoch=last_close,
                as_of_epoch=staleness_now,
            )
        except TypeError:
            regime, rstats = classify_regime(c15, c1h, c4h)
        if rstats.get("stale") or rstats.get("data_invalid"):
            return {"regime": regime, "stats": rstats, "passed": False,
                    "failures": ["regime_history_stale_or_invalid"], "metrics": {}}
    else:
        return {"regime": "UNDEFINED", "stats": {"history_counts": {
            "15m": len(bars_15m), "1h": len(bars_1h or []), "4h": len(bars_4h or [])}},
            "passed": False, "failures": ["regime_history_insufficient"], "metrics": {}}

    ctx, missing = build_dg_context(
        features=features,
        payload=payload,
        pivots=pivots,
        quote=quote,
        bars_15m=bars_15m,
        bars_1h=bars_1h,
        bars_4h=bars_4h,
        entry=entry,
        sl=sl,
        tp=tp,
        sizing=sizing,
        regime=regime,
        symbol=symbol,
    )

    if missing:
        return {
            "regime": regime,
            "stats": rstats,
            "passed": False,
            "failures": missing,
            "metrics": {},
        }

    if regime.startswith("TREND"):
        verdict = model2_checklist(ctx)
    elif regime == "MEAN_REVERT":
        verdict = model1_checklist(ctx)
    elif abs(float(ctx.get("vwap_z") or 0.0)) >= 2.0 or m1_range_override_ok(ctx):
        verdict = model1_checklist(ctx)
    else:
        verdict = Verdict(passed=False, failures=["REGIME_UNDEFINED"])

    return {
        "regime": regime,
        "stats": rstats,
        "passed": verdict.passed,
        "failures": verdict.failures,
        "metrics": verdict.metrics,
    }
