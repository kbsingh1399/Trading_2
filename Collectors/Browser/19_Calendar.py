#!/usr/bin/env python3
"""
Data/Excel_Modules/19_Calendar.py
=================================
Forex Factory Live Institutional Macroeconomic Calendar Harvester.
Captures global economic releases, central bank decisions, and macro volatility drivers from:
  https://www.forexfactory.com/calendar
with dual-source resilience (Live Chrome CDP + Fair Economy JSON fallback).

Extracted Columns:
  1. Sr.No
  2. Date (e.g. Mon Oct 19, 2026)
  3. Time (Release Time)
  4. Currency (USD, EUR, GBP, JPY, AUD, CAD, NZD, CHF, CNY, etc.)
  5. Impact Tier (High / Medium / Low / Non-Economic)
  6. Economic Event Title
  7. Actual Figure
  8. Forecast Figure
  9. Previous Figure
  10. Surprise / Outcome (Better than Forecast / Worse than Forecast / As Expected / Pending)
  11. Market Directional Bias (Hawkish / Bullish, Dovish / Bearish, Neutral)
  12. Forex Factory Event URL

Outputs:
  - Excel Worksheet: '19_Calendar' positioned at Index 28 in Data/feeds/<feed_name>.parquet
  - JSON Archive: Data/ForexFactory/19_Calendar_ThisWeek.json
"""

from __future__ import annotations


import argparse
import asyncio
import datetime
import json
import logging
import os
import pathlib
import re
import sys
import time
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

import websockets

# Parquet Writer Imports
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'Collectors' / 'Core'))
sys.path.insert(0, str(ROOT / 'Terminal' / 'Data_Factory'))
from parquet_feed_writer import write_parquet_feed, IST_TZ, UTC_TZ

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("19_Calendar")

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
DEFAULT_DATA_DIR = ROOT_DIR / "Data" / "ForexFactory"
CALENDAR_URL = "https://www.forexfactory.com/calendar"
JSON_FALLBACK_URL = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"
SHEET_NAME = "19_Calendar"
CDP_BASE_URL = "http://127.0.0.1:9222"


# =====================================================================
# 1. QUANTITATIVE SURPRISE & DIRECTIONAL BIAS INFERENCE
# =====================================================================
def infer_market_bias(event_title: str, outcome: str) -> str:
    """Infers market directional bias from actual vs forecast outcomes."""
    title_upper = event_title.upper()

    if outcome == "Pending" or not outcome:
        return "Upcoming / Pending"

    is_inverted = any(
        kw in title_upper
        for kw in ["UNEMPLOYMENT", "JOBLESS CLAIMS", "INFLATION", "CPI", "PPI", "DEBT", "DEFICIT"]
    )

    if outcome == "Better than Forecast":
        return "Dovish / Easing" if is_inverted else "Hawkish / Currency Bullish"
    elif outcome == "Worse than Forecast":
        return "Hawkish / Tightening" if is_inverted else "Dovish / Currency Bearish"
    elif outcome == "As Expected":
        return "Neutral / Fully Priced In"
    return "Neutral"


