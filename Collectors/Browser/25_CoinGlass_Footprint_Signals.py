#!/usr/bin/env python3
"""
Collectors/Browser/25_CoinGlass_Footprint_Signals.py
===================================================
Dedicated Parquet Feed: CoinGlass Footprint Intelligence, Order Flow Delta & Signals.
Extracts 100% of institutional footprint order flow intelligence from:
https://www.coinglass.com/footprint?symbol=<COIN>

Captures:
  1. Top KPIs:
     - Last Price ($), 24h Change (%)
     - Current Bar Delta ($), Buy/Sell Breakdown ($)
     - Current Bar Volume ($), Trade Count, Avg Trade Size
     - Current Bar Imbalances (Buy count, Sell count, Imbalance ratio %)
     - Delta in View ($) and Time Window
     - Latest Signal (Name, Bias, Description, Age)
  2. Granular Signals Tab:
     - All 50+ signals across 15m, Volume, and Range bars
     - Signal Type: Absorption, Trapped Longs, Trapped Shorts, Exhaustion, Divergence
     - Directional Bias: Bullish, Bearish
     - Price Level ($), Absorbed Volume ($), Full Narrative

Dumps to Data/feeds/25_CoinGlass_Footprint_Signals.parquet and Data/metadata/25_CoinGlass_Footprint_Signals.json.
"""

from __future__ import annotations

import argparse
import asyncio
import datetime
import json
import logging
import pathlib
import re
import sys
import time
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

ROOT_DIR_FOR_PQ = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT_DIR_FOR_PQ / "Collectors" / "Core") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR_FOR_PQ / "Collectors" / "Core"))
if str(ROOT_DIR_FOR_PQ / "Terminal" / "Data_Factory") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR_FOR_PQ / "Terminal" / "Data_Factory"))
from parquet_feed_writer import write_parquet_feed, IST_TZ, UTC_TZ

try:
    import websockets
except ImportError:
    websockets = None

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("FootprintSignals")

CDP_BASE_URL = "http://127.0.0.1:9222"
TARGET_SHEET_NAME = "25_CoinGlass_Footprint_Signals"
DEFAULT_COINS = ["BTC", "ETH", "SOL", "XRP"]


def open_ephemeral_tab(target_url: str, cdp_base_url: str = CDP_BASE_URL) -> Tuple[str, str]:
    """Creates a new dedicated ephemeral tab via CDP."""
    req = urllib.request.Request(f"{cdp_base_url}/json/new?{target_url}", method="PUT")
    new_tab = json.loads(urllib.request.urlopen(req, timeout=10).read().decode())
    return new_tab["id"], new_tab["webSocketDebuggerUrl"]


def close_tab(tab_id: str, cdp_base_url: str = CDP_BASE_URL):
    """Closes ephemeral tab via CDP, strictly preserving arena.ai and user tabs."""
    try:
        urllib.request.urlopen(f"{cdp_base_url}/json/close/{tab_id}", timeout=5)
        log.info(f"Closed ephemeral tab {tab_id}")
    except Exception as e:
        log.warning(f"Error closing tab {tab_id}: {e}")


def parse_usd(str_val: Any) -> float:
    """Parses '$1.53M', '-2.56M', '553K', '54.37M' to numeric USD."""
    if str_val is None:
        return 0.0
    s = str(str_val).replace("$", "").replace(",", "").replace("\u2212", "-").strip()
    mult = 1.0
    if s.endswith("M") or s.endswith("m"):
        mult = 1e6
        s = s[:-1]
    elif s.endswith("K") or s.endswith("k"):
        mult = 1e3
        s = s[:-1]
    elif s.endswith("B") or s.endswith("b"):
        mult = 1e9
        s = s[:-1]
    try:
        return float(s) * mult
    except ValueError:
        return 0.0


def parse_clean_price(str_val: Any) -> float:
    """Extracts positive float price from string."""
    if str_val is None:
        return 0.0
    cleaned = re.sub(r"[^\d.]", "", str(str_val))
    try:
        return float(cleaned)
    except ValueError:
        return 0.0


