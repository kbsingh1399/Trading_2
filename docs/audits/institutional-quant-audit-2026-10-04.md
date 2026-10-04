# Institutional quantitative audit — Trading_2

**Audit date:** 2026-10-04 UTC  
**Reviewed checkout:** `arena/01a10721-trading-2`, based on `1279789d77547698ae669a4932dee2f69f61b995`  
**Scope:** `Terminal/OF_Strategy.py`, `Terminal/MT5_Execution_Bridge.py`, the causal data path, and the Hyperdash/MT5 interfaces.

The supplied provenance cites commit `7b9a0b7`, but that object is not the checked-out parent in this session. The findings below are against the files actually present in the checkout, not against an unverified remote snapshot.

> **Risk notice:** this is a software and research audit, not a recommendation to open, close, or modify a live position. The account figures and tickets in the brief were not independently queried from MT5 in this environment. Do not deploy the live mode until the replay, paper, and broker-contract checks below pass.

## Executive verdict

The project has a useful research skeleton and a clear separation between strategy and MT5 IPC, but the pre-audit live path was not yet institutional-grade. The most important problems were not the absence of another indicator; they were causal integrity, portfolio-level factor limits, broker-side execution controls, and the distinction between an observed resting order and an executable/intentional stop or liquidation event.

The implementation in this branch adds:

- causal orderflow feature normalization with CVD/tick imbalance and age-decayed L3 orders;
- an explicit BTC-factor beta stop-risk budget for concurrent positions;
- Parkinson/Garman-Klass plus Kaufman efficiency regime gates;
- ATR/tick/spread-normalized liquidation-wall TP offsets;
- MT5 spread, quote-age, risk-preserving volume, stop/freeze-level, account-allow-list, and `order_check` guards;
- opt-in, expiring passive limit staging (`--entry-mode limit`) rather than silently replacing market execution;
- a persisted equity high-water mark and hard drawdown veto;
- removal of `future_cvd_15m` from the research feature path and the Delta fallback in `Data_Engine.py`;
- an atomic strategy state write and tests for the new pure quantitative primitives.

These are controls, not proof of alpha. The weight vector is a transparent prior and must be fitted/calibrated with purged out-of-sample data before it is treated as a signal.

## Scorecard

Scores are for the code as found, with the branch changes noted in the last column. A 10 means evidence-backed, replay-tested, broker-validated production behavior; it does not mean more complexity.

| Area | As found | After this branch | Why it is not higher yet |
|---|---:|---:|---|
| Microstructure realism | 4/10 | 5/10 | L2/L3/tape are present, but provider semantics, queue position, cancellations, latency, and partial fills are not captured in a deterministic replay contract. |
| Causal rigor | 3/10 | 6/10 | The walk-forward/purge structure is a good start, but the original path consumed `future_cvd_15m`, and model thresholds were fitted in-sample. The future CVD leak is removed here; threshold calibration still needs a validation fold. |
| Risk governance | 4/10 | 6/10 | Original controls had a position count and nominal per-trade budget, but live beta/HWM/margin-stress gates were absent. Beta stop-risk and HWM vetoes are now wired in; margin, liquidation, and cross-currency stress are still missing. |
| Execution latency and resilience | 3/10 | 5/10 | The bridge now rejects stale/wide quotes, runs `order_check`, floors volume, and supports expiring limits. Hyperdash polling is still synchronous at the strategy boundary and the MT5 terminal remains a remote IPC dependency. |
| Production readiness | 2/10 | 4/10 | There is no immutable event log/replay hash, broker contract test suite, alerting/SLO dashboard, or shadow-to-live promotion gate. |

**Go/no-go:** research and paper/shadow mode: **GO with the new vetoes enabled**. Unattended live entry: **NO-GO** until the validation matrix at the end is completed. Existing positions should remain manageable by the ratchet, but a failed data/quote/account check must fail closed for new entries rather than forcing a trade.

## Material findings

