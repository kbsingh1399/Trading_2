# Arena.ai — 24-Asset Dual-Model Ruling + Live Position Review
## Briefing 2026-10-08 16:28:56 UTC · branch `arena/24eb818b-trading-2` · receipt `ee38345` (snapshot as_of 16:33:37 UTC)

**Desk state at 16:33:37:** equity **4,813.73** | balance 4,813.99 | margin used 309.89 | free margin 4,503.84 | **1 open position — #18703132 NAS100.p SHORT 0.01 @ 30,989.10** (SL 31,089.10 / TP 30,739.10, mark **−$0.25 / −0.03R**) | 0 pending | floor 4,775.00 / threshold 4,795.00
**Author:** Arena.ai — read-only. No broker I/O; nothing staged, modified or cancelled.

---

## 0. RULING

```
POSITION #18703132 (NAS100.p SHORT 30,989.10)  →  HOLD     (no cut, no ratchet yet, no close)
    · invalidation gate (15m close >= 30,999.62) NOT triggered: the 16:15–16:30 bar closed ~30,993–30,995 (margin 0.11 ATR)
    · mark −0.03R; ratchet unarmed (Phase-0 arm sits at 30,909.10); hard SL unchanged 31,089.10

MODEL 2 (TREND-FOLLOWING) — 0 punchable CFDs:
    · in-band shelves exist only for NAS100 (asset already occupied) and GOLD (SL floor infeasible: needs 13.97 > ceiling 13.38)
    · GER40 is the best remaining Model-2 geometry but FAILS the desk's own wick gate (15M upper wicks 10.5 / 15.3 / 7.4 %; 16:00 vol 0.53×)
    · SP500 / DJ30 / USWTI / EURUSD / USDJPY: no shelf inside the 0.10–0.60 ATR band

MODEL 1 (MEAN-REVERSION) — 3 viable crypto candidates (G1 spread exempt):
    SOLUSD.p   LONG 108.20 / SL 106.82 / TP 111.65 / 0.08 lots / risk $11.04 / 2.50R   (limbs b+c, 12/12 band persistence)
    ETHUSD.pi  LONG 2411.00 / SL 2381.60 / TP 2484.50 / 0.37 lots / risk $10.88 / 2.50R (limbs a+b+c, deepest stretch)
    NERUSD.p   LONG 4.6930 / SL 4.561 / TP 5.023 / 1.0 lot / risk $13.20 / 2.50R      (expanded cap only)

TOP-2 STAGES (ready to punch, one only):   A) SOLUSD.p BUY LIMIT 108.20    B) ETHUSD.pi BUY LIMIT 2411.00
SLOT GOVERNANCE: with #18703132 live, a joint full-stop of it + any 10.00–11.04 stage projects 4,783.43 USD —
    below the 4,795 operating threshold (−$11.57) but above the 4,775 hard floor (+$8.43).
```

---

## 1. SECTION 3 — LIVE POSITION REVIEW (#18703132)

**Ruling: HOLD.** The mandate's decision tree — HOLD / piecewise ratchet / emergency shelf cut / close at market — resolves cleanly on the desk's own gate that the council published at 16:13 and reaffirmed at 16:24:

| Gate | Level / rule | Observed at 16:33:37 | Result |
|---|---|---|---|
| **Invalidation cut** | 15m close **≥ 30,999.62** ⇒ cut at market | The 16:15–16:30 bar closed **≈ 30,993–30,995** (mid 30,995.39 at 16:29:37 → 30,992.07 at 16:30:37) — **~6 pts (0.11 ATR) below the line** | **NOT triggered** (razor-thin — stays armed for the 16:30–16:45 bar) |
| Emergency shelf cut | shelf (POC 30,989.08 / EMA20 30,986.77) reclaimed | The 16:17 thrust pierced the shelf intra-bar to **31,040.75**, then fully retraced; price sits at the refreshed session **POC 30,996.00** (+0.09 ATR) with z −0.44 | not triggered |
| Phase 0 (BE arm) | +0.80R = **30,909.10** | price 30,990.79 — arm not reached | not armed (`PHASE_0_PENDING`) |
| Phase 1 (profit lock) | +1.50R = **30,839.10** | — | not armed |
| Hard SL | 31,089.10 (2.08×ATR) | untouched; a full stop costs $10.00 → equity 4,803.73 (+28.73 over the floor) | hold |
| Thesis structure | lower highs + buyer-absorption caveat | Lower-high chain intact below 31,006.91; 1H 15:00 Δ −50,208, 4H 12:00 Δ −30,711; **but** the 16:00 bar printed Δ **+10,988** (1.88× volume) with a **63.7 % lower wick** — buyers defended 30,921 | mixed → HOLD, gate-first |

