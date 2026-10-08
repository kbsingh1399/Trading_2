# Arena.ai — 24-Asset Dual-Model Ruling + Live Position Review
## Briefing 2026-10-08 18:28:41 UTC · branch `arena/24eb818b-trading-2` · receipt `7087a5c` (snapshot as_of 18:29:38 UTC)

**Desk state at 18:29:38:** equity **4,847.16** | balance 4,838.99 | margin used **876.92** | free margin 3,970.24 | capacity **`HARD_ADMISSION_FREEZE (2/2 filled, 0 pending)`** | **2 open positions — #18706769 ETHUSD.pi LONG 0.37 @ 2,411.00** (SL 2,381.60 / TP 2,484.50, mark **+$9.21 / +0.85R**) and **#18710722 SOLUSD.p SHORT 0.08 @ 107.72** (SL 109.10 / TP 104.27, mark **−$1.04 / −0.09R**) | 0 pending | hard floor 4,775.00 | operating buffer 4,795.00 (headroom +52.16) | auth flag `DENIED_UNVERIFIED_ORDERFLOW`
**Panel identity:** the mandate's §2/§3 panel (balance 4,838.99 / equity 4,847.22 / "Margin Used 0.00 / 100 % Cash Flat / 1 risk slot available") is receipt **`ad3280f` @18:27:38**, i.e. the **pre-SOL-fill** panel — the SOL short filled at 18:22–18:23 (margin used stepped 446.04 → 876.92) and §2's own §3 shows **two** positions. Standing interpretation applies: telemetry + §3 govern; **the desk is at 2/2 capacity and no new order is admissible.**
**Author:** Arena.ai — read-only. No broker I/O; nothing staged, modified or cancelled.

---

## 0. RULING

```
#18706769 ETHUSD.pi LONG 0.37 @ 2,411.00  ->  HOLD + EXECUTE PHASE-0 NOW
    · +0.85R (+$9.21); the +0.80R arm 2,434.52 has been crossed repeatedly (state prints PHASE_0_BE_LOCKED)
    · BUT the broker SL field still reads 2,381.60 — the modification was never executed. Send TRADE_ACTION_SLTP: SL -> 2,415.41.
    · emergency shelf cut only on a 15m CLOSE < 2,405.00 ; Phase-1 arm 2,455.10 ; TP 2,484.50

#18710722 SOLUSD.p SHORT 0.08 @ 107.72  ->  HOLD (the entry wall migrated UP, it did not thin)
    · -0.09R (-$1.04); mid 107.635/107.85 chopping in the 107.5-108.2 pocket
    · the $1.08M band that justified the short printed $996k at 107.68 (18:21:38) then re-stacked at 107.85-107.88 (~$2.2M, 240 s spans)
    · ladder: 106.62 arm -> SL 107.51 ; 105.65 arm -> SL 106.62 ; TP 104.27 ; emergency cut on a 15m CLOSE >= 108.35

MODEL 1 (EXTREME MEAN-REVERSION) — ZERO new candidates. The flush has mean-reverted: deepest |z| on the 24-asset board is
    NEAR -1.71 (RSI 31.6), then SOL -1.61, ADA -1.32, BTC -1.08. No asset pairs |z| >= 2.0 with RSI < 30; ETH, the last
    qualifying stretch, is already held long. Nothing to force.

MODEL 2 (TREND-FOLLOWING) — the tape that remains is continuation-short geometry (crypto at EMA20 / broken-swing shelves):
    STANDBY A  LTCUSD.pi  SELL LIMIT 62.330  / SL 63.377 (2.00xATR) / TP 59.712 (2.50R) / 0.10 lots / risk $10.47
    STANDBY B  LNKUSD.p   SELL LIMIT 12.456  / SL 12.717 (2.00xATR) / TP 11.803 (2.50R) / 0.40 lots / risk $10.44
    STANDBY C  DJ30.p     SELL LIMIT 51,171.48 / SL 51,297.94 (1.50xATR) / TP 50,855.33 (2.50R) / 0.01 lot / risk $12.65  (range-high fade, not a trend)
    alternates BTC 81,352 / BNB 726.10 / DOT 1.038 / BCH 279.16 (all flagged); XRP + ADA are UNSIZEABLE by min-lot math.

*** PUNCHABLE NOW = ZERO. Capacity is 2/2 (HARD_ADMISSION_FREEZE). To take any of the above the desk must CLOSE one exposure
    first — the natural rotation candidate is the SOL short (≈ flat), never an add-on. Multi-order staging is prohibited. ***
```

