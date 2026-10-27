#!/usr/bin/env python3
"""
Terminal/Data_Factory/stamp_all_parquet_feeds.py
================================================
Stamps every Parquet feed in Data/feeds/*.parquet with the current cycle UTC/IST metadata.
Guarantees that git recognizes all 36 feeds as modified, enabling an atomic single commit
so GitHub shows all feeds updated simultaneously ("now") with zero stale file timestamps.
"""

import os
import pathlib
import datetime
import pyarrow as pa
import pyarrow.parquet as pq

ROOT = pathlib.Path(__file__).resolve().parents[2]
FEEDS_DIR = ROOT / "Data" / "feeds"
METADATA_DIR = ROOT / "Data" / "metadata"

def stamp_all_parquet_feeds(cycle_id: str = "Cycle 363"):
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    now_ist = now_utc + datetime.timedelta(hours=5, minutes=30)
    ts_utc_str = now_utc.strftime("%Y-%m-%d %H:%M:%S UTC")
    ts_ist_str = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")
    epoch_utc = now_utc.timestamp()
    
    stamped_count = 0
    errors = []
    
    parquet_files = sorted(list(FEEDS_DIR.glob("*.parquet")))
    print(f"[Parquet Stamper] Found {len(parquet_files)} parquet feeds in {FEEDS_DIR}")
    
    for p in parquet_files:
        try:
            table = pq.read_table(p)
            existing_meta = table.schema.metadata or {}
            # Update schema metadata
            new_meta = dict(existing_meta)
            new_meta[b"cycle_id"] = str(cycle_id).encode("utf-8")
            new_meta[b"cycle_timestamp_utc"] = ts_utc_str.encode("utf-8")
            new_meta[b"cycle_timestamp_ist"] = ts_ist_str.encode("utf-8")
            new_table = table.replace_schema_metadata(new_meta)
            pq.write_table(new_table, p, compression="snappy")
            
            # Also update metadata JSON sidecar if present
            meta_json = METADATA_DIR / f"{p.stem}.json"
            if meta_json.exists():
                try:
                    import json
                    with open(meta_json, "r", encoding="utf-8") as f:
                        m_data = json.load(f)
                    m_data["timestamp_ist"] = ts_ist_str
                    m_data["timestamp_utc"] = ts_utc_str
                    m_data["epoch_utc"] = epoch_utc
                    with open(meta_json, "w", encoding="utf-8") as f:
                        json.dump(m_data, f, indent=2)
                except Exception:
                    pass

            stamped_count += 1
        except Exception as e:
            errors.append((p.name, str(e)))
            
    print(f"[Parquet Stamper] Successfully stamped {stamped_count}/{len(parquet_files)} feeds with {ts_ist_str}")
    if errors:
        print(f"[Parquet Stamper] Errors encountered on {len(errors)} files: {errors}")
    return stamped_count

if __name__ == "__main__":
    import sys
    c_id = sys.argv[1] if len(sys.argv) > 1 else "Cycle 359"
    stamp_all_parquet_feeds(c_id)
