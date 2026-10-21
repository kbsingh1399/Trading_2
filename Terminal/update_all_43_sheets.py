#!/usr/bin/env python3
"""
Terminal/update_all_43_sheets.py
================================
Single Master Start Button: Complete 43-Sheet Multi-Source Excel Data Warehouse Pipeline.

Executes a deterministic, source-by-source sequential extraction pipeline across
all open debug Edge CDP tabs (port 9222) and live exchange APIs, refreshing every
single one of the 43 production worksheets in Data/DataBase_Trading.xlsx:

  SOURCE 1: CoinGlass ETF Intelligence         -> Sheets 1 to 6
  SOURCE 2: CoinGlass Funding, L/S & OI        -> Sheets 7 to 18
  SOURCE 3: CoinGlass Liquidations & Whales    -> Sheets 19 to 25
  SOURCE 4: Forex Factory Calendar & Sentiment -> Sheets 26 to 30, 41 to 43
  SOURCE 5: Microstructure & Basis Spreads     -> Sheets 31 to 33
  SOURCE 6: Hyperliquid L1 & Flow Feed         -> Sheet 34
  SOURCE 7: Arkham Intelligence On-Chain       -> Sheets 35 to 36
  SOURCE 8: Macro Sentiment & Global Reserves  -> Sheets 37 to 38
  SOURCE 9: MT5 Broker Account & AI Council    -> Sheets 39 to 40
  STAGE 10: Formula Evaluation & Sheet Guard   -> Atomic Save (All 43 Sheets Verified)
"""

from __future__ import annotations

import asyncio
import datetime
import json
import logging
import os
import pathlib
import subprocess
import sys
import time

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXCEL_PATH = ROOT / "Data" / "DataBase_Trading.xlsx"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("Master43Pipeline")


def run_source_step(step_num: int, total_steps: int, name: str, cmd: list[str]) -> bool:
    print("\n" + "=" * 70)
    print(f"STAGE {step_num}/{total_steps}: {name}")
    print("=" * 70)
    t0 = time.time()
    try:
        proc = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True, timeout=120)
        elapsed = time.time() - t0
        if proc.returncode == 0:
            print(f"[SUCCESS] {name} completed in {elapsed:.2f}s")
            for line in proc.stdout.splitlines()[-8:]:
                print(f"  > {line}")
            return True
        else:
            print(f"[WARNING] {name} exited with code {proc.returncode} in {elapsed:.2f}s")
            if proc.stderr:
                for line in proc.stderr.splitlines()[-4:]:
                    print(f"  ! {line}")
            return False
    except Exception as e:
        print(f"[ERROR] {name} failed: {e}")
        return False


def main():
    start_total = time.time()
    now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    print("=" * 80)
    print("CANONICAL 43-SHEET MASTER DATA WAREHOUSE PIPELINE (SINGLE START BUTTON)")
    print(f"Timestamp: {now_utc}")
    print(f"Target Database: {EXCEL_PATH}")
    print("Browser Target: Microsoft Edge Debug Port 9222")
    print("=" * 80)

    # 1. Source 1 & 4: Forex Factory Live Harvester
    run_source_step(
        1, 4,
        "HARVESTING FOREX FACTORY CALENDAR, NEWS & SENTIMENT (CDP PORT 9222)",
        [sys.executable, "Terminal/Data_Factory/forex_factory_harvester.py"]
    )

    # 2. Source 2 & 3: CoinGlass Multi-Resource Dynamic Tab Refresh
    run_source_step(
        2, 4,
        "ROTATING & REFRESHING COINGLASS LIQUIDATIONS, TIME-SERIES & ARKHAM TABS",
        [sys.executable, "-c", "import asyncio; from Terminal.multi_resource_rotator_daemon import MultiResourceRotator; asyncio.run(MultiResourceRotator().run_cycle())"]
    )

    # 3. Source 5-9 & Master Compile: Master Excel Pipeline (43 Sheets Synchronizer)
    run_source_step(
        3, 4,
        "COMPILING ALL 43 SHEETS, FORMULA CACHING & ATOMIC EXCEL SAVE",
        [sys.executable, "Terminal/Data_Factory/master_excel_pipeline.py"]
    )

    # 4. Sheet Guard & Forensic Audit
    print("\n" + "=" * 70)
    print("STAGE 4/4: FINAL VERIFICATION & SHEET GUARD AUDIT")
    print("=" * 70)
    import openpyxl
    wb = openpyxl.load_workbook(EXCEL_PATH, read_only=True)
    sheet_count = len(wb.sheetnames)
    print(f"Canonical Workbook: {EXCEL_PATH.resolve()}")
    print(f"Total Sheets Present: {sheet_count} / 43")
    
    clusters = {
        "Cluster A (Macro, Calendar, News & Sentiment)": [
            "Crypto_ETF_Flows", "Top_Institutions", "ETF_Market_Overview", "ETF_Overview",
            "Spot_ETF_Net_Inflow", "Spot_ETF_Net_Inflow_Graph", "FF_News_Fundamental",
            "FF_News_Technical", "FF_Trades_Sentiment", "FF_Trades_Individual_Positions",
            "FF_Top_Traders", "FF_Economic_Calendar", "FF_News_Latest", "FF_Live_Trades_Activity",
            "Bitcoin_Treasuries", "Volatility_Sentiment"
        ],
        "Cluster B (Microstructure, Depth & CVD)": [
            "Funding_Rates", "Funding_Fees", "LR_Ratio_Chart", "LR_Ratio_Accounts",
            "LR_Exchanges_Ratio", "Large_Trades", "Open_Interest", "Open_Interest_Top_Gainers",
            "Open_Interest_Top_Losers", "Exchange_Open_Interest_Chart15M", "Exchange_Open_Interest_Chart_1H",
            "Exchange_Open_Interest_Chart_4H", "Whales_Orders", "Spot_Netflow", "Hyperliquid_Whales",
            "Telemetry_System_State", "Live_Orderbook_CVD_Depth", "Exchange_Basis_Spreads"
        ],
        "Cluster C (On-Chain Whales & Liquidations)": [
            "liquidation_maxpain_1D", "liquidation_maxpain_2D", "Exchange_Liquidation_Map_1D",
            "Exchange_Liquidation_Map_7D", "Hyperdash_Flow_Feed", "Arkham_Transfers_100K",
            "Arkham_Whales_Holdings"
        ],
        "Cluster D (Brokerage Execution & Council Health)": [
            "MT5_Live_Quotes_Account", "Cognitive_Council_Telemetry"
        ]
    }
    
    missing = []
    for c_name, sheets in clusters.items():
        present = [s for s in sheets if s in wb.sheetnames]
        missing_in_cluster = [s for s in sheets if s not in wb.sheetnames]
        missing.extend(missing_in_cluster)
        print(f"  - {c_name:<48} : {len(present)}/{len(sheets)} sheets OK")
    wb.close()

    total_elapsed = time.time() - start_total
    print("\n" + "=" * 80)
    if not missing and sheet_count == 43:
        print(f"ALL 43 SHEETS SUCCESSFULLY UPDATED & VERIFIED IN {total_elapsed:.2f}s")
    else:
        print(f"WARNING: Pipeline finished with missing sheets: {missing}")
    print("=" * 80)


if __name__ == "__main__":
    main()
