# Arena.ai — 24-Asset Dual-Track Ruling (EVOLVED GATING) + Resting-Order Verdict
## Briefing 2026-10-08 15:43:46 UTC · branch `arena/24eb818b-trading-2` · receipt `31e76f9` (snapshot as_of 15:43:21 UTC)

**Desk state:** equity **4,813.99** | 0 positions | **1 pending order (Ticket #18702099, BTCUSD.pi SELL LIMIT 81,580)** | floor 4,775.00 / threshold 4,795.00 | one risk slot
**Author:** Arena.ai — read-only. No broker I/O; nothing staged, modified or cancelled.

---

## 0. RULING

```
RESTING ORDER:  Ticket #18702099 → DELETE  (supporting wall at the 81,580 shelf is 100% gone)
TRACK 1 QUALIFIERS (3):  NAS100.p SHORT (#1) · SP500.p SHORT (#2) · USWTI.p LONG (#3)
TRACK 2 QUALIFIER (1):   AVXUSD.p LONG  (all three depth/flow limbs + 360 s wall persistence)
TOP-2 LIMIT STAGES:      A) NAS100.p SELL LIMIT 30989.10   B) AVXUSD.p BUY LIMIT 10.00
```

**Risk-cap conflict, resolved the same way as §47:** Section 2 re-states **10.00–11.04 USD** (stressed ≤ 15.80) while Section 6 states **10.00–15.00**. The G-1 floor math binds at `4813.99 − (risk×1.25 + 2.00) ≥ 4795.00 → risk ≤ 13.59`, so both readings are satisfiable. Stages A, B, SP500, ETH and LINK are sized at **≤ 10.50 USD** (valid under either text); USWTI ($11.59), NEAR ($11.30), SOL ($12.08) and LTC ($12.80) are valid **only** under the expanded 15.00 cap and are flagged as such.

**Data integrity (unchanged caveats):** committed `Data/Candles/*_15m.parquet` still lag at 13:30, so all CFD wick/volume evidence below is recomputed from the briefing's Section-5 15M bars (operative bar = **15:00–15:15**) with the parquet only supplying the 20-bar average scale; crypto depth is judged with the desk's persistence discipline across **11 consecutive one-minute receipts** (15:33:20 → 15:43:21, artifact attached); `whale_walls_l3 = []` on every crypto asset all window (`SAMPLED_ANONYMOUS_BINANCE_AGGREGATED_L2_NOT_L3`); receipt flag `DENIED_UNVERIFIED_ORDERFLOW`.

---

## 1. RESTING-ORDER REVIEW — TICKET #18702099 (BTCUSD.pi SELL LIMIT 81,580 · SL 82,150 · TP 80,155 · 0.02 lots)

**VERDICT: DELETE.** The desk's own review rule is "suporting whale wall thinned >50 %, **or** price drifted > 2.0×ATR → DELETE". The wall limb has fired with certainty:

| Test | Rule | Observed | Result |
|---|---|---|---|
| Supporting wall at the entry shelf (81,580) | DELETE if thinned > 50 % | At staging (15:33) a **BUY 81,387.7 wall of $746,000** carried the shelf. Across all 11 receipts since, the largest wall within ±600 pts of 81,580 is **$0** — every ≥$100k level sits at 81,065–81,240 (hugging mid: 81,007→81,220). The shelf's support is **100 % gone / migrated down with price** | **DELETE** |
| Price drift from entry | DELETE if > 2.0 ATR | mid 81,136.5 vs 81,580 → **−1.11 ATR** (delete line ≈ 80,780) | not yet, but widening |
| Stop sanity | G5 floor: SL ≥ 1.50 × ATR | 570 pts = **1.42 × ATR**(400.13) — below the floor the desk now enforces | fail |
| Fill premise | — | A fill now requires a **+444 pt rally (1.11 ATR)** into a tape whose 1H 15:00 bar printed delta **−17,058** and whose 15:15 bar made a lower low (81,183.5) | stale |

Ticket #18702099 therefore fails the desk's wall-persistence test exactly as BCH's 1.273 imbalance did in §46 and SOL's migrating walls did in §47. Delete it and return to a clean 0/0 baseline; **then** stage at most one of the setups below. *(Optional re-price on the live shelf, expanded-cap only: SELL LIMIT 81,190 / SL 81,800 = 1.52×ATR / TP 79,665 = 2.50R / 0.02 lots / risk $12.20 / stressed $17.25 → post-loss 4,796.74. Note 0.02 lots is the minimum that satisfies the $10 risk floor at a 1.5×ATR stop on this symbol.)*

---

## 2. TRACK 1 (CFD) — THREE QUALIFIERS

All three sit in established regimes (two bearish indices, one bullish commodity) with the operative 15:15 bar satisfying **volume ≥ 0.8× 20-bar avg AND ≥ 30 % rejection wick at the shelf**, and all three pass `stage_trade_plan.validate_plan`.

### #1 — NAS100.p · Model 2 micro-pullback SHORT
```
SELL LIMIT 30989.10   (session POC 30989.08 = +0.484 ATR above mid; EMA20 30993.48 = +0.569 ATR — same cluster)
SL 31089.10           (100.0 pts = 1.937 x ATR 51.6201 ; above the last three lower highs 31006.91 / 31027.90 / 31054.64)
TP 30739.10           (-250.0 pts = 2.50R ; below the session VAL 30874.96)
0.01 lots · risk $10.00 · stressed $14.50 · post-loss equity 4,799.49 · friction 0.37 bps = 0.004R
```
*Evidence:* 200-EMA slope **−0.0306 %** with regime BEARISH, z −0.83, RSI 49.85. The **15:15 bar** (O 30979.46 H 31006.91 L 30972.81 C 30995.08) rallied **through** the shelf to 31006.91 and was capped — **upper wick 34.7 %** on **46,737 vol = 2.39 ×** the 20-bar average (19,525) — the strongest rejection print of the 24-asset CFD set. Flow: 1H 15:00 delta **−32,721** on 94,434 vol; 4H 12:00 delta −13,224.
*CRO caveat:* the stop (31,089.10) is 35.6 pts **below** the day's absolute high (31,124.70), because the min-lot/risk-floor combination (0.01 lots ⇒ $0.10/pt ⇒ ≥100 pts for a $10 risk) does not allow a stop above 31,125 without breaching the 13.59 ceiling. Treat 31,090 as a structural stop above the recent swing highs, not a break-of-day-high stop.

### #2 — SP500.p · Model 2 micro-pullback SHORT (same cluster as #1 — correlated, stage only one)
```
SELL LIMIT 7774.20    (session POC 7774.2011 = +0.485 ATR; EMA20 7774.4039 = +0.511 ATR)
SL 7791.60            (17.40 pts = 2.223 x ATR 7.8267 ; above the session rejection high 7791.56)
TP 7730.70            (43.50 pts = 2.50R ; below the session VAL 7749.79)
0.06 lots · risk $10.44 · stressed $15.05 · post-loss equity 4,798.94 · friction 0.99 bps = 0.026R
```
*Evidence:* slope −0.0169 %, z −0.61. The **15:15 bar** (O 7770.04 H 7773.91 L 7767.81 C 7772.07) approached the POC/EMA20 shelf to within 0.3–0.5 pts and closed with a **30.2 % upper wick** on **1.49 ×** volume; the 1H 15:00 bar carries delta −10,909 and §46/§47 recorded the two prior 55.5 %/41.1 % rejection wicks at this same 7,778–7,784 shelf. Structural stop above the day's high 7791.56 — the cleanest stop geometry in the set.

### #3 — USWTI.p · Model 2 micro-pullback LONG (the universe's strongest trend; expanded-cap only)
```
BUY LIMIT 93.862      (prior 15m/1H swing shelf 93.86 ; -0.403 ATR below mid 94.026)
SL 93.252             (0.610 pts = 1.50 x ATR 0.4066 ; below the pullback low 93.74)
TP 95.387             (+1.525 pts = 2.50R)
0.19 lots · risk $11.59 · stressed $16.49 · post-loss equity 4,797.50
```
*Evidence:* slope **+0.2587 %** (strongest in the universe), BULLISH, z +1.22, RSI 60.49; the 15:15 bar printed a **30.9 % lower wick** at 93.74–93.91 on 1.15 × volume, i.e. the pullback was already bought at the shelf. *Caveat:* $11.59 exceeds the 11.04 boilerplate → valid only under the expanded cap.

**Not qualified (Track 1):** GER40 (all shelves > 2.5 ATR; 15:15 wick 25.5 % < 30 %), DJ30 (price is *above* its EMAs — no shelf overhead; VWAP +0.36 ATR but slope −0.034 % unproven), GOLD (EMA20/VWAP +0.81/+0.89 ATR outside the band), SILVER (POC in-band but 15:15 upper wick 23.1 % < 30 %, and min lot 0.01 × 5,000 oz forces $16.52 risk at a 1.5×ATR stop > 13.59 ceiling), EURUSD / GBPUSD (2-dp prints make wick geometry unverifiable, and slope −0.009 %/−0.003 % is not an established trend), USDJPY (no shelf within the micro-pullback band: EMA20 +0.79 ATR, POC −0.74, VWAP +2.08).

---

## 3. TRACK 2 (CRYPTO PERPS) — ONE CERTIFIED QUALIFIER, FIVE PARTIAL

The 15:00–15:15 flush pushed **all 14 crypto assets** to |Z| ≥ 2.3 with 12 of 14 RSI < 30 — so *geometry* (Model 1) is satisfied nearly everywhere and the ruling turns entirely on the depth/flow limb and on wall persistence.

### CERTIFIED — AVXUSD.p · Model 1 long flush
```
BUY LIMIT 10.00    (mid 10.01; entry sits on the 9.98–10.00 bid-wall shelf)
SL 9.79            (0.21 = 1.704 x ATR 0.1233 ; below the session VAL 9.88 AND below the 15:15 flush low 9.88 ; > stops_level 20 pts)
TP 10.53           (0.53 = 2.524R)
0.50 lots · risk $10.50 · stressed $15.13 · post-loss equity 4,798.86
```
*Geometry:* z **−3.05**, RSI **21.19**, slope −0.5799 %, BEARISH.
*Depth/flow (all three limbs):* (a) top-20 skew **1.4536 ≥ 1.25** at 15:43; (b) clustered ±0.50 ATR bid depth **$191k ≥ 150k**; (c) taker-CVD exhaustion — 3-vs-3 absolute decay **0.54** with the last six 1-minute deltas **−31.7k, +76.9k, +115.5k, +7.2k, +35.3k, −78.8k** (sellers stopped pressing, sum-of-5 +$156k).
*Wall persistence (the desk's ≥150k / ≥180s test):* a BUY wall at **9.977 $241k (15:34) → 9.984 $243.6k (15:36) → 9.996 $244.1k (15:40)** — **same price within 0.15 ATR across 360 s**, while mid held a 9.97–10.06 base for ~10 minutes above the flush low. This is the only crypto wall in the window that persisted *at a fixed price* instead of migrating down with the tape.
*Punch condition:* re-confirm the 9.98–10.00 wall (≥$150k) and skew ≥1.25 on the live book at submission; if the wall is absent, stand down.

### The five partial qualifiers (each fails exactly one limb — listed for the desk's awareness)

| Asset | Stage (validated) | z / RSI | limb (a) skew | limb (b) band | limb (c) CVD | Missing |
|---|---|---|---|---|---|---|
| **ETHUSD.pi** | BUY LIMIT 2447.75 / SL 2420.72 (1.63×ATR) / TP 2515.33 (2.50R) / 0.37 lots / **risk $10.00** | −3.93 / 20.65 | 1.192 ✗ | **$626k** ✓ | decel 0.359 ✓ | (a) — 4.6 % short of 1.25 |
| **SOLUSD.p** | BUY LIMIT 108.90 / SL 107.39 (1.51×ATR) / TP 112.68 (2.50R) / 0.08 lots / **risk $12.08** | −2.99 / 16.42 | 1.060 ✗ | **$4.69M** ✓ | 1.864 ✗ | (a) and (c); its walls migrate down with price each minute |
| **NERUSD.p** | BUY LIMIT 4.696 / SL 4.583 (1.50×ATR) / TP 4.979 (2.50R) / 1 lot / **risk $11.30** | −2.95 / 23.08 | 0.754 ✗ | $771k ✓ | decel 0.48 + flip ✓ | (a); wall 4.684–4.697 seen only at 15:41/15:43 (~120 s) |
| **LNKUSD.p** | BUY LIMIT 12.432 / SL 12.232 (1.89×ATR) / TP 12.932 (2.50R) / 0.50 lots / **risk $10.00** | −3.26 / 21.76 | 0.841 ✗ | $169k ✓ | decel 0.639 ✓ | (a); no discrete ≥150k wall near mid all window |
| **LTCUSD.pi** | BUY LIMIT 62.23 / SL 61.59 (1.52×ATR) / TP 63.83 (2.50R) / 0.2 lots / **risk $12.80** | −2.62 / 22.13 | 0.767 ✗ | $321k ✓ | decel 0.136 ✓ | (a); no discrete wall; min lot 0.1 forces $12.80 risk |

**Unsized / rejected:** **XRP** (the only asset satisfying (a) 1.423 + (b) $2.43M + (c) — but min lot 1.0 × 1,000 units ⇒ **$16.95 minimum risk** at a 1.5×ATR stop > 13.59 ceiling → structurally untradeable); **ADA** (same class: min lot 1.0 × 5,000 ⇒ $20.25 minimum); **BTC** (RSI 30.26 — misses the <30 test by 0.26; skew 0.74); **BNB** (skew 0.177, band $51k); **BCH** (band $25.8k, skew 0.676 — only limb (c)); **DOT** (band $69k, CVD *accelerating* 1.361, spread 202 bps); **TRX** (band $138k < 150k, no wall, skew series 0.48–1.83); **DOGE** (band ✓ but CVD decel 0.909 / no flip, and its round-to-tick stop re-derives below the 1.50×ATR floor).

---

## 4. TOP-2 LIMIT ORDER STAGES — READY TO PUNCH

> Precondition: **delete Ticket #18702099 first** (one risk slot; multi-order staging prohibited). Stage **exactly one** of A or B.

**Stage A — NAS100.p (Track 1 · Model 2 short)**
```
SELL LIMIT 30989.10 | SL 31089.10 | TP 30739.10 | 0.01 lots | risk $10.00 | 2.50R | sl 1.94xATR
```
**Stage B — AVXUSD.p (Track 2 · Model 1 long flush)**
```
BUY LIMIT 10.00 | SL 9.79 | TP 10.53 | 0.50 lots | risk $10.50 | 2.52R | sl 1.70xATR
```
Both were re-validated through `Terminal/Headless/stage_trade_plan.validate_plan` (risk ✓, TP inside the 2.50–3.14R band ✓, SL ≥ 1.50×ATR ✓, tick/step geometry ✓, floor math ✓). Both are ≤ 11.04 USD, so they satisfy either risk-cap reading.

**Substitutes of equal quality** (same validated table): SP500.p 7774.20/7791.60/7730.70 ($10.44 — replaces Stage A if the desk prefers a break-of-day-high stop), ETHUSD.pi 2447.75/2420.72/2515.33 ($10.00 — replaces Stage B with a 3× deeper stretch but 4.6 % short on skew).

---

## 5. PROTOCOL

1. Delete #18702099 → book 0/0 → stage exactly one of Stage A / Stage B (or a listed substitute).
2. Re-verify live at submission: quote/spread, recomputed ATR/VWAP, `stops_level` (AVAX 20 pts ✓ 0.21 > 0.20; indices 0 ✓), broker-native stop valuation, joint-fill admission, blackout calendar (FOMC window closed).
3. Ratchet on fill: **BE at +0.80R → SL entry +0.15R; +1.50R → SL entry +0.80R; final TP 2.50R.**
4. Prune triggers: Stage A — 15m close above **31028** (reclaim of the 15:00 high) or spread > 25 bps; Stage B — loss of the 9.98 wall (mid < 9.90) or skew < 1.0 for two consecutive receipts; either — drift > 2.0×ATR from entry unfilled.
5. Fail-closed: any live check failure ⇒ no stage command; this document is analysis, not an execution instruction.

---

*Artifacts: `artifacts/arena_dual_track_scan_20261008_1543.json` (scanner v2 output, 24 assets) · `artifacts/arena_depth_persistence_20261008_1543.json` (11 one-minute receipts × 9 assets: mid, skew, band depth, wall levels) · `docs/trade_plans/ARENA_LIMIT_STAGES_20261008_1543.json` (all 9 validated plans) · scanner `scripts/arena_dual_track_scan_v2.py` · receipt `31e76f9`.*
