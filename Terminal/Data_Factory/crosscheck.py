"""Cross-source validation for the Zero-Cost Data Factory.

The factory's pillars are independent observations of the same market, which
makes them mutual oracles - a free, continuous data-quality system:

  * mid agreement       : Binance vs Coinbase vs Hyperliquid last trades
  * OI agreement        : Binance fapi openInterest vs Hyperliquid metaAndAssetCtxs
  * liquidation model   : synthetic ΔOI-cohort bands vs REAL Binance @forceOrder
                          prints (hit-rate calibration - did the realized fuel
                          land where the model said the density was?)
  * stop model parity   : optional side-by-side against a legacy vendor feed
                          (Api_Client.fetch_stops) when it is reachable; never
                          required, never blocking
  * freshness           : every pillar's data age vs its max age

Everything is deterministic given (factory state, recorded samples, now): the
report digest is a SHA-256 over canonical JSON, so a quality score is a sealed
fact the decision layer can gate on - never a fabricated statistic.
"""
from __future__ import annotations

import hashlib
import json
import math
import time
from dataclasses import dataclass, field

from Terminal.Risk_Sizing_Engine import number

BAND_BASE = 1.0025          # 25 bps geometric bands (same grid as the engine)


def band_index(price):
    return int(math.log(float(price)) / math.log(BAND_BASE))


@dataclass
class CrossCheckPolicy:
    mid_window_sec: float = 60.0        # last-trade age for venue comparison
    mid_warn_bps: float = 10.0
    mid_fail_bps: float = 50.0
    oi_window_sec: float = 1800.0      # two OI sources must overlap in time
    oi_max_disagreement: float = 0.35  # |a-b|/max(a,b)
    calibration_min_prints: int = 5
    calibration_min_usd: float = 250_000.0
    calibration_band_tolerance: int = 2   # a print within ±2 bands (±50 bps) of a
                                          # hot corridor counts as a hit: realized
                                          # prints scatter around modeled levels
    book_max_age: float = 30.0
    trade_max_age: float = 180.0
    oi_max_age: float = 1800.0
    parity_max_ratio: float = 3.0      # synthetic vs legacy vendor notional


@dataclass
class _OIRecord:
    ts: float
    oi_usd: float