# =====================================================================
# 2. CHROME CDP CALENDAR HARVESTER
# =====================================================================
async def harvest_calendar_cdp() -> List[Dict[str, Any]]:
    """Harvests live economic calendar from Forex Factory via Chrome CDP."""
    log.info(f"Connecting to Chrome CDP at {CDP_BASE_URL}...")
    try:
        with urllib.request.urlopen(f"{CDP_BASE_URL}/json", timeout=6) as resp:
            tabs = json.loads(resp.read().decode())
    except Exception as exc:
        log.warning(f"CDP connection failed: {exc}. Will attempt JSON fallback.")
        return []

    cal_tab = None
    created = False
    for t in tabs:
        if "forexfactory.com/calendar" in t.get("url", ""):
            cal_tab = t
            log.info(f"Reusing existing Forex Factory Calendar tab (ID: {t.get('id')})")
            break

    if not cal_tab:
        log.info(f"Opening temporary calendar tab at {CALENDAR_URL}...")
        create_url = f"{CDP_BASE_URL}/json/new?{CALENDAR_URL}"
        req = urllib.request.Request(create_url, method="PUT")
        try:
            with urllib.request.urlopen(req, timeout=8) as resp:
                cal_tab = json.loads(resp.read().decode())
            created = True
            await asyncio.sleep(4.0)
        except Exception as exc:
            log.warning(f"Failed to open CDP calendar tab: {exc}")
            return []

    ws_url = cal_tab.get("webSocketDebuggerUrl")
    if not ws_url:
        return []

    data = []
    try:
        async with websockets.connect(ws_url, max_size=10_000_000) as ws:
            js_script = """
            (() => {
                const rows = document.querySelectorAll('tr.calendar__row');
                const events = [];
                let lastDate = '';
                let lastTime = '';
                
                rows.forEach(r => {
                    const dateEl = r.querySelector('.calendar__date');
                    if (dateEl && dateEl.innerText.trim()) {
                        lastDate = dateEl.innerText.trim().replace(/\\n+/g, ' ');
                    }
                    
                    const timeEl = r.querySelector('.calendar__time');
                    if (timeEl && timeEl.innerText.trim()) {
                        lastTime = timeEl.innerText.trim();
                    }
                    
                    const curEl = r.querySelector('.calendar__currency');
                    const titleEl = r.querySelector('.calendar__event span.calendar__event-title') || r.querySelector('.calendar__event');
                    const impactEl = r.querySelector('.calendar__impact span, .calendar__impact');
                    const actEl = r.querySelector('.calendar__actual');
                    const fctEl = r.querySelector('.calendar__forecast');
                    const prvEl = r.querySelector('.calendar__previous');
                    
                    if (curEl && curEl.innerText.trim()) {
                        let impact = 'Low Impact';
                        if (impactEl) {
                            const c = impactEl.className || '';
                            const innerSpan = impactEl.querySelector('span');
                            const spanCls = innerSpan ? innerSpan.className : '';
                            const combined = (c + ' ' + spanCls).toLowerCase();
                            
                            if (combined.includes('high') || combined.includes('red')) impact = 'High Impact';
                            else if (combined.includes('med') || combined.includes('medium') || combined.includes('ora')) impact = 'Medium Impact';
                            else if (combined.includes('low') || combined.includes('yel')) impact = 'Low Impact';
                            else if (combined.includes('non') || combined.includes('hol') || combined.includes('whi')) impact = 'Non-Economic';
                        }
                        
                        let outcome = 'Pending';
                        const actualVal = actEl ? actEl.innerText.trim() : '';
                        const forecastVal = fctEl ? fctEl.innerText.trim() : '';
                        
                        if (actualVal) {
                            outcome = 'Neutral';
                            const actSpan = actEl ? actEl.querySelector('span') : null;
                            if (actSpan) {
                                const sc = actSpan.className.toLowerCase();
                                if (sc.includes('better')) outcome = 'Better than Forecast';
                                else if (sc.includes('worse')) outcome = 'Worse than Forecast';
                            }
                            if (outcome === 'Neutral' && forecastVal) {
                                if (actualVal === forecastVal) outcome = 'As Expected';
                            }
                        }
                        
                        const eventTitle = titleEl ? titleEl.innerText.trim() : '';
                        const eventLinkEl = r.querySelector('.calendar__detail a, .calendar__event a');
                        const eventUrl = eventLinkEl ? eventLinkEl.href : '';
                        
                        events.push({
                            date: lastDate,
                            time: lastTime ? lastTime : 'All Day',
                            currency: curEl.innerText.trim(),
                            impact: impact,
                            event: eventTitle,
                            actual: actualVal,
                            forecast: forecastVal,
                            previous: prvEl ? prvEl.innerText.trim() : '',
                            outcome: outcome,
                            url: eventUrl
                        });
                    }
                });
                return events;
            })()
            """
            msg = {"id": 1, "method": "Runtime.evaluate", "params": {"expression": js_script, "returnByValue": True}}
            await ws.send(json.dumps(msg))
            resp = await ws.recv()
            data = json.loads(resp).get("result", {}).get("result", {}).get("value", [])
            log.info(f"CDP extracted {len(data)} calendar events.")
    except Exception as exc:
        log.error(f"CDP calendar extraction failed: {exc}")
    finally:
        if created and cal_tab:
            tab_id = cal_tab.get("id")
            log.info(f"[Tab Guard] Closing temporary calendar tab {tab_id}...")
            try:
                close_url = f"{CDP_BASE_URL}/json/close/{tab_id}"
                with urllib.request.urlopen(close_url, timeout=5) as resp:
                    pass
            except Exception:
                pass

    return data


