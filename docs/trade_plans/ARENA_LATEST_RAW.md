\nI can't verify `b210b94c1` or your `main`. It isn't in my checkout, and my sandbox has no remote access. Your run output is also not reproducible from here. What I can verify is the code. Several of the Cycle 200 behaviours you're relying on are wrong, and I've fixed them in Cycle 201 (commit `b654474` on `arena/74cd2d1a-trading-2`, not pushed). The new suite passes 46/46, and the Cycle 200 suite still passes 21/21.\n\n## Audit of the applied Cycle 200 items\n\n\n| Item | Finding | Cycle 201 fix |\n| --- | --- | --- |\n| F1 `num()` | Strips commas, so `"1,5"` → 15 and `"1,234,5"` → 12345. Also accepts `"1_000"`. Your pasted code still has `.replace(",", "")`, so the summary's "rejects `"-"`/`""`" is correct but the comma case is not. | Strict regex: plain decimal or thousands-grouped only. |\n| F2 blanks | Blank operands count as 0, so a missing OKX leg gives a total with no flag. For a liquidation metric this under-reports risk without warning. | Blank → `"N/A"` by default. `blank_policy="zero"` is an explicit opt-in. |\n| F5 spread | `a < b` lets a locked quote (ask == bid) through as 0 bps, which passes the 25/5 gate. | Locked quotes return `None`. |\n| F6 `max_slots` | `risk <= 0` is evaluated on the raw input, so `max_slots(4863.74, "15")` raises `TypeError`. | Risk goes through `num()` first. |\n| F3 atomic save | Replaces the live file without re-opening the temp file. An Excel lock raises an unhandled `PermissionError`. | Verify temp before replace, optional sheet-count check, and lock handling that leaves the original intact. |\n| WB verification | `CorruptLoad=0` is the normal-load open mode. A clean open does not report "0 repair flags", and it doesn't check that formulas evaluate. | Not a code issue. Use a separate check if you need repair-flag evidence. |\n| F2 scope | "4,760 cells across `Exchange_Liquidation_Map_1D` and `7D`" — I counted 4,760 formula cells across the whole workbook in C200. I did not check the per-sheet split or `7D`. | Please confirm the split from the workbook. |\n| Duplication | Three copies of the same logic (`Cycle_200_fixes/`, `Terminal/risk/`, `Terminal/Data_Factory/`). They will drift. | Keep one import location. |\n| Credential | The `sk-gemini` literal is still in git history. Removing it from the file doesn't remove it from `main`. | Rotate the key. |\n\n\nI can't check your `Terminal/risk/fail_closed.py`, `Terminal/Data_Factory/atomic_xlsx.py`, the spec edits (lines 53, 298, 484–504), or the 23.21 s run. I'd leave the readiness rating at 1/10 until the council runs these suites on `main` and there is a pipeline-level test (for example, a missing OKX leg must produce `N/A`).\n\n## Cycle 201 code\n\n\n### Cycle_201_fixes/fail_closed.py\n\n\n```\n"""Cycle 201 drop-in (supersedes Cycle_200_fixes/fail_closed.py).

Fail-closed numeric parsing and gates. Pure functions, no I/O.
Conventions:
  * unknown / malformed / non-finite value -> None (never 0.0, never 50.0);
  * every gate returns False (or 0 slots) when any input is None.
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
    return 0.0 <= age <= bars_allowed * bar_s\n```\n\n### Cycle_201_fixes/atomic_xlsx.py\n\n\n```\n"""Cycle 201 drop-in (supersedes Cycle_200_fixes/atomic_xlsx.py).

Atomic workbook save with verify-before-replace, row-count guard, and an
Excel-equivalent '=F+G+H' evaluator that treats a missing operand as N/A by default.
"""
from __future__ import annotations

import os
import re
import shutil
from pathlib import Path

import openpyxl

try:
    from .fail_closed import NA, num
except ImportError:  # run as plain script / tests
    from fail_closed import NA, num

_SUM_FORMULA = re.compile(
    r"^=\s*([A-Z]+)(\d+)\s*\+\s*([A-Z]+)(\d+)\s*\+\s*([A-Z]+)(\d+)\s*$"
)


def _default_verify(path: Path) -> bool:
    """Re-open the written temp file. Raises if it is not a readable workbook."""
    wb = openpyxl.load_workbook(path, read_only=True)
    try:
        return len(wb.sheetnames) > 0
    finally:
        wb.close()


