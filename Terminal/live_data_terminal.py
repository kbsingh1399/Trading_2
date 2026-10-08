#!/usr/bin/env python3
"""Multi-Source Live Market Data & API Inspector Terminal.

Institutional-grade cross-venue comparison CLI tool.
Fetches, audits, and displays live data side-by-side across 8 independent sources:
  1. MetaTrader 5 (Blueberry Markets live account & quotes)
  2. Binance USD-M Futures (Price, Depth L2, Open Interest, Funding, Taker CVD)
  3. Binance Spot (Spot Price, Volume)
  4. Coinbase Pro (Spot Price, Coinbase Premium Index)
  5. Hyperliquid Perpetuals (Mark Price, Mid Price, Open Interest, Funding)
  6. Bybit Linear Perpetuals (Price, Open Interest, Funding)
  7. OKX Swaps (Price, 24h Volume)
  8. Kraken Spot (Spot Price)
Plus Macro Feeds:
  * Alternative.me Fear & Greed Index
  * Farside Investors Spot ETF Net Daily Flows (BTC & ETH)
  * Macro Event Calendar & Blackout Runway

Usage:
  python Terminal/live_data_terminal.py              # Single snapshot overview
  python Terminal/live_data_terminal.py --watch      # Continuous live updating screen (every 3s)
  python Terminal/live_data_terminal.py --asset BTC  # Detailed single-asset cross-check
  python Terminal/live_data_terminal.py --json       # Dump raw JSON payloads for all APIs
"""

from __future__ import annotations

import argparse
import json
import math
import pathlib
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from rich import box
from rich.console import Console, Group
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# Root resolution
ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Supported Cross-Venue Crypto Assets
DEFAULT_CRYPTO_ASSETS = ["BTC", "ETH", "SOL", "BNB", "XRP", "DOGE", "ADA", "LINK", "AVAX", "NEAR", "LTC", "BCH"]
MACRO_ASSETS = ["SP500", "USWTI", "GOLD", "EURUSD", "USDJPY"]

MT5_SYMBOL_MAP = {
    "BTC": "BTCUSD.pi",
    "ETH": "ETHUSD.pi",
    "SOL": "SOLUSD.p",
    "BNB": "BNBUSD.p",
    "XRP": "XRPUSD.pi",
    "DOGE": "DOGUSD.p",
    "ADA": "ADAUSD.p",
    "LINK": "LNKUSD.p",
    "AVAX": "AVXUSD.p",
    "NEAR": "NERUSD.p",
    "LTC": "LTCUSD.pi",
    "BCH": "BCHUSD.p",
    "DOT": "DOTUSD.pi",
    "TRX": "TRXUSD.p",
    "SP500": "SP500.p",
    "NAS100": "NAS100.p",
    "DJ30": "DJ30.p",
    "GER40": "GER40.p",
    "GOLD": "XAUUSD.pi",
    "SILVER": "XAGUSD.pi",
    "USWTI": "USWTI.p",
    "EURUSD": "EURUSD.pi",
    "GBPUSD": "GBPUSD.pi",
    "USDJPY": "USDJPY.pi",
}

KRAKEN_PAIR_MAP = {
    "BTC": "XBTUSD",
    "ETH": "ETHUSD",
    "SOL": "SOLUSD",
    "XRP": "XRPUSD",
    "DOGE": "DOGEUSD",
    "ADA": "ADAUSD",
    "LINK": "LINKUSD",
    "LTC": "LTCUSD",
    "BCH": "BCHUSD",
}


def _http_get(url: str, headers: Optional[Dict[str, str]] = None, timeout: float = 3.0) -> Any:
    """Safe HTTP GET with tight timeout."""
    hdrs = {"User-Agent": USER_AGENT}
    if headers:
        hdrs.update(headers)
    req = urllib.request.Request(url, headers=hdrs)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as exc:
        return {"error": str(exc)}


def _http_post_json(url: str, payload: Dict[str, Any], timeout: float = 3.0) -> Any:
    """Safe HTTP POST JSON with tight timeout."""
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json", "User-Agent": USER_AGENT},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as exc:
        return {"error": str(exc)}


# ==============================================================================
# INDIVIDUAL API FETCHERS (THREAD-SAFE)
# ==============================================================================

def fetch_binance_futures_data(asset: str) -> Dict[str, Any]:
    """Fetch price, depth L2, open interest, funding, and 1m CVD from Binance Futures."""
    sym = f"{asset}USDT"
    res = {
        "source": "Binance Futures (USDT-M)",
        "asset": asset,
        "symbol": sym,
        "futures_price": None,
        "mark_price": None,
        "index_price": None,
        "last_funding_rate_bps": None,
        "open_interest_coins": None,
        "open_interest_usd": None,
        "top20_bid_usd": None,
        "top20_ask_usd": None,
        "book_imbalance": None,
        "best_bid": None,
        "best_ask": None,
        "cvd_1m_delta_usd": None,
        "cvd_5m_delta_usd": None,
        "cvd_15m_delta_usd": None,
        "cvd_1m_buy_usd": None,
        "cvd_1m_sell_usd": None,
        "cvd_1m_trades": None,
        "largest_whale_wall": None,
        "raw": {},
        "error": None,
    }

    try:
        # 1. Premium & Funding
        p_data = _http_get(f"https://fapi.binance.com/fapi/v1/premiumIndex?symbol={sym}")
        if "error" not in p_data:
            res["raw"]["premiumIndex"] = p_data
            res["mark_price"] = float(p_data.get("markPrice", 0))
            res["index_price"] = float(p_data.get("indexPrice", 0))
            if p_data.get("lastFundingRate") is not None:
                res["last_funding_rate_bps"] = round(float(p_data["lastFundingRate"]) * 1e4, 4)

        # 2. Ticker price
        t_data = _http_get(f"https://fapi.binance.com/fapi/v1/ticker/price?symbol={sym}")
        if "error" not in t_data:
            res["raw"]["ticker"] = t_data
            res["futures_price"] = float(t_data.get("price", 0))

        # 3. Open Interest
        oi_data = _http_get(f"https://fapi.binance.com/fapi/v1/openInterest?symbol={sym}")
        if "error" not in oi_data:
            res["raw"]["openInterest"] = oi_data
            oi_coins = float(oi_data.get("openInterest", 0))
            res["open_interest_coins"] = oi_coins
            if res["futures_price"]:
                res["open_interest_usd"] = oi_coins * res["futures_price"]

        # 4. Top-20 L2 Orderbook Depth
        d_data = _http_get(f"https://fapi.binance.com/fapi/v1/depth?symbol={sym}&limit=20")
        if "error" not in d_data:
            res["raw"]["depth"] = d_data
            bids = d_data.get("bids", [])
            asks = d_data.get("asks", [])
            if bids:
                res["best_bid"] = float(bids[0][0])
            if asks:
                res["best_ask"] = float(asks[0][0])

            b_usd = sum(float(p) * float(q) for p, q in bids)
            a_usd = sum(float(p) * float(q) for p, q in asks)
            res["top20_bid_usd"] = b_usd
            res["top20_ask_usd"] = a_usd
            if b_usd + a_usd > 0:
                res["book_imbalance"] = round((b_usd - a_usd) / (b_usd + a_usd), 4)

            # Detect largest wall
            max_wall = 0.0
            wall_info = None
            for p, q in bids:
                notional = float(p) * float(q)
                if notional >= 150_000 and notional > max_wall:
                    max_wall = notional
                    wall_info = f"BID {float(p):,.2f} ({notional:,.0f} USD)"
            for p, q in asks:
                notional = float(p) * float(q)
                if notional >= 150_000 and notional > max_wall:
                    max_wall = notional
                    wall_info = f"ASK {float(p):,.2f} ({notional:,.0f} USD)"
            res["largest_whale_wall"] = wall_info

        # 5. Klines / CVD 1m
        k_data = _http_get(f"https://fapi.binance.com/fapi/v1/klines?symbol={sym}&interval=1m&limit=16")
        if isinstance(k_data, list) and k_data:
            res["raw"]["klines_1m_count"] = len(k_data)
            # Filter out uncompleted candle
            completed = [k for k in k_data if int(k[6]) <= time.time() * 1000]
            if not completed:
                completed = k_data[:-1]

            if completed:
                last_k = completed[-1]
                t_vol = float(last_k[7])
                t_buy = float(last_k[10])
                t_sell = t_vol - t_buy
                res["cvd_1m_buy_usd"] = t_buy
                res["cvd_1m_sell_usd"] = t_sell
                res["cvd_1m_delta_usd"] = t_buy - t_sell
                res["cvd_1m_trades"] = int(last_k[8])

                # Rolling 5m
                last5 = completed[-5:] if len(completed) >= 5 else completed
                d5 = sum((float(k[10]) - (float(k[7]) - float(k[10]))) for k in last5)
                res["cvd_5m_delta_usd"] = d5

                # Rolling 15m
                last15 = completed[-15:] if len(completed) >= 15 else completed
                d15 = sum((float(k[10]) - (float(k[7]) - float(k[10]))) for k in last15)
                res["cvd_15m_delta_usd"] = d15

    except Exception as exc:
        res["error"] = str(exc)

    return res


