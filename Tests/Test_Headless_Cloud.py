"""Tests for OX_ALPHA_60: headless cloud execution & desktop dependency
abstraction. 100% offline and deterministic:

  1. Execution package  - ABC contract, paper matching engine, headless REST
     gateway (injectable transport), fail-closed auto-discovery.
  2. Wall persistence   - resting whale walls need >=150k USD AND >=180s.
  3. CandleScheduler    - :14/:29/:44/:59 wakes with drift compensation.
  4. HeadlessService    - signed /healthz /readyz /api/v1/evaluate_candle over
     a real socket, HMAC verification, replay window, 401/404/400 paths.
  5. LLM contract       - SELECT/HOLD validation, exact numeric echoes,
     invariant digest, budget bounds, JSON-pointer resolution.
  6. HeadlessRuntime    - readiness fail-closed, evaluate_candle payloads,
     full-stack paper-bridge trade through the real Omni_Trader.
"""
import asyncio
import copy
import json
import math
import os
import time

import pytest

from Terminal.Execution import (BaseExecutionBridge, BridgeError, NoExecutionBackend,
                                create_bridge, available_backends,
                                NativeMT5Bridge, HeadlessRESTBridge, PaperSimulatedBridge)
from Terminal.Execution.paper import default_symbol_of, asset_of_symbol
from Terminal.Data_Factory import ZeroCostDataFactory
from Terminal.Headless.scheduler import CandleScheduler
from Terminal.Headless.server import (HeadlessService, sign_payload, verify_signed,
                                      canonical_json)
from Terminal.Headless.llm_contract import (build_consultation_request,
                                            validate_consultation_response,
                                            default_invariant_envelope, invariant_digest)
from Terminal.Headless.runtime import HeadlessRuntime

NOW = 1_760_000_000.0
SECRET = "test-secret-0xdeadbeef"


# ============================================== 1. Execution package
def test_every_backend_honours_the_base_contract():
    for cls in (NativeMT5Bridge, HeadlessRESTBridge, PaperSimulatedBridge):
        assert issubclass(cls, BaseExecutionBridge)
        for method in ("get_account_summary", "get_open_positions", "get_pending_orders",
                       "get_symbol_price", "stage_limit_order", "modify_position_sltp",
                       "cancel_pending_order", "cancel_order", "resolve_symbol",
                       "estimate_order", "execute_market_order", "close_position",
                       "position_deals", "reconcile_intent_history", "intent_filled",
                       "get_recent_bars", "health"):
            assert callable(getattr(cls, method, None)), (cls.__name__, method)
    assert set(available_backends()) >= {"native_mt5", "headless_rest", "paper"}


def test_paper_bridge_fills_resting_limits_when_price_crosses():
    bridge = PaperSimulatedBridge(clock=lambda: NOW)
    result = bridge.stage_limit_order("SOLUSD", "SHORT", 0.5, 122.00, 123.00, 120.00,
                                      comment="OMNI:t1", magic=100895)
    assert result["success"] and result["ticket"]
    assert bridge.get_pending_orders()[0]["price_open"] == 122.00
    bridge.on_tick("SOLUSD", 122.50)                    # bid 122.49 >= limit
    assert not any(o["comment"] == "OMNI:t1" for o in bridge.get_pending_orders())
    position = bridge.get_open_positions()[0]
    assert position["direction"] == "SHORT" and position["price_open"] == pytest.approx(122.49)
    # A BUY limit below the market rests until the ask trades through it.
    bridge.stage_limit_order("SOLUSD", "BUY", 0.5, 119.50, 118.50, 121.00, comment="OMNI:t2")   # BUY normalizes to LONG
    bridge.on_tick("SOLUSD", 119.60)
    assert any(o["comment"] == "OMNI:t2" for o in bridge.get_pending_orders())
    bridge.on_tick("SOLUSD", 119.40)                    # ask 119.41 <= 119.50
    position = [p for p in bridge.get_open_positions() if p["comment"] == "OMNI:t2"][0]
    assert position["price_open"] == pytest.approx(119.41)   # filled at limit or better


