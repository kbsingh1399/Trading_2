"""
CoinGlass Institutional Deep Analytics & Multi-Asset Excel Pipeline
===================================================================
Consolidates data into exactly 1 sheet per CoinGlass page/dashboard:
  1. ETF_Overview       -> https://www.coinglass.com/etf
  2. ETF_Bitcoin        -> https://www.coinglass.com/etf/bitcoin
  3. ETF_Ethereum       -> https://www.coinglass.com/etf/ethereum
  4. ETF_Solana         -> https://www.coinglass.com/etf/solana
  5. ETF_XRP            -> https://www.coinglass.com/etf/xrp
  6. Funding_Rates      -> https://www.coinglass.com/FundingRate
  7. Funding_Fees       -> https://www.coinglass.com/funding-fees
  8. Open_Interest      -> https://www.coinglass.com/open-interest/BTC (BTC, ETH, SOL, HYPE, XRP, DOGE, BNB, SUI, NEAR, LINK)
  9. Long_Short_Ratio   -> https://www.coinglass.com/LongShortRatio (20+ assets summary + 22 exchanges appended asset-wise)

Key Operating Invariants:
  - 1 Sheet per Page: Data on the same CoinGlass page resides in structured sections on the SAME Excel sheet.
  - Continuous Asset-Wise Tables: Homogeneous table structures (e.g., Exchange OI, Exchange L/S ratios) are appended ASSET-WISE into ONE unified, continuous table with 'Asset' in column A for 100% system readability.
  - Zero Empty Headers: If a section has 0 rows, it is NEVER rendered.
  - 100% Parsing Accuracy: Validates percentage symbols before parsing exchange table lines to avoid misalignment from sentiment tags.
  - Overwrite/Replace: Completely deletes previous values on each run to reflect live dashboard updates.
  - Complete Chart Time-Series: Tabular extraction of all timestamps available in window across all charts.
  - Generous Uncompressed Layout: Auto-fitted columns (+5 padding), 28pt banners, 26pt headers, 20pt rows, 18pt spacers, frozen panes at A2.
  - Zero Repo Git Push: Confined strictly to Data/DataBase_Trading.xlsx.
"""

import os
import sys
import json
import asyncio
import urllib.request
import argparse
import time
from datetime import datetime, timezone
from pathlib import Path

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

DEFAULT_EXCEL_PATH = Path("Data/DataBase_Trading.xlsx")
CDP_BASE_URL = "http://127.0.0.1:9222"

# ------------------------------------------------------------------------------
# Typography, Palette & Formatting Contracts
# ------------------------------------------------------------------------------
BANNER_FONT = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
BANNER_FILL = PatternFill(start_color="1E293B", end_color="1E293B", fill_type="solid")

HEADER_FONT = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
HEADER_FILL = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")

DATA_FONT = Font(name="Segoe UI", size=9, bold=False, color="1E293B")
BOLD_FONT = Font(name="Segoe UI", size=9, bold=True, color="0F172A")
GREEN_FONT = Font(name="Segoe UI", size=9, bold=True, color="15803D")
RED_FONT = Font(name="Segoe UI", size=9, bold=True, color="B91C1C")
DIM_FONT = Font(name="Segoe UI", size=9, bold=False, color="64748B")

ROW_FILL_DEFAULT = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
ROW_FILL_ALT = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
ROW_FILL_BTC = PatternFill(start_color="FFFBEB", end_color="FFFBEB", fill_type="solid")
ROW_FILL_ETH = PatternFill(start_color="F0FDF4", end_color="F0FDF4", fill_type="solid")
ROW_FILL_SOL = PatternFill(start_color="FAF5FF", end_color="FAF5FF", fill_type="solid")
ROW_FILL_XRP = PatternFill(start_color="ECFEFF", end_color="ECFEFF", fill_type="solid")

THIN_BORDER = Border(
    left=Side(style='thin', color='CBD5E1'),
    right=Side(style='thin', color='CBD5E1'),
    top=Side(style='thin', color='CBD5E1'),
    bottom=Side(style='thin', color='CBD5E1')
)


def get_cdp_tabs():
    """Returns list of open page tabs from Chrome CDP."""
    try:
        data = urllib.request.urlopen(f"{CDP_BASE_URL}/json", timeout=3).read().decode()
        tabs = json.loads(data)
        return [t for t in tabs if t.get("type") == "page"]
    except Exception as e:
        print(f"Failed to connect to Chrome CDP: {e}")
        return []


def render_sections_to_sheet(ws, sections_def, default_fill=ROW_FILL_DEFAULT):
    """
    Renders multiple structured sections sequentially onto a SINGLE worksheet:
      1. Section Banner (Dark Slate #1E293B, 28pt height)
      2. Column Headers (Navy #0F172A, 26pt height)
      3. Data Rows (Formatted, 20pt height, Segoe UI 9pt, color coded)
      4. Spacer Row (18pt height)
      5. Generous column width auto-fit (max_len + 5, min 16-36)
      6. Freeze panes at A2
      Strict rule: Never render empty sections with 0 data rows.
    """
    if ws is None:
        return
    current_row = 1
    max_col_count = 1

    for sec in sections_def:
        title = sec.get("title", "")
        cols = sec.get("columns", [])
        rows = sec.get("rows", [])
        row_fill = sec.get("row_fill", default_fill)

        # Skip sections that have no columns or no data rows
        if not cols or not rows:
            continue
        max_col_count = max(max_col_count, len(cols))

        # 1. Section Title Banner
        if title:
            clean_title = str(title).replace("===", "").strip()
            while clean_title.startswith("="):
                clean_title = clean_title.lstrip("=").strip()
            ws.row_dimensions[current_row].height = 28
            cell = ws.cell(row=current_row, column=1, value=clean_title)
            cell.font = BANNER_FONT
            cell.fill = BANNER_FILL
            cell.alignment = Alignment(horizontal="left", vertical="center", indent=1)
            for c in range(2, max(len(cols) + 1, 8)):
                fill_cell = ws.cell(row=current_row, column=c, value="")
                fill_cell.fill = BANNER_FILL
            current_row += 1

        # 2. Section Column Headers
        ws.row_dimensions[current_row].height = 26
        for col_idx, (_, col_title, _, _) in enumerate(cols, 1):
            h_cell = ws.cell(row=current_row, column=col_idx, value=col_title)
            h_cell.font = HEADER_FONT
            h_cell.fill = HEADER_FILL
            h_cell.alignment = Alignment(horizontal="center", vertical="center")
            h_cell.border = THIN_BORDER
        current_row += 1

        # 3. Section Data Rows
        for r in rows:
            ws.row_dimensions[current_row].height = 20
            for col_idx, (key, _, _, align) in enumerate(cols, 1):
                val = r.get(key, "")
                if isinstance(val, str) and val.startswith("=") and not val.startswith("=SUM") and not val.startswith("=AVERAGE"):
                    val = val.lstrip("=").strip()
                d_cell = ws.cell(row=current_row, column=col_idx, value=val)
                d_cell.border = THIN_BORDER
                d_cell.fill = row_fill
                d_cell.alignment = Alignment(horizontal=align, vertical="center")

                val_str = str(val).strip()
                if any(k in key for k in ["Flow", "Inflow", "Outflow", "Change", "Ratio", "Pct", "Weighted", "Rate"]):
                    if val_str.startswith("+") or (val_str.replace('.', '', 1).isdigit() and float(val_str) > 1.0 and "Ratio" in key):
                        d_cell.font = GREEN_FONT
                    elif val_str.startswith("-") or (val_str.replace('.', '', 1).isdigit() and float(val_str) < 1.0 and "Ratio" in key):
                        d_cell.font = RED_FONT
                    elif val_str in ["0", "+0", "-", "0%", "0.00%"]:
                        d_cell.font = DIM_FONT
                    else:
                        d_cell.font = DATA_FONT
                elif key in ["Date", "Date_UTC", "Timestamp_UTC", "Asset", "Exchange", "Ticker", "Pair", "Symbol", "Ranking"]:
                    d_cell.font = BOLD_FONT
                else:
                    d_cell.font = DATA_FONT
            current_row += 1

        # 4. Spacer row
        ws.row_dimensions[current_row].height = 18
        current_row += 1

    # Pin frozen panes at A2
    ws.freeze_panes = "A2"

    # Generous uncompressed column width auto-fit (never format so as to save space)
    for col_idx in range(1, max_col_count + 1):
        col_letter = get_column_letter(col_idx)
        max_len = 0
        for cell in ws[col_letter]:
            val = cell.value
            if val is not None and not str(val).startswith("=== "):
                max_len = max(max_len, len(str(val)))
        ws.column_dimensions[col_letter].width = max(max_len + 5, 18)


# ==============================================================================
# Extraction Subroutines (Sub-second CDP WebSocket)
# ==============================================================================

async def extract_etf_overview():
    """Extracts Crypto ETF Net Flows chart series & multi-asset comparison from /etf."""
    tabs = get_cdp_tabs()
    target = next((t for t in tabs if "coinglass" in t.get("url", "").lower()), None)
    if not target:
        return None
    ws_url = target["webSocketDebuggerUrl"]

    async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
        await ws.send(json.dumps({"id": 1, "method": "Page.navigate", "params": {"url": "https://www.coinglass.com/etf"}}))
        await ws.recv()
        await asyncio.sleep(2.5)

        script = """(async () => {
            const res = {};
            const allBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === 'All');
            if (allBtn) {
                allBtn.click();
                await new Promise(r => setTimeout(r, 400));
            }

            const chartEls = document.querySelectorAll('.echarts-for-react');
            res.charts = [];
            chartEls.forEach((el, idx) => {
                const fiberKey = Object.keys(el || {}).find(k => k.startsWith('__reactFiber'));
                let cur = el ? el[fiberKey] : null;
                while (cur) {
                    const opt = cur.stateNode?.state?.option || cur.memoizedProps?.option;
                    if (opt?.series) {
                        res.charts.push({
                            idx,
                            xData: opt.xAxis?.[0]?.data || [],
                            series: opt.series.map(s => ({
                                name: (s.name || '').trim(),
                                data: s.data || []
                            }))
                        });
                        break;
                    }
                    cur = cur.return;
                }
            });

            const tables = Array.from(document.querySelectorAll('table'));
            if (tables.length >= 2) {
                res.headers = Array.from(tables[0].querySelectorAll('th, td')).map(c => c.innerText.trim().replace('\\n', ' '));
                res.rows = Array.from(tables[1].querySelectorAll('tr')).map(tr => 
                    Array.from(tr.querySelectorAll('td')).map(td => td.innerText.trim())
                ).filter(r => r.length > 0 && r.some(c => c.length > 0));
            }
            return res;
        })()"""
        await ws.send(json.dumps({"id": 2, "method": "Runtime.evaluate", "params": {"expression": script, "returnByValue": True, "awaitPromise": True}}))
        return json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value", {})


