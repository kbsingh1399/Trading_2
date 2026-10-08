# Arena.ai — 24-Asset Dual-Model Ruling + Live Position Review
## Briefing 2026-10-08 16:43:35 UTC · branch `arena/24eb818b-trading-2` · receipt `ef34f73` (snapshot as_of 16:45:37 UTC)

**Desk state at 16:45:37:** equity **4,818.35** | balance 4,813.99 | margin used 309.89 | free margin 4,508.46 | margin level 1,554.86 % | **1 open position — #18703132 NAS100.p SHORT 0.01 @ 30,989.10** (SL 31,089.10 / TP 30,739.10, mark **+$4.36 / +0.44R**) | 0 pending | hard floor 4,775.00 / operating threshold 4,795.00 | auth flag `DENIED_UNVERIFIED_ORDERFLOW`
**Briefing-panel identity:** the mandate's §2/§3 panel (balance 4,813.99 / equity 4,817.07 / "100 % cash flat" / mark "+0.31R") is receipt **`8919ed7` @16:42:37** — 3 minutes stale at publication. Its own §3 (live short) contradicts its "flat" claim; this ruling honours **telemetry + §3**, per the standing interpretation.
**LIVE ADDENDUM (post-briefing, receipt `18f7cab` @16:49:37):** equity **4,830.70** | #18703132 mark **+$16.71 / +1.67R** (price 30,842.76, mid 30,842.76) | ratchet **`PHASE_1_PROFIT_LOCKED`** — Phase-0 BE arm (30,909.10) fired at ~16:47:37 and Phase-1 (+1.50R, 30,839.10) at 16:49:37. **Flag: the broker-SL field still prints 31,089.10 in every receipt — verify in MT5 that the Phase-0/1 stop modifications actually landed before treating the locked profit as realised risk reduction.**
**Author:** Arena.ai — read-only. No broker I/O; nothing staged, modified or cancelled.

---

## 0. RULING

```
POSITION #18703132 (NAS100.p SHORT 30,989.10)  →  HOLD  (ratchet ladder armed; no cut, no close)
    · invalidation gate (15m close >= 30,999.62) NOT triggered: the 16:30–16:45 bar closed ~30,944.5 (55 pts / 0.96 ATR below the line)
    · failed-sweep read CONFIRMED (close < 30,983); mark +0.44R (+$4.36); Phase-0 BE arm 30,909.10 sits 35 pts below price

MODEL 2 (TREND-FOLLOWING) — 1 institutional punch, genuinely re-scored on the 16:43 tape:
    SP500.p  SHORT  (EMA50 7,777.03 / VWAP 7,777.71 cluster, +0.27..+0.34 ATR)
                    Track-1 PASS on the operative 16:15 bar: 66.9 % upper wick, vol 1.946x avg, Delta -10,115 → 2.50R, risk $10.56
    GOLD / GER40   SELL alternates (GOLD = expanded cap only, 13.78 > scanner window 13.50; GER40 shelf 0.66 ATR, marginally outside the 0.60 band)
    EURUSD / GBPUSD / USDJPY  stand by — shelves exist but rejection-wick gate fails (12.2 / 23.8 / 1.5 % upper wicks; vol 0.90 / 0.91 / 0.74x)

MODEL 1 (MEAN-REVERSION) — crypto flush still live, 5 sizeable candidates (G1 spread exempt for passive limits):
    SOLUSD.p   LONG 108.58 / SL 107.21 / TP 112.01 / 0.08 lots / risk $10.96 / 2.504R  (legs b+c, 13/13 band persistence, deepest stable book)
    ETHUSD.pi  LONG 2411.00 / SL 2381.60 / TP 2484.50 / 0.37 lots / risk $10.88 / 2.50R (legs a+b+c at ref receipt; book whipsaw 0.28-70.6x)
    NERUSD.p   LONG 4.6890 / SL 4.557 / TP 5.019 / 1.0 lot / risk $13.20 / 2.50R      (expanded cap only)
    AVXUSD.p   LONG 9.9800 / SL 9.78 / TP 10.48 / 0.50 lots / risk $10.00 / 2.50R
    DOGUSD.p   LONG 0.0829 / SL 0.0815 / TP 0.0864 / 1.0 lot / risk $14.00 / 2.50R     (expanded cap only; 253 bps spread — G1 exempt)
    ADAUSD.p is EXCLUDED: min-lot contract floor (1.0 lot x 5,000 x 1.5 ATR = $22.50) is 1.5x the 15.00 cap — unsizeable, no blueprint possible.

TOP-2 STAGES (ready to punch, ONE only):  A) SP500.p SELL LIMIT 7,777.40   B) SOLUSD.p BUY LIMIT 108.58
SLOT GOVERNANCE: at the 16:45:37 receipt the slot was blocked — joint full-stop of #18703132 + Stage A projected
    4,793.15 (below the 4,795 threshold; Stage B 4,792.65). The 16:47–16:49 ratchet changes this: with Phase-1
    locked (SL 30,909.10 ⇒ +$8.00 worst case) the joint-stop now projects 4,830.70 + 8.00 − 15.20 (Stage A) = 4,823.50
    and − 15.70 (Stage B) = 4,823.00 — comfortably inside the buffer. CAPACITY IS LIBERATED for exactly ONE stage,
    strictly conditional on the broker-side stop modification being confirmed in MT5.
```

