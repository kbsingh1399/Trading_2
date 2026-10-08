# Arena Council Dual-Track Ruling: 24-Asset Scan (briefing 2026-10-08 19:58:17 UTC)

**Telemetry basis:** `docs/telemetry/live_snapshot_latest.json`, as_of 2026-10-08 19:58:06 UTC (origin commit `5de64bf` at scan time; telemetry commits 19:48 to 19:58 used for persistence).
**Trade authorization in telemetry:** `DENIED_UNVERIFIED_ORDERFLOW`. This ruling is advisory. The desk executes.
**Indicator freshness:** causal indicators at 19:58 are about 13 minutes old (`indicator_age_min` 13.1, last bar close 19:45 UTC). Quotes are FRESH (age 0.0 s).

## 0. Bottom line

1. **ETH #18706769 LONG 0.37 @ 2,411.00: HOLD.** Live SL 2,434.52 (Phase-1 lock). Mark 2,460.90, floating +18.46 USD, telemetry R 2.12 (live SL basis). TP 2,484.50. No further ratchet rung is confirmed (section 2.1).
2. **Capacity: OPEN 1/2, 0 pending. One slot.** Stage **A only**.
3. **Stage A: DOGUSD.p SELL LIMIT 0.0840**, SL 0.0851, TP 0.0812 (2.55R), 1.0 lot, risk **11.00 USD**. Inside the 11.04 preferred cap. Model 2 (EMA50 shelf).
4. **Alternate B: BTCUSD.pi SELL LIMIT 81,800**, SL 82,850, TP 79,175 (2.50R), 0.01 lot, risk **10.50 USD**. Model 2 (swing-high shelf). Used only if A is deleted under the resting-order rule.
5. **Expanded-only C: NERUSD.p SELL LIMIT 4.617**, SL 4.750, TP 4.284 (2.50R), 1.0 lot, risk **13.30 USD**. Needs the 15.00 desk cap. Not staged.
6. **LTC 62.600 (19:43 stage A) RETIRED.** Mid is 62.675, which is above the level. It fails the 0.10 ATR pullback minimum, and no bearish shelf sits above mid. It was never placed (pending list empty), so there is nothing to delete on the book.
7. **Model 1: zero candidates.** No |Z| of 2.0 or more on any asset. Deepest: NEAR Z -1.29, NAS100 Z -1.22.
8. **Briefing §2 and §4 are stale.** §2 shows margin 0.00; telemetry shows 446.04 USD used (ETH). §4 cites 4,813.99 USD capital. Telemetry governs: equity 4,848.25 USD, balance 4,829.79 USD. Briefing "Top-20 N/A" depth is also stale; telemetry carries real Binance L2 for crypto.

## 1. Account state (telemetry 19:58:06 UTC)

| Field | Value |
|---|---|
| Balance / Equity | 4,829.79 / 4,848.25 USD |
| Margin used / free | 446.04 / 4,402.21 USD |
| Margin level | 1,086.95% |
| Hard floor / cushion | 4,775.00 USD / +73.25 USD |
| G-1 buffer | 4,795.00 USD (headroom +53.25 USD on equity) |
| Capacity | OPEN (1/2 filled, 0 pending) |

**Worst case (ETH stopped at its 2,434.52 lock, no other exposure):** locked +8.70 USD, so 4,838.49 USD. That is +43.49 USD over the buffer. G-1 limit = 43.49 / 1.40 = 31.07 USD. The 15.00 USD desk cap binds.

**After stage A stops out:** 4,838.49 - 11.00 = **4,827.49 USD** (+32.49 USD over the buffer). After stage B stops out instead: 4,827.99 USD (+32.99 USD).

## 2. Position review

### 2.1 ETH #18706769 (LONG 0.37 @ 2,411.00)

| Field | Value |
|---|---|
| Live SL | **2,434.52** (Phase-1 lock). Confirmed in telemetry. |
| TP | 2,484.50 |
| Mark (19:58:06) | 2,460.90 (MT5 bid 2,461.6 / ask 2,464.4 at 19:58 in quotes) |
| Floating | +18.46 USD (telemetry `profit_usd`) |
| R (telemetry) | 2.12 on live SL distance |

**Ruling: HOLD.** Keep 2,434.52. Note: the telemetry R basis (live SL distance) and the initial-risk R used in earlier rulings (1.65R at 17.95 USD) do not match. The desk should confirm the Phase-2 rung before any move. The earlier proposal (SL to 2,455.10 at 2,470.80) stays a proposal, not a rule. Emergency cut 15m close below 2,405.00 is unchanged.

