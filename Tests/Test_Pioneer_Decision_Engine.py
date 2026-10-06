"""Tests for consultation 4: the Pioneer decision layer.

Covers, 100% offline and deterministically (fake clock + fake sleep, mocked
pollers/samplers, no network):

  1. CrossSourceValidator - cross-venue mid divergence, Binance-vs-Hyperliquid
     OI agreement, synthetic-vs-empirical liquidation calibration, stop-model
     parity against a legacy vendor feed, freshness, sealed quality reports.
  2. RealtimeRunner - continuous refresh cadences (OI from every source, whale
     cohort sampling, macro, watchdog quality reports), pillar health status,
     jitter-free determinism.
  3. PioneerDecisionEngine - every signal in isolation, weight renormalization,
     fail-closed gates (stale book, quality floor, blackout), friction floor
     (>= 41 bps + spread), veto-only tradeability, SHA-256 chained digests.
  4. Integration - factory payload -> features_from_factory -> pioneer advisory,
     and the Omni_Trader hook: a pioneer veto suppresses NEW entries only.
"""
import asyncio
import copy
import math

import pytest

from Terminal.Data_Factory import (ZeroCostDataFactory, CrossSourceValidator,
                                   CrossCheckPolicy, RealtimeRunner, LivePolicy,
                                   FarsideETFFlows, FearGreedIndex)
from Terminal.Pioneer_Decision_Engine import PioneerDecisionEngine, PioneerPolicy, POLICY_VERSION
from Terminal.Risk_Sizing_Engine import OrderflowModel, RiskPolicy, CovarianceGate, number

NOW = 1_760_000_000.0
FARSIDE_HTML = (b"<html><table><tr><td>Date</td><td>Total</td></tr>"
                b"<tr><td>05 Oct 2026</td><td>IBIT</td><td>412.2</td><td>Total</td><td>412.2</td></tr></table></html>")
FNG_JSON = b'{"data": [{"value": "72", "value_classification": "Greed", "timestamp": "1760000000"}]}'


# ------------------------------------------------------------------ fixtures
class FakeClock:
    """Discrete-event virtual time: concurrent sleeps OVERLAP like wall time.

    (A naive advance-on-every-sleep clock double-counts concurrent loops and
    can blow past deadlines before sibling coroutines are ever scheduled.)"""
    def __init__(self, t=NOW):
        self.t = float(t)
        self._wakeups = []              # heap of (wake_time, future)

    def __call__(self):
        return self.t

    def clock(self):
        return self.t

    async def sleep(self, seconds):
        import heapq
        loop = asyncio.get_running_loop()
        fut = loop.create_future()
        heapq.heappush(self._wakeups, (self.t + max(0.0, float(seconds)), fut))
        # A ready-callback keeps virtual time flowing even when every task is
        # asleep (a real loop fires timer callbacks autonomously; so must we,
        # or the last sleepers deadlock with nobody left to pump the clock).
        loop.call_soon(self._pump)
        await fut

    def _pump(self):
        if self._wakeups:
            wake, fut = self._wakeups[0]
            if wake > self.t:
                self.t = wake            # jump to the next scheduled event
        self._release()

    def _release(self):
        due = [(w, f) for w, f in self._wakeups if w <= self.t and not f.done()]
        for wake, fut in due:
            self._wakeups.remove((wake, fut))
            fut.set_result(None)


def _offline_fetch(url, timeout=10.0):
    raise OSError("offline test")


def feed_factory(now=NOW, *, venues=("BINANCE", "HYPERLIQUID"), whale=False):
    """A primed factory: 30 trades, fresh book, bars, an OI cohort.
    Macro trackers get instant-failing fetchers: no test may touch a network."""
    factory = ZeroCostDataFactory(["SOL"], clock=lambda: now)
    factory.fng = FearGreedIndex(fetch=_offline_fetch, clock=lambda: now)
    factory.farside = FarsideETFFlows(fetch=_offline_fetch, clock=lambda: now)
    for i in range(30):
        factory.ingest_trade("SOL", {"ts": now - 30 + i, "price": 120.5, "size": 3.0,
                                     "side": "BUY" if i % 3 else "SELL",
                                     "venue": venues[i % len(venues)],
                                     "trade_id": i, "notional_usd": 361.5})
    factory.ingest_book("SOL", {"ts": now - 2, "best_bid": 120.49, "best_ask": 120.51,
                                "bids": [{"price": 120.49 - i * 0.01, "size": 80000} for i in range(20)],
                                "asks": [{"price": 120.51 + i * 0.01, "size": 50000} for i in range(20)]})
    factory.ingest_bars("SOL", [{"time": now - (30 - i) * 900, "open": 120, "high": 120.9,
                                 "low": 119.1, "close": 120 + 0.4 * math.sin(i / 3.0),
                                 "volume": 100} for i in range(30)])
    factory.ingest_oi("SOL", ts=now - 900, oi_contracts=0, price=120.5)
    factory.ingest_oi("SOL", ts=now, oi_contracts=83_000, price=120.5)   # ~10M USD cohort
    if whale:
        factory.ingest_whale_positions("SOL", [
            {"address": "0xabc", "size": 40_000.0, "entry_price": 118.0,
             "notional_usd": 4_800_000.0, "unrealized_pnl_usd": 90_000.0,
             "liquidation_price": 106.4}], observed_at=now - 60)
        factory.ingest_whale_flow("SOL", {"ts": now - 3600, "direction": "EXCHANGE_OUTFLOW",
                                          "notional_usd": 900_000.0, "token": "SOL"})
    return factory