---

## 1. SECTION 3 — LIVE POSITION REVIEW (#18703132)

**Ruling: HOLD.** The mandate's decision tree — HOLD / piecewise ratchet (Phase-0 BE +0.80R, Phase-1 +1.50R, TP +2.50R) / emergency shelf cut / close at market — resolves on the desk's own 16:13 gate, which the 16:28 ruling left explicitly armed for the 16:30–16:45 bar:

| Gate | Level / rule | Observed | Result |
|---|---|---|---|
| **Invalidation cut** | 15m close **≥ 30,999.62** ⇒ cut at market | The 16:30–16:45 bar **closed ≈ 30,944.5** (mid 30,945.63 @16:44:37 → 30,944.48 @16:45:37; mark 30,942.98 → 30,945.53) — **55 pts / 0.96 ATR below the line** | **NOT triggered** |
| Failed-sweep confirm | 15m close **< 30,983** | closed ≈ 30,944.5 — **38.5 pts below** | **CONFIRMED** (bearish structure held on the gate bar) |
| Emergency shelf cut | 15m close back ≥ shelf (POC 30,996.00 / EMA20 30,980.88) | closed below both (POC +0.88 ATR overhead, EMA20 +0.62 ATR overhead) | not triggered |
| Phase 0 (BE arm) | +0.80R = **30,909.10** | low of the window ≥ 30,921 (16:00-bar low); mark 30,945.53 → **35 pts (0.61 ATR) from the arm** | not armed (`PHASE_0_PENDING`) |
| Phase 1 (profit lock) | +1.50R = **30,839.10** | — | not armed |
| Hard SL / TP | 31,089.10 (2.08×ATR) / 30,739.10 (2.50R) | native, untouched; full stop still costs $10.00 ⇒ equity 4,808.35 (33.35 over the floor) | hold |

**Mark path (16:35:37 → 16:45:37):** −1.40 → +0.58 → +1.28 → +2.50 → +1.70 → −0.47 → −0.31 → **+3.08** → **+4.61** (peak, 16:43:38) → **+4.36**. Equity over the same span 4,812.59 → 4,818.35; mid 30,999.38 → 30,942.70 (peak favourable) → 30,944.48.

**Structure:** lower-high chain intact — VWAP 31,024.42 (+1.38 ATR overhead, unreclaimed), EMA50 31,008.24 (+1.09), POC 30,996.00 (+0.88), VAH 31,117.04 (+2.99); support side VAL 30,874.96 (−1.24) then the TP. RSI 45.27, z −0.99, regime BEARISH (200-EMA slope −0.03 %). **Resting limits: NONE** (no add-on orders anywhere in the book; native SL/TP only) — the mandate's "resting limits NONE" clause is satisfied by inaction.

**Slot decision (mandate §2 "exactly ONE risk slot") — as measured at 16:45:37:** the slot was consumed by #18703132. Joint full-stop projections at equity 4,818.35, stressed = risk×1.25+2:
* \+ Stage A (SP500, $10.56): `4,818.35 − (10.00×1.25+2) − (10.56×1.25+2) = 4,793.15` → **$1.85 below the 4,795 threshold**, $18.15 above the floor.
* \+ Stage B (SOL, $10.96): `4,792.65` → $2.35 below the threshold.
* After a **Phase-0 ratchet** (SL → 30,974.10 ⇒ worst case +$1.50 instead of −$8.50): `4,818.35 + 1.50 − 15.20 = 4,804.65` (Stage A) / `4,804.15` (Stage B) → **inside the buffer**.
**Council recommendation: HOLD the short into the ratchet ladder, then punch exactly one of the top-2 once the stop modification is broker-confirmed — or, if the desk wants the Model-2 short *now*, close #18703132 at market (then ≈ +1.6R) and punch Stage A immediately. Never both new stages (multi-order staging is prohibited).**

