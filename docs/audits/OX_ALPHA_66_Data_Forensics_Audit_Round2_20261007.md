# OX_ALPHA_66 — Full-Repository Forensics Audit, ROUND 2 (2026-10-07, ~13:55 UTC)

**Mandate (principal, repeated):** "Deep audit, debugging, forensics of entire GitHub files — find any issue that can cause wrong data or hallucination. We need absolutely correct data for decision making."
**Scope this round:** every file NOT covered by round 1 (`OX_ALPHA_66_Data_Forensics_Audit_20261007.md`): the sizing engine, execution simulator, remote reconciler, brain loop, headless server/runtime, cognitive engine, data factory, deploy scripts, test suite, state files, and repo-wide secrets/hallucination-pattern sweeps.
**Round-1 status first:** the muscle **redeployed the hardened generator** — the 13:37 UTC live snapshot carries every round-1 integrity field (`indicators_source`, `indicator_age_min`, `bars_last_close_utc`, `ema_200_bars_used`, `quote_source: MT5_L1_TICK`, `MODEL_RECONSTRUCTED_OI_COHORTS`, `SYNTHETIC_STRUCTURAL_MODEL` coverage, ETF `NOT_YET_REPORTED`). H3 closed. Live effect already visible: SP500 regime now correctly prints **BEARISH** (previously impossible — the dead-slope bug), and USWTI #18625151 progressed to **PHASE_1_PROFIT_LOCKED +3.91R** (equity 4,830.41, cushion +55.41).

---

## R2-1 — P0 SECURITY: live HMAC secret hardcoded in the repo

`deploy/run_headless.py` (before this fix):
```python
os.environ["OMNI_API_SECRET"] = "0b07f4298deddd67dcb505038002399023601bfed067cf48"
```
This is the **signing key for the Arena-brain → laptop command channel** (`stage_order`, `modify_sltp`, `close_position`). Anyone with repo read access can forge validly-signed trading commands against the headless service. It directly violates consultation-5 ("zero hardcoded secrets — gateway tokens via environment variables only") and contradicts `deploy/.env.example`, which states the secret must never be committed. **Fixed:** removed; `run_headless.py` now **fails closed** without `OMNI_API_SECRET` (explicit `OMNI_ALLOW_UNSIGNED_LOCAL=1` opt-in for isolated lab runs only).
**⚠ REQUIRED MUSCLE ACTION (cannot be done from here): ROTATE the secret on both ends.** The leaked value remains recoverable from git history regardless of this fix — deleting it from HEAD is not revocation. Generate a fresh 32-byte secret per `deploy/start_tunnel.ps1` and update the brain side.

## R2-2 — HIGH: the entire test suite was silently bypassed

Every test file is named `Test_*.py` (capital T), but pytest's default collection pattern is `test_*.py`. Result: **`pytest Tests/` and bare `pytest` collected ZERO tests** — "no tests ran" in 0.00s, no error. Any CI or manual gate invoking pytest normally would see an empty (falsely-green) run, masking every regression. Fixed with `pytest.ini` (`python_files = Test_*.py test_*.py`, `testpaths = Tests`). **The first true full-suite run in repo history: 350 passed, 7 failed** — all 7 triaged and resolved below. Final state: **354 passed, 3 skipped (offline-network skips), 0 failed.**

## R2-3 — HIGH (real bug): the trader loop could not run on Linux

`Omni_Trader.run()` imported `msvcrt` unconditionally (Windows-only) for the writer lock — once at acquisition (line 1181) and once in the `finally` unlock (line 1219). On Linux — the platform `deploy/Dockerfile` targets — the loop crashed instantly with `ModuleNotFoundError`, and even the exit path had a second unconditional reference. Fixed with a cross-platform lock: `msvcrt.locking` on Windows, `fcntl.flock` on POSIX (same crash-released exclusive semantics). The paper-mode causality test now passes on Linux.

## R2-4 — MEDIUM (real regression): Farside parser lost its per-fund contract

