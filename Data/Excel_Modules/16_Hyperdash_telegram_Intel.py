#!/usr/bin/env python3
"""
Data/Excel_Modules/16_Hyperdash_telegram_Intel.py
=================================================
Hyperdash Telegram Flow Intelligence & Whale Activity Harvester (100% API).
Harvests real-time institutional orderflow alerts from Hyperdash Flows (@hyperdashflows)
via Telegram Web HTTP API endpoints and native archive synchronization without browser overhead,
parses alerts into structured quantitative events, and writes them into worksheet
'16_Hyperdash_telegram_Intel' in Data/DataBase_Trading.xlsx (positioned immediately after '15_Hyperdash_Stops_Map').

Extracted Event Categories:
  1. CONFIRMED LIQUIDATIONS: Realized short/long liquidations with liquidation price and notional.
  2. IMMINENT LIQUIDATION HAZARDS: Near-threshold liquidation risks <= 1.5% away.
  3. INSTITUTIONAL TWAPS: Active institutional TWAPs, execution durations, and $/min fill rates.
  4. WHALE EXECUTIONS & TRADES: Spot and perpetual whale market orders.
  5. POSITION CLOSES & PnL: Whale take-profit and stop-loss closes with realized profit ($).
  6. OPEN INTEREST SURGES: 5m OI expansions/contractions and surge multiples (x avg).
  7. VOLUME SURGES: 5m taker volume surges and buy/sell delta imbalances.
  8. COLLATERAL MOVEMENTS: Large USDC deposits, withdrawals, and bridge flows.
  9. STAKING FLOWS: Large HYPE token staking and unstaking alerts.
  10. MARKET INTEL & ANNOUNCEMENTS: Protocol notices, research notes, and market updates.
"""

from __future__ import annotations

import argparse
import datetime
import html
import json
import logging
import math
import os
import pathlib
import re
import sys
import time
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

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
log = logging.getLogger("16_Hyperdash_telegram_Intel")

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
DEFAULT_EXCEL_PATH = ROOT_DIR / "Data" / "DataBase_Trading.xlsx"
HIST_ARCHIVE_PATH = ROOT_DIR / "Data" / "Hyperdash_Flows" / "hyperdash_flows_history.json"
SHEET_NAME = "16_Hyperdash_telegram_Intel"
TELEGRAM_CHANNEL_URL = "https://t.me/s/hyperdashflows"

COLUMNS_DEF = [
    ("sr_no", "Sr.No", 8, "center"),
    ("timestamp_utc", "Time (UTC)", 20, "center"),
    ("post_id", "Post ID", 18, "center"),
    ("category", "Category", 18, "center"),
    ("event_type", "Event Type", 22, "center"),
    ("asset", "Asset", 12, "center"),
    ("side", "Side", 14, "center"),
    ("notional_usd", "Notional (USD)", 18, "right"),
    ("price", "Price ($)", 16, "right"),
    ("distance_or_metric", "Distance / Metric", 18, "center"),
    ("market_impact", "Market Impact", 24, "center"),
    ("duration_rate", "Duration / Rate", 20, "center"),
    ("wallet_address", "Wallet Address", 44, "left"),
    ("raw_text", "Telegram Alert Text", 75, "left"),
]


def clean_num(val_str: str, unit: str = "") -> float:
    """Parse string representations of numbers with unit multipliers (K, M, B)."""
    cleaned = str(val_str).replace(",", "").strip()
    mult = {"K": 1e3, "M": 1e6, "B": 1e9}.get(unit.upper(), 1.0)
    try:
        return float(cleaned) * mult
    except (ValueError, TypeError):
        return 0.0


def format_price(px: Optional[float]) -> str:
    """Format price with appropriate decimal precision."""
    if px is None or not math.isfinite(px):
        return "-"
    if px >= 1.0:
        return f"${px:,.2f}"
    return f"${px:,.4f}"


def format_notional(amt: Optional[float]) -> str:
    """Format USD notional value."""
    if amt is None or not math.isfinite(amt) or amt == 0.0:
        return "-"
    return f"${amt:,.2f}"


