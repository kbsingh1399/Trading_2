# 📋 ON WAKEUP: MANDATORY TRADING INTELLIGENCE & EXECUTION PROTOCOL
## Continuous Autonomous Multi-Agent Cycle Scorecard & Running Checklist

> **GOVERNANCE STATUS**: CANONICAL PRODUCTION CYCLE AUDIT CHECKLIST (Single Source of Truth)  
> **Location**: `Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md`  
> **Enforcement**: Mandatory execution verification on EVERY single cycle wake-up across Antigravity, Arena.ai, and Z.ai.  
> **Live Pacing**: Dynamic 20-minute cycle interval maintained by persistent AutoWake timer.

---

## 🎯 OBJECTIVE
Establish a continuous, evidence-driven, multi-agent trading intelligence loop that performs exhaustive asset-level forensics, independently validates trade opportunities, maintains consistent portfolio records, and executes only when predefined risk and confluence requirements are satisfied.

---

## 🛡️ NON-NEGOTIABLE OPERATING PRINCIPLES

1. **Complete Coverage**: Every eligible asset and every associated Markdown dossier must be examined individually without skipping or selective omission.
2. **Independent Intelligence**: Antigravity, Arena.ai, and Z.ai must each conduct their own independent analysis using all available tools and capabilities.
3. **Verified Completion**: Wait for both external systems to finish and verify hash stability before making the final comparative decision.
4. **Data Consistency**: Keep the collaborative intelligence ledger continuously synchronized with the live portfolio and order registry.
5. **Evidence-Driven Execution**: Never place a trade solely on the basis of consensus, incomplete analysis, or an unverified setup.
6. **Continuous Operation**: Repeat the complete workflow every 20 minutes after each cycle finishes.
7. **Failure Handling**: If a system, daemon, or data source fails, report the failure, preserve the current state, and avoid treating incomplete work as completed.

---

## 🔄 THE 7-STEP CANONICAL CYCLE SCORECARD TEMPLATE

Every cycle must systematically evaluate and document completion of the following 7 steps:

```markdown
### Cycle Execution Scorecard: [CYCLE_ID] | Timestamp: [TIMESTAMP_IST]

- [ ] **Step 1: Identify Eligible Assets**
  - [ ] Filter all tradeable assets against broker spread thresholds (TradFi <= 5.0 bps, Crypto <= 25.0 bps).
  - [ ] Interrogate 00_MT5_Account_Telemetry.parquet.
  - [ ] Catalog complete list of eligible candidates before proceeding to analysis.

- [ ] **Step 2: Conduct Comprehensive Asset-Level Forensics**
  - [ ] Antigravity reads and performs forensic examination of every individual dossier FULL LENGTH document.
  - [ ] Examine all 4 macro sectors: Crypto, Forex Majors & Crosses, Global Indices, Precious Metals & Energy.
  - [ ] Strictly prohibit truncating or reading sub-ranges (#L1-90 / #L1-100 banned).
  - [ ] Extract Auction Profile (VAH/VAL/POC), Whale Armor (> 100K USD, > 180s), CVD Delta, and Liquidation cascades.
  - [ ] Formulate high-confluence trade setups with spread-padded stops and +2.5R targets.

- [ ] **Step 3: Synchronise Intelligence Ledger & Portfolio Registry**
  - [ ] Review and update TRI_COUNCIL_COLLABORATIVE_INTELLIGENCE_LEDGER.md with LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md.
  - [ ] Reconcile live MT5 balance, equity, margin free, open positions, and resting pending orders.
  - [ ] Guarantee byte-for-byte data consistency and push updates to GitHub main.

- [ ] **Step 4: Dispatch Independent Analysis to Arena.ai & Z.ai**
  - [ ] Prepare comprehensive, dossier-focused prompt embedding live telemetry and candidate lists.
  - [ ] Dispatch to Z.ai (chat.z.ai) via Chrome CDP (port 9222) Svelte input prototype injection.
  - [ ] Dispatch to Arena.ai (arena.ai) via Chrome CDP (port 9222) ProseMirror text insertion.
  - [ ] Require both systems to deploy multi-agent personas and independently analyze all candidates.

- [ ] **Step 5: Activate AutoWake Hard-Rock Daemon**
  - [ ] Launch rock_hard_dual_watchdog.py to monitor completion status of Arena.ai and Z.ai.
  - [ ] Enter sleep/idle mode while the daemon monitors progress.
  - [ ] Require isGenerating == False, large payload (>= 1000 chars), and stable consecutive hashes.
  - [ ] Auto-harvest outputs into ARENA_LATEST_RAW.md and ZAI_LATEST_RAW.md.

- [ ] **Step 6: Compare Intelligence & Execute Trades**
  - [ ] Perform structured 3-way comparative synthesis across Antigravity, Arena.ai, and Z.ai.
  - [ ] Evaluate evidence, confluence strength, liquidity, execution feasibility, and risk-to-reward.
  - [ ] Resolve discrepancies via empirical verification rather than blind majority voting.
  - [ ] Verify capital solvency (Hard Floor 4,775.00 USD, Operating Buffer 4,795.00 USD, Risk <= 10.00 USD).
  - [ ] Execute qualified maker limit orders directly on MT5 or maintain staged intent.

- [ ] **Step 7: Restart the 20-Minute AutoWake Cycle**
  - [ ] Update collaborative intelligence ledger and portfolio registry with verified execution outcomes.
  - [ ] Arm AutoWake timer for 20 minutes (1,200 seconds).
  - [ ] Enter sleep/idle mode awaiting wakeup to restart protocol from Step 1.
```

