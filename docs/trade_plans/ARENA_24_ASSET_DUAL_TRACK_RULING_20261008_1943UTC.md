# Arena Council Dual-Track Ruling: 24-Asset Scan (briefing 2026-10-08 19:43:28 UTC)

**Telemetry basis:** `docs/telemetry/live_snapshot_latest.json`, as_of 2026-10-08 19:43:06 UTC (origin commit `84df80e` at scan time).
**Trade authorization in telemetry:** `DENIED_UNVERIFIED_ORDERFLOW`. This ruling is advisory. The desk executes.

## 0. Bottom line

1. **ETH #18706769 LONG 0.37 @ 2,411.00: HOLD.** Live SL is 2,434.52 (Phase-1 lock, +0.80R on initial risk). Mark 2,459.50, floating +17.95 USD (+1.65R on initial 29.40 USD risk). Target 2,484.50.
2. **Capacity: OPEN 1/2, 0 pending. One slot.** Stage **A only**.
3. **Top stage A: LTCUSD.pi SELL LIMIT 62.600**, SL 63.650, TP 59.975 (2.50R), 0.10 lot, risk **10.50 USD**. Inside the 11.04 preferred cap.
4. **Alternate B: BTCUSD.pi SELL LIMIT 81,800**, SL 82,850, TP 79,175 (2.50R), 0.01 lot, risk **10.50 USD**. Used only if A is deleted under the resting-order rule.
5. **Model 1: zero candidates.** No |z| >= 2.0 setup. Deepest: NAS100 z -1.55 (CFD, no shelf), NEAR z -1.33 (RSI 34.6, not extreme).
6. **Briefing §2 and §4 are stale.** §2 reports margin 0.00; telemetry shows 446.04 USD margin used (ETH only). §4 cites 4,813.99 USD capital. Telemetry governs: equity 4,847.74 USD, balance 4,829.79 USD.

## 1. Account state (telemetry 19:43:06 UTC)

| Field | Value |
|---|---|
| Balance / Equity | 4,829.79 / 4,847.74 USD |
| Margin used / free | 446.04 / 4,401.70 USD |
| G-1 floor / buffer | 4,795.00 USD (hard floor 4,775.00 USD) |
| Cushion above floor | 72.74 USD |
| Capacity | OPEN (1/2 filled, 0 pending) |

**Worst case (ETH stopped at its 2,434.52 lock, no other exposure):** ETH locked result +8.70 USD (0.37 x (2,434.52 - 2,411.00)), so balance-equivalent 4,838.49 USD. That is +43.49 USD over the 4,795.00 buffer. G-1 limit = 43.49 / 1.40 = 31.07 USD, so the 15.00 USD desk cap binds, not the buffer.

After stage A stops out: 4,838.49 - 10.50 = **4,827.99 USD** (+32.99 USD over the buffer).

## 2. Position review

### 2.1 ETH #18706769 (LONG 0.37 @ 2,411.00)

| Field | Value |
|---|---|
| Live SL | **2,434.52** (Phase-1 lock, +0.80R). Confirmed in telemetry. |
| TP | 2,484.50 (+2.50R) |
| Mark (19:43:06 UTC) | 2,459.50 |
| Floating | +17.95 USD; +1.65R on initial risk (R0 = 29.40 USD) |
| Locked at SL | +8.70 USD |

**Ruling: HOLD.** Keep the 2,434.52 stop.

**Next rung (proposal, not yet a rule):** ACTIVE_CONTEXT §6 names a Phase-2 trailing lock at +2.00R, which is **2,470.80** on initial risk. The context file gives no explicit stop level for that rung. Counter-proposal for desk confirmation: at >= 2,470.80, move SL to **2,455.10** (+1.50R). Above that, trail to 15m structure. Target 2,484.50 stays.

**Emergency cut** (unchanged): 15m close below 2,405.00.

### 2.2 SOL #18710722: CLOSED

Closed by the desk at the 19:23 cycle, realized -9.20 USD (-0.83R). No action.

