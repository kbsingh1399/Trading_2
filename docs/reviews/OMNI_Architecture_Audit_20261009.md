# OMNI quantitative architecture audit — 9 October 2026

This is an audit and implementation blueprint, not a deployment or trading authorization. No production strategy, broker order, service, halt, or automation was changed. Findings refer to current source slices and isolated probes, not to the historical assurances in the briefing. The report is outside the telemetry publisher's explicit `docs/audits/` staging path.

## Review team and evidence

The coordinator traced policy, covariance, uplift, source versions, process state, and the requested entry point. Three independent reviewers investigated microstructure, the Arena/macro/verification chain, and risk plus cross-verification. The risk reviewer independently reproduced the dialectic reviewer's unsafe floor certificate. The reviewers challenged proposals before the final synthesis. Graphify queries navigated the existing graph; actual files supplied final line references. Applied methods: graphify, systematic-debugging, quant-analyst, backtesting-frameworks, and the reviewers' architecture/risk guidance. No ruflo tools were available.

The graph initially contained 8,229 nodes and was built at commit `7b2137ebeca6924595e0debcea664200f32c8269`. The checkout advanced during the audit; it is not a frozen release. An evidence manifest records source hashes and the telemetry context at 14:24:23 UTC: [evidence](C:/Users/SIGMA/Documents/Trading_2/docs/reviews/OMNI_Audit_20261009_evidence.json). A graph relationship is a navigation aid, not proof of runtime reachability or causal correctness.

Native MT5 evidence at 14:16:48 UTC verified account 5064568, USD currency, balance/equity 4,896.55 USD, margin 0, zero filled positions, and one USDJPY.pi buy limit, ticket 18736422, volume 0.12, entry 158.180, SL 158.040, TP 158.530. Nominal broker-valued stop loss was approximately 10.63 USD. Thus the nominal stressed cushion of 110.92 USD is explained by 4,896.55 − 10.63 − 4,775; it excludes a separate execution/gap stress reserve.

