# Arena.ai — 24-Asset Dual-Model Ruling (Model 2 Trend Pullback / Model 1 Extreme Mean-Reversion)

**Briefing under review:** Antigravity x Arena.ai Live Strategy Council, 2026-10-08 13:28:13 UTC
**Machine receipt used:** `origin/arena/83d03e3f-trading-2` → commit `a61284b`, `docs/telemetry/live_snapshot_latest.json`, `as_of_utc = 2026-10-08 13:28:18 UTC`
**Wall-persistence window:** 45 consecutive one-minute telemetry commits, 12:59:19 → 13:43:18 UTC
**Desk state (as of receipt):** Balance/Equity 4,813.99 USD | Margin used 0.00 | 0 positions | 0 pending orders
**Floor defense:** Hard floor 4,775.00 | Operating threshold 4,795.00 | Cushion +38.99 | Headroom above threshold +18.99
**Risk capacity:** exactly 1 slot | admissible nominal risk 10.00–11.04 USD | stressed loss 14.50–15.80 USD | worst-case post-trade equity ≥ 4,798.19
**Ruling author:** Arena.ai (cloud council, read-only; no broker I/O, no order placed, changed or cancelled)

---

## 0. VERDICT

```
VERDICT: PUNCH NONE / DEFENSIVE HOLD
```

**No asset across all 24 passes all five gates under either model at the 13:28:18 UTC receipt.** Nothing is staged, nothing is modified. The two closest candidates — **BCH (Model 2 short at VWAP)** and **SOL (Model 1 oversold long at the −2σ band)** — are published below with their exact missing confirmations and trigger levels so the desk can act the moment the gates close.

Two structural facts dominate this scan:

1. **The orderflow-locating gates (G3/G4) are unavailable for 10 of 24 assets.** The 10 non-crypto names (GOLD, SILVER, USWTI, EURUSD, GBPUSD, USDJPY, SP500, NAS100, DJ30, GER40) are `UNAVAILABLE_L1_ONLY`: no exchange L2, no taker CVD. Tight CFD spreads (0.06–6.09 bps) are **not** a substitute. They fail closed.
2. **All 14 crypto assets fail G4 as defined in this repository.** Feeding the 45 sampled books through the repo's own `Terminal/signals/wall_tracker.py` (≥150,000 USD, present in **every** sampled snapshot for ≥180 s, clustered at 10 bps around a moving mark) returns **zero qualifying entry walls for every asset**. A looser band test (any ≥150k level within ±0.25 ATR of the level in ≥3 consecutive samples) does find band presence for ADA (34 samples), SOL (9), BTC (4), NEAR (3) — but the SOL minute-by-minute timeline proves those "walls" migrate downward **with price** rather than absorb it, which is exactly why the strict, price-anchored definition governs. Band presence is not price-anchored persistence.

Additionally, the receipt self-declares `trade_authorization = DENIED_UNVERIFIED_ORDERFLOW`, and `structural_stop_clusters` / `reconstructed_liquidations` are `UNAVAILABLE` for every asset ("No verified exchange stop-order feed"; "Open interest cannot identify liquidation prices"). The briefing's `Long Flush / Short Squeeze / Discount Sweep / Premium Sweep = N/A` and `Verified Whales = 0` renderings are therefore consistent with the raw file: there are no verified cascade pools or wallet-attributed walls to trade toward.

**Section 3 review mandate:** there are no open positions to HOLD/ratchet/cut and no resting limit orders to KEEP/DELETE. The book is 100% cash flat.

---

## 1. GATE-1→5 EVIDENCE TABLE (machine receipt 13:28:18 UTC)

`M2 Δ to VWAP (ATR)` = signed distance (mid − session VWAP)/ATR(14); negative = mid below VWAP.
`M2 approach` = |distance| ≤ 0.75 × ATR (precondition for any staged pullback order).
`M1 z/rsi` = |Z| ≥ 2.0 **and** RSI < 30 (long) / RSI > 70 (short) simultaneously met.
`Persistent entry wall` = repo `PersistentWallTracker` result within ±0.25 ATR of the candidate entry.
`Size` = at least one lot step exists with SL ∈ [1.5, 2.5]×ATR and nominal risk ∈ [10.00, 11.04] USD.