def parse_flow_message(raw_text: str, links: list) -> dict:
    """Parse raw Telegram alert text into structured quant features."""
    cleaned = raw_text.replace("\ueb1f", "").replace("\u200b", "").strip()
    norm_text = re.sub(r'#xyz\s*:', '#xyz:', cleaned)
    
    # Extract wallet address and asset slug from links
    wallet_address = None
    asset_slug = None
    for link in links:
        href = link.get("href", "")
        if "/address/0x" in href:
            match = re.search(r"address/(0x[a-fA-F0-9]{40})", href)
            if match:
                wallet_address = match.group(1).lower()
        elif "/asset/" in href:
            match = re.search(r"asset/([A-Za-z0-9_:#]+)", href)
            if match:
                asset_slug = match.group(1)

    # 1. TWAP Started
    twap_match = re.search(
        r"#([A-Za-z0-9_:#]+)\s+TWAP\s+Started:\s+(Buy|Sell)\s+\$([\d,\.]+)([KMBkmb]?)\s+over\s+([\d,\.]+)h\s+\(\$([\d,\.]+)([KMBkmb]?)/min\)",
        norm_text, re.IGNORECASE
    )
    if twap_match:
        coin = twap_match.group(1).split(":")[-1].upper()
        side = twap_match.group(2).upper()
        total_usd = clean_num(twap_match.group(3), twap_match.group(4))
        dur_h = float(twap_match.group(5).replace(",", ""))
        rate = clean_num(twap_match.group(6), twap_match.group(7))
        return {
            "category": "TWAP",
            "event_type": f"TWAP_{side}",
            "asset": coin,
            "side": side,
            "notional_usd": total_usd,
            "price": None,
            "distance_or_metric": f"{dur_h:g}h duration",
            "market_impact": "PASSIVE_ACCUMULATION" if side == "BUY" else "PASSIVE_DISTRIBUTION",
            "duration_rate": f"${rate:,.0f}/min ({dur_h:g}h)",
            "wallet_address": wallet_address,
            "raw_text": cleaned
        }

    # 2. Imminent Liquidation
    imminent_match = re.search(
        r"#([A-Za-z0-9_:#]+)\s+Imminent\s+(Short|Long)\s+Liquidation:\s+\$([\d,\.]+)([KMBkmb]?)\s+@\s+([\d,\.]+)%\s+away\s+\(liq:\s+\$([\d,\.]+)\)",
        norm_text, re.IGNORECASE
    )
    if imminent_match:
        coin = imminent_match.group(1).split(":")[-1].upper()
        pos_type = imminent_match.group(2).upper()
        total_usd = clean_num(imminent_match.group(3), imminent_match.group(4))
        dist_pct = float(imminent_match.group(5).replace(",", ""))
        liq_px = float(imminent_match.group(6).replace(",", ""))
        return {
            "category": "IMMINENT_LIQ",
            "event_type": f"IMMINENT_{pos_type}_LIQ",
            "asset": coin,
            "side": f"{pos_type}_RISK",
            "notional_usd": total_usd,
            "price": liq_px,
            "distance_or_metric": f"{dist_pct:+.1f}% away",
            "market_impact": "IMMINENT_BUY_CASCADE" if pos_type == "SHORT" else "IMMINENT_SELL_CASCADE",
            "duration_rate": "-",
            "wallet_address": wallet_address,
            "raw_text": cleaned
        }

    # 3. Confirmed Liquidation
    liq_match = re.search(
        r"#([A-Za-z0-9_:#]+)\s+Liquidated\s+(Short|Long):\s+\$([\d,\.]+)([KMBkmb]?)\s+at\s+\$([\d,\.]+)",
        norm_text, re.IGNORECASE
    )
    if liq_match:
        coin = liq_match.group(1).split(":")[-1].upper()
        pos_type = liq_match.group(2).upper()
        total_usd = clean_num(liq_match.group(3), liq_match.group(4))
        liq_px = float(liq_match.group(5).replace(",", ""))
        return {
            "category": "LIQUIDATION",
            "event_type": f"{pos_type}_LIQUIDATED",
            "asset": coin,
            "side": "SHORT" if pos_type == "SHORT" else "LONG",
            "notional_usd": total_usd,
            "price": liq_px,
            "distance_or_metric": "-",
            "market_impact": "BUY_PRESSURE" if pos_type == "SHORT" else "SELL_PRESSURE",
            "duration_rate": "-",
            "wallet_address": wallet_address,
            "raw_text": cleaned
        }

    # 4. Large Whale Execution / Trade
    trade_match = re.search(
        r"#([A-Za-z0-9_:#]+)\s+(Buy|Sell):\s+\$([\d,\.]+)([KMBkmb]?)\s+at\s+\$([\d,\.]+)",
        norm_text, re.IGNORECASE
    )
    if trade_match:
        coin = trade_match.group(1).split(":")[-1].upper()
        side = trade_match.group(2).upper()
        total_usd = clean_num(trade_match.group(3), trade_match.group(4))
        fill_px = float(trade_match.group(5).replace(",", ""))
        return {
            "category": "WHALE_TRADE",
            "event_type": f"WHALE_{side}",
            "asset": coin,
            "side": side,
            "notional_usd": total_usd,
            "price": fill_px,
            "distance_or_metric": "-",
            "market_impact": "BUY_PRESSURE" if side == "BUY" else "SELL_PRESSURE",
            "duration_rate": "-",
            "wallet_address": wallet_address,
            "raw_text": cleaned
        }

    # 5. Whale Position Close / PnL Realization
    close_match = re.search(
        r"#([A-Za-z0-9_:#]+)\s+trader\s+closed\s+\$([\d,\.]+)([KMBkmb]?)\s+(short|long),\s+realizing\s+([\+\-]?\$?[\d,\.]+)([KMBkmb]?)\s+profit",
        norm_text, re.IGNORECASE
    )
    if close_match:
        coin = close_match.group(1).split(":")[-1].upper()
        pos_type = close_match.group(4).upper()
        size_usd = clean_num(close_match.group(2), close_match.group(3))
        pnl_str = close_match.group(5).replace("$", "")
        pnl_mult = {"K": 1e3, "M": 1e6, "B": 1e9}.get(close_match.group(6).upper(), 1.0)
        pnl_usd = float(pnl_str.replace(",", "")) * pnl_mult
        return {
            "category": "POSITION_CLOSE",
            "event_type": f"CLOSED_{pos_type}",
            "asset": coin,
            "side": f"CLOSE_{pos_type}",
            "notional_usd": size_usd,
            "price": None,
            "distance_or_metric": f"PnL: {pnl_usd:+,.0f} USD",
            "market_impact": "BUY_COVER" if pos_type == "SHORT" else "SELL_COVER",
            "duration_rate": "-",
            "wallet_address": wallet_address,
            "raw_text": cleaned
        }

    # 6. Open Interest Surge
    oi_match = re.search(
        r"#([A-Za-z0-9_:#]+)\s+OI\s+Surge.*?([+\-]?)\$?([\d,\.]+)([KMBkmb]?)\s+in\s+(\w+)\s*([\d,\.]+)x\s+avg",
        norm_text, re.IGNORECASE | re.DOTALL
    )
    if oi_match:
        coin = oi_match.group(1).split(":")[-1].upper()
        sign = -1.0 if oi_match.group(2) == "-" else 1.0
        oi_delta = sign * clean_num(oi_match.group(3), oi_match.group(4))
        tf = oi_match.group(5)
        mult = float(oi_match.group(6).replace(",", ""))
        return {
            "category": "OI_SURGE",
            "event_type": "OI_SURGE",
            "asset": coin,
            "side": "OI_EXPANSION" if oi_delta > 0 else "OI_CONTRACTION",
            "notional_usd": abs(oi_delta),
            "price": None,
            "distance_or_metric": f"{mult:g}x avg in {tf}",
            "market_impact": f"{mult:g}x_AVG_SURGE",
            "duration_rate": f"Δ {oi_delta:+,.0f} USD",
            "wallet_address": wallet_address,
            "raw_text": cleaned
        }

    # 7. Volume Surge
    vol_match = re.search(
        r"#([A-Za-z0-9_:#]+)\s+(\d+m)\s+Volume\s+Surge.*?\$([\d,\.]+)([KMBkmb]?)\s+vs\s+\$([\d,\.]+)([KMBkmb]?)\s+avg.*?[Δ\u0394]\s*([+\-]?)\$?([\d,\.]+)([KMBkmb]?)\s+(buys|sells)",
        norm_text, re.IGNORECASE | re.DOTALL
    )
    if vol_match:
        coin = vol_match.group(1).split(":")[-1].upper()
        timeframe = vol_match.group(2)
        surge_vol = clean_num(vol_match.group(3), vol_match.group(4))
        delta_sign = -1.0 if vol_match.group(7) == "-" else 1.0
        delta_usd = delta_sign * clean_num(vol_match.group(8), vol_match.group(9))
        v_dir = vol_match.group(10).upper()
        return {
            "category": "VOLUME_SURGE",
            "event_type": "VOLUME_SURGE",
            "asset": coin,
            "side": f"{v_dir}_DOMINANT",
            "notional_usd": surge_vol,
            "price": None,
            "distance_or_metric": f"in {timeframe}",
            "market_impact": f"Δ {delta_usd:+,.0f} USD",
            "duration_rate": f"Delta {v_dir}",
            "wallet_address": wallet_address,
            "raw_text": cleaned
        }

    # 8. Large Deposits & Withdrawals
    dep_match = re.search(r"Large\s+Deposit\s*-\s*\$([\d,\.]+)([KMBkmb]?)", norm_text, re.IGNORECASE)
    if dep_match:
        tot_usd = clean_num(dep_match.group(1), dep_match.group(2))
        return {
            "category": "COLLATERAL",
            "event_type": "LARGE_DEPOSIT",
            "asset": "USDC",
            "side": "INFLOW",
            "notional_usd": tot_usd,
            "price": None,
            "distance_or_metric": "Collateral Inflow",
            "market_impact": "COLLATERAL_INJECTION",
            "duration_rate": "-",
            "wallet_address": wallet_address,
            "raw_text": cleaned
        }

    with_match = re.search(r"Large\s+Withdrawal\s*-\s*\$([\d,\.]+)([KMBkmb]?)", norm_text, re.IGNORECASE)
    if with_match:
        tot_usd = clean_num(with_match.group(1), with_match.group(2))
        return {
            "category": "COLLATERAL",
            "event_type": "LARGE_WITHDRAWAL",
            "asset": "USDC",
            "side": "OUTFLOW",
            "notional_usd": tot_usd,
            "price": None,
            "distance_or_metric": "Collateral Outflow",
            "market_impact": "COLLATERAL_DRAIN",
            "duration_rate": "-",
            "wallet_address": wallet_address,
            "raw_text": cleaned
        }

    # 9. Staking / Unstaking
    stake_match = re.search(
        r"Large\s+([A-Za-z0-9]+)\s+(Unstake\s+Initiated|Unstake\s+Finalized|Staked).*?\$([\d,\.]+)([KMBkmb]?)\)",
        norm_text, re.IGNORECASE | re.DOTALL
    )
    if stake_match:
        c_name = stake_match.group(1).upper()
        act = stake_match.group(2).upper().replace(" ", "_")
        tot_usd = clean_num(stake_match.group(3), stake_match.group(4))
        return {
            "category": "STAKING",
            "event_type": f"STAKING_{act}",
            "asset": c_name,
            "side": act,
            "notional_usd": tot_usd,
            "price": None,
            "distance_or_metric": act,
            "market_impact": "SUPPLY_LOCK" if "STAKED" in act else "SUPPLY_UNLOCK",
            "duration_rate": "-",
            "wallet_address": wallet_address,
            "raw_text": cleaned
        }

    # 10. General Flow / Market Intel
    return {
        "category": "MARKET_INTEL",
        "event_type": "ANNOUNCEMENT",
        "asset": asset_slug or "GENERAL",
        "side": "INFO",
        "notional_usd": None,
        "price": None,
        "distance_or_metric": "-",
        "market_impact": "NEWS_INTEL",
        "duration_rate": "-",
        "wallet_address": wallet_address,
        "raw_text": cleaned
    }


