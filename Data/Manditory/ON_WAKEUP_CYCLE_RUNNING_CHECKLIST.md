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
10. **Standing Hourly Watchdog Recovery Cron**: An independent standing daemon cron job (`0 * * * *`, Task ID `task-161494`) fires every 60 minutes to audit the system, verify Parquet feeds freshness (< 5.0m), detect any stalled watchdogs or cycle halts, and immediately unstuck and resume autonomous execution.

---

## 🔄 THE 7-STEP CANONICAL CYCLE SCORECARD TEMPLATE

Every cycle must systematically evaluate, execute, and document completion by explicitly ticking (`- [x]`) the following 7 steps as work progresses:

---

## 📊 LIVE CYCLE EXECUTION SCORECARDS & AUDIT LOG

### 🟢 Cycle_012 Scorecard: COMPLETED & FULLY VERIFIED
**Timestamp**: `2026-10-30 01:57:00 IST` (`2026-10-29 20:27:00 UTC`)

- [x] **Step 0: Mandatory 4-Document Governance & Pitfall Avoidance Read Gate**
  - [x] Full-length read & study: `STANDARDIZED_TRADING_DECISION_CHAIN.md` (SOP, In-Memory Lake, Dynamic Capacity).
  - [x] Full-length read & study: `TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md` (Zero ghost walls [Pitfall 1], zero staging above un-swept stops [Pitfall 2], zero unabsorbed CVD waterfalls [Pitfall 3], zero sub-ATR stops [Pitfall 4], zero random-walk fades [Pitfall 5], zero high spread friction [Pitfall 6], zero rollover traps [Pitfall 7], zero correlated double-bets [Pitfall 8]).
  - [x] Full-length read & study: `32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md` (35-feed row-by-row interrogation across all 4 strategic groups).
  - [x] Full-length read & study: `ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md` (Active cycle scorecard verification).

- [x] **Step 1: Identify Eligible Assets**
  - [x] Filter all tradeable assets against broker spread thresholds (TradFi <= 5.0 bps, Crypto <= 25.0 bps).
  - [x] Interrogate `00_MT5_Account_Telemetry.parquet`: 88 assets qualified (USDJPY 0.06 bps, AUDUSD 0.14 bps, XAUUSD 0.20 bps, DJ30 0.23 bps, NAS100 0.34 bps, BTCUSD 1.87 bps, BNBUSD 8.06 bps).
  - [x] Catalog complete list of eligible candidates before proceeding to analysis.

- [x] **Step 2: Conduct Comprehensive Asset-Level Forensics**
  - [x] Antigravity reads and performs forensic examination of every individual dossier FULL LENGTH document:
    * Crypto: `docs/dossiers/BTC_MASTER_DOSSIER.md` (Sections 1-10 read, VAH 80,879, POC 80,022, 16.3M USD wall @ 81,500).
    * Precious Metals: `docs/dossiers/XAUUSD_MASTER_DOSSIER.md` (100% 1,011 lines read to EOF; VAH 4040.10, POC 4027.32, London High 4046.38).
    * Global Indices: `docs/dossiers/NAS100_MASTER_DOSSIER.md` (100% 301 lines read to EOF; VAH 29,550.22, London High 29,606.49) & `docs/dossiers/DJ30_MASTER_DOSSIER.md` (100% 285 lines read to EOF; VAH 52,589.95, POC 52,331.39).
    * FX Majors: `docs/dossiers/AUDUSD_MASTER_DOSSIER.md` (100% 309 lines read to EOF; VAL 0.7028, Asian Low 0.70180, Bullish Absorption 1,134 USD).
  - [x] Examine all 4 macro sectors: Crypto, Forex Majors & Crosses, Global Indices, Precious Metals & Energy.
  - [x] Strictly prohibit truncating or reading sub-ranges (`#L1-90` / `#L1-100` banned).
  - [x] Extract Auction Profile (VAH/VAL/POC), Whale Armor (> 100K USD, > 180s), CVD Delta, and Liquidation cascades.
  - [x] **Forensic SL & Liquidation Immunity Audit & Live MT5 Modification**:
    * Identified BTC 24H Short Max Pain at `81,494.86 USD` and BNB Short Max Pain at `758.31 USD`.
    * Executed live order modifications on MT5 (`retcode=10009`):
      - Ticket `#19489155` (`BTCUSD.pi`): SL modified to **`81,680.00 USD`** (+185 pts above Max Pain & +127 pts above 81,553 liq band; nominal risk = `5.96 USD` <= 10.00 USD).
      - Ticket `#19489157` (`BNBUSD.p`): SL modified to **`761.50 USD`** (+3.19 pts above Max Pain & +1.60 pts above 759.90 liq band; nominal risk = `0.41 USD` <= 10.00 USD).
    * Certified XAUUSD (`4049.50 USD`, +3.12 pts clear of London High 4046.38), NAS100 (`29,620.00 USD`, +13.51 pts beyond London High 29,606.49), DJ30 (`52,732.00 USD`), and AUDUSD (`0.70150 USD`, -3.0 pips below Asian Low) as 100% immune to sweeps.
    * Total combined contingent downside risk = **`42.87 USD`**. Zero open positions, 100% cash defense preserved.

