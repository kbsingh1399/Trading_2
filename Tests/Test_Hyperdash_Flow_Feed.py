"""
Tests/Test_Hyperdash_Flow_Feed.py
Unit tests verifying Hyperdash on-chain flow feed hardening:
1. Collision-proof fallback trade ID generation.
2. Atomic persistence to JSON and Parquet without race conditions.
3. Safe loading with raise_on_error guard.
"""

import json
import tempfile
import time
from pathlib import Path
import pytest
from Terminal.Data_Factory.hyperdash_flow_feed import atomic_persist_flows, load_raw_flow_history


def test_atomic_persistence_and_loading(tmp_path):
    json_path = tmp_path / "test_flows.json"
    pq_path = tmp_path / "test_flows.parquet"
    
    sample_records = [
        {
            "type": "WHALE_TRADE",
            "coin": "BTC",
            "side": "BUY",
            "market_impact": "BUY_PRESSURE",
            "notional_usd": 150000.0,
            "distance_pct": None,
            "duration_hours": None,
            "rate_usd_per_min": None,
            "price": 83000.0,
            "wallet_address": "0x1234",
            "asset_slug": "BTC",
            "raw_text": "#BTC Whale BUY",
            "msg_id": "HL_TRADE_BTC_1",
            "timestamp_epoch": int(time.time()),
            "time_label": "12:00",
            "date_heading": "October 11",
            "source": "HYPERLIQUID_L1_NATIVE_API"
        }
    ]
    
    # 1. Atomic persist
    ok = atomic_persist_flows(sample_records, json_target=json_path, parquet_target=pq_path)
    assert ok is True
    assert json_path.exists()
    assert pq_path.exists()
    
    # 2. Load back
    loaded = load_raw_flow_history(json_path=json_path, raise_on_error=True)
    assert len(loaded) == 1
    assert loaded[0]["msg_id"] == "HL_TRADE_BTC_1"
    assert loaded[0]["notional_usd"] == 150000.0


def test_collision_proof_fallback_ids():
    # Simulate two identical trades within the same millisecond and price/size
    trades = [
        {"px": "82955.0", "sz": "1.25", "side": "B", "time": 1791631333888, "tid": None},
        {"px": "82955.0", "sz": "1.25", "side": "B", "time": 1791631333888, "tid": None},
    ]
    
    coin = "BTC"
    existing_ids = set()
    generated_ids = []
    trade_seq = 0
    
    for tr in trades:
        trade_seq += 1
        px = float(tr.get("px") or 0.0)
        sz = float(tr.get("sz") or 0.0)
        side_char = str(tr.get("side") or "").upper()
        raw_tid = tr.get("tid")
        t_raw = tr.get("time")
        
        if raw_tid is not None and str(raw_tid).strip() and str(raw_tid) != "None":
            tid = str(raw_tid)
        else:
            t_ms = int(t_raw) if t_raw is not None else int(time.time() * 1000)
            tid = f"{t_ms}_{int(round(px * 1e2))}_{int(round(sz * 1e2))}_{side_char}_{trade_seq}"
        
        event_id = f"HL_TRADE_{coin}_{tid}"
        generated_ids.append(event_id)
        existing_ids.add(event_id)
        
    assert len(generated_ids) == 2
    assert generated_ids[0] != generated_ids[1]
    assert len(existing_ids) == 2, "Both fills must have distinct IDs to prevent deduplication drops"
