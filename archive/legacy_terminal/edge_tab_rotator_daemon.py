"""
Terminal/edge_tab_rotator_daemon.py
Edge Tab Keep-Alive, Auto-Rotation & Anti-Sleep Daemon.

Solves the Edge 'Sleeping Tabs' and dead renderer issue:
1. Prevents Edge from freezing or unloading background tabs (Arkham, Arena.ai).
2. Rotates focus in round-robin using CDP `Page.bringToFront` and `Runtime.evaluate` pings every 45 seconds.
3. Automatically detects and PRUNES duplicate tabs to prevent tab explosion and RAM leaks.
4. Ensures Arkham streaming and Arena.ai WebSocket connections remain 100% active and responsive.
"""

import asyncio
import json
import logging
import pathlib
import sys
import time
import urllib.request
import websockets

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

CDP_JSON_URL = "http://127.0.0.1:9222/json"
ROTATION_INTERVAL_SECONDS = 45

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s UTC] [EdgeRotator] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
log = logging.getLogger("EdgeRotator")

def get_open_pages():
    try:
        req = urllib.request.Request(CDP_JSON_URL, headers={"User-Agent": "EdgeRotatorDaemon/1.0"})
        with urllib.request.urlopen(req, timeout=4) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return [t for t in data if t.get("type") == "page"]
    except Exception as e:
        log.warning(f"Error querying Chrome/Edge CDP endpoint: {e}")
        return []

def close_tab(tab_id: str):
    try:
        close_url = f"http://127.0.0.1:9222/json/close/{tab_id}"
        urllib.request.urlopen(close_url, timeout=3)
        log.info(f"Pruned redundant duplicate tab: {tab_id}")
    except Exception as e:
        log.warning(f"Failed to close tab {tab_id}: {e}")

async def ping_tab(ws_url: str, tab_name: str) -> bool:
    try:
        async with websockets.connect(ws_url, open_timeout=4, max_size=5_000_000) as ws:
            # 1. Bring tab to front to un-throttle renderer and reset idle timers
            await ws.send(json.dumps({"id": 1, "method": "Page.bringToFront"}))
            try:
                await asyncio.wait_for(ws.recv(), timeout=2.0)
            except Exception:
                pass

            # 2. Touch document to keep V8 alive and verify responsive state
            ping_js = "(() => ({ title: document.title, state: document.visibilityState, time: Date.now() }))()"
            await ws.send(json.dumps({
                "id": 2,
                "method": "Runtime.evaluate",
                "params": {"expression": ping_js, "returnByValue": True}
            }))
            resp_raw = await asyncio.wait_for(ws.recv(), timeout=3.0)
            resp = json.loads(resp_raw)
            val = resp.get("result", {}).get("result", {}).get("value", {})
            log.info(f"Refreshed tab [{tab_name}] — state: {val.get('state')}, title: {val.get('title', '')[:35]}")
            return True
    except Exception as e:
        log.warning(f"Failed pinging [{tab_name}] over ws: {e}")
        return False

async def rotation_cycle():
    pages = get_open_pages()
    if not pages:
        log.warning("No open pages found on CDP port 9222.")
        return

    # Categorize tabs and prune duplicates
    arena_tabs = []
    arkham_tabs = []
    other_tabs = []

    for p in pages:
        url = p.get("url", "")
        if "arena.ai" in url:
            arena_tabs.append(p)
        elif "arkm.com" in url or "arkham" in url:
            arkham_tabs.append(p)
        else:
            other_tabs.append(p)

    # Dedup Arena tabs: keep only the first active one, close extras
    if len(arena_tabs) > 1:
        log.info(f"Detected {len(arena_tabs)} Arena tabs. Pruning duplicates...")
        for extra in arena_tabs[1:]:
            close_tab(extra.get("id"))
        arena_tabs = arena_tabs[:1]

    # Dedup Arkham tabs safely: preserve the user's primary streaming tab (arkm.com/)
    # Primary tab is any arkm.com tab that is not an entity/tx scrape tab
    primary_arkham = [p for p in arkham_tabs if not any(x in p.get("url", "") for x in ["/explorer/entity/", "/explorer/tx/"])]
    entity_arkham = [p for p in arkham_tabs if "/explorer/entity/" in p.get("url", "")]
    
    # Never close the primary tab! If multiple root tabs exist, keep the oldest/first
    if len(primary_arkham) > 1:
        log.info(f"Detected {len(primary_arkham)} root Arkham tabs. Keeping primary and cleaning duplicates...")
        for extra in primary_arkham[1:]:
            close_tab(extra.get("id"))
        primary_arkham = primary_arkham[:1]
        
    # Rotate through primary tab if available, else first entity tab
    arkham_tabs = primary_arkham if primary_arkham else (entity_arkham[:1] if entity_arkham else [])

    # Rotate through active target tabs
    targets = []
    for t in arena_tabs:
        if t.get("webSocketDebuggerUrl"):
            targets.append((t["webSocketDebuggerUrl"], "Arena.ai"))
    for t in arkham_tabs:
        if t.get("webSocketDebuggerUrl"):
            targets.append((t["webSocketDebuggerUrl"], "Arkham"))

    for ws_url, name in targets:
        await ping_tab(ws_url, name)
        await asyncio.sleep(2.0)

async def main():
    log.info("Starting Edge Tab Keep-Alive & Auto-Rotation Daemon...")
    while True:
        try:
            await rotation_cycle()
        except Exception as e:
            log.error(f"Error in rotation cycle: {e}")
        await asyncio.sleep(ROTATION_INTERVAL_SECONDS)

if __name__ == "__main__":
    asyncio.run(main())