---

## 1. SECTION 3 — LIVE POSITION REVIEWS

### 1a. #18706769 — ETHUSD.pi LONG 0.37 @ 2,411.00 → **HOLD, and execute the Phase-0 modification**

| Parameter | Value | Read |
|---|---|---|
| Entry / SL / TP | 2,411.00 / 2,381.60 / 2,484.50 | risk 29.40 pts = **$10.88**; SL 1.63×ATR (18.04); TP +2.50R |
| Mark | **+$9.21 / +0.85R** (18:29:38); peak +$9.44 (+0.87R) at 18:24:38 | the post-flush squeeze is paying |
| Ratchet state | `PHASE_0_BE_LOCKED` at 18:22, 18:24, 18:27–18:29 (prints `PHASE_0_PENDING` when mid dips below 2,434.52) | **the +0.80R arm 2,434.52 has been reached — the BE lock is due** |
| Broker SL | **still 2,381.60 in every receipt** | **the desk has NOT executed the stop modification** — send `TRADE_ACTION_SLTP` now: **SL → 2,415.41** (+0.15R locked, +$1.63 worst case) |
| Ladder | Phase-0 2,434.52 → SL 2,415.41 · Phase-1 2,455.10 → SL 2,434.52 · TP 2,484.50 | |
| Emergency shelf cut | **15m close < 2,405.00 ⇒ exit at market** (16:00 flush low 2,412.30 / 17:45 low 2,404.50) | not triggered — the 18:00 bar closed 2,413.6, since then price ran to 2,436 |
| Overhead | **SELL wall 2,436.69 = $624,056** sitting exactly on the current price; then the Phase-1 arm 0.75R above | sellers re-price the cap with every push (2,437.93 → 2,438.88 → 2,437.90 → 2,436.69 across receipts) |
| ETH tape | mid 2,436.10, z **−1.29**, RSI 36.27 (from 16.83 at the fill), 200-EMA slope −0.74 % | flush recovery is intact; the trade is no longer an extreme-stretch trade — it is a recovery trade riding a ladder |

**Verdict: HOLD.** Execute Phase-0 (SL 2,415.41). Do not add (one position per asset; capacity is frozen anyway).

### 1b. #18710722 — SOLUSD.p SHORT 0.08 @ 107.72 (filled 18:22–18:23) → **HOLD, wall-audit supported**

