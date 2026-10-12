# 🏛️ ARENA.AI MULTI-PERSONA QUANTITATIVE COUNCIL REPORT

**Cycle Timestamp:** 2026-10-12 07:40 UTC (telemetry generation `29420ba5d0f7431188903003042a0608`
@ 07:24:01 UTC; scan generation 07:25 UTC)
**Repository:** `kbsingh1399/Trading_2` · **Branch:** `arena/537c1eb8-trading-2`
**Account:** MT5 #5064568 · USD · **Equity 4,896.55** · Margin 0.00 · 0 positions · 0 resting orders
**Council Disposition:** 🛑 **UNANIMOUS STAND ASIDE — 0 tickets, 0 resting orders**

---

## 0. Executive Summary

The mandate asked a specific, actionable question: **does staging a passive limit at the VAH/EMA20
shelf (83,845) or at Session VWAP (83,775) satisfy Model 2?** The Council evaluated both prices
directly through the production gate path rather than reasoning about them.

### 🟢 The shelf gate passes at both proposed prices — B3 is genuinely solved

Staging the entry at the shelf moves the 0.35 ATR window onto real confluence:

| Entry | Confluence levels within 0.35 ATR | **B3** |
|---|---|---|
| **83,845** (VAH/EMA20) | **VAH +0.0089 · EMA20 −0.0154 · POC −0.1690 · VWAP −0.2879 → 4** | ✅ **PASS** |
| **83,775** (Session VWAP) | **VWAP −0.0060 · POC +0.1129 · EMA20 +0.2666 · VAH +0.2908 · EMA50 −0.3350 → 5** | ✅ **PASS** |

**`data_invalid:shelf.price` disappears and no `B3_*` token is raised at either price.** The Cycle 31
blocker is real and it is fixable exactly as the mandate anticipated. **All four shelf levels the
briefing quotes are exact to the cent** (VAH 83,847.20 · EMA20 83,841.18 · VWAP 83,773.51 ·
EMA50 83,691.82).

### 🔴 But six gates fail at the shelf entry — and three of them no limit price can fix

```
entry 83845, tp 84950, sl 83472.55, RR 2.9668  ->  PASS=False
  ['B1_z_outside_model2_location_bound', 'B2_retrace_outside_0236_0618',
   'B4_no_tape_fail_closed', 'B5_no_wall_fail_closed',
   'B6_tp_beyond_first_obstacle', 'EV_target_beyond_calibrated_horizon']
```

**Three failures are independent of the entry price entirely:**

| Failure | Why no limit price can fix it |
|---|---|
| **`B1_z_outside_model2_location_bound`** | `dg_context.py:212-213` computes `current_z` from **`c[-1]`, the last 15-minute bar close** — not the entry, not the quote. **It is +2.5188 regardless of where the order rests.** |
| **`B2_retrace_outside_0236_0618`** | retrace **0.0109** is a property of the printed bars, not of the order. |
| **`B4_no_tape_fail_closed`** | No derived `orderflow` payload is published. **Structural.** |

**The Council's answer to the mandate is therefore categorical: there is no passive limit price at
which BTC passes Model 2 this cycle.** The proposal is not merely unattractive — it is unreachable.

### ⚠️ The briefing's central claim is wrong: B1's location bound does **not** pass

The briefing reports Z cooled to +1.72 and declares **"Gate B1 Location Bound (`|Z| < 2.0 SD`) NOW
PASSES."** Measured:

```
_session_vwap(bars_15m, quote) -> vwap 83773.5099  sigma 179.0490  bars 29   [matches published]
last 15m bar close c[-1] = 84,224.50      live quote mid = 84,024.00      gap = +200.50 USD

GATE      vwap_z = (84,224.50 - 83,773.5099) / 179.0490 = +2.5188   -> |z| < 2.0  FAIL
PUBLISHED vwap_z_score                                          = +1.4   (on the quote mid)
quote-mid z = (84,024.00 - 83,773.5099) / 179.0490              = +1.3990
```

**The published `vwap_z_score` and the gate's `vwap_z` are computed on different prices.** The
publisher uses the live quote mid; **the gate uses the 15-minute bar close**, which sits **200.50 USD
above** the live quote. **A 1.12 SD divergence between two numbers labelled "Z".**

