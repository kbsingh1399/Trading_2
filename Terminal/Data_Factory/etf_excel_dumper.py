"""
CoinGlass Multi-Asset Spot ETF Excel Automation & Tabular Storage Pipeline
========================================================================
Extracts ALL crypto ETF assets and telemetry from https://www.coinglass.com/etf
via Chrome CDP (or local snapshot fallback), capturing:
  1. All 41+ individual institutional ETFs (BTC, ETH, SOL, XRP, HYPE, MULTI)
  2. Top Institutions (Blackrock, Grayscale, Fidelity, Bitwise, 21 Shares, VanEck)
  3. Macro Market Overview by Asset Category and Global Flow Performance Windows

Canonical Target: Data/DataBase_Trading.xlsx
Sheets:
  1. Crypto_ETF_Flows      - Full 41+ ETF directory across ALL assets
  2. Top_Institutions      - Institutional sponsors, total net inflows, and ETF counts
  3. ETF_Market_Overview   - Asset category aggregates and macro flow performance metrics
"""

import os
import sys
import json
import asyncio
import urllib.request
import argparse
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
DEFAULT_SNAPSHOT_PATH = Path("Data/coinglass/latest/coinglass_snapshot.json")
FULL_SNAPSHOT_PATH = Path("Data/coinglass/latest/coinglass_etf_full_snapshot.json")
SHEET_ALL_ETFS = "Crypto_ETF_Flows"
SHEET_INSTITUTIONS = "Top_Institutions"
SHEET_OVERVIEW = "ETF_Market_Overview"
CDP_BASE_URL = "http://127.0.0.1:9222"

# Generous column schemas - never formatted to save space
ETF_COLUMNS = [
    ("Timestamp_UTC", "Timestamp (UTC)", 24, "center"),
    ("Date", "Date", 14, "center"),
    ("Asset", "Asset Category", 16, "center"),
    ("Rank", "Rank", 10, "center"),
    ("Ticker", "Ticker", 14, "center"),
    ("ETF_Name", "Fund Name", 45, "left"),
    ("Issuer", "Issuer / Sponsor", 28, "left"),
    ("Price_USD", "Market Price (USD)", 18, "right"),
    ("Price_Change", "Price Change", 18, "right"),
    ("Daily_Net_Inflow", "Daily Net Inflow", 20, "right"),
    ("AUM_USD", "Total Assets Under Management AUM (USD)", 26, "right"),
    ("Market_Cap_USD", "Market Capitalization (USD)", 24, "right"),
    ("Daily_Volume_USD", "Daily Trading Volume (USD)", 22, "right"),
    ("Volume_Shares", "Trading Volume (Shares)", 20, "right"),
    ("Turnover_Rate", "Turnover Rate", 16, "right"),
    ("Shares_Outstanding", "Shares Outstanding", 20, "right"),
    ("Expense_Ratio", "Expense Ratio / Fee", 18, "right"),
    ("Status", "Trading Status", 16, "center")
]

INSTITUTION_COLUMNS = [
    ("Timestamp_UTC", "Timestamp (UTC)", 24, "center"),
    ("Date", "Date", 14, "center"),
    ("Rank", "Rank", 10, "center"),
    ("Institution_Name", "Institution / Sponsor Name", 28, "left"),
    ("Total_Net_Inflow_USD", "Total Cumulative Net Inflow (USD)", 26, "right"),
    ("Total_ETF_Count", "Total Active ETF Count", 20, "center")
]

