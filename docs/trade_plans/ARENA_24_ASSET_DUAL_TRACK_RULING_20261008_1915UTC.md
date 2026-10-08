# Arena Council Dual-Track Ruling: 24-Asset Scan (briefing 2026-10-08 19:13:28 UTC)

**Telemetry basis:** `docs/telemetry/live_snapshot_latest.json`, as_of 2026-10-08 19:15:06 UTC (origin commit `2f8030c`).
**Trade authorization in telemetry:** `DENIED_UNVERIFIED_ORDERFLOW`. This ruling is advisory. The desk executes.
**Account (telemetry 19:15:06):** Balance 4,838.99 USD | Equity 4,844.66 USD | Margin used 876.92 USD | Floor 4,775.00 | Buffer 4,795.00 | Cushion over floor +69.66 USD.
**Capacity:** `HARD_ADMISSION_FREEZE (2/2 filled, 0 pending)`.

## 0. Bottom line

1. **SOL #18710722 SHORT: EMERGENCY SHELF CUT TRIGGERED. Close at market now.** The 19:00-19:15 15m close is about 108.40-108.55, above the 108.35 cut level. Realized loss is about -7.04 USD (-0.64R), against -11.04 USD at the stop.
2. **ETH #18706769 LONG: HOLD.** The operative stop is 2,415.41 (Phase-0 lock). The telemetry label `PHASE_1_PROFIT_LOCKED` is premature. Phase-1 has not armed (needs 2,455.10; session high 2,448.80).
3. **Capacity:** no punch while both exposures are open. After the SOL close, exactly one slot opens. Only one pending order may exist at a time.
4. **Top-2 LIMIT stages (capacity-gated, validated at 19:16 UTC):**
   - **A. LTCUSD.pi SELL LIMIT 62.330**, SL 63.377, TP 59.712, 0.10 lot, risk 10.47 USD, 2.5005R.
   - **B. LNKUSD.p SELL LIMIT 12.456**, SL 12.717, TP 11.803, 0.40 lot, risk 10.44 USD, 2.5019R. Alternate only; use it only if A is deleted.
5. **Model 1: zero candidates.** No asset has |z| >= 2.0 with RSI < 30 or > 70.
6. **Prior standbys retired:** DJ30 (regime flipped BULLISH), BTC, BNB and BCH (entries now at or below mid, so they would be marketable), DOT (depth 48k), AVAX (depth 145k < 150k).

## 1. References

- Telemetry: `docs/telemetry/live_snapshot_latest.json` (committed to origin every 60 s).
- Ledger: `docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md`.
- `.agents/rules/ACTIVE_CONTEXT.md`: now present in the repository (it was absent at 18:28). It was read. Its operational rules are consistent with this ruling: USD notation, no speculative scratch files, all positions tracked from telemetry.

## 2. Account state and the stale briefing §2

The briefing §2 snapshot (Balance 4,838.99 / Equity 4,845.12 / Margin 0.00 / "exactly ONE slot") is stale. Telemetry shows two live positions and margin of 876.92 USD. Per the standing interpretation, telemetry plus §3 govern. Capacity is 2/2 and admission is frozen.

**Post-SOL-exit worst case (ETH stop-out at the lock, no other positions):**
- Balance 4,838.99 - 7.04 (SOL cut) + 1.63 (ETH SL lock) = **4,833.58 USD**.
- Headroom over the 4,795 buffer: **+38.58 USD**.
- G-1 risk limit: (4,833.58 - 4,795) / 1.40 = 27.56 USD, so the 15.00 desk cap is the binding constraint, not the buffer.
- With LTC A stopped out after it fills: 4,833.58 - 10.47 = 4,823.11 USD (+28.11 over buffer).

## 3. Position reviews

### 3.1 SOL #18710722 SOLUSD.p SHORT 0.08 @ 107.72 (contract 100)

| Field | Value |
|---|---|
| Live SL / TP | 109.10 / 104.27 |
| Mark (19:15:06) | 108.63 (mid 108.505, bid 108.39, ask 108.62) |
| Floating | -7.28 USD (-0.66R on initial basis; R0 = 1.38 price) |
| Emergency cut | 15m close >= 108.35 |
| Cut status | **TRIGGERED** |

**Evidence for the 19:00-19:15 15m close.** The repository parquet is stale (it ends at 16:00 or 18:15), so the close is taken from the 1-minute telemetry snapshots:
- 19:04:06 mid 108.59; 19:09:06 mid 108.27; 19:14:06 mid 108.545, bid 108.43; 19:15:06 mid 108.505, bid 108.39.
- The close is estimated at **108.40-108.55**. Even the lowest bid in the final minute (108.39) clears 108.35.

