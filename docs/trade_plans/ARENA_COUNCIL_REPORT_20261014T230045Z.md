# ARENA COUNCIL REPORT — CYCLE 110 (PURE TELEMETRY & PLAYBOOK ANALYSIS)

**Orchestrator**: Arena.ai Fable Tab (arena/f63583f1-trading-2) · **Prompt**: TRADING DESK COUNCIL CYCLE 110
**Screened generation**: `6a96f85bd4af40bb80306742add1e822` — as_of **2026-10-14 23:00:45 UTC** (the briefing cited `e8694354cd3b4dd6a2880782dcf0aff1` @ 22:59:59; that generation is 46 s stale)
**Canonical source**: `main` @ `63e1425171ab6b79a62af95f87ea40fc91670318` (2026-10-14 23:00:50Z)
**Desk state**: 0 positions · 0 pending · 0/4 joint-fill slots used, 4 available
**Account**: Blueberry Markets SVG LLC, MT5 #5064568 — balance = equity **4859.55 USD**, margin used 0.00 USD
**Floor**: hard 4775.00 · operating 4,795.00 · cushion **+84.55 above the floor / +64.55 above the buffer**

---

## §0 — TELEMETRY & PLAYBOOK INGESTION CITATION

* **generation_id**: `6a96f85bd4af40bb80306742add1e822` (line-by-line read: `assets_matrix_24` → 24 assets, `account`, `risk`, `capacity`, `active_positions`, `pending_orders`, `macro_calendar`, `hyperdash_flow_intelligence`, plus every per-asset block: `quotes`, `causal_indicators`, `multi_horizon_cvd`, `cvd_1m_buckets`, `tradfi_orderflow`, `htf_auction_profiles`, `volume_profile`, `structural_stop_clusters`, `reconstructed_liquidations`, `orderbook_live_depth.whale_walls_l3`, `trapped_traders_signal`, `venue_basis`, `execution_specs`).
* **as_of_utc**: 2026-10-14 23:00:45 UTC (epoch 1792018845.346594; clock basis `CALIBRATED_BROKER_UTC`)
* **data policy**: `OBSERVED_OR_DERIVED_FROM_OBSERVED; unavailable fields never authorize trades` — **observed-only**
* **trade_authorization**: `DENIED_UNVERIFIED_ORDERFLOW` (orderflow verification gate remains closed; this report therefore certifies *geometry and gate compliance*, never fill authority)
* **macro event**: `Fed Bowman Speech: Bangkok Economic Festival` @ 2026-10-15 02:55:00 UTC — blackout_active = **False**, enforcement = `DISABLED_BY_OPERATOR` (operator directive: never halt, purge or disqualify for news runway)
* **book coverage**: 24/24 assets carry causal indicators (VWAP/ATR/EMA stack/regime); **1,039 L3 wallet walls** (252 ≥ 500k USD, **634 with persist ≥ 180 s**); 85 ≥180 s walls was last cycle's high-water mark — persistence verification is now routine telemetry.
* **playbook compliance**: §5.1 spread/ATR ≤ 0.18; §7.4 15% dynamic friction rule with the calibrated wall thresholds (TradFi index ≥ 1.0M, commodities ≥ 0.75M, crypto major ≥ 5.0M, FX ≥ 0.50M); §7.4 graduated targets **ETH ≥ 2.2R, SOL ≥ 2.5R**; archetype registry A1–A8 (A9 retired with the blackout mandate); Gates R-1…R-4 enforced by `Terminal/arena_tournament.py`.

### §0.1 Engine integrity — corrections shipped with this cycle (disclosure)

The council does not quote a number it cannot reproduce. Three engine defects surfaced while preparing this cycle and are fixed in `Terminal/arena_tournament.py` (tests 39/39):

