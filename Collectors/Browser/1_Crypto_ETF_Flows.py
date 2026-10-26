#!/usr/bin/env python3
"""
Collectors/Browser/1_Crypto_ETF_Flows.py
========================================
Dedicated Module 1: Crypto ETF Flows.
Extracts the live 'Crypto ETF Overview' table from CoinGlass (https://www.coinglass.com/etf)
via Chrome/Edge CDP port 9222, executes tab rotation across ETF asset categories,
clicks 'Show All', and dumps all 39+ institutional ETF vehicles atomically into
Data/feeds/1_Crypto_ETF_Flows.parquet in the exact same format.

CoinGlass 'Crypto ETF Overview' Table Columns (12 Core Columns):
  1. #                     (Rank: 1, 2, 3...)
  2. Ticker                (e.g., IBIT BTC, FBTC BTC...)
  3. ETF Name              (e.g., iShares Bitcoin Trust)
  4. Price                 (Market Price USD, e.g., $46.55)
  5. Price Change          (e.g., +0.405 / +0.88%)
  6. Volume (USD)          (Daily Volume in USD, e.g., $41.97M)
  7. Volume (Shares)       (Volume in Shares, e.g., 898.73K)
  8. Turnover Rate         (e.g., 0.065%)
  9. Shares Outstanding    (e.g., 1.38B)
 10. AUM                   (Total Assets Under Management, e.g., $67.10B)
 11. Market Cap            (Market Capitalization, e.g., $64.48B)
 12. Expense Ratio         (Fee %, e.g., 0.25%)

Institutional Quantitative Context Columns:
 13. Asset Category        (Bitcoin, Ethereum, Solana, XRP, Hyperliquid, Multi-Asset)
 14. Issuer / Sponsor      (BlackRock / iShares, Fidelity, Grayscale, Bitwise, etc.)
 15. Daily Net Inflow      (from Table 0 Netflow feed)
 16. Timestamp (IST)       (Harvest Timestamp)
"""

from __future__ import annotations

import asyncio
import datetime
import json
import logging
import os
import pathlib
import sys
import time
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
sys.path.insert(0, str(ROOT_DIR / "Collectors" / "Core"))
sys.path.insert(0, str(ROOT_DIR / "Terminal" / "Data_Factory"))

try:
    from parquet_writer import write_parquet_feed
except ImportError:
    from parquet_feed_writer import write_parquet_feed

try:
    import websockets
except ImportError:
    websockets = None

CDP_BASE_URL = "http://127.0.0.1:9222"
TARGET_URL = "https://www.coinglass.com/etf"
FEED_NAME = "1_Crypto_ETF_Flows"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [1_Crypto_ETF_Flows] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("1_Crypto_ETF_Flows")

EXACT_COINGLASS_COLUMNS = [
    ("#", "#", 8, "center"),
    ("Ticker", "Ticker", 14, "left"),
    ("ETF_Name", "ETF Name", 45, "left"),
    ("Price", "Price", 16, "right"),
    ("Price_Change", "Price Change", 18, "right"),
    ("Volume_USD", "Volume (USD)", 18, "right"),
    ("Volume_Shares", "Volume (Shares)", 18, "right"),
    ("Turnover_Rate", "Turnover Rate", 16, "right"),
    ("Shares_Outstanding", "Shares Outstanding", 20, "right"),
    ("AUM", "AUM", 18, "right"),
    ("Market_Cap", "Market Cap", 18, "right"),
    ("Expense_Ratio", "Expense Ratio", 16, "right"),
    ("Asset_Category", "Asset Category", 16, "center"),
    ("Issuer", "Issuer / Sponsor", 26, "left"),
    ("Daily_Net_Inflow", "Daily Net Inflow", 20, "right"),
    ("Timestamp_IST", "Timestamp (IST)", 24, "center"),
]


