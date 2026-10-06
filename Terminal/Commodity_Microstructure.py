"""Commodity tick-volume microstructure: fusing candle VWAP with price action.

MT5 CFDs (XAUUSD.pi, XAGUSD.pi, US500.cash) expose no resting L3 ladder, but
they produce 7,000+ ticks per 15m candle. This module reconstructs the
microstructure evidence the crypto sleeves get from L2/L3:

  * ``robust_session_vwap`` - session-anchored (00:00 UTC) VWAP with BOTH the
    classic volume-weighted sigma and a volume-weighted MAD band
    (``sigma_mad = 1.4826 * wmedian(|tp - vwap|)``). The MAD band is immune to
    the deviation outliers that define the trade, so news bars cannot balloon
    the bands and erase the signal exactly when it matters; the
    ``ballooning_ratio = sigma_vw / sigma_mad`` flags news-contaminated
    sessions (ratio >> 1) for regime labelling.
  * ``volume_profile`` / ``tick_volume_profile`` - POC and 70% Value Area
    (VAH/VAL) from a tick histogram, or from bars via uniform range
    allocation when ticks are unavailable (flagged lower quality).
  * ``tick_delta`` - Lee-Ready tick-rule volume delta (up-tick vs down-tick
    notional) with bounce-probability caveats; the divergence signal for
    absorption at session extremes.
  * ``wick_rejection`` - pin-bar wick ratio and close position from OHLC
    (tick-exact when ticks are supplied to the caller's own aggregation).
  * ``commodity_mr_gate`` - the deterministic fusion gate for mean-reversion
    entries in Gold/Silver: robust VWAP extension (|z| >= 1.75), wick
    rejection (>= 0.50), close-back confirmation, and a fresh session
    extreme. No LLM input; the cognitive layer remains advisory.
  * ``gk_variance`` / ``gk_vol`` - Garman-Klass range volatility, ~7.4x more
    efficient than close-close on the same bar count, used by the exit
    architecture's chandelier trails.

All functions are pure and causal: bars are sorted, the forming bar is
excluded when ``now`` is supplied, and nothing reads the clock or the broker.
"""
from __future__ import annotations
import math
from datetime import datetime, timezone
import numpy as np
from Terminal.Asset_Universe import canonical_asset
from Terminal.Risk_Sizing_Engine import number, epoch

COMMODITIES = ("GOLD", "SILVER")
INDEXES = ("SP500",)


def weighted_median(values, weights):
    """Volume-weighted median: the smallest value whose cumulative weight
    reaches half the total (linear interpolation inside the straddling bin)."""
    pairs = [(float(v), float(w)) for v, w in zip(values, weights)
             if w > 0 and math.isfinite(float(v))]
    if not pairs:
        return None
    pairs.sort(key=lambda p: p[0])
    total = sum(w for _, w in pairs)
    cumulative = 0.0
    for v, w in pairs:
        cumulative += w
        if cumulative >= total/2.0:
            return v
    return pairs[-1][0]


def _ordered_bars(bars, now=None):
    ordered = sorted((b for b in (bars or [])
                      if number(b.get("close")) > 0 and epoch(b.get("time")) > 0),
                     key=lambda b: epoch(b["time"]))
    if now is not None:
        ordered = [b for b in ordered if epoch(b["time"])+900 <= now]
    return ordered