### 2.2 SOL #18710722: CLOSED at 19:23

SOL 109.10 SELL re-entry rejected as churn. SOL mid is now 109.15, and the 109.10 level is below mid, so it is not a valid SELL LIMIT.

### 2.3 Resting orders

None on the book (`pending_orders: []`). DELETE rule not applicable. The 19:43 LTC stage was never placed and is retired (section 0, item 6).

## 3. Model 2 scan (trend-following pullback), all 24 assets

**Geometry:** trend regime must match the 200 EMA slope. The pullback shelf must sit 0.10 to 0.60 ATR on the trade side of mid (above mid for SELL, below mid for BUY). Shelves are EMA20, EMA50, VWAP, prior 15m/1H structure swing, or volume-profile VAH/VAL/POC (telemetry `volume_profile`).
**Track 2 (crypto):** any one of top-20 imbalance at least 1.25x, ask or bid band depth within +/-0.5 ATR at least 150k USD (300k strict), or 1m CVD exhaustion. Persistence measured on the ask band over the last 12 telemetry receipts (19:48 to 19:58).
**Track 1 (CFD):** geometry must be EMA20, EMA50, or VWAP at 0.10 to 0.60 ATR. Also needs a 15m rejection wick of at least 30% at the shelf and bar volume of at least 0.8x the 20-bar average. CFD bars are not L2-backed.

### 3.1 Crypto (all BEARISH on 200 EMA; no crypto BULLISH regime)

| Asset | Shelf and offset (SELL side) | Depth (ask band min / 12 receipts) | Result |
|---|---|---|---|
| **DOGUSD.p** | EMA50 0.0840 (+0.43 ATR) | 1.99M, 12/12; imbalance -0.20 (ask 1.50x) | **Viable: A** (preferred cap) |
| **BTCUSD.pi** | Swing high 81,771 under entry 81,800 (+0.17 ATR); EMA50 81,892 (+0.41) | 150k, 12/12 (440k now) | **Viable: B** (preferred cap); bid-heavy book (+0.21) is against the trade |
| **NERUSD.p** | EMA20 4.617 (+0.45 ATR) | 199k, 12/12 (938k now) | Viable, **expanded-only (13.30)**: C |
| LTCUSD.pi | No bearish shelf 0.10 to 0.60 ATR above mid (EMA20 below, EMA50 +1.04) | n/a | **No setup.** 19:43 level 62.600 is through mid |
| LNKUSD.p | No EMA/VWAP shelf above mid; 12.48 prior high is now broken (price 12.5345) | 244k min (12.55) | **No setup**: shorting into a fresh breakout with no shelf is not Model 2 |
| BNBUSD.p | EMA20 731.99 (+0.55); VAL 730.33 (+0.13) | 80k min, 6/12 pass | **Fails depth.** Top-20 bid 168k / ask 133k; CVD last 6 bars net -275k (no exhaustion) |
| TRXUSD.p | EMA20 and POC 0.3328 (+0.20) | 101k min, 0/12 pass | **Fails depth**; slope -0.06% (too weak) |
| XRPUSD.pi | EMA50 1.375 (+0.04, below minimum) | n/a | **No setup**; also unsizeable at min lot |
| ADAUSD.p | VAL 0.2322 (+0.04, below minimum) | n/a | **No setup**; also unsizeable at min lot |
| BCHUSD.p | VAL 282.25 (0.00) | 27k min, 1/12 pass (282.5 band) | **Fails depth** |
| AVAXUSD.p | EMA20 10.080 (-0.29) below; EMA50 +2.29 | n/a | **No setup** |
| DOTUSD.pi | EMA50 +1.04; no in-band shelf | n/a | **No setup** |
| SOLUSD.p | EMA50 +1.80; VAL +2.67 | 4.2M min | **Excluded** (cut thesis) |
| ETHUSD.pi | Held. No shelf above mid in band (EMA50 +1.64) | n/a | Managed in section 2.1 |

**Crypto long candidates:** none. All 14 crypto assets are BEARISH.

### 3.2 CFD (Track 1: geometry plus 15m wick plus volume)