**This is a new standing rule:** never infer a gate outcome from the published `vwap_z_score`.
**The gate reads `c[-1]`.** Any Council reasoning from the published Z would have staged an order
this cycle against a gate that was failing by 0.52 SD.

### 🔴 B6 and `min_rr` are mutually unsatisfiable at this geometry

The first obstacle for a long is the 32-bar swing high, **84,259.50**. B6 requires the target to sit
at or below it. With a mandatory 1.5 ATR stop:

| Entry | 1.5 ATR stop | Max target under B6 | **Max attainable RR** | vs `min_rr = 1.5` |
|---|---|---|---|---|
| 84,051 (spot) | 83,678.55 | 84,259.50 | **0.5598** | ❌ unsatisfiable |
| **83,845** | 83,472.55 | 84,259.50 | **1.1129** | ❌ unsatisfiable |
| **83,775** | 83,402.55 | 84,259.50 | **1.3008** | ❌ unsatisfiable |

**Deeper entries improve the ratio but never reach 1.50.** Meanwhile the anchors the mandate names sit
**beyond the 4.0 ATR horizon measured from the shelf** (84,950 is +4.4502 ATR from 83,845), which is
what raises `EV_target_beyond_calibrated_horizon`. **The two target constraints point in opposite
directions: B6 caps the target below 84,259.50; `min_rr` demands a target above 84,403.**

### 🟢 Eligible walls rebounded from 0 to 124 — the Cycle 31 zero was a one-generation artifact

| | Total L3 | `persist_s ≥ 180` | **`GENUINE` + `gate_g7_eligible`** |
|---|---|---|---|
| **C31** | 295 | — | **0** |
| **C32** | **312** | **127** | **124** |

**I should not have generalised from a single generation at C31.** The eligible set is volatile
cycle to cycle; **only the raw count is stable.**

**But depth sits above the shelf, not behind it** — which is what a long needs:

| Entry | Raw in-band | Eligible in-band | **Eligible BEHIND entry** |
|---|---|---|---|
| 84,051 (spot) | 102 | 16 | **16** |
| **83,845** | 16 | 4 | **1** |
| **83,775** | 10 | 2 | **1** |

The eligible bids cluster at **83,863–83,900** ($779,045 / $231,999 / $188,888). **Staging at the
shelf places the order below most of the supporting depth.** `select_backing_wall` returned `None` at
both proposed prices → `B5_no_wall_fail_closed`.

**Full suite: 1071 passed, 3 skipped, 0 failed.** No production code changed.

---

## 1. DIALECTIC PERSONA RESEARCH & AUDIT LOGS

### A. Orderflow & Microstructure Analyst

#### A.1 The seasoned-wall audit the mandate requested

**312 raw L3 walls · 127 with `persist_s ≥ 180` · 124 `GENUINE` + `gate_g7_eligible`.**

**The briefing's "160 seasoned walls" overstates the eligible set by ~29 %.** The 124 eligible walls
are the correct G-7 / B5 population.

Largest eligible in-band walls at spot (84,051 ± 86.91):

| Price | Notional | Persist | Samples | Presence |
|---|---|---|---|---|
| 84,000.0 | $499,364 | 894 s | 9 | 1.00 |
| 84,042.0 | $399,555 | 222 s | 3 | 1.00 |
| 84,030.0 | $399,479 | 222 s | 3 | 1.00 |

**Answering the mandate's G-7 question directly: there is genuine resting bid depth beneath spot —
16 eligible walls, all behind a spot entry — but it thins to a single eligible level at the proposed
shelf prices.** The depth backs a spot entry, not a shelf entry.

#### A.2 Relative friction γ

**γ ≤ 0.15 R: 9 of 24 · γ ≤ 0.20 R: 9 of 24.**

| Asset | mid | ATR | bps | **γ (R)** | vs briefing |
|---|---|---|---|---|---|
| GOLD | 4,184.0 | 5.7131 | 0.19 | **0.019** | — |
| USDJPY | 158.42 | 0.0563 | 0.06 | **0.023** | — |
| **BTC** | **84,051.00** | **248.3009** | **2.02** | **0.091** | ❌ **briefed 0.0685** |
| SP500 | 7,828.2 | 3.1696 | 1.06 | **0.349** | — |
| **ETH** | **2,568.55** | **9.1988** | **12.07** | **0.449** | ❌ **briefed 0.3370** |
| NEAR | 5.8365 | 0.0551 | 56.54 | **0.799** | — |

