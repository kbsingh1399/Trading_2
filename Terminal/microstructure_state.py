"""microstructure_state.py -- rolling microstructure state across cycles.

Two pieces of state the gates need but the point-in-time snapshot cannot carry:

1. WHALE WALL PERSISTENCE. `decision_gates_v3` A3/B5 require
   `wall["persist_s"] >= 180` and `wall["presence_frac"] >= 0.9`. A single
   telemetry sample can prove neither, so both gates fail closed on every asset
   and Gate G-7 can never pass. This module rolls wall identity forward across
   cycles so those two numbers become real measurements.

2. ROLLING HOURLY SPREAD MEDIAN. `SendLimits.spread_vs_median` is meant to
   scale the allowed spread off the hour's *typical* spread. Feeding it the
   instantaneous tick spread makes the comparison `x > 1.5x`, which is never
   true, so the adaptive ceiling silently degenerates to the flat 20 bps cap.

Everything here is a pure function of (previous state, this cycle's
observations, now). I/O stays with the callers so the logic is testable without
a filesystem or a network.

Fail-closed is the design rule: a missing or malformed field yields the least
permissive answer, never a crash and never an invented measurement.
"""
from __future__ import annotations

import statistics
from typing import Any, Dict, Iterable, List, Optional, Tuple

# A wall that disappears for longer than this and reappears is a NEW
# observation. Crediting the earlier sighting would fabricate continuity --
# the same class of error as clamping a wall's age up to the 180s threshold.
GAP_RESET_S = 30.0

# Gate G-7 thresholds, mirrored here so callers can label status consistently.
G7_PERSIST_S = 180.0
G7_PRESENCE_FRAC = 0.9

# Reserved key holding cycle-timing metadata. Wall records are keyed
# "{ASSET}_{SIDE}_{price}", so this can never collide.
META_KEY = "__meta__"

DEFAULT_CYCLE_INTERVAL_S = 60.0
_MAX_INTERVAL_SAMPLES = 40


# ------------------------------------------------------- cycle interval estimate
def record_cycle_interval(prev_state: Dict[str, Any], new_state: Dict[str, Any],
                          now_ts: float) -> None:
    """Carry forward timing metadata and append this cycle's inter-arrival gap.

    The sampling period is measured rather than assumed, because presence_frac
    is a ratio of observed to EXPECTED samples and a wrong denominator would
    silently inflate or deflate every wall's persistence score.
    """
    meta = dict((prev_state or {}).get(META_KEY) or {})
    intervals: List[float] = [float(x) for x in (meta.get("intervals") or [])
                              if isinstance(x, (int, float))]
    last = meta.get("last_ts")
    if isinstance(last, (int, float)) and now_ts > float(last):
        gap = float(now_ts) - float(last)
        # Ignore absurd gaps (process restarts, clock jumps) rather than letting
        # one bad sample corrupt the median.
        if 0 < gap <= 3600.0:
            intervals.append(gap)
            intervals = intervals[-_MAX_INTERVAL_SAMPLES:]
    meta["intervals"] = intervals
    meta["last_ts"] = float(now_ts)
    new_state[META_KEY] = meta


def estimate_cycle_interval(state: Dict[str, Any],
                            default: float = DEFAULT_CYCLE_INTERVAL_S) -> float:
    """Median observed inter-arrival gap, falling back to `default`."""
    meta = (state or {}).get(META_KEY) or {}
    intervals = [float(x) for x in (meta.get("intervals") or [])
                 if isinstance(x, (int, float)) and float(x) > 0]
    if not intervals:
        return float(default)
    try:
        return float(statistics.median(intervals))
    except statistics.StatisticsError:
        return float(default)


# ------------------------------------------------------------- wall persistence
def expected_samples(run_start: float, now_ts: float, cycle_interval_s: float) -> int:
    """How many samples SHOULD have been collected across an unbroken run."""
    interval = float(cycle_interval_s) if cycle_interval_s and cycle_interval_s > 0 else DEFAULT_CYCLE_INTERVAL_S
    span = max(0.0, float(now_ts) - float(run_start))
    return int(round(span / interval)) + 1


