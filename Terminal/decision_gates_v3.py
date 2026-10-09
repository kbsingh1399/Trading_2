"""decision_gates_v3.py -- reference implementation for the Round-2 audit.

Pure, deterministic, dependency-light (numpy only; MT5 module injected).
Drop into Terminal/ and wire behind the existing admission path.

Contents
  1. Estimators ........ yang_zhang_sigma, efficiency_ratio, variance_ratio,
                         slope_tstat_nw
  2. Regime router ..... classify_regime  (regime FIRST, Z only as location)
  3. Checklist A ....... model1_checklist (extreme mean reversion)
  4. Checklist B ....... model2_checklist (trend pullback)
  5. Invalidation ...... resting_order_invalidation
  6. Hold/Cut/BE ....... hold_cut_decision, net_breakeven_stop
  7. Pre-send gate ..... pre_send_gate (MT5 millisecond revalidation)
  8. Toxicity .......... markout_report (adverse-selection proof on CFDs)

EVERY THRESHOLD BELOW IS A PRIOR, NOT A FITTED VALUE. With 17 closed trades
nothing here is statistically calibrated; tune via purged walk-forward and
shadow fills before promotion (see audit report, section 8).
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence

import numpy as np

# ============================================================== 0. results
@dataclass
class Verdict:
    passed: bool
    failures: List[str] = field(default_factory=list)
    metrics: Dict[str, float] = field(default_factory=dict)

    def require(self, cond: bool, code: str) -> None:
        if not cond:
            self.failures.append(code)
            self.passed = False


def _arr(x) -> np.ndarray:
    return np.asarray(x, dtype=float)


# ============================================================ 1. estimators
def yang_zhang_sigma(o, h, l, c, n: int = 32) -> Optional[float]:
    """Per-bar log volatility (Yang-Zhang 2000), last n bars.

    sigma^2 = s_o^2 + k s_c^2 + (1-k) s_RS^2,  k = 0.34/(1.34 + (n+1)/(n-1)).
    On 24h instruments the 'overnight' term is prev-close->open (gaps at
    session breaks / weekend), which is exactly the risk ATR understates.
    """
    o, h, l, c = map(_arr, (o, h, l, c))
    if len(c) < n + 1:
        return None
    o, h, l, c_prev, c = o[-n:], h[-n:], l[-n:], c[-n - 1:-1], c[-n:]
    ro = np.log(o / c_prev)
    rc = np.log(c / o)
    u, d = np.log(h / o), np.log(l / o)
    rs = u * (u - rc) + d * (d - rc)
    k = 0.34 / (1.34 + (n + 1) / (n - 1))
    var = ro.var(ddof=1) + k * rc.var(ddof=1) + (1 - k) * rs.mean()
    return float(math.sqrt(max(var, 0.0)))


def efficiency_ratio(closes, n: int) -> Optional[float]:
    c = _arr(closes)
    if len(c) < n + 1:
        return None
    path = np.abs(np.diff(c[-n - 1:])).sum()
    return float(abs(c[-1] - c[-n - 1]) / path) if path > 0 else 0.0


def variance_ratio(closes, q: int = 4, n: Optional[int] = None):
    """Lo-MacKinlay VR(q) with heteroskedasticity-robust z* (M2)."""
    lp = np.log(_arr(closes))
    if n:
        lp = lp[-n - 1:]
    x = np.diff(lp)
    T = len(x)
    if T < 4 * q:
        return None, None
    mu = x.mean()
    var1 = ((x - mu) ** 2).sum() / (T - 1)
    xq = lp[q:] - lp[:-q]
    m = q * (T - q + 1) * (1 - q / T)
    varq = ((xq - q * mu) ** 2).sum() / m
    vr = varq / var1 if var1 > 0 else 1.0
    d2 = (x - mu) ** 2
    den = d2.sum() ** 2
    if den <= 0:
        return float(vr), 0.0
    phi = 0.0
    for j in range(1, q):
        delta = T * (d2[j:] * d2[:-j]).sum() / den
        phi += (2 * (q - j) / q) ** 2 * delta
    # delta(j) carries the factor T (Lo-MacKinlay 1990 correction), so
    # z* = sqrt(T) * (VR - 1) / sqrt(theta).
    z = math.sqrt(T) * (vr - 1) / math.sqrt(phi) if phi > 0 else 0.0
    return float(vr), float(z)


def slope_tstat_nw(closes, n: int, lags: Optional[int] = None) -> Optional[float]:
    """OLS slope of log price on time, Newey-West HAC t-stat.

    NOTE: regressing a random walk *level* on time inflates naive t-stats;
    HAC with lag ~ n^(1/3)*... still over-rejects. Use as a ranking
    feature with a high bar (|t|>2.5) and combine with ER/VR, never alone.
    """
    y = np.log(_arr(closes))[-n:]
    if len(y) < n or n < 10:
        return None
    t = np.arange(n, dtype=float)
    X = np.column_stack([np.ones(n), t])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    e = y - X @ beta
    L = lags if lags is not None else int(math.floor(4 * (n / 100) ** (2 / 9)))
    Xe = X * e[:, None]
    S = Xe.T @ Xe
    for k in range(1, L + 1):
        w = 1 - k / (L + 1)
        G = Xe[k:].T @ Xe[:-k]
        S += w * (G + G.T)
    XtX_inv = np.linalg.inv(X.T @ X)
    V = XtX_inv @ S @ XtX_inv
    se = math.sqrt(max(V[1, 1], 1e-300))
    return float(beta[1] / se)


# ========================================================= 2. regime router
@dataclass
class RegimeParams:
    er_trend: float = 0.35
    er_mr: float = 0.20
    t_trend: float = 2.5
    t_flat: float = 1.0
    vr_q: int = 4
    vr_z_trend: float = 1.0
    vr_z_mr: float = -1.5
    n_15m: int = 96
    n_1h: int = 48
    n_4h: int = 30


def _tf_stats(closes, n, p: RegimeParams):
    er = efficiency_ratio(closes, n)
    vr, vz = variance_ratio(closes, p.vr_q, n)
    t = slope_tstat_nw(closes, n)
    return {"er": er, "vr": vr, "vr_z": vz, "t": t}


def classify_regime(closes_15m, closes_1h, closes_4h, p: RegimeParams = RegimeParams()):
    """Returns (regime, stats).

    TREND_UP / TREND_DOWN : HTF (4H and 1H) agree, 1H passes >=2 of 3 tests.
    MEAN_REVERT           : 1H flat AND 15m anti-persistent.
    UNDEFINED             : everything else -> BOTH ENGINES STAND ASIDE.
    The 15m is deliberately NOT required to trend: during a pullback it
    is counter-trend by construction.
    """
    s15 = _tf_stats(closes_15m, p.n_15m, p)
    s1h = _tf_stats(closes_1h, p.n_1h, p)
    s4h = _tf_stats(closes_4h, p.n_4h, p)
    stats = {"15m": s15, "1h": s1h, "4h": s4h}
    if any(v is None for s in (s1h, s4h) for v in (s["er"], s["t"])):
        return "UNDEFINED", stats
    for sign, name in ((1, "TREND_UP"), (-1, "TREND_DOWN")):
        votes = sum([
            sign * s1h["t"] > p.t_trend,
            s1h["er"] > p.er_trend and sign * (closes_1h[-1] - closes_1h[-p.n_1h - 1]) > 0,
            (s1h["vr_z"] or 0) > p.vr_z_trend,
        ])
        htf_ok = sign * s4h["t"] > 1.5 and s4h["er"] > 0.25
        if votes >= 2 and htf_ok:
            return name, stats
    # No slope t-stat here: on an I(1) price level it is spuriously large.
    if (s1h["er"] < p.er_mr and (s4h["er"] if s4h["er"] is not None else 1.0) < 0.30
            and s15["vr_z"] is not None and s15["vr_z"] < p.vr_z_mr):
        return "MEAN_REVERT", stats
    return "UNDEFINED", stats


# =================================================== 3. Checklist A (Model 1)
def model1_checklist(ctx: dict) -> Verdict:
    """Extreme mean reversion. ctx keys documented inline.

    Hard rule: Model 1 is admissible ONLY in regime MEAN_REVERT. In a trend,
    |Z|>=2 on a session VWAP means the path is *accelerating* (a linear
    trend saturates near Z~1.7), i.e. it selects cascades, not exhaustion.
    """
    v = Verdict(True)
    side = 1 if ctx["direction"] == "LONG" else -1
    z, dz4 = ctx["vwap_z"], ctx["vwap_z_change_4bars"]
    atr, sig_s = ctx["atr"], ctx["session_sigma"]
    v.metrics.update(z=z, dz4=dz4)
    # --- A1 regime + geometry
    v.require(ctx["regime"] == "MEAN_REVERT", "A1_regime_not_mean_revert")
    z_sweep = ctx.get("sweep_z", z)
    v.metrics["z_sweep"] = z_sweep
    v.require(-side * z_sweep >= 2.0, "A1_z_below_2")
    v.require(-side * z_sweep <= 3.5, "A1_z_beyond_3p5_cascade_zone")
    v.require(ctx["session_bars"] >= 16, "A1_session_sigma_immature_lt16bars")
    v.require(sig_s >= 0.8 * atr, "A1_session_sigma_lt_0p8atr")
    v.require(abs(ctx["vwap_slope_sigma_per_bar"]) <= 0.05, "A1_vwap_sloped")
    v.require(-side * dz4 <= 0.75, "A1_z_still_accelerating")
    v.require(ctx["vol_ratio_4_96"] <= 2.0, "A1_vol_shock")
    # --- A2 orderflow (crypto only; CFDs without tape fail closed; no price-only bypass for Model 1)
    of = ctx.get("orderflow")
    v.require(of is not None, "A2_no_tape_fail_closed")
    if of is not None:
        # divergence: second push's adverse CVD <= 70% of first push's
        leg1, leg2 = of["cvd_push1"], of["cvd_push2"]
        div = (abs(leg2) / abs(leg1)) if leg1 else 9.9
        v.metrics["cvd_push_ratio"] = div
        v.require(side * leg1 < 0 and div <= 0.70, "A2_no_cvd_divergence")
        # absorption: aggression present but impact per $ collapsed
        v.require(of["aggr_usd_sweep"] >= 2.0 * of["aggr_usd_median_1m"], "A2_no_aggression_to_absorb")
        lam_ratio = of["lambda_sweep"] / max(of["lambda_median_60m"], 1e-12)
        v.metrics["lambda_ratio"] = lam_ratio
        v.require(lam_ratio <= 0.50, "A2_impact_not_absorbed")
        v.require(of["bars_cvd_turned"] >= 3, "A2_cvd_not_turned_3x1m")
    # --- A3 resting depth (informational on CFDs: other venue)
    wall = ctx.get("wall")
    if wall is not None:
        v.require(wall["usd"] >= max(150_000, 5 * wall["median_1m_traded_usd"]), "A3_wall_too_small_vs_flow")
        v.require(wall["persist_s"] >= 180 and wall["presence_frac"] >= 0.9, "A3_wall_not_persistent")
        v.require(wall["dist_from_entry_atr"] <= 0.25, "A3_wall_not_behind_entry")
    # --- A4 flush completed
    fl = ctx.get("flush")
    if fl is not None:
        v.require(fl["peak_liq_1m"] >= 3 * fl["median_liq_1m_24h"], "A4_no_real_flush")
        v.require(fl["last_liq_1m"] <= 0.2 * fl["peak_liq_1m"], "A4_flush_ongoing")
        v.require(fl["oi_change_5m_pct"] >= -0.10, "A4_oi_still_falling")
    v.require(ctx["reclaim_close"], "A4_no_close_back_inside_sweep")
    # --- A5 geometry & net expectancy
    entry, sl, tp = ctx["entry"], ctx["sl"], ctx["tp"]
    r = abs(entry - sl)
    v.require(side * (entry - ctx["sweep_extreme"]) > 0, "A5_entry_not_inside_sweep")
    v.require(side * (ctx["sweep_extreme"] - sl) >= 0.2 * atr + ctx["spread"], "A5_stop_not_beyond_sweep_buffer")
    v.require(r >= 1.0 * atr, "A5_stop_lt_1atr")
    rr = side * (tp - entry) / r if r > 0 else 0
    v.metrics["rr_gross"] = rr
    v.require(side * (ctx["vwap"] - tp) >= 0, "A5_tp_beyond_vwap")
    _net_ev(v, ctx, rr, min_rr=1.5)
    return v


# =================================================== 4. Checklist B (Model 2)
def pullback_geometry(highs, lows, closes, direction, impulse_start: int, swing_idx: int,
                      sigma_bar: float):
    """Retrace fraction, depth in sigma units, velocity ratio pullback/impulse."""
    h, l, c = map(_arr, (highs, lows, closes))
    s = 1 if direction == "LONG" else -1
    if s == 1:
        a, ext = l[impulse_start], h[swing_idx]
    else:
        a, ext = h[impulse_start], l[swing_idx]
    p = c[-1]
    leg = abs(ext - a)
    # A breakout beyond the impulse extreme is not a pullback.
    retr = s * (ext - p) / leg if leg > 0 else 0.0
    n_imp = max(swing_idx - impulse_start, 1)
    n_pb = max(len(c) - 1 - swing_idx, 1)
    depth_sigma = abs(math.log(ext / p)) / (sigma_bar * math.sqrt(n_pb))
    v_imp = abs(math.log(ext / a)) / n_imp
    v_pb = abs(math.log(ext / p)) / n_pb
    return {"retrace": retr, "depth_sigma": depth_sigma,
            "velocity_ratio": v_pb / v_imp if v_imp > 0 else 9.9,
            "bars_pullback": n_pb, "bars_impulse": n_imp}


def model2_checklist(ctx: dict) -> Verdict:
    v = Verdict(True)
    side = 1 if ctx["direction"] == "LONG" else -1
    atr, sig = ctx["atr"], ctx["sigma_bar"]
    # --- B1 regime
    want = "TREND_UP" if side == 1 else "TREND_DOWN"
    v.require(ctx["regime"] == want, "B1_regime_mismatch")
    # --- B2 pullback geometry (true pullback vs exhaustion rollover)
    g = ctx["geometry"]
    v.metrics.update({f"geo_{k}": val for k, val in g.items()})
    v.require(0.236 <= g["retrace"] <= 0.618, "B2_retrace_outside_0236_0618")
    v.require(g["depth_sigma"] <= 2.0, "B2_pullback_too_fast")
    v.require(g["velocity_ratio"] <= 0.60, "B2_pullback_velocity_ge_impulse")
    v.require(ctx["structure_intact"], "B2_15m_higher_low_broken")
    ex = ctx["exhaustion_flags"]
    v.metrics["exhaustion_count"] = sum(bool(x) for x in ex.values())
    v.require(v.metrics["exhaustion_count"] <= 1, "B2_exhaustion_rollover")
    # --- B3 shelf
    shelf = ctx.get("shelf")
    if not shelf or shelf.get("price") is None:
        v.require(False, "B3_no_shelf_defined")
    else:
        v.require(abs(ctx["entry"] - shelf["price"]) <= 0.25 * atr, "B3_entry_not_at_shelf")
        v.require(shelf.get("confluence", 0) >= 2, "B3_single_source_shelf")
    # --- B4 orderflow (crypto)
    of = ctx.get("orderflow")
    if of is None:
        v.require(ctx.get("allow_price_only_variant", False), "B4_no_tape_fail_closed")
    else:
        v.require(of["pullback_cvd_share"] <= 0.5, "B4_pullback_on_heavy_counter_aggression")
        v.require(of["exhaustion_gate_ok"], "B4_taker_delta_not_exhausted_at_shelf")
        v.require(not of["liq_burst_toward_entry"], "B4_liquidation_burst_into_shelf")
    # --- B5 wall (informational)
    wall = ctx.get("wall")
    if wall is not None:
        v.require(wall["persist_s"] >= 180 and wall["presence_frac"] >= 0.9, "B5_wall_not_persistent")
        v.require(wall["dist_from_entry_atr"] <= 0.25, "B5_wall_not_behind_entry")
    # --- B6 target & net EV
    entry, sl, tp = ctx["entry"], ctx["sl"], ctx["tp"]
    r = abs(entry - sl)
    v.require(r >= 1.5 * atr, "B6_stop_lt_1p5atr")
    obstacle = ctx.get("first_obstacle")          # swing high / ask wall >= 2M
    v.require(obstacle is not None, "B6_first_obstacle_missing")
    if obstacle is not None:
        v.require(side * (obstacle - tp) >= 2 * ctx["tick"], "B6_tp_beyond_first_obstacle")
    rr = side * (tp - entry) / r if r > 0 else 0
    v.metrics["rr_gross"] = rr
    _net_ev(v, ctx, rr, min_rr=2.0)
    return v


def _net_ev(v: Verdict, ctx: dict, rr: float, min_rr: float) -> None:
    """Net R-multiple after spread+commission and stop slippage, and the
    break-even win probability that the strategy's LOWER bound must beat."""
    risk_usd = ctx["risk_usd"]
    c = ctx["round_trip_cost_usd"] / risk_usd           # friction in R
    s = ctx.get("stop_slip_r", 0.10)                    # stop slippage in R
    win, loss = rr - c, 1 + c + s
    p_star = loss / (win + loss) if win > 0 else 1.0
    v.metrics.update(net_win_r=win, net_loss_r=loss, p_breakeven=p_star)
    v.require(rr >= min_rr, f"EV_rr_below_{min_rr}")
    v.require(c <= 0.15, "EV_friction_gt_0p15R")
    p_lo = ctx.get("p_win_lower_bound")
    v.require(p_lo is not None, "EV_p_win_lower_bound_missing")
    if p_lo is not None:
        v.metrics["ev_lower_r"] = p_lo * win - (1 - p_lo) * loss
        v.require(p_lo >= p_star + 0.03, "EV_lower_bound_below_breakeven")


