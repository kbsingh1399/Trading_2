# 🏛️ SOVEREIGN CANDIDATE DOSSIER: GBPUSD
**Canonical Key**: `GBPUSD` | **Broker Instrument**: `GBPUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-29 23:04:10 IST` (`2026-10-29 17:34:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `1.33` | VWAP Z-Score: `+1.94` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0011` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `68.07` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.34` | Lower -3.00σ Band: `1.33`
  * Upper +2.51σ Band: `1.34` | Lower -2.51σ Band: `1.33`
  * Upper +2.01σ Band: `1.34` | Lower -2.01σ Band: `1.33`
  * Upper +2.00σ Band: `1.34` | Lower -2.00σ Band: `1.33`
  * Upper +1.28σ Band: `1.34` | Lower -1.28σ Band: `1.33`
  * Upper +1.00σ Band: `1.34` | Lower -1.00σ Band: `1.33`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.34` | EMA-20=`1.34` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.33` (Slope: `+0.0000`) | EMA-100=`1.33`
  * Institutional Anchors: EMA-144=`1.33` | EMA-200=`1.33` (Slope: `+0.0400`) | EMA-233=`1.33`
- **Range Boundaries**: 24H High=`1.34` | 24H Low=`1.33` | Weekly High=`1.34` | Weekly Low=`1.33`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.33` (Distance: `+0.29%`)
  * Point of Control (POC) = `1.33` (Distance: `+0.38%`)
  * Value Area Low (VAL) = `1.33` (Distance: `+0.50%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `TREND_UP_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.33` | POC=`1.33` | VAL=`1.33`
  * Prior Day Extremes: PDH=`1.33` | PDL=`1.33` | PDC=`1.33`
  * Monday Range Blueprint: High=`1.34` | Mid=`1.34` | Low=`1.33`
  * Developing Weekly Value Area: Weekly VAH=`1.34` | Weekly POC=`1.33` | Weekly VAL=`1.33`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.33` | Low=`1.33`
  * London Session (08:00-16:00 UTC): High=`1.33` | Low=`1.33`
  * New York Session (13:00-21:00 UTC): High=`1.34` | Low=`1.33`
  * Initial Balance (First Hour): IB High=`1.33` | IB Low=`1.33`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.33` - `1.34`
  * Optimal Trade Entry (OTE 0.705): `1.34`
  * Structural Invalidation Anchor (0.786): `1.35`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.33` | `1.33` | `1.33` | `1.33` | `1,235` | 1,646.29 USD | -832.09 USD | `-50.54%` | 4,290.85 USD | `-0.94` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.33` | `1.33` | `1.33` | `1.33` | `1,141` | 1,521.41 USD | 991.90 USD | `+65.20%` | 5,282.75 USD | `+1.14` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.33` | `1.33` | `1.33` | `1.33` | `1,205` | 1,607.46 USD | 566.92 USD | `+35.27%` | 5,849.66 USD | `+0.60` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.33` | `1.33` | `1.33` | `1.33` | `2,916` | 3,885.34 USD | 2,803.62 USD | `+72.16%` | 7,633.90 USD | `+1.76` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.33` | `1.33` | `1.33` | `1.33` | `3,656` | 4,873.56 USD | 1,254.01 USD | `+25.73%` | 8,887.92 USD | `+0.65` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.33` | `1.33` | `1.33` | `1.33` | `3,605` | 4,810.08 USD | 3,477.88 USD | `+72.30%` | 12,365.79 USD | `+1.95` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.33` | `1.33` | `1.33` | `1.33` | `8,045` | 10,715.30 USD | -4,652.69 USD | `-43.42%` | 8,796.03 USD | `-1.18` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.33` | `1.33` | `1.33` | `1.33` | `12,725` | 16,955.04 USD | 5,816.29 USD | `+34.30%` | 14,612.33 USD | `+1.21` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.33` | `1.34` | `1.33` | `1.34` | `12,464` | 16,646.79 USD | 13,879.53 USD | `+83.38%` | 28,491.86 USD | `+2.56` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.33` | `1.33` | `1.33` | `1.33` | `17,831` | 23,736.63 USD | -8,250.46 USD | `-34.76%` | 6,873.72 USD | `-0.97` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.33` | `1.33` | `1.33` | `1.33` | `23,876` | 31,800.92 USD | 4,068.43 USD | `+12.79%` | 10,942.15 USD | `+0.20` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `1.33` | `1.34` | `1.33` | `1.34` | `40,930` | 54,714.81 USD | 35,923.87 USD | `+65.66%` | 46,866.02 USD | `+1.86` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.33` | `1.33` | `1.33` | `1.33` | `8,476` | 11,286.05 USD | -2,669.82 USD | `-23.66%` | 16,180.76 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.33` | `1.33` | `1.33` | `1.33` | `17,244` | 22,969.01 USD | -1,056.57 USD | `-4.60%` | 15,124.19 USD | `-0.62` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.33` | `1.33` | `1.33` | `1.33` | `17,831` | 23,736.63 USD | -8,250.46 USD | `-34.76%` | 6,873.72 USD | `-0.97` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.33` | `1.33` | `1.33` | `1.33` | `23,876` | 31,800.92 USD | 4,068.43 USD | `+12.79%` | 10,942.15 USD | `+0.20` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `1.33` | `1.34` | `1.33` | `1.34` | `40,930` | 54,714.81 USD | 35,923.87 USD | `+65.66%` | 46,866.02 USD | `+1.86` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `7D` | `1.20` | 45,100.00 USD | 0.00 USD | 45,100.00 USD | 0.00 USD | 0.00 USD | 581.37 USD |
| `7D` | `1.20` | 44,520.00 USD | 0.00 USD | 44,520.00 USD | 0.00 USD | 0.00 USD | 376.19 USD |
| `7D` | `1.20` | 44,140.00 USD | 0.00 USD | 44,140.00 USD | 0.00 USD | 0.00 USD | 649.63 USD |
| `7D` | `1.20` | 43,490.00 USD | 0.00 USD | 43,490.00 USD | 0.00 USD | 0.00 USD | 130.82 USD |
| `1D` | `1.20` | 16,250.00 USD | 0.00 USD | 16,250.00 USD | 0.00 USD | 0.00 USD | 44.12 USD |
| `7D` | `1.21` | 43,360.00 USD | 0.00 USD | 43,360.00 USD | 0.00 USD | 0.00 USD | 57.59 USD |
| `1D` | `1.21` | 16,210.00 USD | 0.00 USD | 16,210.00 USD | 0.00 USD | 0.00 USD | 6.45 USD |
| `7D` | `1.21` | 43,300.00 USD | 0.00 USD | 43,300.00 USD | 0.00 USD | 0.00 USD | 34.30 USD |
| `7D` | `1.28` | 43,270.00 USD | 0.00 USD | 43,270.00 USD | 0.00 USD | 0.00 USD | 829.42 USD |
| `7D` | `1.28` | 42,440.00 USD | 0.00 USD | 42,440.00 USD | 0.00 USD | 0.00 USD | 192.71 USD |
| `1D` | `1.28` | 16,200.00 USD | 0.00 USD | 16,200.00 USD | 0.00 USD | 0.00 USD | 6.59 USD |
| `7D` | `1.28` | 42,250.00 USD | 0.00 USD | 42,250.00 USD | 0.00 USD | 0.00 USD | 656.92 USD |
| `1D` | `1.28` | 16,200.00 USD | 0.00 USD | 16,200.00 USD | 0.00 USD | 0.00 USD | 102.23 USD |
| `7D` | `1.28` | 41,590.00 USD | 0.00 USD | 41,590.00 USD | 0.00 USD | 0.00 USD | 1,670.00 USD |
| `1D` | `1.28` | 16,090.00 USD | 0.00 USD | 16,090.00 USD | 0.00 USD | 0.00 USD | 502.26 USD |
| `7D` | `1.28` | 39,920.00 USD | 0.00 USD | 39,920.00 USD | 0.00 USD | 0.00 USD | 2,120.00 USD |
| `1D` | `1.28` | 15,590.00 USD | 0.00 USD | 15,590.00 USD | 0.00 USD | 0.00 USD | 1,570.00 USD |
| `7D` | `1.28` | 37,810.00 USD | 0.00 USD | 37,810.00 USD | 0.00 USD | 0.00 USD | 153.00 USD |
| `1D` | `1.28` | 14,020.00 USD | 0.00 USD | 14,020.00 USD | 0.00 USD | 0.00 USD | 2.92 USD |
| `7D` | `1.29` | 37,650.00 USD | 0.00 USD | 37,650.00 USD | 0.00 USD | 0.00 USD | 437.32 USD |
| `1D` | `1.29` | 14,020.00 USD | 0.00 USD | 14,020.00 USD | 0.00 USD | 0.00 USD | 130.29 USD |
| `7D` | `1.29` | 37,220.00 USD | 0.00 USD | 37,220.00 USD | 0.00 USD | 0.00 USD | 112.68 USD |
| `7D` | `1.29` | 37,100.00 USD | 0.00 USD | 37,100.00 USD | 0.00 USD | 0.00 USD | 16.53 USD |
| `7D` | `1.30` | 37,090.00 USD | 0.00 USD | 37,090.00 USD | 0.00 USD | 0.00 USD | 1,660.00 USD |
| `7D` | `1.30` | 35,430.00 USD | 0.00 USD | 35,430.00 USD | 0.00 USD | 0.00 USD | 385.39 USD |
| `1D` | `1.31` | 13,890.00 USD | 0.00 USD | 13,890.00 USD | 0.00 USD | 0.00 USD | 13.17 USD |
| `7D` | `1.31` | 35,040.00 USD | 0.00 USD | 35,040.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD |
| `1D` | `1.31` | 13,880.00 USD | 0.00 USD | 13,880.00 USD | 0.00 USD | 0.00 USD | 204.45 USD |
| `7D` | `1.31` | 33,730.00 USD | 0.00 USD | 33,730.00 USD | 0.00 USD | 0.00 USD | 3,330.00 USD |
| `1D` | `1.31` | 13,670.00 USD | 0.00 USD | 13,670.00 USD | 0.00 USD | 0.00 USD | 1,000.00 USD |
| `7D` | `1.31` | 30,400.00 USD | 0.00 USD | 30,400.00 USD | 0.00 USD | 0.00 USD | 4,230.00 USD |
| `1D` | `1.31` | 12,670.00 USD | 0.00 USD | 12,670.00 USD | 0.00 USD | 0.00 USD | 3,140.00 USD |
| `7D` | `1.31` | 26,160.00 USD | 0.00 USD | 26,160.00 USD | 0.00 USD | 0.00 USD | 290.42 USD |
| `1D` | `1.31` | 9,530.00 USD | 0.00 USD | 9,530.00 USD | 0.00 USD | 0.00 USD | 10.50 USD |
| `7D` | `1.31` | 25,870.00 USD | 0.00 USD | 25,870.00 USD | 0.00 USD | 0.00 USD | 879.35 USD |
| `1D` | `1.31` | 9,520.00 USD | 0.00 USD | 9,520.00 USD | 0.00 USD | 0.00 USD | 260.57 USD |
| `7D` | `1.31` | 24,990.00 USD | 0.00 USD | 24,990.00 USD | 0.00 USD | 0.00 USD | 222.30 USD |
| `7D` | `1.31` | 24,770.00 USD | 0.00 USD | 24,770.00 USD | 0.00 USD | 0.00 USD | 47.02 USD |
| `7D` | `1.32` | 24,730.00 USD | 0.00 USD | 24,730.00 USD | 0.00 USD | 0.00 USD | 3,240.00 USD |
| `7D` | `1.32` | 21,480.00 USD | 0.00 USD | 21,480.00 USD | 0.00 USD | 0.00 USD | 158.18 USD |
| `1D` | `1.32` | 9,260.00 USD | 0.00 USD | 9,260.00 USD | 0.00 USD | 0.00 USD | 26.34 USD |
| `7D` | `1.32` | 21,330.00 USD | 0.00 USD | 21,330.00 USD | 0.00 USD | 0.00 USD | 880.93 USD |
| `1D` | `1.32` | 9,230.00 USD | 0.00 USD | 9,230.00 USD | 0.00 USD | 0.00 USD | 291.75 USD |
| `7D` | `1.32` | 20,440.00 USD | 0.00 USD | 20,440.00 USD | 0.00 USD | 0.00 USD | 5,970.00 USD |
| `1D` | `1.32` | 8,940.00 USD | 0.00 USD | 8,940.00 USD | 0.00 USD | 0.00 USD | 239.53 USD |
| `7D` | `1.32` | 14,480.00 USD | 0.00 USD | 14,480.00 USD | 0.00 USD | 0.00 USD | 9,780.00 USD |
| `1D` | `1.32` | 8,700.00 USD | 0.00 USD | 8,700.00 USD | 0.00 USD | 0.00 USD | 7,990.00 USD |
| `7D` | `1.32` | 4,700.00 USD | 0.00 USD | 4,700.00 USD | 0.00 USD | 0.00 USD | 2,220.00 USD |
| `1D` | `1.32` | 712.19 USD | 0.00 USD | 712.19 USD | 0.00 USD | 0.00 USD | 191.05 USD |
| `7D` | `1.32` | 2,480.00 USD | 0.00 USD | 2,480.00 USD | 0.00 USD | 0.00 USD | 1,410.00 USD |
| `1D` | `1.32` | 521.14 USD | 0.00 USD | 521.14 USD | 0.00 USD | 0.00 USD | 456.63 USD |
| `7D` | `1.33` | 1,070.00 USD | 0.00 USD | 1,070.00 USD | 0.00 USD | 0.00 USD | 728.50 USD |
| `1D` | `1.33` | 64.51 USD | 0.00 USD | 64.51 USD | 0.00 USD | 0.00 USD | 64.51 USD |
| `7D` | `1.33` | 343.07 USD | 0.00 USD | 343.07 USD | 0.00 USD | 0.00 USD | 343.07 USD |
| `1D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 3,240.00 USD | 3,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,240.00 USD |
| `7D` | `1.34` | 3,400.00 USD | 3,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 158.18 USD |
| `1D` | `1.34` | 26.34 USD | 26.34 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.34 USD |
| `7D` | `1.35` | 4,280.00 USD | 4,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 880.93 USD |
| `1D` | `1.35` | 318.09 USD | 318.09 USD | 0.00 USD | 0.00 USD | 0.00 USD | 291.75 USD |
| `7D` | `1.35` | 10,250.00 USD | 10,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,970.00 USD |
| `1D` | `1.35` | 557.62 USD | 557.62 USD | 0.00 USD | 0.00 USD | 0.00 USD | 239.53 USD |
| `7D` | `1.35` | 19,220.00 USD | 19,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,980.00 USD |
| `1D` | `1.35` | 6,500.00 USD | 6,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,940.00 USD |
| `7D` | `1.35` | 22,170.00 USD | 22,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD |
| `1D` | `1.35` | 8,740.00 USD | 8,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,240.00 USD |
| `7D` | `1.35` | 22,600.00 USD | 22,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 432.04 USD |
| `1D` | `1.35` | 9,190.00 USD | 9,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 456.63 USD |
| `7D` | `1.35` | 24,210.00 USD | 24,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,610.00 USD |
| `1D` | `1.35` | 9,260.00 USD | 9,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 64.51 USD |
| `7D` | `1.35` | 24,730.00 USD | 24,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 516.86 USD |
| `7D` | `1.36` | 26,380.00 USD | 26,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,660.00 USD |
| `7D` | `1.36` | 26,770.00 USD | 26,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 385.39 USD |
| `1D` | `1.36` | 9,270.00 USD | 9,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.17 USD |
| `7D` | `1.36` | 28,080.00 USD | 28,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD |
| `1D` | `1.36` | 9,420.00 USD | 9,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 149.50 USD |
| `7D` | `1.36` | 30,310.00 USD | 30,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,230.00 USD |
| `1D` | `1.36` | 10,080.00 USD | 10,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 662.23 USD |
| `7D` | `1.36` | 35,650.00 USD | 35,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,340.00 USD |
| `1D` | `1.36` | 13,600.00 USD | 13,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,520.00 USD |
| `7D` | `1.36` | 35,890.00 USD | 35,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 242.94 USD |
| `1D` | `1.36` | 13,630.00 USD | 13,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.44 USD |
| `7D` | `1.37` | 36,670.00 USD | 36,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 778.05 USD |
| `1D` | `1.37` | 13,890.00 USD | 13,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 260.57 USD |
| `7D` | `1.37` | 36,930.00 USD | 36,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 257.94 USD |
| `7D` | `1.37` | 37,090.00 USD | 37,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 160.16 USD |
| `7D` | `1.38` | 37,920.00 USD | 37,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 829.42 USD |
| `7D` | `1.38` | 38,110.00 USD | 38,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 192.71 USD |
| `1D` | `1.39` | 13,890.00 USD | 13,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6.59 USD |
| `7D` | `1.39` | 38,770.00 USD | 38,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 656.92 USD |
| `1D` | `1.39` | 13,970.00 USD | 13,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 74.75 USD |
| `7D` | `1.39` | 39,840.00 USD | 39,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,070.00 USD |
| `1D` | `1.39` | 14,300.00 USD | 14,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 327.85 USD |
| `7D` | `1.39` | 42,550.00 USD | 42,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,710.00 USD |
| `1D` | `1.39` | 16,060.00 USD | 16,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,760.00 USD |
| `7D` | `1.39` | 42,660.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 106.24 USD |
| `1D` | `1.39` | 16,070.00 USD | 16,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.22 USD |
| `7D` | `1.39` | 43,040.00 USD | 43,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 382.02 USD |
| `1D` | `1.39` | 16,200.00 USD | 16,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 130.29 USD |
| `7D` | `1.39` | 43,180.00 USD | 43,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 145.50 USD |
| `7D` | `1.39` | 43,270.00 USD | 43,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 85.77 USD |
| `7D` | `1.46` | 43,600.00 USD | 43,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 331.77 USD |
| `7D` | `1.46` | 43,650.00 USD | 43,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 48.18 USD |
| `1D` | `1.46` | 16,210.00 USD | 16,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2.63 USD |
| `7D` | `1.47` | 43,720.00 USD | 43,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 66.99 USD |
| `1D` | `1.47` | 16,240.00 USD | 16,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.91 USD |
| `7D` | `1.47` | 44,320.00 USD | 44,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 605.48 USD |
| `1D` | `1.47` | 16,300.00 USD | 16,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65.84 USD |
| `7D` | `1.47` | 45,240.00 USD | 45,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 921.56 USD |
| `1D` | `1.47` | 16,890.00 USD | 16,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 584.72 USD |
| `7D` | `1.47` | 45,280.00 USD | 45,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33.49 USD |
| `1D` | `1.47` | 16,910.00 USD | 16,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19.11 USD |
| `7D` | `1.47` | 45,310.00 USD | 45,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31.50 USD |
| `1D` | `1.47` | 16,950.00 USD | 16,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44.12 USD |
| `1D` | `1.47` | 16,960.00 USD | 16,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6.45 USD |
| `7D` | `1.47` | 45,450.00 USD | 45,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 139.54 USD |
| `7D` | `1.47` | 45,470.00 USD | 45,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17.37 USD |

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
| **USDT MEXC** | `0.0200%` | **USDT BingX** | `-` |
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
| `16:50:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 1,112.37 USD | 531.36 USD | 581.01 USD | -49.66 USD | `-4.46%` | `0B / 1S` |
| `16:55:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 1,295.11 USD | 938.30 USD | 356.82 USD | 581.48 USD | `+44.90%` | `1B / 0S` |
| `17:00:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.33` | 16,646.79 USD | 15,263.16 USD | 1,383.63 USD | 13,879.53 USD | `+83.38%` | `1B / 0S` |
| `17:00:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 1,617.41 USD | 715.39 USD | 902.02 USD | -186.62 USD | `-11.54%` | `0B / 1S` |
| `17:00:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 4,873.56 USD | 3,063.79 USD | 1,809.77 USD | 1,254.01 USD | `+25.73%` | `1B / 0S` |
| `17:05:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 1,609.45 USD | 1,528.98 USD | 80.47 USD | 1,448.51 USD | `+90.00%` | `1B / 0S` |
| `17:10:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 1,646.29 USD | 407.10 USD | 1,239.19 USD | -832.09 USD | `-50.54%` | `0B / 1S` |
| `17:15:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 4,810.08 USD | 4,143.98 USD | 666.10 USD | 3,477.88 USD | `+72.30%` | `1B / 0S` |
| `17:15:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 1,521.41 USD | 1,256.65 USD | 264.76 USD | 991.90 USD | `+65.20%` | `1B / 0S` |
| `17:20:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 1,607.46 USD | 1,087.19 USD | 520.27 USD | 566.92 USD | `+35.27%` | `1B / 0S` |

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
  * `2026-10-29 23:01:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:02:06 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1.33` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1.33` (Risk Distance: `0.0013` pts)
  * +2.5R Take Profit: `1.33`
  * Mathematical Lot Sizing: **`0.07 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.33` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.33` (Risk Distance: `0.0013` pts)
  * +2.5R Take Profit: `1.33`
  * Mathematical Lot Sizing: **`0.07 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.35`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
