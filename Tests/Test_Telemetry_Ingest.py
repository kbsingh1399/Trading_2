"""Regression tests for Terminal/telemetry_ingest.py -- the staleness gate.

Two classes of test live here:

* Unit tests on injected clocks and synthetic payloads (deterministic, no repo
  file, no wall clock).
* Characterisation tests that pin the MEASURED behaviour of the real,
  git-propagated snapshot.  These exist because the operator-mandated 90 s
  budget is tighter than the file's observed propagation latency, and that
  fact must be visible in the suite rather than rediscovered in production.
"""
import json
import math
import os
import subprocess
import sys
import time

import pytest

from Terminal.telemetry_ingest import (
    CLOCK_SKEW_TOLERANCE_S,
    DEFAULT_MAX_AGE_S,
    GENERATION_CADENCE_S,
    StaleDataError,
    TELEMETRY_BRANCH,
    get_fresh_snapshot,
    make_git_refresh,
    measure_snapshot_age,
    resolve_snapshot_path,
)

NOW = 1_791_715_800.0
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIVE = os.path.join(ROOT, "docs", "telemetry", "live_snapshot_latest.json")


def _snap(as_of=NOW, gen="gen-1"):
    return {"as_of_epoch": as_of, "generation_id": gen, "assets_matrix_24": {}}


@pytest.fixture
def snapfile(tmp_path):
    def _write(payload):
        p = tmp_path / "live_snapshot_latest.json"
        p.write_text(json.dumps(payload), encoding="utf-8")
        return str(p)

    return _write


# ----------------------------------------------------------------- fresh path

def test_fresh_snapshot_is_returned_and_age_is_within_budget(snapfile):
    p = snapfile(_snap(as_of=NOW - 10.0))
    out = get_fresh_snapshot(p, max_age_s=DEFAULT_MAX_AGE_S, now=NOW)
    assert out["generation_id"] == "gen-1"
    assert measure_snapshot_age(out, now=NOW).age_s == pytest.approx(10.0)


def test_age_exactly_at_the_budget_is_admitted(snapfile):
    p = snapfile(_snap(as_of=NOW - DEFAULT_MAX_AGE_S))
    assert get_fresh_snapshot(p, now=NOW)["generation_id"] == "gen-1"


def test_age_one_microsecond_over_the_budget_is_refused(snapfile):
    p = snapfile(_snap(as_of=NOW - DEFAULT_MAX_AGE_S - 1e-6))
    with pytest.raises(StaleDataError) as ei:
        get_fresh_snapshot(p, now=NOW)
    assert ei.value.reason == "snapshot_stale"
    assert ei.value.diagnostics["age_s"] > DEFAULT_MAX_AGE_S


# ---------------------------------------------------------------- failure modes

def test_missing_file_raises_stale_data_error(tmp_path):
    with pytest.raises(StaleDataError) as ei:
        get_fresh_snapshot(str(tmp_path / "absent.json"), now=NOW)
    assert ei.value.reason == "snapshot_missing"


def test_unparseable_file_raises_stale_data_error(tmp_path):
    p = tmp_path / "live_snapshot_latest.json"
    p.write_text("{not json", encoding="utf-8")
    with pytest.raises(StaleDataError) as ei:
        get_fresh_snapshot(str(p), now=NOW)
    assert ei.value.reason == "snapshot_unparseable"


@pytest.mark.parametrize("payload", [
    {"generation_id": "g"},                                  # no as_of_epoch
    {"as_of_epoch": None, "generation_id": "g"},             # null stamp
    {"as_of_epoch": "2026-10-11", "generation_id": "g"},     # non-numeric
    {"as_of_epoch": float("nan"), "generation_id": "g"},     # NaN
    {"as_of_epoch": float("inf"), "generation_id": "g"},     # infinite
    [],                                                      # wrong shape entirely
])
def test_unstamped_or_unusable_stamp_fails_closed(snapfile, payload):
    p = snapfile(payload)
    with pytest.raises(StaleDataError) as ei:
        get_fresh_snapshot(p, now=NOW)
    assert ei.value.reason == "snapshot_unstamped"


def test_snapshot_stamped_in_the_host_future_is_unmeasurable_not_fresh(snapfile):
    p = snapfile(_snap(as_of=NOW + 5_000.0))
    with pytest.raises(StaleDataError) as ei:
        get_fresh_snapshot(p, now=NOW)
    assert ei.value.reason == "snapshot_future_stamped_unmeasurable_age"


