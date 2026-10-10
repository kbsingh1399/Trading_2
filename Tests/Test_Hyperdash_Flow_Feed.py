"""
Tests/Test_Hyperdash_Flow_Feed.py
Unit tests verifying Hyperdash on-chain flow feed hardening:
1. Collision-proof fallback trade ID generation.
2. Serialized JSON and Parquet replacement with failure rollback.
3. Safe loading with raise_on_error guard.
"""

import json
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



@pytest.fixture
def archive(tmp_path, monkeypatch):
    from Terminal.Data_Factory import hyperdash_flow_feed as feed
    monkeypatch.setattr(feed, "FLOWS_JSON_PATH", tmp_path / "flows.json")
    monkeypatch.setattr(feed, "FLOWS_PARQUET_PATH", tmp_path / "flows.parquet")
    return feed


def trade(**changes):
    return dict({"coin": "BTC", "px": "82955.001", "sz": "1.251", "side": "B", "time": 1791631333888, "tid": None}, **changes)


def poll(feed, monkeypatch, trades):
    monkeypatch.setattr(feed, "_post_json", lambda payload, **kwargs: trades if payload.get("coin") == "BTC" else [])
    return feed.sync_live_api_flows()


def test_fallback_ids_survive_poll_overlap_and_preserve_multiplicity(archive, monkeypatch):
    a, b = trade(), trade(px="82955.002")
    assert poll(archive, monkeypatch, [a, a, b]) == 3
    initial = {r["msg_id"] for r in archive.load_raw_flow_history()}
    assert poll(archive, monkeypatch, [trade(time=1791631333889), b, a, a]) == 1
    assert initial <= {r["msg_id"] for r in archive.load_raw_flow_history()}
    assert poll(archive, monkeypatch, [b, a, a]) == 0
    assert poll(archive, monkeypatch, [b, a, a, a]) == 1
    records = archive.load_raw_flow_history()
    assert len(records) == 5
    assert all(r["identity_basis"] == "PAYLOAD_MULTIPLICITY" for r in records)


def test_fallback_precision_and_wallet_identity(archive, monkeypatch):
    a = trade()
    b = trade(sz="1.252")
    c = trade(users=["0xaaa", "0xbbb"])
    assert poll(archive, monkeypatch, [a, b, c]) == 3
    assert poll(archive, monkeypatch, [c, b, a]) == 0


def test_timestamp_absence_cannot_fabricate_stable_identity(archive, monkeypatch):
    assert poll(archive, monkeypatch, [trade(time=None)]) == 0
    assert archive.load_raw_flow_history() == []


def test_native_ids_scope_assets_and_deduplicate(archive, monkeypatch):
    monkeypatch.setattr(archive, "_post_json", lambda payload, **kwargs:
                        [trade(tid=0), trade(tid=0)] if payload.get("coin") in ("BTC", "ETH") else [])
    assert archive.sync_live_api_flows() == 2
    assert archive.sync_live_api_flows() == 0
    assert {r["coin"] for r in archive.load_raw_flow_history()} == {"BTC", "ETH"}


def test_mixed_id_types_match_json_and_parquet(archive):
    import pandas as pd
    records = [{"msg_id": 123, "notional_usd": None}, {"msg_id": "HL_TRADE_BTC_123", "notional_usd": 50000.0}]
    assert archive.atomic_persist_flows(records)
    loaded = archive.load_raw_flow_history(raise_on_error=True)
    assert [r["msg_id"] for r in loaded] == ["123", "HL_TRADE_BTC_123"]
    assert pd.read_parquet(archive.FLOWS_PARQUET_PATH)["msg_id"].tolist() == ["123", "HL_TRADE_BTC_123"]
    assert records[0]["msg_id"] == 123


@pytest.mark.parametrize("content", [{}, [None], ["not a record"]])
def test_strict_loader_rejects_valid_json_with_invalid_shape(archive, content):
    archive.FLOWS_JSON_PATH.write_text(json.dumps(content), encoding="utf-8")
    with pytest.raises(ValueError):
        archive.load_raw_flow_history(raise_on_error=True)
    assert archive.load_raw_flow_history() == []


