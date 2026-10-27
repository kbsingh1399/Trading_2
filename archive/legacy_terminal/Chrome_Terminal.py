#!/usr/bin/env python3
"""
Terminal/Chrome_Terminal.py
Institutional Interactive Real-Time Web & Chrome Trading Terminal.
Provides a unified, ultra-low-latency dashboard featuring:
- Full Hyperdash Master Tabs: [Liquidations], [Stops], [Cohort Heatmap], [Orderbook]
- Dual Visualization Modes:
  * [Chart]: Candlesticks + Right-Side Horizontal Volume Profile Ladder with interactive hover & white price marker
  * [Historical]: 2D Time x Price Heatmap tiles under candles with left vertical intensity scale bar ($0 to $Max)
- Granularity Controls: Fine, Medium, Coarse resolution
- Multi-Timeframe Controls: 15m, 1h, 4h, 1d
- Live Price Ticker with directional arrows (▲/▼) and green/red flash updating every second
- Level 2 Orderbook with Visual Depth Bars & Bid/Ask Balance Meter
- Real-Time Liquidation Cascade Risk Ladder & Stop-Loss Concentration Clusters
- Level 3 Resting Whale Orders mapped to verified Ethereum Wallet Addresses
- Live Real-Time Trades Tape (Aggressor prints with whale alerts)
- Full 234-Coin Asset Universe Screener & Instant Asset Switching
"""

import sys
import os
import time
import datetime
import pathlib
import uvicorn
from typing import Dict, Any, List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Ensure workspace root is in sys.path
root_dir = pathlib.Path(__file__).parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from Terminal.Api_Client import HyperdashClient

app = FastAPI(title="Hyperdash Institutional Chrome Terminal", version="2.5")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global Client
CLIENT = HyperdashClient()
LAST_UNIVERSE_TIME = 0.0
CACHED_UNIVERSE: List[Dict[str, Any]] = []

def get_universe() -> List[Dict[str, Any]]:
    global LAST_UNIVERSE_TIME, CACHED_UNIVERSE
    now = time.time()
    if not CACHED_UNIVERSE or (now - LAST_UNIVERSE_TIME > 60.0):
        try:
            CACHED_UNIVERSE = CLIENT.fetch_all_assets()
            LAST_UNIVERSE_TIME = now
        except Exception as e:
            if not CACHED_UNIVERSE:
                raise e
    return CACHED_UNIVERSE

HEATMAP_ENGINES: Dict[str, Any] = {}

def get_heatmap_engine(coin: str, timeframe: str = "1h") -> Any:
    key = f"{coin}_{timeframe}"
    if key not in HEATMAP_ENGINES:
        from Terminal.Heatmap_Engine import HeatmapEngine
        HEATMAP_ENGINES[key] = HeatmapEngine(coin=coin, timeframe=timeframe)
    return HEATMAP_ENGINES[key]

LIVE_ANALYTICS_CACHE: Dict[str, Dict[str, Any]] = {}
ANALYTICS_CACHE_TTL = 8.0  # seconds
REFRESHING_COINS: set = set()

def _refresh_analytics_worker(coin: str, live_px: float):
    global LIVE_ANALYTICS_CACHE, REFRESHING_COINS
    try:
        now = time.time()
        cached = LIVE_ANALYTICS_CACHE.get(coin)
        liqs = cached.get("liquidations", {"kind": "UNAVAILABLE", "total_long_size": None, "total_short_size": None, "bands": [], "reason": "NO_VERIFIED_PROVIDER_DATA"}) if cached else {"kind": "UNAVAILABLE", "total_long_size": None, "total_short_size": None, "bands": [], "reason": "NO_VERIFIED_PROVIDER_DATA"}
        stops = cached.get("stops", {"kind": "UNAVAILABLE", "total_buy_size": None, "total_sell_size": None, "bands": [], "reason": "NO_VERIFIED_PROVIDER_DATA"}) if cached else {"kind": "UNAVAILABLE", "total_buy_size": None, "total_sell_size": None, "bands": [], "reason": "NO_VERIFIED_PROVIDER_DATA"}
        l3_orders = cached.get("l3_orders", []) if cached else []
        coarse_ob = cached.get("coarse_orderbook", {"bids": [], "asks": []}) if cached else {"bids": [], "asks": []}
        current_candle_info = cached.get("current_candle", {}) if cached else {}
        sources = dict(cached.get("sources", {})) if cached else {}
        wallet_risk = cached.get("wallet_risk", {}) if cached else {}

        # Hyperdash analytics are genuine provider responses, but their
        # historicalData.totalAmount unit/coverage and aggregation methodology
        # are NOT attested as exchange-reported hidden orders. Surface raw
        # bands for audit; do not convert them to "USD" or populate live bands.
        try:
            raw_liqs = CLIENT.fetch_liquidations(coin, max(0.0, live_px * .35), live_px * 2.10)
            sources["liquidations"] = {"observed_at": raw_liqs.get("received_at"),
                "timestamp_basis": "RECEIPT_ONLY", "provider": "HYPERDASH_GRAPHQL_ANALYTICS_UNVERIFIED_METHODOLOGY"}
            liqs = {"kind": "UNVERIFIED_BAND_LANDSCAPE", "bands": [],
                    "unverified_raw_bands": raw_liqs.get("bands") or [],
                    "reported_totals": {"long": raw_liqs.get("total_long_size"),
                                        "short": raw_liqs.get("total_short_size")},
                    "amount_semantics": "PROVIDER_REPORTED_UNIT_UNVERIFIED_NOT_USD",
                    "reason": "Unverified analytics units/coverage; no executable resting exposure"}
        except Exception:
            pass

        try:
            raw_stops = CLIENT.fetch_stops(coin, max(0.0, live_px * .35), live_px * 2.10)
            sources["stops"] = {"observed_at": raw_stops.get("received_at"),
                "timestamp_basis": "RECEIPT_ONLY", "provider": "HYPERDASH_GRAPHQL_ANALYTICS_UNVERIFIED_METHODOLOGY"}
            stops = {"kind": "UNVERIFIED_STOP_LANDSCAPE", "bands": [],
                     "unverified_raw_bands": raw_stops.get("bands") or [],
                     "reported_totals": {"buy": raw_stops.get("total_buy_size"),
                                         "sell": raw_stops.get("total_sell_size")},
                     "amount_semantics": "PROVIDER_REPORTED_UNIT_UNVERIFIED_NOT_USD",
                     "reason": "Unverified analytics units/coverage; use only sampled exchange stop triggers"}
        except Exception:
            pass

        # 3. L3 Whale Orders & Coarse Aggregated Orderbook
        try:
            raw_l3 = CLIENT.fetch_l3_orders(coin, live_px * 0.88, live_px * 1.12)
            sources["l3"] = {"observed_at": time.time(), "timestamp_basis": "RECEIPT_ONLY", "coverage": "WALLET_ATTRIBUTED_SNAPSHOT_NO_ORDER_ID_NOT_FULL_L3", "provider": "HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT"}
            new_l3 = []
            bucket_size = 1.0 if live_px > 50 else (0.1 if live_px > 5 else (0.01 if live_px > 0.5 else 0.001))
            b_bids = {}
            b_asks = {}

            for o in raw_l3:
                val = o.get("notional_usd", 0.0)
                px = o.get("price", 0.0)
                sz = o.get("size", 0.0)
                side = o.get("side", "")
                dist = ((px - live_px) / live_px * 100.0) if live_px > 0 else 0.0

                tier = "MEGA WHALE" if val >= 500000 else ("WHALE" if val >= 150000 else ("SHARK" if val >= 50000 else "DOLPHIN"))
                if len(new_l3) < 20:
                    new_l3.append({
                        "address": o.get("address", ""),
                        "side": side,
                        "price": px,
                        "size": sz,
                        "notional_usd": val,
                        "observed_at": o.get("observed_at"),
                        "tier": tier,
                        "dist_pct": dist
                    })

                b_px = round(px / bucket_size) * bucket_size
                if side == "BUY" and b_px <= live_px:
                    if b_px not in b_bids: b_bids[b_px] = {"price": b_px, "size": 0.0, "total_usd": 0.0, "orders": 0}
                    b_bids[b_px]["size"] += sz
                    b_bids[b_px]["total_usd"] += val
                    b_bids[b_px]["orders"] += 1
                elif side == "SELL" and b_px >= live_px:
                    if b_px not in b_asks: b_asks[b_px] = {"price": b_px, "size": 0.0, "total_usd": 0.0, "orders": 0}
                    b_asks[b_px]["size"] += sz
                    b_asks[b_px]["total_usd"] += val
                    b_asks[b_px]["orders"] += 1

            l3_orders = new_l3  # An observed empty book clears previous walls.
            try:
                risk_book = CLIENT.fetch_l2_book(coin)
                wallet_risk = CLIENT.fetch_wallet_risk(coin, [o.get("address") for o in new_l3], risk_book)
                sources["wallet_risk"] = {"observed_at": wallet_risk["observed_at"], "timestamp_basis": "RECEIPT_ONLY", "coverage": "SAMPLED_WALLETS", "provider": "HYPERLIQUID_PUBLIC_INFO"}
            except Exception:
                pass

            closest_asks = sorted(b_asks.keys())[:15]
            sorted_asks = [b_asks[k] for k in sorted(closest_asks, reverse=True)]
            closest_bids = sorted(b_bids.keys(), reverse=True)[:15]
            sorted_bids = [b_bids[k] for k in closest_bids]
            coarse_ob = {"bids": sorted_bids, "asks": sorted_asks, "bucket_size": bucket_size}
        except Exception:
            pass

        # 4. Current Candle Microstructure Status (read cached safely)
        try:
            key = f"{coin}_1h"
            if key in HEATMAP_ENGINES:
                current_candle_info = getattr(HEATMAP_ENGINES[key], "cached_current_candle", {}) or {}
        except Exception:
            pass

        LIVE_ANALYTICS_CACHE[coin] = {
            "timestamp": now,
            "liquidations": liqs,
            "stops": stops,
            "l3_orders": l3_orders,
            "coarse_orderbook": coarse_ob,
            "current_candle": current_candle_info
            ,"sources": sources, "wallet_risk": wallet_risk
        }
    finally:
        REFRESHING_COINS.discard(coin)

def get_live_analytics(coin: str, live_px: float) -> Dict[str, Any]:
    global LIVE_ANALYTICS_CACHE, REFRESHING_COINS
    now = time.time()
    cached = LIVE_ANALYTICS_CACHE.get(coin)

    # Initial load if never fetched
    if not cached:
        _refresh_analytics_worker(coin, live_px)
        return LIVE_ANALYTICS_CACHE.get(coin, {})

    # Non-blocking async background refresh if stale
    if (now - cached.get("timestamp", 0) > ANALYTICS_CACHE_TTL) and (coin not in REFRESHING_COINS):
        REFRESHING_COINS.add(coin)
        import threading
        threading.Thread(target=_refresh_analytics_worker, args=(coin, live_px), daemon=True).start()

    return cached

@app.get("/api/universe")
def api_universe():
    assets = get_universe()
    # Forensics round 3: on upstream failure get_universe() serves its cache
    # indefinitely - expose the fetch age so stale data is detectable.
    age = time.time() - LAST_UNIVERSE_TIME if LAST_UNIVERSE_TIME else None
    return {"count": len(assets), "assets": assets,
            "universe_fetched_at_epoch": LAST_UNIVERSE_TIME or None,
            "universe_age_seconds": round(age, 1) if age is not None else None,
            "universe_stale": bool(age is not None and age > 300.0)}

@app.get("/api/live/{coin}")
def api_live(coin: str):
    coin = coin.strip().upper()
    universe = get_universe()
    meta = next((a for a in universe if a["coin"] == coin), None)
    if not meta:
        raise HTTPException(status_code=404, detail=f"Asset {coin} not found in universe")

    mark_px = meta.get("mark_px", 0.0)

    # 1. Fast Path: Concurrent L2 Book & Recent Trades via Hyperliquid REST
    l2_book = {}
    trades = []
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=2) as executor:
        f_book = executor.submit(CLIENT.fetch_l2_book, coin)
        f_trades = executor.submit(CLIENT.fetch_recent_trades, coin)
        try:
            l2_book = f_book.result()
        except Exception as e:
            l2_book = {"bids": [], "asks": [], "spread": 0, "spread_bps": 0, "error": str(e)}
        try:
            trades = f_trades.result()
        except Exception:
            trades = []

    # Dynamic live price resolution
    live_px = mark_px
    if l2_book.get("best_bid") and l2_book.get("best_ask"):
        live_px = (l2_book["best_bid"] + l2_book["best_ask"]) / 2.0
    elif trades:
        live_px = float(max(trades, key=lambda t: float(t.get("time", 0))).get("px", mark_px))

    # 2. Analytics Path: Liquidations, Stops, L3 Whales (Cached with TTL)
    analytics = get_live_analytics(coin, live_px)

    # 3. Formatted Trades Tape
    formatted_trades = []
    for t in sorted(trades, key=lambda t: float(t.get("time", 0)), reverse=True)[:100]:
        px = float(t.get("px", 0.0))
        sz = float(t.get("sz", 0.0))
        notional = px * sz
        formatted_trades.append({
            "time": t.get("time", 0),
            "trade_id": t.get("tid", t.get("hash")),
            "side": "BUY" if t.get("side") == "B" else "SELL" if t.get("side") == "A" else "UNKNOWN",
            "price": px,
            "size": sz,
            "notional_usd": notional,
            "is_whale": notional >= 50000
        })

    # 4. Cohort Summary
    oi_usd = meta.get("open_interest_usd", 0.0)
    liq_totals = analytics.get("liquidations") or {}
    long_count = liq_totals.get("total_long_count")
    short_count = liq_totals.get("total_short_count")
    total_traders = (long_count + short_count if isinstance(long_count, (int, float))
                     and isinstance(short_count, (int, float)) else None)
    long_pct = round(long_count / total_traders * 100.0, 1) if total_traders and total_traders > 0 else None
    short_pct = round(100.0 - long_pct, 1) if long_pct is not None else None

    # Forensics round 3: the even 50/50 notional split below was a FABRICATED
    # statistic (no venue reports a long/short notional split here; OI is
    # two-sided by construction). Emit null + status instead of pseudo-data.
    cohort_summary = {
        "coin": coin,
        "notional_usd": oi_usd,
        "long_notional_usd": None,
        "short_notional_usd": None,
        "notional_split_status": "NOT_MEASURED (OI is two-sided; no venue split reported)",
        "total_traders": total_traders,
        "long_traders": long_count,
        "short_traders": short_count,
        "long_traders_pct": long_pct,
        "short_traders_pct": short_pct,
        "profit_traders_pct": None,
        "loss_traders_pct": None,
        "kind": "LIQUIDATION_COHORT_COUNTS_NOT_ALL_TRADERS"
    }

    return {
        "coin": coin,
        "price": live_px,
        "meta": meta,
        "signal_market": meta.get("signal_market"),
        "sources": {**analytics.get("sources", {}), "l2": {"observed_at": l2_book.get("timestamp", 0), "timestamp_basis": "VENUE_EVENT_TIME", "provider": "HYPERLIQUID_PUBLIC_INFO"}},
        "whale_positions": analytics.get("wallet_risk", {}).get("positions", []),
        "projected_liquidations": analytics.get("wallet_risk", {}).get("liquidations", {}),
        "observed_stops": analytics.get("wallet_risk", {}).get("stops", {}),
        "l2_book": l2_book,
        "liquidations": analytics.get("liquidations", {}),
        "stops": analytics.get("stops", {}),
        "l3_orders": analytics.get("l3_orders", []),
        "coarse_orderbook": analytics.get("coarse_orderbook", {"bids": [], "asks": []}),
        "cohort_summary": cohort_summary,
        "recent_trades": formatted_trades,
        "current_candle": analytics.get("current_candle", {}),
        # Forensics round 3: analytics (liq/stops/L3) are TTL-cached and may
        # lag the live book - publish the cache age alongside the payload.
        "analytics_cache_age_seconds": round(time.time() - analytics.get("timestamp", 0), 1) if analytics.get("timestamp") else None,
        "timestamp": int(time.time() * 1000),
        "utc_time": datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S UTC")
    }

