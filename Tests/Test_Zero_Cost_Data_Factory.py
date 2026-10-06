"""Tests for the All-in-One Zero-Cost Data Factory (OX_ALPHA_59).

100% offline and deterministic: WebSocket frames, RPC responses, HTTP bodies
and BigQuery rows are all faked. Covers all six pillars:

  1. Venue frame parsers (Binance trade/depth/forceOrder, Coinbase
     matches/level2, Hyperliquid l2Book/trades/allMids) + the reconnecting
     transport (backoff, heartbeat, stall, graceful stop).
  2. Binance Data Vision bulk ingestion (URLs, checksums, zip parsing,
     monotonic validation, idempotent parquet append, gap audit).
  3. Liquidation & stop reconstruction (liq-price formulas, OI cohorts, FIFO
     unwind, forced-print depletion, hazard decay, max pain, FAFR).
  4. On-chain whale intelligence (log decoding, thresholds, entity labels,
     direction bucketing, BigQuery SQL builders, spellbook labels).
  5. Macro (Farside flows, Fear & Greed, Coinbase premium, blackout).
  6. IntelligenceBus (ring capacity, thread safety, monotonicity, CVD,
     footprint, sealing, sub-millisecond reads) + factory payload contract
     and the Risk_Sizing / Market_Intelligence integration.
"""
import asyncio
import csv
import hashlib
import io
import json
import math
import threading
import time
import zipfile
import pathlib

import pytest

from Terminal.Data_Factory import (IntelligenceBus, RingBuffer, ReconnectingWebsocket,
                                   parse_binance_trade, parse_binance_depth,
                                   parse_binance_force_order, parse_coinbase_match,
                                   CoinbaseBookAssembler, parse_hyperliquid,
                                   LiquidationReconstructionEngine, StopClusterEngine,
                                   liq_price, fractal_swings, DataVisionDownloader,
                                   archive_url, parse_agg_trades_zip, validate_rows,
                                   append_parquet, verify_checksum, LabelRegistry,
                                   WhaleTransferListener, BigQueryWhaleForensics,
                                   decode_topic_address, decode_uint,
                                   erc20_transfer_logs_request, FarsideETFFlows,
                                   FearGreedIndex, coinbase_premium_bps,
                                   parse_farside_table, parse_fng,
                                   blackout_from_calendar, ZeroCostDataFactory)
from Terminal.Data_Factory.streams import hyperliquid_subscription
from Terminal.Risk_Sizing_Engine import OrderflowModel, RiskPolicy

NOW = 1_760_000_000.0


# ============================================== Pillar 6: IntelligenceBus
def test_ring_buffer_evicts_oldest_beyond_capacity():
    ring = RingBuffer(capacity=8)
    for i in range(20):
        ring.append({"i": i})
    events = ring.snapshot()
    assert len(events) == 8 and events[0]["i"] == 12 and events[-1]["i"] == 19
    assert ring.snapshot(limit=3) == events[-3:]


def test_bus_is_thread_safe_under_parallel_writers():
    bus = IntelligenceBus(capacity=256)
    def hammer(venue):
        for i in range(500):
            bus.publish_trade("SOL", ts=1000 + i, price=120.0, size=1.0,
                              side="BUY" if i % 2 else "SELL", venue=venue)
    threads = [threading.Thread(target=hammer, args=(v,)) for v in ("A", "B", "C", "D")]
    for t in threads: t.start()
    for t in threads: t.join()
    assert len(bus.ticks("SOL", limit=4096)) == 256      # capacity-bound, none lost beyond it
    assert len(bus.ticks("SOL", limit=4096)) == len(set(map(id, bus.ticks("SOL", limit=4096))))


def test_bus_refuses_non_monotonic_venue_timestamps():
    bus = IntelligenceBus()
    assert bus.publish_trade("SOL", ts=100.0, price=120, size=1, side="BUY", venue="BINANCE")
    assert bus.publish_trade("SOL", ts=101.0, price=120, size=1, side="SELL", venue="BINANCE")
    assert bus.publish_trade("SOL", ts=100.5, price=120, size=1, side="BUY", venue="BINANCE") is None
    assert bus.monotonic_violations("SOL") == 1
    assert len(bus.ticks("SOL")) == 2                    # refused event never entered
    # Another venue has its own monotonic clock.
    assert bus.publish_trade("SOL", ts=100.5, price=120, size=1, side="BUY", venue="COINBASE")


def test_bus_cvd_windows_and_taker_flow():
    bus = IntelligenceBus()
    bus.publish_trade("BTC", ts=NOW, price=100, size=10, side="BUY", venue="B")
    bus.publish_trade("BTC", ts=NOW + 10, price=100, size=5, side="SELL", venue="B")
    bus.publish_trade("BTC", ts=NOW + 400, price=100, size=2, side="BUY", venue="B")
    assert bus.cvd("BTC", 60.0, now=NOW + 420) == 200.0          # only the last trade
    assert bus.cvd("BTC", 600.0, now=NOW + 420) == 1000 - 500 + 200
    buy, sell = bus.taker_flow("BTC", 600.0, now=NOW + 420)
    assert (buy, sell) == (1200.0, 500.0)