1. **Mandate RR floors (playbook §7.4)**: `RR_MIN_BY_ASSET = {ETHUSD.pi: 2.20, SOLUSD.p: 2.50}` — previously the engine applied a flat 2.0R floor to the two friction-heaviest admitted instruments.
2. **Minimum-compliant-stop convergence (archetype-1 mask)**: the stop derived by clearing the entry's own belt by 0.35 ATR could land *inside a second belt* just beyond it (live XAGUSD.pi: stop 56.7006 inside the [56.7, 57.1] belt). The anchor now walks outward (bounded) until the stop sits in free space with a full buffer to the next cluster — including near-miss clusters whose near edge is within one buffer length.
3. **Magnet-ladder merge (ceiling inflation)**: contiguous magnet bins are one ladder, not independent pools. Front-running an interior bin parked the TP *inside the neighbouring bin of the same ladder* — a TP the engine's own `TP_INSIDE_MAGNET` gate rejects — which inflated `max_achievable_rr` on every asset whose stops/cascades are binned adjacently (BTC's sell-stop ladder below runs [80,500→81,600] in 100-pt bins). Merged, the reported Cycle-106 BTC ceiling falls from **1.88R to 0.73R**; the Cycle-109 BTC ceiling of 1.969R was the same artifact (this generation's honest BTC card pays **0.59R** and has **no front-runnable exit at all**). A new `PRICE_INSIDE_MAGNET_LADDER` finding records the case where price itself sits inside a ladder.

**Net effect on prior rulings**: every prior *conclusion* (stand aside; delete the SOL ticket; do not fade the BTC belt) survives — the corrections make the geometry strictly **worse**, not better. Any number quoted from Cycle 106/109 ceilings is superseded by this report.

---

## §1 — MANDATE 1: LINE-BY-LINE SCREEN OF ALL 24 ASSETS (DUAL ENGINE)

**Result: 0 CANDIDATE · 0 WATCHLIST · 24 NO SETUP.** Engine 1 (|Z| ≥ 2.0 mean reversion) triggers nowhere usable; Engine 2 (trend pullbacks) is unpayable or structurally blocked on every asset. The only forward-looking posture the book supports is the armed BTC post-sweep trigger (§9) — a condition, not an order. Full table, then the per-asset reasoning.

| Asset | Symbol | Class | Mid | Z | RSI | Regime | Spread bps | Engine 1 verdict | Engine 2 verdict | Final |
|---|---|---|---|---|---|---|---|---|---|---|
| BTC | BTCUSD.pi | CRYPTO_MAJOR | 81563.5 | -1.23 | 41.84 | BEARISH | 2.08 | no trigger (|Z| < 2.0) | S: no legal perimeter geometry (step-1 fatals: NO_REACHABLE_MAGNET, SL_INSIDE_SWEEP, TP_INSIDE_MAGNET) · L: best 0.71R vs 2.0R floor → COUNTER_TREND, NO_PAYABLE_SETUP, RR_BELOW_MIN, UNPAYABLE_GEOMETRY | **NO SETUP** |
| ETH | ETHUSD.pi | CRYPTO_MAJOR | 2416.4 | -1.25 | 40.75 | BEARISH | 11.59 | no trigger (|Z| < 2.0) | S: no legal perimeter geometry (step-1 fatals: FRICTION_BUDGET, NO_REACHABLE_MAGNET, SL_INSIDE_SWEEP, TP_INSIDE_MAGNET) · L: best 0.24R vs 2.2R floor → COUNTER_TREND, NO_PAYABLE_SETUP, OVERWHELM_RATIO, RR_BELOW_MIN, UNPAYABLE_GEOMETRY | **NO SETUP** |
| SOL | SOLUSD.p | CRYPTO_ALT | 104.435 | -0.7 | 50.39 | BEARISH | 22.02 | no trigger (|Z| < 2.0) | S: best 0.16R vs 2.5R floor → NO_PAYABLE_SETUP, OVERWHELM_RATIO, RR_BELOW_MIN, UNPAYABLE_GEOMETRY · L: best 0.24R vs 2.5R floor → COUNTER_TREND, NO_PAYABLE_SETUP, OVERWHELM_RATIO, RR_BELOW_MIN, UNPAYABLE_GEOMETRY | **NO SETUP** |
| BNB | BNBUSD.p | CRYPTO_ALT | 728.95 | -1.29 | 48.73 | BEARISH | 6.86 | no trigger (|Z| < 2.0) | S: no legal perimeter geometry (step-1 fatals: FRICTION_BUDGET, NO_MAGNETS, SL_INSIDE_SWEEP) · L: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, FRICTION_BUDGET, NO_REACHABLE_MAGNET, SL_INSIDE_SWEEP) | **NO SETUP** |
| XRP | XRPUSD.pi | CRYPTO_ALT | 1.3315 | -0.73 | 50.31 | BEARISH | 22.53 | no trigger (|Z| < 2.0) | S: best 0.38R vs 2.0R floor → FLOOR_BREACH, NO_PAYABLE_SETUP, RR_BELOW_MIN, UNPAYABLE_GEOMETRY · L: best 0.30R vs 2.0R floor → COUNTER_TREND, FLOOR_BREACH, NO_PAYABLE_SETUP, RR_BELOW_MIN, UNPAYABLE_GEOMETRY | **NO SETUP** |
| ADA | ADAUSD.p | CRYPTO_ALT | 0.2291 | -0.47 | 54.09 | BEARISH | 91.64 | no trigger (|Z| < 2.0) | S: no legal perimeter geometry (step-1 fatals: FRICTION_BUDGET, NO_MAGNETS, SL_INSIDE_SWEEP) · L: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, FRICTION_BUDGET, NO_MAGNETS, SL_INSIDE_SWEEP) | **NO SETUP** |
| DOGE | DOGUSD.p | CRYPTO_ALT | 0.0819 | -0.31 | 48.01 | BEARISH | 256.57 | no trigger (|Z| < 2.0) | S: no legal perimeter geometry (step-1 fatals: FRICTION_BUDGET, NO_REACHABLE_MAGNET, SL_INSIDE_SWEEP) · L: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, FRICTION_BUDGET, NO_MAGNETS, SL_INSIDE_SWEEP) | **NO SETUP** |
| TRX | TRXUSD.p | CRYPTO_ALT | 0.3321 | 0.15 | 32.5 | BULLISH | 24.09 | no trigger (|Z| < 2.0) | S: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, FRICTION_BUDGET, NO_MAGNETS, SL_INSIDE_SWEEP) · L: no legal perimeter geometry (step-1 fatals: FRICTION_BUDGET, NO_MAGNETS, SL_INSIDE_SWEEP) | **NO SETUP** |
| DOT | DOTUSD.pi | CRYPTO_ALT | 1.145 | 0.85 | 63.41 | BEARISH | 174.67 | no trigger (|Z| < 2.0) | S: no legal perimeter geometry (step-1 fatals: FRICTION_BUDGET, NO_MAGNETS) · L: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, FRICTION_BUDGET, NO_MAGNETS, SL_INSIDE_SWEEP) | **NO SETUP** |
| LINK | LNKUSD.p | CRYPTO_ALT | 12.396 | -1.06 | 45.18 | BEARISH | 69.38 | no trigger (|Z| < 2.0) | S: no legal perimeter geometry (step-1 fatals: FRICTION_BUDGET, NO_REACHABLE_MAGNET, SL_INSIDE_SWEEP) · L: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, FRICTION_BUDGET, NO_MAGNETS, SL_INSIDE_SWEEP) | **NO SETUP** |
| BCH | BCHUSD.p | CRYPTO_ALT | 267.6 | -1.45 | 41.83 | BEARISH | 17.94 | no trigger (|Z| < 2.0) | S: no legal perimeter geometry (step-1 fatals: FRICTION_BUDGET, NO_MAGNETS, SL_INSIDE_SWEEP) · L: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, FRICTION_BUDGET, NO_REACHABLE_MAGNET, SL_INSIDE_SWEEP) | **NO SETUP** |
| LTC | LTCUSD.pi | CRYPTO_ALT | 59.24 | -0.94 | 42.8 | BEARISH | 50.64 | no trigger (|Z| < 2.0) | S: best 0.42R vs 2.0R floor → FRICTION_BUDGET, NO_PAYABLE_SETUP, RR_BELOW_MIN, UNPAYABLE_GEOMETRY · L: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, FRICTION_BUDGET, NO_MAGNETS, SL_INSIDE_SWEEP) | **NO SETUP** |
| AVAX | AVXUSD.p | CRYPTO_ALT | 9.99 | -0.37 | 61.64 | BEARISH | 40.04 | no trigger (|Z| < 2.0) | S: no legal perimeter geometry (step-1 fatals: FRICTION_BUDGET, NO_MAGNETS) · L: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, FRICTION_BUDGET, NO_MAGNETS) | **NO SETUP** |
| NEAR | NERUSD.p | CRYPTO_ALT | 4.873 | -0.87 | 56.06 | BEARISH | 65.67 | no trigger (|Z| < 2.0) | S: best 2.53R vs 2.0R floor → FRICTION_BUDGET · L: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, FRICTION_BUDGET, NO_REACHABLE_MAGNET, SL_INSIDE_SWEEP) | **NO SETUP** |
| SP500 | SP500.p | INDEX | 7703.92 | -1.41 | 32.36 | BEARISH | 0.44 | no trigger (|Z| < 2.0) | S: best 0.41R vs 2.0R floor → NO_PAYABLE_SETUP, RR_BELOW_MIN, UNPAYABLE_GEOMETRY · L: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, NO_REACHABLE_MAGNET, SL_INSIDE_SWEEP) | **NO SETUP** |
| NAS100 | NAS100.p | INDEX | 29785.57 | -1.88 | 21.76 | BEARISH | 0.41 | no trigger (|Z|=1.88 < 2.0) | S: no legal perimeter geometry (step-1 fatals: NO_REACHABLE_MAGNET, SL_INSIDE_SWEEP, TP_INSIDE_MAGNET) · L: best 0.14R vs 2.0R floor → COUNTER_TREND, FLOOR_BREACH, NO_PAYABLE_SETUP, OVERWHELM_RATIO, RR_BELOW_MIN, UNPAYABLE_GEOMETRY | **NO SETUP** |
| DJ30 | DJ30.p | INDEX | 51621.85 | 0.1 | 55.07 | BEARISH | 0.31 | no trigger (|Z| < 2.0) | S: no legal perimeter geometry (step-1 fatals: NO_MAGNETS) · L: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, NO_MAGNETS) | **NO SETUP** |
| GER40 | GER40.p | INDEX | 25203.4 | -2.07 | 34.09 | BEARISH | 1.23 | **TRIGGER** |Z|=−2.07 — disqualified: long-only mean reversion vs BEARISH regime (counter-trend ban) + 0 walls + 0 magnets | S: no legal perimeter geometry (step-1 fatals: FRICTION_BUDGET, NO_MAGNETS) · L: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, FRICTION_BUDGET, NO_MAGNETS) | **NO SETUP** |
| GOLD | XAUUSD.pi | COMMODITY | 4106.59 | -0.33 | 56.05 | BEARISH | 0.29 | no trigger (|Z| < 2.0) | S: best 0.40R vs 2.0R floor → FLOOR_BREACH, NO_PAYABLE_SETUP, RR_BELOW_MIN, UNPAYABLE_GEOMETRY · L: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, NO_MAGNETS, SL_INSIDE_SWEEP) | **NO SETUP** |
| SILVER | XAGUSD.pi | COMMODITY | 55.632 | -1.29 | 43.28 | BEARISH | 6.47 | no trigger (|Z| < 2.0) | S: best 0.73R vs 2.0R floor → FLOOR_BREACH, NO_PAYABLE_SETUP, RR_BELOW_MIN, UNPAYABLE_GEOMETRY · L: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, FRICTION_BUDGET, NO_REACHABLE_MAGNET, SL_INSIDE_SWEEP) | **NO SETUP** |
| USWTI | USWTI.p | COMMODITY | 94.9 | -0.87 | 37.8 | BULLISH | 4.85 | no trigger (|Z| < 2.0) | S: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, FRICTION_BUDGET, NO_REACHABLE_MAGNET, SL_INSIDE_SWEEP) · L: no legal perimeter geometry (step-1 fatals: FRICTION_BUDGET, NO_MAGNETS) | **NO SETUP** |
| EURUSD | EURUSD.pi | FX | 1.1174 | 0.59 | 72.54 | BEARISH | 0.09 | no trigger (|Z| < 2.0) | S: no legal perimeter geometry (step-1 fatals: NO_REACHABLE_MAGNET, TP_INSIDE_MAGNET) · L: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, NO_REACHABLE_MAGNET, SL_INSIDE_SWEEP) | **NO SETUP** |
| GBPUSD | GBPUSD.pi | FX | 1.3205 | -0.1 | 65.56 | BEARISH | 0.08 | no trigger (|Z| < 2.0) | S: no legal perimeter geometry (step-1 fatals: NO_MAGNETS, SL_INSIDE_SWEEP) · L: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, NO_REACHABLE_MAGNET) | **NO SETUP** |
| USDJPY | USDJPY.pi | FX | 158.092 | -1.6 | 26.44 | BEARISH | 0.38 | no trigger (|Z| < 2.0) | S: no legal perimeter geometry (step-1 fatals: FLOOR_BREACH, NO_REACHABLE_MAGNET, SL_INSIDE_SWEEP) · L: no legal perimeter geometry (step-1 fatals: COUNTER_TREND, FLOOR_BREACH, NO_REACHABLE_MAGNET) | **NO SETUP** |

