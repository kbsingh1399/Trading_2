# ARENA 24-ASSET DUAL-MODEL RULING + PENDING ORDER AUDIT
**Machine receipt:** `docs/telemetry/live_snapshot_latest.json` — `protocol: omni.telemetry.v3.observed_only`, `generation_id c56410ac9d324a81bb3f7986f630d137`, `as_of_utc 2026-10-15 13:42:12 UTC` (snapshot age 148.5 s at audit open, inside the 180 s latency gate).
**Account:** MT5 #5064568 (Blueberry Markets) — equity 4,862.28 USD, 0 filled positions, 2 pending SELL_LIMIT tickets.
**Advisory status:** The receipt carries the static provenance tag `trade_authorization: DENIED_UNVERIFIED_ORDERFLOW` (publisher never submits orders) and per-asset `portfolio_gating: ADMISSION_FROZEN_UNVERIFIED_DATA`. This ruling is an analytical gate assessment. Nothing below is staged, modified or cancelled by Arena.

---

## 1. Data-contract gate (Step 1)

| Check | Result |
|---|---|
| Snapshot age vs 180 s latency gate | PASS (148.5 s) |
| Quotes | 24/24 `FRESH`, MT5 L1 tick source |
| 15m / 1H / 4H bar monotonicity, zero nulls, OHLC+volume assertions | 0 violations across 24 assets x 3 timeframes |
| Binance CVD 1-minute bucket series | 59 buckets, strictly monotonic, BTC and ETH both continuous |
| Cross-venue basis available | Crypto yes (`venue_basis`): BTC MT5 = Binance -101.005 / HL -55.0; ETH MT5 = Binance -2.89 / HL -1.575 |
| TradFi basis | `None` for indices/commodities/FX — HTF levels are broker-native, no mapping required |
| HTF EMA200 hierarchy verifiability | **LIMITED**: only 96 x 1H and 96 x 4H bars shipped, so a 200-period HTF EMA cannot be recomputed. HTF hierarchy verified at 1H/4H EMA20/EMA50 + slope; 15m EMA200 (`bars_used=800`) used as the long-horizon reference. |
| Per-asset Arkham mapping | **CONTRACT GAP**: `assets_matrix_24[symbol].arkham_onchain` is absent in this snapshot although the SOP schema states it is mapped. Only the top-level `onchain_arkham_intelligence` block is present. |
| Arkham content | `feed_status STREAMING_ACTIVE`, sentiment `NEUTRAL_BALANCED_FLOW`, exchange_inflow_events 0, exchange_outflow_events 0, whale_alerts [] — zero directional on-chain evidence this cycle. |
| p_win calibration | lower bound 0.4197, `calibrated=False`, n=17 wins=11, `p_win_calibration_minimum_sample=100` (Clopper-Pearson exact, one-sided 95 pct). Not a calibrated edge estimate. |

---

## 2. Account health and capital floor audit

| Metric | Value |
|---|---|
| Balance / Equity / Margin used / Free margin | 4,862.28 / 4,862.28 / 0.00 / 4,862.28 USD |
| Hard floor | 4,775.00 USD |
| Floor cushion (equity - floor) | +87.28 USD |
| Operating threshold (floor + 20.00) | 4,795.00 USD — surplus +67.28 USD |
| Staged nominal risk (2 pending tickets) | 11.20 + 10.98 = 22.18 USD |
| Broker-valued contingent stress (x1.25 + 2.00 execution per ticket) | 16.000 + 15.725 = 31.725 USD |
| Stressed post-joint-stop equity | 4,830.555 USD — preserves floor, buffer +35.555 USD |
| Capacity | OPEN: 2/4 joint-fill slots used (0 filled, 2 pending), 2 available |
| Margin on fill (both pendings) | 2,350.585 USD; free margin after fills 2,511.695 USD |
| Equity vs 5,000.00 USD initial capital | -2.75 pct |

Floor geometry is intact and is **not** the binding constraint this cycle. The binding constraints are microstructure gates.

---

## 3. Pending orders audit (Task 3)