# ============================================== 5. resting-order invalidation
HARD, SOFT = "HARD", "SOFT"


def resting_order_invalidation(o: dict, m: dict):
    """Return ('CANCEL'|'KEEP', reasons). HARD alone cancels; SOFT needs 2.

    On MT5 CFDs there is no queue to lose, so cancel cost ~ 0: bias to cancel.
    """
    s = 1 if o["direction"] == "LONG" else -1
    atr, sig = o["atr"], m["sigma_bar"]
    ev = []
    # structural / regime
    if m["regime"] != o["regime_at_stage"]:
        ev.append((HARD, "regime_changed"))
    if m["new_counter_swing"]:                       # LL for longs / HH for shorts
        ev.append((HARD, "counter_structure_formed_before_fill"))
    dist = s * (m["mid"] - o["limit"])               # >0 = price above buy limit
    v_app = -s * m["ret_3bars_log"] / (sig * math.sqrt(3))
    if 0 <= dist <= 1.0 * atr and v_app > 2.0:
        ev.append((HARD, f"fast_approach_{v_app:.2f}sigma"))
    if dist > 2.0 * atr:
        ev.append((HARD, "drift_gt_2atr"))
    if m["minutes_resting"] > o["ttl_minutes"]:
        ev.append((HARD, "ttl_diffusion_expired"))
    if m["macro_blackout"] or m["spread_bps"] > max(1.0, 2.5 * m["spread_median_bps"]):
        ev.append((HARD, "context_blackout_or_spread"))
    # orderflow (crypto; None = unobservable, adds nothing)
    w = m.get("wall_retained_frac")
    if w is not None and w < 0.5 and o.get("wall_is_primary_thesis"):
        ev.append((HARD, "primary_wall_pulled"))
    if m.get("liq_burst_toward_limit"):
        ev.append((HARD, "liquidation_cascade_toward_limit"))
    if m.get("aggr_share_toward_5m") is not None and m["aggr_share_toward_5m"] >= 0.65:
        ev.append((SOFT, "aggressor_pressure"))
    if m.get("lambda_ratio") is not None and m["lambda_ratio"] >= 1.5:
        ev.append((SOFT, "impact_rising_no_absorption"))
    if m.get("depth_near_limit_change") is not None and m["depth_near_limit_change"] <= -0.5:
        ev.append((SOFT, "depth_near_limit_thinned_50pct"))
    if m.get("poc_migration_atr") is not None and -s * m["poc_migration_atr"] >= 0.5:
        ev.append((SOFT, "value_migrating_through_limit"))
    if m.get("ref_basis_bps") is not None and abs(m["ref_basis_bps"]) > m.get("ref_basis_limit_bps", 15):
        ev.append((SOFT, "broker_reference_divergence"))
    hard = [r for k, r in ev if k == HARD]
    soft = [r for k, r in ev if k == SOFT]
    if hard or len(soft) >= 2:
        return "CANCEL", hard + soft
    return "KEEP", soft