def synthetic_payload(**overrides):
    """A minimal trader-contract payload for pioneer signal isolation."""
    payload = {"coin": "SOL", "price": 120.0,
               "l2_book": {"timestamp": NOW * 1000, "best_bid": 119.99, "best_ask": 120.01},
               "orderflow": {"cvd_1m": 0.0, "cvd_5m": 0.0, "cvd_15m": 0.0,
                             "taker_buy_usd_15m": 0.0, "taker_sell_usd_15m": 0.0,
                             "taker_ratio_15m": 0.0, "spread_bps": 1.7},
               "projected_liquidations": {"kind": "PROJECTED_EXPOSURE", "bands": []},
               "observed_stops": {"kind": "OBSERVED_STOP_ORDERS", "bands": []},
               "whale_positions": [], "whale_net_flow_usd_24h": 0.0,
               "sources": {}}
    payload.update(overrides)
    return payload


def features(direction="LONG", book_as_of=NOW - 1):
    return {"direction": direction, "book_as_of": book_as_of, "sigma_h": 0.4,
            "confluence": 0.8, "quality": 0.8}


# ============================================== 1. CrossSourceValidator
def test_mid_divergence_between_venues_is_measured_and_scored():
    factory = feed_factory()
    validator = CrossSourceValidator(factory)
    # BINANCE trades at 120.5, HYPERLIQUID at 120.5: no divergence.
    assert validator.mid_divergence_bps("SOL", NOW) is not None
    assert validator.mid_divergence_bps("SOL", NOW) == pytest.approx(0.0, abs=1.0)
    # Push the venues 60 bps apart: the check must fail the quality score.
    factory.ingest_trade("SOL", {"ts": NOW + 1, "price": 121.22, "size": 1.0,
                                 "side": "BUY", "venue": "BINANCE", "notional_usd": 121.22})
    assert validator.mid_divergence_bps("SOL", NOW + 2) > 50.0
    clean = validator.quality_report(["SOL"], NOW + 2)["assets"]["SOL"]["quality_score"]
    factory2 = feed_factory()
    validator2 = CrossSourceValidator(factory2)
    good = validator2.quality_report(["SOL"], NOW + 2)["assets"]["SOL"]["quality_score"]
    assert clean < good


def test_oi_agreement_between_binance_and_hyperliquid():
    validator = CrossSourceValidator(feed_factory())
    validator.record_oi("SOL", "BINANCE", NOW, 10_000_000)
    assert validator.oi_agreement("SOL", NOW) is None            # one source only
    validator.record_oi("SOL", "HYPERLIQUID", NOW, 9_200_000)
    agreement = validator.oi_agreement("SOL", NOW)
    assert agreement["pass"] and agreement["disagreement"] == pytest.approx(0.08, abs=1e-9)
    validator.record_oi("SOL", "BYBIT", NOW, 4_000_000)
    assert not validator.oi_agreement("SOL", NOW)["pass"]        # 60% disagreement


def test_liquidation_calibration_hit_rate_against_real_prints():
    def printed(price, n=6, usd=100_000.0):
        factory = feed_factory()
        for i in range(n):
            factory.ingest_liquidation("SOL", {"ts": NOW - 60 + i, "price": price,
                                               "notional_usd": usd,
                                               "position_side_liquidated": "LONG"})
        return CrossSourceValidator(factory)

    # Prints inside the 10x long-liq corridor (~108.5) the model ranks hottest.
    inside = printed(108.5).liquidation_calibration("SOL", NOW)
    assert inside["available"] and inside["hit_rate"] > 0.5
    # Prints far below every modeled band: the model ranked those bands cold.
    outside = printed(101.0).liquidation_calibration("SOL", NOW)
    assert outside["available"] and outside["hit_rate"] < 0.5
    # Too few prints to judge: honest unavailable, never a fabricated score.
    thin = printed(108.5, n=2).liquidation_calibration("SOL", NOW)
    assert not thin["available"]


