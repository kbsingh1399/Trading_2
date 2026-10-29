# 🏛️ SOVEREIGN CANDIDATE DOSSIER: EURUSD
**Canonical Key**: `EURUSD` | **Broker Instrument**: `EURUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-29 22:45:59 IST` (`2026-10-29 17:15:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.12` | **Live Ask Quote**: `1.12` | **Mid Price**: `1.12`
- **Spread Points**: `1.00` | **Spread BPS**: `0.09 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `1.11` | VWAP Z-Score: `+1.63` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0010` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `59.50` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.12` | Lower -3.00σ Band: `1.11`
  * Upper +2.51σ Band: `1.12` | Lower -2.51σ Band: `1.11`
  * Upper +2.01σ Band: `1.12` | Lower -2.01σ Band: `1.11`
  * Upper +2.00σ Band: `1.12` | Lower -2.00σ Band: `1.11`
  * Upper +1.28σ Band: `1.12` | Lower -1.28σ Band: `1.11`
  * Upper +1.00σ Band: `1.12` | Lower -1.00σ Band: `1.11`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.12` | EMA-20=`1.12` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.11` (Slope: `+0.0000`) | EMA-100=`1.11`
  * Institutional Anchors: EMA-144=`1.11` | EMA-200=`1.11` (Slope: `+0.0155`) | EMA-233=`1.11`
- **Range Boundaries**: 24H High=`1.12` | 24H Low=`1.11` | Weekly High=`1.12` | Weekly Low=`1.11`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.12` (Distance: `+0.12%`)
  * Point of Control (POC) = `1.11` (Distance: `+0.26%`)
  * Value Area Low (VAL) = `1.11` (Distance: `+0.35%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.12` | POC=`1.11` | VAL=`1.11`
  * Prior Day Extremes: PDH=`1.12` | PDL=`1.11` | PDC=`1.12`
  * Monday Range Blueprint: High=`1.12` | Mid=`1.12` | Low=`1.12`
  * Developing Weekly Value Area: Weekly VAH=`1.12` | Weekly POC=`1.11` | Weekly VAL=`1.11`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.12` | Low=`1.11`
  * London Session (08:00-16:00 UTC): High=`1.12` | Low=`1.11`
  * New York Session (13:00-21:00 UTC): High=`1.12` | Low=`1.11`
  * Initial Balance (First Hour): IB High=`1.11` | IB Low=`1.11`
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
| `5m` | `1.11` | `1.11` | `1.11` | `1.11` | `1,029` | 1,145.35 USD | -433.84 USD | `-37.88%` | 2,715.63 USD | `-0.58` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.11` | `1.11` | `1.11` | `1.11` | `1,092` | 1,216.82 USD | 991.18 USD | `+81.46%` | 3,706.81 USD | `+1.26` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.11` | `1.11` | `1.11` | `1.11` | `968` | 1,078.09 USD | -524.73 USD | `-48.67%` | 3,182.08 USD | `-0.72` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.11` | `1.11` | `1.11` | `1.11` | `3,893` | 4,328.90 USD | -2,532.87 USD | `-58.51%` | 2,520.23 USD | `-2.38` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.11` | `1.11` | `1.11` | `1.11` | `3,372` | 3,754.86 USD | 3,081.43 USD | `+82.07%` | 5,601.67 USD | `+2.41` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.11` | `1.11` | `1.11` | `1.11` | `3,089` | 3,440.31 USD | 344.03 USD | `+10.00%` | 5,945.70 USD | `+0.16` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.11` | `1.11` | `1.11` | `1.11` | `6,887` | 7,663.85 USD | -5,925.14 USD | `-77.31%` | -1,315.41 USD | `-2.09` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.11` | `1.11` | `1.11` | `1.11` | `12,682` | 14,121.91 USD | 7,835.94 USD | `+55.49%` | 6,520.53 USD | `+2.39` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.11` | `1.12` | `1.11` | `1.12` | `9,481` | 10,581.65 USD | 6,918.77 USD | `+65.38%` | 13,439.31 USD | `+1.94` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.11` | `15,359` | 17,108.39 USD | -3,758.66 USD | `-21.97%` | -788.33 USD | `-0.79` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.11` | `19,887` | 22,130.25 USD | -13,427.34 USD | `-60.67%` | -14,215.68 USD | `-1.59` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.12` | `35,597` | 39,738.71 USD | 24,268.79 USD | `+61.07%` | 10,053.12 USD | `+1.92` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.11` | `1.11` | `6,905` | 7,691.89 USD | -4,002.63 USD | `-52.04%` | 3,128.22 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.11` | `13,318` | 14,841.58 USD | -157.89 USD | `-1.06%` | 2,970.33 USD | `-0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.11` | `15,359` | 17,108.39 USD | -3,758.66 USD | `-21.97%` | -788.33 USD | `-0.79` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.11` | `19,887` | 22,130.25 USD | -13,427.34 USD | `-60.67%` | -14,215.68 USD | `-1.59` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.12` | `35,597` | 39,738.71 USD | 24,268.79 USD | `+61.07%` | 10,053.12 USD | `+1.92` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:44:58 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `242` | `0x0911...129a` | `LONG` | 9,938,280.24 USD | `8,898,889.90` | `1.15` | `1.12` | `1.06` | -284,462.18 USD | `-2.86%` | `20X Isolated` |
| `1186` | `0xe03b...ed11` | `SHORT` | 1,955,384.53 USD | `1,750,724.80` | `1.14` | `1.12` | `1.20` | 47,964.93 USD | `+2.45%` | `50X Isolated` |
| `1806` | `0x3f31...a3d7` | `SHORT` | 1,202,248.71 USD | `1,076,512.10` | `1.11` | `1.12` | `1.13` | -2,317.27 USD | `-0.19%` | `50X Isolated` |
| `1906` | `0x9df2...c665` | `SHORT` | 1,116,729.75 USD | `999,937.10` | `1.12` | `1.12` | `1.46` | 3,840.08 USD | `+0.34%` | `5X Isolated` |

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
| `1D` | `1.01` | 31,610.00 USD | 0.00 USD | 31,610.00 USD | 0.00 USD | 0.00 USD | 387.33 USD |
| `7D` | `1.01` | 31,610.00 USD | 0.00 USD | 31,610.00 USD | 0.00 USD | 0.00 USD | 387.33 USD |
| `1D` | `1.07` | 31,220.00 USD | 0.00 USD | 31,220.00 USD | 0.00 USD | 0.00 USD | 203.99 USD |
| `7D` | `1.07` | 31,220.00 USD | 0.00 USD | 31,220.00 USD | 0.00 USD | 0.00 USD | 203.99 USD |
| `1D` | `1.07` | 31,020.00 USD | 0.00 USD | 31,020.00 USD | 0.00 USD | 0.00 USD | 1,600.00 USD |
| `7D` | `1.07` | 31,020.00 USD | 0.00 USD | 31,020.00 USD | 0.00 USD | 0.00 USD | 1,600.00 USD |
| `1D` | `1.07` | 29,420.00 USD | 0.00 USD | 29,420.00 USD | 0.00 USD | 0.00 USD | 2,060.00 USD |
| `7D` | `1.07` | 29,420.00 USD | 0.00 USD | 29,420.00 USD | 0.00 USD | 0.00 USD | 2,060.00 USD |
| `1D` | `1.07` | 27,350.00 USD | 0.00 USD | 27,350.00 USD | 0.00 USD | 0.00 USD | 592.47 USD |
| `7D` | `1.07` | 27,350.00 USD | 0.00 USD | 27,350.00 USD | 0.00 USD | 0.00 USD | 592.47 USD |
| `1D` | `1.09` | 26,760.00 USD | 0.00 USD | 26,760.00 USD | 0.00 USD | 0.00 USD | 2,140.00 USD |
| `7D` | `1.09` | 26,760.00 USD | 0.00 USD | 26,760.00 USD | 0.00 USD | 0.00 USD | 2,140.00 USD |
| `1D` | `1.09` | 24,620.00 USD | 0.00 USD | 24,620.00 USD | 0.00 USD | 0.00 USD | 4,760.00 USD |
| `7D` | `1.09` | 24,620.00 USD | 0.00 USD | 24,620.00 USD | 0.00 USD | 0.00 USD | 4,760.00 USD |
| `1D` | `1.10` | 19,860.00 USD | 0.00 USD | 19,860.00 USD | 0.00 USD | 0.00 USD | 915.01 USD |
| `7D` | `1.10` | 19,860.00 USD | 0.00 USD | 19,860.00 USD | 0.00 USD | 0.00 USD | 915.01 USD |
| `1D` | `1.10` | 18,940.00 USD | 0.00 USD | 18,940.00 USD | 0.00 USD | 0.00 USD | 1,100.00 USD |
| `7D` | `1.10` | 18,940.00 USD | 0.00 USD | 18,940.00 USD | 0.00 USD | 0.00 USD | 1,100.00 USD |
| `1D` | `1.10` | 17,840.00 USD | 0.00 USD | 17,840.00 USD | 0.00 USD | 0.00 USD | 815.98 USD |
| `7D` | `1.10` | 17,840.00 USD | 0.00 USD | 17,840.00 USD | 0.00 USD | 0.00 USD | 815.98 USD |
| `1D` | `1.11` | 17,030.00 USD | 0.00 USD | 17,030.00 USD | 0.00 USD | 0.00 USD | 6,420.00 USD |
| `7D` | `1.11` | 17,030.00 USD | 0.00 USD | 17,030.00 USD | 0.00 USD | 0.00 USD | 6,420.00 USD |
| `1D` | `1.11` | 10,600.00 USD | 0.00 USD | 10,600.00 USD | 0.00 USD | 0.00 USD | 8,260.00 USD |
| `7D` | `1.11` | 10,600.00 USD | 0.00 USD | 10,600.00 USD | 0.00 USD | 0.00 USD | 8,260.00 USD |
| `1D` | `1.11` | 2,340.00 USD | 0.00 USD | 2,340.00 USD | 0.00 USD | 0.00 USD | 2,340.00 USD |
| `7D` | `1.11` | 2,340.00 USD | 0.00 USD | 2,340.00 USD | 0.00 USD | 0.00 USD | 2,340.00 USD |
| `1D` | `1.12` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.12` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.13` | 4,280.00 USD | 4,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,280.00 USD |
| `7D` | `1.13` | 4,280.00 USD | 4,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,280.00 USD |
| `1D` | `1.13` | 13,840.00 USD | 13,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,560.00 USD |
| `7D` | `1.13` | 13,840.00 USD | 13,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,560.00 USD |
| `1D` | `1.13` | 15,640.00 USD | 15,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,800.00 USD |
| `7D` | `1.13` | 15,640.00 USD | 15,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,800.00 USD |
| `1D` | `1.13` | 17,840.00 USD | 17,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,200.00 USD |
| `7D` | `1.13` | 17,840.00 USD | 17,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,200.00 USD |
| `1D` | `1.14` | 19,980.00 USD | 19,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,140.00 USD |
| `7D` | `1.14` | 19,980.00 USD | 19,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,140.00 USD |
| `1D` | `1.14` | 23,300.00 USD | 23,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,320.00 USD |
| `7D` | `1.14` | 23,300.00 USD | 23,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,320.00 USD |
| `1D` | `1.14` | 25,590.00 USD | 25,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,290.00 USD |
| `7D` | `1.14` | 25,590.00 USD | 25,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,290.00 USD |
| `1D` | `1.14` | 26,760.00 USD | 26,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,170.00 USD |
| `7D` | `1.14` | 26,760.00 USD | 26,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,170.00 USD |
| `1D` | `1.16` | 26,970.00 USD | 26,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 203.99 USD |
| `7D` | `1.16` | 26,970.00 USD | 26,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 203.99 USD |
| `1D` | `1.16` | 27,840.00 USD | 27,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 870.49 USD |
| `7D` | `1.16` | 27,840.00 USD | 27,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 870.49 USD |
| `1D` | `1.16` | 30,220.00 USD | 30,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,390.00 USD |
| `7D` | `1.16` | 30,220.00 USD | 30,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,390.00 USD |
| `1D` | `1.16` | 30,670.00 USD | 30,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 450.41 USD |
| `7D` | `1.16` | 30,670.00 USD | 30,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 450.41 USD |
| `1D` | `1.16` | 31,220.00 USD | 31,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 550.14 USD |
| `7D` | `1.16` | 31,220.00 USD | 31,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 550.14 USD |
| `1D` | `1.23` | 31,300.00 USD | 31,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 81.60 USD |
| `7D` | `1.23` | 31,300.00 USD | 31,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 81.60 USD |
| `1D` | `1.23` | 31,930.00 USD | 31,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 622.95 USD |
| `7D` | `1.23` | 31,930.00 USD | 31,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 622.95 USD |
| `1D` | `1.23` | 32,610.00 USD | 32,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 678.92 USD |
| `7D` | `1.23` | 32,610.00 USD | 32,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 678.92 USD |
| `1D` | `1.23` | 32,780.00 USD | 32,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 177.21 USD |
| `7D` | `1.23` | 32,780.00 USD | 32,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 177.21 USD |
| `1D` | `1.23` | 33,000.00 USD | 33,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 220.05 USD |
| `7D` | `1.23` | 33,000.00 USD | 33,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 220.05 USD |

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
  * `2026-10-29 22:05:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [bea.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1.11` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1.11` (Risk Distance: `0.0013` pts)
  * +2.5R Take Profit: `1.12`
  * Mathematical Lot Sizing: **`0.07 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.12` (Risk Distance: `0.0013` pts)
  * +2.5R Take Profit: `1.11`
  * Mathematical Lot Sizing: **`0.07 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.13`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
