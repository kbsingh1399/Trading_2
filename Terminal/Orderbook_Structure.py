"""Deterministic L3 wall-cluster analytics and structural exit geometry.

All functions are pure: no I/O, no clock reads, no broker calls. Every input
is either a raw feed payload field or an explicit parameter, so the geometry
computed here is reproducible from the journal alone.

This module implements the Incident C remediation:
  * Pullback (S1) and breakout (T1) sleeves are classified deterministically
    from the orderflow feature vector, never by cognitive inference.
  * Take-profits snap to front-run the first major overhead liquidity cluster
    (> 2.0M USD) instead of an arbitrary fixed R-multiple, with the R-hurdle
    depressed dynamically and vetoed when the net-of-friction payoff cannot
    clear the policy floor.
"""
from __future__ import annotations
import math
from Terminal.Risk_Sizing_Engine import number, epoch

DEFAULT_ENTRY_WALL_MIN_USD = 150_000.0
DEFAULT_ENTRY_WALL_MIN_PERSISTENCE_SEC = 180.0
DEFAULT_TPF_WALL_MIN_USD = 2_000_000.0
DEFAULT_MAX_WALL_AGE_SEC = 30.0


def wall_clusters(l3_orders, side, lo, hi, now, *,
                  min_notional_usd=DEFAULT_ENTRY_WALL_MIN_USD,
                  min_persistence_sec=DEFAULT_ENTRY_WALL_MIN_PERSISTENCE_SEC,
                  max_age_sec=DEFAULT_MAX_WALL_AGE_SEC,
                  cluster_tol_bps=10.0):
    """Verified, freshness-gated L3 wall clusters with price inside [lo, hi].

    A cluster aggregates co-located wall quotes (within ``cluster_tol_bps``)
    into a single liquidity object with:
      * ``edge_price``: the price facing the market (max for BUY, min for SELL)
      * ``notional_usd``: aggregated notional
      * ``persistence_sec``: longest observed member span
    Freshness uses the feed's own ``observed_at`` stamp; a wall older than
    ``max_age_sec`` (or from the future) is discarded, never assumed fresh.
    """
    walls = []
    for w in l3_orders or []:
        if w.get("side") != side:
            continue
        px, usd = number(w.get("price")), number(w.get("notional_usd"))
        if px <= 0 or usd < min_notional_usd:
            continue
        if not lo <= px <= hi:
            continue
        span = max(number(w.get("persistence_sec")), number(w.get("observed_span_s")))
        if span < min_persistence_sec:
            continue
        if w.get("is_stale"):
            continue
        observed_at = epoch(w.get("observed_at"))
        if observed_at and not 0.0 <= now - observed_at <= max_age_sec:
            continue
        walls.append({"price": px, "notional_usd": usd, "persistence_sec": span,
                      "order_id": str(w.get("order_id") or f"{w.get('address', 'anon')}:{side}:{px}")})
    if not walls:
        return []
    walls.sort(key=lambda w: w["price"])
    tol = cluster_tol_bps / 10_000.0
    clusters = []
    for w in walls:
        if clusters and abs(math.log(w["price"] / clusters[-1]["price"])) <= tol:
            c = clusters[-1]
            total = c["notional_usd"] + w["notional_usd"]
            c["price"] = (c["price"] * c["notional_usd"] + w["price"] * w["notional_usd"]) / total
            c["edge_price"] = max(c["edge_price"], w["price"]) if side == "BUY" else min(c["edge_price"], w["price"])
            c["notional_usd"] = total
            c["persistence_sec"] = max(c["persistence_sec"], w["persistence_sec"])
            c["members"] += 1
        else:
            clusters.append({**w, "edge_price": w["price"], "members": 1})
    return clusters