# =====================================================================
# 3. FAIR ECONOMY JSON FALLBACK HARVESTER
# =====================================================================
def harvest_calendar_json_fallback() -> List[Dict[str, Any]]:
    """Fallback harvester using Fair Economy official JSON feed."""
    log.info(f"Fetching calendar from JSON fallback: {JSON_FALLBACK_URL}...")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Institutional-Quant-Engine/2.0"}
    req = urllib.request.Request(JSON_FALLBACK_URL, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            raw_events = json.loads(resp.read().decode())
    except Exception as exc:
        log.error(f"Fallback JSON harvest failed: {exc}")
        return []

    events = []
    for r in raw_events:
        dt_str = r.get("date", "")
        # Parse ISO datetime
        try:
            dt = datetime.datetime.fromisoformat(dt_str)
            date_str = dt.strftime("%a %b %d")
            time_str = dt.strftime("%I:%M%p").lower().lstrip("0")
        except Exception:
            date_str = dt_str[:10]
            time_str = ""

        impact_raw = r.get("impact", "Low")
        impact = f"{impact_raw} Impact" if "Impact" not in impact_raw else impact_raw

        actual = r.get("actual", "")
        forecast = r.get("forecast", "")
        previous = r.get("previous", "")

        outcome = "Pending" if not actual else ("As Expected" if actual == forecast else "Neutral")

        events.append({
            "date": date_str,
            "time": time_str if time_str else "All Day",
            "currency": r.get("country", "USD"),
            "impact": impact,
            "event": r.get("title", ""),
            "actual": actual,
            "forecast": forecast,
            "previous": previous,
            "outcome": outcome,
            "url": "https://www.forexfactory.com/calendar",
        })

    log.info(f"Fallback JSON harvested {len(events)} events.")
    return events


# =====================================================================
# 4. EXCEL WORKSHEET EXPORTER & STYLER
# =====================================================================
def export_calendar_to_parquet(events: list[dict], feed_name: str = SHEET_NAME) -> int:
    if not events:
        return 0
    meta = write_parquet_feed(feed_name, events)
    log.info(f"Successfully dumped {len(events)} calendar events into Parquet feed '{feed_name}': {meta.get('byte_size')} bytes.")
    return len(events)


def main():
    parser = argparse.ArgumentParser(description="Forex Factory Macro Calendar Pure-Parquet Dumper")
    parser.add_argument("--sheet-name", type=str, default=SHEET_NAME, help="Feed name (default: 19_Calendar)")
    args = parser.parse_args()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        events = loop.run_until_complete(harvest_calendar_cdp())
    finally:
        loop.close()

    if not events:
        log.warning("CDP calendar returned 0 events. Switching to Fair Economy JSON fallback...")
        events = harvest_calendar_json_fallback()

    if not events:
        log.error("Failed to harvest any calendar events from all sources. Aborting.")
        return 1

    written = export_calendar_to_parquet(events, feed_name=args.sheet_name)
    log.info(f"[SUCCESS] 19_Calendar completed successfully with {written} events.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
