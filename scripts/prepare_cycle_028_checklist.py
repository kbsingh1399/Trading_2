with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'r', encoding='utf-8') as f:
    text = f.read()

c28_target = """### ⏳ Cycle_028 Scorecard: PRE-INITIALIZED & ARMED
**Target Interval**: `20 Minutes` | **Pacing Engine**: Dynamic AutoWake Timer"""

c28_new = """### ⏳ Cycle_028 Scorecard: IN PROGRESS
**Timestamp**: 2026-10-30 13:24:00 IST (2026-10-30 07:54:00 UTC)
**Target Interval**: `20 Minutes` | **Pacing Engine**: Dynamic AutoWake Timer"""

if c28_target in text:
    text = text.replace(c28_target, c28_new, 1)

idx28 = text.find("### ⏳ Cycle_028 Scorecard: IN PROGRESS")
idx29 = text.find("### ⏳ Cycle_029 Scorecard")
if idx28 != -1 and idx29 != -1:
    part = text[idx28:idx29]
    part = part.replace("- [x] **Step 4: Dispatch Independent Analysis", "- [ ] **Step 4: Dispatch Independent Analysis")
    part = part.replace("- [x] Explicitly stamp and embed the active Cycle ID", "- [ ] Explicitly stamp and embed the active Cycle ID")
    part = part.replace("- [x] Dispatch prompt embedding dossier evidence", "- [ ] Dispatch prompt embedding dossier evidence")
    part = part.replace("- [x] **Step 5: Activate AutoWake Hard-Rock Daemon**", "- [ ] **Step 5: Activate AutoWake Hard-Rock Daemon**")
    part = part.replace("- [x] Await watchdog completion and harvest outputs", "- [ ] Await watchdog completion and harvest outputs")
    part = part.replace("- [x] **Step 6: Compare Intelligence", "- [ ] **Step 6: Compare Intelligence")
    part = part.replace("- [x] Conduct 3-way Tri-Council comparative analysis", "- [ ] Conduct 3-way Tri-Council comparative analysis")
    part = part.replace("- [x] Interrogate live orders on dossiers", "- [ ] Interrogate live orders on dossiers")
    part = part.replace("- [x] Punch validated consensus limit orders", "- [ ] Punch validated consensus limit orders")
    part = part.replace("- [x] **Step 7: Restart the 20-Minute AutoWake Cycle**", "- [ ] **Step 7: Restart the 20-Minute AutoWake Cycle**")
    part = part.replace("- [x] Re-arm dynamic 20-minute cycle timer", "- [ ] Re-arm dynamic 20-minute cycle timer")
    text = text[:idx28] + part + text[idx29:]

with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Cycle_028 initialized to IN PROGRESS cleanly.")
