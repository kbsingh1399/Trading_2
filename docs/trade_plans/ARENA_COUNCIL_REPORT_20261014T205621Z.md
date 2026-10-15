# ARENA COUNCIL REPORT — CYCLE 106
### Pure Telemetry & Playbook Analysis · Dual-Engine Screening · Zero Decision Gates
**Orchestrator:** Claude Fable (Arena.ai, Tab 2) · **Broker:** Blueberry Markets SVG LLC, MT5 #5064568
**Report UTC stamp:** 2026-10-14 21:10 UTC · **Machine trace:** `docs/trade_plans/arena_runs/cycle106_20261014T205621Z/{run.json,REPORT.md}`

---

## 0. INGESTION CITATION AND DATA AUTHORITY

| Fact | Value |
|---|---|
| Source file | `docs/telemetry/live_snapshot_latest.json` (4.2 MB) |
| **Generation used** | **`c82b8c85623c4368812f708ca9dd33e8`** |
| **`as_of_utc`** | **2026-10-14 20:56:21 UTC** |
| Prompt-cited generation | `f214c940152c4deaa1d81de871342925` @ 20:21:28 UTC — **superseded, 34 min 53 s older** |
| Git commit backing the snapshot | `2aa42b4` (the only commit touching the file — no `HEAD~1`) |
| `trade_authorization` | **`DENIED_UNVERIFIED_ORDERFLOW`** |
| Data policy | `OBSERVED_ONLY_DATA_POLICY.md`: the git snapshot is a delayed read-only receipt, **not** an order-authorisation feed. Stop/liq bands are `UNVERIFIED_*` landscapes, never execution corridors. Missing coverage ⇒ `ffr: null` + entry veto. |
| Macro blackouts | `blackout_enforcement = DISABLED_BY_OPERATOR` — no candidate may be disqualified for event runway. |
| Mid-drift vs prompt | ETH 2,421.20 (was 2,430.25), BTC 81,725 (was 81,877) — the drift alone moved the live ETH ticket from a 1.43 ATR to a **2.46 ATR** entry. |

**Operational consequence of the drift:** the prompt's arithmetic (1.68 ATR, 15.1 % friction) no longer describes the ticket. Everything below is computed from the on-disk generation.

**Playbook compliance of this report:** dual-engine decoupling (§7.3) preserved — Engine 1 and Engine 2 are judged separately and never collapsed; trend-first hierarchy respected (§2); §7.4 calibrated multi-asset standards used for every wall and friction call; §3.B stop construction from `min_price`/`max_price` of the governing cluster; ≤ 2.0:1 overwhelm ratio enforced; §7.1 ratchet ladder reserved for Mandate 2; macro gates ignored by operator mandate.

**Reproducibility:** every ruling in this report was produced by `Terminal/arena_tournament.py` from the cards in `docs/trade_plans/arena_cards/cycle106_20261014.json` (sha256 `8c965e4510ddf8d5…`) against the snapshot above, seed 106, then re-verified by `Tests/Test_Arena_Tournament.py` (30 tests). Re-running reproduces the identical bracket.

---

## 1. MANDATE 1 — DUAL-ENGINE SCREENING OF ALL 24 ASSETS

### 1.1 The two engines, kept separate

* **Engine 1 — extreme mean reversion:** requires |Z| ≥ 2.0 **with** tape exhaustion **and** ≥ 500 k USD whale backing carrying ≥ 180 s persistence **and** HTF alignment. Filtering the universe on |Z| ≥ 2.0 first is explicitly **forbidden**.
* **Engine 2 — trend pullback:** shelf = EMA stack / VP POC-VAH-VAL / prior day-week auction levels / L2-L3 walls; entry inside the 2.0 ATR proximity bound; SL 0.35–0.50 ATR outside the governing belt (0.50–0.75 ATR per Gate R-1 on pullbacks); TP front-running a magnet by 5–10 bps; friction ≤ 15 % of risk.

### 1.2 Coverage finding that governs every row (read this first)

Only **3 of 24** assets carry live causal indicators (`indicators_source = LIVE_BRIDGE`, 83 session bars, last close 20:45 UTC, age 10.6 min): **BTC, ETH, SP500**. The other **21 assets report `INSUFFICIENT_HISTORY` with 0 bars and 310.6 min stale data** — no Z, no RSI, no ATR, no EMA, no regime. `volume_profile` is populated for BTC and SP500 only; `htf_auction_profiles` are populated for all 24.

