\nI can't wire these into `main`. This session is closed for remote GitHub operations, and it is fixed to `arena/74cd2d1a-trading-2`, so I can't push or open a PR. The files are committed locally as `c90ad9b` on that branch, and the full contents are below, copied from disk.\n\nTwo limits to read before the council uses them:\n\n- The `Cycle_200_fixes/` modules are tested in isolation (21/21). The F1–F7 pipeline snippets in the report are not applied patches. They refer to variables such as `ws`, `q` and `counts` that exist only in the real pipeline, and the `check_minimums` thresholds are placeholders.\n- Section 5 of the report refers to "§3.5", which does not exist. The "4,878 capacity threshold" row in §1 is the intended target.\n\n## Cycle_200_Remediation_Audit.md\n\n\n```\n# Cycle 200 — Re-audit of "Comprehensive Remediation of all Cycle 199 Audit Concerns"

**Repo:** `kbsingh1399/Trading_2` · **Audited ref:** `main` @ `cf62dc9` (2026-10-19 03:23:47 +0530) · **Local branch:** `arena/74cd2d1a-trading-2` (`17dca57`)
**Status:** NOT CERTIFIED · **Institutional-grade:** NO · **Autonomous-execution ready:** NO · **Readiness: 1/10**
**Reference time for live-data checks:** 2026-10-18 22:14 UTC (snapshot `as_of_utc` 2026-10-18 05:14:06 UTC, ~17 h old).

Remote verification was not possible (fetch blocked). Every statement below is against the `main` blobs extracted to `/tmp/q200/`.

---

## 1. Headline

The 14-point remediation is **not present** on `main`, on the local branch, or on any other ref. The submission describes a state of the code that the repository does not contain. Searches for every remediation artifact returned zero matches in the committed tree:

| Claimed artifact | `main` result |
|---|---|
| `cache_liquidation_map_formulas` | 0 |
| `os.replace` atomic save (pipeline) | 0 (`os.replace` exists only in unrelated modules) |
| `DataBase_Trading.tmp` / `tmp.xlsx` | 0 |
| `GEMINI_WEB2API_AUTH` | 0 |
| `CandleIndicatorEngine` wired into pipeline | 0 (class exists only in `Terminal/Candle_Indicator_Engine.py`) |
| `Stage 3A`, `Stage 3B` | 0 in spec |
| `4,878` capacity threshold | 0 in code (arithmetic only, see §3.5) |
| `16.89 s` latency figure | 0 (no artifact) |
| Spec line 53 reconciled to 4,795 | **Not done**: still `Σ(Risk×1.25) ≥ 4,775.00` |
| `sk-gemini` removed | **Not done**: 2 hits in `master_excel_pipeline.py` |
| 19-column Sheet 33 / zero nulls | Not in `main`; workbook unchanged |

Workbook formulas are still uncached in the committed file. The snapshot still reads `DENIED_UNVERIFIED_ORDERFLOW`, with capacity 0/4.

Verdict: **the remediation claims cannot be accepted.** Items that are arithmetically correct are not implemented, and several claims are contradicted by the data.

---

## 2. Claim-by-claim result

