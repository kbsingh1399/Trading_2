"""IntelligenceBus: thread-safe in-memory ring buffers for the Data Factory.

Design (Pillar 6):
  * Per-asset ``RingBuffer`` of the most recent 1,024 trade events, plus the
    latest book snapshot, rolling CVD / taker-flow windows (1m/5m/15m) and a
    footprint tick ladder (volume per discrete price tick).
  * Writes are lock-scoped to an append + index bump (sub-microsecond under
    the GIL); reads take a snapshot copy and filter outside the lock, so the
    15-minute trading loop never contends with feed writers.
  * Every snapshot can be sealed with a SHA-256 digest chain (per asset),
    giving the same tamper-evidence discipline as
    ``Terminal/Deterministic_Features.py`` but for bus-level features.
  * Monotonicity: trade timestamps must be non-decreasing per venue stream;
    violations are counted and exposed (never silently reordered).
"""
from __future__ import annotations
import hashlib
import json
import math
import threading
import time
from collections import deque
from Terminal.Risk_Sizing_Engine import number

CVD_WINDOWS = (60.0, 300.0, 900.0)


class RingBuffer:
    """Fixed-capacity ring buffer with sequence numbers and cheap snapshots."""

    def __init__(self, capacity=1024):
        if capacity < 2:
            raise ValueError("capacity must be >= 2")
        self.capacity = int(capacity)
        self._slots = [None] * self.capacity
        self._head = 0
        self._seq = 0
        self._lock = threading.Lock()

    def append(self, event):
        with self._lock:
            self._slots[self._head] = event
            self._head = (self._head + 1) % self.capacity
            self._seq += 1
            return self._seq

    def snapshot(self, limit=None):
        """Newest-last list of the last ``limit`` events."""
        with self._lock:
            if self._seq == 0:
                return []
            n = self._seq if limit is None else min(self._seq, int(limit), self.capacity)
            out = []
            idx = (self._head - 1) % self.capacity
            for _ in range(min(n, self.capacity)):
                item = self._slots[idx]
                if item is not None:
                    out.append(item)
                idx = (idx - 1) % self.capacity
            out.reverse()
            return out

    def __len__(self):
        return min(self._seq, self.capacity)


class _AssetState:
    __slots__ = ("ticks", "book", "book_lock", "cvd", "footprint", "last_ts",
                 "monotonic_violations", "digest", "volume_by_band")

    def __init__(self, capacity=1024):
        self.ticks = RingBuffer(capacity)
        self.book = None
        self.book_lock = threading.Lock()
        self.cvd = deque()               # (ts_sec, signed_usd)
        self.footprint = {}              # price_bucket -> [buy_sz, sell_sz]
        self.last_ts = {}                # venue -> last trade ts (monotonic check)
        self.monotonic_violations = 0
        self.digest = None               # SHA-256 chain head for sealed snapshots
        self.volume_by_band = {}         # 25bps band index -> traded USD (hazard input)