Both tickets are passive SELL_LIMIT shorts in a confirmed bearish HTF regime. Directional thesis is aligned with the dominant trend; the geometry and microstructure gates are not.

### Ticket 18954801 — BTCUSD.pi SELL_LIMIT 0.04 @ 81,280.00, SL 81,560.00, TP 80,440.00
- Mid 80,567.50 (bid 80,558.00 / ask 80,577.00), ATR14 312.0218, half-spread 9.50, spread 2.36 bps (PASS, crypto ceiling 25.0 bps).
- **Runway: (81,280.00 - 80,567.50) / 312.0218 = 2.283 ATR — FAILS the 2.0 ATR limit (Anti-Trap 5 / Rule 7).**
- **Entry is staged inside an un-swept opposing buy-stop cluster: 81,280 lies inside [81,200, 81,300] = 1,768,822 USD (above the 1,000,000 USD intraday micro-cluster floor). Anti-Trap 1 violation.**
- **SL 81,560.00 lies INSIDE the institutional buy-stop band [81,500, 81,600] = 1,374,178 USD. Anti-Trap 3 / Rule 4 violation.** Canonical bunker: SL >= 81,400 + 0.50 x 312.0218 + 9.50 = 81,565.51 (nearest band) or, including the 81,500-81,600 micro-cluster, SL >= 81,600 + 156.01 + 9.50 = **81,765.51**. Current SL is 5.51 and 205.51 points short respectively.
- Cash risk 280 x 0.04 x 1.0 = 11.20 USD (inside Tier 1), stressed 16.00 USD, R:R = 840/280 = 3.00.
- **Whale gate FAIL:** BTC has 0 `gate_g7_eligible` walls. The supporting ask wall 81,163.00 (25,028,591 USD) shows `persist_s 423.0`, `presence_frac 0.7500`, `gate_g7_eligible False`, status `INSUFFICIENT_PERSISTENCE`. Mapped to the MT5 grid (HL basis -55.0) it sits at ~81,108 — i.e. the limit at 81,280 sits ABOVE the shielding wall, so a fill would require consuming that 25.0M offer.
- Tape: session CVD -34.15M, 24h -56.58M, weekly -170.38M (bearish), but the last four 1-minute deltas are +1.90M, +0.85M, +1.98M, +0.22M off the 80,064 low — a **positive divergence / absorption impulse**, adverse for a fresh short entry.
- Order age: 6,607 s (1 h 50 m) unfilled.
- **VERDICT: CANCEL IMMEDIATELY (C).**

### Ticket 18956325 — ETHUSD.pi SELL_LIMIT 0.61 @ 2,377.00, SL 2,395.00, TP 2,340.00
- Mid 2,351.45 (bid 2,349.40 / ask 2,353.50), ATR14 12.3202, half-spread 2.05, spread 17.44 bps (PASS, crypto ceiling 25.0 bps).
- **Runway: (2,377.00 - 2,351.45) / 12.3202 = 2.074 ATR — FAILS the 2.0 ATR limit.**
- **Entry 2,377 lies inside the buy-stop cluster [2,370, 2,380] = 929,499 USD and immediately beneath the institutional band [2,380, 2,390] = 1,366,666 USD. Anti-Trap 1 violation.**
- **SL 2,395.00 lies INSIDE the buy-stop band [2,390, 2,400] = 537,970 USD, and inside the wider un-swept stack [2,400, 2,410] 1,814,685 / [2,410, 2,420] 1,144,696 / [2,420, 2,430] 2,716,520 / [2,430, 2,440] 1,385,255. Anti-Trap 3 / Rule 4 violation.**
  - SL >= 2,400 + 6.16 + 2.05 = 2,408.21 (nearest band) -> risk at 0.61 lots = 19.04 USD, above the 14.50 USD Tier-1 cap.
  - SL >= 2,440 + 6.16 + 2.05 = 2,448.21 (outer boundary of the stack) -> risk at 0.61 lots = 43.44 USD, i.e. 3.0x the envelope; max compliant size is 0.20 lots.
