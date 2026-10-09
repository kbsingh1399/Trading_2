# Astra dialectic, Arena bridge, and certification audit — 2026-10-09

The current CDP bridge implements prompt transport and ledger writing. It does not implement the specified independent four-agent challenge loop, quantitative arbitration, or order execution. Several assurance statements can be generated without the evidence they claim to certify. These reporting defects must be distinguished from downstream order-admission failures, which the parent risk/QA reviewer examined separately.

## Scope and evidence freeze

Read-only review of the canonical council protocol, `.agents/AGENTS.md`, ACTIVE_CONTEXT, scoped recent session history, the graphify and architecture/debugging skill guidance, and current source. Graphify queries succeeded and were followed by AST inventories and focused source slices. No full production script was executed or imported; no MT5 IPC, orders, Arena submissions, runtime changes, automation changes, production edits, Git staging, commits, or pushes were performed. Isolated probes compiled only named AST function nodes with in-memory dependencies. No ruflo/ToolSearch capabilities were available in the tool catalog.

Canonical review policy: hard floor 4,775 USD, operating floor 4,795 USD, at most four filled positions, all pending contingent risk counted, Arena send at :25/:55 with read at :29/:59. The four-minute cadence is operator policy; this review changes no automation.

The snapshot captured at 2026-10-09 14:19:52 UTC was as of 14:18:58 UTC. SHA-256: `6ec05a25e39b6f1febbc39048c94ca06e871feb5cc96a16e84e116e66044a723`. It carried `DENIED_UNVERIFIED_ORDERFLOW`, capacity 12, and `STALE_REVIEW_REQUIRED` with runway -45.32 hours. It is a recorded observation, not a claim about subsequent live state.

Initial source review HEAD: `5a22d0087b62f94aed709a1cc4bec1a66bb9ce7d`. Persistence check at 2026-10-09 14:25:27 UTC: HEAD `2810e778a9074bed051f032b714b674d3cb9fb9f`. All four reviewed source hashes were unchanged:

| File | SHA-256 |
|---|---|
| Terminal/arena_bridge.py | c7f01ca2d2012fcc57f01b37caa4b5d235bee7fc3df7f59032902ab4ba7369d2 |
| Terminal/chain_verification_360.py | b82b0c9b8dcc9d46301f4eb57e6f18b23acd48e28b290d432aec7fe75466ae3f |
| Terminal/Data_Factory/autonomous_telemetry_git_daemon.py | 9145e15ed5154ed761f7986e7ec6a40b3c8ddb8b6c6ae245cc593de8cba3dc35 |
| Terminal/Data_Factory/heretic_daemon.py | 427f2c95136e82bc631cba06b5e9cef654d9bfa580bfda1ce56a766fa24c46be |

History at persistence check: 52,101 lines, SHA-256 `ff238cee068470d91def45d954e1003382a320c1ecff567713050b4b3483447f`. Its last nonempty line says the background engine is paused/idle. The parent independently observed live telemetry and duplicate daemon processes after that claim; this reviewer did not change runtime state.

## Verified findings

### D1 — P1: Telemetry authorization and provenance are discarded

`build_48h_orderflow_prompt` loads JSON without validating protocol, observation epoch, authorization, source receipts, or completeness. JSON errors are ignored. Account fields fall back to historical numeric literals. A false `mt5.initialize()` result skips the exception handler, leaving positions/orders empty and later emitting flat/clean claims. Snapshot positions/orders are used only after an exception, rather than on every unavailable broker-state result.

References: [load:174](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:174), [defaults:185](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:185), [initialization:195](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:195), [exception fallback:241](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:241), [flat claim:318](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:318), [clean queue claim:325](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:325).

The publisher does enforce an observed-only protocol. Its validator explicitly requires `DENIED_UNVERIFIED_ORDERFLOW`; publication success therefore cannot be interpreted as trading authorization. [Telemetry_Provenance.py:9](C:/Users/SIGMA/Documents/Trading_2/Terminal/Telemetry_Provenance.py:9).