def hazard_ttl(span_sec, *, prior_sec=1800.0, survival_target=0.35,
               ttl_min_sec=7200.0, ttl_max_sec=21600.0):
    """Dynamic order TTL from a memoryless wall-survival model (Incident A).

    Model: the anchor wall's remaining life is approximated as exponential
    with rate lambda = 1/(span + prior), where ``span`` is the observed
    persistence of the anchor cluster and ``prior`` is a 30-minute prior that
    regularises freshly-observed walls. The TTL is the horizon at which the
    modelled survival probability falls to ``survival_target``:

        TTL = -ln(p_target) / lambda = -ln(p_target) * (span + prior)

    With p_target = 0.35 the multiplier is ~1.05, so a wall observed for 2h
    earns ~2.6h of resting life and a 6h wall ~7.4h, clipped to the policy
    band [ttl_min_sec, ttl_max_sec] (2h..6h by default). The governor renews
    the deadline monotonically while the wall keeps being observed.
    """
    span = max(0.0, number(span_sec))
    if prior_sec <= 0 or not 0.0 < survival_target < 1.0:
        raise ValueError("invalid_hazard_ttl_parameters")
    lam = 1.0 / (span + prior_sec)
    ttl = -math.log(survival_target) / lam
    return float(min(ttl_max_sec, max(ttl_min_sec, ttl)))


def structural_exit(entry, sl, direction, overhead_clusters, *, tick, friction_r,
                    min_broker_dist=0.0, target_base_r=2.50, target_max_r=2.75,
                    min_net_target_r=1.50, buffer_ticks=2,
                    wall_min_usd=DEFAULT_TPF_WALL_MIN_USD):
    """Orderbook-aware take-profit. Returns (plan, veto_reason).

    LONG exits consider SELL clusters above entry; SHORT exits consider BUY
    clusters below entry. Policy:
      1. Default hurdle is the band target ``target_base_r`` (2.40R..2.75R).
      2. If the first major overhead cluster (>= ``wall_min_usd``) sits inside
         the band, the TP snaps to ``edge - buffer_ticks * tick`` (front-run
         the wall) and the hurdle becomes the wall distance in R.
      3. The hurdle must clear ``min_net_target_r + friction_r``; otherwise
         the candidate is vetoed (net_payoff_insufficient) rather than
         targeting beyond an institutional wall.
      4. The hurdle is capped at ``target_max_r`` so no exit is ever staged
         beyond the ratchet band even when no wall is visible.
    """
    sign = 1.0 if direction == "LONG" else -1.0
    r = abs(entry - sl)
    if r <= 0 or tick <= 0:
        return None, "invalid_exit_geometry"
    ordered = sorted((c for c in overhead_clusters or []
                      if number(c.get("notional_usd")) >= wall_min_usd),
                     key=lambda c: sign * (number(c.get("edge_price")) - entry))
    wall = ordered[0] if ordered else None
    hurdle_r = float(target_base_r)
    mode = "ratchet_band"
    wall_price = wall_notional = None
    if wall is not None:
        wall_price = number(wall["edge_price"])
        wall_notional = number(wall["notional_usd"])
        tp_wall = wall_price - sign * buffer_ticks * tick
        wall_r = sign * (tp_wall - entry) / r
        if wall_r <= 0:
            return None, f"overhead_wall_{wall_price:.6g}_blocks_profit_side"
        if wall_r < hurdle_r:
            hurdle_r = wall_r
            mode = "wall_front_run"
    floor_r = min_net_target_r + max(0.0, number(friction_r))
    if hurdle_r < floor_r:
        return None, (f"net_payoff_insufficient:structural_hurdle_{hurdle_r:.3f}R_"
                      f"below_floor_{floor_r:.3f}R_wall_{wall_price or 0:.6g}")
    tp_r = min(hurdle_r, float(target_max_r))
    raw_tp = entry + sign * tp_r * r
    tp = (math.floor(raw_tp / tick) if sign == 1 else math.ceil(raw_tp / tick)) * tick
    if sign * (tp - entry) < min_broker_dist:
        anchor = entry + sign * min_broker_dist
        tp = (math.floor(anchor / tick) if sign == 1 else math.ceil(anchor / tick)) * tick
    plan = {"tp": tp, "hurdle_r": tp_r, "mode": mode,
            "wall_price": wall_price, "wall_notional_usd": wall_notional or 0.0,
            "target_base_r": float(target_base_r), "target_max_r": float(target_max_r)}
    return plan, None