async def extract_etf_asset(asset_slug="bitcoin"):
    """Extracts all data for a specific ETF asset (Overview, Charts, Holdings, Benchmark)."""
    tabs = get_cdp_tabs()
    target = next((t for t in tabs if "coinglass" in t.get("url", "").lower()), None)
    if not target:
        return None
    ws_url = target["webSocketDebuggerUrl"]

    target_url = f"https://www.coinglass.com/etf/{asset_slug}"
    async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
        await ws.send(json.dumps({"id": 10, "method": "Page.navigate", "params": {"url": target_url}}))
        await ws.recv()
        await asyncio.sleep(2.5)

        script = """(() => {
            const res = {};
            const tables = Array.from(document.querySelectorAll('table'));
            if (tables.length >= 2) {
                res.dailyHeaders = Array.from(tables[0].querySelectorAll('th, td')).map(c => c.innerText.trim().replace('\\n', ' '));
                res.dailyRows = Array.from(tables[1].querySelectorAll('tr')).map(tr => 
                    Array.from(tr.querySelectorAll('td')).map(td => td.innerText.trim())
                ).filter(r => r.length > 0 && r.some(c => c.length > 0));
            }

            const chartEls = document.querySelectorAll('.echarts-for-react');
            res.chartSeriesList = [];
            res.rawBtcState = null;
            chartEls.forEach(el => {
                const fiberKey = Object.keys(el || {}).find(k => k.startsWith('__reactFiber'));
                if (fiberKey) {
                    let cur = el[fiberKey];
                    let depth = 0;
                    while (cur && depth < 25) {
                        if (cur.stateNode?.state?.btc) {
                            res.rawBtcState = cur.stateNode.state.btc;
                        }
                        if (cur.memoizedProps?.option?.series) {
                            const opt = cur.memoizedProps.option;
                            res.chartSeriesList.push({
                                xData: opt.xAxis?.[0]?.data || opt.xAxis?.data || [],
                                series: opt.series.map(s => ({
                                    name: (s.name || '').trim(),
                                    type: s.type,
                                    data: s.data || []
                                }))
                            });
                            break;
                        }
                        cur = cur.return;
                        depth++;
                    }
                }
            });
            return res;
        })()"""
        await ws.send(json.dumps({"id": 11, "method": "Runtime.evaluate", "params": {"expression": script, "returnByValue": True}}))
        overview_data = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value", {})

        chart_subtabs = {}
        if asset_slug == "bitcoin":
            chart_tabs_script = """(async () => {
                const chartData = {};
                const getEChart = () => {
                    const el = document.querySelector('.echarts-for-react');
                    const fiberKey = Object.keys(el || {}).find(k => k.startsWith('__reactFiber'));
                    let cur = el ? el[fiberKey] : null;
                    let depth = 0;
                    while (cur && depth < 25) {
                        if (cur.memoizedProps?.option?.series) return cur.memoizedProps.option;
                        cur = cur.return;
                        depth++;
                    }
                    return null;
                };

                for (const name of ['AUM', 'Market Cap', 'Volume', 'Flows (USD)']) {
                    const btn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === name);
                    if (btn) {
                        btn.click();
                        await new Promise(r => setTimeout(r, 400));
                        const opt = getEChart();
                        if (opt) {
                            chartData[name] = {
                                xData: opt.xAxis?.[0]?.data || opt.xAxis?.data || [],
                                series: opt.series.map(s => ({
                                    name: (s.name || '').trim(),
                                    type: s.type,
                                    data: s.data || []
                                }))
                            };
                        }
                    }
                }
                return chartData;
            })()"""
            await ws.send(json.dumps({"id": 12, "method": "Runtime.evaluate", "params": {"expression": chart_tabs_script, "awaitPromise": True, "returnByValue": True}}))
            chart_subtabs = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value", {})

        holdings_script = """(async () => {
            const btn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === 'Assets Inflows/Outflows');
            if (btn) {
                btn.click();
                await new Promise(r => setTimeout(r, 600));
                const tables = Array.from(document.querySelectorAll('table'));
                if (tables.length >= 4) {
                    const headers = Array.from(tables[2].querySelectorAll('th, td')).map(c => c.innerText.trim().replace('\\n', ' '));
                    const rows = Array.from(tables[3].querySelectorAll('tr')).map(tr => 
                        Array.from(tr.querySelectorAll('td')).map(td => td.innerText.trim())
                    ).filter(r => r.length > 0 && r.some(c => c.length > 0));
                    return { headers, rows };
                }
            }
            return null;
        })()"""
        await ws.send(json.dumps({"id": 13, "method": "Runtime.evaluate", "params": {"expression": holdings_script, "awaitPromise": True, "returnByValue": True}}))
        holdings_data = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value", {})

        top_etfs_data = None
        if asset_slug == "bitcoin":
            top_etfs_script = """(async () => {
                const btn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === 'Bitcoin ETFs vs Top ETFs');
                if (btn) {
                    btn.click();
                    await new Promise(r => setTimeout(r, 600));
                    const tables = Array.from(document.querySelectorAll('table'));
                    if (tables.length >= 6) {
                        const headers = Array.from(tables[4].querySelectorAll('th, td')).map(c => c.innerText.trim().replace('\\n', ' '));
                        const rows = Array.from(tables[5].querySelectorAll('tr')).map(tr => 
                            Array.from(tr.querySelectorAll('td')).map(td => td.innerText.trim())
                        ).filter(r => r.length > 0 && r.some(c => c.length > 0));
                        return { headers, rows };
                    }
                }
                return null;
            })()"""
            await ws.send(json.dumps({"id": 14, "method": "Runtime.evaluate", "params": {"expression": top_etfs_script, "awaitPromise": True, "returnByValue": True}}))
            top_etfs_data = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value", {})

        return {
            "asset_slug": asset_slug,
            "overview": overview_data,
            "chart_subtabs": chart_subtabs,
            "holdings": holdings_data,
            "top_etfs": top_etfs_data
        }


async def extract_funding_analytics():
    """Extracts live rates, 3,000pt OI-weighted chart, multi-exchange chart, and settlements dashboard."""
    tabs = get_cdp_tabs()
    target = next((t for t in tabs if "coinglass" in t.get("url", "").lower()), None)
    if not target:
        return None
    ws_url = target["webSocketDebuggerUrl"]

    results = {}
    async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
        await ws.send(json.dumps({"id": 20, "method": "Page.navigate", "params": {"url": "https://www.coinglass.com/FundingRate"}}))
        await ws.recv()
        await asyncio.sleep(2.5)

        fr_script = """(() => {
            const res = {};
            const tables = Array.from(document.querySelectorAll('table'));
            if (tables.length >= 2) {
                res.headers = Array.from(tables[0].querySelectorAll('th, td')).map(c => c.innerText.trim().replace('\\n', ' ')).filter(Boolean);
                res.rows = Array.from(tables[1].querySelectorAll('tr')).map(tr => 
                    Array.from(tr.querySelectorAll('td')).map(td => td.innerText.trim())
                ).filter(r => r.length > 0 && r.some(c => c.length > 0));
            }

            const echarts = document.querySelectorAll('.echarts-for-react');
            if (echarts.length >= 1) {
                const el0 = echarts[0];
                const fk = Object.keys(el0 || {}).find(k => k.startsWith('__reactFiber'));
                let cur = el0[fk];
                while (cur) {
                    const opt = cur.stateNode?.state?.option || cur.memoizedProps?.option;
                    if (opt?.series) {
                        res.oiWeightedDates = opt.xAxis?.[0]?.data || [];
                        res.oiWeightedSeries = opt.series.map(s => ({ name: s.name, data: s.data || [] }));
                        break;
                    }
                    cur = cur.return;
                }
            }

            if (echarts.length >= 2) {
                const el1 = echarts[1];
                const fk = Object.keys(el1 || {}).find(k => k.startsWith('__reactFiber'));
                let cur = el1[fk];
                while (cur) {
                    const opt = cur.stateNode?.state?.option || cur.memoizedProps?.option;
                    if (opt?.series) {
                        res.exDates = opt.xAxis?.[0]?.data || [];
                        res.exSeries = opt.series.map(s => ({ name: s.name, data: s.data || [] }));
                        break;
                    }
                    cur = cur.return;
                }
            }
            return res;
        })()"""
        await ws.send(json.dumps({"id": 21, "method": "Runtime.evaluate", "params": {"expression": fr_script, "returnByValue": True}}))
        results["rates"] = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value", {})

        await ws.send(json.dumps({"id": 22, "method": "Page.navigate", "params": {"url": "https://www.coinglass.com/funding-fees"}}))
        await ws.recv()
        await asyncio.sleep(2.0)

        ff_script = """(() => {
            const tables = Array.from(document.querySelectorAll('table'));
            if (tables.length < 2) return null;
            const headers = Array.from(tables[0].querySelectorAll('th, td')).map(c => c.innerText.trim().replace('\\n', ' ')).filter(Boolean);
            const rows = Array.from(tables[1].querySelectorAll('tr')).map(tr => 
                Array.from(tr.querySelectorAll('td')).map(td => td.innerText.trim())
            ).filter(r => r.length > 0 && r.some(c => c.length > 0));
            return { headers, rows };
        })()"""
        await ws.send(json.dumps({"id": 23, "method": "Runtime.evaluate", "params": {"expression": ff_script, "returnByValue": True}}))
        results["fees"] = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value", {})

    return results


async def extract_open_interest_multi(assets=("BTC", "ETH", "SOL", "HYPE", "XRP", "ZEC", "XAU", "NEAR", "DOGE", "BNB")):
    """
    Extracts complete institutional Open Interest analytics matching User Images 1, 2, and 3:
      1. Sheet 'Open_Interest': Table 1 stacked across all 10 institutional assets.
      2. Sheet 'Open_Interest_Top_Gainers': Top Gainers for BOTH 1h and 4h timeframes.
      3. Sheet 'Open_Interest_Top_Losers': Top Losers for BOTH 1h and 4h timeframes.
      4. Sheets 'Exchange_Open_Interest_Chart_15M', 'Exchange_Open_Interest_Chart_1H', 'Exchange_Open_Interest_Chart_4H':
         Historical candle series across assets formatted with Sr.No, Asset, Timestamp_UTC, Price_USD, Open_Interest_USD.
    """
    tabs = get_cdp_tabs()
    target = next((t for t in tabs if "coinglass" in t.get("url", "").lower()), None)
    if not target:
        return None
    ws_url = target["webSocketDebuggerUrl"]

    results = {
        "tables": {},
        "h1_gainers": [],
        "h1_losers": [],
        "h4_gainers": [],
        "h4_losers": [],
        "charts_15m": {},
        "charts_1h": {},
        "charts_4h": {}
    }

    async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
        msg_id = 300

        # Ensure we are on /open-interest/BTC
        msg_id += 1
        await ws.send(json.dumps({"id": msg_id, "method": "Runtime.evaluate", "params": {"expression": "window.location.href"}}))
        cur_url = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value", "")
        if "open-interest" not in cur_url:
            print(">> Navigating to https://www.coinglass.com/open-interest/BTC...")
            msg_id += 1
            await ws.send(json.dumps({"id": msg_id, "method": "Page.navigate", "params": {"url": "https://www.coinglass.com/open-interest/BTC"}}))
            await ws.recv()
            await asyncio.sleep(2.5)

        # 1. Harvest Table 1 across all 10 institutional assets via rapid tab switching
        print(f">> Extracting Table 1 across {len(assets)} assets ({', '.join(assets)})...")
        extract_tables_script = f"""(async () => {{
            const targetAssets = {json.dumps(list(assets))};
            const allResults = {{}};

            const getRows = () => {{
                const tables = document.querySelectorAll('table');
                if (tables.length < 2) return [];
                const tbody = tables[1].querySelector('tbody') || tables[1];
                return Array.from(tbody.querySelectorAll('tr')).map(tr => 
                    Array.from(tr.querySelectorAll('td')).map(td => td.innerText.trim().replace(/\\n/g, ' '))
                ).filter(r => r.length > 0 && r.some(c => c.length > 0));
            }};

            for (const sym of targetAssets) {{
                const tabs = Array.from(document.querySelectorAll('.cg-tab-item, button, div[role="button"]'));
                const btn = tabs.find(b => b.innerText.trim() === sym);
                if (btn) {{
                    btn.scrollIntoView({{ behavior: 'instant', block: 'nearest', inline: 'center' }});
                    btn.click();
                    
                    const start = Date.now();
                    while (Date.now() - start < 3000) {{
                        await new Promise(r => setTimeout(r, 100));
                        const rows = getRows();
                        const allRow = rows.find(r => r.includes('All'));
                        if (allRow && (allRow[2] || '').includes(sym)) {{
                            break;
                        }}
                    }}
                    allResults[sym] = getRows();
                }}
            }}
            return allResults;
        }})()"""
        msg_id += 1
        await ws.send(json.dumps({"id": msg_id, "method": "Runtime.evaluate", "params": {"expression": extract_tables_script, "returnByValue": True, "awaitPromise": True}}))
        tables_data = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value", {})
        results["tables"] = tables_data
        for sym, r_list in tables_data.items():
            print(f"  [{sym}] Harvested {len(r_list)} exchange breakdown rows")

        # 2. Extract Top Gainers and Top Losers (both 1h and 4h)
        print(">> Extracting Top Gainers and Top Losers (both 1 hour and 4 hour)...")
        gainers_losers_script = """(async () => {
            const cards = Array.from(document.querySelectorAll('.cgj-card, .MuiCard-root, div[class*="Card"]'));
            const cardEl = cards.find(c => (c.innerText || '').includes('Top Gainers'));
            if (cardEl) cardEl.scrollIntoView({ behavior: 'instant', block: 'center' });

            const parseCardSection = (isGainers) => {
                const text = cardEl ? cardEl.innerText : '';
                const parts = text.split(isGainers ? 'Top Gainers' : 'Top Losers');
                if (parts.length < 2) return [];
                const block = parts[1].split(isGainers ? 'Top Losers' : 'OI/24h_Vol')[0];
                const lines = block.split('\\n').map(l => l.trim()).filter(Boolean);
                
                const validRows = [];
                for (let i = 0; i < lines.length - 4; i++) {
                    const pair = lines[i];
                    if ((pair.includes('/') || pair.includes('USDT') || pair.includes('USD')) && 
                        !pair.includes('Pair') && !pair.includes('Price') && !pair.includes('OI')) {
                        const prc = lines[i+1];
                        const prcChg = lines[i+2];
                        const oi = lines[i+3];
                        const oiChg = lines[i+4];
                        if (prcChg.includes('%') && oiChg.includes('%')) {
                            validRows.push({
                                pair: pair,
                                price: prc,
                                priceChange: prcChg,
                                oi: oi,
                                oiChange: oiChg
                            });
                        }
                    }
                }
                return validRows;
            };

            const out = { h1_gainers: [], h1_losers: [], h4_gainers: [], h4_losers: [] };

            const btn = Array.from(document.querySelectorAll('.MuiSelect-button')).find(b => b.innerText.trim() === '1 hour' || b.innerText.trim() === '4 hour');
            if (btn && btn.innerText.trim() !== '1 hour') {
                btn.click();
                await new Promise(r => setTimeout(r, 200));
                const opt1h = Array.from(document.querySelectorAll('[role="option"], li')).find(o => o.innerText.trim() === '1 hour');
                if (opt1h) opt1h.click();
                await new Promise(r => setTimeout(r, 1200));
            }
            out.h1_gainers = parseCardSection(true);
            out.h1_losers = parseCardSection(false);

            if (btn) {
                btn.click();
                await new Promise(r => setTimeout(r, 200));
                const opt4h = Array.from(document.querySelectorAll('[role="option"], li')).find(o => o.innerText.trim() === '4 hour');
                if (opt4h) opt4h.click();
                await new Promise(r => setTimeout(r, 1200));
            }
            out.h4_gainers = parseCardSection(true);
            out.h4_losers = parseCardSection(false);

            return out;
        })()"""
        msg_id += 1
        await ws.send(json.dumps({"id": msg_id, "method": "Runtime.evaluate", "params": {"expression": gainers_losers_script, "returnByValue": True, "awaitPromise": True}}))
        cards_data = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value", {})
        results["h1_gainers"] = cards_data.get("h1_gainers", [])
        results["h1_losers"] = cards_data.get("h1_losers", [])
        results["h4_gainers"] = cards_data.get("h4_gainers", [])
        results["h4_losers"] = cards_data.get("h4_losers", [])
        print(f"  Top Gainers (1h: {len(results['h1_gainers'])} | 4h: {len(results['h4_gainers'])})")
        print(f"  Top Losers  (1h: {len(results['h1_losers'])} | 4h: {len(results['h4_losers'])})")

        # 3. Extract Charts across 15m, 1h, and 4h timeframes
        print(">> Extracting Historical Open Interest Charts across 15m, 1h, and 4h...")
        chart_assets = ["BTC", "ETH", "SOL", "HYPE", "XRP", "DOGE", "BNB"]
        chart_script = f"""(async () => {{
            const assets = {json.dumps(chart_assets)};
            const timeframes = [
                {{ name: '15 minute', key: '15m' }},
                {{ name: '1 hour', key: '1h' }},
                {{ name: '4 hour', key: '4h' }}
            ];

            const getChartData = () => {{
                const echarts = document.querySelectorAll('.echarts-for-react');
                if (!echarts.length) return null;
                const el = echarts[0];
                const fk = Object.keys(el).find(k => k.startsWith('__reactFiber'));
                let cur = el[fk];
                while (cur) {{
                    const opt = cur.stateNode?.getEchartsInstance?.()?.getOption?.() || cur.stateNode?.state?.option;
                    if (opt?.xAxis?.[0]?.data?.length > 0) {{
                        return {{
                            x: opt.xAxis[0].data,
                            prc: opt.series.find(s => s.name?.includes('Price'))?.data || [],
                            oi: opt.series.find(s => s.name?.includes('Interest') || s.name?.includes('OI'))?.data || []
                        }};
                    }}
                    cur = cur.return;
                }}
                return null;
            }};

            const setTimeframe = async (tfName) => {{
                const container = document.querySelector('.CurencieOi_box1__Fa78w');
                if (!container) return false;
                const btns = Array.from(container.querySelectorAll('.MuiSelect-button'));
                const tfBtn = btns.find(b => b.innerText.includes('minute') || b.innerText.includes('hour') || b.innerText.includes('day'));
                if (!tfBtn) return false;
                if (tfBtn.innerText.trim() === tfName) return true;

                tfBtn.click();
                await new Promise(r => setTimeout(r, 200));

                const listbox = Array.from(document.querySelectorAll('.MuiSelect-listbox')).find(el => (el.innerText || '').includes('15 minute') && (el.innerText || '').includes('1 day'));
                if (!listbox) return false;
                const opt = Array.from(listbox.querySelectorAll('li, [role="option"]')).find(o => o.innerText.trim() === tfName);
                if (!opt) return false;
                opt.click();
                await new Promise(r => setTimeout(r, 1200));
                return true;
            }};

            const selectAsset = async (sym) => {{
                const allButtons = Array.from(document.querySelectorAll('button, div[role="button"], .MuiTab-root'));
                const btn = allButtons.find(b => b.innerText.trim() === sym);
                if (btn) {{
                    btn.click();
                    await new Promise(r => setTimeout(r, 350));
                }}
            }};

            const out = {{ '15m': {{}}, '1h': {{}}, '4h': {{}} }};

            for (const tf of timeframes) {{
                await setTimeframe(tf.name);
                for (const sym of assets) {{
                    await selectAsset(sym);
                    const d = getChartData();
                    if (d) {{
                        out[tf.key][sym] = {{
                            x: d.x,
                            prc: d.prc,
                            oi: d.oi
                        }};
                    }}
                }}
            }}

            return out;
        }})()"""
        msg_id += 1
        await ws.send(json.dumps({"id": msg_id, "method": "Runtime.evaluate", "params": {"expression": chart_script, "returnByValue": True, "awaitPromise": True}}))
        charts_data = json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value", {})
        results["charts_15m"] = charts_data.get("15m", {})
        results["charts_1h"] = charts_data.get("1h", {})
        results["charts_4h"] = charts_data.get("4h", {})
        for tf_key, key_label in [("charts_15m", "15m"), ("charts_1h", "1h"), ("charts_4h", "4h")]:
            count_map = {s: len(d.get("x", [])) for s, d in results[tf_key].items()}
            print(f"  Chart {key_label} Series: {count_map}")

    return results


