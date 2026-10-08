# Arena.ai — 24-Asset Dual-Model Ruling + Live Position Review
## Briefing 2026-10-08 16:59:22 UTC · branch `arena/24eb818b-trading-2` · receipt `1c561cd` (snapshot as_of 16:59:49 UTC)

**Desk state at 16:59:37:** equity **4,839.40** | balance **4,838.99** | margin used 446.04 | free margin 4,393.36 | capacity **1/2 filled** | **1 open position — #18706769 ETHUSD.pi LONG 0.37 @ 2,411.00** (SL 2,381.60 / TP 2,484.50, mark **+$0.41 / +0.04R**, `PHASE_0_PENDING`, opened 16:56:55) | 0 pending | hard floor 4,775.00 | operating buffer 4,795.00 (headroom +44.40) | auth flag `DENIED_UNVERIFIED_ORDERFLOW`
**Panel identity: the mandate's §2/§3 panel (balance 4,838.99 / equity 4,839.58 / "100 % Cash Flat") = receipt `1dfc2ec` @16:58:37.** Its own §3 shows the live ETH long, and telemetry reports margin used 446.04 — the "0.00 / 100 % flat" line is stale by one minute and contradicts §3; this ruling honours **telemetry + §3**, per the standing interpretation.
**Closed since the last council:** **#18703132 NAS100.p SHORT exited at TP 30,739.10 — realised +$25.00 (+2.50R)**, balance 4,813.99 → 4,838.99. The 16:13 / 16:28 / 16:43 HOLD rulings never saw the 30,999.62 gate trigger; Phase-0 BE locked at 16:47:37, Phase-1 at 16:49:37, TP filled between 16:55:37 and 16:56:37.
**Author:** Arena.ai — read-only. No broker I/O; nothing staged, modified or cancelled.
**Reference-integrity flag:** mandate §1's `.agents/rules/ACTIVE_CONTEXT.md` **does not exist** on this branch or on `main` (404) — no such path is tracked in the repository.

---

## 0. RULING

```
#18703132 NAS100.p SHORT  →  EXITED AT TP.  +$25.00 (+2.50R) realised. Whole ladder paid: BE 16:47:37, Phase-1 16:49:37, TP 16:55-16:56.
#18706769 ETHUSD.pi LONG  →  HOLD.  Ladder: 2434.52 arm -> SL 2415.41 | 2455.10 arm -> SL 2434.52 | TP 2484.50.
    Emergency shelf cut only on a 15m CLOSE < 2405.00 (flush-low shelf 2412.30 fails). Mark +0.04R, risk $10.88.

MODEL 2 (TREND-FOLLOWING) — ACTIVE, and this tape finally has a compliant crypto trend entry:
    SOLUSD.p  SELL LIMIT 107.72  (retest of the broken 16:15-low shelf 107.78, +0.20 ATR, ON the $1.08M SELL wall 107.72; regime bearish slope -0.63%)
    SP500.p   SELL LIMIT 7772.57 (retest of the broken 16:30 bar low; that bar printed a 30.4 % upper wick on 1.154x volume, Delta -11,944)
    GOLD / GER40 alternates; EURUSD / GBPUSD / USDJPY / NAS100 / DJ30 / SILVER / USWTI fail a gate (reasons tabulated)

MODEL 1 (MEAN-REVERSION) — crypto only (RSI < 30), all sizeable candidates listed; SOL/ETH/BTC carry |z| >= 2.0:
    NEARUSD.p  LONG 4.6270 / SL 4.498 / TP 4.950 / 1.0 lot / risk $12.90   (wall $222k + band $820k-1.39M 13/13)
    DOGUSD.p   LONG 0.0820 / SL 0.0806 / TP 0.0855 / 1.0 lot / risk $14.00  (180-s double wall $186k + $280k - the only >=180 s whale wall on the board)
    BTCUSD.pi  LONG 80,800 / SL 80,142 / TP 82,445 / 0.02 lots / risk $13.16 (z -2.38; thin bid band + $530k overhead SELL wall - flagged)
    ADA (RSI 16.31) and XRP are UNSIZEABLE: their minimum-lot risk ($23.25 / $19.35) exceeds the 15.00 cap - no legal blueprint exists.

TOP-2 STAGES (punch ONE):  A) SOLUSD.p SELL LIMIT 107.72 / SL 109.10 / TP 104.27 / 0.08 lots / risk $11.04 / 2.50R
                           B) SP500.p  SELL LIMIT 7772.57 / SL 7788.00 / TP 7733.90 / 0.07 lots / risk $10.80 / 2.506R
SLOT GOVERNANCE: ETH long holds slot 1 of 2. Joint full-stop with the heaviest alternate (DOGE): 4,804.30 USD - 9.30 above the buffer.
    With Stage A or B: 4,808.00-4,808.30. ONE new stage is affordable; two are not (multi-order staging stays prohibited).
```

