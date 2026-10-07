"""Tests for OX_ALPHA_61: the hybrid "Arena Brain + laptop muscle" link.

100% offline and deterministic:

  D1  remote command protocol: HMAC signing, nonce replay ledger, timestamp
      window, idempotency; the polling reconciler (Pathway C) applying,
      refusing, isolating failures and purging; the signed HTTP command
      endpoints (Pathway A) over a real socket.
  D2  the ARENA:TEST_LIMIT_v1 protocol: Wilder ATR stops, the 10.00 USD risk
      cap, non-crossing enforcement, the 24-bar auto-purge, capacity guard.
  D3  the tri-specialist deliberation contract and its synthesis into the
      Pioneer conviction + llm_contract attestation.
  D4  the taker-delta exhaustion gate and the adaptive volatility stop buffer
      (the ETH stop-out fix), wired into the real trader.
"""
import asyncio
import json
import math

import pytest

from Terminal.Execution.remote_reconciler import (PROTOCOL_VERSION, TEST_LIMIT_COMMENT,
                                                  TEST_LIMIT_MAX_BARS, TEST_LIMIT_RISK_CAP_USD,
                                                  new_command, sign_command, verify_command,
                                                  apply_command, purge_expired_test_limits,
                                                  plan_test_limit, wilder_atr,
                                                  RemoteCommandReconciler, gist_fetch,
                                                  reconciler_from_env)
from Terminal.Execution.paper import PaperSimulatedBridge
from Terminal.Orderbook_Structure import taker_delta_exhaustion, adaptive_stop_level
from Terminal.Headless.swarm import (orderflow_analyst, position_manager,
                                     macro_risk_analyst, deliberate,
                                     build_brain_request, HARD_FLOOR_USD, MAX_CONCURRENT)
from Terminal.Headless.llm_contract import validate_consultation_response

NOW = 1_760_000_000.0
SECRET = "arena-test-secret-0x61"


# ============================================== D1: command protocol
def _signed(type_, params, *, nonce=None, ts=NOW, command_id=None, secret=SECRET):
    command = new_command(type_, params, nonce=nonce, ts=ts)
    if command_id:
        command["command_id"] = command_id
    return sign_command(command, secret)


def test_command_signature_tamper_window_and_type_guards():
    command = _signed("PURGE_TEST_LIMITS", {})
    assert verify_command(command, SECRET, now=NOW)["ok"]
    # Tampered params break the signature.
    tampered = {**command, "params": {"evil": True}}
    assert verify_command(tampered, SECRET, now=NOW)["reason"] == "bad_signature"
    # Wrong secret, missing signature, stale/future timestamps.
    assert verify_command(command, "other", now=NOW)["reason"] == "bad_signature"
    assert verify_command({k: v for k, v in command.items() if k != "signature"},
                          SECRET, now=NOW)["reason"] == "missing_signature"
    assert verify_command(command, SECRET, now=NOW + 60)["reason"] == "outside_replay_window"
    assert verify_command(command, SECRET, now=NOW - 60)["reason"] == "outside_replay_window"
    # Unknown command type refused even when properly signed.
    assert verify_command(_signed("STEAL_FUNDS", {}), SECRET, now=NOW)["reason"] \
        == "unknown_command_type"


def test_nonce_replay_and_idempotency_ledgers():
    command = _signed("PURGE_TEST_LIMITS", {}, nonce="nonce-1", command_id="cmd-1")
    seen, applied = set(), set()
    verdict = verify_command(command, SECRET, now=NOW, seen_nonces=seen,
                             applied_ids=applied)
    assert verdict["ok"]
    applied.add("cmd-1")                      # the caller marks it applied
    # Same nonce again (replay capture): refused.
    replayed = _signed("PURGE_TEST_LIMITS", {}, nonce="nonce-1", command_id="cmd-2")
    assert verify_command(replayed, SECRET, now=NOW, seen_nonces=seen,
                          applied_ids=applied)["reason"] == "nonce_replayed"
    # Fresh nonce but already-applied command id (store re-delivery): no-op.
    redelivered = _signed("PURGE_TEST_LIMITS", {}, nonce="nonce-2", command_id="cmd-1")
    assert verify_command(redelivered, SECRET, now=NOW, seen_nonces=seen,
                          applied_ids=applied)["reason"] == "command_already_applied"