### Engine 1 — extreme mean reversion (|Z| ≥ 2.0, all four legs required)

Only **GER40** reaches the statistical trigger (Z = −2.07, RSI 34.09) and it fails every other leg: a Model-1 long is banned in a verified BEARISH regime (EMA20 25,184 < EMA50 25,310 < EMA200 25,353 with price under all three), the asset carries **zero** whale walls ≥ 180 s, **zero** structural stop clusters and **zero** reconstructed liquidation bands — there is no tape-exhaustion evidence, no whale backing and no magnet to exit into. **NAS100** (Z = −1.88, RSI 21.76) is the near-miss: still sub-threshold, and its price sits *inside* a 21.8M USD long-cascade ladder [28,800–29,800], so no front-runnable exit exists either.

### Engine 2 — trend pullbacks (regime + shelf + walls + low velocity)

All 24 assets print BEARISH regime except TRX and USWTI (BULLISH); trend-first hierarchy therefore permits pullback **shorts** and bans longs everywhere else. Every short dies on one of four gates:

* **Unpayable geometry (A6)** — the reachable, front-runnable exit is too close relative to the compliance-mandated stop: BTC 0.59R (blocked), ETH 0.16R, SOL 0.16R, SP500 0.41R, NAS100 n/a, GOLD 0.39R, SILVER 0.73R, XRP 0.37R, LTC 0.42R.
* **Friction (A7)** — NEAR is the only asset whose geometry reaches 2.0R (2.53R) and it pays 41.5% of its risk in spread; TRX 381%, LTC 15.5%, ADA/DOGE/DOT/LINK/AVAX all breach the 15% rule before the R-floor is even asked.
* **Price inside the magnet ladder (new A6 sub-case)** — BTC mid 81,563.50 sits **inside** the $94.59M sell-stop ladder [80,500–81,600]; ETH mid 2,416.40 sits inside the $101.87M sell-stop ladder [2,320–2,420] (with a $202.80M cascade ladder overlapping it); SOL mid 104.435 sits inside the $15.38M buy-stop belt [104–114]. For these three, the exit cannot front-run a pool without being inside one.
* **Ephemeral / thin defense (A4)** — where the geometry is otherwise closest to sanity, the bunker fails the asset-class threshold: SOL's best in-corridor wall is 4.85M < 5.0M (crypto alt); NEAR, LTC, TRX, DOGE and the FX book have no qualifying wall at all.