def fetch_binance_spot_price(asset: str) -> Dict[str, Any]:
    """Fetch Spot price from Binance Spot."""
    sym = f"{asset}USDT"
    res = {"source": "Binance Spot", "asset": asset, "spot_price": None, "raw": {}, "error": None}
    data = _http_get(f"https://api.binance.com/api/v3/ticker/price?symbol={sym}")
    if "error" in data:
        res["error"] = data["error"]
    else:
        res["spot_price"] = float(data.get("price", 0))
        res["raw"] = data
    return res


def fetch_coinbase_spot_price(asset: str) -> Dict[str, Any]:
    """Fetch Spot price from Coinbase Pro."""
    res = {"source": "Coinbase Pro", "asset": asset, "spot_price": None, "raw": {}, "error": None}
    pair = f"{asset}-USD"
    data = _http_get(f"https://api.coinbase.com/v2/prices/{pair}/spot")
    if "error" in data:
        res["error"] = data["error"]
    elif "data" in data and "amount" in data["data"]:
        res["spot_price"] = float(data["data"]["amount"])
        res["raw"] = data
    else:
        res["error"] = "Invalid payload"
    return res


def fetch_hyperliquid_data() -> Dict[str, Any]:
    """Fetch full universe mark price, mid price, OI and funding from Hyperliquid."""
    payload = {"type": "metaAndAssetCtxs"}
    data = _http_post_json("https://api.hyperliquid.xyz/info", payload)
    res = {"source": "Hyperliquid", "coins": {}, "raw_count": 0, "error": None}
    if isinstance(data, list) and len(data) >= 2:
        universe = data[0].get("universe", [])
        contexts = data[1]
        res["raw_count"] = len(universe)
        for i, meta in enumerate(universe):
            coin_name = meta.get("name")
            if i < len(contexts):
                ctx = contexts[i]
                res["coins"][coin_name] = {
                    "mark_price": float(ctx.get("markPx", 0)),
                    "mid_price": float(ctx.get("midPx", 0)) if ctx.get("midPx") else None,
                    "open_interest": float(ctx.get("openInterest", 0)),
                    "funding_rate": float(ctx.get("funding", 0)),
                    "day_ntnl_vol": float(ctx.get("dayNtnlVlm", 0)),
                }
    else:
        res["error"] = str(data.get("error", "Malformed response")) if isinstance(data, dict) else "Unknown error"
    return res


def fetch_bybit_ticker(asset: str) -> Dict[str, Any]:
    """Fetch Bybit Linear Perpetual ticker."""
    sym = f"{asset}USDT"
    res = {"source": "Bybit Linear", "asset": asset, "last_price": None, "mark_price": None, "open_interest": None, "funding_rate": None, "error": None}
    data = _http_get(f"https://api.bybit.com/v5/market/tickers?category=linear&symbol={sym}")
    if "error" in data:
        res["error"] = data["error"]
    else:
        items = data.get("result", {}).get("list", [])
        if items:
            item = items[0]
            res["last_price"] = float(item.get("lastPrice", 0))
            res["mark_price"] = float(item.get("markPrice", 0))
            res["open_interest"] = float(item.get("openInterest", 0))
            if item.get("fundingRate"):
                res["funding_rate"] = float(item["fundingRate"])
        else:
            res["error"] = "Symbol not found"
    return res


def fetch_okx_ticker(asset: str) -> Dict[str, Any]:
    """Fetch OKX Swap Perpetual ticker."""
    inst_id = f"{asset}-USDT-SWAP"
    res = {"source": "OKX Swap", "asset": asset, "last_price": None, "vol_24h": None, "error": None}
    data = _http_get(f"https://www.okx.com/api/v5/market/ticker?instId={inst_id}")
    if "error" in data:
        res["error"] = data["error"]
    else:
        items = data.get("data", [])
        if items:
            res["last_price"] = float(items[0].get("last", 0))
            res["vol_24h"] = float(items[0].get("volCcy24h", 0))
        else:
            res["error"] = "Instrument not found"
    return res


def fetch_kraken_ticker(asset: str) -> Dict[str, Any]:
    """Fetch Kraken Spot ticker."""
    res = {"source": "Kraken Spot", "asset": asset, "last_price": None, "error": None}
    pair = KRAKEN_PAIR_MAP.get(asset)
    if not pair:
        res["error"] = "Pair not mapped"
        return res
    data = _http_get(f"https://api.kraken.com/0/public/Ticker?pair={pair}")
    if isinstance(data, dict) and data.get("error") and len(data["error"]) > 0:
        res["error"] = data["error"]
    elif isinstance(data, dict) and "result" in data:
        result = data.get("result", {})
        if result:
            first_key = list(result.keys())[0]
            val = result[first_key]
            c = val.get("c", [])
            if c:
                res["last_price"] = float(c[0])
        else:
            res["error"] = "Result empty"
    return res


