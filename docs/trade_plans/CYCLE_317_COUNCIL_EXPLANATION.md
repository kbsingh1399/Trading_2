# Cycle 317 — Council Explanation

**Cutoff:** 2026-10-24 01:15:13 UTC (Saturday)
**Dispatch nonce:** `a2fc999c-a416-4437-958f-0fb2d9391255`
**Declared evidence commit:** `8ffb37a3` (snapshot as_of 01:13:53 UTC, 80 s before cutoff)
**Ruling:** `CYCLE_317_COUNCIL_RULING.json` (`response_sha256` = sha256 of the file with that field set to `PENDING`)
**Authorization:** `DENIED_FAIL_CLOSED`

## 1. Verdict

Integrity verifies at the declared commit and capital passes. No row is executable. The BTC receipt geometry also fails the Tier 2 risk band. Quotes are about 84 s old against a 15 s gate, and the calendar blackout is still asserted.

## 2. Provenance

- `verify_cycle_envelope.py` returns **ENVELOPE_INTEGRITY_VERIFIED**. Commit, tree, manifest (`c19f32be`) and workbook (`d4cd52fb`, which has changed from `e855a87f`) all match at the declared commit.
- The envelope's **market-clock claims are contradicted**. It declares `broker_clock_open`, `native_market_open` and `calendar_verified` all true. The declared-commit snapshot says `CALENDAR_UNAVAILABLE` with `blackout_active: true`, `FAIL_CLOSED_BLOCKED`. The reference calendar is 27,613 s old. It is Saturday, so FX, indices and metals are closed.
- **Excel freshness is declared true but not verified.** The verifier's gate reads the envelope's claim and never tests audit age. The independent audit (21:42:14 UTC) is 12,779 s old, far outside the 900 s ceiling. I flag this as a verifier gap (DIS-317-03).

## 3. The receipt

- The self-hash matches, but the receipt is **post-cutoff**: observed 01:15:26 (+13 s), tick 01:15:31 (+18 s).
- The candidate is **BTC SELL LIMIT 80,960, SL 81,242, TP 80,252, 0.03 lot**. Risk is 8.46 USD (8.91 with spread), **below the 15.00 USD Tier 2 minimum**. Stress is 13.14 by the spread-inclusive model, which I reproduce exactly.
- The margin reconciles this time (margin_free 3,650.67 = 4,865.07 − 1,214.40). That is the first receipt in this sequence where it does. It does not make the receipt admissible.

## 4. Hard gates at 01:15:13 UTC

| Gate | Result |
|---|---|
| Legal account | PASS (flat, 5064568) |
| Quote (15 s) | **FAIL**: BTC 84.3 s, SOL 81.8 s, ETH 83.7 s |
| Depth (180 s) | PASS for BTC this cycle (83.0 s). Sampling-dependent |
| Liquidation map (900 s) | PASS (~304 s) |
| Calendar / blackout | **FAIL**: `FAIL_CLOSED_BLOCKED`. Envelope claim contradicted |
| Broker session | **UNKNOWN** (no broker-time receipt; no order_check) |
| Native venue | **FAIL** for FX, indices, metals (Saturday). Crypto open |
| Rollover embargo | Clear |
| Tier 2 risk band (15–25 USD) | **FAIL**: BTC receipt 8.46 USD |
| Joint solvency (≥ 4,795) | PASS (BTC alone 4,849.93) |
| Contingent capacity | PASS (2 of 2 slots) |

## 5. Discovery across the four personas

- **Regime/calibration:** BTC, SOL and ETH are BEARISH. Probability evidence is still 11/17 account-wide and uncalibrated.
- **Fill/microstructure:** Price has recovered from 80,596 (00:39) to about 80,640 (01:13). The 80,960 entry is 320.5 pts above the declared mid. The driftless fill bound is ≤ 0.066, heuristic, so fill odds are better than in Cycles 314–315 but still uncalibrated. Book imbalance (−0.91) is noise.
- **Solvency/portfolio:** BTC 0.03 lot leaves 4,849.93 post-stress, a 54.93 cushion. The 1.57 sovereign illustration is unchanged.
- **Market-clock/provenance:** Crypto is open. FX, indices and metals are closed. The calendar blackout cannot be cleared, and the envelope's clock claims are contradicted.

## 6. Hurdle arithmetic

- **BTC:** driftless P_TP = 282/990 = **0.2849**. Break-even with the 0.45 spread is 8.91/29.70 = **0.3000**, so +1.5 pp of edge is needed. TP sits 7.05 σ_5min away (~4.1 h), against a 900 s TTL.

## 7. Universe

156 symbols declared. Forex 60, Cryptos 53, Cryptos_Raw 5, Indices 16, Commodities_Raw 14, Commodities 8. 24 assets have row-level evidence, and none passes the 15 s quote gate. **0 of 156 executable.**

## 8. What would change the verdict

1. A preflight run on the trading host, inside the window, bound to nonce `a2fc999c`, producing `order_calc_profit`, `order_calc_margin` and `order_check`.
2. A signed calendar with valid event provenance that clears the blackout.
3. A stop/TP geometry that meets the 15–25 USD band at a legal lot size.
4. A cutoff-time Excel audit within 900 s.
5. Calibrated P_fill and P_TP (n ≥ 100, time-blocked OOS).
