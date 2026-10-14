# ARENA COUNCIL REPORT — CYCLE 109
### Pure Telemetry & Playbook Analysis · Dual-Engine Screening · Zero Decision Gates
**Orchestrator:** Claude Fable (Arena.ai, Tab 2) · **Broker:** Blueberry Markets SVG LLC, MT5 #5064568
**Machine trace:** `docs/trade_plans/arena_runs/cycle109_20261014T223246Z/{run.json,REPORT.md}` · **Cards:** `docs/trade_plans/arena_cards/cycle109_20261014T223246Z.json`
**Arena skill:** applied via `.agent/skills/arena/{SKILL.md,rubric.md}` — five personas, written rubric, fatal rule, single-elimination bracket, executed deterministically by `Terminal/arena_tournament.py` (seed 106).

---

## 0 · INGESTION CITATION

| Fact | Value |
|---|---|
| **Generation used** | **`f9286408c3e24884ac0bd85af53c4fb5` @ 2026-10-14 22:32:46 UTC** |
| Generation cited in prompt | `c74503df3d29434c9ca2ac5f3d61c647` @ 22:30:40 UTC — **superseded by 2 min 06 s** (one generation newer was already on `main`) |
| Authorization | `DENIED_UNVERIFIED_ORDERFLOW` (unchanged all session) |
| Protocol / policy | `omni.telemetry.v3.observed_only`; `OBSERVED_OR_DERIVED_FROM_OBSERVED` — unavailable fields never authorise trades |
| Macro | Fed Bowman (Bangkok Economic Festival) 2026-10-15 02:55 UTC, `blackout_active = false`; **blackout enforcement permanently disabled by operator** — no candidate was delayed, disqualified or purged |
| Account | balance = equity **4,859.55 USD**, margin used 0.00, positions **0**, pending **0**, joint-fill slots **0/4 used** |
| Playbook compliance | dual engines kept separate (§7.3); trend-first hierarchy (§2); §7.4 asset-class wall calibration + 15% dynamic friction; §3.B stop placement from cluster `min_price`/`max_price`; ≤2.0:1 overwhelm cap; §7.1 ratchet reserved for Mandate 2 |

### 0.1 What changed since Cycle 106 (this is the headline)

| Metric | Cycle 106 (20:56:21) | **Cycle 109 (22:32:46)** |
|---|---|---|
| Assets with live causal indicators | 3 / 24 | **24 / 24** |
| L3 walls ≥ 500k USD | 248 total, **0** with verified persistence | 248 total, **85 with `persist_s` ≥ 180 s** |
| Engine 2 verifiable at all? | No (ATR unavailable for 21 assets) | **Yes — every asset** |
| Account state | flat + 1 pending (ETH) | **flat, 0 pending** |

The observation-history rollover that produced Cycle 106's "zero persistence" reading has fully resolved: Gate R-2 (calibrated whale-wall bunker shield) is now *satisfiable*, and for the first time this session every one of the 24 instruments can be judged on both engines.

### 0.2 Engine corrections shipped this cycle (disclosure)

Three defects were found and fixed in `Terminal/arena_tournament.py` (36 tests, all passing):

1. **LONG-side hazard orientation (crash + latent error).** The long branch never defined the squeeze term (crash) and treated the *buy* stops above as the hazard — the mirror of the correct doctrine. A LONG's sweep hazard is the **sell**-stop cluster below; its reward magnets are the buy stops above. Fixed and covered by five new tests.
2. **Gate R-2 corridor rule.** A wall only shelters a stop if it stands **between the entry and the stop**. Previously any same-side wall at or inside the stop level counted, which inflated "in-range defense" with walls sitting *beyond* the stop (they cannot absorb anything before it is touched). Tightening this made several Cycle-106 defense figures read larger than they should have; no Cycle-106 ruling changes, but the numbers are corrected here.
3. **Corridor fuel.** "Forced fuel" is now the hazard notional standing between entry and stop, not only the belt that contains the stop (which is fatal on its own).