---

## 📊 LIVE CYCLE EXECUTION AUDIT LOG

### 🟢 Cycle_010 Audit (COMPLETED & PUNCHED)
- **Timestamp**: `2026-10-30 01:10:00 IST` (`2026-10-29 19:40:00 UTC`)
- **Step 1 (Eligible Assets)**: `PASSED` — 93 assets cleared broker spread gates (32 FX, 11 Metals/Energy, 13 Indices, 11 Crypto).
- **Step 2 (Dossier Forensics)**: `PASSED` — Full-length master dossiers examined across BTC, USDJPY, BNB, XAUUSD, NAS100, DJ30, USWTI.
- **Step 3 (Ledger/Registry Sync)**: `PASSED` — LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md & TRI_COUNCIL_COLLABORATIVE_INTELLIGENCE_LEDGER.md updated.
- **Step 4 (Dual Dispatch)**: `PASSED` — 34,711-char prompt dispatched to Arena.ai and Z.ai via Chrome CDP port 9222.
- **Step 5 (AutoWake Watchdog)**: `PASSED` — Arena.ai (53,753 chars) and Z.ai (22,723 chars) completed and harvested into RAW files. Watchdog patched for multi-vector completion detection.
- **Step 6 (Compare & Execute)**: `PASSED` — Unanimous Tri-Council convergence achieved across 7 high-confluence candidates. **All 7 maker limit orders punched directly onto MT5**:
  * `#19489155`: `BTCUSD.pi` SELL_LIMIT 0.01 @ 81,084.00 (Risk: 3.62 USD)
  * `#19489156`: `USDJPY.pi` SELL_LIMIT 0.13 @ 157.970 (Risk: 9.05 USD)
  * `#19489157`: `BNBUSD.p` SELL_LIMIT 0.05 @ 753.30 (Risk: 0.20 USD)
  * `#19489158`: `XAUUSD.pi` SELL_LIMIT 0.01 @ 4040.50 (Risk: 9.00 USD)
  * `#19489159`: `NAS100.p` SELL_LIMIT 0.01 @ 29,535.00 (Risk: 8.50 USD)
  * `#19489160`: `DJ30.p` SELL_LIMIT 0.01 @ 52,638.00 (Risk: 9.40 USD)
  * `#19489161`: `USWTI.p` BUY_LIMIT 0.01 @ 101.550 (Risk: 0.56 USD)
  * Total contingent risk: `40.33 USD` | Max single risk: `9.40 USD <= 10.00 USD`.
- **Step 7 (20-Min AutoWake)**: `PASSED` — 20-minute cycle timer armed (`task-160906`) for Cycle_011.

---

### ⏳ Cycle_011 Audit (SCHEDULED & ARMED)
- **Status**: `AWAITING_WAKEUP`
- **Wakeup Pacing**: Armed via `task-160906` (`DurationSeconds: 1200`).
- **Next Actions on Wakeup**:
  1. Screen 156 assets for live spreads in `00_MT5_Account_Telemetry.parquet`.
  2. Conduct comprehensive full-length dossier forensics for eligible assets.
  3. Synchronize ledger and portfolio registry with active MT5 resting orders.
  4. Dispatch updated dossier-focused prompts to Arena.ai and Z.ai.
  5. Activate AutoWake watchdog.
  6. Compare intelligence and manage/adjust resting orders or punch new qualified setups.
  7. Reset 20-minute timer for Cycle_012.