def test_reconciler_applies_once_and_refuses_bad_signatures():
    bridge = PaperSimulatedBridge(clock=lambda: NOW)
    bridge.set_price("XAUUSD.pi", 4175.99, 4176.01, ts=NOW)
    store = {"commands": []}

    def fetch():
        return list(store["commands"])

    journal = []
    reconciler = RemoteCommandReconciler(bridge, secret=SECRET, fetch=fetch,
                                         clock=lambda: NOW,
                                         journal=lambda name, rec: journal.append(rec))
    good = _signed("STAGE_TEST_LIMIT", {"symbol": "XAUUSD.pi", "direction": "SHORT",
                                        "limit_price": 4182.00, "volume": 0.01,
                                        "atr": 4.1})
    bad = _signed("STAGE_TEST_LIMIT", {"symbol": "XAUUSD.pi", "direction": "SHORT",
                                       "limit_price": 4182.00, "volume": 0.01,
                                       "atr": 4.1}, secret="wrong-secret")
    store["commands"] = [good, bad]
    results = reconciler.poll_once()
    assert len(results) == 1 and results[0]["type"] == "STAGE_TEST_LIMIT"
    pending = bridge.get_pending_orders()
    assert len(pending) == 1 and pending[0]["comment"] == TEST_LIMIT_COMMENT
    assert pending[0]["price_open"] == pytest.approx(4182.00)
    assert pending[0]["sl"] == pytest.approx(4182.00 + 1.5 * 4.1)      # Wilder stop
    assert any(r["event"] == "command_refused" and r["reason"] == "bad_signature"
               for r in journal)
    # Re-delivery of the same store: idempotent, no second order.
    assert reconciler.poll_once() == []
    assert len(bridge.get_pending_orders()) == 1
    assert reconciler.stats["applied"] == 1 and reconciler.stats["refused"] >= 2


def test_reconciler_survives_a_dead_store():
    def fetch():
        raise OSError("gist unreachable")

    journal = []
    reconciler = RemoteCommandReconciler(PaperSimulatedBridge(clock=lambda: NOW),
                                         secret=SECRET, fetch=fetch, clock=lambda: NOW,
                                         journal=lambda name, rec: journal.append(rec))
    assert reconciler.poll_once() == []                 # error isolated, loop lives
    assert reconciler.stats["errors"] == 1
    assert any(r["event"] == "fetch_error" for r in journal)


def test_stage_order_endpoint_over_http_with_signature_and_replay():
    from Terminal.Headless.server import HeadlessService
    from Terminal.Headless.server import canonical_json as cj

    class Runtime:
        def __init__(self, bridge):
            self.bridge = bridge
        def readiness(self):
            return True, []
        def evaluate_candle(self, force=False):
            return {"decision": "HOLD"}

    bridge = PaperSimulatedBridge(clock=lambda: NOW)
    bridge.set_price("XAUUSD.pi", 4175.99, 4176.01, ts=NOW)
    service = HeadlessService(Runtime(bridge), host="127.0.0.1", port=0,
                              secret=SECRET, clock=lambda: NOW)

    async def request(path, body):
        reader, writer = await asyncio.open_connection("127.0.0.1", service._bound_port)
        raw = cj(body)
        writer.write(("POST " + path + " HTTP/1.1\r\nHost: x\r\nContent-Length: "
                      + str(len(raw)) + "\r\nConnection: close\r\n\r\n").encode() + raw)
        await writer.drain()
        response = b""
        while True:
            chunk = await reader.read(4096)
            if not chunk:
                break
            response += chunk
        writer.close()
        head, _, body_out = response.partition(b"\r\n\r\n")
        status = int(head.split(b"\r\n")[0].decode().split()[1])
        return status, json.loads(body_out or b"{}")

    async def scenario():
        server = await service.serve()
        service._bound_port = server.sockets[0].getsockname()[1]
        command = _signed("STAGE_TEST_LIMIT", {"symbol": "XAUUSD.pi", "direction": "SHORT",
                                               "limit_price": 4182.00, "volume": 0.01,
                                               "atr": 4.1})
        status, body = await request("/api/v1/stage_order", command)
        assert status == 200 and body["type"] == "STAGE_TEST_LIMIT"
        assert body["result"]["comment"] == TEST_LIMIT_COMMENT
        ticket = body["result"]["ticket"]
        # Unsigned request: refused.
        status, body = await request("/api/v1/stage_order",
                                     new_command("STAGE_TEST_LIMIT", {}))
        assert status == 401 and body["error"] == "missing_signature"
        # Replayed nonce: refused.
        status, body = await request("/api/v1/stage_order", command)
        assert status == 401 and body["error"] == "nonce_replayed"
        # modify_sltp is a first-class signed route (it acts on POSITIONS -
        # open one on a second symbol, capacity is still 2).
        bridge.set_price("ETHUSD.pi", 2690.00, 2690.50, ts=NOW)
        position = bridge.execute_market_order("ETHUSD.pi", "LONG", 0.01, 2680.0, 2700.0)
        assert position["success"]
        modify = _signed("MODIFY_SLTP", {"ticket": position["ticket"], "sl": 2685.00})
        status, body = await request("/api/v1/modify_sltp", modify)
        assert status == 200 and body["result"]["success"]
        assert bridge.get_open_positions(symbol="ETHUSD.pi")[0]["sl"] == 2685.00
        # A risk-violating order is a 409 refusal, never a silent stage.
        fat = _signed("STAGE_TEST_LIMIT", {"symbol": "XAUUSD.pi", "direction": "SHORT",
                                           "limit_price": 4182.00, "volume": 0.05,
                                           "atr": 9.0})
        status, body = await request("/api/v1/stage_order", fat)
        assert status == 409 and "test_limit_risk_cap_exceeded" in body["error"]
        server.close()

    asyncio.run(scenario())