1. **The original confluence points double-counted nested liquidation thresholds.** A $500k wall earned both the `$100k` and `$500k` points, while a $99k-to-$100k change caused a discontinuous decision. The new live score is continuous and saturating; fit its weights later with a calibrated model.
2. **The historical feature path used a field named `future_cvd_15m`.** It was used to build `zc_norm`/`sf_div` and structural delta. That is a direct or likely availability leak. The branch no longer loads it and uses observed spot CVD changes. The field may still be used as a label in a separate research job, but never as a feature.
3. **A ratcheted stop was being reused as the definition of 1R.** Once the broker SL moved, `gain_r` changed its denominator. The branch stores an immutable per-ticket `position_r_dist` and uses that for every phase.
4. **The live hard drawdown guard did not gate new entries.** It now maintains a persisted equity high-water mark and blocks entries at `peak_equity * (1 - 4.5%)`. The initial $5,000 reference implies a $4,775 floor, but the live broker equity must be the source of truth.
5. **A fixed `$0.10` front-run offset has no cross-asset meaning.** It is replaced with a broker-point, spread, and ATR-aware offset. The exact coefficients still require fill/outcome calibration.
6. **An inside-spread limit is not a free improvement.** It can miss the move or be adversely selected. Limit staging is opt-in, expires after 30 seconds, and does not silently fall back to a market order.
7. **The macro blackout is a safety gate, not a complete event calendar.** The current recurring schedule can miss revisions, unscheduled releases, holidays, DST changes, and non-US events. Treat an unavailable calendar as a veto in live mode if macro safety is a hard requirement.
8. **“Liquidation below price” and “resting whale” are provider semantics, not facts inferred from price alone.** Retain explicit side, `observed_at`, source timestamp, schema version, and missingness. A provider assertion that an address is “verified” is not identity proof.

---

## Q1 — Orderflow entry trigger refinement

### Recommended feature vector

At decision time `t`, use only observations whose **provider availability time** is `<= t`. For a feature `x`, use a past-only robust normalization:

\[
 z_t(x) = \frac{x_t - \operatorname{median}(x_{t-N:t-1})}
 {1.4826\operatorname{MAD}(x_{t-N:t-1})+\epsilon}
\]

The live implementation uses bounded versions for fields that arrive in heterogeneous schemas:

- L2 imbalance:
  \[
  I^{L2}_t=\frac{V^{bid}_t-V^{ask}_t}{V^{bid}_t+V^{ask}_t+\epsilon}
  \]
- Liquidation demand/supply: sum bands within a maximum distance, weighted by proximity, then map with `tanh(log1p(notional / scale))`. Do not use raw USD thresholds across BTC, SOL, and XRP.
- L3 support/resistance: for each order `j`,
  \[
  W_j = N_j\,\exp(-\text{age}_j/\tau)\,
        \max(0,1-d_j/d_{max})\,1_{\text{age}_j<TTL}
  \]
  where `age` is measured from `observed_at`/`last_seen`, not the time the strategy happened to poll it.
- Tape imbalance:
  \[
  I^{tape}_t=\frac{B_t-S_t}{B_t+S_t+\epsilon},\qquad
  I^{whale}_t=\frac{B^{whale}_t-S^{whale}_t}
  {B^{whale}_t+S^{whale}_t+\epsilon}
  \]
- CVD slope: fit a slope to completed sub-bars or use a finite difference of observed CVD. A useful absorption/divergence feature is
  \[
  D^{CVD}_t = \tanh\left(k\left(z(\Delta CVD_t)-z(r_t)\right)\right)
  \]
  where positive `D` means CVD is stronger than the price move. Never use a `future_*` CVD column.

The branch function `compute_orderflow_features()` implements these fields, including `cvd_divergence`, `tick_imbalance`, L2, weighted liquidation, and age-decayed L3 features.

### Score and decision rule

A transparent starting prior is:

\[
 S_L=\sum_i w_i\max(x_i^+,0),\qquad
 S_S=\sum_i w_i\max((-x_i)^+,0)
\]

then map the evidence to the existing six-point display scale. The branch uses weights for liquidation, L2, L3, whale tape, tick imbalance, and CVD divergence. The decision must additionally require a margin between long and short scores, macro permission, a regime permission, a beta-risk budget, and a fresh executable quote.

For research, replace the hand weights with a causal calibration model:

