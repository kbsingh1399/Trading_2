import re
from pathlib import Path

path = Path("Terminal/rock_hard_dual_watchdog.py")
content = path.read_text(encoding="utf-8")

old_reload_func = '''async def reload_cdp_tab(match_keyword: str) -> bool:
    try:
        def get_tabs():
            try:
                with urllib.request.urlopen(CDP_URL, timeout=3) as r:
                    return json.loads(r.read().decode("utf-8"))
            except Exception:
                return []
        tabs = await asyncio.to_thread(get_tabs)
        for t in tabs:
            if match_keyword in t.get("url", "") and t.get("webSocketDebuggerUrl"):
                ws_url = t["webSocketDebuggerUrl"]
                try:
                    ws = await asyncio.wait_for(
                        websockets.connect(ws_url, max_size=10_000_000, open_timeout=3, close_timeout=1),
                        timeout=4.0
                    )
                    print(f"[RockHardWatchdog] Refreshing tab for '{match_keyword}' via CDP location.reload()...", flush=True)
                    await asyncio.wait_for(
                        ws.send(json.dumps({"id": 8888, "method": "Runtime.evaluate", "params": {"expression": "location.reload()", "returnByValue": False}})),
                        timeout=2.0
                    )
                    try:
                        await asyncio.wait_for(ws.close(), timeout=1.0)
                    except Exception:
                        pass
                    print(f"[RockHardWatchdog] 5-minute auto-refresh triggered for '{match_keyword}' successfully!", flush=True)
                    await asyncio.sleep(2.0)
                    return True
                except Exception as ws_err:
                    print(f"[RockHardWatchdog] Handled ws reload event for '{match_keyword}': {ws_err}", flush=True)
                    return True
    except Exception as e:
        print(f"[RockHardWatchdog] Warning on reload for '{match_keyword}': {e}", file=sys.stderr, flush=True)
    return False'''

new_reload_func = '''async def reload_cdp_tab(match_keyword: str) -> bool:
    try:
        def get_tabs():
            try:
                with urllib.request.urlopen(CDP_URL, timeout=3) as r:
                    return json.loads(r.read().decode("utf-8"))
            except Exception:
                return []
        tabs = await asyncio.to_thread(get_tabs)
        for t in tabs:
            url = t.get("url", "")
            if match_keyword in url and "preview-" not in url and t.get("webSocketDebuggerUrl"):
                ws_url = t["webSocketDebuggerUrl"]
                try:
                    ws = await asyncio.wait_for(
                        websockets.connect(ws_url, max_size=10_000_000, open_timeout=4, close_timeout=1),
                        timeout=5.0
                    )
                    print(f"[RockHardWatchdog] Refreshing tab for '{match_keyword}' via CDP Page.reload() & location.reload()...", flush=True)
                    # Page.reload protocol method
                    await ws.send(json.dumps({"id": 8888, "method": "Page.reload", "params": {"ignoreCache": True}}))
                    # Runtime.evaluate location.reload fallback
                    await ws.send(json.dumps({"id": 8889, "method": "Runtime.evaluate", "params": {"expression": "window.location.reload()", "returnByValue": False}}))
                    try:
                        await asyncio.wait_for(ws.close(), timeout=1.0)
                    except Exception:
                        pass
                    print(f"[RockHardWatchdog] 5-minute auto-refresh triggered for '{match_keyword}' successfully!", flush=True)
                    await asyncio.sleep(2.0)
                    return True
                except Exception as ws_err:
                    print(f"[RockHardWatchdog] Handled ws reload event for '{match_keyword}': {ws_err}", flush=True)
                    return True
    except Exception as e:
        print(f"[RockHardWatchdog] Warning on reload for '{match_keyword}': {e}", file=sys.stderr, flush=True)
    return False'''

old_refresh_trigger = '''        # Auto-refresh tab every 5 minutes ONLY IF NOT GENERATING (stuck/idle guardrail)
        if not arena_done and not a_gen_flag and (now - arena_last_reload) >= RELOAD_INTERVAL_SEC:
            arena_last_reload = now
            print(f"\\n[RockHardWatchdog t={elapsed}s] ⏱️ 5-Minute interval reached without Arena completion (idle/stuck). Auto-refreshing Arena.ai tab via CDP Page.reload...", flush=True)
            await reload_cdp_tab("arena.ai")
            await asyncio.sleep(2.0)

        # Auto-refresh tab every 5 minutes ONLY IF NOT GENERATING (stuck/idle guardrail)
        if not zai_done and not z_gen_flag and (now - zai_last_reload) >= RELOAD_INTERVAL_SEC:
            zai_last_reload = now
            print(f"\\n[RockHardWatchdog t={elapsed}s] ⏱️ 5-Minute interval reached without Z.ai completion (idle/stuck). Auto-refreshing Z.ai tab via CDP Page.reload...", flush=True)
            await reload_cdp_tab("chat.z.ai")
            await asyncio.sleep(2.0)'''

new_refresh_trigger = '''        # Auto-refresh tab every 5 minutes until completed (Operator Mandate: unstick any stalled session)
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
            await asyncio.sleep(2.0)'''

# Normalize newlines
content_norm = content.replace("\r\n", "\n")
old_reload_norm = old_reload_func.replace("\r\n", "\n")
old_refresh_norm = old_refresh_trigger.replace("\r\n", "\n")

if old_reload_norm in content_norm and old_refresh_norm in content_norm:
    content_norm = content_norm.replace(old_reload_norm, new_reload_func)
    content_norm = content_norm.replace(old_refresh_norm, new_refresh_trigger)
    path.write_text(content_norm, encoding="utf-8")
    print("SUCCESS: Updated rock_hard_dual_watchdog.py")
else:
    print("FAILED: Could not find matching targets")
