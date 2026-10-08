# Arena Council Dual-Track Ruling: 24-Asset Scan (briefing 2026-10-08 20:25:08 UTC)

**Telemetry basis:** `docs/telemetry/live_snapshot_latest.json`, as_of 2026-10-08 20:25:06 UTC.
**Trade authorization in telemetry:** `DENIED_UNVERIFIED_ORDERFLOW`. This ruling is advisory. The desk executes.

## 0. Bottom line

1. **CAPACITY IS FROZEN at 2/2.** Telemetry shows one filled position (ETH #18706769) and one pending order (NERUSD.p SELL_LIMIT, ticket 18713247, 1.0 lot @ 4.617, placed 20:15:42 UTC). Under the freeze rule, **zero new punches**. The briefing's "one slot available" is stale.
2. **The pending NEAR order matches my 20:10 alternate B exactly** (entry 4.617, SL 4.744, TP 4.299, 1.0 lot). It was not placed by this agent. It was placed on the desk side, most likely from the stage file. It was never the primary stage (A was DOGE 0.0840). The desk should confirm who placed it and under what cap.
3. **Ticket 18713247 (NEAR): KEEP under the resting-order rule.** The wall did not thin (ask band at 4.617 is 718k USD, up from 699k at 20:10), and drift is +0.47 ATR, below the 2.0 ATR trigger. **Flag for desk decision:** nominal risk 12.70 USD is expanded-only (above the 11.04 preferred cap), and stressed loss 18.29 USD exceeds the 15.80 USD stressed cap in briefing §2. If the desk enforces §2 strictly, DELETE 18713247 to free the slot for stage A below.
4. **DOGE 0.0840 (20:10 stage A): RETIRED.** Mid is now 0.0842, above the level, and the EMA50 has been crossed. Not placed.
5. **Standby A (preferred cap): LTCUSD.pi SELL LIMIT 63.100**, SL 64.150, TP 60.475 (2.50R), 0.10 lot, risk **10.50 USD**. Model 2, EMA50 shelf, 12/12 depth at 150k or more. **Standby only.** Do not punch while capacity is 2/2.
6. **Standby B (preferred cap): BTCUSD.pi SELL LIMIT 81,833**, SL 82,370, TP 80,490.5 (2.50R), 0.02 lot, risk **10.74 USD**. Model 2, 20:00 rejection high, 12/12 depth at 150k or more. **Standby only**, and the alternate if A is blocked.
7. **Model 1: zero candidates.** No |Z| of 2.0 or more with the RSI gate met. DJ30 (+1.76), GOLD (+1.52), EURUSD (+1.72), and GBPUSD (+1.74) all fall short of 2.0.
8. **Briefing §2 and §4 are stale.** §2 shows margin 0.00. Telemetry shows 446.04 USD margin used (ETH), capacity 2/2, and one pending order. §4 cites 4,813.99 USD capital. Telemetry governs: equity 4,849.77 USD, balance 4,829.79 USD.

## 1. Account state (telemetry 20:25:06 UTC)

| Field | Value |
|---|---|
| Balance / Equity | 4,829.79 / 4,849.77 USD |
| Margin used / free | 446.04 / 4,403.73 USD |
| Margin level | 1,087.29% |
| Hard floor / cushion | 4,775.00 USD / +74.77 USD |
| G-1 buffer | 4,795.00 USD (headroom +54.77 USD on equity) |
| Capacity | 1 filled, 1 pending: **FROZEN 2/2** |

**Worst case, ETH stopped at its 2,434.52 lock:** locked +8.70 USD gives 4,838.49 USD (+43.49 over the buffer). G-1 limit 31.07 USD. The 15.00 USD desk cap binds.

**If NEAR (18713247) fills and then stops at 4.744:** 4,838.49 - 12.70 = 4,825.79 USD (+30.79 over the buffer). Stressed (18.29 USD): 4,820.20 USD (+25.20 over the buffer). Still above the buffer, but the stressed loss breaches the 15.80 USD cap in §2.

## 2. Position review

### 2.1 ETH #18706769 (LONG 0.37 @ 2,411.00)

| Field | Value |
|---|---|
| Live SL | **2,434.52** (Phase-1 lock). Confirmed in telemetry. |
| TP | 2,484.50 |
| Mark (20:25:06) | 2,465.00 |
| Floating | +19.98 USD (telemetry `profit_usd`) |
| R (telemetry) | 2.30 on live SL distance |

**Ruling: HOLD.** Keep 2,434.52. No Phase-2 rung is confirmed; the telemetry R basis (live SL distance) and the initial-risk R in earlier rulings still do not match. The desk should confirm before any move. Emergency cut 15m close below 2,405.00 is unchanged.

### 2.2 Pending order ticket 18713247 (NERUSD.p SELL_LIMIT 1.0 @ 4.617)

| Check | Result |
|---|---|
| Mid / drift from entry | Mid 4.5785. Entry is +0.47 ATR above mid (ATR 0.0811). Below the 2.0 ATR DELETE trigger. |
| Supporting ask band (+/-0.5 ATR of 4.617) | 718k USD now; 12/12 receipts at 637k or more. Not thinned. |
| Book imbalance | +0.12 (bid-heavy; no ask-heavy edge) |
| Geometry | EMA20 4.6077 (+0.36 ATR) is the shelf. 200 EMA slope -1.39%. Entry sits 0.47 ATR above mid, inside the band. |
| Resting-order rule | **KEEP** |
| Sizing | Risk 12.70 USD (expanded-only, above 11.04). Stressed 18.29 USD (above the 15.80 stressed cap in §2). |

**Desk decision required:** either keep the order and accept the sizing exception, or DELETE it and stage A. I am not making that call. Under my standing rule, expanded-only plans are flagged, not silently admitted.

### 2.3 DOGE 0.0840 (20:10 stage A): RETIRED

Mid 0.0842 is above the entry, so the level has been traded through. EMA50 is now 0.0839 (-0.50 ATR, below mid). Ask-side depth is strong (2.28M USD), but there is no shelf above mid in band. Not placed.

## 3. Model 2 scan (trend-following pullback), all 24 assets

**Geometry:** trend regime must match the 200 EMA slope. Pullback shelf 0.10 to 0.60 ATR on the trade side of mid. Shelves: EMA20, EMA50, VWAP, prior 15m/1H swing structure, or VAH/VAL/POC.
**Track 2 (crypto):** any one of top-20 imbalance at least 1.25x, ask-band depth within +/-0.5 ATR at least 150k USD (300k strict), or 1m CVD exhaustion. Persistence standard: 12/12 receipts at or above 150k.
**Track 1 (CFD):** EMA20, EMA50, or VWAP at 0.10 to 0.60 ATR. Also needs a 15m rejection wick of at least 30% at the shelf and bar volume of at least 0.8x the 20-bar average.

### 3.1 Crypto (all 14 BEARISH on the 200 EMA; no crypto BULLISH regime)

| Asset | Shelf and offset (SELL side) | Depth (ask band, 12 receipts) | Result |
|---|---|---|---|
| **LTCUSD.pi** | EMA50 63.085 (+0.57 ATR) | 264k min, 12/12 (476k now); imbalance +0.12 | **Standby A** (preferred cap, 10.50) |
| **BTCUSD.pi** | 20:00 rejection high 81,833 (+0.40 ATR). EMA50 81,881 (+0.54) has 11/12 | 233k min, 12/12 at 81,833 (659k now); imbalance +0.04 | **Standby B** (preferred cap, 10.74) |
| NERUSD.p | EMA20 4.617 (+0.47 ATR from mid) | 637k min, 12/12 (718k now) | **Live** (ticket 18713247). KEEP; expanded-only, see section 2.2 |
| DOGUSD.p | EMA50 0.0839 now below mid; 0.0840 traded through | n/a | **Retired** (section 2.3) |
| BNBUSD.p | EMA20 731.69 (-0.04 ATR, below mid) | n/a | **No setup** |
| TRXUSD.p | EMA20 0.3327 (-0.20); POC at mid | n/a | **No setup**; depth failed earlier (101k) |
| LNKUSD.p | EMA50 12.654 (+0.30 ATR) | Not tested for persistence this cycle | **Watch.** Shelf is in band and the trend is bearish, but the EMA50 level was not persistence-tested this cycle. Not admitted |
| BCHUSD.p | EMA50 287.09 (+1.89) out; VAL 282.25 (-0.17) below | n/a | **No setup** |
| AVAXUSD.p | EMA50 +1.66; VAL -0.94 | n/a | **No setup** |
| DOTUSD.pi | EMA50 -1.93 | n/a | **No setup** (bearish trend, no short shelf above mid) |
| XRPUSD.pi | EMA50 1.3748 (-0.11) below mid | n/a | **No setup**; unsizeable at min lot |
| ADAUSD.p | EMA50 +1.75 | n/a | **No setup**; unsizeable at min lot |
| SOLUSD.p | EMA50 +1.69; VAL +2.76 | n/a | **Excluded** (cut thesis) |
| ETHUSD.pi | Held; EMA50 +1.39 out of band | n/a | Managed in section 2.1 |

**Crypto long candidates:** none.

### 3.2 CFD (Track 1: geometry, 15m wick, volume)

| Asset | Regime | Geometry (offset) | Result |
|---|---|---|---|
| NAS100.p | BEARISH | EMA20 30,770.7 (+0.14). Highest 15m high 30,760.05 (20:00), so 30,770.7 is not tested | **Shelf not tested. Fail** |
| SP500.p | BEARISH | VWAP 7770.34 (+0.09, below minimum). POC 7774.33 (+0.45) is profile-only | **No Track 1 shelf** |
| SILVER | BEARISH | VWAP 59.276 (+0.42). Highest 15m high 59.23, so untested | **Shelf not tested. Fail** |
| USDJPY.pi | BEARISH | EMA20 157.933 (+0.82). Highest 15m high 157.91, so untested; 2 dp bars | **Fail** |
| GER40.p | BEARISH | All shelves below mid | **Fail geometry** |
| GOLD | BULLISH | EMA20 -1.07; EMA50 -1.42; VWAP -1.46 | **Fail geometry** |
| DJ30.p | BULLISH | EMA20 -1.82; EMA50 -2.87; VWAP -3.65 | **Fail geometry** (Model 1 check in section 3.3) |
| USWTI.p | BULLISH on EMA200 slope, but price is below the stack | EMA20 +1.65 and VWAP +1.55 (above mid for BUY). VAL 91.98 (+0.09, below minimum) | **No BUY shelf** |
| EURUSD.pi / GBPUSD.pi | BULLISH | EMA20 -1.14 / -0.87; both outside band or at the edge | **Fail geometry**; 2 dp bars cannot support wick test |

### 3.3 Model 1 (extreme mean-reversion, |Z| at least 2.0, RSI below 30 or above 70)

- Crypto: all VWAP Z-scores between -1.25 and +0.57. None at |Z| of 2.0 or more.
- CFD: DJ30 +1.76 (RSI 68.7, below the 70 gate); GBPUSD +1.74 (RSI 62); EURUSD +1.72 (RSI 62.4); GOLD +1.52 (RSI 60.6). None reach |Z| of 2.0.
- **Model 1 result: zero admissible candidates.**

## 4. Blueprints

All plans are SELL LIMIT, passive (entry above MT5 bid), SL at least 1.5 ATR, TP at least 2.5R. Validated with `validate_plan` (PASS). Expiry 21:58:00 UTC. Stage file: `docs/trade_plans/ARENA_LIMIT_STAGES_20261008_2025_STANDBY.json`.

| Rank | Symbol | Direction | Entry (SELL LIMIT) | SL | TP | R | SL / ATR | Lot | Risk (USD) | Stressed (USD) | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **A** | LTCUSD.pi | SELL LIMIT | 63.100 | 64.150 | 60.475 | 2.50 | 2.53 | 0.10 | **10.50** | 15.12 | Standby (frozen) |
| **B** | BTCUSD.pi | SELL LIMIT | 81,833 | 82,370 | 80,490.5 | 2.50 | 1.54 | 0.02 | **10.74** | 15.47 | Standby (frozen) |

**Microstructure justification:**
- **A (LTC):** 200 EMA slope -0.70% BEARISH. Entry 63.10 sits on the EMA50 (63.085), +0.57 ATR above mid 62.85. EMA20 (62.32) is below. Ask band minimum 264k USD across 12 receipts (476k now, passes 300k strict). Imbalance +0.12 is bid-heavy, so this rests on the ask band. 1m CVD is net negative over the last 6 bars (sellers), but there is no exhaustion signal. SL 64.15 is 2.53 ATR above entry. Risk 10.50 USD, inside the 11.04 cap. Stressed 15.12, inside the 15.80 cap in §2.
- **B (BTC):** 200 EMA slope -0.29% BEARISH. Entry 81,833 is the 20:00 rejection high, +0.40 ATR above mid 81,693.5. EMA50 81,881 sits just above it. Ask band minimum 233k USD across 12 receipts (659k now). Imbalance +0.04 is balanced. 1m CVD is strongly negative over the last 6 bars, with no exhaustion. SL 82,370 is 1.54 ATR above entry (the floor is 1.5 ATR). Risk 10.74 USD at 0.02 lot. Stressed 15.47, inside the 15.80 cap.

**Standby rule:** do not punch A or B while capacity is 2/2. If ticket 18713247 is deleted, capacity goes to 1/2 and A is the one to stage. B is the fallback if A is blocked. Never hold A and B together.

## 5. Footprint review (telemetry 15m, 1m CVD, L2 depth)

- **BTC:** The 20:00 bar spiked to 81,833 and sold back to 81,693 within 25 minutes. The 1m CVD is strongly negative (sellers) for the last 6 bars. This fits a short into a rejection, but there is no exhaustion signal, so admission rests on depth.
- **LTC:** 1m CVD over the last 6 bars is net negative (-70k). Admission rests on the ask band.
- **NEAR:** 1m CVD over the last 6 bars is mixed (net negative, with one +179k bucket among them).
- **CFDs:** NAS100, SILVER, and USDJPY all printed 15m highs below their shelves, so the wick test cannot be measured.
- **Trade authorization:** `DENIED_UNVERIFIED_ORDERFLOW` persists. Pioneer, stop-cluster, and liquidation-band fields are UNAVAILABLE.

## 6. Governance

- **Capacity 2/2 freeze:** zero new punches. Both plans above are standby only.
- **Resting-order rule for 18713247 (NEAR):** KEEP. DELETE triggers if the 4.617 ask band thins by more than 50% (below about 359k USD) or if price drifts more than 2.0 ATR (0.162) from 4.617. Neither has occurred.
- **Sizing exception for 18713247:** expanded-only (12.70 nominal) and stressed 18.29, above the 15.80 cap in §2. Desk decision.
- **Retired:** DOGE 0.0840 (20:10 stage A, not placed). BTC 81,800 (19:58 alternate, retired at 20:10). LTC 62.600 (19:43 stage A). LNK 12.530 (19:43 alternate).
- **Do not re-enter SOL 109.10 SELL.**

## 7. Data caveats

- Briefing §2 (margin 0.00; "one slot available") and §4 (4,813.99 USD capital) are stale. Telemetry governs.
- Briefing "Top-20 N/A" depth is stale. Telemetry carries Binance L2 for crypto, sampled to top-20 levels only. Band depth is a lower bound.
- Briefing 48H profile values do not match telemetry `volume_profile`. Telemetry was used for shelf geometry. This conflict is unresolved and did not change any admitted candidate.
- Causal indicators are about 13 minutes old (last bar close 19:45 UTC). Quotes are fresh.
- CFD feeds are 2 dp for FX and 1 point for indices in the briefing, so the Track 1 wick test cannot be measured on FX.
- `scripts/arena_dual_track_scan_v2.py` hard-codes 4,813.99 USD equity and was not used.
- Telemetry R values re-base after SL ratchets. Quote R on initial risk where stated.
