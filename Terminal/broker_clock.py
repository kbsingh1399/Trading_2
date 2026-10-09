"""Bounded broker/host clock calibration after broker timezone normalization."""
from __future__ import annotations

import math
import time
import threading


class BrokerClock:
    """Confirm clock skew with advancing ticks; repeated ticks retain their age.

    Timestamps passed here must already be UTC. Broker timezone offsets are
    deliberately not estimated by this clock. Calibration is process-local.
    """

    def __init__(self, max_offset_seconds=60.0, progression_tolerance_seconds=2.0):
        self.max_offset_seconds = float(max_offset_seconds)
        self.progression_tolerance_seconds = float(progression_tolerance_seconds)
        self.offset_seconds = None
        self.status = "UNVERIFIED"
        self._ticks = {}
        self._anchor = None
        self._lock = threading.RLock()

    def utc_now(self, *, now=None, monotonic_now=None):
        with self._lock:
            return self._utc_now(now=now, monotonic_now=monotonic_now)

    def _utc_now(self, *, now=None, monotonic_now=None):
        if self._anchor is None:
            return None
        mono = time.monotonic() if monotonic_now is None else float(monotonic_now)
        elapsed = mono - self._anchor[1]
        if not math.isfinite(elapsed) or elapsed < 0:
            return None
        trusted = self._anchor[0] + elapsed
        # Explicit monotonic-only calls support deterministic clock tests.
        wall = (time.time() if monotonic_now is None else None) if now is None else float(now)
        if wall is not None:
            if not math.isfinite(wall) or abs(trusted - wall) > self.max_offset_seconds:
                self.status = "OFFSET_OUT_OF_BOUNDS"
                return None
            self.offset_seconds = trusted - wall
        self.status = "CALIBRATED"
        return trusted

    def tick_age_seconds(self, normalized_tick_msc, *, symbol, now=None, monotonic_now=None):
        with self._lock:
            return self._tick_age_seconds(normalized_tick_msc, symbol=symbol,
                                          now=now, monotonic_now=monotonic_now)

    def _tick_age_seconds(self, normalized_tick_msc, *, symbol, now=None, monotonic_now=None):
        wall = time.time() if now is None else float(now)
        mono = time.monotonic() if monotonic_now is None else float(monotonic_now)
        try:
            stamp = float(normalized_tick_msc) / 1000.0
        except (TypeError, ValueError):
            stamp = 0.0
        if not all(math.isfinite(v) for v in (stamp, wall, mono)) or stamp <= 0:
            if self._anchor is None:
                self.status = "INVALID_TICK"
            return None
        previous = self._ticks.get(symbol)
        if previous and stamp < previous[0]:
            if self._anchor is None:
                self.status = "REGRESSING_TICK"
            return None
        if previous and stamp == previous[0]:
            # In particular, never move the UTC anchor to this receipt time.
            if self._anchor is None or previous[2] is None:
                return None
            trusted = self.utc_now(now=wall, monotonic_now=mono)
            return max(0.0, trusted - stamp) if trusted is not None else None

        trusted_before = self.utc_now(now=wall, monotonic_now=mono)
        if abs(stamp - wall) > self.max_offset_seconds and (trusted_before is None or stamp > trusted_before):
            if self._anchor is None:
                self.status = "OFFSET_OUT_OF_BOUNDS"
            return None

        if self._anchor is None:
            self._ticks[symbol] = (stamp, mono, None)
            if previous is None:
                self.status = "UNVERIFIED"
                return None
            elapsed = mono - previous[1]
            if elapsed <= 0 or abs(stamp - previous[0] - elapsed) > self.progression_tolerance_seconds:
                self.status = "UNVERIFIED"
                return None
            self._anchor = (stamp, mono)
            self.status = "CALIBRATED"
        trusted_now = self.utc_now(now=wall, monotonic_now=mono)
        if trusted_now is None:
            return None
        future = stamp - trusted_now
        if future > self.progression_tolerance_seconds:
            self._ticks[symbol] = (stamp, mono, None)
            return None
        # Advancing ticks may improve the transport-delay upper envelope.
        # An older/delayed tick can never move the clock backwards.
        if future > 0:
            self._anchor = (stamp, mono)
            trusted_now = stamp
        age = max(0.0, trusted_now - stamp)
        self.offset_seconds = trusted_now - wall
        if abs(self.offset_seconds) > self.max_offset_seconds:
            self.status = "OFFSET_OUT_OF_BOUNDS"
            return None
        self._ticks[symbol] = (stamp, mono, age)
        return age