---

## 1. SECTION 3 — POSITION REVIEWS

### 1a. #18706769 — ETHUSD.pi LONG 0.37 @ 2,411.00 → **HOLD**

| Parameter | Value | Read |
|---|---|---|
| Entry / SL / TP | 2,411.00 / 2,381.60 / 2,484.50 | risk 29.40 pts = **$10.88**; SL 1.52×ATR (19.36); TP +2.50R |
| Mark path | −0.07R (16:56:37) → 0.00R (16:57:37) → **+0.05R** (16:58:37) → **+0.04R** (16:59:37) | flat, mid 2,409.0 → 2,412.1 |
| ETH tape | z **−2.20**, RSI **16.83** (deepest on the board), mid 2,412.70 | the flush thesis is intact |
| Intraday flow | 15M Δ: 16:00 **−1,526** → 16:15 **−19** → 16:30 **+330** | seller pressure decaying, taker flow flipped positive — constructive |
| 4H / 1H | 4H 16:00 bar Δ −1,215 (CVD −1,180); 1H 16:00 Δ −1,215 | no reversal confirmation yet — the trade needs the ladder, not bravery |
| Overhead | **SELL wall 2,415.21 $534,438** (+0.13 ATR), then e20 2,480.4 (+3.49 ATR), e50 2,518.0 (+5.44) | the first bounce is capped ~0.9R short of Phase-0; expect work to reach the arms |
| Structure | flush low 2,412.30 (16:00 bar) swept to ~2,409 (16:56) then reclaimed | entry sits on the shelf; the sweep-and-reclaim is the thesis |