def test_paper_bridge_evaluates_sl_and_tp_on_bid_ask():
    bridge = PaperSimulatedBridge(clock=lambda: NOW)
    bridge.stage_limit_order("ETHUSD", "LONG", 0.85, 2695.50, 2686.00, 2725.00,
                             comment="OMNI:eth")
    bridge.on_tick("ETHUSD", 2695.40)
    assert len(bridge.get_open_positions()) == 1        # filled long
    bridge.on_tick("ETHUSD", 2686.05)                   # bid 2686.04 > SL: still alive
    assert len(bridge.get_open_positions()) == 1
    bridge.on_tick("ETHUSD", 2685.90)                   # bid through the stop
    assert not bridge.get_open_positions()
    deal = [d for d in bridge.deals if d["event"] == "stop_loss"][0]
    assert deal["price"] == pytest.approx(2686.00)      # server-side SL semantics
    assert deal["pnl_usd"] == pytest.approx((2686.00 - 2695.41) * 0.85 * 100, rel=1e-6)

    tp_bridge = PaperSimulatedBridge(clock=lambda: NOW)
    tp_bridge.stage_limit_order("ETHUSD", "LONG", 0.85, 2695.50, 2686.00, 2725.00)
    tp_bridge.on_tick("ETHUSD", 2695.40)
    tp_bridge.on_tick("ETHUSD", 2725.10)                # bid through the target
    deal = [d for d in tp_bridge.deals if d["event"] == "take_profit"][0]
    assert deal["price"] == pytest.approx(2725.00)
    assert deal["pnl_usd"] > 0


def test_paper_bridge_market_orders_account_and_margin_math():
    bridge = PaperSimulatedBridge(clock=lambda: NOW, slippage_bps=2.0)
    bridge.set_price("SOLUSD", 119.99, 120.01)
    result = bridge.execute_market_order("SOLUSD", "LONG", 0.10, 119.00, 121.00,
                                         comment="OMNI:mkt")
    assert result["success"]
    assert result["price_open"] == pytest.approx(120.01 * (1 + 2.0 / 1e4), abs=0.005)  # ask+slip, 2dp
    bridge.on_tick("SOLUSD", 120.50)
    account = bridge.get_account_summary()
    assert account["equity_usd"] == pytest.approx(5000.0 + (120.49 - result["price_open"])
                                                  * 0.10 * 100, abs=0.005)
    assert account["margin_usd"] == pytest.approx(0.10 * 1000.0)
    assert 0 < account["margin_free_usd"] < account["equity_usd"]


def test_paper_bridge_lifecycle_intents_and_deals_ledger():
    bridge = PaperSimulatedBridge(clock=lambda: NOW)
    staged = bridge.stage_limit_order("SOLUSD", "LONG", 0.5, 119.50, 118.50, 121.00,
                                      comment="OMNI:k")
    assert bridge.intent_filled("OMNI:k", NOW) is False             # still resting
    assert bridge.cancel_pending_order(staged["ticket"])["success"]
    assert bridge.cancel_pending_order(staged["ticket"])["success"] is False
    bridge.stage_limit_order("SOLUSD", "LONG", 0.5, 119.50, 118.50, 121.00, comment="OMNI:j")
    bridge.on_tick("SOLUSD", 119.40)
    assert bridge.intent_filled("OMNI:j", NOW) is True               # filled and open
    assert bridge.position_deals(bridge.get_open_positions()[0]["ticket"])[0]["event"] == "fill"
    assert bridge.estimate_order("SOLUSD", "LONG", 120.0, 119.0)["stop_loss_per_lot"] \
        == pytest.approx(100.0)
    assert bridge.reconcile_intent_history("OMNI:j", NOW) == {"state": None}
    assert default_symbol_of("GOLD") == "XAUUSD" and asset_of_symbol("XAUUSD") == "GOLD"
    assert asset_of_symbol("SOLUSD.pi") == "SOL"


class FakeTransport:
    """MetaApi-shaped canned gateway responses (the live Blueberry account)."""

    def __init__(self):
        self.calls = []
        self.routes = {
            "summary": (200, {"login": 5064568, "currency": "USD", "balance": 4841.23,
                              "equity": 4836.72, "freeMargin": 3691.13}),
            "positions": (200, [{"id": 18593333, "symbol": "ETHUSD.pi",
                                 "type": "POSITION_TYPE_BUY", "volume": 0.85,
                                 "openPrice": 2695.50, "stopLoss": 2686.00,
                                 "takeProfit": 2725.00, "profit": 5.49,
                                 "time": 1760000000000, "magic": 100895,
                                 "comment": "OMNI:live"}]),
            "pending": (200, [{"id": 18573320, "symbol": "ETHUSD.pi",
                               "type": "ORDER_TYPE_SELL_LIMIT", "volume": 0.55,
                               "openPrice": 2732.80, "stopLoss": 2741.50,
                               "takeProfit": 2705.00, "magic": 100895,
                               "comment": "OMNI:rest"}]),
            "price": (200, {"bid": 2710.00, "ask": 2710.55, "time": 1760000000000}),
            "trade": (200, {"orderId": 18599999}),
        }
        self.fail_route = None

    def __call__(self, method, url, headers, payload):
        self.calls.append((method, url, headers, payload))
        match = None
        if url.endswith("/account-summary"):
            match = "summary"
        elif url.endswith("/positions"):
            match = "positions"
        elif "pendingOrders" in url:
            match = "pending"
        elif "symbolPrice" in url:
            match = "price"
        elif url.endswith("/trade"):
            match = "trade"
        if match is not None:
            if self.fail_route == match:
                return 500, {"message": "gateway down"}
            status, body = self.routes[match]
            return status, copy.deepcopy(body)
        return 404, {"message": "no route"}


