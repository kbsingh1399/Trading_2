"""
Terminal/Data_Factory/coinglass_extended_harvester.py
Ultra-Fast CoinGlass Comprehensive Harvester covering all 54 analytical tabs
from Market, Stocks, Institutions, Long/Short, Options, Heatmaps, and Technical Indicators.
Uses in-memory client-side Next.js routing in an ephemeral background tab with Edge session cookies.
"""

from __future__ import annotations
import asyncio
import datetime
import json
import os
import pathlib
import re
import sys
import time
import urllib.request
from typing import Any, Dict, List, Optional

import websockets

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.Data_Factory.time_series_database import ts_db

CDP_BASE_URL = "http://127.0.0.1:9222"
COINGLASS_DATA_DIR = ROOT / "Data" / "coinglass"
LATEST_SNAPSHOT_PATH = COINGLASS_DATA_DIR / "latest" / "coinglass_extended_snapshot.json"
HISTORY_DIR = ROOT / "Data" / "history" / "coinglass"

# Comprehensive endpoint catalog derived directly from user UI screenshots
EXTENDED_PAGES = [
    # --- Stocks (Screenshot 1) ---
    {"category": "stocks", "slug": "us_stocks_overview", "name": "US Stock Market Overview", "path": "/stocks", "wait_s": 1.5},
    {"category": "stocks", "slug": "stock_screener", "name": "Stock Screener", "path": "/stock-screener", "wait_s": 1.5},
    {"category": "stocks", "slug": "stock_heatmap", "name": "Stock Heatmap", "path": "/stock-heatmap", "wait_s": 1.5},
    {"category": "stocks", "slug": "stock_bubbles", "name": "Stock Bubbles", "path": "/stock-bubble", "wait_s": 1.5},

    # --- Market (Screenshot 2 - Column 1) ---
    {"category": "market", "slug": "crypto_overview", "name": "Cryptocurrency Overview", "path": "/", "wait_s": 1.5},
    {"category": "market", "slug": "volume_overview", "name": "Volume Overview", "path": "/volume", "wait_s": 1.5},
    {"category": "market", "slug": "token_unlock", "name": "Token Unlock Overview", "path": "/token-unlock", "wait_s": 1.5},
    {"category": "market", "slug": "crypto_heatmap", "name": "Crypto Market Cap Heatmap", "path": "/pro/heatmap/market-cap", "wait_s": 1.5},
    {"category": "market", "slug": "gainers_losers", "name": "Gainers & Losers", "path": "/gainers-losers", "wait_s": 1.5},
    {"category": "market", "slug": "spot_inflow_outflow", "name": "Spot Inflow / Outflow", "path": "/spot-inflow-outflow", "wait_s": 1.5},
    {"category": "market", "slug": "inflow_outflow_history", "name": "Inflow / Outflow History", "path": "/inflow-outflow-history", "wait_s": 1.5},
    {"category": "market", "slug": "gems_filter", "name": "GEMs Filter", "path": "/gems", "wait_s": 1.5},
    {"category": "market", "slug": "bull_market_peak_signals", "name": "Bull Market Peak Indicators", "path": "/bull-market-peak-signals", "wait_s": 1.5},
    {"category": "market", "slug": "coinglass_index", "name": "CoinGlass Index (CDRI)", "path": "/pro/i/CDRI", "wait_s": 1.5},
    {"category": "market", "slug": "crypto_flippening", "name": "Crypto Flippening Monitor", "path": "/reversal-index", "wait_s": 1.5},

    # --- Institutions & ETFs (Screenshot 2 - Column 2) ---
    {"category": "institutions", "slug": "crypto_etfs", "name": "Crypto ETFs Overview", "path": "/etf", "wait_s": 1.5},
    {"category": "institutions", "slug": "bitcoin_etfs", "name": "Bitcoin ETFs", "path": "/etf/bitcoin", "wait_s": 1.5},
    {"category": "institutions", "slug": "ethereum_etfs", "name": "Ethereum ETFs", "path": "/etf/ethereum", "wait_s": 1.5},
    {"category": "institutions", "slug": "solana_etfs", "name": "Solana ETFs", "path": "/etf/solana", "wait_s": 1.5},
    {"category": "institutions", "slug": "xrp_etfs", "name": "XRP ETFs", "path": "/etf/xrp", "wait_s": 1.5},
    {"category": "institutions", "slug": "hype_etfs", "name": "HYPE ETFs", "path": "/etf/hype", "wait_s": 1.5},
    {"category": "institutions", "slug": "hk_etfs", "name": "Hong Kong ETF", "path": "/hk-etf", "wait_s": 1.5},
    {"category": "institutions", "slug": "grayscale", "name": "Grayscale Holdings", "path": "/Grayscale", "wait_s": 1.5},
    {"category": "institutions", "slug": "gbtc_investors", "name": "Investors in GBTC", "path": "/GbtcInvestor", "wait_s": 1.5},
    {"category": "institutions", "slug": "bitcoin_treasuries", "name": "Bitcoin Treasuries", "path": "/BitcoinTreasuries", "wait_s": 1.5},
    {"category": "institutions", "slug": "ethereum_treasuries", "name": "Strategic Ethereum Reserve", "path": "/ETFTreasuries", "wait_s": 1.5},

    # --- Long / Short & Whales (Screenshot 2 - Column 3) ---
    {"category": "long_short", "slug": "long_short_ratio", "name": "Global Long/Short Ratio", "path": "/LongShortRatio", "wait_s": 1.5},
    {"category": "long_short", "slug": "top_trader_long_short", "name": "Top Trader Long/Short", "path": "/position", "wait_s": 1.5},
    {"category": "long_short", "slug": "binance_top_trader", "name": "Binance Top Trader", "path": "/TopTrader/Binance", "wait_s": 1.5},
    {"category": "long_short", "slug": "okx_top_trader", "name": "OKX Top Trader", "path": "/TopTrader/OKX", "wait_s": 1.5},
    {"category": "long_short", "slug": "whale_vs_retail_delta", "name": "Whale vs Retail Delta", "path": "/pro/i/whale-vs-retail-delta", "wait_s": 1.5},
    {"category": "long_short", "slug": "hype_burn", "name": "HYPE Burn", "path": "/hype-burn", "wait_s": 1.5},
    {"category": "long_short", "slug": "hyperliquid_wallets", "name": "Hyperliquid Wallet Analysis", "path": "/hl", "wait_s": 1.5},
    {"category": "long_short", "slug": "hyperliquid_whales", "name": "Hyperliquid Whale Tracker", "path": "/hyperliquid", "wait_s": 1.5},
    {"category": "long_short", "slug": "bitfinex_margin", "name": "Bitfinex Margin Longs/Shorts", "path": "/BitfinexMargin", "wait_s": 1.5},
    {"category": "long_short", "slug": "net_long_vs_short", "name": "Net Long vs Net Short", "path": "/net-longs-vs-net-short", "wait_s": 1.5},

    # --- Options (Screenshot 2 - Column 4) ---
    {"category": "options", "slug": "options_overview", "name": "Options Overview", "path": "/options", "wait_s": 1.5},
    {"category": "options", "slug": "options_net_premium", "name": "Options Net Premium Strike Heatmap", "path": "/pro/options/net-premium-strike-heatmap", "wait_s": 1.5},
    {"category": "options", "slug": "options_max_pain", "name": "Options Max Pain", "path": "/pro/options/max-pain", "wait_s": 1.5},
    {"category": "options", "slug": "options_open_interest", "name": "Options Open Interest", "path": "/pro/options/OpenInterest", "wait_s": 1.5},
    {"category": "options", "slug": "options_vol_expiry", "name": "Volume By Expiration", "path": "/pro/options/VolExpiry", "wait_s": 1.5},
    {"category": "options", "slug": "option_greeks", "name": "Option Greeks Tables", "path": "/pro/options/OptionGreeks", "wait_s": 1.5},

    # --- Technical Indicators & Cycles (Earlier Screenshots) ---
    {"category": "indicators", "slug": "macd_indicator", "name": "MACD Indicator (All Symbols)", "path": "/pro/i/MACD", "wait_s": 1.5},
    {"category": "indicators", "slug": "rsi_heatmap", "name": "RSI Heatmap", "path": "/pro/i/RsiHeatMap", "wait_s": 1.5},
    {"category": "indicators", "slug": "200wma", "name": "200 Week Moving Average Heatmap", "path": "/pro/i/200WMA", "wait_s": 1.5},
    {"category": "indicators", "slug": "two_year_ma", "name": "2-Year MA Multiplier", "path": "/pro/i/MA", "wait_s": 1.5},
    {"category": "indicators", "slug": "fear_greed", "name": "Crypto Fear & Greed Index", "path": "/pro/i/FearGreedIndex", "wait_s": 1.5},

    # --- Liquidity & Liquidations (Earlier Screenshots) ---
    {"category": "liquidations", "slug": "liquidation_heatmap", "name": "Liquidation Heatmap", "path": "/pro/futures/LiquidationHeatMap", "wait_s": 1.5},
    {"category": "liquidations", "slug": "liquidation_map", "name": "Crypto Liquidation Map", "path": "/pro/futures/LiquidationMap", "wait_s": 1.5},
    {"category": "liquidations", "slug": "liquidation_levels", "name": "Bitcoin Liquidation Levels Lines", "path": "/liquidation-levels", "wait_s": 1.5},
    {"category": "liquidations", "slug": "liquidation_maxpain", "name": "Futures Liquidation Max Pain", "path": "/liquidation-maxpain", "wait_s": 1.5},
    {"category": "liquidations", "slug": "aggregate_liquidations", "name": "24h Forced Liquidations", "path": "/liquidations", "wait_s": 1.5},

    # --- On-Chain ---
    {"category": "onchain", "slug": "exchange_balance", "name": "Bitcoin Exchange Balance", "path": "/Balance", "wait_s": 1.5},
    {"category": "onchain", "slug": "utxo_age_bands", "name": "Bitcoin Realized Price UTXO Age Bands", "path": "/pro/i/utxo", "wait_s": 1.5}
]


