"""Tests for OX_ALPHA_63: the omni.decision_chain.v2 decision chain.

100% offline and deterministic (fake clock, scripted factory ingestion, no
network). Covers:

  1. v1 backward compatibility - PioneerDecisionEngine still emits exactly
     the 5 legacy signals and the omni.pioneer.v1 policy version, even when
     the payload carries v2-only blocks (l3_orders, crosscheck).
  2. The two NEW v2 signals in isolation:
       walls       - persistent resting whale-wall asymmetry (proximity
                     weighted, anti-spoof persistence re-verified);
       consistency - cross-venue consensus divergence vs the bus mid,
                     fail-closed on insufficient venues / OI disagreement.
  3. Weight renormalization across the 7-signal chain.
  4. The 6-pillar availability manifest, stamped inside the SHA-256 digest.
  5. Full-chain integration: ZeroCostDataFactory ingestion (books fed twice
     so walls persist >= 180 s, tri-venue trades, bars, OI cohort, whale
     cohort) -> CrossSourceValidator -> DecisionChainEngine advisory.
  6. Inherited fail-closed gates (stale book, blackout, quality floor),
     the friction floor, veto-only tradeability, and digest determinism.
"""
import copy
import json
import math

import pytest

from Terminal.Data_Factory import ZeroCostDataFactory, CrossSourceValidator
from Terminal.Pioneer_Decision_Engine import (
    DECISION_CHAIN_VERSION,
    DecisionChainEngine,
    DecisionChainPolicy,
    PioneerDecisionEngine,
    PioneerPolicy,
    POLICY_VERSION,
)
from Terminal.Risk_Sizing_Engine import number

NOW = 1_791_331_200.0            # 2026-10-07 00:00:00 UTC
VENUES = ("BINANCE", "COINBASE", "HYPERLIQUID")


# ------------------------------------------------------------------ fixtures
def chain_payload(**overrides):
    """A minimal trader-contract payload for v2 signal isolation."""
    payload = {
        "coin": "SOL", "price": 120.0,
        "l2_book": {"timestamp": NOW * 1000, "best_bid": 119.99, "best_ask": 120.01},
        "orderflow": {"cvd_1m": 0.0, "cvd_5m": 0.0, "cvd_15m": 0.0,
                      "taker_buy_usd_15m": 0.0, "taker_sell_usd_15m": 0.0,
                      "taker_ratio_15m": 0.0, "spread_bps": 1.7},
        "projected_liquidations": {"kind": "PROJECTED_EXPOSURE", "bands": []},
        "observed_stops": {"kind": "OBSERVED_STOP_ORDERS", "bands": []},
        "whale_positions": [], "whale_net_flow_usd_24h": 0.0,
        "l3_orders": [], "sources": {},
    }
    payload.update(overrides)
    return payload


def features(direction="LONG", book_as_of=NOW - 1):
    return {"direction": direction, "book_as_of": book_as_of, "sigma_h": 0.4,
            "confluence": 0.8, "quality": 0.8}


def macro_block(etf=300.0, premium=5.0, fng=20.0):
    return {"etf_net_flow_musd_1d": etf, "coinbase_premium_bps": premium,
            "fear_greed": {"value": fng}}


def feed_factory(now=NOW, *, whale=True):
    """A primed factory: tri-venue trades, fresh book, bars, an OI cohort
    and a whale cohort. Nothing touches a network."""
    factory = ZeroCostDataFactory(["SOL"], clock=lambda: now)
    for i in range(30):
        factory.ingest_trade("SOL", {
            "ts": now - 30 + i, "price": 120.5, "size": 3.0,
            "side": "BUY" if i % 3 else "SELL",
            "venue": VENUES[i % len(VENUES)],
            "trade_id": i, "notional_usd": 361.5})
    factory.ingest_book("SOL", {"ts": now - 2, "best_bid": 120.49, "best_ask": 120.51,
                                "bids": [{"price": 120.49 - i * 0.01, "size": 80000} for i in range(20)],
                                "asks": [{"price": 120.51 + i * 0.01, "size": 50000} for i in range(20)]})
    factory.ingest_bars("SOL", [{"time": now - (30 - i) * 900, "open": 120,
                                 "high": 120.9, "low": 119.1,
                                 "close": 120 + 0.4 * math.sin(i / 3.0),
                                 "volume": 100} for i in range(30)])
    factory.ingest_oi("SOL", ts=now - 900, oi_contracts=0, price=120.5)
    factory.ingest_oi("SOL", ts=now, oi_contracts=83_000, price=120.5)
    if whale:
        factory.ingest_whale_positions("SOL", [
            {"address": "0xabc", "size": 40_000.0, "entry_price": 118.0,
             "notional_usd": 4_800_000.0, "unrealized_pnl_usd": 90_000.0,
             "liquidation_price": 106.4}], observed_at=now - 60)
        factory.ingest_whale_flow("SOL", {
            "ts": now - 3600, "direction": "EXCHANGE_OUTFLOW",
            "notional_usd": 900_000.0, "token": "SOL"})
    return factory


