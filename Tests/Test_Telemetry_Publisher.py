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


def git_responder(calls, staged="", generation=None):
    def run(command):
        calls.append(command)
        if command[1:3] == ["branch", "--show-current"]:
            return 0, "main", ""
        if command[1:3] == ["remote", "get-url"]:
            return 0, publisher.CANONICAL_REMOTE + ".git", ""
        if command[1:4] == ["diff", "--cached", "--name-only"]:
            return 0, staged, ""
        if command[1] == "rev-parse":
            return 0, "remote-base" if command[2] == "origin/main" else "verified-head", ""
        if command[1] == "rev-list":
            return 0, "verified-head remote-base", ""
        if command[1] == "diff-tree":
            return 0, publisher.SNAPSHOT_FILE, ""
        if command[1] == "show":
            return 0, json.dumps(generation), ""
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
    monkeypatch.setattr(publisher, "run_cmd", git_responder(calls, generation=generation[0]))
    assert publisher.sync_git_cycle(generation[0]) is True
    commit = next(command for command in calls if command[1] == "commit")
    assert "--only" in commit and commit[-2:] == ["--", publisher.SNAPSHOT_FILE]
    assert ["git", "push", "--atomic", "origin", f"verified-head:{publisher.BRANCH_NAME}", f"verified-head:{publisher.ARENA_BRANCH}"] in calls
    assert not any(command[1] in ("add", "stash", "rebase") for command in calls)


@pytest.mark.parametrize("failure", ["status", "operator_commit", "merge_commit", "wrong_generation", "history"])
def test_publication_refuses_unproven_revision(generation, monkeypatch, failure):
    calls = []
    base = git_responder(calls, generation=generation[0])
    def run(command):
        result = base(command)
        if failure == "status" and command[1] == "status":
            return 1, "", "index unavailable"
        if failure == "operator_commit" and command[1] == "diff-tree":
            return 0, publisher.SNAPSHOT_FILE + "\nTerminal/Omni_Trader.py", ""
        if failure == "merge_commit" and command[1] == "rev-list":
            return 0, "verified-head parent-one parent-two", ""
        if failure == "wrong_generation" and command[1] == "show":
            return 0, json.dumps(generation[0] | {"generation_id": "other-writer"}), ""
        if failure == "history" and command[1] == "rev-list":
            return 1, "", "objects unavailable"
        return result
    monkeypatch.setattr(publisher, "run_cmd", run)
    assert publisher.sync_git_cycle(generation[0]) is False
    assert not any(command[1] == "push" for command in calls)


def test_concurrent_head_change_and_dual_push_failure_use_verified_sha(generation, monkeypatch):
    calls = []
    base = git_responder(calls, generation=generation[0])
    head_reads = 0
    def run(command):
        nonlocal head_reads
        result = base(command)
        if command[1:] == ["rev-parse", "HEAD"]:
            head_reads += 1
            # An operator commits after the daemon captures its publication SHA.
            if head_reads > 2:
                return 0, "unrelated-operator-head", ""
        if command[1:3] == ["push", "--atomic"]:
            return 1, "", "arena branch diverged"
        return result
    monkeypatch.setattr(publisher, "run_cmd", run)
    assert publisher.sync_git_cycle(generation[0]) is True
    pushes = [command for command in calls if command[1] == "push"]
    assert pushes[-1] == ["git", "push", "origin", "verified-head:main"]
    assert all(not ref.startswith("HEAD:") for command in pushes for ref in command)


@pytest.mark.parametrize("during_fallback", [False, True])
def test_replaced_generation_or_elapsed_fallback_never_pushes(generation, monkeypatch, during_fallback):
    value, path = generation
    calls = []
    base = git_responder(calls, generation=value)
    def run(command):
        result = base(command)
        if not during_fallback and command[1] == "show":
            path.write_text(json.dumps(value | {"generation_id": "new-cycle"}))
        if during_fallback and command[1:3] == ["push", "--atomic"]:
            monkeypatch.setattr(publisher.time, "time", lambda: value["as_of_epoch"] + 181)
            return 1, "", "push timeout"
        return result
    monkeypatch.setattr(publisher, "run_cmd", run)
    assert publisher.sync_git_cycle(value) is False
    pushes = [command for command in calls if command[1] == "push"]
    assert len(pushes) == int(during_fallback)


def test_os_singleton_is_exclusive_and_released_on_close(tmp_path, monkeypatch):
    import subprocess
    import sys
    path = tmp_path / "publisher.pid"
    monkeypatch.setattr(publisher, "PID_FILE", path)
    monkeypatch.setattr(publisher, "_singleton_handle", None)
    script = """import os, sys
h = open(sys.argv[1], 'a+b')
h.seek(0)
try:
    if os.name == 'nt':
        import msvcrt
        msvcrt.locking(h.fileno(), msvcrt.LK_NBLCK, 1)
    else:
        import fcntl
        fcntl.flock(h.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
except OSError:
    sys.exit(23)
"""
    publisher.enforce_single_instance()
    handle = publisher._singleton_handle
    try:
        result = subprocess.run([sys.executable, "-c", script, str(path.with_suffix(".lock"))], timeout=10)
        assert result.returncode == 23
    finally:
        handle.close()
        monkeypatch.setattr(publisher, "_singleton_handle", None)
    result = subprocess.run([sys.executable, "-c", script, str(path.with_suffix(".lock"))], timeout=10)
    assert result.returncode == 0


def test_daemon_continues_after_generation_and_gc_exceptions(monkeypatch):
    from Terminal import MT5_Execution_Bridge
    from Terminal.Data_Factory import generate_telemetry_snapshot
    monkeypatch.setattr(publisher, "enforce_single_instance", lambda: None)
    monkeypatch.setattr(MT5_Execution_Bridge, "MT5ExecutionBridge", lambda account: object())
    attempts, cleanups, sleeps = [], [], []
    def generate(**kwargs):
        attempts.append(True)
        raise RuntimeError("generation unavailable")
    def cleanup():
        cleanups.append(True)
        if len(cleanups) == 1:
            raise RuntimeError("GC unavailable")
    def sleep(delay):
        sleeps.append(delay)
        if len(sleeps) == 2:
            raise KeyboardInterrupt
    monkeypatch.setattr(generate_telemetry_snapshot, "generate_full_snapshot", generate)
    monkeypatch.setattr(publisher.gc, "collect", cleanup)
    monkeypatch.setattr(publisher.time, "sleep", sleep)
    monkeypatch.setattr(publisher, "sync_git_cycle", lambda *args, **kwargs: pytest.fail("failed generation must not publish"))
    with pytest.raises(KeyboardInterrupt):
        publisher.main()
    assert len(attempts) == len(cleanups) == 2


def test_singleton_lock_failure_never_kills_a_recorded_pid(tmp_path, monkeypatch):
    import os
    path = tmp_path / "publisher.pid"
    path.write_text("1234")
    monkeypatch.setattr(publisher, "PID_FILE", path)
    monkeypatch.setattr(publisher, "_singleton_handle", None)
    if os.name == "nt":
        import msvcrt
        monkeypatch.setattr(msvcrt, "locking", lambda *args: (_ for _ in ()).throw(OSError("locked")))
    else:
        import fcntl
        monkeypatch.setattr(fcntl, "flock", lambda *args: (_ for _ in ()).throw(OSError("locked")))
    monkeypatch.setattr(publisher.subprocess, "run", lambda *args, **kwargs: pytest.fail("must not invoke taskkill"))
    with pytest.raises(SystemExit, match="lock unavailable"):
        publisher.enforce_single_instance()
    assert path.read_text() == "1234"