def wall_persistence_record(prev_state: Dict[str, Any], new_state: Dict[str, Any],
                            wall_key: str, now_ts: float,
                            gap_reset_s: float = GAP_RESET_S,
                            cycle_interval_s: float = DEFAULT_CYCLE_INTERVAL_S) -> Dict[str, Any]:
    """Roll one wall's persistence record forward; return gate-ready fields.

    Returns a dict with `persist_s`, `presence_frac`, `samples`,
    `first_seen`, `run_start`, `persistence_status` and `first_seen_utc_epoch`,
    suitable for merging straight into a published wall record.

    Repeated or backward observation timestamps never add samples or time.
    These fields describe sampled recurrence, not continuous order identity.

    `persist_s` is measured from the start of the CURRENT UNBROKEN run. A gap
    longer than `gap_reset_s` restarts the run, so a wall that flickers cannot
    accumulate credit for time it was not on the book.

    `presence_frac` is observed cycles over cycles expected across that run, so
    an intermittent wall cannot reach the 0.9 the gates demand.

    Legacy state files stored a bare float (first_seen); that shape is still
    accepted and migrated rather than discarded.
    """
    now_ts = float(now_ts)
    prev = (prev_state or {}).get(wall_key)

    # The gap threshold must exceed the sampling interval, or EVERY observation
    # looks like a gap: at a 60s cycle a wall present on every single sample
    # still shows a 60s gap, and a flat 30s threshold would restart the run
    # every cycle so persist_s could never accrue.
    #
    # 2.5x (not 1.5x) is deliberate. At 1.5x a single missed sample already
    # breaks the run, so presence_frac could only ever be 1.0 or the run would
    # restart -- the metric would never discriminate. At 2.5x one missed sample
    # extends the run while samples stays below expected, so a wall that
    # flickers in and out of the book accrues persist_s but is denied the
    # >=0.9 presence the gates require. Two consecutive misses break it.
    interval = float(cycle_interval_s) if cycle_interval_s and cycle_interval_s > 0 else DEFAULT_CYCLE_INTERVAL_S
    effective_gap_reset = max(float(gap_reset_s), 2.5 * interval)

    first_seen = run_start = now_ts
    samples = 1

    if isinstance(prev, dict):
        prev_first = prev.get("first_seen", prev.get("run_start", now_ts))
        prev_run = prev.get("run_start", prev_first)
        prev_last = prev.get("last_seen", prev_run)
        try:
            prev_first, prev_run, prev_last = float(prev_first), float(prev_run), float(prev_last)
            prev_samples = int(prev.get("samples", 1) or 1)
        except (TypeError, ValueError):
            prev_first = prev_run = prev_last = now_ts
            prev_samples = 1
        gap = now_ts - prev_last
        if gap <= 0:
            # Cached/backward receipts preserve the measured run without adding evidence.
            now_ts = prev_last
            run_start = prev_run
            first_seen = prev_first
            samples = prev_samples
            interval = float(prev.get("cycle_interval_s", interval))
        elif gap <= effective_gap_reset:
            # A new observation extends the sampled run.
            run_start = prev_run
            first_seen = prev_first
            samples = prev_samples + 1
        else:
            # Broken run: restart. Do NOT carry first_seen forward as run_start.
            run_start = now_ts
            first_seen = now_ts
            samples = 1
    elif isinstance(prev, (int, float)):
        # Legacy float record. Treat it as a sighting at that time with no
        # gap information, so the run starts fresh at now.
        first_seen = float(prev)
        run_start = now_ts
        samples = 1

    persist_s = max(0.0, now_ts - run_start)
    exp = expected_samples(run_start, now_ts, interval)
    presence_frac = (samples / exp) if exp > 0 else 0.0
    presence_frac = max(0.0, min(1.0, presence_frac))

    if persist_s >= G7_PERSIST_S and presence_frac >= G7_PRESENCE_FRAC:
        status = "PERSISTENT_VERIFIED"
    elif persist_s > 0.0:
        status = "INSUFFICIENT_PERSISTENCE"
    else:
        status = "SINGLE_SAMPLE"

    record = {
        "first_seen": first_seen,
        "run_start": run_start,
        "last_seen": now_ts,
        "samples": samples,
        "cycle_interval_s": interval,
    }
    new_state[wall_key] = record

    return {
        "persist_s": round(persist_s, 1),
        "presence_frac": round(presence_frac, 4),
        "samples": samples,
        "expected_samples": exp,
        "first_seen": first_seen,
        "run_start": run_start,
        "persistence_status": status,
        "gate_g7_eligible": status == "PERSISTENT_VERIFIED",
    }


