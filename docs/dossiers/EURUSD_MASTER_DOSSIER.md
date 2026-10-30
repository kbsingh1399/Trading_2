# 🏛️ SOVEREIGN CANDIDATE DOSSIER: EURUSD
**Canonical Key**: `EURUSD` | **Broker Instrument**: `EURUSD.pi` | **Asset Class**: `FX Major`
**Timestamp**: `2026-10-30 15:42:19 IST` (`2026-10-30 10:12:19 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Upper +3.00σ Band: `1.13` | Lower -3.00σ Band: `1.11`
  * Upper +2.51σ Band: `1.13` | Lower -2.51σ Band: `1.11`
  * Upper +2.01σ Band: `1.12` | Lower -2.01σ Band: `1.12`
  * Upper +2.00σ Band: `1.12` | Lower -2.00σ Band: `1.12`
  * Upper +1.28σ Band: `1.12` | Lower -1.28σ Band: `1.12`
  * Upper +1.00σ Band: `1.12` | Lower -1.00σ Band: `1.12`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.12` | EMA-20=`1.12` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.12` (Slope: `+0.0000`) | EMA-100=`1.12`
  * Institutional Anchors: EMA-144=`1.12` | EMA-200=`1.12` (Slope: `+0.0000`) | EMA-233=`1.12`
- **Range Boundaries**: 24H High=`1.13` | 24H Low=`1.11` | Weekly High=`1.14` | Weekly Low=`1.10`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.12` (Distance: `+0.01%`)
  * Point of Control (POC) = `1.12` (Distance: `+0.06%`)
  * Value Area Low (VAL) = `1.12` (Distance: `+0.15%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `TREND_UP_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.12` | POC=`1.11` | VAL=`1.11`
  * Prior Day Extremes: PDH=`1.12` | PDL=`1.11` | PDC=`1.12`
  * Monday Range Blueprint: High=`1.12` | Mid=`1.12` | Low=`1.12`
  * Developing Weekly Value Area: Weekly VAH=`1.12` | Weekly POC=`1.11` | Weekly VAL=`1.11`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.12` | Low=`1.12`
  * London Session (08:00-16:00 UTC): High=`1.12` | Low=`1.12`
  * New York Session (13:00-21:00 UTC): High=`1.12` | Low=`1.12`
  * Initial Balance (First Hour): IB High=`1.12` | IB Low=`1.12`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.12` - `1.12`
  * Optimal Trade Entry (OTE 0.705): `1.12`
  * Structural Invalidation Anchor (0.786): `1.13`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `390` | 436.00 USD | -73.84 USD | `-16.94%` | 1,796.49 USD | `-0.31` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `295` | 329.76 USD | -193.98 USD | `-58.82%` | 1,602.51 USD | `-0.89` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.12` | `1.12` | `1.12` | `1.12` | `347` | 387.94 USD | 202.79 USD | `+52.27%` | 1,805.29 USD | `+1.14` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `1,228` | 1,373.19 USD | -1,057.51 USD | `-77.01%` | 8,672.90 USD | `-1.81` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `1,032` | 1,153.76 USD | -111.65 USD | `-9.68%` | 8,561.25 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `1.12` | `1.12` | `1.12` | `1.12` | `1,441` | 1,611.79 USD | 744.58 USD | `+46.20%` | 9,305.83 USD | `+1.50` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `2,559` | 2,862.14 USD | -224.88 USD | `-7.86%` | 5,339.26 USD | `-0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `4,327` | 4,837.50 USD | -2,007.05 USD | `-41.49%` | 3,332.21 USD | `-0.64` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.12` | `1.12` | `1.12` | `1.12` | `5,112` | 5,720.38 USD | 4,735.72 USD | `+82.79%` | 8,067.94 USD | `+1.29` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `6,284` | 7,036.57 USD | 6,332.91 USD | `+90.00%` | 24,991.26 USD | `+0.01` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `15,119` | 16,913.02 USD | -10,827.76 USD | `-64.02%` | 14,163.50 USD | `-0.99` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `18,385` | 20,581.27 USD | 7,828.95 USD | `+38.04%` | 21,992.45 USD | `+0.33` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.11` | `1.12` | `1.11` | `1.12` | `35,597` | 39,738.71 USD | 24,268.79 USD | `+61.07%` | 10,841.45 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `14,336` | 16,024.64 USD | 7,816.90 USD | `+48.78%` | 18,658.34 USD | `+0.10` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `6,284` | 7,036.57 USD | 6,332.91 USD | `+90.00%` | 24,991.26 USD | `+0.01` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `15,119` | 16,913.02 USD | -10,827.76 USD | `-64.02%` | 14,163.50 USD | `-0.99` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.12` | `1.12` | `1.12` | `1.12` | `18,385` | 20,581.27 USD | 7,828.95 USD | `+38.04%` | 21,992.45 USD | `+0.33` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `215` | `0x0911...129a` | `LONG` | 9,970,316.24 USD | `8,898,889.90` | `1.15` | `1.12` | `1.06` | -252,426.18 USD | `-2.53%` | `20X Isolated` |
| `1115` | `0xe03b...ed11` | `SHORT` | 1,951,577.82 USD | `1,741,858.10` | `1.14` | `1.12` | `1.20` | 41,625.50 USD | `+2.13%` | `50X Isolated` |
| `1735` | `0x3f31...a3d7` | `SHORT` | 1,206,124.16 USD | `1,076,512.10` | `1.11` | `1.12` | `1.13` | -6,192.71 USD | `-0.51%` | `50X Isolated` |
| `1836` | `0x9df2...c665` | `SHORT` | 1,120,329.53 USD | `999,937.10` | `1.12` | `1.12` | `1.46` | 240.31 USD | `+0.02%` | `5X Isolated` |
| `1986` | `0x5e91...76ca` | `SHORT` | 1,004,998.80 USD | `897,000.00` | `1.11` | `1.12` | `1.16` | -5,326.99 USD | `-0.53%` | `20X Isolated` |

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
| `7D` | `1.01` | 112,070.00 USD | 0.00 USD | 112,070.00 USD | 0.00 USD | 0.00 USD | 560.68 USD |
| `7D` | `1.01` | 111,510.00 USD | 0.00 USD | 111,510.00 USD | 0.00 USD | 0.00 USD | 1,360.00 USD |
| `1D` | `1.01` | 62,450.00 USD | 0.00 USD | 62,450.00 USD | 0.00 USD | 0.00 USD | 734.84 USD |
| `7D` | `1.01` | 110,140.00 USD | 0.00 USD | 110,140.00 USD | 0.00 USD | 0.00 USD | 964.38 USD |
| `1D` | `1.01` | 61,710.00 USD | 0.00 USD | 61,710.00 USD | 0.00 USD | 0.00 USD | 151.30 USD |
| `7D` | `1.01` | 109,180.00 USD | 0.00 USD | 109,180.00 USD | 0.00 USD | 0.00 USD | 163.80 USD |
| `1D` | `1.01` | 61,560.00 USD | 0.00 USD | 61,560.00 USD | 0.00 USD | 0.00 USD | 49.14 USD |
| `7D` | `1.01` | 109,010.00 USD | 0.00 USD | 109,010.00 USD | 0.00 USD | 0.00 USD | 130.96 USD |
| `7D` | `1.07` | 108,880.00 USD | 0.00 USD | 108,880.00 USD | 0.00 USD | 0.00 USD | 460.25 USD |
| `7D` | `1.07` | 108,420.00 USD | 0.00 USD | 108,420.00 USD | 0.00 USD | 0.00 USD | 2,100.00 USD |
| `1D` | `1.07` | 61,510.00 USD | 0.00 USD | 61,510.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `1.07` | 106,320.00 USD | 0.00 USD | 106,320.00 USD | 0.00 USD | 0.00 USD | 3,180.00 USD |
| `1D` | `1.07` | 60,050.00 USD | 0.00 USD | 60,050.00 USD | 0.00 USD | 0.00 USD | 1,640.00 USD |
| `7D` | `1.07` | 103,150.00 USD | 0.00 USD | 103,150.00 USD | 0.00 USD | 0.00 USD | 2,040.00 USD |
| `1D` | `1.07` | 58,410.00 USD | 0.00 USD | 58,410.00 USD | 0.00 USD | 0.00 USD | 21.51 USD |
| `7D` | `1.07` | 101,110.00 USD | 0.00 USD | 101,110.00 USD | 0.00 USD | 0.00 USD | 1,230.00 USD |
| `1D` | `1.08` | 58,390.00 USD | 0.00 USD | 58,390.00 USD | 0.00 USD | 0.00 USD | 3,300.00 USD |
| `7D` | `1.08` | 99,880.00 USD | 0.00 USD | 99,880.00 USD | 0.00 USD | 0.00 USD | 3,430.00 USD |
| `1D` | `1.08` | 55,090.00 USD | 0.00 USD | 55,090.00 USD | 0.00 USD | 0.00 USD | 1,860.00 USD |
| `7D` | `1.08` | 96,460.00 USD | 0.00 USD | 96,460.00 USD | 0.00 USD | 0.00 USD | 2,450.00 USD |
| `1D` | `1.08` | 53,230.00 USD | 0.00 USD | 53,230.00 USD | 0.00 USD | 0.00 USD | 371.68 USD |
| `7D` | `1.08` | 94,000.00 USD | 0.00 USD | 94,000.00 USD | 0.00 USD | 0.00 USD | 533.13 USD |
| `1D` | `1.08` | 52,860.00 USD | 0.00 USD | 52,860.00 USD | 0.00 USD | 0.00 USD | 134.03 USD |
| `7D` | `1.08` | 93,470.00 USD | 0.00 USD | 93,470.00 USD | 0.00 USD | 0.00 USD | 327.41 USD |
| `7D` | `1.09` | 93,140.00 USD | 0.00 USD | 93,140.00 USD | 0.00 USD | 0.00 USD | 4,580.00 USD |
| `1D` | `1.09` | 52,720.00 USD | 0.00 USD | 52,720.00 USD | 0.00 USD | 0.00 USD | 1,550.00 USD |
| `7D` | `1.09` | 88,560.00 USD | 0.00 USD | 88,560.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD |
| `1D` | `1.09` | 51,170.00 USD | 0.00 USD | 51,170.00 USD | 0.00 USD | 0.00 USD | 3,210.00 USD |
| `7D` | `1.10` | 85,770.00 USD | 0.00 USD | 85,770.00 USD | 0.00 USD | 0.00 USD | 6,350.00 USD |
| `1D` | `1.10` | 47,960.00 USD | 0.00 USD | 47,960.00 USD | 0.00 USD | 0.00 USD | 1,440.00 USD |
| `7D` | `1.10` | 79,420.00 USD | 0.00 USD | 79,420.00 USD | 0.00 USD | 0.00 USD | 4,280.00 USD |
| `1D` | `1.10` | 46,520.00 USD | 0.00 USD | 46,520.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD |
| `1D` | `1.10` | 45,430.00 USD | 0.00 USD | 45,430.00 USD | 0.00 USD | 0.00 USD | 5,630.00 USD |
| `7D` | `1.10` | 75,140.00 USD | 0.00 USD | 75,140.00 USD | 0.00 USD | 0.00 USD | 9,400.00 USD |
| `1D` | `1.10` | 39,800.00 USD | 0.00 USD | 39,800.00 USD | 0.00 USD | 0.00 USD | 3,820.00 USD |
| `7D` | `1.10` | 65,740.00 USD | 0.00 USD | 65,740.00 USD | 0.00 USD | 0.00 USD | 3,090.00 USD |
| `1D` | `1.10` | 35,980.00 USD | 0.00 USD | 35,980.00 USD | 0.00 USD | 0.00 USD | 694.16 USD |
| `7D` | `1.10` | 62,650.00 USD | 0.00 USD | 62,650.00 USD | 0.00 USD | 0.00 USD | 340.94 USD |
| `1D` | `1.10` | 35,290.00 USD | 0.00 USD | 35,290.00 USD | 0.00 USD | 0.00 USD | 137.39 USD |
| `7D` | `1.10` | 62,310.00 USD | 0.00 USD | 62,310.00 USD | 0.00 USD | 0.00 USD | 654.82 USD |
| `7D` | `1.10` | 61,660.00 USD | 0.00 USD | 61,660.00 USD | 0.00 USD | 0.00 USD | 3,330.00 USD |
| `7D` | `1.10` | 58,330.00 USD | 0.00 USD | 58,330.00 USD | 0.00 USD | 0.00 USD | 11,270.00 USD |
| `1D` | `1.11` | 35,150.00 USD | 0.00 USD | 35,150.00 USD | 0.00 USD | 0.00 USD | 5,830.00 USD |
| `7D` | `1.11` | 47,060.00 USD | 0.00 USD | 47,060.00 USD | 0.00 USD | 0.00 USD | 9,710.00 USD |
| `1D` | `1.11` | 29,310.00 USD | 0.00 USD | 29,310.00 USD | 0.00 USD | 0.00 USD | 6,560.00 USD |
| `7D` | `1.11` | 37,350.00 USD | 0.00 USD | 37,350.00 USD | 0.00 USD | 0.00 USD | 6,790.00 USD |
| `1D` | `1.11` | 22,760.00 USD | 0.00 USD | 22,760.00 USD | 0.00 USD | 0.00 USD | 86.06 USD |
| `7D` | `1.11` | 30,560.00 USD | 0.00 USD | 30,560.00 USD | 0.00 USD | 0.00 USD | 4,910.00 USD |
| `1D` | `1.11` | 22,670.00 USD | 0.00 USD | 22,670.00 USD | 0.00 USD | 0.00 USD | 13,190.00 USD |
| `7D` | `1.11` | 25,650.00 USD | 0.00 USD | 25,650.00 USD | 0.00 USD | 0.00 USD | 13,700.00 USD |
| `1D` | `1.11` | 9,480.00 USD | 0.00 USD | 9,480.00 USD | 0.00 USD | 0.00 USD | 7,400.00 USD |
| `7D` | `1.11` | 11,950.00 USD | 0.00 USD | 11,950.00 USD | 0.00 USD | 0.00 USD | 9,820.00 USD |
| `1D` | `1.11` | 2,080.00 USD | 0.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD | 1,390.00 USD |
| `7D` | `1.11` | 2,130.00 USD | 0.00 USD | 2,130.00 USD | 0.00 USD | 0.00 USD | 2,130.00 USD |
| `1D` | `1.11` | 691.45 USD | 0.00 USD | 691.45 USD | 0.00 USD | 0.00 USD | 691.45 USD |
| `1D` | `1.12` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.12` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.13` | 10,080.00 USD | 10,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,080.00 USD |
| `1D` | `1.13` | 3,100.00 USD | 3,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,100.00 USD |
| `7D` | `1.13` | 14,740.00 USD | 14,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,670.00 USD |
| `1D` | `1.13` | 12,310.00 USD | 12,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,210.00 USD |
| `7D` | `1.13` | 27,440.00 USD | 27,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,690.00 USD |
| `1D` | `1.13` | 12,410.00 USD | 12,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 98.72 USD |
| `7D` | `1.13` | 36,000.00 USD | 36,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,570.00 USD |
| `1D` | `1.13` | 14,580.00 USD | 14,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,170.00 USD |
| `1D` | `1.13` | 25,840.00 USD | 25,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,270.00 USD |
| `7D` | `1.13` | 54,800.00 USD | 54,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,800.00 USD |
| `1D` | `1.13` | 33,490.00 USD | 33,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,640.00 USD |
| `7D` | `1.13` | 60,980.00 USD | 60,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,170.00 USD |
| `1D` | `1.13` | 34,660.00 USD | 34,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,170.00 USD |
| `7D` | `1.13` | 61,660.00 USD | 61,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 681.89 USD |
| `1D` | `1.14` | 35,150.00 USD | 35,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 491.52 USD |
| `7D` | `1.14` | 62,970.00 USD | 62,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD |
| `7D` | `1.14` | 66,550.00 USD | 66,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,580.00 USD |
| `7D` | `1.14` | 70,340.00 USD | 70,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,790.00 USD |
| `1D` | `1.14` | 38,070.00 USD | 38,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,920.00 USD |
| `7D` | `1.14` | 75,120.00 USD | 75,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,780.00 USD |
| `1D` | `1.14` | 41,350.00 USD | 41,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,280.00 USD |
| `7D` | `1.14` | 78,520.00 USD | 78,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,400.00 USD |
| `1D` | `1.14` | 41,390.00 USD | 41,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43.03 USD |
| `7D` | `1.14` | 80,970.00 USD | 80,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,450.00 USD |
| `1D` | `1.14` | 47,990.00 USD | 47,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `1.14` | 87,820.00 USD | 87,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,850.00 USD |
| `1D` | `1.14` | 51,680.00 USD | 51,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,700.00 USD |
| `7D` | `1.14` | 92,730.00 USD | 92,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,910.00 USD |
| `1D` | `1.14` | 52,380.00 USD | 52,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 693.14 USD |
| `7D` | `1.15` | 93,800.00 USD | 93,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,070.00 USD |
| `1D` | `1.15` | 52,720.00 USD | 52,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 345.73 USD |
| `7D` | `1.15` | 94,450.00 USD | 94,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 654.82 USD |
| `7D` | `1.16` | 96,970.00 USD | 96,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,520.00 USD |
| `1D` | `1.16` | 53,500.00 USD | 53,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 776.05 USD |
| `7D` | `1.16` | 98,140.00 USD | 98,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,170.00 USD |
| `1D` | `1.16` | 55,810.00 USD | 55,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,310.00 USD |
| `7D` | `1.16` | 101,360.00 USD | 101,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,230.00 USD |
| `1D` | `1.16` | 55,830.00 USD | 55,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18.27 USD |
| `7D` | `1.16` | 103,450.00 USD | 103,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,090.00 USD |
| `1D` | `1.16` | 56,370.00 USD | 56,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 542.23 USD |
| `1D` | `1.17` | 59,180.00 USD | 59,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,820.00 USD |
| `7D` | `1.17` | 108,150.00 USD | 108,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,700.00 USD |
| `1D` | `1.17` | 61,080.00 USD | 61,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,900.00 USD |
| `7D` | `1.17` | 109,450.00 USD | 109,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,300.00 USD |
| `1D` | `1.17` | 61,390.00 USD | 61,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 305.16 USD |
| `7D` | `1.17` | 109,860.00 USD | 109,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 409.49 USD |
| `1D` | `1.17` | 61,510.00 USD | 61,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 122.88 USD |
| `7D` | `1.17` | 110,190.00 USD | 110,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 327.41 USD |
| `7D` | `1.23` | 110,270.00 USD | 110,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 81.33 USD |
| `7D` | `1.23` | 111,210.00 USD | 111,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 941.96 USD |
| `1D` | `1.23` | 61,820.00 USD | 61,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 310.42 USD |
| `7D` | `1.23` | 112,010.00 USD | 112,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 792.91 USD |
| `1D` | `1.23` | 62,750.00 USD | 62,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 923.99 USD |
| `7D` | `1.23` | 112,950.00 USD | 112,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 943.29 USD |
| `1D` | `1.23` | 62,750.00 USD | 62,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4.47 USD |
| `7D` | `1.23` | 113,790.00 USD | 113,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 835.18 USD |
| `1D` | `1.23` | 62,970.00 USD | 62,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 216.89 USD |
| `1D` | `1.23` | 64,090.00 USD | 64,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD |
| `7D` | `1.23` | 115,510.00 USD | 115,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,720.00 USD |
| `1D` | `1.23` | 64,830.00 USD | 64,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 739.56 USD |
| `7D` | `1.23` | 116,110.00 USD | 116,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 606.94 USD |
| `1D` | `1.23` | 64,950.00 USD | 64,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 124.88 USD |
| `1D` | `1.23` | 64,960.00 USD | 64,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4.46 USD |
| `7D` | `1.24` | 116,280.00 USD | 116,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 163.80 USD |
| `7D` | `1.24` | 116,410.00 USD | 116,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 130.96 USD |

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
  * Current Rate: `724.78` | Last 24h: `658.59` | Last 3d: `761.48` | Last 7d: `828.22`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0854%` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0000%` | **USDT Bitget** | `-0.0654%` |
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
  * `2026-10-30 15:33:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:19:00 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:00 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:00 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:00 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.12` (Risk Distance: `0.0034` pts)
  * +2.5R Take Profit: `1.13`
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