def fetch_mt5_account_and_quotes(assets: List[str]) -> Dict[str, Any]:
    """Fetch live account state, equity, margin and symbol quotes from MetaTrader 5."""
    res = {
        "source": "MetaTrader 5 (Blueberry Markets)",
        "connected": False,
        "account": {},
        "quotes": {},
        "positions": [],
        "orders": [],
        "error": None,
    }
    try:
        from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge
        bridge = MT5ExecutionBridge(5064568)
        acc = bridge.get_account_summary()
        res["connected"] = acc.get("connected", False)
        if res["connected"]:
            res["account"] = {
                "balance": acc.get("balance_usd", 0.0),
                "equity": acc.get("equity_usd", 0.0),
                "margin_used": acc.get("margin_used_usd", 0.0),
                "margin_free": acc.get("margin_free_usd", 0.0),
                "margin_level": acc.get("margin_level_pct", 0.0),
                "leverage": acc.get("leverage", 0),
                "server": acc.get("server", ""),
            }
            res["positions"] = bridge.get_open_positions()
            res["orders"] = bridge.get_pending_orders()

            for a in assets:
                sym = MT5_SYMBOL_MAP.get(a)
                if sym:
                    q = bridge.get_symbol_price(sym)
                    if q and q.get("bid") is not None and q.get("ask") is not None:
                        bid = float(q["bid"])
                        ask = float(q["ask"])
                        spread_pts = ask - bid
                        mid = (bid + ask) / 2.0 if bid + ask > 0 else 0.0
                        spread_bps = (spread_pts / mid * 1e4) if mid > 0 else 0.0
                        res["quotes"][a] = {
                            "symbol": sym,
                            "bid": bid,
                            "ask": ask,
                            "mid": mid,
                            "spread_pts": spread_pts,
                            "spread_bps": round(spread_bps, 2),
                            "time": q.get("time_msc", 0),
                        }
    except Exception as exc:
        res["error"] = str(exc)

    return res


def fetch_macro_sentiment_data() -> Dict[str, Any]:
    """Fetch Fear & Greed index, ETF flows, and Macro event runway."""
    res = {
        "fear_and_greed": None,
        "btc_etf_flows": None,
        "eth_etf_flows": None,
        "macro_calendar": None,
    }

    # 1. Alternative.me Fear & Greed
    try:
        fng_data = _http_get("https://api.alternative.me/fng/?limit=1")
        if "data" in fng_data and fng_data["data"]:
            item = fng_data["data"][0]
            res["fear_and_greed"] = {
                "value": int(item.get("value", 0)),
                "classification": item.get("value_classification", "Unknown"),
                "timestamp": int(item.get("timestamp", 0)),
            }
    except Exception:
        pass

    # 2. Farside ETF flows via local engine or scrape
    try:
        from Terminal.Data_Factory.macro import FarsideETFFlows
        etf = FarsideETFFlows()
        rows_btc = etf.refresh("BTC")
        if rows_btc:
            res["btc_etf_flows"] = {
                "date": rows_btc[-1].get("date"),
                "total_musd": rows_btc[-1].get("total_musd"),
            }
        rows_eth = etf.refresh("ETH")
        if rows_eth:
            res["eth_etf_flows"] = {
                "date": rows_eth[-1].get("date"),
                "total_musd": rows_eth[-1].get("total_musd"),
            }
    except Exception:
        pass

    # 3. Macro Calendar
    cal_path = ROOT / "Data" / "macro_calendar.json"
    if cal_path.exists():
        try:
            cal = json.loads(cal_path.read_text(encoding="utf-8"))
            res["macro_calendar"] = {
                "next_event": cal.get("event"),
                "fomc_release": cal.get("fomc_release_utc"),
                "runway_hours": cal.get("runway_hours_to_blackout"),
            }
        except Exception:
            pass

def fetch_hyperdash_orderbook_and_analytics(coin: str) -> Dict[str, Any]:
    """Fetch live L2 book, liquidations, and stops from Hyperliquid/Hyperdash."""
    res: Dict[str, Any] = {"l2": None, "liquidations": None, "stops": None}
    try:
        from Terminal.Api_Client import HyperdashClient
        client = HyperdashClient()
        l2 = client.fetch_l2_book(coin)
        res["l2"] = l2
        px = l2.get("best_bid", 0.0)
        if px > 0:
            try:
                res["liquidations"] = client.fetch_liquidations(coin, px * 0.85, px * 1.15)
            except Exception as e:
                res["liquidations_error"] = str(e)
            try:
                res["stops"] = client.fetch_stops(coin, px * 0.85, px * 1.15)
            except Exception as e:
                res["stops_error"] = str(e)
    except Exception as exc:
        res["error"] = str(exc)
    return res


def fetch_binance_mtf_orderflow(symbol: str) -> Dict[str, Any]:
    """Fetch running candle orderflow (Volume, Buy/Sell, Delta) for 4H, 1H, and 15m."""
    sym = f"{symbol.upper()}USDT"
    res: Dict[str, Any] = {}
    for tf in ["15m", "1h", "4h"]:
        try:
            url = f"https://fapi.binance.com/fapi/v1/klines?symbol={sym}&interval={tf}&limit=2"
            data = _http_get(url, timeout=3.0)
            if isinstance(data, list) and len(data) > 0:
                kl = data[-1]
                vol = float(kl[5])
                buy = float(kl[9])
                sell = max(0.0, vol - buy)
                delta = buy - sell
                delta_pct = (delta / vol * 100.0) if vol > 0 else 0.0
                open_px = float(kl[1])
                close_px = float(kl[4])
                chg_pct = ((close_px - open_px) / open_px * 100.0) if open_px > 0 else 0.0
                res[tf] = {
                    "open": open_px,
                    "high": float(kl[2]),
                    "low": float(kl[3]),
                    "close": close_px,
                    "change_pct": chg_pct,
                    "volume": vol,
                    "buy_volume": buy,
                    "sell_volume": sell,
                    "delta": delta,
                    "delta_pct": delta_pct,
                    "trades": int(kl[8]),
                }
        except Exception as exc:
            res[tf] = {"error": str(exc)}
    return res


# ==============================================================================
# MASTER PARALLEL DATA AGGREGATOR
# ==============================================================================