def atomic_save(wb, path, verify=None, expected_sheets: int | None = None) -> None:
    """Write temp -> fsync -> verify temp -> keep .bak -> os.replace.

    * The live file is replaced only after the temp file re-opens and passes
      verification (sheet count == expected_sheets when given).
    * If the target is locked (e.g. open in Excel) os.replace raises
      PermissionError; we raise RuntimeError and the original is left intact.
    """
    path = Path(path)
    tmp = path.with_name(path.stem + ".tmp" + path.suffix)
    bak = path.with_name(path.stem + ".bak" + path.suffix)

    wb.save(tmp)
    with open(tmp, "rb") as fh:
        os.fsync(fh.fileno())

    ok = (verify(tmp) if verify is not None else _default_verify(tmp))
    if not ok:
        raise RuntimeError(f"verification failed for {tmp}; original left intact")
    if expected_sheets is not None:
        n = len(openpyxl.load_workbook(tmp, read_only=True).sheetnames)
        if n != expected_sheets:
            raise RuntimeError(f"sheet count {n} != expected {expected_sheets}; original left intact")

    if path.exists():
        shutil.copy2(path, bak)
    try:
        os.replace(tmp, path)
    except PermissionError as exc:
        raise RuntimeError(
            f"{path} is locked (open in Excel?). Original left intact; new copy kept at {tmp}"
        ) from exc


def check_minimums(counts: dict, minimums: dict) -> None:
    """Raise if any harvest is below its minimum. A missing key counts as 0 (fail closed)."""
    short = {k: (counts.get(k, 0), m) for k, m in minimums.items() if counts.get(k, 0) < m}
    if short:
        raise RuntimeError(f"refusing to save: harvest below minimum {short}")


def cache_sum_formulas(ws, sheet_formula_rows: range | None = None,
                       blank_policy: str = "na") -> dict:
    """Evaluate '=Fr+Gr+Hr' formulas and replace them with values.

    blank_policy:
      "na"   (default, fail closed): any blank operand -> "N/A". A missing
             exchange leg must not silently under-report the total.
      "zero" (explicit opt-in only): blank operand -> 0.
    Numeric text operands are read with num(). Any other text (e.g. "-") -> "N/A".
    Returns {'cached': n, 'na': m, 'skipped': k}.
    NOTE: this replaces the formula. To keep the live formula, write the value
    to a new column instead.
    """
    if blank_policy not in ("na", "zero"):
        raise ValueError("blank_policy must be 'na' or 'zero'")
    out = {"cached": 0, "na": 0, "skipped": 0}
    rows = sheet_formula_rows or range(1, ws.max_row + 1)
    for r in rows:
        for c in ws[r]:
            v = c.value
            if not (isinstance(v, str) and v.startswith("=")):
                continue
            m = _SUM_FORMULA.match(v)
            if not m:
                out["skipped"] += 1
                continue
            refs = [(m.group(1), int(m.group(2))),
                    (m.group(3), int(m.group(4))),
                    (m.group(5), int(m.group(6)))]
            vals, bad = [], False
            for col, row in refs:
                raw = ws[f"{col}{row}"].value
                if raw is None or (isinstance(raw, str) and raw.strip() == ""):
                    if blank_policy == "zero":
                        vals.append(0.0)
                        continue
                    bad = True
                    break
                x = num(raw)
                if x is None:
                    bad = True
                    break
                vals.append(x)
            if bad:
                c.value = NA
                out["na"] += 1
            else:
                c.value = round(sum(vals), 2)
                out["cached"] += 1
    return out\n```\n\n### Cycle_201_fixes/test_cycle201_fixes.py\n\n\n```\nimport os
import sys

sys.path.insert(0, os.path.dirname(__file__))

import openpyxl  # noqa: E402
import pytest  # noqa: E402

from fail_closed import (  # noqa: E402
    NA, num, cell, spread_bps, spread_gate, stressed_equity, admissible,
    max_slots, four_slot_threshold, bar_fresh,
)
from atomic_xlsx import atomic_save, check_minimums, cache_sum_formulas  # noqa: E402
import atomic_xlsx  # noqa: E402


# ---- F1: numeric parsing, strict
@pytest.mark.parametrize("v", [None, "", "-", "nan", "inf", "-inf", "1e400",
                               "abc", True, False, float("nan"), float("inf"),
                               "1,5", "1,234,5", "1_000", "12,34", " ", "0x1A"])
def test_num_rejects_unknown_or_ambiguous(v):
    assert num(v) is None


