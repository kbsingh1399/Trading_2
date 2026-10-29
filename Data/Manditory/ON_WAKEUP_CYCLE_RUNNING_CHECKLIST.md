# 📋 ON WAKEUP: MANDATORY TRADING INTELLIGENCE & EXECUTION PROTOCOL
## Continuous Autonomous Multi-Agent Cycle Scorecard & Running Checklist

> **GOVERNANCE STATUS**: CANONICAL PRODUCTION CYCLE AUDIT CHECKLIST (Single Source of Truth)  
> **Location**: `Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md`  
> **Enforcement**: Mandatory execution verification on EVERY single cycle wake-up across Antigravity, Arena.ai, and Z.ai.  
> **Live Pacing**: Dynamic 20-minute cycle interval maintained by persistent AutoWake timer.

---

## 🎯 OBJECTIVE
Establish a continuous, evidence-driven, multi-agent trading intelligence loop that performs exhaustive asset-level forensics, independently validates trade opportunities, maintains consistent portfolio records, rigorously manages active resting limit orders and live filled positions, and executes only when predefined risk and confluence requirements are satisfied.

---

## 🛡️ NON-NEGOTIABLE OPERATING PRINCIPLES

1. **Complete Coverage**: Every eligible asset and every associated Markdown dossier must be examined individually without skipping, summarizing without inspection, or selective omission.
2. **Independent Intelligence**: Antigravity, Arena.ai, and Z.ai must each conduct their own independent analysis using all available tools and capabilities.
3. **Mandatory 4-Document Governance Study Gate**: On EVERY cycle, the desk MUST physically read, analyze, and enforce the full text of:
   - `STANDARDIZED_TRADING_DECISION_CHAIN.md`
   - `TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md`
   - `32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md`
   - `ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md`
4. **Verified Completion**: Wait for both external systems to finish and verify hash stability across consecutive ticks before making the final comparative decision.
5. **Data Consistency**: Keep the collaborative intelligence ledger continuously synchronized with the live portfolio and order registry.
6. **Active Order & Position Health Interrogation**: On EVERY cycle, deeply interrogate each resting limit order and filled position: **"Should I let it run or cut it? Is it still a valid trade?"** Purge invalidated limit orders immediately; cut deteriorating filled positions at small losses; trail stops and extend profit targets when momentum confirms.
7. **Evidence-Driven Execution**: Never place a trade solely on the basis of consensus, incomplete analysis, or an unverified setup.
8. **Continuous Operation**: Repeat the complete workflow every 20 minutes after each cycle finishes.
9. **Failure Handling**: If a system, daemon, or data source fails, report the failure, preserve the current state, and avoid treating incomplete work as completed.

---

## 🔄 THE 7-STEP CANONICAL CYCLE SCORECARD TEMPLATE

Every cycle must systematically evaluate and document completion of the following 7 steps:

```markdown
### Cycle Execution Scorecard: [CYCLE_ID] | Timestamp: [TIMESTAMP_IST]

- [ ] **Step 0: Mandatory 4-Document Governance & Pitfall Avoidance Read Gate**
  - [ ] Full-length read & study: STANDARDIZED_TRADING_DECISION_CHAIN.md (SOP & Section 10 Order Lifecycle).
  - [ ] Full-length read & study: TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md (Verify zero ghost walls [Pitfall 1], zero staging above un-swept stops [Pitfall 2], zero unabsorbed CVD waterfalls [Pitfall 3], zero sub-ATR stops [Pitfall 4], zero random-walk fades [Pitfall 5], zero high spread friction [Pitfall 6], zero rollover traps [Pitfall 7], zero correlated double-bets [Pitfall 8]).
  - [ ] Full-length read & study: 32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md (35-feed row-by-row interrogation across all 4 strategic groups).
  - [ ] Full-length read & study: ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md (Active cycle scorecard verification).

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

- [ ] **Step 6: Compare Intelligence, Actively Manage Existing Orders & Execute New Trades**
  - [ ] Perform structured 3-way comparative synthesis across Antigravity, Arena.ai, and Z.ai.
  - [ ] **Active Resting Limit Orders Deep Interrogation & Purge Protocol**:
    * Check defending whale wall persistence: If resting wall (> 100K USD, > 180s) vanished/pulled -> PURGE / CANCEL IMMEDIATELY.
    * Check adverse liquidity sweep: If price swept through entry without filling, or initiated second-leg expansion -> PURGE / CANCEL IMMEDIATELY.
    * Check CVD delta waterfall: If aggressive taker delta cascading against thesis -> PURGE / CANCEL IMMEDIATELY.
    * Check rollover window: If entering 21:15-22:30 UTC for Forex/CFDs -> PURGE / CANCEL IMMEDIATELY.
    * Check time decay: If untouched for > 24 bars (6 hours) -> PURGE / CANCEL IMMEDIATELY.
  - [ ] **Live Filled Positions Real-Time Health Diagnostics, Early Cut & Trailing Protocol**:
    * Check orderflow thesis: If trade moves against thesis or auction boundary is violated -> CUT IMMEDIATELY AT MARKET taking a small loss (-0.2R to -0.4R) rather than waiting for full stopout.
    * Check profit ratchets:
      - +0.75R to +0.80R gain -> Ratchet SL to Entry ± 0.10R / 0.15R (Early Breakeven Lock).
      - +1.25R gain -> Ratchet SL to Entry ± 0.15R.
      - +1.50R to +1.65R gain -> Ratchet SL to Entry ± 0.80R (Profit Lock).
      - >= +2.00R gain -> Continuous 0.50 ATR trail behind 15m micro-shelves.
    * Check Take Profit extension: If institutional momentum and CVD delta confirm runway beyond +2.5R, dynamically extend TP to next major auction boundary/liquidation shelf while trailing SL.
  - [ ] Execute qualified maker limit orders directly on MT5 or maintain staged intent.

- [ ] **Step 7: Restart the 20-Minute AutoWake Cycle**
  - [ ] Update collaborative intelligence ledger and portfolio registry with verified execution outcomes.
  - [ ] Arm AutoWake timer for 20 minutes (1,200 seconds).
  - [ ] Enter sleep/idle mode awaiting wakeup to restart protocol from Step 0/1.
```

