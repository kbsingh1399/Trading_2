# Astra microstructure and dual-engine forensic findings — 2026-10-09

Read-only review of the current primary checkout at `C:\Users\SIGMA\Documents\Trading_2`. This is a methodology/code audit, not live trading surveillance or an order authorization. Graphify queries and existing node explanations located the relevant symbols; scoped AST/source slices verified the current source citations. The graph contained 8,230 nodes when inspected, so earlier node counts should be treated as historical metadata. The named `Engine/forex_engine.py` and `Engine_2/forex_engine.py` do not exist here. `OF_Strategy.py` is a CLI delegating to `AI15mMT5Trader`.

Applied guidance: `.agents/skills/graphify/SKILL.md`, `.agents/skills/backtesting-trading-strategies/SKILL.md`, and `.agents/skills/systematic-debugging/SKILL.md`. The graphify path named in AGENTS is stale; the repository skill exists. No ToolSearch/ruflo tools were exposed to this reviewer. No production module was imported or changed. Behavioral probes compiled selected AST definitions into isolated in-memory namespaces and supplied synthetic inputs. They demonstrate function behavior, not active live exploitation or profitable strategy performance.

The latest scoped memory entry records a stand-down at 14:12 UTC; it supersedes earlier always-on execution instructions for this audit. Runtime/state verification is handled by the parent reviewer. This document is under `docs/reviews/`, outside the telemetry daemon's explicit `docs/audits/` auto-stage path.

## Main finding

The written five-pillar, passive-only, VWAP dual-engine policy is not implemented end to end by the current local trader. Several current guards correctly reject missing observed risk coverage. That refusal should not be weakened by relabeling modeled stop/liquidation exposure or anonymous L2 as observed orders. First repair time/provenance defects and reconcile the strategy policy; then evaluate any explicitly modeled alternative through a separately versioned causal replay.

## Evidence capability matrix

| Claimed pillar | What the inspected code actually provides | Implication |
|---|---|---|
| Session VWAP / Z | Telemetry derives session VWAP from MT5 bar volume/tick counts; the local trader computes a rolling last-96-bar VWAP and does not route on VWAP Z. | Broker activity proxy and session geometry must be typed separately; they are not a futures exchange's true traded-volume VWAP. |
| CVD absorption | Telemetry's crypto CVD is completed Binance one-minute kline taker quote volume; the bus can calculate 1/5/15-minute trade deltas. The local feature model mainly uses a 60-second exponentially weighted tape imbalance. | Aggressor flow is observable, but the present absorption gate is not price-local and cannot establish a defended shelf by itself. |
| L2 / L3 walls | Binance top-20 L2 is anonymous aggregated price levels. Factory and telemetry explicitly emit empty L3. Wallet-attributed L3 is accepted only through a distinct receipt contract. | Repeated anonymous depth samples do not identify wallets or prove continuous order persistence. |
| Liquidation pools | Current factory/telemetry return unavailable projected exposure. A separate OI-cohort research model exists. Public forced-liquidation prints are executed events. | Exposure, execution, reconstruction and missing coverage must remain different types. |
| Stops / profile | Current live stops are unavailable. The volume profile puts each broker bar's entire volume at its high/low midpoint. Research stop bands are heuristic scores derived from swings/ATR/profile/round numbers. | Neither midpoint-volume profile nor structural swing score reveals hidden stop sizes or queues. |

Relevant producers: [factory payload](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/factory.py:251), [telemetry missing exposure](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/generate_telemetry_snapshot.py:623), [telemetry L2 identity](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/generate_telemetry_snapshot.py:704), [profile approximation](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/generate_telemetry_snapshot.py:246), [provenance guards](C:/Users/SIGMA/Documents/Trading_2/Terminal/Telemetry_Provenance.py:36).

For non-perpetual instruments, the exporter explicitly emits `NOT_APPLICABLE` for perpetual exposure. There is no Binance futures order book for the broker's EURUSD, USDJPY, gold, oil or index CFD instrument. A distinct venue proxy, if proposed, requires declared basis, contract, timestamp and applicability rules; it is not direct observation of that broker's order inventory.

## F1 — P1: Stale source books are rejuvenated by reads

[factory.py:239](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/factory.py:239) sets a default venue timestamp and then overwrites `book.received_at = now` on every payload construction. [Risk_Sizing_Engine.py:156](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:156) prefers that receipt for freshness; its separate venue-time condition rejects future observations, not old observations.