### §1.1 — Closest-call dossiers (why the top four do not clear)

| Asset | Best legal geometry | Binding arithmetic | Archetype that kills it |
|---|---|---|---|
| **BTC** | SELL LIMIT 82,055.49 (mid + 1.95 ATR) · SL 82,690.83 · TP must clear 81,600 | quoted 0.59R; no front-runnable exit at all — mid 81,563.50 is *inside* the $94.59M ladder [80,500–81,600] | **A6** unpayable geometry + **A8** entry parked in $41.04M of un-swept buy-stop fuel |
| **NEAR** | SELL LIMIT 4.9584 · SL 5.0355 · TP 4.7636 | 2.53R geometry, but spread 0.0320 USD ÷ 0.0771 stop = **41.5% of risk** | **A7** friction (also on the playbook banned list at 62%) |
| **SILVER** | SELL LIMIT 56.1844 · SL 57.2006 · TP 55.4415 | 0.73R ceiling; min lot 0.01 sizes a **50.81 USD** risk vs the 14.50 envelope | **A5/A7** floor + lot granularity (FLOOR_BREACH) |
| **SP500** | SELL LIMIT 7,723.22 · SL 7,813.51 · TP 7,685.76 | 0.41R: an $18,418.6M index belt [7,700–7,810] forces a 90-pt stop against a 37-pt reachable reward | **A6** unpayable geometry + **A8** entry in the cluster |

Every one of these geometries was *constructed to be as favourable as the playbook allows* (deep shelf anchor, 0.36 ATR clearance, 5–10 bps front-run) before being rejected — the screen is a falsification harness, not a wish list.

---

## §2 — MANDATE 2: ACTIVE / RUNNING TRADES AUDIT

`active_positions` = **[]** — the desk is flat. `risk.total_contingent_stress_usd` = **0.00 USD**, `post_joint_stop_equity_usd` = **4859.55 USD** vs the 4,795.00 buffer (floor buffer preserved = true). No ratchet, no TP/SL modification, no protective action is mathematically required or permitted: there is nothing to modify, and the frozen-R0 bookkeeping of the desk is empty by definition.