def robust_session_vwap(bars, now=None, min_session_bars=8, rolling=96):
    """Session VWAP (00:00 UTC anchor) with volume-weighted MAD bands.

    Falls back to a rolling 96-bar window when the session has fewer than
    ``min_session_bars`` completed bars (early session), mirroring the
    primary-VWAP selection rule of the candle engine.
    """
    ordered = _ordered_bars(bars, now)
    if len(ordered) < 14:
        return None
    times = [epoch(b["time"]) for b in ordered]
    last = datetime.fromtimestamp(times[-1], timezone.utc)
    midnight = datetime(last.year, last.month, last.day, tzinfo=timezone.utc).timestamp()
    session = [b for b, t in zip(ordered, times) if t >= midnight]
    used = "session" if len(session) >= min_session_bars else "rolling"
    window = session if used == "session" else ordered[-rolling:]
    tps = np.array([(number(b["high"])+number(b["low"])+number(b["close"]))/3.0 for b in window])
    vols = np.array([max(number(b.get("volume") or b.get("tick_volume") or 1.0), 1e-9) for b in window])
    total = float(vols.sum())
    vwap = float((tps*vols).sum()/total)
    devs = np.abs(tps-vwap)
    sigma_vw = math.sqrt(float((vols*devs**2).sum()/total))
    wm = weighted_median(devs.tolist(), vols.tolist())
    sigma_mad = 1.4826*wm if wm else 0.0
    if not sigma_mad > 1e-12:
        sigma_mad = sigma_vw
    close = number(ordered[-1]["close"])
    z = (close-vwap)/sigma_mad if sigma_mad > 1e-12 else 0.0
    return {"used": used, "session_bars": len(session), "vwap": vwap,
            "sigma_vw": sigma_vw, "sigma_mad": sigma_mad,
            "ballooning_ratio": sigma_vw/max(sigma_mad, 1e-12),
            "vwap_z_robust": z, "last_close": close,
            "upper_1": vwap+sigma_mad, "lower_1": vwap-sigma_mad,
            "upper_2": vwap+2.0*sigma_mad, "lower_2": vwap-2.0*sigma_mad,
            "upper_3": vwap+3.0*sigma_mad, "lower_3": vwap-3.0*sigma_mad}


def volume_profile(bars, bins=240, value_area=0.70, now=None, window=96):
    """POC / VAH / VAL from bars via uniform range allocation (fallback when
    no tick capture is available; prefer ``tick_volume_profile``)."""
    ordered = _ordered_bars(bars, now)[-window:]
    if len(ordered) < 2:
        return None
    lo = min(number(b["low"]) for b in ordered)
    hi = max(number(b["high"]) for b in ordered)
    if not hi > lo:
        return None
    bin_size = (hi-lo)/bins
    hist = np.zeros(bins)
    for b in ordered:
        v = max(number(b.get("volume") or b.get("tick_volume") or 1.0), 1e-9)
        i0 = min(bins-1, max(0, int((number(b["low"])-lo)/bin_size)))
        i1 = min(bins-1, max(0, int((number(b["high"])-lo)/bin_size)))
        if i1 >= i0:
            hist[i0:i1+1] += v/(i1-i0+1)
    return _profile_from_hist(hist, lo, bin_size, value_area)


def tick_volume_profile(ticks, lo=None, hi=None, bins=480, value_area=0.70):
    """Exact POC / VAH / VAL from tick prices and sizes."""
    pts = [(number(t.get("price")), number(t.get("size")) or number(t.get("volume")) or 0.0)
           for t in (ticks or [])]
    pts = [(p, s) for p, s in pts if p > 0 and s > 0]
    if len(pts) < 2:
        return None
    if lo is None:
        lo = min(p for p, _ in pts)
    if hi is None:
        hi = max(p for p, _ in pts)
    if not hi > lo:
        return None
    bin_size = (hi-lo)/bins
    hist = np.zeros(bins)
    for p, s in pts:
        idx = min(bins-1, max(0, int((p-lo)/bin_size)))
        hist[idx] += s
    return _profile_from_hist(hist, lo, bin_size, value_area)