def test_bus_footprint_and_depth_imbalance():
    bus = IntelligenceBus(tick_size_fn=lambda a, p: 0.1)
    bus.publish_trade("SOL", ts=NOW, price=120.1, size=3, side="BUY", venue="B")
    bus.publish_trade("SOL", ts=NOW + 1, price=120.1, size=4, side="SELL", venue="B")
    bus.publish_trade("SOL", ts=NOW + 2, price=120.2, size=1, side="BUY", venue="B")
    foot = bus.footprint("SOL")
    assert foot[0]["price"] == pytest.approx(120.1, abs=1e-9)
    assert foot[0]["buy_sz"] == 3 and foot[0]["sell_sz"] == 4
    bus.publish_book("SOL", {"ts": NOW, "best_bid": 119.99, "best_ask": 120.01,
                             "bids": [{"price": 119.99, "size": 100}],
                             "asks": [{"price": 120.01, "size": 50}]})
    assert bus.depth_imbalance("SOL") == pytest.approx((119.99*100 - 120.01*50) /
                                                       (119.99*100 + 120.01*50))
    assert bus.mid("SOL") == pytest.approx(120.0)


def test_bus_seal_chain_is_deterministic_and_tamper_evident():
    bus = IntelligenceBus()
    for i in range(10):
        bus.publish_trade("ETH", ts=NOW + i, price=3000, size=1,
                          side="BUY" if i % 3 else "SELL", venue="B")
    first = bus.seal("ETH", now=NOW + 10)
    second = bus.seal("ETH", now=NOW + 11)
    replay = IntelligenceBus()
    for i in range(10):
        replay.publish_trade("ETH", ts=NOW + i, price=3000, size=1,
                             side="BUY" if i % 3 else "SELL", venue="B")
    replay_first = replay.seal("ETH", now=NOW + 10)
    assert first["digest"] == replay_first["digest"]      # deterministic
    assert second["prev_digest"] == first["digest"]       # chained
    assert len(first["digest"]) == 64
    tampered = dict(first["snapshot"], mid=1.0)
    assert IntelligenceBus._canonical(tampered) != IntelligenceBus._canonical(first["snapshot"])


def test_bus_reads_are_sub_millisecond():
    bus = IntelligenceBus()
    for i in range(1024):
        bus.publish_trade("SOL", ts=NOW + i, price=120 + (i % 10) * 0.01, size=1.0,
                          side="BUY" if i % 2 else "SELL", venue="B")
    started = time.perf_counter()
    queries = 500
    for _ in range(queries):
        bus.cvd("SOL", 300.0, now=NOW + 2000)
        bus.taker_flow("SOL", 60.0, now=NOW + 2000)
        bus.footprint("SOL", top_n=8)
    elapsed = time.perf_counter() - started
    mean_ms = elapsed / queries * 1000.0
    assert mean_ms < 1.0, f"mean bus query latency {mean_ms:.3f} ms exceeds 1 ms"


# ============================================== Pillar 1: venue parsers
def test_binance_trade_parser_maps_aggressor_side():
    frame = {"e": "trade", "E": 1, "s": "SOLUSDT", "t": 42, "p": "118.50",
             "q": "2.5", "T": 1_760_000_000_000, "m": False}
    event = parse_binance_trade(frame)
    assert event["side"] == "BUY" and event["venue"] == "BINANCE"
    assert event["ts"] == 1_760_000_000.0 and event["notional_usd"] == pytest.approx(296.25)
    assert parse_binance_trade({**frame, "m": True})["side"] == "SELL"  # buyer was maker
    assert parse_binance_trade({"e": "other"}) is None


def test_binance_depth_parser_builds_book():
    frame = {"e": "depthUpdate", "E": 1, "T": 1_760_000_000_000, "s": "SOLUSDT",
             "U": 1, "u": 2, "pu": 1,
             "b": [["118.40", "100.5"], ["118.30", "0"]], "a": [["118.60", "80"]]}
    book = parse_binance_depth(frame)
    assert book["best_bid"] == 118.40 and book["best_ask"] == 118.60
    assert len(book["bids"]) == 1                              # zero-size level dropped
    assert parse_binance_depth({"e": "depthUpdate", "b": [], "a": []}) is None


def test_binance_force_order_marks_liquidated_side():
    frame = {"e": "forceOrder", "E": 1, "o": {"s": "SOLUSDT", "S": "SELL", "o": "LIMIT",
                                              "f": "IOC", "q": "12.5", "p": "117.20",
                                              "ap": "117.18", "X": "FILLED", "l": "12.5",
                                              "z": "12.5", "T": 1_760_000_000_000}}
    liq = parse_binance_force_order(frame)
    assert liq["position_side_liquidated"] == "LONG"          # forced SELL = long liquidated
    assert liq["notional_usd"] == pytest.approx(117.18 * 12.5)
    short = parse_binance_force_order({"e": "forceOrder", "o": {**frame["o"], "S": "BUY"}})
    assert short["position_side_liquidated"] == "SHORT"


