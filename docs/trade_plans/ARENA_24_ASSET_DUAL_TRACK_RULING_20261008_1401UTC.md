# Arena.ai — 24-Asset Dual-Track Ruling (Track 1 CFD / Track 2 Crypto-Perp)
## Briefing 2026-10-08 14:01:10 UTC · receipt `2a1c7ce` (as_of 14:00:38 UTC)

**Machine receipt:** `origin/arena/24eb818b-trading-2` → `docs/telemetry/live_snapshot_latest.json`, `as_of_utc = 2026-10-08 14:00:38 UTC`
**Desk state:** balance/equity **4,813.99** | margin 0.00 | **0 positions / 0 pending** | floor 4,775.00 | operating threshold 4,795.00 | headroom **+18.99** | **exactly 1 risk slot**
**Capacity math (repo `validate_plan` + `assert_joint_fill_safe`):** nominal risk ∈ [10.00, 11.04]; stressed = risk×1.25 + 2.00; post-loss equity must be ≥ 4,795.00
**Author:** Arena.ai — read-only; no MT5 order was placed, changed or cancelled.

---

## 0. RULING

```
TRACK 1 QUALIFIER (1):  SP500.p  — Model 2 trend-pullback SHORT  → full blueprint in §2
TRACK 2 QUALIFIER:      none (BCHUSD.p technical pass refuted in §3 — unstable depth proxy)
```

One setup clears all five gates of its venue-appropriate track at this receipt: **SP500.p SELL LIMIT 7783.40**. Four runners-up are ranked with exact missing triggers in §4. Because exactly **one** risk slot exists, at most one blueprint may be staged — multi-order staging remains prohibited.

**Method note (why some gates read differently from Section 45):** this ruling applies the council's 14:01:10 dual-track mandate — CFD instruments are *not* failed for lacking Binance L2/taker-CVD, and crypto instruments are judged on the Track 2 depth/flow alternatives. Wall/imbalance tests are additionally checked for **sample stability** (the desk's standing anti-spoofing discipline), which is what refutes the BCH pass in §3.

---

## 1. 24-ASSET DUAL-TRACK GATE MATRIX (receipt 14:00:38 UTC)

