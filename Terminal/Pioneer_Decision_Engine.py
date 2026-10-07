"""Pioneer Decision Engine — deterministic conviction fusion over the
Zero-Cost Data Factory (consultation 4).

The existing decision architecture is preserved exactly: OrderflowModel
features + confluence gates propose, RiskPolicy sizes, the governor and the
4,775 floor protect. The Pioneer layer ADDS the data points no vendor was
feeding the book before:

  signal          source (all $0, all live)                     weight
  --------------- ------------------------------------------------ ------
  orderflow       bus CVD 1m/5m/15m + 15m taker imbalance        0.30
  cascade         unavailable without observed resting exposure       0.25
  stops           sampled exchange-reported stop trigger orders       0.15
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

from Terminal.Telemetry_Provenance import verified_wallet_block, verified_wallet_l3
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
        # Reported wallet liquidation prices are projections, not forced
        # executions or complete resting exposure: never count as cascade fuel.
        return None, {"available": False, "reason": "no_observed_resting_liquidations"}

    def _signal_stops(self, payload, mid):
        bands = (verified_wallet_block(payload, "observed_stops", self.clock()) or {}).get("bands") or []
        sell_usd = buy_usd = 0.0
        for band in bands:
            usd = number(band.get("amount_usd"), 0.0)
            side = str(band.get("position_side_at_risk", "")).upper()
            px = number(band.get("mid_px"), 0.0)
            if px <= 0 or usd <= 0:
                continue
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
        # Only a fresh public clearinghouseState sample is wallet-attributed.
        # Arbitrary injected whale_positions and unattributed on-chain flow
        # cannot add conviction to a live order.
        block = verified_wallet_block(payload, "observed_stops", self.clock())
        wallets = set(block.get("wallets") or []) if block else set()
        positions = [p for p in (payload.get("whale_positions") or [])
                     if p.get("address") in wallets]
        pos_net = sum(_sign(p.get("size")) * number(p.get("notional_usd"), 0.0)
                      for p in positions if number(p.get("notional_usd"), 0.0) > 0)
        flow = 0.0  # no independently attested on-chain provider in this payload
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
    def _evaluators(self, payload, mid, macro):
        """Signal evaluators for evaluate(). The v2 decision chain
        (DecisionChainEngine) extends this hook with the wall-persistence
        and cross-source-consistency pillars; v1 behavior is identical."""
        return {"orderflow": lambda: self._signal_orderflow(payload),
                "cascade": lambda: self._signal_cascade(payload, mid),
                "stops": lambda: self._signal_stops(payload, mid),
                "whale": lambda: self._signal_whale(payload),
                "macro": lambda: self._signal_macro(macro)}

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
        evaluators = self._evaluators(payload, mid, macro)
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


# ===========================================================================
# omni.decision_chain.v2 (OX_ALPHA_63): the 6 Factory pillars fused.
#
#   pillar                          signal            source module
#   ------------------------------  ----------------  ------------------------
#   P1 reconstructed liquidations   cascade           liquidation_engine.py
#   P2A structural stop clusters    stops             liquidation_engine.py
#   P2B whale-wall persistence      walls   (NEW)     factory.py _WallTracker
#   P3 on-chain whale flows         whale             onchain.py / factory.py
#   P4 Farside ETF flows            macro             macro.py
#   P5 F&G + Coinbase premium       macro             macro.py
#   P6 cross-source consistency     consistency (NEW) crosscheck.py
#
# The chain is a strict superset of the v1 Pioneer layer: every v1 signal,
# gate, digest rule and invariant is preserved verbatim; v2 ADDS two signals
# (persistent resting walls, cross-venue consensus divergence), attaches the
# CrossSourceValidator block to the payload, and stamps a 6-pillar
# availability manifest into every advisory (inside the SHA-256 digest).
# ===========================================================================
DECISION_CHAIN_VERSION = "omni.decision_chain.v2"


@dataclass
class DecisionChainPolicy(PioneerPolicy):
    """v2 weights + the two new pillar calibrations (sum = 1.00; unavailable
    pillars renormalize exactly like v1)."""

    weights: dict = field(default_factory=lambda: {
        "orderflow": 0.24, "cascade": 0.20, "stops": 0.08, "whale": 0.08,
        "walls": 0.16, "macro": 0.16, "consistency": 0.08})
    wall_reach: float = 0.015            # walls within 1.5% of mid count fully
    wall_scale_usd: float = 5.0e6        # tanh scale for wall asymmetry
    wall_min_persistence_sec: float = 180.0   # >= 3 min resting (anti-spoof)
    consistency_scale_bps: float = 10.0  # tanh scale for consensus gap
    consistency_min_venues: int = 2      # fail closed below this
    version: str = DECISION_CHAIN_VERSION


class DecisionChainEngine(PioneerDecisionEngine):
    """The 6-pillar decision chain (omni.decision_chain.v2).

    Drop-in for the v1 engine wherever ``attach_pioneer`` is used: the
    ``evaluate`` signature and the advisory contract are unchanged, so the
    Omni_Trader veto hook keeps working with zero modifications.
    """

    def __init__(self, policy=None, *, quality_provider=None, validator=None,
                 clock=time.time):
        super().__init__(policy or DecisionChainPolicy(),
                         quality_provider=quality_provider, clock=clock)
        self.validator = validator        # optional CrossSourceValidator

    # ------------------------------------------------------------ new signals
    def _signal_walls(self, payload, mid):
        """Persistent resting whale walls (pillar 2, L3 half).

        Bid walls below mid are support, ask walls above are resistance,
        proximity-weighted inside ``wall_reach`` exactly like cascade fuel.
        The tracker already filters persistence; the signal re-verifies it
        (defense in depth - a payload from any other source gets the same
        anti-spoof guarantee).
        """
        walls = verified_wallet_l3(payload, self.clock())
        if mid <= 0:
            return None, {"available": False, "reason": "no_mid"}
        reach = math.log(1.0 + self.policy.wall_reach)
        bid_usd = ask_usd = 0.0
        counted = 0
        top_bid = top_ask = None
        for wall in walls:
            if not isinstance(wall, dict):
                continue
            side = str(wall.get("side", "")).upper()
            px = number(wall.get("price"), 0.0)
            usd = number(wall.get("notional_usd"), 0.0)
            persistence = number(wall.get("persistence_sec"), 0.0)
            if px <= 0 or usd <= 0:
                continue
            if persistence + 1e-9 < self.policy.wall_min_persistence_sec:
                continue                      # fleeting depth, not a wall
            proximity = (max(0.0, 1.0 - abs(math.log(px / mid)) / reach)
                         if reach > 0 else 1.0)
            if side == "BUY" and px < mid:
                bid_usd += usd * proximity
                counted += 1
                if top_bid is None or usd > top_bid[1]:
                    top_bid = (px, usd)
            elif side == "SELL" and px > mid:
                ask_usd += usd * proximity
                counted += 1
                if top_ask is None or usd > top_ask[1]:
                    top_ask = (px, usd)
        if bid_usd + ask_usd <= 0 or counted == 0:
            return None, {"available": False, "reason": "no_persistent_walls"}
        value = math.tanh((bid_usd - ask_usd) / self.policy.wall_scale_usd)
        basis = {"available": True, "bid_wall_usd": round(bid_usd, 4),
                 "ask_wall_usd": round(ask_usd, 4), "walls_counted": counted}
        if top_bid is not None:
            basis["top_bid_wall"] = {"price": top_bid[0],
                                     "notional_usd": top_bid[1]}
        if top_ask is not None:
            basis["top_ask_wall"] = {"price": top_ask[0],
                                     "notional_usd": top_ask[1]}
        return value, basis

    def _signal_consistency(self, payload, mid):
        """Cross-venue consensus divergence (pillar 6).

        Positive when the per-venue last-trade consensus sits ABOVE the bus
        mid (the local book is cheap relative to the cross-source consensus).
        Fail-closed: fewer than ``consistency_min_venues`` venues, or a
        failing OI agreement between sources, degrades to unavailable.
        """
        block = payload.get("crosscheck") or {}
        venue_prices = block.get("venue_prices") or {}
        venues = {str(name): number(price, 0.0)
                  for name, price in venue_prices.items()
                  if number(price, 0.0) > 0}
        if len(venues) < self.policy.consistency_min_venues:
            return None, {"available": False, "reason": "insufficient_venues",
                          "venues": sorted(venues)}
        oi = block.get("oi_agreement")
        if isinstance(oi, dict) and oi.get("pass") is False:
            return None, {"available": False, "reason": "oi_disagreement",
                          "disagreement": oi.get("disagreement")}
        if mid <= 0:
            return None, {"available": False, "reason": "no_mid"}
        consensus = sum(venues.values()) / len(venues)
        delta_bps = (consensus - mid) / mid * 1e4
        value = _clamp(math.tanh(delta_bps / self.policy.consistency_scale_bps))
        return value, {"available": True, "venues": sorted(venues),
                       "consensus_price": round(consensus, 8),
                       "delta_bps": round(delta_bps, 6),
                       "mid_divergence_bps": block.get("mid_divergence_bps")}

    # ------------------------------------------------------------ chain hooks
    def _evaluators(self, payload, mid, macro):
        evaluators = super()._evaluators(payload, mid, macro)
        evaluators["walls"] = lambda: self._signal_walls(payload, mid)
        evaluators["consistency"] = lambda: self._signal_consistency(payload, mid)
        return evaluators

    def _enrich_payload(self, asset, payload, now):
        """Attach the pillar-6 crosscheck block (never raises; a missing
        validator simply leaves the consistency pillar unavailable)."""
        if self.validator is None or not isinstance(payload, dict):
            return payload
        try:
            block = {"venue_prices": self.validator.venue_prices(asset, now),
                     "mid_divergence_bps": self.validator.mid_divergence_bps(asset, now),
                     "oi_agreement": self.validator.oi_agreement(asset, now)}
        except Exception:                                 # noqa: BLE001
            return payload
        payload = dict(payload)
        payload["crosscheck"] = block
        return payload

    def _pillar_manifest(self, payload, advisory):
        """Availability manifest of the 6 factory pillars (deterministic)."""
        signals = advisory.get("signals") or {}

        def availability(name):
            signal = signals.get(name) or {}
            out = {"signal": name, "available": bool(signal.get("available"))}
            if not out["available"]:
                out["reason"] = signal.get("reason", "no_data")
            return out

        return {
            "P1_RECONSTRUCTED_LIQUIDATIONS": availability("cascade"),
            "P2A_STOP_CLUSTERS": availability("stops"),
            "P2B_WHALE_WALL_PERSISTENCE": availability("walls"),
            "P3_ONCHAIN_WHALE_FLOWS": availability("whale"),
            "P4_FARSIDE_ETF_FLOWS": availability("macro"),
            "P5_SENTIMENT_COINBASE_PREMIUM": availability("macro"),
            "P6_CROSS_SOURCE_CONSISTENCY": {**availability("consistency"),
                                            "quality_score": advisory.get("quality_score")},
        }

    def evaluate(self, asset, payload, features, macro=None, now=None):
        asset = str(asset).upper()
        resolved = float(number(now, self.clock()))
        payload = self._enrich_payload(asset, payload, resolved)
        return super().evaluate(asset, payload, features, macro, now)

    def _finalize(self, advisory, payload):
        """Stamp the pillar manifest INSIDE the digest (tamper-evident)."""
        if "pillars" not in advisory:
            advisory["pillars"] = self._pillar_manifest(payload, advisory)
        return super()._finalize(advisory, payload)