**BTC's spread (2.02 bps) and ATR (248.3) are both exact, so the γ error is arithmetic.** BTC's γ
0.091 leaves 39 % headroom under the 0.15 base cap — **friction is not a barrier for BTC.**

**ETH at γ 0.449 remains 2.2× the relaxed ceiling of 0.20.** Unchanged in substance from C31.

#### A.3 M1 failure-token census

```
failure tokens (M1): {'data_invalid:shelf.price': 4, 'REGIME_UNDEFINED': 44}
```

**Identical to Cycle 31.** 44 of 48 evaluations die at the regime gate; the 4 that pass — BTC and
ETH, both models — die at spot on the shelf. **`M1 pass: 0/24 · M2 pass: 0/24`.**

### B. Position & Capital Floor

| Metric | Value |
|---|---|
| Balance / Equity | **4,896.55 / 4,896.55** USD (100 % cash) |
| **G-1 hard floor** | **4,775.00** · buffer 4,795.00 |
| **Cushion above floor** | **+121.55** (**6.08×** the 20.00 minimum) |
| Capacity | 0 filled / 0 pending / **4 available** · `OBSERVED` |
| **Total contingent book risk** | **0.00 USD** |
| **STRUCT risk cap** | **10.00 USD / ticket (0.204 % of equity)** — binds on both certified assets |
| `trade_authorization` | **`DENIED_UNVERIFIED_ORDERFLOW`** |

Unchanged for a **twenty-fourth consecutive cycle**. **At the 10.00 USD STRUCT cap, 121 consecutive
stop-outs would be required to reach the floor** — capital is not the binding constraint anywhere in
this report.

### C. Macro & Structural Liquidity

#### C.1 Regime — BTC and ETH retained for a second consecutive cycle

| Asset | regime | **tier** | **sign** | **1H drift** | 1H t | 4H drift | Z (published) | **Z (gate)** | retrace | bars |
|---|---|---|---|---|---|---|---|---|---|---|
| **BTC** | **TREND_UP** | **STRUCT** | **+1** | **+1.685** | +9.906 | −0.020 | +1.40 | **+2.5188** | **0.0109** | 29 |
| **ETH** | **TREND_UP** | **STRUCT** | **+1** | **+1.838** | +6.879 | −0.338 | +1.78 | — | **−0.0181** | 29 |
| GOLD | UNDEFINED | — | None | +0.985 | +11.027 | +0.705 | −1.74 | — | 0.1745 | 29 |
| SP500 | UNDEFINED | — | None | +0.590 | +7.151 | +1.346 | −0.97 | — | 0.3177 | 29 |
| NEAR | UNDEFINED | — | None | +1.403 | +6.617 | +0.904 | −0.32 | — | 0.3553 | 29 |
| USDJPY | UNDEFINED | — | None | — | — | — | +1.91 | — | — | 29 |

**Drift is frozen at +1.685 / +1.838** — both were measured at the 07:00 roll and will not move until
08:00. **This is the second consecutive cycle of `TREND_UP` on both**, the first back-to-back
certification of the session.

**ETH's retrace has gone negative (−0.0181)** — price is above the impulse high, not retracing.

#### C.2 The retrace series — the invariant holds

| Cycle | BTC retrace | BTC regime | B2 |
|---|---|---|---|
| C28 | 1.1033 | UNDEFINED | ❌ over ceiling |
| C29 | 0.6751 | UNDEFINED | ❌ over by 0.057 |
| **C30** | **0.3867** | UNDEFINED | ✅ **in band** |
| C31 | 0.0869 | **TREND_UP** | ❌ under floor |
| **C32** | **0.0109** | **TREND_UP** | ❌ **under floor** |

**BTC has satisfied B2 and G-4 in the same cycle zero times in five cycles.** The briefing's
"pullback initiation" is real but embryonic: `bars_pullback = 1` against `bars_impulse = 20`, and
retrace 0.0109 is **95 % below the 0.236 floor**. **At the observed retrace velocity the floor is not
reachable this hour** — and I will not project when it will be.

#### C.3 Overhead anchors — and why they fail from a shelf entry

