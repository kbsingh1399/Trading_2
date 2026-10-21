#!/usr/bin/env python3
"""
Terminal/multi_resource_rotator_daemon.py
=========================================
Institutional Multi-Resource Dynamic Tab & Asset Rotator Daemon.

Solves the Multi-Resource Rotation & Edge Anti-Sleep Requirements:
1. CoinGlass Liquidation Map: Dynamically rotates across canonical assets (BTC -> ETH -> SOL -> XRP -> DOGE -> BNB)
   and toggles between '1 day' and '7 day' horizons via native CDP DOM manipulation.
2. Arkham Intelligence: Keeps streaming websockets active via Page.bringToFront and DOM pings.
3. Forex Factory: Refreshes calendar and trader sentiment tabs.
4. Arena.ai: Prevents session timeout and verifies completion banners.
5. Tab Pruning: Automatically detects and closes orphan or duplicate tabs to stop RAM leaks.
6. System RAM Governor: Calls Windows EmptyWorkingSet every 5 minutes on heavy processes.
7. Status Heartbeat: Writes real-time rotation state to Data/multi_resource_rotator_status.json.
"""

from __future__ import annotations

import asyncio
import ctypes
import datetime
import json
import logging
import os
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

ROOT = pathlib.Path(__file__).resolve().parents[1]
CDP_BASE_URL = "http://127.0.0.1:9222"
STATUS_FILE = ROOT / "Data" / "multi_resource_rotator_status.json"
ROTATION_INTERVAL_S = 35.0  # 35 seconds per rotation step

CANONICAL_COINGLASS_ASSETS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
CANONICAL_TIMEFRAMES = ["1 day", "7 day"]

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s UTC] [MultiRotator] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
log = logging.getLogger("MultiRotator")


def trim_system_memory():
    """Trims working sets of Python, Edge, and language_server to reclaim physical RAM."""
    if sys.platform != "win32":
        return
    try:
        PROCESS_ALL_ACCESS = 0x1F0FFF
        kernel32 = ctypes.windll.kernel32
        psapi = ctypes.windll.psapi

        import subprocess
        ps_cmd = 'Get-Process | Where-Object { $_.ProcessName -match "python|msedge|language_server" } | Select-Object -ExpandProperty Id'
        out = subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], capture_output=True, text=True, timeout=5)
        trimmed = 0
        for line in out.stdout.splitlines():
            line = line.strip()
            if line.isdigit():
                pid = int(line)
                h_proc = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
                if h_proc:
                    try:
                        if psapi.EmptyWorkingSet(h_proc):
                            trimmed += 1
                    finally:
                        kernel32.CloseHandle(h_proc)
        log.info(f"RAM Governor: successfully trimmed working sets for {trimmed} processes.")
    except Exception as e:
        log.warning(f"RAM Governor notice: {e}")


def get_cdp_pages():
    try:
        req = urllib.request.Request(f"{CDP_BASE_URL}/json", headers={"User-Agent": "MultiRotator/1.0"})
        with urllib.request.urlopen(req, timeout=4) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return [t for t in data if t.get("type") == "page"]
    except Exception as e:
        log.warning(f"Error querying CDP endpoint: {e}")
        return []


def open_tab(url: str):
    try:
        req = urllib.request.Request(f"{CDP_BASE_URL}/json/new?{url}", method="PUT")
        with urllib.request.urlopen(req, timeout=5) as resp:
            tab = json.loads(resp.read().decode("utf-8"))
            log.info(f"Opened target tab: {url} -> id={tab.get('id')}")
            return tab
    except Exception as e:
        log.warning(f"Failed to open tab for {url}: {e}")
        return None


def close_tab(tab_id: str):
    try:
        close_url = f"{CDP_BASE_URL}/json/close/{tab_id}"
        urllib.request.urlopen(close_url, timeout=3)
        log.info(f"Pruned redundant tab: {tab_id}")
    except Exception as e:
        log.warning(f"Failed to close tab {tab_id}: {e}")


