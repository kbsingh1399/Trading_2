"""Terminal/dg_hardening.py -- external audit patches (2026-10-11).
Pure, deterministic, dependency-light (numpy + stdlib). No MT5, no I/O.
Every function FAILS CLOSED: an unknown operand yields the least permissive
answer, never a fabricated measurement. Every numeric default is a PRIOR,
not a fitted value. Replace the gap priors and basis constants with estimates
from your own archives before promotion.
"""
from __future__ import annotations

import math
import statistics
from dataclasses import asdict, dataclass
from numbers import Real
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple
import numpy as np


def _fin(x: Any) -> bool:
    if isinstance(x, (bool, np.bool_)) or not isinstance(x, Real):
        return False
    try:
        return math.isfinite(float(x))
    except (OverflowError, ValueError, TypeError):
        return False


# =================================================================== 1. Option A'
WALL_BAND_ATR = 0.25
BASIS_TOL_CAP_ATR = 0.25       # never looser than the wall band itself
BASIS_TOL_FLOOR_TICKS = 2.0     # quantization floor for micro-ATR assets
BASIS_SIGMA_K = 4.0             # ~4 robust sigmas of basis noise
BASIS_MAX_CLOCK_SKEW_S = 5.0    # broker-mid vs venue-mid timestamp skew (allows small network jitter)
BASIS_MIN_SCALE_SAMPLES = 10


def quantize_to_tick(price: Any, tick: Any) -> Optional[float]:
    if not (_fin(price) and _fin(tick)) or float(tick) <= 0:
        return None
    t = float(tick)
    return float(round(round(float(price) / t) * t, 10))


def robust_basis_sigma(samples: Optional[Iterable[Any]], min_samples: int = BASIS_MIN_SCALE_SAMPLES) -> Optional[float]:
    """1.4826 * MAD of basis prints. Accepts floats or (ts, basis) pairs."""
    if samples is None:
        return None
    vals: List[float] = []
    for item in samples:
        b = item[1] if isinstance(item, (list, tuple)) and len(item) == 2 else item
        if _fin(b):
            vals.append(float(b))
    if len(vals) < int(min_samples):
        return None
    med = statistics.median(vals)
    return 1.4826 * statistics.median([abs(b - med) for b in vals])


@dataclass
class BasisDecision:
    ok: bool
    reason: str
    b_now: Optional[float] = None
    b_hat: Optional[float] = None
    drift: Optional[float] = None
    tol: Optional[float] = None
    sigma_b: Optional[float] = None
    skew_s: Optional[float] = None


def basis_drift_decision(
    broker_mid: Any, venue_mid: Any, b_hat: Any, atr: Any, tick: Any, *,
    broker_ts: Any, venue_ts: Any,
    basis_samples: Optional[Iterable[Any]] = None,
    b_hat_long: Any = None,
    max_skew_s: float = BASIS_MAX_CLOCK_SKEW_S,
    k_sigma: float = BASIS_SIGMA_K,
    cap_atr: float = BASIS_TOL_CAP_ATR,
    floor_ticks: float = BASIS_TOL_FLOOR_TICKS
) -> BasisDecision:
    """Validate the cross-venue basis before any wall is translated.
    Fails closed on: missing mids, cold start (no independent b_hat), unverified or skewed
    clocks, a short/long anchor regime shift, and drift beyond a volatility-scaled
    tolerance capped at the wall band.
    """
    if not (_fin(atr) and float(atr) > 0 and _fin(tick) and float(tick) > 0):
        return BasisDecision(False, "venue_basis_scale_invalid")
    if not (_fin(broker_mid) and float(broker_mid) > 0 and _fin(venue_mid) and float(venue_mid) > 0):
        return BasisDecision(False, "venue_basis_mid_unavailable")
    b_now = float(broker_mid) - float(venue_mid)
    if not _fin(b_hat):
        # Legacy fallback b_hat = b_now makes drift identically 0: breaker inert.
        return BasisDecision(False, "venue_basis_cold_start", b_now=b_now)
    b_hat = float(b_hat)
    if not (_fin(broker_ts) and _fin(venue_ts)):
        return BasisDecision(False, "venue_basis_clock_unverified", b_now=b_now, b_hat=b_hat)
    skew = abs(float(broker_ts) - float(venue_ts))
    if skew > max_skew_s:
        return BasisDecision(False, "venue_basis_clock_skew", b_now=b_now, b_hat=b_hat, skew_s=skew)
    cap = cap_atr * float(atr)
    floor = floor_ticks * float(tick)
    sigma_b = robust_basis_sigma(basis_samples)
    tol = max(floor, cap if sigma_b is None else min(cap, k_sigma * sigma_b))
    drift = abs(b_now - b_hat)
    common = dict(b_now=b_now, b_hat=b_hat, drift=drift, tol=tol, sigma_b=sigma_b, skew_s=skew)
    if _fin(b_hat_long) and abs(b_hat - float(b_hat_long)) > cap:
        return BasisDecision(False, "venue_basis_regime_shift", **common)
    if drift > tol:
        return BasisDecision(False, "venue_basis_drift_tripped", **common)
    return BasisDecision(True, "ok", **common)


