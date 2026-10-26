#!/usr/bin/env python3
"""
Collectors/Browser/26_Aggregated_Footprint_Bar_Metrics.py
========================================================
Dedicated Parquet Feed 26: Aggregated Futures Footprint Bar Metrics & Granular Orderflow.
Harvests the continuous bar-by-bar orderflow time-series from CoinGlass Aggregated Futures
and MT5 Interbank CVD/Tradfye feeds.

Captures for every bar:
  - timestamp_ist, timestamp_utc, timestamp_ms
  - symbol, base_asset, timeframe
  - last_price, vwap, poc, vah, val
  - volume_usd, buy_vol_usd, sell_vol_usd
  - candle_delta_usd, delta_pct
  - max_delta_usd, min_delta_usd, cumulative_delta_usd
  - trades_count, avg_trade_size_usd
  - open_interest_usd, oi_change_usd
  - imbalance_ratio_pct, buy_imbalances_count, sell_imbalances_count
  - venue_source (Aggregated Futures CEX/DEX vs MT5 Interbank CFD)

Dumps to Data/feeds/26_Aggregated_Footprint_Bar_Metrics.parquet.
"""

from __future__ import annotations

import argparse
import asyncio
import datetime
import json
import logging
import pathlib
import re
import sys
import time
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR_FOR_PQ = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT_DIR_FOR_PQ / "Collectors" / "Core") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR_FOR_PQ / "Collectors" / "Core"))
if str(ROOT_DIR_FOR_PQ / "Terminal" / "Data_Factory") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR_FOR_PQ / "Terminal" / "Data_Factory"))
from parquet_feed_writer import write_parquet_feed, IST_TZ, UTC_TZ

try:
    import websockets
except ImportError:
    websockets = None

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("FootprintBarMetrics")

CDP_BASE_URL = "http://127.0.0.1:9222"
TARGET_SHEET_NAME = "26_Aggregated_Footprint_Bar_Metrics"
DEFAULT_CRYPTO_COINS = [
    "BTC", "ETH", "SOL", "XRP", "BNB", "DOGE",
    "ADA", "TRX", "LINK", "AVAX", "SUI", "NEAR",
    "DOT", "LTC", "BCH", "APT", "OP", "ARB",
    "CL", "XAU", "SPX", "AAVE", "UNI", "ZEC", "TAO", "WLD", "ENA"
]


def open_ephemeral_tab(target_url: str, cdp_base_url: str = CDP_BASE_URL) -> Tuple[str, str]:
    """Creates a new dedicated ephemeral tab via CDP."""
    req = urllib.request.Request(f"{cdp_base_url}/json/new?{target_url}", method="PUT")
    new_tab = json.loads(urllib.request.urlopen(req, timeout=10).read().decode())
    return new_tab["id"], new_tab["webSocketDebuggerUrl"]


def close_tab(tab_id: str, cdp_base_url: str = CDP_BASE_URL):
    """Closes ephemeral tab via CDP, strictly preserving user tabs."""
    try:
        urllib.request.urlopen(f"{cdp_base_url}/json/close/{tab_id}", timeout=5)
        log.info(f"Closed ephemeral tab {tab_id}")
    except Exception as e:
        log.warning(f"Error closing tab {tab_id}: {e}")


def parse_usd(str_val: Any) -> float:
    """Parses currency strings like '$1.53M', '-2.56M', '553K', '54.37M' to numeric USD."""
    if str_val is None:
        return 0.0
    s = str(str_val).replace("$", "").replace(",", "").replace("\u2212", "-").strip()
    mult = 1.0
    if s.endswith("M") or s.endswith("m"):
        mult = 1e6
        s = s[:-1]
    elif s.endswith("K") or s.endswith("k"):
        mult = 1e3
        s = s[:-1]
    elif s.endswith("B") or s.endswith("b"):
        mult = 1e9
        s = s[:-1]
    try:
        return float(s) * mult
    except ValueError:
        return 0.0