**Re-entry rejected.** SOL 109.10 SELL is the thesis the desk just cut. A new SELL inside the same cycle is churn. SOL is excluded from this ruling (its ask-band depth is 3.67M minimum across 12 receipts, but that does not change the rejection).

### 2.3 Resting orders

None on the book. The DELETE rule is not applicable. The 19:23 stages (LTC 62.450, LINK 12.476) were never placed and are superseded by section 3.

## 3. Model 2 scan (trend-following pullback), all 24 assets

**Rules applied:** 200 EMA slope direction matches the trade. Adaptive micro-pullback 0.10-0.60 ATR to a shelf (EMA20, EMA50, VWAP, VAH/VAL, prior structure, or an ask-stack node). Passive limit, spread exempt (G1). Crypto Track 2 ANY-ONE-of: top-20 imbalance >= 1.25x, +/-0.50 ATR clustered depth >= 150k (300k strict), or 1m/5m CVD exhaustion. Persistence judged over the last 12 receipts (19:31-19:43 UTC), not single prints.

### 3.1 Crypto (all BEARISH on 200 EMA; no bullish crypto setup)

| Asset | Entry | Depth / persistence (min over 12 receipts) | Result |
|---|---|---|---|
| **LTCUSD.pi** | 62.600 on ask stack 62.55-62.61 | 386k, 12/12 | **Viable: A** |
| **BTCUSD.pi** | 81,800 on ask stack 81,718 / 81,901 | 228k, 12/12; imbalance -0.96 | **Viable: B** |
| **LNKUSD.p** | 12.530 on ask stack 12.527-12.532 | 206k, 12/12 | **Viable: C** |
| **NERUSD.p** | 4.585 on ask stack 4.582-4.586 | 569k, 12/12 | Viable, **expanded-only (14.00 USD)** |
| **DOGUSD.p** | 0.0838 | 1.29M, 12/12 | Viable, **expanded-only (12.00 USD)** |
| BNBUSD.p | EMA20 732.2 / ask 730.65 | Pass 4/12 and 5/12 | **Fails persistence** |
| XRPUSD.pi | 1.3742 | 1.46M, 12/12 | **Unsizeable** (min-lot risk at 1.5 ATR SL = 18.7 USD, over 15.00) |
| ADAUSD.p | VAL 0.2322 | Shelf present | **Unsizeable** (min-lot risk over 15.00) |
| TRXUSD.p | Ask 0.3330 | 144k (<150k); slope -0.06% | **Fails depth; trend too weak** |
| AVAXUSD.p | Ask 10.101 (band edge) | Not verified | **Not admissible** (no EMA/VWAP shelf at entry; persistence not verified) |
| DOTUSD.pi | None in band | n/a | **No setup** |
| BCHUSD.p | None in band | n/a | **No setup** (marketable at mid) |
| SOLUSD.p | Ask 109.10 | 3.67M, 12/12 | **Excluded** (cut thesis, section 2.2) |
| ETHUSD.pi | Held | n/a | Managed in section 2.1 |

### 3.2 CFD

| Asset | Regime | Shelf check | Result |
|---|---|---|---|
| DJ30.p | BULLISH, slope +0.003% | No long-side shelf in band; short invalid on BULLISH | **No setup** |
| SP500.p | BEARISH | No in-band shelf | **No setup** |
| NAS100.p | BEARISH; z -1.55 | No in-band shelf | **No setup** |
| SILVER | BEARISH | VWAP 59.278 (+0.46 ATR). The 19:15 bar high of 59.21 did not reach the VWAP, so there was no test of the shelf | **Not punchable** |
| USWTI.p | BULLISH | No pullback shelf below mid in band | **No setup** |
| GER40.p / GOLD / USDJPY | BEARISH / RANGE / BEARISH | No shelf in band | **No setup** |
| EURUSD.pi / GBPUSD.pi | Flat / BULLISH | Bars at 2 dp: wick and volume cannot be measured | **Fails by data resolution** |

Track 1 for CFD requires a 15m rejection wick >= 30% of bar range AND volume >= 0.8x the 20-bar average at the shelf. No CFD meets both legs.

