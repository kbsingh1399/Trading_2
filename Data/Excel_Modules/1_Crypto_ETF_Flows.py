#!/usr/bin/env python3
"""
Data/Excel_Modules/1_Crypto_ETF_Flows.py
========================================
Dedicated Excel Module 1: Crypto ETF Flows.
Extracts the live 'Crypto ETF Overview' table from CoinGlass (https://www.coinglass.com/etf)
via Chrome/Edge CDP port 9222, automatically clicks 'Show All', and dumps the table
into the 'Crypto_ETF_Flows' worksheet in Data/DataBase_Trading.xlsx in the EXACT same format.

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
 16. Timestamp (UTC)       (Harvest Timestamp)
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

try:
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    raise ImportError("openpyxl is required. Run 'pip install openpyxl'.")

try:
    import websockets
except ImportError:
    websockets = None

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "Data"
DEFAULT_EXCEL_PATH = DATA_DIR / "DataBase_Trading.xlsx"
CDP_BASE_URL = "http://127.0.0.1:9222"
SHEET_NAME = "1_Crypto_ETF_Flows"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [1_Crypto_ETF_Flows] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
log = logging.getLogger("1_Crypto_ETF_Flows")

# Exact CoinGlass Crypto ETF Overview Schema
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
    ("Timestamp_UTC", "Timestamp (UTC)", 24, "center")
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


def open_etf_tab() -> tuple[str, str]:
    """Creates a new dedicated ephemeral CoinGlass ETF tab via CDP."""
    req = urllib.request.Request(f"{CDP_BASE_URL}/json/new?https://www.coinglass.com/etf", method="PUT")
    new_tab = json.loads(urllib.request.urlopen(req, timeout=5).read().decode())
    return new_tab["id"], new_tab["webSocketDebuggerUrl"]


def close_tab(tab_id: str):
    """Closes tab via CDP."""
    try:
        urllib.request.urlopen(f"{CDP_BASE_URL}/json/close/{tab_id}", timeout=4)
        log.info(f"Closed ephemeral tab {tab_id}")
    except Exception as e:
        log.warning(f"Error closing tab: {e}")


async def extract_coinglass_overview_table() -> list[dict]:
    """Connects to CDP, opens tab, clicks 'Show All', extracts Crypto ETF Overview table, and closes tab."""
    tab_id, ws_url = open_etf_tab()
    log.info(f"Opened dedicated CoinGlass ETF tab (ID: {tab_id})")

    now_dt = datetime.datetime.now(datetime.timezone.utc)
    ts_str = now_dt.strftime("%Y-%m-%d %H:%M:%S UTC")

    try:
        # Connect to websocket with connection retry
        ws = None
        for attempt in range(10):
            try:
                ws = await websockets.connect(ws_url, max_size=25 * 1024 * 1024, open_timeout=8)
                break
            except Exception as e:
                await asyncio.sleep(0.5)

        if not ws:
            raise RuntimeError(f"Could not connect to WebSocket at {ws_url}")

        async with ws:
            # 1. Dynamic readiness check: wait for tables to render
            table_check_js = """
            (() => {
                const tables = Array.from(document.querySelectorAll('table'));
                const overview = tables.find(t => {
                    const ths = Array.from(t.querySelectorAll('th')).map(th => th.innerText.trim());
                    return ths.includes('#') && ths.includes('Ticker');
                }) || (tables.length > 2 ? tables[tables.length - 1] : null);
                if (!overview) return 0;
                return overview.querySelectorAll('tbody tr').length;
            })()
            """
            table_ready = False
            for _ in range(30):  # up to 15 seconds
                await ws.send(json.dumps({"id": 10, "method": "Runtime.evaluate", "params": {"expression": table_check_js, "returnByValue": True}}))
                res = json.loads(await ws.recv())
                row_count = res.get("result", {}).get("result", {}).get("value", 0)
                if row_count >= 10:
                    table_ready = True
                    log.info(f"Overview table ready with initial {row_count} rows.")
                    break
                await asyncio.sleep(0.5)

            if not table_ready:
                log.warning("Table readiness timed out after 15s; proceeding with best effort.")

            # 2. Click 'Show All' and verify expansion
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
            for click_attempt in range(5):
                await ws.send(json.dumps({"id": 20 + click_attempt, "method": "Runtime.evaluate", "params": {"expression": show_all_js, "returnByValue": True}}))
                res1 = json.loads(await ws.recv())
                clicked = res1.get("result", {}).get("result", {}).get("value")
                if clicked:
                    log.info("Clicked 'Show All' button successfully.")
                    break
                await asyncio.sleep(0.5)

            # Wait for table expansion to >= 35 rows
            for _ in range(12):  # up to 6 seconds
                await asyncio.sleep(0.5)
                await ws.send(json.dumps({"id": 30, "method": "Runtime.evaluate", "params": {"expression": table_check_js, "returnByValue": True}}))
                res_exp = json.loads(await ws.recv())
                exp_count = res_exp.get("result", {}).get("result", {}).get("value", 0)
                if exp_count >= 35:
                    log.info(f"Table expanded to {exp_count} rows.")
                    break

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
            await ws.send(json.dumps({"id": 40, "method": "Runtime.evaluate", "params": {"expression": extract_js, "returnByValue": True}}))
            res2 = json.loads(await ws.recv())
            val = res2.get("result", {}).get("result", {}).get("value", {})
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
                    "Timestamp_UTC": ts_str
                })

            return records
    finally:
        close_tab(tab_id)


def dump_crypto_etf_overview_to_excel(excel_path: pathlib.Path = DEFAULT_EXCEL_PATH) -> bool:
    """Dumps the Crypto ETF Overview table into Data/DataBase_Trading.xlsx matching CoinGlass format."""
    records = asyncio.run(extract_coinglass_overview_table())
    if not records:
        log.error("No records extracted from CoinGlass.")
        return False

    if not excel_path.exists():
        log.error(f"Excel file not found: {excel_path}")
        return False

    wb = openpyxl.load_workbook(excel_path)
    if SHEET_NAME in wb.sheetnames:
        ws = wb[SHEET_NAME]
    elif "Crypto_ETF_Flows" in wb.sheetnames:
        ws = wb["Crypto_ETF_Flows"]
        ws.title = SHEET_NAME
    else:
        ws = wb.create_sheet(title=SHEET_NAME, index=0)

    # Styles
    header_font = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")  # Dark slate / black theme

    data_font = Font(name="Segoe UI", size=10, bold=False, color="1E293B")
    green_font = Font(name="Segoe UI", size=10, bold=True, color="15803D")
    red_font = Font(name="Segoe UI", size=10, bold=True, color="B91C1C")
    dim_font = Font(name="Segoe UI", size=10, bold=False, color="64748B")

    # Soft asset fills
    asset_fills = {
        "Bitcoin": PatternFill(start_color="FFFBEB", end_color="FFFBEB", fill_type="solid"),
        "Ethereum": PatternFill(start_color="F0FDF4", end_color="F0FDF4", fill_type="solid"),
        "Solana": PatternFill(start_color="FAF5FF", end_color="FAF5FF", fill_type="solid"),
        "XRP": PatternFill(start_color="ECFEFF", end_color="ECFEFF", fill_type="solid"),
        "Hyperliquid": PatternFill(start_color="FFF7ED", end_color="FFF7ED", fill_type="solid"),
        "Multi-Asset": PatternFill(start_color="FFF1F2", end_color="FFF1F2", fill_type="solid"),
        "Default": PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
    }

    thin_border = Border(
        left=Side(style='thin', color='CBD5E1'),
        right=Side(style='thin', color='CBD5E1'),
        top=Side(style='thin', color='CBD5E1'),
        bottom=Side(style='thin', color='CBD5E1')
    )

    # Write Headers
    for col_idx, (_, col_title, width, align) in enumerate(EXACT_COINGLASS_COLUMNS, 1):
        c = ws.cell(row=1, column=col_idx, value=col_title)
        c.font = header_font
        c.fill = header_fill
        c.alignment = Alignment(horizontal=align, vertical="center")
        c.border = thin_border
        col_letter = get_column_letter(col_idx)
        ws.column_dimensions[col_letter].width = max(width, 12)
    ws.row_dimensions[1].height = 26

    # Write Data Rows directly starting at Row 2
    for idx, rec in enumerate(records):
        r_idx = 2 + idx
        asset = rec.get("Asset_Category", "Default")
        row_fill = asset_fills.get(asset, asset_fills["Default"])

        for col_idx, (key, _, _, align) in enumerate(EXACT_COINGLASS_COLUMNS, 1):
            val = rec.get(key, "-")
            cell_obj = ws.cell(row=r_idx, column=col_idx, value=val)
            cell_obj.border = thin_border
            cell_obj.alignment = Alignment(horizontal=align, vertical="center")
            cell_obj.fill = row_fill

            sval = str(val or "").strip()
            if key in ["Price_Change", "Daily_Net_Inflow"]:
                if sval.startswith("+") or (any(c.isdigit() for c in sval) and not sval.startswith("-") and not sval.startswith("$0") and sval != "-"):
                    cell_obj.font = green_font
                elif sval.startswith("-") and sval != "-":
                    cell_obj.font = red_font
                else:
                    cell_obj.font = dim_font
            else:
                cell_obj.font = data_font

        ws.row_dimensions[r_idx].height = 20

    # Prune any old trailing rows
    current_data_end = 1 + len(records)
    if ws.max_row > current_data_end:
        ws.delete_rows(current_data_end + 1, ws.max_row - current_data_end)

    # Save Atomically
    temp_excel = excel_path.with_suffix(".tmp.xlsx")
    wb.save(temp_excel)
    wb.close()
    temp_excel.replace(excel_path)

    log.info(f"Successfully dumped {len(records)} CoinGlass Crypto ETF Overview records into '{SHEET_NAME}' at {excel_path}.")
    return True


if __name__ == "__main__":
    success = dump_crypto_etf_overview_to_excel()
    sys.exit(0 if success else 1)