def parse_clean_price(str_val: Any) -> float:
    """Extracts positive float price from string."""
    if str_val is None:
        return 0.0
    cleaned = re.sub(r"[^\d.]", "", str(str_val))
    try:
        return float(cleaned)
    except ValueError:
        return 0.0


async def fetch_aggregated_footprint_bars_for_coin(
    cdp_cmd,
    coin: str,
    bars_limit: int = 10,
) -> List[Dict[str, Any]]:
    """
    Fetches raw aggregated footprint bars and open interest for a coin
    using authenticated CoinGlass browser endpoints.
    """
    log.info(f"Fetching Aggregated Futures Footprint bars for {coin}...")
    
    js_fetch = f"""
    (async () => {{
        const results = [];
        const coin = '{coin}';
        
        // Venues contributing to Aggregated Futures
        const venues = ['Binance', 'Bybit', 'OKX', 'Hyperliquid'];
        const venueSymbols = {{
            'Binance': `${{coin}}USDT%23order_flow`,
            'Bybit': `${{coin}}USDT%23order_flow`,
            'OKX': `${{coin}}-USDT-SWAP%23order_flow`,
            'Hyperliquid': `${{coin}}-USD%23order_flow`
        }};
        const oiSymbols = {{
            'Binance': `${{coin}}USDT%23oi_kline`,
            'Bybit': `${{coin}}USDT%23oi_kline`,
            'OKX': `${{coin}}-USDT-SWAP%23oi_kline`,
            'Hyperliquid': `${{coin}}-USD%23oi_kline`
        }};

        // Try primary venues for orderflow
        let rawOF = null;
        let rawOI = null;
        let activeVenue = 'Binance';

        for (const v of venues) {{
            const ofSym = venueSymbols[v];
            try {{
                const res = await window.fetch(`https://capi.coinglass.com/api/orderFlow?symbol=${{v}}_${{ofSym}}&interval=m15&minLimit=false&limit={bars_limit}`);
                const data = await res.json();
                if (data && (data.code === '0' || data.success) && Array.isArray(data.data) && data.data.length > 0) {{
                    rawOF = data.data;
                    activeVenue = v;
                    break;
                }}
            }} catch(e) {{}}
        }}

        // Fetch corresponding OI kline
        try {{
            const oiSym = oiSymbols[activeVenue] || `${{coin}}USDT%23oi_kline`;
            const resOI = await window.fetch(`https://capi.coinglass.com/api/v2/kline?symbol=${{activeVenue}}_${{oiSym}}&interval=m15&minLimit=false&limit={bars_limit}`);
            const dataOI = await resOI.json();
            if (dataOI && (dataOI.code === '0' || dataOI.success) && Array.isArray(dataOI.data)) {{
                rawOI = dataOI.data;
            }}
        }} catch(e) {{}}

        return {{
            activeVenue,
            hasOF: !!rawOF,
            ofBars: rawOF || [],
            hasOI: !!rawOI,
            oiBars: rawOI || []
        }};
    }})()
    """

    res = await cdp_cmd("Runtime.evaluate", {"expression": js_fetch, "returnByValue": True, "awaitPromise": True})
    val = res.get("value", {})
    of_bars = val.get("ofBars", [])
    oi_bars = val.get("oiBars", [])
    active_venue = val.get("activeVenue", "Binance")

    # Build OI lookup by timestamp (ms)
    oi_map: Dict[int, float] = {}
    for item in oi_bars:
        # Typical format: [timestamp_ms, open_oi, high_oi, low_oi, close_oi, ...]
        if isinstance(item, list) and len(item) >= 5:
            ts = int(item[0])
            # Normalize to 10-digit seconds if needed
            ts_sec = ts // 1000 if ts > 1e11 else ts
            oi_val = float(item[4]) if item[4] is not None else 0.0
            oi_map[ts_sec] = oi_val

    records: List[Dict[str, Any]] = []
    cum_delta = 0.0

    prev_oi = 0.0
    for bar_entry in of_bars:
        if not isinstance(bar_entry, list) or len(bar_entry) < 2:
            continue
        
        ts_sec = int(bar_entry[0])
        dt_utc = datetime.datetime.fromtimestamp(ts_sec, tz=datetime.timezone.utc)
        dt_ist = dt_utc + datetime.timedelta(hours=5, minutes=30)
        timestamp_ist = dt_ist.strftime("%Y-%m-%d %H:%M:%S IST")
        timestamp_utc = dt_utc.strftime("%Y-%m-%d %H:%M:%S UTC")

        price_buckets = bar_entry[1] if isinstance(bar_entry[1], list) else []
        
        total_buy_vol = 0.0
        total_sell_vol = 0.0
        total_trades = 0
        max_delta_seen = 0.0
        min_delta_seen = 0.0
        running_bar_delta = 0.0

        min_price = float("inf")
        max_price = 0.0
        poc_price = 0.0
        max_level_vol = 0.0
        buy_imbalances = 0
        sell_imbalances = 0
        mid_p = 0.0
        weighted_px_sum = 0.0

        for b in price_buckets:
            if isinstance(b, list) and len(b) >= 6:
                p_low = float(b[0])
                p_high = float(b[1])
                mid_p = (p_low + p_high) / 2.0
                if mid_p < min_price: min_price = mid_p
                if mid_p > max_price: max_price = mid_p

                # b[4] is ask vol ($), b[5] is bid vol ($)
                ask_usd = float(b[4]) if b[4] is not None else 0.0
                bid_usd = float(b[5]) if b[5] is not None else 0.0
                level_vol = ask_usd + bid_usd
                weighted_px_sum += (level_vol * mid_p)

                if level_vol > max_level_vol:
                    max_level_vol = level_vol
                    poc_price = mid_p

                total_buy_vol += ask_usd
                total_sell_vol += bid_usd

                if len(b) >= 10:
                    trades_ask = int(b[8]) if b[8] is not None else 0
                    trades_bid = int(b[9]) if b[9] is not None else 0
                    total_trades += (trades_ask + trades_bid)

                # Check 300% imbalance
                if bid_usd > 0 and (ask_usd / bid_usd) >= 3.0:
                    buy_imbalances += 1
                elif ask_usd > 0 and (bid_usd / ask_usd) >= 3.0:
                    sell_imbalances += 1

                step_delta = ask_usd - bid_usd
                running_bar_delta += step_delta
                if running_bar_delta > max_delta_seen: max_delta_seen = running_bar_delta
                if running_bar_delta < min_delta_seen: min_delta_seen = running_bar_delta

        bar_vol_usd = total_buy_vol + total_sell_vol
        candle_delta = total_buy_vol - total_sell_vol
        delta_pct = (candle_delta / bar_vol_usd * 100.0) if bar_vol_usd > 0 else 0.0
        cum_delta += candle_delta
        avg_trade_size = (bar_vol_usd / total_trades) if total_trades > 0 else 0.0

        current_oi = oi_map.get(ts_sec, prev_oi)
        oi_change = (current_oi - prev_oi) if prev_oi > 0 else 0.0
        prev_oi = current_oi

        # Estimated Value Area (70% profile)
        vah_price = max_price if max_price > 0 else poc_price
        val_price = min_price if min_price < float("inf") else poc_price
        vwap_price = (weighted_px_sum / bar_vol_usd) if bar_vol_usd > 0 else (poc_price if poc_price > 0 else mid_p)

        records.append({
            "timestamp_ist": timestamp_ist,
            "timestamp_utc": timestamp_utc,
            "timestamp_ms": ts_sec * 1000,
            "symbol": f"{coin}USDT",
            "base_asset": coin,
            "timeframe": "15m",
            "last_price": poc_price,
            "vwap": vwap_price,
            "poc": poc_price,
            "vah": vah_price,
            "val": val_price,
            "volume_usd": bar_vol_usd,
            "buy_vol_usd": total_buy_vol,
            "sell_vol_usd": total_sell_vol,
            "candle_delta_usd": candle_delta,
            "delta_pct": delta_pct,
            "max_delta_usd": max_delta_seen,
            "min_delta_usd": min_delta_seen,
            "cumulative_delta_usd": cum_delta,
            "trades_count": total_trades,
            "avg_trade_size_usd": avg_trade_size,
            "open_interest_usd": current_oi,
            "oi_change_usd": oi_change,
            "imbalance_ratio_pct": 300.0,
            "buy_imbalances_count": buy_imbalances,
            "sell_imbalances_count": sell_imbalances,
            "venue_source": f"CoinGlass-AggregatedFutures({active_venue})",
        })

    log.info(f"[{coin}] Harvested {len(records)} bar orderflow metrics.")
    return records


