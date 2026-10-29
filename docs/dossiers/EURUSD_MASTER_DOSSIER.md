# 🏛️ SOVEREIGN CANDIDATE DOSSIER: EURUSD
**Canonical Key**: `EURUSD` | **Broker Instrument**: `EURUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 02:36:44 IST` (`2026-10-29 21:06:44 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.12` | **Live Ask Quote**: `1.12` | **Mid Price**: `1.12`
- **Spread Points**: `51.00` | **Spread BPS**: `4.56 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `1.11` | VWAP Z-Score: `+2.12` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.000747` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `61.80` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.12` | Lower -3.00σ Band: `1.11`
  * Upper +2.51σ Band: `1.12` | Lower -2.51σ Band: `1.11`
  * Upper +2.01σ Band: `1.12` | Lower -2.01σ Band: `1.11`
  * Upper +2.00σ Band: `1.12` | Lower -2.00σ Band: `1.11`
  * Upper +1.28σ Band: `1.12` | Lower -1.28σ Band: `1.11`
  * Upper +1.00σ Band: `1.12` | Lower -1.00σ Band: `1.11`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.12` | EMA-20=`1.12` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.12` (Slope: `+0.0000`) | EMA-100=`1.12`
  * Institutional Anchors: EMA-144=`1.11` | EMA-200=`1.11` (Slope: `+0.0229`) | EMA-233=`1.11`
- **Range Boundaries**: 24H High=`1.12` | 24H Low=`1.11` | Weekly High=`1.12` | Weekly Low=`1.11`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.12` (Distance: `-0.02%`)
  * Point of Control (POC) = `1.12` (Distance: `+0.02%`)
  * Value Area Low (VAL) = `1.12` (Distance: `+0.02%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.12` | POC=`1.11` | VAL=`1.11`
  * Prior Day Extremes: PDH=`1.12` | PDL=`1.11` | PDC=`1.12`
  * Monday Range Blueprint: High=`1.12` | Mid=`1.12` | Low=`1.12`
  * Developing Weekly Value Area: Weekly VAH=`1.12` | Weekly POC=`1.11` | Weekly VAL=`1.11`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.12` | Low=`1.12`
  * London Session (08:00-16:00 UTC): High=`1.12` | Low=`1.11`
  * New York Session (13:00-21:00 UTC): High=`1.12` | Low=`1.11`
  * Initial Balance (First Hour): IB High=`1.12` | IB Low=`1.11`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.11` - `1.12`
  * Optimal Trade Entry (OTE 0.705): `1.12`
  * Structural Invalidation Anchor (0.786): `1.13`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `327` | 365.23 USD | 138.54 USD | `+37.93%` | 4,645.97 USD | `+0.60` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `341` | 380.85 USD | -182.81 USD | `-48.00%` | 4,463.16 USD | `-0.73` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `278` | 310.42 USD | -175.02 USD | `-56.38%` | 4,288.14 USD | `-0.80` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `1,177` | 1,314.92 USD | 812.86 USD | `+61.82%` | 11,051.34 USD | `+0.40` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `782` | 873.43 USD | -306.47 USD | `-35.09%` | 10,744.87 USD | `-0.58` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `946` | 1,056.73 USD | 584.98 USD | `+55.36%` | 11,329.85 USD | `+0.19` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `4,883` | 5,451.14 USD | -163.07 USD | `-2.99%` | 6,987.31 USD | `-0.14` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `4,017` | 4,486.67 USD | 1,936.35 USD | `+43.16%` | 8,923.66 USD | `+0.49` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `3,717` | 4,148.80 USD | -3,242.51 USD | `-78.16%` | 5,681.14 USD | `-1.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.11` | `19,887` | 22,130.25 USD | -13,427.34 USD | `-60.67%` | -21,346.53 USD | `-1.65` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.12` | `35,597` | 39,738.71 USD | 24,268.79 USD | `+61.07%` | 2,922.26 USD | `+1.88` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `14,336` | 16,024.64 USD | 7,816.90 USD | `+48.78%` | 10,739.16 USD | `+0.51` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.11` | `13,318` | 14,841.58 USD | -157.89 USD | `-1.06%` | -4,160.52 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.11` | `15,359` | 17,108.39 USD | -3,758.66 USD | `-21.97%` | -7,919.18 USD | `-0.64` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.11` | `19,887` | 22,130.25 USD | -13,427.34 USD | `-60.67%` | -21,346.53 USD | `-1.65` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.12` | `35,597` | 39,738.71 USD | 24,268.79 USD | `+61.07%` | 2,922.26 USD | `+1.88` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `14,336` | 16,024.64 USD | 7,816.90 USD | `+48.78%` | 10,739.16 USD | `+0.51` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:35:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `226` | `0x0911...129a` | `LONG` | 9,951,628.58 USD | `8,898,889.90` | `1.15` | `1.12` | `1.06` | -271,113.85 USD | `-2.72%` | `20X Isolated` |
| `1153` | `0xe03b...ed11` | `SHORT` | 1,947,919.91 USD | `1,741,858.10` | `1.14` | `1.12` | `1.20` | 45,283.41 USD | `+2.32%` | `50X Isolated` |
| `1741` | `0x3f31...a3d7` | `SHORT` | 1,204,078.78 USD | `1,076,512.10` | `1.11` | `1.12` | `1.13` | -4,147.34 USD | `-0.34%` | `50X Isolated` |
| `1835` | `0x9df2...c665` | `SHORT` | 1,118,529.64 USD | `999,937.10` | `1.12` | `1.12` | `1.46` | 2,040.20 USD | `+0.18%` | `5X Isolated` |

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
| `7D` | `1.00` | 97,540.00 USD | 0.00 USD | 97,540.00 USD | 0.00 USD | 0.00 USD | 157.14 USD |
| `7D` | `1.00` | 97,390.00 USD | 0.00 USD | 97,390.00 USD | 0.00 USD | 0.00 USD | 355.64 USD |
| `7D` | `1.00` | 97,030.00 USD | 0.00 USD | 97,030.00 USD | 0.00 USD | 0.00 USD | 1,680.00 USD |
| `7D` | `1.01` | 95,350.00 USD | 0.00 USD | 95,350.00 USD | 0.00 USD | 0.00 USD | 260.94 USD |
| `1D` | `1.01` | 29,170.00 USD | 0.00 USD | 29,170.00 USD | 0.00 USD | 0.00 USD | 167.71 USD |
| `7D` | `1.01` | 95,090.00 USD | 0.00 USD | 95,090.00 USD | 0.00 USD | 0.00 USD | 650.14 USD |
| `1D` | `1.01` | 29,000.00 USD | 0.00 USD | 29,000.00 USD | 0.00 USD | 0.00 USD | 211.33 USD |
| `7D` | `1.01` | 94,440.00 USD | 0.00 USD | 94,440.00 USD | 0.00 USD | 0.00 USD | 490.75 USD |
| `7D` | `1.01` | 93,950.00 USD | 0.00 USD | 93,950.00 USD | 0.00 USD | 0.00 USD | 921.27 USD |
| `7D` | `1.01` | 93,030.00 USD | 0.00 USD | 93,030.00 USD | 0.00 USD | 0.00 USD | 768.71 USD |
| `7D` | `1.01` | 92,260.00 USD | 0.00 USD | 92,260.00 USD | 0.00 USD | 0.00 USD | 343.95 USD |
| `7D` | `1.07` | 91,920.00 USD | 0.00 USD | 91,920.00 USD | 0.00 USD | 0.00 USD | 818.90 USD |
| `7D` | `1.07` | 91,100.00 USD | 0.00 USD | 91,100.00 USD | 0.00 USD | 0.00 USD | 839.06 USD |
| `1D` | `1.07` | 28,790.00 USD | 0.00 USD | 28,790.00 USD | 0.00 USD | 0.00 USD | 779.56 USD |
| `7D` | `1.07` | 90,260.00 USD | 0.00 USD | 90,260.00 USD | 0.00 USD | 0.00 USD | 3,870.00 USD |
| `1D` | `1.07` | 28,010.00 USD | 0.00 USD | 28,010.00 USD | 0.00 USD | 0.00 USD | 2,390.00 USD |
| `7D` | `1.07` | 86,390.00 USD | 0.00 USD | 86,390.00 USD | 0.00 USD | 0.00 USD | 1,010.00 USD |
| `1D` | `1.07` | 25,610.00 USD | 0.00 USD | 25,610.00 USD | 0.00 USD | 0.00 USD | 411.85 USD |
| `7D` | `1.07` | 85,370.00 USD | 0.00 USD | 85,370.00 USD | 0.00 USD | 0.00 USD | 1,230.00 USD |
| `1D` | `1.07` | 25,200.00 USD | 0.00 USD | 25,200.00 USD | 0.00 USD | 0.00 USD | 528.32 USD |
| `7D` | `1.08` | 84,150.00 USD | 0.00 USD | 84,150.00 USD | 0.00 USD | 0.00 USD | 1,230.00 USD |
| `7D` | `1.08` | 82,920.00 USD | 0.00 USD | 82,920.00 USD | 0.00 USD | 0.00 USD | 2,550.00 USD |
| `7D` | `1.08` | 80,370.00 USD | 0.00 USD | 80,370.00 USD | 0.00 USD | 0.00 USD | 2,070.00 USD |
| `7D` | `1.08` | 78,290.00 USD | 0.00 USD | 78,290.00 USD | 0.00 USD | 0.00 USD | 1,020.00 USD |
| `7D` | `1.09` | 77,270.00 USD | 0.00 USD | 77,270.00 USD | 0.00 USD | 0.00 USD | 785.70 USD |
| `7D` | `1.09` | 76,490.00 USD | 0.00 USD | 76,490.00 USD | 0.00 USD | 0.00 USD | 1,780.00 USD |
| `7D` | `1.09` | 74,710.00 USD | 0.00 USD | 74,710.00 USD | 0.00 USD | 0.00 USD | 4,570.00 USD |
| `1D` | `1.09` | 24,670.00 USD | 0.00 USD | 24,670.00 USD | 0.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `1.09` | 70,130.00 USD | 0.00 USD | 70,130.00 USD | 0.00 USD | 0.00 USD | 4,100.00 USD |
| `1D` | `1.10` | 21,650.00 USD | 0.00 USD | 21,650.00 USD | 0.00 USD | 0.00 USD | 4,140.00 USD |
| `7D` | `1.10` | 66,030.00 USD | 0.00 USD | 66,030.00 USD | 0.00 USD | 0.00 USD | 3,190.00 USD |
| `1D` | `1.10` | 17,510.00 USD | 0.00 USD | 17,510.00 USD | 0.00 USD | 0.00 USD | 1,060.00 USD |
| `7D` | `1.10` | 62,840.00 USD | 0.00 USD | 62,840.00 USD | 0.00 USD | 0.00 USD | 3,570.00 USD |
| `1D` | `1.10` | 16,460.00 USD | 0.00 USD | 16,460.00 USD | 0.00 USD | 0.00 USD | 9.20 USD |
| `7D` | `1.10` | 59,270.00 USD | 0.00 USD | 59,270.00 USD | 0.00 USD | 0.00 USD | 215.30 USD |
| `7D` | `1.10` | 59,060.00 USD | 0.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD | 5,780.00 USD |
| `7D` | `1.10` | 53,280.00 USD | 0.00 USD | 53,280.00 USD | 0.00 USD | 0.00 USD | 3,450.00 USD |
| `7D` | `1.10` | 49,830.00 USD | 0.00 USD | 49,830.00 USD | 0.00 USD | 0.00 USD | 1,850.00 USD |
| `7D` | `1.10` | 47,980.00 USD | 0.00 USD | 47,980.00 USD | 0.00 USD | 0.00 USD | 3,280.00 USD |
| `7D` | `1.10` | 44,700.00 USD | 0.00 USD | 44,700.00 USD | 0.00 USD | 0.00 USD | 10,080.00 USD |
| `1D` | `1.10` | 16,450.00 USD | 0.00 USD | 16,450.00 USD | 0.00 USD | 0.00 USD | 5,880.00 USD |
| `7D` | `1.11` | 34,620.00 USD | 0.00 USD | 34,620.00 USD | 0.00 USD | 0.00 USD | 8,760.00 USD |
| `1D` | `1.11` | 10,570.00 USD | 0.00 USD | 10,570.00 USD | 0.00 USD | 0.00 USD | 6,910.00 USD |
| `7D` | `1.11` | 25,860.00 USD | 0.00 USD | 25,860.00 USD | 0.00 USD | 0.00 USD | 4,050.00 USD |
| `1D` | `1.11` | 3,660.00 USD | 0.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD | 1,550.00 USD |
| `7D` | `1.11` | 21,810.00 USD | 0.00 USD | 21,810.00 USD | 0.00 USD | 0.00 USD | 4,910.00 USD |
| `1D` | `1.11` | 2,110.00 USD | 0.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD | 2,110.00 USD |
| `7D` | `1.11` | 16,890.00 USD | 0.00 USD | 16,890.00 USD | 0.00 USD | 0.00 USD | 4,910.00 USD |
| `7D` | `1.11` | 11,990.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD | 0.00 USD | 10,210.00 USD |
| `7D` | `1.11` | 1,770.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD | 1,770.00 USD |
| `1D` | `1.12` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.12` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.12` | 1,570.00 USD | 1,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,570.00 USD |
| `7D` | `1.13` | 5,130.00 USD | 5,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,560.00 USD |
| `7D` | `1.13` | 14,270.00 USD | 14,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,150.00 USD |
| `1D` | `1.13` | 6,060.00 USD | 6,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,060.00 USD |
| `7D` | `1.13` | 22,870.00 USD | 22,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,600.00 USD |
| `1D` | `1.13` | 14,320.00 USD | 14,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,260.00 USD |
| `7D` | `1.13` | 28,850.00 USD | 28,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,980.00 USD |
| `1D` | `1.13` | 16,430.00 USD | 16,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,110.00 USD |
| `7D` | `1.13` | 35,990.00 USD | 35,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,140.00 USD |
| `1D` | `1.13` | 16,450.00 USD | 16,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18.40 USD |
| `7D` | `1.13` | 36,420.00 USD | 36,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 430.60 USD |
| `7D` | `1.13` | 47,980.00 USD | 47,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,560.00 USD |
| `7D` | `1.13` | 54,880.00 USD | 54,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,900.00 USD |
| `7D` | `1.14` | 58,580.00 USD | 58,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,700.00 USD |
| `7D` | `1.14` | 60,220.00 USD | 60,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,640.00 USD |
| `7D` | `1.14` | 65,720.00 USD | 65,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD |
| `1D` | `1.14` | 19,400.00 USD | 19,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,950.00 USD |
| `7D` | `1.14` | 69,640.00 USD | 69,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,920.00 USD |
| `1D` | `1.14` | 22,840.00 USD | 22,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,440.00 USD |
| `7D` | `1.14` | 71,670.00 USD | 71,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,030.00 USD |
| `1D` | `1.14` | 23,620.00 USD | 23,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 774.06 USD |
| `7D` | `1.14` | 74,130.00 USD | 74,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,460.00 USD |
| `1D` | `1.14` | 24,670.00 USD | 24,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,060.00 USD |
| `7D` | `1.14` | 76,580.00 USD | 76,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,450.00 USD |
| `7D` | `1.14` | 81,690.00 USD | 81,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,110.00 USD |
| `7D` | `1.14` | 85,560.00 USD | 85,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD |
| `7D` | `1.15` | 86,400.00 USD | 86,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 840.16 USD |
| `7D` | `1.15` | 87,870.00 USD | 87,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,470.00 USD |
| `7D` | `1.16` | 88,270.00 USD | 88,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 392.85 USD |
| `7D` | `1.16` | 89,160.00 USD | 89,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 889.09 USD |
| `1D` | `1.16` | 25,450.00 USD | 25,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 776.05 USD |
| `7D` | `1.16` | 92,290.00 USD | 92,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,140.00 USD |
| `1D` | `1.16` | 27,110.00 USD | 27,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,660.00 USD |
| `7D` | `1.16` | 93,590.00 USD | 93,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,300.00 USD |
| `1D` | `1.16` | 28,250.00 USD | 28,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,150.00 USD |
| `7D` | `1.16` | 95,260.00 USD | 95,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,670.00 USD |
| `1D` | `1.16` | 28,780.00 USD | 28,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 527.80 USD |
| `7D` | `1.16` | 96,870.00 USD | 96,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,610.00 USD |
| `1D` | `1.17` | 28,790.00 USD | 28,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4.60 USD |
| `7D` | `1.17` | 96,980.00 USD | 96,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 107.65 USD |
| `7D` | `1.17` | 99,870.00 USD | 99,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,890.00 USD |
| `7D` | `1.17` | 101,540.00 USD | 101,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,670.00 USD |
| `7D` | `1.17` | 102,520.00 USD | 102,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 977.74 USD |
| `7D` | `1.23` | 102,850.00 USD | 102,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 327.56 USD |
| `7D` | `1.23` | 103,110.00 USD | 103,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 266.58 USD |
| `1D` | `1.23` | 29,100.00 USD | 29,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 310.42 USD |
| `7D` | `1.23` | 104,710.00 USD | 104,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,600.00 USD |
| `1D` | `1.23` | 30,050.00 USD | 30,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 951.29 USD |
| `7D` | `1.23` | 104,800.00 USD | 104,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 89.77 USD |
| `1D` | `1.23` | 30,220.00 USD | 30,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 168.41 USD |
| `7D` | `1.23` | 105,470.00 USD | 105,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 668.22 USD |
| `1D` | `1.23` | 30,430.00 USD | 30,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 211.46 USD |
| `7D` | `1.23` | 106,110.00 USD | 106,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 643.84 USD |
| `7D` | `1.23` | 106,150.00 USD | 106,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 37.22 USD |
| `7D` | `1.23` | 107,040.00 USD | 107,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 884.05 USD |

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
  * Current Rate: `0.00` | Last 24h: `95.44` | Last 3d: `265.06` | Last 7d: `325.21`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0000%` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0000%` | **USDT Bitget** | `0.0000%` |
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
| 15m Bar | Interbank Tick Flow | - | - | - | - | - | - | - | - | 0.00% | Balanced Interbank Imbalance |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| Live | 15m | Tape Flow | NEUTRAL | Orderflow balanced at current level | - | 0.00 USD | 0.00 USD |

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
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:30:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1.12` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1.12` (Risk Distance: `0.0017` pts)
  * +2.5R Take Profit: `1.12`
  * Mathematical Lot Sizing: **`0.06 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.12` (Risk Distance: `0.0017` pts)
  * +2.5R Take Profit: `1.11`
  * Mathematical Lot Sizing: **`0.06 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.13`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
