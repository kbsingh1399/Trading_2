"""Forensic hardening tests for the 2026-10-06 incident remediations.

Covers: dynamic TTL governor (Incident A), sealed deterministic features and
numeric attestation (Incident B), orderbook-aware structural exits and sleeve
decoupling (Incident C), and the execution-chain race fixes (F-02/F-03/F-04).
All tests run offline with fake bridges; nothing touches a terminal.
"""
import copy
import json
import math
import pathlib
from types import SimpleNamespace

import pytest

from Terminal.Asset_Universe import UNIVERSE
from Terminal.Cognitive_Engine import CognitiveEngine, DECISION_SCHEMA
from Terminal.Deterministic_Features import (FeatureSealer, seal_vector, verify_seal,
                                             attest_decision, extract_numeric_claims, SEAL_KEYS)
from Terminal.Orderbook_Structure import (wall_clusters, hazard_ttl, structural_exit,
                                          classify_sleeve, anchors_from_clusters, wall_liveness)
from Terminal.Order_Persistence_Governor import OrderPersistenceGovernor
from Terminal.Omni_Trader import AI15mMT5Trader, MAGIC
from Terminal.Risk_Sizing_Engine import RiskPolicy, CovarianceGate, OrderflowModel

NOW = (1700000000 // 900) * 900 + 870


def bars(now=NOW, count=96, trend=0.0, mid=120.0):
    """Deterministic bars pinned to the instrument price level (ATR = 1.00)."""
    start = int(now // 900) * 900 - count * 900
    out = []
    for i in range(count):
        close = mid + trend * i + 0.05 * math.sin(0.9 * i)
        out.append({"time": start + i * 900, "open": close, "high": close + 0.5,
                    "low": close - 0.5, "close": close})
    return out


def payload(now=NOW, asset="SOL", reverse=False, l3=None, liquidations=None, mid=120.0):
    return {"coin": asset, "price": mid, "l2_book": {"timestamp": now * 1000, "best_bid": mid - 0.01,
            "best_ask": mid + 0.01, "bids": [{"price": mid - 0.01 - i * 0.01, "size": 10000 if not reverse else 100} for i in range(20)],
            "asks": [{"price": mid + 0.01 + i * 0.01, "size": 100 if not reverse else 10000} for i in range(20)]},
            "recent_trades": [{"time": now * 1000, "side": "SELL" if reverse else "BUY", "price": mid, "size": 100, "notional_usd": 10000},
                              {"time": now * 1000, "side": "BUY", "price": mid, "size": 100, "notional_usd": 10000}],
            "sources": {"l3": {"observed_at": now, "provider": "HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT"},
                        "liquidations": {"observed_at": now},
                        "wallet_risk": {"observed_at": now, "coverage": "SAMPLED_WALLETS",
                                        "provider": "HYPERLIQUID_PUBLIC_INFO"}},
            "observed_stops": {"kind": "OBSERVED_STOP_ORDERS", "coverage": "SAMPLED_WALLETS",
                "wallets": ["0xtest"], "bands": [
                    {"kind": "OBSERVED_STOP_ORDERS", "address": "0xtest", "position_side_at_risk": "LONG",
                     "min_px": mid - 0.10, "max_px": mid - 0.10, "mid_px": mid - 0.10, "amount_usd": 1e7},
                    {"kind": "OBSERVED_STOP_ORDERS", "address": "0xtest", "position_side_at_risk": "SHORT",
                     "min_px": mid + 0.10, "max_px": mid + 0.10, "mid_px": mid + 0.10, "amount_usd": 1e7}]},
            "l3_orders": l3 or [], "liquidations": liquidations or {}}


def covariance(now=NOW, assets=UNIVERSE, sigma=0.003):
    import numpy as np
    matrix = np.eye(len(assets)) * sigma ** 2
    return CovarianceGate(assets, matrix, {"return_units": "decimal_log_return", "horizon_minutes": 15,
                                           "created_at": now - 60, "data_end": now - 900, "max_age_seconds": 86400})


class Broker:
    """Offline broker double: paper fills, live staging, scripted history."""

    def __init__(self, clock, mid=120.0):
        self.clock = clock; self.positions = []; self.pending = []; self.modified = []
        self.closed = []; self.sent = []; self.mid = mid
        self.history_state = None; self.filled = False

    def get_open_positions(self): return copy.deepcopy(self.positions)
    def get_pending_orders(self): return copy.deepcopy(self.pending)
    def get_account_summary(self): return {"connected": True, "login": 1, "currency": "USD",
                                           "equity_usd": 5000, "margin_free_usd": 5000}
    def resolve_symbol(self, asset): return asset + "USD" if asset not in ("GOLD", "SILVER") else "XAUUSD"
    def get_recent_bars(self, symbol, count=96): return bars(self.clock())
    def get_symbol_price(self, symbol):
        return {"bid": self.mid - 0.01, "ask": self.mid + 0.01, "point": .01, "tick_size": .01,
                "time_msc": self.clock() * 1000, "digits": 2, "contract_size": 100, "min_lot": .01,
                "step_lot": .01, "max_lot": 10, "stops_level": 0, "freeze_level": 0, "currency_profit": "USD"}
    def estimate_order(self, symbol, direction, entry, sl): return {"stop_loss_per_lot": abs(entry - sl) * 100, "margin_per_lot": 1000}
    def modify_position_sltp(self, ticket, sl, tp): self.modified.append((ticket, sl, tp)); return {"success": True}
    def close_position(self, ticket): self.closed.append(ticket); return {"success": True}
    def position_deals(self, ticket): return []
    def execute_market_order(self, *a, **k): self.sent.append(("market", a, k)); return {"success": False, "uncertain": True}
    def stage_limit_order(self, symbol, direction, volume, limit_price, sl, tp, **kwargs):
        ticket = 1000 + len(self.sent)
        order = {"ticket": ticket, "symbol": symbol, "direction": direction, "volume": volume,
                 "price_open": limit_price, "sl": sl, "tp": tp, "magic": kwargs.get("magic", MAGIC)}
        self.pending.append(order); self.sent.append(("limit", order, kwargs))
        return {"success": True, "ticket": ticket, "symbol": symbol, "direction": direction,
                "volume": volume, "price": limit_price, "sl": sl, "tp": tp,
                "persistent": kwargs.get("persistent", False), "expires_at": None}
    def cancel_pending_order(self, ticket):
        self.pending = [o for o in self.pending if o["ticket"] != ticket]
        self.closed.append(f"cancel_{ticket}")
        return {"success": True, "ticket": ticket}
    def reconcile_intent_history(self, comment, prepared_at):
        return self.history_state
    def intent_filled(self, comment, prepared_at):
        return self.filled


class Intel:
    def check_macro_blackout(self): return False, "NO_EVENT", 999
    def get_market_intelligence_report(self): return {"asset_scores": {a: 1 for a in UNIVERSE}, "sentiment_valid": True}


def trader(tmp_path, clock=None, paper=True, mid=120.0, entry_mode="limit"):
    clock = clock or (lambda: NOW)
    broker = Broker(clock, mid=mid)
    t = AI15mMT5Trader(bridge=broker, intel=Intel(), cognitive=object(), covariance=covariance(),
                       uplift_path=tmp_path / "no_uplift", cognitive_enabled=False, clock=clock,
                       paper_mode=paper, state_file=tmp_path / "state.json",
                       journal_dir=tmp_path / "journal", entry_mode=entry_mode)
    t.symbols = {a: broker.resolve_symbol(a) for a in UNIVERSE}
    t.bars = {a: bars(clock()) for a in UNIVERSE}
    return t, broker


# ============================================================ Incident A: TTL
def test_hazard_ttl_matches_survival_model_and_band():
    # TTL = -ln(0.35) * (span + 1800s prior), clipped to [2h, 6h].
    assert hazard_ttl(0) == pytest.approx(7200.0)                          # clipped up to the floor
    assert hazard_ttl(3600) == pytest.approx(7200.0)                       # 1.0498*5400 = 5669s -> floor
    assert hazard_ttl(7200) == pytest.approx(-math.log(0.35) * 9000)       # inside the band
    assert hazard_ttl(6 * 3600) == pytest.approx(21600.0)                  # 1.0498*23400 -> capped
    assert hazard_ttl(3600, ttl_min_sec=60, ttl_max_sec=300) == pytest.approx(300.0)
    with pytest.raises(ValueError):
        hazard_ttl(100, survival_target=1.5)


def test_governor_renews_ttl_while_anchor_persists():
    events = []
    bridge = Broker(lambda: NOW)
    gov = OrderPersistenceGovernor(bridge, journal=lambda n, r: events.append(r), clock=lambda: NOW)
    anchors = [{"price": 119.41, "notional_usd": 4.93e6, "persistence_sec": 3600, "role": "primary"}]
    gov.register("k", asset="SOL", symbol="SOLUSD", direction="LONG", order_ticket=1000,
                 limit_price=119.42, sl=117.42, tp=125.42, volume=0.5, anchors=anchors,
                 atr=1.2, ttl_sec=hazard_ttl(3600), now=NOW, comment="OMNI:k", hurdle_r=2.5)
    wall = [{"side": "BUY", "price": 119.41, "notional_usd": 4.93e6, "persistence_sec": 6000,
             "observed_at": NOW}]
    data = payload(NOW, l3=wall)
    intents = {"k": {"status": "STAGED_LIMIT"}}
    pending = [{"ticket": 1000, "symbol": "SOLUSD"}]
    gov.heartbeat(now=NOW + 60, intents=intents, payloads={"SOL": data}, pending=pending,
                  quote_fn=lambda s: {"bid": 119.99, "ask": 120.01})
    assert not bridge.closed and gov.count() == 1
    # Monotone renewal: deadline extended toward now + TTL(6000s span).
    renewed = gov.orders["k"]["deadline"]
    assert renewed >= NOW + 60 + hazard_ttl(6000) - 1e-6
    assert renewed <= gov.orders["k"]["hard_deadline"]


def test_governor_cancels_when_whale_support_is_pulled():
    bridge = Broker(lambda: NOW)
    events = []
    gov = OrderPersistenceGovernor(bridge, journal=lambda n, r: events.append(r), clock=lambda: NOW)
    anchors = [{"price": 119.41, "notional_usd": 4.93e6, "persistence_sec": 3600, "role": "primary"}]
    gov.register("k", asset="SOL", symbol="SOLUSD", direction="LONG", order_ticket=1000,
                 limit_price=119.42, sl=117.42, tp=125.42, volume=0.5, anchors=anchors,
                 atr=1.2, ttl_sec=7200, now=NOW, comment="OMNI:k", hurdle_r=2.5)
    # Wall vanished from the book entirely.
    data = payload(NOW, l3=[])
    gov.heartbeat(now=NOW + 60, intents={"k": {"status": "STAGED_LIMIT"}},
                  payloads={"SOL": data}, pending=[{"ticket": 1000, "symbol": "SOLUSD"}],
                  quote_fn=lambda s: {"bid": 119.99, "ask": 120.01})
    assert bridge.closed == ["cancel_1000"] and gov.count() == 0
    cancel_event = next(e for e in events if e["event"] == "governor_cancel")
    assert cancel_event["reason"] == "anchor_wall_pulled"


def test_governor_cancel_replaces_onto_shifted_wall_preserving_risk_geometry():
    bridge = Broker(lambda: NOW)
    bridge.sent.append("seed")  # keep replacement ticket != 1000
    gov = OrderPersistenceGovernor(bridge, journal=lambda n, r: None, clock=lambda: NOW)
    anchors = [{"price": 119.41, "notional_usd": 4.93e6, "persistence_sec": 3600, "role": "primary"}]
    gov.register("k", asset="SOL", symbol="SOLUSD", direction="LONG", order_ticket=1000,
                 limit_price=119.42, sl=117.42, tp=125.42, volume=0.5, anchors=anchors,
                 atr=1.2, ttl_sec=7200, now=NOW, comment="OMNI:k", hurdle_r=2.5, risk_usd=20.0)
    # Old wall pulled; an institutional wall re-posted 18 bps lower.
    shifted = [{"side": "BUY", "price": 119.20, "notional_usd": 3.5e6, "persistence_sec": 1200,
                "observed_at": NOW}]
    gov.heartbeat(now=NOW + 60, intents={"k": {"status": "STAGED_LIMIT"}},
                  payloads={"SOL": payload(NOW, l3=shifted)}, pending=[{"ticket": 1000, "symbol": "SOLUSD"}],
                  quote_fn=lambda s: {"bid": 119.99, "ask": 120.01})
    assert bridge.closed == ["cancel_1000"]
    replacement = next(o for o in bridge.pending if o["ticket"] != 1000)
    assert replacement["price_open"] == pytest.approx(119.21)          # new edge + 1 tick
    assert replacement["sl"] == pytest.approx(119.21 - 2.0)            # R-geometry preserved
    assert replacement["tp"] == pytest.approx(119.21 + 2.5 * 2.0)
    assert replacement["volume"] == 0.5                                 # risk invariant
    assert gov.orders["k"]["recenters"] == 1


def test_governor_never_replaces_after_uncertain_cancel():
    class UncertainBridge(Broker):
        def cancel_pending_order(self, ticket):
            self.closed.append(f"cancel_{ticket}")
            return {"success": False, "uncertain": True, "error": "timeout"}
    bridge = UncertainBridge(lambda: NOW)
    gov = OrderPersistenceGovernor(bridge, journal=lambda n, r: None, clock=lambda: NOW)
    anchors = [{"price": 119.41, "notional_usd": 4.93e6, "persistence_sec": 3600, "role": "primary"}]
    gov.register("k", asset="SOL", symbol="SOLUSD", direction="LONG", order_ticket=1000,
                 limit_price=119.42, sl=117.42, tp=125.42, volume=0.5, anchors=anchors,
                 atr=1.2, ttl_sec=7200, now=NOW, comment="OMNI:k", hurdle_r=2.5)
    shifted = [{"side": "BUY", "price": 119.20, "notional_usd": 3.5e6, "persistence_sec": 1200, "observed_at": NOW}]
    gov.heartbeat(now=NOW + 60, intents={"k": {"status": "STAGED_LIMIT"}},
                  payloads={"SOL": payload(NOW, l3=shifted)}, pending=[{"ticket": 1000, "symbol": "SOLUSD"}],
                  quote_fn=lambda s: {"bid": 119.99, "ask": 120.01})
    # No second order staged while the cancel is ambiguous: fill-race safety.
    assert not [o for o in bridge.pending if o["ticket"] != 1000]
    assert gov.orders["k"]["cancel_uncertain_at"] == NOW + 60
    # The retry path cancels again on the next beat and then resolves.
    bridge.__class__.cancel_pending_order = Broker.cancel_pending_order
    gov.heartbeat(now=NOW + 70, intents={"k": {"status": "STAGED_LIMIT"}},
                  payloads={"SOL": payload(NOW, l3=shifted)}, pending=[{"ticket": 1000, "symbol": "SOLUSD"}],
                  quote_fn=lambda s: {"bid": 119.99, "ask": 120.01})
    assert gov.count() == 0


def test_governor_ttl_deadline_is_enforced():
    bridge = Broker(lambda: NOW)
    gov = OrderPersistenceGovernor(bridge, journal=lambda n, r: None, clock=lambda: NOW)
    anchors = [{"price": 119.41, "notional_usd": 4.93e6, "persistence_sec": 3600, "role": "primary"}]
    gov.register("k", asset="SOL", symbol="SOLUSD", direction="LONG", order_ticket=1000,
                 limit_price=119.42, sl=117.42, tp=125.42, volume=0.5, anchors=anchors,
                 atr=1.2, ttl_sec=7200, now=NOW, comment="OMNI:k", hurdle_r=2.5)
    gov.orders["k"]["deadline"] = NOW - 1
    data = payload(NOW, l3=[{"side": "BUY", "price": 119.41, "notional_usd": 4.93e6,
                             "persistence_sec": 6000, "observed_at": NOW}])
    changes = gov.heartbeat(now=NOW, intents={"k": {"status": "STAGED_LIMIT"}},
                            payloads={"SOL": data}, pending=[{"ticket": 1000, "symbol": "SOLUSD"}],
                            quote_fn=lambda s: {"bid": 119.99, "ask": 120.01})
    assert bridge.closed == ["cancel_1000"]
    assert changes[0]["reason"] == "ttl_expired"


# =================================================== Incident B: sealed truth
def test_incident_b_exact_hallucination_is_rejected(tmp_path):
    engine = CognitiveEngine(ledger_path=tmp_path / "ledger.jsonl")
    features = {"as_of": NOW, "direction": "LONG", "sleeve": "S1_PULLBACK", "signal_mid": 120.84,
                "aggressor_robust_z": 0.92, "l2_imbalance": 0.31, "confluence": 0.62,
                "quality": 0.9, "atr": 1.31, "friction_bps": 41.0, "sigma_h": 0.011,
                "efficiency_ratio": 0.22, "aggressor_imbalance": 0.18, "wall_imbalance": 0.44,
                "liquidation_delta": -0.21, "macro_score": 0.4, "target_fuel": 0.8,
                "opposing_magnet": 0.0, "ffr": 1.4, "friction_adjusted_fuel_ratio": 0.9,
                "risk_intent_usd": 18.0, "l2_robust_z": 0.4, "wall_imbalance_robust_z": 1.1}
    walls = [{"side": "SELL", "price": 122.34, "notional_usd": 8_040_000, "observed_span_s": 2100,
              "observed_at": NOW}]
    snapshot = engine.build_snapshot("SOL", "SOLUSD.p", 120.84, features, walls, [],
                                     {"score": 0.4, "blackout": False}, {"equity": 4841.23, "slots": 2}, {},
                                     sealed=seal_vector(features, None))
    decision = {k: None for k in DECISION_SCHEMA["required"]}
    decision.update(snapshot_id=snapshot["snapshot_id"], action="HOLD", candidate_id=None,
                    analyst_thesis=("CVD divergence is only +0.92 standard deviations and an "
                                    "8.04M USD sell wall sits at 122.34; friction is 41 bps."),
                    critic_objection="The reclaim lacks confirmation above 122.34.",
                    rationale_summary="Hold: the 8.04M wall caps the target.",
                    support_refs=["/walls/0/visible_notional_usd"], counter_refs=[], invalidation_refs=[])
    assert CognitiveEngine.validate_decision(snapshot, decision)
    ok, violations = attest_decision(snapshot, decision)
    assert ok, violations

    # The exact Incident B fabrication: +1.8 sigma and an "empty" book above 122.00.
    fabricated = dict(decision)
    fabricated.update(analyst_thesis=("CVD divergence is +1.8 standard deviations and the ask book "
                                      "above 122.00 is empty."),
                      rationale_summary="Momentum continuation expected.")
    ok, violations = attest_decision(snapshot, fabricated)
    assert not ok
    flagged = {v["raw"].lstrip("+-") for v in violations}
    assert "1.8" in flagged and "122.00" in flagged


def test_attestation_scientific_notation_is_one_claim_not_exempt():
    """Forensics round 3: '3e5' used to parse as exempt integer 3; '1.2e-4'
    as 1.2. Exponent literals must attest as their full magnitudes."""
    snap = {"econometrics": {"notional": 300000.0, "sigma": 0.00012}}
    ok_true, _ = attest_decision(snap, {"rationale_summary": "fuel of 3e5 USD"})
    assert ok_true
    ok_true2, _ = attest_decision(snap, {"rationale_summary": "sigma 1.2e-4"})
    assert ok_true2
    snap_wrong = {"econometrics": {"notional": 42.0, "sigma": 0.00012}}
    rejected, _ = attest_decision(snap_wrong, {"rationale_summary": "fuel of 3e5 USD"})
    assert not rejected


def test_numeric_claim_extraction_handles_suffixes_and_percent():
    claims = extract_numeric_claims("8.04M wall, +1.8 sigma, 5.2% spread, 41 bps, 122.34, 2 hours")
    values = {c["raw"]: c["value"] for c in claims}
    assert values["8.04"] == pytest.approx(8.04e6)     # M suffix scales the value
    assert values["+1.8"] == pytest.approx(1.8)
    assert values["5.2"] == pytest.approx(0.052)       # percent scaled to fraction
    assert values["41"] == pytest.approx(41)
    assert values["122.34"] == pytest.approx(122.34)
    assert values["2"] == pytest.approx(2)             # exempt ordinal, still extracted


def test_seals_are_deterministic_chain_linked_and_tamper_evident():
    base = {"as_of": NOW, "signal_mid": 120.84, "sigma_h": 0.011, "atr": 1.31,
            "efficiency_ratio": 0.22, "l2_imbalance": 0.31, "l2_robust_z": 0.4,
            "aggressor_imbalance": 0.18, "aggressor_robust_z": 0.92, "wall_imbalance": 0.44,
            "wall_imbalance_robust_z": 1.1, "liquidation_delta": -0.21, "macro_score": 0.4,
            "confluence": 0.62, "quality": 0.9, "target_fuel": 0.8, "opposing_magnet": 0.0,
            "ffr": 1.4, "friction_adjusted_fuel_ratio": 0.9, "friction_bps": 41.0,
            "risk_intent_usd": 18.0}
    a = seal_vector(base, None)
    b = seal_vector(base, None)
    assert a["digest"] == b["digest"]                      # deterministic
    sealer = FeatureSealer()
    first = sealer.update("SOL", base)
    second = sealer.update("SOL", base)
    assert first["chain_digest"] != second["chain_digest"]  # chain advances
    assert second["prev_digest"] == first["chain_digest"]
    assert verify_seal(first)
    tampered = copy.deepcopy(first)
    tampered["values"]["aggressor_robust_z"] = 1.8          # retro-edit attempt
    assert not verify_seal(tampered)
    assert set(SEAL_KEYS) == set(first["values"])


def test_cognitive_engine_rejects_fabricated_decision_end_to_end(monkeypatch, tmp_path):
    import requests as requests_module
    engine = CognitiveEngine(ledger_path=tmp_path / "ledger.jsonl")
    features = {"as_of": NOW, "direction": "LONG", "signal_mid": 120.84, "aggressor_robust_z": 0.92,
                "confluence": 0.62, "quality": 0.9, "atr": 1.31, "friction_bps": 41.0}
    sealed = seal_vector(features, None)
    snapshot = engine.build_snapshot("SOL", "SOLUSD.p", 120.84, features, [], [], {"score": 0.4},
                                     {"equity": 4841.23, "slots": 2}, {}, sealed=sealed)
    decision = {k: None for k in DECISION_SCHEMA["required"]}
    decision.update(snapshot_id=snapshot["snapshot_id"], action="HOLD",
                    analyst_thesis="Divergence is +1.8 standard deviations.",
                    critic_objection="c", rationale_summary="r",
                    support_refs=["/portfolio/equity_usd"], counter_refs=[], invalidation_refs=[])
    response = SimpleNamespace(status_code=200, json=lambda: {"choices": [{"message": {"content": json.dumps(decision)}}]})
    monkeypatch.setattr(requests_module, "post", lambda *a, **k: response)
    assert engine.evaluate_snapshot(snapshot, "LONG", budget_seconds=1.0) is None
    ledger = (tmp_path / "ledger.jsonl").read_text().strip().splitlines()
    rejection = json.loads(ledger[-1])
    assert rejection["event"] == "cognitive_fabrication_rejection"
    assert any(v["raw"].lstrip("+-") == "1.8" for v in rejection["violations"])


# ============================================= Incident C: structural exits
def test_structural_tp_front_runs_first_major_overhead_wall():
    entry, sl = 120.84, 118.84   # r = 2.0
    wall = [{"edge_price": 124.50, "notional_usd": 8.04e6, "persistence_sec": 900}]
    plan, veto = structural_exit(entry, sl, "LONG", wall, tick=0.01, friction_r=0.25)
    assert veto is None
    assert plan["mode"] == "wall_front_run"
    assert plan["tp"] == pytest.approx(124.48)               # 2 ticks below the wall edge
    assert 1.75 <= plan["hurdle_r"] < 2.50                   # dynamically depressed hurdle


def test_structural_tp_never_stages_beyond_band_cap_or_into_a_wall():
    entry, sl = 120.84, 118.84
    far_wall = [{"edge_price": 130.00, "notional_usd": 8.04e6}]   # beyond 2.75R
    plan, veto = structural_exit(entry, sl, "LONG", far_wall, tick=0.01, friction_r=0.25)
    assert veto is None and plan["mode"] == "ratchet_band"
    assert plan["tp"] == pytest.approx(125.84)              # 2.50R band target, inside the wall
    plan, veto = structural_exit(entry, sl, "LONG", [], tick=0.01, friction_r=0.25)
    assert veto is None and plan["tp"] == pytest.approx(125.84)


def test_structural_tp_vetoes_when_wall_sits_inside_net_payoff_floor():
    # The 8.04M wall at 122.34 with a 2.0R stop leaves ~0.74R gross: vetoed.
    wall = [{"edge_price": 122.34, "notional_usd": 8.04e6}]
    plan, veto = structural_exit(120.84, 118.84, "LONG", wall, tick=0.01, friction_r=0.25)
    assert plan is None and "net_payoff_insufficient" in veto


def test_structural_tp_symmetric_for_shorts():
    entry, sl = 122.00, 124.00   # r = 2.0
    wall = [{"edge_price": 118.00, "notional_usd": 8.0e6}]
    plan, veto = structural_exit(entry, sl, "SHORT", wall, tick=0.02, friction_r=0.25)
    assert veto is None
    assert plan["tp"] == pytest.approx(118.04)              # 2 ticks above the bid-side wall
    assert plan["hurdle_r"] == pytest.approx(1.98, abs=1e-6)


def test_sleeve_decoupling_is_deterministic():
    assert classify_sleeve({"direction": "LONG", "liquidity_vacuum": True}) == "T1_BREAKOUT"
    assert classify_sleeve({"direction": "LONG", "liquidity_vacuum": False,
                            "efficiency_ratio": 0.5, "aggressor_imbalance": 0.6}) == "T1_BREAKOUT"
    assert classify_sleeve({"direction": "LONG", "liquidity_vacuum": False,
                            "efficiency_ratio": 0.5, "aggressor_imbalance": -0.6}) == "S1_PULLBACK"
    assert classify_sleeve({"direction": "SHORT", "liquidity_vacuum": False,
                            "efficiency_ratio": 0.1, "aggressor_imbalance": 0.9}) == "S1_PULLBACK"


def test_wall_clusters_enforce_freshness_thresholds_and_aggregate():
    walls = [{"side": "BUY", "price": 119.41, "notional_usd": 3.0e6, "persistence_sec": 600, "observed_at": NOW},
             {"side": "BUY", "price": 119.40, "notional_usd": 1.93e6, "persistence_sec": 400, "observed_at": NOW},
             {"side": "BUY", "price": 118.0, "notional_usd": 5.0e6, "persistence_sec": 60, "observed_at": NOW},
             {"side": "BUY", "price": 117.0, "notional_usd": 5.0e6, "persistence_sec": 600, "observed_at": NOW - 60},
             {"side": "SELL", "price": 119.42, "notional_usd": 5.0e6, "persistence_sec": 600, "observed_at": NOW}]
    clusters = wall_clusters(walls, "BUY", 115.0, 119.99, NOW)
    assert len(clusters) == 1                                  # aggregated, persistence/freshness filtered
    assert clusters[0]["edge_price"] == pytest.approx(119.41)
    assert clusters[0]["notional_usd"] == pytest.approx(4.93e6)  # the SOL anchor geometry
    assert clusters[0]["members"] == 2


def test_s1_pullback_stages_passive_limit_and_front_runs_overhead_wall(tmp_path):
    # SOL 2026-10-06 geometry: 4.93M bid wall at 119.41, 8.04M ask wall at 122.34.
    t, b = trader(tmp_path, mid=120.0, entry_mode="limit")
    walls = [{"side": "BUY", "price": 119.41, "notional_usd": 4.93e6, "persistence_sec": 600,
              "observed_at": NOW, "address": "0xabc"},
             {"side": "SELL", "price": 122.34, "notional_usd": 8.04e6, "persistence_sec": 300,
              "observed_at": NOW, "address": "0xabc"}]
    seed = payload(NOW - 10, l3=[dict(walls[0], observed_at=NOW - 10)])
    t.flow.observe_walls("SOL", seed, NOW - 10)  # second observation earns persistence credit
    data = payload(NOW, l3=walls)
    result = t.evaluate_market({"SOL": data}, {"received_at": NOW, "sentiment_valid": True,
                                               "asset_scores": {"SOL": 1}})
    assert result["decision"] == "PAPER_FILLED"
    pos = t.state["paper_positions"][0]
    assert pos["sleeve"] == "S1_PULLBACK"
    assert pos["price_open"] == pytest.approx(119.42)      # 1 tick above the whale edge
    assert pos["sl"] < pos["price_open"] < pos["tp"]
    assert pos["tp"] == pytest.approx(122.32)               # front-runs the 8.04M wall, never 123.00
    assert pos["tp"] < 122.34
    assert pos["hurdle_r"] < 2.5                            # hurdle depressed by the wall


def test_t1_breakout_routes_to_aggressive_market_entry(tmp_path):
    t, b = trader(tmp_path, mid=120.0, entry_mode="limit")
    trend_bars = bars(trend=0.2)      # efficiency ratio >= 0.35 with aligned tape
    t.bars = {a: trend_bars for a in UNIVERSE}
    data = payload(NOW)
    result = t.evaluate_market({"SOL": data}, {"received_at": NOW, "sentiment_valid": True,
                                               "asset_scores": {"SOL": 1}})
    assert result["decision"] == "PAPER_FILLED"
    pos = t.state["paper_positions"][0]
    assert pos["sleeve"] == "T1_BREAKOUT"
    assert pos["entry_mode"] == "market"                   # aggressive entry despite --entry-mode limit
    assert pos["price_open"] == pytest.approx(120.01)       # filled at the ask


# ================================= Execution-chain race fixes (F-02..F-04)
def test_vanished_limit_reconciles_fill_before_expiring(tmp_path):
    t, b = trader(tmp_path, paper=False)
    intent = {"status": "STAGED_LIMIT", "comment": "OMNI:x", "prepared_at": NOW - 60,
              "order_ticket": 777, "candidate": {"sl": 118.0, "risk_usd": 20.0, "initial_r": 2.0,
                                                  "price_open": 120.0}}
    t.state["intents"]["x"] = intent
    # Fill-and-closed inside the inventory race window: history proves it.
    b.history_state = {"state": "FILLED_CLOSED", "position_id": 42, "deals": [], "net_pnl_usd": 12.0}
    t._reconcile([], [])
    assert t.state["intents"]["x"]["status"] == "RECONCILED_CLOSED"
    # Fill-and-open: status moves to ACKNOWLEDGED, never EXPIRED.
    t2, b2 = trader(tmp_path, paper=False)
    t2.state["intents"]["x"] = {"status": "STAGED_LIMIT", "comment": "OMNI:x", "prepared_at": NOW - 60,
                                "order_ticket": 778, "candidate": {"sl": 118.0, "risk_usd": 20.0,
                                                                   "initial_r": 2.0, "price_open": 120.0}}
    b2.history_state = None; b2.filled = True
    t2._reconcile([], [])
    assert t2.state["intents"]["x"]["status"] == "ACKNOWLEDGED"
    # No fill evidence anywhere: genuine expiry.
    t3, b3 = trader(tmp_path, paper=False)
    t3.state["intents"]["x"] = {"status": "STAGED_LIMIT", "comment": "OMNI:x", "prepared_at": NOW - 60,
                                "order_ticket": 779, "candidate": {"sl": 118.0, "risk_usd": 20.0,
                                                                   "initial_r": 2.0, "price_open": 120.0}}
    b3.history_state = None; b3.filled = False
    t3._reconcile([], [])
    assert t3.state["intents"]["x"]["status"] == "EXPIRED"


def test_aged_unresolved_intent_no_longer_deadlocks_new_entries(tmp_path):
    t, b = trader(tmp_path, paper=False)
    t.state["intents"]["stuck"] = {"status": "UNCERTAIN", "comment": "OMNI:stuck",
                                   "prepared_at": NOW - 900, "candidate": {}}
    b.filled = False
    t._reconcile([], [])
    assert t.state["intents"]["stuck"]["status"] == "ABANDONED"
    now = [NOW + 900]
    t.clock = lambda: now[0]
    t.state["last_slot"] = int(NOW // 900)  # allow the next slot
    report = t.evaluate_market({"SOL": payload(now[0])}, {"received_at": now[0], "sentiment_valid": True,
                                                          "asset_scores": {"SOL": 1}})
    assert report.get("reason") != "unresolved_execution_intent"


def test_bridge_stages_persistent_gtc_limit(monkeypatch):
    from Terminal import MT5_Execution_Bridge as module
    sends = []
    info = SimpleNamespace(digits=2, point=.01, volume_step=.25, volume_min=.25, volume_max=10,
                           trade_stops_level=0, trade_freeze_level=0, trade_tick_size=.01)
    tick = SimpleNamespace(bid=100.0, ask=100.02, time_msc=int(NOW * 1000), time=int(NOW))
    def send(request): sends.append(copy.deepcopy(request)); return SimpleNamespace(retcode=10009, comment="ok", order=321, deal=0, volume=.25, price=99.90)
    fake = SimpleNamespace(terminal_info=lambda: SimpleNamespace(connected=True),
                           account_info=lambda: SimpleNamespace(login=1, trade_mode=0, company="Blueberry", currency="USD",
                                                                balance=5000.0, equity=5000.0, profit=0.0, margin=0.0,
                                                                margin_free=5000.0, margin_level=0.0),
                           positions_get=lambda *a: (), orders_get=lambda *a: (),
                           order_calc_profit=lambda *a: -48.0, order_calc_margin=lambda *a: 100.0,
                           symbol_select=lambda *a: True, symbol_info=lambda *a: info,
                           symbol_info_tick=lambda *a: tick,
                           order_check=lambda r: SimpleNamespace(retcode=0, comment="ok"),
                           order_send=send, last_error=lambda: (0, "fake"),
                           ORDER_TYPE_BUY=0, ORDER_TYPE_SELL=1, ORDER_TYPE_BUY_LIMIT=2,
                           TRADE_ACTION_PENDING=5, TRADE_ACTION_DEAL=1, ORDER_TIME_GTC=0,
                           ORDER_TIME_SPECIFIED=2, ORDER_FILLING_IOC=1, ORDER_FILLING_RETURN=2,
                           TRADE_RETCODE_DONE=10009, TRADE_RETCODE_PLACED=10008)
    monkeypatch.setattr(module, "mt5", fake)
    monkeypatch.setattr(module, "MT5_AVAILABLE", True)
    bridge = module.MT5ExecutionBridge()
    result = bridge.stage_limit_order("SOLUSD.p", "LONG", 0.25, 99.90, 97.90, 104.00,
                                      persistent=True, passive_only=True)
    assert result["success"] and result["persistent"] and result["expires_at"] is None
    assert sends[-1]["type_time"] == 0            # ORDER_TIME_GTC
    assert sends[-1]["expiration"] == 0           # no broker-side deadline


def test_features_include_incident_b_deterministic_statistics():
    model = OrderflowModel()
    f = model.features("SOL", payload(), bars(), {}, NOW)
    for key in ("aggressor_robust_z", "wall_imbalance_robust_z", "friction_adjusted_fuel_ratio",
                "friction_bps", "l2_robust_z"):
        assert key in f
    assert f["friction_bps"] == 41.0
    assert set(SEAL_KEYS) <= {k for k, v in f.items() if not isinstance(v, (list, dict))}