def diffusion_ttl_minutes(dist_at_stage: float, sigma_bar_price: float, bar_minutes: int = 15,
                          mult: float = 2.0, min_ttl_minutes: float = 15.0) -> float:
    """Expected first-passage scale ~ (d/sigma)^2 bars; computed ONCE at order staging.
    Do NOT recompute on live shrinking distance, as dist -> 0 near fill would shrink TTL to 0!
    """
    if sigma_bar_price <= 0:
        return min_ttl_minutes
    ttl = mult * (dist_at_stage / sigma_bar_price) ** 2 * bar_minutes
    return max(float(ttl), min_ttl_minutes)


# ================================================ 6. hold / cut / breakeven
def p_hit_upper(x: float, lo: float, hi: float, mu: float = 0.0, sig: float = 1.0) -> float:
    """P(Brownian with drift mu, vol sig hits hi before lo) from x."""
    if abs(mu) < 1e-12:
        return (x - lo) / (hi - lo)
    sfun = lambda y: math.exp(-2 * mu * y / sig ** 2)
    return (sfun(x) - sfun(lo)) / (sfun(hi) - sfun(lo))


def hold_cut_decision(st: dict):
    """st (all in R units): x (current), stop (current stop, e.g. -1),
    tp, mu_hat (drift per bar, from evidence), sig (per-bar vol in R),
    exit_cost (R), be_level (net-BE stop in R), hard_invalidation (bool).

    Returns ('HOLD'|'CUT'|'MOVE_BE', metrics).
    Under mu_hat = 0 every option has the same gross EV (optional stopping),
    so CUT/BE only win when evidence says drift has turned against us.
    """
    x, lo, tp, mu, sg = st["x"], st["stop"], st["tp"], st["mu_hat"], st["sig"]
    if st.get("hard_invalidation"):
        return "CUT", {"reason": "hard_invalidation"}
    p_hold = p_hit_upper(x, lo, tp, mu, sg)
    ev_hold = p_hold * tp + (1 - p_hold) * lo
    ev_cut = x - st["exit_cost"]
    out = {"p_hold": p_hold, "ev_hold": ev_hold, "ev_cut": ev_cut}
    be = st.get("be_level")
    if be is not None and x > be:
        p_be = p_hit_upper(x, be, tp, mu, sg)
        ev_be = p_be * tp + (1 - p_be) * be - st.get("modify_cost", 0.0)
        out["ev_be"] = ev_be
        if ev_be > ev_hold + 0.02 and ev_be >= ev_cut:
            return "MOVE_BE", out
    if ev_cut > ev_hold + 0.05:
        return "CUT", out
    return "HOLD", out


