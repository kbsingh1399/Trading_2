#!/usr/bin/env python3
"""
Terminal/Data_Factory/forced_liquidation_daemon.py
===================================================
Always-On Multi-Timeframe Forced Liquidation Aggregator & Parquet Sync Daemon.
Aggregates live forced liquidation events across 5m, 15m, 1h, and 4h candles
with explicit dual IST (UTC+5:30) and UTC timestamps.

Features:
  1. Subscribes to Binance Futures '!forceOrder@arr' real-time WebSocket.
  2. Ingests existing Data/feeds/7_Live_Liq.parquet / CoinGlass rows for historical bootstrap.
  3. Maintains rolling time-bucketed candles (5m, 15m, 1h, 4h) per asset & market-wide.
  4. Computes Long Liq USD, Short Liq USD, Net Delta, Order Count, and Dominant Flow.
  5. Periodically triggers Parquet dump to Data/feeds/22_Forced_Liquidations_MTF.parquet.
"""

from __future__ import annotations

import argparse
import asyncio
import dataclasses
import datetime
import json
import logging
import os
import pathlib
import sys
import time
from typing import Dict, List, Optional, Tuple

try:
    import websockets
except ImportError:
    websockets = None

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT / "Collectors" / "Core") not in sys.path:
    sys.path.insert(0, str(ROOT / "Collectors" / "Core"))
if str(ROOT / "Terminal" / "Data_Factory") not in sys.path:
    sys.path.insert(0, str(ROOT / "Terminal" / "Data_Factory"))
from parquet_feed_writer import write_parquet_feed

DATA_DIR = ROOT / "Data"
BUFFER_FILE = DATA_DIR / "forced_liquidations_buffer.json"

IST_TIMEZONE = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
UTC_TIMEZONE = datetime.timezone.utc

INSTITUTIONAL_ASSETS = [
    "BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "XRPUSDT", "DOGEUSDT",
    "ADAUSDT", "TRXUSDT", "LINKUSDT", "AVAXUSDT", "SUIUSDT", "NEARUSDT",
    "DOTUSDT", "LTCUSDT", "BCHUSDT", "APTUSDT", "OPUSDT", "ARBUSDT",
    "ALL_MARKET"
]

TIMEFRAMES = ["5m", "15m", "1h", "4h"]
TF_MINUTES = {
    "5m": 5,
    "15m": 15,
    "1h": 60,
    "4h": 240,
}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [LiqDaemon] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("LiqDaemon")


@dataclasses.dataclass
class LiquidationEvent:
    symbol: str
    side: str  # "SELL" (Long liquidated) or "BUY" (Short liquidated)
    price: float
    quantity: float
    usd_value: float
    timestamp_utc: datetime.datetime
    exchange: str = "Binance"


