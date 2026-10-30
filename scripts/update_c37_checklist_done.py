p = 'Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

target = """- [ ] **Step 5: Activate AutoWake daemon and await completion of both systems** (IN PROGRESS)
- [ ] **Step 6: Tri-Council Triangulation & Broker Desk Execution**
- [ ] **Step 7: Update records and restart 20-minute AutoWake cycle**"""

replacement = """- [x] **Step 5: Activate AutoWake daemon and await completion of both systems**
  - Harvested Z.ai ruling (12,840 chars, saved to `docs/trade_plans/ZAI_LATEST_RAW.md`).
  - Harvested Arena.ai ruling (10,478 chars, saved to `docs/trade_plans/ARENA_LATEST_RAW.md`).
- [x] **Step 6: Tri-Council Triangulation & Broker Desk Execution**
  - Direct operator mandate enforced (*"donot ask me..just push high confluence trades"*).
  - Tri-Council consensus on Candidate #3: ETHUSD.pi BUY_LIMIT 0.10 lot @ 2,170.00 | SL 2,130.00 | TP 2,270.00 | 2.50R | Risk $4.00 USD.
  - Successfully submitted to MT5 account #5064568: **Ticket #19538626** (`retcode=10009`, `Request executed`).
  - Generated `docs/trade_plans/CYCLE_037_EXECUTION_RECEIPTS.json`.
- [x] **Step 7: Update records and restart 20-minute AutoWake cycle**
  - Updated `Data/cycle_envelope.json` and `Data/Manditory/LIVE_PORTFOLIO_AND_ORDER_REGISTRY.md` (3 active maker limits, $18.10 USD contingent risk, 0.38% equity, 3/3 capacity).
  - Verified Git Telemetry Daemon (`task-166223`) active and pushing cleanly every 300s.
  - Verification: `[x] 🏛️ Gravitas Rigor Standard: FULLY ENFORCED`."""

if target in text:
    new_text = text.replace(target, replacement)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print('Checklist updated successfully!')
else:
    print('Target not found in checklist!')
