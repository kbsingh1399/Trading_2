> **SUPERSEDED FOR PROVENANCE (23:51 UTC):** the declared `workbook_sha256` fb6aebf6 matched no artifact, so this review's provenance section is withdrawn. See `CYCLE_312_ENVELOPE_DEFECT.md`; verdict is `DENIED_BAD_CYCLE_ENVELOPE`. The authorization it reached (`DENIED_FAIL_CLOSED`) was conservative and remains correct.

# Cycle 312 — Co-Equal Council Ruling (Arena.ai GPT Astra + Z.ai GLM-5.3-Flash)

**Cutoff** 2026-10-23 23:37:12 UTC · **Nonce** 9e2562d4-c54b-4b84-96d5-4e222ec3f88a · **Envelope** canonical sha256 `ce69e21653601b702c38ec46cd137048bde9fb100cf6bdbbd8e3f9c0d69db67b` · **Manifest** 5cf58f83… · **Ruling** `44dd879f3b12824d6b320bb2b3c61de1db8c1fd7894fa68d9e9e6c43f4b87fbd`

**Delta vs Cycle 311 (23:20:26 UTC):** +1,006 s. Inventory and solvency identical (4,865.07 flat; 4,863.07 post-reserve; 68.07 kernel headroom). Every evidence age advanced by 1,006 s and every clock is still null. Provenance moved from cf28fa8a/303be24f to 1f1c73e/5cf58f83 (still unverifiable locally). **Authorization unchanged: DENIED_FAIL_CLOSED.**

---

## 1. Provenance — valid envelope, self-declared artifacts, fail-closed

The attachment is a well-formed `schema_version 1.1.0` envelope: 10 required keys, UUIDv4 nonce, cutoff 3 m 23 s in the past at review time, no template markers (`{{`, `TODO`, `PLACEHOLDER`, `XXX`). `DENIED_BAD_CYCLE_ENVELOPE` therefore **does not apply** — the denial is produced by the gate values *inside* a valid envelope.

| Artifact | Declared | Independently obtained | Verdict |
|---|---|---|---|
| Risk policy | 4633e4af… | recomputed 4633e4af… (same sorted dict as `Terminal/generate_cycle_envelope.py`) | **MATCH** |
| Evidence manifest | 5cf58f83… | `Data/history/master_manifest.json` = 15fc034c… | MISMATCH |
| Workbook | fb6aebf6… | live `Data/DataBase_Trading.xlsx` = e855a87f… (mtime 23:16:52) | MISMATCH |
| Git commit / tree | 1f1c73e… / e07dec16… | absent in this clone (HEAD e6876ee / tree b948b0b) | UNVERIFIABLE |
| Excel freshness | `null` | audit 21:42:14 UTC: 29/33 fresh, 4 frozen | NOT VERIFIED |

Attestation level: the risk policy is **independently verified**; inventory is **dispatcher-declared and corroborated** by a 25-minute-old snapshot; manifest, workbook and commit are **declared-only**; Excel freshness is **null**. The mismatch pattern (declared artifacts older than the working copy) is consistent with post-envelope regeneration, not with proven tampering — but no council may upgrade a self-declared digest into proof.

**Freshness ledger (ages at cutoff).** Max-age policy: quote 15 s (10 s FX), L2 depth 180 s, CVD 900 s, session calendar 900 s, broker preflight 0 s (must be live). SOP's 900 s sheet ceiling is an outer limit, never a substitute.

| Evidence | Availability | Age at 23:37:12 | Limit | Result |
|---|---|---|---|---|
| BTC L1 quote | 23:12:12 UTC | 1,499 s | 15 s | FAIL |
| ETH L1 quote | 23:12:12 UTC | 1,499 s | 15 s | FAIL |
| EURUSD L1 quote | 20:59:59 UTC | 9,432 s | 10 s | FAIL |
| GER40 L1 quote | 20:00:00 UTC | 13,032 s | 15 s | FAIL |
| Binance L2 depth | 23:12:08 UTC | 1,504 s | 180 s | FAIL |
| Multi-horizon CVD | 23:12:18 UTC | 1,494 s | 900 s | PASS age, but uncalibrated |
| Workbook 12_Hyperdash row | 21:34:26 UTC | 7,366 s | 900 s | FAIL |
| Macro calendar | 17:35:00 UTC | 21,732 s | 900 s | FAIL |
| Excel audit itself | 21:42:14 UTC | 6,898 s | — | cannot attest cutoff |