def fetch_telegram_channel_messages(max_pages: int = 25) -> List[Dict[str, Any]]:
    """Fetches real-time alert messages via Telegram channel web preview API."""
    all_raw_posts = []
    before_cursor = ""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    log.info(f"Connecting to Telegram channel API ({TELEGRAM_CHANNEL_URL}) across {max_pages} pages...")

    for page in range(max_pages):
        url = f"{TELEGRAM_CHANNEL_URL}{before_cursor}"
        content = None
        for attempt in range(2):
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=12) as resp:
                    content = resp.read().decode("utf-8")
                break
            except Exception as exc:
                if attempt == 1:
                    log.warning(f"Failed fetching page {page} ({url}): {exc}")
                time.sleep(0.5)

        if not content:
            break

        if BeautifulSoup is not None:
            soup = BeautifulSoup(content, "html.parser")
            wraps = soup.find_all("div", class_=re.compile(r"tgme_widget_message_wrap"))
            if not wraps:
                break

            first_post_id = None
            for wrap in wraps:
                msg = wrap.find("div", class_="tgme_widget_message")
                if not msg:
                    continue
                p_id = msg.get("data-post")
                if not first_post_id and p_id:
                    first_post_id = p_id.split("/")[-1]

                time_tag = msg.find("time", class_="time")
                dt_iso = time_tag.get("datetime") if time_tag else datetime.datetime.now(datetime.timezone.utc).isoformat()

                text_div = msg.find("div", class_="tgme_widget_message_text")
                if not text_div:
                    continue

                links = [{"text": a.text.strip(), "href": a.get("href", "")} for a in text_div.find_all("a")]
                clean_text = re.sub(r"\s+", " ", text_div.get_text(separator=" ")).strip()

                parsed = parse_flow_message(clean_text, links)
                parsed["post_id"] = p_id
                parsed["timestamp_utc"] = dt_iso.replace("T", " ").split("+")[0]
                parsed["source"] = "TELEGRAM_WEB_API"
                all_raw_posts.append(parsed)

            if first_post_id:
                before_cursor = f"?before={first_post_id}"
            else:
                break
        else:
            # Fallback simple extractor if bs4 not present
            raw_posts = re.findall(r'data-post="([^"]+)"', content)
            if not raw_posts:
                break
            first_post_id = raw_posts[0].split("/")[-1]
            before_cursor = f"?before={first_post_id}"

        time.sleep(0.15)  # Jitter

    log.info(f"Harvested {len(all_raw_posts)} live Telegram alerts across {max_pages} pages.")
    return all_raw_posts


