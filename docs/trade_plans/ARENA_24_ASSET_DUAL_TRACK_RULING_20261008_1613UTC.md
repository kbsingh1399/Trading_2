# Arena.ai — 24-Asset Dual-Track Ruling (EVOLVED GATING) + Resting-Order Verdict
## Briefing 2026-10-08 16:13:45 UTC · branch `arena/24eb818b-trading-2` · receipt `b63bafc` (snapshot as_of 16:13:37 UTC)

**Desk state at 16:13:37:** equity **4,813.99** | 0 positions | **1 pending order — Ticket #18703132 (NAS100.p SELL LIMIT 30,989.10)** | floor 4,775.00 / threshold 4,795.00 | one risk slot
**Author:** Arena.ai — read-only. No broker I/O; nothing staged, modified or cancelled.

> **⚠ UPDATE (16:19:37 UTC, receipt `ea138dd`):** Ticket #18703132 **FILLED at 16:17:16 UTC** — during a **market-wide macro thrust** (+87 pts in one minute) — and is now a **live SHORT NAS100.p 0.01 @ 30,989.10** (SL 31,089.10 / TP 30,739.10), marked **+$0.83 (+0.08R)** as the thrust fully retraced. Equity **4,814.82** (cushion +39.82 over the floor). §1 is retained as the review **as published at 16:13** (unfilled), followed by the position ruling; §5 is revised — **the same thrust voided the CFD-short stages** (see §5).

---

## 0. RULING

```
RESTING ORDER:  Ticket #18703132 (NAS100.p) → KEEP at 16:13  →  FILLED 16:17:16 @ 30,989.10  →  POSITION RULING: HOLD
TRACK 1 QUALIFIERS (3):  SP500.p SHORT (best) · GER40.p SHORT · GOLD SHORT   →  ⚠ ALL THREE VOIDED by the 16:17 thrust (§5)
TRACK 2 QUALIFIERS (2 certified):  SOLUSD.p LONG · NERUSD.p LONG
                        (+ 3 watch-tier: AVXUSD.p, DOTUSD.pi, BTCUSD.pi — reasons in §4)
TOP-2 LIMIT STAGES:  WITHDRAWN — the single risk slot is occupied by the live NAS100.p short; SP500.p/GOLD would have filled
                     into the thrust and are now underwater (§5). SOLUSD.p remains the best candidate but needs re-pricing.
```

**Desk bookkeeping honoured:** my §50 verdict on **Ticket #18702099 (BTCUSD.pi) was executed — the ticket is gone**; the desk staged **#18703132 = EXACTLY the §50 Stage A** (NAS100.p 30,989.10 / SL 31,089.10 / TP 30,739.10 / 0.01 lots). This ruling therefore opens with the review the mandate asks for, then re-scans all 24.

**Risk caps:** Section 2 restates 10.00–11.04 USD; Section 6 states 10.00–15.00. The floor math binds at `4813.99 − (risk×1.25 + 2.00) ≥ 4795.00 → risk ≤ 13.59`. Every stage below is quoted with exact risk + stressed equity; the two top stages ($10.82 and $12.06) are valid under either reading except where flagged.

**Data integrity:** committed `Data/Candles/*_15m.parquet` still lag at 13:30, so CFD wick/volume evidence is recomputed from the briefing's Section-5 bars (**15:15 / 15:30 / 15:45**) with the parquet supplying only the 20-bar average scale (artifact `arena_briefing_bars_20261008_1613.json`). Crypto depth is judged over **13 consecutive one-minute receipts** (16:02:37 → 16:13:37, artifact `arena_depth_persistence_20261008_1613.json`). `whale_walls_l3 = []` on all crypto again; receipt flag `DENIED_UNVERIFIED_ORDERFLOW`.

---

## 1. RESTING-ORDER REVIEW — TICKET #18703132 (NAS100.p SELL LIMIT 30,989.10 · SL 31,089.10 · TP 30,739.10 · 0.01 lots)

**VERDICT (published 16:13, unfilled): KEEP** — the ruling below is kept as published; the order then **filled at 16:17:16 UTC** (§1b).