def aggregate_all_data(assets: List[str]) -> Dict[str, Any]:
    """Fetch all sources concurrently across threads with tight latency."""
    start_t = time.time()
    results = {
        "timestamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "timestamp_epoch": time.time(),
        "assets": assets,
        "mt5": {},
        "hyperliquid": {},
        "macro": {},
        "per_asset": {},
    }

    # Parallel tasks
    with ThreadPoolExecutor(max_workers=20) as executor:
        future_mt5 = executor.submit(fetch_mt5_account_and_quotes, assets + MACRO_ASSETS)
        future_hl = executor.submit(fetch_hyperliquid_data)
        future_macro = executor.submit(fetch_macro_sentiment_data)

        # Per-asset futures
        futures_bin_fut = {a: executor.submit(fetch_binance_futures_data, a) for a in assets}
        futures_bin_spot = {a: executor.submit(fetch_binance_spot_price, a) for a in assets}
        futures_cb = {a: executor.submit(fetch_coinbase_spot_price, a) for a in assets}
        futures_bybit = {a: executor.submit(fetch_bybit_ticker, a) for a in assets}
        futures_okx = {a: executor.submit(fetch_okx_ticker, a) for a in assets}
        futures_kraken = {a: executor.submit(fetch_kraken_ticker, a) for a in assets}

        # Extra single-asset institutional orderflow & Hyperdash deep-dive futures
        futures_hd_extra = {a: executor.submit(fetch_hyperdash_orderbook_and_analytics, a) for a in assets} if len(assets) == 1 else {}
        futures_mtf_extra = {a: executor.submit(fetch_binance_mtf_orderflow, a) for a in assets}

        # Resolve global
        results["mt5"] = future_mt5.result()
        results["hyperliquid"] = future_hl.result()
        results["macro"] = future_macro.result()

        # Resolve per-asset
        for a in assets:
            bf = futures_bin_fut[a].result()
            bs = futures_bin_spot[a].result()
            cb = futures_cb[a].result()
            bb = futures_bybit[a].result()
            okx = futures_okx[a].result()
            krk = futures_kraken[a].result()
            hd_analytics = futures_hd_extra[a].result() if a in futures_hd_extra else None
            mtf_orderflow = futures_mtf_extra[a].result() if a in futures_mtf_extra else None

            # Cross-venue comparison computations
            spot_cb = cb.get("spot_price")
            spot_bn = bs.get("spot_price")
            fut_bn = bf.get("futures_price")
            hl_coin = results["hyperliquid"].get("coins", {}).get(a, {})
            hl_mid = hl_coin.get("mid_price") or hl_coin.get("mark_price")

            # Coinbase Premium
            cb_premium_bps = None
            if spot_cb and spot_bn and spot_bn > 0:
                cb_premium_bps = round((spot_cb - spot_bn) / spot_bn * 1e4, 2)

            # Basis: Futures vs Spot
            basis_bps = None
            if fut_bn and spot_bn and spot_bn > 0:
                basis_bps = round((fut_bn - spot_bn) / spot_bn * 1e4, 2)

            # Cross-venue dispersion (max vs min %)
            prices = [p for p in [fut_bn, spot_bn, spot_cb, hl_mid, bb.get("last_price"), okx.get("last_price"), krk.get("last_price")] if p]
            dispersion_bps = None
            if len(prices) >= 2:
                p_min, p_max = min(prices), max(prices)
                dispersion_bps = round((p_max - p_min) / p_min * 1e4, 2)

            results["per_asset"][a] = {
                "binance_futures": bf,
                "binance_spot": bs,
                "coinbase_spot": cb,
                "bybit_linear": bb,
                "okx_swap": okx,
                "kraken_spot": krk,
                "hyperliquid": hl_coin,
                "hyperdash_analytics": hd_analytics,
                "binance_mtf": mtf_orderflow,
                "coinbase_premium_bps": cb_premium_bps,
                "basis_futures_spot_bps": basis_bps,
                "cross_venue_dispersion_bps": dispersion_bps,
            }

    results["elapsed_seconds"] = round(time.time() - start_t, 3)
    return results