```python
features = compute_orderflow_features(snapshot, price, now_seconds=available_at)
X = past_only_robust_scale(features)
p_win = calibrated_logistic.predict_proba(X)[0, 1]
edge_r = p_win * avg_win_r - (1 - p_win) * avg_loss_r
enter = edge_r > estimated_round_trip_cost_r + safety_margin_r
```

Fit the scale, weights, and calibration on the training fold only; fit a probability calibration model on a later validation fold; apply both to a purged test fold. Report Brier score, calibration by decile, conditional expectancy, and degradation by asset and spread bucket. A CVD feature should be retained only if its incremental out-of-sample contribution survives shuffled-label and no-orderflow baselines.

### Answer to the specific suggestions

- **CVD slope divergence:** yes, but only from completed/available observations and normalized by its own historical scale.
- **Sub-bar tick imbalance:** yes; use both all-tape and whale-tape imbalance, with a minimum notional/print count so one trade cannot dominate.
- **Exponential resting-order decay:** yes, but only when the feed supplies an observation/refresh time. Use a TTL and log missing age; an undated order is not automatically “fresh.”
- **Absolute $100k/$500k cutoffs:** use them as reporting buckets, not as the primary cross-asset decision variable.

---

## Q2 — Cross-asset beta and hedge governance

A SOL long and XRP short are not automatically market neutral. Estimate the common crypto factor using completed 15-minute log returns:

\[
 r_{i,t}=\log(P_{i,t}/P_{i,t-1}),\qquad
 \beta_i=\frac{\operatorname{Cov}(r_i,r_{BTC})}
 {\operatorname{Var}(r_{BTC})+\epsilon}
\]

Use an exponentially weighted covariance or a rolling 96-bar sample, with at least 24 aligned observations and a shrinkage/clip policy. The branch `PortfolioBetaRisk` uses a conservative beta of 1.0 until enough aligned history exists; a stricter live configuration should veto entries when history is insufficient.

For CFD positions, raw notional is not a useful risk budget by itself. First compute stop-risk:

\[
 R_i=|P_{entry,i}-P_{SL,i}|\,q_i\,C_i
\]

where `q` is lots/units and `C` is the broker contract size. Then calculate signed BTC-factor stop-risk:

\[
 F_{net}=\sum_i s_i\,\beta_i R_i,
 \qquad
 F_{gross}=\sum_i |\beta_i R_i|
\]

with `s=+1` for long and `-1` for short. The current branch applies default limits of 2.5% equity net and 5% equity gross, then vetoes a candidate if either projected limit is exceeded. Those percentages are governance starting points, not optimized constants.

For a two-asset beta hedge, the factor-neutral notional relationship is:

\[
 N_B = \left|N_A\frac{\beta_A}{\beta_B}\right|
\]

but beta neutrality does not remove idiosyncratic volatility, basis, funding, spread, or liquidation risk. Also report:

\[
 \sigma_p^2=w^T\Sigma w
\]

using a shrinkage covariance matrix and cap portfolio volatility/expected shortfall separately from BTC-factor exposure. Cointegration/Z-scores should be used only when a stationary spread, stable hedge ratio, and half-life have been demonstrated out of sample. SOL/XRP alone is not evidence of cointegration.

Implementation note: factor exposure is recomputed from live MT5 positions before every candidate; the risk model does not assume two individually acceptable trades are jointly acceptable.

---

## Q3 — Dynamic TP and cascade front-running

The correct offset is in **price units**, but it should be derived from instrument-specific execution units:

\[
 \delta = \operatorname{clip}\left(
 \max(k_{tick}\,point,\;k_{spread}\,spread,\;k_{ATR}\,ATR),
 \delta_{min},\delta_{max}\right)
\]

A reasonable initial prior is `k_tick=2`, `k_ATR=0.025`, and `delta_max=0.10*ATR`. Round the resulting target to the broker digits and then re-check that the target remains beyond the minimum expected value threshold, for example `entry + 1.8R` for a long. The branch function `front_run_offset()` implements this policy.

The value should be increased for stale/volatile books and decreased for a thick wall with low observed cancellation. Add these fields to the replay dataset:

- wall notional and notional/ADV;
- distance in ATR and ticks;
- wall age and refresh count;
- cancellation/consumption rate;
- realized fill probability and time-to-fill at each offset.

A liquidation band is not guaranteed to trade through in the expected direction. Use the nearest **executable** side, preserve a fallback structural TP, and never move a TP closer to market just because an old wall was polled. The branch includes L3 ask/bid walls alongside liquidation bands but still needs wall persistence/fill validation.

---

## Q4 — Broker friction, spread widening, and execution defense

The most robust default at a candle boundary is not a blind market order and not a blind passive limit. It is a conditional execution policy:

1. At `T-30s` (the default `:14:30` cadence), fetch a fresh MT5 quote and reject if spread exceeds the symbol-specific budget.
2. If the signal, regime, macro gate, beta gate, and account guard all still pass, stage either:
   - a passive inside-spread limit with a short expiry when missed entry is acceptable; or
   - a marketable limit/market order with a small deviation budget when participation is more important than queue position.
3. At `T-2s` or on a quote invalidation, cancel the passive order. Do not convert it to a market order unless the strategy explicitly revalidates signal age, spread, and risk.
4. Record decision timestamp, quote timestamp, request/ack timestamps, requested/fill price, spread, deviation, retcode, partial fill, and slippage.

A passive buy limit at the midpoint can fail to fill before a breakout and can be adversely selected when it does fill. Thus `--entry-mode limit` is opt-in, expires after 30 seconds, and deliberately does not silently fall back. The default remains a market order with `max_spread_points`, quote-age, broker `order_check`, and explicit deviation guards.

`MT5_Execution_Bridge.py` now provides:

- `get_execution_quality()`;
- risk-preserving floor volume normalization rather than rounding up;
- account allow-list validation when `--account-id` is supplied;
- stop/freeze-level checks for SL/TP modification;
- `max_spread_points`, `deviation_points`, and stale-tick checks;
- filling-mode retries and `order_check`;
- `stage_limit_order()` and `cancel_pending_order()` for explicit pending-order governance.

The current Hyperdash fetch remains synchronous at the strategy boundary. For production, move it behind a single-flight async poller with request deadlines, stale-age flags, retry-on-429/5xx only, and a circuit breaker. A stale snapshot must never be relabeled “live.”

---

## Q5 — Lightweight local regime classifier

For completed OHLC bars, use two range estimators and Kaufman efficiency.

**Parkinson:**

\[
 \sigma_P^2=\frac{1}{4\ln 2}\left[\ln(H/L)\right]^2
\]

**Garman-Klass:**

\[
 \sigma_{GK}^2=\frac12[\ln(H/L)]^2-(2\ln2-1)[\ln(C/O)]^2
\]

Clamp the realized variance estimate at zero before taking a square root. Compare recent volatility with a past-only median or EWMA baseline:

\[
 VR_t=\frac{\sigma_{recent,t}}{\operatorname{median}(\sigma_{baseline,t})+\epsilon}
\]

**Kaufman efficiency ratio:**

\[
 ER_t=\frac{|C_t-C_{t-n}|}
 {\sum_{j=1}^{n}|C_{t-j+1}-C_{t-j}|+\epsilon}
\]

A simple policy is:

- `SHOCK` if `VR >= 2.25`;
- `MOMENTUM` if `ER >= 0.45` and `VR >= 1.10`;
- `CHOP` if `ER < 0.25` and `VR < 1.50`;
- otherwise `TREND`/`RANGE`.

Then apply setup-specific vetoes:

```python
regime = classify_market_regime(completed_bars, lookback=20)
if setup_kind == "BREAKOUT" and regime["regime"] in {"CHOP", "RANGE"}:
    veto("breakout_in_chop")
if setup_kind in {"MEAN_REVERSION", "LIQUIDATION_FADE"} \\
        and regime["regime"] in {"MOMENTUM", "SHOCK"}:
    veto("fade_against_cascade")
```

The branch wires this gate to liquidation-fade candidates and obtains bars through `MT5ExecutionBridge.get_recent_bars()`, excluding the still-forming bar. `UNKNOWN` is surfaced rather than fabricated; the stricter production policy should veto live entry when a required regime feed is unavailable.