| # | Claim | Result | Evidence |
|---|---|---|---|
| 1 | Candle indicators from 800-bar MT5 history replace defaults | **FAIL (not wired)** | Engine exists; `master_excel_pipeline.py` still uses `ci.get("rsi_14", 50.0)`, `atr_14 0.0`, `vwap_z_score 0.0` (L359–366). Engine `sync_candles` default `count=512`, not 800. No staleness check. |
| 2 | Liquidation map formulas cached, 4,760 cells | **FAIL** | No cache function. Formula `=F3+G3+H3` in column I (Binance/OKX/Bybit) is the correct mapping, but F/G/H hold numeric-text strings and `-` cells; plain cache would coerce those to 0 (see fix F2). |
| 3 | Atomic save, `GEMINI_WEB2API_AUTH`, `sk` literal removed | **FAIL** | `wb.save` non-atomic (L1530 region); `Bearer sk-gemini` still present (L1473 region). |
| 4 | Spec line 53 reconciled to 4,795 | **FAIL** | `main` line 53: `Equity − Σ(Risk×1.25) ≥ 4,775.00`. Line 296 (the 2.00-per-slot form at 4,795) is still the only correct statement; the two lines still contradict. |
| 5 | Capacity 2/3/4 slots, threshold 4,878 | **Arithmetic correct, not enforced** | 4,795 + 4×20.75 = 4,878.00 ✓. Max slots: 2 at $25 (4,863.74), 3 at $15 ✓. But `4795` appears only as a default in the pipeline (L136); no `max_slots` / admission function exists in `Terminal/`. The snapshot capacity "rule" is a text string. |
| 6 | Stage 3A / 3B, rollover 21:30–22:30 UTC gate | **FAIL / PARTIAL** | Stage 3A/3B absent. Rollover window exists (spec L131, L563) but nothing enforces it in code. The 22:14 UTC reference time falls **inside** the window. |
| 7 | Spread values (BTC 1.96 …) | **Correct against snapshot; source conflict unresolved** | Recomputed `(ask−bid)/mid×1e4` matches stored `spread_bps` for 23/24. EURUSD stored 6.76 vs recomputed 6.23. Workbook MT5 path uses ask-denominator and live overrides, so workbook values differ. Two sources, one gate: unresolved. |
| 8 | Telemetry: FOMC runway 252.77 h, Deribit +14.29 IV, Arkham $38.96B "verified on-chain", MicroStrategy "$70.18B total balance sheet" | **Mixed** | FOMC arithmetic: 2026-10-28 18:00 UTC − 2026-10-18 05:14:06 UTC = 252.77 h ✓, but the workbook still shows 252.26 h. Deribit: 37.93 vs 52.22 → gap 14.29 IV pts ✓, relative +37.67% ✓. "$38.96B verified on-chain": **not verified**; it is an Arkham label, and the sheet conflicts with the `main` registry. "$70.18B total balance sheet": **wrong label**; it is 848,000 BTC valued in USD, not a balance sheet total. |
| 9 | Sheet numbers in prompt corrected | **Correct** | Arkham_Whales_Holdings 40, Bitcoin_Treasuries 36, Volatility_Sentiment 37, MT5_Live_Quotes_Account 38, Cognitive_Council_Telemetry 39. |
| 10 | Clopper-Pearson 0.4197 | **Reproduced** | 11/17 one-sided 95% lower bound = 0.4197. Calibration still n=17 vs 100-trade minimum (CALIBRATING). |
| 11 | Zero nulls / 19-column Sheet 33 | **FAIL** | Not in `main`. Workbook still has defaults (`or 0.0`) and `N/A` count 0 in pipeline. |
| 12 | 16.89 s total latency | **UNVERIFIED** | No artifact. C199 claim of 15.42 s also has no reproducible artifact. |
| 13 | Freshness / data currency gate | **FAIL** | Crypto last 15m bar 2026-10-18 04:45 UTC (17.5 h old). TradFi last bar 2026-10-16 19:30–20:30 UTC (~50 h, weekend). No flag, no gate. Snapshot stays `DENIED_UNVERIFIED_ORDERFLOW`. |
| 14 | Hyperdash "50 verified" | **NOT CONFIRMED** | Not reproduced in Hyperdash_Flow_Feed (736 whale trades, 9,264 liquidations). |

---

## 3. Corrections to Cycle 199

