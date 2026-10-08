# Arena Council Dual-Track Ruling: 24-Asset Scan (briefing 2026-10-08 20:10:11 UTC)

**Telemetry basis:** `docs/telemetry/live_snapshot_latest.json`, as_of 2026-10-08 20:10:06 UTC (origin commit at scan time, after the 20:10 auto-sync).
**Trade authorization in telemetry:** `DENIED_UNVERIFIED_ORDERFLOW`. This ruling is advisory. The desk executes.

## 0. Bottom line

1. **ETH #18706769 LONG 0.37 @ 2,411.00: HOLD.** Live SL 2,434.52 (Phase-1 lock, state `PHASE_1_PROFIT_LOCKED`). Mark 2,465.90, floating +20.31 USD, telemetry R 2.33 (live SL basis). TP 2,484.50. No Phase-2 rung is confirmed (section 2.1).
2. **Capacity: OPEN 1/2, 0 pending. One slot.** Stage **A only**.
3. **Stage A: DOGUSD.p SELL LIMIT 0.0840**, SL 0.0851, TP 0.0812 (2.55R), 1.0 lot, risk **11.00 USD** (inside the 11.04 preferred cap). Model 2, EMA50 shelf.
4. **Alternate B (expanded-only): NERUSD.p SELL LIMIT 4.617**, SL 4.744, TP 4.299 (2.50R), 1.0 lot, risk **12.70 USD**. Needs the 15.00 desk cap. Used only if A is deleted; never held alongside A.
5. **BTC 81,800 (19:58 alternate) RETIRED.** Mid is now 81,830.5, above the level. The 81,771 swing high is broken. The ask band fell to 59k USD, below the 150k floor, and the book is 30:1 bid-heavy. No admissible BTC short.
6. **Model 1: zero candidates.** The only |Z| of 2.0 or more is DJ30 (+2.12), which fails the RSI gate (66.88 is below 70) and the 15m upper-wick test (about 28%, below 30%). GBPUSD (+2.05) fails the RSI gate and 2 dp data resolution.
7. **Briefing §2 and §4 are stale.** §2 shows margin 0.00 and "exactly ONE slot". Telemetry shows 446.04 USD margin used (ETH) and capacity OPEN 1/2. §4 cites 4,813.99 USD capital. Telemetry governs: equity 4,850.10 USD, balance 4,829.79 USD. Briefing "Top-20 N/A" depth is stale; telemetry carries real Binance L2 for crypto.

## 1. Account state (telemetry 20:10:06 UTC)

| Field | Value |
|---|---|
| Balance / Equity | 4,829.79 / 4,850.10 USD |
| Margin used / free | 446.04 / 4,404.06 USD |
| Margin level | 1,087.37% |
| Hard floor / cushion | 4,775.00 USD / +75.10 USD |
| G-1 buffer | 4,795.00 USD (headroom +55.10 USD on equity) |
| Capacity | OPEN (1/2 filled, 0 pending) |

**Worst case (ETH stopped at its 2,434.52 lock, no other exposure):** locked +8.70 USD, so 4,838.49 USD. That is +43.49 USD over the buffer. G-1 limit = 43.49 / 1.40 = 31.07 USD. The 15.00 USD desk cap binds.

**After stage A stops out:** 4,838.49 - 11.00 = **4,827.49 USD** (+32.49 USD over the buffer). After alternate B instead: 4,825.79 USD (+30.79 USD).

## 2. Position review

### 2.1 ETH #18706769 (LONG 0.37 @ 2,411.00)

| Field | Value |
|---|---|
| Live SL | **2,434.52** (Phase-1 lock). Confirmed in telemetry. |
| TP | 2,484.50 |
| Mark (20:10:06) | 2,465.90 |
| Floating | +20.31 USD (telemetry `profit_usd`) |
| R (telemetry) | 2.33 on live SL distance |

