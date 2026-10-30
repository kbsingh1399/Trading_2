with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace header for Cycle_027
c27_target = """### ⏳ Cycle_027 Scorecard: IN PROGRESS
**Timestamp**: 2026-10-30 11:18:00 IST (2026-10-30 05:48:00 UTC)
**Target Interval**: `20 Minutes` | **Pacing Engine**: Dynamic AutoWake Timer"""

c27_completed = """### 🟢 Cycle_027 Scorecard: COMPLETED & FULLY VERIFIED
**Timestamp**: 2026-10-30 11:18:00 IST (2026-10-30 05:48:00 UTC)
**Target Interval**: `20 Minutes` | **Pacing Engine**: Dynamic AutoWake Timer"""

if c27_target in text:
    text = text.replace(c27_target, c27_completed, 1)

idx27 = text.find("### 🟢 Cycle_027 Scorecard: COMPLETED & FULLY VERIFIED")
idx28 = text.find("### ⏳ Cycle_028 Scorecard")
if idx27 != -1 and idx28 != -1:
    part = text[idx27:idx28]
    part = part.replace("- [ ] **Step 6: Compare Intelligence", "- [x] **Step 6: Compare Intelligence")
    part = part.replace("- [ ] Conduct 3-way Tri-Council comparative analysis", "- [x] Conduct 3-way Tri-Council comparative analysis")
    part = part.replace("- [ ] Interrogate live orders on dossiers", "- [x] Interrogate live orders on dossiers")
    part = part.replace("- [ ] Punch validated consensus limit orders", "- [x] Punch validated consensus limit orders")
    part = part.replace("- [ ] **Step 7: Restart the 20-Minute AutoWake Cycle**", "- [x] **Step 7: Restart the 20-Minute AutoWake Cycle**")
    part = part.replace("- [ ] Re-arm dynamic 20-minute cycle timer", "- [x] Re-arm dynamic 20-minute cycle timer")
    part = part.replace("- [ ] Advance to `Cycle_028`.", "- [x] Advance to `Cycle_028`.")
    text = text[:idx27] + part + text[idx28:]

with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Cycle_027 checklist completed and checked off successfully!")
