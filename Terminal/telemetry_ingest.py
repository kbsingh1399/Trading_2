"""Terminal/telemetry_ingest.py -- single point of entry for live telemetry.

Mandate (Arena.AI operator, 2026-10-11): one function, ``get_fresh_snapshot``,
that loads ``docs/telemetry/live_snapshot_latest.json``, measures its age, and
REFUSES to return a payload that is older than the staleness budget. Every
caller downstream of this module therefore sees either a provably fresh
snapshot or an exception -- never a silently stale one.

Design notes that differ from the one-line spec, each one load-bearing:

1. ``raise``, never ``assert``.  An ``assert`` is stripped by ``python -O`` and
   by any ``PYTHONOPTIMIZE`` setting, which would silently delete the risk
   gate in exactly the environment where it matters.  A staleness refusal is a
   control-flow decision, not a debug invariant.

2. A negative age is a failure, not freshness.  ``as_of_epoch`` is stamped by
   the telemetry generator on ``CALIBRATED_BROKER_UTC``; the host wall clock
   is a different clock.  If the host reads a snapshot stamped in its own
   future, the age is unmeasurable, and "unmeasurable" must fail closed
   rather than read as very fresh.  The tolerance is ``BrokerClock``'s own
   ``max_offset_seconds`` so the two modules cannot disagree.

3. The budget is checked against the payload's own stamp, never against file
   mtime.  mtime is rewritten by ``git checkout``/``git reset`` and carries no
   information about when the market data inside the file was sampled.

4. Freshness is only meaningful if the file can actually advance.  The snapshot
   reaches this working copy by git, so its age is
   ``generation cadence + propagation + time since last pull``.  Measured on
   2026-10-11: cadence mean 60.0 s / median 60.2 s / max 63.7 s over 14
   intervals, with an observed end-to-end age of 146-168 s.  A 90 s budget is
   therefore NOT satisfiable by a bare read.  ``refresh`` is the escape hatch:
   pull first, then re-measure, and prove by ``generation_id`` that the payload
   actually moved.
"""
from __future__ import annotations

import json
import math
import os
import time
from dataclasses import dataclass, field
from numbers import Real
from typing import Any, Callable, Dict, Mapping, Optional

# ------------------------------------------------------------------ constants

#: Snapshot path, relative to the repository root.
SNAPSHOT_REL_PATH = os.path.join("docs", "telemetry", "live_snapshot_latest.json")

#: The operator-mandated staleness budget, in seconds.
#:
#: Derivation, not a prior: the generator publishes on a ~60 s cadence
#: (measured mean 60.0 s, max 63.7 s).  90 s leaves ~26 s of headroom over one
#: cadence, which is tight but achievable WHEN the caller refreshes first.
#: Without a refresh the file's git-propagated age exceeds this by a wide
#: margin -- see module note 4.
DEFAULT_MAX_AGE_S = 90.0

#: Clock-skew tolerance for a snapshot stamped in the host's future.
#: Matches ``Terminal/broker_clock.py::BrokerClock.max_offset_seconds``.
CLOCK_SKEW_TOLERANCE_S = 60.0

#: Measured generation cadence of the telemetry daemon, in seconds.
#: 14 consecutive intervals: mean 60.0, median 60.2, min 54.3, max 63.7.
#: A retry that fires faster than this re-reads the SAME generation and is
#: therefore wasted work -- observed directly, not inferred.
GENERATION_CADENCE_S = 60.0

#: Field that carries the sample instant. ``as_of_epoch`` is present at the top
#: level of every current snapshot (verified against generation 288ae67d).
AS_OF_EPOCH_KEY = "as_of_epoch"
GENERATION_ID_KEY = "generation_id"


