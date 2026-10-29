# 🏛️ SOVEREIGN CANDIDATE DOSSIER: GBPUSD
**Canonical Key**: `GBPUSD` | **Broker Instrument**: `GBPUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-29 23:49:57 IST` (`2026-10-29 18:19:57 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `1.33` | VWAP Z-Score: `+1.81` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000924` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `67.69` (State: `OVERBOUGHT`)
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
  * Institutional Anchors: EMA-144=`1.33` | EMA-200=`1.33` (Slope: `+0.0427`) | EMA-233=`1.33`
- **Range Boundaries**: 24H High=`1.34` | 24H Low=`1.33` | Weekly High=`1.34` | Weekly Low=`1.33`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.33` (Distance: `+0.27%`)
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
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `653` | 872.87 USD | 703.75 USD | `+80.63%` | 8,680.86 USD | `+0.44` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `718` | 960.12 USD | 681.02 USD | `+70.93%` | 9,361.88 USD | `+0.49` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.34` | `1.34` | `1.34` | `1.34` | `613` | 819.76 USD | 37.84 USD | `+4.62%` | 9,399.71 USD | `-0.47` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `1.33` | `1.34` | `1.33` | `1.34` | `2,359` | 3,150.66 USD | 1,683.56 USD | `+53.44%` | 14,976.20 USD | `+0.67` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `2,145` | 2,868.34 USD | 2,575.16 USD | `+89.78%` | 17,551.37 USD | `+1.16` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.34` | `1.34` | `1.34` | `1.34` | `2,289` | 3,060.83 USD | -635.71 USD | `-20.77%` | 16,915.65 USD | `-0.79` | **`BEARISH`** | `AGGRESSIVE SELLING` |
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
| `7D` | `1.20` | 44,750.00 USD | 0.00 USD | 44,750.00 USD | 0.00 USD | 0.00 USD | 56.91 USD |
| `7D` | `1.20` | 44,700.00 USD | 0.00 USD | 44,700.00 USD | 0.00 USD | 0.00 USD | 690.23 USD |
| `7D` | `1.20` | 44,010.00 USD | 0.00 USD | 44,010.00 USD | 0.00 USD | 0.00 USD | 879.37 USD |
| `7D` | `1.20` | 43,130.00 USD | 0.00 USD | 43,130.00 USD | 0.00 USD | 0.00 USD | 55.13 USD |
| `1D` | `1.21` | 16,260.00 USD | 0.00 USD | 16,260.00 USD | 0.00 USD | 0.00 USD | 51.11 USD |
| `7D` | `1.21` | 43,070.00 USD | 0.00 USD | 43,070.00 USD | 0.00 USD | 0.00 USD | 138.62 USD |
| `7D` | `1.21` | 42,930.00 USD | 0.00 USD | 42,930.00 USD | 0.00 USD | 0.00 USD | 29.04 USD |
| `7D` | `1.28` | 42,910.00 USD | 0.00 USD | 42,910.00 USD | 0.00 USD | 0.00 USD | 28.92 USD |
| `7D` | `1.28` | 42,880.00 USD | 0.00 USD | 42,880.00 USD | 0.00 USD | 0.00 USD | 947.40 USD |
| `1D` | `1.28` | 16,210.00 USD | 0.00 USD | 16,210.00 USD | 0.00 USD | 0.00 USD | 79.53 USD |
| `7D` | `1.28` | 41,930.00 USD | 0.00 USD | 41,930.00 USD | 0.00 USD | 0.00 USD | 142.27 USD |
| `1D` | `1.28` | 16,130.00 USD | 0.00 USD | 16,130.00 USD | 0.00 USD | 0.00 USD | 59.87 USD |
| `7D` | `1.28` | 41,790.00 USD | 0.00 USD | 41,790.00 USD | 0.00 USD | 0.00 USD | 1,220.00 USD |
| `1D` | `1.28` | 16,070.00 USD | 0.00 USD | 16,070.00 USD | 0.00 USD | 0.00 USD | 2,000.00 USD |
| `7D` | `1.28` | 40,560.00 USD | 0.00 USD | 40,560.00 USD | 0.00 USD | 0.00 USD | 3,200.00 USD |
| `1D` | `1.28` | 14,080.00 USD | 0.00 USD | 14,080.00 USD | 0.00 USD | 0.00 USD | 47.77 USD |
| `7D` | `1.28` | 37,360.00 USD | 0.00 USD | 37,360.00 USD | 0.00 USD | 0.00 USD | 82.52 USD |
| `1D` | `1.28` | 14,030.00 USD | 0.00 USD | 14,030.00 USD | 0.00 USD | 0.00 USD | 115.48 USD |
| `7D` | `1.29` | 37,280.00 USD | 0.00 USD | 37,280.00 USD | 0.00 USD | 0.00 USD | 425.34 USD |
| `1D` | `1.29` | 13,910.00 USD | 0.00 USD | 13,910.00 USD | 0.00 USD | 0.00 USD | 16.13 USD |
| `7D` | `1.29` | 36,860.00 USD | 0.00 USD | 36,860.00 USD | 0.00 USD | 0.00 USD | 126.51 USD |
| `7D` | `1.29` | 36,730.00 USD | 0.00 USD | 36,730.00 USD | 0.00 USD | 0.00 USD | 9.37 USD |
| `7D` | `1.30` | 36,720.00 USD | 0.00 USD | 36,720.00 USD | 0.00 USD | 0.00 USD | 57.84 USD |
| `7D` | `1.30` | 36,660.00 USD | 0.00 USD | 36,660.00 USD | 0.00 USD | 0.00 USD | 1,890.00 USD |
| `1D` | `1.31` | 13,900.00 USD | 0.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD | 13.17 USD |
| `7D` | `1.31` | 34,770.00 USD | 0.00 USD | 34,770.00 USD | 0.00 USD | 0.00 USD | 284.55 USD |
| `1D` | `1.31` | 13,880.00 USD | 0.00 USD | 13,880.00 USD | 0.00 USD | 0.00 USD | 253.19 USD |
| `7D` | `1.31` | 34,480.00 USD | 0.00 USD | 34,480.00 USD | 0.00 USD | 0.00 USD | 2,420.00 USD |
| `1D` | `1.31` | 13,630.00 USD | 0.00 USD | 13,630.00 USD | 0.00 USD | 0.00 USD | 2,980.00 USD |
| `7D` | `1.31` | 32,060.00 USD | 0.00 USD | 32,060.00 USD | 0.00 USD | 0.00 USD | 6,420.00 USD |
| `1D` | `1.31` | 10,650.00 USD | 0.00 USD | 10,650.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD |
| `7D` | `1.31` | 25,640.00 USD | 0.00 USD | 25,640.00 USD | 0.00 USD | 0.00 USD | 90.19 USD |
| `1D` | `1.31` | 9,530.00 USD | 0.00 USD | 9,530.00 USD | 0.00 USD | 0.00 USD | 230.96 USD |
| `7D` | `1.31` | 25,550.00 USD | 0.00 USD | 25,550.00 USD | 0.00 USD | 0.00 USD | 446.25 USD |
| `1D` | `1.31` | 9,300.00 USD | 0.00 USD | 9,300.00 USD | 0.00 USD | 0.00 USD | 32.26 USD |
| `7D` | `1.31` | 25,100.00 USD | 0.00 USD | 25,100.00 USD | 0.00 USD | 0.00 USD | 699.25 USD |
| `7D` | `1.31` | 24,400.00 USD | 0.00 USD | 24,400.00 USD | 0.00 USD | 0.00 USD | 51.79 USD |
| `7D` | `1.32` | 24,350.00 USD | 0.00 USD | 24,350.00 USD | 0.00 USD | 0.00 USD | 39.33 USD |
| `7D` | `1.32` | 24,310.00 USD | 0.00 USD | 24,310.00 USD | 0.00 USD | 0.00 USD | 3,400.00 USD |
| `1D` | `1.32` | 9,260.00 USD | 0.00 USD | 9,260.00 USD | 0.00 USD | 0.00 USD | 26.34 USD |
| `7D` | `1.32` | 20,910.00 USD | 0.00 USD | 20,910.00 USD | 0.00 USD | 0.00 USD | 655.32 USD |
| `1D` | `1.32` | 9,240.00 USD | 0.00 USD | 9,240.00 USD | 0.00 USD | 0.00 USD | 298.99 USD |
| `7D` | `1.32` | 20,260.00 USD | 0.00 USD | 20,260.00 USD | 0.00 USD | 0.00 USD | 3,000.00 USD |
| `1D` | `1.32` | 8,940.00 USD | 0.00 USD | 8,940.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD |
| `7D` | `1.32` | 17,260.00 USD | 0.00 USD | 17,260.00 USD | 0.00 USD | 0.00 USD | 8,860.00 USD |
| `1D` | `1.32` | 7,630.00 USD | 0.00 USD | 7,630.00 USD | 0.00 USD | 0.00 USD | 7,050.00 USD |
| `7D` | `1.32` | 8,390.00 USD | 0.00 USD | 8,390.00 USD | 0.00 USD | 0.00 USD | 6,350.00 USD |
| `1D` | `1.32` | 579.32 USD | 0.00 USD | 579.32 USD | 0.00 USD | 0.00 USD | 52.87 USD |
| `7D` | `1.32` | 2,040.00 USD | 0.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | 568.64 USD |
| `1D` | `1.33` | 526.45 USD | 0.00 USD | 526.45 USD | 0.00 USD | 0.00 USD | 526.45 USD |
| `7D` | `1.33` | 1,470.00 USD | 0.00 USD | 1,470.00 USD | 0.00 USD | 0.00 USD | 1,470.00 USD |
| `1D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.34` | 39.33 USD | 39.33 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39.33 USD |
| `7D` | `1.34` | 3,440.00 USD | 3,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,400.00 USD |
| `1D` | `1.34` | 26.34 USD | 26.34 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.34 USD |
| `7D` | `1.35` | 4,100.00 USD | 4,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 655.32 USD |
| `1D` | `1.35` | 325.33 USD | 325.33 USD | 0.00 USD | 0.00 USD | 0.00 USD | 298.99 USD |
| `7D` | `1.35` | 7,100.00 USD | 7,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,000.00 USD |
| `1D` | `1.35` | 1,640.00 USD | 1,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD |
| `7D` | `1.35` | 12,020.00 USD | 12,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,920.00 USD |
| `1D` | `1.35` | 8,670.00 USD | 8,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,040.00 USD |
| `7D` | `1.35` | 22,180.00 USD | 22,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,160.00 USD |
| `1D` | `1.35` | 8,740.00 USD | 8,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 63.02 USD |
| `7D` | `1.35` | 22,720.00 USD | 22,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 541.38 USD |
| `1D` | `1.35` | 9,260.00 USD | 9,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 526.45 USD |
| `7D` | `1.35` | 24,250.00 USD | 24,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,530.00 USD |
| `7D` | `1.35` | 24,740.00 USD | 24,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 488.27 USD |
| `7D` | `1.36` | 24,790.00 USD | 24,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 57.84 USD |
| `7D` | `1.36` | 26,690.00 USD | 26,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,890.00 USD |
| `1D` | `1.36` | 9,280.00 USD | 9,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.17 USD |
| `7D` | `1.36` | 26,920.00 USD | 26,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 233.92 USD |
| `1D` | `1.36` | 9,520.00 USD | 9,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 246.15 USD |
| `7D` | `1.36` | 29,390.00 USD | 29,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,470.00 USD |
| `1D` | `1.36` | 12,510.00 USD | 12,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,990.00 USD |
| `7D` | `1.36` | 35,820.00 USD | 35,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,420.00 USD |
| `1D` | `1.36` | 13,630.00 USD | 13,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD |
| `7D` | `1.36` | 35,910.00 USD | 35,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 90.19 USD |
| `1D` | `1.36` | 13,630.00 USD | 13,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.49 USD |
| `7D` | `1.37` | 36,260.00 USD | 36,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 356.86 USD |
| `1D` | `1.37` | 13,900.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 262.73 USD |
| `7D` | `1.37` | 36,960.00 USD | 36,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 695.22 USD |
| `7D` | `1.37` | 37,100.00 USD | 37,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 145.21 USD |
| `7D` | `1.38` | 37,130.00 USD | 37,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28.92 USD |
| `7D` | `1.38` | 38,080.00 USD | 38,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 947.40 USD |
| `1D` | `1.39` | 13,900.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6.59 USD |
| `7D` | `1.39` | 38,200.00 USD | 38,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 116.96 USD |
| `1D` | `1.39` | 14,030.00 USD | 14,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 123.06 USD |
| `7D` | `1.39` | 38,920.00 USD | 38,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 727.84 USD |
| `1D` | `1.39` | 15,520.00 USD | 15,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,490.00 USD |
| `7D` | `1.39` | 42,640.00 USD | 42,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,720.00 USD |
| `1D` | `1.39` | 16,080.00 USD | 16,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 557.26 USD |
| `7D` | `1.39` | 42,690.00 USD | 42,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 45.10 USD |
| `1D` | `1.39` | 16,080.00 USD | 16,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2.92 USD |
| `7D` | `1.39` | 42,850.00 USD | 42,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 156.88 USD |
| `1D` | `1.39` | 16,210.00 USD | 16,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 131.61 USD |
| `7D` | `1.39` | 43,210.00 USD | 43,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 369.15 USD |
| `7D` | `1.39` | 43,290.00 USD | 43,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 72.61 USD |
| `7D` | `1.46` | 43,300.00 USD | 43,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11.57 USD |
| `7D` | `1.46` | 43,670.00 USD | 43,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 370.40 USD |
| `1D` | `1.47` | 16,210.00 USD | 16,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2.63 USD |
| `7D` | `1.47` | 43,720.00 USD | 43,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 46.66 USD |
| `1D` | `1.47` | 16,260.00 USD | 16,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 40.90 USD |
| `7D` | `1.47` | 43,970.00 USD | 43,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 252.38 USD |
| `1D` | `1.47` | 16,450.00 USD | 16,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 195.68 USD |
| `7D` | `1.47` | 44,850.00 USD | 44,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 886.38 USD |
| `1D` | `1.47` | 16,910.00 USD | 16,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 457.71 USD |
| `7D` | `1.47` | 45,300.00 USD | 45,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 441.09 USD |
| `1D` | `1.47` | 16,910.00 USD | 16,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.29 USD |
| `7D` | `1.47` | 45,340.00 USD | 45,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39.05 USD |
| `1D` | `1.47` | 16,960.00 USD | 16,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 49.42 USD |
| `1D` | `1.47` | 16,970.00 USD | 16,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1.69 USD |
| `7D` | `1.47` | 45,470.00 USD | 45,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 134.92 USD |
| `7D` | `1.47` | 45,490.00 USD | 45,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15.10 USD |

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
| `17:35:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 1,167.13 USD | 881.83 USD | 285.30 USD | 596.53 USD | `+51.11%` | `1B / 0S` |
| `17:40:00` | `1.33` | `1.33` | `1.33` | `1.33` | `1.33` | 1,241.45 USD | 1,150.16 USD | 91.28 USD | 1,058.88 USD | `+85.29%` | `1B / 0S` |
| `17:45:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.33` | 1,064.19 USD | 873.65 USD | 190.55 USD | 683.10 USD | `+64.19%` | `1B / 0S` |
| `17:45:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.33` | 3,150.66 USD | 2,417.11 USD | 733.55 USD | 1,683.56 USD | `+53.44%` | `1B / 0S` |
| `17:50:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.33` | 1,051.27 USD | 918.35 USD | 132.92 USD | 785.44 USD | `+74.71%` | `1B / 0S` |
| `17:55:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 1,035.08 USD | 425.44 USD | 609.65 USD | -184.21 USD | `-17.80%` | `0B / 1S` |
| `18:00:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 2,868.34 USD | 2,721.75 USD | 146.59 USD | 2,575.16 USD | `+89.78%` | `1B / 0S` |
| `18:00:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 12,279.59 USD | 10,373.28 USD | 1,906.31 USD | 8,466.97 USD | `+68.95%` | `1B / 0S` |
| `18:00:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 1,034.07 USD | 864.55 USD | 169.52 USD | 695.03 USD | `+67.21%` | `1B / 0S` |
| `18:05:00` | `1.34` | `1.34` | `1.34` | `1.34` | `1.34` | 872.87 USD | 788.31 USD | 84.56 USD | 703.75 USD | `+80.63%` | `1B / 0S` |

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
  * `2026-10-29 23:30:59 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:59 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:59 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:59 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:54:59 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:44:59 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:40:59 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:41:59 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:41:59 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:41:59 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:41:59 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.33` (Risk Distance: `0.0011` pts)
  * +2.5R Take Profit: `1.33`
  * Mathematical Lot Sizing: **`0.08 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.33` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.33` (Risk Distance: `0.0011` pts)
  * +2.5R Take Profit: `1.33`
  * Mathematical Lot Sizing: **`0.08 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.35`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
