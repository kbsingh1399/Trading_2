# OMNI engine operations and evidence contracts

The production entry point is `Terminal/OF_Strategy.py`; orchestration lives in
`Terminal/Omni_Trader.py`. Historical candle research was preserved in
`Terminal/OF_Backtest_Legacy.py`. Its old scorecard does not validate this policy.

## Run

From the repository root, install `Terminal/requirements-omni.txt` into the
Python environment that will run the engine. MetaTrader 5 must be connected to
the intended USD account. The Hyperdash server must run the updated
`Terminal/Chrome_Terminal.py` for per-component timestamps and sampled wallet
risk. Start the server using its existing launcher or `python -m
uvicorn Terminal.Chrome_Terminal:app --host 127.0.0.1 --port 8095`.

```text
python -m Terminal.OF_Strategy --mode inspect
python -m Terminal.OF_Strategy --mode mt5-trader --paper --account-id ACCOUNT_LOGIN
python -m Terminal.OF_Strategy --mode mt5-trader --live --account-id ACCOUNT_LOGIN
```

Paper is the default. `--ticks 1` bounds verification to one loop. Live dispatch
occurs only at :14:30, :29:30, :44:30 and :59:30, once per slot, before close.
`--no-cognitive` explicitly selects the deterministic policy. Otherwise the
existing local LLM endpoint at port 8081 must return a validated SELECT decision
within eight seconds. The broker writer continues position management while
inference runs. Model name and credentials can be supplied with
`OMNI_LLM_MODEL` and `OMNI_LLM_API_KEY`; credentials are not logged.

Stop any superseded strategy process before starting a replacement. The new
writer lock prevents two OMNI writers in the same mode, but older processes
cannot honor that lock. Nothing in this implementation restarts existing
processes or places orders during unit tests.

## Fixed invariants

- Initial capital: 5000 USD. Maximum permitted equity loss from the initial
  capital or subsequent equity high-water mark: 225 USD. The halt is persistent.
- Maximum two global broker positions. Manual positions contribute exposure;
  only magic 100895 and previously registered strategy tickets are managed.
- Risk intent: 10 + 35 * (Q * S)^2 USD. Accepted risk stays within 10 to 45 USD,
  including stop loss and modeled round-trip friction. Lot rounding is downward.
- Effective friction: max(41 bps, live spread + configured commission +
  slippage allowance). Paper charges spread through bid/ask plus the remaining
  modeled cost. Live PnL is reconciled from broker deals and actual charges.
- A separate 15-minute portfolio standard-deviation cap defaults to 45 USD.
  `--sigma-budget` configures this statistical budget. It is not the stop-loss
  budget or a guarantee against a price gap.
- Immutable initial R; at 0.8R the stop locks 0.35R, at 1.5R it locks 0.80R.
  From 2.0R, trailing locks at least 1.5R using the asset's ATR. TP is 2.5R,
  increasing to 3.0R when completed-bar Kaufman ER exceeds 0.60. A position below
  0.20R after 24 bars exits at market. Stops never loosen.

SL brackets and the equity latch enforce the policy under available execution.
Broker outages, slippage and gaps can produce a realized loss beyond the floor;
the engine cannot create guaranteed-stop execution where the broker lacks it.

## Orderflow math

Completed MT5 M15 bars provide decimal log-return standard deviation over a
trailing 96-bar sample and true ATR. H defaults to 15 minutes; sigma_H is scaled
by sqrt(H / 15). Forming bars, future timestamps and stale histories are rejected.
Each book level contributes price * base quantity * exp(-abs(log(price / mid)) /
sigma_H). This preserves dimensions across assets. L2 imbalance is the weighted
bid/ask difference divided by their sum. Median/MAD normalization uses only prior
decision snapshots and persists across restarts; its first 24 observations carry
no invented anomaly score.

S = clip(0.25*B + 0.15*M + 0.20*W + 0.15*T + 0.10*L +
0.15*sqrt(max(B,0)*max(M,0)), 0, 1).

B, M, W, T and L are aligned with the candidate direction. W requires repeated
fresh observations of the same wall; rereading one cache generation adds no
persistence. T uses fresh, deduplicated, age-decayed aggressor prints. The
liquidation/stop pressure ratio compares projected exposure with observed book
depth inside the identical corridor. An uncovered corridor is unknown, not zero
depth or an infinite pressure ratio.

The existing Hyperdash historical `liquidationLevelsV2` and stop landscapes have
unverified prospective semantics. They remain visible but do not become
projected pressure inputs. Observed Hyperliquid wallet positions supply
liquidation prices, sizes and PnL; explicit stop triggers supply stop exposure.
Only two sampled whale wallets per asset are queried. Their exposure is a
lower bound, not the whole market. A verified complete upstream feed can provide
`PROJECTED_EXPOSURE` or `OBSERVED_STOP_ORDERS` with USD amounts and source times.
All unknowns remain explicit in the LLM snapshot. No LLM can change the broker
symbol, direction, risk, bracket, covariance or macro veto.