| Test | Desk rule | Observed (16:13:37) | Result |
|---|---|---|---|
| Price drift from entry | DELETE if > 2.0 × ATR | entry − mid = **+43.40 pts = +0.835 ATR** (delete line ≈ 30,885) | **pass** |
| Supporting wall thinned > 50 %? | DELETE if yes | CFDs carry no whale-wall feed (`orderbook N/A`, Verified Whales 0) → limb inapplicable; the equivalent check is the shelf itself: session POC **30,989.08** and EMA20 **30,986.77** are still 0.79–0.84 ATR above price and unbroken | **pass** |
| Shelf still rejecting? | — | The 15:00–15:15 bar capped at **31,006.91** (34.7 % upper wick on **2.39×** volume); since staging (15:51:06) the 15:45 bar topped at 30,979.78 — two failures to reclaim | **pass** |
| Stop geometry | G5: SL ≥ 1.50 × ATR | 100.0 pts = **1.925 × ATR**(51.9454) | **pass** |
| Trend intact? | — | Lower highs 31,006.91 → 30,999.62 → 30,979.78; 1H 15:00 delta **−50,208**, 4H 12:00 delta −30,711, 15:30/15:45 15M deltas −8,721 / −8,766 on 43k/39k volume (2.2×/2.0× the 20-bar average) | **pass** |
| Reward | — | TP 30,739.10 = 2.50R, below the session VAL 30,874.96 | pass |

**Prune triggers (delete or re-price):** (i) a 15m close **above 30,999.62** (shelf reclaimed → thesis dead); (ii) mid **< 30,885.2** (drift > 2.0 ATR → stale level, rotate to the fresh shelf); (iii) spread > 25 bps. The order needs a **+0.84 ATR** pullback to fill; it costs nothing while unfilled, but it does occupy the single risk slot — if the desk wants the crypto flush instead, delete it first (§5).

### 1b. FILL & POSITION RULING (16:19:37 UTC, receipt `ea138dd`)

**FILLED 16:17:16 UTC @ 30,989.10** — exactly the staged limit. The fill was swept by a **market-wide macro thrust at 16:17** (one-minute moves: NAS100 +87.05, SP500 +17.12, GER40 +76.45, DJ30 +134.00, **USWTI −1.70 (−1.8 %)**, GOLD +16.87, SILVER +0.69 %, EURUSD +0.09 %, USDJPY −0.08 %, BTC +0.43 %). The thrust **fully retraced within two minutes**: NAS100 mid 30,947.41 (16:14:37) → 30,945.89 → 30,944.52 → **31,031.57** (16:17:37, spike high on `price_current` 31,040.75) → 31,002.45 → **30,982.76** (16:19:37) — i.e. +87 pts, then −29, then −20 back to the shelf: a **failed sweep / stop-run above the 30,999.62 lower high**, not an accepted reclaim.

**POSITION RULING: HOLD.** Trade thesis intact — price is back at the EMA20 shelf (30,982.9973 ≡ mid 30,982.76, z **−0.54**, trend regime **BEARISH**, EMA200 31,068.23 unbroken overhead), and the mark is **+$0.83 (+0.08R)**. Maximum adverse excursion so far −$5.17 (−0.52R at 16:17:37); cushion 39.82 USD over the floor — a full −$10.00 stop still leaves equity at **4,803.99** (+$28.99 over the 4,775 floor / +$8.99 over the 4,795 threshold).

| Position gate | Level | Action |
|---|---|---|
| Hard stop (unchanged) | **31,089.10** = 2.08 × ATR(51.1143) | −$10.00, cushion-safe |
| **Invalidation cut** | **15m close ≥ 30,999.62** (16:15 bar closes 16:30:00) | market cut at once (thesis dead) |
| Phase 0 (BE arm) | 30,909.10 = **+0.80R** | SL → 30,974.10 (+0.15R lock) |
| Phase 1 (profit lock) | 30,839.10 = **+1.50R** | SL → 30,909.10 (+0.80R lock) |
| Base target | **30,739.10 = +2.50R** (+$25.00) | extend only with SL locked ≥ +1.50R |

No ratchet action is possible yet (price has not reached +0.80R; `ratchet_state = PHASE_0_PENDING`). **Do not add, average or hedge** — the single risk slot is consumed by this ticket.

---

## 2. MARKET STATE AT 16:13 — TWO DIVERGENT TAPES