def deduce_issuer(name: str, ticker: str) -> str:
    n = (name or "").lower()
    t = (ticker or "").upper()
    if "ishares" in n or "blackrock" in n: return "BlackRock / iShares"
    if "fidelity" in n or t in ["FBTC", "FETH", "FSOL"]: return "Fidelity"
    if "grayscale" in n or t in ["GBTC", "BTC", "ETHE", "ETH", "GSOL", "GXRP", "HYPG"]: return "Grayscale"
    if "bitwise" in n or t in ["BITB", "ETHW", "BITW", "BITC", "AETH", "BSOL", "XRP", "BHYP"]: return "Bitwise"
    if "canary" in n or t in ["XRPC"]: return "Canary Capital"
    if "ark" in n or "21shares" in n or t in ["ARKB", "TETH", "TSOL", "THYP"]: return "ARK / 21Shares"
    if "vaneck" in n or t in ["HODL", "ETHV", "VSOL"]: return "VanEck"
    if "franklin" in n or t in ["EZBC", "EZET", "XRPZ"]: return "Franklin Templeton"
    if "invesco" in n or t in ["BTCO", "QETH"]: return "Invesco Galaxy"
    if "wisdomtree" in n or t in ["BTCW"]: return "WisdomTree"
    if "proshares" in n or t in ["BITO", "BETH", "BETE", "EETH"]: return "ProShares"
    if "coinshares" in n or t in ["BRRR", "BTF"]: return "CoinShares / Valkyrie"
    if "morgan stanley" in n or t in ["MSBT"]: return "Morgan Stanley"
    if "hashdex" in n or t in ["DEFI"]: return "Hashdex"
    if "global x" in n or t in ["BITS"]: return "Global X"
    return "Independent"


def deduce_asset(ticker: str, name: str, explicit_tag: str = "") -> str:
    if explicit_tag:
        tag = explicit_tag.upper().strip()
        if "," in tag: return "Multi-Asset"
        if tag == "BTC": return "Bitcoin"
        if tag == "ETH": return "Ethereum"
        if tag == "SOL": return "Solana"
        if tag == "XRP": return "XRP"
        if tag == "HYPE": return "Hyperliquid"
    t = (ticker or "").upper()
    n = (name or "").lower()
    if "solana" in n or t in ["BSOL", "GSOL", "FSOL", "VSOL", "TSOL"] or t.endswith("SOL"):
        return "Solana"
    if "xrp" in n or t in ["XRP", "XRPC", "XRPZ", "GXRP"]:
        return "XRP"
    if "hyperliquid" in n or "hype" in n or t in ["BHYP", "THYP", "HYPG"]:
        return "Hyperliquid"
    if "ethereum" in n or "ether" in n or t in ["ETHA", "ETH", "ETHE", "FETH", "ETHW", "ETHV", "EZET", "QETH", "TETH", "ETHB"]:
        return "Ethereum"
    if "bitcoin" in n or t in ["IBIT", "FBTC", "GBTC", "BTC", "BITB", "ARKB", "BITO", "HODL", "BRRR", "EZBC", "BTCO", "BTCW", "MSBT"]:
        return "Bitcoin"
    if "crypto" in n or "index" in n or "basket" in n or t in ["BITW", "DEFI", "BTF", "BETH", "BETE"]:
        return "Multi-Asset"
    return "Other Crypto"


def get_target_tab() -> tuple[str, str, bool]:
    """Finds existing CoinGlass ETF tab or opens an ephemeral dedicated tab."""
    try:
        req = urllib.request.Request(f"{CDP_BASE_URL}/json")
        tabs = json.loads(urllib.request.urlopen(req, timeout=5).read().decode())
        for t in tabs:
            if "/etf" in t.get("url", ""):
                log.info(f"Reusing active CoinGlass ETF tab (ID: {t['id']}).")
                return t["id"], t["webSocketDebuggerUrl"], False
    except Exception as e:
        log.warning(f"Failed to query existing tabs: {e}")

    req = urllib.request.Request(f"{CDP_BASE_URL}/json/new?{TARGET_URL}", method="PUT")
    new_tab = json.loads(urllib.request.urlopen(req, timeout=8).read().decode())
    log.info(f"Opened dedicated ephemeral tab (ID: {new_tab['id']}).")
    return new_tab["id"], new_tab["webSocketDebuggerUrl"], True