def render_single_asset_deepdive(asset: str, data: Dict[str, Any], console: Console) -> None:
    """Render a comprehensive multi-table deep dive for a single asset."""
    a = asset.upper()
    p_info = data.get("per_asset", {}).get(a, {})
    mt5 = data.get("mt5", {})
    mt5_q = mt5.get("quotes", {}).get(a, {})
    bf = p_info.get("binance_futures", {})
    bs = p_info.get("binance_spot", {})
    cb = p_info.get("coinbase_spot", {})
    hl = p_info.get("hyperliquid", {})
    bb = p_info.get("bybit_linear", {})
    okx = p_info.get("okx_swap", {})
    krk = p_info.get("kraken_spot", {})

    baseline_spot = bs.get("spot_price") or 0.0

    # 1. Price & Arbitrage Table
    t_price = Table(title=f"[{a} CROSS-VENUE PRICE & BASIS ARBITRAGE (8 SOURCES)]", box=box.ROUNDED, expand=True)
    t_price.add_column("Venue / Source", style="bold yellow")
    t_price.add_column("Market Type", style="dim white")
    t_price.add_column("Live Price (USD)", style="bold green", justify="right")
    t_price.add_column("Delta vs Binance Spot", style="cyan", justify="right")
    t_price.add_column("Basis / Spread (bps)", style="magenta", justify="right")
    t_price.add_column("Feed Status", style="green", justify="center")

    def _row(venue, m_type, price, is_base=False, extra_bps=None):
        if price:
            delta = price - baseline_spot if (baseline_spot > 0 and not is_base) else 0.0
            delta_str = f"{delta:+,.2f} USD" if not is_base else "[dim]BASELINE[/dim]"
            bps = ((delta / baseline_spot) * 1e4) if (baseline_spot > 0 and not is_base) else (extra_bps or 0.0)
            bps_str = f"{bps:+.2f} bps" if not is_base else (f"{extra_bps:.1f} bps" if extra_bps else "[dim]0.0[/dim]")
            t_price.add_row(venue, m_type, f"{price:,.2f} USD", delta_str, bps_str, "[bold green]FRESH[/bold green]")
        else:
            t_price.add_row(venue, m_type, "-", "-", "-", "[dim red]UNAVAILABLE[/dim red]")

    mt5_mid = mt5_q.get("mid")
    mt5_spread = mt5_q.get("spread_bps")
    _row("MetaTrader 5 (Blueberry)", "Broker CFD Perpetuals", mt5_mid, extra_bps=mt5_spread)
    _row("Binance Spot", "Spot Exchange (Primary)", bs.get("spot_price"), is_base=True)
    _row("Binance Futures (USDT-M)", "Perpetual Swap", bf.get("futures_price"))
    _row("Coinbase Pro", "US Regulated Spot", cb.get("spot_price"))
    hl_p = hl.get("mid_price") or hl.get("mark_price")
    _row("Hyperliquid", "On-Chain Perpetuals DEX", hl_p)
    _row("Bybit Linear", "Linear Perpetuals", bb.get("last_price"))
    _row("OKX Swap", "Perpetuals Swap", okx.get("last_price"))
    _row("Kraken Spot", "Regulated Spot Exchange", krk.get("last_price"))

    console.print(t_price)

    # 2. Derivatives, Open Interest & Orderflow Table
    t_deriv = Table(title=f"[{a} DERIVATIVES, ORDERBOOK L2 DEPTH & TAKER CVD AUDIT]", box=box.ROUNDED, expand=True)
    t_deriv.add_column("Metric / Field", style="bold white")
    t_deriv.add_column("Primary Venue (Binance Futures)", style="cyan", justify="right")
    t_deriv.add_column("Secondary Venue (Hyperliquid / Bybit / MT5)", style="magenta", justify="right")
    t_deriv.add_column("Analysis / Consensus", style="yellow", justify="left")

    bn_oi_usd = bf.get("open_interest_usd")
    bn_oi_c = bf.get("open_interest_coins")
    hl_oi_c = hl.get("open_interest")
    hl_oi_usd = (hl_oi_c * (hl.get("mark_price") or 0)) if hl_oi_c else 0
    bb_oi_c = bb.get("open_interest")
    t_deriv.add_row(
        "Open Interest (USD Notional)",
        f"{bn_oi_usd / 1e6:,.2f} M USD ({bn_oi_c:,.1f} {a})" if bn_oi_usd else "-",
        f"HL: {hl_oi_usd / 1e6:,.2f} M USD | Bybit: {bb_oi_c:,.1f} {a}" if hl_oi_usd else "-",
        f"Consensus: {((bn_oi_usd or 0) + hl_oi_usd)/1e9:.2f}B USD aggregate"
    )

    bn_fr = bf.get("last_funding_rate_bps")
    hl_fr = hl.get("funding_rate")
    hl_fr_bps = (hl_fr * 1e4) if hl_fr is not None else None
    t_deriv.add_row(
        "Funding Rate (Current)",
        f"{bn_fr:+.4f} bps" if bn_fr is not None else "-",
        f"HL: {hl_fr_bps:+.4f} bps" if hl_fr_bps is not None else "-",
        "Neutral Basis"
    )

    b_usd = bf.get("top20_bid_usd") or 0
    a_usd = bf.get("top20_ask_usd") or 0
    imb = bf.get("book_imbalance") or 0
    t_deriv.add_row(
        "Top-20 Orderbook Depth",
        f"Bids: {b_usd:,.0f} USD | Asks: {a_usd:,.0f} USD",
        f"Best: Bid {bf.get('best_bid', 0):,.2f} / Ask {bf.get('best_ask', 0):,.2f}",
        f"Imbalance: {imb:+.2f} ({'Bid Skew' if imb > 0.05 else ('Ask Skew' if imb < -0.05 else 'Balanced')})"
    )

    wall = bf.get("largest_whale_wall") or "None resting >= 150k USD"
    t_deriv.add_row(
        "Largest Resting Whale Wall",
        wall,
        "[dim]Anonymous L2 Aggregated[/dim]",
        "Structural Liquidity Shelf"
    )

    c1 = bf.get("cvd_1m_delta_usd")
    c5 = bf.get("cvd_5m_delta_usd")
    c15 = bf.get("cvd_15m_delta_usd")
    trades = bf.get("cvd_1m_trades") or 0
    t_deriv.add_row(
        "Taker Orderflow CVD (AggTrades)",
        f"1m: {c1:+,.0f} USD | 5m: {c5:+,.0f} USD",
        f"15m: {c15:+,.0f} USD ({trades:,} trades/min)",
        f"{'Aggressive Buying' if (c5 or 0) > 0 else 'Aggressive Selling'}"
    )

    console.print(t_deriv)

    hd = p_info.get("hyperdash_analytics") or {}
    l2 = hd.get("l2") or {}
    liqs = hd.get("liquidations") or {}
    stops = hd.get("stops") or {}
    mtf = p_info.get("binance_mtf") or {}

    # 3. LEVEL 2 ORDERBOOK & VISUAL DEPTH LADDER (HYPERLIQUID L2)
    if l2 and l2.get("bids") and l2.get("asks"):
        t_book = Table(title=f"[{a} LEVEL 2 ORDERBOOK & VISUAL DEPTH LADDER (HYPERLIQUID)]", box=box.ROUNDED, expand=True)
        t_book.add_column("Price (USD)", justify="right", style="bold")
        t_book.add_column("Size", justify="right")
        t_book.add_column("Notional (USD)", justify="right")
        t_book.add_column("Visual Depth", justify="left")
        t_book.add_column("Side", justify="center")

        bids = l2.get("bids", [])[:8]
        asks = list(reversed(l2.get("asks", [])[:8]))
        max_vol = max([x.get("total_usd", 1.0) for x in bids + asks] + [1.0])

        # Asks (Red)
        for ask in asks:
            v = ask.get("total_usd", 0.0)
            bar_len = int((v / max_vol) * 30)
            bar = "█" * max(1, bar_len)
            t_book.add_row(
                f"{ask['price']:,.2f} USD",
                f"{ask['size']:.4f}",
                f"{v:,.0f} USD",
                f"[bright_red]{bar}[/bright_red]",
                "[bright_red]ASK (SELL)[/bright_red]",
            )

        # Spread Row
        spread = l2.get("spread", 0.0)
        spread_bps = l2.get("spread_bps", 0.0)
        t_book.add_row(
            "[bold yellow]─── SPREAD ───[/bold yellow]",
            f"[bold yellow]{spread:,.2f} USD[/bold yellow]",
            f"[bold yellow]{spread_bps:.2f} bps[/bold yellow]",
            "[dim yellow]──────────────────────────────[/dim yellow]",
            "[bold yellow]MID[/bold yellow]",
        )

        # Bids (Green)
        for bid in bids:
            v = bid.get("total_usd", 0.0)
            bar_len = int((v / max_vol) * 30)
            bar = "█" * max(1, bar_len)
            t_book.add_row(
                f"{bid['price']:,.2f} USD",
                f"{bid['size']:.4f}",
                f"{v:,.0f} USD",
                f"[bright_green]{bar}[/bright_green]",
                "[bright_green]BID (BUY)[/bright_green]",
            )

        bid_pct = l2.get("bid_pct", 50.0)
        ask_pct = l2.get("ask_pct", 50.0)
        bid_vol = l2.get("bid_volume_usd", 0.0)
        ask_vol = l2.get("ask_volume_usd", 0.0)
        meter_len = 35
        g_len = int((bid_pct / 100.0) * meter_len)
        r_len = meter_len - g_len
        ratio_bar = f"[bright_green]{'█' * g_len}[/bright_green][bright_red]{'█' * r_len}[/bright_red]"
        book_footer = f"Top-20 Bids: {bid_vol:,.0f} USD ({bid_pct:.1f}%) | {ratio_bar} | Top-20 Asks: {ask_vol:,.0f} USD ({ask_pct:.1f}%)"
        console.print(Panel(t_book, subtitle=book_footer, border_style="cyan", box=box.ROUNDED))

    # 4. CURRENT RUNNING CANDLE ORDERFLOW - 4H | 1H | 15M (BINANCE FUTURES)
    if mtf:
        t_mtf = Table(title=f"[{a} CURRENT RUNNING CANDLE ORDERFLOW - 4H | 1H | 15M (BINANCE FUTURES)]", box=box.ROUNDED, expand=True)
        t_mtf.add_column("Timeframe", style="bold yellow", justify="center")
        t_mtf.add_column("Candle Range (O -> C)", style="white", justify="right")
        t_mtf.add_column("High / Low", style="dim white", justify="right")
        t_mtf.add_column("Return %", style="bold", justify="right")
        t_mtf.add_column("Total Volume", style="cyan", justify="right")
        t_mtf.add_column("Taker Buy Vol", style="green", justify="right")
        t_mtf.add_column("Taker Sell Vol", style="red", justify="right")
        t_mtf.add_column("Net Delta", style="bold", justify="right")
        t_mtf.add_column("Delta Imbalance", style="bold", justify="center")
        t_mtf.add_column("Orderflow Pressure", style="bold", justify="left")

        for tf in ["4h", "1h", "15m"]:
            c_data = mtf.get(tf)
            if not c_data or "error" in c_data:
                t_mtf.add_row(tf.upper(), "-", "-", "-", "-", "-", "-", "-", "-", "[dim red]UNAVAILABLE[/dim red]")
                continue

            chg = c_data["change_pct"]
            chg_style = "bright_green" if chg >= 0 else "bright_red"
            chg_str = f"[{chg_style}]{chg:+.2f}%[/{chg_style}]"

            d = c_data["delta"]
            d_style = "bright_green" if d >= 0 else "bright_red"
            d_str = f"[{d_style}]{d:+,.2f} {a}[/{d_style}]"

            imb = c_data["delta_pct"]
            imb_style = "bold bright_green" if imb > 5.0 else ("bold bright_red" if imb < -5.0 else "white")
            imb_str = f"[{imb_style}]{imb:+.1f}%[/{imb_style}]"

            pressure = "[bold bright_green]BUYING ABSORPTION[/bold bright_green]" if imb > 10.0 else (
                "[bold bright_red]AGGRESSIVE SELLING[/bold bright_red]" if imb < -10.0 else (
                    "[bright_green]LEAN BUY[/bright_green]" if imb > 2.0 else (
                        "[bright_red]LEAN SELL[/bright_red]" if imb < -2.0 else "[dim white]NEUTRAL CONSOLIDATION[/dim white]"
                    )
                )
            )

            t_mtf.add_row(
                f"[bold cyan]{tf.upper()}[/bold cyan]",
                f"{c_data['open']:,.2f} -> {c_data['close']:,.2f}",
                f"H: {c_data['high']:,.2f} / L: {c_data['low']:,.2f}",
                chg_str,
                f"{c_data['volume']:,.1f} {a}",
                f"{c_data['buy_volume']:,.1f} {a}",
                f"{c_data['sell_volume']:,.1f} {a}",
                d_str,
                imb_str,
                pressure,
            )

        console.print(t_mtf)

    # 5. LIQUIDATION CASCADE CONCENTRATION LADDER (HYPERDASH ANALYTICS)
    if liqs and liqs.get("bands"):
        t_liq = Table(title=f"[{a} LIQUIDATION CASCADE CONCENTRATION LADDER (HYPERDASH ANALYTICS)]", box=box.ROUNDED, expand=True)
        t_liq.add_column("Price Band (USD)", style="bold", justify="right")
        t_liq.add_column("Distance %", justify="right")
        t_liq.add_column("Cascade Type", justify="center")
        t_liq.add_column("Estimated Liquidation Volume", justify="left")
        t_liq.add_column("Notional Amount", justify="right", style="bold")

        curr_px = liqs.get("current_price") or baseline_spot
        bands = liqs.get("bands", [])
        valid_bands = [b for b in bands if b.get("amount", 0.0) > 0]
        max_amt = max([b.get("amount", 0.0) for b in valid_bands] + [1.0])

        # Top 5 Short Squeeze (above price) + Top 5 Long Cascade (below price)
        above = sorted([b for b in valid_bands if b.get("mid_px", 0.0) >= curr_px], key=lambda x: x.get("mid_px", 0.0), reverse=True)[:5]
        below = sorted([b for b in valid_bands if b.get("mid_px", 0.0) < curr_px], key=lambda x: x.get("mid_px", 0.0), reverse=True)[:5]

        for b in above + below:
            mid = b.get("mid_px", 0.0)
            amt = b.get("amount", 0.0)
            dist = ((mid - curr_px) / curr_px * 100.0) if curr_px > 0 else 0.0
            is_above = mid >= curr_px
            liq_type = "[bright_red]SHORT SQUEEZE[/bright_red]" if is_above else "[bright_green]LONG CASCADE[/bright_green]"
            bar_color = "bright_red" if is_above else "bright_green"
            bar_len = int((amt / max_amt) * 28)
            bar = "█" * max(1, bar_len)
            t_liq.add_row(
                f"{b.get('min_px', 0.0):,.1f} - {b.get('max_px', 0.0):,.1f} USD",
                f"{dist:+.1f}%",
                liq_type,
                f"[{bar_color}]{bar}[/{bar_color}]",
                f"{amt:,.1f} {a}",
            )

        long_size = liqs.get("total_long_size", 0.0)
        short_size = liqs.get("total_short_size", 0.0)
        liq_sub = f"TOTAL LONG LIQUIDATION RISK: {long_size:,.1f} {a} (CASCADE RISK)  |  TOTAL SHORT LIQUIDATION RISK: {short_size:,.1f} {a} (SQUEEZE RISK)"
        console.print(Panel(t_liq, subtitle=liq_sub, border_style="magenta", box=box.ROUNDED))

    # 6. STOP-LOSS TRIGGER POOLS & BREAKOUT CLUSTERS (HYPERDASH ANALYTICS)
    if stops and stops.get("bands"):
        t_stop = Table(title=f"[{a} STOP-LOSS TRIGGER POOLS & BREAKOUT CLUSTERS (HYPERDASH ANALYTICS)]", box=box.ROUNDED, expand=True)
        t_stop.add_column("Price Range (USD)", style="bold", justify="right")
        t_stop.add_column("Distance %", justify="right")
        t_stop.add_column("Trigger Side", justify="center")
        t_stop.add_column("Stop Density", justify="left")
        t_stop.add_column("Stop Volume", justify="right", style="bold")

        curr_px = stops.get("current_price") or baseline_spot
        bands = stops.get("bands", [])
        valid_bands = [b for b in bands if b.get("amount", 0.0) > 0]
        max_amt = max([b.get("amount", 0.0) for b in valid_bands] + [1.0])

        above = sorted([b for b in valid_bands if b.get("mid_px", 0.0) >= curr_px], key=lambda x: x.get("mid_px", 0.0), reverse=True)[:5]
        below = sorted([b for b in valid_bands if b.get("mid_px", 0.0) < curr_px], key=lambda x: x.get("mid_px", 0.0), reverse=True)[:5]

        for b in above + below:
            mid = b.get("mid_px", 0.0)
            amt = b.get("amount", 0.0)
            dist = ((mid - curr_px) / curr_px * 100.0) if curr_px > 0 else 0.0
            is_above = mid >= curr_px
            side_badge = "[bright_cyan]BUY STOPS[/bright_cyan]" if is_above else "[bright_yellow]SELL STOPS[/bright_yellow]"
            bar_color = "bright_cyan" if is_above else "bright_yellow"
            bar_len = int((amt / max_amt) * 28)
            bar = "█" * max(1, bar_len)
            t_stop.add_row(
                f"{b.get('min_px', 0.0):,.1f} - {b.get('max_px', 0.0):,.1f} USD",
                f"{dist:+.1f}%",
                side_badge,
                f"[{bar_color}]{bar}[/{bar_color}]",
                f"{amt:,.1f} {a}",
            )

        buy_stops = stops.get("total_buy_size", 0.0)
        sell_stops = stops.get("total_sell_size", 0.0)
        stop_sub = f"TOTAL BUY STOPS (BREAKOUT ACCELERATION): {buy_stops:,.1f} {a}  |  TOTAL SELL STOPS (BREAKDOWN ACCELERATION): {sell_stops:,.1f} {a}"
        console.print(Panel(t_stop, subtitle=stop_sub, border_style="yellow", box=box.ROUNDED))