def _profile_from_hist(hist, lo, bin_size, value_area):
    total = float(hist.sum())
    if total <= 0:
        return None
    poc_i = int(np.argmax(hist))
    va = float(hist[poc_i])
    lo_i = hi_i = poc_i
    while va < value_area*total and (lo_i > 0 or hi_i < len(hist)-1):
        down = float(hist[lo_i-1]) if lo_i > 0 else -1.0
        up = float(hist[hi_i+1]) if hi_i < len(hist)-1 else -1.0
        if up >= down and up >= 0:
            hi_i += 1
            va += up
        elif down >= 0:
            lo_i -= 1
            va += down
        else:
            break
    return {"poc": lo+(poc_i+0.5)*bin_size, "vah": lo+(hi_i+1)*bin_size,
            "val": lo+lo_i*bin_size, "bin_size": bin_size, "total_volume": total,
            "value_area_captured": va/total}


def tick_delta(ticks):
    """Lee-Ready tick-rule volume delta: sign(t) = sign(p_t - p_{t-1}),
    zero increments inherit the previous sign (bounce cases are the known
    misclassification cost of the tick test)."""
    buy = sell = 0.0
    last_sign = 0
    prev = None
    for t in sorted(ticks or [], key=lambda t: epoch(t.get("time"))):
        p = number(t.get("price"))
        if p <= 0:
            continue
        v = number(t.get("notional_usd")) or p*number(t.get("size"))
        if prev is not None:
            sign = 1 if p > prev else (-1 if p < prev else last_sign)
        else:
            sign = 0
        if sign > 0:
            buy += v
        elif sign < 0:
            sell += v
        if sign:
            last_sign = sign
        prev = p
    total = buy+sell
    return {"buy_usd": buy, "sell_usd": sell, "delta_usd": buy-sell,
            "delta_norm": (buy-sell)/total if total > 0 else 0.0, "total_usd": total}


def wick_rejection(bars, now=None):
    """Pin-bar geometry of the latest completed bar: wick ratios and the
    close position inside the range (tick-exact aggregation is the caller's
    upgrade path; this bar-level proxy is the always-available floor)."""
    ordered = _ordered_bars(bars, now)
    if not ordered:
        return {"upper_ratio": 0.0, "lower_ratio": 0.0, "close_pos": 0.5}
    b = ordered[-1]
    o, h, l, c = (number(b["open"]), number(b["high"]), number(b["low"]), number(b["close"]))
    rng = h-l
    if rng <= 0:
        return {"upper_ratio": 0.0, "lower_ratio": 0.0, "close_pos": 0.5}
    return {"upper_ratio": (h-max(o, c))/rng, "lower_ratio": (min(o, c)-l)/rng,
            "close_pos": (c-l)/rng}


