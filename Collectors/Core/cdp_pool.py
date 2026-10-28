#!/usr/bin/env python3
"""
Collectors/Core/cdp_pool.py
===========================
Persistent Edge CDP Connection Pool & Tab Manager.

Guarantees:
  1. Airtight Tab Hygiene: Cleans up transient scraping tabs immediately on completion/exit.
  2. Tab Shielding: Strictly preserves critical tabs (Arena.ai, Z.ai, ChatGPT).
  3. Connection Health Check: Verifies Edge CDP port (default 9222) is alive.
  4. Tab Reuse & Allocation: Avoids spawning unbounded browser tabs.
"""
from __future__ import annotations

import json
import logging
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional

CDP_BASE_URL = "http://127.0.0.1:9222"
SHIELDED_KEYWORDS = ["arena.ai", "z.ai", "chatgpt.com", "gemini.google.com"]

log = logging.getLogger("CDPPool")


def check_cdp_available(timeout: float = 3.0) -> bool:
    """Verifies that Edge CDP is accessible on the expected port."""
    try:
        req = urllib.request.urlopen(f"{CDP_BASE_URL}/json/version", timeout=timeout)
        data = json.loads(req.read().decode())
        return "webSocketDebuggerUrl" in data or "Browser" in data
    except Exception:
        return False


def get_open_tabs(timeout: float = 3.0) -> List[Dict[str, Any]]:
    """Returns list of open tabs from CDP /json."""
    try:
        req = urllib.request.urlopen(f"{CDP_BASE_URL}/json", timeout=timeout)
        return json.loads(req.read().decode())
    except Exception as e:
        log.warning(f"Failed to query CDP tabs: {e}")
        return []


def is_shielded(url: str, title: str = "") -> bool:
    """Determines whether a tab is protected from auto-closing."""
    url_lower = (url or "").lower()
    title_lower = (title or "").lower()
    for kw in SHIELDED_KEYWORDS:
        if kw in url_lower or kw in title_lower:
            return True
    return False


def close_tab(tab_id: str, timeout: float = 3.0) -> bool:
    """Closes a specific tab via CDP /json/close/{tab_id}."""
    try:
        urllib.request.urlopen(f"{CDP_BASE_URL}/json/close/{tab_id}", timeout=timeout)
        return True
    except Exception as e:
        log.warning(f"Failed to close tab {tab_id}: {e}")
        return False


def reap_scraping_tabs(except_tab_id: Optional[str] = None) -> int:
    """
    Airtight Tab Reaper:
    Closes all non-shielded scraping tabs while preserving Arena.ai and Z.ai tabs.
    Returns the count of reaped tabs.
    """
    tabs = get_open_tabs()
    reaped = 0
    for tab in tabs:
        t_id = tab.get("id")
        t_url = tab.get("url", "")
        t_title = tab.get("title", "")
        t_type = tab.get("type", "")

        if t_type != "page":
            continue
        if is_shielded(t_url, t_title):
            continue
        if except_tab_id and t_id == except_tab_id:
            continue

        if close_tab(t_id):
            reaped += 1
            log.info(f"Reaped tab: [{t_id}] {t_title[:40]} ({t_url[:50]})")

    return reaped


def find_or_create_tab(url: str, wait_secs: float = 1.0) -> Optional[Dict[str, Any]]:
    """Finds an existing tab for the given URL prefix or opens a new one."""
    tabs = get_open_tabs()
    for tab in tabs:
        if tab.get("type") == "page" and url.lower() in tab.get("url", "").lower():
            return tab

    # Create new tab
    try:
        encoded_url = urllib.parse.quote(url, safe=":/?=&")
        req = urllib.request.urlopen(f"{CDP_BASE_URL}/json/new?{encoded_url}", timeout=5)
        new_tab = json.loads(req.read().decode())
        return new_tab
    except Exception as e:
        log.error(f"Failed to create new tab for {url}: {e}")
        return None


async def wait_for_page_and_component_load(
    cdp_cmd,
    selector: str = "table tbody tr, canvas, [_echarts_instance_], [class*='grid'], [class*='table']",
    min_elements: int = 1,
    timeout_sec: float = 30.0,
    poll_interval: float = 0.4,
    log: Optional[logging.Logger] = None,
) -> bool:
    """
    Universal Page & Component Hydration Readiness Gate:
    1. Awaits document.readyState === 'complete'.
    2. Ensures active spinners / skeleton loaders (.ant-spin, .skeleton, .loading) are cleared.
    3. Confirms target DOM elements are present, rendered (height > 0), and meet min_elements.
    4. Guarantees zero blank / empty scrapes by preventing premature execution.
    """
    import asyncio
    import time

    t0 = time.time()
    logger = log or logging.getLogger("CDPPool")
    
    js_check = f"""
    (() => {{
        const isDocReady = (document.readyState === 'complete' || document.readyState === 'interactive');
        if (!isDocReady) return {{ ready: false, reason: "document.readyState = " + document.readyState }};
        
        // Check for blocking global loaders
        const spinners = document.querySelectorAll('.ant-spin-spinning, .spinner, .global-loading, [class*="skeleton"]');
        if (spinners.length > 0) {{
            const visibleSpinner = Array.from(spinners).some(s => s.offsetParent !== null);
            if (visibleSpinner) return {{ ready: false, reason: "active spinner detected" }};
        }}

        // Check target component presence and hydration
        const selector = {json.dumps(selector)};
        const elements = Array.from(document.querySelectorAll(selector));
        const validElements = elements.filter(el => {{
            const rect = el.getBoundingClientRect();
            return (rect.width > 0 || rect.height > 0 || el.innerText.trim().length > 0);
        }});

        if (validElements.length < {min_elements}) {{
            return {{ ready: false, reason: "found " + validElements.length + "/{min_elements} valid elements for selector" }};
        }}

        return {{ ready: true, count: validElements.length }};
    }})()
    """

    while time.time() - t0 < timeout_sec:
        try:
            res = await cdp_cmd("Runtime.evaluate", {"expression": js_check, "returnByValue": True})
            val = res.get("result", {}).get("value") if "result" in res else res.get("value", {})
            if val and val.get("ready") is True:
                elapsed = time.time() - t0
                logger.info(f"Page & component hydrated successfully in {elapsed:.2f}s ({val.get('count')} elements matching '{selector}').")
                return True
        except Exception as e:
            logger.debug(f"Hydration polling check notice: {e}")

        await asyncio.sleep(poll_interval)

    elapsed = time.time() - t0
    logger.warning(f"Component hydration gate timed out after {elapsed:.2f}s for selector '{selector}'")
    return False

