"""Offline clock, actual HTF history and four-ticket capacity regression tests."""
import math
from types import SimpleNamespace as NS

import pytest

from Terminal.broker_clock import BrokerClock
from Terminal.decision_gates_v3 import pre_send_gate
from Terminal.dg_context import evaluate_candidate_dg_v3
from Terminal.Omni_Trader import AI15mMT5Trader


@pytest.mark.parametrize("offset", [-60.0, -29.0, 0.0, 29.0, 60.0])
def test_advancing_ticks_confirm_bounded_clock_offset(offset):
    clock = BrokerClock()
    assert clock.tick_age_seconds((1000 + offset) * 1000, symbol="BTC", now=1000, monotonic_now=10) is None
    assert clock.tick_age_seconds((1001 + offset) * 1000, symbol="BTC", now=1001, monotonic_now=11) == 0
    assert clock.offset_seconds == pytest.approx(offset)
    assert clock.utc_now(monotonic_now=12) == pytest.approx(1002 + offset)


def test_unchanged_tick_never_rejuvenates_even_when_host_clock_steps():
    clock = BrokerClock()
    clock.tick_age_seconds(1029000, symbol="BTC", now=1000, monotonic_now=10)
    clock.tick_age_seconds(1030000, symbol="BTC", now=1001, monotonic_now=11)
    for elapsed in (1, 3, 30, 90):
        assert clock.tick_age_seconds(1030000, symbol="BTC", now=1001 + elapsed - 29,
                                      monotonic_now=11 + elapsed) == pytest.approx(elapsed)


@pytest.mark.parametrize("stamp", [0, float("nan"), 1061000, 939000])
def test_unknown_or_outlier_clock_fails_closed(stamp):
    clock = BrokerClock()
    assert clock.tick_age_seconds(stamp, symbol="BTC", now=1000, monotonic_now=1) is None
    assert clock.utc_now(monotonic_now=2) is None


def test_cached_tick_cannot_confirm_skew_and_regressing_tick_is_rejected():
    clock = BrokerClock()
    assert clock.tick_age_seconds(1029000, symbol="BTC", now=1000, monotonic_now=1) is None
    assert clock.tick_age_seconds(1029000, symbol="BTC", now=1001, monotonic_now=2) is None
    assert clock.tick_age_seconds(1028000, symbol="BTC", now=1002, monotonic_now=3) is None


def test_delayed_advancing_tick_preserves_age_after_calibration():
    clock = BrokerClock()
    clock.tick_age_seconds(1000000, symbol="BTC", now=1000, monotonic_now=10)
    clock.tick_age_seconds(1001000, symbol="BTC", now=1001, monotonic_now=11)
    assert clock.tick_age_seconds(1002000, symbol="BTC", now=1008, monotonic_now=18) == 6
    assert clock.tick_age_seconds(1002000, symbol="BTC", now=1010, monotonic_now=20) == 8


def test_regressing_other_market_cannot_poison_or_rewind_shared_clock():
    clock = BrokerClock()
    clock.tick_age_seconds(1000000, symbol="BTC", now=1000, monotonic_now=10)
    clock.tick_age_seconds(1001000, symbol="BTC", now=1001, monotonic_now=11)
    assert clock.tick_age_seconds(950000, symbol="GOLD", now=1002, monotonic_now=12) == 52
    assert clock.tick_age_seconds(949000, symbol="GOLD", now=1003, monotonic_now=13) is None
    assert clock.tick_age_seconds(951000, symbol="GOLD", now=1003, monotonic_now=13) == 52
    assert clock.utc_now(now=1003, monotonic_now=13) == 1003


def test_repeated_tick_and_cadence_reject_host_step_over_sixty_seconds():
    clock = BrokerClock()
    clock.tick_age_seconds(1000000, symbol="BTC", now=1000, monotonic_now=10)
    clock.tick_age_seconds(1001000, symbol="BTC", now=1001, monotonic_now=11)
    assert clock.tick_age_seconds(1001000, symbol="BTC", now=1100, monotonic_now=12) is None
    assert clock.utc_now(now=1100, monotonic_now=12) is None
    assert clock.utc_now(now=1002, monotonic_now=12) == 1002