def _rest_bridge(transport=None):
    transport = transport or FakeTransport()
    return HeadlessRESTBridge(token="tok", account_id="acc", domain="gw.example",
                              transport=transport, clock=lambda: NOW), transport


def test_headless_rest_bridge_maps_account_state():
    bridge, transport = _rest_bridge()
    summary = bridge.get_account_summary()
    assert summary["login"] == 5064568 and summary["equity_usd"] == pytest.approx(4836.72)
    positions = bridge.get_open_positions()
    assert positions[0]["ticket"] == 18593333 and positions[0]["direction"] == "LONG"
    assert positions[0]["sl"] == 2686.00 and positions[0]["time"] == pytest.approx(1760000000.0)
    pending = bridge.get_pending_orders()
    assert pending[0]["ticket"] == 18573320 and pending[0]["direction"] == "SHORT"
    assert pending[0]["price_open"] == 2732.80
    quote = bridge.get_symbol_price("ETHUSD.pi")
    assert quote["bid"] == 2710.00 and 0 < quote["point"] and quote["currency_profit"] == "USD"
    # Token rides the auth header; nothing is in the URL.
    assert all(h.get("auth") == "tok" for (_m, _u, h, _p) in transport.calls)
    assert all("tok" not in u for (_m, u, _h, _p) in transport.calls)


def test_headless_rest_bridge_trades_and_fails_closed():
    bridge, transport = _rest_bridge()
    staged = bridge.stage_limit_order("SOLUSD.p", "SELL", 0.06, 122.25, 123.15, 120.10,
                                      comment="OMNI:s", magic=100895)
    assert staged == {"success": True, "ticket": 18599999}
    assert bridge.modify_position_sltp(18593333, 2698.82)["success"]
    assert bridge.cancel_pending_order(18573320)["success"]
    assert bridge.execute_market_order("SOLUSD.p", "SHORT", 0.06, 123.15, 120.10)["success"]
    # The ledger answers intent queries from live state, not assumptions.
    transport.routes["pending"] = (200, [])
    assert bridge.intent_filled("OMNI:s", NOW) is False    # ticket left pending but has no position
    transport.routes["positions"] = (200, [{"id": 18599999, "symbol": "SOLUSD.p",
                                            "type": "POSITION_TYPE_SELL", "volume": 0.06,
                                            "openPrice": 122.25, "profit": 0.0}])
    assert bridge.intent_filled("OMNI:s", NOW) is True     # gone from pending, alive as a position
    transport.routes["positions"] = (200, [])
    assert bridge.intent_filled("OMNI:s", NOW) is False
    # Fail-closed: a 5xx from the gateway raises, never a silent success.
    transport.fail_route = "trade"
    with pytest.raises(BridgeError):
        bridge.stage_limit_order("SOLUSD.p", "SELL", 0.06, 122.25, 123.15, 120.10)
    # And the health probe fails closed when the account route itself is down.
    transport.fail_route = "summary"
    assert bridge.health()["healthy"] is False


def test_create_bridge_is_fail_closed_on_explicit_unhealthy_backend(monkeypatch):
    monkeypatch.setenv("EXECUTION_BACKEND", "native_mt5")   # no terminal in this container
    with pytest.raises(NoExecutionBackend):
        create_bridge()
    monkeypatch.setenv("EXECUTION_BACKEND", "fix_protocol")
    with pytest.raises(NoExecutionBackend):
        create_bridge()