Do not use a regime label as an unvalidated trading signal. Measure veto precision, missed-positive rate, and net expectancy after costs by regime.

---

## Integration map

| File | Change |
|---|---|
| `Terminal/Quantitative_Governance.py` | Pure normalized orderflow, TP offset, regime, and beta-risk functions; deterministic unit-test target. |
| `Terminal/OF_Strategy.py` | Uses those functions for live scoring, TP construction, regime/beta/equity gates, immutable R, atomic state, cadence second, and `market|limit` entry mode. Removes future CVD feature use. |
| `Terminal/MT5_Execution_Bridge.py` | Completed-bar reads, quote quality, account check, floor volume, spread/age/order-check guards, pending limit staging/cancel, and stop/freeze validation. |
| `Terminal/Data_Engine.py` | Prevents `future_cvd_15m` from being a visualization delta fallback. |
| `Tests/Test_Quantitative_Governance.py` | Coverage for decay, normalized flow, TP scaling, regime veto, and signed beta risk. |

Example paper invocation:

```bash
python Terminal/OF_Strategy.py --mode mt5-trader --coin SOL --ticks 1 --paper \
  --entry-mode market --max-spread-points 40
```

Example opt-in limit staging after paper validation:

```bash
python Terminal/OF_Strategy.py --mode mt5-trader --coin SOL --live \
  --entry-mode limit --cadence-second 30 --account-id 5064568
```

The account id is intentionally optional in code but should be mandatory in a live deployment configuration. Never put broker passwords or tokens in the repository or command history.

## Gate 3 and Gate 4 implementation

The promotion harnesses requested in Round 2 are implemented in:

- `Terminal/Orderflow_Replay.py`: deterministic cached-snapshot replay with explicit `observed_at`/`decision_at`, stable SHA-256 input/source hashes, `FRESH`/`DECAYED`/`STALE`/`NO_OBSERVATION`/`FUTURE_OBSERVATION` states, and exponential quote-age decay.
- `Terminal/Execution_Simulator.py`: deterministic market-versus-passive-limit simulator with route latency, quote-age, deviation, spread guard, expiry, partial liquidity, and a configurable 5x candle-open spread spike.
- `Tests/Test_Gates.py`: replay determinism, stale/future fail-closed behavior, market rejection under spread stress, pending-limit cancellation, and favorable-retrace comparison.
- `docs/gates/gate-3-4-validation.md`: snapshot/quote contracts and runbook.

These gates raise reproducibility and observability, but not to an 8/10 production claim by themselves. The simulator is a conservative broker-policy model, not proof of Blueberry queue priority or matching behavior. Production promotion still requires broker-captured quote/fill fixtures and measured slippage/fill-rate results.

## Required validation matrix before unattended live entry

1. **Causal replay:** assert no feature column, including CVD, has availability time after the decision time. Add a schema test that rejects names beginning with `future_` outside label code.
2. **Purged walk-forward:** fit scalers, classifier, calibration, and thresholds on train/validation only; embargo the maximum lookback plus orderflow snapshot TTL. Compare shuffled labels and no-orderflow baselines.
3. **Orderflow replay:** replay raw payloads with provider timestamps, missing snapshots, stale L3, cancellations, and contradictory side fields. Verify `BLACKOUT`, `STALE_DATA`, and `NO_OBSERVATION` behavior.
4. **Execution simulation:** model spread widening, quote age, slippage, partial fills, rejected filling modes, stop/freeze levels, pending expiry, and terminal disconnects.
5. **Portfolio stress:** shock BTC, SOL, XRP, basis, spread, and margin simultaneously; verify net/gross beta, max two positions, HWM floor, and margin cushion.
6. **Shadow/paper:** run a statistically meaningful shadow sample by asset, regime, score bucket, and spread bucket. Compare predicted versus realized fill and slippage.
7. **Promotion gate:** enable live entry only after a human reviews the immutable audit log, broker symbol contract, account allow-list, and a rollback/kill-switch procedure.

The project should be promoted based on calibrated net expectancy and operational reliability, not on the current live PnL or the existence of a convincing liquidation heatmap.