---

## 1 · MANDATE 1 — DUAL-ENGINE SCREENING OF ALL 24 ASSETS

Engine columns use the operator's own definitions. Engine 1 requires **all four** legs: |Z| ≥ 2.0 + tape exhaustion + ≥500k USD whale backing with ≥180 s persistence + HTF alignment. Engine 2 requires a confirmed regime, a shelf in the direction of the trend, structural geometry that clears the 0.35–0.50 ATR bunker rule, and a reachable magnet that pays ≥ 2.0R. Longs are banned in `BEARISH`, shorts in `BULLISH`. Entry column = maximal permitted Model 2 entry (mid ± 2.0 ATR); "Ceiling" = maximum achievable R:R against the **minimum compliant stop**.

| # | Asset | Mid | Spr bps | Z | RSI | ATR | Regime | Engine 1 | Engine 2 | Belt above entry | Best reachable magnet | Ceiling | Walls ≥180s | **Final** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | BTCUSD.pi | 81554.50 | 2.08 | −1.29 | 37.6 | 244.79 | BEARISH | \|Z\|<2.0 | shelf = EMA50 82075 / VWAP; belt 41.04M overhead | 81600–82600 = **41.04M** | 80700–80800 = 15.51M → 80860.60 | **1.969** | 40 | **WATCHLIST** |
| 2 | ETHUSD.pi | 2416.95 | 12.83 | −1.28 | 35.6 | 11.11 | BEARISH | \|Z\|<2.0 | EMA20 2422 shelf, 8 verified walls | 2420–2530 = 17.97M | 2400–2410 = 42.27M → 2411.81 | 0.597 | 8 | NO SETUP |
| 3 | SOLUSD.p | 104.53 | 23.92 | −0.65 | 47.7 | 0.526 | BEARISH | \|Z\|<2.0 | EMA20 104.20 shelf, 4 walls | 105–115 = 15.36M | 100–101 = 47.22M → 101.08 | 0.258 | 4 | NO SETUP |
| 4 | BNBUSD.p | 728.55 | 6.87 | −1.41 | 41.4 | 1.835 | BEARISH | \|Z\|<2.0 | EMA20 728.69, 1 wall | 729–739 = 0.01M | — | — | 1 | NO SETUP |
| 5 | XRPUSD.pi | 1.335 | 22.45 | −0.62 | 52.9 | 0.0064 | BEARISH | \|Z\|<2.0 | no verified wall | 1.34–1.44 = 9.50M | 1.30–1.31 = 17.96M | unreachable (<0.35 ATR stop) | 0 | NO SETUP |
| 6 | ADAUSD.p | 0.229 | 96.0 | −0.47 | 49.0 | 0.0013 | BEARISH | \|Z\|<2.0 | no wall; 92–96 bps spread | 0.229–0.240 | — | — | 0 | NO SETUP |
| 7 | DOGUSD.p | 0.082 | 256.6 | −0.33 | 45.5 | 0.0004 | BEARISH | \|Z\|<2.0 | banned (friction 256 bps) | 0.082–0.083 | 0.0788 | — | 0 | NO SETUP |
| 8 | TRXUSD.p | 0.332 | 27.08 | +0.17 | 30.7 | 0.0004 | BULLISH | \|Z\|<2.0 | long permitted but SL inside [0.320,0.332] | 0.322–0.332 = 0.43M | — | — | 0 | NO SETUP |
| 9 | DOTUSD.pi | 1.139 | 184.3 | +0.47 | 54.4 | 0.0069 | BEARISH | \|Z\|<2.0 | banned (184 bps) | 1.14–1.24 | — | — | 0 | NO SETUP |
| 10 | LNKUSD.p | 12.403 | 70.1 | −1.05 | 41.9 | 0.0615 | BEARISH | \|Z\|<2.0 | no wall; 70 bps | 12.4–13.5 | 10.9–11.0 | — | 0 | NO SETUP |
| 11 | BCHUSD.p | 268.00 | 17.9 | −1.39 | 39.9 | 1.384 | BEARISH | \|Z\|<2.0 | no wall | 268–278 | — | — | 0 | NO SETUP |
| 12 | LTCUSD.pi | 59.52 | 50.4 | −0.70 | 44.6 | 0.272 | BEARISH | \|Z\|<2.0 | no wall; 50 bps | 59.5–60.9 | 58.8–58.9 | 1.204 | 0 | NO SETUP |
| 13 | AVXUSD.p | 10.01 | 40.0 | −0.26 | 60.1 | 0.0517 | BEARISH | \|Z\|<2.0 | no structure | — | — | — | 0 | NO SETUP |
| 14 | NERUSD.p | 4.872 | 67.7 | −0.91 | 50.9 | 0.0448 | BEARISH | \|Z\|<2.0 | banned (friction 43% at size) | 4.87–5.02 = 1.37M | 4.75–4.76 | 3.241 (unreachable/size-gated) | 0 | NO SETUP |
| 15 | SP500.p | 7703.32 | 0.44 | −1.44 | 33.1 | 9.948 | BEARISH | \|Z\|<2.0 | EMA20 7719 shelf, 20 walls | 7700–7810 = **18,418M*** | 7650–7660 = 8.93M → 7665.74 | 0.505 | 20 | NO SETUP |
| 16 | NAS100.p | 29802.07 | 0.41 | −1.85 | 25.1 | 63.36 | BEARISH | \|Z\|<2.0 (nearest miss) | EMA20 29967, 6 walls | 29800–30900 = 6.32M | 29700–29800 = 0.58M | 0.309 | 6 | NO SETUP |
| 17 | DJ30.p | 51613.35 | 0.31 | +0.05 | 55.0 | 60.61 | BEARISH | \|Z\|<2.0 | no clusters at all | — | — | — | 0 | NO SETUP |
| 18 | GER40.p | 25204.90 | 1.23 | **−2.14** | 33.8 | 26.93 | BEARISH | **Z PASS — 3 legs fail** | no clusters, no walls | — | — | — | 0 | NO SETUP |
| 19 | XAUUSD.pi | 4109.08 | 0.27 | −0.25 | 58.5 | 7.031 | BEARISH | \|Z\|<2.0 | 4 walls, EMA20 4099 | 4110–4210 = 1.81M | 4070–4080 = 1.05M | unreachable at compliant stop | 4 | NO SETUP |
| 20 | XAGUSD.pi | 55.705 | 6.46 | −1.25 | 45.0 | 0.308 | BEARISH | \|Z\|<2.0 | no wall ≥500k | 55.7–57.1 | 55.3–55.4 | 1.783 | 0 | NO SETUP |
| 21 | USWTI.p | 95.045 | 4.84 | −0.54 | 39.9 | 0.270 | BULLISH | \|Z\|<2.0 | longs permitted; no wall, no magnet | — | — | — | 0 | NO SETUP |
| 22 | EURUSD.pi | 1.117 | 0.18 | +0.32 | 65.4 | 0.0006 | BEARISH | \|Z\|<2.0 | 1 wall only | — | 1.11–1.12 = 2.44M | — | 1 | NO SETUP |
| 23 | GBPUSD.pi | 1.320 | 0.08 | −0.25 | 59.3 | 0.0007 | BEARISH | \|Z\|<2.0 | no wall | 1.32–1.37 = 1.35M | — | — | 0 | NO SETUP |
| 24 | USDJPY.pi | 158.19 | 0.13 | −1.27 | 33.9 | 0.087 | BEARISH | \|Z\|<2.0 | 1 wall | 158–167 = 1.33M | 156–157 = 0.53M | — | 1 | NO SETUP |