def test_native_cadence_uses_confirmed_utc_not_lagging_host(tmp_path):
    from Tests.Test_Omni_Engine import NOW, trader
    trading, broker = trader(tmp_path, clock=lambda: NOW-35, paper=False)
    broker.broker_utc_now = lambda: NOW
    report = trading.evaluate_market(multi_data={})
    assert report["slot"] == int(NOW//900)
    assert report.get("reason") != "outside_execution_window"
    assert report["cadence_time"] == NOW


def test_native_cadence_rejects_postclose_and_unverified_clock(tmp_path):
    from Tests.Test_Omni_Engine import NOW, trader
    trading, broker = trader(tmp_path, clock=lambda: NOW, paper=False)
    broker.broker_utc_now = lambda: NOW+31
    assert trading.evaluate_market(force=True)["reason"] == "outside_execution_window"
    broker.broker_utc_now = lambda: None
    assert trading.evaluate_market(force=True)["reason"] == "broker_quote_clock_unverified"
    with pytest.raises(ValueError, match="execution_window_expired"):
        trading._dispatch({}, int(NOW//900))
    assert not trading.state["intents"]


@pytest.mark.parametrize("entry_mode", ["limit", "market"])
def test_expiring_window_after_intent_preparation_is_proven_rejection(tmp_path, monkeypatch, entry_mode):
    from Tests.Test_Omni_Engine import NOW, trader
    from Terminal.risk.blackout_guard import BlackoutGuard
    trading, broker = trader(tmp_path, clock=lambda: NOW, paper=False)
    observations = iter([NOW, NOW, NOW+29])
    broker.broker_utc_now = lambda: next(observations)
    monkeypatch.setattr(BlackoutGuard, "get", lambda: NS(is_blocked=lambda moment: (False, "")))
    candidate = {"candidate_id": "expired", "entry_mode": entry_mode, "symbol": "BTCUSD",
                 "asset": "BTC", "direction": "LONG", "volume": .01,
                 "price_open": 99, "sl": 98, "tp": 102, "atr": 1}
    result = trading._dispatch(candidate, int(NOW//900))
    assert not result["success"] and not result.get("uncertain")
    assert next(iter(trading.state["intents"].values()))["status"] == "REJECTED"
    assert not broker.sent


def send_fixture():
    tick = NS(bid=100, ask=100.005, time_msc=1000000)
    info = NS(trade_mode=4, point=.01, trade_stops_level=0, volume_min=.1, volume_step=.1)
    broker = NS(symbol_info=lambda sym: info, symbol_info_tick=lambda sym: tick,
        account_info=lambda: NS(trade_allowed=True), terminal_info=lambda: NS(trade_allowed=True),
        orders_get=lambda **kw: [], positions_get=lambda: [], order_check=lambda req: NS(retcode=0),
        SYMBOL_TRADE_MODE_FULL=4, ORDER_TYPE_BUY_LIMIT=2)
    req = {"symbol": "BTC", "price": 99, "sl": 98, "tp": 102, "volume": .1, "type": 2, "comment": "unit"}
    plan = {"server_now_ms": 1000000, "mid_at_decision": 100, "atr": 10,
        "decision_age_s": 0, "joint_fill_ok": True, "spread_median_bps_this_hour": 0}
    return broker, req, plan


def test_pre_send_computes_actual_spread_and_rejects_unknown_inventory():
    broker, req, plan = send_fixture()
    assert pre_send_gate(broker, req, plan)[0]
    broker.orders_get = lambda **kw: None
    assert "broker_inventory_unavailable" in pre_send_gate(broker, req, plan)[1]
    broker.orders_get = lambda **kw: []
    broker.positions_get = lambda: None
    assert "broker_inventory_unavailable" in pre_send_gate(broker, req, plan)[1]


@pytest.mark.parametrize("age,reason", [(None, "tick_clock_unverified"), (3.0, "tick_stale_3000ms"), (-1, "tick_clock_unverified")])
def test_pre_send_uses_calibrated_tick_age(age, reason):
    broker, req, plan = send_fixture()
    assert reason in pre_send_gate(broker, req, plan, tick_age_seconds=lambda t, s: age)[1]


def test_pre_send_rejects_uncalibrated_future_tick():
    broker, req, plan = send_fixture()
    broker.symbol_info_tick("BTC").time_msc += 29000
    assert "tick_clock_unverified" in pre_send_gate(broker, req, plan)[1]


def actual_bars(count, duration, now):
    start = math.floor(now / duration) * duration - count * duration
    return [{"time": start + i * duration, "open": 100 + i, "high": 101 + i,
             "low": 99 + i, "close": 100 + i, "volume": i + 1} for i in range(count)]


def test_omni_reads_actual_h1_h4_depth_and_excludes_forming_bars(monkeypatch):
    from Terminal import Omni_Trader as module
    monkeypatch.setattr(module, "mt5", NS(TIMEFRAME_H1=60, TIMEFRAME_H4=240))
    now = 2000000
    histories = {60: actual_bars(60, 3600, now), 240: actual_bars(60, 14400, now)}
    for tf, duration in ((60, 3600), (240, 14400)):
        histories[tf].append({**histories[tf][-1], "time": math.floor(now / duration) * duration, "close": 999999})
    calls = []
    def read(symbol, *, count, timeframe):
        calls.append((count, timeframe))
        return histories[timeframe]
    trader = AI15mMT5Trader.__new__(AI15mMT5Trader)
    trader.bridge = NS(get_recent_bars=read)
    trader.bars_1h, trader.bars_4h = {}, {}
    trader._refresh_higher_timeframes("BTC", "BTCUSD", now)
    assert calls == [(96, 60), (96, 240)]
    assert len(trader.bars_1h["BTC"]) == len(trader.bars_4h["BTC"]) == 60
    assert trader.bars_1h["BTC"][-1]["close"] == 159
    assert trader.bars_4h["BTC"][-1]["close"] == 159


def test_insufficient_htf_history_does_not_fabricate_a_trend():
    result = evaluate_candidate_dg_v3({"direction": "LONG"}, {}, None,
        {"bid": 100, "ask": 101, "time_msc": 2000000000}, actual_bars(120, 900, 2000000),
        bars_1h=actual_bars(48, 3600, 2000000), bars_4h=actual_bars(35, 14400, 2000000))
    assert result["regime"] == "UNDEFINED"
    assert result["passed"] is False
    assert result["failures"] == ["regime_history_insufficient"]


def test_sufficient_actual_history_reaches_real_regime_classifier(monkeypatch):
    from Terminal import dg_context as module
    counts = []
    def classify(c15, c1h, c4h):
        counts.append(tuple(map(len, (c15, c1h, c4h))))
        return "UNDEFINED", {"actual_history": True}
    monkeypatch.setattr(module, "classify_regime", classify)
    result = module.evaluate_candidate_dg_v3({"direction": "LONG"}, {}, None,
        {"bid": 100, "ask": 101, "time_msc": 2000000000}, actual_bars(120, 900, 2000000),
        bars_1h=actual_bars(50, 3600, 2000000), bars_4h=actual_bars(50, 14400, 2000000))
    assert counts == [(120, 50, 50)]
    assert result["stats"] == {"actual_history": True}
    assert result["regime"] == "UNDEFINED"


@pytest.fixture
def timezone_bridge(monkeypatch):
    from Terminal import MT5_Execution_Bridge as module
    from Terminal import broker_clock as clock_module
    observed = NS(wall=1700000000.0, mono=100.0, reference_msc=1700010800000)
    fake_time = NS(time=lambda: observed.wall, monotonic=lambda: observed.mono)
    def reference_tick(symbol):
        assert symbol == "BTCUSD.pi", "Candidate quotes must not infer the broker timezone"
        return NS(time_msc=observed.reference_msc)
    monkeypatch.setattr(module, "MT5_AVAILABLE", True)
    monkeypatch.setattr(module, "mt5", NS(symbol_info_tick=reference_tick))
    monkeypatch.setattr(module, "time", fake_time)
    monkeypatch.setattr(clock_module, "time", fake_time)
    bridge = module.MT5ExecutionBridge.__new__(module.MT5ExecutionBridge)
    bridge.broker_utc_offset_sec, bridge.broker_utc_offset_ms = 10800, 10800000
    bridge.broker_clock = BrokerClock()
    return bridge, observed, module


def advance_reference(observed, *, timezone_seconds=10800):
    observed.wall += 1
    observed.mono += 1
    observed.reference_msc = int((observed.wall + timezone_seconds) * 1000)


def test_frozen_cfd_cannot_infer_timezone_and_rejuvenate_its_quote(timezone_bridge):
    bridge, observed, _ = timezone_bridge
    assert bridge.tick_age_seconds(NS(time_msc=observed.reference_msc), "BTCUSD.pi") is None
    advance_reference(observed)
    assert bridge.tick_age_seconds(NS(time_msc=observed.reference_msc), "BTCUSD.pi") == 0
    frozen = NS(time_msc=int((observed.wall + 10800 - 7200) * 1000))
    assert bridge.tick_age_seconds(frozen, "CLOSED_CFD") == 7200
    assert bridge.broker_utc_offset_sec == 10800
    advance_reference(observed)
    assert bridge.tick_age_seconds(frozen, "CLOSED_CFD") == 7201


def test_dst_change_requires_two_advancing_reference_ticks(timezone_bridge):
    bridge, observed, _ = timezone_bridge
    assert bridge._utc_offset_seconds("ANY_CFD") == 10800
    advance_reference(observed)
    assert bridge._utc_offset_seconds("ANY_CFD") == 10800
    advance_reference(observed, timezone_seconds=7200)
    assert bridge._utc_offset_seconds("ANY_CFD") == 10800
    observed.wall += 1
    observed.mono += 1
    assert bridge._utc_offset_seconds("ANY_CFD") == 10800  # cached reference
    advance_reference(observed, timezone_seconds=7200)
    assert bridge._utc_offset_seconds("ANY_CFD") == 7200
    assert bridge._normalize_tick_msc(observed.reference_msc, "ANY_CFD") == int(observed.wall * 1000)


def test_legitimately_confirmed_utc_zero_has_no_default_offset_fallback(timezone_bridge):
    bridge, observed, _ = timezone_bridge
    observed.reference_msc = int(observed.wall * 1000)
    assert bridge._utc_offset_seconds("ANY_CFD") == 10800
    advance_reference(observed, timezone_seconds=0)
    assert bridge._utc_offset_seconds("ANY_CFD") == 0
    assert bridge._normalize_tick_msc(observed.reference_msc, "ANY_CFD") == observed.reference_msc
    assert bridge.broker_utc_offset_ms == 0


def test_bars_share_confirmed_timezone_even_when_candidate_market_is_closed(timezone_bridge):
    import numpy as np
    bridge, observed, module = timezone_bridge
    bridge.ensure_connected = lambda: True
    raw = np.array([(int(observed.wall + 10800 - 7200), 100., 101., 99., 100., 10.)],
                   dtype=[("time", "i8"), ("open", "f8"), ("high", "f8"),
                          ("low", "f8"), ("close", "f8"), ("tick_volume", "f8")])
    module.mt5.symbol_select = lambda *args: True
    module.mt5.copy_rates_from_pos = lambda *args: raw
    bars = bridge.get_recent_bars("CLOSED_CFD", timeframe=60)
    assert bars[0]["time"] == observed.wall - 7200
    assert bridge.broker_utc_offset_sec == 10800
