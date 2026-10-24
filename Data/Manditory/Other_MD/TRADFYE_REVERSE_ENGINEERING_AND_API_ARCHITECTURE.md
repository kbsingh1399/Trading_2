# Tradfye Platform Reverse-Engineering & Microstructure Feed Architecture

> **Document Type:** Institutional Forensic Audit & Integration Blueprint  
> **Target:** `https://tradfye.com` (`tradfye.com/terminal`)  
> **Internal Project Name:** `jev-desk` / `tradfye-web`  
> **Date:** October 24, 2026  
> **Status:** Fully Reverse-Engineered & Verified  

---

## 1. Executive Summary

Tradfye (`https://tradfye.com`) was reverse-engineered from source JavaScript bundles (`assets/index-Dh3S7wf7.js`, `assets/terminal-BAV6kaHf.js`, `assets/web-runtime-RJAebV1n.js`, `assets/trading-app-BEwyDbbW.js`, `assets/access-BLgtcX1_.js`, and `assets/account-gate-BjPk_6Qq.js`). 

The analysis reveals:
1. **Frontend Architecture:** Deployed on Cloudflare edge using TanStack Start / TanStack Router (`__TSR_ROUTER__`) and Lovable (`lovable.dev`).
2. **Backend Architecture:** Built entirely on **Supabase** (Project ID: `pfrtjjxrczmvpdiewejg`, URL: `https://pfrtjjxrczmvpdiewejg.supabase.co`, Key: `sb_publishable_T1ZPsQjpHSZpKHNAr9hXhA_Os4Msm5C`).
3. **Plan & Monetization Reality:** The platform currently offers a single active plan, the **"Beta" plan**, which is **100% Free (`price_cents: 0`)**. Every single terminal view is unlocked for anyone with an account.
4. **Market Data Architecture:** Tradfye does **not** maintain a proprietary server-side data pipeline. Its client-side engine (`jev-desk`) connects directly from the user's browser to public exchange REST and WebSocket endpoints (Binance Vision, Bybit Linear, Coinbase, and Deribit Options).
5. **Tab Closure Root Cause:** The recurring automatic closure of browser tabs was caused by resource contention on Edge remote debugging port 9222, where our background `run_unified_30_sheets_cycle.py` daemon was concurrently opening and closing ephemeral tabs across 16 CoinGlass modules.

---

## 2. Root Cause Analysis: Why Tabs Closed Automatically

### Forensic Sequence
1. The Antigravity task runner maintains `run_unified_30_sheets_cycle.py` (running every 300s).
2. That cycle launches up to 16 parallel Excel data modules (`2_Spot_Netflow_S.py`, `3_Exchanges_LS_Ratio_15M.py`, `7_Liq_Heapmap.py`, etc.).
3. Each module opens an ephemeral tab over CDP (`PUT http://127.0.0.1:9222/json/new?...`), streams DOM updates, and executes `urllib.request.urlopen("http://127.0.0.1:9222/json/close/{tab_id}")` upon completion.
4. When Tradfye was opened inside the same Edge debug instance (`--remote-debugging-port=9222`), Edge's renderer manager suffered memory pressure, process isolation swaps, and WinError 10053 socket terminations (`ConnectionAbortedError: An established connection was aborted by the software in your host machine`), triggering tab tear-downs.

### Permanent Resolution
To view or use the Tradfye interface without tab interference, it must be launched in an **isolated user window** independent of the port 9222 headless scraping queue:
```powershell
Start-Process "msedge.exe" -ArgumentList "--new-window https://tradfye.com/terminal"
```
Or in Google Chrome directly.

---

## 3. Database & Authentication Architecture (Supabase)

Tradfye's state and entitlement model are managed via Supabase:
- **Supabase URL:** `https://pfrtjjxrczmvpdiewejg.supabase.co`
- **Publishable Key:** `sb_publishable_T1ZPsQjpHSZpKHNAr9hXhA_Os4Msm5C`

### Entitlement Plan Query (`rest/v1/plans?select=*`)
```json
[
  {
    "id": "c09aef2a-3313-47dd-a01f-5be02dfb89ea",
    "name": "Beta",
    "description": "Free full access while Tradfye is in beta.",
    "price_cents": 0,
    "interval": "month",
    "features": [
      "heatmap",
      "footprint",
      "whales",
      "profile",
      "gamma",
      "tape",
      "liquidity",
      "futures",
      "sentiment",
      "guide",
      "chart"
    ],
    "highlights": [
      "Liquidity heatmap & DOM",
      "Footprint & volume profile",
      "Whale prints & tape",
      "Gamma, futures & sentiment",
      "Decision panel"
    ],
    "active": true,
    "sort": 1,
    "created_at": "2026-10-11T02:31:18.3455+00:00"
  }
]
```

