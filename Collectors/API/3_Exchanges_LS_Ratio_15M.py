#!/usr/bin/env python3
"""
Collectors/API/3_Exchanges_LS_Ratio_15M.py
==========================================
Pure-API Long/Short Ratio Collector (15-Minute Timeframe).
Direct REST endpoints from Binance Futures and Bybit.
"""
import asyncio
import sys
import pathlib

ROOT_DIR = pathlib.Path(__file__).resolve().parents[2]
CORE_DIR = ROOT_DIR / "Collectors" / "Core"
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))

from long_short_api_core import run_long_short_harvest

def main():
    success = asyncio.run(run_long_short_harvest("15m"))
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
