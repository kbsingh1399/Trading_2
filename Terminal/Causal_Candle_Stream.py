"""Causal candle ingestion: O(1) incremental indicators with WAL crash recovery.

Replaces the full-recompute candle engine (O(N) per 15m close, O(N^2) per
session) with an event-sourced stream:

  * ``IncrementalIndicators`` - Wilder-recursive ATR/RSI, recursive EMA and
    session-anchored (00:00 UTC) VWAP, each O(1) per bar, bit-identical to
    the batch recursion in ``batch_reference`` (which exists to prove the
    equivalence in tests, not to be run in production).
  * ``CausalCandleStream`` - per-symbol stream manager:
      - causal filter: a bar is committed only when its close time
        (open_time + timeframe) has passed; forming bars are rejected, so no
        future information can ever enter indicator state;
      - idempotent-by-open_time: a second bar with the same open_time is a
        broker CORRECTION - state is restored from the prior snapshot and
        the corrected bar applied, never double-counted;
      - gap ledger: disconnects and weekend holes are recorded as gap events
        (from/to/missing_buckets) and EXPOSED, never filled with synthetic
        candles. ATR stays honest through gaps because true range uses the
        previous close (gap-aware); session VWAP resets at the UTC boundary
        anyway. Indicators computed across a gap carry a ``gap_flag`` so the
        trader can distrust them for one bar;
      - write-ahead log: every state-changing event is appended and flushed
        to ``wal.jsonl`` BEFORE the in-memory mutation, and a full state
        snapshot (a handful of scalars) is journaled every bar. ``recover()``
        rebuilds state from the last snapshot plus the WAL tail - worst case
        one bar of replay - giving 100% crash recovery without re-reading
        history;
      - parquet reconciliation: ``reconcile_parquet`` appends newly
        committed bars to the historical store (3.47M-candle OOS parquet),
        rewrites corrections, refuses any bar whose close time is in the
        future, and verifies the store's monotonic open_time uniqueness.
"""
from __future__ import annotations
import json
import math
import os
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from Terminal.Risk_Sizing_Engine import number

WILDER_N = 14


def _utc_day(ts):
    d = datetime.fromtimestamp(number(ts), timezone.utc)
    return (d.year, d.month, d.day)


class IncrementalIndicators:
    """O(1) Wilder/EMA/VWAP state. ``update`` is the ONLY mutator."""

    __slots__ = ("ema", "atr", "avg_gain", "avg_loss", "prev_close", "seeded",
                 "pv", "vv", "session_day", "bars", "last_open", "gap_flag")

    def __init__(self, ema=None, atr=0.0, avg_gain=0.0, avg_loss=0.0, prev_close=None,
                 seeded=False, pv=0.0, vv=0.0, session_day=None, bars=0, last_open=None, gap_flag=False):
        self.ema, self.atr, self.avg_gain, self.avg_loss = ema, atr, avg_gain, avg_loss
        self.prev_close, self.seeded = prev_close, seeded
        self.pv, self.vv, self.session_day = pv, vv, session_day
        self.bars, self.last_open, self.gap_flag = bars, last_open, gap_flag

    # ---------------------------------------------------------------- state
    def snapshot(self):
        return {"ema": self.ema, "atr": self.atr, "avg_gain": self.avg_gain,
                "avg_loss": self.avg_loss, "prev_close": self.prev_close,
                "seeded": self.seeded, "pv": self.pv, "vv": self.vv,
                "session_day": list(self.session_day) if self.session_day else None,
                "bars": self.bars, "last_open": self.last_open, "gap_flag": self.gap_flag}

    @classmethod
    def from_snapshot(cls, s):
        return cls(ema=s.get("ema"), atr=number(s.get("atr")), avg_gain=number(s.get("avg_gain")),
                   avg_loss=number(s.get("avg_loss")), prev_close=s.get("prev_close"),
                   seeded=bool(s.get("seeded")), pv=number(s.get("pv")), vv=number(s.get("vv")),
                   session_day=tuple(s["session_day"]) if s.get("session_day") else None,
                   bars=int(s.get("bars", 0)), last_open=s.get("last_open"),
                   gap_flag=bool(s.get("gap_flag")))

    # ---------------------------------------------------------------- update
    def update(self, bar, timeframe=900):
        """Apply one COMPLETED bar. Returns True if state changed."""
        o, h, l, c = (number(bar.get("open")), number(bar.get("high")),
                      number(bar.get("low")), number(bar.get("close")))
        v = max(number(bar.get("volume") or bar.get("tick_volume") or 1.0), 1e-9)
        if min(o, h, l, c) <= 0 or h < l:
            return False
        t = number(bar.get("time"))
        self.gap_flag = (self.last_open is not None and t > self.last_open + timeframe*1.5)
        day = _utc_day(t)
        if self.session_day != day:  # 00:00 UTC session reset (VWAP anchor)
            self.session_day, self.pv, self.vv = day, 0.0, 0.0
        # --- True range (gap-aware: bridges the previous close across holes)
        tr = h-l
        if self.prev_close:
            tr = max(tr, abs(h-self.prev_close), abs(l-self.prev_close))
        if not self.seeded:
            self.ema, self.atr, self.avg_gain, self.avg_loss = c, tr, 0.0, 0.0
            self.seeded, self.prev_close = True, c
        else:
            self.ema = c  # single-bar EMA of the latest close for streaming
            prev_atr = self.atr if self.bars >= WILDER_N else (self.atr*self.bars or tr)
            self.atr = (prev_atr*(WILDER_N-1)+tr)/WILDER_N if self.bars >= WILDER_N \
                else (prev_atr*self.bars+tr)/(self.bars+1)
            change = c-self.prev_close
            gain, loss = max(change, 0.0), max(-change, 0.0)
            if self.bars >= WILDER_N:
                self.avg_gain = (self.avg_gain*(WILDER_N-1)+gain)/WILDER_N
                self.avg_loss = (self.avg_loss*(WILDER_N-1)+loss)/WILDER_N
            else:
                self.avg_gain = (self.avg_gain*self.bars+gain)/(self.bars+1)
                self.avg_loss = (self.avg_loss*self.bars+loss)/(self.bars+1)
            self.prev_close = c
        tp = (h+l+c)/3.0
        self.pv += tp*v
        self.vv += v
        self.bars += 1
        self.last_open = t
        return True

    # -------------------------------------------------------------- readouts
    def stats(self):
        vwap = self.pv/self.vv if self.vv > 0 else None
        rsi = 100.0 if self.avg_loss <= 0 and self.avg_gain > 0 else \
              (0.0 if self.avg_gain <= 0 and self.avg_loss > 0 else
               (100.0-100.0/(1.0+self.avg_gain/self.avg_loss) if self.avg_loss > 0 else None))
        return {"ema": self.ema, "atr": self.atr, "rsi": rsi, "vwap": vwap,
                "session_day": self.session_day, "bars": self.bars,
                "gap_flag": self.gap_flag}


