"""Terminal/gate_diagnostics.py -- observability for gates G-4, G-5/G-6 and G-7.

Pure, deterministic, dependency-light (stdlib only). No MT5, no I/O, no network.
Every function FAILS CLOSED: an unknown operand yields the least permissive
answer, never a fabricated measurement.

WHY THIS MODULE EXISTS
----------------------
A council cycle on 2026-10-11 proposed loosening three gates to unblock crypto
entries. Measured against live telemetry, all three proposals turned out to be
answered by constraints that already ship -- but the desk could not SEE that,
because the gates emit an opaque token (`UNDEFINED`, `venue_basis_unverified`)
with no magnitude attached. A veto you cannot measure looks arbitrary, and an
arbitrary-looking veto invites a loosening patch.

So this module adds *magnitude*, not tolerance. Nothing here changes a verdict.
Each function reports how far a candidate sits from a boundary so the desk can
distinguish "knife-edge, watch it" from "nowhere close, stop looking".

The three findings it encodes, all measured on generation ab5f242f (12:10 UTC):

1. G-6 ALREADY is the ATR-scaled relative friction gate the council proposed,
   at 0.15 R base / 0.20 R relaxed (decision_gates_v3.py:235-236). SOL, the
   proposal's flagship, measures 1.6002 R -- it fails 0.15, 0.20 and the
   proposed 0.25 alike. No threshold short of 1.6 R admits it.

2. No epsilon flips any regime. All 14 crypto miss the binding
   `vr_z_15m < -1.5` leg by >= 0.5642 (BTC, the closest). ETH's much-cited
   -1.4998 was transient: 52 minutes later it read -1.3161.

3. The G-7 clock-skew fix in commit a6b5b74d is correct in source but INERT,
   because the resident telemetry daemon still executes the pre-fix module.
   Its signature is detectable: one `wall_sample_ts_epoch` shared across all
   24 assets, and no `binance_mid_ts` / `hyperdash_mid_ts` field at all.
   ``audit_wall_timestamps`` reports exactly that, so a stale daemon can never
   again be mistaken for a fixed one.
"""
from __future__ import annotations

import math
from numbers import Real
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

# ----------------------------------------------------------------- constants

#: Stop distance the desk uses, in ATRs. Friction is normalised against this so
#: that "cost in R" and "1.5 ATR stop" are the same ruler.
STOP_ATR_MULTIPLE = 1.5

#: A spread is crossed twice (entry and exit) for a round trip.
ROUND_TRIP_CROSSES = 2

#: Gate G-6 as shipped. Mirrored here for reporting only -- the authoritative
#: values live in decision_gates_v3.py and the gate itself is NOT duplicated.
G6_FRICTION_BASE_MAX_R = 0.15
G6_FRICTION_RELAXED_MAX_R = 0.20

#: Gate G-5 as shipped.
G5_MAX_SPREAD_BPS_HARD = 20.0


def _fin(x: Any) -> bool:
    if isinstance(x, bool) or not isinstance(x, Real):
        return False
    try:
        return math.isfinite(float(x))
    except (OverflowError, ValueError, TypeError):
        return False


# ===================================================== 1. G-5 / G-6 friction

def spread_friction_r(
    spread_bps: Any, mid: Any, atr: Any, *,
    stop_atr_multiple: float = STOP_ATR_MULTIPLE,
    round_trip_crosses: int = ROUND_TRIP_CROSSES,
) -> Optional[float]:
    """Cost of a round trip expressed in units of R, where R = the stop distance.

        gamma = (crosses * spread_price) / (stop_atr_multiple * ATR)

    This is the quantity Gate G-6 already caps. Exposing it lets a candidate be
    ranked by *real* friction instead of by nominal bps, which is what makes the
    static/relative comparison legible.

    Returns None (not 0.0) when any operand is unusable: an unknown cost must
    never read as a free trade.
    """
    if not (_fin(spread_bps) and _fin(mid) and _fin(atr)):
        return None
    bps, m, a = float(spread_bps), float(mid), float(atr)
    if m <= 0 or a <= 0 or bps < 0:
        return None
    if not _fin(stop_atr_multiple) or float(stop_atr_multiple) <= 0:
        return None
    if not isinstance(round_trip_crosses, int) or round_trip_crosses < 1:
        return None
    spread_price = m * bps / 1e4
    return (float(round_trip_crosses) * spread_price) / (float(stop_atr_multiple) * a)