OVERVIEW_COLUMNS = [
    ("Timestamp_UTC", "Timestamp (UTC)", 24, "center"),
    ("Date", "Date", 14, "center"),
    ("Asset_Category", "Asset Category", 20, "left"),
    ("Netflow_24h_USD", "24h Netflow (USD)", 22, "right"),
    ("Total_AUM_USD", "Total AUM (USD)", 24, "right"),
    ("Active_ETF_Count", "Active ETF Count", 18, "center"),
    ("Top_Leader_Ticker", "Flow Leader Ticker", 20, "center"),
    ("Leader_Netflow_USD", "Leader Netflow (USD)", 22, "right"),
    ("Global_24h_Netflow", "Global 24h Netflow (USD)", 24, "right"),
    ("Global_Total_AUM", "Global Total AUM (USD)", 24, "right"),
    ("Flow_Last_Week", "Flow Last Week (USD)", 22, "right"),
    ("Flow_Last_Month", "Flow Last Month (USD)", 22, "right"),
    ("Flow_Last_Quarter", "Flow Last Quarter (USD)", 24, "right"),
    ("Yearly_Strongest_Month", "Yearly Strongest Month", 24, "center"),
    ("Yearly_Weakest_Month", "Yearly Weakest Month", 24, "center")
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

def deduce_asset(ticker: str, name: str, explicit_tag: str) -> str:
    if explicit_tag:
        tag = explicit_tag.upper().strip()
        if "," in tag:
            return "Multi-Asset"
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
    if "crypto" in n or "index" in n or "basket" in n:
        return "Multi-Asset"
    return "Other Crypto"

async def fetch_live_etf_via_cdp():
    """Extracts live ETF data across ALL assets, Top Institutions, and KPIs via Chrome CDP on port 9222."""
    if not websockets:
        return None, None, None
    try:
        tabs_data = urllib.request.urlopen(f"{CDP_BASE_URL}/json", timeout=3).read().decode()
        tabs = json.loads(tabs_data)
        etf_tabs = [t for t in tabs if "etf" in t.get("url", "").lower() and t.get("type") == "page"]
        if not etf_tabs:
            return None, None, None
        ws_url = etf_tabs[0]["webSocketDebuggerUrl"]
    except Exception:
        return None, None, None

    try:
        async with websockets.connect(ws_url, max_size=25*1024*1024) as ws:
            # 1. Expand Show All button if present
            click_cmd = {
                "id": 1,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": """
                    (() => {
                        const btnShowAll = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === 'Show All');
                        if (btnShowAll) {
                            btnShowAll.click();
                            return true;
                        }
                        return false;
                    })()
                    """,
                    "returnByValue": True
                }
            }
            await ws.send(json.dumps(click_cmd))
            await ws.recv()
            await asyncio.sleep(0.8)

            # 2. Extract DOM data including tables, Top Institutions, and Global KPIs
            extract_cmd = {
                "id": 2,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": """
                    (() => {
                        const tables = Array.from(document.querySelectorAll('table'));
                        if (tables.length === 0) return null;

                        // Table 0: Top ETF Netflows by category
                        const t0Rows = Array.from(tables[0].querySelectorAll('tr')).map(tr => 
                            Array.from(tr.querySelectorAll('td, th')).map(c => c.innerText.trim())
                        ).filter(r => r.length >= 2 && r[0] !== 'ETF' && r[0] !== '');

                        // Table 1: Market summary by Asset Category
                        const t1Rows = Array.from(tables[1].querySelectorAll('tr')).map(tr => 
                            Array.from(tr.querySelectorAll('td, th')).map(c => c.innerText.trim())
                        ).filter(r => r.length >= 3 && r[0] !== 'ETF' && r[0] !== '');

                        // Table 2: All ETFs List (expanded)
                        const t2 = tables[tables.length - 1];
                        const t2Rows = Array.from(t2.querySelectorAll('tr')).map(tr => 
                            Array.from(tr.querySelectorAll('td')).map(c => c.innerText.trim())
                        ).filter(r => r.length >= 4 && r[0] !== '');

                        // Top Institutions extraction
                        const institutions = [];
                        const text = document.body.innerText;
                        const lines = text.split('\\n');
                        let startIdx = -1;
                        for (let i = 0; i < lines.length; i++) {
                            if (lines[i].trim() === 'Top Institutions') {
                                startIdx = i;
                                break;
                            }
                        }
                        if (startIdx !== -1) {
                            let i = startIdx + 1;
                            while (i < lines.length && !lines[i].includes('Crypto ETF Overview') && institutions.length < 15) {
                                const name = lines[i].trim();
                                if (name && !name.includes(':') && lines[i+1] && lines[i+1].includes('Total Net Inflow')) {
                                    const inflowVal = lines[i+1].replace('Total Net Inflow :', '').replace('Total Net Inflow:', '').trim();
                                    const countVal = lines[i+2] ? lines[i+2].replace('ETF Count :', '').replace('ETF Count:', '').trim() : '';
                                    institutions.push({
                                        institution: name,
                                        total_net_inflow: inflowVal,
                                        etf_count: countVal
                                    });
                                    i += 3;
                                } else {
                                    i++;
                                }
                            }
                        }

                        // Global KPIs
                        let kpis = {};
                        for (let i = 0; i < lines.length; i++) {
                            const l = lines[i].trim();
                            if (l === 'Crypto ETF Net Inflow' && lines[i+1]) kpis['net_inflow_24h'] = lines[i+1].trim();
                            if (l === 'Total Crypto ETF AUM' && lines[i+1]) kpis['total_aum'] = lines[i+1].trim();
                            if (l === 'Number of Active Crypto ETFs' && lines[i+1]) kpis['active_etfs_count'] = lines[i+1].trim();
                            if (l === 'Active ETF Issuers' && lines[i+1]) kpis['active_issuers_count'] = lines[i+1].trim();
                            if (l === 'Last Week' && lines[i+1]) kpis['flow_last_week'] = lines[i+1].trim();
                            if (l === 'Last Month' && lines[i+1]) kpis['flow_last_month'] = lines[i+1].trim();
                            if (l === 'Last Quarter' && lines[i+1]) kpis['flow_last_quarter'] = lines[i+1].trim();
                            if (l === 'Strongest month' && lines[i+1]) {
                                kpis['strongest_month_val'] = lines[i+1].trim();
                                if (lines[i+2]) kpis['strongest_month_date'] = lines[i+2].trim();
                            }
                            if (l === 'Weakest month' && lines[i+1]) {
                                kpis['weakest_month_val'] = lines[i+1].trim();
                                if (lines[i+2]) kpis['weakest_month_date'] = lines[i+2].trim();
                            }
                        }

                        return { t0Rows, t1Rows, t2Rows, institutions, kpis };
                    })()
                    """,
                    "returnByValue": True
                }
            }
            await ws.send(json.dumps(extract_cmd))
            resp = await ws.recv()
            data = json.loads(resp).get("result", {}).get("result", {}).get("value")
            if not data:
                return None, None, None

            # 3. Also extract HYPE ETFs tab if present to guarantee 100% asset coverage
            hype_rows = []
            try:
                hype_click_cmd = {
                    "id": 3,
                    "method": "Runtime.evaluate",
                    "params": {
                        "expression": """
                        (() => {
                            const btnHype = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === 'HYPE ETFs');
                            if (btnHype) {
                                btnHype.click();
                                return true;
                            }
                            return false;
                        })()
                        """,
                        "returnByValue": True
                    }
                }
                await ws.send(json.dumps(hype_click_cmd))
                await ws.recv()

                hype_extract_cmd = {
                    "id": 4,
                    "method": "Runtime.evaluate",
                    "params": {
                        "expression": """
                        (() => {
                            const tables = Array.from(document.querySelectorAll('table'));
                            const t2 = tables[tables.length - 1];
                            return Array.from(t2.querySelectorAll('tbody tr')).map(tr => 
                                Array.from(tr.querySelectorAll('td')).map(td => td.innerText.trim())
                            ).filter(r => r.length >= 3 && r[1] && r[1] !== 'Ticker' && r[1] !== 'No data');
                        })()
                        """,
                        "returnByValue": True
                    }
                }

                # Wait up to 3 seconds for AJAX rows to populate
                for _ in range(6):
                    await asyncio.sleep(0.5)
                    await ws.send(json.dumps(hype_extract_cmd))
                    resp_hype = await ws.recv()
                    val = json.loads(resp_hype).get("result", {}).get("result", {}).get("value") or []
                    if val and any(len(r) >= 2 and any(tk in r[1] for tk in ["BHYP", "THYP", "HYPG"]) for r in val):
                        hype_rows = val
                        break

                # Restore back to All Crypto ETFs tab and expand if needed
                restore_cmd = {
                    "id": 5,
                    "method": "Runtime.evaluate",
                    "params": {
                        "expression": """
                        (() => {
                            const btnAll = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === 'All Crypto ETFs');
                            if (btnAll) btnAll.click();
                            setTimeout(() => {
                                const btnShowAll = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === 'Show All');
                                if (btnShowAll) btnShowAll.click();
                            }, 300);
                            return true;
                        })()
                        """,
                        "returnByValue": True
                    }
                }
                await ws.send(json.dumps(restore_cmd))
                await ws.recv()
                await asyncio.sleep(0.4)
            except Exception as e_hype:
                print(f"HYPE ETF extraction warning: {e_hype}")

            now_dt = datetime.now(timezone.utc)
            ts_str = now_dt.strftime("%Y-%m-%d %H:%M:%S UTC")
            date_str = now_dt.strftime("%Y-%m-%d")

            # Leaders mapping (Table 0)
            leaders = {}
            for r in data.get("t0Rows", []):
                parts = r[0].split()
                cat = parts[0]
                ticker = parts[1] if len(parts) > 1 else ""
                leaders[cat.lower()] = {"ticker": ticker, "flow": r[1]}

            kpis = data.get("kpis", {})
            strongest_str = f"{kpis.get('strongest_month_val', '')} ({kpis.get('strongest_month_date', '')})" if kpis.get('strongest_month_val') else ""
            weakest_str = f"{kpis.get('weakest_month_val', '')} ({kpis.get('weakest_month_date', '')})" if kpis.get('weakest_month_val') else ""

            # 1. Market Overview (Table 1 + KPIs)
            overview_records = []
            for r in data.get("t1Rows", []):
                asset_cat = r[0]
                netflow = r[1]
                aum = r[2]
                count = r[3]
                ldr = leaders.get(asset_cat.lower(), {})
                overview_records.append({
                    "Timestamp_UTC": ts_str,
                    "Date": date_str,
                    "Asset_Category": asset_cat,
                    "Netflow_24h_USD": netflow,
                    "Total_AUM_USD": aum,
                    "Active_ETF_Count": count,
                    "Top_Leader_Ticker": ldr.get("ticker", ""),
                    "Leader_Netflow_USD": ldr.get("flow", ""),
                    "Global_24h_Netflow": kpis.get("net_inflow_24h", ""),
                    "Global_Total_AUM": kpis.get("total_aum", ""),
                    "Flow_Last_Week": kpis.get("flow_last_week", ""),
                    "Flow_Last_Month": kpis.get("flow_last_month", ""),
                    "Flow_Last_Quarter": kpis.get("flow_last_quarter", ""),
                    "Yearly_Strongest_Month": strongest_str,
                    "Yearly_Weakest_Month": weakest_str
                })

            # 2. Top Institutions Records
            institution_records = []
            for rank_idx, inst in enumerate(data.get("institutions", []), 1):
                institution_records.append({
                    "Timestamp_UTC": ts_str,
                    "Date": date_str,
                    "Rank": str(rank_idx),
                    "Institution_Name": inst.get("institution", ""),
                    "Total_Net_Inflow_USD": inst.get("total_net_inflow", ""),
                    "Total_ETF_Count": inst.get("etf_count", "")
                })

            # 3. All ETFs List (Table 2)
            all_etfs = []
            for r in data.get("t2Rows", []):
                rank = r[0]
                ticker_raw = r[1]
                parts = ticker_raw.split()
                ticker = parts[0].upper()
                tag = parts[1] if len(parts) > 1 else ""
                name = r[2] if len(r) > 2 else ""
                price = r[3] if len(r) > 3 else ""
                price_chg = r[4].replace("\n", " ") if len(r) > 4 else ""
                vol_usd = r[5] if len(r) > 5 else ""
                vol_sh = r[6] if len(r) > 6 else ""
                turnover = r[7] if len(r) > 7 else ""
                shares_out = r[8] if len(r) > 8 else ""
                aum = r[9] if len(r) > 9 else ""
                mkt_cap = r[10] if len(r) > 10 else ""
                fee = r[11] if len(r) > 11 else ""
                asset = deduce_asset(ticker, name, tag)

                leader_flow = "-"
                for cat_key, ldr_info in leaders.items():
                    if ldr_info.get("ticker", "").upper() == ticker:
                        leader_flow = ldr_info.get("flow", "-")

                all_etfs.append({
                    "Timestamp_UTC": ts_str,
                    "Date": date_str,
                    "Asset": asset,
                    "Rank": rank,
                    "Ticker": ticker,
                    "ETF_Name": name,
                    "Issuer": deduce_issuer(name, ticker),
                    "Price_USD": price,
                    "Price_Change": price_chg,
                    "Daily_Net_Inflow": leader_flow,
                    "AUM_USD": aum,
                    "Market_Cap_USD": mkt_cap,
                    "Daily_Volume_USD": vol_usd,
                    "Volume_Shares": vol_sh,
                    "Turnover_Rate": turnover,
                    "Shares_Outstanding": shares_out,
                    "Expense_Ratio": fee,
                    "Status": "Trading"
                })

            # 4. Merge HYPE ETFs if present and not already in all_etfs
            seen_tickers = set(x["Ticker"] for x in all_etfs)
            for r in hype_rows:
                if len(r) < 4:
                    continue
                ticker_raw = r[1]
                parts = ticker_raw.split()
                if not parts:
                    continue
                ticker = parts[0].upper()
                if not ticker or ticker in seen_tickers:
                    continue
                seen_tickers.add(ticker)
                
                name = r[2] if len(r) > 2 else ""
                price = r[3] if len(r) > 3 else ""
                price_chg = r[4].replace("\n", " ") if len(r) > 4 else ""
                vol_usd = r[5] if len(r) > 5 else ""
                vol_sh = r[6] if len(r) > 6 else ""
                turnover = r[7] if len(r) > 7 else ""
                shares_out = r[8] if len(r) > 8 else ""
                aum = r[9] if len(r) > 9 and r[9] else "-"
                mkt_cap = r[10] if len(r) > 10 and r[10] else "-"
                fee = r[11] if len(r) > 11 and r[11] else "-"
                status = r[12] if len(r) > 12 and r[12] else "Closed"
                
                all_etfs.append({
                    "Timestamp_UTC": ts_str,
                    "Date": date_str,
                    "Asset": "Hyperliquid",
                    "Rank": str(len(all_etfs) + 1),
                    "Ticker": ticker,
                    "ETF_Name": name,
                    "Issuer": deduce_issuer(name, ticker),
                    "Price_USD": price,
                    "Price_Change": price_chg,
                    "Daily_Net_Inflow": "-",
                    "AUM_USD": aum,
                    "Market_Cap_USD": mkt_cap,
                    "Daily_Volume_USD": vol_usd,
                    "Volume_Shares": vol_sh,
                    "Turnover_Rate": turnover,
                    "Shares_Outstanding": shares_out,
                    "Expense_Ratio": fee,
                    "Status": status
                })

            # Cache to full snapshot file
            FULL_SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
            with open(FULL_SNAPSHOT_PATH, "w", encoding="utf-8") as f:
                json.dump({
                    "harvest_timestamp_utc": now_dt.isoformat(),
                    "overview_records": overview_records,
                    "institution_records": institution_records,
                    "all_etfs": all_etfs,
                    "kpis": kpis
                }, f, indent=2)

            return overview_records, institution_records, all_etfs
    except Exception as e:
        print(f"CDP extraction failed: {e}")
        return None, None, None

def load_data_from_cache(snapshot_path: Path):
    """Loads ETF data, Institutions, and Overview from cached snapshot files."""
    if FULL_SNAPSHOT_PATH.exists():
        with open(FULL_SNAPSHOT_PATH, "r", encoding="utf-8") as f:
            d = json.load(f)
            return d.get("overview_records", []), d.get("institution_records", []), d.get("all_etfs", [])

    return [], [], []

def apply_sheet_batch(
    ws,
    columns_def,
    records,
    sheet_type: str = "etfs"
) -> tuple:
    """Writes or appends a batch of records with header management and spacer row protocol."""
    header_font = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")
    
    data_font = Font(name="Segoe UI", size=10, bold=False, color="1E293B")
    green_font = Font(name="Segoe UI", size=10, bold=True, color="15803D")
    red_font = Font(name="Segoe UI", size=10, bold=True, color="B91C1C")
    dim_font = Font(name="Segoe UI", size=10, bold=False, color="64748B")

    btc_fill = PatternFill(start_color="FFFBEB", end_color="FFFBEB", fill_type="solid")  # Gold
    eth_fill = PatternFill(start_color="F0FDF4", end_color="F0FDF4", fill_type="solid")  # Mint
    sol_fill = PatternFill(start_color="FAF5FF", end_color="FAF5FF", fill_type="solid")  # Violet
    xrp_fill = PatternFill(start_color="ECFEFF", end_color="ECFEFF", fill_type="solid")  # Cyan
    hype_fill = PatternFill(start_color="FFF7ED", end_color="FFF7ED", fill_type="solid") # Amber
    multi_fill = PatternFill(start_color="FFF1F2", end_color="FFF1F2", fill_type="solid") # Rose
    inst_fill = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")  # Slate tint
    white_fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

    thin_border = Border(
        left=Side(style='thin', color='CBD5E1'),
        right=Side(style='thin', color='CBD5E1'),
        top=Side(style='thin', color='CBD5E1'),
        bottom=Side(style='thin', color='CBD5E1')
    )

    first_col_title = columns_def[0][1]
    has_headers = (ws.max_row >= 1 and ws.cell(row=1, column=1).value == first_col_title)

    if not has_headers:
        for col_idx, (_, title, _, _) in enumerate(columns_def, 1):
            cell = ws.cell(row=1, column=col_idx, value=title)
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=False)
            cell.border = thin_border
        ws.row_dimensions[1].height = 30
        ws.freeze_panes = "A2"
        start_row = 2
        spacer_row = None
        is_first = True
    else:
        last_row = ws.max_row
        spacer_row = last_row + 1
        ws.row_dimensions[spacer_row].height = 16
        start_row = last_row + 2
        is_first = False

    current_row = start_row
    for r in records:
        asset = r.get("Asset", "") or r.get("Asset_Category", "")
        if sheet_type == "institutions":
            row_fill = inst_fill
        elif "SOL" in asset.upper(): row_fill = sol_fill
        elif "XRP" in asset.upper(): row_fill = xrp_fill
        elif "ETH" in asset.upper() or "ETHEREUM" in asset.upper(): row_fill = eth_fill
        elif "BTC" in asset.upper() or "BITCOIN" in asset.upper(): row_fill = btc_fill
        elif "HYPE" in asset.upper() or "HYPERLIQUID" in asset.upper(): row_fill = hype_fill
        elif "MULTI" in asset.upper(): row_fill = multi_fill
        else: row_fill = white_fill

        for col_idx, (col_key, _, _, align) in enumerate(columns_def, 1):
            val = r.get(col_key, "")
            cell = ws.cell(row=current_row, column=col_idx, value=val)
            cell.border = thin_border
            cell.fill = row_fill
            cell.alignment = Alignment(horizontal=align, vertical="center")

            # Dynamic font colors for flow and return metrics
            if any(k in col_key for k in ["Price_Change", "Daily_Net_Inflow", "Netflow", "Inflow", "Flow"]):
                val_str = str(val).strip()
                if val_str.startswith("+"):
                    cell.font = green_font
                elif val_str.startswith("-"):
                    cell.font = red_font
                elif val_str in ["0", "-", "+0"]:
                    cell.font = dim_font
                else:
                    cell.font = data_font
            elif col_key in ["Ticker", "Institution_Name", "Asset_Category"]:
                cell.font = Font(name="Segoe UI", size=10, bold=True, color="0F172A")
            elif col_key == "Asset":
                cell.font = Font(name="Segoe UI", size=10, bold=True, color="0F172A")
            else:
                cell.font = data_font

        ws.row_dimensions[current_row].height = 22
        current_row += 1

    # Auto-adjust column widths - never format so as to save space
    for col_idx, (_, _, min_w, _) in enumerate(columns_def, 1):
        col_letter = get_column_letter(col_idx)
        max_len = 0
        for cell in ws[col_letter]:
            if cell.value:
                max_len = max(max_len, len(str(cell.value)))
        ws.column_dimensions[col_letter].width = max(max_len + 5, min_w)

    end_row = current_row - 1
    return is_first, spacer_row, start_row, end_row

def dump_all_etf_data(
    excel_path: Path = DEFAULT_EXCEL_PATH,
    snapshot_path: Path = DEFAULT_SNAPSHOT_PATH,
    reset: bool = False
) -> dict:
    """Dumps all ETF records, Top Institutions, and Market Overview into DataBase_Trading.xlsx."""
    excel_path = Path(excel_path)
    excel_path.parent.mkdir(parents=True, exist_ok=True)

    # 1. Try Live CDP extraction first
    overview_records, institution_records, all_etfs = None, None, None
    try:
        overview_records, institution_records, all_etfs = asyncio.run(fetch_live_etf_via_cdp())
    except Exception as e:
        print(f"Async CDP extraction error: {e}")

    # 2. Fallback to cache if CDP not available
    if not all_etfs:
        print("Falling back to snapshot cache...")
        overview_records, institution_records, all_etfs = load_data_from_cache(snapshot_path)

    if not all_etfs:
        return {"status": "error", "message": "Failed to extract ETF records"}

    # 3. Open or create Excel workbook
    if excel_path.exists() and not reset:
        try:
            wb = openpyxl.load_workbook(excel_path)
        except Exception as e:
            raise RuntimeError(f"Failed to open {excel_path}: {e}")
    else:
        wb = openpyxl.Workbook()

    # Clean up default empty Sheet/Sheet1
    for s_name in ["Sheet", "Sheet1"]:
        if s_name in wb.sheetnames and len(wb.sheetnames) > 1 and wb[s_name].max_row <= 1 and wb[s_name]["A1"].value is None:
            del wb[s_name]

    # --- SHEET 1: Crypto_ETF_Flows (All 41+ ETFs across all assets) ---
    if SHEET_ALL_ETFS in wb.sheetnames:
        if reset:
            del wb[SHEET_ALL_ETFS]
            ws_etfs = wb.create_sheet(title=SHEET_ALL_ETFS, index=0)
        else:
            ws_etfs = wb[SHEET_ALL_ETFS]
    else:
        if "Sheet" in wb.sheetnames and wb["Sheet"].max_row <= 1 and wb["Sheet"]["A1"].value is None:
            ws_etfs = wb["Sheet"]
            ws_etfs.title = SHEET_ALL_ETFS
        else:
            ws_etfs = wb.create_sheet(title=SHEET_ALL_ETFS, index=0)

    is_first_e, spacer_e, start_e, end_e = apply_sheet_batch(ws_etfs, ETF_COLUMNS, all_etfs, sheet_type="etfs")

    # --- SHEET 2: Top_Institutions (Sponsors, Net Inflows, ETF Counts) ---
    inst_stats = {}
    if institution_records:
        if SHEET_INSTITUTIONS in wb.sheetnames:
            if reset:
                del wb[SHEET_INSTITUTIONS]
                ws_inst = wb.create_sheet(title=SHEET_INSTITUTIONS, index=1)
            else:
                ws_inst = wb[SHEET_INSTITUTIONS]
        else:
            ws_inst = wb.create_sheet(title=SHEET_INSTITUTIONS, index=1)

        is_first_i, spacer_i, start_i, end_i = apply_sheet_batch(ws_inst, INSTITUTION_COLUMNS, institution_records, sheet_type="institutions")
        inst_stats = {
            "is_first_batch": is_first_i,
            "spacer_row": spacer_i,
            "start_row": start_i,
            "end_row": end_i,
            "records_written": len(institution_records)
        }

    # --- SHEET 3: ETF_Market_Overview (Asset breakdown & Macro KPIs) ---
    overview_stats = {}
    if overview_records:
        if SHEET_OVERVIEW in wb.sheetnames:
            if reset:
                del wb[SHEET_OVERVIEW]
                ws_over = wb.create_sheet(title=SHEET_OVERVIEW, index=2)
            else:
                ws_over = wb[SHEET_OVERVIEW]
        else:
            ws_over = wb.create_sheet(title=SHEET_OVERVIEW, index=2)

        is_first_o, spacer_o, start_o, end_o = apply_sheet_batch(ws_over, OVERVIEW_COLUMNS, overview_records, sheet_type="overview")
        overview_stats = {
            "is_first_batch": is_first_o,
            "spacer_row": spacer_o,
            "start_row": start_o,
            "end_row": end_o,
            "records_written": len(overview_records)
        }

    # Remove any lingering empty default sheets
    for s_name in ["Sheet", "Sheet1"]:
        if s_name in wb.sheetnames and len(wb.sheetnames) > 1 and wb[s_name].max_row <= 1 and wb[s_name]["A1"].value is None:
            del wb[s_name]

    wb.active = ws_etfs

    try:
        wb.save(excel_path)
        wb.close()
    except PermissionError:
        raise PermissionError(
            f"Cannot write to {excel_path} because it is currently open in Excel. "
            "Please close the file in Excel and re-run."
        )

    return {
        "status": "success",
        "excel_path": str(excel_path),
        "sheets": wb.sheetnames,
        "all_etfs_sheet": {
            "name": SHEET_ALL_ETFS,
            "is_first_batch": is_first_e,
            "spacer_row": spacer_e,
            "start_row": start_e,
            "end_row": end_e,
            "records_written": len(all_etfs)
        },
        "top_institutions_sheet": inst_stats,
        "market_overview_sheet": overview_stats,
        "assets_covered": list(set(r.get("Asset", "") for r in all_etfs))
    }

dump_to_excel = dump_all_etf_data

def main():
    parser = argparse.ArgumentParser(description="CoinGlass Multi-Asset Spot ETF Excel Dumper")
    parser.add_argument("--excel-path", default=str(DEFAULT_EXCEL_PATH), help="Path to DataBase_Trading.xlsx")
    parser.add_argument("--snapshot-path", default=str(DEFAULT_SNAPSHOT_PATH), help="Path to coinglass_snapshot.json")
    parser.add_argument("--reset", action="store_true", help="Reset sheets and start fresh from Row 1")
    parser.add_argument("--status", action="store_true", help="Print current status of Excel database")
    args = parser.parse_args()

    excel_path = Path(args.excel_path)

    if args.status:
        if not excel_path.exists():
            print(f"Excel file does not exist: {excel_path}")
            return
        wb = openpyxl.load_workbook(excel_path)
        print(f"Workbook: {excel_path}")
        print(f"Sheets: {wb.sheetnames}")
        for s in wb.sheetnames:
            ws = wb[s]
            print(f"  Sheet '{s}': max_row={ws.max_row}, max_column={ws.max_column}")
        return

    result = dump_all_etf_data(
        excel_path=excel_path,
        snapshot_path=Path(args.snapshot_path),
        reset=args.reset
    )
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
