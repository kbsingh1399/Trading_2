# 🏛️ SOVEREIGN CANDIDATE DOSSIER: APT
**Canonical Key**: `APT` | **Broker Instrument**: `APTUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 02:03:23 IST` (`2026-10-29 20:33:23 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.6596` | `0.6637` | `0.6568` | `0.6633` | `603,355` | 399,120.74 USD | 1,460.08 USD | `+0.37%` | -3,860,715.90 USD | `+0.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.6633` | `0.6663` | `0.6616` | `0.6644` | `657,206` | 436,716.09 USD | 255,722.29 USD | `+58.56%` | -3,604,993.60 USD | `+2.25` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.6645` | `0.6656` | `0.6603` | `0.6638` | `497,613` | 329,765.61 USD | -118,475.56 USD | `-35.93%` | -3,723,469.16 USD | `-0.99` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.6715` | `0.6738` | `0.6703` | `0.6721` | `322,435` | 216,510.95 USD | -44,296.65 USD | `-20.46%` | -3,319,935.80 USD | `+0.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.6721` | `0.6728` | `0.6545` | `0.6633` | `4,707,296` | 3,111,032.57 USD | -531,591.72 USD | `-17.09%` | -3,851,527.52 USD | `-2.44` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.6633` | `0.6663` | `0.6603` | `0.6639` | `1,156,401` | 767,531.46 USD | 138,296.49 USD | `+18.02%` | -3,713,231.03 USD | `+1.19` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.6796` | `0.6804` | `0.6673` | `0.6699` | `4,032,719` | 2,714,496.22 USD | -416,792.27 USD | `-15.35%` | -3,627,547.27 USD | `-0.90` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.6700` | `0.6740` | `0.6665` | `0.6721` | `2,120,904` | 1,422,528.11 USD | 209,427.40 USD | `+14.72%` | -3,418,119.86 USD | `+1.29` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.6721` | `0.6728` | `0.6545` | `0.6638` | `5,862,115` | 3,877,514.26 USD | -394,344.98 USD | `-10.17%` | -3,812,464.84 USD | `-0.75` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -1,678,888.13 USD | `+0.66` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -3,147,816.26 USD | `-1.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6545` | `0.6639` | `5,863,696` | 3,878,564.02 USD | -393,295.23 USD | `-10.14%` | -3,541,111.49 USD | `+0.38` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6611` | `0.6759` | `0.6485` | `0.6561` | `10,656,422` | 7,044,804.33 USD | -366,898.68 USD | `-5.21%` | -1,470,659.97 USD | `+1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6561` | `0.6774` | `0.6549` | `0.6712` | `7,448,343` | 4,965,296.85 USD | -60,141.40 USD | `-1.21%` | -1,530,801.38 USD | `+1.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -1,678,888.13 USD | `+0.66` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -3,147,816.26 USD | `-1.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6545` | `0.6639` | `5,863,696` | 3,878,564.02 USD | -393,295.23 USD | `-10.14%` | -3,541,111.49 USD | `+0.38` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:54:30 IST` |

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
| `Live` | `Long Liquidation` | `0.5785` | 662.59 USD | 76,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5835` | 1,690.00 USD | 75,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 210.96 USD | 74,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 586.80 USD | 73,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5870` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 1,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5880` | 2,070,000.00 USD | 2,070,000.00 USD | 4,160.00 USD | 1,580.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5880` | 2,590,000.00 USD | 2,590,000.00 USD | 3,110.00 USD | 0.00 USD | 65.70 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5885` | 440.16 USD | 73,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5890` | 2,060,000.00 USD | 2,060,000.00 USD | 3,460.00 USD | 0.00 USD | 7.65 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5890` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 15.37 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5895` | 1,690.00 USD | 72,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5900` | 2,060,000.00 USD | 2,060,000.00 USD | 4,730.00 USD | 679.41 USD | 3.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5900` | 2,580,000.00 USD | 2,580,000.00 USD | 3,120.00 USD | 1,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5910` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 1,820.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5920` | 2,050,000.00 USD | 2,050,000.00 USD | 11,320.00 USD | 2,650.00 USD | 1,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5920` | 2,580,000.00 USD | 2,580,000.00 USD | 11,690.00 USD | 2,820.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5925` | 609.14 USD | 71,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5930` | 2,030,000.00 USD | 2,030,000.00 USD | 3,420.00 USD | 0.00 USD | 5,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5930` | 2,560,000.00 USD | 2,560,000.00 USD | 10,090.00 USD | 0.00 USD | 9,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5935` | 21,790.00 USD | 70,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5940` | 2,030,000.00 USD | 2,030,000.00 USD | 5,890.00 USD | 0.00 USD | 4,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5940` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 46.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5950` | 2,010,000.00 USD | 2,010,000.00 USD | 11,950.00 USD | 2,470.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5950` | 2,540,000.00 USD | 2,540,000.00 USD | 13,060.00 USD | 0.00 USD | 4,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5955` | 3,850.00 USD | 48,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5960` | 2,000,000.00 USD | 2,000,000.00 USD | 8,460.00 USD | 456.46 USD | 6,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5960` | 2,520,000.00 USD | 2,520,000.00 USD | 5,120.00 USD | 1,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5970` | 1,980,000.00 USD | 1,980,000.00 USD | 4,020.00 USD | 2,820.00 USD | 4,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5970` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 16,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5975` | 157.22 USD | 45,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5980` | 1,970,000.00 USD | 1,970,000.00 USD | 6,400.00 USD | 1,740.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5980` | 2,500,000.00 USD | 2,500,000.00 USD | 20,380.00 USD | 826.53 USD | 3,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5990` | 1,950,000.00 USD | 1,950,000.00 USD | 12,500.00 USD | 1,140.00 USD | 3,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5990` | 2,470,000.00 USD | 2,470,000.00 USD | 3,320.00 USD | 1,340.00 USD | 14,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6000` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 1,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6000` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 796.28 USD | 4,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6005` | 852.06 USD | 44,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6010` | 1,930,000.00 USD | 1,930,000.00 USD | 735.24 USD | 461.96 USD | 15.46 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6020` | 1,930,000.00 USD | 1,930,000.00 USD | 7,230.00 USD | 4,200.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6020` | 2,450,000.00 USD | 2,450,000.00 USD | 4,890.00 USD | 8,040.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6030` | 1,920,000.00 USD | 1,920,000.00 USD | 5,150.00 USD | 2,940.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6030` | 2,430,000.00 USD | 2,430,000.00 USD | 2,890.00 USD | 0.00 USD | 139.74 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6040` | 1,910,000.00 USD | 1,910,000.00 USD | 6,990.00 USD | 2,320.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6040` | 2,430,000.00 USD | 2,430,000.00 USD | 5,730.00 USD | 3,100.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6045` | 527.44 USD | 43,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6050` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 1,750.00 USD | 2,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6060` | 1,890,000.00 USD | 1,890,000.00 USD | 8,500.00 USD | 606.70 USD | 4,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6060` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 65.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6070` | 1,880,000.00 USD | 1,880,000.00 USD | 7,700.00 USD | 1,030.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6070` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 161.30 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6080` | 1,860,000.00 USD | 1,860,000.00 USD | 2,970.00 USD | 0.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6080` | 2,410,000.00 USD | 2,410,000.00 USD | 2,860.00 USD | 0.00 USD | 26.37 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6085` | 455.69 USD | 43,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6090` | 1,860,000.00 USD | 1,860,000.00 USD | 6,430.00 USD | 0.00 USD | 47.82 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6090` | 2,410,000.00 USD | 2,410,000.00 USD | 13,920.00 USD | 0.00 USD | 8,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6100` | 1,850,000.00 USD | 1,850,000.00 USD | 3,960.00 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6100` | 2,390,000.00 USD | 2,390,000.00 USD | 7,480.00 USD | 2,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6105` | 6,090.00 USD | 43,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6110` | 1,840,000.00 USD | 1,840,000.00 USD | 1,430.00 USD | 0.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6110` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 2,210.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6120` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6120` | 2,360,000.00 USD | 2,360,000.00 USD | 2,100.00 USD | 3,510.00 USD | 5,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6130` | 1,840,000.00 USD | 1,840,000.00 USD | 2,140.00 USD | 596.50 USD | 1,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6130` | 2,350,000.00 USD | 2,350,000.00 USD | 8,870.00 USD | 1,050.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6140` | 1,830,000.00 USD | 1,830,000.00 USD | 6,120.00 USD | 0.00 USD | 1,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6140` | 2,340,000.00 USD | 2,340,000.00 USD | 4,540.00 USD | 7,000.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6150` | 1,830,000.00 USD | 1,830,000.00 USD | 2,730.00 USD | 0.00 USD | 30.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6150` | 2,320,000.00 USD | 2,320,000.00 USD | 11,130.00 USD | 5,870.00 USD | 2,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6160` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 1,270.00 USD | 126.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6160` | 2,300,000.00 USD | 2,300,000.00 USD | 1,790.00 USD | 2,510.00 USD | 3,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6170` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6170` | 2,290,000.00 USD | 2,290,000.00 USD | 13,260.00 USD | 2,610.00 USD | 14,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6180` | 2,260,000.00 USD | 2,260,000.00 USD | 7,600.00 USD | 1,190.00 USD | 4,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6190` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 126.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6190` | 2,250,000.00 USD | 2,250,000.00 USD | 9,560.00 USD | 1,930.00 USD | 9,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6195` | 3,170.00 USD | 36,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6200` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6200` | 2,230,000.00 USD | 2,230,000.00 USD | 13,870.00 USD | 5,230.00 USD | 6,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6210` | 1,820,000.00 USD | 1,820,000.00 USD | 1,990.00 USD | 0.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6210` | 2,200,000.00 USD | 2,200,000.00 USD | 4,760.00 USD | 1,860.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6220` | 1,810,000.00 USD | 1,810,000.00 USD | 2,520.00 USD | 0.00 USD | 7.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6220` | 2,190,000.00 USD | 2,190,000.00 USD | 7,960.00 USD | 2,310.00 USD | 29,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6230` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 1,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6230` | 2,150,000.00 USD | 2,150,000.00 USD | 9,770.00 USD | 4,700.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6235` | 3,250.00 USD | 33,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6240` | 1,810,000.00 USD | 1,810,000.00 USD | 3,220.00 USD | 3,780.00 USD | 76.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6240` | 2,130,000.00 USD | 2,130,000.00 USD | 18,610.00 USD | 4,720.00 USD | 5,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6250` | 1,800,000.00 USD | 1,800,000.00 USD | 1,800.00 USD | 2,050.00 USD | 113.26 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6250` | 2,100,000.00 USD | 2,100,000.00 USD | 16,120.00 USD | 3,830.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6255` | 286.65 USD | 30,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6260` | 1,800,000.00 USD | 1,800,000.00 USD | 8,920.00 USD | 751.16 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6260` | 2,080,000.00 USD | 2,080,000.00 USD | 20,890.00 USD | 7,660.00 USD | 26,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6265` | 10,530.00 USD | 30,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6270` | 1,790,000.00 USD | 1,790,000.00 USD | 3,700.00 USD | 3,940.00 USD | 12,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6270` | 2,020,000.00 USD | 2,020,000.00 USD | 17,460.00 USD | 8,200.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6280` | 1,770,000.00 USD | 1,770,000.00 USD | 11,690.00 USD | 463.43 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6280` | 1,970,000.00 USD | 1,970,000.00 USD | 9,160.00 USD | 9,230.00 USD | 16,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6290` | 1,750,000.00 USD | 1,750,000.00 USD | 11,890.00 USD | 1,200.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6290` | 1,940,000.00 USD | 1,940,000.00 USD | 17,710.00 USD | 6,740.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6300` | 1,730,000.00 USD | 1,730,000.00 USD | 12,950.00 USD | 2,010.00 USD | 3,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6300` | 1,900,000.00 USD | 1,900,000.00 USD | 10,040.00 USD | 7,890.00 USD | 11,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6310` | 1,720,000.00 USD | 1,720,000.00 USD | 12,360.00 USD | 6,080.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6310` | 1,870,000.00 USD | 1,870,000.00 USD | 19,340.00 USD | 4,520.00 USD | 17,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6315` | 1,010.00 USD | 19,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6320` | 1,680,000.00 USD | 1,680,000.00 USD | 33,310.00 USD | 10,600.00 USD | 14,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6320` | 1,830,000.00 USD | 1,830,000.00 USD | 34,110.00 USD | 12,650.00 USD | 23,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6330` | 1,620,000.00 USD | 1,620,000.00 USD | 17,300.00 USD | 3,580.00 USD | 19,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6330` | 1,760,000.00 USD | 1,760,000.00 USD | 57,940.00 USD | 14,700.00 USD | 33,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6340` | 1,580,000.00 USD | 1,580,000.00 USD | 21,990.00 USD | 2,600.00 USD | 17,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6340` | 1,650,000.00 USD | 1,650,000.00 USD | 10,730.00 USD | 3,420.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6350` | 1,540,000.00 USD | 1,540,000.00 USD | 32,430.00 USD | 9,480.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6350` | 1,630,000.00 USD | 1,630,000.00 USD | 34,320.00 USD | 2,430.00 USD | 22,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6360` | 1,490,000.00 USD | 1,490,000.00 USD | 50,620.00 USD | 10,760.00 USD | 37,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6360` | 1,570,000.00 USD | 1,570,000.00 USD | 42,690.00 USD | 7,300.00 USD | 56,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6370` | 1,390,000.00 USD | 1,390,000.00 USD | 26,310.00 USD | 6,240.00 USD | 30,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6370` | 1,470,000.00 USD | 1,470,000.00 USD | 80,880.00 USD | 4,870.00 USD | 9,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6375` | 5,900.00 USD | 18,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6380` | 1,330,000.00 USD | 1,330,000.00 USD | 36,240.00 USD | 7,180.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6380` | 1,370,000.00 USD | 1,370,000.00 USD | 18,140.00 USD | 3,870.00 USD | 30,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6385` | 582.30 USD | 12,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6390` | 1,280,000.00 USD | 1,280,000.00 USD | 18,790.00 USD | 529.57 USD | 6,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6390` | 1,320,000.00 USD | 1,320,000.00 USD | 10,200.00 USD | 7,510.00 USD | 13,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6400` | 1,260,000.00 USD | 1,260,000.00 USD | 9,830.00 USD | 9,970.00 USD | 26,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6400` | 1,290,000.00 USD | 1,290,000.00 USD | 15,560.00 USD | 0.00 USD | 569.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6410` | 1,210,000.00 USD | 1,210,000.00 USD | 20,930.00 USD | 1,480.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6410` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 6,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6415` | 4,740.00 USD | 12,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6420` | 1,180,000.00 USD | 1,180,000.00 USD | 43,840.00 USD | 13,850.00 USD | 12,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6420` | 1,270,000.00 USD | 1,270,000.00 USD | 55,350.00 USD | 26,560.00 USD | 10,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6430` | 1,110,000.00 USD | 1,110,000.00 USD | 35,700.00 USD | 9,880.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6430` | 1,180,000.00 USD | 1,180,000.00 USD | 16,200.00 USD | 7,140.00 USD | 2,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6435` | 3,450.00 USD | 7,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6440` | 1,050,000.00 USD | 1,050,000.00 USD | 39,760.00 USD | 16,890.00 USD | 27,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6440` | 1,150,000.00 USD | 1,150,000.00 USD | 28,490.00 USD | 17,680.00 USD | 15,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6450` | 965,390.00 USD | 965,390.00 USD | 70,250.00 USD | 22,940.00 USD | 36,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6450` | 1,090,000.00 USD | 1,090,000.00 USD | 81,220.00 USD | 15,560.00 USD | 35,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6455` | 3,730.00 USD | 3,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6460` | 835,560.00 USD | 835,560.00 USD | 57,400.00 USD | 12,380.00 USD | 56,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6460` | 955,230.00 USD | 955,230.00 USD | 91,390.00 USD | 14,300.00 USD | 75,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6470` | 708,950.00 USD | 708,950.00 USD | 69,180.00 USD | 7,780.00 USD | 46,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6470` | 773,980.00 USD | 773,980.00 USD | 9,660.00 USD | 3,880.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6480` | 585,710.00 USD | 585,710.00 USD | 74,630.00 USD | 16,500.00 USD | 15,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6480` | 751,070.00 USD | 751,070.00 USD | 76,770.00 USD | 0.00 USD | 23,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6485` | 259.68 USD | 259.68 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6490` | 479,170.00 USD | 479,170.00 USD | 60,640.00 USD | 3,800.00 USD | 59,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6490` | 650,740.00 USD | 650,740.00 USD | 36,340.00 USD | 0.00 USD | 18,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6500` | 355,090.00 USD | 355,090.00 USD | 64,920.00 USD | 4,610.00 USD | 35,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6500` | 596,310.00 USD | 596,310.00 USD | 37,220.00 USD | 0.00 USD | 114,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6510` | 250,150.00 USD | 250,150.00 USD | 33,120.00 USD | 7,910.00 USD | 75,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6510` | 444,520.00 USD | 444,520.00 USD | 165,050.00 USD | 4,190.00 USD | 18,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6520` | 133,720.00 USD | 133,720.00 USD | 69,880.00 USD | 6,190.00 USD | 14,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6520` | 256,920.00 USD | 256,920.00 USD | 46,620.00 USD | 6,720.00 USD | 86,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6530` | 43,540.00 USD | 43,540.00 USD | 5,780.00 USD | 1,060.00 USD | 11,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6530` | 116,670.00 USD | 116,670.00 USD | 0.00 USD | 0.00 USD | 46,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6540` | 24,970.00 USD | 24,970.00 USD | 11,450.00 USD | 2,530.00 USD | 10,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6540` | 69,860.00 USD | 69,860.00 USD | 15,730.00 USD | 0.00 USD | 14,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6550` | 426.09 USD | 426.09 USD | 0.00 USD | 0.00 USD | 46.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6550` | 39,600.00 USD | 39,600.00 USD | 0.00 USD | 0.00 USD | 302.99 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6560` | 379.57 USD | 379.57 USD | 0.00 USD | 0.00 USD | 0.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6560` | 39,300.00 USD | 39,300.00 USD | 0.00 USD | 5,380.00 USD | 562.81 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6570` | 379.45 USD | 379.45 USD | 0.00 USD | 0.00 USD | 39.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6570` | 33,360.00 USD | 33,360.00 USD | 0.00 USD | 6,350.00 USD | 198.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6580` | 339.59 USD | 339.59 USD | 0.00 USD | 0.00 USD | 30.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6580` | 26,810.00 USD | 26,810.00 USD | 0.00 USD | 21,920.00 USD | 383.15 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6590` | 308.97 USD | 308.97 USD | 0.00 USD | 0.00 USD | 98.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6590` | 4,500.00 USD | 4,500.00 USD | 0.00 USD | 0.00 USD | 193.29 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6600` | 4,310.00 USD | 4,310.00 USD | 0.00 USD | 4,180.00 USD | 127.46 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6610` | 210.21 USD | 210.21 USD | 0.00 USD | 0.00 USD | 150.77 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6610` | 540.47 USD | 540.47 USD | 0.00 USD | 0.00 USD | 540.47 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6610` | 1,080.00 USD | 1,080.00 USD | 0.00 USD | 0.00 USD | 540.47 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6620` | 59.44 USD | 59.44 USD | 0.00 USD | 0.00 USD | 59.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6620` | 1,280.00 USD | 1,280.00 USD | 0.00 USD | 0.00 USD | 202.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6630` | 41.69 USD | 41.69 USD | 0.00 USD | 0.00 USD | 41.69 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6630` | 83.38 USD | 83.38 USD | 0.00 USD | 0.00 USD | 41.69 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6630` | 1,790.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | 502.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6640` | 142.80 USD | 142.80 USD | 0.00 USD | 0.00 USD | 59.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6640` | 1,960.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD | 170.30 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6650` | 8,860.00 USD | 8,860.00 USD | 0.00 USD | 6,770.00 USD | 133.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6660` | 5,550.00 USD | 5,550.00 USD | 0.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6660` | 9,140.00 USD | 9,140.00 USD | 0.00 USD | 0.00 USD | 279.02 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6670` | 24,420.00 USD | 24,420.00 USD | 18,850.00 USD | 0.00 USD | 17.74 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6670` | 9,380.00 USD | 9,380.00 USD | 0.00 USD | 0.00 USD | 238.68 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6680` | 10,040.00 USD | 10,040.00 USD | 0.00 USD | 0.00 USD | 666.83 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6690` | 28,810.00 USD | 28,810.00 USD | 0.00 USD | 0.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6700` | 64,130.00 USD | 64,130.00 USD | 8,830.00 USD | 1,920.00 USD | 24,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6710` | 106,110.00 USD | 106,110.00 USD | 41,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6710` | 98,650.00 USD | 98,650.00 USD | 58,470.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6720` | 106,110.00 USD | 106,110.00 USD | 0.00 USD | 0.00 USD | 3.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6730` | 136,090.00 USD | 136,090.00 USD | 24,320.00 USD | 1,170.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6740` | 179,660.00 USD | 179,660.00 USD | 26,500.00 USD | 7,120.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6740` | 138,380.00 USD | 138,380.00 USD | 39,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6750` | 222,590.00 USD | 222,590.00 USD | 28,700.00 USD | 5,970.00 USD | 8,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6750` | 214,170.00 USD | 214,170.00 USD | 0.00 USD | 75,730.00 USD | 68.35 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6760` | 240,280.00 USD | 240,280.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6760` | 249,500.00 USD | 249,500.00 USD | 0.00 USD | 2,240.00 USD | 33,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6770` | 275,230.00 USD | 275,230.00 USD | 14,540.00 USD | 6,110.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6770` | 335,230.00 USD | 335,230.00 USD | 63,600.00 USD | 4,190.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6780` | 321,470.00 USD | 321,470.00 USD | 33,610.00 USD | 12,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6780` | 345,450.00 USD | 345,450.00 USD | 0.00 USD | 10,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6790` | 354,280.00 USD | 354,280.00 USD | 0.00 USD | 18,610.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6790` | 362,040.00 USD | 362,040.00 USD | 0.00 USD | 16,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6800` | 356,740.00 USD | 356,740.00 USD | 0.00 USD | 0.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6810` | 364,320.00 USD | 364,320.00 USD | 0.00 USD | 0.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6810` | 377,750.00 USD | 377,750.00 USD | 0.00 USD | 15,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6820` | 406,030.00 USD | 406,030.00 USD | 22,600.00 USD | 12,000.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6820` | 448,050.00 USD | 448,050.00 USD | 32,570.00 USD | 37,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6830` | 492,550.00 USD | 492,550.00 USD | 24,570.00 USD | 26,060.00 USD | 35,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6830` | 507,330.00 USD | 507,330.00 USD | 0.00 USD | 11,020.00 USD | 48,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6840` | 573,410.00 USD | 573,410.00 USD | 45,780.00 USD | 24,170.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6840` | 655,960.00 USD | 655,960.00 USD | 57,890.00 USD | 36,580.00 USD | 54,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6850` | 646,650.00 USD | 646,650.00 USD | 56,840.00 USD | 5,780.00 USD | 10,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6850` | 688,410.00 USD | 688,410.00 USD | 17,270.00 USD | 4,710.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6860` | 703,880.00 USD | 703,880.00 USD | 40,250.00 USD | 4,380.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6860` | 731,040.00 USD | 731,040.00 USD | 32,660.00 USD | 9,830.00 USD | 131.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6870` | 753,160.00 USD | 753,160.00 USD | 44,290.00 USD | 1,160.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6870` | 750,900.00 USD | 750,900.00 USD | 19,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6880` | 810,020.00 USD | 810,020.00 USD | 14,350.00 USD | 9,600.00 USD | 32,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6880` | 786,370.00 USD | 786,370.00 USD | 18,170.00 USD | 17,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6890` | 812,770.00 USD | 812,770.00 USD | 0.00 USD | 0.00 USD | 2,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6890` | 797,400.00 USD | 797,400.00 USD | 0.00 USD | 11,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6900` | 850,000.00 USD | 850,000.00 USD | 14,580.00 USD | 1,610.00 USD | 21,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6900` | 818,430.00 USD | 818,430.00 USD | 0.00 USD | 4,480.00 USD | 16,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6910` | 920,340.00 USD | 920,340.00 USD | 28,860.00 USD | 1,730.00 USD | 39,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6910` | 927,660.00 USD | 927,660.00 USD | 69,620.00 USD | 2,090.00 USD | 37,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6920` | 950,820.00 USD | 950,820.00 USD | 16,800.00 USD | 0.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6920` | 952,030.00 USD | 952,030.00 USD | 0.00 USD | 0.00 USD | 24,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6930` | 961,020.00 USD | 961,020.00 USD | 10,030.00 USD | 0.00 USD | 168.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6930` | 1,010,000.00 USD | 1,010,000.00 USD | 14,220.00 USD | 0.00 USD | 42,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6940` | 986,130.00 USD | 986,130.00 USD | 11,230.00 USD | 4,420.00 USD | 9,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6950` | 1,020,000.00 USD | 1,020,000.00 USD | 22,480.00 USD | 4,460.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6950` | 1,050,000.00 USD | 1,050,000.00 USD | 31,450.00 USD | 0.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6960` | 1,080,000.00 USD | 1,080,000.00 USD | 58,370.00 USD | 6,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6960` | 1,080,000.00 USD | 1,080,000.00 USD | 28,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6970` | 1,120,000.00 USD | 1,120,000.00 USD | 33,460.00 USD | 2,430.00 USD | 34.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6970` | 1,110,000.00 USD | 1,110,000.00 USD | 21,650.00 USD | 3,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6980` | 1,130,000.00 USD | 1,130,000.00 USD | 9,140.00 USD | 4,100.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6980` | 1,130,000.00 USD | 1,130,000.00 USD | 14,330.00 USD | 10,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6990` | 1,150,000.00 USD | 1,150,000.00 USD | 5,180.00 USD | 4,830.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6990` | 1,170,000.00 USD | 1,170,000.00 USD | 13,410.00 USD | 0.00 USD | 30,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7000` | 1,190,000.00 USD | 1,190,000.00 USD | 18,240.00 USD | 4,020.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7000` | 1,200,000.00 USD | 1,200,000.00 USD | 16,330.00 USD | 0.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7010` | 1,200,000.00 USD | 1,200,000.00 USD | 15,520.00 USD | 0.00 USD | 73.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7010` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 98.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7020` | 1,220,000.00 USD | 1,220,000.00 USD | 14,360.00 USD | 0.00 USD | 22.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7020` | 1,270,000.00 USD | 1,270,000.00 USD | 16,350.00 USD | 0.00 USD | 52,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7030` | 1,230,000.00 USD | 1,230,000.00 USD | 4,330.00 USD | 0.00 USD | 10,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7030` | 1,400,000.00 USD | 1,400,000.00 USD | 76,610.00 USD | 0.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7040` | 1,280,000.00 USD | 1,280,000.00 USD | 29,930.00 USD | 2,630.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7040` | 1,460,000.00 USD | 1,460,000.00 USD | 18,910.00 USD | 0.00 USD | 46,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7050` | 1,330,000.00 USD | 1,330,000.00 USD | 29,790.00 USD | 2,660.00 USD | 18,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7050` | 1,610,000.00 USD | 1,610,000.00 USD | 27,630.00 USD | 0.00 USD | 123,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7060` | 1,360,000.00 USD | 1,360,000.00 USD | 8,590.00 USD | 3,860.00 USD | 12,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7060` | 1,720,000.00 USD | 1,720,000.00 USD | 20,200.00 USD | 33,490.00 USD | 54,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7070` | 1,420,000.00 USD | 1,420,000.00 USD | 19,980.00 USD | 21,860.00 USD | 17,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7070` | 1,800,000.00 USD | 1,800,000.00 USD | 8,720.00 USD | 36,300.00 USD | 29,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7075` | 2,220.00 USD | 2,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7080` | 1,440,000.00 USD | 1,440,000.00 USD | 18,420.00 USD | 3,500.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7080` | 1,890,000.00 USD | 1,890,000.00 USD | 15,730.00 USD | 28,570.00 USD | 53,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7090` | 1,470,000.00 USD | 1,470,000.00 USD | 17,580.00 USD | 3,160.00 USD | 8,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7090` | 2,170,000.00 USD | 2,170,000.00 USD | 106,000.00 USD | 32,830.00 USD | 134,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7100` | 1,490,000.00 USD | 1,490,000.00 USD | 8,730.00 USD | 1,280.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7100` | 2,260,000.00 USD | 2,260,000.00 USD | 44,820.00 USD | 30,700.00 USD | 14,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7110` | 1,510,000.00 USD | 1,510,000.00 USD | 2,660.00 USD | 8,760.00 USD | 8,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7110` | 2,420,000.00 USD | 2,420,000.00 USD | 40,300.00 USD | 33,410.00 USD | 92,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7120` | 1,550,000.00 USD | 1,550,000.00 USD | 21,700.00 USD | 4,410.00 USD | 15,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7120` | 2,670,000.00 USD | 2,670,000.00 USD | 60,730.00 USD | 45,350.00 USD | 135,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7130` | 1,610,000.00 USD | 1,610,000.00 USD | 28,640.00 USD | 3,110.00 USD | 32,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7130` | 2,820,000.00 USD | 2,820,000.00 USD | 75,250.00 USD | 31,940.00 USD | 51,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7140` | 1,650,000.00 USD | 1,650,000.00 USD | 24,010.00 USD | 5,910.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7140` | 3,070,000.00 USD | 3,070,000.00 USD | 127,300.00 USD | 35,310.00 USD | 81,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7150` | 1,700,000.00 USD | 1,700,000.00 USD | 18,260.00 USD | 6,980.00 USD | 23,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7150` | 3,240,000.00 USD | 3,240,000.00 USD | 50,460.00 USD | 26,770.00 USD | 96,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7160` | 1,740,000.00 USD | 1,740,000.00 USD | 17,400.00 USD | 11,180.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7160` | 3,410,000.00 USD | 3,410,000.00 USD | 62,580.00 USD | 38,490.00 USD | 67,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7170` | 1,760,000.00 USD | 1,760,000.00 USD | 4,910.00 USD | 3,880.00 USD | 8,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7170` | 3,610,000.00 USD | 3,610,000.00 USD | 105,890.00 USD | 35,770.00 USD | 54,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7180` | 1,780,000.00 USD | 1,780,000.00 USD | 6,240.00 USD | 2,890.00 USD | 14,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7180` | 3,700,000.00 USD | 3,700,000.00 USD | 59,980.00 USD | 21,140.00 USD | 12,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7190` | 1,800,000.00 USD | 1,800,000.00 USD | 12,780.00 USD | 5,680.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7190` | 3,830,000.00 USD | 3,830,000.00 USD | 28,670.00 USD | 11,840.00 USD | 88,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7200` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 4,740.00 USD | 9,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7200` | 4,020,000.00 USD | 4,020,000.00 USD | 65,080.00 USD | 33,310.00 USD | 90,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7210` | 1,840,000.00 USD | 1,840,000.00 USD | 10,550.00 USD | 13,350.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7210` | 4,320,000.00 USD | 4,320,000.00 USD | 206,240.00 USD | 24,720.00 USD | 70,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7220` | 1,860,000.00 USD | 1,860,000.00 USD | 6,730.00 USD | 3,610.00 USD | 885.59 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7220` | 4,500,000.00 USD | 4,500,000.00 USD | 112,190.00 USD | 42,410.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7230` | 1,870,000.00 USD | 1,870,000.00 USD | 1,140.00 USD | 3,060.00 USD | 7,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7230` | 4,670,000.00 USD | 4,670,000.00 USD | 59,050.00 USD | 10,400.00 USD | 94,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7240` | 1,890,000.00 USD | 1,890,000.00 USD | 11,320.00 USD | 3,290.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7240` | 4,800,000.00 USD | 4,800,000.00 USD | 87,060.00 USD | 14,510.00 USD | 35,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7250` | 1,900,000.00 USD | 1,900,000.00 USD | 4,760.00 USD | 3,950.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7250` | 4,960,000.00 USD | 4,960,000.00 USD | 52,270.00 USD | 25,530.00 USD | 82,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7255` | 43,950.00 USD | 46,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7260` | 1,930,000.00 USD | 1,930,000.00 USD | 16,740.00 USD | 2,210.00 USD | 12,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7260` | 5,140,000.00 USD | 5,140,000.00 USD | 54,140.00 USD | 26,590.00 USD | 93,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7270` | 1,980,000.00 USD | 1,980,000.00 USD | 25,220.00 USD | 3,230.00 USD | 12,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7270` | 5,250,000.00 USD | 5,250,000.00 USD | 57,190.00 USD | 18,120.00 USD | 33,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7280` | 2,010,000.00 USD | 2,010,000.00 USD | 20,470.00 USD | 3,050.00 USD | 9,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7280` | 5,360,000.00 USD | 5,360,000.00 USD | 42,560.00 USD | 22,060.00 USD | 50,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7290` | 2,040,000.00 USD | 2,040,000.00 USD | 13,150.00 USD | 6,310.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7290` | 5,520,000.00 USD | 5,520,000.00 USD | 47,200.00 USD | 32,380.00 USD | 76,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7300` | 2,080,000.00 USD | 2,080,000.00 USD | 9,980.00 USD | 7,000.00 USD | 16,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7300` | 5,650,000.00 USD | 5,650,000.00 USD | 68,110.00 USD | 27,940.00 USD | 33,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7310` | 2,080,000.00 USD | 2,080,000.00 USD | 1,010.00 USD | 1,670.00 USD | 2,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7310` | 5,830,000.00 USD | 5,830,000.00 USD | 115,470.00 USD | 40,620.00 USD | 31,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7320` | 2,100,000.00 USD | 2,100,000.00 USD | 12,500.00 USD | 1,140.00 USD | 3,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7320` | 5,980,000.00 USD | 5,980,000.00 USD | 74,380.00 USD | 25,020.00 USD | 49,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7330` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 2,180.00 USD | 2,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7330` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 0.00 USD | 32,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7340` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 1,530.00 USD | 3,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7340` | 6,090,000.00 USD | 6,090,000.00 USD | 31,260.00 USD | 8,620.00 USD | 30,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7345` | 150.17 USD | 46,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7350` | 2,110,000.00 USD | 2,110,000.00 USD | 735.24 USD | 1,470.00 USD | 40.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7350` | 6,180,000.00 USD | 6,180,000.00 USD | 66,390.00 USD | 15,820.00 USD | 15,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7360` | 2,130,000.00 USD | 2,130,000.00 USD | 7,230.00 USD | 5,360.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7360` | 6,270,000.00 USD | 6,270,000.00 USD | 37,210.00 USD | 30,980.00 USD | 19,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7370` | 2,140,000.00 USD | 2,140,000.00 USD | 5,150.00 USD | 2,940.00 USD | 3,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7370` | 6,310,000.00 USD | 6,310,000.00 USD | 9,640.00 USD | 3,860.00 USD | 21,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7380` | 2,150,000.00 USD | 2,150,000.00 USD | 6,990.00 USD | 2,320.00 USD | 1,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7380` | 6,430,000.00 USD | 6,430,000.00 USD | 64,070.00 USD | 16,760.00 USD | 39,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7390` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 2,330.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7390` | 6,460,000.00 USD | 6,460,000.00 USD | 0.00 USD | 8,110.00 USD | 25,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7400` | 2,170,000.00 USD | 2,170,000.00 USD | 8,500.00 USD | 606.70 USD | 4,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7400` | 6,480,000.00 USD | 6,480,000.00 USD | 1,730.00 USD | 6,500.00 USD | 11,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7410` | 2,180,000.00 USD | 2,180,000.00 USD | 7,700.00 USD | 1,030.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7410` | 6,570,000.00 USD | 6,570,000.00 USD | 28,380.00 USD | 30,100.00 USD | 31,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7420` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 3.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7420` | 6,590,000.00 USD | 6,590,000.00 USD | 7,430.00 USD | 13,420.00 USD | 520.95 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7430` | 2,190,000.00 USD | 2,190,000.00 USD | 1,240.00 USD | 0.00 USD | 125.56 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7430` | 6,710,000.00 USD | 6,710,000.00 USD | 46,330.00 USD | 13,970.00 USD | 54,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7440` | 6,780,000.00 USD | 6,780,000.00 USD | 28,120.00 USD | 25,920.00 USD | 15,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7450` | 6,880,000.00 USD | 6,880,000.00 USD | 50,150.00 USD | 16,360.00 USD | 38,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7460` | 6,940,000.00 USD | 6,940,000.00 USD | 38,650.00 USD | 10,350.00 USD | 13,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7470` | 7,030,000.00 USD | 7,030,000.00 USD | 35,630.00 USD | 18,610.00 USD | 33,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7480` | 7,070,000.00 USD | 7,070,000.00 USD | 24,950.00 USD | 10,290.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7490` | 7,100,000.00 USD | 7,100,000.00 USD | 17,270.00 USD | 5,180.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7500` | 7,160,000.00 USD | 7,160,000.00 USD | 35,050.00 USD | 7,430.00 USD | 16,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7510` | 7,230,000.00 USD | 7,230,000.00 USD | 25,900.00 USD | 5,870.00 USD | 35,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7520` | 7,280,000.00 USD | 7,280,000.00 USD | 27,570.00 USD | 7,130.00 USD | 15,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7530` | 7,320,000.00 USD | 7,320,000.00 USD | 21,290.00 USD | 1,890.00 USD | 14,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7540` | 7,340,000.00 USD | 7,340,000.00 USD | 9,060.00 USD | 0.00 USD | 10,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7550` | 7,380,000.00 USD | 7,380,000.00 USD | 18,390.00 USD | 6,470.00 USD | 19,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7560` | 7,390,000.00 USD | 7,390,000.00 USD | 7,600.00 USD | 1,100.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7570` | 7,460,000.00 USD | 7,460,000.00 USD | 29,140.00 USD | 4,260.00 USD | 33,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7580` | 7,500,000.00 USD | 7,500,000.00 USD | 26,280.00 USD | 7,530.00 USD | 12,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7590` | 7,570,000.00 USD | 7,570,000.00 USD | 34,970.00 USD | 717.68 USD | 32,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7600` | 7,650,000.00 USD | 7,650,000.00 USD | 22,050.00 USD | 3,600.00 USD | 47,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7610` | 7,690,000.00 USD | 7,690,000.00 USD | 14,110.00 USD | 8,700.00 USD | 16,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7620` | 7,750,000.00 USD | 7,750,000.00 USD | 40,030.00 USD | 15,470.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7630` | 7,820,000.00 USD | 7,820,000.00 USD | 33,960.00 USD | 13,520.00 USD | 22,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7635` | 143.11 USD | 46,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7640` | 7,850,000.00 USD | 7,850,000.00 USD | 16,430.00 USD | 0.00 USD | 19,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7650` | 7,980,000.00 USD | 7,980,000.00 USD | 43,020.00 USD | 9,740.00 USD | 79,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7660` | 8,020,000.00 USD | 8,020,000.00 USD | 13,100.00 USD | 8,390.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7670` | 8,090,000.00 USD | 8,090,000.00 USD | 32,170.00 USD | 17,130.00 USD | 24,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7680` | 8,160,000.00 USD | 8,160,000.00 USD | 34,410.00 USD | 15,390.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7690` | 8,170,000.00 USD | 8,170,000.00 USD | 5,320.00 USD | 2,840.00 USD | 9,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7700` | 8,220,000.00 USD | 8,220,000.00 USD | 5,540.00 USD | 9,750.00 USD | 31,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7710` | 8,310,000.00 USD | 8,310,000.00 USD | 53,500.00 USD | 19,240.00 USD | 17,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7720` | 8,340,000.00 USD | 8,340,000.00 USD | 4,880.00 USD | 13,680.00 USD | 8,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7725` | 165.62 USD | 46,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7730` | 8,400,000.00 USD | 8,400,000.00 USD | 37,120.00 USD | 14,120.00 USD | 12,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7740` | 8,450,000.00 USD | 8,450,000.00 USD | 14,480.00 USD | 11,130.00 USD | 23,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7750` | 8,460,000.00 USD | 8,460,000.00 USD | 5,090.00 USD | 0.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7760` | 8,510,000.00 USD | 8,510,000.00 USD | 33,080.00 USD | 2,980.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7765` | 330.78 USD | 46,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7770` | 8,560,000.00 USD | 8,560,000.00 USD | 15,750.00 USD | 15,940.00 USD | 19,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7780` | 8,630,000.00 USD | 8,630,000.00 USD | 53,050.00 USD | 4,910.00 USD | 13,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7790` | 8,660,000.00 USD | 8,660,000.00 USD | 11,330.00 USD | 2,770.00 USD | 22,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7800` | 8,790,000.00 USD | 8,790,000.00 USD | 49,160.00 USD | 19,160.00 USD | 57,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7810` | 8,850,000.00 USD | 8,850,000.00 USD | 49,880.00 USD | 5,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7820` | 8,900,000.00 USD | 8,900,000.00 USD | 40,140.00 USD | 12,700.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7830` | 8,980,000.00 USD | 8,980,000.00 USD | 70,580.00 USD | 6,240.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7840` | 9,010,000.00 USD | 9,010,000.00 USD | 24,790.00 USD | 4,140.00 USD | 32.85 USD | `Tier 1 CEX` |
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
| `7D` | `0.5870` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 0.00 USD | 1,400.00 USD | 0.00 USD |
| `1D` | `0.5880` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 4,160.00 USD | 1,580.00 USD | 3,620.00 USD |
| `7D` | `0.5880` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 3,110.00 USD | 0.00 USD | 65.70 USD |
| `1D` | `0.5890` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 3,460.00 USD | 0.00 USD | 7.65 USD |
| `7D` | `0.5890` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 15.37 USD |
| `1D` | `0.5900` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 4,730.00 USD | 679.41 USD | 3.61 USD |
| `7D` | `0.5900` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 3,120.00 USD | 1,560.00 USD | 0.00 USD |
| `1D` | `0.5910` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 0.00 USD | 1,820.00 USD | 4,100.00 USD |
| `1D` | `0.5920` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 11,320.00 USD | 2,650.00 USD | 1,190.00 USD |
| `7D` | `0.5920` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 11,690.00 USD | 2,820.00 USD | 6,030.00 USD |
| `1D` | `0.5930` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 3,420.00 USD | 0.00 USD | 5,760.00 USD |
| `7D` | `0.5930` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 10,090.00 USD | 0.00 USD | 9,780.00 USD |
| `1D` | `0.5940` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 5,890.00 USD | 0.00 USD | 4,450.00 USD |
| `7D` | `0.5940` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 46.83 USD |
| `1D` | `0.5950` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 11,950.00 USD | 2,470.00 USD | 1,900.00 USD |
| `7D` | `0.5950` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 13,060.00 USD | 0.00 USD | 4,530.00 USD |
| `1D` | `0.5960` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 8,460.00 USD | 456.46 USD | 6,230.00 USD |
| `7D` | `0.5960` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 5,120.00 USD | 1,640.00 USD | 0.00 USD |
| `1D` | `0.5970` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 4,020.00 USD | 2,820.00 USD | 4,420.00 USD |
| `7D` | `0.5970` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 16,330.00 USD |
| `1D` | `0.5980` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 6,400.00 USD | 1,740.00 USD | 11,190.00 USD |
| `7D` | `0.5980` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 20,380.00 USD | 826.53 USD | 3,590.00 USD |
| `1D` | `0.5990` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 12,500.00 USD | 1,140.00 USD | 3,840.00 USD |
| `7D` | `0.5990` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 3,320.00 USD | 1,340.00 USD | 14,100.00 USD |
| `1D` | `0.6000` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 1,130.00 USD |
| `7D` | `0.6000` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 0.00 USD | 796.28 USD | 4,700.00 USD |
| `1D` | `0.6010` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 735.24 USD | 461.96 USD | 15.46 USD |
| `1D` | `0.6020` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 7,230.00 USD | 4,200.00 USD | 3,710.00 USD |
| `7D` | `0.6020` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 4,890.00 USD | 8,040.00 USD | 4,010.00 USD |
| `1D` | `0.6030` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 5,150.00 USD | 2,940.00 USD | 3,710.00 USD |
| `7D` | `0.6030` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 2,890.00 USD | 0.00 USD | 139.74 USD |
| `1D` | `0.6040` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 6,990.00 USD | 2,320.00 USD | 1,880.00 USD |
| `7D` | `0.6040` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 5,730.00 USD | 3,100.00 USD | 7,830.00 USD |
| `1D` | `0.6050` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 0.00 USD | 1,750.00 USD | 2,160.00 USD |
| `1D` | `0.6060` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 8,500.00 USD | 606.70 USD | 4,740.00 USD |
| `7D` | `0.6060` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 65.64 USD |
| `1D` | `0.6070` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 7,700.00 USD | 1,030.00 USD | 4,740.00 USD |
| `7D` | `0.6070` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 161.30 USD |
| `1D` | `0.6080` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 2,970.00 USD | 0.00 USD | 4,010.00 USD |
| `7D` | `0.6080` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 2,860.00 USD | 0.00 USD | 26.37 USD |
| `1D` | `0.6090` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 6,430.00 USD | 0.00 USD | 47.82 USD |
| `7D` | `0.6090` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 13,920.00 USD | 0.00 USD | 8,280.00 USD |
| `1D` | `0.6100` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 3,960.00 USD | 0.00 USD | 5,750.00 USD |
| `7D` | `0.6100` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 7,480.00 USD | 2,570.00 USD | 0.00 USD |
| `1D` | `0.6110` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 1,430.00 USD | 0.00 USD | 1,070.00 USD |
| `7D` | `0.6110` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 0.00 USD | 2,210.00 USD | 12,890.00 USD |
| `1D` | `0.6120` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD |
| `7D` | `0.6120` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 2,100.00 USD | 3,510.00 USD | 5,700.00 USD |
| `1D` | `0.6130` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 2,140.00 USD | 596.50 USD | 1,020.00 USD |
| `7D` | `0.6130` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 8,870.00 USD | 1,050.00 USD | 4,140.00 USD |
| `1D` | `0.6140` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 6,120.00 USD | 0.00 USD | 1,000.00 USD |
| `7D` | `0.6140` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 4,540.00 USD | 7,000.00 USD | 6,570.00 USD |
| `1D` | `0.6150` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 2,730.00 USD | 0.00 USD | 30.06 USD |
| `7D` | `0.6150` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 11,130.00 USD | 5,870.00 USD | 2,820.00 USD |
| `1D` | `0.6160` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 1,270.00 USD | 126.06 USD |
| `7D` | `0.6160` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 1,790.00 USD | 2,510.00 USD | 3,780.00 USD |
| `1D` | `0.6170` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 3,480.00 USD |
| `7D` | `0.6170` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 13,260.00 USD | 2,610.00 USD | 14,720.00 USD |
| `7D` | `0.6180` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 7,600.00 USD | 1,190.00 USD | 4,360.00 USD |
| `1D` | `0.6190` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 126.86 USD |
| `7D` | `0.6190` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 9,560.00 USD | 1,930.00 USD | 9,440.00 USD |
| `1D` | `0.6200` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD |
| `7D` | `0.6200` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 13,870.00 USD | 5,230.00 USD | 6,180.00 USD |
| `1D` | `0.6210` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 1,990.00 USD | 0.00 USD | 2,070.00 USD |
| `7D` | `0.6210` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 4,760.00 USD | 1,860.00 USD | 5,170.00 USD |
| `1D` | `0.6220` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 2,520.00 USD | 0.00 USD | 7.22 USD |
| `7D` | `0.6220` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 7,960.00 USD | 2,310.00 USD | 29,910.00 USD |
| `1D` | `0.6230` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 1,100.00 USD |
| `7D` | `0.6230` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 9,770.00 USD | 4,700.00 USD | 8,370.00 USD |
| `1D` | `0.6240` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 3,220.00 USD | 3,780.00 USD | 76.16 USD |
| `7D` | `0.6240` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 18,610.00 USD | 4,720.00 USD | 5,140.00 USD |
| `1D` | `0.6250` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 1,800.00 USD | 2,050.00 USD | 113.26 USD |
| `7D` | `0.6250` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 16,120.00 USD | 3,830.00 USD | 2,500.00 USD |
| `1D` | `0.6260` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 8,920.00 USD | 751.16 USD | 2,060.00 USD |
| `7D` | `0.6260` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 20,890.00 USD | 7,660.00 USD | 26,050.00 USD |
| `1D` | `0.6270` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 3,700.00 USD | 3,940.00 USD | 12,850.00 USD |
| `7D` | `0.6270` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 17,460.00 USD | 8,200.00 USD | 24,470.00 USD |
| `1D` | `0.6280` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 11,690.00 USD | 463.43 USD | 2,070.00 USD |
| `7D` | `0.6280` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 9,160.00 USD | 9,230.00 USD | 16,710.00 USD |
| `1D` | `0.6290` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 11,890.00 USD | 1,200.00 USD | 3,750.00 USD |
| `7D` | `0.6290` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 17,710.00 USD | 6,740.00 USD | 10,230.00 USD |
| `1D` | `0.6300` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 12,950.00 USD | 2,010.00 USD | 3,640.00 USD |
| `7D` | `0.6300` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 10,040.00 USD | 7,890.00 USD | 11,360.00 USD |
| `1D` | `0.6310` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 12,360.00 USD | 6,080.00 USD | 14,390.00 USD |
| `7D` | `0.6310` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 19,340.00 USD | 4,520.00 USD | 17,290.00 USD |
| `1D` | `0.6320` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 33,310.00 USD | 10,600.00 USD | 14,850.00 USD |
| `7D` | `0.6320` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 34,110.00 USD | 12,650.00 USD | 23,660.00 USD |
| `1D` | `0.6330` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 17,300.00 USD | 3,580.00 USD | 19,110.00 USD |
| `7D` | `0.6330` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 57,940.00 USD | 14,700.00 USD | 33,860.00 USD |
| `1D` | `0.6340` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 21,990.00 USD | 2,600.00 USD | 17,600.00 USD |
| `7D` | `0.6340` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 10,730.00 USD | 3,420.00 USD | 4,560.00 USD |
| `1D` | `0.6350` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 32,430.00 USD | 9,480.00 USD | 8,060.00 USD |
| `7D` | `0.6350` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 34,320.00 USD | 2,430.00 USD | 22,930.00 USD |
| `1D` | `0.6360` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 50,620.00 USD | 10,760.00 USD | 37,420.00 USD |
| `7D` | `0.6360` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 42,690.00 USD | 7,300.00 USD | 56,850.00 USD |
| `1D` | `0.6370` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 26,310.00 USD | 6,240.00 USD | 30,110.00 USD |
| `7D` | `0.6370` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 80,880.00 USD | 4,870.00 USD | 9,480.00 USD |
| `1D` | `0.6380` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 36,240.00 USD | 7,180.00 USD | 5,230.00 USD |
| `7D` | `0.6380` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 18,140.00 USD | 3,870.00 USD | 30,380.00 USD |
| `1D` | `0.6390` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 18,790.00 USD | 529.57 USD | 6,800.00 USD |
| `7D` | `0.6390` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 10,200.00 USD | 7,510.00 USD | 13,150.00 USD |
| `1D` | `0.6400` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 9,830.00 USD | 9,970.00 USD | 26,730.00 USD |
| `7D` | `0.6400` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 15,560.00 USD | 0.00 USD | 569.80 USD |
| `1D` | `0.6410` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 20,930.00 USD | 1,480.00 USD | 7,440.00 USD |
| `7D` | `0.6410` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 6,200.00 USD |
| `1D` | `0.6420` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 43,840.00 USD | 13,850.00 USD | 12,640.00 USD |
| `7D` | `0.6420` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 55,350.00 USD | 26,560.00 USD | 10,080.00 USD |
| `1D` | `0.6430` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 35,700.00 USD | 9,880.00 USD | 13,730.00 USD |
| `7D` | `0.6430` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 16,200.00 USD | 7,140.00 USD | 2,840.00 USD |
| `1D` | `0.6440` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 39,760.00 USD | 16,890.00 USD | 27,720.00 USD |
| `7D` | `0.6440` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 28,490.00 USD | 17,680.00 USD | 15,240.00 USD |
| `1D` | `0.6450` | 965,390.00 USD | 0.00 USD | 965,390.00 USD | 70,250.00 USD | 22,940.00 USD | 36,640.00 USD |
| `7D` | `0.6450` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 81,220.00 USD | 15,560.00 USD | 35,680.00 USD |
| `1D` | `0.6460` | 835,560.00 USD | 0.00 USD | 835,560.00 USD | 57,400.00 USD | 12,380.00 USD | 56,830.00 USD |
| `7D` | `0.6460` | 955,230.00 USD | 0.00 USD | 955,230.00 USD | 91,390.00 USD | 14,300.00 USD | 75,550.00 USD |
| `1D` | `0.6470` | 708,950.00 USD | 0.00 USD | 708,950.00 USD | 69,180.00 USD | 7,780.00 USD | 46,280.00 USD |
| `7D` | `0.6470` | 773,980.00 USD | 0.00 USD | 773,980.00 USD | 9,660.00 USD | 3,880.00 USD | 9,370.00 USD |
| `1D` | `0.6480` | 585,710.00 USD | 0.00 USD | 585,710.00 USD | 74,630.00 USD | 16,500.00 USD | 15,410.00 USD |
| `7D` | `0.6480` | 751,070.00 USD | 0.00 USD | 751,070.00 USD | 76,770.00 USD | 0.00 USD | 23,550.00 USD |
| `1D` | `0.6490` | 479,170.00 USD | 0.00 USD | 479,170.00 USD | 60,640.00 USD | 3,800.00 USD | 59,650.00 USD |
| `7D` | `0.6490` | 650,740.00 USD | 0.00 USD | 650,740.00 USD | 36,340.00 USD | 0.00 USD | 18,090.00 USD |
| `1D` | `0.6500` | 355,090.00 USD | 0.00 USD | 355,090.00 USD | 64,920.00 USD | 4,610.00 USD | 35,410.00 USD |
| `7D` | `0.6500` | 596,310.00 USD | 0.00 USD | 596,310.00 USD | 37,220.00 USD | 0.00 USD | 114,570.00 USD |
| `1D` | `0.6510` | 250,150.00 USD | 0.00 USD | 250,150.00 USD | 33,120.00 USD | 7,910.00 USD | 75,410.00 USD |
| `7D` | `0.6510` | 444,520.00 USD | 0.00 USD | 444,520.00 USD | 165,050.00 USD | 4,190.00 USD | 18,370.00 USD |
| `1D` | `0.6520` | 133,720.00 USD | 0.00 USD | 133,720.00 USD | 69,880.00 USD | 6,190.00 USD | 14,110.00 USD |
| `7D` | `0.6520` | 256,920.00 USD | 0.00 USD | 256,920.00 USD | 46,620.00 USD | 6,720.00 USD | 86,910.00 USD |
| `1D` | `0.6530` | 43,540.00 USD | 0.00 USD | 43,540.00 USD | 5,780.00 USD | 1,060.00 USD | 11,730.00 USD |
| `7D` | `0.6530` | 116,670.00 USD | 0.00 USD | 116,670.00 USD | 0.00 USD | 0.00 USD | 46,810.00 USD |
| `1D` | `0.6540` | 24,970.00 USD | 0.00 USD | 24,970.00 USD | 11,450.00 USD | 2,530.00 USD | 10,560.00 USD |
| `7D` | `0.6540` | 69,860.00 USD | 0.00 USD | 69,860.00 USD | 15,730.00 USD | 0.00 USD | 14,530.00 USD |
| `1D` | `0.6550` | 426.09 USD | 0.00 USD | 426.09 USD | 0.00 USD | 0.00 USD | 46.52 USD |
| `7D` | `0.6550` | 39,600.00 USD | 0.00 USD | 39,600.00 USD | 0.00 USD | 0.00 USD | 302.99 USD |
| `1D` | `0.6560` | 379.57 USD | 0.00 USD | 379.57 USD | 0.00 USD | 0.00 USD | 0.12 USD |
| `7D` | `0.6560` | 39,300.00 USD | 0.00 USD | 39,300.00 USD | 0.00 USD | 5,380.00 USD | 562.81 USD |
| `1D` | `0.6570` | 379.45 USD | 0.00 USD | 379.45 USD | 0.00 USD | 0.00 USD | 39.86 USD |
| `7D` | `0.6570` | 33,360.00 USD | 0.00 USD | 33,360.00 USD | 0.00 USD | 6,350.00 USD | 198.80 USD |
| `1D` | `0.6580` | 339.59 USD | 0.00 USD | 339.59 USD | 0.00 USD | 0.00 USD | 30.62 USD |
| `7D` | `0.6580` | 26,810.00 USD | 0.00 USD | 26,810.00 USD | 0.00 USD | 21,920.00 USD | 383.15 USD |
| `1D` | `0.6590` | 308.97 USD | 0.00 USD | 308.97 USD | 0.00 USD | 0.00 USD | 98.76 USD |
| `7D` | `0.6590` | 4,500.00 USD | 0.00 USD | 4,500.00 USD | 0.00 USD | 0.00 USD | 193.29 USD |
| `7D` | `0.6600` | 4,310.00 USD | 0.00 USD | 4,310.00 USD | 0.00 USD | 4,180.00 USD | 127.46 USD |
| `1D` | `0.6610` | 210.21 USD | 0.00 USD | 210.21 USD | 0.00 USD | 0.00 USD | 150.77 USD |
| `7D` | `0.6610` | 540.47 USD | 540.47 USD | 0.00 USD | 0.00 USD | 0.00 USD | 540.47 USD |
| `7D` | `0.6610` | 1,080.00 USD | 1,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 540.47 USD |
| `1D` | `0.6620` | 59.44 USD | 0.00 USD | 59.44 USD | 0.00 USD | 0.00 USD | 59.44 USD |
| `7D` | `0.6620` | 1,280.00 USD | 1,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 202.10 USD |
| `1D` | `0.6630` | 41.69 USD | 41.69 USD | 0.00 USD | 0.00 USD | 0.00 USD | 41.69 USD |
| `1D` | `0.6630` | 83.38 USD | 83.38 USD | 0.00 USD | 0.00 USD | 0.00 USD | 41.69 USD |
| `7D` | `0.6630` | 1,790.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 502.00 USD |
| `1D` | `0.6640` | 142.80 USD | 142.80 USD | 0.00 USD | 0.00 USD | 0.00 USD | 59.42 USD |
| `7D` | `0.6640` | 1,960.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 170.30 USD |
| `7D` | `0.6650` | 8,860.00 USD | 8,860.00 USD | 0.00 USD | 0.00 USD | 6,770.00 USD | 133.80 USD |
| `1D` | `0.6660` | 5,550.00 USD | 5,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,410.00 USD |
| `7D` | `0.6660` | 9,140.00 USD | 9,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 279.02 USD |
| `1D` | `0.6670` | 24,420.00 USD | 24,420.00 USD | 0.00 USD | 18,850.00 USD | 0.00 USD | 17.74 USD |
| `7D` | `0.6670` | 9,380.00 USD | 9,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 238.68 USD |
| `7D` | `0.6680` | 10,040.00 USD | 10,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 666.83 USD |
| `1D` | `0.6690` | 28,810.00 USD | 28,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,390.00 USD |
| `1D` | `0.6700` | 64,130.00 USD | 64,130.00 USD | 0.00 USD | 8,830.00 USD | 1,920.00 USD | 24,570.00 USD |
| `1D` | `0.6710` | 106,110.00 USD | 106,110.00 USD | 0.00 USD | 41,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6710` | 98,650.00 USD | 98,650.00 USD | 0.00 USD | 58,470.00 USD | 0.00 USD | 30,140.00 USD |
| `1D` | `0.6720` | 106,110.00 USD | 106,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.80 USD |
| `1D` | `0.6730` | 136,090.00 USD | 136,090.00 USD | 0.00 USD | 24,320.00 USD | 1,170.00 USD | 4,490.00 USD |
| `1D` | `0.6740` | 179,660.00 USD | 179,660.00 USD | 0.00 USD | 26,500.00 USD | 7,120.00 USD | 9,950.00 USD |
| `7D` | `0.6740` | 138,380.00 USD | 138,380.00 USD | 0.00 USD | 39,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6750` | 222,590.00 USD | 222,590.00 USD | 0.00 USD | 28,700.00 USD | 5,970.00 USD | 8,250.00 USD |
| `7D` | `0.6750` | 214,170.00 USD | 214,170.00 USD | 0.00 USD | 0.00 USD | 75,730.00 USD | 68.35 USD |
| `1D` | `0.6760` | 240,280.00 USD | 240,280.00 USD | 0.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.6760` | 249,500.00 USD | 249,500.00 USD | 0.00 USD | 0.00 USD | 2,240.00 USD | 33,090.00 USD |
| `1D` | `0.6770` | 275,230.00 USD | 275,230.00 USD | 0.00 USD | 14,540.00 USD | 6,110.00 USD | 14,290.00 USD |
| `7D` | `0.6770` | 335,230.00 USD | 335,230.00 USD | 0.00 USD | 63,600.00 USD | 4,190.00 USD | 17,930.00 USD |
| `1D` | `0.6780` | 321,470.00 USD | 321,470.00 USD | 0.00 USD | 33,610.00 USD | 12,640.00 USD | 0.00 USD |
| `7D` | `0.6780` | 345,450.00 USD | 345,450.00 USD | 0.00 USD | 0.00 USD | 10,220.00 USD | 0.00 USD |
| `1D` | `0.6790` | 354,280.00 USD | 354,280.00 USD | 0.00 USD | 0.00 USD | 18,610.00 USD | 14,200.00 USD |
| `7D` | `0.6790` | 362,040.00 USD | 362,040.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 0.00 USD |
| `1D` | `0.6800` | 356,740.00 USD | 356,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,450.00 USD |
| `1D` | `0.6810` | 364,320.00 USD | 364,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,590.00 USD |
| `7D` | `0.6810` | 377,750.00 USD | 377,750.00 USD | 0.00 USD | 0.00 USD | 15,720.00 USD | 0.00 USD |
| `1D` | `0.6820` | 406,030.00 USD | 406,030.00 USD | 0.00 USD | 22,600.00 USD | 12,000.00 USD | 7,110.00 USD |
| `7D` | `0.6820` | 448,050.00 USD | 448,050.00 USD | 0.00 USD | 32,570.00 USD | 37,730.00 USD | 0.00 USD |
| `1D` | `0.6830` | 492,550.00 USD | 492,550.00 USD | 0.00 USD | 24,570.00 USD | 26,060.00 USD | 35,880.00 USD |
| `7D` | `0.6830` | 507,330.00 USD | 507,330.00 USD | 0.00 USD | 0.00 USD | 11,020.00 USD | 48,260.00 USD |
| `1D` | `0.6840` | 573,410.00 USD | 573,410.00 USD | 0.00 USD | 45,780.00 USD | 24,170.00 USD | 10,920.00 USD |
| `7D` | `0.6840` | 655,960.00 USD | 655,960.00 USD | 0.00 USD | 57,890.00 USD | 36,580.00 USD | 54,170.00 USD |
| `1D` | `0.6850` | 646,650.00 USD | 646,650.00 USD | 0.00 USD | 56,840.00 USD | 5,780.00 USD | 10,620.00 USD |
| `7D` | `0.6850` | 688,410.00 USD | 688,410.00 USD | 0.00 USD | 17,270.00 USD | 4,710.00 USD | 10,480.00 USD |
| `1D` | `0.6860` | 703,880.00 USD | 703,880.00 USD | 0.00 USD | 40,250.00 USD | 4,380.00 USD | 12,600.00 USD |
| `7D` | `0.6860` | 731,040.00 USD | 731,040.00 USD | 0.00 USD | 32,660.00 USD | 9,830.00 USD | 131.40 USD |
| `1D` | `0.6870` | 753,160.00 USD | 753,160.00 USD | 0.00 USD | 44,290.00 USD | 1,160.00 USD | 3,830.00 USD |
| `7D` | `0.6870` | 750,900.00 USD | 750,900.00 USD | 0.00 USD | 19,860.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6880` | 810,020.00 USD | 810,020.00 USD | 0.00 USD | 14,350.00 USD | 9,600.00 USD | 32,900.00 USD |
| `7D` | `0.6880` | 786,370.00 USD | 786,370.00 USD | 0.00 USD | 18,170.00 USD | 17,300.00 USD | 0.00 USD |
| `1D` | `0.6890` | 812,770.00 USD | 812,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,750.00 USD |
| `7D` | `0.6890` | 797,400.00 USD | 797,400.00 USD | 0.00 USD | 0.00 USD | 11,030.00 USD | 0.00 USD |
| `1D` | `0.6900` | 850,000.00 USD | 850,000.00 USD | 0.00 USD | 14,580.00 USD | 1,610.00 USD | 21,050.00 USD |
| `7D` | `0.6900` | 818,430.00 USD | 818,430.00 USD | 0.00 USD | 0.00 USD | 4,480.00 USD | 16,550.00 USD |
| `1D` | `0.6910` | 920,340.00 USD | 920,340.00 USD | 0.00 USD | 28,860.00 USD | 1,730.00 USD | 39,760.00 USD |
| `7D` | `0.6910` | 927,660.00 USD | 927,660.00 USD | 0.00 USD | 69,620.00 USD | 2,090.00 USD | 37,520.00 USD |
| `1D` | `0.6920` | 950,820.00 USD | 950,820.00 USD | 0.00 USD | 16,800.00 USD | 0.00 USD | 13,680.00 USD |
| `7D` | `0.6920` | 952,030.00 USD | 952,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,370.00 USD |
| `1D` | `0.6930` | 961,020.00 USD | 961,020.00 USD | 0.00 USD | 10,030.00 USD | 0.00 USD | 168.16 USD |
| `7D` | `0.6930` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 14,220.00 USD | 0.00 USD | 42,460.00 USD |
| `1D` | `0.6940` | 986,130.00 USD | 986,130.00 USD | 0.00 USD | 11,230.00 USD | 4,420.00 USD | 9,470.00 USD |
| `1D` | `0.6950` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 22,480.00 USD | 4,460.00 USD | 3,790.00 USD |
| `7D` | `0.6950` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 31,450.00 USD | 0.00 USD | 12,390.00 USD |
| `1D` | `0.6960` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 58,370.00 USD | 6,000.00 USD | 0.00 USD |
| `7D` | `0.6960` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 28,500.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6970` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 33,460.00 USD | 2,430.00 USD | 34.66 USD |
| `7D` | `0.6970` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 21,650.00 USD | 3,180.00 USD | 0.00 USD |
| `1D` | `0.6980` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 9,140.00 USD | 4,100.00 USD | 1,290.00 USD |
| `7D` | `0.6980` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 14,330.00 USD | 10,960.00 USD | 0.00 USD |
| `1D` | `0.6990` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 5,180.00 USD | 4,830.00 USD | 5,340.00 USD |
| `7D` | `0.6990` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 13,410.00 USD | 0.00 USD | 30,360.00 USD |
| `1D` | `0.7000` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 18,240.00 USD | 4,020.00 USD | 16,170.00 USD |
| `7D` | `0.7000` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 16,330.00 USD | 0.00 USD | 9,990.00 USD |
| `1D` | `0.7010` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 15,520.00 USD | 0.00 USD | 73.64 USD |
| `7D` | `0.7010` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 98.80 USD |
| `1D` | `0.7020` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 14,360.00 USD | 0.00 USD | 22.18 USD |
| `7D` | `0.7020` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 16,350.00 USD | 0.00 USD | 52,980.00 USD |
| `1D` | `0.7030` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 4,330.00 USD | 0.00 USD | 10,510.00 USD |
| `7D` | `0.7030` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 76,610.00 USD | 0.00 USD | 50,470.00 USD |
| `1D` | `0.7040` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 29,930.00 USD | 2,630.00 USD | 17,930.00 USD |
| `7D` | `0.7040` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 18,910.00 USD | 0.00 USD | 46,110.00 USD |
| `1D` | `0.7050` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 29,790.00 USD | 2,660.00 USD | 18,960.00 USD |
| `7D` | `0.7050` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 27,630.00 USD | 0.00 USD | 123,470.00 USD |
| `1D` | `0.7060` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 8,590.00 USD | 3,860.00 USD | 12,360.00 USD |
| `7D` | `0.7060` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 20,200.00 USD | 33,490.00 USD | 54,450.00 USD |
| `1D` | `0.7070` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 19,980.00 USD | 21,860.00 USD | 17,150.00 USD |
| `7D` | `0.7070` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 8,720.00 USD | 36,300.00 USD | 29,430.00 USD |
| `1D` | `0.7080` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 18,420.00 USD | 3,500.00 USD | 4,310.00 USD |
| `7D` | `0.7080` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 15,730.00 USD | 28,570.00 USD | 53,830.00 USD |
| `1D` | `0.7090` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 17,580.00 USD | 3,160.00 USD | 8,900.00 USD |
| `7D` | `0.7090` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 106,000.00 USD | 32,830.00 USD | 134,470.00 USD |
| `1D` | `0.7100` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 8,730.00 USD | 1,280.00 USD | 5,030.00 USD |
| `7D` | `0.7100` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 44,820.00 USD | 30,700.00 USD | 14,310.00 USD |
| `1D` | `0.7110` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 2,660.00 USD | 8,760.00 USD | 8,680.00 USD |
| `7D` | `0.7110` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 40,300.00 USD | 33,410.00 USD | 92,560.00 USD |
| `1D` | `0.7120` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 21,700.00 USD | 4,410.00 USD | 15,710.00 USD |
| `7D` | `0.7120` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 60,730.00 USD | 45,350.00 USD | 135,220.00 USD |
| `1D` | `0.7130` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 28,640.00 USD | 3,110.00 USD | 32,850.00 USD |
| `7D` | `0.7130` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 75,250.00 USD | 31,940.00 USD | 51,140.00 USD |
| `1D` | `0.7140` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 24,010.00 USD | 5,910.00 USD | 6,410.00 USD |
| `7D` | `0.7140` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 127,300.00 USD | 35,310.00 USD | 81,980.00 USD |
| `1D` | `0.7150` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 18,260.00 USD | 6,980.00 USD | 23,310.00 USD |
| `7D` | `0.7150` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 50,460.00 USD | 26,770.00 USD | 96,460.00 USD |
| `1D` | `0.7160` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 17,400.00 USD | 11,180.00 USD | 10,820.00 USD |
| `7D` | `0.7160` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 62,580.00 USD | 38,490.00 USD | 67,940.00 USD |
| `1D` | `0.7170` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 4,910.00 USD | 3,880.00 USD | 8,680.00 USD |
| `7D` | `0.7170` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 105,890.00 USD | 35,770.00 USD | 54,000.00 USD |
| `1D` | `0.7180` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 6,240.00 USD | 2,890.00 USD | 14,880.00 USD |
| `7D` | `0.7180` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 59,980.00 USD | 21,140.00 USD | 12,910.00 USD |
| `1D` | `0.7190` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 12,780.00 USD | 5,680.00 USD | 2,050.00 USD |
| `7D` | `0.7190` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 28,670.00 USD | 11,840.00 USD | 88,250.00 USD |
| `1D` | `0.7200` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 4,740.00 USD | 9,070.00 USD |
| `7D` | `0.7200` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 65,080.00 USD | 33,310.00 USD | 90,530.00 USD |
| `1D` | `0.7210` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 10,550.00 USD | 13,350.00 USD | 7,190.00 USD |
| `7D` | `0.7210` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 206,240.00 USD | 24,720.00 USD | 70,760.00 USD |
| `1D` | `0.7220` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 6,730.00 USD | 3,610.00 USD | 885.59 USD |
| `7D` | `0.7220` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 112,190.00 USD | 42,410.00 USD | 27,290.00 USD |
| `1D` | `0.7230` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 1,140.00 USD | 3,060.00 USD | 7,380.00 USD |
| `7D` | `0.7230` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 59,050.00 USD | 10,400.00 USD | 94,260.00 USD |
| `1D` | `0.7240` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 11,320.00 USD | 3,290.00 USD | 3,650.00 USD |
| `7D` | `0.7240` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 87,060.00 USD | 14,510.00 USD | 35,020.00 USD |
| `1D` | `0.7250` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 4,760.00 USD | 3,950.00 USD | 9,380.00 USD |
| `7D` | `0.7250` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 52,270.00 USD | 25,530.00 USD | 82,650.00 USD |
| `1D` | `0.7260` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 16,740.00 USD | 2,210.00 USD | 12,280.00 USD |
| `7D` | `0.7260` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 54,140.00 USD | 26,590.00 USD | 93,640.00 USD |
| `1D` | `0.7270` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 25,220.00 USD | 3,230.00 USD | 12,510.00 USD |
| `7D` | `0.7270` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 57,190.00 USD | 18,120.00 USD | 33,750.00 USD |
| `1D` | `0.7280` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 20,470.00 USD | 3,050.00 USD | 9,480.00 USD |
| `7D` | `0.7280` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 42,560.00 USD | 22,060.00 USD | 50,430.00 USD |
| `1D` | `0.7290` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 13,150.00 USD | 6,310.00 USD | 16,170.00 USD |
| `7D` | `0.7290` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 47,200.00 USD | 32,380.00 USD | 76,560.00 USD |
| `1D` | `0.7300` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 9,980.00 USD | 7,000.00 USD | 16,570.00 USD |
| `7D` | `0.7300` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 68,110.00 USD | 27,940.00 USD | 33,050.00 USD |
| `1D` | `0.7310` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 1,010.00 USD | 1,670.00 USD | 2,420.00 USD |
| `7D` | `0.7310` | 5,830,000.00 USD | 5,830,000.00 USD | 0.00 USD | 115,470.00 USD | 40,620.00 USD | 31,490.00 USD |
| `1D` | `0.7320` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 12,500.00 USD | 1,140.00 USD | 3,630.00 USD |
| `7D` | `0.7320` | 5,980,000.00 USD | 5,980,000.00 USD | 0.00 USD | 74,380.00 USD | 25,020.00 USD | 49,130.00 USD |
| `1D` | `0.7330` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 2,180.00 USD | 2,690.00 USD |
| `7D` | `0.7330` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 32,370.00 USD |
| `1D` | `0.7340` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 1,530.00 USD | 3,510.00 USD |
| `7D` | `0.7340` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 31,260.00 USD | 8,620.00 USD | 30,570.00 USD |
| `1D` | `0.7350` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 735.24 USD | 1,470.00 USD | 40.36 USD |
| `7D` | `0.7350` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 66,390.00 USD | 15,820.00 USD | 15,410.00 USD |
| `1D` | `0.7360` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 7,230.00 USD | 5,360.00 USD | 3,710.00 USD |
| `7D` | `0.7360` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 37,210.00 USD | 30,980.00 USD | 19,550.00 USD |
| `1D` | `0.7370` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 5,150.00 USD | 2,940.00 USD | 3,730.00 USD |
| `7D` | `0.7370` | 6,310,000.00 USD | 6,310,000.00 USD | 0.00 USD | 9,640.00 USD | 3,860.00 USD | 21,180.00 USD |
| `1D` | `0.7380` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 6,990.00 USD | 2,320.00 USD | 1,910.00 USD |
| `7D` | `0.7380` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 64,070.00 USD | 16,760.00 USD | 39,590.00 USD |
| `1D` | `0.7390` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 2,330.00 USD | 2,180.00 USD |
| `7D` | `0.7390` | 6,460,000.00 USD | 6,460,000.00 USD | 0.00 USD | 0.00 USD | 8,110.00 USD | 25,670.00 USD |
| `1D` | `0.7400` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 8,500.00 USD | 606.70 USD | 4,810.00 USD |
| `7D` | `0.7400` | 6,480,000.00 USD | 6,480,000.00 USD | 0.00 USD | 1,730.00 USD | 6,500.00 USD | 11,580.00 USD |
| `1D` | `0.7410` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 7,700.00 USD | 1,030.00 USD | 4,740.00 USD |
| `7D` | `0.7410` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 28,380.00 USD | 30,100.00 USD | 31,140.00 USD |
| `1D` | `0.7420` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.80 USD |
| `7D` | `0.7420` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 7,430.00 USD | 13,420.00 USD | 520.95 USD |
| `1D` | `0.7430` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 1,240.00 USD | 0.00 USD | 125.56 USD |
| `7D` | `0.7430` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 46,330.00 USD | 13,970.00 USD | 54,880.00 USD |
| `7D` | `0.7440` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 28,120.00 USD | 25,920.00 USD | 15,730.00 USD |
| `7D` | `0.7450` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 50,150.00 USD | 16,360.00 USD | 38,320.00 USD |
| `7D` | `0.7460` | 6,940,000.00 USD | 6,940,000.00 USD | 0.00 USD | 38,650.00 USD | 10,350.00 USD | 13,230.00 USD |
| `7D` | `0.7470` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 35,630.00 USD | 18,610.00 USD | 33,890.00 USD |
| `7D` | `0.7480` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 24,950.00 USD | 10,290.00 USD | 4,350.00 USD |
| `7D` | `0.7490` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 17,270.00 USD | 5,180.00 USD | 8,830.00 USD |
| `7D` | `0.7500` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 35,050.00 USD | 7,430.00 USD | 16,180.00 USD |
| `7D` | `0.7510` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 25,900.00 USD | 5,870.00 USD | 35,780.00 USD |
| `7D` | `0.7520` | 7,280,000.00 USD | 7,280,000.00 USD | 0.00 USD | 27,570.00 USD | 7,130.00 USD | 15,770.00 USD |
| `7D` | `0.7530` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 21,290.00 USD | 1,890.00 USD | 14,280.00 USD |
| `7D` | `0.7540` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 9,060.00 USD | 0.00 USD | 10,650.00 USD |
| `7D` | `0.7550` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 18,390.00 USD | 6,470.00 USD | 19,630.00 USD |
| `7D` | `0.7560` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 7,600.00 USD | 1,100.00 USD | 2,640.00 USD |
| `7D` | `0.7570` | 7,460,000.00 USD | 7,460,000.00 USD | 0.00 USD | 29,140.00 USD | 4,260.00 USD | 33,340.00 USD |
| `7D` | `0.7580` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 26,280.00 USD | 7,530.00 USD | 12,300.00 USD |
| `7D` | `0.7590` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 34,970.00 USD | 717.68 USD | 32,950.00 USD |
| `7D` | `0.7600` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 22,050.00 USD | 3,600.00 USD | 47,870.00 USD |
| `7D` | `0.7610` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 14,110.00 USD | 8,700.00 USD | 16,520.00 USD |
| `7D` | `0.7620` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 40,030.00 USD | 15,470.00 USD | 5,060.00 USD |
| `7D` | `0.7630` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 33,960.00 USD | 13,520.00 USD | 22,460.00 USD |
| `7D` | `0.7640` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 16,430.00 USD | 0.00 USD | 19,540.00 USD |
| `7D` | `0.7650` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 43,020.00 USD | 9,740.00 USD | 79,180.00 USD |
| `7D` | `0.7660` | 8,020,000.00 USD | 8,020,000.00 USD | 0.00 USD | 13,100.00 USD | 8,390.00 USD | 11,530.00 USD |
| `7D` | `0.7670` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 32,170.00 USD | 17,130.00 USD | 24,300.00 USD |
| `7D` | `0.7680` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 34,410.00 USD | 15,390.00 USD | 16,720.00 USD |
| `7D` | `0.7690` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 5,320.00 USD | 2,840.00 USD | 9,920.00 USD |
| `7D` | `0.7700` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 5,540.00 USD | 9,750.00 USD | 31,600.00 USD |
| `7D` | `0.7710` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 53,500.00 USD | 19,240.00 USD | 17,250.00 USD |
| `7D` | `0.7720` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 4,880.00 USD | 13,680.00 USD | 8,590.00 USD |
| `7D` | `0.7730` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 37,120.00 USD | 14,120.00 USD | 12,580.00 USD |
| `7D` | `0.7740` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 14,480.00 USD | 11,130.00 USD | 23,120.00 USD |
| `7D` | `0.7750` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 5,090.00 USD | 0.00 USD | 7,770.00 USD |
| `7D` | `0.7760` | 8,510,000.00 USD | 8,510,000.00 USD | 0.00 USD | 33,080.00 USD | 2,980.00 USD | 4,930.00 USD |
| `7D` | `0.7770` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 15,750.00 USD | 15,940.00 USD | 19,320.00 USD |
| `7D` | `0.7780` | 8,630,000.00 USD | 8,630,000.00 USD | 0.00 USD | 53,050.00 USD | 4,910.00 USD | 13,280.00 USD |
| `7D` | `0.7790` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 11,330.00 USD | 2,770.00 USD | 22,790.00 USD |
| `7D` | `0.7800` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 49,160.00 USD | 19,160.00 USD | 57,940.00 USD |
| `7D` | `0.7810` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 49,880.00 USD | 5,150.00 USD | 0.00 USD |
| `7D` | `0.7820` | 8,900,000.00 USD | 8,900,000.00 USD | 0.00 USD | 40,140.00 USD | 12,700.00 USD | 6,210.00 USD |
| `7D` | `0.7830` | 8,980,000.00 USD | 8,980,000.00 USD | 0.00 USD | 70,580.00 USD | 6,240.00 USD | 2,170.00 USD |
| `7D` | `0.7840` | 9,010,000.00 USD | 9,010,000.00 USD | 0.00 USD | 24,790.00 USD | 4,140.00 USD | 32.85 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `96.90M` | Total OI Tokens: `146,104,450.9 APT`
  * 1h OI Change: `+0.52%` | 4h OI Change: `-3.18%` | 24h OI Change: `-4.64%`
  * Exchange Breakdown: Binance=`18.97M` | Bybit=`19.76M` | OKX=`4.62M` | Hyperliquid=`3.66M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.82K` | Last 24h: `8.88K` | Last 3d: `10.89K` | Last 7d: `5.22K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0041%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0029%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0043%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0032%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `APT` | `59.45%` | `40.55%` | `1.47` | 7,450,000.00 USD |
| `15M` | `Binance` | `61.06%` | `38.94%` | `1.57` | 2,730,000.00 USD |
| `15M` | `OKX` | `70.5%` | `29.5%` | `2.39` | 1,060,000.00 USD |
| `15M` | `Bybit` | `64.21%` | `35.79%` | `1.79` | 1,170,000.00 USD |
| `15M` | `KuCoin` | `52.04%` | `47.96%` | `1.09` | 139,880.00 USD |
| `15M` | `Gate` | `64.96%` | `35.04%` | `1.85` | 161,470.00 USD |
| `15M` | `Bitget` | `83.69%` | `16.31%` | `5.13` | 320,790.00 USD |
| `15M` | `BingX` | `28.39%` | `71.61%` | `0.40` | 163,900.00 USD |
| `15M` | `MEXC` | `59.39%` | `40.61%` | `1.46` | 27,870.00 USD |
| `15M` | `Bitunix` | `39.17%` | `60.83%` | `0.64` | 226,280.00 USD |
| `15M` | `Hyperliquid` | `73.44%` | `26.56%` | `2.77` | 80,460.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.95%` | `52.05%` | `0.92` | 1,160,000.00 USD |
| `15M` | `Crypto.com` | `59.96%` | `40.04%` | `1.50` | 14.11 USD |
| `15M` | `WhiteBIT` | `10.05%` | `89.95%` | `0.11` | 167,670.00 USD |
| `15M` | `HTX` | `69.9%` | `30.1%` | `2.32` | 3,160.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `94.25%` | `5.75%` | `16.39` | 25,980.00 USD |
| `15M` | `Aster` | `78.86%` | `21.14%` | `3.73` | 4,880.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `32.97%` | `67.03%` | `0.49` | 5,730.00 USD |
| `15M` | `Whale Positions` | `61.06%` | `38.94%` | `1.57` | 2,730,000.00 USD |
| `15M` | `Global Accounts` | `59.45%` | `40.55%` | `1.47` | 7,450,000.00 USD |
| `1H` | `APT` | `45.03%` | `54.97%` | `0.82` | 11,100,000.00 USD |
| `1H` | `Binance` | `46.53%` | `53.47%` | `0.87` | 4,600,000.00 USD |
| `1H` | `OKX` | `45.53%` | `54.47%` | `0.84` | 1,050,000.00 USD |
| `1H` | `Bybit` | `48.25%` | `51.75%` | `0.93` | 1,320,000.00 USD |
| `1H` | `KuCoin` | `49.66%` | `50.34%` | `0.99` | 582,810.00 USD |
| `1H` | `Gate` | `63.82%` | `36.18%` | `1.76` | 342,650.00 USD |
| `1H` | `Bitget` | `44.28%` | `55.72%` | `0.79` | 359,200.00 USD |
| `1H` | `BingX` | `32.7%` | `67.3%` | `0.49` | 864,800.00 USD |
| `1H` | `MEXC` | `38.75%` | `61.25%` | `0.63` | 793,110.00 USD |
| `1H` | `Bitunix` | `49.91%` | `50.09%` | `1.00` | 252,590.00 USD |
| `1H` | `Hyperliquid` | `29.5%` | `70.5%` | `0.42` | 158,810.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.27%` | `50.73%` | `0.97` | 307,940.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `31.7%` | `68.3%` | `0.46` | 396,230.00 USD |
| `1H` | `HTX` | `36.95%` | `63.05%` | `0.59` | 1,920.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `45.82%` | `54.18%` | `0.85` | 55,020.00 USD |
| `1H` | `Aster` | `57.16%` | `42.84%` | `1.33` | 8,660.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `60.11%` | `39.89%` | `1.51` | 10,010.00 USD |
| `1H` | `Whale Positions` | `46.53%` | `53.47%` | `0.87` | 4,600,000.00 USD |
| `1H` | `Global Accounts` | `45.03%` | `54.97%` | `0.82` | 11,100,000.00 USD |
| `4H` | `APT` | `41.10%` | `58.90%` | `0.70` | 74,800,000.00 USD |
| `4H` | `Binance` | `43.21%` | `56.79%` | `0.76` | 26,440,000.00 USD |
| `4H` | `OKX` | `47.17%` | `52.83%` | `0.89` | 12,730,000.00 USD |
| `4H` | `Bybit` | `42.52%` | `57.48%` | `0.74` | 7,860,000.00 USD |
| `4H` | `KuCoin` | `49.89%` | `50.11%` | `1.00` | 1,980,000.00 USD |
| `4H` | `Gate` | `56.52%` | `43.48%` | `1.30` | 1,300,000.00 USD |
| `4H` | `Bitget` | `34.61%` | `65.39%` | `0.53` | 2,220,000.00 USD |
| `4H` | `BingX` | `17.82%` | `82.18%` | `0.22` | 2,660,000.00 USD |
| `4H` | `MEXC` | `43.78%` | `56.22%` | `0.78` | 1,170,000.00 USD |
| `4H` | `Bitunix` | `44.57%` | `55.43%` | `0.80` | 2,590,000.00 USD |
| `4H` | `Hyperliquid` | `26.26%` | `73.74%` | `0.36` | 726,410.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.27%` | `48.73%` | `1.05` | 11,570,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 389.65 USD |
| `4H` | `WhiteBIT` | `46.37%` | `53.63%` | `0.86` | 3,140,000.00 USD |
| `4H` | `HTX` | `56.12%` | `43.88%` | `1.28` | 22,900.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `74.84%` | `25.16%` | `2.97` | 173,440.00 USD |
| `4H` | `Aster` | `34.58%` | `65.42%` | `0.53` | 172,520.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `70.05%` | `29.95%` | `2.34` | 58,910.00 USD |
| `4H` | `Whale Positions` | `43.21%` | `56.79%` | `0.76` | 26,440,000.00 USD |
| `4H` | `Global Accounts` | `41.10%` | `58.90%` | `0.70` | 74,800,000.00 USD |


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
| `0:00 UTC` | `0.6624` | `0.6625` | `0.6624` | `0.6635` | `0.6618` | 55,407.56 USD | 37,177.76 USD | 18,229.80 USD | 18,947.96 USD | `+34.20%` | `5B / 0S` |

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
| `5m` | -1,950.00 USD | -113,810.00 USD | **`DISTRIBUTION`** |
| `15m` | 6,480.00 USD | 252,610.00 USD | **`ACCUMULATION`** |
| `30m` | -59,770.00 USD | -640,940.00 USD | **`DISTRIBUTION`** |
| `1h` | -49,340.00 USD | -477,300.00 USD | **`DISTRIBUTION`** |
| `2h` | -133,800.00 USD | -392,570.00 USD | **`DISTRIBUTION`** |
| `4h` | -151,070.00 USD | -2,340,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 86,500.00 USD | -2,920,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 116,270.00 USD | -3,200,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 120,070.00 USD | -3,350,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,190,000.00 USD | -6,680,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -4,820,000.00 USD | -20,860,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,640,000.00 USD | -101,540,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.95K` | 15m=`+6.48K` | 1h=`-49.34K` | 24h=`-1.19M`
* Futures Capital Netflows: 5m=`-113.81K` | 15m=`+252.61K` | 1h=`-477.30K` | 24h=`-6.68M`
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
  * `2026-10-30 01:35:49 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:00:49 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