# ============================================== D2: test-limit protocol
def test_wilder_atr_matches_hand_computed_smoothing():
    bars = []
    price = 100.0
    for i in range(20):
        bars.append({"time": NOW - (20 - i) * 900, "open": price, "high": price + 2.0,
                     "low": price, "close": price})
    assert wilder_atr(bars, period=14) == pytest.approx(2.0)     # constant TR
    assert wilder_atr(bars[:10], period=14) is None              # not enough bars
    # A single range expansion lifts the smoothed ATR but is damped by Wilder.
    bars[15] = {"time": bars[15]["time"], "open": price, "high": price + 16.0,
                "low": price, "close": price}
    assert 2.0 < wilder_atr(bars, period=14) < 4.0


def test_plan_test_limit_enforces_the_10_usd_cap_and_atr_geometry():
    plan = plan_test_limit(direction="SHORT", limit_price=4182.00, volume=0.01, atr=4.1)
    assert plan["sl"] == pytest.approx(4182.00 + 1.5 * 4.1)      # Wilder stop
    assert plan["tp"] == pytest.approx(4182.00 - 3.75 * 4.1)     # 2.50R target (3.75 ATR)
    assert (plan["sl"] - plan["limit_price"]) * 2.5 == pytest.approx(plan["limit_price"] - plan["tp"])
    assert plan["risk_usd"] == pytest.approx(0.01 * 100 * 1.5 * 4.1)
    assert plan["risk_usd"] <= TEST_LIMIT_RISK_CAP_USD
    assert plan["comment"] == TEST_LIMIT_COMMENT
    assert plan["expires_after_bars"] == TEST_LIMIT_MAX_BARS
    # A stop too wide for min lots breaches the cap: fail-closed.
    with pytest.raises(ValueError, match="test_limit_risk_cap_exceeded"):
        plan_test_limit(direction="SHORT", limit_price=4182.00, volume=0.01, atr=9.0)
    with pytest.raises(ValueError):
        plan_test_limit(direction="SIDEWAYS", limit_price=4182.00, volume=0.01, atr=4.0)
    with pytest.raises(ValueError):
        plan_test_limit(direction="LONG", limit_price=4182.00, volume=0.01, atr=0.0)


def test_test_limit_refuses_to_cross_the_market():
    bridge = PaperSimulatedBridge(clock=lambda: NOW)
    bridge.set_price("XAUUSD.pi", 4175.99, 4176.01, ts=NOW)
    crossing = _signed("STAGE_TEST_LIMIT", {"symbol": "XAUUSD.pi", "direction": "SHORT",
                                            "limit_price": 4170.00, "volume": 0.01,
                                            "atr": 4.0})
    with pytest.raises(ValueError, match="sell_limit_crosses_market"):
        apply_command(bridge, crossing, clock=lambda: NOW)
    buy_crossing = _signed("STAGE_TEST_LIMIT", {"symbol": "XAUUSD.pi", "direction": "LONG",
                                                "limit_price": 4180.00, "volume": 0.01,
                                                "atr": 4.0})
    with pytest.raises(ValueError, match="buy_limit_crosses_market"):
        apply_command(bridge, buy_crossing, clock=lambda: NOW)
    assert bridge.get_pending_orders() == []