@app.get("/api/heatmap/{coin}")
def api_heatmap(coin: str, mode: str = "liquidations", timeframe: str = "1h", granularity: str = "medium", lookback: int = 3):
    coin = coin.strip().upper()
    # Research heatmaps carry historical GraphQL bands forward into later
    # candles, infer side by price and label provider units USD. None of those
    # transformations is an observed resting stop/liquidation instruction.
    # Keep the research engine separate; do not publish it as a live chart.
    return {"coin": coin, "mode": mode, "timeframe": timeframe,
            "kind": "UNAVAILABLE_UNVERIFIED_ANALYTICS",
            "reason": "Hyperdash band methodology/unit not verified; carried-forward heatmaps are research, not live observations",
            "candles": [], "price_bands": [], "heatmap_grid": [], "volume_profile": [],
            "total_long_size": None, "total_short_size": None}

@app.get("/api/cohorts/{coin}")
def api_cohorts(coin: str, limit: int = 30):
    coin = coin.strip().upper()
    try:
        cohorts = CLIENT.fetch_top_traders(coin, limit=limit)
        if not cohorts:
            # Analytics liquidation bands do not report entry, leverage or
            # unrealized PnL. The former fallback fabricated these fields.
            return {"coin": coin, "cohorts": [],
                    "status": "UNAVAILABLE_NO_EXCHANGE_REPORTED_TRADER_POSITIONS"}
        return {"coin": coin, "cohorts": cohorts}
    except Exception as e:
        return {"coin": coin, "cohorts": [], "error": str(e)}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Hyperdash Institutional Terminal</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    :root {
      --bg-dark: #07090e;
      --bg-card: #0d121d;
      --bg-panel: #111827;
      --border-color: #1f293d;
      --text-main: #f3f4f6;
      --text-dim: #9ca3af;
      --accent-cyan: #00f0ff;
      --accent-green: #00ff88;
      --accent-red: #ff3366;
      --accent-yellow: #ffd700;
      --accent-magenta: #bd00ff;
      --font-mono: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-mono);
      font-size: 13px;
      overflow-x: hidden;
      padding: 10px;
    }
    /* Header Bar */
    header {
      background: var(--bg-card);
      border: 1px solid var(--accent-cyan);
      border-radius: 6px;
      padding: 10px 16px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 8px;
      box-shadow: 0 0 15px rgba(0, 240, 255, 0.15);
    }
    .brand-section {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .badge-brand {
      background: var(--accent-cyan);
      color: #000;
      font-weight: 900;
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 13px;
      letter-spacing: 1px;
    }
    .badge-live {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(0, 255, 136, 0.15);
      color: var(--accent-green);
      border: 1px solid var(--accent-green);
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: bold;
    }
    .pulse-dot {
      width: 7px;
      height: 7px;
      background: var(--accent-green);
      border-radius: 50%;
      animation: pulse 1s infinite alternate;
    }
    @keyframes pulse {
      0% { opacity: 0.3; transform: scale(0.8); }
      100% { opacity: 1; transform: scale(1.3); }
    }
    .coin-select {
      background: #111827;
      color: var(--accent-cyan);
      border: 1px solid var(--border-color);
      padding: 5px 12px;
      border-radius: 4px;
      font-family: inherit;
      font-weight: bold;
      font-size: 13px;
      cursor: pointer;
    }
    .price-box {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 20px;
      font-weight: bold;
      transition: all 0.3s;
      padding: 2px 8px;
      border-radius: 4px;
    }
    .price-flash-up {
      background: rgba(0, 255, 136, 0.25);
      box-shadow: 0 0 12px rgba(0, 255, 136, 0.5);
    }
    .price-flash-down {
      background: rgba(255, 51, 102, 0.25);
      box-shadow: 0 0 12px rgba(255, 51, 102, 0.5);
    }
    .stat-pill {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      font-size: 11px;
    }
    .stat-label { color: var(--text-dim); font-size: 10px; }
    .stat-val { font-weight: bold; }
    .text-green { color: var(--accent-green); }
    .text-red { color: var(--accent-red); }
    .text-cyan { color: var(--accent-cyan); }
    .text-yellow { color: var(--accent-yellow); }
    .text-magenta { color: var(--accent-magenta); }

    /* Master Tabs Navigation Bar (Directly matching Hyperdash.com) */
    .master-tabs-bar {
      display: flex;
      gap: 4px;
      background: #090d16;
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 4px 8px;
      margin-bottom: 8px;
      align-items: center;
    }
    .nav-tab {
      background: transparent;
      border: none;
      color: #94a3b8;
      font-family: inherit;
      font-size: 12px;
      font-weight: bold;
      padding: 8px 16px;
      cursor: pointer;
      border-radius: 4px;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .nav-tab:hover {
      color: #fff;
      background: rgba(255, 255, 255, 0.05);
    }
    .nav-tab.active {
      color: #000;
      background: var(--accent-cyan);
      box-shadow: 0 0 12px rgba(0, 240, 255, 0.4);
    }
    .nav-tab.active-stop {
      color: #fff;
      background: linear-gradient(135deg, #bd00ff, #ff007f);
      box-shadow: 0 0 12px rgba(255, 0, 127, 0.4);
    }

    /* Watchlist Ribbon */
    .watchlist-bar {
      display: flex;
      gap: 6px;
      overflow-x: auto;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 6px 12px;
      margin-bottom: 10px;
      align-items: center;
    }
    .watch-btn {
      background: #111827;
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 4px 10px;
      border-radius: 4px;
      font-family: inherit;
      font-size: 11px;
      cursor: pointer;
      font-weight: bold;
      white-space: nowrap;
      transition: all 0.2s;
    }
    .watch-btn:hover, .watch-btn.active {
      border-color: var(--accent-cyan);
      color: var(--accent-cyan);
      background: rgba(0, 240, 255, 0.1);
    }

    /* Candlestick & Orderflow Card */
    .heatmap-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      overflow: hidden;
      margin-bottom: 12px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    .heatmap-header {
      background: #111827;
      padding: 8px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border-color);
      flex-wrap: wrap;
      gap: 10px;
    }
    .btn-group {
      display: inline-flex;
      background: #090e17;
      border: 1px solid #1e293b;
      border-radius: 4px;
      padding: 2px;
      gap: 2px;
    }
    .view-btn {
      background: transparent;
      border: none;
      color: #94a3b8;
      padding: 4px 10px;
      border-radius: 3px;
      cursor: pointer;
      font-family: inherit;
      font-size: 11px;
      font-weight: bold;
      transition: all 0.2s;
    }
    .view-btn.active {
      background: var(--accent-cyan);
      color: #000;
      box-shadow: 0 0 8px rgba(0, 240, 255, 0.3);
    }
    .res-btn {
      background: transparent;
      border: none;
      color: #94a3b8;
      padding: 4px 8px;
      border-radius: 3px;
      cursor: pointer;
      font-family: inherit;
      font-size: 11px;
      font-weight: bold;
      transition: all 0.2s;
    }
    .res-btn.active {
      background: #334155;
      color: #fff;
    }
    .tf-btn {
      background: transparent;
      border: none;
      color: #94a3b8;
      padding: 4px 8px;
      border-radius: 3px;
      cursor: pointer;
      font-family: inherit;
      font-size: 11px;
      font-weight: bold;
      transition: all 0.2s;
    }
    .tf-btn.active {
      background: #334155;
      color: var(--accent-cyan);
      font-weight: bold;
    }
    .hud-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 6px 14px;
      background: #090e17;
      border-bottom: 1px solid #1e293b;
      font-size: 11px;
      flex-wrap: wrap;
      gap: 12px;
    }
    .hud-item {
      display: flex;
      gap: 6px;
      align-items: center;
    }
    .chart-wrapper {
      position: relative;
      background: #060911;
      width: 100%;
      height: 420px;
    }
    .chart-tooltip {
      position: absolute;
      pointer-events: none;
      background: rgba(13, 18, 29, 0.95);
      border: 1px solid var(--accent-cyan);
      border-radius: 4px;
      padding: 8px 12px;
      font-size: 11px;
      line-height: 1.4;
      color: #fff;
      z-index: 100;
      box-shadow: 0 4px 15px rgba(0, 240, 255, 0.3);
    }

    /* Cohort Heatmap Panel */
    .cohort-panel {
      padding: 12px;
      background: #060911;
      display: none;
      overflow-x: auto;
      max-height: 420px;
    }

    /* Dashboard Multi-Column Grid */
    .dashboard-grid {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 12px;
    }
    @media (max-width: 1200px) {
      .dashboard-grid { grid-template-columns: 1fr; }
    }
    .card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      overflow: hidden;
      margin-bottom: 12px;
    }
    .card-header {
      background: var(--bg-panel);
      padding: 8px 12px;
      font-weight: bold;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 12px;
      letter-spacing: 0.5px;
    }
    .card-body {
      padding: 8px;
      overflow-y: auto;
    }
    table.table-data, table.table-orderbook {
      width: 100%;
      border-collapse: collapse;
      font-size: 11px;
    }
    table.table-data th, table.table-orderbook th {
      color: var(--text-dim);
      font-weight: normal;
      padding: 4px 6px;
      border-bottom: 1px solid var(--border-color);
      font-size: 10px;
    }
    table.table-data td, table.table-orderbook td {
      padding: 3px 6px;
    }
    .text-left { text-align: left; }
    .text-right { text-align: right; }
    .text-center { text-align: center; }
    .spread-row {
      text-align: center;
      padding: 5px;
      background: #0b0f19;
      font-size: 11px;
      color: var(--accent-cyan);
      border-top: 1px dashed var(--border-color);
      border-bottom: 1px dashed var(--border-color);
      font-weight: bold;
    }
    .balance-meter {
      display: flex;
      height: 8px;
      border-radius: 4px;
      overflow: hidden;
      margin: 8px 0 4px 0;
      background: #1e293b;
    }
    .meter-bid { background: var(--accent-green); height: 100%; }
    .meter-ask { background: var(--accent-red); height: 100%; }
    .badge-tag {
      font-size: 9px;
      padding: 2px 6px;
      border-radius: 3px;
      font-weight: bold;
    }
  </style>