### Access Entitlement Hook (`access-BLgtcX1_.js`)
When a user logs in:
1. `supabase.auth.getUser()` retrieves the authenticated user `id`.
2. Supabase checks `profiles`, `user_roles`, and `subscriptions`.
3. If no active paid subscription exists, it assigns the free Beta plan (`price_cents === 0`), setting `active: true` and unlocking all 11 features:
   - `chart` (Pro chart)
   - `heatmap` (Liquidity heatmap)
   - `footprint` (Footprint)
   - `whales` (Whale candles)
   - `profile` (Volume profile)
   - `gamma` (Gamma levels)
   - `tape` (Time & sales)
   - `liquidity` (L3 liquidity events)
   - `futures` (Futures)
   - `sentiment` (Sentiment)
   - `guide` (Guide)

---

## 4. Reverse-Engineered Microstructure Data Feeds (`web-runtime-RJAebV1n.js`)

Tradfye collects and aggregates orderflow in real-time by streaming raw market data directly from four major crypto venues:

### A. Binance Market Data Feed
- **REST Trades Aggregation:**
  ```http
  GET https://data-api.binance.vision/api/v3/aggTrades?symbol={SYMBOL}&limit=1000
  ```
- **Real-Time Combined WebSocket Stream:**
  ```
  wss://data-stream.binance.vision/stream?streams={symbol}@aggTrade/{symbol}@depth@100ms/{symbol}@bookTicker
  ```
  *Stream details:*
  - `{symbol}@aggTrade`: Aggregated taker trades with buyer/seller flag, volume, and microsecond timestamps.
  - `{symbol}@depth@100ms`: 100ms L2 order book delta snapshots for real-time liquidity heatmap rendering.
  - `{symbol}@bookTicker`: Top of book best bid/ask prices and sizes for high-frequency spread tracking.

### B. Bybit Linear Perpetual Feed
- **WebSocket Endpoint:**
  ```
  wss://stream.bybit.com/v5/public/linear
  ```
- **Subscription Payload:**
  ```json
  {
    "op": "subscribe",
    "args": [
      "orderbook.50.{venue_symbol}",
      "publicTrade.{venue_symbol}",
      "tickers.{venue_symbol}"
    ]
  }
  ```
- **Keep-Alive:** Sends `{"op": "ping"}` every 20 seconds.

### C. Coinbase Exchange Feed
- **WebSocket Endpoint:**
  ```
  wss://ws-feed.exchange.coinbase.com
  ```
- **Subscription Payload:**
  ```json
  {
    "type": "subscribe",
    "product_ids": ["BTC-USD", "ETH-USD"],
    "channels": ["matches", "level2_batch"]
  }
  ```

### D. Deribit Options Feed (Gamma & Strike Volatility)
- **REST Active Options Query:**
  ```http
  GET https://www.deribit.com/api/v2/public/get_instruments?currency={CURRENCY}&kind=option&expired=false
  ```
- **REST Options Book Summary:**
  ```http
  GET https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency={CURRENCY}&kind=option
  ```
  Used to construct the options gamma pin levels, delta-neutral strike walls, and dealer gamma exposure (GEX).

---

## 5. Local Storage & Client Cache Schema

Tradfye caches settings, recent symbols, and custom signal rules in browser storage:
- **IndexedDB:** Database `tradfye-web` (version 1) stores historical order flow chunks and replay snapshots.
- **LocalStorage Keys:**
  - `jev-desk:recent-symbols`: Array of recently viewed trading pairs (e.g. `["BTCUSDT", "ETHUSDT"]`).
  - `tradfye:save_signals:{symbol}`: Custom alert definitions for orderbook sweeps.
  - `tradfye:load_signals:{symbol}`: Signal playback states.

---

## 6. Strategic Takeaways for Our Quant Desk

1. **No External Black Box Dependency:** Tradfye does not possess any proprietary predictive AI or exclusive institutional feeds. Everything it displays is derived mathematically from public Binance, Bybit, Coinbase, and Deribit WebSocket data.
2. **Direct Replication Feasibility:** Since our existing desk infrastructure (`Terminal/Data_Factory/heretic_daemon.py`, Binance Backtesting Data, and MT5 ticks) already processes taker CVD, liquidity sweeps, and whale walls directly in Python and Cython, we already possess faster and deeper access to these same raw orderflow streams.
3. **Safe UI Access:** If the operator wishes to use the Tradfye visual terminal as a supplementary dashboard, opening it in a standalone browser window (`msedge.exe --new-window https://tradfye.com/terminal`) prevents all tab closure conflicts.
