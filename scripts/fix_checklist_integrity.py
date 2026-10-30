import re

with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix Cycle_027 header if not completed
c27_old = "### ⏳ Cycle_027 Scorecard: PRE-INITIALIZED & ARMED"
c27_done = """### 🟢 Cycle_027 Scorecard: COMPLETED & FULLY VERIFIED
**Timestamp**: 2026-10-30 11:18:00 IST (2026-10-30 05:48:00 UTC)
**Target Interval**: `20 Minutes` | **Pacing Engine**: Dynamic AutoWake Timer"""

if c27_old in text:
    text = text.replace(c27_old, c27_done, 1)

# 2. In Cycle_028, reset Step 2, 5, 6, 7 to unchecked
idx28 = text.find("### ⏳ Cycle_028 Scorecard: IN PROGRESS")
idx29 = text.find("### ⏳ Cycle_029 Scorecard")
if idx28 != -1 and idx29 != -1:
    c28_part = text[idx28:idx29]
    # Uncheck Step 2
    c28_part = c28_part.replace("- [x] **Step 2: Conduct Comprehensive Asset-Level Forensics", "- [ ] **Step 2: Conduct Comprehensive Asset-Level Forensics")
    c28_part = c28_part.replace("- [x] **Phase 2A: Comprehensive Sector-Wide", "- [ ] **Phase 2A: Comprehensive Sector-Wide")
    c28_part = c28_part.replace("- [x] **Phase 2B: Running Trade", "- [ ] **Phase 2B: Running Trade")
    c28_part = c28_part.replace("- [x] **Phase 2C: Active Order", "- [ ] **Phase 2C: Active Order")
    # Uncheck Step 5, 6, 7
    c28_part = c28_part.replace("- [x] Await watchdog completion and harvest outputs", "- [ ] Await watchdog completion and harvest outputs")
    c28_part = c28_part.replace("- [x] **Step 6: Compare Intelligence", "- [ ] **Step 6: Compare Intelligence")
    c28_part = c28_part.replace("- [x] Conduct 3-way Tri-Council comparative analysis", "- [ ] Conduct 3-way Tri-Council comparative analysis")
    c28_part = c28_part.replace("- [x] Interrogate live orders on dossiers", "- [ ] Interrogate live orders on dossiers")
    c28_part = c28_part.replace("- [x] Punch validated consensus limit orders", "- [ ] Punch validated consensus limit orders")
    c28_part = c28_part.replace("- [x] **Step 7: Restart the 20-Minute AutoWake Cycle**", "- [ ] **Step 7: Restart the 20-Minute AutoWake Cycle**")
    c28_part = c28_part.replace("- [x] Re-arm dynamic 20-minute cycle timer", "- [ ] Re-arm dynamic 20-minute cycle timer")
    c28_part = c28_part.replace("- [x] Advance to `Cycle_029`.", "- [ ] Advance to `Cycle_029`.")
    text = text[:idx28] + c28_part + text[idx29:]

# 3. For Cycle_029 through Cycle_100, uncheck ALL checkboxes completely!
# Find where Cycle_029 starts
if idx29 != -1:
    future_text = text[idx29:]
    # Replace all - [x] with - [ ] in future_text
    future_text_clean = future_text.replace("- [x] ", "- [ ] ")
    text = text[:idx29] + future_text_clean

with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md! Future cycles (029-100) are all unchecked, Cycle_028 Step 2 is unchecked.")