def test_test_limit_auto_purges_after_24_bars_but_not_before():
    clock = {"t": NOW}
    bridge = PaperSimulatedBridge(clock=lambda: clock["t"])
    bridge.set_price("XAUUSD.pi", 4175.99, 4176.01, ts=NOW)
    command = _signed("STAGE_TEST_LIMIT", {"symbol": "XAUUSD.pi", "direction": "SHORT",
                                           "limit_price": 4182.00, "volume": 0.01,
                                           "atr": 4.1})
    result = apply_command(bridge, command, clock=lambda: clock["t"])
    assert result["success"] and result["expires_at"] == pytest.approx(NOW + 24 * 900)
    # 5 hours in: still resting.
    clock["t"] = NOW + 5 * 3600
    assert purge_expired_test_limits(bridge, clock=lambda: clock["t"]) == []
    assert len(bridge.get_pending_orders()) == 1
    # 6 hours + 1s: purged automatically.
    clock["t"] = NOW + 24 * 900 + 1
    purged = purge_expired_test_limits(bridge, clock=lambda: clock["t"])
    assert len(purged) == 1 and purged[0]["ticket"] == result["ticket"]
    assert bridge.get_pending_orders() == []


def test_capacity_guard_respects_max_concurrent_two():
    bridge = PaperSimulatedBridge(clock=lambda: NOW)
    bridge.set_price("XAUUSD.pi", 4175.99, 4176.01, ts=NOW)
    bridge.set_price("ETHUSD.pi", 2690.0, 2690.5, ts=NOW)
    for symbol in ("ETHUSD.pi", "SOLUSD.p"):
        bridge.set_price(symbol, 100.0, 100.5, ts=NOW)
        bridge.execute_market_order(symbol, "LONG", 0.01, 99.0, 101.0)
    assert len(bridge.get_open_positions()) == MAX_CONCURRENT
    command = _signed("STAGE_TEST_LIMIT", {"symbol": "XAUUSD.pi", "direction": "SHORT",
                                           "limit_price": 4182.00, "volume": 0.01,
                                           "atr": 4.1})
    with pytest.raises(ValueError, match="max_concurrent_positions_reached"):
        apply_command(bridge, command, clock=lambda: NOW)


# ============================================== D3: deliberation contract
def _sample_payload():
    return {"coin": "SOL", "price": 120.0,
            "orderflow": {"cvd_1m": 120_000.0, "cvd_5m": -500_000.0, "cvd_15m": -1_200_000.0,
                          "taker_buy_usd_1m": 400_000.0, "taker_sell_usd_1m": 280_000.0,
                          "taker_buy_usd_5m": 1_500_000.0, "taker_sell_usd_5m": 2_000_000.0,
                          "depth_imbalance": 0.35},
            "l3_orders": [{"side": "BUY", "price": 119.40, "notional_usd": 4_930_000.0,
                           "persistence_sec": 2400.0, "observed_at": NOW},
                          {"side": "SELL", "price": 122.34, "notional_usd": 8_040_000.0,
                           "persistence_sec": 300.0, "observed_at": NOW},
                          {"side": "BUY", "price": 119.0, "notional_usd": 900_000.0,
                           "persistence_sec": 40.0, "observed_at": NOW}]}


def test_orderflow_analyst_reads_tape_book_and_persistent_walls():
    perspective = orderflow_analyst(_sample_payload())
    assert perspective["available"] and perspective["perspective"] == "ORDERFLOW"
    # The 900k wall persisting only 40s is EXCLUDED (needs >= 180s).
    assert any("bid_usd=4930000" in d for d in perspective["drivers"])
    assert -1.0 <= perspective["conviction"] <= 1.0
    # No tape at all: honestly unavailable.
    empty = orderflow_analyst({"l3_orders": []})
    assert empty["available"] is False and empty["conviction"] == 0.0


def test_position_manager_tracks_r_phases_and_capacity():
    gold = {"ticket": 18576872, "symbol": "XAUUSD.pi", "direction": "SHORT",
            "price_open": 4176.00, "sl": 4186.50, "tp": 4143.00,
            "current_price": 4171.37, "volume": 0.01, "contract_size": 100.0,
            "profit_usd": 4.63}
    perspective = position_manager([gold])
    # SHORT from 4176.00, initial R = 10.50, price 4171.37 -> +0.44R: OPEN phase.
    assert perspective["filled"] == 1 and perspective["capacity_open"]
    assert any("gain_r=0.44" in d for d in perspective["drivers"])
    # Deep in profit: the phase label advances.
    runner = dict(gold, current_price=4155.0)
    assert any("phase=RUNNER" in d for d in position_manager([runner])["drivers"])
    # Capacity: two filled positions blocks new risk.
    assert position_manager([gold, dict(gold, ticket=2)])["capacity_open"] is False
    # Already holding the same asset: conviction zeroed.
    assert position_manager([gold], asset="XAUUSD")["conviction"] == 0.0