def render_dashboard(data: Dict[str, Any], console: Console, asset_filter: Optional[str] = None) -> None:
    """Render the master multi-source comparison tables."""
    console.clear()

    # Header Panel
    ts = data.get("timestamp_utc", "")
    elapsed = data.get("elapsed_seconds", 0.0)
    header_text = Text()
    header_text.append(">> REAL-TIME MULTI-SOURCE MARKET DATA & API AUDIT TERMINAL\n", style="bold cyan")
    header_text.append(f"As of: {ts} | Parallel Fetch Latency: {elapsed:.2f}s | Active Sources: 8 Venues + Macro Oracles", style="dim white")
    console.print(Panel(header_text, style="cyan", box=box.ROUNDED))

    # 1. BROKER ACCOUNT & FLOOR DEFENSE CARD
    mt5 = data.get("mt5") or {}
    acc = mt5.get("account") or {}
    balance = acc.get("balance", 0.0)
    equity = acc.get("equity", 0.0)
    margin_used = acc.get("margin_used", 0.0)
    margin_free = acc.get("margin_free", 0.0)
    open_pos = len(mt5.get("positions", [])) if isinstance(mt5.get("positions"), list) else 0
    pending_ord = len(mt5.get("orders", [])) if isinstance(mt5.get("orders"), list) else 0
    floor = 4775.00
    cushion = equity - floor
    buffer_val = 4795.00
    headroom = equity - buffer_val

    macro = data.get("macro") or {}
    fng = macro.get("fear_and_greed") or {}
    fng_str = f"{fng.get('value', 'N/A')} ({fng.get('classification', 'N/A')})"
    btc_flow = macro.get("btc_etf_flows") or {}
    btc_flow_str = f"{btc_flow.get('total_musd', 'N/A')} M USD ({btc_flow.get('date', 'N/A')})"

    acc_table = Table(box=box.SIMPLE_HEAD, expand=True)
    acc_table.add_column("MT5 Equity", style="bold green", justify="right")
    acc_table.add_column("Balance", style="white", justify="right")
    acc_table.add_column("Free Margin", style="cyan", justify="right")
    acc_table.add_column("Open Pos", style="yellow", justify="center")
    acc_table.add_column("Pending", style="yellow", justify="center")
    acc_table.add_column("Hard Floor", style="red", justify="right")
    acc_table.add_column("Floor Cushion", style="bold green" if cushion >= 20 else "bold red", justify="right")
    acc_table.add_column("Usable Headroom", style="bold cyan" if headroom > 0 else "bold red", justify="right")
    acc_table.add_column("Fear & Greed", style="magenta", justify="center")
    acc_table.add_column("BTC ETF Flow", style="blue", justify="right")

    acc_table.add_row(
        f"{equity:,.2f} USD",
        f"{balance:,.2f} USD",
        f"{margin_free:,.2f} USD",
        str(open_pos),
        str(pending_ord),
        f"{floor:,.2f} USD",
        f"+{cushion:,.2f} USD",
        f"+{headroom:,.2f} USD",
        fng_str,
        btc_flow_str,
    )
    console.print(Panel(acc_table, title="[bold][MT5 ACCOUNT & MACRO STATE][/bold]", border_style="blue", box=box.ROUNDED))

    # If single asset filter requested, render deep dive!
    if asset_filter:
        render_single_asset_deepdive(asset_filter, data, console)
        # Footer
        footer_text = Text()
        footer_text.append("Commands: ", style="bold")
        footer_text.append("--watch ", style="cyan")
        footer_text.append("(continuous 3s stream) | ")
        footer_text.append("python Terminal/live_data_terminal.py ", style="cyan")
        footer_text.append("(show all 12 assets) | ")
        footer_text.append("--json ", style="cyan")
        footer_text.append("(print raw JSON) | ")
        footer_text.append("Ctrl+C to exit", style="dim white")
        console.print(Panel(footer_text, style="dim", box=box.ROUNDED))
        return

    # 2. CROSS-VENUE PRICE & ARBITRAGE MATRIX
    assets_to_show = data.get("assets", [])
    
    price_table = Table(title="[CROSS-VENUE PRICE, SPREAD & ARBITRAGE COMPARISON - 8 SOURCES]", box=box.ROUNDED, expand=True)
    price_table.add_column("Asset", style="bold yellow", justify="left")
    price_table.add_column("MT5 Broker (Mid)", style="green", justify="right")
    price_table.add_column("Spread (bps)", style="dim white", justify="right")
    price_table.add_column("Binance Futures", style="bold white", justify="right")
    price_table.add_column("Binance Spot", style="white", justify="right")
    price_table.add_column("Coinbase Spot", style="cyan", justify="right")
    price_table.add_column("Hyperliquid", style="magenta", justify="right")
    price_table.add_column("Bybit Linear", style="white", justify="right")
    price_table.add_column("OKX Swap", style="white", justify="right")
    price_table.add_column("Kraken Spot", style="white", justify="right")
    price_table.add_column("CB Prem (bps)", style="bold yellow", justify="right")
    price_table.add_column("Dispersion", style="bold red", justify="right")

    for a in assets_to_show:
        p_info = data.get("per_asset", {}).get(a, {})
        mt5_q = mt5.get("quotes", {}).get(a, {})
        mt5_mid = f"{mt5_q.get('mid', 0):,.2f}" if mt5_q.get("mid") else "-"
        spread_bps = f"{mt5_q.get('spread_bps', 0):.1f}" if mt5_q.get("spread_bps") is not None else "-"

        bf_p = p_info.get("binance_futures", {}).get("futures_price")
        bf_str = f"{bf_p:,.2f}" if bf_p else "-"

        bs_p = p_info.get("binance_spot", {}).get("spot_price")
        bs_str = f"{bs_p:,.2f}" if bs_p else "-"

        cb_p = p_info.get("coinbase_spot", {}).get("spot_price")
        cb_str = f"{cb_p:,.2f}" if cb_p else "-"

        hl_coin = p_info.get("hyperliquid", {})
        hl_p = hl_coin.get("mid_price") or hl_coin.get("mark_price")
        hl_str = f"{hl_p:,.2f}" if hl_p else "-"

        bb_p = p_info.get("bybit_linear", {}).get("last_price")
        bb_str = f"{bb_p:,.2f}" if bb_p else "-"

        okx_p = p_info.get("okx_swap", {}).get("last_price")
        okx_str = f"{okx_p:,.2f}" if okx_p else "-"

        krk_p = p_info.get("kraken_spot", {}).get("last_price")
        krk_str = f"{krk_p:,.2f}" if krk_p else "-"

        cb_prem = p_info.get("coinbase_premium_bps")
        cb_prem_str = f"{cb_prem:+.2f}" if cb_prem is not None else "-"

        disp = p_info.get("cross_venue_dispersion_bps")
        disp_str = f"{disp:.1f} bps" if disp is not None else "-"

        price_table.add_row(
            a,
            mt5_mid,
            spread_bps,
            bf_str,
            bs_str,
            cb_str,
            hl_str,
            bb_str,
            okx_str,
            krk_str,
            cb_prem_str,
            disp_str,
        )

    console.print(price_table)

    # 3. ORDERBOOK L2 DEPTH, WHALES & TAKER CVD
    depth_table = Table(title="[ORDERBOOK L2 DEPTH, WHALE SENTRY & TAKER CVD - BINANCE & HYPERLIQUID]", box=box.ROUNDED, expand=True)
    depth_table.add_column("Asset", style="bold yellow")
    depth_table.add_column("Binance Top-20 Bids", style="green", justify="right")
    depth_table.add_column("Binance Top-20 Asks", style="red", justify="right")
    depth_table.add_column("Book Imbalance", style="bold cyan", justify="center")
    depth_table.add_column("1m CVD Delta", style="white", justify="right")
    depth_table.add_column("5m CVD Delta", style="bold yellow", justify="right")
    depth_table.add_column("15m CVD Delta", style="bold magenta", justify="right")
    depth_table.add_column("Open Interest (Binance)", style="white", justify="right")
    depth_table.add_column("Open Interest (HL)", style="white", justify="right")
    depth_table.add_column("Largest Whale Wall (>= 150k USD)", style="bold green", justify="left")

    for a in assets_to_show:
        bf = data.get("per_asset", {}).get(a, {}).get("binance_futures", {})
        hl_coin = data.get("per_asset", {}).get(a, {}).get("hyperliquid", {})

        b_usd = bf.get("top20_bid_usd")
        b_str = f"{b_usd:,.0f} USD" if b_usd else "-"

        a_usd = bf.get("top20_ask_usd")
        a_str = f"{a_usd:,.0f} USD" if a_usd else "-"

        imb = bf.get("book_imbalance")
        if imb is not None:
            imb_style = "bold green" if imb > 0.1 else ("bold red" if imb < -0.1 else "white")
            imb_str = f"[{imb_style}]{imb:+.2f}[/{imb_style}]"
        else:
            imb_str = "-"

        d1 = bf.get("cvd_1m_delta_usd")
        d1_str = f"{d1:+,.0f} USD" if d1 is not None else "-"

        d5 = bf.get("cvd_5m_delta_usd")
        d5_str = f"{d5:+,.0f} USD" if d5 is not None else "-"

        d15 = bf.get("cvd_15m_delta_usd")
        d15_str = f"{d15:+,.0f} USD" if d15 is not None else "-"

        bn_oi = bf.get("open_interest_usd")
        bn_oi_str = f"{bn_oi / 1e6:,.1f} M USD" if bn_oi else "-"

        hl_oi = hl_coin.get("open_interest")
        hl_px = hl_coin.get("mark_price", 0)
        hl_oi_usd = (hl_oi * hl_px) if hl_oi and hl_px else None
        hl_oi_str = f"{hl_oi_usd / 1e6:,.1f} M USD" if hl_oi_usd else "-"

        wall = bf.get("largest_whale_wall") or "[dim]None resting[/dim]"

        depth_table.add_row(
            a,
            b_str,
            a_str,
            imb_str,
            d1_str,
            d5_str,
            d15_str,
            bn_oi_str,
            hl_oi_str,
            wall,
        )

    console.print(depth_table)

    # 4. MULTI-TIMEFRAME ORDERFLOW & TAKER DELTA (ALL ASSETS)
    mtf_table = Table(title="[MULTI-TIMEFRAME RUNNING CANDLE ORDERFLOW - 15M | 1H | 4H (ALL ASSETS)]", box=box.ROUNDED, expand=True)
    mtf_table.add_column("Asset", style="bold yellow")
    mtf_table.add_column("15m Taker Delta", justify="right")
    mtf_table.add_column("15m Imbalance %", justify="center")
    mtf_table.add_column("1H Taker Delta", justify="right")
    mtf_table.add_column("1H Imbalance %", justify="center")
    mtf_table.add_column("4H Taker Delta", justify="right")
    mtf_table.add_column("4H Imbalance %", justify="center")
    mtf_table.add_column("Orderflow Regime", justify="left")

    for a in assets_to_show:
        mtf = data.get("per_asset", {}).get(a, {}).get("binance_mtf", {})
        c15 = mtf.get("15m", {})
        c1h = mtf.get("1h", {})
        c4h = mtf.get("4h", {})

        def _fmt_delta(c, sym):
            if not c or "delta" not in c:
                return "-", "-"
            d = c["delta"]
            d_col = "bright_green" if d > 0 else "bright_red"
            imb = c.get("delta_pct", 0.0)
            imb_col = "bold bright_green" if imb > 5.0 else ("bold bright_red" if imb < -5.0 else "white")
            return f"[{d_col}]{d:+,.1f} {sym}[/{d_col}]", f"[{imb_col}]{imb:+.1f}%[/{imb_col}]"

        d15_str, imb15_str = _fmt_delta(c15, a)
        d1h_str, imb1h_str = _fmt_delta(c1h, a)
        d4h_str, imb4h_str = _fmt_delta(c4h, a)

        imb15 = c15.get("delta_pct", 0.0) if c15 else 0.0
        regime = "[bold bright_green]BUY ABSORPTION[/bold bright_green]" if imb15 > 5.0 else (
            "[bold bright_red]AGGRESSIVE SELLING[/bold bright_red]" if imb15 < -5.0 else "[dim white]NEUTRAL CONSOLIDATION[/dim white]"
        )

        mtf_table.add_row(a, d15_str, imb15_str, d1h_str, imb1h_str, d4h_str, imb4h_str, regime)

    console.print(mtf_table)

    # Footer instructions
    footer_text = Text()
    footer_text.append("Commands: ", style="bold")
    footer_text.append("--watch ", style="cyan")
    footer_text.append("(continuous 3s stream) | ")
    footer_text.append("--asset BTC ", style="cyan")
    footer_text.append("(isolate single coin) | ")
    footer_text.append("--json ", style="cyan")
    footer_text.append("(print raw aggregated JSON payload) | ")
    footer_text.append("Ctrl+C to exit", style="dim white")
    console.print(Panel(footer_text, style="dim", box=box.ROUNDED))