### 1b. LIVE ADDENDUM — the ratchet fired (16:47:37 → 16:49:37)

| Receipt | Time (UTC) | Equity | Mid | Mark | R | `ratchet_state` |
|---|---|---|---|---|---|---|
| `a19765e` | 16:46:37 | 4,818.27 | 30,938.49 | +$4.28 | +0.43 | `PHASE_0_PENDING` |
| `2547197` | 16:47:37 | 4,823.44 | 30,891.95 | +$9.45 | +0.95 | **`PHASE_0_BE_LOCKED`** (arm 30,909.10 hit) |
| `94cf2d3` | 16:48:37 | 4,827.62 | 30,857.45 | +$13.63 | +1.36 | `PHASE_0_BE_LOCKED` |
| `18f7cab` | 16:49:37 | **4,830.70** | **30,842.76** | **+$16.71** | **+1.67** | **`PHASE_1_PROFIT_LOCKED`** (arm 30,839.10 hit) |

The failed-sweep thesis paid off fast: mid fell 30,944.48 → 30,842.76 in four minutes (z −0.99 → **−2.26**), touching the Phase-1 arm. Remaining ladder: TP 30,739.10 (2.50R) is **103 pts (1.8 ATR) below mid**; Phase-2 trailing (behind the 15m EMA20, currently ~30,980 and falling) governs after Phase-1; the desk's own Mandate-4 clause (price ≤ 30,750 with 1H Δ < −40,000 ⇒ extend TP into 30,550) is not yet live. **Two open items:** (i) the telemetry's `sl` field never moved from 31,089.10 across the whole progression — confirm the broker-side stop actually sits at 30,974.10 / 30,909.10; (ii) if the stop *did not* move and price re-runs to 31,089.10, the plan reverts to the 16:45:37 projections (4,793.15 joint-stop ⇒ no second stage).

---

## 2. MARKET STATE AT 16:43–16:45 — RISK-ON RETRACE STALLS, COMMODITIES FLUSH

* **Equities:** SP500 7,774.70 (z −0.26, below VWAP 7,777.71, POC 7,774.20); NAS100 30,944.48 (z −0.99); GER40 24,889.00 (z −0.35, below VWAP 24,917.64); DJ30 51,068.10 (z +0.83, RSI 62.0 — the only index still positive on the day). The 16:15 spike on all three indices (SP500 +22, NAS100 +105, GER40 +104, DJ30 +193) has fully retraced; SP500/GER40/DJ30 printed **66.9 / 37.5 / 78.0 % upper rejection wicks** on 1.95× / 1.70× / 1.54× volume.
* **Commodities:** GOLD 4,120.47 (z −0.53, 16:15 high 4,133.00 rejected, 64.2 % upper wick, 1.75× Δ −3,803); SILVER 58.938 (59.7 % upper wick, 1.65×); USWTI 92.05 — the day's flush leader (16:15 low 91.47, −1.5 % off the pre-thrust level, vol 2.55×, EMA20 93.31 = +2.36 ATR overhead, "BULLISH"-labelled regime with slope +0.24 % — the label contradicts the tape).
* **Crypto — flush is still the dominant state, books stable:** every asset is ≤ −1.1σ below VWAP; the deepest stretches are **ETH 18.86, BNB 18.30, ADA 18.92, DOGE 21.30, SOL 24.94, AVAX 26.45**. Taker CVD is decelerating on SOL (0.358), NEAR (0.460), LTC (0.255), BNB (0.603), TRX (0.802), BTC (0.757) — BTC's absolute flows remain the heaviest (last 3m −$6.4 M vs prev 5m −$1.9 M, i.e. re-accelerating in absolute size).
* **FX:** EURUSD 1.1194 (z −0.05), GBPUSD 1.3211 (z +0.49), USDJPY 158.1195 (z +0.07); 200-EMA slopes ≤ 0.007 % — **no established trend**, so Model 2 (trend-following) does not apply, and the wick gate fails on the last closed bar for all three.

---

## 3. MODEL 2 (TREND-FOLLOWING) — SCORED ON THE 16:43 TAPE