def test_macro_analyst_blocks_on_blackout_and_thin_cushion():
    blocked = macro_risk_analyst({"blackout_active": True})
    assert blocked["blocked"] and blocked["conviction"] == 0.0
    thin = macro_risk_analyst({"asset_scores": {"SOL": 1.0}}, equity_usd=4800.0)
    assert not thin["blocked"] and thin["cushion_usd"] == pytest.approx(25.0)
    healthy = macro_risk_analyst({"asset_scores": {"SOL": 1.0}}, equity_usd=4837.78)
    assert healthy["conviction"] > 0
    below_floor = macro_risk_analyst({}, equity_usd=4770.0)
    assert below_floor["blocked"]


def test_deliberation_fuses_into_pioneer_and_attests_via_llm_contract():
    payload = _sample_payload()
    positions = [{"ticket": 18576872, "symbol": "XAUUSD.pi", "direction": "SHORT",
                  "price_open": 4176.00, "sl": 4186.50, "current_price": 4171.37,
                  "volume": 0.01, "contract_size": 100.0}]
    macro = {"blackout_active": False, "asset_scores": {"SOL": 0.8, "GOLD": 0.2}}
    record = deliberate(payload, positions, macro, equity_usd=4837.78)
    assert [p["perspective"] for p in record["perspectives"]] == \
        ["ORDERFLOW", "POSITIONS", "MACRO"]
    assert not record["blocked"] and record["capacity_open"]
    assert record["synthesis"]["weights"] == {"orderflow": 0.30, "cascade": 0.25,
                                              "stops": 0.15, "whale": 0.15, "macro": 0.15}
    # The full brain request carries the llm_contract consultation envelope...
    request = build_brain_request(as_of=NOW, asset="SOL", payload=payload,
                                  features={"direction": "LONG", "confluence": 0.9,
                                            "pioneer": {"digest": "d1"}},
                                  pioneer={"conviction": 0.4, "advice": "SUPPORT_LONG",
                                           "digest": "d1"},
                                  candidate={"candidate_id": "s:SOL:LONG", "direction": "LONG",
                                             "price_open": 119.42, "sl": 117.92, "tp": 122.32,
                                             "hurdle_r": 2.4, "risk_usd": 15.0,
                                             "sizing": {"risk_usd": 15.0}},
                                  positions=positions, macro=macro, equity_usd=4837.78)
    consultation = request["consultation"]
    # ...and a clean SELECT passes the zero-hallucination validator.
    response = {"action": "SELECT", "candidate_id": "s:SOL:LONG", "risk_usd": 15.0,
                "sl": 117.92, "tp": 122.32,
                "rationale_summary": "Exhausted sellers into persistent bid walls.",
                "support_refs": ["/deliberation/perspectives/0"],
                "invalidation_refs": ["/candidate/sl"],
                "invariant_digest": consultation["invariant_digest"]}
    ok, violations = validate_consultation_response(consultation, response)
    assert ok, violations
    # A moved stop is rejected.
    bad = dict(response, sl=117.00)
    ok, violations = validate_consultation_response(consultation, bad)
    assert not ok and any(v.startswith("sl_not_echoed") for v in violations)


# ============================================== D4: exhaustion + stop buffer
def test_exhaustion_gate_requires_deceleration_and_absorption():
    pressing = {"cvd_1m": -40_000.0, "cvd_5m": -500_000.0,           # pace fading
                "taker_buy_usd_1m": 300_000.0, "taker_sell_usd_1m": 340_000.0,
                "taker_buy_usd_5m": 1_200_000.0, "taker_sell_usd_5m": 1_700_000.0}
    gate = taker_delta_exhaustion(pressing, "LONG")
    assert gate["status"] == "ENFORCED" and gate["ok"], gate["reasons"]
    # Still pressing hard: the 1m pace matches the 5m average -> veto.
    still_selling = dict(pressing, cvd_1m=-150_000.0)
    gate = taker_delta_exhaustion(still_selling, "LONG")
    assert not gate["ok"] and "seller_pressure_not_decelerating" in gate["reasons"]
    # Deceleration but no buyers lifting: no absorption -> veto.
    no_absorption = dict(pressing, taker_buy_usd_1m=5_000.0)
    gate = taker_delta_exhaustion(no_absorption, "LONG")
    assert not gate["ok"] and "insufficient_buy_absorption_at_support" in gate["reasons"]
    # No 5m selling at all: nothing to exhaust -> veto (no setup).
    drift = dict(pressing, cvd_5m=50_000.0)
    gate = taker_delta_exhaustion(drift, "LONG")
    assert not gate["ok"] and "no_seller_pressure_to_exhaust" in gate["reasons"]
    # Mirrored SHORT case.
    short_ok = {"cvd_1m": 40_000.0, "cvd_5m": 500_000.0,
                "taker_buy_usd_1m": 340_000.0, "taker_sell_usd_1m": 300_000.0,
                "taker_buy_usd_5m": 1_700_000.0, "taker_sell_usd_5m": 1_200_000.0}
    assert taker_delta_exhaustion(short_ok, "SHORT")["ok"]
    # Missing tape: UNVERIFIED (caller policy decides).
    assert taker_delta_exhaustion(None, "LONG")["status"] == "UNVERIFIED_NO_TAPE"


