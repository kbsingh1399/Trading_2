"""Order Persistence & TTL Governor for resting limit orders (Incident A).

The governor owns the lifecycle of *persistent* (GTC) limit orders that rest
for hours ahead of verified whale walls. The 15-minute decision cadence in
``Omni_Trader.evaluate_market`` is untouched: staging still happens in minute
14, but the resting order is then managed continuously (every ``run`` loop
tick) by this component, which is the single authority for:

  * Dynamic TTL: an exponential wall-survival horizon (see
    ``Orderbook_Structure.hazard_ttl``), renewed monotonically while the
    anchor wall persists, hard-capped at ``ttl_max_sec`` after staging.
  * Wall tracking: cancel when the primary anchor wall is pulled or thinned
    below ``pull_ratio`` (adverse-selection guard), and cancel/replace when
    the wall *shifts* inside ``replace_shift_bps`` while still qualifying.
  * Queue-priority hysteresis (Q1b): a replace is only worth losing queue
    position when the shift clears a noise-adaptive threshold:
    ``max(min_shift_bps, 2 x MAD(edge shifts), proximity floor)``. Micro
    shifts (e.g. SOL whale breathing 118.41 -> 118.45) are absorbed first by
    cluster aggregation (10 bps) and the liveness match tolerance, then by
    the shift floor; the replacement wall must also have persisted at least
    ``dwell_sec`` (flicker filter).
  * Adverse-selection telemetry (Q1c): an ``AdverseSelectionMonitor`` scores
    book-thinning velocity, cancel-to-trade intensity, aggressor pressure
    toward the level and spread velocity; a corroborated hazard aborts the
    order before price reaches the level.
  * Drift bounds: cancel when price wanders further than ``drift_atr`` * ATR
    from the limit with no surviving anchor (1.5x ATR) or with one (3.0x).
  * Fill-race safety: a cancel that comes back "order unknown" is treated as
    UNCERTAIN and never followed by a replacement in the same cycle; the
    reconciler in ``Omni_Trader._reconcile`` owns disappearance semantics.

The governor never sizes trades and never places orders that were not already
vetted by the deterministic candidate pipeline; a replacement preserves the
original R-geometry (same volume, same R distance, same hurdle), so USD risk
and friction exposure are invariant across a replace.
"""
from __future__ import annotations
import math
import time

from Terminal.Orderbook_Structure import (wall_clusters, hazard_ttl, wall_liveness,
                                          DEFAULT_ENTRY_WALL_MIN_USD)
from Terminal.Risk_Sizing_Engine import number, epoch
from Terminal.Adverse_Selection import AdverseSelectionMonitor


def _round_to_tick(price, tick, direction_up):
    if tick <= 0:
        return float(price)
    steps = price / tick
    return (math.floor(steps + 1e-9) if direction_up else math.ceil(steps - 1e-9)) * tick


