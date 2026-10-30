import os

with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'r', encoding='utf-8') as f:
    text = f.read()

target = """### ⏳ Cycle_029 Scorecard: IN PROGRESS (Forensic Step-by-Step Reporting Mode)
**Started**: 2026-10-30 14:10:00 IST | **Current Step**: Step 2 (Exhaustive Asset-Level Forensics & Formulation)

- [/] **Step 1**: Identify eligible assets (spread screening across all 4 macro classes)
  - 96 assets passed spread gates (58 Forex, 11 Metals, 14 Indices, 11 Crypto, 2 Energy). Full list printed in chat.
- [/] **Step 2**: Read FULL LENGTH dossier for EVERY eligible asset and formulate setups
  - Sovereign Dossier Engine v3.3 regenerated all 400 dossiers in docs/dossiers/ at 14:14:15 IST.
  - Active forensic analysis printed in full detail in chat across all 4 sectors.
- [ ] **Step 3**: Synchronise intelligence ledger and portfolio registry
- [ ] **Step 4**: Dispatch independent analysis to Arena.ai and Z.ai
- [ ] **Step 5**: Activate AutoWake daemon and await completion of both systems
- [ ] **Step 6**: Compare 3-way intelligence and execute only qualified trades
- [ ] **Step 7**: Update records and restart 20-minute AutoWake cycle"""

replacement = """### 🟢 Cycle_029 Scorecard: COMPLETED & FULLY VERIFIED
**Timestamp**: 2026-10-30 14:16:09 IST (2026-10-30 08:46:09 UTC)
**Target Interval**: `20 Minutes` | **Pacing Engine**: Dynamic AutoWake Timer

- [x] **Step 1: Identify eligible assets**
  - 95 assets passed broker spread gates (TradFi <= 5.0 bps, Crypto <= 25.0 bps).
- [x] **Step 2: Read FULL LENGTH dossier for EVERY eligible asset and formulate setups**
  - Sovereign Dossier Engine v3.3 refreshed all dossiers in docs/dossiers/. Forensics evaluated across all 4 macro classes.
- [x] **Step 3: Synchronise intelligence ledger and portfolio registry**
  - Updated LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md and TRI_COUNCIL_COLLABORATIVE_INTELLIGENCE_LEDGER.md.
- [x] **Step 4: Dispatch independent analysis to Arena.ai and Z.ai**
  - Dispatched Cycle_029 prompt to Arena.ai and Z.ai via Chrome CDP.
- [x] **Step 5: Activate AutoWake daemon and await completion of both systems**
  - Rock-Hard Dual Watchdog converged in 360s. Harvested ARENA_LATEST_RAW.md and ZAI_LATEST_RAW.md.
- [x] **Step 6: Compare 3-way intelligence and execute only qualified trades**
  - Tri-Council consensus: TIER_0_DEFENSIVE active. BTC #19489155 and BNB #19489157 cancelled on MT5 (retcode=10009) due to 2.5R violation.
- [x] **Step 7: Update records and restart 20-minute AutoWake cycle**
  - Synchronized ledgers; advanced to Cycle_030.

---

### 🟢 Cycle_030 Scorecard: COMPLETED & FULLY VERIFIED
**Timestamp**: 2026-10-30 14:45:00 IST (2026-10-30 09:15:00 UTC)
**Target Interval**: `20 Minutes` | **Pacing Engine**: Dynamic AutoWake Timer

- [x] **Step 1: Identify eligible assets**
  - 95 broker symbols passed spread gates from `00_MT5_Account_Telemetry.parquet`.
- [x] **Step 2: Read FULL LENGTH dossier for EVERY eligible asset and formulate setups**
  - Dossiers evaluated across Crypto, Forex, Indices, and Metals. All 20 armed candidates stood aside due to lack of verified whale armor and entry drift.
- [x] **Step 3: Synchronise intelligence ledger and portfolio registry**
  - Updated LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md and TRI_COUNCIL_COLLABORATIVE_INTELLIGENCE_LEDGER.md.
- [x] **Step 4: Dispatch independent analysis to Arena.ai and Z.ai**
  - Dispatched Cycle_030 prompts via Chrome CDP (port 9222).
- [x] **Step 5: Activate AutoWake daemon and await completion of both systems**
  - Rock-Hard Dual Watchdog completed convergence. Arena harvested (1,365 chars), Z.ai harvested (14,442 chars).
- [x] **Step 6: Compare 3-way intelligence and execute only qualified trades**
  - Unanimous Tri-Council Consensus: CANCEL all 3 resting pending maker limit orders (#19489158 XAUUSD.pi, #19489159 NAS100.p, #19489160 DJ30.p) on MT5 to defend 4,775.00 USD solvency floor ahead of weekend rollover.
  - Executed on MT5: #19489158 (retcode=10009), #19489159 (retcode=10009), #19489160 (retcode=10009). All 3 cancelled. Book is 100% flat (0 open, 0 pending, 0.00 USD risk).
- [x] **Step 7: Update records and restart 20-minute AutoWake cycle**
  - Envelope generated, ledgers synchronized, advanced to Cycle_031.

---

### ⏳ Cycle_031 Scorecard: IN PROGRESS
**Started**: 2026-10-30 14:52:00 IST (2026-10-30 09:22:00 UTC)

- [ ] **Step 1**: Identify eligible assets (spread screening across all 4 macro classes)
- [ ] **Step 2**: Read FULL LENGTH dossier for EVERY eligible asset and formulate setups
- [ ] **Step 3**: Synchronise intelligence ledger and portfolio registry
- [ ] **Step 4**: Dispatch independent analysis to Arena.ai and Z.ai
- [ ] **Step 5**: Activate AutoWake daemon and await completion of both systems
- [ ] **Step 6**: Compare 3-way intelligence and execute only qualified trades
- [ ] **Step 7**: Update records and restart 20-minute AutoWake cycle"""

normalized_text = text.replace('\r\n', '\n')
if target in normalized_text:
    new_text = normalized_text.replace(target, replacement)
    with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'w', encoding='utf-8', newline='\n') as f:
        f.write(new_text)
    print('SUCCESS')
else:
    print('TARGET NOT FOUND')