Every dynamic row must satisfy `observation ≤ availability ≤ cutoff` and `0 ≤ cutoff − observation ≤ max_age`. Workbook mtime (23:16:52) is not row freshness.

## 2. Inventory — reconciled flat

`balance = equity = 4,865.07`, margin used 0.00, free 4,865.07, margin level 0.0 %, 0 positions, 0 pendings. The 23:12:13 UTC snapshot reproduces the same numbers to the cent. Ticket #19267445 (SELL 0.06 BTC 81,700→80,600) closed 22:54 UTC at +66.00 gross / +65.19 net after −0.81 swap; #19270994 canceled. No residual, no unexplained deal or commission. **RECONCILED_FLAT.**

## 3. Strict solvency — capital passes, conjunction fails

`min(4,865.07, 4,865.07) − 2.00 = 4,863.07 ≥ 4,795.00` → headroom **68.07**; 265.07 above the 4,600 floor, 215.07 above the 4,650 buffer.

| Scenario | Stress | Post-loss | Kernel cushion |
|---|---|---|---|
| Baseline (reserve only) | 2.00 | 4,863.07 | 68.07 |
| One BTC ticket (0.04 lot) | 26.00 | 4,837.07 | 42.07 |
| Two identical BTC tickets | 52.00 | 4,811.07 | 16.07 |
| Sovereign illustration 2 × (1.25×25+2) | 70.00 | 4,796.57 | **1.57** |

Floating P/L and expected TP are credited **zero**. Tier 2 House Money (balance > 4,850) permits 15–25 USD nominal risk per ticket and at most **2** concurrent tickets. The live snapshot's looser 4-slot policy (`capacity.max_concurrent=4`) is overridden by the stricter envelope. There is no broker-native atomic OCO, so correlated BTC tickets are joint-stressed rather than treated as independent slots. The 1.57 USD residual in the sovereign illustration is a property of that model only; two nominal 25.00 USD losses do not confer immunity to gap, slippage or model error.

## 4. Candidate mathematics — discovery results, zero executable rows

All 156 MT5 symbols were scanned against the current symbol map; 24 carry row-level evidence in the snapshot matrix. Four rows are reported, all **HOLD**.

**(a) BTCUSD.pi — the only coherent structure found.** Bid 80,450.00 / ask 80,465.00 (1.86 bps), ATR14(15m) = 176.675, book imbalance −0.62 (ask-heavy), weekly CVD −154.0 M, 15m bar delta −17.0 M, pullback classifier SHORT at velocity 7.80. Price (80,457.5) sits **below** the value area (VAL 81,311.82, POC 81,663.49, VAH 81,739.94) — a value rejection, not a mean-reversion short. Research geometry: **SELL LIMIT 81,320** (broken VAL + 8.18), **SL 81,800** (2.72 ATR above VAH), **TP 79,650** (ahead of the 61.3 M USD sell-stop cascade at 79,500–79,600), **0.04 lot**.

- Risk = 0.04 × 480.00 × contract 1.0 = **19.20 USD** (inside the 15–25 band)
- Reward = 0.04 × 1,670.00 = **66.80 USD**; **R:R 3.48**
- Exit spread = 15.00 pts × 0.04 = **0.60 USD**, charged once (limit entry and TP treated as maker)
- Stress = 1.25 × 19.20 + 2.00 = **26.00 USD**; post-joint-stop **4,837.07** (cushion 42.07)
- Notional 3,252.80 USD; required margin **unknown** because no `order_calc_margin` exists
- Commission and swap unknown; they are *not* priced, and no cost is counted twice

The stop is structurally valid and the arithmetic is exact, but the cash loss rests on a 25-minute-old `symbol_info` snapshot, not on `order_calc_profit`. That is a missing broker receipt, not a missing idea.

**(b) ETHUSD.pi — adversarial veto.** CVD shows BULLISH_ABSORPTION, the book is +0.79 bid-heavy, yet the pullback classifier says SHORT at velocity 8.95 and ETH (2,358.75) is below its value area (VAL 2,389.216). Three native signals contradict each other, so no invalidation level is defensible → no order, null geometry.

