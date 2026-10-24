# Cycle 315 — Council Explanation

**Cutoff:** 2026-10-24 00:38:47 UTC (Saturday)
**Dispatch nonce:** `443f36be-72ac-43d3-a78d-efac412a162d`
**Declared evidence commit:** `382d1074` (snapshot as_of 00:34:00 UTC, 287 s before cutoff)
**Ruling:** `CYCLE_315_COUNCIL_RULING.json` (`response_sha256` = sha256 of the file with that field set to `PENDING`)
**Authorization:** `DENIED_FAIL_CLOSED`

## 1. Verdict

Integrity verifies at the declared commit and capital passes, with a thinner joint cushion. No row is executable. Quote freshness is about 290 s against a 15 s gate. The pipeline calendar still asserts a fail-closed blackout, the venue is closed for Saturday, and there is no order_check.

## 2. Provenance

- `verify_cycle_envelope.py` returns **ENVELOPE_INTEGRITY_VERIFIED** (exit 0). Commit, tree, risk policy, the manifest at the declared commit (`4086741b`) and the workbook (`e855a87f`) all match.
- Open gates, not provenance failures: the manifest working copy differs, and `excel_freshness_verified` is null.
- **A newer commit exists but is not attested.** `df8e0b1` (as_of 00:38:43, 4 s before cutoff) has manifest `876f8def` and tree `0630e355`. Neither matches the envelope, so it is excluded. This matters: had the dispatcher pinned `df8e0b1`, BTC's tick would have been about 8 s old at cutoff and could have passed the 15 s gate. The pin decides admissibility (DIS-315-01, UNK-315-08).

## 3. The embedded receipt is not admissible

The "PREFLIGHT_PASS" receipt fails on timing. Its observation is 00:38:55, 8 s after the cutoff, and its tick is 00:39:00, 13 s after. Its self-hash is internally consistent, which proves nothing about provenance. It is not a `Terminal/execution_preflight.py` output, and its clock skew (−5.31 s) and margin figures are not reconciled.

It also changes the stress model to include the exit spread: `(base_loss + spread) × 1.25 + 2.00`. I adopted that model as the conservative basis for both candidates.

## 4. Hard gates at 00:38:47 UTC

| Gate | Result |
|---|---|
| Legal account | PASS (5064568, flat, matches snapshot) |
| Quote (15 s) | **FAIL**: BTC 291.7 s, SOL 288.9 s, ETH 289.6 s |
| Depth (180 s) | **FAIL**: BTC 291.4 s. This cycle's failure contrasts with 314's PASS at 83 s. That is sampling dependence, not data quality |
| Liquidation map (900 s) | PASS (~507 s) |
| Calendar / blackout | **FAIL**: `CALENDAR_UNAVAILABLE`, `blackout_active: true`, `FAIL_CLOSED_BLOCKED`. Calendar 25,427 s stale |
| Broker session | **UNKNOWN** (`broker_clock_open = null`) |
| Native venue | **FAIL** for FX, indices, metals (Saturday). Crypto is open 24/7 |
| Rollover embargo | Clear |
| Broker feasibility / order_check | **UNKNOWN** |
| Joint solvency (≥ 4,795) | PASS: 4,801.07 with the spread-inclusive stress |
| Contingent capacity | PASS (2 of 2 slots) |

## 5. Discovery across the four personas

- **Regime/calibration:** BTC, SOL and ETH are all BEARISH at the declared commit. The only probability evidence is 11/17 account-wide, uncalibrated. No setup clears n ≥ 100.
- **Fill/microstructure:** Book imbalance flips sign across commits (+0.66 at `382d1074`, −0.69 at `254b7f3`), so it stays quarantined. BTC's pullback classifier also flipped, from SHORT to LONG. The 81,300 entry is 659 pts (+0.82%) above the declared mid. The driftless fill bound is about 0.015%, heuristic.
- **Solvency/portfolio:** Joint BTC+SOL post-stress equity is 4,801.07, a 6.07 cushion. It was 12.57 in Cycle 314, and the drop is entirely the spread-inclusive stress. The sovereign 1.57 illustration is unchanged.
- **Market-clock/provenance:** Crypto is open. FX, indices and metals are closed. The calendar blackout cannot be cleared.

## 6. Hurdle arithmetic

- **BTC:** driftless P_TP = 480/1,930 = 0.2487. With the 0.60 spread, break-even is 0.2565, so +0.78 pp of edge is needed.
- **SOL:** driftless P_TP = 110/420 = 0.2619. With the 4.60 spread, break-even is 0.3167, so +5.48 pp is needed.

## 7. Universe coverage

156 symbols declared and verified. The universe file is identical to `f73a6513`. 24 assets carry row-level evidence. None passes the 15 s quote gate at cutoff. **0 of 156 executable.**

## 8. What would change the verdict

1. A dispatch pinned to the latest pre-cutoff commit with a matching manifest (`df8e0b1` or later). Its freshness must be checked.
2. A preflight run on the trading host, inside the window, bound to nonce `443f36be`, producing `order_calc_profit`, `order_calc_margin` and `order_check`.
3. A signed calendar that clears the blackout.
4. Calibrated P_fill and P_TP (n ≥ 100, time-blocked OOS). Until then EV, LCB and Utility stay null and every row stays HOLD.
