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
  - Excel Worksheet: '19_News' positioned at Index 27 in Data/feeds/<feed_name>.parquet
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
log = logging.getLogger("19_News")

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
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
        try:
            utc_dt = datetime.datetime.strptime(utc_ts, "%Y-%m-%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc)
            ist_tz = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
            ist_ts = utc_dt.astimezone(ist_tz).strftime("%Y-%m-%d %H:%M:%S IST")
        except Exception:
            ist_ts = f"{utc_ts} IST" 
        source = item.get("source") or "ForexFactory"
        cur_tag, cat_tag = attribute_currency_and_category(title, item.get("preview", ""))

        unique_stories.append({
            "title": title,
            "url": item["url"],
            "source": source,
            "time_ago": time_ago,
            "timestamp_utc": utc_ts,
            "timestamp_ist": ist_ts,
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
def export_news_to_parquet(stories: list[dict], feed_name: str = SHEET_NAME) -> int:
    if not stories:
        return 0
    meta = write_parquet_feed(feed_name, stories)
    log.info(f"Successfully dumped {len(stories)} stories into Parquet feed '{feed_name}': {meta.get('byte_size')} bytes.")
    return len(stories)


def main():
    parser = argparse.ArgumentParser(description="Forex Factory News Pure-Parquet Dumper")
    parser.add_argument("--sheet-name", type=str, default=SHEET_NAME, help="Feed name (default: 19_News)")
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

    written = export_news_to_parquet(stories, feed_name=args.sheet_name)
    log.info(f"[SUCCESS] 19_News completed successfully with {written} stories.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
