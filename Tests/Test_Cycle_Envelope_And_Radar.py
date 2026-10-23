"""Native-read and lot-grid regressions without broker submissions."""
from types import SimpleNamespace as NS
from datetime import datetime, timezone
import json
import numpy as np
import pytest
from Terminal import generate_cycle_envelope as envelope
from Terminal import run_comprehensive_universe_scanner as radar


class Broker:
    ORDER_TYPE_BUY, ORDER_TYPE_SELL = 0, 1
    ORDER_TYPE_BUY_LIMIT, ORDER_TYPE_SELL_LIMIT = 2, 3
    TRADE_ACTION_PENDING, ORDER_TIME_GTC, ORDER_FILLING_RETURN, TIMEFRAME_M15 = 5, 0, 2, 15

    def __init__(self):
        self.account = {"login": 5064568, "currency": "USD", "server": "BlueberryMarkets-SVG-Live",
                        "balance": 4865.07, "equity": 4865.07, "margin": 0., "margin_free": 4865.07}
        self.positions, self.orders, self.starts = [], [], []
        self.info = NS(name="BTCUSD.pi", path="Crypto", visible=True, trade_mode=4,
                       volume_min=.25, volume_max=2., volume_step=.25, trade_tick_size=.01)

    def account_info(self): return self.account
    def positions_get(self): return self.positions
    def orders_get(self): return self.orders
    def order_calc_profit(self, kind, symbol, volume, entry, stop): return -20 * volume
    def order_calc_margin(self, kind, symbol, volume, entry): return 100 * volume
    def symbols_get(self): return [self.info]
    def symbol_info_tick(self, symbol): return NS(bid=100., ask=100.01)
    def order_check(self, request): return NS(retcode=0)

    def copy_rates_from_pos(self, symbol, period, start, count):
        self.starts.append(start)
        return np.array([(99.8, 99.4, 99.6) for _ in range(count)],
                        dtype=[("high", "f8"), ("low", "f8"), ("close", "f8")])


def test_flat_baseline_reserves_contingency_and_selects_house_money():
    _, _, _, state = envelope.read_inventory(Broker())
    assert state["kernel_cushion_usd"] == 70.07
    assert state["realized_headroom_usd"] == 68.07
    assert state["new_risk_admissible"]
    assert (state["risk_min_usd"], state["risk_max_usd"], state["max_concurrent_tickets"]) == (15, 25, 2)
    assert 4865.07 - 2 - 2 * (25 * 1.25 + 2) == pytest.approx(4796.57)


@pytest.mark.parametrize("balance,risk", [(4819.99, 10.), (4820., 12.), (4850., 12.), (4850.01, 15.)])
def test_capital_tiers_match_preserved_governance(balance, risk):
    broker = Broker()
    broker.account.update(balance=balance, equity=balance)
    assert envelope.read_inventory(broker)[3]["risk_min_usd"] == risk


def test_existing_stress_is_not_rounded_before_candidate_arithmetic():
    broker = Broker()
    broker.orders = [dict(type=2, symbol="BTCUSD.pi", volume_current=.333333, price_open=100., sl=90.)]
    state = envelope.read_inventory(broker)[3]
    assert state["existing_ticket_stress_usd"] == pytest.approx(.333333 * 20 * 1.25 + 2)
    assert state["existing_ticket_stress_usd"] != round(state["existing_ticket_stress_usd"], 2)


def test_gap_floor_helper_preserves_kernel_above_evaluation_floor():
    from Terminal.dg_hardening import joint_floor_check
    checked = joint_floor_check(4865.07, 4865.07, [33.25, 33.25])
    assert checked["ok"] and checked["post_stress_equity_usd"] == pytest.approx(4796.57)
    assert checked["required_usd"] == 4795
    assert not joint_floor_check(4865.07, 4865.07, [80.0])["ok"]
    assert not joint_floor_check(4865.07, 4865.07, None)["ok"]


@pytest.mark.parametrize("field,value", [("login", 123), ("currency", "EUR"), ("balance", float("nan"))])
def test_identity_and_nonfinite_account_are_refused(field, value):
    broker = Broker()
    broker.account[field] = value
    with pytest.raises((RuntimeError, ValueError)):
        envelope.read_inventory(broker)


@pytest.mark.parametrize("field", ["positions", "orders"])
def test_none_inventory_is_unknown_not_flat(field):
    broker = Broker()
    setattr(broker, field, None)
    with pytest.raises(RuntimeError, match="inventory_unavailable"):
        envelope.read_inventory(broker)


def test_all_pending_fills_consume_stress_and_capacity():
    broker = Broker()
    broker.orders = [dict(type=2, symbol="BTCUSD.pi", volume_current=1.25, price_open=100., sl=90.)] * 2
    _, _, _, state = envelope.read_inventory(broker)
    assert state["existing_ticket_stress_usd"] == 66.50
    assert state["post_joint_stress_equity_usd"] == 4796.57
    assert not state["new_risk_admissible"]


def test_unprotected_position_freezes_envelope():
    broker = Broker()
    broker.positions = [dict(type=0, symbol="BTCUSD.pi", volume=1., price_current=100., sl=0.)]
    with pytest.raises(ValueError, match="invalid_inventory_stop"):
        envelope.read_inventory(broker)


def test_lot_search_never_rounds_up_past_budget_and_respects_margin():
    broker = Broker()
    sized = radar.lot_star(broker, broker.info, True, 100., 90., 24.9, 1000.)
    assert sized["lot"] == 1. and sized["risk_usd"] == 20.
    assert radar.lot_star(broker, broker.info, True, 100., 90., 25., 90.)["lot"] == .75
    assert radar.lot_star(broker, broker.info, True, 100., 90., 4., 1000.) is None


def test_readonly_radar_uses_completed_bars_and_never_authorizes_uncalibrated_candidates():
    broker = Broker()
    report = radar.scan(broker, datetime(2026, 10, 24, 12, tzinfo=timezone.utc))
    assert broker.starts == [1]
    assert report["total"] > 0
    for rows in report["pipeline"].values():
        for row in rows:
            assert 15 <= row["risk_usd"] <= 25
            assert row["stressed_equity"] >= 4795
            assert row["authorization"].startswith("WATCHLIST_ONLY")
            assert row["ev_net"] is None


def test_atomic_envelope_replacement_preserves_previous_on_serialization_failure(tmp_path):
    path = tmp_path / "cycle.json"
    envelope.atomic_json(path, {"generation": "previous"})
    with pytest.raises(ValueError):
        envelope.atomic_json(path, {"generation": float("nan")})
    assert json.loads(path.read_text()) == {"generation": "previous"}
    assert not list(tmp_path.glob("*.tmp.*"))
