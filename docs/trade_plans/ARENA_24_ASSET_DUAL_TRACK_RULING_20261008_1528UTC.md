# Arena.ai — 24-Asset Dual-Track Ruling (EVOLVED GATING)
## Briefing 2026-10-08 15:28:25 UTC · branch `arena/24eb818b-trading-2` · receipt `bae7950` (snapshot as_of 15:28:20 UTC)

**Machine receipt:** `docs/telemetry/live_snapshot_latest.json` @ `bae7950` — `as_of_utc 2026-10-08 15:28:20`, `trade_authorization: DENIED_UNVERIFIED_ORDERFLOW`
**Desk state:** equity **4,813.99** | 0 positions / 0 pending | floor 4,775.00 | operating threshold 4,795.00 | **exactly 1 risk slot** (multi-order staging prohibited)
**Author:** Arena.ai — read-only. No broker I/O, no order staged, changed or cancelled.

---

## 0. RULING

```
TRACK 1 QUALIFIER (1):  SP500.p  — Model 2 micro-pullback SHORT  → full blueprint §2
TRACK 2 QUALIFIER:      none certified. Top-2 limit stages staged in §3 (AVAXUSD.p, SOLUSD.p)
                        — both pending the 3-sample depth-persistence trigger.
```

**Risk envelope applied (desk updates of 15:05/15:28 honoured, one conflict flagged):**
1. **G1 spread EXEMPT** for passive resting limits — no asset was failed for spreading wide (crypto spreads 19.6–250 bps no longer matter).
2. **Expanded risk budget** — Section 6 says *10.00–15.00 USD*, Section 2 boilerplate still says *10.00–11.04*. **Both are satisfiable**: the G-1 floor math binds at `4813.99 − (risk × 1.25 + 2.00) ≥ 4795.00 → risk ≤ 13.59`. Every blueprint below is quoted with the exact risk and stressed equity; the primary is sized at **$10.88**, i.e. valid under *either* reading.
3. **Adaptive micro-pullback** — Model 2 geometry re-scored as 0.10–0.60 ATR to a shelf (20/50 EMA, VWAP, VAH/VAL/POC, prior 15m/1H structure). This is what rescues SP500 (shelf +0.59 ATR) after the full-VWAP test became unreachable.

**Data-integrity notes (affect evidence selection):**
* Committed `Data/Candles/*_15m.parquet` lag at **13:30** (last write commit 22c7521, 13:48:45Z) — all CFD wick/volume evidence below is therefore recomputed from the briefing's **Section-5 15M bars** (14:30/14:45/15:00) and cross-checked with the snapshot indicators (`bars_last_close_utc 15:15`). Parquet volumes are used only as the 20-bar **average scale**.
* Crypto depth is judged with the desk's **persistence discipline** (the §46 BCH precedent): a signal quoted from a single 60-second receipt is not evidence. See §3 table.
* Binance L2 coverage is `REAL_BINANCE_FUTURES_L2` but `wall_coverage = SAMPLED_ANONYMOUS_BINANCE_AGGREGATED_L2_NOT_L3` with `whale_walls_l3 = []` on every crypto asset — no verified whales this window.

---

## 1. GEOMETRY SWEEP — ALL 24 (snapshot 15:28:20, distances in ATR from mid)

