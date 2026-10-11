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

import json
import math
import pathlib
import time
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
        "lagging_quote_assets": {}, "closed_market_assets": {},
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
        if ob.get("binance_mid_ts") is not None or ob.get("hyperdash_mid_ts") is not None or ob.get("hyperliquid_mid_ts") is not None:
            have_field += 1
        ts = ob.get("wall_sample_ts_epoch")
        if _fin(ts):
            wall_ts.append(float(ts))
            if broker_ts_by_symbol:
                bts = broker_ts_by_symbol.get(sym)
                if _fin(bts):
                    quotes = payload.get("quotes") if isinstance(payload, Mapping) else None
                    is_stale_quote = (
                        isinstance(quotes, Mapping)
                        and (quotes.get("quote_freshness") == "STALE"
                             or (quotes.get("broker_tick_age_s") is not None and float(quotes["broker_tick_age_s"]) > 300.0))
                    )
                    if is_stale_quote:
                        out.setdefault("closed_market_assets", {})[sym] = {
                            "broker_tick_age_s": quotes.get("broker_tick_age_s") if isinstance(quotes, Mapping) else None,
                            "quote_freshness": quotes.get("quote_freshness") if isinstance(quotes, Mapping) else None,
                        }
                    elif (
                        isinstance(quotes, Mapping)
                        and quotes.get("broker_tick_age_s") is not None
                        and float(quotes["broker_tick_age_s"]) > float(max_skew_s)
                    ):
                        out.setdefault("lagging_quote_assets", {})[sym] = {
                            "broker_tick_age_s": float(quotes["broker_tick_age_s"]),
                            "skew_s": float(ts) - float(bts),
                        }
                        out["skew_ok"][sym] = False
                    else:
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
    elif not out["skew_s"] and out.get("lagging_quote_assets"):
        out["verdict"] = "all_quotes_lagging"
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
    liquid_spread_bps_cap: float = 20.0,
    history_path: Optional[Any] = None,
    min_rolling_sample: int = 30,
    max_rolling_sample: int = 200,
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
        "liquid_observations": 0, "liquid_inside_spread": 0, "liquid_inside_spread_share": None,
        "suspect": None, "near_threshold": None, "threshold_margin_assets": None,
        "verdict": "insufficient_data",
    }
    if not isinstance(assets, Mapping) or not assets:
        return out
    inside = 0
    exact = 0
    n = 0
    liq_inside = 0
    liq_n = 0
    fresh_samples: List[Dict[str, Any]] = []
    for sym, payload in assets.items():
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
        is_inside = (float(bid) <= float(vm) <= float(ask))
        is_exact = (_fin(mid) and abs(float(vm) - float(mid)) <= float(exact_zero_tol))
        if is_inside:
            inside += 1
        if is_exact:
            exact += 1
        spr_bps = q.get("spread_bps")
        if _fin(spr_bps) and float(spr_bps) <= float(liquid_spread_bps_cap):
            liq_n += 1
            if is_inside:
                liq_inside += 1
        fresh_samples.append({
            "sym": str(sym),
            "inside": bool(is_inside),
            "exact": bool(is_exact),
            "ts": time.time(),
        })

    out["observations"] = n
    out["inside_spread"] = inside
    out["exact_zero"] = exact
    out["liquid_observations"] = liq_n
    out["liquid_inside_spread"] = liq_inside
    if liq_n > 0:
        out["liquid_inside_spread_share"] = liq_inside / liq_n

    if n == 0:
        return out

    instant_inside_share = inside / n
    instant_exact_share = exact / n
    out["instantaneous_inside_spread_share"] = instant_inside_share
    out["instantaneous_exact_zero_share"] = instant_exact_share
    out["inside_spread_share"] = instant_inside_share
    out["exact_zero_share"] = instant_exact_share

    # Optional multi-cycle rolling buffer to resolve small-n discrete knife-edge
    if history_path is not None:
        try:
            hp = pathlib.Path(history_path)
            hist: List[Dict[str, Any]] = []
            if hp.exists():
                hist = json.loads(hp.read_text(encoding="utf-8"))
            hist.extend(fresh_samples)
            hist = hist[-int(max_rolling_sample):]
            hp.parent.mkdir(parents=True, exist_ok=True)
            hp.write_text(json.dumps(hist), encoding="utf-8")
            if len(hist) >= int(min_rolling_sample):
                r_inside = sum(1 for s in hist if s.get("inside"))
                r_exact = sum(1 for s in hist if s.get("exact"))
                r_n = len(hist)
                out["rolling_observations"] = r_n
                out["rolling_inside_spread"] = r_inside
                out["rolling_inside_spread_share"] = r_inside / r_n
                out["rolling_exact_zero_share"] = r_exact / r_n
                # Use robust pooled statistics when minimum sample is met
                out["inside_spread_share"] = r_inside / r_n
                out["exact_zero_share"] = r_exact / r_n
        except Exception:
            pass

    suspect = out["inside_spread_share"] >= float(suspect_inside_share)
    out["suspect"] = suspect
    # The measured share sits at 10-12 of 14 (0.714-0.857) across every cycle
    # observed 2026-10-11 15:34-15:53, i.e. it straddles the 0.80 threshold. A
    # binary verdict there flips cycle to cycle on one asset crossing the spread
    # edge, which is not evidence of a state change. Say so explicitly.
    out["near_threshold"] = abs(out["inside_spread_share"] - float(suspect_inside_share)) <= 0.10
    out["threshold_margin_assets"] = (
        (out["inside_spread_share"] - float(suspect_inside_share)) * out["observations"])
    out["verdict"] = "broker_derived_suspect" if suspect else "consistent_with_independent_venue"
    return out


