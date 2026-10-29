# 🏛️ SOVEREIGN CANDIDATE DOSSIER: GBPUSD
**Canonical Key**: `GBPUSD` | **Broker Instrument**: `GBPUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 01:36:03 IST` (`2026-10-29 20:06:03 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.34` | **Live Ask Quote**: `1.34` | **Mid Price**: `1.34`
- **Spread Points**: `7.00` | **Spread BPS**: `0.52 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `1.33` | VWAP Z-Score: `+1.44` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000741` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `58.01` (State: `NEUTRAL`)
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
  * Institutional Anchors: EMA-144=`1.33` | EMA-200=`1.33` (Slope: `+0.0368`) | EMA-233=`1.33`
- **Range Boundaries**: 24H High=`1.34` | 24H Low=`1.33` | Weekly High=`1.34` | Weekly Low=`1.33`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.33` (Distance: `+0.23%`)
  * Point of Control (POC) = `1.33` (Distance: `+0.36%`)
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
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `457` | 610.72 USD | -310.54 USD | `-50.85%` | 7,189.64 USD | `-0.52` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `531` | 709.84 USD | 637.24 USD | `+89.77%` | 7,826.87 USD | `+1.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `504` | 673.76 USD | -238.62 USD | `-35.42%` | 7,588.25 USD | `-0.37` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `1,418` | 1,895.44 USD | -279.46 USD | `-14.74%` | 15,434.09 USD | `-0.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `1,589` | 2,124.16 USD | 1,114.31 USD | `+52.46%` | 16,548.41 USD | `+0.25` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `1,553` | 2,076.25 USD | -224.46 USD | `-10.81%` | 16,323.95 USD | `-0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `9,181` | 12,279.59 USD | 8,466.97 USD | `+68.95%` | 36,740.80 USD | `+1.64` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `6,560` | 8,769.34 USD | -3,203.17 USD | `-36.53%` | 33,537.62 USD | `-0.90` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `5,661` | 7,567.79 USD | -1,435.27 USD | `-18.97%` | 32,102.35 USD | `-0.50` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.33` | `1.33` | `1.33` | `1.33` | `23,876` | 31,800.92 USD | 4,068.43 USD | `+12.79%` | -7,908.43 USD | `+1.38` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `1.33` | `1.34` | `1.33` | `1.34` | `40,930` | 54,714.81 USD | 35,923.87 USD | `+65.66%` | 28,015.44 USD | `+1.94` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `13,076` | 17,481.17 USD | 2,417.61 USD | `+13.83%` | 30,433.05 USD | `-0.19` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `1.33` | `1.33` | `1.33` | `1.33` | `17,244` | 22,969.01 USD | -1,056.57 USD | `-4.60%` | -3,726.39 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.33` | `1.33` | `1.33` | `1.33` | `17,831` | 23,736.63 USD | -8,250.46 USD | `-34.76%` | -11,976.86 USD | `-1.38` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.33` | `1.33` | `1.33` | `1.33` | `23,876` | 31,800.92 USD | 4,068.43 USD | `+12.79%` | -7,908.43 USD | `+1.38` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `1.33` | `1.34` | `1.33` | `1.34` | `40,930` | 54,714.81 USD | 35,923.87 USD | `+65.66%` | 28,015.44 USD | `+1.94` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.34` | `1.34` | `1.34` | `1.34` | `13,076` | 17,481.17 USD | 2,417.61 USD | `+13.83%` | 30,433.05 USD | `-0.19` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `7D` | `1.20` | 45,010.00 USD | 0.00 USD | 45,010.00 USD | 0.00 USD | 0.00 USD | 56.90 USD |
| `7D` | `1.20` | 44,950.00 USD | 0.00 USD | 44,950.00 USD | 0.00 USD | 0.00 USD | 745.17 USD |
| `7D` | `1.20` | 44,210.00 USD | 0.00 USD | 44,210.00 USD | 0.00 USD | 0.00 USD | 819.05 USD |
| `7D` | `1.20` | 43,390.00 USD | 0.00 USD | 43,390.00 USD | 0.00 USD | 0.00 USD | 143.85 USD |
| `1D` | `1.21` | 15,020.00 USD | 0.00 USD | 15,020.00 USD | 0.00 USD | 0.00 USD | 51.19 USD |
| `7D` | `1.21` | 43,250.00 USD | 0.00 USD | 43,250.00 USD | 0.00 USD | 0.00 USD | 52.16 USD |
| `7D` | `1.21` | 43,190.00 USD | 0.00 USD | 43,190.00 USD | 0.00 USD | 0.00 USD | 25.42 USD |
| `7D` | `1.28` | 43,170.00 USD | 0.00 USD | 43,170.00 USD | 0.00 USD | 0.00 USD | 19.09 USD |
| `7D` | `1.28` | 43,150.00 USD | 0.00 USD | 43,150.00 USD | 0.00 USD | 0.00 USD | 957.15 USD |
| `1D` | `1.28` | 14,970.00 USD | 0.00 USD | 14,970.00 USD | 0.00 USD | 0.00 USD | 72.94 USD |
| `7D` | `1.28` | 42,190.00 USD | 0.00 USD | 42,190.00 USD | 0.00 USD | 0.00 USD | 141.96 USD |
| `1D` | `1.28` | 14,900.00 USD | 0.00 USD | 14,900.00 USD | 0.00 USD | 0.00 USD | 35.30 USD |
| `7D` | `1.28` | 42,050.00 USD | 0.00 USD | 42,050.00 USD | 0.00 USD | 0.00 USD | 1,910.00 USD |
| `1D` | `1.28` | 14,870.00 USD | 0.00 USD | 14,870.00 USD | 0.00 USD | 0.00 USD | 1,850.00 USD |
| `7D` | `1.28` | 40,140.00 USD | 0.00 USD | 40,140.00 USD | 0.00 USD | 0.00 USD | 2,430.00 USD |
| `1D` | `1.28` | 13,020.00 USD | 0.00 USD | 13,020.00 USD | 0.00 USD | 0.00 USD | 47.77 USD |
| `7D` | `1.28` | 37,710.00 USD | 0.00 USD | 37,710.00 USD | 0.00 USD | 0.00 USD | 174.22 USD |
| `1D` | `1.28` | 12,970.00 USD | 0.00 USD | 12,970.00 USD | 0.00 USD | 0.00 USD | 118.22 USD |
| `7D` | `1.29` | 37,530.00 USD | 0.00 USD | 37,530.00 USD | 0.00 USD | 0.00 USD | 445.78 USD |
| `1D` | `1.29` | 12,850.00 USD | 0.00 USD | 12,850.00 USD | 0.00 USD | 0.00 USD | 16.13 USD |
| `7D` | `1.29` | 37,090.00 USD | 0.00 USD | 37,090.00 USD | 0.00 USD | 0.00 USD | 66.68 USD |
| `7D` | `1.29` | 37,020.00 USD | 0.00 USD | 37,020.00 USD | 0.00 USD | 0.00 USD | 16.35 USD |
| `7D` | `1.30` | 37,000.00 USD | 0.00 USD | 37,000.00 USD | 0.00 USD | 0.00 USD | 38.18 USD |
| `7D` | `1.30` | 36,960.00 USD | 0.00 USD | 36,960.00 USD | 0.00 USD | 0.00 USD | 1,910.00 USD |
| `1D` | `1.31` | 12,830.00 USD | 0.00 USD | 12,830.00 USD | 0.00 USD | 0.00 USD | 145.88 USD |
| `7D` | `1.31` | 35,050.00 USD | 0.00 USD | 35,050.00 USD | 0.00 USD | 0.00 USD | 283.92 USD |
| `1D` | `1.31` | 12,690.00 USD | 0.00 USD | 12,690.00 USD | 0.00 USD | 0.00 USD | 70.63 USD |
| `7D` | `1.31` | 34,770.00 USD | 0.00 USD | 34,770.00 USD | 0.00 USD | 0.00 USD | 3,830.00 USD |
| `1D` | `1.31` | 12,620.00 USD | 0.00 USD | 12,620.00 USD | 0.00 USD | 0.00 USD | 3,700.00 USD |
| `7D` | `1.31` | 30,940.00 USD | 0.00 USD | 30,940.00 USD | 0.00 USD | 0.00 USD | 4,860.00 USD |
| `1D` | `1.31` | 8,920.00 USD | 0.00 USD | 8,920.00 USD | 0.00 USD | 0.00 USD | 95.54 USD |
| `7D` | `1.31` | 26,070.00 USD | 0.00 USD | 26,070.00 USD | 0.00 USD | 0.00 USD | 242.14 USD |
| `1D` | `1.31` | 8,820.00 USD | 0.00 USD | 8,820.00 USD | 0.00 USD | 0.00 USD | 236.43 USD |
| `7D` | `1.31` | 25,830.00 USD | 0.00 USD | 25,830.00 USD | 0.00 USD | 0.00 USD | 922.75 USD |
| `1D` | `1.31` | 8,590.00 USD | 0.00 USD | 8,590.00 USD | 0.00 USD | 0.00 USD | 32.26 USD |
| `7D` | `1.31` | 24,910.00 USD | 0.00 USD | 24,910.00 USD | 0.00 USD | 0.00 USD | 208.43 USD |
| `7D` | `1.31` | 24,700.00 USD | 0.00 USD | 24,700.00 USD | 0.00 USD | 0.00 USD | 32.69 USD |
| `7D` | `1.32` | 24,670.00 USD | 0.00 USD | 24,670.00 USD | 0.00 USD | 0.00 USD | 3,400.00 USD |
| `7D` | `1.32` | 21,270.00 USD | 0.00 USD | 21,270.00 USD | 0.00 USD | 0.00 USD | 694.76 USD |
| `1D` | `1.32` | 8,560.00 USD | 0.00 USD | 8,560.00 USD | 0.00 USD | 0.00 USD | 298.99 USD |
| `7D` | `1.32` | 20,570.00 USD | 0.00 USD | 20,570.00 USD | 0.00 USD | 0.00 USD | 1,240.00 USD |
| `1D` | `1.32` | 8,260.00 USD | 0.00 USD | 8,260.00 USD | 0.00 USD | 0.00 USD | 631.91 USD |
| `7D` | `1.32` | 19,330.00 USD | 0.00 USD | 19,330.00 USD | 0.00 USD | 0.00 USD | 13,950.00 USD |
| `1D` | `1.32` | 7,630.00 USD | 0.00 USD | 7,630.00 USD | 0.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `1.32` | 5,380.00 USD | 0.00 USD | 5,380.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD |
| `1D` | `1.32` | 590.27 USD | 0.00 USD | 590.27 USD | 0.00 USD | 0.00 USD | 52.87 USD |
| `7D` | `1.32` | 2,440.00 USD | 0.00 USD | 2,440.00 USD | 0.00 USD | 0.00 USD | 1,490.00 USD |
| `1D` | `1.33` | 537.40 USD | 0.00 USD | 537.40 USD | 0.00 USD | 0.00 USD | 537.40 USD |
| `7D` | `1.33` | 947.24 USD | 0.00 USD | 947.24 USD | 0.00 USD | 0.00 USD | 647.69 USD |
| `7D` | `1.33` | 299.55 USD | 0.00 USD | 299.55 USD | 0.00 USD | 0.00 USD | 299.55 USD |
| `1D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 3,400.00 USD | 3,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,400.00 USD |
| `7D` | `1.35` | 4,100.00 USD | 4,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 694.76 USD |
| `1D` | `1.35` | 298.99 USD | 298.99 USD | 0.00 USD | 0.00 USD | 0.00 USD | 298.99 USD |
| `7D` | `1.35` | 5,340.00 USD | 5,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240.00 USD |
| `1D` | `1.35` | 930.90 USD | 930.90 USD | 0.00 USD | 0.00 USD | 0.00 USD | 631.91 USD |
| `7D` | `1.35` | 12,610.00 USD | 12,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,270.00 USD |
| `1D` | `1.35` | 7,970.00 USD | 7,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `1.35` | 22,120.00 USD | 22,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,510.00 USD |
| `1D` | `1.35` | 8,020.00 USD | 8,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 52.87 USD |
| `7D` | `1.35` | 22,690.00 USD | 22,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 569.14 USD |
| `1D` | `1.35` | 8,560.00 USD | 8,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 537.40 USD |
| `7D` | `1.35` | 24,340.00 USD | 24,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,640.00 USD |
| `7D` | `1.35` | 24,640.00 USD | 24,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 304.12 USD |
| `7D` | `1.36` | 24,670.00 USD | 24,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 27.93 USD |
| `7D` | `1.36` | 24,710.00 USD | 24,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 38.18 USD |
| `7D` | `1.36` | 26,620.00 USD | 26,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,910.00 USD |
| `7D` | `1.36` | 26,900.00 USD | 26,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 283.92 USD |
| `1D` | `1.36` | 8,750.00 USD | 8,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 197.01 USD |
| `7D` | `1.36` | 28,940.00 USD | 28,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,030.00 USD |
| `1D` | `1.36` | 11,450.00 USD | 11,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,690.00 USD |
| `7D` | `1.36` | 35,210.00 USD | 35,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,270.00 USD |
| `1D` | `1.36` | 12,570.00 USD | 12,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD |
| `7D` | `1.36` | 35,840.00 USD | 35,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 632.03 USD |
| `1D` | `1.36` | 12,790.00 USD | 12,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 221.08 USD |
| `7D` | `1.37` | 36,660.00 USD | 36,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 818.81 USD |
| `1D` | `1.37` | 12,830.00 USD | 12,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 47.61 USD |
| `7D` | `1.37` | 36,890.00 USD | 36,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 232.91 USD |
| `7D` | `1.37` | 37,000.00 USD | 37,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 112.15 USD |
| `7D` | `1.38` | 37,020.00 USD | 37,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19.09 USD |
| `7D` | `1.38` | 37,980.00 USD | 37,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 957.15 USD |
| `7D` | `1.39` | 38,120.00 USD | 38,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 141.96 USD |
| `1D` | `1.39` | 12,930.00 USD | 12,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 98.49 USD |
| `7D` | `1.39` | 38,900.00 USD | 38,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 778.93 USD |
| `1D` | `1.39` | 14,280.00 USD | 14,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,350.00 USD |
| `7D` | `1.39` | 42,270.00 USD | 42,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,370.00 USD |
| `1D` | `1.39` | 14,840.00 USD | 14,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 557.26 USD |
| `7D` | `1.39` | 42,590.00 USD | 42,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 316.02 USD |
| `1D` | `1.39` | 14,840.00 USD | 14,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.16 USD |
| `7D` | `1.39` | 42,950.00 USD | 42,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 361.85 USD |
| `1D` | `1.39` | 14,970.00 USD | 14,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 134.11 USD |
| `7D` | `1.39` | 43,110.00 USD | 43,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 156.54 USD |
| `7D` | `1.39` | 43,170.00 USD | 43,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 63.56 USD |
| `7D` | `1.46` | 43,180.00 USD | 43,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7.64 USD |
| `7D` | `1.46` | 43,550.00 USD | 43,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 374.31 USD |
| `7D` | `1.47` | 43,600.00 USD | 43,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 46.66 USD |
| `1D` | `1.47` | 15,010.00 USD | 15,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 32.39 USD |
| `7D` | `1.47` | 43,900.00 USD | 43,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 301.46 USD |
| `1D` | `1.47` | 15,140.00 USD | 15,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 134.93 USD |
| `7D` | `1.47` | 45,070.00 USD | 45,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,170.00 USD |
| `1D` | `1.47` | 15,600.00 USD | 15,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 457.71 USD |
| `7D` | `1.47` | 45,170.00 USD | 45,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 105.64 USD |
| `1D` | `1.47` | 15,600.00 USD | 15,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.29 USD |
| `7D` | `1.47` | 45,220.00 USD | 45,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44.42 USD |
| `1D` | `1.47` | 15,650.00 USD | 15,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44.74 USD |
| `7D` | `1.47` | 45,360.00 USD | 45,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 144.47 USD |
| `7D` | `1.47` | 45,370.00 USD | 45,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4.53 USD |

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
| `19:15:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 800.89 USD | 41.43 USD | 759.46 USD | -718.04 USD | `-89.66%` | `0B / 1S` |
| `19:20:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 730.17 USD | 638.90 USD | 91.27 USD | 547.62 USD | `+75.00%` | `1B / 0S` |
| `19:25:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 651.07 USD | 122.84 USD | 528.23 USD | -405.38 USD | `-62.26%` | `0B / 1S` |
| `19:30:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 715.10 USD | 81.94 USD | 633.16 USD | -551.22 USD | `-77.08%` | `0B / 1S` |
| `19:30:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 1,895.44 USD | 807.99 USD | 1,087.45 USD | -279.46 USD | `-14.74%` | `0B / 1S` |
| `19:35:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 509.33 USD | 433.97 USD | 75.36 USD | 358.61 USD | `+70.41%` | `1B / 0S` |
| `19:40:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 671.02 USD | 246.39 USD | 424.63 USD | -178.24 USD | `-26.56%` | `0B / 1S` |
| `19:45:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 2,124.16 USD | 1,619.24 USD | 504.92 USD | 1,114.31 USD | `+52.46%` | `1B / 0S` |
| `19:45:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 803.36 USD | 411.72 USD | 391.64 USD | 20.08 USD | `+2.50%` | `1B / 0S` |
| `19:50:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 610.72 USD | 150.09 USD | 460.63 USD | -310.54 USD | `-50.85%` | `0B / 1S` |

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
  * `2026-10-30 00:58:24 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:29:24 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:29:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.33` (Risk Distance: `0.000994` pts)
  * +2.5R Take Profit: `1.33`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.33` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.33` (Risk Distance: `0.000994` pts)
  * +2.5R Take Profit: `1.33`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.35`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