- TP 2,340.00 sits exactly on the upper edge of the sell-stop cluster [2,330, 2,340] = 1,542,300 USD rather than front-running it by 5-10 bps (compliant TP ~2,341.2-2,342.4).
- Cash risk 18 x 0.61 = 10.98 USD, stressed 15.725 USD, R:R = 37/18 = 2.056.
- **Whale gate FAIL:** ETH shows 7 `gate_g7_eligible` walls (persist up to 7,273.0 s, presence 0.9407) but the largest is only 663,503 USD, versus the 5,000,000 USD BTC/ETH threshold after the SOP's 1,000,000 USD intraday micro-cluster relaxation. The large 14,814,078 USD SELL wall at 2,385.00 shows `persist_s 77.2`, `gate_g7_eligible False` -> fail-closed as unverified.
- Tape: session CVD -112.70M, 24h -214.84M, weekly -227.45M; last four 1-minute deltas +242k, +60k, +184k, +82k after a -766k minute -> deceleration, adverse for a fresh short.
- Order age: 1,197 s (20 m).
- **VERDICT: CANCEL IMMEDIATELY (C).**

### Why neither ticket qualifies for verdict (B) MODIFY
A modification could repair runway and bunker placement, but not the microstructure gates. Worked examples:
- BTC short rebuilt at the Session VWAP shelf 81,052.55 (1.55 ATR from mid, runway-compliant) with the canonical SL 81,765.51: risk distance 712.96 points -> 0.02 lots = 14.26 USD (compliant). The first material opposing barrier below is the sell-stop cluster [80,000, 80,100] = 25,439,638 USD; a 5-10 bps front-run TP at 80,060 gives reward 992.55 points = **1.39R — fails the 2.0R gate.** Deeper targets (79,650 / 79,550) reach only 1.97R / 2.11R while the path must traverse two intermediate institutional magnets.
- ETH short rebuilt at the 20 EMA shelf 2,358.23 (0.55 ATR) with the conservative SL 2,448.21: risk 89.98 points -> 0.12 lots = 10.80 USD (compliant). The first magnet below is the sell-stop cluster [2,330, 2,340]; a front-run TP at 2,338.83 gives reward 19.40 points = **0.216R.**
The overhead institutional bunkers are wider than the downside runway. Both cards are geometrically unpayable after a lawful stop. Additionally, no modification can create a qualifying shielding wall, because the qualifying-wall population is empty across the whole book (Section 4).

---

## 4. Task 1 — 24-asset dual-engine screen

Gate legend: SPR = MT5 spread gate (25.0 bps crypto / 5.0 bps TradFi); REG = HTF regime from 1H and 4H EMA20/EMA50 stacks and slopes; |Z| = session VWAP z-score; IMB = L2 top-20 book imbalance; Q = count of shielding walls passing the DOUBLE gate (`gate_g7_eligible True` AND `persist_s >= 180` AND `presence_frac >= 0.85` AND notional >= institutional threshold).