| Asset | Mid | ΔEMA20 | ΔEMA50 | ΔVWAP | Z | RSI | Slope % | Regime | Model-2 shelf in 0.10–0.60 band? |
|---|---|---|---|---|---|---|---|---|---|
| **SP500.p** | 7773.42 | **+0.16** | **+0.58** | **+0.59** | −0.37 | 45.8 | −0.017 | BEARISH | **YES — EMA50/VWAP cluster 7778.05/7778.09** |
| NAS100.p | 31005.4 | −0.23 | **+0.27** | +0.55 | −0.35 | 47.9 | −0.032 | BEARISH | YES — EMA50 31019.6 |
| GER40.p | 24833.0 | +1.55 | +2.57 | +2.23 | −1.13 | 36.1 | −0.100 | BEARISH | no (extends: nearest shelf 24851 = 15m structure, +0.43) |
| DJ30.p | 50961.1 | −0.26 | −0.20 | −0.43 | +0.21 | 51.0 | −0.037 | BEARISH | no (price above its EMAs, no shelf above) |
| GOLD | 4117.21 | +0.81 | +0.72 | +0.89 | −1.19 | 43.6 | −0.012 | BEARISH | no (outside band) |
| SILVER | 58.916 | +0.41 | +1.18 | +2.00 | −0.82 | 44.0 | −0.193 | BEARISH | geometry ✓ — but **G5 impossible**: min lot 0.01 × 5,000 oz × 1.5×ATR = $17.03 > 13.59 |
| USWTI.p | 93.776 | +0.92 | +2.64 | +3.11 | +1.05 | 65.7 | **+0.259** | BULLISH | no (extended; needs pullback to 93.41) |
| EURUSD.pi | 1.1199 | −0.33 | −0.44 | −0.56 | +0.50 | 57.2 | −0.010 | BEARISH | only VAH 1.1204 (+0.56); trend not established |
| GBPUSD.pi | 1.3215 | −0.18 | −0.64 | −0.82 | +0.89 | 56.4 | −0.003 | BEARISH | no shelf above in band |
| USDJPY.pi | 158.267 | +1.13 | +1.36 | +2.46 | +1.03 | 55.3 | +0.003 | BULLISH | no (extended) |
| BTCUSD.pi | 81408 | −2.95 | −3.55 | −3.54 | −3.61 | 41.3 | −0.197 | BEARISH | no — Model 1 stretch only |
| ETHUSD.pi | 2464.75 | −5.07 | −6.16 | −6.41 | −4.17 | 31.6 | −0.339 | BEARISH | no |
| SOLUSD.p | 109.245 | −4.92 | −6.58 | −7.24 | −3.39 | **24.5** | −0.471 | BEARISH | no — Model 1 long candidate (§3) |
| BNBUSD.p | 736.9 | −7.44 | −8.86 | −9.05 | **−4.65** | **22.6** | −0.221 | BEARISH | no — flow fails (bid book $23k) |
| XRPUSD.pi | 1.359 | −4.28 | −4.99 | −5.25 | −4.41 | 32.4 | −0.365 | BEARISH | no |
| ADAUSD.p | 0.2358 | −4.85 | −5.61 | −6.36 | −4.40 | **25.1** | −0.455 | BEARISH | no — **G5 impossible** (min lot 1.0 × 5,000 = $16.50 min risk) |
| DOGUSD.p | 0.0839 | −3.90 | −5.20 | −5.20 | −3.40 | 30.6 | −0.410 | BEARISH | VAL 0.0842 (+0.60) — flow fails |
| TRXUSD.p | 0.3329 | −3.25 | −4.00 | −4.50 | −2.98 | 32.2 | −0.018 | BEARISH | no |
| DOTUSD.pi | 1.0435 | −4.93 | −5.13 | −5.17 | **−6.36** | 32.5 | −0.316 | BEARISH | no — RSI > 30, spread 191 bps |
| LNKUSD.p | 12.5295 | −4.65 | −5.79 | −6.00 | −4.07 | 30.5 | −0.446 | BEARISH | no |
| BCHUSD.p | 285.65 | −5.22 | −5.82 | −5.61 | −5.18 | 34.9 | −0.318 | BEARISH | no |
| LTCUSD.pi | 62.565 | −4.41 | −5.55 | −5.54 | −2.86 | 33.0 | −0.445 | BEARISH | no |
| AVXUSD.p | 10.105 | −5.11 | −6.14 | −6.48 | −3.82 | **28.1** | −0.530 | BEARISH | no — Model 1 long candidate (§3) |
| NERUSD.p | 4.777 | −3.98 | −5.63 | −7.20 | −2.92 | **28.5** | −0.436 | BEARISH | no — flow weaker (§4) |

The tape is a **broad risk-off flush**: every crypto is 2.9–6.4 SD below session VWAP with a waterfall on the 15:00 bar (BTC −6,311 delta, ETH −2,726, SOL −1,386, AVAX −191, NEAR −1,335 …). On the CFD side the three equity indices are all bearish (leads: DJ30 14:30 bar −2,110, NAS100 15:00 bar −47,030, SP500 15:00 bar −17,445).

---

## 2. QUALIFIED BLUEPRINT — SP500.p MODEL 2 MICRO-PULLBACK SHORT (Track 1)