class IntelligenceBus:
    """The single in-memory store every pillar publishes into."""

    def __init__(self, capacity=1024, tick_size_fn=None):
        self.capacity = int(capacity)
        self.tick_size_fn = tick_size_fn or (lambda asset, price: self._default_tick(asset, price))
        self._assets = {}
        self._lock = threading.Lock()
        self.started_at = time.time()

    # ------------------------------------------------------------- internals
    @staticmethod
    def _default_tick(asset, price):
        if not price or price <= 0:
            return 0.01
        for guess in (0.001, 0.01, 0.1, 1.0):
            if price >= 100 * guess:
                return guess
        return 0.001

    def _state(self, asset):
        with self._lock:
            state = self._assets.get(asset)
            if state is None:
                state = _AssetState(self.capacity)
                self._assets[asset] = state
            return state

    # -------------------------------------------------------------- publish
    def publish_trade(self, asset, *, ts, price, size, side, venue, trade_id=None,
                      notional_usd=None):
        """Record one trade print. ``side`` is the AGGRESSOR side (BUY/SELL).
        Timestamps are per-venue monotonic; regressions are counted, not
        reordered (a venue replay is a data-quality event, not history)."""
        state = self._state(asset)
        ts = float(number(ts))
        last = state.last_ts.get(venue)
        if last is not None and ts < last:
            state.monotonic_violations += 1
            return None  # stale/duplicate venue event: refuse, never reorder
        state.last_ts[venue] = ts
        px = float(number(price))
        sz = float(number(size))
        usd = float(number(notional_usd)) or px * sz
        if px <= 0 or sz <= 0 or ts <= 0:
            return None
        signed = usd if side == "BUY" else -usd if side == "SELL" else 0.0
        event = {"asset": asset, "ts": ts, "price": px, "size": sz, "side": side,
                 "venue": venue, "trade_id": trade_id, "notional_usd": usd}
        state.ticks.append(event)
        with state.book_lock:
            state.cvd.append((ts, signed))
            cut = ts - CVD_WINDOWS[-1] - 5.0
            while state.cvd and state.cvd[0][0] < cut:
                state.cvd.popleft()
            tick = self.tick_size_fn(asset, px)
            bucket = round(px / tick) * tick
            cell = state.footprint.get(bucket)
            if cell is None:
                cell = state.footprint[bucket] = [0.0, 0.0]
            cell[0 if side == "BUY" else 1] += sz
            band = int(math.log(px) / math.log(1.0025))  # 25 bps geometric band
            state.volume_by_band[band] = state.volume_by_band.get(band, 0.0) + usd
        return event

    def publish_book(self, asset, book):
        """Record the latest book snapshot {ts, best_bid, best_ask, bids, asks}."""
        state = self._state(asset)
        with state.book_lock:
            state.book = dict(book)

    def publish_liquidation(self, asset, liquidation):
        """Record a forced-liquidation print (Binance @forceOrder)."""
        state = self._state(asset)
        state.ticks.append({"asset": asset, "kind": "LIQUIDATION", **liquidation})

    # ---------------------------------------------------------------- reads
    def ticks(self, asset, limit=256, since_ts=None):
        state = self._assets.get(asset)
        if state is None:
            return []
        events = state.ticks.snapshot(limit=limit)
        if since_ts is not None:
            events = [e for e in events if e.get("ts", 0) >= since_ts]
        return events

    def book(self, asset):
        state = self._assets.get(asset)
        if state is None:
            return None
        with state.book_lock:
            return dict(state.book) if state.book else None

    def liquidations(self, asset, limit=256):
        return [e for e in self.ticks(asset, limit=4096) if e.get("kind") == "LIQUIDATION"]

    def cvd(self, asset, window_sec=300.0, now=None):
        """Cumulative volume delta over the trailing window (signed USD)."""
        state = self._assets.get(asset)
        if state is None:
            return 0.0
        now = float(number(now, time.time()))
        with state.book_lock:
            cut = now - float(window_sec)
            return sum(usd for ts, usd in state.cvd if ts >= cut)

    def taker_flow(self, asset, window_sec=300.0, now=None):
        """(buy_usd, sell_usd) aggressive notional over the trailing window."""
        state = self._assets.get(asset)
        if state is None:
            return 0.0, 0.0
        now = float(number(now, time.time()))
        cut = now - float(window_sec)
        buy = sell = 0.0
        with state.book_lock:
            for ts, usd in state.cvd:
                if ts >= cut:
                    if usd > 0:
                        buy += usd
                    elif usd < 0:
                        sell -= usd
        return buy, sell

    def footprint(self, asset, top_n=20):
        """Top price buckets by traded size: [{price, buy_sz, sell_sz, total_sz}]."""
        state = self._assets.get(asset)
        if state is None:
            return []
        with state.book_lock:
            rows = [{"price": p, "buy_sz": v[0], "sell_sz": v[1], "total_sz": v[0] + v[1]}
                    for p, v in state.footprint.items()]
        rows.sort(key=lambda r: r["total_sz"], reverse=True)
        return rows[:top_n]

    def volume_by_band(self, asset):
        state = self._assets.get(asset)
        if state is None:
            return {}
        with state.book_lock:
            return dict(state.volume_by_band)

    def mid(self, asset):
        book = self.book(asset)
        if not book:
            return None
        bid, ask = number(book.get("best_bid")), number(book.get("best_ask"))
        if 0 < bid < ask:
            return (bid + ask) / 2.0
        return None

    def depth_imbalance(self, asset, levels=20):
        """Notional-weighted L2 imbalance in [-1, 1] from the latest book."""
        book = self.book(asset)
        if not book:
            return None
        bid_usd = sum(number(r.get("price")) * number(r.get("size"))
                      for r in (book.get("bids") or [])[:levels])
        ask_usd = sum(number(r.get("price")) * number(r.get("size"))
                      for r in (book.get("asks") or [])[:levels])
        if bid_usd + ask_usd <= 0:
            return None
        return (bid_usd - ask_usd) / (bid_usd + ask_usd)

    def monotonic_violations(self, asset=None):
        if asset is None:
            with self._lock:
                return sum(s.monotonic_violations for s in self._assets.values())
        state = self._assets.get(asset)
        return state.monotonic_violations if state else 0

    # ------------------------------------------------------------- snapshot
    def snapshot(self, asset, now=None):
        """Deterministic bus-level feature snapshot (sealable)."""
        now = float(number(now, time.time()))
        mid = self.mid(asset)
        buy1, sell1 = self.taker_flow(asset, 60.0, now)
        buy5, sell5 = self.taker_flow(asset, 300.0, now)
        buy15, sell15 = self.taker_flow(asset, 900.0, now)
        book = self.book(asset) or {}
        spread_bps = None
        if mid and number(book.get("best_bid")):
            spread_bps = (number(book["best_ask"]) - number(book["best_bid"])) / mid * 1e4
        return {
            "asset": asset, "as_of": now, "mid": mid, "spread_bps": spread_bps,
            "cvd_1m": self.cvd(asset, 60.0, now), "cvd_5m": self.cvd(asset, 300.0, now),
            "cvd_15m": self.cvd(asset, 900.0, now),
            "taker_buy_usd_1m": buy1, "taker_sell_usd_1m": sell1,
            "taker_buy_usd_5m": buy5, "taker_sell_usd_5m": sell5,
            "taker_buy_usd_15m": buy15, "taker_sell_usd_15m": sell15,
            "taker_ratio_15m": (buy15 - sell15) / (buy15 + sell15) if buy15 + sell15 > 0 else 0.0,
            "depth_imbalance": self.depth_imbalance(asset),
            "footprint_top": [{"price": r["price"], "total_sz": r["total_sz"]}
                              for r in self.footprint(asset, top_n=8)],
            "monotonic_violations": self.monotonic_violations(asset),
        }

    @staticmethod
    def _canonical(obj):
        return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str)

    def seal(self, asset, now=None):
        """SHA-256 chain seal of the snapshot; returns {snapshot, digest, prev}."""
        snap = self.snapshot(asset, now)
        state = self._state(asset)
        payload = self._canonical({"asset": asset, "snapshot": snap})
        digest = hashlib.sha256((state.digest or "genesis").encode()
                                + b"|" + payload.encode()).hexdigest()
        prev, state.digest = state.digest, digest
        return {"asset": asset, "snapshot": snap, "digest": digest, "prev_digest": prev}