def carry_forward_unseen(prev_state: Dict[str, Any], new_state: Dict[str, Any]) -> None:
    """Keep records for walls NOT seen this cycle, unchanged.

    Without this, a wall absent from one book snapshot is dropped from state
    outright, so its reappearance looks like a brand-new sighting and the gap
    can never be measured -- every intermittent wall would reset to
    persist_s=0 and presence_frac=1.0 and G-7 could neither confirm nor deny
    anything meaningful. `last_seen` must survive the absence for the gap test
    in `wall_persistence_record` to have something to compare against.

    Pruning by age is what eventually removes them; see `prune_wall_state`.
    """
    for key, rec in (prev_state or {}).items():
        if key == META_KEY or key in new_state:
            continue
        new_state[key] = rec


def prune_wall_state(state: Dict[str, Any], now_ts: float,
                     max_age_s: float = 3600.0) -> Dict[str, Any]:
    """Drop wall records not seen within `max_age_s`, so the file stays bounded.

    Preserves META_KEY. Never raises on malformed records -- an unreadable
    entry is simply discarded.
    """
    out: Dict[str, Any] = {}
    for key, rec in (state or {}).items():
        if key == META_KEY:
            out[key] = rec
            continue
        last = None
        if isinstance(rec, dict):
            last = rec.get("last_seen", rec.get("run_start", rec.get("first_seen")))
        elif isinstance(rec, (int, float)):
            last = rec
        try:
            if last is None or (float(now_ts) - float(last)) <= max_age_s:
                out[key] = rec
        except (TypeError, ValueError):
            continue
    return out


# ------------------------------------------------------- rolling spread median
def record_spread_observation(history: Dict[str, Any], symbol: str, ts: float,
                              bps: float, window_s: float = 3600.0) -> Dict[str, Any]:
    """Append a spread print and trim to the rolling window. Returns new history."""
    out = dict(history or {})
    key = str(symbol)
    series = [(float(t), float(b)) for t, b in (out.get(key) or [])
              if isinstance(t, (int, float)) and isinstance(b, (int, float))]
    try:
        ts_f, bps_f = float(ts), float(bps)
    except (TypeError, ValueError):
        out[key] = series
        return out
    if not (bps_f > 0) or ts_f <= 0:
        out[key] = series
        return out
    series.append((ts_f, bps_f))
    cutoff = ts_f - float(window_s)
    series = [(t, b) for t, b in series if t >= cutoff]
    out[key] = series
    return out


def rolling_spread_median_bps(history: Dict[str, Any], symbol: str, now_ts: float,
                              window_s: float = 3600.0) -> Optional[float]:
    """Median spread over the trailing window, or None if no usable print.

    Returns None rather than a fabricated 1.0 default: `pre_send_gate` treats a
    missing median conservatively, and a wrong default here would silently
    widen or tighten the allowed spread for every asset.
    """
    series = (history or {}).get(str(symbol)) or []
    cutoff = float(now_ts) - float(window_s)
    vals = [float(b) for t, b in series
            if isinstance(t, (int, float)) and isinstance(b, (int, float))
            and float(t) >= cutoff and float(b) > 0]
    if not vals:
        return None
    try:
        return float(statistics.median(vals))
    except statistics.StatisticsError:
        return None