def commodity_mr_gate(bars, direction, now=None, z_threshold=1.75,
                      wick_min=0.50, close_pos_max=0.45):
    """Deterministic mean-reversion confirmation for Gold/Silver entries.

    Requires, in order: robust-VWAP extension of the trigger bar's SESSION
    EXTREME (|z_extreme| >= 1.75 measured at the wick, because the required
    close-back confirmation has already pulled the close inside the band),
    an opposing wick of at least half the bar's range, a close back inside
    that range, and a fresh session extreme on the trigger bar (liquidity
    rejection at the session high/low). Returns dict(confirmed, reason, ...).
    """
    sess = robust_session_vwap(bars, now)
    if not sess:
        return {"confirmed": False, "reason": "history_insufficient", "session": None}
    sigma = sess["sigma_mad"] if sess["sigma_mad"] > 1e-12 else sess["sigma_vw"]
    if sigma <= 1e-12:
        return {"confirmed": False, "reason": "zero_dispersion", "session": sess}
    wick = wick_rejection(bars, now)
    ordered = _ordered_bars(bars, now)
    trigger = ordered[-1]
    extreme = number(trigger["high"]) if direction == "SHORT" else number(trigger["low"])
    z_extreme = (extreme-sess["vwap"])/sigma if direction == "SHORT" \
        else (extreme-sess["vwap"])/sigma
    if direction == "SHORT" and not z_extreme >= z_threshold:
        return {"confirmed": False, "reason": f"vwap_extension_missing:z_{z_extreme:.2f}",
                "session": sess, "wick": wick}
    if direction == "LONG" and not z_extreme <= -z_threshold:
        return {"confirmed": False, "reason": f"vwap_extension_missing:z_{z_extreme:.2f}",
                "session": sess, "wick": wick}
    ratio = wick["upper_ratio"] if direction == "SHORT" else wick["lower_ratio"]
    if ratio < wick_min:
        return {"confirmed": False, "reason": f"wick_rejection_missing:{ratio:.2f}",
                "session": sess, "wick": wick}
    close_ok = wick["close_pos"] <= close_pos_max if direction == "SHORT" \
        else wick["close_pos"] >= 1.0-close_pos_max
    if not close_ok:
        return {"confirmed": False, "reason": f"close_position_unconfirmed:{wick['close_pos']:.2f}",
                "session": sess, "wick": wick}
    times = [epoch(b["time"]) for b in ordered]
    last = datetime.fromtimestamp(times[-1], timezone.utc)
    midnight = datetime(last.year, last.month, last.day, tzinfo=timezone.utc).timestamp()
    session_bars = [b for b, t in zip(ordered, times) if t >= midnight]
    if len(session_bars) >= 2:
        if direction == "SHORT":
            extreme_ok = extreme >= max(number(b["high"]) for b in session_bars[:-1])-1e-9
        else:
            extreme_ok = extreme <= min(number(b["low"]) for b in session_bars[:-1])+1e-9
        if not extreme_ok:
            return {"confirmed": False, "reason": "session_extreme_missing",
                    "session": sess, "wick": wick}
    return {"confirmed": True, "reason": "ok", "session": sess, "wick": wick,
            "z_extreme": z_extreme, "z_close": sess["vwap_z_robust"]}


def commodity_override(base, bars, now=None):
    """Merge session-anchored robust anchors into the pivot dict.

    Replaces the rolling 96-bar VWAP fields with the session VWAP + MAD band
    (when the session has >= 8 completed bars) and adds POC/VAH/VAL so the
    entry hierarchy and structural TP can use them on CFDs without L3.
    """
    out = dict(base or {})
    sess = robust_session_vwap(bars, now)
    if sess and sess["used"] == "session" and sess["session_bars"] >= 8:
        out.update(vwap=sess["vwap"], vwap_sigma=sess["sigma_mad"],
                   vwap_upper_1=sess["upper_1"], vwap_lower_1=sess["lower_1"],
                   vwap_upper_2=sess["upper_2"], vwap_lower_2=sess["lower_2"],
                   vwap_ballooning_ratio=sess["ballooning_ratio"],
                   vwap_z_robust=sess["vwap_z_robust"],
                   vwap_session_sigma_vw=sess["sigma_vw"])
    profile = volume_profile(bars, now=now)
    if profile:
        out.update(poc=profile["poc"], vah=profile["vah"], val=profile["val"])
    return out


# ------------------------------------------------------------ Garman-Klass
def gk_variance(bar):
    """Per-bar Garman-Klass log-price variance:
    0.5*ln^2(H/L) - (2 ln 2 - 1)*ln^2(C/O)."""
    o, h, l, c = (number(bar.get("open")), number(bar.get("high")),
                  number(bar.get("low")), number(bar.get("close")))
    if min(o, h, l, c) <= 0 or h <= l:
        return 0.0
    hl = math.log(h/l)
    co = math.log(c/o)
    return max(0.0, 0.5*hl*hl - (2.0*math.log(2.0)-1.0)*co*co)


def gk_vol(bars, lookback=14, now=None):
    """Per-bar GK log-price sigma over the last ``lookback`` completed bars.
    Roughly 7.4x more efficient than the close-close estimator on the same
    bar count, so 14 bars carry the information of ~100 close-close bars."""
    ordered = _ordered_bars(bars, now)
    vals = [gk_variance(b) for b in ordered[-lookback:]]
    vals = [v for v in vals if v > 0]
    return math.sqrt(sum(vals)/len(vals)) if vals else 0.0
