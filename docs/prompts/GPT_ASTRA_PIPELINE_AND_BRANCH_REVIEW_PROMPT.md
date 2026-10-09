# ================================================================================
# INSTITUTIONAL PIPELINE, BRANCH AUDIT & AUTONOMOUS FIX DIRECTIVE
# TARGET MODEL: GPT ASTRA (AUTONOMOUS CODEBASE ARCHITECT & SENIOR QUANT ENGINEER)
# FROM: ANTIGRAVITY AUTONOMOUS ORDER DESK & COLLABORATIVE QUANT COUNCIL
# REPOSITORY: https://github.com/kbsingh1399/Trading_2 (Branch: main)
# LOCAL ROOT: C:\Users\SIGMA\Documents\Trading_2
# ================================================================================

You are GPT Astra, an Elite Institutional Quantitative Software Architect, Microstructure Engineer, and Senior Systems Auditor. You have direct read/write access to this repository.

### MISSION OBJECTIVE:
Conduct a comprehensive end-to-end review of our live quantitative trading pipeline and git branches, identify any latent architectural, mathematical, or runtime errors, and **DIRECTLY FIX THEM IN THE CODEBASE AND COMMIT TO MAIN (OR A CLEAN PR BRANCH)** so the local execution desk does not require manual intervention.

---

## 1. STRATEGIC NARRATIVE & CURRENT OPERATIONAL CONTEXT

### A. The Evolution to Microsoft Copilot Studio (Claude Opus 5.5)
- We have fully transitioned from Arena.ai to **Microsoft Copilot Studio (Claude Opus 5.5 - Chief Quantitative Strategist & Second Brain)** connected via Chrome DevTools Protocol (CDP port 9222).
- Our live broker execution desk connects via native IPC to **MetaTrader 5 Account #5064568 (Blueberry Markets SVG-Live)**.
- **One-Way Read-Only External Channel Invariant**:
  * Claude Opus 5.5 in Copilot Studio is an external, read-only web client. It has zero local file access and zero write access to GitHub.
  * Our local Python bridge (`Terminal/copilot_studio_bridge.py`) serializes live MT5 account metrics and our 24-asset orderflow telemetry matrix directly into the prompt text, dispatches it to Copilot Studio via CDP, harvests the completed ruling from the browser DOM, records it into `docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md`, and pushes it to GitHub `main`.

### B. Live Capitalization & Risk Milestones (Real Performance)
- **Starting Capital**: 5,000.00 USD
- **Current Balance / Equity**: **4,896.55 USD** (97.93% capital preserved; 100% Cash Reserves | 0.00 USD Margin Used).
- **Hard Capital Floor (G-1)**: **4,775.00 USD** (Maximum allowable lifetime drawdown: 4.50% / 225.00 USD).
- **Operating Safety Buffer**: **4,795.00 USD** (Mandatory >= 20.00 USD safety cushion above floor).
- **Live Floor Cushion**: **+121.55 USD** above hard floor (+101.55 USD above operating buffer).
- **Realized PnL Banked Today**: **+84.05 USD Net Cash Profit** across 17 completed trades (**64.7% Win Rate: 11 Wins / 6 Losses**).
  * Notable Wins: BTCUSD Take Profit hit at 83,250.00 USD (+24.00 USD cash); SP500 Take Profit at 7,798.50 USD (+34.00 USD); USWTI Take Profit at 92.000 USD (+30.00 USD); USWTI Phase 0 Breakeven ratchet locked (+0.70 USD guaranteed).
- **Active Exposure**: **0 Open Positions | 0 Pending Orders** (Queue 100% clean | All 4 position capacity slots vacant).

---

## 2. CANONICAL REPOSITORY ARTIFACTS & LINKS

