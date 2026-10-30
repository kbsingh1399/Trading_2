# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USDJPY
**Canonical Key**: `USDJPY` | **Broker Instrument**: `USDJPY.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 11:14:10 IST` (`2026-10-30 05:44:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `157.66` | **Live Ask Quote**: `157.66` | **Mid Price**: `157.66`
- **Spread Points**: `1.00` | **Spread BPS**: `0.06 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `100,000.0` | Digits: `3` | Point: `0.001`
  * Point Value (1.0 Lot): `100.00 USD` | Point Value (0.01 Lot): `1.0000 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`50.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `157.43` | VWAP Z-Score: `+1.21` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1451` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `54.13` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `157.81` | Lower -3.00σ Band: `157.06`
  * Upper +2.51σ Band: `157.75` | Lower -2.51σ Band: `157.12`
  * Upper +2.01σ Band: `157.69` | Lower -2.01σ Band: `157.18`
  * Upper +2.00σ Band: `157.69` | Lower -2.00σ Band: `157.18`
  * Upper +1.28σ Band: `157.60` | Lower -1.28σ Band: `157.27`
  * Upper +1.00σ Band: `157.56` | Lower -1.00σ Band: `157.31`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`157.44` | EMA-20=`157.46` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`157.59` (Slope: `+0.0000`) | EMA-100=`157.70`
  * Institutional Anchors: EMA-144=`157.75` | EMA-200=`157.78` (Slope: `-0.0298`) | EMA-233=`157.79`
- **Range Boundaries**: 24H High=`158.13` | 24H Low=`157.12` | Weekly High=`158.35` | Weekly Low=`157.12`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `157.59` (Distance: `+0.04%`)
  * Point of Control (POC) = `157.45` (Distance: `+0.13%`)
  * Value Area Low (VAL) = `157.24` (Distance: `+0.27%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`157.99` | POC=`157.87` | VAL=`157.76`
  * Prior Day Extremes: PDH=`158.13` | PDL=`157.60` | PDC=`157.69`
  * Monday Range Blueprint: High=`157.64` | Mid=`157.15` | Low=`156.65`
  * Developing Weekly Value Area: Weekly VAH=`158.06` | Weekly POC=`157.87` | Weekly VAL=`157.44`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`157.90` | Low=`157.12`
  * London Session (08:00-16:00 UTC): High=`157.70` | Low=`157.40`
  * New York Session (13:00-21:00 UTC): High=`158.60` | Low=`156.71`
  * Initial Balance (First Hour): IB High=`157.70` | IB Low=`157.40`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `157.03` - `158.29`
  * Optimal Trade Entry (OTE 0.705): `157.97`
  * Structural Invalidation Anchor (0.786): `158.92`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `157.48` | `157.53` | `157.46` | `157.48` | `488` | 76,849.26 USD | -20,310.16 USD | `-26.43%` | 486,470.03 USD | `-0.22` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `157.48` | `157.53` | `157.47` | `157.49` | `335` | 52,758.14 USD | -9,255.81 USD | `-17.54%` | 477,214.21 USD | `-0.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `157.49` | `157.51` | `157.43` | `157.46` | `282` | 44,402.59 USD | -16,584.10 USD | `-37.35%` | 460,630.11 USD | `-0.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `157.43` | `157.55` | `157.42` | `157.46` | `2,804` | 441,523.45 USD | -18,679.84 USD | `-4.23%` | -42,770.59 USD | `-0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `157.46` | `157.53` | `157.45` | `157.48` | `1,669` | 262,839.13 USD | 7,467.02 USD | `+2.84%` | -35,303.56 USD | `+0.11` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `157.48` | `157.53` | `157.43` | `157.46` | `1,105` | 173,988.88 USD | -65,245.83 USD | `-37.50%` | -100,549.39 USD | `-0.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `157.81` | `157.90` | `157.31` | `157.36` | `12,235` | 1,925,262.90 USD | -1,548,081.92 USD | `-80.41%` | -1,144,679.06 USD | `-2.67` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `157.36` | `157.50` | `157.19` | `157.42` | `16,438` | 2,587,735.71 USD | 925,962.94 USD | `+35.78%` | -218,716.12 USD | `+1.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `157.43` | `157.59` | `157.42` | `157.58` | `6,490` | 1,022,687.71 USD | 869,872.31 USD | `+85.06%` | 651,156.18 USD | `+1.31` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `157.88` | `157.98` | `157.63` | `157.69` | `20,300` | 3,201,147.60 USD | -1,948,126.97 USD | `-60.86%` | -212,851.23 USD | `-0.93` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.64` | `157.90` | `157.31` | `157.36` | `20,459` | 3,219,366.86 USD | -2,125,220.88 USD | `-66.01%` | -2,338,072.11 USD | `-0.83` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.36` | `157.63` | `157.12` | `157.43` | `39,720` | 6,253,000.44 USD | 1,103,833.41 USD | `+17.65%` | -1,234,238.70 USD | `+0.68` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `157.87` | `158.08` | `157.81` | `158.06` | `23,822` | 3,765,376.79 USD | 3,094,533.80 USD | `+82.18%` | 3,521,504.93 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `158.06` | `158.13` | `157.71` | `157.88` | `37,561` | 5,930,280.92 USD | -1,786,229.19 USD | `-30.12%` | 1,735,275.74 USD | `-1.19` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.88` | `157.98` | `157.63` | `157.69` | `20,300` | 3,201,147.60 USD | -1,948,126.97 USD | `-60.86%` | -212,851.23 USD | `-0.93` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.64` | `157.90` | `157.31` | `157.36` | `20,459` | 3,219,366.86 USD | -2,125,220.88 USD | `-66.01%` | -2,338,072.11 USD | `-0.83` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.36` | `157.63` | `157.12` | `157.43` | `39,720` | 6,253,000.44 USD | 1,103,833.41 USD | `+17.65%` | -1,234,238.70 USD | `+0.68` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `204` | `0x0911...129a` | `SHORT` | 10,435,451.86 USD | `66,223.20` | `156.58` | `157.58` | `167.72` | -66,431.62 USD | `-0.64%` | `20X Isolated` |
| `1022` | `0x9dea...d617` | `LONG` | 2,137,884.71 USD | `13,566.98` | `157.66` | `157.59` | `149.22` | -1,129.04 USD | `-0.05%` | `50X Isolated` |
| `1113` | `0xec0b...b078` | `SHORT` | 1,988,390.25 USD | `12,617.49` | `158.22` | `157.59` | `162.95` | 7,975.42 USD | `+0.40%` | `20X Isolated` |
| `1152` | `0xc966...f6b6` | `SHORT` | 1,933,965.16 USD | `12,272.91` | `157.61` | `157.59` | `215.27` | 312.50 USD | `+0.02%` | `5X Isolated` |
| `1198` | `0xbef1...d2e5` | `LONG` | 1,862,917.09 USD | `11,821.29` | `157.63` | `157.59` | `155.50` | -443.52 USD | `-0.02%` | `50X Isolated` |
| `1880` | `0x3d89...eb14` | `LONG` | 1,087,302.00 USD | `6,900.00` | `158.17` | `157.59` | `127.35` | -4,087.60 USD | `-0.38%` | `5X Isolated` |

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
| `7D` | `141.50` | 90,360.00 USD | 0.00 USD | 90,360.00 USD | 0.00 USD | 0.00 USD | 36.20 USD |
| `1D` | `141.55` | 6,460.00 USD | 0.00 USD | 6,460.00 USD | 0.00 USD | 0.00 USD | 126.03 USD |
| `7D` | `141.67` | 90,320.00 USD | 0.00 USD | 90,320.00 USD | 0.00 USD | 0.00 USD | 66.87 USD |
| `1D` | `141.71` | 6,340.00 USD | 0.00 USD | 6,340.00 USD | 0.00 USD | 0.00 USD | 23.80 USD |
| `7D` | `141.84` | 90,260.00 USD | 0.00 USD | 90,260.00 USD | 0.00 USD | 0.00 USD | 1,640.00 USD |
| `1D` | `141.87` | 6,310.00 USD | 0.00 USD | 6,310.00 USD | 0.00 USD | 0.00 USD | 178.51 USD |
| `7D` | `142.01` | 88,620.00 USD | 0.00 USD | 88,620.00 USD | 0.00 USD | 0.00 USD | 1,230.00 USD |
| `1D` | `142.03` | 6,140.00 USD | 0.00 USD | 6,140.00 USD | 0.00 USD | 0.00 USD | 7.98 USD |
| `7D` | `142.18` | 87,390.00 USD | 0.00 USD | 87,390.00 USD | 0.00 USD | 0.00 USD | 882.48 USD |
| `7D` | `142.35` | 86,510.00 USD | 0.00 USD | 86,510.00 USD | 0.00 USD | 0.00 USD | 454.97 USD |
| `7D` | `150.34` | 86,050.00 USD | 0.00 USD | 86,050.00 USD | 0.00 USD | 0.00 USD | 3.61 USD |
| `7D` | `150.51` | 86,050.00 USD | 0.00 USD | 86,050.00 USD | 0.00 USD | 0.00 USD | 542.84 USD |
| `7D` | `150.68` | 85,510.00 USD | 0.00 USD | 85,510.00 USD | 0.00 USD | 0.00 USD | 120.48 USD |
| `1D` | `150.83` | 6,130.00 USD | 0.00 USD | 6,130.00 USD | 0.00 USD | 0.00 USD | 15.64 USD |
| `7D` | `150.85` | 85,390.00 USD | 0.00 USD | 85,390.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `1D` | `150.99` | 6,110.00 USD | 0.00 USD | 6,110.00 USD | 0.00 USD | 0.00 USD | 299.45 USD |
| `7D` | `151.02` | 85,370.00 USD | 0.00 USD | 85,370.00 USD | 0.00 USD | 0.00 USD | 132.23 USD |
| `1D` | `151.15` | 5,810.00 USD | 0.00 USD | 5,810.00 USD | 0.00 USD | 0.00 USD | 65.96 USD |
| `7D` | `151.19` | 85,240.00 USD | 0.00 USD | 85,240.00 USD | 0.00 USD | 0.00 USD | 930.37 USD |
| `1D` | `151.31` | 5,750.00 USD | 0.00 USD | 5,750.00 USD | 0.00 USD | 0.00 USD | 474.33 USD |
| `7D` | `151.36` | 84,310.00 USD | 0.00 USD | 84,310.00 USD | 0.00 USD | 0.00 USD | 5,190.00 USD |
| `1D` | `151.47` | 5,270.00 USD | 0.00 USD | 5,270.00 USD | 0.00 USD | 0.00 USD | 19.94 USD |
| `7D` | `151.53` | 79,120.00 USD | 0.00 USD | 79,120.00 USD | 0.00 USD | 0.00 USD | 1,480.00 USD |
| `7D` | `151.70` | 77,630.00 USD | 0.00 USD | 77,630.00 USD | 0.00 USD | 0.00 USD | 3,870.00 USD |
| `7D` | `153.57` | 73,760.00 USD | 0.00 USD | 73,760.00 USD | 0.00 USD | 0.00 USD | 902.92 USD |
| `7D` | `153.74` | 72,860.00 USD | 0.00 USD | 72,860.00 USD | 0.00 USD | 0.00 USD | 430.97 USD |
| `7D` | `153.91` | 72,430.00 USD | 0.00 USD | 72,430.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `1D` | `154.03` | 5,250.00 USD | 0.00 USD | 5,250.00 USD | 0.00 USD | 0.00 USD | 35.94 USD |
| `7D` | `154.08` | 72,400.00 USD | 0.00 USD | 72,400.00 USD | 0.00 USD | 0.00 USD | 154.27 USD |
| `1D` | `154.19` | 5,220.00 USD | 0.00 USD | 5,220.00 USD | 0.00 USD | 0.00 USD | 646.62 USD |
| `7D` | `154.25` | 72,240.00 USD | 0.00 USD | 72,240.00 USD | 0.00 USD | 0.00 USD | 334.35 USD |
| `1D` | `154.35` | 4,570.00 USD | 0.00 USD | 4,570.00 USD | 0.00 USD | 0.00 USD | 218.34 USD |
| `7D` | `154.42` | 71,910.00 USD | 0.00 USD | 71,910.00 USD | 0.00 USD | 0.00 USD | 5,860.00 USD |
| `1D` | `154.51` | 4,350.00 USD | 0.00 USD | 4,350.00 USD | 0.00 USD | 0.00 USD | 817.72 USD |
| `7D` | `154.59` | 66,050.00 USD | 0.00 USD | 66,050.00 USD | 0.00 USD | 0.00 USD | 7,030.00 USD |
| `1D` | `154.67` | 3,530.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD | 0.00 USD | 32.03 USD |
| `7D` | `154.76` | 59,020.00 USD | 0.00 USD | 59,020.00 USD | 0.00 USD | 0.00 USD | 3,160.00 USD |
| `7D` | `154.93` | 55,860.00 USD | 0.00 USD | 55,860.00 USD | 0.00 USD | 0.00 USD | 6,690.00 USD |
| `7D` | `155.10` | 49,170.00 USD | 0.00 USD | 49,170.00 USD | 0.00 USD | 0.00 USD | 653.34 USD |
| `7D` | `155.27` | 48,520.00 USD | 0.00 USD | 48,520.00 USD | 0.00 USD | 0.00 USD | 2,010.00 USD |
| `7D` | `155.61` | 46,510.00 USD | 0.00 USD | 46,510.00 USD | 0.00 USD | 0.00 USD | 362.07 USD |
| `1D` | `155.63` | 3,500.00 USD | 0.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | 74.96 USD |
| `7D` | `155.78` | 46,140.00 USD | 0.00 USD | 46,140.00 USD | 0.00 USD | 0.00 USD | 668.68 USD |
| `1D` | `155.79` | 3,430.00 USD | 0.00 USD | 3,430.00 USD | 0.00 USD | 0.00 USD | 1,290.00 USD |
| `1D` | `155.95` | 2,140.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD | 0.00 USD | 1,240.00 USD |
| `7D` | `155.95` | 45,470.00 USD | 0.00 USD | 45,470.00 USD | 0.00 USD | 0.00 USD | 6,350.00 USD |
| `1D` | `156.11` | 899.58 USD | 0.00 USD | 899.58 USD | 0.00 USD | 0.00 USD | 865.66 USD |
| `7D` | `156.12` | 39,120.00 USD | 0.00 USD | 39,120.00 USD | 0.00 USD | 0.00 USD | 19,200.00 USD |
| `1D` | `156.27` | 33.92 USD | 0.00 USD | 33.92 USD | 0.00 USD | 0.00 USD | 33.92 USD |
| `7D` | `156.29` | 19,920.00 USD | 0.00 USD | 19,920.00 USD | 0.00 USD | 0.00 USD | 4,430.00 USD |
| `7D` | `156.46` | 15,490.00 USD | 0.00 USD | 15,490.00 USD | 0.00 USD | 0.00 USD | 15,490.00 USD |
| `1D` | `157.39` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `157.39` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `158.33` | 2,190.00 USD | 2,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,190.00 USD |
| `7D` | `158.50` | 2,670.00 USD | 2,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 481.90 USD |
| `7D` | `158.67` | 2,720.00 USD | 2,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 53.52 USD |
| `1D` | `158.83` | 1,260.00 USD | 1,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,260.00 USD |
| `7D` | `158.84` | 3,250.00 USD | 3,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 528.92 USD |
| `1D` | `158.99` | 1,510.00 USD | 1,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 246.56 USD |
| `7D` | `159.01` | 4,010.00 USD | 4,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 764.81 USD |
| `1D` | `159.15` | 3,050.00 USD | 3,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,540.00 USD |
| `7D` | `159.18` | 20,730.00 USD | 20,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,720.00 USD |
| `1D` | `159.31` | 3,500.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 452.39 USD |
| `7D` | `159.35` | 29,470.00 USD | 29,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,740.00 USD |
| `7D` | `159.52` | 44,620.00 USD | 44,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,150.00 USD |
| `7D` | `159.69` | 49,170.00 USD | 49,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,550.00 USD |
| `7D` | `159.86` | 50,270.00 USD | 50,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,090.00 USD |
| `7D` | `160.03` | 50,510.00 USD | 50,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 240.95 USD |
| `7D` | `160.20` | 50,530.00 USD | 50,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `1D` | `160.27` | 3,530.00 USD | 3,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31.27 USD |
| `7D` | `160.37` | 50,800.00 USD | 50,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 264.46 USD |
| `1D` | `160.43` | 4,130.00 USD | 4,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 598.91 USD |
| `7D` | `160.54` | 51,020.00 USD | 51,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 224.16 USD |
| `1D` | `160.59` | 4,260.00 USD | 4,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 131.92 USD |
| `7D` | `160.71` | 55,630.00 USD | 55,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,610.00 USD |
| `1D` | `160.75` | 5,210.00 USD | 5,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 945.38 USD |
| `7D` | `160.88` | 63,830.00 USD | 63,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,200.00 USD |
| `1D` | `160.91` | 5,250.00 USD | 5,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43.17 USD |
| `7D` | `161.05` | 66,010.00 USD | 66,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,180.00 USD |
| `7D` | `161.22` | 73,760.00 USD | 73,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,740.00 USD |
| `7D` | `162.92` | 73,830.00 USD | 73,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 73.85 USD |
| `7D` | `163.09` | 74,430.00 USD | 74,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 593.08 USD |
| `7D` | `163.43` | 74,440.00 USD | 74,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `1D` | `163.47` | 5,270.00 USD | 5,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17.97 USD |
| `7D` | `163.60` | 74,570.00 USD | 74,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 132.23 USD |
| `1D` | `163.63` | 5,590.00 USD | 5,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 323.31 USD |
| `7D` | `163.77` | 74,900.00 USD | 74,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 329.05 USD |
| `1D` | `163.79` | 5,680.00 USD | 5,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 90.16 USD |
| `7D` | `163.94` | 79,960.00 USD | 79,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,060.00 USD |
| `1D` | `163.95` | 6,110.00 USD | 6,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 426.36 USD |
| `1D` | `164.11` | 6,130.00 USD | 6,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17.52 USD |
| `7D` | `164.11` | 82,180.00 USD | 82,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,220.00 USD |
| `7D` | `164.28` | 84,910.00 USD | 84,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `7D` | `164.45` | 86,050.00 USD | 86,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,140.00 USD |
| `7D` | `172.44` | 86,270.00 USD | 86,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 217.16 USD |
| `7D` | `172.61` | 86,320.00 USD | 86,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 47.72 USD |
| `7D` | `172.78` | 86,320.00 USD | 86,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.35 USD |
| `1D` | `172.91` | 6,130.00 USD | 6,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7.49 USD |
| `7D` | `172.95` | 86,380.00 USD | 86,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 52.89 USD |
| `1D` | `173.07` | 6,260.00 USD | 6,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 126.44 USD |
| `7D` | `173.12` | 86,420.00 USD | 86,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44.83 USD |
| `1D` | `173.16` | 6,280.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14.17 USD |
| `7D` | `173.29` | 87,240.00 USD | 87,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 817.20 USD |
| `7D` | `173.46` | 88,850.00 USD | 88,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,610.00 USD |

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
  * Current Rate: `-35.08` | Last 24h: `-624.43` | Last 3d: `-912.05` | Last 7d: `-912.05`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-0.0117%` | **USDT BingX** | `-` |
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
| `05:00:00` | `157.58` | `157.58` | `157.58` | `157.59` | `157.42` | 1,022,687.71 USD | 946,280.01 USD | 76,407.70 USD | 869,872.31 USD | `+85.06%` | `1B / 0S` |
| `05:00:00` | `157.47` | `157.47` | `157.47` | `157.49` | `157.42` | 157,939.40 USD | 116,165.57 USD | 41,773.83 USD | 74,391.75 USD | `+47.10%` | `1B / 0S` |
| `05:05:00` | `157.52` | `157.52` | `157.52` | `157.54` | `157.45` | 145,072.24 USD | 108,422.41 USD | 36,649.83 USD | 71,772.58 USD | `+49.47%` | `1B / 0S` |
| `05:10:00` | `157.46` | `157.46` | `157.46` | `157.55` | `157.46` | 138,566.56 USD | 16,567.74 USD | 121,998.82 USD | -105,431.08 USD | `-76.09%` | `0B / 1S` |
| `05:15:00` | `157.48` | `157.48` | `157.48` | `157.53` | `157.45` | 262,839.13 USD | 135,153.07 USD | 127,686.05 USD | 7,467.02 USD | `+2.84%` | `1B / 0S` |
| `05:15:00` | `157.49` | `157.49` | `157.49` | `157.49` | `157.45` | 98,272.51 USD | 81,022.55 USD | 17,249.96 USD | 63,772.59 USD | `+64.89%` | `1B / 0S` |
| `05:20:00` | `157.50` | `157.50` | `157.50` | `157.53` | `157.46` | 83,002.50 USD | 47,207.67 USD | 35,794.83 USD | 11,412.84 USD | `+13.75%` | `1B / 0S` |
| `05:25:00` | `157.48` | `157.48` | `157.48` | `157.50` | `157.47` | 81,576.19 USD | 22,579.13 USD | 58,997.07 USD | -36,417.94 USD | `-44.64%` | `0B / 1S` |
| `05:30:00` | `157.48` | `157.48` | `157.48` | `157.53` | `157.46` | 76,849.26 USD | 28,269.55 USD | 48,579.71 USD | -20,310.16 USD | `-26.43%` | `0B / 1S` |
| `05:30:00` | `157.46` | `157.46` | `157.46` | `157.53` | `157.43` | 173,988.88 USD | 54,371.52 USD | 119,617.36 USD | -65,245.83 USD | `-37.50%` | `0B / 1S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 17:30:00 IST` | `4h` | `AGGRESSIVE BUYING` | **`BULLISH`** | USDJPY Macro Delta Flow: AGGRESSIVE BUYI | `157.95` | 2,346,385.47 USD | 2,346,385.47 USD |

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
  * `2026-10-30 11:03:23 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:09:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:10:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `157.24` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `157.06` (Risk Distance: `0.1756` pts)
  * +2.5R Take Profit: `157.68`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.18 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `157.59` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `157.77` (Risk Distance: `0.1756` pts)
  * +2.5R Take Profit: `157.15`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.18 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`158.92`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