| Asset | SPR bps | Gate | REG (1H/4H) | Z | IMB | Best g7 wall / threshold | Q | Fatal blocker |
|---|---|---|---|---|---|---|---|---|
| BTC | 2.36 | PASS | BEAR/BEAR | -1.45 | -0.73 | 0 / 5,000,000 | 0 | No g7 wall; max presence 0.80 |
| ETH | 17.44 | PASS | BEAR/BEAR | -0.82 | -0.88 | 663,503 / 5,000,000 | 0 | g7 walls are 7.5x under the notional floor |
| SOL | 22.57 | PASS | BEAR/BEAR | -0.76 | +0.06 | 200,540 / 500,000 | 0 | Notional floor; IMB wrong side |
| BNB | 6.96 | PASS | BEAR/BEAR | -0.38 | -0.58 | 0 / 500,000 | 0 | No g7 wall (max persist 0 s) |
| XRP | 30.75 | FAIL | BEAR/BEAR | -0.97 | -0.24 | 0 / 500,000 | 0 | Spread 30.75 > 25.0 bps |
| ADA | 99.68 | FAIL | BEAR/BEAR | -0.05 | -0.03 | 0 / 500,000 | 0 | Spread 99.68 bps; no |Z| edge |
| DOGE | 264.65 | FAIL | BEAR/BEAR | +0.51 | -0.40 | 0 / 500,000 | 0 | Spread 264.65 bps |
| TRX | 30.33 | FAIL | MIX/BEAR | -1.09 | +0.17 | 0 / 500,000 | 0 | Spread; 1H stack mixed |
| DOT | 197.09 | FAIL | BEAR/BEAR | -1.37 | +0.23 | 0 / 500,000 | 0 | Spread; zero L3 walls |
| LINK | 74.34 | FAIL | BEAR/BEAR | -0.81 | -0.07 | 0 / 500,000 | 0 | Spread |
| BCH | 25.77 | FAIL | BEAR/BEAR | +0.62 | -0.15 | 0 / 500,000 | 0 | Spread 25.77 > 25.0 bps |
| LTC | 51.45 | FAIL | BEAR/BEAR | +0.53 | +0.03 | 0 / 500,000 | 0 | Spread |
| AVAX | 41.80 | FAIL | BEAR/BEAR | -0.24 | -0.06 | 0 / 500,000 | 0 | Spread |
| NEAR | 71.37 | FAIL | BEAR/BEAR | -0.49 | +0.02 | 0 / 500,000 | 0 | Spread |
| SP500 | 0.39 | PASS | BEAR/BEAR | +0.70 | +0.76 | 0 / 1,000,000 | 0 | Ask walls 7,758 & 7,741 (6.30M / 6.29M) show presence 0.75; IMB is bid-heavy against shorts |
| NAS100 | 0.36 | PASS | BEAR/BEAR | -0.51 | +0.23 | 0 / 1,000,000 | 0 | Ask wall 29,942 (1.16M) presence 0.80, persist 233.5 s -> g7 false |
| DJ30 | 0.23 | PASS | MIX/BULL | +1.43 | n/a | 0 / 1,000,000 | 0 | Zero L3 walls, zero depth, zero stop feed |
| GER40 | 0.32 | PASS | MIX/BULL | +1.07 | n/a | 0 / 1,000,000 | 0 | Zero L3 walls, zero depth, zero stop feed |
| GOLD | 0.24 | PASS | MIXED | +1.89 | -0.13 | 205,700 / 1,000,000 | 0 | g7 bids 4,114.0 / 4,106.0 are 4.9-5.3x under floor |
| SILVER | 6.33 | FAIL | MIX/BEAR | +1.83 | +0.44 | 231,440 / 1,000,000 | 0 | Spread 6.33 > 5.0 bps; g7 sells 57.86 under floor |
| USWTI | 5.85 | FAIL | BULL/BULL | +2.15 | +0.44 | 0 / 1,000,000 | 0 | Spread 5.85 > 5.0 bps; blow-through, TRAPPED_SELLERS_BELOW |
| EURUSD | 0.09 | PASS | BULL/MIX | -0.09 | +0.09 | 254,348 / 500,000 | 0 | Best-quality wall in the book (3,724.4 s, presence 0.9180) but 2.0x under the FX floor |
| GBPUSD | 0.23 | PASS | BULL/BULL | +0.65 | +0.37 | 0 / 500,000 | 0 | No g7 wall |
| USDJPY | 0.32 | PASS | BEAR/MIX | -0.23 | -0.45 | 199,701 / 500,000 | 0 | g7 walls ~2.5x under the FX floor |

**Structural finding (the decisive gate):** the qualifying-wall population is empty in all 24 assets. The book bifurcates cleanly:
- Walls with verified persistence (`gate_g7_eligible True`, persist 3,527-7,278 s, presence 0.912-0.941) top out at **663,503 USD** — below every institutional notional threshold.
- Walls with institutional notional (BTC 35.8M / 25.0M, ETH 14.8M, SP500 6.30M, NAS100 1.16M) all print `presence_frac` 0.7500-0.8000 versus the 0.85 SOP floor and 0.90 generator constant, and therefore `gate_g7_eligible False`.

