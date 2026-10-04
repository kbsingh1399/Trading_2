# Promotion Gates 3 and 4 — deterministic replay and execution stress

**Date:** 2026-10-04  
**Branch:** `arena/01a10721-trading-2`  
**Target commit under review:** `13e2e2a`

These two harnesses are offline validation tools. They do not connect to Hyperdash, MT5, or the live account and do not place or modify orders.

## Gate 3 — orderflow replay

Implementation: `Terminal/Orderflow_Replay.py`

The harness accepts a JSON list, or `{ "snapshots": [...] }`, with the following minimum fields:

```json
{
  "observed_at": 1700000000.0,
  "decision_at": 1700000005.0,
  "price": 100.0,
  "l2_book": {"bid_volume_usd": 300000, "ask_volume_usd": 100000},
  "l3_orders": [],
  "liquidations": {"bands": []}
}
```

`timestamp` is accepted as an alias for `observed_at`. Numeric values above `1e11` are interpreted as milliseconds; ISO-8601 strings are accepted. Missing timestamps fail closed as `NO_OBSERVATION`; a decision before the observation is `FUTURE_OBSERVATION`.

For a valid observation:

```text
age = decision_at - observed_at
weight = exp(-age / decay_tau_seconds)
```

Snapshots beyond `max_quote_age_seconds` become `STALE` and produce no direction or score. Valid but older snapshots become `DECAYED`; their directional features and scores are multiplied by the deterministic quote-age weight. The harness also passes the replay decision time to `compute_orderflow_features()`, so L3 order timestamps are evaluated against replay time rather than wall-clock time.

Every input and snapshot receives a SHA-256 digest. Records are stably sorted by `(decision_at, source_index)` so repeated runs produce the same order and result. The output includes state counts, direction counts, policy, source hashes, quote age, decay weight, and features.

CLI:

```bash
python Terminal/Orderflow_Replay.py \
  --input fixtures/hyperdash_snapshots.json \
  --output artifacts/orderflow_replay.json \
  --decay-tau 10 \
  --max-age 30
```

The source snapshot file should be immutable and include raw provider timestamps, request/response timestamps, schema version, and missingness. Do not replay a dashboard's already-smoothed/carry-forward values as if they were exchange events.

## Gate 4 — broker execution simulation

Implementation: `Terminal/Execution_Simulator.py`

The simulator is a deterministic quote-stream model for the bridge's two entry paths:

- **Market:** fills at ask for long/bid for short after route latency, then applies optional adverse slippage. It rejects stale quotes, excessive spread, deviation, non-positive volume, and insufficient liquidity.
- **Limit:** validates that a passive limit is inside the spread, waits until ask <= buy-limit or bid >= sell-limit, respects expiry, and cancels while pending if the spread guard is breached. It does not silently convert a missed limit into a market order.

A 5x candle-open spread spike widens bid/ask symmetrically around the same mid price. This isolates spread impact from directional price movement:

```python
stressed = SpreadSpike(
    multiplier=5.0,
    candle_epoch=1700000000.0,
    open_window_seconds=30.0,
).apply(quotes)
```

For the normal quote sequence, submit before the spike. Submitting after the spike intentionally tests the submission spread guard rather than the pending-order cancellation path.

CLI:

```bash
python Terminal/Execution_Simulator.py \
  --input fixtures/sol_quotes.json \
  --symbol SOLUSD.p \
  --direction LONG \
  --volume 0.50 \
  --submitted-at 1700000899 \
  --limit-price 121.505 \
  --max-spread-points 40 \
  --spike-multiplier 5
```

The simulator reports status, fill price, volume, quote age, spread points, adverse slippage, and reason for both modes. A useful promotion report should include at least:

- fill rate by mode and spread bucket;
- rejection/cancellation/expiry counts;
- mean and p95 adverse slippage in points and USD;
- missed-move opportunity cost for expired limits;
- partial-fill rate and residual exposure;
- result by normal spread, 2x, 5x, and outage scenarios.

A passive limit is not automatically superior. It should be promoted only if the improvement in realized spread/slippage exceeds the opportunity cost of missed fills and adverse selection, after fees and funding.

## Test command

```bash
pytest -q Tests/Test_Gates.py Tests/Test_Quantitative_Governance.py
```

`Tests/Test_Gates.py` covers:

1. deterministic replay ordering and hashing;
2. fresh, decayed, stale, missing, and future observations;
3. five-times open spread behavior;
4. market rejection under a spread guard;
5. pending-limit cancellation during a spread spike;
6. limit fill after a favorable retrace versus market ask payment;
7. deterministic spread transformation.

## Promotion interpretation

These gates increase Production Readiness by making data age and execution assumptions measurable. They do not validate alpha, broker-specific queue priority, or the provider's interpretation of liquidation/L3 side. Before live promotion, add broker-captured quote/fill fixtures, partial-fill behavior, reconnects, stop/freeze-level rejects, and immutable audit-log storage to the scenario set.