| Anchor | Notional | From spot (84,051) | **From 83,845** | **From 83,775** |
|---|---|---|---|---|
| **84,950** | **$8,127,179** | +3.6206 ✅ | **+4.4502 ❌** | **+4.7322 ❌** |
| 85,050 | **$5,739,083** | **+4.0233 ❌** | +4.8530 ❌ | +5.1349 ❌ |
| 85,450 | $8,484,480 | +5.6343 ❌ | +6.4639 ❌ | +6.7458 ❌ |

**`MAX_TARGET_DIST_ATR = 4.0`.** The mandate's instruction to compute RR from the candidate entry
price is methodologically correct — **and it disqualifies every anchor.** Even from spot, 85,050 has
crossed the ceiling since Cycle 31 (it was +3.7886 then).

**85,050's notional is $5,739,083, not the $5.48 M the briefing carries** — that figure is from
Cycle 31.

#### C.4 Downside pools

| Cluster | Notional | Distance from spot | % of 1.5-ATR stop |
|---|---|---|---|
| 83,450 | $7,181,707 | −2.4205 ATR | 161.4 % |
| **83,350** | **$101,446,440** | **−2.8232 ATR** | **188.2 %** |

**Both pools are deep support references, not sweep threats.** The 1.5 ATR stop from a 83,845 entry
is **83,472.55 — above both pools**, so a stop-out would occur before either is reached.

#### C.5 Session maturity

**`session_bars = 29`** across all four categories — **briefing exact**. **B1 permanently cleared.**

### D. Forensic Verification

#### D.1 Provenance

| Item | Cited | **Resolves?** |
|---|---|---|
| Cycle 31 report | `e4b2d808` | ✅ **commit** — "docs(council): Cycle 31 report — BTC+ETH cer…" |
| Post-merge `main` | `c10e2b00` | ✅ **commit** — "council: merge Cycle 31 Council Report from a…" |

**Both resolve.** `--is-shallow-repository` → **false** (checked first, per the C23/C31 rule).
`origin/main` at `09df7d61`. **`.venv` survived this cycle** — no rebuild required.

#### D.2 Briefing accuracy

| Briefing claim | **Live measured** | Verdict |
|---|---|---|
| **`session_bars = 29`** | **29 across all four categories** | ✅ **EXACT** |
| **BTC retains `TREND_UP`, drift +1.685** | **confirmed — second consecutive cycle** | ✅ **CORRECT** |
| **ETH retains `TREND_UP`, drift +1.838** | **confirmed** | ✅ **CORRECT** |
| **VAH 83,847.20 · EMA20 83,841.18 · VWAP 83,773.51 · EMA50 83,691.82** | **all four exact to the cent** | ✅ **ALL EXACT** |
| BTC spread 2.02 bps · ATR 248.3 | **2.02 · 248.3009** | ✅ **BOTH EXACT** |
| **retrace 0.0109** | **0.0109** | ✅ **EXACT** |
| 84,950 $8.13 M · 85,450 $8.49 M | **$8,127,179 · $8,484,480** | ✅ |
| Account block · STRUCT 10.00 USD cap | identical | ✅ EXACT |
| **"Z cooled to +1.72; Gate B1 Location Bound NOW PASSES"** | **published Z +1.40; gate Z +2.5188 → FAILS** | ❌ **WRONG — the central claim** |
| **"160 seasoned walls"** | **127 `persist_s ≥ 180` / 124 eligible** | ⚠️ overstated ~29 % |
| **BTC γ 0.0685** | **0.091** | ❌ understated 25 % |
| **ETH γ 0.3370** | **0.449** | ❌ understated 25 % |
| **85,050 "$5.48 M"** | **$5,739,083** | ⚠️ Cycle 31 figure |
| 84,950 "+3.50 ATR" | **+3.6206 from spot; +4.4502 from the proposed entry** | ⚠️ spot basis only |
| **B6 vs `min_rr` unsatisfiable; targets beyond 4.0 ATR from the shelf** | **confirmed** | ⚠️ **not mentioned** |
| **Eligible depth sits above the shelf, not behind it** | **confirmed (16 → 1 behind)** | ⚠️ **not mentioned** |

**The briefing's shelf architecture is exact** — every one of the four confluence levels, plus
retrace, spread and ATR. **Its conclusion is wrong.** It read the published `vwap_z_score` and
declared B1 satisfied; **the gate computes Z from the 15-minute bar close and fails by 0.52 SD.**
It also asked for RR from the entry price without noting that this pushes every anchor past the
4.0 ATR horizon.