def test_adaptive_stop_buffer_protects_the_structural_swing():
    # Swing 1.0 ATR below entry: buffered stop = swing - 0.2 ATR, distance 1.2
    # ATR < 1.5 ATR floor -> the floor wins.
    assert adaptive_stop_level(120.0, 1.0, 119.0, "LONG") == pytest.approx(118.5)
    # Swing 1.8 ATR below entry: buffered distance 2.0 ATR > floor -> buffer wins.
    assert adaptive_stop_level(120.0, 1.0, 118.2, "LONG") == pytest.approx(118.0)
    # ETH regression shape: the stop sits BELOW swing low - 0.2 ATR, so the
    # sweep that took the swing (wick to swing - 0.1 ATR) cannot take the stop.
    entry, atr, swing = 2695.50, 6.3, 2690.0
    stop = adaptive_stop_level(entry, atr, swing, "LONG")
    assert stop <= swing - 0.2 * atr + 1e-9
    wick = swing - 0.1 * atr
    assert stop < wick < entry
    # No swing data: pure volatility floor.
    assert adaptive_stop_level(120.0, 1.0, None, "LONG") == pytest.approx(118.5)
    # Mirrored SHORT.
    assert adaptive_stop_level(120.0, 1.0, 121.8, "SHORT") == pytest.approx(122.0)
    assert adaptive_stop_level(120.0, 0.0, 119.0, "LONG") is None