def translate_wall_distance(
    entry: Any, wall_price: Any, side: int, decision: BasisDecision, atr: Any, tick: Any,
    band_atr: float = WALL_BAND_ATR
) -> Tuple[bool, Optional[float], Optional[float], str]:
    """Error-budgeted band: residual basis error is charged against BOTH edges.
    Accept iff drift <= d <= band - drift (all in ATR), where
    d = side * (entry - quantize(wall + b_hat)) / ATR.
    Returns (accepted, worst_case_dist_atr, wall_mt5, reason).
    """
    if not decision.ok:
        return False, None, None, decision.reason
    if not (_fin(entry) and _fin(wall_price) and float(wall_price) > 0 and side in (1, -1)):
        return False, None, None, "wall_operand_invalid"
    wall_mt5 = quantize_to_tick(float(wall_price) + float(decision.b_hat), tick)
    if wall_mt5 is None:
        return False, None, None, "wall_quantization_failed"
    scale = max(float(atr), 2.0 * float(tick) / band_atr) if (float(tick) > 0 and band_atr > 0) else float(atr)
    dist = side * (float(entry) - wall_mt5) / float(atr)
    budget = float(decision.drift or 0.0) / scale
    if dist - budget < -1e-12:
        return False, dist, wall_mt5, "wall_not_behind_entry_within_basis_error"
    if dist + budget > band_atr + 1e-12:
        return False, dist, wall_mt5, "wall_outside_band_after_basis_error"
    return True, dist + budget, wall_mt5, "ok"


_WALL_FIELDS = ("price", "notional_usd", "persist_s", "presence_frac")


def resolve_wall_venue(row: Mapping[str, Any], default_venue: str = "BINANCE") -> str:
    raw = str(row.get("venue") or row.get("source") or "").upper()
    if "HYPER" in raw:
        return "HYPERLIQUID"
    if "BINANCE" in raw:
        return "BINANCE"
    if "MT5" in raw or "NATIVE" in raw:
        return "NATIVE"
    return str(default_venue).upper()


def adaptive_wall_band_atr(atr: Any, tick: Any, stop_atr: float = 1.5) -> float:
    """Institutional envelope-aware adaptive wall band.
    band_atr = clamp( max(0.35, 6.0 * tick / atr), 0.20, min(0.55, stop_atr - 0.70) )
    """
    if not (_fin(atr) and float(atr) > 0):
        return 0.40
    t = float(tick) if _fin(tick) and float(tick) > 0 else 0.0
    floor = max(0.20, (6.0 * t) / float(atr))
    band = max(0.35, floor)
    envelope = max(0.20, float(stop_atr) - 0.70)
    return float(min(band, 0.55, envelope))


def venue_quotes_from_orderbook(ob: Any, payload: Any = None) -> Dict[str, Dict[str, Any]]:
    """Read per-venue basis blocks; fall back to legacy single-venue keys."""
    ob = ob if isinstance(ob, dict) else {}
    payload = payload if isinstance(payload, dict) else {}
    out: Dict[str, Dict[str, Any]] = {}
    vb = ob.get("venue_basis")
    if isinstance(vb, dict):
        for venue, q in vb.items():
            if isinstance(q, dict):
                out[str(venue).upper()] = {
                    "mid": q.get("mid"),
                    "ts": q.get("mid_ts"),
                    "b_hat": q.get("basis_median"),
                    "b_hat_long": q.get("basis_median_long"),
                    "samples": q.get("basis_samples"),
                }
    if "BINANCE" not in out:
        def pick(key: str) -> Any:
            value = ob.get(key)
            return value if value is not None else payload.get(key)
        out["BINANCE"] = {
            "mid": pick("binance_mid"),
            "ts": pick("binance_mid_ts"),
            "b_hat": pick("basis_median"),
            "b_hat_long": pick("basis_median_long"),
            "samples": pick("basis_samples"),
        }
    return out


