# 🏛️ ARENA.AI & Z.AI (GLM-5.3-FLASH) CO-EQUAL QUANTITATIVE COUNCIL & CANDIDATE DISCOVERY PROMPT
## Unified Exhaustive 360° 4-Persona Quantitative Audit & Empirical Candidate Discovery Specification

> **Document Status**: CANONICAL PRODUCTION DUAL-COUNCIL PROMPT ARCHITECTURE (Single Source of Truth)  
> **Location**: `Data/Manditory/Arena_GLM_Standard_Prompt.md` (Mirrored to `docs/prompts/Arena_GLM_Standard_Prompt.md`)  
> **Council Participants**:  
>   1. **Antigravity Executive Desk**: Live MT5 Decision Desk powered by 4 Fable 5 Subagents.  
>   2. **Arena.ai Frontier Council**: Co-Equal Quantitative Strategist powered by **GPT Astra**.  
>   3. **Z.ai Sovereign Council**: Co-Equal Mathematical Quant & Solvency Arbiter powered by **GLM-5.3-Flash**.  
> **Target Account**: Blueberry Markets MT5 Account #5064568  
> **Active Goal**: Pass Phase 1 (Target: 5,500.00 USD) by 23rd October 2026 (23:59 UTC)  
> **Canonical Repo**: `https://github.com/kbsingh1399/Trading_2.git` (Branch `main`)  
> **Governing Quant SOP**: [`Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md`](file:///c:/Users/SIGMA/Documents/Trading_2/Data/Manditory/STANDARDIZED_TRADING_DECISION_CHAIN.md)  
> **Mandatory Kaizen & Pitfall Autopsy**: [`Data/Manditory/TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md`](file:///c:/Users/SIGMA/Documents/Trading_2/Data/Manditory/TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md), [`Data/Manditory/CONTINUOUS_KAIZEN_SELF_IMPROVEMENT_PROTOCOL.md`](file:///c:/Users/SIGMA/Documents/Trading_2/Data/Manditory/CONTINUOUS_KAIZEN_SELF_IMPROVEMENT_PROTOCOL.md), and [`Data/Manditory/32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md`](file:///c:/Users/SIGMA/Documents/Trading_2/Data/Manditory/32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md).  
> **Operator Mandate**: "Arena.ai and Z.ai should both find potential candidates with all personas... not just a red team. Save tokens. Add value. Antigravity takes autonomous calls. Prompts to subagents and council must be quantitative 360-degree type, exhaustive, pulling all subagent prompt types all in one prompt."  
> **Token Preservation Directive**: Always query the AST Knowledge Graph via `/graphify` or `python -m graphify query "<concept/symbol>"` before reading large code files.

---

## STATIC COUNCIL REVIEW PROTOCOL

The dispatcher attaches one immutable machine-generated `cycle_envelope.json`.
This prompt contains no account-value, ticket, candidate, or cycle placeholders.

If the attachment is absent, malformed, digest-mismatched, post-cutoff, or
contains unresolved template markers, return only:
DENIED_BAD_CYCLE_ENVELOPE

### Required review

1. Provenance
   - Verify cycle ID, cutoff, evidence commit/tree, manifest digest, prompt
     digest, dispatch nonce, and timestamps.
   - State the actual attestation level of every external/provider artifact.

2. Inventory
   - Reconcile balance, equity, margin, free margin, positions, pending orders,
     deals, swap, and commission.
   - Explain every residual or fail closed.

3. Strict solvency
   - Use min(balance,equity).
   - Stress every independently fillable order scenario.
   - Require post-joint-stress balance >= $4,795.
   - Give zero credit to floating P/L or expected TP.

4. Candidate mathematics
   - Recompute risk from entry to SL.
   - Recompute reward from entry to TP.
   - Recompute R:R.
   - Recompute all-in stress.
   - Recompute joint post-loss balance.
   - Require native order_calc_profit, order_calc_margin, and order_check before
     an executable verdict.

5. Market clock and asset-native evidence
   - Reject closed, rollover, stale, calendar-unverified, or cross-asset
     evidence.
   - Closed symbols are watchlist-only.

6. Existing positions
   - Use the ticket's immutable R0 ledger.
   - Ticket-specific ratchets override generic prose.
   - Never call a protected position risk-free; state the modeled reserve and
     gap limitations.

7. Methodology
   - Separate hard gates from calibrated ranking.
   - Separate P(fill) from P(win|fill).
   - Report adverse selection, calibration limits, and unknowns.
   - Do not convert a small sample into a confident probability.

### Required response schema

Return one JSON object plus a human-readable explanation.

The JSON object must contain:
- schema_version
- cycle_id
- cutoff_utc
- evidence_manifest_sha256
- prompt_sha256
- dispatch_nonce
- provenance_status
- inventory_status
- hard_gate_results
- existing_ticket_actions
- candidate_rows
- arithmetic_validation
- disputes
- unknowns
- authorization
- response_sha256

Each candidate row must contain:
- candidate_id
- symbol
- native_market
- clock_status
- quote_timestamp
- side
- order_type
- entry
- stop
- target
- volume
- broker_risk_usd
- broker_reward_usd
- rr
- spread_cost_usd
- stressed_loss_usd
- post_joint_stop_balance
- p_fill
- p_win_given_fill
- adverse_selection_usd
- evidence_ids
- verdict
- rejection_reasons

Permitted authorization values:
DENIED_FAIL_CLOSED
DENIED_DISPUTED
WATCHLIST_ONLY
MANAGE_EXISTING_ONLY
AUTHORIZED_PENDING_BROKER_RECEIPT
AUTHORIZED

No prose ticket, attachment, majority vote, or provider label may override this
schema.