Mandate §6 geometry: 0.10–0.60 ATR micro-pullback into 20/50 EMA, prior 15m/1H structure, VAH/VAL, or FVG/node. Track 1 = **15m volume ≥ 0.8× 20-bar AND wick ≥ 30 % at the shelf**. (The scanner's own `flow_vol`/`flow_wick` flags lag one bar — its blocks read the 16:00 bar; the operative rejection bar is **16:15**, recomputed from the briefing in `artifacts/arena_briefing_bars_20261008_1643.json`.)

| Asset | Shelf (distance in ATR) | Track-1 evidence — 16:15 bar | Verdict |
|---|---|---|---|
| **SP500.p** | **EMA50 7,777.03 (+0.27) / VWAP 7,777.71 (+0.34)** | **66.9 % upper wick** (high 7,796.73 → close 7,780.03), vol 30,008 = **1.946×**, Δ **−10,115** | **PASS — punch** |
| **XAUUSD.pi** | **EMA50 4,121.93 (+0.31) / POC 4,123.91 (+0.52) / VWAP 4,124.17 (+0.55)** | **64.2 % upper wick** (high 4,133.00), vol 13,435 = **1.745×**, Δ −3,803 | PASS — but SL floor forces risk **13.78 > scanner window 13.50** (expanded cap only) |
| **GER40.p** | VWAP 24,917.64 (**+0.66 — 0.06 ATR outside the 0.60 band**) | **37.5 % upper wick** (high 24,940.45), vol 3,051 = **1.698×**, Δ +762 | qualified pass — band-marginal, flag |
| EURUSD.pi | EMA50/VWAP 1.1194 (0.00) | 12.2 % upper wick, 0.896× | **FAIL wick gate** — stand by |
| GBPUSD.pi | EMA20 1.3212 (+0.10) | 23.8 % upper wick, 0.908× | **FAIL wick gate** — stand by |
| USDJPY.pi | VWAP 158.108 (−0.14) | 1.5 % upper wick, 0.744× | **FAIL wick + volume** — stand by |
| XAGUSD.pi | POC 58.973 (+0.15) | 59.7 % upper wick, 1.653× | geometry pass, but **trade disabled in the desk's standing set** (silver excluded from candidates since 15:05); listed for completeness only |
| NAS100.p | EMA50 31,008.24 (+1.09) | 51.0 % upper wick, 1.453× | shelf **occupied by our own short** — no new risk |
| USWTI.p | EMA20 93.31 (+2.36, beyond band) | 1.8 % upper wick, 2.549× | **FAIL band + wick** (post-flush chop) |
| TRXUSD.p (crypto M2) | VAL 0.3336 (+0.40) | 42.9 % upper wick, 2.90× | **FAIL all three flow legs** (skew 0.92-bid-side, band $126 k <150 k, no CVD decel) |

**Model 2 is therefore NOT idle: SP500.p is a genuine, gate-complete institutional short on the 16:43 tape** (first CFD besides NAS100/GOLD to clear its own Track-1 gate since 15:05).

---

## 4. MODEL 1 (MEAN-REVERSION) — CRYPTO, 13-RECEIPT DEPTH PERSISTENCE

Persistence window **`2e524f0` @16:34:47 → `ef34f73` @16:45:37, 13 receipts × 14 crypto assets = 182 records** (`artifacts/arena_depth_persistence_20261008_1643.json`). Band = top-20 notional inside mid ±0.5×ATR.

| Asset | z / RSI | ±0.5 ATR bid band (13 receipts) | Skew ≥1.25× | CVD decay min. / decel / flip | Walls (USD, span) | Verdict |
|---|---|---|---|---|---|---|
| **SOLUSD.p** | −1.99 / **24.94** | **$3.92 M – 5.58 M, 13/13 ≥150 k** | 0/13 (max 1.198) | 0.358 / 5 / 4 | 108.67–108.68 ($154 k, $183 k); earlier 108.58–108.61 ($176 k–$365 k) | **TOP — stage B** (legs b+c; deepest *stable* book) |
| **ETHUSD.pi** | **−2.07** / **18.86** | $100 k – 25.6 M (spike), 11/13 ≥150 k, last **$296 k** | 5/13 (up to **70.6× — junk spike**) | 0.095 / 4 / 2 | none | viable — legs **a+b+c** at ref receipt, but book whipsaw ⇒ ranked below SOL |
| **NERUSD.p** | −1.79 / 28.50 | **$904 k – 1.22 M, 13/13** | 0/13 (max 1.216) | 0.298 / **7** / 4 | 4.707 ($163 k buy), 4.689/4.687 ($162–172 k) | viable — expanded cap only |
| **AVXUSD.p** | −1.67 / 26.45 | $185 k – 491 k, 13/13 | 6/13 | 0.268 / **8** / 1 | none ≥150 k persistent | viable |
| **DOGUSD.p** | −1.11 / **21.30** | $996 k – 1.86 M, 13/13 | 0/13 | 0.194 / 6 / 4 | **0.0828 ($277 k, span 120 s)**, 0.0829 ($403 k) | viable — expanded cap only, z weak, 253 bps spread (G1 exempt) |
| ADAUSD.p | −1.67 / 18.92 | $2.23 M – 3.05 M, 13/13 | 3/13 | 0.066 / 3 / 4 | 0.2307–0.2308 ($151–154 k) | geometry strong, **UNSIZEABLE** (min 1.0 lot × 5,000 × 1.5 ATR = $22.50 > 15.00 cap) |
| BTCUSD.pi | −1.87 / 34.05 | $161 k – 1.73 M | 6/13 | 0.357 / 6 / 3 | 81,299.5 ($320 k) / 81,299.6 ($322 k) | RSI >30 and z <2.0 ⇒ outside Model-1 thresholds |
| BNBUSD.p | −1.70 / **18.30** | $55 k – 285 k, **1/13 ≥150 k** | 2/13 | 0.107 / 5 / 3 | none | **FAIL depth floor** (last $87 k < 150 k) |
| XRP/LTC/LINK/BCH/DOT/TRX | −1.59 … −0.48 / 29.2–40.0 | $60 k – 2.34 M (XRP/LTC/LINK pass, BCH/DOT/TRX fail) | mixed | — | LINK 12.49 ($195 k) | RSI ≥29.2 with z > −1.7 and/or legs incomplete — **below the day's flush leaders** |

*Method note:* single-print skew is an artifact (ETH printed 70.6× intrabar); only multi-receipt persistence is used for ranking. CAD/indices have no whale/CVD feeds (structurally unavailable) — never scored on them.

---

## 5. TOP-2 LIMIT ORDER STAGES + ALTERNATES

**Stage A — SP500.p · Track 1 · Model 2 trend-following short (rejection of the 16:15 spike)**
```
SELL LIMIT 7777.40  (EMA50 7777.03 / VWAP 7777.71 cluster; mid 7774.70 -> entry 0.30 ATR above mid, passive)
SL 7795.00          (17.60 = 1.962 x ATR 8.9704  — above the 7796.73 spike high)
TP 7733.40          (44.00 = 2.50R)
0.06 lots · risk $10.56 · stressed $15.20 · post-loss 4,803.15 · spread 0.99 bps
```
*Evidence:* Track 1 **PASS** — 16:15 bar upper wick **66.9 %**, volume **1.946×** the 20-bar average, Δ **−10,115**; shelf is the EMA50/VWAP/POC triple cluster; structure = failed spike, price back below VWAP with z −0.26 and RSI 50. *Caveat:* the only shelf inside the band is the EMA50/VWAP cluster — if SP500 closes a 15m bar > 7,796.73 the setup is dead (delete).

**Stage B — SOLUSD.p · Track 2 · Model 1 long flush**
```
BUY LIMIT 108.58   (BUY-wall cluster 108.58-108.68; mid 108.655 -> entry 0.08 ATR below mid, passive)
SL 107.21          (1.37 = 1.503 x ATR 0.9118 [ref-receipt ATR 0.8945 -> 1.532x])
TP 112.01          (3.43 = 2.504R)
0.08 lots · risk $10.96 · stressed $15.70 · post-loss 4,802.65 · spread 21.2 bps (G1 exempt for passive limits)
```
*Evidence:* z **−1.99**, RSI **24.94**, slope −0.63 %; ±0.5 ATR bid band **$3.92–5.58 M in 13/13 receipts** (26–37× the 150 k floor); CVD decay 0.358 with 4 positive flips; discrete BUY walls at 108.67–108.68 ($154 k/$183 k) plus the earlier 108.58–108.61 shelf ($176 k–$365 k). *Caveat:* limb (a) never printed (skew max 1.198).

**Alternates (validated, same table):** ETHUSD.pi BUY 2411.00 / SL 2381.60 / TP 2484.50 / 0.37 lots / risk **$10.88** / 2.50R (all three flow limbs at the ref receipt, but the book whipsawed to a 70.6× skew spike and a $25.6 M band print — treat depth as unreliable) · NERUSD.p BUY 4.6890 / SL 4.557 / TP 5.019 / 1.0 lot / risk **$13.20** / 2.50R (**expanded cap**) · AVXUSD.p BUY 9.9800 / SL 9.78 / TP 10.48 / 0.50 lots / risk **$10.00** / 2.50R · XAUUSD.pi SELL 4,121.93 / SL 4,135.71 / TP 4,087.48 / 0.01 lot / risk **$13.78** / 2.50R (**expanded cap; 0.28 above the scanner's 13.50 window**) · GER40.p SELL 24,917.64 / SL 25,017.64 / TP 24,667.64 / 0.01 lot / risk **$10.00** / 2.50R (**shelf 0.66 ATR — outside the 0.60 band**) · DOGUSD.p BUY 0.0829 / SL 0.0815 / TP 0.0864 / 1.0 lot / risk **$14.00** / 2.50R (**expanded cap, 253 bps spread, z −1.11 weakest**).

All eight plans in `docs/trade_plans/ARENA_LIMIT_STAGES_20261008_1643.json` validated through `Terminal/Headless/stage_trade_plan.validate_plan` — risk window ✓, TP ≥ 2.50R ✓ (2.500–2.504), SL ≥ 1.50×ATR ✓ (1.503–2.314), tick/step ✓, floor ✓. **None is staged; the desk executes.**

**Risk-envelope conflict (standing):** mandate §2 caps nominal risk at **10.00–11.04** (stressed ≤15.80) while mandate §6 permits **≤15.00**. Binding cap today = §6's 15.00 (G-1 floor math: risk ≤ (equity − 4,795)/1.40 = 16.68 at 4,818.35). Arena prefers ≤11.04; every plan above 11.04 is explicitly flagged **expanded-only**.

---

## 6. PROTOCOL

1. **#18703132: HOLD.** No MT5 action from Arena. The gate bar closed at ≈ 30,944.5 — failed-sweep confirmed, and the ladder has since armed **through Phase-1** (mark +1.67R at 16:49:37). Next rungs: TP 30,739.10; Phase-2 trail behind the 15m EMA20; extend only with SL locked ≥ +1.50R. **Verify in MT5 that SL is 30,909.10 (Phase-1) — telemetry still reports the original 31,089.10.** If a 15m bar closes back ≥ 30,999.62 ⇒ market cut.
2. **Punch exactly one top-2 stage, now permitted by the ratchet — conditional on broker-SL confirmation.** With Phase-1 locked, the joint-stop projects 4,823.00–4,823.50 ≥ 4,795 ✓. If the stop is *not* confirmed moved, capacity is not liberated and the desk must rotate (close at ≈ +1.67R) before staging. Never stage two new orders; multi-order staging is prohibited.
3. **Model 2 is live again:** SP500.p stage A is the first gate-complete CFD short since 15:05. Delete it if a 15m bar closes > 7,796.73, if the 7,777 shelf thins, or if price drifts > 2.0×ATR (≈18 pts) away from the entry before the fill.
4. **Crypto M1 rotation order:** SOL → ETH → NEAR → AVAX → DOGE. Drop any asset whose ±0.5 ATR bid band falls < $150 k or whose book prints an >5× single-receipt skew spike.
5. Re-verify live at submission: quote/spread, recomputed ATR/VWAP, broker-native stop valuation, blackout calendar (FOMC window closed 2026-10-07 18:30 UTC). Fail-closed on any check failure. **No MT5 action taken by Arena.**

---

*Artifacts: `artifacts/arena_dual_track_scan_20261008_1643.json` (scanner v2, 24 assets, ref `ef34f73`) · `artifacts/arena_depth_persistence_20261008_1643.json` (13 receipts × 14 crypto assets = 182 records: mid, z, band, skew, walls, CVD) · `artifacts/arena_briefing_bars_20261008_1643.json` (15:45/16:00/16:15 bars with wick/volume/delta recomputation) · `docs/trade_plans/ARENA_LIMIT_STAGES_20261008_1643.json` · receipts `8919ed7` (16:42:37, briefing panel), `ef34f73` (16:45:37, operative) and `18f7cab` (16:49:37, live addendum).*