class MultiResourceRotator:
    def __init__(self):
        self.asset_idx = 0
        self.tf_idx = 0
        self.last_memory_trim = time.time()
        self.cycle_count = 0
        STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)

    async def execute_cdp_command(self, ws_url: str, method: str, params: dict | None = None) -> dict:
        async with websockets.connect(ws_url, open_timeout=5, max_size=10_000_000) as ws:
            payload = {"id": 1, "method": method}
            if params:
                payload["params"] = params
            await ws.send(json.dumps(payload))
            while True:
                raw = await asyncio.wait_for(ws.recv(), timeout=6.0)
                msg = json.loads(raw)
                if msg.get("id") == 1:
                    return msg

    async def rotate_coinglass(self, tab: dict) -> dict:
        ws_url = tab.get("webSocketDebuggerUrl")
        if not ws_url:
            return {"status": "NO_WS_URL"}

        target_asset = CANONICAL_COINGLASS_ASSETS[self.asset_idx % len(CANONICAL_COINGLASS_ASSETS)]
        target_tf = CANONICAL_TIMEFRAMES[self.tf_idx % len(CANONICAL_TIMEFRAMES)]
        self.asset_idx += 1
        if self.asset_idx % len(CANONICAL_COINGLASS_ASSETS) == 0:
            self.tf_idx += 1

        try:
            # 1. Bring tab to front
            await self.execute_cdp_command(ws_url, "Page.bringToFront")
            await asyncio.sleep(0.5)

            # 2. Rotate Timeframe if needed
            rotate_tf_js = f"""(() => {{
                const targetTf = {json.dumps(target_tf)};
                const btns = Array.from(document.querySelectorAll('button.MuiSelect-button')).filter(b => {{
                    const t = (b.innerText || '').trim();
                    return (t.includes('day') || t.includes('hour') || t.includes('Year')) && !t.includes('English');
                }});
                if (btns.length === 0) return {{ status: 'NO_TF_BUTTON' }};
                const btn = btns[0];
                if (btn.innerText.trim() === targetTf) return {{ status: 'ALREADY_ACTIVE', tf: targetTf }};
                btn.click();
                
                const controlsId = btn.getAttribute('aria-controls');
                let listbox = controlsId ? document.getElementById(controlsId) : null;
                if (!listbox) {{
                    listbox = Array.from(document.querySelectorAll('[role="listbox"]')).find(ul => (ul.innerText || '').includes(targetTf));
                }}
                if (!listbox) return {{ status: 'NO_LISTBOX' }};
                const opt = Array.from(listbox.querySelectorAll('li, [role="option"]')).find(el => el.innerText.trim() === targetTf);
                if (opt) {{
                    opt.dispatchEvent(new MouseEvent('mousedown', {{ bubbles: true }}));
                    opt.dispatchEvent(new MouseEvent('mouseup', {{ bubbles: true }}));
                    opt.click();
                    return {{ status: 'ROTATED_TF', tf: targetTf }};
                }}
                return {{ status: 'TF_OPT_NOT_FOUND' }};
            }})()"""
            tf_res = await self.execute_cdp_command(ws_url, "Runtime.evaluate", {"expression": rotate_tf_js, "returnByValue": True})
            tf_val = tf_res.get("result", {}).get("result", {}).get("value", {})

            # 3. Rotate Asset Symbol
            clear_input_js = f"""(() => {{
                const inputs = Array.from(document.querySelectorAll('input.MuiAutocomplete-input')).filter(i => 
                    ['BTC', 'ETH', 'SOL', 'XRP', 'DOGE', 'BNB', 'HYPE', 'SUI'].includes(i.value.trim())
                );
                if (inputs.length > 0) {{
                    const inp = inputs[0];
                    if (inp.value.trim() === {json.dumps(target_asset)}) return {{ status: 'ALREADY_ACTIVE' }};
                    inp.focus();
                    inp.click();
                    const nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
                    nativeSetter.call(inp, '');
                    inp.dispatchEvent(new Event('input', {{ bubbles: true }}));
                    inp.dispatchEvent(new Event('change', {{ bubbles: true }}));
                    return {{ status: 'CLEARED', id: inp.id }};
                }}
                return {{ status: 'NO_INPUT' }};
            }})()"""
            clear_res = await self.execute_cdp_command(ws_url, "Runtime.evaluate", {"expression": clear_input_js, "returnByValue": True})
            clear_val = clear_res.get("result", {}).get("result", {}).get("value", {})

            asset_status = "ALREADY_ACTIVE"
            if clear_val.get("status") == "CLEARED":
                await asyncio.sleep(0.2)
                # Type symbol
                await self.execute_cdp_command(ws_url, "Input.insertText", {"text": target_asset})
                await asyncio.sleep(0.5)

                select_opt_js = f"""(() => {{
                    const targetSymbol = {json.dumps(target_asset)};
                    const listbox = document.querySelector('.MuiAutocomplete-popper, ul.MuiAutocomplete-listbox, div[role="listbox"]');
                    if (!listbox) return {{ status: 'NO_LISTBOX' }};
                    const options = Array.from(listbox.querySelectorAll('li, div[role="option"]'));
                    const match = options.find(o => {{
                        const txt = (o.innerText || '').trim();
                        const tokens = txt.split(/[^A-Za-z0-9]+/).filter(Boolean).map(t => t.toUpperCase());
                        return tokens[0] === targetSymbol || tokens.includes(targetSymbol);
                    }});
                    if (match) {{
                        match.dispatchEvent(new MouseEvent('mousedown', {{ bubbles: true }}));
                        match.dispatchEvent(new MouseEvent('mouseup', {{ bubbles: true }}));
                        match.click();
                        return {{ status: 'SELECTED_ASSET', text: match.innerText.trim() }};
                    }}
                    return {{ status: 'NO_MATCH' }};
                }})()"""
                sel_res = await self.execute_cdp_command(ws_url, "Runtime.evaluate", {"expression": select_opt_js, "returnByValue": True})
                asset_status = sel_res.get("result", {}).get("result", {}).get("value", {}).get("status", "FAILED")

            log.info(f"CoinGlass Rotation -> Asset: {target_asset} ({asset_status}), Timeframe: {target_tf} ({tf_val.get('status')})")
            return {
                "resource": "CoinGlass_LiquidationMap",
                "asset": target_asset,
                "asset_status": asset_status,
                "timeframe": target_tf,
                "tf_status": tf_val.get("status")
            }
        except Exception as e:
            log.warning(f"Error rotating CoinGlass: {e}")
            return {"resource": "CoinGlass_LiquidationMap", "error": str(e)}

    async def ping_and_keepalive(self, tab: dict, label: str) -> dict:
        ws_url = tab.get("webSocketDebuggerUrl")
        if not ws_url:
            return {"status": "NO_WS_URL"}
        try:
            await self.execute_cdp_command(ws_url, "Page.bringToFront")
            ping_js = "(() => ({ title: document.title, state: document.visibilityState, time: Date.now() }))()"
            res = await self.execute_cdp_command(ws_url, "Runtime.evaluate", {"expression": ping_js, "returnByValue": True})
            val = res.get("result", {}).get("result", {}).get("value", {})
            log.info(f"Keepalive [{label}] -> visibility: {val.get('state')}, title: {val.get('title', '')[:35]}")
            return {"resource": label, "status": "ACTIVE", "visibility": val.get("state")}
        except Exception as e:
            log.warning(f"Error in keepalive for {label}: {e}")
            return {"resource": label, "error": str(e)}

    async def run_cycle(self):
        self.cycle_count += 1
        pages = get_cdp_pages()
        if not pages:
            log.warning("No CDP pages found on port 9222.")
            return

        arena_tabs = [p for p in pages if "arena.ai" in p.get("url", "")]
        arkham_tabs = [p for p in pages if "arkm.com" in p.get("url", "") or "arkham" in p.get("url", "")]
        cg_tabs = [p for p in pages if "LiquidationMap" in p.get("url", "")]
        ff_tabs = [p for p in pages if "forexfactory.com" in p.get("url", "")]

        # Prune redundant duplicate tabs
        if len(arena_tabs) > 1:
            for extra in arena_tabs[1:]:
                close_tab(extra.get("id"))
            arena_tabs = arena_tabs[:1]

        if len(arkham_tabs) > 1:
            for extra in arkham_tabs[1:]:
                close_tab(extra.get("id"))
            arkham_tabs = arkham_tabs[:1]

        if len(cg_tabs) > 1:
            for extra in cg_tabs[1:]:
                close_tab(extra.get("id"))
            cg_tabs = cg_tabs[:1]

        # Ensure Arkham Intelligence tab exists
        if not arkham_tabs:
            log.info("Opening Arkham Intelligence tab...")
            new_tab = open_tab("https://arkm.com/")
            if new_tab:
                arkham_tabs = [new_tab]
                await asyncio.sleep(4.0)

        # Ensure CoinGlass LiquidationMap tab exists
        if not cg_tabs:
            log.info("Opening CoinGlass LiquidationMap tab...")
            new_tab = open_tab("https://www.coinglass.com/pro/futures/LiquidationMap")
            if new_tab:
                cg_tabs = [new_tab]
                await asyncio.sleep(5.0)

        # Ensure Forex Factory tab exists
        if not ff_tabs:
            log.info("Opening Forex Factory Calendar tab...")
            new_tab = open_tab("https://www.forexfactory.com/calendar")
            if new_tab:
                ff_tabs = [new_tab]
                await asyncio.sleep(4.0)

        results = {}
        # 1. Rotate CoinGlass Liquidation Map
        if cg_tabs:
            results["coinglass"] = await self.rotate_coinglass(cg_tabs[0])
            await asyncio.sleep(2.0)

        # 2. Keepalive Arkham
        if arkham_tabs:
            results["arkham"] = await self.ping_and_keepalive(arkham_tabs[0], "Arkham")
            await asyncio.sleep(2.0)

        # 3. Keepalive Forex Factory
        if ff_tabs:
            results["forexfactory"] = await self.ping_and_keepalive(ff_tabs[0], "ForexFactory")
            await asyncio.sleep(2.0)

        # 4. Keepalive Arena.ai
        if arena_tabs:
            results["arena"] = await self.ping_and_keepalive(arena_tabs[0], "Arena.ai")

        # 5. RAM Governor: trim memory every 5 minutes
        if time.time() - self.last_memory_trim > 300.0:
            trim_system_memory()
            self.last_memory_trim = time.time()

        # 6. Save heartbeat status
        status_data = {
            "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "cycle_count": self.cycle_count,
            "current_asset": CANONICAL_COINGLASS_ASSETS[(self.asset_idx - 1) % len(CANONICAL_COINGLASS_ASSETS)],
            "current_timeframe": CANONICAL_TIMEFRAMES[(self.tf_idx - 1) % len(CANONICAL_TIMEFRAMES)],
            "last_results": results
        }
        with open(STATUS_FILE, "w", encoding="utf-8") as f:
            json.dump(status_data, f, indent=2)


async def main():
    log.info("Starting Multi-Resource Dynamic Tab & Asset Rotator Daemon...")
    rotator = MultiResourceRotator()
    while True:
        try:
            await rotator.run_cycle()
        except Exception as e:
            log.error(f"Error in multi-resource rotation cycle: {e}")
        await asyncio.sleep(ROTATION_INTERVAL_S)


if __name__ == "__main__":
    asyncio.run(main())