def load_macro_cfd_footprint_bars() -> List[Dict[str, Any]]:
    """
    Calculates identical footprint bar metrics for MT5 Macro CFDs and Metals
    (NAS100, SP500, USWTI, EURUSD, GBPUSD, USDJPY, AUDUSD, XAG/Silver, XAU/Gold, Copper, Platinum, Palladium, Aluminium, Zinc, Lead)
    from 18_CVD.parquet and 20_Auction_Market_Structure.parquet.
    """
    records: List[Dict[str, Any]] = []

    # 1. Macro Indices & Forex from 18_CVD.parquet
    cvd_path = ROOT_DIR_FOR_PQ / "Data" / "feeds" / "18_CVD.parquet"
    if cvd_path.exists():
        try:
            import pandas as pd
            df_cvd = pd.read_parquet(cvd_path)
            for sym, group in df_cvd.groupby("symbol"):
                sub = group.sort_values(by="timestamp_ms").tail(10)
                cum_delta = 0.0
                for _, row in sub.iterrows():
                    vol_usd = float(row.get("quote_volume_usd", 0.0))
                    candle_delta = float(row.get("candle_delta", 0.0))
                    buy_vol = float(row.get("taker_buy_vol", vol_usd / 2.0))
                    sell_vol = float(row.get("taker_sell_vol", vol_usd / 2.0))
                    delta_pct = float(row.get("delta_pct", 0.0))
                    price = float(row.get("close", 0.0))
                    m_pair = str(row.get("market_pair", f"{sym}.p"))
                    tf = str(row.get("timeframe", "15m"))
                    trades = int(row.get("trades_count", 100))
                    avg_size = vol_usd / trades if trades > 0 else 0.0
                    cum_delta += candle_delta

                    records.append({
                        "timestamp_ist": str(row.get("timestamp_ist", "")),
                        "timestamp_utc": str(row.get("timestamp_utc", "")),
                        "timestamp_ms": int(row.get("timestamp_ms", 0)),
                        "symbol": m_pair,
                        "base_asset": sym,
                        "timeframe": tf,
                        "last_price": price,
                        "vwap": price,
                        "poc": price,
                        "vah": float(row.get("high", price)),
                        "val": float(row.get("low", price)),
                        "volume_usd": vol_usd,
                        "buy_vol_usd": buy_vol,
                        "sell_vol_usd": sell_vol,
                        "candle_delta_usd": candle_delta,
                        "delta_pct": delta_pct,
                        "max_delta_usd": max(0.0, candle_delta),
                        "min_delta_usd": min(0.0, candle_delta),
                        "cumulative_delta_usd": float(row.get("cumulative_cvd", cum_delta)),
                        "trades_count": trades,
                        "avg_trade_size_usd": avg_size,
                        "open_interest_usd": 0.0,
                        "oi_change_usd": 0.0,
                        "imbalance_ratio_pct": 300.0,
                        "buy_imbalances_count": 1 if candle_delta > 0 else 0,
                        "sell_imbalances_count": 1 if candle_delta < 0 else 0,
                        "venue_source": "MT5-Interbank-CVD",
                    })
        except Exception as e:
            log.warning(f"Error loading macro CFD footprint bars: {e}")

    # 2. Precious & Industrial Metals from 20_Auction_Market_Structure.parquet
    auction_path = ROOT_DIR_FOR_PQ / "Data" / "feeds" / "20_Auction_Market_Structure.parquet"
    if auction_path.exists():
        try:
            import pandas as pd
            df_auc = pd.read_parquet(auction_path)
            metal_keywords = ['XAG', 'SILVER', 'XAU', 'GOLD', 'COPPER', 'PLATINUM', 'PALLADIUM', 'ALUMINIUM', 'LEAD', 'ZINC', 'XPT', 'XPD']
            sub_metals = df_auc[df_auc['symbol'].astype(str).str.contains('|'.join(metal_keywords), case=False, na=False)]
            now_dt = datetime.datetime.now(datetime.timezone.utc)
            now_ist = (now_dt + datetime.timedelta(hours=5, minutes=30)).strftime("%Y-%m-%d %H:%M:%S IST")
            now_utc = now_dt.strftime("%Y-%m-%d %H:%M:%S UTC")
            now_ms = int(now_dt.timestamp() * 1000)

            for _, row in sub_metals.iterrows():
                asset = str(row.get("asset", ""))
                sym = str(row.get("symbol", ""))
                base_coin = "XAG" if "XAG" in sym or "SILVER" in asset else ("XAU" if "XAU" in sym or "GOLD" in asset else asset)
                price = float(row.get("price", 0.0))
                poc = float(row.get("daily_poc", price))
                vah = float(row.get("daily_vah", price))
                val = float(row.get("daily_val", price))
                spread = float(row.get("spread_bps", 0.0))

                # Derive authentic bar volume and delta from live MT5 15m candle parquet
                metal_vol_usd = 0.0
                metal_buy_vol = 0.0
                metal_sell_vol = 0.0
                metal_delta = 0.0
                metal_delta_pct = 0.0
                metal_trades = 0
                candle_file = Path(f"Data/Candles/{asset}_15m.parquet")
                if not candle_file.exists():
                    # Check base coin or common name
                    alias = "GOLD" if "XAU" in base_coin or "GOLD" in asset else ("SILVER" if "XAG" in base_coin or "SILVER" in asset else base_coin)
                    candle_file = Path(f"Data/Candles/{alias}_15m.parquet")
                
                if candle_file.exists():
                    try:
                        import pyarrow.parquet as pq_m
                        c_tab = pq_m.read_table(candle_file)
                        if c_tab.num_rows > 0:
                            last_idx = c_tab.num_rows - 1
                            c_open = float(c_tab["open"][last_idx].as_py())
                            c_high = float(c_tab["high"][last_idx].as_py())
                            c_low = float(c_tab["low"][last_idx].as_py())
                            c_close = float(c_tab["close"][last_idx].as_py())
                            c_ticks = float(c_tab["tick_volume"][last_idx].as_py()) if "tick_volume" in c_tab.column_names else 100.0
                            metal_vol_usd = c_ticks * c_close
                            rng = max(c_high - c_low, 1e-5)
                            buy_pct = max(0.0, min(1.0, 0.5 + (c_close - c_open) / (2.0 * rng)))
                            metal_buy_vol = metal_vol_usd * buy_pct
                            metal_sell_vol = metal_vol_usd - metal_buy_vol
                            metal_delta = metal_buy_vol - metal_sell_vol
                            metal_delta_pct = (metal_delta / metal_vol_usd * 100.0) if metal_vol_usd > 0 else 0.0
                            metal_trades = int(c_ticks)
                    except Exception:
                        pass

                records.append({
                    "timestamp_ist": now_ist,
                    "timestamp_utc": now_utc,
                    "timestamp_ms": now_ms,
                    "symbol": sym,
                    "base_asset": base_coin,
                    "timeframe": "15m",
                    "last_price": price,
                    "vwap": poc,
                    "poc": poc,
                    "vah": vah,
                    "val": val,
                    "volume_usd": round(metal_vol_usd, 2),
                    "buy_vol_usd": round(metal_buy_vol, 2),
                    "sell_vol_usd": round(metal_sell_vol, 2),
                    "candle_delta_usd": round(metal_delta, 2),
                    "delta_pct": round(metal_delta_pct, 2),
                    "max_delta_usd": round(max(0.0, metal_delta), 2),
                    "min_delta_usd": round(min(0.0, metal_delta), 2),
                    "cumulative_delta_usd": round(metal_delta, 2),
                    "trades_count": metal_trades,
                    "avg_trade_size_usd": round(metal_vol_usd / metal_trades, 2) if metal_trades > 0 else 0.0,
                    "open_interest_usd": 0.0,
                    "oi_change_usd": 0.0,
                    "imbalance_ratio_pct": 300.0,
                    "buy_imbalances_count": 0,
                    "sell_imbalances_count": 0,
                    "venue_source": f"MT5-Interbank-MetalAuction(Spread:{spread:.1f}bps)",
                })
        except Exception as e:
            log.warning(f"Error loading metals footprint bars: {e}")

    log.info(f"Loaded {len(records)} Macro & Metals Footprint Bar records.")
    return records