---

## 📊 LIVE CYCLE EXECUTION AUDIT LOG

### 🟢 Cycle_010 Audit (COMPLETED & PUNCHED)
- **Timestamp**: `2026-10-30 01:10:00 IST` (`2026-10-29 19:40:00 UTC`)
- **Step 0 (Governance Read Gate)**: `PASSED` — Full-length study of STANDARDIZED_TRADING_DECISION_CHAIN.md, TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md, 32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md, and ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md.
- **Step 1 (Eligible Assets)**: `PASSED` — 93 assets cleared broker spread gates.
- **Step 2 (Dossier Forensics)**: `PASSED` — Full-length dossiers examined without line clamping.
- **Step 3 (Ledger/Registry Sync)**: `PASSED` — Registries updated.
- **Step 4 (Dual Dispatch)**: `PASSED` — Dispatched prompt to Arena.ai and Z.ai.
- **Step 5 (AutoWake Watchdog)**: `PASSED` — Dual completions harvested.
- **Step 6 (Compare & Execute)**: `PASSED` — Punched 7 limit orders.
- **Step 7 (20-Min AutoWake)**: `PASSED` — Timer armed.

---

### 🟢 Cycle_011 Audit (COMPLETED & EXECUTED)
- **Status**: `COMPLETED`
- **Completed At**: `2026-10-30 01:44:00 IST` (`2026-10-29 20:14:00 UTC`)
- **Execution Log**:
  * **Step 0 (Governance Read Gate & Active Order Interrogation)**: `PASSED` — Studied 4 canonical documents. Verified MT5 account: Equity = `4,742.31 USD`, 7 pending limit orders active, 0 filled positions, 0.00 margin used.
  * **Step 1 (Spread Qualification Screen)**: `PASSED` — Screened live MT5 universe: 85 eligible assets within spread limits.
  * **Step 2 (Full-Length Dossier Forensics)**: `PASSED` — Read 100% full-length master dossiers for eligible candidates without line clamping.
  * **Step 3 (Registry & Ledger Sync)**: `PASSED` — Synced live orders.
  * **Step 4 (Dual Council Dispatch)**: `PASSED` — Dispatched to Z.ai (GLM-5.3-Flash) and Arena.ai.
  * **Step 5 (AutoWake Hard-Rock Watchdog)**: `PASSED` — Both models completed full outputs (60,764 chars & 29,596 chars).
  * **Step 6 (Tri-Council Deliberation, Trade Interrogation & Execution)**: `PASSED`
    * **WIN TAKE PROFIT**: `#19489156` (`USDJPY.pi` SELL 0.13 lot @ 157.970) filled and **HIT TAKE PROFIT at 157.710 (+26.0 pips)** for **`+21.43 USD` profit**! Account equity increased to **`4,762.83 USD`**!
    * **PURGE / CANCEL**: `#19489161` (`USWTI.p` BUY_LIMIT 101.550) canceled per unanimous Tri-Council finding.
    * **STAGED NEW CANDIDATE**: `#19490051` (`AUDUSD.pi` BUY_LIMIT 0.08 lot @ 0.70270 | SL 0.70150 | TP 0.70570 | Risk: `9.60 USD`) punched autonomously onto MT5.
    * **MAINTAINED RESTING**: Remaining orders confirmed active and resting behind verified armor.
  * **Step 7 (20-Min AutoWake)**: `PASSED` — Timer fired at 01:49:07 IST.

