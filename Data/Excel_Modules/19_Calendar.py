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
  - Excel Worksheet: '19_Calendar' positioned at Index 28 in Data/DataBase_Trading.xlsx
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

try:
    import openpyxl
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    openpyxl = None

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("19_Calendar")

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
DEFAULT_EXCEL_PATH = ROOT_DIR / "Data" / "DataBase_Trading.xlsx"
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
def export_calendar_to_excel(
    events: List[Dict[str, Any]],
    excel_path: pathlib.Path = DEFAULT_EXCEL_PATH,
    sheet_name: str = SHEET_NAME,
) -> int:
    """Exports economic calendar to Data/DataBase_Trading.xlsx at Index 28."""
    if openpyxl is None:
        log.error("openpyxl is not installed. Skipping Excel export.")
        return 0

    if not excel_path.exists():
        log.error(f"Excel workbook not found at {excel_path}")
        return 0

    log.info(f"Loading workbook {excel_path.name} to write sheet '{sheet_name}'...")
    wb = openpyxl.load_workbook(excel_path)

    # Position at Index 28 (immediately following 19_News at Index 27)
    if sheet_name in wb.sheetnames:
        idx = wb.sheetnames.index(sheet_name)
        wb.remove(wb[sheet_name])
        ws = wb.create_sheet(title=sheet_name, index=idx)
    else:
        if "19_News" in wb.sheetnames:
            target_idx = wb.sheetnames.index("19_News") + 1
        elif "18_CVD" in wb.sheetnames:
            target_idx = wb.sheetnames.index("18_CVD") + 2
        else:
            target_idx = 28 if len(wb.sheetnames) >= 28 else len(wb.sheetnames)
        ws = wb.create_sheet(title=sheet_name, index=target_idx)

    final_idx = wb.sheetnames.index(sheet_name)
    log.info(f"Target worksheet '{sheet_name}' positioned at index {final_idx}")

    # Typography & Styling
    hdr_font = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
    hdr_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")

    base_font = Font(name="Segoe UI", size=9, color="000000")
    bold_font = Font(name="Segoe UI", size=9, bold=True, color="000000")
    link_font = Font(name="Segoe UI", size=9, underline="single", color="0284C7")

    fill_high_impact = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
    fill_med_impact = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
    fill_low_impact = PatternFill(start_color="FEF9C3", end_color="FEF9C3", fill_type="solid")
    fill_better = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")
    fill_worse = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")

    font_high = Font(name="Segoe UI", size=9, bold=True, color="991B1B")
    font_med = Font(name="Segoe UI", size=9, bold=True, color="92400E")
    font_low = Font(name="Segoe UI", size=9, bold=True, color="854D0E")
    font_better = Font(name="Segoe UI", size=9, bold=True, color="166534")
    font_worse = Font(name="Segoe UI", size=9, bold=True, color="991B1B")

    currency_colors = {
        "USD": ("1E40AF", "DBEAFE"),  # Blue
        "EUR": ("1E293B", "F1F5F9"),  # Navy
        "GBP": ("6B21A8", "F3E8FF"),  # Purple
        "JPY": ("9F1239", "FFE4E6"),  # Rose
        "AUD": ("0F766E", "CCFBF1"),  # Teal
        "CAD": ("3730A3", "E0E7FF"),  # Indigo
        "NZD": ("065F46", "D1FAE5"),  # Emerald
        "CHF": ("991B1B", "FEE2E2"),  # Red
        "CNY": ("92400E", "FEF3C7"),  # Amber
    }

    thin_border_side = Side(border_style="thin", color="E2E8F0")
    row_border = Border(
        left=thin_border_side,
        right=thin_border_side,
        top=thin_border_side,
        bottom=thin_border_side,
    )

    headers = [
        "Sr.No",
        "Date",
        "Time",
        "Currency",
        "Impact Tier",
        "Economic Event Title",
        "Actual",
        "Forecast",
        "Previous",
        "Surprise / Outcome",
        "Directional Bias",
        "Event URL",
    ]

    ws.row_dimensions[1].height = 26
    ws.append(headers)

    for col_idx in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=col_idx)
        cell.font = hdr_font
        cell.fill = hdr_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=False)

    for idx, e in enumerate(events, start=1):
        outcome = e.get("outcome", "Pending")
        bias = infer_market_bias(e["event"], outcome)

        ws.append([
            idx,
            e["date"],
            e["time"],
            e["currency"],
            e["impact"],
            e["event"],
            e["actual"],
            e["forecast"],
            e["previous"],
            outcome,
            bias,
            e["url"],
        ])

    for row_idx in range(2, len(events) + 2):
        ws.row_dimensions[row_idx].height = 21

        # Alignments
        ws.cell(row=row_idx, column=1).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=2).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=3).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=4).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=5).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=6).alignment = Alignment(horizontal="left", vertical="center")
        ws.cell(row=row_idx, column=7).alignment = Alignment(horizontal="right", vertical="center")
        ws.cell(row=row_idx, column=8).alignment = Alignment(horizontal="right", vertical="center")
        ws.cell(row=row_idx, column=9).alignment = Alignment(horizontal="right", vertical="center")
        ws.cell(row=row_idx, column=10).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=11).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=12).alignment = Alignment(horizontal="left", vertical="center")

        # Currency badge
        cur_cell = ws.cell(row=row_idx, column=4)
        cur_val = str(cur_cell.value or "")
        if cur_val in currency_colors:
            cfg, cbg = currency_colors[cur_val]
            cur_cell.font = Font(name="Segoe UI", size=8, bold=True, color=cfg)
            cur_cell.fill = PatternFill(start_color=cbg, end_color=cbg, fill_type="solid")

        # Impact highlight
        imp_cell = ws.cell(row=row_idx, column=5)
        imp_val = str(imp_cell.value or "")
        if "High" in imp_val:
            imp_cell.fill = fill_high_impact
            imp_cell.font = font_high
        elif "Medium" in imp_val:
            imp_cell.fill = fill_med_impact
            imp_cell.font = font_med
        else:
            imp_cell.fill = fill_low_impact
            imp_cell.font = font_low

        # Event title bold
        ws.cell(row=row_idx, column=6).font = bold_font

        # Outcome highlight
        out_cell = ws.cell(row=row_idx, column=10)
        out_val = str(out_cell.value or "")
        if "Better" in out_val:
            out_cell.fill = fill_better
            out_cell.font = font_better
            ws.cell(row=row_idx, column=7).font = font_better
        elif "Worse" in out_val:
            out_cell.fill = fill_worse
            out_cell.font = font_worse
            ws.cell(row=row_idx, column=7).font = font_worse

        # Event URL hyperlink
        url_cell = ws.cell(row=row_idx, column=12)
        url_val = str(url_cell.value or "")
        if url_val.startswith("http"):
            url_cell.hyperlink = url_val
            url_cell.font = link_font

        # Apply borders
        for c_idx in range(1, len(headers) + 1):
            ws.cell(row=row_idx, column=c_idx).border = row_border

    # Column Widths
    col_widths = {
        "A": 8,   # Sr.No
        "B": 16,  # Date
        "C": 12,  # Time
        "D": 12,  # Currency
        "E": 16,  # Impact
        "F": 42,  # Event Title
        "G": 14,  # Actual
        "H": 14,  # Forecast
        "I": 14,  # Previous
        "J": 24,  # Surprise / Outcome
        "K": 26,  # Directional Bias
        "L": 35,  # Event URL
    }
    for col_let, w in col_widths.items():
        ws.column_dimensions[col_let].width = w

    # UI Polish
    ws.views.sheetView[0].showGridLines = True
    ws.auto_filter.ref = f"A1:L{len(events) + 1}"
    ws.freeze_panes = "A2"

    import os, time
        # Enforce Operator Invariant: Stamp Tier-1 Completion Banner ONLY ONCE row data is filled
    if ws.max_row > 1:
        try:
            from logger_config import stamp_sheet_completion_ist
            ws.insert_rows(1)
            stamp_sheet_completion_ist(
                ws=ws,
                sheet_title="19_Calendar",
                row_count=ws.max_row - 2,
                banner_cell="A1",
                status="LIVE",
                merge_max_col=ws.max_column
            )
            ws.freeze_panes = "A3"
        except Exception as _e:
            pass

    temp_excel = excel_path.with_name(f"{excel_path.stem}_{os.getpid()}_{int(time.time()*1000)}.tmp.xlsx")
    wb.save(temp_excel)
    wb.close()
    import time, zipfile
    _is_valid = False
    with zipfile.ZipFile(temp_excel, "r") as _z:
        _is_valid = (_z.testzip() is None)
    if _is_valid:
        for _att in range(30):
            try:
                temp_excel.replace(excel_path)
                break
            except PermissionError:
                if _att == 29: raise
                time.sleep(1.0)
    else:
        if temp_excel.exists(): temp_excel.unlink()
        raise ValueError("Corrupt zip produced during export")
    log.info(f"Saved {len(events)} events to worksheet '{sheet_name}' in {excel_path.name}.")
    return len(events)