### 3.3 Model 1 (mean-reversion)

No |z| >= 2.0 setup. Deepest: NAS100 z -1.55 (CFD, no shelf); NEAR z -1.33 (RSI 34.6, not extreme). **Zero candidates.**

## 4. Blueprints

All plans are SELL LIMIT, passive, validated with `validate_plan` (PASS) in the 19:43 build. Expiry 21:44:00 UTC. Stage file: `docs/trade_plans/ARENA_LIMIT_STAGES_20261008_1943.json`.

| Rank | Asset | Entry (SELL LIMIT) | SL | TP | Lot | Risk (USD) | R | SL (ATR) | Status |
|---|---|---|---|---|---|---|---|---|---|
| **A** | LTCUSD.pi | 62.600 | 63.650 | 59.975 | 0.10 | **10.50** | 2.50 | 2.32 | **Stage** (one slot) |
| **B** | BTCUSD.pi | 81,800 | 82,850 | 79,175 | 0.01 | **10.50** | 2.50 | 2.67 | Alternate |
| **C** | LNKUSD.p | 12.530 | 12.800 | 11.855 | 0.40 | **10.80** | 2.50 | 2.39 | Alternate |
| D | NERUSD.p | 4.585 | 4.725 | 4.235 | 1.00 | 14.00 | 2.50 | 1.55 | Expanded-only (needs 15.00 cap) |
| E | DOGUSD.p | 0.0838 | 0.0850 | 0.0808 | 1.00 | 12.00 | 2.50 | 1.71 | Expanded-only (needs 15.00 cap) |

**Justification:**
- **A (LTC):** 200 EMA slope -0.74% BEARISH. Entry sits on the 62.55-62.61 ask stack, which held at least 386k in each of the last 12 receipts. EMA20 (62.25) is below the entry, so this is a stack retest, not an EMA20 retest. EMA50 (63.16) is about +1.5 ATR, outside the band. Spread 48 bps is exempt as a passive limit.
- **B (BTC):** 200 EMA slope -0.33% BEARISH. Ask-heavy book (imbalance -0.96). Entry 81,800 is inside the 81,718 / 81,901 stack. EMA50 81,901 is about +0.58 ATR. Persistence 228k minimum across 12 receipts.
- **C (LINK):** 200 EMA slope -0.87% BEARISH. Entry on the 12.527-12.532 ask stack (206k minimum across 12 receipts).
- **D (NEAR) and E (DOGE):** both clear depth and persistence. Their 1-lot minimum puts risk above the 11.04 preferred cap, so they are alternates that need the 15.00 USD desk cap. NEAR EMA20 4.624 retest was present in only 4 of 12 receipts, so the 4.585 stack was used instead.

**Sizing check:** SL >= 1.50 ATR on all five; TP >= 2.50R on all five; risk within 10.00-15.00 USD.

## 5. Governance

- **One order at a time.** Stage A only, with B as the alternate. Multi-order staging is prohibited. A and B must never be held together.
- **Resting-order rule:** delete A immediately if the 62.55-62.61 ask band thins by more than 50%, or if price drifts more than 2.0 ATR from 62.600.
- **Superseded:** LTC 62.450 and LINK 12.476 (19:23 stages), and LTC 62.330 and LINK 12.456 (19:15 stages). Do not re-stage.
- **Budget:** stage A risk 10.50 USD is inside the 11.04 preferred cap and leaves 32.99 USD headroom over the buffer after a stop-out.

## 6. Data caveats

- Briefing §2 (margin 0.00; "exactly ONE slot") and §4 (4,813.99 USD capital) are stale. Telemetry governs.
- Repo 15m parquet files are stale. Persistence and depth come from telemetry receipts, not parquet.
- FX bars are 2 dp, which is insufficient for Track 1 wick analysis; those assets fail by data resolution.
- `scripts/arena_dual_track_scan_v2.py` hard-codes 4,813.99 USD equity and was not used.
- Telemetry `r_multiple` re-bases after each SL ratchet. Quote R on initial risk.
