# OMNI microstructure review — 5 October 2026

The fuel-versus-depth formulation is a useful diagnostic. The supplied specification does not establish that FFR 1.50 is optimal, that it implies a 72 percent cascade probability, that whale front-running dominates CE staging, or that a 0.35R stop guarantees positive net profit. Current code also differs materially from the specification. Correct these differences before using historical optimization to select a production policy.

This is a source review and nine broker-free counterexamples, not a historical performance study or certification of the running process. Production Python modules, account state, MT5 orders, and deployed models were not changed. The checked source hashes and numerical results are saved in [microstructure_stress_20261005.json](C:/Users/SIGMA/Documents/Trading_2/docs/audits/microstructure_stress_20261005.json). The reproducer is [stress_microstructure_review_20261005.py](C:/Users/SIGMA/Documents/Trading_2/scratch/stress_microstructure_review_20261005.py). Its engine fixture injects fake IPC; two checks execute isolated source blocks and several are mathematical counterexamples. They establish reachable defects, not their live frequency.

## Current implementation findings

| Priority | Evidence in current source | Consequence |
| --- | --- | --- |
| Critical | [Omni_Trader.py:257](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:257) computes the drawdown floor from mutable state capital. The inspected state has capital 4775 and peak equity 4805.67. | The function produces a floor of 4590.795, rather than the mandated original-capital floor of 4775. The existing sticky latch and pending-order flattening act on this incorrect floor. Persist original capital separately; a migrated or restarted account must not receive a new loss allowance. |
| High | [Risk_Sizing_Engine.py:255](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:255) sums full cluster exposures and separately sums depth per band. Zero depth with positive exposure becomes FFR 10. The candidate path at [Omni_Trader.py:473](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:473) has confluence and vacuum vetoes but no FFR threshold veto. | Missing coverage becomes apparent strength; overlapping bands repeat depth; a fixture with FFR 0.004995 and confluence 0.72886 reaches PAPER_FILLED despite the specified dense-friction veto. This fixture uses market mode; it proves the absent candidate gate, not that a live limit was filled. |
| High | [Omni_Trader.py:482](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:482) raises sector vetoes inside a try block that catches ValueError and passes. | Both intended vetoes are swallowed. The isolated block accepts positive-correlation opposite directions. Also, the proposed direction rules reject variance-reducing hedges; they are not covariance risk protection. |
| High | [Omni_Trader.py:503](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:503) and the mirrored short branch filter walls only by side and price corridor. | Tier 1 does not require 150000 USD notional, 180 seconds of persistence, a fresh component timestamp, or a continuously identifiable order. A newly observed one-dollar wall qualifies in the isolated entry filter. |
| High | [Omni_Trader.py:695](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:695) immediately creates a paper position at the chosen entry price, including limit mode. | Paper results cannot evaluate passive fill probability, missed trades, partial fills, adverse selection, or splitting. A favorable limit price is assumed filled without a causal broker trigger. |
| High | [Omni_Trader.py:708](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:708) treats unsuccessful limit sends and exceptions as REJECTED; the market branch instead preserves UNCERTAIN. [MT5_Execution_Bridge.py:563](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:563) treats a missing acknowledgment as rejection. | Lost acknowledgments can destroy the unresolved-intent barrier. Reconcile broker orders and deals before a retry. A STAGED_LIMIT absent from both current pending orders and positions is marked EXPIRED before consulting deal history, so a fill-and-close between polls can be missed. |
| High | [Omni_Trader.py:361](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:361) manages positions and cancels pending orders on hard drawdown; the blackout branch at line 457 rejects new evaluations without canceling already staged orders. Limits are submitted with a 600-second expiry at line 706. | A pending order can fill after a whale disappears or during a newly started blackout. Pending risk needs continuous revalidation, not only the checks at submission. |
| Medium | [Omni_Trader.py:29](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:29) uses the last 96 observations for VWAP and pivots; line 47 substitutes one for missing or zero volume. | This is a rolling bar-weighted price benchmark, not a session-anchored VWAP. Closed-market gaps can make 96 observations span more than 24 hours. Missing volume silently becomes an equal-weight proxy; daily pivots use a rolling window rather than the previous completed session. |
| Medium | [Omni_Trader.py:77](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:77) retains bullish gaps until their lower edge is reached, and line 89 returns only the latest gap CE. | A gap can remain partially unfilled after its CE has been touched. The code does not distinguish these states or search all eligible CEs within the entry corridor. A gap from 100 to 102 retains CE 101 after a subsequent low of 100.5. |
| Medium | [Risk_Sizing_Engine.py:242](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:242) still derives trade direction from the same weighted L2, macro, whale, tape, and liquidation features. | The stated EMA-200/confirmed 4H trend and separate pullback execution architecture is not implemented in this path. Negative pullback tape still moves the directional vote against a long. |

