#!/usr/bin/env python3
"""
Terminal/Data_Factory/forced_liquidation_daemon.py
===================================================
Always-On Multi-Timeframe Forced Liquidation Aggregator & Excel Sync Daemon.
Aggregates live forced liquidation events across 5m, 15m, 1h, and 4h candles
with explicit dual IST (UTC+5:30) and UTC timestamps.

Features:
  1. Subscribes to Binance Futures '!forceOrder@arr' real-time WebSocket.
  2. Ingests existing Sheet '7_Live_Liq' / CoinGlass rows for historical bootstrap.
  3. Maintains rolling time-bucketed candles (5m, 15m, 1h, 4h) per asset & market-wide.
  4. Computes Long Liq USD, Short Liq USD, Net Delta, Order Count, and Dominant Flow.
  5. Periodically triggers Excel dump to Sheet '22_Forced_Liquidations_MTF' in Data/DataBase_Trading.xlsx.
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
DATA_DIR = ROOT / "Data"
BUFFER_FILE = DATA_DIR / "forced_liquidations_buffer.json"
EXCEL_PATH = DATA_DIR / "DataBase_Trading.xlsx"

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

    def bootstrap_from_excel_live_liq(self, excel_path: pathlib.Path) -> int:
        """Bootstraps historical liquidations from Sheet 7_Live_Liq if available."""
        if not excel_path.exists():
            return 0
        try:
            import openpyxl
            wb = openpyxl.load_workbook(excel_path, read_only=True, data_only=True)
            if "7_Live_Liq" not in wb.sheetnames:
                return 0
            
            ws = wb["7_Live_Liq"]
            count = 0
            now_dt = datetime.datetime.now(datetime.timezone.utc)
            
            for row in ws.iter_rows(min_row=3, values_only=True):
                if not row or len(row) < 5 or row[0] is None:
                    continue
                # Columns: #, Coin / Pair, Side, Price, Amount, Time, Exchange, Timestamp (IST)
                pair = str(row[1]).upper()
                side_str = str(row[2]).upper()
                price_str = str(row[3]).replace("$", "").replace(",", "").strip()
                amt_str = str(row[4]).replace("$", "").replace(",", "").strip()
                ts_str = str(row[7]) if len(row) > 7 else ""
                
                try:
                    price = float(price_str)
                    multiplier = 1.0
                    if amt_str.endswith("K"):
                        multiplier = 1e3
                        amt_clean = amt_str[:-1]
                    elif amt_str.endswith("M"):
                        multiplier = 1e6
                        amt_clean = amt_str[:-1]
                    elif amt_str.endswith("B"):
                        multiplier = 1e9
                        amt_clean = amt_str[:-1]
                    else:
                        amt_clean = amt_str
                    usd_val = float(amt_clean) * multiplier
                    qty = usd_val / price if price > 0 else 0.0
                except (ValueError, TypeError):
                    continue

                # Parse timestamp if available: "YYYY-MM-DD HH:MM:SS IST"
                ev_time = now_dt
                if "IST" in ts_str:
                    try:
                        clean_ts = ts_str.replace(" IST", "").strip()
                        dt_ist = datetime.datetime.strptime(clean_ts, "%Y-%m-%d %H:%M:%S").replace(tzinfo=IST_TIMEZONE)
                        ev_time = dt_ist.astimezone(UTC_TIMEZONE)
                    except Exception:
                        pass
                
                # Invert side naming if CoinGlass uses Long/Short
                # Long position liquidation = SELL order
                # Short position liquidation = BUY order
                side = "SELL" if "LONG" in side_str else "BUY"
                
                ev = LiquidationEvent(
                    symbol=pair,
                    side=side,
                    price=price,
                    quantity=qty,
                    usd_value=usd_val,
                    timestamp_utc=ev_time,
                    exchange=str(row[6]) if len(row) > 6 else "CoinGlass"
                )
                self.ingest_event(ev)
                count += 1
                
            logger.info("Successfully bootstrapped %d historical liquidation events from Sheet 7_Live_Liq", count)
            return count
        except Exception as e:
            logger.warning("Error bootstrapping from 7_Live_Liq: %s", e)
            return 0


class ForcedLiquidationDaemon:
    def __init__(self, excel_path: pathlib.Path = EXCEL_PATH):
        self.excel_path = excel_path
        self.aggregator = ForcedLiquidationAggregator()
        self.is_running = False
        self.last_dump_time = 0.0
        self.dump_interval_seconds = 30.0  # Update Excel every 30s

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
                        # Payload schema:
                        # {"e":"forceOrder","E":1568014460893,"o":{"s":"BTCUSDT","S":"SELL","q":"0.014","p":"9910","ap":"9910","T":1568014460890}}
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
                            
                        # Check periodic dump
                        if time.time() - self.last_dump_time >= self.dump_interval_seconds:
                            self.dump_to_excel()
            except Exception as e:
                logger.warning("Binance WebSocket disconnected: %s. Reconnecting in 5s...", e)
                await asyncio.sleep(5)

    def dump_to_excel(self) -> bool:
        """Dumps aggregated multi-timeframe candles to Sheet 22_Forced_Liquidations_MTF."""
        try:
            from Data.Excel_Modules._22_Forced_Liquidations_MTF import dump_forced_liquidations_to_excel
        except ImportError:
            try:
                # Add root to sys.path
                if str(ROOT) not in sys.path:
                    sys.path.insert(0, str(ROOT))
                from Data.Excel_Modules._22_Forced_Liquidations_MTF import dump_forced_liquidations_to_excel
            except Exception as e:
                logger.error("Could not import Excel writer module: %s", e)
                return False

        candles = self.aggregator.get_all_candles_sorted(limit=1000)
        if not candles:
            return False

        success = dump_forced_liquidations_to_excel(candles, target_path=self.excel_path)
        if success:
            self.last_dump_time = time.time()
            logger.info("Successfully updated Sheet 22_Forced_Liquidations_MTF with %d candles", len(candles))
        return success

    def run(self):
        """Main daemon synchronous entrypoint."""
        self.is_running = True
        logger.info("Starting Forced Liquidation Aggregator Daemon...")
        # Step 1: Bootstrap existing records from Sheet 7_Live_Liq
        self.aggregator.bootstrap_from_excel_live_liq(self.excel_path)
        # Step 2: Initial Excel dump
        self.dump_to_excel()
        # Step 3: Run event loop for real-time WebSocket
        asyncio.run(self.connect_binance_websocket())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Forced Liquidation Multi-Timeframe Daemon")
    parser.add_argument("--test-run", action="store_true", help="Run once, bootstrap from 7_Live_Liq and dump to Excel")
    args = parser.parse_args()

    daemon = ForcedLiquidationDaemon()
    if args.test_run:
        logger.info("Running single-pass test run...")
        daemon.aggregator.bootstrap_from_excel_live_liq(EXCEL_PATH)
        ok = daemon.dump_to_excel()
        print(f"Test run completed: success={ok}")
        sys.exit(0 if ok else 1)
    else:
        daemon.run()
