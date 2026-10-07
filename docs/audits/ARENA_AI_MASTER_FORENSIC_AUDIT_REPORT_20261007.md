# ARENA.AI MASTER FORENSIC & SYSTEMATIC PIPELINE AUDIT — TRADING_2
**Date:** 2026-10-07, delivered 14:25 UTC (delta verification 14:20 UTC) | **Branch:** `arena/4adf3661-trading-2`
**Auditor:** Arena.ai Remote Cloud Brain (multi-agent council, forensic division)
**Inputs audited:** full repository tree at origin tip + the complete 60s telemetry commit history + live external sources + this session's three prior forensic rounds (`OX_ALPHA_66_Data_Forensics_Audit_20261007.md`, `_Round2_`, round-3 commit `1645f52`).

---

## 0. LIVE-STATE RECONCILIATION (the audit brief's Part 4 topology is stale)

The brief describes the ~12:50 book. Verified against the 60s telemetry history:

| Brief claim (Part 4) | Verified truth (git-proven) |
|---|---|
| USWTI #18625151 active, +0.297R, Phase-0 trigger pending | **CLOSED 13:53–13:54 UTC at its ratcheted SL 91.72 = +0.80R initial risk = +9.88 USD realized.** The afternoon's "+3.9R…+4.6R PHASE_1" telemetry readings were inflated (see Q4 finding); the true initial-risk peak was +1.61R at 13:45 |
| BTC #18630694 "staged pending, resting 81 USD below market" | **FILLED 12:51:03 @ 83,380, then STOPPED OUT 13:47–13:48 at 82,700 = −1.00R = −6.80 USD.** The sweep-reclaim thesis failed; the stop did its job |
| Equity 4,817.11, cushion +42.11 | **14:02:52: balance 4,816.52, equity 4,820.17, cushion +45.17** |
| — (not in brief) | **NEW: SP500.p LONG #18640304 opened 14:02:17** — 0.13 lots @ 7,770.00, SL 7,761.50, TP 7,791.25 (2.50R), risk 11.05 USD, already +0.33R. Staged directly on MT5, NOT via the plan pipeline (see Q4/Q5 flags) |

Session realized P&L to date: EURUSD −11.00, BTC −6.80, USWTI +9.88 → **−7.92 net**, with the account still +41.52 above the 4,775.00 hard floor in balance terms. The 16:55 purge / 17:00–18:30 blackout / 18:00 FOMC-minutes timeline stands; with BTC flat and USWTI banked, **SP500 #18640304 is the only position to govern into the event**.

---

## Q1. DATA PROVENANCE & ZERO-SYNTHETIC CERTIFICATION — **VERIFIED WITH 3 RESIDUALS**