---

## §3 — MANDATE 3: UNFILLED LIMIT ORDERS AUDIT (TICKET BY TICKET)

`pending_orders` = **[]** on generation `6a96f85bd4af40bb80306742add1e822` — **0 pending tickets**. Nothing to WAIT on, nothing to MODIFY, nothing to DELETE. The audit is therefore a **post-mortem confirmation** of the only recently-live order:

**Ticket #18925879** (SOLUSD.p SELL LIMIT 0.10 @ 104.90 / SL 105.75 / TP 103.10), re-audited at the desk's own levels against this generation → **DELETE — confirmed** (`verified = true`, i.e. the delete is justified by at least one independent fatal gate).

* probe fatals: `FRICTION_BUDGET, SL_INSIDE_SWEEP, UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, TP_INSIDE_MAGNET`
* probe majors: `SPREAD_OVER_ATR, ENTRY_IN_FUEL, BUNKER_WALL_THIN, RR_BELOW_MIN, COUNTER_CVD`
* geometry: quoted RR 2.12R against the **2.5R SOL floor**; friction **27.06%** of risk; SL sits **3.18 ATR inside** the [104.0, 114.0] purchase-side belt ($15.38M); asset ceiling **0.09R**; entry 0.85 ATR from mid with $15.38M of un-swept fuel at/above it.
* The desk's own cancellation (observed between the 22:29:55 and 22:30:40 generations, balance unchanged at 4,859.55) is therefore **ratified for the second consecutive cycle** — and the new SOL 2.5R floor makes the ticket even more indefensible than it looked in Cycle 109.

---

## §4 — ACTIONABLE EXECUTION SUMMARY TABLE

| Action | Symbol | Side | Lots | Entry | SL Bunker | TP Magnet | Risk USD | R:R | Engine | Archetype Defense | Rationale |
|---|---|---|---|---|---|---|---|---|---|---|---|
| STAND ASIDE | — | — | — | — | — | — | — | — | — | A1–A8 all | No ticket on any of the 24 assets clears the dual-engine gates: 0 eligible Engine-1 triggers, 0 payable Engine-2 geometries, 4 free slots and the +64.55 USD cushion retained unspent |

A single row is the *correct* output of a nine-gate falsification harness that found nothing to certify. The tournament (below) competitively evaluated 15 hypotheses, including every plausible alternative, and the stand-aside card won.

---

## §5 — ARENA SKILL IMPLEMENTATION & TOURNAMENT

**Skill provenance** (MANDATE: always): the canonical tournament methodology is installed in-repo at `.agent/skills/arena/` (`SKILL.md`, `rubric.md`, `bracket.py`), mirrored from `https://github.com/Jakeschincariol/arena-skill`, and is a first-class repository feature — `Terminal/arena_tournament.py` re-implements the bracket deterministically (seeded, rubric-weighted, fatal-rule-first) so the arbitration is reproducible by any operator instead of living in a chat narrative. Rubric weights: correctness 30 / completeness 25 / specificity 15 / robustness 20 / clarity 10.

**Run**: `docs/trade_plans/arena_runs/cycle110_20261014T230045Z/` (seed 106, snapshot `6a96f85bd4af40bb80306742add1e822`, cards sha in `run.json`), 15 competing cards.

| # | Hypothesis (card) | Action | Rubric total | Fatal | Verdict |
|---|---|---|---|---|---|
| 1 | `desk_stand_aside_cycle110` | STAND_ASIDE | 71.50 | no | stands |
| 2 | `btc_armed_post_sweep_short` | WATCH | 69.00 | no | stands |
| 3 | `sol_ticket_18925879_reaudit` | DELETE | 59.64 | no | verified |
| 4 | `near_friction_probe` | STAGE | 51.39 | **yes** | CONTRADICTED by snapshot |
| 5 | `btc_ladder_top_long` | STAGE | 48.00 | **yes** | CONTRADICTED by snapshot |
| 6 | `sol_repair_short` | STAGE | 48.00 | **yes** | CONTRADICTED by snapshot |
| 7 | `sp500_core_short` | STAGE | 48.00 | **yes** | CONTRADICTED by snapshot |
| 8 | `trx_bullish_regime_long` | STAGE | 48.00 | **yes** | CONTRADICTED by snapshot |
| 9 | `gold_minlot_floor_probe` | STAGE | 48.00 | **yes** | CONTRADICTED by snapshot |
| 10 | `ger40_engine1_long` | STAGE | 44.84 | **yes** | CONTRADICTED by snapshot |
| 11 | `btc_ladder_straddle_short` | STAGE | 43.77 | **yes** | CONTRADICTED by snapshot |
| 12 | `eth_straddle_short` | STAGE | 42.58 | **yes** | CONTRADICTED by snapshot |
| 13 | `desk_batch_4x_max_risk` | STAGE_BATCH | 42.58 | **yes** | CONTRADICTED by snapshot |
| 14 | `uswti_bullish_regime_long` | STAGE | 42.50 | **yes** | CONTRADICTED by snapshot |
| 15 | `dj30_empty_book_probe` | STAGE | 42.50 | **yes** | CONTRADICTED by snapshot |

**Bracket path (single elimination, deterministic):**