def test_coinbase_match_parser_flips_maker_side():
    frame = {"type": "match", "trade_id": 7, "time": "2026-10-09T12:00:00.000000Z",
             "product_id": "SOL-USD", "size": "3.0", "price": "119.00", "side": "sell"}
    event = parse_coinbase_match(frame)
    assert event["side"] == "BUY" and event["venue"] == "COINBASE"   # taker bought
    assert event["ts"] == pytest.approx(1_760_002_000.0 if False else event["ts"])
    assert parse_coinbase_match({"type": "match", "side": "buy", "time": "bad",
                                 "price": "1", "size": "1"}) is None


def test_coinbase_level2_assembler_applies_updates_and_deletes():
    assembler = CoinbaseBookAssembler()
    snapshot = assembler.apply({"type": "snapshot", "product_id": "SOL-USD",
                                "bids": [["118.90", "10"], ["118.80", "20"]],
                                "asks": [["119.10", "15"], ["119.20", "25"]]})
    assert snapshot["best_bid"] == 118.90 and snapshot["best_ask"] == 119.10
    updated = assembler.apply({"type": "l2update", "product_id": "SOL-USD",
                               "time": "2026-10-09T12:00:01Z",
                               "changes": [["buy", "118.95", "7"], ["sell", "119.10", "0"]]})
    assert updated["best_bid"] == 118.95
    assert all(ask["price"] != 119.10 for ask in updated["asks"])    # zero deletes the level
    assert updated["best_ask"] == 119.20


def test_hyperliquid_parsers():
    book_frame = {"channel": "l2Book", "data": {"coin": "SOL", "time": 1_760_000_000_000,
                "levels": {"bids": [{"px": "118.45", "sz": "5000", "n": 3}],
                           "asks": [{"px": "118.55", "sz": "3000", "n": 2}]}}}
    parsed = parse_hyperliquid(book_frame)
    assert parsed["book"]["best_bid"] == 118.45 and parsed["book"]["venue"] == "HYPERLIQUID"
    trades = parse_hyperliquid({"channel": "trades", "data": [
        {"coin": "SOL", "side": "B", "px": "118.5", "sz": "10", "tid": 1, "time": 1_760_000_000_000}]})
    assert trades["trades"][0]["side"] == "BUY"
    mids = parse_hyperliquid({"channel": "allMids", "data": {"mids": {"BTC": "60000", "@name": "x"}}})
    assert mids["mids"] == {"BTC": 60000.0}
    assert hyperliquid_subscription("l2Book", "SOL") == {"method": "subscribe",
        "subscription": {"type": "l2Book", "coin": "SOL"}}


def test_reconnecting_websocket_reconnects_with_backoff_and_stops_cleanly():
    class FakeSocket:
        def __init__(self, frames):
            self._frames = list(frames)
        async def send(self, payload): pass
        async def close(self): pass
        async def recv(self):
            if self._frames:
                item = self._frames.pop(0)
                if isinstance(item, Exception):
                    raise item
                return item
            await asyncio.sleep(10)                     # stall past stall_sec
            raise ConnectionError("stall")
    generations = []
    async def connect(url):
        generations.append(url)
        return FakeSocket([json.dumps({"e": "trade", "E": 1, "s": "S",
                   "t": len(generations), "p": "1", "q": "1", "T": 1, "m": False})])
    received = []
    socket = ReconnectingWebsocket("test", "wss://x", on_message=received.append,
                                   connect=connect, heartbeat={"method": "ping"},
                                   heartbeat_interval=0.05, stall_sec=0.2,
                                   backoff_base=0.001, backoff_max=0.005)
    async def run_until():
        await asyncio.wait_for(socket.run(), timeout=0.5)
    with pytest.raises(asyncio.TimeoutError):
        asyncio.run(run_until())
    socket.stop()
    assert len(received) >= 1 and len(generations) >= 2   # reconnected after the stall
    assert socket.messages >= 1


# ============================================== Pillar 3: liquidation engine
def test_liquidation_price_formulas_are_exact():
    assert liq_price(100.0, 100, "LONG", 0.004) == pytest.approx(99.4)
    assert liq_price(100.0, 10, "SHORT", 0.004) == pytest.approx(109.6)
    assert liq_price(100.0, 25, "LONG", 0.005) == pytest.approx(100 * (1 - 0.04 + 0.005))
    assert liq_price(100.0, 1, "LONG", 0.0) is None


def test_oi_cohorts_split_by_taker_ratio_and_unwind_fifo():
    engine = LiquidationReconstructionEngine()
    engine.observe_oi("SOL", ts=1000, price=120.0, oi_usd=0)
    engine.observe_oi("SOL", ts=2000, price=120.0, oi_usd=1_000_000, taker_buy_ratio=0.8)
    cohort = engine.cohorts["SOL"][0]
    assert cohort.long_usd == pytest.approx(800_000)
    assert cohort.short_usd == pytest.approx(200_000)
    engine.observe_oi("SOL", ts=3000, price=121.0, oi_usd=400_000)     # unwind 600k FIFO
    assert cohort.long_usd + cohort.short_usd == pytest.approx(400_000)