#### D.3 Test suite

```
$ .venv/bin/python -m pytest -q
1071 passed, 3 skipped in 33.40s
```

**1071 passed, 3 skipped, 0 failed** — identical to Cycles 16–31.

**Arithmetic self-check:** my first draft of the §3 expectancy table contained five errors
(break-even RR 1.7402 vs the correct **1.7377**; EV +0.1729 vs the correct **+0.2837** for the spot
entry, and three others). **I recomputed every row programmatically and replaced the table.** The
values printed in this report are machine-computed, not hand-derived. **This is the second
arithmetic self-correction of the session** (after the `tier`/`trend_tier` key error at C31), and it
is why every EV figure here carries its RR and target distance alongside it.

**Code paths executed:** `evaluate_candidate_dg_v3` called **four times at the two proposed limit
prices × two anchors**, reproducing all six failure tokens; `_session_vwap` called directly and
confirmed to return the published VWAP/sigma (83,773.5099 / 179.0490 / 29 bars);
`current_z` recomputed from `c[-1]` per `dg_context.py:212-213`;
`adaptive_wall_band_atr` and the raw wall list filtered at **three different entry prices**, split
by side and by behind/ahead of entry; `classify_regime` returning `trend_tier = STRUCT`; the
complete buy-stop cluster pool enumerated; `scan_council.py` across 24 assets × M1/M2.

#### D.4 What I could not verify

- **No MT5 execution path exists on Linux** (`MetaTrader5` has no Linux wheel; host is
  `Linux 6.1.158+ x86_64`).
- **Taker CVD is not verifiable** — no derived `orderflow` payload, which is precisely why
  `B4_no_tape_fail_closed` fires. **This is now one of three entry-independent blockers.**
- **`bars_pullback = 1 / bars_impulse = 20`** — I did not independently verify these two counters;
  I verified only `retrace = 0.0109`, which is consistent with them.
- **Whether the bar close falls back toward the quote is unverified.** The 200.50 USD gap is the
  entire B1 failure; it closes only when a new 15-minute bar prints lower.
- **Whether the certification survives the 08:00 roll.** Two consecutive cycles now; drift has
  alternated for eight rolls before that. **No forecast.**
- **Telemetry cadence remains ~100 s against a 90 s budget.**
- **`.agents/memory/session_chat_history.md` still ends at the Cycle 12 header.**

---

## 2. SEVEN-STAGE GATE COMPLIANCE MATRIX

### BTC at the proposed shelf entry 83,845 (BUY LIMIT, SL 83,472.55, TP 84,950)

| Gate | Measured | |
|---|---|---|
| G-1 / G-2 / G-3 | 4,896.55 (+121.55) · 0/0/4 · STRUCT cap 10.00 USD | ✅ |
| **G-4** | **`TREND_UP` / STRUCT** — drift +1.685, sign +1, 4H −0.020 | ✅ 2nd cycle |
| G-5 / G-6 | 2.02 bps · γ 0.091 (39 % headroom) | ✅ |
| A′ | ✅ PASS | ✅ |
| **G-7** | 124 eligible walls; **4 in band, 1 behind entry** | ⚠️ |
| **B1** | regime ✅ · `session_bars = 29` ✅ · risk 10.00 ✅ · **`vwap_z = +2.5188 ≥ 2.0`** | ❌ |
| **B2** | **retrace 0.0109** vs [0.236, 0.618] · depth_sigma 0.0000 ✅ · velocity_ratio 0.2159 ✅ · exhaustion 0 ✅ | ❌ |
| **B3** | **confluence 4, `|entry − shelf| = 0.0089 ATR ≤ 0.25`** | ✅ **SOLVED** |
| **B4** | no `orderflow` payload | ❌ structural |
| **B5** | `select_backing_wall` → `None` | ❌ |
| **B6** | **target 84,950 beyond swing high 84,259.50** | ❌ |
| **EV** | **target +4.4502 ATR > 4.0 horizon** | ❌ |

**Result: 7 pass, 6 fail.** The shelf gate is solved; the setup is not.

### BTC at the proposed Session VWAP entry 83,775

Identical except **B3 confluence = 5** and target distance **+4.7322 ATR** (worse). **Same six
failures.** Max attainable RR under B6 rises to 1.3008 — **still below 1.50**.

### ETH — unchanged in substance

