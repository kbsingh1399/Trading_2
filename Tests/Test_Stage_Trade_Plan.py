"""Offline deterministic tests for the OX_ALPHA_62 fail-closed plan stager.

Every network surface is a scripted fake; nothing here touches the tunnel.
The suite pins the governance envelope (risk band, ATR floor, target band,
tick/step alignment, blackout, expiry), the fail-closed live gates (transport,
freshness, macro, equity floor, capacity, marketable limit, contract mismatch,
spread-in-R) and the exact signed-submission payload.
"""

from __future__ import annotations

import copy
import json
import math
from pathlib import Path

import pytest

from Terminal.Headless.stage_trade_plan import (
    MAX_RISK_USD,
    MIN_RISK_USD,
    PlanValidationError,
    execute_plan,
    live_precheck,
    purge_expired,
    stage,
    validate_plan,
    _main,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
COMMITTED_PLAN = REPO_ROOT / "docs/trade_plans/OX_ALPHA_62_SOL_Long_20261007.json"

# 2026-10-07 00:00 UTC: inside the plan validity window, outside the declared
# FOMC blackout (17:00-18:30 UTC the same day).
NOW = 1791331200.0

BASE_PLAN = {
    "plan_version": "omni.trade_plan.v1",
    "plan_id": "TEST-SOL-LONG",
    "asset": "SOL",
    "symbol": "SOLUSD.p",
    "direction": "LONG",
    "limit_price": 119.95,
    "sl": 119.25,
    "tp": 121.70,
    "volume": 0.15,
    "risk_usd": 10.50,
    "atr": 0.46123,
    "tp_r": 2.5,
    "ttl_bars": 24,
    "comment": "ARENA:PLAN_v1",
    "created_at_epoch": 1791315000.0,
    "expires_at_epoch": 1791374400.0,
    "max_friction_r": 0.35,
    "blackout_windows": [
        {"start_epoch": 1791392400.0, "end_epoch": 1791397800.0,
         "reason": "FOMC minutes 18:00 UTC"},
    ],
    "contract": {"tick_size": 0.01, "contract_size": 100.0,
                 "min_lot": 0.01, "step_lot": 0.01, "digits": 2},
}


def plan(**overrides) -> dict:
    doc = copy.deepcopy(BASE_PLAN)
    doc.update(overrides)
    return doc


GOOD_STATE = {
    "service": "omni.headless.v1",
    "as_of": NOW,
    "positions": [
        {"ticket": 18576872, "symbol": "XAUUSD.pi", "direction": "SHORT",
         "volume": 0.01, "entry": 4176.0, "sl": 4186.5, "contract_size": 100.0},
    ],
    "pending_orders": [],
    "quotes": {
        "XAUUSD.pi": {"bid": 4166.79, "ask": 4167.13, "tick_size": 0.01,
                      "contract_size": 100.0, "min_lot": 0.01,
                      "step_lot": 0.01, "digits": 2},
        "SOLUSD.p": {"bid": 120.31, "ask": 120.39, "tick_size": 0.01,
                     "contract_size": 100.0, "min_lot": 0.01,
                     "step_lot": 0.01, "digits": 2},
    },
    "symbols": {"SOL": "SOLUSD.p"},
    "macro": {"blackout_active": False, "blackout_event": None},
    "account": {"balance_usd": 4833.15, "equity_usd": 4839.88,
                "margin_free_usd": 4422.28},
}


class FakeClient:
    """Scripted tunnel double: captures every mutating call."""

    def __init__(self, state=None, stage_result=None, cancel_result=None):
        self.state = copy.deepcopy(state if state is not None else GOOD_STATE)
        self.stage_result = (stage_result if stage_result is not None
                             else {"ok": True, "ticket": 424242,
                                   "risk_usd": 10.5})
        self.cancel_result = cancel_result if cancel_result is not None \
            else {"ok": True}
        self.calls = []

    def market_state(self, assets=None):
        return self.state

    def stage_order(self, **kwargs):
        self.calls.append(("stage", kwargs))
        return self.stage_result

    def cancel_order(self, ticket):
        self.calls.append(("cancel", ticket))
        return self.cancel_result


def state(**overrides) -> dict:
    doc = copy.deepcopy(GOOD_STATE)
    doc.update(overrides)
    return doc


def refusal_code(plan_doc, now=NOW) -> str:
    with pytest.raises(PlanValidationError) as excinfo:
        validate_plan(plan_doc, now=now)
    return excinfo.value.code


# ------------------------------------------------------------ offline gates
def test_committed_plan_document_validates():
    """The real plan JSON in docs/trade_plans must pass its own validator."""
    doc = json.loads(COMMITTED_PLAN.read_text(encoding="utf-8"))
    normalised = validate_plan(doc, now=NOW)
    assert normalised["symbol"] == "SOLUSD.p"
    assert normalised["direction"] == "LONG"
    assert normalised["computed_risk_usd"] == pytest.approx(10.50, abs=1e-6)
    assert normalised["computed_tp_r"] == pytest.approx(2.50, abs=1e-6)


def test_geometry_and_sizing_recomputed():
    normalised = validate_plan(plan(), now=NOW)
    distance = 119.95 - 119.25
    assert distance / normalised["atr"] == pytest.approx(1.5175, abs=1e-3)
    assert normalised["computed_risk_usd"] == pytest.approx(
        0.15 * distance * 100.0, abs=1e-9)
    assert MIN_RISK_USD <= normalised["computed_risk_usd"] <= MAX_RISK_USD


def test_risk_outside_band_rejected():
    assert refusal_code(plan(volume=0.30, risk_usd=21.0)) == "risk_above_cap"
    assert refusal_code(plan(volume=0.14, risk_usd=9.80)) == "risk_below_floor"


def test_declared_risk_mismatch_rejected():
    assert refusal_code(plan(risk_usd=12.0)) == "declared_risk_mismatch"


def test_tp_outside_band_rejected():
    assert refusal_code(plan(tp=121.00)) == "tp_outside_band"
    assert refusal_code(plan(tp=123.00)) == "tp_outside_band"


def test_sl_inside_atr_floor_rejected():
    # 119.60 leaves 0.35 = 0.76 x ATR, inside the 1.5 x ATR floor.
    assert refusal_code(plan(sl=119.60)) == "sl_inside_atr_floor"


def test_volume_feasibility_rejected():
    assert refusal_code(plan(volume=0.005)) == "volume_below_min_lot"
    assert refusal_code(plan(volume=0.155)) == "volume_off_step"


def test_price_off_tick_rejected():
    assert refusal_code(plan(limit_price=119.955)) == "price_off_tick"


def test_geometry_direction_and_comment_rejected():
    assert refusal_code(plan(sl=120.50)) == "geometry_violation"
    assert refusal_code(plan(direction="BUY")) == "invalid_direction"
    assert refusal_code(plan(comment="SOL PLAN")) == "invalid_comment_prefix"


def test_validity_window_and_blackout_rejected():
    assert refusal_code(plan(), now=1791374401.0) == "plan_expired"
    assert refusal_code(plan(created_at_epoch=NOW + 600.0)) == \
        "plan_created_in_future"
    # Blackout is reachable only while the plan is still valid: extend expiry.
    assert refusal_code(plan(expires_at_epoch=1791417600.0),
                        now=1791393000.0) == "blackout_active"


def test_missing_field_and_version_rejected():
    doc = plan()
    del doc["sl"]
    assert refusal_code(doc) == "missing_field"
    assert refusal_code(plan(plan_version="omni.trade_plan.v0")) == \
        "unsupported_plan_version"


# -------------------------------------------------------------- live gates
def test_live_precheck_passes_with_full_report():
    report = live_precheck(FakeClient(), validate_plan(plan(), now=NOW), now=NOW)
    assert report["ok"] is True and report["reason"] is None
    checks = report["checks"]
    assert checks["macro"] == "clear"
    assert checks["capacity"] == {"filled": 1, "pending": 0}
    assert checks["friction"]["friction_r"] == pytest.approx(
        round((120.39 - 120.31 + 0.01) / 0.70, 4), abs=1e-9)
    assert checks["account"]["cushion_above_floor_usd"] == pytest.approx(
        4839.88 - 10.50 - 10.50 - 4775.0, abs=0.01)


def test_live_precheck_refuses_transport_and_stale_state():
    down = live_precheck(FakeClient(state={"http_status": 0,
                                           "error": "tunnel_unreachable:x"}),
                         validate_plan(plan(), now=NOW), now=NOW)
    assert down["ok"] is False and down["reason"] == "tunnel_unreachable"
    stale = live_precheck(FakeClient(state=state(as_of=NOW - 500.0)),
                          validate_plan(plan(), now=NOW), now=NOW)
    assert stale["ok"] is False and stale["reason"] == "market_state_stale"


def test_live_precheck_refuses_macro_blackout():
    blocked = live_precheck(
        FakeClient(state=state(macro={"blackout_active": True,
                                      "blackout_event": "FOMC_MINUTES"})),
        validate_plan(plan(), now=NOW), now=NOW)
    assert blocked["ok"] is False and blocked["reason"] == "macro_blackout"


def test_live_precheck_refuses_equity_floor_breach():
    """Equity 4,790 minus 10.50 existing risk minus 10.50 plan risk lands
    6.00 USD under the 4,775.00 hard floor -> NO TRADE."""
    squeezed = live_precheck(FakeClient(state=state(
        account={"balance_usd": 4780.0, "equity_usd": 4790.0,
                 "margin_free_usd": 4400.0})),
        validate_plan(plan(), now=NOW), now=NOW)
    assert squeezed["ok"] is False and squeezed["reason"] == "equity_floor_breach"


def test_live_precheck_refuses_capacity_exhaustion():
    two_filled = state(positions=[
        {"ticket": 1, "symbol": "XAUUSD.pi", "direction": "SHORT",
         "volume": 0.01, "entry": 4176.0, "sl": 4186.5, "contract_size": 100.0},
        {"ticket": 2, "symbol": "SOLUSD.p", "direction": "LONG",
         "volume": 0.15, "entry": 119.95, "sl": 119.25, "contract_size": 100.0},
    ])
    assert live_precheck(FakeClient(state=two_filled),
                         validate_plan(plan(), now=NOW), now=NOW)["reason"] == \
        "max_filled_positions"

    four_pending = state(pending_orders=[{"ticket": 10 + i} for i in range(4)])
    report = live_precheck(FakeClient(state=four_pending),
                           validate_plan(plan(), now=NOW), now=NOW)
    assert report["ok"] is False and report["reason"] == "pending_limit_ceiling"


def test_live_precheck_refuses_marketable_limit_and_contract_mismatch():
    marketable = live_precheck(FakeClient(state=state(quotes={
        **GOOD_STATE["quotes"],
        "SOLUSD.p": {"bid": 119.85, "ask": 119.90, "tick_size": 0.01,
                     "contract_size": 100.0, "min_lot": 0.01,
                     "step_lot": 0.01, "digits": 2}})),
        validate_plan(plan(), now=NOW), now=NOW)
    assert marketable["ok"] is False and marketable["reason"] == "marketable_limit"

    mismatch = live_precheck(FakeClient(state=state(quotes={
        **GOOD_STATE["quotes"],
        "SOLUSD.p": {"bid": 120.31, "ask": 120.39, "tick_size": 0.01,
                     "contract_size": 10.0, "min_lot": 0.01,
                     "step_lot": 0.01, "digits": 2}})),
        validate_plan(plan(), now=NOW), now=NOW)
    assert mismatch["ok"] is False and mismatch["reason"] == "contract_mismatch"


def test_live_precheck_refuses_excessive_spread():
    wide = live_precheck(FakeClient(state=state(quotes={
        **GOOD_STATE["quotes"],
        "SOLUSD.p": {"bid": 119.30, "ask": 120.00, "tick_size": 0.01,
                     "contract_size": 100.0, "min_lot": 0.01,
                     "step_lot": 0.01, "digits": 2}})),
        validate_plan(plan(), now=NOW), now=NOW)
    assert wide["ok"] is False and wide["reason"] == "friction_excessive"
    assert wide["checks"]["friction"]["friction_r"] == pytest.approx(
        round(0.71 / 0.70, 4), abs=1e-9)


# -------------------------------------------------------------- execution
def test_execute_submits_exact_signed_params_and_journals():
    client = FakeClient()
    rows = []
    outcome = execute_plan(client, validate_plan(plan(), now=NOW),
                           journal=rows.append, now=NOW)
    assert outcome["ok"] is True
    assert client.calls == [("stage", {
        "symbol": "SOLUSD.p", "direction": "LONG", "volume": 0.15,
        "limit_price": 119.95, "sl": 119.25, "tp": 121.70,
        "comment": "ARENA:PLAN_v1", "expiration_seconds": 21600})]
    assert rows[0]["event"] == "staged" and rows[0]["ticket"] == 424242
    assert rows[0]["expires_at_epoch"] == NOW + 21600


def test_execute_stage_failure_is_reported_not_raised():
    client = FakeClient(stage_result={"http_status": 500, "error": "boom"})
    rows = []
    outcome = execute_plan(client, validate_plan(plan(), now=NOW),
                           journal=rows.append, now=NOW)
    assert outcome["ok"] is False
    assert rows[0]["event"] == "stage_failed"


def test_stage_orchestrator_dry_run_then_execute(tmp_path):
    doc_path = tmp_path / "plan.json"
    doc_path.write_text(json.dumps(plan()), encoding="utf-8")

    dry = FakeClient()
    journal = tmp_path / "journal.jsonl"
    assert stage(dry, str(doc_path), execute=False, now=NOW,
                 journal_path=str(journal)) == 0
    assert dry.calls == []                       # dry run never submits
    assert json.loads(journal.read_text().splitlines()[0])["event"] == "validated"

    live = FakeClient()
    assert stage(live, str(doc_path), execute=True, now=NOW,
                 journal_path=str(journal)) == 0
    assert [c[0] for c in live.calls] == ["stage"]
    events = [json.loads(line)["event"] for line in
              journal.read_text().splitlines()]
    assert events == ["validated", "staged"]


def test_stage_orchestrator_exit_codes(tmp_path):
    doc_path = tmp_path / "plan.json"
    doc_path.write_text(json.dumps(plan(volume=0.30, risk_usd=21.0)),
                        encoding="utf-8")
    assert stage(FakeClient(), str(doc_path), now=NOW) == 2      # offline refusal

    doc_path.write_text(json.dumps(plan()), encoding="utf-8")
    blocked = FakeClient(state=state(macro={"blackout_active": True,
                                             "blackout_event": "FOMC"}))
    assert stage(blocked, str(doc_path), execute=True, now=NOW) == 3  # live refusal

    failing = FakeClient(stage_result={"http_status": 0,
                                       "error": "tunnel_unreachable:x"})
    assert stage(failing, str(doc_path), execute=True, now=NOW) == 4  # stage failure


def test_purge_expired_cancels_only_stale_tickets(tmp_path):
    journal = tmp_path / "journal.jsonl"
    rows = [
        {"ts": 1, "event": "staged", "ticket": 111, "plan_id": "A",
         "expires_at_epoch": NOW - 100.0},
        {"ts": 2, "event": "staged", "ticket": 222, "plan_id": "B",
         "expires_at_epoch": NOW + 9999.0},
        {"ts": 3, "event": "staged", "ticket": 333, "plan_id": "C",
         "expires_at_epoch": NOW - 100.0},
        {"ts": 4, "event": "purged", "ticket": 333},
    ]
    journal.write_text("\n".join(json.dumps(r) for r in rows) + "\n",
                       encoding="utf-8")
    client = FakeClient()
    assert purge_expired(client, str(journal), now=NOW) == 0
    assert client.calls == [("cancel", 111)]     # fresh 222 and done 333 untouched
    appended = [json.loads(line) for line in journal.read_text().splitlines()][4:]
    assert appended == [{"ts": NOW, "event": "purged", "ticket": 111,
                         "plan_id": "A"}]


def test_cli_main_validate_dry_run(tmp_path):
    import time as _time
    doc_path = tmp_path / "plan.json"
    doc_path.write_text(json.dumps(plan()), encoding="utf-8")
    # The CLI resolves `now` from the wall clock, so the scripted state must
    # carry a fresh as_of (real construction time) for the freshness gate.
    fake = FakeClient(state=state(as_of=_time.time()))
    journal = tmp_path / "cli_journal.jsonl"     # never touch the default path
    code = _main([str(doc_path), "--url", "https://tunnel.example",
                  "--secret", "s3cret", "--journal", str(journal)],
                 client_factory=lambda: fake)
    assert code == 0
    assert fake.calls == []                      # no --execute -> no submission
    assert json.loads(journal.read_text().splitlines()[0])["event"] == "validated"
