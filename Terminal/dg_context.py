"""Terminal/dg_context.py -- Build validated execution context for Decision Gates V3.
Pure, deterministic, dependency-light. Maps live telemetry and MT5 bars
into the exact contract required by model1_checklist and model2_checklist.
"""
from __future__ import annotations

import math
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
    Verdict,
)


def _arr(x) -> np.ndarray:
    return np.asarray(x, dtype=float)


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
    direction = str(features.get("direction", "LONG")).upper()
    side = 1 if direction == "LONG" else -1

    if not bars_15m or len(bars_15m) < 16:
        missing.append("bars_15m_insufficient")
        return {}, missing

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
) -> Dict[str, any]:
    """Execute complete Decision Gates V3 evaluation on candidate.

    Returns dict with regime, stats, passed (bool), failures, and metrics.
    """
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
        c15 = [b["close"] for b in bars_15m]
        c1h = [b["close"] for b in bars_1h]
        c4h = [b["close"] for b in bars_4h]
        regime, rstats = classify_regime(c15, c1h, c4h)
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
    else:
        verdict = Verdict(passed=False, failures=["REGIME_UNDEFINED"])

    return {
        "regime": regime,
        "stats": rstats,
        "passed": verdict.passed,
        "failures": verdict.failures,
        "metrics": verdict.metrics,
    }
