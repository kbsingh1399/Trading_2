"""
Terminal/Heatmap_Engine.py
Real-Time & Historical Candle-Level Liquidation & Stop Heatmap Engine.
Captures, synchronizes, and records 2D orderflow liquidation cascades and stop-loss clusters
at each discrete candle interval, continuously updating the active candle in real time.
"""
from __future__ import annotations
import json
import pathlib
import time
from typing import Dict, List, Any, Optional
import polars as pl
import pandas as pd
from Terminal.Api_Client import HyperdashClient


class HeatmapEngine:
    """
    Engine to capture, align, and persist candle-level liquidation and stop-loss distributions.
    Maintains a live, rolling candle-level historical parquet file and in-memory cache.
    """

    def __init__(
        self,
        coin: str = "BTC",
        timeframe: str = "1h",
        lookback_days: int = 3,
        storage_dir: str = "Data/Hyperdash_Historical"
    ):
        self.coin = coin.upper()
        self.timeframe = timeframe
        self.lookback_days = lookback_days
        self.storage_dir = pathlib.Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self.parquet_path = self.storage_dir / f"{self.coin}_{self.timeframe}_candle_heatmap.parquet"

        self.client = HyperdashClient()
        self.last_sync_ts: float = 0.0
        self.cached_candles: List[Dict[str, Any]] = []
        self.cached_liq_matrix: Dict[str, Any] = {}
        self.cached_stop_matrix: Dict[str, Any] = {}
        self.cached_current_candle: Dict[str, Any] = {}

    def sync_data(self, force: bool = False) -> Dict[str, Any]:
        """
        Synchronize candles, liquidations, and stops from Hyperliquid/Hyperdash.
        Re-fetches if older than 5 seconds or if force=True.
        """
        now = time.time()
        if not force and (now - self.last_sync_ts < 5.0) and self.cached_current_candle:
            return self.get_summary()

        # 1. Fetch current price to determine dynamic price bounds
        all_assets = self.client.fetch_all_assets()
        mark_px = 85000.0
        for a in all_assets:
            if a["coin"] == self.coin:
                mark_px = a["mark_px"]
                break

        # Dynamic price range (+/- 20% around mark price)
        min_px = mark_px * 0.80
        max_px = mark_px * 1.20

        # Dynamic lookback based on timeframe
        lookback = self.lookback_days
        if self.timeframe == "1d":
            lookback = max(lookback, 30)
        elif self.timeframe == "4h":
            lookback = max(lookback, 14)
        elif self.timeframe == "1h":
            lookback = max(lookback, 4)
        elif self.timeframe == "15m":
            lookback = max(lookback, 2)

        # 2. Fetch candles, liquidations, and stops
        candles = self.client.fetch_candles(self.coin, interval=self.timeframe, lookback_days=lookback)
        liqs = self.client.fetch_liquidations(self.coin, min_price=min_px, max_price=max_px, lookback_days=min(lookback, 7))
        stops = self.client.fetch_stops(self.coin, min_price=min_px, max_price=max_px, lookback_days=min(lookback, 7))

        self.cached_candles = candles
        self.cached_liq_matrix = liqs
        self.cached_stop_matrix = stops
        self.last_sync_ts = now

        # 3. Fuse data at each candle level
        records = []
        liq_by_candle = liqs.get("candle_snapshots", {})
        stop_by_candle = stops.get("candle_snapshots", {})

        for c in candles:
            dt_str = c["datetime"]
            # Hyperdash timestamps are formatted like 'YYYY-MM-DD HH:00:00'
            c_liqs = liq_by_candle.get(dt_str, [])
            c_stops = stop_by_candle.get(dt_str, [])

            # Compute liquidation breakdown for this candle
            long_liq_usd = 0.0
            short_liq_usd = 0.0
            peak_liq_px = 0.0
            peak_liq_amt = 0.0

            for b in c_liqs:
                amt = float(b.get("amount", 0.0))
                abs_amt = abs(amt)
                mid_px = float(b.get("mid_px", 0.0))
                if mid_px < c["close"] or amt > 0:
                    long_liq_usd += abs_amt
                else:
                    short_liq_usd += abs_amt
                if abs_amt > peak_liq_amt:
                    peak_liq_amt = abs_amt
                    peak_liq_px = mid_px

            total_liq_usd = long_liq_usd + short_liq_usd

            # Compute stop breakdown for this candle
            buy_stops_usd = 0.0
            sell_stops_usd = 0.0
            peak_stop_px = 0.0
            peak_stop_amt = 0.0

            for s in c_stops:
                amt = float(s.get("amount", 0.0))
                abs_amt = abs(amt)
                mid_px = float(s.get("mid_px", 0.0))
                if mid_px > c["close"]:
                    buy_stops_usd += abs_amt
                else:
                    sell_stops_usd += abs_amt
                if abs_amt > peak_stop_amt:
                    peak_stop_amt = abs_amt
                    peak_stop_px = mid_px

            total_stops_usd = buy_stops_usd + sell_stops_usd

            record = {
                "timestamp": c["timestamp"],
                "datetime": dt_str,
                "coin": self.coin,
                "open": c["open"],
                "high": c["high"],
                "low": c["low"],
                "close": c["close"],
                "volume": c["volume"],
                "trades": c["trades"],
                # Liquidation stats for this candle
                "liq_total_usd": total_liq_usd,
                "liq_long_usd": long_liq_usd,
                "liq_short_usd": short_liq_usd,
                "liq_peak_price": peak_liq_px,
                "liq_peak_amount": peak_liq_amt,
                # Stop stats for this candle
                "stop_total_usd": total_stops_usd,
                "stop_buy_usd": buy_stops_usd,
                "stop_sell_usd": sell_stops_usd,
                "stop_peak_price": peak_stop_px,
                "stop_peak_amount": peak_stop_amt,
                # Serialized full distributions for exact level re-construction
                "liq_bands_count": len(c_liqs),
                "stop_bands_count": len(c_stops),
            }
            records.append(record)

        # 4. Save/update to Parquet file
        if records:
            df = pl.DataFrame(records).sort("timestamp")
            df.write_parquet(self.parquet_path)

            # Store current (latest) candle in memory
            latest = records[-1]
            latest["current_price"] = mark_px
            latest["liq_bands"] = c_liqs
            latest["stop_bands"] = c_stops
            self.cached_current_candle = latest

        return self.get_summary()

    def get_summary(self) -> Dict[str, Any]:
        """Return the current candle status and overall snapshot."""
        if not self.cached_current_candle:
            self.sync_data(force=True)
        return {
            "coin": self.coin,
            "timeframe": self.timeframe,
            "current_candle": self.cached_current_candle,
            "total_candles": len(self.cached_candles),
            "parquet_file": str(self.parquet_path),
            "last_sync": self.last_sync_ts
        }

    def get_chart_heatmap_payload(self, mode: str = "liquidations", granularity: str = "medium") -> Dict[str, Any]:
        """
        Build the full payload required by the interactive Chrome Heatmap chart.
        mode can be 'liquidations' or 'stops'.
        granularity can be 'fine', 'medium', or 'coarse'.
        """
        self.sync_data(force=False)

        candles = self.cached_candles
        matrix_data = self.cached_liq_matrix if mode == "liquidations" else self.cached_stop_matrix
        candle_snapshots = matrix_data.get("candle_snapshots", {})

        # Extract all distinct price bands
        all_bands = matrix_data.get("bands", [])
        price_bands = [{"min_px": b["min_px"], "max_px": b["max_px"], "mid_px": b["mid_px"]} for b in all_bands]
        price_bands.sort(key=lambda x: x["mid_px"])

        # Extract 2D grid: for each candle, get distribution.
        # GraphQL historicalData is sampled at 1-hour granularity.
        # For sub-hourly timeframes (15m, 4h intra) candles that fall between
        # hourly snapshots, carry forward the most recent preceding snapshot.
        heatmap_grid = []
        max_cell_usd = 1.0

        # Pre-sort snapshot keys chronologically for binary search
        import bisect
        sorted_snap_keys = sorted(candle_snapshots.keys())

        def _get_levels_with_fallback(dt_str: str) -> list:
            """Exact match first; fall back to most-recent preceding snapshot."""
            levels = candle_snapshots.get(dt_str)
            if levels is not None:
                return levels
            # Binary search: find the largest key <= dt_str
            idx = bisect.bisect_right(sorted_snap_keys, dt_str) - 1
            if idx >= 0:
                return candle_snapshots[sorted_snap_keys[idx]]
            # No preceding observation: never use a future snapshot. Returning
            # it would leak information into the first candles of a backtest.
            return []

        for c in candles:
            dt_str = c["datetime"]
            levels = _get_levels_with_fallback(dt_str)
            cell_map = {}
            for lvl in levels:
                val = abs(float(lvl.get("amount", 0.0)))
                px = float(lvl["mid_px"])
                cell_map[f"{px:.1f}"] = val
                cell_map[f"{px:.2f}"] = val
                cell_map[str(round(px, 1))] = val
                cell_map[str(int(px))] = val
                if val > max_cell_usd:
                    max_cell_usd = val

            heatmap_grid.append({
                "time": dt_str,
                "timestamp": c["timestamp"],
                "levels": cell_map
            })

        # Compute Volume Profile along right price axis (as seen in Hyperdash Chart view)
        mark_px = self.cached_current_candle.get("close", 0.0) or (candles[-1]["close"] if candles else 2600.0)
        raw_profile = []
        for b in all_bands:
            amt = abs(float(b.get("amount", 0.0)))
            mid = float(b.get("mid_px", 0.0))
            if amt > 0:
                is_above = mid >= mark_px
                if mode == "liquidations":
                    side = "SHORT" if is_above else "LONG"
                    col = "rgba(0, 255, 136, 0.85)" if is_above else "rgba(246, 70, 93, 0.85)"
                else:
                    side = "BUY" if is_above else "SELL"
                    col = "rgba(0, 240, 255, 0.85)" if is_above else "rgba(255, 215, 0, 0.85)"

                raw_profile.append({
                    "min_px": b.get("min_px", 0.0),
                    "max_px": b.get("max_px", 0.0),
                    "mid_px": mid,
                    "amount": amt,
                    "side": side,
                    "color": col
                })

        raw_profile.sort(key=lambda x: x["mid_px"])

        # Granularity aggregation
        profile = raw_profile
        if granularity == "coarse" and len(raw_profile) > 8:
            merged = []
            for i in range(0, len(raw_profile), 4):
                chunk = raw_profile[i:i+4]
                merged.append({
                    "min_px": chunk[0]["min_px"],
                    "max_px": chunk[-1]["max_px"],
                    "mid_px": (chunk[0]["min_px"] + chunk[-1]["max_px"]) / 2.0,
                    "amount": sum(c["amount"] for c in chunk),
                    "side": chunk[0]["side"],
                    "color": chunk[0]["color"]
                })
            profile = merged
        elif granularity == "medium" and len(raw_profile) > 8:
            merged = []
            for i in range(0, len(raw_profile), 2):
                chunk = raw_profile[i:i+2]
                merged.append({
                    "min_px": chunk[0]["min_px"],
                    "max_px": chunk[-1]["max_px"],
                    "mid_px": (chunk[0]["min_px"] + chunk[-1]["max_px"]) / 2.0,
                    "amount": sum(c["amount"] for c in chunk),
                    "side": chunk[0]["side"],
                    "color": chunk[0]["color"]
                })
            profile = merged

        max_profile_usd = max((p["amount"] for p in profile), default=1.0)

        return {
            "coin": self.coin,
            "mode": mode,
            "granularity": granularity,
            "timeframe": self.timeframe,
            "candles": candles,
            "price_bands": price_bands,
            "heatmap_grid": heatmap_grid,
            "volume_profile": profile,
            "max_profile_usd": max_profile_usd,
            "max_intensity_usd": max_cell_usd,
            "current_candle": self.cached_current_candle,
            "total_long_size": matrix_data.get("total_long_size", 0.0) if mode == "liquidations" else matrix_data.get("total_buy_size", 0.0),
            "total_short_size": matrix_data.get("total_short_size", 0.0) if mode == "liquidations" else matrix_data.get("total_sell_size", 0.0),
        }