1. **Spread counts were wrong.** C199 said crypto 4/14 and TradFi 8/10 pass the 25/5 bps gate, using workbook MT5 quotes. On the snapshot `spread_bps` (the source the spec's telemetry uses):
   - Crypto ≤ 25 bps: **5/14** pass (BTC 1.96, ETH 11.6, BNB 8.33, XRP 23.17, BCH 20.95). SOL 25.06 fails narrowly. 9 fail.
   - TradFi ≤ 5 bps: **7/10** pass (SP500 1.14, NAS100 0.49, DJ30 0.39, GER40 0.31, GOLD 1.06, USWTI 3.0, GBPUSD 3.0). EURUSD 6.76, USDJPY 8.73, SILVER 14.04 fail.
   The conclusion (the gate disqualifies most crypto perps, and the spec is internally inconsistent) stands. The counts in C199 do not.
2. **Fail-open spread default.** Pipeline L247: `spread_bps = q.get("spread_bps", 0.0) or 0.0`. A missing quote becomes **0 bps and passes every gate**. This is worse than C199 described.
3. **ETF / ETH IV labels:** C199 said "+14.29%". Correct: +14.29 IV points, +37.67% relative.

---

## 4. Readiness rating

**1 / 10.** Unchanged from C199. Reasons:
- Remediation not in any ref; several claims are false on the committed tree.
- Fail-open defaults remain across Telemetry, Orderbook and Basis sheets (`or 0.0`, `50.0`, `0.0`).
- Stale data (17.5 h crypto, ~50 h TradFi) is not flagged anywhere.
- Capacity/stressed-equity rule exists as text only; nothing enforces it.
- Spec contradicts itself (line 53 vs 296; ATR 0.35 at L311 vs 0.50 at L247; FOMC stand-aside at L449 vs disabled telemetry blackout).
- Whale data covers 18 assets; no whale data for any of 10 TradFi.

NOT institutional-grade. NOT ready for autonomous execution. The system is currently correct to deny trading (`DENIED_UNVERIFIED_ORDERFLOW`, 0/4 slots).

---

## 5. Exact fixes

All fix code is in `Cycle_200_fixes/` on this branch. It is **not wired into `main`**. 21 unit tests pass (`pytest Cycle_200_fixes/test_cycle200_fixes.py`, run in `/tmp/q199/venv`). Each fix below gives the file, the line, and the replacement.

### F1 — Fail-closed numeric parsing (replaces `or 0.0` / `get(…, 0.0)` / `50.0`)
File: `Terminal/Data_Factory/master_excel_pipeline.py`, all sheet builders (L124–136, L155–162, L244–266, L352–366).

```python
from Cycle_200_fixes.fail_closed import num, cell   # or copy the module

# replace every  acc.get("balance_usd", 0.0)  style default with:
rows.append(("Account Capital", "balance_usd", cell(acc.get("balance_usd")), "USD", ...))
# and  ci.get("rsi_14", 50.0) or 50.0  with:
rsi = num(ci.get("rsi_14"))          # None -> "N/A", never 50.0\n```\n\nAlso remove `or 0.0` from L244–266 and L352–366 and use `num(...)`. A real zero stays valid because `num(0)` returns `0.0`.\n\n### F2 — Liquidation map: exact Excel semantics\n\n\nFile: pipeline, sheet `Exchange_Liquidation_Map_1D`.\n\n```\nfrom Cycle_200_fixes.atomic_xlsx import cache_sum_formulas
stats = cache_sum_formulas(ws)     # {'cached': n, 'na': m, 'skipped': k}\n```\n\nBlank operand → 0; numeric text → number; `-` or other text → `"N/A"` (Excel would give `#VALUE!`). **Preferred alternative:** write the value to a new column (e.g. `J = ROUND(F+G+H,2)` evaluated in Python) and keep the live formula in column I, because openpyxl cannot store a cached value alongside a formula.\n\n### F3 — Atomic save and row-count guard\n\n\nFile: pipeline, `run_pipeline` save (L1530 region).\n\n```\nfrom Cycle_200_fixes.atomic_xlsx import atomic_save, check_minimums
check_minimums(counts, {"arkham_entities": 40, "treasury_rows": 50, "calendar_rows": 20, "orderflow_rows": 100})
atomic_save(wb, "Data/DataBase_Trading.xlsx")   # tmp + fsync + os.replace, keeps .bak\n```\n\nAlso guard `recreate_sheet` (L83): call `check_minimums` before clearing a sheet, so an empty harvest does not wipe good data.\n\n### F4 — Remove the hard-coded credential\n\n\nFile: pipeline L1473 region.\n\n```\nkey = os.environ.get("GEMINI_WEB2API_AUTH")
if not key:
    raise RuntimeError("GEMINI_WEB2API_AUTH not set; refusing to call Gemini")
headers = {"Authorization": f"Bearer {key}"}\n```\n\nRotate the `sk-gemini` value: it is in git history, so deleting it from the file does not remove it from `main`.\n\n### F5 — One spread definition, fail closed, with freshness\n\n\nFile: pipeline L244–247.\n\n```\nfrom Cycle_200_fixes.fail_closed import spread_bps, spread_gate
sp = spread_bps(q.get("bid"), q.get("ask"), q.get("quote_age_s"), max_age_s=5.0)
ok = spread_gate(sp, category)     # category "CRYPTO" (25 bps) or "TRADFI" (5 bps)\n```\n\nReplace the workbook ask-denominator and `spread_bps or 0.0` with this. Use the snapshot mid-based definition everywhere. `spread_gate(None, …)` returns False.\n\n### F6 — Enforce the stressed-equity / slot rule in code\n\n\nFile: execution path (the bridge that places orders; not in `Terminal/` today, so this is new code).\n\n```\nfrom Cycle_200_fixes.fail_closed import admissible, max_slots, four_slot_threshold
assert admissible(equity, open_risks, new_risk)   # False blocks the order
slots = max_slots(equity, new_risk)               # 2 at $25 @4,863.74; 3 at $15\n```\n\nSpec line 53 must be replaced with the line 296 form (see S1). Without this enforcement the 4,878 threshold is only documentation.\n\n### F7 — Candle freshness and history length\n\n\nFile: `Terminal/Candle_Indicator_Engine.py` `sync_candles` (default `count=512` → `800`, and the pipeline must call with `count=800`).\n\n```\nfrom Cycle_200_fixes.fail_closed import bar_fresh
fresh = bar_fresh(last_bar_epoch, now_epoch, bar_s=900, session_open=is_session_open(asset))\n```\n\nTradFi outside session returns False and is shown as `CLOSED`, not as data. Also remove `or 0.0` on volume (L137, L147–151). Use `None` so missing volume does not look like zero volume.\n\n### F8 — Macro blackout and FOMC gate\n\n\nThis is an operator decision (see §6). Code change needed once decided: if the guard is enforced, use one flag, `MACRO_BLACKOUT = ENFORCED | DISABLED_BY_OPERATOR`, read by both telemetry and execution. If disabled, record it in the snapshot and remove the spec's FOMC stand-aside (L449) or state the exception.\n\n### F9 — Label corrections (text-only)\n\n\n- "$38.96B verified on-chain" → "Arkham-labelled balance, UNVERIFIED".\n- "$70.18B total balance sheet" → "848,000 BTC at USD spot (not balance-sheet total)".\n- "+14.29%" → "+14.29 IV points (+37.67% relative)".\n\n---\n\n## 6. Spec replacements (exact text)\n\n\n**S1 — line 53** (replace the stress formula with the line 296 form):\n\n```\nStressed Equity = Current Equity − Σ(Risk_i × 1.25 + 2.00) ≥ 4,795.00 USD\n```\n\n**S2 — Capacity table:** max slots = ⌊(Equity − 4,795) / (Risk × 1.25 + 2.00)⌋, clipped to [0, 4]. Four slots at $15 require Equity ≥ 4,878.00.\n
**S3 — Freshness:** closed-bar age ≤ 2 × 15 min for crypto; TradFi outside session = `CLOSED`, never `DATA_OK`.\n
**S4 — Spread gate:** one definition, `(ask − bid)/mid × 1e4`, quote age ≤ 5 s; CRYPTO ≤ 25 bps, TRADFI ≤ 5 bps; missing = fail.\n
**S5 — ATR buffer:** pick one value (0.35 at L311 or 0.50 at L247) and delete the other.\n
**S6 — Stage 3A/3B:** either write the stages into the spec or delete the references. Currently neither exists in the spec.\n\n---\n\n## 7. Open decisions (user)\n\n\n1. Macro blackout: enforced, disabled by operator, or removed (AGENTS.md says "permanently removed").\n2. Whether the 1-hour FOMC stand-aside applies while the telemetry blackout is disabled.\n3. Whether the spread gates (25/5 bps) stand, given 9/14 crypto and 3/10 TradFi fail on the snapshot values.\n4. Source of truth for spread: snapshot mid-based (recommended) or workbook ask-based with live override.\n5. Rotate the `sk-gemini` credential.\n6. Whether to rebuild the workbook from the pipeline or keep the current committed file.\n\n---\n\n## 8. Not done / limits\n\n\n- Fixes are written and unit-tested in isolation (21/21). They are **not applied to `main`**. No pipeline run was executed (no MT5 / live feeds in this sandbox).\n- Hyperdash "50 verified", the 16.89 s latency, and the Arkham "verified on-chain" claim remain unverified.\n- Remote state (`origin/main` beyond `cf62dc9`) could not be fetched; the audit is against the local `main` blob.\n- Session note: no instruction to commit or push was given this cycle.\n\n```\n
## `Cycle_200_fixes/__init__.py`

```python\n```\n\n(Empty file, 0 bytes.)\n\n## Cycle_200_fixes/fail_closed.py\n\n\n```\n"""Cycle 200 drop-in: fail-closed numeric parsing and spread/capacity/freshness gates.

Nothing here is wired into main. Each function is pure and unit-tested in
test_cycle200_fixes.py. Conventions:
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
    return 0.0 <= (now - last) <= bars_allowed * bar_s\n```\n\n## Cycle_200_fixes/atomic_xlsx.py\n\n\n```\n"""Cycle 200 drop-in: atomic workbook save, row-count guard, Excel-equivalent formula cache.

Not wired into main. Tested in test_cycle200_fixes.py.
"""
from __future__ import annotations

import os
import re
import shutil
from pathlib import Path

try:
    from .fail_closed import NA, num
except ImportError:  # run as plain script / tests
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
    with open(tmp, "rb") as fh:
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
    Note: this REPLACES the formula. If the live formula must survive, write the
    value to a new column instead (openpyxl cannot store a cached value with a formula).
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
    return out\n```\n\n## Cycle_200_fixes/test_cycle200_fixes.py\n\n\n```\nimport math
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(__file__))

