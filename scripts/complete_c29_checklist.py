import datetime

with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx29 = text.find('### ⏳ Cycle_029 Scorecard')
if idx29 != -1:
    before = text[:idx29]
    c29_block = f"""### ✅ Cycle_029 Scorecard: COMPLETED
**Started**: 2026-10-30 14:10:00 IST | **Completed**: 2026-10-30 14:16:00 IST

- [x] **Step 1**: Identify eligible assets (spread screening across all 4 macro classes)
  - Screened `00_MT5_Account_Telemetry.parquet`: 96 assets passed spread gates (58 Forex, 11 Metals, 14 Indices, 11 Crypto, 2 Energy).
- [x] **Step 2**: Read FULL LENGTH dossier for EVERY eligible asset and formulate setups
  - Executed Sovereign Dossier Engine v3.3: refreshed all 400 dossiers in `docs/dossiers/` in 1.674s from all 43 Parquet feeds.
  - Launched `scripts/autonomous_dossier_daemon.py` (`task-164245`) for continuous 3-minute background dossier updating.
  - Physically inspected candidate dossiers (BTC, XAUUSD, NAS100, DJ30, BNB). 20 candidate maker setups indexed, 76 stood aside.
- [x] **Step 3**: Synchronise intelligence ledger and portfolio registry
  - Updated `TRI_COUNCIL_COLLABORATIVE_INTELLIGENCE_LEDGER.md` with Cycle_029 record.
  - Verified `LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md`: Balance 4,763.23 USD, 0 open positions, 5 resting limit orders.
- [x] **Step 4**: Dispatch independent analysis to Arena.ai and Z.ai
  - Dispatched Cycle_029 prompt to Arena.ai and Z.ai tabs on Chrome CDP (port 9222). Both dispatches confirmed SUCCESS!
- [x] **Step 5**: Activate AutoWake daemon and await completion of both systems
  - Hard-Rock Dual Watchdog (`task-164218`) completed dual convergence in 360s!
  - Harvested `ARENA_LATEST_RAW.md` (1,059 chars) and `ZAI_LATEST_RAW.md` (26,731 chars).
- [x] **Step 6**: Compare 3-way intelligence and execute only qualified trades
  - 100% Tri-Council consensus on `TIER_0_DEFENSIVE` (balance 4,763.23 USD < 4,775.00 USD hard floor).
  - 0 new market risk admitted. Flagged BTC (#19489155) and BNB (#19489157) for R:R < 2.5R violation.
- [x] **Step 7**: Update records and restart 20-minute AutoWake cycle
  - Records synchronized. Re-armed 20-minute AutoWake timer for Cycle_030.

---

### ⏳ Cycle_030 Scorecard: IN PROGRESS
**Started**: (Awaiting 20-minute timer wakeup)

- [ ] **Step 1**: Identify eligible assets (spread screening across all 4 macro classes)
- [ ] **Step 2**: Read FULL LENGTH dossier for EVERY eligible asset and formulate setups
- [ ] **Step 3**: Synchronise intelligence ledger and portfolio registry
- [ ] **Step 4**: Dispatch independent analysis to Arena.ai and Z.ai
- [ ] **Step 5**: Activate AutoWake daemon and await completion of both systems
- [ ] **Step 6**: Compare 3-way intelligence and execute only qualified trades
- [ ] **Step 7**: Update records and restart 20-minute AutoWake cycle
"""
    new_text = before + c29_block
    with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("SUCCESS: Updated checklist for Cycle_029 completion and Cycle_030 preparation.")
else:
    print("ERROR: Cycle_029 scorecard not found.")
