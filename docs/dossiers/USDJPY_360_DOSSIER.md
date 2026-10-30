# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USDJPY
**Canonical Key**: `USDJPY` | **Broker Instrument**: `USDJPY.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 17:28:17 IST` (`2026-10-30 11:58:17 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `157.06` | **Live Ask Quote**: `157.06` | **Mid Price**: `157.06`
- **Spread Points**: `2.00` | **Spread BPS**: `0.13 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `157.41` | VWAP Z-Score: `-2.04` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.1394` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `35.98` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `157.90` | Lower -3.00σ Band: `156.91`
  * Upper +2.51σ Band: `157.82` | Lower -2.51σ Band: `156.99`
  * Upper +2.01σ Band: `157.74` | Lower -2.01σ Band: `157.08`
  * Upper +2.00σ Band: `157.73` | Lower -2.00σ Band: `157.08`
  * Upper +1.28σ Band: `157.62` | Lower -1.28σ Band: `157.20`
  * Upper +1.00σ Band: `157.57` | Lower -1.00σ Band: `157.24`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`157.20` | EMA-20=`157.30` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`157.43` (Slope: `+0.0000`) | EMA-100=`157.57`
  * Institutional Anchors: EMA-144=`157.64` | EMA-200=`157.69` (Slope: `-0.0365`) | EMA-233=`157.72`
- **Range Boundaries**: 24H High=`158.13` | 24H Low=`156.99` | Weekly High=`158.35` | Weekly Low=`156.99`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `157.65` (Distance: `-0.37%`)
  * Point of Control (POC) = `157.34` (Distance: `-0.17%`)
  * Value Area Low (VAL) = `157.24` (Distance: `-0.11%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`157.99` | POC=`157.87` | VAL=`157.76`
  * Prior Day Extremes: PDH=`158.13` | PDL=`157.60` | PDC=`157.69`
  * Monday Range Blueprint: High=`157.64` | Mid=`157.15` | Low=`156.65`
  * Developing Weekly Value Area: Weekly VAH=`158.03` | Weekly POC=`157.87` | Weekly VAL=`157.38`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`157.90` | Low=`157.12`
  * London Session (08:00-16:00 UTC): High=`157.75` | Low=`156.99`
  * New York Session (13:00-21:00 UTC): High=`157.36` | Low=`156.99`
  * Initial Balance (First Hour): IB High=`157.70` | IB Low=`157.40`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `156.43` - `157.69`
  * Optimal Trade Entry (OTE 0.705): `157.38`
  * Structural Invalidation Anchor (0.786): `158.32`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `157.27` | `157.35` | `157.24` | `157.33` | `690` | 108,559.77 USD | 72,025.23 USD | `+66.35%` | 198,301.06 USD | `+1.53` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `157.33` | `157.35` | `157.21` | `157.21` | `727` | 114,290.22 USD | -102,861.19 USD | `-90.00%` | 95,439.86 USD | `-1.22` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `157.21` | `157.26` | `157.20` | `157.25` | `314` | 49,375.56 USD | 30,859.72 USD | `+62.50%` | 126,299.59 USD | `+0.82` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `157.43` | `157.43` | `157.17` | `157.19` | `2,794` | 439,174.89 USD | -395,257.40 USD | `-90.00%` | -1,123,009.85 USD | `-2.08` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `157.19` | `157.35` | `157.16` | `157.33` | `2,529` | 397,895.16 USD | 331,945.68 USD | `+83.43%` | -791,064.17 USD | `+1.92` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `157.33` | `157.35` | `157.20` | `157.28` | `1,380` | 217,051.92 USD | -19,798.65 USD | `-9.12%` | -810,862.83 USD | `+0.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `157.62` | `157.71` | `157.47` | `157.67` | `8,064` | 1,271,458.94 USD | 557,244.35 USD | `+43.83%` | 2,784,643.74 USD | `+0.73` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `157.67` | `157.75` | `157.44` | `157.55` | `6,987` | 1,100,801.85 USD | -368,732.65 USD | `-33.50%` | 2,415,911.09 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `157.55` | `157.58` | `157.16` | `157.28` | `9,162` | 1,441,036.01 USD | -770,625.97 USD | `-53.48%` | 1,645,285.12 USD | `-1.15` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.64` | `157.90` | `157.31` | `157.36` | `20,459` | 3,219,366.86 USD | -2,125,220.88 USD | `-66.01%` | -2,765,043.25 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.36` | `157.63` | `157.12` | `157.43` | `39,720` | 6,253,000.44 USD | 1,103,833.41 USD | `+17.65%` | -1,661,209.84 USD | `+0.69` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `157.43` | `157.75` | `157.16` | `157.28` | `32,041` | 5,039,536.64 USD | -2,107,047.65 USD | `-41.81%` | -3,768,257.49 USD | `-0.73` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `158.06` | `158.13` | `157.71` | `157.88` | `37,561` | 5,930,280.92 USD | -1,786,229.19 USD | `-30.12%` | 1,308,304.60 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.88` | `157.98` | `157.63` | `157.69` | `20,300` | 3,201,147.60 USD | -1,948,126.97 USD | `-60.86%` | -639,822.37 USD | `-0.74` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.64` | `157.90` | `157.31` | `157.36` | `20,459` | 3,219,366.86 USD | -2,125,220.88 USD | `-66.01%` | -2,765,043.25 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `157.36` | `157.63` | `157.12` | `157.43` | `39,720` | 6,253,000.44 USD | 1,103,833.41 USD | `+17.65%` | -1,661,209.84 USD | `+0.69` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `157.43` | `157.75` | `157.16` | `157.28` | `32,041` | 5,039,536.64 USD | -2,107,047.65 USD | `-41.81%` | -3,768,257.49 USD | `-0.73` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `200` | `0x0911...129a` | `SHORT` | 10,398,366.86 USD | `66,223.20` | `156.58` | `157.01` | `167.71` | -29,346.63 USD | `-0.28%` | `20X Isolated` |
| `1019` | `0x9dea...d617` | `LONG` | 2,130,422.87 USD | `13,566.98` | `157.66` | `157.01` | `149.21` | -8,590.88 USD | `-0.40%` | `50X Isolated` |
| `1093` | `0xec0b...b078` | `SHORT` | 1,981,324.45 USD | `12,617.49` | `158.22` | `157.01` | `162.94` | 15,041.22 USD | `+0.76%` | `20X Isolated` |
| `1160` | `0xc966...f6b6` | `SHORT` | 1,896,073.03 USD | `12,075.36` | `157.61` | `157.01` | `215.26` | 7,069.67 USD | `+0.37%` | `5X Isolated` |
| `1176` | `0xbef1...d2e5` | `LONG` | 1,856,178.96 USD | `11,821.29` | `157.63` | `157.01` | `155.50` | -7,181.65 USD | `-0.39%` | `50X Isolated` |
| `1879` | `0x3d89...eb14` | `LONG` | 1,083,231.00 USD | `6,900.00` | `158.17` | `157.01` | `127.34` | -8,158.60 USD | `-0.75%` | `5X Isolated` |

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
| `7D` | `141.42` | 90,340.00 USD | 0.00 USD | 90,340.00 USD | 0.00 USD | 0.00 USD | 5.35 USD |
| `1D` | `141.44` | 5,640.00 USD | 0.00 USD | 5,640.00 USD | 0.00 USD | 0.00 USD | 6.71 USD |
| `7D` | `141.59` | 90,340.00 USD | 0.00 USD | 90,340.00 USD | 0.00 USD | 0.00 USD | 52.93 USD |
| `1D` | `141.60` | 5,640.00 USD | 0.00 USD | 5,640.00 USD | 0.00 USD | 0.00 USD | 127.68 USD |
| `1D` | `141.76` | 5,510.00 USD | 0.00 USD | 5,510.00 USD | 0.00 USD | 0.00 USD | 85.61 USD |
| `7D` | `141.76` | 90,280.00 USD | 0.00 USD | 90,280.00 USD | 0.00 USD | 0.00 USD | 176.77 USD |
| `1D` | `141.92` | 5,420.00 USD | 0.00 USD | 5,420.00 USD | 0.00 USD | 0.00 USD | 74.04 USD |
| `7D` | `141.93` | 90,110.00 USD | 0.00 USD | 90,110.00 USD | 0.00 USD | 0.00 USD | 2,180.00 USD |
| `1D` | `142.08` | 5,350.00 USD | 0.00 USD | 5,350.00 USD | 0.00 USD | 0.00 USD | 3.39 USD |
| `7D` | `142.10` | 87,930.00 USD | 0.00 USD | 87,930.00 USD | 0.00 USD | 0.00 USD | 1,010.00 USD |
| `7D` | `142.27` | 86,920.00 USD | 0.00 USD | 86,920.00 USD | 0.00 USD | 0.00 USD | 882.31 USD |
| `7D` | `150.43` | 86,040.00 USD | 0.00 USD | 86,040.00 USD | 0.00 USD | 0.00 USD | 420.80 USD |
| `7D` | `150.60` | 85,610.00 USD | 0.00 USD | 85,610.00 USD | 0.00 USD | 0.00 USD | 246.16 USD |
| `1D` | `150.88` | 5,340.00 USD | 0.00 USD | 5,340.00 USD | 0.00 USD | 0.00 USD | 19.11 USD |
| `7D` | `150.94` | 85,370.00 USD | 0.00 USD | 85,370.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `1D` | `151.04` | 5,330.00 USD | 0.00 USD | 5,330.00 USD | 0.00 USD | 0.00 USD | 323.31 USD |
| `7D` | `151.11` | 85,360.00 USD | 0.00 USD | 85,360.00 USD | 0.00 USD | 0.00 USD | 402.91 USD |
| `1D` | `151.20` | 5,000.00 USD | 0.00 USD | 5,000.00 USD | 0.00 USD | 0.00 USD | 214.09 USD |
| `7D` | `151.28` | 84,950.00 USD | 0.00 USD | 84,950.00 USD | 0.00 USD | 0.00 USD | 3,570.00 USD |
| `1D` | `151.36` | 4,790.00 USD | 0.00 USD | 4,790.00 USD | 0.00 USD | 0.00 USD | 191.00 USD |
| `7D` | `151.45` | 81,380.00 USD | 0.00 USD | 81,380.00 USD | 0.00 USD | 0.00 USD | 4,900.00 USD |
| `1D` | `151.52` | 4,600.00 USD | 0.00 USD | 4,600.00 USD | 0.00 USD | 0.00 USD | 16.01 USD |
| `7D` | `151.62` | 76,480.00 USD | 0.00 USD | 76,480.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `7D` | `153.49` | 73,740.00 USD | 0.00 USD | 73,740.00 USD | 0.00 USD | 0.00 USD | 116.22 USD |
| `7D` | `153.66` | 73,630.00 USD | 0.00 USD | 73,630.00 USD | 0.00 USD | 0.00 USD | 979.02 USD |
| `7D` | `153.83` | 72,650.00 USD | 0.00 USD | 72,650.00 USD | 0.00 USD | 0.00 USD | 238.69 USD |
| `7D` | `154.00` | 72,410.00 USD | 0.00 USD | 72,410.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `1D` | `154.08` | 4,580.00 USD | 0.00 USD | 4,580.00 USD | 0.00 USD | 0.00 USD | 71.03 USD |
| `7D` | `154.17` | 72,380.00 USD | 0.00 USD | 72,380.00 USD | 0.00 USD | 0.00 USD | 264.63 USD |
| `1D` | `154.24` | 4,510.00 USD | 0.00 USD | 4,510.00 USD | 0.00 USD | 0.00 USD | 668.64 USD |
| `7D` | `154.34` | 72,120.00 USD | 0.00 USD | 72,120.00 USD | 0.00 USD | 0.00 USD | 980.16 USD |
| `1D` | `154.40` | 3,840.00 USD | 0.00 USD | 3,840.00 USD | 0.00 USD | 0.00 USD | 436.07 USD |
| `7D` | `154.51` | 71,140.00 USD | 0.00 USD | 71,140.00 USD | 0.00 USD | 0.00 USD | 10,950.00 USD |
| `1D` | `154.56` | 3,410.00 USD | 0.00 USD | 3,410.00 USD | 0.00 USD | 0.00 USD | 351.35 USD |
| `7D` | `154.68` | 60,190.00 USD | 0.00 USD | 60,190.00 USD | 0.00 USD | 0.00 USD | 5,550.00 USD |
| `7D` | `154.85` | 54,630.00 USD | 0.00 USD | 54,630.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD |
| `7D` | `155.19` | 49,160.00 USD | 0.00 USD | 49,160.00 USD | 0.00 USD | 0.00 USD | 2,190.00 USD |
| `7D` | `155.36` | 46,980.00 USD | 0.00 USD | 46,980.00 USD | 0.00 USD | 0.00 USD | 482.11 USD |
| `7D` | `155.53` | 46,500.00 USD | 0.00 USD | 46,500.00 USD | 0.00 USD | 0.00 USD | 53.53 USD |
| `1D` | `155.68` | 3,050.00 USD | 0.00 USD | 3,050.00 USD | 0.00 USD | 0.00 USD | 1,260.00 USD |
| `7D` | `155.70` | 46,440.00 USD | 0.00 USD | 46,440.00 USD | 0.00 USD | 0.00 USD | 220.39 USD |
| `1D` | `155.84` | 1,790.00 USD | 0.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | 638.15 USD |
| `7D` | `155.87` | 46,220.00 USD | 0.00 USD | 46,220.00 USD | 0.00 USD | 0.00 USD | 2,000.00 USD |
| `1D` | `156.00` | 1,150.00 USD | 0.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | 971.23 USD |
| `7D` | `156.04` | 44,230.00 USD | 0.00 USD | 44,230.00 USD | 0.00 USD | 0.00 USD | 15,050.00 USD |
| `1D` | `156.16` | 179.88 USD | 0.00 USD | 179.88 USD | 0.00 USD | 0.00 USD | 179.88 USD |
| `7D` | `156.21` | 29,170.00 USD | 0.00 USD | 29,170.00 USD | 0.00 USD | 0.00 USD | 18,240.00 USD |
| `7D` | `156.38` | 10,940.00 USD | 0.00 USD | 10,940.00 USD | 0.00 USD | 0.00 USD | 10,940.00 USD |
| `1D` | `157.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `157.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `158.25` | 954.59 USD | 954.59 USD | 0.00 USD | 0.00 USD | 0.00 USD | 954.59 USD |
| `7D` | `158.42` | 2,190.00 USD | 2,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240.00 USD |
| `7D` | `158.59` | 2,670.00 USD | 2,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 477.37 USD |
| `1D` | `158.72` | 67.12 USD | 67.12 USD | 0.00 USD | 0.00 USD | 0.00 USD | 67.12 USD |
| `7D` | `158.76` | 2,720.00 USD | 2,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 53.53 USD |
| `1D` | `158.88` | 1,290.00 USD | 1,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,220.00 USD |
| `7D` | `158.93` | 3,700.00 USD | 3,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 977.64 USD |
| `1D` | `159.04` | 1,950.00 USD | 1,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 662.79 USD |
| `7D` | `159.10` | 5,620.00 USD | 5,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,920.00 USD |
| `1D` | `159.20` | 2,970.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,020.00 USD |
| `7D` | `159.27` | 27,930.00 USD | 27,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,310.00 USD |
| `1D` | `159.36` | 3,050.00 USD | 3,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 79.79 USD |
| `7D` | `159.44` | 38,230.00 USD | 38,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,290.00 USD |
| `7D` | `159.61` | 49,160.00 USD | 49,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,940.00 USD |
| `7D` | `159.78` | 49,360.00 USD | 49,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 199.19 USD |
| `7D` | `159.95` | 50,260.00 USD | 50,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 896.05 USD |
| `7D` | `160.12` | 50,500.00 USD | 50,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 238.69 USD |
| `7D` | `160.29` | 50,520.00 USD | 50,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.76 USD |
| `1D` | `160.32` | 3,090.00 USD | 3,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 38.23 USD |
| `7D` | `160.46` | 50,630.00 USD | 50,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 110.19 USD |
| `1D` | `160.48` | 3,740.00 USD | 3,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 646.62 USD |
| `7D` | `160.63` | 51,750.00 USD | 51,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD |
| `1D` | `160.64` | 4,130.00 USD | 4,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 390.14 USD |
| `1D` | `160.80` | 4,550.00 USD | 4,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 420.07 USD |
| `7D` | `160.80` | 62,600.00 USD | 62,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,850.00 USD |
| `1D` | `160.96` | 4,580.00 USD | 4,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 32.03 USD |
| `7D` | `160.97` | 68,280.00 USD | 68,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,670.00 USD |
| `7D` | `161.14` | 73,740.00 USD | 73,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD |
| `7D` | `163.01` | 74,290.00 USD | 74,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 544.08 USD |
| `7D` | `163.18` | 74,410.00 USD | 74,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 122.88 USD |
| `7D` | `163.35` | 74,420.00 USD | 74,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.38 USD |
| `1D` | `163.52` | 4,620.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 35.51 USD |
| `1D` | `163.68` | 4,920.00 USD | 4,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 306.91 USD |
| `7D` | `163.69` | 74,830.00 USD | 74,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 402.91 USD |
| `1D` | `163.84` | 5,170.00 USD | 5,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 245.45 USD |
| `7D` | `163.86` | 77,560.00 USD | 77,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `1D` | `164.00` | 5,340.00 USD | 5,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 167.17 USD |
| `7D` | `164.03` | 82,250.00 USD | 82,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,690.00 USD |
| `1D` | `164.16` | 5,340.00 USD | 5,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8.48 USD |
| `7D` | `164.20` | 83,300.00 USD | 83,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,050.00 USD |
| `7D` | `164.37` | 86,040.00 USD | 86,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD |
| `7D` | `172.36` | 86,180.00 USD | 86,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 144.82 USD |
| `7D` | `172.53` | 86,250.00 USD | 86,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 72.30 USD |
| `7D` | `172.70` | 86,300.00 USD | 86,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 47.74 USD |
| `7D` | `172.87` | 86,310.00 USD | 86,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.35 USD |
| `1D` | `172.94` | 5,360.00 USD | 5,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14.20 USD |
| `7D` | `173.04` | 86,330.00 USD | 86,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22.04 USD |
| `7D` | `173.21` | 86,520.00 USD | 86,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 188.22 USD |
| `7D` | `173.26` | 86,540.00 USD | 86,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19.44 USD |

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
  * Current Rate: `0.00` | Last 24h: `-325.46` | Last 3d: `-948.57` | Last 7d: `-948.57`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-0.0137%` | **USDT BingX** | `-` |
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
| `10:40:00` | `157.64` | `157.64` | `157.64` | `157.65` | `157.54` | 82,285.99 USD | 71,651.57 USD | 10,634.42 USD | 61,017.16 USD | `+74.15%` | `1B / 0S` |
| `10:45:00` | `157.55` | `157.55` | `157.55` | `157.67` | `157.55` | 281,384.30 USD | 23,836.27 USD | 257,548.03 USD | -233,711.75 USD | `-83.06%` | `0B / 1S` |
| `10:45:00` | `157.63` | `157.63` | `157.63` | `157.67` | `157.61` | 94,417.97 USD | 31,886.77 USD | 62,531.20 USD | -30,644.43 USD | `-32.46%` | `0B / 1S` |
| `10:50:00` | `157.60` | `157.60` | `157.60` | `157.63` | `157.57` | 84,160.54 USD | 35,400.86 USD | 48,759.68 USD | -13,358.82 USD | `-15.87%` | `0B / 1S` |
| `10:55:00` | `157.55` | `157.55` | `157.55` | `157.62` | `157.55` | 102,880.15 USD | 8,684.69 USD | 94,195.46 USD | -85,510.77 USD | `-83.12%` | `0B / 1S` |
| `11:00:00` | `157.43` | `157.43` | `157.43` | `157.58` | `157.41` | 387,108.08 USD | 36,867.44 USD | 350,240.64 USD | -313,373.20 USD | `-80.95%` | `0B / 1S` |
| `11:00:00` | `157.54` | `157.54` | `157.54` | `157.58` | `157.52` | 146,988.55 USD | 61,828.52 USD | 85,160.03 USD | -23,331.52 USD | `-15.87%` | `0B / 1S` |
| `11:00:00` | `157.28` | `157.28` | `157.28` | `157.58` | `157.16` | 1,441,036.01 USD | 335,205.02 USD | 1,105,830.99 USD | -770,625.97 USD | `-53.48%` | `0B / 1S` |
| `11:05:00` | `157.52` | `157.52` | `157.52` | `157.58` | `157.52` | 98,765.04 USD | 15,902.85 USD | 82,862.19 USD | -66,959.35 USD | `-67.80%` | `0B / 1S` |
| `11:10:00` | `157.43` | `157.43` | `157.43` | `157.53` | `157.41` | 141,525.08 USD | 12,414.48 USD | 129,110.59 USD | -116,696.11 USD | `-82.46%` | `0B / 1S` |

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
  * `2026-10-30 16:36:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:03 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:49:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `157.07` (Risk Distance: `0.1703` pts)
  * +2.5R Take Profit: `157.67`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.17 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `157.65` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `157.82` (Risk Distance: `0.1703` pts)
  * +2.5R Take Profit: `157.23`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.17 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`158.32`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