import pytest  # noqa: E402
import openpyxl  # noqa: E402

from fail_closed import (  # noqa: E402
    NA, num, cell, spread_bps, spread_gate, stressed_equity, admissible,
    max_slots, four_slot_threshold, bar_fresh,
)
from atomic_xlsx import atomic_save, check_minimums, cache_sum_formulas  # noqa: E402


# ---------------- numeric parsing: no fake defaults
@pytest.mark.parametrize("v", [None, "", "-", "nan", "inf", "abc", True, float("nan")])
def test_num_rejects_unknown(v):
    assert num(v) is None


def test_num_accepts_numbers_and_thousands_separators():
    assert num("1,234.5") == 1234.5
    assert num(0) == 0.0          # real zero is kept, not confused with missing
    assert num("0") == 0.0


def test_cell_renders_na_not_zero():
    assert cell(None) == NA
    assert cell("-") == NA
    assert cell(1.23456, "{:.2f}") == 1.23


# ---------------- spread: one definition, fail closed
def test_spread_matches_live_btc_snapshot():
    # live snapshot BTC: bid 81722, ask 81738, spread_bps 1.96
    assert round(spread_bps(81722.0, 81738.0, 0.1), 2) == 1.96


def test_spread_invalid_or_stale_is_none():
    assert spread_bps(None, 81738.0, 0.1) is None
    assert spread_bps(81738.0, 81722.0, 0.1) is None       # crossed
    assert spread_bps(81722.0, 81738.0, 6.0) is None        # stale > 5 s
    assert spread_bps(0.0, 1.0, 0.1) is None                # non-positive bid


