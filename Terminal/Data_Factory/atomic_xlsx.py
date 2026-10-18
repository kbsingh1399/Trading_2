"""Terminal/Data_Factory/atomic_xlsx.py
======================================
Canonical atomic workbook save, row-count guard, and formula evaluation cache.
"""
from __future__ import annotations

import os
import re
import shutil
from pathlib import Path

try:
    from Terminal.risk.fail_closed import NA, num
except ImportError:
    try:
        from ..risk.fail_closed import NA, num
    except ImportError:
        from fail_closed import NA, num

_SUM_FORMULA = re.compile(r"^=\s*([A-Z]+)(\d+)\s*\+\s*([A-Z]+)(\d+)\s*\+\s*([A-Z]+)(\d+)\s*$")


def atomic_save(wb, path) -> None:
    """Serialize to a temp file in the same directory, fsync, then os.replace.

    Keeps the previous workbook as <name>.bak so a bad run can be rolled back.
    """
    path = Path(path)
    tmp = path.with_name(path.stem + ".tmp" + path.suffix)
    bak = path.with_name(path.stem + ".bak" + path.suffix)
    wb.save(tmp)
    with open(tmp, "a+b") as fh:
        os.fsync(fh.fileno())
    if path.exists():
        shutil.copy2(path, bak)
    os.replace(tmp, path)


def check_minimums(counts: dict, minimums: dict) -> None:
    """Raise before saving if any harvest returned fewer rows than required.

    Prevents an outage from overwriting a good sheet with an empty one.
    """
    short = {k: (counts.get(k, 0), m) for k, m in minimums.items() if counts.get(k, 0) < m}
    if short:
        raise RuntimeError(f"refusing to save: harvest below minimum {short}")


def cache_sum_formulas(ws, sheet_formula_rows: range | None = None) -> dict:
    """Replace '=Fr+Gr+Hr'-style formulas with evaluated values, mirroring Excel.

    Excel semantics: blank operand -> 0; numeric text operand -> its number;
    any other text (e.g. '-') -> #VALUE!, which we write as 'N/A' rather than 0.
    Returns counts: {'cached': n, 'na': m, 'skipped': k}.
    """
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
            refs = [(m.group(1), int(m.group(2))), (m.group(3), int(m.group(4))), (m.group(5), int(m.group(6)))]
            vals = []
            bad = False
            for col, row in refs:
                raw = ws[f"{col}{row}"].value
                if raw is None or raw == "":
                    vals.append(0.0)
                    continue
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
    return out