Mark path since the fill: −$5.17 (−0.52R) at 16:17:37 → +$0.83 (+0.08R) at 16:19:37 → oscillating −0.25 to −0.36 → **−$0.25 (−0.03R)** now. Levels overhead: EMA50 **31,010.67**, VWAP **31,026.00**, EMA200 **31,067.50**, VAH 31,117.04.

**Slot decision (mandate Section 2: "Exactly ONE risk slot available"):** the position is open, so staging anything new means two concurrent contingent losses. Joint full-stop projection: `4,813.73 − (11.04×1.25+2) − (10.00×1.25+2) = 4,783.43` → **$11.57 below the 4,795 operating threshold**, $8.43 above the 4,775 hard floor. **Council recommendation: rotate, don't stack** — closing #18703132 at ≈ −$0.25 (0.03R) frees a clean, unencumbered slot at negligible cost; then punch exactly one stage below. If the desk instead accepts the joint-fill projection, punch one — never both.

---

## 2. MARKET STATE AT 16:33 — AFTER THE 16:17 THRUST

* **The thrust has fully retraced.** NAS100 30,944 → 31,041 (16:17) → 30,993 (16:30 close) → 30,990.79; the cross-asset impulse (SP500 +17.1, GER40 +76, DJ30 +134, USWTI −1.70, GOLD +16.9, BTC +0.43 %) left no directional follow-through; USWTI is the exception (mid 92.19, −1.5 % off its pre-thrust level, EMA20 93.42 now 2.22 ATR overhead in a "BULLISH"-labelled regime).
* **Equities:** SP500 7,781.66 (z +0.33, above VWAP), NAS100 30,990.79 (z −0.44), GER40 24,894.00 (z −0.29), DJ30 51,083.10 (z +0.95, RSI 61.4). Only NAS100/GER40 remain below their session VWAPs.
* **Crypto: flush recovering, not re-accelerating.** Every asset is off its low (BTC 81,139 with z −2.15; ETH 2,424 z −2.38, RSI 18.3; SOL 108.48 z −2.16, RSI 25.4) and taker CVD is decelerating on SOL (0.707), ETH (0.644), NEAR (0.715), ADA (0.560) — but **not** on BTC (1.869, last minute −$9.8 M).
* **FX:** EURUSD/GBPUSD/USDJPY all within ±0.5 ATR of their VWAPs, 200-EMA slopes ≤ |0.01 %| — no established trend (mandate Section 4 requires one).

---

## 3. MODEL 2 (TREND-FOLLOWING) — SCORED, ZERO PUNCHABLE

**Track 1 bar table** (briefing Section-5 bars 15:30 / 15:45 / 16:00; upper-wick % of range · volume ÷ 20-bar average · delta):

| Asset | 15:30 | 15:45 | **16:00 (operative)** | In-band shelf above mid | Verdict |
|---|---|---|---|---|---|
| **NAS100.p** | 8.4 % (2.23×) | 22.9 % (2.02×) | **35.0 % (1.88×) Δ+10,988** | EMA50 31,010.67 (**+0.333 ATR**) | gate **passes** but asset occupied (we are short from 30,989.10) |
| **GOLD** | **35.4 % (0.92×)** | 14.6 % (0.95×) | 11.7 % (1.07×) | EMA20 4,120.68 (+0.246) / EMA50 4,122.04 (+0.39) | geometry ✓, **sizing infeasible**: SL ≥ 1.5×ATR = 13.97 → risk $13.97 > floor ceiling 13.38 |
| **GER40.p** | 10.5 % (0.99×) | 15.3 % (0.72×) | 7.4 % (**0.53×**) | VWAP 24,918.29 (+0.557) / EMA50 24,920.80 (+0.592) | geometry ✓, **wick gate FAILS** (no bar ≥ 30 %) — scored `WICK GATE FAILS` |
| SP500.p | 16.6 % (1.30×) | **40.9 % (1.06×)** | 28.2 % (0.91×) | none — EMA20 7,774.09 / EMA50 7,777.14 / VWAP 7,777.74 all **below** mid | no sell shelf inside 0.10–0.60 ATR (VAH 7,792.94 = +1.28) |
| DJ30.p | 4.2 % (1.20×) | 22.9 % (1.10×) | 22.3 % (0.98×) | none — all EMAs/VWAP below mid (−1.43 / −1.60 / −1.84) | no shelf; RSI 61.4, z +0.95 → no established bearish trend |
| USWTI.p | **38.5 % (1.37×)** | 18.2 % (1.09×) | 0.0 % (1.18×) | EMA50 92.87 (+0.752) / VWAP 92.66 (+0.752) | price collapsed below all shelves — no in-band retest |
| SILVER | **33.3 % (0.97×)** | 20.0 % (0.90×) | 4.3 % (1.01×) | EMA20 58.925 (**+0.00**) | shelf at market (outside band); min-lot risk $18.10 > ceiling |
| USDJPY | 14.3 % | **33.3 %** | 0.0 % | EMA50 +0.025 (at market) | no shelf inside the band; slope +0.005 % = no trend |
| EURUSD / GBPUSD | 2-dp briefing prints ⇒ wick geometry **unverifiable** | | | GBPUSD EMA50 +0.40 (only in-band shelf) | GBPUSD scored low-conviction (§5 alt) |

