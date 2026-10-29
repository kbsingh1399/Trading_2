with open('Terminal/rock_hard_dual_watchdog.py', 'r', encoding='utf-8') as f:
    content = f.read()

old_str = """        const allChatMsgs = Array.from(document.querySelectorAll('.chat-assistant.markdown-prose'));
        const lastProse = allChatMsgs.length > 0 ? allChatMsgs[allChatMsgs.length - 1] : null;
        const chatText = lastProse ? (lastProse.innerText || '').trim() : '';"""

new_str = """        const allChatMsgs = Array.from(document.querySelectorAll('.chat-assistant.markdown-prose, div.prose, .chat-assistant'));
        let chatText = '';
        for (let i = allChatMsgs.length - 1; i >= 0; i--) {
            const t = (allChatMsgs[i].innerText || '').trim();
            if (t.includes('Cycle_005') || t.includes('COUNCIL REPORT')) {
                chatText = t;
                break;
            }
        }
        if (!chatText || chatText.length < 200) {
            const body = document.body.innerText;
            const rIdx = body.lastIndexOf('# [COUNCIL REPORT');
            if (rIdx !== -1) {
                chatText = body.substring(rIdx);
            } else {
                const cIdx = body.lastIndexOf('Cycle_005');
                if (cIdx !== -1) chatText = body.substring(cIdx);
            }
        }"""

if old_str in content:
    content = content.replace(old_str, new_str)
    content = content.replace('default=600.0', 'default=1800.0')
    old_reload = """        if (now - last_reload_time) >= RELOAD_INTERVAL_SEC:
            last_reload_time = now
            print(f"\\n[RockHardWatchdog t={elapsed}s] 5-Minute interval reached. Refreshing both tabs to prevent frontend DOM freeze...")
            if not arena_done:
                await reload_cdp_tab("arena.ai")
            if not zai_done:
                await reload_cdp_tab("chat.z.ai")
            await asyncio.sleep(2.0)"""
    new_reload = """        if (now - last_reload_time) >= RELOAD_INTERVAL_SEC:
            last_reload_time = now
            if not arena_done and not a_stat == "GENERATING":
                print(f"\\n[RockHardWatchdog t={elapsed}s] 5-Minute interval reached. Refreshing Arena tab...", flush=True)
                await reload_cdp_tab("arena.ai")
            if not zai_done and not z_stat == "GENERATING":
                print(f"\\n[RockHardWatchdog t={elapsed}s] 5-Minute interval reached. Refreshing Z.ai tab...", flush=True)
                await reload_cdp_tab("chat.z.ai")
            await asyncio.sleep(2.0)"""
    content = content.replace(old_reload, new_reload)
    with open('Terminal/rock_hard_dual_watchdog.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print('SUCCESSFULLY PATCHED rock_hard_dual_watchdog.py!')
else:
    print('old_str NOT FOUND in content')
