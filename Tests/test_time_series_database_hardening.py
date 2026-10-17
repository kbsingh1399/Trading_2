"""
Tests/test_time_series_database_hardening.py
============================================
Verifies fixes for Arena Cycle 197 defects:
1. Date partition derived strictly from event epoch/timestamp (not wall-clock time).
2. Safe relative path handling when base_dir is outside repo root.
"""

import datetime
import pathlib
import pytest
from Terminal.Data_Factory.time_series_database import TimeSeriesDatabase

def test_date_partition_derived_from_epoch(tmp_path: pathlib.Path):
    db = TimeSeriesDatabase(base_dir=tmp_path)
    
    # Historical event epoch: 2025-05-10 14:30:00 UTC
    hist_dt = datetime.datetime(2025, 5, 10, 14, 30, 0, tzinfo=datetime.timezone.utc)
    hist_epoch = hist_dt.timestamp()
    hist_utc = hist_dt.strftime("%Y-%m-%dT%H:%M:%SZ")

    res = db.record_snapshot(
        stream="telemetry",
        data={"test": "historical_record", "assets_matrix_24": {}},
        timestamp_utc=hist_utc,
        epoch=hist_epoch,
        compress=False
    )

    # Verify partition is 2025-05-10 (NOT today's date)
    assert "2025-05-10" in res["history_file"]
    hist_file = pathlib.Path(res["history_file"])
    assert hist_file.parent.name == "2025-05-10"
    assert hist_file.exists()


def test_safe_relative_path_when_outside_root(tmp_path: pathlib.Path):
    # tmp_path is outside repo ROOT
    db = TimeSeriesDatabase(base_dir=tmp_path)
    
    now_epoch = datetime.datetime.now(datetime.timezone.utc).timestamp()
    res = db.record_snapshot(
        stream="arkham",
        data={"institutional_entities_deep": {}},
        epoch=now_epoch,
        compress=True
    )

    assert res["stream"] == "arkham"
    assert pathlib.Path(res["history_file"]).exists()