</head>
<body>

  <!-- Top Real-Time Master Header -->
  <header>
    <div class="brand-section">
      <div class="badge-brand">HYPERDASH</div>
      <div class="badge-live"><div class="pulse-dot"></div><span id="liveStatus">LIVE 1.0s</span></div>
      <select id="coinSelect" class="coin-select" onchange="switchCoin(this.value)">
        <option value="BTC">BTC</option>
        <option value="ETH">ETH</option>
        <option value="SOL">SOL</option>
        <option value="BNB">BNB</option>
        <option value="XRP">XRP</option>
      </select>
    </div>

    <div class="price-box" id="priceContainer">
      <span id="priceArrow" class="text-green">▲</span>
      <span class="price-main" id="markPrice">$84,150.00</span>
      <span id="changePill" class="badge-tag" style="background:rgba(0,255,136,0.2); color:var(--accent-green);">+0.42%</span>
    </div>

    <div style="display:flex; gap:16px; align-items:center;">
      <div class="stat-pill"><span class="stat-label">24h Vol</span><span class="stat-val text-yellow" id="vol24h">$3.52B</span></div>
      <div class="stat-pill"><span class="stat-label">Open Interest</span><span class="stat-val text-magenta" id="oiUsd">$3.17B</span></div>
      <div class="stat-pill"><span class="stat-label">Funding APR</span><span class="stat-val text-cyan" id="fundingApr">+1.37%</span></div>
      <div class="stat-pill"><span class="stat-label">Max Lev</span><span class="stat-val" id="maxLev">50x</span></div>
      <div class="stat-pill"><span class="stat-label">Clock</span><span class="stat-val" id="utcClock" style="color:#cbd5e1;">--:--:-- UTC</span></div>
    </div>
  </header>

  <!-- Master Feature Tabs Navigation Bar -->
  <div class="master-tabs-bar">
    <button class="nav-tab active" id="tabLiq" onclick="setMasterTab('liquidations')">🔥 Liquidations</button>
    <button class="nav-tab" id="tabStops" onclick="setMasterTab('stops')">🛡️ Stops</button>
    <button class="nav-tab" id="tabCohorts" onclick="setMasterTab('cohorts')">👥 Cohort Heatmap</button>
    <button class="nav-tab" id="tabOrderbook" onclick="setMasterTab('orderbook')">📖 Orderbook</button>
    <span style="margin-left:auto; font-size:11px; color:var(--text-dim);" id="latencyLabel">Latency: -- ms</span>
  </div>

  <!-- Watchlist Ribbon -->
  <div class="watchlist-bar">
    <span style="color:var(--text-dim); font-size:11px; margin-right:4px;">WATCHLIST:</span>
    <button class="watch-btn active" onclick="switchCoin('BTC')">BTC</button>
    <button class="watch-btn" onclick="switchCoin('ETH')">ETH</button>
    <button class="watch-btn" onclick="switchCoin('SOL')">SOL</button>
    <button class="watch-btn" onclick="switchCoin('BNB')">BNB</button>
    <button class="watch-btn" onclick="switchCoin('XRP')">XRP</button>
    <button class="watch-btn" onclick="switchCoin('DOGE')">DOGE</button>
    <button class="watch-btn" onclick="switchCoin('ADA')">ADA</button>
    <button class="watch-btn" onclick="switchCoin('SUI')">SUI</button>
    <button class="watch-btn" onclick="switchCoin('LINK')">LINK</button>
    <button class="watch-btn" onclick="switchCoin('AVAX')">AVAX</button>
  </div>

  <!-- Candlestick & Microstructure Heatmap Card -->
  <div class="heatmap-card">
    <div class="heatmap-header">
      <div style="display:flex; align-items:center; gap:12px; flex-wrap:wrap;">
        <span style="font-weight:bold; color:var(--accent-cyan); letter-spacing:0.5px;" id="mainCardTitle">CANDLESTICK · ORDERFLOW PROFILE</span>
        <span class="badge-tag" id="chartAssetTf" style="background:#1e293b; color:#fff;">ETH/USD · 1H</span>
        <span style="font-size:11px; color:var(--text-dim);" id="candleOhlcvLabel">
          O: <span id="cHdrOpen" class="text-green">--</span>
          H: <span id="cHdrHigh" class="text-green">--</span>
          L: <span id="cHdrLow" class="text-red">--</span>
          C: <span id="cHdrClose" style="font-weight:bold;">--</span>
          Vol: <span id="cHdrVol" class="text-yellow">--</span>
        </span>
      </div>

      <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
        <!-- View Mode Toggle: [● Live] vs [Chart] vs [Historical] -->
        <div class="btn-group">
          <button class="view-btn active" id="btnViewLive" onclick="setViewMode('live')">● Live</button>
          <button class="view-btn" id="btnViewChart" onclick="setViewMode('chart')">📈 Chart</button>
          <button class="view-btn" id="btnViewHist" onclick="setViewMode('historical')">📊 Historical</button>
        </div>

        <!-- Granularity Resolution: [Fine] / [Medium] / [Coarse] -->
        <div class="btn-group">
          <button class="res-btn" id="resFine" onclick="setGranularity('fine')">Fine</button>
          <button class="res-btn active" id="resMed" onclick="setGranularity('medium')">Medium</button>
          <button class="res-btn" id="resCoarse" onclick="setGranularity('coarse')">Coarse</button>
        </div>

        <!-- Multi-Timeframe Selection: [15m] / [1h] / [4h] / [1d] -->
        <div class="btn-group">
          <button class="tf-btn" id="tfBtn15m" onclick="setTimeframe('15m')">15m</button>
          <button class="tf-btn active" id="tfBtn1h" onclick="setTimeframe('1h')">1h</button>
          <button class="tf-btn" id="tfBtn4h" onclick="setTimeframe('4h')">4h</button>
          <button class="tf-btn" id="tfBtn1d" onclick="setTimeframe('1d')">1d</button>
        </div>
      </div>
    </div>

    <!-- Live Mode Interactive Toggles Legend Bar -->
    <div id="liveLegendBar" style="display:flex; justify-content:space-between; align-items:center; padding:6px 14px; background:#080c15; border-bottom:1px solid #1e293b; font-size:11px; flex-wrap:wrap; gap:10px;">
      <div style="display:flex; gap:16px; align-items:center;" id="liqLegendGroup">
        <label style="cursor:pointer; display:flex; align-items:center; gap:5px; color:#f43f5e; font-weight:bold;"><input type="checkbox" id="chkLongLiq" checked onchange="renderCanvas()"> Long liquidations</label>
        <label style="cursor:pointer; display:flex; align-items:center; gap:5px; color:#10b981; font-weight:bold;"><input type="checkbox" id="chkShortLiq" checked onchange="renderCanvas()"> Short liquidations</label>
        <label style="cursor:pointer; display:flex; align-items:center; gap:5px; color:#fb7185;"><input type="checkbox" id="chkCumLong" checked onchange="renderCanvas()"> Cumulative longs</label>
        <label style="cursor:pointer; display:flex; align-items:center; gap:5px; color:#34d399;"><input type="checkbox" id="chkCumShort" checked onchange="renderCanvas()"> Cumulative shorts</label>
      </div>
      <div style="display:none; gap:16px; align-items:center;" id="stopsLegendGroup">
        <label style="cursor:pointer; display:flex; align-items:center; gap:5px; color:#38bdf8; font-weight:bold;"><input type="checkbox" id="chkBuyStops" checked onchange="renderCanvas()"> Buy stops</label>
        <label style="cursor:pointer; display:flex; align-items:center; gap:5px; color:#eab308; font-weight:bold;"><input type="checkbox" id="chkSellStops" checked onchange="renderCanvas()"> Sell stops</label>
        <label style="cursor:pointer; display:flex; align-items:center; gap:5px; color:#0284c7;"><input type="checkbox" id="chkCumBuys" checked onchange="renderCanvas()"> Cumulative buys</label>
        <label style="cursor:pointer; display:flex; align-items:center; gap:5px; color:#ca8a04;"><input type="checkbox" id="chkCumSells" checked onchange="renderCanvas()"> Cumulative sells</label>
      </div>
      <div style="display:flex; gap:6px; align-items:center;">
        <span style="color:var(--text-dim); font-size:10px;">UNIT:</span>
        <div class="btn-group">
          <button class="res-btn" id="unitCoinBtn" onclick="setDenom('coin')">COIN</button>
          <button class="res-btn active" id="unitUsdBtn" onclick="setDenom('usd')">USD</button>
        </div>
      </div>
    </div>

    <!-- Active Candle Real-Time Orderflow HUD -->
    <div class="hud-bar">
      <div class="hud-item">
        <span style="color:var(--text-dim);">ACTIVE CANDLE:</span>
        <span id="candleTimeBadge" style="color:var(--accent-cyan); font-weight:bold;">--:-- UTC</span>
      </div>
      <div class="hud-item">
        <span style="color:var(--text-dim);">LONG CASCADE RISK:</span>
        <span class="text-green" id="hudLongLiq" style="font-weight:bold;">--</span>
      </div>
      <div class="hud-item">
        <span style="color:var(--text-dim);">SHORT SQUEEZE RISK:</span>
        <span class="text-red" id="hudShortLiq" style="font-weight:bold;">--</span>
      </div>
      <div class="hud-item">
        <span style="color:var(--text-dim);">PEAK LIQ LEVEL:</span>
        <span class="text-yellow" id="hudPeakLiq" style="font-weight:bold;">--</span>
      </div>
      <div class="hud-item">
        <span style="color:var(--text-dim);">STOPS CLUSTER:</span>
        <span class="text-cyan" id="hudTotalStops" style="font-weight:bold;">--</span>
      </div>
      <div class="hud-item" style="margin-left:auto;">
        <span style="color:#10b981; font-weight:bold; font-size:10px;">● RECORDING AT CANDLE LEVEL (PARQUET)</span>
      </div>
    </div>

    <!-- Interactive Canvas & Tooltip Container -->
    <div class="chart-wrapper" id="chartContainer">
      <canvas id="heatmapCanvas" height="420" style="width:100%; height:420px; display:block; cursor:crosshair;"></canvas>
      <div id="chartTooltip" class="chart-tooltip" style="display:none;"></div>
    </div>

    <!-- Cohort Heatmap Panel (Shown when Cohort Heatmap tab is active) -->
    <div class="cohort-panel" id="cohortsPanel">
      <table class="table-data" style="font-size:11px;">
        <thead>
          <tr style="color:var(--text-dim); border-bottom:1px solid #334155;">
            <th class="text-left" style="width:5%;">#</th>
            <th class="text-left" style="width:25%;">Trader / Wallet</th>
            <th class="text-center" style="width:10%;">Side</th>
            <th class="text-right" style="width:15%;">Size</th>
            <th class="text-right" style="width:15%;">Notional ($)</th>
            <th class="text-right" style="width:15%;">Entry Price ($)</th>
            <th class="text-right" style="width:15%;">Unrealized PnL ($)</th>
          </tr>
        </thead>
        <tbody id="cohortsBody"></tbody>
      </table>
    </div>

  </div>

  <!-- Dual Orderbook Panel (Matching Screenshot 3 when Orderbook Tab is active) -->
  <div id="dualOrderbookSection" style="display:none; margin-bottom:12px;">
    <div class="card">
      <div class="card-header">
        <div style="display:flex; align-items:center; gap:12px;">
          <span style="font-weight:bold; color:var(--accent-cyan);">DUAL ORDERBOOK & DEPTH PROFILE</span>
          <span class="badge-tag" style="background:#1e293b; color:#fff;" id="dualObCoin">SOL/USD</span>
        </div>
        <div style="display:flex; align-items:center; gap:8px;">
          <span style="font-size:10px; color:var(--text-dim);">TICK GROUPING:</span>
          <select id="obGroupingSelect" class="coin-select" style="font-size:11px; padding:2px 8px;" onchange="renderDualOrderbook()">
            <option value="1">1 USD</option>
            <option value="0.5">0.5 USD</option>
            <option value="0.1">0.1 USD</option>
          </select>
        </div>
      </div>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:1px; background:#1e293b;">
        <!-- Left: Coarse Aggregated Depth Ladder -->
        <div style="background:#090e17; padding:10px;">
          <div style="font-size:11px; font-weight:bold; color:var(--accent-cyan); margin-bottom:8px; display:flex; justify-content:space-between;">
            <span>AGGREGATED DEPTH LADDER</span>
            <span id="coarseSpreadLabel" style="color:var(--text-dim);">Spread: $1.00</span>
          </div>
          <table class="table-orderbook" style="font-size:11px;">
            <thead><tr><th>PRICE ($)</th><th style="text-align:right;">SIZE</th><th style="text-align:right;">TOTAL ($)</th></tr></thead>
            <tbody id="coarseAsksBody"></tbody>
          </table>
          <div class="spread-row" id="coarseMidRow" style="margin:4px 0;">MID PRICE: $119.50</div>
          <table class="table-orderbook" style="font-size:11px;">
            <tbody id="coarseBidsBody"></tbody>
          </table>
        </div>
        <!-- Right: Fine L2 Orderbook with Balance Meter -->
        <div style="background:#090e17; padding:10px;">
          <div style="font-size:11px; font-weight:bold; color:var(--accent-green); margin-bottom:8px; display:flex; justify-content:space-between;">
            <span>FINE LEVEL 2 DEPTH</span>
            <span id="fineSpreadLabel" class="text-cyan">Spread: $0.10 (0.084%)</span>
          </div>
          <table class="table-orderbook" style="font-size:11px;">
            <thead><tr><th>PRICE ($)</th><th style="text-align:right;">SIZE</th><th style="text-align:right;">TOTAL ($)</th></tr></thead>
            <tbody id="fineAsksBody"></tbody>
          </table>
          <div class="spread-row" id="fineMidRow" style="margin:4px 0;">SPREAD: $0.10 (0.084%)</div>
          <table class="table-orderbook" style="font-size:11px;">
            <tbody id="fineBidsBody"></tbody>
          </table>
          <div class="balance-meter" style="margin-top:10px;">
            <div id="dualMeterBid" class="meter-bid" style="width:45%;"></div>
            <div id="dualMeterAsk" class="meter-ask" style="width:55%;"></div>
          </div>
          <div style="display:flex; justify-content:space-between; font-size:10px; margin-top:3px;">
            <span class="text-green" id="dualBidPct">B 45%</span>
            <span class="text-red" id="dualAskPct">55% S</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Persistent Cohorts Dock (Directly from Hyperdash Screenshots 1, 2, and 3) -->
  <div class="card" style="margin-bottom:12px; background:#080c16; border-color:#1e293b;" id="persistentCohortsCard">
    <div style="display:flex; justify-content:space-between; align-items:center; padding:10px 16px; flex-wrap:wrap; gap:12px;">
      <div style="display:flex; align-items:center; gap:10px; cursor:pointer;" onclick="toggleCohortsExpand()">
        <div class="badge-brand" style="background:#1e293b; color:var(--accent-cyan); font-size:10px; padding:3px 8px;">COHORTS</div>
        <span style="font-weight:bold; color:#fff; font-size:13px;" id="cohortAssetTitle">SOL All traders</span>
        <span style="font-size:11px; color:var(--text-dim);" id="cohortExpandIcon">▼ Details</span>
      </div>
      <div style="display:flex; gap:28px; align-items:center; flex-wrap:wrap;">
        <!-- Notional -->
        <div style="min-width:160px;">
          <div style="display:flex; justify-content:space-between; margin-bottom:3px; font-size:11px;">
            <span style="color:var(--text-dim); font-size:10px;">NOTIONAL</span>
            <span style="color:#fff; font-weight:bold;" id="cohortNotionalTxt">$326.82M</span>
          </div>
          <div style="display:flex; height:6px; border-radius:3px; overflow:hidden; background:#1e293b;">
            <div style="width:50%; background:#10b981;" id="cohortNotionalLongBar"></div>
            <div style="width:50%; background:#f43f5e;" id="cohortNotionalShortBar"></div>
          </div>
          <div style="display:flex; justify-content:space-between; font-size:9px; color:var(--text-dim); margin-top:2px;">
            <span id="cohortNotionalLongTxt" class="text-green">50% Long</span>
            <span id="cohortNotionalShortTxt" class="text-red">50% Short</span>
          </div>
        </div>
        <!-- Traders -->
        <div style="min-width:160px;">
          <div style="display:flex; justify-content:space-between; margin-bottom:3px; font-size:11px;">
            <span style="color:var(--text-dim); font-size:10px;">TRADERS</span>
            <span style="color:#fff; font-weight:bold;" id="cohortTradersTxt">10,979</span>
          </div>
          <div style="display:flex; height:6px; border-radius:3px; overflow:hidden; background:#1e293b;">
            <div style="width:78%; background:#10b981;" id="cohortTradersLongBar"></div>
            <div style="width:22%; background:#f43f5e;" id="cohortTradersShortBar"></div>
          </div>
          <div style="display:flex; justify-content:space-between; font-size:9px; color:var(--text-dim); margin-top:2px;">
            <span id="cohortTradersLongTxt" class="text-green">78% Long</span>
            <span id="cohortTradersShortTxt" class="text-red">22% Short</span>
          </div>
        </div>
        <!-- Unrealized PnL -->
        <div style="min-width:160px;">
          <div style="display:flex; justify-content:space-between; margin-bottom:3px; font-size:11px;">
            <span style="color:var(--text-dim); font-size:10px;">UNREALIZED PNL</span>
            <span style="color:#fff; font-weight:bold;" id="cohortPnlTxt">8,992</span>
          </div>
          <div style="display:flex; height:6px; border-radius:3px; overflow:hidden; background:#1e293b;">
            <div style="width:64%; background:#10b981;" id="cohortPnlProfitBar"></div>
            <div style="width:36%; background:#f43f5e;" id="cohortPnlLossBar"></div>
          </div>
          <div style="display:flex; justify-content:space-between; font-size:9px; color:var(--text-dim); margin-top:2px;">
            <span id="cohortPnlProfitTxt" class="text-green">64% Profit</span>
            <span id="cohortPnlLossTxt" class="text-red">36% Loss</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Dashboard Multi-Column Grid -->
  <div class="dashboard-grid">
    
    <!-- Column 1: Orderbook L2 -->
    <div id="orderbookCardSection">
      <div class="card">
        <div class="card-header">
          <span>LEVEL 2 ORDERBOOK & DEPTH</span>
          <span id="orderbookCoin" class="text-cyan">BTC</span>
        </div>
        <div class="card-body" style="padding:0;">
          <table class="table-orderbook">
            <thead>
              <tr><th>Price ($)</th><th>Size</th><th>Total ($)</th></tr>
            </thead>
            <tbody id="asksBody"></tbody>
          </table>
          <div class="spread-row" id="spreadRow">SPREAD: $0.50 (0.06 bps)</div>
          <table class="table-orderbook">
            <tbody id="bidsBody"></tbody>
          </table>
        </div>
        <div style="padding:8px 12px; background:#0a0f1d; border-top:1px solid var(--border-color); font-size:10px;">
          <div style="display:flex; justify-content:space-between;">
            <span class="text-green" id="bidVolLabel">Bids: $1.5M (45%)</span>
            <span class="text-red" id="askVolLabel">Asks: $1.8M (55%)</span>
          </div>
          <div class="balance-meter">
            <div id="meterBid" class="meter-bid" style="width:45%;"></div>
            <div id="meterAsk" class="meter-ask" style="width:55%;"></div>
          </div>
          <div id="imbalanceBadge" style="text-align:center; font-weight:bold; margin-top:4px;" class="text-cyan">BALANCED FLOW</div>
        </div>
      </div>
    </div>

    <!-- Column 2: Liquidations & Stops -->
    <div>
      <!-- Liquidations Ladder -->
      <div class="card">
        <div class="card-header">
          <span>LIQUIDATION CASCADE RISK</span>
          <span class="badge-tag" style="background:rgba(189,0,255,0.2); color:var(--accent-magenta);">REAL-TIME</span>
        </div>
        <div class="card-body">
          <div style="font-size:11px; display:flex; justify-content:space-between; margin-bottom:8px; border-bottom:1px solid #1e293b; padding-bottom:6px;">
            <span class="text-green" id="longLiqTotal">Total Long Risk: 0</span>
            <span class="text-red" id="shortLiqTotal">Total Short Risk: 0</span>
          </div>
          <table class="table-data">
            <thead>
              <tr style="color:var(--text-dim); font-size:10px;">
                <th class="text-left" style="width:38%;">Band ($)</th>
                <th class="text-right" style="width:18%;">Dist %</th>
                <th class="text-center" style="width:24%;">Type</th>
                <th class="text-right" style="width:20%;">Volume ($)</th>
              </tr>
            </thead>
            <tbody id="liqBody"></tbody>
          </table>
        </div>
      </div>

      <!-- Stop Loss Clusters -->
      <div class="card">
        <div class="card-header">
          <span>STOP-LOSS CONCENTRATION CLUSTERS</span>
          <span class="badge-tag" style="background:rgba(255,215,0,0.2); color:var(--accent-yellow);">MICROSTRUCTURE</span>
        </div>
        <div class="card-body">
          <table class="table-data">
            <thead>
              <tr style="color:var(--text-dim); font-size:10px;">
                <th class="text-left" style="width:38%;">Cluster Range</th>
                <th class="text-right" style="width:18%;">Dist %</th>
                <th class="text-center" style="width:24%;">Trigger</th>
                <th class="text-right" style="width:20%;">Amount ($)</th>
              </tr>
            </thead>
            <tbody id="stopsBody"></tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Column 3: Whale Orders (L3) & Live Trades Tape -->
    <div>
      <!-- L3 Whale Orders -->
      <div class="card">
        <div class="card-header">
          <span>LEVEL 3 RESTING WHALE ORDERS</span>
          <span class="badge-tag" style="background:rgba(0,240,255,0.2); color:var(--accent-cyan);">WALLETS</span>
        </div>
        <div class="card-body" style="max-height:200px;">
          <table class="table-data" style="font-size:10px;">
            <thead>
              <tr style="color:var(--text-dim);">
                <th class="text-left" style="width:36%;">Wallet Address</th>
                <th class="text-center" style="width:16%;">Side</th>
                <th class="text-right" style="width:24%;">Price</th>
                <th class="text-right" style="width:24%;">Value ($)</th>
              </tr>
            </thead>
            <tbody id="whalesBody"></tbody>
          </table>
        </div>
      </div>

      <!-- Live Tape -->
      <div class="card">
        <div class="card-header">
          <span>REAL-TIME TRADES TAPE</span>
          <span class="badge-tag text-green">STREAMING</span>
        </div>
        <div class="card-body" style="max-height:220px;">
          <table class="table-data" style="font-size:10px;">
            <thead>
              <tr style="color:var(--text-dim);">
                <th class="text-left" style="width:26%;">Time</th>
                <th class="text-center" style="width:14%;">Side</th>
                <th class="text-right" style="width:24%;">Price ($)</th>
                <th class="text-right" style="width:16%;">Size</th>
                <th class="text-center" style="width:20%;">Alert</th>
              </tr>
            </thead>
            <tbody id="tradesBody"></tbody>
          </table>
        </div>
      </div>
    </div>

  </div>

  <script>
    let currentCoin = 'BTC';
    let prevPrice = 0.0;
    let universeAssets = [];
    
    // Master State
    let currentMasterTab = 'liquidations'; // 'liquidations', 'stops', 'cohorts', 'orderbook'
    let viewMode = 'live'; // 'live', 'chart', 'historical'
    let currentGranularity = 'medium'; // 'fine', 'medium', 'coarse'
    let currentTf = '1h'; // '15m', '1h', '4h', '1d'
    let currentDenom = 'usd'; // 'usd' or 'coin'
    let lastLiveData = null;
    let chartPayload = null;
    let hoveredPriceBand = null;
    let hoveredCandleIdx = -1;
    let cohortsExpanded = false;

    function formatVol(val) {
      if (!val || isNaN(val)) return '0';
      if (val >= 1e9) return (val / 1e9).toFixed(2) + 'B';
      if (val >= 1e6) return (val / 1e6).toFixed(2) + 'M';
      if (val >= 1e3) return (val / 1e3).toFixed(1) + 'k';
      return Math.round(val).toLocaleString();
    }

    function setDenom(d) {
      currentDenom = d;
      const coinBtn = document.getElementById('unitCoinBtn');
      const usdBtn = document.getElementById('unitUsdBtn');
      if (coinBtn) coinBtn.classList.toggle('active', d === 'coin');
      if (usdBtn) usdBtn.classList.toggle('active', d === 'usd');
      if (viewMode === 'live') {
        renderCanvas();
      }
    }

    // Bootstrap Universe
    async function loadUniverse() {
      try {
        const res = await fetch('/api/universe');
        const data = await res.json();
        universeAssets = data.assets || [];
        const select = document.getElementById('coinSelect');
        if (select) {
          select.innerHTML = '';
          universeAssets.slice(0, 100).forEach(a => {
            const opt = document.createElement('option');
            opt.value = a.coin;
            opt.textContent = `${a.coin} ($${a.mark_px.toLocaleString()})`;
            if (a.coin === currentCoin) opt.selected = true;
            select.appendChild(opt);
          });
        }
      } catch (e) {
        console.error('Universe load error:', e);
      }
    }

    function switchCoin(coin) {
      currentCoin = coin.toUpperCase();
      const select = document.getElementById('coinSelect');
      if (select) select.value = currentCoin;
      const unitCoinBtn = document.getElementById('unitCoinBtn');
      if (unitCoinBtn) unitCoinBtn.textContent = currentCoin;
      const chartAssetTf = document.getElementById('chartAssetTf');
      if (chartAssetTf) chartAssetTf.textContent = `${currentCoin}/USD · ${currentTf.toUpperCase()}`;
      document.querySelectorAll('.watch-btn').forEach(btn => {
        btn.classList.toggle('active', btn.textContent === currentCoin);
      });
      fetchLiveData();
      if (currentMasterTab === 'cohorts') {
        loadCohortsData();
      } else {
        loadHeatmapData();
      }
    }

    function setMasterTab(tab) {
      currentMasterTab = tab;
      
      const tabLiq = document.getElementById('tabLiq');
      const tabStops = document.getElementById('tabStops');
      const tabCohorts = document.getElementById('tabCohorts');
      const tabOrderbook = document.getElementById('tabOrderbook');
      if (tabLiq) tabLiq.className = 'nav-tab' + (tab === 'liquidations' ? ' active' : '');
      if (tabStops) tabStops.className = 'nav-tab' + (tab === 'stops' ? ' active-stop' : '');
      if (tabCohorts) tabCohorts.className = 'nav-tab' + (tab === 'cohorts' ? ' active' : '');
      if (tabOrderbook) tabOrderbook.className = 'nav-tab' + (tab === 'orderbook' ? ' active' : '');

      const chartCont = document.getElementById('chartContainer');
      const cohortsPanel = document.getElementById('cohortsPanel');
      const dualObSection = document.getElementById('dualOrderbookSection');
      const liveLeg = document.getElementById('liveLegendBar');
      const liqGroup = document.getElementById('liqLegendGroup');
      const stopsGroup = document.getElementById('stopsLegendGroup');
      const titleElem = document.getElementById('mainCardTitle');

      if (tab === 'cohorts') {
        if (chartCont) chartCont.style.display = 'none';
        if (liveLeg) liveLeg.style.display = 'none';
        if (dualObSection) dualObSection.style.display = 'none';
        if (cohortsPanel) cohortsPanel.style.display = 'block';
        if (titleElem) titleElem.textContent = 'SMART MONEY & WHALE COHORT POSITIONS';
        loadCohortsData();
      } else if (tab === 'orderbook') {
        if (chartCont) chartCont.style.display = 'none';
        if (liveLeg) liveLeg.style.display = 'none';
        if (cohortsPanel) cohortsPanel.style.display = 'none';
        if (dualObSection) dualObSection.style.display = 'block';
        if (titleElem) titleElem.textContent = 'DUAL ORDERBOOK & DEPTH PROFILE';
        renderDualOrderbook();
      } else {
        if (chartCont) chartCont.style.display = 'block';
        if (liveLeg) liveLeg.style.display = viewMode === 'live' ? 'flex' : 'none';
        if (cohortsPanel) cohortsPanel.style.display = 'none';
        if (dualObSection) dualObSection.style.display = 'none';
        if (tab === 'liquidations') {
          if (liqGroup) liqGroup.style.display = 'flex';
          if (stopsGroup) stopsGroup.style.display = 'none';
          if (titleElem) titleElem.textContent = 'LIVE LIQUIDATIONS DISTRIBUTION';
        } else {
          if (liqGroup) liqGroup.style.display = 'none';
          if (stopsGroup) stopsGroup.style.display = 'flex';
          if (titleElem) titleElem.textContent = 'LIVE STOP-LOSS CONCENTRATIONS';
        }
        if (viewMode === 'live') {
          renderCanvas();
        } else {
          loadHeatmapData();
        }
      }
    }

    function setViewMode(mode) {
      viewMode = mode;
      const btnLive = document.getElementById('btnViewLive');
      const btnChart = document.getElementById('btnViewChart');
      const btnHist = document.getElementById('btnViewHist');
      if (btnLive) btnLive.className = 'view-btn' + (mode === 'live' ? ' active' : '');
      if (btnChart) btnChart.className = 'view-btn' + (mode === 'chart' ? ' active' : '');
      if (btnHist) btnHist.className = 'view-btn' + (mode === 'historical' ? ' active' : '');

      const liveLeg = document.getElementById('liveLegendBar');
      if (liveLeg) {
        liveLeg.style.display = (mode === 'live' && (currentMasterTab === 'liquidations' || currentMasterTab === 'stops')) ? 'flex' : 'none';
      }

      renderCanvas();
    }

    function setGranularity(res) {
      currentGranularity = res;
      ['Fine', 'Med', 'Coarse'].forEach(r => {
        const id = 'res' + r;
        const elem = document.getElementById(id);
        if (elem) elem.classList.toggle('active', r.toLowerCase() === res.slice(0, 3).toLowerCase());
      });
      loadHeatmapData();
    }

    function setTimeframe(tf) {
      currentTf = tf;
      ['15m', '1h', '4h', '1d'].forEach(t => {
        const btn = document.getElementById('tfBtn' + t);
        if (btn) btn.className = 'tf-btn' + (t === tf ? ' active' : '');
      });
      const chartAssetTf = document.getElementById('chartAssetTf');
      if (chartAssetTf) chartAssetTf.textContent = `${currentCoin}/USD · ${tf.toUpperCase()}`;
      loadHeatmapData();
    }

    function toggleCohortsExpand() {
      cohortsExpanded = !cohortsExpanded;
      const icon = document.getElementById('cohortExpandIcon');
      if (cohortsExpanded) {
        setMasterTab('cohorts');
        if (icon) icon.textContent = '▲ Collapse';
      } else {
        setMasterTab('liquidations');
        if (icon) icon.textContent = '▼ Details';
      }
    }

    // Cohorts API Fetcher
    async function loadCohortsData() {
      const tbody = document.getElementById('cohortsBody');
      if (tbody) tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:20px; color:var(--accent-cyan);"><div class="pulse-dot" style="display:inline-block; margin-right:8px;"></div> Synchronizing top smart money & whale cohorts...</td></tr>';
      try {
        const res = await fetch(`/api/cohorts/${currentCoin}`);
        const data = await res.json();
        const cohorts = data.cohorts || [];
        if (!cohorts || cohorts.length === 0) {
          tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:20px; color:var(--text-dim);">No active smart money cohort positions found for this asset.</td></tr>';
          return;
        }
        tbody.innerHTML = cohorts.map((c, idx) => {
          const shortAddr = c.address ? (c.address.slice(0, 6) + '...' + c.address.slice(-4)) : 'Anonymous';
          const name = c.displayName || shortAddr;
          const sz = parseFloat(c.size || 0);
          const isLong = sz > 0;
          const sideTag = isLong ? '<span class="badge-tag text-green" style="background:rgba(0,255,136,0.15);">LONG</span>' : '<span class="badge-tag text-red" style="background:rgba(255,51,102,0.15);">SHORT</span>';
          const notional = parseFloat(c.notional || 0);
          const entryPx = parseFloat(c.entryPrice || 0);
          const pnl = parseFloat(c.unrealizedPnl || 0);
          const roe = parseFloat(c.returnOnEquity || 0) * 100.0;
          const pnlClass = pnl >= 0 ? 'text-green' : 'text-red';

          return `<tr style="border-bottom:1px solid #1e293b;">
            <td style="color:var(--text-dim);">${idx + 1}</td>
            <td><b style="color:var(--accent-cyan); font-family:monospace;">${name}</b></td>
            <td style="text-align:center;">${sideTag}</td>
            <td style="text-align:right;">${Math.abs(sz).toFixed(3)} ${currentCoin}</td>
            <td style="text-align:right; font-weight:bold;">$${Math.round(notional).toLocaleString()}</td>
            <td style="text-align:right;">$${entryPx.toLocaleString(undefined, {minimumFractionDigits: 1, maximumFractionDigits: 1})}</td>
            <td style="text-align:right;" class="${pnlClass}">
              <b>${(pnl >= 0 ? '+' : '')}$${Math.round(pnl).toLocaleString()}</b>
              <span style="font-size:9px;">(${(roe >= 0 ? '+' : '')}${roe.toFixed(1)}%)</span>
            </td>
          </tr>`;
        }).join('');
      } catch (e) {
        console.error('Cohorts load error:', e);
      }
    }

    // Heatmap / Chart API Fetcher
    async function loadHeatmapData() {
      if (currentMasterTab === 'cohorts' || currentMasterTab === 'orderbook') return;
      try {
        const mode = currentMasterTab === 'stops' ? 'stops' : 'liquidations';
        const res = await fetch(`/api/heatmap/${currentCoin}?mode=${mode}&timeframe=${currentTf}&granularity=${currentGranularity}`);
        chartPayload = await res.json();
        const chartAssetTf = document.getElementById('chartAssetTf');
        if (chartAssetTf) chartAssetTf.textContent = chartPayload.kind === 'UNAVAILABLE_UNVERIFIED_ANALYTICS'
          ? `${currentCoin} · CHART UNAVAILABLE (UNVERIFIED UNITS)`
          : `${currentCoin}/USD · ${currentTf.toUpperCase()}`;

        const candles = chartPayload.candles || [];
        if (candles.length > 0) {
          const lastC = candles[candles.length - 1];
          const cOpen = document.getElementById('cHdrOpen');
          const cHigh = document.getElementById('cHdrHigh');
          const cLow = document.getElementById('cHdrLow');
          const cClose = document.getElementById('cHdrClose');
          const cVol = document.getElementById('cHdrVol');
          if (cOpen) cOpen.textContent = lastC.open.toLocaleString();
          if (cHigh) cHigh.textContent = lastC.high.toLocaleString();
          if (cLow) cLow.textContent = lastC.low.toLocaleString();
          if (cClose) cClose.textContent = lastC.close.toLocaleString();
          if (cVol) cVol.textContent = Math.round(lastC.volume).toLocaleString();
        }

        renderCanvas();
      } catch (err) {
        console.error('Heatmap load error:', err);
      }
    }

    // Render Dual Orderbook (Aggregated Depth Ladder + Fine L2 Depth)
    function renderDualOrderbook() {
      if (!lastLiveData) return;
      const coin = currentCoin;
      const livePx = lastLiveData.price || 0.0;
      const dualObCoin = document.getElementById('dualObCoin');
      if (dualObCoin) dualObCoin.textContent = `${coin}/USD`;

      const coarse = lastLiveData.coarse_orderbook || { bids: [], asks: [] };
      const l2 = lastLiveData.l2_book || { bids: [], asks: [] };

      // 1. Render Coarse Left
      const cAsks = coarse.asks || [];
      const cBids = coarse.bids || [];
      const maxCVol = Math.max(...cAsks.map(a => a.total_usd), ...cBids.map(b => b.total_usd), 1.0);

      const coarseAsksBody = document.getElementById('coarseAsksBody');
      if (coarseAsksBody) {
        coarseAsksBody.innerHTML = cAsks.map(a => {
          const widthPct = Math.min(100, Math.round((a.total_usd / maxCVol) * 100));
          return `<tr style="background: linear-gradient(to left, rgba(246, 70, 93, 0.20) ${widthPct}%, transparent ${widthPct}%); border-bottom: 1px solid #131d2e;">
            <td class="text-red">$${a.price.toLocaleString(undefined, {minimumFractionDigits: 1, maximumFractionDigits: 1})}</td>
            <td class="text-right">${a.size.toFixed(2)}</td>
            <td class="text-right">$${Math.round(a.total_usd).toLocaleString()}</td>
          </tr>`;
        }).join('');
      }

      const coarseMidRow = document.getElementById('coarseMidRow');
      if (coarseMidRow) {
        coarseMidRow.textContent = `MID PRICE: $${livePx.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}`;
      }

      const coarseBidsBody = document.getElementById('coarseBidsBody');
      if (coarseBidsBody) {
        coarseBidsBody.innerHTML = cBids.map(b => {
          const widthPct = Math.min(100, Math.round((b.total_usd / maxCVol) * 100));
          return `<tr style="background: linear-gradient(to left, rgba(14, 203, 129, 0.20) ${widthPct}%, transparent ${widthPct}%); border-bottom: 1px solid #131d2e;">
            <td class="text-green">$${b.price.toLocaleString(undefined, {minimumFractionDigits: 1, maximumFractionDigits: 1})}</td>
            <td class="text-right">${b.size.toFixed(2)}</td>
            <td class="text-right">$${Math.round(b.total_usd).toLocaleString()}</td>
          </tr>`;
        }).join('');
      }

      const coarseSpreadLabel = document.getElementById('coarseSpreadLabel');
      const bucketSz = coarse.bucket_size || 1.0;
      if (coarseSpreadLabel) coarseSpreadLabel.textContent = `Bucket: $${bucketSz.toFixed(2)}`;

      // 2. Render Fine Right
      const fAsks = (l2.asks || []).slice(0, 15).reverse();
      const fBids = (l2.bids || []).slice(0, 15);
      const maxFVol = Math.max(...fAsks.map(a => a.total_usd), ...fBids.map(b => b.total_usd), 1.0);

      const fineAsksBody = document.getElementById('fineAsksBody');
      if (fineAsksBody) {
        fineAsksBody.innerHTML = fAsks.map(a => {
          const widthPct = Math.min(100, Math.round((a.total_usd / maxFVol) * 100));
          return `<tr style="background: linear-gradient(to left, rgba(246, 70, 93, 0.20) ${widthPct}%, transparent ${widthPct}%); border-bottom: 1px solid #131d2e;">
            <td class="text-red">$${a.price.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}</td>
            <td class="text-right">${a.size.toFixed(3)}</td>
            <td class="text-right">$${Math.round(a.total_usd).toLocaleString()}</td>
          </tr>`;
        }).join('');
      }

      const spread = l2.spread || 0.0;
      const spreadBps = l2.spread_bps || 0.0;
      const fineMidRow = document.getElementById('fineMidRow');
      const fineSpreadLabel = document.getElementById('fineSpreadLabel');
      const spreadStr = `SPREAD: $${spread.toFixed(2)} (${spreadBps.toFixed(3)}%)`;
      if (fineMidRow) fineMidRow.textContent = spreadStr;
      if (fineSpreadLabel) fineSpreadLabel.textContent = spreadStr;

      const fineBidsBody = document.getElementById('fineBidsBody');
      if (fineBidsBody) {
        fineBidsBody.innerHTML = fBids.map(b => {
          const widthPct = Math.min(100, Math.round((b.total_usd / maxFVol) * 100));
          return `<tr style="background: linear-gradient(to left, rgba(14, 203, 129, 0.20) ${widthPct}%, transparent ${widthPct}%); border-bottom: 1px solid #131d2e;">
            <td class="text-green">$${b.price.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}</td>
            <td class="text-right">${b.size.toFixed(3)}</td>
            <td class="text-right">$${Math.round(b.total_usd).toLocaleString()}</td>
          </tr>`;
        }).join('');
      }

      const bidPct = l2.bid_pct || 50.0;
      const askPct = l2.ask_pct || 50.0;
      const meterBid = document.getElementById('dualMeterBid');
      const meterAsk = document.getElementById('dualMeterAsk');
      const dualBidPct = document.getElementById('dualBidPct');
      const dualAskPct = document.getElementById('dualAskPct');
      if (meterBid) meterBid.style.width = bidPct + '%';
      if (meterAsk) meterAsk.style.width = askPct + '%';
      if (dualBidPct) dualBidPct.textContent = `B ${bidPct.toFixed(0)}%`;
      if (dualAskPct) dualAskPct.textContent = `${askPct.toFixed(0)}% S`;
    }

    // Canvas Events (Crosshair & Hover Interaction)
    function initCanvasEvents() {
      const canvas = document.getElementById('heatmapCanvas');
      const tooltip = document.getElementById('chartTooltip');
      if (!canvas || !tooltip) return;

      canvas.addEventListener('mousemove', (e) => {
        const rect = canvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;
        const w = rect.width;
        const h = rect.height;

        if (viewMode === 'live') {
          renderCanvas(mouseX, mouseY);
          return;
        }

        if (!chartPayload || !chartPayload.candles || chartPayload.candles.length === 0) return;

        const plotX = viewMode === 'historical' ? 55 : 20;
        const profileW = viewMode === 'chart' ? 180 : 0;
        const axisW = 85;
        const plotW = w - plotX - profileW - axisW;
        const plotY = 15;
        const plotH = h - 45;

        if (mouseY < plotY || mouseY > plotY + plotH || mouseX < plotX || mouseX > plotX + plotW + profileW) {
          tooltip.style.display = 'none';
          hoveredPriceBand = null;
          hoveredCandleIdx = -1;
          renderCanvas();
          return;
        }

        const candles = chartPayload.candles;
        const profile = chartPayload.volume_profile || [];
        const bands = chartPayload.price_bands || [];

        let minPrice = Math.min(...candles.map(c => c.low));
        let maxPrice = Math.max(...candles.map(c => c.high));
        if (bands.length > 0) {
          minPrice = Math.min(minPrice, bands[0].min_px);
          maxPrice = Math.max(maxPrice, bands[bands.length - 1].max_px);
        }
        const pad = (maxPrice - minPrice) * 0.03 || 1.0;
        minPrice -= pad;
        maxPrice += pad;
        const priceRange = maxPrice - minPrice;

        const mousePrice = maxPrice - ((mouseY - plotY) / plotH) * priceRange;

        if (viewMode === 'chart') {
          const matchedBand = profile.find(b => mousePrice >= b.min_px && mousePrice <= b.max_px);
          hoveredPriceBand = matchedBand || null;

          if (matchedBand) {
            tooltip.style.display = 'block';
            let tipX = mouseX + 15;
            if (tipX + 220 > w) tipX = mouseX - 225;
            tooltip.style.left = tipX + 'px';
            tooltip.style.top = Math.max(10, mouseY - 35) + 'px';

            const bandLabel = `$${Math.round(matchedBand.min_px).toLocaleString()} - $${Math.round(matchedBand.max_px).toLocaleString()}`;
            const sideName = matchedBand.side === 'LONG' ? 'Long liquidations' : (matchedBand.side === 'SHORT' ? 'Short liquidations' : (matchedBand.side === 'BUY' ? 'Buy stops' : 'Sell stops'));
            const col = matchedBand.side === 'LONG' ? 'var(--accent-red)' : 'var(--accent-green)';

            tooltip.innerHTML = `
              <div style="font-weight:bold; color:#fff; font-size:11px; margin-bottom:3px;">${bandLabel}</div>
              <div style="color:${col}; font-weight:bold; font-size:11px;">
                ${sideName}: <b>$${formatVol(matchedBand.amount)}</b>
              </div>
            `;
          } else {
            tooltip.style.display = 'none';
          }
          renderCanvas(mouseX, mouseY);

        } else {
          // Historical 2D view
          const N = candles.length;
          const candleW = Math.max(4, plotW / Math.max(1, N));
          const idx = Math.min(N - 1, Math.max(0, Math.floor((mouseX - plotX) / candleW)));
          hoveredCandleIdx = idx;

          const c = candles[idx];
          const gridEntry = (chartPayload.heatmap_grid || [])[idx] || {};
          const levels = gridEntry.levels || {};

          let closestMid = 0;
          let minDist = 1e9;
          let matchedVol = 0;
          for (const [pxStr, vol] of Object.entries(levels)) {
            const px = parseFloat(pxStr);
            const d = Math.abs(px - mousePrice);
            if (d < minDist) {
              minDist = d;
              closestMid = px;
              matchedVol = vol;
            }
          }

          tooltip.style.display = 'block';
          let tipX = mouseX + 15;
          if (tipX + 220 > w) tipX = mouseX - 225;
          tooltip.style.left = tipX + 'px';
          tooltip.style.top = Math.max(10, mouseY - 40) + 'px';

          const modeTag = currentMasterTab === 'stops' ? 'Stops Volume' : (mousePrice < c.close ? 'Long Liquidations' : 'Short Liquidations');
          const col = currentMasterTab === 'stops' ? 'var(--accent-magenta)' : 'var(--accent-yellow)';

          tooltip.innerHTML = `
            <div style="font-weight:bold; color:var(--accent-cyan); margin-bottom:4px; font-size:11px;">${c.datetime} UTC</div>
            <div style="color:var(--text-dim); margin-bottom:4px; font-size:10px;">
              O: <span class="text-green">${c.open.toLocaleString()}</span>
              H: <span class="text-green">${c.high.toLocaleString()}</span>
              L: <span class="text-red">${c.low.toLocaleString()}</span>
              C: <b>${c.close.toLocaleString()}</b>
            </div>
            <div style="border-top:1px solid #334155; padding-top:4px; font-size:11px;">
              <span style="color:#cbd5e1;">Band Level:</span> <b>$${mousePrice.toLocaleString(undefined, {minimumFractionDigits: 1, maximumFractionDigits: 1})}</b><br/>
              <span style="color:${col}; font-weight:bold;">${modeTag}:</span> <b>$${formatVol(matchedVol)}</b>
            </div>
          `;
          renderCanvas(mouseX, mouseY);
        }
      });

      canvas.addEventListener('mouseleave', () => {
        tooltip.style.display = 'none';
        hoveredPriceBand = null;
        hoveredCandleIdx = -1;
        renderCanvas();
      });

      window.addEventListener('resize', () => {
        renderCanvas();
      });
    }

    // Live Mode Two-Sided Distribution Canvas Renderer (Exact Hyperdash.com Parity)
    function renderLiveCanvas(ctx, w, h, mouseX, mouseY) {
      const isStops = currentMasterTab === 'stops';
      const source = isStops ? (lastLiveData && lastLiveData.stops) : (lastLiveData && lastLiveData.liquidations);
      const bands = (source && source.bands) ? source.bands : [];
      const livePx = (lastLiveData && lastLiveData.price) || prevPrice || 100.0;
      const isCoin = currentDenom === 'coin';

      ctx.fillStyle = '#060911';
      ctx.fillRect(0, 0, w, h);

      if (!bands || bands.length === 0) {
        ctx.fillStyle = 'var(--text-dim)';
        ctx.font = '12px JetBrains Mono, monospace';
        ctx.textAlign = 'center';
        ctx.fillText('Synchronizing real-time live distribution data...', w / 2, h / 2);
        return;
      }

      const plotX = 65;
      const axisRightW = 75;
      const plotW = w - plotX - axisRightW;
      const plotY = 30;
      const plotH = h - 65;

      let minPx = bands[0].min_px;
      let maxPx = bands[bands.length - 1].max_px;
      if (minPx >= maxPx) { minPx = livePx * 0.5; maxPx = livePx * 1.5; }
      const pxSpan = maxPx - minPx;

      function pToX(p) { return plotX + ((p - minPx) / pxSpan) * plotW; }
      function xToP(x) { return minPx + ((x - plotX) / plotW) * pxSpan; }

      const maxBar = Math.max(...bands.map(b => (isCoin ? (b.amount_coin || 0) : (b.amount_usd || b.amount || 0))), 1.0);
      const maxCum = Math.max(...bands.map(b => (isCoin ? (b.cum_amount_coin || 0) : (b.cum_amount_usd || b.cum_amount || 0))), 1.0);

      const chkLong = document.getElementById('chkLongLiq')?.checked ?? true;
      const chkShort = document.getElementById('chkShortLiq')?.checked ?? true;
      const chkCumLong = document.getElementById('chkCumLong')?.checked ?? true;
      const chkCumShort = document.getElementById('chkCumShort')?.checked ?? true;

      const chkBuyStops = document.getElementById('chkBuyStops')?.checked ?? true;
      const chkSellStops = document.getElementById('chkSellStops')?.checked ?? true;
      const chkCumBuys = document.getElementById('chkCumBuys')?.checked ?? true;
      const chkCumSells = document.getElementById('chkCumSells')?.checked ?? true;

      // Grid Lines & Y-Axes
      ctx.lineWidth = 0.5;
      ctx.strokeStyle = '#141d2d';
      ctx.fillStyle = '#64748b';
      ctx.font = '10px JetBrains Mono, monospace';

      const steps = 5;
      for (let s = 0; s <= steps; s++) {
        const y = plotY + (plotH / steps) * s;
        ctx.beginPath();
        ctx.moveTo(plotX, y);
        ctx.lineTo(plotX + plotW, y);
        ctx.stroke();

        const barVal = maxBar * (1 - s / steps);
        ctx.textAlign = 'right';
        ctx.fillStyle = '#94a3b8';
        const leftTxt = isCoin ? `${formatVol(barVal)}` : `$${formatVol(barVal)}`;
        ctx.fillText(leftTxt, plotX - 8, y + 3);

        const cumVal = maxCum * (1 - s / steps);
        ctx.textAlign = 'left';
        ctx.fillStyle = isStops ? '#38bdf8' : '#34d399';
        const rightTxt = isCoin ? `${formatVol(cumVal)}` : `$${formatVol(cumVal)}`;
        ctx.fillText(rightTxt, plotX + plotW + 8, y + 3);
      }

      // X-Axis Price Steps
      ctx.textAlign = 'center';
      ctx.fillStyle = '#64748b';
      const xSteps = 8;
      for (let s = 0; s <= xSteps; s++) {
        const p = minPx + (pxSpan / xSteps) * s;
        const x = pToX(p);
        ctx.beginPath();
        ctx.moveTo(x, plotY + plotH);
        ctx.lineTo(x, plotY + plotH + 5);
        ctx.strokeStyle = '#334155';
        ctx.stroke();
        ctx.fillText('$' + Math.round(p).toLocaleString(), x, plotY + plotH + 18);
      }

      // Find Hovered Band
      let hovered = null;
      if (mouseX && mouseY && mouseX >= plotX && mouseX <= plotX + plotW && mouseY >= plotY && mouseY <= plotY + plotH) {
        const mPx = xToP(mouseX);
        let minD = 1e9;
        for (const b of bands) {
          const d = Math.abs(b.mid_px - mPx);
          if (d < minD) { minD = d; hovered = b; }
        }
      }

      // Draw Histogram Bars
      for (let i = 0; i < bands.length; i++) {
        const b = bands[i];
        const val = isCoin ? (b.amount_coin || 0) : (b.amount_usd || b.amount || 0);
        if (val <= 0) continue;

        const x1 = pToX(b.min_px);
        const x2 = pToX(b.max_px);
        const barW = Math.max(1.5, x2 - x1 - 0.5);
        const barH = (val / maxBar) * (plotH - 10);
        const barY = plotY + plotH - barH;

        let fillCol = '#64748b';
        let shouldDraw = true;

        if (!isStops) {
          if (b.mid_px < livePx) {
            fillCol = '#f43f5e';
            shouldDraw = chkLong;
          } else {
            fillCol = '#10b981';
            shouldDraw = chkShort;
          }
        } else {
          if (b.mid_px < livePx) {
            fillCol = '#eab308';
            shouldDraw = chkSellStops;
          } else {
            fillCol = '#38bdf8';
            shouldDraw = chkBuyStops;
          }
        }

        if (shouldDraw) {
          ctx.fillStyle = fillCol;
          ctx.fillRect(x1, barY, barW, barH);

          if (hovered && hovered.mid_px === b.mid_px) {
            ctx.strokeStyle = '#ffffff';
            ctx.lineWidth = 1.5;
            ctx.strokeRect(x1 - 1, barY - 1, barW + 2, barH + 2);
          }
        }
      }

      // Draw Cumulative Curves
      if (!isStops) {
        if (chkCumLong) {
          const longBands = bands.filter(b => b.mid_px < livePx);
          if (longBands.length > 0) {
            ctx.beginPath();
            ctx.strokeStyle = '#fb7185';
            ctx.lineWidth = 2.0;
            for (let i = 0; i < longBands.length; i++) {
              const b = longBands[i];
              const cum = isCoin ? (b.cum_amount_coin || 0) : (b.cum_amount_usd || b.cum_amount || 0);
              const x = pToX(b.mid_px);
              const y = plotY + plotH - (cum / maxCum) * (plotH - 10);
              if (i === 0) ctx.moveTo(x, y);
              else ctx.lineTo(x, y);
            }
            ctx.stroke();
          }
        }

        if (chkCumShort) {
          const shortBands = bands.filter(b => b.mid_px >= livePx);
          if (shortBands.length > 0) {
            ctx.beginPath();
            ctx.strokeStyle = '#34d399';
            ctx.lineWidth = 2.0;
            for (let i = 0; i < shortBands.length; i++) {
              const b = shortBands[i];
              const cum = isCoin ? (b.cum_amount_coin || 0) : (b.cum_amount_usd || b.cum_amount || 0);
              const x = pToX(b.mid_px);
              const y = plotY + plotH - (cum / maxCum) * (plotH - 10);
              if (i === 0) ctx.moveTo(x, y);
              else ctx.lineTo(x, y);
            }
            ctx.stroke();
          }
        }
      } else {
        if (chkCumSells) {
          const sellBands = bands.filter(b => b.mid_px < livePx);
          if (sellBands.length > 0) {
            ctx.beginPath();
            ctx.strokeStyle = '#ca8a04';
            ctx.lineWidth = 2.0;
            for (let i = 0; i < sellBands.length; i++) {
              const b = sellBands[i];
              const cum = isCoin ? (b.cum_amount_coin || 0) : (b.cum_amount_usd || b.cum_amount || 0);
              const x = pToX(b.mid_px);
              const y = plotY + plotH - (cum / maxCum) * (plotH - 10);
              if (i === 0) ctx.moveTo(x, y);
              else ctx.lineTo(x, y);
            }
            ctx.stroke();
          }
        }

        if (chkCumBuys) {
          const buyBands = bands.filter(b => b.mid_px >= livePx);
          if (buyBands.length > 0) {
            ctx.beginPath();
            ctx.strokeStyle = '#0284c7';
            ctx.lineWidth = 2.0;
            for (let i = 0; i < buyBands.length; i++) {
              const b = buyBands[i];
              const cum = isCoin ? (b.cum_amount_coin || 0) : (b.cum_amount_usd || b.cum_amount || 0);
              const x = pToX(b.mid_px);
              const y = plotY + plotH - (cum / maxCum) * (plotH - 10);
              if (i === 0) ctx.moveTo(x, y);
              else ctx.lineTo(x, y);
            }
            ctx.stroke();
          }
        }
      }

      // Current Price Vertical Line & Badge
      const currX = pToX(livePx);
      if (currX >= plotX && currX <= plotX + plotW) {
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 1.2;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(currX, plotY);
        ctx.lineTo(currX, plotY + plotH);
        ctx.stroke();
        ctx.setLineDash([]);

        const badgeW = 95;
        const badgeH = 18;
        const badgeX = Math.max(plotX, Math.min(plotX + plotW - badgeW, currX - badgeW / 2));
        const badgeY = plotY - 20;

        ctx.fillStyle = '#10b981';
        ctx.fillRect(badgeX, badgeY, badgeW, badgeH);
        ctx.fillStyle = '#000000';
        ctx.font = 'bold 10px JetBrains Mono, monospace';
        ctx.textAlign = 'center';
        ctx.fillText(`Current: $${livePx.toFixed(2)}`, badgeX + badgeW / 2, badgeY + 13);
      }

      // Hover Tooltip
      const tooltip = document.getElementById('chartTooltip');
      if (hovered && tooltip) {
        const hoverX = pToX(hovered.mid_px);
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
        ctx.lineWidth = 1.0;
        ctx.setLineDash([2, 2]);
        ctx.beginPath();
        ctx.moveTo(hoverX, plotY);
        ctx.lineTo(hoverX, plotY + plotH);
        ctx.stroke();
        ctx.setLineDash([]);

        tooltip.style.display = 'block';
        let tipX = hoverX + 15;
        if (tipX + 220 > w) tipX = hoverX - 225;
        tooltip.style.left = tipX + 'px';
        tooltip.style.top = Math.max(10, (mouseY || plotY) - 30) + 'px';

        const val = isCoin ? (hovered.amount_coin || 0) : (hovered.amount_usd || hovered.amount || 0);
        const cum = isCoin ? (hovered.cum_amount_coin || 0) : (hovered.cum_amount_usd || hovered.cum_amount || 0);
        const unitSym = isCoin ? ` ${currentCoin}` : '';
        const prefix = isCoin ? '' : '$';

        let typeStr = '';
        let col = '#fff';
        if (!isStops) {
          const isSqueeze = hovered.mid_px >= livePx;
          typeStr = isSqueeze ? 'Short Liquidations' : 'Long Liquidations';
          col = isSqueeze ? '#10b981' : '#f43f5e';
        } else {
          const isBuy = hovered.mid_px >= livePx;
          typeStr = isBuy ? 'Buy Stops' : 'Sell Stops';
          col = isBuy ? '#38bdf8' : '#eab308';
        }

        tooltip.innerHTML = `
          <div style="font-weight:bold; color:#fff; font-size:11px; margin-bottom:4px;">
            $${hovered.mid_px.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}
            <span style="color:var(--text-dim); font-size:10px;">($${hovered.min_px.toFixed(1)} - $${hovered.max_px.toFixed(1)})</span>
          </div>
          <div style="color:${col}; font-weight:bold; font-size:11px; margin-bottom:2px;">
            ${typeStr}: <b>${prefix}${formatVol(val)}${unitSym}</b>
          </div>
          <div style="color:var(--accent-cyan); font-size:10px; margin-bottom:2px;">
            Cumulative: <b>${prefix}${formatVol(cum)}${unitSym}</b>
          </div>
          <div style="color:var(--text-dim); font-size:9px;">
            Distance: <b>${(hovered.dist_pct >= 0 ? '+' : '')}${hovered.dist_pct.toFixed(2)}%</b> from mid
          </div>
        `;
      } else if (tooltip && viewMode === 'live') {
        tooltip.style.display = 'none';
      }
    }

    // Canvas Master Renderer
    function renderCanvas(crossX, crossY) {
      const canvas = document.getElementById('heatmapCanvas');
      if (!canvas) return;
      const rect = canvas.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      canvas.width = rect.width * dpr;
      canvas.height = 420 * dpr;
      const ctx = canvas.getContext('2d');
      ctx.scale(dpr, dpr);

      const w = rect.width;
      const h = 420;

      if (viewMode === 'live') {
        renderLiveCanvas(ctx, w, h, crossX, crossY);
        return;
      }

      const isChart = viewMode === 'chart';
      const plotX = isChart ? 20 : 55;
      const profileW = isChart ? 180 : 0;
      const axisW = 85;
      const plotW = w - plotX - profileW - axisW;
      const plotY = 15;
      const plotH = h - 45;

      ctx.fillStyle = '#060911';
      ctx.fillRect(0, 0, w, h);

      if (!chartPayload || !chartPayload.candles || chartPayload.candles.length === 0) {
        ctx.fillStyle = 'var(--text-dim)';
        ctx.font = '12px JetBrains Mono, monospace';
        ctx.textAlign = 'center';
        ctx.fillText(chartPayload?.reason || 'Synchronizing market telemetry...', w / 2, h / 2);
        return;
      }

      const candles = chartPayload.candles;
      const bands = chartPayload.price_bands || [];
      const grid = chartPayload.heatmap_grid || [];
      const profile = chartPayload.volume_profile || [];
      const maxIntensity = chartPayload.max_intensity_usd || 1.0;
      const maxProfUsd = chartPayload.max_profile_usd || 1.0;

      let minPrice = Math.min(...candles.map(c => c.low));
      let maxPrice = Math.max(...candles.map(c => c.high));
      if (bands.length > 0) {
        minPrice = Math.min(minPrice, bands[0].min_px);
        maxPrice = Math.max(maxPrice, bands[bands.length - 1].max_px);
      }
      const pad = (maxPrice - minPrice) * 0.03 || 1.0;
      minPrice -= pad;
      maxPrice += pad;
      const priceRange = maxPrice - minPrice;

      function priceToY(p) { return plotY + plotH - ((p - minPrice) / priceRange) * plotH; }
      function roundMid(m) { return Math.round(m * 100) / 100; }

      const N = candles.length;
      const candleW = Math.max(4, plotW / Math.max(1, N));

      // Historical 2D Scale & Tiles
      if (!isChart) {
        const legendX = 14;
        const legendY = plotY;
        const legendW = 10;
        const legendH = plotH;

        const grad = ctx.createLinearGradient(0, legendY + legendH, 0, legendY);
        if (currentMasterTab === 'liquidations') {
          grad.addColorStop(0, 'rgba(40, 15, 60, 0.4)');
          grad.addColorStop(0.5, 'rgba(230, 92, 0, 0.85)');
          grad.addColorStop(1, 'rgba(255, 215, 0, 1)');
        } else {
          grad.addColorStop(0, 'rgba(30, 10, 50, 0.4)');
          grad.addColorStop(0.5, 'rgba(160, 32, 240, 0.85)');
          grad.addColorStop(1, 'rgba(255, 0, 128, 1)');
        }
        ctx.fillStyle = grad;
        ctx.fillRect(legendX, legendY, legendW, legendH);

        ctx.strokeStyle = '#334155';
        ctx.lineWidth = 1;
        ctx.strokeRect(legendX, legendY, legendW, legendH);

        ctx.fillStyle = 'var(--text-dim)';
        ctx.font = '8px JetBrains Mono, monospace';
        ctx.textAlign = 'right';
        ctx.fillText('$' + formatVol(maxIntensity), legendX - 3, legendY + 9);
        ctx.fillText('$0', legendX - 3, legendY + legendH);

        for (let i = 0; i < N; i++) {
          const x = plotX + i * candleW;
          const entry = grid[i] || {};
          const levels = entry.levels || {};

          for (let b = 0; b < bands.length; b++) {
            const band = bands[b];
            const mid = band.mid_px;
            const amt = levels[mid.toFixed(1)] || levels[mid.toFixed(2)] || levels[String(roundMid(mid))] || levels[String(parseInt(mid))] || levels[mid] || 0.0;
            if (amt > 0) {
              const yTop = priceToY(band.max_px);
              const yBot = priceToY(band.min_px);
              const cellH = Math.max(1.5, Math.abs(yBot - yTop));
              const norm = Math.min(1.0, Math.pow(amt / maxIntensity, 0.45));

              if (currentMasterTab === 'liquidations') {
                const r = Math.round(50 + 205 * norm);
                const g = Math.round(15 + 200 * Math.pow(norm, 1.8));
                const bCol = Math.round(70 * (1 - norm));
                ctx.fillStyle = `rgba(${r}, ${g}, ${bCol}, ${0.35 + 0.6 * norm})`;
              } else {
                const r = Math.round(60 + 195 * norm);
                const g = Math.round(15 + 30 * norm);
                const bCol = Math.round(100 + 155 * norm);
                ctx.fillStyle = `rgba(${r}, ${g}, ${bCol}, ${0.35 + 0.6 * norm})`;
              }
              ctx.fillRect(x, Math.min(yTop, yBot), candleW - 0.5, cellH);
            }
          }
        }
      }

      // Chart Mode Right-Side Volume Profile
      if (isChart) {
        const profX = plotX + plotW;
        for (let p = 0; p < profile.length; p++) {
          const band = profile[p];
          const yTop = priceToY(band.max_px);
          const yBot = priceToY(band.min_px);
          const barH = Math.max(2, Math.abs(yBot - yTop));
          const barW = (band.amount / maxProfUsd) * (profileW - 10);
          const barX = profX + profileW - barW;

          let barFill = band.color;
          let barBorder = band.color;
          if (currentMasterTab === 'liquidations') {
            if (band.side === 'SHORT') {
              barFill = 'rgba(0, 255, 136, 0.70)';
              barBorder = '#00ff88';
            } else {
              barFill = 'rgba(255, 51, 102, 0.70)';
              barBorder = '#ff3366';
            }
          } else {
            if (band.side === 'BUY') {
              barFill = 'rgba(0, 240, 255, 0.70)';
              barBorder = '#00f0ff';
            } else {
              barFill = 'rgba(255, 215, 0, 0.70)';
              barBorder = '#ffd700';
            }
          }

          ctx.fillStyle = barFill;
          ctx.fillRect(barX, Math.min(yTop, yBot), barW, barH - 1);
          ctx.strokeStyle = barBorder;
          ctx.lineWidth = 0.5;
          ctx.strokeRect(barX, Math.min(yTop, yBot), barW, barH - 1);
        }
      }

      // Horizontal Grid & Price Axis
      ctx.lineWidth = 0.5;
      ctx.strokeStyle = '#141d2d';
      ctx.fillStyle = '#64748b';
      ctx.font = '10px JetBrains Mono, monospace';
      ctx.textAlign = 'left';

      const priceSteps = 8;
      const totalPlotWidth = plotW + profileW;
      for (let s = 0; s <= priceSteps; s++) {
        const p = minPrice + (priceRange / priceSteps) * s;
        const y = priceToY(p);
        ctx.beginPath();
        ctx.moveTo(plotX, y);
        ctx.lineTo(plotX + totalPlotWidth, y);
        ctx.stroke();

        ctx.fillText('$' + p.toLocaleString(undefined, {maximumFractionDigits: 1}), plotX + totalPlotWidth + 6, y + 3);
      }

      // Time Grid & Labels
      ctx.textAlign = 'center';
      const timeSteps = Math.min(6, N);
      const stepIdx = Math.max(1, Math.floor(N / timeSteps));
      for (let s = 0; s < N; s += stepIdx) {
        const x = plotX + s * candleW + candleW / 2;
        const dt = candles[s].datetime;
        const shortDt = dt ? dt.slice(5, 16) : '';
        ctx.beginPath();
        ctx.moveTo(x, plotY);
        ctx.lineTo(x, plotY + plotH);
        ctx.stroke();

        ctx.fillText(shortDt, x, plotY + plotH + 16);
      }

      // Candlesticks
      for (let i = 0; i < N; i++) {
        const c = candles[i];
        const cx = plotX + i * candleW + candleW / 2;
        const isUp = c.close >= c.open;
        const col = isUp ? '#00ff88' : '#ff3366';

        const yOpen = priceToY(c.open);
        const yClose = priceToY(c.close);
        const yHigh = priceToY(c.high);
        const yLow = priceToY(c.low);

        ctx.strokeStyle = col;
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(cx, yHigh);
        ctx.lineTo(cx, yLow);
        ctx.stroke();

        const bTop = Math.min(yOpen, yClose);
        const bH = Math.max(2, Math.abs(yOpen - yClose));
        const bW = Math.max(3, candleW * 0.72);
        ctx.fillStyle = col;
        ctx.fillRect(cx - bW / 2, bTop, bW, bH);
      }

      // Live Price Line & Right Axis Pill
      const livePriceNow = prevPrice || candles[N - 1].close;
      const currY = priceToY(livePriceNow);
      ctx.strokeStyle = '#00f0ff';
      ctx.lineWidth = 1.2;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(plotX, currY);
      ctx.lineTo(plotX + totalPlotWidth, currY);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#00f0ff';
      ctx.fillRect(plotX + totalPlotWidth + 2, currY - 9, 78, 18);
      ctx.fillStyle = '#000';
      ctx.font = 'bold 10px JetBrains Mono, monospace';
      ctx.textAlign = 'left';
      ctx.fillText('$' + livePriceNow.toFixed(1), plotX + totalPlotWidth + 6, currY + 4);

      // Hover Highlight in Chart Mode
      if (isChart && hoveredPriceBand) {
        const b = hoveredPriceBand;
        const yTop = priceToY(b.max_px);
        const yBot = priceToY(b.min_px);
        const barH = Math.max(2, Math.abs(yBot - yTop));

        ctx.fillStyle = 'rgba(255, 255, 255, 0.08)';
        ctx.fillRect(plotX, Math.min(yTop, yBot), totalPlotWidth, barH);

        const profX = plotX + plotW;
        const barW = (b.amount / maxProfUsd) * (profileW - 10);
        const barX = profX + profileW - barW;
        ctx.fillStyle = 'rgba(255, 255, 255, 0.35)';
        ctx.fillRect(barX, Math.min(yTop, yBot), barW, barH - 1);

        const badgeText = `$${Math.round(b.min_px).toLocaleString()} - $${Math.round(b.max_px).toLocaleString()}`;
        const badgeX = plotX + totalPlotWidth + 2;
        const badgeY = Math.min(yTop, yBot) - 2;
        const badgeW = 92;
        const badgeH = Math.max(18, barH + 4);

        ctx.fillStyle = '#ffffff';
        ctx.fillRect(badgeX, badgeY, badgeW, badgeH);
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 1;
        ctx.strokeRect(badgeX, badgeY, badgeW, badgeH);

        ctx.fillStyle = '#000000';
        ctx.font = 'bold 9px JetBrains Mono, monospace';
        ctx.textAlign = 'center';
        ctx.fillText(badgeText, badgeX + badgeW / 2, badgeY + badgeH / 2 + 3);
      }

      // Crosshair in Historical Mode
      if (!isChart && crossX && crossY && crossX >= plotX && crossX <= plotX + plotW && crossY >= plotY && crossY <= plotY + plotH) {
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.35)';
        ctx.lineWidth = 0.8;
        ctx.setLineDash([2, 2]);

        ctx.beginPath();
        ctx.moveTo(crossX, plotY);
        ctx.lineTo(crossX, plotY + plotH);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(plotX, crossY);
        ctx.lineTo(plotX + plotW, crossY);
        ctx.stroke();
        ctx.setLineDash([]);
      }
    }

    // Real-Time Live Data Poller (Ticks every second)
    async function fetchLiveData() {
      const t0 = performance.now();
      try {
        const res = await fetch('/api/live/' + currentCoin);
        const data = await res.json();
        lastLiveData = data;
        const latency = Math.round(performance.now() - t0);
        const latElem = document.getElementById('latencyLabel');
        if (latElem) latElem.textContent = `Latency: ${latency} ms`;

        // 0. Update Current Candle Orderflow HUD
        const currCandle = data.current_candle || {};
        const price = data.price || 0.0;
        const candleTimeBadge = document.getElementById('candleTimeBadge');
        const hudLongLiq = document.getElementById('hudLongLiq');
        const hudShortLiq = document.getElementById('hudShortLiq');
        const hudPeakLiq = document.getElementById('hudPeakLiq');
        const hudTotalStops = document.getElementById('hudTotalStops');

        if (currCandle && currCandle.datetime) {
          const parts = currCandle.datetime.split(' ');
          const timePart = parts.length > 1 ? parts[1] : currCandle.datetime;
          if (candleTimeBadge) candleTimeBadge.textContent = timePart + ' UTC';
          if (hudLongLiq) hudLongLiq.textContent = '$' + formatVol(currCandle.liq_long_usd || 0);
          if (hudShortLiq) hudShortLiq.textContent = '$' + formatVol(currCandle.liq_short_usd || 0);
          const peakLiqPx = currCandle.liq_peak_price || 0;
          const peakLiqAmt = currCandle.liq_peak_amount || 0;
          if (hudPeakLiq) hudPeakLiq.textContent = peakLiqPx > 0 ? ('$' + peakLiqPx.toLocaleString() + ' ($' + formatVol(peakLiqAmt) + ')') : '--';
          if (hudTotalStops) hudTotalStops.textContent = '$' + formatVol(currCandle.stop_total_usd || 0);
        } else {
          const liqs = data.liquidations || {};
          const stops = data.stops || {};
          const longUsd = (liqs.total_long_size || 0) * (price || 1);
          const shortUsd = (liqs.total_short_size || 0) * (price || 1);
          const totalStopsUsd = ((stops.total_buy_size || 0) + (stops.total_sell_size || 0)) * (price || 1);
          const topBand = (liqs.bands && liqs.bands[0]) ? liqs.bands[0] : null;
          if (candleTimeBadge) candleTimeBadge.textContent = 'LIVE FEED';
          if (hudLongLiq) hudLongLiq.textContent = '$' + formatVol(longUsd);
          if (hudShortLiq) hudShortLiq.textContent = '$' + formatVol(shortUsd);
          if (hudPeakLiq) hudPeakLiq.textContent = topBand ? ('$' + Math.round(topBand.mid_px).toLocaleString() + ' ($' + formatVol(topBand.amount) + ')') : '--';
          if (hudTotalStops) hudTotalStops.textContent = '$' + formatVol(totalStopsUsd);
        }

        // 1. Update Price & Top Header
        const markElem = document.getElementById('markPrice');
        const container = document.getElementById('priceContainer');
        const arrow = document.getElementById('priceArrow');

        if (markElem) markElem.textContent = '$' + price.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});

        if (prevPrice > 0 && price !== prevPrice && container && arrow) {
          if (price > prevPrice) {
            arrow.textContent = '▲';
            arrow.className = 'text-green';
            container.classList.add('price-flash-up');
            setTimeout(() => container.classList.remove('price-flash-up'), 500);
          } else {
            arrow.textContent = '▼';
            arrow.className = 'text-red';
            container.classList.add('price-flash-down');
            setTimeout(() => container.classList.remove('price-flash-down'), 500);
          }
        }
        prevPrice = price;

        if (chartPayload && chartPayload.candles && chartPayload.candles.length > 0) {
          const lastCandle = chartPayload.candles[chartPayload.candles.length - 1];
          lastCandle.close = price;
          if (price > lastCandle.high) lastCandle.high = price;
          if (price < lastCandle.low) lastCandle.low = price;
          const closeElem = document.getElementById('cHdrClose');
          if (closeElem) closeElem.textContent = price.toLocaleString(undefined, {minimumFractionDigits: 1, maximumFractionDigits: 1});
        }

        // Meta stats
        const meta = data.meta || {};
        const chg = meta.change_24h || 0.0;
        const chgPill = document.getElementById('changePill');
        if (chgPill) {
          chgPill.textContent = (chg >= 0 ? '+' : '') + chg.toFixed(2) + '%';
          chgPill.style.background = chg >= 0 ? 'rgba(0,255,136,0.2)' : 'rgba(255,51,102,0.2)';
          chgPill.style.color = chg >= 0 ? 'var(--accent-green)' : 'var(--accent-red)';
        }

        const vol24h = document.getElementById('vol24h');
        const oiUsd = document.getElementById('oiUsd');
        const fundingApr = document.getElementById('fundingApr');
        const maxLev = document.getElementById('maxLev');
        const utcClock = document.getElementById('utcClock');
        if (vol24h) vol24h.textContent = '$' + formatVol(meta.volume_24h || 0);
        if (oiUsd) oiUsd.textContent = '$' + formatVol(meta.open_interest_usd || 0);
        if (fundingApr) fundingApr.textContent = ((meta.funding_annualized || 0) >= 0 ? '+' : '') + (meta.funding_annualized || 0).toFixed(2) + '%';
        if (maxLev) maxLev.textContent = (meta.max_leverage || 50) + 'x';
        if (utcClock) utcClock.textContent = data.utc_time;

        // 2. Render Orderbook L2
        const book = data.l2_book || {};
        const bids = (book.bids || []).slice(0, 10);
        const asks = (book.asks || []).slice(0, 10).reverse();
        const maxVol = Math.max(...bids.map(b => b.total_usd), ...asks.map(a => a.total_usd), 1.0);

        const asksBody = document.getElementById('asksBody');
        if (asksBody) {
          asksBody.innerHTML = asks.map(a => {
            const widthPct = Math.min(100, Math.round((a.total_usd / maxVol) * 100));
            return `<tr style="background: linear-gradient(to left, rgba(246, 70, 93, 0.20) ${widthPct}%, transparent ${widthPct}%); border-bottom: 1px solid #131d2e;">
              <td class="text-red row-text">$${a.price.toLocaleString(undefined, {minimumFractionDigits: 1})}</td>
              <td class="row-text">${a.size.toFixed(3)}</td>
              <td class="row-text">$${Math.round(a.total_usd).toLocaleString()}</td>
            </tr>`;
          }).join('');
        }

        const bidsBody = document.getElementById('bidsBody');
        if (bidsBody) {
          bidsBody.innerHTML = bids.map(b => {
            const widthPct = Math.min(100, Math.round((b.total_usd / maxVol) * 100));
            return `<tr style="background: linear-gradient(to left, rgba(14, 203, 129, 0.20) ${widthPct}%, transparent ${widthPct}%); border-bottom: 1px solid #131d2e;">
              <td class="text-green row-text">$${b.price.toLocaleString(undefined, {minimumFractionDigits: 1})}</td>
              <td class="row-text">${b.size.toFixed(3)}</td>
              <td class="row-text">$${Math.round(b.total_usd).toLocaleString()}</td>
            </tr>`;
          }).join('');
        }

        const spread = book.spread || 0.0;
        const spreadBps = book.spread_bps || 0.0;
        const spreadRow = document.getElementById('spreadRow');
        if (spreadRow) spreadRow.textContent = `─── SPREAD: $${spread.toFixed(2)} (${spreadBps.toFixed(2)} bps) ───`;

        const bidPct = book.bid_pct || 50.0;
        const askPct = book.ask_pct || 50.0;
        const meterBid = document.getElementById('meterBid');
        const meterAsk = document.getElementById('meterAsk');
        const bidVolLabel = document.getElementById('bidVolLabel');
        const askVolLabel = document.getElementById('askVolLabel');
        if (meterBid) meterBid.style.width = bidPct + '%';
        if (meterAsk) meterAsk.style.width = askPct + '%';
        if (bidVolLabel) bidVolLabel.textContent = `Bids: $${((book.bid_volume_usd || 0)/1e3).toFixed(0)}k (${bidPct.toFixed(0)}%)`;
        if (askVolLabel) askVolLabel.textContent = `Asks: $${((book.ask_volume_usd || 0)/1e3).toFixed(0)}k (${askPct.toFixed(0)}%)`;

        const imbElem = document.getElementById('imbalanceBadge');
        if (imbElem) {
          if (bidPct > 56) {
            imbElem.textContent = 'STRONG BUY PRESSURE';
            imbElem.className = 'text-green';
          } else if (askPct > 56) {
            imbElem.textContent = 'STRONG SELL PRESSURE';
            imbElem.className = 'text-red';
          } else {
            imbElem.textContent = 'BALANCED FLOW';
            imbElem.className = 'text-cyan';
          }
        }

        // 3. Render Liquidations Table
        const liqs = data.liquidations || {};
        const longLiqTotal = document.getElementById('longLiqTotal');
        const shortLiqTotal = document.getElementById('shortLiqTotal');
        if (longLiqTotal) longLiqTotal.textContent = `Long Risk: ${(liqs.total_long_size || 0).toLocaleString()} ${currentCoin}`;
        if (shortLiqTotal) shortLiqTotal.textContent = `Short Risk: ${(liqs.total_short_size || 0).toLocaleString()} ${currentCoin}`;

        const liqBands = liqs.bands || [];
        const maxLiq = Math.max(...liqBands.map(b => b.amount || 0), 1.0);
        const liqBody = document.getElementById('liqBody');
        if (liqBody) {
          liqBody.innerHTML = liqBands.slice(0, 30).map(b => {
            const isSqueeze = b.type === 'SHORT SQUEEZE';
            const colClass = isSqueeze ? 'text-red' : 'text-green';
            const bgRgba = isSqueeze ? 'rgba(246, 70, 93, 0.15)' : 'rgba(14, 203, 129, 0.15)';
            const widthPct = Math.min(100, Math.round(((b.amount || 0) / maxLiq) * 100));
            return `<tr style="background: linear-gradient(to left, ${bgRgba} ${widthPct}%, transparent ${widthPct}%); border-bottom:1px solid #131d2e;">
              <td style="text-align:left;">$${Math.round(b.min_px).toLocaleString()} - $${Math.round(b.max_px).toLocaleString()}</td>
              <td class="${colClass}">${(b.dist_pct >= 0 ? '+' : '') + b.dist_pct.toFixed(1)}%</td>
              <td style="text-align:center;"><span class="badge-tag ${colClass}" style="background:rgba(255,255,255,0.05);">${b.type}</span></td>
              <td style="font-weight:bold;">$${Math.round(b.amount).toLocaleString()}</td>
            </tr>`;
          }).join('');
        }

        // 4. Render Stops Table
        const stops = data.stops || {};
        const stopBands = stops.bands || [];
        const maxStop = Math.max(...stopBands.map(s => s.amount || 0), 1.0);
        const stopsBody = document.getElementById('stopsBody');
        if (stopsBody) {
          stopsBody.innerHTML = stopBands.slice(0, 30).map(s => {
            const isBuy = s.side === 'BUY STOPS';
            const colClass = isBuy ? 'text-cyan' : 'text-yellow';
            const bgRgba = isBuy ? 'rgba(0, 243, 255, 0.15)' : 'rgba(255, 215, 0, 0.15)';
            const widthPct = Math.min(100, Math.round(((s.amount || 0) / maxStop) * 100));
            return `<tr style="background: linear-gradient(to left, ${bgRgba} ${widthPct}%, transparent ${widthPct}%); border-bottom:1px solid #131d2e;">
              <td style="text-align:left;">$${Math.round(s.min_px).toLocaleString()} - $${Math.round(s.max_px).toLocaleString()}</td>
              <td class="${colClass}">${(s.dist_pct >= 0 ? '+' : '') + s.dist_pct.toFixed(1)}%</td>
              <td style="text-align:center;"><span class="badge-tag ${colClass}" style="background:rgba(255,255,255,0.05);">${s.side}</span></td>
              <td style="font-weight:bold;">$${Math.round(s.amount).toLocaleString()}</td>
            </tr>`;
          }).join('');
        }

        // 5. Render Whale L3 Orders Table
        const whales = data.l3_orders || [];
        const whalesBody = document.getElementById('whalesBody');
        if (whalesBody) {
          whalesBody.innerHTML = whales.map(w => {
            const shortAddr = w.address ? (w.address.slice(0, 6) + '...' + w.address.slice(-4)) : 'Anonymous';
            const sideClass = w.side === 'BUY' ? 'text-green' : 'text-red';
            return `<tr style="border-bottom:1px solid #131d2e;">
              <td style="text-align:left; font-family:monospace;"><span style="color:var(--accent-cyan);">${shortAddr}</span></td>
              <td class="${sideClass}" style="font-weight:bold;">${w.side}</td>
              <td>$${w.price.toLocaleString(undefined, {minimumFractionDigits: 1})}</td>
              <td style="font-weight:bold;">$${Math.round(w.notional_usd).toLocaleString()}</td>
            </tr>`;
          }).join('');
        }

        // 6. Render Trades Tape
        const trades = data.recent_trades || [];
        const tradesBody = document.getElementById('tradesBody');
        if (tradesBody) {
          tradesBody.innerHTML = trades.map(t => {
            const d = new Date(t.time);
            const timeStr = d.toTimeString().split(' ')[0] + '.' + String(d.getMilliseconds()).padStart(3, '0');
            const sideClass = t.side === 'BUY' ? 'text-green' : 'text-red';
            const alertPill = t.is_whale ? '<span class="badge-tag text-yellow" style="background:rgba(255,215,0,0.2);">🐋 WHALE</span>' : '';
            return `<tr>
              <td style="color:var(--text-dim);">${timeStr}</td>
              <td class="${sideClass}" style="font-weight:bold;">${t.side}</td>
              <td class="${sideClass}">$${t.price.toLocaleString(undefined, {minimumFractionDigits: 1})}</td>
              <td>${t.size.toFixed(3)}</td>
              <td style="text-align:center;">${alertPill}</td>
            </tr>`;
          }).join('');
        }

        // 7. Update Persistent Cohorts Dock
        const cohort = data.cohort_summary || {};
        if (cohort && cohort.coin) {
          const assetTitle = document.getElementById('cohortAssetTitle');
          if (assetTitle) assetTitle.textContent = `${cohort.coin} Observed liquidation cohort`;
          const notionalTxt = document.getElementById('cohortNotionalTxt');
          if (notionalTxt) notionalTxt.textContent = `$${formatVol(cohort.notional_usd || 0)}`;
          const tradersTxt = document.getElementById('cohortTradersTxt');
          if (tradersTxt) tradersTxt.textContent = (cohort.total_traders || 0).toLocaleString();
          const pnlTxt = document.getElementById('cohortPnlTxt');
          if (pnlTxt) pnlTxt.textContent = cohort.profit_traders_pct == null ? 'PnL coverage unavailable' : `${cohort.profit_traders_pct.toFixed(0)}% Profit / ${cohort.loss_traders_pct.toFixed(0)}% Loss`;

          const nLongBar = document.getElementById('cohortNotionalLongBar');
          const nShortBar = document.getElementById('cohortNotionalShortBar');
          if (nLongBar) nLongBar.style.width = '50%';
          if (nShortBar) nShortBar.style.width = '50%';

          const tLongBar = document.getElementById('cohortTradersLongBar');
          const tShortBar = document.getElementById('cohortTradersShortBar');
          const tLongTxt = document.getElementById('cohortTradersLongTxt');
          const tShortTxt = document.getElementById('cohortTradersShortTxt');
          const lPct = cohort.long_traders_pct ?? 0;
          const sPct = cohort.short_traders_pct ?? 0;
          if (tLongBar) tLongBar.style.width = lPct + '%';
          if (tShortBar) tShortBar.style.width = sPct + '%';
          if (tLongTxt) tLongTxt.textContent = cohort.long_traders_pct == null ? 'Unknown' : `${lPct}% Long`;
          if (tShortTxt) tShortTxt.textContent = cohort.short_traders_pct == null ? 'Unknown' : `${sPct}% Short`;

          const pProfitBar = document.getElementById('cohortPnlProfitBar');
          const pLossBar = document.getElementById('cohortPnlLossBar');
          const pProfitTxt = document.getElementById('cohortPnlProfitTxt');
          const pLossTxt = document.getElementById('cohortPnlLossTxt');
          const pPct = cohort.profit_traders_pct ?? 0;
          const lossPct = cohort.loss_traders_pct ?? 0;
          if (pProfitBar) pProfitBar.style.width = pPct + '%';
          if (pLossBar) pLossBar.style.width = lossPct + '%';
          if (pProfitTxt) pProfitTxt.textContent = cohort.profit_traders_pct == null ? 'Unknown' : `${pPct}% Profit`;
          if (pLossTxt) pLossTxt.textContent = cohort.loss_traders_pct == null ? 'Unknown' : `${lossPct}% Loss`;
        }

        // Active View Refresh
        if (currentMasterTab === 'orderbook') {
          renderDualOrderbook();
        } else if (viewMode === 'live') {
          renderCanvas();
        }

      } catch (err) {
        console.error('Live fetch error:', err);
      }
    }

    async function init() {
      await loadUniverse();
      initCanvasEvents();
      await loadHeatmapData();
      await fetchLiveData();

      // Tick live orderbook & trades tape every single second
      setInterval(fetchLiveData, 1000);

      // Refresh 2D orderflow heatmap matrix every 8 seconds
      setInterval(loadHeatmapData, 8000);

      // Real-time clock
      setInterval(() => {
        const now = new Date();
        const utcStr = now.toISOString().split('T')[1].split('.')[0] + ' UTC';
        const clk = document.getElementById('utcClock');
        if (clk) clk.textContent = utcStr;
      }, 500);
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', init);
    } else {
      init();
    }
  </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def index_page():
    return HTML_TEMPLATE

def start_terminal_server(port: int = 8095):
    print(f"\n[bold bright_green]>>> Starting Hyperdash Chrome Interactive Terminal on http://localhost:{port} <<<[/bold bright_green]")
    uvicorn.run(app, host="127.0.0.1", port=port, log_level="warning")

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8095
    start_terminal_server(port=port)
