# OMNI Sentinel multi-agent wake protocol

This protocol implements the user's request for multiple independent checks of current market intelligence and Hyperdash on every scheduled Sentinel wake. It is supervisory. The execution daemon retains its own deterministic gates and dispatch schedule.

## Wake sequence

1. Run the account-bound Sentinel with --enforce --journal. Verify account 5064568, USD currency, original capital 5000, floor 4775, risk 10–20 per trade, risk cap 10 below equity 4800, maximum two positions, pending inventory and sticky halt. A failed inventory read is unknown inventory, not zero. Execute only already authorized protective cancellation/closing. Never open trades, restart the daemon, clear a halt or edit trading policy during a scheduled run.
2. Save one timestamped review context beneath Data/Omni/sentinel/debate. Include the Sentinel audit path/hash, latest completed decision and slot, daemon/process status, raw Hyperdash payloads or exact archived references, RSS headlines with publication/receipt timestamps, dated event calendar metadata, covariance metadata and uplift qualification. Fetch at most eight assets concurrently. Keep venue timestamps and local receipt timestamps separately. Record failed, missing or stale inputs explicitly. Unknown macro information is not a neutral score. Do not normalize a clock discrepancy silently or claim absent depth outside the observed book is zero.
3. Use collaboration.spawn_agent to start three independent read-only reviewers in parallel. Give every reviewer the same archived context path and review as-of time. Each reviewer may check a bounded additional source, but must label later observations with their own timestamps. Do not create separate user-owned chats for these reviewers.
4. Assign the roles below. Each role returns a verdict, at most three material findings, evidence references, unknowns, confidence in data validity and one concrete challenge to another role. Do not ask reviewers to maximize agreement or invent calibrated probabilities.
5. Route each challenge to the relevant reviewer for one short rebuttal. The risk reviewer adjudicates remaining conflicts against deterministic invariants. Do not permit a majority vote to overrule a hard veto. If data validity is unresolved, the supervisory conclusion is HOLD_VALIDATION. If the reviews do not finish promptly, record REVIEW_INCOMPLETE and report the missing review; do not delay or interfere with order dispatch. Aim to finish the supervision within the current minute, but report actual completion time and lateness rather than claiming a guaranteed latency.
6. Append the structured debate, references and dissent to a uniquely named JSON file and audit index. Append the status and evidence paths to session history, then run the workspace-scoped parity script. Return the account status card, current candle decision and asset vetoes, role conclusions/disagreement, infrastructure findings and exact next UTC wake at minutes 14, 29, 44 or 59.

## Independent roles

| Role | Required checks | Must challenge |
| --- | --- | --- |
| Orderflow conviction analyst | Volatility-normalized L2 imbalance; aggressor tape; liquidation and stop corridor coverage; fuel-to-friction ratio; L3 persistence and cancellation; signal/broker basis; unknown versus absent data | An apparent directional setup that lacks observed depth, reliable timing or sufficient net payoff |
| Macro intelligence analyst | Freshness and scope of RSS sentiment; publication time versus receipt time; asset-specific macro exposure; CPI/NFP/FOMC dated blackout completeness; calendar refresh failures and conflicting sources | A technical setup whose macro regime assertion is unsupported, stale or contradicted |
| Portfolio risk reviewer | Broker equity and inventory; floor cushion; stop-plus-friction risk and margin; correlation/covariance validity; second-position uplift qualification; ratchet and order hygiene; time alignment and causal completed bars | Any recommendation relying on incompatible clocks, invalid sizing, unqualified models or breached capital constraints |

## Structured debate record

Required top-level fields: schema_version, wake_due_utc, review_started_utc, review_completed_utc, account_id, slot, context_path, context_sha256, data_quality_flags, reviewers, challenges, rebuttals, deterministic_vetoes, supervisory_verdict, protective_actions, execution_authority, next_wake_utc.

Each reviewer finding needs: claim, observation_or_inference, source_reference, source_event_time, received_at_utc, missing_information, proposed_validation. Null values indicate unknowns. Any confidence value describes evidence quality; it is not a forecast win rate. Set execution_authority to protective_only. Summaries must distinguish the daemon's actual decision from the reviewers' supervisory opinion.

## Current unresolved findings to recheck

- Hyperdash event timestamps have led the host by approximately 20 seconds. Confirm clock alignment independently; do not relax freshness gates to hide this.
- The broker bar reader has returned wall-time-looking bar opens approximately three hours ahead of UTC without normalization. Check both bar timestamp convention and cache cadence before trusting features or covariance fitted from those bars.
- Dated macro-calendar refresh returned HTTP 403, while a cached calendar returned NO_EVENT. Cached coverage is not a fresh source certification.
- The uplift artifact no longer qualifies against the revised ratchet policy and currently blocks second positions. Do not retag its manifest to bypass qualification.

Use USD and plain math in reports. A modeled stop-profit floor is not a guaranteed realized profit.