| Parameter | Value | Read |
|---|---|---|
| Entry / SL / TP | 107.72 / 109.10 / 104.27 | risk 1.38 = **$11.04**; SL 1.50×ATR (1.0117 — ATR expanded from 0.9192); TP +2.50R |
| Mark | **−$1.04 / −0.09R** (18:29:38, cur 107.85); worst print −$3.60 (−0.33R) at 18:24:38; the same receipt's mid is 107.635 ⇒ ≈ +0.06R on the mid | flat, chopping at the entry |
| **Wall audit (mandate §3)** | 18:21:38: **S107.68 $996k** (the wall the desk staged against had drifted down from 107.72) → 18:22:38 the wall is **gone from 107.68–72** and price squeezes to 108.17 → 18:29:38: **S107.85 $795k + S107.86 $687k + S107.87/107.88 $459k (240 s spans)** ≈ **$2.2M re-stacked above** | **the supporting wall did NOT thin >50 % — it migrated upward and grew.** For a short this is the thesis intact (sellers still committed overhead), not a delete signal |
| Below | BUY walls 107.55–107.66 with **120–240 s spans** ($209k–$915k) | persistent bids cushion the downside — expect chop, not a straight drop |
| Trend | 200-EMA slope **−0.86 %** (steepest bearish slope on the board); price 1.1 / 3.6 / 4.9 ATR below e20/e50/VWAP; z −1.61 | structure favours the short |
| Counter-signal | RSI recovered 18.85 → 35.42; 18:00 15m bar uw/lw 47.6 %/47.6 % (two-way, vol 0.70×) | momentum is no longer one-way |
| Ladder | **Phase-0 arm 106.62 → SL 107.51** · Phase-1 arm 105.65 → SL 106.62 · TP 104.27 | |
| Emergency shelf cut | **15m close ≥ 108.35 ⇒ exit at market** (above the 18:24 squeeze high 108.17) — cost ≈ −0.46R, saves ~0.5R vs the 109.10 hard stop | not triggered |

**Verdict: HOLD.** The original thesis (broken-shelf retest defended by a ≥$1M seller stack) survives the audit; the trade is simply early. Rotation out at ≈ flat remains available if the desk wants the LTC/LINK standby instead.

---

## 2. MARKET STATE AT 18:28 — THE FLUSH HAS MEAN-REVERTED; A BROAD RELIEF BOUNCE IS UNDERWAY