__all__.append("audit_venue_mid_independence")
__all__.append("VENUE_MID_INSIDE_SHARE_SUSPECT")

# ==================================== 5. composite G-7 readiness

def g7_readiness(
    assets: Mapping[str, Any],
    *,
    broker_ts_by_symbol: Optional[Mapping[str, float]] = None,
    max_skew_s: float = 5.0,
    venue_mid_key: Optional[str] = None,
    history_path: Optional[Any] = None,
) -> Dict[str, Any]:
    """One call answering: can Gate G-7 admit a wall right now, and if not, why?

    G-7 has three preconditions and they bind in a specific order:

    0. the published basis_median must be an independent anchor rather than the
       same cycle's own b_now, or the drift breaker is inert
       (``audit_basis_median_independence``);
    1. the venue a wall sits on must have a published mid
       (``audit_wall_venue_coverage``) -- this one binds first, and when it fails
       nothing downstream is ever reached;
    2. the wall stamp must be contemporaneous with the broker quote
       (``audit_wall_timestamps``);
    3. the venue mid it is differenced against must be an independent
       observation (``audit_venue_mid_independence``).

    Measured 2026-10-11 gen 46055c42: all 734 G-7-eligible GENUINE walls resolve
    to HYPERLIQUID while only BINANCE mids are published, so (1) fails for 24 of
    24 assets and ``select_backing_wall`` returns ``venue_basis_mid_unavailable``
    (92 rejections on BTC alone). (2) and (3) also fail, but they are downstream
    of a refusal that happens first.

    * the wall stamp must be contemporaneous with the broker quote
      (``audit_wall_timestamps``), and
    * the venue mid it is differenced against must be an independent
      observation (``audit_venue_mid_independence``).

    """
    if broker_ts_by_symbol is None and isinstance(assets, Mapping):
        extracted_bts: Dict[str, float] = {}
        for sym, a in assets.items():
            if isinstance(a, Mapping):
                q = a.get("quotes")
                if isinstance(q, Mapping):
                    msc = q.get("broker_tick_time_utc_msc")
                    if isinstance(msc, (int, float)) and msc > 0:
                        extracted_bts[sym] = float(msc) / 1000.0
        if extracted_bts:
            broker_ts_by_symbol = extracted_bts

    walls = audit_wall_timestamps(
        assets, broker_ts_by_symbol=broker_ts_by_symbol, max_skew_s=max_skew_s
    )
    cover = audit_wall_venue_coverage(assets)
    anchor = audit_basis_median_independence(assets)

    # Determine which venue(s) to audit for mid independence.
    # If caller specified venue_mid_key explicitly, respect that.
    # Otherwise audit the host venue(s) where the G-7 walls actually sit.
    wall_venues_total = cover.get("wall_venues_total") or {}
    if venue_mid_key is not None:
        venues_to_check = [("SPECIFIED", venue_mid_key)]
    else:
        active = [v for v in wall_venues_total.keys() if v in ("BINANCE", "HYPERLIQUID")]
        if not active:
            active = ["BINANCE"]
        venues_to_check = [
            (v, "hyperliquid_mid" if v == "HYPERLIQUID" else "binance_mid")
            for v in active
        ]

    venue_reports: Dict[str, Any] = {}
    venue_blockers: List[str] = []
    for v_name, v_key in venues_to_check:
        rep = audit_venue_mid_independence(
            assets, venue_mid_key=v_key, history_path=history_path
        )
        venue_reports[v_name] = rep
        if rep.get("suspect") is True:
            venue_blockers.append("venue_mid:broker_derived_suspect")

    primary_venue_name = venues_to_check[0][0]
    venue = venue_reports[primary_venue_name]

    # Venue coverage is checked FIRST because it binds before the others. When a
    # wall's venue has no published mid, select_backing_wall refuses with
    # venue_basis_mid_unavailable and never reaches a clock or drift check, so
    # repairing the clock admits nothing.
    blockers: List[str] = []
    if cover.get("verdict") == "wall_venue_mid_missing":
        blockers.append("venue_coverage:wall_venue_mid_missing")
    if anchor.get("breaker_inert") is True:
        blockers.append("drift_breaker:b_hat_pinned_to_b_now")
    if walls.get("verdict") not in ("contemporaneous", "no_walls_published"):
        blockers.append(f"wall_timestamps:{walls.get('verdict')}")
    # audit_wall_timestamps computes max_abs_skew_s only over assets whose broker
    # quote is itself fresh; assets whose quote lags are recorded with
    # skew_ok[sym] = False and excluded, because a stale quote age is not a clock
    # disagreement. That exclusion is sound for the aggregate, but the aggregate
    # verdict then reads "contemporaneous" even when individual assets still fail
    # their own skew test -- and "ready" must not imply desk-wide.
    skew_failed = sorted(
        k for k, ok in (walls.get("skew_ok") or {}).items() if ok is False
    )
    # Only supplement a PASSING aggregate. When the aggregate already fails, that
    # blocker is reported and adding this one would double-count the same defect.
    if skew_failed and walls.get("verdict") == "contemporaneous":
        blockers.append(f"wall_timestamps:per_asset_skew_failed:{','.join(skew_failed)}")
    if venue_blockers:
        blockers.extend(venue_blockers)
    elif venue.get("suspect") is True:
        blockers.append("venue_mid:broker_derived_suspect")
    ready = not blockers

    # A clock repair opens the gate only if it is the sole remaining blocker and
    # the venue mid it would differ against is both present and independent.
    clock_only = (
        blockers == ["wall_timestamps:clock_skew_exceeds_allowance"]
        and cover.get("coverage_complete") is True
        and venue.get("suspect") is not True
        and anchor.get("breaker_inert") is not True
    )
    out: Dict[str, Any] = {
        "ready": ready,
        "blockers": blockers,
        # The blocker that actually refuses the wall in production, in bind order.
        "binding_blocker": blockers[0] if blockers else None,
        "venue_coverage_verdict": cover.get("verdict"),
        "g7_walls_total": cover.get("g7_walls_total"),
        "wall_venues_total": cover.get("wall_venues_total"),
        "covered_assets": cover.get("covered_assets"),
        "drift_breaker_verdict": anchor.get("verdict"),
        "inert_venues": anchor.get("inert_venues"),
        "per_venue_pinned_share": {
            k: v.get("pinned_share") for k, v in (anchor.get("per_venue") or {}).items()
        },
        "wall_verdict": walls.get("verdict"),
        "venue_verdict": venue.get("verdict"),
        "max_abs_skew_s": walls.get("max_abs_skew_s"),
        # Assets excluded from max_abs_skew_s because their own broker quote lags.
        "per_asset_skew_failed": skew_failed,
        "lagging_quote_assets": sorted(walls.get("lagging_quote_assets") or {}),
        "closed_market_assets": sorted(walls.get("closed_market_assets") or {}),
        "inside_spread_share": venue.get("inside_spread_share"),
        "venue_mid_near_threshold": venue.get("near_threshold"),
        "exact_zero_share": venue.get("exact_zero_share"),
        "clock_fix_alone_would_open_gate": clock_only,
        "venue_reports": venue_reports,
        "wall_venues_audited": [v[0] for v in venues_to_check],
    }
    return out