Isolated reproduction: book timestamp `as_of - 500`, receipt `as_of`, policy maximum age 10 seconds. `OrderflowModel.features` returns features instead of `book_stale_or_future`. It still reports `coverage_missing=True`; the later missing-corridor veto can prevent an entry in this synthetic case. This establishes a stale-data gate defect, not that an order was placed.

Fix provenance at ingestion:

```text
on network/book event:
    observed_at = venue event time
    received_at = local transport receipt time
    sequence = venue sequence/update identifiers, if supplied
on payload read:
    preserve observed_at and received_at
    assembled_at = decision/read time
fresh = -allowed_skew <= t - observed_at <= max_event_age
        and 0 <= t - received_at <= max_receipt_age
        and sequence_state_is_valid
```

Never use assembly time as evidence of a new observation. The same stale-read issue affects wall measurements: [_WallTracker.observe](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/factory.py:44) uses its `now` argument, without checking that the underlying book contains a new event. Replaying one unchanged old book at ten-second intervals produces a returned 200-second wall span and a fresh-looking `observed_at`, even though the book is 200 seconds old.

## F2 — P1: Bus CVD admits future events; duplicate identity is not enforced

[bus.py:187](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/bus.py:187) and [bus.py:199](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/bus.py:199) only require `event_time >= window_start`; neither requires `event_time <= as_of`. [factory.py:250](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/factory.py:250) filters future `recent_trades`, but `orderflow = bus.snapshot(asset, now)` uses the unfiltered bus computations. Thus one field's quarantine does not protect the other.

Reproduction: publish a BUY of 10 units at 100 at time 1010, query at time 1000. Both one-minute CVD and taker BUY USD return 1,000. [publish_trade](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/bus.py:119) rejects timestamp regressions but allows identical timestamps; it stores trade IDs without deduplicating them. A reconnect replay at the same timestamp can therefore be counted again.

Proposed contract:

```text
accept each (venue, instrument, trade_id) once
quarantine future events before mutating any feature state
CVD_v(w,t) = sum(side_i * price_i * base_size_i)
             over t-w < event_time_i <= t, for venue v only
```

Retain venue and instrument in CVD/footprint records. Current `state.cvd` stores only `(timestamp, signed_usd)`, so later filtering cannot separate spot from perpetual flow or distinguish venues. Summing several venues is an explicitly modeled composite, not an interchangeable direct feed. Missing windows/transport gaps should have coverage status; zero is not a substitute for unavailable evidence.

## F3 — P1: The router implements pullback/breakout, not the specified dual engines

The protocol requires mean reversion at `abs(VWAP Z) >= 2` and trend continuation inside that range, with EMA200 slope and 0.10–0.60 ATR pullbacks. [classify_sleeve](C:/Users/SIGMA/Documents/Trading_2/Terminal/Orderbook_Structure.py:170) instead uses liquidity vacuum or efficiency ratio/tape thresholds; everything else is S1. There is no VWAP Z/RSI/EMA200 classification in this function or the local feature model.

[Omni_Trader.py:773](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:773) then forces T1 into `market` mode even when the configured entry mode is `limit`. [entry hierarchy](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:797) scans up to 2.5 ATR below/above the quote. This differs from both passive-only entries and the specified shallow trend shelf constraint.

Reproduction: a feature vector carrying `vwap_z=-3`, bullish tape 0.5 and efficiency ratio 0.5 returns `T1_BREAKOUT`. The supplied extreme-Z value is ignored. This does not prove that such a candidate reaches dispatch; other gates can refuse it.

Implement one sealed causal feature vector and explicit outputs for both engines:

```text
valid bars: open_time + bar_duration <= as_of
session: predeclared UTC/exchange-session anchor and calendar
VWAP = sum(weight_i * typical_price_i) / sum(weight_i)
sigma² = sum(weight_i * (typical_price_i - VWAP)²) / sum(weight_i)
Z = (fresh_signal_mid - VWAP) / sigma, only when estimator is valid
slope = (EMA200_j - EMA200_(j-k)) / (k * ATR_j)

MR_LONG eligible = Z <= -2 and RSI < 30 and measured exhaustion/support
MR_SHORT eligible = Z >= 2 and RSI > 70 and measured exhaustion/resistance
TF_LONG eligible = abs(Z) < 2 and slope > 0 and bullish context
TF_SHORT eligible = abs(Z) < 2 and slope < 0 and bearish context
planned_shelf_offset_ATR = side * (fresh_mid - entry_shelf) / ATR
TF shelf admissible = 0.10 <= planned_shelf_offset_ATR <= 0.60
```

