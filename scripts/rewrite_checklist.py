import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'r', encoding='utf-8') as f:
    old = f.read()

# Extract the completed cycle blocks (012-028)
# Find from first completed cycle to just before Cycle_029
start = old.find("### 🟢 Cycle_012 Scorecard: COMPLETED")
end_028 = old.find("### ⏳ Cycle_029 Scorecard:")
if end_028 == -1:
    end_028 = old.find("### 🟢 Cycle_029 Scorecard:")  # just in case
if end_028 == -1:
    # fallback: find Cycle_029 any way
    end_028 = old.find("Cycle_029 Scorecard:")
    if end_028 != -1:
        # go back to find the ### before it
        prev_newline = old.rfind('\n', 0, end_028)
        end_028 = prev_newline + 1

completed_history = ""
if start != -1 and end_028 != -1:
    completed_history = old[start:end_028].rstrip() + "\n"
    print(f"Extracted completed history: {len(completed_history)} chars (cycles 012-028)")
else:
    print(f"WARNING: Could not extract. start={start}, end_028={end_028}")
    # Try alternate approach
    end_028_alt = old.find("### ⏳ \n")
    if end_028_alt == -1:
        end_028_alt = len(old)
    completed_history = old[start:end_028_alt].rstrip() + "\n"
    print(f"Fallback: Extracted {len(completed_history)} chars")