## Covariance provenance

The supplied parquet currently contains 14 assets, excludes NAS100/DJ30, and
lacks return-horizon metadata. It is preserved. A usable artifact requires a
matching JSON manifest with checksum, labels, decimal-log-return units,
15-minute horizon, creation time, training data end and expiry. Pandas index
labels require an explicit `label_column` in that manifest.

When the supplied matrix cannot be validated, the engine fits a separate
`ledoit_wolf_covariance.omni.parquet` from aligned completed MT5 returns, with at
least 48 common observations, and writes its manifest. Missing symbols/history
remain vetoed. No correlations are fabricated for uncovered assets.

Portfolio variance = signed_notional' * covariance * signed_notional.
The candidate's quadratic incremental variance is solved for its largest
admissible size, then broker lot rounding and variance are checked again.
Outstanding stop losses and costs also reserve room above the equity floor.
Broker CFD profit/margin calculators value each proposed lot.

## Uplift model

Second-position candidates are logged even when the model vetoes them. The
target is accept-branch final net equity minus reject-branch final net equity
over six hours. Both branches manage the identical initial existing book;
only the accept branch adds the candidate. This is a fixed-book marginal
estimand; it does not claim to estimate later opportunity replacement or a
randomized causal treatment effect.

The engine records sampled quotes for diagnosis. Sampled replay can train a
research model, but cannot qualify it for live use. Export full historical MT5
bid/ask ticks for execution-realistic labels:

```text
python -m Terminal.Export_MT5_Ticks --episodes Data/Omni/live/uplift_episodes.jsonl --output Data/Omni/live/full_ticks --account-id ACCOUNT_LOGIN
python -m Terminal.Uplift_Model label --episodes Data/Omni/live/uplift_episodes.jsonl --ticks "Data/Omni/live/full_ticks/*.parquet" --output Data/Omni/live/uplift_labels.jsonl
python -m Terminal.Uplift_Model train --labels Data/Omni/live/uplift_labels.jsonl --output Data/Models/omni_uplift
```

LightGBM learns positive uplift and a separate net-expectancy regression. A
chronological 60/20/20 train/calibration/test split purges overlapping outcomes
and adds a six-hour embargo. Training requires at least 200 retained training
episodes and 40 episodes in each later fold. Probability is calibrated on the
middle fold. The live gate requires probability at least 0.60 and expectancy
above the calibration residual buffer. Promotion also requires at least 40
nonoverlapping selected test episodes, at least ten selected decision days,
and a positive lower daily-block-bootstrap mean. Full tick provenance is
mandatory. Failed validation, stale artifacts, schema/hash errors or no model
veto the second position. No qualified uplift artifact existed at implementation.

Models are versioned on disk and read at startup. Restart the engine after a
new qualified artifact is produced; the persistent position/intent state survives.
Model fitting does not autonomously loosen any risk invariant.

## Macro, state and recovery

Macro blackouts use dated CPI/NFP/FOMC events, including DST-aware conversion
from Eastern Time. The seed calendar covers October 2026, verified against BLS
and Federal Reserve calendars. The background intelligence worker attempts a
daily refresh from BLS ICS and Fed monthly pages. If those providers fail,
existing dated coverage is retained; entries halt when verified coverage ends.
RSS sentiment is scoped by asset and age and remains a weak keyword feature.

State saves use atomic replacement and fsync. An intent is persisted before
dispatch. A broker timeout or missing acknowledgement reserves exposure and
is never blindly retried. Only an explicit INVALID_FILL result permits a fill
policy retry. Partial fills retain their actual filled volume. Inventory
read errors never imply a flat account. Ambiguous sends require reconciliation
with broker inventory/deal history before exposure is released.

Decision, execution, outcome, quote, model-episode and data-error ledgers live
under `Data/Omni/paper` or `Data/Omni/live`. Own positions retain immutable
initial R and original evidence; exits attach broker-net outcomes to cognitive
memory. A latched drawdown requires explicit operator recovery after review;
no autonomous equity rebound clears it.

## Validation

Run the broker-free engine tests plus existing governance, microstructure and
execution fixture tests. No test connects to MT5 or places an order.

```text
python -m pytest Tests/Test_Omni_Engine.py Tests/Test_Quantitative_Governance.py Tests/Test_Microstructure.py Tests/Test_Gates.py Tests/Test_Blueberry_Fixture.py -q -p no:cacheprovider
python -m pytest Tests/Test_Omni_Execution.py -q -p no:cacheprovider
```

These checks verify mechanics, causality and failure behavior. They do not
establish profitability. New L2/L3 alpha needs point-in-time historical replay
and an untouched forward paper period before its equity curve can be assessed.