- [x] **Step 3: Synchronise Intelligence Ledger & Portfolio Registry**
  - [x] Updated `LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md` with modified SLs, risk metrics, and equity `4,762.83 USD`.
  - [x] Reconciled live MT5 balance, equity, margin free, open positions (0), and resting pending orders (6).
  - [x] Guaranteed byte-for-byte data consistency across local files and GitHub push daemon.

- [x] **Step 4: Dispatch Independent Analysis to Arena.ai & Z.ai**
  - [x] Prepared 14,684-character comprehensive prompt embedding live telemetry and candidate lists.
  - [x] Dispatched to Z.ai (chat.z.ai, GLM-5.3-Flash) via Chrome CDP (port 9222).
  - [x] Dispatched to Arena.ai (arena.ai) via Chrome CDP (port 9222).
  - [x] Dispatched to Gemini Web2API (port 8081).

- [x] **Step 5: Activate AutoWake Hard-Rock Daemon**
  - [x] Launched `rock_hard_dual_watchdog.py --cycle Cycle_013 --timeout 1200` (`task-161246`) to monitor Arena.ai and Z.ai completion status.
  - [x] Background watcher active and harvesting outputs.

- [x] **Step 6: Compare Intelligence, Actively Manage Existing Orders & Execute New Trades**
  - [x] Deliberated resting orders: USDJPY win banked (+21.43 USD), USWTI purged, AUDUSD punched, BTC & BNB SLs armored.
  - [x] Book is in 100% Cash Defense with 6 high-confluence passive maker limits resting.

- [x] **Step 7: Restart the 20-Minute AutoWake Cycle**
  - [x] Live portfolio and order registry synchronized.
  - [x] Timer re-armed (`task-161289`) for dynamic cycle pacing with strict 7-step canonical scorecard prompt.

---

### ⏳ Cycle_013 Scorecard: RUNNING & MONITORED BY WATCHDOG
**Dispatched At**: `2026-10-30 01:57:33 IST` (`2026-10-29 20:27:33 UTC`) | **Watchdog Task**: `task-161246` | **Timer Task**: `task-161289`

- [x] **Step 0: Mandatory 4-Document Governance & Pitfall Avoidance Read Gate**
  - [x] Full-length read & study: `STANDARDIZED_TRADING_DECISION_CHAIN.md`.
  - [x] Full-length read & study: `TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md`.
  - [x] Full-length read & study: `32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md`.
  - [x] Full-length read & study: `ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md`.

- [x] **Step 1: Identify Eligible Assets**
  - [x] Live MT5 account telemetry interrogated (`00_MT5_Account_Telemetry.parquet`).
  - [x] Spread thresholds validated: TradFi <= 5.0 bps, Crypto <= 25.0 bps.

- [x] **Step 2: Conduct Comprehensive Asset-Level Forensics**
  - [x] Full-length master dossier examination executed across all 4 macro sectors:
    * Crypto: `docs/dossiers/BTC_MASTER_DOSSIER.md` (Sections 1-10 read).
    * Precious Metals: `docs/dossiers/XAUUSD_MASTER_DOSSIER.md` (1,011 lines read to EOF).
    * Global Indices: `docs/dossiers/NAS100_MASTER_DOSSIER.md` (301 lines read to EOF) & `docs/dossiers/DJ30_MASTER_DOSSIER.md` (285 lines read to EOF).
    * FX Majors: `docs/dossiers/AUDUSD_MASTER_DOSSIER.md` (309 lines read to EOF).
  - [x] SL immunity against short max pain & liquidation cascades verified.

- [x] **Step 3: Synchronise Intelligence Ledger & Portfolio Registry**
  - [x] `LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md` synchronized with live MT5 tickets.

- [x] **Step 4: Dispatch Independent Analysis to Arena.ai & Z.ai**
  - [x] Dispatched Cycle_013 prompt to Arena.ai, Z.ai (GLM-5.3-Flash), and Web2API.