**Engine 1 cannot be evaluated for 21 of 24 assets** — not because they failed, but because the telemetry that would feed it is absent. Engine 2 is judged on the shelf/auction/wall geometry that *is* present, and every such row still dies on `ATR_UNAVAILABLE` (an unbounded stop cannot be sized inside a 7.50–14.50 USD envelope).

**Second book-wide finding:** every one of the snapshot's L3 walls — across all 24 assets — is `persistence_status = SINGLE_SAMPLE`, `persist_s = 0.0`, `samples = 1`, `gate_g7_eligible = false`. The retired gate flag may never be used as a filter; lineage must be re-established from the evidence ledgers. Doing that (`docs/trade_plans/ARENA_COUNCIL_EVIDENCE_20261014_*.json`, observed 13:26/14:42/15:09 UTC) confirms the **same wallets** at re-pegged prices, so continuity exists where a wall stayed within 2.0 ATR of its previous price — and it is granted only under that constraint.

### 1.3 The 24-asset table

Entry column uses the maximum permissible Model 2 short entry (**mid + 2.0 ATR**); minimum compliant stop clears the belt adjacent to that entry by 0.35 ATR; "Max R:R" is the asset-level ceiling (best reachable front-runnable magnet ÷ minimum compliant stop). In a `BEARISH` regime longs are banned, so only short-side geometry is scored.

| # | Asset | Mid | Spr bps | Z | RSI | ATR | Regime | Engine 1 | Belt above entry | Min stop (pts) | Best reachable magnet below | **Max R:R** | L3 ≥500k (persist≥180s) | **Final** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | BTCUSD.pi | 81725.0000 | 1.96 | −1.18 | 42.0 | 248.6643 | BEARISH | \|Z\| 1.18 < 2.0 | 81800–82800 = 28.09M | 664.7 | 80700–80800 = 18.73M → 80880.80 | **2.018** | 103 (0) | WATCHLIST |
| 2 | ETHUSD.pi | 2421.2000 | 13.22 | −1.30 | 34.1 | 10.6894 | BEARISH | \|Z\| 1.30 < 2.0 | 2420–2540 = 18.53M | 101.2 | 2380–2390 = 21.92M → 2392.39 | **0.496** | 65 (0) | NO SETUP |
| 3 | SOLUSD.p | 104.1750 | 22.08 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | 104.0–114.0 = 17.57M | — | — | — | 17 (0) | NO SETUP |
| 4 | BNBUSD.p | 727.5000 | 8.25 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | — | — | — | — | 2 (0) | NO SETUP |
| 5 | XRPUSD.pi | 1.3250 | 30.19 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | 1.32–1.43 = 8.87M | — | — | — | 0 (0) | NO SETUP |
| 6 | ADAUSD.p | 0.2281 | 92.09 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | 0.228–0.238 | — | — | — | 0 (0) | NO SETUP |
| 7 | DOGUSD.p | 0.0817 | 256.88 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | — | — | — | — | 0 (0) | NO SETUP |
| 8 | TRXUSD.p | 0.3328 | 27.04 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | — | — | — | — | 0 (0) | NO SETUP |
| 9 | DOTUSD.pi | 1.1385 | 184.45 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | — | — | — | — | 0 (0) | NO SETUP |
| 10 | LNKUSD.p | 12.3900 | 69.41 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | — | — | — | — | 0 (0) | NO SETUP |
| 11 | BCHUSD.p | 268.8000 | 14.88 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | — | — | — | — | 0 (0) | NO SETUP |
| 12 | LTCUSD.pi | 59.4850 | 50.43 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | — | — | — | — | 0 (0) | NO SETUP |
| 13 | AVXUSD.p | 9.9450 | 30.17 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | — | — | — | — | 0 (0) | NO SETUP |
| 14 | NERUSD.p | 4.8145 | 68.54 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | 4.81–4.92 | — | — | — | 0 (0) | NO SETUP |
| 15 | SP500.p | 7717.6950 | 1.13 | −1.13 | 39.5 | 10.0704 | BEARISH | \|Z\| 1.13 < 2.0 | 7720–7820 = 5.34M | 85.7 | 7670–7680 = 0.65M → 7687.68 | **0.585** | 30 (0) | NO SETUP |
| 16 | NAS100.p | 29917.5000 | 0.47 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | 29900–30900 = 4.31M | — | — | — | 14 (0) | NO SETUP |
| 17 | DJ30.p | 51603.9000 | 0.29 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | — | — | — | — | 0 (0) | NO SETUP |
| 18 | GER40.p | 25241.4500 | 1.23 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | — | — | — | — | 0 (0) | NO SETUP |
| 19 | XAUUSD.pi | 4103.7950 | 0.76 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | — | — | — | — | 17 (0) | NO SETUP |
| 20 | XAGUSD.pi | 55.6270 | 10.79 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | 55.6–56.6 | — | — | — | 7 (0) | NO SETUP |
| 21 | USWTI.p | 95.2790 | 3.15 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | — | — | — | — | 0 (0) | NO SETUP |
| 22 | EURUSD.pi | 1.1156 | 0.45 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | — | — | — | — | 1 (0) | NO SETUP |
| 23 | GBPUSD.pi | 1.3190 | 0.61 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | — | — | — | — | 0 (0) | NO SETUP |
| 24 | USDJPY.pi | 158.3490 | 0.63 | — | — | — | INSUFFICIENT_HISTORY | UNDECIDABLE | 158.0–167.0 | — | — | — | 1 (0) | NO SETUP |