class StaleDataError(RuntimeError):
    """Raised when the telemetry payload cannot be proven fresh.

    Callers on the live path should convert this into a STAND ASIDE for the
    current cycle.  It is deliberately NOT raised-and-swallowed inside this
    module: a gate that hides its own failure is not a gate.
    """

    def __init__(self, reason: str, diagnostics: Optional[Mapping[str, Any]] = None):
        self.reason = str(reason)
        self.diagnostics: Dict[str, Any] = dict(diagnostics or {})
        super().__init__(f"{self.reason} :: {self.diagnostics}")


@dataclass(frozen=True)
class SnapshotFreshness:
    """What was measured, so a refusal is auditable rather than a bare exception."""

    as_of_epoch: Optional[float]
    generation_id: Optional[str]
    age_s: Optional[float]
    max_age_s: float
    source: str
    refreshed: bool = False
    generation_changed: Optional[bool] = None

    def as_dict(self) -> Dict[str, Any]:
        return {
            "as_of_epoch": self.as_of_epoch,
            "generation_id": self.generation_id,
            "age_s": self.age_s,
            "max_age_s": self.max_age_s,
            "source": self.source,
            "refreshed": self.refreshed,
            "generation_changed": self.generation_changed,
        }


def _fin(x: Any) -> bool:
    if isinstance(x, (bool,)) or not isinstance(x, Real):
        return False
    try:
        return math.isfinite(float(x))
    except (OverflowError, ValueError, TypeError):
        return False


def resolve_snapshot_path(path: Any = None) -> str:
    """Absolute snapshot path, defaulting to the repo-relative canonical file."""
    if path:
        return os.path.abspath(str(path))
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    return os.path.join(root, SNAPSHOT_REL_PATH)


def _resolve_now(now: Any) -> float:
    """Resolve an injected clock.

    ``now`` may be a float (fixed instant) or a zero-arg callable (advancing
    clock).  A callable is required to exercise the cadence-aware retry path,
    where the retry is only meaningful if the clock moves between reads.
    """
    if callable(now):
        val = now()
        return float(val) if _fin(val) else time.time()
    return float(now) if _fin(now) else time.time()


def measure_snapshot_age(payload: Any, *, now: Any = None) -> SnapshotFreshness:
    """Measure a snapshot's age WITHOUT the freshness verdict.

    Pure: no I/O, no clock beyond the injected ``now``.  Returned regardless of
    whether the payload is acceptable, so callers can log the measurement even
    when the payload is rejected.
    """
    as_of: Optional[float] = None
    gen: Optional[str] = None
    age: Optional[float] = None
    if isinstance(payload, Mapping):
        raw = payload.get(AS_OF_EPOCH_KEY)
        if _fin(raw):
            as_of = float(raw)
            age = _resolve_now(now) - as_of
        gid = payload.get(GENERATION_ID_KEY)
        if isinstance(gid, str) and gid.strip():
            gen = gid.strip()
    return SnapshotFreshness(
        as_of_epoch=as_of,
        generation_id=gen,
        age_s=age,
        max_age_s=DEFAULT_MAX_AGE_S,
        source="<payload>",
    )


