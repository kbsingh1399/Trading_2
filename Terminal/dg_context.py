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

try:  # pragma: no cover - import shim for standalone invocation
    from Terminal.microstructure_state import two_sided_grid_addresses
except Exception:  # pragma: no cover
    try:
        from microstructure_state import two_sided_grid_addresses
    except Exception:
        def two_sided_grid_addresses(walls, **_kw):
            return set()


def _arr(x) -> np.ndarray:
    return np.asarray(x, dtype=float)


def _finite_number(value):
    return (not isinstance(value, bool) and isinstance(value, (int, float))
            and math.isfinite(value))


def _quote_tick_msc(quote):
    """Broker tick time in ms, under whichever key the caller uses.

    The live MT5 path supplies ``time_msc`` directly. The emitted telemetry
    snapshot renames it to ``broker_tick_time_utc_msc``
    (Data_Factory/generate_telemetry_snapshot.py), which left every published
    snapshot unable to build a session VWAP here.
    """
    if not isinstance(quote, dict):
        raise TypeError("quote")
    for key in ("time_msc", "broker_tick_time_utc_msc"):
        value = quote.get(key)
        if value is not None:
            return value
    raise KeyError("time_msc")


def _bar_open_ts(bar):
    """Bar open epoch. Live bars use ``time``; emitted telemetry uses ``ts``."""
    if not isinstance(bar, dict):
        raise TypeError("bar")
    for key in ("time", "ts"):
        value = bar.get(key)
        if value is not None:
            return value
    raise KeyError("time")


def _safe_bar_open_ts(bar):
    """Safe bar open epoch returning float or None without throwing."""
    if not isinstance(bar, dict):
        return None
    for key in ("time", "ts"):
        value = bar.get(key)
        if _finite_number(value):
            return float(value)
    return None


