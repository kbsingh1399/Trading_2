with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'r', encoding='utf-8') as f:
    text = f.read()

target = '- [ ] Launch `rock_hard_dual_watchdog.py --cycle Cycle_027 --timeout 1200`'
replacement = '- [x] Launch `rock_hard_dual_watchdog.py --cycle Cycle_027 --timeout 1200`'

if target in text:
    text = text.replace(target, replacement, 1)
    with open('Data/Manditory/ON_WAKEUP_CYCLE_RUNNING_CHECKLIST.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Checked off Step 5 launch in Cycle_027 cleanly!')
else:
    print('Target string not found')