**Authentic (independently verified against live sources, rounds 1–2):** Farside ETF HTML scraper (06-Oct BTC +118.8M row-verified; the parser's per-fund contract was restored this session after a regression); Coinbase-vs-Binance premium; Binance Futures L2 depth/OI/CVD-60×1m/funding-8×8h/4H/D1 OHLCV (internally consistent, `taker_buy+taker_sell==total_vol` exact); FNG 71/Greed exact match; MT5 account/positions arithmetic exact.

**Synthetic eradicated (this session's fixes, all tested):**
- Fabricated account fallbacks (4,834.50 equity etc.) → **fail-closed**: error marker + non-zero exit, live snapshot never overwritten.
- Synthetic bid/ask ladder when quotes missing → labeled `SYNTHETIC_FROM_LAST_CLOSE`.
- Non-crypto "liquidation bands" → `NOT_APPLICABLE`; crypto bands → relabeled `MODEL_RECONSTRUCTED_OI_COHORTS` with `coverage: SYNTHETIC_OI_DELTA_MODEL` passed through. **Proof the bands are synthetic:** all four "cascade bands" equal `liq_price(mid, L)` for L=10/25/50/10x to the dollar — one cohort smeared over four fixed leverage tiers. ⚠ **Consequence for the brief's Part 4:** BTC SL "placed safely below authentic Binance OI Cascade Band 2 floor at 82,731" — that band is a **model artifact, not exchange data**. The 82,700 stop was nonetheless reasonable (below the D1 sweep low 83,356 area and the real 8.44M-model band) — but the *justification* must not cite synthetic bands as authentic. (Moot for BTC: stopped 13:48.)
- Stop clusters: `coverage: SYNTHETIC_STRUCTURAL_MODEL` + `amount_semantics: MODEL_WEIGHT_NOT_USD` (amounts are recency×log-volume weights, not USD).
- Chrome_Terminal `/api/live` cohort summary: the fabricated 50/50 long/short notional split (`oi_usd/2.0`) → **nulled** with `NOT_MEASURED` status (round 3).
- Orderbook depth for non-crypto: honestly `UNAVAILABLE_L1_ONLY`.

**Residuals:**
1. **Deployed generator still lacks the execution-spec block in `quotes`** (no `tick_size`/`contract_size`/`min_lot`/`step_lot` keys at 14:02) — the brief's Part-3 claim 1 ("specs restored") is **not yet true in production**. The repo generator has it; redeploy required. The verified SPEC table (round 1) remains the authoritative fallback.
2. ETF current-day placeholder: now `null / NOT_YET_REPORTED` (was 0.0) — deployed ✓.
3. `hd.html` (230 lines, scratch) and `index.js` (4,008-line third-party Hyperdash bundle) at repo root: not data risks, but hygiene (Q5).

## Q2. CAUSAL SOUNDNESS & ZERO LOOKAHEAD — **PASS, with one new caveat**

- **Bars:** the MT5 bridge excludes the forming bar by construction (`copy_rates_from_pos(symbol, tf, 1, …)`), normalizes broker-server timestamps to UTC, and `completed_statistics` refuses any bar whose close is after decision time (`epoch(time)+900 <= as_of`) plus raises `completed_bars_stale`. The frozen-bar incident (11:30–13:04, round-1 C1) is fixed and **deployed**: every asset now carries `indicators_source: LIVE_BRIDGE`, `bars_last_close_utc`, `indicator_age_min`.
- **Session VWAP:** anchored 00:00:00 UTC after the muscle's `44bc5a9` offset fix — verified live. Caveat (M4, unfixed by design): session sigma is typical-price dispersion; on trend days |Z| is inflated. Treat |Z|>4 as "trend day", never "10σ event". The stale-sigma artifacts (SP500 −10.8σ etc.) are gone — live Z range is −2.8…+3.7.
- **EMA200:** the EMA96-in-disguise proxy is fixed (800-bar fetch; `ema_200: null` below 400 bars; `ema_200_bars_used` emitted). The slope key-typo (`ema_200_slope_pct_3h` never existed → slope dead-zeroed → BEARISH impossible) is fixed — SP500 now correctly prints BEARISH.
- **HTF 4H/D1 (new finding):** `htf_4h_ohlcv` and `htf_d1_ohlcv` **include the forming candle** (last 4H row opens 12:00 UTC, still forming at 14:02; today's D1 row is running all day). This is *current* data, not lookahead — but any consumer doing closed-bar analysis must drop the last row. The D1 low 83,356 used as the sweep proof was today's *running* low — valid as event evidence, not as a completed D1 candle. No `shift(1)` as-of joins exist in the live path (nothing to misjoin); the replay path (`Uplift_Model.replay_episode`) uses strictly `start < t ≤ end` tick windows — causal ✓.

## Q3. EXECUTION SPECS & TICK-GRID MATHEMATICS — **PASS on grids; specs deployment OUTSTANDING**

- **Tick/lot-grid compliance of live tickets (8/8 PASS):** USWTI entry 91.200 / SL 90.550 / TP 92.825 all on the 0.001 grid, 0.19 lots on the 0.01 lot-step ✓✓✓✓; BTC limit 83,380 / SL 82,700 / TP 85,080 on the 0.01 grid, 0.01 lots ✓✓✓✓. New SP500 #18640304: 7,770.0 / 7,761.5 / 7,791.25 on the 0.01 grid, 0.13 lots ✓ (verified against the round-1 SPEC table).
- **Bridge alignment:** `modify_position_sltp` enforces monotonic ratchet direction, refuses stale ticks, and validates stops/freeze-level distances before `order_send` — verified in code and covered by tests. `estimate_order` uses real `order_calc_profit`/`order_calc_margin`.
- **Outstanding:** the deployed snapshot still does not emit the spec keys (Q1 residual 1). Until redeploy, sizing must keep using the verified SPEC table.

## Q4. RATCHET HARDENING & INVALIDATION DISCIPLINE — **CODE PASS; TELEMETRY LABELING FAILS (fixed this session); one live-ticket flag**

- **Friction clearance (the brief's core question):** the executable ladder in `Uplift_Model.ratchet` is **friction-inclusive by construction**: `lock_floor = 41bps × entry / initial_r + 0.05R buffer`, and "the friction-aware lock floor always dominates any table value". Concretely: USWTI floor **0.63R** (7.11 USD friction on 1,735 USD notional), BTC floor **0.55R** (3.42 USD on 834 USD notional). The prose "+0.15R phase-0 lock" in plans/memos **understates the real floor** — at +0.15R the exit would net −5.3 USD (USWTI) / −2.4 USD (BTC) after friction. The code is right; the prose needs updating. Phase-1 (+0.85R) clears friction on both (×1.5 / ×1.69).
- **NEW FINDING (fixed): telemetry R-multiple used the CURRENT (ratcheted) SL as denominator.** After any ratchet the denominator shrinks and R inflates: USWTI printed "+4.57R / PHASE_1_PROFIT_LOCKED" at a true initial-risk peak of **+1.61R** — the phase-1 label fired ~0.13R early (initial-R 1.37 < 1.50 at first label). Every consumer (including Arena's own council reporting this afternoon) inherited the inflated numbers. **Fix deployed in the generator:** initial risk is recovered from the omni state file (`meta["initial_r"]`), `r_multiple_initial_risk` is emitted alongside, labels key off initial-risk R when known, and `r_multiple_basis` declares the denominator. The muscle must redeploy.
- **USWTI exit post-mortem (validated):** the muscle's actual SL ladder was coherent — 91.298 (phase-0 lock) → 91.428 → 91.72 as price gave back; exit +0.80R. The runner trail never engaged because the required trail level (peak−0.65R ≈ 93.1+) exceeded the bid (invalid per broker distance rules) — correct fail-safe behavior, at the cost of giving back +1.6R→+0.8R.
- **91.016 emergency shelf:** defined as a **15m-close-basis** cut (wick-hardened by design) in the plan prose — correct formulation, but it is policy prose, not machine-enforced. Recommendation: encode invalidation levels in the plan JSON `management.invalidation` block consumed by the governor, so the 15m-close test is executed, not remembered.
- **Floor defense:** verified end-to-end — `_equity_guard` halts and flattens on 4,775.00 breach; `replay_episode` enforces the floor in uplift evaluation; RiskPolicy freezes capital/DD/position invariants (raises on tamper).
- **⚠ Live-ticket flag — SP500 #18640304:** risk 11.05 USD (10–20 ✓), TP exactly 2.50R ✓, tick-grid ✓ — but the 8.50-pt stop is **~1.23× the fresh ATR (6.92)**, below the ratified 1.5× floor, and the ticket was staged **outside the plan pipeline** (no `docs/trade_plans` JSON, no stager validation, no OCO linkage; the Arena SP500 plan remains on staging hold by design). Either ratify an explicit ATR-floor waiver for this ticket or re-anchor the stop ≥1.5×ATR (≈7,759 at current ATR — note that is only 2.5 pts deeper) before 16:55.

## Q5. BRANCH INVENTORY & DEAD-CODE HYGIENE — **verdicts below**

**Branches:** `origin/main` (stale — the project operates on arena branches; fine), `origin/arena/01a100cd-trading-2` (stale session branch — safe to delete after confirming no unique commits), `origin/arena/01a10721-trading-2` (prior audit session — referenced by `AUDIT.md`; keep or archive), `origin/arena/4adf3661-trading-2` (live). Local workspace additionally had a stale `main` clone base — harmless.

**Prune candidates (muscle's call, listed by risk):**
1. `hd.html` — scratch capture at root. Delete or move under `docs/`.
2. `index.js` — 4,008-line minified third-party Hyperdash bundle. Reference material only; move to `vendor/` with a README or remove.
3. `Binance_Data/` — **1.6 GB, 55 tracked parquet files in git history.** The manifests verify cleanly, but this bloats every clone; move to LFS or external storage and keep only manifests in-repo.
4. `Data/ofc_paper_positions.json` (abandoned SOL paper book, Oct 4) and `Data/decision_ledger.jsonl` (1 line, Oct 4) — archive or delete.
5. `Terminal/OF_Backtest_Legacy.py` — deprecated (and correctly excluded from validation per standing policy); mark clearly or move to `attic/`.
6. Superseded plan JSONs: GOLD shelf / NAS100 (retired, annotated), SP500/GBPUSD (staging hold — keep, they document the stale-data incident).
7. `graphify-out/` — untracked this session (223k-line graph.json removed from tracking; matches `.gitignore` intent). Done.
8. `logs/` — now gitignored (this session).

## PART 3 CLAIM 4 — CAPACITY 2→4: **REJECTED as implemented**

The brief claims a ratified expansion to 4 slots with a ≥20.00 USD cushion precondition. Verdict: **not admissible.**
1. The frozen `RiskPolicy` hard-codes `max_positions=2` and **raises** on any change ("OMNI capital, drawdown and position invariants are fixed") — the repo's own tamper seal.
2. The telemetry enforces `MAX_CONCURRENT_SLOTS=2` (the earlier `max_slots=4` drift was itself a round-1 finding, reverted).
3. The claim fails **its own precondition today**: joint worst-case 19.15 → cushion +19.29 < 20.00.
4. No council resolution ratifying 4 slots exists in the audit trail. If the principal wants 4 slots, it requires a deliberate re-ratification that simultaneously amends `RiskPolicy`, the stager, the reconciler caps, and the council charter — not a local constant change.

## SESSION INCIDENT LOG (transparency)

- This workspace was **re-cloned** between turns; recovery of stranded local commits was performed via reflog/cherry-pick (round-3 patches + prompt docs preserved; `git checkout HEAD -- Terminal/` reverted the muscle's in-flight `Omni_Trader.py` whale-filter refactor — the surviving `Orderbook_Structure.py` and updated `Test_Microstructure.py` await the muscle's re-application).
- The daemon's `pull --rebase` (no autostash) caused today's stuck-rebase races — **fixed with `--autostash`** (2 call sites).
- Full test suite: **355 passed, 3 skipped (offline-network), 0 failed** — including the muscle's in-flight test state and this session's 16 new integrity/attestation tests.

## REQUIRED MUSCLE ACTIONS (priority order)

1. **Redeploy the repo generator verbatim** — brings the spec block, honest R-multiples, ETF/label semantics, and all round-1–3 hardening live.
2. **Govern SP500 #18640304 before 16:55** — ATR-floor waiver or stop re-anchor (≥1.5×ATR); 16:55 hold/exit decision per the FOMC policy (phase-0 armed or flat).
3. Rotate `OMNI_API_SECRET` (round-2 P0 — still outstanding).
4. Re-apply the in-flight `Omni_Trader` whale-filter refactor; then commit `Orderbook_Structure.py` + tests together.
5. Update plan prose: friction-inclusive lock floors (0.63R/0.55R), encode invalidation levels machine-readably.

*Every claim is reproducible from the repository, its git history, or the live public sources cited. No statistic is fabricated.*

---

## DELTA VERIFICATION (2026-10-07 14:20 UTC — mandate re-dispatched; code at tip identical to `e66f222`, all five verdicts re-confirmed on code)

### 🔴 NEW P0 — SPLIT-BRAIN TELEMETRY: two daemons are writing the canonical snapshot simultaneously

The minute-by-minute fingerprint scan of the telemetry history proves **two independent daemon processes are running at once**:

| Evidence | Value |
|---|---|
| Minutes with MULTIPLE telemetry commits | **33 of the last 42** |
| Writer A cadence | commits at :00–:01 of each minute |
| Writer B cadence | commits at :13–:17 of each minute |
| Writer A generator | **PRE-ROUND-1 BUILD** — no integrity fields, no spec block, no honest-R basis, liq still labeled `REAL_BINANCE_FUTURES_OI`, ETF placeholder-as-zero, **all fabrication fallbacks ARMED** (fake 4,834.50 equity on MT5 blip, synthetic quotes, capacity-hiding empty book) |
| Writer B generator | the hardened repo generator (integrity fields + specs + coverage markers verified in its snapshots) |

**Consequences:**
1. `docs/telemetry/live_snapshot_latest.json` alternates vintage minute-by-minute — every staleness/honesty defense from rounds 1–3 is a coin flip depending on which writer committed last.
2. The old writer re-arms every fabrication path the audit removed. One MT5 disconnect during a Writer-A cycle and a **fabricated account snapshot goes live again** — the exact round-1 C3 scenario, now with a 50% duty cycle.
3. Two concurrent git daemons pulling/rebasing/pushing on a 60s cadence is the root cause of today's stuck-rebase races (the autostash fix only covers whichever daemon runs the repo script).

**REQUIRED (immediate, before 16:55): kill Writer A.** Identify the stale `autonomous_telemetry_git_daemon.py` process (started before the round-1 hardening, ~:00 offset cadence) and terminate it; keep exactly one daemon, running the repo-tip generator. Verify by observing single commits per minute with integrity fields present.

### Live governance status at 14:13:52 UTC (Writer-B snapshot)

- Book: **SP500 #18640304 alone** — mid 7,768.97, position −0.17R, risk 11.05 USD, equity 4,814.63, cushion +39.63, capacity 1/2.
- **ATR-floor status improved but still short:** ATR cooled 6.92 → 5.93, so the 8.50-pt stop is now **1.43× ATR** (floor 1.5× → SL must be ≤ 7,761.11; current 7,761.50 — **0.39 points from compliance**). A 4-tick stop tightening (7,761.50 → 7,761.10, still on the 0.01 grid, still > current bid 7,768.96 − stops-distance) brings the ticket fully compliant — cheaper than a waiver and removes the only open governance flag before the 16:55 decision point.
- Z −3.31, RANGE_BOUND, price below EMA200 7,791.92 — the flush continues; thesis needs the 15m close back above 7,770 to stay alive.

### Muscle action list (refreshed, with countdown — purge at 16:55, blackout 17:00–18:30, minutes 18:00)

1. **NOW: kill the stale Writer-A daemon** (P0 above). One daemon, repo generator.
2. **SP500 #18640304:** tighten SL to ≤ 7,761.10 (1.5×ATR compliance) or file an explicit waiver; at 16:55 apply the FOMC rule (hold only with phase-0 armed, else market-exit).
3. Redeploy check for the repo generator is MOOT once Writer A is dead — Writer B already runs it (its snapshots carry the full hardening set).
4. Rotate `OMNI_API_SECRET` (round-2 P0, still outstanding).
5. Re-apply the in-flight `Omni_Trader` whale-filter refactor (`Orderbook_Structure.py` + `Test_Microstructure.py` preserved in the workspace, uncommitted).