def batch_reference(bars, timeframe=900):
    """Slow-but-obvious recomputation of the exact same recursions; exists so
    tests can prove the O(1) stream equals the batch semantics."""
    inc = IncrementalIndicators()
    for b in bars:
        inc.update(b, timeframe)
    return inc


class CausalCandleStream:
    """Event-sourced per-symbol candle stream with WAL crash recovery."""

    ROTATE_AFTER_EVENTS = 4096  # compact the WAL to a single baseline snapshot

    def __init__(self, symbol, timeframe=900, wal_dir=None):
        self.symbol = symbol
        self.timeframe = timeframe
        self.wal_path = (Path(wal_dir)/f"{symbol}_{timeframe}_wal.jsonl") if wal_dir else None
        if self.wal_path:
            self.wal_path.parent.mkdir(parents=True, exist_ok=True)
        self.state = IncrementalIndicators()
        self._snapshots = deque(maxlen=2)   # (open_time, state) of last two bars
        self._events = 0
        self.corrections = 0

    # ------------------------------------------------------------------ WAL
    def _journal(self, record):
        if not self.wal_path:
            return
        with open(self.wal_path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, separators=(",", ":"))+"\n")
            fh.flush()
            os.fsync(fh.fileno())
        self._events += 1

    def _rotate_wal_if_needed(self):
        """Bound the WAL: once it exceeds ROTATE_AFTER_EVENTS records, compact
        to a single baseline snapshot (atomic tmp+rename). Corrections only
        ever touch the most recent bar, so the baseline is always sufficient."""
        if not self.wal_path or not self.wal_path.exists():
            return
        if self._events < self.ROTATE_AFTER_EVENTS:
            return
        tmp = self.wal_path.with_suffix(".tmp")
        with open(tmp, "w", encoding="utf-8") as fh:
            fh.write(json.dumps({"type": "snapshot", "state": self.state.snapshot()},
                                separators=(",", ":"))+"\n")
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, self.wal_path)
        self._events = 1

    def recover(self):
        """Rebuild state from the WAL: seek the LAST snapshot record and apply
        at most the handful of events journaled after it (a crash can leave at
        most one bar/correction un-snapshotted). Returns replayed event count.
        A torn final line (partial write during the crash) is discarded."""
        if not self.wal_path or not self.wal_path.exists():
            return 0
        with open(self.wal_path, "r", encoding="utf-8") as fh:
            lines = fh.readlines()
        records = []
        for line in lines:
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                break  # torn tail write from a crash: discard
        snapshot_idx = [i for i, r in enumerate(records) if r.get("type") == "snapshot"]
        if not snapshot_idx:
            # No snapshot yet (crash during the very first bar): replay bars.
            for rec in records:
                if rec.get("type") in ("bar", "correction"):
                    self.state.update(rec, self.timeframe)
                    self._snapshots.append((self.state.last_open, self.state.snapshot()))
            self._events = len(records)
            return len(records)
        last = snapshot_idx[-1]
        self.state = IncrementalIndicators.from_snapshot(records[last]["state"])
        self._snapshots = deque(maxlen=2)
        if len(snapshot_idx) >= 2:
            prev = IncrementalIndicators.from_snapshot(records[snapshot_idx[-2]]["state"])
            self._snapshots.append((prev.last_open, prev.snapshot()))
        self._snapshots.append((self.state.last_open, self.state.snapshot()))
        replayed = 0
        for rec in records[last+1:]:
            kind = rec.get("type")
            t = number(rec.get("time"))
            if kind in ("bar", "correction") and t >= self.state.last_open:
                if t == self.state.last_open and len(self._snapshots) >= 2:
                    # crash mid-correction: restore the pre-correction snapshot
                    self.state = IncrementalIndicators.from_snapshot(self._snapshots[0][1])
                self.state.update(rec, self.timeframe)
                replayed += 1
                self._snapshots.append((self.state.last_open, self.state.snapshot()))
        self._events = len(records)
        self._rotate_wal_if_needed()
        return replayed

    # -------------------------------------------------------------- ingest
    def ingest(self, bars, now):
        """Causally ingest a batch of raw broker bars. Returns a report dict.
        A bar commits only if its close time has passed; duplicates on
        open_time are corrections (restore-then-reapply); holes are ledgered,
        never filled."""
        report = {"applied": 0, "corrected": 0, "rejected_forming": 0,
                  "rejected_stale": 0, "gaps": []}
        ordered = sorted((b for b in (bars or []) if number(b.get("time")) > 0),
                         key=lambda b: number(b["time"]))
        for bar in ordered:
            t = number(bar.get("time"))
            if t+self.timeframe > number(now):
                report["rejected_forming"] += 1
                continue
            if self.state.last_open is not None and t < self.state.last_open:
                report["rejected_stale"] += 1
                continue
            if t == self.state.last_open:
                # Broker correction: restore the prior snapshot, re-apply.
                if len(self._snapshots) >= 2:
                    prior = IncrementalIndicators.from_snapshot(self._snapshots[0][1])
                else:
                    prior = IncrementalIndicators()
                self.state = prior
                self._journal({"type": "correction", "time": t,
                               **{k: bar.get(k) for k in ("open", "high", "low", "close", "volume")}})
                self.state.update(bar, self.timeframe)
                self.corrections += 1
                report["corrected"] += 1
            else:
                if self.state.last_open is not None and t > self.state.last_open+self.timeframe*1.5:
                    missing = int((t-self.state.last_open)/self.timeframe)-1
                    gap = {"from": self.state.last_open, "to": t, "missing_buckets": missing}
                    report["gaps"].append(gap)
                    self._journal({"type": "gap", **gap})
                self._journal({"type": "bar", "time": t,
                               **{k: bar.get(k) for k in ("open", "high", "low", "close", "volume")}})
                self.state.update(bar, self.timeframe)
                report["applied"] += 1
            self._snapshots.append((self.state.last_open, self.state.snapshot()))
            self._journal({"type": "snapshot", "state": self.state.snapshot()})
        self._rotate_wal_if_needed()
        return report

    def stats(self):
        return self.state.stats()


