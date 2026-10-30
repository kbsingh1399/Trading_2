import pathlib

p = pathlib.Path("Terminal/rock_hard_dual_watchdog.py")
content = p.read_text(encoding="utf-8")

old_code = """        # Auto-refresh tab every 5 minutes until completed (Operator Mandate: unstick any stalled session)
        if not arena_done and (now - arena_last_reload) >= RELOAD_INTERVAL_SEC:
            arena_last_reload = now
            print(f"\\n[RockHardWatchdog t={elapsed}s] ⏱️ 5-Minute interval reached without Arena completion. Auto-refreshing Arena.ai tab via CDP Page.reload...", flush=True)
            await reload_cdp_tab("arena.ai")
            await asyncio.sleep(2.0)

        # Auto-refresh tab every 5 minutes until completed (Operator Mandate: unstick any stalled session)
        if not zai_done and (now - zai_last_reload) >= RELOAD_INTERVAL_SEC:
            zai_last_reload = now
            print(f"\\n[RockHardWatchdog t={elapsed}s] ⏱️ 5-Minute interval reached without Z.ai completion. Auto-refreshing Z.ai tab via CDP Page.reload...", flush=True)
            await reload_cdp_tab("z.ai")
            await asyncio.sleep(2.0)"""

new_code = """        # Auto-refresh tab every 5 minutes ONLY IF NOT ACTIVELY GENERATING (Protects in-flight model reasoning)
        if not arena_done and not a_gen_flag and (now - arena_last_reload) >= RELOAD_INTERVAL_SEC:
            arena_last_reload = now
            print(f"\\n[RockHardWatchdog t={elapsed}s] ⏱️ 5-Minute idle interval reached (not generating). Auto-refreshing Arena.ai tab via CDP Page.reload...", flush=True)
            await reload_cdp_tab("arena.ai")
            await asyncio.sleep(2.0)

        # Auto-refresh tab every 5 minutes ONLY IF NOT ACTIVELY GENERATING (Protects in-flight model reasoning)
        if not zai_done and not z_gen_flag and (now - zai_last_reload) >= RELOAD_INTERVAL_SEC:
            zai_last_reload = now
            print(f"\\n[RockHardWatchdog t={elapsed}s] ⏱️ 5-Minute idle interval reached (not generating). Auto-refreshing Z.ai tab via CDP Page.reload...", flush=True)
            await reload_cdp_tab("z.ai")
            await asyncio.sleep(2.0)"""

norm_content = content.replace("\r\n", "\n")
norm_old = old_code.replace("\r\n", "\n")
norm_new = new_code.replace("\r\n", "\n")

if norm_old in norm_content:
    norm_content = norm_content.replace(norm_old, norm_new, 1)
    p.write_text(norm_content, encoding="utf-8")
    print("SUCCESS: rock_hard_dual_watchdog.py patched with isGenerating guards!")
else:
    print("FAILED: old code not found")