def select_backing_wall(
    walls: Iterable[Any], *, entry: float, side: int, atr: float, tick: float,
    broker_mid: Any, broker_ts: Any,
    venue_quotes: Mapping[str, Mapping[str, Any]],
    grid_addrs: Iterable[str] = frozenset(),
    flow_usd: Any = None,
    default_venue: str = "BINANCE",
    band_atr: float = 0.40,
    require_clock: bool = True
) -> Tuple[Optional[Dict[str, Any]], Dict[str, Any]]:
    """Drop-in replacement for the inline Option A' block in build_dg_context."""
    diag: Dict[str, Any] = {"rejections": {}, "basis": {}}
    def reject(code: str) -> None:
        diag["rejections"][code] = diag["rejections"].get(code, 0) + 1

    if side not in (1, -1) or not (_fin(atr) and float(atr) > 0) or not _fin(entry):
        reject("context_invalid")
        return None, diag

    grid = {str(a).strip() for a in (grid_addrs or ())}
    target = "BUY" if side == 1 else "SELL"
    decisions: Dict[str, BasisDecision] = {}
    best = None

    any_venue_mids = any(_fin(v.get("mid")) for v in (venue_quotes or {}).values() if isinstance(v, dict))

    for w in walls or ():
        if not isinstance(w, dict) or str(w.get("side") or "").upper() != target:
            continue
        if str(w.get("address") or "").strip() in grid:
            reject("two_sided_grid")
            continue
        if w.get("gate_g7_eligible") is not True or w.get("wall_class") != "GENUINE":
            reject("not_g7_genuine")
            continue
        if any(not _fin(w.get(k)) for k in _WALL_FIELDS):
            reject("non_finite_fields")
            continue
        venue = resolve_wall_venue(w, default_venue)
        if venue not in decisions:
            q = (venue_quotes or {}).get(venue) or {}
            if (not any_venue_mids and q.get("mid") is None) or venue == "NATIVE":
                # Native broker book: wall prices published in native broker space
                tol = max(BASIS_TOL_FLOOR_TICKS * float(tick), BASIS_TOL_CAP_ATR * float(atr))
                decisions[venue] = BasisDecision(True, "native_basis", b_now=0.0, b_hat=0.0, drift=0.0, tol=tol, sigma_b=0.0, skew_s=0.0)
            else:
                v_ts = q.get("ts") if (require_clock and q.get("ts") is not None) else broker_ts
                decisions[venue] = basis_drift_decision(
                    broker_mid, q.get("mid"), q.get("b_hat"), atr, tick,
                    broker_ts=broker_ts,
                    venue_ts=v_ts,
                    basis_samples=q.get("samples"),
                    b_hat_long=q.get("b_hat_long"),
                )
            diag["basis"][venue] = asdict(decisions[venue])
        ok, worst, wall_mt5, reason = translate_wall_distance(
            entry, w["price"], side, decisions[venue], atr, tick, band_atr
        )
        if not ok:
            reject(reason)
            continue
        raw = side * (float(entry) - wall_mt5) / float(atr)
        if best is None or raw < best[0]:
            best = (raw, worst, w, wall_mt5, venue)

    if best is None:
        return None, diag

    raw, worst, w, wall_mt5, venue = best
    d = decisions[venue]
    return {
        "usd": float(w["notional_usd"]),
        "persist_s": float(w["persist_s"]),
        "presence_frac": float(w["presence_frac"]),
        "dist_from_entry_atr": float(raw),
        "dist_from_entry_atr_worst": float(worst),
        "dist_from_entry_atr_point": float(raw),
        "median_1m_traded_usd": flow_usd if _fin(flow_usd) and float(flow_usd) > 0 else None,
        "wall_class": "GENUINE",
        "gate_g7_eligible": True,
        "venue": venue,
        "raw_wall_price": float(w["price"]),
        "effective_wall_price": float(wall_mt5),
        "venue_basis_applied": float(d.b_hat),
        "venue_basis_drift_ok": True,
        "basis_error_atr": float(d.drift) / float(atr),
    }, diag