# --------------------------------------------------- 1. v1 backward compat
def test_v1_engine_unchanged_five_signals():
    """v1 must ignore the v2-only payload blocks entirely."""
    payload = chain_payload(
        l3_orders=[{"side": "BUY", "price": 119.0, "notional_usd": 1e7,
                    "persistence_sec": 400.0}],
        crosscheck={"venue_prices": {"BINANCE": 120.0, "COINBASE": 120.06},
                    "mid_divergence_bps": 5.0, "oi_agreement": None})
    engine = PioneerDecisionEngine(clock=lambda: NOW)
    advisory = engine.evaluate("SOL", payload, features(), None, NOW)
    assert advisory["policy_version"] == POLICY_VERSION == "omni.pioneer.v1"
    assert sorted(advisory["signals"]) == ["cascade", "macro", "orderflow",
                                           "stops", "whale"]
    assert "pillars" not in advisory


def test_v1_policy_default_untouched():
    policy = PioneerPolicy()
    assert policy.version == POLICY_VERSION
    assert set(policy.weights) == {"orderflow", "cascade", "stops", "whale",
                                   "macro"}
    assert not hasattr(policy, "wall_reach")


# --------------------------------------------------- 2. new v2 signals
def test_wall_signal_bid_support_is_positive():
    engine = DecisionChainEngine(clock=lambda: NOW)
    payload = chain_payload(l3_orders=[
        {"side": "BUY", "price": 119.0, "notional_usd": 1e7,
         "address": "0xabc", "persistence_sec": 400.0}],
        sources={"l3": {"provider": "HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT", "observed_at": NOW}})
    value, basis = engine._signal_walls(payload, 120.0)
    expected = math.tanh(1e7 * (1.0 - abs(math.log(119.0 / 120.0))
                                / math.log(1.015)) / 5.0e6)
    assert value == pytest.approx(expected, abs=1e-12)
    assert basis["available"] is True
    assert basis["bid_wall_usd"] > 0 and basis["ask_wall_usd"] == 0.0
    assert basis["top_bid_wall"]["price"] == 119.0


def test_wall_signal_ask_resistance_is_negative():
    engine = DecisionChainEngine(clock=lambda: NOW)
    payload = chain_payload(l3_orders=[
        {"side": "SELL", "price": 121.0, "notional_usd": 1e7,
         "address": "0xabc", "persistence_sec": 400.0}],
        sources={"l3": {"provider": "HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT", "observed_at": NOW}})
    value, basis = engine._signal_walls(payload, 120.0)
    assert value < 0.0
    assert basis["ask_wall_usd"] > 0.0 and basis["bid_wall_usd"] == 0.0


def test_wall_signal_filters_spoofs_and_far_walls():
    engine = DecisionChainEngine(clock=lambda: NOW)
    # Seen for 100 s only: fleeting depth, not a resting whale cluster.
    spoof = chain_payload(l3_orders=[
        {"side": "BUY", "price": 119.0, "notional_usd": 1e7,
         "persistence_sec": 100.0}])
    value, basis = engine._signal_walls(spoof, 120.0)
    assert value is None and basis["reason"] == "no_persistent_walls"
    # A wall outside the 1.5% proximity reach carries zero weight.
    far = chain_payload(l3_orders=[
        {"side": "BUY", "price": 117.5, "notional_usd": 1e7,
         "persistence_sec": 400.0}])
    value, basis = engine._signal_walls(far, 120.0)
    assert value is None and basis["reason"] == "no_persistent_walls"


