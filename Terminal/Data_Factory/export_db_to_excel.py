"""
Terminal/Data_Factory/export_db_to_excel.py
============================================
Exports SQLite time-series tables and tabular views into a multi-sheet Excel workbook.
File output: Data/trading_data_vault.xlsx
"""

import pathlib
import sqlite3
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "Data" / "history" / "time_series_index.db"
EXCEL_PATH = ROOT / "Data" / "trading_data_vault.xlsx"

def export_all_to_excel() -> pathlib.Path:
    conn = sqlite3.connect(DB_PATH)
    views_and_tables = [
        ("Latest Whales", "SELECT * FROM v_latest_whale_walls"),
        ("Market Telemetry 24", "SELECT * FROM v_latest_market_telemetry"),
        ("Forex Macro Events", "SELECT * FROM v_latest_macro_events"),
        ("Account Equity History", "SELECT * FROM v_account_equity_timeline LIMIT 500"),
        ("Arkham Smart Money", "SELECT * FROM v_latest_arkham_smart_money"),
        ("CoinGlass MaxPain", "SELECT * FROM coinglass_maxpain_history ORDER BY id DESC LIMIT 500"),
        ("Snapshot Catalog", "SELECT * FROM snapshot_catalog ORDER BY id DESC LIMIT 200"),
        ("Stream Downtime Gaps", "SELECT * FROM stream_gaps ORDER BY id DESC")
    ]

    with pd.ExcelWriter(EXCEL_PATH, engine="openpyxl") as writer:
        for sheet_name, query in views_and_tables:
            try:
                df = pd.read_sql_query(query, conn)
                df.to_excel(writer, sheet_name=sheet_name, index=False)
            except Exception as e:
                print(f"Warning: Sheet {sheet_name} query error: {e}")

    conn.close()
    print(f"Exported all tables -> {EXCEL_PATH} ({EXCEL_PATH.stat().st_size / 1024:.1f} KB)")
    return EXCEL_PATH

if __name__ == "__main__":
    export_all_to_excel()
