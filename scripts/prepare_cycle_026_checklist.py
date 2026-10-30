import re

with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace header for Cycle_026
c26_target = """### ⏳ Cycle_026 Scorecard: PRE-INITIALIZED & ARMED
**Target Interval**: `20 Minutes` | **Pacing Engine**: Dynamic AutoWake Timer"""

c26_new = """### ⏳ Cycle_026 Scorecard: IN PROGRESS
**Timestamp**: 2026-10-30 10:43:00 IST (2026-10-30 05:13:00 UTC)
**Target Interval**: `20 Minutes` | **Pacing Engine**: Dynamic AutoWake Timer"""

text = text.replace(c26_target, c26_new)

# Reset Step 4, 5, 6, 7 to unchecked
idx26 = text.find("### ⏳ Cycle_026 Scorecard: IN PROGRESS")
idx27 = text.find("### ⏳ Cycle_027 Scorecard")
if idx26 != -1 and idx27 != -1:
    part = text[idx26:idx27]
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
    text = text[:idx26] + part + text[idx27:]

with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Cycle_026 initialized to IN PROGRESS cleanly.")