def test_consistency_signal_positive_when_consensus_above_mid():
    engine = DecisionChainEngine(clock=lambda: NOW)
    payload = chain_payload(crosscheck={
        "venue_prices": {"BINANCE": 120.0, "COINBASE": 120.06,
                         "HYPERLIQUID": 120.04},
        "mid_divergence_bps": 5.0, "oi_agreement": None})
    value, basis = engine._signal_consistency(payload, 120.0)
    consensus = (120.0 + 120.06 + 120.04) / 3.0
    expected = math.tanh(((consensus - 120.0) / 120.0 * 1e4) / 10.0)
    assert value == pytest.approx(expected, abs=1e-12)
    assert value > 0.0
    assert basis["consensus_price"] == pytest.approx(consensus)
    assert basis["mid_divergence_bps"] == 5.0


def test_consistency_signal_negative_and_fail_closed():
    engine = DecisionChainEngine(clock=lambda: NOW)
    below = chain_payload(crosscheck={
        "venue_prices": {"BINANCE": 120.0, "COINBASE": 119.9},
        "mid_divergence_bps": 8.3, "oi_agreement": None})
    value, _ = engine._signal_consistency(below, 120.0)
    assert value < 0.0
    # One venue only: fail closed.
    lone = chain_payload(crosscheck={
        "venue_prices": {"BINANCE": 120.0}, "oi_agreement": None})
    value, basis = engine._signal_consistency(lone, 120.0)
    assert value is None and basis["reason"] == "insufficient_venues"
    # Cross-source OI disagreement: the divergence cannot be trusted.
    disagree = chain_payload(crosscheck={
        "venue_prices": {"BINANCE": 120.0, "COINBASE": 120.06},
        "oi_agreement": {"pass": False, "disagreement": 0.9}})
    value, basis = engine._signal_consistency(disagree, 120.0)
    assert value is None and basis["reason"] == "oi_disagreement"


# --------------------------------------------------- 3. weights and manifest
def test_weight_renormalization_with_single_pillar():
    """Only orderflow available: conviction collapses to its exact value."""
    engine = DecisionChainEngine(clock=lambda: NOW)
    of = {"taker_buy_usd_15m": 900.0, "taker_sell_usd_15m": 100.0,
          "taker_ratio_15m": 0.8, "cvd_1m": 5e5, "cvd_5m": 5e5, "cvd_15m": 5e5,
          "spread_bps": 1.7}
    payload = chain_payload(orderflow=of)
    advisory = engine.evaluate("SOL", payload, features(), None, NOW)
    orderflow_value = advisory["signals"]["orderflow"]["value"]
    assert advisory["signals"]["orderflow"]["available"] is True
    available = [name for name, sig in advisory["signals"].items()
                 if sig["available"]]
    assert available == ["orderflow"]
    assert advisory["conviction"] == pytest.approx(orderflow_value, abs=1e-9)


