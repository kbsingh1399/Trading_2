"""Pioneer Decision Engine — deterministic conviction fusion over the
Zero-Cost Data Factory (consultation 4).

The existing decision architecture is preserved exactly: OrderflowModel
features + confluence gates propose, RiskPolicy sizes, the governor and the
4,775 floor protect. The Pioneer layer ADDS the data points no vendor was
feeding the book before:

  signal          source (all $0, all live)                     weight
  --------------- ------------------------------------------------ ------
  orderflow       bus CVD 1m/5m/15m + 15m taker imbalance        0.30
  cascade         synthetic liquidation fuel asymmetry around mid 0.25
  stops           structural stop-cluster asymmetry (magnet)      0.15
  whales          sampled HL cohort positioning + on-chain flows  0.15
  macro           ETF net flows + Coinbase premium + F&G extremes 0.15

Contract guarantees (mirrors every standing invariant):

  * DETERMINISTIC  - same inputs -> same vector, same SHA-256 chained digest;
                     nothing is fabricated, every number carries its basis.
  * ADVISORY/VETO  - the trader hook only vetoes NEW entries (quality floor,
                     stale book, blackout, opposed conviction). It never
                     sizes, never forces, never touches an open position or
                     an exit. Sizing stays 10-45 USD behind the floor.
  * FRICTION       - every advisory carries min_favorable_move_bps =
                     41 bps round-trip + live spread + slip buffer; a
                     conviction that cannot pay its own friction is noise.
  * FAIL-CLOSED    - missing data degrades a signal to "unavailable"
                     (weight renormalizes); missing quality -> no quality
                     discount but the staleness gates still fire.
"""
from __future__ import annotations

import hashlib
import json
import math
import time
from dataclasses import dataclass, field

from Terminal.Risk_Sizing_Engine import number

POLICY_VERSION = "omni.pioneer.v1"


def _clamp(x, lo=-1.0, hi=1.0):
    return max(lo, min(hi, float(x)))


def _sign(x):
    x = float(number(x, 0.0))
    return 0.0 if abs(x) < 1e-12 else math.copysign(1.0, x)


@dataclass
class PioneerPolicy:
    friction_bps: float = 41.0            # mandatory round-trip friction
    slip_buffer_bps: float = 5.0          # conservative extra slip allowance
    conviction_threshold: float = 0.25    # |conviction| needed to opine
    min_quality: float = 0.60             # cross-source quality floor to trade
    max_book_age: float = 30.0            # book staleness gate (fail closed)
    weights: dict = field(default_factory=lambda: {
        "orderflow": 0.30, "cascade": 0.25, "stops": 0.15, "whale": 0.15, "macro": 0.15})
    cascade_reach: float = 0.05           # fuel within 5% of mid counts fully
    cascade_scale_usd: float = 5.0e6      # tanh scale for fuel asymmetry
    whale_scale_usd: float = 2.0e6        # tanh scale for whale pressure
    etf_scale_musd: float = 500.0         # tanh scale for daily ETF net flow
    premium_scale_bps: float = 10.0       # tanh scale for Coinbase premium
    fng_extreme: float = 25.0            # |F&G - 50| beyond this = contrarian
    version: str = POLICY_VERSION