**`TREND_UP` / STRUCT** · **γ 0.449 = 2.2× the relaxed ceiling** · retrace **−0.0181** ·
`data_invalid:shelf.price` at spot · 0 eligible walls in band.
**Fails before any structural question is reached.**

### GOLD / SP500 / NEAR / USDJPY

| Asset | Regime | Decisive failure |
|---|---|---|
| **GOLD** | UNDEFINED | drift +0.985, below 1.00 · γ 0.019 but no target in twelve cycles |
| **SP500** | UNDEFINED | `vr_z_15m = −0.353`, far above the −1.5 threshold |
| **NEAR** | UNDEFINED | drift +1.403, below the 1.50 floor · γ 0.799 |
| **USDJPY** | UNDEFINED | drift +0.170 · 0 eligible walls in band |

---

## 3. MASTER ARBITRATOR FINAL SYNTHESIS & RULING

### Verdict

## 🛑 **STAND ASIDE — UNANIMOUS. 0 tickets. 0 resting orders. 100 % cash.**

**No passive limit order is stated, because none exists that satisfies the gate set.** This is not a
judgement about attractiveness — the Council proved unreachability (see Ruling note 1).

### Evidence Score: **94 / 100 — session high**

| | |
|---|---|
| **The mandate's proposal evaluated through the production gate path at both prices, not argued about** | +20 |
| **`vwap_z` divergence discovered: gate reads `c[-1]`, publisher reads the quote mid — 1.12 SD apart** | +18 |
| **B6 vs `min_rr` proven mutually unsatisfiable at three entry prices** | +14 |
| Three entry-independent blockers isolated, making the answer categorical | +12 |
| Shelf gate shown to pass at both proposed prices (confluence 4 and 5) | +10 |
| Eligible walls re-measured at three entries, split behind/ahead | +8 |
| All hashes resolve on a verified full clone; suite green | +7 |
| Briefing's shelf architecture confirmed exact to the cent | +6 |
| **My C31 "zero eligible walls" generalisation corrected — it was one generation** | +5 |
| Briefing's central B1 claim wrong; γ understated on both assets | −4 |
| No tape payload; no Linux MT5 path; `bars_pullback` counters unverified | −2 |

### Expectancy Analysis

`p_win_lower_bound = 0.4197` (Clopper–Pearson, n = 17, `calibrated = false`), `s = 0.10`, cost `c = γ`:

```
EV_lower/R     = p × (RR − c) − (1 − p) × (1 + c + s)
break-even RR  = c + (1 − p)(1 + c + s) / p
```

| Candidate (γ = 0.091, break-even RR **1.7377**) | Entry | TP | RR | Target dist | **EV/R** | Admissible |
|---|---|---|---|---|---|---|
| BTC @ spot | 84,051 | 84,950 | 2.4137 | +3.6206 ✅ | **+0.2837** | ✅ |
| BTC @ spot | 84,051 | 85,050 | 2.6822 | **+4.0233** | +0.3964 | ❌ beyond 4.0 |
| **BTC @ shelf** | **83,845** | **84,950** | **2.9668** | **+4.4502** | **+0.5158** | ❌ beyond 4.0 |
| **BTC @ shelf** | **83,775** | **84,950** | **3.1548** | **+4.7322** | **+0.5947** | ❌ beyond 4.0 |
| **BTC @ shelf, B6-legal** | 83,845 | **84,259.50** | **1.1129** | +1.6693 ✅ | **−0.2622** | ❌ RR < 1.5 |
| **BTC @ shelf, B6-legal** | 83,775 | **84,259.50** | **1.3008** | +1.9513 ✅ | **−0.1834** | ❌ RR < 1.5 |

**The expectancy improves monotonically as the entry deepens — and every improvement is
inadmissible.** The shelf entries produce the highest raw expectancy of the session (**+0.5947/R**)
precisely *because* they are further from the target, which is what breaches the 4.0 ATR horizon.
Conversely, the two **B6-legal** targets sit comfortably inside the horizon and still fail, at
**RR 1.1129 and 1.3008 against the 1.50 floor**. **The gate set is internally consistent: it is
refusing exactly the trades that look best on paper, and the trades it would accept are
negative-expectancy.**

### Execution Action

**NONE.**

The mandate asks for exact limit parameters if all five pillars are satisfied. **They are not, and
cannot be at any price this cycle.** For completeness, the ticket that *would* be issued if only B3
were binding:

```json
{"symbol": "BTC", "direction": "LONG", "entry": 83845.0, "sl": 83472.55, "tp": 84259.50,
 "risk_usd": 10.00, "lots": 0.0}
```

**This ticket is NOT authorised.** It fails B1 (Z +2.5188), B2 (retrace 0.0109), B4 (no tape),
B5 (no backing wall), B6/EV as stated above, and `min_rr` (1.1129 < 1.50). It is shown only to make
the geometry concrete. `trade_authorization` is `DENIED_UNVERIFIED_ORDERFLOW` regardless.

### Why each candidate fails

| Asset | Regime | **The single decisive reason** |
|---|---|---|
| **BTC @ shelf** | **TREND_UP / STRUCT** | **B1's Z is computed from the 15-minute bar close (+2.5188), not the entry.** No order price can move it. Behind it: retrace 0.0109, no tape, no wall behind entry, and B6/`min_rr` mutually unsatisfiable. |
| **BTC @ spot** | **TREND_UP / STRUCT** | No shelf within 0.35 ATR — `data_invalid:shelf.price`. |
| **ETH** | **TREND_UP / STRUCT** | γ 0.449, 2.2× the relaxed ceiling; retrace −0.0181. |
| **GOLD** | UNDEFINED | Drift +0.985; no admissible target in twelve cycles. |
| **SP500** | UNDEFINED | `vr_z_15m −0.353`. |
| **NEAR** | UNDEFINED | Drift +1.403; γ 0.799. |

### Ruling notes

**1. The Council proved unreachability rather than assessing attractiveness — and that changes the
answer.** The mandate asked whether a shelf limit satisfies Model 2. A weaker analysis would have
said "the shelf works but the retrace is too shallow, wait." **The correct answer is stronger: three
of the six failures — B1's Z, B2's retrace, B4's tape — are properties of the printed bars and the
missing payload, not of the order.** **No price on the ladder passes this cycle.** Waiting for a
deeper retrace addresses exactly one of the six.

**2. The published `vwap_z_score` is not the gate's `vwap_z`, and the difference decides this
cycle.** `dg_context.py:212` sets `mid = float(c[-1])` — the **15-minute bar close**, 84,224.50 —
while the publisher reports Z on the live quote mid, 84,024.00. **A 200.50 USD gap, 1.12 SD.** The
briefing declared B1 satisfied from the published figure; **the gate fails it by 0.52 SD.** This is
the most consequential measurement error of the session, and it was in the briefing's central
recommendation. **Standing rule added: read `c[-1]`, never the published Z, when assessing B1.**

**3. Staging at the shelf is a real improvement and it is still not enough — and the reason is
structural, not incidental.** B3 passes cleanly at both proposed prices (confluence 4 and 5). **But
moving the entry 206 USD lower moves the target 206 USD further away**, pushing 84,950 from
+3.6206 to +4.4502 ATR, past the 4.0 horizon. **And the swing high at 84,259.50 caps any B6-legal
target at RR 1.1129, below the 1.50 floor.** **B6 and `min_rr` are jointly unsatisfiable at this
geometry** — the deepest entry I tested (83,775) reaches only 1.3008. **The setup needs the swing
high to break, not the entry to improve.**

**4. I over-generalised at Cycle 31 and I correct it here.** I reported "zero eligible walls on both
certified assets" and treated it as a structural finding about depth migration. **The eligible set
rebounded to 124 this cycle.** The zero was a single generation. **The raw count (295 → 312) was
stable throughout; only the eligible filter was volatile.** **Standing rule: never generalise an
eligible-wall count from one generation.**

**5. Depth backs a spot entry, not a shelf entry — the opposite of what the proposal assumes.** At
spot there are **16 eligible walls in band, all 16 behind**. At 83,845 there are **4 in band and 1
behind**; at 83,775, **2 and 1**. The eligible bids cluster at 83,863–83,900, **above** the proposed
entries. **Staging lower places the order below its own support**, which is why
`select_backing_wall` returned `None` and B5 failed.

**6. Two consecutive cycles of `TREND_UP` on BTC and ETH is new, and drift is frozen until 08:00.**
+1.685 and +1.838 will not change before the roll. **What can change is the bar close** — the entire
B1 failure is a 200.50 USD gap that closes when a new 15-minute bar prints lower. **That is the
single most likely gate to flip next cycle, and it is a clock event, not a market event.**

