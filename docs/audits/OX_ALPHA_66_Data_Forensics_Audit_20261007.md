# OX_ALPHA_66 — Full-Repository Data Forensics Audit (2026-10-07, ~13:30 UTC)

**Mandate (principal):** "Deep audit, debugging, forensics of entire GitHub files — find any issue that can cause wrong data or hallucination. We need absolutely correct data for decision making."
**Method:** line-by-line review of the telemetry generator, indicator engine, liquidation/stop engines, MT5 bridge, stager; numeric recomputation of every published statistic from raw parquet candles; git pickaxe forensics over the full 60s-snapshot history; independent external verification of every externally-sourced datum.
**Verdict:** the *external* data layer is authentic (verified against live sources). The *internal* pipeline has **4 critical defects, 6 high, 7 medium** — one of which (the stale-indicator window) **corrupted live decision data for ~95 minutes today, including the 12:41 scan study and both new trade plans.** All fixes are committed with this audit; two plans are placed on staging hold.

---

## 1. The centerpiece finding: the stale-indicator incident (11:30 → 13:04 UTC)

Every candle-derived indicator in the live telemetry — EMA 20/50/200, ATR(14), RSI(14), session VWAP, session sigma — was computed on **15m bars frozen at ~07:45 UTC** for at least 95 minutes, while bid/ask quotes, the account block, and all Binance-sourced data (L2, OI, CVD, funding, HTF) stayed live. The bar-fetch path failed silently (`except: pass` → parquet fallback → parquet itself frozen) and **no field anywhere indicated indicator staleness.**

Git-verified timeline (values extracted from the per-minute snapshot commits):

| as_of UTC | SP500 ema_200 | SP500 ATR | SP500 VWAP | SP500 Z | BTC ATR | GBPUSD Z |
|---|---|---|---|---|---|---|
| 11:30 | 7,789.44 | 3.093 | 7,825.01 | −1.92 | 194.5 | −2.29 |
| 12:20 | 7,789.44 | 3.093 | 7,825.01 | **−11.02** | 194.5 | **−8.16** |
| 12:41 (scan study) | 7,789.44 | 3.093 | 7,825.01 | **−10.65** | 194.5 | **−8.60** |
| 12:50 (Council 66) | 7,789.44 | 3.093 | 7,825.01 | **−10.79** | 194.5 | **−8.93** |
| 13:00 | 7,789.44 | 3.093 | 7,825.01 | −11.00 | 194.5 | −7.83 |
| **13:04 (bar feed recovered)** | **7,812.17** | **5.900** | **7,816.96** | **−2.12** | **232.0** | **−1.96** |
| 13:12 | 7,812.17 | 5.900 | 7,816.96 | −2.22 | 232.0 | −1.95 |

**How to read this:** EMA/ATR/VWAP columns frozen for hours while the Z column swings — because `vwap_z = (LIVE mid − FROZEN vwap) / FROZEN sigma`. The "historic extremes" (SP500 −10.8σ, GBPUSD −8.9σ, NAS100 −11.3σ) **never existed**: fresh session sigma is ~4× larger (SP500 3.35 → 13.22) and the true Zs are **−2.1 to −2.3**, ordinary deviations. The muscle's commit `44bc5a9` ("fix True UTC Session VWAP broker offset (10800s) + live MT5 bar syncing") landed at ~13:05 UTC and recovered the feed.