Under Patch 2 (Whale Wall Persistence Gate), Patch 4 (Significant Notional Threshold), SOP Step 6 and Verify Rule 5, none of the 2,600+ published walls can shield a new order. Step 6 requires an order to be shielded by a genuine, gate-verified whale order; that precondition is unsatisfiable this cycle regardless of entry geometry.

Additional cross-cutting blockers: 14 of 24 assets fail the spread gate outright (all crypto ex-BTC/ETH/SOL/BNB, plus SILVER and USWTI). 15 of 24 print a confirmed 1H+4H bearish EMA stack, but the bearish set is precisely the set whose overhead clusters are sub-threshold noise, so Model 2 shorts lack both shielding liquidity and institutional bunkers. DJ30 and GER40 ship zero microstructure of any kind.

**TASK 1 VERDICT: STAND ASIDE — no new orders. No asset satisfies 100 pct of the SOP criteria.** Not a macro halt: the blackout guard is permanently disabled by operator mandate, and the F&G index is 53 (Neutral) with the next event (BoE Bailey fireside chat, 2026-10-16 02:00 UTC) outside the immediate window.

---

## 5. New order recommendations

| Symbol | Action | Lots | Limit | SL | TP | Cash risk | R:R | Whale depth & persistence | Target magnet |
|---|---|---|---|---|---|---|---|---|---|
| — | STAND ASIDE | — | — | — | — | 0.00 USD | — | 0 of 24 assets hold a qualifying shielding wall | — |

Rationale: Patch 2 + Patch 4 + Rule 5 are unsatisfiable, and the two geometrically nearest cards (BTC and ETH shorts) resolve to 1.39R and 0.216R at the first material opposing barrier. Cash is the position.

---

## 6. Dialectic debate summary

- **Persona A (Aggressive Orderflow):** wants the BTC and ETH shorts to stay, arguing bearish HTF alignment, bearish multi-horizon CVD (BTC -34.15M / ETH -112.70M session) and the 25.0M BTC offer at 81,163. **Rebutted:** that wall is `gate_g7_eligible False` with `presence_frac 0.75` — it is unverified liquidity by the desk's own gate, and the last four 1-minute CVD deltas flipped positive (+1.90M / +0.85M / +1.98M / +0.22M) straight into the staged limit.
- **Persona B (Macro and Regime Risk):** confirms 1H and 4H both print price < EMA20 < EMA50 with negative slope on BTC, ETH, SP500 and NAS100, so the short *direction* is right, and that no macro blackout applies. It reframes the problem: the desk is short the correct trend with the wrong geometry — entries above the resistance shelf at 2.28 and 2.07 ATR and stops inside cluster bands. Verdict: the trend does not cure a stop placed inside a bunker.
- **Persona C (Forensic Position and Friction Auditor):** reproduces every number broker-style. BTC risk 280 x 0.04 = 11.20 USD, stressed 16.00; ETH 18 x 0.61 = 10.98, stressed 15.725; joint stress 31.725 -> post-loss equity 4,830.555, floor preserved with +35.555 USD. Friction is acceptable (2.36 and 17.44 bps). Disqualification is structural, not frictional: SL 81,560 sits inside a 1.37M band and SL 2,395 sits inside a 538k band inside a wider un-swept stack, and the repaired ETH stop needs 2,448.21 which needs 0.20 lots to stay inside 14.50 USD risk, at which point the 0.216R payoff is not payable.
- **Ratification:** unanimous CANCEL on both tickets, zero new orders, stand aside on all 24 assets.

---

## 7. Publication and caveats

Computation PASS means the arithmetic matches the pinned snapshot `c56410ac9d324a81bb3f7986f630d137`; it does not certify that every upstream data defect is repaired, and it does not authorize a trade. Known unresolved items: HTF arrays ship only 96 bars so a 1H/4H EMA200 hierarchy cannot be independently recomputed; `assets_matrix_24[symbol].arkham_onchain` is missing; Arkham reports zero exchange events this cycle, so Patch 1 corroboration is vacuous rather than confirming or refuting; p_win lower bound 0.4197 is uncalibrated at n=17 against a 100-sample minimum. No live order, ratchet, cancellation, production patch or backtest result is claimed by Arena.