* **Equities bid, hard.** The 17:00–18:15 window printed heavy buy-side deltas: SP500 15M Δ **+24,388 / −4,325 / +19,026** (1H +30,008 then +19,026), NAS100 15M Δ **+23,492 / +13,983 / +41,584**, DJ30 +3,771 then −1,096/−554, GER40 +1,588 / −146 / +715. SP500 7,757.69 (z −0.88, recovered from the 7,729.84 low), NAS100 30,751.16 (z −1.37, off the 30,547.43 low), DJ30 51,124.10 (z +0.98, 34 pts off the session high), GER40 24,934.05 (z +0.22, back above VWAP).
* **Crypto off the lows; nothing is extreme any more.** BTC 81,313.5 (z −1.08, RSI 46.4 — was −2.38 at 16:59), ETH 2,436.10 (z −1.29, RSI 36.3 — was 16.83 at the fill), SOL 107.635 (z −1.61, RSI 35.4 — was 18.85 at 18:17), NEAR 4.4995 (z −1.71, the deepest remaining stretch), ADA/DOGE/TRX/DOT/LINK/BCH/LTC/AVAX/XRP/BNB all between −0.33 and −1.32. **The mean-reversion window closed.**
* **Metals / oil:** GOLD 4,125.29 (z +0.07, pinned to VWAP/POC after the 4,134.49 rejection); SILVER 59.037 (z −0.46); USWTI 92.68 (z +0.05, VWAP reclaim, label BULLISH on a +0.14 % 200-EMA slope — the day's flush low 91.47 is 2.3 ATR below).
* **FX:** EURUSD 1.1203 (z +0.71), GBPUSD 1.3221 (z +1.12, RANGE_BOUND), USDJPY 157.9235 (z −0.80, buyers in the last three 15M bars: Δ +1,138 / +443 / +1,589 — the range's lower half is being defended).

---

## 3. MODEL 2 (TREND-FOLLOWING) — SCORED ON THE 18:28 TAPE

Geometry: 0.10–0.60 ATR micro-pullback to a 20/50 EMA, prior 15m/1H broken structure, VAH/VAL, or FVG/node. **Track 1 (CFD):** volume ≥ 0.8× 20-bar avg **and** rejection wick ≥ 30 % on the operative bar — recomputed from the mandate's **18:00 bar** (18:00–18:15) against committed parquet (`artifacts/arena_briefing_bars_20261008_1828.json`). **Track 2 (crypto):** depth/CVD legs, no wick gate.

| Asset | Shelf (distance from mid) | Operative 18:00 bar | Verdict |
|---|---|---|---|
| **LTCUSD.pi** | EMA20 **62.33** (+0.54 ATR) | uw 45.2 %, vol 0.94× | **STANDBY A** — Track-2 legs: ask band $437k–668k (13/13 receipts ≥150k) ✓, CVD decay min 0.089 ✓, regime −0.77 % ✓ |
| **LNKUSD.p** | EMA20 **12.456** (+0.53 ATR) | lw 36.4 %, vol 1.05× | **STANDBY B** — ask band ≥150k in 11/13 ✓, decay 0.194 ✓, regime −0.90 % ✓ |
| **DJ30.p** | 2h swing high **51,171.48** (+0.56 ATR) | **uw 44.8 %, vol 1.006×** — Track-1 PASS | **STANDBY C** — but regime RANGE_BOUND (slope −0.009 %): a range-high fade, not a trend continuation |
| XRPUSD.pi | EMA20 1.3546 (+0.27 ATR) | — | compliant but **UNSIZEABLE** (min-lot risk $20.25 > 15.00) |
| BTCUSD.pi | EMA20 81,352 (+0.09 ATR — marginal) | lw 81.8 %, vol 0.90× | alternate — **$1.08M SELL wall at 81,335.5 directly overhead**; ask band 13/13 ✓ |
| BNBUSD.p | broken 2h swing low 726.10 (+0.16 ATR) | lw 62.1 %, vol 1.00× | alternate — ask band ≥150k in only 3/13 |
| DOTUSD.pi | EMA20 1.038 (+0.24 ATR) | lw 57.1 %, vol 0.85× | alternate — ask band ≥150k in 1/13 |
| BCHUSD.p | broken swing low 279.16 (+0.35 ATR) | lw 60.0 %, vol 1.14× | alternate — ask band 0/13 |
| USWTI.p | EMA20 92.95 (+0.52 ATR) | **uw 56.6 %, vol 1.142×** — gate PASS | direction contradicts its BULLISH label ⇒ not a Model-2 trend trade; no long shelf below mid in band |
| GBPUSD.pi | EMA20 −0.30 ATR | **lw 57.1 %, vol 0.812×** — gate PASS | RANGE_BOUND (slope −0.0009 %) ⇒ no trend to follow; stand by |
| GOLD | POC/VWAP 4,125.4 | uw 21.9 %, vol 0.644× | **fails both** the wick and volume legs |
| EURUSD.pi | VAH +0.67 ATR | uw 50.0 %, vol 0.786× | fails the volume leg (0.786 < 0.8) |
| SP500.p / NAS100.p / GER40.p | — | lower wicks 39.8 / 44.2 / 85.7 % with Δ +19,026 / +41,584 / +715 — **buyer absorption at the lows** | no shelf below mid inside 0.60 ATR (VWAP sits 1.1–2.5 ATR above) ⇒ nothing to buy per the rules |
| SILVER | — | uw 23.1 %, vol 0.69× | outside the desk's standing asset set |

**Answer to "must not sit idle":** the honest state is that **the punchable set is empty for capacity reasons, not for lack of setups** — Model 2 does offer LTC/LINK/DJ30 (full blueprints below), but the desk is at 2/2 with a hard admission freeze. Forcing a third order is prohibited; the council's recommendation is to let the two live positions resolve (ETH is +0.85R with a BE lock due; SOL is flat) and then rotate into the best standby, not to stack now.

---

## 4. MODEL 1 (EXTREME MEAN-REVERSION) — ZERO NEW CANDIDATES (the flush is over)

13-receipt depth persistence window **`c060fc3` @18:17:38 → `7087a5c` @18:29:38, 13 × 14 crypto assets = 182 records** (`artifacts/arena_depth_persistence_20261008_1828.json`).

| Asset | z / RSI | ±0.5 ATR bands (13 receipts) | Verdict |
|---|---|---|---|
| NEARUSD.pi | **−1.71** / 31.58 | bid $398k–823k, ask 13/13 | deepest stretch — still **inside** the −2.0 threshold; no walls |
| SOLUSD.p | −1.61 / 35.42 | bid $3.08–5.18 M, ask 13/13 | already short |
| ADA / BTC / XRP / AVAX / BCH / ETH | −1.32 … −1.05 | ADA $2.03–2.58 M bid 13/13 · BTC bid 0/13 (ask 13/13, $1.08 M wall at 81,335.5) · XRP bid 13/13 ($2.6 M last) · AVAX last bid 512k | no |z| ≥ 2.0 |
| BNB / DOT / LINK / LTC / DOGE / TRX | −1.26 … −0.33 | DOGE $1.25–1.68 M bid 13/13; LINK $157k–488k; others mixed | no extreme |

**Method note:** single-receipt skew spikes (BTC 6.9×, ETH 14.4×, BNB 13.6×) remain book-refresh artifacts — only multi-receipt persistence is used; index/commodity/FX assets have no whale/CVD feed (structurally unavailable) and are never scored on them.

---

## 5. STANDBY BLUEPRINTS (validated — **NOT PUNCHABLE** while capacity is 2/2)

**STANDBY A — LTCUSD.pi · Track 2 · Model 2 trend-continuation short (EMA20 retest)**
```
SELL LIMIT 62.330  (EMA20 shelf 62.33 = +0.54 ATR above mid 62.05)
SL 63.377          (1.047 = 2.00 x ATR 0.5236)
TP 59.712          (2.618 = 2.5005R)
0.10 lots · risk $10.47 · stressed $15.09 · spread 48 bps (G1 exempt for passive limits)
```
*Evidence:* established bearish trend (200-EMA slope −0.77 %); Track-2 flow: ask-side ±0.5 ATR band **$437k–668k in 13/13 receipts**, 1m taker CVD abs-decay min **0.089** (decelerating); the operative 18:00 bar printed a **45.2 % upper wick** on 0.94× volume — a bonus rejection signature on top of the Track-2 legs.

**STANDBY B — LNKUSD.p · Track 2 · Model 2 trend-continuation short (EMA20 retest)**
```
SELL LIMIT 12.456  (EMA20 shelf 12.456 = +0.53 ATR above mid 12.3865)
SL 12.717          (0.261 = 1.998 x ATR 0.1306)
TP 11.803          (0.653 = 2.502R)
0.40 lots · risk $10.44 · stressed $15.05 · spread 69 bps (exempt)
```
*Evidence:* slope −0.90 %; ask band ≥ $150k in 11/13 receipts; CVD decay 0.194 with 7/13 decelerating prints; BUY wall 12.364 ($250k) is *below* price, so the retest sells into a thinner book than SOL's.

**STANDBY C — DJ30.p · Track 1 · Model 2 range-high fade (swing shelf)**
```
SELL LIMIT 51,171.48  (2h swing high = +0.56 ATR above mid 51,124.10)
SL 51,297.94          (126.46 = 1.50 x ATR 84.3059)
TP 50,855.33          (2.50R)
0.01 lot · risk $12.65 · stressed $17.81 · spread 0.25 bps
```
*Evidence:* the only CFD to clear **both** Track-1 legs on the operative bar (upper wick **44.8 %**, volume **1.006×** avg20, Δ −554); DJ30 is the day's strongest index (RSI 60.46, z +0.98) sitting at its 2h swing high — the fade is a *range* trade, explicitly flagged as **not** an established-trend Model-2 entry.

**Alternates (validated):** BTCUSD.pi SELL 81,352 / SL 82,452 (2.48×ATR) / TP 78,602 / 0.01 lot / risk **$11.00** (geometry 0.09 ATR — marginal; $1.08 M sell wall overhead) · BNBUSD.p SELL 726.10 / SL 732.99 (1.50×ATR) / TP 708.87 / 2.0 lots / risk **$13.78** (depth leg weak) · DOTUSD.pi SELL 1.038 / SL 1.065 (2.00×ATR) / TP 0.970 / 0.38 lots / risk **$10.26** (depth leg weak) · BCHUSD.p SELL 279.16 / SL 286.16 (2.31×ATR) / TP 261.66 / 0.2 lots / risk **$14.00** (depth leg weak).

All seven plans in `docs/trade_plans/ARENA_LIMIT_STAGES_20261008_1828.json` validated through `Terminal/Headless/stage_trade_plan.validate_plan` — risk window ✓ (10.26–14.00), TP ≥ 2.50R ✓ (2.500–2.519), SL ≥ 1.50×ATR ✓ (1.500–2.483), tick/step ✓, floor ✓. **Excluded by contract math:** XRP (min-lot risk $20.25) and ADA (min-lot risk $22.50) — both exceed the 15.00 cap at any legal size.

**Risk envelope:** §2 prefers nominal ≤ 11.04, §6 permits ≤ 15.00. Both floor ceilings are non-binding at this equity (equity-basis 37.3, balance-basis 33.6), so **§6's 15.00 is the cap**; nothing here exceeds 14.00. **The binding constraint tonight is capacity, not risk:** the freeze blocks any new order, and with the ETH BE lock executed the joint worst case is `4,847.16 + 1.63 − 11.04 = 4,837.75` — the book cannot approach the 4,795 buffer through these positions alone.

---

## 6. PROTOCOL (in priority order)

1. **EXECUTE the ETH Phase-0 stop modification now:** `TRADE_ACTION_SLTP` on **#18706769 → SL 2,415.41** (TP unchanged 2,484.50). The +0.80R arm (2,434.52) has been crossed repeatedly; the state machine already prints `PHASE_0_BE_LOCKED` while the broker stop still reads 2,381.60 — until the modification lands, +0.85R is a mark, not protected capital.
2. **SOL short #18710722: HOLD.** Ladder 106.62 → SL 107.51; 105.65 → SL 106.62; TP 104.27. Emergency cut on a **15m close ≥ 108.35**. Re-audit the seller stack each cycle: the entry wall migrated to 107.85–107.88 (~$2.2 M). If that stack thins below ~$0.5 M while price holds above 107.85, cut instead of waiting for the stop.
3. **No new orders.** Capacity `HARD_ADMISSION_FREEZE (2/2)`. The standby blueprints are for rotation: if the desk wants LTC/LINK/DJ30, **close the SOL short first** (≈ flat) — one for one, never an add-on, never two new stages.
4. **Model 1 stays flat by evidence:** no asset pairs |z| ≥ 2.0 with RSI < 30; re-check next cycle (a fresh leg down would re-open the window; ETH is the only stretch already expressed).
5. Re-verify live at submission: quote/spread, recomputed ATR/VWAP, broker-native stop valuation, blackout calendar (FOMC window closed 2026-10-07 18:30 UTC). Fail-closed on any check failure. **No MT5 action taken by Arena.**

---

*Artifacts: `artifacts/arena_dual_track_scan_20261008_1828.json` (scanner v2, 24 assets, ref `7087a5c`) · `artifacts/arena_depth_persistence_20261008_1828.json` (13 receipts × 14 crypto assets = 182 records) · `artifacts/arena_briefing_bars_20261008_1828.json` (18:00-bar wick/volume recomputation for all 24 assets) · `docs/trade_plans/ARENA_LIMIT_STAGES_20261008_1828.json` · receipts `ad3280f` (18:27:38, briefing panel) and `7087a5c` (18:29:38, operative).*