__all__.append("g7_readiness")

# ==================================== 6. wall venue coverage (the true G-7 blocker)

def audit_wall_venue_coverage(
    assets: Mapping[str, Any],
    *,
    ob_key: str = "orderbook_live_depth",
    default_venue: str = "BINANCE",
) -> Dict[str, Any]:
    """Do the assets publish a mid for the venue their walls actually sit on?

    ``select_backing_wall`` resolves each wall's venue, then looks that venue up
    in ``venue_quotes``. When the lookup misses it calls ``basis_drift_decision``
    with ``venue_mid=None``, which returns ``venue_basis_mid_unavailable`` --
    and because some *other* venue has a mid, ``any_venue_mids`` is True, so the
    ``native_basis`` escape hatch is not taken either. The wall is refused before
    any clock or drift check runs.

    Measured 2026-10-11 gen 46055c42: all 734 G-7-eligible GENUINE walls in the
    universe resolve to HYPERLIQUID, while only BINANCE mids are published, and
    ``venue_basis`` is absent everywhere. Coverage is 0 of 24.
    """
    per_asset: Dict[str, Any] = {}
    total_walls = 0
    covered_assets = 0
    examined = 0
    venue_counter: Dict[str, int] = {}
    for symbol, asset in (assets or {}).items():
        if not isinstance(asset, dict):
            continue
        examined += 1
        ob = asset.get(ob_key)
        ob = ob if isinstance(ob, dict) else {}
        walls = [
            w for w in (ob.get("whale_walls_l3") or [])
            if isinstance(w, dict)
            and w.get("gate_g7_eligible") is True
            and w.get("wall_class") == "GENUINE"
        ]
        venues: Dict[str, int] = {}
        for w in walls:
            raw = str(w.get("venue") or w.get("source") or "").upper()
            if "HYPER" in raw:
                venue = "HYPERLIQUID"
            elif "BINANCE" in raw:
                venue = "BINANCE"
            elif "MT5" in raw or "NATIVE" in raw:
                venue = "NATIVE"
            else:
                venue = str(default_venue).upper()
            venues[venue] = venues.get(venue, 0) + 1
            venue_counter[venue] = venue_counter.get(venue, 0) + 1
        total_walls += len(walls)
        mids = {
            v for v, q in _venue_mids(ob, asset).items()
            if isinstance(q, dict) and isinstance(q.get("mid"), (int, float))
            and not isinstance(q.get("mid"), bool)
        }
        uncovered = sorted(set(venues) - mids)
        # An asset without G7 walls has no uncovered venues; an asset with walls is covered iff not uncovered.
        covered = not bool(uncovered)
        covered_assets += covered
        per_asset[symbol] = {
            "g7_walls": len(walls),
            "wall_venues": venues,
            "venues_with_mid": sorted(mids),
            "uncovered_venues": uncovered,
            "covered": covered,
        }
    return {
        "assets_examined": examined,
        "g7_walls_total": total_walls,
        "wall_venues_total": venue_counter,
        "covered_assets": covered_assets,
        "coverage_complete": bool(covered_assets == examined and examined > 0 and total_walls > 0),
        "verdict": (
            "no_g7_walls_published" if total_walls == 0
            else "venue_mid_covered" if covered_assets == examined
            else "wall_venue_mid_missing"
        ),
        "per_asset": per_asset,
    }