def test_bounded_clock_skew_is_tolerated_using_the_broker_clock_allowance(snapfile):
    p = snapfile(_snap(as_of=NOW + CLOCK_SKEW_TOLERANCE_S))
    assert get_fresh_snapshot(p, now=NOW)["generation_id"] == "gen-1"


def test_negative_max_age_is_rejected_rather_than_silently_passing(snapfile):
    p = snapfile(_snap())
    with pytest.raises(StaleDataError) as ei:
        get_fresh_snapshot(p, max_age_s=-1.0, now=NOW)
    assert ei.value.reason == "invalid_max_age_s"


def test_zero_budget_admits_only_a_coincident_stamp(snapfile):
    p = snapfile(_snap(as_of=NOW))
    assert get_fresh_snapshot(p, max_age_s=0.0, now=NOW)["generation_id"] == "gen-1"


# --------------------------------------------------------------- refresh path

def test_refresh_that_advances_the_generation_rescues_a_stale_file(snapfile):
    p = snapfile(_snap(as_of=NOW - 600.0, gen="old"))
    calls = {"n": 0}

    def _refresh():
        calls["n"] += 1
        with open(p, "w", encoding="utf-8") as fh:
            json.dump(_snap(as_of=NOW - 5.0, gen="new"), fh)

    out = get_fresh_snapshot(p, now=NOW, refresh=_refresh)
    assert out["generation_id"] == "new"
    assert calls["n"] >= 1


def test_refresh_that_does_not_advance_the_generation_still_refuses(snapfile):
    """A retry that re-reads the SAME generation must not be reported as fresh."""
    p = snapfile(_snap(as_of=NOW - 600.0, gen="same"))
    calls = {"n": 0}

    def _refresh():
        calls["n"] += 1
        # The generator is stuck: same stamp, same generation id, forever.
        with open(p, "w", encoding="utf-8") as fh:
            json.dump(_snap(as_of=NOW - 600.0, gen="same"), fh)

    with pytest.raises(StaleDataError) as ei:
        get_fresh_snapshot(
            p, now=NOW, refresh=_refresh, refresh_wait_s=1.0, retry_deadline_s=3.0,
            sleep=lambda _s: None,
        )
    assert ei.value.reason == "snapshot_stale"
    assert ei.value.diagnostics["generation_changed"] is False
    assert calls["n"] >= 2


def test_immediate_retry_without_a_cadence_wait_is_refused_not_faked(snapfile):
    """The observed defect: retrying faster than one cadence cannot help.

    With ``retry_deadline_s=0`` the gate reads once and refuses, rather than
    burning a second pull that provably returns the same generation.
    """
    p = snapfile(_snap(as_of=NOW - 600.0, gen="g"))
    calls = {"n": 0}

    def _refresh():
        calls["n"] += 1

    with pytest.raises(StaleDataError) as ei:
        get_fresh_snapshot(p, now=NOW, refresh=_refresh)
    assert ei.value.reason == "snapshot_stale"
    assert calls["n"] == 1, "no retry should be attempted with retry_deadline_s=0"


def test_cadence_aware_retry_waits_then_admits_the_next_generation(snapfile):
    """Cadence-aware retry, scripted with the ages OBSERVED against the live repo.

    The first pull returned a generation 107.98 s old (over the 90 s budget);
    the retry after one 60 s cadence returned one 63.4 s old (inside budget).
    This encodes that sequence so the retry path is covered by real numbers
    rather than a synthetic toy, and asserts the wait is exactly one cadence.

    Uses an ADVANCING clock: on a frozen clock every retry re-measures the same
    age, so no wait could ever rescue it and the test would be vacuous.
    """
    p = snapfile(_snap(as_of=NOW - 600.0, gen="gen-0"))
    clock = {"t": NOW}
    slept = []
    # Age, at pull time, of the generation each pull yields.
    script = iter([107.98, 63.4])

    def _sleep(s):
        slept.append(s)
        clock["t"] += s

    def _refresh():
        age = next(script)
        with open(p, "w", encoding="utf-8") as fh:
            json.dump(_snap(as_of=clock["t"] - age, gen=f"gen-age-{age}"), fh)

    out = get_fresh_snapshot(
        p, now=lambda: clock["t"], refresh=_refresh,
        refresh_wait_s=GENERATION_CADENCE_S, retry_deadline_s=2 * GENERATION_CADENCE_S,
        sleep=_sleep,
    )
    assert out["generation_id"] == "gen-age-63.4", "second generation should be admitted"
    assert slept == [GENERATION_CADENCE_S], "retry must wait exactly one cadence"


