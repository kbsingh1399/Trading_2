# 🏛️ SOVEREIGN CANDIDATE DOSSIER: APT
**Canonical Key**: `APT` | **Broker Instrument**: `APTUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 02:33:42 IST` (`2026-10-29 21:03:42 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.6900` | **Live Ask Quote**: `0.6901` | **Mid Price**: `0.6901`
- **Spread Points**: `0.000138` | **Spread BPS**: `2.00 bps` (Charter Threshold: `12.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE_MAKER_LIMIT_ONLY` | **Order Type Allowed**: `LIMIT_ONLY`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `4` | Point: `0.0001`
  * Point Value (1.0 Lot): `0.00 USD` | Point Value (0.01 Lot): `0.0000 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `0.6901` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.6949` | Lower -3.00σ Band: `0.6852`
  * Upper +2.51σ Band: `0.6939` | Lower -2.51σ Band: `0.6863`
  * Upper +2.01σ Band: `0.6930` | Lower -2.01σ Band: `0.6872`
  * Upper +2.00σ Band: `0.6928` | Lower -2.00σ Band: `0.6873`
  * Upper +1.28σ Band: `0.6920` | Lower -1.28σ Band: `0.6881`
  * Upper +1.00σ Band: `0.6914` | Lower -1.00σ Band: `0.6887`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.6901` | EMA-20=`0.6901` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.6901` (Slope: `+0.0000`) | EMA-100=`0.6901`
  * Institutional Anchors: EMA-144=`0.6901` | EMA-200=`0.6901` (Slope: `+0.0000`) | EMA-233=`0.6901`
- **Range Boundaries**: 24H High=`0.6970` | 24H Low=`0.6832` | Weekly High=`0.7039` | Weekly Low=`0.6763`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.6921` (Distance: `+0.00%`)
  * Point of Control (POC) = `0.6901` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `0.6880` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.6928` | POC=`0.6901` | VAL=`0.6873`
  * Prior Day Extremes: PDH=`0.6942` | PDL=`0.6859` | PDC=`0.6901`
  * Monday Range Blueprint: High=`0.6935` | Mid=`0.6901` | Low=`0.6866`
  * Developing Weekly Value Area: Weekly VAH=`0.6956` | Weekly POC=`0.6901` | Weekly VAL=`0.6845`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.6914` | Low=`0.6887`
  * London Session (08:00-16:00 UTC): High=`0.6928` | Low=`0.6873`
  * New York Session (13:00-21:00 UTC): High=`0.6942` | Low=`0.6859`
  * Initial Balance (First Hour): IB High=`0.6921` | IB Low=`0.6880`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.6873` - `0.6928`
  * Optimal Trade Entry (OTE 0.705): `0.6914`
  * Structural Invalidation Anchor (0.786): `0.6956`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.6217` | `0.6249` | `0.6003` | `0.6175` | `6,000,751` | 3,682,480.56 USD | -191,977.80 USD | `-5.21%` | -6,606,391.39 USD | `-0.08` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.6174` | `0.6291` | `0.6174` | `0.6217` | `2,141,340` | 1,336,761.70 USD | -73,425.44 USD | `-5.49%` | -6,679,816.83 USD | `+0.18` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.6217` | `0.6233` | `0.6212` | `0.6231` | `168,694` | 104,987.92 USD | -9,701.06 USD | `-9.24%` | -6,689,517.89 USD | `+0.31` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.6633` | `0.6663` | `0.6600` | `0.6617` | `1,568,931` | 1,040,684.48 USD | 66,061.07 USD | `+6.35%` | -3,883,650.51 USD | `+0.84` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.6617` | `0.6640` | `0.6134` | `0.6218` | `15,937,422` | 10,130,057.36 USD | -2,530,763.08 USD | `-24.98%` | -6,414,413.59 USD | `-4.13` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.6217` | `0.6291` | `0.6003` | `0.6227` | `8,293,922` | 5,113,729.11 USD | -277,431.18 USD | `-5.43%` | -6,691,844.76 USD | `-0.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.6796` | `0.6804` | `0.6673` | `0.6699` | `4,032,719` | 2,714,496.22 USD | -416,792.27 USD | `-15.35%` | -3,627,547.27 USD | `-0.90` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.6700` | `0.6740` | `0.6665` | `0.6721` | `2,120,904` | 1,422,528.11 USD | 209,427.40 USD | `+14.72%` | -3,418,119.86 USD | `+1.29` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.6721` | `0.6728` | `0.6003` | `0.6223` | `30,511,998` | 19,398,260.33 USD | -3,275,731.71 USD | `-16.89%` | -6,693,851.57 USD | `-4.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -1,678,888.13 USD | `+0.66` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -3,147,816.26 USD | `-1.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6003` | `0.6231` | `30,524,433` | 19,406,004.58 USD | -3,271,398.03 USD | `-16.86%` | -6,419,214.29 USD | `-1.99` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.6611` | `0.6759` | `0.6485` | `0.6561` | `10,656,422` | 7,044,804.33 USD | -366,898.68 USD | `-5.21%` | -1,470,659.97 USD | `+1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6561` | `0.6774` | `0.6549` | `0.6712` | `7,448,343` | 4,965,296.85 USD | -60,141.40 USD | `-1.21%` | -1,530,801.38 USD | `+1.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -1,678,888.13 USD | `+0.66` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -3,147,816.26 USD | `-1.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6003` | `0.6231` | `30,524,433` | 19,406,004.58 USD | -3,271,398.03 USD | `-16.86%` | -6,419,214.29 USD | `-1.99` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:26:17 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.7002` | 8,527.41 USD | `-` | `NEWS_INTEL` | `-` | #APT Whale BUY: 8.53K USD at 0.7002 USD [API] | `2026-10-28 01:55:53` |
| `ANNOUNCEMENT` | `INFO` | `0.7021` | 10,246.45 USD | `-` | `NEWS_INTEL` | `-` | #APT Whale BUY: 10.25K USD at 0.7021 USD [API] | `2026-10-28 03:31:19` |
| `ANNOUNCEMENT` | `INFO` | `0.7021` | 10,246.45 USD | `-` | `NEWS_INTEL` | `-` | #APT Whale BUY: 10.25K USD at 0.7021 USD [API] | `2026-10-28 03:31:19` |
| `ANNOUNCEMENT` | `INFO` | `0.6953` | 10,147.22 USD | `-` | `NEWS_INTEL` | `-` | #APT Whale SELL: 10.15K USD at 0.6953 USD [API] | `2026-10-28 08:39:58` |
| `ANNOUNCEMENT` | `INFO` | `0.6918` | 5,841.73 USD | `-` | `NEWS_INTEL` | `-` | #APT Whale SELL: 5.84K USD at 0.6918 USD [API] | `2026-10-28 09:11:19` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.7060` (Vol: 90,823.17 USD, Dist: `+2.43%`) | Long MP=`0.6718` (Vol: 39,956.88 USD, Dist: `--2.53%`)
  * 48H Horizon: Short MP=`0.7055` (Vol: 81,903.46 USD, Dist: `+2.36%`) | Long MP=`0.6702` (Vol: 45,046.52 USD, Dist: `--2.77%`)
  * 3D Horizon: Short MP=`0.7210` (Vol: 125,191.03 USD, Dist: `+4.60%`) | Long MP=`0.6703` (Vol: 75,398.81 USD, Dist: `--2.76%`)
  * 7D Horizon: Short MP=`0.8539` (Vol: 187,280.71 USD, Dist: `+24.46%`) | Long MP=`0.6700` (Vol: 92,436.78 USD, Dist: `--2.35%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.1545` | 160.39 USD | 258,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 269.27 USD | 258,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1955` | 2,210.00 USD | 258,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 3,410.00 USD | 256,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3035` | 607.00 USD | 252,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3115` | 467.25 USD | 252,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3175` | 10,620.00 USD | 251,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3305` | 543.58 USD | 241,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3495` | 244.65 USD | 240,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3545` | 177.25 USD | 240,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3565` | 2,140.00 USD | 240,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 189.47 USD | 237,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3675` | 194.23 USD | 237,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3715` | 3,430.00 USD | 237,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3795` | 948.75 USD | 234,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3835` | 721.50 USD | 233,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3845` | 495.42 USD | 232,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3905` | 359.26 USD | 232,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3955` | 2,640.00 USD | 231,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3995` | 271.06 USD | 229,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4005` | 405.48 USD | 228,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 570.81 USD | 228,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4135` | 1,600.00 USD | 227,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 630.86 USD | 226,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4255` | 224.96 USD | 225,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4405` | 4,300.00 USD | 225,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 226.63 USD | 221,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4515` | 27,090.00 USD | 220,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4525` | 147.06 USD | 193,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4605` | 125.38 USD | 193,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4625` | 1,100.00 USD | 193,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4685` | 468.50 USD | 192,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4695` | 5,350.00 USD | 191,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4705` | 425.88 USD | 186,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4715` | 7,780.00 USD | 186,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4755` | 472.63 USD | 178,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4765` | 990.20 USD | 177,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 135.33 USD | 176,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 3,170.00 USD | 176,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 429.90 USD | 173,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 102.82 USD | 173,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5095` | 2,550.00 USD | 173,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 248.05 USD | 170,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5135` | 110.50 USD | 170,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5145` | 288.78 USD | 170,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 9,440.00 USD | 169,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5315` | 11,510.00 USD | 160,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5320` | 710,760.00 USD | 710,760.00 USD | 11,240.00 USD | 0.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5335` | 163.22 USD | 148,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5340` | 696,050.00 USD | 696,050.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5350` | 505,520.00 USD | 505,520.00 USD | 2,650.00 USD | 1,850.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5360` | 693,450.00 USD | 693,450.00 USD | 2,440.00 USD | 3,040.00 USD | 44.79 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5370` | 499,140.00 USD | 499,140.00 USD | 4,720.00 USD | 2,450.00 USD | 1,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5380` | 687,920.00 USD | 687,920.00 USD | 0.00 USD | 1,550.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5385` | 2,690.00 USD | 148,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5390` | 490,110.00 USD | 490,110.00 USD | 6,850.00 USD | 1,140.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5400` | 683,460.00 USD | 683,460.00 USD | 0.00 USD | 0.00 USD | 80.65 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5410` | 476,640.00 USD | 476,640.00 USD | 618.50 USD | 0.00 USD | 2,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5420` | 683,380.00 USD | 683,380.00 USD | 7,660.00 USD | 1,290.00 USD | 2,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5430` | 474,030.00 USD | 474,030.00 USD | 3,300.00 USD | 0.00 USD | 3,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5440` | 671,580.00 USD | 671,580.00 USD | 0.00 USD | 1,150.00 USD | 6,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5445` | 330.14 USD | 145,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5450` | 467,300.00 USD | 467,300.00 USD | 1,070.00 USD | 298.25 USD | 1,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5460` | 663,460.00 USD | 663,460.00 USD | 2,250.00 USD | 3,030.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5470` | 464,900.00 USD | 464,900.00 USD | 3,980.00 USD | 633.67 USD | 499.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5480` | 652,990.00 USD | 652,990.00 USD | 2,000.00 USD | 795.70 USD | 4,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5490` | 459,790.00 USD | 459,790.00 USD | 0.00 USD | 0.00 USD | 7,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5495` | 630.26 USD | 145,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5500` | 645,720.00 USD | 645,720.00 USD | 5,990.00 USD | 1,440.00 USD | 6,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5510` | 452,560.00 USD | 452,560.00 USD | 0.00 USD | 0.00 USD | 849.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5520` | 631,550.00 USD | 631,550.00 USD | 4,110.00 USD | 1,920.00 USD | 1,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5530` | 451,710.00 USD | 451,710.00 USD | 1,260.00 USD | 0.00 USD | 432.53 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5540` | 623,670.00 USD | 623,670.00 USD | 12,840.00 USD | 4,860.00 USD | 18,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5545` | 47,450.00 USD | 145,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5550` | 450,020.00 USD | 450,020.00 USD | 1,090.00 USD | 1,520.00 USD | 32.36 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5560` | 587,460.00 USD | 587,460.00 USD | 13,490.00 USD | 1,920.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5565` | 3,250.00 USD | 97,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5570` | 447,370.00 USD | 447,370.00 USD | 0.00 USD | 1,940.00 USD | 553.28 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5580` | 565,800.00 USD | 565,800.00 USD | 6,000.00 USD | 6,820.00 USD | 18,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5585` | 10,520.00 USD | 94,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5590` | 444,880.00 USD | 444,880.00 USD | 1,100.00 USD | 2,960.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5600` | 534,690.00 USD | 534,690.00 USD | 4,070.00 USD | 8,160.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5610` | 438,580.00 USD | 438,580.00 USD | 1,550.00 USD | 2,040.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5615` | 1,720.00 USD | 83,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5620` | 520,000.00 USD | 520,000.00 USD | 19,480.00 USD | 7,420.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5630` | 433,040.00 USD | 433,040.00 USD | 715.25 USD | 1,020.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5640` | 481,550.00 USD | 481,550.00 USD | 2,950.00 USD | 741.21 USD | 53.84 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5650` | 426,280.00 USD | 426,280.00 USD | 0.00 USD | 3,040.00 USD | 463.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5660` | 477,810.00 USD | 477,810.00 USD | 11,490.00 USD | 2,990.00 USD | 4,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5670` | 422,780.00 USD | 422,780.00 USD | 0.00 USD | 232.89 USD | 5.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5680` | 458,910.00 USD | 458,910.00 USD | 5,100.00 USD | 0.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5695` | 164.24 USD | 82,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5700` | 450,930.00 USD | 450,930.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5715` | 289.08 USD | 81,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5720` | 448,360.00 USD | 448,360.00 USD | 0.00 USD | 1,520.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5725` | 4,880.00 USD | 81,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 214.84 USD | 76,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5740` | 445,440.00 USD | 445,440.00 USD | 8,160.00 USD | 1,100.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5760` | 434,570.00 USD | 434,570.00 USD | 2,150.00 USD | 0.00 USD | 27.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5780` | 432,390.00 USD | 432,390.00 USD | 0.00 USD | 0.00 USD | 1,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5785` | 662.59 USD | 76,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5790` | 422,540.00 USD | 422,540.00 USD | 0.00 USD | 0.00 USD | 59.63 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5800` | 430,870.00 USD | 430,870.00 USD | 1,610.00 USD | 0.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5820` | 426,420.00 USD | 426,420.00 USD | 0.00 USD | 0.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5830` | 422,480.00 USD | 422,480.00 USD | 0.00 USD | 1,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5835` | 1,690.00 USD | 75,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 210.96 USD | 74,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 586.80 USD | 73,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5870` | 421,480.00 USD | 421,480.00 USD | 2,890.00 USD | 1,290.00 USD | 18,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5880` | 419,900.00 USD | 419,900.00 USD | 3,110.00 USD | 1,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5885` | 440.16 USD | 73,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5890` | 398,930.00 USD | 398,930.00 USD | 4,730.00 USD | 1,580.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5895` | 1,690.00 USD | 72,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5900` | 415,390.00 USD | 415,390.00 USD | 3,120.00 USD | 1,560.00 USD | 81.07 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5910` | 388,920.00 USD | 388,920.00 USD | 4,730.00 USD | 3,210.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5920` | 410,630.00 USD | 410,630.00 USD | 11,690.00 USD | 2,820.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5925` | 609.14 USD | 71,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5930` | 376,880.00 USD | 376,880.00 USD | 14,740.00 USD | 4,790.00 USD | 13,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5935` | 21,790.00 USD | 70,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5940` | 390,090.00 USD | 390,090.00 USD | 10,090.00 USD | 0.00 USD | 9,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5950` | 343,810.00 USD | 343,810.00 USD | 25,410.00 USD | 14,370.00 USD | 6,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5955` | 3,850.00 USD | 48,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5960` | 370,220.00 USD | 370,220.00 USD | 18,180.00 USD | 18,410.00 USD | 13,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5970` | 297,690.00 USD | 297,690.00 USD | 12,480.00 USD | 7,520.00 USD | 17,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5975` | 157.22 USD | 45,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5980` | 320,580.00 USD | 320,580.00 USD | 20,380.00 USD | 826.53 USD | 19,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5990` | 259,960.00 USD | 259,960.00 USD | 18,900.00 USD | 2,880.00 USD | 44,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6000` | 279,460.00 USD | 279,460.00 USD | 3,320.00 USD | 2,140.00 USD | 18,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6005` | 852.06 USD | 44,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6010` | 193,400.00 USD | 193,400.00 USD | 735.24 USD | 461.96 USD | 12,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6020` | 255,240.00 USD | 255,240.00 USD | 4,890.00 USD | 8,040.00 USD | 4,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6030` | 179,660.00 USD | 179,660.00 USD | 12,380.00 USD | 13,200.00 USD | 27.08 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6040` | 238,200.00 USD | 238,200.00 USD | 8,620.00 USD | 3,100.00 USD | 7,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6045` | 527.44 USD | 43,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6050` | 154,060.00 USD | 154,060.00 USD | 6,990.00 USD | 4,070.00 USD | 13,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6060` | 218,570.00 USD | 218,570.00 USD | 0.00 USD | 0.00 USD | 92.01 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6070` | 129,800.00 USD | 129,800.00 USD | 16,200.00 USD | 15,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6080` | 218,470.00 USD | 218,470.00 USD | 2,860.00 USD | 0.00 USD | 161.30 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6085` | 455.69 USD | 43,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6090` | 97,990.00 USD | 97,990.00 USD | 9,390.00 USD | 14,090.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6100` | 215,450.00 USD | 215,450.00 USD | 21,400.00 USD | 36,110.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6105` | 6,090.00 USD | 43,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6110` | 60,330.00 USD | 60,330.00 USD | 5,380.00 USD | 8,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6120` | 132,820.00 USD | 132,820.00 USD | 2,100.00 USD | 5,720.00 USD | 18,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6130` | 46,480.00 USD | 46,480.00 USD | 2,140.00 USD | 596.50 USD | 22,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6140` | 106,330.00 USD | 106,330.00 USD | 13,410.00 USD | 8,040.00 USD | 10,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6150` | 20,970.00 USD | 20,970.00 USD | 8,850.00 USD | 12,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6160` | 74,150.00 USD | 74,150.00 USD | 12,920.00 USD | 7,460.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6180` | 47,240.00 USD | 47,240.00 USD | 20,870.00 USD | 2,610.00 USD | 283.36 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6195` | 3,170.00 USD | 36,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.6200` | 23,480.00 USD | 23,480.00 USD | 23,430.00 USD | 0.00 USD | 53.30 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6210` | 1,990.00 USD | 1,990.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6210` | 3,980.00 USD | 3,980.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6220` | 13,040.00 USD | 13,040.00 USD | 12,720.00 USD | 0.00 USD | 317.62 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6230` | 6,500.00 USD | 6,500.00 USD | 2,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6235` | 3,250.00 USD | 33,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.6240` | 41,930.00 USD | 41,930.00 USD | 28,380.00 USD | 0.00 USD | 514.08 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6250` | 11,520.00 USD | 11,520.00 USD | 5,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6255` | 286.65 USD | 30,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.6260` | 79,480.00 USD | 79,480.00 USD | 37,010.00 USD | 0.00 USD | 536.81 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6265` | 10,530.00 USD | 30,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6270` | 24,140.00 USD | 24,140.00 USD | 12,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6280` | 106,510.00 USD | 106,510.00 USD | 26,620.00 USD | 0.00 USD | 408.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6290` | 64,460.00 USD | 64,460.00 USD | 23,580.00 USD | 0.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6300` | 163,710.00 USD | 163,710.00 USD | 27,740.00 USD | 7,890.00 USD | 21,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6310` | 131,370.00 USD | 131,370.00 USD | 25,310.00 USD | 23,850.00 USD | 17,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6315` | 1,010.00 USD | 19,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.6320` | 275,260.00 USD | 275,260.00 USD | 53,460.00 USD | 17,170.00 USD | 40,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6330` | 258,370.00 USD | 258,370.00 USD | 50,610.00 USD | 28,280.00 USD | 48,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6340` | 450,910.00 USD | 450,910.00 USD | 68,660.00 USD | 51,670.00 USD | 55,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6350` | 397,820.00 USD | 397,820.00 USD | 73,350.00 USD | 25,560.00 USD | 40,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6360` | 617,750.00 USD | 617,750.00 USD | 77,000.00 USD | 9,720.00 USD | 80,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6370` | 566,920.00 USD | 566,920.00 USD | 76,930.00 USD | 17,000.00 USD | 75,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6375` | 5,900.00 USD | 18,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.6380` | 765,110.00 USD | 765,110.00 USD | 99,030.00 USD | 8,740.00 USD | 39,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6385` | 582.30 USD | 12,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6390` | 685,030.00 USD | 685,030.00 USD | 55,020.00 USD | 10,860.00 USD | 52,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6400` | 812,050.00 USD | 812,050.00 USD | 25,750.00 USD | 7,510.00 USD | 13,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6410` | 773,520.00 USD | 773,520.00 USD | 30,760.00 USD | 23,570.00 USD | 34,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6415` | 4,740.00 USD | 12,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.6420` | 910,480.00 USD | 910,480.00 USD | 55,350.00 USD | 26,560.00 USD | 16,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6430` | 915,450.00 USD | 915,450.00 USD | 79,540.00 USD | 29,430.00 USD | 32,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6435` | 3,450.00 USD | 7,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.6440` | 997,590.00 USD | 997,590.00 USD | 44,690.00 USD | 24,820.00 USD | 17,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6450` | 1,120,000.00 USD | 1,120,000.00 USD | 110,010.00 USD | 28,780.00 USD | 64,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6455` | 3,730.00 USD | 3,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.6460` | 1,340,000.00 USD | 1,340,000.00 USD | 172,610.00 USD | 46,630.00 USD | 119,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6470` | 1,260,000.00 USD | 1,260,000.00 USD | 126,580.00 USD | 4,240.00 USD | 7,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6480` | 1,460,000.00 USD | 1,460,000.00 USD | 86,440.00 USD | 3,880.00 USD | 33,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6485` | 259.68 USD | 259.68 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6490` | 1,430,000.00 USD | 1,430,000.00 USD | 173,130.00 USD | 0.00 USD | 234.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6500` | 1,670,000.00 USD | 1,670,000.00 USD | 73,560.00 USD | 0.00 USD | 132,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6510` | 1,540,000.00 USD | 1,540,000.00 USD | 98,030.00 USD | 0.00 USD | 11,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6520` | 1,990,000.00 USD | 1,990,000.00 USD | 211,670.00 USD | 10,910.00 USD | 105,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6530` | 1,620,000.00 USD | 1,620,000.00 USD | 75,650.00 USD | 6,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6540` | 2,070,000.00 USD | 2,070,000.00 USD | 15,730.00 USD | 0.00 USD | 61,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6550` | 1,640,000.00 USD | 1,640,000.00 USD | 11,450.00 USD | 0.00 USD | 10,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6560` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 5,380.00 USD | 817.52 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6580` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 28,280.00 USD | 633.84 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6590` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 98.76 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6600` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 4,180.00 USD | 814.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6610` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 5,010.00 USD | 210.40 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6620` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 588.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6630` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6640` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 700.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6650` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 3,160.00 USD | 17,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6660` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 6,770.00 USD | 396.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6670` | 1,700,000.00 USD | 1,700,000.00 USD | 18,850.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6690` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 3,550.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6700` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 215.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6710` | 1,790,000.00 USD | 1,790,000.00 USD | 50,800.00 USD | 1,920.00 USD | 30,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6720` | 2,210,000.00 USD | 2,210,000.00 USD | 58,470.00 USD | 0.00 USD | 30,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6730` | 1,820,000.00 USD | 1,820,000.00 USD | 24,320.00 USD | 3,670.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6740` | 2,250,000.00 USD | 2,250,000.00 USD | 39,730.00 USD | 0.00 USD | 111.52 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6750` | 1,950,000.00 USD | 1,950,000.00 USD | 93,070.00 USD | 13,090.00 USD | 22,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6760` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 77,970.00 USD | 33,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6770` | 2,010,000.00 USD | 2,010,000.00 USD | 26,380.00 USD | 11,960.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6780` | 2,460,000.00 USD | 2,460,000.00 USD | 63,600.00 USD | 14,400.00 USD | 17,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6790` | 2,100,000.00 USD | 2,100,000.00 USD | 33,610.00 USD | 32,830.00 USD | 22,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6800` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 16,590.00 USD | 297.02 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6810` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 1,940.00 USD | 10,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6820` | 2,560,000.00 USD | 2,560,000.00 USD | 32,570.00 USD | 53,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6830` | 2,240,000.00 USD | 2,240,000.00 USD | 47,170.00 USD | 42,650.00 USD | 42,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6840` | 2,770,000.00 USD | 2,770,000.00 USD | 57,890.00 USD | 54,300.00 USD | 102,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6850` | 2,390,000.00 USD | 2,390,000.00 USD | 96,870.00 USD | 31,640.00 USD | 21,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6860` | 2,850,000.00 USD | 2,850,000.00 USD | 49,930.00 USD | 14,540.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6870` | 2,520,000.00 USD | 2,520,000.00 USD | 103,470.00 USD | 5,540.00 USD | 16,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6880` | 2,900,000.00 USD | 2,900,000.00 USD | 38,030.00 USD | 17,300.00 USD | 131.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6890` | 2,580,000.00 USD | 2,580,000.00 USD | 14,350.00 USD | 9,600.00 USD | 40,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6900` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 15,510.00 USD | 16,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6910` | 2,690,000.00 USD | 2,690,000.00 USD | 43,430.00 USD | 5,760.00 USD | 60,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6920` | 3,070,000.00 USD | 3,070,000.00 USD | 69,620.00 USD | 2,090.00 USD | 61,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6930` | 2,730,000.00 USD | 2,730,000.00 USD | 26,830.00 USD | 0.00 USD | 13,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6940` | 3,130,000.00 USD | 3,130,000.00 USD | 14,220.00 USD | 0.00 USD | 42,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6950` | 2,790,000.00 USD | 2,790,000.00 USD | 33,700.00 USD | 8,880.00 USD | 13,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6960` | 3,200,000.00 USD | 3,200,000.00 USD | 59,960.00 USD | 0.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6970` | 2,890,000.00 USD | 2,890,000.00 USD | 91,820.00 USD | 8,430.00 USD | 34.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6980` | 3,250,000.00 USD | 3,250,000.00 USD | 35,980.00 USD | 14,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6990` | 2,920,000.00 USD | 2,920,000.00 USD | 14,320.00 USD | 8,940.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7000` | 3,320,000.00 USD | 3,320,000.00 USD | 29,740.00 USD | 0.00 USD | 40,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7010` | 2,970,000.00 USD | 2,970,000.00 USD | 33,760.00 USD | 4,020.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7020` | 3,390,000.00 USD | 3,390,000.00 USD | 16,350.00 USD | 0.00 USD | 53,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7030` | 3,000,000.00 USD | 3,000,000.00 USD | 18,690.00 USD | 0.00 USD | 10,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7040` | 3,580,000.00 USD | 3,580,000.00 USD | 95,520.00 USD | 0.00 USD | 96,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7050` | 3,100,000.00 USD | 3,100,000.00 USD | 59,720.00 USD | 5,290.00 USD | 36,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7060` | 3,840,000.00 USD | 3,840,000.00 USD | 47,840.00 USD | 33,490.00 USD | 177,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7070` | 3,190,000.00 USD | 3,190,000.00 USD | 28,570.00 USD | 25,720.00 USD | 29,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7075` | 2,220.00 USD | 2,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7080` | 4,010,000.00 USD | 4,010,000.00 USD | 24,440.00 USD | 64,870.00 USD | 82,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7090` | 3,240,000.00 USD | 3,240,000.00 USD | 36,000.00 USD | 6,660.00 USD | 13,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7100` | 4,370,000.00 USD | 4,370,000.00 USD | 150,830.00 USD | 63,530.00 USD | 149,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7110` | 3,280,000.00 USD | 3,280,000.00 USD | 11,400.00 USD | 10,040.00 USD | 13,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7120` | 4,780,000.00 USD | 4,780,000.00 USD | 101,040.00 USD | 78,760.00 USD | 227,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7130` | 3,380,000.00 USD | 3,380,000.00 USD | 44,600.00 USD | 8,520.00 USD | 48,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7140` | 5,190,000.00 USD | 5,190,000.00 USD | 202,560.00 USD | 67,260.00 USD | 133,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7150` | 3,460,000.00 USD | 3,460,000.00 USD | 42,280.00 USD | 11,520.00 USD | 29,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7160` | 5,530,000.00 USD | 5,530,000.00 USD | 113,040.00 USD | 65,260.00 USD | 164,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7170` | 3,520,000.00 USD | 3,520,000.00 USD | 22,310.00 USD | 15,690.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7180` | 5,820,000.00 USD | 5,820,000.00 USD | 165,860.00 USD | 56,910.00 USD | 66,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7190` | 3,570,000.00 USD | 3,570,000.00 USD | 19,020.00 USD | 8,580.00 USD | 16,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7200` | 6,140,000.00 USD | 6,140,000.00 USD | 93,750.00 USD | 45,160.00 USD | 178,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7210` | 3,610,000.00 USD | 3,610,000.00 USD | 10,550.00 USD | 18,090.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7220` | 6,620,000.00 USD | 6,620,000.00 USD | 318,420.00 USD | 67,130.00 USD | 98,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7230` | 3,640,000.00 USD | 3,640,000.00 USD | 7,870.00 USD | 7,380.00 USD | 8,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7240` | 6,920,000.00 USD | 6,920,000.00 USD | 146,110.00 USD | 24,910.00 USD | 129,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7250` | 3,670,000.00 USD | 3,670,000.00 USD | 16,070.00 USD | 7,230.00 USD | 13,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7255` | 43,950.00 USD | 46,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7260` | 7,250,000.00 USD | 7,250,000.00 USD | 106,410.00 USD | 52,120.00 USD | 176,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7270` | 3,750,000.00 USD | 3,750,000.00 USD | 46,660.00 USD | 5,430.00 USD | 24,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7280` | 7,480,000.00 USD | 7,480,000.00 USD | 99,750.00 USD | 40,180.00 USD | 84,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7290` | 3,820,000.00 USD | 3,820,000.00 USD | 33,620.00 USD | 8,680.00 USD | 25,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7300` | 7,760,000.00 USD | 7,760,000.00 USD | 115,310.00 USD | 60,310.00 USD | 109,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7310` | 3,860,000.00 USD | 3,860,000.00 USD | 10,990.00 USD | 8,670.00 USD | 18,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7320` | 8,100,000.00 USD | 8,100,000.00 USD | 189,840.00 USD | 65,640.00 USD | 80,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7330` | 3,880,000.00 USD | 3,880,000.00 USD | 12,500.00 USD | 3,310.00 USD | 9,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7340` | 8,200,000.00 USD | 8,200,000.00 USD | 31,260.00 USD | 8,620.00 USD | 62,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7345` | 150.17 USD | 46,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7350` | 3,890,000.00 USD | 3,890,000.00 USD | 735.24 USD | 3,000.00 USD | 3,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7360` | 8,390,000.00 USD | 8,390,000.00 USD | 103,600.00 USD | 46,790.00 USD | 34,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7370` | 3,920,000.00 USD | 3,920,000.00 USD | 12,380.00 USD | 8,300.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7380` | 8,540,000.00 USD | 8,540,000.00 USD | 73,710.00 USD | 19,000.00 USD | 60,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7390` | 3,930,000.00 USD | 3,930,000.00 USD | 6,990.00 USD | 4,650.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7400` | 8,590,000.00 USD | 8,590,000.00 USD | 1,730.00 USD | 6,610.00 USD | 37,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7410` | 3,960,000.00 USD | 3,960,000.00 USD | 16,200.00 USD | 1,640.00 USD | 9,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7420` | 8,700,000.00 USD | 8,700,000.00 USD | 35,810.00 USD | 41,830.00 USD | 31,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7430` | 3,960,000.00 USD | 3,960,000.00 USD | 1,240.00 USD | 969.00 USD | 149.25 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7440` | 8,880,000.00 USD | 8,880,000.00 USD | 74,450.00 USD | 39,890.00 USD | 70,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7450` | 3,970,000.00 USD | 3,970,000.00 USD | 8,160.00 USD | 1,410.00 USD | 4,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7460` | 9,050,000.00 USD | 9,050,000.00 USD | 88,800.00 USD | 28,800.00 USD | 51,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7470` | 3,990,000.00 USD | 3,990,000.00 USD | 5,380.00 USD | 0.00 USD | 6,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7480` | 9,180,000.00 USD | 9,180,000.00 USD | 60,580.00 USD | 28,900.00 USD | 38,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7490` | 3,990,000.00 USD | 3,990,000.00 USD | 2,140.00 USD | 596.50 USD | 2,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7500` | 4,000,000.00 USD | 4,000,000.00 USD | 6,120.00 USD | 0.00 USD | 14.33 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7500` | 9,270,000.00 USD | 9,270,000.00 USD | 52,320.00 USD | 12,610.00 USD | 25,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7520` | 9,390,000.00 USD | 9,390,000.00 USD | 53,470.00 USD | 13,000.00 USD | 51,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7540` | 9,440,000.00 USD | 9,440,000.00 USD | 30,340.00 USD | 1,890.00 USD | 25,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7560` | 9,500,000.00 USD | 9,500,000.00 USD | 26,000.00 USD | 7,570.00 USD | 22,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7580` | 9,610,000.00 USD | 9,610,000.00 USD | 55,420.00 USD | 11,790.00 USD | 45,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7600` | 9,750,000.00 USD | 9,750,000.00 USD | 57,020.00 USD | 4,320.00 USD | 80,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7620` | 9,850,000.00 USD | 9,850,000.00 USD | 54,140.00 USD | 24,170.00 USD | 21,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7635` | 143.11 USD | 46,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7640` | 9,960,000.00 USD | 9,960,000.00 USD | 50,390.00 USD | 13,520.00 USD | 41,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7660` | 10,130,000.00 USD | 10,130,000.00 USD | 56,130.00 USD | 18,130.00 USD | 91,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7680` | 10,270,000.00 USD | 10,270,000.00 USD | 66,570.00 USD | 32,520.00 USD | 41,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7700` | 10,330,000.00 USD | 10,330,000.00 USD | 10,860.00 USD | 12,600.00 USD | 41,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7720` | 10,450,000.00 USD | 10,450,000.00 USD | 58,380.00 USD | 32,920.00 USD | 25,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7725` | 165.62 USD | 46,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7740` | 10,560,000.00 USD | 10,560,000.00 USD | 51,600.00 USD | 25,250.00 USD | 35,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7760` | 10,610,000.00 USD | 10,610,000.00 USD | 38,170.00 USD | 2,980.00 USD | 12,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7765` | 330.78 USD | 46,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7780` | 10,740,000.00 USD | 10,740,000.00 USD | 68,800.00 USD | 20,860.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7800` | 10,900,000.00 USD | 10,900,000.00 USD | 60,490.00 USD | 21,940.00 USD | 80,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7820` | 11,010,000.00 USD | 11,010,000.00 USD | 90,020.00 USD | 17,850.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7840` | 11,120,000.00 USD | 11,120,000.00 USD | 95,370.00 USD | 7,150.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7860` | 11,230,000.00 USD | 11,230,000.00 USD | 32,690.00 USD | 12,990.00 USD | 63,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7880` | 11,290,000.00 USD | 11,290,000.00 USD | 11,900.00 USD | 22,650.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7900` | 11,380,000.00 USD | 11,380,000.00 USD | 59,120.00 USD | 16,710.00 USD | 17,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7910` | 11,420,000.00 USD | 11,420,000.00 USD | 30,620.00 USD | 5,860.00 USD | 153.33 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8005` | 19,120.00 USD | 66,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8035` | 114.11 USD | 66,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8615` | 15,640.00 USD | 81,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8665` | 378.95 USD | 82,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9935` | 166.01 USD | 82,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.00` | 21,250.00 USD | 103,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.06` | 18,750.00 USD | 122,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.07` | 81,760.00 USD | 204,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 3,080.00 USD | 207,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 479.74 USD | 207,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.12` | 2,800.00 USD | 210,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.21` | 101.43 USD | 210,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.27` | 13,320.00 USD | 223,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 197.51 USD | 224,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 284.61 USD | 224,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1545` | 258,840.00 USD | 0.00 USD | 160.39 USD | `-77.02%` | `1,038.12` |
| `Live` | `Long` | `0.1875` | 258,680.00 USD | 0.00 USD | 269.27 USD | `-72.11%` | `1,436.09` |
| `Live` | `Long` | `0.1955` | 258,410.00 USD | 0.00 USD | 2,210.00 USD | `-70.93%` | `11,284.25` |
| `Live` | `Long` | `0.2745` | 256,200.00 USD | 0.00 USD | 3,410.00 USD | `-59.18%` | `12,426.15` |
| `Live` | `Long` | `0.3035` | 252,790.00 USD | 0.00 USD | 607.00 USD | `-54.86%` | `2,000.00` |
| `Live` | `Long` | `0.3115` | 252,180.00 USD | 0.00 USD | 467.25 USD | `-53.67%` | `1,500.00` |
| `Live` | `Long` | `0.3175` | 251,720.00 USD | 0.00 USD | 10,620.00 USD | `-52.78%` | `33,446.85` |
| `Live` | `Long` | `0.3305` | 241,100.00 USD | 0.00 USD | 543.58 USD | `-50.85%` | `1,644.73` |
| `Live` | `Long` | `0.3495` | 240,550.00 USD | 0.00 USD | 244.65 USD | `-48.02%` | `700.00` |
| `Live` | `Long` | `0.3545` | 240,310.00 USD | 0.00 USD | 177.25 USD | `-47.28%` | `500.00` |
| `Live` | `Long` | `0.3565` | 240,130.00 USD | 0.00 USD | 2,140.00 USD | `-46.98%` | `6,000.00` |
| `Live` | `Long` | `0.3665` | 237,990.00 USD | 0.00 USD | 189.47 USD | `-45.49%` | `516.98` |
| `Live` | `Long` | `0.3675` | 237,800.00 USD | 0.00 USD | 194.23 USD | `-45.35%` | `528.52` |
| `Live` | `Long` | `0.3715` | 237,610.00 USD | 0.00 USD | 3,430.00 USD | `-44.75%` | `9,243.24` |
| `Live` | `Long` | `0.3795` | 234,170.00 USD | 0.00 USD | 948.75 USD | `-43.56%` | `2,500.00` |
| `Live` | `Long` | `0.3835` | 233,230.00 USD | 0.00 USD | 721.50 USD | `-42.97%` | `1,881.36` |
| `Live` | `Long` | `0.3845` | 232,500.00 USD | 0.00 USD | 495.42 USD | `-42.82%` | `1,288.49` |
| `Live` | `Long` | `0.3905` | 232,010.00 USD | 0.00 USD | 359.26 USD | `-41.92%` | `919.99` |
| `Live` | `Long` | `0.3955` | 231,650.00 USD | 0.00 USD | 2,640.00 USD | `-41.18%` | `6,686.27` |
| `Live` | `Long` | `0.3995` | 229,000.00 USD | 0.00 USD | 271.06 USD | `-40.59%` | `678.49` |
| `Live` | `Long` | `0.4005` | 228,730.00 USD | 0.00 USD | 405.48 USD | `-40.44%` | `1,012.44` |
| `Live` | `Long` | `0.4035` | 228,330.00 USD | 0.00 USD | 570.81 USD | `-39.99%` | `1,414.65` |
| `Live` | `Long` | `0.4135` | 227,760.00 USD | 0.00 USD | 1,600.00 USD | `-38.50%` | `3,868.97` |
| `Live` | `Long` | `0.4185` | 226,160.00 USD | 0.00 USD | 630.86 USD | `-37.76%` | `1,507.44` |
| `Live` | `Long` | `0.4255` | 225,530.00 USD | 0.00 USD | 224.96 USD | `-36.72%` | `528.69` |
| `Live` | `Long` | `0.4405` | 225,300.00 USD | 0.00 USD | 4,300.00 USD | `-34.49%` | `9,753.33` |
| `Live` | `Long` | `0.4475` | 221,010.00 USD | 0.00 USD | 226.63 USD | `-33.45%` | `506.43` |
| `Live` | `Long` | `0.4515` | 220,780.00 USD | 0.00 USD | 27,090.00 USD | `-32.85%` | `60,000.00` |
| `Live` | `Long` | `0.4525` | 193,690.00 USD | 0.00 USD | 147.06 USD | `-32.70%` | `325.00` |
| `Live` | `Long` | `0.4605` | 193,540.00 USD | 0.00 USD | 125.38 USD | `-31.51%` | `272.27` |
| `Live` | `Long` | `0.4625` | 193,420.00 USD | 0.00 USD | 1,100.00 USD | `-31.22%` | `2,368.95` |
| `Live` | `Long` | `0.4685` | 192,320.00 USD | 0.00 USD | 468.50 USD | `-30.32%` | `1,000.00` |
| `Live` | `Long` | `0.4695` | 191,850.00 USD | 0.00 USD | 5,350.00 USD | `-30.18%` | `11,392.84` |
| `Live` | `Long` | `0.4705` | 186,500.00 USD | 0.00 USD | 425.88 USD | `-30.03%` | `905.16` |
| `Live` | `Long` | `0.4715` | 186,080.00 USD | 0.00 USD | 7,780.00 USD | `-29.88%` | `16,497.37` |
| `Live` | `Long` | `0.4755` | 178,300.00 USD | 0.00 USD | 472.63 USD | `-29.28%` | `993.96` |
| `Live` | `Long` | `0.4765` | 177,830.00 USD | 0.00 USD | 990.20 USD | `-29.13%` | `2,078.06` |
| `Live` | `Long` | `0.4835` | 176,840.00 USD | 0.00 USD | 135.33 USD | `-28.09%` | `279.90` |
| `Live` | `Long` | `0.4865` | 176,700.00 USD | 0.00 USD | 3,170.00 USD | `-27.65%` | `6,508.47` |
| `Live` | `Long` | `0.4985` | 173,530.00 USD | 0.00 USD | 429.90 USD | `-25.86%` | `862.38` |
| `Live` | `Long` | `0.5085` | 173,100.00 USD | 0.00 USD | 102.82 USD | `-24.38%` | `202.20` |
| `Live` | `Long` | `0.5095` | 173,000.00 USD | 0.00 USD | 2,550.00 USD | `-24.23%` | `5,003.93` |
| `Live` | `Long` | `0.5125` | 170,450.00 USD | 0.00 USD | 248.05 USD | `-23.78%` | `484.00` |
| `Live` | `Long` | `0.5135` | 170,200.00 USD | 0.00 USD | 110.50 USD | `-23.63%` | `215.19` |
| `Live` | `Long` | `0.5145` | 170,090.00 USD | 0.00 USD | 288.78 USD | `-23.48%` | `561.28` |
| `Live` | `Long` | `0.5175` | 169,800.00 USD | 0.00 USD | 9,440.00 USD | `-23.04%` | `18,249.92` |
| `Live` | `Long` | `0.5315` | 160,360.00 USD | 0.00 USD | 11,510.00 USD | `-20.95%` | `21,664.95` |
| `Live` | `Long` | `0.5335` | 148,850.00 USD | 0.00 USD | 163.22 USD | `-20.66%` | `305.95` |
| `Live` | `Long` | `0.5385` | 148,680.00 USD | 0.00 USD | 2,690.00 USD | `-19.91%` | `5,002.20` |
| `Live` | `Long` | `0.5445` | 145,990.00 USD | 0.00 USD | 330.14 USD | `-19.02%` | `606.32` |
| `Live` | `Long` | `0.5495` | 145,660.00 USD | 0.00 USD | 630.26 USD | `-18.28%` | `1,146.97` |
| `Live` | `Long` | `0.5545` | 145,030.00 USD | 0.00 USD | 47,450.00 USD | `-17.53%` | `85,578.81` |
| `Live` | `Long` | `0.5565` | 97,570.00 USD | 0.00 USD | 3,250.00 USD | `-17.24%` | `5,839.42` |
| `Live` | `Long` | `0.5585` | 94,320.00 USD | 0.00 USD | 10,520.00 USD | `-16.94%` | `18,834.52` |
| `Live` | `Long` | `0.5615` | 83,810.00 USD | 0.00 USD | 1,720.00 USD | `-16.49%` | `3,064.43` |
| `Live` | `Long` | `0.5695` | 82,090.00 USD | 0.00 USD | 164.24 USD | `-15.30%` | `288.40` |
| `Live` | `Long` | `0.5715` | 81,920.00 USD | 0.00 USD | 289.08 USD | `-15.01%` | `505.82` |
| `Live` | `Long` | `0.5725` | 81,630.00 USD | 0.00 USD | 4,880.00 USD | `-14.86%` | `8,530.92` |
| `Live` | `Long` | `0.5735` | 76,750.00 USD | 0.00 USD | 214.84 USD | `-14.71%` | `374.62` |
| `Live` | `Long` | `0.5785` | 76,530.00 USD | 0.00 USD | 662.59 USD | `-13.96%` | `1,145.36` |
| `Live` | `Long` | `0.5835` | 75,870.00 USD | 0.00 USD | 1,690.00 USD | `-13.22%` | `2,899.29` |
| `Live` | `Long` | `0.5845` | 74,180.00 USD | 0.00 USD | 210.96 USD | `-13.07%` | `360.92` |
| `Live` | `Long` | `0.5865` | 73,970.00 USD | 0.00 USD | 586.80 USD | `-12.78%` | `1,000.51` |
| `Live` | `Long` | `0.5885` | 73,380.00 USD | 0.00 USD | 440.16 USD | `-12.48%` | `747.93` |
| `Live` | `Long` | `0.5895` | 72,940.00 USD | 0.00 USD | 1,690.00 USD | `-12.33%` | `2,865.95` |
| `Live` | `Long` | `0.5925` | 71,250.00 USD | 0.00 USD | 609.14 USD | `-11.88%` | `1,028.09` |
| `Live` | `Long` | `0.5935` | 70,640.00 USD | 0.00 USD | 21,790.00 USD | `-11.73%` | `36,718.57` |
| `Live` | `Long` | `0.5955` | 48,850.00 USD | 0.00 USD | 3,850.00 USD | `-11.44%` | `6,467.73` |
| `Live` | `Long` | `0.5975` | 45,000.00 USD | 0.00 USD | 157.22 USD | `-11.14%` | `263.13` |
| `Live` | `Long` | `0.6005` | 44,840.00 USD | 0.00 USD | 852.06 USD | `-10.69%` | `1,418.92` |
| `Live` | `Long` | `0.6045` | 43,990.00 USD | 0.00 USD | 527.44 USD | `-10.10%` | `872.53` |
| `Live` | `Long` | `0.6085` | 43,460.00 USD | 0.00 USD | 455.69 USD | `-9.50%` | `748.87` |
| `Live` | `Long` | `0.6105` | 43,010.00 USD | 0.00 USD | 6,090.00 USD | `-9.21%` | `9,974.00` |
| `Live` | `Long` | `0.6195` | 36,920.00 USD | 0.00 USD | 3,170.00 USD | `-7.87%` | `5,109.42` |
| `Live` | `Long` | `0.6235` | 33,750.00 USD | 0.00 USD | 3,250.00 USD | `-7.27%` | `5,220.30` |
| `Live` | `Long` | `0.6255` | 30,500.00 USD | 0.00 USD | 286.65 USD | `-6.98%` | `458.28` |
| `Live` | `Long` | `0.6265` | 30,210.00 USD | 0.00 USD | 10,530.00 USD | `-6.83%` | `16,808.62` |
| `Live` | `Long` | `0.6315` | 19,680.00 USD | 0.00 USD | 1,010.00 USD | `-6.08%` | `1,599.74` |
| `Live` | `Long` | `0.6375` | 18,670.00 USD | 0.00 USD | 5,900.00 USD | `-5.19%` | `9,256.34` |
| `Live` | `Long` | `0.6385` | 12,770.00 USD | 0.00 USD | 582.30 USD | `-5.04%` | `911.98` |
| `Live` | `Long` | `0.6415` | 12,190.00 USD | 0.00 USD | 4,740.00 USD | `-4.60%` | `7,394.26` |
| `Live` | `Long` | `0.6435` | 7,440.00 USD | 0.00 USD | 3,450.00 USD | `-4.30%` | `5,363.24` |
| `Live` | `Long` | `0.6455` | 3,990.00 USD | 0.00 USD | 3,730.00 USD | `-4.00%` | `5,780.73` |
| `Live` | `Long` | `0.6485` | 259.68 USD | 0.00 USD | 259.68 USD | `-3.55%` | `400.43` |
| `Live` | `Short` | `0.7075` | 2,220.00 USD | 2,220.00 USD | 0.00 USD | `+5.22%` | `3,144.75` |
| `Live` | `Short` | `0.7255` | 46,170.00 USD | 43,950.00 USD | 0.00 USD | `+7.90%` | `60,578.26` |
| `Live` | `Short` | `0.7345` | 46,320.00 USD | 150.17 USD | 0.00 USD | `+9.24%` | `204.45` |
| `Live` | `Short` | `0.7635` | 46,470.00 USD | 143.11 USD | 0.00 USD | `+13.55%` | `187.44` |
| `Live` | `Short` | `0.7725` | 46,630.00 USD | 165.62 USD | 0.00 USD | `+14.89%` | `214.40` |
| `Live` | `Short` | `0.7765` | 46,960.00 USD | 330.78 USD | 0.00 USD | `+15.48%` | `425.99` |
| `Live` | `Short` | `0.8005` | 66,080.00 USD | 19,120.00 USD | 0.00 USD | `+19.05%` | `23,882.80` |
| `Live` | `Short` | `0.8035` | 66,200.00 USD | 114.11 USD | 0.00 USD | `+19.50%` | `142.02` |
| `Live` | `Short` | `0.8615` | 81,840.00 USD | 15,640.00 USD | 0.00 USD | `+28.12%` | `18,155.35` |
| `Live` | `Short` | `0.8665` | 82,220.00 USD | 378.95 USD | 0.00 USD | `+28.87%` | `437.33` |
| `Live` | `Short` | `0.9935` | 82,380.00 USD | 166.01 USD | 0.00 USD | `+47.75%` | `167.10` |
| `Live` | `Short` | `1.00` | 103,630.00 USD | 21,250.00 USD | 0.00 USD | `+48.94%` | `21,218.48` |
| `Live` | `Short` | `1.06` | 122,380.00 USD | 18,750.00 USD | 0.00 USD | `+58.02%` | `17,648.14` |
| `Live` | `Short` | `1.07` | 204,140.00 USD | 81,760.00 USD | 0.00 USD | `+59.35%` | `76,300.00` |
| `Live` | `Short` | `1.09` | 207,220.00 USD | 3,080.00 USD | 0.00 USD | `+61.73%` | `2,829.20` |
| `Live` | `Short` | `1.09` | 207,700.00 USD | 479.74 USD | 0.00 USD | `+62.33%` | `439.52` |
| `Live` | `Short` | `1.12` | 210,490.00 USD | 2,800.00 USD | 0.00 USD | `+66.49%` | `2,500.00` |
| `Live` | `Short` | `1.21` | 210,600.00 USD | 101.43 USD | 0.00 USD | `+79.73%` | `83.93` |
| `Live` | `Short` | `1.27` | 223,920.00 USD | 13,320.00 USD | 0.00 USD | `+88.65%` | `10,500.00` |
| `Live` | `Short` | `1.32` | 224,110.00 USD | 197.51 USD | 0.00 USD | `+96.53%` | `149.46` |
| `Live` | `Short` | `1.33` | 224,400.00 USD | 284.61 USD | 0.00 USD | `+97.72%` | `214.07` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.3505` | 116,630.00 USD | 0.00 USD | 340.19 USD | `-47.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4635` | 116,280.00 USD | 0.00 USD | 104.57 USD | `-31.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4805` | 116,180.00 USD | 0.00 USD | 14,740.00 USD | `-28.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 101,440.00 USD | 0.00 USD | 604.46 USD | `-25.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5125` | 100,840.00 USD | 0.00 USD | 5,380.00 USD | `-23.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5205` | 95,460.00 USD | 0.00 USD | 228.77 USD | `-22.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5305` | 95,230.00 USD | 0.00 USD | 770.19 USD | `-21.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5445` | 94,460.00 USD | 0.00 USD | 8,750.00 USD | `-19.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5455` | 85,700.00 USD | 0.00 USD | 8,150.00 USD | `-18.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5485` | 77,550.00 USD | 0.00 USD | 4,500.00 USD | `-18.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5515` | 73,060.00 USD | 0.00 USD | 126.71 USD | `-17.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5525` | 72,930.00 USD | 0.00 USD | 126.90 USD | `-17.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5555` | 72,800.00 USD | 0.00 USD | 33,000.00 USD | `-17.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5565` | 39,800.00 USD | 0.00 USD | 300.09 USD | `-17.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5595` | 39,500.00 USD | 0.00 USD | 127.61 USD | `-16.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 39,380.00 USD | 0.00 USD | 339.84 USD | `-16.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5625` | 39,040.00 USD | 0.00 USD | 126.55 USD | `-16.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5655` | 38,910.00 USD | 0.00 USD | 127.62 USD | `-15.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5695` | 38,780.00 USD | 0.00 USD | 127.30 USD | `-15.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5715` | 38,660.00 USD | 0.00 USD | 127.63 USD | `-15.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5755` | 38,530.00 USD | 0.00 USD | 127.29 USD | `-14.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5785` | 38,400.00 USD | 0.00 USD | 127.36 USD | `-13.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5815` | 38,270.00 USD | 0.00 USD | 127.27 USD | `-13.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5835` | 38,150.00 USD | 0.00 USD | 178.88 USD | `-13.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5845` | 37,970.00 USD | 0.00 USD | 127.33 USD | `-13.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5865` | 37,840.00 USD | 0.00 USD | 128.36 USD | `-12.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5875` | 37,710.00 USD | 0.00 USD | 128.34 USD | `-12.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5895` | 37,580.00 USD | 0.00 USD | 128.45 USD | `-12.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5905` | 37,450.00 USD | 0.00 USD | 127.30 USD | `-12.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5925` | 37,330.00 USD | 0.00 USD | 128.33 USD | `-11.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5975` | 37,200.00 USD | 0.00 USD | 597.80 USD | `-11.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 36,600.00 USD | 0.00 USD | 3,510.00 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 33,090.00 USD | 0.00 USD | 1,510.00 USD | `-9.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6065` | 31,590.00 USD | 0.00 USD | 1,910.00 USD | `-9.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6085` | 29,680.00 USD | 0.00 USD | 301.32 USD | `-9.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6175` | 29,380.00 USD | 0.00 USD | 699.67 USD | `-8.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6185` | 28,680.00 USD | 0.00 USD | 177.58 USD | `-8.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 28,500.00 USD | 0.00 USD | 541.40 USD | `-7.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6275` | 27,960.00 USD | 0.00 USD | 433.11 USD | `-6.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6285` | 27,530.00 USD | 0.00 USD | 469.94 USD | `-6.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 27,060.00 USD | 0.00 USD | 4,430.00 USD | `-6.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6315` | 22,630.00 USD | 0.00 USD | 160.16 USD | `-6.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6335` | 22,470.00 USD | 0.00 USD | 8,390.00 USD | `-5.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6345` | 14,070.00 USD | 0.00 USD | 276.40 USD | `-5.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6395` | 13,800.00 USD | 0.00 USD | 1,200.00 USD | `-4.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6405` | 12,600.00 USD | 0.00 USD | 145.91 USD | `-4.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6445` | 12,450.00 USD | 0.00 USD | 121.42 USD | `-4.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6485` | 12,330.00 USD | 0.00 USD | 447.03 USD | `-3.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 11,880.00 USD | 0.00 USD | 567.58 USD | `-3.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6525` | 11,320.00 USD | 0.00 USD | 111.92 USD | `-2.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 11,210.00 USD | 0.00 USD | 349.76 USD | `-2.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 10,860.00 USD | 0.00 USD | 4,080.00 USD | `-2.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6565` | 6,780.00 USD | 0.00 USD | 284.88 USD | `-2.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6585` | 6,490.00 USD | 0.00 USD | 1,440.00 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6595` | 5,050.00 USD | 0.00 USD | 746.46 USD | `-1.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6605` | 4,310.00 USD | 0.00 USD | 580.23 USD | `-1.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6645` | 3,730.00 USD | 0.00 USD | 124.55 USD | `-1.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6655` | 3,600.00 USD | 0.00 USD | 1,110.00 USD | `-1.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6675` | 2,490.00 USD | 0.00 USD | 290.78 USD | `-0.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6685` | 2,200.00 USD | 0.00 USD | 170.95 USD | `-0.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6695` | 2,030.00 USD | 0.00 USD | 1,670.00 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 365.54 USD | 0.00 USD | 162.91 USD | `-0.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6715` | 202.63 USD | 0.00 USD | 202.63 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6725` | 1,670.00 USD | 1,670.00 USD | 0.00 USD | `+0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6745` | 2,270.00 USD | 598.31 USD | 0.00 USD | `+0.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6755` | 2,630.00 USD | 361.53 USD | 0.00 USD | `+0.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 4,760.00 USD | 2,130.00 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6805` | 4,980.00 USD | 214.20 USD | 0.00 USD | `+1.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6815` | 15,540.00 USD | 10,560.00 USD | 0.00 USD | `+1.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6825` | 15,650.00 USD | 112.49 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6835` | 15,760.00 USD | 108.41 USD | 0.00 USD | `+1.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6855` | 15,870.00 USD | 112.98 USD | 0.00 USD | `+1.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6865` | 16,160.00 USD | 292.33 USD | 0.00 USD | `+2.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6875` | 16,300.00 USD | 140.41 USD | 0.00 USD | `+2.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6885` | 16,820.00 USD | 514.80 USD | 0.00 USD | `+2.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6895` | 17,010.00 USD | 194.09 USD | 0.00 USD | `+2.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6915` | 17,110.00 USD | 101.96 USD | 0.00 USD | `+2.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6925` | 18,140.00 USD | 1,020.00 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6945` | 18,750.00 USD | 610.10 USD | 0.00 USD | `+3.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6955` | 18,850.00 USD | 101.38 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6965` | 19,640.00 USD | 789.18 USD | 0.00 USD | `+3.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6985` | 19,740.00 USD | 102.99 USD | 0.00 USD | `+3.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7005` | 19,880.00 USD | 137.19 USD | 0.00 USD | `+4.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7015` | 20,440.00 USD | 561.40 USD | 0.00 USD | `+4.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7085` | 21,390.00 USD | 947.29 USD | 0.00 USD | `+5.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7095` | 21,520.00 USD | 132.99 USD | 0.00 USD | `+5.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7115` | 21,640.00 USD | 122.04 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7135` | 21,950.00 USD | 307.58 USD | 0.00 USD | `+6.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7165` | 23,780.00 USD | 1,830.00 USD | 0.00 USD | `+6.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7195` | 24,160.00 USD | 373.99 USD | 0.00 USD | `+7.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7205` | 24,300.00 USD | 147.15 USD | 0.00 USD | `+7.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7215` | 27,570.00 USD | 3,260.00 USD | 0.00 USD | `+7.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7225` | 27,720.00 USD | 150.08 USD | 0.00 USD | `+7.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7265` | 34,130.00 USD | 6,410.00 USD | 0.00 USD | `+8.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7325` | 34,300.00 USD | 165.17 USD | 0.00 USD | `+8.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7345` | 35,330.00 USD | 1,030.00 USD | 0.00 USD | `+9.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7375` | 35,430.00 USD | 106.75 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7395` | 35,640.00 USD | 208.16 USD | 0.00 USD | `+9.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7405` | 36,370.00 USD | 733.09 USD | 0.00 USD | `+10.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7415` | 36,530.00 USD | 156.98 USD | 0.00 USD | `+10.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7425` | 36,660.00 USD | 132.95 USD | 0.00 USD | `+10.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7445` | 37,420.00 USD | 757.16 USD | 0.00 USD | `+10.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7455` | 39,590.00 USD | 2,170.00 USD | 0.00 USD | `+10.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7475` | 39,910.00 USD | 318.43 USD | 0.00 USD | `+11.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7505` | 40,050.00 USD | 141.39 USD | 0.00 USD | `+11.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7525` | 40,180.00 USD | 134.74 USD | 0.00 USD | `+11.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7565` | 44,300.00 USD | 4,120.00 USD | 0.00 USD | `+12.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7575` | 44,810.00 USD | 511.82 USD | 0.00 USD | `+12.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7585` | 44,940.00 USD | 135.82 USD | 0.00 USD | `+12.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7615` | 45,820.00 USD | 875.23 USD | 0.00 USD | `+13.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7635` | 45,920.00 USD | 103.35 USD | 0.00 USD | `+13.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7665` | 46,050.00 USD | 127.48 USD | 0.00 USD | `+13.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7675` | 46,150.00 USD | 101.61 USD | 0.00 USD | `+14.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7695` | 46,340.00 USD | 186.97 USD | 0.00 USD | `+14.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7705` | 46,450.00 USD | 109.43 USD | 0.00 USD | `+14.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7775` | 46,620.00 USD | 166.70 USD | 0.00 USD | `+15.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7815` | 47,750.00 USD | 1,140.00 USD | 0.00 USD | `+16.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7865` | 54,070.00 USD | 6,310.00 USD | 0.00 USD | `+16.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8095` | 54,200.00 USD | 133.42 USD | 0.00 USD | `+20.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8125` | 66,270.00 USD | 12,070.00 USD | 0.00 USD | `+20.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8335` | 67,200.00 USD | 929.08 USD | 0.00 USD | `+23.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8475` | 107,790.00 USD | 40,590.00 USD | 0.00 USD | `+26.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8505` | 124,530.00 USD | 16,740.00 USD | 0.00 USD | `+26.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8515` | 137,250.00 USD | 12,720.00 USD | 0.00 USD | `+26.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8525` | 149,030.00 USD | 11,780.00 USD | 0.00 USD | `+26.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8705` | 150,310.00 USD | 1,280.00 USD | 0.00 USD | `+29.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8725` | 150,470.00 USD | 159.86 USD | 0.00 USD | `+29.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 150,660.00 USD | 193.62 USD | 0.00 USD | `+35.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 151,000.00 USD | 340.54 USD | 0.00 USD | `+41.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 151,150.00 USD | 145.72 USD | 0.00 USD | `+44.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 152,140.00 USD | 987.50 USD | 0.00 USD | `+46.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 152,270.00 USD | 136.10 USD | 0.00 USD | `+48.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 152,820.00 USD | 550.48 USD | 0.00 USD | `+48.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 153,140.00 USD | 314.99 USD | 0.00 USD | `+52.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 153,740.00 USD | 602.17 USD | 0.00 USD | `+56.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 154,100.00 USD | 360.61 USD | 0.00 USD | `+57.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 155,040.00 USD | 942.77 USD | 0.00 USD | `+60.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 155,380.00 USD | 337.31 USD | 0.00 USD | `+60.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 155,780.00 USD | 397.19 USD | 0.00 USD | `+63.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 168,910.00 USD | 13,130.00 USD | 0.00 USD | `+85.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 170,230.00 USD | 1,320.00 USD | 0.00 USD | `+87.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 207,080.00 USD | 36,850.00 USD | 0.00 USD | `+92.67%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.5320` | 710,760.00 USD | 0.00 USD | 710,760.00 USD | 11,240.00 USD | 0.00 USD | 3,480.00 USD |
| `7D` | `0.5340` | 696,050.00 USD | 0.00 USD | 696,050.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD |
| `1D` | `0.5350` | 505,520.00 USD | 0.00 USD | 505,520.00 USD | 2,650.00 USD | 1,850.00 USD | 1,880.00 USD |
| `7D` | `0.5360` | 693,450.00 USD | 0.00 USD | 693,450.00 USD | 2,440.00 USD | 3,040.00 USD | 44.79 USD |
| `1D` | `0.5370` | 499,140.00 USD | 0.00 USD | 499,140.00 USD | 4,720.00 USD | 2,450.00 USD | 1,860.00 USD |
| `7D` | `0.5380` | 687,920.00 USD | 0.00 USD | 687,920.00 USD | 0.00 USD | 1,550.00 USD | 2,910.00 USD |
| `1D` | `0.5390` | 490,110.00 USD | 0.00 USD | 490,110.00 USD | 6,850.00 USD | 1,140.00 USD | 5,480.00 USD |
| `7D` | `0.5400` | 683,460.00 USD | 0.00 USD | 683,460.00 USD | 0.00 USD | 0.00 USD | 80.65 USD |
| `1D` | `0.5410` | 476,640.00 USD | 0.00 USD | 476,640.00 USD | 618.50 USD | 0.00 USD | 2,000.00 USD |
| `7D` | `0.5420` | 683,380.00 USD | 0.00 USD | 683,380.00 USD | 7,660.00 USD | 1,290.00 USD | 2,860.00 USD |
| `1D` | `0.5430` | 474,030.00 USD | 0.00 USD | 474,030.00 USD | 3,300.00 USD | 0.00 USD | 3,430.00 USD |
| `7D` | `0.5440` | 671,580.00 USD | 0.00 USD | 671,580.00 USD | 0.00 USD | 1,150.00 USD | 6,970.00 USD |
| `1D` | `0.5450` | 467,300.00 USD | 0.00 USD | 467,300.00 USD | 1,070.00 USD | 298.25 USD | 1,030.00 USD |
| `7D` | `0.5460` | 663,460.00 USD | 0.00 USD | 663,460.00 USD | 2,250.00 USD | 3,030.00 USD | 5,180.00 USD |
| `1D` | `0.5470` | 464,900.00 USD | 0.00 USD | 464,900.00 USD | 3,980.00 USD | 633.67 USD | 499.51 USD |
| `7D` | `0.5480` | 652,990.00 USD | 0.00 USD | 652,990.00 USD | 2,000.00 USD | 795.70 USD | 4,480.00 USD |
| `1D` | `0.5490` | 459,790.00 USD | 0.00 USD | 459,790.00 USD | 0.00 USD | 0.00 USD | 7,230.00 USD |
| `7D` | `0.5500` | 645,720.00 USD | 0.00 USD | 645,720.00 USD | 5,990.00 USD | 1,440.00 USD | 6,740.00 USD |
| `1D` | `0.5510` | 452,560.00 USD | 0.00 USD | 452,560.00 USD | 0.00 USD | 0.00 USD | 849.87 USD |
| `7D` | `0.5520` | 631,550.00 USD | 0.00 USD | 631,550.00 USD | 4,110.00 USD | 1,920.00 USD | 1,840.00 USD |
| `1D` | `0.5530` | 451,710.00 USD | 0.00 USD | 451,710.00 USD | 1,260.00 USD | 0.00 USD | 432.53 USD |
| `7D` | `0.5540` | 623,670.00 USD | 0.00 USD | 623,670.00 USD | 12,840.00 USD | 4,860.00 USD | 18,510.00 USD |
| `1D` | `0.5550` | 450,020.00 USD | 0.00 USD | 450,020.00 USD | 1,090.00 USD | 1,520.00 USD | 32.36 USD |
| `7D` | `0.5560` | 587,460.00 USD | 0.00 USD | 587,460.00 USD | 13,490.00 USD | 1,920.00 USD | 6,250.00 USD |
| `1D` | `0.5570` | 447,370.00 USD | 0.00 USD | 447,370.00 USD | 0.00 USD | 1,940.00 USD | 553.28 USD |
| `7D` | `0.5580` | 565,800.00 USD | 0.00 USD | 565,800.00 USD | 6,000.00 USD | 6,820.00 USD | 18,290.00 USD |
| `1D` | `0.5590` | 444,880.00 USD | 0.00 USD | 444,880.00 USD | 1,100.00 USD | 2,960.00 USD | 2,240.00 USD |
| `7D` | `0.5600` | 534,690.00 USD | 0.00 USD | 534,690.00 USD | 4,070.00 USD | 8,160.00 USD | 2,470.00 USD |
| `1D` | `0.5610` | 438,580.00 USD | 0.00 USD | 438,580.00 USD | 1,550.00 USD | 2,040.00 USD | 1,950.00 USD |
| `7D` | `0.5620` | 520,000.00 USD | 0.00 USD | 520,000.00 USD | 19,480.00 USD | 7,420.00 USD | 11,550.00 USD |
| `1D` | `0.5630` | 433,040.00 USD | 0.00 USD | 433,040.00 USD | 715.25 USD | 1,020.00 USD | 5,030.00 USD |
| `7D` | `0.5640` | 481,550.00 USD | 0.00 USD | 481,550.00 USD | 2,950.00 USD | 741.21 USD | 53.84 USD |
| `1D` | `0.5650` | 426,280.00 USD | 0.00 USD | 426,280.00 USD | 0.00 USD | 3,040.00 USD | 463.14 USD |
| `7D` | `0.5660` | 477,810.00 USD | 0.00 USD | 477,810.00 USD | 11,490.00 USD | 2,990.00 USD | 4,420.00 USD |
| `1D` | `0.5670` | 422,780.00 USD | 0.00 USD | 422,780.00 USD | 0.00 USD | 232.89 USD | 5.87 USD |
| `7D` | `0.5680` | 458,910.00 USD | 0.00 USD | 458,910.00 USD | 5,100.00 USD | 0.00 USD | 2,880.00 USD |
| `7D` | `0.5700` | 450,930.00 USD | 0.00 USD | 450,930.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD |
| `7D` | `0.5720` | 448,360.00 USD | 0.00 USD | 448,360.00 USD | 0.00 USD | 1,520.00 USD | 1,410.00 USD |
| `7D` | `0.5740` | 445,440.00 USD | 0.00 USD | 445,440.00 USD | 8,160.00 USD | 1,100.00 USD | 1,600.00 USD |
| `7D` | `0.5760` | 434,570.00 USD | 0.00 USD | 434,570.00 USD | 2,150.00 USD | 0.00 USD | 27.34 USD |
| `7D` | `0.5780` | 432,390.00 USD | 0.00 USD | 432,390.00 USD | 0.00 USD | 0.00 USD | 1,520.00 USD |
| `1D` | `0.5790` | 422,540.00 USD | 0.00 USD | 422,540.00 USD | 0.00 USD | 0.00 USD | 59.63 USD |
| `7D` | `0.5800` | 430,870.00 USD | 0.00 USD | 430,870.00 USD | 1,610.00 USD | 0.00 USD | 2,850.00 USD |
| `7D` | `0.5820` | 426,420.00 USD | 0.00 USD | 426,420.00 USD | 0.00 USD | 0.00 USD | 6,520.00 USD |
| `1D` | `0.5830` | 422,480.00 USD | 0.00 USD | 422,480.00 USD | 0.00 USD | 1,000.00 USD | 0.00 USD |
| `1D` | `0.5870` | 421,480.00 USD | 0.00 USD | 421,480.00 USD | 2,890.00 USD | 1,290.00 USD | 18,370.00 USD |
| `7D` | `0.5880` | 419,900.00 USD | 0.00 USD | 419,900.00 USD | 3,110.00 USD | 1,400.00 USD | 0.00 USD |
| `1D` | `0.5890` | 398,930.00 USD | 0.00 USD | 398,930.00 USD | 4,730.00 USD | 1,580.00 USD | 3,700.00 USD |
| `7D` | `0.5900` | 415,390.00 USD | 0.00 USD | 415,390.00 USD | 3,120.00 USD | 1,560.00 USD | 81.07 USD |
| `1D` | `0.5910` | 388,920.00 USD | 0.00 USD | 388,920.00 USD | 4,730.00 USD | 3,210.00 USD | 4,100.00 USD |
| `7D` | `0.5920` | 410,630.00 USD | 0.00 USD | 410,630.00 USD | 11,690.00 USD | 2,820.00 USD | 6,030.00 USD |
| `1D` | `0.5930` | 376,880.00 USD | 0.00 USD | 376,880.00 USD | 14,740.00 USD | 4,790.00 USD | 13,540.00 USD |
| `7D` | `0.5940` | 390,090.00 USD | 0.00 USD | 390,090.00 USD | 10,090.00 USD | 0.00 USD | 9,780.00 USD |
| `1D` | `0.5950` | 343,810.00 USD | 0.00 USD | 343,810.00 USD | 25,410.00 USD | 14,370.00 USD | 6,340.00 USD |
| `7D` | `0.5960` | 370,220.00 USD | 0.00 USD | 370,220.00 USD | 18,180.00 USD | 18,410.00 USD | 13,040.00 USD |
| `1D` | `0.5970` | 297,690.00 USD | 0.00 USD | 297,690.00 USD | 12,480.00 USD | 7,520.00 USD | 17,730.00 USD |
| `7D` | `0.5980` | 320,580.00 USD | 0.00 USD | 320,580.00 USD | 20,380.00 USD | 826.53 USD | 19,920.00 USD |
| `1D` | `0.5990` | 259,960.00 USD | 0.00 USD | 259,960.00 USD | 18,900.00 USD | 2,880.00 USD | 44,790.00 USD |
| `7D` | `0.6000` | 279,460.00 USD | 0.00 USD | 279,460.00 USD | 3,320.00 USD | 2,140.00 USD | 18,760.00 USD |
| `1D` | `0.6010` | 193,400.00 USD | 0.00 USD | 193,400.00 USD | 735.24 USD | 461.96 USD | 12,530.00 USD |
| `7D` | `0.6020` | 255,240.00 USD | 0.00 USD | 255,240.00 USD | 4,890.00 USD | 8,040.00 USD | 4,110.00 USD |
| `1D` | `0.6030` | 179,660.00 USD | 0.00 USD | 179,660.00 USD | 12,380.00 USD | 13,200.00 USD | 27.08 USD |
| `7D` | `0.6040` | 238,200.00 USD | 0.00 USD | 238,200.00 USD | 8,620.00 USD | 3,100.00 USD | 7,920.00 USD |
| `1D` | `0.6050` | 154,060.00 USD | 0.00 USD | 154,060.00 USD | 6,990.00 USD | 4,070.00 USD | 13,200.00 USD |
| `7D` | `0.6060` | 218,570.00 USD | 0.00 USD | 218,570.00 USD | 0.00 USD | 0.00 USD | 92.01 USD |
| `1D` | `0.6070` | 129,800.00 USD | 0.00 USD | 129,800.00 USD | 16,200.00 USD | 15,620.00 USD | 0.00 USD |
| `7D` | `0.6080` | 218,470.00 USD | 0.00 USD | 218,470.00 USD | 2,860.00 USD | 0.00 USD | 161.30 USD |
| `1D` | `0.6090` | 97,990.00 USD | 0.00 USD | 97,990.00 USD | 9,390.00 USD | 14,090.00 USD | 14,170.00 USD |
| `7D` | `0.6100` | 215,450.00 USD | 0.00 USD | 215,450.00 USD | 21,400.00 USD | 36,110.00 USD | 25,120.00 USD |
| `1D` | `0.6110` | 60,330.00 USD | 0.00 USD | 60,330.00 USD | 5,380.00 USD | 8,470.00 USD | 0.00 USD |
| `7D` | `0.6120` | 132,820.00 USD | 0.00 USD | 132,820.00 USD | 2,100.00 USD | 5,720.00 USD | 18,660.00 USD |
| `1D` | `0.6130` | 46,480.00 USD | 0.00 USD | 46,480.00 USD | 2,140.00 USD | 596.50 USD | 22,770.00 USD |
| `7D` | `0.6140` | 106,330.00 USD | 0.00 USD | 106,330.00 USD | 13,410.00 USD | 8,040.00 USD | 10,720.00 USD |
| `1D` | `0.6150` | 20,970.00 USD | 0.00 USD | 20,970.00 USD | 8,850.00 USD | 12,120.00 USD | 0.00 USD |
| `7D` | `0.6160` | 74,150.00 USD | 0.00 USD | 74,150.00 USD | 12,920.00 USD | 7,460.00 USD | 6,520.00 USD |
| `7D` | `0.6180` | 47,240.00 USD | 0.00 USD | 47,240.00 USD | 20,870.00 USD | 2,610.00 USD | 283.36 USD |
| `7D` | `0.6200` | 23,480.00 USD | 0.00 USD | 23,480.00 USD | 23,430.00 USD | 0.00 USD | 53.30 USD |
| `1D` | `0.6210` | 1,990.00 USD | 1,990.00 USD | 0.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6210` | 3,980.00 USD | 3,980.00 USD | 0.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6210` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6220` | 13,040.00 USD | 13,040.00 USD | 0.00 USD | 12,720.00 USD | 0.00 USD | 317.62 USD |
| `1D` | `0.6230` | 6,500.00 USD | 6,500.00 USD | 0.00 USD | 2,520.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6240` | 41,930.00 USD | 41,930.00 USD | 0.00 USD | 28,380.00 USD | 0.00 USD | 514.08 USD |
| `1D` | `0.6250` | 11,520.00 USD | 11,520.00 USD | 0.00 USD | 5,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6260` | 79,480.00 USD | 79,480.00 USD | 0.00 USD | 37,010.00 USD | 0.00 USD | 536.81 USD |
| `1D` | `0.6270` | 24,140.00 USD | 24,140.00 USD | 0.00 USD | 12,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6280` | 106,510.00 USD | 106,510.00 USD | 0.00 USD | 26,620.00 USD | 0.00 USD | 408.60 USD |
| `1D` | `0.6290` | 64,460.00 USD | 64,460.00 USD | 0.00 USD | 23,580.00 USD | 0.00 USD | 16,750.00 USD |
| `7D` | `0.6300` | 163,710.00 USD | 163,710.00 USD | 0.00 USD | 27,740.00 USD | 7,890.00 USD | 21,570.00 USD |
| `1D` | `0.6310` | 131,370.00 USD | 131,370.00 USD | 0.00 USD | 25,310.00 USD | 23,850.00 USD | 17,750.00 USD |
| `7D` | `0.6320` | 275,260.00 USD | 275,260.00 USD | 0.00 USD | 53,460.00 USD | 17,170.00 USD | 40,930.00 USD |
| `1D` | `0.6330` | 258,370.00 USD | 258,370.00 USD | 0.00 USD | 50,610.00 USD | 28,280.00 USD | 48,120.00 USD |
| `7D` | `0.6340` | 450,910.00 USD | 450,910.00 USD | 0.00 USD | 68,660.00 USD | 51,670.00 USD | 55,320.00 USD |
| `1D` | `0.6350` | 397,820.00 USD | 397,820.00 USD | 0.00 USD | 73,350.00 USD | 25,560.00 USD | 40,540.00 USD |
| `7D` | `0.6360` | 617,750.00 USD | 617,750.00 USD | 0.00 USD | 77,000.00 USD | 9,720.00 USD | 80,120.00 USD |
| `1D` | `0.6370` | 566,920.00 USD | 566,920.00 USD | 0.00 USD | 76,930.00 USD | 17,000.00 USD | 75,170.00 USD |
| `7D` | `0.6380` | 765,110.00 USD | 765,110.00 USD | 0.00 USD | 99,030.00 USD | 8,740.00 USD | 39,590.00 USD |
| `1D` | `0.6390` | 685,030.00 USD | 685,030.00 USD | 0.00 USD | 55,020.00 USD | 10,860.00 USD | 52,220.00 USD |
| `7D` | `0.6400` | 812,050.00 USD | 812,050.00 USD | 0.00 USD | 25,750.00 USD | 7,510.00 USD | 13,670.00 USD |
| `1D` | `0.6410` | 773,520.00 USD | 773,520.00 USD | 0.00 USD | 30,760.00 USD | 23,570.00 USD | 34,170.00 USD |
| `7D` | `0.6420` | 910,480.00 USD | 910,480.00 USD | 0.00 USD | 55,350.00 USD | 26,560.00 USD | 16,520.00 USD |
| `1D` | `0.6430` | 915,450.00 USD | 915,450.00 USD | 0.00 USD | 79,540.00 USD | 29,430.00 USD | 32,960.00 USD |
| `7D` | `0.6440` | 997,590.00 USD | 997,590.00 USD | 0.00 USD | 44,690.00 USD | 24,820.00 USD | 17,600.00 USD |
| `1D` | `0.6450` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 110,010.00 USD | 28,780.00 USD | 64,360.00 USD |
| `7D` | `0.6460` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 172,610.00 USD | 46,630.00 USD | 119,970.00 USD |
| `1D` | `0.6470` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 126,580.00 USD | 4,240.00 USD | 7,140.00 USD |
| `7D` | `0.6480` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 86,440.00 USD | 3,880.00 USD | 33,040.00 USD |
| `1D` | `0.6490` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 173,130.00 USD | 0.00 USD | 234.70 USD |
| `7D` | `0.6500` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 73,560.00 USD | 0.00 USD | 132,600.00 USD |
| `1D` | `0.6510` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 98,030.00 USD | 0.00 USD | 11,630.00 USD |
| `7D` | `0.6520` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 211,670.00 USD | 10,910.00 USD | 105,350.00 USD |
| `1D` | `0.6530` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 75,650.00 USD | 6,060.00 USD | 0.00 USD |
| `7D` | `0.6540` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 15,730.00 USD | 0.00 USD | 61,310.00 USD |
| `1D` | `0.6550` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 11,450.00 USD | 0.00 USD | 10,560.00 USD |
| `7D` | `0.6560` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 5,380.00 USD | 817.52 USD |
| `7D` | `0.6580` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 28,280.00 USD | 633.84 USD |
| `1D` | `0.6590` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 98.76 USD |
| `7D` | `0.6600` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 4,180.00 USD | 814.64 USD |
| `1D` | `0.6610` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 5,010.00 USD | 210.40 USD |
| `7D` | `0.6620` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 588.76 USD |
| `1D` | `0.6630` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,740.00 USD |
| `7D` | `0.6640` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 700.80 USD |
| `1D` | `0.6650` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 3,160.00 USD | 17,480.00 USD |
| `7D` | `0.6660` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 6,770.00 USD | 396.96 USD |
| `1D` | `0.6670` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 18,850.00 USD | 0.00 USD | 5,410.00 USD |
| `1D` | `0.6690` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 3,550.00 USD | 4,390.00 USD |
| `7D` | `0.6700` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 215.36 USD |
| `1D` | `0.6710` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 50,800.00 USD | 1,920.00 USD | 30,520.00 USD |
| `7D` | `0.6720` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 58,470.00 USD | 0.00 USD | 30,170.00 USD |
| `1D` | `0.6730` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 24,320.00 USD | 3,670.00 USD | 4,500.00 USD |
| `7D` | `0.6740` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 39,730.00 USD | 0.00 USD | 111.52 USD |
| `1D` | `0.6750` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 93,070.00 USD | 13,090.00 USD | 22,020.00 USD |
| `7D` | `0.6760` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 77,970.00 USD | 33,160.00 USD |
| `1D` | `0.6770` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 26,380.00 USD | 11,960.00 USD | 14,290.00 USD |
| `7D` | `0.6780` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 63,600.00 USD | 14,400.00 USD | 17,960.00 USD |
| `1D` | `0.6790` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 33,610.00 USD | 32,830.00 USD | 22,910.00 USD |
| `7D` | `0.6800` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 297.02 USD |
| `1D` | `0.6810` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 1,940.00 USD | 10,080.00 USD |
| `7D` | `0.6820` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 32,570.00 USD | 53,450.00 USD | 0.00 USD |
| `1D` | `0.6830` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 47,170.00 USD | 42,650.00 USD | 42,990.00 USD |
| `7D` | `0.6840` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 57,890.00 USD | 54,300.00 USD | 102,430.00 USD |
| `1D` | `0.6850` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 96,870.00 USD | 31,640.00 USD | 21,540.00 USD |
| `7D` | `0.6860` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 49,930.00 USD | 14,540.00 USD | 10,480.00 USD |
| `1D` | `0.6870` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 103,470.00 USD | 5,540.00 USD | 16,430.00 USD |
| `7D` | `0.6880` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 38,030.00 USD | 17,300.00 USD | 131.40 USD |
| `1D` | `0.6890` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 14,350.00 USD | 9,600.00 USD | 40,270.00 USD |
| `7D` | `0.6900` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 15,510.00 USD | 16,550.00 USD |
| `1D` | `0.6910` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 43,430.00 USD | 5,760.00 USD | 60,800.00 USD |
| `7D` | `0.6920` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 69,620.00 USD | 2,090.00 USD | 61,890.00 USD |
| `1D` | `0.6930` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 26,830.00 USD | 0.00 USD | 13,840.00 USD |
| `7D` | `0.6940` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 14,220.00 USD | 0.00 USD | 42,460.00 USD |
| `1D` | `0.6950` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 33,700.00 USD | 8,880.00 USD | 13,260.00 USD |
| `7D` | `0.6960` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 59,960.00 USD | 0.00 USD | 12,390.00 USD |
| `1D` | `0.6970` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 91,820.00 USD | 8,430.00 USD | 34.66 USD |
| `7D` | `0.6980` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 35,980.00 USD | 14,140.00 USD | 0.00 USD |
| `1D` | `0.6990` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 14,320.00 USD | 8,940.00 USD | 6,660.00 USD |
| `7D` | `0.7000` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 29,740.00 USD | 0.00 USD | 40,190.00 USD |
| `1D` | `0.7010` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 33,760.00 USD | 4,020.00 USD | 16,240.00 USD |
| `7D` | `0.7020` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 16,350.00 USD | 0.00 USD | 53,380.00 USD |
| `1D` | `0.7030` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 18,690.00 USD | 0.00 USD | 10,530.00 USD |
| `7D` | `0.7040` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 95,520.00 USD | 0.00 USD | 96,320.00 USD |
| `1D` | `0.7050` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 59,720.00 USD | 5,290.00 USD | 36,890.00 USD |
| `7D` | `0.7060` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 47,840.00 USD | 33,490.00 USD | 177,930.00 USD |
| `1D` | `0.7070` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 28,570.00 USD | 25,720.00 USD | 29,510.00 USD |
| `7D` | `0.7080` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 24,440.00 USD | 64,870.00 USD | 82,800.00 USD |
| `1D` | `0.7090` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 36,000.00 USD | 6,660.00 USD | 13,210.00 USD |
| `7D` | `0.7100` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 150,830.00 USD | 63,530.00 USD | 149,060.00 USD |
| `1D` | `0.7110` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 11,400.00 USD | 10,040.00 USD | 13,710.00 USD |
| `7D` | `0.7120` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 101,040.00 USD | 78,760.00 USD | 227,910.00 USD |
| `1D` | `0.7130` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 44,600.00 USD | 8,520.00 USD | 48,550.00 USD |
| `7D` | `0.7140` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 202,560.00 USD | 67,260.00 USD | 133,720.00 USD |
| `1D` | `0.7150` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 42,280.00 USD | 11,520.00 USD | 29,720.00 USD |
| `7D` | `0.7160` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 113,040.00 USD | 65,260.00 USD | 164,620.00 USD |
| `1D` | `0.7170` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 22,310.00 USD | 15,690.00 USD | 22,980.00 USD |
| `7D` | `0.7180` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 165,860.00 USD | 56,910.00 USD | 66,960.00 USD |
| `1D` | `0.7190` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 19,020.00 USD | 8,580.00 USD | 16,930.00 USD |
| `7D` | `0.7200` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 93,750.00 USD | 45,160.00 USD | 178,510.00 USD |
| `1D` | `0.7210` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 10,550.00 USD | 18,090.00 USD | 16,250.00 USD |
| `7D` | `0.7220` | 6,620,000.00 USD | 6,620,000.00 USD | 0.00 USD | 318,420.00 USD | 67,130.00 USD | 98,110.00 USD |
| `1D` | `0.7230` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 7,870.00 USD | 7,380.00 USD | 8,260.00 USD |
| `7D` | `0.7240` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 146,110.00 USD | 24,910.00 USD | 129,240.00 USD |
| `1D` | `0.7250` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 16,070.00 USD | 7,230.00 USD | 13,030.00 USD |
| `7D` | `0.7260` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 106,410.00 USD | 52,120.00 USD | 176,200.00 USD |
| `1D` | `0.7270` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 46,660.00 USD | 5,430.00 USD | 24,800.00 USD |
| `7D` | `0.7280` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 99,750.00 USD | 40,180.00 USD | 84,240.00 USD |
| `1D` | `0.7290` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 33,620.00 USD | 8,680.00 USD | 25,650.00 USD |
| `7D` | `0.7300` | 7,760,000.00 USD | 7,760,000.00 USD | 0.00 USD | 115,310.00 USD | 60,310.00 USD | 109,550.00 USD |
| `1D` | `0.7310` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 10,990.00 USD | 8,670.00 USD | 18,990.00 USD |
| `7D` | `0.7320` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 189,840.00 USD | 65,640.00 USD | 80,650.00 USD |
| `1D` | `0.7330` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 12,500.00 USD | 3,310.00 USD | 9,300.00 USD |
| `7D` | `0.7340` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 31,260.00 USD | 8,620.00 USD | 62,890.00 USD |
| `1D` | `0.7350` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 735.24 USD | 3,000.00 USD | 3,550.00 USD |
| `7D` | `0.7360` | 8,390,000.00 USD | 8,390,000.00 USD | 0.00 USD | 103,600.00 USD | 46,790.00 USD | 34,980.00 USD |
| `1D` | `0.7370` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 12,380.00 USD | 8,300.00 USD | 7,420.00 USD |
| `7D` | `0.7380` | 8,540,000.00 USD | 8,540,000.00 USD | 0.00 USD | 73,710.00 USD | 19,000.00 USD | 60,700.00 USD |
| `1D` | `0.7390` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 6,990.00 USD | 4,650.00 USD | 4,100.00 USD |
| `7D` | `0.7400` | 8,590,000.00 USD | 8,590,000.00 USD | 0.00 USD | 1,730.00 USD | 6,610.00 USD | 37,560.00 USD |
| `1D` | `0.7410` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 16,200.00 USD | 1,640.00 USD | 9,550.00 USD |
| `7D` | `0.7420` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 35,810.00 USD | 41,830.00 USD | 31,340.00 USD |
| `1D` | `0.7430` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 1,240.00 USD | 969.00 USD | 149.25 USD |
| `7D` | `0.7440` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 74,450.00 USD | 39,890.00 USD | 70,670.00 USD |
| `1D` | `0.7450` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 8,160.00 USD | 1,410.00 USD | 4,110.00 USD |
| `7D` | `0.7460` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 88,800.00 USD | 28,800.00 USD | 51,570.00 USD |
| `1D` | `0.7470` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 5,380.00 USD | 0.00 USD | 6,850.00 USD |
| `7D` | `0.7480` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 60,580.00 USD | 28,900.00 USD | 38,210.00 USD |
| `1D` | `0.7490` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 2,140.00 USD | 596.50 USD | 2,060.00 USD |
| `1D` | `0.7500` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 6,120.00 USD | 0.00 USD | 14.33 USD |
| `7D` | `0.7500` | 9,270,000.00 USD | 9,270,000.00 USD | 0.00 USD | 52,320.00 USD | 12,610.00 USD | 25,050.00 USD |
| `7D` | `0.7520` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 53,470.00 USD | 13,000.00 USD | 51,060.00 USD |
| `7D` | `0.7540` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 30,340.00 USD | 1,890.00 USD | 25,360.00 USD |
| `7D` | `0.7560` | 9,500,000.00 USD | 9,500,000.00 USD | 0.00 USD | 26,000.00 USD | 7,570.00 USD | 22,270.00 USD |
| `7D` | `0.7580` | 9,610,000.00 USD | 9,610,000.00 USD | 0.00 USD | 55,420.00 USD | 11,790.00 USD | 45,670.00 USD |
| `7D` | `0.7600` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 57,020.00 USD | 4,320.00 USD | 80,730.00 USD |
| `7D` | `0.7620` | 9,850,000.00 USD | 9,850,000.00 USD | 0.00 USD | 54,140.00 USD | 24,170.00 USD | 21,570.00 USD |
| `7D` | `0.7640` | 9,960,000.00 USD | 9,960,000.00 USD | 0.00 USD | 50,390.00 USD | 13,520.00 USD | 41,670.00 USD |
| `7D` | `0.7660` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 56,130.00 USD | 18,130.00 USD | 91,160.00 USD |
| `7D` | `0.7680` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 66,570.00 USD | 32,520.00 USD | 41,020.00 USD |
| `7D` | `0.7700` | 10,330,000.00 USD | 10,330,000.00 USD | 0.00 USD | 10,860.00 USD | 12,600.00 USD | 41,500.00 USD |
| `7D` | `0.7720` | 10,450,000.00 USD | 10,450,000.00 USD | 0.00 USD | 58,380.00 USD | 32,920.00 USD | 25,790.00 USD |
| `7D` | `0.7740` | 10,560,000.00 USD | 10,560,000.00 USD | 0.00 USD | 51,600.00 USD | 25,250.00 USD | 35,710.00 USD |
| `7D` | `0.7760` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 38,170.00 USD | 2,980.00 USD | 12,750.00 USD |
| `7D` | `0.7780` | 10,740,000.00 USD | 10,740,000.00 USD | 0.00 USD | 68,800.00 USD | 20,860.00 USD | 32,590.00 USD |
| `7D` | `0.7800` | 10,900,000.00 USD | 10,900,000.00 USD | 0.00 USD | 60,490.00 USD | 21,940.00 USD | 80,720.00 USD |
| `7D` | `0.7820` | 11,010,000.00 USD | 11,010,000.00 USD | 0.00 USD | 90,020.00 USD | 17,850.00 USD | 6,210.00 USD |
| `7D` | `0.7840` | 11,120,000.00 USD | 11,120,000.00 USD | 0.00 USD | 95,370.00 USD | 7,150.00 USD | 2,170.00 USD |
| `7D` | `0.7860` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 32,690.00 USD | 12,990.00 USD | 63,730.00 USD |
| `7D` | `0.7880` | 11,290,000.00 USD | 11,290,000.00 USD | 0.00 USD | 11,900.00 USD | 22,650.00 USD | 29,600.00 USD |
| `7D` | `0.7900` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 59,120.00 USD | 16,710.00 USD | 17,390.00 USD |
| `7D` | `0.7910` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 30,620.00 USD | 5,860.00 USD | 153.33 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `88.64M` | Total OI Tokens: `143,105,422.4 APT`
  * 1h OI Change: `-8.54%` | 4h OI Change: `-11.01%` | 24h OI Change: `-12.98%`
  * Exchange Breakdown: Binance=`16.35M` | Bybit=`18.08M` | OKX=`4.20M` | Hyperliquid=`3.56M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `946.72` | Last 24h: `8.88K` | Last 3d: `10.89K` | Last 7d: `5.22K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0018%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0049%` | **USDT KuCoin** | `0.0092%` |
| **USDT MEXC** | `-0.0017%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0009%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `APT` | `41.34%` | `58.66%` | `0.70` | 28,320,000.00 USD |
| `15M` | `Binance` | `40.34%` | `59.66%` | `0.68` | 11,450,000.00 USD |
| `15M` | `OKX` | `48.06%` | `51.94%` | `0.93` | 3,950,000.00 USD |
| `15M` | `Bybit` | `46.54%` | `53.46%` | `0.87` | 5,310,000.00 USD |
| `15M` | `KuCoin` | `43.17%` | `56.83%` | `0.76` | 431,760.00 USD |
| `15M` | `Gate` | `48.29%` | `51.71%` | `0.93` | 416,000.00 USD |
| `15M` | `Bitget` | `44.36%` | `55.64%` | `0.80` | 1,300,000.00 USD |
| `15M` | `BingX` | `14.54%` | `85.46%` | `0.17` | 2,010,000.00 USD |
| `15M` | `MEXC` | `36.37%` | `63.63%` | `0.57` | 1,290,000.00 USD |
| `15M` | `Bitunix` | `44.11%` | `55.89%` | `0.79` | 415,170.00 USD |
| `15M` | `Hyperliquid` | `49.58%` | `50.42%` | `0.98` | 858,380.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.19%` | `48.81%` | `1.05` | 64,640.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `40.82%` | `59.18%` | `0.69` | 594,240.00 USD |
| `15M` | `HTX` | `53.8%` | `46.2%` | `1.16` | 66,530.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `66.34%` | `33.66%` | `1.97` | 71,230.00 USD |
| `15M` | `Aster` | `53.03%` | `46.97%` | `1.13` | 40,580.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `4.84%` | `95.16%` | `0.05` | 36,420.00 USD |
| `15M` | `Whale Positions` | `40.34%` | `59.66%` | `0.68` | 11,450,000.00 USD |
| `15M` | `Global Accounts` | `41.34%` | `58.66%` | `0.70` | 28,320,000.00 USD |
| `1H` | `APT` | `46.56%` | `53.44%` | `0.87` | 56,430,000.00 USD |
| `1H` | `Binance` | `48.95%` | `51.05%` | `0.96` | 22,330,000.00 USD |
| `1H` | `OKX` | `46.4%` | `53.6%` | `0.87` | 8,660,000.00 USD |
| `1H` | `Bybit` | `44.77%` | `55.23%` | `0.81` | 6,450,000.00 USD |
| `1H` | `KuCoin` | `46.5%` | `53.5%` | `0.87` | 786,710.00 USD |
| `1H` | `Gate` | `46.42%` | `53.58%` | `0.87` | 1,430,000.00 USD |
| `1H` | `Bitget` | `44.99%` | `55.01%` | `0.82` | 2,110,000.00 USD |
| `1H` | `BingX` | `45.2%` | `54.8%` | `0.82` | 885,500.00 USD |
| `1H` | `MEXC` | `39.72%` | `60.28%` | `0.66` | 976,660.00 USD |
| `1H` | `Bitunix` | `52.07%` | `47.93%` | `1.09` | 1,860,000.00 USD |
| `1H` | `Hyperliquid` | `26.82%` | `73.18%` | `0.37` | 1,060,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.27%` | `51.73%` | `0.93` | 8,740,000.00 USD |
| `1H` | `Crypto.com` | `39.55%` | `60.45%` | `0.65` | 1,690.00 USD |
| `1H` | `WhiteBIT` | `5%` | `95%` | `0.05` | 735,770.00 USD |
| `1H` | `HTX` | `42.64%` | `57.36%` | `0.74` | 95,300.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `38.28%` | `61.72%` | `0.62` | 127,600.00 USD |
| `1H` | `Aster` | `38.51%` | `61.49%` | `0.63` | 103,430.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `41.14%` | `58.86%` | `0.70` | 85,420.00 USD |
| `1H` | `Whale Positions` | `48.95%` | `51.05%` | `0.96` | 22,330,000.00 USD |
| `1H` | `Global Accounts` | `46.56%` | `53.44%` | `0.87` | 56,430,000.00 USD |
| `4H` | `APT` | `41.09%` | `58.91%` | `0.70` | 99,310,000.00 USD |
| `4H` | `Binance` | `41.89%` | `58.11%` | `0.72` | 37,320,000.00 USD |
| `4H` | `OKX` | `47.49%` | `52.51%` | `0.90` | 15,290,000.00 USD |
| `4H` | `Bybit` | `43.7%` | `56.3%` | `0.78` | 10,860,000.00 USD |
| `4H` | `KuCoin` | `48.54%` | `51.46%` | `0.94` | 2,140,000.00 USD |
| `4H` | `Gate` | `51.53%` | `48.47%` | `1.06` | 2,010,000.00 USD |
| `4H` | `Bitget` | `39.35%` | `60.65%` | `0.65` | 3,190,000.00 USD |
| `4H` | `BingX` | `15.83%` | `84.17%` | `0.19` | 2,850,000.00 USD |
| `4H` | `MEXC` | `41.28%` | `58.72%` | `0.70` | 1,670,000.00 USD |
| `4H` | `Bitunix` | `45.38%` | `54.62%` | `0.83` | 3,470,000.00 USD |
| `4H` | `Hyperliquid` | `40.67%` | `59.33%` | `0.69` | 1,270,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.51%` | `51.49%` | `0.94` | 15,520,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 1,870.00 USD |
| `4H` | `WhiteBIT` | `47.46%` | `52.54%` | `0.90` | 3,080,000.00 USD |
| `4H` | `HTX` | `53.74%` | `46.26%` | `1.16` | 110,440.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `73.49%` | `26.51%` | `2.77` | 191,910.00 USD |
| `4H` | `Aster` | `53.25%` | `46.75%` | `1.14` | 232,850.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `26.08%` | `73.92%` | `0.35` | 101,120.00 USD |
| `4H` | `Whale Positions` | `41.89%` | `58.11%` | `0.72` | 37,320,000.00 USD |
| `4H` | `Global Accounts` | `41.09%` | `58.91%` | `0.70` | 99,310,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.6717` | `0.6708` | `0.6717` | `0.6727` | `0.6676` | 334,763.13 USD | 213,901.71 USD | 120,861.42 USD | 93,040.30 USD | `+27.79%` | `17B / 7S` |
| `0:00 UTC` | `0.6677` | `0.6685` | `0.6677` | `0.6704` | `0.6665` | 391,631.76 USD | 249,885.86 USD | 141,745.90 USD | 108,139.96 USD | `+27.61%` | `10B / 3S` |
| `5:00 UTC` | `0.6715` | `0.6701` | `0.6715` | `0.6721` | `0.6670` | 386,689.12 USD | 212,109.34 USD | 174,579.78 USD | 37,529.57 USD | `+9.71%` | `19B / 4S` |
| `0:00 UTC` | `0.6734` | `0.6731` | `0.6734` | `0.6741` | `0.6704` | 427,696.28 USD | 267,875.40 USD | 159,820.88 USD | 108,054.53 USD | `+25.26%` | `9B / 2S` |
| `5:00 UTC` | `0.6713` | `0.6715` | `0.6713` | `0.6739` | `0.6704` | 216,510.95 USD | 86,107.15 USD | 130,403.80 USD | -44,296.65 USD | `-20.46%` | `5B / 11S` |
| `0:00 UTC` | `0.6618` | `0.6610` | `0.6618` | `0.6728` | `0.6545` | 3,111,032.57 USD | 1,289,720.42 USD | 1,821,312.14 USD | -531,591.72 USD | `-17.09%` | `14B / 47S` |
| `5:00 UTC` | `0.6646` | `0.6634` | `0.6646` | `0.6663` | `0.6601` | 1,040,684.48 USD | 553,372.77 USD | 487,311.70 USD | 66,061.07 USD | `+6.35%` | `21B / 6S` |
| `0:00 UTC` | `0.6256` | `0.6358` | `0.6256` | `0.6640` | `0.6136` | 10,130,057.36 USD | 3,799,647.14 USD | 6,330,410.22 USD | -2,530,763.08 USD | `-24.98%` | `3B / 31S` |
| `5:00 UTC` | `0.6208` | `0.6173` | `0.6208` | `0.6292` | `0.6004` | 5,930,137.61 USD | 2,790,946.56 USD | 3,139,191.05 USD | -348,244.48 USD | `-5.87%` | `7B / 8S` |
| `0:00 UTC` | `0.6268` | `0.6225` | `0.6268` | `0.6282` | `0.6164` | 788,261.47 USD | 390,802.82 USD | 397,458.65 USD | -6,655.84 USD | `-0.84%` | `21B / 15S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 21:06` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6898` | 0.00 USD | 0.00 USD |
| `10-28 21:06` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6871` | 68,000.00 USD | 0.00 USD |
| `10-28 21:02` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6867` | 0.00 USD | 0.00 USD |
| `10-28 20:37` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6858` | 33,000.00 USD | 0.00 USD |
| `10-28 20:01` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6782` | 0.00 USD | 0.00 USD |
| `10-28 20:01` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6808` | 79,000.00 USD | 0.00 USD |
| `10-28 19:48` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6764` | 22,000.00 USD | 0.00 USD |
| `10-28 19:46` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6752` | 44,000.00 USD | 0.00 USD |
| `10-28 19:46` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6752` | 44,000.00 USD | 0.00 USD |
| `10-28 19:43` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6771` | 0.00 USD | 0.00 USD |
| `10-28 19:43` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6793` | 39,000.00 USD | 0.00 USD |
| `10-28 19:41` | `Volume 1.0M APT` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6752` | 361,000.00 USD | 0.00 USD |
| `10-28 19:35` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6807` | 0.00 USD | 0.00 USD |
| `10-28 19:31` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6762` | 79,000.00 USD | 0.00 USD |
| `10-28 19:31` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6762` | 79,000.00 USD | 0.00 USD |
| `10-28 19:31` | `Range 0.002` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `0.6762` | 106,000.00 USD | 0.00 USD |
| `10-28 19:21` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6771` | 75,000.00 USD | 0.00 USD |
| `10-28 19:07` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6859` | 121,000.00 USD | 0.00 USD |
| `10-28 18:48` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6796` | 47,000.00 USD | 0.00 USD |
| `10-28 18:44` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6793` | 107,000.00 USD | 0.00 USD |
| `10-28 18:37` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6818` | 0.00 USD | 0.00 USD |
| `10-28 17:54` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6887` | 177,000.00 USD | 0.00 USD |
| `10-28 17:46` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6884` | 112,000.00 USD | 0.00 USD |
| `10-28 17:43` | `Volume 1.0M APT` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6842` | 275,000.00 USD | 0.00 USD |
| `10-28 17:36` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6934` | 22,000.00 USD | 0.00 USD |
| `10-28 17:03` | `Volume 1.0M APT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6995` | 234,000.00 USD | 0.00 USD |
| `10-28 16:15` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6994` | 140,000.00 USD | 0.00 USD |
| `10-28 16:02` | `Volume 1.0M APT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6994` | 223,000.00 USD | 0.00 USD |
| `10-28 14:46` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6950` | 67,000.00 USD | 0.00 USD |
| `10-28 14:31` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6922` | 0.00 USD | 0.00 USD |
| `10-28 14:31` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6896` | 58,000.00 USD | 0.00 USD |
| `10-28 14:31` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6896` | 58,000.00 USD | 0.00 USD |
| `10-28 14:09` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6972` | 0.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6976` | 0.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.7006` | 0.00 USD | 0.00 USD |
| `10-28 13:57` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6962` | 0.00 USD | 0.00 USD |
| `10-28 13:33` | `Volume 1.0M APT` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6929` | 351,000.00 USD | 0.00 USD |
| `10-28 12:44` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6912` | 0.00 USD | 0.00 USD |
| `10-28 12:22` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6924` | 0.00 USD | 0.00 USD |
| `10-28 10:16` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6976` | 25,000.00 USD | 0.00 USD |
| `10-28 09:48` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6958` | 18,000.00 USD | 0.00 USD |
| `10-28 09:29` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6985` | 55,000.00 USD | 0.00 USD |
| `10-28 09:11` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.7008` | 0.00 USD | 0.00 USD |
| `10-28 09:04` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.7021` | 0.00 USD | 0.00 USD |
| `10-28 09:00` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.7001` | 27,000.00 USD | 0.00 USD |
| `10-28 08:49` | `Range 0.002` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `0.6966` | 73,000.00 USD | 0.00 USD |
| `10-28 08:31` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6974` | 0.00 USD | 0.00 USD |
| `10-28 07:29` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.7003` | 0.00 USD | 0.00 USD |
| `10-28 07:23` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6977` | 10,000.00 USD | 0.00 USD |
| `10-28 06:12` | `Range 0.002` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.6982` | 122,000.00 USD | 0.00 USD |
| `10-28 05:31` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6963` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -11,930.00 USD | 319,900.00 USD | **`ACCUMULATION`** |
| `15m` | -224,050.00 USD | -3,020,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -405,980.00 USD | -3,860,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -475,820.00 USD | -4,510,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -455,830.00 USD | -4,080,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -693,390.00 USD | -5,790,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -369,110.00 USD | -6,210,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -247,360.00 USD | -6,990,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -257,040.00 USD | -7,170,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,650,000.00 USD | -10,540,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,210,000.00 USD | -24,730,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,940,000.00 USD | -105,410,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-11.93K` | 15m=`-224.05K` | 1h=`-475.82K` | 24h=`-1.65M`
* Futures Capital Netflows: 5m=`+319.90K` | 15m=`-3.02M` | 1h=`-4.51M` | 24h=`-10.54M`
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
  * Execution Entry: `0.6880` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-0.5122` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.69`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.6921` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.89` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.31`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.6956`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