**Ruling: EMERGENCY SHELF CUT. Buy-to-close SOLUSD.p 0.08 at market now.**
- Expected realized: about -7.04 USD (-0.64R) at a 108.60 fill; about -7.20 USD at the 108.62 ask. Against -11.04 USD at the stop.
- Verify the MT5 19:00 15m bar close on the chart. If MT5 prints a close below 108.35, hold and re-rule.
- Reason to act now: the cut is a close-based rule and the bar has already closed. Delay risks a further push through the 108.5 wall stack.
- Overhead ask stack: 108.54-108.73 (top levels 729k at 108.69, 486k at 108.73). Bid stack below: 108.46 (944k), 108.37 (825k).

### 3.2 ETH #18706769 ETHUSD.pi LONG 0.37 @ 2,411.00 (contract 1)

| Field | Value |
|---|---|
| Live SL / TP | 2,415.41 / 2,484.50 |
| Mark (19:15:06) | 2,446.0 (mid 2,447.35) |
| Floating | +12.95 USD (+1.19R on initial basis; R0 = 29.40 price) |
| Locked worst case | +1.63 USD at SL 2,415.41 |
| Session high | 2,448.80 |

**Ratchet status.** The telemetry label `PHASE_1_PROFIT_LOCKED` and R = 7.94 are artifacts of the re-based R (live SL distance is now 4.41, the Phase-0 lock distance). The actual price is +1.19R on the initial risk. Phase-1 has not armed. The SL field (2,415.41) is correct.

**Ruling: HOLD.**
- Phase-1 arm: at >= 2,455.10 (+1.50R), move SL to **2,434.52** (+0.80R).
- Target: 2,484.50 (+2.50R).
- Emergency cut: 15m close < 2,405.00.
- Overhead cap: SELL wall 2,448.35 (558,814 USD), directly above mark. Do not chase into it. Let the stop manage the trade.

### 3.3 Resting orders

None (`pending_orders: []`). The resting-order DELETE rule is therefore N/A this cycle.

## 4. Model 1 (extreme mean-reversion): zero candidates

Rule: |z| >= 2.0 SD from session VWAP with RSI < 30 (long) or > 70 (short).

| Asset | z | RSI | Result |
|---|---|---|---|
| NAS100.p (CFD) | -1.80 | 35.2 | Fails |
| NEAR (NERUSD.p) | -1.54 | 33.0 | Fails (deepest crypto stretch) |
| SOL / BNB / ETH / DJ30 / GBPUSD / EURUSD | -1.61 to +1.57 | 31 to 63 | Fail |

No Model 1 entry is admissible.

## 5. Model 2 (trend-following pullback): scan of all 24

Rules: 200 EMA slope direction matches the trade. Micro-pullback 0.10-0.60 ATR to a shelf (EMA20, EMA50, VWAP, VAH, VAL, POC). Entry is passive. Crypto Track 2 needs one of: top-20 imbalance >= 1.25x, clustered depth within +/-0.50 ATR of the entry >= 150k USD (300k strict), or 1m CVD exhaustion. CFD Track 1 needs 15m volume >= 0.8x the 20-bar average and a rejection wick >= 30% at the shelf. Spread is exempt for passive limits.

**Crypto short setups, 19:15 telemetry:**

| Asset | Shelf offset (ATR from mid) | Ask band +/-0.5 ATR (USD) | Slope | Result |
|---|---|---|---|---|
| **LTCUSD.pi** | EMA20 +0.17 (entry 62.330 = +0.32) | **466,078** (300k strict) | -0.74% | **ADMISSIBLE, A** |
| **LNKUSD.p** | EMA20 +0.24 (entry 12.456 = +0.50) | **233,313** (150k floor) | -0.87% | **ADMISSIBLE, B** |
| AVAXUSD.p | EMA20 +0.54 | 145,016 at the valid entry | -1.06% | Fails depth floor |
| TRXUSD.p | EMA20 +0.33 | 153,000 | -0.06% | Trend too weak |
| DOTUSD.pi | VAL +0.56 | 48,367 | -0.99% | Fails depth |
| BCHUSD.p | EMA20 +0.80 | 0 | -0.87% | Shelf out of band |
| BNBUSD.p | EMA20 +1.32 | n/a | -0.65% | Shelf out of band |
| BTCUSD.pi | EMA20 -0.07 (below mid); 81,436 wall +0.09 | 939k wall at 81,436 | -0.34% | No valid passive shelf (81,436 is 0.01 ATR below the 0.10 floor) |
| XRPUSD.pi, ADAUSD.p, DOGEUSD.p, NEAR | Shelves -0.5 to +1.4 ATR or far above band | Fail | BEARISH | No admissible shelf |
| ETH, SOL | Held positions | n/a | BEARISH | Managed in section 3 |