def mu_from_evidence(flags: Dict[str, bool], sig: float) -> float:
    """Map deterministic evidence to a drift prior (per bar, R units).
    Priors to be replaced by journal-estimated conditional drifts."""
    w = {"close_beyond_shelf": -0.15, "cvd_against_3bars": -0.05,
         "wall_pulled": -0.05, "htf_regime_flip": -0.10,
         "absorption_confirmed": +0.05}
    return sig * sum(w[k] for k, on in flags.items() if on and k in w)


def net_breakeven_stop(mt5, symbol: str, is_buy: bool, volume: float, entry: float,
                       commission_usd: float, swap_usd: float, credit_usd: float = 0.50):
    """Invert broker-valued PnL: smallest SL (long) such that
    order_calc_profit - commission + swap >= credit. Bisection on price."""
    order_type = mt5.ORDER_TYPE_BUY if is_buy else mt5.ORDER_TYPE_SELL
    need = credit_usd + commission_usd - swap_usd
    lo, hi = (entry, entry * 1.05) if is_buy else (entry * 0.95, entry)
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        pnl = mt5.order_calc_profit(order_type, symbol, volume, entry, mid)
        if pnl is None:
            return None
        ok = pnl >= need
        if is_buy:
            hi, lo = (mid, lo) if ok else (hi, mid)
        else:
            lo, hi = (mid, hi) if ok else (lo, mid)
    return hi if is_buy else lo