\* **Data-quality flag:** SP500's stop-cluster notionals (7,054M / 11,367M / 18,418M USD inside a 110-point belt) are larger than the entire listed derivatives book for the index and are internally inconsistent with the same asset's liquidation bands (0.13M). They appear to be un-normalised by contract size. The engine therefore treats index-cluster notionals as *relative* structure only; the 15%-friction and magnet-materiality tests still apply as written. See §7.1.

**Tally: 0 CANDIDATE · 1 WATCHLIST (BTC) · 23 NO SETUP.**

### 1.1 Engine 1 — one trigger on the board, and it dies on three legs

**GER40.p, Z = −2.14** is the only asset whose statistical dislocation reaches the Engine 1 threshold. It is disqualified three independent ways:
1. **Trend-first hierarchy:** the regime is BEARISH, so mean reversion (a LONG here — price is *below* VWAP) is **banned**. (v. engine: `FATAL COUNTER_TREND`.)
2. **Whale backing:** GER40 has **zero** L3 walls — the ≥500k/≥180 s confluence leg cannot be met.
3. **No magnet:** GER40 carries no stop clusters and no liquidation bands, so `NO_MAGNETS` fires — there is no object to front-run.

Note the asymmetry worth stating plainly: **Z alone has never been the gate.** 23 assets fail |Z| ≥ 2.0; the one that passes fails everything else.