def test_freshness_fails_closed_on_stale_book():
    validator = CrossSourceValidator(feed_factory())
    fresh = validator.freshness("SOL", NOW)
    assert fresh["book"]["pass"] and fresh["trades"]["pass"]
    stale = validator.freshness("SOL", NOW + 120)
    assert not stale["book"]["pass"]
    report = validator.quality_report(["SOL"], NOW + 120)
    assert report["assets"]["SOL"]["quality_score"] < 0.5


def test_quality_report_is_deterministic_and_sealed():
    validator = CrossSourceValidator(feed_factory())
    first = validator.quality_report(["SOL"], NOW)
    second = validator.quality_report(["SOL"], NOW)
    assert first["digest"] == second["digest"]
    validator.record_oi("SOL", "BINANCE", NOW, 10_000_000)
    third = validator.quality_report(["SOL"], NOW)
    assert third["digest"] != first["digest"]                  # state changed => new seal
    assert 0.0 <= third["quality_score"] <= 1.0


def test_stop_model_parity_against_legacy_vendor_feed():
    factory = feed_factory()
    validator = CrossSourceValidator(factory)
    # No vendor reachable: parity degrades honestly.
    assert validator.stop_model_parity("SOL")["available"] is False
    synthetic_total = sum(b["amount_usd"] for b in factory.payload("SOL", NOW)["observed_stops"]["bands"])
    comparable = {"bands": [{"amount_usd": synthetic_total}]}
    parity = validator.stop_model_parity("SOL", legacy_stops=comparable)
    assert parity["available"] and parity["pass"] and parity["ratio"] == pytest.approx(1.0)
    assert not validator.stop_model_parity(
        "SOL", legacy_stops={"bands": [{"amount_usd": synthetic_total / 20.0}]})["pass"]


# ============================================== 2. RealtimeRunner
def run_runner(factory, *, validator=None, oi_pollers=None, whale_sampler=None,
               stop_after_calls=3, max_seconds=None, clock=None, policy=None):
    clock = clock or FakeClock()
    sleep = clock.sleep                    # discrete-event virtual time
    stop_event = asyncio.Event()
    calls = {"n": 0}

    def maybe_stop():
        calls["n"] += 1
        if calls["n"] >= stop_after_calls:
            stop_event.set()

    pollers, sampler = oi_pollers, whale_sampler
    if pollers:
        wrapped = {}
        for source, fn in pollers.items():
            def wrap(asset, _fn=fn):
                sample = _fn(asset)
                maybe_stop()
                return sample
            wrapped[source] = wrap
        pollers = wrapped
    if sampler:
        def wrapped_sampler(asset, _fn=sampler):      # default-arg: capture, don't rebind
            out = _fn(asset)
            maybe_stop()
            return out
        sampler = wrapped_sampler

    runner = RealtimeRunner(factory, validator, oi_pollers=pollers, whale_sampler=sampler,
                            policy=policy or LivePolicy(jitter_fraction=0.0),
                            clock=clock, sleep=sleep)
    asyncio.run(runner.run(["SOL"], stop_event=stop_event, max_seconds=max_seconds))
    return runner, calls["n"]


def oi_sample(asset, ts):
    return {"ts": ts, "oi_contracts": 83_000, "price": 120.5, "contract_size": 1.0}


def test_runner_polls_every_oi_source_and_feeds_the_cohort_model():
    factory = feed_factory()
    validator = CrossSourceValidator(factory)
    clock = FakeClock()
    polls = {"BINANCE": 0, "HYPERLIQUID": 0}

    def poller(source):
        def fn(asset):
            polls[source] += 1
            return oi_sample(asset, clock() + polls[source])      # runner clock advances
        return fn

    runner, calls = run_runner(factory, validator=validator, clock=clock,
                               oi_pollers={"BINANCE": poller("BINANCE"),
                                           "HYPERLIQUID": poller("HYPERLIQUID")})
    assert calls >= 3 and polls["BINANCE"] >= 2 and polls["HYPERLIQUID"] >= 2
    # Only the PRIMARY source drives the cohort ledger...
    assert factory.stats["oi_samples"] >= 4                       # 2 seeds + >=2 polls
    # ...but BOTH sources feed the cross-source agreement check.
    agreement = validator.oi_agreement("SOL", clock())
    assert agreement is not None and set(agreement["sources"]) == {"BINANCE", "HYPERLIQUID"}
    assert runner.status()["pillars"]["oi"]["healthy"]


