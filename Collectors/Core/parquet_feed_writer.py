#!/usr/bin/env python3
"""
Collectors/Core/parquet_feed_writer.py
======================================
Re-export of Terminal/Data_Factory/parquet_feed_writer.py for seamless importing
by all collectors in Collectors/API/ and Collectors/Browser/.
"""
from __future__ import annotations

import pathlib
import sys

CORE_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = CORE_DIR.parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from Terminal.Data_Factory.parquet_feed_writer import (
    write_parquet_feed,
    read_parquet_feed,
    get_parquet_feed_metadata,
    validate_loading_before_dump,
    ensure_directories,
    FEEDS_DIR,
    METADATA_DIR,
    IST_TZ,
    UTC_TZ,
)

__all__ = [
    "write_parquet_feed",
    "read_parquet_feed",
    "get_parquet_feed_metadata",
    "validate_loading_before_dump",
    "ensure_directories",
    "FEEDS_DIR",
    "METADATA_DIR",
    "IST_TZ",
    "UTC_TZ",
]
