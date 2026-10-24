# Cycle 319 — Council Explanation

**Cutoff:** 2026-10-24 02:02:22 UTC (Saturday)
**Dispatch nonce:** `fc2770f4-dec3-49fa-9d08-c9bbea4b10c8`
**Declared evidence commit:** `5d49653` (02:02:20 UTC, on origin/main)
**Freeze commit:** `de96941` (02:02:22 UTC, changes only `Data/cycle_envelope.json`)
**Ruling:** `CYCLE_319_COUNCIL_RULING.json` (`response_sha256` `896d7cd4…`)
**Authorization:** `DENIED_FAIL_CLOSED`

## 1. Verdict

The envelope is valid as an artifact. The BTC 0.06 geometry sizes correctly, clears the Tier 2 band (16.92 USD), and survives the joint stress test (4,838.72 vs. the 4,795 kernel). It still fails on calendar, depth and quote freshness, orderflow authorization and receipt causality. All six rows are HOLD, and nothing is executable.

## 2. Provenance

- `verify_cycle_envelope.py` returns **ENVELOPE_INTEGRITY_VERIFIED** (exit 0). Commit, tree, risk policy, manifest (`bcf503b3`) and workbook (`4fd031f5`) all match at `5d49653`.
- The envelope in the prompt is byte-equal to `Data/cycle_envelope.json` at `de96941`, and the committed receipt equals the embedded receipt.
- **Open gates:** working-copy manifest (`15fc034c`) and workbook (`e855a87f`) do not match the declared digests. Both FAIL, as in Cycles 314–318.
- **Market-clock claims are contradicted.** The envelope claims `calendar_verified: true` and `native_market_open: true`. The live calendar reports `CALENDAR_UNAVAILABLE`, `blackout_active: true`, `FAIL_CLOSED_BLOCKED`.
- **Excel freshness is genuinely true this cycle.** The audit is 02:01:54 UTC, 28 s before cutoff (31/33 fresh, 0 formula errors). The verifier gap (`verify_cycle_envelope.py:232`) is still latent, and it did not change this verdict.

## 3. The receipt

- Observed 02:02:04 UTC, 18 s before cutoff. Tick 02:02:10 UTC, 12 s before cutoff.
- The self-hash reproduces (`41040be6…`), and the committed receipt equals the embedded one.
- **Not admissible.** The tick is stamped 6 s after the moment the receipt says it was observed (clock skew −5.55 s). An order_check cannot be tied causally to an observation that predates the quote it used. The tick is pre-cutoff, so this is an ordering defect, not the post-cutoff defect of Cycle 318.
- The arithmetic reconciles (risk, reward, R:R, spread, stress, margin). Reconciliation does not make a receipt admissible.

## 4. Hard gates at 02:02:22 UTC

| Gate | Result |
|---|---|
| Legal account | PASS (5064568, flat) |
| Causal fresh evidence | **FAIL** (snapshot 204 s old; receipt inadmissible; layer 3 STALE; layer 7 UNAVAILABLE) |
| Broker session | **UNVERIFIED** (receipt not admissible; trade_mode FULL observed) |
| Native venue | PASS for BTC (crypto 24/7). FAIL for FX, indices, metals (Saturday) |
| Calendar / blackout | **FAIL** (`FAIL_CLOSED_BLOCKED`; repo calendar 30,442 s old) |
| FX rollover 21:15–22:30 | PASS (02:02 UTC is outside the window) |
| Broker feasibility / order_check | **UNKNOWN** (retcode 0 reported, not causally admissible) |
| Structural stop | **UNPROVEN** (see §6) |
| Contingent capacity (2) | PASS (1 candidate, 0 existing) |
| Joint solvency ≥ 4,795 | PASS (4,838.72; cushion 43.72) |
| Quote, 15 s | **FAIL** (snapshot 204+ s; receipt 12 s, inadmissible) |
| Depth, 180 s | **FAIL** (≥ 204 s at cutoff) |
| Liquidation map, 900 s | PASS (≈450 s, not re-measured) |
| Excel freshness, 900 s | PASS (28 s) |
| Tier 2 risk band | PASS (16.92 USD) |
| Orderflow authorization | **FAIL** (`DENIED_UNVERIFIED_ORDERFLOW`; pioneer UNAVAILABLE) |
| Manifest / workbook working copy | **FAIL** |

## 5. Discovery across the four personas

- **Regime/calibration:** BTC is bearish. CVD is −3.10 M for the session and −3.05 M for 24 h, with a BEARISH_MOMENTUM divergence. Price sits below EMA 20/50/200 and below session VWAP (80,670). The probability evidence is n = 17 and uncalibrated, so this is a hypothesis, not an edge.
- **Fill/microstructure:** The sell limit at 81,000 is 195 pts above mid (0.86 ATR-14). No validated P_fill exists. Book imbalance and pullback direction are quarantined after repeated sign flips. The depth that would support a fill estimate is ≥ 204 s old.
- **Solvency/portfolio:** One ticket, 24.35 stressed, post-stop 4,838.72, kernel cushion 43.72, hard-floor cushion 238.72, operating-buffer cushion 188.72. Single candidate within the 2-ticket limit. The 4,863.07 figure in the envelope is the no-candidate baseline and is not the candidate's post-stop balance.
- **Market-clock/provenance:** Saturday. Crypto is open, FX/indices/metals are closed (watchlist-only). The calendar is blocked. The freeze commit landed at the cutoff second (see DIS-319-05).

## 6. Structure, stop and hurdle arithmetic

- **Stop:** SL 81,282 is 282 pts above the entry, 544 pts below VAH 81,826.32, and 65.5 pts below VAL 81,347.52. It sits inside the value area and is not anchored to a documented structural high. The stop is 1.24 ATR-14. Structural validity is UNPROVEN.
- **Hurdle:** Driftless P_TP = 282 / 990 = **0.2849**. Break-even = 17.88 / 59.40 = **0.3010**, where Loss_net = 16.92 + 0.96 and Gain_net = 42.48 − 0.96. The shortfall is **1.6 pp**. P_TP is uncalibrated, so this is not an edge claim.

## 7. Universe

156 symbols declared (sha `4d023fe8…`, identical at `5d49653`). 24 assets carry row-level evidence. The only in-window receipt is BTC, which is inadmissible. **0 of 156 pass the 15 s quote gate. 0 executable.**

## 8. Disputes

DIS-319-01 receipt causality (tick after observation). DIS-319-02 envelope clock claims contradicted. DIS-319-03 snapshot depth and quote ages at cutoff. DIS-319-04 orderflow unverified. DIS-319-05 freeze commit at the cutoff second. DIS-319-06 prompt digest drift (working copy `8dae957f`, committed `2b436bee` template). DIS-319-07 working-copy digests. DIS-319-08 unproven structural stop. DIS-319-09 verifier gap, latent this cycle. DIS-319-10 Cycle 318 response hash not reproducible from the saved file.

## 9. What would change the verdict

1. An admissible receipt. The tick must be at or before observed_at, and both before cutoff, with order_calc_profit, order_calc_margin and order_check bound to nonce `fc2770f4`.
2. A verified calendar that clears the blackout, with provenance.
3. BTC depth ≤ 180 s and quote ≤ 15 s at cutoff.
4. Verified broker session for BTCUSD.pi.
5. A documented structural invalidation above the entry.
6. Calibrated P_fill and P_TP (n ≥ 100, time-blocked out-of-sample), with P_TP clearing 0.3010.
7. Working-copy manifest and workbook digests matching the declared commit.
