# Cycle 314 — Council Explanation

**Cutoff:** 2026-10-24 00:15:12 UTC (Saturday)
**Dispatch nonce:** `2faf3bab-8760-409f-8ee7-093f4834ddb6`
**Evidence commit:** `254b7f39` (origin/main, snapshot as_of 00:13:53 UTC, 79 s before cutoff)
**Ruling:** `CYCLE_314_COUNCIL_RULING.json` (42,258 bytes; `response_sha256` = sha256 of the file with that field set to `PENDING`)
**Authorization:** `DENIED_FAIL_CLOSED`

## 1. Verdict in one line

Integrity verifies and capital passes (4,807.57 joint post-stress, 12.57 cushion). No row is executable, because the quote gate, the calendar blackout, the broker session, the weekend venue closure and the order_check all fail or are unknown.

## 2. Provenance

- `verify_cycle_envelope.py` returns **ENVELOPE_INTEGRITY_VERIFIED** (exit 0). Commit, tree, risk policy, workbook (`e855a87f`, byte-identical at commit and on disk) and the manifest at the declared commit (`60dd9731`) all match.
- Open gates, not provenance failures: manifest working copy differs (gate FAIL), and `excel_freshness_verified` is null.
- Commit `254b7f39` is 79 s before cutoff. The 00:18:53 snapshot (`bc11f09`) is post-cutoff and excluded.

## 3. The embedded PREFLIGHT_PASS receipt is not admissible

The prompt carries a "verified" `execution_preflight_receipt.json` with `PREFLIGHT_PASS`. It fails on four independent grounds:

1. **Post-cutoff.** `observed_at` is 00:19:11, 239 s after the 00:15:12 cutoff. The tick is 00:19:17.
2. **Self-contradictory freshness.** `tick_age_seconds = -5.82` (tick after observation) while `quote_fresh = true`.
3. **Unit and margin inconsistencies.** `spread_raw` is in price units but labelled as if in points. Margin required (1,626) and unchanged free margin (4,865.07) are not reconciled.
4. **Not from our tool.** The receipt body is hash-consistent (`sort_keys, indent=2`), which proves only internal consistency. It is not a `Terminal/execution_preflight.py` output, and no broker artifact backs it.

The receipt is therefore recorded as evidence that a preflight *was attempted* after the window, and it cannot authorize anything.

## 4. Hard gates at 00:15:12 UTC

| Gate | Result |
|---|---|
| Legal account | PASS (5064568, flat, matches snapshot to the cent) |
| Quote freshness (15 s) | **FAIL**: BTC ~83 s, SOL ~82 s, ETH ~80 s |
| Depth (180 s) | PASS for BTC this cycle (83 s). Sampling-dependent; not a data-quality claim |
| Liquidation map (900 s) | PASS (BTC ~282 s) |
| Calendar / blackout | **FAIL**: snapshot `macro_calendar` = `CALENDAR_UNAVAILABLE`, `blackout_active: true`, `FAIL_CLOSED_BLOCKED` ("event provenance/window invalid"). The envelope-referenced calendar is 24,012 s old |
| Broker session | **UNKNOWN** (`broker_clock_open = null`) |
| Native venue | **FAIL** for FX, indices, metals (Saturday; weekend embargo Fri 21:55 to Sun 22:00 UTC). Crypto 24/7 open |
| Rollover embargo 21:15–22:30 UTC | Clear (not active at cutoff) |
| Broker feasibility / order_check | **UNKNOWN** (no receipt bound to nonce 2faf3bab) |
| Structural stop | Analysable, not broker-validated |
| Joint solvency (≥ 4,795) | PASS (4,807.57 for BTC+SOL) |
| Contingent capacity | PASS (2 of 2 slots, envelope governs over snapshot's 4) |

## 5. Discovery across all four personas

- **Regime/calibration:** BTC, ETH and SOL are all BEARISH (EMA200 slope −0.11% to −0.17% per 3 h). The only probability evidence is 11/17 account-wide, uncalibrated (n < 100). No setup can produce an admissible EV or LCB.
- **Fill/microstructure:** Book imbalance flips sign between generations, so it is quarantined (DIS-314-02). BTC price fell from 81,069 (23:58:53) to 80,906.5 (00:13:53) to 80,769.5 (00:19:17). The 81,300 SELL LIMIT is now **530 pts (0.66%) above the market**. A driftless reflection bound on the 5-minute sigma (100.36) gives roughly a 0.2% chance of touching within the 900 s TTL. That is heuristic, not calibrated, but it shows the candidate is now a deep rally-fade, not a pullback fill.
- **Solvency/portfolio:** The kernel binds at 4,795. Post-stress BTC 4,837.07, SOL 4,833.57, joint 4,807.57. Two slots, no atomic OCO, correlated crypto-beta shorts joint-stressed.
- **Market-clock/provenance:** Crypto is open; FX, indices and metals are closed on Saturday. The pipeline calendar asserts a blackout and cannot clear it.

## 6. Hurdle arithmetic (unchanged geometry, updated spread)

- **BTC** driftless P_TP = 480/1,930 = **0.2487**. With the 0.60 USD exit spread, break-even is 19.80/77.20 = **0.2565**, so +0.78 pp of genuine edge is needed before commission.
- **SOL** driftless P_TP = 110/420 = **0.2619**. With the 4.60 USD spread, break-even is **0.3167**, so +5.48 pp is needed. That is 7× the BTC requirement.

## 7. Full-universe coverage

- 156 symbols declared and verified (file digest identical to `f73a6513`): Forex 60, Cryptos 53, Cryptos_Raw 5, Indices 16, Commodities_Raw 14, Commodities 8.
- 24 assets carry row-level evidence. 14 crypto CFDs are fresh at generation but over the 15 s gate at cutoff. Ten TradFi and metals assets are stale at 11,600 to 15,300 s with weekend-closed venues.
- **0 of 156 executable.**

## 8. Disputes raised this cycle

- **DIS-314-01 (sev 3):** The receipt is post-cutoff, so it is excluded as future evidence.
- **DIS-314-03 (sev 3):** The pipeline's calendar now asserts a fail-closed blackout. Cycle 313 recorded only staleness.
- **DIS-314-11 (sev 2):** BTC structure has drifted; the candidate is now a deep rally-fade.
- Others (DIS-314-02, 04–10) are carried or note-only.

## 9. What would change the verdict

1. A preflight run on the trading host, inside the cutoff window, bound to nonce `2faf3bab` (`Terminal/execution_preflight.py`), producing `order_calc_profit`, `order_calc_margin` and `order_check`.
2. A signed calendar with valid event provenance that clears the blackout.
3. A weekend-appropriate swap/commission table for BTC/SOL (UNK-314-05).
4. Calibrated `P_fill`/`P_TP` (n ≥ 100, time-blocked OOS). Until then, EV, LCB and Utility stay null and every row stays HOLD.

Even with all four, the structural case for the current BTC/SOL geometry is weaker than in Cycle 313. The entry is now far from market and the needed edge has not been shown.