| Asset | Regime | Geometry (EMA20 / EMA50 / VWAP offset) | Result |
|---|---|---|---|
| SP500.p | BEARISH | EMA50 +0.22; VWAP +0.42 (SELL side) | **Shelf not tested.** Highest 15m high 7765.35 (19:15); shelf is 7768.2 to 7770.5. No wick at shelf. **Fail** |
| NAS100.p | BEARISH | EMA20 +0.58 (SELL side) | **Shelf not tested.** Highest 15m high 30721.70. **Fail** |
| SILVER | BEARISH | VWAP +0.41 (SELL side) | **Shelf not tested.** Highest 15m high 59.22 (19:30), VWAP 59.277. **Fail** |
| GOLD | BULLISH, slope +0.002% | EMA20 -0.74; EMA50 -0.99; VWAP -0.95 (all outside band) | **Fail geometry.** Telemetry VAH 4128.7 (-0.45) is not a Track 1 geometry. Not admitted |
| DJ30.p | BULLISH, slope +0.005% | EMA20 -1.63; EMA50 -2.59; VWAP -3.25 | **Fail geometry.** Telemetry VAH 51,204 (-0.36) is not Track 1 geometry; briefing 48H VAH 51,275.7 is above mid. Not admitted |
| USWTI.p | BULLISH, slope +0.10% | EMA20 +1.17; EMA50 +1.04; VWAP +0.80 (all above mid for BUY) | **Fail geometry** |
| EURUSD.pi | BULLISH, flat | EMA20 -1.00; EMA50 -1.71; VWAP -2.29 | **Fail geometry**; bars at 2 dp cannot support wick test |
| GBPUSD.pi | BULLISH, flat | EMA20 -1.12; EMA50 -1.88; VWAP -2.62 | **Fail geometry**; 2 dp resolution |
| USDJPY.pi | BEARISH, slope -0.02% | EMA20 +0.81; EMA50 +1.84; VWAP +1.94 (all outside band) | **Fail geometry** |
| GER40.p | BEARISH, slope -0.07% | All shelves below mid | **Fail geometry** |

### 3.3 Model 1 (extreme mean-reversion, |Z| at least 2.0 from VWAP)

Crypto VWAP Z-scores: all between -0.27 and -1.29 (deepest NEAR -1.29). CFD Z-scores: all between -1.22 and +1.83 (deepest GBPUSD +1.83, NAS100 -1.22). No asset meets |Z| at least 2.0. **Zero candidates.**

## 4. Blueprints

All plans are SELL LIMIT, passive (entry above MT5 bid), SL at least 1.5 ATR, TP at least 2.5R. Validated with `validate_plan` (PASS). Expiry 21:58:00 UTC. Stage file: `docs/trade_plans/ARENA_LIMIT_STAGES_20261008_1958.json`.

| Rank | Symbol | Direction | Entry (SELL LIMIT) | SL | TP | R | SL / ATR | Lot | Risk (USD) | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| **A** | DOGUSD.p | SELL LIMIT | 0.0840 | 0.0851 | 0.0812 | 2.55 | 1.57 | 1.0 | **11.00** | **Stage** (one slot) |
| **B** | BTCUSD.pi | SELL LIMIT | 81,800 | 82,850 | 79,175 | 2.50 | 2.77 | 0.01 | **10.50** | Alternate |
| **C** | NERUSD.p | SELL LIMIT | 4.617 | 4.750 | 4.284 | 2.50 | 1.52 | 1.0 | 13.30 | Expanded-only (needs 15.00 cap) |

**Microstructure justification:**
- **A (DOGE):** 200 EMA slope -0.87% BEARISH. Entry 0.0840 sits on the EMA50 (0.0840), +0.43 ATR above mid 0.0837, with EMA20 (0.0825) below. Ask band 1.99M minimum across 12 receipts (2.67M now). Top-20 imbalance -0.20 (ask 1.50x bid), which passes the 1.25x imbalance test. 1m CVD over the last 6 bars is mixed (+69k, +17k, +143k, -32k, +56k, +35k; net +288k), so there is no clean buyer-exhaustion signal. The Track 2 pass rests on depth and imbalance. SL 0.0851 sits 1.57 ATR above entry. Risk 11.00 USD, inside the 11.04 preferred cap. Feed is 4 dp with ATR 0.0007 (7 ticks), so the stop has coarse resolution. Spread 251 bps is exempt as a passive limit (bid 0.0827, ask 0.0848).
- **B (BTC):** 200 EMA slope -0.32% BEARISH. Entry 81,800 sits 0.17 ATR above mid, just above the 81,771 swing high (4H 16:00, 1H 19:00, 15M 19:30 highs), so price is still under that structure. EMA50 81,892 (+0.41 ATR) is the next shelf above. Ask band 150k minimum across 12 receipts (440k now, passes 300k strict). Book imbalance is bid-heavy (+0.21), which works against the trade, so this case rests on depth alone. Spread 1.8 bps. SL 82,850 is 2.77 ATR above entry (the 1.5 ATR floor is 82,368, so 82,850 is comfortably outside). A 0.02 lot version at SL 82,400 (1.58 ATR) would also be valid but gives 12.00 USD (expanded). Not used.
- **C (NEAR):** 200 EMA slope -1.39% BEARISH, RSI 38.7. Entry 4.617 is the EMA20 (4.6172), +0.45 ATR above mid 4.5775. Ask band 199k minimum across 12 receipts (938k now, passes 300k strict). Lot min 1.0, so the risk floor of 13.30 USD sits above the 11.04 cap. Expanded-only.