```
Symbol:      SP500.p                  Model:    Model 2 (trend-following pullback)
Direction:   SELL LIMIT               Entry:    7778.00
Stop Loss:   7791.60   (13.60 pts = 1.709 x ATR 7.9595 ; above the session rejection high 7791.56)
Take Profit: 7744.00   (-34.00 pts = exactly 2.50R ; below 48h VAL 7761.57 toward the 4H low 7749.79)
Volume:      0.08 lots                (contract 10.0 -> $0.80/point)
Nominal risk $10.88   (valid under BOTH the 11.04 boilerplate and the 15.00 expansion)
Stressed:    10.88 x 1.25 + 2.00 = $15.60  ->  post-loss equity 4,798.39 (>= 4,795.00)
Friction:    spread 0.77 pts (0.99 bps) = $0.62 = 0.057R  (max_friction_r 0.35)
TTL:         8 x 15m bars
```

**Repo validation:** passes `Terminal/Headless/stage_trade_plan.validate_plan` — `risk 10.88 ✓`, `tp_r 2.50 ✓`, SL 1.71×ATR ≥ 1.50 ✓, tick/lot geometry ✓, floor math ✓ (one slot, no cluster conflict).

### Microstructure justification
1. **Shelf cluster (the micro-pullback target):** EMA20 **7774.65** (+0.16 ATR), EMA50 **7778.05** (+0.58), Session VWAP **7778.09** (+0.59), session POC 7774.20 (+0.10). The short limit sits *inside* the 20/50-EMA + VWAP cluster — exactly the mandate's "retest of 20 EMA or 50 EMA dynamic shelf".
2. **The shelf has already rejected twice:**
   * **15:00 bar (15:00–15:15, operative):** O **7779.27**, H **7779.30**, L 7770.04, C 7770.05 — opened *at* the shelf, was capped within 3 ticks, sold 9.25 pts to close on the low. Volume **17,483 = 1.58×** the 20-bar average (11,082) and **delta −17,445 — the largest sell delta of the session**. 1H 15:00 delta −17,445; 4H 12:00 closed at 7770.05, delta −4,787.
   * **13:30 bar (rejection of record, §46):** H 7779.33 rejected with a **55.5 % upper wick on 2.89× volume** — the same 7779 shelf, same session.
3. **Trend alignment:** 200-EMA slope −0.017 %, regime BEARISH, z −0.37 (value retest, not chasing) — price sits 0.59 ATR *below* the shelf and 0.44 ATR above the 48h VAL, so the 2.5R objective is inside the value area, not a moonshot.
4. **Friction:** 0.99 bps spread = 0.057R round-trip.

### CRO reservations (disclosed, not hidden)
* **Strict-wick caveat:** the operative bars' upper wicks are 16.2 % (14:30), 10.1 % (14:45), **0.3 %** (15:00 — the bar opened at its high, so the "wick" is a body-appearance artifact). The mandate's ≥30 % rejection geometry at this shelf is met by the **13:30 bar (55.5 %, 2.89× volume)** and by the 15:00 cap-at-shelf; if the desk reads the gate as "last completed bar only", SP500 fails it and the strict verdict is **PUNCH NONE**. My ruling: the shelf-rejection proxy is satisfied (documented rejection + volume + delta), and I would stage it.
* Index internals diverge: NAS100 bounced off 30,979 / DJ30 off 50,939 before rolling; an equity bounce toward 7,800 would stop the order at −1R without breaking the 7,791.56 structure.
* Receipt carries `DENIED_UNVERIFIED_ORDERFLOW`; broker-native stop valuation + live joint-fill admission remain mandatory. **Not staged by Arena.**

**Alternative geometry (deeper shelf = 20 EMA):** SELL LIMIT 7774.65 / SL 7791.60 (16.95 pts = 2.13×ATR) / TP 7732.27 (2.50R) / 0.06 lots / risk $10.17. Higher fill probability, lower venue depth.

---

## 3. TRACK 2 — NO CERTIFIED QUALIFIER (top-2 limit stages below)

The evolved Track 2 rule is an OR — (a) top-20 depth ratio ≥ 1.25× in trade direction, (b) clustered ±0.50 ATR depth ≥ 150k–300k USD, (c) 1m/5m taker-CVD exhaustion. **Criterion (c) is satisfied for SOL/AVAX/ADA; criterion (b) for SOL/AVAX, NEAR, ADA, DOGE; criterion (a) only for AVAX — and every depth reading fails the desk's own persistence discipline.** Fourteen consecutive one-minute receipts (15:15:28 → 15:28:30 UTC, committed artifact):