### D2 — P1: The prompt itself supplies the obsolete margin trap

The bridge hardcodes `max_concurrent=12` and staging while free margin exceeds 4,000 USD. This contradicts the current four-filled-slot policy and the protocol's rejection of the fixed 4,000 USD gate. An Arena response repeating that rule may be following its local input rather than independently hallucinating it. [arena_bridge.py:282](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:282).

Capacity must be an immutable versioned policy object. Four filled slots and contingent pending risk are separate constraints. Pending orders do not presently consume filled slots, but simultaneous pending fills can exceed them; admission must enforce reservations or atomically prevent excess fills.

### D3 — P1: Submission and response identity are not verified

The clear operation's boolean is ignored. Submission sends Enter and then invokes a click/onSubmit fallback, potentially submitting twice. CDP results are not matched to a durable application-level submission receipt. The success message is based on completing those operations.

Response completion means no detected stop button and more than 50 characters in the last `.prose` element. The extraction has no conversation/turn identity, cycle ID, snapshot/policy digest, expected answer schema, observation expiry, or replay guard. An old response can satisfy the rule. The first tab with an `arena.ai` substring is selected, without pinning conversation identity.

References: [tab selection:444](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:444), [clear ignored:566](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:566), [Enter/fallback:626](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:626), [success claim:683](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:683), [response selection:738](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:738), [completion:770](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:770).

### D4 — P1: The cycle ledger can manufacture consensus

The `cycle` path waits 120 seconds, conflicting with the requested four-minute :25/:55 to :29/:59 interval. It appends response text when its length exceeds 50 even if `done=False`. Ledger status/capacity claims are historical literals. The strings `PUNCH NONE` or `DEFENSIVE HOLD` become a consensus verdict without any independent comparison. No subagent invocation, quantitative arbitration, or `order_send` exists in this path.

References: [wait:795](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:795), [append condition:810](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:810), [historical ledger claims:822](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:822), [keyword consensus:827](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:827).

### D5 — P1: Certification materially exceeds performed verification

Feature causality/VWAP flags start as `True`. Computing endpoint ATR/EMA/RSI/VWAP does not test prefix invariance, future perturbations, higher-timeframe closure, production feature equality, or next-bar execution. Only BTC feature processing is called. The routines labeled Wilder ATR/RSI use recent arithmetic means, without comparing these with production smoothing.

L2 freshness starts as `True`. One REST request for each of BTC/ETH does not verify exchange event age, repeated update continuity, or 180-second persistence. Parquet freshness is counted but never changes status. A missing timestamp can leave monotonicity and age defaults apparently passing. Telemetry checks filesystem mtime, reads the obsolete `assets` key, and leaves `positions_in_sync=True` without reconciliation. The aggregate passes any layer value other than FAIL/WARN, including SKIP. This certificate path does not invoke pytest.

References: [L2 truth flag:142](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:142), [timestamp/defaults:219](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:219), [stale count:244](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:244), [parquet verdict:261](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:261), [causal flags:270](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:270), [telemetry audit:363](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:363), [BTC-only call:533](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:533), [aggregation:539](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:539).

Replace blanket 100%/10-of-10 claims with a scoped evidence certificate: code hash, policy hash, account identity, fixture/data hashes, required checks, observed results, test command/exit status, coverage and exclusions, timestamp/expiry. Required checks must all equal PASS. SKIP/UNKNOWN/NOT_RUN are incomplete rather than certified. A passed unit suite is not a claim that all runtime data, broker behavior, or financial outcomes are correct.

### D6 — P1: The floor certificate is not an admission gate

The audit omits pending orders, uses price difference times contract size times lots rather than broker cash conversion, treats stop-locked profit as credit, and never fails when stressed equity breaches the hard/operating floors. `positions_get() or []` also collapses IPC errors into empty state. Calculating a cushion is not enforcing it.

