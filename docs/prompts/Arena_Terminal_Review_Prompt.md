# PROMPT FOR ARENA.AI / OX ALPHA: INSTITUTIONAL CODE REVIEW & AUDIT OF HYPERDASH CHROMIUM TRADING TERMINAL & ORDERFLOW PIPELINE

---

## 🎯 MISSION BRIEFING & OBJECTIVE

You are acting as an Institutional Senior Quantitative Architect, High-Frequency Trading (HFT) Systems Engineer, and Market Microstructure Forensics Auditor.

Your mission is to perform a **comprehensive, adversarial code review and architecture audit** of the newly developed **Hyperdash Institutional Chromium Trading Terminal & Quantitative Pipeline** (`Trading_2`).

The system ingests real-time orderflow, Level 2 depth, Level 3 resting whale orders with verified Ethereum wallet addresses, liquidation cascade ladders, stop-loss cluster landscapes, and multi-timeframe OHLCV candles from Hyperliquid and Hyperdash, presenting them via an ultra-low-latency interactive Web/Chrome terminal (`http://localhost:8095`) and dumping synchronized multi-modal Parquet datasets for quant research.

---

## 🏗️ SYSTEM ARCHITECTURE & CODEBASE INVENTORY

The pipeline comprises four core production modules in `Terminal/`:

```
Trading_2/
├── Terminal/
│   ├── Chrome_Terminal.py     (1,834 lines) — FastAPI server, SSE/polling loops, L2/L3 orderbook, HTML5 Canvas 2D Heatmap engine & UI
│   ├── Heatmap_Engine.py       (325 lines)   — Multi-resolution orderflow fusion, carry-forward binary-search interpolation, volume profiles
│   ├── Api_Client.py           (590 lines)   — Dual REST & GraphQL client (Hyperliquid + Hyperdash), Cloudflare 429 backoff, UTC normalizer
│   └── Dump_History.py         (285 lines)   — End-to-end historical data fusion engine (OHLCV + Liqs + Stops + Funding -> Parquet)
├── Data/
│   └── Hyperdash_Historical/   — Fused multi-modal 15m/1h historical Parquet datasets
├── Tests/
│   ├── Test_Hyperdash_Client.py — Pytest suite for API connectivity & data contracts
│   └── Test_Terminal_Render.py  — Visual & numeric sanity verification
```

---

## 🔍 DEEP-DIVE COMPONENT SPECIFICATIONS

### 1. `Terminal/Api_Client.py` (Dual REST / GraphQL Exchange Ingestion)
- **Hyperliquid Info REST**:
  - `fetch_candles(coin, interval, lookback_days)`: Ingests `candleSnapshot` (epoch ms timestamps), normalizes to ISO UTC `YYYY-MM-DD HH:MM:SS`.
  - `fetch_recent_trades(coin)`: Ingests trade ticks with aggressor side (`B` / `A`) and whale volume tags.
  - `fetch_l2_book(coin)`: Real-time Level 2 depth book, computing cumulative bid/ask volume, spread, and spread in basis points (bps).
  - `fetch_all_assets()`: 234-coin universe discovery with mark prices, 24h volume, open interest, and annualized funding APR.
- **Hyperdash GraphQL**:
  - `fetch_liquidations(coin, min_price, max_price, lookback_days)`: Queries `liquidationLevelsV2` with price bands and hourly historical time-series distributions.
  - `fetch_stops(coin, min_price, max_price, lookback_days)`: Queries `stopOrderLevelsV2` with resting buy/sell stop clusters.
  - `fetch_l3_orders(coin, min_price, max_price)`: Queries `orderbookSnapshotFiltered` resolving resting orders directly to verified Ethereum wallet addresses.
  - `fetch_top_traders(coin)`: Ingests top PnL traders and whale cohort positions.
- **Robustness**:
  - Cloudflare HTTP 429 Error 1015 exponential retry loop (`_retry_call`).
  - UTC epoch-second conversion normalizer ensuring `candle_snapshots` keys match candle datetime keys.

### 2. `Terminal/Heatmap_Engine.py` (Multi-Timeframe Orderflow Engine)
- **Dynamic Lookback Scaling**:
  - `15m` -> 2 days (192 candles)
  - `1h` -> 4 days (96 candles)
  - `4h` -> 14 days (84 candles)
  - `1d` -> 30 days (30 candles)
- **Sub-Hourly Gap Resolution (The 1-Hour vs 15-Minute Mismatch)**:
  - Hyperdash GraphQL supplies historical liquidation/stop matrices at 1-hour resolution.
  - To prevent blank tiles on 15m charts, implemented chronological binary-search carry-forward:
    ```python
    def _get_levels_with_fallback(dt_str: str) -> list:
        levels = candle_snapshots.get(dt_str)
        if levels is not None:
            return levels
        idx = bisect.bisect_right(sorted_snap_keys, dt_str) - 1
        if idx >= 0:
            return candle_snapshots[sorted_snap_keys[idx]]
        return candle_snapshots[sorted_snap_keys[0]] if sorted_snap_keys else []
    ```
- **Volume Profile Ladder**:
  - Right-side price-aligned horizontal bars color-coded by microstructure side (Red for Long Liquidation risk below price, Green for Short Squeeze risk above price).

### 3. `Terminal/Chrome_Terminal.py` (FastAPI Server & HTML5 Canvas UI)
- **FastAPI Backend (`http://localhost:8095`)**:
  - `/api/universe`: 234-asset live discovery.
  - `/api/live/{coin}`: Ultra-low latency endpoint returning live price ticks, 10-level L2 depth, L3 resting whale orders, aggressor tape, and active-candle orderflow HUD metrics.
  - `/api/heatmap/{coin}`: Serves complete 2D time x price matrix tiles and volume profile ladder.
  - `/api/cohorts/{coin}`: Smart money wallet cohorts with ROE, leverage, entry price, and liquidation cushion.