@pytest.mark.parametrize("v,expected", [
    ("1,234.5", 1234.5), ("1,058,753.36", 1058753.36), ("0", 0.0), (0, 0.0),
    ("-1.5", -1.5), (" 81722 ", 81722.0), (".5", 0.5), ("1e3", 1000.0), (7, 7.0),
])
def test_num_accepts_plain_and_grouped(v, expected):
    assert num(v) == pytest.approx(expected)


def test_cell_renders_na_not_zero():
    assert cell(None) == NA
    assert cell("1,5") == NA           # ambiguous -> N/A, not 15
    assert cell(1.23456, "{:.2f}") == 1.23


# ---- F5: spread, locked and stale quotes fail closed
def test_spread_matches_live_btc_snapshot():
    assert round(spread_bps(81722.0, 81738.0, 0.1), 2) == 1.96


def test_spread_locked_quote_is_none_not_zero():
    assert spread_bps(100.0, 100.0, 0.1) is None      # was 0.0 in Cycle 200
    assert spread_gate(spread_bps(100.0, 100.0, 0.1), "CRYPTO") is False


def test_spread_invalid_or_stale_is_none():
    assert spread_bps(None, 81738.0, 0.1) is None
    assert spread_bps(81738.0, 81722.0, 0.1) is None   # crossed
    assert spread_bps(81722.0, 81738.0, 6.0) is None   # stale > 5 s
    assert spread_bps(81722.0, 81738.0, -1.0) is None  # negative age
    assert spread_bps(0.0, 1.0, 0.1) is None


def test_spread_gate_limits_and_fail_closed():
    assert spread_gate(25.0, "CRYPTO") is True
    assert spread_gate(25.06, "CRYPTO") is False       # live SOL fails
    assert spread_gate(23.17, "CRYPTO") is True        # live XRP passes
    assert spread_gate(5.0, "TRADFI") is True
    assert spread_gate(6.76, "TRADFI") is False        # live EURUSD fails
    assert spread_gate(None, "CRYPTO") is False
    assert spread_gate(0.0, "UNKNOWN") is False


# ---- F6: capacity
def test_stressed_equity_formula():
    assert stressed_equity(4863.74, [25.0, 25.0]) == pytest.approx(4797.24)
    assert stressed_equity(4863.74, [25.0, None]) is None
    assert stressed_equity(4863.74, [-5.0]) is None


def test_max_slots_matches_remediation_claims():
    assert max_slots(4863.74, 25.0) == 2
    assert max_slots(4863.74, 15.0) == 3


def test_max_slots_accepts_numeric_string_risk():
    assert max_slots(4863.74, "15") == 3              # was TypeError in Cycle 200
    assert max_slots(4863.74, "15,0") == 0           # ambiguous string -> 0 slots
    assert max_slots(4863.74, "abc") == 0


def test_four_slot_threshold_4878_and_unknown_risk():
    assert four_slot_threshold(15.0) == pytest.approx(4878.0)
    assert four_slot_threshold("15") == pytest.approx(4878.0)
    assert four_slot_threshold(None) is None
    assert max_slots(4878.0, 15.0) == 4
    assert max_slots(4877.99, 15.0) == 3


def test_admissible_fail_closed():
    assert admissible(4863.74, [], 25.0) is True
    assert admissible(4863.74, [25.0], 25.0) is True
    assert admissible(4863.74, [25.0, 25.0], 25.0) is False
    assert admissible(4863.74, [None], 15.0) is False
    assert admissible(4863.74, [15.0] * 4, 15.0) is False
    assert admissible(4863.74, [], None) is False


# ---- freshness
def test_bar_freshness():
    now = 1_000_000.0
    assert bar_fresh(now - 1000, now) is True          # open-age in [900,1800)
    assert bar_fresh(now - 2000, now) is False         # one bar stale
    assert bar_fresh(now + 60, now) is False           # future-dated
    assert bar_fresh(None, now) is False
    assert bar_fresh(now - 60, now, session_open=False) is False


# ---- F2: formula cache, blank = N/A by default
def _sheet():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws["F3"], ws["G3"], ws["H3"] = 1058753.36, 743422.24, 1077880.33
    ws["I3"] = "=F3+G3+H3"
    ws["F4"], ws["G4"], ws["H4"] = 1.0, None, 2.0       # blank OKX leg
    ws["I4"] = "=F4+G4+H4"
    ws["F5"], ws["G5"], ws["H5"] = "-", 1.0, 2.0        # dash text
    ws["I5"] = "=F5+G5+H5"
    ws["F6"], ws["G6"], ws["H6"] = "1,058.5", 1.0, 2.0  # numeric text with grouping
    ws["I6"] = "=F6+G6+H6"
    ws["I7"] = "=SUM(F7:H7)"                            # unsupported -> skipped
    return wb, ws


