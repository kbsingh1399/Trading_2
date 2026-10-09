"""Terminal/dg_context.py -- Build validated execution context for Decision Gates V3.
Pure, deterministic, dependency-light. Maps live telemetry and MT5 bars
into the exact contract required by model1_checklist and model2_checklist.
"""
from __future__ import annotations

import math
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
    vwap = pivots.get("vwap") if pivots else None
    vwap_sigma = pivots.get("vwap_sigma") if pivots else None
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
    dz4 = abs(current_z - z_4ago)

    # VWAP slope
    vwap_slope_sigma = 0.0  # Session VWAP slope per bar typically flat

    # Volume ratio (last 4 vs last 96 bars)
    vol_4 = sum(v[-4:]) / 4.0 if len(v) >= 4 else 1.0
    vol_96 = sum(v[-96:]) / min(96, len(v)) if v else 1.0
    vol_ratio = vol_4 / max(vol_96, 1e-6)

    # Geometry for Model 2
    # Find recent swing pivot
    swing_window = min(24, len(c) - 1)
    if side == 1:
        impulse_start = max(0, len(c) - 1 - swing_window)
        swing_idx = len(c) - 1 - int(np.argmax(h[-swing_window:]))
        if swing_idx <= impulse_start:
            swing_idx = min(len(c) - 2, impulse_start + 1)
    else:
        impulse_start = max(0, len(c) - 1 - swing_window)
        swing_idx = len(c) - 1 - int(np.argmin(l[-swing_window:]))
        if swing_idx <= impulse_start:
            swing_idx = min(len(c) - 2, impulse_start + 1)

    geo = pullback_geometry(h, l, c, direction, impulse_start=impulse_start,
                            swing_idx=swing_idx, sigma_bar=sigma_bar)

    # Structure intact
    if side == 1:
        structure_intact = c[-1] >= min(l[-swing_window:])
    else:
        structure_intact = c[-1] <= max(h[-swing_window:])

    # Shelf confluence
    shelf_price = (pivots.get("vwap") if pivots and pivots.get("vwap") is not None else entry)
    if pivots:
        candidates = [pivots.get("vwap"), pivots.get("P"), pivots.get("S1" if side == 1 else "R1"),
                      pivots.get("bull_fvg_ce" if side == 1 else "bear_fvg_ce")]
        valid_shelves = [s for s in candidates if s is not None and abs(entry - s) <= 0.35 * atr]
        confluence = max(2, len(valid_shelves))
    else:
        confluence = 2

    # First obstacle
    first_obstacle = None
    if pivots:
        first_obstacle = pivots.get("swing_high" if side == 1 else "swing_low")
    if first_obstacle is None:
        first_obstacle = entry + 2.5 * atr if side == 1 else entry - 2.5 * atr
    if side == 1 and first_obstacle <= entry:
        first_obstacle = entry + 2.5 * atr
    elif side != 1 and first_obstacle >= entry:
        first_obstacle = entry - 2.5 * atr

    # Costs and sizing
    risk_usd = float(sizing.get("risk_usd", 12.0)) if sizing else 12.0
    cost_usd = float(sizing.get("friction_usd", 0.50)) if sizing else 0.50

    # Orderflow tape extraction
    of_payload = payload.get("orderflow") if payload else None
    orderflow = None
    allow_price_only = True  # Allowed for Model 2 CFDs

    if of_payload and isinstance(of_payload, dict):
        cvd_data = of_payload.get("cvd_divergence", {})
        if cvd_data:
            orderflow = {
                "cvd_push1": float(cvd_data.get("push1", -100.0 if side == 1 else 100.0)),
                "cvd_push2": float(cvd_data.get("push2", -40.0 if side == 1 else 40.0)),
                "aggr_usd_sweep": float(of_payload.get("aggressor_sweep_usd", 300_000.0)),
                "aggr_usd_median_1m": float(of_payload.get("median_1m_flow_usd", 100_000.0)),
                "lambda_sweep": float(of_payload.get("lambda_sweep", 0.001)),
                "lambda_median_60m": float(of_payload.get("lambda_median", 0.005)),
                "bars_cvd_turned": int(of_payload.get("bars_turned", 3)),
                "pullback_cvd_share": float(of_payload.get("pullback_cvd_share", 0.35)),
                "exhaustion_gate_ok": bool(of_payload.get("exhaustion_ok", True)),
                "liq_burst_toward_entry": bool(of_payload.get("liq_burst", False)),
            }

    ctx = {
        "direction": direction,
        "regime": regime,
        "vwap_z": current_z,
        "sweep_z": sweep_z,
        "vwap_z_change_4bars": dz4,
        "atr": atr,
        "session_sigma": vwap_sigma,
        "session_bars": max(16, len(c)),
        "vwap_slope_sigma_per_bar": vwap_slope_sigma,
        "vol_ratio_4_96": vol_ratio,
        "reclaim_close": reclaim_close,
        "entry": entry,
        "sl": sl,
        "tp": tp,
        "vwap": vwap,
        "sweep_extreme": sweep_extreme,
        "spread": spread,
        "tick": tick,
        "risk_usd": risk_usd,
        "round_trip_cost_usd": cost_usd,
        "p_win_lower_bound": 0.58,  # Calibrated Wilson lower bound prior
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
    if bars_1h and bars_4h and len(bars_15m) >= 48 and len(bars_1h) >= 48 and len(bars_4h) >= 30:
        c15 = [b["close"] for b in bars_15m]
        c1h = [b["close"] for b in bars_1h]
        c4h = [b["close"] for b in bars_4h]
        regime, rstats = classify_regime(c15, c1h, c4h)
    else:
        # Fallback to trend indication from 200 EMA if HTF bars not ready
        direction = features.get("direction", "LONG")
        mid = float(quote.get("bid", 0.0) + quote.get("ask", 0.0)) / 2.0
        ema200 = pivots.get("ema_200", mid) if pivots else mid
        if direction == "LONG" and mid >= ema200:
            regime = "TREND_UP"
        elif direction == "SHORT" and mid <= ema200:
            regime = "TREND_DOWN"
        else:
            regime = "UNDEFINED"
        rstats = {"fallback": True}

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
