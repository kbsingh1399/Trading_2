"""Offline adversarial checks for the forensic certificate's evidence gates."""
import importlib.util
import json
import os
import sys
import time
from pathlib import Path
from types import SimpleNamespace as NS

import polars as pl
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from Terminal import chain_verification_360 as audit
from Terminal.policy import HTF_STRATEGY_MIN


@pytest.fixture
def native(monkeypatch):
    fake = NS(initialize=lambda: True, shutdown=lambda: None,
              terminal_info=lambda: NS(connected=True, trade_allowed=True),
              account_info=lambda: NS(login=5064568, currency="USD", balance=4896.55,
                                      equity=4896.55, margin=0.0, margin_free=4896.55, margin_level=0.0),
              positions_get=lambda: [], orders_get=lambda: [],
              history_deals_get=lambda *args: [], order_calc_profit=lambda *args: -10.0,
              last_error=lambda: (-1, "simulated failure"))
    monkeypatch.setitem(sys.modules, "MetaTrader5", fake)
    return fake


def ticket(**changes):
    fields = dict(ticket=1, symbol="BTCUSD.pi", volume=1.0, volume_current=1.0,
                  type=0, price_open=100.0, price_current=100.0, sl=90.0, tp=125.0,
                  profit=0.0, swap=0.0)
    return NS(**(fields | changes))


@pytest.mark.parametrize("inventory", ["positions_get", "orders_get"])
def test_native_unknown_inventory_cannot_become_a_flat_pass(native, inventory):
    setattr(native, inventory, lambda: None)
    report = audit.audit_broker_execution_and_floor()
    assert report["status"] == "FAIL" and not report["inventory_verified"]


@pytest.mark.parametrize("change", [dict(login=1), dict(currency="EUR")])
def test_native_wrong_account_or_currency_fails(native, change):
    account = native.account_info().__dict__ | change
    native.account_info = lambda: NS(**account)
    assert audit.audit_broker_execution_and_floor()["status"] == "FAIL"


def test_disconnected_terminal_fails_even_with_account_data(native):
    native.terminal_info = lambda: NS(connected=False)
    assert audit.audit_broker_execution_and_floor()["status"] == "FAIL"


@pytest.mark.parametrize("row", [ticket(sl=0), ticket(type=99), ticket(type=6, sl=110)])
def test_unprotected_or_unsupported_pending_inventory_fails(native, row):
    native.orders_get = lambda: [row]
    assert audit.audit_broker_execution_and_floor()["status"] == "FAIL"


def test_native_stop_valuation_failure_never_falls_back_to_contract_size(native):
    native.positions_get = lambda: [ticket()]
    native.order_calc_profit = lambda *args: None
    assert audit.audit_broker_execution_and_floor()["status"] == "FAIL"


def test_stress_and_execution_costs_can_reject_a_nominal_floor_pass(native):
    native.account_info = lambda: NS(login=5064568, currency="USD", balance=4810.0,
                                    equity=4810.0, margin=0, margin_free=4810, margin_level=0)
    native.orders_get = lambda: [ticket(type=6)]
    native.order_calc_profit = lambda *args: -14.0
    report = audit.audit_broker_execution_and_floor()
    assert 4810 - 14 > 4795  # old nominal-only audit would pass
    assert report["status"] == "FAIL"
    assert report["stressed_worst_case_equity_usd"] == 4790.5
    assert report["downside_portfolio_risk_usd"] == 19.5


def test_locked_profit_is_not_credit_against_other_tickets(native):
    native.positions_get = lambda: [ticket(sl=110), ticket(ticket=2)]
    native.order_calc_profit = lambda kind, symbol, volume, entry, stop: 100.0 if stop > entry else -10.0
    report = audit.audit_broker_execution_and_floor()
    assert report["status"] == "PASS"
    assert report["downside_portfolio_risk_usd"] == 16.5


def test_four_joint_fill_slots_include_pending_contingent_fills(native):
    native.orders_get = lambda: [ticket(type=2, ticket=index) for index in range(5)]
    assert audit.audit_broker_execution_and_floor()["status"] == "FAIL"


def snapshot(now):
    assets = {}
    for asset in audit.PRIMARY_ASSETS:
        row = {"htf_history": {}}
        for key, interval in (("1h", 3600), ("4h", 14400)):
            row[f"htf_{key}_ohlcv"] = [dict(ts=now - (HTF_STRATEGY_MIN+1-i)*interval,
                close_ts=now-(HTF_STRATEGY_MIN-i)*interval, open=100, high=101, low=99, close=100)
                for i in range(HTF_STRATEGY_MIN)]
            row["htf_history"][key] = dict(completed_count=HTF_STRATEGY_MIN, status="READY", freshness="FRESH",
                                          source="MT5_BROKER_COMPLETED_BARS")
        assets[asset] = row
    return dict(as_of_epoch=now, account=dict(login=5064568, currency="USD",
                balance_usd=4896.55, equity_usd=4896.55), active_positions=[], pending_orders=[],
                capacity=dict(max_concurrent=4, used_joint_fill=0), assets_matrix_24=assets)


@pytest.fixture
def payload(monkeypatch, tmp_path):
    now = 1791600000.0
    path = tmp_path / "snapshot.json"
    monkeypatch.setattr(audit, "TELEMETRY_FILE", path)
    monkeypatch.setattr(audit, "_audit_epoch", lambda: now)
    monkeypatch.setattr(audit, "_clock_verified", lambda: True)
    value = snapshot(now)
    path.write_text(json.dumps(value))
    return value, path, now


def test_real_assets_schema_and_complete_native_parity_can_pass(native, payload):
    assert audit.audit_telemetry_snapshot_integrity()["status"] == "PASS"