def test_runner_samples_the_whale_cohort_into_the_payload():
    factory = feed_factory(whale=True)
    positions = [{"address": "0xabc", "size": 40_000.0, "entry_price": 118.0,
                  "notional_usd": 4_800_000.0, "liquidation_price": 106.4}]
    runner, calls = run_runner(factory, whale_sampler=lambda asset: positions,
                               stop_after_calls=3)
    assert calls >= 3 and runner.stats["whale_polls"] >= 3
    payload = factory.payload("SOL", NOW)
    assert payload["whale_positions"] and payload["whale_positions"][0]["address"] == "0xabc"
    assert payload["whale_net_flow_usd_24h"] == pytest.approx(900_000.0)   # the seeded outflow
    assert runner.status()["pillars"]["whales"]["healthy"]


def test_runner_refreshes_macro_and_runs_the_watchdog():
    factory = feed_factory()
    factory.fng = FearGreedIndex(fetch=lambda url: FNG_JSON, clock=lambda: NOW)
    factory.farside = FarsideETFFlows(fetch=lambda url: FARSIDE_HTML, clock=lambda: NOW)
    validator = CrossSourceValidator(factory)
    runner, _ = run_runner(factory, validator=validator, max_seconds=3660)
    assert factory.fng.value()["value"] == 72
    assert runner.stats["etf_refreshes"] >= 2                    # BTC + ETH
    assert runner.last_quality is not None
    assert runner.quality_history[0]["quality_score"] > 0.5      # fresh at t0
    # With no live streams feeding the bus, fake time flows on and the report
    # degrades honestly to zero: fail-closed, never fabricated freshness.
    assert runner.last_quality["quality_score"] == 0.0
    assert not runner.last_quality["assets"]["SOL"]["freshness"]["book"]["pass"]
    assert runner.status()["quality_digest"] == runner.last_quality["digest"]
    assert runner.status()["pillars"]["fng"]["healthy"]


def test_runner_is_deterministic_without_jitter():
    def build():
        factory = feed_factory()
        validator = CrossSourceValidator(factory)
        runner, _ = run_runner(factory, validator=validator,
                               oi_pollers={"BINANCE": lambda a: oi_sample(a, NOW)},
                               stop_after_calls=2)
        return runner.stats, runner.last_quality["digest"]

    first_stats, first_digest = build()
    second_stats, second_digest = build()
    assert first_stats == second_stats and first_digest == second_digest


# ============================================== 3. PioneerDecisionEngine
def test_pioneer_abstains_on_stale_book_no_mid_and_blackout():
    pioneer = PioneerDecisionEngine(clock=lambda: NOW)
    stale = pioneer.evaluate("SOL", synthetic_payload(), features(book_as_of=NOW - 120), now=NOW)
    assert not stale["tradeable"] and stale["reason"] == "book_stale"
    no_mid = pioneer.evaluate("SOL", synthetic_payload(price=0.0), features(), now=NOW)
    assert not no_mid["tradeable"] and no_mid["reason"] == "no_mid"
    blackout = pioneer.evaluate("SOL", synthetic_payload(), features(),
                                macro={"blackout_active": True}, now=NOW)
    assert not blackout["tradeable"] and blackout["reason"] == "macro_blackout"


def test_pioneer_abstains_below_the_quality_floor():
    pioneer = PioneerDecisionEngine(quality_provider=lambda asset: {"quality_score": 0.30},
                                    clock=lambda: NOW)
    advisory = pioneer.evaluate("SOL", synthetic_payload(), features(), now=NOW)
    assert not advisory["tradeable"] and advisory["reason"].startswith("quality_below_floor")
    passing = PioneerDecisionEngine(quality_provider=lambda asset: {"quality_score": 0.90},
                                    clock=lambda: NOW)
    assert passing.evaluate("SOL", synthetic_payload(), features(), now=NOW)["quality_score"] == 0.90


def test_orderflow_signal_reads_the_live_tape():
    pioneer = PioneerDecisionEngine(clock=lambda: NOW)
    bullish = dict(synthetic_payload()["orderflow"])
    bullish.update(cvd_1m=800_000.0, cvd_5m=2_000_000.0, cvd_15m=4_000_000.0,
                   taker_buy_usd_15m=5_000_000.0, taker_sell_usd_15m=1_000_000.0,
                   taker_ratio_15m=0.6667)
    advisory = pioneer.evaluate("SOL", synthetic_payload(orderflow=bullish), features(), now=NOW)
    assert advisory["signals"]["orderflow"]["value"] > 0.3
    bearish = dict(bullish)
    bearish.update(cvd_1m=-800_000.0, cvd_5m=-2_000_000.0, cvd_15m=-4_000_000.0,
                   taker_buy_usd_15m=1_000_000.0, taker_sell_usd_15m=5_000_000.0,
                   taker_ratio_15m=-0.6667)
    advisory = pioneer.evaluate("SOL", synthetic_payload(orderflow=bearish), features(), now=NOW)
    assert advisory["signals"]["orderflow"]["value"] < -0.3
    empty = pioneer.evaluate("SOL", synthetic_payload(), features(), now=NOW)
    assert empty["signals"]["orderflow"]["available"] is False    # no tape: no opinion