def atr_in_bps(mid: Any, atr: Any) -> Optional[float]:
    """ATR as a percentage of price, in basis points.

    The diagnostic that exposes the intuition error behind "SOL's ATR is
    proportionally huge". SOL measures 20.54 bps of ATR against a 24.65 bps
    spread -- the spread EXCEEDS the whole 15m ATR. Comparing spread_bps with
    atr_bps directly is the honest way to see that.
    """
    if not (_fin(mid) and _fin(atr)) or float(mid) <= 0 or float(atr) < 0:
        return None
    return float(atr) / float(mid) * 1e4


def friction_verdict(
    spread_bps: Any, mid: Any, atr: Any, *,
    base_max_r: float = G6_FRICTION_BASE_MAX_R,
    relaxed_max_r: float = G6_FRICTION_RELAXED_MAX_R,
) -> Dict[str, Any]:
    """Report a candidate against BOTH the static bps cap and the relative cap.

    Purely descriptive. The two gates already run in decision_gates_v3; this
    only makes their margins visible side by side.
    """
    gamma = spread_friction_r(spread_bps, mid, atr)
    ab = atr_in_bps(mid, atr)
    out: Dict[str, Any] = {
        "gamma_r": gamma,
        "atr_bps": ab,
        "spread_bps": float(spread_bps) if _fin(spread_bps) else None,
        "g5_static_bps_ok": (_fin(spread_bps) and float(spread_bps) <= G5_MAX_SPREAD_BPS_HARD),
        "g6_base_ok": (gamma is not None and gamma <= base_max_r),
        "g6_relaxed_ok": (gamma is not None and gamma <= relaxed_max_r),
    }
    # Margin to the binding cap. None means "not measurable", never "infinite room".
    out["margin_to_base_r"] = (base_max_r - gamma) if gamma is not None else None
    out["margin_to_relaxed_r"] = (relaxed_max_r - gamma) if gamma is not None else None
    if gamma is not None:
        # What gamma_max WOULD be needed to admit this candidate. Makes "raise
        # the cap to unlock X" a number the desk can reject on sight.
        out["gamma_max_required_r"] = gamma
    return out


# ===================================================== 2. G-4 regime proximity

#: Mean-reversion legs, in the order decision_gates_v3 evaluates them.
def regime_proximity(
    stats: Mapping[str, Any],
    *,
    er_mr: float = 0.20,
    er_4h_mr_cap: float = 0.30,
    vr_z_mr: float = -1.5,
    er_trend: float = 0.35,
    t_trend: float = 2.5,
    vr_z_trend: float = 1.0,
) -> Dict[str, Any]:
    """How far a candidate sits from each regime boundary, and what it would take.

    Consumes the ``stats`` dict returned by ``classify_regime`` (keys "15m",
    "1h", "4h", each holding er / vr / vr_z / t).

    Reports a DEFICIT per leg: positive means the leg passes and by how much,
    negative means it fails and by how much. ``epsilon_needed`` is the smallest
    uniform tolerance that would flip the verdict -- so a proposal to add a
    tolerance band can be checked against reality instead of argued about.

    This function NEVER returns a regime. It is a measuring stick, not a router.
    """
    out: Dict[str, Any] = {"usable": False}
    if not isinstance(stats, Mapping):
        out["reason"] = "stats_not_a_mapping"
        return out
    s15, s1h, s4h = stats.get("15m"), stats.get("1h"), stats.get("4h")
    if not all(isinstance(s, Mapping) for s in (s15, s1h, s4h)):
        out["reason"] = "stats_missing_timeframe"
        return out

    def num(s: Mapping, k: str) -> Optional[float]:
        v = s.get(k)
        return float(v) if _fin(v) else None

    er_1h, er_4h = num(s1h, "er"), num(s4h, "er")
    vr_15, vr_1h = num(s15, "vr_z"), num(s1h, "vr_z")
    t_1h, t_4h = num(s1h, "t"), num(s4h, "t")
    if None in (er_1h, er_4h, vr_15):
        out["reason"] = "regime_statistics_unavailable"
        return out

    mr_legs = {
        "er_1h_lt_er_mr": er_mr - er_1h,
        "er_4h_lt_cap": er_4h_mr_cap - er_4h,
        # Passes iff vr_z < cut, so a positive margin means it is past the cut.
        "vr_z_15m_lt_cut": vr_z_mr - vr_15,
    }
    # A leg passes when its margin is > 0.
    mr_pass = {k: (v > 0) for k, v in mr_legs.items()}
    mr_ok = all(mr_pass.values())
    # Smallest uniform epsilon that would flip every failing leg to passing.
    failing = [abs(v) for v in mr_legs.values() if v <= 0]
    eps_needed = max(failing) if failing else 0.0

    # TREND legs, for completeness: >=2 of 3 votes on 1H plus an HTF agreement.
    trend_votes = {}
    if t_1h is not None:
        trend_votes["t_1h_gt_t_trend"] = t_1h - t_trend
    if er_1h is not None:
        trend_votes["er_1h_gt_er_trend"] = er_1h - er_trend
    if vr_1h is not None:
        trend_votes["vr_z_1h_gt_cut"] = vr_1h - vr_z_trend
    htf_ok = None
    if t_4h is not None:
        htf_ok = {"t_4h_margin": t_4h - 1.5, "er_4h_margin": er_4h - 0.25}

    out.update({
        "usable": True,
        "mean_revert_ok": mr_ok,
        "mean_revert_leg_margins": mr_legs,
        "mean_revert_leg_pass": mr_pass,
        "binding_leg": (min(mr_legs, key=lambda k: mr_legs[k]) if not mr_ok else None),
        "epsilon_needed_to_flip_mr": eps_needed,
        "trend_vote_margins": trend_votes,
        "trend_votes_passing": sum(1 for v in trend_votes.values() if v > 0),
        "htf_margins": htf_ok,
    })
    return out