| # | Asset (broker) | Spread bps | Regime | VWAP Z | RSI | Δ to VWAP (ATR) | M2 at approach? | M1 z/rsi met? | Persistent entry wall | Size 10–11.04 USD? | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | BTCUSD.pi | 1.94 | BEARISH | -1.31 | 41.8 | -1.40 | no (-1.40) | no | NONE | yes | FAIL |
| 2 | ETHUSD.pi | 13.02 | BEARISH | -1.37 | 34.4 | -2.10 | no (-2.10) | no | NONE | yes | FAIL |
| 3 | SOLUSD.p | 23.15 | BEARISH | -2.07 | 21.0 | -4.16 | no (-4.16) | **YES** | NONE (strict) | yes | **WATCH** |
| 4 | BNBUSD.p | 9.21 | BEARISH | -1.52 | 29.1 | -2.86 | no (-2.86) | no | NONE | yes | FAIL |
| 5 | XRPUSD.pi | 35.73 | BEARISH | -0.75 | 44.3 | -1.08 | no (-1.08) | no | NONE | yes | FAIL (G1 spread) |
| 6 | ADAUSD.p | 84.76 | BEARISH | -1.47 | 33.3 | -2.17 | no (-2.17) | no | NONE | **NO** | FAIL |
| 7 | DOGUSD.p | 241.80 | BEARISH | +0.20 | 36.0 | +0.50 | YES | no | NONE | yes | FAIL (G1 spread) |
| 8 | TRXUSD.p | 26.91 | RANGE_BOUND | -0.91 | 38.9 | -1.00 | no (-1.00) | no | NONE | yes | FAIL |
| 9 | DOTUSD.pi | 180.83 | BEARISH | +1.19 | 47.8 | +1.19 | no (+1.19) | no | NONE | yes | FAIL (G1 spread) |
| 10 | LNKUSD.p | 65.63 | BEARISH | -1.23 | 35.2 | -2.02 | no (-2.02) | no | NONE | yes | FAIL (G1 spread) |
| 11 | BCHUSD.p | 19.62 | BEARISH | -0.17 | 47.9 | **-0.25** | **YES** | no | NONE | yes | **WATCH** |
| 12 | LTCUSD.pi | 46.74 | BEARISH | -0.51 | 40.5 | -1.31 | no (-1.31) | no | NONE | yes | FAIL (G1 spread) |
| 13 | AVXUSD.p | 28.32 | BEARISH | -1.66 | 33.5 | -3.01 | no (-3.01) | no | NONE | yes | FAIL |
| 14 | NERUSD.p | 63.76 | BEARISH | -2.25 | 32.5 | -4.44 | no (-4.44) | no (RSI 32.5) | NONE | yes | FAIL |
| 15 | XAUUSD.pi | 0.17 | BEARISH | -0.42 | 53.1 | -0.38 | YES | no | n/a L1-only | NO | FAIL (no G3/G4 feed) |
| 16 | XAGUSD.pi | 6.09 | BEARISH | -0.54 | 50.2 | -1.44 | no (-1.44) | no | n/a L1-only | NO | FAIL (no G3/G4 feed) |
| 17 | USWTI.p | 5.38 | **BULLISH** | +0.56 | 53.3 | +2.06 | no (+2.06) | no | n/a L1-only | yes | FAIL (no G3/G4 feed) |
| 18 | EURUSD.pi | 0.09 | BEARISH | -0.30 | 51.2 | -0.25 | YES | no | n/a L1-only | yes | FAIL (no G3/G4 feed) |
| 19 | GBPUSD.pi | 0.15 | BEARISH | +0.55 | 56.5 | +0.56 | YES | no | n/a L1-only | yes | FAIL (no G3/G4 feed) |
| 20 | USDJPY.pi | 0.06 | **BULLISH** | +0.55 | 49.0 | +1.45 | no (+1.45) | no | n/a L1-only | NO | FAIL (no G3/G4 feed) |
| 21 | SP500.p | 0.39 | BEARISH | -0.12 | 53.4 | -0.26 | YES | no | n/a L1-only | yes | FAIL (no G3/G4 feed) |
| 22 | NAS100.p | 0.34 | BEARISH | -0.57 | 49.0 | -1.39 | no (-1.39) | no | n/a L1-only | NO | FAIL (no G3/G4 feed) |
| 23 | DJ30.p | 0.23 | BEARISH | +0.43 | 59.1 | +1.09 | no (+1.09) | no | n/a L1-only | yes | FAIL (no G3/G4 feed) |
| 24 | GER40.p | 0.32 | BEARISH | +0.18 | 56.4 | +0.38 | YES | no | n/a L1-only | yes | FAIL (no G3/G4 feed) |

