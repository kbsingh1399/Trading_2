#!/usr/bin/env python3
"""
Collectors/Core/parquet_writer.py
=================================
Wrapper and core utility for writing parquet feeds.
Redirects to Terminal/Data_Factory/parquet_feed_writer.py.
"""
from __future__ import annotations
import pathlib
import sys

CORE_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = CORE_DIR.parents[1]
DATA_FACTORY_DIR = ROOT_DIR / "Terminal" / "Data_Factory"
if str(DATA_FACTORY_DIR) not in sys.path:
    sys.path.insert(0, str(DATA_FACTORY_DIR))

from parquet_feed_writer import (
    write_parquet_feed,
    read_parquet_feed,
    get_parquet_feed_metadata,
    ensure_directories,
    FEEDS_DIR,
    METADATA_DIR,
)

__all__ = [
    "write_parquet_feed",
    "read_parquet_feed",
    "get_parquet_feed_metadata",
    "ensure_directories",
    "FEEDS_DIR",
    "METADATA_DIR",
]