def test_refresh_that_raises_never_masquerades_as_a_fresh_read(snapfile):
    p = snapfile(_snap(as_of=NOW - 600.0))

    def _refresh():
        raise RuntimeError("git pull failed")

    with pytest.raises(StaleDataError) as ei:
        get_fresh_snapshot(p, now=NOW, refresh=_refresh)
    assert ei.value.reason == "refresh_failed"
    assert "git pull failed" in ei.value.diagnostics["error"]


def test_retry_gives_up_at_the_deadline(snapfile):
    p = snapfile(_snap(as_of=NOW - 600.0))
    slept = []

    def _refresh():
        pass  # generator never advances

    with pytest.raises(StaleDataError) as ei:
        get_fresh_snapshot(
            p, now=NOW, refresh=_refresh, refresh_wait_s=60.0, retry_deadline_s=120.0,
            sleep=slept.append,
        )
    assert ei.value.reason == "snapshot_stale"
    assert sum(slept) <= 120.0


def test_wait_longer_than_the_budget_is_not_attempted(snapfile):
    """Waiting past the budget cannot produce a fresh read; refuse immediately."""
    p = snapfile(_snap(as_of=NOW - 600.0))
    slept = []
    with pytest.raises(StaleDataError):
        get_fresh_snapshot(
            p, now=NOW, max_age_s=90.0, refresh=lambda: None,
            refresh_wait_s=200.0, retry_deadline_s=1000.0, sleep=slept.append,
        )
    assert slept == []


@pytest.mark.parametrize("kwargs,reason", [
    ({"refresh_wait_s": -1.0}, "invalid_refresh_wait_s"),
    ({"retry_deadline_s": -1.0}, "invalid_retry_deadline_s"),
    ({"refresh_wait_s": float("nan")}, "invalid_refresh_wait_s"),
    ({"sleep": "not callable"}, "sleep_not_callable"),
])
def test_invalid_retry_parameters_are_rejected(snapfile, kwargs, reason):
    p = snapfile(_snap())
    with pytest.raises(StaleDataError) as ei:
        get_fresh_snapshot(p, now=NOW, **kwargs)
    assert ei.value.reason == reason


def test_non_callable_refresh_is_rejected(snapfile):
    p = snapfile(_snap())
    with pytest.raises(StaleDataError) as ei:
        get_fresh_snapshot(p, now=NOW, refresh="git pull")
    assert ei.value.reason == "refresh_not_callable"


# ------------------------------------------- the assert-vs-raise defect guard

def test_gate_still_refuses_under_python_dash_O(tmp_path):
    """``assert`` is deleted by -O; this gate must not be built on one.

    Runs the refusal in a subprocess with PYTHONOPTIMIZE so an accidental
    regression to ``assert`` fails here instead of silently opening the gate
    in a production launch that happens to set -O.
    """
    stale = tmp_path / "live_snapshot_latest.json"
    stale.write_text(json.dumps(_snap(as_of=NOW - 5_000.0)), encoding="utf-8")
    code = (
        "import sys;from Terminal.telemetry_ingest import get_fresh_snapshot,StaleDataError\n"
        f"p=r'{stale}'\n"
        "try:\n"
        "    get_fresh_snapshot(p, now=%r)\n"
        "    print('NO_RAISE')\n" % (NOW,)
        + "except StaleDataError as e:\n"
        "    print('RAISED:'+e.reason)\n"
    )
    env = dict(os.environ, PYTHONOPTIMIZE="2")
    proc = subprocess.run(
        [sys.executable, "-O", "-c", code], cwd=ROOT, env=env,
        capture_output=True, text=True, timeout=120,
    )
    assert "RAISED:snapshot_stale" in proc.stdout, proc.stdout + proc.stderr


# ---------------------------------------------------- pure measurement helper

def test_measure_snapshot_age_is_pure_and_never_raises():
    m = measure_snapshot_age({"as_of_epoch": NOW - 30.0}, now=NOW)
    assert m.age_s == pytest.approx(30.0)
    assert measure_snapshot_age({}, now=NOW).age_s is None
    assert measure_snapshot_age(None, now=NOW).as_of_epoch is None