Reproduction: `python scripts/arena_dual_model_scan.py --decision-utc "2026-10-08 13:28:20 UTC" --json-out artifacts/arena_dual_model_scan_20261008_1328.json`
The briefing's rendered tick and this receipt differ only by sub-minute quote drift (e.g. briefing BTC mid 82,367.0 / Z −1.29 vs receipt 82,360.0 / Z −1.31; briefing SOL spread 20.47 bps vs receipt 23.15 bps). VWAP and ATR match exactly, confirming the same 13:28 snapshot generation.

---

## 2. MODEL 2 — TREND-FOLLOWING PULLBACK: CLOSEST NAMES AND EXACT TRIGGERS

### 2.1 Only two assets are in a confirmed bullish regime — and both are structurally non-executable on this feed

| Asset | EMA200 slope (3h) | Price vs VWAP | Status |
|---|---|---|---|
| USWTI.p | **+0.2994 %** | +2.06 ATR above | `UNAVAILABLE_L1_ONLY` → no taker CVD, no L2 → G3/G4 cannot be evaluated. USWTI cannot pass these gates by approaching price; it needs an instrument-appropriate flow feed or an approved replacement policy. |
| USDJPY.pi | +0.0084 % | +1.45 ATR above | Same L1-only veto; pullback long would need 158.087 (VWAP) − but no flow confirmation available. |

A bullish-regime "buy the pullback" entry therefore **does not exist** for any executable name at this receipt.

### 2.2 Bearish-regime pullback shorts — ranked by distance to Session VWAP (the value shelf)

| Rank | Asset | VWAP (13:28) | Δ ATR | 0.75×ATR approach trigger | Spread | Sizing example (risk ≤ 11.04) | Blocking gates |
|---|---|---|---|---|---|---|---|
| 1 | **BCHUSD.p** | 295.8868 | **−0.25** (already in zone) | 295.89 ± 1.03 → **[294.86 – 296.91]** | 19.62 ✓ | 0.50 lots, SL 2.21 (1.62 ATR) → 11.04; or 0.40 lots, SL 2.76 (2.02 ATR) → 11.04 | **G3**: closed 5m/15m CVD is +0.023/+0.147 M USD (net buying — no seller rejection yet). **G4**: no persistent ask wall at VWAP. No completed bearish rejection OHLC at the shelf. |
| 2 | LTCUSD.pi | 64.5368 | −1.31 | rally to **64.339** | 46.74 ✗ | — | G1 spread toxic. |
| 3 | BTCUSD.pi | 82,761.34 | −1.40 | rally to **82,545.8** | 1.94 ✓ | 0.02 lots, SL 500–552 pts (1.74–1.92 ATR) → 10.00–11.04 | G2 not at approach; G4 unverifiable 1.4 ATR away (top-20 book spans ≈2 USD); CVD mixed (15m +30.0 M vs 5m −4.0 M, 60m −72.6 M). |
| 4 | XRPUSD.pi | 1.4072 | −1.08 | rally to **1.4019** | 35.73 ✗ | — | G1 spread toxic. |
| 5 | ADAUSD.p | 0.2516 | −2.17 | rally to **0.25025** | 84.76 ✗ | **none** (min 1 lot × 5,000 × 1.5 ATR = 13.50 > 11.04 cap) | G1, G4, and structurally un-sizeable at current ATR. |
| 6 | ETHUSD.pi | 2,555.97 | −2.10 | rally to **2,548.06** | 13.02 ✓ | 0.38–0.40 lots, SL 2.37–2.50 ATR → 10.01–10.56 | G2; G4 unverifiable (book span 0.2 USD); CVD still net selling. |
| 7 | LNKUSD.p | 13.0796 | −2.02 | rally to **13.0318** | 65.63 ✗ | — | G1. |
| 8 | BNBUSD.p | 766.2856 | −2.86 | rally to **764.57** | 9.21 ✓ | 1.75 lots @ 2.50 ATR → 10.00 | RSI 29.1 is the only near-extreme signature; no wall, no exhaustion; 1.75 lots = 1,306 USD margin (~27 % equity). |
| 9 | AVXUSD.p | 10.8421 | −3.01 | rally to **10.7804** | 28.32 ✗ | — | G1. |
| 10 | SOLUSD.p | 114.6754 | −4.16 | rally to **114.2488** | 23.15 ✓ (marginal) | 0.08–0.10 lots, SL 1.76–2.43 ATR | Over-extended *below* value: wrong side for a pullback short; belongs to Model 1 screen. |
| 11 | NERUSD.p | 5.3092 | −4.44 | rally to **5.2602** | 63.76 ✗ | — | G1. |

