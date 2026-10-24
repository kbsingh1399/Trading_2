# Cycle 318 — Council Explanation

**Cutoff:** 2026-10-24 01:46:29 UTC (Saturday)
**Dispatch nonce:** `ab50c695-1f3c-4d92-bdac-ea6b9af73c53`
**Declared evidence commit:** `7a921cc4` (origin/main head; snapshot as_of 01:43:54 UTC, 155 s before cutoff)
**Ruling:** `CYCLE_318_COUNCIL_RULING.json` (`response_sha256` = sha256 of the file with that field set to `PENDING`)
**Authorization:** `DENIED_FAIL_CLOSED`

## 1. Verdict

Integrity verifies at the declared commit and capital passes. The BTC 0.06-lot geometry now clears the Tier 2 risk band (16.92 USD). It still fails on quote freshness, the calendar blackout, weekend venue closure and the missing broker receipt. Nothing is executable.

## 2. Provenance

- `verify_cycle_envelope.py` returns **ENVELOPE_INTEGRITY_VERIFIED**. Commit, tree, manifest (`e5b2814e`) and workbook (`4fd031f5`) all match at the declared commit. The commit was created at 01:45:58 UTC, before cutoff.
- The envelope's **market-clock claims are contradicted**. It declares `broker_clock_open`, `native_market_open` and `calendar_verified` all true. The declared snapshot says `CALENDAR_UNAVAILABLE`, `blackout_active: true`, `FAIL_CLOSED_BLOCKED`. The reference calendar is 29,489 s old. It is Saturday, so FX, indices and metals are closed.
- **Excel freshness is declared true but not verified.** The verifier reads the claim (verify_cycle_envelope.py:232) and never tests age. The independent audit (21:42:14 UTC) is 14,655 s old, against a 900 s ceiling. The verifier gap is still open (DIS-318-03).

## 3. The receipt

- The receipt straddles the cutoff. Observation is 2 s **before** cutoff (01:46:27), but the tick it relies on is 2 s **after** (01:46:31). The order_check ran at a post-cutoff tick, so it is not admissible.
- Candidate: **BTC SELL LIMIT 80,960, SL 81,242, TP 80,252, 0.06 lot.** Risk 16.92 USD, reward 42.48, R:R 2.511, spread 0.90, stress 24.28 (the spread-inclusive model, reproduced exactly).
- Margin reconciles (free 2,436.27 = 4,865.07 − 2,428.80), and the self-hash matches. Neither makes the receipt admissible.

## 4. Hard gates at 01:46:29 UTC

| Gate | Result |
|---|---|
| Legal account | PASS (flat, 5064568) |
| Quote (15 s) | **FAIL**: BTC 158.9 s, SOL 158.6 s, ETH 157.8 s |
| Depth (180 s) | PASS for BTC this cycle (158.4 s). Sampling-dependent |
| Liquidation map (900 s) | PASS (~354 s) |
| Calendar / blackout | **FAIL**: `FAIL_CLOSED_BLOCKED`. Envelope claim contradicted |
| Broker session | **UNKNOWN** (no admissible broker-time receipt) |
| Native venue | **FAIL** for FX, indices, metals (Saturday). Crypto open |
| Rollover embargo | Clear |
| Tier 2 risk band (15–25 USD) | **PASS**: 16.92 USD |
| Excel freshness | **NOT VERIFIED** (audit 14,655 s old) |
| Broker feasibility / order_check | **UNKNOWN** (receipt tick post-cutoff) |
| Joint solvency (≥ 4,795) | PASS (BTC alone 4,838.79) |
| Contingent capacity | PASS (2 of 2 slots) |

## 5. Discovery across the four personas

- **Regime/calibration:** BTC, SOL and ETH are BEARISH. Probability evidence is still 11/17 account-wide and uncalibrated.
- **Fill/microstructure:** BTC has risen to 80,727 (from 80,639 at 01:13). The 80,960 entry is 233 pts above. The driftless bound is ≤ 0.18, heuristic. The VAH has moved to 81,826.32, and the stop sits 584 pts below it. Book imbalance (−0.02) and the pullback direction (LONG) are both quarantined, as they flipped across commits.
- **Solvency/portfolio:** BTC 0.06 lot leaves 4,838.79 post-stress, a 43.79 cushion. The sovereign illustration is unchanged.
- **Market-clock/provenance:** Crypto is open. FX, indices and metals are closed. The calendar blackout cannot be cleared, and the envelope's clock claims are contradicted.

## 6. Hurdle arithmetic

- **BTC:** driftless P_TP = 282/990 = **0.2849**. Break-even with the 0.90 spread is 17.82/59.40 = **0.3000**, so +1.5 pp of edge is needed. TP sits 7.05 σ_5min away (~4.1 h), against a 900 s TTL.

## 7. Universe

156 symbols declared. Forex 60, Cryptos 53, Cryptos_Raw 5, Indices 16, Commodities_Raw 14, Commodities 8. 24 assets carry row-level evidence, and none passes the 15 s quote gate. **0 of 156 executable.**

## 8. What would change the verdict

1. A preflight run on the trading host, inside the window, bound to nonce `ab50c695`, producing `order_calc_profit`, `order_calc_margin` and `order_check`.
2. A signed calendar that clears the blackout.
3. A cutoff-time Excel audit within 900 s.
4. Calibrated P_fill and P_TP (n ≥ 100, time-blocked OOS).