def _median(values):
    ordered = sorted(values)
    n = len(ordered)
    if n == 0:
        return 0.0
    return ordered[n//2] if n % 2 else 0.5*(ordered[n//2-1]+ordered[n//2])


class OrderPersistenceGovernor:
    def __init__(self, bridge=None, journal=None, clock=time.time, *,
                 ttl_min_sec=7200.0, ttl_max_sec=21600.0,
                 pull_ratio=0.40, match_tol_bps=15.0, replace_shift_bps=75.0,
                 drift_atr_no_anchor=1.5, drift_atr_anchored=3.0,
                 max_recenters=2, scan_band_atr=2.5, wall_min_usd=DEFAULT_ENTRY_WALL_MIN_USD,
                 dwell_sec=240.0, min_shift_bps=5.0, proximity_bps=25.0, proximity_atr=0.25,
                 adverse=None):
        if not 0 < ttl_min_sec <= ttl_max_sec:
            raise ValueError("ttl band invalid")
        self.bridge = bridge
        self.journal = journal or (lambda name, record: None)
        self.clock = clock
        self.ttl_min_sec, self.ttl_max_sec = float(ttl_min_sec), float(ttl_max_sec)
        self.pull_ratio, self.match_tol_bps = float(pull_ratio), float(match_tol_bps)
        self.replace_shift_bps, self.max_recenters = float(replace_shift_bps), int(max_recenters)
        self.drift_atr_no_anchor, self.drift_atr_anchored = float(drift_atr_no_anchor), float(drift_atr_anchored)
        self.scan_band_atr, self.wall_min_usd = float(scan_band_atr), float(wall_min_usd)
        self.dwell_sec, self.min_shift_bps = float(dwell_sec), float(min_shift_bps)
        self.proximity_bps, self.proximity_atr = float(proximity_bps), float(proximity_atr)
        self.adverse = adverse if adverse is not None else AdverseSelectionMonitor()
        self.orders = {}

    # ------------------------------------------------------------------ state
    def load(self, state):
        self.orders = {str(k): dict(v) for k, v in (state or {}).items()
                       if isinstance(v, dict) and v.get("status") == "RESTING"}

    def export(self):
        return {k: dict(v) for k, v in self.orders.items()}

    def count(self):
        return len(self.orders)

    # ----------------------------------------------------------------- events
    def register(self, key, *, asset, symbol, direction, order_ticket, limit_price,
                 sl, tp, volume, anchors, atr, ttl_sec, now, comment, hurdle_r,
                 risk_usd=0.0, tick_size=0.01, magic=100895):
        if key in self.orders:
            raise ValueError("governor_duplicate_registration")
        self.orders[key] = {
            "asset": asset, "symbol": symbol, "direction": direction,
            "order_ticket": int(order_ticket), "limit_price": float(limit_price),
            "sl": float(sl), "tp": float(tp), "volume": float(volume),
            "anchors": [dict(a) for a in anchors or []], "atr": float(atr),
            "r": abs(float(limit_price) - float(sl)), "hurdle_r": float(hurdle_r or 0.0),
            "risk_usd": float(risk_usd), "comment": comment,
            "tick_size": float(tick_size), "magic": int(magic),
            "staged_at": float(now), "deadline": float(now) + float(ttl_sec),
            "hard_deadline": float(now) + self.ttl_max_sec,
            "recenters": 0, "status": "RESTING", "cancel_uncertain_at": 0.0,
        }
        self.journal("executions.jsonl", {"time": self.clock(), "event": "governor_register",
                                          "intent_id": key, "order_ticket": int(order_ticket),
                                          "anchors": self.orders[key]["anchors"],
                                          "deadline": self.orders[key]["deadline"],
                                          "ttl_sec": float(ttl_sec)})
        return self.orders[key]

    # -------------------------------------------------------------- main loop
    def heartbeat(self, *, now, intents, payloads, pending, quote_fn):
        """Manage every resting order once. Returns a list of change records.

        ``intents`` is the trader intent table (status STAGED_LIMIT keeps the
        order alive), ``payloads`` the latest feed snapshot per asset,
        ``pending`` the broker pending-order inventory and ``quote_fn(symbol)``
        a fresh-quote callable that may raise ValueError when stale.
        """
        changes = []
        pending_tickets = {int(o.get("ticket", 0)) for o in (pending or [])}
        for key in list(self.orders):
            order = self.orders.get(key)
            if order is None:
                continue
            intent = (intents or {}).get(key) or {}
            if intent.get("status") != "STAGED_LIMIT" or order["order_ticket"] not in pending_tickets:
                # Filled, expired, cancelled elsewhere or already reconciled:
                # disappearance semantics belong to the reconciler only.
                self.orders.pop(key, None)
                self.journal("executions.jsonl", {"time": now, "event": "governor_release",
                                                  "intent_id": key,
                                                  "intent_status": intent.get("status"),
                                                  "order_ticket": order["order_ticket"]})
                continue
            if order.get("cancel_uncertain_at", 0.0) > 0:
                # Retry a cancel that previously came back ambiguous. Never
                # replace in the same cycle as an uncertain cancel.
                changes.append(self._cancel(key, order, now, reason="cancel_retry_after_uncertain"))
                continue
            payload = (payloads or {}).get(order["asset"]) or {}
            try:
                quote = quote_fn(order["symbol"]) if quote_fn else None
            except (ValueError, RuntimeError):
                quote = None
            clusters, wall_data_fresh = self._anchor_scan(order, payload, now)
            alive, detail = wall_liveness(order["anchors"], clusters,
                                          pull_ratio=self.pull_ratio,
                                          match_tol_bps=self.match_tol_bps)
            # Track the primary anchor's observed edge for noise-adaptive
            # re-center hysteresis (Q1b).
            if alive and wall_data_fresh:
                matched = self._matched_edge(order, clusters)
                if matched:
                    history = order.setdefault("edge_history", [])
                    if not history or abs(math.log(max(matched, 1e-12)/max(history[-1], 1e-12))) > 1e-9:
                        history.append(matched)
                    del history[:-16]
            # 1) TTL expiry first: a deadline that has passed must cancel
            #    before any renewal arithmetic can lift it (the renewal below
            #    only ever extends a still-live deadline).
            if now >= order["deadline"] or now >= order["hard_deadline"]:
                changes.append(self._cancel(key, order, now, reason="ttl_expired",
                                            detail={"deadline": order["deadline"],
                                                    "hard_deadline": order["hard_deadline"]}))
                continue
            # 2) TTL renewal while the anchor keeps being observed.
            ttl = hazard_ttl(self._primary_span(order, clusters, wall_data_fresh),
                             ttl_min_sec=self.ttl_min_sec, ttl_max_sec=self.ttl_max_sec)
            order["deadline"] = min(max(order["deadline"], now + ttl), order["hard_deadline"])
            # 3) Anchor pull: cancel, or cancel/replace onto a shifted wall
            #    that clears the queue-priority hysteresis threshold.
            if not alive:
                shift = self._replacement_cluster(order, clusters, quote)
                if shift is not None and order["recenters"] < self.max_recenters:
                    changes.extend(self._replace(key, order, shift, now, detail))
                else:
                    changes.append(self._cancel(key, order, now, reason="anchor_wall_pulled", detail=detail))
                continue
            # 4) Adverse-selection telemetry (Q1c): corroborated flow hazard
            #    aborts the order before price reaches the level.
            if self.adverse is not None:
                try:
                    self.adverse.observe(order["asset"], payload, now)
                    score, alarms = self.adverse.hazard(order["asset"], order["direction"],
                                                        order["limit_price"], order["atr"])
                    if score >= self.adverse.abort_score:
                        changes.append(self._cancel(key, order, now, reason="adverse_selection_hazard",
                                                    detail={"score": score, "alarms": alarms}))
                        continue
                except Exception:
                    pass
            # 5) Adverse drift guard (outer bound; the trader keeps its own
            #    structural check as defence in depth).
            drift_atr = self.drift_atr_no_anchor if not order["anchors"] else self.drift_atr_anchored
            if quote and order["atr"] > 0:
                mid = (number(quote.get("bid")) + number(quote.get("ask"))) / 2.0
                if abs(mid - order["limit_price"]) > drift_atr * order["atr"]:
                    changes.append(self._cancel(key, order, now, reason="adverse_drift",
                                                detail={"mid": mid, "limit": order["limit_price"],
                                                        "atr": order["atr"]}))
                    continue
            order["last_heartbeat"] = now
            order["liveness"] = detail
        return changes

    # ---------------------------------------------------------------- helpers
    def _anchor_scan(self, order, payload, now):
        """Entry-side clusters for this order from the freshest payload."""
        sources = payload.get("sources") or {}
        observed = epoch((sources.get("l3") or {}).get("observed_at") or payload.get("timestamp"))
        fresh = bool(observed and 0.0 <= now - observed <= 60.0)
        if not fresh:
            return [], False
        side = "BUY" if order["direction"] == "LONG" else "SELL"
        ref = order["limit_price"]
        band = self.scan_band_atr * max(order["atr"], 1e-9)
        lo, hi = (ref - band, ref + 0.05 * max(order["atr"], 1e-9)) if side == "BUY" else (ref - 0.05 * max(order["atr"], 1e-9), ref + band)
        clusters = wall_clusters(payload.get("l3_orders", []), side, lo, hi, now,
                                 min_notional_usd=min(self.wall_min_usd * self.pull_ratio, self.wall_min_usd),
                                 min_persistence_sec=0.0, max_age_sec=60.0)
        return clusters, True

    def _primary_span(self, order, clusters, fresh):
        primary = next((a for a in order["anchors"] if a.get("role") == "primary"),
                       (order["anchors"] or [{}])[0] if order["anchors"] else None)
        if primary is None:
            return 0.0
        if fresh and clusters:
            tol = self.match_tol_bps / 10_000.0
            for c in clusters:
                if abs(math.log(max(number(c.get("edge_price")), 1e-12) / max(primary["price"], 1e-12))) <= tol:
                    return max(number(c.get("persistence_sec")), number(primary.get("persistence_sec")))
        return number(primary.get("persistence_sec"))

    def _matched_edge(self, order, clusters):
        """Current edge of the cluster matching the primary anchor, if any."""
        primary = next((a for a in order["anchors"] if a.get("role") == "primary"), None)
        if primary is None or not clusters:
            return None
        tol = self.match_tol_bps / 10_000.0
        for c in clusters:
            if abs(math.log(max(number(c.get("edge_price")), 1e-12) / max(primary["price"], 1e-12))) <= tol:
                return number(c.get("edge_price"))
        return None

    def _replace_threshold_bps(self, order, quote=None):
        """Queue-priority hysteresis threshold (Q1b): the minimum wall shift,
        in bps, that justifies losing our queue position via cancel/replace.

        ``max(min_shift_bps, 2 x MAD(edge shifts), proximity floor)`` where
        the proximity floor widens to ``proximity_bps`` once price is within
        ``proximity_atr`` ATR of the limit: at the touch, queue priority is
        worth the most.
        """
        threshold = self.min_shift_bps
        history = order.get("edge_history") or []
        if len(history) >= 4:
            shifts = [abs(math.log(max(history[i], 1e-12)/max(history[i-1], 1e-12))) * 1e4
                      for i in range(1, len(history))]
            if shifts:
                threshold = max(threshold, 2.0*_median(shifts))
        if quote and order.get("atr", 0) > 0:
            mid = (number(quote.get("bid")) + number(quote.get("ask"))) / 2.0
            if mid > 0 and abs(mid-order["limit_price"]) <= self.proximity_atr*order["atr"]:
                threshold = max(threshold, self.proximity_bps)
        return threshold

    def _replacement_cluster(self, order, clusters, quote=None):
        """A qualifying shifted wall to re-anchor onto, if any.

        A wall that merely thinned at the same price is a pull (cancel), not
        a shift; only a genuine relocation beyond the hysteresis threshold
        (and inside ``replace_shift_bps``) that has itself persisted at least
        ``dwell_sec`` qualifies for a cancel/replace.
        """
        primary = next((a for a in order["anchors"] if a.get("role") == "primary"), None)
        if primary is None or not clusters:
            return None
        tol = self.replace_shift_bps / 10_000.0
        min_shift = self._replace_threshold_bps(order, quote) / 10_000.0
        side = "BUY" if order["direction"] == "LONG" else "SELL"
        candidates = [c for c in clusters
                      if number(c.get("notional_usd")) >= self.wall_min_usd
                      and number(c.get("persistence_sec")) >= self.dwell_sec
                      and min_shift <= abs(math.log(max(number(c.get("edge_price")), 1e-12) / max(primary["price"], 1e-12))) <= tol]
        if not candidates:
            return None
        return (max(candidates, key=lambda c: c["edge_price"]) if side == "BUY"
                else min(candidates, key=lambda c: c["edge_price"]))

    def _cancel(self, key, order, now, *, reason, detail=None):
        record = {"time": now, "event": "governor_cancel", "intent_id": key,
                  "order_ticket": order["order_ticket"], "reason": reason, "detail": detail or {}}
        result = None
        if self.bridge is not None:
            try:
                result = self.bridge.cancel_pending_order(order["order_ticket"])
            except Exception as exc:  # IPC failure is uncertainty, never success
                result = {"success": False, "uncertain": True, "error": str(exc)}
        record["result"] = result
        if result is None or result.get("success"):
            self.orders.pop(key, None)
        elif result.get("uncertain") or _order_unknown(result):
            order["cancel_uncertain_at"] = now
            record["uncertain"] = True
            # Keep the order registered; a fill in the cancel window is
            # resolved by the reconciler, and the cancel is retried next beat.
        else:
            # Definite rejection (e.g. already filling): release to reconciler.
            self.orders.pop(key, None)
        self.journal("executions.jsonl", record)
        return record

    def _replace(self, key, order, cluster, now, detail):
        """Cancel/replace onto a shifted wall preserving R-geometry and risk."""
        sign = 1.0 if order["direction"] == "LONG" else -1.0
        side = "BUY" if order["direction"] == "LONG" else "SELL"
        new_edge = number(cluster.get("edge_price"))
        new_limit = new_edge + sign * max(order.get("tick_size", 0.01) or 0.01, 1e-9)
        new_sl = new_limit - sign * order["r"]
        new_tp = new_limit + sign * order["hurdle_r"] * order["r"]
        actions = []
        cancel = self._cancel(key, order, now, reason="anchor_shifted_replace", detail=detail)
        actions.append(cancel)
        if order.get("cancel_uncertain_at", 0.0) > 0 or not (cancel.get("result") or {}).get("success", True):
            return actions  # never stage a second order while the first is ambiguous
        if self.bridge is None or not hasattr(self.bridge, "stage_limit_order"):
            return actions
        try:
            result = self.bridge.stage_limit_order(order["symbol"], order["direction"], order["volume"],
                                                   new_limit, new_sl, new_tp,
                                                   persistent=True, magic=order.get("magic", 100895),
                                                   comment=order["comment"])
        except Exception as exc:
            result = {"success": False, "error": str(exc)}
        record = {"time": now, "event": "governor_replace", "intent_id": key,
                  "old_limit": order["limit_price"], "new_limit": new_limit,
                  "new_sl": new_sl, "new_tp": new_tp, "cluster_edge": new_edge,
                  "result": result}
        if result.get("success"):
            order.update(order_ticket=int(result.get("ticket") or 0), limit_price=new_limit,
                         sl=new_sl, tp=new_tp, recenters=order["recenters"] + 1,
                         deadline=min(max(order["deadline"], now + hazard_ttl(cluster.get("persistence_sec"),
                            ttl_min_sec=self.ttl_min_sec, ttl_max_sec=self.ttl_max_sec)), order["hard_deadline"]),
                         cancel_uncertain_at=0.0,
                         anchors=[{"price": new_edge, "notional_usd": number(cluster.get("notional_usd")),
                                   "persistence_sec": number(cluster.get("persistence_sec")),
                                   "order_id": cluster.get("order_id"), "role": "primary"}])
            # The cancel above removed the registry entry; re-adopt the replacement.
            self.orders[key] = order
        else:
            order["cancel_uncertain_at"] = 0.0
        self.journal("executions.jsonl", record)
        actions.append(record)
        return actions


def _order_unknown(result):
    text = str(result.get("error", "")).lower()
    return "not found" in text or "unknown" in text