* R1: `near_friction_probe` vs `eth_straddle_short` → **near_friction_probe** (higher rubric total (51.39 vs 42.58))
* R1: `gold_minlot_floor_probe` vs `sol_repair_short` → **gold_minlot_floor_probe** (exact tie: fewer standing attacks (deterministic order))
* R1: `btc_ladder_top_long` vs `dj30_empty_book_probe` → **btc_ladder_top_long** (higher rubric total (48.0 vs 42.5))
* R1: `ger40_engine1_long` vs `sp500_core_short` → **sp500_core_short** (higher rubric total (48.0 vs 44.84))
* R1: `sol_ticket_18925879_reaudit` vs `btc_armed_post_sweep_short` → **btc_armed_post_sweep_short** (higher rubric total (69.0 vs 59.64))
* R1: `desk_stand_aside_cycle110` vs `uswti_bullish_regime_long` → **desk_stand_aside_cycle110** (uswti_bullish_regime_long is contradicted by the snapshot; desk_stand_aside_cycle110 is not)
* R1: `btc_ladder_straddle_short` vs `trx_bullish_regime_long` → **trx_bullish_regime_long** (higher rubric total (48.0 vs 43.77))
* R2: `near_friction_probe` vs `gold_minlot_floor_probe` → **near_friction_probe** (higher rubric total (51.39 vs 48.0))
* R2: `btc_ladder_top_long` vs `sp500_core_short` → **btc_ladder_top_long** (exact tie: fewer standing attacks (deterministic order))
* R2: `btc_armed_post_sweep_short` vs `desk_stand_aside_cycle110` → **desk_stand_aside_cycle110** (higher rubric total (71.5 vs 69.0))
* R2: `trx_bullish_regime_long` vs `desk_batch_4x_max_risk` → **trx_bullish_regime_long** (higher rubric total (48.0 vs 42.58))
* R3: `near_friction_probe` vs `btc_ladder_top_long` → **near_friction_probe** (higher rubric total (51.39 vs 48.0))
* R3: `desk_stand_aside_cycle110` vs `trx_bullish_regime_long` → **desk_stand_aside_cycle110** (trx_bullish_regime_long is contradicted by the snapshot; desk_stand_aside_cycle110 is not)
* R4: `near_friction_probe` vs `desk_stand_aside_cycle110` → **desk_stand_aside_cycle110** (near_friction_probe is contradicted by the snapshot; desk_stand_aside_cycle110 is not)

**WINNER: `desk_stand_aside_cycle110` — rubric 71.50/100, five-seat NO OBJECTION.**

The final was decided on the fatal rule, not on rhetoric: the NEAR card carried the only ≥2.0R geometry in the book (2.53R) and was still struck down by the 15% dynamic friction rule (41.5%), while the stand-aside card survived every gate attack. The armed BTC WATCH card scored 69.00 — a strong second: it is the only forward-looking posture the book supports.

---

## §6 — FIVE PERSONAS, INDEPENDENT, THEN SYNTHESIS

Each seat audits the same generation through its own discipline; the engine records each seat's evidence verbatim (`personas` in run.json).

**1. Orderflow & Microstructure Analyst** — 24/24 assets report taker flow: session CVD is negative on BTC (−$103.54M), ETH (−$101.00M), BNB, XRP, LTC, NEAR and the equity indices, while SOL (+$7.65M), XRP (+$29.80M), TRX (+$9.58M) and the FX book print positive tick CVD. **Vote: NO OBJECTION to standing aside** — shorting into SOL's positive CVD or holding long into BTC's −$103.5M are both archetype-2 errors; the flow book offers no clean directional asymmetry at a payable distance.

**2. Structural Price Action Specialist** — the EMA stack is bearish on 22 of 24 assets (price < EMA20 < EMA50 < EMA200 on BTC: 81,563.5 < 81,661 < 82,027 < 82,749; ETH 2,416 < 2,420 < 2,440 < 2,480; NAS100 29,786 < 29,8xx). Pullbacks are *into* shelves that sit under six-figure ladder fuel, so the shelf-touch leg is satisfied while the exit leg is not. **Vote: NO OBJECTION** — the correct reading of a bearish, ladder-pinned tape is patience, not participation.

**3. Liquidation & Stop Hunt Forensic** — the new ladder view is the story of the cycle: **19 price-inside-ladder cases** across the book, including BTC's $94.59M sell-stop ladder straddling mid and the $18,418.6M SP500 index cluster belt [7,700–7,810]. Front-running a ladder that contains price is impossible; the exit must clear the ladder's near edge, which collapses every R-multiple. **Vote: NO OBJECTION** — a stop inside the ladder or a TP inside the ladder is archetype-1/6; both are avoided by standing aside.

**4. Macro Risk & Portfolio Governor** — balance 4,859.55 = equity; 0.00 contingent stress; post-joint-stop equity 4,859.55 vs the 4,795.00 buffer; 0/4 slots used; +64.55 USD budget. Capacity could fund **three** max-risk tickets (3 × 20.13 = 60.38 ≤ 64.55) — and that is exactly why the governor insists on quality: the floor survives the fourth only by refusing it. **Vote: NO OBJECTION.**

**5. Adversarial Pre-Mortem Red Team** — the default is no trade. Every STAGE card in the universe was probed by the full gate set: BTC short → `NO_REACHABLE_MAGNET, RR_BELOW_MIN`; ETH short → `NO_REACHABLE_MAGNET, RR_BELOW_MIN`; SOL → `UNPAYABLE_GEOMETRY, NO_PAYABLE_SETUP, RR_BELOW_MIN`; NEAR → `FRICTION_BUDGET`; GOLD → `FLOOR_BREACH` (min lot risks 92.54 USD against a 14.50 envelope); GER40 long → `NO_MAGNETS, COUNTER_TREND`; TRX long → `FRICTION_BUDGET, SL_INSIDE_SWEEP, NO_MAGNETS`; USWTI long → `NO_MAGNETS`; DJ30 → `NO_MAGNETS`. Every archetype A1–A8 has at least one live example; none of them is on our side of the ledger. **Vote: NO OBJECTION.**