**Ruling: HOLD.** Keep 2,434.52. The telemetry R basis (live SL distance) and the initial-risk R used in earlier rulings do not match. The desk should confirm the Phase-2 rung before any move. The earlier proposal (SL to 2,455.10 at 2,470.80) stays a proposal, not a rule. Emergency cut 15m close below 2,405.00 is unchanged.

### 2.2 SOL #18710722: CLOSED at 19:23

SOL 109.10 SELL re-entry rejected as churn. SOL mid is 109.24 (above 109.10), and SOL has no shelf in band (EMA50 +1.68 ATR, VAL +2.66 ATR).

### 2.3 Resting orders

None on the book (`pending_orders: []`). The DELETE rule does not apply. The 19:58 BTC alternate was never placed and is retired.

## 3. Model 2 scan (trend-following pullback), all 24 assets

**Geometry:** trend regime must match the 200 EMA slope. The pullback shelf must sit 0.10 to 0.60 ATR on the trade side of mid (above mid for SELL, below mid for BUY). Shelves are EMA20, EMA50, VWAP, prior 15m/1H swing structure, or volume-profile VAH/VAL/POC.
**Track 2 (crypto):** any one of top-20 imbalance at least 1.25x, ask or bid band depth within +/-0.5 ATR at least 150k USD (300k strict), or 1m CVD exhaustion. Persistence measured over the last 12 telemetry receipts (about 19:58 to 20:10 UTC). The standard is 12/12 at or above 150k.
**Track 1 (CFD):** geometry must be EMA20, EMA50, or VWAP at 0.10 to 0.60 ATR. Also needs a 15m rejection wick of at least 30% at the shelf and bar volume of at least 0.8x the 20-bar average.

### 3.1 Crypto (all 14 BEARISH on 200 EMA; no crypto BULLISH regime)

| Asset | Shelf and offset (SELL side) | Depth (ask band min / 12 receipts) | Result |
|---|---|---|---|
| **DOGUSD.p** | EMA50 0.0840 (+0.17 ATR) | 1.75M, 12/12 (2.09M now); imbalance -0.11 (ask 1.26x) | **Viable: A** (preferred cap) |
| **NERUSD.p** | EMA20 4.617 (+0.28 ATR) | 679k, 12/12 (699k now); imbalance +0.07 | Viable, **expanded-only (12.70)**: B |
| BTCUSD.pi | 81,800 is now below mid (-0.08 ATR). EMA50 81,884 (+0.15); 81,771 swing broken | 59k now; 10/12 (fails current floor); imbalance +0.94 bid-heavy | **Fails depth and structure.** Retired |
| LTCUSD.pi | EMA50 63.10 (+0.47 ATR); ask at 63.00 (+0.23) | 63.10: 8/12 pass (457k now). 63.00: 11/12 | **Watch only.** 63.10 fails the 12/12 standard. 63.00 is a round level, not a geometric shelf. 19:43 stage A (62.600) is through mid and retired |
| BNBUSD.p | EMA20 731.71 (+0.08 ATR, below minimum); VAL 729.15 below | 73k min, 5/12 pass | **Fails** geometry and depth |
| TRXUSD.p | EMA20 0.3327 (-0.20); POC at mid | 101k, 0/12 | **Fails** geometry, depth; slope -0.06% |
| LNKUSD.p | EMA50 12.658 (+0.78) | n/a | **No setup** (EMA50 outside band). Prior 12.48 high now broken |
| SOLUSD.p | EMA50 +1.68; VAL +2.66 | 4.6M min | **Excluded** (cut thesis) |
| XRPUSD.pi | EMA50 1.3748 (+0.03, below minimum) | n/a | **No setup**; also unsizeable at min lot |
| ADAUSD.p | EMA50 +2.25; VAL -0.29 | n/a | **No setup**; also unsizeable at min lot |
| BCHUSD.p | EMA50 +1.71; VAL -0.37 | n/a | **No setup** |
| AVAXUSD.p | EMA50 +1.64; VAL -0.75 | n/a | **No setup** |
| DOTUSD.pi | EMA50 -1.93; VWAP -0.76 (both below mid) | n/a | **No setup** |
| ETHUSD.pi | Held; EMA50 +1.34 out of band; VAL below | n/a | Managed in section 2.1 |