# ------------------------------------------------------------------ json state
def load_json_state(path: Any, default: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Read a JSON state file. Any failure yields `default`, never a raise."""
    try:
        import json
        import pathlib
        p = pathlib.Path(str(path))
        if p.exists():
            data = json.loads(p.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                return data
    except Exception:
        pass
    return dict(default or {})


def save_json_state(state: Dict[str, Any], path: Any) -> bool:
    """Write a JSON state file atomically-ish. Returns False on any failure."""
    try:
        import json
        import pathlib
        p = pathlib.Path(str(path))
        p.parent.mkdir(parents=True, exist_ok=True)
        tmp = p.with_suffix(p.suffix + ".tmp")
        tmp.write_text(json.dumps(state), encoding="utf-8")
        tmp.replace(p)
        return True
    except Exception:
        return False


SPREAD_STATE_FILENAME = ".spread_history_state.json"


def observe_and_median_spread(symbol: str, bps: Optional[float], now_ts: float,
                              state_path: Any, window_s: float = 3600.0) -> Optional[float]:
    """Record a spread print and return the rolling hourly median for `symbol`.

    Returns None when there is not yet a usable print, so the caller can decide
    how to degrade -- it must not silently substitute a fabricated median, which
    is exactly the defect that made the adaptive ceiling inert.
    """
    history = load_json_state(state_path, {})
    try:
        bps_f = float(bps) if bps is not None else None
    except (TypeError, ValueError):
        bps_f = None
    if bps_f is not None and bps_f > 0:
        history = record_spread_observation(history, symbol, now_ts, bps_f, window_s)
        save_json_state(history, state_path)
    return rolling_spread_median_bps(history, symbol, now_ts, window_s)


# ------------------------------------------------------ wall authenticity class
WALL_TOP_OF_BOOK = "TOP_OF_BOOK"
WALL_MIRRORED_LEG = "MIRRORED_LEG"
WALL_GENUINE = "GENUINE"

# Price proximity as a fraction of the reference price. 1e-6 keeps this below
# any instrument tick while still absorbing float rounding at 4 dp.
_TOP_OF_BOOK_EPS_FRAC = 1e-6
_MIRROR_PRICE_TOL_FRAC = 5e-4
_MIRROR_RATIO_MIN = 0.8


def is_top_of_book(side: str, price: float, best_bid: Optional[float],
                   best_ask: Optional[float],
                   eps_frac: float = _TOP_OF_BOOK_EPS_FRAC) -> bool:
    """True when the level IS the touch rather than resting depth behind it.

    A best-bid/best-ask print routinely exceeds the 150k whale threshold on
    liquid instruments -- BTC's top of book carried 719,971 / 377,384 USD this
    cycle -- so without this check ordinary top-of-book depth gets certified as
    a whale wall, in BOTH directions at once, which makes the flag worthless as
    evidence of directional commitment.
    """
    try:
        px = abs(float(price))
    except (TypeError, ValueError):
        return False
    if px <= 0:
        return False
    ref = best_ask if str(side).upper() == "SELL" else best_bid
    try:
        ref = abs(float(ref))
    except (TypeError, ValueError):
        return False
    if ref <= 0:
        return False
    return abs(px - ref) <= eps_frac * ref


def is_mirrored_leg(side: str, price: float, notional_usd: float,
                    opposite_legs: Iterable[Tuple[float, float]],
                    price_tol_frac: float = _MIRROR_PRICE_TOL_FRAC,
                    ratio_min: float = _MIRROR_RATIO_MIN) -> bool:
    """True when a size-matched opposite order sits at ~the same price.

    Such a pair is a two-sided bracket, not directional intent -- it is the
    shape a spoofed or hedged quote takes. Only the resting leg can be
    cancelled, so treating either side as whale backing is unsafe.
    """
    try:
        px, note = abs(float(price)), abs(float(notional_usd))
    except (TypeError, ValueError):
        return False
    if px <= 0 or note <= 0:
        return False
    for op in opposite_legs or ():
        try:
            opx, onote = abs(float(op[0])), abs(float(op[1]))
        except (TypeError, ValueError, IndexError):
            continue
        if opx <= 0 or onote <= 0:
            continue
        if abs(opx - px) > price_tol_frac * px:
            continue
        if min(note, onote) / max(note, onote) >= ratio_min:
            return True
    return False


def classify_wall(side: str, price: float, notional_usd: float,
                  best_bid: Optional[float], best_ask: Optional[float],
                  opposite_legs: Iterable[Tuple[float, float]]) -> str:
    """Return WALL_TOP_OF_BOOK | WALL_MIRRORED_LEG | WALL_GENUINE.

    Top of book is checked first: a level at the touch cannot be read as
    resting depth behind price regardless of what sits opposite it.
    """
    if is_top_of_book(side, price, best_bid, best_ask):
        return WALL_TOP_OF_BOOK
    if is_mirrored_leg(side, price, notional_usd, opposite_legs):
        return WALL_MIRRORED_LEG
    return WALL_GENUINE
