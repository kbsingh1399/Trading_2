"""Real-time continuous operation for the Zero-Cost Data Factory.

``RealtimeRunner`` is the production heartbeat that keeps EVERY data point
continuously updating:

  * venue websockets  : delegated to ``factory.run`` (reconnect/backoff built in)
  * open interest     : polled from every configured source; the primary feeds
                        the ΔOI cohort model, all sources feed the cross-source
                        validator (Binance vs Hyperliquid agreement)
  * whale cohort      : Hyperliquid public /info sampling of tracked addresses
                        (clearinghouseState liquidationPx + frontendOpenOrders
                        trigger stops - exact, keyless, $0)
  * bars              : completed 15m bars for the stop-cluster structural model
  * macro             : Fear & Greed hourly, Farside ETF flows every 6h
  * watchdog          : cross-source quality report every 30s; pillar ages,
                        stall streaks and the sealed quality digest are exposed
                        via ``status()`` for the decision layer

Every cadence is jittered (thundering-herd avoidance), every loop is
failure-isolated (one dead poller never stops the others), and everything is
driven by an injectable clock + sleep so the offline test suite runs the full
schedule deterministically in microseconds - no real waiting, no network.
"""
from __future__ import annotations

import asyncio
import random
import time
from dataclasses import dataclass, field

from Terminal.Risk_Sizing_Engine import number


@dataclass
class LivePolicy:
    oi_interval: float = 300.0          # Binance fapi / HL meta cadence
    whale_interval: float = 60.0        # HL /info cohort sampling (rate-limit safe)
    bar_interval: float = 900.0         # completed 15m bars
    fng_interval: float = 3600.0        # alternative.me
    etf_interval: float = 21600.0       # Farside (daily data, 6h poll catches it)
    watchdog_interval: float = 30.0     # cross-source quality report
    jitter_fraction: float = 0.10       # ±10% cadence jitter
    stall_strikes: int = 3              # watchdog ticks with zero flow => stale