def get_fresh_snapshot(
    path: Any = None,
    *,
    max_age_s: float = DEFAULT_MAX_AGE_S,
    now: Any = None,
    refresh: Optional[Callable[[], Any]] = None,
    clock_skew_tolerance_s: float = CLOCK_SKEW_TOLERANCE_S,
    refresh_wait_s: float = 0.0,
    retry_deadline_s: float = 0.0,
    sleep: Callable[[float], Any] = time.sleep,
) -> Dict[str, Any]:
    """Return ``live_snapshot_latest.json`` only if it is provably fresh.

    Args:
        path: Snapshot location. Defaults to the canonical repo-relative file.
        max_age_s: Staleness budget. Operator mandate: 90.0.
        now: Injectable clock for deterministic tests: either a fixed epoch
            float, or a zero-arg callable for an ADVANCING clock (required to
            exercise the cadence-aware retry, which is meaningless on a frozen
            clock).
        refresh: Optional zero-arg callable that advances the working copy
            (typically a git pull of the telemetry branch).  When supplied it is
            called once BEFORE the first measurement.
        clock_skew_tolerance_s: How far the payload may be stamped in the
            host's future before the age is treated as unmeasurable.
        refresh_wait_s: Seconds to wait before each RETRY refresh.  Must be at
            least one generation cadence, otherwise the retry re-reads the same
            generation and cannot help.  See ``GENERATION_CADENCE_S``.
        retry_deadline_s: Total wall-clock seconds available for retrying after
            the first stale read.  0 means "read once, then refuse".
        sleep: Injectable sleep for deterministic tests.

    Returns:
        The parsed snapshot ``dict``.

    Raises:
        StaleDataError: payload unreadable, unstamped, future-stamped beyond
            tolerance, or older than ``max_age_s``.  Always carries the
            measurement so the refusal can be audited.
    """
    if not _fin(max_age_s) or float(max_age_s) < 0:
        raise StaleDataError("invalid_max_age_s", {"max_age_s": max_age_s})
    if not _fin(clock_skew_tolerance_s) or float(clock_skew_tolerance_s) < 0:
        raise StaleDataError("invalid_clock_skew_tolerance_s",
                             {"clock_skew_tolerance_s": clock_skew_tolerance_s})
    for name, val in (("refresh_wait_s", refresh_wait_s), ("retry_deadline_s", retry_deadline_s)):
        if not _fin(val) or float(val) < 0:
            raise StaleDataError(f"invalid_{name}", {name: val})
    if not callable(sleep):
        raise StaleDataError("sleep_not_callable", {"sleep": type(sleep).__name__})

    src = resolve_snapshot_path(path)
    budget = float(max_age_s)
    wait = float(refresh_wait_s)
    deadline = float(retry_deadline_s)

    if refresh is not None and not callable(refresh):
        raise StaleDataError("refresh_not_callable", {"refresh": type(refresh).__name__})
    if refresh is not None:
        _run_refresh(refresh, src)

    prior_gen: Optional[str] = None
    elapsed = 0.0

    while True:
        try:
            with open(src, encoding="utf-8") as stream:
                payload = json.load(stream)
        except FileNotFoundError:
            raise StaleDataError("snapshot_missing", {"source": src}) from None
        except json.JSONDecodeError as exc:
            raise StaleDataError(
                "snapshot_unparseable", {"source": src, "error": str(exc)}
            ) from None
        except OSError as exc:
            raise StaleDataError(
                "snapshot_unreadable", {"source": src, "error": str(exc)}
            ) from None

        meas = measure_snapshot_age(payload, now=now)
        meas = SnapshotFreshness(
            as_of_epoch=meas.as_of_epoch,
            generation_id=meas.generation_id,
            age_s=meas.age_s,
            max_age_s=budget,
            source=src,
            refreshed=refresh is not None,
            generation_changed=(
                None if prior_gen is None else (meas.generation_id != prior_gen)
            ),
        )

        if meas.as_of_epoch is None or meas.age_s is None:
            raise StaleDataError("snapshot_unstamped", meas.as_dict())
        if meas.age_s < -float(clock_skew_tolerance_s):
            # Host clock behind the generator: the age is unmeasurable.
            raise StaleDataError("snapshot_future_stamped_unmeasurable_age", meas.as_dict())
        if meas.age_s <= budget:
            return payload if isinstance(payload, dict) else {"payload": payload}

        # Stale. Retry only if a refresh is available, time remains, and waiting
        # one cadence can plausibly land inside the budget.
        can_retry = (
            refresh is not None
            and deadline > 0.0
            and elapsed + wait <= deadline
            and wait < budget  # waiting longer than the budget cannot help
        )
        if not can_retry:
            raise StaleDataError("snapshot_stale", meas.as_dict())

        prior_gen = meas.generation_id
        sleep(wait)
        elapsed += wait
        _run_refresh(refresh, src)