def test_create_bridge_auto_discovers_paper_only_when_allowed(monkeypatch):
    for var in ("EXECUTION_BACKEND", "METAAPI_TOKEN", "METAAPI_ACCOUNT_ID"):
        monkeypatch.delenv(var, raising=False)
    monkeypatch.setenv("OMNI_ALLOW_PAPER", "0")
    with pytest.raises(NoExecutionBackend):
        create_bridge()
    monkeypatch.setenv("OMNI_ALLOW_PAPER", "1")
    bridge = create_bridge()
    assert isinstance(bridge, PaperSimulatedBridge)


# ============================================== 2. persistent whale walls
def _book_with_walls(mid=120.0, bid_size=80000, ask_size=50000):
    return {"ts": NOW, "best_bid": mid - 0.01, "best_ask": mid + 0.01,
            "bids": [{"price": mid - 0.01 - i * 0.01, "size": bid_size} for i in range(20)],
            "asks": [{"price": mid + 0.01 + i * 0.01, "size": ask_size} for i in range(20)]}


def test_resting_walls_require_150k_and_180s_persistence():
    factory = ZeroCostDataFactory(["SOL"], clock=lambda: NOW)
    book = _book_with_walls()                      # ~80000*120 = 9.6M bid wall
    factory.ingest_book("SOL", book)
    factory.ingest_trade("SOL", {"ts": NOW, "price": 120.0, "size": 1.0, "side": "BUY",
                                 "venue": "BINANCE", "notional_usd": 120.0})
    factory.ingest_bars("SOL", [{"time": NOW - i * 900, "open": 120, "high": 120.9,
                                 "low": 119.1, "close": 120, "volume": 100}
                                for i in range(30, 0, -1)])
    # Seen once: fleeting depth, NOT a resting whale cluster (checked on a
    # separate factory so the priming span below starts uncontaminated).
    fleeting = ZeroCostDataFactory(["SOL"], clock=lambda: NOW)
    fleeting.ingest_book("SOL", book)
    assert fleeting.payload("SOL", NOW)["l3_orders"] == []
    # Observed every 30s for 240s: now it is persistent.
    for step in range(9):
        factory.wall_tracker.observe("SOL", book, NOW - 240 + step * 30)
    walls = factory.payload("SOL", NOW)["l3_orders"]
    assert walls and walls[0]["notional_usd"] >= 150_000
    assert walls[0]["persistence_sec"] >= 180
    # Sub-150k depth never qualifies, however long it rests.
    thin = _book_with_walls(bid_size=100, ask_size=100)
    factory.ingest_book("SOL", thin)
    for step in range(9):
        factory.wall_tracker.observe("SOL", thin, NOW + step * 30)
    assert all(w["notional_usd"] >= 150_000
               for w in factory.payload("SOL", NOW + 240)["l3_orders"])