# ===================================================== 3. G-7 pipeline audit

def audit_wall_timestamps(
    assets: Mapping[str, Any],
    *,
    broker_ts_by_symbol: Optional[Mapping[str, float]] = None,
    max_skew_s: float = 5.0,
    ob_key: str = "orderbook_live_depth",
) -> Dict[str, Any]:
    """Detect a telemetry pipeline whose wall timestamps are not contemporaneous.

    Two independent failure signatures, both observed in production:

    * ``shared_across_assets`` -- one `wall_sample_ts_epoch` value reused for
      every asset. A per-asset venue sample cannot be identical to the
      nanosecond across 24 books, so this identifies a cycle-level `now_ts`
      captured once, i.e. the pre-fix generator.
    * ``missing_ts_fields`` -- neither `binance_mid_ts` nor `hyperdash_mid_ts`
      present. Commit a6b5b74d adds at least one of them on every branch that
      publishes walls, so their total absence identifies pre-fix code.

    Together these distinguish "the fix is deployed and the book is genuinely
    late" from "the resident daemon never reloaded the fix". The second is not
    visible from any single snapshot's numbers alone.
    """
    out: Dict[str, Any] = {
        "assets_examined": 0, "assets_with_walls": 0, "distinct_wall_ts": 0,
        "shared_across_assets": None, "missing_ts_fields": None,
        "skew_s": {}, "skew_ok": {}, "max_abs_skew_s": None,
        "verdict": "insufficient_data",
    }
    if not isinstance(assets, Mapping) or not assets:
        return out

    wall_ts: List[float] = []
    have_field = 0
    with_walls = 0
    for sym, payload in assets.items():
        if not isinstance(payload, Mapping):
            continue
        ob = payload.get(ob_key)
        if not isinstance(ob, Mapping):
            continue
        out["assets_examined"] += 1
        if ob.get("whale_walls_l3") or ob.get("l2_wall_levels"):
            with_walls += 1
        if ob.get("binance_mid_ts") is not None or ob.get("hyperdash_mid_ts") is not None:
            have_field += 1
        ts = ob.get("wall_sample_ts_epoch")
        if _fin(ts):
            wall_ts.append(float(ts))
            if broker_ts_by_symbol:
                bts = broker_ts_by_symbol.get(sym)
                if _fin(bts):
                    sk = float(ts) - float(bts)
                    out["skew_s"][sym] = sk
                    out["skew_ok"][sym] = abs(sk) <= float(max_skew_s)
    out["assets_with_walls"] = with_walls
    out["distinct_wall_ts"] = len(set(wall_ts))
    out["missing_ts_fields"] = (with_walls > 0 and have_field == 0)
    out["shared_across_assets"] = (
        with_walls > 1 and out["distinct_wall_ts"] == 1
    )
    if out["skew_s"]:
        out["max_abs_skew_s"] = max(abs(v) for v in out["skew_s"].values())

    # Least permissive verdict first.
    if out["assets_examined"] == 0:
        return out
    if out["missing_ts_fields"] and out["shared_across_assets"]:
        out["verdict"] = "pre_fix_pipeline_signature"
    elif out["shared_across_assets"]:
        out["verdict"] = "shared_wall_timestamp_suspect"
    elif out["missing_ts_fields"]:
        out["verdict"] = "missing_venue_ts_fields"
    elif out["max_abs_skew_s"] is not None and out["max_abs_skew_s"] > float(max_skew_s):
        out["verdict"] = "clock_skew_exceeds_allowance"
    elif out["assets_with_walls"] == 0:
        out["verdict"] = "no_walls_published"
    else:
        out["verdict"] = "contemporaneous"
    return out