References: [positions only:443](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:443), [cash formula:458](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:458), [credit/stress:495](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:495), [return without floor verdict:518](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:518).

The probe below demonstrates an unsafe reporting assurance, not itself a broker execution bypass. The parent's separately reproduced admission failure is the relevant evidence for actual gate enforcement. Downstream execution controls cannot rescue the truthfulness of this certificate, while this certificate's false PASS does not prove every downstream control is absent.

### D7 — P1: The publication daemon mutates production code and can include unrelated staged files

The daemon pulls arbitrary remote changes with rebase/autostash, then dynamically reloads execution-bridge and producer modules next iteration. There is no data-only remote allowlist or review step protecting imported source changes. It stages telemetry plus the whole `docs/audits/` directory and pushes the branch and main. The observed-only/180-second validation is useful but applies to the snapshot before publishing, not to production code changes or trading approval.

Crucial scope refinement: `git add` names specific paths, but the subsequent bare `git commit` includes the entire already-staged index. The path allowlist therefore does not isolate pre-staged files. If another process stages `docs/reviews/` or source changes, a telemetry commit could publish them. The index was empty immediately before this report was written, and this reviewer leaves the report unstaged under `docs/reviews/`.

References: [pull:109](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/autonomous_telemetry_git_daemon.py:109), [validation:124](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/autonomous_telemetry_git_daemon.py:124), [explicit staging:137](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/autonomous_telemetry_git_daemon.py:137), [whole-index commit:140](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/autonomous_telemetry_git_daemon.py:140), [push main:152](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/autonomous_telemetry_git_daemon.py:152), [reload:177](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/autonomous_telemetry_git_daemon.py:177).

A safer design uses an isolated publication checkout/index containing only validated data artifacts, never pulls remote production source into a live worker, and never grants the publisher trade-execution authority.

### D8 — P1: Macro/session freshness is divergent and incomplete

Snapshot generation hardcodes the Oct 7 minutes event and flags it stale after 24 hours rather than selecting the next verified calendar event. The bridge does not include the calendar stale status in its briefing. `MarketIntelligenceEngine` checks coverage but not verified-at age; `BlackoutGuard` checks neither coverage nor verified-at age. The chain auditor declares the calendar path but does not audit it. Three implementations can disagree about the same runway.

References: [snapshot constant:482](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/generate_telemetry_snapshot.py:482), [stale flag:493](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/generate_telemetry_snapshot.py:493), [coverage-only:230](C:/Users/SIGMA/Documents/Trading_2/Terminal/Market_Intelligence.py:230), [guard loading:65](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/blackout_guard.py:65), [unused path:48](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:48), [fixed UTC rollover:125](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/blackout_guard.py:125).

The October local file was verified Oct 5 and contains US CPI/NFP/FOMC series. Freshness, coverage, correct timezone conversion, event-selection and asset-specific jurisdiction coverage are separate checks. A fixed 21:30–22:30 UTC quarantine is explicit policy, not proof of current broker trading/swap/session conditions. Use broker sessions and relevant IANA timezones with DST/holiday tests; retain operator windows as an additional policy constraint.