def test_failed_commit_returns_zero_and_preserves_files(archive, monkeypatch):
    import pandas as pd
    assert archive.atomic_persist_flows([{"msg_id": "original"}])
    old_json = archive.FLOWS_JSON_PATH.read_bytes()
    old_parquet = archive.FLOWS_PARQUET_PATH.read_bytes()
    def fail(*args, **kwargs):
        raise OSError("injected Parquet failure")
    monkeypatch.setattr(pd.DataFrame, "to_parquet", fail)
    assert poll(archive, monkeypatch, [trade(tid=77)]) == 0
    assert archive.FLOWS_JSON_PATH.read_bytes() == old_json
    assert archive.FLOWS_PARQUET_PATH.read_bytes() == old_parquet
    assert not list(archive.FLOWS_JSON_PATH.parent.glob("*.tmp.*"))


def test_json_commit_failure_restores_previous_parquet(archive, monkeypatch):
    assert archive.atomic_persist_flows([{"msg_id": "original"}])
    old_json = archive.FLOWS_JSON_PATH.read_bytes()
    old_parquet = archive.FLOWS_PARQUET_PATH.read_bytes()
    real_replace = Path.replace
    def fail_json(path, target):
        if Path(target) == archive.FLOWS_JSON_PATH:
            raise OSError("injected JSON commit failure")
        return real_replace(path, target)
    monkeypatch.setattr(Path, "replace", fail_json)
    assert not archive.atomic_persist_flows([{"msg_id": "new"}])
    assert archive.FLOWS_JSON_PATH.read_bytes() == old_json
    assert archive.FLOWS_PARQUET_PATH.read_bytes() == old_parquet


def test_concurrent_poll_commits_merge_history(archive, monkeypatch):
    from concurrent.futures import ThreadPoolExecutor
    import threading
    barrier = threading.Barrier(2)
    local = threading.local()
    def api(payload, **kwargs):
        if payload.get("coin") == "BTC":
            barrier.wait(timeout=5)
            return [trade(tid=local.tid)]
        return []
    monkeypatch.setattr(archive, "_post_json", api)
    def sync(tid):
        local.tid = tid
        return archive.sync_live_api_flows()
    with ThreadPoolExecutor(max_workers=2) as pool:
        assert list(pool.map(sync, (101, 102))) == [1, 1]
    assert {r["msg_id"] for r in archive.load_raw_flow_history()} == {"HL_TRADE_BTC_101", "HL_TRADE_BTC_102"}


def test_concurrent_writer_pairs_are_consistent(archive, monkeypatch):
    from concurrent.futures import ThreadPoolExecutor
    import pandas as pd
    monkeypatch.setattr(archive.time, "time", lambda: 123.0)
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(lambda n: archive.atomic_persist_flows([{"msg_id": n}]), range(8)))
    assert all(results)
    assert archive.load_raw_flow_history() == pd.read_parquet(archive.FLOWS_PARQUET_PATH).to_dict("records")
    assert not list(archive.FLOWS_JSON_PATH.parent.glob("*.tmp.*"))


def test_aggregation_identity_scopes_provider_asset_and_type(archive, monkeypatch):
    base = {"msg_id": 7, "source": "TELEGRAM", "coin": "BTC", "type": "WHALE_TRADE", "notional_usd": 100.0}
    records = [base, dict(base, msg_id="7"), dict(base, coin="ETH"),
               dict(base, source="OTHER"), dict(base, type="LIQUIDATION", side="LONG_LIQUIDATED")]
    monkeypatch.setattr(archive, "sync_live_api_flows", lambda: 0)
    monkeypatch.setattr(archive, "load_raw_flow_history", lambda: records)
    result = archive.get_hyperdash_flow_intelligence()
    assert result["summary"]["whale_trades_count"] == 3
    assert result["summary"]["total_alerts_tracked"] == 4
    assert result["universe_asset_breakdown"]["BTC"]["whale_trades_usd"] == 200.0
    assert result["universe_asset_breakdown"]["ETH"]["whale_trades_usd"] == 100.0


@pytest.mark.parametrize("tid", [None, 33])
def test_native_event_without_timestamp_is_not_rejuvenated(archive, monkeypatch, tid):
    assert poll(archive, monkeypatch, [trade(time=None, tid=tid)]) == 0