* **Crypto: still flushing.** All 14 assets sit 1.5–3.1 SD below session VWAP with 12 of 14 RSI < 30 (BNB **14.11**, ADA 14.83, DOGE 15.59, ETH **16.23**, NEAR 18.32, LINK 18.62, SOL 19.10, AVX 19.91, DOT 19.94, LTC 19.99, XRP 20.62, BCH 21.05, TRX 21.62; BTC 27.11). The 15:00–15:15 and 15:30–15:45 bars printed the largest sell deltas of the session (BTC 1H −25,199; NEAR 1H −4,277; LINK 1H −2,158), but the *last* three minutes show taker-CVD decay on SOL (0.74), NEAR (0.29 + buyer flip), ADA (0.16) and AVAX (0.47) — sellers are losing force into the lows.
* **Indices: orderly continuation lower.** NAS100/SP500/GER40 all BEARISH on negative 200-EMA slopes with heavy sell deltas (NAS100 1H −50,208; SP500 1H −12,449; GER40 1H −2,183). **DJ30 is the odd one out** — +0.74 SD *above* VWAP and rising highs (51,001.46), i.e. an index rallying against its own bearish slope → no shelf, no trade.
* **FX/commodities: no established trends.** EURUSD −0.007 %, GBPUSD −0.002 %, USDJPY +0.005 % — all flat; GOLD drifting at −0.017 % (rejected 4,118.46 on the 15:30 bar); USWTI remains the only bull (+0.261 %).

---

## 3. TRACK 1 (CFD) — THREE QUALIFIERS (evidence from the briefing's 15M bars)

Bar table (wick % of range · volume ÷ 20-bar average):

