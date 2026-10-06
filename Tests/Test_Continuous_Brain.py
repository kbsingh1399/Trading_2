"""Tests for OX_ALPHA_62: the continuous autonomous Arena Brain loop.

100% offline and deterministic - the tunnel is replaced by a scripted fake
client, the clock is injectable, and no test ever touches a network.

  * Position Manager: the exact GOLD #18576872 ratchet geometry (phase 0 BE
    lock at +0.80R -> entry - 0.15R), phase 1 profit lock, phase 2 runner
    trail with re-arm, only-ever-tightening guard, 24-bar time decay close.
  * Deliberation: minute-14 window alignment (once per slot), macro verdict,
    staging policy (muscle-abstained + capacity + exhaustion + conviction),
    refusal paths.
  * Error recovery: dead tunnel, bad payloads - the loop never raises.
  * The CLOSE_POSITION command and the signed market_state endpoint.
"""
import asyncio
import json
import math

import pytest

from Terminal.Headless.arena_continuous_brain import (ContinuousBrain, BrainPolicy,
                                                      BRAIN_COMMENT, BRAIN_VERSION)
from Terminal.Execution.remote_reconciler import apply_command, new_command, sign_command
from Terminal.Execution.paper import PaperSimulatedBridge

NOW = 1_760_000_000.0
SECRET = "arena-test-secret-0x62"


# ------------------------------------------------------------------ fixtures
class FakeClient:
    """Scripted tunnel double: records every dispatch, mutates the shared
    position on successful SL modifications (like a real broker would)."""

    def __init__(self, states=None, evaluations=None, positions=None, quotes=None):
        self.states = list(states or [])
        self.evaluations = list(evaluations or [])
        self.positions = positions if positions is not None else []
        self.quotes = quotes or {}
        self.calls = []

    def market_state(self, assets=None):
        self.calls.append(("market_state", assets))
        if self.states:
            state = self.states.pop(0)
        else:
            state = {"positions": list(self.positions), "pending_orders": [],
                     "quotes": dict(self.quotes),
                     "symbols": {"GOLD": "XAUUSD.pi"}, "orderflow": {},
                     "macro": {"blackout_active": False},
                     "account": {"equity_usd": 4839.88}}
        return state

    def evaluate_candle(self, force=False):
        self.calls.append(("evaluate_candle", force))
        return self.evaluations.pop(0) if self.evaluations else {"decision": "HOLD"}

    def modify_sltp(self, ticket, sl, tp=None):
        self.calls.append(("modify_sltp", ticket, sl))
        for position in self.positions:
            if str(position.get("ticket")) == str(ticket):
                position["sl"] = sl                     # broker applies it
        return {"success": True}

    def close_position(self, ticket, reason="brain_close"):
        self.calls.append(("close_position", ticket, reason))
        self.positions = [p for p in self.positions if str(p.get("ticket")) != str(ticket)]
        return {"success": True}

    def stage_order(self, symbol, direction, volume, limit_price, sl, tp,
                    comment="ARENA:ORDER"):
        self.calls.append(("stage_order", symbol, direction, volume, limit_price,
                           sl, tp, comment))
        return {"success": True, "ticket": 990001}


def gold_position(price=4167.50, sl=4186.50, age_sec=3600.0):
    """The live GOLD short #18576872: entry 4176.00, initial R = 10.50."""
    return {"ticket": 18576872, "symbol": "XAUUSD.pi", "direction": "SHORT",
            "price_open": 4176.00, "sl": sl, "tp": 4143.00, "volume": 0.01,
            "time": NOW - age_sec, "profit_usd": 6.73}


def gold_state(position, bid=4167.50, ask=4167.57, **extra):
    state = {"positions": [position], "pending_orders": [],
             "quotes": {"XAUUSD.pi": {"bid": bid, "ask": ask, "tick_size": 0.01,
                                      "contract_size": 100.0, "min_lot": 0.01,
                                      "step_lot": 0.01, "digits": 2}},
             "symbols": {"GOLD": "XAUUSD.pi"}, "orderflow": {},
             "macro": {"blackout_active": False},
             "account": {"balance_usd": 4833.15, "equity_usd": 4839.88,
                         "margin_free_usd": 4422.28}}
    state.update(extra)
    return state


