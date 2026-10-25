from __future__ import annotations

import pathlib
import sys
ROOT_DIR_FOR_PQ = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT_DIR_FOR_PQ / "Collectors" / "Core") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR_FOR_PQ / "Collectors" / "Core"))
if str(ROOT_DIR_FOR_PQ / "Terminal" / "Data_Factory") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR_FOR_PQ / "Terminal" / "Data_Factory"))
from parquet_feed_writer import write_parquet_feed, IST_TZ, UTC_TZ

#!/usr/bin/env python3
"""
Collectors/Browser/3_Exchanges_LS_Ratio_1H.py
=============================================
In-Memory Browser Extraction Collector for Exchanges Long/Short Ratio (1H).
Extracts authentic CoinGlass multi-exchange Long/Short ratios over Edge CDP.
"""
import asyncio
import sys
import pathlib

ROOT_DIR = pathlib.Path(__file__).resolve().parents[2]
CORE_DIR = ROOT_DIR / "Collectors" / "Core"
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))

from coinglass_ls_browser_core import run_coinglass_ls_harvest

def main():
    success = asyncio.run(run_coinglass_ls_harvest("1h"))
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
