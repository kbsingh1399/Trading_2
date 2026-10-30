with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("- [ ] **Step 4: Dispatch Independent Analysis to Arena.ai & Z.ai", "- [x] **Step 4: Dispatch Independent Analysis to Arena.ai & Z.ai")
text = text.replace("- [ ] Explicitly stamp and embed the active Cycle ID", "- [x] Explicitly stamp and embed the active Cycle ID")
text = text.replace("- [ ] Dispatch prompt embedding dossier evidence to Arena.ai", "- [x] Dispatch prompt embedding dossier evidence to Arena.ai")

with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Checked off Step 4 in ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md")