def test_cascade_signal_squeezes_toward_the_heavier_fuel():
    pioneer = PioneerDecisionEngine(clock=lambda: NOW)
    short_fuel = {"projected_liquidations": {"bands": [
        {"mid_px": 122.0, "amount_usd": 4_000_000.0, "position_side_at_risk": "SHORT"}]}}
    advisory = pioneer.evaluate("SOL", synthetic_payload(**short_fuel), features(), now=NOW)
    assert advisory["signals"]["cascade"]["value"] > 0            # shorts fuel the upside
    long_fuel = {"projected_liquidations": {"bands": [
        {"mid_px": 118.0, "amount_usd": 4_000_000.0, "position_side_at_risk": "LONG"}]}}
    advisory = pioneer.evaluate("SOL", synthetic_payload(**long_fuel), features(), now=NOW)
    assert advisory["signals"]["cascade"]["value"] < 0            # longs fuel the downside
    # Proximity discount: the same fuel 10% away counts for almost nothing.
    far = {"projected_liquidations": {"bands": [
        {"mid_px": 132.0, "amount_usd": 4_000_000.0, "position_side_at_risk": "SHORT"}]}}
    advisory = pioneer.evaluate("SOL", synthetic_payload(**far), features(), now=NOW)
    assert advisory["signals"]["cascade"]["available"] is False   # beyond the 5% reach


def test_stops_signal_points_at_the_heavier_stop_pool():
    pioneer = PioneerDecisionEngine(clock=lambda: NOW)
    sell_heavy = {"observed_stops": {"bands": [
        {"mid_px": 118.0, "amount_usd": 2_000_000.0, "position_side_at_risk": "LONG"},
        {"mid_px": 122.0, "amount_usd": 500_000.0, "position_side_at_risk": "SHORT"}]}}
    advisory = pioneer.evaluate("SOL", synthetic_payload(**sell_heavy), features(), now=NOW)
    assert advisory["signals"]["stops"]["value"] < 0              # sell stops below magnet down
    buy_heavy = {"observed_stops": {"bands": [
        {"mid_px": 118.0, "amount_usd": 500_000.0, "position_side_at_risk": "LONG"},
        {"mid_px": 122.0, "amount_usd": 2_000_000.0, "position_side_at_risk": "SHORT"}]}}
    advisory = pioneer.evaluate("SOL", synthetic_payload(**buy_heavy), features(), now=NOW)
    assert advisory["signals"]["stops"]["value"] > 0


def test_whale_signal_reads_cohort_positions_and_onchain_flows():
    pioneer = PioneerDecisionEngine(clock=lambda: NOW)
    longs = {"whale_positions": [{"size": 40_000.0, "notional_usd": 4_800_000.0}],
             "whale_net_flow_usd_24h": 900_000.0}
    advisory = pioneer.evaluate("SOL", synthetic_payload(**longs), features(), now=NOW)
    assert advisory["signals"]["whale"]["value"] > 0
    shorts = {"whale_positions": [{"size": -40_000.0, "notional_usd": 4_800_000.0}],
              "whale_net_flow_usd_24h": -900_000.0}
    advisory = pioneer.evaluate("SOL", synthetic_payload(**shorts), features(), now=NOW)
    assert advisory["signals"]["whale"]["value"] < 0
    none = pioneer.evaluate("SOL", synthetic_payload(), features(), now=NOW)
    assert none["signals"]["whale"]["available"] is False


def test_macro_signal_combines_etf_premium_and_contrarian_fng():
    pioneer = PioneerDecisionEngine(clock=lambda: NOW)
    bullish = {"etf_net_flow_musd_1d": 800.0, "coinbase_premium_bps": 15.0,
               "fear_greed": {"value": 55.0}}
    advisory = pioneer.evaluate("SOL", synthetic_payload(), features(), macro=bullish, now=NOW)
    assert advisory["signals"]["macro"]["value"] > 0.3
    # Extreme greed flips the F&G component contrarian (it is a crowded trade).
    greed = dict(bullish, fear_greed={"value": 88.0})
    advisory = pioneer.evaluate("SOL", synthetic_payload(), features(), macro=greed, now=NOW)
    assert advisory["signals"]["macro"]["components"]["fear_greed_contra"] < 0
    # The Market_Intelligence report shape (macro nested under data_factory) works too.
    report_shape = {"blackout_active": False, "data_factory": greed}
    nested = pioneer.evaluate("SOL", synthetic_payload(), features(), macro=report_shape, now=NOW)
    assert nested["signals"]["macro"]["available"]
    assert nested["signals"]["macro"]["value"] == pytest.approx(
        advisory["signals"]["macro"]["value"], abs=1e-9)