**(c) EURUSD.pi — venue closed.** Last tick 20:59:59 UTC (9,432 s). Spread 3.57 bps at the close is not executable; the FX rollover window (21:15–22:30) is clear, but the weekend embargo (Fri 21:55 – Sun 22:00 UTC) governs.

**(d) GER40.p — venue closed.** Last tick exactly 20:00:00 UTC (13,032 s). **Correction:** 2026-10-23 is still CEST (DST ends 2026-10-25), so the Eurex 22:00 CEST close is **20:00 UTC**, not the 21:00 UTC asserted in earlier cycles; the broker's final tick corroborates the corrected clock.

## 5. Market clock, universe and asset-native evidence

156 symbols: Forex_Raw 60, other crypto CFDs 53, crypto majors 5, indices 16, commodity raws 14, energy/metals 8. Binary gates are conjunctive: `legal × fresh × broker session × native venue × calendar × rollover × feasibility × structural stop × capacity × solvency`. Capital and capacity pass; **freshness, broker session, native venue, calendar and broker `order_check` fail or are unknown**, so `overall_hard_gates_pass = false` and the ranking set is empty.

- Crypto native venues are 24/7, but the `.pi` CFD mirror still needs broker session proof — native openness cannot authorize a closed FX or index contract.
- The macro calendar was verified at 17:35 UTC (21,732 s); no blackout is known in the 23:37 window, but unknown freshness fails closed.
- 98 TradFi symbols are in weekend closure; 53 alt-crypto CFDs have no per-symbol depth/CVD; the 14 crypto majors with evidence still fail freshness and broker gates.

## 6. Existing positions — none

Flat inventory means no ratchet, no trailing stop and no protected-position claim. Nothing is labelled risk-free; the R0 ledger is immutable and unchanged by this review.

## 7. Methodology, calibration and soft ranking

Four personas were run affirmatively and adversarially: regime/calibration (BTC value rejection vs ETH contradiction), fill/microstructure (book imbalance, stop clusters, maker vs taker), solvency/portfolio (26.00 and 52.00 stress, 2-slot cap), and clock/provenance (ages, digests, calendars).

`P_fill` and `P_TP` remain **null**. The snapshot publishes `p_win_lower_bound = 0.4197`, an exact one-sided Clopper–Pearson 95 % bound on **11 wins / 17 trades**, with `calibrated = false` and a stated minimum sample of 100. That is an account-wide diagnostic, not an asset- or setup-specific `P_TP`; using it would smuggle a small-sample point estimate into the formula. There is no Brier score, log-loss, reliability curve, effective sample size ≥ 100, fill model, or time-blocked out-of-sample window.

`EV_net = P_fill × [P_TP × Gain_net − (1 − P_TP) × Loss_net − AdverseSelection − BrokerFrictions] − (1 − P_fill) × WaitCost` and `Utility = LCB_5%(EV_net) / Expected_Capital_Minutes` are therefore **not computable** (null), not zero. The displayed two-outcome form is also insufficient for a resting limit: unfilled, partial-fill and 900 s time-stop outcomes are separate branches, and timeout mass is not folded into `P_TP`. `AdverseSelection` (queue/refill) and `BrokerFrictions` (commission/swap) are incremental-on-fill and unmeasured; `WaitCost` is on-no-fill and unmeasured. No LLM conviction, pillar count or invented percentage is substituted.

## 8. What would re-arm the desk

1. One envelope whose ticks, L2 depth and calendar are all inside their max ages **at the same cutoff** (quote ≤ 15 s, depth ≤ 180 s, calendar ≤ 900 s).
2. `order_calc_profit`, `order_calc_margin` and `order_check` receipts bound to that dispatch nonce for the exact proposed request, plus a broker session proof.
3. A verified venue calendar covering the 2026-10-25 DST switch and any holiday/early close.
4. A calibrated `P_fill`/`P_TP` model with ≥ 100 time-blocked out-of-sample labels, Brier/log-loss, ESS and a documented bootstrap for `LCB_5%`.
5. Recomputed manifest and workbook digests matching the envelope at commit `1f1c73e` (or a commit this clone can resolve).

Until then: **DENIED_FAIL_CLOSED**, four WATCHLIST rows, no order emission. The desk keeps the 68.07 USD kernel headroom intact and the next catalyst is Monday's Xetra/London open (~08:00 UTC) with a fresh calendar.