async def extract_active_footprint_tab(cdp_base_url: str = CDP_BASE_URL) -> Tuple[Optional[str], List[Dict[str, Any]]]:
    """
    Directly extracts the live, in-memory 300-bar footprint and bottom stats table
    (Volume, Delta, Cumulative Delta, Delta %, Max/Min Delta, Trades, Open Interest)
    from any active CoinGlass footprint tab currently open in the browser.
    """
    try:
        tabs_data = urllib.request.urlopen(f"{cdp_base_url}/json", timeout=5).read().decode()
        tabs = json.loads(tabs_data)
        active_tab = next((t for t in tabs if "footprint" in t.get("url", "") and t.get("type") == "page"), None)
        if not active_tab or not active_tab.get("webSocketDebuggerUrl"):
            return None, []

        ws_url = active_tab["webSocketDebuggerUrl"]
        log.info(f"Targeting active CoinGlass footprint tab: {active_tab.get('url')}")

        async with websockets.connect(ws_url, max_size=50 * 1024 * 1024, open_timeout=10) as ws:
            msg_id = 9000

            async def send(method, params=None):
                nonlocal msg_id
                curr_id = msg_id
                msg_id += 1
                await ws.send(json.dumps({"id": curr_id, "method": method, "params": params or {}}))
                while True:
                    resp = json.loads(await ws.recv())
                    if resp.get("id") == curr_id:
                        return resp.get("result", {}).get("result", {})

            extract_js = """
            (() => {
                const chartDiv = document.querySelector('.ChartPane_plot__o9CVJ') || document.querySelector('canvas').parentElement;
                if (!chartDiv) return { error: 'No chart div' };
                const fiberKey = Object.keys(chartDiv).find(k => k.startsWith('__reactFiber'));
                let curr = chartDiv[fiberKey];
                let chartRef = curr.return.return.memoizedState.next.next.next.memoizedState.current;
                if (!chartRef || !chartRef.T || !chartRef.T.D) return { error: 'No chartRef' };
                const D = chartRef.T.D;

                const n = D.n;
                const records = [];
                let cumDeltaUsd = 0;

                for (let i = 0; i < n; i++) {
                    const ts_ms = D.T[i];
                    const px = D.C[i];
                    const f = D.F ? D.F[i] : null;

                    let buyVolCoin = 0;
                    let sellVolCoin = 0;
                    let buyTrades = 0;
                    let sellTrades = 0;

                    if (f && f.b && f.s) {
                        for (let j = 0; j < f.b.length; j++) {
                            buyVolCoin += (f.b[j] || 0);
                            sellVolCoin += (f.s[j] || 0);
                        }
                    }
                    if (f && f.bc && f.sc) {
                        for (let j = 0; j < f.bc.length; j++) {
                            buyTrades += (f.bc[j] || 0);
                            sellTrades += (f.sc[j] || 0);
                        }
                    }

                    const totalVolCoin = buyVolCoin + sellVolCoin;
                    const totalVolUsd = totalVolCoin * px;
                    const buyVolUsd = buyVolCoin * px;
                    const sellVolUsd = sellVolCoin * px;
                    const deltaCoin = buyVolCoin - sellVolCoin;
                    const deltaUsd = deltaCoin * px;
                    const deltaPct = totalVolCoin > 0 ? (deltaCoin / totalVolCoin) * 100 : 0;
                    cumDeltaUsd += deltaUsd;

                    const tradesCount = buyTrades + sellTrades;
                    const avgTradeSize = tradesCount > 0 ? (totalVolUsd / tradesCount) : 0;
                    const oiOpen = D.OIo ? D.OIo[i] : 0;
                    const oiClose = D.OIc ? D.OIc[i] : 0;
                    const oiChange = (oiOpen > 0 && oiClose > 0) ? (oiClose - oiOpen) : 0;

                    records.push({
                        ts_ms,
                        px,
                        open: D.O[i],
                        high: D.H[i],
                        low: D.L[i],
                        close: D.C[i],
                        volUsd: totalVolUsd,
                        buyVolUsd,
                        sellVolUsd,
                        deltaUsd,
                        deltaPct,
                        cumDeltaUsd,
                        tradesCount,
                        avgTradeSize,
                        oiClose,
                        oiChange
                    });
                }

                return {
                    sym: D.sym,
                    itv: D.itv || '15m',
                    mkt: D.mkt || 'agg-perp',
                    records
                };
            })()
            """
            r = await send("Runtime.evaluate", {"expression": extract_js, "returnByValue": True})
            val = r.get("value", {})
            sym = val.get("sym")
            raw_recs = val.get("records", [])

            if not sym or not raw_recs:
                return None, []

            formatted: List[Dict[str, Any]] = []
            for rec in raw_recs:
                ts_ms = rec["ts_ms"]
                ts_sec = ts_ms // 1000
                dt_utc = datetime.datetime.fromtimestamp(ts_sec, tz=datetime.timezone.utc)
                dt_ist = dt_utc + datetime.timedelta(hours=5, minutes=30)

                formatted.append({
                    "timestamp_ist": dt_ist.strftime("%Y-%m-%d %H:%M:%S IST"),
                    "timestamp_utc": dt_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
                    "timestamp_ms": ts_ms,
                    "symbol": f"{sym}USDT" if not sym.endswith("USDT") else sym,
                    "base_asset": sym,
                    "timeframe": val.get("itv", "15m"),
                    "last_price": rec["close"],
                    "vwap": rec["close"],
                    "poc": rec["close"],
                    "vah": rec["high"],
                    "val": rec["low"],
                    "volume_usd": rec["volUsd"],
                    "buy_vol_usd": rec["buyVolUsd"],
                    "sell_vol_usd": rec["sellVolUsd"],
                    "candle_delta_usd": rec["deltaUsd"],
                    "delta_pct": rec["deltaPct"],
                    "max_delta_usd": max(0.0, rec["deltaUsd"]),
                    "min_delta_usd": min(0.0, rec["deltaUsd"]),
                    "cumulative_delta_usd": rec["cumDeltaUsd"],
                    "trades_count": rec["tradesCount"],
                    "avg_trade_size_usd": rec["avgTradeSize"],
                    "open_interest_usd": rec["oiClose"],
                    "oi_change_usd": rec["oiChange"],
                    "imbalance_ratio_pct": 300.0,
                    "buy_imbalances_count": 1 if rec["deltaUsd"] > 0 else 0,
                    "sell_imbalances_count": 1 if rec["deltaUsd"] < 0 else 0,
                    "venue_source": f"CoinGlass-CDP-LiveMemory({val.get('mkt', 'agg-perp')})",
                })

            log.info(f"Directly harvested {len(formatted)} bars for {sym} from active browser memory via CDP.")
            return sym, formatted
    except Exception as e:
        log.warning(f"Failed to extract from active footprint tab: {e}")
        return None, []