def test_unavailable_signals_renormalize_their_weight():
    pioneer = PioneerDecisionEngine(clock=lambda: NOW)
    # Only the orderflow signal has data: conviction == that signal's value.
    bullish = dict(synthetic_payload()["orderflow"])
    bullish.update(cvd_1m=800_000.0, cvd_5m=2_000_000.0, cvd_15m=4_000_000.0,
                   taker_buy_usd_15m=5_000_000.0, taker_sell_usd_15m=1_000_000.0,
                   taker_ratio_15m=0.6667)
    advisory = pioneer.evaluate("SOL", synthetic_payload(orderflow=bullish), features(), now=NOW)
    assert advisory["conviction"] == pytest.approx(advisory["signals"]["orderflow"]["value"],
                                                   abs=1e-6)


def test_quality_discount_scales_conviction():
    bullish = dict(synthetic_payload()["orderflow"])
    bullish.update(cvd_1m=800_000.0, cvd_5m=2_000_000.0, cvd_15m=4_000_000.0,
                   taker_buy_usd_15m=5_000_000.0, taker_sell_usd_15m=1_000_000.0,
                   taker_ratio_15m=0.6667)
    full = PioneerDecisionEngine(quality_provider=lambda a: {"quality_score": 1.0},
                                 clock=lambda: NOW)
    partial = PioneerDecisionEngine(quality_provider=lambda a: {"quality_score": 0.75},
                                    clock=lambda: NOW)
    c_full = full.evaluate("SOL", synthetic_payload(orderflow=bullish), features(), now=NOW)["conviction"]
    c_part = partial.evaluate("SOL", synthetic_payload(orderflow=bullish), features(), now=NOW)["conviction"]
    assert c_part == pytest.approx(0.75 * c_full, abs=1e-6)


def test_advice_thresholds_and_veto_only_tradeability():
    pioneer = PioneerDecisionEngine(clock=lambda: NOW)
    strong_bull = dict(synthetic_payload()["orderflow"])
    strong_bull.update(cvd_1m=1_500_000.0, cvd_5m=4_000_000.0, cvd_15m=8_000_000.0,
                       taker_buy_usd_15m=9_000_000.0, taker_sell_usd_15m=1_000_000.0,
                       taker_ratio_15m=0.8)
    advisory = pioneer.evaluate("SOL", synthetic_payload(orderflow=strong_bull),
                                features(direction="LONG"), now=NOW)
    assert advisory["advice"] == "SUPPORT_LONG" and advisory["tradeable"]
    opposed = pioneer.evaluate("SOL", synthetic_payload(orderflow=strong_bull),
                               features(direction="SHORT"), now=NOW)
    assert opposed["advice"] == "SUPPORT_LONG" and not opposed["tradeable"]
    assert opposed["reason"] == "opposed_conviction:SUPPORT_LONG_vs_SHORT"
    # NEUTRAL conviction never blocks: absence of evidence is not a veto.


def test_friction_floor_covers_41bps_round_trip_plus_spread():
    pioneer = PioneerDecisionEngine(clock=lambda: NOW)
    advisory = pioneer.evaluate("SOL", synthetic_payload(), features(), now=NOW)
    assert advisory["min_favorable_move_bps"] >= 41.0 + 5.0
    assert advisory["min_favorable_move_bps"] == pytest.approx(41.0 + 5.0 + 1.7)


def test_digests_chain_per_asset_and_stay_deterministic():
    def fresh():
        pioneer = PioneerDecisionEngine(clock=lambda: NOW)
        a = pioneer.evaluate("SOL", synthetic_payload(), features(), now=NOW)
        b = pioneer.evaluate("SOL", synthetic_payload(), features(), now=NOW)
        return a["digest"], b["digest"]

    d1, d2 = fresh()
    e1, e2 = fresh()
    assert d1 == e1                             # same inputs -> same first digest
    assert d2 != d1 and e2 != e1                # chained: each eval seals the previous
    pioneer = PioneerDecisionEngine(clock=lambda: NOW)
    pioneer.evaluate("SOL", synthetic_payload(), features(), now=NOW)
    btc = pioneer.evaluate("BTC", synthetic_payload(), features(), now=NOW)
    assert btc["digest"] != d1                  # per-asset chains stay independent


