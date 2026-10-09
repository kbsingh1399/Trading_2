import json
from datetime import datetime, timezone

from Terminal.Macro_Calendar import refresh_calendar
from Terminal.Market_Intelligence import MarketIntelligenceEngine
from Terminal.risk import blackout_guard


def test_explicit_half_hour_blackout_is_enforced_by_both_consumers(tmp_path, monkeypatch):
    event = {"name": "Retail Sales", "impact": "HIGH", "time_utc": "2026-10-15T12:30:00Z",
             "currency": "USD", "pre_blackout_m": 30, "post_blackout_m": 30}
    path = tmp_path / "calendar.json"
    path.write_text(json.dumps({"required_series": ["CPI", "NFP", "FOMC"],
                               "coverage_start": "2026-10-01T00:00:00Z",
                               "coverage_end": "2026-11-01T00:00:00Z", "events": [event]}))
    monkeypatch.setattr(blackout_guard, "_CALENDAR_JSON", path)
    guard = blackout_guard.BlackoutGuard()
    for text, expected in [("2026-10-15T11:59:59+00:00", False),
                           ("2026-10-15T12:00:00+00:00", True),
                           ("2026-10-15T12:50:00+00:00", True),
                           ("2026-10-15T13:00:00+00:00", False)]:
        now = datetime.fromisoformat(text)
        intel = MarketIntelligenceEngine(calendar_path=path, clock=lambda: now.timestamp())
        assert intel.check_macro_blackout()[0] is expected
        assert guard.is_blocked(now)[0] is expected


def test_refresh_keeps_verified_supplemental_events_and_core_windows(tmp_path):
    path = tmp_path / "calendar.json"
    supplemental = {"name": "Retail Sales", "time_utc": "2026-10-15T12:30:00Z",
                    "impact": "HIGH", "source": "https://www.census.gov/retail/release_schedule.html",
                    "currency": "USD", "pre_blackout_m": 30, "post_blackout_m": 30}
    path.write_text(json.dumps({"events": [supplemental, {"name": "CPI",
                               "time_utc": "2026-10-14T12:30:00Z", "pre_blackout_m": 30,
                               "post_blackout_m": 30, "currency": "USD"}]}))
    bls = "BEGIN:VEVENT\nSUMMARY:Consumer Price Index\nDTSTART:20261014T123000Z\nEND:VEVENT\nBEGIN:VEVENT\nSUMMARY:Employment Situation\nDTSTART:20261002T123000Z\nEND:VEVENT"
    fed = '<div><h4>FOMC Meetings</h4></div><div><div class="panel-body"><div><div>2:00 p.m.</div><div>FOMC Meeting</div><div>28</div></div></div></div><div><h4>Other</h4></div>'
    result = refresh_calendar(path, datetime(2026, 10, 10, tzinfo=timezone.utc),
                              lambda url: bls if url.endswith(".ics") else fed)
    assert supplemental in result["events"]
    cpi = next(e for e in result["events"] if e["name"] == "CPI")
    assert cpi["pre_blackout_m"] == cpi["post_blackout_m"] == 30


def test_invalid_blackout_buffer_fails_closed(tmp_path, monkeypatch):
    path = tmp_path / "calendar.json"
    path.write_text(json.dumps({"required_series": ["CPI", "NFP", "FOMC"],
                               "coverage_start": "2026-10-01T00:00:00Z",
                               "coverage_end": "2026-11-01T00:00:00Z",
                               "events": [{"name": "CPI", "impact": "HIGH",
                                           "time_utc": "2026-10-14T12:30:00Z",
                                           "pre_blackout_m": -1}]}))
    now = datetime(2026, 10, 10, tzinfo=timezone.utc)
    monkeypatch.setattr(blackout_guard, "_CALENDAR_JSON", path)
    assert blackout_guard.BlackoutGuard().is_blocked(now)[0]
    assert MarketIntelligenceEngine(calendar_path=path, clock=lambda: now.timestamp()).check_macro_blackout()[0]


def test_expired_calendar_cannot_open_the_order_gate(tmp_path, monkeypatch):
    path = tmp_path / "calendar.json"
    path.write_text(json.dumps({"coverage_start": "2026-10-01T00:00:00Z",
                               "coverage_end": "2026-10-19T00:00:00Z",
                               "events": [{"name": "CPI", "impact": "HIGH",
                                           "time_utc": "2026-10-14T12:30:00Z"}]}))
    monkeypatch.setattr(blackout_guard, "_CALENDAR_JSON", path)
    assert blackout_guard.BlackoutGuard().is_blocked(datetime(2026, 10, 20, tzinfo=timezone.utc))[0]


def test_telemetry_calendar_uses_the_same_half_hour_window(tmp_path):
    from Terminal.Data_Factory.generate_telemetry_snapshot import calendar_observation
    path = tmp_path / "calendar.json"
    path.write_text(json.dumps({"schema": "omni.calendar.v1", "required_series": ["CPI", "NFP", "FOMC"],
                               "verified_at": "2026-10-10T00:00:00Z",
                               "coverage_start": "2026-10-01T00:00:00Z",
                               "coverage_end": "2026-11-01T00:00:00Z",
                               "events": [{"name": "CPI", "impact": "HIGH", "source": "https://www.bls.gov",
                                           "time_utc": "2026-10-14T12:30:00Z",
                                           "pre_blackout_m": 30, "post_blackout_m": 30}]}))
    for text, expected in [("2026-10-14T12:10:00+00:00", True),
                           ("2026-10-14T12:50:00+00:00", True),
                           ("2026-10-14T13:00:00+00:00", False)]:
        assert calendar_observation(datetime.fromisoformat(text).timestamp(), path)["blackout_active"] is expected