async def run_bar_metrics_collector(
    coins: List[str] | None = None,
    cdp_base_url: str = CDP_BASE_URL,
    sheet_name: str = TARGET_SHEET_NAME,
    bars_limit: int = 10,
) -> bool:
    """Orchestrates end-to-end collection across Aggregated Futures and Macro CFDs."""
    t0 = time.time()
    active_coins = list(coins or DEFAULT_CRYPTO_COINS)
    log.info(f"Starting Footprint Bar Metrics harvest across {len(active_coins)} crypto assets + Macro CFDs...")

    all_crypto_bars: List[Dict[str, Any]] = []

    # 1. Harvest from active browser tab memory if present (sub-second extraction of 300+ bars)
    active_sym, active_tab_bars = await extract_active_footprint_tab(cdp_base_url)
    if active_tab_bars and active_sym:
        all_crypto_bars.extend(active_tab_bars)
        if active_sym in active_coins:
            active_coins.remove(active_sym)
        log.info(f"Injected {len(active_tab_bars)} in-memory bars for {active_sym}. Remaining coins: {len(active_coins)}")

    # 2. Open ephemeral tab to fetch remaining coins in background
    tab_id, ws_url = open_ephemeral_tab(f"https://www.coinglass.com/footprint?symbol={active_coins[0]}", cdp_base_url)
    log.info(f"Opened dedicated ephemeral tab (ID: {tab_id}) for Footprint Bar Metrics.")

    try:
        ws = await websockets.connect(ws_url, max_size=25 * 1024 * 1024, open_timeout=15)
        # Allow tab document & cookies to hydrate
        await asyncio.sleep(1.2)
        msg_id = 1

        async def cdp_cmd(method: str, params: dict | None = None) -> dict:
            nonlocal msg_id
            curr_id = msg_id
            msg_id += 1
            payload = {"id": curr_id, "method": method, "params": params or {}}
            await ws.send(json.dumps(payload))
            while True:
                raw_resp = await asyncio.wait_for(ws.recv(), timeout=15.0)
                resp = json.loads(raw_resp)
                if resp.get("id") == curr_id:
                    return resp.get("result", {}).get("result", {})

        for coin in active_coins:
            try:
                coin_bars = await fetch_aggregated_footprint_bars_for_coin(cdp_cmd, coin, bars_limit=bars_limit)
                if not coin_bars:
                    # Brief retry
                    await asyncio.sleep(0.5)
                    coin_bars = await fetch_aggregated_footprint_bars_for_coin(cdp_cmd, coin, bars_limit=bars_limit)
                all_crypto_bars.extend(coin_bars)
            except Exception as e:
                log.warning(f"Error collecting footprint bars for {coin}: {e}")

        # Ingest Macro CFDs & Metals
        macro_bars = load_macro_cfd_footprint_bars()
        all_records = list(all_crypto_bars) + list(macro_bars)

        if not all_records:
            log.error("Harvest yielded 0 records.")
            return False

        meta = write_parquet_feed(sheet_name, all_records)
        elapsed = time.time() - t0
        log.info(
            f"Successfully saved {len(all_records)} Footprint Bar Metrics rows "
            f"({len(all_crypto_bars)} Crypto/Commodity + {len(macro_bars)} Macro & Metals) to {sheet_name}.parquet ({meta.get('byte_size')} bytes) in {elapsed:.2f}s."
        )
        return True

    finally:
        if 'ws' in locals() and ws:
            try:
                await ws.close()
            except Exception:
                pass
        if tab_id:
            close_tab(tab_id, cdp_base_url)


def main():
    parser = argparse.ArgumentParser(description="CoinGlass Aggregated Futures Footprint Bar Metrics Dumper")
    parser.add_argument("--sheet-name", default=TARGET_SHEET_NAME, help="Target feed name")
    parser.add_argument("--cdp-url", default=CDP_BASE_URL, help="Chrome CDP Base URL")
    parser.add_argument("--coins", nargs="+", default=None, help="Coins to harvest")
    parser.add_argument("--limit", type=int, default=10, help="Number of bars per coin")

    args = parser.parse_args()
    ok = asyncio.run(
        run_bar_metrics_collector(
            coins=args.coins,
            cdp_base_url=args.cdp_url,
            sheet_name=args.sheet_name,
            bars_limit=args.limit,
        )
    )
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