# ============================================== 4. Integration
def test_pioneer_end_to_end_over_factory_features():
    factory = feed_factory(whale=True)
    # A decisively bullish tape on top of the primed factory.
    for i in range(20):
        factory.ingest_trade("SOL", {"ts": NOW - 20 + i, "price": 120.5 + i * 0.01,
                                     "size": 5.0, "side": "BUY", "venue": "BINANCE",
                                     "trade_id": 1000 + i, "notional_usd": 600_000.0})
    validator = CrossSourceValidator(factory)
    quality = validator.quality_report(["SOL"], NOW)
    pioneer = PioneerDecisionEngine(quality_provider=lambda a: quality, clock=lambda: NOW)
    model = OrderflowModel(RiskPolicy())
    bars = factory._bars["SOL"]
    macro = {"blackout_active": False,
             "data_factory": factory.macro_snapshot()}
    feats = model.features_from_factory(factory, "SOL", bars, macro, NOW)
    advisory = pioneer.evaluate("SOL", factory.payload("SOL", NOW), feats, macro, now=NOW)
    assert advisory["policy_version"] == POLICY_VERSION
    assert advisory["signals"]["orderflow"]["available"]
    assert advisory["signals"]["whale"]["value"] > 0
    # Whatever the base model proposed, the pioneer only passes or vetoes -
    # and here the live tape, whale cohort and flows all agree bullish.
    direction = feats["direction"]
    assert advisory["advice"] in ("SUPPORT_LONG", "SUPPORT_SHORT", "NEUTRAL")
    assert advisory["tradeable"] == (advisory["advice"] in ("NEUTRAL", f"SUPPORT_{direction}"))


# ------- Omni_Trader integration (harness mirrors Test_Omni_Hardening) -----
from Terminal.Asset_Universe import UNIVERSE                      # noqa: E402
from Terminal.Omni_Trader import AI15mMT5Trader, MAGIC            # noqa: E402