**Model-2 conclusion (stated plainly per the mandate):** the desk should **not** force a trend-following entry this round. The index/crypto bear trends are real but stretched **away** from their shelves (crypto sits 1.6–3.7 ATR below its 20-EMAs, indices sit on/above their own), so the ATR-scaled micro-pullback entries the mandate asks for simply do not exist on the current tape. The one clean Model-2 short (NAS100 at the 50-EMA) is already held via #18703132; the next-best (GER40 at VWAP/EMA50) does not have a single ≥ 30 % rejection bar in the window.

---

## 4. MODEL 1 (MEAN-REVERSION) — CRYPTO, 12-RECEIPT PERSISTENCE

Persistence table (12 consecutive 1-minute receipts, 16:19:37 → 16:33:37; limbs: **a** = top-20 imbalance ≥ 1.25×, **b** = ±0.50 ATR band ≥ 150 k (strict 300 k), **c** = 1m CVD decel/flip):

| Asset | z / RSI | limb a (skew range) | limb b (band range, $k) | limb c (decay) | Verdict |
|---|---|---|---|---|---|
| **SOLUSD.p** | **−2.16** / 25.4 | ✗ (0.80–1.18) | **✓ 4,049–5,263 (12/12)** | **✓ 0.707** | **VIABLE — strongest (band depth 13–35× the floor, walls 108.37–108.42 with 60–180 s spans)** |
| **ETHUSD.pi** | **−2.32** / 18.3 | ✓ (0.19–7.68, **fresh/unstable**) | ✓ 92–2,752 (last 582) | **✓ 0.644** | **VIABLE — all three limbs, but the book is whipsawing (single-sample spikes)** |
| **NERUSD.p** | −1.88 / 29.7 | ✗ (0.73–1.40) | ✓ 704–1,376 | ✓ 0.715 | VIABLE (expanded cap only) — z just short of the −2.0 Model-1 threshold; RSI < 30; BUY wall 4.693 $171 k |
| BTCUSD.pi | −2.15 / 34.3 | ✓ (0.23–37.8) | ✓ 116–2,240 | **✗ 1.869 accelerating** (last 1m −$9.8 M) | reject — flow still one-way; RSI no longer < 30 |
| XRPUSD.pi | −1.71 / 29.4 | ✗ | ✓ 1,787–2,276 | ✗ 1.685 | reject (geometry + flow); also min-lot risk > ceiling |
| ADAUSD.p | −1.72 / 19.5 | ✗ | ✓ 2,646–3,567 | ✓ 0.560 | reject — min lot 1.0 × 5,000 ⇒ $20+ minimum risk, structurally unsizeable |
| AVAX / LINK / DOT / LTC / BNB / BCH / DOGE / TRX | z −0.83 … −1.70 | mostly ✗ | mostly < 150 k | mixed | reject (no extreme + no persistent absorption) |

**Model-1 conclusion:** the deep-flush longs remain the desk's edge this hour — but note the context: the flush is **healing** (all assets up off their lows) and the +1.5 % recovery since 16:14 has already eroded the stretch (SOL z −2.27 → −2.16; the entries below are pullback limits, not market chases).

---

## 5. TOP-2 LIMIT ORDER STAGES + ALTERNATES

> One risk slot. With #18703132 live, punching any stage stacks two contingent losses (joint full-stop ⇒ 4,783.43). **Preferred: close #18703132 (≈ −$0.25) first, then punch exactly one.**