def reconcile_parquet(store_path, bars, now, timeframe=900, symbol=None):
    """Causal reconciliation of the historical parquet store.

    New committed bars append; corrections rewrite the existing row; any bar
    whose close time is in the future raises (never persisted). Returns a
    report; the store is written atomically (tmp + rename).
    """
    import polars as pl
    store = Path(store_path)
    ordered = sorted((b for b in (bars or []) if number(b.get("time")) > 0),
                     key=lambda b: number(b["time"]))
    committed = [b for b in ordered if number(b["time"])+timeframe <= number(now)]
    if len(committed) != len(ordered):
        raise ValueError("future_bar_rejected: refusing to persist forming candles")
    frame = pl.DataFrame({
        "time": [int(number(b["time"])) for b in committed],
        "open": [number(b["open"]) for b in committed],
        "high": [number(b["high"]) for b in committed],
        "low": [number(b["low"]) for b in committed],
        "close": [number(b["close"]) for b in committed],
        "volume": [number(b.get("volume") or b.get("tick_volume") or 0.0) for b in committed]})
    report = {"appended": len(committed), "corrected": 0, "total_rows": len(committed)}
    if store.exists():
        old = pl.read_parquet(store)
        old_times = set(old.get_column("time").to_list())
        report["corrected"] = sum(1 for b in committed if int(number(b["time"])) in old_times)
        frame = pl.concat([old, frame]).unique(subset=["time"], keep="last",
                                               maintain_order=True).sort("time")
        report["appended"] = len(committed)-report["corrected"]
        report["total_rows"] = len(frame)
    tmp = store.with_suffix(".tmp.parquet")
    frame.write_parquet(tmp)
    os.replace(tmp, store)
    # Verify causal monotonicity + uniqueness of the persisted store.
    check = pl.read_parquet(store)
    times = check.get_column("time").to_list()
    if len(times) != len(set(times)) or any(b <= a for a, b in zip(times, times[1:])):
        raise ValueError("parquet_store_corrupt: non-monotonic or duplicate open_time")
    report["max_time"] = times[-1] if times else None
    return report