SLOT = (NOW // 900) * 900 + 870          # the minute-14 execution window


def _bars(now=SLOT, count=96, trend=0.2, mid=120.0):
    start = int(now // 900) * 900 - count * 900
    return [{"time": start + i * 900, "open": mid + trend * i + 0.05 * math.sin(0.9 * i),
             "high": mid + trend * i + 0.55, "low": mid + trend * i - 0.55,
             "close": mid + trend * i + 0.05 * math.sin(0.9 * i)} for i in range(count)]


def _covariance(now=SLOT, assets=UNIVERSE, sigma=0.003):
    import numpy as np
    return CovarianceGate(assets, np.eye(len(assets)) * sigma ** 2,
                          {"return_units": "decimal_log_return", "horizon_minutes": 15,
                           "created_at": now - 60, "data_end": now - 900,
                           "max_age_seconds": 86400})


class _Broker:
    def __init__(self, clock, mid=120.0):
        self.clock = clock; self.positions = []; self.pending = []; self.sent = []
        self.mid = mid; self.filled = False; self.history_state = None

    def get_open_positions(self): return copy.deepcopy(self.positions)
    def get_pending_orders(self): return copy.deepcopy(self.pending)
    def get_account_summary(self): return {"connected": True, "login": 1, "currency": "USD",
                                           "equity_usd": 5000, "margin_free_usd": 5000}
    def resolve_symbol(self, asset): return asset + "USD" if asset not in ("GOLD", "SILVER") else "XAUUSD"
    def get_recent_bars(self, symbol, count=96): return _bars(self.clock())
    def get_symbol_price(self, symbol):
        return {"bid": self.mid - 0.01, "ask": self.mid + 0.01, "point": .01, "tick_size": .01,
                "time_msc": self.clock() * 1000, "digits": 2, "contract_size": 100, "min_lot": .01,
                "step_lot": .01, "max_lot": 10, "stops_level": 0, "freeze_level": 0,
                "currency_profit": "USD"}
    def estimate_order(self, symbol, direction, entry, sl):
        return {"stop_loss_per_lot": abs(entry - sl) * 100, "margin_per_lot": 1000}
    def modify_position_sltp(self, ticket, sl, tp): return {"success": True}
    def close_position(self, ticket): return {"success": True}
    def position_deals(self, ticket): return []
    def execute_market_order(self, *a, **k): return {"success": True, "ticket": 1, "uncertain": False}
    def stage_limit_order(self, symbol, direction, volume, limit_price, sl, tp, **kwargs):
        ticket = 1000 + len(self.sent)
        order = {"ticket": ticket, "symbol": symbol, "direction": direction, "volume": volume,
                 "price_open": limit_price, "sl": sl, "tp": tp, "magic": kwargs.get("magic", MAGIC)}
        self.pending.append(order); self.sent.append((order, kwargs))
        return {"success": True, "ticket": ticket}
    def cancel_pending_order(self, ticket): return {"success": True}
    def reconcile_intent_history(self, comment, prepared_at): return self.history_state
    def intent_filled(self, comment, prepared_at): return self.filled


class _Intel:
    def check_macro_blackout(self): return False, "NO_EVENT", 999
    def get_market_intelligence_report(self): return {"asset_scores": {a: 1 for a in UNIVERSE},
                                                      "sentiment_valid": True}


def _payload(now=SLOT, l3=None, mid=120.0):
    half = 0.01
    return {"coin": "SOL", "price": mid,
            "l2_book": {"timestamp": now * 1000, "best_bid": mid - half, "best_ask": mid + half,
                        "bids": [{"price": mid - half - i * 0.01, "size": 10000} for i in range(20)],
                        "asks": [{"price": mid + half + i * 0.01, "size": 100} for i in range(20)]},
            "recent_trades": [{"time": now * 1000, "side": "BUY", "price": mid, "size": 100,
                               "notional_usd": 10000},
                              {"time": now * 1000, "side": "BUY", "price": mid, "size": 100,
                               "notional_usd": 10000}],
            "sources": {"l3": {"observed_at": now}, "liquidations": {"observed_at": now}},
            "l3_orders": l3 or [], "liquidations": {}}


def _trader(tmp_path, mid=120.0):
    broker = _Broker(lambda: SLOT, mid=mid)
    t = AI15mMT5Trader(bridge=broker, intel=_Intel(), cognitive=object(),
                       covariance=_covariance(), uplift_path=tmp_path / "no_uplift",
                       cognitive_enabled=False, clock=lambda: SLOT, paper_mode=True,
                       state_file=tmp_path / "state.json", journal_dir=tmp_path / "journal",
                       entry_mode="limit")
    t.symbols = {a: broker.resolve_symbol(a) for a in UNIVERSE}
    t.bars = {a: _bars() for a in UNIVERSE}
    return t, broker


def _macro():
    return {"received_at": SLOT, "sentiment_valid": True, "asset_scores": {"SOL": 1},
            "blackout_active": False}


def test_omni_pioneer_veto_suppresses_new_entries_only(tmp_path):
    # Proven T1-breakout geometry: this exact fixture fills without a pioneer.
    baseline_t, _ = _trader(tmp_path / "baseline")
    result = baseline_t.evaluate_market({"SOL": _payload()}, _macro())
    assert result["decision"] == "PAPER_FILLED"

    # Same geometry + a low-quality pioneer: the entry is vetoed...
    vetoed_t, _ = _trader(tmp_path / "vetoed")
    vetoed_t.attach_pioneer(PioneerDecisionEngine(
        quality_provider=lambda a: {"quality_score": 0.10}, clock=lambda: SLOT))
    vetoed = vetoed_t.evaluate_market({"SOL": _payload()}, _macro())
    assert vetoed["decision"] == "HOLD"                          # no dispatch, no reason spam
    assert vetoed["vetoes"]["SOL"].startswith("pioneer_veto:quality_below_floor")
    assert not vetoed_t.state["paper_positions"]                 # nothing was staged

    # ...and an opposed conviction vetoes too, while a passing pioneer lets the
    # identical trade through untouched (sizing, sleeve and exits unchanged).
    opposed_t, _ = _trader(tmp_path / "opposed")
    opposed_t.attach_pioneer(PioneerDecisionEngine(clock=lambda: SLOT))
    strong_bear = dict(synthetic_payload()["orderflow"])
    strong_bear.update(cvd_1m=-1_500_000.0, cvd_5m=-4_000_000.0, cvd_15m=-8_000_000.0,
                       taker_buy_usd_15m=1_000_000.0, taker_sell_usd_15m=9_000_000.0,
                       taker_ratio_15m=-0.8, spread_bps=1.7)
    opposed_payload = _payload()
    opposed_payload["orderflow"] = strong_bear
    opposed_result = opposed_t.evaluate_market({"SOL": opposed_payload}, _macro())
    assert opposed_result["decision"] == "HOLD"
    assert opposed_result["vetoes"]["SOL"].startswith("pioneer_veto:opposed_conviction")
    assert not opposed_t.state["paper_positions"]

    aligned_t, broker = _trader(tmp_path / "aligned")
    aligned_t.attach_pioneer(PioneerDecisionEngine(
        quality_provider=lambda a: {"quality_score": 0.95}, clock=lambda: SLOT))
    aligned = aligned_t.evaluate_market({"SOL": _payload()}, _macro())
    assert aligned["decision"] == "PAPER_FILLED"
    assert aligned["execution"]["volume"] == result["execution"]["volume"]   # sizing untouched


def test_omni_without_pioneer_is_bit_for_bit_unchanged(tmp_path):
    t, _ = _trader(tmp_path)
    assert t.pioneer is None
    result = t.evaluate_market({"SOL": _payload()}, _macro())
    assert result["decision"] == "PAPER_FILLED"               # no pioneer: zero behavior delta