**Classification tally: 0 CANDIDATE · 1 WATCHLIST (BTC) · 23 NO SETUP.**

### 1.4 Engine-by-engine narrative for the three instrumented assets

**BTCUSD.pi — Engine 2 WATCHLIST, Engine 1 NO SETUP (|Z| 1.18).**
Mid 81,725; BELOW EMA20 81,779.78 < EMA50 82,215.41 < EMA200 82,857.74 (stack bearish, EMA200 slope −0.187 %/3 h); VWAP 82,679.57 at Z −1.18; RSI 42.03; session CVD **−94.45M** (weekly −82.41M, 24 h −110.85M) with `BEARISH_MOMENTUM` divergence; L2 bid 582 k vs ask 217 k, imbalance **+0.4576** (bid-heavy book into a falling tape); `trapped_traders_signal = BALANCED`; `pullback_geometry`: retrace 0.4421, velocity ratio 0.5236, 11 pullback bars vs 13 impulse bars — a live relief rally, i.e. a textbook *Model 2 shelf*, spoiled only by geometry.
Engine 2 belt: **81,800–82,800 carrying 28.09 M USD of un-swept buy-stop fuel**, contiguous across all ten 100-point bins. The sell-stop ladder below is *also* contiguous (81,700 → 80,000). This two-sided belt is why no BTC card can be staged today (§3.2).

**ETHUSD.pi — Engine 2 NO SETUP, Engine 1 NO SETUP (|Z| 1.30).**
Mid 2,421.20, spread **13.22 bps** (spread/ATR 0.299 — worst ratio of the 24); EMA20 2,430.63 / EMA50 2,450.87 / EMA200 2,486.46; VWAP 2,467.65 σ 35.73; RSI 34.1; session CVD −96.44M (weekly −111.47M); VP POC 2,428.39, VAL 2,411.20; prior-day POC 2,501.43 / VAH 2,528.87; pullback retrace **0.0758** with velocity 0.016 (24 pullback bars vs 5 impulse) — the relief rally has flat-lined. Buy-stop belt **2,420–2,540 = 18.53 M USD**; sell-stop ladder contiguous below. Asset ceiling 0.496 R.

**SP500.p — Engine 2 NO SETUP, Engine 1 NO SETUP (|Z| 1.13).**
Mid 7,717.695, spread 1.13 bps; EMA20 7,721.91 / EMA50 7,749.89 / EMA200 7,787.28; VWAP 7,766.10 σ 42.90; RSI 39.46; `SELLER_AGGRESSION`; L2 imbalance −0.2357; session sell-stop clusters **7,710–7,720 = 271.15 M** and **7,700–7,710 = 4,082.06 M** (flagged as a single-generation outlier, 174× its neighbour, excluded per the > 100× rule); buy-stop belt 7,720–7,820 = 5.34 M; biggest wall BUY @ 7,687 = **38.36 M** (persisted across generations from 13:26 UTC). Asset ceiling 0.585 R.

### 1.5 Qualifying setups with archetype-defense proof

**None. Zero of 24 assets produce a setup that clears the gate set.** Per the mandated output format, the closest candidate (BTC) is shown in full so the desk can see exactly what fails and why:

