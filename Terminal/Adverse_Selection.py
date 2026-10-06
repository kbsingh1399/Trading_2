"""Adverse-selection telemetry for resting limit orders (Consultation Q1c).

The monitor watches the same live payloads the governor sees and computes
flow metrics that abort a resting limit *before* price reaches the level:

  * book-thinning velocity  - d ln(V_defense)/dt on the side defending the
    order (bids under a buy limit / asks over a sell limit). Sustained
    halving faster than ``thin_half_life_sec`` is a fade alarm; twice that
    rate is a collapse alarm on its own.
  * cancel-to-trade intensity - notional removed from the defending side per
    unit of traded notional over the window. CTR >= ``ctr_max`` means the
    book is being pulled faster than it is being consumed by trades.
  * aggressor pressure toward the level - share of aggressive volume on the
    side that would run at the order (sellers into a buy limit) while the
    mid is within ``approach_atr`` ATR of the limit.
  * spread velocity - bps per minute of widening.

Aborts require corroboration: the composite hazard score must reach
``abort_score`` (2), except that a collapsing book alone scores 3. All
thresholds are deterministic; every abort is journalled with its alarms.
Snapshots are deduplicated by book timestamp, so the window measures feed
polls (~5s), not heartbeat frequency.
"""
from __future__ import annotations
import math
from collections import deque
from Terminal.Risk_Sizing_Engine import number, epoch


class AdverseSelectionMonitor:
    def __init__(self, *, window=12, thin_half_life_sec=180.0, collapse_factor=2.0,
                 ctr_max=2.5, pressure_min=0.60, approach_atr=1.0,
                 spread_vel_bps_per_min=3.0, abort_score=2, max_book_age=30.0):
        if window < 2 or thin_half_life_sec <= 0:
            raise ValueError("invalid_adverse_selection_parameters")
        self.window = int(window)
        self.thin_rate_per_s = -math.log(2.0)/float(thin_half_life_sec)
        self.collapse_factor = float(collapse_factor)
        self.ctr_max = float(ctr_max)
        self.pressure_min = float(pressure_min)
        self.approach_atr = float(approach_atr)
        self.spread_vel_bps_per_min = float(spread_vel_bps_per_min)
        self.abort_score = int(abort_score)
        self.max_book_age = float(max_book_age)
        self.history = {}
        self._last_book_ts = {}

    # ------------------------------------------------------------- observation
    def observe(self, asset, payload, now):
        """Record one deduplicated L2 snapshot for the asset. Returns the snap."""
        book = payload.get("l2_book") or {}
        ts = epoch(book.get("timestamp"))
        if not ts or not 0.0 <= now-ts <= self.max_book_age:
            return None
        if self._last_book_ts.get(asset) == ts:
            return None  # unchanged snapshot: window counts polls, not heartbeats
        self._last_book_ts[asset] = ts

        def notional(rows):
            total = 0.0
            for r in (rows or [])[:20]:
                px = number(r.get("price", r.get("px")))
                sz = number(r.get("size", r.get("sz")))
                if px > 0 and sz > 0:
                    total += px*sz
            return total

        bid_usd, ask_usd = notional(book.get("bids")), notional(book.get("asks"))
        best_bid, best_ask = number(book.get("best_bid")), number(book.get("best_ask"))
        mid = (best_bid+best_ask)/2.0 if 0 < best_bid < best_ask else 0.0
        spread_bps = (best_ask-best_bid)/mid*1e4 if mid > 0 else 0.0
        buy_usd = sell_usd = 0.0
        for t in payload.get("recent_trades") or []:
            if not 0.0 <= now-epoch(t.get("time")) <= 60:
                continue
            usd = number(t.get("notional_usd")) or number(t.get("price"))*number(t.get("size"))
            if t.get("side") == "BUY":
                buy_usd += usd
            elif t.get("side") == "SELL":
                sell_usd += usd
        snap = {"t": float(now), "ts": ts, "bid_usd": bid_usd, "ask_usd": ask_usd,
                "mid": mid, "spread_bps": spread_bps, "buy_usd": buy_usd, "sell_usd": sell_usd}
        self.history.setdefault(asset, deque(maxlen=self.window)).append(snap)
        return snap

    # ------------------------------------------------------------------ hazard
    def hazard(self, asset, direction, limit_price, atr):
        """Composite abort score plus the individual alarms (deterministic)."""
        alarms = {}
        hist = self.history.get(asset)
        if not hist or len(hist) < 2:
            return 0, alarms
        first, last = hist[0], hist[-1]
        dt = last["t"]-first["t"]
        if dt <= 5:
            return 0, alarms
        defending = "bid_usd" if direction == "LONG" else "ask_usd"
        v0, v1 = first[defending], last[defending]
        if v0 > 0:
            rate = math.log(max(v1, 1e-9)/v0)/dt
            if rate <= self.thin_rate_per_s:
                alarms["book_thinning"] = {"rate_per_s": round(rate, 6), "window_s": round(dt, 1)}
            if rate <= self.collapse_factor*self.thin_rate_per_s:
                alarms["book_collapsing"] = {"rate_per_s": round(rate, 6)}
        traded = sum(h["buy_usd"]+h["sell_usd"] for h in hist)
        removed = max(0.0, v0-v1)
        if traded > 0 and removed/traded >= self.ctr_max:
            alarms["cancel_intensity"] = {"ctr": round(removed/traded, 2)}
        if last["mid"] > 0:
            toward = last["sell_usd"] if direction == "LONG" else last["buy_usd"]
            total = last["buy_usd"]+last["sell_usd"]
            if total > 0:
                share = toward/total
                near = abs(last["mid"]-limit_price) <= self.approach_atr*max(number(atr), 1e-9)
                if share >= self.pressure_min and near:
                    alarms["aggressor_pressure"] = {"share": round(share, 3)}
            spread_vel = (last["spread_bps"]-first["spread_bps"])/(dt/60.0)
            if spread_vel >= self.spread_vel_bps_per_min:
                alarms["spread_velocity"] = {"bps_per_min": round(spread_vel, 2)}
        score = len(alarms)+(1 if "book_collapsing" in alarms else 0)
        return score, alarms