# ==================================================== 7. pre-send MT5 gate
@dataclass
class SendLimits:
    max_tick_age_ms: int = 2_000
    max_spread_bps: float = 20.0
    spread_vs_median: float = 1.5
    max_spread_frac_r: float = 0.10
    max_drift_atr: float = 0.25
    max_decision_age_s: float = 90.0


def pre_send_gate(mt5, req: dict, plan: dict, lim: SendLimits = SendLimits(), now_ms=None, *, tick_age_seconds=None):
    """Run immediately before mt5.order_send(req). Returns (ok, reasons, check)."""
    r: List[str] = []
    sym = req["symbol"]
    info, tick, acct = mt5.symbol_info(sym), mt5.symbol_info_tick(sym), mt5.account_info()
    term = mt5.terminal_info()
    if not (info and tick and acct and term):
        return False, ["mt5_state_unavailable"], None
    if not term.trade_allowed or not acct.trade_allowed:
        r.append("autotrading_disabled")
    if info.trade_mode != mt5.SYMBOL_TRADE_MODE_FULL:
        r.append("symbol_trade_mode_not_full")
    now_ms = now_ms if now_ms is not None else plan["server_now_ms"]
    if tick_age_seconds is not None:
        age = tick_age_seconds(tick, sym)
        age_ms = None if age is None else age * 1000
    else:
        age_ms = now_ms - tick.time_msc
    if age_ms is None or not math.isfinite(age_ms) or age_ms < 0:
        r.append("tick_clock_unverified")
    elif age_ms > lim.max_tick_age_ms:
        r.append(f"tick_stale_{age_ms:.0f}ms")
    mid = 0.5 * (tick.bid + tick.ask)
    if not 0 < tick.bid < tick.ask or not math.isfinite(mid):
        return False, r + ["broker_quote_invalid"], None
    spr_bps = (tick.ask - tick.bid) / mid * 10_000
    allowed_spread = min(lim.max_spread_bps, max(1.0, lim.spread_vs_median * plan.get("spread_median_bps_this_hour", 1.0)))
    if spr_bps > allowed_spread:
        r.append(f"spread_{spr_bps:.1f}bps")
    r_price = abs(req["price"] - req["sl"])
    if (tick.ask - tick.bid) > lim.max_spread_frac_r * r_price:
        r.append("spread_gt_10pct_of_R")
    if abs(mid - plan["mid_at_decision"]) > lim.max_drift_atr * plan["atr"]:
        r.append("drift_since_decision")
    if plan["decision_age_s"] > lim.max_decision_age_s:
        r.append("decision_stale")
    pt = info.point
    min_dist = info.trade_stops_level * pt
    is_buy_limit = req["type"] == mt5.ORDER_TYPE_BUY_LIMIT
    ref = tick.ask if is_buy_limit else tick.bid
    if (ref - req["price"] if is_buy_limit else req["price"] - ref) < max(min_dist, pt):
        r.append("limit_violates_stops_level_or_marketable")
    if abs(req["price"] - req["sl"]) < min_dist or abs(req["tp"] - req["price"]) < min_dist:
        r.append("sltp_inside_stops_level")
    vol = req["volume"]
    steps = round((vol - info.volume_min) / info.volume_step)
    if vol < info.volume_min or abs(info.volume_min + steps * info.volume_step - vol) > 1e-9:
        r.append("volume_not_on_step")
    orders = mt5.orders_get(symbol=sym)
    positions = mt5.positions_get()
    if orders is None or positions is None:
        r.append("broker_inventory_unavailable")
    dup = [o for o in (orders if orders is not None else []) if o.comment == req.get("comment")]
    if dup:
        r.append("duplicate_intent_resting")
    if plan.get("joint_fill_ok") is not True:
        r.append("joint_fill_floor_not_reverified")
    if plan.get("blackout_active"):
        r.append("macro_blackout")
    chk = mt5.order_check(req)
    if chk is None or chk.retcode != 0:
        r.append(f"order_check_{getattr(chk, 'retcode', None)}")
    return (not r), r, chk