__all__ = [
    "G5_MAX_SPREAD_BPS_HARD",
    "G6_FRICTION_BASE_MAX_R",
    "G6_FRICTION_RELAXED_MAX_R",
    "ROUND_TRIP_CROSSES",
    "STOP_ATR_MULTIPLE",
    "atr_in_bps",
    "audit_wall_timestamps",
    "friction_verdict",
    "regime_proximity",
    "spread_friction_r",
]


# ==================================== 4. G-7 venue-mid independence

#: Above this share of observations landing inside the broker's own bid/ask, a
#: "venue" mid is more consistent with being derived from the broker quote than
#: observed on another venue. Measured on 2026-10-11: 29% inside across 135
#: pre-restart observations (96 of 135 outside) versus 92% inside across 65
#: post-restart observations (5 of 65 outside).
VENUE_MID_INSIDE_SHARE_SUSPECT = 0.80


def audit_venue_mid_independence(
    assets: Mapping[str, Any], *,
    venue_mid_key: str = "binance_mid",
    ob_key: str = "orderbook_live_depth",
    exact_zero_tol: float = 1e-12,
    suspect_inside_share: float = VENUE_MID_INSIDE_SHARE_SUSPECT,
) -> Dict[str, Any]:
    """Test whether a published venue mid is an independent observation.

    A cross-venue basis gate is only as good as the two mids it differences.
    If the "venue" mid is in fact derived from the broker quote, the basis is
    zero by construction, its drift is zero by construction, and the gate passes
    without ever having compared two venues. That is a silent un-gating: every
    wall in the book becomes admissible on a number that carries no
    cross-venue information.

    Two independent signals, both distributional:

    * ``inside_spread_share`` -- how often the venue mid lands within the
      broker's own bid/ask. A real second venue, priced off its own order book,
      crosses a 1-2 bps broker spread constantly. A derived value almost never
      leaves it.
    * ``exact_zero_share`` -- how often mid and venue mid are bit-identical.
      Two venues agreeing exactly, repeatedly, is arithmetic identity rather
      than coincidence.

    Fails closed: with too few observations it reports ``insufficient_data``
    rather than certifying independence.
    """
    out: Dict[str, Any] = {
        "observations": 0, "inside_spread": 0, "exact_zero": 0,
        "inside_spread_share": None, "exact_zero_share": None,
        "suspect": None, "verdict": "insufficient_data",
    }
    if not isinstance(assets, Mapping) or not assets:
        return out
    inside = 0
    exact = 0
    n = 0
    for _sym, payload in assets.items():
        if not isinstance(payload, Mapping):
            continue
        q = payload.get("quotes")
        ob = payload.get(ob_key)
        if not (isinstance(q, Mapping) and isinstance(ob, Mapping)):
            continue
        bid, ask, vm = q.get("bid"), q.get("ask"), ob.get(venue_mid_key)
        mid = q.get("mid")
        if not (_fin(bid) and _fin(ask) and _fin(vm)):
            continue
        n += 1
        if float(bid) <= float(vm) <= float(ask):
            inside += 1
        if _fin(mid) and abs(float(vm) - float(mid)) <= float(exact_zero_tol):
            exact += 1
    out["observations"] = n
    out["inside_spread"] = inside
    out["exact_zero"] = exact
    if n == 0:
        return out
    out["inside_spread_share"] = inside / n
    out["exact_zero_share"] = exact / n
    suspect = out["inside_spread_share"] >= float(suspect_inside_share)
    out["suspect"] = suspect
    out["verdict"] = "broker_derived_suspect" if suspect else "consistent_with_independent_venue"
    return out


__all__.append("audit_venue_mid_independence")
__all__.append("VENUE_MID_INSIDE_SHARE_SUSPECT")