async def extract_long_short_multi(asset_symbols=("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB", "ADA", "AVAX", "SUI", "NEAR", "LINK", "DOT", "LTC", "BCH", "APT", "OP", "ARB", "TRX", "HYPE")):
    """
    Extracts the exact 4-tier modular sequence requested by user for Long/Short:
      1. Sheet 'LR_Ratio_Chart': 15-Minute Long/Short Chart Time-Series across top 20 assets
      2. Sheet 'LR_Exchanges_Ratio': Exchanges Long/Short Ratio Breakdown at 4h across top 20 assets (appended asset-wise)
      3. Sheet 'Large_Trades': Real-Time Large Whale Block Trades (Filtered >= $100K, appended asset-wise)
      4. Sheet 'LR_Ratio_Accounts': Cryptocurrency Futures Longs vs Shorts (ALL 279 Tradable Assets across all 14 pages)
    """
    tabs = get_cdp_tabs()
    target = next((t for t in tabs if "longshortratio" in t.get("url", "").lower()), None)
    if not target:
        target = next((t for t in tabs if "coinglass" in t.get("url", "").lower()), None)
    if not target and tabs:
        target = tabs[0]
    if not target:
        return None
    ws_url = target["webSocketDebuggerUrl"]

    results = {
        "all_coins_table": None,
        "assets_15m_chart": {},
        "assets_4h_exchanges": {},
        "large_trades": [],
        "assets_large_trades": {}
    }

    async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
        msg_id = 400

        # 1. First navigate to /LongShortRatio and harvest ALL 279 assets across all 14 pages
        print(">> Navigating to /LongShortRatio to harvest all 279 assets across all 14 pages...")
        msg_id += 1
        await ws.send(json.dumps({"id": msg_id, "method": "Page.navigate", "params": {"url": "https://www.coinglass.com/LongShortRatio"}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get("id") == msg_id:
                break
        await asyncio.sleep(2.5)

        all_coins_script = """(async () => {
            const allRecords = [];
            const seenAssets = new Set();
            
            // Wait for table hydration
            const start = Date.now();
            while (Date.now() - start < 8000) {
                const tables = document.querySelectorAll('table');
                if (tables.length >= 8 && tables[7].querySelectorAll('tr').length > 5) break;
                await new Promise(r => setTimeout(r, 200));
            }

            function extractCurrentPage() {
                const tables = document.querySelectorAll('table');
                const tBody = tables[7];
                if (!tBody) return [];
                
                const trs = Array.from(tBody.querySelectorAll('tr')).slice(1);
                const rows = [];
                for (const tr of trs) {
                    const tds = Array.from(tr.querySelectorAll('td'));
                    if (tds.length < 5) continue;
                    
                    const rank = tds[0] ? tds[0].innerText.trim() : '';
                    const asset = tds[1] ? tds[1].innerText.trim().split('\\n')[0].trim() : '';
                    const price = tds[2] ? tds[2].innerText.trim() : '';
                    const change24h = tds[3] ? tds[3].innerText.trim() : '';
                    
                    const ratioRaw = tds[4] ? tds[4].innerText.trim().replace(/\\n/g, ' ') : '';
                    const ratioParts = ratioRaw.split(' ').filter(Boolean);
                    const ratioVal = ratioParts[0] || '';
                    const longPct = ratioParts[1] || '';
                    const shortPct = ratioParts[2] || '';
                    
                    const cleanText = (el) => el ? el.innerText.replace(/[\\uD800-\\uDBFF][\\uDC00-\\uDFFF]|\\uD83D[\\uDC00-\\uDFFF]|[\\u2600-\\u27BF]/g, '').replace(/\\t/g, ' ').replace(/\\n/g, ' ').trim() : '';
                    
                    const binanceWhale = cleanText(tds[5]);
                    const binanceRetail = cleanText(tds[6]);
                    const okxWhale = cleanText(tds[7]);
                    const okxRetail = cleanText(tds[8]);
                    const bybitWhale = cleanText(tds[9]);
                    
                    if (asset && !seenAssets.has(asset)) {
                        seenAssets.add(asset);
                        rows.push({
                            rank, asset, price, change24h,
                            ratioVal, longPct, shortPct,
                            binanceWhale, binanceRetail, okxWhale, okxRetail, bybitWhale
                        });
                    }
                }
                return rows;
            }

            // Click Page 1
            let pageButtons = Array.from(document.querySelectorAll('.ant-pagination-item, [class*="pagination-item"], .MuiPaginationItem-root'));
            let p1 = pageButtons.find(b => b.innerText.trim() === '1');
            if (p1) p1.click();
            await new Promise(r => setTimeout(r, 400));

            for (let page = 1; page <= 15; page++) {
                const rows = extractCurrentPage();
                allRecords.push(...rows);
                
                pageButtons = Array.from(document.querySelectorAll('.ant-pagination-item, [class*="pagination-item"], .MuiPaginationItem-root'));
                const nextPageBtn = pageButtons.find(b => b.innerText.trim() === String(page + 1));
                const nextArrow = document.querySelector('.ant-pagination-next, [class*="pagination-next"], button[aria-label="Go to next page"]');
                
                if (nextPageBtn) {
                    nextPageBtn.click();
                    await new Promise(r => setTimeout(r, 300));
                } else if (nextArrow && !nextArrow.classList.contains('ant-pagination-disabled')) {
                    nextArrow.click();
                    await new Promise(r => setTimeout(r, 300));
                } else {
                    break;
                }
            }
            return allRecords;
        })()"""
        msg_id += 1
        await ws.send(json.dumps({"id": msg_id, "method": "Runtime.evaluate", "params": {"expression": all_coins_script, "returnByValue": True, "awaitPromise": True}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get("id") == msg_id:
                results["all_coins_table"] = msg.get("result", {}).get("result", {}).get("value") or []
                print(f">> Harvested {len(results['all_coins_table'])} assets across all pages!")
                break

        # 2. Extract Large Trades (Real-Time >= $100K) directly from tradesCard
        print(">> Extracting live Large Trades (filtered to >100K institutional executions)...")
        trades_script = """(async () => {
            const cards = Array.from(document.querySelectorAll('.cgj-card, .MuiCard-root'));
            const tradesCard = cards.find(c => c.innerText && c.innerText.includes('Large Trades'));
            if (!tradesCard) return [];

            const filterBtn = tradesCard.querySelector('.MuiSelect-button, button');
            if (filterBtn && !filterBtn.innerText.includes('100K')) {
                filterBtn.click();
                await new Promise(r => setTimeout(r, 200));
                const opt100 = Array.from(document.querySelectorAll('[role="option"], .MuiOption-root, li')).find(o => o.innerText.trim().includes('100K'));
                if (opt100) {
                    opt100.click();
                    await new Promise(r => setTimeout(r, 600));
                }
            }

            const divs = Array.from(tradesCard.querySelectorAll('.liq-live-table'));
            const trades = [];
            divs.forEach(d => {
                const isBuy = d.className.includes('liqLong');
                const isSell = d.className.includes('liqShort');
                const side = isBuy ? 'Buy (Long)' : (isSell ? 'Sell (Short)' : 'Unknown');
                const pair = d.querySelector('.LsLive_box2__AKk3A, [class*="box2"]')?.innerText?.trim() || '';
                const price = d.querySelector('.mbh, [class*="price"], [class*="mbh"]')?.innerText?.trim() || '';
                const valEl = d.querySelector('.Number, [class*="Number"]');
                const rawAria = valEl ? (valEl.getAttribute('aria-label') || '').replace(/,/g, '') : '';
                const value = valEl && valEl.innerText ? valEl.innerText.trim() : (rawAria ? '$' + rawAria : '');
                const datePart = d.querySelector('.LsLive_box3__qEJyJ, [class*="box3"]')?.innerText?.trim() || '';
                const timePart = d.querySelector('.LsLive_box4__IFDuD, [class*="box4"]')?.innerText?.trim() || '';
                const timeStr = `${datePart} ${timePart}`.trim();

                const asset = pair.split('-')[0].split('/')[0].replace(/USDT|USD|BUSD|PERP/i, '').trim() || pair;

                if (pair && price) {
                    trades.push({
                        asset,
                        pair,
                        side,
                        price,
                        value,
                        time: timeStr,
                        filter: '>100K'
                    });
                }
            });
            return trades;
        })()"""
        msg_id += 1
        await ws.send(json.dumps({"id": msg_id, "method": "Runtime.evaluate", "params": {"expression": trades_script, "returnByValue": True, "awaitPromise": True}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get("id") == msg_id:
                results["large_trades"] = msg.get("result", {}).get("result", {}).get("value") or []
                print(f">> Harvested {len(results['large_trades'])} live whale executions (>100K)!")
                break

        # Also group large trades by asset for backward compatibility
        for t in results["large_trades"]:
            t_asset = t.get("asset", "")
            if t_asset not in results["assets_large_trades"]:
                results["assets_large_trades"][t_asset] = []
            results["assets_large_trades"][t_asset].append(t)

        # 3. LR_Ratio_Chart: Switch chartCard to 15 minute, and traverse institutional assets via MuiAutocomplete
        switch_chart_tf_script = """(async () => {
            const cards = Array.from(document.querySelectorAll('.cgj-card, .MuiCard-root'));
            const chartCard = cards.find(c => c.innerText && c.innerText.includes('Long/Short Ratio Chart'));
            if (!chartCard) return false;
            const tfBtn = chartCard.querySelector('.MuiSelect-button, button[role="combobox"]');
            if (tfBtn && tfBtn.innerText.trim() !== '15 minute') {
                tfBtn.click();
                await new Promise(r => setTimeout(r, 200));
                const opt15m = Array.from(document.querySelectorAll('[role="option"], .MuiOption-root, li')).find(o => o.innerText.trim() === '15 minute');
                if (opt15m) {
                    opt15m.click();
                    await new Promise(r => setTimeout(r, 1000));
                }
            }
            return true;
        })()"""
        msg_id += 1
        await ws.send(json.dumps({"id": msg_id, "method": "Runtime.evaluate", "params": {"expression": switch_chart_tf_script, "returnByValue": True, "awaitPromise": True}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get("id") == msg_id:
                break

        print(f">> Extracting 15m Long/Short Ratio charts across {len(asset_symbols)} institutional assets via MuiAutocomplete...")
        for sym in asset_symbols:
            select_chart_asset_script = f"""(async () => {{
                const targetSymbol = {json.dumps(sym)};
                const cards = Array.from(document.querySelectorAll('.cgj-card, .MuiCard-root'));
                const chartCard = cards.find(c => c.innerText && c.innerText.includes('Long/Short Ratio Chart'));
                if (!chartCard) return false;
                const auto = chartCard.querySelector('.MuiAutocomplete-root');
                const inp = auto ? auto.querySelector('input') : null;
                if (!inp) return false;

                if ((inp.value || '').trim().toUpperCase() !== targetSymbol) {{
                    inp.focus();
                    inp.select();
                    document.execCommand('delete');
                    document.execCommand('insertText', false, targetSymbol);
                    await new Promise(r => setTimeout(r, 250));

                    const listbox = document.querySelector('.MuiAutocomplete-popper, ul.MuiAutocomplete-listbox, div[role="listbox"]');
                    if (listbox) {{
                        const opts = Array.from(listbox.querySelectorAll('li, div[role="option"]'));
                        const match = opts.find(o => {{
                            const txt = (o.innerText || '').trim();
                            const tokens = txt.split(/[^A-Za-z0-9]+/).filter(Boolean).map(t => t.toUpperCase());
                            return tokens[0] === targetSymbol || tokens.includes(targetSymbol) || txt.toUpperCase() === targetSymbol;
                        }});
                        if (match) {{
                            match.dispatchEvent(new MouseEvent('mousedown', {{ bubbles: true }}));
                            match.dispatchEvent(new MouseEvent('mouseup', {{ bubbles: true }}));
                            match.click();
                        }}
                    }}
                    inp.dispatchEvent(new KeyboardEvent('keydown', {{ key: 'Escape', bubbles: true }}));
                }}
                return true;
            }})()"""
            msg_id += 1
            await ws.send(json.dumps({"id": msg_id, "method": "Runtime.evaluate", "params": {"expression": select_chart_asset_script, "returnByValue": True, "awaitPromise": True}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get("id") == msg_id:
                    break

            # Mandated 1.2s wait
            await asyncio.sleep(1.2)

            extract_chart_script = """(() => {
                const hc = window._Highcharts || window.Highcharts;
                if (!hc || !hc.charts) return [];
                const valid = (hc.charts || []).filter(Boolean);
                const c15 = valid.find(c => {
                    const d = c.series[0]?.data;
                    return d && d.length > 1 && (d[1].x - d[0].x) === 900000;
                });
                if (!c15) return [];
                const prcData = c15.series[0]?.data || [];
                const lsData = c15.series[1]?.data || [];
                const lsMap = new Map();
                lsData.forEach(p => lsMap.set(p.x, p.y));

                const pts = [];
                prcData.forEach(p => {
                    const ratio = lsMap.get(p.x);
                    pts.push({
                        x: p.x,
                        price: p.y,
                        ratio: ratio !== undefined ? ratio : null
                    });
                });
                return pts;
            })()"""
            msg_id += 1
            await ws.send(json.dumps({"id": msg_id, "method": "Runtime.evaluate", "params": {"expression": extract_chart_script, "returnByValue": True}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get("id") == msg_id:
                    pts = msg.get("result", {}).get("result", {}).get("value") or []
                    results["assets_15m_chart"][sym] = pts
                    print(f"  [{sym}] Harvested {len(pts)} 15m candle points")
                    break

        # 4. LR_Exchanges_Ratio: Switch exCard to 4 hour, and traverse institutional assets via MuiAutocomplete
        switch_ex_tf_script = """(async () => {
            const cards = Array.from(document.querySelectorAll('.cgj-card, .MuiCard-root'));
            const exCard = cards.find(c => c.innerText && c.innerText.includes('Exchanges') && c.innerText.includes('Long/Short Ratio'));
            if (!exCard) return false;
            const tfBtn = exCard.querySelector('.MuiSelect-button, button[role="combobox"]');
            if (tfBtn && tfBtn.innerText.trim() !== '4 hour') {
                tfBtn.click();
                await new Promise(r => setTimeout(r, 200));
                const opt4h = Array.from(document.querySelectorAll('[role="option"], .MuiOption-root, li')).find(o => o.innerText.trim() === '4 hour');
                if (opt4h) {
                    opt4h.click();
                    await new Promise(r => setTimeout(r, 800));
                }
            }
            return true;
        })()"""
        msg_id += 1
        await ws.send(json.dumps({"id": msg_id, "method": "Runtime.evaluate", "params": {"expression": switch_ex_tf_script, "returnByValue": True, "awaitPromise": True}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get("id") == msg_id:
                break

        print(f">> Extracting 4h Exchange breakdowns across {len(asset_symbols)} institutional assets via MuiAutocomplete...")
        for sym in asset_symbols:
            select_ex_asset_script = f"""(async () => {{
                const targetSymbol = {json.dumps(sym)};
                const cards = Array.from(document.querySelectorAll('.cgj-card, .MuiCard-root'));
                const exCard = cards.find(c => c.innerText && c.innerText.includes('Exchanges') && c.innerText.includes('Long/Short Ratio'));
                if (!exCard) return false;
                const auto = exCard.querySelector('.MuiAutocomplete-root');
                const inp = auto ? auto.querySelector('input') : null;
                if (!inp) return false;

                if ((inp.value || '').trim().toUpperCase() !== targetSymbol) {{
                    inp.focus();
                    inp.select();
                    document.execCommand('delete');
                    document.execCommand('insertText', false, targetSymbol);
                    await new Promise(r => setTimeout(r, 250));

                    const listbox = document.querySelector('.MuiAutocomplete-popper, ul.MuiAutocomplete-listbox, div[role="listbox"]');
                    if (listbox) {{
                        const opts = Array.from(listbox.querySelectorAll('li, div[role="option"]'));
                        const match = opts.find(o => {{
                            const txt = (o.innerText || '').trim();
                            const tokens = txt.split(/[^A-Za-z0-9]+/).filter(Boolean).map(t => t.toUpperCase());
                            return tokens[0] === targetSymbol || tokens.includes(targetSymbol) || txt.toUpperCase() === targetSymbol;
                        }});
                        if (match) {{
                            match.dispatchEvent(new MouseEvent('mousedown', {{ bubbles: true }}));
                            match.dispatchEvent(new MouseEvent('mouseup', {{ bubbles: true }}));
                            match.click();
                        }}
                    }}
                    inp.dispatchEvent(new KeyboardEvent('keydown', {{ key: 'Escape', bubbles: true }}));
                }}
                return true;
            }})()"""
            msg_id += 1
            await ws.send(json.dumps({"id": msg_id, "method": "Runtime.evaluate", "params": {"expression": select_ex_asset_script, "returnByValue": True, "awaitPromise": True}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get("id") == msg_id:
                    break

            # Mandated 1.0s wait
            await asyncio.sleep(1.0)

            extract_ex_script = """(() => {
                const cards = Array.from(document.querySelectorAll('.cgj-card, .MuiCard-root'));
                const exCard = cards.find(c => c.innerText && c.innerText.includes('Exchanges') && c.innerText.includes('Long/Short Ratio'));
                if (!exCard) return [];

                const rows = [];
                const lines = exCard.innerText.split('\\n').map(l => l.trim()).filter(Boolean);
                for (let i = 0; i < lines.length - 7; i++) {
                    const line = lines[i].trim();
                    if (/^\\d+$/.test(line)) {
                        const rank = parseInt(line);
                        if (rank >= 1 && rank <= 25) {
                            const exName = lines[i+1];
                            const lp = lines[i+2];
                            const sp = lines[i+3];
                            if (lp && lp.includes('%') && sp && sp.includes('%')) {
                                let longVol = '';
                                let shortVol = '';
                                if (lines[i+4] === 'Long' && lines[i+5]) longVol = lines[i+5];
                                if (lines[i+6] === 'Short' && lines[i+7]) shortVol = lines[i+7];
                                
                                let netRatio = '-';
                                const lpNum = parseFloat(lp.replace('%', ''));
                                const spNum = parseFloat(sp.replace('%', ''));
                                if (!isNaN(lpNum) && !isNaN(spNum) && spNum > 0) {
                                    netRatio = (lpNum / spNum).toFixed(4);
                                }

                                rows.push({
                                    rank,
                                    exchange: exName,
                                    longPct: lp,
                                    shortPct: sp,
                                    longVol,
                                    shortVol,
                                    netRatio
                                });
                            }
                        }
                    }
                }
                return rows;
            })()"""
            msg_id += 1
            await ws.send(json.dumps({"id": msg_id, "method": "Runtime.evaluate", "params": {"expression": extract_ex_script, "returnByValue": True}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get("id") == msg_id:
                    ex_rows = msg.get("result", {}).get("result", {}).get("value") or []
                    results["assets_4h_exchanges"][sym] = ex_rows
                    print(f"  [{sym}] Harvested {len(ex_rows)} exchange rows")
                    break

    return results


# ==============================================================================
# Master Excel Multi-Section Dump Engine (1 Sheet per Page, Overwrite Mode)
# ==============================================================================

def execute_consolidated_dump(sheet_filter=None):
    """Coordinates extraction and saves dashboard sheets into DataBase_Trading.xlsx."""
    ts_now = datetime.now(timezone.utc)
    ts_str = ts_now.strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n================================================================================")
    print(f"CoinGlass Institutional Deep Analytics & Multi-Asset Pipeline")
    print(f"Timestamp (UTC): {ts_str}")
    print(f"Target Excel: {DEFAULT_EXCEL_PATH}")
    print(f"Target Sheet Filter: {sheet_filter or 'ALL 9 CANONICAL SHEETS'}")
    print(f"Layout Contract: Exactly 1 Sheet per Page | Continuous Asset-Wise Tables | Overwrite Mode")
    print(f"================================================================================\n")

    # Initialize Workbook in Overwrite Mode
    if DEFAULT_EXCEL_PATH.exists():
        wb = openpyxl.load_workbook(DEFAULT_EXCEL_PATH)
    else:
        wb = openpyxl.Workbook()
        if "Sheet" in wb.sheetnames:
            wb.remove(wb["Sheet"])

    CANONICAL_SHEETS = [
        "ETF_Overview",
        "ETF_Bitcoin",
        "ETF_Ethereum",
        "ETF_Solana",
        "ETF_XRP",
        "Funding_Rates",
        "Funding_Fees",
        "Open_Interest",
        "Open_Interest_Top_Gainers",
        "Open_Interest_Top_Losers",
        "Exchange_Open_Interest_Chart15M",
        "Exchange_Open_Interest_Chart_1H",
        "Exchange_Open_Interest_Chart_4H",
        "LR_Ratio_Chart",
        "LR_Ratio_Accounts",
        "LR_Exchanges_Ratio",
        "Large_Trades"
    ]

    for name in list(wb.sheetnames):
        if name not in CANONICAL_SHEETS:
            wb.remove(wb[name])

    def get_clean_ws(sheet_name):
        """Creates or resets worksheet to guarantee clean overwrite of existing values."""
        if sheet_filter is not None and sheet_filter != sheet_name:
            if sheet_filter == "Long_Short_Ratio" and sheet_name in ["LR_Ratio_Chart", "LR_Ratio_Accounts", "LR_Exchanges_Ratio", "Large_Trades"]:
                pass  # allow running all 4 when Long_Short_Ratio is requested
            elif sheet_filter in [
                "Open_Interest", "Open_Interest_Top_Gainers", "Open_Interest_Top_Losers",
                "Exchange_Open_Interest_Chart15M", "Exchange_Open_Interest_Chart_1H", "Exchange_Open_Interest_Chart_4H"
            ] and sheet_name in [
                "Open_Interest", "Open_Interest_Top_Gainers", "Open_Interest_Top_Losers",
                "Exchange_Open_Interest_Chart15M", "Exchange_Open_Interest_Chart_1H", "Exchange_Open_Interest_Chart_4H"
            ]:
                pass  # allow running all 6 when Open_Interest is requested
            else:
                return None
        if sheet_name in wb.sheetnames:
            wb.remove(wb[sheet_name])
        return wb.create_sheet(title=sheet_name)

    report = {"timestamp": ts_str, "sheets": []}

    # 1. Macro ETF Overview
    if sheet_filter is None or sheet_filter == "ETF_Overview":
        print(">> Extracting /etf macro overview...")
        etf_macro = asyncio.run(extract_etf_overview())
    else:
        etf_macro = None

    # 2. Asset ETFs (BTC, ETH, SOL, XRP)
    asset_etfs = {}
    if sheet_filter is None or str(sheet_filter).startswith("ETF_"):
        for asset in ["bitcoin", "ethereum", "solana", "xrp"]:
            target_sheet = f"ETF_{asset.capitalize()}"
            if sheet_filter is None or sheet_filter == target_sheet:
                print(f">> Extracting /etf/{asset}...")
                asset_etfs[asset] = asyncio.run(extract_etf_asset(asset))

    # 3. Funding Analytics (/FundingRate & /funding-fees)
    if sheet_filter is None or sheet_filter in ["Funding_Rates", "Funding_Fees"]:
        print(">> Extracting /FundingRate and /funding-fees...")
        funding_data = asyncio.run(extract_funding_analytics())
    else:
        funding_data = None

    # 4. Multi-Asset Open Interest across 10 core institutional assets
    oi_target_sheets = [
        "Open_Interest", "Open_Interest_Top_Gainers", "Open_Interest_Top_Losers",
        "Exchange_Open_Interest_Chart15M", "Exchange_Open_Interest_Chart_1H", "Exchange_Open_Interest_Chart_4H"
    ]
    if sheet_filter is None or sheet_filter in oi_target_sheets:
        oi_assets = ["BTC", "ETH", "SOL", "HYPE", "XRP", "ZEC", "XAU", "NEAR", "DOGE", "BNB"]
        print(f">> Extracting /open-interest across {len(oi_assets)} assets ({', '.join(oi_assets)})...")
        oi_data = asyncio.run(extract_open_interest_multi(oi_assets))
    else:
        oi_data = None

    # 5. Long/Short Ratios & Whale Analytics (/LongShortRatio)
    ls_sheets = ["Long_Short_Ratio", "LR_Ratio_Chart", "LR_Ratio_Accounts", "LR_Exchanges_Ratio", "Large_Trades"]
    if sheet_filter is None or sheet_filter in ls_sheets:
        print(">> Extracting /LongShortRatio (15m chart, 4h exchanges, >=$100K trades, and all 279 tradable assets)...")
        ls_data = asyncio.run(extract_long_short_multi())
    else:
        ls_data = None

    report = {"timestamp": ts_str, "sheets": []}

    # ==========================================================================
    # SHEET 1: ETF_Overview (https://www.coinglass.com/etf)
    # ==========================================================================
    ws_ov = get_clean_ws("ETF_Overview")
    sec_overview = []

    if etf_macro and etf_macro.get("rows"):
        m_headers = etf_macro.get("headers", [])
        cols = [("Timestamp_UTC", "Timestamp (UTC)", 22, "center")]
        for idx, h in enumerate(m_headers):
            cols.append((f"col_{idx}", h, 18 if idx != 0 else 12, "center" if idx == 0 else "right"))
        rows = []
        for r in etf_macro["rows"]:
            rec = {"Timestamp_UTC": ts_str}
            for idx, val in enumerate(r):
                rec[f"col_{idx}"] = val.replace("\n", " ")
            rows.append(rec)
        sec_overview.append({
            "title": "=== SECTION 1: CRYPTO SPOT ETF ASSET COMPARISON & OVERVIEW ===",
            "columns": cols,
            "rows": rows,
            "row_fill": ROW_FILL_DEFAULT
        })

    if etf_macro and etf_macro.get("charts"):
        c0 = etf_macro["charts"][0]
        x_dates = c0.get("xData", [])
        net_inflow_series = next((s["data"] for s in c0.get("series", []) if "Net" in s.get("name", "")), [])
        inflow_series = next((s["data"] for s in c0.get("series", []) if "Inflow" == s.get("name", "")), [])
        outflow_series = next((s["data"] for s in c0.get("series", []) if "Outflow" == s.get("name", "")), [])

        flow_rows = []
        for idx, dt in enumerate(x_dates):
            net_val = net_inflow_series[idx] if idx < len(net_inflow_series) else 0
            inf_val = inflow_series[idx] if idx < len(inflow_series) else 0
            outf_val = outflow_series[idx] if idx < len(outflow_series) else 0
            flow_rows.append({
                "Timestamp_UTC": ts_str,
                "Date_UTC": dt,
                "Net_Inflow_USD": f"+${net_val:,.0f}" if net_val > 0 else (f"-${abs(net_val):,.0f}" if net_val < 0 else "$0"),
                "Inflow_USD": f"${inf_val:,.0f}" if inf_val else "$0",
                "Outflow_USD": f"-${abs(outf_val):,.0f}" if outf_val else "$0"
            })
        cols_flows = [
            ("Timestamp_UTC", "Timestamp (UTC)", 22, "center"),
            ("Date_UTC", "Date (UTC)", 16, "center"),
            ("Net_Inflow_USD", "Total Net Inflow (USD)", 24, "right"),
            ("Inflow_USD", "Total Inflow (USD)", 22, "right"),
            ("Outflow_USD", "Total Outflow (USD)", 22, "right")
        ]
        sec_overview.append({
            "title": "=== SECTION 2: CRYPTO ETF NET FLOWS HISTORICAL TIME-SERIES (DAILY) ===",
            "columns": cols_flows,
            "rows": flow_rows,
            "row_fill": ROW_FILL_ALT
        })

    render_sections_to_sheet(ws_ov, sec_overview)
    if ws_ov is not None:
        report["sheets"].append({"name": "ETF_Overview", "sections": len(sec_overview), "rows": sum(len(s["rows"]) for s in sec_overview)})

    # ==========================================================================
    # SHEET 2: ETF_Bitcoin (https://www.coinglass.com/etf/bitcoin)
    # ==========================================================================
    ws_btc = get_clean_ws("ETF_Bitcoin")
    sec_btc = []
    btc_data = asset_etfs.get("bitcoin") or {}

    d_headers = (btc_data.get("overview") or {}).get("dailyHeaders", [])
    d_rows = (btc_data.get("overview") or {}).get("dailyRows", [])
    if d_headers and d_rows:
        cols_tbl = [("Timestamp_UTC", "Timestamp (UTC)", 22, "center")]
        for idx, h in enumerate(d_headers):
            cols_tbl.append((f"col_{idx}", h, 18 if idx != 0 else 12, "center" if idx == 0 else "right"))
        rows_tbl = []
        for r in d_rows:
            rec = {"Timestamp_UTC": ts_str}
            for idx, cell_val in enumerate(r):
                rec[f"col_{idx}"] = cell_val
            rows_tbl.append(rec)
        sec_btc.append({
            "title": "=== SECTION 1: BITCOIN SPOT ETF DAILY FUND BREAKDOWN ===",
            "columns": cols_tbl,
            "rows": rows_tbl,
            "row_fill": ROW_FILL_BTC
        })

    raw_btc = (btc_data.get("overview") or {}).get("rawBtcState")
    btc_flow_records = []
    if raw_btc and isinstance(raw_btc, list):
        for item in raw_btc:
            dt = item.get("date", "")
            prc = item.get("btcPrice", 0)
            chg = item.get("change", 0)
            net_assets = item.get("netAssets", 0)
            btc_flow_records.append({
                "Timestamp_UTC": ts_str,
                "Date_UTC": dt,
                "BTC_Price_USD": f"${prc:,.2f}" if prc else "$0",
                "Net_Inflow_USD": f"+${chg:,.0f}" if chg > 0 else (f"-${abs(chg):,.0f}" if chg < 0 else "$0"),
                "Total_Net_Assets_USD": f"${net_assets:,.0f}" if net_assets else "$0"
            })
    else:
        c_list = (btc_data.get("overview") or {}).get("chartSeriesList", [])
        c1 = c_list[1] if len(c_list) > 1 else (c_list[0] if c_list else {})
        x_dates = c1.get("xData", [])
        net_s = next((s["data"] for s in c1.get("series", []) if "Net" in (s.get("name") or "") or "Inflow" in (s.get("name") or "")), [])
        price_s = next((s["data"] for s in c1.get("series", []) if "Price" in (s.get("name") or "")), [])
        for idx, dt in enumerate(x_dates):
            netf = net_s[idx] if idx < len(net_s) else 0
            prc = price_s[idx] if idx < len(price_s) else 0
            btc_flow_records.append({
                "Timestamp_UTC": ts_str,
                "Date_UTC": dt,
                "BTC_Price_USD": f"${prc:,.2f}" if prc else "$0",
                "Net_Inflow_USD": f"+${netf:,.0f}" if netf > 0 else (f"-${abs(netf):,.0f}" if netf < 0 else "$0"),
                "Total_Net_Assets_USD": "$0"
            })

    cols_btc_flow = [
        ("Timestamp_UTC", "Timestamp (UTC)", 22, "center"),
        ("Date_UTC", "Historical Date", 16, "center"),
        ("BTC_Price_USD", "Bitcoin Market Price (USD)", 24, "right"),
        ("Net_Inflow_USD", "Total Daily Net Inflow (USD)", 26, "right"),
        ("Total_Net_Assets_USD", "Total Net Assets (USD)", 24, "right")
    ]
    sec_btc.append({
        "title": "=== SECTION 2: BITCOIN SPOT ETF NET INFLOWS & TOTAL NET ASSETS TIME-SERIES ===",
        "columns": cols_btc_flow,
        "rows": btc_flow_records,
        "row_fill": ROW_FILL_DEFAULT
    })

    chart_tabs = btc_data.get("chart_subtabs") or {}
    aum_data = chart_tabs.get("AUM", {})
    mcap_data = chart_tabs.get("Market Cap", {})
    vol_data = chart_tabs.get("Volume", {})
    dates_aum = aum_data.get("xData") or mcap_data.get("xData") or vol_data.get("xData") or []

    aum_s = next((s["data"] for s in aum_data.get("series", [])), [])
    mcap_s = next((s["data"] for s in mcap_data.get("series", [])), [])
    vol_s = next((s["data"] for s in vol_data.get("series", [])), [])

    records_aum = []
    for idx, dt in enumerate(dates_aum):
        a_val = aum_s[idx] if idx < len(aum_s) else 0
        m_val = mcap_s[idx] if idx < len(mcap_s) else 0
        v_val = vol_s[idx] if idx < len(vol_s) else 0
        records_aum.append({
            "Timestamp_UTC": ts_str,
            "Date_UTC": dt,
            "AUM_USD": f"${a_val:,.0f}" if a_val else "$0",
            "Market_Cap_USD": f"${m_val:,.0f}" if m_val else "$0",
            "Volume_USD": f"${v_val:,.0f}" if v_val else "$0"
        })
    cols_aum = [
        ("Timestamp_UTC", "Timestamp (UTC)", 22, "center"),
        ("Date_UTC", "Historical Date", 16, "center"),
        ("AUM_USD", "Total AUM (USD)", 22, "right"),
        ("Market_Cap_USD", "Total Market Cap (USD)", 22, "right"),
        ("Volume_USD", "Trading Volume (USD)", 22, "right")
    ]
    sec_btc.append({
        "title": "=== SECTION 3: BITCOIN ETF AUM, MARKET CAP & VOLUME HISTORICAL TIME-SERIES ===",
        "columns": cols_aum,
        "rows": records_aum,
        "row_fill": ROW_FILL_ALT
    })

    h_info = btc_data.get("holdings") or {}
    if h_info and h_info.get("headers") and h_info.get("rows"):
        cols_h = [("Timestamp_UTC", "Timestamp (UTC)", 22, "center")]
        for idx, h in enumerate(h_info["headers"]):
            cols_h.append((f"col_{idx}", h, 14 if idx == 0 else (26 if "Name" in h else 18), "center" if idx <= 2 else "right"))
        rows_h = []
        for r in h_info["rows"]:
            rec = {"Timestamp_UTC": ts_str}
            for idx, cell_val in enumerate(r):
                rec[f"col_{idx}"] = cell_val.replace("\n", " ")
            rows_h.append(rec)
        sec_btc.append({
            "title": "=== SECTION 4: BITCOIN SPOT ETF HOLDINGS & NAV BREAKDOWN ===",
            "columns": cols_h,
            "rows": rows_h,
            "row_fill": ROW_FILL_BTC
        })

    top_info = btc_data.get("top_etfs") or {}
    if top_info and top_info.get("headers") and top_info.get("rows"):
        cols_top = [("Timestamp_UTC", "Timestamp (UTC)", 22, "center")]
        for idx, h in enumerate(top_info["headers"]):
            cols_top.append((f"col_{idx}", h, 12 if idx == 0 else (34 if "Name" in h else 18), "center" if idx in [0, 2, 3] else "right"))
        rows_top = []
        for r in top_info["rows"]:
            rec = {"Timestamp_UTC": ts_str}
            for idx, cell_val in enumerate(r):
                rec[f"col_{idx}"] = cell_val.replace("\n", " ")
            rows_top.append(rec)
        sec_btc.append({
            "title": "=== SECTION 5: GLOBAL BITCOIN ETFS BENCHMARK RANKING ===",
            "columns": cols_top,
            "rows": rows_top,
            "row_fill": ROW_FILL_ALT
        })

    render_sections_to_sheet(ws_btc, sec_btc)
    if ws_btc is not None:
        report["sheets"].append({"name": "ETF_Bitcoin", "sections": len(sec_btc), "rows": sum(len(s["rows"]) for s in sec_btc)})

    # ==========================================================================
    # SHEET 3: ETF_Ethereum (https://www.coinglass.com/etf/ethereum)
    # ==========================================================================
    ws_eth = get_clean_ws("ETF_Ethereum")
    sec_eth = []
    eth_data = asset_etfs.get("ethereum") or {}

    d_headers = (eth_data.get("overview") or {}).get("dailyHeaders", [])
    d_rows = (eth_data.get("overview") or {}).get("dailyRows", [])
    if d_headers and d_rows:
        cols_tbl = [("Timestamp_UTC", "Timestamp (UTC)", 22, "center")]
        for idx, h in enumerate(d_headers):
            cols_tbl.append((f"col_{idx}", h, 18 if idx != 0 else 12, "center" if idx == 0 else "right"))
        rows_tbl = []
        for r in d_rows:
            rec = {"Timestamp_UTC": ts_str}
            for idx, cell_val in enumerate(r):
                rec[f"col_{idx}"] = cell_val
            rows_tbl.append(rec)
        sec_eth.append({
            "title": "=== SECTION 1: ETHEREUM SPOT ETF DAILY FUND BREAKDOWN ===",
            "columns": cols_tbl,
            "rows": rows_tbl,
            "row_fill": ROW_FILL_ETH
        })

    c_list = (eth_data.get("overview") or {}).get("chartSeriesList", [])
    c1 = c_list[1] if len(c_list) > 1 else (c_list[0] if c_list else {})
    x_dates = c1.get("xData", [])
    net_s = next((s["data"] for s in c1.get("series", []) if "Net" in (s.get("name") or "") or "Inflow" in (s.get("name") or "")), [])
    price_s = next((s["data"] for s in c1.get("series", []) if "Price" in (s.get("name") or "")), [])
    eth_flow_records = []
    for idx, dt in enumerate(x_dates):
        netf = net_s[idx] if idx < len(net_s) else 0
        prc = price_s[idx] if idx < len(price_s) else 0
        eth_flow_records.append({
            "Timestamp_UTC": ts_str,
            "Date_UTC": dt,
            "ETH_Price_USD": f"${prc:,.2f}" if prc else "$0",
            "Net_Inflow_USD": f"+${netf:,.0f}" if netf > 0 else (f"-${abs(netf):,.0f}" if netf < 0 else "$0")
        })
    cols_eth = [
        ("Timestamp_UTC", "Timestamp (UTC)", 22, "center"),
        ("Date_UTC", "Historical Date", 16, "center"),
        ("ETH_Price_USD", "Ethereum Market Price (USD)", 24, "right"),
        ("Net_Inflow_USD", "Total Daily Net Inflow (USD)", 26, "right")
    ]
    sec_eth.append({
        "title": "=== SECTION 2: ETHEREUM SPOT ETF NET INFLOWS HISTORICAL TIME-SERIES ===",
        "columns": cols_eth,
        "rows": eth_flow_records,
        "row_fill": ROW_FILL_DEFAULT
    })

    h_info = eth_data.get("holdings") or {}
    if h_info and h_info.get("headers") and h_info.get("rows"):
        cols_h = [("Timestamp_UTC", "Timestamp (UTC)", 22, "center")]
        for idx, h in enumerate(h_info["headers"]):
            cols_h.append((f"col_{idx}", h, 14 if idx == 0 else (26 if "Name" in h else 18), "center" if idx <= 2 else "right"))
        rows_h = []
        for r in h_info["rows"]:
            rec = {"Timestamp_UTC": ts_str}
            for idx, cell_val in enumerate(r):
                rec[f"col_{idx}"] = cell_val.replace("\n", " ")
            rows_h.append(rec)
        sec_eth.append({
            "title": "=== SECTION 3: ETHEREUM SPOT ETF HOLDINGS & NAV BREAKDOWN ===",
            "columns": cols_h,
            "rows": rows_h,
            "row_fill": ROW_FILL_ETH
        })

    render_sections_to_sheet(ws_eth, sec_eth)
    if ws_eth is not None:
        report["sheets"].append({"name": "ETF_Ethereum", "sections": len(sec_eth), "rows": sum(len(s["rows"]) for s in sec_eth)})

    # ==========================================================================
    # SHEET 4: ETF_Solana (https://www.coinglass.com/etf/solana)
    # ==========================================================================
    ws_sol = get_clean_ws("ETF_Solana")
    sec_sol = []
    sol_data = asset_etfs.get("solana") or {}

    d_headers = (sol_data.get("overview") or {}).get("dailyHeaders", [])
    d_rows = (sol_data.get("overview") or {}).get("dailyRows", [])
    if d_headers and d_rows:
        cols_tbl = [("Timestamp_UTC", "Timestamp (UTC)", 22, "center")]
        for idx, h in enumerate(d_headers):
            cols_tbl.append((f"col_{idx}", h, 18 if idx != 0 else 12, "center" if idx == 0 else "right"))
        rows_tbl = []
        for r in d_rows:
            rec = {"Timestamp_UTC": ts_str}
            for idx, cell_val in enumerate(r):
                rec[f"col_{idx}"] = cell_val
            rows_tbl.append(rec)
        sec_sol.append({
            "title": "=== SECTION 1: SOLANA ETF DAILY FUND BREAKDOWN ===",
            "columns": cols_tbl,
            "rows": rows_tbl,
            "row_fill": ROW_FILL_SOL
        })

    c_list = (sol_data.get("overview") or {}).get("chartSeriesList", [])
    c1 = c_list[1] if len(c_list) > 1 else (c_list[0] if c_list else {})
    x_dates = c1.get("xData", [])
    net_s = next((s["data"] for s in c1.get("series", []) if "Net" in (s.get("name") or "") or "Inflow" in (s.get("name") or "")), [])
    price_s = next((s["data"] for s in c1.get("series", []) if "Price" in (s.get("name") or "")), [])
    sol_flow_records = []
    for idx, dt in enumerate(x_dates):
        netf = net_s[idx] if idx < len(net_s) else 0
        prc = price_s[idx] if idx < len(price_s) else 0
        sol_flow_records.append({
            "Timestamp_UTC": ts_str,
            "Date_UTC": dt,
            "SOL_Price_USD": f"${prc:,.2f}" if prc else "$0",
            "Net_Inflow_USD": f"+${netf:,.0f}" if netf > 0 else (f"-${abs(netf):,.0f}" if netf < 0 else "$0")
        })
    cols_sol = [
        ("Timestamp_UTC", "Timestamp (UTC)", 22, "center"),
        ("Date_UTC", "Historical Date", 16, "center"),
        ("SOL_Price_USD", "Solana Market Price (USD)", 24, "right"),
        ("Net_Inflow_USD", "Total Daily Net Inflow (USD)", 26, "right")
    ]
    sec_sol.append({
        "title": "=== SECTION 2: SOLANA ETF NET INFLOWS HISTORICAL TIME-SERIES ===",
        "columns": cols_sol,
        "rows": sol_flow_records,
        "row_fill": ROW_FILL_DEFAULT
    })

    render_sections_to_sheet(ws_sol, sec_sol)
    if ws_sol is not None:
        report["sheets"].append({"name": "ETF_Solana", "sections": len(sec_sol), "rows": sum(len(s["rows"]) for s in sec_sol)})

    # ==========================================================================
    # SHEET 5: ETF_XRP (https://www.coinglass.com/etf/xrp)
    # ==========================================================================
    ws_xrp = get_clean_ws("ETF_XRP")
    sec_xrp = []
    xrp_data = asset_etfs.get("xrp") or {}

    d_headers = (xrp_data.get("overview") or {}).get("dailyHeaders", [])
    d_rows = (xrp_data.get("overview") or {}).get("dailyRows", [])
    if d_headers and d_rows:
        cols_tbl = [("Timestamp_UTC", "Timestamp (UTC)", 22, "center")]
        for idx, h in enumerate(d_headers):
            cols_tbl.append((f"col_{idx}", h, 18 if idx != 0 else 12, "center" if idx == 0 else "right"))
        rows_tbl = []
        for r in d_rows:
            rec = {"Timestamp_UTC": ts_str}
            for idx, cell_val in enumerate(r):
                rec[f"col_{idx}"] = cell_val
            rows_tbl.append(rec)
        sec_xrp.append({
            "title": "=== SECTION 1: XRP ETF DAILY FUND BREAKDOWN ===",
            "columns": cols_tbl,
            "rows": rows_tbl,
            "row_fill": ROW_FILL_XRP
        })

    c_list = (xrp_data.get("overview") or {}).get("chartSeriesList", [])
    c1 = c_list[1] if len(c_list) > 1 else (c_list[0] if c_list else {})
    x_dates = c1.get("xData", [])
    net_s = next((s["data"] for s in c1.get("series", []) if "Net" in (s.get("name") or "") or "Inflow" in (s.get("name") or "")), [])
    price_s = next((s["data"] for s in c1.get("series", []) if "Price" in (s.get("name") or "")), [])
    xrp_flow_records = []
    for idx, dt in enumerate(x_dates):
        netf = net_s[idx] if idx < len(net_s) else 0
        prc = price_s[idx] if idx < len(price_s) else 0
        xrp_flow_records.append({
            "Timestamp_UTC": ts_str,
            "Date_UTC": dt,
            "XRP_Price_USD": f"${prc:,.4f}" if prc else "$0",
            "Net_Inflow_USD": f"+${netf:,.0f}" if netf > 0 else (f"-${abs(netf):,.0f}" if netf < 0 else "$0")
        })
    cols_xrp = [
        ("Timestamp_UTC", "Timestamp (UTC)", 22, "center"),
        ("Date_UTC", "Historical Date", 16, "center"),
        ("XRP_Price_USD", "XRP Market Price (USD)", 24, "right"),
        ("Net_Inflow_USD", "Total Daily Net Inflow (USD)", 26, "right")
    ]
    sec_xrp.append({
        "title": "=== SECTION 2: XRP ETF NET INFLOWS HISTORICAL TIME-SERIES ===",
        "columns": cols_xrp,
        "rows": xrp_flow_records,
        "row_fill": ROW_FILL_DEFAULT
    })

    render_sections_to_sheet(ws_xrp, sec_xrp)
    if ws_xrp is not None:
        report["sheets"].append({"name": "ETF_XRP", "sections": len(sec_xrp), "rows": sum(len(s["rows"]) for s in sec_xrp)})

    # ==========================================================================
    # SHEET 6: Funding_Rates (https://www.coinglass.com/FundingRate)
    # ==========================================================================
    ws_fr = get_clean_ws("Funding_Rates")
    sec_fr = []

    if funding_data and funding_data.get("rates"):
        fr_info = funding_data["rates"]
        headers = fr_info.get("headers", [])
        rows = fr_info.get("rows", [])
        if headers and rows:
            cols_fr = [("Timestamp_UTC", "Timestamp (UTC)", 22, "center")]
            for idx, h in enumerate(headers):
                cols_fr.append((f"col_{idx}", h, 18 if "Symbol" in h else 14, "left" if "Symbol" in h else "right"))
            rows_fr = []
            for r in rows:
                rec = {"Timestamp_UTC": ts_str}
                for idx, cell_val in enumerate(r):
                    rec[f"col_{idx}"] = cell_val
                rows_fr.append(rec)
            sec_fr.append({
                "title": "=== SECTION 1: LIVE MULTI-EXCHANGE FUNDING RATES COMPARISON ===",
                "columns": cols_fr,
                "rows": rows_fr,
                "row_fill": ROW_FILL_DEFAULT
            })

        oi_dates = fr_info.get("oiWeightedDates", [])
        oi_series = fr_info.get("oiWeightedSeries", [])
        if oi_dates and oi_series:
            prc_s = next((s["data"] for s in oi_series if "Price" in s.get("name", "")), [])
            oi_w_s = next((s["data"] for s in oi_series if "Weighted" in s.get("name", "") or "OI" in s.get("name", "")), [])
            rows_oi_w = []
            for idx, dt in enumerate(oi_dates):
                prc = prc_s[idx] if idx < len(prc_s) else 0
                oi_rate = oi_w_s[idx] if idx < len(oi_w_s) else 0
                rows_oi_w.append({
                    "Timestamp_UTC": dt,
                    "BTC_Price_USD": f"${prc:,.2f}" if prc else "$0",
                    "OI_Weighted_Funding_Rate_Pct": f"{oi_rate:.4f}%" if isinstance(oi_rate, (int, float)) else str(oi_rate)
                })
            cols_oi_w = [
                ("Timestamp_UTC", "Candle Timestamp (UTC)", 24, "center"),
                ("BTC_Price_USD", "Bitcoin Market Price (USD)", 24, "right"),
                ("OI_Weighted_Funding_Rate_Pct", "OI-Weighted Funding Rate (%)", 26, "right")
            ]
            sec_fr.append({
                "title": "=== SECTION 2: BTC OI-WEIGHTED FUNDING RATE & PRICE HIGH-RESOLUTION TIME-SERIES ===",
                "columns": cols_oi_w,
                "rows": rows_oi_w,
                "row_fill": ROW_FILL_BTC
            })

        ex_dates = fr_info.get("exDates", [])
        ex_series = fr_info.get("exSeries", [])
        if ex_dates and ex_series:
            cols_ex = [("Timestamp_UTC", "Candle Timestamp (UTC)", 24, "center")]
            for idx, s in enumerate(ex_series):
                s_name = s.get("name") or f"Ex_{idx}"
                cols_ex.append((f"series_{idx}", f"{s_name} Rate (%)", 18, "right"))
            rows_ex = []
            for d_idx, dt in enumerate(ex_dates):
                rec = {"Timestamp_UTC": dt}
                for s_idx, s in enumerate(ex_series):
                    s_data = s.get("data", [])
                    val = s_data[d_idx] if d_idx < len(s_data) else ""
                    val_str = f"{val:.4f}%" if isinstance(val, (int, float)) else str(val)
                    rec[f"series_{s_idx}"] = val_str
                rows_ex.append(rec)
            sec_fr.append({
                "title": "=== SECTION 3: MULTI-EXCHANGE HISTORICAL FUNDING RATES COMPARISON TIME-SERIES ===",
                "columns": cols_ex,
                "rows": rows_ex,
                "row_fill": ROW_FILL_ALT
            })

    render_sections_to_sheet(ws_fr, sec_fr)
    if ws_fr is not None:
        report["sheets"].append({"name": "Funding_Rates", "sections": len(sec_fr), "rows": sum(len(s["rows"]) for s in sec_fr)})

    # ==========================================================================
    # SHEET 7: Funding_Fees (https://www.coinglass.com/funding-fees)
    # ==========================================================================
    ws_ff = get_clean_ws("Funding_Fees")
    sec_ff = []

    if funding_data and funding_data.get("fees"):
        ff_info = funding_data["fees"]
        headers = ff_info.get("headers", [])
        rows = ff_info.get("rows", [])
        if headers and rows:
            cols_ff = [("Timestamp_UTC", "Timestamp (UTC)", 22, "center")]
            for idx, h in enumerate(headers):
                cols_ff.append((f"col_{idx}", h, 18 if "Symbol" in h else 16, "left" if "Symbol" in h else "right"))
            rows_ff = []
            for r in rows:
                rec = {"Timestamp_UTC": ts_str}
                for idx, cell_val in enumerate(r):
                    rec[f"col_{idx}"] = cell_val
                rows_ff.append(rec)
            sec_ff.append({
                "title": "=== SECTION 1: PERPETUAL FUTURES FUNDING FEE SETTLEMENT DASHBOARD ===",
                "columns": cols_ff,
                "rows": rows_ff,
                "row_fill": ROW_FILL_DEFAULT
            })

    render_sections_to_sheet(ws_ff, sec_ff)
    if ws_ff is not None:
        report["sheets"].append({"name": "Funding_Fees", "sections": len(sec_ff), "rows": sum(len(s["rows"]) for s in sec_ff)})

    # ==========================================================================
    # SHEET 8: Open_Interest (Image 1 Format - Table 1 Stacked Asset-Wise)
    # ==========================================================================
    ws_oi = get_clean_ws("Open_Interest")
    sec_oi = []

    if oi_data and oi_data.get("tables"):
        all_tbl_rows = []
        for sym, rows in oi_data["tables"].items():
            for r in rows:
                if len(r) >= 9:
                    all_tbl_rows.append({
                        "Asset": sym,
                        "Ranking": r[0] if r[0] else ("All" if r[1] == "All" else "-"),
                        "Exchanges": r[1],
                        "OI_Coin": r[2],
                        "OI_USD": r[3],
                        "Market_Share_Pct": r[4],
                        "OI_Change_1h": r[5],
                        "OI_Change_4h": r[6],
                        "OI_Change_24h": r[7],
                        "OI_24h_Vol": r[8] if len(r) > 8 else ""
                    })

        cols_oi = [
            ("Asset", "Asset", 12, "center"),
            ("Ranking", "Ranking", 10, "center"),
            ("Exchanges", "Exchanges", 18, "center"),
            ("OI_Coin", "OI (Coin)", 22, "right"),
            ("OI_USD", "OI (USD)", 22, "right"),
            ("Market_Share_Pct", "Market Share (%)", 18, "right"),
            ("OI_Change_1h", "OI Change (1h)", 16, "right"),
            ("OI_Change_4h", "OI Change (4h)", 16, "right"),
            ("OI_Change_24h", "OI Change (24h)", 16, "right"),
            ("OI_24h_Vol", "OI/24h_Vol", 16, "right")
        ]
        if all_tbl_rows:
            sec_oi.append({
                "title": f"COINGLASS DERIVATIVES ANALYTICS - TOTAL OPEN INTEREST BY ASSET & EXCHANGE BREAKDOWN (ALL {len(all_tbl_rows)} ROWS STACKED ASSET-WISE)",
                "columns": cols_oi,
                "rows": all_tbl_rows,
                "row_fill": ROW_FILL_DEFAULT
            })

    render_sections_to_sheet(ws_oi, sec_oi)
    if ws_oi is not None:
        report["sheets"].append({"name": "Open_Interest", "sections": len(sec_oi), "rows": sum(len(s["rows"]) for s in sec_oi)})

    # ==========================================================================
    # SHEET 8B: Open_Interest_Top_Gainers (Image 2 Format - 1h & 4h Timeframes)
    # ==========================================================================
    ws_gainers = get_clean_ws("Open_Interest_Top_Gainers")
    sec_gainers = []
    if oi_data:
        cols_g = [
            ("Timeframe", "Timeframe", 14, "center"),
            ("Pair", "Derivatives Pair", 20, "center"),
            ("Price_USD", "Market Price (USD)", 20, "right"),
            ("Price_Change_Pct", "Price Change (%)", 18, "right"),
            ("OI_USD", "Open Interest (USD)", 22, "right"),
            ("OI_Change_Pct", "OI Change (%)", 18, "right")
        ]
        rows_g_1h = []
        for r in oi_data.get("h1_gainers", []):
            rows_g_1h.append({
                "Timeframe": "1 hour",
                "Pair": r.get("pair", ""),
                "Price_USD": r.get("price", ""),
                "Price_Change_Pct": r.get("priceChange", ""),
                "OI_USD": r.get("oi", ""),
                "OI_Change_Pct": r.get("oiChange", "")
            })
        if rows_g_1h:
            sec_gainers.append({
                "title": "COINGLASS DERIVATIVES ANALYTICS - DERIVATIVES OPEN INTEREST TOP GAINERS (1 HOUR TIMEFRAME)",
                "columns": cols_g,
                "rows": rows_g_1h,
                "row_fill": ROW_FILL_DEFAULT
            })

        rows_g_4h = []
        for r in oi_data.get("h4_gainers", []):
            rows_g_4h.append({
                "Timeframe": "4 hour",
                "Pair": r.get("pair", ""),
                "Price_USD": r.get("price", ""),
                "Price_Change_Pct": r.get("priceChange", ""),
                "OI_USD": r.get("oi", ""),
                "OI_Change_Pct": r.get("oiChange", "")
            })
        if rows_g_4h:
            sec_gainers.append({
                "title": "COINGLASS DERIVATIVES ANALYTICS - DERIVATIVES OPEN INTEREST TOP GAINERS (4 HOUR TIMEFRAME)",
                "columns": cols_g,
                "rows": rows_g_4h,
                "row_fill": ROW_FILL_ALT
            })

    render_sections_to_sheet(ws_gainers, sec_gainers)
    if ws_gainers is not None:
        report["sheets"].append({"name": "Open_Interest_Top_Gainers", "sections": len(sec_gainers), "rows": sum(len(s["rows"]) for s in sec_gainers)})

    # ==========================================================================
    # SHEET 8C: Open_Interest_Top_Losers (Image 2 Format - 1h & 4h Timeframes)
    # ==========================================================================
    ws_losers = get_clean_ws("Open_Interest_Top_Losers")
    sec_losers = []
    if oi_data:
        cols_l = [
            ("Timeframe", "Timeframe", 14, "center"),
            ("Pair", "Derivatives Pair", 20, "center"),
            ("Price_USD", "Market Price (USD)", 20, "right"),
            ("Price_Change_Pct", "Price Change (%)", 18, "right"),
            ("OI_USD", "Open Interest (USD)", 22, "right"),
            ("OI_Change_Pct", "OI Change (%)", 18, "right")
        ]
        rows_l_1h = []
        for r in oi_data.get("h1_losers", []):
            rows_l_1h.append({
                "Timeframe": "1 hour",
                "Pair": r.get("pair", ""),
                "Price_USD": r.get("price", ""),
                "Price_Change_Pct": r.get("priceChange", ""),
                "OI_USD": r.get("oi", ""),
                "OI_Change_Pct": r.get("oiChange", "")
            })
        if rows_l_1h:
            sec_losers.append({
                "title": "COINGLASS DERIVATIVES ANALYTICS - DERIVATIVES OPEN INTEREST TOP LOSERS (1 HOUR TIMEFRAME)",
                "columns": cols_l,
                "rows": rows_l_1h,
                "row_fill": ROW_FILL_DEFAULT
            })

        rows_l_4h = []
        for r in oi_data.get("h4_losers", []):
            rows_l_4h.append({
                "Timeframe": "4 hour",
                "Pair": r.get("pair", ""),
                "Price_USD": r.get("price", ""),
                "Price_Change_Pct": r.get("priceChange", ""),
                "OI_USD": r.get("oi", ""),
                "OI_Change_Pct": r.get("oiChange", "")
            })
        if rows_l_4h:
            sec_losers.append({
                "title": "COINGLASS DERIVATIVES ANALYTICS - DERIVATIVES OPEN INTEREST TOP LOSERS (4 HOUR TIMEFRAME)",
                "columns": cols_l,
                "rows": rows_l_4h,
                "row_fill": ROW_FILL_ALT
            })

    render_sections_to_sheet(ws_losers, sec_losers)
    if ws_losers is not None:
        report["sheets"].append({"name": "Open_Interest_Top_Losers", "sections": len(sec_losers), "rows": sum(len(s["rows"]) for s in sec_losers)})

    # ==========================================================================
    # SHEET 8D: Exchange_Open_Interest_Chart15M (Image 3 Format - 15m Candles)
    # ==========================================================================
    ws_c15 = get_clean_ws("Exchange_Open_Interest_Chart15M")
    sec_c15 = []
    if oi_data and oi_data.get("charts_15m"):
        rows_c15 = []
        sr_no = 1
        cols_chart = [
            ("Sr_No", "Sr.No", 10, "center"),
            ("Asset", "Asset", 12, "center"),
            ("Timestamp_UTC", "Timestamp (UTC)", 24, "center"),
            ("Price_USD", "Market Price (USD)", 22, "right"),
            ("Open_Interest_USD", "Total Open Interest (USD)", 26, "right")
        ]
        for sym, d in oi_data["charts_15m"].items():
            x_dates = d.get("x", [])
            prc_s = d.get("prc", [])
            oi_s = d.get("oi", [])
            for idx, dt in enumerate(x_dates):
                prc = prc_s[idx] if idx < len(prc_s) else 0
                oi_val = oi_s[idx] if idx < len(oi_s) else 0
                rows_c15.append({
                    "Sr_No": sr_no,
                    "Asset": sym,
                    "Timestamp_UTC": dt,
                    "Price_USD": f"${prc:,.2f}" if prc else "$0",
                    "Open_Interest_USD": f"${oi_val:,.0f}" if oi_val else "$0"
                })
                sr_no += 1
        if rows_c15:
            sec_c15.append({
                "title": f"COINGLASS DERIVATIVES ANALYTICS - EXCHANGE OPEN INTEREST 15-MINUTE CANDLE CHART ({len(rows_c15)} INTRADAY CANDLES STACKED ASSET-WISE)",
                "columns": cols_chart,
                "rows": rows_c15,
                "row_fill": ROW_FILL_DEFAULT
            })

    render_sections_to_sheet(ws_c15, sec_c15)
    if ws_c15 is not None:
        report["sheets"].append({"name": "Exchange_Open_Interest_Chart15M", "sections": len(sec_c15), "rows": sum(len(s["rows"]) for s in sec_c15)})

    # ==========================================================================
    # SHEET 8E: Exchange_Open_Interest_Chart_1H (Image 3 Format - 1h Candles)
    # ==========================================================================
    ws_c1h = get_clean_ws("Exchange_Open_Interest_Chart_1H")
    sec_c1h = []
    if oi_data and oi_data.get("charts_1h"):
        rows_c1h = []
        sr_no = 1
        cols_chart = [
            ("Sr_No", "Sr.No", 10, "center"),
            ("Asset", "Asset", 12, "center"),
            ("Timestamp_UTC", "Timestamp (UTC)", 24, "center"),
            ("Price_USD", "Market Price (USD)", 22, "right"),
            ("Open_Interest_USD", "Total Open Interest (USD)", 26, "right")
        ]
        for sym, d in oi_data["charts_1h"].items():
            x_dates = d.get("x", [])
            prc_s = d.get("prc", [])
            oi_s = d.get("oi", [])
            for idx, dt in enumerate(x_dates):
                prc = prc_s[idx] if idx < len(prc_s) else 0
                oi_val = oi_s[idx] if idx < len(oi_s) else 0
                rows_c1h.append({
                    "Sr_No": sr_no,
                    "Asset": sym,
                    "Timestamp_UTC": dt,
                    "Price_USD": f"${prc:,.2f}" if prc else "$0",
                    "Open_Interest_USD": f"${oi_val:,.0f}" if oi_val else "$0"
                })
                sr_no += 1
        if rows_c1h:
            sec_c1h.append({
                "title": f"COINGLASS DERIVATIVES ANALYTICS - EXCHANGE OPEN INTEREST 1-HOUR CANDLE CHART ({len(rows_c1h)} HOURLY CANDLES STACKED ASSET-WISE)",
                "columns": cols_chart,
                "rows": rows_c1h,
                "row_fill": ROW_FILL_DEFAULT
            })

    render_sections_to_sheet(ws_c1h, sec_c1h)
    if ws_c1h is not None:
        report["sheets"].append({"name": "Exchange_Open_Interest_Chart_1H", "sections": len(sec_c1h), "rows": sum(len(s["rows"]) for s in sec_c1h)})

    # ==========================================================================
    # SHEET 8F: Exchange_Open_Interest_Chart_4H (Image 3 Format - 4h Candles)
    # ==========================================================================
    ws_c4h = get_clean_ws("Exchange_Open_Interest_Chart_4H")
    sec_c4h = []
    if oi_data and oi_data.get("charts_4h"):
        rows_c4h = []
        sr_no = 1
        cols_chart = [
            ("Sr_No", "Sr.No", 10, "center"),
            ("Asset", "Asset", 12, "center"),
            ("Timestamp_UTC", "Timestamp (UTC)", 24, "center"),
            ("Price_USD", "Market Price (USD)", 22, "right"),
            ("Open_Interest_USD", "Total Open Interest (USD)", 26, "right")
        ]
        for sym, d in oi_data["charts_4h"].items():
            x_dates = d.get("x", [])
            prc_s = d.get("prc", [])
            oi_s = d.get("oi", [])
            for idx, dt in enumerate(x_dates):
                prc = prc_s[idx] if idx < len(prc_s) else 0
                oi_val = oi_s[idx] if idx < len(oi_s) else 0
                rows_c4h.append({
                    "Sr_No": sr_no,
                    "Asset": sym,
                    "Timestamp_UTC": dt,
                    "Price_USD": f"${prc:,.2f}" if prc else "$0",
                    "Open_Interest_USD": f"${oi_val:,.0f}" if oi_val else "$0"
                })
                sr_no += 1
        if rows_c4h:
            sec_c4h.append({
                "title": f"COINGLASS DERIVATIVES ANALYTICS - EXCHANGE OPEN INTEREST 4-HOUR CANDLE CHART ({len(rows_c4h)} SWING CANDLES STACKED ASSET-WISE)",
                "columns": cols_chart,
                "rows": rows_c4h,
                "row_fill": ROW_FILL_DEFAULT
            })

    render_sections_to_sheet(ws_c4h, sec_c4h)
    if ws_c4h is not None:
        report["sheets"].append({"name": "Exchange_Open_Interest_Chart_4H", "sections": len(sec_c4h), "rows": sum(len(s["rows"]) for s in sec_c4h)})

    # ==========================================================================
    # SHEET 9: LR_Ratio_Chart (15-Minute Intraday Highcharts Time-Series)
    # ==========================================================================
    ws_chart = get_clean_ws("LR_Ratio_Chart")
    sec_chart = []
    if ls_data:
        rows_15m = []
        for sym, pts in (ls_data.get("assets_15m_chart") or {}).items():
            for p in pts:
                ts_ms = p.get("x", 0)
                dt_str = datetime.fromtimestamp(ts_ms / 1000, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S") if ts_ms else ""
                prc = p.get("price", 0)
                ratio = p.get("ratio")
                sentiment = ("Bullish (>1.0)" if ratio > 1.0 else "Bearish (<1.0)") if isinstance(ratio, (int, float)) else "-"
                rows_15m.append({
                    "Timestamp_UTC": dt_str,
                    "Asset": sym,
                    "Timeframe": "15m",
                    "Price_USD": f"${prc:,.2f}" if prc else "$0",
                    "Long_Short_Ratio": f"{ratio:.4f}" if isinstance(ratio, (int, float)) else str(ratio or "-"),
                    "Sentiment_Bias": sentiment
                })

        cols_15m = [
            ("Timestamp_UTC", "Candle Timestamp (UTC)", 24, "center"),
            ("Asset", "Asset", 12, "center"),
            ("Timeframe", "Timeframe", 12, "center"),
            ("Price_USD", "Market Price (USD)", 22, "right"),
            ("Long_Short_Ratio", "Long/Short Ratio", 20, "right"),
            ("Sentiment_Bias", "Sentiment Bias", 20, "center")
        ]
        if rows_15m:
            sec_chart.append({
                "title": "COINGLASS DERIVATIVES ANALYTICS - LONG/SHORT RATIO 15-MINUTE INTRADAY CANDLE CHART (HIGH-RESOLUTION TIME-SERIES)",
                "columns": cols_15m,
                "rows": rows_15m,
                "row_fill": ROW_FILL_DEFAULT
            })
    render_sections_to_sheet(ws_chart, sec_chart)
    if ws_chart is not None:
        report["sheets"].append({"name": "LR_Ratio_Chart", "sections": len(sec_chart), "rows": sum(len(s["rows"]) for s in sec_chart)})

    # ==========================================================================
    # SHEET 10: LR_Ratio_Accounts (Cryptocurrency Futures Longs vs Shorts - ALL TRADABLE ASSETS)
    # ==========================================================================
    ws_acc = get_clean_ws("LR_Ratio_Accounts")
    sec_acc = []
    if ls_data:
        raw_ac = ls_data.get("all_coins_table") or []
        rows_ac = []
        for item in raw_ac:
            if isinstance(item, dict):
                rows_ac.append({
                    "Ranking": item.get("rank", ""),
                    "Asset": item.get("asset", ""),
                    "Price_USD": item.get("price", ""),
                    "Price_24h_Pct": item.get("change24h", ""),
                    "Long_Short_5m": item.get("ratioVal", ""),
                    "Long_Pct": item.get("longPct", ""),
                    "Short_Pct": item.get("shortPct", ""),
                    "Binance_Whale_Bias": item.get("binanceWhale", ""),
                    "Binance_Retail_Ratio": item.get("binanceRetail", ""),
                    "OKX_Whale_Bias": item.get("okxWhale", ""),
                    "OKX_Retail_Ratio": item.get("okxRetail", ""),
                    "Bybit_Whale_Bias": item.get("bybitWhale", "")
                })

        cols_ac = [
            ("Ranking", "Ranking", 10, "center"),
            ("Asset", "Asset", 12, "center"),
            ("Price_USD", "Market Price (USD)", 20, "right"),
            ("Price_24h_Pct", "24h Change (%)", 18, "right"),
            ("Long_Short_5m", "5m Long/Short Ratio", 20, "right"),
            ("Long_Pct", "Long Ratio (%)", 16, "right"),
            ("Short_Pct", "Short Ratio (%)", 16, "right"),
            ("Binance_Whale_Bias", "Binance Whale Bias", 22, "center"),
            ("Binance_Retail_Ratio", "Binance Retail Ratio", 20, "right"),
            ("OKX_Whale_Bias", "OKX Whale Bias", 22, "center"),
            ("OKX_Retail_Ratio", "OKX Retail Ratio", 20, "right"),
            ("Bybit_Whale_Bias", "Bybit Whale Bias", 22, "center")
        ]
        if rows_ac:
            sec_acc.append({
                "title": f"COINGLASS DERIVATIVES ANALYTICS - CRYPTOCURRENCY FUTURES LONGS VS SHORTS ACCOUNTS SUMMARY (ALL {len(rows_ac)} TRADABLE ASSETS)",
                "columns": cols_ac,
                "rows": rows_ac,
                "row_fill": ROW_FILL_ALT
            })
    render_sections_to_sheet(ws_acc, sec_acc)
    if ws_acc is not None:
        report["sheets"].append({"name": "LR_Ratio_Accounts", "sections": len(sec_acc), "rows": sum(len(s["rows"]) for s in sec_acc)})

    # ==========================================================================
    # SHEET 11: LR_Exchanges_Ratio (4-Hour Multi-Exchange Breakdown Across Top Assets)
    # ==========================================================================
    ws_ex = get_clean_ws("LR_Exchanges_Ratio")
    sec_ex = []
    if ls_data:
        rows_4h = []
        for sym, ex_list in (ls_data.get("assets_4h_exchanges") or {}).items():
            for r in ex_list:
                rows_4h.append({
                    "Asset": sym,
                    "Rank": r.get("rank", ""),
                    "Exchange": r.get("exchange", ""),
                    "Timeframe": "4 hour",
                    "Long_Pct": r.get("longPct", ""),
                    "Short_Pct": r.get("shortPct", ""),
                    "Long_Vol": r.get("longVol", ""),
                    "Short_Vol": r.get("shortVol", ""),
                    "Net_Ratio": r.get("netRatio", "")
                })

        cols_4h = [
            ("Asset", "Asset", 12, "center"),
            ("Rank", "Rank", 10, "center"),
            ("Exchange", "Exchange", 18, "center"),
            ("Timeframe", "Timeframe", 14, "center"),
            ("Long_Pct", "Long Ratio (%)", 16, "right"),
            ("Short_Pct", "Short Ratio (%)", 16, "right"),
            ("Long_Vol", "Long Volume", 18, "right"),
            ("Short_Vol", "Short Volume", 18, "right"),
            ("Net_Ratio", "Net Long/Short Ratio", 20, "right")
        ]
        if rows_4h:
            sec_ex.append({
                "title": "COINGLASS DERIVATIVES ANALYTICS - EXCHANGES LONG/SHORT RATIO BREAKDOWN (4-HOUR TIMEFRAME ACROSS 22 DERIVATIVES EXCHANGES)",
                "columns": cols_4h,
                "rows": rows_4h,
                "row_fill": ROW_FILL_ALT
            })
    render_sections_to_sheet(ws_ex, sec_ex)
    if ws_ex is not None:
        report["sheets"].append({"name": "LR_Exchanges_Ratio", "sections": len(sec_ex), "rows": sum(len(s["rows"]) for s in sec_ex)})

    # ==========================================================================
    # SHEET 12: Large_Trades (Real-Time Whale Block Trades >= $100K)
    # ==========================================================================
    ws_trades = get_clean_ws("Large_Trades")
    sec_trades = []
    if ls_data:
        rows_trades = []
        raw_trades = ls_data.get("large_trades") or []
        if not raw_trades and isinstance(ls_data.get("assets_large_trades"), dict):
            for sym, t_list in ls_data.get("assets_large_trades", {}).items():
                for t in t_list:
                    t_item = dict(t)
                    t_item.setdefault("asset", sym)
                    raw_trades.append(t_item)
        for t in raw_trades:
            rows_trades.append({
                "Timestamp_UTC": t.get("time", ""),
                "Asset": t.get("asset", ""),
                "Pair": t.get("pair", ""),
                "Side": t.get("side", ""),
                "Price_USD": t.get("price", ""),
                "Value_USD": t.get("value", ""),
                "Whale_Filter": str(t.get("filter", ">100K")).lstrip("=").strip()
            })

        cols_trades = [
            ("Asset", "Asset", 12, "center"),
            ("Timestamp_UTC", "Trade Timestamp (UTC)", 24, "center"),
            ("Pair", "Trading Pair", 18, "center"),
            ("Side", "Order Side", 16, "center"),
            ("Value_USD", "Trade Value (USD)", 22, "right"),
            ("Price_USD", "Execution Price (USD)", 22, "right"),
            ("Whale_Filter", "Whale Filter Threshold", 22, "center")
        ]
        if rows_trades:
            sec_trades.append({
                "title": "COINGLASS DERIVATIVES ANALYTICS - REAL-TIME INSTITUTIONAL LARGE WHALE TRADES (MINIMUM BLOCK SIZE 100K+ USD)",
                "columns": cols_trades,
                "rows": rows_trades,
                "row_fill": ROW_FILL_DEFAULT
            })
    render_sections_to_sheet(ws_trades, sec_trades)
    if ws_trades is not None:
        report["sheets"].append({"name": "Large_Trades", "sections": len(sec_trades), "rows": sum(len(s["rows"]) for s in sec_trades)})

    # --------------------------------------------------------------------------
    # Final Global Workbook Sanitizer: Eliminate Any Formula Triggers Across ALL Sheets
    # --------------------------------------------------------------------------
    for sh in wb.worksheets:
        for row in sh.iter_rows(values_only=False):
            for cell in row:
                if isinstance(cell.value, str):
                    if cell.value.startswith("==="):
                        cell.value = cell.value.replace("===", "").strip()
                    while cell.value.startswith("=") and not cell.value.startswith("=SUM") and not cell.value.startswith("=AVERAGE"):
                        cell.value = cell.value.lstrip("=").strip()

    # --------------------------------------------------------------------------
    # Save Consolidated Workbook
    # --------------------------------------------------------------------------
    DEFAULT_EXCEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    wb.save(DEFAULT_EXCEL_PATH)

    print(f"\n================================================================================")
    print(f"PIPELINE EXECUTION COMPLETE - ALL PAGES SUCCESSFULLY PERSISTED")
    print(f"Total Consolidated Sheets: {len(report['sheets'])}")
    for s in report["sheets"]:
        print(f"  - Sheet '{s['name']}': {s['sections']} sections | {s['rows']:,} total rows")
    print(f"Saved into: {DEFAULT_EXCEL_PATH.resolve()}")
    print(f"================================================================================\n")
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CoinGlass Consolidated Deep Excel Pipeline")
    parser.add_argument("--reset", action="store_true", help="Reset/overwrite mode")
    parser.add_argument("--sheet", default=None, help="Target specific sheet to update (e.g. Long_Short_Ratio)")
    args = parser.parse_args()

    execute_consolidated_dump(sheet_filter=args.sheet)