MT5 reported `trade_mode=0`, which equals the installed `ACCOUNT_TRADE_MODE_DEMO` constant. The server name containing Live does not establish real-money mode. [Official account-mode documentation](https://www.mql5.com/en/book/automation/account/account_real_demo_contest). This review does not silently treat demo execution as evidence of real-account fill quality.

The reported 17-trade basket spans October 7–9; it is not a verified single-UTC-day result. Matching all 17 named position IDs to 34 entry/exit deals gives 85.31 USD gross minus 1.89 USD commission and 0.31 USD swap, or **83.11 USD net**, 0.94 USD below the reported 84.05. The risk review found nine closed positions totaling 66.76 USD net on the raw October 9 broker date, and eight totaling 50.75 USD on October 9 UTC after the inferred three-hour timestamp adjustment. The timestamp convention must be established per broker session before production accounting. Aggregate by position ID, include entry and exit commission, fees, swap, and partial exits, exclude deposits, and distinguish UTC day from a selected strategy session. The briefing's 11/17 win rate, even if the selected basket is valid, has an approximate 95% Wilson interval of 41%–83% under an independent-binomial approximation; shared market exposure makes that approximation optimistic. It cannot identify optimal thresholds or prove alpha. [Broker reconciliation and isolated risk evidence](C:/Users/SIGMA/Documents/Trading_2/docs/reviews/ASTRA_20261009_risk_qa_evidence.json).

The latest snapshot denies new-risk authorization (`DENIED_UNVERIFIED_ORDERFLOW`), flags the calendar `STALE_REVIEW_REQUIRED`, and advertises 12 slots. Persistent state still records capital 4,841.23 USD rather than the fresh broker balance. `Engine/forex_engine.py` is absent from both primary and mirror; there is no honest source-level patch to that requested path yet.

The journal records a 14:12 UTC stand-down. Actual process inspection at 14:20:32 UTC still found the telemetry publisher and duplicate Heretic, Gemini, and graph-watch processes. No OF_Strategy/Omni_Trader execution process appeared in that inspection. This is a process-list observation, not proof that no other executable can trade. No process was stopped or started during this audit.

## Findings that precede alpha optimization

| Priority | Finding and consequence | Source |
|---|---|---|
| P0 | High-free-margin admission ignores existing pending risk and drops the 20 USD operating buffer. It can admit a book that fails both the hard floor and four-filled-position requirement. | [live_admission.py:85](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/live_admission.py:85), [relaxed reserve:105](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/live_admission.py:105) |
| P1 | Capacity has no canonical owner: council 4; RiskPolicy fixed 2; admission 6 with up to 12 pending; Arena and telemetry 12. Risk bands also differ between council 10–15, admission 10–20, and generic policy 10–45. The daemon's effective risk cap is 10 below equity 4,800 and otherwise min(20, policy cap), so generic 45 is not its effective live cap. Changing one limit does not migrate the system. | [protocol:86](C:/Users/SIGMA/Documents/Trading_2/docs/specs/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md:86), [RiskPolicy:37](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:37), [admission:13](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/live_admission.py:13), [Arena:282](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:282) |
| P1 | Re-reading a cached book stamps receipt time as now. The feature gate prefers that receipt stamp. Old source data can acquire fresh-looking age and apparent persistence. Future trades also enter bus CVD because its window has no upper bound. | [factory.py:239](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/factory.py:239), [features:156](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:156), [bus.py:187](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/bus.py:187) |
| P1 | The auditor can certify SKIP as pristine, unknown inventory as empty, pending risk as zero, and a cushion below the operating threshold as PASS. Its certificate is not a demonstrated causal/risk proof. | [aggregation:529](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:529), [telemetry audit:363](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:363), [broker floor audit:443](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:443) |
| P1 | The Arena bridge neither validates the denied/stale evidence envelope nor binds a response to a cycle. It can label failed MT5 initialization cash-flat, reuse old prose, and write historical account literals as fresh consensus. | [snapshot/defaults:174](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:174), [completion:738](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:738), [ledger:810](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:810) |
| P1 | The specified dual engine and structural TP rules are not the current daemon's complete routing logic. A breakout sleeve can force market entry; shelf search spans 2.5 ATR; missing verified L3 target depth falls back to a fixed-R target. | [sleeve/market selection:773](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:773), [shelf corridor:797](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:797), [TP inputs:901](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:901) |
| P1 | Labels use a fixed ratchet while live management uses a conditional policy. Session classification also maps class labels back to CRYPTO, so a GOLD session can become crypto US-hours. Qualifying the fixed-policy uplift model does not qualify this altered execution policy. | [policy versions:24](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:24), [class/session mapping:41](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:41), [live caller:540](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:540) |
| P1 | The publisher rebases remote changes into the working checkout, reloads modules, stages audits, and pushes to main. Evidence synchronization and executable deployment lack an explicit separation. | [remote pull:109](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/autonomous_telemetry_git_daemon.py:109), [publication:137](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/autonomous_telemetry_git_daemon.py:137), [reload:177](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/autonomous_telemetry_git_daemon.py:177) |

The strongest numerical counterexample used an in-memory bridge, not actual broker orders: equity/balance 4,800, free margin 3,000, four pending orders with nominal risk 10 each, and a proposed fifth with risk 10. The relaxed branch reserved only 14.50 USD and accepted post-loss equity 4,785.50. Reserving all five under that same 1.25 multiplier plus 2 USD per order gives 72.50 USD exposure and post-loss equity 4,727.50. Five simultaneous fills also exceed four filled slots. The no-free-margin branch rejected this same book. Existing narrow tests passed because their fake bridge omitted free margin and exercised the strict branch.

Other isolated probes reproduced stale 500-second books passing a 10-second feature policy, future trade inclusion, all-SKIP pristine certification, a 4,780 USD account receiving a PASS floor certificate, and failed MT5 initialization producing a flat/clean Arena briefing. These are branch-level proofs, not a full execution certification. Primary and mirror `.agents` check-only comparison initially found 29 byte mismatches and the final check found 133 as background graph caches continued changing. Both checks failed; neither establishes source-repository parity. The session audit entry was appended to both journals while preserving their pre-existing differences. No parity repair or bidirectional overwrite was performed. `safe_cmp` returning True after OSError is itself unsafe assurance. [parity helper:47](C:/Users/SIGMA/Documents/Trading_2/.agents/scripts/verify_and_sync_agents.py:47).

## Deliverable 1 — dual models, pullbacks, and whale persistence

The sound part of the dual-model idea is separating continuation from exhaustion. The unsound part is using abs(Z)=2 as if it identifies that distinction. A strong trend can remain above 2Z; a weak sideways market can remain inside 2Z. Do not force a trade because it is in range. Require both engines to be evaluated; permit HOLD when neither has positive conservative net expectancy.

Use a causal regime probability rather than a rigid Z boundary:

```text
p_trend = calibrated P(continuation regime | completed trend, volatility,
                       session, OFI, absorption, spread, basis)
EV_MR   = conditional net value of fading a tested exhaustion/sweep
EV_TP   = conditional net value of a continuation pullback
Choose the feasible engine with the greatest positive lower bound of EV.
```

An implementable initial model is a regularized logistic regime router plus separate shallow LightGBM conditional-return/fill models. Record Z continuously. Include slope of completed EMA200 in volatility units, price acceptance/rejection around session VWAP, aggressor activity relative to observed price response, wall cancellation/replenishment, and cross-venue basis. Training needs failed, rejected, and unfilled candidates too; analyzing only winning pullbacks creates selection bias. There is no local replay result here that establishes a profitable router.

For completed bars i, calculate per-bar log variance:

```text
GK_i = 0.5 * ln(H_i/L_i)^2 − (2*ln(2) − 1) * ln(C_i/O_i)^2
PK_i = ln(H_i/L_i)^2 / (4*ln(2))
v_t  = EWMA(GK_i) over completed bars
g_t  = a separate overnight/reopening-jump estimate
V_t  = current broker price * sqrt(forecast variance over the entry horizon)
d_normalized = abs(entry − reference shelf) / V_t
```

The forecast horizon must match the fill/holding question; multiplying variance by H assumes a time-scaling model and should be checked against returns dependence. Neither estimator supplies an alpha threshold. The diffusion assumptions make overnight gaps, session openings, discontinuous CFDs, and bad OHLC inputs material; retain gap stress and compare with realized-return estimates rather than silently replacing ATR. [Original Garman–Klass paper, including the high-low estimator](https://www.cmegroup.com/trading/fx/files/a_estimation_of_security_price.pdf).

Replace universal 0.10–0.60 ATR with conditional retracement quantiles and conditional utility by asset class, session, volatility bucket, trend strength, and spread/V_t. Shrink sparse asset-specific estimates toward sector estimates. Indices need explicit cash-open/reopen conditions; crypto needs weekend/funding and venue conditions. Quantiles must be learned from all causally generated opportunities, not just future winners. Evaluate the original band against wider/narrower bands on untouched chronological episodes. Do not call either band optimal before this comparison.

The entry objective is:

```text
J(level) = P(broker fill by TTL | state, level)
           * E(net PnL | fill, state, level)
           − stressed-loss penalty − risk/capacity opportunity cost
```

The fill-conditional term matters: a deep resting bid often fills precisely when the market is deteriorating. Broker CFD limits do not demonstrate exchange maker rebates, zero spread, or Binance queue priority. A buy limit triggers on the broker Ask and a sell limit on Bid. [Official MT5 order mechanics](https://www.metatrader5.com/en/terminal/help/trading/general_concept). A prudent replay must model fill/price-path dependence, not independent fills and returns. [Adverse-selection simulation research](https://arxiv.org/abs/2409.12721).

For whales, 150,000 USD and 180 seconds are candidate research parameters, not proof against spoofing. An aggregated Binance price level is not an individual wallet order; replacement liquidity at the same price can appear persistent. Require genuine order identity for L3 claims; otherwise label the feature persistent L2 depth.

Use separate age and survival terms:

```text
W_effective = W_usd
  * (1 − exp(−ln(2) * continuously_observed_age / h_build))
  * exp(−ln(2) * time_since_actual_receipt / h_data)
  * P(order survives until projected touch | state)
  * exp(−distance_in_price / V_t)
```

Reset/censor persistence on sequence gaps, feed loss, order replacement, or cancellation. Never build persistence from repeated reads of one cached snapshot. Model cancellation and execution as competing events; executed absorption can be supportive evidence rather than cancellation. Test exponential survival against Weibull or a power-law tail using held-out likelihood, survival calibration, and conditional trade utility. A power law is not automatically better. Set size thresholds by asset/session depth percentiles and relative corridor participation, not one nominal USD threshold across BTC, metals, and indices. Replenishment after aggressive hits and realized short-horizon markout are stronger tests than elapsed presence alone.

Challenge/rebuttal refinement: the current sparse anonymous L2 samples cannot identify the displayed survival probability. Until sufficient sequence-valid event histories exist, output UNKNOWN or defensible probability bounds; do not insert an invented point estimate. The conditioning horizon is time until the candidate level is touched, which is itself state-dependent. In a fitted implementation, do not count the same age/coverage information repeatedly through build-age, freshness, and survival multipliers. Fit the incremental contribution of each term jointly. FFR remains descriptive when sampled-wallet fuel coverage is selective or resting depth can replenish; complete corridor geometry alone does not calibrate cascade probability.

Event OFI should include additions, cancellations, and aggressive depletion rather than relying only on a static top-20 ratio. The empirical link between OFI and price impact is supported in stock data; transferring it to these CFDs and proxy venues requires validation. [Cont, Kukanov, Stoikov](https://arxiv.org/abs/1011.6402).

## Deliverable 2 — evidence-bound debate and arbitration

The bridge currently places four personas in one Arena prompt. That is not evidence of four independent agents. The headless swarm's three deterministic perspectives are useful checks but share inputs. The CDP cycle uses a 120-second wait, not the documented four minutes, and accepts text without a cycle identity. The local hardcoded 4,000 USD margin text also helps create the margin misconception attributed to Arena. Fix the information contract before trying more persuasive prompts.

Each cycle should have an immutable evidence bundle and a versioned policy envelope. Store both UTC event time and immutable receipt time, source/venue/sequence, unit, coverage, observed-versus-derived label, feature computation version, and references to archived raw receipts. For each derived feature, preserve input hashes. A valid receipt proves provenance of an observation, not the truth of a trading interpretation.

```json
{
  "schema": "omni.council.v1",
  "cycle_id": "UTC_SLOT_AND_NONCE",
  "evidence_sha256": "HASH_OF_ARCHIVED_BUNDLE",
  "policy_sha256": "HASH_OF_CANONICAL_POLICY",
  "as_of_utc": "RFC3339",
  "expires_at_utc": "RFC3339",
  "candidate_id": "OR_BROKER_TICKET",
  "action": "KEEP_PENDING",
  "claims": [
    {"evidence_ref": "book.sequence", "test": "wall_survival", "result": "PASS"}
  ],
  "invalidation_refs": [],
  "missing_evidence": [],
  "uncertainty": "UNQUALIFIED_MODEL"
}
```

Reviewers first analyze the shared bundle without Arena's opinion. The coordinator then sends one specific contrary claim to the relevant reviewer for a bounded challenge/rebuttal round. Preserve dissent. Re-query only the disputed source if needed; archive the new receipt and reissue the evidence digest. Missing and late reviews remain explicit. Multiple agent opinions derived from one L2 observation do not multiply the observation's statistical weight.

Challenge/rebuttal refinement: an intact :25/:55 evidence hash does not make four-minute-old L1/L2 data executable at :29/:59. Preserve the original deliberation bundle and record a separate fresh broker/orderflow/macro revalidation bundle before action. Compare material state changes to predefined tolerances; changed or expired proposals return to review or HOLD_VALIDATION. Do not silently attach fresh timestamps to an unchanged analysis. A high probability score also cannot replace value: 90% probability of gaining 1 USD and 10% of losing 20 USD produces a 90/100 score but an expected loss of 1.10 USD.

The existing headless contract offers a starting seam for candidate/digest binding and numeric/reference validation. Extend it for KEEP_PENDING, DELETE_PENDING, HOLD_POSITION, EXIT_POSITION, SELECT_NEW, and HOLD_VALIDATION; migrate its two-slot default. [llm_contract.py:66](C:/Users/SIGMA/Documents/Trading_2/Terminal/Headless/llm_contract.py:66). Numeric echoes alone do not verify profitability.

For a thesis-valid state V:

```text
Posterior odds(V | unique evidence) = prior odds(V) * joint likelihood ratio
Score = 100 * calibrated P(incremental net PnL > 0 | evidence, action)
U(a) = E(incremental net equity from action a)
       − lambda * expected shortfall(loss_a)
       − opportunity cost − uncertainty penalty
```

Estimate a joint model or grouped source features, not independent likelihood ratios for correlated pillars or repeated summaries. Arena's opinion gains a weight only if it adds predictive value conditional on the raw evidence, measured on held-out cycles. A probability score is not expected value: rare large losses can outweigh frequent small wins. Execution additionally requires a positive lower confidence bound of the relevant utility difference and every deterministic gate. There is no justified universal score threshold such as 80 or 90 from the current sample.

| Conflict | Deterministic result | Comparison after validity passes |
|---|---|---|
| Arena DELETE; local support intact | Denied/expired new-risk evidence cannot authorize a new placement. Existing ticket is audited separately. | KEEP value = fill probability × conditional net outcome less contingent-risk opportunity cost; compare with DELETE and alternatives. |
| Arena EXIT; local support intact | Emergency floor, invalid protective stop, or mandatory blackout policy dominates model opinions. | Compare future HOLD versus EXIT from current executable mark; entry price and prior losses are sunk. |
| Local wall pulled; Arena optimistic | A verified predefined invalidation can win; a single noisy depth change is not automatically the whole thesis. | Re-measure sequence-correct depth, depletion versus execution, price response, and continuation value. |
| Broker inventory unknown, bundle mismatch, or stale calendar | HOLD_VALIDATION for new risk; deterministic protective management follows its separate verified broker route. | No scoring override. Unknown data alone does not automatically prove an existing order should be deleted or a position panic-closed. |

Measure cancellation, hold, and exit counterfactuals on the same future quote path. A subsequent winning trade does not prove keeping it was optimal; a subsequent stopout does not prove Arena was right ex ante. Reject a biased protocol that always requires rebutting DELETE while never requiring rebutting KEEP.

## Deliverable 3 — honest stop/liquidation reconstruction and TP selection

Arena's observation that public retail stop inventory is unavailable is correct. It does not prohibit useful latent-liquidity estimates, but those estimates must not be renamed observed stops. POC/VAH/VAL, pivots, equal highs/lows, and round numbers describe public price/volume structure. They do not identify exact stop volume, leverage, or cross-margin liquidation thresholds. Net OI alone also cannot uniquely tell which side initiated new positions.

Current live math deliberately excludes synthetic liquidation bands and uses verified sampled-wallet stops. [Risk_Sizing_Engine.py:210](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:210). This is a sensible provenance boundary; retain it while improving a separately labelled research estimator. The sampled-wallet coverage is not the market's full inventory.

The review found a research OI accounting flaw: changing price with unchanged contracts creates an apparent notional OI increase. Maintain base-contract quantities. If only USD OI is available, a first-order correction is:

```text
quantity_innovation_approx = (ΔOI_usd − OI_usd_previous * ΔP/P_previous) / P
```

Use actual quantity differences when available, contract multipliers, timestamps, resets, and matched price vintages. Treat remaining side/leverage allocation as latent. Also deduplicate liquidation updates and use incremental executed quantity, not original order quantity, when estimating realized forced flow. The isolated q=10/z=2 probe showed a fivefold overstatement when original quantity was used.

Construct probability-weighted corridors rather than point walls:

```text
latent_fuel_d(p) = sum over cohorts j of
  P(side_j=d | observed state) * exposure_j
  * probability_density(liquidation_price_j=p | margin/leverage uncertainty)

friction_d(corridor) = observed executable opposing depth in that corridor
FFR_d = estimated forced-flow fuel in corridor / measured opposing corridor depth
```

Unknown leverage, account collateral, hedging, maintenance-margin tiers, funding, and cross-margin transfers require uncertainty bounds. Prefer venue-reported wallet liquidation prices where verifiable; do not apply isolated-margin shortcuts to cross-margined portfolios. Distinguish marked position notional from incremental market-order flow under partial liquidation.

A 20-level book cannot measure absorption to a distant target it does not cover. Require corridor coverage at both endpoints and a fresh sequence-correct book; otherwise FFR is UNKNOWN or an explicitly censored research estimate. Small denominators and extrapolated liquidation pools do not establish explosive cascades. Fit hit/absorption probabilities by regime; FFR=1.5 is not a universally calibrated 72% probability.

Map proxy venue prices onto the broker with a backward-looking synchronized basis model, for example P_broker = a_t + b_t * P_source plus residual uncertainty. Refit by asset/session; retain basis/dislocation vetoes. HIP-3 synthetic liquidity, Binance perpetual liquidity, exchange futures, and Blueberry CFD quotes are distinct venues. A source liquidation band cannot be used as an exact broker TP price without this mapping.

For a long target p before opposing absorption:

```text
V_TP(p) = P(broker Bid reaches p before adverse exit | state)
          * net payoff at p
          − expected adverse-exit loss − execution/tail penalty
```

Reverse executable sides for shorts: closing a short requires Ask reaching TP. Select a feasible tick-rounded target maximizing a conservative bound of V_TP; use wall/cascade intervals to propose candidates, not to guarantee the future peak. Fit the front-run buffer from executable-side spread, basis residuals, observed overshoot/absorption, and horizon volatility. If every defensible structural target yields less than the required net reward/risk, reject or redesign the entry/stop; do not invent a farther target to obtain 2.5R on paper.

## Deliverable 4 — cost-aware ratchets and conditional drawdown

The proposed 0.15R first lock cannot establish net breakeven. With entry E, initial price risk R, volume q, and a linear USD contract multiplier c:

```text
gross lock value = q*c*0.15*R
stress friction reserve = q*c*E*0.0041
0.15R clears the 41 bps model only if R/E >= 0.0041/0.15 = 2.7333%
```

Use broker-valued profit for non-USD or nonlinear contracts. For the cited SP500 entry 7,791.50, initial R=13, volume 0.10, contract multiplier 10, the lock is 1.95 USD while the 41 bps reserve is 31.945 USD. Gross TP reward 26.50 USD also fails that reserve. For ETH entry 2,494.50, initial R=17, volume 0.70, contract multiplier 1, the lock is 1.785 USD versus 7.159 USD reserved friction. These are contradictions under the stated conservative cost model, not claims that actual broker commission equals that reserve.

Keep one accounting convention: an actual Bid/Ask replay already incorporates spread; do not subtract that spread a second time as an expected cost. Explicit commission, swap, and slippage remain separate. A conservative 41 bps reserve may be retained as a stress floor, but must be identified as a reserve, consistently enforced, and reconciled against actual fills. Passive broker orders do not erase the spread. [MT5 mechanics](https://www.metatrader5.com/en/terminal/help/trading/general_concept).

No ordinary stop guarantees execution price in a gap. A stop moved into profit still has modeled downside under adverse fill, fees, swap, and counterparty/execution risk. Separate filled-position count, collateral use, stress loss, and statistical covariance. A locked position consumes a filled slot until it closes. Never fund new downside exposure using assumed future stop-profit credits.

Compute a desired stop by inverting broker-valued net PnL, not by assuming price × contract is USD:

```text
required_gross_profit = booked trade costs + remaining cost stress + desired_net_lock
desired_SL = inverse_broker_profit(entry, volume, required_gross_profit, direction)
```

Before submitting, require a tick-valid level beyond stops/freeze restrictions, tighten monotonically, and verify the broker acknowledgement plus fresh position SL. Preserve initial R immutably. A new tighter SL is not a new initial R.

Neither 0.50R friction-only nor 0.80R first lock is established as optimal. The useful question is the post-trigger distribution of retracement before another expansion, conditional on sleeve/session/volatility. Estimate conditional drawdown quantiles after reaching a trigger, including failures and gap exits. Compare baseline .8→.15, .8→cost-aware lock, .5→friction-only, and volatility/structure trails on the same untouched tick episodes. Optimize net expectancy and tail loss, not the count of small positive exits. Earlier locking can increase win rate while reducing PnL.

At a price jump directly above multiple stages, evaluate every eligible stop level and choose the tightest feasible one in a single cycle. The separate ratchet manager's if/elif transition takes multiple polls to advance stages. For a long, a proposed structure trail is max(prior_SL, executable_Bid − k*V_t, eligible net-lock levels), followed by feasibility checks; use min and Ask for a short. k and trigger bands require validation. Never loosen an existing broker stop to satisfy a newly recomputed model.

Time decay needs an explicit definition: exit after six hours if maximum executable-side favorable excursion never reached 0.20R, or exit if current gain is below 0.20R after six hours. Those are different policies and must share the same replay/live implementation. Neither a forming candle high nor a midpoint-only touch proves an executable gain.

## Deliverable 5 — concrete integration blueprint

### One policy and one submission owner

Create a canonical versioned policy. For this latest council proposal: four filled slots, nominal risk 10–15 USD as specified by its Gate 6, operating floor 4,795, hard floor 4,775, original capital 5,000. Preserve the prior defensive 10 USD cap below 4,800 unless a superseding operator policy changes it. Document whether the per-trade band is nominal stop risk or total stressed loss; the sizing and capacity optimizer should use total reserved loss. Carry the policy hash into every request, model artifact, receipt, and audit. A mismatched policy is a veto, not a warning.

Pending orders need not appear as filled positions in the UI, but they must reserve loss and potential filled capacity. Without verified atomic broker-supported mutual exclusion, an arbitrary number of resting limits plus a hard four-filled cap are incompatible: several can fill before a local cancellation loop runs. Give each active fill-capable order an admission reservation. Initially enforce filled + independently fillable pending + unresolved intents + proposed <=4. More working orders require a proven mutually exclusive group or a broker-side mechanism; post-fill cleanup is not proof.

```python
# Proposed interface, not installed production code.
def admit(bundle, proposed, policy, writer):
    with writer.account_lock(policy.account_id):
        account, positions, pending, intents = writer.reconcile_native_inventory()
        require_known_usd_account(account, policy.account_id)
        require_policy_and_evidence_hashes(bundle, policy)
        require_no_halt_or_entry_blackout(account, bundle, policy)
        book = positions + pending + unresolved_fill_intents(intents) + [proposed]
        require(max_simultaneous_filled(book) <= policy.max_filled)
        # Mark-equity convention: remaining losses from executable marks for
        # filled positions; from stressed fills for pending/proposed orders.
        reserves = [broker_remaining_stress_loss(x, account, policy) for x in book]
        require(all_finite_and_nonnegative(reserves))
        require(account.equity - sum(reserves) >= policy.operating_floor)
        require_all_fill_margin_and_stress_covariance(book, account, policy)
        reservation = writer.persist_intent_and_reservation(proposed, bundle)
        return writer.send_once_and_reconcile(reservation)
```

The loss helper includes broker USD conversion, remaining fees/swap, calibrated adverse stop-fill quantiles and the explicit cost reserve. It gives positive stop-profit no financing credit in the conservative gate. Any unsupported valuation or None inventory means UNKNOWN and denies new risk. Balance-based full trade-stop PnL and equity-based remaining loss are alternative conventions; do not mix them and count floating PnL twice. Account-level locking must cover every strategy writer, not just one daemon. Lost acknowledgement keeps the reservation live until broker history reconciles the intent. Reconciliation must deduplicate a matched intent, pending order and resulting position by their canonical broker/order identifiers; one exposure must not become three separate reservations.

The hard floor triggers a sticky emergency halt, cancellation of all account pending orders, flattening, and verification; it must not be automatically reset. This can enforce admission and emergency behavior under specified stress scenarios. Unbounded market gaps mean it cannot mathematically guarantee a never-breached realized equity floor.

### Changes to the requested modules

`Terminal/OF_Strategy.py` is a 131-line CLI; it delegates to `AI15mMT5Trader`. Keep it thin. Add canonical policy loading and remove duplicated CLI defaults. Reconcile the four-slot migration in RiskPolicy, uplift artifacts, headless contracts, telemetry, admission, and every broker submission path. Implement the substantive engine changes in `Omni_Trader.py`, not only the launcher.

```python
policy = load_verified_policy(args.policy_file)
require_runtime_config_matches(policy, args)
trader = AI15mMT5Trader(policy=policy, account_id=policy.account_id,
                      **runtime_dependencies)
# In evaluate_market, after source validity and before sizing:
bundle = archive_observed_bundle(asset, now, policy)
mr = mean_reversion.evaluate(bundle)
tp = trend_pullback.evaluate(bundle)
candidate = highest_positive_net_value_feasible_candidate(mr, tp)
# Broker-facing limits, TP/SL and fill-contingent risk use the same gate.
```

Fix receipt-time rejuvenation at acquisition, constrain every event window to cut <= event_time <= decision_time, and require completed bar_close <= decision_time. Receipt age and exchange observation age are separate checks. Sequence gaps invalidate continuity. The bridge's OHLC close-location proxy must be named a proxy and must not overwrite actual aggressor delta. Preserve the old book timestamp when serving a cached payload.

`Terminal/arena_bridge.py`: reuse and extend the structured headless contract; fail unknown broker state; remove account literals, hardcoded 12 slots and 4,000 USD staging text. Record exactly one successful browser submission receipt with conversation/turn/cycle identity. Poll the recorded turn until complete or deadline; retries query that same turn rather than submit again. A DOM length threshold is not completion. Never append incomplete response text as final consensus. CDP transport remains separate from the account's single execution writer.

```python
request = council_request(bundle, policy, local_reports, cycle_id)
turn = arena.submit_once(request, idempotency_key=cycle_id)
reply = arena.await_completed_turn(turn, deadline=request.expires_at)
validate_reply_identity_schema_and_refs(reply, request)
arbitration = compare_action_utilities(bundle, local_reports, reply, policy)
append_decision_receipt(arbitration, dissent=collect_dissent(local_reports))
# Only the canonical execution service may act, after a fresh admission check.
```

Archive uncertainty, missing sources, dissent, observed forecasts, selected action, and later outcomes. For memory, retrieve only closed/fully observable prior episodes available before the current decision, conditioned on asset/session/regime/policy. Track probability calibration and net expectancy by failure mode. Reflections propose versioned research changes; they must not mutate live weights based on recent PnL or hindsight narratives. Evaluate a proposal against unchanged-policy counterfactual replay before promotion.

`Engine/forex_engine.py`: absent, so the implementation task must first identify the intended execution owner or recover the module from a known version. Do not create an empty replacement to satisfy a filename. Its eventual contract is the same central admission/ratchet/evidence service with broker-valued USD risk, session-aware calendars, and per-asset provenance. An unknown asset class must fail closed; NAS100, DJ30, FX, and oil must not silently become CRYPTO.

Fix session mapping with a canonical asset/class table and idempotent normalization:

```python
def normalize_asset_class(asset_or_class):
    if asset_or_class in {"CRYPTO", "COMMODITY", "INDEX", "FOREX", "ENERGY"}:
        return asset_or_class
    return validated_asset_registry[asset_or_class].asset_class
```

Unify replay and live ratchets into the same pure transition function; stamp its complete policy hash into uplift labels and inference qualification. The existing second-position model summarizes only one existing position and explicitly allocates one second slot. Four-slot use needs full-book features and paired counterfactual episodes managing the same complete portfolio, all pending fills, future slot opportunities, and execution costs. [first-position uplift features:928](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:928), [one-second-slot replay selection:297](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:297). Paired simulated replay is a modeled counterfactual under its fill assumptions, not automatically an identified causal treatment effect.

Ledoit–Wolf code already validates units, checksums, vintage, and PSD, and fits aligned completed broker M15 returns. Retain those checks. [covariance:322](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:322). Extend the candidate exposure vector to every possible pending/intended fill and regime-stressed covariance scenarios. For signed notionals w and candidate n in asset c:

```text
incremental_variance = n^2 * Cov(c,c) + 2*n*sum(w_i*Cov(c,i))
portfolio_sigma = sqrt(w_transpose * Cov * w)
```

Currency-convert notionals for FX. A 45 USD standard-deviation budget is not a bound on stop loss, correlated jumps, or four-position loss tails; retain the separate stressed floor/margin test. Treat statistical hedging and directional concentration as distinct policies. Fixed sector correlation bans do not establish optimal diversification; test their incremental cost after covariance and stress controls.

### Qualification and release sequence

1. Correct policy contradictions, unsafe admission, unknown-inventory handling, time/provenance defects, and certificate aggregation. Every required component must explicitly PASS; FAIL, UNKNOWN, SKIP, missing checks and stale evidence prevent certification. Bind the certificate to tested source/data/policy hashes and actual test receipts.
2. Pin execution code to an approved immutable release. Publish evidence through a separate data-only checkout with an explicit file allowlist and no automatic remote code imports or pushes of unrelated staged changes. Verify process identity and singleton locks; health must test actual model inference and fresh produced evidence, not importability/capability literals.
3. Build event-driven broker Bid/Ask replay of causally generated opportunities. Test future perturbation/prefix invariance, forming HTF exclusion, stale books, sequence gaps, partial fills, multiple simultaneous pending fills, lost acknowledgements, gap stop fills, blackout coverage, USD conversion, lot/stops rounding, and direct jumps through multiple ratchet stages.
4. Preregister small parameter families and test each engine, their router, wall weighting, structural targets, ratchets, and four-slot admission by ablation. Use chronological train/calibration/test partitions; purge overlapping full holding episodes and apply an embargo covering the specified information/label horizon. Preserve the repository's five-day separation where required rather than silently adopting the uplift file's shorter interval.
5. Bootstrap dependent market/session or day blocks and simulate the entire sequential portfolio. Do not sum overlapping candidate labels as achievable cash. Record every parameter trial, untouched out-of-sample net expectancy, tail loss, floor violations under the defined stress suite, calibration, fill/markout, and activity. Correct selection bias from the full search. [Deflated Sharpe original paper](https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf).
6. Run shadow decisions before any release promotion. Four slots increase opportunity only if additional candidates have positive conservative marginal value after existing exposure and contingent fills. Frequency and win rate are diagnostics, not substitutes for net equity and tail-loss protection.

Detailed independent reviews: [microstructure](C:/Users/SIGMA/Documents/Trading_2/docs/reviews/ASTRA_20261009_microstructure_findings.md), [dialectic and macro](C:/Users/SIGMA/Documents/Trading_2/docs/reviews/ASTRA_20261009_dialectic_findings.md), [risk and cross-verification](C:/Users/SIGMA/Documents/Trading_2/docs/reviews/ASTRA_20261009_risk_qa_findings.md). Four selected existing offline regressions passed; additional isolated probes exposed the relaxed-admission, certificate, freshness, and causality failures described above. The relaxed-admission probe imported the actual module with a fake bridge; other probes extracted individual current AST functions. The full 402-test suite, real-money fill quality, and new strategy walk-forward performance were not verified in this audit. Independent report QA passed for quantitative accuracy and bounded conclusions; all 35 source links and line bounds were verified, and all four proposed Python snippets passed syntax parsing. Those checks do not establish production readiness.

The proposed architecture can be evaluated rigorously. No threshold optimum, profitability improvement, full production certification, or real-money execution guarantee was established by this audit.