def _run_refresh(refresh: Callable[[], Any], src: str) -> None:
    """Invoke a refresh; a failed pull must never masquerade as fresh data."""
    try:
        refresh()
    except Exception as exc:
        raise StaleDataError(
            "refresh_failed", {"source": src, "error": f"{type(exc).__name__}: {exc}"}
        ) from exc


#: Branch the telemetry daemon actually publishes to.
#:
#: VERIFIED, not assumed.  At 2026-10-11 ~11:10 UTC the newest snapshot on
#: ``origin/main`` was 41.9 s old while ``origin/arena/537c1eb8-trading-2``
#: carried one 518.9 s old and would not advance across two 60 s retries
#: (``generation_changed=False``), because that branch only receives telemetry
#: as a side effect of a code push.  Reading the working branch is therefore a
#: silent staleness trap: the file exists, parses, and is simply always late.
TELEMETRY_BRANCH = "main"


def make_git_refresh(
    branch: str = TELEMETRY_BRANCH,
    remote: str = "origin",
    repo_root: Optional[str] = None,
    rel_path: str = SNAPSHOT_REL_PATH,
) -> Callable[[], Any]:
    """Build a ``refresh`` callable that pulls one telemetry file from git.

    Defaults to ``TELEMETRY_BRANCH`` (``main``) because that is where the
    generator publishes; a session working branch will look current only for as
    long as the last code push happened to carry a recent snapshot.

    Checks out only the snapshot path, so a concurrent working tree is left
    untouched.  Raises on failure -- ``get_fresh_snapshot`` converts that into
    ``StaleDataError('refresh_failed')`` rather than proceeding on stale data.
    """
    import subprocess

    root = os.path.abspath(repo_root) if repo_root else os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
    posix_rel = rel_path.replace(os.sep, "/")

    def _refresh() -> None:
        subprocess.run(
            ["git", "fetch", "-q", remote, branch], cwd=root, check=True,
            capture_output=True, text=True,
        )
        subprocess.run(
            ["git", "checkout", "-q", f"{remote}/{branch}", "--", posix_rel],
            cwd=root, check=True, capture_output=True, text=True,
        )

    return _refresh


def enforce_fresh_snapshot(
    path: Any = None,
    *,
    max_age_s: float = DEFAULT_MAX_AGE_S,
    refresh: Optional[Callable[[], Any]] = None,
    refresh_wait_s: float = GENERATION_CADENCE_S,
    retry_deadline_s: float = 2 * GENERATION_CADENCE_S,
) -> Dict[str, Any]:
    """Process-terminating variant: the operator's "kill the process" reading.

    Identical gate to ``get_fresh_snapshot``; re-raises ``StaleDataError``
    unchanged so the caller's exit status is non-zero.  Provided separately so
    the batch/one-shot entry points can die loudly while the resident trading
    loop can catch the same exception and STAND ASIDE instead of abandoning
    management of any already-resting orders.

    Defaults here are cadence-aware: wait one generation (60 s) and allow two
    generations of retry, which is what actually makes the 90 s budget
    satisfiable against a git-propagated file.
    """
    return get_fresh_snapshot(
        path,
        max_age_s=max_age_s,
        refresh=refresh,
        refresh_wait_s=refresh_wait_s,
        retry_deadline_s=retry_deadline_s,
    )


__all__ = [
    "AS_OF_EPOCH_KEY",
    "CLOCK_SKEW_TOLERANCE_S",
    "DEFAULT_MAX_AGE_S",
    "GENERATION_CADENCE_S",
    "GENERATION_ID_KEY",
    "SNAPSHOT_REL_PATH",
    "TELEMETRY_BRANCH",
    "SnapshotFreshness",
    "StaleDataError",
    "enforce_fresh_snapshot",
    "get_fresh_snapshot",
    "make_git_refresh",
    "measure_snapshot_age",
    "resolve_snapshot_path",
]