@pytest.mark.parametrize("changes", [{"px": "NaN"}, {"sz": "Infinity"}, {"side": "UNKNOWN"}, {"px": "bad"}, {"time": "bad"}])
def test_invalid_trade_evidence_does_not_contaminate_archive(archive, monkeypatch, changes):
    assert poll(archive, monkeypatch, [trade(**changes), trade(tid=22)]) == 1
    assert len(archive.load_raw_flow_history()) == 1


def test_provider_id_collision_does_not_suppress_native_event(archive, monkeypatch):
    assert archive.atomic_persist_flows([{"msg_id": "HL_TRADE_BTC_33", "source": "TELEGRAM", "coin": "BTC"}])
    assert poll(archive, monkeypatch, [trade(tid=33)]) == 1
    assert len(archive.load_raw_flow_history()) == 2


def test_liquidation_subfills_keep_direction_and_arrivals(archive, monkeypatch):
    assert archive.atomic_persist_flows([{"msg_id": "wallet", "wallet_address": "0xabc"}])
    fills = [trade(tid=1, liquidation=True), trade(tid=2, side="A", liquidation=True)]
    monkeypatch.setattr(archive, "_post_json", lambda payload, **kwargs: fills if payload.get("type") == "userFills" else [])
    assert archive.sync_live_api_flows() == 2
    fills.append(trade(tid=3, liquidation=True))
    assert archive.sync_live_api_flows() == 1
    assert archive.sync_live_api_flows() == 0
    rows = [r for r in archive.load_raw_flow_history() if r.get("type") == "LIQUIDATION"]
    assert len(rows) == 3
    assert [r["side"] for r in rows] == ["SHORT_LIQUIDATED", "LONG_LIQUIDATED", "SHORT_LIQUIDATED"]
    assert all(r["notional_usd"] == 103776.71 for r in rows)


def test_liquidation_fallback_preserves_visible_identical_fills(archive, monkeypatch):
    assert archive.atomic_persist_flows([{"msg_id": "wallet", "wallet_address": "0xabc"}])
    fills = [trade(liquidation=True), trade(liquidation=True)]
    monkeypatch.setattr(archive, "_post_json", lambda payload, **kwargs: fills if payload.get("type") == "userFills" else [])
    assert archive.sync_live_api_flows() == 2
    assert archive.sync_live_api_flows() == 0
    assert len(archive.load_raw_flow_history()) == 3


def test_process_writers_serialize_pair_replacement(archive):
    import subprocess
    import sys
    import pandas as pd
    script = """
import sys, time
from pathlib import Path
from Terminal.Data_Factory import hyperdash_flow_feed as feed
original = feed.pd.DataFrame.to_parquet

def slow_write(self, *args, **kwargs):
    result = original(self, *args, **kwargs)
    time.sleep(0.025)
    return result
feed.pd.DataFrame.to_parquet = slow_write
for index in range(5):
    assert feed.atomic_persist_flows([{'msg_id': sys.argv[3] + str(index)}], Path(sys.argv[1]), Path(sys.argv[2]))
"""
    processes = [subprocess.Popen([sys.executable, "-c", script, str(archive.FLOWS_JSON_PATH),
                                    str(archive.FLOWS_PARQUET_PATH), name], stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True) for name in ("a", "b")]
    for process in processes:
        _, error = process.communicate(timeout=30)
        assert process.returncode == 0, error
    assert archive.load_raw_flow_history() == pd.read_parquet(archive.FLOWS_PARQUET_PATH).to_dict("records")


def test_legacy_liquidation_aggregate_is_not_recounted(archive, monkeypatch):
    t_sec = trade()["time"] // 1000
    previous = {"type": "LIQUIDATION", "wallet_address": "0xabc", "coin": "BTC", "timestamp_epoch": t_sec,
                "msg_id": f"HL_LIQ_0xabc_BTC_{t_sec}", "source": "HYPERLIQUID_L1_NATIVE_API", "notional_usd": 200000.0}
    assert archive.atomic_persist_flows([previous])
    fills = [trade(tid=1, liquidation=True), trade(tid=2, liquidation=True, time=trade()["time"] + 1000)]
    monkeypatch.setattr(archive, "_post_json", lambda payload, **kwargs: fills if payload.get("type") == "userFills" else [])
    assert archive.sync_live_api_flows() == 1
    records = archive.load_raw_flow_history()
    assert len(records) == 2
    assert records[0] == previous