def load_and_merge_archive(live_records: List[Dict[str, Any]], max_limit: int = 1500) -> List[Dict[str, Any]]:
    """Merges live Telegram API events with historical JSON flow archive."""
    merged_map: Dict[str, Dict[str, Any]] = {}

    # 1. First load historical archive if present
    if HIST_ARCHIVE_PATH.exists():
        try:
            with open(HIST_ARCHIVE_PATH, "r", encoding="utf-8") as f:
                hist_data = json.load(f)
            log.info(f"Loaded {len(hist_data)} historical archive records from {HIST_ARCHIVE_PATH}")
            for h in hist_data:
                msg_id = str(h.get("msg_id", ""))
                t_sec = h.get("timestamp_epoch")
                if t_sec:
                    dt_str = datetime.datetime.fromtimestamp(t_sec, tz=datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
                else:
                    dt_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

                raw_t = h.get("raw_text", "")
                parsed = parse_flow_message(raw_t, [])
                parsed["post_id"] = msg_id
                parsed["timestamp_utc"] = dt_str
                parsed["source"] = h.get("source", "HYPERDASH_ARCHIVE")
                # Inherit original fields if available
                if h.get("coin"): parsed["asset"] = str(h.get("coin")).upper()
                if h.get("notional_usd"): parsed["notional_usd"] = float(h.get("notional_usd"))
                if h.get("price"): parsed["price"] = float(h.get("price"))
                if h.get("wallet_address"): parsed["wallet_address"] = h.get("wallet_address")
                
                merged_map[msg_id] = parsed
        except Exception as exc:
            log.warning(f"Could not read historical archive: {exc}")

    # 2. Layer live Telegram alerts over archive
    for lr in live_records:
        pid = lr.get("post_id") or lr.get("raw_text", "")[:30]
        merged_map[pid] = lr

    records = list(merged_map.values())
    # Sort descending by timestamp
    records.sort(key=lambda r: r.get("timestamp_utc", ""), reverse=True)

    if max_limit > 0:
        records = records[:max_limit]

    # Assign Sr.No
    for idx, r in enumerate(records, start=1):
        r["sr_no"] = idx

    log.info(f"Total merged & structured Telegram intel records: {len(records)} events.")
    return records


def dump_to_excel(records: List[Dict[str, Any]], excel_path: pathlib.Path = DEFAULT_EXCEL_PATH) -> bool:
    """Dumps structured Telegram intel into worksheet '16_Hyperdash_telegram_Intel'."""
    if openpyxl is None:
        log.error("openpyxl library not installed.")
        return False

    if not excel_path.exists():
        log.error(f"Excel workbook not found at: {excel_path}")
        return False

    if not records:
        log.error("0 records to dump. Aborting to protect workbook integrity.")
        return False

    wb = openpyxl.load_workbook(excel_path)

    # Position immediately after 15_Hyperdash_Stops_Map (or Index 24)
    if SHEET_NAME in wb.sheetnames:
        idx = wb.sheetnames.index(SHEET_NAME)
        wb.remove(wb[SHEET_NAME])
        ws = wb.create_sheet(title=SHEET_NAME, index=idx)
    else:
        if "15_Hyperdash_Stops_Map" in wb.sheetnames:
            target_idx = wb.sheetnames.index("15_Hyperdash_Stops_Map") + 1
        else:
            target_idx = 24 if len(wb.sheetnames) >= 24 else len(wb.sheetnames)
        ws = wb.create_sheet(title=SHEET_NAME, index=target_idx)

    final_idx = wb.sheetnames.index(SHEET_NAME)
    log.info(f"Target worksheet '{SHEET_NAME}' positioned at index {final_idx}")

    # Typography & Styles
    hdr_font = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
    hdr_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")

    base_font = Font(name="Segoe UI", size=9, color="000000")
    bold_font = Font(name="Segoe UI", size=9, bold=True, color="000000")
    mono_font = Font(name="Consolas", size=9, color="475569")
    green_font = Font(name="Segoe UI", size=9, bold=True, color="00A86B")
    red_font = Font(name="Segoe UI", size=9, bold=True, color="E53935")
    amber_font = Font(name="Segoe UI", size=9, bold=True, color="D97706")
    subdued_font = Font(name="Segoe UI", size=9, color="64748B")

    thin_border_side = Side(border_style="thin", color="E2E8F0")
    row_border = Border(
        left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side
    )

    # 1. Header Row
    ws.row_dimensions[1].height = 26
    for col_idx, (col_key, header_title, width, align) in enumerate(COLUMNS_DEF, start=1):
        cell = ws.cell(row=1, column=col_idx, value=header_title)
        cell.font = hdr_font
        cell.fill = hdr_fill
        cell.alignment = Alignment(horizontal=align, vertical="center")
        cell.border = row_border
        col_letter = get_column_letter(col_idx)
        ws.column_dimensions[col_letter].width = width

    # 2. Data Rows
    for row_idx, r in enumerate(records, start=2):
        ws.row_dimensions[row_idx].height = 20
        cat = str(r.get("category", "")).upper()
        side_val = str(r.get("side", "")).upper()
        impact = str(r.get("market_impact", "")).upper()

        for col_idx, (col_key, _, _, align) in enumerate(COLUMNS_DEF, start=1):
            val = r.get(col_key, "")

            # Format numbers
            if col_key == "notional_usd":
                cell_val = format_notional(val) if isinstance(val, (int, float)) else str(val or "-")
            elif col_key == "price":
                cell_val = format_price(val) if isinstance(val, (int, float)) else str(val or "-")
            else:
                cell_val = val if val is not None else "-"

            cell = ws.cell(row=row_idx, column=col_idx, value=cell_val)
            cell.alignment = Alignment(horizontal=align, vertical="center")
            cell.border = row_border

            # Semantic Typography
            if col_key in ("sr_no", "asset"):
                cell.font = bold_font
            elif col_key == "category":
                if cat in ("LIQUIDATION", "IMMINENT_LIQ"):
                    cell.font = amber_font if cat == "IMMINENT_LIQ" else red_font
                elif cat in ("WHALE_TRADE", "TWAP"):
                    cell.font = green_font if "BUY" in side_val else red_font
                elif cat == "COLLATERAL":
                    cell.font = green_font if "INFLOW" in side_val else red_font
                else:
                    cell.font = bold_font
            elif col_key in ("side", "market_impact"):
                if any(k in cell_val.upper() for k in ("BUY", "INFLOW", "SHORT_LIQUIDATED", "SUPPLY_LOCK", "COVER")):
                    cell.font = green_font
                elif any(k in cell_val.upper() for k in ("SELL", "OUTFLOW", "LONG_LIQUIDATED", "SUPPLY_UNLOCK", "CASCADE")):
                    cell.font = red_font
                elif "RISK" in cell_val.upper() or "SURGE" in cell_val.upper():
                    cell.font = amber_font
                else:
                    cell.font = base_font
            elif col_key == "notional_usd":
                cell.font = bold_font
            elif col_key == "wallet_address":
                cell.font = mono_font
            elif col_key == "raw_text":
                cell.font = subdued_font
            else:
                cell.font = base_font

    ws.views.sheetView[0].showGridLines = True
    ws.freeze_panes = "A2"

    temp_excel = excel_path.with_suffix(".tmp.xlsx")
    wb.save(temp_excel)
    wb.close()
    import zipfile
    with zipfile.ZipFile(temp_excel, "r") as _z:
        if _z.testzip() is None:
            temp_excel.replace(excel_path)
        else:
            if temp_excel.exists(): temp_excel.unlink()
            raise ValueError("Corrupt zip produced during export")
    log.info(f"Successfully saved {len(records)} rows to '{SHEET_NAME}' at {excel_path}")
    return True


def main():
    parser = argparse.ArgumentParser(description="16_Hyperdash_telegram_Intel Harvester & Excel Dumper")
    parser.add_argument("--pages", type=int, default=30, help="Number of Telegram channel pages to fetch via API")
    parser.add_argument("--limit", type=int, default=1500, help="Max records to write to Excel worksheet")
    parser.add_argument("--excel-path", type=pathlib.Path, default=DEFAULT_EXCEL_PATH, help="Path to DataBase_Trading.xlsx")
    args = parser.parse_args()

    log.info(f"Starting Telegram Intel harvest (Pages: {args.pages}, Limit: {args.limit})")
    live_posts = fetch_telegram_channel_messages(max_pages=args.pages)
    records = load_and_merge_archive(live_posts, max_limit=args.limit)

    if not records:
        log.error("Harvesting yielded 0 records. Excel dump aborted.")
        sys.exit(1)

    success = dump_to_excel(records, excel_path=args.excel_path)
    if not success:
        sys.exit(1)

    log.info("16_Hyperdash_telegram_Intel pipeline executed successfully.")


if __name__ == "__main__":
    main()