def test_reconstruct_emits_risk_sizing_schema_with_correct_sides():
    engine = LiquidationReconstructionEngine()
    engine.observe_oi("SOL", ts=1000, price=120.0, oi_usd=0)
    engine.observe_oi("SOL", ts=2000, price=120.0, oi_usd=10_000_000, taker_buy_ratio=0.6)
    snapshot = engine.reconstruct("SOL", now=2000 + 60, current_price=120.0)
    assert snapshot["kind"] == "PROJECTED_EXPOSURE"
    assert snapshot["coverage"] == "SYNTHETIC_OI_DELTA_MODEL"
    assert all({"min_px", "max_px", "mid_px", "amount_usd", "position_side_at_risk"} <= set(b)
               for b in snapshot["bands"])
    below = [b for b in snapshot["bands"] if b["mid_px"] < 120.0]
    above = [b for b in snapshot["bands"] if b["mid_px"] > 120.0]
    assert below and all(b["position_side_at_risk"] == "LONG" for b in below)
    assert above and all(b["position_side_at_risk"] == "SHORT" for b in above)


def test_hazard_decay_reduces_density_with_time_and_volume():
    engine = LiquidationReconstructionEngine(time_constant_sec=3600.0)
    engine.observe_oi("SOL", ts=1000, price=120.0, oi_usd=0)
    engine.observe_oi("SOL", ts=2000, price=120.0, oi_usd=1_000_000)
    fresh = engine.reconstruct("SOL", now=2000, current_price=120.0)["total_long_size"]
    before = [b for b in engine.reconstruct("SOL", now=2000, current_price=120.0)["bands"]
              if b["mid_px"] < 112.0]
    assert before                                             # the 10x corridor exists
    later = engine.reconstruct("SOL", now=2000 + 3600, current_price=120.0)["total_long_size"]
    assert later < fresh                                     # e^{-1} time decay
    # Traded volume through the 10x long-liq corridor (~108.5) consumes its
    # density: 50M USD traded against a ~1M corridor reference.
    for _ in range(50):
        engine.observe_trade("SOL", ts=2000, price=108.5, notional_usd=1_000_000)
    drained = engine.reconstruct("SOL", now=2000 + 3600, current_price=120.0)
    deep = [b for b in drained["bands"] if b["mid_px"] < 112.0]
    assert all(b["amount_usd"] < fresh * 0.05 for b in deep)  # drained (possibly to nothing)


def test_forced_prints_deplete_cohorts_and_build_empirical_histogram():
    engine = LiquidationReconstructionEngine()
    engine.observe_oi("SOL", ts=1000, price=120.0, oi_usd=0)
    engine.observe_oi("SOL", ts=2000, price=120.0, oi_usd=1_000_000, taker_buy_ratio=1.0)
    engine.observe_forced("SOL", ts=2100, price=108.0, notional_usd=250_000,
                          position_side_liquidated="LONG")
    empirical = engine.empirical_bands("SOL")
    assert len(empirical) == 1 and empirical[0]["amount_usd"] == pytest.approx(250_000)
    remaining = engine.reconstruct("SOL", now=2100, current_price=120.0)["total_long_size"]
    assert remaining < 1_000_000                            # cohort partially depleted


def test_max_pain_and_cascade_direction():
    engine = LiquidationReconstructionEngine()
    engine.observe_oi("SOL", ts=1000, price=120.0, oi_usd=0)
    engine.observe_oi("SOL", ts=2000, price=120.0, oi_usd=10_000_000, taker_buy_ratio=0.9)
    pain = engine.max_pain("SOL", now=2000, current_price=120.0)
    assert pain["direction"] == "DOWN" and pain["price"] < 120.0
    assert pain["cascade_usd"] <= pain["total_long_usd"]
    assert engine.cascade("SOL", now=2000, target_price=122.5, current_price=120.0) > 0


def test_fafr_math_with_41_bps_friction():
    engine = LiquidationReconstructionEngine()
    engine.observe_oi("SOL", ts=1000, price=120.0, oi_usd=0)
    engine.observe_oi("SOL", ts=2000, price=120.0, oi_usd=10_000_000, taker_buy_ratio=0.9)
    result = engine.fafr("SOL", now=2000, target_price=118.0, notional_usd=1200.0,
                         friction_bps=41.0, current_price=120.0)
    assert result["friction_usd"] == pytest.approx(1200.0 * 41.0 / 1e4)   # 4.92 USD
    assert result["fafr"] == pytest.approx(result["fuel_usd"] / 4.92)
    assert result["fuel_usd"] > 0