### 1.2 Engine 2 — the geometry is the binding constraint, not the regime

Every instrumented asset is now evaluable. The regime legs pass almost everywhere (22 of 24 are trending), the shelf legs pass on the majors (EMA stacks are clean and aligned), and verified walls now exist — but **no asset produces payable geometry**, because the governing sweep belt sits directly above the only entry the 2.0 ATR proximity rule permits, and the stop that clears that belt is 2.5–3.5 ATR wide while the reachable magnets pay less than 2.0R against it.

**BTC is the closest and deserves the detail (it is the session's best card):**

| Field | Value | Verdict |
|---|---|---|
| Entry (max permitted) | 82,044.08 = mid + **2.0000008 ATR** | **fails by 8×10⁻⁷ ATR** (`ENTRY_TOO_FAR`) |
| Stop that clears the belt | belt max 82,600 + 0.35 ATR = **82,685.68** (641.6 pts = **2.62 ATR** wide) | clears, at the exact floor |
| Take profit | 80,720.0 | **inside** the 80,700–80,800 pool (15.51M) → `TP_INSIDE_MAGNET` |
| Compliant alternative TP | 80,860.60 (above the whole 80,600–80,800 ladder) | pays **1.84R** |
| Engine ceiling (best reachable ÷ min compliant stop) | **1.969R** | **< 2.0R required** → `UNPAYABLE_GEOMETRY`, `NO_PAYABLE_SETUP` |
| Corridor fuel vs in-corridor verified defense | 24.36M vs 43.42M = 0.56:1 | passes the ≤2.0:1 overwhelm cap |
| R-2 shield in the entry→stop corridor | SELL **82,341 = 14.957M, persist 4,512 s** | passes the ≥5.0M crypto-major requirement |
| Entry position | inside 41.04M USD of un-swept squeeze fuel | `ENTRY_IN_FUEL` (major) |

The decisive fact is structural: **BTC's sell-stop ladder below is contiguous from ~81,600 down to ~80,500**, so front-running any pool places the take-profit inside its neighbour. The deepest *coherent* front-run inside the 3.5 ATR reachability horizon pays 1.84–1.97R against a stop the belt forces to 2.62 ATR. **The 2.0R floor cannot be reached on BTC today**, and no other instrument gets within 1.2R of it.

*Honest robustness note:* the engine's ceiling of 1.969R is measured against the *minimum* compliant stop at the *maximum* permitted entry — i.e. the best corner of the parameter space. Widening the stop to a comfortable 0.50 ATR clearance drops the best reachable reward to **1.863R**. The pass/fail boundary is knife-edge by construction; the ruling is not.

---

## 2 · MANDATE 2 — ACTIVE / RUNNING TRADES

`active_positions = []` → **FLAT**. No TP/SL ratchet applies (§7.1 ladder reserved; nothing to ratchet). Margin used 0.00 USD; balance = equity 4,859.55 USD; cushion **+64.55 USD** above the 4,795.00 operating buffer and **+84.55 USD** above the 4,775.00 hard floor.

---

## 3 · MANDATE 3 — UNFILLED LIMIT ORDER AUDIT

**Snapshot reading: 0 pending orders.** No ticket is live, so there is nothing to WAIT on, MODIFY or DELETE. However, Part CP describes **ticket #18925879 (SOLUSD.p SELL LIMIT 0.10 @ 104.90 / SL 105.75 / TP 103.10)** as live, so it is audited here as a post-mortem — the ruling must be falsifiable.

**Lifecycle, established from generation-by-generation snapshots on `main`:**

| Generation (UTC) | Pending order present? | Balance |
|---|---|---|
| 21:40 → 22:20 (8 sampled generations) | ✅ #18925879 | 4,859.55 |
| **22:29:55** (`56bcff13`) | ✅ #18925879 — last observable state | 4,859.55 |
| **22:30:40** (`c74503df` — the generation this prompt cites) | ❌ none | 4,859.55 |
| 22:32:46 (`f9286408` — used here) | ❌ none | 4,859.55 |

Balance never moved and no position ever appeared ⇒ **the ticket was cancelled, not filled.** The desk deleted it ~45 seconds before the cited generation.

**Audit of the deleted ticket on its last observable generation (22:29:55):**

| # | Finding | Arithmetic |
|---|---|---|
| 1 | **FATAL** `SL_INSIDE_SWEEP` | SL 105.75 sits inside the purchase-side belt **[104.0, 114.0] = 15.367M USD** — Archetype 1, the desk's most common killer |
| 2 | **FATAL** `FRICTION_BUDGET` | spread 0.22 ÷ stop 0.85 = **25.88%** of risk (cap 15%) |
| 3 | **FATAL** `NO_PAYABLE_SETUP` | asset ceiling **0.194R**; best reachable target 104.08 pays 0.16R against the 9.3-point minimum compliant stop |
| 4 | **FATAL** `TP_INSIDE_MAGNET` | TP 103.10 sits **inside** the 103.0–104.0 pool (3.27M) instead of front-running it |
| 5 | **FATAL** `OVERWHELM_RATIO` | forced fuel 15.367M vs in-corridor verified defense 5.652M = **2.72:1** (cap 2.0:1) |
| 6 | MAJOR `ENTRY_IN_FUEL` | entry 104.90 inside 15.37M of un-swept fuel |
| 7 | MAJOR `BUNKER_WALL_THIN` | largest in-corridor wall 2.484M < 5.0M crypto requirement |
| 8 | MAJOR `COUNTER_CVD` | short against **+7.62M USD** positive session CVD |
| 9 | MAJOR `SPREAD_OVER_ATR` | spread/ATR 0.416 exceeds 0.18 |

**RULING: `DELETE` — CONFIRMED CORRECT.** Four fatal gate failures, including the exact Archetype-1 signature (SL inside a sweep belt) and the exact Archetype-4 signature (in-corridor shield 2.48M < 5.0M requirement). Notably its "2.12R" quoted reward was an artefact of a stop that could never survive the belt: with a compliant 9.6-point stop the ceiling is **0.19R**. The desk's cancellation is ratified. A KAIZEN note for the desk: the three deleted tickets this session (ETH #18925596, BTC #18925868, SOL #18925879) were **all** destroyed by the same single defect — a stop placed inside a sweep belt — which is now mechanically impossible to miss with the engine's corridor rule.

**Part CP BTC question (SELL LIMIT @ 82,190 / SL 82,420 / TP 81,660):** re-tested on the current generation; the ruling is unchanged and now has a second, independent proof. The card fails `SL_INSIDE_SWEEP` (SL 82,420 inside the belt) *and* `NO_PAYABLE_SETUP` — and the reason the whole BTC complex is unpayable today is §1.2: the sell-stop ladder below is contiguous, so no compliant TP reaches 2.0R. `DO NOT STAGE`.

---

## 4 · ACTIONABLE EXECUTION SUMMARY

| Action | Symbol | Side | Lots | Entry | SL Bunker | TP Magnet | Risk USD | R:R | Engine | Archetype Defense | Rationale |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **STAND ASIDE** | — | — | — | — | — | — | — | — | — | A1/A3/A4/A6 all mechanically enforced | 0 of 24 assets clear the gate set: Engine 1 triggers nowhere (GER40's Z=−2.14 is counter-trend, unwalled, unmagnetised); Engine 2 ceilings are BTC 1.969R, ETH 0.597R, SOL 0.258R, SP500 0.505R against a 2.0R floor; the only live ticket (#18925879) was correctly cancelled (4 fatals). Book is flat, 0 positions, 0 pending, 4/4 slots free, cushion +64.55 USD above the buffer. |

**Forward protocol (armed, not staged — zero resting exposure):**

| Priority | Trigger | Action if it fires | Archetypes it answers |
|---|---|---|---|
| P1 | BTC 15 m high ≥ 82,880 **and** close back below 82,700, session CVD still negative | The 41.04M belt is consumed; re-derive a short from the realised sweep high + 0.35 ATR against the **25.0M USD buy wall @ 81,196 (persist 5,812 s)** and the 80,000–80,100 pool (23.13M). The 82,868 sell wall (22.83M, persist 4,512 s) is the barrier to break. | A2, A5, A8 — enters only after the fuel is spent |
| P2 | Any asset's ceiling (best reachable ÷ min compliant stop) ≥ 2.0R in a fresh generation | Run the tournament before staging. | A6 |
| P3 | SOL retraces to ≤ 105.2 with the 104.0–114.0 belt intact | **Do nothing** — the belt caps SOL's ceiling at 0.26R; wait for a belt sweep. | A1, A6 |

---

## 5 · ARENA TOURNAMENT (MANDATORY SKILL ENFORCEMENT)

**Method:** `.agent/skills/arena/{SKILL.md,rubric.md}` — weights **correctness 30 / completeness 25 / specificity 15 / robustness 20 / clarity 10**, **fatal rule** (a card contradicted by the snapshot cannot beat one that is not) applied before totals, single-elimination bracket, seed 106, executed by `Terminal/arena_tournament.py` on the 22:32:46 generation. *Runtime disclosure: the installed skill describes a 100-agent bracket; this cycle ran the five mandated council seats as the scored personas with the bracket executed mechanically — a single-assistant adaptation.*

| Card | Action | Fatal | Purchase-side hazard | Score | Verdict |
|---|---|---|---|---|---|
| `desk_stand_aside_cycle109` | STAND_ASIDE | no | — | **71.50** | **BRACKET WINNER** |
| `btc_armed_post_sweep_short` | WATCH | no | — | 69.00 | forward protocol |
| `sol_ticket_18925879_postmortem` | DELETE | no | — | 67.80 | **VERIFIED** — delete justified (4 fatals) |
| `desk_batch_3x_max_risk` | ×3 BATCH | YES | ENTRY_IN_FUEL | 49.55 | CONTRADICTED |
| `btc_perimeter_short_robust` | STAGE | YES | ENTRY_IN_FUEL | 48.18 | CONTRADICTED |
| `btc_perimeter_short_exact` | STAGE | YES | ENTRY_IN_FUEL | 48.00 | CONTRADICTED |
| `btc_deep_tp_extension` | STAGE | YES | ENTRY_IN_FUEL | 48.00 | CONTRADICTED |
| `eth_repair_short` | STAGE | YES | ENTRY_IN_FUEL | 48.00 | CONTRADICTED |
| `sol_short_repair` | STAGE | YES | ENTRY_IN_FUEL, BUNKER_WALL_THIN, COUNTER_CVD | 48.00 | CONTRADICTED |
| `near_short_friction_probe` | STAGE | YES | ENTRY_IN_FUEL, NO_BUNKER_WALL | 48.00 | CONTRADICTED (43.4% friction) |
| `trx_long_bullish_regime` | STAGE | YES | — | 48.00 | CONTRADICTED (SL inside [0.320,0.332], 28.1% friction) |
| `sp500_core_short` | STAGE | YES | ENTRY_IN_FUEL | 48.00 | CONTRADICTED (ceiling 0.50R) |
| `ger40_engine1_meanreversion` | STAGE (Engine 1) | YES | — | 42.59 | CONTRADICTED (counter-trend + no magnets + no walls) |

**Bracket path:** R1 dismissed every ticket-level card; R2 `sol_postmortem` beat `btc_robust`, `stand_aside` beat `btc_deep_tp`; R3 `stand_aside` beat `sol_postmortem` 71.50–67.80 and `armed_post_sweep` beat `sp500`; **R4 FINAL: `desk_stand_aside_cycle109` 71.50 vs `btc_armed_post_sweep_short` 69.00 → stand aside wins.**

**Personas on the winner (all five independent, all unanimous):** ① flow/tape: 24/24 coverage but zero eligible engines · ② structure: EMA stacks aligned bearish yet no entry inside the 2.0 ATR proximity bound is payable · ③ forensics: 85 verified walls exist, none converts a belt-wide stop into ≥2.0R · ④ governor: flat book, 4/4 slots, 64.55 USD budget, nothing worth spending it on · ⑤ red team: every candidate card was force-tested for the exact fatal flaw that killed the last three tickets — and each failed independently.

---

## 6 · GOVERNANCE CHECK

| Rule | Value | Status |
|---|---|---|
| Stressed loss per ticket | 1.25 × nominal + 2.00 USD | enforced in the engine |
| Best card stress (BTC exact) | 12.83 nominal → **18.04 stressed** | post-stop equity **4,841.51 ≥ 4,795.00** |
| Joint worst case (all three slots at max risk) | 3 × 20.12 = 60.36 ≤ 64.55 budget | feasible — but unused |
| Hard floor / buffer | 4,775.00 / 4,795.00 | preserved |
| Passive limits only | stand-aside + armed triggers place no order | satisfied |
| Zero archetype regression | A1/A3/A4/A6 mechanically gated; A2 enforced by regime+CVD rules | satisfied |

---

## 7 · INSTITUTIONAL QUANTITATIVE TELEMETRY AUDIT

### 7.1 Schema and data-quality findings (new this cycle)

| # | Finding | Evidence | Recommendation |
|---|---|---|---|
| 1 | **Index stop-cluster notionals look un-normalised** | SP500 belt = 18,418M USD over 110 points; the same asset's liquidation bands total 0.13M | Divide cluster notionals by `contract_size × point` and re-derive, or publish `amount_semantics` per asset. Until then index clusters are usable only as *relative* structure. |
| 2 | **Adjacent 100-pt bins defeat 5–10 bps front-running** | BTC: front-running the 80,600–80,700 pool lands inside 80,700–80,800; the ladder is contiguous from 81,600 to 80,500 | Emit a **merged-ladder** view (`contiguous_belt` with outer edges) so TP placement can target the *belt edge*, not the bin edge. The engine now computes belts internally; the feed should too. |
| 3 | **Persistence now works — make it first-class** | 85 walls carry `persist_s` ≥ 180 s; the earlier rollover produced a false zero | Add `persist_s_p95`, `relocation_count`, `first_seen_utc` and a `gate_g7_eligible` that is *computed*, not retired. |
| 4 | **No micro-price, no queue decay, no per-window aggressor ratio** | Schema has one OFI scalar for TradFi and session-only tick CVD for crypto | Add `micro_price`, `micro_price_drift_1m`, `ofi_l1..l5`, `taker_aggressor_ratio_1m/5m/15m/30m`, `queue_position_decay_per_s`, `footprint_absorption_score`. |
| 5 | **Session vs 24 h CVD divergence is unusable as a gate** | BTC session −98.85M with 15 m delta turning positive; SOL +7.67M session against a BEARISH regime | Publish `cvd_delta_5m/15m/30m` explicitly (the engine currently reads `divergence` labels, which are coarse). |

### 7.2 Calibrating Model 1 and Model 2 for payable 2.0–2.5R (the operator's core question)

The honest diagnosis from this cycle: **the binding constraint is not the regime test, it is (a) the width of the governing belt and (b) the contiguity of the magnet ladder.** A stop that clears a 1000-point BTC belt is 2.62 ATR wide; a 2.0R target therefore requires a magnet ~5.2 ATR away, which either does not exist or sits inside the ladder.

Three concrete, deployable calibrations:

1. **Belt-edge targeting (fixes contiguity).** Define the target as the *outer edge of the contiguous ladder being front-run*, not the bin edge: `TP = ladder_edge ± (5–10 bps)`. On BTC this alone moves the compliant target from "inside the neighbour" to 80,860.60.
2. **Volatility-scaled bunker with a payoff guard.** Replace the flat 0.35–0.50 ATR rule with `clearance = max(0.35, k·σ_book)` where σ_book = the 90th-percentile sweep depth observed in the last 200 sweeps for that asset, capped so that `RR ≥ 2.0` remains achievable — i.e., *skip the trade when the belt width × 2 exceeds the distance to the nearest non-contiguous magnet*. This converts today's knife-edge BTC card from "maybe" to an explicit "no", decided before staging.
3. **Payoff-first screening (what the engine now does).** Compute `max_achievable_RR` per asset *before* designing any ticket, and publish it in the telemetry as `payable_candidate: true/false`. Assets whose ceiling is < 2.0R should not consume council time at all. Today that is 23 of 24 assets, and the 24th (BTC) is at 1.969R.

### 7.3 Friction and execution optimisation under the 15% rule

* Minimum-lot spread cash today: BTC 0.17, SP500 0.03, ETH 0.03, GER40 0.31 USD — these instruments are effectively friction-free at size. **NEAR 3.30, TRX 9.00, ADA ~10, DOGE ~21, USDJPY 10.00, XRP 4.00 USD** remain mathematically excluded at minimum lot, independently of spreads-in-bps.
* The two live bindings this cycle were **stop-width friction** (SOL ticket 25.9%, NEAR 43.4%) — i.e., a *tight stop* is what makes friction lethal, not a wide spread. Practical rule: never size a ticket whose compliant stop is under ~6× the asset's spread.
* Macro blackout enforcement remains disabled by operator directive; no candidate in this cycle was delayed, disqualified or purged for the Fed-Bowman window.

---

## 8 · FINAL RULING

1. **No new tickets.** 0 of 24 assets clear the gate set; BTC's ceiling is 1.969R against a 2.0R floor.
2. **Ticket #18925879's cancellation is ratified** — 4 fatal gate failures (SL inside the 15.37M belt, 25.9% friction, TP inside a magnet, 2.72:1 overwhelm) and a 0.19R true ceiling.
3. **BTC post-sweep trigger stays armed** (P1 in §4). No resting order.
4. **Capacity:** 4/4 joint-fill slots free, 64.55 USD budget, unused. The cash cushion of +64.55 USD above the operating buffer is retained intact.

**Machine-readable trace:** `docs/trade_plans/arena_runs/cycle109_20261014T223246Z/run.json` (per-card findings, metrics, persona scores, bracket) · `…/REPORT.md` · cards `docs/trade_plans/arena_cards/cycle109_20261014T223246Z.json` · engine `Terminal/arena_tournament.py` (v2: long-side orientation, R-2 corridor rule, corridor fuel) · tests `Tests/Test_Arena_Tournament.py` — **36/36 passing**.