Non-crypto bearish regimes sit close to VWAP in *geometry* — EURUSD −0.25 ATR, SP500 −0.26, GER40 +0.38, DJ30 +1.09, GOLD −0.38 — but all are `UNAVAILABLE_L1_ONLY` (no taker CVD, no L2): **G3/G4 cannot be evaluated → fail closed.** Note DJ30 rallied **+2.17 ATR within the 15 minutes after this receipt** (50,943 → 51,074): any fade of that move without a completed rejection would have been run over — the reason the rejection-OHLC gate is not optional.

### 2.3 Exact Model 2 trigger conditions (apply to any name before staging)

A `SELL LIMIT` at the value/resistance shelf may be staged **only when all of the following hold simultaneously**:

1. **Approach:** price within 0.75 × then-current ATR of a freshly recomputed VWAP (or VAH / structural shelf).
2. **Completed rejection:** a *closed* 15M candle that trades into the shelf and closes back below it (for shorts), or a closed 15M candle that sweeps the shelf and closes back above it (for longs) — not a forming bar.
3. **Wall:** a ≥150,000 USD resting wall on the defending side within 0.25 ATR of the revalidated entry, present without interruption in ≥3 consecutive 60-second telemetry samples (repo `PersistentWallTracker` semantics). A wall that tracks price downward is not a wall.
4. **CVD flip:** closed 5m and 15m taker-CVD move to the trade's direction (negative for shorts / non-negative for longs) as price tests the shelf.
5. **Friction & sizing:** spread ≤ 25 bps; SL ≥ 1.5×ATR; **TP = 2.50R**; nominal risk ∈ [10.00, 11.04] USD; stressed post-loss equity ≥ 4,795.00 USD; and the entry must be re-verified against a live ATR/VWAP — the levels above are pinned to 13:28:18 and decay with every new receipt.

If any item is absent, **no stage command**.

---

## 3. MODEL 1 — EXTREME MEAN-REVERSION: CLOSEST NAMES AND MISSING CONFIRMATION

### 3.1 SOLUSD.p — the only asset that clears the numeric extreme thresholds (and it still fails closed)

| Field | Value (13:28:18 receipt) |
|---|---|
| Mid / Bid-Ask | 112.310 / 112.170–112.430 |
| Session VWAP / σ | 114.6754 / 1.1424 → **−2σ band = 112.3906** |
| VWAP Z-score | **−2.07 SD** ✓ (gate: ≤ −2.0) |
| RSI(14) | **21.03** ✓ (gate: < 30) |
| Spread | 23.15 bps ✓ (gate: < 25 bps) — only 1.85 bps of margin |
| ATR(14) | 0.5690 |
| 48h value area | POC 115.725 / VAH 119.30 / **VAL 114.10** — price is 4.16 ATR below VWAP and below the entire value area |
| CVD (closed buckets, forming 1m excluded) | 1m **+0.13 M**, 5m **−0.42 M**, 15m **+2.37 M**, 60m **−20.60 M** USD |
| Bid wall in ±0.25 ATR band of 112.39 | strict repo tracker: **NONE**; loose band test: present in 9 consecutive samples (≈540 s) up to **$568,665** |
| Sizing | 0.08–0.10 lots with SL 1.76–2.43 ATR ⇒ risk 10.00–11.04; 0.10 lots / SL 1.05 (1.85 ATR) ⇒ risk 10.50, stressed 15.13, post-trade 4,798.86 ≥ 4,795 ✓ |

**What is missing (all three must close before staging):**

1. **G4 price-anchored persistence** — the repo tracker (present in *every* sample, 10-bps clustering around a moving mark) finds no qualifying bid wall at the band. The looser ±band test that found 9/45 samples includes the migration effect: the largest single level at 13:28 was **$730,094 at 112.21**, and the same book had migrated to 111.4–111.6 within 15 minutes.
2. **G3 aggressor exhaustion** — the closed 5-minute CVD is still **negative (−0.42 M USD)**. The 15m positive reading (+2.37 M) is suggestive absorption, but the most recent closed minute (+0.13 M) is the only clean flip; one bucket is not an exhaustion series.
3. **G2 completed bullish rejection** — the most recent closed 15M bar (13:00–13:15) traded to 111.50 and closed 112.39 ≈ exactly at the band, but price has since printed 112.31 (below band) and the sweep low sits 1.5 ATR under it; a re-test holding the band on a *closed* bar has not occurred.

