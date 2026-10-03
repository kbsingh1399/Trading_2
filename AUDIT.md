# Institutional audit — Trading_2

## Verdict and scorecard

This is a useful visualization prototype, not yet an institutional execution or research-grade pipeline. Scores (1 poor, 10 strong): architecture **5/10**, causal soundness **4/10**, microstructure fidelity **3/10**, latency/resilience **3/10**, production readiness **2/10**. The claimed Hyperdash contracts and 234-asset coverage must be verified against captured fixtures; the existing network tests are not deterministic tests.

## P0 — must fix before using features in a backtest

* **Causal leak:** `Heatmap_Engine` used the first future snapshot when no preceding observation existed. It now returns an empty observation. Preserve `observed_at`, `source_interval`, and `age_seconds`; never silently fill pre-history.
* **Liquidation semantics are not proven by price:** `mid < current` is a visualization heuristic, not proof of a long liquidation. Use an explicit position side/event field from the provider. If unavailable, name fields `below_price_liq_risk` and `above_price_liq_risk`, not long/short.
* **Stop direction requires an order-type field:** price above market implies a buy trigger, but does not prove stop-loss versus stop-entry. Keep `buy_trigger`/`sell_trigger` separate from `stop_loss` until the exchange schema supplies intent.
* **Historical snapshots are not event history:** carry-forward of an hourly landscape can create stale exposure and survivorship/availability bias. Add snapshot age and drop/decay observations beyond a documented TTL.

## P1 — high

* Synchronous `urllib` in FastAPI handlers serializes work per worker and blocks the event loop. Move I/O to a shared `httpx.AsyncClient` or `asyncio.to_thread`, with bounded concurrency, per-host token bucket, connection pool, timeout, and circuit breaker.
* Retry only 429/5xx, honor `Retry-After`, add jitter, and cap total request deadline. A fixed 30-second retry can synchronize callers into another rate-limit burst. The client now has a shared process-local token bucket, but multi-process deployments need a Redis/shared limiter.
* Cache keys must include endpoint, coin, price range, timeframe and schema version. Use monotonic expiry and stale-while-revalidate; never let an old cache masquerade as real-time.
* The live poller can overlap requests after a slow response and has no abort controller. Use a single-flight request, abort the prior fetch on coin/timeframe change, and clear its interval.
* Do not expose wallet addresses in logs or public APIs without a data-governance decision; “verified” is a provider assertion, not identity proof.

## P2 — moderate

* Whale tiers of $50k/$150k/$500k are not cross-asset comparable. Store notional, notional/ADV, notional/(ATR*contract multiplier), and percentile by coin.
* `$1` denominators distort small observations. The dump now uses `(x-y)/(x+y)` and returns zero for no data. Retain raw totals and missingness flags.
* Canvas should use one persistent context, device-pixel-ratio backing dimensions, requestAnimationFrame coalescing, typed arrays, and a dirty rectangle. Guard `plotW <= 0 || plotH <= 0` before coordinate transforms.

## Recommended definitions

For each snapshot observed at `s` and candle close `t`, use only `s <= t`; `age=t-s`. Apply `w=exp(-age/tau)` only if a decay model is validated, and set weight zero after TTL. For a price level `L`, use distance `abs(log(L/close))/ATR_log`, not raw dollars. Compute rolling, past-only z-scores: `(x-mean_{t-1,N})/(std_{t-1,N}+eps)`. Imbalance is `(long-short)/(long+short)`; retain a `no_observation` flag.

Maintenance cushion should be computed from provider tiered maintenance margin and collateral haircuts: `cushion=(equity-maint_margin(notional)-fees_buffer)/equity`, with stress price and mark/index divergence scenarios. Do not infer liquidation price from leverage alone.

## Drop-in code delivered

* `Terminal/Microstructure.py`: explicit-side liquidation classifier, bounded imbalance, and a thread-safe token bucket.
* `Terminal/Api_Client.py`: shared limiter before REST/GraphQL calls.
* `Terminal/Heatmap_Engine.py`: removes future fallback.
* `Terminal/Dump_History.py`: bounded imbalance features.

## Quant roadmap

1. Capture immutable raw API payloads with request/response timestamps and schema hashes.
2. Build replay fixtures and contract tests; separate availability time from candle time.
3. Add age/TTL/missingness, ATR-normalized cluster distances, weighted depth slope, spread, book imbalance, trade-flow delta, liquidation/stop z-scores, and regime interactions.
4. Purged walk-forward splits with embargo at least the maximum feature lookback; fit scalers on train only. Compare no-orderflow, orderflow, and shuffled-label baselines.
5. Model transaction costs, queue position, latency, funding, liquidation slippage, partial fills, and exchange outages. Promote only after paper and shadow execution.
6. Run all 20 engines from one feature-versioned Parquet contract and report calibration, turnover, capacity, PnL attribution, and degradation by asset/liquidity bucket.

## Pull commands

This session's branch is `arena/01a100cd-trading-2`:

```bash
git fetch origin
git checkout arena/01a100cd-trading-2
git pull --ff-only origin arena/01a100cd-trading-2
```

For a local copy that has only `main`, inspect or merge the reviewed branch rather than assuming it is safe to overwrite production:

```bash
git fetch origin
git checkout -b arena-terminal-audit origin/arena/01a100cd-trading-2
```