def test_spread_gate_limits_and_fail_closed():
    assert spread_gate(25.0, "CRYPTO") is True
    assert spread_gate(25.06, "CRYPTO") is False            # live SOL fails
    assert spread_gate(23.17, "CRYPTO") is True             # live XRP passes
    assert spread_gate(5.0, "TRADFI") is True
    assert spread_gate(6.76, "TRADFI") is False             # live EURUSD fails
    assert spread_gate(None, "CRYPTO") is False             # missing never passes
    assert spread_gate(0.0, "UNKNOWN") is False             # unknown category


# ---------------- capacity: arithmetic from Cycle 200 remediation, verified
def test_stressed_equity_formula():
    assert stressed_equity(4863.74, [25.0, 25.0]) == pytest.approx(4797.24)
    assert stressed_equity(4863.74, []) == 4863.74
    assert stressed_equity(4863.74, [25.0, None]) is None


def test_max_slots_matches_remediation_claims():
    assert max_slots(4863.74, 25.0) == 2     # floor(68.74/33.25)
    assert max_slots(4863.74, 15.0) == 3     # floor(68.74/20.75)


def test_four_slot_threshold_is_4878_at_15_usd():
    assert four_slot_threshold(15.0) == pytest.approx(4878.0)
    assert max_slots(4878.0, 15.0) == 4
    assert max_slots(4877.99, 15.0) == 3