`parse_farside_table`'s docstring promises `[{date, funds{...}, total_musd}]` and the committed test asserts `rows[-1]["funds"]["GBTC"] == -40.0` — but the implementation only ever emitted the total. The per-fund breakdown (which the ETH-flow cross-check and per-ISSUER attribution depend on) silently vanished in an earlier refactor. Restored: fund names from the header row, `(40.0)` → −40.0 negatives, and Farside's `"-"` placeholder cells → `None` (not-yet-reported, matching round-1's M1 semantics).

## R2-5 — LOW: live-network tests masquerading as unit tests

`Test_Hyperdash_Client.py` (live POST to api.hyperliquid.xyz), `Test_Terminal_Render.py` (live Hyperdash asset switch), and `Test_Omni_Engine.py::test_stage_limit_order_passive_guard` (imports the Windows-native `MetaTrader5` module directly — it only passed on Linux by accident of test-ordering module injection) all failed hard in offline/CI environments. All three now skip gracefully with an explicit reason. AUDIT.md's P1 ("existing network tests are not deterministic") is now half-addressed; the remaining work is proper fixture mocking.

## R2-6 — Verified clean this round (no action)

- **`Risk_Sizing_Engine.py`** — institutional grade. Frozen `RiskPolicy` **raises** if capital/DD/position invariants are altered; `completed_statistics` **refuses stale completed bars** (`completed_bars_stale`) — notable contrast: the brain would have refused the frozen-bar data the telemetry happily published in round-1's C1 window. Sealed deterministic z-scores ("the cognitive engine can never substitute its own statistics"). Decimal-floored volume; lookahead-safe bar filtering; session-gap-aware returns.
- **`Terminal/Execution/remote_reconciler.py`** — HMAC-SHA256 + 30s replay window + single-use nonce ledger + `command_id` idempotency + protocol risk caps (≤10.00 test limits, ≤20.00 generic, refuses at 2 filled). Textbook.
- **`Execution_Simulator.py`** — quote-age/spread/deviation guards at submission AND execution, passive-limit discipline, cancel-on-spread-widen, expiry handling. No fabricated fills.
- **`Cognitive_Engine.py`** — the mechanical anti-hallucination layer: every numeric claim in decision prose is attested against the sealed feature digest; unmatched statistics **reject the decision and journal it** for forensic review.
- **`Headless/server.py`** — HMAC on all endpoints; **503 "no_secret_configured"** when the secret is missing (fail-closed, not fail-open).
- **`Data_Factory/factory.py` / `live.py` / `streams.py`** — zero-lookahead guards, receipt timestamps, pillar-health watchdog with stall streaks; the `random.Random()` in `live.py` is cadence jitter only, never data.
- **`Asset_Universe.py`** — alias/broker-base mapping correct for the Blueberry symbol set (incl. DOG→DOGUSD, LINK→LNKUSD special cases); no wrong-instrument routing found.
- **Secrets sweep repo-wide** — clean apart from R2-1 (test fixtures use obvious fake values; `deploy/.env.example` is placeholders-only; tunnel script generates random secrets).
- **`Binance_Data/`** — manifest + verification report re-checked: row counts, SHA256 digests, and 3-agent continuity/microstructure/schema verification all PASS for the sampled symbols.
- **`Api_Client.py`, `Pioneer_Decision_Engine.py`, `Quantitative_Governance.py`, `Dump_History.py`** — no fabrication patterns beyond those already catalogued in AUDIT.md.

## Cumulative posture after rounds 1+2

| Layer | State |
|---|---|
| External data (FNG, Farside, Coinbase, Binance L2/OI/CVD/funding/HTF) | ✅ verified authentic |
| Telemetry generator | ✅ hardened (round 1) + **deployed and live** (confirmed 13:37 UTC) |
| Sizing/risk engine, reconciler, simulator, server | ✅ clean (audited this round) |
| Cognitive/decision layer | ✅ mechanically attested anti-fabrication |
| Test suite | ✅ 354 passing, collection bypass fixed, network tests isolated |
| Credentials | ⚠ **secret rotation required** (R2-1) |
| Plans on staging hold (round 1) | SP500 + GBPUSD remain held pending re-anchor on fresh data |

**Outstanding muscle actions:** (1) rotate `OMNI_API_SECRET` both ends — P0; (2) re-anchor or retire the two held plans on fresh indicators; (3) consider wiring `pytest` (now meaningful) into CI with `--maxfail=1` so collection bypasses can never recur.

*Every claim is reproducible from the repository, its git history, or the live public sources cited. No statistic is fabricated.*