def classify_sleeve(features):
    """Deterministic sleeve routing: S1 pullback (passive) vs T1 breakout (aggressive).

    T1 requires either a confirmed liquidity vacuum on the profit side
    (opposing magnet present, zero target fuel) or aligned one-sided tape with
    a trending efficiency ratio. Everything else is S1: absorb the discount
    passively ahead of verified walls. The cognitive engine may not override.
    """
    direction = 1 if features.get("direction") == "LONG" else -1
    tape = number(features.get("aggressor_imbalance"))
    er = number(features.get("efficiency_ratio"))
    if features.get("liquidity_vacuum"):
        return "T1_BREAKOUT"
    if er >= 0.35 and abs(tape) >= 0.35 and direction * tape > 0:
        return "T1_BREAKOUT"
    return "S1_PULLBACK"


def anchors_from_clusters(clusters, entry, side, *, max_dist_bps=30.0):
    """Anchor set for the persistence governor: entry-side clusters near the limit.

    The primary anchor is the cluster the resting limit front-runs (highest
    BUY edge below a long entry / lowest SELL edge above a short entry).
    """
    tol = max_dist_bps / 10_000.0
    near = [c for c in clusters or []
            if side == "BUY" and c["edge_price"] <= entry and math.log(entry / max(c["edge_price"], 1e-12)) <= tol
            or side == "SELL" and c["edge_price"] >= entry and math.log(max(c["edge_price"], 1e-12) / entry) <= tol]
    if not near:
        return []
    primary = max(near, key=lambda c: c["edge_price"]) if side == "BUY" else min(near, key=lambda c: c["edge_price"])
    anchors = [{"price": c["edge_price"], "notional_usd": c["notional_usd"],
                "persistence_sec": c["persistence_sec"], "order_id": c["order_id"],
                "role": "primary" if c is primary else "support"}
               for c in sorted(near, key=lambda c: abs(math.log(max(c["edge_price"], 1e-12) / entry)))]
    return anchors


def wall_liveness(anchors, clusters, *, pull_ratio=0.40, match_tol_bps=15.0):
    """Has the primary anchor wall been pulled? (Incident A adverse-selection guard).

    Alive requires a current cluster within ``match_tol_bps`` of the primary
    anchor price holding at least ``pull_ratio`` of the anchored notional.
    Returns (alive, detail) where detail is journalled verbatim.
    """
    primary = next((a for a in anchors or [] if a.get("role") == "primary"), None)
    if primary is None:
        return True, {"reason": "no_primary_anchor", "checked_clusters": len(clusters or [])}
    tol = match_tol_bps / 10_000.0
    matches = [c for c in clusters or []
               if abs(math.log(max(number(c.get("edge_price")), 1e-12) / max(primary["price"], 1e-12))) <= tol]
    if not matches:
        return False, {"reason": "anchor_absent", "anchor_price": primary["price"],
                       "anchor_notional_usd": primary["notional_usd"], "current_notional_usd": 0.0}
    best = max(matches, key=lambda c: number(c.get("notional_usd")))
    retained = number(best.get("notional_usd"))
    alive = retained >= pull_ratio * max(primary["notional_usd"], 1e-9)
    return alive, {"reason": "anchor_retained" if alive else "anchor_thinned",
                   "anchor_price": primary["price"], "anchor_notional_usd": primary["notional_usd"],
                   "current_notional_usd": retained, "retained_ratio": retained / max(primary["notional_usd"], 1e-9)}
