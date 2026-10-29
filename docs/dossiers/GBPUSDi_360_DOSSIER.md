# 🏛️ SOVEREIGN CANDIDATE DOSSIER: GBPUSD
**Canonical Key**: `GBPUSD` | **Broker Instrument**: `GBPUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-29 22:33:52 IST` (`2026-10-29 17:03:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `1.33` | VWAP Z-Score: `+3.05` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0011` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `68.63` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.33` | Lower -3.00σ Band: `1.33`
  * Upper +2.51σ Band: `1.33` | Lower -2.51σ Band: `1.33`
  * Upper +2.01σ Band: `1.33` | Lower -2.01σ Band: `1.33`
  * Upper +2.00σ Band: `1.33` | Lower -2.00σ Band: `1.33`
  * Upper +1.28σ Band: `1.33` | Lower -1.28σ Band: `1.33`
  * Upper +1.00σ Band: `1.33` | Lower -1.00σ Band: `1.33`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.33` | EMA-20=`1.33` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.33` (Slope: `+0.0000`) | EMA-100=`1.33`
  * Institutional Anchors: EMA-144=`1.33` | EMA-200=`1.33` (Slope: `+0.0068`) | EMA-233=`1.33`
- **Range Boundaries**: 24H High=`1.33` | 24H Low=`1.33` | Weekly High=`1.34` | Weekly Low=`1.33`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.33` (Distance: `+0.28%`)
  * Point of Control (POC) = `1.33` (Distance: `+0.37%`)
  * Value Area Low (VAL) = `1.33` (Distance: `+0.48%`)
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
| `5m` | `1.33` | `1.33` | `1.33` | `1.33` | `835` | 1,112.37 USD | -49.66 USD | `-4.46%` | 3,168.47 USD | `-0.02` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `1.33` | `1.33` | `1.33` | `1.33` | `972` | 1,295.11 USD | 581.48 USD | `+44.90%` | 3,749.95 USD | `+0.78` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.33` | `1.33` | `1.33` | `1.33` | `1,214` | 1,617.41 USD | -186.62 USD | `-11.54%` | 3,563.32 USD | `-0.19` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `1.33` | `1.33` | `1.33` | `1.33` | `3,838` | 5,111.22 USD | -2,183.27 USD | `-42.72%` | 5,313.04 USD | `-1.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `1.33` | `1.33` | `1.33` | `1.33` | `2,916` | 3,885.34 USD | 2,803.62 USD | `+72.16%` | 8,116.67 USD | `+1.76` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.33` | `1.33` | `1.33` | `1.33` | `3,656` | 4,873.56 USD | 1,254.01 USD | `+25.73%` | 9,370.68 USD | `+0.65` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `7D` | `1.20` | 44,020.00 USD | 0.00 USD | 44,020.00 USD | 0.00 USD | 0.00 USD | 305.59 USD |
| `7D` | `1.20` | 43,710.00 USD | 0.00 USD | 43,710.00 USD | 0.00 USD | 0.00 USD | 425.44 USD |
| `1D` | `1.20` | 16,360.00 USD | 0.00 USD | 16,360.00 USD | 0.00 USD | 0.00 USD | 206.67 USD |
| `7D` | `1.20` | 43,290.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD | 0.00 USD | 888.61 USD |
| `1D` | `1.20` | 16,150.00 USD | 0.00 USD | 16,150.00 USD | 0.00 USD | 0.00 USD | 460.90 USD |
| `7D` | `1.20` | 42,400.00 USD | 0.00 USD | 42,400.00 USD | 0.00 USD | 0.00 USD | 50.66 USD |
| `7D` | `1.21` | 42,350.00 USD | 0.00 USD | 42,350.00 USD | 0.00 USD | 0.00 USD | 57.15 USD |
| `7D` | `1.21` | 42,290.00 USD | 0.00 USD | 42,290.00 USD | 0.00 USD | 0.00 USD | 77.77 USD |
| `7D` | `1.21` | 42,210.00 USD | 0.00 USD | 42,210.00 USD | 0.00 USD | 0.00 USD | 6.73 USD |
| `7D` | `1.28` | 42,210.00 USD | 0.00 USD | 42,210.00 USD | 0.00 USD | 0.00 USD | 810.32 USD |
| `1D` | `1.28` | 15,690.00 USD | 0.00 USD | 15,690.00 USD | 0.00 USD | 0.00 USD | 21.38 USD |
| `7D` | `1.28` | 41,400.00 USD | 0.00 USD | 41,400.00 USD | 0.00 USD | 0.00 USD | 86.09 USD |
| `1D` | `1.28` | 15,670.00 USD | 0.00 USD | 15,670.00 USD | 0.00 USD | 0.00 USD | 49.38 USD |
| `7D` | `1.28` | 41,310.00 USD | 0.00 USD | 41,310.00 USD | 0.00 USD | 0.00 USD | 242.38 USD |
| `1D` | `1.28` | 15,620.00 USD | 0.00 USD | 15,620.00 USD | 0.00 USD | 0.00 USD | 74.75 USD |
| `7D` | `1.28` | 41,070.00 USD | 0.00 USD | 41,070.00 USD | 0.00 USD | 0.00 USD | 1,520.00 USD |
| `1D` | `1.28` | 15,540.00 USD | 0.00 USD | 15,540.00 USD | 0.00 USD | 0.00 USD | 331.10 USD |
| `7D` | `1.28` | 39,540.00 USD | 0.00 USD | 39,540.00 USD | 0.00 USD | 0.00 USD | 2,800.00 USD |
| `1D` | `1.28` | 15,210.00 USD | 0.00 USD | 15,210.00 USD | 0.00 USD | 0.00 USD | 1,760.00 USD |
| `7D` | `1.28` | 36,740.00 USD | 0.00 USD | 36,740.00 USD | 0.00 USD | 0.00 USD | 113.97 USD |
| `1D` | `1.28` | 13,460.00 USD | 0.00 USD | 13,460.00 USD | 0.00 USD | 0.00 USD | 7.97 USD |
| `7D` | `1.28` | 36,630.00 USD | 0.00 USD | 36,630.00 USD | 0.00 USD | 0.00 USD | 162.50 USD |
| `7D` | `1.29` | 36,470.00 USD | 0.00 USD | 36,470.00 USD | 0.00 USD | 0.00 USD | 177.57 USD |
| `7D` | `1.29` | 36,290.00 USD | 0.00 USD | 36,290.00 USD | 0.00 USD | 0.00 USD | 113.55 USD |
| `7D` | `1.30` | 36,180.00 USD | 0.00 USD | 36,180.00 USD | 0.00 USD | 0.00 USD | 1,620.00 USD |
| `1D` | `1.30` | 13,450.00 USD | 0.00 USD | 13,450.00 USD | 0.00 USD | 0.00 USD | 42.74 USD |
| `7D` | `1.30` | 34,560.00 USD | 0.00 USD | 34,560.00 USD | 0.00 USD | 0.00 USD | 172.14 USD |
| `1D` | `1.30` | 13,410.00 USD | 0.00 USD | 13,410.00 USD | 0.00 USD | 0.00 USD | 98.76 USD |
| `7D` | `1.31` | 34,380.00 USD | 0.00 USD | 34,380.00 USD | 0.00 USD | 0.00 USD | 484.77 USD |
| `1D` | `1.31` | 13,310.00 USD | 0.00 USD | 13,310.00 USD | 0.00 USD | 0.00 USD | 149.50 USD |
| `7D` | `1.31` | 33,900.00 USD | 0.00 USD | 33,900.00 USD | 0.00 USD | 0.00 USD | 3,050.00 USD |
| `1D` | `1.31` | 13,160.00 USD | 0.00 USD | 13,160.00 USD | 0.00 USD | 0.00 USD | 655.73 USD |
| `7D` | `1.31` | 30,850.00 USD | 0.00 USD | 30,850.00 USD | 0.00 USD | 0.00 USD | 5,600.00 USD |
| `1D` | `1.31` | 12,500.00 USD | 0.00 USD | 12,500.00 USD | 0.00 USD | 0.00 USD | 3,520.00 USD |
| `7D` | `1.31` | 25,250.00 USD | 0.00 USD | 25,250.00 USD | 0.00 USD | 0.00 USD | 212.47 USD |
| `1D` | `1.31` | 8,980.00 USD | 0.00 USD | 8,980.00 USD | 0.00 USD | 0.00 USD | 15.94 USD |
| `7D` | `1.31` | 25,040.00 USD | 0.00 USD | 25,040.00 USD | 0.00 USD | 0.00 USD | 296.02 USD |
| `7D` | `1.31` | 24,740.00 USD | 0.00 USD | 24,740.00 USD | 0.00 USD | 0.00 USD | 302.40 USD |
| `7D` | `1.31` | 24,440.00 USD | 0.00 USD | 24,440.00 USD | 0.00 USD | 0.00 USD | 324.32 USD |
| `7D` | `1.32` | 24,120.00 USD | 0.00 USD | 24,120.00 USD | 0.00 USD | 0.00 USD | 3,350.00 USD |
| `1D` | `1.32` | 8,970.00 USD | 0.00 USD | 8,970.00 USD | 0.00 USD | 0.00 USD | 90.12 USD |
| `7D` | `1.32` | 20,760.00 USD | 0.00 USD | 20,760.00 USD | 0.00 USD | 0.00 USD | 733.67 USD |
| `1D` | `1.32` | 8,880.00 USD | 0.00 USD | 8,880.00 USD | 0.00 USD | 0.00 USD | 192.88 USD |
| `7D` | `1.32` | 20,030.00 USD | 0.00 USD | 20,030.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD |
| `1D` | `1.32` | 8,680.00 USD | 0.00 USD | 8,680.00 USD | 0.00 USD | 0.00 USD | 492.27 USD |
| `7D` | `1.32` | 17,400.00 USD | 0.00 USD | 17,400.00 USD | 0.00 USD | 0.00 USD | 6,670.00 USD |
| `1D` | `1.32` | 8,190.00 USD | 0.00 USD | 8,190.00 USD | 0.00 USD | 0.00 USD | 5,970.00 USD |
| `7D` | `1.32` | 10,730.00 USD | 0.00 USD | 10,730.00 USD | 0.00 USD | 0.00 USD | 8,460.00 USD |
| `1D` | `1.32` | 2,220.00 USD | 0.00 USD | 2,220.00 USD | 0.00 USD | 0.00 USD | 2,220.00 USD |
| `7D` | `1.32` | 2,270.00 USD | 0.00 USD | 2,270.00 USD | 0.00 USD | 0.00 USD | 612.00 USD |
| `7D` | `1.33` | 1,660.00 USD | 0.00 USD | 1,660.00 USD | 0.00 USD | 0.00 USD | 791.44 USD |
| `7D` | `1.33` | 866.95 USD | 0.00 USD | 866.95 USD | 0.00 USD | 0.00 USD | 705.61 USD |
| `7D` | `1.33` | 161.34 USD | 0.00 USD | 161.34 USD | 0.00 USD | 0.00 USD | 161.34 USD |
| `1D` | `1.33` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.33` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 3,350.00 USD | 3,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,350.00 USD |
| `1D` | `1.34` | 90.12 USD | 90.12 USD | 0.00 USD | 0.00 USD | 0.00 USD | 90.12 USD |
| `7D` | `1.35` | 4,090.00 USD | 4,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 733.67 USD |
| `1D` | `1.35` | 283.00 USD | 283.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 192.88 USD |
| `7D` | `1.35` | 6,720.00 USD | 6,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD |
| `1D` | `1.35` | 775.27 USD | 775.27 USD | 0.00 USD | 0.00 USD | 0.00 USD | 492.27 USD |
| `7D` | `1.35` | 13,380.00 USD | 13,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,670.00 USD |
| `1D` | `1.35` | 6,750.00 USD | 6,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,970.00 USD |
| `7D` | `1.35` | 21,850.00 USD | 21,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,460.00 USD |
| `1D` | `1.35` | 8,970.00 USD | 8,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,220.00 USD |
| `7D` | `1.35` | 22,430.00 USD | 22,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 580.88 USD |
| `7D` | `1.35` | 23,250.00 USD | 23,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 822.56 USD |
| `7D` | `1.35` | 23,780.00 USD | 23,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 529.80 USD |
| `7D` | `1.35` | 24,120.00 USD | 24,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 337.15 USD |
| `7D` | `1.36` | 25,740.00 USD | 25,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,620.00 USD |
| `1D` | `1.36` | 9,010.00 USD | 9,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 42.74 USD |
| `7D` | `1.36` | 25,910.00 USD | 25,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 172.14 USD |
| `1D` | `1.36` | 9,110.00 USD | 9,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 98.76 USD |
| `7D` | `1.36` | 26,260.00 USD | 26,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 347.41 USD |
| `1D` | `1.36` | 9,260.00 USD | 9,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 149.50 USD |
| `7D` | `1.36` | 29,440.00 USD | 29,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,190.00 USD |
| `1D` | `1.36` | 9,590.00 USD | 9,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 329.23 USD |
| `7D` | `1.36` | 34,130.00 USD | 34,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,690.00 USD |
| `1D` | `1.36` | 13,430.00 USD | 13,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,840.00 USD |
| `7D` | `1.36` | 35,240.00 USD | 35,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD |
| `1D` | `1.36` | 13,450.00 USD | 13,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21.02 USD |
| `7D` | `1.36` | 35,440.00 USD | 35,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 203.30 USD |
| `7D` | `1.37` | 35,820.00 USD | 35,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 374.04 USD |
| `7D` | `1.37` | 36,140.00 USD | 36,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 324.71 USD |
| `7D` | `1.37` | 36,180.00 USD | 36,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33.65 USD |
| `7D` | `1.38` | 36,990.00 USD | 36,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 810.32 USD |
| `1D` | `1.38` | 13,470.00 USD | 13,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21.38 USD |
| `7D` | `1.38` | 37,070.00 USD | 37,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 86.09 USD |
| `1D` | `1.38` | 13,520.00 USD | 13,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 49.38 USD |
| `7D` | `1.39` | 37,250.00 USD | 37,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 173.70 USD |
| `1D` | `1.39` | 13,590.00 USD | 13,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 74.75 USD |
| `7D` | `1.39` | 38,740.00 USD | 38,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,490.00 USD |
| `1D` | `1.39` | 13,750.00 USD | 13,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 160.97 USD |
| `7D` | `1.39` | 40,990.00 USD | 40,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `1.39` | 15,660.00 USD | 15,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,910.00 USD |
| `7D` | `1.39` | 41,720.00 USD | 41,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 731.25 USD |
| `1D` | `1.39` | 15,690.00 USD | 15,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 27.74 USD |
| `7D` | `1.39` | 41,830.00 USD | 41,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 108.00 USD |
| `7D` | `1.39` | 41,990.00 USD | 41,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 168.35 USD |
| `7D` | `1.39` | 42,190.00 USD | 42,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 194.47 USD |
| `7D` | `1.40` | 42,210.00 USD | 42,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16.82 USD |
| `7D` | `1.46` | 42,530.00 USD | 42,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 324.13 USD |
| `1D` | `1.46` | 15,700.00 USD | 15,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8.55 USD |
| `7D` | `1.46` | 42,540.00 USD | 42,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14.71 USD |
| `1D` | `1.46` | 15,720.00 USD | 15,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18.41 USD |
| `7D` | `1.47` | 42,630.00 USD | 42,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 80.63 USD |
| `1D` | `1.47` | 15,750.00 USD | 15,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.18 USD |
| `7D` | `1.47` | 43,190.00 USD | 43,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 562.18 USD |
| `1D` | `1.47` | 15,770.00 USD | 15,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23.95 USD |
| `7D` | `1.47` | 43,560.00 USD | 43,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 376.19 USD |
| `1D` | `1.47` | 16,360.00 USD | 16,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 588.44 USD |
| `7D` | `1.47` | 44,180.00 USD | 44,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 619.25 USD |
| `7D` | `1.47` | 44,210.00 USD | 44,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 30.38 USD |

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
| `13:30:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 466.26 USD | 224.50 USD | 241.76 USD | -17.27 USD | `-3.70%` | `0B / 1S` |
| `13:35:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 633.99 USD | 56.90 USD | 577.09 USD | -520.20 USD | `-82.05%` | `0B / 1S` |
| `13:40:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 551.53 USD | 513.23 USD | 38.30 USD | 474.93 USD | `+86.11%` | `1B / 0S` |
| `13:45:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 520.96 USD | 434.13 USD | 86.83 USD | 347.31 USD | `+66.67%` | `1B / 0S` |
| `13:45:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 1,590.80 USD | 900.91 USD | 689.89 USD | 211.02 USD | `+13.27%` | `1B / 0S` |
| `13:50:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 475.64 USD | 146.89 USD | 328.75 USD | -181.86 USD | `-38.24%` | `0B / 1S` |
| `13:55:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 594.22 USD | 234.09 USD | 360.13 USD | -126.05 USD | `-21.21%` | `0B / 1S` |
| `14:00:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 542.34 USD | 416.44 USD | 125.90 USD | 290.54 USD | `+53.57%` | `1B / 0S` |
| `14:00:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 5,477.00 USD | 1,638.42 USD | 3,838.58 USD | -2,200.16 USD | `-40.17%` | `0B / 1S` |
| `14:00:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 1,291.28 USD | 768.90 USD | 522.38 USD | 246.52 USD | `+19.09%` | `1B / 0S` |

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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.33` (Risk Distance: `0.0014` pts)
  * +2.5R Take Profit: `1.33`
  * Mathematical Lot Sizing: **`0.07 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.33` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.33` (Risk Distance: `0.0014` pts)
  * +2.5R Take Profit: `1.33`
  * Mathematical Lot Sizing: **`0.07 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.35`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