# ==============================================================================
# MAIN ENTRYPOINT
# ==============================================================================

def main() -> None:
    parser = argparse.ArgumentParser(description="Multi-Source Real-Time Market Data Terminal")
    parser.add_argument("--asset", "-a", type=str, default=None, help="Filter to a specific asset (e.g. BTC, ETH, SOL)")
    parser.add_argument("--watch", "-w", action="store_true", help="Continuously refresh terminal every N seconds")
    parser.add_argument("--interval", "-i", type=float, default=3.0, help="Refresh interval in seconds (default: 3.0)")
    parser.add_argument("--json", "-j", action="store_true", help="Print raw aggregated JSON and exit")
    args = parser.parse_args()

    console = Console()

    assets = DEFAULT_CRYPTO_ASSETS
    if args.asset:
        target = args.asset.upper().replace("USDT", "").replace("USD", "")
        assets = [target]

    if args.json:
        data = aggregate_all_data(assets)
        print(json.dumps(data, indent=2))
        return

    if args.watch:
        try:
            while True:
                data = aggregate_all_data(assets)
                render_dashboard(data, console, args.asset)
                time.sleep(args.interval)
        except KeyboardInterrupt:
            console.print("\n[bold yellow]Terminal watch mode stopped by user.[/bold yellow]")
    else:
        data = aggregate_all_data(assets)
        render_dashboard(data, console, args.asset)


if __name__ == "__main__":
    main()