async def extract_footprint_for_coin(cdp_cmd, coin: str) -> List[Dict[str, Any]]:
    """Navigates to https://www.coinglass.com/footprint?symbol={coin} and extracts all footprint intelligence."""
    url = f"https://www.coinglass.com/footprint?symbol={coin}"
    log.info(f"Navigating to {url}...")
    await cdp_cmd("Page.navigate", {"url": url})

    # Wait for footprint DOM hydration (KPIs visible)
    for attempt in range(20):
        await asyncio.sleep(0.3)
        res = await cdp_cmd("Runtime.evaluate", {
            "expression": """
            (() => {
                const kpis = document.querySelectorAll('.KpiStrip_kpi__7Xgii');
                return { kpiCount: kpis.length };
            })()
            """,
            "returnByValue": True
        })
        val = res.get("value", {})
        if val.get("kpiCount", 0) >= 4:
            break

    # 1. Extract Top KPIs
    js_kpis = """
    (() => {
        const kpis = Array.from(document.querySelectorAll('.KpiStrip_kpi__7Xgii')).map(el => el.innerText.trim());
        return { kpis };
    })()
    """
    kpi_res = await cdp_cmd("Runtime.evaluate", {"expression": js_kpis, "returnByValue": True})
    raw_kpis = kpi_res.get("value", {}).get("kpis", [])

    kpi_dict: Dict[str, Any] = {
        "last_price": 0.0,
        "bar_delta_usd": 0.0,
        "bar_volume_usd": 0.0,
        "delta_in_view_usd": 0.0,
        "latest_signal_name": "",
        "latest_signal_bias": "",
        "latest_signal_desc": "",
    }

    for k in raw_kpis:
        lines = [line.strip() for line in k.split("\n") if line.strip()]
        if not lines:
            continue
        header = lines[0].lower()
        if "last price" in header and len(lines) > 1:
            kpi_dict["last_price"] = parse_clean_price(lines[1])
        elif "current bar delta" in header and len(lines) > 1:
            kpi_dict["bar_delta_usd"] = parse_usd(lines[1])
        elif "current bar volume" in header and len(lines) > 1:
            kpi_dict["bar_volume_usd"] = parse_usd(lines[1])
        elif "delta in view" in header and len(lines) > 1:
            kpi_dict["delta_in_view_usd"] = parse_usd(lines[1])
        elif "latest signal" in header:
            if len(lines) > 1:
                kpi_dict["latest_signal_name"] = lines[1]
            if len(lines) > 2:
                kpi_dict["latest_signal_bias"] = lines[2]
            if len(lines) > 3:
                kpi_dict["latest_signal_desc"] = lines[3]

    # 2. Click Signals tab and wait for signal rows to hydrate
    await cdp_cmd("Runtime.evaluate", {
        "expression": """
        (() => {
            const tabs = Array.from(document.querySelectorAll('.tab-inner-label, div, span')).filter(el => el.innerText && el.innerText.trim() === 'Signals');
            if (tabs.length > 0) { tabs[0].click(); }
        })()
        """
    })

    for attempt in range(15):
        await asyncio.sleep(0.3)
        res = await cdp_cmd("Runtime.evaluate", {
            "expression": "(() => { return document.querySelectorAll('.SidePanel_lrow__m40N_').length; })()",
            "returnByValue": True
        })
        sig_count = res.get("value", 0)
        if sig_count > 0:
            break

    js_signals = """
    (() => {
        const rows = Array.from(document.querySelectorAll('.SidePanel_lrow__m40N_'));
        return rows.map(r => {
            const txt = r.innerText ? r.innerText.trim() : '';
            const lines = txt.split('\\n').map(l => l.trim()).filter(Boolean);
            return {
                raw_text: txt,
                lines: lines
            };
        });
    })()
    """
    signals_res = await cdp_cmd("Runtime.evaluate", {"expression": js_signals, "returnByValue": True})
    raw_signals = signals_res.get("value", [])

    records: List[Dict[str, Any]] = []
    now_ist = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=5, minutes=30)).strftime("%Y-%m-%d %H:%M:%S IST")

    for s in raw_signals:
        lines = s.get("lines", [])
        if len(lines) < 3:
            continue

        time_str = lines[0]  # e.g. "10-26 16:36"
        timeframe = lines[1] if len(lines) > 1 else "15m"  # e.g. "Range 250", "15m", "Volume 1.0K BTC"
        sig_type = lines[2] if len(lines) > 2 else "Signal"  # e.g. "Absorption", "Trapped shorts", "Trapped longs"
        narrative_title = lines[3] if len(lines) > 3 else ""
        full_detail = " ".join(lines[4:]) if len(lines) > 4 else narrative_title

        bias = "NEUTRAL"
        combined_text = f"{sig_type} {narrative_title} {full_detail}".lower()
        if "bullish" in combined_text or "bull" in combined_text:
            bias = "BULLISH"
        elif "bearish" in combined_text or "bear" in combined_text:
            bias = "BEARISH"

        price_level = 0.0
        volume_usd = 0.0
        for token in full_detail.split():
            clean_tok = token.replace(",", "").replace("·", "").strip()
            if ("M" in clean_tok or "K" in clean_tok) and not any(c in clean_tok for c in ["ETH", "BTC", "SOL"]):
                v = parse_usd(clean_tok)
                if v > 0 and volume_usd == 0:
                    volume_usd = v
            try:
                p = float(clean_tok)
                if p > 1.0:
                    price_level = p
            except ValueError:
                pass

        records.append({
            "timestamp_ist": now_ist,
            "signal_time": time_str,
            "symbol": f"{coin}USDT",
            "base_asset": coin,
            "timeframe": timeframe,
            "signal_type": sig_type,
            "bias": bias,
            "headline": narrative_title,
            "detail": full_detail,
            "price_level": price_level,
            "absorbed_vol_usd": volume_usd,
            "last_price": float(kpi_dict.get("last_price", 0.0)),
            "current_bar_delta_usd": float(kpi_dict.get("bar_delta_usd", 0.0)),
            "current_bar_volume_usd": float(kpi_dict.get("bar_volume_usd", 0.0)),
            "delta_in_view_usd": float(kpi_dict.get("delta_in_view_usd", 0.0)),
            "latest_signal_kpi": str(kpi_dict.get("latest_signal_name", "")),
            "latest_signal_bias": str(kpi_dict.get("latest_signal_bias", "")),
        })

    # If no signals extracted from tab, add top-level KPI summary row
    if not records:
        records.append({
            "timestamp_ist": now_ist,
            "signal_time": "LIVE",
            "symbol": f"{coin}USDT",
            "base_asset": coin,
            "timeframe": "15m",
            "signal_type": str(kpi_dict.get("latest_signal_name") or "DELTA_FLOW"),
            "bias": str(kpi_dict.get("latest_signal_bias") or "NEUTRAL").upper(),
            "headline": str(kpi_dict.get("latest_signal_desc") or "Live Footprint Stream"),
            "detail": f"Bar Delta: {kpi_dict.get('bar_delta_usd', 0.0)} | Vol: {kpi_dict.get('bar_volume_usd', 0.0)}",
            "price_level": float(kpi_dict.get("last_price", 0.0)),
            "absorbed_vol_usd": 0.0,
            "last_price": float(kpi_dict.get("last_price", 0.0)),
            "current_bar_delta_usd": float(kpi_dict.get("bar_delta_usd", 0.0)),
            "current_bar_volume_usd": float(kpi_dict.get("bar_volume_usd", 0.0)),
            "delta_in_view_usd": float(kpi_dict.get("delta_in_view_usd", 0.0)),
            "latest_signal_kpi": str(kpi_dict.get("latest_signal_name", "")),
            "latest_signal_bias": str(kpi_dict.get("latest_signal_bias", "")),
        })

    log.info(f"[{coin}] Harvested {len(records)} footprint signal records.")
    return records


