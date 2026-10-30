# 🏛️ SOVEREIGN CANDIDATE DOSSIER: GBPUSD
**Canonical Key**: `GBPUSD` | **Broker Instrument**: `GBPUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 14:29:40 IST` (`2026-10-30 08:59:40 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.34` | **Live Ask Quote**: `1.34` | **Mid Price**: `1.34`
- **Spread Points**: `1.00` | **Spread BPS**: `0.07 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `100,000.0` | Digits: `5` | Point: `1e-05`
  * Point Value (1.0 Lot): `1.00 USD` | Point Value (0.01 Lot): `0.0100 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`50.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `1.34` | VWAP Z-Score: `+2.07` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.000722` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `64.33` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.34` | Lower -3.00σ Band: `1.34`
  * Upper +2.51σ Band: `1.34` | Lower -2.51σ Band: `1.34`
  * Upper +2.01σ Band: `1.34` | Lower -2.01σ Band: `1.34`
  * Upper +2.00σ Band: `1.34` | Lower -2.00σ Band: `1.34`
  * Upper +1.28σ Band: `1.34` | Lower -1.28σ Band: `1.34`
  * Upper +1.00σ Band: `1.34` | Lower -1.00σ Band: `1.34`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.34` | EMA-20=`1.34` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.34` (Slope: `+0.0000`) | EMA-100=`1.34`
  * Institutional Anchors: EMA-144=`1.34` | EMA-200=`1.34` (Slope: `+0.0496`) | EMA-233=`1.33`
- **Range Boundaries**: 24H High=`1.34` | 24H Low=`1.33` | Weekly High=`1.34` | Weekly Low=`1.33`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.34` (Distance: `+0.06%`)
  * Point of Control (POC) = `1.34` (Distance: `+0.17%`)
  * Value Area Low (VAL) = `1.34` (Distance: `+0.20%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `TREND_UP_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.33` | POC=`1.33` | VAL=`1.33`
  * Prior Day Extremes: PDH=`1.34` | PDL=`1.33` | PDC=`1.34`
  * Monday Range Blueprint: High=`1.34` | Mid=`1.34` | Low=`1.33`
  * Developing Weekly Value Area: Weekly VAH=`1.34` | Weekly POC=`1.33` | Weekly VAL=`1.33`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.34` | Low=`1.34`
  * London Session (08:00-16:00 UTC): High=`1.34` | Low=`1.34`
  * New York Session (13:00-21:00 UTC): High=`1.35` | Low=`1.33`
  * Initial Balance (First Hour): IB High=`1.34` | IB Low=`1.34`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.34` - `1.35`
  * Optimal Trade Entry (OTE 0.705): `1.34`
  * Structural Invalidation Anchor (0.786): `1.35`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `206` | 275.70 USD | 74.23 USD | `+26.92%` | 3,344.35 USD | `+0.62` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `236` | 315.85 USD | 19.74 USD | `+6.25%` | 3,364.09 USD | `+0.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `211` | 282.43 USD | 243.92 USD | `+86.36%` | 3,608.00 USD | `+1.73` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `708` | 947.67 USD | -440.77 USD | `-46.51%` | 15,008.35 USD | `-0.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `766` | 1,025.16 USD | -37.97 USD | `-3.70%` | 14,970.38 USD | `-0.02` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `653` | 874.06 USD | 690.79 USD | `+79.03%` | 15,661.17 USD | `+0.57` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `5,416` | 7,252.94 USD | -2,574.35 USD | `-35.49%` | 21,456.94 USD | `-0.72` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `3,016` | 4,037.55 USD | -3,484.01 USD | `-86.29%` | 17,972.93 USD | `-0.91` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `2,941` | 3,938.20 USD | 2,366.38 USD | `+60.09%` | 20,339.31 USD | `+0.31` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `9,697` | 12,990.20 USD | 11,691.18 USD | `+90.00%` | 57,525.20 USD | `-0.21` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `23,442` | 31,382.04 USD | -22,459.70 USD | `-71.57%` | 35,065.51 USD | `-1.58` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `17,584` | 23,586.83 USD | 19,217.68 USD | `+81.48%` | 54,283.19 USD | `+0.58` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.33` | `1.34` | `1.33` | `1.34` | `40,930` | 54,714.81 USD | 35,923.87 USD | `+65.66%` | 39,992.30 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `16,632` | 22,245.30 USD | 5,841.73 USD | `+26.26%` | 45,834.02 USD | `-0.65` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `9,697` | 12,990.20 USD | 11,691.18 USD | `+90.00%` | 57,525.20 USD | `-0.21` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `23,442` | 31,382.04 USD | -22,459.70 USD | `-71.57%` | 35,065.51 USD | `-1.58` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `17,584` | 23,586.83 USD | 19,217.68 USD | `+81.48%` | 54,283.19 USD | `+0.58` | **`BULLISH`** | `AGGRESSIVE BUYING` |

- **Deribit Institutional Options Max Pain & Volatility Surface (21_Tradfye_Orderflow.parquet)**:
  * Options Max Pain Price: `0.000000`
  * Call Wall Strike: `0.000000` | Put Wall Strike: `0.000000`

---

## 5. Institutional Whale Armor, Hyperdash Intel & L2 Depth Ladders
*(Sources: 10_Whale_Orders.parquet, 17_Orderbook.parquet, 12_Hyperdash.parquet, 13_Hyperliquid.parquet, 4_Hyperliquid_Analysis.parquet, 16_Hyperdash_telegram_Intel.parquet)*
- **Defending Resting Whale Walls (10_Whale_Orders.parquet)**:
  * Top Defending Bid Wall: `None` (Unarmored)
  * Top Defending Ask Wall: `None` (Unarmored)
| Side | Wall Price (USD) | Size (Coins) | Depth (USD) | Distance (%) | Persistence | Traded % | Venue | Order ID |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID/ASK` | None | `0.0000` | 0.00 USD | `0.00%` | Unarmored | `0.0%` | Interbank L2 | NONE |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Hyperdash | Resting Book | - | - | - | Normal Interbank Book | - | - |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Matrix | Interbank Flow | - | - | - | - | - | - | Interbank Tier |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Map | Near Money | - | - | - | - | 0.00% | - |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.21` | 43,810.00 USD | 0.00 USD | 43,810.00 USD | 0.00 USD | 0.00 USD | 147.73 USD |
| `1D` | `1.21` | 5,290.00 USD | 0.00 USD | 5,290.00 USD | 0.00 USD | 0.00 USD | 49.01 USD |
| `7D` | `1.21` | 43,660.00 USD | 0.00 USD | 43,660.00 USD | 0.00 USD | 0.00 USD | 59.40 USD |
| `1D` | `1.21` | 5,240.00 USD | 0.00 USD | 5,240.00 USD | 0.00 USD | 0.00 USD | 3.66 USD |
| `7D` | `1.28` | 43,610.00 USD | 0.00 USD | 43,610.00 USD | 0.00 USD | 0.00 USD | 810.32 USD |
| `7D` | `1.28` | 42,790.00 USD | 0.00 USD | 42,790.00 USD | 0.00 USD | 0.00 USD | 211.81 USD |
| `1D` | `1.28` | 5,240.00 USD | 0.00 USD | 5,240.00 USD | 0.00 USD | 0.00 USD | 74.75 USD |
| `7D` | `1.28` | 42,580.00 USD | 0.00 USD | 42,580.00 USD | 0.00 USD | 0.00 USD | 656.92 USD |
| `1D` | `1.28` | 5,160.00 USD | 0.00 USD | 5,160.00 USD | 0.00 USD | 0.00 USD | 15.07 USD |
| `7D` | `1.28` | 41,930.00 USD | 0.00 USD | 41,930.00 USD | 0.00 USD | 0.00 USD | 1,670.00 USD |
| `1D` | `1.28` | 5,150.00 USD | 0.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD | 307.98 USD |
| `7D` | `1.28` | 40,260.00 USD | 0.00 USD | 40,260.00 USD | 0.00 USD | 0.00 USD | 2,120.00 USD |
| `1D` | `1.28` | 4,840.00 USD | 0.00 USD | 4,840.00 USD | 0.00 USD | 0.00 USD | 5.25 USD |
| `7D` | `1.28` | 38,140.00 USD | 0.00 USD | 38,140.00 USD | 0.00 USD | 0.00 USD | 145.22 USD |
| `1D` | `1.29` | 4,830.00 USD | 0.00 USD | 4,830.00 USD | 0.00 USD | 0.00 USD | 141.12 USD |
| `7D` | `1.29` | 38,000.00 USD | 0.00 USD | 38,000.00 USD | 0.00 USD | 0.00 USD | 386.75 USD |
| `1D` | `1.29` | 4,690.00 USD | 0.00 USD | 4,690.00 USD | 0.00 USD | 0.00 USD | 127.78 USD |
| `7D` | `1.29` | 37,610.00 USD | 0.00 USD | 37,610.00 USD | 0.00 USD | 0.00 USD | 210.14 USD |
| `1D` | `1.29` | 4,560.00 USD | 0.00 USD | 4,560.00 USD | 0.00 USD | 0.00 USD | 76.18 USD |
| `7D` | `1.29` | 37,400.00 USD | 0.00 USD | 37,400.00 USD | 0.00 USD | 0.00 USD | 25.39 USD |
| `7D` | `1.30` | 37,380.00 USD | 0.00 USD | 37,380.00 USD | 0.00 USD | 0.00 USD | 1,620.00 USD |
| `7D` | `1.30` | 35,760.00 USD | 0.00 USD | 35,760.00 USD | 0.00 USD | 0.00 USD | 321.93 USD |
| `1D` | `1.31` | 4,490.00 USD | 0.00 USD | 4,490.00 USD | 0.00 USD | 0.00 USD | 149.50 USD |
| `7D` | `1.31` | 35,430.00 USD | 0.00 USD | 35,430.00 USD | 0.00 USD | 0.00 USD | 1,420.00 USD |
| `1D` | `1.31` | 4,340.00 USD | 0.00 USD | 4,340.00 USD | 0.00 USD | 0.00 USD | 30.16 USD |
| `7D` | `1.31` | 34,020.00 USD | 0.00 USD | 34,020.00 USD | 0.00 USD | 0.00 USD | 2,230.00 USD |
| `1D` | `1.31` | 4,310.00 USD | 0.00 USD | 4,310.00 USD | 0.00 USD | 0.00 USD | 615.94 USD |
| `7D` | `1.31` | 31,790.00 USD | 0.00 USD | 31,790.00 USD | 0.00 USD | 0.00 USD | 5,340.00 USD |
| `1D` | `1.31` | 3,690.00 USD | 0.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD | 10.50 USD |
| `7D` | `1.31` | 26,450.00 USD | 0.00 USD | 26,450.00 USD | 0.00 USD | 0.00 USD | 242.94 USD |
| `1D` | `1.31` | 3,680.00 USD | 0.00 USD | 3,680.00 USD | 0.00 USD | 0.00 USD | 273.78 USD |
| `7D` | `1.31` | 26,210.00 USD | 0.00 USD | 26,210.00 USD | 0.00 USD | 0.00 USD | 795.47 USD |
| `1D` | `1.31` | 3,410.00 USD | 0.00 USD | 3,410.00 USD | 0.00 USD | 0.00 USD | 247.22 USD |
| `7D` | `1.31` | 25,410.00 USD | 0.00 USD | 25,410.00 USD | 0.00 USD | 0.00 USD | 397.26 USD |
| `1D` | `1.31` | 3,160.00 USD | 0.00 USD | 3,160.00 USD | 0.00 USD | 0.00 USD | 169.13 USD |
| `7D` | `1.31` | 25,020.00 USD | 0.00 USD | 25,020.00 USD | 0.00 USD | 0.00 USD | 99.37 USD |
| `7D` | `1.32` | 24,920.00 USD | 0.00 USD | 24,920.00 USD | 0.00 USD | 0.00 USD | 3,240.00 USD |
| `7D` | `1.32` | 21,680.00 USD | 0.00 USD | 21,680.00 USD | 0.00 USD | 0.00 USD | 113.51 USD |
| `7D` | `1.32` | 21,560.00 USD | 0.00 USD | 21,560.00 USD | 0.00 USD | 0.00 USD | 733.67 USD |
| `1D` | `1.32` | 2,990.00 USD | 0.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD | 298.99 USD |
| `7D` | `1.32` | 20,830.00 USD | 0.00 USD | 20,830.00 USD | 0.00 USD | 0.00 USD | 5,860.00 USD |
| `1D` | `1.32` | 2,690.00 USD | 0.00 USD | 2,690.00 USD | 0.00 USD | 0.00 USD | 1,280.00 USD |
| `7D` | `1.32` | 14,970.00 USD | 0.00 USD | 14,970.00 USD | 0.00 USD | 0.00 USD | 3,920.00 USD |
| `1D` | `1.32` | 1,410.00 USD | 0.00 USD | 1,410.00 USD | 0.00 USD | 0.00 USD | 17.19 USD |
| `7D` | `1.32` | 11,050.00 USD | 0.00 USD | 11,050.00 USD | 0.00 USD | 0.00 USD | 8,300.00 USD |
| `1D` | `1.32` | 1,390.00 USD | 0.00 USD | 1,390.00 USD | 0.00 USD | 0.00 USD | 11.68 USD |
| `7D` | `1.32` | 2,750.00 USD | 0.00 USD | 2,750.00 USD | 0.00 USD | 0.00 USD | 432.04 USD |
| `1D` | `1.33` | 1,380.00 USD | 0.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD | 634.13 USD |
| `7D` | `1.33` | 2,320.00 USD | 0.00 USD | 2,320.00 USD | 0.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `1.33` | 746.17 USD | 0.00 USD | 746.17 USD | 0.00 USD | 0.00 USD | 581.06 USD |
| `7D` | `1.33` | 874.40 USD | 0.00 USD | 874.40 USD | 0.00 USD | 0.00 USD | 874.40 USD |
| `1D` | `1.33` | 165.11 USD | 0.00 USD | 165.11 USD | 0.00 USD | 0.00 USD | 165.11 USD |
| `1D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 3,240.00 USD | 3,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,240.00 USD |
| `7D` | `1.34` | 3,350.00 USD | 3,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 113.51 USD |
| `7D` | `1.35` | 4,090.00 USD | 4,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 733.67 USD |
| `1D` | `1.35` | 298.99 USD | 298.99 USD | 0.00 USD | 0.00 USD | 0.00 USD | 298.99 USD |
| `7D` | `1.35` | 9,940.00 USD | 9,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,860.00 USD |
| `1D` | `1.35` | 1,580.00 USD | 1,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,280.00 USD |
| `7D` | `1.35` | 13,870.00 USD | 13,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,920.00 USD |
| `1D` | `1.35` | 1,590.00 USD | 1,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7.88 USD |
| `7D` | `1.35` | 21,900.00 USD | 21,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,030.00 USD |
| `1D` | `1.35` | 1,610.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20.99 USD |
| `7D` | `1.35` | 22,460.00 USD | 22,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 558.86 USD |
| `1D` | `1.35` | 2,220.00 USD | 2,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 604.09 USD |
| `7D` | `1.35` | 24,040.00 USD | 24,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,580.00 USD |
| `1D` | `1.35` | 2,800.00 USD | 2,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 581.41 USD |
| `7D` | `1.35` | 24,820.00 USD | 24,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 772.82 USD |
| `1D` | `1.36` | 2,990.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 194.80 USD |
| `7D` | `1.36` | 24,920.00 USD | 24,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101.58 USD |
| `7D` | `1.36` | 26,540.00 USD | 26,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,620.00 USD |
| `7D` | `1.36` | 26,860.00 USD | 26,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 321.93 USD |
| `1D` | `1.36` | 3,140.00 USD | 3,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 145.88 USD |
| `7D` | `1.36` | 27,190.00 USD | 27,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 334.98 USD |
| `1D` | `1.36` | 3,170.00 USD | 3,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33.78 USD |
| `7D` | `1.36` | 30,240.00 USD | 30,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,050.00 USD |
| `1D` | `1.36` | 3,790.00 USD | 3,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 615.94 USD |
| `7D` | `1.36` | 35,840.00 USD | 35,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,600.00 USD |
| `1D` | `1.36` | 3,800.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10.50 USD |
| `7D` | `1.36` | 36,050.00 USD | 36,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 212.47 USD |
| `1D` | `1.36` | 4,040.00 USD | 4,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 236.43 USD |
| `7D` | `1.36` | 36,780.00 USD | 36,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 727.96 USD |
| `1D` | `1.37` | 4,160.00 USD | 4,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 125.22 USD |
| `7D` | `1.37` | 37,000.00 USD | 37,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 220.89 USD |
| `1D` | `1.37` | 4,490.00 USD | 4,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 328.48 USD |
| `7D` | `1.37` | 37,380.00 USD | 37,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 373.72 USD |
| `7D` | `1.38` | 38,190.00 USD | 38,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 810.32 USD |
| `7D` | `1.38` | 38,350.00 USD | 38,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 160.99 USD |
| `1D` | `1.39` | 4,560.00 USD | 4,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 72.94 USD |
| `7D` | `1.39` | 38,510.00 USD | 38,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 167.48 USD |
| `1D` | `1.39` | 4,570.00 USD | 4,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10.65 USD |
| `7D` | `1.39` | 40,040.00 USD | 40,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,520.00 USD |
| `1D` | `1.39` | 4,890.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 314.21 USD |
| `7D` | `1.39` | 42,840.00 USD | 42,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,800.00 USD |
| `1D` | `1.39` | 4,890.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.25 USD |
| `7D` | `1.39` | 42,940.00 USD | 42,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 106.24 USD |
| `1D` | `1.39` | 5,010.00 USD | 5,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 114.36 USD |
| `7D` | `1.39` | 43,300.00 USD | 43,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 351.30 USD |
| `1D` | `1.39` | 5,050.00 USD | 5,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44.17 USD |
| `7D` | `1.39` | 43,420.00 USD | 43,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 123.10 USD |
| `1D` | `1.39` | 5,230.00 USD | 5,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 177.41 USD |
| `7D` | `1.39` | 43,610.00 USD | 43,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 186.86 USD |
| `1D` | `1.40` | 5,240.00 USD | 5,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9.14 USD |
| `7D` | `1.46` | 43,930.00 USD | 43,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 324.13 USD |
| `7D` | `1.46` | 43,990.00 USD | 43,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 55.82 USD |
| `7D` | `1.47` | 44,020.00 USD | 44,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39.52 USD |
| `1D` | `1.47` | 5,270.00 USD | 5,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 32.04 USD |
| `7D` | `1.47` | 44,660.00 USD | 44,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 632.95 USD |
| `1D` | `1.47` | 5,390.00 USD | 5,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 125.64 USD |
| `7D` | `1.47` | 45,500.00 USD | 45,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 842.97 USD |
| `1D` | `1.47` | 5,400.00 USD | 5,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.93 USD |
| `7D` | `1.47` | 45,610.00 USD | 45,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 112.08 USD |
| `1D` | `1.47` | 5,400.00 USD | 5,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1.17 USD |
| `7D` | `1.47` | 45,630.00 USD | 45,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20.28 USD |
| `1D` | `1.47` | 5,450.00 USD | 5,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 53.90 USD |
| `7D` | `1.47` | 45,780.00 USD | 45,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 144.79 USD |
| `1D` | `1.47` | 5,490.00 USD | 5,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 42.62 USD |
| `7D` | `1.47` | 45,850.00 USD | 45,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 67.56 USD |
| `1D` | `1.48` | 5,510.00 USD | 5,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17.01 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `0.00` | Last 24h: `0.00` | Last 3d: `0.00` | Last 7d: `0.00`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0122%` | **USDT BingX** | `-` |
| **USDT Gate** | `-` | **USDT Bitget** | `-` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Multi-TF | Interbank Desk | 50.0% | 50.0% | 1.00 | Normal Balanced Liquidity |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `08:15:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 277.02 USD | 25.39 USD | 251.63 USD | -226.23 USD | `-81.67%` | `0B / 1S` |
| `08:20:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 318.48 USD | 100.39 USD | 218.09 USD | -117.70 USD | `-36.96%` | `0B / 1S` |
| `08:25:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 429.60 USD | 330.06 USD | 99.54 USD | 230.52 USD | `+53.66%` | `1B / 0S` |
| `08:30:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 275.70 USD | 174.96 USD | 100.74 USD | 74.23 USD | `+26.92%` | `1B / 0S` |
| `08:30:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 874.06 USD | 782.42 USD | 91.64 USD | 690.79 USD | `+79.03%` | `1B / 0S` |
| `08:35:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 315.85 USD | 167.80 USD | 148.06 USD | 19.74 USD | `+6.25%` | `1B / 0S` |
| `08:40:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 282.43 USD | 263.17 USD | 19.26 USD | 243.92 USD | `+86.36%` | `1B / 0S` |
| `08:45:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 369.46 USD | 299.08 USD | 70.37 USD | 228.71 USD | `+61.90%` | `1B / 0S` |
| `08:45:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 1,090.00 USD | 982.54 USD | 107.47 USD | 875.07 USD | `+80.28%` | `1B / 0S` |
| `08:50:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 323.98 USD | 295.63 USD | 28.35 USD | 267.28 USD | `+82.50%` | `1B / 0S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 17:30:00 IST` | `4h` | `BULLISH ABSORPTION` | **`BULLISH`** | GBPUSD Macro Delta Flow: BULLISH ABSORPT | `1.33` | 1,668.59 USD | 1,668.59 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `15m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `2h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `4h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `6h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `8h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `12h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `24h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1w` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30d` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
- **Institutional Crypto ETF Capital Flows (1_Crypto_ETF_Flows.parquet)**:
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)

- **High-Impact Macro Economic Events (19_Calendar.parquet)**:
  * `Sun Oct 25` [CHF - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Sun Oct 25` [EUR - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Sun Oct 25` [GBP - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Mon Oct 26` [NZD - Low Impact]: Bank Holiday (Forecast: , Previous: )
  * `Mon Oct 26` [AUD - Low Impact]: RBA Assist Gov Jones Speaks (Forecast: , Previous: )
  * `Mon Oct 26` [EUR - Low Impact]: German ifo Business Climate (Forecast: 90.0, Previous: 89.9)
  * `Mon Oct 26` [GBP - Low Impact]: CBI Realized Sales (Forecast: -47, Previous: -55)
  * `Tue Oct 27` [JPY - Low Impact]: SPPI y/y (Forecast: 3.7%, Previous: 3.5%)
  * `Tue Oct 27` [GBP - Low Impact]: BRC Shop Price Index y/y (Forecast: 1.6%, Previous: 1.4%)
  * `Tue Oct 27` [JPY - Low Impact]: BOJ Core CPI y/y (Forecast: 1.9%, Previous: 1.8%)
  * `Tue Oct 27` [EUR - Low Impact]: Spanish Unemployment Rate (Forecast: 9.9%, Previous: 9.9%)
  * `Tue Oct 27` [EUR - Low Impact]: M3 Money Supply y/y (Forecast: 3.5%, Previous: 3.5%)
  * `Tue Oct 27` [EUR - Low Impact]: Private Loans y/y (Forecast: 3.1%, Previous: 3.1%)
  * `Tue Oct 27` [USD - Low Impact]: ADP Weekly Employment Change (Forecast: , Previous: 17.5K)
  * `Tue Oct 27` [USD - Low Impact]: Core Durable Goods Orders m/m (Forecast: 0.6%, Previous: 0.2%)

- **Breaking Institutional News & Market Intelligence (19_News.parquet)**:
  * `2026-10-30 14:09:50 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:50:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:31:50 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [insee.fr] - (Sentiment: `Neutral`)


---

## 9. TradFi & Interbank Market Mechanics
*(Applicable to Foreign Exchange Majors, Precious Metals, Global Equity Indices, and Commodities)*
- **Central Bank Monetary Policy & Rate Differential**:
  * Prevailing Policy Stance: `Federal Reserve (4.75% - 5.00%) Neutral-Gradualist Stance`
  * 2-Year Sovereign Yield Spread Direction & 10-Year Real Yield Momentum.
- **Interbank Foreign Exchange Mechanics**:
  * London/NY Overlap Window (13:00 - 16:00 UTC): Prime Institutional Liquidity.
  * Rollover Spread Expansion Gate: Execution strictly prohibited between 21:15 UTC and 22:30 UTC.
- **Global Commodity & Index Pricing Drivers**:
  * Precious Metals (XAU/XAG): Real Yield Sensitivity & Geopolitical Safe-Haven Premium.
  * Equity Indices (US30, SP500, NAS100): E-mini Auction VWAP Dispersion & Institutional Gamma Profiles.

---

## 10. Quantitative Trade Formulation & Autonomous Broker Execution Card
*(Sources: Canonical Quant Rules, STANDARDIZED_TRADING_DECISION_CHAIN.md, 10 lethal traps)*
- **Candidate Long Setup (Model 1 / Model 2 VAL Sweep Fade)**:
  * Order Type: `BUY_LIMIT`
  * Execution Entry: `1.34` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1.34` (Risk Distance: `0.000882` pts)
  * +2.5R Take Profit: `1.34`
  * Mathematical Lot Sizing: **`0.11 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.34` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.34` (Risk Distance: `0.000882` pts)
  * +2.5R Take Profit: `1.34`
  * Mathematical Lot Sizing: **`0.11 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.35`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