class CrossSourceValidator:
    """Records multi-source samples and scores factory data quality."""

    def __init__(self, factory, policy=None, *, parity_stops=None, clock=time.time):
        self.factory = factory
        self.policy = policy or CrossCheckPolicy()
        self.parity_stops = parity_stops      # optional callable(coin)->{"bands": [...]}
        self.clock = clock
        self._oi = {}                          # (asset, source) -> [_OIRecord, ...]
        self.last_parity = {}

    # ------------------------------------------------------------ recorders
    def record_oi(self, asset, source, ts, oi_usd):
        """Record an OI sample from one venue for cross-source agreement."""
        rows = self._oi.setdefault((str(asset).upper(), str(source)), [])
        rows.append(_OIRecord(float(number(ts)), float(number(oi_usd))))
        del rows[:-8]
        return rows[-1]

    # ----------------------------------------------------------- comparisons
    def venue_prices(self, asset, now=None):
        """Last trade price per venue inside the comparison window."""
        now = float(number(now, self.clock()))
        out = {}
        for e in self.factory.bus.ticks(str(asset).upper(), limit=1024):
            if e.get("kind") == "LIQUIDATION":
                continue
            venue = e.get("venue")
            ts = number(e.get("ts"), 0.0)
            if not venue or ts <= 0 or now - ts > self.policy.mid_window_sec:
                continue
            if venue not in out or ts >= out[venue][0]:
                out[venue] = (ts, number(e.get("price"), 0.0))
        return {v: px for v, (ts, px) in out.items() if px > 0}

    def mid_divergence_bps(self, asset, now=None):
        """Max pairwise cross-venue divergence in bps (None if <2 venues)."""
        prices = self.venue_prices(asset, now)
        values = sorted(prices.values())
        if len(values) < 2:
            return None
        lo, hi = values[0], values[-1]
        return abs(hi - lo) / lo * 1e4 if lo > 0 else None

    def oi_agreement(self, asset, now=None):
        """Relative disagreement between the freshest OI samples per source."""
        now = float(number(now, self.clock()))
        latest = {}
        for (a, source), rows in self._oi.items():
            if a != str(asset).upper() or not rows:
                continue
            recent = [r for r in rows if 0.0 <= now - r.ts <= self.policy.oi_window_sec]
            if recent:
                latest[source] = recent[-1].oi_usd
        if len(latest) < 2:
            return None
        values = sorted(latest.values())
        lo, hi = values[0], values[-1]
        if hi <= 0:
            return None
        return {"sources": latest, "disagreement": abs(hi - lo) / hi,
                "pass": abs(hi - lo) / hi <= self.policy.oi_max_disagreement}

    def liquidation_calibration(self, asset, now=None):
        """Did realized @forceOrder fuel land in the bands the synthetic model
        ranked as hot? Returns a hit-rate, or ``available: False`` when the
        empirical sample is too thin to judge (the honest default)."""
        now = float(number(now, self.clock()))
        empirical = self.factory.liq.empirical_bands(str(asset).upper())
        realized_usd = sum(number(b.get("amount_usd"), 0.0) for b in empirical)
        prints = sum(int(number(b.get("count"), 0)) for b in empirical)
        if prints < self.policy.calibration_min_prints or realized_usd < self.policy.calibration_min_usd:
            return {"available": False, "prints": prints, "realized_usd": realized_usd}
        synthetic = self.factory.liq.reconstruct(str(asset).upper(), now=now).get("bands", [])
        amounts = sorted((number(b.get("amount_usd"), 0.0) for b in synthetic), reverse=True)
        if not amounts:
            return {"available": False, "prints": prints, "realized_usd": realized_usd}
        median = amounts[len(amounts) // 2]
        tolerance = int(self.policy.calibration_band_tolerance)
        hot = set()
        for b in synthetic:
            if number(b.get("mid_px"), 0) > 0 and number(b.get("amount_usd"), 0.0) >= median:
                center = band_index(number(b.get("mid_px"), 0.0))
                hot.update(range(center - tolerance, center + tolerance + 1))
        hit_usd = sum(number(b.get("amount_usd"), 0.0) for b in empirical
                      if band_index(number(b.get("mid_px"), 0.0)) in hot)
        return {"available": True, "prints": prints, "realized_usd": realized_usd,
                "hot_bands": len(hot), "hit_usd": hit_usd,
                "hit_rate": hit_usd / realized_usd if realized_usd > 0 else 0.0}

    def stop_model_parity(self, asset, legacy_stops=None):
        """Optional side-by-side of the synthetic stop model against a legacy
        vendor feed (Hyperdash via Api_Client). Informational, never blocking:
        recorded, not scored, because vendor availability is intermittent."""
        asset = str(asset).upper()
        source = legacy_stops
        if source is None and self.parity_stops is not None:
            try:
                source = self.parity_stops(asset)
            except Exception:                   # noqa: BLE001 - parity is best-effort
                source = None
        bands = (source or {}).get("bands") or []
        if not bands:
            self.last_parity[asset] = {"available": False}
            return self.last_parity[asset]
        legacy_usd = sum(number(b.get("amount_usd"), 0.0) for b in bands)
        mid = self.factory.bus.mid(asset) or 0.0
        synthetic = self.factory.stops.reconstruct(
            self.factory._bars.get(asset) or [], now=self.clock(), mid=mid,
            atr=self.factory._atr(asset)).get("bands", [])
        synth_usd = sum(number(b.get("amount_usd"), 0.0) for b in synthetic)
        ratio = (synth_usd / legacy_usd) if legacy_usd > 0 else None
        self.last_parity[asset] = {
            "available": True, "legacy_usd": legacy_usd, "synthetic_usd": synth_usd,
            "ratio": ratio,
            "pass": ratio is not None and 1.0 / self.policy.parity_max_ratio <= ratio
                    <= self.policy.parity_max_ratio}
        return self.last_parity[asset]

    def freshness(self, asset, now=None):
        """Age of every pillar's data vs its max age."""
        now = float(number(now, self.clock()))
        asset = str(asset).upper()
        book = self.factory.bus.book(asset) or {}
        book_ts = number(book.get("ts"), 0.0)
        trade_age = None
        for e in self.factory.bus.ticks(asset, limit=64):
            if e.get("kind") != "LIQUIDATION":
                trade_age = now - number(e.get("ts"), 0.0)
                break
        oi_age = None
        for (a, _source), rows in self._oi.items():
            if a == asset and rows:
                oi_age = now - rows[-1].ts if oi_age is None else min(oi_age, now - rows[-1].ts)
        checks = {"book": {"age": now - book_ts if book_ts > 0 else None,
                           "pass": book_ts > 0 and now - book_ts <= self.policy.book_max_age},
                  "trades": {"age": trade_age,
                             "pass": trade_age is not None and trade_age <= self.policy.trade_max_age},
                  "oi": {"age": oi_age,
                         "pass": oi_age is not None and oi_age <= self.policy.oi_max_age,
                         "available": oi_age is not None}}
        return checks

    # ---------------------------------------------------------------- report
    def quality_report(self, assets, now=None):
        """Deterministic per-asset quality score in [0, 1] + SHA-256 digest.

        Scoring: required freshness checks (book .35, trades .25, OI .15 when
        recorded), cross-venue mid agreement .25 (warn scores half). Checks
        with no data at all are excluded and the weight renormalizes - EXCEPT
        book and trades, which are mandatory and fail closed."""
        now = float(number(now, self.clock()))
        report = {"as_of": now, "assets": {}, "policy": "omni.crosscheck.v1"}
        for asset in assets:
            asset = str(asset).upper()
            weighted, total = 0.0, 0.0
            checks = self.freshness(asset, now)
            for name, weight, mandatory in (("book", 0.35, True), ("trades", 0.25, True),
                                            ("oi", 0.15, False)):
                check = checks[name]
                if not mandatory and not check["available"]:
                    continue                      # no OI source ever connected: skip
                weighted += weight * (1.0 if check["pass"] else 0.0)
                total += weight
            divergence = self.mid_divergence_bps(asset, now)
            if divergence is not None:
                score = 1.0 if divergence <= self.policy.mid_warn_bps else (
                    0.5 if divergence <= self.policy.mid_fail_bps else 0.0)
                weighted += 0.25 * score
                total += 0.25
            score = weighted / total if total > 0 else 0.0
            report["assets"][asset] = {
                "quality_score": round(score, 6),
                "freshness": checks,
                "mid_divergence_bps": divergence,
                "oi_agreement": self.oi_agreement(asset, now),
                "liquidation_calibration": self.liquidation_calibration(asset, now),
                "stop_model_parity": self.last_parity.get(asset, {"available": False}),
                "monotonic_violations": self.factory.bus.monotonic_violations(asset)}
        scored = [a["quality_score"] for a in report["assets"].values()]
        report["quality_score"] = round(sum(scored) / len(scored), 6) if scored else 0.0
        report["digest"] = hashlib.sha256(
            json.dumps(report, sort_keys=True, separators=(",", ":"), default=str)
            .encode("utf-8")).hexdigest()
        return report