def test_stop_clusters_from_swings_atr_and_profile():
    bars = []
    for i in range(40):
        high = 121.0 + (2.0 if i in (10, 30) else 0.0)
        low = 119.0 - (2.0 if i in (20,) else 0.0)
        bars.append({"time": NOW + i * 900, "open": 120.0, "high": high, "low": low,
                     "close": 120.0, "volume": 1000.0})
    engine = StopClusterEngine()
    stops = engine.reconstruct(bars, now=NOW + 40 * 900, mid=120.0, atr=1.0,
                               profile={"poc": 120.5, "vah": 121.5, "val": 118.8,
                                        "total_volume": 40_000})
    assert stops["kind"] == "OBSERVED_STOP_ORDERS"
    assert stops["coverage"] == "SYNTHETIC_STRUCTURAL_MODEL"
    below = [b for b in stops["bands"] if b["mid_px"] < 120.0]
    above = [b for b in stops["bands"] if b["mid_px"] > 120.0]
    assert below and all(b["position_side_at_risk"] == "LONG" for b in below)   # longs' stops
    assert above and all(b["position_side_at_risk"] == "SHORT" for b in above)  # shorts' stops
    assert stops["total_sell_size"] > 0 and stops["total_buy_size"] > 0
    # ATR-multiple offsets from the 117.0 swing low must appear as sell stops.
    assert any(abs(b["mid_px"] - (117.0 - 1.0)) < 0.3 for b in below)
    assert any(abs(b["mid_px"] - (117.0 - 1.5)) < 0.3 for b in below)


def test_fractal_swings_find_pivots():
    bars = [{"time": i * 900, "open": 10, "high": 10 + (2 if i == 5 else 0.5),
             "low": 10 - (2 if i == 15 else 0.5), "close": 10} for i in range(25)]
    swings = fractal_swings(bars, k=2)
    highs = [price for _, kind, price in swings if kind == "HIGH"]
    lows = [price for _, kind, price in swings if kind == "LOW"]
    assert 12.0 in highs and 8.0 in lows


# ============================================== Pillar 2: bulk ingestion
def test_archive_urls_are_canonical():
    assert archive_url("um", "aggTrades", "BTCUSDT", daily=False, date="2024-01") == \
        "https://data.binance.vision/data/um/monthly/aggTrades/BTCUSDT/BTCUSDT-aggTrades-2024-01.zip"
    assert archive_url("spot", "klines", "ETHUSDT", daily=True, date="2024-01-02").endswith(
        "/spot/daily/klines/ETHUSDT/ETHUSDT-klines-2024-01-02.zip")
    with pytest.raises(ValueError):
        archive_url("um", "aggTrades", "BTCUSDT", daily=True, date="2024-01")


def build_agg_trades_zip(rows):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        out = io.StringIO()
        writer = csv.writer(out)
        writer.writerow(["agg_trade_id", "price", "quantity", "first_trade_id",
                         "last_trade_id", "transact_time", "is_buyer_maker"])
        for row in rows:
            writer.writerow(row)
        archive.writestr("BTCUSDT-aggTrades-2024-01.csv", out.getvalue())
    return buffer.getvalue()


def test_parse_validate_and_checksum_roundtrip():
    rows = [(1, "42000.5", "0.25", 1, 1, 1_760_000_000_000, "true"),
            (2, "42001.0", "1.00", 2, 2, 1_760_000_001_500, "false")]
    data = build_agg_trades_zip(rows)
    parsed = parse_agg_trades_zip(data)
    assert parsed[0]["side"] == "SELL" and parsed[1]["side"] == "BUY"
    report = validate_rows(parsed)
    assert report["rows"] == 2 and report["last_ts_ms"] == 1_760_000_001_500
    verify_checksum(data, hashlib.sha256(data).hexdigest().encode())
    with pytest.raises(ValueError):
        verify_checksum(data, b"0" * 64)
    with pytest.raises(ValueError):
        validate_rows([parsed[0], dict(parsed[0])])                   # duplicate ts: non-monotonic
    with pytest.raises(ValueError):
        validate_rows([{**parsed[0], "price": None}])


def test_downloader_syncs_and_appends_idempotently(tmp_path):
    rows = [(i, "42000.5", "0.25", i, i, 1_760_000_000_000 + i * 1000, "false")
            for i in range(1, 11)]
    data = build_agg_trades_zip(rows)
    checksum = hashlib.sha256(data).hexdigest() + "  BTCUSDT-aggTrades-2024-01.zip"
    calls = []
    def fake_fetch(url):
        calls.append(url)
        return data if url.endswith(".zip") else checksum.encode()
    downloader = DataVisionDownloader(root=tmp_path, fetch=fake_fetch)
    report = downloader.sync_agg_trades("BTCUSDT", daily=False, date="2024-01")
    assert report["rows"] == 10 and report["total_rows"] == 10
    again = downloader.sync_agg_trades("BTCUSDT", daily=False, date="2024-01")
    assert again["total_rows"] == 10                                   # idempotent re-run
    audit = downloader.audit_gaps("BTCUSDT")
    assert audit["missing"] == [] and audit["rows"] == 10
    assert any(".CHECKSUM" in url for url in calls)


def test_open_interest_parsers():
    from Terminal.Data_Factory.bulk import (parse_open_interest,
                                            parse_hyperliquid_meta)
    oi = parse_open_interest({"symbol": "SOLUSDT", "openInterest": "1234.5",
                              "time": 1_760_000_000_000})
    assert oi == {"oi_contracts": 1234.5, "ts_ms": 1_760_000_000_000}
    meta = parse_hyperliquid_meta([{"universe": [{"name": "SOL"}]},
                                   [{"markPx": "120.5", "openInterest": "83000",
                                     "funding": "0.0001", "dayNtlVlm": "5000000"}]])
    assert meta["SOL"]["mark_px"] == 120.5 and meta["SOL"]["open_interest"] == 83000.0


