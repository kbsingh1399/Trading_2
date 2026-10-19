"""Cycle 201 round-2 corrections. Pure functions; no I/O.

Replaces four scorecard fixes that would re-introduce defects:
  * quote age defaulted to 0.5 s (fabricated freshness);
  * orderbook spread freshness relaxed to 60 s (contradicts the 5 s gate);
  * INACTIVE / UNKNOWN colours claimed without a defined rule;
  * a sheet-count check cannot detect a renamed or missing sheet.
Depends on fail_closed.py and data_quality.py in this folder.
"""
from __future__ import annotations

from typing import Iterable, Optional, Tuple

try:
    from .fail_closed import num, spread_bps
    from .data_quality import quote_or_na, age_hours
except ImportError:  # run as plain script / tests
    from fail_closed import num, spread_bps
    from data_quality import quote_or_na, age_hours

FRESHNESS_MAX_S = 5.0  # must match fail_closed.spread_bps default and SOP step S4


def quote_age_or_none(v) -> Optional[float]:
    """Age in seconds, or None. No default: a missing age is never fresh."""
    x = num(v)
    return x if (x is not None and x >= 0) else None


def execution_status(bid, ask, quote_age_s) -> Tuple[str, str]:
    """Return (status, colour). A missing or stale age can never be ACTIVE."""
    b, a = quote_or_na(bid), quote_or_na(ask)
    if b is None or a is None:
        return "MISSING QUOTE", "RED"
    if a <= b:
        return "INACTIVE", "AMBER"            # crossed book
    age = quote_age_or_none(quote_age_s)
    if age is None or age > FRESHNESS_MAX_S:
        return "INACTIVE", "AMBER"            # stale or unknown age
    return "ACTIVE EXECUTION", "GREEN"


def orderbook_spread(bid, ask, quote_age_s) -> Optional[float]:
    """Mid-based spread bps with the 5 s freshness gate. No relaxation."""
    return spread_bps(bid, ask, quote_age_or_none(quote_age_s), max_age_s=FRESHNESS_MAX_S)


def within_window(label, window_h: float = 24.0) -> bool:
    """True only if the label parses and is within the window.

    'just now' and 'now' count as age 0. Unparseable labels return False,
    but the caller must count them as rejected rather than dropping them.
    """
    if label is not None and str(label).strip().lower() in ("just now", "now"):
        return True
    a = age_hours(label)
    return a is not None and a <= window_h


def harvest_key(t: dict, harvest_epoch: float = 0.0) -> Optional[tuple]:
    """Key on the on-chain identity. The time label is not part of the key.

    Returns None when there is no full transaction hash; such rows must be
    flagged for review, not deduplicated on weaker fields.
    """
    tx = str(t.get("tx_hash", "")).strip().lower()
    if not (tx.startswith("0x") and len(tx) == 66):
        return None
    s = lambda k: str(t.get(k, "")).strip().lower()  # noqa: E731
    return (tx, s("from_address"), s("to_address"), s("token_symbol"),
            s("token_value"), s("usd_value"))


def sheet_guard(actual: Iterable[str], required: Iterable[str]) -> Tuple[list, list]:
    """Return (missing, unexpected) sheet names.

    Missing sheets are a hard failure. Unexpected sheets are a warning. The
    required list must come from the specification, not from a single run.
    """
    act = set(actual)
    req = list(required)
    missing = [r for r in req if r not in act]
    unexpected = sorted(act - set(req))
    return missing, unexpected