| Field | Required | BTC best possible short | Verdict |
|---|---|---|---|
| Symbol | — | BTCUSD.pi | — |
| Order | BUY/SELL LIMIT | SELL LIMIT @ 82,222.3 (mid + 2.0 ATR — the extreme edge of the proximity bound) | boundary |
| Lot | 0.01–0.02 → risk 7.50–14.50 USD | 0.02 ⇒ **13.29 USD** | PASS |
| SL | outside belt `[min,max]` + 0.35–0.50 ATR | 82,887.03 = 82,800 (belt max) + 0.35 ATR ⇒ clearance **0.34999 ATR** | **FAIL (by 0.00001 ATR)** |
| SL (alternative) | — | 82,924.03 = belt max + 0.50 ATR ⇒ clearance 0.4988 ATR | PASS |
| TP | front-run a magnet by 5–10 bps | every reachable magnet sits inside the contiguous sell-stop ladder; 80,906.1 lands inside the 80,900–81,000 pool (30.08 M USD) | **FAIL — TP inside magnet** |
| R:R | ≥ 2.0 R | 1.980 R (0.35 ATR stop) / 1.876 R (0.50 ATR stop); ceiling **2.018 R** | **FAIL** |
| Engine | 2 | Model 2 pullback, regime-aligned | PASS |
| Archetype defense | — | **A1** SL clears belt by construction but by 0.00001 ATR — a rounding-level miss, not a defense; **A4** in-range wall defense 128.9 M is verified only through ledger continuity (no live `persist_s`); **A8** entry sits inside 28.09 M of un-swept purchase-side fuel — the exact arrangement that killed ticket #18786372; **A5** 664.7-point stop on a 248.7-point ATR = 2.67 ATR of give; **A6** no reachable magnet pays 2.0 R | **NOT DEFENSIBLE** |

---

## 2. MANDATE 2 — RUNNING-TRADE AUDIT

| Check | Snapshot value | Ruling |
|---|---|---|
| Open positions | `active_positions = []` (0) | **FLAT** |
| Ratchet ladder (§7.1) | nothing to ratchet | **no action** |
| Pending orders | 1 — ticket 18925596 (ETHUSD.pi SELL LIMIT 1.00 @ 2447.50) | handled in Mandate 3 |
| Margin used | 0.00 USD | — |
| Equity / balance | 4,859.55 / 4,859.55 USD | — |
| Hard floor / buffer | 4,775.00 / 4,795.00 USD | cushion **+64.55** over buffer, +84.55 over floor |
| Contingent stress live | 13.875 USD (1.25 × 9.50 + 2.00, broker-valued) | post-joint-stop **4,845.675 USD ≥ 4,795.00** ⇒ `floor_buffer_preserved = true` |
| Capacity | 1/4 joint-fill slots used, 3 available; budget 50.675 USD | +2 max-risk tickets OK; **+3 breaches** (4,785.68 < 4,795) |

**Mandate 2 conclusion: no ratchets, no purges, no partial closes — there are no running trades.** The three-"available-slot" reading in the briefing is arithmetically false: with the ETH pending order retained, only **two** additional max-risk tickets fit the buffer.

---

## 3. MANDATE 3 — PENDING TICKET AND PART CP

### 3.1 Ticket #18925596 — ETHUSD.pi SELL LIMIT 1.00 @ 2447.50, SL 2457.00, TP 2425.00

**RULING: `DELETE` (cancel the resting order). WAIT is contradicted, MODIFY is contradicted.**

The order was audited with the identical gate set a fresh card would face. Fresh generation, six findings — **three of them fatal**:

| # | Finding | Exact arithmetic | Gate |
|---|---|---|---|
| 1 | `ENTRY_TOO_FAR` **(FATAL)** | entry 2,447.50 − mid 2,421.20 = 26.30 = **2.460 ATR** (cap 2.0 ATR ⇒ max entry 2,442.58) | §3.A.3 — 34 minutes of drift broke it |
| 2 | `FRICTION_BUDGET` **(FATAL)** | spread cash 3.20 USD ÷ risk 9.50 USD = **33.68 %** (cap 15 %; minimum stop for 15 % = 21.33 pts = 2.00 ATR) | §7.4 dynamic friction |
| 3 | `SL_INSIDE_SWEEP` **(FATAL)** | SL 2,457.00 sits inside the purchase-side belt **2,450–2,460 carrying 6.19 M USD** (6.19 M = buy-stop clusters + squeeze bands merged; 2,457.2 is itself a 4.17 M USD ask level) | A1 / Gate R-2 |
| 4 | `ENTRY_IN_FUEL` (MAJOR) | entry 2,447.50 sits inside the **2,440–2,450 bin = 4.97 M USD** of un-swept buy-stop fuel — the ticket is positioned to be run over before it fills | A8 |
| 5 | `TP_FRONT_RUN_OFF` (MAJOR) | TP 2,425.00 is **20.66 bps** from the governing magnet edge 2,420 (doctrine: 5–10 bps) | A6 |
| 6 | `NO_PAYABLE_SETUP` (FATAL) | asset ceiling: best reachable target 2,392.39 (front-run of the 2,380–2,390 magnet, 21.92 M) pays **0.496 R** against the 101.2-point minimum compliant stop | A6 |

