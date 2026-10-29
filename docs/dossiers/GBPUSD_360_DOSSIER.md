# 🏛️ SOVEREIGN CANDIDATE DOSSIER: GBPUSD
**Canonical Key**: `GBPUSD` | **Broker Instrument**: `GBPUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 00:14:11 IST` (`2026-10-29 18:44:11 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.34` | **Live Ask Quote**: `1.34` | **Mid Price**: `1.34`
- **Spread Points**: `6.00` | **Spread BPS**: `0.45 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `1.33` | VWAP Z-Score: `+1.48` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000911` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `59.64` (State: `NEUTRAL`)
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
  * Institutional Anchors: EMA-144=`1.33` | EMA-200=`1.33` (Slope: `+0.0418`) | EMA-233=`1.33`
- **Range Boundaries**: 24H High=`1.34` | 24H Low=`1.33` | Weekly High=`1.34` | Weekly Low=`1.33`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.33` (Distance: `+0.21%`)
  * Point of Control (POC) = `1.33` (Distance: `+0.31%`)
  * Value Area Low (VAL) = `1.33` (Distance: `+0.44%`)
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
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `983` | 1,314.46 USD | -644.59 USD | `-49.04%` | 8,718.16 USD | `-1.49` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `877` | 1,172.11 USD | -764.42 USD | `-65.22%` | 7,953.74 USD | `-1.53` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `743` | 993.38 USD | 719.84 USD | `+72.46%` | 8,673.59 USD | `+0.57` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `2,145` | 2,868.34 USD | 2,575.16 USD | `+89.78%` | 17,745.99 USD | `+1.16` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `2,289` | 3,060.83 USD | -635.71 USD | `-20.77%` | 17,110.28 USD | `-0.79` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `2,402` | 3,211.69 USD | 388.08 USD | `+12.08%` | 17,498.36 USD | `-0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `1.33` | `1.33` | `1.33` | `1.33` | `12,725` | 16,955.04 USD | 5,816.29 USD | `+34.30%` | 14,155.26 USD | `+1.21` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.33` | `1.34` | `1.33` | `1.34` | `12,464` | 16,646.79 USD | 13,879.53 USD | `+83.38%` | 28,034.80 USD | `+2.56` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.34` | `1.34` | `1.34` | `1.34` | `9,181` | 12,279.59 USD | 8,466.97 USD | `+68.95%` | 36,501.77 USD | `+1.64` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `1D` | `1.21` | 16,260.00 USD | 0.00 USD | 16,260.00 USD | 0.00 USD | 0.00 USD | 51.11 USD |
| `7D` | `1.21` | 43,360.00 USD | 0.00 USD | 43,360.00 USD | 0.00 USD | 0.00 USD | 57.59 USD |
| `7D` | `1.21` | 43,300.00 USD | 0.00 USD | 43,300.00 USD | 0.00 USD | 0.00 USD | 34.30 USD |
| `7D` | `1.28` | 43,270.00 USD | 0.00 USD | 43,270.00 USD | 0.00 USD | 0.00 USD | 829.42 USD |
| `7D` | `1.28` | 42,440.00 USD | 0.00 USD | 42,440.00 USD | 0.00 USD | 0.00 USD | 192.71 USD |
| `1D` | `1.28` | 16,210.00 USD | 0.00 USD | 16,210.00 USD | 0.00 USD | 0.00 USD | 79.53 USD |
| `7D` | `1.28` | 42,250.00 USD | 0.00 USD | 42,250.00 USD | 0.00 USD | 0.00 USD | 656.92 USD |
| `1D` | `1.28` | 16,130.00 USD | 0.00 USD | 16,130.00 USD | 0.00 USD | 0.00 USD | 59.87 USD |
| `7D` | `1.28` | 41,590.00 USD | 0.00 USD | 41,590.00 USD | 0.00 USD | 0.00 USD | 1,670.00 USD |
| `1D` | `1.28` | 16,070.00 USD | 0.00 USD | 16,070.00 USD | 0.00 USD | 0.00 USD | 2,000.00 USD |
| `7D` | `1.28` | 39,920.00 USD | 0.00 USD | 39,920.00 USD | 0.00 USD | 0.00 USD | 2,120.00 USD |
| `1D` | `1.28` | 14,080.00 USD | 0.00 USD | 14,080.00 USD | 0.00 USD | 0.00 USD | 47.77 USD |
| `7D` | `1.28` | 37,810.00 USD | 0.00 USD | 37,810.00 USD | 0.00 USD | 0.00 USD | 153.00 USD |
| `1D` | `1.28` | 14,030.00 USD | 0.00 USD | 14,030.00 USD | 0.00 USD | 0.00 USD | 115.48 USD |
| `7D` | `1.29` | 37,650.00 USD | 0.00 USD | 37,650.00 USD | 0.00 USD | 0.00 USD | 437.32 USD |
| `1D` | `1.29` | 13,910.00 USD | 0.00 USD | 13,910.00 USD | 0.00 USD | 0.00 USD | 16.13 USD |
| `7D` | `1.29` | 37,220.00 USD | 0.00 USD | 37,220.00 USD | 0.00 USD | 0.00 USD | 112.68 USD |
| `7D` | `1.29` | 37,100.00 USD | 0.00 USD | 37,100.00 USD | 0.00 USD | 0.00 USD | 16.53 USD |
| `7D` | `1.30` | 37,090.00 USD | 0.00 USD | 37,090.00 USD | 0.00 USD | 0.00 USD | 1,660.00 USD |
| `7D` | `1.30` | 35,430.00 USD | 0.00 USD | 35,430.00 USD | 0.00 USD | 0.00 USD | 385.39 USD |
| `1D` | `1.31` | 13,900.00 USD | 0.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD | 13.17 USD |
| `7D` | `1.31` | 35,040.00 USD | 0.00 USD | 35,040.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD |
| `1D` | `1.31` | 13,880.00 USD | 0.00 USD | 13,880.00 USD | 0.00 USD | 0.00 USD | 253.19 USD |
| `7D` | `1.31` | 33,730.00 USD | 0.00 USD | 33,730.00 USD | 0.00 USD | 0.00 USD | 3,330.00 USD |
| `1D` | `1.31` | 13,630.00 USD | 0.00 USD | 13,630.00 USD | 0.00 USD | 0.00 USD | 2,980.00 USD |
| `7D` | `1.31` | 30,400.00 USD | 0.00 USD | 30,400.00 USD | 0.00 USD | 0.00 USD | 4,230.00 USD |
| `1D` | `1.31` | 10,650.00 USD | 0.00 USD | 10,650.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD |
| `7D` | `1.31` | 26,160.00 USD | 0.00 USD | 26,160.00 USD | 0.00 USD | 0.00 USD | 290.42 USD |
| `1D` | `1.31` | 9,530.00 USD | 0.00 USD | 9,530.00 USD | 0.00 USD | 0.00 USD | 230.96 USD |
| `7D` | `1.31` | 25,870.00 USD | 0.00 USD | 25,870.00 USD | 0.00 USD | 0.00 USD | 879.35 USD |
| `1D` | `1.31` | 9,300.00 USD | 0.00 USD | 9,300.00 USD | 0.00 USD | 0.00 USD | 32.26 USD |
| `7D` | `1.31` | 24,990.00 USD | 0.00 USD | 24,990.00 USD | 0.00 USD | 0.00 USD | 222.30 USD |
| `7D` | `1.31` | 24,770.00 USD | 0.00 USD | 24,770.00 USD | 0.00 USD | 0.00 USD | 47.02 USD |
| `7D` | `1.32` | 24,730.00 USD | 0.00 USD | 24,730.00 USD | 0.00 USD | 0.00 USD | 3,240.00 USD |
| `7D` | `1.32` | 21,480.00 USD | 0.00 USD | 21,480.00 USD | 0.00 USD | 0.00 USD | 158.18 USD |
| `1D` | `1.32` | 9,260.00 USD | 0.00 USD | 9,260.00 USD | 0.00 USD | 0.00 USD | 26.34 USD |
| `7D` | `1.32` | 21,330.00 USD | 0.00 USD | 21,330.00 USD | 0.00 USD | 0.00 USD | 880.93 USD |
| `1D` | `1.32` | 9,240.00 USD | 0.00 USD | 9,240.00 USD | 0.00 USD | 0.00 USD | 298.99 USD |
| `7D` | `1.32` | 20,440.00 USD | 0.00 USD | 20,440.00 USD | 0.00 USD | 0.00 USD | 5,970.00 USD |
| `1D` | `1.32` | 8,940.00 USD | 0.00 USD | 8,940.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD |
| `7D` | `1.32` | 14,480.00 USD | 0.00 USD | 14,480.00 USD | 0.00 USD | 0.00 USD | 9,780.00 USD |
| `1D` | `1.32` | 7,630.00 USD | 0.00 USD | 7,630.00 USD | 0.00 USD | 0.00 USD | 7,050.00 USD |
| `7D` | `1.32` | 4,700.00 USD | 0.00 USD | 4,700.00 USD | 0.00 USD | 0.00 USD | 2,220.00 USD |
| `1D` | `1.32` | 579.32 USD | 0.00 USD | 579.32 USD | 0.00 USD | 0.00 USD | 52.87 USD |
| `7D` | `1.32` | 2,480.00 USD | 0.00 USD | 2,480.00 USD | 0.00 USD | 0.00 USD | 1,410.00 USD |
| `1D` | `1.33` | 526.45 USD | 0.00 USD | 526.45 USD | 0.00 USD | 0.00 USD | 526.45 USD |
| `7D` | `1.33` | 1,070.00 USD | 0.00 USD | 1,070.00 USD | 0.00 USD | 0.00 USD | 728.50 USD |
| `7D` | `1.33` | 343.07 USD | 0.00 USD | 343.07 USD | 0.00 USD | 0.00 USD | 343.07 USD |
| `1D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 3,240.00 USD | 3,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,240.00 USD |
| `7D` | `1.34` | 3,400.00 USD | 3,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 158.18 USD |
| `1D` | `1.34` | 26.34 USD | 26.34 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.34 USD |
| `7D` | `1.35` | 4,280.00 USD | 4,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 880.93 USD |
| `1D` | `1.35` | 325.33 USD | 325.33 USD | 0.00 USD | 0.00 USD | 0.00 USD | 298.99 USD |
| `7D` | `1.35` | 10,250.00 USD | 10,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,970.00 USD |
| `1D` | `1.35` | 1,640.00 USD | 1,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD |
| `7D` | `1.35` | 19,220.00 USD | 19,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,980.00 USD |
| `1D` | `1.35` | 8,670.00 USD | 8,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,040.00 USD |
| `7D` | `1.35` | 22,170.00 USD | 22,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD |
| `1D` | `1.35` | 8,740.00 USD | 8,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 63.02 USD |
| `7D` | `1.35` | 22,600.00 USD | 22,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 432.04 USD |
| `1D` | `1.35` | 9,260.00 USD | 9,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 526.45 USD |
| `7D` | `1.35` | 24,210.00 USD | 24,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,610.00 USD |
| `7D` | `1.35` | 24,730.00 USD | 24,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 516.86 USD |
| `7D` | `1.36` | 26,380.00 USD | 26,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,660.00 USD |
| `7D` | `1.36` | 26,770.00 USD | 26,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 385.39 USD |
| `1D` | `1.36` | 9,280.00 USD | 9,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.17 USD |
| `7D` | `1.36` | 28,080.00 USD | 28,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD |
| `1D` | `1.36` | 9,520.00 USD | 9,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 246.15 USD |
| `7D` | `1.36` | 30,310.00 USD | 30,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,230.00 USD |
| `1D` | `1.36` | 12,510.00 USD | 12,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,990.00 USD |
| `7D` | `1.36` | 35,650.00 USD | 35,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,340.00 USD |
| `1D` | `1.36` | 13,630.00 USD | 13,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD |
| `7D` | `1.36` | 35,890.00 USD | 35,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 242.94 USD |
| `1D` | `1.36` | 13,630.00 USD | 13,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.49 USD |
| `7D` | `1.37` | 36,670.00 USD | 36,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 778.05 USD |
| `1D` | `1.37` | 13,900.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 262.73 USD |
| `7D` | `1.37` | 36,930.00 USD | 36,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 257.94 USD |
| `7D` | `1.37` | 37,090.00 USD | 37,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 160.16 USD |
| `7D` | `1.38` | 37,920.00 USD | 37,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 829.42 USD |
| `7D` | `1.38` | 38,110.00 USD | 38,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 192.71 USD |
| `1D` | `1.39` | 13,900.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6.59 USD |
| `7D` | `1.39` | 38,770.00 USD | 38,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 656.92 USD |
| `1D` | `1.39` | 14,030.00 USD | 14,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 123.06 USD |
| `7D` | `1.39` | 39,840.00 USD | 39,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,070.00 USD |
| `1D` | `1.39` | 15,520.00 USD | 15,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,490.00 USD |
| `7D` | `1.39` | 42,550.00 USD | 42,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,710.00 USD |
| `1D` | `1.39` | 16,080.00 USD | 16,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 557.26 USD |
| `7D` | `1.39` | 42,660.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 106.24 USD |
| `1D` | `1.39` | 16,080.00 USD | 16,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2.92 USD |
| `7D` | `1.39` | 43,040.00 USD | 43,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 382.02 USD |
| `1D` | `1.39` | 16,210.00 USD | 16,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 131.61 USD |
| `7D` | `1.39` | 43,180.00 USD | 43,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 145.50 USD |
| `7D` | `1.39` | 43,270.00 USD | 43,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 85.77 USD |
| `7D` | `1.46` | 43,600.00 USD | 43,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 331.77 USD |
| `7D` | `1.46` | 43,650.00 USD | 43,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 48.18 USD |
| `1D` | `1.47` | 16,210.00 USD | 16,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2.63 USD |
| `7D` | `1.47` | 43,720.00 USD | 43,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 66.99 USD |
| `1D` | `1.47` | 16,260.00 USD | 16,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 40.90 USD |
| `7D` | `1.47` | 44,320.00 USD | 44,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 605.48 USD |
| `1D` | `1.47` | 16,450.00 USD | 16,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 195.68 USD |
| `7D` | `1.47` | 45,240.00 USD | 45,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 921.56 USD |
| `1D` | `1.47` | 16,910.00 USD | 16,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 457.71 USD |
| `7D` | `1.47` | 45,280.00 USD | 45,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33.49 USD |
| `1D` | `1.47` | 16,910.00 USD | 16,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.29 USD |
| `7D` | `1.47` | 45,310.00 USD | 45,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31.50 USD |
| `1D` | `1.47` | 16,960.00 USD | 16,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 49.42 USD |
| `1D` | `1.47` | 16,970.00 USD | 16,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1.69 USD |
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
| `18:00:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 1,034.07 USD | 864.55 USD | 169.52 USD | 695.03 USD | `+67.21%` | `1B / 0S` |
| `18:05:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 872.87 USD | 788.31 USD | 84.56 USD | 703.75 USD | `+80.63%` | `1B / 0S` |
| `18:10:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 960.12 USD | 820.57 USD | 139.55 USD | 681.02 USD | `+70.93%` | `1B / 0S` |
| `18:15:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 819.76 USD | 428.80 USD | 390.96 USD | 37.84 USD | `+4.62%` | `1B / 0S` |
| `18:15:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 3,060.83 USD | 1,212.56 USD | 1,848.27 USD | -635.71 USD | `-20.77%` | `0B / 1S` |
| `18:20:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 926.82 USD | 572.45 USD | 354.37 USD | 218.07 USD | `+23.53%` | `1B / 0S` |
| `18:25:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 1,314.46 USD | 334.93 USD | 979.52 USD | -644.59 USD | `-49.04%` | `0B / 1S` |
| `18:30:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 3,211.69 USD | 1,799.88 USD | 1,411.81 USD | 388.08 USD | `+12.08%` | `1B / 0S` |
| `18:30:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 1,172.11 USD | 203.85 USD | 968.27 USD | -764.42 USD | `-65.22%` | `0B / 1S` |
| `18:35:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 993.38 USD | 856.61 USD | 136.77 USD | 719.84 USD | `+72.46%` | `1B / 0S` |

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
  * `2026-10-29 23:31:18 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:18 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:10:18 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:10:18 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.33` (Risk Distance: `0.0012` pts)
  * +2.5R Take Profit: `1.33`
  * Mathematical Lot Sizing: **`0.08 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.33` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.33` (Risk Distance: `0.0012` pts)
  * +2.5R Take Profit: `1.33`
  * Mathematical Lot Sizing: **`0.08 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.35`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