**Synthesis** — five independent disciplines converge on the same sentence: *the tape is hostile to both engines and the exit geometry is the binding constraint, not the entry*. The council therefore ratifies the stand-aside, keeps the BTC post-sweep trigger armed, and spends nothing.

---

## §7 — GOVERNANCE STRESS MATH

Stressed loss per ticket = 1.25 × nominal risk + 2.00 USD. Budget to the 4,795.00 operating buffer = 64.55 USD.

| Sizing scenario | Nominal risk | Stressed (per ticket) | Joint stress | Post-stop equity | Floor verdict |
|---|---|---|---|---|---|
| 1 × max envelope (14.50) | 14.50 | 20.13 | 20.13 | 4,839.42 | **OK** (+44.42 above buffer) |
| 2 × max envelope | 29.00 | 20.13 | 40.25 | 4,819.30 | **OK** (+24.30) |
| 3 × max envelope | 43.50 | 20.13 | 60.38 | 4,799.18 | **OK** (+4.18 — the binding limit) |
| 4 × max envelope | 58.00 | 20.13 | 80.50 | 4,779.05 | **BREACH** (−15.95 below buffer, +4.05 above the 4,775 hard floor) |
| Best card of this cycle (`btc_ladder_straddle_short`) | 12.71 | 17.88 | 17.88 | 4841.67 | OK for stress, fatal for geometry |

The `desk_batch_4x_max_risk` strawman went through the tournament to prove the boundary empirically: the engine flagged `FLOOR_BREACH`, the same boundary the governor computes by hand. Three tickets fit; four do not; zero were staged.

---

## §8 — INSTITUTIONAL QUANTITATIVE TELEMETRY AUDIT & PROFITABILITY MANDATE

### 8a. Schema & microstructure gaps (what the JSON does not yet carry)

This generation is the strongest coverage yet — 24/24 causal blocks, 1,039 L3 walls, 634 with persist ≥ 180 s (median 780 s, p90 7,492 s), 252 ≥ 500k USD, venue basis, per-asset execution specs, 1-minute CVD buckets. The remaining gaps, in priority order:

1. **Multi-level OFI (l2–l5)**. The snapshot exposes `book_imbalance` (top-20) and a single `skew_ratio`. Order-flow imbalance at several depths — `OFI_k = Σ(Δbid_vol_k − Δask_vol_k)/(ΣΔ)` over the last 1–5 s at levels 2…5 — separates *queue replenishment* from *aggressive taking*. Without it, L2 imbalance cannot be distinguished from spoof replenishment (today's BTC imbalance −0.7289 with bid depth 141.9k vs ask depth 905.1k is consistent with both).
2. **Micro-price drift vs mid** (`microprice = (bid·ask_sz + ask·bid_sz)/(bid_sz+ask_sz)`), reported as bps drift over 1/5/15 s. The mid is a stale two-sided average; the micro-price leads it by ~1 tick, which is exactly the edge we need for limit-queue priority on the entries we keep missing by 8×10⁻⁷ ATR.
3. **Queue-position decay rate**. We consume `persist_s` (age) but not the *decay slope*: `d(notional)/dt` per wall, plus a `relocation_count`. A wall that has decayed >50% in 90 s is archetype-4 fuel; today the schema reports only first-visit age.
4. **Taker-aggressor ratio over 1 / 5 / 15 / 30 m** (buy-taker USD ÷ sell-taker USD, log). `cvd_1m_buckets` allows a reconstruction but the ratio is not materialised, nor is its 30-minute baseline — which is how we distinguish *exhaustion* (ratio reverting toward 1 with falling volume) from *momentum* (ratio extreme with rising volume).
5. **Footprint absorption score** per price bin: `absorbed_usd / traded_usd` at the bid/ask. The `trapped_traders_signal` gives the binary state (TRAPPED_BUYERS_ABOVE / TRAPPED_SELLERS_BELOW / BALANCED) but no magnitude of the absorbed flow — the single strongest candidate for turning *tape exhaustion* from a human judgement into a number.
6. **Index-notional normalisation** (audit carry-over): SP500's [7,700–7,810] cluster prints $18,418.6M against $0.13M of neighbouring liquidation bands — a 5-order-of-magnitude discontinuity inside one asset block. Until the feed publishes merged contiguous belts and a unit convention, index clusters must be read as *relative* structure, never as comparable notional.
7. **Merged contiguous belts + `persist_s_p95`**. The engine now merges 100-pt bins internally; the feed should publish the merged belt (lo, hi, Σnotional, bin_count, persist p95) so downstream tools cannot double-count or under-front-run a ladder.

### 8b. How to construct payable 2.0–2.5R setups without multi-day excursions

The binding constraint this cycle is **exit geometry**, not entry timing. The arithmetic that produces *no candidates* is:

* Payable target distance must be ≥ 2.0–2.5 × (compliant stop distance).
* The compliant stop distance is set by the contiguous hazard belt (0.35–0.50 ATR outside its outer edge) — on BTC that is 2.6 ATR because the purchase-side belt [81,600–82,600] is $41.04M deep.
* The compliant target must front-run a magnet 5–10 bps from its near edge, inside a 3.5-ATR reach horizon — and **may not sit inside any ladder** (new gate).

So a payable setup needs either (i) a **narrow hazard belt** relative to the reward pool, or (ii) a **collapsed stop** legitimately outside a thin belt. Concretely, for Cycle 111 the council proposes:

1. **Belt-efficiency screening**: rank assets by `reward_pool_usd ÷ belt_usd` within the 3.5-ATR horizon, and only then run the R-test. An asset whose hazard belt is >3× its reachable reward pool can never pay 2.0R — that is a one-line filter that removes the 24-asset scan's dead weight (this generation: BTC 41.04 vs 4.12 = 10.0×, ETH 17.97 vs 7.99 = 2.25×, SP500 18,418 vs 2.12 = 8,700×).
2. **Two-leg structures where the strategy permits**: enter on the reversal leg with a stop outside the *first* belt, and take the second leg only after the first belt is consumed (the armed-trigger pattern already in the BTC WATCH card). This converts a 2.6-ATR stop into a 0.9-ATR stop after the sweep, which is the only path to 2.0R+ on a ladder-pinned asset.
3. **Volatility-surface-calibrated buffers**: replace the fixed 0.35 ATR buffer with `max(0.35 ATR, k·σ_book)` where σ_book is the depth-weighted spread-of-depth at the stop level. Today the buffer is calibrated to the *time-series* volatility only; adding the book's static depth makes it robust to the sweep geometry that actually hunts stops.
4. **TP front-run calibration**: 5–10 bps is correct for liquid books; for books whose top-20 depth is < $200k (XRP 0.09M, TRX 0.58M) the required front-run scales with `spread_bps + depth_penalty`. Publish `front_run_bps = clip(5, 10, 2·spread_bps)`, feeding it to the engine instead of the constant.
5. **Never size a ticket whose compliant stop is under ~6× the asset spread.** This generation's friction bindings were stop-width problems, not spread problems: SOL 25.9% and NEAR 41.5% of risk lost to spread *because* the compliant stop was 4–10 spread-widths wide. The rule turns friction from a post-hoc veto into a pre-screen: min-lot spread cash ≥ 2.175 USD (15% × 14.50) disqualifies NEAR (3.20), TRX (8.00), ADA (10.50), DOGE (21.00), LTC (3.00), XRP (3.00), USDJPY (6.00) outright at the minimum lot.

### 8c. Maximum net alpha under the 15% friction rule (macro blackouts permanently disabled)

* **Trade the two friction champions when their geometry clears.** SP500 (0.44 bps) and NAS100 (0.41 bps) carry 0.4% friction — their disqualification this cycle was purely geometric (0.41R / n/a). If either prints a day where the belt is thin (post-sweep) the same assets pay 2.0R+. Keep them in the top trio of every scan.
* **Use the friction budget as a sizing tool, not only a veto.** Since stress is 1.25 × nominal + 2.00, the *cheapest* friction per stressed dollar is on the tight-spread indices; the marginal risk budget should always be spent there first.
* **Never chase the volume.** The book's most active alts (DOGE 256.6 bps, DOT 174.7 bps, ADA 91.6 bps) are mathematically lethal on MT5 CFDs; the banned list (DOGE/DOT/ADA/LINK/NEAR) is confirmed this cycle by NEAR's 2.53R geometry dying at 41.5% friction.
* **Arm, don't stage.** The armed post-sweep trigger is the highest-expectancy instrument the desk holds in a ladder-pinned tape: it converts a hostile geometry into a favourable one by waiting for the fuel to be consumed, at zero carrying cost and zero risk.

---

## §9 — STANDING POSTURE & ARMED TRIGGERS

1. **No new tickets on any of the 24 assets.** All four slots and the +64.55 USD cushion remain unspent.
2. **Ratify the desk's #18925879 cancellation** (second consecutive cycle).
3. **BTC armed post-sweep short** (WATCH, 69.00 in the bracket): trigger = 15 m high ≥ 82,620 (through the [81,600–82,600] belt top) AND close back below 82,450 while session CVD stays negative; invalidation = 15 m close > 83,300 or CVD > +25M; on trigger, re-derive the stop from the realised sweep high + 0.36 ATR against the $25.0M verified buy wall at 81,196, and place the TP to clear the ladder's near edge 81,600 — never inside [80,500–81,600].
4. **Re-scan cadence**: the feed streams a generation every ~1 minute; re-run `Terminal/arena_tournament.py` against the newest generation before any manual staging — the desk mutates orders without notice (it cancelled #18925879 between two consecutive generations).

---

## §10 — ARTIFACTS & PROVENANCE

* Generation: `6a96f85bd4af40bb80306742add1e822` · `docs/telemetry/live_snapshot_latest.json` on `main` (copy used: fetched at 23:0x, sha in `run.json` as `cards_sha256`/snapshot path)
* Cards: `docs/trade_plans/arena_cards/cycle110_20261014T230045Z.json` (15 hypotheses)
* Tournament: `docs/trade_plans/arena_runs/cycle110_20261014T230045Z/{run.json,REPORT.md}` (seed 106)
* Engine: `Terminal/arena_tournament.py` (v2.1 — ladder merge, stop convergence, mandate RR floors) · tests `Tests/Test_Arena_Tournament.py` 39/39
* Skill mirror: `.agent/skills/arena/{SKILL.md,rubric.md,bracket.py}` ⇄ `https://github.com/Jakeschincariol/arena-skill`

**Signed**: Arena Fable orchestrator, Tab 2 — five-seat council, zero decision gates, line-by-line on the cited generation.