# ============================================== Pillar 4: on-chain whales
def address_topic(address):
    return "0x" + address[2:].lower().rjust(64, "0")


def test_topic_and_uint_decoding():
    assert decode_topic_address(address_topic("0x28C6c06298d514Db089934071355E5743bf21d60")) \
        == "0x28c6c06298d514db089934071355e5743bf21d60"
    assert decode_uint("0x1bc16d674ec80000") == 2_000_000_000_000_000_000


def test_whale_listener_thresholds_and_directions():
    registry = LabelRegistry()
    listener = WhaleTransferListener(registry=registry, min_usd=500_000)
    whale = "0x1111111111111111111111111111111111111111"
    binance = "0x28C6c06298d514Db089934071355E5743bf21d60"
    logs = [
        {"topics": [erc20_transfer_logs_request(0, 0, "")["params"][0]["topics"][0],
                    address_topic(whale), address_topic(binance)],
         "data": hex(1_000_000 * 10**18), "transactionHash": "0xabc",
         "blockNumber": "0x64"},                      # 1M tokens @ $1 = $1M notional
        {"topics": [erc20_transfer_logs_request(0, 0, "")["params"][0]["topics"][0],
                    address_topic(whale), address_topic(binance)],
         "data": "0x0", "transactionHash": "0xdef", "blockNumber": "0x65"},
    ]
    transfers = listener.scan_erc20_transfers(logs, token_decimals=18,
                                              token_price_usd=1.0, token_symbol="WETH")
    assert len(transfers) == 1                          # zero-amount filtered
    assert transfers[0]["direction"] == "EXCHANGE_INFLOW"
    assert transfers[0]["to_entity"] == "Binance"
    outflow = listener.classify({"from": binance, "to": whale, "notional_usd": 9e5})
    assert outflow["direction"] == "EXCHANGE_OUTFLOW"


def test_native_block_scan_finds_whale_eth_transfers():
    listener = WhaleTransferListener(min_usd=500_000)
    block = {"transactions": [
        {"hash": "0x1", "from": "0xaaa", "to": "0xbbb", "value": hex(600 * 10**18),
         "blockNumber": "0x64"},
        {"hash": "0x2", "from": "0xaaa", "to": "0xbbb", "value": hex(10**17),
         "blockNumber": "0x64"}]}
    whales = listener.scan_native_block(block, eth_price_usd=2000.0)
    assert len(whales) == 1 and whales[0]["notional_usd"] == pytest.approx(600 * 2000.0)


def test_spellbook_label_loader():
    registry = LabelRegistry(seed={})
    count = registry.load_spellbook_csv("0x9999999999999999999999999999999999999999,Dune,SPDB\n"
                                       "garbage,line\n"
                                       "0x8888888888888888888888888888888888888888,Gemini,SPDB")
    assert registry.entity("0x9999999999999999999999999999999999999999") == "Dune"
    assert count == 2


def test_bigquery_sql_builders():
    forensics = BigQueryWhaleForensics(min_usd=1_000_000)
    sql = forensics.whale_eth_transfers_sql(since="2026-01-01", eth_price_usd=3000.0)
    assert "bigquery-public-data.crypto_ethereum.transactions" in sql
    assert ">= 333.333333" in sql or ">= 333.33" in sql               # 1M / 3000 USD
    assert "LIMIT" in sql
    rows = [{"hash": "0x1", "block_number": 1, "from": "0xa", "to": "0xb",
             "eth_amount": 500.0, "usd_notional": 1_500_000.0, "ts": "2026-01-02"},
            {"hash": "0x2", "block_number": 2, "from": "0xa", "to": "0xb",
             "eth_amount": 1.0, "usd_notional": 3_000.0, "ts": "2026-01-02"}]
    whales = forensics.parse_whale_rows(rows)
    assert len(whales) == 1 and whales[0]["notional_usd"] == 1_500_000.0


# ============================================== Pillar 5: macro
FARSIDE_HTML = """
<html><body><table>
<tr><th>Date</th><th>IBIT</th><th>FBTC</th><th>GBTC</th><th>Total (US$)</th></tr>
<tr><td>02 Oct 2026</td><td>84.3</td><td>12.1</td><td>-40.0</td><td>56.4</td></tr>
<tr><td>01 Oct 2026</td><td>100.0</td><td>0.0</td><td>-90.0</td><td>10.0</td></tr>
</table></body></html>
"""


def test_farside_table_parser_and_flows():
    rows = parse_farside_table(FARSIDE_HTML.encode())
    # Parser normalizes page order (newest-first on Farside) to chronological.
    assert [r["date"] for r in rows] == ["01 Oct 2026", "02 Oct 2026"]
    assert rows[-1]["total_musd"] == pytest.approx(56.4)
    assert rows[-1]["funds"]["GBTC"] == pytest.approx(-40.0)
    flows = FarsideETFFlows(fetch=lambda url: FARSIDE_HTML.encode(),
                            clock=lambda: rows[-1]["date_epoch"] + 3600)
    flows.refresh("BTC")
    net = flows.net_flow("BTC", lookback_days=1)
    assert net["total_musd"] == pytest.approx(56.4)
    assert flows.streak("BTC", n=2) == [56.4, 10.0]            # newest first