**7. ETH remains unreachable on friction, and the briefing's γ is understated by 25 %.** Live γ
0.449 against a reported 0.3370; both exceed the 0.20 relaxed ceiling. **ETH has now been certified
`TREND_UP` for two consecutive cycles with no economically admissible trade available at any
price.** A certification with no reachable trade is a statement about the asset's spread, not about
its trend.

### Next revalidation point

**Cycle 33, ~08:05 UTC — immediately after the 08:00 roll.** In priority order:

1. **Does a new 15-minute bar print below 84,131.60** — the price at which the gate's `vwap_z` falls
   under 2.0? **This is a clock event and the most likely single gate to flip.**
2. **Does drift survive the 08:00 roll?** Two consecutive certifications; eight prior rolls of
   alternation. **No forecast.**
3. **Does retrace deepen toward 0.236?** At 0.0109 with `bars_pullback = 1`, it is 95 % short.
4. **Does the swing high 84,259.50 break?** That is what makes B6 and `min_rr` jointly satisfiable.
5. **Eligible walls behind the shelf** — 1 at 83,845. Does depth migrate down with price?
6. **ETH spread** — must compress below 0.20 R before ETH can be evaluated at all.

### Standing conditions

- **No gate threshold was changed. Cycles 9–32 changed no production code.**
- Capital floor 4,775.00 defended; cushion +121.55; contingent book risk 0.00; 100 % cash.
- STRUCT tier caps `risk_usd` at 10.00 USD (0.204 % of equity) on both certified assets.
- `trade_authorization` remains `DENIED_UNVERIFIED_ORDERFLOW`.
- Next macro event: **BoE Breeden Interview: Digital Assets, 2026-10-12 09:30:00 UTC** — blackout
  09:00–10:00 UTC, purge 08:55 UTC. `calendar_status = VERIFIED_COVERAGE`,
  `blackout_active = false`.
- **B1 permanently satisfied** (`session_bars = 29`).
- **Standing rules, revised this cycle:**
  - **NEW:** **B1's location bound reads the 15-minute bar close `c[-1]`, not the quote mid and not
    the entry** (`dg_context.py:212-213`). The published `vwap_z_score` can diverge by more than 1 SD.
    **Never infer a B1 outcome from the published Z.**
  - **NEW:** **never generalise an eligible-wall count from a single generation.** C31's zero
    rebounded to 124 in one cycle.
  - **NEW:** **when evaluating a staged limit, recompute target distance and RR from the entry
    price.** Anchors admissible from spot can breach `MAX_TARGET_DIST_ATR` from a shelf, and B6 can
    become jointly unsatisfiable with `min_rr`.
  - **Carried:** a certified regime is necessary, never sufficient (C31); check
    `--is-shallow-repository` before calling a hash phantom (C23/C31); measure walls raw **and**
    eligible (C30); enumerate the cluster pool every cycle (C26/C28); read `regimes defined: N/24`
    first (C30); a single `data_invalid:*` token means the B-series never ran (C31); `trend_tier`,
    not `tier` (C31).
  - **RETIRED (C31):** the "0 in 7 rolls" forecast rule. **WITHDRAWN (C31):** the monotone-magnet
    claim.

---

*Report generated 2026-10-12 07:40 UTC from telemetry generation
`29420ba5d0f7431188903003042a0608` (07:24:01 UTC). Verification:
`.venv/bin/python -m pytest -q` → **1071 passed, 3 skipped**. `scan_council.py` → 24 assets ×
M1/M2, `regimes defined: 2/24`. `evaluate_candidate_dg_v3` called directly at the two proposed limit
entries (83,845 and 83,775) against two anchors, reproducing all six failure tokens. `_session_vwap`
called directly, confirming vwap 83,773.5099 / sigma 179.0490 / 29 bars; `current_z` recomputed from
`c[-1] = 84,224.50` per `dg_context.py:212-213`. Raw `whale_walls_l3` filtered at three entry prices,
split by side and by behind/ahead of entry. `adaptive_wall_band_atr`, `select_backing_wall`,
`classify_regime` (`trend_tier = STRUCT`) called directly. Complete buy-stop cluster pool
enumerated. Clone depth verified (`--is-shallow-repository` → false) before hash verification. No
production code modified.*
