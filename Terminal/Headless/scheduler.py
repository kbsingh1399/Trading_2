"""15-minute candle-boundary scheduler with sub-second drift compensation.

The execution window is minute :14 of every 15-minute candle (the trader's
own gate: ``840 + cadence_second <= elapsed < 898``). The scheduler wakes at
``HH:14:30, HH:29:30, HH:44:30, HH:59:30`` UTC - second 30 of minute 14 by
default, matching ``cadence_second=30``.

Drift compensation: the sleep target is always recomputed from the WALL clock
(never accumulated), in two phases - a coarse sleep to T-0.5s, then a fine
loop in <=50ms increments. A system suspend that skips past the deadline
fires the missed wake exactly once and resynchronizes to the next boundary.
"""
from __future__ import annotations

import asyncio
import time
from typing import Awaitable, Callable, Optional

EVAL_MINUTE = 14          # minute-of-candle the decision window opens
SLOT_SECONDS = 900.0
COARSE_MARGIN = 0.5       # switch to fine sleeping half a second out
FINE_STEP = 0.05


class CandleScheduler:
    """Deterministic boundary clock; injectable clock/sleep for tests."""

    def __init__(self, *, cadence_second: float = 30.0, clock: Callable = time.time,
                 sleep: Callable[[float], Awaitable] = asyncio.sleep):
        self.cadence_second = float(cadence_second)
        self.clock = clock
        self._sleep = sleep
        self.cycles = 0

    def next_deadline(self, now: Optional[float] = None) -> float:
        """The next HH:{14,29,44,59}:{cadence} UTC boundary strictly after now."""
        now = float(self.clock() if now is None else now)
        slot = int(now // SLOT_SECONDS) * SLOT_SECONDS
        candidate = slot + EVAL_MINUTE * 60.0 + self.cadence_second
        while candidate <= now:
            candidate += SLOT_SECONDS
        return candidate

    def seconds_until(self, now: Optional[float] = None) -> float:
        now = float(self.clock() if now is None else now)
        return max(0.0, self.next_deadline(now) - now)

    async def run(self, on_wake: Callable[[float], None], *,
                  stop_event: Optional[asyncio.Event] = None,
                  max_cycles: Optional[int] = None,
                  on_wake_async: Optional[Callable[[float], Awaitable]] = None):
        """Wake ``on_wake(deadline)`` at every boundary until stopped."""
        while True:
            if stop_event is not None and stop_event.is_set():
                return
            if max_cycles is not None and self.cycles >= max_cycles:
                return
            target = self.next_deadline()
            remaining = target - self.clock()
            while remaining > 0:
                if stop_event is not None and stop_event.is_set():
                    return
                step = remaining - COARSE_MARGIN if remaining > COARSE_MARGIN + FINE_STEP \
                    else min(FINE_STEP, remaining)
                if step > 0:
                    await self._sleep(step)
                remaining = target - self.clock()   # recompute: never accumulate drift
            self.cycles += 1
            if on_wake_async is not None:
                await on_wake_async(target)
            else:
                on_wake(target)
