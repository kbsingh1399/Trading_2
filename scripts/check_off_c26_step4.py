with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx26 = text.find("### ⏳ Cycle_026 Scorecard: IN PROGRESS")
idx27 = text.find("### ⏳ Cycle_027 Scorecard")
if idx26 != -1 and idx27 != -1:
    part = text[idx26:idx27]
    part = part.replace("- [ ] **Step 4: Dispatch Independent Analysis", "- [x] **Step 4: Dispatch Independent Analysis")
    part = part.replace("- [ ] Explicitly stamp and embed the active Cycle ID", "- [x] Explicitly stamp and embed the active Cycle ID")
    part = part.replace("- [ ] Dispatch prompt embedding dossier evidence", "- [x] Dispatch prompt embedding dossier evidence")
    text = text[:idx26] + part + text[idx27:]

with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Checked off Step 4 for Cycle_026.")