**Track 1 assets — G3/4 proxies measured on committed 15m candles** (last closed bar in `Data/Candles/*.parquet` = 13:30; the briefing's 13:45 bar is cross-checked where it changes an outcome).

| Asset | G1 spread bps | Δ VWAP (ATR) | EMA200 slope | 15m vol ratio | Upper / lower wick | G5 size in 10–11.04 USD | Verdict |
|---|---|---|---|---|---|---|---|
| SP500.p | **0.31** ✓ | **+0.24** ✓ | −0.0307 % (bear) | **2.89×** (13:45: 2.39×) | **55.5 % / 22.2 %** (13:45: 41.1 % / 6.3 %) | 0.05–0.10 lots ✓ | **QUALIFIES (M2 SHORT)** |
| GER40.p | 0.32 ✓ | +0.67 ✓ | −0.1128 % (bear) | 1.21× | 47.7 % / 45.2 % (13:45: **28.5 %** / 37.7 %) | 0.01 lot ✓ | Conditional — 13:45 bar misses wick by 1.5 pts (§4.1) |
| EURUSD.pi | 0.09 ✓ | +0.62 ✓ | −0.0236 % (bear) | 1.26× | 43.5 % / 11.3 % (13:45 unverifiable — briefing rounds to 2 dp) | 0.05 lots ✓ | Conditional — most-recent-bar wick unverifiable (§4.2) |
| GOLD | 0.17 ✓ | +0.20 ✓ | −0.0154 % | 1.72× | 42.4 % / 34.2 % | **none** (min lot 0.01 → SL ≥1.5 ATR forces $12.27 > 11.04 cap) | FAIL G5 (structural, not price) |
| USDJPY.pi | 0.19 ✓ | +0.59 ✓ | **+0.0068 % (bull)** | 1.20× | 33.8 % / 56.8 % (13:45: 12.5 % / **25.0 %**) | 0.15 lot (JPY-adjusted) ✓ | FAIL G3 — pullback long needs ≥30 % lower wick; 13:45 = 25 % |
| USWTI.p | 5.04 ✓ | **+2.63** ✗ | +0.2727 % (bull) | 1.41× | 13.7 % / 6.7 % | 0.10–0.13 lots ✓ | FAIL G2 — extended above VWAP, not a pullback |
| GBPUSD.pi | 0.38 ✓ | +1.11 ✗ | −0.0152 % | 1.25× | 56.4 % / 38.6 % | 0.04 lots ✓ | FAIL G2 |
| DJ30.p | 0.23 ✓ | +3.51 ✗ | −0.0705 % | 2.76× | 18.5 % / 10.9 % | 0.01 lot ✓ | FAIL G2 (Z 1.57 < 2.0 for M1; RANGE_BOUND) |
| NAS100.p | 0.32 ✓ | −1.74 ✗ | −0.0503 % | 3.73× | 53.6 % / 20.9 % | 0.01 lot ✓ | FAIL G2 |
| SILVER | 6.08 ✓ | −1.06 ✗ | −0.2258 % | 1.74× | 14.2 % / 12.8 % | none | FAIL G2 + G5 |

**Track 2 assets (14 crypto).** G2 column: `M2` = |ΔVWAP| ≤ 0.75 ATR in-trend; `M1` = |Z| ≥ 2.0 **and** RSI < 30 / > 70. G3/4 = (a) top-20 depth ratio ≥ 1.25×, (b) clustered ±0.50 ATR depth ≥ $300k, (c) 1m/5m CVD exhaustion.

| Asset | G1 spread bps | Z / RSI | Δ VWAP (ATR) | G2 | G3/4 evidence (14:00:38) | G5 | Verdict |
|---|---|---|---|---|---|---|---|
| BCHUSD.p | 23.04 ✓ | −0.07 / 49.3 | **−0.09** | M2 ✓ | (a) ask/bid **1.273** ✓ point-in-time — **but see §3: unstable** | 0.4 lots ✓ | **FAIL** (proxy not persistent) |
| SOLUSD.p | 20.52 ✓ | −1.77 / 27.7 | −3.55 | ✗ | band $8.36 M ✓, CVD 5m −$5.16 M (still selling) | ✓ | FAIL G2 (Z short of 2.0; price far below value) |
| BNBUSD.p | 10.58 ✓ | −1.74 / 24.8 | −3.42 | ✗ | (a) 1.379 ✓, band $181k ✗ | ✓ | FAIL G2 |
| BTCUSD.pi | 7.56 ✓ | −1.76 / 37.0 | −1.88 | ✗ | band $1.24 M ✓, 1m CVD whipsawing ±$12 M | ✓ | FAIL G2 |
| XRPUSD.pi | 35.75 ✗ | −0.75 / 45.1 | −1.01 | ✗ | band $2.77 M ✓ | ✓ | FAIL G1+G2 |
| ADAUSD.p | 92.99 ✗ | −1.22 / 36.3 | −1.90 | ✗ | band $2.91 M ✓ | ✗ | FAIL |
| DOGE | 241.52 ✗ | +0.44 / 42.1 | +0.60 | ✓ M2 but no trend | — | ✓ | FAIL G1 |
| TRX / DOT / LINK / LTC / AVAX | 32.9 / 189.5 / 71.9 / 46.8 / 37.8 ✗ | — | — | ✗ | — | — | FAIL G1 |
| NEAR | 64.17 ✗ | −2.02 / 33.9 | −4.34 | ✗ (RSI 33.9) | band $2.08 M ✓ | ✓ | FAIL G1 |

No Track 2 instrument qualifies: the only geometric pass (BCH) fails the stability test on its depth proxy; every other crypto misses G1, G2 or both.

---

## 2. QUALIFIED BLUEPRINT — SP500.p MODEL 2 PULLBACK SHORT (Track 1)

```
Symbol:      SP500.p          Model:  Model 2 (trend-following pullback)
Direction:   SELL LIMIT       Entry:  7783.40
Stop Loss:   7794.40          (11.00 pts = 1.515 × ATR(14) 7.2623 ; 1.46 pts above snapshot VAH 7792.94)
Take Profit: 7755.90          (−27.50 pts = exactly 2.50R ; sits between POC 7771.93 and VAL 7749.79)
Volume:      0.10 lots        (contract 10.0 → $1.00/point)
Nominal risk: $11.00          (≤ 11.04 cap)  |  Stressed: 11.00×1.25 + 2.00 = $15.75
Post-loss equity: 4,798.24    (≥ 4,795.00 threshold; floor cushion preserved)
Friction:    spread 0.24 pts = $0.24 = 0.022R  (max_friction_r 0.35 ✓)
TTL:         8 × 15m bars (2 h) — recommend hard expiry; re-validate at fill
```

**Validation:** the plan passes the repo's own `Terminal/Headless/stage_trade_plan.validate_plan` client-side governance envelope (SL ≥ 1.5×ATR ✓; TP inside the 2.50–3.14R band ✓; risk 10.00–20.00 ✓; tick/step/lot geometry ✓; floor math via `assert_joint_fill_safe` ✓ — one slot, no correlation-cluster conflict).

### Microstructure justification (why *this* level)
1. **Geometry:** mid 7779.20 sits **+0.243 ATR** above Session VWAP 7777.4345 with a **negative** 200-EMA slope (−0.0307 %) — a value-area pullback in the desk's own bearish classifier → sell the retest.
2. **Two consecutive rejection bars at the same shelf** (this is the persistence the mandate's CFD proxy is looking for):
   • 13:30 bar: H 7779.33 rejected, **upper wick 55.5 %** of range, tick volume **31,976 = 2.89×** the 20-bar average (11,082);
   • 13:45 bar: H **7783.38** (≈ the 4H[08:00] high 7784.17), **upper wick 41.1 %**, volume 26,520 = **2.39×**.
   Price has been unable to hold above 7779–7784 despite the largest volume of the session.
3. **Structural stop/target:** SL sits **above VAH 7792.94** (the value-area high = invalidation line); TP 7755.90 is a 2.50R objective inside the lower value area toward the session low 7749.79 (4H low) — no moonshot target.
4. **Friction:** 0.31 bps spread (institutional < 1 bps target met); 2.2 % of R round-trip.

### CRO reservations (disclosed, not gate failures)
* 200-EMA slope is only −0.03 % — the weakest "trend alignment" in the qualifying set; this is a *value retest* short, not a strong-trend continuation.
* The 13:45 bar's delta was **+4722** (buyers) and DJ30 is +2.17 ATR risk-on — index internals are divergent. If SP500 closes a 15m bar **above 7784.20**, the false-breakout read fails and the order should be pulled (prune trigger = structure break, not just the 2×ATR drift rule).
* The receipt itself carries `trade_authorization: DENIED_UNVERIFIED_ORDERFLOW` and `ADMISSION_FROZEN_UNVERIFIED_DATA` — the generator does not certify trades. This ruling is an analytical gate assessment; broker-native valuation (`order_calc_profit`) and the live joint-fill admission check remain mandatory before any staging.

**Alternative geometry (more selective, false-breakout entry):** SELL LIMIT 7784.20 / SL 7795.20 (11.00 pts = 1.51×ATR) / TP 7756.70 (2.50R) / 0.10 lots / risk $11.00 — fills only if price pushes above the 4H double top and fails.

---

## 3. WHY BCHUSD.p IS NOT CERTIFIED (Track 2 depth proxy is unstable)

BCH ticked every box on first inspection — spread 23.04 bps < 25, ΔVWAP −0.09 ATR, bearish slope −0.356 %, sizing 0.4 lots @ 1.67×ATR (risk $10.40), and top-20 ask/bid = **1.273 ≥ 1.25**. The desk's standing anti-spoofing discipline then required persistence. The last 12 one-minute receipts:

| receipt (UTC) | 13:49 | 13:50 | 13:51 | 13:52 | 13:53 | 13:54 | 13:55 | 13:56 | 13:57 | 13:58 | 13:59 | 14:00 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ask/bid | 2.11 | 1.60 | 1.20 | **0.51** | 1.04 | **0.52** | 2.10 | 1.72 | **0.96** | **0.55** | **0.46** | 1.27 |
| book size (bid+ask) | $75k | $66k | $82k | $90k | $72k | $65k | $93k | $98k | $87k | $77k | $79k | $68k |

The ratio swings **0.46 → 2.11** on a $65–98k book: 7 of 12 samples were *below* the 1.25 threshold (5 below 1.0). A single-sample 1.273 reading is noise, not resting depth. The other Track 2 alternatives also fail for BCH: clustered ±0.50 ATR depth = **$67.7k ≪ $300k**, and 1m/5m CVD shows buyers **pressing** (+$283k over the last 5 closed minutes), i.e. no seller exhaustion. **BCH remains a watch item, not an order.**

*Watch trigger for BCH:* ask/bid ≥ 1.25 in **≥ 3 consecutive** 60-second samples, book ≥ $150k, price still within 0.75 ATR of VWAP, and a closed 15m bar rejecting ≥ 295.96.

---

## 4. RUNNERS-UP AND EXACT MISSING TRIGGERS

### 4.1 GER40.p — Model 2 short (fails by 1.5 wick points on the operative bar)
Spread 0.32 bps ✓, ΔVWAP **+0.67 ATR** ✓, slope −0.1128 % (bearish) ✓, 13:30 bar upper wick 47.7 % with 1.21× volume ✓ — but the **13:45** completed bar's upper wick is **28.5 %** (below the 30 % floor) and it closed **up** (+868 delta). Trigger: a completed 15m bar with an upper wick ≥ 30 % that fails at/above **24968.1** (13:30 high) with volume ≥ 0.8×; then short entry 24968.10, SL ≥25073 (≥1.5 ATR; 0.01 lot ⇒ risk $10.52), TP 2.5R ≈ 24705.

### 4.2 EURUSD.pi — Model 2 short (most-recent-bar evidence unverifiable)
Spread 0.09 bps ✓, ΔVWAP **+0.62 ATR** ✓, slope −0.0236 % (bearish) ✓, 13:30 bar upper wick 43.5 % with 1.26× volume ✓. The 13:45 bar cannot be verified (the briefing prints EURUSD to 2 dp: O=H=L=C=1.12), so the operative-bar gate fails closed. Trigger: a closed 15m bar ≥ 1.1197 with an upper wick ≥ 30 % and volume ≥ 0.8× (avg 1,353); then SELL LIMIT 1.1197, SL 1.1217 (2.5 ATR, risk $10.00 @ 0.05 lots), TP 1.1147.

### 4.3 USWTI.p — Model 2 long (strongest bullish trend; needs the pullback)
Slope **+0.2727 %** (strongest in the universe), spread 5.04 bps ✓, sizeable (0.10–0.13 lots). Price is **+2.63 ATR above VWAP** — entering now is chasing, not pulling back. Trigger: pullback to **≤ 92.65** (VWAP 92.386 + 0.75 × ATR 0.3495) with a completed 15m bar showing a lower wick ≥ 30 % and volume ≥ 0.8× (avg 1,307); then BUY LIMIT in 92.39–92.65, SL ≥1.5 ATR below, TP 2.5R.

### 4.4 SOLUSD.p / BNBUSD.p — Model 1 longs (one gate short)
SOL: RSI **27.7** ✓ but Z **−1.77** (needs ≤ −2.0), ΔVWAP −3.55 ATR; BNB: RSI **24.8** ✓ but Z **−1.74**. Both still show negative closed 5m CVD (SOL −$5.16 M). Trigger: Z ≤ −2.0 on a fresh receipt **and** a stalled 1m/5m delta series (exhaustion) **and** an unbroken clustered band ≥ $300k at the −2σ shelf. Do not catch the knife before that.

*(Also screened and failed: GOLD — all gates met except sizing, structurally untradeable at this risk budget; USDJPY — bullish-regime pullback long, 13:45 lower wick 25 % < 30 %; DJ30 — RSI 74.1 overbought but Z 1.57 < 2.0 and RANGE_BOUND; NAS100 — ΔVWAP −1.74 ATR; NEAR — Z −2.02 but RSI 33.9 and spread 64.2 bps.)*

---

## 5. STAGING PROTOCOL (if the desk accepts the Track 1 blueprint)

1. One order maximum. SP500.p SELL LIMIT 7783.40 / SL 7794.40 / TP 7755.90 / 0.10 lots — or the 7784.20 false-breakout variant. Not both.
2. Re-verify at submission: live quote/spread, VWAP/ATR recompute, `stops_level` (0 ✓), broker-native stop valuation, joint-fill admission (single slot, no cluster conflict), blackout calendar (FOMC window closed 2026-10-07 18:30 UTC ✓).
3. Confirm-fill ratchet (desk standard): Phase 0 BE at +0.80R → SL to entry +0.15R; Phase 1 at +1.50R → SL to entry +0.80R; final TP 2.50R.
4. Prune triggers: 15m close **above 7784.20** (structure break), price drift > 2.0×ATR from entry without filling, or spread > 25 bps.
5. If any live check fails, **no stage command** — the fail-closed rules of `live_admission.py` govern over this document.

---

*Evidence: `artifacts/arena_dual_track_scan_20261008_1401.json` · tool `scripts/arena_dual_track_scan.py` (read-only, re-runnable) · receipt commit `2a1c7ce` · plan template `docs/trade_plans/ARENA_SP500_M2_SHORT_20261008_1401.json` (validation-passing, conditional, not staged).*
