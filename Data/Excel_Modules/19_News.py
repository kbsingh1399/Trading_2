#!/usr/bin/env python3
"""
Data/Excel_Modules/19_News.py
=============================
Forex Factory Live Institutional News & Breaking Stories Harvester.
Harvests live macro stories, central bank commentary, and economic news from:
  https://www.forexfactory.com/news

Extracted Columns:
  1. Sr.No
  2. Published Time (Raw)
  3. Timestamp (Approx UTC)
  4. Impact Level (High / Medium / Low / General)
  5. News Title
  6. Source Domain
  7. Story URL
  8. Comments Count
  9. Currency / Asset Attribution (USD, EUR, GBP, JPY, GOLD, etc.)
  10. Macro Category (Inflation, Central Banks, Growth, Yields, etc.)
  11. Story Preview / Key Snippet

Outputs:
  - Excel Worksheet: '19_News' positioned at Index 27 in Data/DataBase_Trading.xlsx
  - JSON Archive: Data/ForexFactory/19_News_Latest.json
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
log = logging.getLogger("19_News")

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
DEFAULT_EXCEL_PATH = ROOT_DIR / "Data" / "DataBase_Trading.xlsx"
DEFAULT_DATA_DIR = ROOT_DIR / "Data" / "ForexFactory"
NEWS_URL = "https://www.forexfactory.com/news"
SHEET_NAME = "19_News"
CDP_BASE_URL = "http://127.0.0.1:9222"


# =====================================================================
# 1. QUANTITATIVE TOPIC & CURRENCY ATTRIBUTION HEURISTICS
# =====================================================================
CURRENCY_KEYWORDS = {
    "USD": ["USD", "FED", "POWELL", "US ", "U.S.", "TREASURY", "DOLLAR", "WALL STREET", "AMERICAN"],
    "EUR": ["EUR", "ECB", "LAGARDE", "EURO", "GERMAN", "BUNDESBANK", "NAGEL", "FRANCE", "ITALY"],
    "GBP": ["GBP", "BOE", "BAILEY", "POUND", "STERLING", "UK ", "U.K.", "BRITISH", "ONS"],
    "JPY": ["JPY", "BOJ", "UEDA", "HIMINO", "YEN", "JAPAN", "TOKYO", "KANDA"],
    "AUD": ["AUD", "RBA", "BULLOCK", "AUSSIE", "AUSTRALIA"],
    "CAD": ["CAD", "BOC", "MACKLEM", "LOONIE", "CANADA"],
    "NZD": ["NZD", "RBNZ", "KIWI", "NEW ZEALAND"],
    "CHF": ["CHF", "SNB", "FRANC", "SWISS"],
    "CNY": ["CNY", "PBOC", "YUAN", "CHINA", "CHINESE", "BEIJING"],
    "GOLD": ["GOLD", "XAU", "BULLION", "PRECIOUS METALS"],
    "OIL": ["OIL", "CRUDE", "WTI", "BRENT", "OPEC", "ENERGY"],
    "CRYPTO": ["CRYPTO", "BITCOIN", "BTC", "ETHEREUM", "ETH", "BINANCE"],
}

CATEGORY_KEYWORDS = {
    "Inflation & CPI": ["INFLATION", "CPI", "PCE", "PPI", "PRICE INDEX", "LIVING COSTS"],
    "Central Banks & Rates": ["RATE", "FED", "ECB", "BOE", "BOJ", "HIKE", "CUT", "HAWKISH", "DOVISH", "POLICY", "CENTRAL BANK", "POWELL", "LAGARDE"],
    "Labor & Employment": ["JOBS", "PAYROLLS", "NFP", "UNEMPLOYMENT", "WAGES", "EMPLOYMENT", "LABOR"],
    "Growth & GDP": ["GDP", "GROWTH", "RECESSION", "EXPANSION", "PMI", "MANUFACTURING", "SERVICES"],
    "Bond Yields & Debt": ["YIELD", "BOND", "TREASURY", "DEBT", "DEFICIT", "FINANCES", "GILTS", "BUNDS"],
    "Housing & Real Estate": ["HOUSING", "HOME PRICES", "HPI", "MORTGAGE", "BUILDING", "REAL ESTATE"],
    "Trade & Geopolitics": ["TARIFF", "TRADE", "WAR", "SANCTIONS", "GEOPOLITICAL", "EXPORT", "IMPORT"],
}


def attribute_currency_and_category(title: str, snippet: str = "") -> Tuple[str, str]:
    """Infers relevant currency and economic category from text."""
    combined = f"{title} {snippet}".upper()

    # Match currency
    matched_cur = []
    for cur, kws in CURRENCY_KEYWORDS.items():
        for kw in kws:
            if re.search(r"\b" + re.escape(kw) + r"\b", combined):
                matched_cur.append(cur)
                break
    currency_tag = "/".join(matched_cur[:3]) if matched_cur else "GLOBAL"

    # Match category
    matched_cat = "General Market Intel"
    for cat, kws in CATEGORY_KEYWORDS.items():
        for kw in kws:
            if re.search(r"\b" + re.escape(kw) + r"\b", combined):
                matched_cat = cat
                break
        if matched_cat != "General Market Intel":
            break

    return currency_tag, matched_cat


def estimate_utc_timestamp(time_ago_str: str) -> str:
    """Estimates ISO UTC timestamp from relative time strings (e.g. '12 min ago')."""
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    raw = time_ago_str.lower().strip()

    try:
        if "min" in raw or "m ago" in raw:
            match = re.search(r"(\d+)", raw)
            mins = int(match.group(1)) if match else 5
            t = now_utc - datetime.timedelta(minutes=mins)
        elif "hr" in raw or "h ago" in raw or "hour" in raw:
            match = re.search(r"(\d+)\s*(?:hr|hour)", raw)
            hrs = int(match.group(1)) if match else 1
            min_match = re.search(r"(\d+)\s*min", raw)
            mins = int(min_match.group(1)) if min_match else 0
            t = now_utc - datetime.timedelta(hours=hrs, minutes=mins)
        elif "sec" in raw:
            t = now_utc
        else:
            t = now_utc
        return t.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return now_utc.strftime("%Y-%m-%d %H:%M:%S")


# =====================================================================
# 2. CHROME CDP SCRAPER WITH AUTOMATIC TAB HYGIENE
# =====================================================================
async def harvest_forex_factory_news_cdp() -> List[Dict[str, Any]]:
    """Extracts live news stories from Forex Factory using Chrome DevTools Protocol."""
    log.info(f"Connecting to Chrome CDP at {CDP_BASE_URL}...")
    try:
        with urllib.request.urlopen(f"{CDP_BASE_URL}/json", timeout=6) as resp:
            tabs = json.loads(resp.read().decode())
    except Exception as exc:
        log.error(f"Failed to connect to Chrome CDP: {exc}")
        return []

    news_tab = None
    created = False
    for t in tabs:
        if "forexfactory.com/news" in t.get("url", ""):
            news_tab = t
            log.info(f"Reusing existing Forex Factory News tab (ID: {t.get('id')})")
            break

    if not news_tab:
        log.info(f"Opening temporary news tab at {NEWS_URL}...")
        create_url = f"{CDP_BASE_URL}/json/new?{NEWS_URL}"
        req = urllib.request.Request(create_url, method="PUT")
        try:
            with urllib.request.urlopen(req, timeout=8) as resp:
                news_tab = json.loads(resp.read().decode())
            created = True
            await asyncio.sleep(4.0)
        except Exception as exc:
            log.error(f"Failed to create new CDP tab: {exc}")
            return []

    ws_url = news_tab.get("webSocketDebuggerUrl")
    if not ws_url:
        log.error("No webSocketDebuggerUrl found for tab")
        return []

    extracted_items = []
    try:
        async with websockets.connect(ws_url, max_size=10_000_000) as ws:
            # JavaScript evaluation extracting all story elements
            js_script = """
            (() => {
                const stories = [];
                // Look for all news items in the main news container
                document.querySelectorAll('.news-block__item, .hot-stories__item').forEach(item => {
                    const titleEl = item.querySelector('.news-block__title a, .news-block__title, .hot-stories__title a');
                    if (!titleEl) return;
                    const title = titleEl.innerText.trim();
                    if (!title || title.length < 5) return;
                    
                    const link = titleEl.getAttribute('href') || '';
                    const fullUrl = link.startsWith('http') ? link : ('https://www.forexfactory.com/' + link.replace(/^\\//, ''));
                    
                    // Determine impact from icon class / svg
                    let impact = 'Low Impact';
                    const iconEl = item.querySelector('[class*="impact-ff"], [class*="impact"], [class*="folder"], img.svg-img');
                    if (iconEl) {
                        const src = iconEl.getAttribute('src') || '';
                        const cls = iconEl.className || '';
                        if (src.includes('high') || cls.includes('high')) impact = 'High Impact';
                        else if (src.includes('med') || cls.includes('medium') || cls.includes('ora')) impact = 'Medium Impact';
                        else if (src.includes('low') || cls.includes('low') || cls.includes('yel')) impact = 'Low Impact';
                    }
                    
                    const detailsEl = item.querySelector('.news-block__details, .hot-stories__details');
                    let source = '';
                    let timeAgo = '';
                    let comments = '0 comments';
                    let exactTimeTitle = '';
                    
                    if (detailsEl) {
                        const srcLink = detailsEl.querySelector('a[href^="http"], a.darklink:not([href*="comments"])');
                        if (srcLink) source = srcLink.innerText.trim().replace(/^From\\s+/i, '');
                        
                        const commLink = detailsEl.querySelector('a[href*="comments"]');
                        if (commLink) comments = commLink.innerText.trim();
                        
                        const timeSpan = detailsEl.querySelector('span[title], span.nowrap');
                        if (timeSpan) {
                            timeAgo = timeSpan.innerText.trim();
                            exactTimeTitle = timeSpan.getAttribute('title') || '';
                        } else {
                            const raw = detailsEl.innerText;
                            const parts = raw.split('|').map(p => p.trim());
                            for (const p of parts) {
                                if (p.includes('ago') || p.includes('min') || p.includes('hr') || p.includes('sec')) {
                                    timeAgo = p;
                                    break;
                                }
                            }
                        }
                    }
                    
                    const prevEl = item.querySelector('.news-block__preview, .hot-stories__story');
                    const preview = prevEl ? prevEl.innerText.trim() : '';
                    
                    stories.push({
                        title: title,
                        url: fullUrl,
                        source: source,
                        time_ago: timeAgo,
                        exact_time_title: exactTimeTitle,
                        comments: comments,
                        impact: impact,
                        preview: preview
                    });
                });
                return stories;
            })()
            """
            msg = {"id": 1, "method": "Runtime.evaluate", "params": {"expression": js_script, "returnByValue": True}}
            await ws.send(json.dumps(msg))
            resp = await ws.recv()
            data = json.loads(resp)
            extracted_items = data.get("result", {}).get("result", {}).get("value", [])
            log.info(f"CDP extracted {len(extracted_items)} live stories from Forex Factory.")
    except Exception as exc:
        log.error(f"CDP interaction failed: {exc}")
    finally:
        # Close only the temporary tab if we created it, NEVER touch arena.ai
        if created and news_tab:
            tab_id = news_tab.get("id")
            log.info(f"[Tab Guard] Closing temporary tab {tab_id} while preserving other tabs...")
            try:
                close_url = f"{CDP_BASE_URL}/json/close/{tab_id}"
                with urllib.request.urlopen(close_url, timeout=5) as resp:
                    pass
            except Exception:
                pass

    # Process, deduplicate, and enrich extracted items
    unique_stories = []
    seen_titles = set()

    for item in extracted_items:
        title = item["title"]
        if title in seen_titles:
            continue
        seen_titles.add(title)

        time_ago = item.get("time_ago") or "Recently"
        utc_ts = estimate_utc_timestamp(time_ago)
        source = item.get("source") or "ForexFactory"
        cur_tag, cat_tag = attribute_currency_and_category(title, item.get("preview", ""))

        unique_stories.append({
            "title": title,
            "url": item["url"],
            "source": source,
            "time_ago": time_ago,
            "timestamp_utc": utc_ts,
            "exact_title_time": item.get("exact_time_title", ""),
            "impact": item.get("impact", "Low Impact"),
            "comments": item.get("comments", "0 comments"),
            "currency": cur_tag,
            "category": cat_tag,
            "preview": item.get("preview", ""),
        })

    return unique_stories


# =====================================================================
# 3. EXCEL WORKSHEET EXPORTER & STYLER
# =====================================================================
def export_news_to_excel(
    stories: List[Dict[str, Any]],
    excel_path: pathlib.Path = DEFAULT_EXCEL_PATH,
    sheet_name: str = SHEET_NAME,
) -> int:
    """Exports structured news into Data/DataBase_Trading.xlsx at Index 27."""
    if openpyxl is None:
        log.error("openpyxl is not installed. Skipping Excel export.")
        return 0

    if not excel_path.exists():
        log.error(f"Excel workbook not found at {excel_path}")
        return 0

    log.info(f"Loading workbook {excel_path.name} to write sheet '{sheet_name}'...")
    wb = openpyxl.load_workbook(excel_path)

    # Position at Index 27 (immediately following 18_CVD at Index 26)
    if sheet_name in wb.sheetnames:
        idx = wb.sheetnames.index(sheet_name)
        wb.remove(wb[sheet_name])
        ws = wb.create_sheet(title=sheet_name, index=idx)
    else:
        if "18_CVD" in wb.sheetnames:
            target_idx = wb.sheetnames.index("18_CVD") + 1
        elif "17_Orderbook" in wb.sheetnames:
            target_idx = wb.sheetnames.index("17_Orderbook") + 2
        else:
            target_idx = 27 if len(wb.sheetnames) >= 27 else len(wb.sheetnames)
        ws = wb.create_sheet(title=sheet_name, index=target_idx)

    final_idx = wb.sheetnames.index(sheet_name)
    log.info(f"Worksheet '{sheet_name}' positioned at index {final_idx}")

    # Typography & Styling
    hdr_font = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
    hdr_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")

    base_font = Font(name="Segoe UI", size=9, color="000000")
    bold_font = Font(name="Segoe UI", size=9, bold=True, color="000000")
    link_font = Font(name="Segoe UI", size=9, underline="single", color="0284C7")

    fill_high_impact = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
    fill_med_impact = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
    fill_low_impact = PatternFill(start_color="FEF9C3", end_color="FEF9C3", fill_type="solid")

    font_high = Font(name="Segoe UI", size=9, bold=True, color="991B1B")
    font_med = Font(name="Segoe UI", size=9, bold=True, color="92400E")
    font_low = Font(name="Segoe UI", size=9, bold=True, color="854D0E")

    currency_colors = {
        "USD": ("1E40AF", "DBEAFE"),  # Blue
        "EUR": ("1E293B", "F1F5F9"),  # Navy
        "GBP": ("6B21A8", "F3E8FF"),  # Purple
        "JPY": ("9F1239", "FFE4E6"),  # Rose
        "AUD": ("0F766E", "CCFBF1"),  # Teal
        "CAD": ("3730A3", "E0E7FF"),  # Indigo
        "GOLD": ("B45309", "FEF3C7"), # Gold
        "OIL": ("3F6212", "ECFCCB"),  # Olive
        "CRYPTO": ("0369A1", "E0F2FE"),# Sky
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
        "Published Time",
        "Timestamp (UTC)",
        "Impact Level",
        "Currency / Asset",
        "Macro Category",
        "News Story Title",
        "Source Domain",
        "Comments Count",
        "Story Summary / Key Preview",
        "Forex Factory URL",
    ]

    ws.row_dimensions[1].height = 26
    ws.append(headers)

    for col_idx in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=col_idx)
        cell.font = hdr_font
        cell.fill = hdr_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=False)

    for idx, s in enumerate(stories, start=1):
        ws.append([
            idx,
            s["time_ago"],
            s["timestamp_utc"],
            s["impact"],
            s["currency"],
            s["category"],
            s["title"],
            s["source"],
            s["comments"],
            s["preview"] if s["preview"] else s["title"],
            s["url"],
        ])

    for row_idx in range(2, len(stories) + 2):
        ws.row_dimensions[row_idx].height = 22

        # Alignments
        ws.cell(row=row_idx, column=1).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=2).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=3).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=4).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=5).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=6).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=7).alignment = Alignment(horizontal="left", vertical="center")
        ws.cell(row=row_idx, column=8).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=9).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=10).alignment = Alignment(horizontal="left", vertical="center")
        ws.cell(row=row_idx, column=11).alignment = Alignment(horizontal="left", vertical="center")

        # Impact highlight
        imp_cell = ws.cell(row=row_idx, column=4)
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

        # Currency badge
        cur_cell = ws.cell(row=row_idx, column=5)
        cur_val = str(cur_cell.value or "").split("/")[0]
        if cur_val in currency_colors:
            cfg, cbg = currency_colors[cur_val]
            cur_cell.font = Font(name="Segoe UI", size=8, bold=True, color=cfg)
            cur_cell.fill = PatternFill(start_color=cbg, end_color=cbg, fill_type="solid")

        # Title bold
        ws.cell(row=row_idx, column=7).font = bold_font

        # URL hyperlink
        url_cell = ws.cell(row=row_idx, column=11)
        url_val = str(url_cell.value or "")
        if url_val.startswith("http"):
            url_cell.hyperlink = url_val
            url_cell.font = link_font

        # Apply row borders
        for c_idx in range(1, len(headers) + 1):
            ws.cell(row=row_idx, column=c_idx).border = row_border

    # Column Widths
    col_widths = {
        "A": 8,   # Sr.No
        "B": 16,  # Published Time
        "C": 20,  # Timestamp UTC
        "D": 16,  # Impact Level
        "E": 18,  # Currency / Asset
        "F": 22,  # Macro Category
        "G": 55,  # News Story Title
        "H": 24,  # Source Domain
        "I": 16,  # Comments
        "J": 60,  # Story Summary
        "K": 40,  # Forex Factory URL
    }
    for col_let, w in col_widths.items():
        ws.column_dimensions[col_let].width = w

    # UI Polish
    ws.views.sheetView[0].showGridLines = True
    ws.auto_filter.ref = f"A1:K{len(stories) + 1}"
    ws.freeze_panes = "A2"

    import os, time
    temp_excel = excel_path.with_name(f"{excel_path.stem}_{os.getpid()}_{int(time.time()*1000)}.tmp.xlsx")
    wb.save(temp_excel)
    wb.close()
    import time, zipfile
    _is_valid = False
    with zipfile.ZipFile(temp_excel, "r") as _z:
        _is_valid = (_z.testzip() is None)
    if _is_valid:
        for _att in range(10):
            try:
                temp_excel.replace(excel_path)
                break
            except PermissionError:
                if _att == 9: raise
                time.sleep(0.5)
    else:
        if temp_excel.exists(): temp_excel.unlink()
        raise ValueError("Corrupt zip produced during export")
    log.info(f"Saved {len(stories)} stories to worksheet '{sheet_name}' in {excel_path.name}.")
    return len(stories)


# =====================================================================
# 4. JSON / DISK PERSISTENCE
# =====================================================================
def save_news_to_disk(
    stories: List[Dict[str, Any]],
    out_dir: pathlib.Path = DEFAULT_DATA_DIR,
) -> pathlib.Path:
    """Saves news archive to Data/ForexFactory/19_News_Latest.json."""
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "19_News_Latest.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(stories, f, indent=2, ensure_ascii=False)
    log.info(f"Archived news stories to {json_path}")
    return json_path


# =====================================================================
# 5. MAIN ENTRYPOINT
# =====================================================================
def main() -> int:
    parser = argparse.ArgumentParser(
        description="19_News: Forex Factory Live Institutional News & Breaking Stories Harvester"
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
        help="Excel sheet name (default: 19_News)",
    )
    args = parser.parse_args()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        stories = loop.run_until_complete(harvest_forex_factory_news_cdp())
    finally:
        loop.close()

    if not stories:
        log.error("Failed to harvest any stories from Forex Factory News.")
        return 1

    save_news_to_disk(stories)
    written = export_news_to_excel(stories, excel_path=args.excel_path, sheet_name=args.sheet_name)
    log.info(f"[SUCCESS] 19_News completed successfully with {written} stories.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