@pytest.mark.parametrize("count", [35, 49])
def test_insufficient_strategy_history_cannot_claim_ready(native, payload, count):
    value, path, _ = payload
    row = value["assets_matrix_24"]["BTC"]
    row["htf_1h_ohlcv"] = row["htf_1h_ohlcv"][-count:]
    row["htf_history"]["1h"]["completed_count"] = count
    path.write_text(json.dumps(value))
    assert audit.audit_telemetry_snapshot_integrity()["status"] == "FAIL"


@pytest.mark.parametrize("movement", [.05, -10.0])
def test_unchanged_inventory_equity_movement_is_not_snapshot_corruption(native, payload, movement):
    value, path, now = payload
    position = ticket()
    native.positions_get = lambda: [position]
    original = native.account_info
    native.account_info = lambda: NS(**(original().__dict__ | {"equity": 4896.55 + movement}))
    value["active_positions"] = [{key: getattr(position, key) for key in
                                 ("ticket", "symbol", "volume", "price_open", "sl", "tp")}]
    value["capacity"]["used_joint_fill"] = 1
    value["as_of_epoch"] = now-1
    path.write_text(json.dumps(value))
    report = audit.audit_telemetry_snapshot_integrity()
    assert report["status"] == "PASS"
    assert report["equity_movement_since_snapshot_usd"] == pytest.approx(movement)


@pytest.mark.parametrize("delta", [-1000, 10])
def test_file_touch_does_not_rejuvenate_old_or_future_payload(native, payload, delta):
    value, path, now = payload
    value["as_of_epoch"] = now + delta
    path.write_text(json.dumps(value))
    os.utime(path, (now, now))
    assert audit.audit_telemetry_snapshot_integrity()["status"] == "FAIL"


def test_future_htf_bar_is_rejected_even_when_quality_claims_ready(native, payload):
    value, path, now = payload
    bar = value["assets_matrix_24"]["BTC"]["htf_4h_ohlcv"][-1]
    bar.update(ts=now, close_ts=now+14400)
    path.write_text(json.dumps(value))
    assert audit.audit_telemetry_snapshot_integrity()["status"] == "FAIL"


def test_claimed_htf_count_cannot_replace_actual_observations(native, payload):
    value, path, _ = payload
    value["assets_matrix_24"]["BTC"]["htf_1h_ohlcv"] = []
    path.write_text(json.dumps(value))
    assert audit.audit_telemetry_snapshot_integrity()["status"] == "FAIL"


def test_native_pending_ticket_missing_from_telemetry_is_rejected(native, payload):
    native.orders_get = lambda: [ticket(type=2)]
    assert audit.audit_telemetry_snapshot_integrity()["status"] == "FAIL"


def test_unverified_clock_does_not_certify_a_fresh_file(native, payload, monkeypatch):
    monkeypatch.setattr(audit, "_clock_verified", lambda: False)
    assert audit.audit_telemetry_snapshot_integrity()["status"] == "UNKNOWN"


def test_diagnostic_features_do_not_claim_proven_causality(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "CANDLES_DIR", tmp_path)
    now = time.time()
    pl.DataFrame({"time": [int(now)-(220-i)*900 for i in range(220)],
                  "open": [100.0]*220, "high": [101.0]*220, "low": [99.0]*220,
                  "close": [100.0]*220, "tick_volume": [10.0]*220}).write_parquet(tmp_path / "BTC_15m.parquet")
    report = audit.audit_causal_feature_processing()
    assert report["status"] == "UNKNOWN"
    assert report["anti_lookahead_causal_verified"] is None
    assert report["vwap_reset_verified"] is None


@pytest.mark.parametrize("status", ["UNKNOWN", "FAIL", "WARN", "SKIP", None, "garbage"])
def test_any_nonpass_pillar_prevents_pristine_certificate(monkeypatch, status):
    functions = ["audit_mt5_live_data_source", "audit_binance_l2_data_source",
                 "audit_parquet_candle_archives", "audit_causal_feature_processing",
                 "audit_telemetry_snapshot_integrity", "audit_broker_execution_and_floor"]
    for name in functions:
        monkeypatch.setattr(audit, name, lambda *args: {"status": "PASS"})
    monkeypatch.setattr(audit, functions[0], lambda: {"status": status})
    assert audit.run_360_degree_chain_verification()["overall_verdict"] != "CERTIFIED_100_PERCENT_PRISTINE"


def parity_module():
    path = Path(__file__).resolve().parents[1] / ".agents/scripts/verify_and_sync_agents.py"
    spec = importlib.util.spec_from_file_location("agent_parity_audit", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_parity_comparison_oserror_is_failure(tmp_path, monkeypatch):
    module = parity_module()
    for name in (".agents", "Engine_2/.agents"):
        root = tmp_path / name
        root.mkdir(parents=True)
        (root / "context.md").write_text("same bytes")
    def unreadable(*args, **kwargs):
        raise PermissionError("simulated unreadable file")
    monkeypatch.setattr(module.filecmp, "cmp", unreadable)
    assert not module.sync_agents(tmp_path, check_only=True)


def test_parity_scan_error_is_failure_even_when_no_files_visible(tmp_path, monkeypatch):
    module = parity_module()
    (tmp_path / ".agents").mkdir()
    (tmp_path / "Engine_2/.agents").mkdir(parents=True)
    def unreadable(root, onerror):
        onerror(PermissionError("simulated unreadable tree"))
        return []
    monkeypatch.setattr(module.os, "walk", unreadable)
    assert not module.sync_agents(tmp_path, check_only=True)