class ForcedLiquidationAggregator:
    def __init__(self, symbols: Optional[List[str]] = None):
        self.symbols = symbols or INSTITUTIONAL_ASSETS
        # Buckets structure: {timeframe: {symbol: {bucket_start_epoch: candle_dict}}}
        self.buckets: Dict[str, Dict[str, Dict[int, Dict]]] = {
            tf: {sym: {} for sym in self.symbols} for tf in TIMEFRAMES
        }
        self.raw_events: List[LiquidationEvent] = []

    @staticmethod
    def get_candle_bounds(dt: datetime.datetime, timeframe: str) -> Tuple[datetime.datetime, datetime.datetime]:
        """Aligns datetime to fixed timeframe open/close boundaries."""
        dt_utc = dt.astimezone(UTC_TIMEZONE)
        mins = TF_MINUTES[timeframe]
        
        if timeframe in ("5m", "15m"):
            minute_bucket = (dt_utc.minute // mins) * mins
            start = dt_utc.replace(minute=minute_bucket, second=0, microsecond=0)
            end = start + datetime.timedelta(minutes=mins)
        elif timeframe == "1h":
            start = dt_utc.replace(minute=0, second=0, microsecond=0)
            end = start + datetime.timedelta(hours=1)
        elif timeframe == "4h":
            hour_bucket = (dt_utc.hour // 4) * 4
            start = dt_utc.replace(hour=hour_bucket, minute=0, second=0, microsecond=0)
            end = start + datetime.timedelta(hours=4)
        else:
            raise ValueError(f"Unsupported timeframe: {timeframe}")
            
        return start, end

    def ingest_event(self, event: LiquidationEvent) -> None:
        """Ingests a liquidation event into all active timeframe buckets."""
        self.raw_events.append(event)
        # Keep recent 10,000 events in memory
        if len(self.raw_events) > 10000:
            self.raw_events = self.raw_events[-10000:]

        sym = event.symbol.upper()
        targets = [sym]
        if "ALL_MARKET" in self.symbols and sym != "ALL_MARKET":
            targets.append("ALL_MARKET")

        for tf in TIMEFRAMES:
            start_dt, end_dt = self.get_candle_bounds(event.timestamp_utc, tf)
            start_epoch = int(start_dt.timestamp())
            start_ist = start_dt.astimezone(IST_TIMEZONE).strftime("%Y-%m-%d %H:%M:%S IST")
            end_ist = end_dt.astimezone(IST_TIMEZONE).strftime("%Y-%m-%d %H:%M:%S IST")
            start_utc = start_dt.strftime("%Y-%m-%d %H:%M:%S UTC")
            end_utc = end_dt.strftime("%Y-%m-%d %H:%M:%S UTC")

            for s in targets:
                if s not in self.buckets[tf]:
                    self.buckets[tf][s] = {}

                if start_epoch not in self.buckets[tf][s]:
                    self.buckets[tf][s][start_epoch] = {
                        "symbol": s,
                        "timeframe": tf,
                        "candle_start_epoch": start_epoch,
                        "candle_start_ist": start_ist,
                        "candle_end_ist": end_ist,
                        "candle_start_utc": start_utc,
                        "candle_end_utc": end_utc,
                        "long_liq_usd": 0.0,
                        "short_liq_usd": 0.0,
                        "total_liq_usd": 0.0,
                        "net_liq_delta_usd": 0.0,
                        "orders_count": 0,
                        "dominant_side": "BALANCED",
                    }

                b = self.buckets[tf][s][start_epoch]
                b["orders_count"] += 1
                b["total_liq_usd"] = round(b["total_liq_usd"] + event.usd_value, 2)
                
                # Side == "SELL" means a LONG was liquidated (forced sell)
                # Side == "BUY" means a SHORT was liquidated (forced buy)
                if event.side.upper() in ("SELL", "LONG"):
                    b["long_liq_usd"] = round(b["long_liq_usd"] + event.usd_value, 2)
                else:
                    b["short_liq_usd"] = round(b["short_liq_usd"] + event.usd_value, 2)

                # Net Delta: Short Liq - Long Liq
                # Positive delta = short squeeze / buying pressure
                # Negative delta = long flush / selling pressure
                b["net_liq_delta_usd"] = round(b["short_liq_usd"] - b["long_liq_usd"], 2)

                if b["short_liq_usd"] > b["long_liq_usd"] * 1.5 and b["short_liq_usd"] > 10000:
                    b["dominant_side"] = "SHORTS_PURGED"
                elif b["long_liq_usd"] > b["short_liq_usd"] * 1.5 and b["long_liq_usd"] > 10000:
                    b["dominant_side"] = "LONGS_FLUSHED"
                else:
                    b["dominant_side"] = "BALANCED"

    def get_current_candle(self, symbol: str, timeframe: str, dt: Optional[datetime.datetime] = None) -> Optional[Dict]:
        """Retrieves the active or closest candle for a symbol and timeframe."""
        if dt is None:
            dt = datetime.datetime.now(datetime.timezone.utc)
        start_dt, _ = self.get_candle_bounds(dt, timeframe)
        start_epoch = int(start_dt.timestamp())
        sym = symbol.upper()
        return self.buckets.get(timeframe, {}).get(sym, {}).get(start_epoch)

    def get_all_candles_sorted(self, limit: int = 500) -> List[Dict]:
        """Returns flattened list of aggregated candles sorted newest to oldest."""
        all_candles = []
        for tf in TIMEFRAMES:
            for sym, epoch_dict in self.buckets[tf].items():
                for b in epoch_dict.values():
                    all_candles.append(b)
        
        # Sort by candle_start_epoch descending, then symbol
        all_candles.sort(key=lambda x: (x["candle_start_epoch"], x["total_liq_usd"]), reverse=True)
        return all_candles[:limit]

    def save_buffer(self, buffer_path: pathlib.Path = BUFFER_FILE) -> bool:
        """Persists current buckets and recorded history to disk buffer."""
        try:
            buffer_path.parent.mkdir(parents=True, exist_ok=True)
            data = {
                "saved_at_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
                "buckets": self.buckets,
                "raw_events_count": len(self.raw_events)
            }
            tmp_path = buffer_path.with_suffix(".tmp")
            with open(tmp_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            tmp_path.replace(buffer_path)
            return True
        except Exception as e:
            logger.warning("Error saving forced liquidation buffer: %s", e)
            return False

    def load_buffer(self, buffer_path: pathlib.Path = BUFFER_FILE) -> int:
        """Restores previously recorded multi-timeframe buckets from disk buffer."""
        if not buffer_path.exists():
            return 0
        try:
            with open(buffer_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            loaded_buckets = data.get("buckets", {})
            restored_count = 0
            for tf in TIMEFRAMES:
                if tf not in loaded_buckets:
                    continue
                for sym, epoch_dict in loaded_buckets[tf].items():
                    if sym not in self.buckets[tf]:
                        self.buckets[tf][sym] = {}
                    for epoch_str, candle in epoch_dict.items():
                        epoch_int = int(epoch_str)
                        if epoch_int not in self.buckets[tf][sym]:
                            self.buckets[tf][sym][epoch_int] = candle
                            restored_count += 1
                        else:
                            existing = self.buckets[tf][sym][epoch_int]
                            if candle.get("total_liq_usd", 0) > existing.get("total_liq_usd", 0):
                                self.buckets[tf][sym][epoch_int] = candle
            logger.info("Successfully loaded %d historical candles from disk buffer %s", restored_count, buffer_path.name)
            return restored_count
        except Exception as e:
            logger.warning("Error loading forced liquidation buffer: %s", e)
            return 0

    def bootstrap_from_parquet_live_liq(self) -> int:
        """Bootstraps historical liquidations from Data/feeds/7_Live_Liq.parquet."""
        p_path = DATA_DIR / "feeds" / "7_Live_Liq.parquet"
        if not p_path.exists():
            return 0
        try:
            import pyarrow.parquet as pq
            table = pq.read_table(p_path)
            rows = table.to_pylist()
            count = 0
            now_dt = datetime.datetime.now(datetime.timezone.utc)
            for r in rows:
                pair = str(r.get("Coin___Pair", r.get("coin", ""))).upper()
                side_str = str(r.get("Side", r.get("side", ""))).upper()
                px_val = r.get("Price", r.get("price", 0.0))
                amt_val = r.get("Amount", r.get("amount", 0.0))
                ts_str = str(r.get("Timestamp_IST", r.get("timestamp_ist", "")))

                try:
                    price = float(str(px_val).replace("$", "").replace(",", "").strip())
                    s_amt = str(amt_val).replace("$", "").replace(",", "").strip()
                    mult = 1.0
                    if s_amt.endswith("K"): mult = 1e3; s_amt = s_amt[:-1]
                    elif s_amt.endswith("M"): mult = 1e6; s_amt = s_amt[:-1]
                    elif s_amt.endswith("B"): mult = 1e9; s_amt = s_amt[:-1]
                    usd_val = float(s_amt) * mult
                    qty = usd_val / price if price > 0 else 0.0
                except Exception:
                    continue

                ev_time = now_dt
                if "IST" in ts_str:
                    try:
                        clean_ts = ts_str.replace(" IST", "").strip()
                        dt_ist = datetime.datetime.strptime(clean_ts, "%Y-%m-%d %H:%M:%S").replace(tzinfo=IST_TIMEZONE)
                        ev_time = dt_ist.astimezone(UTC_TIMEZONE)
                    except Exception:
                        pass

                side = "SELL" if "LONG" in side_str else "BUY"
                ev = LiquidationEvent(
                    symbol=pair,
                    side=side,
                    price=price,
                    quantity=qty,
                    usd_value=usd_val,
                    timestamp_utc=ev_time,
                    exchange=str(r.get("Exchange", "CoinGlass"))
                )
                self.ingest_event(ev)
                count += 1
            logger.info("Successfully bootstrapped %d historical liquidation events from Parquet 7_Live_Liq", count)
            return count
        except Exception as e:
            logger.warning("Error bootstrapping from 7_Live_Liq.parquet: %s", e)
            return 0

class ForcedLiquidationDaemon:
    def __init__(self):
        self.aggregator = ForcedLiquidationAggregator()
        self.is_running = False
        self.last_dump_time = 0.0
        self.dump_interval_seconds = 120.0  # Update Parquet and Buffer every 120s

    async def connect_binance_websocket(self):
        """Continuously streams from Binance Futures !forceOrder@arr."""
        if websockets is None:
            logger.error("websockets library missing. Cannot connect to Binance stream.")
            return

        uri = "wss://fstream.binance.com/ws/!forceOrder@arr"
        while self.is_running:
            try:
                logger.info("Connecting to Binance Futures liquidation feed: %s", uri)
                async with websockets.connect(uri, open_timeout=15, ping_interval=20, ping_timeout=20) as ws:
                    logger.info("Connected to Binance Liquidation Stream! Ingesting forced orders in real-time...")
                    while self.is_running:
                        msg = await ws.recv()
                        data = json.loads(msg)
                        o = data.get("o", {})
                        symbol = o.get("s")
                        side = o.get("S")
                        price = float(o.get("ap") or o.get("p") or 0.0)
                        qty = float(o.get("q") or o.get("z") or 0.0)
                        usd_val = price * qty
                        t_ms = o.get("T") or data.get("E") or (time.time() * 1000)
                        ev_dt = datetime.datetime.fromtimestamp(t_ms / 1000.0, tz=UTC_TIMEZONE)

                        if symbol and price > 0 and qty > 0:
                            ev = LiquidationEvent(
                                symbol=symbol,
                                side=side,
                                price=price,
                                quantity=qty,
                                usd_value=round(usd_val, 2),
                                timestamp_utc=ev_dt,
                                exchange="Binance Futures"
                            )
                            self.aggregator.ingest_event(ev)
                            
                        # Check periodic dump & buffer persistence
                        if time.time() - self.last_dump_time >= self.dump_interval_seconds:
                            self.aggregator.save_buffer(BUFFER_FILE)
                            self.dump_to_parquet()
            except Exception as e:
                logger.warning("Binance WebSocket disconnected: %s. Reconnecting in 5s...", e)
                await asyncio.sleep(5)

    def dump_to_parquet(self) -> bool:
        """Dumps aggregated multi-timeframe candles to Data/feeds/22_Forced_Liquidations_MTF.parquet."""
        candles = self.aggregator.get_all_candles_sorted(limit=1000)
        if not candles:
            return False

        try:
            write_parquet_feed("22_Forced_Liquidations_MTF", candles)
            self.last_dump_time = time.time()
            logger.info("Successfully updated 22_Forced_Liquidations_MTF.parquet with %d candles", len(candles))
            return True
        except Exception as e:
            logger.error("Could not write Parquet feed 22_Forced_Liquidations_MTF: %s", e)
            return False

    def run(self):
        """Main daemon synchronous entrypoint."""
        self.is_running = True
        logger.info("Starting Forced Liquidation Aggregator Daemon (Pure Parquet)...")
        # Step 1: Restore previously recorded candles from disk buffer (zero data loss)
        self.aggregator.load_buffer(BUFFER_FILE)
        # Step 2: Bootstrap existing records from 7_Live_Liq.parquet
        self.aggregator.bootstrap_from_parquet_live_liq()
        # Step 3: Save merged buffer to disk immediately
        self.aggregator.save_buffer(BUFFER_FILE)
        # Step 4: Initial Parquet dump
        self.dump_to_parquet()
        # Step 5: Run continuous real-time WebSocket ingestion
        asyncio.run(self.connect_binance_websocket())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Forced Liquidation Multi-Timeframe Daemon")
    parser.add_argument("--test-run", action="store_true", help="Run once, bootstrap from 7_Live_Liq.parquet and dump to Parquet")
    args = parser.parse_args()

    daemon = ForcedLiquidationDaemon()
    if args.test_run:
        logger.info("Running single-pass test run...")
        daemon.aggregator.bootstrap_from_parquet_live_liq()
        ok = daemon.dump_to_parquet()
        print(f"Test run completed: success={ok}")
        sys.exit(0 if ok else 1)
    else:
        daemon.run()
