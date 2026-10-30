"""
Terminal/autonomous_cdp_tab_refresher_daemon.py
Autonomous background daemon to refresh Arena.ai and Z.ai tabs on Chrome CDP (port 9222)
every 5 minutes (300 seconds) continuously.
"""

import asyncio
import datetime
import json
import sys
import time
import urllib.request
import websockets

CDP_URL = "http://127.0.0.1:9222/json"
REFRESH_INTERVAL_SECONDS = 300  # 5 minutes

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
except Exception:
    pass

def log(msg: str):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] [CDP-Refresher-Daemon] {msg}", flush=True)

def get_target_tabs():
    try:
        with urllib.request.urlopen(CDP_URL, timeout=4) as r:
            tabs = json.loads(r.read().decode("utf-8"))
        arena_tab = next((t for t in tabs if "arena.ai" in t.get("url", "") and "preview-" not in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)
        zai_tab = next((t for t in tabs if "chat.z.ai" in t.get("url", "") and "preview-" not in t.get("url", "") and t.get("webSocketDebuggerUrl")), None)
        return arena_tab, zai_tab
    except Exception as e:
        log(f"Error fetching CDP tabs from {CDP_URL}: {e}")
        return None, None

async def reload_tab(ws_url: str, tab_name: str) -> bool:
    try:
        ws = await asyncio.wait_for(
            websockets.connect(ws_url, max_size=10_000_000, open_timeout=4, close_timeout=1),
            timeout=5.0
        )
        # Send Page.reload
        await ws.send(json.dumps({"id": 7771, "method": "Page.reload", "params": {"ignoreCache": True}}))
        # Fallback Runtime.evaluate
        await ws.send(json.dumps({"id": 7772, "method": "Runtime.evaluate", "params": {"expression": "window.location.reload()", "returnByValue": False}}))
        try:
            await asyncio.wait_for(ws.close(), timeout=1.0)
        except Exception:
            pass
        log(f"✅ Successfully refreshed {tab_name} tab via CDP!")
        return True
    except Exception as e:
        log(f"⚠️ Exception refreshing {tab_name} tab: {e}")
        return False

async def main():
    log("🚀 Autonomous CDP Tab Refresher Daemon started (5-minute interval).")
    
    while True:
        try:
            log("Checking Chrome CDP (port 9222) for Arena.ai and Z.ai tabs...")
            arena_tab, zai_tab = get_target_tabs()
            
            if arena_tab:
                log(f"Refreshing Arena.ai tab ({arena_tab.get('url')})...")
                await reload_tab(arena_tab["webSocketDebuggerUrl"], "Arena.ai")
                await asyncio.sleep(2.0)
            else:
                log("Arena.ai tab not detected on port 9222.")
                
            if zai_tab:
                log(f"Refreshing Z.ai tab ({zai_tab.get('url')})...")
                await reload_tab(zai_tab["webSocketDebuggerUrl"], "Z.ai")
                await asyncio.sleep(2.0)
            else:
                log("Z.ai tab not detected on port 9222.")
                
            log(f"Next refresh cycle in {REFRESH_INTERVAL_SECONDS} seconds (5 minutes). Sleeping...")
        except Exception as e:
            log(f"Loop error: {e}")
            
        await asyncio.sleep(REFRESH_INTERVAL_SECONDS)

if __name__ == "__main__":
    asyncio.run(main())