def test_pillar_manifest_complete_and_inside_digest():
    engine = DecisionChainEngine(clock=lambda: NOW)
    payload = chain_payload(
        orderflow={"taker_buy_usd_15m": 900.0, "taker_sell_usd_15m": 100.0,
                   "taker_ratio_15m": 0.8, "cvd_1m": 1e5, "cvd_5m": 1e5,
                   "cvd_15m": 1e5, "spread_bps": 1.7},
        l3_orders=[{"side": "BUY", "price": 119.9, "notional_usd": 6e6,
                    "persistence_sec": 300.0}],
        crosscheck={"venue_prices": {"BINANCE": 120.0, "COINBASE": 120.05},
                    "mid_divergence_bps": 4.2, "oi_agreement": None})
    advisory = engine.evaluate("SOL", payload, features(), macro_block(), NOW)
    assert advisory["policy_version"] == DECISION_CHAIN_VERSION
    pillars = advisory["pillars"]
    assert sorted(pillars) == [
        "P1_RECONSTRUCTED_LIQUIDATIONS", "P2A_STOP_CLUSTERS",
        "P2B_WHALE_WALL_PERSISTENCE", "P3_ONCHAIN_WHALE_FLOWS",
        "P4_FARSIDE_ETF_FLOWS", "P5_SENTIMENT_COINBASE_PREMIUM",
        "P6_CROSS_SOURCE_CONSISTENCY"]
    assert pillars["P2B_WHALE_WALL_PERSISTENCE"]["available"] is False
    assert pillars["P6_CROSS_SOURCE_CONSISTENCY"]["available"] is True
    assert pillars["P1_RECONSTRUCTED_LIQUIDATIONS"]["available"] is False
    # The manifest is stamped INSIDE the digest: recompute the chain hash
    # over the advisory minus the digest and it must match exactly.
    import hashlib
    core = {k: v for k, v in advisory.items() if k != "digest"}
    rebuilt = hashlib.sha256(
        ("genesis" + "|" + json.dumps(core, sort_keys=True,
                                      separators=(",", ":"), default=str))
        .encode("utf-8")).hexdigest()
    assert advisory["digest"] == rebuilt


def test_synthetic_signals_cannot_make_all_pillars_available():
    engine = DecisionChainEngine(clock=lambda: NOW)
    payload = chain_payload(
        orderflow={"taker_buy_usd_15m": 900.0, "taker_sell_usd_15m": 100.0,
                   "taker_ratio_15m": 0.8, "cvd_1m": 1e5, "cvd_5m": 1e5,
                   "cvd_15m": 1e5, "spread_bps": 1.7},
        projected_liquidations={"bands": [
            {"mid_px": 121.0, "amount_usd": 6e6, "position_side_at_risk": "SHORT"}]},
        observed_stops={"bands": [
            {"mid_px": 121.0, "amount_usd": 4e6, "position_side_at_risk": "SHORT"}]},
        whale_positions=[{"size": 1.0, "notional_usd": 4e6}],
        whale_net_flow_usd_24h=5e5,
        l3_orders=[{"side": "BUY", "price": 119.9, "notional_usd": 6e6,
                    "persistence_sec": 300.0}],
        crosscheck={"venue_prices": {"BINANCE": 120.0, "COINBASE": 120.05},
                    "mid_divergence_bps": 4.2, "oi_agreement": None})
    advisory = engine.evaluate("SOL", payload, features(), macro_block(), NOW)
    assert len(advisory["signals"]) == 7
    for name in ("cascade", "stops", "walls"):
        assert advisory["signals"][name]["available"] is False
    assert advisory["pillars"]["P1_RECONSTRUCTED_LIQUIDATIONS"]["available"] is False


# --------------------------------------------------- 5. full-chain integration
def test_full_chain_factory_validator_to_advisory():
    factory = feed_factory()
    validator = CrossSourceValidator(factory)
    validator.record_oi("SOL", "BINANCE", NOW, 10_000_000)
    validator.record_oi("SOL", "HYPERLIQUID", NOW, 10_400_000)   # 4% apart: pass
    engine = DecisionChainEngine(validator=validator, clock=lambda: NOW)
    # Walls accumulate persistence only under CONTINUOUS observation (a gap
    # > 30 s resets the cluster - the anti-spoof design). The brain's 15 s
    # tick cadence grows these clusters past the 180 s floor:
    payload = None
    for tick in range(int(NOW - 400), int(NOW) + 1, 15):
        payload = factory.payload("SOL", tick)
    assert payload["l3_orders"] == []  # anonymous aggregated L2 is not wallet L3
    assert payload["l2_wall_levels"]
    advisory = engine.evaluate("SOL", payload, features(),
                               macro_block(), NOW)
    assert advisory["policy_version"] == DECISION_CHAIN_VERSION
    # The validator enriched the payload with the pillar-6 block.
    assert advisory["signals"]["consistency"]["available"] is True
    assert advisory["signals"]["walls"]["available"] is False
    assert advisory["signals"]["orderflow"]["available"] is True
    assert advisory["pillars"]["P6_CROSS_SOURCE_CONSISTENCY"][
        "quality_score"] == advisory["quality_score"]
    # Bids 80k x 20 levels outweigh asks 50k x 20 at equal proximity:
    # net bid support from the resting walls.
    assert advisory["signals"]["walls"]["value"] is None