Define actual retracement from the preceding impulse separately from planned shelf distance; these two quantities need not agree. Do not quietly change the meaning of the 0.10–0.60 ATR parameter between telemetry, review and execution. Missing/degenerate sigma or inadequate warmup is `UNKNOWN_GEOMETRY`, not `Z=0`. Emit both engine verdicts, each with measured/model/unknown inputs and veto reasons. Within-range Z is eligibility for evaluating the trend engine, not sufficient evidence to trade.

The present VWAP producers also differ: [local pivots](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:38) use a rolling 96-bar window; [CandleIndicatorEngine](C:/Users/SIGMA/Documents/Trading_2/Terminal/Candle_Indicator_Engine.py:167) computes a daily UTC session, while [active VWAP](C:/Users/SIGMA/Documents/Trading_2/Terminal/Candle_Indicator_Engine.py:201) falls back to rolling VWAP before eight session bars. The exporter explicitly uses session VWAP. Use explicit estimator identity and volume units so these cannot be treated as the same Z. Two standard-deviation bands do not establish normality, a 95% probability, or an optimal fade threshold.

## F4 — P1: Structural target absence falls back to fixed R

[Omni_Trader.py:901](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:901) passes only verified L3 clusters above a 2 million USD threshold to `structural_exit`. It does not pass the reconstructed liquidation/stop targets specified by the protocol, or even its available VWAP magnet parameter. [structural_exit.py logic](C:/Users/SIGMA/Documents/Trading_2/Terminal/Orderbook_Structure.py:133) initializes `hurdle_r=2.50`, mode `ratchet_band`; absence of an anchor still yields a TP.

Reproduction: entry 100, stop 99, no overhead cluster/magnet, friction 0.1R returns TP 102.50 with no veto. An overhead wall can reduce the target to the 1.5R net policy floor, also differing from the written 2.0–2.5R structural requirement. A wall beyond the cap can leave the target at fixed R without coinciding with that wall.

Proposed target planner:

```text
anchors = observed opposite-side depth clusters
          + explicitly permitted modeled structural target zones
          + sampled-wallet liquidation/trigger observations, with coverage
remove anchors on wrong side, stale anchors and incompatible venue bases
sort valid profit-side anchor fronts by signed distance from entry
select first material intervening obstacle/target; do not skip a blocking wall
TP = front edge minus side * buffer; round conservatively to broker tick
net_R = (signed broker-profit-to-TP - all expected costs) / initial_stop_loss
if no valid anchor: NO_STRUCTURAL_TARGET
if target fails policy/broker minimum-distance constraints: veto
```

Preserve the selected anchor's source/type/price bounds/coverage in the sealed plan. A farther modeled squeeze pool does not justify placing a TP through a nearer opposing wall. Fit front-run buffers and minimum materiality on development data using actual venue tick sizes, volatility and observed queue behavior; 2 million USD is not established as a universal threshold. Modeled magnets should contribute uncertainty-aware target candidates, never guaranteed exits or hidden-location claims.

## F5 — P2: Wall aggregation and persistence semantics differ from the policy

[wall_clusters.py:45](C:/Users/SIGMA/Documents/Trading_2/Terminal/Orderbook_Structure.py:45) rejects each row below 150,000 USD before clustering. Two nearby persistent 80,000 USD rows therefore return no cluster, despite meeting the written 150,000 USD clustered threshold when combined. It uses the longest member persistence after aggregation, which is not necessarily the span during which the total qualifying cluster amount was continuously present.

The current L2 exporter correctly labels wall span `SAMPLED_ONLY_NOT_CONTINUOUS` and emits empty L3. Keep that correction. Snapshot repetition cannot establish wallet identity, stable order IDs, continuous quantities, or intent to spoof. At most it provides persistence of an anonymous sampled aggregate.

Compute cluster totals first, then apply the cluster threshold; record continuous event coverage and quantity survival separately:

```text
cluster_quantity(t) = sum(notional of eligible levels in fixed corridor at t)
threshold_span starts when cluster_quantity crosses policy threshold
reset span on threshold loss, sequence gap, stale transport or corridor migration
retention = current comparable quantity / admitted anchor quantity
cancel policy = retention < 0.50 or abs(mid-entry)/ATR > 2.0
```

