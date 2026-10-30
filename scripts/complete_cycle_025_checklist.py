with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace header for Cycle_025
text = text.replace("### ⏳ Cycle_025 Scorecard: IN PROGRESS", "### 🟢 Cycle_025 Scorecard: COMPLETED & FULLY VERIFIED")

# Check off Step 5
text = text.replace("- [ ] **Step 5: Activate AutoWake Hard-Rock Daemon**", "- [x] **Step 5: Activate AutoWake Hard-Rock Daemon**")
text = text.replace("- [ ] Launch `rock_hard_dual_watchdog.py --cycle Cycle_025 --timeout 1200`", "- [x] Launch `rock_hard_dual_watchdog.py --cycle Cycle_025 --timeout 1200`")
text = text.replace("- [ ] Await watchdog completion and harvest outputs", "- [x] Await watchdog completion and harvest outputs")

# Check off Step 6
text = text.replace("- [ ] **Step 6: Compare Intelligence, Actively Manage Existing Orders & Execute New Trades (USE ONLY DOSSIER FILES)**", "- [x] **Step 6: Compare Intelligence, Actively Manage Existing Orders & Execute New Trades (USE ONLY DOSSIER FILES)**")
text = text.replace("- [ ] Conduct 3-way Tri-Council comparative analysis across Antigravity", "- [x] Conduct 3-way Tri-Council comparative analysis across Antigravity")
text = text.replace("- [ ] Interrogate live orders on dossiers: purge invalidated tickets", "- [x] Interrogate live orders on dossiers: purge invalidated tickets")
text = text.replace("- [ ] Punch validated consensus limit orders on MT5", "- [x] Punch validated consensus limit orders on MT5")

# Check off Step 7
text = text.replace("- [ ] **Step 7: Restart the 20-Minute AutoWake Cycle**", "- [x] **Step 7: Restart the 20-Minute AutoWake Cycle**")
text = text.replace("- [ ] Re-arm dynamic 20-minute cycle timer via `schedule` tool with strict 7-step canonical scorecard prompt.", "- [x] Re-arm dynamic 20-minute cycle timer via `schedule` tool with strict 7-step canonical scorecard prompt.")
text = text.replace("- [ ] Advance to `Cycle_026`.", "- [x] Advance to `Cycle_026`.")

with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Marked Cycle_025 as COMPLETED & FULLY VERIFIED in ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md")
