"""Cycle 200 drop-in: fail-closed numeric parsing and spread/capacity/freshness gates.

Pure and unit-tested in test_cycle200_fixes.py. Conventions:
  * a missing / non-finite / non-numeric value is None, never 0.0 or 50.0;
  * every gate returns False when any input is None (fail closed).
"""
from __future__ import annotations

import math
from typing import Iterable, Optional

NA = "N/A"

FLOOR_OPERATING = 4795.00      # operating buffer (floor + $20)
FLOOR_HARD = 4775.00           # catastrophic hard floor
STRESS_MULT = 1.25
STRESS_ADD = 2.00
MAX_CONCURRENT = 4

SPREAD_LIMIT_BPS = {"CRYPTO": 25.0, "TRADFI": 5.0}


def num(v) -> Optional[float]:
    """Finite float or None. Rejects bool, NaN, inf, '-', '', and non-numeric text."""
    if v is None or isinstance(v, bool):
        return None
    try:
        x = float(str(v).replace(",", "").strip()) if isinstance(v, str) else float(v)
    except (TypeError, ValueError):
        return None
    return x if math.isfinite(x) else None


def cell(v, fmt: str = "{:.4f}") -> str | float:
    """Value for a spreadsheet cell: formatted number or the literal 'N/A'."""
    x = num(v)
    return NA if x is None else float(fmt.format(x))


# ---------------------------------------------------------------- spread
def spread_bps(bid, ask, quote_age_s, max_age_s: float = 5.0) -> Optional[float]:
    """Single spread definition for the whole pipeline: (ask-bid)/mid * 1e4.

    Returns None for invalid, crossed, or stale quotes.
    """
    b, a, age = num(bid), num(ask), num(quote_age_s)
    if b is None or a is None or age is None:
        return None
    if b <= 0 or a <= 0 or a < b or age > max_age_s:
        return None
    mid = (a + b) / 2.0
    return (a - b) / mid * 1e4


def spread_gate(bps, category: str) -> bool:
    """True only if spread is known and within the category limit."""
    x = num(bps)
    limit = SPREAD_LIMIT_BPS.get(str(category).upper())
    if x is None or limit is None:
        return False
    return 0.0 <= x <= limit


# ---------------------------------------------------------------- capacity
def stressed_equity(equity, risks: Iterable[float]) -> Optional[float]:
    """Equity - sum(Risk_i * 1.25 + 2.00). None if any input is unknown."""
    e = num(equity)
    rs = [num(r) for r in risks]
    if e is None or any(r is None or r < 0 for r in rs):
        return None
    return e - sum(r * STRESS_MULT + STRESS_ADD for r in rs)


def admissible(equity, open_risks: Iterable[float], new_risk: float) -> bool:
    """True only if adding new_risk keeps stressed equity >= operating floor
    and the joint slot count stays <= MAX_CONCURRENT.
    """
    rs = [num(r) for r in open_risks]
    if any(r is None for r in rs):
        return False
    rs_all = rs + [new_risk]
    if len(rs_all) > MAX_CONCURRENT:
        return False
    s = stressed_equity(equity, rs_all)
    return s is not None and s >= FLOOR_OPERATING


def max_slots(equity, risk: float) -> int:
    """floor((Equity - 4795) / (risk*1.25 + 2)), clipped to [0, MAX_CONCURRENT].

    Uses a small epsilon so exact multiples are not lost to float error.
    """
    e = num(equity)
    if e is None or num(risk) is None or risk <= 0:
        return 0
    per = risk * STRESS_MULT + STRESS_ADD
    n = math.floor((e - FLOOR_OPERATING) / per + 1e-9)
    return max(0, min(MAX_CONCURRENT, n))


def four_slot_threshold(risk: float) -> float:
    """Equity above which 4 slots of `risk` are admissible."""
    return FLOOR_OPERATING + MAX_CONCURRENT * (risk * STRESS_MULT + STRESS_ADD)


# ---------------------------------------------------------------- freshness
def bar_fresh(last_bar_epoch, now_epoch, bar_s: int = 900, session_open: bool = True,
              bars_allowed: int = 2) -> bool:
    """Crypto (24/7): last closed bar must be within `bars_allowed` bars of now.
    TradFi outside session: freshness cannot be judged, so return False and let
    the caller use the explicit closed-market path.
    """
    last, now = num(last_bar_epoch), num(now_epoch)
    if last is None or now is None or not session_open:
        return False
    return 0.0 <= (now - last) <= bars_allowed * bar_s
