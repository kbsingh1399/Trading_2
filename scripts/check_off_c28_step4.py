with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx28 = text.find('### ⏳ Cycle_028 Scorecard')
idx29 = text.find('### ⏳ Cycle_029 Scorecard')
if idx28 != -1 and idx29 != -1:
    part = text[idx28:idx29]
    part = part.replace('- [ ] **Step 4: Dispatch Independent Analysis', '- [x] **Step 4: Dispatch Independent Analysis')
    part = part.replace('- [ ] Explicitly stamp and embed the active Cycle ID', '- [x] Explicitly stamp and embed the active Cycle ID')
    part = part.replace('- [ ] Dispatch prompt embedding dossier evidence', '- [x] Dispatch prompt embedding dossier evidence')
    text = text[:idx28] + part + text[idx29:]

with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'w', encoding='utf-8') as f:
    f.write(text)

print('Checked off Step 4 for Cycle_028.')
