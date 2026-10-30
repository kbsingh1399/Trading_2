with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx26 = text.find("### ⏳ Cycle_026 Scorecard: IN PROGRESS")
idx27 = text.find("### ⏳ Cycle_027 Scorecard")
if idx26 != -1 and idx27 != -1:
    part = text[idx26:idx27]
    part = part.replace("### ⏳ Cycle_026 Scorecard: IN PROGRESS", "### 🟢 Cycle_026 Scorecard: COMPLETED & FULLY VERIFIED")
    part = part.replace("- [ ] **Step 5: Activate AutoWake Hard-Rock Daemon**", "- [x] **Step 5: Activate AutoWake Hard-Rock Daemon**")
    part = part.replace("- [ ] Launch `rock_hard_dual_watchdog.py --cycle Cycle_026 --timeout 1200`", "- [x] Launch `rock_hard_dual_watchdog.py --cycle Cycle_026 --timeout 1200`")
    part = part.replace("- [ ] Await watchdog completion and harvest outputs", "- [x] Await watchdog completion and harvest outputs")
    part = part.replace("- [ ] **Step 6: Compare Intelligence", "- [x] **Step 6: Compare Intelligence")
    part = part.replace("- [ ] Conduct 3-way Tri-Council comparative analysis", "- [x] Conduct 3-way Tri-Council comparative analysis")
    part = part.replace("- [ ] Interrogate live orders on dossiers", "- [x] Interrogate live orders on dossiers")
    part = part.replace("- [ ] Punch validated consensus limit orders", "- [x] Punch validated consensus limit orders")
    part = part.replace("- [ ] **Step 7: Restart the 20-Minute AutoWake Cycle**", "- [x] **Step 7: Restart the 20-Minute AutoWake Cycle**")
    part = part.replace("- [ ] Re-arm dynamic 20-minute cycle timer", "- [x] Re-arm dynamic 20-minute cycle timer")
    part = part.replace("- [ ] Advance to `Cycle_027`.", "- [x] Advance to `Cycle_027`.")
    text = text[:idx26] + part + text[idx27:]

with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Cycle_026 marked COMPLETED & FULLY VERIFIED.")