def _session_vwap(bars, quote):
    """Observed UTC-day VWAP; broker tick volume remains a volume proxy."""
    try:
        observed = float(_quote_tick_msc(quote)) / 1000.0
        if not math.isfinite(observed) or observed <= 0:
            return None, None, None, 0
        opened = np.asarray([float(_bar_open_ts(bar)) for bar in bars])
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

    atr_input = features.get("atr") if features.get("atr") is not None else features.get("atr_14")
    if atr_input is not None:
        if not _finite_number(atr_input) or float(atr_input) <= 0:
            return {}, ["atr_invalid"]
        atr = float(atr_input)
    else:
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
    entry_z = (float(entry) - vwap) / max(vwap_sigma, 1e-12) if (_finite_number(entry) and float(entry) > 0) else current_z

    # Sweep Z over recent 8 bars
    recent_k = min(8, len(c))
    if side == 1:
        # Long: extreme flush low
        sweep_low = min(l[-recent_k:])
        sweep_extreme = sweep_low
        sweep_z = (sweep_low - vwap) / max(vwap_sigma, 1e-12)
    else:
        # Short: extreme squeeze high
        sweep_high = max(h[-recent_k:])
        sweep_extreme = sweep_high
        sweep_z = (sweep_high - vwap) / max(vwap_sigma, 1e-12)

    from Terminal.dg_hardening import causal_dz4, reclaim_close_strict
    # Strict A4 reclaim: bar must have pierced 2.0 SD band and closed back inside
    reclaim_close = reclaim_close_strict(bars_15m, side, vwap, vwap_sigma, z_band=2.0)
    if not reclaim_close and len(c) > 0:
        # Legacy fallback if bars lack high/low pierce history but satisfy basic reclaim
        if (side == 1 and c[-1] > sweep_low) or (side == -1 and c[-1] < sweep_high):
            # Only allow fallback if sweep actually exceeded 2.0 SD
            if abs(sweep_z) >= 2.0 - 1e-6:
                reclaim_close = True

    # Causal dz4 over session bars (P1-2)
    _session_rows = []
    _tick_msc = None
    if isinstance(quote, dict):
        try:
            _tick_msc = _quote_tick_msc(quote)
        except (KeyError, TypeError, ValueError):
            _tick_msc = None
    if _finite_number(_tick_msc):
        _day_start = math.floor(float(_tick_msc) / 1000.0 / 86400.0) * 86400.0
        for b in bars_15m:
            bts = _safe_bar_open_ts(b)
            if bts is not None and bts >= _day_start:
                _session_rows.append(b)
    dz4 = causal_dz4(_session_rows, min_bars=5) if len(_session_rows) >= 5 else None

    # Volume ratio (last 4 vs last 96 bars)
    vol_4 = sum(v[-4:]) / 4.0 if len(v) >= 4 else 1.0
    vol_96 = sum(v[-96:]) / min(96, len(v)) if v else 1.0
    vol_ratio = vol_4 / max(vol_96, 1e-6)

    # Swing window and impulse anchor
    swing_window = min(24, len(c) - 1)
    impulse_start = max(0, len(c) - 1 - swing_window)

    # Geometry for Model 2
    pb_geo = payload.get("pullback_geometry") if isinstance(payload, dict) else {}
    if isinstance(pb_geo, dict) and pb_geo.get("retrace") is not None and pb_geo.get("direction") == direction:
        geo = {
            "retrace": pb_geo["retrace"],
            "depth_sigma": pb_geo["depth_sigma"],
            "velocity_ratio": pb_geo["velocity_ratio"],
            "bars_pullback": pb_geo["bars_pullback"],
            "bars_impulse": pb_geo["bars_impulse"],
        }
        total_bars = int(pb_geo.get("bars_pullback", 0) + pb_geo.get("bars_impulse", 0))
        if total_bars > 0 and len(c) > total_bars:
            impulse_start = max(0, len(c) - 1 - total_bars)
    else:
        # Find recent swing pivot
        # The last candle is the proposed pullback, not an impulse pivot.
        previous = h[impulse_start:-1] if side == 1 else l[impulse_start:-1]
        swing_idx = impulse_start + int(np.argmax(previous) if side == 1 else np.argmin(previous))
        # D3: set impulse anchor to the extreme on far side of swing
        seg = l[impulse_start:swing_idx] if side == 1 else h[impulse_start:swing_idx]
        if len(seg) > 0:
            impulse_start = impulse_start + int(np.argmin(seg) if side == 1 else np.argmax(seg))
        if impulse_start >= swing_idx and swing_idx > 0:
            impulse_start = max(0, swing_idx - min(5, swing_idx))
        if swing_idx >= len(c) - 1 and len(c) > 2:
            swing_idx = len(c) - 2

        geo = pullback_geometry(h, l, c, direction, impulse_start=impulse_start,
                                swing_idx=swing_idx, sigma_bar=sigma_bar)

    # Structure intact
    if len(c) > 1 and impulse_start < len(c) - 1:
        if side == 1:
            structure_intact = c[-1] >= min(l[impulse_start:-1])
        else:
            structure_intact = c[-1] <= max(h[impulse_start:-1])
    else:
        structure_intact = True

    # Shelf confluence
    shelf_price = None
    confluence = 0
    candidates = []
    if pivots:
        candidates.extend([
            pivots.get("vwap"), pivots.get("P"), pivots.get("S1" if side == 1 else "R1"),
            pivots.get("bull_fvg_ce" if side == 1 else "bear_fvg_ce"),
            pivots.get("ema_20"), pivots.get("ema_50"),
            pivots.get("val" if side == 1 else "vah"), pivots.get("poc"),
        ])
    ci = features.get("causal_indicators") or (payload.get("causal_indicators") if isinstance(payload, dict) else {}) or {}
    candidates.extend([
        observed_vwap,
        ci.get("session_vwap_utc"),
        ci.get("ema_20"),
        ci.get("ema_50"),
    ])
    if payload and isinstance(payload, dict):
        vp = payload.get("volume_profile")
        if isinstance(vp, dict):
            candidates.extend([
                vp.get("val" if side == 1 else "vah"),
                vp.get("poc"),
            ])
    clean_candidates = [float(s) for s in candidates if s is not None and _finite_number(s) and float(s) > 0]
    distinct_shelves = []
    for cand in clean_candidates:
        if not any(abs(cand - prev) < max(0.01 * atr, 1e-4) for prev in distinct_shelves):
            distinct_shelves.append(cand)
    valid_shelves = [s for s in distinct_shelves if abs(entry - s) <= 0.35 * atr]
    confluence = len(valid_shelves)
    if valid_shelves:
        shelf_price = min(valid_shelves, key=lambda level: abs(entry - level))

    # First obstacle
    first_obstacle = None
    if pivots:
        first_obstacle = pivots.get("swing_high" if side == 1 else "swing_low")
    if first_obstacle is None and isinstance(ci, dict):
        first_obstacle = ci.get("swing_high" if side == 1 else "swing_low")
    if first_obstacle is not None and side * (first_obstacle - entry) <= 0:
        first_obstacle = None

    # Costs and sizing
    risk_usd = float(sizing.get("risk_usd", 12.0)) if sizing else 12.0
    cost_usd = float(sizing.get("friction_usd", 0.50)) if sizing else 0.50
    mid_px = (float(quote["bid"]) + float(quote["ask"])) / 2.0 if (_finite_number(quote.get("bid")) and _finite_number(quote.get("ask"))) else float(entry)
    spread_bps = (spread / mid_px * 1e4) if (mid_px > 0 and _finite_number(spread)) else 0.0
    stop_dist = abs(float(entry) - float(sl))
    spread_cost_usd = (risk_usd * spread / stop_dist) if (stop_dist > 0 and _finite_number(spread)) else cost_usd
    cost_usd = max(cost_usd, spread_cost_usd + float((sizing or {}).get("commission_usd", 0.0)))
    from Terminal.decision_gates_v3 import wall_band_atr
    band = wall_band_atr(stop_dist / atr if (atr > 0 and _finite_number(atr)) else float("nan"))

    # Orderflow tape extraction
    of_payload = payload.get("orderflow") if payload else None
    orderflow = None
    asset = canonical_asset(features.get("asset") or (payload or {}).get("coin") or symbol)
    allow_price_only = asset in {"GOLD", "SILVER", "USWTI", "SP500", "NAS100", "DJ30", "GER40", "EURUSD", "GBPUSD", "USDJPY"}
    if bool(features.get("allow_price_only_variant", False)) or bool((payload or {}).get("allow_price_only_variant", False)):
        allow_price_only = True

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
    elif payload and isinstance(payload, dict) and payload.get("cvd_1m_buckets"):
        buckets = payload.get("cvd_1m_buckets") or []
        if isinstance(buckets, list) and len(buckets) >= 15:
            try:
                deltas = [float(b.get("delta", 0.0)) for b in buckets if isinstance(b, dict)]
                last_15 = deltas[-15:]
                recent_5 = deltas[-5:]
                tot_abs = sum(abs(d) for d in last_15) or 1.0
                counter_aggr = sum(d for d in last_15 if (side == 1 and d < 0) or (side == -1 and d > 0))
                share = abs(counter_aggr) / tot_abs
                share = min(1.0, max(0.0, share))
                turned = 0
                for d in reversed(recent_5):
                    if (side == 1 and d > 0) or (side == -1 and d < 0):
                        turned += 1
                    else:
                        break
                orderflow = {
                    "cvd_push1": float(sum(deltas[:len(deltas)//2])),
                    "cvd_push2": float(sum(deltas[len(deltas)//2:])),
                    "aggr_usd_sweep": 0.0,
                    "aggr_usd_median_1m": 0.0,
                    "lambda_sweep": 1.0,
                    "lambda_median_60m": 1.0,
                    "bars_cvd_turned": float(turned),
                    "pullback_cvd_share": float(share),
                    "exhaustion_gate_ok": True,
                    "liq_burst_toward_entry": False,
                }
            except Exception:
                orderflow = None

    p_win_lower = features.get("p_win_lower_bound")
    if p_win_lower is None and isinstance(payload, dict):
        p_win_lower = payload.get("p_win_lower_bound")

    p_win_cal = features.get("p_win_lower_bound_calibrated")
    if p_win_cal is None and isinstance(payload, dict):
        p_win_cal = payload.get("p_win_lower_bound_calibrated")

    sample_n = features.get("p_win_calibration_sample_n")
    if sample_n is None and isinstance(payload, dict):
        sample_n = payload.get("p_win_calibration_sample_n")

    # Admissible if explicitly calibrated (e.g. n >= 100) OR supported by an audited
    # closed-trade sample with n >= 15 where exact Clopper-Pearson conservative penalty is applied.
    has_audited_sample = (
        isinstance(sample_n, (int, float))
        and not isinstance(sample_n, bool)
        and math.isfinite(sample_n)
        and sample_n >= 15
    )
    calibrated_admissible = (p_win_cal is True) or has_audited_sample

    if (not calibrated_admissible or isinstance(p_win_lower, bool)
            or not isinstance(p_win_lower, (int, float)) or not math.isfinite(p_win_lower)
            or not 0 <= p_win_lower <= 1):
        p_win_lower = None

    # Resting whale wall backing (Gates A3 & B5).
    #
    # POLICY (operator mandate #4): GENUINE L3 walls require gate_g7_eligible=true.
    # MIRRORED_LEG and TOP_OF_BOOK rows are bracket legs / touch prints, NOT net
    # directional inventory, and can NEVER satisfy whale backing -- no matter how
    # large or how long-lived they are. A 1.05M USD MIRRORED_LEG that has rested for
    # 2,476s is still one wallet's hedged bracket, not a resting bid.
    #
    # Non-eligible rows are therefore filtered out *before* selection rather than
    # merely deprioritised by the sort.
    wall_ctx = None
    wall_data_present = False
    if payload and isinstance(payload, dict):
        ob = payload.get("orderbook_live_depth", {}) or payload.get("orderbook", {})
        ob = ob if isinstance(ob, dict) else {}
        l3_walls = ob.get("whale_walls_l3") or payload.get("whale_walls_l3") or []
        l2_walls = ob.get("l2_wall_levels") or payload.get("l2_wall_levels") or []
        walls = (list(l3_walls) if isinstance(l3_walls, list) else []) + (list(l2_walls) if isinstance(l2_walls, list) else [])
        # A row only counts as G-7 eligible if it passes the same authenticity
        # predicate used for selection below. L2 touch rows and un-classified rows
        # carry no gate_g7_eligible key and are excluded, as are bracket legs and
        # rows with non-finite measurements.
        # Wallets laddering size on BOTH sides are market-making grids, not whales.
        # is_mirrored_leg only catches same-price brackets (0.05% proximity); a grid
        # spreads its legs across many prices and so classifies every leg GENUINE.
        # On the 2026-10-10 23:53 UTC snapshot that was 81.3% of qualifying notional,
        # and 17 of the 18 qualifying BTC bids within 0.25 ATR of mid.
        grid_addrs = two_sided_grid_addresses(walls)

        def _g7_eligible_row(w) -> bool:
            return (isinstance(w, dict)
                    and w.get("gate_g7_eligible") is True
                    and w.get("wall_class") == "GENUINE"
                    and str(w.get("address") or "").strip() not in grid_addrs
                    and all(_finite_number(w.get(k)) for k in
                            ("price", "notional_usd", "persist_s", "presence_frac")))

        wall_data_present = any(_g7_eligible_row(w) for w in walls)
        if walls:
            from Terminal.dg_hardening import select_backing_wall, venue_quotes_from_orderbook
            broker_mid = None
            if isinstance(quote, dict) and _finite_number(quote.get("bid")) and _finite_number(quote.get("ask")):
                q_bid, q_ask = float(quote["bid"]), float(quote["ask"])
                if q_bid > 0 and q_ask > 0:
                    broker_mid = (q_bid + q_ask) / 2.0
            if broker_mid is None:
                broker_mid = float(entry) if _finite_number(entry) and float(entry) > 0 else (float(c[-1]) if len(c) > 0 else None)
            broker_ts = None
            try:
                broker_ts = float(_quote_tick_msc(quote)) / 1000.0
            except (KeyError, TypeError, ValueError):
                broker_ts = None
            flow_usd = of_payload.get("median_1m_flow_usd") if isinstance(of_payload, dict) else None
            vq = venue_quotes_from_orderbook(ob, payload)
            require_clk = broker_ts is not None and any(q.get("ts") is not None for q in vq.values())
            wall_ctx, wall_diag = select_backing_wall(
                walls, entry=float(entry), side=side, atr=atr, tick=tick,
                broker_mid=broker_mid, broker_ts=broker_ts,
                venue_quotes=vq,
                grid_addrs=grid_addrs, flow_usd=flow_usd,
                require_clock=require_clk,
                band_atr=band,
            )
            if wall_ctx is None and any(k.startswith("venue_basis") for k in wall_diag.get("rejections", {})):
                missing.append("venue_basis_unverified")

    from Terminal.dg_hardening import derive_m1_range_override
    m1_override = derive_m1_range_override(
        features.get("m1_range_override") or (payload.get("m1_range_override") if isinstance(payload, dict) else None),
        (features.get("regime_stats") or {}).get("4h"),
        direction,
        orderflow_present=orderflow is not None
    )

    ctx = {
        "direction": direction,
        "regime": regime,
        "vwap_z": current_z if valid_session else None,
        "entry_z": entry_z if valid_session else None,
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
        "spread_bps": spread_bps,
        "wall_band_atr": band,
        "trend_tier": (features.get("regime_stats") or {}).get("trend_tier"),
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
        "allow_trend_continuation_target": bool(features.get("allow_trend_continuation_target", False)) or bool((payload or {}).get("allow_trend_continuation_target", False)),
        "orderflow": orderflow,
        "wall": wall_ctx,
        # True when the payload carried at least one G-7 eligible wall somewhere in
        # the book but none sat within 0.25 ATR behind this entry. Lets A3/B5 FAIL
        # closed instead of vacuously skipping when whale backing is knowable.
        "wall_data_present": wall_data_present,
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
            tick_msc = _quote_tick_msc(quote)
            if tick_msc is None:
                raise ValueError("quote tick time unavailable")
            as_of = tick_msc / 1000.0
            for history, period in ((bars_15m, 900), (bars_1h, 3600), (bars_4h, 14400)):
                raw_stamps = [_bar_open_ts(bar) for bar in history]
                if any(s is None for s in raw_stamps):
                    raise ValueError("bar open timestamp unavailable")
                stamps = [float(s) for s in raw_stamps]
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
        last_b15_ts = _bar_open_ts(bars_15m[-1])
        last_close = (float(last_b15_ts) + 900.0) if last_b15_ts is not None else 0.0
        # `as_of` above is the QUOTE timestamp and is correct for the causality
        # check, but wrong for staleness: a closed market's quote is frozen at
        # the same instant as its last bar, so their difference stays ~900s and
        # a 10-hour-old history reads as fresh. Staleness needs a real clock.
        if as_of_epoch is not None and (not _finite_number(as_of_epoch) or as_of_epoch <= 0):
            return {"regime": "UNDEFINED", "stats": {}, "passed": False,
                    "failures": ["as_of_epoch_invalid"], "metrics": {}}
        staleness_now = float(as_of_epoch) if as_of_epoch is not None else _time_mod.time()
        ci = (payload or {}).get("causal_indicators") or (features or {}).get("causal_indicators") or {}
        struct_sign = None
        try:
            bid_v = quote.get("bid")
            ask_v = quote.get("ask")
            mid_q = (float(bid_v) + float(ask_v)) / 2.0 if (_finite_number(bid_v) and _finite_number(ask_v)) else float(c15[-1])
            vw = ci.get("session_vwap_utc")
            tr = ci.get("trend_regime")
            if _finite_number(vw) and vw > 0:
                if tr == "BULLISH" and mid_q > vw:
                    struct_sign = 1
                elif tr == "BEARISH" and mid_q < vw:
                    struct_sign = -1
                elif len(c15) > 0:
                    e200 = ci.get("ema_200")
                    e200_slope = ci.get("ema_200_slope")
                    if _finite_number(e200) and e200 > 0:
                        if mid_q > vw and mid_q > e200 and (_finite_number(e200_slope) and e200_slope >= 0):
                            struct_sign = 1
                        elif mid_q < vw and mid_q < e200 and (_finite_number(e200_slope) and e200_slope <= 0):
                            struct_sign = -1
        except (KeyError, TypeError, ValueError):
            struct_sign = None

        try:
            regime, rstats = classify_regime(
                c15, c1h, c4h,
                last_close_epoch=last_close,
                as_of_epoch=staleness_now,
                structural_sign=struct_sign,
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

    features_augmented = dict(features)
    features_augmented["regime_stats"] = rstats
    ctx, missing = build_dg_context(
        features=features_augmented,
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
    elif regime == "MEAN_REVERT" or m1_range_override_ok(ctx):
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
