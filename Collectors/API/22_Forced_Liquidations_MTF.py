from __future__ import annotations

import pathlib
import sys
ROOT_DIR_FOR_PQ = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT_DIR_FOR_PQ / "Collectors" / "Core") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR_FOR_PQ / "Collectors" / "Core"))
if str(ROOT_DIR_FOR_PQ / "Terminal" / "Data_Factory") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR_FOR_PQ / "Terminal" / "Data_Factory"))
from parquet_feed_writer import write_parquet_feed, IST_TZ, UTC_TZ

import datetime
import logging
import os
import time
from typing import Dict, List, Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [22_Forced_Liquidations_MTF] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("22_Forced_Liquidations_MTF")

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "Data"
SHEET_NAME = "22_Forced_Liquidations_MTF"


def dump_forced_liquidations_to_parquet(candles: list[dict], feed_name: str = SHEET_NAME) -> bool:
    if not candles:
        log.warning("No candles to dump to Parquet.")
        return False
    meta = write_parquet_feed(feed_name, candles)
    log.info(f"Successfully dumped {len(candles)} MTF forced liquidation candles into Parquet feed '{feed_name}': {meta.get('byte_size')} bytes in {meta.get('write_latency_ms', 0):.2f}ms.")
    return True


if __name__ == "__main__":
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from Terminal.Data_Factory.forced_liquidation_daemon import ForcedLiquidationAggregator
    agg = ForcedLiquidationAggregator()
    agg.bootstrap_from_parquet_live_liq()
    candles = agg.get_all_candles_sorted(limit=500)
    ok = dump_forced_liquidations_to_parquet(candles)
    sys.exit(0 if ok else 1)