- **Front-End UX & Canvas 2D Engine**:
  - Dual modes: `[📈 Chart Mode]` (candlesticks + volume profile ladder) and `[📊 Historical Mode]` (2D heatmap matrix tiles with left-hand vertical gradient colorbar).
  - Multi-resolution granularity: Fine, Medium, Coarse price binning.
  - Active Candle Orderflow HUD: Real-time Long Liquidation Risk ($), Short Squeeze Risk ($), Peak Liquidation Level ($), and Total Stop-Loss Clusters ($).
  - Dynamic live price ticking with green/red flashing animation and sub-second directional arrows (▲/▼).

### 4. `Terminal/Dump_History.py` (Historical Multi-Modal Data Dump Pipeline)
- Paginates Hyperliquid OHLCV candles backward to genesis (5,009 15m bars).
- Fetches 7-day liquidation and stop landscapes with Cloudflare 429 exponential backoff.
- Ingests 90-day funding rate history.
- Fuses all 23 features per candle with carry-forward interpolation and writes clean Parquet files to `Data/Hyperdash_Historical/`.

---

## 📋 AUDIT & REVIEW CHECKLIST FOR ARENA.AI

Please conduct a rigorous forensic audit covering the following five domains and provide an actionable scorecard with specific code recommendations:

### Domain 1: Microstructure Realism & Data Provenance
1. **Exchange Liquidation Semantics**:
   - Are Hyperliquid perpetual liquidation mechanics correctly modeled? Specifically: does mid_price < current_price accurately isolate Long Liquidations, and mid_price >= current_price isolate Short Squeezes?
   - How should maintenance margin and collateral haircuts be accounted for in the cohort liquidation cushion?
2. **Stop-Loss vs Liquidation Dynamics**:
   - Stop-loss orders resting above price represent Buy Stops (short covers or breakout longs), while stops below price represent Sell Stops (long stops or breakdown shorts). Does the terminal's classification adhere strictly to exchange order types?
3. **Resting L3 Whale Orders**:
   - Are the notional thresholds ($500k Mega Whale, $150k Whale, $50k Shark) calibrated appropriately for top-cap Binance/Hyperliquid liquidity, or should they be dynamically scaled by Average Daily Volume (ADV) or 20-period ATR?

### Domain 2: Causal Soundness & Lookahead Prevention
1. **Carry-Forward Interpolation (`bisect_right`)**:
   - For sub-hourly 15m candles using hourly GraphQL snapshots, is the backward carry-forward strictly causal ($t_{snap} \le t_{candle}$)?
   - Does this introduce step-function latency bias in backtesting features (`liq_cascade_imbal`, `stop_imbalance`)?
   - What filtering or EWMA decay should be applied to decaying liquidation levels as prices move away from old clusters?
2. **Real-Time Bar Updating**:
   - In `fetchLiveData()`, the active live price updates the latest candle's close, high, and low on-the-fly. Does this preserve bar immutability on closed candles?

### Domain 3: Concurrency, Latency & Network Resilience
1. **Cloudflare Rate Limiting (Error 1015)**:
   - Hyperdash GraphQL enforces aggressive rate limits. Evaluate the existing 5-second in-memory caching and 30-second exponential back-off.
   - Propose an optimal token-bucket rate limiter or background polling queue to eliminate any chance of 429 errors during multi-asset switching.
2. **Uvicorn / FastAPI Async Architecture**:
   - The current API client uses synchronous `urllib.request`. What is the throughput bottleneck under multiple concurrent browser sessions?
   - Provide an async refactoring pattern using `httpx.AsyncClient` with connection pooling.

### Domain 4: Front-End Rendering Performance & Memory Safety
1. **HTML5 Canvas Double-Buffering & High-DPI Scaling**:
   - How can canvas rendering of 300+ candles with 500+ price bands be optimized for 60 FPS on Retina/4K displays?
   - Are there event-listener memory leaks or canvas context recreation issues during rapid timeframe/asset toggling?
2. **Crosshair & Tooltip Responsiveness**:
   - Is the price-to-canvas coordinate transformation numerically robust against zero-height canvas states or extreme price volatility?

### Domain 5: Quantitative Feature Engineering & Alpha Readiness
1. **Derived Microstructure Features in `Dump_History.py`**:
   - Evaluate `liq_cascade_imbal = (long_liq - short_liq) / (total_liq + 1.0)` and `stop_imbalance = (buy_stops - sell_stops) / (total_stops + 1.0)`.
   - Are these stationary and normalized for use in XGBoost / LightGBM directional prediction models?
   - What additional alpha features (e.g. Distance to Nearest Liquidation Cluster in ATR units, Liquidation Delta Z-Score) should be integrated into the Parquet schema?

---

## 🏆 REQUIRED OUTPUT FORMAT

Please present your review in the following structured format:

1. **Executive Verdict & Institutional Readiness Score** (Scale of 1 to 10 across: Architecture, Causal Soundness, Microstructure Fidelity, Latency/Resilience, Production Readiness).
2. **Critical Vulnerabilities & Edge Cases Identified** (Categorized by P0 Critical, P1 High, P2 Moderate).
3. **Microstructure & Econometric Hardening Recommendations** (Mathematical definitions and precise algorithmic logic).
4. **Concrete Code Patches** (Drop-in Python / JS snippets for recommended improvements).
5. **Next-Phase Quantitative Roadmap** (Integrating these orderflow features into our 20 Out-Of-Sample walk-forward execution engines).
