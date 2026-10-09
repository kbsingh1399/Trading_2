Completed the [full quantitative audit and implementation blueprint](C:/Users/SIGMA/Documents/Trading_2/docs/reviews/OMNI_Architecture_Audit_20261009.md), with three independent reviews, source citations, numerical reproductions, and integration pseudocode.

**The immediate priority is correcting admission and evidence failures. More sophisticated debate cannot compensate for them.**

Native MT5 at 14:22 UTC showed 4,896.55 USD equity, zero positions, and one USDJPY pending limit. It reported **DEMO mode**, despite the server’s “Live” name. Broker reconciliation gives **83.11 USD net across the 17 listed positions**, spanning October 7–9, rather than 84.05 USD earned today. [Reconciliation evidence](C:/Users/SIGMA/Documents/Trading_2/docs/reviews/ASTRA_20261009_risk_qa_evidence.json).

The most consequential findings are:

| Finding | Verified consequence |
|---|---|
| High free margin bypasses joint pending-risk reservation | Four resting orders plus a fifth candidate were accepted at 4,800 USD equity; simultaneous stressed fills leave **4,727.50 USD**. |
| Capacity differs across components | Council: four; daemon policy: two; admission: six; Arena/telemetry: twelve. |
| Cached books receive fresh timestamps | A 500-second-old book passed a 10-second freshness policy. Future-dated trades also entered current CVD. |
| Verification can certify missing evidence | Six SKIP results produced “CERTIFIED_100_PERCENT_PRISTINE”; pending risk and unknown inventory were omitted. |
| Arena responses lack cycle binding | Old or incomplete prose can become a fresh-looking consensus. |

The admission defect is in [live_admission.py:105](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/live_admission.py:105); timestamp rejuvenation starts in [factory.py:240](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/factory.py:240); unsafe certification aggregates in [chain_verification_360.py:529](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:529).

**1. Dual-engine and entry optimization**

Evaluate both engines, but remove the implication that an in-range Z-score obligates entry. Z measures displacement; it does not distinguish continuation from exhaustion. Select the feasible engine with the highest positive lower confidence bound of net expectancy.

Replace a universal 0.10–0.60 ATR band with asset/session-conditioned retracement distributions:

- Normalize shelf distance by price × forecast return volatility.
- Estimate volatility from completed bars, comparing Garman–Klass with realized returns and retaining separate opening-gap stress.
- Fit broker fill probability and subsequent return jointly.
- Include failed and unfilled opportunities, rather than learning only from successful pullbacks.

The objective should be:

Entry value = P(fill) × E(net PnL | fill) − tail-risk penalty − capacity opportunity cost.

For whales, 150,000 USD and 180 seconds are hypotheses to test. Anonymous L2 persistence does not prove that one whale maintained one order. Separate actual receipt freshness, continuous presence, cancellation, executions, and replenishment. Compare exponential versus Weibull/power-law survival using held-out calibration. With the current sparse observations, wall-survival probability should remain unknown or bounded.

**2. Debate and arbitration**

Bind every request and response to a cycle ID, evidence digest, policy digest, candidate/ticket, source references, and expiry. Obtain independent local assessments before revealing Arena’s recommendation; then conduct one targeted challenge/rebuttal round.

Use a calibrated joint evidence model. Repeated interpretations of one book must not become independent Bayesian votes.

Score = 100 × P(incremental net PnL > 0).

That score is insufficient by itself: a 90% chance of gaining 1 USD and 10% of losing 20 USD scores 90 but has expectancy −1.10 USD. Require positive conservative action value and all deterministic gates.

Compare KEEP versus DELETE using fill-conditional value and released risk capacity. Compare HOLD versus EXIT from the current executable mark, avoiding attachment to the entry price. Unknown new-risk evidence means HOLD_VALIDATION; it does not automatically justify panic-closing an existing position.

Crucially, a four-minute Arena review needs a **separate fresh execution revalidation**. An intact hash does not make old depth fresh. The existing [structured headless contract](C:/Users/SIGMA/Documents/Trading_2/Terminal/Headless/llm_contract.py:66) is a useful integration starting point.

**3. Liquidation reconstruction and structural targets**

POC, value areas, pivots, and OI can support probabilistic latent-liquidity estimates. They cannot establish exact hidden stop inventory or a future liquidation peak.

Correct OI reconstruction to difference contract quantities before valuation: unchanged contracts with a rising price must not create new exposure. Deduplicate liquidation updates and use incremental executed quantity.

For FFR, require fuel and opposing depth in the same fully observed corridor. A top-20 book cannot quantify absorption to a distant target outside its coverage. Preserve sampled-wallet coverage uncertainty.

Select targets by conservative expected payoff before opposing absorption, including broker/source basis uncertainty. Long exits depend on Bid; short exits depend on Ask. Broker CFD limits still use executable bid/ask pricing; they do not establish zero spread or exchange queue priority. [Official MT5 mechanics](https://www.metatrader5.com/en/terminal/help/trading/general_concept).

**4. Ratchet optimization**

The 0.15R lock does not establish net breakeven under your 41 bps model:

0.15 × R / Entry >= 0.0041 requires R / Entry >= 2.7333%.

For the cited SP500 trade, 0.15R locks **1.95 USD gross**, versus **31.945 USD** reserved friction under that model. Actual broker costs and the conservative reserve must be distinguished.

Invert broker-valued PnL to obtain a cost-aware stop; preserve original R across restarts and tighten stops monotonically. A profit-side stop retains gap/slippage risk and still occupies a filled slot.

Test 0.50R friction-only, 0.80R locking, and volatility/structure trails on identical untouched tick episodes. Measure expectancy and tail loss, not merely win rate. Advance directly to the strongest eligible stage after a price jump.

**5. Implementation and qualification**

The report includes proposed code interfaces for canonical admission, dual-engine selection, Arena handshake, and asset-class normalization.

OF_Strategy.py is a thin launcher; substantive changes belong in Omni_Trader.py and the shared risk/execution services. The requested Engine/forex_engine.py is absent from both repositories.

Adopt one versioned policy and one submission owner. Reserve every independently fillable pending order and unresolved intent. Without verified atomic mutual exclusion, unlimited resting orders are incompatible with a strict four-filled-position cap.

Admission must enforce:

Equity − total remaining stressed loss >= 4,795 USD.

Keep the sticky 4,775 USD emergency halt separately. Covariance sizing cannot replace this loss constraint, and ordinary stops cannot guarantee a floor through unbounded gaps.

Finally, unify live and replay ratchets before qualifying uplift; the current second-slot model does not qualify a four-slot portfolio. Use chronological, purged portfolio replay, realistic broker costs, dependent-block uncertainty estimates, and untouched validation.

**Verification:** four focused regressions passed; additional isolated probes exposed the failures above. Independent QA validated the report’s arithmetic and citations. No production changes, orders, restarts, or automation changes were made.

The final mirror check found **133 differences**; byte parity is not certified. The audit was recorded in both session journals.