The current [governor defaults](C:/Users/SIGMA/Documents/Trading_2/Terminal/Order_Persistence_Governor.py:65) use retention 0.40, anchored drift 3 ATR and unanchored drift 1.5 ATR. [Omni's general fallback](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:634) uses `max(6*ATR, 3%*mid)`. The stricter governor applies only to its registered orders. These are three distinct policies, not an implementation of one 2 ATR / 50% rule.

For a diff-book implementation, buffer events, reconcile a REST snapshot, enforce update continuity and reset on gaps using [Binance's official local-book procedure](https://developers.binance.com/en/docs/products/derivatives-trading-usds-futures/websocket-market-streams/How-to-manage-a-local-order-book-correctly). The current `parse_binance_depth` expressly parses a partial top-20 snapshot; do not incorrectly demand diff continuity fields from that different message contract. To study cancels/refills, add a correctly assembled diff stream rather than treating partial snapshots as a complete event history. Sequence-valid L2 still does not expose individual wallet orders. [Hyperliquid's L2 API](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint) similarly returns price-level aggregates.

## F6 — P2: Aggregate taker activity does not prove shelf absorption

[taker_delta_exhaustion](C:/Users/SIGMA/Documents/Trading_2/Terminal/Orderbook_Structure.py:274) compares nested 1-minute/5-minute deltas and calls 25,000 USD of same-direction taker flow absorption. It does not locate trades at the proposed shelf, test price response, or observe limit-side replenishment. Missing tape returns `UNVERIFIED_NO_TAPE`; [the local caller](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:789) vetoes only failed `ENFORCED` results. The remote path may refuse unknown tape, but the local gate itself is permissive.

Use disjoint windows and local response evidence:

```text
recent_pace = CVD(t-60,t) / 1 minute
prior_pace = CVD(t-300,t-60) / 4 minutes
long exhaustion: prior_pace < 0 and recent_pace > lambda * prior_pace
short exhaustion: prior_pace > 0 and recent_pace < lambda * prior_pace
local adverse flow = signed aggressor notional inside declared shelf corridor
price_response = adverse price movement in ticks during that flow
absorption evidence = substantial adverse local flow + limited adverse response
                      + contemporaneous same-side visible depth replenishment
```

For a long, aggressive sells trading into a bid shelf while price holds and bids replenish is evidence relevant to bid-side absorption. Taker buys lifting offers can corroborate recovery but alone do not prove that bids absorbed sells. Normalize flow and price response by asset/session/venue baselines rather than assume a universal 25,000 USD gate. [Cont, Kukanov and Stoikov](https://arxiv.org/abs/1011.6402) motivate studying order additions, cancellations and execution imbalance together; their US-equity empirical results do not validate these crypto/CFD thresholds.

If this pillar is mandatory, `UNKNOWN` must be an explicit veto at the common admission boundary. If a separate bar-only strategy is proposed for instruments without tape, version and validate it separately instead of calling its evidence five-pillar confluence.

## F7 — P2, research-only: OI revaluation creates phantom cohorts; liquidation formula is approximate

[factory.py:160](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/factory.py:160) converts OI contracts to current-price USD notional before [observe_oi.py:118](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/liquidation_engine.py:118) differences it. Constant 100 contracts with price 100 then 110 yields a new 1,000 USD cohort, split 750 long / 250 short when taker-buy ratio is 0.75. No new contract was created in that reproduction.

Difference contract/base units first: `delta_contracts = contracts_t - contracts_(t-1)`; only then value the change with a declared price and contract multiplier. Separate revaluation: `delta_notional = multiplier * (price_t*delta_contracts + contracts_(t-1)*delta_price)`. Treat the second term as valuation change.

Even corrected net OI change cannot identify every new entry, leverage, collateral, side concentration or closure. Every new futures contract has a buyer and seller and OI conventionally counts one side, as [CME explains](https://www.cmegroup.com/trading/about-volume.html). A taker ratio does not divide newly created market-wide contracts into actual long versus short inventory. Use a latent scenario model constrained by `opens - closes = delta_contracts`; publish leverage/entry/closing assumptions and intervals rather than observed position dollars. Starting cohorts only after the first observed OI sample also leaves pre-existing exposure unmodeled.

[liq_price.py:61](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/liquidation_engine.py:61) uses `entry*(1 - 1/L + mmr)` for longs and its short mirror, despite describing itself as an exchange formula. Under the restricted assumptions of one isolated linear position, collateral `entry*quantity/L`, no fees/funding/additional collateral, and maintenance `mmr*quantity*liquidation_price`, the algebra is:

```text
long_liquidation = entry * (1 - 1/L) / (1 - mmr)
short_liquidation = entry * (1 + 1/L) / (1 + mmr)
```

At entry 100, leverage 10 and maintenance 0.004, the current approximations yield 90.4 / 109.6; the restricted equations yield 90.36144578 / 109.56175299. Actual venue margin tiers, cross equity, funding and other positions require venue-specific state. [Hyperliquid's documented formula](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations) depends on margin available and maintenance leverage; changing unrealized PnL/funding can change a reported threshold. Its sampled-user [clearinghouse state](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals) is a legitimate limited observation when transport and timestamp are attested, not a full-market liquidation map.

These research modules are explicitly excluded from the current production payload. Fix them before using their predictions, not by enabling their outputs to satisfy missing live pillars.

## F8 — P2: Realized liquidation prints overstate partial fills and mix time/side buckets

[parse_binance_force_order.py:94](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/streams.py:94) values original quantity `q` even for `PARTIALLY_FILLED`. Reproduction: `q=10`, filled cumulative `z=2`, average price 100 yields size 10 and 1,000 USD; observed cumulative fill is only 200 USD. [Binance's official message schema](https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-streams/market) distinguishes original quantity, last filled quantity and accumulated filled quantity. Its liquidation stream is a rate-limited snapshot, not every execution.

Use actual fill fields and a declared deduplication contract. If stable order identity is unavailable, preserve that limitation; do not silently infer a complete fill history or sum repeated cumulative quantities. Track realized events by `(venue, instrument, side, time bucket, price bucket)` and expire completed windows. [observe_forced.py:157](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/liquidation_engine.py:157) currently keys by price band alone, accumulates USD and overwrites side with the latest event; [empirical_bands.py:223](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/liquidation_engine.py:223) has no trailing-time cutoff despite calling these recent prints. Executed liquidations remain historical flow and cannot be reused as still-resting exposure.

## Structural/profile reconstruction changes

[StopClusterEngine](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/liquidation_engine.py:354) multiplies recency and `log1p(broker volume)` by 1,000, then emits those scores under `amount_usd`. That scale is a heuristic, not measured stop notional. Emit `structural_density_score`, provenance `MODEL`, and input bar availability; reserve USD fields for measured or explicitly calibrated probabilistic exposure. Require `bar_open + duration <= as_of` at the reconstruction boundary. Causal fractal pivots become available only after their right-side confirmation bars have closed.

Replace midpoint-only volume profiling with actual trade-price aggregation where available:

```text
V(price_bin, session) = sum(executed base quantity at prices in bin)
POC = bin maximizing V
value area = deterministic adjacent expansion from POC to configured volume fraction
```

Declare bin width, tie policy, session calendar and volume units. Broker tick-count weighting remains a broker activity profile proxy; OHLC plus total bar volume does not uniquely identify intrabar volume by price. For bar-only research, a distribution across the bar range may be a declared approximation, but it still cannot produce observed stop sizes. Swing/profile/round-number stop zones should be price hypotheses with uncertainty. Their inferred USD weights must not enter a measured fuel/depth ratio.

## Refinement of the proposed next model

The parent's proposed survival-weighted wall feature has a useful structure:

```text
wall_weight = USD * (1 - exp(-ln(2)*present_duration/h_build))
              * exp(-ln(2)*age_since_actual_observation/h_data)
              * P(survive_until_conditional_touch)
              * exp(-distance/sigma_price)
```

Its weak assumption is that the survival probability is currently identifiable. Sparse anonymous samples do not support a calibrated probability of cancellation versus execution, and build span, freshness decay and survival can count related age/coverage evidence repeatedly. Estimate survival only from a declared event history and a validated competing-risk model; otherwise emit `UNKNOWN` or justified bounds. Survival should be integrated over the conditional touch-time distribution, not evaluated at an arbitrary fixed horizon. Consumption by executions and pulling a wall are different events; replenishment and price response decide their interpretation.

An expected-value admission/TP criterion should use outcomes conditional on the broker limit actually filling:

```text
EU(plan | D) = P(fill | D, plan)
               * sum_o P(outcome_o | fill, D, plan)
                       * E(net_cash_PnL_o | outcome_o, fill, D, plan)
               - E(cancel/requote costs | D, plan)
```

Include stop, target and timeout outcomes, all costs, nonfills and adverse selection. Never estimate conditional win probabilities from an unconditional candle-touch backtest. A limit at the broker and a queue on a separate exchange have different execution semantics; use the broker's observed fill contract and basis. The role of queues, order flow and fees in execution choice is supported by [Cont and Kukanov's order-placement research](https://arxiv.org/abs/1210.1625), but its equity-exchange solutions are not direct broker-CFD fill models.

A model version that blends regime evidence near the Z boundary can compare `EU_MR` and `EU_TF`, while the current authorized version retains its explicit engine eligibility. Both versions must avoid compulsory entries merely because `abs(Z)<2`. Parameterized pullback quantiles by asset/session and fill-conditional utility are testable alternatives to universal thresholds; replacing the current 0.10–0.60 ATR policy requires an explicit policy revision and held-out validation.

Finally, observing full same-venue depth over the same target corridor repairs one FFR geometry problem, but selectively sampled wallet fuel and transient visible depth still do not establish total market demand or price impact. Report covered extent, sampling and refill uncertainty. Use FFR as a conditional descriptive feature until calibration demonstrates predictive value; do not transform it directly into TP-hit probability or an exact peak forecast.

## Recommended implementation and validation order

1. Repair event/receipt freshness, stale wall aging, future windows and replay deduplication. Keep missing coverage separate from neutral values. Validate event and receipt ages on the same sealed as-of clock.
2. Replace local S1/T1 routing with the explicit two-engine contract and passive entry enforcement. Reconcile the session VWAP estimator, shallow shelf metric, wall retention and drift policy across producer, evaluator and order manager.
3. Require a typed structural target; refuse a fixed-R substitute when the authorized strategy requires structure. Carry the nearest intervening depth obstacle and all net costs into target feasibility.
4. Correct research-only OI units, liquidation equations, stop-score units and realized-liquidation event accounting. Treat models as hypotheses; never use labels or default fields to turn missing observations into facts.
5. Run preregistered chronological replay with point-in-time event and receipt timestamps, missing-data episodes, queue uncertainty, rejected/nonfilled limits and broker costs. Compare both engines separately and jointly; retain all considered candidates and rejection reasons. Test wall-size/persistence/flow thresholds on development data, lock them before held-out evaluation, and report uncertainty rather than universal optima. Neither a static confluence score nor a 180-second wall span is a calibrated success probability.

Specific acceptance cases should include: old source/new read; a future trade; same-ID replay; two subthreshold members exceeding the cluster threshold together; a threshold crossing or feed gap resetting persistence; opposing flow without local absorption; both Z boundaries; valid in-range trend shelves; missing target; a nearer blocking wall; constant contracts/changing price; partial fills; opposite-side prints in the same price band; and delayed confirmation of a fractal pivot.

### Isolated verification results

| Probe | Current result |
|---|---|
| Book age 500s, receipt age 0s, policy max age 10s | Feature model accepted book; later coverage remained missing. |
| Same old L2 read every 10s for 200s | Two 200s sampled walls returned with updated observation time. |
| Trade timestamp 1010, query as-of 1000 | CVD and taker BUY each included 1,000 USD. |
| `Z=-3`, aligned tape/ER | `T1_BREAKOUT`; Z unused. |
| TP with no wall or magnet | Fixed 2.5R plan returned. |
| Nearby persistent 80k + 80k wall rows | Empty cluster list. |
| Constant 100 contracts, price 100→110 | New 1,000 USD OI cohort. |
| Force order original 10, accumulated filled 2, price 100 | Parser emitted 1,000 USD instead of filled 200 USD. |

No historical strategy backtest, full pytest run, live execution, service start/stop, Arena submission, remote publication, automation mutation, or repository parity synchronization was performed by this reviewer. Existing operational tests and prior win rates are not evidence that these newly demonstrated cases pass.

### Source fingerprints at verification (SHA-256 prefix)

```text
Terminal/OF_Strategy.py                              1e3322e957909897
Terminal/Omni_Trader.py                              08b308813b227958
Terminal/Risk_Sizing_Engine.py                        3e0c84c585b02d38
Terminal/Orderbook_Structure.py                      cfe4f0179813fb6c
Terminal/Order_Persistence_Governor.py               2d44491c7ae7132a
Terminal/Telemetry_Provenance.py                     c7017788ac0e532a
Terminal/Data_Factory/factory.py                     5768de8add37cfe6
Terminal/Data_Factory/bus.py                         32f3a6d32b52afe8
Terminal/Data_Factory/liquidation_engine.py          c518232cc019e00d
Terminal/Data_Factory/streams.py                     9bf60cd49de29802
Terminal/Data_Factory/generate_telemetry_snapshot.py 9dd66103da6934a4
Terminal/Candle_Indicator_Engine.py                  f857534451ede1f2
```