Against it, and honestly stated: the direction is right (BEARISH regime, session CVD −96.44 M, Z −1.30), the request is passive-sized (limit, not market), risk 9.50 USD is inside the 7.50–14.50 envelope, stressed 13.875 USD keeps the floor intact, and a 14.43 M USD ask wall sits at 2,452.2 below the stop (continuity-verified from the 15:09 UTC ledger at a 14.5-point re-peg). **None of that can rescue a stop that sits inside a 6.19 M USD belt whose lower edge (2,450) is only 2.50 points below the entry** — the ticket is, by construction, an order to be stopped out by a sweep that has not yet happened.

Torn down properly: to clear the belt the stop must reach **2,544** (2,540 belt max + 0.35 ATR). Every repaired variant then fails on payoff — TP 2,412 ⇒ 0.30 R, TP 2,311.5 (inside the 2,310–2,320 pool) ⇒ 1.43 R, and the TP that would force 2.20 R (2,219.2) sits **60 points below the outer edge of the 108.45 M USD 2,300–2,320 cascade cluster** — a wish, not a front-run. **Widening the stop to survive the belt destroys the payoff; narrowing it to pay the payoff guarantees the sweep-out.**

*Supporting evidence from prior cycles (context, not authority): ticket **#18786372** was stopped −9.16 USD with the identical signature — SL inside a sweep belt against unabsorbed opposite-side fuel. Archetype **A1/A8 must not be re-registered a third time.***

### 3.2 PART CP — "Should we also stage a BTCUSD.pi SELL LIMIT @ 82,190 (SL 82,420, TP 81,660, 2.30R)?"

**RULING: `DO NOT STAGE`. The 2.30 R on the card is an artefact of an illegal stop.** Three independent fatal defects:

1. **`SL_INSIDE_SWEEP` (FATAL).** SL 82,420 sits **inside the contiguous purchase-side belt 81,800–82,800 = 28.09 M USD** (the 82,400–82,500 bin alone carries 1.58 M; the 82,200–82,300 bin 3.84 M). For a short, the stop must clear the *outer* edge: > 82,800 + 0.35 ATR = **82,887**. This is the same defect as the live ETH ticket and the same defect as the autopsy ticket — a third registration of A1 is not permitted.
2. **`NO_PAYABLE_SETUP` (FATAL).** Repairing the stop does not save the card, it kills it: with SL 82,887 (0.35 ATR clearance) the best reachable front-runnable target pays **1.980 R**; with SL 82,924 (0.50 ATR) it pays **1.876 R**. **BTC's asset ceiling in this generation is 2.018 R** — measured at the extreme `mid + 2.0 ATR` perimeter (82,222.3), not at the card's 82,190, and with a 664.7-point stop that is itself 0.00001 ATR short of the 0.35 ATR floor. The 2.30 R quoted *requires* the illegal 230-point stop.
3. **TP placement.** 81,660 sits inside the **81,600–81,700 sell-stop bin** (and the deeper 80,900–81,000 pool carries 30.08 M USD), i.e. inside a magnet rather than front-running one. Moving the TP to a true 7.5 bps front-run (80,906.1) puts it inside the 80,900–81,000 pool; front-running the *top* of the contiguous sell-stop ladder (≈81,760) pays only ≈0.70 R. There is no TP on the board that both front-runs and pays.

Supporting facts (they do not change the ruling, they explain why the drop is tempting): BTC is the only instrument with a live regime, it is BEARISH, session CVD is −94.45 M, the 81,196 BUY wall (**25.00 M USD**, wallet `0xf517639a…`) is literally the same wall observed at 15:09 UTC — the single best-documented defense in the book — and 2.30 R above it looked like free money. It is not: the wall is 529 points *below* mid and the belt is *above* the entry. The correct use of that wall is as the **landing zone for a post-sweep short**, not as shelter for a pre-sweep one.

**Forward action (armed, not staged):** WATCH card `btc_armed_post_sweep_short` — *if* BTC prints a 15 m high ≥ 82,450 and closes back below 82,300 with session CVD still negative, the belt above has been consumed; re-derive the stop from the realised sweep high + 0.35 ATR and the ticket becomes payable (the 81,196 wall and the 80,900–81,000 pool are then the front-runnable targets). Invalidation: 15 m close above 83,300, or CVD flipping above +25 M. **No resting order is placed until the trigger prints.**

---

## 4. ARENA TOURNAMENT — 14 COMPETING HYPOTHESES, 5 SEATS, ONE BRACKET