class RealtimeRunner:
    """Owns the continuous refresh schedule around a ZeroCostDataFactory."""

    def __init__(self, factory, validator=None, *, transports=None,
                 oi_pollers=None, whale_sampler=None, bar_provider=None,
                 policy=None, clock=time.time, sleep=asyncio.sleep):
        self.factory = factory
        self.validator = validator
        self.transports = transports or {}
        self.oi_pollers = dict(oi_pollers or {})
        self.whale_sampler = whale_sampler
        self.bar_provider = bar_provider
        self.policy = policy or LivePolicy()
        self.clock = clock
        self._sleep = sleep
        self._rng = random.Random()
        self._stop = None
        self._deadline = None
        self.last_quality = None
        self.quality_history = []
        self.stats = {"oi_polls": 0, "oi_errors": 0, "whale_polls": 0,
                      "whale_errors": 0, "bar_refreshes": 0, "fng_refreshes": 0,
                      "etf_refreshes": 0, "watchdog_ticks": 0}
        self.status_ = {"pillars": {}, "streaks": {}}

    # ------------------------------------------------------------- utilities
    def _interval(self, base):
        jitter = self.policy.jitter_fraction
        return base * (1.0 + self._rng.uniform(-jitter, jitter)) if jitter > 0 else base

    async def _call(self, fn, *args):
        result = fn(*args)
        if asyncio.iscoroutine(result):
            result = await result
        return result

    def _mark(self, pillar, ok, detail=None):
        pillar_state = self.status_["pillars"].setdefault(
            pillar, {"last_success": -1.0, "last_attempt": -1.0, "healthy": False})
        pillar_state["last_attempt"] = self.clock()
        if ok:
            pillar_state["last_success"] = self.clock()
            pillar_state["healthy"] = True
            self.status_["streaks"][pillar] = 0
        else:
            self.status_["streaks"][pillar] = self.status_["streaks"].get(pillar, 0) + 1
            if self.status_["streaks"][pillar] >= self.policy.stall_strikes:
                pillar_state["healthy"] = False
        if detail is not None:
            pillar_state["detail"] = detail

    def _stopped(self):
        if self._stop is not None and self._stop.is_set():
            return True
        return self._deadline is not None and self.clock() >= self._deadline

    # ----------------------------------------------------------------- loops
    async def run(self, assets=None, stop_event=None, max_seconds=None):
        """Run every refresh loop until ``stop_event`` (or ``.stop()``) fires.

        ``max_seconds`` optionally bounds the runtime (wall/fake clock): a
        scheduled shutdown that does not rely on the caller racing to set the
        event - used in production for controlled restarts and in tests for
        deterministic, hang-free schedules."""
        assets = [str(a).upper() for a in (assets or self.factory.assets)]
        self._stop = stop_event if stop_event is not None else asyncio.Event()
        self._deadline = (self.clock() + float(max_seconds)) if max_seconds else None
        tasks = []
        if self.transports:
            tasks.append(self.factory.run(assets=assets, transports=self.transports))
        tasks.extend([self._oi_loop(assets), self._whale_loop(assets),
                      self._bar_loop(assets), self._macro_loop(),
                      self._watchdog_loop(assets)])
        await asyncio.gather(*tasks)

    def stop(self):
        if self._stop is not None:
            self._stop.set()

    async def _oi_loop(self, assets):
        primary = next(iter(self.oi_pollers), None)
        while not self._stopped():
            ok_any = False
            for source, poller in self.oi_pollers.items():
                for asset in assets:
                    try:
                        sample = await self._call(poller, asset)
                        if not sample:
                            continue
                        price = float(number(sample.get("price"), 0.0))
                        oi_usd = float(number(sample.get("oi_contracts"), 0.0)) \
                            * float(number(sample.get("contract_size"), 1.0)) * price
                        if self.validator is not None:
                            self.validator.record_oi(asset, source, sample.get("ts"), oi_usd)
                        if source == primary:
                            self.factory.ingest_oi(asset, **sample)
                        ok_any = True
                        self.stats["oi_polls"] += 1
                    except Exception:             # noqa: BLE001 - poller isolation
                        self.stats["oi_errors"] += 1
            self._mark("oi", ok_any)
            await self._sleep(self._interval(self.policy.oi_interval))

    async def _whale_loop(self, assets):
        while not self._stopped():
            ok_any = False
            if self.whale_sampler is not None:
                for asset in assets:
                    try:
                        positions = await self._call(self.whale_sampler, asset)
                        if positions:
                            self.factory.ingest_whale_positions(asset, positions)
                            ok_any = True
                        self.stats["whale_polls"] += 1
                    except Exception:             # noqa: BLE001 - sampler isolation
                        self.stats["whale_errors"] += 1
            self._mark("whales", ok_any)
            await self._sleep(self._interval(self.policy.whale_interval))

    async def _bar_loop(self, assets):
        while not self._stopped():
            ok_any = False
            if self.bar_provider is not None:
                for asset in assets:
                    try:
                        bars = await self._call(self.bar_provider, asset)
                        if self.factory.ingest_bars(asset, bars):
                            ok_any = True
                    except Exception:             # noqa: BLE001 - provider isolation
                        pass
                if ok_any:
                    self.stats["bar_refreshes"] += 1
            self._mark("bars", ok_any)
            await self._sleep(self._interval(self.policy.bar_interval))

    async def _macro_loop(self):
        next_etf = 0.0
        while not self._stopped():
            try:
                if self.factory.fng.value() is not None:
                    self.stats["fng_refreshes"] += 1
                    self._mark("fng", True)
                else:
                    self._mark("fng", False)
            except Exception:                     # noqa: BLE001 - macro isolation
                self._mark("fng", False)
            if self.clock() >= next_etf:
                for asset in ("BTC", "ETH"):
                    try:
                        rows = self.factory.farside.refresh(asset)
                        self._mark("etf", bool(rows), {"rows": len(rows) if rows else 0})
                        if rows:
                            self.stats["etf_refreshes"] += 1
                    except Exception:             # noqa: BLE001 - macro isolation
                        self._mark("etf", False)
                next_etf = self.clock() + self.policy.etf_interval
            await self._sleep(self._interval(self.policy.fng_interval))

    async def _watchdog_loop(self, assets):
        while not self._stopped():
            try:
                if self.validator is not None:
                    self.last_quality = self.validator.quality_report(assets, self.clock())
                    self.quality_history.append(self.last_quality)
                    del self.quality_history[:-64]
                flow = self.factory.stats.get("trades", 0) + self.factory.stats.get("books", 0)
                self._mark("streams", flow > self.status_.get("last_flow", -1),
                           {"events": flow})
                self.status_["last_flow"] = flow
                self.stats["watchdog_ticks"] += 1
            except Exception:                     # noqa: BLE001 - watchdog isolation
                pass
            await self._sleep(self._interval(self.policy.watchdog_interval))

    # ---------------------------------------------------------------- status
    def status(self):
        """Pillar health snapshot for monitoring and the decision layer."""
        now = self.clock()
        pillars = {}
        for name, state in self.status_["pillars"].items():
            pillars[name] = {**state,
                             "age_since_success": (now - state["last_success"])
                             if state["last_success"] > 0 else None}
        return {"as_of": now, "pillars": pillars,
                "stall_streaks": dict(self.status_["streaks"]),
                "stats": dict(self.stats),
                "quality": (self.last_quality or {}).get("quality_score"),
                "quality_digest": (self.last_quality or {}).get("digest")}