**Decision data corrupted by this window:**
- The 12:41 scan study's entire Z/extremity table (superseded — banner added).
- **SP500 plan** (`OXALPHA66-SP500-LONG-EMA200-20261007A`): "sitting EXACTLY on EMA200 7,789.44" was the frozen value (fresh proxy reads 7,812.17); stop 6.0 pts = 1.94× the *stale* ATR but only **1.02× the fresh ATR 5.90 — below the 1.5× floor.** Placed on **staging hold** (limit 7,786 is ~1.7 pts under live mid — it must not fill on a stale thesis).
- **GBPUSD plan** (`OXALPHA66-GBPUSD-LONG-POSTFOMC-20261007A`): the "deepest FX extreme at −8.6σ" premise is dead (fresh Z −1.95); stop 9 pips = 1.50× stale ATR but **1.13× fresh ATR 0.0008 — below the floor.** Placed on **staging hold** pending re-anchor.
- **BTC plan** (live position #18630694): stop 680 = 3.50× stale ATR, **2.93× fresh ATR — still compliant**; no action, but the "3.50×ATR" label in the plan is stale-derived.
- Council 66 formal report's indicator citations (regime/Z/RSI rows) — correction addendum appended.

## 2. Critical finding 2: "ema_200" is not an EMA200

`generate_telemetry_snapshot.py` fetches `count=120` bars; `CandleIndicatorEngine.compute_indicators` computes `calc_ema(closes, 200)` only when `len(closes) >= 200`, **else silently falls back to a ~96-period EMA and labels it `ema_200`**. With 120 bars, every "EMA200" in the telemetry is an EMA96-in-disguise. Additionally `calc_ema` seeds at `arr[0]` with no warmup — even with 200 bars the first bar retains ~37% weight, so the estimator needs ~800 bars to converge. Proof: the deployed "ema_200" moved **23 points in 22 minutes** (7,789.44 → 7,812.17 between 12:50 and 13:12) — behavior of a fast average, impossible for a true EMA200 on 15m bars. Every EMA200-anchored decision today (SP500 plan, USDJPY watchlist, regime classification) used the proxy. **Fix:** 800-bar fetch; `ema_200` emitted as `null` + `ema_200_bars_used` when < 400 bars available (proxy impossible to mislabel).

## 3. Critical finding 3: armed fabrication paths in the account/book block

`generate_telemetry_snapshot.py` (repo copy):
```python
equity_usd  = float(acc_summary.get("equity_usd")  or 4834.50)
balance_usd = float(acc_summary.get("balance_usd") or 4831.73)
margin_used = float(acc_summary.get("margin_usd")  or 412.50)
...
```
If MT5 disconnects, `get_account_summary()` returns `{"connected": False}` → these **hardcoded constants (frozen from this morning's real state — 4,831.73 was the genuine 09:00 balance) print as live account equity**. Worse, `get_open_positions() if bridge.initialized else []` → positions silently empty → capacity "OPEN" — **a snapshot that looks alive, advertises free slots, and hides real open positions that still exist server-side.** Git forensics: the fallback **never fired in committed history** (the equity trace 09:00–13:10 is continuous and plausible; the `4834.5` pickaxe hits were the substring `874834.55` in ask-depth) — but it is one disconnect away. Related silent paths: synthetic bid/ask fabrication (`mid×0.9998/1.0002`, hardcoded 4.0 bps) when quotes missing; `atr = mid×0.006`, `rsi = 50.0`, `sigma = 0.8×atr` fabrications when indicators missing. **Fix:** fail-closed — on bridge failure the generator writes `docs/telemetry/.generator_error.json`, exits non-zero, and **does not touch the live snapshot** (its `as_of` age then exposes staleness; brain must NO_TRADE on it per consultation-5 semantics).

## 4. Critical finding 4: synthetic reconstructions relabeled "REAL"

The engines are honest; the generator's formatting strips their honesty:
- `LiquidationReconstructionEngine` returns `coverage: "SYNTHETIC_OI_DELTA_MODEL"`. The generator **drops the coverage field** and labels the output `source: "REAL_BINANCE_FUTURES_OI"`. Only the OI *total* is real — the bands are reconstructed. Mathematical proof from the live snapshot: the four "cascade bands" below BTC mid 83,350 (83,249 / 82,422 / 80,389 / 75,336) are **exactly `liq_price(mid, L)` for L = 100/50/25/10** (83,183/82,516/80,433/75,348 ± band mid) — i.e., one synthetic cohort at ~mid smeared across four fixed leverage tiers (weights 35/40/20/5%). The "8.44M cascade fuel at 82,525–82,731" cited in the Council 66 report is a **model artifact, not observed fuel** (the phase-1-before-FOMC recommendation stands on conservatism alone).
- `StopClusterEngine` returns `coverage: "SYNTHETIC_STRUCTURAL_MODEL"`; amounts are `recency × log1p(tick_volume) × 1000` — **arbitrary units presented as `amount_usd`** (e.g., USWTI "2,389.6 USD of sell stops" = 2.39 model-weight units). The generator strips the coverage marker here too.
**Fix:** coverage markers passed through; liquidation source relabeled `MODEL_RECONSTRUCTED_OI_COHORTS (real OI total, synthetic band allocation)`; amount semantics labeled.

## 5. High-severity findings

- **H1 — Plans non-compliant on fresh data:** SP500 stop 1.02×ATR, GBPUSD 1.13×ATR (floor 1.5×) — both on staging hold with this audit (see §1).
- **H2 — Dead `ema_200_slope`:** requires ≥212 bars; generator fetched 120 → **slope = 0.0 for 24/24 assets in every snapshot** → `trend_regime` can never print BEARISH (needs slope < 0) and prints BULLISH whenever price > EMA200 (slope 0 passes `>= 0`). The regime classifier is structurally biased on a crashing day: the board showed zero BEARISH assets during a full risk-off flush.
- **H3 — Deployed ≠ repo generator:** three fingerprints (no `execution_specs` key, no `session_bars`, capacity string format) prove the daemon runs an older build than the repo — the 13:05 UTC "specs restore" commit is not yet live. **Redeploy required; repo fixes do nothing until then.**
- **H4 — Candle store frozen:** all 24 `Data/Candles/*_15m.parquet` end at ~07:45 UTC (512 rows, otherwise clean: monotonic, no dups, no OHLC violations — verified). The parquet write path failed silently; any backtest/audit on the repo today runs on frozen candles.
- **H5 — FX friction understated:** EURUSD/GBPUSD print `spread_price: 0.00000` (raw-spread MT5 account) → the stager's `friction_r = (ask − bid + tick)/distance` sees ~0.0 and passes trivially; **commission (~3.50 USD/lot/side) is excluded** — GBPUSD true round-trip ≈ 0.08R, not the 0.011R the plan claims.
- **H6 — Capacity constant wrong in repo:** `max_slots = 4` (entered at 12:20 UTC, commit `bddcfd4` "expand capacity to 4 slots") vs policy max 2 (`max_concurrent: 2`). Status string and per-asset gating use 4 → **over-admission risk the moment this repo version deploys.** Fixed to a single constant.

## 6. Medium / low findings

- **M1** Farside ETF placeholder semantics: "07 Oct 0.0" is Farside's not-yet-reported placeholder (verified live: row of "-", total 0.0) presented as a reported zero. 06-Oct +118.8M is row-verified authentic (IBIT 122.0 + MSB 7.8 − BTC 11.0). Fixed: null + `NOT_YET_REPORTED` until the day completes.
- **M2** FOMC/blackout window strings are hardcoded in the generator (not read from `Data/macro_calendar.json`, which exists and is verified) — they go silently stale tomorrow. Fixed with a staleness flag; full calendar wiring recommended.
- **M3** Whale-wall `persistence_sec = 0.0` for 51/51 walls — persistence state is not surviving runs; feature dead. `first_seen_utc` now emitted for diagnosis.
- **M4** Session VWAP: <3 session bars silently falls back to rolling-24h VWAP (mislabeled "session"); sigma is dispersion of typical price → strong-trend sessions compress it and inflate |Z| even with fresh bars (SP500 fresh Z −2.2 still carries this bias — treat |Z|>4 as "trend day," never "10σ event").
- **M5** No order-lifecycle journal: XRP pending #18624984 vanished between 11:07:47 and 11:11:47 UTC with no position, no fill, no cancel record (the bridge has `reconcile_intent_history` — unused by telemetry). `decision_ledger.jsonl` abandoned (1 line, Oct 4). Recommend: journal every order/deal event.
- **M6** Three disagreeing capital sources: `mt5_ai_trader_state.json` 4,841.23 vs live balance 4,813.44 vs `ofc_paper_positions.json` 5,000. Sizing must read live telemetry only.
- **M7** `_utc_offset_seconds` snaps to a 30-min grid from a possibly-stale tick — theoretical ±30-min timestamp error on illiquid symbols (today's position times verified correct: USWTI first appears ~11:56, BTC ~12:51–12:53, matching reported opens).
- **L1** `session_bars` field absent in deployed output. **L2** Coinbase premium includes USDT basis (−2.4 bps reported; independent check ≈ −0.7 bps — same order). **L3** Auto-`confluence_trade_setup` uses 1.1×ATR stops — below the 1.5× floor if ever staged. **L4** `index.js` (4,008 lines) is a third-party Hyperdash dashboard bundle — reference material, not a data source.

## 7. Verified authentic (no action)

External layer independently verified this session: FNG **71/Greed ts 1791331200 — exact match** with api.alternative.me; Farside 06-Oct BTC **+118.8M** row-verified; Coinbase BTC-USD spot 83,292 (premium plausible); Binance L2/OI/CVD/funding/HTF internally consistent (60×1m CVD buckets: `taker_buy + taker_sell == total_vol` exactly, timestamps monotonic 60s; funding 8×8h; 4H/D1 aligned). Account arithmetic exact (equity = balance + Σfloats, margin level, cushion — recomputed). All six trade-plan geometries recompute exactly (risk, R, epochs). Parquet candles clean on all integrity axes. Bridge offset handling correct for today's positions. The 60s telemetry commit chain is continuous 11:30→13:12.

## 8. Remediation delivered with this audit (commit references in git log)

1. `generate_telemetry_snapshot.py` hardened: fail-closed MT5 (no fabricated account/book — error marker + non-zero exit), 800-bar fetch, `ema_200` null below 400 bars + `ema_200_bars_used`, single `MAX_CONCURRENT_SLOTS = 2`, per-asset `bars_last_close_utc` + `indicator_age_min` staleness fields, `indicators_source` (LIVE_BRIDGE vs PARQUET_FALLBACK), coverage passthrough + honest liquidation source label, ETF `NOT_YET_REPORTED` semantics, macro-calendar staleness flag, FX zero-spread caveat, whale `first_seen_utc`. Injectable bridge/paths for testability.
2. New test suite `Tests/Test_Telemetry_Data_Integrity.py`: fail-closed on bridge loss (snapshot not overwritten, error marker written), no fabricated constants, capacity freeze at 2, coverage markers present, ETF placeholder semantics, EMA null below threshold, staleness fields present.
3. Both new plans annotated `staging_hold: true` with stale-ATR reasoning; scan study and Council 66 report carry correction banners/addenda.
4. Required from the muscle (cannot be done from here): **redeploy the generator** (H3), **re-sync the candle parquets**, and re-anchor the two held plans on fresh ATRs if the setups survive re-analysis; journal order lifecycle events.

*Every claim above is reproducible from the git history and files in this repository, or from the live public sources cited. No statistic is fabricated.*