def test_engine_without_validator_leaves_consistency_unavailable():
    factory = feed_factory()
    engine = DecisionChainEngine(clock=lambda: NOW)
    advisory = engine.evaluate("SOL", factory.payload("SOL", NOW),
                               features(), None, NOW)
    assert advisory["signals"]["consistency"]["available"] is False
    assert advisory["signals"]["consistency"]["reason"] == "insufficient_venues"


# --------------------------------------------------- 6. inherited guarantees
def test_fail_closed_gates_inherited():
    engine = DecisionChainEngine(clock=lambda: NOW)
    stale = engine.evaluate("SOL", chain_payload(), features(book_as_of=NOW - 999),
                            None, NOW)
    assert stale["reason"] == "book_stale" and not stale["tradeable"]
    blackout = engine.evaluate("SOL", chain_payload(), features(),
                               {"blackout_active": True,
                                "blackout_event": "FOMC_MINUTES"}, NOW)
    assert blackout["reason"] == "macro_blackout"
    low_quality = DecisionChainEngine(
        quality_provider=lambda asset: {"quality_score": 0.30},
        clock=lambda: NOW)
    refused = low_quality.evaluate("SOL", chain_payload(), features(), None, NOW)
    assert refused["reason"].startswith("quality_below_floor")


def test_friction_floor_and_veto_only_tradeability():
    engine = DecisionChainEngine(clock=lambda: NOW)
    payload = chain_payload(
        orderflow={"taker_buy_usd_15m": 100.0, "taker_sell_usd_15m": 900.0,
                   "taker_ratio_15m": -0.8, "cvd_1m": -1e5, "cvd_5m": -1e5,
                   "cvd_15m": -1e5, "spread_bps": 2.0})
    advisory = engine.evaluate("SOL", payload, features(direction="LONG"),
                               None, NOW)
    # 41 bps mandatory + 5 bps slip + 2 bps live spread.
    assert advisory["min_favorable_move_bps"] == pytest.approx(48.0)
    assert advisory["advice"] == "SUPPORT_SHORT"
    assert advisory["tradeable"] is False          # veto-only: opposes LONG
    assert advisory["reason"].startswith("opposed_conviction")


def test_digest_chain_and_determinism():
    payload = chain_payload(
        orderflow={"taker_buy_usd_15m": 900.0, "taker_sell_usd_15m": 100.0,
                   "taker_ratio_15m": 0.8, "cvd_1m": 1e5, "cvd_5m": 1e5,
                   "cvd_15m": 1e5, "spread_bps": 1.7},
        l3_orders=[{"side": "BUY", "price": 119.9, "notional_usd": 6e6,
                    "persistence_sec": 300.0}])
    # Two fresh engines, identical inputs -> byte-identical advisories.
    first = DecisionChainEngine(clock=lambda: NOW).evaluate(
        "SOL", copy.deepcopy(payload), features(), macro_block(), NOW)
    second = DecisionChainEngine(clock=lambda: NOW).evaluate(
        "SOL", copy.deepcopy(payload), features(), macro_block(), NOW)
    assert json.dumps(first, sort_keys=True, default=str) == \
        json.dumps(second, sort_keys=True, default=str)
    # Same engine twice -> the digest CHAINS (tamper-evident sequence).
    engine = DecisionChainEngine(clock=lambda: NOW)
    a = engine.evaluate("SOL", copy.deepcopy(payload), features(), None, NOW)
    b = engine.evaluate("SOL", copy.deepcopy(payload), features(), None, NOW)
    assert a["digest"] != b["digest"]


def test_policy_weights_sum_and_scales():
    policy = DecisionChainPolicy()
    assert policy.version == DECISION_CHAIN_VERSION
    assert sum(policy.weights.values()) == pytest.approx(1.0)
    assert policy.wall_min_persistence_sec == 180.0
    assert policy.consistency_min_venues == 2