**Rejected entries from the 19:43 cycle:**
- LTC 62.600 (stage A, 19:43): mid is through the level. Fails the 0.10 ATR minimum. Retired.
- LNK 12.530 (19:43 alternate C): entry is -0.03 ATR from mid (price at shelf). Fails the minimum. Retired. A re-anchored 12.550 would be a breakout short with no shelf; rejected.

## 5. Footprint review (telemetry 15m, 1m CVD)

- **Crypto 1m CVD (last 6 bars, USD):** BTC +3.39M net; ETH and SOL mixed; DOGE +288k; NEAR +89k; LTC +49k; LINK +44k; BNB -275k; TRX +4.5k; BCH +12.7k. No candidate shows a clean 1m exhaustion signal on the short side. Admission for A and B rests on the depth and imbalance tests, not CVD.
- **CFD 15m (briefing bars):** SP500, NAS100, and SILVER all printed their 15m highs below their shelves. None touched the shelf, so no wick test is possible. Not admissible.
- **Trade authorization:** `DENIED_UNVERIFIED_ORDERFLOW` persists. Pioneer and stop-cluster modules are UNAVAILABLE (no verified stop feed). Liquidation-band fields are UNAVAILABLE. The ruling uses only Binance top-20 depth, CVD, and price geometry.

## 6. Governance

- **One order at a time.** Stage A only, with B as the alternate. Multi-order staging is prohibited. A and B must never be held together.
- **Resting-order rule:** delete A immediately if the ask band at 0.0840 to 0.0851 thins by more than 50%, or if price drifts more than 2.0 ATR (0.0014) from 0.0840.
- **Retired:** LTC 62.600 (19:43 stage A, not placed), LNK 12.530 (19:43 alternate C), and all 19:23 and 19:15 stages.
- **Do not re-enter SOL 109.10 SELL.**
- **Preferred-cap check:** A 11.00 is inside the 11.04 cap. B 10.50 is inside the cap. C 13.30 is expanded-only.

## 7. Data caveats

- Briefing §2 (margin 0.00; "exactly ONE slot") and §4 (4,813.99 USD capital) are stale. Telemetry governs.
- Briefing "Top-20 N/A" depth is stale. Telemetry carries Binance L2 for crypto, sampled to top-20 levels only. Band depth is a lower bound.
- Briefing 48H profile values (for example LTC VAH 68.27, BTC VAH 84,340) do not match telemetry `volume_profile` (LTC VAH 64.74, BTC VAH 82,847). Telemetry was used for shelf geometry. Briefing profile was used only as a cross-check. This conflict is not resolved; it did not change any admitted candidate.
- CFD feeds are 2 dp for FX and 1 point for indices in the briefing. The Track 1 wick test cannot be measured on FX.
- `scripts/arena_dual_track_scan_v2.py` hard-codes 4,813.99 USD equity and was not used.
- Telemetry R values re-base after SL ratchets. Quote R on initial risk where stated.

## 8. Spot check at 20:01:06 UTC (telemetry commit `d470f24`)

- Capacity still OPEN 1/2, 0 pending. ETH mark 2,464.70, SL 2,434.52, floating +19.87 USD, telemetry R 2.28. HOLD unchanged.
- **A (DOGE 0.0840):** mid 0.0839, ATR 0.0006. Entry is +0.17 ATR above mid, still inside the 0.10 to 0.60 band. Bid 0.0828 is below entry, so the order stays passive. **A remains valid.** SL 0.0851 is now 1.83 ATR.
- **B (BTC 81,800):** mid 81,770.5, ATR 364.6. Entry is now only +0.08 ATR above mid, **below the 0.10 ATR floor**. Price is at the 81,771 swing high. B is not valid at 81,800. A re-anchor to at least 81,808 (0.10 ATR) would need a fresh validation before it could be staged. Do not stage B from this ruling.
- **C (NEAR 4.617):** mid 4.607, ATR 0.0841. Entry is +0.12 ATR above mid, still in band. Expanded-only; not staged.