These observations concern the checked files. Source on disk, an already running imported Python process, a historical ledger, and broker inventory are different evidence sources. A prior log cannot certify the current deployment. Improvements since the earlier audit are also present: future component timestamps are rejected more strictly, covariance expiry has a hard cap, and the inspected uplift manifest now declares live_eligible false. This review does not treat that model as qualified for live second-position selection.

## 1. FFR sensitivity and calibration

**Answer: use 1.50 as a hypothesis, not a universal threshold or probability.** A large exposure/depth ratio does not establish that the price will reach the liquidation triggers, that the exposure will remain outstanding, or that depth will not replenish. The documented Hyperliquid mechanism uses mark price and allows partial liquidation; for positions exceeding 100000 USDC, the initial liquidation order is 20 percent. Full projected position notional therefore does not equal immediate aggressor flow. [Hyperliquid liquidation documentation](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations).

Research relates short-horizon price changes to order-flow imbalance from limit, market, and cancellation events, with sensitivity inversely related to depth. That supports incorporating book dynamics, but does not validate these FFR thresholds on crypto or CFDs. [Cont, Kukanov and Stoikov](https://arxiv.org/abs/1011.6402).

First fix the observable ratio. Choose a terminal price p_star in direction d and a forecast horizon H, rather than summing every cluster indefinitely above or below the market. Use the full path from mid to p_star, including intervening levels before the cluster. Count each book level once. Exposure identities must prevent counting the same position both as a stop and as a later liquidation that the stop would preempt. Broad bands are uncertainty intervals, not evidence of a uniform distribution of notional over price.

```text
C(d, p_star) = price path from mid to p_star

E_eff(d, H) = sum over unique exposures in C:
    exposure_usd * P(trigger before H and before invalidation | available state)
                 * expected liquidation fraction
                 * P(position still exists when reached | available state)

D_eff(d, H) = sum over unique opposing levels in C:
    depth_usd * P(level survives until arrival | available state)
    + expected replenishment in C over H

FFR_H = E_eff / D_eff, only with verified corridor coverage and a valid denominator

z_ffr = (log1p(FFR_H) - trailing_median_asset_session_regime)
        / max(1.4826 * trailing_MAD_asset_session_regime, scale_floor)
```

These probabilities are quantities to estimate from past events, not constants to invent. When sufficient event data is unavailable, retain the raw unique-exposure/depth diagnostic plus separate coverage and distance features. A corridor beyond the 20-level book is unknown, not empty. Make the feature missing and reject the cascade-specific setup, or explicitly abstain from its cascade component. Never substitute FFR 10 or a one-dollar denominator for absent coverage. If verified depth is very small, retain that fact separately and cap the numerical feature; do not confuse it with missing data.

The current pressure calculation prorates full exposure by a linear band overlap at [Risk_Sizing_Engine.py:225](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:225), while FFR later uses the full amount. Neither a projected trigger distribution nor the raw path depth is faithfully represented. One reproduced unobserved corridor carries one million USD of fuel, zero visible depth, pressure ratio missing, and FFR 10. Two overlapping corridors can also produce naive FFR 1 when unique-depth FFR is 2.

Use a calibrated logistic model as a baseline, then compare LightGBM on log-FFR, volatility, normalized trigger distance, depth coverage, spread, cancellation/replenishment rates, aggressor imbalance, mark/book basis, venue, asset, session, and trend regime. Define a cascade label before training: favorable first passage before an adverse barrier within a fixed horizon. Separately model the trade's conditional net PnL; a correct cascade prediction can still produce a losing entry after costs or an adverse fill.

Use common chronological splits across correlated assets. Purge training labels that overlap evaluation episodes and embargo by the maximum applicable outcome horizon; six-hour trade labels require treatment of six-hour overlap. Estimate medians, MAD scales, volatility regimes, calibration, thresholds, and hyperparameters inside each training fold. Reserve an untouched final period. Report calibration and Brier score alongside net equity, drawdown, turnover, nonfills, and uncertainty from session/day block resampling. Do not optimize accuracy or in-sample Sharpe alone. Threshold 1.50 is promoted only if it improves feasible net execution outcomes over nearby thresholds, a continuous-score policy, and a no-entry baseline in independent periods.

For pullbacks, separate setup direction from entry state. A confirmed trend supplies the candidate direction; negative tape can be acceptable for a long only when bid replenishment, limited downward price impact, and support survival indicate absorption. Negative tape alone also describes the beginning of a selloff. Do not simply reverse its sign to manufacture confluence. Model the trend/pullback and cascade entry families separately; FFR can play different roles in them.

## 2. Whale versus CE entry selection

**Answer: neither fixed whale priority nor automatic splitting is strictly superior.** One-tick improvement relative to a Hyperliquid wall does not establish queue priority for a Blueberry MT5 CFD order. The signal venue and execution venue differ; transfer the price level through a validated, timestamped basis model and estimate fills from actual broker bid/ask events and acknowledgments. A bid-only bar low cannot certify a buy-limit fill, and a last/mid touch cannot certify either side.

Estimate each candidate level's fill probability before a short, explicit TTL, its conditional net return, adverse post-fill markout, and opportunity cost of missing an expiring signal. Queue-reactive research provides a state-dependent framework for order arrivals, cancellations, and execution simulation; its published venue results are methodological support rather than a fitted MT5 fill model. [Huang, Lehalle and Rosenbaum](https://arxiv.org/abs/1312.0563).

```text
Utility_j = P(fill before TTL | available state)
            * E(net_PnL_usd | fill, available state)
            - inventory_and_tail_risk_penalty_j
            - missed_opportunity_cost_j
```

Select the highest positive utility among whale, eligible CE, VWAP, and no-entry. Evaluate joint split utility as a separate policy; summing independent utilities ignores that both legs can fill in the same adverse move. Compare whale-only, CE-only, selected splits, and no-entry on identical opportunity timestamps, with event-driven fills, partial fills, cancellations, TTL expiry, broker latency, slippage, brackets, costs, and the same portfolio state. Favor a split only when its incremental net benefit survives independent periods and realistic cost/fill perturbations.

Split by risk contribution rather than equal lots when stop distances differ. Reserve risk, free margin, covariance capacity, and position slots for the worst feasible combination of child fills. On a hedging account, two child tickets plus an existing position can violate the maximum of two; broker minimum lots may make a 0.01-lot parent unsplittable. OCO cancellation is not instantaneous: reserve both child exposures until cancellation is acknowledged. Partial fills must also reduce the unfilled reservation correctly. A slot belongs to the execution intent, not merely to the presently visible position list.

Pending-order lifecycle should be:

```text
PREPARED -> SEND_UNCERTAIN or STAGED
STAGED -> PARTIALLY_FILLED -> FILLED
STAGED/PARTIALLY_FILLED -> CANCEL_REQUESTED -> confirmed residual cancellation
STAGED -> confirmed expiry
```

Reconcile position, order, and deal identifiers after every ambiguous acknowledgment. Revalidate pending setup quality, whale survival, feed age, broker basis, macro blackout, drawdown room, and portfolio capacity while the order waits. Cancel invalidated residual orders; reserve their possible fill risk until the cancellation is confirmed. A broker-supported native expiry supplies a backstop, not a substitute for these checks. Query supported time and filling modes per symbol. The current RETURN policy is appropriate to ordinary MT5 pending-order submission, but the local preflight check does not prove broker-side post-only behavior. MT5 documents BOC as a passive mechanism where supported; do not assume this account or symbol implements it. [MT5 symbol and execution properties](https://www.mql5.com/en/docs/constants/environment_state/marketinfoconstants).

Correct the level definitions before testing selection:

```text
Bullish CE untouched at decision time:
    every subsequent completed-bar low > CE

Bearish CE untouched at decision time:
    every subsequent completed-bar high < CE
```

Keep separate flags for untouched CE and not-fully-filled gap. Evaluate all eligible historical gaps in the corridor. A newly created gap has no post-formation observations; tag its age explicitly. The current gap-edge rule matches the specification's not-fully-filled invariant, but that invariant does not establish an untouched midpoint. Select an actual session anchor for VWAP; reset by a declared venue/calendar rule. Record real trade volume versus tick-volume proxy explicitly. Price dispersion bands describe dispersion around the weighted mean, not forecast confidence intervals or Gaussian reversal probabilities. Use previous completed-session H/L/C for daily pivots.

## 3. Whale persistence, cancellation, and decay

**Answer: test a conditional survival model; do not replace exponential weighting with power law on intuition.** The current min(age/60, 1) is an age ramp, and exp(-distance) is spatial attenuation. Neither models the future cancellation hazard. The stated 180-second eligibility requirement is absent from the entry branch. In addition, the spatial width is max(3*sigma, 0.01), so it has a one-percent floor at low volatility. [Risk_Sizing_Engine.py:180](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:180).

Let a be observed order age, Delta the estimated time until entry interaction, and S(t | x) the survival function conditional on order and market state. A wall visible now should receive conditional remaining-life weight, not unconditional survival from its original submission.

```text
survival_weight(a, Delta, x) = S(a + Delta | x) / S(a | x)

Exponential: S(t) = exp(-t / tau)
    survival_weight = exp(-Delta / tau)

Lomax/power law: S(t) = (1 + t / tau)^(-alpha)
    survival_weight = ((tau + a) / (tau + a + Delta))^alpha
    residual_half_life(a) = (tau + a) * (2^(1/alpha) - 1)

effective_wall_usd = notional_usd
                     * exp(-abs(log(wall_price / mid)) / (k * sigma_H))
                     * survival_weight
                     * source_confidence
                     * absorption_confidence
```

Use a declared, positive sigma floor only for numerical stability, and calibrate k on past data. Apply notional and continuous-visibility eligibility before computing the effective weight. Large aged orders can survive more often in a fitted heavy-tail model, but size, approach speed, distance, volatility, replenishment, and prior wallet behavior should condition the hazard. Persistence alone does not establish beneficial support or intent to trade.

Compare exponential, Weibull, Lomax, and a discrete-time competing-risk hazard model. Distinguish cancellation, execution, partial execution, modification, and loss of observation outside the visible book. A vanished top-20 order is not evidence of cancellation, and cancellation is not proof of spoofing. Snapshot data yields interval-censored event times; end-of-sample orders are right censored. Selecting only orders surviving 180 seconds also truncates the sample and must be handled in estimation.

Reliable order IDs, exchange event times, receipt times, sequence gaps, and modification histories are essential. The current fallback wallet:side:price identity can merge unrelated orders or split modified ones. Without identifiable event histories, call the feature visible-wall persistence and abstain from claims about cancellation kinetics. Choose the hazard model on chronological out-of-sample likelihood, horizon-specific calibration, censoring-aware Brier scores, and resulting net entry utility. A power law is accepted only if it wins these comparisons; no particular half-life is established by the supplied evidence.

## Ratchet arithmetic and the Silver claim

The stated 0.35R lock is not enough to clear the stated 41 bps cost model for the supplied Silver entry. This conclusion does not require knowing the lot multiplier:

```text
Entry = 62.020
Initial price R = 0.580
0.35R price gain = 0.203
Locked return = 0.203 / 62.020 * 10000 = 32.7314 bps
Stated round-trip reserve = 41 bps
Cost break-even lock = 0.0041 * 62.020 / 0.580 = 0.438417R
```

Using the ten units implied by the claimed 2.03 USD gross gain, the cost reserve is 2.54282 USD and the modeled net is -0.51282 USD before any additional gap/stop slippage. At 0.80R, modeled net is 2.09718 USD, below half the initial stop-only risk of 2.90 USD. These are consequences of the specification's cost assumption, not observed settled broker PnL; actual commission, spread already embedded in execution prices, swap, fees, and slippage must be reconciled without double counting.

Use a cost-aware lock condition:

```text
required_lock_R = (remaining_and_sunk_trade_cost_usd
                   + chosen_exit_slippage_reserve_usd
                   + desired_net_profit_usd) / initial_stop_risk_usd
```

Place it only when executable under current stops/freeze/tick rules, and preserve monotonic stops. Account for costs already recognized in floating equity consistently. Even a sufficient modeled lock does not guarantee an executable stop price through a gap. Passive entry also does not eliminate round-trip commissions, exit spread, financing, or adverse selection; retain the 41 bps production reserve until measured broker-deal evidence supports a revised policy.

The local execution record supports an acknowledged modification to SL 61.817 for ticket 18510585 at approximately +0.80345R. It does not establish a minimum net profit, settlement at that stop, the supplied +0.94R timing, or that the current sector branch prevented a Gold order. The present phase-2 code also uses max(1.5R, gain_R - max(0.5R, ATR/R)) after +2R, rather than a fixed current-price-minus-1R trail. [Uplift_Model.py:30](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:30).

For covariance, positive correlation with opposite signed exposure reduces variance. With equal leg standard deviations of 20 USD and rho 0.7655, opposite directions produce portfolio sigma 13.6967 USD; same directions produce 37.5819 USD. These are illustrative 15-minute standard deviations, not stop-loss budgets. An anti-conflicting-sector-alpha overlay may still be tested as an expectancy policy, but it should not be described as a variance shield, and a single favorable subsequent Gold move does not establish its benefit. A 45 USD covariance budget also does not provide a pathwise guarantee of the 225 USD original-capital drawdown limit.

## Recommended implementation order

1. Restore the immutable original-capital floor, preserve the sticky latch, and retain broker reconciliation as the authority for sends, fills, closes, and cancellations.
2. Correct corridor coverage, unique depth/exposure counting, explicit units, missing values, and the specified gate behavior. Enforce wall eligibility and distinguish CE states and session anchors. Narrow exception handling so intended vetoes escape their local helper.
3. Add a pending-order paper/replay state machine driven by broker-side quote events, latency, partial fills, and cancellation races. Record unfilled opportunities as well as fills. Reserve worst-case pending inventory.
4. Fit FFR response, broker fill/adverse-selection, and wall survival models on chronological data. Compare simple baselines before adding model complexity, and enforce the same costs, ratchets, blackout, portfolio, and drawdown policies in every counterfactual.
5. Evaluate complete strategies on untouched periods, then shadow the chosen policy with versioned features, predictions, intended orders, broker acknowledgments, and settled net outcomes. This review has not established any threshold's profitability or authorized a claim of optimality.