**Ratchet ladder (identical convention to the reviewed NAS100 trade):**
* **Phase 0:** arm at **2,434.52** (+0.80R) → SL to **2,415.41** (+0.15R, BE+buffer).
* **Phase 1:** arm at **2,455.10** (+1.50R) → SL to **2,434.52** (+0.80R).
* **Target:** TP 2,484.50 (+2.50R). Extend only with SL locked ≥ +1.50R.
* **Emergency shelf cut:** a **15m CLOSE below 2,405.00** (≈0.4 ATR under the flush low) ⇒ exit at market — the shelf failed; that saves ≈1.1R against the hard SL.
**Resting orders: NONE** (the desk's pending list is empty; no Arena order was ever left on the book). **Verdict: HOLD, manage with the ladder.**

### 1b. #18703132 — NAS100.p SHORT → **CLOSED AT TP (post-mortem, +2.50R)**

The trade that dominated the last four councils resolved cleanly: gate 30,999.62 never reclaimed (16:30–16:45 bar closed ≈ 30,944.5), Phase-0 BE locked at 16:47:37, Phase-1 at 16:49:37, and the TP at 30,739.10 filled between 16:55:37 (mid 30,782.16) and 16:56:37 (mid 30,741.57). **Realised +$25.00 on 0.01 lot** — the full 2.50R, balance 4,813.99 → 4,838.99. **Lesson for the book:** the piecewise ratchet plus "do not cut on the gate bar" was worth 2.5R versus the −0.03R rotate-at-breakeven alternative that the 16:28 council had offered; and the same ladder is now armed on the ETH long.

---

## 2. MARKET STATE AT 16:59 — THE FLUSH DEEPENED ONE MORE LEG

* **Indices:** NAS100 30,740.82 (**z −3.07**, RSI 30.26, ATR 69.53 — the biggest stretch on the board), SP500 7,754.95 (z −1.81, RSI 37.97), GER40 24,878.50 (z −0.46), DJ30 51,100.15 (z +1.01, RSI 64.03 — the only asset still up). The 16:30 15m bars were heavy sellers: NAS100 Δ **−26,870**, SP500 Δ **−11,944**.
* **Crypto:** the whole complex is 2σ–2.4σ under its session VWAP, and each asset is 2–6 ATR below its 20/50 EMA and VWAP: BTC z −2.38 (RSI 29.96), ETH −2.20 (16.83), SOL −2.27 (21.44), BNB −1.92 (15.99), XRP −1.98 (25.92), ADA −1.90 (16.31), NEAR −1.99 (25.99), AVAX −1.94 (23.63), DOGE −1.41 (18.23), LINK −1.85, BCH −1.89, DOT −1.84, LTC −1.47, TRX −0.97. Every asset is *below* every moving average — bearish trend still intact; the mean-reversion case rests on stretch + absorption, not on structure.
* **Metals / oil:** GOLD 4,123.62 (z −0.07, back on VWAP/POC after a 45 % rejection wick at 4,122.65 on 1.22× volume); SILVER 58.873 (z −0.79); USWTI 92.246 — post-flush chop (z −0.34, POC 3.8 ATR below, regime label BULLISH on a +0.236 % 200-EMA slope yet price 5.6 ATR under VAL).
* **FX:** EURUSD 1.1196 (z +0.20), GBPUSD 1.3214 (z +0.70), USDJPY 157.989 (z −0.73, RANGE_BOUND) — no trend, no compliant shelf.

---

## 3. MODEL 2 (TREND-FOLLOWING) — SCORED ON THE 16:59 TAPE

Geometry: 0.10–0.60 ATR micro-pullback to a 20/50 EMA, prior 15m/1H broken structure, VAH/VAL, or FVG/high-volume node. **Track 1 (CFD):** 15m volume ≥ 0.8× 20-bar avg **and** rejection wick ≥ 30 % at the shelf. Track-1 evidence is computed from the mandate's **16:30 bars** (the operative last closed bar) — `artifacts/arena_briefing_bars_20261008_1659.json`.

| Asset | Shelf (distance from mid) | 16:30 bar wick / vol | Verdict |
|---|---|---|---|
| **SOLUSD.p** (Track 2) | broken 16:15 low **107.78 → SELL wall 107.72** (+0.20 ATR) | n/a (crypto track) | **PASS — Stage A.** Legs: ask band $ ≥150 k in 13/13 receipts; CVD not decelerating (1/13 decel — trend leg intact). Regime bearish (slope −0.63 %), price 3.2/5.4/6.2 ATR below e20/e50/VWAP |
| **SP500.p** | broken 16:30 bar low **7,772.57** (+1.74 ATR — flagged outside the 0.10–0.60 band; the tape ran away from every shelf) | **uw 30.4 %**, vol **1.154×**, Δ −11,944 | **PASS — Stage B** (band-distance flag) |
| **XAUUSD.pi** | **VAH 4,126.91** (+0.36 ATR; just above VWAP 4,124.12 / POC 4,123.90) | **uw 45.2 %**, vol **1.224×** | PASS but **regime is flat** (slope −0.02 %) — expanded cap only, weak trend premise |
| **GER40.p** | POC/high-volume node **24,881.22** (+0.06 ATR) | uw **26.0 % (< 30 %)**, vol 1.343× ✓ | marginal — wick-gate waiver required |
| USWTI.p | VWAP 92.63 (+0.74 ATR — outside band) | uw 67.2 %, vol 1.58× ✓ | band fail; watch only |
| GBPUSD.pi | VAH 1.3226 (+0.40 ATR) | **prints unverifiable** (2-dp) | stand by |
| EURUSD.pi | VAH 1.1209 (+1.44 ATR) | unverifiable | stand by — no trend |
| USDJPY.pi | VAL 157.971 (−0.18 ATR, long) | lw **20.0 %** (<30 %), vol 0.96× | fail — RANGE_BOUND |
| NAS100.p | e20 30,959 (−3.14 ATR) / VAL 30,722 (−0.27) | uw 18.2 %, lw 17.9 % | **fail both wick legs** — despite |z| 3.07 (the deepest stretch on the board, but Track 1 still demands the wick) |
| DJ30.p | VAH 51,224 (+1.59 ATR) | uw 24.5 % (<30 %) | fail |
| SILVER | e20 58.916 (+0.19 ATR) | uw 36.8 %, vol 0.96× | desk's standing asset set excludes silver |
| TRXUSD.p (crypto M2) | VAL 0.3335 (+0.60 ATR) | — | fails flow (skew 0.71 ask-side but band $126 k < 150 k, no wall) |

**Answer to "must not sit idle":** a compliant Model-2 trend entry now exists — **SOL at the 107.72 shelf/wall confluence** (Stage A) — and a second CFD retest entry at **SP500 7,772.57** (Stage B). Crypto Model-2 shorts higher up the book (NEAR 4.67 broken structure, LTC 62.21) are listed as watches but lack wall confluence.

---

## 4. MODEL 1 (MEAN-REVERSION) — CRYPTO, 13-RECEIPT DEPTH PERSISTENCE

Window **`c1b8f43` @16:50:37 → `1c561cd` @16:59:49, 13 receipts × 14 assets = 182 records** (`artifacts/arena_depth_persistence_20261008_1659.json`). Band = top-20 notional inside mid ±0.5×ATR.

| Asset | z / RSI | ±0.5 ATR bid band (13 receipts) | Skew range | CVD (last) | Walls (USD, span) | Verdict |
|---|---|---|---|---|---|---|
| **SOLUSD.p** | −2.27 / **21.44** | **$3.18 M – 5.46 M, 13/13** | 0.741–1.369 | 3m −0.75 M, decay 0.296, decel 1/13 | **BUY stack 107.44–107.59 ($0.17–0.82 M each)**; SELL stack 107.71–107.72 ($0.44 M / **$1.08 M**) | **dual-sided: M2 short wins** (wall confluence); M1 long exists as the mirror (see §5 note) |
| **NEARUSD.p** | −1.99 / 25.99 | $0.82 M – 1.39 M, 13/13 | 0.716–1.628 | decay min 0.062 | BUY 4.627 ($222 k, **60 s**), 4.617 ($196 k) | viable M1 long |
| **DOGUSD.p** | −1.41 / **18.23** | $1.04 M – 1.79 M, 13/13 | 0.709–1.394 | decay min 0.369 | **BUY 0.0820 ×2 ($185,880 + $280,387, both span 180 s)** | viable M1 long — the only ≥180 s whale wall on the board |
| **BTCUSD.pi** | **−2.38** / 29.96 | $79 k – 2.09 M (9/13 pass), last $113 k | 0.115–15.1 (spikes) | 3m −6.4 M | **SELL 80,902.4 ($530 k)** overhead | viable but flagged (thin bid band + sell wall) |
| ADAUSD.p | −1.90 / **16.31** | $1.72 M – 2.86 M, 13/13 | 1.019–1.366 | decay min 0.457 | BUY 0.2268 ($183 k, 60 s) | **UNSIZEABLE** (min-lot risk $23.25 > 15.00) |
| XRPUSD.pi | −1.98 / 25.92 | $0.95 M – 2.53 M, 13/13 | 0.615–1.681 | 3m +0.34 M (buyers) | SELL 1.3430/1.3435 ($170 k/$154 k) | **UNSIZEABLE** (min-lot risk $19.35 > 15.00) |
| ETHUSD.pi | −2.20 / 16.83 | $67 k last (7/13 pass) | 0.104–5.658 | 3m −27.5 M | SELL 2,415.21 ($534 k) | **already held long** — no second position |
| BNBUSD.p | −1.92 / **15.99** | $22 k last (6/13 pass) | 0.083–5.728 | decay min 0.080 | — | fails depth floor |
| LINK / LTC / AVAX | −1.85 / −1.47 / −1.94 | $141 k–226 k / $368–460 k / $132–234 k | mixed | — | — | depth OK, |z| < 2.0 and RSI > 25 — sub-threshold |
| BCH / DOT / TRX | −1.89 / −1.84 / −0.97 | $29 k / $58 k / $126 k | — | — | — | fail the 150 k depth floor |

*Method note:* single-receipt skew spikes (BTC up to 15.1, BNB 5.7, ETH 5.7) are Binance book-refresh artifacts; only multi-receipt persistence is used for ranking, and index/commodity/FX assets have no whale/CVD feed (never scored on them).

---

## 5. TOP-2 LIMIT ORDER STAGES + ALTERNATES

**Stage A — SOLUSD.p · Track 2 · Model 2 trend-following short (shelf + wall confluence)**
```
SELL LIMIT 107.72  (broken 16:15-low shelf 107.78 / 16:00 low 107.68; ON the largest resting wall in the book - SELL 107.72 = $1.08 M, with 107.71 $444 k behind it)
SL 109.10          (1.38 = 1.501 x ATR 0.9192  — above the 107.78/107.82 structure and the cheap side of the wall stack)
TP 104.27          (3.45 = 2.50R)
0.08 lots · risk $11.04 · stressed $15.80 · post-loss 4,828.36 · spread 24 bps (G1 exempt for passive limits)
```
*Evidence:* regime BEARISH (200-EMA slope −0.63 %), price below e20/e50/VWAP by 3.2/5.4/6.2 ATR; Track-2 flow legs **b** (ask-side band ≥ $150 k in 13/13 receipts) and **c** (CVD not decelerating: only 1/13 receipts) satisfied; entry is 0.20 ATR above mid so the order rests passively. *Alternate framing (desk's choice, never both):* the mirror **M1 long** at the buy stack — BUY LIMIT 107.50 (the $817 k wall) / SL 106.12 / TP 110.95 / 0.08 lots / risk $11.04 / 2.50R — rejected as the primary because the **$1.08 M SELL wall at 107.72 sits 0.2 ATR overhead** and caps the first bounce.

**Stage B — SP500.p · Track 1 · Model 2 trend-following short (broken-structure retest)**
```
SELL LIMIT 7772.57  (the 16:30 bar low, now resistance; mid 7754.95 -> entry +1.74 ATR above market - BAND FLAG)
SL 7788.00          (15.43 = 1.52 x ATR 10.1518  — above the 16:30 close 7774.31 and the 16:45 supply shelf)
TP 7733.90          (38.67 = 2.506R)
0.07 lots · risk $10.80 · stressed $15.50 · post-loss 4,828.60 · spread 0.99 bps
```
*Evidence:* the operative 16:30 bar rejected from 7,783.30 with a **30.4 % upper wick on 1.154× volume and Δ −11,944** (Track-1 gate PASS); the regime is bearish (slope −0.015 %), price is 1.7–2.2 ATR under e20/e50/VWAP; 48H POC 7,770.41 / VAL 7,761.57 have already failed, so the TP is a momentum continuation target. *Caveat:* the entry sits 1.74 ATR above the current mid — outside the preferred 0.10–0.60 micro-pullback band — because the tape has run away from every shelf; the desk may prefer to wait for a shallower retest (7,760–7,765 zone) rather than stage the deeper retest.

**Alternates (validated, same table):** XAUUSD.pi SELL 4,126.91 / SL 4,140.74 / TP 4,092.20 / 0.01 lot / risk **$13.83** / 2.51R (**expanded-only**; 16:30 bar 45.2 % wick on 1.224× volume; flat regime) · GER40.p SELL 24,881.22 / SL 24,981.22 / TP 24,631.22 / 0.01 lot / risk **$10.00** / 2.50R (**wick-gate waiver**: 26.0 % < 30 %) · NERUSD.p BUY 4.6270 / SL 4.498 / TP 4.950 / 1.0 lot / risk **$12.90** / 2.504R (**expanded-only**) · DOGUSD.p BUY 0.0820 / SL 0.0806 / TP 0.0855 / 1.0 lot / risk **$14.00** / 2.50R (**expanded-only**; 180-s double wall; spread 268 bps G1-exempt) · BTCUSD.pi BUY 80,800 / SL 80,142 / TP 82,445 / 0.02 lots / risk **$13.16** / 2.50R (**expanded-only**; thin bid band + overhead sell wall).

All seven plans in `docs/trade_plans/ARENA_LIMIT_STAGES_20261008_1659.json` validated through `Terminal/Headless/stage_trade_plan.validate_plan` — risk window ✓, TP ≥ 2.50R ✓ (2.500–2.510), SL ≥ 1.50×ATR ✓ (1.500–2.327), tick/step ✓, floor ✓. **None is staged; the desk executes.**

**Risk-envelope conflict (standing):** mandate §2 caps nominal risk at 10.00–11.04 (stressed ≤ 15.80) while mandate §6 permits ≤ 15.00. Both floor ceilings are non-binding at this equity (equity-basis 31.71, balance-basis 33.59), so **§6's 15.00 is today's binding cap**; Arena still prefers ≤ 11.04 and flags every plan above it **expanded-only**.

---

## 6. PROTOCOL

1. **#18706769 ETH long: HOLD, manage with the ladder.** Arms 2,434.52 → SL 2,415.41; 2,455.10 → SL 2,434.52; TP 2,484.50; emergency market cut only on a 15m close < 2,405.00. Do not add to it (one position per asset).
2. **Punch ONE top-2 stage** — the ETH long holds slot 1 of 2; capacity and the joint-stop projection (4,804.30–4,808.30 ≥ 4,795) permit exactly one new order. Never two new orders; multi-order staging remains prohibited.
3. **Delete criteria before the fill:** Stage A — delete if the $1.08 M wall at 107.72 thins > 50 % or price drifts > 2.0×ATR (≈1.84 pts) away; Stage B — delete if a 15m bar closes > 7,788 or price drifts > 2.0×ATR (≈20 pts) from 7,772.57.
4. **Crypto M1 rotation order (if the desk prefers the long side):** NEAR → DOGE → BTC. ADA/XRP stay excluded on min-lot risk; BNB/BCH/DOT/TRX stay excluded on depth; ETH is already held.
5. Re-verify live at submission: quote/spread, recomputed ATR/VWAP, broker-native stop valuation, blackout calendar (FOMC window closed 2026-10-07 18:30 UTC). Fail-closed on any check failure. **No MT5 action taken by Arena.**

---

*Artifacts: `artifacts/arena_dual_track_scan_20261008_1659.json` (scanner v2, 24 assets, ref `1c561cd`) · `artifacts/arena_depth_persistence_20261008_1659.json` (13 receipts × 14 crypto assets = 182 records) · `artifacts/arena_briefing_bars_20261008_1659.json` (16:15/16:30 bars with wick/volume/delta recomputation) · `artifacts/arena_position_tape_20261008_1659.json` (NAS100 exit + ETH fill tape) · `docs/trade_plans/ARENA_LIMIT_STAGES_20261008_1659.json` · receipts `1dfc2ec` (16:58:37, briefing panel) and `1c561cd` (16:59:49, operative).*