def test_formula_cache_blank_is_na_by_default():
    _, ws = _sheet()
    stats = cache_sum_formulas(ws)
    assert ws["I3"].value == round(1058753.36 + 743422.24 + 1077880.33, 2)
    assert ws["I4"].value == NA                         # was 3.0 in Cycle 200
    assert ws["I5"].value == NA
    assert ws["I6"].value == round(1058.5 + 1.0 + 2.0, 2)
    assert ws["I7"].value == "=SUM(F7:H7)"
    assert stats == {"cached": 2, "na": 2, "skipped": 1}


def test_formula_cache_blank_zero_is_explicit_opt_in():
    _, ws = _sheet()
    cache_sum_formulas(ws, blank_policy="zero")
    assert ws["I4"].value == 3.0


def test_formula_cache_rejects_bad_policy():
    _, ws = _sheet()
    with pytest.raises(ValueError):
        cache_sum_formulas(ws, blank_policy="guess")


# ---- F3: atomic save, verify before replace, lock handling, minimums
def test_atomic_save_creates_bak_and_cleans_tmp(tmp_path):
    wb, _ = _sheet()
    p = tmp_path / "DataBase_Trading.xlsx"
    atomic_save(wb, p, expected_sheets=1)
    assert p.exists()
    assert not (tmp_path / "DataBase_Trading.tmp.xlsx").exists()
    atomic_save(wb, p, expected_sheets=1)
    assert (tmp_path / "DataBase_Trading.bak.xlsx").exists()


def test_failed_verify_leaves_original_untouched(tmp_path):
    wb, _ = _sheet()
    p = tmp_path / "DataBase_Trading.xlsx"
    atomic_save(wb, p)
    before = p.read_bytes()
    with pytest.raises(RuntimeError):
        atomic_save(wb, p, verify=lambda t: False)
    assert p.read_bytes() == before


def test_wrong_sheet_count_leaves_original_untouched(tmp_path):
    wb, _ = _sheet()
    p = tmp_path / "DataBase_Trading.xlsx"
    atomic_save(wb, p)
    before = p.read_bytes()
    with pytest.raises(RuntimeError, match="sheet count"):
        atomic_save(wb, p, expected_sheets=40)
    assert p.read_bytes() == before


def test_locked_target_raises_and_keeps_original(tmp_path, monkeypatch):
    wb, _ = _sheet()
    p = tmp_path / "DataBase_Trading.xlsx"
    atomic_save(wb, p)
    before = p.read_bytes()

    def locked(src, dst):
        raise PermissionError("locked")

    monkeypatch.setattr(atomic_xlsx.os, "replace", locked)
    with pytest.raises(RuntimeError, match="locked"):
        atomic_save(wb, p)
    assert p.read_bytes() == before
    assert (tmp_path / "DataBase_Trading.tmp.xlsx").exists()   # new copy kept


def test_check_minimums_missing_key_fails_closed():
    with pytest.raises(RuntimeError):
        check_minimums({}, {"arkham": 50})
    with pytest.raises(RuntimeError):
        check_minimums({"arkham": 0}, {"arkham": 50})
    check_minimums({"arkham": 138}, {"arkham": 50})\n```\n\n## Wiring notes\n\n\n- **Run:** `pytest -q Cycle_201_fixes/test_cycle201_fixes.py` from the repo root. Requires Python 3.10+ for the `int | None` and `range | None` annotations. Each test file is loaded with the same `sys.path` setup, so one copy of each module is enough.\n- **Breaking changes:**
\n- `four_slot_threshold()` now returns `None` for an unknown risk, not a float. Callers that format it need a `None` check.\n- `cache_sum_formulas()` now writes `"N/A"` for blank operands by default. The pipeline must pass `blank_policy="zero"` explicitly if it wants the old behaviour, and I'd recommend against that.\n- `atomic_save()` raises `RuntimeError` on a locked target. The caller should tell the operator to close Excel and retry.\n\n- **Pipeline-level test still missing:** a test that runs `master_excel_pipeline.py` with a missing OKX leg and checks the liquidation cell reads `N/A`. Unit tests don't cover the wiring.\n- **Commit:** `b654474` on `arena/74cd2d1a-trading-2`. Nothing was pushed, and `main` is unchanged in this session.\n