**Crypto long setups:** none. All crypto is BEARISH on the 200 EMA.

**CFD setups, 19:15 telemetry:**

| Asset | Regime / slope | Shelf check | Result |
|---|---|---|---|
| DJ30.p | **BULLISH, +0.0003%** | No short shelf (VAH +0.57 is counter-trend); no long shelf in band | **Rejected** (18:28 short invalid) |
| SP500.p | BEARISH, -0.04% | EMA20 +0.51 ATR (7,760.49). Last 3 bars never reached the shelf (highs 7,758.55). Track-1 wick/volume not evidenced at the shelf. | Not punchable (watch) |
| NAS100.p | BEARISH, -0.12% | EMA20 +1.81 ATR (out of band) | No setup |
| GER40.p | BEARISH, -0.08% | VAH -0.06 (no) | No setup |
| GOLD / SILVER | BEARISH, flat | No shelf in band | No setup |
| USDJPY.pi | BEARISH, -0.02% | EMA20 +1.28 ATR (out of band) | No setup |
| USWTI.p | BULLISH, +0.10% | No pullback shelf in band below mid | No setup |
| GBPUSD.pi | BULLISH, +0.002% | EMA20 -0.78 ATR (out of band) | No setup |
| EURUSD.pi | RANGE_BOUND | None | No setup |

Index and commodity CFDs have no whale or CVD feed in telemetry, so Track-1 relies on the 15m bars in the briefing only.

## 6. Top-2 LIMIT stages (capacity-gated)

**Gate:** capacity is 2/2. Do not punch either stage until SOL #18710722 is closed. After that, exactly one pending order at a time. The two stages expire at **2026-10-08 20:34:10 UTC**. If the SOL close has not happened by then, re-rule.

### A. LTCUSD.pi SELL LIMIT (Model 2, primary)

| Field | Value |
|---|---|
| Entry (SELL LIMIT) | **62.330** (= EMA20 shelf 62.261, +0.32 ATR above mid 62.18) |
| Stop loss | **63.377** (2.24 ATR, 1.047 price distance) |
| Take profit | **59.712** (2.5005R) |
| Volume | **0.10 lot** (contract 100; step 0.10) |
| Nominal risk | **10.47 USD** (within the 11.04 preferred cap) |
| Stressed risk | ~15.09 USD (per the 18:28 validator; within the 15.80 stress ceiling) |
| Shelf | EMA20 (62.261) with the 62.33 ask level (102k) sitting on the entry |
| Depth | Ask band +/-0.5 ATR = 466,078 USD (above 300k strict) |
| Trend | 200 EMA slope -0.74%, BEARISH |
| Spread | 48 bps (exempt for passive limit) |
| Expiry | 2026-10-08 20:34:10 UTC |
| Validation | `validate_plan` PASS at 19:16 UTC |

**Resting-order rule (standing):** delete the order immediately if the supporting ask stack (62.19-62.38) thins by more than 50%, or if price drifts more than 2.0 ATR (0.93 USD) from the 62.330 entry.

### B. LNKUSD.p SELL LIMIT (Model 2, alternate)

| Field | Value |
|---|---|
| Entry (SELL LIMIT) | **12.456** (= +0.50 ATR above mid 12.3985; +0.26 ATR above EMA20 12.426) |
| Stop loss | **12.717** (2.26 ATR, 0.261 price distance) |
| Take profit | **11.803** (2.5019R) |
| Volume | **0.40 lot** (contract 100; step 0.10) |
| Nominal risk | **10.44 USD** (within the 11.04 preferred cap) |
| Shelf | EMA20 +0.26 ATR; entry sits behind the 12.399-12.418 ask stack |
| Depth | Ask band +/-0.5 ATR = 233,313 USD (150k floor) |
| Trend | 200 EMA slope -0.87%, BEARISH |
| Spread | 69 bps (exempt for passive limit) |
| Expiry | 2026-10-08 20:34:10 UTC |
| Validation | `validate_plan` PASS at 19:16 UTC |

**Use rule:** B is an alternate. Stage it only if A is deleted or not filled. Never hold A and B together, because multi-order staging is prohibited.

**Caveat:** the LINK entry is at the outer edge of the 0.60 ATR band (+0.50). If price drifts more than 2.0 ATR (0.23 USD) from 12.456, delete the order.

## 7. Resting-order and position governance