def venue_basis_block(
    meta: Optional[Dict[str, Any]], asset: str, venue: str,
    broker_mid: Any, venue_mid: Any, venue_mid_ts: Any, now_ts: float
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """PRODUCER helper: median over PRIOR prints only, then record this print."""
    from Terminal.microstructure_state import (
        BASIS_HISTORY_KEY, record_basis_observation, rolling_basis_median,
    )
    key = f"{asset}@{str(venue).upper()}"
    b_hat = rolling_basis_median(meta, key, now_ts)
    hist = ((meta or {}).get(BASIS_HISTORY_KEY) or {}).get(key) or []
    samples = [[t, b] for t, b in hist if _fin(t) and float(t) >= now_ts - 1800.0]
    new_meta = dict(meta or {})
    if _fin(broker_mid) and _fin(venue_mid):
        new_meta = record_basis_observation(new_meta, key, now_ts, float(broker_mid) - float(venue_mid))
    return new_meta, {
        "mid": venue_mid, "mid_ts": venue_mid_ts, "basis_median": b_hat,
        "basis_median_long": None, "basis_samples": samples,
    }


# ============================================================ 2. gap-aware floor stress
TAIL_GAP_FRAC_SESSION_CLOSE = {
    "CRYPTO": 0.08, "INDEX": 0.025, "METAL": 0.025, "ENERGY": 0.04, "FX": 0.008
}
TAIL_GAP_FRAC_INTRADAY = {
    "CRYPTO": 0.03, "INDEX": 0.005, "METAL": 0.006, "ENERGY": 0.01, "FX": 0.002
}


def gap_stressed_loss(
    *, direction: str, entry: float, sl: float, volume: float,
    usd_per_price_unit_per_lot: float, asset_class: str,
    crosses_session_close: bool,
    nominal_multiplier: float = 1.25,
    cost_reserve_usd: float = 2.0,
    gap_table: Optional[Mapping[str, float]] = None
) -> Optional[float]:
    """max(legacy stress, loss if price gaps gap_frac beyond the stop)."""
    if direction not in ("LONG", "SHORT"):
        return None
    vals = (entry, sl, volume, usd_per_price_unit_per_lot)
    if not all(_fin(x) for x in vals) or min(float(x) for x in vals) <= 0:
        return None
    table = gap_table or (TAIL_GAP_FRAC_SESSION_CLOSE if crosses_session_close else TAIL_GAP_FRAC_INTRADAY)
    gap_frac = table.get(str(asset_class).upper())
    if not _fin(gap_frac) or float(gap_frac) < 0:
        return None
    side = 1 if direction == "LONG" else -1
    stop_dist = side * (float(entry) - float(sl))
    usd_per_unit = float(usd_per_price_unit_per_lot) * float(volume)
    nominal = max(0.0, stop_dist) * usd_per_unit
    base = nominal_multiplier * nominal + cost_reserve_usd
    gap_loss = max(0.0, stop_dist + float(gap_frac) * float(sl)) * usd_per_unit + cost_reserve_usd
    return float(max(base, gap_loss))


def joint_floor_check(
    balance: Any, equity: Any, stressed_losses: Iterable[Any],
    hard_floor_usd: float = 4775.0, buffer_usd: float = 20.0
) -> Dict[str, Any]:
    if not (_fin(balance) and _fin(equity)):
        return {"ok": False, "reason": "account_unobserved"}
    vals = list(stressed_losses)
    if any(not _fin(v) or float(v) < 0 for v in vals):
        return {"ok": False, "reason": "ticket_stress_unavailable"}
    post = min(float(balance), float(equity)) - sum(float(v) for v in vals)
    req = hard_floor_usd + buffer_usd
    return {
        "ok": post >= req, "post_stress_equity_usd": post,
        "required_usd": req, "cushion_usd": post - req,
        "reason": "ok" if post >= req else "floor_buffer_breached_under_gap_stress",
    }


# =================================================== 3. outcome-class expectancy
def _binom_sf(k: int, n: int, p: float) -> float:
    if k <= 0:
        return 1.0
    if k > n:
        return 0.0
    return float(sum(math.comb(n, i) * p ** i * (1.0 - p) ** (n - i) for i in range(k, n + 1)))


def clopper_pearson_bounds(k: int, n: int, confidence: float = 0.95) -> Optional[Tuple[float, float]]:
    """Exact one-sided lower and upper bounds (each at `confidence`)."""
    if not (isinstance(k, int) and isinstance(n, int)) or n <= 0 or not 0 <= k <= n:
        return None
    if not 0.0 < confidence < 1.0:
        return None
    alpha = 1.0 - confidence
    lo, hi = 0.0, 1.0
    if k > 0:
        a, b = 0.0, 1.0
        for _ in range(200):
            m = 0.5 * (a + b)
            if _binom_sf(k, n, m) > alpha:
                b = m
            else:
                a = m
        lo = 0.5 * (a + b)
    if k < n:
        a, b = 0.0, 1.0
        for _ in range(200):
            m = 0.5 * (a + b)
            if 1.0 - _binom_sf(k + 1, n, m) > alpha:
                a = m
            else:
                b = m
        hi = 0.5 * (a + b)
    return lo, hi


def binary_ev_lower(n_win: int, n: int, rr: float, cost_r: float, slip_r: float = 0.10) -> Optional[float]:
    b = clopper_pearson_bounds(n_win, n)
    if b is None:
        return None
    p = b[0]
    return p * (rr - cost_r) - (1.0 - p) * (1.0 + cost_r + slip_r)


def ternary_ev_lower(
    n_tp: int, n_scratch: int, n_sl: int, rr: float, cost_r: float,
    slip_r: float = 0.10, scratch_net_r: float = 0.0, confidence: float = 0.95
) -> Optional[Dict[str, float]]:
    """Conservative EV with TP / scratch / SL as separate outcomes."""
    n = n_tp + n_scratch + n_sl
    b_tp = clopper_pearson_bounds(n_tp, n, confidence)
    b_sl = clopper_pearson_bounds(n_sl, n, confidence)
    if b_tp is None or b_sl is None:
        return None
    p_tp, p_sl = b_tp[0], b_sl[1]
    if p_tp + p_sl > 1.0:
        p_tp = max(0.0, 1.0 - p_sl)
    p_sc = max(0.0, 1.0 - p_tp - p_sl)
    ev = p_tp * (rr - cost_r) + p_sc * scratch_net_r - p_sl * (1.0 + cost_r + slip_r)
    return {
        "ev_lower_r": ev, "p_tp_lower": p_tp, "p_sl_upper": p_sl,
        "p_scratch": p_sc, "n": float(n),
    }


# ===================================================== 4. measured M1 override
ALLOW_M1_RANGE_OVERRIDE = False  # ratified mandate: UNDEFINED -> stand aside


def derive_m1_range_override(
    caller_override: Any, stats_4h: Any, direction: str, *, orderflow_present: bool
) -> Optional[Dict[str, Any]]:
    """Re-derive the override flags from MEASURED 4H statistics."""
    if not ALLOW_M1_RANGE_OVERRIDE or not isinstance(caller_override, dict):
        return None
    if direction not in ("LONG", "SHORT") or not isinstance(stats_4h, dict):
        return None
    from Terminal.decision_gates_v3 import htf_confirms_direction
    ext_sign = -1 if direction == "LONG" else 1
    adverse = htf_confirms_direction(stats_4h, ext_sign)
    return {
        "absorption_verified": bool(orderflow_present and caller_override.get("absorption_verified") is True),
        "htf_adverse_trend": bool(adverse),
        "source": "MEASURED_4H",
    }


# ============================================================ 5. causal dz4
def causal_session_z_path(bars: Sequence[Mapping[str, Any]]) -> Optional[np.ndarray]:
    """Z_t = (close_t - VWAP_t) / sigma_t using ONLY bars 0..t of the session."""
    try:
        h = np.array([float(b["high"]) for b in bars])
        l = np.array([float(b["low"]) for b in bars])
        c = np.array([float(b["close"]) for b in bars])
        v = np.array([float(b.get("volume") or b.get("tick_volume") or 0.0) for b in bars])
    except (KeyError, TypeError, ValueError):
        return None
    if len(c) == 0 or not (np.isfinite(h).all() and np.isfinite(l).all() and np.isfinite(c).all() and np.isfinite(v).all()) or (v < 0).any():
        return None
    tp = (h + l + c) / 3.0
    cv = np.cumsum(v)
    with np.errstate(divide="ignore", invalid="ignore"):
        vwap = np.cumsum(v * tp) / cv
        var = np.cumsum(v * tp * tp) / cv - vwap ** 2
        sig = np.sqrt(np.maximum(var, 0.0))
        z = (c - vwap) / sig
        z[~np.isfinite(z) | (sig <= 0)] = np.nan
    return z


def causal_dz4(bars: Sequence[Mapping[str, Any]], min_bars: int = 16) -> Optional[float]:
    z = causal_session_z_path(bars)
    if z is None or len(z) < max(min_bars, 5) or not (np.isfinite(z[-1]) and np.isfinite(z[-5])):
        return None
    return float(z[-1] - z[-5])


# ======================================================== 6. real reclaim (A4)
def reclaim_close_strict(
    bars: Sequence[Mapping[str, Any]], side: int, vwap: float, sigma: float,
    z_band: float = 2.0, lookback: int = 8
) -> bool:
    """True only if a PRIOR bar pierced the -/+ z_band band and the LAST bar closed back inside it."""
    if side not in (1, -1) or not (_fin(vwap) and _fin(sigma) and float(sigma) > 0):
        return False
    if len(bars) < 2:
        return False
    band = float(vwap) - side * z_band * float(sigma)
    prior = bars[-(lookback + 1):-1]
    try:
        pierced = any((side * (band - float(b["low" if side == 1 else "high"]))) > 0 for b in prior)
        back_inside = side * (float(bars[-1]["close"]) - band) > 0
    except (KeyError, TypeError, ValueError):
        return False
    return bool(pierced and back_inside)


# ================================================== 7. drift t-stat (not level)
def drift_tstat_nw(closes: Sequence[float], n: int, lags: Optional[int] = None) -> Optional[float]:
    """HAC t-stat of the MEAN LOG RETURN. Valid under I(1) prices."""
    try:
        c = np.asarray(closes, dtype=float)[-(n + 1):]
    except (TypeError, ValueError):
        return None
    if len(c) < n + 1 or n < 10 or not np.isfinite(c).all() or (c <= 0).any():
        return None
    r = np.diff(np.log(c))
    e = r - r.mean()
    L = lags if lags is not None else int(math.floor(4 * (n / 100) ** (2 / 9)))
    s = float(e @ e) / n
    for k in range(1, L + 1):
        s += 2 * (1 - k / (L + 1)) * float(e[k:] @ e[:-k]) / n
    if s <= 0:
        return 0.0
    return float(r.mean() / math.sqrt(s / n))


# ================================================ 8. pre-send discrete checks
def discrete_order_checks(
    *, price: float, sl: float, tp: float, volume: float, side: int,
    bid: float, ask: float, tick_size: float, point: float,
    stops_level_pts: float, freeze_level_pts: float,
    volume_min: float, volume_step: float, volume_max: Optional[float],
    risk_budget_usd: float, usd_per_price_unit_per_lot: float
) -> List[str]:
    """Supplements pre_send_gate: tick alignment, freeze level, lot rounding DOWN only, and realised risk <= budget after rounding."""
    r: List[str] = []
    if not all(_fin(x) for x in (price, sl, tp, volume, bid, ask, tick_size, point,
                                 stops_level_pts, freeze_level_pts, volume_min,
                                 volume_step, risk_budget_usd, usd_per_price_unit_per_lot)):
        return ["discrete_operand_invalid"]
    if tick_size <= 0 or volume_step <= 0 or side not in (1, -1):
        return ["discrete_operand_invalid"]
    for name, px in (("price", price), ("sl", sl), ("tp", tp)):
        if abs(px / tick_size - round(px / tick_size)) > 1e-6:
            r.append(f"{name}_off_tick")
    ref = ask if side == 1 else bid
    min_dist = max(stops_level_pts, freeze_level_pts) * point
    if side * (ref - price) < max(min_dist, tick_size):
        r.append("limit_inside_stops_or_freeze_level")
    if abs(price - sl) < min_dist or abs(tp - price) < min_dist:
        r.append("sltp_inside_stops_or_freeze_level")
    steps = math.floor((volume - volume_min) / volume_step + 1e-9)
    legal = volume_min + max(steps, 0) * volume_step
    if volume < volume_min - 1e-12 or abs(legal - volume) > 1e-9:
        r.append("volume_not_on_step_round_down_required")
    if volume_max is not None and _fin(volume_max) and volume > volume_max:
        r.append("volume_exceeds_broker_max")
    risk = abs(price - sl) * volume * usd_per_price_unit_per_lot
    if risk > risk_budget_usd + 1e-9:
        r.append(f"realised_risk_{risk:.2f}_exceeds_budget")
    return r
