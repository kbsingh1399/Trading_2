# 🏛️ SOVEREIGN CANDIDATE DOSSIER: EURUSD
**Canonical Key**: `EURUSD` | **Broker Instrument**: `EURUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 01:08:43 IST` (`2026-10-29 19:38:43 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `1.12` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0028` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
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
  * Institutional Anchors: EMA-144=`1.12` | EMA-200=`1.12` (Slope: `+0.0000`) | EMA-233=`1.12`
- **Range Boundaries**: 24H High=`1.13` | 24H Low=`1.11` | Weekly High=`1.14` | Weekly Low=`1.09`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.12` (Distance: `+0.09%`)
  * Point of Control (POC) = `1.11` (Distance: `+0.27%`)
  * Value Area Low (VAL) = `1.11` (Distance: `+0.38%`)
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
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `368` | 410.87 USD | 280.14 USD | `+68.18%` | 3,202.90 USD | `+0.54` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `432` | 482.18 USD | -406.05 USD | `-84.21%` | 2,796.86 USD | `-0.83` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `524` | 584.84 USD | -264.12 USD | `-45.16%` | 2,532.73 USD | `-0.45` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `1,379` | 1,540.19 USD | 1,083.59 USD | `+70.35%` | 8,215.05 USD | `+0.66` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `1,188` | 1,326.00 USD | -1,164.10 USD | `-87.79%` | 7,050.95 USD | `-0.99` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `1,400` | 1,562.78 USD | 609.48 USD | `+39.00%` | 7,660.43 USD | `+0.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.11` | `1.12` | `1.11` | `1.12` | `9,481` | 10,581.65 USD | 6,918.77 USD | `+65.38%` | 9,276.37 USD | `+1.94` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `8,551` | 9,546.08 USD | 136.37 USD | `+1.43%` | 9,412.75 USD | `+0.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `4,883` | 5,451.14 USD | -163.07 USD | `-2.99%` | 9,249.68 USD | `-0.14` | **`BEARISH`** | `BEARISH ABSORPTION` |
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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:03:14 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `234` | `0x0911...129a` | `LONG` | 9,940,060.02 USD | `8,898,889.90` | `1.15` | `1.12` | `1.06` | -282,682.40 USD | `-2.84%` | `20X Isolated` |
| `1183` | `0xe03b...ed11` | `SHORT` | 1,945,655.50 USD | `1,741,858.10` | `1.14` | `1.12` | `1.20` | 47,547.82 USD | `+2.44%` | `50X Isolated` |
| `1781` | `0x3f31...a3d7` | `SHORT` | 1,202,464.02 USD | `1,076,512.10` | `1.11` | `1.12` | `1.13` | -2,532.57 USD | `-0.21%` | `50X Isolated` |
| `1873` | `0x9df2...c665` | `SHORT` | 1,116,929.74 USD | `999,937.10` | `1.12` | `1.12` | `1.46` | 3,640.10 USD | `+0.33%` | `5X Isolated` |

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
| `7D` | `1.00` | 108,130.00 USD | 0.00 USD | 108,130.00 USD | 0.00 USD | 0.00 USD | 725.98 USD |
| `7D` | `1.00` | 107,410.00 USD | 0.00 USD | 107,410.00 USD | 0.00 USD | 0.00 USD | 1,510.00 USD |
| `7D` | `1.01` | 105,900.00 USD | 0.00 USD | 105,900.00 USD | 0.00 USD | 0.00 USD | 391.35 USD |
| `7D` | `1.01` | 105,510.00 USD | 0.00 USD | 105,510.00 USD | 0.00 USD | 0.00 USD | 965.98 USD |
| `1D` | `1.01` | 29,480.00 USD | 0.00 USD | 29,480.00 USD | 0.00 USD | 0.00 USD | 241.87 USD |
| `7D` | `1.01` | 104,540.00 USD | 0.00 USD | 104,540.00 USD | 0.00 USD | 0.00 USD | 104.19 USD |
| `7D` | `1.01` | 104,440.00 USD | 0.00 USD | 104,440.00 USD | 0.00 USD | 0.00 USD | 688.48 USD |
| `7D` | `1.01` | 103,750.00 USD | 0.00 USD | 103,750.00 USD | 0.00 USD | 0.00 USD | 885.21 USD |
| `7D` | `1.01` | 102,860.00 USD | 0.00 USD | 102,860.00 USD | 0.00 USD | 0.00 USD | 355.65 USD |
| `7D` | `1.07` | 102,510.00 USD | 0.00 USD | 102,510.00 USD | 0.00 USD | 0.00 USD | 392.99 USD |
| `7D` | `1.07` | 102,110.00 USD | 0.00 USD | 102,110.00 USD | 0.00 USD | 0.00 USD | 1,530.00 USD |
| `7D` | `1.07` | 100,590.00 USD | 0.00 USD | 100,590.00 USD | 0.00 USD | 0.00 USD | 3,710.00 USD |
| `1D` | `1.07` | 29,240.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD | 0.00 USD | 2,430.00 USD |
| `7D` | `1.07` | 96,870.00 USD | 0.00 USD | 96,870.00 USD | 0.00 USD | 0.00 USD | 1,290.00 USD |
| `1D` | `1.07` | 26,810.00 USD | 0.00 USD | 26,810.00 USD | 0.00 USD | 0.00 USD | 1,150.00 USD |
| `7D` | `1.07` | 95,580.00 USD | 0.00 USD | 95,580.00 USD | 0.00 USD | 0.00 USD | 2,070.00 USD |
| `1D` | `1.07` | 25,660.00 USD | 0.00 USD | 25,660.00 USD | 0.00 USD | 0.00 USD | 597.58 USD |
| `7D` | `1.08` | 93,510.00 USD | 0.00 USD | 93,510.00 USD | 0.00 USD | 0.00 USD | 260.49 USD |
| `7D` | `1.08` | 93,250.00 USD | 0.00 USD | 93,250.00 USD | 0.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `1.08` | 91,430.00 USD | 0.00 USD | 91,430.00 USD | 0.00 USD | 0.00 USD | 2,540.00 USD |
| `7D` | `1.08` | 88,890.00 USD | 0.00 USD | 88,890.00 USD | 0.00 USD | 0.00 USD | 1,020.00 USD |
| `7D` | `1.09` | 87,860.00 USD | 0.00 USD | 87,860.00 USD | 0.00 USD | 0.00 USD | 785.98 USD |
| `7D` | `1.09` | 87,080.00 USD | 0.00 USD | 87,080.00 USD | 0.00 USD | 0.00 USD | 6,580.00 USD |
| `1D` | `1.09` | 25,070.00 USD | 0.00 USD | 25,070.00 USD | 0.00 USD | 0.00 USD | 1,560.00 USD |
| `7D` | `1.09` | 80,500.00 USD | 0.00 USD | 80,500.00 USD | 0.00 USD | 0.00 USD | 4,790.00 USD |
| `1D` | `1.09` | 23,510.00 USD | 0.00 USD | 23,510.00 USD | 0.00 USD | 0.00 USD | 4,770.00 USD |
| `7D` | `1.10` | 75,710.00 USD | 0.00 USD | 75,710.00 USD | 0.00 USD | 0.00 USD | 3,370.00 USD |
| `1D` | `1.10` | 18,740.00 USD | 0.00 USD | 18,740.00 USD | 0.00 USD | 0.00 USD | 908.35 USD |
| `7D` | `1.10` | 72,340.00 USD | 0.00 USD | 72,340.00 USD | 0.00 USD | 0.00 USD | 2,480.00 USD |
| `1D` | `1.10` | 17,830.00 USD | 0.00 USD | 17,830.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD |
| `7D` | `1.10` | 69,870.00 USD | 0.00 USD | 69,870.00 USD | 0.00 USD | 0.00 USD | 730.14 USD |
| `7D` | `1.10` | 69,140.00 USD | 0.00 USD | 69,140.00 USD | 0.00 USD | 0.00 USD | 6,150.00 USD |
| `7D` | `1.10` | 62,990.00 USD | 0.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD | 2,880.00 USD |
| `7D` | `1.10` | 60,110.00 USD | 0.00 USD | 60,110.00 USD | 0.00 USD | 0.00 USD | 1,530.00 USD |
| `7D` | `1.10` | 58,570.00 USD | 0.00 USD | 58,570.00 USD | 0.00 USD | 0.00 USD | 1,570.00 USD |
| `7D` | `1.10` | 57,000.00 USD | 0.00 USD | 57,000.00 USD | 0.00 USD | 0.00 USD | 12,700.00 USD |
| `1D` | `1.10` | 16,710.00 USD | 0.00 USD | 16,710.00 USD | 0.00 USD | 0.00 USD | 3,100.00 USD |
| `7D` | `1.11` | 44,300.00 USD | 0.00 USD | 44,300.00 USD | 0.00 USD | 0.00 USD | 8,260.00 USD |
| `1D` | `1.11` | 13,610.00 USD | 0.00 USD | 13,610.00 USD | 0.00 USD | 0.00 USD | 9,500.00 USD |
| `7D` | `1.11` | 36,040.00 USD | 0.00 USD | 36,040.00 USD | 0.00 USD | 0.00 USD | 5,170.00 USD |
| `1D` | `1.11` | 4,110.00 USD | 0.00 USD | 4,110.00 USD | 0.00 USD | 0.00 USD | 1,870.00 USD |
| `7D` | `1.11` | 30,870.00 USD | 0.00 USD | 30,870.00 USD | 0.00 USD | 0.00 USD | 8,290.00 USD |
| `1D` | `1.11` | 2,240.00 USD | 0.00 USD | 2,240.00 USD | 0.00 USD | 0.00 USD | 2,240.00 USD |
| `7D` | `1.11` | 22,590.00 USD | 0.00 USD | 22,590.00 USD | 0.00 USD | 0.00 USD | 1,040.00 USD |
| `7D` | `1.11` | 21,540.00 USD | 0.00 USD | 21,540.00 USD | 0.00 USD | 0.00 USD | 7,280.00 USD |
| `7D` | `1.11` | 14,270.00 USD | 0.00 USD | 14,270.00 USD | 0.00 USD | 0.00 USD | 9,650.00 USD |
| `7D` | `1.11` | 4,620.00 USD | 0.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD | 3,950.00 USD |
| `7D` | `1.11` | 670.27 USD | 0.00 USD | 670.27 USD | 0.00 USD | 0.00 USD | 670.27 USD |
| `1D` | `1.12` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.12` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.13` | 5,550.00 USD | 5,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,550.00 USD |
| `7D` | `1.13` | 14,730.00 USD | 14,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,170.00 USD |
| `1D` | `1.13` | 3,120.00 USD | 3,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,120.00 USD |
| `7D` | `1.13` | 24,620.00 USD | 24,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,890.00 USD |
| `1D` | `1.13` | 12,690.00 USD | 12,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,570.00 USD |
| `7D` | `1.13` | 31,040.00 USD | 31,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,420.00 USD |
| `1D` | `1.13` | 14,480.00 USD | 14,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,790.00 USD |
| `7D` | `1.13` | 35,990.00 USD | 35,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,950.00 USD |
| `1D` | `1.13` | 16,710.00 USD | 16,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,230.00 USD |
| `7D` | `1.13` | 37,450.00 USD | 37,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `1.13` | 49,750.00 USD | 49,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,300.00 USD |
| `7D` | `1.13` | 54,550.00 USD | 54,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,800.00 USD |
| `7D` | `1.14` | 58,570.00 USD | 58,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,030.00 USD |
| `7D` | `1.14` | 59,360.00 USD | 59,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 785.98 USD |
| `7D` | `1.14` | 65,940.00 USD | 65,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,580.00 USD |
| `1D` | `1.14` | 18,260.00 USD | 18,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,550.00 USD |
| `7D` | `1.14` | 69,840.00 USD | 69,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,900.00 USD |
| `1D` | `1.14` | 23,030.00 USD | 23,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,760.00 USD |
| `7D` | `1.14` | 72,430.00 USD | 72,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,580.00 USD |
| `1D` | `1.14` | 23,950.00 USD | 23,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 921.90 USD |
| `7D` | `1.14` | 76,570.00 USD | 76,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,140.00 USD |
| `1D` | `1.14` | 25,070.00 USD | 25,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD |
| `7D` | `1.14` | 77,090.00 USD | 77,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 520.97 USD |
| `7D` | `1.14` | 80,730.00 USD | 80,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,640.00 USD |
| `7D` | `1.14` | 85,550.00 USD | 85,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,820.00 USD |
| `7D` | `1.15` | 87,530.00 USD | 87,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,980.00 USD |
| `7D` | `1.15` | 87,860.00 USD | 87,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 335.14 USD |
| `7D` | `1.16` | 88,260.00 USD | 88,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 392.99 USD |
| `7D` | `1.16` | 89,250.00 USD | 89,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 995.54 USD |
| `7D` | `1.16` | 91,580.00 USD | 91,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,330.00 USD |
| `1D` | `1.16` | 26,540.00 USD | 26,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,470.00 USD |
| `7D` | `1.16` | 94,020.00 USD | 94,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,440.00 USD |
| `1D` | `1.16` | 28,240.00 USD | 28,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,700.00 USD |
| `7D` | `1.16` | 95,620.00 USD | 95,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,610.00 USD |
| `1D` | `1.16` | 28,680.00 USD | 28,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 446.77 USD |
| `7D` | `1.16` | 96,860.00 USD | 96,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240.00 USD |
| `1D` | `1.16` | 29,240.00 USD | 29,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 558.58 USD |
| `7D` | `1.17` | 97,220.00 USD | 97,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 365.08 USD |
| `7D` | `1.17` | 100,300.00 USD | 100,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,070.00 USD |
| `7D` | `1.17` | 101,500.00 USD | 101,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,200.00 USD |
| `7D` | `1.17` | 102,510.00 USD | 102,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,010.00 USD |
| `7D` | `1.23` | 102,660.00 USD | 102,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 157.20 USD |
| `7D` | `1.23` | 103,230.00 USD | 103,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 568.78 USD |
| `7D` | `1.23` | 104,740.00 USD | 104,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `1.23` | 29,830.00 USD | 29,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 588.94 USD |
| `7D` | `1.23` | 104,960.00 USD | 104,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 220.18 USD |
| `1D` | `1.23` | 30,520.00 USD | 30,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 686.49 USD |
| `7D` | `1.23` | 105,600.00 USD | 105,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 642.04 USD |
| `1D` | `1.23` | 30,690.00 USD | 30,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 168.79 USD |
| `7D` | `1.23` | 106,100.00 USD | 106,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 495.11 USD |
| `1D` | `1.23` | 30,910.00 USD | 30,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 223.43 USD |
| `7D` | `1.23` | 106,240.00 USD | 106,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 140.19 USD |
| `7D` | `1.23` | 106,490.00 USD | 106,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 251.46 USD |

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
  * `2026-10-30 00:57:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:47:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:16:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:59:49 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:59:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.11` (Risk Distance: `0.0034` pts)
  * +2.5R Take Profit: `1.12`
  * Mathematical Lot Sizing: **`0.02 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.12` (Risk Distance: `0.0034` pts)
  * +2.5R Take Profit: `1.11`
  * Mathematical Lot Sizing: **`0.02 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.13`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