**Stage A — SOLUSD.p · Track 2 · Model 1 long flush**
```
BUY LIMIT 108.20   (mid 108.48–108.57 ; entry inside the persistent Binance bid cluster 108.37–108.42)
SL 106.82          (1.38 = 1.513 x ATR 0.9118 ; below the 107.68 flush low)
TP 111.65          (3.45 = 2.50R)
0.08 lots · risk $11.04 · stressed $15.80 · post-loss 4,797.93 · spread 21 bps (G1 exempt for passive limits)
```
*Evidence:* z **−2.16**, RSI **25.4**, slope −0.61 %; ±0.50 ATR bid band **$4.05–5.26 M in 12/12 receipts** (27–35× the 150 k floor); 1m CVD last six [−260 k, −795 k, −194 k, −404 k, −371 k, −107 k] → **abs_decay 0.707**; discrete BUY walls at 108.37–108.42 ($182 k–$310 k) with 60–180 s spans. *Caveat:* limb (a) fails — the 1.25× imbalance never printed.

**Stage B — ETHUSD.pi · Track 2 · Model 1 long flush**
```
BUY LIMIT 2411.00  (sweep level under the 2,412.30 session flush low ; mid 2,424–2,427)
SL 2381.60         (29.40 = 1.513 x ATR 19.4275)
TP 2484.50         (73.50 = 2.50R)
0.37 lots · risk $10.88 · stressed $15.60 · post-loss 4,798.13 · spread 13.6 bps (exempt)
```
*Evidence:* the **deepest stretch on the board** — z **−2.32**, RSI **18.3**; all three flow limbs: skew 4.76 ×, ±0.50 ATR bid $582 k, 1m CVD abs_decay 0.644. *Caveat:* ETH's book is the least stable of the set (bid band 92 k → 2,752 k → 582 k → 164 k across 12 receipts; the 4.76× imbalance and the $451 k wall at 2,423.72 are single-sample) — hence second, not first.

**Alternates (validated, same table):** NERUSD.p BUY 4.6930 / SL 4.561 / TP 5.023 / 1.0 lot / risk **$13.20** / 2.50R (expanded cap only — post-loss 4,795.23, the tightest admissible margin on the floor) · GBPUSD.pi SELL 1.3209 / SL 1.32257 / TP 1.31670 / 0.06 lots / risk $10.02 / 2.515R (Model 2, **low conviction**: EMA50 shelf in band, but the rejection-wick evidence is unverifiable in the 2-dp FX prints) · GER40.p SELL 24,918.30 / SL 25,018.30 / TP 24,668.30 / 0.01 lot / risk $10.00 / 2.50R (Model 2, scored **wick-gate fails** — punch only if the desk waives its own wick gate) · NAS100.p SELL 31,010.67 / SL 31,110.67 / TP 30,760.67 / 0.01 lot / risk $10.00 / 2.50R (**conditional**: only if #18703132 is closed first).

All six plans in `docs/trade_plans/ARENA_LIMIT_STAGES_20261008_1628.json` re-validated through `Terminal/Headless/stage_trade_plan.validate_plan` (risk ✓, TP 2.50–2.515R ✓, SL ≥ 1.50×ATR ✓ — SOL/ETH at 1.513, NEAR 1.505, tick/step ✓, floor ✓).

---

## 6. PROTOCOL

1. **#18703132: HOLD.** Do not touch until the 16:30–16:45 bar closes. If it closes **≥ 30,999.62** ⇒ market cut (thesis dead); if it closes back **< 30,983** ⇒ the failed-sweep read is confirmed and the ratchet ladder governs (Phase 0 arm 30,909.10 → SL 30,974.10; Phase 1 arm 30,839.10 → SL 30,909.10; TP 30,739.10, extend only with SL locked ≥ +1.50R).
2. **Rotate, then stage one.** Closing the NAS100 short at ≈ −0.03R costs ~$0.25 and removes the 4,783.43 joint-fill exposure; then punch **Stage A or Stage B — never both, and never alongside the live short** without explicitly accepting that projection.
3. **Model 2 stands by.** If GER40 prints a ≥ 30 % rejection wick on ≥ 0.8× volume at 24,918–24,921, or NAS100 frees its slot with the 50-EMA shelf still intact, those become the trend-following punch.
4. Re-verify live at submission: quote/spread, recomputed ATR/VWAP, broker-native stop valuation, blackout calendar (FOMC window closed 2026-10-07 18:30 UTC). Fail-closed on any check failure. **No MT5 action taken by Arena.**

---

*Artifacts: `artifacts/arena_dual_track_scan_20261008_1628.json` (scanner v2, 24 assets) · `artifacts/arena_depth_persistence_20261008_1628.json` (12 receipts × 10 crypto assets: mid, z, band, skew, walls + spans) · `artifacts/arena_briefing_bars_20261008_1628.json` (15:30/15:45/16:00 bars with wick/volume/delta recomputation) · `docs/trade_plans/ARENA_LIMIT_STAGES_20261008_1628.json` · receipt `ee38345`.*