class PioneerDecisionEngine:
    """Cross-validated conviction layer over the zero-cost data factory."""

    def __init__(self, policy=None, *, quality_provider=None, clock=time.time):
        self.policy = policy or PioneerPolicy()
        self.quality_provider = quality_provider        # callable(asset) -> report dict
        self.clock = clock
        self._chain = {}                                # asset -> previous digest
        self.last = {}

    # ------------------------------------------------------------- analytics
    def _signal_orderflow(self, payload):
        of = payload.get("orderflow") or {}
        buy = number(of.get("taker_buy_usd_15m"), 0.0)
        sell = number(of.get("taker_sell_usd_15m"), 0.0)
        if buy + sell <= 0:
            return None, {"available": False, "reason": "no_tape"}
        ratio = _clamp(number(of.get("taker_ratio_15m"), 0.0))
        windows, weights = [], []
        for key, weight in (("cvd_1m", 0.2), ("cvd_5m", 0.3), ("cvd_15m", 0.5)):
            cvd = of.get(key)
            if cvd is None:
                continue
            windows.append(_sign(cvd) * _clamp(abs(number(cvd, 0.0)) /
                                              max(buy + sell, 1e-9)))
            weights.append(weight)
        agreement = (sum(w * v for w, v in zip(weights, windows)) / sum(weights)) \
            if weights else 0.0
        value = _clamp(0.5 * ratio + 0.5 * agreement)
        return value, {"available": True, "taker_ratio_15m": ratio,
                       "cvd_window_signs": [round(v, 6) for v in windows],
                       "tape_usd_15m": buy + sell}

    def _signal_cascade(self, payload, mid):
        bands = (payload.get("projected_liquidations") or {}).get("bands") or []
        if not bands or mid <= 0:
            return None, {"available": False, "reason": "no_liquidation_model"}
        reach = math.log(1.0 + self.policy.cascade_reach)
        long_fuel = short_fuel = 0.0
        for band in bands:
            px = number(band.get("mid_px"), 0.0)
            usd = number(band.get("amount_usd"), 0.0)
            side = str(band.get("position_side_at_risk", "")).upper()
            if px <= 0 or usd <= 0:
                continue
            proximity = max(0.0, 1.0 - abs(math.log(px / mid)) / reach) if reach > 0 else 1.0
            if side == "LONG" and px < mid:          # longs liquidated below
                long_fuel += usd * proximity
            elif side == "SHORT" and px > mid:       # shorts liquidated above
                short_fuel += usd * proximity
        if long_fuel + short_fuel <= 0:
            return None, {"available": False, "reason": "no_fuel_within_reach"}
        net = short_fuel - long_fuel                 # upside squeeze fuel minus downside
        value = math.tanh(net / self.policy.cascade_scale_usd)
        return value, {"available": True, "long_fuel_usd": long_fuel,
                       "short_fuel_usd": short_fuel, "reach": self.policy.cascade_reach}

    def _signal_stops(self, payload, mid):
        bands = (payload.get("observed_stops") or {}).get("bands") or []
        sell_usd = buy_usd = 0.0
        for band in bands:
            usd = number(band.get("amount_usd"), 0.0)
            side = str(band.get("position_side_at_risk", "")).upper()
            px = number(band.get("mid_px"), 0.0)
            if side == "LONG" and px < mid:          # longs' sell stops below
                sell_usd += usd
            elif side == "SHORT" and px > mid:       # shorts' buy stops above
                buy_usd += usd
        total = sell_usd + buy_usd
        if total <= 0:
            return None, {"available": False, "reason": "no_stop_clusters"}
        # The heavier pool is the magnet: sell stops below attract price down.
        value = _clamp(-(sell_usd - buy_usd) / total)
        return value, {"available": True, "sell_stop_usd": sell_usd,
                       "buy_stop_usd": buy_usd}

    def _signal_whale(self, payload):
        positions = payload.get("whale_positions") or []
        pos_net = sum(_sign(p.get("size")) * number(p.get("notional_usd"), 0.0)
                      for p in positions if number(p.get("notional_usd"), 0.0) > 0)
        flow = number(payload.get("whale_net_flow_usd_24h"), 0.0)
        if not positions and flow == 0:
            return None, {"available": False, "reason": "no_whale_data"}
        value = math.tanh((0.6 * pos_net + 0.4 * flow) / self.policy.whale_scale_usd)
        return value, {"available": True, "cohort_positions": len(positions),
                       "position_net_usd": pos_net, "net_flow_usd_24h": flow}

    def _signal_macro(self, macro):
        source = macro or {}
        if not source.get("etf_net_flow_musd_1d") and not source.get("coinbase_premium_bps") \
                and not (source.get("fear_greed") or {}).get("value"):
            source = source.get("data_factory") or {}   # Market_Intelligence report shape
        etf = number(source.get("etf_net_flow_musd_1d"), 0.0)
        premium = number(source.get("coinbase_premium_bps"), 0.0)
        fng = number((source.get("fear_greed") or {}).get("value"), 0.0)
        if etf == 0 and premium == 0 and fng == 0:
            return None, {"available": False, "reason": "no_macro_data"}
        s_etf = math.tanh(etf / self.policy.etf_scale_musd) if etf else 0.0
        s_prem = math.tanh(premium / self.policy.premium_scale_bps) if premium else 0.0
        s_fng = 0.0
        if fng and abs(fng - 50.0) > self.policy.fng_extreme:
            s_fng = _clamp((50.0 - fng) / 50.0)      # contrarian at the extremes
        value = _clamp(0.4 * s_etf + 0.4 * s_prem + 0.2 * s_fng)
        return value, {"available": True, "etf_net_flow_musd_1d": etf,
                       "coinbase_premium_bps": premium, "fear_greed": fng,
                       "components": {"etf": round(s_etf, 6), "premium": round(s_prem, 6),
                                      "fear_greed_contra": round(s_fng, 6)}}

    # ------------------------------------------------------------- lifecycle
    def evaluate(self, asset, payload, features, macro=None, now=None):
        """Deterministic advisory for one asset. Never raises on data gaps."""
        asset = str(asset).upper()
        now = float(number(now, self.clock()))
        policy = self.policy
        advisory = {"asset": asset, "as_of": now, "policy_version": policy.version,
                    "signals": {}, "conviction": 0.0, "advice": "NEUTRAL",
                    "tradeable": False, "reason": "", "quality_score": None}

        # ---- fail-closed gates -------------------------------------------------
        mid = number(payload.get("price"), 0.0)
        book_as_of = number((features or {}).get("book_as_of"), 0.0)
        if mid <= 0:
            advisory["reason"] = "no_mid"
            return self._finalize(advisory, payload)
        if book_as_of <= 0 or not 0.0 <= now - book_as_of <= policy.max_book_age:
            advisory["reason"] = "book_stale"
            return self._finalize(advisory, payload)
        if macro and macro.get("blackout_active"):
            advisory["reason"] = "macro_blackout"
            return self._finalize(advisory, payload)
        quality = None
        if self.quality_provider is not None:
            try:
                quality = self.quality_provider(asset)
            except Exception:                       # noqa: BLE001 - quality is advisory
                quality = None
            score = number((quality or {}).get("quality_score"), -1.0)
            advisory["quality_score"] = score if score >= 0 else None
            if score >= 0 and score < policy.min_quality:
                advisory["reason"] = f"quality_below_floor:{score:.3f}"
                return self._finalize(advisory, payload)

        # ---- signals -----------------------------------------------------------
        evaluators = {"orderflow": lambda: self._signal_orderflow(payload),
                      "cascade": lambda: self._signal_cascade(payload, mid),
                      "stops": lambda: self._signal_stops(payload, mid),
                      "whale": lambda: self._signal_whale(payload),
                      "macro": lambda: self._signal_macro(macro)}
        raw, weight_total = 0.0, 0.0
        for name, evaluate_one in evaluators.items():
            value, basis = evaluate_one()
            advisory["signals"][name] = {"value": None if value is None else round(value, 6),
                                         **basis}
            if value is not None:
                raw += policy.weights[name] * value
                weight_total += policy.weights[name]
        conviction = raw / weight_total if weight_total > 0 else 0.0
        if advisory["quality_score"] is not None:    # live quality discount
            conviction *= max(0.0, min(1.0, advisory["quality_score"]))
        conviction = _clamp(conviction)
        advisory["conviction"] = round(conviction, 6)
        advisory["advice"] = ("SUPPORT_LONG" if conviction >= policy.conviction_threshold
                              else "SUPPORT_SHORT" if conviction <= -policy.conviction_threshold
                              else "NEUTRAL")

        # ---- friction floor ----------------------------------------------------
        spread_bps = number((payload.get("orderflow") or {}).get("spread_bps"), 0.0)
        advisory["min_favorable_move_bps"] = round(
            policy.friction_bps + policy.slip_buffer_bps + max(0.0, spread_bps), 3)

        # ---- tradeability: veto-only power --------------------------------------
        direction = (features or {}).get("direction")
        aligned = advisory["advice"] in ("NEUTRAL", f"SUPPORT_{direction}") if direction \
            else advisory["advice"] == "NEUTRAL"
        advisory["tradeable"] = bool(aligned)
        advisory["reason"] = "" if aligned else f"opposed_conviction:{advisory['advice']}_vs_{direction}"
        return self._finalize(advisory, payload)

    def _finalize(self, advisory, payload):
        """SHA-256 chain the advisory (tamper-evident, deterministic)."""
        core = {k: v for k, v in advisory.items() if k != "digest"}
        prev = self._chain.get(advisory["asset"], "genesis")
        digest = hashlib.sha256(
            (prev + "|" + json.dumps(core, sort_keys=True, separators=(",", ":"), default=str))
            .encode("utf-8")).hexdigest()
        advisory["digest"] = digest
        self._chain[advisory["asset"]] = digest
        self.last[advisory["asset"]] = advisory
        return advisory