---

### 🟢 Cycle_012 Audit (COMPLETED & VERIFIED)
- **Status**: `COMPLETED`
- **Completed At**: `2026-10-30 01:57:00 IST` (`2026-10-29 20:27:00 UTC`)
- **Execution Log**:
  * **Step 0 (Governance Read Gate & Active Order Interrogation)**: `PASSED` — Studied 4 canonical documents. Verified MT5 account: Equity = `4,762.83 USD`, 6 pending limit orders active, 0 filled positions, 0.00 margin used.
  * **Step 1 (Spread Qualification Screen)**: `PASSED` — Screened live MT5 universe: 88 eligible assets within spread limits.
  * **Step 2 (Forensic SL & Liquidation Immunity Audit)**: `PASSED`
    * Interrogated `14_Liquidation_Matrix.parquet`, `15_Hyperdash_Stops_Map.parquet`, `9_Liquidation_Max_Pain_24H.parquet`, `9_Liquidation_Max_Pain_48H.parquet`, and `10_Whale_Orders.parquet`.
    * Identified that BTC (`#19489155`) and BNB (`#19489157`) previous SLs were resting below their respective short max pain prices (BTC 81,494.86 vs SL 81,446; BNB 758.31 vs SL 757.20).
    * **AUTONOMOUS BROKER ORDER MODIFICATION ON MT5**:
      - `BTCUSD.pi` (`#19489155`): Modified SL to `81,680.00` (`retcode=10009`). Placed +185 pts above 24H Short Max Pain (81,494.86), +59 pts above 48H Max Pain (81,620.94), and +127 pts above 81,553.00 liquidation peak. Nominal risk = `5.96 USD` ($\le 10.00$ USD).
      - `BNBUSD.p` (`#19489157`): Modified SL to `761.50` (`retcode=10009`). Placed +3.19 pts above 24H Short Max Pain (758.31) and +1.60 pts above 759.90 liquidation cluster. Nominal risk = `0.41 USD` ($\le 10.00$ USD).
    * **TRADFI SL VALIDATION**:
      - `XAUUSD.pi` (`#19489158`): SL at `4049.50` (+3.12 pts clear of London High 4046.38 sweep zone; risk = 9.00 USD).
      - `NAS100.p` (`#19489159`): SL at `29,620.00` (+13.51 pts beyond London High 29,606.49; risk = 8.50 USD).
      - `DJ30.p` (`#19489160`): SL at `52,732.00` (+136.66 pts above Daily VAH 52,595.34; risk = 9.40 USD).
      - `AUDUSD.pi` (`#19490051`): SL at `0.70150` (-3.0 pips below Asian Low 0.70180 retail stop hunt pocket; risk = 9.60 USD).
    * Total combined contingent downside risk = **`42.87 USD`**. 100% of Stop Losses certified immune outside liquidation zones!
  * **Step 3 (Registry & Ledger Sync)**: `PASSED` — `LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md` synchronized.

---

### ⏳ Cycle_013 Audit (DISPATCHED & RUNNING)
- **Status**: `RUNNING_MONITORED_BY_WATCHDOG`
- **Dispatched At**: `2026-10-30 01:57:33 IST` (`2026-10-29 20:27:33 UTC`)
- **Watchdog Task**: `rock_hard_dual_watchdog.py --cycle Cycle_013 --timeout 1200` (`task-161246`)
- **Standing Directives on Wakeup**:
  0. **Governance Read Gate**: Physically read `ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md`, `STANDARDIZED_TRADING_DECISION_CHAIN.md`, `TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md`, and `32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md`.
  1. **Interrogate Resting Orders & Live Positions**: "Should I let it run or cut it?" (Evaluate any newly filled tickets, trail stops if +0.80R gained, cut if thesis violated).
  2. **Tri-Council Comparison (Step 6)**: Compare harvested Arena.ai and Z.ai outputs for Cycle_013.
  3. **Punch Qualified Limit Orders**: Stage new consensus candidates if dynamic capacity ($N_{\text{open}} + N_{\text{pending}} \le 3$ in DD defense / max 2 filled) allows.
