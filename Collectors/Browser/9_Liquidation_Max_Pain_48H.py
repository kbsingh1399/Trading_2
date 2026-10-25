#!/usr/bin/env python3
"""
Data/Excel_Modules/9_Liquidation_Max_Pain_48H.py
================================================
Dedicated Excel Module 15: CoinGlass Cryptocurrency Liquidation Max Pain (48-Hour Window).
Extracts 100% of candidates (~745 assets) from https://www.coinglass.com/liquidation-maxpain
and writes to worksheet '9_Liquidation_Max_Pain_48H' in Data/feeds/<feed_name>.parquet
(positioned at Index 14, immediately following '9_Liquidation_Max_Pain_24H').
"""

from __future__ import annotations

import pathlib
import sys
ROOT_DIR_FOR_PQ = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT_DIR_FOR_PQ / "Collectors" / "Core") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR_FOR_PQ / "Collectors" / "Core"))
if str(ROOT_DIR_FOR_PQ / "Terminal" / "Data_Factory") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR_FOR_PQ / "Terminal" / "Data_Factory"))
from parquet_feed_writer import write_parquet_feed, IST_TZ, UTC_TZ


import sys
import pathlib

MODULES_DIR = pathlib.Path(__file__).resolve().parent
if str(MODULES_DIR) not in sys.path:
    sys.path.insert(0, str(MODULES_DIR))

from liquidation_maxpain_core import run_maxpain_harvest

if __name__ == "__main__":
    run_maxpain_harvest(
        timeframe_code="48H",
        timeframe_label="48 hour",
        sheet_name="9_Liquidation_Max_Pain_48H",
        target_index=14,
        log_name="9_Liquidation_Max_Pain_48H",
    )