SLOT14 = (NOW // 900) * 900 + 14 * 60 + 45      # inside the deliberation window


def brain(client, clock=lambda: SLOT14, **policy_overrides):
    policy = BrainPolicy()
    for key, value in policy_overrides.items():
        setattr(policy, key, value)
    return ContinuousBrain(client, policy=policy, clock=clock)


# ============================================== Position Manager
def test_phase0_be_lock_matches_the_live_gold_geometry():
    position = gold_position(price=4167.50)             # <= 4167.60 trigger
    client = FakeClient(positions=[position],
                        quotes=gold_state(position)["quotes"])
    engine = brain(client)
    engine.tick()
    modifies = [c for c in client.calls if c[0] == "modify_sltp"]
    assert len(modifies) == 1
    ticket, sl = modifies[0][1], modifies[0][2]
    assert ticket == 18576872
    # Phase 0: entry - 0.15R = 4176.00 - 1.575 = 4174.425 (the spec's 4174.40
    # is the same lock rounded to a coarse tick).
    assert sl == pytest.approx(4174.425, abs=1e-6)
    assert abs(sl - 4174.40) < 0.03
    # Dedupe: the next tick does not re-dispatch phase 0.
    engine.tick()
    assert len([c for c in client.calls if c[0] == "modify_sltp"]) == 1


def test_phase1_profit_lock_and_phase2_runner_trail():
    # Price 4160.00: gain = 16/10.5 = 1.524R -> phases 0 AND 1 fire together.
    position = gold_position(price=4160.00, sl=4186.50)
    client = FakeClient(positions=[position],
                        quotes=gold_state(position, bid=4160.00, ask=4160.07)["quotes"])
    engine = brain(client)
    engine.tick()
    locks = [c[2] for c in client.calls if c[0] == "modify_sltp"]
    assert locks[0] == pytest.approx(4174.425, abs=1e-6)          # phase 0
    assert locks[1] == pytest.approx(4176.00 - 0.85 * 10.5, abs=1e-6)  # phase 1: 4167.075
    assert position["sl"] == pytest.approx(4167.075, abs=1e-6)    # broker applied

    # Price 4152.00: gain 2.286R -> runner trail = ask + 0.65R (a SHORT covers
    # at the ask) = 4152.07 + 6.825 = 4158.895.
    position["profit_usd"] = 24.0
    state = gold_state(position, bid=4152.00, ask=4152.07)
    client.states = [state]
    engine.tick()
    trail = [c[2] for c in client.calls if c[0] == "modify_sltp"][-1]
    assert trail == pytest.approx(4152.07 + 0.65 * 10.5, abs=1e-6)
    # Same price again: re-arm threshold (0.05R) not met -> no dispatch.
    client.states = [gold_state(position, bid=4152.00, ask=4152.07)]
    engine.tick()
    assert len([c for c in client.calls if c[0] == "modify_sltp"]) == 3
    # Price 4145.00 (gain 2.95R, improvement 0.67R): trail re-arms.
    client.states = [gold_state(position, bid=4145.00, ask=4145.07)]
    engine.tick()
    trail = [c[2] for c in client.calls if c[0] == "modify_sltp"][-1]
    assert trail == pytest.approx(4145.07 + 0.65 * 10.5, abs=1e-6)


def test_ratchet_never_widens_and_never_crosses_price():
    # The muscle already tightened to 4170.00 (past the phase-0 lock): the
    # brain's 4174.425 would WIDEN the stop -> refused.
    position = gold_position(price=4167.50, sl=4170.00)
    client = FakeClient(positions=[position],
                        quotes=gold_state(position)["quotes"])
    engine = brain(client)
    engine.tick()
    assert [c for c in client.calls if c[0] == "modify_sltp"] == []
    assert position["sl"] == 4170.00
    # A stop computed through the current price is never dispatched: at gain
    # 2.29R the trail (4158.825) is valid, but a very tight spread quote at
    # 4158.80 makes it cross - the guard must skip.
    position2 = gold_position(price=4152.00, sl=4186.50)
    client2 = FakeClient(positions=[position2],
                         quotes=gold_state(position2, bid=4152.00, ask=4152.07)["quotes"])
    engine2 = brain(client2)
    engine2.tick()
    applied = [c for c in client2.calls if c[0] == "modify_sltp"]
    assert all(4152.07 < c[2] < 4186.50 for c in applied)        # SHORT: sl above ask


def test_time_decay_closes_a_stale_dud_once():
    position = gold_position(price=4175.90, sl=4186.50, age_sec=25 * 900)
    client = FakeClient(positions=[position],
                        quotes=gold_state(position, bid=4175.90, ask=4175.97)["quotes"])
    engine = brain(client)
    engine.tick()
    closes = [c for c in client.calls if c[0] == "close_position"]
    assert len(closes) == 1 and closes[0][1] == 18576872
    assert "time_decay" in closes[0][2]
    assert not client.positions                                  # gone
    # Dedupe (the position would have vanished from state anyway).
    engine.tick()
    assert len([c for c in client.calls if c[0] == "close_position"]) == 1
    # A position that reached +0.20R never decays out.
    healthy = gold_position(price=4173.00, sl=4186.50, age_sec=25 * 900)
    client2 = FakeClient(positions=[healthy],
                         quotes=gold_state(healthy, bid=4173.00, ask=4173.07)["quotes"])
    brain(client2).tick()
    assert [c for c in client2.calls if c[0] == "close_position"] == []


# ============================================== deliberation + staging
def _sol_state(orderflow, conviction_advisory, positions=None, pending=None,
               blackout=False):
    return {"positions": positions or [], "pending_orders": pending or [],
            "quotes": {"SOLUSD.p": {"bid": 119.99, "ask": 120.01, "tick_size": 0.01,
                                    "contract_size": 100.0, "min_lot": 0.01,
                                    "step_lot": 0.01, "digits": 2}},
            "symbols": {"SOL": "SOLUSD.p"},
            "orderflow": {"SOL": orderflow},
            "macro": {"blackout_active": blackout},
            "account": {"equity_usd": 4839.88}}


EXHAUSTED_LONG = {"cvd_1m": -40_000.0, "cvd_5m": -500_000.0,
                  "taker_buy_usd_1m": 300_000.0, "taker_sell_usd_1m": 340_000.0,
                  "taker_buy_usd_5m": 1_200_000.0, "taker_sell_usd_5m": 1_700_000.0,
                  "atr": 1.0}
STILL_PRESSING = dict(EXHAUSTED_LONG, cvd_1m=-150_000.0)


def test_deliberation_fires_once_per_slot_at_minute_14():
    client = FakeClient(positions=[])
    client.states = [_sol_state({}, {}) for _ in range(4)]
    client.evaluations = [{"decision": "HOLD"} for _ in range(4)]
    engine = brain(client)
    slot = int(NOW // 900)
    clock = {"t": slot * 900 + 14 * 60 + 45}
    engine.clock = lambda: clock["t"]
    assert engine.deliberate().get("skipped") is not True
    assert engine.deliberate().get("skipped") is True            # same slot: once
    clock["t"] = slot * 900 + 15 * 60
    assert engine.deliberate().get("skipped") is True            # outside minute 14
    clock["t"] = (slot + 1) * 900 + 14 * 60 + 50
    result = engine.deliberate()
    assert result.get("slot") == slot + 1                        # next candle: fires


def test_staging_policy_requires_capacity_exhaustion_and_conviction():
    advisory = {"conviction": 0.60, "advice": "SUPPORT_LONG"}
    evaluation = {"decision": "HOLD",
                  "pioneer_conviction_vector": {"SOL": advisory}}

    # Full clearance: 0 filled, 0 pending, exhaustion passing, extreme
    # conviction, muscle abstained -> exactly ONE staged limit.
    client = FakeClient(positions=[])
    client.states = [_sol_state(EXHAUSTED_LONG, advisory)]
    client.evaluations = [evaluation]
    engine = brain(client)
    result = engine.deliberate()
    assert result["verdict"] == "CLEAR_TO_TRADE" and result["staged"]
    stage = [c for c in client.calls if c[0] == "stage_order"][0]
    symbol, direction, volume, entry, sl, tp, comment = stage[1:]
    assert symbol == "SOLUSD.p" and direction == "LONG" and comment == BRAIN_COMMENT
    assert entry == pytest.approx(119.99)                        # passive at the bid
    assert sl == pytest.approx(119.99 - 1.5 * 1.0)               # adaptive stop floor
    assert tp == pytest.approx(119.99 + 2.5 * 1.5)               # 2.50R target
    assert volume == pytest.approx(0.06)                         # 10 USD / (1.5*100)
    assert volume * 1.5 * 100.0 <= 20.0                          # muscle-side cap holds

    # Capacity blocked: 1 filled + 1 pending = MAX_CONCURRENT -> no stage.
    pending = [{"ticket": 18595858, "symbol": "XAUUSD.pi", "comment": "ARENA:TEST_LIMIT_v1"}]
    client = FakeClient(positions=[gold_position()])
    client.states = [_sol_state(EXHAUSTED_LONG, advisory, positions=[gold_position()],
                                pending=pending)]
    client.evaluations = [evaluation]
    engine = brain(client)
    result = engine.deliberate()
    assert result["capacity_open"] is False and result["staged"] is None

    # The muscle already staged this slot -> the brain never supplements.
    client = FakeClient(positions=[])
    client.states = [_sol_state(EXHAUSTED_LONG, advisory)]
    client.evaluations = [{"decision": "LIMIT_STAGED",
                           "pioneer_conviction_vector": {"SOL": advisory}}]
    engine = brain(client)
    assert engine.deliberate()["staged"] is None

    # Sellers still pressing -> the exhaustion gate refuses.
    client = FakeClient(positions=[])
    client.states = [_sol_state(STILL_PRESSING, advisory)]
    client.evaluations = [evaluation]
    engine = brain(client)
    result = engine.deliberate()
    assert result["staged"] is None and engine.stats["refusals"] == 1

    # Macro blackout -> BLOCKED, no stage.
    client = FakeClient(positions=[])
    client.states = [_sol_state(EXHAUSTED_LONG, advisory, blackout=True)]
    client.evaluations = [evaluation]
    engine = brain(client)
    result = engine.deliberate()
    assert result["verdict"] == "BLOCKED" and result["staged"] is None


def test_staging_refuses_when_min_lot_breaches_the_risk_budget():
    # ATR 30 on a 100-contract: 10 USD / (45 * 100) < min lot -> refuse.
    advisory = {"conviction": 0.60, "advice": "SUPPORT_LONG"}
    fat_atr = dict(EXHAUSTED_LONG, atr=30.0)
    client = FakeClient(positions=[])
    client.states = [_sol_state(fat_atr, advisory)]
    client.evaluations = [{"decision": "HOLD",
                           "pioneer_conviction_vector": {"SOL": advisory}}]
    engine = brain(client)
    assert engine.deliberate()["staged"] is None
    assert engine.stats["refusals"] == 1


# ============================================== error recovery
def test_dead_tunnel_never_kills_the_loop():
    class DeadClient:
        def market_state(self, assets=None):
            raise OSError("tunnel unreachable")
        def evaluate_candle(self, force=False):
            return {"http_status": 0, "error": "tunnel_unreachable"}
        def modify_sltp(self, ticket, sl, tp=None):
            raise AssertionError("must not be reached")
        def close_position(self, ticket, reason="brain_close"):
            raise AssertionError("must not be reached")
        def stage_order(self, **kwargs):
            raise AssertionError("must not be reached")

    engine = brain(DeadClient())
    result = engine.tick()                                       # counts the error
    assert result["event"] == "tick_error" and engine.stats["errors"] == 1
    # The endless loop itself survives: three iterations, then a clean stop.
    stops = {"n": 0}
    import threading
    stop = threading.Event()

    def fake_sleep(seconds):
        stops["n"] += 1
        if stops["n"] >= 3:
            stop.set()

    engine.run_forever(stop=stop, sleep=fake_sleep)
    assert stops["n"] == 3 and engine.stats["errors"] >= 4       # tick + deliberate
    # Recovery: a healthy client resumes normal service on the same engine.
    position = gold_position(price=4167.50)
    healthy = FakeClient(positions=[position],
                         quotes=gold_state(position)["quotes"])
    engine.client = healthy
    engine.tick()
    assert [c for c in healthy.calls if c[0] == "modify_sltp"]    # phase 0 fires


def test_bad_payloads_are_isolated():
    client = FakeClient(positions=[])
    client.states = [{"positions": "not-a-list", "quotes": None},
                     {"positions": [{"ticket": 1}], "quotes": {}}]
    engine = brain(client)
    engine.tick()                                                # garbage positions
    engine.tick()                                                # position w/o quote
    assert engine.stats["errors"] == 0                           # skipped, not crashed
    assert engine.stats["ticks"] == 2


# ============================================== command + endpoint
def test_close_position_command_applies_through_the_bridge():
    bridge = PaperSimulatedBridge(clock=lambda: NOW)
    bridge.set_price("XAUUSD.pi", 4175.99, 4176.01, ts=NOW)
    opened = bridge.execute_market_order("XAUUSD.pi", "SHORT", 0.01, 4186.50, 4143.00)
    assert opened["success"]
    command = sign_command(new_command("CLOSE_POSITION",
                                       {"ticket": opened["ticket"],
                                        "reason": "time_decay_24bars"}), SECRET)
    result = apply_command(bridge, command, clock=lambda: NOW)
    assert result["success"] and result["reason"] == "time_decay_24bars"
    assert bridge.get_open_positions() == []


def test_market_state_endpoint_is_signed_and_complete(tmp_path):
    from Terminal.Headless.server import HeadlessService, sign_payload, canonical_json
    from Terminal.Headless.runtime import HeadlessRuntime

    class Factory:
        def __init__(self):
            self.bus = self
        def book(self, asset):
            return {"ts": NOW - 2}
        def payload(self, asset, now=None):
            return {"coin": asset}

    class FactoryWithFlow(Factory):
        def __init__(self):
            super().__init__()
            self.snapshots = {"SOL": {"cvd_1m": 1.0, "taker_buy_usd_15m": 5.0}}
        def snapshot(self, asset, now=None):
            return self.snapshots.get(asset)
        def _atr(self, asset, lookback=14):
            return 1.0

    bridge = PaperSimulatedBridge(clock=lambda: NOW)
    bridge.set_price("SOLUSD", 119.99, 120.01, ts=NOW)

    class Trader:
        symbols = {"SOL": "SOLUSD"}

    runtime = HeadlessRuntime(assets=["SOL"], bridge=bridge,
                              factory=FactoryWithFlow(), trader=Trader(),
                              clock=lambda: NOW)
    state = runtime.market_state()
    assert state["positions"] == [] and state["quotes"]["SOLUSD"]["contract_size"] == 100.0
    assert state["symbols"]["SOL"] == "SOLUSD"
    assert state["orderflow"]["SOL"]["cvd_1m"] == 1.0
    assert state["account"]["equity_usd"] == pytest.approx(5000.0)
    assert state["macro"]["blackout_active"] in (True, False)

    service = HeadlessService(runtime, host="127.0.0.1", port=0, secret=SECRET,
                              clock=lambda: NOW)

    async def request(body, headers):
        reader, writer = await asyncio.open_connection("127.0.0.1", service._bound_port)
        raw = canonical_json(body)
        lines = ["POST /api/v1/market_state HTTP/1.1", "Host: x",
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
        code, body = await request({}, None)
        assert code == 401 and body["error"] == "invalid_signature"
        envelope = sign_payload({}, SECRET, ts=NOW)
        code, body = await request({}, {"X-Signature": envelope["signature"],
                                        "X-Signature-Ts": f"{envelope['ts']:.3f}"})
        assert code == 200 and body["quotes"]["SOLUSD"]["bid"] == pytest.approx(119.99)
        server.close()

    asyncio.run(scenario())