**Crypto long candidates:** none. All crypto is BEARISH on the 200 EMA.

### 3.2 CFD (Track 1: geometry plus 15m wick plus volume)

| Asset | Regime | Geometry (SELL or BUY side, offset) | Result |
|---|---|---|---|
| SP500.p | BEARISH | EMA20 -0.94; EMA50 -0.30; VWAP -0.09 (all below mid). POC 7775.1 (+0.33) is volume-profile only | **No Track 1 shelf** |
| NAS100.p | BEARISH | EMA20 30773.3 (+0.27). Highest 15m high 30739.5, so 30773 untested | **Shelf not tested. Fail** |
| SILVER | BEARISH | VWAP 59.276 (+0.39). Highest 15m high 59.21, so untested | **Shelf not tested. Fail** |
| USDJPY.pi | BEARISH | EMA20 157.941 (+0.58). Highest 15m high 157.90, so untested; 2 dp bars | **Shelf not tested. Fail** |
| GER40.p | BEARISH | All shelves below mid | **Fail geometry** |
| GOLD | BULLISH | EMA20 -1.03; EMA50 -1.33; VWAP -1.32 (all outside band) | **Fail geometry** |
| DJ30.p | BULLISH | EMA20 -2.65; EMA50 -3.67; VWAP -4.39 | **Fail geometry** (Model 1 check in section 3.3) |
| USWTI.p | BULLISH on EMA200 slope, but price is below the EMA20/50 stack | EMA20 +2.06; EMA50 +2.01; VWAP +1.80 (all above mid for BUY) | **No BUY shelf** |
| EURUSD.pi / GBPUSD.pi | BULLISH | EMA20 -1.43 / -1.25; both outside band | **Fail geometry**; 2 dp bars cannot support wick test |

### 3.3 Model 1 (extreme mean-reversion, |Z| at least 2.0 from VWAP, RSI below 30 or above 70)

- Crypto: all VWAP Z-scores between -1.22 and +0.23. No |Z| of 2.0 or more. **Zero candidates.**
- DJ30 SHORT check: Z +2.12, RSI 66.88 (fails the RSI above 70 gate). The 19:45 15m bar's upper wick is 18 of 65 points (about 28%), which fails the 30% test. **Rejected.**
- GBPUSD: Z +2.05, RSI 61.67 (fails the RSI gate). FX bars are 2 dp, so the wick test cannot be measured. **Rejected.**
- EURUSD: Z +1.95, below 2.0. **Rejected.**
- **Model 1 result: zero admissible candidates.**

## 4. Blueprints

All plans are SELL LIMIT, passive (entry above MT5 bid), SL at least 1.5 ATR, TP at least 2.5R. Validated with `validate_plan` (PASS). Expiry 21:58:00 UTC. Stage file: `docs/trade_plans/ARENA_LIMIT_STAGES_20261008_2010.json`.

| Rank | Symbol | Direction | Entry (SELL LIMIT) | SL | TP | R | SL / ATR | Lot | Risk (USD) | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| **A** | DOGUSD.p | SELL LIMIT | 0.0840 | 0.0851 | 0.0812 | 2.55 | 1.83 | 1.0 | **11.00** | **Stage** (one slot) |
| **B** | NERUSD.p | SELL LIMIT | 4.617 | 4.744 | 4.299 | 2.50 | 1.51 | 1.0 | 12.70 | Alternate, expanded-only |