# =====================================================================
# 5. JSON DISK ARCHIVE
# =====================================================================
def save_calendar_to_disk(
    events: List[Dict[str, Any]],
    out_dir: pathlib.Path = DEFAULT_DATA_DIR,
) -> pathlib.Path:
    """Saves calendar events to Data/ForexFactory/19_Calendar_ThisWeek.json."""
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "19_Calendar_ThisWeek.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=2, ensure_ascii=False)
    log.info(f"Archived calendar events to {json_path}")
    return json_path


# =====================================================================
# 6. MAIN ENTRYPOINT
# =====================================================================
def main() -> int:
    parser = argparse.ArgumentParser(
        description="19_Calendar: Forex Factory Live Institutional Macroeconomic Calendar Harvester"
    )
    parser.add_argument(
        "--excel-path",
        type=pathlib.Path,
        default=DEFAULT_EXCEL_PATH,
        help="Path to Data/DataBase_Trading.xlsx",
    )
    parser.add_argument(
        "--sheet-name",
        type=str,
        default=SHEET_NAME,
        help="Excel sheet name (default: 19_Calendar)",
    )
    args = parser.parse_args()

    # 1. Harvest via Chrome CDP
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        events = loop.run_until_complete(harvest_calendar_cdp())
    finally:
        loop.close()

    # 2. If CDP failed or returned empty, use Fair Economy JSON fallback
    if not events:
        log.warning("CDP calendar returned 0 events. Switching to Fair Economy JSON fallback...")
        events = harvest_calendar_json_fallback()

    if not events:
        log.error("Failed to harvest any calendar events from all sources. Aborting.")
        return 1

    # save_calendar_to_disk(events) - Direct to Excel only
    written = export_calendar_to_excel(events, excel_path=args.excel_path, sheet_name=args.sheet_name)
    log.info(f"[SUCCESS] 19_Calendar completed successfully with {written} events.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