def _venue_mids(ob: Mapping[str, Any], asset: Mapping[str, Any]) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    vb = ob.get("venue_basis")
    if isinstance(vb, dict):
        for venue, q in vb.items():
            if isinstance(q, dict):
                out[str(venue).upper()] = {"mid": q.get("mid")}
    if "BINANCE" not in out and ob.get("binance_mid") is not None:
        out["BINANCE"] = {"mid": ob.get("binance_mid")}
    return out


__all__.append("audit_wall_venue_coverage")

# ==================================== 7. is the drift breaker actually live?

def audit_basis_median_independence(
    assets: Mapping[str, Any],
    *,
    ob_key: str = "orderbook_live_depth",
    exact_tol: float = 1e-9,
) -> Dict[str, Any]:
    """Is ``basis_median`` an independent anchor, or just this cycle's own b_now?

    ``basis_drift_decision`` compares the live basis against a published
    ``basis_median`` and trips when they diverge. If the publisher writes the
    *current* observation into that field, then b_hat == b_now by construction,
    drift is identically zero, and the circuit breaker can never fire. The
    shipped code guards the ``b_hat is None`` cold-start case explicitly --
    "Legacy fallback b_hat = b_now makes drift identically 0: breaker inert" --
    but a publisher that writes b_now straight through is finite, so it passes
    that guard and silently disables the breaker.

    Measured 2026-10-11 across gens 14:34:15 / 14:35:38 / 14:36:32: the
    HYPERLIQUID ``basis_median`` equals that cycle's b_now to the cent in every
    generation (diff +0.0000), while BINANCE's differs by -47.79 / -2.65 /
    -11.45 -- a genuine rolling median. Every G-7 wall resolves to HYPERLIQUID,
    so the breaker is inert for the entire wall population.
    """
    per_asset: Dict[str, Any] = {}
    examined = 0
    total = 0
    pinned = 0
    per_venue: Dict[str, Dict[str, int]] = {}
    cold_start: Dict[str, Dict[str, int]] = {}
    cold_total = 0
    for symbol, asset in (assets or {}).items():
        if not isinstance(asset, dict):
            continue
        examined += 1
        ob = asset.get(ob_key)
        ob = ob if isinstance(ob, dict) else {}
        quote = asset.get("quotes")
        quote = quote if isinstance(quote, dict) else {}
        broker_mid = quote.get("mid")
        if not _is_num(broker_mid):
            continue
        vb = ob.get("venue_basis")
        if not isinstance(vb, dict):
            continue
        venues: Dict[str, Any] = {}
        for venue, block in vb.items():
            if not isinstance(block, dict):
                continue
            v_mid = block.get("mid")
            b_hat = block.get("basis_median")
            if not _is_num(v_mid):
                continue
            # A null anchor is not a defect: rolling_basis_median returns None
            # until BASIS_MIN_SAMPLES prior prints exist, and basis_drift_decision
            # reads that as venue_basis_cold_start. Tracking it separately is how
            # a daemon restart is confirmed -- the expected sequence after a
            # restart is null, null, ... then a median that diverges from b_now.
            if not _is_num(b_hat):
                key = str(venue).upper()
                cold = cold_start.setdefault(key, {"observations": 0})
                cold["observations"] += 1
                cold_total += 1
                continue
            b_now = float(broker_mid) - float(v_mid)
            diff = abs(b_now - float(b_hat))
            same = diff <= exact_tol
            total += 1
            pinned += same
            key = str(venue).upper()
            slot = per_venue.setdefault(key, {"observations": 0, "pinned": 0})
            slot["observations"] += 1
            slot["pinned"] += int(same)
            venues[key] = {
                "b_now": b_now, "b_hat": float(b_hat),
                "abs_diff": diff, "equals_b_now": same,
            }
        if venues:
            per_asset[symbol] = venues

    # Per venue, because an aggregate share across venues hides the case that
    # matters. Measured 2026-10-11 gen 2d60461f: all 14 HYPERLIQUID observations
    # are pinned (|diff| exactly 0) while all BINANCE ones are independent, so
    # the blended share is only 0.389 and reports a healthy breaker -- while the
    # breaker is in fact inert for every single wall, since every G-7 wall
    # resolves to HYPERLIQUID.
    venue_verdicts: Dict[str, Any] = {}
    inert_venues: List[str] = []
    for key, slot in sorted(per_venue.items()):
        share = (slot["pinned"] / slot["observations"]) if slot["observations"] else 0.0
        inert = share >= VENUE_MID_INSIDE_SHARE_SUSPECT
        if inert:
            inert_venues.append(key)
        venue_verdicts[key] = {
            "observations": slot["observations"],
            "pinned": slot["pinned"],
            "pinned_share": share,
            "inert": inert,
        }
    return {
        "assets_examined": examined,
        "observations": total,
        "cold_start_observations": cold_total,
        "cold_start": cold_start,
        "pinned_to_b_now": pinned,
        "pinned_share": (pinned / total) if total else 0.0,
        "per_venue": venue_verdicts,
        "inert_venues": inert_venues,
        "any_venue_inert": bool(inert_venues),
        "breaker_inert": bool(inert_venues),
        "verdict": (
            "insufficient_data" if (total == 0 and cold_total == 0)
            else "cold_start_no_anchor_yet" if total == 0
            else "b_hat_pinned_to_b_now" if inert_venues
            else "b_hat_independent"
        ),
        "per_asset": per_asset,
    }


def _is_num(x: Any) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


__all__.append("audit_basis_median_independence")