def test_resolve_snapshot_path_defaults_into_the_repo_telemetry_file():
    assert resolve_snapshot_path().endswith(
        os.path.join("docs", "telemetry", "live_snapshot_latest.json")
    )


# ------------------------------------------------------------- git refresh factory

def test_make_git_refresh_pulls_only_the_snapshot_path(tmp_path):
    """The refresh must advance the snapshot without disturbing the working tree."""
    subprocess.run(["git", "init", "-q", str(tmp_path / "remote")], check=True)
    subprocess.run(["git", "init", "-q", str(tmp_path / "local")], check=True)
    remote = tmp_path / "remote"
    local = tmp_path / "local"

    def _git(cwd, *args):
        subprocess.run(["git", *args], cwd=str(cwd), check=True,
                       capture_output=True, text=True)

    for repo in (remote, local):
        _git(repo, "config", "user.email", "t@example.com")
        _git(repo, "config", "user.name", "t")
        _git(repo, "config", "commit.gpgsign", "false")

    tele = remote / "docs" / "telemetry"
    tele.mkdir(parents=True, exist_ok=True)
    (tele / "live_snapshot_latest.json").write_text(json.dumps(_snap(gen="g-remote-1")))
    _git(remote, "add", "-A")
    _git(remote, "commit", "-q", "-m", "gen 1")
    _git(remote, "branch", "-M", "main")

    _git(local, "remote", "add", "origin", str(remote))
    _git(local, "fetch", "-q", "origin")
    _git(local, "checkout", "-q", "-b", "main", "origin/main")

    # A local-only file must survive the refresh untouched.
    (local / "keep.txt").write_text("local work")

    refresh = make_git_refresh(branch="main", repo_root=str(local))
    refresh()
    assert json.loads(
        (local / "docs" / "telemetry" / "live_snapshot_latest.json").read_text()
    )["generation_id"] == "g-remote-1"
    assert (local / "keep.txt").read_text() == "local work"

    # Publish a newer generation upstream and confirm the refresh picks it up.
    (tele / "live_snapshot_latest.json").write_text(json.dumps(_snap(gen="g-remote-2")))
    _git(remote, "add", "-A")
    _git(remote, "commit", "-q", "-m", "gen 2")
    refresh()
    assert json.loads(
        (local / "docs" / "telemetry" / "live_snapshot_latest.json").read_text()
    )["generation_id"] == "g-remote-2"


def test_make_git_refresh_raises_on_a_bad_remote(tmp_path):
    """A broken pull must surface, so the gate reports refresh_failed not fresh."""
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    refresh = make_git_refresh(branch="main", repo_root=str(tmp_path))
    with pytest.raises(subprocess.CalledProcessError):
        refresh()
    with pytest.raises(StaleDataError) as ei:
        get_fresh_snapshot(tmp_path / "nope.json", refresh=refresh)
    assert ei.value.reason == "refresh_failed"


def test_default_refresh_branch_is_the_publishing_branch_not_the_working_branch():
    """Pin the trap: reading a session branch looks current and always is not.

    Observed 2026-10-11 ~11:10 UTC -- ``origin/main`` held a 41.9 s old
    snapshot while ``origin/arena/537c1eb8-trading-2`` held one 518.9 s old and
    refused to advance across two 60 s retries.  The generator publishes to
    ``main``; a working branch only receives telemetry as a side effect of a
    code push.  Asserting the default keeps that from being swapped back.
    """
    import inspect

    assert TELEMETRY_BRANCH == "main"
    sig = inspect.signature(make_git_refresh)
    assert sig.parameters["branch"].default == "main"


# ---------------------------------- integration: the wired broker-state fallback

pytest.importorskip("pandas", reason="arena_bridge imports pandas at module scope")
pytest.importorskip("polars", reason="arena_bridge imports polars at module scope")


def _broker_state_with_snapshot(monkeypatch, tmp_path, payload):
    """Run the REAL get_live_broker_state() against a snapshot we control.

    Forces the fallback branch so the test exercises the gate's verdict on
    the snapshot rather than a live MT5 terminal.
    """
    import sys
    import types
    import Terminal.dispatch_comprehensive_wake_up_prompt as disp

    mock_mt5 = types.ModuleType("MetaTrader5")
    def _fail_init():
        raise RuntimeError("MT5 unavailable")
    mock_mt5.initialize = _fail_init
    monkeypatch.setitem(sys.modules, "MetaTrader5", mock_mt5)

    tele = tmp_path / "docs" / "telemetry"
    tele.mkdir(parents=True, exist_ok=True)
    (tele / "live_snapshot_latest.json").write_text(json.dumps(payload), encoding="utf-8")
    monkeypatch.setattr(disp, "ROOT", tmp_path)
    # tmp_path is not a git repo: neutralise the pull so the test exercises the
    # gate's verdict on the file we control, not git plumbing.
    monkeypatch.setattr(disp, "make_git_refresh", lambda **_kw: (lambda: None))
    return disp.get_live_broker_state()


