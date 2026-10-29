from pathlib import Path

p = Path("Terminal/arena_completion_daemon.py")
txt = p.read_text(encoding="utf-8")

# Fix 1: timers and variables
old_str = "    arena_last_refresh: float = 0.0\n    zai_last_refresh: float = 0.0\n    \n    stable_arena_ticks: int = 0\n    stable_zai_ticks: int = 0\n    \n    last_arena_hash: str = \"\"\n    last_zai_hash: str = \"\""

new_str = "    arena_last_refresh: float = time.time()\n    zai_last_refresh: float = time.time()\n    \n    stable_arena_ticks: int = 0\n    stable_zai_ticks: int = 0\n    \n    last_arena_hash: str = \"\"\n    last_zai_hash: str = \"\"\n    astate: dict = {}\n    zstate: dict = {}"

if old_str in txt:
    txt = txt.replace(old_str, new_str, 1)
    print("Patch 1 applied!")
else:
    print("Patch 1 not matched!")

# Fix 2: auto-refresh check in wait
old_refresh = "            # Operator Mandate: Auto-refresh Arena tab every 5 minutes until completed\n            if not arena_done and (now - arena_last_refresh) >= refresh_limit_s:"
new_refresh = "            # Operator Mandate: Auto-refresh Arena tab every 5 minutes until completed (only if generating for >= refresh_limit_s)\n            gen_dur = (now - arena_gen_start) if arena_gen_start > 0 else 0.0\n            if is_a_gen and gen_dur >= refresh_limit_s and (now - arena_last_refresh) >= refresh_limit_s:"

if old_refresh in txt:
    txt = txt.replace(old_refresh, new_refresh, 1)
    print("Patch 2 applied!")
else:
    print("Patch 2 not matched!")

# Fix 3: auto-refresh check for Z.ai in wait
old_z_refresh = "            # Operator Mandate: Auto-refresh Z.ai tab every 5 minutes until completed\n            if not zai_done and (now - zai_last_refresh) >= refresh_limit_s:"
new_z_refresh = "            # Operator Mandate: Auto-refresh Z.ai tab every 5 minutes until completed (only if generating for >= refresh_limit_s)\n            z_dur = (now - zai_gen_start) if zai_gen_start > 0 else 0.0\n            if is_z_gen and z_dur >= refresh_limit_s and (now - zai_last_refresh) >= refresh_limit_s:"

if old_z_refresh in txt:
    txt = txt.replace(old_z_refresh, new_z_refresh, 1)
    print("Patch 3 applied!")
else:
    print("Patch 3 not matched!")

# Fix 4: timers in run_persistent_daemon
old_p_timers = "    arena_gen_start: float = 0.0\n    arena_last_refresh: float = 0.0\n    zai_gen_start: float = 0.0\n    zai_last_refresh: float = 0.0"
new_p_timers = "    arena_gen_start: float = 0.0\n    arena_last_refresh: float = time.time()\n    zai_gen_start: float = 0.0\n    zai_last_refresh: float = time.time()"

if old_p_timers in txt:
    txt = txt.replace(old_p_timers, new_p_timers, 1)
    print("Patch 4 applied!")
else:
    print("Patch 4 not matched!")

p.write_text(txt, encoding="utf-8")
print("Saved patched file!")
