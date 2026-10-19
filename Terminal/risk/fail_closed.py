"""Terminal/risk/fail_closed.py
=============================
Canonical drop-in fail-closed numeric parsing and spread/capacity/freshness gates.
(Hardened Cycle 201 implementation).
"""
from __future__ import annotations

import math
import re
from typing import Iterable, Optional

NA = "N/A"

FLOOR_OPERATING = 4795.00      # hard floor 4,775 + $20 operating buffer
FLOOR_HARD = 4775.00
STRESS_MULT = 1.25
STRESS_ADD = 2.00
MAX_CONCURRENT = 4

SPREAD_LIMIT_BPS = {"CRYPTO": 25.0, "TRADFI": 5.0}

# Plain decimal / scientific, e.g. "81722", "-1.5", ".5", "1e3".
_PLAIN = re.compile(r"^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$")
# Thousands-grouped only, e.g. "1,058,753.36". Anything else with a comma is rejected,
# so "1,5" (European decimal) and "1,234,5" are NOT silently read as 15 or 12345.
_GROUPED = re.compile(r"^[+-]?\d{1,3}(?:,\d{3})+(?:\.\d*)?$")


def num(v) -> Optional[float]:
    """Finite float or None.

    Accepts int/float (not bool) and strings that are plain decimals or
    thousands-grouped. Rejects bool, NaN, inf, '-', '', '1_000', '1,5', '1,234,5'.
    """
    if v is None or isinstance(v, bool):
        return None
    if isinstance(v, str):
        s = v.strip()
        if _GROUPED.match(s):
            s = s.replace(",", "")
        elif not _PLAIN.match(s):
            return None
        try:
            x = float(s)
        except ValueError:
            return None
    else:
        try:
            x = float(v)
        except (TypeError, ValueError):
            return None
    return x if math.isfinite(x) else None


def cell(v, fmt: str = "{:.4f}"):
    """Spreadsheet cell value: formatted number, or the literal 'N/A'."""
    x = num(v)
    return NA if x is None else float(fmt.format(x))


# ---------------------------------------------------------------- spread
def spread_bps(bid, ask, quote_age_s, max_age_s: float = 5.0) -> Optional[float]:
    """Single spread definition: (ask - bid) / mid * 1e4.

    None for: missing, non-positive, crossed (ask < bid), LOCKED (ask == bid,
    which is treated as a frozen quote, not a 0 bps spread), or stale quotes.
    """
    b, a, age = num(bid), num(ask), num(quote_age_s)
    if b is None or a is None or age is None:
        return None
    if b <= 0 or a <= 0 or a <= b or age < 0 or age > max_age_s:
        return None
    mid = (a + b) / 2.0
    return (a - b) / mid * 1e4


def spread_gate(bps, category: str) -> bool:
    """True only if the spread is known and 0 <= spread <= category limit."""
    x = num(bps)
    limit = SPREAD_LIMIT_BPS.get(str(category).upper())
    return x is not None and limit is not None and 0.0 <= x <= limit


# ---------------------------------------------------------------- capacity
def stressed_equity(equity, risks: Iterable) -> Optional[float]:
    """Equity - sum(Risk_i * 1.25 + 2.00). None if any input is unknown or negative."""
    e = num(equity)
    rs = [num(r) for r in risks]
    if e is None or any(r is None or r < 0 for r in rs):
        return None
    return e - sum(r * STRESS_MULT + STRESS_ADD for r in rs)


def admissible(equity, open_risks: Iterable, new_risk) -> bool:
    """True only if adding new_risk keeps stressed equity >= 4,795 and the
    joint slot count stays <= 4. Any unknown input -> False.
    """
    rs = [num(r) for r in open_risks]
    if any(r is None for r in rs) or len(rs) + 1 > MAX_CONCURRENT:
        return False
    s = stressed_equity(equity, rs + [new_risk])
    return s is not None and s >= FLOOR_OPERATING


def max_slots(equity, risk) -> int:
    """floor((Equity - 4795) / (Risk*1.25 + 2)), clipped to [0, 4].

    risk is validated with num(), so a string such as "15" is handled
    (Cycle 200 raised TypeError on it). Unknown or non-positive risk -> 0.
    """
    e, r = num(equity), num(risk)
    if e is None or r is None or r <= 0:
        return 0
    per = r * STRESS_MULT + STRESS_ADD
    n = math.floor((e - FLOOR_OPERATING) / per + 1e-9)
    return max(0, min(MAX_CONCURRENT, n))


def four_slot_threshold(risk) -> Optional[float]:
    """Equity needed for 4 slots of `risk`: 4,795 + 4*(Risk*1.25 + 2). None if risk unknown."""
    r = num(risk)
    if r is None or r <= 0:
        return None
    return FLOOR_OPERATING + MAX_CONCURRENT * (r * STRESS_MULT + STRESS_ADD)


# ---------------------------------------------------------------- freshness
def bar_fresh(last_bar_epoch, now_epoch, bar_s: int = 900, session_open: bool = True,
              bars_allowed: int = 2) -> bool:
    """last_bar_epoch is the bar OPEN time (epoch seconds).

    A current feed has open-age in [bar_s, 2*bar_s). With bars_allowed=2 the
    check passes while open-age <= 2*bar_s, and fails for a feed one bar stale.
    Future-dated bars fail. TradFi outside session -> False (caller shows CLOSED).
    """
    last, now = num(last_bar_epoch), num(now_epoch)
    if last is None or now is None or not session_open:
        return False
    age = now - last
    return 0.0 <= age <= bars_allowed * bar_s
