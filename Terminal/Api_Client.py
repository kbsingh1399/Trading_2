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
from Terminal.Microstructure import TokenBucket
from Terminal.Asset_Universe import canonical_asset, UNIVERSE

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
        self.wallet_risk_cache = {}
        self._graphql_cache: Dict[str, Tuple[float, Any]] = {}
        # Dedicated limiters: fast REST for live orderbook/trades, protected GraphQL for analytics
        self._hl_limiter = TokenBucket(rate=15.0, capacity=30.0)
        self._graphql_limiter = TokenBucket(rate=3.0, capacity=6.0)

    def _post_json(self, url: str, payload: dict) -> dict:
        if HD_GRAPHQL_URL in url:
            self._graphql_limiter.acquire()
        else:
            self._hl_limiter.acquire()
        data_bytes = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data_bytes, headers=DEFAULT_HEADERS)
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    result = json.loads(resp.read().decode("utf-8"))
                    if isinstance(result, dict) and result.get("errors"):
                        err_str = str(result["errors"])
                        if ("RATE_LIMIT_EXCEEDED" in err_str or "Too many" in err_str or "429" in err_str) and attempt < 2:
                            time.sleep(2.0 * (attempt + 1))
                            continue
                        raise ValueError(f"GraphQL rejected request: {result['errors']}")
                    return result
            except urllib.error.HTTPError as e:
                if (e.code == 429 or e.code == 503) and attempt < 2:
                    time.sleep(2.0 * (attempt + 1))
                    continue
                err_msg = e.read().decode("utf-8", errors="ignore")
                raise RuntimeError(f"HTTP {e.code} Error from {url}: {err_msg}")
            except Exception as e:
                if attempt < 2 and ("timeout" in str(e).lower() or "reset" in str(e).lower() or "rate" in str(e).lower()):
                    time.sleep(1.0)
                    continue
                raise RuntimeError(f"Connection Error to {url}: {e}")

    def fetch_all_assets(self) -> List[Dict[str, Any]]:
        """Fetch all active perpetual assets on Hyperliquid with live stats."""
        # 1. Fetch main global DEX assets
        payload = {"type": "metaAndAssetCtxs"}
        data = self._post_json(HL_INFO_URL, payload)
        meta_universe = data[0]["universe"]
        asset_ctxs = data[1]
        origins = [""]*len(meta_universe)

        # 2. Fetch HIP-3 builder markets (xyz DEX) for legacy assets
        xyz_payload = {"type": "metaAndAssetCtxs", "dex": "xyz"}
        try:
            xyz_data = self._post_json(HL_INFO_URL, xyz_payload)
            if xyz_data and len(xyz_data) == 2:
                meta_universe.extend(xyz_data[0]["universe"])
                asset_ctxs.extend(xyz_data[1])
                origins.extend(["xyz"]*len(xyz_data[0]["universe"]))
        except Exception as e:
            pass # fallback to global only if xyz fails

        # 3. Fetch HIP-3 builder markets (flx DEX) for NAS100/DJ30
        flx_payload = {"type": "metaAndAssetCtxs", "dex": "flx"}
        try:
            flx_data = self._post_json(HL_INFO_URL, flx_payload)
            if flx_data and len(flx_data) == 2:
                meta_universe.extend(flx_data[0]["universe"])
                asset_ctxs.extend(flx_data[1])
                origins.extend(["flx"]*len(flx_data[0]["universe"]))
        except Exception as e:
            pass

        results = []
        self.universe = []
        new_cache = {}
        for meta, ctx, dex in zip(meta_universe, asset_ctxs, origins):
            # Clean prefix for terminal consistency if present
            raw_coin = meta["name"]
            if dex and ":" not in raw_coin: raw_coin = dex+":"+raw_coin
            coin = raw_coin.split(":")[-1] if ":" in raw_coin else raw_coin
            coin = canonical_asset(coin)
            if meta.get("isDelisted"): continue

            if coin in self.universe:
                continue

            self.universe.append(coin)
            mark_px = float(ctx["markPx"]) if ctx.get("markPx") is not None else None
            if mark_px is None or mark_px <= 0:
                continue  # cannot quote/size a market without a real mark
            oi = float(ctx["openInterest"]) if ctx.get("openInterest") is not None else None
            funding = float(ctx["funding"]) if ctx.get("funding") is not None else None
            volume_24h = float(ctx["dayNtlVlm"]) if ctx.get("dayNtlVlm") is not None else None
            prev_day_px = float(ctx["prevDayPx"]) if ctx.get("prevDayPx") is not None else None
            change_24h = ((mark_px - prev_day_px) / prev_day_px * 100.0) if prev_day_px and prev_day_px > 0 else None

            item = {
                "coin": coin,
                "signal_market": raw_coin,
                "metadata_observed_at": time.time(),
                "mark_px": mark_px,
                "open_interest": oi,
                "open_interest_usd": oi * mark_px if oi is not None else None,
                "funding_rate": funding,
                "funding_annualized": funding * 24 * 365 * 100 if funding is not None else None, # Hyperliquid hourly rate
                "volume_24h": volume_24h,
                "change_24h": change_24h,
                "max_leverage": meta.get("maxLeverage"),
                "sz_decimals": meta.get("szDecimals")
            }
            results.append(item)
            new_cache[coin] = item

        # Sort by 24h volume descending
        results.sort(key=lambda x: x["volume_24h"] or 0, reverse=True)
        self.asset_cache = new_cache
        return results

    def _resolve_coin(self, coin: str) -> str:
        if ":" in coin: return coin
        asset = canonical_asset(coin)
        if asset in self.asset_cache and "signal_market" in self.asset_cache[asset]:
            return self.asset_cache[asset]["signal_market"]
        HIP3_MAP = {
            "SP500": "xyz:SP500",
            "NAS100": "xyz:XYZ100",
            "GOLD": "xyz:GOLD",
            "SILVER": "xyz:SILVER",
            "USWTI": "xyz:CL",
            "EURUSD": "xyz:EUR",
            "GBPUSD": "xyz:GBP",
            "USDJPY": "xyz:JPY",
        }
        if asset in HIP3_MAP:
            return HIP3_MAP[asset]
        return asset

    def fetch_l2_book(self, coin: str) -> Dict[str, Any]:
        """Fetch real-time Level 2 orderbook (20 bids, 20 asks) with depth metrics."""
        hl_coin = self._resolve_coin(coin)
        payload = {"type": "l2Book", "coin": hl_coin}
        raw = self._post_json(HL_INFO_URL, payload)
        levels = raw.get("levels") if isinstance(raw, dict) else None
        if not isinstance(levels, list) or len(levels) < 2 or not levels[0] or not levels[1]:
            raise RuntimeError("Hyperliquid L2 book unavailable")
        raw_bids = levels[0][:20] if len(levels) > 0 else []
        raw_asks = levels[1][:20] if len(levels) > 1 else []

        bids = [{"price": float(b["px"]), "size": float(b["sz"]), "total_usd": float(b["px"]) * float(b["sz"])} for b in raw_bids]
        asks = [{"price": float(a["px"]), "size": float(a["sz"]), "total_usd": float(a["px"]) * float(a["sz"])} for a in raw_asks]

        best_bid, best_ask = bids[0]["price"], asks[0]["price"]
        if not 0 < best_bid < best_ask or any(r["price"] <= 0 or r["size"] <= 0 for r in bids + asks):
            raise RuntimeError("Hyperliquid L2 book crossed or invalid")
        spread = best_ask - best_bid
        spread_bps = spread / best_bid * 10000.0

        bid_vol = sum(b["total_usd"] for b in bids)
        ask_vol = sum(a["total_usd"] for a in asks)
        total_vol = bid_vol + ask_vol
        bid_ratio = bid_vol / total_vol * 100.0  # validated positive sizes

        return {
            "coin": coin,
            "signal_market": hl_coin,
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
            "timestamp": raw.get("time", 0),
            "received_at": time.time()
        }

    def fetch_l3_orders(self, coin: str, min_price: float, max_price: float) -> List[Dict[str, Any]]:
        """
        Fetch individual Level 3 resting orders mapped to specific Ethereum wallet addresses.
        Powers the Hyperdash Level 3 orderbook overlay.
        """
        hl_coin = self._resolve_coin(coin)
        cache_key = f"l3_{hl_coin}"
        now_epoch = time.time()
        if cache_key in self._graphql_cache and (now_epoch - self._graphql_cache[cache_key][0]) < 90.0:
            return self._graphql_cache[cache_key][1]

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
        variables = {"market": hl_coin, "minPrice": float(min_price), "maxPrice": float(max_price)}
        try:
            data = self._post_json(HD_GRAPHQL_URL, {"query": query, "variables": variables})
            node = data.get("data") or {}
            if "orderbookSnapshotFiltered" not in node or not isinstance(node["orderbookSnapshotFiltered"], list):
                raise RuntimeError("Hyperdash orderbookSnapshotFiltered response unavailable")
            orders_raw = node["orderbookSnapshotFiltered"]

            orders = []
            observed_at = time.time()
            for o in orders_raw:
                sub = o.get("order", {})
                px = float(sub.get("limitPx", 0.0))
                sz = float(sub.get("sz", 0.0))
                if px <= 0 or sz <= 0 or not str(o.get("address", "")).startswith("0x") or sub.get("side") not in ("B", "A"):
                    continue
                orders.append({
                    "address": o.get("address", ""),
                    "side": "BUY" if sub.get("side") == "B" else "SELL" if sub.get("side") == "A" else "UNKNOWN",
                    "price": px,
                    "size": sz,
                    "notional_usd": px * sz,
                    "observed_at": observed_at,
                    "timestamp_basis": "RECEIPT_ONLY",
                    "coverage": "WALLET_ATTRIBUTED_SNAPSHOT_NO_ORDER_ID_NOT_FULL_L3",
                    "source": "HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT",
                })

            # Sort by notional value descending (whales first)
            orders.sort(key=lambda x: x["notional_usd"], reverse=True)
            self._graphql_cache[cache_key] = (now_epoch, orders)
            return orders
        except Exception:
            if cache_key in self._graphql_cache:
                return self._graphql_cache[cache_key][1]
            raise

    def fetch_liquidations(self, coin: str, min_price: float, max_price: float, lookback_days: int = 3) -> Dict[str, Any]:
        """Fetch real-time liquidation clusters, totals, and top liquidation whale addresses."""
        hl_coin = self._resolve_coin(coin)
        cache_key = f"liq_{hl_coin}"
        now_epoch = time.time()
        if cache_key in self._graphql_cache and (now_epoch - self._graphql_cache[cache_key][0]) < 90.0:
            return self._graphql_cache[cache_key][1]

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
            "coin": hl_coin,
            "minPrice": float(min_price),
            "maxPrice": float(max_price),
            "startTime": float(start_time),
            "endTime": float(now)
        }
        try:
            data = self._post_json(HD_GRAPHQL_URL, {"query": query, "variables": variables})
            res = (data.get("data") or {}).get("analytics") or {}
            if "liquidationLevels" not in res or not isinstance(res["liquidationLevels"], dict):
                raise RuntimeError("Hyperdash liquidationLevels response unavailable")
            res = res["liquidationLevels"]

            bands = []
            time_series_by_candle: Dict[str, List[Dict[str, Any]]] = {}
            candle_totals: Dict[str, float] = {}

            raw_bands = res.get("bands", [])
            for b in raw_bands:
                hist = b.get("historicalData", [])
                if not hist or hist[-1].get("totalAmount") is None:
                    continue  # missing history is not an observed zero
                latest_amt = float(hist[-1]["totalAmount"])
                min_px = float(b.get("minPrice") or 0)
                max_px = float(b.get("maxPrice") or 0)
                if min_px <= 0 or max_px < min_px:
                    continue
                mid_px = (min_px + max_px) / 2.0

                bands.append({
                    "min_px": min_px,
                    "max_px": max_px,
                    "mid_px": mid_px,
                    "amount": latest_amt,
                    "observed_at": hist[-1].get("timestamp", 0) if hist else 0
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

            out_res = {
                "coin": coin,
                "current_price": res.get("currentPrice"),
                "kind": "UNVERIFIED_BAND_LANDSCAPE",
                "received_at": time.time(),
                "band_size": res.get("bandSize"),
                "source": "HYPERDASH_GRAPHQL_ANALYTICS_UNVERIFIED_METHODOLOGY",
                "size_unit": "BASE_ASSET_REPORTED_UNVERIFIED",
                "total_long_size": (res.get("totalLongLiquidations") or {}).get("size"),
                "total_long_count": (res.get("totalLongLiquidations") or {}).get("count"),
                "total_short_size": (res.get("totalShortLiquidations") or {}).get("size"),
                "total_short_count": (res.get("totalShortLiquidations") or {}).get("count"),
                "top_long_whales": res.get("topLongLiquidations", []),
                "top_short_whales": res.get("topShortLiquidations", []),
                "bands": bands,
                "timestamps": sorted_timestamps,
                "candle_snapshots": time_series_by_candle,
                "candle_totals": candle_totals,
                "current_candle": {
                    "timestamp": latest_ts,
                    "total_amount": candle_totals.get(latest_ts) if latest_ts else None,
                    "distribution": current_candle_distribution
                }
            }
            self._graphql_cache[cache_key] = (now_epoch, out_res)
            return out_res
        except Exception:
            if cache_key in self._graphql_cache:
                return self._graphql_cache[cache_key][1]
            raise

    def fetch_stops(self, coin: str, min_price: float, max_price: float, lookback_days: int = 3) -> Dict[str, Any]:
        """Fetch live buy/sell stop orders, stop clusters, and top stop-loss whale addresses."""
        hl_coin = self._resolve_coin(coin)
        cache_key = f"stop_{hl_coin}"
        now_epoch = time.time()
        if cache_key in self._graphql_cache and (now_epoch - self._graphql_cache[cache_key][0]) < 90.0:
            return self._graphql_cache[cache_key][1]

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
            "coin": hl_coin,
            "minPrice": float(min_price),
            "maxPrice": float(max_price),
            "startTime": float(start_time),
            "endTime": float(now)
        }
        try:
            data = self._post_json(HD_GRAPHQL_URL, {"query": query, "variables": variables})
            res = (data.get("data") or {}).get("analytics") or {}
            if "stopOrderLevels" not in res or not isinstance(res["stopOrderLevels"], dict):
                raise RuntimeError("Hyperdash stopOrderLevels response unavailable")
            res = res["stopOrderLevels"]

            bands = []
            time_series_by_candle: Dict[str, List[Dict[str, Any]]] = {}
            candle_totals: Dict[str, float] = {}

            raw_bands = res.get("bands", [])
            for b in raw_bands:
                hist = b.get("historicalData", [])
                if not hist or hist[-1].get("totalAmount") is None:
                    continue  # missing history is not an observed zero
                latest_amt = float(hist[-1]["totalAmount"])
                min_px = float(b.get("minPrice") or 0)
                max_px = float(b.get("maxPrice") or 0)
                if min_px <= 0 or max_px < min_px:
                    continue
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

            out_res = {
                "coin": coin,
                "current_price": res.get("currentPrice"),
                "band_size": res.get("bandSize"),
                "source": "HYPERDASH_GRAPHQL_ANALYTICS_UNVERIFIED_METHODOLOGY",
                "size_unit": "BASE_ASSET_REPORTED_UNVERIFIED",
                "total_buy_size": (res.get("totalBuyStops") or {}).get("size"),
                "kind": "UNVERIFIED_STOP_LANDSCAPE",
                "received_at": time.time(),
                "total_buy_count": (res.get("totalBuyStops") or {}).get("count"),
                "total_sell_size": (res.get("totalSellStops") or {}).get("size"),
                "total_sell_count": (res.get("totalSellStops") or {}).get("count"),
                "top_buy_whales": res.get("topBuyStops", []),
                "top_sell_whales": res.get("topSellStops", []),
                "bands": bands,
                "timestamps": sorted_timestamps,
                "candle_snapshots": time_series_by_candle,
                "candle_totals": candle_totals,
                "current_candle": {
                    "timestamp": latest_ts,
                    "total_amount": candle_totals.get(latest_ts) if latest_ts else None,
                    "distribution": current_candle_distribution
                }
            }
            self._graphql_cache[cache_key] = (now_epoch, out_res)
            return out_res
        except Exception:
            if cache_key in self._graphql_cache:
                return self._graphql_cache[cache_key][1]
            raise

    def fetch_top_traders(self, coin: str, limit: int = 20) -> List[Dict[str, Any]]:
        """Fetch top PnL positions and smart money wallets for the asset."""
        hl_coin = self._resolve_coin(coin)
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
                notionalSize
                entryPrice
                unrealizedPnl
              }
            }
          }
        }
        """
        variables = {"coin": hl_coin, "pnlLimit": limit}
        data = self._post_json(HD_GRAPHQL_URL, {"query": query, "variables": variables})
        positions = data.get("data", {}).get("analytics", {}).get("winners", {}).get("positions", [])
        return positions

    def fetch_recent_trades(self, coin: str) -> List[Dict[str, Any]]:
        """Fetch latest tick trades with aggressor side."""
        hl_coin = self._resolve_coin(coin)
        payload = {"type": "recentTrades", "coin": hl_coin}
        try:
            trades = self._post_json(HL_INFO_URL, payload)
            return trades if trades else []
        except Exception:
            return []

    def fetch_wallet_risk(self, coin, addresses, book):
        """Observed positions and trigger orders for a sampled whale cohort.

        These are lower-bound exposures of observed wallets, not estimates of
        every trader's hidden leverage. Historical band landscapes stay separate.
        """
        qualified = self._resolve_coin(coin)
        dex = qualified.split(":")[0] if ":" in qualified else ""
        now = time.time(); cache = self.wallet_risk_cache.get(qualified)
        if cache and now-cache["observed_at"] < 30: return cache
        positions, liquidations, stops = [], [], []
        sampled = list(dict.fromkeys(a for a in addresses if a))[:2]
        for address in sampled:
            context = {"user": address, **({"dex": dex} if dex else {})}
            state = self._post_json(HL_INFO_URL, {"type": "clearinghouseState", **context})
            orders = self._post_json(HL_INFO_URL, {"type": "frontendOpenOrders", **context})
            for item in state.get("assetPositions", []):
                p = item.get("position", {})
                if canonical_asset(p.get("coin")) != canonical_asset(coin): continue
                size = float(p.get("szi", 0)); liq = float(p.get("liquidationPx") or 0)
                positions.append({"address": address, "size": size, "entry_price": float(p.get("entryPx", 0)),
                                  "notional_usd": float(p.get("positionValue", 0)), "unrealized_pnl_usd": float(p.get("unrealizedPnl", 0)),
                                  "liquidation_price": liq or None})
                if liq > 0 and size:
                    long = size > 0
                    endpoint = float(book.get("best_bid" if long else "best_ask", 0))
                    if endpoint > 0 and (liq < endpoint if long else liq > endpoint):
                        liquidations.append({"min_px": liq, "max_px": liq,
                                             "mid_px": liq, "book_reference_px": endpoint, "amount_usd": abs(size)*liq,
                                             "position_side_at_risk": "LONG" if long else "SHORT", "address": address,
                                             "kind": "PROJECTED_EXPOSURE"})
            for order in orders:
                if not order.get("isTrigger") or not order.get("reduceOnly") or canonical_asset(order.get("coin")) != canonical_asset(coin): continue
                # A take-profit trigger is not a stop loss. Explicit order type is required.
                if "stop" not in str(order.get("orderType", "")).lower(): continue
                trigger, size = float(order.get("triggerPx") or 0), float(order.get("sz") or 0)
                side = "LONG" if order.get("side") == "A" else "SHORT" if order.get("side") == "B" else None
                if trigger <= 0 or size <= 0 or side is None: continue
                endpoint = float(book.get("best_bid" if side=="LONG" else "best_ask", 0))
                if endpoint <= 0 or not (trigger < endpoint if side=="LONG" else trigger > endpoint): continue
                stops.append({"min_px": trigger, "max_px": trigger, "mid_px": trigger,
                              "book_reference_px": endpoint, "amount_usd": trigger*size, "position_side_at_risk": side, "address": address,
                              "order_id": order.get("oid"), "kind": "OBSERVED_STOP_ORDERS"})
        result = {"observed_at": time.time(), "positions": positions,
                  "liquidations": {"kind": "PROJECTED_EXPOSURE", "bands": liquidations, "coverage": "SAMPLED_WALLETS", "wallets": sampled},
                  "stops": {"kind": "OBSERVED_STOP_ORDERS", "bands": stops, "coverage": "SAMPLED_WALLETS", "wallets": sampled}}
        self.wallet_risk_cache[qualified] = result
        return result

    def fetch_candles(self, coin: str, interval: str = "1h", lookback_days: int = 3) -> List[Dict[str, Any]]:
        """Fetch live OHLCV candles from Hyperliquid for charting & alignment."""
        hl_coin = self._resolve_coin(coin)
        now_ms = int(time.time() * 1000)
        start_ms = now_ms - (lookback_days * 24 * 3600 * 1000)
        payload = {
            "type": "candleSnapshot",
            "req": {
                "coin": hl_coin,
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
