# 🏛️ SOVEREIGN CANDIDATE DOSSIER: APT
**Canonical Key**: `APT` | **Broker Instrument**: `APTUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 02:15:30 IST` (`2026-10-29 20:45:30 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.6617` | `0.6640` | `0.6468` | `0.6539` | `3,103,019` | 2,027,197.50 USD | -246,687.75 USD | `-12.17%` | -4,035,144.20 USD | `-1.78` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.6539` | `0.6548` | `0.6462` | `0.6494` | `1,800,768` | 1,170,599.39 USD | -122,513.88 USD | `-10.47%` | -4,157,658.08 USD | `-0.73` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.6493` | `0.6495` | `0.6134` | `0.6232` | `9,435,689` | 5,933,525.40 USD | -2,042,223.43 USD | `-34.42%` | -6,199,881.52 USD | `-4.19` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.6721` | `0.6728` | `0.6545` | `0.6633` | `4,707,296` | 3,111,032.57 USD | -531,591.72 USD | `-17.09%` | -3,854,517.52 USD | `-2.44` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.6633` | `0.6663` | `0.6600` | `0.6617` | `1,568,931` | 1,040,684.48 USD | 66,061.07 USD | `+6.35%` | -3,788,456.45 USD | `+0.84` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.6617` | `0.6640` | `0.6134` | `0.6244` | `14,264,158` | 9,084,331.15 USD | -2,404,328.81 USD | `-26.47%` | -6,192,785.26 USD | `-4.11` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.6796` | `0.6804` | `0.6673` | `0.6699` | `4,032,719` | 2,714,496.22 USD | -416,792.27 USD | `-15.35%` | -3,627,547.27 USD | `-0.90` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.6700` | `0.6740` | `0.6665` | `0.6721` | `2,120,904` | 1,422,528.11 USD | 209,427.40 USD | `+14.72%` | -3,418,119.86 USD | `+1.29` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.6721` | `0.6728` | `0.6134` | `0.6246` | `20,527,916` | 13,228,264.58 USD | -2,869,490.92 USD | `-21.69%` | -6,287,610.78 USD | `-3.93` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -1,678,888.13 USD | `+0.66` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -3,147,816.26 USD | `-1.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6134` | `0.6249` | `20,553,829` | 13,244,449.04 USD | -2,868,991.18 USD | `-21.66%` | -6,016,807.44 USD | `-1.91` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.6611` | `0.6759` | `0.6485` | `0.6561` | `10,656,422` | 7,044,804.33 USD | -366,898.68 USD | `-5.21%` | -1,470,659.97 USD | `+1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6561` | `0.6774` | `0.6549` | `0.6712` | `7,448,343` | 4,965,296.85 USD | -60,141.40 USD | `-1.21%` | -1,530,801.38 USD | `+1.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -1,678,888.13 USD | `+0.66` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -3,147,816.26 USD | `-1.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6134` | `0.6249` | `20,553,829` | 13,244,449.04 USD | -2,868,991.18 USD | `-21.66%` | -6,016,807.44 USD | `-1.91` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`0.6901`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:14:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.6971` | 5,803.06 USD | `-` | `NEWS_INTEL` | `-` | #APT Whale BUY: 5.80K USD at 0.6971 USD [API] | `2026-10-28 01:20:10` |
| `ANNOUNCEMENT` | `INFO` | `0.7002` | 8,527.41 USD | `-` | `NEWS_INTEL` | `-` | #APT Whale BUY: 8.53K USD at 0.7002 USD [API] | `2026-10-28 01:55:53` |
| `ANNOUNCEMENT` | `INFO` | `0.7021` | 10,246.45 USD | `-` | `NEWS_INTEL` | `-` | #APT Whale BUY: 10.25K USD at 0.7021 USD [API] | `2026-10-28 03:31:19` |
| `ANNOUNCEMENT` | `INFO` | `0.7021` | 10,246.45 USD | `-` | `NEWS_INTEL` | `-` | #APT Whale BUY: 10.25K USD at 0.7021 USD [API] | `2026-10-28 03:31:19` |


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
| `Live` | `Long Liquidation` | `0.5335` | 163.22 USD | 148,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5385` | 2,690.00 USD | 148,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5445` | 330.14 USD | 145,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5495` | 630.26 USD | 145,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5545` | 47,450.00 USD | 145,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5565` | 3,250.00 USD | 97,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5585` | 10,520.00 USD | 94,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5615` | 1,720.00 USD | 83,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 164.24 USD | 82,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5715` | 289.08 USD | 81,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5725` | 4,880.00 USD | 81,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 214.84 USD | 76,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5770` | 2,010,000.00 USD | 2,010,000.00 USD | 2,150.00 USD | 0.00 USD | 26.97 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5785` | 662.59 USD | 76,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5790` | 2,000,000.00 USD | 2,000,000.00 USD | 1,610.00 USD | 0.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5810` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5830` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5835` | 1,690.00 USD | 75,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 210.96 USD | 74,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5860` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 658.88 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5865` | 586.80 USD | 73,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5870` | 1,430,000.00 USD | 1,430,000.00 USD | 2,890.00 USD | 631.19 USD | 3,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5870` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 1,400.00 USD | 65.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5880` | 1,430,000.00 USD | 1,430,000.00 USD | 1,270.00 USD | 1,580.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5885` | 440.16 USD | 73,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5890` | 1,420,000.00 USD | 1,420,000.00 USD | 3,460.00 USD | 0.00 USD | 7.65 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5890` | 1,990,000.00 USD | 1,990,000.00 USD | 3,110.00 USD | 0.00 USD | 15.37 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5895` | 1,690.00 USD | 72,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5900` | 1,420,000.00 USD | 1,420,000.00 USD | 4,730.00 USD | 1,390.00 USD | 3.61 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5910` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 1,820.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5910` | 1,990,000.00 USD | 1,990,000.00 USD | 3,120.00 USD | 1,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5920` | 1,400,000.00 USD | 1,400,000.00 USD | 11,320.00 USD | 2,650.00 USD | 1,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5925` | 609.14 USD | 71,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5930` | 1,390,000.00 USD | 1,390,000.00 USD | 3,420.00 USD | 0.00 USD | 5,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5930` | 1,980,000.00 USD | 1,980,000.00 USD | 21,790.00 USD | 2,820.00 USD | 15,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5935` | 21,790.00 USD | 70,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5940` | 1,380,000.00 USD | 1,380,000.00 USD | 5,890.00 USD | 0.00 USD | 4,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5950` | 1,370,000.00 USD | 1,370,000.00 USD | 19,520.00 USD | 2,470.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5950` | 1,940,000.00 USD | 1,940,000.00 USD | 13,060.00 USD | 0.00 USD | 4,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5955` | 3,850.00 USD | 48,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5960` | 1,340,000.00 USD | 1,340,000.00 USD | 8,460.00 USD | 456.46 USD | 6,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5970` | 1,330,000.00 USD | 1,330,000.00 USD | 4,020.00 USD | 2,820.00 USD | 4,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5970` | 1,920,000.00 USD | 1,920,000.00 USD | 5,120.00 USD | 1,640.00 USD | 16,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5975` | 157.22 USD | 45,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5980` | 1,320,000.00 USD | 1,320,000.00 USD | 6,400.00 USD | 1,740.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5990` | 1,300,000.00 USD | 1,300,000.00 USD | 12,500.00 USD | 1,140.00 USD | 3,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5990` | 1,900,000.00 USD | 1,900,000.00 USD | 23,710.00 USD | 2,170.00 USD | 17,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6000` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 1,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6005` | 852.06 USD | 44,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6010` | 1,280,000.00 USD | 1,280,000.00 USD | 735.24 USD | 461.96 USD | 15.46 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6010` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 796.28 USD | 4,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6020` | 1,280,000.00 USD | 1,280,000.00 USD | 7,230.00 USD | 4,200.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6030` | 1,260,000.00 USD | 1,260,000.00 USD | 5,150.00 USD | 2,940.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6030` | 1,850,000.00 USD | 1,850,000.00 USD | 7,780.00 USD | 8,040.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6040` | 1,250,000.00 USD | 1,250,000.00 USD | 6,990.00 USD | 2,320.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6045` | 527.44 USD | 43,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6050` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 1,750.00 USD | 2,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6050` | 1,830,000.00 USD | 1,830,000.00 USD | 5,730.00 USD | 3,100.00 USD | 7,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6060` | 1,240,000.00 USD | 1,240,000.00 USD | 8,500.00 USD | 606.70 USD | 4,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6070` | 1,220,000.00 USD | 1,220,000.00 USD | 7,700.00 USD | 1,030.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6070` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 65.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6080` | 1,210,000.00 USD | 1,210,000.00 USD | 2,970.00 USD | 0.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6085` | 455.69 USD | 43,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6090` | 1,200,000.00 USD | 1,200,000.00 USD | 6,430.00 USD | 0.00 USD | 47.82 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6090` | 1,820,000.00 USD | 1,820,000.00 USD | 16,780.00 USD | 0.00 USD | 8,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6100` | 1,200,000.00 USD | 1,200,000.00 USD | 3,960.00 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6105` | 6,090.00 USD | 43,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6110` | 1,190,000.00 USD | 1,190,000.00 USD | 1,430.00 USD | 0.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6110` | 1,790,000.00 USD | 1,790,000.00 USD | 7,480.00 USD | 4,780.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6120` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6130` | 1,180,000.00 USD | 1,180,000.00 USD | 2,140.00 USD | 596.50 USD | 1,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6130` | 1,770,000.00 USD | 1,770,000.00 USD | 10,980.00 USD | 4,560.00 USD | 9,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6140` | 1,180,000.00 USD | 1,180,000.00 USD | 6,120.00 USD | 0.00 USD | 1,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6150` | 1,170,000.00 USD | 1,170,000.00 USD | 2,730.00 USD | 0.00 USD | 30.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6150` | 1,740,000.00 USD | 1,740,000.00 USD | 15,680.00 USD | 12,870.00 USD | 9,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6160` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 1,270.00 USD | 126.06 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6170` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6170` | 1,700,000.00 USD | 1,700,000.00 USD | 15,050.00 USD | 5,120.00 USD | 18,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6190` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 126.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6190` | 1,660,000.00 USD | 1,660,000.00 USD | 17,170.00 USD | 3,130.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6195` | 3,170.00 USD | 36,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6200` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6210` | 1,160,000.00 USD | 1,160,000.00 USD | 1,990.00 USD | 0.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6210` | 1,630,000.00 USD | 1,630,000.00 USD | 18,630.00 USD | 7,090.00 USD | 11,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6220` | 1,160,000.00 USD | 1,160,000.00 USD | 2,520.00 USD | 0.00 USD | 60.30 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6230` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 1,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6230` | 1,590,000.00 USD | 1,590,000.00 USD | 17,730.00 USD | 7,010.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6235` | 3,250.00 USD | 33,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6240` | 1,150,000.00 USD | 1,150,000.00 USD | 3,220.00 USD | 3,780.00 USD | 76.16 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6250` | 1,150,000.00 USD | 1,150,000.00 USD | 1,800.00 USD | 2,050.00 USD | 113.26 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6250` | 1,530,000.00 USD | 1,530,000.00 USD | 34,730.00 USD | 8,550.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6255` | 286.65 USD | 30,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6260` | 1,140,000.00 USD | 1,140,000.00 USD | 8,920.00 USD | 2,330.00 USD | 10,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6265` | 10,530.00 USD | 30,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6270` | 1,120,000.00 USD | 1,120,000.00 USD | 3,700.00 USD | 3,940.00 USD | 12,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6270` | 1,480,000.00 USD | 1,480,000.00 USD | 38,350.00 USD | 15,860.00 USD | 50,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6280` | 1,100,000.00 USD | 1,100,000.00 USD | 11,690.00 USD | 463.43 USD | 2,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6290` | 1,090,000.00 USD | 1,090,000.00 USD | 11,890.00 USD | 1,200.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6290` | 1,370,000.00 USD | 1,370,000.00 USD | 26,870.00 USD | 15,960.00 USD | 26,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6300` | 1,070,000.00 USD | 1,070,000.00 USD | 12,950.00 USD | 3,790.00 USD | 3,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6310` | 1,050,000.00 USD | 1,050,000.00 USD | 12,360.00 USD | 6,080.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6310` | 1,300,000.00 USD | 1,300,000.00 USD | 29,380.00 USD | 12,400.00 USD | 28,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6315` | 1,010.00 USD | 19,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6320` | 1,020,000.00 USD | 1,020,000.00 USD | 33,310.00 USD | 10,600.00 USD | 14,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6330` | 958,240.00 USD | 958,240.00 USD | 17,300.00 USD | 3,580.00 USD | 19,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6330` | 1,230,000.00 USD | 1,230,000.00 USD | 92,050.00 USD | 27,360.00 USD | 57,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6340` | 918,260.00 USD | 918,260.00 USD | 21,990.00 USD | 2,600.00 USD | 17,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6350` | 876,060.00 USD | 876,060.00 USD | 51,360.00 USD | 9,480.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6350` | 1,060,000.00 USD | 1,060,000.00 USD | 45,040.00 USD | 5,850.00 USD | 27,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6360` | 807,160.00 USD | 807,160.00 USD | 50,620.00 USD | 10,760.00 USD | 37,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6370` | 708,360.00 USD | 708,360.00 USD | 26,310.00 USD | 6,240.00 USD | 30,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6370` | 977,920.00 USD | 977,920.00 USD | 123,570.00 USD | 12,170.00 USD | 66,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6375` | 5,900.00 USD | 18,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6380` | 645,700.00 USD | 645,700.00 USD | 36,240.00 USD | 7,180.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6385` | 582.30 USD | 12,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6390` | 597,050.00 USD | 597,050.00 USD | 18,790.00 USD | 3,690.00 USD | 24,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6390` | 776,040.00 USD | 776,040.00 USD | 28,340.00 USD | 11,380.00 USD | 43,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6400` | 550,370.00 USD | 550,370.00 USD | 9,830.00 USD | 9,970.00 USD | 26,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6410` | 503,840.00 USD | 503,840.00 USD | 20,930.00 USD | 1,480.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6410` | 692,890.00 USD | 692,890.00 USD | 15,560.00 USD | 0.00 USD | 6,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6415` | 4,740.00 USD | 12,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6420` | 473,990.00 USD | 473,990.00 USD | 43,840.00 USD | 13,850.00 USD | 12,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6430` | 403,670.00 USD | 403,670.00 USD | 35,700.00 USD | 13,440.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6430` | 670,690.00 USD | 670,690.00 USD | 71,550.00 USD | 33,700.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6435` | 3,450.00 USD | 7,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6440` | 340,800.00 USD | 340,800.00 USD | 39,760.00 USD | 16,890.00 USD | 27,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6450` | 256,440.00 USD | 256,440.00 USD | 70,250.00 USD | 22,940.00 USD | 36,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6450` | 552,040.00 USD | 552,040.00 USD | 109,710.00 USD | 33,240.00 USD | 50,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6455` | 3,730.00 USD | 3,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6460` | 126,610.00 USD | 126,610.00 USD | 57,400.00 USD | 12,380.00 USD | 56,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6470` | 123,240.00 USD | 123,240.00 USD | 69,180.00 USD | 7,780.00 USD | 46,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6470` | 246,480.00 USD | 246,480.00 USD | 69,180.00 USD | 7,780.00 USD | 46,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6470` | 358,640.00 USD | 358,640.00 USD | 101,050.00 USD | 18,180.00 USD | 84,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6480` | 374,390.00 USD | 374,390.00 USD | 112,500.00 USD | 0.00 USD | 15,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6485` | 259.68 USD | 259.68 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6490` | 435,160.00 USD | 435,160.00 USD | 60,640.00 USD | 0.00 USD | 132.01 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6490` | 154,540.00 USD | 154,540.00 USD | 113,110.00 USD | 0.00 USD | 41,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6500` | 500,120.00 USD | 500,120.00 USD | 64,920.00 USD | 0.00 USD | 44.56 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6510` | 533,350.00 USD | 533,350.00 USD | 33,120.00 USD | 0.00 USD | 117.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6510` | 339,420.00 USD | 339,420.00 USD | 202,260.00 USD | 4,190.00 USD | 132,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6520` | 603,230.00 USD | 603,230.00 USD | 69,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6530` | 609,010.00 USD | 609,010.00 USD | 5,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6530` | 526,420.00 USD | 526,420.00 USD | 46,620.00 USD | 6,720.00 USD | 133,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6540` | 631,020.00 USD | 631,020.00 USD | 11,450.00 USD | 0.00 USD | 10,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6550` | 557,200.00 USD | 557,200.00 USD | 15,730.00 USD | 0.00 USD | 15,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6570` | 569,470.00 USD | 569,470.00 USD | 0.00 USD | 11,730.00 USD | 538.23 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6590` | 631,120.00 USD | 631,120.00 USD | 0.00 USD | 0.00 USD | 98.76 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6590` | 591,900.00 USD | 591,900.00 USD | 0.00 USD | 21,920.00 USD | 504.55 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6610` | 631,270.00 USD | 631,270.00 USD | 0.00 USD | 0.00 USD | 150.77 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6610` | 596,330.00 USD | 596,330.00 USD | 0.00 USD | 4,180.00 USD | 249.08 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6620` | 631,330.00 USD | 631,330.00 USD | 0.00 USD | 0.00 USD | 59.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6630` | 631,370.00 USD | 631,370.00 USD | 0.00 USD | 0.00 USD | 41.69 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6630` | 596,710.00 USD | 596,710.00 USD | 0.00 USD | 0.00 USD | 382.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6640` | 631,430.00 USD | 631,430.00 USD | 0.00 USD | 0.00 USD | 59.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6650` | 652,000.00 USD | 652,000.00 USD | 0.00 USD | 3,160.00 USD | 17,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6650` | 604,050.00 USD | 604,050.00 USD | 0.00 USD | 6,770.00 USD | 568.33 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6660` | 657,420.00 USD | 657,420.00 USD | 0.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6670` | 676,280.00 USD | 676,280.00 USD | 18,850.00 USD | 0.00 USD | 17.74 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6670` | 604,510.00 USD | 604,510.00 USD | 0.00 USD | 0.00 USD | 456.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6690` | 684,220.00 USD | 684,220.00 USD | 0.00 USD | 3,550.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6690` | 604,810.00 USD | 604,810.00 USD | 0.00 USD | 0.00 USD | 301.75 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6700` | 719,550.00 USD | 719,550.00 USD | 8,830.00 USD | 1,920.00 USD | 24,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6710` | 761,520.00 USD | 761,520.00 USD | 41,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6710` | 693,740.00 USD | 693,740.00 USD | 58,470.00 USD | 0.00 USD | 30,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6720` | 761,530.00 USD | 761,530.00 USD | 0.00 USD | 0.00 USD | 3.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6730` | 791,510.00 USD | 791,510.00 USD | 24,320.00 USD | 1,170.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6730` | 693,840.00 USD | 693,840.00 USD | 0.00 USD | 0.00 USD | 99.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6740` | 872,940.00 USD | 872,940.00 USD | 64,370.00 USD | 7,120.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6750` | 915,870.00 USD | 915,870.00 USD | 28,700.00 USD | 5,970.00 USD | 8,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6750` | 809,290.00 USD | 809,290.00 USD | 39,730.00 USD | 75,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6760` | 933,570.00 USD | 933,570.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6770` | 968,510.00 USD | 968,510.00 USD | 14,540.00 USD | 6,110.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6770` | 930,350.00 USD | 930,350.00 USD | 63,600.00 USD | 6,430.00 USD | 51,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6780` | 1,030,000.00 USD | 1,030,000.00 USD | 33,610.00 USD | 14,220.00 USD | 8,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6790` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 18,610.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6790` | 957,160.00 USD | 957,160.00 USD | 0.00 USD | 26,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6800` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6810` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6810` | 972,870.00 USD | 972,870.00 USD | 0.00 USD | 15,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6820` | 1,110,000.00 USD | 1,110,000.00 USD | 22,600.00 USD | 13,770.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6830` | 1,200,000.00 USD | 1,200,000.00 USD | 24,570.00 USD | 26,060.00 USD | 35,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6830` | 1,100,000.00 USD | 1,100,000.00 USD | 32,570.00 USD | 48,750.00 USD | 48,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6840` | 1,280,000.00 USD | 1,280,000.00 USD | 45,780.00 USD | 24,170.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6850` | 1,350,000.00 USD | 1,350,000.00 USD | 51,090.00 USD | 5,780.00 USD | 10,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6850` | 1,280,000.00 USD | 1,280,000.00 USD | 75,160.00 USD | 41,290.00 USD | 64,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6860` | 1,400,000.00 USD | 1,400,000.00 USD | 40,250.00 USD | 4,380.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6870` | 1,470,000.00 USD | 1,470,000.00 USD | 63,220.00 USD | 1,160.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6870` | 1,350,000.00 USD | 1,350,000.00 USD | 52,530.00 USD | 9,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6880` | 1,530,000.00 USD | 1,530,000.00 USD | 14,350.00 USD | 9,600.00 USD | 32,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6890` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 2,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6890` | 1,390,000.00 USD | 1,390,000.00 USD | 18,170.00 USD | 28,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6900` | 1,570,000.00 USD | 1,570,000.00 USD | 14,580.00 USD | 1,610.00 USD | 21,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6910` | 1,640,000.00 USD | 1,640,000.00 USD | 28,860.00 USD | 1,730.00 USD | 39,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6910` | 1,520,000.00 USD | 1,520,000.00 USD | 69,620.00 USD | 6,570.00 USD | 54,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6920` | 1,670,000.00 USD | 1,670,000.00 USD | 16,800.00 USD | 0.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6930` | 1,680,000.00 USD | 1,680,000.00 USD | 10,030.00 USD | 0.00 USD | 168.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6930` | 1,600,000.00 USD | 1,600,000.00 USD | 14,220.00 USD | 0.00 USD | 66,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6940` | 1,700,000.00 USD | 1,700,000.00 USD | 11,230.00 USD | 4,420.00 USD | 9,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6950` | 1,740,000.00 USD | 1,740,000.00 USD | 22,480.00 USD | 4,460.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6950` | 1,650,000.00 USD | 1,650,000.00 USD | 31,450.00 USD | 0.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6960` | 1,800,000.00 USD | 1,800,000.00 USD | 58,370.00 USD | 6,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6970` | 1,840,000.00 USD | 1,840,000.00 USD | 33,460.00 USD | 2,430.00 USD | 34.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6970` | 1,700,000.00 USD | 1,700,000.00 USD | 50,160.00 USD | 3,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6980` | 1,850,000.00 USD | 1,850,000.00 USD | 9,140.00 USD | 4,100.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6990` | 1,870,000.00 USD | 1,870,000.00 USD | 5,180.00 USD | 4,830.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6990` | 1,770,000.00 USD | 1,770,000.00 USD | 27,730.00 USD | 10,960.00 USD | 30,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7000` | 1,900,000.00 USD | 1,900,000.00 USD | 18,240.00 USD | 4,020.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7010` | 1,920,000.00 USD | 1,920,000.00 USD | 15,520.00 USD | 0.00 USD | 73.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7010` | 1,800,000.00 USD | 1,800,000.00 USD | 16,330.00 USD | 0.00 USD | 10,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7020` | 1,930,000.00 USD | 1,930,000.00 USD | 14,360.00 USD | 0.00 USD | 22.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7030` | 1,950,000.00 USD | 1,950,000.00 USD | 4,330.00 USD | 0.00 USD | 10,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7030` | 1,990,000.00 USD | 1,990,000.00 USD | 92,960.00 USD | 0.00 USD | 103,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7040` | 2,000,000.00 USD | 2,000,000.00 USD | 29,930.00 USD | 2,630.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7050` | 2,050,000.00 USD | 2,050,000.00 USD | 29,790.00 USD | 2,660.00 USD | 18,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7050` | 2,210,000.00 USD | 2,210,000.00 USD | 46,540.00 USD | 0.00 USD | 169,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7060` | 2,080,000.00 USD | 2,080,000.00 USD | 8,590.00 USD | 3,860.00 USD | 12,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7070` | 2,130,000.00 USD | 2,130,000.00 USD | 19,980.00 USD | 21,860.00 USD | 17,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7070` | 2,390,000.00 USD | 2,390,000.00 USD | 28,920.00 USD | 69,790.00 USD | 83,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7075` | 2,220.00 USD | 2,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7080` | 2,160,000.00 USD | 2,160,000.00 USD | 18,420.00 USD | 3,500.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7090` | 2,190,000.00 USD | 2,190,000.00 USD | 17,580.00 USD | 3,160.00 USD | 8,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7090` | 2,760,000.00 USD | 2,760,000.00 USD | 121,730.00 USD | 61,400.00 USD | 188,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7100` | 2,210,000.00 USD | 2,210,000.00 USD | 8,730.00 USD | 1,280.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7110` | 2,230,000.00 USD | 2,230,000.00 USD | 2,660.00 USD | 8,760.00 USD | 8,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7110` | 3,020,000.00 USD | 3,020,000.00 USD | 85,130.00 USD | 64,110.00 USD | 107,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7120` | 2,270,000.00 USD | 2,270,000.00 USD | 21,700.00 USD | 4,410.00 USD | 15,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7130` | 2,330,000.00 USD | 2,330,000.00 USD | 22,890.00 USD | 3,110.00 USD | 32,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7130` | 3,420,000.00 USD | 3,420,000.00 USD | 135,980.00 USD | 77,290.00 USD | 186,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7140` | 2,360,000.00 USD | 2,360,000.00 USD | 24,010.00 USD | 5,910.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7150` | 2,410,000.00 USD | 2,410,000.00 USD | 18,260.00 USD | 6,980.00 USD | 23,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7150` | 3,840,000.00 USD | 3,840,000.00 USD | 177,760.00 USD | 62,090.00 USD | 178,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7160` | 2,450,000.00 USD | 2,450,000.00 USD | 17,400.00 USD | 11,180.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7170` | 2,470,000.00 USD | 2,470,000.00 USD | 4,910.00 USD | 4,510.00 USD | 12,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7170` | 4,200,000.00 USD | 4,200,000.00 USD | 168,460.00 USD | 74,260.00 USD | 121,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7180` | 2,500,000.00 USD | 2,500,000.00 USD | 6,240.00 USD | 2,890.00 USD | 14,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7190` | 2,520,000.00 USD | 2,520,000.00 USD | 12,780.00 USD | 5,680.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7190` | 4,420,000.00 USD | 4,420,000.00 USD | 88,650.00 USD | 32,980.00 USD | 100,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7200` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 4,740.00 USD | 9,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7210` | 2,560,000.00 USD | 2,560,000.00 USD | 10,550.00 USD | 13,350.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7210` | 4,910,000.00 USD | 4,910,000.00 USD | 271,310.00 USD | 58,030.00 USD | 160,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7220` | 2,570,000.00 USD | 2,570,000.00 USD | 6,730.00 USD | 4,320.00 USD | 885.59 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7230` | 2,590,000.00 USD | 2,590,000.00 USD | 1,140.00 USD | 3,060.00 USD | 7,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7230` | 5,260,000.00 USD | 5,260,000.00 USD | 171,240.00 USD | 52,810.00 USD | 121,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7240` | 2,600,000.00 USD | 2,600,000.00 USD | 11,320.00 USD | 3,290.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7250` | 2,620,000.00 USD | 2,620,000.00 USD | 4,760.00 USD | 3,950.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7250` | 5,560,000.00 USD | 5,560,000.00 USD | 139,330.00 USD | 40,040.00 USD | 117,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7255` | 43,950.00 USD | 46,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7260` | 2,650,000.00 USD | 2,650,000.00 USD | 16,740.00 USD | 2,210.00 USD | 12,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7270` | 2,700,000.00 USD | 2,700,000.00 USD | 29,920.00 USD | 3,230.00 USD | 12,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7270` | 5,840,000.00 USD | 5,840,000.00 USD | 111,330.00 USD | 44,700.00 USD | 126,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7280` | 2,730,000.00 USD | 2,730,000.00 USD | 20,470.00 USD | 3,050.00 USD | 9,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7290` | 2,770,000.00 USD | 2,770,000.00 USD | 13,150.00 USD | 6,310.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7290` | 6,110,000.00 USD | 6,110,000.00 USD | 89,770.00 USD | 54,440.00 USD | 126,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7300` | 2,800,000.00 USD | 2,800,000.00 USD | 9,980.00 USD | 7,000.00 USD | 16,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7310` | 2,810,000.00 USD | 2,810,000.00 USD | 1,010.00 USD | 1,670.00 USD | 2,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7310` | 6,430,000.00 USD | 6,430,000.00 USD | 183,580.00 USD | 68,560.00 USD | 64,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7320` | 2,820,000.00 USD | 2,820,000.00 USD | 12,500.00 USD | 1,140.00 USD | 3,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7330` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 2,180.00 USD | 2,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7330` | 6,610,000.00 USD | 6,610,000.00 USD | 74,380.00 USD | 25,020.00 USD | 81,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7340` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 1,530.00 USD | 3,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7345` | 150.17 USD | 46,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7350` | 2,830,000.00 USD | 2,830,000.00 USD | 735.24 USD | 1,470.00 USD | 40.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7350` | 6,780,000.00 USD | 6,780,000.00 USD | 97,650.00 USD | 24,440.00 USD | 46,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7360` | 2,850,000.00 USD | 2,850,000.00 USD | 7,230.00 USD | 5,360.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7370` | 2,860,000.00 USD | 2,860,000.00 USD | 5,150.00 USD | 2,940.00 USD | 3,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7370` | 6,900,000.00 USD | 6,900,000.00 USD | 46,860.00 USD | 34,840.00 USD | 40,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7380` | 2,870,000.00 USD | 2,870,000.00 USD | 6,990.00 USD | 2,320.00 USD | 1,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7390` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 2,330.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7390` | 7,050,000.00 USD | 7,050,000.00 USD | 64,070.00 USD | 21,590.00 USD | 65,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7400` | 2,890,000.00 USD | 2,890,000.00 USD | 8,500.00 USD | 606.70 USD | 4,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7410` | 2,910,000.00 USD | 2,910,000.00 USD | 7,700.00 USD | 1,030.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7410` | 7,160,000.00 USD | 7,160,000.00 USD | 30,110.00 USD | 36,600.00 USD | 42,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7420` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 3.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7430` | 2,910,000.00 USD | 2,910,000.00 USD | 1,240.00 USD | 0.00 USD | 125.56 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7430` | 7,290,000.00 USD | 7,290,000.00 USD | 53,760.00 USD | 27,390.00 USD | 55,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7440` | 2,910,000.00 USD | 2,910,000.00 USD | 1,730.00 USD | 0.00 USD | 4,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7450` | 7,470,000.00 USD | 7,470,000.00 USD | 78,270.00 USD | 42,280.00 USD | 54,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7470` | 7,620,000.00 USD | 7,620,000.00 USD | 74,280.00 USD | 28,960.00 USD | 47,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7490` | 7,690,000.00 USD | 7,690,000.00 USD | 42,220.00 USD | 15,480.00 USD | 13,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7510` | 7,820,000.00 USD | 7,820,000.00 USD | 60,950.00 USD | 13,310.00 USD | 51,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7530` | 7,900,000.00 USD | 7,900,000.00 USD | 48,850.00 USD | 9,020.00 USD | 29,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7550` | 7,970,000.00 USD | 7,970,000.00 USD | 27,450.00 USD | 6,470.00 USD | 30,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7570` | 8,050,000.00 USD | 8,050,000.00 USD | 36,750.00 USD | 5,360.00 USD | 36,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7590` | 8,160,000.00 USD | 8,160,000.00 USD | 61,250.00 USD | 8,240.00 USD | 45,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7610` | 8,270,000.00 USD | 8,270,000.00 USD | 36,150.00 USD | 12,300.00 USD | 64,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7630` | 8,400,000.00 USD | 8,400,000.00 USD | 73,980.00 USD | 28,990.00 USD | 27,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7635` | 143.11 USD | 46,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7650` | 8,570,000.00 USD | 8,570,000.00 USD | 59,460.00 USD | 9,740.00 USD | 98,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7670` | 8,680,000.00 USD | 8,680,000.00 USD | 45,270.00 USD | 25,520.00 USD | 35,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7690` | 8,760,000.00 USD | 8,760,000.00 USD | 39,720.00 USD | 18,230.00 USD | 26,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7710` | 8,900,000.00 USD | 8,900,000.00 USD | 59,050.00 USD | 29,000.00 USD | 48,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7725` | 165.62 USD | 46,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7730` | 8,990,000.00 USD | 8,990,000.00 USD | 42,000.00 USD | 27,790.00 USD | 21,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7750` | 9,050,000.00 USD | 9,050,000.00 USD | 19,570.00 USD | 11,130.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7765` | 330.78 USD | 46,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7770` | 9,150,000.00 USD | 9,150,000.00 USD | 48,840.00 USD | 18,920.00 USD | 24,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7790` | 9,250,000.00 USD | 9,250,000.00 USD | 64,380.00 USD | 7,690.00 USD | 36,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7810` | 9,430,000.00 USD | 9,430,000.00 USD | 99,040.00 USD | 24,320.00 USD | 57,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7830` | 9,570,000.00 USD | 9,570,000.00 USD | 110,720.00 USD | 18,940.00 USD | 8,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7850` | 9,690,000.00 USD | 9,690,000.00 USD | 38,200.00 USD | 15,730.00 USD | 63,610.00 USD | `Tier 1 CEX` |
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
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.5770` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 2,150.00 USD | 0.00 USD | 26.97 USD |
| `7D` | `0.5790` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 1,610.00 USD | 0.00 USD | 4,410.00 USD |
| `7D` | `0.5810` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 3,100.00 USD |
| `7D` | `0.5830` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD |
| `1D` | `0.5860` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 0.00 USD | 658.88 USD | 0.00 USD |
| `1D` | `0.5870` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 2,890.00 USD | 631.19 USD | 3,500.00 USD |
| `7D` | `0.5870` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 0.00 USD | 1,400.00 USD | 65.70 USD |
| `1D` | `0.5880` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 1,270.00 USD | 1,580.00 USD | 3,620.00 USD |
| `1D` | `0.5890` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 3,460.00 USD | 0.00 USD | 7.65 USD |
| `7D` | `0.5890` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 3,110.00 USD | 0.00 USD | 15.37 USD |
| `1D` | `0.5900` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 4,730.00 USD | 1,390.00 USD | 3.61 USD |
| `1D` | `0.5910` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | 1,820.00 USD | 4,100.00 USD |
| `7D` | `0.5910` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 3,120.00 USD | 1,560.00 USD | 0.00 USD |
| `1D` | `0.5920` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 11,320.00 USD | 2,650.00 USD | 1,190.00 USD |
| `1D` | `0.5930` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 3,420.00 USD | 0.00 USD | 5,760.00 USD |
| `7D` | `0.5930` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 21,790.00 USD | 2,820.00 USD | 15,810.00 USD |
| `1D` | `0.5940` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 5,890.00 USD | 0.00 USD | 4,450.00 USD |
| `1D` | `0.5950` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 19,520.00 USD | 2,470.00 USD | 1,900.00 USD |
| `7D` | `0.5950` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 13,060.00 USD | 0.00 USD | 4,530.00 USD |
| `1D` | `0.5960` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 8,460.00 USD | 456.46 USD | 6,230.00 USD |
| `1D` | `0.5970` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 4,020.00 USD | 2,820.00 USD | 4,420.00 USD |
| `7D` | `0.5970` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 5,120.00 USD | 1,640.00 USD | 16,380.00 USD |
| `1D` | `0.5980` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 6,400.00 USD | 1,740.00 USD | 11,190.00 USD |
| `1D` | `0.5990` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 12,500.00 USD | 1,140.00 USD | 3,840.00 USD |
| `7D` | `0.5990` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 23,710.00 USD | 2,170.00 USD | 17,690.00 USD |
| `1D` | `0.6000` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 1,130.00 USD |
| `1D` | `0.6010` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 735.24 USD | 461.96 USD | 15.46 USD |
| `7D` | `0.6010` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 0.00 USD | 796.28 USD | 4,750.00 USD |
| `1D` | `0.6020` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 7,230.00 USD | 4,200.00 USD | 3,710.00 USD |
| `1D` | `0.6030` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 5,150.00 USD | 2,940.00 USD | 3,710.00 USD |
| `7D` | `0.6030` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 7,780.00 USD | 8,040.00 USD | 4,010.00 USD |
| `1D` | `0.6040` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 6,990.00 USD | 2,320.00 USD | 1,880.00 USD |
| `1D` | `0.6050` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 1,750.00 USD | 2,160.00 USD |
| `7D` | `0.6050` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 5,730.00 USD | 3,100.00 USD | 7,920.00 USD |
| `1D` | `0.6060` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 8,500.00 USD | 606.70 USD | 4,740.00 USD |
| `1D` | `0.6070` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 7,700.00 USD | 1,030.00 USD | 4,740.00 USD |
| `7D` | `0.6070` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 65.64 USD |
| `1D` | `0.6080` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 2,970.00 USD | 0.00 USD | 4,010.00 USD |
| `1D` | `0.6090` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 6,430.00 USD | 0.00 USD | 47.82 USD |
| `7D` | `0.6090` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 16,780.00 USD | 0.00 USD | 8,490.00 USD |
| `1D` | `0.6100` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 3,960.00 USD | 0.00 USD | 5,750.00 USD |
| `1D` | `0.6110` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 1,430.00 USD | 0.00 USD | 1,110.00 USD |
| `7D` | `0.6110` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 7,480.00 USD | 4,780.00 USD | 12,860.00 USD |
| `1D` | `0.6120` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD |
| `1D` | `0.6130` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 2,140.00 USD | 596.50 USD | 1,020.00 USD |
| `7D` | `0.6130` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 10,980.00 USD | 4,560.00 USD | 9,770.00 USD |
| `1D` | `0.6140` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 6,120.00 USD | 0.00 USD | 1,000.00 USD |
| `1D` | `0.6150` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 2,730.00 USD | 0.00 USD | 30.06 USD |
| `7D` | `0.6150` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 15,680.00 USD | 12,870.00 USD | 9,450.00 USD |
| `1D` | `0.6160` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 1,270.00 USD | 126.06 USD |
| `1D` | `0.6170` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 3,480.00 USD |
| `7D` | `0.6170` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 15,050.00 USD | 5,120.00 USD | 18,460.00 USD |
| `1D` | `0.6190` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 126.86 USD |
| `7D` | `0.6190` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 17,170.00 USD | 3,130.00 USD | 13,980.00 USD |
| `1D` | `0.6200` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD |
| `1D` | `0.6210` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 1,990.00 USD | 0.00 USD | 2,070.00 USD |
| `7D` | `0.6210` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 18,630.00 USD | 7,090.00 USD | 11,280.00 USD |
| `1D` | `0.6220` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 2,520.00 USD | 0.00 USD | 60.30 USD |
| `1D` | `0.6230` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 1,100.00 USD |
| `7D` | `0.6230` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 17,730.00 USD | 7,010.00 USD | 38,270.00 USD |
| `1D` | `0.6240` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 3,220.00 USD | 3,780.00 USD | 76.16 USD |
| `1D` | `0.6250` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 1,800.00 USD | 2,050.00 USD | 113.26 USD |
| `7D` | `0.6250` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 34,730.00 USD | 8,550.00 USD | 7,460.00 USD |
| `1D` | `0.6260` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 8,920.00 USD | 2,330.00 USD | 10,770.00 USD |
| `1D` | `0.6270` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 3,700.00 USD | 3,940.00 USD | 12,850.00 USD |
| `7D` | `0.6270` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 38,350.00 USD | 15,860.00 USD | 50,630.00 USD |
| `1D` | `0.6280` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 11,690.00 USD | 463.43 USD | 2,070.00 USD |
| `1D` | `0.6290` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 11,890.00 USD | 1,200.00 USD | 3,750.00 USD |
| `7D` | `0.6290` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 26,870.00 USD | 15,960.00 USD | 26,850.00 USD |
| `1D` | `0.6300` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 12,950.00 USD | 3,790.00 USD | 3,640.00 USD |
| `1D` | `0.6310` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 12,360.00 USD | 6,080.00 USD | 14,390.00 USD |
| `7D` | `0.6310` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 29,380.00 USD | 12,400.00 USD | 28,520.00 USD |
| `1D` | `0.6320` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 33,310.00 USD | 10,600.00 USD | 14,850.00 USD |
| `1D` | `0.6330` | 958,240.00 USD | 0.00 USD | 958,240.00 USD | 17,300.00 USD | 3,580.00 USD | 19,110.00 USD |
| `7D` | `0.6330` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 92,050.00 USD | 27,360.00 USD | 57,650.00 USD |
| `1D` | `0.6340` | 918,260.00 USD | 0.00 USD | 918,260.00 USD | 21,990.00 USD | 2,600.00 USD | 17,600.00 USD |
| `1D` | `0.6350` | 876,060.00 USD | 0.00 USD | 876,060.00 USD | 51,360.00 USD | 9,480.00 USD | 8,060.00 USD |
| `7D` | `0.6350` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 45,040.00 USD | 5,850.00 USD | 27,680.00 USD |
| `1D` | `0.6360` | 807,160.00 USD | 0.00 USD | 807,160.00 USD | 50,620.00 USD | 10,760.00 USD | 37,420.00 USD |
| `1D` | `0.6370` | 708,360.00 USD | 0.00 USD | 708,360.00 USD | 26,310.00 USD | 6,240.00 USD | 30,110.00 USD |
| `7D` | `0.6370` | 977,920.00 USD | 0.00 USD | 977,920.00 USD | 123,570.00 USD | 12,170.00 USD | 66,140.00 USD |
| `1D` | `0.6380` | 645,700.00 USD | 0.00 USD | 645,700.00 USD | 36,240.00 USD | 7,180.00 USD | 5,230.00 USD |
| `1D` | `0.6390` | 597,050.00 USD | 0.00 USD | 597,050.00 USD | 18,790.00 USD | 3,690.00 USD | 24,220.00 USD |
| `7D` | `0.6390` | 776,040.00 USD | 0.00 USD | 776,040.00 USD | 28,340.00 USD | 11,380.00 USD | 43,430.00 USD |
| `1D` | `0.6400` | 550,370.00 USD | 0.00 USD | 550,370.00 USD | 9,830.00 USD | 9,970.00 USD | 26,730.00 USD |
| `1D` | `0.6410` | 503,840.00 USD | 0.00 USD | 503,840.00 USD | 20,930.00 USD | 1,480.00 USD | 7,440.00 USD |
| `7D` | `0.6410` | 692,890.00 USD | 0.00 USD | 692,890.00 USD | 15,560.00 USD | 0.00 USD | 6,650.00 USD |
| `1D` | `0.6420` | 473,990.00 USD | 0.00 USD | 473,990.00 USD | 43,840.00 USD | 13,850.00 USD | 12,640.00 USD |
| `1D` | `0.6430` | 403,670.00 USD | 0.00 USD | 403,670.00 USD | 35,700.00 USD | 13,440.00 USD | 13,730.00 USD |
| `7D` | `0.6430` | 670,690.00 USD | 0.00 USD | 670,690.00 USD | 71,550.00 USD | 33,700.00 USD | 13,390.00 USD |
| `1D` | `0.6440` | 340,800.00 USD | 0.00 USD | 340,800.00 USD | 39,760.00 USD | 16,890.00 USD | 27,720.00 USD |
| `1D` | `0.6450` | 256,440.00 USD | 0.00 USD | 256,440.00 USD | 70,250.00 USD | 22,940.00 USD | 36,640.00 USD |
| `7D` | `0.6450` | 552,040.00 USD | 0.00 USD | 552,040.00 USD | 109,710.00 USD | 33,240.00 USD | 50,450.00 USD |
| `1D` | `0.6460` | 126,610.00 USD | 0.00 USD | 126,610.00 USD | 57,400.00 USD | 12,380.00 USD | 56,830.00 USD |
| `1D` | `0.6470` | 123,240.00 USD | 123,240.00 USD | 0.00 USD | 69,180.00 USD | 7,780.00 USD | 46,280.00 USD |
| `1D` | `0.6470` | 246,480.00 USD | 246,480.00 USD | 0.00 USD | 69,180.00 USD | 7,780.00 USD | 46,280.00 USD |
| `7D` | `0.6470` | 358,640.00 USD | 0.00 USD | 358,640.00 USD | 101,050.00 USD | 18,180.00 USD | 84,860.00 USD |
| `1D` | `0.6480` | 374,390.00 USD | 374,390.00 USD | 0.00 USD | 112,500.00 USD | 0.00 USD | 15,410.00 USD |
| `1D` | `0.6490` | 435,160.00 USD | 435,160.00 USD | 0.00 USD | 60,640.00 USD | 0.00 USD | 132.01 USD |
| `7D` | `0.6490` | 154,540.00 USD | 0.00 USD | 154,540.00 USD | 113,110.00 USD | 0.00 USD | 41,430.00 USD |
| `1D` | `0.6500` | 500,120.00 USD | 500,120.00 USD | 0.00 USD | 64,920.00 USD | 0.00 USD | 44.56 USD |
| `7D` | `0.6500` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6510` | 533,350.00 USD | 533,350.00 USD | 0.00 USD | 33,120.00 USD | 0.00 USD | 117.48 USD |
| `7D` | `0.6510` | 339,420.00 USD | 339,420.00 USD | 0.00 USD | 202,260.00 USD | 4,190.00 USD | 132,970.00 USD |
| `1D` | `0.6520` | 603,230.00 USD | 603,230.00 USD | 0.00 USD | 69,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6530` | 609,010.00 USD | 609,010.00 USD | 0.00 USD | 5,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6530` | 526,420.00 USD | 526,420.00 USD | 0.00 USD | 46,620.00 USD | 6,720.00 USD | 133,660.00 USD |
| `1D` | `0.6540` | 631,020.00 USD | 631,020.00 USD | 0.00 USD | 11,450.00 USD | 0.00 USD | 10,560.00 USD |
| `7D` | `0.6550` | 557,200.00 USD | 557,200.00 USD | 0.00 USD | 15,730.00 USD | 0.00 USD | 15,060.00 USD |
| `7D` | `0.6570` | 569,470.00 USD | 569,470.00 USD | 0.00 USD | 0.00 USD | 11,730.00 USD | 538.23 USD |
| `1D` | `0.6590` | 631,120.00 USD | 631,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 98.76 USD |
| `7D` | `0.6590` | 591,900.00 USD | 591,900.00 USD | 0.00 USD | 0.00 USD | 21,920.00 USD | 504.55 USD |
| `1D` | `0.6610` | 631,270.00 USD | 631,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 150.77 USD |
| `7D` | `0.6610` | 596,330.00 USD | 596,330.00 USD | 0.00 USD | 0.00 USD | 4,180.00 USD | 249.08 USD |
| `1D` | `0.6620` | 631,330.00 USD | 631,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 59.44 USD |
| `1D` | `0.6630` | 631,370.00 USD | 631,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 41.69 USD |
| `7D` | `0.6630` | 596,710.00 USD | 596,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 382.86 USD |
| `1D` | `0.6640` | 631,430.00 USD | 631,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 59.42 USD |
| `1D` | `0.6650` | 652,000.00 USD | 652,000.00 USD | 0.00 USD | 0.00 USD | 3,160.00 USD | 17,420.00 USD |
| `7D` | `0.6650` | 604,050.00 USD | 604,050.00 USD | 0.00 USD | 0.00 USD | 6,770.00 USD | 568.33 USD |
| `1D` | `0.6660` | 657,420.00 USD | 657,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,410.00 USD |
| `1D` | `0.6670` | 676,280.00 USD | 676,280.00 USD | 0.00 USD | 18,850.00 USD | 0.00 USD | 17.74 USD |
| `7D` | `0.6670` | 604,510.00 USD | 604,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 456.36 USD |
| `1D` | `0.6690` | 684,220.00 USD | 684,220.00 USD | 0.00 USD | 0.00 USD | 3,550.00 USD | 4,390.00 USD |
| `7D` | `0.6690` | 604,810.00 USD | 604,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 301.75 USD |
| `1D` | `0.6700` | 719,550.00 USD | 719,550.00 USD | 0.00 USD | 8,830.00 USD | 1,920.00 USD | 24,570.00 USD |
| `1D` | `0.6710` | 761,520.00 USD | 761,520.00 USD | 0.00 USD | 41,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6710` | 693,740.00 USD | 693,740.00 USD | 0.00 USD | 58,470.00 USD | 0.00 USD | 30,460.00 USD |
| `1D` | `0.6720` | 761,530.00 USD | 761,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.80 USD |
| `1D` | `0.6730` | 791,510.00 USD | 791,510.00 USD | 0.00 USD | 24,320.00 USD | 1,170.00 USD | 4,490.00 USD |
| `7D` | `0.6730` | 693,840.00 USD | 693,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 99.42 USD |
| `1D` | `0.6740` | 872,940.00 USD | 872,940.00 USD | 0.00 USD | 64,370.00 USD | 7,120.00 USD | 9,950.00 USD |
| `1D` | `0.6750` | 915,870.00 USD | 915,870.00 USD | 0.00 USD | 28,700.00 USD | 5,970.00 USD | 8,250.00 USD |
| `7D` | `0.6750` | 809,290.00 USD | 809,290.00 USD | 0.00 USD | 39,730.00 USD | 75,730.00 USD | 0.00 USD |
| `1D` | `0.6760` | 933,570.00 USD | 933,570.00 USD | 0.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD |
| `1D` | `0.6770` | 968,510.00 USD | 968,510.00 USD | 0.00 USD | 14,540.00 USD | 6,110.00 USD | 14,290.00 USD |
| `7D` | `0.6770` | 930,350.00 USD | 930,350.00 USD | 0.00 USD | 63,600.00 USD | 6,430.00 USD | 51,030.00 USD |
| `1D` | `0.6780` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 33,610.00 USD | 14,220.00 USD | 8,710.00 USD |
| `1D` | `0.6790` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 18,610.00 USD | 14,200.00 USD |
| `7D` | `0.6790` | 957,160.00 USD | 957,160.00 USD | 0.00 USD | 0.00 USD | 26,810.00 USD | 0.00 USD |
| `1D` | `0.6800` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,450.00 USD |
| `1D` | `0.6810` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,590.00 USD |
| `7D` | `0.6810` | 972,870.00 USD | 972,870.00 USD | 0.00 USD | 0.00 USD | 15,720.00 USD | 0.00 USD |
| `1D` | `0.6820` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 22,600.00 USD | 13,770.00 USD | 7,110.00 USD |
| `1D` | `0.6830` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 24,570.00 USD | 26,060.00 USD | 35,880.00 USD |
| `7D` | `0.6830` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 32,570.00 USD | 48,750.00 USD | 48,260.00 USD |
| `1D` | `0.6840` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 45,780.00 USD | 24,170.00 USD | 10,920.00 USD |
| `1D` | `0.6850` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 51,090.00 USD | 5,780.00 USD | 10,620.00 USD |
| `7D` | `0.6850` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 75,160.00 USD | 41,290.00 USD | 64,650.00 USD |
| `1D` | `0.6860` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 40,250.00 USD | 4,380.00 USD | 12,600.00 USD |
| `1D` | `0.6870` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 63,220.00 USD | 1,160.00 USD | 3,830.00 USD |
| `7D` | `0.6870` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 52,530.00 USD | 9,830.00 USD | 0.00 USD |
| `1D` | `0.6880` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 14,350.00 USD | 9,600.00 USD | 32,960.00 USD |
| `1D` | `0.6890` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,750.00 USD |
| `7D` | `0.6890` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 18,170.00 USD | 28,330.00 USD | 0.00 USD |
| `1D` | `0.6900` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 14,580.00 USD | 1,610.00 USD | 21,050.00 USD |
| `1D` | `0.6910` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 28,860.00 USD | 1,730.00 USD | 39,760.00 USD |
| `7D` | `0.6910` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 69,620.00 USD | 6,570.00 USD | 54,200.00 USD |
| `1D` | `0.6920` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 16,800.00 USD | 0.00 USD | 13,680.00 USD |
| `1D` | `0.6930` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 10,030.00 USD | 0.00 USD | 168.16 USD |
| `7D` | `0.6930` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 14,220.00 USD | 0.00 USD | 66,970.00 USD |
| `1D` | `0.6940` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 11,230.00 USD | 4,420.00 USD | 9,470.00 USD |
| `1D` | `0.6950` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 22,480.00 USD | 4,460.00 USD | 3,790.00 USD |
| `7D` | `0.6950` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 31,450.00 USD | 0.00 USD | 12,390.00 USD |
| `1D` | `0.6960` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 58,370.00 USD | 6,000.00 USD | 0.00 USD |
| `1D` | `0.6970` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 33,460.00 USD | 2,430.00 USD | 34.66 USD |
| `7D` | `0.6970` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 50,160.00 USD | 3,180.00 USD | 0.00 USD |
| `1D` | `0.6980` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 9,140.00 USD | 4,100.00 USD | 1,290.00 USD |
| `1D` | `0.6990` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 5,180.00 USD | 4,830.00 USD | 5,380.00 USD |
| `7D` | `0.6990` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 27,730.00 USD | 10,960.00 USD | 30,200.00 USD |
| `1D` | `0.7000` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 18,240.00 USD | 4,020.00 USD | 16,170.00 USD |
| `1D` | `0.7010` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 15,520.00 USD | 0.00 USD | 73.64 USD |
| `7D` | `0.7010` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 16,330.00 USD | 0.00 USD | 10,140.00 USD |
| `1D` | `0.7020` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 14,360.00 USD | 0.00 USD | 22.18 USD |
| `1D` | `0.7030` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 4,330.00 USD | 0.00 USD | 10,510.00 USD |
| `7D` | `0.7030` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 92,960.00 USD | 0.00 USD | 103,540.00 USD |
| `1D` | `0.7040` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 29,930.00 USD | 2,630.00 USD | 17,930.00 USD |
| `1D` | `0.7050` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 29,790.00 USD | 2,660.00 USD | 18,960.00 USD |
| `7D` | `0.7050` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 46,540.00 USD | 0.00 USD | 169,430.00 USD |
| `1D` | `0.7060` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 8,590.00 USD | 3,860.00 USD | 12,360.00 USD |
| `1D` | `0.7070` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 19,980.00 USD | 21,860.00 USD | 17,150.00 USD |
| `7D` | `0.7070` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 28,920.00 USD | 69,790.00 USD | 83,530.00 USD |
| `1D` | `0.7080` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 18,420.00 USD | 3,500.00 USD | 4,310.00 USD |
| `1D` | `0.7090` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 17,580.00 USD | 3,160.00 USD | 8,900.00 USD |
| `7D` | `0.7090` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 121,730.00 USD | 61,400.00 USD | 188,060.00 USD |
| `1D` | `0.7100` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 8,730.00 USD | 1,280.00 USD | 5,030.00 USD |
| `1D` | `0.7110` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 2,660.00 USD | 8,760.00 USD | 8,680.00 USD |
| `7D` | `0.7110` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 85,130.00 USD | 64,110.00 USD | 107,200.00 USD |
| `1D` | `0.7120` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 21,700.00 USD | 4,410.00 USD | 15,710.00 USD |
| `1D` | `0.7130` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 22,890.00 USD | 3,110.00 USD | 32,850.00 USD |
| `7D` | `0.7130` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 135,980.00 USD | 77,290.00 USD | 186,450.00 USD |
| `1D` | `0.7140` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 24,010.00 USD | 5,910.00 USD | 6,410.00 USD |
| `1D` | `0.7150` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 18,260.00 USD | 6,980.00 USD | 23,310.00 USD |
| `7D` | `0.7150` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 177,760.00 USD | 62,090.00 USD | 178,190.00 USD |
| `1D` | `0.7160` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 17,400.00 USD | 11,180.00 USD | 10,820.00 USD |
| `1D` | `0.7170` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 4,910.00 USD | 4,510.00 USD | 12,160.00 USD |
| `7D` | `0.7170` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 168,460.00 USD | 74,260.00 USD | 121,980.00 USD |
| `1D` | `0.7180` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 6,240.00 USD | 2,890.00 USD | 14,880.00 USD |
| `1D` | `0.7190` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 12,780.00 USD | 5,680.00 USD | 2,050.00 USD |
| `7D` | `0.7190` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 88,650.00 USD | 32,980.00 USD | 100,700.00 USD |
| `1D` | `0.7200` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 4,740.00 USD | 9,070.00 USD |
| `1D` | `0.7210` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 10,550.00 USD | 13,350.00 USD | 7,190.00 USD |
| `7D` | `0.7210` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 271,310.00 USD | 58,030.00 USD | 160,570.00 USD |
| `1D` | `0.7220` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 6,730.00 USD | 4,320.00 USD | 885.59 USD |
| `1D` | `0.7230` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 1,140.00 USD | 3,060.00 USD | 7,380.00 USD |
| `7D` | `0.7230` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 171,240.00 USD | 52,810.00 USD | 121,450.00 USD |
| `1D` | `0.7240` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 11,320.00 USD | 3,290.00 USD | 3,650.00 USD |
| `1D` | `0.7250` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 4,760.00 USD | 3,950.00 USD | 9,380.00 USD |
| `7D` | `0.7250` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 139,330.00 USD | 40,040.00 USD | 117,460.00 USD |
| `1D` | `0.7260` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 16,740.00 USD | 2,210.00 USD | 12,280.00 USD |
| `1D` | `0.7270` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 29,920.00 USD | 3,230.00 USD | 12,510.00 USD |
| `7D` | `0.7270` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 111,330.00 USD | 44,700.00 USD | 126,460.00 USD |
| `1D` | `0.7280` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 20,470.00 USD | 3,050.00 USD | 9,480.00 USD |
| `1D` | `0.7290` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 13,150.00 USD | 6,310.00 USD | 16,170.00 USD |
| `7D` | `0.7290` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 89,770.00 USD | 54,440.00 USD | 126,840.00 USD |
| `1D` | `0.7300` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 9,980.00 USD | 7,000.00 USD | 16,570.00 USD |
| `1D` | `0.7310` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 1,010.00 USD | 1,670.00 USD | 2,420.00 USD |
| `7D` | `0.7310` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 183,580.00 USD | 68,560.00 USD | 64,190.00 USD |
| `1D` | `0.7320` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 12,500.00 USD | 1,140.00 USD | 3,630.00 USD |
| `1D` | `0.7330` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 2,180.00 USD | 2,690.00 USD |
| `7D` | `0.7330` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 74,380.00 USD | 25,020.00 USD | 81,690.00 USD |
| `1D` | `0.7340` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 1,530.00 USD | 3,510.00 USD |
| `1D` | `0.7350` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 735.24 USD | 1,470.00 USD | 40.36 USD |
| `7D` | `0.7350` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 97,650.00 USD | 24,440.00 USD | 46,410.00 USD |
| `1D` | `0.7360` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 7,230.00 USD | 5,360.00 USD | 3,710.00 USD |
| `1D` | `0.7370` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 5,150.00 USD | 2,940.00 USD | 3,730.00 USD |
| `7D` | `0.7370` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 46,860.00 USD | 34,840.00 USD | 40,410.00 USD |
| `1D` | `0.7380` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 6,990.00 USD | 2,320.00 USD | 1,910.00 USD |
| `1D` | `0.7390` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 2,330.00 USD | 2,180.00 USD |
| `7D` | `0.7390` | 7,050,000.00 USD | 7,050,000.00 USD | 0.00 USD | 64,070.00 USD | 21,590.00 USD | 65,060.00 USD |
| `1D` | `0.7400` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 8,500.00 USD | 606.70 USD | 4,810.00 USD |
| `1D` | `0.7410` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 7,700.00 USD | 1,030.00 USD | 4,740.00 USD |
| `7D` | `0.7410` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 30,110.00 USD | 36,600.00 USD | 42,560.00 USD |
| `1D` | `0.7420` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.80 USD |
| `1D` | `0.7430` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 1,240.00 USD | 0.00 USD | 125.56 USD |
| `7D` | `0.7430` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 53,760.00 USD | 27,390.00 USD | 55,060.00 USD |
| `1D` | `0.7440` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 1,730.00 USD | 0.00 USD | 4,030.00 USD |
| `7D` | `0.7450` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 78,270.00 USD | 42,280.00 USD | 54,220.00 USD |
| `7D` | `0.7470` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 74,280.00 USD | 28,960.00 USD | 47,350.00 USD |
| `7D` | `0.7490` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 42,220.00 USD | 15,480.00 USD | 13,190.00 USD |
| `7D` | `0.7510` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 60,950.00 USD | 13,310.00 USD | 51,890.00 USD |
| `7D` | `0.7530` | 7,900,000.00 USD | 7,900,000.00 USD | 0.00 USD | 48,850.00 USD | 9,020.00 USD | 29,630.00 USD |
| `7D` | `0.7550` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 27,450.00 USD | 6,470.00 USD | 30,480.00 USD |
| `7D` | `0.7570` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 36,750.00 USD | 5,360.00 USD | 36,040.00 USD |
| `7D` | `0.7590` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 61,250.00 USD | 8,240.00 USD | 45,520.00 USD |
| `7D` | `0.7610` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 36,150.00 USD | 12,300.00 USD | 64,270.00 USD |
| `7D` | `0.7630` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 73,980.00 USD | 28,990.00 USD | 27,580.00 USD |
| `7D` | `0.7650` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 59,460.00 USD | 9,740.00 USD | 98,390.00 USD |
| `7D` | `0.7670` | 8,680,000.00 USD | 8,680,000.00 USD | 0.00 USD | 45,270.00 USD | 25,520.00 USD | 35,980.00 USD |
| `7D` | `0.7690` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 39,720.00 USD | 18,230.00 USD | 26,680.00 USD |
| `7D` | `0.7710` | 8,900,000.00 USD | 8,900,000.00 USD | 0.00 USD | 59,050.00 USD | 29,000.00 USD | 48,990.00 USD |
| `7D` | `0.7730` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 42,000.00 USD | 27,790.00 USD | 21,150.00 USD |
| `7D` | `0.7750` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 19,570.00 USD | 11,130.00 USD | 30,950.00 USD |
| `7D` | `0.7770` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 48,840.00 USD | 18,920.00 USD | 24,270.00 USD |
| `7D` | `0.7790` | 9,250,000.00 USD | 9,250,000.00 USD | 0.00 USD | 64,380.00 USD | 7,690.00 USD | 36,040.00 USD |
| `7D` | `0.7810` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 99,040.00 USD | 24,320.00 USD | 57,920.00 USD |
| `7D` | `0.7830` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 110,720.00 USD | 18,940.00 USD | 8,410.00 USD |
| `7D` | `0.7850` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 38,200.00 USD | 15,730.00 USD | 63,610.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `94.74M` | Total OI Tokens: `145,246,901.1 APT`
  * 1h OI Change: `-2.47%` | 4h OI Change: `-4.59%` | 24h OI Change: `-6.40%`
  * Exchange Breakdown: Binance=`18.41M` | Bybit=`19.41M` | OKX=`4.51M` | Hyperliquid=`3.59M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.71K` | Last 24h: `8.88K` | Last 3d: `10.89K` | Last 7d: `5.22K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0029%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0038%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0031%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0025%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `APT` | `32.66%` | `67.34%` | `0.49` | 6,700,000.00 USD |
| `15M` | `Binance` | `41.84%` | `58.16%` | `0.72` | 2,790,000.00 USD |
| `15M` | `OKX` | `46.71%` | `53.29%` | `0.88` | 493,000.00 USD |
| `15M` | `Bybit` | `36.69%` | `63.31%` | `0.58` | 699,160.00 USD |
| `15M` | `KuCoin` | `49.52%` | `50.48%` | `0.98` | 176,530.00 USD |
| `15M` | `Gate` | `39.43%` | `60.57%` | `0.65` | 125,870.00 USD |
| `15M` | `Bitget` | `38.68%` | `61.32%` | `0.63` | 140,500.00 USD |
| `15M` | `BingX` | `5.08%` | `94.92%` | `0.05` | 1,570,000.00 USD |
| `15M` | `MEXC` | `29.92%` | `70.08%` | `0.43` | 332,730.00 USD |
| `15M` | `Bitunix` | `45.47%` | `54.53%` | `0.83` | 106,000.00 USD |
| `15M` | `Hyperliquid` | `36.62%` | `63.38%` | `0.58` | 57,460.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `29.42%` | `70.58%` | `0.42` | 97,240.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `73.82%` | `26.18%` | `2.82` | 81,220.00 USD |
| `15M` | `HTX` | `18.7%` | `81.3%` | `0.23` | 950.26 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `2.98%` | `97.02%` | `0.03` | 11,620.00 USD |
| `15M` | `Aster` | `7.49%` | `92.51%` | `0.08` | 6,170.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `82.17%` | `17.83%` | `4.61` | 1,300.00 USD |
| `15M` | `Whale Positions` | `41.84%` | `58.16%` | `0.72` | 2,790,000.00 USD |
| `15M` | `Global Accounts` | `32.66%` | `67.34%` | `0.49` | 6,700,000.00 USD |
| `1H` | `APT` | `40.28%` | `59.72%` | `0.67` | 15,510,000.00 USD |
| `1H` | `Binance` | `45.44%` | `54.56%` | `0.83` | 6,340,000.00 USD |
| `1H` | `OKX` | `45.52%` | `54.48%` | `0.84` | 1,340,000.00 USD |
| `1H` | `Bybit` | `44.74%` | `55.26%` | `0.81` | 1,760,000.00 USD |
| `1H` | `KuCoin` | `49.57%` | `50.43%` | `0.98` | 698,430.00 USD |
| `1H` | `Gate` | `61.18%` | `38.82%` | `1.58` | 441,190.00 USD |
| `1H` | `Bitget` | `40.67%` | `59.33%` | `0.69` | 444,650.00 USD |
| `1H` | `BingX` | `12.88%` | `87.12%` | `0.15` | 2,220,000.00 USD |
| `1H` | `MEXC` | `31.9%` | `68.1%` | `0.47` | 936,260.00 USD |
| `1H` | `Bitunix` | `50.81%` | `49.19%` | `1.03` | 316,070.00 USD |
| `1H` | `Hyperliquid` | `30.85%` | `69.15%` | `0.45` | 188,170.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.99%` | `52.01%` | `0.92` | 319,520.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `42.1%` | `57.9%` | `0.73` | 416,950.00 USD |
| `1H` | `HTX` | `31.24%` | `68.76%` | `0.45` | 2,850.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `41.36%` | `58.64%` | `0.71` | 56,320.00 USD |
| `1H` | `Aster` | `36.74%` | `63.26%` | `0.58` | 14,320.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `62.54%` | `37.46%` | `1.67` | 11,320.00 USD |
| `1H` | `Whale Positions` | `45.44%` | `54.56%` | `0.83` | 6,340,000.00 USD |
| `1H` | `Global Accounts` | `40.28%` | `59.72%` | `0.67` | 15,510,000.00 USD |
| `4H` | `APT` | `41.50%` | `58.50%` | `0.71` | 73,830,000.00 USD |
| `4H` | `Binance` | `44.07%` | `55.93%` | `0.79` | 26,450,000.00 USD |
| `4H` | `OKX` | `47.54%` | `52.46%` | `0.91` | 11,700,000.00 USD |
| `4H` | `Bybit` | `41.6%` | `58.4%` | `0.71` | 7,930,000.00 USD |
| `4H` | `KuCoin` | `49.82%` | `50.18%` | `0.99` | 1,960,000.00 USD |
| `4H` | `Gate` | `54.41%` | `45.59%` | `1.19` | 1,250,000.00 USD |
| `4H` | `Bitget` | `36.37%` | `63.63%` | `0.57` | 2,290,000.00 USD |
| `4H` | `BingX` | `18.5%` | `81.5%` | `0.23` | 2,660,000.00 USD |
| `4H` | `MEXC` | `41.71%` | `58.29%` | `0.72` | 1,230,000.00 USD |
| `4H` | `Bitunix` | `48.06%` | `51.94%` | `0.93` | 2,550,000.00 USD |
| `4H` | `Hyperliquid` | `27.37%` | `72.63%` | `0.38` | 772,390.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.84%` | `50.16%` | `0.99` | 11,570,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 375.23 USD |
| `4H` | `WhiteBIT` | `49.12%` | `50.88%` | `0.97` | 3,070,000.00 USD |
| `4H` | `HTX` | `54.45%` | `45.55%` | `1.20` | 25,540.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `75.18%` | `24.82%` | `3.03` | 156,420.00 USD |
| `4H` | `Aster` | `27.84%` | `72.16%` | `0.39` | 195,150.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `73.43%` | `26.57%` | `2.76` | 30,380.00 USD |
| `4H` | `Whale Positions` | `44.07%` | `55.93%` | `0.79` | 26,450,000.00 USD |
| `4H` | `Global Accounts` | `41.50%` | `58.50%` | `0.71` | 73,830,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.6769` | `0.6744` | `0.6769` | `0.6780` | `0.6712` | 1,016,262.60 USD | 354,802.44 USD | 661,460.16 USD | -306,657.72 USD | `-30.18%` | `8B / 14S` |
| `0:00 UTC` | `0.6692` | `0.6690` | `0.6692` | `0.6736` | `0.6673` | 765,890.04 USD | 348,689.76 USD | 417,200.28 USD | -68,510.51 USD | `-8.95%` | `4B / 13S` |
| `5:00 UTC` | `0.6717` | `0.6708` | `0.6717` | `0.6727` | `0.6676` | 334,763.13 USD | 213,901.71 USD | 120,861.42 USD | 93,040.30 USD | `+27.79%` | `17B / 7S` |
| `0:00 UTC` | `0.6677` | `0.6685` | `0.6677` | `0.6704` | `0.6665` | 391,631.76 USD | 249,885.86 USD | 141,745.90 USD | 108,139.96 USD | `+27.61%` | `10B / 3S` |
| `5:00 UTC` | `0.6715` | `0.6701` | `0.6715` | `0.6721` | `0.6670` | 386,689.12 USD | 212,109.34 USD | 174,579.78 USD | 37,529.57 USD | `+9.71%` | `19B / 4S` |
| `0:00 UTC` | `0.6734` | `0.6731` | `0.6734` | `0.6741` | `0.6704` | 427,696.28 USD | 267,875.40 USD | 159,820.88 USD | 108,054.53 USD | `+25.26%` | `9B / 2S` |
| `5:00 UTC` | `0.6713` | `0.6715` | `0.6713` | `0.6739` | `0.6704` | 216,510.95 USD | 86,107.15 USD | 130,403.80 USD | -44,296.65 USD | `-20.46%` | `5B / 11S` |
| `0:00 UTC` | `0.6618` | `0.6610` | `0.6618` | `0.6728` | `0.6545` | 3,111,032.57 USD | 1,289,720.42 USD | 1,821,312.14 USD | -531,591.72 USD | `-17.09%` | `14B / 47S` |
| `5:00 UTC` | `0.6646` | `0.6634` | `0.6646` | `0.6663` | `0.6601` | 1,040,684.48 USD | 553,372.77 USD | 487,311.70 USD | 66,061.07 USD | `+6.35%` | `21B / 6S` |
| `0:00 UTC` | `0.6501` | `0.6521` | `0.6501` | `0.6641` | `0.6462` | 3,246,224.53 USD | 1,437,266.04 USD | 1,808,958.49 USD | -371,692.46 USD | `-11.45%` | `15B / 41S` |

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
| `5m` | -163,770.00 USD | -74,240.00 USD | **`DISTRIBUTION`** |
| `15m` | -172,970.00 USD | -153,300.00 USD | **`DISTRIBUTION`** |
| `30m` | -225,780.00 USD | -340,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -235,230.00 USD | -569,760.00 USD | **`DISTRIBUTION`** |
| `2h` | -247,980.00 USD | -81,220.00 USD | **`DISTRIBUTION`** |
| `4h` | -346,760.00 USD | -2,030,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -131,020.00 USD | -3,130,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -47,130.00 USD | -3,240,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -50,060.00 USD | -3,420,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,350,000.00 USD | -6,630,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -4,990,000.00 USD | -20,940,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,790,000.00 USD | -101,620,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-163.77K` | 15m=`-172.97K` | 1h=`-235.23K` | 24h=`-1.35M`
* Futures Capital Netflows: 5m=`-74.24K` | 15m=`-153.30K` | 1h=`-569.76K` | 24h=`-6.63M`
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
  * `2026-10-30 01:35:25 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:09:25 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:09:25 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:09:25 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:08:25 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:08:25 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:25 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:25 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:25 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:25 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:25 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