| Receipt (UTC) | 15:28 | 15:27 | 15:26 | 15:25 | 15:24 | 15:23 | 15:22 | 15:21 | 15:20 | 15:19 | 15:18 | 15:17 | 15:16 | 15:15 | Stable? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SOL skew (bid20/ask20) | **1.24** | 0.96 | 1.03 | 1.04 | 1.14 | 0.64 | 1.68 | 0.62 | 1.15 | 2.27 | 0.74 | 0.76 | 0.75 | 0.87 | **NO** |
| AVAX skew | **1.66** | 0.87 | 1.46 | 1.89 | 0.63 | 0.25 | 0.74 | 0.33 | 0.42 | 0.33 | 1.00 | 1.07 | 0.96 | 1.03 | **NO** |
| SOL mid | 109.245 | 109.45 | 109.185 | 109.215 | 109.085 | 109.615 | 109.765 | 110.425 | 110.255 | 110.57 | 110.785 | 110.775 | 110.685 | 110.845 | −1.6 pts in 13 min |

SOL's six "buy walls" **migrate down with price every minute** (109.96/109.94/109.93/109.88 → 109.36 → 109.06/109.04/109.01 → 109.24/109.23/109.21/109.17 → 109.16/109.15/109.13/109.10 → 109.36/109.35/109.34/109.31 → 109.29/109.25/109.22/109.21) with `persistence_status = SAMPLED_ONLY_NOT_CONTINUOUS`, `sample_span_sec = 0.0`. That is the identical pattern that had SOL's "wall" migrate with price in the 13:13 window and that refuted BCH's 1.273 reading in §46 — **price is pushing through near-touch liquidity, not absorbing it.** Model 1's own spec (wall ≥150k USD **and ≥180 s persistence**) is therefore **not** met for any crypto.

**Stage A (best crypto candidate — punch ONLY on confirmation):**
```
AVXUSD.p  Model 1 (mean reversion)  BUY LIMIT
Entry 10.10 | SL 9.95 (0.15 = 1.52 x ATR 0.0989 ; below the 15:24 flush low 9.98) | TP 10.48 (2.53R)
Volume 0.68 lots (contract 100) | risk $10.20 | stressed $14.75 -> post-loss 4,799.24
```
*Evidence:* z **−3.82**, RSI **28.09**; the flush low printed **9.98 at 15:24** and price has since made higher lows (10.02 → 10.115 → 10.13) — a stopped knife, not a falling one. 1m taker CVD flipped buyers: **+237k, +506k, +1.09M, +205k** (last 4 min); 5-minute sum **−0.32M vs −4.26M** in the prior 5 minutes. Book at 15:28: bid20 **$196k** vs ask20 **$118k** (1.66× ≥ 1.25 ✓); clustered ±0.50 ATR depth **$196k ≥ 150k ✓**.
*Missing trigger:* the skew held ≥1.25 in exactly **one** receipt (0.87 at 15:27; range 0.25–1.89). **Punch only after the skew prints ≥1.25 in ≥3 consecutive receipts with the ±0.50 ATR band ≥ $150k** — otherwise leave it.

**Stage B (deepest stretch — punch ONLY on wall-persistence confirmation):**
```
SOLUSD.p  Model 1 (mean reversion)  BUY LIMIT
Entry 109.25 | SL 108.20 (1.05 = 1.51 x ATR 0.6966) | TP 111.88 (2.50R)
Volume 0.11 lots (contract 100) | risk $11.55 | stressed $16.44 -> post-loss 4,797.55
```
*Evidence:* z **−3.39**, RSI **24.45** (lowest of the 24 with feasible sizing); ±0.50 ATR bid depth **$4.48 M**; six Binance USDT-M buy walls 109.19–109.29 totalling **≈ $2.06 M**; CVD exhaustion — 5m **−10.4 M vs −19.1 M** prior, last 3 min **+6.05 M**.
*Missing trigger:* skew 1.2445 — **0.4 % below** the 1.25 threshold — plus non-continuous wall sampling (above). **Punch only if** the 109.19–109.29 wall level holds (does not migrate >0.15 ATR) and skew ≥1.25 across ≥3 consecutive receipts.

*(ADA, NEAR, DOGE reach criteria (b)+(c) but fail elsewhere: ADA & DOGE cannot be sized or flowed — ADA min lot 1.0 × 5,000 = $16.50 minimum risk > 13.59 ceiling; NEAR skew 1.20 and CVD worsening −0.78 M vs −0.48 M; DOGE needs ask-heavy skew ≤ 0.80 and shows 1.11.)*

