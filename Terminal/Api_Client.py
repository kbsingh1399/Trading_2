"""
Hyperdash & Hyperliquid Production API Client
Fetches real-time Level 2, Level 3 (with wallet addresses), Liquidations,
Stops, Whale Positions, and Historical OHLCV/Funding data via native APIs.
"""

import urllib.request
import urllib.error
import json
import time
import pathlib
from typing import Dict, List, Any, Optional
import polars as pl

HL_INFO_URL = "https://api.hyperliquid.xyz/info"
HD_GRAPHQL_URL = "https://api.hyperdash.com/graphql"
DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

class HyperdashClient:
    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.asset_cache: Dict[str, Any] = {}
        self.universe: List[str] = []

    def _post_json(self, url: str, payload: dict) -> dict:
        data_bytes = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data_bytes, headers=DEFAULT_HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            err_msg = e.read().decode("utf-8", errors="ignore")
            raise RuntimeError(f"HTTP {e.code} Error from {url}: {err_msg}")
        except Exception as e:
            raise RuntimeError(f"Connection Error to {url}: {e}")

    def fetch_all_assets(self) -> List[Dict[str, Any]]:
        """Fetch all active perpetual assets on Hyperliquid with live stats."""
        payload = {"type": "metaAndAssetCtxs"}
        data = self._post_json(HL_INFO_URL, payload)
        meta_universe = data[0]["universe"]
        asset_ctxs = data[1]

        results = []
        self.universe = []
        for meta, ctx in zip(meta_universe, asset_ctxs):
            coin = meta["name"]
            self.universe.append(coin)
            mark_px = float(ctx.get("markPx", 0.0))
            oi = float(ctx.get("openInterest", 0.0))
            funding = float(ctx.get("funding", 0.0))
            volume_24h = float(ctx.get("dayNtlVlm", 0.0))
            prev_day_px = float(ctx.get("prevDayPx", mark_px))
            change_24h = ((mark_px - prev_day_px) / prev_day_px * 100.0) if prev_day_px > 0 else 0.0

            item = {
                "coin": coin,
                "mark_px": mark_px,
                "open_interest": oi,
                "open_interest_usd": oi * mark_px,
                "funding_rate": funding,
                "funding_annualized": funding * 3 * 365 * 100, # 8h to annual %
                "volume_24h": volume_24h,
                "change_24h": change_24h,
                "max_leverage": meta.get("maxLeverage", 50),
                "sz_decimals": meta.get("szDecimals", 2)
            }
            results.append(item)
            self.asset_cache[coin] = item

        # Sort by 24h volume descending
        results.sort(key=lambda x: x["volume_24h"], reverse=True)
        return results

    def fetch_l2_book(self, coin: str) -> Dict[str, Any]:
        """Fetch real-time Level 2 orderbook (20 bids, 20 asks) with depth metrics."""
        payload = {"type": "l2Book", "coin": coin}
        raw = self._post_json(HL_INFO_URL, payload)
        levels = raw.get("levels", [[], []])
        raw_bids = levels[0]
        raw_asks = levels[1]

        bids = [{"price": float(b["px"]), "size": float(b["sz"]), "total_usd": float(b["px"]) * float(b["sz"])} for b in raw_bids]
        asks = [{"price": float(a["px"]), "size": float(a["sz"]), "total_usd": float(a["px"]) * float(a["sz"])} for a in raw_asks]

        best_bid = bids[0]["price"] if bids else 0.0
        best_ask = asks[0]["price"] if asks else 0.0
        spread = best_ask - best_bid if (best_bid and best_ask) else 0.0
        spread_bps = (spread / best_bid * 10000.0) if best_bid > 0 else 0.0

        bid_vol = sum(b["total_usd"] for b in bids)
        ask_vol = sum(a["total_usd"] for a in asks)
        total_vol = bid_vol + ask_vol
        bid_ratio = (bid_vol / total_vol * 100.0) if total_vol > 0 else 50.0

        return {
            "coin": coin,
            "best_bid": best_bid,
            "best_ask": best_ask,
            "spread": spread,
            "spread_bps": spread_bps,
            "bids": bids,
            "asks": asks,
            "bid_volume_usd": bid_vol,
            "ask_volume_usd": ask_vol,
            "bid_pct": bid_ratio,
            "ask_pct": 100.0 - bid_ratio,
            "timestamp": raw.get("time", int(time.time() * 1000))
        }

    def fetch_l3_orders(self, coin: str, min_price: float, max_price: float) -> List[Dict[str, Any]]:
        """
        Fetch individual Level 3 resting orders mapped to specific Ethereum wallet addresses.
        Powers the Hyperdash Level 3 orderbook overlay.
        """
        query = """
        query GetOrderbookSnapshotFiltered($market: String!, $minPrice: Float!, $maxPrice: Float!) {
          orderbookSnapshotFiltered(market: $market, minPrice: $minPrice, maxPrice: $maxPrice) {
            address
            order {
              coin
              side
              limitPx
              sz
            }
          }
        }
        """
        variables = {"market": coin, "minPrice": float(min_price), "maxPrice": float(max_price)}
        data = self._post_json(HD_GRAPHQL_URL, {"query": query, "variables": variables})
        orders_raw = data.get("data", {}).get("orderbookSnapshotFiltered", [])

        orders = []
        for o in orders_raw:
            sub = o.get("order", {})
            px = float(sub.get("limitPx", 0.0))
            sz = float(sub.get("sz", 0.0))
            orders.append({
                "address": o.get("address", ""),
                "side": "BUY" if sub.get("side") == "B" else "SELL",
                "price": px,
                "size": sz,
                "notional_usd": px * sz
            })

        # Sort by notional value descending (whales first)
        orders.sort(key=lambda x: x["notional_usd"], reverse=True)
        return orders

    def fetch_liquidations(self, coin: str, min_price: float, max_price: float, lookback_days: int = 3) -> Dict[str, Any]:
        """Fetch real-time liquidation clusters, totals, and top liquidation whale addresses."""
        query = """
        query GetLiquidationLevelsV2(
          $coin: String!
          $minPrice: Float!
          $maxPrice: Float!
          $startTime: Float!
          $endTime: Float
        ) {
          analytics {
            liquidationLevels: liquidationLevelsV2(
              coin: $coin
              minPrice: $minPrice
              maxPrice: $maxPrice
              startTime: $startTime
              endTime: $endTime
            ) {
              coin
              currentPrice
              bandSize
              minPrice
              maxPrice
              bands {
                minPrice
                maxPrice
                historicalData {
                  timestamp
                  totalAmount
                }
              }
              totalLongLiquidations {
                size
                count
              }
              totalShortLiquidations {
                size
                count
              }
              topLongLiquidations {
                address
                price
                size
              }
              topShortLiquidations {
                address
                price
                size
              }
            }
          }
        }
        """
        now = int(time.time())
        start_time = now - (lookback_days * 24 * 3600)
        variables = {
            "coin": coin,
            "minPrice": float(min_price),
            "maxPrice": float(max_price),
            "startTime": float(start_time),
            "endTime": float(now)
        }
        data = self._post_json(HD_GRAPHQL_URL, {"query": query, "variables": variables})
        res = data.get("data", {}).get("analytics", {}).get("liquidationLevels") or {}

        bands = []
        time_series_by_candle: Dict[str, List[Dict[str, Any]]] = {}
        candle_totals: Dict[str, float] = {}

        raw_bands = res.get("bands", [])
        for b in raw_bands:
            hist = b.get("historicalData", [])
            latest_amt = hist[-1]["totalAmount"] if hist else 0.0
            min_px = b.get("minPrice", 0.0)
            max_px = b.get("maxPrice", 0.0)
            mid_px = (min_px + max_px) / 2.0

            bands.append({
                "min_px": min_px,
                "max_px": max_px,
                "mid_px": mid_px,
                "amount": latest_amt
            })

            # Index every historical candle point
            # GraphQL timestamp is epoch seconds (int or str). Normalize to
            # "YYYY-MM-DD HH:MM:SS" UTC to match fetch_candles() datetime keys.
            for pt in hist:
                raw_ts = pt.get("timestamp")
                amt = float(pt.get("totalAmount", 0.0))
                if raw_ts is None:
                    continue
                try:
                    epoch_sec = int(float(raw_ts))
                    ts = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(epoch_sec))
                except (ValueError, TypeError, OSError):
                    ts = str(raw_ts)
                if ts not in time_series_by_candle:
                    time_series_by_candle[ts] = []
                    candle_totals[ts] = 0.0
                time_series_by_candle[ts].append({
                    "min_px": min_px,
                    "max_px": max_px,
                    "mid_px": mid_px,
                    "amount": amt
                })
                candle_totals[ts] += amt

        # Sort candle timestamps chronologically
        sorted_timestamps = sorted(time_series_by_candle.keys())
        latest_ts = sorted_timestamps[-1] if sorted_timestamps else None
        current_candle_distribution = time_series_by_candle.get(latest_ts, []) if latest_ts else []

        return {
            "coin": coin,
            "current_price": res.get("currentPrice", 0.0),
            "band_size": res.get("bandSize", 100.0),
            "total_long_size": res.get("totalLongLiquidations", {}).get("size", 0.0),
            "total_long_count": res.get("totalLongLiquidations", {}).get("count", 0),
            "total_short_size": res.get("totalShortLiquidations", {}).get("size", 0.0),
            "total_short_count": res.get("totalShortLiquidations", {}).get("count", 0),
            "top_long_whales": res.get("topLongLiquidations", []),
            "top_short_whales": res.get("topShortLiquidations", []),
            "bands": bands,
            "timestamps": sorted_timestamps,
            "candle_snapshots": time_series_by_candle,
            "candle_totals": candle_totals,
            "current_candle": {
                "timestamp": latest_ts,
                "total_amount": candle_totals.get(latest_ts, 0.0) if latest_ts else 0.0,
                "distribution": current_candle_distribution
            }
        }

    def fetch_stops(self, coin: str, min_price: float, max_price: float, lookback_days: int = 3) -> Dict[str, Any]:
        """Fetch live buy/sell stop orders, stop clusters, and top stop-loss whale addresses."""
        query = """
        query GetStopOrderLevelsV2(
          $coin: String!
          $minPrice: Float!
          $maxPrice: Float!
          $startTime: Float!
          $endTime: Float
        ) {
          analytics {
            stopOrderLevels: stopOrderLevelsV2(
              coin: $coin
              minPrice: $minPrice
              maxPrice: $maxPrice
              startTime: $startTime
              endTime: $endTime
            ) {
              coin
              currentPrice
              bandSize
              totalBuyStops {
                size
                count
              }
              totalSellStops {
                size
                count
              }
              topBuyStops {
                address
                price
                size
              }
              topSellStops {
                address
                price
                size
              }
              bands {
                minPrice
                maxPrice
                historicalData {
                  timestamp
                  totalAmount
                }
              }
            }
          }
        }
        """
        now = int(time.time())
        start_time = now - (lookback_days * 24 * 3600)
        variables = {
            "coin": coin,
            "minPrice": float(min_price),
            "maxPrice": float(max_price),
            "startTime": float(start_time),
            "endTime": float(now)
        }
        data = self._post_json(HD_GRAPHQL_URL, {"query": query, "variables": variables})
        res = data.get("data", {}).get("analytics", {}).get("stopOrderLevels") or {}

        bands = []
        time_series_by_candle: Dict[str, List[Dict[str, Any]]] = {}
        candle_totals: Dict[str, float] = {}

        raw_bands = res.get("bands", [])
        for b in raw_bands:
            hist = b.get("historicalData", [])
            latest_amt = hist[-1]["totalAmount"] if hist else 0.0
            min_px = b.get("minPrice", 0.0)
            max_px = b.get("maxPrice", 0.0)
            mid_px = (min_px + max_px) / 2.0

            bands.append({
                "min_px": min_px,
                "max_px": max_px,
                "mid_px": mid_px,
                "amount": latest_amt
            })

            # Index every historical candle point
            # GraphQL timestamp is epoch seconds (int or str). Normalize to
            # "YYYY-MM-DD HH:MM:SS" UTC to match fetch_candles() datetime keys.
            for pt in hist:
                raw_ts = pt.get("timestamp")
                amt = float(pt.get("totalAmount", 0.0))
                if raw_ts is None:
                    continue
                try:
                    epoch_sec = int(float(raw_ts))
                    ts = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(epoch_sec))
                except (ValueError, TypeError, OSError):
                    ts = str(raw_ts)
                if ts not in time_series_by_candle:
                    time_series_by_candle[ts] = []
                    candle_totals[ts] = 0.0
                time_series_by_candle[ts].append({
                    "min_px": min_px,
                    "max_px": max_px,
                    "mid_px": mid_px,
                    "amount": amt
                })
                candle_totals[ts] += amt

        # Sort candle timestamps chronologically
        sorted_timestamps = sorted(time_series_by_candle.keys())
        latest_ts = sorted_timestamps[-1] if sorted_timestamps else None
        current_candle_distribution = time_series_by_candle.get(latest_ts, []) if latest_ts else []

        return {
            "coin": coin,
            "current_price": res.get("currentPrice", 0.0),
            "band_size": res.get("bandSize", 100.0),
            "total_buy_size": res.get("totalBuyStops", {}).get("size", 0.0),
            "total_buy_count": res.get("totalBuyStops", {}).get("count", 0),
            "total_sell_size": res.get("totalSellStops", {}).get("size", 0.0),
            "total_sell_count": res.get("totalSellStops", {}).get("count", 0),
            "top_buy_whales": res.get("topBuyStops", []),
            "top_sell_whales": res.get("topSellStops", []),
            "bands": bands,
            "timestamps": sorted_timestamps,
            "candle_snapshots": time_series_by_candle,
            "candle_totals": candle_totals,
            "current_candle": {
                "timestamp": latest_ts,
                "total_amount": candle_totals.get(latest_ts, 0.0) if latest_ts else 0.0,
                "distribution": current_candle_distribution
            }
        }

    def fetch_top_traders(self, coin: str, limit: int = 20) -> List[Dict[str, Any]]:
        """Fetch top PnL positions and smart money wallets for the asset."""
        query = """
        query GetAssetTopTraders($coin: String!, $pnlLimit: Int) {
          analytics {
            winners: perpsTickerPositions(
              coin: $coin
              limit: $pnlLimit
              offset: 0
              sortBy: { field: unrealizedPnl, order: desc }
            ) {
              coin
              positions {
                address
                displayName
                label
                size
                notional
                entryPrice
                unrealizedPnl
                returnOnEquity
                leverage
              }
            }
          }
        }
        """
        variables = {"coin": coin, "pnlLimit": limit}
        data = self._post_json(HD_GRAPHQL_URL, {"query": query, "variables": variables})
        positions = data.get("data", {}).get("analytics", {}).get("winners", {}).get("positions", [])
        return positions

    def fetch_recent_trades(self, coin: str) -> List[Dict[str, Any]]:
        """Fetch latest tick trades with aggressor side."""
        payload = {"type": "recentTrades", "coin": coin}
        trades = self._post_json(HL_INFO_URL, payload)
        return trades

    def fetch_candles(self, coin: str, interval: str = "1h", lookback_days: int = 3) -> List[Dict[str, Any]]:
        """Fetch live OHLCV candles from Hyperliquid for charting & alignment."""
        now_ms = int(time.time() * 1000)
        start_ms = now_ms - (lookback_days * 24 * 3600 * 1000)
        payload = {
            "type": "candleSnapshot",
            "req": {
                "coin": coin,
                "interval": interval,
                "startTime": start_ms,
                "endTime": now_ms
            }
        }
        batch = self._post_json(HL_INFO_URL, payload)
        candles = []
        for c in (batch or []):
            candles.append({
                "timestamp": c["t"],
                "datetime": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(c["t"] / 1000)),
                "open": float(c["o"]),
                "high": float(c["h"]),
                "low": float(c["l"]),
                "close": float(c["c"]),
                "volume": float(c["v"]),
                "trades": int(c.get("n", 0))
            })
        return candles

    def download_historical_candles(
        self,
        coin: str,
        interval: str = "15m",
        days: int = 30,
        output_dir: str = "Data/Hyperdash_Historical"
    ) -> str:
        """
        Download historical OHLCV candles from Hyperliquid and save to a clean Parquet file.
        """
        out_path = pathlib.Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)
        file_path = out_path / f"{coin}_{interval}_historical.parquet"

        now = int(time.time() * 1000)
        start_time = now - (days * 24 * 3600 * 1000)
        all_candles = []

        curr_start = start_time
        print(f"Downloading historical {interval} candles for {coin} ({days} days)...", flush=True)

        while curr_start < now:
            payload = {
                "type": "candleSnapshot",
                "req": {
                    "coin": coin,
                    "interval": interval,
                    "startTime": curr_start,
                    "endTime": now
                }
            }
            batch = self._post_json(HL_INFO_URL, payload)
            if not batch:
                break

            all_candles.extend(batch)
            last_ts = batch[-1]["T"]
            if last_ts <= curr_start or len(batch) < 100:
                break
            curr_start = last_ts + 1
            time.sleep(0.1) # Respect exchange limits

        if not all_candles:
            raise RuntimeError(f"No candles retrieved for {coin}")

        # Deduplicate by timestamp
        seen = set()
        deduped = []
        for c in all_candles:
            t = c["t"]
            if t not in seen:
                seen.add(t)
                deduped.append({
                    "timestamp": c["t"],
                    "datetime": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(c["t"] / 1000)),
                    "open": float(c["o"]),
                    "high": float(c["h"]),
                    "low": float(c["l"]),
                    "close": float(c["c"]),
                    "volume": float(c["v"]),
                    "trades": int(c["n"])
                })

        df = pl.DataFrame(deduped).sort("timestamp")
        df.write_parquet(file_path)
        print(f"Saved {len(df)} candles to {file_path}", flush=True)
        return str(file_path)

    def download_historical_funding(
        self,
        coin: str,
        days: int = 90,
        output_dir: str = "Data/Hyperdash_Historical"
    ) -> str:
        """Download complete funding rate history for the asset."""
        out_path = pathlib.Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)
        file_path = out_path / f"{coin}_funding_historical.parquet"

        now = int(time.time() * 1000)
        start_time = now - (days * 24 * 3600 * 1000)

        payload = {
            "type": "fundingHistory",
            "coin": coin,
            "startTime": start_time
        }
        records = self._post_json(HL_INFO_URL, payload)
        if not records:
            raise RuntimeError(f"No funding records found for {coin}")

        formatted = []
        for r in records:
            formatted.append({
                "timestamp": r["time"],
                "datetime": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(r["time"] / 1000)),
                "coin": r["coin"],
                "funding_rate": float(r["fundingRate"]),
                "premium": float(r.get("premium", 0.0))
            })

        df = pl.DataFrame(formatted).sort("timestamp")
        df.write_parquet(file_path)
        print(f"Saved {len(df)} funding history records to {file_path}", flush=True)
        return str(file_path)
