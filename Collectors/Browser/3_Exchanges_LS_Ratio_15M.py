#!/usr/bin/env python3
"""
Collectors/Browser/3_Exchanges_LS_Ratio_15M.py
==============================================
In-Memory Browser Extraction Collector for Exchanges Long/Short Ratio (15M).
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
    success = asyncio.run(run_coinglass_ls_harvest("15m"))
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