**Methodology:** `.agent/skills/arena/{SKILL.md,rubric.md}` applied as a single-elimination bracket; rubric weights **correctness 30 / completeness 25 / specificity 15 / robustness 20 / clarity 10**; **the fatal rule** (a card contradicted by the snapshot cannot win a match against one that is not) is applied before totals. Executed deterministically by `Terminal/arena_tournament.py` (seed 106) so the ruling is reproducible, not narrated. *Runtime disclosure: the installed skill describes a 100-agent bracket; this cycle ran the desk's five mandated seats as the competitors, with the bracket itself executed mechanically — a single-assistant adaptation, not 100 agents.*

**Seats (each interrogates independently with its own evidence before synthesis):** ① Orderflow & Microstructure ② Structural Price Action ③ Liquidation & Stop Forensic ④ Macro Risk & Portfolio Governor ⑤ Adversarial Pre-Mortem Red Team.

### 4.1 Scoreboard (rubric total / 100)

| Card | Action | Fatal? | Purchase-side hazard | Total | Verdict |
|---|---|---|---|---|---|
| `desk_stand_aside_cycle106` | STAND_ASIDE | no | — | **71.50** | **BRACKET WINNER** |
| `btc_armed_post_sweep_short` | WATCH (armed) | no | — | 69.00 | runs as the forward protocol |
| `eth_delete_18925596` | DELETE | no | — | 67.31 | VERIFIED — delete justified |
| `btc_stage_82190_argon` | STAGE (peer card) | YES | SL_INSIDE_SWEEP, ENTRY_IN_FUEL | 53.58 | CONTRADICTED |
| `eth_modify_r3_forced_rr` | MODIFY | YES | — | 52.58 | CONTRADICTED |
| `eth_hold_18925596` | HOLD | YES | — | 52.29 | CONTRADICTED |
| `btc_stage_argon_tp_fixed` | STAGE | YES | SL_INSIDE_SWEEP, ENTRY_IN_FUEL | 51.10 | CONTRADICTED |
| `btc_stage_belt_cleared` | STAGE | YES | ENTRY_IN_FUEL | 49.73 | CONTRADICTED |
| `eth_modify_safe_stop_near_tp` / `_deep_tp` | MODIFY | YES | — | 48.74 | CONTRADICTED |
| `sp500_stage_short_7738` | STAGE | YES | ENTRY_IN_FUEL | 48.18 | CONTRADICTED |
| `desk_batch_3x_max_risk` | STAGE_BATCH ×3 | YES | ENTRY_IN_FUEL | 48.18 | CONTRADICTED (buffer breach) |
| `nas100_stage_short_30000` | STAGE | YES | SL_INSIDE_SWEEP, ENTRY_IN_FUEL, COUNTER_CVD | 48.00 | CONTRADICTED |
| `gold_stage_short_4115` | STAGE | YES | SL_INSIDE_SWEEP, BUNKER_WALL_THIN | 48.00 | CONTRADICTED |

### 4.2 Bracket path (four rounds)

* **R1** `eth_delete` beats `btc_argon`; `r3_forced_rr` beats `near_tp`; `deep_tp` beats `nas100`; `stand_aside` beats `argon_tp_fixed`; `armed_post_sweep` beats `gold`; `eth_hold` beats `sp500`; `belt_cleared` beats `batch_3x`; `eth_delete`… (byes as seeded).
* **R2** `eth_delete` beats `r3_forced_rr`; `stand_aside` beats `deep_tp`; `armed_post_sweep` beats `eth_hold`.
* **R3** `stand_aside` beats `eth_delete` **71.50 – 67.31**; `armed_post_sweep` beats `belt_cleared`.
* **R4 FINAL** `desk_stand_aside_cycle106` beats `btc_armed_post_sweep_short` **71.50 – 69.00**.

### 4.3 The five seats on the winner and on the rejected peer card

*Stand-aside (all five: NO OBJECTION)* — ① "flow coverage 3/24 assets report taker/tick CVD" ② "regime coverage 3/24 assets carry a trend regime" ③ "verified wall defense across the book: **0** walls with persist ≥ 180 s" ④ "balance 4,859.55 USD; contingent stress 13.875 USD; post-joint-stop 4,845.675 vs 4,795.00 buffer; joint-fill slots 1/4; causal coverage 3/24" ⑤ "worst case: every card in the universe was probed by the full gate set — none survived."

*Argon BTC card 53.58* — ① NO OBJECTION (CVD −94.45 M is with the short, L2 +0.4576 bid-heavy but BALANCED trap) ② **CONTRADICTS** (entry belt 81,800–82,800; mid below the whole EMA stack) ③ **CONTRADICTS** ("28.09 M USD of un-swept fuel at the entry; 28.09 M in the SL belt") ④ NO OBJECTION (friction 6.96 %, stress 16.38 USD, post-stop 4,829.30) ⑤ **CONTRADICTS** ("best reachable 5.69 R vs asset ceiling 1.88 R; entry 1.87 ATR from mid; 6 fuel belts overhead").