All inspection and modifications must be anchored in our primary GitHub repository:
- **Repository URL**: `https://github.com/kbsingh1399/Trading_2` (Branch: `main`)
- **Master Enforcement Rules**: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/AGENTS.md`
- **Active Operational Context**: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md`
- **Thinking Chain Protocol V2.0**: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md`
- **Round 2 Thinking Chain Audit**: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/reviews/ROUND2_THINKING_CHAIN_AUDIT.md`
- **Decision Gates V3 Reference Implementation**: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/decision_gates_v3.py`
- **Live Telemetry Snapshot**: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json`
- **Collaborative Order Desk Blackboard**: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md`
- **360-Degree Forensic Verifier**: `https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/chain_verification_360.py`

AST Knowledge Graph (for token-efficient queries):
- Index: `graphify-out/graph.json` (7,400+ nodes). Run `python -m graphify query "<concept>"` to query.

---

## 3. AUDIT & FIX WORKLIST (ACTIONABLE DEFECTS IDENTIFIED BY OPUS 5.5 & SWARM)

Inspect the codebase and directly resolve the following 6 identified defect categories:

### Issue 1: Host Machine Clock Drift & Tick Age Dynamic Calibration
- **Symptom**: In recent cycles, `broker_tick_age_s` serialized in telemetry ran negative (-0.6s to -28.67s) because the local host machine clock is ~29 seconds behind broker server time.
- **Vulnerability**: In `Terminal/decision_gates_v3.py` and `Terminal/Omni_Trader.py`, `pre_send_gate` verifies tick freshness within tight boundaries. If local host time drifts further, authentic live ticks may be falsely rejected.
- **Required Fix**:
  * In `Terminal/decision_gates_v3.py` and `Terminal/Omni_Trader.py`, implement an adaptive broker clock offset calibration that calculates `delta = broker_server_time - local_host_time` dynamically using MT5 tick timestamps, normalizing tick age so that local clock skew does not cause false rejections.
  * Ensure fail-closed safety: if tick delta exceeds ±60 seconds from broker quotes, reject; otherwise, accurately normalize tick age.

### Issue 2: Telemetry Snapshot Capacity Metadata Alignment
- **Symptom**: In `docs/telemetry/live_snapshot_latest.json`, the metadata header currently contains legacy comments stating `max_concurrent: 12` and "pending orders do not consume slots".
- **Vulnerability**: External models (like Claude Opus 5.5) reading the snapshot observe a contradiction against our code in `Terminal/live_admission.py` and `Terminal/Omni_Trader.py`, which strictly enforce `max_concurrent: 4` and count pending orders toward floor risk.
- **Required Fix**:
  * Update `Terminal/Data_Factory/autonomous_telemetry_git_daemon.py` to ensure the generated snapshot capacity block explicitly reflects the active 4-slot capacity rule, accurate margin calculations, and explicit contingent book risk.

### Issue 3: Multi-Timeframe Regime Serialization (1H & 4H Bar Depth)
- **Symptom**: Opus 5.5 noted that 1H closes were omitted from the telemetry JSON snapshot, and BTC had only 29 of the 31 required 4H closes, causing external regime classifiers (`classify_regime`) to default to `UNDEFINED`.
- **Required Fix**:
  * In `Terminal/Data_Factory/autonomous_telemetry_git_daemon.py`, ensure that for all 24 assets, the telemetry snapshot serializes at least 35 1H closes and at least 35 4H closes alongside the 15m candle indicators, allowing deterministic regime classification across all models.

### Issue 4: Macro Economic Calendar Coverage Extension
- **Symptom**: `Data/macro_calendar.json` currently concludes at the Oct 07 FOMC meeting and lacks forward scheduling for next week.
- **Required Fix**:
  * Update `Data/macro_calendar.json` with the upcoming high-impact economic releases for the upcoming week (e.g. US CPI on October 14, 2026 at 12:30 UTC, Retail Sales, and central bank speeches) with exact UTC timestamps, currencies, and blackout buffer intervals.

### Issue 5: Remote Branch Sanitation & Reconciled Git Trunk
- **Symptom**: Multiple remote legacy branches exist on origin (`arena/01a100cd-trading-2`, `arena/01a10721-trading-2`, `arena/24eb818b-trading-2`, `arena/4adf3661-trading-2`, `arena/83d03e3f-trading-2`).
- **Required Action**:
  * Audit all remote branches against `origin/main`.
  * Ensure all valuable improvements or patches from those branches are merged into `main`.
  * Prune or delete obsolete remote branches if appropriate, ensuring `main` is the clean, authoritative, and deployable trunk.

### Issue 6: Comprehensive Pytest & 360-Degree Forensic Test Suite Validation
- **Requirement**:
  * Run the full pytest suite: `pytest Tests/` (must pass 415+ tests, 0 failures).
  * Run `python Terminal/chain_verification_360.py` and verify that Layer 1 (Feeds/Data), Layer 2 (Causal Indicators), and Layer 3 (Broker & Capital Floor) report `CERTIFIED_100_PERCENT_PRISTINE`.
  * Ensure zero temporary or scratch scripts remain in `scratch/`.

---

## 4. EXECUTION PROTOCOL & EXPECTED OUTPUT

1. **Autonomous Fix & Verification**:
   - Perform the code changes directly in the appropriate files.
   - Run tests and verifications locally to confirm zero regressions.
   - Commit your fixes with clear, conventional commit messages (e.g., `fix(microstructure): calibrate broker server time skew in pre_send_gate`, `feat(telemetry): serialize 1H/4H closes and align capacity metadata`).
   - Push to `main` (or provide a clean PR merge).
2. **Audit Report Deliverable**:
   - Produce a concise summary explaining:
     * Specific files modified and the rationale for each change.
     * Verification test results (`pytest` output, `chain_verification_360.py` output).
     * Final branch status and remote synchronization.
     * Confirmation that the live trading desk can operate seamlessly without manual operator adjustments.