- **SOL:** emergency cut as above. If the cut is not executed, the position stays open and the 15m close test runs again next bar.
- **ETH:** ladder as in 3.2. Watch for the 2,455.10 arm.
- **Capacity:** after the SOL close, one slot. Punch A only. Keep B on the shelf as an alternate, not as a second order.
- **Deletion rule:** if A is staged and then the wall thins by more than 50% or price drifts more than 2.0 ATR, delete immediately (per the standing rule).

## 8. Excluded and unsizeable

- XRPUSD.pi and ADAUSD.p: minimum-lot risk exceeds 15.00 USD. Unsizeable.
- DJ30, BTC, BNB, BCH, DOT, AVAX, TRX: rejected (section 5).
- Expanded-only plans (11.04 < risk <= 15.00): none. Both admissible plans sit inside the 11.04 preferred cap.

## 9. Data notes

- Crypto order books are taken from the live telemetry (`bids_top20`, `asks_top20`, `l2_wall_levels`). The briefing order-book fields read N/A and were not used.
- `l2_wall_levels` are `SAMPLED_ONLY_NOT_CONTINUOUS`. Persistence is judged over the 13 receipts, not single prints.
- The repository 15m parquets are stale. The SOL close was therefore taken from the minute snapshots. The desk should confirm on the MT5 chart before acting.
- The scanner `scripts/arena_dual_track_scan_v2.py` hard-codes equity at 4,813.99 and reads the stale parquets, so it was not used for this cycle. The scan used a temp script on telemetry only (no repository writes).
- Telemetry R (`r_multiple_basis: live_sl_distance`) re-bases after each ratchet. Use the initial risk for R statements.

---

## 10. ADDENDUM 19:23:06 UTC (supersedes sections 0, 3.1, 6 where they conflict)

**Telemetry 19:23:06 (origin `74c41c7`):** SOL #18710722 is CLOSED. Balance 4,838.99 to **4,829.79** (realized **-9.20 USD**, -0.83R against -11.04 at the stop). The desk executed the cut about four minutes after the 19:15 trigger; the SOL mark was 108.91 at 19:19:06. Equity 4,845.22 · margin 446.04 · free margin 4,399.18.

**Capacity: OPEN 1/2, 0 pending. One slot is open.**

**Retired 19:15 stages:**
- **LTC 62.330:** price reached the shelf (mid 62.34, offset -0.02 ATR). Fails the 0.10-0.60 ATR micro-pullback minimum.
- **LINK 12.456:** mid 12.451, offset +0.04 ATR. Fails the same minimum.
- Pending orders are 0, so nothing needs deleting.

**Replacement stages (validated at 19:23:06, `docs/trade_plans/ARENA_LIMIT_STAGES_20261008_1923.json`):**

| | A. LTCUSD.pi SELL LIMIT (primary, stage this) | B. LNKUSD.p SELL LIMIT (alternate) |
|---|---|---|
| Entry | **62.450** (+0.24 ATR above mid 62.34; inside ask stack 62.41-62.46) | **12.476** (+0.22 ATR above mid 12.451; above ask stack 12.453-12.464) |
| SL | **63.500** (2.25 ATR) | **12.746** (2.34 ATR) |
| TP | **59.825** (2.50R) | **11.801** (2.50R) |
| Volume | 0.10 lot | 0.40 lot |
| Risk | **10.50 USD** | **10.80 USD** (both within the 11.04 preferred cap) |
| Depth (ask band +/-0.5 ATR) | 425,045 USD (above 300k strict) | 220,866 USD (150k floor) |
| Spread | 48 bps (passive, exempt) | 69 bps (passive, exempt) |
| Expires | 2026-10-08 21:23:06 UTC | 2026-10-08 21:23:06 UTC |

**Rules:** stage **A only**, one pending order. B is an alternate, used only if A is deleted under the resting-order rule (ask stack thins more than 50%, or price drifts more than 2.0 ATR from entry). Never hold A and B together.

**Post-cut account:** balance 4,829.79 + ETH lock 1.63 = worst-case equity **4,831.42 USD** · headroom over the 4,795 buffer **+36.42 USD** · G-1 limit (36.42 / 1.40) = 26.0 USD. The 15.00 desk cap binds, not the buffer. Stage A adds 10.50 USD worst case, leaving 4,820.92 USD.

**ETH #18706769:** mark 2,452.70, 2.40 USD below the Phase-1 arm at 2,455.10. Ruling unchanged: HOLD. At >= 2,455.10, move SL to **2,434.52**. The telemetry label `PHASE_1_PROFIT_LOCKED` remains premature until the SL field moves.

**Model 1:** still zero candidates.