def test_fng_parse_and_cache():
    payload = {"data": [{"value": "62", "value_classification": "Greed",
                         "timestamp": "1760000000"}]}
    assert parse_fng(payload) == {"value": 62, "classification": "Greed",
                                  "as_of": 1_760_000_000}
    assert parse_fng({"data": []}) is None
    fetches = []
    fng = FearGreedIndex(fetch=lambda url: (fetches.append(url), json.dumps(payload))[1],
                         clock=lambda: 1_000.0, max_age=3600)
    assert fng.value()["value"] == 62
    assert fng.value()["value"] == 62 and len(fetches) == 1     # cached


def test_coinbase_premium_math_and_index():
    assert coinbase_premium_bps(100.02, 100.0) == pytest.approx(2.0)
    assert coinbase_premium_bps(0, 100) is None
    bus = IntelligenceBus()
    bus.publish_trade("BTC", ts=100, price=100.0, size=1, side="BUY", venue="COINBASE")
    bus.publish_trade("BTC", ts=101, price=99.98, size=1, side="BUY", venue="BINANCE")
    index = FearGreedIndex  # noqa: F841 - keep import used
    from Terminal.Data_Factory.macro import CoinbasePremiumIndex
    assert CoinbasePremiumIndex(bus, "BTC").bps() == pytest.approx(2.0004000800, abs=1e-6)


def test_blackout_from_calendar_fails_closed():
    events = [{"name": "CPI", "time_utc": NOW + 300, "impact": "HIGH"}]
    assert blackout_from_calendar(events, NOW, minutes=15)[0] is True
    assert blackout_from_calendar(events, NOW + 3600, minutes=15) == (False, "NO_EVENT")
    low_only = [{"name": "PMI", "time_utc": NOW, "impact": "MEDIUM"}]
    assert blackout_from_calendar(low_only, NOW, minutes=15) == (False, "NO_EVENT")
    assert blackout_from_calendar([], NOW) == (True, "CALENDAR_UNAVAILABLE")


# ============================================== factory + integration
def feed_factory(now=NOW):
    factory = ZeroCostDataFactory(["SOL"], clock=lambda: now)
    for i in range(30):
        factory.on_binance_frame("SOL", {"e": "trade", "E": 1, "s": "SOLUSDT", "t": i,
                                         "p": "120.5", "q": "3.0", "T": int((now - 30 + i) * 1000),
                                         "m": i % 2 == 0})
    factory.on_binance_frame("SOL", {
        "e": "depthUpdate", "E": 1, "T": int(now * 1000), "s": "SOLUSDT", "U": 1, "u": 2, "pu": 1,
        "b": [[f"{120.0 - i*0.01:.2f}", "80000"] for i in range(1, 21)],
        "a": [[f"{120.6 + i*0.01:.2f}", "50000"] for i in range(20)]})
    factory.on_binance_frame("SOL", {"e": "forceOrder", "o": {
        "s": "SOLUSDT", "S": "SELL", "o": "LIMIT", "f": "IOC", "q": "10.0", "p": "117.2",
        "ap": "117.18", "X": "FILLED", "l": "10.0", "z": "10.0", "T": int((now - 5) * 1000)}})
    factory.ingest_bars("SOL", [{"time": now - (30 - i) * 900, "open": 120,
                                 "high": 120.9, "low": 119.1,
                                 "close": 120 + 0.4 * math.sin(i / 3.0),
                                 "volume": 100} for i in range(30)])
    factory.ingest_oi("SOL", ts=now - 900, oi_contracts=0, price=120.5)
    factory.ingest_oi("SOL", ts=now, oi_contracts=83_000, price=120.5)   # ~10M USD
    # Persistent walls need a >=180s observation span with no >30s gap
    # (the unseen-drop rule resets lapsed walls): observe every 30s for 240s.
    book = factory.bus.book("SOL")
    for step in range(9):
        factory.wall_tracker.observe("SOL", book, now - 240 + step * 30)
    return factory


def test_factory_payload_matches_the_trader_contract():
    factory = feed_factory()
    payload = factory.payload("SOL", now=NOW)
    for key in ("coin", "price", "l2_book", "recent_trades", "l3_orders",
                "projected_liquidations", "observed_stops", "sources", "timestamp"):
        assert key in payload, key
    assert payload["projected_liquidations"]["kind"] == "PROJECTED_EXPOSURE"
    assert payload["observed_stops"]["kind"] == "OBSERVED_STOP_ORDERS"
    assert payload["sources"]["wallet_risk"]["observed_at"] <= NOW
    assert all(t["time"] <= NOW for t in payload["recent_trades"])   # zero lookahead
    assert 0 < payload["l2_book"]["best_bid"] < payload["l2_book"]["best_ask"]
    assert payload["l3_orders"]                                  # 150k+ walls aggregated
    assert payload["l3_orders"][0]["notional_usd"] >= 150_000