**Synthesis (Fable, orchestrator):** the tournament's two non-contradicted *ticket-level* answers are **DELETE** (67.31, verified) and **no new ticket**; the winner is the portfolio card because it also survives the adversarial seat on capacity, coverage and floor arithmetic. The three cards are one policy, not three: **cancel the stale ETH limit, stage nothing new, arm the post-sweep trigger.**

---

## 5. EXECUTION SUMMARY (PASSIVE LIMIT ORDERS ONLY)

| # | Action | Instrument | Details | Risk | Archetypes countered |
|---|---|---|---|---|---|
| **E1** | **DELETE pending order** | ETHUSD.pi | Cancel ticket **#18925596** (SELL LIMIT 1.00 @ 2447.50, SL 2457.00, TP 2425.00). Frees 13.875 USD of stressed exposure and the last-used joint-fill slot. | 0 | A1 (SL in 6.19 M belt), A8 (entry in 4.97 M fuel), A5, A6, A7 (33.68 % friction) |
| **E2** | **NO NEW TICKETS** | all 24 | 0 of 24 assets produce a qualifying setup; BTC is WATCHLIST (ceiling 2.018 R), ETH 0.496 R, SP500 0.585 R, 21 assets undecidable without causal indicators. | 0 | A2 (no counter-trend fade), A3, A4 (0 verified walls), A6 (no payable geometry) |
| **E3** | **ARM (do not stage)** | BTCUSD.pi | WATCH: 15 m high ≥ 82,450 **and** close back below 82,300 with CVD still negative ⇒ re-derive SL from the realised sweep high + 0.35 ATR against the 81,196 (25.00 M) wall / 80,900–81,000 (30.08 M) pool. Invalidation: 15 m close > 83,300 or CVD > +25 M. | 0 until armed | A1, A5, A8 — enters only after the belt is consumed |
| **E4** | **BUDGET CAP** | portfolio | With the pending retained only 2 max-risk slots exist; after E1 the budget returns to 64.55 USD ⇒ 3 slots. Three simultaneous max-risk tickets must never be opened while a pending order is live. | 0 | A5 (floor defense) |

**Post-execution state (modelled):** balance/equity 4,859.55 USD · positions 0 · orders 0 · stressed exposure 0.00 USD · all 4 joint-fill slots free · cushion +64.55 USD over the 4,795.00 buffer, +84.55 USD over the 4,775.00 hard floor.

---

## 6. QUANTITATIVE TELEMETRY AUDIT (what the book does and does not support)

**6.1 Schema gaps that cap alpha today**

| Missing field | Consequence | Workaround used |
|---|---|---|
| Multi-level OFI (only a single `order_flow_imbalance_ofi` scalar) | Cannot distinguish a shelf from a vacuum; no depth-weighted pressure | L2 imbalance + `hazard_runs` belt counting |
| Micro-price vs mid | No lead indicator for the next 1–5 m; CVD is a lagging proxy | Session CVD + `pullback_geometry.velocity_ratio` |
| Queue-position decay curve | Fill-probability at a limit is unobservable; queue position unknowable | Conservative: assume worst queue, treat passive fill as optional |
| Taker aggressor ratio by 1m/5m/15m/30m (crypto) | Crypto carries only `session_tick_cvd` + 15 m delta; TradFi has 5 m/15 m tick CVD | 15 m deltas + `BEARISH_MOMENTUM`/`BULLISH_ABSORPTION` labels |
| Footprint delta absorption score | No per-price absorption map; "exhaustion" is inferred, not measured | Stop-cluster binaries + trapped-trader flags |
| Causal indicators for 21/24 assets | Engine 1 mathematically unavailable off the top-3 | Engine 2 geometry judged anyway; all still fail ATR gating |