# ================================================= 8. adverse-selection proof
def markout_report(fills: Sequence[dict], horizons=("5s", "60s", "300s", "900s"),
                   friction_bps: float = 0.0):
    """fills: {side:+1/-1, price, mid:{h: mid at t+h}, ref_mid_at_fill (opt)}.
    Markout_h = side*(mid_{t+h}-price)/price in bps. Edge is proven only if
    mean(markout_900s) - friction > 0 with t >= 2 AND short-horizon
    markouts are not significantly negative (toxic fills)."""
    out = {}
    for h in horizons:
        m = np.array([f["side"] * (f["mid"][h] - f["price"]) / f["price"] * 1e4
                      for f in fills if h in f["mid"]])
        if len(m) < 2:
            continue
        se = m.std(ddof=1) / math.sqrt(len(m))
        out[h] = {"n": int(len(m)), "mean_bps": float(m.mean()),
                  "t": float(m.mean() / se) if se > 0 else 0.0,
                  "p_adverse": float((m < 0).mean())}
    lag = [f["side"] * (f["ref_mid_at_fill"] - f["price"]) / f["price"] * 1e4
           for f in fills if f.get("ref_mid_at_fill")]
    if lag:
        lag = np.array(lag)
        out["stale_quote_pickoff_frac"] = float((lag < -5).mean())
    last = out.get(horizons[-1])
    out["edge_proven"] = bool(last and last["mean_bps"] - friction_bps > 0 and last["t"] >= 2)
    first = out.get(horizons[0])
    out["toxic"] = bool(first and first["t"] <= -2)
    return out