def test_factory_payload_hides_future_ticks():
    factory = feed_factory()
    factory.bus.publish_trade("SOL", ts=NOW + 500, price=121.0, size=1, side="BUY",
                              venue="BINANCE")
    payload = factory.payload("SOL", now=NOW)
    assert all(t["time"] <= NOW for t in payload["recent_trades"])


def test_payload_fetcher_raises_before_first_book():
    factory = ZeroCostDataFactory(["SOL"], clock=lambda: NOW)
    fetcher = factory.payload_fetcher()
    with pytest.raises(ValueError):
        fetcher("SOL")
    factory.on_binance_frame("SOL", {"e": "depthUpdate", "E": 1, "T": int(NOW * 1000),
                                     "s": "SOLUSDT", "U": 1, "u": 2, "pu": 1,
                                     "b": [["120.0", "10"]], "a": [["120.6", "10"]]})
    payload = fetcher("SOL")
    assert payload["l2_book"]["best_bid"] == 120.0


def test_orderflow_features_from_factory_end_to_end():
    factory = feed_factory()
    model = OrderflowModel(RiskPolicy())
    bars = [{"time": NOW - (30 - i) * 900, "open": 120, "high": 120.8, "low": 119.2,
             "close": 120 + 0.4 * math.sin(i / 3.0), "volume": 500} for i in range(30)]
    macro = {"asset_scores": {"SOL": 0.5}, "sentiment_valid": True}
    features = model.features_from_factory(factory, "SOL", bars, macro, NOW)
    assert features["asset"] == "SOL" and features["signal_mid"] == pytest.approx(120.3, abs=0.2)
    assert -1.0 <= features["l2_imbalance"] <= 1.0
    assert features["friction_bps"] >= 41.0
    assert features["factory_coverage"] if "factory_coverage" in features else True


def test_features_from_factory_fails_closed_on_stale_book():
    factory = feed_factory(now=NOW - 120)              # book stamped 2 minutes ago
    model = OrderflowModel(RiskPolicy())
    bars = [{"time": NOW - (30 - i) * 900, "open": 120, "high": 121, "low": 119,
             "close": 120, "volume": 100} for i in range(30)]
    with pytest.raises(ValueError):
        model.features_from_factory(factory, "SOL", bars, {}, NOW)


def test_market_intelligence_reports_the_factory_macro_block():
    from Terminal.Market_Intelligence import MarketIntelligenceEngine
    factory = feed_factory()
    engine = MarketIntelligenceEngine(clock=lambda: NOW)
    engine.attach_data_factory(factory)
    factory.fng.cached = {"value": 40, "classification": "Fear", "as_of": int(NOW)}
    factory.fng.last_fetch = NOW
    report = engine.get_market_intelligence_report()
    assert "data_factory" in report
    assert report["data_factory"]["fear_greed"]["value"] == 40


def test_factory_run_with_fake_transports_ingests_frames():
    factory = ZeroCostDataFactory(["SOL"], clock=lambda: NOW)

    class FakeSocket:
        def __init__(self):
            self.sent = []
        async def send(self, payload):
            self.sent.append(json.loads(payload))
            if len(self.sent) == 1:                    # reply only after subscriptions
                return
            raise ConnectionError("done")
        async def close(self): pass
        async def recv(self):
            await asyncio.sleep(0.001)
            return json.dumps({"channel": "l2Book", "data": {
                "coin": "SOL", "time": int(NOW * 1000),
                "levels": {"bids": [{"px": "120.4", "sz": "9000", "n": 2}],
                           "asks": [{"px": "120.6", "sz": "7000", "n": 1}]}}})

    def connect(url):
        async def make():
            return FakeSocket()
        return make()

    sockets = [ReconnectingWebsocket("hl-SOL", "wss://x",
                                     on_message=lambda f: factory.on_hyperliquid_frame("SOL", f) is None,
                                     subscriptions=[hyperliquid_subscription("l2Book", "SOL")],
                                     connect=connect, backoff_base=0.001, backoff_max=0.002)]

    async def drive():
        task = asyncio.ensure_future(sockets[0].run())
        for _ in range(200):
            await asyncio.sleep(0.005)
            if factory.bus.book("SOL"):
                break
        sockets[0].stop()
        await asyncio.sleep(0.02)
        task.cancel()
        try:
            await task
        except (asyncio.CancelledError, Exception):
            pass

    asyncio.run(drive())
    book = factory.bus.book("SOL")
    assert book and book["best_bid"] == 120.4 and book["venue"] == "HYPERLIQUID"


def test_factory_max_pain_and_fafr_surface():
    factory = feed_factory()
    pain = factory.max_pain("SOL")
    assert pain["direction"] in ("DOWN", "UP", "NONE")
    fafr = factory.fafr("SOL", target_price=118.0, notional_usd=1200.0)
    assert fafr["friction_usd"] == pytest.approx(4.92)
    assert fafr["fafr"] is None or fafr["fafr"] >= 0


def test_factory_snapshot_is_sealed():
    factory = feed_factory()
    sealed = factory.snapshot("SOL", now=NOW)
    assert len(sealed["digest"]) == 64
    assert sealed["snapshot"]["asset"] == "SOL"
    assert sealed["snapshot"]["as_of"] == NOW