**Microstructure justification:**
- **A (DOGE):** 200 EMA slope -0.84% BEARISH. Entry 0.0840 sits on the EMA50 (0.0840), +0.17 ATR above mid 0.0839. EMA20 (0.0825) is below. Ask band 1.75M minimum across 12 receipts (2.09M now, which passes the 300k strict test). Top-20 imbalance -0.11 (ask 1.26x bid), which passes the 1.25x test. 1m CVD is mixed, so admission rests on depth and imbalance, not CVD. SL 0.0851 is 1.83 ATR above entry (floor 1.5 ATR). Risk 11.00 USD, inside the 11.04 preferred cap. The feed is 4 dp with ATR 0.0006, so the stop has coarse resolution. Spread 250 bps is exempt as a passive limit.
- **B (NEAR):** 200 EMA slope -1.39% BEARISH, RSI 39.0. Entry 4.617 is the EMA20 (4.6114 to 4.617), +0.28 ATR above mid 4.5935. Ask band 679k minimum across 12 receipts (699k now). Top-20 imbalance +0.07, so there is no ask-heavy edge. Lot minimum is 1.0, so risk is 12.70 USD at the 1.51 ATR stop, which is above the 11.04 preferred cap. Expanded-only.

**Sizing check:** SL at least 1.50 ATR on both (A 1.83, B 1.51); TP at least 2.50R on both (A 2.55, B 2.50); risk within 10.00-15.00 USD (A 11.00, B 12.70).

## 5. Footprint review (telemetry 15m, 1m CVD, L2 depth)

- **BTC book:** top-20 bid 1.77M USD vs ask 59k USD, imbalance +0.94. This is the opposite of a short setup. Another reason BTC is retired.
- **DOGE:** 1m CVD last 6 bars mixed (+19k, -103k, -94k, +90k, +8k, +126k). No clean exhaustion signal. Admission rests on depth and imbalance.
- **NEAR:** 1m CVD last 6 bars mixed (-14k, +53k, +68k, +37k, -152k, +83k). Admission rests on depth.
- **LTC 63.10:** 1m CVD mixed; depth 8/12. Watch only.
- **CFDs:** NAS100, SILVER, and USDJPY all printed 15m highs below their EMA or VWAP shelves. None touched the shelf, so no wick test is possible.
- **Trade authorization:** `DENIED_UNVERIFIED_ORDERFLOW` persists. Pioneer, stop-cluster, and liquidation-band fields are UNAVAILABLE. The ruling uses only Binance top-20 depth, CVD, and price geometry.

## 6. Governance

- **One order at a time.** Stage A only, with B as an alternate. Multi-order staging is prohibited. A and B must never be held together.
- **Resting-order rule for A:** delete immediately if the ask band at 0.0840 to 0.0851 thins by more than 50%, or if price drifts more than 2.0 ATR (0.0012) from 0.0840.
- **Resting-order rule for B (if ever staged):** delete immediately if the 4.617 ask band thins by more than 50%, or if price drifts more than 2.0 ATR (0.168) from 4.617.
- **Retired:** BTC 81,800 (19:58 alternate; price now above the level and the swing high is broken). LTC 62.600 (19:43 stage A). LNK 12.530 (19:43 alternate). The 19:58 DOGE stage remains valid and is carried into this ruling as stage A (re-validated at ATR 0.0006).
- **Do not re-enter SOL 109.10 SELL.**
- **Preferred-cap check:** A 11.00 is inside the 11.04 cap. B 12.70 is expanded-only.

## 7. Data caveats

- Briefing §2 (margin 0.00; "exactly ONE slot") and §4 (4,813.99 USD capital) are stale. Telemetry governs.
- Briefing "Top-20 N/A" depth is stale. Telemetry carries Binance L2 for crypto, sampled to top-20 levels only. Band depth is a lower bound.
- Briefing 48H profile values (for example BTC VAH 84,322 and LTC VAH 68.17) do not match telemetry `volume_profile` (BTC VAH 82,847 and LTC VAH 64.74). Telemetry was used for shelf geometry. This conflict is unresolved and did not change any admitted candidate.
- Indicator freshness: causal indicators are about 13 minutes old (last bar close 19:45 UTC). Quotes are fresh.
- CFD feeds are 2 dp for FX and 1 point for indices in the briefing. The Track 1 wick test cannot be measured on FX.
- `scripts/arena_dual_track_scan_v2.py` hard-codes 4,813.99 USD equity and was not used.
- Telemetry R values re-base after SL ratchets. Quote R on initial risk where stated.