**Live adjudication of the thesis (13:28 → 13:43 UTC):** SOL fell a further **−1.40 ATR** (worst mid **111.215**, −1.92 ATR). The $730k level at 112.21 and the −2σ band at 112.39 were both absorbed. An illustrative long staged at 112.30 with the desk's minimum 1.5–1.9 ATR stop (111.43–111.25) would have been **filled within seconds and stopped out within ~14 minutes** (mid 111.465 at 13:39; low 111.215 at 13:42). This is direct evidence for refusing to pre-stage an unconfirmed mean-reversion limit, and the reason the verdict does not change even though SOL is the closest numeric candidate.

### 3.2 Runners-up and their exact blockers

| Asset | Extreme evidence | Exact missing confirmation |
|---|---|---|
| **NERUSD.p** | Z **−2.25 SD** (second deepest) | RSI 32.5 (needs <30); spread **63.76 bps** (needs <25) — two hard fails. Wall band: 3 samples, $211k loose / none strict. |
| **ADAUSD.p** | Most persistent band depth of the window: ≥150k bid inside ±0.25 ATR of the −2σ band in **34 consecutive samples (~34 min)**, max **$646,074** | Z −1.47 (needs ≤ −2.0); RSI 33.3 (needs <30); spread **84.76 bps**; and **no admissible lot size** — min 1.0 lot × contract 5,000 × 1.5×ATR 0.0027 = **13.50 USD > 11.04 cap**. Structurally untradeable at this risk budget. |
| **BTCUSD.pi** | Bid wall band presence 4 consecutive samples (240 s), max **$716,410** near 82,150 | Z −1.31 and RSI 41.8 — numeric extremes absent; price never reached the −2σ band (0.73 ATR above mid at receipt). |
| **BNBUSD.p** | RSI **29.14** ✓ oversold | Z −1.52 (needs ≤ −2.0); no qualifying wall; last 60m CVD −7.29 M with no exhaustion flip. |
| **DOGUSD.p** | Massive stacked ask depth at 0.0867 (~$947k combined; 0.50 ATR above mid at 13:43) | Spread **241.80 bps** — fatal on G1 alone. |
| **ETHUSD.pi** | 60m CVD −58.4 M, 5m −6.8 M — persistent selling | Z −1.37 / RSI 34.4 (needs ≤ −2.0 / <30); band wall only 2 loose samples (120 s < 180 s); price is 2.10 ATR below VWAP, not yet at −2σ (−2σ sits 0.95 ATR *above* mid at receipt). |

### 3.3 Exact Model 1 confirmation checklist (SOL template, applies to any name)

1. **Price-anchored wall:** ≥$150k bid (long) unbroken across ≥3 consecutive 60-second samples at the revalidated −2σ level — no gaps, no downward migration of the level.
2. **Exhaustion:** closed 5m **and** 15m taker CVD ≥ 0 (or the counter-direction for a short) while price holds the level; and the 60m cumulative bleeding must at least halve from the receipt value (−20.6 M for SOL).
3. **Completed rejection:** a closed 15M bar whose low sweeps the level and whose close is back above it (long case), with the sweep low establishing the structural stop reference.
4. **Then** the geometry blueprint may be armed (entry at band/wall, SL ≥ 1.5×ATR beyond the sweep low, TP = 2.50R, 0.08–0.10 lots for SOL).

Until 1–3 all print on closed data, the SOL thesis remains **research-only**.

---

## 4. BLUEPRINT APPENDIX — research geometry only, NOT authorized to stage