| Asset | 15:15 | 15:30 | 15:45 | Shelf (dist from mid, ATR) | Verdict |
|---|---|---|---|---|---|
| **SP500.p** | **uw 30.2 % (1.49×)** | uw 16.6 % (1.30×) | **uw 40.9 % (1.06×)** | EMA20 7,773.56 (**+0.175**) / POC 7,774.20 (+0.26) | **QUALIFIES** |
| **GER40.p** | **uw 46.9 % (1.005×)** | uw 10.5 % (0.99×) | uw 15.3 % (0.72×) | broken 2h shelf 24,831–24,837 (**+0.13**) | **QUALIFIES** |
| **GOLD** | uw 22.7 % (1.02×) | **uw 35.4 % (0.92×)** | uw 14.6 % (0.95×) | session VAL 4,112.10 (**+0.143**, broken) | **QUALIFIES** |
| USWTI.p | **lw 30.9 % (1.62×)** | lw 20.5 % | lw 12.1 % | EMA20 93.55 (−0.29) | near-miss — pullback hasn't printed a fresh ≥30 % lower-wick bar |
| SILVER | uw 23.1 % | uw 33.3 % (0.97×) | uw 20.0 % | no shelf in band; min lot 0.01 × 5,000 oz ⇒ $16.52 minimum risk | reject |
| NAS100.p | uw 34.7 % (2.39×) | uw 8.4 % | uw 22.9 % | shelf 30,986.77–30,989.08 (+0.79/+0.84) | already staged (#18703132) |
| DJ30.p | uw 24.7 % | lw 36.8 % | uw 22.9 % | none (price above all EMAs) | reject |
| EURUSD / GBPUSD | 2-dp prints ⇒ geometry unverifiable | | | POC/EMA50 at market; slope < 0.01 % | reject |
| USDJPY | lw 8.3 % | lw 8.3 % | lw 8.3 % | extended +1.11 ATR above EMA20 | reject |

### #1 — SP500.p · Model 2 micro-pullback SHORT *(best in set)*
```
SELL LIMIT 7773.56    (EMA20 shelf; session POC 7774.20 and VWAP 7777.61 overlap = 0.26/0.71 ATR)
SL 7791.60            (18.04 pts = 2.383 x ATR 7.5688 ; above the day's rejection high 7791.56)
TP 7728.46            (45.10 pts = 2.50R ; below session VAL 7749.79)
0.06 lots · risk $10.82 · stressed $15.53 · post-loss equity 4,798.47 · friction 0.99 bps = 0.026R
```
*Evidence:* bearish slope −0.016 %, z −0.44. **Two rejection bars at the same ~7,773 shelf**: 15:15 (H 7,773.91, **uw 30.2 %**, vol 1.49×) and 15:45 (H 7,773.02, **uw 40.9 %**, vol 1.06×), against a 15:30 bar that held the shelf twice; 1H 15:00 delta −12,449 on 60,154 volume. Structural stop above the day high.
*Tighter variant (if the desk prefers a small stop):* SELL 7773.56 / **SL 7786.06** (1.652×ATR) / TP 7742.31 / 0.08 lots / risk $10.00 — stop sits inside the day range, so it is more exposed to a wick.

### #2 — GER40.p · Model 2 micro-pullback SHORT
```
SELL LIMIT 24835.00   (broken 2h shelf 24,831–24,837 ; +0.23 ATR above mid 24,826.05)
SL 24935.00           (100.0 pts = 2.553 x ATR 39.1767 ; above EMA50 24,925.48 / VWAP 24,920.27)
TP 24585.00           (250.0 pts = 2.50R)
0.01 lots · risk $10.00 · stressed $14.50 · post-loss equity 4,799.49
```
*Evidence:* the strongest bearish slope among CFD assets (−0.1076 %), RSI 36.2; **15:15 bar upper wick 46.9 %** at 24,837.50 on 1.005× volume, then a descending-high chain (24,837.50 → 24,820.45 → 24,812.95). *Caveat:* 0.01-lot granularity forces a 2.55×ATR stop (100 pts) to clear the $10 risk floor, so the 2.5R target (24,585) lies below every 4H low of the day — this is a range-expansion bet, not a scalp.

### #3 — GOLD · Model 2 micro-pullback SHORT *(floor-margin tight)*
```
SELL LIMIT 4112.10    (broken session VAL 4,112.10 retest ; +0.143 ATR above mid 4,110.92)
SL 4125.34            (13.24 = 1.605 x ATR 8.2485 ; just under VWAP 4,124.67)
TP 4079.00            (33.10 = 2.50R)
0.01 lots · risk $13.24 · stressed $18.55 · post-loss equity 4,795.44  (only +0.44 above the 4,795 threshold)
```
*Evidence:* the 15:30 bar rejected **4,118.46 with a 35.4 % upper wick** on 0.92× volume; the 15:45 bar then closed bearish at 4,112.01 (δ −3,860) back into the broken VAL. *Caveat:* slope is only −0.017 % (the weakest of the three) and the min-lot forces almost the entire remaining floor headroom — if the desk wants a margin buffer, skip it.

---

## 4. TRACK 2 (CRYPTO) — TWO CERTIFIED QUALIFIERS, THREE ON WATCH

Persistence table — 13 one-minute receipts, 16:02:37 → 16:13:37:

| Asset | skew ≥ 1.25 | band ($k) ≥ 150 | band samples | max wall span | CVD decay | Limbs | Verdict |
|---|---|---|---|---|---|---|---|
| **SOLUSD.p** | 0/13 (max 1.12) | 3,736–5,359 | **13/13** | 120 s | **0.736** | (b)+(c) | **CERTIFIED** |
| **NERUSD.p** | 4/13 (max 1.73) | 781–1,737 | **13/13** | 60 s | **0.29 + flip** | (b)+(c) | **CERTIFIED** |
| AVXUSD.p | 2/13 | 160–457 | 13/13 | 0 s | 0.472 | (b)+(c) | watch — band only just above the 150 k floor and the §50 anchor wall (9.98–10.00, $243 k, 360 s) is **gone** |
| DOTUSD.pi | 3/13 (**last 3 in a row**) | 38–168 | **1/13** | 0 s | 0.81 | (a)+(c) | watch — imbalance only just turned ≥1.25 (1.44/1.30/2.07) and band depth only crossed $150 k in the final sample |
| BTCUSD.pi | 8/13 | 11–2,024 | 10/13 | 0 s | **1.662** | (b) | watch — imbalance is unstable (0.003 ↔ 9.65 across minutes) and CVD is still **accelerating**; RSI 27.1 |
| ADAUSD.p | 2/13 | 2,417–3,567 | 13/13 | **240 s** | **0.164** | (b)+(c) | **technically best, cannot be sized** — min lot 1.0 × 5,000 units ⇒ $22.50 minimum risk at a 1.5×ATR stop > 13.59 ceiling |
| XRPUSD.pi | 2/13 | 981–2,138 | 13/13 | 0 s | 0.324 | (b)+(c) | unsizeable — min lot 1.0 × 1,000 ⇒ $18.15 minimum risk |
| LINK / LTC / BCH / DOGE / TRX / ETH / BNB | — | — | — | — | — | ≤1 limb (ETH band $119 k; BCH $31 k; BNB $42 k; DOGE fails geometry at z −1.54; LTC z −1.87 < 2.0) | reject |

### CERTIFIED — SOLUSD.p · Model 1 long flush
```
BUY LIMIT 108.20      (mid 108.285 ; entry sits on the 108.16–108.30 bid-wall cluster ≈ $3.2M)
SL 106.86             (1.34 = 1.513 x ATR 0.8854 ; below the 107.82 flush low)
TP 111.55             (3.35 = 2.50R)
0.09 lots · risk $12.06 · stressed $17.08 · post-loss equity 4,796.91 · spread 20.3 bps (exempt for passive limits)
```
*Geometry:* z **−2.65**, RSI **19.10**, slope −0.5559 %, BEARISH. *Depth/flow:* ±0.50 ATR bid band **$3.74M–$5.36M in all 13 samples** (25–36× the $150 k floor); 1-minute taker-CVD decay **0.736** with the last 10 deltas [−0.17 M, −0.67 M, −1.09 M, −0.84 M, −1.21 M, **+1.48 M, +0.63 M, +0.92 M, +0.08 M**, −1.46 M] — three consecutive positive-absorption minutes mid-window. *Tape:* the 107.82 low was set at 15:30 and the 108.23–108.96 base has held for ~45 minutes. *Caveat:* a ~$4.2 M offer stack sits at 108.36–108.55 directly above the entry — expect slow progress, and the very last minute printed −1.46 M, so the exhaustion read is not yet sealed.

### CERTIFIED — NERUSD.p · Model 1 long flush
```
BUY LIMIT 4.651       (mid 4.651 ; entry on the 4.647 bid wall, $166k, with the 4.663 offer above)
SL 4.526              (0.125 = 1.504 x ATR 0.0831 ; below stops_level 20 pts = 0.020 ✓  ; below the 4.60 flush low)
TP 4.964              (0.313 = 2.504R)
1.0 lot · risk $12.50 · stressed $17.63 · post-loss equity 4,796.36
```
*Geometry:* z **−2.52**, RSI **18.32**, slope −0.6227 %, BEARISH. *Depth/flow:* ±0.50 ATR bid band **$781k–$1.74M in all 13 samples**; CVD decay **0.29** and a **buyer flip** (last 10: +0.54 M, −0.26 M, −0.25 M, −0.41 M, −2.10 M, **+0.48 M, +0.44 M, +0.75 M**, −0.09 M, +0.04 M). *Caveat:* a discrete $177 k offer sits at 4.663 (0.26 % above entry) and NEAR's band is 1/4 the size of SOL's.

**Watch triggers (do NOT punch yet):** DOT — require skew ≥1.25 **and** band ≥$150 k in ≥3 further consecutive receipts (its last three were 1.44/1.30/2.07 with band $86 k/$81 k/$168 k). AVX — require the 9.98–10.00 wall to reappear ≥$150 k and hold ≥180 s. BTC — require CVD decay < 0.85 (now 1.662) and a stable (not whipsawing) imbalance.

---

## 5. TOP-2 LIMIT ORDER STAGES — **REVISED AFTER THE 16:17 THRUST**

> **⚠ REVISION (16:19:37).** The 16:17 macro thrust moved **every CFD short entry in this file above its shelf**, so the stages as written would have filled into a losing position: **SP500.p mid 7,780.30 vs entry 7,773.56** (had it been staged it would be ≈ **−$6.4** at 0.06 lots, z flipped to +0.23), **GOLD mid 4,120.27 vs entry 4,112.10** (≈ **−$10.1** at 0.01 lots), **GER40 mid ≈ 24,896 vs entry 24,835** (≈ **−$6.1** at 0.01 lots). **All CFD-short stages are WITHDRAWN — do not stage them at these levels.** They re-qualify only after a fresh reversal bar closes back below the shelf.
>
> **Slot rule unchanged and now binding:** the single risk slot is **occupied by the live NAS100.p short** (§1b) — **nothing may be staged** until it resolves (TP / SL / invalidation cut). Any pre-priced candidate below is a *next-round* candidate, not a punch instruction.

**Stage A — SP500.p · Track 1 · Model 2 short — WITHDRAWN (see revision above)**
```
SELL LIMIT 7773.56 | SL 7791.60 | TP 7728.46 | 0.06 lots | risk $10.82 | 2.50R | SL 2.38xATR
```
*Why first:* the only setup in the set with **two** qualifying rejection bars at the same shelf in the last three bars, a structural stop above the day high, and a shelf cluster (EMA20 + session POC + VWAP) that has capped three consecutive rallies. Valid under both risk-cap readings.

**Stage B — SOLUSD.p · Track 2 · Model 1 long flush — DEFERRED (not withdrawn; slot occupied)**
```
BUY LIMIT 108.20 | SL 106.86 | TP 111.55 | 0.09 lots | risk $12.06 | 2.50R | SL 1.51xATR
```
*Why second:* deepest stretch with a **persistent 13/13** ±0.50 ATR bid band (25–36× the floor) plus CVD decay; the single largest tactical risk is the $4.2 M offer stack immediately overhead. **Status at 16:19:37:** SOL **108.745** (z −2.23, RSI 17.91, bid20 $4.80 M, skew 1.0605, fresh BUY walls 108.81–108.84 at $210–232 k) — the flush is *recovering* (+0.73 % off the 16:14 low), so the 108.20 entry is now 0.5 % below market and its edge is decaying. Keep as a pending candidate: **re-price and re-validate in the next council round**, only when the NAS100 position has closed. NEAR followed the same pattern (4.651 → **4.710**, z −2.03) — same treatment.

**Alternates (same validation table, in rank order):** SP500 tight (**withdrawn** — same thrust) · GER40 (**withdrawn** — same thrust) · NEAR (4.651 / 4.526 / 4.964 / 1.0 / $12.50 → **deferred/re-price**) · GOLD (**withdrawn** — entry now below market) · SOL smaller (108.20 / 106.76 / 111.80 / 0.07 / $10.08 — same deferral).

All seven plans in `docs/trade_plans/ARENA_LIMIT_STAGES_20261008_1613.json` were re-validated through `Terminal/Headless/stage_trade_plan.validate_plan` (risk ✓, TP inside the 2.50–3.14R band ✓, SL ≥ 1.50×ATR ✓, tick/step geometry ✓, floor math ✓, `stops_level` respected for NEAR 20 pts ✓ / AVAX 20 pts ✓ / SP500-GER40-GOLD-SOL 0 ✓).

---

## 6. PROTOCOL

1. **#18703132 is now a LIVE POSITION — HOLD** (no delete possible; it filled at 16:17:16). Cut only on the invalidation gate: 15m close ≥ 30,999.62. Ratchet ladder as per §1b.
2. **No new stages while the position is live.** When it closes (TP 30,739.10 / SL 31,089.10 / cut), the slot frees and the council will re-price SOLUSD.p (and re-scan all 24) on the then-current receipt.
3. Re-verify live at submission: quote/spread, recomputed ATR/VWAP, broker-native stop valuation, joint-fill admission, blackout calendar (FOMC window closed 2026-10-07 18:30 UTC).
4. Ratchet on fill: **BE +0.80R → SL entry +0.15R; +1.50R → SL entry +0.80R; final TP 2.50R.**
5. Fail-closed: any live check failure ⇒ no stage command. This document is analysis, not an execution instruction; no MT5 action was taken by Arena.

---

*Artifacts: `artifacts/arena_dual_track_scan_20261008_1613.json` (scanner v2, 24 assets) · `artifacts/arena_depth_persistence_20261008_1613.json` (13 receipts × 8 crypto assets: mid, skew, band depth, wall levels + spans) · `artifacts/arena_briefing_bars_20261008_1613.json` (15:15/15:30/15:45 bars with wick/volume recomputation) · `docs/trade_plans/ARENA_LIMIT_STAGES_20261008_1613.json` · scanner `scripts/arena_dual_track_scan_v2.py` · receipt `b63bafc`.*