class CoinglassExtendedHarvester:
    """High-speed client-side router harvester extracting all 54 CoinGlass endpoints."""

    def __init__(self, cdp_url: str = CDP_BASE_URL):
        self.cdp_url = cdp_url
        COINGLASS_DATA_DIR.mkdir(parents=True, exist_ok=True)
        (COINGLASS_DATA_DIR / "latest").mkdir(parents=True, exist_ok=True)

    def _open_background_target(self) -> Dict[str, Any]:
        req = urllib.request.Request(f"{self.cdp_url}/json/new", method="PUT")
        resp = urllib.request.urlopen(req, timeout=5)
        return json.loads(resp.read().decode("utf-8"))

    def _close_target(self, target_id: str) -> None:
        try:
            urllib.request.urlopen(f"{self.cdp_url}/json/close/{target_id}", timeout=5)
        except Exception:
            pass

    async def harvest_all_tabs(self) -> Dict[str, Any]:
        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        start_ts = time.time()
        print(f"[{now_utc}] Starting Ultra-Fast CoinGlass Harvest ({len(EXTENDED_PAGES)} tabs)...")

        target = self._open_background_target()
        tid = target["id"]
        ws_url = target["webSocketDebuggerUrl"]
        print(f"Created ephemeral background tab: {tid}")

        results: Dict[str, Any] = {
            "harvest_timestamp_utc": now_utc,
            "harvest_epoch": time.time(),
            "tab_count": len(EXTENDED_PAGES),
            "domains": {}
        }

        try:
            async with websockets.connect(ws_url, max_size=50 * 1024 * 1024) as ws:
                async def send_cmd(method: str, params: Optional[dict] = None, cmd_id: int = 1):
                    payload = {"id": cmd_id, "method": method}
                    if params:
                        payload["params"] = params
                    await ws.send(json.dumps(payload))
                    while True:
                        raw = await ws.recv()
                        msg = json.loads(raw)
                        if msg.get("id") == cmd_id:
                            return msg

                # 1. Initial Page Load to prime Next.js router and session in memory
                await send_cmd("Page.enable", cmd_id=1)
                await send_cmd("Page.navigate", {"url": "https://www.coinglass.com/stocks"}, cmd_id=2)
                await asyncio.sleep(4.0)

                # Script to extract structured tables, stat cards, and SVG labels
                extract_js = """(() => {
                    const title = document.title;
                    const path = window.location.pathname;
                    
                    // Extract all tables (Ant Design or standard HTML)
                    const tables = Array.from(document.querySelectorAll('table')).map(table => {
                        const headers = Array.from(table.querySelectorAll('th')).map(th => th.innerText.trim().replace(/\\s+/g, ' '));
                        const rows = Array.from(table.querySelectorAll('.ant-table-row, tr')).map(tr => {
                            return Array.from(tr.querySelectorAll('td')).map(td => td.innerText.trim().replace(/\\s+/g, ' '));
                        }).filter(r => r.length > 0 && r.some(c => c.length > 0));
                        return { headers, rowCount: rows.length, rows: rows.slice(0, 150) };
                    });

                    // Extract all summary stat cards / metrics
                    const cards = Array.from(document.querySelectorAll('[class*=\"card\"], [class*=\"stat\"], [class*=\"metric\"], [class*=\"overview\"], [class*=\"item\"], [class*=\"summary\"]')).map(el => {
                        const t = el.innerText ? el.innerText.trim().replace(/\\s+/g, ' ') : '';
                        return (t.length > 3 && t.length < 250) ? t : null;
                    }).filter(Boolean).slice(0, 50);

                    // Extract SVG chart text & labels
                    const svgLabels = Array.from(document.querySelectorAll('svg text')).map(el => el.textContent.trim()).filter(t => t.length > 0 && t.length < 50).slice(0, 50);

                    return {
                        title,
                        path,
                        tableCount: tables.length,
                        tables,
                        cardsCount: cards.length,
                        cards,
                        svgLabelsCount: svgLabels.length,
                        svgLabels
                    };
                })()"""

                # 2. Iterate through all 54 pages with ultra-fast client-side transition
                for idx, page in enumerate(EXTENDED_PAGES, 1):
                    p_start = time.time()
                    path = page["path"]
                    slug = page["slug"]
                    cat = page["category"]
                    
                    # Client-side router.push() executes in ~1.2s
                    push_js = f"""(() => {{
                        if (window.next && window.next.router) {{
                            window.next.router.push('{path}');
                            return true;
                        }}
                        window.location.href = '{path}';
                        return false;
                    }})()"""
                    await send_cmd("Runtime.evaluate", {"expression": push_js, "returnByValue": True}, cmd_id=100 + idx)
                    await asyncio.sleep(page["wait_s"])

                    eval_res = await send_cmd("Runtime.evaluate", {"expression": extract_js, "returnByValue": True}, cmd_id=200 + idx)
                    page_data = eval_res.get("result", {}).get("result", {}).get("value", {})
                    
                    p_elapsed = time.time() - p_start
                    total_rows = sum(t.get("rowCount", 0) for t in page_data.get("tables", []))
                    
                    if cat not in results["domains"]:
                        results["domains"][cat] = {}
                    
                    results["domains"][cat][slug] = {
                        "name": page["name"],
                        "path": path,
                        "title": page_data.get("title", ""),
                        "table_count": page_data.get("tableCount", 0),
                        "total_rows": total_rows,
                        "tables": page_data.get("tables", []),
                        "cards": page_data.get("cards", []),
                        "svg_labels": page_data.get("svgLabels", []),
                        "harvest_elapsed_s": round(p_elapsed, 2)
                    }

                    print(f"[{idx:02d}/{len(EXTENDED_PAGES):02d}][{p_elapsed:.2f}s] {page['name']:35} -> {page_data.get('title')[:30]} | {total_rows} rows | {page_data.get('cardsCount', 0)} cards")

        finally:
            self._close_target(tid)
            print(f"Closed background tab: {tid}")

        total_elapsed = time.time() - start_ts
        results["total_harvest_duration_seconds"] = round(total_elapsed, 2)
        print(f"Harvest completed across all {len(EXTENDED_PAGES)} tabs in {total_elapsed:.2f}s!")

        # 3. Save Latest Extended Snapshot atomically
        from Terminal.Data_Factory.time_series_database import atomic_write_text
        atomic_write_text(LATEST_SNAPSHOT_PATH, json.dumps(results, indent=2))
        print(f"Saved latest snapshot to: {LATEST_SNAPSHOT_PATH}")

        # 4. Ingest into TimeSeriesDatabase (Gzip Compressed Partition + SQLite Relational Index)
        try:
            db_res = ts_db.record_snapshot("coinglass", results, compress=True)
            print(f"TimeSeriesDatabase: Archived to {db_res.get('history_file')} ({db_res.get('size_kb')} KB)")
        except Exception as e:
            print(f"TimeSeriesDatabase record notice: {e}")

        return results


if __name__ == "__main__":
    harvester = CoinglassExtendedHarvester()
    asyncio.run(harvester.harvest_all_tabs())
