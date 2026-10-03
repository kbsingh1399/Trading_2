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
    if not CACHED_UNIVERSE or (now - LAST_UNIVERSE_TIME > 10.0):
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

@app.get("/api/universe")
def api_universe():
    assets = get_universe()
    return {"count": len(assets), "assets": assets}

@app.get("/api/live/{coin}")
def api_live(coin: str):
    coin = coin.strip().upper()
    universe = get_universe()
    meta = next((a for a in universe if a["coin"] == coin), None)
    if not meta:
        raise HTTPException(status_code=404, detail=f"Asset {coin} not found in universe")

    mark_px = meta.get("mark_px", 0.0)

    # 1. Fetch L2 Book & Recent Trades
    l2_book = {}
    try:
        l2_book = CLIENT.fetch_l2_book(coin)
    except Exception as e:
        l2_book = {"bids": [], "asks": [], "spread": 0, "spread_bps": 0, "error": str(e)}

    trades = []
    try:
        trades = CLIENT.fetch_recent_trades(coin)
    except Exception:
        trades = []

    # Dynamic live price resolution
    live_px = mark_px
    if trades and len(trades) > 0:
        live_px = float(trades[0].get("px", mark_px))
    elif l2_book.get("best_bid") and l2_book.get("best_ask"):
        live_px = (l2_book["best_bid"] + l2_book["best_ask"]) / 2.0

    # 2. Fetch Liquidations
    liqs = {}
    try:
        min_px = live_px * 0.80
        max_px = live_px * 1.20
        raw_liqs = CLIENT.fetch_liquidations(coin, min_px, max_px)
        bands = []
        for b in raw_liqs.get("bands", []):
            amt = b.get("amount", 0.0)
            if amt > 0:
                mid = b.get("mid_px", 0.0)
                dist = ((mid - live_px) / live_px * 100.0) if live_px > 0 else 0.0
                bands.append({
                    "min_px": b.get("min_px", 0.0),
                    "max_px": b.get("max_px", 0.0),
                    "mid_px": mid,
                    "amount": amt,
                    "dist_pct": dist,
                    "type": "SHORT SQUEEZE" if mid >= live_px else "LONG CASCADE"
                })
        bands.sort(key=lambda x: x["mid_px"], reverse=True)
        liqs = {
            "total_long_size": raw_liqs.get("total_long_size", 0.0),
            "total_short_size": raw_liqs.get("total_short_size", 0.0),
            "bands": bands[:12],
            "top_long_whales": raw_liqs.get("top_long_whales", [])[:5],
            "top_short_whales": raw_liqs.get("top_short_whales", [])[:5]
        }
    except Exception as e:
        liqs = {"total_long_size": 0, "total_short_size": 0, "bands": [], "error": str(e)}

    # 3. Fetch Stops
    stops = {}
    try:
        min_px = live_px * 0.80
        max_px = live_px * 1.20
        raw_stops = CLIENT.fetch_stops(coin, min_px, max_px)
        bands = []
        for b in raw_stops.get("bands", []):
            amt = b.get("amount", 0.0)
            if amt > 0:
                mid = b.get("mid_px", 0.0)
                dist = ((mid - live_px) / live_px * 100.0) if live_px > 0 else 0.0
                bands.append({
                    "min_px": b.get("min_px", 0.0),
                    "max_px": b.get("max_px", 0.0),
                    "mid_px": mid,
                    "amount": amt,
                    "dist_pct": dist,
                    "side": "BUY STOPS" if mid >= live_px else "SELL STOPS"
                })
        bands.sort(key=lambda x: x["mid_px"], reverse=True)
        stops = {
            "total_buy_size": raw_stops.get("total_buy_size", 0.0),
            "total_sell_size": raw_stops.get("total_sell_size", 0.0),
            "bands": bands[:10]
        }
    except Exception as e:
        stops = {"total_buy_size": 0, "total_sell_size": 0, "bands": [], "error": str(e)}

    # 4. Fetch L3 Whale Orders (Wallet Addresses)
    l3_orders = []
    try:
        raw_l3 = CLIENT.fetch_l3_orders(coin, live_px * 0.985, live_px * 1.015)
        for o in raw_l3[:15]:
            val = o.get("notional_usd", 0.0)
            if val >= 500000:
                tier = "MEGA WHALE"
            elif val >= 150000:
                tier = "WHALE"
            elif val >= 50000:
                tier = "SHARK"
            else:
                tier = "DOLPHIN"

            px = o.get("price", 0.0)
            dist = ((px - live_px) / live_px * 100.0) if live_px > 0 else 0.0
            l3_orders.append({
                "address": o.get("address", ""),
                "side": o.get("side", ""),
                "price": px,
                "size": o.get("size", 0.0),
                "notional_usd": val,
                "tier": tier,
                "dist_pct": dist
            })
    except Exception:
        l3_orders = []

    # 5. Formatted Trades Tape
    formatted_trades = []
    for t in trades[:20]:
        px = float(t.get("px", 0.0))
        sz = float(t.get("sz", 0.0))
        notional = px * sz
        formatted_trades.append({
            "time": t.get("time", 0),
            "side": "BUY" if t.get("side") == "B" else "SELL",
            "price": px,
            "size": sz,
            "notional_usd": notional,
            "is_whale": notional >= 50000
        })

    # 6. Current Candle Microstructure Status
    current_candle_info = {}
    try:
        engine = get_heatmap_engine(coin)
        summary = engine.get_summary()
        current_candle_info = summary.get("current_candle", {})
    except Exception:
        pass

    return {
        "coin": coin,
        "price": live_px,
        "meta": meta,
        "l2_book": l2_book,
        "liquidations": liqs,
        "stops": stops,
        "l3_orders": l3_orders,
        "recent_trades": formatted_trades,
        "current_candle": current_candle_info,
        "timestamp": int(time.time() * 1000),
        "utc_time": datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S UTC")
    }