Official schedules retrieved for this review support Oct 14 CPI and Oct 28 FOMC dates: [BLS October 2026](https://www.bls.gov/schedule/2026/10_sched.htm), [Federal Reserve October 2026](https://www.federalreserve.gov/newsevents/2026-october.htm). Correct dates in a file do not prove that its refresh/coverage enforcement is sufficient for every traded asset.

### D9 — P2: Heretic status is importability, not an operational council

The daemon exposes GET health/status and periodically imports `heretic`. It does not load a model, perform inference, run optimization, or produce trading evidence. The capability names are literals. The status file reports port 8083 even after a failed bind. PID enforcement in the telemetry daemon can kill a reused PID because it checks liveness rather than command identity and does not acquire an atomic process lock.

References: [health:55](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/heretic_daemon.py:55), [binding failure:88](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/heretic_daemon.py:88), [heartbeat/capabilities:121](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/heretic_daemon.py:121), [PID handling:54](C:/Users/SIGMA/Documents/Trading_2/Terminal/Data_Factory/autonomous_telemetry_git_daemon.py:54). [Heretic's documented project purpose](https://github.com/p-e-w/heretic) is language-model ablation, which does not establish a working trading inference service.

### D10 — P1: Proxy footprint and incomplete higher-timeframe labels

The bridge overwrites delta with `volume × (2 × close_location - 1)`, an OHLC close-location proxy rather than aggressor-side traded volume. Its final 1H/4H resampled bins are labeled completed without comparing closing timestamps with the decision time. A tail of 192 rows is labeled 48 hours without verifying actual elapsed coverage or session gaps.

References: [proxy:88](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:88), [resample:106](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:106), [labels:377](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:377). Keep proxies separately typed and excluded from gates requiring observed CVD. Filter bars by available-at/close time and report actual window coverage.

## What the council actually implements

Arena's four specialists are instructions inside one prompt, with no evidence that four separate instances are invoked: [arena_bridge.py:303](C:/Users/SIGMA/Documents/Trading_2/Terminal/arena_bridge.py:303). The headless swarm computes three deterministic perspectives from the same payload; this is useful modular checking but not four independent observations: [swarm.py:192](C:/Users/SIGMA/Documents/Trading_2/Terminal/Headless/swarm.py:192). A separate helper actually launches parallel HTTP tasks, though one default model is used and the bridge does not call it: [web2api_multi_agent.py:47](C:/Users/SIGMA/Documents/Trading_2/.agents/scripts/web2api_multi_agent.py:47).

Published multiagent-debate research uses multiple model instances. It does not establish that named personas are independent votes or improve trading expectancy: [Du et al.](https://arxiv.org/abs/2305.14325).

There is an existing structured validation seam. `llm_contract.py` binds a candidate ID/invariant digest, validates keys, exact numeric echoes and support/invalidation references. It is disconnected from the CDP bridge, supports SELECT/HOLD rather than EXIT/DELETE, and retains two filled slots. Pointer resolution checks existence, not truth/provenance. References: [request:66](C:/Users/SIGMA/Documents/Trading_2/Terminal/Headless/llm_contract.py:66), [validation:106](C:/Users/SIGMA/Documents/Trading_2/Terminal/Headless/llm_contract.py:106), [old capacity:60](C:/Users/SIGMA/Documents/Trading_2/Terminal/Headless/llm_contract.py:60), [pointer existence:93](C:/Users/SIGMA/Documents/Trading_2/Terminal/Headless/llm_contract.py:93).

A separate ContinuousBrain path can supplement a muscle abstention by staging. Its block decision uses macro blackout/equity ≤4,775, not the computed perspective blocks, and `_maybe_stage` uses fixed ATR stops/fixed R targets. Downstream muscle checks need separate verification before claiming a bypass: [block/stage:243](C:/Users/SIGMA/Documents/Trading_2/Terminal/Headless/arena_continuous_brain.py:243), [fixed terms:295](C:/Users/SIGMA/Documents/Trading_2/Terminal/Headless/arena_continuous_brain.py:295).

## Isolated probes and limits

Executed named current AST nodes in memory; no production-module imports, broker IPC, network requests, writes, sleeps, Git operations, or full scripts.

| Probe input | Current output | Interpretation |
|---|---|---|
| Six audit layers return SKIP | CERTIFIED_100_PERCENT_PRISTINE | Aggregation is not fail-closed for nonpassing statuses. Synthetic classifier probe, not a claim all production layers currently return SKIP. |
| Fresh filesystem mtime, wrong protocol, epoch 0, denied authorization, unreconciled positions | PASS; positions_in_sync=True; assets_serialized=0 | Fresh mtime is accepted without semantic integrity or reconciliation. |
| Fake balance/equity 4,780 USD plus pending order | PASS; stressed equity 4,780; cushion 5; risk 0 | Pending risk and operating-floor violation do not change the audit verdict. |
| MT5 initialization false, stale denied snapshot containing positions/pending | Cash-flat and queue-clean claims; denial omitted; policy 12 retained | Unavailable broker state can become apparently known empty state. |

## Proposed arbitration and independent challenge

Apply canonical hard vetoes first. Seal an immutable bundle and policy digest before local specialist reviews, obtain their independent initial findings before revealing Arena's stance, and group evidence by its underlying provider/market stream. Arena is an interpretation of evidence, not an independent market observation. Multiple local downloads of the same Binance state are also correlated observations.

**Challenge to the parent proposal:** keeping a fixed bundle hash from :25/:55 through :29/:59 prevents evidence substitution, but its quotes/depth will be four minutes old at action time. Hash agreement cannot satisfy freshness. **Rebuttal/refinement:** preserve the original response-to-bundle binding and acquire a separate fresh revalidation bundle at :29/:59. Record its differences explicitly. If candidate validity, price/venue basis, source availability, policy or joint risk changes materially, reject the old proposal or request one bounded re-review. Do not silently replace facts under the original digest. This preserves the requested cadence without using stale orderflow to authorize action.

Another distinction: `100 × P(net incremental PnL > 0)` is a probability score only after chronological calibration; it is not EV. A hypothetical 90% chance of +1 USD and 10% chance of -20 USD earns 90/100 probability but has EV -1.10 USD. A process-compliance rubric is a separate score. Neither score can replace a positive lower bound on incremental utility and feasible stress/floor checks.

### Proposed Bayesian and expected-utility rule

For thesis-valid state V, invalidated state I, and unique observations E:

```text
Posterior odds(V | E) = prior odds(V) × joint likelihood ratio(E).
```

Use a calibrated joint model or source-group feature model. Do not multiply individual likelihood ratios for duplicate/correlated evidence. An LLM opinion receives a predictive weight only after measuring its incremental contribution conditional on the underlying facts on chronologically held-out decisions. Named persona agreement is not a likelihood update. Outcome-selected anecdotes, including one held trade later hitting TP, cannot establish the superiority of HOLD or invalidate an EXIT policy.

For an existing position, compare future incremental monetary outcomes from the current executable mark:

```text
ΔU(HOLD, EXIT) =
  E[future incremental net PnL if held | E]
  - E[future incremental net PnL if exited | E]
  - incremental tail-risk penalty
  - incremental opportunity/capacity cost.
```

Include broker Bid/Ask, account-currency conversion, commissions, swap, slippage, gaps and a specified horizon. Current PnL is already reflected in the current mark; do not double-count it or anchor decisions to entry. Compare against a genuine non-increasing broker close. Any revised SL/TP must also be evaluated as a distinct feasible action.

For a pending order:

```text
U(KEEP) = P(fill | E) × E[net PnL | fill, E]
          - contingent-risk reservation/opportunity cost
          - adverse-selection and tail penalty.
U(DELETE) = value of released risk/margin and feasible alternatives.
```

Give CFD queue priority no assumed credit without venue evidence. A Binance orderbook is not the broker CFD execution queue. The admission feasible set must preserve ≥4,795 USD stressed equity with all positions, existing pending orders and proposed pending orders, conservative execution costs, and simultaneous-fill capacity. Nominal four-slot capacity does not replace risk or joint-fill enforcement.

Select only when the lower confidence bound of ΔU against the best feasible alternative is positive. Priors, payoff/utility functions, source weights, costs, horizons and confidence thresholds require preregistration and chronological calibration. These formulas specify a proposed decision policy, not a validated edge. [Gelman's institutional decision-analysis discussion](https://statmodeling.stat.columbia.edu/2004/11/16/institutional_d/) supports explicit justified models/utilities and evaluation of their assumptions.

### Machine-readable response and action lifecycle proposal

```text
Response = {
  schema, cycle_id, conversation_id, turn_id,
  input_bundle_hash, policy_hash, observed_at, expires_at,
  ticket_or_candidate_id, action,
  evidence_refs, contrary_evidence_refs, source_lineages,
  calibrated_probability_or_null, incremental_utility_interval_or_null,
  invalidation_condition, rationale_summary
}

validate schema, identity, hashes, ticket, expiry and complete receipts
deduplicate source lineages
check canonical vetoes
if new-risk validation unavailable: HOLD_VALIDATION
else compute joint posterior and feasible action utilities
revalidate against fresh bundle; record changed evidence
if positive LCB(ΔU) and feasible joint stress/capacity:
    persist unique action intent and idempotency key
    perform one permitted action through execution authority
    reconcile broker acknowledgement and final ticket state
else:
    record abstention and the failed evidence/gate
```

Missing data for new risk means HOLD_VALIDATION. It does **not** automatically DELETE a valid existing limit or EXIT an existing position. Existing-order actions need a proven invalidation, policy expiry, deterministic risk-reduction requirement, or positive incremental utility advantage. Deterministic emergency risk reduction has its own verified route rather than relying on an LLM score. No schema or transport layer should gain execution authority through prose.

### Proposed 0–100 process rubric for EXIT/DELETE disagreements

Score each proposed action independently. This is an evidence-quality rubric, separate from calibrated `100 × P(net incremental PnL > 0)`.

| Dimension | Maximum | Required support |
|---|---:|---|
| Provenance/freshness | 20 | Valid venue/source/receipt timestamps, fixed bundle identity and complete broker state. |
| Thesis/invalidation | 20 | Observed trigger, mechanism, horizon and contradictory evidence. |
| Conditional net utility | 20 | Calibrated probabilities, full execution costs, uncertainty and alternative-action comparison. |
| Capital/capacity | 20 | 4,775 floor/4,795 operating threshold; all contingent orders; joint four-filled-slot simulation. |
| Execution feasibility | 10 | Correct ticket/action, broker-supported prices, genuine close/cancel semantics. |
| Macro/session | 10 | Calendar age/coverage, relevant asset events and broker session/rollover conditions. |

Hard failures override the total: unknown broker state/identity, mismatched cycle/hash, expired evidence, denied new-risk authorization or failed joint stress/capacity. Suggested preregistered governance bands are ≥80 for eligible consideration with positive utility LCB, 60–79 for one bounded targeted remeasurement, and <60 to reject the recommendation. The bands are proposed policy choices, not calibrated financial probabilities.

## Primary-source support and validation priorities

Binance depth documentation provides `lastUpdateId`, event/output time and transaction time, and price/quantity rows; a current L2 receipt is not evidence of wallet identity or 180-second persistence. [Binance market-data/depth documentation](https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data).

Necessary acceptance tests are adversarial rather than implementation mirrors: old-but-long Arena answer, missing/multiple tabs, duplicate Enter/click, generation timeout, wrong bundle/policy/ticket, replayed response/action, future/repeated market timestamps, incomplete HTF bins, missing/expired calendar coverage, denied provenance, IPC failure distinguishable from empty book, all pending joint fills, broker-currency conversion, partial/rejected close/cancel, process crash between intent and acknowledgement, and publication with unrelated pre-staged files. Run no live actions to perform these tests. Use dependency-injected fixtures and recorded receipts, then explicitly bounded paper/shadow validation before any execution promotion.

The reviewed source supports neither blanket 100%/10-of-10 certification nor statistical independence from a persona count. The useful foundations are observed-only publication, deterministic hard gates, structured candidate binding and modular specialist checks. Their missing connection must be proved end-to-end with evidence-bound, fresh, idempotent arbitration.