# ============================================== 3. CandleScheduler
def test_scheduler_deadlines_land_on_minute_14_of_each_candle():
    scheduler = CandleScheduler(cadence_second=30.0)
    slot = (NOW // 900) * 900
    # Just after a boundary -> the next candle's :14:30.
    assert scheduler.next_deadline(slot + 871.0) == slot + 900 + 870.0
    # Early in a candle -> this candle's :14:30.
    assert scheduler.next_deadline(slot + 10.0) == slot + 870.0
    # Exactly at the deadline is too late: the next candle.
    assert scheduler.next_deadline(slot + 870.0) == slot + 900 + 870.0
    assert scheduler.seconds_until(slot + 800.0) == pytest.approx(70.0)


def test_scheduler_wakes_exactly_on_boundaries_with_drift_compensation():
    class Clock:
        def __init__(self): self.t = (NOW // 900) * 900 + 500.0
        def __call__(self): return self.t

    clock = Clock()
    wakes, sleeps = [], []

    async def fake_sleep(seconds):
        sleeps.append(seconds)
        clock.t += seconds                     # perfect virtual time

    scheduler = CandleScheduler(cadence_second=30.0, clock=clock, sleep=fake_sleep)
    async def run():
        await scheduler.run(lambda deadline: wakes.append((deadline, clock())),
                            max_cycles=3)
    asyncio.run(run())
    slot = (NOW // 900) * 900
    expected = [slot + 870.0, slot + 900 + 870.0, slot + 1800 + 870.0]
    assert [w[0] for w in wakes] == expected
    assert all(w[1] == pytest.approx(w[0]) for w in wakes)      # zero residual drift
    # The fine phase sleeps in <=50ms increments near the boundary; coarse
    # sleeps are the big jumps (>= the 0.5s coarse margin).
    assert all(s <= 0.05 + 1e-9 or s >= 0.5 - 1e-9 for s in sleeps)


# ============================================== 4. HeadlessService (HTTP)
class FakeRuntime:
    def __init__(self, ready=True, payload=None):
        self.ready, self.payload = ready, payload or {"decision": "LIMIT_STAGED",
                                                      "pioneer_conviction_vector": {"SOL": {"conviction": 0.4}},
                                                      "staged_order_tickets": [{"asset": "SOL"}],
                                                      "traded": True}
        self.calls = []

    def readiness(self):
        return self.ready, [] if self.ready else ["bridge_unhealthy"]

    def evaluate_candle(self, force=False):
        self.calls.append(force)
        return dict(self.payload)


async def _request(port, method, path, body=None, headers=None):
    reader, writer = await asyncio.open_connection("127.0.0.1", port)
    raw = canonical_json(body) if body is not None else b""
    lines = [f"{method} {path} HTTP/1.1", "Host: 127.0.0.1",
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
    status_line = head.split(b"\r\n")[0].decode()
    header_map = {}
    for line in head.split(b"\r\n")[1:]:
        key, _, value = line.decode().partition(":")
        header_map[key.strip().lower()] = value.strip()
    return int(status_line.split()[1]), header_map, json.loads(body_out or b"{}")


def _serve(runtime, secret=None):
    service = HeadlessService(runtime, host="127.0.0.1", port=0, secret=secret,
                              clock=lambda: NOW)
    return service


def test_sign_and_verify_roundtrip_tamper_and_replay():
    envelope = sign_payload({"a": 1, "b": [2, 3]}, SECRET, ts=NOW)
    assert verify_signed(envelope, SECRET, now=NOW)
    tampered = {**envelope, "payload": {"a": 2, "b": [2, 3]}}
    assert not verify_signed(tampered, SECRET, now=NOW)          # payload tampered
    assert not verify_signed(envelope, "other-secret", now=NOW)  # wrong key
    assert not verify_signed(envelope, SECRET, now=NOW + 60.0)   # outside replay window
    assert not verify_signed({}, SECRET, now=NOW)


def test_healthz_and_readyz_over_http():
    async def scenario(runtime, path):
        service = _serve(runtime)
        server = asyncio.run_coroutine_threadsafe(service.serve(), LOOP) if False else None
        return None
    # run inline (no threads needed): each scenario gets its own event loop
    async def check():
        ready_runtime = FakeRuntime(ready=True)
        service = _serve(ready_runtime)
        server = await service.serve()
        port = server.sockets[0].getsockname()[1]
        status, headers, body = await _request(port, "GET", "/healthz")
        assert status == 200 and body["ok"] and body["service"] == "omni-headless"
        status, _, body = await _request(port, "GET", "/readyz")
        assert status == 200 and body["ready"]
        server.close()
        sick = FakeRuntime(ready=False)
        service = _serve(sick)
        server = await service.serve()
        port = server.sockets[0].getsockname()[1]
        status, _, body = await _request(port, "GET", "/readyz")
        assert status == 503 and body["reasons"] == ["bridge_unhealthy"]
        status, _, _ = await _request(port, "GET", "/nope")
        assert status == 404
        server.close()
    asyncio.run(check())


def test_evaluate_candle_returns_signed_payload_and_enforces_auth():
    async def check():
        runtime = FakeRuntime()
        service = _serve(runtime, secret=SECRET)
        server = await service.serve()
        port = server.sockets[0].getsockname()[1]
        # Unsigned request: rejected.
        status, _, body = await _request(port, "POST", "/api/v1/evaluate_candle",
                                         body={"force": False})
        assert status == 401 and body["error"] == "invalid_signature"
        # Properly signed request: 200 + HMAC-signed response.
        envelope = sign_payload({"force": False}, SECRET, ts=NOW)
        status, headers, body = await _request(
            port, "POST", "/api/v1/evaluate_candle", body=envelope["payload"],
            headers={"X-Signature": envelope["signature"],
                     "X-Signature-Ts": f"{envelope['ts']:.3f}"})
        assert status == 200
        assert body["decision"] == "LIMIT_STAGED" and body["traded"]
        assert body["pioneer_conviction_vector"]["SOL"]["conviction"] == 0.4
        assert body["staged_order_tickets"] == [{"asset": "SOL"}]
        assert runtime.calls == [False]
        ts = float(headers["x-signature-ts"])
        import hmac as hmac_module
        digest = hmac_module.new(SECRET.encode(), f"{ts:.3f}".encode() + b"."
                                 + canonical_json(body), "sha256").hexdigest()
        assert hmac_module.compare_digest(digest, headers["x-signature"])
        # Stale signature (outside the 30s replay window): rejected.
        stale = sign_payload({"force": False}, SECRET, ts=NOW - 120.0)
        status, _, _ = await _request(
            port, "POST", "/api/v1/evaluate_candle", body=stale["payload"],
            headers={"X-Signature": stale["signature"],
                     "X-Signature-Ts": f"{stale['ts']:.3f}"})
        assert status == 401
        # Malformed JSON body: 400.
        reader, writer = await asyncio.open_connection("127.0.0.1", port)
        writer.write(b"POST /api/v1/evaluate_candle HTTP/1.1\r\nHost: x\r\n"
                     b"Content-Length: 7\r\nConnection: close\r\n\r\nnot json")
        await writer.drain()
        response = b""
        while True:
            chunk = await reader.read(4096)
            if not chunk:
                break
            response += chunk
        writer.close()
        assert b"400" in response.split(b"\r\n")[0]
        server.close()
    asyncio.run(check())


# ============================================== 5. LLM contract
def _candidate():
    return {"candidate_id": "1955556:SOL:LONG", "direction": "LONG",
            "price_open": 119.42, "sl": 117.42, "tp": 122.32, "hurdle_r": 2.4,
            "risk_usd": 15.0, "sizing": {"risk_usd": 15.0}}


def _request_contract():
    return build_consultation_request(
        as_of=NOW, asset="SOL",
        features={"direction": "LONG", "confluence": 0.9,
                  "pioneer": {"digest": "abc123", "conviction": 0.55}},
        pioneer={"conviction": 0.55, "advice": "SUPPORT_LONG", "digest": "abc123"},
        candidate=_candidate())


def _valid_select(request):
    return {"action": "SELECT", "candidate_id": request["candidate"]["candidate_id"],
            "risk_usd": request["candidate"]["risk_usd"],
            "sl": request["candidate"]["sl"], "tp": request["candidate"]["tp"],
            "rationale_summary": "Tape, whale cohort and cascade fuel align long; the "
                                 "wall front-runs the target within friction.",
            "support_refs": ["/pioneer_advisory", "/sealed_features/vector/confluence"],
            "invalidation_refs": ["/candidate/sl"],
            "invariant_digest": request["invariant_digest"]}


def test_llm_contract_accepts_a_clean_select_and_hold():
    request = _request_contract()
    ok, violations = validate_consultation_response(request, _valid_select(request))
    assert ok, violations
    hold = {"action": "HOLD", "candidate_id": None, "risk_usd": None, "sl": None,
            "tp": None, "rationale_summary": "Quality below floor.",
            "support_refs": [], "invalidation_refs": [],
            "invariant_digest": request["invariant_digest"]}
    ok, violations = validate_consultation_response(request, hold)
    assert ok, violations


def test_llm_contract_rejects_invented_or_moved_numbers():
    request = _request_contract()
    # A "better" risk, a moved stop, a stretched target: all violations.
    moved = _valid_select(request)
    moved.update(risk_usd=45.0, sl=117.00, tp=124.00)
    ok, violations = validate_consultation_response(request, moved)
    assert not ok
    assert "risk_usd_not_echoed:45.0!=15.0" in violations
    assert any(v.startswith("sl_not_echoed") for v in violations)
    assert any(v.startswith("tp_not_echoed") for v in violations)
    assert "risk_budget_violation:45.0" in violations
    # A fabricated candidate id, a stale digest, an unresolved pointer.
    wrong = _valid_select(request)
    wrong["candidate_id"] = "1955556:BTC:LONG"
    ok, violations = validate_consultation_response(request, wrong)
    assert "candidate_id_mismatch" in violations
    wrong = _valid_select(request)
    wrong["invariant_digest"] = "0" * 64
    ok, violations = validate_consultation_response(request, wrong)
    assert "invariant_digest_mismatch" in violations
    wrong = _valid_select(request)
    wrong["support_refs"] = ["/fabricated/field"]
    ok, violations = validate_consultation_response(request, wrong)
    assert "support_refs_unresolved:/fabricated/field" in violations
    # HOLD that carries order terms: rejected.
    noisy_hold = {"action": "HOLD", "candidate_id": None, "risk_usd": 15.0,
                  "sl": 117.42, "tp": 122.32, "rationale_summary": "x",
                  "support_refs": [], "invalidation_refs": [],
                  "invariant_digest": request["invariant_digest"]}
    ok, violations = validate_consultation_response(request, noisy_hold)
    assert "hold_must_not_carry_order_terms" in violations


def test_invariant_envelope_encodes_the_production_risk_set():
    envelope = default_invariant_envelope(risk_min_usd=10.0, risk_max_usd=20.0)
    assert envelope["hard_floor_usd"] == 4775.0
    assert envelope["friction_bps_round_trip"] == 41.0
    assert envelope["max_concurrent_filled"] == 2
    assert envelope["ratchet"]["be_trigger_r"] == 0.80 and envelope["ratchet"]["lock_1_r"] == 0.35
    assert envelope["ratchet"]["trigger_2_r"] == 1.50 and envelope["ratchet"]["runner_trigger_r"] == 2.00
    assert invariant_digest(envelope) == invariant_digest(default_invariant_envelope(
        risk_min_usd=10.0, risk_max_usd=20.0))
    assert invariant_digest(envelope) != invariant_digest(
        default_invariant_envelope(risk_min_usd=10.0, risk_max_usd=45.0))


# ============================================== 6. HeadlessRuntime
class UnhealthyBridge:
    name = "broken"
    def health(self): return {"healthy": False, "backend": "broken", "detail": "dead"}


class FakeFactory:
    def __init__(self, fresh=True):
        self.bus = self
        self.fresh = fresh

    def book(self, asset):
        return {"ts": NOW - 2 if self.fresh else NOW - 500}

    def payload(self, asset, now=None):
        return {"coin": asset, "price": 120.0}


def test_runtime_readiness_fails_closed():
    runtime = HeadlessRuntime(assets=["SOL"], clock=lambda: NOW)          # no bridge
    ready, reasons = runtime.readiness()
    assert not ready and "no_bridge" in reasons
    runtime = HeadlessRuntime(assets=["SOL"], bridge=UnhealthyBridge(),
                              factory=FakeFactory(), clock=lambda: NOW)
    ready, reasons = runtime.readiness()
    assert not ready and any(r.startswith("bridge_unhealthy") for r in reasons)
    runtime = HeadlessRuntime(assets=["SOL"], bridge=PaperSimulatedBridge(clock=lambda: NOW),
                              factory=FakeFactory(fresh=False), clock=lambda: NOW)
    ready, reasons = runtime.readiness()
    assert not ready and "no_fresh_book" in reasons
    runtime = HeadlessRuntime(assets=["SOL"], bridge=PaperSimulatedBridge(clock=lambda: NOW),
                              factory=FakeFactory(), clock=lambda: NOW)
    assert runtime.readiness() == (True, [])


def test_runtime_evaluate_candle_is_fail_closed_without_a_healthy_bridge():
    class ExplodingTrader:
        def evaluate_market(self, *a, **k):
            raise AssertionError("must never be consulted")
    runtime = HeadlessRuntime(assets=["SOL"], bridge=UnhealthyBridge(),
                              factory=FakeFactory(), trader=ExplodingTrader(),
                              clock=lambda: NOW)
    result = runtime.evaluate_candle()
    assert result["ok"] is False and result["traded"] is False
    assert result["decision"] == "NO_TRADE_FAIL_CLOSED"
    assert "bridge_unhealthy" in result["reason"]


def test_runtime_evaluate_candle_returns_the_microservice_contract():
    class Trader:
        def __init__(self):
            self.intel = None
            self.state = {"intents": {"k": {"status": "STAGED_LIMIT", "candidate": {
                "asset": "SOL", "direction": "LONG", "price_open": 119.42,
                "sl": 117.42, "tp": 122.32, "volume": 0.5, "risk_usd": 15.0},
                "order_ticket": 1001, "expires_at": NOW + 3600}}}
        def evaluate_market(self, payloads, macro, force=False):
            return {"decision": "LIMIT_STAGED", "reason": "", "vetoes": {"ETH": "x"}}
    class Runner:
        last_quality = {"quality_score": 0.9, "digest": "q1"}
    class Pioneer:
        last = {"SOL": {"conviction": 0.55, "advice": "SUPPORT_LONG",
                        "quality_score": 0.9, "min_favorable_move_bps": 47.7,
                        "digest": "p1"}}
    runtime = HeadlessRuntime(assets=["SOL"], bridge=PaperSimulatedBridge(clock=lambda: NOW),
                              factory=FakeFactory(), trader=Trader(), pioneer=Pioneer(),
                              validator=object(), runner=Runner(), clock=lambda: NOW)
    result = runtime.evaluate_candle()
    assert result["ok"] and result["traded"] and result["decision"] == "LIMIT_STAGED"
    assert result["pioneer_conviction_vector"]["SOL"]["digest"] == "p1"
    ticket = result["staged_order_tickets"][0]
    assert (ticket["asset"], ticket["order_ticket"], ticket["risk_usd"]) == ("SOL", 1001, 15.0)
    assert result["data_quality"] == {"score": 0.9, "digest": "q1"}
    assert runtime.last_evaluation is result


def test_full_stack_paper_bridge_trade_through_the_real_trader(tmp_path):
    """Backend C is a true drop-in: the REAL Omni_Trader executes a T1 breakout
    through PaperSimulatedBridge fills (no test broker double in sight)."""
    from Terminal.Omni_Trader import AI15mMT5Trader, MAGIC
    from Terminal.Asset_Universe import UNIVERSE
    from Terminal.Risk_Sizing_Engine import CovarianceGate

    slot = (NOW // 900) * 900 + 870
    bridge = PaperSimulatedBridge(clock=lambda: slot)
    bridge.set_price("SOLUSD", 119.99, 120.01, ts=slot)
    import numpy as np
    covariance = CovarianceGate(UNIVERSE, np.eye(len(UNIVERSE)) * 0.003 ** 2,
                                {"return_units": "decimal_log_return", "horizon_minutes": 15,
                                 "created_at": slot - 60, "data_end": slot - 900,
                                 "max_age_seconds": 86400})

    class OfflineIntel:
        def check_macro_blackout(self): return False, "NO_EVENT", 999
        def get_market_intelligence_report(self):
            return {"asset_scores": {a: 1 for a in UNIVERSE}, "sentiment_valid": True}

    trader = AI15mMT5Trader(bridge=bridge, covariance=covariance,
                            intel=OfflineIntel(),
                            cognitive=object(), cognitive_enabled=False,
                            uplift_path=tmp_path / "no_uplift",
                            clock=lambda: slot, paper_mode=False, entry_mode="market",
                            state_file=tmp_path / "state.json",
                            journal_dir=tmp_path / "journal")
    trader.symbols = {a: bridge.resolve_symbol(a) for a in UNIVERSE}
    start = int(slot // 900) * 900 - 96 * 900
    trader.bars = {a: [{"time": start + i * 900, "open": 120 + 0.2 * i,
                        "high": 120 + 0.2 * i + 0.55, "low": 120 + 0.2 * i - 0.55,
                        "close": 120 + 0.2 * i} for i in range(96)] for a in UNIVERSE}

    def payload(now=slot, mid=120.0):
        return {"coin": "SOL", "price": mid,
                "l2_book": {"timestamp": now * 1000, "best_bid": mid - 0.01,
                            "best_ask": mid + 0.01,
                            "bids": [{"price": mid - 0.01 - i * 0.01, "size": 10000}
                                     for i in range(20)],
                            "asks": [{"price": mid + 0.01 + i * 0.01, "size": 100}
                                     for i in range(20)]},
                "recent_trades": [{"time": now * 1000, "side": "BUY", "price": mid,
                                   "size": 100, "notional_usd": 10000},
                                  {"time": now * 1000, "side": "BUY", "price": mid,
                                   "size": 100, "notional_usd": 10000}],
                "sources": {"l3": {"observed_at": now}, "liquidations": {"observed_at": now}},
                "l3_orders": [], "liquidations": {}}

    result = trader.evaluate_market({"SOL": payload()}, {"received_at": slot,
                                                         "sentiment_valid": True,
                                                         "asset_scores": {"SOL": 1}})
    assert result["decision"] == "ORDER_FILLED"
    positions = bridge.get_open_positions()
    assert len(positions) == 1
    position = positions[0]
    assert position["direction"] == "LONG" and position["magic"] == MAGIC
    assert position["sl"] and position["tp"] and position["sl"] < position["price_open"] < position["tp"]
    # The paper matching engine then honours the broker-side ratchet actuator:
    # price appreciates, the BE lock moves the stop under the bid, and the
    # position survives (a stop moved ABOVE the bid would - correctly - fire).
    bridge.set_price("SOLUSD", 120.49, 120.51, ts=slot + 900)
    assert bridge.modify_position_sltp(position["ticket"], 120.30)["success"]
    assert bridge.get_open_positions()[0]["sl"] == 120.30
    assert len(bridge.get_open_positions()) == 1