**6.2 How a payable 2.0–2.5 R intraday sweep setup must be constructed here**
1. **Wait for the belt to be consumed** (E3). The operator's sweep doctrine and the autopsy record agree: entering before the purchase-side belt is swept is A8 by definition.
2. Entry at the **2.0 ATR perimeter**, never beyond — 2.46 ATR killed the live ticket.
3. SL = realised sweep high + **0.35–0.50 ATR** (Gate R-1), always measured from the belt's *outer* `max_price`.
4. TP = **5–10 bps in front of a ≥ 0.50 M USD magnet**, never inside a 100-point bin (BTC's 81,660 failed exactly here).
5. Size so that `spread_cash / risk ≤ 15 %` — this is the binding constraint on 8 instruments (DOGE 21.00, ADA 10.50, TRX 9.00, XRP 4.00, NEAR 3.30, LTC 3.00, XAG 3.00, DOT/LINK historically) against a 2.175 USD maximum.

**6.3 Dynamic SL-buffer / TP-front-run calibration (closed form used)**

```
min_stop_points = (belt_max_above_entry − entry) + 0.35 × ATR      # short
sl_clearance_atr = (SL − governing_belt_max) / ATR                 # must be 0.35–0.50
tp_front_run_bps = |TP − governing_magnet_edge| / edge × 10 000     # must be 5–10
friction_pct     = spread_cash ÷ (stop_points × contract × lots) × 100   # ≤ 15
max_achievable_rr = best_reachable_reward ÷ min_stop_points          # asset ceiling, ≥ 2.0
post_stop_equity = balance − contingent_stress − (1.25 × risk + 2.00) × tickets ≥ 4,795
```
Calibration results today: BTC 1.980–2.018 R (boundary), SP500 0.585 R, ETH 0.496 R ⇒ **no asset clears the 2.0 R floor in this generation.**

**6.4 Macro:** blackout enforcement is `DISABLED_BY_OPERATOR`; no candidate was disqualified, delayed or purged for the 15 Oct 02:55 UTC Fed-Bowman window. Fear & Greed 62 (Greed); Coinbase premium −14.16 bps; ETF flows not yet reported; funding BTC +0.29 / ETH +0.25 bps.

**6.5 Maximum net alpha under the 15 % friction rule (Blueberry MT5 CFDs):** with the current spread book, BTC (1.96 bps) and SP500 (1.13 bps) cost only 0.16 and 0.09 USD of spread at minimum lot against the 2.175 USD allowance, so their stops are never friction-bound; ETH (13.22 bps) needs a stop of **≥ 21.33 points (2.00 ATR)** to stay inside 15 %; and **USDJPY (10.00 USD), XRP (4.00), ADA (10.50), DOGE (21.00), TRX (9.00), NEAR (3.30), LTC (3.00) and XAG (3.00) are excluded outright at minimum lot.** Under the 2.0 R floor with a compliant stop, the *maximum realisable* R in this generation is **2.018 R on BTC (≈ 26.3 USD of reward at 0.02 lots)**, and it is only reachable at the extreme perimeter — 0.02 R above the floor. **The honest ceiling for today's book is: no payable intermediate-horizon setup.**

---

## 7. GOVERNANCE AND FINAL RULING

* **Account:** Blueberry Markets SVG LLC, MT5 **#5064568** · balance = equity **4,859.55 USD** · margin used 0.00.
* **Constraints honoured:** risk 7.50–14.50 USD/ticket · stressed loss 1.25 × nominal + 2.00 USD/ticket · post-stop equity ≥ 4,795.00 (buffer) and ≥ 4,775.00 (hard floor) · ≤ 4 joint-fill slots · passive limit orders only · zero registration/repetition of prior loss archetypes.
* **Final ruling:** **(1)** cancel pending ticket #18925596; **(2)** stage no new tickets on any of the 24 assets; **(3)** hold the post-sweep BTC trigger armed per E3; **(4)** keep the three-new-ticket cap and treat capacity as two slots while any pending order lives.
* **Self-critical disclosure (adversarial seat):** the strongest counter-argument is that stand-aside forfeits a legitimately bearish tape. It is rejected on arithmetic: the entry, the stop *and* the payoff are each individually disqualifying, and the floor-protected account gains nothing by paying 18.62 USD of stressed exposure for a geometry whose best outcome is 1.98 R. A second caveat: the engine's "TP must not sit inside a ≥ 0.5 M pool" rule is strict — under a looser "front-run the specific bin" reading the BTC card reaches 2.30 R gross, but its stop remains inside a 28.09 M belt, so the ruling does not change.
* **Runtime disclosure:** decisive layer is deterministic and reproducible; the modelled stress is not immunity to gap risk, and `trade_authorization = DENIED_UNVERIFIED_ORDERFLOW` means the venue itself does not certify this flow as executable.

**Machine-readable trace:** `docs/trade_plans/arena_runs/cycle106_20261014T205621Z/run.json` (per-card findings, metrics, persona scores, bracket) · human report `…/REPORT.md` · cards `docs/trade_plans/arena_cards/cycle106_20261014.json` · engine `Terminal/arena_tournament.py` · tests `Tests/Test_Arena_Tournament.py` (30/30 passing).