def close_tab(tab_id: str):
    """Closes tab via CDP."""
    try:
        urllib.request.urlopen(f"{CDP_BASE_URL}/json/close/{tab_id}", timeout=4)
        log.info(f"Closed ephemeral tab {tab_id}")
    except Exception as e:
        log.warning(f"Error closing tab: {e}")


async def extract_coinglass_overview_table() -> list[dict]:
    """Connects to CDP, executes tab rotation across ETF categories, extracts all 39+ ETFs, and writes to parquet."""
    tab_id, ws_url, is_ephemeral = get_target_tab()

    now_ist = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    ).strftime("%Y-%m-%d %H:%M:%S IST")

    try:
        ws = None
        for attempt in range(10):
            try:
                ws = await websockets.connect(ws_url, max_size=25 * 1024 * 1024, open_timeout=8)
                break
            except Exception:
                await asyncio.sleep(0.5)

        if not ws:
            raise RuntimeError(f"Could not connect to WebSocket at {ws_url}")

        mid = 1

        async def cdp_cmd(method: str, params: dict | None = None) -> dict:
            nonlocal mid
            m = mid
            mid += 1
            await ws.send(json.dumps({"id": m, "method": method, "params": params or {}}))
            while True:
                msg = await ws.recv()
                d = json.loads(msg)
                if d.get("id") == m:
                    return d.get("result", {})

        if is_ephemeral:
            log.info("Awaiting page hydration on new ETF tab (4s)...")
            await asyncio.sleep(4.0)

        # 1. Tab rotation function across ETF categories
        async def click_tab(tab_name: str) -> bool:
            js_tab = f"""
            (() => {{
                const tabs = Array.from(document.querySelectorAll('[role="tab"]'));
                const target = tabs.find(t => t.innerText && t.innerText.trim() === '{tab_name}');
                if (target) {{
                    target.click();
                    return true;
                }}
                return false;
            }})()
            """
            res = await cdp_cmd("Runtime.evaluate", {"expression": js_tab, "returnByValue": True})
            return bool(res.get("result", {}).get("value"))

        # Perform tab rotation through asset categories
        etf_category_tabs = ["Bitcoin ETFs", "Ethereum ETFs", "Solana ETFs", "XRP ETFs", "All Crypto ETFs"]
        for cat_tab in etf_category_tabs:
            clicked = await click_tab(cat_tab)
            log.info(f"Tab rotation -> '{cat_tab}' (clicked: {clicked})")
            await asyncio.sleep(0.25)

        # Ensure return to 'All Crypto ETFs' to capture full universe
        await click_tab("All Crypto ETFs")
        await asyncio.sleep(0.3)

        # 2. Click 'Show All' to expand all rows in the overview table
        show_all_js = """
        (() => {
            const btn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === 'Show All');
            if (btn) {
                btn.click();
                return true;
            }
            return false;
        })()
        """
        await cdp_cmd("Runtime.evaluate", {"expression": show_all_js, "returnByValue": True})
        await asyncio.sleep(0.4)

        # 3. Extract Table 0 (Daily Net Inflows) & Table 2 (Crypto ETF Overview)
        extract_js = """
        (() => {
            const tables = Array.from(document.querySelectorAll('table'));
            
            // Table 0 Daily Inflows
            const inflows = {};
            if (tables.length > 0) {
                Array.from(tables[0].querySelectorAll('tbody tr')).forEach(tr => {
                    const tds = Array.from(tr.querySelectorAll('td')).map(td => td.innerText.trim());
                    if (tds.length >= 2) {
                        const parts = tds[0].split(/[ \\n]+/);
                        const ticker = parts[parts.length - 1].toUpperCase();
                        inflows[ticker] = tds[1];
                    }
                });
            }

            // Table 2 (Crypto ETF Overview)
            const overviewTable = tables.find(t => {
                const ths = Array.from(t.querySelectorAll('th')).map(th => th.innerText.trim());
                return ths.includes('#') && ths.includes('Ticker');
            }) || (tables.length > 2 ? tables[tables.length - 1] : null);

            if (!overviewTable) return { inflows, rows: [] };

            const trElements = Array.from(overviewTable.querySelectorAll('tbody tr'));
            const rows = trElements.map(tr => {
                const cells = Array.from(tr.querySelectorAll('td'));
                if (cells.length === 0) return null;
                return cells.map(td => td.innerText.replace(/\\n/g, ' ').trim());
            }).filter(r => r && r.length >= 4 && r[0] !== '');

            return { inflows, rows };
        })()
        """
        res_data = await cdp_cmd("Runtime.evaluate", {"expression": extract_js, "returnByValue": True})
        val = res_data.get("result", {}).get("value", {})
        inflows = val.get("inflows", {})
        raw_rows = val.get("rows", [])

        log.info(f"Extracted {len(raw_rows)} rows from 'Crypto ETF Overview' table.")

        records = []
        for r in raw_rows:
            rank = r[0] if len(r) > 0 else str(len(records) + 1)
            ticker_raw = r[1] if len(r) > 1 else ""
            parts = ticker_raw.split()
            ticker = parts[0].upper() if parts else ""
            explicit_tag = parts[1] if len(parts) > 1 else ""

            name = r[2] if len(r) > 2 else ""
            price = r[3] if len(r) > 3 else ""
            price_chg = r[4] if len(r) > 4 else ""
            vol_usd = r[5] if len(r) > 5 else ""
            vol_shares = r[6] if len(r) > 6 else ""
            turnover = r[7] if len(r) > 7 else ""
            shares_out = r[8] if len(r) > 8 else ""
            aum = r[9] if len(r) > 9 and r[9] else "-"
            mkt_cap = r[10] if len(r) > 10 and r[10] else "-"
            fee = r[11] if len(r) > 11 and r[11] else "-"

            asset = deduce_asset(ticker, name, explicit_tag)
            issuer = deduce_issuer(name, ticker)
            inflow = inflows.get(ticker, "-")

            records.append({
                "#": rank,
                "Ticker": ticker_raw,
                "ETF_Name": name,
                "Price": price,
                "Price_Change": price_chg,
                "Volume_USD": vol_usd,
                "Volume_Shares": vol_shares,
                "Turnover_Rate": turnover,
                "Shares_Outstanding": shares_out,
                "AUM": aum,
                "Market_Cap": mkt_cap,
                "Expense_Ratio": fee,
                "Asset_Category": asset,
                "Issuer": issuer,
                "Daily_Net_Inflow": inflow,
                "Timestamp_IST": now_ist,
            })

        await ws.close()
        return records

    finally:
        if is_ephemeral:
            close_tab(tab_id)


def dump_crypto_etf_overview_to_parquet() -> bool:
    log.info("Harvesting Crypto ETF Flows with tab rotation...")
    records = asyncio.run(extract_coinglass_overview_table())
    if not records:
        log.error("No records extracted from CoinGlass.")
        return False
    meta = write_parquet_feed(FEED_NAME, records)
    log.info(f"Successfully dumped {len(records)} Crypto ETF Overview assets into Parquet feed '{FEED_NAME}': {meta.get('byte_size')} bytes in {meta.get('write_latency_ms', 0):.2f}ms.")
    return True


if __name__ == "__main__":
    success = dump_crypto_etf_overview_to_parquet()
    sys.exit(0 if success else 1)