# Build the new clean file
new_file = """# 📋 ON WAKEUP: Mandatory Trading Intelligence & Execution Protocol

> **GOVERNANCE STATUS**: CANONICAL PRODUCTION CYCLE PROTOCOL (Single Source of Truth)
> **Location**: `Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md`
> **Enforcement**: Mandatory on EVERY cycle wake-up. Antigravity, Arena.ai, and Z.ai each independently follow this protocol.
> **Pacing**: 20-minute cycle interval via persistent AutoWake timer.
> **Data Ground Truth**: USE ONLY the authoritative 360° master dossier files in `docs/dossiers/`.

---

## 🎯 Objective

Establish a continuous, evidence-driven, multi-agent trading intelligence loop that:
- Performs exhaustive asset-level forensics on every eligible asset's full-length dossier
- Independently validates trade opportunities across three AI systems
- Maintains consistent portfolio records
- Executes only when predefined risk and confluence requirements are satisfied

---

## 🛡️ Non-Negotiable Operating Principles

1. **Complete coverage**: Every eligible asset and every associated Markdown dossier must be examined individually. Skipping, summarising without inspection, or selectively reviewing documents is strictly prohibited.
2. **Independent intelligence**: Antigravity, Arena.ai, and Z.ai must each conduct their own analysis.
3. **Verified completion**: Wait for both external systems to finish before making the final comparison.
4. **Data consistency**: Keep the collaborative intelligence ledger synchronised with the live portfolio and order registry.
5. **Evidence-driven execution**: Never place a trade solely on the basis of consensus, incomplete analysis, or an unverified setup.
6. **Continuous operation**: Repeat the complete workflow every 20 minutes after each cycle finishes.
7. **Failure handling**: If a system, daemon, or data source fails, report the failure, preserve the current state, and avoid treating incomplete work as completed.
8. **Mandatory Exclusive Dossier Use**: ALL analysis MUST use ONLY the comprehensive 360° master dossier files (`docs/dossiers/<ASSET>_MASTER_DOSSIER.md`). Isolated indicators or un-cross-referenced columns are strictly forbidden.

---

## 🔄 THE 7-STEP CANONICAL CYCLE PROTOCOL

On every wakeup, execute these 7 steps in order. Do NOT check a step until the work is physically done.

### Step 1: Identify Eligible Assets
- Identify and list ALL assets currently within the defined spread range.
- Read `00_MT5_Account_Telemetry.parquet` and filter against broker spread thresholds (TradFi ≤ 5.0 bps, Crypto ≤ 25.0 bps).
- Establish the complete list of eligible candidates (across Crypto, Forex, Indices, and Metals) before proceeding.

### Step 2: Conduct Comprehensive Asset-Level Forensics
- **Read, analyse, and perform forensic examination of every individual dossier FULL LENGTH document** belonging to every eligible asset across CRYPTO, FOREX, INDICES and METALS.
- Every `.md` file associated with each eligible asset must be examined individually. Skipping, summarising without inspection, or selectively reviewing documents is strictly prohibited.
- Based on this comprehensive review, formulate high-confluence trade setups supported by evidence, market conditions, and the available intelligence.
- This requirement is mandatory and applies equally to Antigravity, Arena.ai, and Z.ai. Each system must independently perform its own analysis using all relevant dossier documents and available capabilities.

### Step 3: Synchronise the Intelligence Ledger and Portfolio Registry
- Review and update `TRI_COUNCIL_COLLABORATIVE_INTELLIGENCE_LEDGER.md` using the latest information from `LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md`.
- Ensure the collaborative intelligence ledger accurately reflects the current portfolio, open positions, pending orders, and relevant order-registry information.
- Preserve data integrity and ensure all updates are consistent with the authoritative portfolio and order records.

### Step 4: Dispatch Independent Analysis to Arena.ai and Z.ai
- Prepare comprehensive, asset-specific prompts for both Arena.ai and Z.ai.
- Dispatch the prompts and instruct each system to independently analyse every eligible asset and all associated dossier documents, leveraging all relevant skills, tools, and analytical capabilities available to it.
- Require each system to produce its own evidence-backed trade candidates, confluence assessments, risk analysis, entry criteria, invalidation levels, and execution recommendations.
- Ensure that both systems complete their analyses independently before proceeding to the final trade decision.

### Step 5: Activate the AutoWake Hard-Rock Daemon
- Once the required analyses have been initiated, start the AutoWake Hard-Rock Daemon.
- Configure the daemon to monitor the completion status of both Arena.ai and Z.ai.
- Enter sleep or idle mode while the daemon monitors progress.
- The daemon must wake the workflow when both systems have completed their assigned analyses.
- Do not proceed to trade execution merely because prompts have been dispatched. Confirm that the required analyses are complete and available for review.

### Step 6: Compare Intelligence and Execute Trades
After waking, perform a structured comparison of the three independent analyses:
- **Antigravity**: Internal dossier forensics, market analysis, and trade formulation.
- **Arena.ai**: Independent asset analysis and trade recommendations.
- **Z.ai**: Independent asset analysis and trade recommendations.

Evaluate each candidate against the available evidence, confluence strength, market conditions, portfolio exposure, liquidity, execution feasibility, and risk-to-reward profile.
- Identify areas of agreement and disagreement across all three analyses.
- Resolve discrepancies through evidence-based verification rather than blindly accepting a majority opinion.
- Select only trades that satisfy the predefined strategy rules, risk limits, and execution criteria.
- Before placing any order, verify that the setup remains valid under current market conditions and that the portfolio and order registry are up to date.
- Execute only qualified trades. If no candidate meets the required criteria, do not force a trade.

### Step 7: Restart the 20-Minute AutoWake Cycle
1. Update the collaborative intelligence ledger and portfolio/order registry with the latest verified outcomes.
2. Set the AutoWake timer for 20 minutes.
3. Enter sleep or idle mode while awaiting the next wake-up.
4. When awakened, restart the entire protocol from Step 1.

---

## 📊 CYCLE SCORECARD TEMPLATE

> **IMPORTANT**: All checkboxes in a new cycle scorecard MUST start as `- [ ]` (unchecked).
> A step may only be checked `- [x]` AFTER the work described in that step has been physically completed and verified.
> Pre-checking or copy-pasting checked templates is strictly prohibited.

```
### ⏳ Cycle_NNN Scorecard: IN PROGRESS
**Started**: YYYY-MM-DD HH:MM:SS IST (YYYY-MM-DD HH:MM:SS UTC)

- [ ] **Step 1**: Identify eligible assets (spread screening across all 4 macro classes)
- [ ] **Step 2**: Read FULL LENGTH dossier for EVERY eligible asset and formulate setups
- [ ] **Step 3**: Synchronise intelligence ledger and portfolio registry
- [ ] **Step 4**: Dispatch independent analysis to Arena.ai and Z.ai
- [ ] **Step 5**: Activate AutoWake daemon and await completion of both systems
- [ ] **Step 6**: Compare 3-way intelligence and execute only qualified trades
- [ ] **Step 7**: Update records and restart 20-minute AutoWake cycle
```

---

## 📜 COMPLETED CYCLE HISTORY

""" + completed_history + """
---

### ⏳ Cycle_029 Scorecard: IN PROGRESS
**Started**: (Awaiting next 20-minute timer wakeup)

- [ ] **Step 1**: Identify eligible assets (spread screening across all 4 macro classes)
- [ ] **Step 2**: Read FULL LENGTH dossier for EVERY eligible asset and formulate setups
- [ ] **Step 3**: Synchronise intelligence ledger and portfolio registry
- [ ] **Step 4**: Dispatch independent analysis to Arena.ai and Z.ai
- [ ] **Step 5**: Activate AutoWake daemon and await completion of both systems
- [ ] **Step 6**: Compare 3-way intelligence and execute only qualified trades
- [ ] **Step 7**: Update records and restart 20-minute AutoWake cycle

"""

with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'w', encoding='utf-8') as f:
    f.write(new_file)

print(f"DONE. New file size: {len(new_file)} chars ({len(new_file.splitlines())} lines)")
print(f"Old file was: {len(old)} chars ({len(old.splitlines())} lines)")
print(f"Reduction: {len(old) - len(new_file)} chars removed ({(1 - len(new_file)/len(old))*100:.1f}% smaller)")