| Setup | Entry | SL (ATR multiple) | TP (2.50R) | Volume | Nominal risk | Stressed total | Post-loss equity | Status |
|---|---|---|---|---|---|---|---|---|
| SOLUSD.p Model 1 long (illustrative) | 112.30 | 111.25 (1.85×) | 114.93 | 0.10 | 10.50 | 15.13 | **4,798.86** | **NOT STAGED — would have been stopped at 111.25 (low 111.215 after receipt)** |
| BTCUSD.pi Model 2 short (conditional) | 82,761 (VWAP, recompute) | 83,313 (1.92×, 552 pts) | 81,381 | 0.02 | 11.04 | 15.80 | **4,798.19** | Blocked: not at approach (needs ≤ 82,545.8), no wall, CVD mixed |
| BCHUSD.p Model 2 short (conditional) | 295.89 (VWAP, in approach zone) | 298.10 (1.62×, 2.21) | 290.37 | 0.50 | 11.04 | 15.80 | **4,798.19** | Blocked: no closed rejection, no ask wall, closed CVD still positive |

All three pass Gate 5 in isolation (and only SOL/BCH pass Gate 1 in their models), which is precisely why the missing G2/G3/G4 evidence — not the sizing — decides the ruling.

---

## 5. OPERATIONAL DIRECTIVES

1. **Stage nothing.** Keep 100 % cash flat. Preserve the +38.99 USD cushion and +18.99 USD headroom above the 4,795.00 operating threshold.
2. **Standing triggers (in priority order).**
   - **BCHUSD.p:** alert if a closed 15M bar rejects ≥295.89 with an upper wick AND a ≥$150k ask wall holds ≥180 s at/above 295.80 AND closed 5m CVD flips negative. Then re-run the scan; if all gates confirm, the blueprint in §4 may be submitted for admission.
   - **SOLUSD.p:** alert if the −2σ band (≈112.39 at receipt; recompute) is re-tested, held on a closed 15M bar, and closed 5m/15m CVD ≥ 0 with an unbroken ≥$150k bid at the level for ≥3 samples. Otherwise stand down; the current tape (−1.40 ATR further since receipt) is hostile to the long.
   - **BTCUSD.pi / ETHUSD.pi:** alert only on a rally to within 0.75 ATR of VWAP (82,545.8 / 2,548.06 recomputed) with the full §2.3 checklist.
3. **Non-crypto names (GOLD, SILVER, USWTI, EURUSD, GBPUSD, USDJPY, SP500, NAS100, DJ30, GER40):** remain ineligible for admission until an instrument-appropriate taker-flow/L2 feed (or an explicitly approved replacement confirmation policy) exists. Geometry-only entries are prohibited.
4. **Expiry discipline:** every level in this document is pinned to the 13:28:18 receipt and decays with each new telemetry commit. Any trigger must be re-derived from the live snapshot (ATR, VWAP, book) at the moment of decision, per the desk's approach-trigger doctrine.
5. **No broker action was taken** by this council: 0 positions, 0 pending orders, 0 modifications.

---

## 6. POST-BRIEFING TAPE UPDATE (13:43:18 UTC receipt — advisory, not a new ruling)

The next 15 minutes deepened the extremes while the missing gate got *worse*, not better:

| Asset | Z @13:28 → 13:43 | RSI @13:28 → 13:43 | Spread (bps) | Closed 5m CVD @13:43 | G4 strict wall | Reading |
|---|---|---|---|---|---|---|
| SOLUSD.p | −2.07 → **−2.63** | 21.0 → **19.4** | 24.21 (≤25, 0.79 bp margin) | **−5.16 M** | none | Numeric extremes qualify; sellers accelerating — no exhaustion. |
| BNBUSD.p | −1.52 → **−2.52** | 29.1 → **29.7** | 9.27 | **−1.30 M** | none | Z/RSI/spread now qualify; flow still one-sided down, no wall. |
| BTCUSD.pi | −1.31 → −2.69 | 41.8 → 38.3 | 1.83 | −16.97 M | none | Cascade leg; RSI still >30. |
| ETHUSD.pi | −1.37 → −2.64 | 34.4 → 33.0 | 13.53 | −22.47 M | none | Cascade leg; no exhaustion. |

This is the classic falling-knife signature: **extreme extensions with accelerating sell-side CVD**. The Model 1 gate set is a conjunction — a qualifying Z/RSI does not compensate for absent absorption, and absorption is the last thing present in an accelerating decline. VERDICT unchanged: **PUNCH NONE / DEFENSIVE HOLD**. Watch, do not catch.

*Evidence artifacts: `artifacts/arena_dual_model_scan_20261008_1328.json` (full per-asset JSON, 45-sample wall feed) · tool: `scripts/arena_dual_model_scan.py` (read-only, re-runnable) · receipt commit `a61284b` on `origin/arena/83d03e3f-trading-2`.*