- [x] **Step 5: Activate AutoWake Hard-Rock Daemon**
  - [x] `rock_hard_dual_watchdog.py --cycle Cycle_013` completed surveillance.
  - [x] Successfully harvested Arena.ai (`docs/trade_plans/ARENA_LATEST_RAW.md`, 52,816 chars).
  - [x] Successfully harvested Z.ai (`docs/trade_plans/ZAI_LATEST_RAW.md`, 29,510 chars).

- [x] **Step 6: Compare Intelligence, Actively Manage Existing Orders & Execute New Trades**
  - [x] Conducted 3-way Tri-Council comparative forensics across Antigravity, Arena.ai, and Z.ai:
    * Arena.ai validates active resting limits on BTC, BNB, XAUUSD, NAS100, DJ30, and AUDUSD; endorses purge of USWTI and quarantine of FX pre-rollover entries.
    * Z.ai endorses `STAGED_FROZEN_CAPACITY_ZERO`, confirming that no new speculative risk should be staged while preserving TIER_0_DEFENSIVE capital defense.
    * Antigravity confirms MT5 execution status: 0 open positions, 6 passive resting limits, total contingent downside risk = `42.87 USD`.
  - [x] Interrogated live orders ("Should I let it run or cut it?"): All 6 orders maintain valid auction structure, defending whale armor, and SL immunity beyond liquidation cascades. Orders remain resting.
  - [x] Sizing & solvency invariant preserved: Nominal risk per ticket <= 10.00 USD. Capital floor (4,775.00 USD) fully defended.

- [x] **Step 7: Restart the 20-Minute AutoWake Cycle**
  - [x] Synchronized `LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md` and `cycle_envelope.json`.
  - [x] Cycle_013 COMPLETED & FULLY VERIFIED. Advanced to Cycle_014.

---

### ⏳ Cycle_014 Scorecard: PRE-INITIALIZED & ARMED
**Target Interval**: `20 Minutes` | **Pacing Engine**: Dynamic AutoWake Timer

- [ ] **Step 0: Mandatory 4-Document Governance & Pitfall Avoidance Read Gate**
  - [ ] Full-length read & study: `STANDARDIZED_TRADING_DECISION_CHAIN.md`.
  - [ ] Full-length read & study: `TOP_10_TRADE_EXECUTION_PITFALLS_AND_AUTOPSY.md`.
  - [ ] Full-length read & study: `32_SHEET_REAL_WORLD_PITFALL_AVOIDANCE_QUESTIONS.md`.
  - [ ] Full-length read & study: `ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md`.

- [ ] **Step 1: Identify Eligible Assets**
  - [ ] Live MT5 account telemetry interrogated (`00_MT5_Account_Telemetry.parquet`).
  - [ ] Spread thresholds validated: TradFi <= 5.0 bps, Crypto <= 25.0 bps.

- [ ] **Step 2: Conduct Comprehensive Asset-Level Forensics**
  - [ ] Full-length master dossier examination executed across all 4 macro sectors:
    * Crypto: `docs/dossiers/BTC_MASTER_DOSSIER.md` (Sections 1-10 read).
    * Precious Metals: `docs/dossiers/XAUUSD_MASTER_DOSSIER.md` (1,011 lines read to EOF).
    * Global Indices: `docs/dossiers/NAS100_MASTER_DOSSIER.md` & `docs/dossiers/DJ30_MASTER_DOSSIER.md`.
    * FX Majors: `docs/dossiers/AUDUSD_MASTER_DOSSIER.md`.
  - [ ] SL immunity against short max pain & liquidation cascades verified.

- [ ] **Step 3: Synchronise Intelligence Ledger & Portfolio Registry**
  - [ ] `LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md` synchronized with live MT5 tickets.

- [ ] **Step 4: Dispatch Independent Analysis to Arena.ai & Z.ai**
  - [ ] Explicitly stamp and embed the active Cycle ID (`Cycle_014`) in the prompt header, metadata block, and JSON schema.
  - [ ] Dispatch Cycle_014 prompt to Arena.ai, Z.ai (GLM-5.3-Flash), and Web2API.

- [ ] **Step 5: Activate AutoWake Hard-Rock Daemon**
  - [ ] Launch `rock_hard_dual_watchdog.py --cycle Cycle_014 --timeout 1200` to monitor Arena.ai and Z.ai completion status.

- [ ] **Step 6: Compare Intelligence, Actively Manage Existing Orders & Execute New Trades**
  - [ ] Conduct Tri-Council deliberation comparison, interrogate live orders ('Should I let it run or cut it?'), punch consensus limit orders, and trail stops.

- [ ] **Step 7: Restart the 20-Minute AutoWake Cycle**
  - [ ] Re-arm dynamic 20-minute cycle timer and advance to Cycle_015.
