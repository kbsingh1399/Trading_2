# Trading_2

Institutional Quantitative Trading Terminal, Orderflow Heatmap Engine, and Multi-Asset Backtesting Repository.

---

## 🚀 Key Modules & Capabilities

### 1. `Terminal/` — Institutional Interactive Trading Terminal & Pipelines
- **`Chrome_Terminal.py`**: High-performance interactive Chrome/web trading terminal (FastAPI + Uvicorn + WebSocket/SSE streaming) running on `http://localhost:8095`.
  - **Master Navigation Tabs**: `[Liquidations]`, `[Stops]`, `[Cohort Heatmap]`, `[Orderbook L2/L3]`.
  - **Dual Visualization Modes**:
    - **`📈 Chart View`**: Interactive Candlesticks with Right-Side Horizontal Volume Profile Ladder & white crosshair price markers.
    - **`📊 Historical View`**: 2D Time x Price Heatmap Matrix tiles under candles with left vertical intensity scale bar ($0 to $Max) and 100% continuous sub-hourly carry-forward interpolation.
  - **Orderflow HUD**: Real-time long liquidation risk, short squeeze risk, peak liquidation price, and stop clusters.
  - **Live Aggressor Tape & L2/L3 Book**: Real-time transaction tape with whale prints, depth bars, and bid/ask pressure imbalance meter.
  - **Cohort Heatmap**: Smart money / top whale positions with verified wallet addresses, notional size, liquidation levels, and unrealized PnL.
- **`Heatmap_Engine.py`**: Real-time and historical multi-resolution orderflow fusion engine with binary-search carry-forward alignment for 15m/1h/4h/1d candles.
- **`Api_Client.py`**: Production Hyperliquid info REST and Hyperdash GraphQL client with Cloudflare 429 back-off handling and UTC timestamp synchronization.
- **`Dump_History.py`**: End-to-end historical dump pipeline fusing 5,000+ 15m candles with liquidation landscapes, stop-loss landscapes, and 90-day funding rates into parquet files.

### 2. `Data/Hyperdash_Historical/`
- Parquet historical dumps for quantitative modeling and backtesting (`BTC_15m_full_dump.parquet`, `BTC_15m_candle_heatmap.parquet`, `ETH_15m_candle_heatmap.parquet`, funding rates, etc.).

### 3. `Binance_Data/`
- **Universe**: 18 Institutional Binance USDT-M Perpetuals (`BTC`, `ETH`, `SOL`, `BNB`, `XRP`, `DOGE`, `ADA`, `TRX`, `LINK`, `AVAX`, `SUI`, `NEAR`, `DOT`, `LTC`, `BCH`, `APT`, `OP`, `ARB`).
- **Data Coverage**: Master 15m candles (2020–2026), tick footprint ladders, and dataset manifests.

### 4. `Forex_Data/`
- **Universe**: 156 Multi-Asset Instruments (Major FX pairs, Exotic crosses, Global Equity Indices, Commodities, Metals) across `15m`, `1h`, `4h`, `d1` synchronized parquets.

---

## ⚡ Quick Start

### Launch Interactive Terminal
```bash
python Terminal/Chrome_Terminal.py 8095
```
Open **`http://localhost:8095`** in Google Chrome or your default browser.

### Run Historical Data Dump
```bash
python Terminal/Dump_History.py --coin BTC --tf 15m --liq-days 7 --funding-days 90
```

### Run Tests
```bash
pytest Tests/ -v
```