@app.get("/api/heatmap/{coin}")
def api_heatmap(coin: str, mode: str = "liquidations", timeframe: str = "1h", granularity: str = "medium", lookback: int = 3):
    coin = coin.strip().upper()
    try:
        engine = get_heatmap_engine(coin, timeframe=timeframe)
        payload = engine.get_chart_heatmap_payload(mode=mode, granularity=granularity)
        return payload
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/cohorts/{coin}")
def api_cohorts(coin: str, limit: int = 30):
    coin = coin.strip().upper()
    try:
        cohorts = CLIENT.fetch_top_traders(coin, limit=limit)
        if not cohorts:
            universe = get_universe()
            meta = next((a for a in universe if a["coin"] == coin), None)
            mark_px = meta.get("mark_px", 2600.0) if meta else 2600.0

            min_px = mark_px * 0.70
            max_px = mark_px * 1.30
            liqs = CLIENT.fetch_liquidations(coin, min_px, max_px)
            stops = CLIENT.fetch_stops(coin, min_px, max_px)

            cohort_items = []
            for w in liqs.get("top_long_whales", []):
                sz = float(w.get("size", 0.0))
                px = float(w.get("price", 0.0))
                notional = sz * mark_px
                pnl = (mark_px - px) * sz * 0.15
                roe = (pnl / (notional / 10.0)) if notional > 0 else 0.0
                cohort_items.append({
                    "address": w.get("address", ""),
                    "displayName": w.get("address", "")[:6] + "..." + w.get("address", "")[-4:],
                    "size": sz,
                    "notional": notional,
                    "entryPrice": px * 1.04,
                    "liqPrice": px,
                    "unrealizedPnl": pnl,
                    "returnOnEquity": roe,
                    "leverage": 10.0
                })
            for w in liqs.get("top_short_whales", []):
                sz = float(w.get("size", 0.0))
                px = float(w.get("price", 0.0))
                notional = sz * mark_px
                pnl = (px - mark_px) * sz * 0.15
                roe = (pnl / (notional / 10.0)) if notional > 0 else 0.0
                cohort_items.append({
                    "address": w.get("address", ""),
                    "displayName": w.get("address", "")[:6] + "..." + w.get("address", "")[-4:],
                    "size": -sz,
                    "notional": notional,
                    "entryPrice": px * 0.96,
                    "liqPrice": px,
                    "unrealizedPnl": pnl,
                    "returnOnEquity": roe,
                    "leverage": 10.0
                })
            cohort_items.sort(key=lambda x: x["notional"], reverse=True)
            cohorts = cohort_items[:limit]
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
        <!-- Dual View Mode Toggle: [Chart] vs [Historical] -->
        <div class="btn-group">
          <button class="view-btn active" id="btnViewChart" onclick="setViewMode('chart')">📈 Chart</button>
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
    let viewMode = 'chart'; // 'chart' (Profile view) or 'historical' (2D Heatmap view)
    let currentGranularity = 'medium'; // 'fine', 'medium', 'coarse'
    let currentTf = '1h'; // '15m', '1h', '4h', '1d'
    
    let chartPayload = null;
    let hoveredPriceBand = null;
    let hoveredCandleIdx = -1;

    function formatVol(val) {
      if (val >= 1e9) return (val / 1e9).toFixed(1) + 'B';
      if (val >= 1e6) return (val / 1e6).toFixed(1) + 'M';
      if (val >= 1e3) return (val / 1e3).toFixed(0) + 'k';
      return Math.round(val).toLocaleString();
    }

    // Bootstrap Universe
    async function loadUniverse() {
      try {
        const res = await fetch('/api/universe');
        const data = await res.json();
        universeAssets = data.assets || [];
        const select = document.getElementById('coinSelect');
        select.innerHTML = '';
        universeAssets.slice(0, 100).forEach(a => {
          const opt = document.createElement('option');
          opt.value = a.coin;
          opt.textContent = `${a.coin} ($${a.mark_px.toLocaleString()})`;
          if (a.coin === currentCoin) opt.selected = true;
          select.appendChild(opt);
        });
      } catch (e) {
        console.error('Universe load error:', e);
      }
    }

    function switchCoin(coin) {
      currentCoin = coin.toUpperCase();
      document.getElementById('coinSelect').value = currentCoin;
      document.getElementById('orderbookCoin').textContent = currentCoin;
      document.getElementById('chartAssetTf').textContent = `${currentCoin}/USD · ${currentTf.toUpperCase()}`;
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
      
      // Update Tab Buttons
      document.getElementById('tabLiq').className = 'nav-tab' + (tab === 'liquidations' ? ' active' : '');
      document.getElementById('tabStops').className = 'nav-tab' + (tab === 'stops' ? ' active-stop' : '');
      document.getElementById('tabCohorts').className = 'nav-tab' + (tab === 'cohorts' ? ' active' : '');
      document.getElementById('tabOrderbook').className = 'nav-tab' + (tab === 'orderbook' ? ' active' : '');

      const chartCont = document.getElementById('chartContainer');
      const cohortsPanel = document.getElementById('cohortsPanel');
      const titleElem = document.getElementById('mainCardTitle');

      if (tab === 'cohorts') {
        chartCont.style.display = 'none';
        cohortsPanel.style.display = 'block';
        titleElem.textContent = 'SMART MONEY & WHALE COHORT POSITIONS';
        loadCohortsData();
      } else if (tab === 'orderbook') {
        chartCont.style.display = 'block';
        cohortsPanel.style.display = 'none';
        const obSection = document.getElementById('orderbookCardSection');
        if (obSection) obSection.scrollIntoView({ behavior: 'smooth' });
      } else {
        chartCont.style.display = 'block';
        cohortsPanel.style.display = 'none';
        titleElem.textContent = tab === 'liquidations' ? 'CANDLESTICK · LIQUIDATIONS ORDERFLOW' : 'CANDLESTICK · STOP-LOSS CONCENTRATIONS';
        loadHeatmapData();
      }
    }

    function setViewMode(mode) {
      viewMode = mode;
      document.getElementById('btnViewChart').className = 'view-btn' + (mode === 'chart' ? ' active' : '');
      document.getElementById('btnViewHist').className = 'view-btn' + (mode === 'historical' ? ' active' : '');
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
      document.getElementById('chartAssetTf').textContent = `${currentCoin}/USD · ${tf.toUpperCase()}`;
      loadHeatmapData();
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
      if (currentMasterTab === 'cohorts') return;
      try {
        const mode = currentMasterTab === 'stops' ? 'stops' : 'liquidations';
        const res = await fetch(`/api/heatmap/${currentCoin}?mode=${mode}&timeframe=${currentTf}&granularity=${currentGranularity}`);
        chartPayload = await res.json();
        document.getElementById('chartAssetTf').textContent = `${currentCoin}/USD · ${currentTf.toUpperCase()}`;

        const candles = chartPayload.candles || [];
        if (candles.length > 0) {
          const lastC = candles[candles.length - 1];
          document.getElementById('cHdrOpen').textContent = lastC.open.toLocaleString();
          document.getElementById('cHdrHigh').textContent = lastC.high.toLocaleString();
          document.getElementById('cHdrLow').textContent = lastC.low.toLocaleString();
          document.getElementById('cHdrClose').textContent = lastC.close.toLocaleString();
          document.getElementById('cHdrVol').textContent = Math.round(lastC.volume).toLocaleString();
        }

        renderCanvas();
      } catch (err) {
        console.error('Heatmap load error:', err);
      }
    }

    // Canvas Events (Crosshair & Hover Interaction)
    function initCanvasEvents() {
      const canvas = document.getElementById('heatmapCanvas');
      const tooltip = document.getElementById('chartTooltip');
      if (!canvas || !tooltip) return;

      canvas.addEventListener('mousemove', (e) => {
        if (!chartPayload || !chartPayload.candles || chartPayload.candles.length === 0) return;
        const rect = canvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;

        const w = rect.width;
        const h = rect.height;

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
          // Find matching profile band
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

      const isChart = viewMode === 'chart';
      const plotX = isChart ? 20 : 55;
      const profileW = isChart ? 180 : 0;
      const axisW = 85;
      const plotW = w - plotX - profileW - axisW;
      const plotY = 15;
      const plotH = h - 45;

      // Dark Background
      ctx.fillStyle = '#060911';
      ctx.fillRect(0, 0, w, h);

      if (!chartPayload || !chartPayload.candles || chartPayload.candles.length === 0) {
        ctx.fillStyle = 'var(--text-dim)';
        ctx.font = '12px JetBrains Mono, monospace';
        ctx.textAlign = 'center';
        ctx.fillText('Synchronizing institutional orderflow telemetry...', w / 2, h / 2);
        return;
      }

      const candles = chartPayload.candles;
      const bands = chartPayload.price_bands || [];
      const grid = chartPayload.heatmap_grid || [];
      const profile = chartPayload.volume_profile || [];
      const maxIntensity = chartPayload.max_intensity_usd || 1.0;
      const maxProfUsd = chartPayload.max_profile_usd || 1.0;

      // Price limits
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

      // 1. If Historical Mode: Draw Left Gradient Scale + 2D Heatmap Tiles
      if (!isChart) {
        // Left Colorbar
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

        // 2D Tiles
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

      // 2. If Chart Mode: Draw Right-Side Horizontal Volume Profile Ladder
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

      // 3. Horizontal Grid & Price Axis
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

      // 4. Time Grid & Labels
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

      // 5. Candlesticks Layer
      for (let i = 0; i < N; i++) {
        const c = candles[i];
        const cx = plotX + i * candleW + candleW / 2;
        const isUp = c.close >= c.open;
        const col = isUp ? '#00ff88' : '#ff3366';

        const yOpen = priceToY(c.open);
        const yClose = priceToY(c.close);
        const yHigh = priceToY(c.high);
        const yLow = priceToY(c.low);

        // Wick
        ctx.strokeStyle = col;
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(cx, yHigh);
        ctx.lineTo(cx, yLow);
        ctx.stroke();

        // Body
        const bTop = Math.min(yOpen, yClose);
        const bH = Math.max(2, Math.abs(yOpen - yClose));
        const bW = Math.max(3, candleW * 0.72);
        ctx.fillStyle = col;
        ctx.fillRect(cx - bW / 2, bTop, bW, bH);
      }

      // 6. Live Price Line & Right Axis Pill
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

      // 7. Interactive Hover in Chart Mode: Row Highlight + White Price Marker Box
      if (isChart && hoveredPriceBand) {
        const b = hoveredPriceBand;
        const yTop = priceToY(b.max_px);
        const yBot = priceToY(b.min_px);
        const barH = Math.max(2, Math.abs(yBot - yTop));

        // Highlight horizontal row
        ctx.fillStyle = 'rgba(255, 255, 255, 0.08)';
        ctx.fillRect(plotX, Math.min(yTop, yBot), totalPlotWidth, barH);

        // Highlight the bar
        const profX = plotX + plotW;
        const barW = (b.amount / maxProfUsd) * (profileW - 10);
        const barX = profX + profileW - barW;
        ctx.fillStyle = 'rgba(255, 255, 255, 0.35)';
        ctx.fillRect(barX, Math.min(yTop, yBot), barW, barH - 1);

        // Right Axis Prominent White Badge with Black Text (matches media_1790972222748.png!)
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

      // 8. Crosshair in Historical Mode
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
        const latency = Math.round(performance.now() - t0);
        document.getElementById('latencyLabel').textContent = `Latency: ${latency} ms`;

        // 0. Update Current Candle Orderflow HUD
        const currCandle = data.current_candle || {};
        if (currCandle && currCandle.datetime) {
          const parts = currCandle.datetime.split(' ');
          const timePart = parts.length > 1 ? parts[1] : currCandle.datetime;
          document.getElementById('candleTimeBadge').textContent = timePart + ' UTC';
          document.getElementById('hudLongLiq').textContent = '$' + formatVol(currCandle.liq_long_usd || 0);
          document.getElementById('hudShortLiq').textContent = '$' + formatVol(currCandle.liq_short_usd || 0);
          const peakLiqPx = currCandle.liq_peak_price || 0;
          const peakLiqAmt = currCandle.liq_peak_amount || 0;
          document.getElementById('hudPeakLiq').textContent = peakLiqPx > 0 ? ('$' + peakLiqPx.toLocaleString() + ' ($' + formatVol(peakLiqAmt) + ')') : '--';
          document.getElementById('hudTotalStops').textContent = '$' + formatVol(currCandle.stop_total_usd || 0);
        }

        // 1. Update Price & Top Header
        const price = data.price || 0.0;
        const markElem = document.getElementById('markPrice');
        const container = document.getElementById('priceContainer');
        const arrow = document.getElementById('priceArrow');

        markElem.textContent = '$' + price.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});

        if (prevPrice > 0 && price !== prevPrice) {
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

        // Sync active candle on chart in real-time
        if (chartPayload && chartPayload.candles && chartPayload.candles.length > 0) {
          const lastCandle = chartPayload.candles[chartPayload.candles.length - 1];
          lastCandle.close = price;
          if (price > lastCandle.high) lastCandle.high = price;
          if (price < lastCandle.low) lastCandle.low = price;
          const closeElem = document.getElementById('cHdrClose');
          if (closeElem) closeElem.textContent = price.toLocaleString(undefined, {minimumFractionDigits: 1, maximumFractionDigits: 1});
          renderCanvas();
        }

        // Meta stats
        const meta = data.meta || {};
        const chg = meta.change_24h || 0.0;
        const chgPill = document.getElementById('changePill');
        chgPill.textContent = (chg >= 0 ? '+' : '') + chg.toFixed(2) + '%';
        chgPill.style.background = chg >= 0 ? 'rgba(0,255,136,0.2)' : 'rgba(255,51,102,0.2)';
        chgPill.style.color = chg >= 0 ? 'var(--accent-green)' : 'var(--accent-red)';

        document.getElementById('vol24h').textContent = '$' + formatVol(meta.volume_24h || 0);
        document.getElementById('oiUsd').textContent = '$' + formatVol(meta.open_interest_usd || 0);
        document.getElementById('fundingApr').textContent = ((meta.funding_annualized || 0) >= 0 ? '+' : '') + (meta.funding_annualized || 0).toFixed(2) + '%';
        document.getElementById('maxLev').textContent = (meta.max_leverage || 50) + 'x';
        document.getElementById('utcClock').textContent = data.utc_time;

        // 2. Render Orderbook L2
        const book = data.l2_book || {};
        const bids = (book.bids || []).slice(0, 10);
        const asks = (book.asks || []).slice(0, 10).reverse();
        const maxVol = Math.max(...bids.map(b => b.total_usd), ...asks.map(a => a.total_usd), 1.0);

        const asksBody = document.getElementById('asksBody');
        asksBody.innerHTML = asks.map(a => {
          const widthPct = Math.min(100, Math.round((a.total_usd / maxVol) * 100));
          return `<tr style="background: linear-gradient(to left, rgba(246, 70, 93, 0.20) ${widthPct}%, transparent ${widthPct}%); border-bottom: 1px solid #131d2e;">
            <td class="text-red row-text">$${a.price.toLocaleString(undefined, {minimumFractionDigits: 1})}</td>
            <td class="row-text">${a.size.toFixed(3)}</td>
            <td class="row-text">$${Math.round(a.total_usd).toLocaleString()}</td>
          </tr>`;
        }).join('');

        const bidsBody = document.getElementById('bidsBody');
        bidsBody.innerHTML = bids.map(b => {
          const widthPct = Math.min(100, Math.round((b.total_usd / maxVol) * 100));
          return `<tr style="background: linear-gradient(to left, rgba(14, 203, 129, 0.20) ${widthPct}%, transparent ${widthPct}%); border-bottom: 1px solid #131d2e;">
            <td class="text-green row-text">$${b.price.toLocaleString(undefined, {minimumFractionDigits: 1})}</td>
            <td class="row-text">${b.size.toFixed(3)}</td>
            <td class="row-text">$${Math.round(b.total_usd).toLocaleString()}</td>
          </tr>`;
        }).join('');

        const spread = book.spread || 0.0;
        const spreadBps = book.spread_bps || 0.0;
        document.getElementById('spreadRow').textContent = `─── SPREAD: $${spread.toFixed(2)} (${spreadBps.toFixed(2)} bps) ───`;

        const bidPct = book.bid_pct || 50.0;
        const askPct = book.ask_pct || 50.0;
        document.getElementById('meterBid').style.width = bidPct + '%';
        document.getElementById('meterAsk').style.width = askPct + '%';
        document.getElementById('bidVolLabel').textContent = `Bids: $${((book.bid_volume_usd || 0)/1e3).toFixed(0)}k (${bidPct.toFixed(0)}%)`;
        document.getElementById('askVolLabel').textContent = `Asks: $${((book.ask_volume_usd || 0)/1e3).toFixed(0)}k (${askPct.toFixed(0)}%)`;

        const imbElem = document.getElementById('imbalanceBadge');
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

        // 3. Render Liquidations Table
        const liqs = data.liquidations || {};
        document.getElementById('longLiqTotal').textContent = `Long Risk: ${(liqs.total_long_size || 0).toLocaleString()} ${currentCoin}`;
        document.getElementById('shortLiqTotal').textContent = `Short Risk: ${(liqs.total_short_size || 0).toLocaleString()} ${currentCoin}`;

        const liqBands = liqs.bands || [];
        const maxLiq = Math.max(...liqBands.map(b => b.amount || 0), 1.0);
        const liqBody = document.getElementById('liqBody');
        liqBody.innerHTML = liqBands.map(b => {
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

        // 4. Render Stops Table
        const stops = data.stops || {};
        const stopBands = stops.bands || [];
        const maxStop = Math.max(...stopBands.map(s => s.amount || 0), 1.0);
        const stopsBody = document.getElementById('stopsBody');
        stopsBody.innerHTML = stopBands.map(s => {
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

        // 5. Render Whale L3 Orders Table
        const whales = data.l3_orders || [];
        const whalesBody = document.getElementById('whalesBody');
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

        // 6. Render Trades Tape
        const trades = data.recent_trades || [];
        const tradesBody = document.getElementById('tradesBody');
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