def test_broker_state_fallback_ignores_a_stale_capital_snapshot(monkeypatch, tmp_path):
    """A stale file must NOT overwrite equity/balance -- it misstates the G-1 floor."""
    stale = _snap(as_of=time.time() - 5_000.0)
    stale["account"] = {"equity_usd": 9_999.99, "balance_usd": 9_999.99, "margin_usd": 7.0}
    state = _broker_state_with_snapshot(monkeypatch, tmp_path, stale)
    assert state["equity"] == 4896.55, "stale equity was trusted"
    assert state["balance"] == 4896.55, "stale balance was trusted"
    assert state["margin"] == 0.0, "stale margin was trusted"


def test_broker_state_fallback_uses_a_fresh_capital_snapshot(monkeypatch, tmp_path):
    fresh = _snap(as_of=time.time())
    fresh["account"] = {"equity_usd": 5_001.25, "balance_usd": 4_980.00,
                        "margin_used_usd": 3.5}
    state = _broker_state_with_snapshot(monkeypatch, tmp_path, fresh)
    assert state["equity"] == 5_001.25
    assert state["balance"] == 4_980.00
    assert state["margin"] == 3.5


def test_broker_state_reads_the_margin_key_the_snapshot_actually_publishes(monkeypatch, tmp_path):
    """The account block publishes `margin_used_usd`, not `margin_usd`.

    Reading the absent key returned 0.0, which understates margin and therefore
    OVERSTATES the cushion above the hard floor -- the wrong direction for a
    capital gate. Both spellings must resolve.
    """
    for key in ("margin_used_usd", "margin_usd"):
        fresh = _snap(as_of=time.time())
        fresh["account"] = {"equity_usd": 4_900.0, "balance_usd": 4_900.0, key: 42.5}
        state = _broker_state_with_snapshot(monkeypatch, tmp_path, fresh)
        assert state["margin"] == 42.5, f"{key} was not read"


# ------------------------------------------- characterisation of the LIVE file

def test_live_snapshot_carries_the_stamp_and_generation_the_gate_requires():
    if not os.path.exists(LIVE):
        pytest.skip("live telemetry not present in this checkout")
    with open(LIVE, encoding="utf-8") as fh:
        payload = json.load(fh)
    m = measure_snapshot_age(payload, now=time.time())
    assert m.as_of_epoch is not None, "as_of_epoch absent -- gate cannot measure age"
    assert m.generation_id, "generation_id absent -- refresh cannot prove movement"
    assert math.isfinite(m.age_s)


def test_documented_operator_budget_is_tighter_than_git_propagation_latency():
    """Pin the finding: 90 s is below the file's real, git-propagated age.

    The generator cadence is ~60 s (mean 60.0 / max 63.7 over 14 intervals),
    but this working copy only advances when it is pulled, so the observed age
    is cadence + propagation + time-since-pull and measured 146-168 s.  The
    consequence is NOT that the budget is wrong -- refusing stale data is the
    correct posture -- but that a bare read can never satisfy it.  This test
    asserts the mechanism, not a fixed number: the live file's age is whatever
    it is, and the gate must report it faithfully and refuse when it exceeds
    the budget.
    """
    if not os.path.exists(LIVE):
        pytest.skip("live telemetry not present in this checkout")
    with open(LIVE, encoding="utf-8") as fh:
        payload = json.load(fh)
    age = measure_snapshot_age(payload, now=time.time()).age_s
    if age <= DEFAULT_MAX_AGE_S:
        assert get_fresh_snapshot(LIVE, max_age_s=DEFAULT_MAX_AGE_S)["generation_id"]
        return
    with pytest.raises(StaleDataError) as ei:
        get_fresh_snapshot(LIVE, max_age_s=DEFAULT_MAX_AGE_S)
    assert ei.value.reason == "snapshot_stale"
    assert ei.value.diagnostics["age_s"] == pytest.approx(age, abs=5.0)
