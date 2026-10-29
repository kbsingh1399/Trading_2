# 🏛️ SOVEREIGN CANDIDATE DOSSIER: APT
**Canonical Key**: `APT` | **Broker Instrument**: `APTUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 03:43:29 IST` (`2026-10-29 22:13:29 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.6267` | `0.6279` | `0.6217` | `0.6226` | `363,452` | 227,057.16 USD | 23,879.22 USD | `+10.52%` | -6,627,361.52 USD | `+0.37` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.6227` | `0.6270` | `0.6181` | `0.6191` | `1,248,317` | 776,592.70 USD | -148,736.09 USD | `-19.15%` | -6,776,097.61 USD | `+0.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.6191` | `0.6195` | `0.6183` | `0.6185` | `45,766` | 28,324.56 USD | 444.43 USD | `+1.57%` | -6,775,653.18 USD | `+0.32` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.6316` | `0.6411` | `0.6277` | `0.6279` | `2,225,961` | 1,411,771.88 USD | -129,170.10 USD | `-9.15%` | -6,565,797.96 USD | `+0.15` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.6279` | `0.6309` | `0.6217` | `0.6226` | `1,460,907` | 914,324.95 USD | -46,516.10 USD | `-5.09%` | -6,612,314.06 USD | `+0.30` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.6227` | `0.6270` | `0.6167` | `0.6187` | `1,393,587` | 866,374.54 USD | -184,034.70 USD | `-21.24%` | -6,796,348.76 USD | `+0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.6721` | `0.6728` | `0.6003` | `0.6199` | `31,822,286` | 20,211,912.01 USD | -3,344,538.21 USD | `-16.55%` | -6,520,275.48 USD | `-4.04` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.6198` | `0.6411` | `0.6164` | `0.6226` | `11,690,306` | 7,362,985.80 USD | 19,097.99 USD | `+0.26%` | -6,501,177.50 USD | `+0.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.6227` | `0.6270` | `0.6167` | `0.6187` | `1,393,587` | 866,374.54 USD | -184,034.70 USD | `-21.24%` | -6,685,212.20 USD | `+0.13` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -1,678,888.13 USD | `+0.66` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -3,147,816.26 USD | `-1.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6003` | `0.6187` | `44,906,179` | 28,441,272.35 USD | -3,509,474.92 USD | `-12.34%` | -6,657,291.18 USD | `-2.02` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6611` | `0.6759` | `0.6485` | `0.6561` | `10,656,422` | 7,044,804.33 USD | -366,898.68 USD | `-5.21%` | -1,470,659.97 USD | `+1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6561` | `0.6774` | `0.6549` | `0.6712` | `7,448,343` | 4,965,296.85 USD | -60,141.40 USD | `-1.21%` | -1,530,801.38 USD | `+1.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -1,678,888.13 USD | `+0.66` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -3,147,816.26 USD | `-1.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6003` | `0.6187` | `44,906,179` | 28,441,272.35 USD | -3,509,474.92 USD | `-12.34%` | -6,657,291.18 USD | `-2.02` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:35:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.6795` | 7,438.61 USD | `-` | `NEWS_INTEL` | `-` | #APT Whale SELL: 7.44K USD at 0.6795 USD [API] | `2026-10-28 13:20:11` |


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
| `Live` | `Long Liquidation` | `0.1395` | 419.65 USD | 310,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 200.61 USD | 310,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 269.27 USD | 309,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2035` | 1,480.00 USD | 309,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2065` | 207.79 USD | 308,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 230.98 USD | 307,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2235` | 2,520.00 USD | 307,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 1,460.00 USD | 305,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2545` | 32,830.00 USD | 303,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3175` | 1,590.00 USD | 270,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3255` | 9,260.00 USD | 269,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3265` | 149.84 USD | 259,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3305` | 543.58 USD | 259,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3365` | 25,600.00 USD | 259,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3545` | 177.25 USD | 233,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 189.47 USD | 233,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3805` | 570.75 USD | 233,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3895` | 272.65 USD | 232,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3905` | 359.26 USD | 232,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3955` | 2,640.00 USD | 232,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3995` | 5,240.00 USD | 229,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 570.81 USD | 224,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4045` | 404.50 USD | 223,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4135` | 1,600.00 USD | 223,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 630.86 USD | 221,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4255` | 655.75 USD | 221,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4275` | 3,950.00 USD | 220,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4405` | 4,300.00 USD | 216,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4425` | 101.06 USD | 212,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4445` | 6,490.00 USD | 212,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 226.63 USD | 205,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4515` | 27,090.00 USD | 205,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4575` | 112.72 USD | 178,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4605` | 125.38 USD | 178,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4615` | 830.07 USD | 177,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4625` | 1,680.00 USD | 177,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4635` | 273.41 USD | 175,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4645` | 876.05 USD | 175,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4685` | 468.50 USD | 174,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4715` | 887.06 USD | 173,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4755` | 325.64 USD | 172,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 135.33 USD | 172,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 3,170.00 USD | 172,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4895` | 1,220.00 USD | 169,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 3,180.00 USD | 168,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4975` | 168.65 USD | 164,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 429.90 USD | 164,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 102.82 USD | 164,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 248.05 USD | 164,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5135` | 110.50 USD | 163,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5145` | 288.78 USD | 163,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 9,440.00 USD | 163,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5225` | 11,160.00 USD | 154,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5245` | 3,780.00 USD | 142,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5295` | 39,070.00 USD | 139,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5315` | 12,360.00 USD | 100,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5320` | 869,300.00 USD | 869,300.00 USD | 11,240.00 USD | 0.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5335` | 374.06 USD | 87,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5340` | 854,580.00 USD | 854,580.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5355` | 1,110.00 USD | 87,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5360` | 721,930.00 USD | 721,930.00 USD | 4,510.00 USD | 2,900.00 USD | 3,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5360` | 851,980.00 USD | 851,980.00 USD | 2,440.00 USD | 3,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5380` | 710,790.00 USD | 710,790.00 USD | 5,850.00 USD | 2,040.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5380` | 846,500.00 USD | 846,500.00 USD | 0.00 USD | 1,550.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5400` | 699,760.00 USD | 699,760.00 USD | 4,470.00 USD | 256.13 USD | 2,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5420` | 692,670.00 USD | 692,670.00 USD | 2,590.00 USD | 0.00 USD | 4,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5420` | 842,010.00 USD | 842,010.00 USD | 7,660.00 USD | 1,290.00 USD | 2,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5425` | 156.46 USD | 86,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5440` | 685,200.00 USD | 685,200.00 USD | 714.14 USD | 0.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5440` | 830,120.00 USD | 830,120.00 USD | 0.00 USD | 1,150.00 USD | 6,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5445` | 330.14 USD | 86,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5460` | 683,420.00 USD | 683,420.00 USD | 5,050.00 USD | 298.25 USD | 990.37 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5460` | 822,000.00 USD | 822,000.00 USD | 2,250.00 USD | 3,030.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5480` | 677,080.00 USD | 677,080.00 USD | 0.00 USD | 633.67 USD | 14.03 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5480` | 811,530.00 USD | 811,530.00 USD | 2,000.00 USD | 795.70 USD | 4,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5495` | 630.26 USD | 85,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5500` | 676,430.00 USD | 676,430.00 USD | 0.00 USD | 0.00 USD | 7,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5500` | 804,260.00 USD | 804,260.00 USD | 5,990.00 USD | 1,440.00 USD | 6,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5520` | 669,210.00 USD | 669,210.00 USD | 0.00 USD | 0.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5520` | 790,120.00 USD | 790,120.00 USD | 4,110.00 USD | 1,920.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5535` | 1,660.00 USD | 85,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5540` | 667,930.00 USD | 667,930.00 USD | 1,790.00 USD | 1,320.00 USD | 7.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5540` | 782,200.00 USD | 782,200.00 USD | 12,840.00 USD | 4,860.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5545` | 47,580.00 USD | 83,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5560` | 664,810.00 USD | 664,810.00 USD | 557.27 USD | 201.08 USD | 520.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5560` | 746,040.00 USD | 746,040.00 USD | 13,490.00 USD | 1,920.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5580` | 663,530.00 USD | 663,530.00 USD | 1,100.00 USD | 4,900.00 USD | 3,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5580` | 724,380.00 USD | 724,380.00 USD | 6,000.00 USD | 6,820.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5585` | 10,520.00 USD | 35,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5600` | 653,970.00 USD | 653,970.00 USD | 1,550.00 USD | 1,830.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5600` | 693,260.00 USD | 693,260.00 USD | 4,070.00 USD | 8,160.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5615` | 211.33 USD | 25,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5620` | 649,130.00 USD | 649,130.00 USD | 715.25 USD | 1,230.00 USD | 1,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5620` | 678,530.00 USD | 678,530.00 USD | 19,480.00 USD | 7,420.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5640` | 645,600.00 USD | 645,600.00 USD | 0.00 USD | 3,980.00 USD | 4,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5640` | 640,090.00 USD | 640,090.00 USD | 2,950.00 USD | 741.21 USD | 27.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5660` | 636,370.00 USD | 636,370.00 USD | 11,490.00 USD | 2,990.00 USD | 4,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5680` | 617,470.00 USD | 617,470.00 USD | 5,100.00 USD | 0.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5700` | 609,480.00 USD | 609,480.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5715` | 289.08 USD | 25,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5720` | 637,030.00 USD | 637,030.00 USD | 0.00 USD | 2,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5720` | 606,900.00 USD | 606,900.00 USD | 0.00 USD | 4,370.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5725` | 4,880.00 USD | 24,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 767.96 USD | 20,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5740` | 601,170.00 USD | 601,170.00 USD | 21,620.00 USD | 1,100.00 USD | 1,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5745` | 6,550.00 USD | 19,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5760` | 576,830.00 USD | 576,830.00 USD | 2,150.00 USD | 0.00 USD | 19.23 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5780` | 634,680.00 USD | 634,680.00 USD | 0.00 USD | 0.00 USD | 94.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5780` | 574,660.00 USD | 574,660.00 USD | 0.00 USD | 0.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5800` | 573,090.00 USD | 573,090.00 USD | 1,610.00 USD | 0.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5820` | 634,580.00 USD | 634,580.00 USD | 0.00 USD | 1,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5820` | 568,640.00 USD | 568,640.00 USD | 0.00 USD | 0.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5835` | 188.28 USD | 12,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5840` | 633,580.00 USD | 633,580.00 USD | 0.00 USD | 0.00 USD | 47.28 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5845` | 210.96 USD | 12,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5860` | 633,540.00 USD | 633,540.00 USD | 0.00 USD | 658.88 USD | 14,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5860` | 562,120.00 USD | 562,120.00 USD | 0.00 USD | 0.00 USD | 146.30 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5865` | 1,260.00 USD | 12,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5880` | 618,000.00 USD | 618,000.00 USD | 4,160.00 USD | 2,210.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5880` | 561,970.00 USD | 561,970.00 USD | 3,110.00 USD | 1,400.00 USD | 65.70 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5885` | 440.16 USD | 11,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 1,840.00 USD | 10,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5900` | 604,440.00 USD | 604,440.00 USD | 8,190.00 USD | 1,390.00 USD | 11.26 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5900` | 557,400.00 USD | 557,400.00 USD | 3,120.00 USD | 1,560.00 USD | 15.37 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5905` | 1,950.00 USD | 8,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5920` | 594,860.00 USD | 594,860.00 USD | 11,320.00 USD | 4,470.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5920` | 552,700.00 USD | 552,700.00 USD | 11,690.00 USD | 2,820.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5925` | 609.14 USD | 6,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5940` | 567,190.00 USD | 567,190.00 USD | 9,310.00 USD | 8,970.00 USD | 15,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5940` | 532,160.00 USD | 532,160.00 USD | 10,090.00 USD | 0.00 USD | 9,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5955` | 3,850.00 USD | 6,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5960` | 533,050.00 USD | 533,050.00 USD | 27,990.00 USD | 12,850.00 USD | 15,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5960` | 512,290.00 USD | 512,290.00 USD | 18,180.00 USD | 18,410.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5980` | 476,980.00 USD | 476,980.00 USD | 10,420.00 USD | 8,800.00 USD | 45,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5980` | 462,320.00 USD | 462,320.00 USD | 20,380.00 USD | 826.53 USD | 19,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6000` | 412,350.00 USD | 412,350.00 USD | 18,690.00 USD | 7,050.00 USD | 9,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6000` | 421,190.00 USD | 421,190.00 USD | 3,320.00 USD | 2,140.00 USD | 18,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6005` | 852.06 USD | 2,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6015` | 995.49 USD | 1,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6020` | 377,480.00 USD | 377,480.00 USD | 21,590.00 USD | 13,700.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6020` | 396,920.00 USD | 396,920.00 USD | 23,960.00 USD | 8,040.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6035` | 507.36 USD | 507.36 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6040` | 330,790.00 USD | 330,790.00 USD | 19,460.00 USD | 7,680.00 USD | 46.43 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6040` | 360,860.00 USD | 360,860.00 USD | 8,620.00 USD | 7,530.00 USD | 7,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6060` | 303,590.00 USD | 303,590.00 USD | 8,500.00 USD | 6,650.00 USD | 28,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6060` | 336,790.00 USD | 336,790.00 USD | 0.00 USD | 0.00 USD | 227.43 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6080` | 260,330.00 USD | 260,330.00 USD | 10,660.00 USD | 37,840.00 USD | 11,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6080` | 336,560.00 USD | 336,560.00 USD | 2,860.00 USD | 0.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6100` | 200,600.00 USD | 200,600.00 USD | 10,380.00 USD | 17,750.00 USD | 14,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6100` | 324,330.00 USD | 324,330.00 USD | 21,400.00 USD | 47,430.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6120` | 158,230.00 USD | 158,230.00 USD | 25,010.00 USD | 0.00 USD | 8,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6120` | 230,190.00 USD | 230,190.00 USD | 35,760.00 USD | 5,720.00 USD | 18,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6140` | 124,930.00 USD | 124,930.00 USD | 35,500.00 USD | 30,510.00 USD | 22,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6140` | 170,200.00 USD | 170,200.00 USD | 51,550.00 USD | 8,040.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6160` | 36,140.00 USD | 36,140.00 USD | 17,390.00 USD | 4,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6160` | 99,830.00 USD | 99,830.00 USD | 12,920.00 USD | 16,340.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6180` | 13,910.00 USD | 13,910.00 USD | 0.00 USD | 0.00 USD | 13,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6180` | 65,810.00 USD | 65,810.00 USD | 20,870.00 USD | 2,610.00 USD | 228.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6200` | 42,100.00 USD | 42,100.00 USD | 23,430.00 USD | 0.00 USD | 18,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6220` | 20,540.00 USD | 20,540.00 USD | 1,990.00 USD | 18,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6220` | 27,620.00 USD | 27,620.00 USD | 4,760.00 USD | 22,640.00 USD | 215.59 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6240` | 27,790.00 USD | 27,790.00 USD | 0.00 USD | 0.00 USD | 171.81 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6260` | 95,110.00 USD | 95,110.00 USD | 67,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6300` | 105,020.00 USD | 105,020.00 USD | 0.00 USD | 0.00 USD | 9,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6320` | 81,480.00 USD | 81,480.00 USD | 45,660.00 USD | 3,970.00 USD | 11,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6320` | 105,390.00 USD | 105,390.00 USD | 0.00 USD | 0.00 USD | 369.35 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6340` | 185,580.00 USD | 185,580.00 USD | 39,290.00 USD | 0.00 USD | 64,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6340` | 174,440.00 USD | 174,440.00 USD | 68,660.00 USD | 0.00 USD | 381.22 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6360` | 360,430.00 USD | 360,430.00 USD | 114,380.00 USD | 0.00 USD | 60,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6360` | 265,740.00 USD | 265,740.00 USD | 34,320.00 USD | 0.00 USD | 56,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6380` | 420,550.00 USD | 420,550.00 USD | 0.00 USD | 24,790.00 USD | 35,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6380` | 304,820.00 USD | 304,820.00 USD | 0.00 USD | 0.00 USD | 39,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6400` | 581,870.00 USD | 581,870.00 USD | 55,850.00 USD | 31,730.00 USD | 73,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6400` | 325,340.00 USD | 325,340.00 USD | 0.00 USD | 7,510.00 USD | 13,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6420` | 708,140.00 USD | 708,140.00 USD | 79,430.00 USD | 20,170.00 USD | 26,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6420` | 432,660.00 USD | 432,660.00 USD | 55,350.00 USD | 35,430.00 USD | 16,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6440` | 899,810.00 USD | 899,810.00 USD | 75,460.00 USD | 39,300.00 USD | 76,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6440` | 520,040.00 USD | 520,040.00 USD | 44,690.00 USD | 24,820.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6460` | 1,090,000.00 USD | 1,090,000.00 USD | 127,650.00 USD | 16,540.00 USD | 43,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6460` | 877,570.00 USD | 877,570.00 USD | 172,610.00 USD | 46,630.00 USD | 138,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6480` | 1,290,000.00 USD | 1,290,000.00 USD | 181,680.00 USD | 22,790.00 USD | 174.56 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6480` | 1,020,000.00 USD | 1,020,000.00 USD | 86,440.00 USD | 26,520.00 USD | 33,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6500` | 1,430,000.00 USD | 1,430,000.00 USD | 131,750.00 USD | 5,920.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6500` | 1,230,000.00 USD | 1,230,000.00 USD | 73,560.00 USD | 0.00 USD | 132,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6520` | 1,590,000.00 USD | 1,590,000.00 USD | 139,000.00 USD | 9,040.00 USD | 11,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6520` | 1,640,000.00 USD | 1,640,000.00 USD | 298,050.00 USD | 10,910.00 USD | 104,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6540` | 1,630,000.00 USD | 1,630,000.00 USD | 24,560.00 USD | 2,420.00 USD | 10,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6540` | 1,730,000.00 USD | 1,730,000.00 USD | 15,730.00 USD | 4,440.00 USD | 61,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6560` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 14,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6560` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 5,380.00 USD | 847.61 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6580` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 3,310.00 USD | 30.58 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6580` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 28,280.00 USD | 9,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6600` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 14,280.00 USD | 223.65 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6600` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 15,500.00 USD | 580.13 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6620` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 7,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6620` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 128.16 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6625` | 1,050.00 USD | 1,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6640` | 1,680,000.00 USD | 1,680,000.00 USD | 11,190.00 USD | 0.00 USD | 165.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6640` | 1,820,000.00 USD | 1,820,000.00 USD | 33,660.00 USD | 0.00 USD | 534.34 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6660` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 3,160.00 USD | 22,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6660` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 6,770.00 USD | 436.87 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6680` | 1,730,000.00 USD | 1,730,000.00 USD | 18,850.00 USD | 0.00 USD | 47.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6680` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 308.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6700` | 1,770,000.00 USD | 1,770,000.00 USD | 8,830.00 USD | 5,470.00 USD | 29,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6700` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 966.49 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6720` | 1,820,000.00 USD | 1,820,000.00 USD | 41,970.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6720` | 1,920,000.00 USD | 1,920,000.00 USD | 58,470.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6740` | 1,930,000.00 USD | 1,930,000.00 USD | 88,690.00 USD | 10,790.00 USD | 13,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6740` | 1,960,000.00 USD | 1,960,000.00 USD | 39,730.00 USD | 0.00 USD | 99.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6760` | 2,000,000.00 USD | 2,000,000.00 USD | 40,550.00 USD | 11,820.00 USD | 12,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6760` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 77,970.00 USD | 33,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6780` | 2,090,000.00 USD | 2,090,000.00 USD | 48,140.00 USD | 18,790.00 USD | 23,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6780` | 2,160,000.00 USD | 2,160,000.00 USD | 63,600.00 USD | 14,400.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6800` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 18,610.00 USD | 17,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6800` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 16,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6820` | 2,180,000.00 USD | 2,180,000.00 USD | 22,600.00 USD | 18,530.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6820` | 2,270,000.00 USD | 2,270,000.00 USD | 32,570.00 USD | 53,450.00 USD | 145.79 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6840` | 2,350,000.00 USD | 2,350,000.00 USD | 70,350.00 USD | 51,350.00 USD | 48,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6840` | 2,480,000.00 USD | 2,480,000.00 USD | 57,890.00 USD | 54,300.00 USD | 102,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6860` | 2,480,000.00 USD | 2,480,000.00 USD | 91,340.00 USD | 10,160.00 USD | 23,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6860` | 2,560,000.00 USD | 2,560,000.00 USD | 49,930.00 USD | 14,540.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6880` | 2,600,000.00 USD | 2,600,000.00 USD | 77,570.00 USD | 12,320.00 USD | 35,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6880` | 2,610,000.00 USD | 2,610,000.00 USD | 38,030.00 USD | 17,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6900` | 2,650,000.00 USD | 2,650,000.00 USD | 14,580.00 USD | 4,030.00 USD | 28,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6900` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 15,510.00 USD | 16,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6920` | 2,750,000.00 USD | 2,750,000.00 USD | 45,660.00 USD | 1,730.00 USD | 53,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6920` | 2,780,000.00 USD | 2,780,000.00 USD | 69,620.00 USD | 2,090.00 USD | 62,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6940` | 2,780,000.00 USD | 2,780,000.00 USD | 21,260.00 USD | 2,090.00 USD | 9,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6940` | 2,830,000.00 USD | 2,830,000.00 USD | 14,220.00 USD | 0.00 USD | 42,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6960` | 2,880,000.00 USD | 2,880,000.00 USD | 80,850.00 USD | 10,460.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6960` | 2,910,000.00 USD | 2,910,000.00 USD | 59,960.00 USD | 0.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6980` | 2,930,000.00 USD | 2,930,000.00 USD | 42,600.00 USD | 8,880.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6980` | 2,960,000.00 USD | 2,960,000.00 USD | 35,980.00 USD | 16,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7000` | 2,980,000.00 USD | 2,980,000.00 USD | 23,420.00 USD | 8,850.00 USD | 21,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7000` | 3,030,000.00 USD | 3,030,000.00 USD | 29,740.00 USD | 0.00 USD | 40,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7020` | 3,010,000.00 USD | 3,010,000.00 USD | 29,880.00 USD | 0.00 USD | 95.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7020` | 3,110,000.00 USD | 3,110,000.00 USD | 29,810.00 USD | 0.00 USD | 53,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7040` | 3,070,000.00 USD | 3,070,000.00 USD | 34,260.00 USD | 2,630.00 USD | 19,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7040` | 3,300,000.00 USD | 3,300,000.00 USD | 95,520.00 USD | 0.00 USD | 96,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7060` | 3,150,000.00 USD | 3,150,000.00 USD | 38,380.00 USD | 6,520.00 USD | 32,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7060` | 3,560,000.00 USD | 3,560,000.00 USD | 47,840.00 USD | 33,490.00 USD | 178,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7080` | 3,230,000.00 USD | 3,230,000.00 USD | 38,400.00 USD | 25,370.00 USD | 21,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7080` | 3,740,000.00 USD | 3,740,000.00 USD | 24,440.00 USD | 64,870.00 USD | 82,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7100` | 3,280,000.00 USD | 3,280,000.00 USD | 26,310.00 USD | 4,440.00 USD | 14,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7100` | 4,100,000.00 USD | 4,100,000.00 USD | 150,830.00 USD | 63,530.00 USD | 148,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7120` | 3,340,000.00 USD | 3,340,000.00 USD | 24,360.00 USD | 14,170.00 USD | 25,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7120` | 4,510,000.00 USD | 4,510,000.00 USD | 101,040.00 USD | 78,760.00 USD | 228,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7140` | 3,440,000.00 USD | 3,440,000.00 USD | 46,910.00 USD | 9,020.00 USD | 39,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7140` | 4,910,000.00 USD | 4,910,000.00 USD | 202,560.00 USD | 67,260.00 USD | 133,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7160` | 3,520,000.00 USD | 3,520,000.00 USD | 35,660.00 USD | 16,790.00 USD | 33,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7160` | 5,250,000.00 USD | 5,250,000.00 USD | 113,040.00 USD | 65,260.00 USD | 164,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7180` | 3,570,000.00 USD | 3,570,000.00 USD | 11,150.00 USD | 7,400.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7180` | 5,540,000.00 USD | 5,540,000.00 USD | 165,860.00 USD | 56,910.00 USD | 66,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7200` | 3,590,000.00 USD | 3,590,000.00 USD | 12,780.00 USD | 3,000.00 USD | 7,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7200` | 5,860,000.00 USD | 5,860,000.00 USD | 93,750.00 USD | 45,160.00 USD | 177,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7220` | 3,630,000.00 USD | 3,630,000.00 USD | 17,280.00 USD | 13,330.00 USD | 8,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7220` | 6,340,000.00 USD | 6,340,000.00 USD | 318,420.00 USD | 67,130.00 USD | 98,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7240` | 3,660,000.00 USD | 3,660,000.00 USD | 12,450.00 USD | 6,350.00 USD | 11,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7240` | 6,640,000.00 USD | 6,640,000.00 USD | 146,110.00 USD | 24,910.00 USD | 128,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7255` | 124.05 USD | 1,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7260` | 3,710,000.00 USD | 3,710,000.00 USD | 21,500.00 USD | 5,000.00 USD | 22,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7260` | 6,980,000.00 USD | 6,980,000.00 USD | 106,410.00 USD | 52,120.00 USD | 175,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7280` | 3,790,000.00 USD | 3,790,000.00 USD | 50,390.00 USD | 6,280.00 USD | 21,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7280` | 7,200,000.00 USD | 7,200,000.00 USD | 99,750.00 USD | 40,180.00 USD | 83,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7295` | 43,330.00 USD | 44,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7300` | 3,850,000.00 USD | 3,850,000.00 USD | 23,130.00 USD | 12,630.00 USD | 32,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7300` | 7,480,000.00 USD | 7,480,000.00 USD | 115,310.00 USD | 60,310.00 USD | 109,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7320` | 3,880,000.00 USD | 3,880,000.00 USD | 13,500.00 USD | 2,810.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7320` | 7,820,000.00 USD | 7,820,000.00 USD | 189,840.00 USD | 65,640.00 USD | 80,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7340` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 3,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7340` | 7,920,000.00 USD | 7,920,000.00 USD | 31,260.00 USD | 8,620.00 USD | 63,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7360` | 3,900,000.00 USD | 3,900,000.00 USD | 7,970.00 USD | 4,660.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7360` | 8,110,000.00 USD | 8,110,000.00 USD | 103,600.00 USD | 46,790.00 USD | 35,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7380` | 3,920,000.00 USD | 3,920,000.00 USD | 12,130.00 USD | 5,260.00 USD | 5,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7380` | 8,260,000.00 USD | 8,260,000.00 USD | 73,710.00 USD | 19,000.00 USD | 60,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7400` | 3,930,000.00 USD | 3,930,000.00 USD | 8,500.00 USD | 2,360.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7400` | 8,300,000.00 USD | 8,300,000.00 USD | 1,730.00 USD | 4,760.00 USD | 27,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7420` | 8,410,000.00 USD | 8,410,000.00 USD | 35,810.00 USD | 41,830.00 USD | 31,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7440` | 8,590,000.00 USD | 8,590,000.00 USD | 74,450.00 USD | 39,890.00 USD | 70,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7460` | 8,760,000.00 USD | 8,760,000.00 USD | 88,800.00 USD | 28,800.00 USD | 51,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7480` | 8,890,000.00 USD | 8,890,000.00 USD | 60,580.00 USD | 28,900.00 USD | 38,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7500` | 8,980,000.00 USD | 8,980,000.00 USD | 52,320.00 USD | 12,610.00 USD | 25,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7520` | 9,100,000.00 USD | 9,100,000.00 USD | 53,470.00 USD | 13,000.00 USD | 50,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7540` | 9,150,000.00 USD | 9,150,000.00 USD | 30,340.00 USD | 1,890.00 USD | 25,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7560` | 9,210,000.00 USD | 9,210,000.00 USD | 26,000.00 USD | 7,570.00 USD | 22,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7580` | 9,320,000.00 USD | 9,320,000.00 USD | 55,420.00 USD | 11,790.00 USD | 45,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7600` | 9,460,000.00 USD | 9,460,000.00 USD | 57,020.00 USD | 4,320.00 USD | 80,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7620` | 9,560,000.00 USD | 9,560,000.00 USD | 54,140.00 USD | 24,170.00 USD | 21,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7640` | 9,670,000.00 USD | 9,670,000.00 USD | 50,390.00 USD | 13,520.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7660` | 9,830,000.00 USD | 9,830,000.00 USD | 56,130.00 USD | 18,130.00 USD | 91,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7680` | 9,970,000.00 USD | 9,970,000.00 USD | 66,570.00 USD | 32,520.00 USD | 41,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7700` | 10,040,000.00 USD | 10,040,000.00 USD | 10,860.00 USD | 12,600.00 USD | 41,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7720` | 10,160,000.00 USD | 10,160,000.00 USD | 58,380.00 USD | 32,920.00 USD | 25,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7725` | 165.62 USD | 44,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7740` | 10,270,000.00 USD | 10,270,000.00 USD | 51,600.00 USD | 25,250.00 USD | 35,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7760` | 10,320,000.00 USD | 10,320,000.00 USD | 38,170.00 USD | 2,980.00 USD | 12,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7765` | 330.78 USD | 45,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7780` | 10,450,000.00 USD | 10,450,000.00 USD | 68,800.00 USD | 20,860.00 USD | 32,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7800` | 10,610,000.00 USD | 10,610,000.00 USD | 60,490.00 USD | 21,940.00 USD | 80,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7820` | 10,720,000.00 USD | 10,720,000.00 USD | 90,020.00 USD | 17,850.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7840` | 10,830,000.00 USD | 10,830,000.00 USD | 95,370.00 USD | 7,150.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7860` | 10,910,000.00 USD | 10,910,000.00 USD | 32,690.00 USD | 9,290.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7880` | 10,970,000.00 USD | 10,970,000.00 USD | 11,900.00 USD | 22,650.00 USD | 22,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7900` | 11,060,000.00 USD | 11,060,000.00 USD | 59,120.00 USD | 16,710.00 USD | 17,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7910` | 11,100,000.00 USD | 11,100,000.00 USD | 30,620.00 USD | 5,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8005` | 19,120.00 USD | 64,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8515` | 428.27 USD | 64,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8665` | 378.95 USD | 64,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8725` | 11,700.00 USD | 76,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9345` | 24,680.00 USD | 101,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9805` | 17,300.00 USD | 118,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9935` | 166.01 USD | 118,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 479.74 USD | 119,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.12` | 2,800.00 USD | 122,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 85,880.00 USD | 207,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.17` | 501.44 USD | 208,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1395` | 310,430.00 USD | 0.00 USD | 419.65 USD | `-77.62%` | `3,008.22` |
| `Live` | `Long` | `0.1445` | 310,010.00 USD | 0.00 USD | 200.61 USD | `-76.81%` | `1,388.32` |
| `Live` | `Long` | `0.1875` | 309,810.00 USD | 0.00 USD | 269.27 USD | `-69.91%` | `1,436.09` |
| `Live` | `Long` | `0.2035` | 309,540.00 USD | 0.00 USD | 1,480.00 USD | `-67.35%` | `7,272.07` |
| `Live` | `Long` | `0.2065` | 308,060.00 USD | 0.00 USD | 207.79 USD | `-66.86%` | `1,006.27` |
| `Live` | `Long` | `0.2225` | 307,860.00 USD | 0.00 USD | 230.98 USD | `-64.30%` | `1,038.12` |
| `Live` | `Long` | `0.2235` | 307,620.00 USD | 0.00 USD | 2,520.00 USD | `-64.14%` | `11,284.25` |
| `Live` | `Long` | `0.2425` | 305,100.00 USD | 0.00 USD | 1,460.00 USD | `-61.09%` | `6,000.00` |
| `Live` | `Long` | `0.2545` | 303,650.00 USD | 0.00 USD | 32,830.00 USD | `-59.16%` | `129,000.00` |
| `Live` | `Long` | `0.3175` | 270,820.00 USD | 0.00 USD | 1,590.00 USD | `-49.05%` | `5,000.00` |
| `Live` | `Long` | `0.3255` | 269,230.00 USD | 0.00 USD | 9,260.00 USD | `-47.77%` | `28,446.85` |
| `Live` | `Long` | `0.3265` | 259,970.00 USD | 0.00 USD | 149.84 USD | `-47.61%` | `458.93` |
| `Live` | `Long` | `0.3305` | 259,820.00 USD | 0.00 USD | 543.58 USD | `-46.97%` | `1,644.73` |
| `Live` | `Long` | `0.3365` | 259,280.00 USD | 0.00 USD | 25,600.00 USD | `-46.00%` | `76,064.38` |
| `Live` | `Long` | `0.3545` | 233,680.00 USD | 0.00 USD | 177.25 USD | `-43.12%` | `500.00` |
| `Live` | `Long` | `0.3665` | 233,500.00 USD | 0.00 USD | 189.47 USD | `-41.19%` | `516.98` |
| `Live` | `Long` | `0.3805` | 233,310.00 USD | 0.00 USD | 570.75 USD | `-38.94%` | `1,500.00` |
| `Live` | `Long` | `0.3895` | 232,740.00 USD | 0.00 USD | 272.65 USD | `-37.50%` | `700.00` |
| `Live` | `Long` | `0.3905` | 232,470.00 USD | 0.00 USD | 359.26 USD | `-37.34%` | `919.99` |
| `Live` | `Long` | `0.3955` | 232,110.00 USD | 0.00 USD | 2,640.00 USD | `-36.54%` | `6,686.27` |
| `Live` | `Long` | `0.3995` | 229,470.00 USD | 0.00 USD | 5,240.00 USD | `-35.90%` | `13,104.64` |
| `Live` | `Long` | `0.4035` | 224,230.00 USD | 0.00 USD | 570.81 USD | `-35.25%` | `1,414.65` |
| `Live` | `Long` | `0.4045` | 223,660.00 USD | 0.00 USD | 404.50 USD | `-35.09%` | `1,000.00` |
| `Live` | `Long` | `0.4135` | 223,260.00 USD | 0.00 USD | 1,600.00 USD | `-33.65%` | `3,868.97` |
| `Live` | `Long` | `0.4185` | 221,660.00 USD | 0.00 USD | 630.86 USD | `-32.85%` | `1,507.44` |
| `Live` | `Long` | `0.4255` | 221,030.00 USD | 0.00 USD | 655.75 USD | `-31.72%` | `1,541.13` |
| `Live` | `Long` | `0.4275` | 220,370.00 USD | 0.00 USD | 3,950.00 USD | `-31.40%` | `9,243.24` |
| `Live` | `Long` | `0.4405` | 216,420.00 USD | 0.00 USD | 4,300.00 USD | `-29.32%` | `9,753.33` |
| `Live` | `Long` | `0.4425` | 212,120.00 USD | 0.00 USD | 101.06 USD | `-29.00%` | `228.39` |
| `Live` | `Long` | `0.4445` | 212,020.00 USD | 0.00 USD | 6,490.00 USD | `-28.67%` | `14,594.79` |
| `Live` | `Long` | `0.4475` | 205,530.00 USD | 0.00 USD | 226.63 USD | `-28.19%` | `506.43` |
| `Live` | `Long` | `0.4515` | 205,310.00 USD | 0.00 USD | 27,090.00 USD | `-27.55%` | `60,000.00` |
| `Live` | `Long` | `0.4575` | 178,220.00 USD | 0.00 USD | 112.72 USD | `-26.59%` | `246.38` |
| `Live` | `Long` | `0.4605` | 178,100.00 USD | 0.00 USD | 125.38 USD | `-26.11%` | `272.27` |
| `Live` | `Long` | `0.4615` | 177,980.00 USD | 0.00 USD | 830.07 USD | `-25.95%` | `1,798.64` |
| `Live` | `Long` | `0.4625` | 177,150.00 USD | 0.00 USD | 1,680.00 USD | `-25.79%` | `3,622.78` |
| `Live` | `Long` | `0.4635` | 175,470.00 USD | 0.00 USD | 273.41 USD | `-25.63%` | `589.89` |
| `Live` | `Long` | `0.4645` | 175,200.00 USD | 0.00 USD | 876.05 USD | `-25.47%` | `1,886.00` |
| `Live` | `Long` | `0.4685` | 174,320.00 USD | 0.00 USD | 468.50 USD | `-24.82%` | `1,000.00` |
| `Live` | `Long` | `0.4715` | 173,860.00 USD | 0.00 USD | 887.06 USD | `-24.34%` | `1,881.36` |
| `Live` | `Long` | `0.4755` | 172,970.00 USD | 0.00 USD | 325.64 USD | `-23.70%` | `684.84` |
| `Live` | `Long` | `0.4835` | 172,640.00 USD | 0.00 USD | 135.33 USD | `-22.42%` | `279.90` |
| `Live` | `Long` | `0.4865` | 172,510.00 USD | 0.00 USD | 3,170.00 USD | `-21.94%` | `6,508.47` |
| `Live` | `Long` | `0.4895` | 169,340.00 USD | 0.00 USD | 1,220.00 USD | `-21.45%` | `2,500.00` |
| `Live` | `Long` | `0.4955` | 168,120.00 USD | 0.00 USD | 3,180.00 USD | `-20.49%` | `6,422.59` |
| `Live` | `Long` | `0.4975` | 164,930.00 USD | 0.00 USD | 168.65 USD | `-20.17%` | `339.00` |
| `Live` | `Long` | `0.4985` | 164,770.00 USD | 0.00 USD | 429.90 USD | `-20.01%` | `862.38` |
| `Live` | `Long` | `0.5085` | 164,340.00 USD | 0.00 USD | 102.82 USD | `-18.41%` | `202.20` |
| `Live` | `Long` | `0.5125` | 164,230.00 USD | 0.00 USD | 248.05 USD | `-17.76%` | `484.00` |
| `Live` | `Long` | `0.5135` | 163,990.00 USD | 0.00 USD | 110.50 USD | `-17.60%` | `215.19` |
| `Live` | `Long` | `0.5145` | 163,870.00 USD | 0.00 USD | 288.78 USD | `-17.44%` | `561.28` |
| `Live` | `Long` | `0.5175` | 163,590.00 USD | 0.00 USD | 9,440.00 USD | `-16.96%` | `18,249.92` |
| `Live` | `Long` | `0.5225` | 154,140.00 USD | 0.00 USD | 11,160.00 USD | `-16.16%` | `21,364.96` |
| `Live` | `Long` | `0.5245` | 142,980.00 USD | 0.00 USD | 3,780.00 USD | `-15.84%` | `7,212.35` |
| `Live` | `Long` | `0.5295` | 139,200.00 USD | 0.00 USD | 39,070.00 USD | `-15.04%` | `73,785.90` |
| `Live` | `Long` | `0.5315` | 100,130.00 USD | 0.00 USD | 12,360.00 USD | `-14.71%` | `23,252.00` |
| `Live` | `Long` | `0.5335` | 87,770.00 USD | 0.00 USD | 374.06 USD | `-14.39%` | `701.14` |
| `Live` | `Long` | `0.5355` | 87,390.00 USD | 0.00 USD | 1,110.00 USD | `-14.07%` | `2,078.06` |
| `Live` | `Long` | `0.5425` | 86,280.00 USD | 0.00 USD | 156.46 USD | `-12.95%` | `288.40` |
| `Live` | `Long` | `0.5445` | 86,120.00 USD | 0.00 USD | 330.14 USD | `-12.63%` | `606.32` |
| `Live` | `Long` | `0.5495` | 85,790.00 USD | 0.00 USD | 630.26 USD | `-11.83%` | `1,146.97` |
| `Live` | `Long` | `0.5535` | 85,160.00 USD | 0.00 USD | 1,660.00 USD | `-11.18%` | `3,002.78` |
| `Live` | `Long` | `0.5545` | 83,500.00 USD | 0.00 USD | 47,580.00 USD | `-11.02%` | `85,806.96` |
| `Live` | `Long` | `0.5585` | 35,920.00 USD | 0.00 USD | 10,520.00 USD | `-10.38%` | `18,834.52` |
| `Live` | `Long` | `0.5615` | 25,400.00 USD | 0.00 USD | 211.33 USD | `-9.90%` | `376.36` |
| `Live` | `Long` | `0.5715` | 25,190.00 USD | 0.00 USD | 289.08 USD | `-8.30%` | `505.82` |
| `Live` | `Long` | `0.5725` | 24,900.00 USD | 0.00 USD | 4,880.00 USD | `-8.14%` | `8,530.92` |
| `Live` | `Long` | `0.5735` | 20,020.00 USD | 0.00 USD | 767.96 USD | `-7.97%` | `1,339.07` |
| `Live` | `Long` | `0.5745` | 19,250.00 USD | 0.00 USD | 6,550.00 USD | `-7.81%` | `11,392.84` |
| `Live` | `Long` | `0.5835` | 12,710.00 USD | 0.00 USD | 188.28 USD | `-6.37%` | `322.68` |
| `Live` | `Long` | `0.5845` | 12,520.00 USD | 0.00 USD | 210.96 USD | `-6.21%` | `360.92` |
| `Live` | `Long` | `0.5865` | 12,310.00 USD | 0.00 USD | 1,260.00 USD | `-5.89%` | `2,142.98` |
| `Live` | `Long` | `0.5885` | 11,050.00 USD | 0.00 USD | 440.16 USD | `-5.57%` | `747.93` |
| `Live` | `Long` | `0.5895` | 10,610.00 USD | 0.00 USD | 1,840.00 USD | `-5.41%` | `3,127.08` |
| `Live` | `Long` | `0.5905` | 8,770.00 USD | 0.00 USD | 1,950.00 USD | `-5.25%` | `3,302.26` |
| `Live` | `Long` | `0.5925` | 6,820.00 USD | 0.00 USD | 609.14 USD | `-4.93%` | `1,028.09` |
| `Live` | `Long` | `0.5955` | 6,210.00 USD | 0.00 USD | 3,850.00 USD | `-4.44%` | `6,467.73` |
| `Live` | `Long` | `0.6005` | 2,350.00 USD | 0.00 USD | 852.06 USD | `-3.64%` | `1,418.92` |
| `Live` | `Long` | `0.6015` | 1,500.00 USD | 0.00 USD | 995.49 USD | `-3.48%` | `1,655.01` |
| `Live` | `Long` | `0.6035` | 507.36 USD | 0.00 USD | 507.36 USD | `-3.16%` | `840.70` |
| `Live` | `Short` | `0.6625` | 1,050.00 USD | 1,050.00 USD | 0.00 USD | `+6.31%` | `1,591.60` |
| `Live` | `Short` | `0.7255` | 1,180.00 USD | 124.05 USD | 0.00 USD | `+16.42%` | `170.98` |
| `Live` | `Short` | `0.7295` | 44,510.00 USD | 43,330.00 USD | 0.00 USD | `+17.06%` | `59,401.36` |
| `Live` | `Short` | `0.7725` | 44,680.00 USD | 165.62 USD | 0.00 USD | `+23.96%` | `214.40` |
| `Live` | `Short` | `0.7765` | 45,010.00 USD | 330.78 USD | 0.00 USD | `+24.60%` | `425.99` |
| `Live` | `Short` | `0.8005` | 64,130.00 USD | 19,120.00 USD | 0.00 USD | `+28.45%` | `23,882.80` |
| `Live` | `Short` | `0.8515` | 64,550.00 USD | 428.27 USD | 0.00 USD | `+36.63%` | `502.96` |
| `Live` | `Short` | `0.8665` | 64,930.00 USD | 378.95 USD | 0.00 USD | `+39.04%` | `437.33` |
| `Live` | `Short` | `0.8725` | 76,630.00 USD | 11,700.00 USD | 0.00 USD | `+40.00%` | `13,408.98` |
| `Live` | `Short` | `0.9345` | 101,310.00 USD | 24,680.00 USD | 0.00 USD | `+49.95%` | `26,406.53` |
| `Live` | `Short` | `0.9805` | 118,610.00 USD | 17,300.00 USD | 0.00 USD | `+57.33%` | `17,648.14` |
| `Live` | `Short` | `0.9935` | 118,780.00 USD | 166.01 USD | 0.00 USD | `+59.42%` | `167.10` |
| `Live` | `Short` | `1.09` | 119,260.00 USD | 479.74 USD | 0.00 USD | `+75.14%` | `439.52` |
| `Live` | `Short` | `1.12` | 122,060.00 USD | 2,800.00 USD | 0.00 USD | `+79.64%` | `2,500.00` |
| `Live` | `Short` | `1.13` | 207,930.00 USD | 85,880.00 USD | 0.00 USD | `+80.60%` | `76,300.00` |
| `Live` | `Short` | `1.17` | 208,440.00 USD | 501.44 USD | 0.00 USD | `+88.30%` | `427.30` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.3505` | 86,630.00 USD | 0.00 USD | 340.19 USD | `-43.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4635` | 86,290.00 USD | 0.00 USD | 104.57 USD | `-25.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4805` | 86,180.00 USD | 0.00 USD | 14,740.00 USD | `-22.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 71,440.00 USD | 0.00 USD | 604.46 USD | `-19.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5085` | 70,840.00 USD | 0.00 USD | 101.97 USD | `-18.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5125` | 70,730.00 USD | 0.00 USD | 5,380.00 USD | `-17.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5205` | 65,350.00 USD | 0.00 USD | 228.77 USD | `-16.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5305` | 65,120.00 USD | 0.00 USD | 770.19 USD | `-14.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5445` | 64,350.00 USD | 0.00 USD | 8,750.00 USD | `-12.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5455` | 55,600.00 USD | 0.00 USD | 8,150.00 USD | `-12.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5485` | 47,450.00 USD | 0.00 USD | 4,500.00 USD | `-11.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5515` | 42,950.00 USD | 0.00 USD | 126.71 USD | `-11.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5525` | 42,830.00 USD | 0.00 USD | 126.90 USD | `-11.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5555` | 42,700.00 USD | 0.00 USD | 33,000.00 USD | `-10.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5565` | 9,700.00 USD | 0.00 USD | 173.58 USD | `-10.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5595` | 9,530.00 USD | 0.00 USD | 127.61 USD | `-10.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 9,400.00 USD | 0.00 USD | 339.84 USD | `-10.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5625` | 9,060.00 USD | 0.00 USD | 126.55 USD | `-9.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5655` | 8,940.00 USD | 0.00 USD | 127.62 USD | `-9.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5695` | 8,810.00 USD | 0.00 USD | 127.30 USD | `-8.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5715` | 8,680.00 USD | 0.00 USD | 127.63 USD | `-8.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5735` | 8,550.00 USD | 0.00 USD | 151.62 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5755` | 8,400.00 USD | 0.00 USD | 127.29 USD | `-7.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5785` | 8,270.00 USD | 0.00 USD | 127.36 USD | `-7.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5815` | 8,150.00 USD | 0.00 USD | 127.27 USD | `-6.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5835` | 8,020.00 USD | 0.00 USD | 178.88 USD | `-6.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5845` | 7,840.00 USD | 0.00 USD | 127.33 USD | `-6.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5865` | 7,710.00 USD | 0.00 USD | 128.36 USD | `-5.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5875` | 7,580.00 USD | 0.00 USD | 128.34 USD | `-5.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5895` | 7,460.00 USD | 0.00 USD | 128.45 USD | `-5.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5905` | 7,330.00 USD | 0.00 USD | 127.30 USD | `-5.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5925` | 7,200.00 USD | 0.00 USD | 265.69 USD | `-4.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5975` | 6,930.00 USD | 0.00 USD | 784.58 USD | `-4.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 6,150.00 USD | 0.00 USD | 953.02 USD | `-3.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 5,200.00 USD | 0.00 USD | 1,510.00 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6065` | 3,690.00 USD | 0.00 USD | 1,910.00 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6085` | 1,780.00 USD | 0.00 USD | 301.32 USD | `-2.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6135` | 1,480.00 USD | 0.00 USD | 242.45 USD | `-1.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6175` | 1,240.00 USD | 0.00 USD | 519.13 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6185` | 718.99 USD | 0.00 USD | 177.58 USD | `-0.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 541.40 USD | 0.00 USD | 541.40 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6275` | 433.11 USD | 433.11 USD | 0.00 USD | `+0.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6285` | 903.04 USD | 469.94 USD | 0.00 USD | `+0.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 5,330.00 USD | 4,430.00 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6315` | 5,490.00 USD | 160.16 USD | 0.00 USD | `+1.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 6,480.00 USD | 987.19 USD | 0.00 USD | `+1.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6335` | 14,870.00 USD | 8,390.00 USD | 0.00 USD | `+1.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6345` | 15,150.00 USD | 276.40 USD | 0.00 USD | `+1.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6395` | 16,350.00 USD | 1,200.00 USD | 0.00 USD | `+2.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6405` | 16,490.00 USD | 145.91 USD | 0.00 USD | `+2.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6445` | 16,610.00 USD | 121.42 USD | 0.00 USD | `+3.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6465` | 17,020.00 USD | 410.21 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6485` | 17,470.00 USD | 447.03 USD | 0.00 USD | `+4.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6505` | 18,040.00 USD | 567.58 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6525` | 18,150.00 USD | 111.92 USD | 0.00 USD | `+4.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6535` | 18,500.00 USD | 349.76 USD | 0.00 USD | `+4.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6555` | 22,580.00 USD | 4,080.00 USD | 0.00 USD | `+5.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6565` | 22,860.00 USD | 284.88 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6585` | 24,300.00 USD | 1,440.00 USD | 0.00 USD | `+5.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6595` | 25,050.00 USD | 746.46 USD | 0.00 USD | `+5.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6605` | 25,630.00 USD | 580.23 USD | 0.00 USD | `+5.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6645` | 25,890.00 USD | 262.60 USD | 0.00 USD | `+6.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6655` | 26,180.00 USD | 283.50 USD | 0.00 USD | `+6.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6675` | 26,470.00 USD | 290.78 USD | 0.00 USD | `+7.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6685` | 26,640.00 USD | 170.95 USD | 0.00 USD | `+7.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6695` | 28,310.00 USD | 1,670.00 USD | 0.00 USD | `+7.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6705` | 28,470.00 USD | 162.91 USD | 0.00 USD | `+7.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6715` | 28,670.00 USD | 202.63 USD | 0.00 USD | `+7.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6725` | 30,350.00 USD | 1,670.00 USD | 0.00 USD | `+7.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6745` | 30,940.00 USD | 598.31 USD | 0.00 USD | `+8.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6755` | 31,310.00 USD | 361.53 USD | 0.00 USD | `+8.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 33,430.00 USD | 2,130.00 USD | 0.00 USD | `+8.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6805` | 33,650.00 USD | 214.20 USD | 0.00 USD | `+9.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6815` | 44,210.00 USD | 10,560.00 USD | 0.00 USD | `+9.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6825` | 44,320.00 USD | 112.49 USD | 0.00 USD | `+9.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6835` | 44,430.00 USD | 108.41 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6855` | 44,540.00 USD | 112.98 USD | 0.00 USD | `+10.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6865` | 44,830.00 USD | 292.33 USD | 0.00 USD | `+10.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6875` | 44,970.00 USD | 140.41 USD | 0.00 USD | `+10.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6885` | 45,490.00 USD | 514.80 USD | 0.00 USD | `+10.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6895` | 45,680.00 USD | 194.09 USD | 0.00 USD | `+10.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6915` | 45,780.00 USD | 101.96 USD | 0.00 USD | `+10.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6925` | 46,810.00 USD | 1,020.00 USD | 0.00 USD | `+11.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6945` | 47,420.00 USD | 610.10 USD | 0.00 USD | `+11.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6955` | 47,520.00 USD | 101.38 USD | 0.00 USD | `+11.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6965` | 48,310.00 USD | 789.18 USD | 0.00 USD | `+11.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6985` | 48,410.00 USD | 102.99 USD | 0.00 USD | `+12.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7005` | 48,520.00 USD | 111.08 USD | 0.00 USD | `+12.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7015` | 49,080.00 USD | 561.40 USD | 0.00 USD | `+12.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7085` | 50,030.00 USD | 947.29 USD | 0.00 USD | `+13.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7095` | 50,160.00 USD | 132.99 USD | 0.00 USD | `+13.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7115` | 50,280.00 USD | 122.04 USD | 0.00 USD | `+14.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7135` | 50,590.00 USD | 307.58 USD | 0.00 USD | `+14.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7165` | 52,430.00 USD | 1,830.00 USD | 0.00 USD | `+14.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7195` | 52,610.00 USD | 183.26 USD | 0.00 USD | `+15.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7205` | 52,760.00 USD | 147.15 USD | 0.00 USD | `+15.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7215` | 56,020.00 USD | 3,260.00 USD | 0.00 USD | `+15.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7225` | 56,170.00 USD | 150.08 USD | 0.00 USD | `+15.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7265` | 62,590.00 USD | 6,410.00 USD | 0.00 USD | `+16.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7325` | 62,750.00 USD | 165.17 USD | 0.00 USD | `+17.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7345` | 63,780.00 USD | 1,030.00 USD | 0.00 USD | `+17.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7375` | 63,890.00 USD | 106.75 USD | 0.00 USD | `+18.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7395` | 64,090.00 USD | 208.16 USD | 0.00 USD | `+18.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7405` | 64,830.00 USD | 733.09 USD | 0.00 USD | `+18.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7415` | 64,980.00 USD | 156.98 USD | 0.00 USD | `+18.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7425` | 65,120.00 USD | 132.95 USD | 0.00 USD | `+19.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7445` | 65,550.00 USD | 432.66 USD | 0.00 USD | `+19.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7455` | 67,720.00 USD | 2,170.00 USD | 0.00 USD | `+19.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7475` | 68,030.00 USD | 318.43 USD | 0.00 USD | `+19.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7505` | 68,180.00 USD | 141.39 USD | 0.00 USD | `+20.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7525` | 68,310.00 USD | 134.74 USD | 0.00 USD | `+20.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7565` | 72,430.00 USD | 4,120.00 USD | 0.00 USD | `+21.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7575` | 72,940.00 USD | 511.82 USD | 0.00 USD | `+21.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7585` | 73,070.00 USD | 135.82 USD | 0.00 USD | `+21.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7615` | 73,950.00 USD | 875.23 USD | 0.00 USD | `+22.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7635` | 74,050.00 USD | 103.35 USD | 0.00 USD | `+22.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7665` | 74,180.00 USD | 127.48 USD | 0.00 USD | `+22.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7675` | 74,280.00 USD | 101.61 USD | 0.00 USD | `+23.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7695` | 74,470.00 USD | 186.97 USD | 0.00 USD | `+23.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7705` | 74,580.00 USD | 109.43 USD | 0.00 USD | `+23.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7775` | 74,740.00 USD | 166.70 USD | 0.00 USD | `+24.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7815` | 75,880.00 USD | 1,140.00 USD | 0.00 USD | `+25.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7865` | 82,190.00 USD | 6,310.00 USD | 0.00 USD | `+26.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8095` | 82,330.00 USD | 133.42 USD | 0.00 USD | `+29.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8125` | 94,400.00 USD | 12,070.00 USD | 0.00 USD | `+30.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8335` | 95,330.00 USD | 929.08 USD | 0.00 USD | `+33.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8475` | 135,920.00 USD | 40,590.00 USD | 0.00 USD | `+35.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8505` | 152,660.00 USD | 16,740.00 USD | 0.00 USD | `+36.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8515` | 165,380.00 USD | 12,720.00 USD | 0.00 USD | `+36.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8525` | 177,160.00 USD | 11,780.00 USD | 0.00 USD | `+36.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8705` | 178,440.00 USD | 1,280.00 USD | 0.00 USD | `+39.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8725` | 178,600.00 USD | 159.86 USD | 0.00 USD | `+40.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 180,030.00 USD | 1,430.00 USD | 0.00 USD | `+44.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 180,220.00 USD | 193.62 USD | 0.00 USD | `+45.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 180,560.00 USD | 340.54 USD | 0.00 USD | `+52.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 180,710.00 USD | 145.72 USD | 0.00 USD | `+55.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 182,740.00 USD | 2,030.00 USD | 0.00 USD | `+58.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 182,880.00 USD | 136.10 USD | 0.00 USD | `+60.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 183,430.00 USD | 550.48 USD | 0.00 USD | `+60.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 183,740.00 USD | 314.99 USD | 0.00 USD | `+64.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 184,350.00 USD | 602.17 USD | 0.00 USD | `+68.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 184,710.00 USD | 360.61 USD | 0.00 USD | `+70.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 185,650.00 USD | 942.77 USD | 0.00 USD | `+73.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 185,990.00 USD | 337.31 USD | 0.00 USD | `+73.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 186,380.00 USD | 397.19 USD | 0.00 USD | `+76.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 186,910.00 USD | 525.37 USD | 0.00 USD | `+97.29%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.5320` | 869,300.00 USD | 0.00 USD | 869,300.00 USD | 11,240.00 USD | 0.00 USD | 3,480.00 USD |
| `7D` | `0.5340` | 854,580.00 USD | 0.00 USD | 854,580.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD |
| `1D` | `0.5360` | 721,930.00 USD | 0.00 USD | 721,930.00 USD | 4,510.00 USD | 2,900.00 USD | 3,730.00 USD |
| `7D` | `0.5360` | 851,980.00 USD | 0.00 USD | 851,980.00 USD | 2,440.00 USD | 3,040.00 USD | 0.00 USD |
| `1D` | `0.5380` | 710,790.00 USD | 0.00 USD | 710,790.00 USD | 5,850.00 USD | 2,040.00 USD | 3,130.00 USD |
| `7D` | `0.5380` | 846,500.00 USD | 0.00 USD | 846,500.00 USD | 0.00 USD | 1,550.00 USD | 2,940.00 USD |
| `1D` | `0.5400` | 699,760.00 USD | 0.00 USD | 699,760.00 USD | 4,470.00 USD | 256.13 USD | 2,370.00 USD |
| `1D` | `0.5420` | 692,670.00 USD | 0.00 USD | 692,670.00 USD | 2,590.00 USD | 0.00 USD | 4,880.00 USD |
| `7D` | `0.5420` | 842,010.00 USD | 0.00 USD | 842,010.00 USD | 7,660.00 USD | 1,290.00 USD | 2,950.00 USD |
| `1D` | `0.5440` | 685,200.00 USD | 0.00 USD | 685,200.00 USD | 714.14 USD | 0.00 USD | 1,070.00 USD |
| `7D` | `0.5440` | 830,120.00 USD | 0.00 USD | 830,120.00 USD | 0.00 USD | 1,150.00 USD | 6,970.00 USD |
| `1D` | `0.5460` | 683,420.00 USD | 0.00 USD | 683,420.00 USD | 5,050.00 USD | 298.25 USD | 990.37 USD |
| `7D` | `0.5460` | 822,000.00 USD | 0.00 USD | 822,000.00 USD | 2,250.00 USD | 3,030.00 USD | 5,190.00 USD |
| `1D` | `0.5480` | 677,080.00 USD | 0.00 USD | 677,080.00 USD | 0.00 USD | 633.67 USD | 14.03 USD |
| `7D` | `0.5480` | 811,530.00 USD | 0.00 USD | 811,530.00 USD | 2,000.00 USD | 795.70 USD | 4,470.00 USD |
| `1D` | `0.5500` | 676,430.00 USD | 0.00 USD | 676,430.00 USD | 0.00 USD | 0.00 USD | 7,220.00 USD |
| `7D` | `0.5500` | 804,260.00 USD | 0.00 USD | 804,260.00 USD | 5,990.00 USD | 1,440.00 USD | 6,710.00 USD |
| `1D` | `0.5520` | 669,210.00 USD | 0.00 USD | 669,210.00 USD | 0.00 USD | 0.00 USD | 1,280.00 USD |
| `7D` | `0.5520` | 790,120.00 USD | 0.00 USD | 790,120.00 USD | 4,110.00 USD | 1,920.00 USD | 1,880.00 USD |
| `1D` | `0.5540` | 667,930.00 USD | 0.00 USD | 667,930.00 USD | 1,790.00 USD | 1,320.00 USD | 7.66 USD |
| `7D` | `0.5540` | 782,200.00 USD | 0.00 USD | 782,200.00 USD | 12,840.00 USD | 4,860.00 USD | 18,470.00 USD |
| `1D` | `0.5560` | 664,810.00 USD | 0.00 USD | 664,810.00 USD | 557.27 USD | 201.08 USD | 520.52 USD |
| `7D` | `0.5560` | 746,040.00 USD | 0.00 USD | 746,040.00 USD | 13,490.00 USD | 1,920.00 USD | 6,250.00 USD |
| `1D` | `0.5580` | 663,530.00 USD | 0.00 USD | 663,530.00 USD | 1,100.00 USD | 4,900.00 USD | 3,560.00 USD |
| `7D` | `0.5580` | 724,380.00 USD | 0.00 USD | 724,380.00 USD | 6,000.00 USD | 6,820.00 USD | 18,300.00 USD |
| `1D` | `0.5600` | 653,970.00 USD | 0.00 USD | 653,970.00 USD | 1,550.00 USD | 1,830.00 USD | 1,460.00 USD |
| `7D` | `0.5600` | 693,260.00 USD | 0.00 USD | 693,260.00 USD | 4,070.00 USD | 8,160.00 USD | 2,500.00 USD |
| `1D` | `0.5620` | 649,130.00 USD | 0.00 USD | 649,130.00 USD | 715.25 USD | 1,230.00 USD | 1,580.00 USD |
| `7D` | `0.5620` | 678,530.00 USD | 0.00 USD | 678,530.00 USD | 19,480.00 USD | 7,420.00 USD | 11,550.00 USD |
| `1D` | `0.5640` | 645,600.00 USD | 0.00 USD | 645,600.00 USD | 0.00 USD | 3,980.00 USD | 4,590.00 USD |
| `7D` | `0.5640` | 640,090.00 USD | 0.00 USD | 640,090.00 USD | 2,950.00 USD | 741.21 USD | 27.20 USD |
| `7D` | `0.5660` | 636,370.00 USD | 0.00 USD | 636,370.00 USD | 11,490.00 USD | 2,990.00 USD | 4,430.00 USD |
| `7D` | `0.5680` | 617,470.00 USD | 0.00 USD | 617,470.00 USD | 5,100.00 USD | 0.00 USD | 2,890.00 USD |
| `7D` | `0.5700` | 609,480.00 USD | 0.00 USD | 609,480.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD |
| `1D` | `0.5720` | 637,030.00 USD | 0.00 USD | 637,030.00 USD | 0.00 USD | 2,350.00 USD | 0.00 USD |
| `7D` | `0.5720` | 606,900.00 USD | 0.00 USD | 606,900.00 USD | 0.00 USD | 4,370.00 USD | 1,360.00 USD |
| `7D` | `0.5740` | 601,170.00 USD | 0.00 USD | 601,170.00 USD | 21,620.00 USD | 1,100.00 USD | 1,610.00 USD |
| `7D` | `0.5760` | 576,830.00 USD | 0.00 USD | 576,830.00 USD | 2,150.00 USD | 0.00 USD | 19.23 USD |
| `1D` | `0.5780` | 634,680.00 USD | 0.00 USD | 634,680.00 USD | 0.00 USD | 0.00 USD | 94.61 USD |
| `7D` | `0.5780` | 574,660.00 USD | 0.00 USD | 574,660.00 USD | 0.00 USD | 0.00 USD | 1,570.00 USD |
| `7D` | `0.5800` | 573,090.00 USD | 0.00 USD | 573,090.00 USD | 1,610.00 USD | 0.00 USD | 2,850.00 USD |
| `1D` | `0.5820` | 634,580.00 USD | 0.00 USD | 634,580.00 USD | 0.00 USD | 1,000.00 USD | 0.00 USD |
| `7D` | `0.5820` | 568,640.00 USD | 0.00 USD | 568,640.00 USD | 0.00 USD | 0.00 USD | 6,520.00 USD |
| `1D` | `0.5840` | 633,580.00 USD | 0.00 USD | 633,580.00 USD | 0.00 USD | 0.00 USD | 47.28 USD |
| `1D` | `0.5860` | 633,540.00 USD | 0.00 USD | 633,540.00 USD | 0.00 USD | 658.88 USD | 14,870.00 USD |
| `7D` | `0.5860` | 562,120.00 USD | 0.00 USD | 562,120.00 USD | 0.00 USD | 0.00 USD | 146.30 USD |
| `1D` | `0.5880` | 618,000.00 USD | 0.00 USD | 618,000.00 USD | 4,160.00 USD | 2,210.00 USD | 7,190.00 USD |
| `7D` | `0.5880` | 561,970.00 USD | 0.00 USD | 561,970.00 USD | 3,110.00 USD | 1,400.00 USD | 65.70 USD |
| `1D` | `0.5900` | 604,440.00 USD | 0.00 USD | 604,440.00 USD | 8,190.00 USD | 1,390.00 USD | 11.26 USD |
| `7D` | `0.5900` | 557,400.00 USD | 0.00 USD | 557,400.00 USD | 3,120.00 USD | 1,560.00 USD | 15.37 USD |
| `1D` | `0.5920` | 594,860.00 USD | 0.00 USD | 594,860.00 USD | 11,320.00 USD | 4,470.00 USD | 11,880.00 USD |
| `7D` | `0.5920` | 552,700.00 USD | 0.00 USD | 552,700.00 USD | 11,690.00 USD | 2,820.00 USD | 6,030.00 USD |
| `1D` | `0.5940` | 567,190.00 USD | 0.00 USD | 567,190.00 USD | 9,310.00 USD | 8,970.00 USD | 15,850.00 USD |
| `7D` | `0.5940` | 532,160.00 USD | 0.00 USD | 532,160.00 USD | 10,090.00 USD | 0.00 USD | 9,780.00 USD |
| `1D` | `0.5960` | 533,050.00 USD | 0.00 USD | 533,050.00 USD | 27,990.00 USD | 12,850.00 USD | 15,240.00 USD |
| `7D` | `0.5960` | 512,290.00 USD | 0.00 USD | 512,290.00 USD | 18,180.00 USD | 18,410.00 USD | 13,390.00 USD |
| `1D` | `0.5980` | 476,980.00 USD | 0.00 USD | 476,980.00 USD | 10,420.00 USD | 8,800.00 USD | 45,410.00 USD |
| `7D` | `0.5980` | 462,320.00 USD | 0.00 USD | 462,320.00 USD | 20,380.00 USD | 826.53 USD | 19,920.00 USD |
| `1D` | `0.6000` | 412,350.00 USD | 0.00 USD | 412,350.00 USD | 18,690.00 USD | 7,050.00 USD | 9,120.00 USD |
| `7D` | `0.6000` | 421,190.00 USD | 0.00 USD | 421,190.00 USD | 3,320.00 USD | 2,140.00 USD | 18,810.00 USD |
| `1D` | `0.6020` | 377,480.00 USD | 0.00 USD | 377,480.00 USD | 21,590.00 USD | 13,700.00 USD | 11,410.00 USD |
| `7D` | `0.6020` | 396,920.00 USD | 0.00 USD | 396,920.00 USD | 23,960.00 USD | 8,040.00 USD | 4,060.00 USD |
| `1D` | `0.6040` | 330,790.00 USD | 0.00 USD | 330,790.00 USD | 19,460.00 USD | 7,680.00 USD | 46.43 USD |
| `7D` | `0.6040` | 360,860.00 USD | 0.00 USD | 360,860.00 USD | 8,620.00 USD | 7,530.00 USD | 7,920.00 USD |
| `1D` | `0.6060` | 303,590.00 USD | 0.00 USD | 303,590.00 USD | 8,500.00 USD | 6,650.00 USD | 28,110.00 USD |
| `7D` | `0.6060` | 336,790.00 USD | 0.00 USD | 336,790.00 USD | 0.00 USD | 0.00 USD | 227.43 USD |
| `1D` | `0.6080` | 260,330.00 USD | 0.00 USD | 260,330.00 USD | 10,660.00 USD | 37,840.00 USD | 11,220.00 USD |
| `7D` | `0.6080` | 336,560.00 USD | 0.00 USD | 336,560.00 USD | 2,860.00 USD | 0.00 USD | 9,370.00 USD |
| `1D` | `0.6100` | 200,600.00 USD | 0.00 USD | 200,600.00 USD | 10,380.00 USD | 17,750.00 USD | 14,240.00 USD |
| `7D` | `0.6100` | 324,330.00 USD | 0.00 USD | 324,330.00 USD | 21,400.00 USD | 47,430.00 USD | 25,300.00 USD |
| `1D` | `0.6120` | 158,230.00 USD | 0.00 USD | 158,230.00 USD | 25,010.00 USD | 0.00 USD | 8,290.00 USD |
| `7D` | `0.6120` | 230,190.00 USD | 0.00 USD | 230,190.00 USD | 35,760.00 USD | 5,720.00 USD | 18,510.00 USD |
| `1D` | `0.6140` | 124,930.00 USD | 0.00 USD | 124,930.00 USD | 35,500.00 USD | 30,510.00 USD | 22,770.00 USD |
| `7D` | `0.6140` | 170,200.00 USD | 0.00 USD | 170,200.00 USD | 51,550.00 USD | 8,040.00 USD | 10,780.00 USD |
| `1D` | `0.6160` | 36,140.00 USD | 0.00 USD | 36,140.00 USD | 17,390.00 USD | 4,840.00 USD | 0.00 USD |
| `7D` | `0.6160` | 99,830.00 USD | 0.00 USD | 99,830.00 USD | 12,920.00 USD | 16,340.00 USD | 4,760.00 USD |
| `1D` | `0.6180` | 13,910.00 USD | 0.00 USD | 13,910.00 USD | 0.00 USD | 0.00 USD | 13,910.00 USD |
| `7D` | `0.6180` | 65,810.00 USD | 0.00 USD | 65,810.00 USD | 20,870.00 USD | 2,610.00 USD | 228.92 USD |
| `7D` | `0.6200` | 42,100.00 USD | 0.00 USD | 42,100.00 USD | 23,430.00 USD | 0.00 USD | 18,670.00 USD |
| `1D` | `0.6210` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6210` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6220` | 20,540.00 USD | 20,540.00 USD | 0.00 USD | 1,990.00 USD | 18,550.00 USD | 0.00 USD |
| `7D` | `0.6220` | 27,620.00 USD | 27,620.00 USD | 0.00 USD | 4,760.00 USD | 22,640.00 USD | 215.59 USD |
| `7D` | `0.6240` | 27,790.00 USD | 27,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 171.81 USD |
| `7D` | `0.6260` | 95,110.00 USD | 95,110.00 USD | 0.00 USD | 67,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6300` | 105,020.00 USD | 105,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,920.00 USD |
| `1D` | `0.6320` | 81,480.00 USD | 81,480.00 USD | 0.00 USD | 45,660.00 USD | 3,970.00 USD | 11,300.00 USD |
| `7D` | `0.6320` | 105,390.00 USD | 105,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 369.35 USD |
| `1D` | `0.6340` | 185,580.00 USD | 185,580.00 USD | 0.00 USD | 39,290.00 USD | 0.00 USD | 64,810.00 USD |
| `7D` | `0.6340` | 174,440.00 USD | 174,440.00 USD | 0.00 USD | 68,660.00 USD | 0.00 USD | 381.22 USD |
| `1D` | `0.6360` | 360,430.00 USD | 360,430.00 USD | 0.00 USD | 114,380.00 USD | 0.00 USD | 60,480.00 USD |
| `7D` | `0.6360` | 265,740.00 USD | 265,740.00 USD | 0.00 USD | 34,320.00 USD | 0.00 USD | 56,980.00 USD |
| `1D` | `0.6380` | 420,550.00 USD | 420,550.00 USD | 0.00 USD | 0.00 USD | 24,790.00 USD | 35,330.00 USD |
| `7D` | `0.6380` | 304,820.00 USD | 304,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39,090.00 USD |
| `1D` | `0.6400` | 581,870.00 USD | 581,870.00 USD | 0.00 USD | 55,850.00 USD | 31,730.00 USD | 73,730.00 USD |
| `7D` | `0.6400` | 325,340.00 USD | 325,340.00 USD | 0.00 USD | 0.00 USD | 7,510.00 USD | 13,010.00 USD |
| `1D` | `0.6420` | 708,140.00 USD | 708,140.00 USD | 0.00 USD | 79,430.00 USD | 20,170.00 USD | 26,670.00 USD |
| `7D` | `0.6420` | 432,660.00 USD | 432,660.00 USD | 0.00 USD | 55,350.00 USD | 35,430.00 USD | 16,530.00 USD |
| `1D` | `0.6440` | 899,810.00 USD | 899,810.00 USD | 0.00 USD | 75,460.00 USD | 39,300.00 USD | 76,920.00 USD |
| `7D` | `0.6440` | 520,040.00 USD | 520,040.00 USD | 0.00 USD | 44,690.00 USD | 24,820.00 USD | 17,870.00 USD |
| `1D` | `0.6460` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 127,650.00 USD | 16,540.00 USD | 43,760.00 USD |
| `7D` | `0.6460` | 877,570.00 USD | 877,570.00 USD | 0.00 USD | 172,610.00 USD | 46,630.00 USD | 138,290.00 USD |
| `1D` | `0.6480` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 181,680.00 USD | 22,790.00 USD | 174.56 USD |
| `7D` | `0.6480` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 86,440.00 USD | 26,520.00 USD | 33,000.00 USD |
| `1D` | `0.6500` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 131,750.00 USD | 5,920.00 USD | 4,410.00 USD |
| `7D` | `0.6500` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 73,560.00 USD | 0.00 USD | 132,400.00 USD |
| `1D` | `0.6520` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 139,000.00 USD | 9,040.00 USD | 11,510.00 USD |
| `7D` | `0.6520` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 298,050.00 USD | 10,910.00 USD | 104,780.00 USD |
| `1D` | `0.6540` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 24,560.00 USD | 2,420.00 USD | 10,560.00 USD |
| `7D` | `0.6540` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 15,730.00 USD | 4,440.00 USD | 61,750.00 USD |
| `1D` | `0.6560` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,960.00 USD |
| `7D` | `0.6560` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 5,380.00 USD | 847.61 USD |
| `1D` | `0.6580` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 3,310.00 USD | 30.58 USD |
| `7D` | `0.6580` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 28,280.00 USD | 9,690.00 USD |
| `1D` | `0.6600` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 14,280.00 USD | 223.65 USD |
| `7D` | `0.6600` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 15,500.00 USD | 580.13 USD |
| `1D` | `0.6620` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,850.00 USD |
| `7D` | `0.6620` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 128.16 USD |
| `1D` | `0.6640` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 11,190.00 USD | 0.00 USD | 165.44 USD |
| `7D` | `0.6640` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 33,660.00 USD | 0.00 USD | 534.34 USD |
| `1D` | `0.6660` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 3,160.00 USD | 22,830.00 USD |
| `7D` | `0.6660` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 6,770.00 USD | 436.87 USD |
| `1D` | `0.6680` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 18,850.00 USD | 0.00 USD | 47.28 USD |
| `7D` | `0.6680` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 308.18 USD |
| `1D` | `0.6700` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 8,830.00 USD | 5,470.00 USD | 29,150.00 USD |
| `7D` | `0.6700` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 966.49 USD |
| `1D` | `0.6720` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 41,970.00 USD | 0.00 USD | 5,950.00 USD |
| `7D` | `0.6720` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 58,470.00 USD | 0.00 USD | 30,140.00 USD |
| `1D` | `0.6740` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 88,690.00 USD | 10,790.00 USD | 13,770.00 USD |
| `7D` | `0.6740` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 39,730.00 USD | 0.00 USD | 99.42 USD |
| `1D` | `0.6760` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 40,550.00 USD | 11,820.00 USD | 12,070.00 USD |
| `7D` | `0.6760` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 77,970.00 USD | 33,090.00 USD |
| `1D` | `0.6780` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 48,140.00 USD | 18,790.00 USD | 23,000.00 USD |
| `7D` | `0.6780` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 63,600.00 USD | 14,400.00 USD | 17,930.00 USD |
| `1D` | `0.6800` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 18,610.00 USD | 17,030.00 USD |
| `7D` | `0.6800` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 0.00 USD |
| `1D` | `0.6820` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 22,600.00 USD | 18,530.00 USD | 17,620.00 USD |
| `7D` | `0.6820` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 32,570.00 USD | 53,450.00 USD | 145.79 USD |
| `1D` | `0.6840` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 70,350.00 USD | 51,350.00 USD | 48,180.00 USD |
| `7D` | `0.6840` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 57,890.00 USD | 54,300.00 USD | 102,430.00 USD |
| `1D` | `0.6860` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 91,340.00 USD | 10,160.00 USD | 23,220.00 USD |
| `7D` | `0.6860` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 49,930.00 USD | 14,540.00 USD | 10,480.00 USD |
| `1D` | `0.6880` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 77,570.00 USD | 12,320.00 USD | 35,340.00 USD |
| `7D` | `0.6880` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 38,030.00 USD | 17,300.00 USD | 0.00 USD |
| `1D` | `0.6900` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 14,580.00 USD | 4,030.00 USD | 28,370.00 USD |
| `7D` | `0.6900` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 15,510.00 USD | 16,550.00 USD |
| `1D` | `0.6920` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 45,660.00 USD | 1,730.00 USD | 53,430.00 USD |
| `7D` | `0.6920` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 69,620.00 USD | 2,090.00 USD | 62,020.00 USD |
| `1D` | `0.6940` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 21,260.00 USD | 2,090.00 USD | 9,630.00 USD |
| `7D` | `0.6940` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 14,220.00 USD | 0.00 USD | 42,600.00 USD |
| `1D` | `0.6960` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 80,850.00 USD | 10,460.00 USD | 3,790.00 USD |
| `7D` | `0.6960` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 59,960.00 USD | 0.00 USD | 12,390.00 USD |
| `1D` | `0.6980` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 42,600.00 USD | 8,880.00 USD | 1,320.00 USD |
| `7D` | `0.6980` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 35,980.00 USD | 16,990.00 USD | 0.00 USD |
| `1D` | `0.7000` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 23,420.00 USD | 8,850.00 USD | 21,540.00 USD |
| `7D` | `0.7000` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 29,740.00 USD | 0.00 USD | 40,190.00 USD |
| `1D` | `0.7020` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 29,880.00 USD | 0.00 USD | 95.82 USD |
| `7D` | `0.7020` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 29,810.00 USD | 0.00 USD | 53,230.00 USD |
| `1D` | `0.7040` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 34,260.00 USD | 2,630.00 USD | 19,270.00 USD |
| `7D` | `0.7040` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 95,520.00 USD | 0.00 USD | 96,250.00 USD |
| `1D` | `0.7060` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 38,380.00 USD | 6,520.00 USD | 32,360.00 USD |
| `7D` | `0.7060` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 47,840.00 USD | 33,490.00 USD | 178,200.00 USD |
| `1D` | `0.7080` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 38,400.00 USD | 25,370.00 USD | 21,840.00 USD |
| `7D` | `0.7080` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 24,440.00 USD | 64,870.00 USD | 82,560.00 USD |
| `1D` | `0.7100` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 26,310.00 USD | 4,440.00 USD | 14,560.00 USD |
| `7D` | `0.7100` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 150,830.00 USD | 63,530.00 USD | 148,790.00 USD |
| `1D` | `0.7120` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 24,360.00 USD | 14,170.00 USD | 25,710.00 USD |
| `7D` | `0.7120` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 101,040.00 USD | 78,760.00 USD | 228,080.00 USD |
| `1D` | `0.7140` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 46,910.00 USD | 9,020.00 USD | 39,250.00 USD |
| `7D` | `0.7140` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 202,560.00 USD | 67,260.00 USD | 133,230.00 USD |
| `1D` | `0.7160` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 35,660.00 USD | 16,790.00 USD | 33,290.00 USD |
| `7D` | `0.7160` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 113,040.00 USD | 65,260.00 USD | 164,360.00 USD |
| `1D` | `0.7180` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 11,150.00 USD | 7,400.00 USD | 23,900.00 USD |
| `7D` | `0.7180` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 165,860.00 USD | 56,910.00 USD | 66,540.00 USD |
| `1D` | `0.7200` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 12,780.00 USD | 3,000.00 USD | 7,000.00 USD |
| `7D` | `0.7200` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 93,750.00 USD | 45,160.00 USD | 177,940.00 USD |
| `1D` | `0.7220` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 17,280.00 USD | 13,330.00 USD | 8,260.00 USD |
| `7D` | `0.7220` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 318,420.00 USD | 67,130.00 USD | 98,130.00 USD |
| `1D` | `0.7240` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 12,450.00 USD | 6,350.00 USD | 11,350.00 USD |
| `7D` | `0.7240` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 146,110.00 USD | 24,910.00 USD | 128,950.00 USD |
| `1D` | `0.7260` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 21,500.00 USD | 5,000.00 USD | 22,330.00 USD |
| `7D` | `0.7260` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 106,410.00 USD | 52,120.00 USD | 175,450.00 USD |
| `1D` | `0.7280` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 50,390.00 USD | 6,280.00 USD | 21,990.00 USD |
| `7D` | `0.7280` | 7,200,000.00 USD | 7,200,000.00 USD | 0.00 USD | 99,750.00 USD | 40,180.00 USD | 83,870.00 USD |
| `1D` | `0.7300` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 23,130.00 USD | 12,630.00 USD | 32,400.00 USD |
| `7D` | `0.7300` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 115,310.00 USD | 60,310.00 USD | 109,420.00 USD |
| `1D` | `0.7320` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 13,500.00 USD | 2,810.00 USD | 7,460.00 USD |
| `7D` | `0.7320` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 189,840.00 USD | 65,640.00 USD | 80,460.00 USD |
| `1D` | `0.7340` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,950.00 USD |
| `7D` | `0.7340` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 31,260.00 USD | 8,620.00 USD | 63,250.00 USD |
| `1D` | `0.7360` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 7,970.00 USD | 4,660.00 USD | 3,750.00 USD |
| `7D` | `0.7360` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 103,600.00 USD | 46,790.00 USD | 35,030.00 USD |
| `1D` | `0.7380` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 12,130.00 USD | 5,260.00 USD | 5,620.00 USD |
| `7D` | `0.7380` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 73,710.00 USD | 19,000.00 USD | 60,620.00 USD |
| `1D` | `0.7400` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 8,500.00 USD | 2,360.00 USD | 2,350.00 USD |
| `7D` | `0.7400` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 1,730.00 USD | 4,760.00 USD | 27,790.00 USD |
| `7D` | `0.7420` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 35,810.00 USD | 41,830.00 USD | 31,380.00 USD |
| `7D` | `0.7440` | 8,590,000.00 USD | 8,590,000.00 USD | 0.00 USD | 74,450.00 USD | 39,890.00 USD | 70,380.00 USD |
| `7D` | `0.7460` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 88,800.00 USD | 28,800.00 USD | 51,780.00 USD |
| `7D` | `0.7480` | 8,890,000.00 USD | 8,890,000.00 USD | 0.00 USD | 60,580.00 USD | 28,900.00 USD | 38,290.00 USD |
| `7D` | `0.7500` | 8,980,000.00 USD | 8,980,000.00 USD | 0.00 USD | 52,320.00 USD | 12,610.00 USD | 25,140.00 USD |
| `7D` | `0.7520` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 53,470.00 USD | 13,000.00 USD | 50,770.00 USD |
| `7D` | `0.7540` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 30,340.00 USD | 1,890.00 USD | 25,430.00 USD |
| `7D` | `0.7560` | 9,210,000.00 USD | 9,210,000.00 USD | 0.00 USD | 26,000.00 USD | 7,570.00 USD | 22,260.00 USD |
| `7D` | `0.7580` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 55,420.00 USD | 11,790.00 USD | 45,930.00 USD |
| `7D` | `0.7600` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 57,020.00 USD | 4,320.00 USD | 80,740.00 USD |
| `7D` | `0.7620` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 54,140.00 USD | 24,170.00 USD | 21,540.00 USD |
| `7D` | `0.7640` | 9,670,000.00 USD | 9,670,000.00 USD | 0.00 USD | 50,390.00 USD | 13,520.00 USD | 41,540.00 USD |
| `7D` | `0.7660` | 9,830,000.00 USD | 9,830,000.00 USD | 0.00 USD | 56,130.00 USD | 18,130.00 USD | 91,090.00 USD |
| `7D` | `0.7680` | 9,970,000.00 USD | 9,970,000.00 USD | 0.00 USD | 66,570.00 USD | 32,520.00 USD | 41,010.00 USD |
| `7D` | `0.7700` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 10,860.00 USD | 12,600.00 USD | 41,730.00 USD |
| `7D` | `0.7720` | 10,160,000.00 USD | 10,160,000.00 USD | 0.00 USD | 58,380.00 USD | 32,920.00 USD | 25,780.00 USD |
| `7D` | `0.7740` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 51,600.00 USD | 25,250.00 USD | 35,740.00 USD |
| `7D` | `0.7760` | 10,320,000.00 USD | 10,320,000.00 USD | 0.00 USD | 38,170.00 USD | 2,980.00 USD | 12,740.00 USD |
| `7D` | `0.7780` | 10,450,000.00 USD | 10,450,000.00 USD | 0.00 USD | 68,800.00 USD | 20,860.00 USD | 32,580.00 USD |
| `7D` | `0.7800` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 60,490.00 USD | 21,940.00 USD | 80,690.00 USD |
| `7D` | `0.7820` | 10,720,000.00 USD | 10,720,000.00 USD | 0.00 USD | 90,020.00 USD | 17,850.00 USD | 6,240.00 USD |
| `7D` | `0.7840` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 95,370.00 USD | 7,150.00 USD | 2,180.00 USD |
| `7D` | `0.7860` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 32,690.00 USD | 9,290.00 USD | 45,150.00 USD |
| `7D` | `0.7880` | 10,970,000.00 USD | 10,970,000.00 USD | 0.00 USD | 11,900.00 USD | 22,650.00 USD | 22,510.00 USD |
| `7D` | `0.7900` | 11,060,000.00 USD | 11,060,000.00 USD | 0.00 USD | 59,120.00 USD | 16,710.00 USD | 17,430.00 USD |
| `7D` | `0.7910` | 11,100,000.00 USD | 11,100,000.00 USD | 0.00 USD | 30,620.00 USD | 5,860.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `87.86M` | Total OI Tokens: `142,495,697.5 APT`
  * 1h OI Change: `-2.50%` | 4h OI Change: `-9.83%` | 24h OI Change: `-13.01%`
  * Exchange Breakdown: Binance=`16.14M` | Bybit=`17.94M` | OKX=`4.23M` | Hyperliquid=`3.58M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-1.07K` | Last 24h: `8.88K` | Last 3d: `10.89K` | Last 7d: `5.22K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0042%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0049%` | **USDT KuCoin** | `0.0074%` |
| **USDT MEXC** | `-0.0040%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0001%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `APT` | `44.71%` | `55.29%` | `0.81` | 5,060,000.00 USD |
| `15M` | `Binance` | `41.54%` | `58.46%` | `0.71` | 1,440,000.00 USD |
| `15M` | `OKX` | `45.32%` | `54.68%` | `0.83` | 609,790.00 USD |
| `15M` | `Bybit` | `37.84%` | `62.16%` | `0.61` | 1,010,000.00 USD |
| `15M` | `KuCoin` | `44.68%` | `55.32%` | `0.81` | 102,880.00 USD |
| `15M` | `Gate` | `39.51%` | `60.49%` | `0.65` | 195,020.00 USD |
| `15M` | `Bitget` | `29.31%` | `70.69%` | `0.41` | 56,200.00 USD |
| `15M` | `BingX` | `48.29%` | `51.71%` | `0.93` | 609,590.00 USD |
| `15M` | `MEXC` | `39.94%` | `60.06%` | `0.67` | 108,290.00 USD |
| `15M` | `Bitunix` | `50.61%` | `49.39%` | `1.02` | 65,600.00 USD |
| `15M` | `Hyperliquid` | `17.47%` | `82.53%` | `0.21` | 87,570.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.45%` | `50.55%` | `0.98` | 171,520.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `67.1%` | `32.9%` | `2.04` | 559,130.00 USD |
| `15M` | `HTX` | `48.44%` | `51.56%` | `0.94` | 27,860.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `49.39%` | `50.61%` | `0.98` | 11,910.00 USD |
| `15M` | `Aster` | `13.55%` | `86.45%` | `0.16` | 6,690.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `97.86%` | `2.14%` | `45.73` | 183.92 USD |
| `15M` | `Whale Positions` | `41.54%` | `58.46%` | `0.71` | 1,440,000.00 USD |
| `15M` | `Global Accounts` | `44.71%` | `55.29%` | `0.81` | 5,060,000.00 USD |
| `1H` | `APT` | `51.79%` | `48.21%` | `1.07` | 32,440,000.00 USD |
| `1H` | `Binance` | `51.97%` | `48.03%` | `1.08` | 14,360,000.00 USD |
| `1H` | `OKX` | `50.34%` | `49.66%` | `1.01` | 3,240,000.00 USD |
| `1H` | `Bybit` | `53.95%` | `46.05%` | `1.17` | 2,950,000.00 USD |
| `1H` | `KuCoin` | `52.31%` | `47.69%` | `1.10` | 676,910.00 USD |
| `1H` | `Gate` | `59.1%` | `40.9%` | `1.44` | 796,160.00 USD |
| `1H` | `Bitget` | `67.29%` | `32.71%` | `2.06` | 1,600,000.00 USD |
| `1H` | `BingX` | `21.43%` | `78.57%` | `0.27` | 880,720.00 USD |
| `1H` | `MEXC` | `55.51%` | `44.49%` | `1.25` | 536,670.00 USD |
| `1H` | `Bitunix` | `47.7%` | `52.3%` | `0.91` | 1,210,000.00 USD |
| `1H` | `Hyperliquid` | `58.72%` | `41.28%` | `1.42` | 240,230.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.64%` | `50.36%` | `0.99` | 4,980,000.00 USD |
| `1H` | `Crypto.com` | `95.68%` | `4.32%` | `22.15` | 3,070.00 USD |
| `1H` | `WhiteBIT` | `50.69%` | `49.31%` | `1.03` | 708,580.00 USD |
| `1H` | `HTX` | `73.53%` | `26.47%` | `2.78` | 16,440.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `85.11%` | `14.89%` | `5.72` | 96,380.00 USD |
| `1H` | `Aster` | `59.41%` | `40.59%` | `1.46` | 123,440.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `32.2%` | `67.8%` | `0.47` | 15,380.00 USD |
| `1H` | `Whale Positions` | `51.97%` | `48.03%` | `1.08` | 14,360,000.00 USD |
| `1H` | `Global Accounts` | `51.79%` | `48.21%` | `1.07` | 32,440,000.00 USD |
| `4H` | `APT` | `48.78%` | `51.22%` | `0.95` | 117,520,000.00 USD |
| `4H` | `Binance` | `50.75%` | `49.25%` | `1.03` | 46,870,000.00 USD |
| `4H` | `OKX` | `48.67%` | `51.33%` | `0.95` | 16,050,000.00 USD |
| `4H` | `Bybit` | `49.79%` | `50.21%` | `0.99` | 12,570,000.00 USD |
| `4H` | `KuCoin` | `49.08%` | `50.92%` | `0.96` | 2,220,000.00 USD |
| `4H` | `Gate` | `53.89%` | `46.11%` | `1.17` | 2,880,000.00 USD |
| `4H` | `Bitget` | `53.12%` | `46.88%` | `1.13` | 4,400,000.00 USD |
| `4H` | `BingX` | `40.2%` | `59.8%` | `0.67` | 3,170,000.00 USD |
| `4H` | `MEXC` | `45.59%` | `54.41%` | `0.84` | 1,820,000.00 USD |
| `4H` | `Bitunix` | `50.99%` | `49.01%` | `1.04` | 4,120,000.00 USD |
| `4H` | `Hyperliquid` | `34.67%` | `65.33%` | `0.53` | 1,490,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.27%` | `50.73%` | `0.97` | 18,250,000.00 USD |
| `4H` | `Crypto.com` | `75.66%` | `24.34%` | `3.11` | 5,380.00 USD |
| `4H` | `WhiteBIT` | `14.01%` | `85.99%` | `0.16` | 2,930,000.00 USD |
| `4H` | `HTX` | `46.63%` | `53.37%` | `0.87` | 124,330.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `52.9%` | `47.1%` | `1.12` | 262,260.00 USD |
| `4H` | `Aster` | `53.33%` | `46.67%` | `1.14` | 248,850.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `35.39%` | `64.61%` | `0.55` | 119,970.00 USD |
| `4H` | `Whale Positions` | `50.75%` | `49.25%` | `1.03` | 46,870,000.00 USD |
| `4H` | `Global Accounts` | `48.78%` | `51.22%` | `0.95` | 117,520,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.6713` | `0.6715` | `0.6713` | `0.6739` | `0.6704` | 216,510.95 USD | 86,107.15 USD | 130,403.80 USD | -44,296.65 USD | `-20.46%` | `5B / 11S` |
| `0:00 UTC` | `0.6618` | `0.6610` | `0.6618` | `0.6728` | `0.6545` | 3,111,032.57 USD | 1,289,720.42 USD | 1,821,312.14 USD | -531,591.72 USD | `-17.09%` | `14B / 47S` |
| `5:00 UTC` | `0.6646` | `0.6634` | `0.6646` | `0.6663` | `0.6601` | 1,040,684.48 USD | 553,372.77 USD | 487,311.70 USD | 66,061.07 USD | `+6.35%` | `21B / 6S` |
| `0:00 UTC` | `0.6256` | `0.6358` | `0.6256` | `0.6640` | `0.6136` | 10,130,057.36 USD | 3,799,647.14 USD | 6,330,410.22 USD | -2,530,763.08 USD | `-24.98%` | `3B / 31S` |
| `5:00 UTC` | `0.6208` | `0.6173` | `0.6208` | `0.6292` | `0.6004` | 5,930,137.61 USD | 2,790,946.56 USD | 3,139,191.05 USD | -348,244.48 USD | `-5.87%` | `7B / 8S` |
| `0:00 UTC` | `0.6268` | `0.6270` | `0.6268` | `0.6331` | `0.6164` | 2,767,755.14 USD | 1,444,801.14 USD | 1,322,953.99 USD | 121,847.15 USD | `+4.40%` | `10B / 14S` |
| `5:00 UTC` | `0.6356` | `0.6324` | `0.6356` | `0.6401` | `0.6246` | 2,269,133.84 USD | 1,171,035.44 USD | 1,098,098.41 USD | 72,937.03 USD | `+3.21%` | `20B / 14S` |
| `0:00 UTC` | `0.6381` | `0.6343` | `0.6381` | `0.6411` | `0.6278` | 1,411,771.88 USD | 641,300.89 USD | 770,470.99 USD | -129,170.10 USD | `-9.15%` | `24B / 26S` |
| `5:00 UTC` | `0.6253` | `0.6259` | `0.6253` | `0.6310` | `0.6218` | 914,324.95 USD | 433,904.43 USD | 480,420.52 USD | -46,516.10 USD | `-5.09%` | `13B / 14S` |
| `0:00 UTC` | `0.6226` | `0.6204` | `0.6226` | `0.6270` | `0.6137` | 1,922,061.59 USD | 906,736.81 USD | 1,015,324.78 USD | -108,587.97 USD | `-5.65%` | `9B / 22S` |

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
| `5m` | -27,770.00 USD | -31,130.00 USD | **`DISTRIBUTION`** |
| `15m` | -99,640.00 USD | -109,270.00 USD | **`DISTRIBUTION`** |
| `30m` | -158,070.00 USD | -305,920.00 USD | **`DISTRIBUTION`** |
| `1h` | 115,470.00 USD | 182,930.00 USD | **`ACCUMULATION`** |
| `2h` | -322,220.00 USD | -3,640,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -403,070.00 USD | -4,150,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -429,030.00 USD | -6,120,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -210,180.00 USD | -6,810,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -119,410.00 USD | -7,230,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,550,000.00 USD | -10,310,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,200,000.00 USD | -24,410,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,630,000.00 USD | -105,120,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-27.77K` | 15m=`-99.64K` | 1h=`+115.47K` | 24h=`-1.55M`
* Futures Capital Netflows: 5m=`-31.13K` | 15m=`-109.27K` | 1h=`+182.93K` | 24h=`-10.31M`
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
  * `2026-10-30 03:29:57 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:57 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:40:57 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:41:57 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:41:57 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:57 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
