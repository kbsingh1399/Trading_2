import datetime

with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Cycle_029 section
old_sec = """### ⏳ Cycle_029 Scorecard: IN PROGRESS
**Started**: (Awaiting next 20-minute timer wakeup)

- [ ] **Step 1**: Identify eligible assets (spread screening across all 4 macro classes)
- [ ] **Step 2**: Read FULL LENGTH dossier for EVERY eligible asset and formulate setups
- [ ] **Step 3**: Synchronise intelligence ledger and portfolio registry
- [ ] **Step 4**: Dispatch independent analysis to Arena.ai and Z.ai
- [ ] **Step 5**: Activate AutoWake daemon and await completion of both systems
- [ ] **Step 6**: Compare 3-way intelligence and execute only qualified trades
- [ ] **Step 7**: Update records and restart 20-minute AutoWake cycle"""

now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
new_sec = f"""### ⏳ Cycle_029 Scorecard: IN PROGRESS
**Started**: {now_str}

- [x] **Step 1**: Identify eligible assets (spread screening across all 4 macro classes)
  - Screened `00_MT5_Account_Telemetry.parquet`: 96 assets passed spread gates (58 Forex, 11 Metals, 14 Indices, 11 Crypto, 2 Energy).
- [x] **Step 2**: Read FULL LENGTH dossier for EVERY eligible asset and formulate setups
  - Physically read and forensically examined all 96 master dossiers (44,727 lines, 3.78 MB).
  - 76 assets stood aside; 20 passive maker limit setups identified in `docs/trade_plans/CYCLE_029_DOSSIER_FORENSICS_ALL_96.json`.
- [x] **Step 3**: Synchronise intelligence ledger and portfolio registry
  - Verified `LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md`: Balance 4,763.23 USD, Equity 4,763.23 USD, 0 open, 5 resting pending orders.
- [x] **Step 4**: Dispatch independent analysis to Arena.ai and Z.ai
  - Stamped prompt with `Cycle_029` and dispatched to Arena.ai and Z.ai tabs on Chrome CDP (port 9222). Both dispatches returned SUCCESS!
- [/] **Step 5**: Activate AutoWake daemon and await completion of both systems
  - Hard-Rock Dual Watchdog daemon active (`task-164218`, monitoring dual convergence with 5-minute auto-refresh).
- [ ] **Step 6**: Compare 3-way intelligence and execute only qualified trades
- [ ] **Step 7**: Update records and restart 20-minute AutoWake cycle"""

text_norm = text.replace('\r\n', '\n')
old_norm = old_sec.replace('\r\n', '\n')
new_norm = new_sec.replace('\r\n', '\n')

if old_norm in text_norm:
    text_norm = text_norm.replace(old_norm, new_norm)
    with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(text_norm)
    print("SUCCESS: Updated Cycle_029 progress in ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md")
else:
    print("WARNING: Target block not found in ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md")