def test_trader_vetoes_limit_entry_while_sellers_still_press():
    """The real trader, limit mode: an S1 pullback with sellers still pressing
    is refused; the same geometry with an exhausted, absorbed tape stages."""
    from Terminal.Omni_Trader import AI15mMT5Trader, MAGIC
    from Terminal.Asset_Universe import UNIVERSE
    from Terminal.Risk_Sizing_Engine import CovarianceGate
    import numpy as np

    slot = (NOW // 900) * 900 + 870

    def bars(now=slot, count=96, mid=120.0):
        start = int(now // 900) * 900 - count * 900
        return [{"time": start + i * 900, "open": mid + 0.05 * math.sin(0.9 * i),
                 "high": mid + 0.55, "low": mid - 0.55,
                 "close": mid + 0.05 * math.sin(0.9 * i)} for i in range(count)]

    class OfflineIntel:
        def check_macro_blackout(self): return False, "NO_EVENT", 999
        def get_market_intelligence_report(self):
            return {"asset_scores": {a: 1 for a in UNIVERSE}, "sentiment_valid": True}

    def make(tmp_path):
        bridge = PaperSimulatedBridge(clock=lambda: slot)
        bridge.set_price("SOLUSD", 119.99, 120.01, ts=slot)
        covariance = CovarianceGate(UNIVERSE, np.eye(len(UNIVERSE)) * 0.003 ** 2,
                                    {"return_units": "decimal_log_return",
                                     "horizon_minutes": 15, "created_at": slot - 60,
                                     "data_end": slot - 900, "max_age_seconds": 86400})
        trader = AI15mMT5Trader(bridge=bridge, covariance=covariance, intel=OfflineIntel(),
                                cognitive=object(), cognitive_enabled=False,
                                uplift_path=tmp_path / "no_uplift", clock=lambda: slot,
                                paper_mode=False, entry_mode="limit",
                                state_file=tmp_path / "state.json",
                                journal_dir=tmp_path / "journal")
        trader.symbols = {a: bridge.resolve_symbol(a) for a in UNIVERSE}
        trader.bars = {a: bars() for a in UNIVERSE}
        return trader, bridge

    def payload(orderflow):
        return {"coin": "SOL", "price": 120.0,
                "l2_book": {"timestamp": slot * 1000, "best_bid": 119.99, "best_ask": 120.01,
                            "bids": [{"price": 119.99 - i * 0.01, "size": 10000}
                                     for i in range(20)],
                            "asks": [{"price": 120.01 + i * 0.01, "size": 100}
                                     for i in range(20)]},
                "recent_trades": [{"time": slot * 1000, "side": "SELL", "price": 120.0,
                                   "size": 100, "notional_usd": 10000},
                                  {"time": slot * 1000, "side": "BUY", "price": 120.0,
                                   "size": 100, "notional_usd": 10000}],
                "sources": {"l3": {"observed_at": slot},
                            "liquidations": {"observed_at": slot}},
                "l3_orders": [], "liquidations": {}, "orderflow": orderflow}

    macro = {"received_at": slot, "sentiment_valid": True, "asset_scores": {"SOL": 1}}

    still_pressing = {"cvd_1m": -150_000.0, "cvd_5m": -500_000.0,
                      "taker_buy_usd_1m": 300_000.0, "taker_sell_usd_1m": 450_000.0,
                      "taker_buy_usd_5m": 1_200_000.0, "taker_sell_usd_5m": 1_700_000.0}
    trader, _ = make(pytest.active_tmp / "veto")
    result = trader.evaluate_market({"SOL": payload(still_pressing)}, macro)
    assert result["decision"] == "HOLD"
    assert "exhaustion_gate:seller_pressure_not_decelerating" in result["vetoes"]["SOL"]

    exhausted = {"cvd_1m": -40_000.0, "cvd_5m": -500_000.0,
                 "taker_buy_usd_1m": 300_000.0, "taker_sell_usd_1m": 340_000.0,
                 "taker_buy_usd_5m": 1_200_000.0, "taker_sell_usd_5m": 1_700_000.0}
    trader, bridge = make(pytest.active_tmp / "pass")
    result = trader.evaluate_market({"SOL": payload(exhausted)}, macro)
    assert result["decision"] == "LIMIT_STAGED", result
    pending = bridge.get_pending_orders()
    assert len(pending) == 1 and pending[0]["magic"] == MAGIC
    # The staged stop honours the adaptive buffer: >= 1.5 ATR from entry.
    position_sl = pending[0]["sl"]
    assert pending[0]["price_open"] - position_sl >= 1.5 * 1.0 - 0.02


@pytest.fixture(scope="module", autouse=True)
def _shared_tmp(tmp_path_factory):
    pytest.active_tmp = tmp_path_factory.mktemp("arena")
    yield


# ============================================== follow-up hardening
def test_manage_cadence_purges_stale_test_limits(tmp_path):
    """Pathway-A-only deployments still purge: the trader's ~1s manage
    cadence scans for expired ARENA:TEST_LIMIT_v1 orders (throttled 5 min)."""
    from Terminal.Omni_Trader import AI15mMT5Trader
    from Terminal.Asset_Universe import UNIVERSE
    from Terminal.Risk_Sizing_Engine import CovarianceGate
    import numpy as np

    clock = {"t": NOW}

    class OfflineIntel:
        def check_macro_blackout(self): return False, "NO_EVENT", 999
        def get_market_intelligence_report(self):
            return {"asset_scores": {a: 1 for a in UNIVERSE}, "sentiment_valid": True}

    bridge = PaperSimulatedBridge(clock=lambda: clock["t"])
    bridge.set_price("XAUUSD.pi", 4175.99, 4176.01, ts=NOW)
    covariance = CovarianceGate(UNIVERSE, np.eye(len(UNIVERSE)) * 0.003 ** 2,
                                {"return_units": "decimal_log_return",
                                 "horizon_minutes": 15, "created_at": NOW - 60,
                                 "data_end": NOW - 900, "max_age_seconds": 86400})
    trader = AI15mMT5Trader(bridge=bridge, covariance=covariance, intel=OfflineIntel(),
                            cognitive=object(), cognitive_enabled=False,
                            uplift_path=tmp_path / "no_uplift", clock=lambda: clock["t"],
                            paper_mode=False, entry_mode="limit",
                            state_file=tmp_path / "state.json",
                            journal_dir=tmp_path / "journal")
    stale = _signed("STAGE_TEST_LIMIT", {"symbol": "XAUUSD.pi", "direction": "SHORT",
                                         "limit_price": 4182.00, "volume": 0.01,
                                         "atr": 4.1})
    assert apply_command(bridge, stale, clock=lambda: clock["t"])["success"]
    # 6 hours + 1s later, joint-fill defense refuses a second correlated
    # order until the stale order is *actually* purged from broker inventory.
    clock["t"] = NOW + 24 * 900 + 1
    fresh = _signed("STAGE_TEST_LIMIT", {"symbol": "XAUUSD.pi", "direction": "SHORT",
                                         "limit_price": 4185.00, "volume": 0.01,
                                         "atr": 4.1})
    with pytest.raises(ValueError, match="correlated_joint_fill"):
        apply_command(bridge, fresh, clock=lambda: clock["t"])
    trader.manage_active_positions()
    assert bridge.get_pending_orders() == []
    assert apply_command(bridge, fresh, clock=lambda: clock["t"])["success"]
    pending = bridge.get_pending_orders()
    assert len(pending) == 1 and pending[0]["price_open"] == pytest.approx(4185.00)
    # The throttle holds: an immediate second call is a no-op (fresh survives).
    trader.manage_active_positions()
    assert len(bridge.get_pending_orders()) == 1


def test_reconciler_from_env_is_fail_closed(monkeypatch, tmp_path):
    # Missing configuration: refuses to build.
    with pytest.raises(ValueError, match="reconciler_requires"):
        reconciler_from_env(environ={})
    # Paper fallback allowed: builds on the deterministic paper bridge.
    for var in ("EXECUTION_BACKEND", "METAAPI_TOKEN", "METAAPI_ACCOUNT_ID"):
        monkeypatch.delenv(var, raising=False)
    monkeypatch.setattr("Terminal.Execution.base._native_available", lambda: False)
    monkeypatch.setenv("OMNI_ALLOW_PAPER", "1")
    monkeypatch.setenv("ARENA_COMMANDS_URL", "https://gist.example/raw/arena_commands.json")
    monkeypatch.setenv("OMNI_API_SECRET", SECRET)
    monkeypatch.setenv("ARENA_POLL_INTERVAL", "3")
    reconciler = reconciler_from_env()
    assert isinstance(reconciler.bridge, PaperSimulatedBridge)
    assert reconciler.secret == SECRET and reconciler.poll_interval == 3.0
    # Paper fallback disallowed and no MT5 terminal here: fail-closed.
    monkeypatch.setenv("OMNI_ALLOW_PAPER", "0")
    from Terminal.Execution import NoExecutionBackend
    with pytest.raises(NoExecutionBackend):
        reconciler_from_env()


def test_status_endpoint_and_runtime_status(tmp_path):
    from Terminal.Headless.server import HeadlessService, sign_payload, canonical_json
    from Terminal.Headless.runtime import HeadlessRuntime

    # Runtime composition: bridge + fresh book -> ready, no balances exposed.
    class Factory:
        def __init__(self):
            self.bus = self
        def book(self, asset):
            return {"ts": NOW - 2}
        def payload(self, asset, now=None):
            return {"coin": asset}

    runtime = HeadlessRuntime(assets=["SOL"],
                              bridge=PaperSimulatedBridge(clock=lambda: NOW),
                              factory=Factory(), clock=lambda: NOW)
    status = runtime.status()
    assert status["ready"] and status["bridge"]["backend"] == "paper"
    assert status["bridge"]["healthy"] is True
    assert "balance" not in status and "equity" not in status
    assert status["last_evaluation"] is None

    class Runtime:
        def __init__(self, status_payload):
            self.status_payload = status_payload
        def readiness(self):
            return True, []
        def evaluate_candle(self, force=False):
            return {"decision": "HOLD"}
        def status(self):
            return self.status_payload

    service = HeadlessService(Runtime(status), host="127.0.0.1", port=0,
                              secret=SECRET, clock=lambda: NOW)

    async def request(body, headers):
        reader, writer = await asyncio.open_connection("127.0.0.1", service._bound_port)
        raw = canonical_json(body)
        lines = ["POST /api/v1/status HTTP/1.1", "Host: x",
                 f"Content-Length: {len(raw)}", "Connection: close"]
        for key, value in (headers or {}).items():
            lines.append(f"{key}: {value}")
        writer.write(("\r\n".join(lines) + "\r\n\r\n").encode() + raw)
        await writer.drain()
        response = b""
        while True:
            chunk = await reader.read(4096)
            if not chunk:
                break
            response += chunk
        writer.close()
        head, _, body_out = response.partition(b"\r\n\r\n")
        return int(head.split(b"\r\n")[0].decode().split()[1]), json.loads(body_out or b"{}")

    async def scenario():
        server = await service.serve()
        service._bound_port = server.sockets[0].getsockname()[1]
        # Unsigned: refused.
        status_code, body = await request({}, None)
        assert status_code == 401 and body["error"] == "invalid_signature"
        # Signed: the muscle reports in.
        envelope = sign_payload({}, SECRET, ts=NOW)
        status_code, body = await request({}, {"X-Signature": envelope["signature"],
                                               "X-Signature-Ts": f"{envelope['ts']:.3f}"})
        assert status_code == 200 and body["ready"] and body["bridge"]["backend"] == "paper"
        server.close()

    asyncio.run(scenario())