def test_max_slots_unknown_or_negative_is_zero():
    assert max_slots(None, 15.0) == 0
    assert max_slots(4700.0, 15.0) == 0
    assert max_slots(4863.74, 0.0) == 0


def test_admissible_fail_closed_on_unknown_open_risk():
    assert admissible(4863.74, [], 25.0) is True
    assert admissible(4863.74, [25.0], 25.0) is True        # 4830.49
    assert admissible(4863.74, [25.0, 25.0], 25.0) is False # 4763.99 < 4795
    assert admissible(4863.74, [None], 15.0) is False
    assert admissible(4863.74, [15.0] * 4, 15.0) is False   # 5th slot over cap


# ---------------- freshness
def test_bar_freshness_crypto():
    now = 1_000_000.0
    assert bar_fresh(now - 600, now) is True        # 10 min old, 15m bars
    assert bar_fresh(now - 2000, now) is False      # > 2 bars
    assert bar_fresh(None, now) is False
    assert bar_fresh(now - 60, now, session_open=False) is False


# ---------------- workbook: formula cache mirrors Excel
def _sheet():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws["F3"], ws["G3"], ws["H3"] = 1058753.36, 743422.24, 1077880.33
    ws["I3"] = "=F3+G3+H3"
    ws["F4"], ws["G4"], ws["H4"] = 1.0, None, 2.0          # blank -> 0
    ws["I4"] = "=F4+G4+H4"
    ws["F5"], ws["G5"], ws["H5"] = "-", 1.0, 2.0           # text -> N/A
    ws["I5"] = "=F5+G5+H5"
    ws["I6"] = "=SUM(F6:H6)"                               # unsupported -> skipped
    return wb, ws


def test_formula_cache_values_and_na():
    wb, ws = _sheet()
    stats = cache_sum_formulas(ws)
    assert ws["I3"].value == round(1058753.36 + 743422.24 + 1077880.33, 2)
    assert ws["I4"].value == 3.0
    assert ws["I5"].value == NA
    assert ws["I6"].value == "=SUM(F6:H6)"
    assert stats == {"cached": 2, "na": 1, "skipped": 1}


def test_atomic_save_and_backup_and_minimums():
    wb, _ = _sheet()
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "DataBase_Trading.xlsx")
        atomic_save(wb, p)
        assert os.path.exists(p) and not os.path.exists(p.replace(".xlsx", ".tmp.xlsx"))
        atomic_save(wb, p)
        assert os.path.exists(p.replace(".xlsx", ".bak.xlsx"))
    with pytest.raises(RuntimeError):
        check_minimums({"arkham": 0}, {"arkham": 50})
    check_minimums({"arkham": 138}, {"arkham": 50})   # passes\n```\n\n## Notes for the council\n\n\n- **Verification:** `/tmp/q199/venv/bin/python -m pytest -q Cycle_200_fixes/test_cycle200_fixes.py` → 21 passed. Run from the repo root.\n- **Python version:** the annotations `str | float` and `range | None` need Python 3.10 or newer.\n- **Not verified:** nothing has been run against the real pipeline or live MT5 and feed data.\n- **Commit:** `c90ad9b` on `arena/74cd2d1a-trading-2`. `main` is unchanged and nothing was pushed.\n