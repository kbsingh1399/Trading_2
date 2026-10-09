"""Publication never borrows evidence or commits another operator's changes."""
import json

import pytest

from Terminal.Data_Factory import autonomous_telemetry_git_daemon as publisher


@pytest.fixture
def generation(tmp_path, monkeypatch):
    now = 1_791_600_000.0
    value = {"generation_id": "cycle-one", "snapshot_status": "LIVE_OBSERVATION",
             "as_of_epoch": now, "as_of_utc": "2026-10-10 00:00:00 UTC",
             "active_positions": [], "pending_orders": [], "account": {"currency": "USD", "login": 5064568},
             "capacity": {"max_concurrent": 4, "inventory_status": "OBSERVED",
                          "filled": 0, "pending": 0, "used_joint_fill": 0}, "assets_matrix_24": {}}
    row = {"htf_history": {}}
    for key, period in (("1h", 3600), ("4h", 14400)):
        row[f"htf_{key}_ohlcv"] = [{"ts": now-period, "close_ts": now}]
        row["htf_history"][key] = {"source": "MT5_BROKER_COMPLETED_BARS", "completed_count": 1}
    value["assets_matrix_24"]["BTC"] = row
    path = tmp_path / publisher.SNAPSHOT_FILE
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps(value))
    monkeypatch.setattr(publisher, "ROOT", tmp_path)
    monkeypatch.setattr(publisher.time, "time", lambda: now)
    monkeypatch.setattr("Terminal.Telemetry_Provenance.validate_observed_snapshot", lambda document: True)
    return value, path


def test_only_exact_successful_generation_can_be_published(generation):
    value, path = generation
    assert publisher.load_successful_generation(value) == value
    assert publisher.load_successful_generation(None) is None
    assert publisher.load_successful_generation(value | {"generation_id": "different"}) is None
    changed = value | {"as_of_epoch": value["as_of_epoch"] - 181}
    path.write_text(json.dumps(changed))
    assert publisher.load_successful_generation(changed) is None


def test_future_bar_cannot_be_published(generation):
    value, path = generation
    bar = value["assets_matrix_24"]["BTC"]["htf_1h_ohlcv"][0]
    bar.update(ts=value["as_of_epoch"], close_ts=value["as_of_epoch"]+3600)
    path.write_text(json.dumps(value))
    assert publisher.load_successful_generation(value) is None


def test_wrong_account_never_published(generation):
    value, path = generation
    value["account"]["login"] = 123456
    path.write_text(json.dumps(value))
    assert publisher.load_successful_generation(value) is None


@pytest.mark.parametrize("failures", [2, 5])
def test_atomic_snapshot_owns_unique_temp_and_preserves_old_on_failure(tmp_path, monkeypatch, failures):
    from pathlib import Path
    from Terminal.Data_Factory.generate_telemetry_snapshot import atomic_snapshot_write
    path = tmp_path / "snapshot.json"
    path.write_text('{"old": true}')
    # Another generation's temporary file must not be overwritten or removed.
    unrelated = tmp_path / "snapshot.tmp"
    unrelated.write_text("another writer")
    original = Path.replace
    attempts = []
    def replace(source, target):
        attempts.append(source)
        if len(attempts) <= failures:
            raise PermissionError("Windows reader holds destination")
        return original(source, target)
    monkeypatch.setattr(Path, "replace", replace)
    monkeypatch.setattr("Terminal.Data_Factory.generate_telemetry_snapshot.time.sleep", lambda delay: None)
    if failures == 5:
        with pytest.raises(PermissionError):
            atomic_snapshot_write(path, {"new": True})
        assert json.loads(path.read_text()) == {"old": True}
    else:
        atomic_snapshot_write(path, {"new": True})
        assert json.loads(path.read_text()) == {"new": True}
    assert unrelated.read_text() == "another writer"
    assert list(tmp_path.glob(".snapshot.json.*.tmp")) == []


def git_responder(calls, staged=""):
    def run(command):
        calls.append(command)
        if command[1:3] == ["branch", "--show-current"]:
            return 0, "main", ""
        if command[1:3] == ["remote", "get-url"]:
            return 0, publisher.CANONICAL_REMOTE + ".git", ""
        if command[1:4] == ["diff", "--cached", "--name-only"]:
            return 0, staged, ""
        if command[1] == "rev-parse":
            return 0, "same-head", ""
        if command[1] == "status":
            return 0, " M " + publisher.SNAPSHOT_FILE, ""
        return 0, "", ""
    return run


def test_foreign_staged_work_defers_publication(generation, monkeypatch):
    calls = []
    monkeypatch.setattr(publisher, "run_cmd", git_responder(calls, "Terminal/Omni_Trader.py"))
    assert publisher.sync_git_cycle(generation[0]) is False
    assert not any(command[1] in ("commit", "push") for command in calls)


def test_successful_cycle_commits_only_snapshot_and_pushes_main(generation, monkeypatch):
    calls = []
    monkeypatch.setattr(publisher, "run_cmd", git_responder(calls))
    assert publisher.sync_git_cycle(generation[0]) is True
    commit = next(command for command in calls if command[1] == "commit")
    assert "--only" in commit and commit[-2:] == ["--", publisher.SNAPSHOT_FILE]
    assert ["git", "push", "origin", "HEAD:main"] in calls
    assert not any(command[1] in ("add", "stash", "rebase") for command in calls)


def test_singleton_lock_failure_never_kills_a_recorded_pid(tmp_path, monkeypatch):
    import msvcrt
    path = tmp_path / "publisher.pid"
    path.write_text("1234")
    monkeypatch.setattr(publisher, "PID_FILE", path)
    monkeypatch.setattr(publisher, "_singleton_handle", None)
    monkeypatch.setattr(msvcrt, "locking", lambda *args: (_ for _ in ()).throw(OSError("locked")))
    monkeypatch.setattr(publisher.subprocess, "run", lambda *args, **kwargs: pytest.fail("must not invoke taskkill"))
    with pytest.raises(SystemExit, match="lock unavailable"):
        publisher.enforce_single_instance()
    assert path.read_text() == "1234"