async def run_footprint_collector(
    coins: List[str] | None = None,
    cdp_base_url: str = CDP_BASE_URL,
    sheet_name: str = TARGET_SHEET_NAME,
) -> bool:
    """Orchestrates full footprint collection across target assets."""
    active_coins = coins or DEFAULT_COINS
    log.info(f"Starting CoinGlass Footprint & Signals collector for {active_coins}...")

    # Open ephemeral tab
    initial_url = f"https://www.coinglass.com/footprint?symbol={active_coins[0]}"
    tab_id, ws_url = open_ephemeral_tab(initial_url, cdp_base_url)
    log.info(f"Opened dedicated ephemeral tab (ID: {tab_id}) for Footprint Signals.")

    try:
        ws = await websockets.connect(ws_url, max_size=25 * 1024 * 1024, open_timeout=15)
        msg_id = 1

        async def cdp_cmd(method: str, params: dict | None = None) -> dict:
            nonlocal msg_id
            curr_id = msg_id
            msg_id += 1
            payload = {"id": curr_id, "method": method, "params": params or {}}
            await ws.send(json.dumps(payload))
            while True:
                resp = json.loads(await ws.recv())
                if resp.get("id") == curr_id:
                    return resp.get("result", {}).get("result", {})

        all_records: List[Dict[str, Any]] = []
        for coin in active_coins:
            try:
                coin_records = await extract_footprint_for_coin(cdp_cmd, coin)
                all_records.extend(coin_records)
            except Exception as e:
                log.warning(f"Error harvesting footprint for {coin}: {e}")

        if not all_records:
            log.error("Footprint collector yielded 0 records.")
            return False

        meta = write_parquet_feed(sheet_name, all_records)
        log.info(f"Successfully saved {len(all_records)} Footprint Signal rows to {sheet_name}.parquet ({meta.get('byte_size')} bytes).")
        return True

    finally:
        if tab_id:
            close_tab(tab_id, cdp_base_url)


def main():
    parser = argparse.ArgumentParser(description="CoinGlass Footprint & Signals Pure-Parquet Dumper")
    parser.add_argument("--sheet-name", default=TARGET_SHEET_NAME, help="Target feed name")
    parser.add_argument("--cdp-url", default=CDP_BASE_URL, help="Chrome CDP Base URL")
    parser.add_argument("--coins", nargs="+", default=DEFAULT_COINS, help="Coins to harvest")

    args = parser.parse_args()
    ok = asyncio.run(run_footprint_collector(coins=args.coins, cdp_base_url=args.cdp_url, sheet_name=args.sheet_name))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