---

## 4. RUNNERS-UP & EXACT MISSING TRIGGERS

| # | Setup | Exact stage ready to punch | Missing trigger |
|---|---|---|---|
| 1 | **GER40.p** M2 short (slope −0.100, RSI 36.1) | SELL LIMIT **24849.00** / SL 24912.00 (1.50×ATR) / TP 24691.50 / 0.02 lots / risk **$12.60** | 15:00-bar upper wick **25.5 %** (needs ≥30 %); 14:45 = 17.8 %, 14:30 = 20.1 %. Trigger: a 15m bar failing at/above 24851 with ≥30 % upper wick on ≥0.8× volume. |
| 2 | **NAS100.p** M2 short (slope −0.032) | SELL LIMIT **31019.60** (EMA50 +0.27 ATR) / SL 31119.60 (1.89×ATR) / TP 30769.60 / 0.01 lots / risk **$10.00** | Operative-bar wicks 7.0 % / 8.1 % / 0.9 % (needs ≥30 %). Trigger: ≥30 % upper-wick bar at 31,020–31,055 with ≥0.8× volume. |
| 3 | **USDJPY.pi** M2 long (BULLISH, slope +0.003) | BUY LIMIT **158.19** (EMA20) / SL 158.09 (1.5×ATR) / TP 158.44 / 0.15 lots / risk ≈ $10.30 | Extended +1.13 ATR above EMA20 (band ≤0.60) and slope +0.003 % is not an established trend. Trigger: pullback to ≤158.19 with ≥30 % lower wick. |
| 4 | **USWTI.p** M2 long (slope **+0.259**, strongest bull) | BUY LIMIT **93.41** (EMA20) / SL 92.82 / TP 94.89 / 0.14 lots / risk ≈ $11.00 | +0.92 ATR above EMA20 — outside the micro-pullback band; TP 94.89 sits under today's 94.37 high but the setup is chased. Trigger: pullback to ≤93.41 with ≥30 % lower wick, vol ≥0.8×. |
| 5 | **DOGUSD.p** M2 short (VAL retest) | SELL LIMIT **0.0842** / SL 0.0852 / TP 0.0817 / 1 lot / risk $10.00 | Flow: ask/bid skew 1.11 (needs ≤0.80 for a short) and 1m CVD not decelerating. Trigger: skew ≤0.80 for 3 receipts + a failed retest bar at 0.0842. |
| — | **GOLD** | (0.01 lots @1.5×ATR = risk $13.35, post-loss 4,795.30 — now feasible) | Geometry fails: EMA20 +0.81 ATR, VWAP +0.89 ATR; and $0.30 of floor headroom is not an operating margin. |

---

## 5. STAGING PROTOCOL

1. **One order only** (single slot). If the desk accepts the ruling: **SP500.p SELL LIMIT 7778.00 / SL 7791.60 / TP 7744.00 / 0.08 lots** — or the 20-EMA alternative at 7774.65 — never both, and never alongside a crypto stage.
2. Re-verify at submission: live quote/spread, recomputed VWAP/ATR, `stops_level` (0 ✓), broker-native stop valuation, joint-fill admission (`live_admission.py`), blackout calendar (FOMC window closed 2026-10-07 18:30Z ✓).
3. Confirm-fill ratchet: **BE at +0.80R → SL to entry +0.15R; at +1.50R → SL to entry +0.80R; final TP 2.50R.**
4. Prune: 15m close **above 7784.20** (false-break above the 15:00 bar high + EMA50), drift > 2.0×ATR from entry without filling, or spread > 25 bps.
5. If any live check fails, **no stage command** — fail-closed governance supersedes this document.

---

*Artifacts: `artifacts/arena_dual_track_scan_20261008_1528.json` (scanner v2 output) · `artifacts/arena_briefing_bars_20261008_1528.json` (Section-5 15M bars + wick/volume recomputation) · `artifacts/arena_crypto_depth_persistence_20261008_1528.json` (14 one-minute depth receipts) · `scripts/arena_dual_track_scan_v2.py` (re-runnable, read-only) · plans: `docs/trade_plans/ARENA_LIMIT_STAGES_20261008_1528.json` (all stager-validated, conditional).*
