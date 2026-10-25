#!/usr/bin/env python3
"""
Data/Excel_Modules/9_Liquidation_Max_Pain_24H.py
================================================
Dedicated Excel Module 14: CoinGlass Cryptocurrency Liquidation Max Pain (24-Hour Window).
Extracts 100% of candidates (~745 assets) from https://www.coinglass.com/liquidation-maxpain
and writes to worksheet '9_Liquidation_Max_Pain_24H' in Data/DataBase_Trading.xlsx
(positioned at Index 13, immediately following '8_Exchange_Liquidation_Map_7D').
"""

from __future__ import annotations

try:
    import excel_lock_hook
except Exception:
    pass
import sys
import pathlib

MODULES_DIR = pathlib.Path(__file__).resolve().parent
if str(MODULES_DIR) not in sys.path:
    sys.path.insert(0, str(MODULES_DIR))

from liquidation_maxpain_core import run_maxpain_harvest

if __name__ == "__main__":
    run_maxpain_harvest(
        timeframe_code="24H",
        timeframe_label="24 hour",
        sheet_name="9_Liquidation_Max_Pain_24H",
        target_index=13,
        log_name="9_Liquidation_Max_Pain_24H",
    )
