# 🏛️ SOVEREIGN CANDIDATE DOSSIER: APT
**Canonical Key**: `APT` | **Broker Instrument**: `APTUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 23:40:50 IST` (`2026-10-29 18:10:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.6777` | `0.6804` | `0.6768` | `0.6795` | `185,444` | 125,914.95 USD | 26,390.74 USD | `+20.96%` | -3,599,607.51 USD | `+0.95` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.6796` | `0.6802` | `0.6774` | `0.6791` | `306,060` | 207,708.53 USD | -9,134.27 USD | `-4.40%` | -3,608,741.77 USD | `+0.53` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `0.6791` | `0.6799` | `0.6788` | `0.6799` | `43,974` | 29,865.66 USD | 7,350.64 USD | `+24.61%` | -3,601,391.13 USD | `+0.64` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.6877` | `0.6898` | `0.6792` | `0.6800` | `1,357,766` | 929,091.57 USD | -281,134.41 USD | `-30.26%` | -3,393,024.69 USD | `-1.67` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.6800` | `0.6816` | `0.6730` | `0.6795` | `1,554,134` | 1,052,942.47 USD | -184,461.17 USD | `-17.52%` | -3,577,485.86 USD | `-0.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.6796` | `0.6802` | `0.6774` | `0.6795` | `346,164` | 234,944.25 USD | -4,413.56 USD | `-1.88%` | -3,581,899.42 USD | `+0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.7037` | `0.7077` | `0.6911` | `0.6926` | `5,801,752` | 4,049,481.14 USD | -506,091.42 USD | `-12.50%` | -2,881,736.42 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.6926` | `0.6945` | `0.6730` | `0.6795` | `4,651,736` | 3,182,247.98 USD | -755,471.85 USD | `-23.74%` | -3,637,208.27 USD | `-2.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.6796` | `0.6802` | `0.6774` | `0.6795` | `346,164` | 234,944.25 USD | -4,413.56 USD | `-1.88%` | -3,641,621.83 USD | `+0.53` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.6561` | `0.6774` | `0.6549` | `0.6712` | `7,448,343` | 4,965,296.85 USD | -60,141.40 USD | `-1.21%` | -2,083,618.45 USD | `+1.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -2,231,705.21 USD | `+0.80` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6730` | `0.6796` | `10,800,447` | 7,467,213.73 USD | -1,265,436.48 USD | `-16.95%` | -3,497,141.68 USD | `-1.50` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.7002` | `0.7012` | `0.6555` | `0.6611` | `16,465,880` | 11,061,810.70 USD | -1,103,761.29 USD | `-9.98%` | -1,656,578.37 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6611` | `0.6759` | `0.6485` | `0.6561` | `10,656,422` | 7,044,804.33 USD | -366,898.68 USD | `-5.21%` | -2,023,477.05 USD | `+0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6561` | `0.6774` | `0.6549` | `0.6712` | `7,448,343` | 4,965,296.85 USD | -60,141.40 USD | `-1.21%` | -2,083,618.45 USD | `+1.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -2,231,705.21 USD | `+0.80` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6730` | `0.6796` | `10,800,447` | 7,467,213.73 USD | -1,265,436.48 USD | `-16.95%` | -3,497,141.68 USD | `-1.50` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:36:01 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.6956` | 10,520.98 USD | `-` | `NEWS_INTEL` | `-` | #APT Whale BUY: 10.52K USD at 0.6956 USD [API] | `2026-10-27 21:39:38` |
| `ANNOUNCEMENT` | `INFO` | `0.6925` | 8,223.30 USD | `-` | `NEWS_INTEL` | `-` | #APT Whale SELL: 8.22K USD at 0.6925 USD [API] | `2026-10-27 21:42:23` |
| `ANNOUNCEMENT` | `INFO` | `0.8175` | 207.26 USD | `-` | `NEWS_INTEL` | `-` | #APT Liquidated Long: 0.21K USD at 0.8175 USD [API] | `2026-09-28 07:26:38` |
| `ANNOUNCEMENT` | `INFO` | `0.8175` | 750.34 USD | `-` | `NEWS_INTEL` | `-` | #APT Liquidated Long: 0.75K USD at 0.8175 USD [API] | `2026-09-28 07:26:38` |
| `ANNOUNCEMENT` | `INFO` | `0.8175` | 575.00 USD | `-` | `NEWS_INTEL` | `-` | #APT Liquidated Long: 0.58K USD at 0.8175 USD [API] | `2026-09-28 07:26:38` |
| `ANNOUNCEMENT` | `INFO` | `0.8175` | 520.97 USD | `-` | `NEWS_INTEL` | `-` | #APT Liquidated Long: 0.52K USD at 0.8175 USD [API] | `2026-09-28 07:26:38` |
| `ANNOUNCEMENT` | `INFO` | `0.8176` | 375.14 USD | `-` | `NEWS_INTEL` | `-` | #APT Liquidated Long: 0.38K USD at 0.8176 USD [API] | `2026-09-28 07:26:38` |


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
| `Live` | `Long Liquidation` | `0.1875` | 269.27 USD | 246,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1935` | 2,180.00 USD | 246,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2025` | 506.25 USD | 243,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 2,700.00 USD | 243,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 511.00 USD | 240,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 428.25 USD | 240,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3155` | 8,970.00 USD | 239,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3175` | 1,590.00 USD | 230,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3225` | 415.54 USD | 229,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3275` | 3,030.00 USD | 228,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3305` | 543.58 USD | 225,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3335` | 233.45 USD | 225,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3405` | 640.60 USD | 225,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3545` | 177.25 USD | 224,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3565` | 2,140.00 USD | 224,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 189.47 USD | 222,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3675` | 194.23 USD | 221,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3895` | 394.35 USD | 221,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3905` | 359.26 USD | 221,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3955` | 2,640.00 USD | 220,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3995` | 271.06 USD | 218,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 570.81 USD | 218,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4135` | 1,600.00 USD | 217,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 630.86 USD | 215,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4255` | 224.96 USD | 215,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4405` | 4,300.00 USD | 215,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4455` | 5,080.00 USD | 210,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 226.63 USD | 205,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4515` | 27,090.00 USD | 205,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4525` | 147.06 USD | 178,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4605` | 1,080.00 USD | 178,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4625` | 1,100.00 USD | 177,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4675` | 7,710.00 USD | 175,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4685` | 468.50 USD | 168,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4755` | 472.63 USD | 167,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 135.33 USD | 167,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4855` | 3,160.00 USD | 167,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 429.90 USD | 164,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 102.82 USD | 163,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5095` | 2,550.00 USD | 163,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 248.05 USD | 160,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5135` | 110.50 USD | 160,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5145` | 288.78 USD | 160,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 9,440.00 USD | 160,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5315` | 11,510.00 USD | 150,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5325` | 3,110.00 USD | 139,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5335` | 163.22 USD | 136,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5365` | 1,430.00 USD | 136,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5385` | 2,690.00 USD | 134,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5445` | 330.14 USD | 131,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5475` | 482.65 USD | 131,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5495` | 630.26 USD | 131,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5545` | 67,280.00 USD | 130,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5585` | 10,520.00 USD | 63,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5615` | 1,720.00 USD | 52,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5675` | 649.99 USD | 50,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 164.24 USD | 50,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5715` | 289.08 USD | 50,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 214.84 USD | 49,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5835` | 132.92 USD | 49,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 210.96 USD | 49,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 586.80 USD | 49,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5870` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 1,400.00 USD | 65.70 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5880` | 2,540,000.00 USD | 2,540,000.00 USD | 3,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5885` | 440.16 USD | 48,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5890` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 15.37 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5895` | 1,690.00 USD | 48,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5900` | 2,530,000.00 USD | 2,530,000.00 USD | 3,120.00 USD | 1,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5920` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 2,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5925` | 609.14 USD | 46,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5930` | 2,530,000.00 USD | 2,530,000.00 USD | 10,090.00 USD | 0.00 USD | 9,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5935` | 572.40 USD | 46,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5945` | 3,850.00 USD | 45,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5950` | 2,510,000.00 USD | 2,510,000.00 USD | 5,120.00 USD | 0.00 USD | 4,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5960` | 2,500,000.00 USD | 2,500,000.00 USD | 5,120.00 USD | 1,640.00 USD | 46.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5970` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5975` | 157.22 USD | 41,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5980` | 2,480,000.00 USD | 2,480,000.00 USD | 7,660.00 USD | 826.53 USD | 3.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5990` | 2,470,000.00 USD | 2,470,000.00 USD | 3,320.00 USD | 1,340.00 USD | 14,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6000` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 796.28 USD | 4,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6005` | 852.06 USD | 41,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.6020` | 2,450,000.00 USD | 2,450,000.00 USD | 4,890.00 USD | 8,040.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6025` | 451.19 USD | 40,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6030` | 2,120,000.00 USD | 2,120,000.00 USD | 5,230.00 USD | 1,970.00 USD | 7,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6030` | 2,430,000.00 USD | 2,430,000.00 USD | 2,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6040` | 2,110,000.00 USD | 2,110,000.00 USD | 4,530.00 USD | 963.47 USD | 1,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6040` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6045` | 527.44 USD | 40,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6050` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 599.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6060` | 2,100,000.00 USD | 2,100,000.00 USD | 2,880.00 USD | 606.70 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6060` | 2,420,000.00 USD | 2,420,000.00 USD | 2,850.00 USD | 0.00 USD | 32.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6070` | 2,090,000.00 USD | 2,090,000.00 USD | 1,490.00 USD | 1,030.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6070` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 32.69 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6080` | 2,090,000.00 USD | 2,090,000.00 USD | 1,240.00 USD | 0.00 USD | 3,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6080` | 2,420,000.00 USD | 2,420,000.00 USD | 2,860.00 USD | 0.00 USD | 124.87 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6090` | 2,080,000.00 USD | 2,080,000.00 USD | 2,110.00 USD | 0.00 USD | 47.82 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6090` | 2,410,000.00 USD | 2,410,000.00 USD | 6,360.00 USD | 0.00 USD | 9,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6100` | 2,080,000.00 USD | 2,080,000.00 USD | 5,670.00 USD | 307.09 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6100` | 2,400,000.00 USD | 2,400,000.00 USD | 7,480.00 USD | 2,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6105` | 126.47 USD | 39,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6110` | 2,070,000.00 USD | 2,070,000.00 USD | 2,490.00 USD | 0.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6110` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 2,210.00 USD | 6,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6120` | 2,060,000.00 USD | 2,060,000.00 USD | 902.06 USD | 398.52 USD | 2,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6120` | 2,380,000.00 USD | 2,380,000.00 USD | 2,100.00 USD | 3,510.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6130` | 2,060,000.00 USD | 2,060,000.00 USD | 3,070.00 USD | 596.50 USD | 2,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6130` | 2,370,000.00 USD | 2,370,000.00 USD | 8,870.00 USD | 1,050.00 USD | 4,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6140` | 2,050,000.00 USD | 2,050,000.00 USD | 6,120.00 USD | 0.00 USD | 2,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6140` | 2,350,000.00 USD | 2,350,000.00 USD | 4,540.00 USD | 7,000.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6150` | 2,050,000.00 USD | 2,050,000.00 USD | 2,730.00 USD | 0.00 USD | 30.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6150` | 2,330,000.00 USD | 2,330,000.00 USD | 11,130.00 USD | 5,870.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6160` | 2,040,000.00 USD | 2,040,000.00 USD | 1,460.00 USD | 1,690.00 USD | 126.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6160` | 2,310,000.00 USD | 2,310,000.00 USD | 1,790.00 USD | 2,510.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6170` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6170` | 2,310,000.00 USD | 2,310,000.00 USD | 13,260.00 USD | 2,610.00 USD | 14,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6180` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 678.61 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6180` | 2,280,000.00 USD | 2,280,000.00 USD | 7,600.00 USD | 1,190.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6190` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 126.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6190` | 2,260,000.00 USD | 2,260,000.00 USD | 9,560.00 USD | 1,930.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6195` | 3,170.00 USD | 39,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6200` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6200` | 2,240,000.00 USD | 2,240,000.00 USD | 13,870.00 USD | 5,230.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6210` | 2,030,000.00 USD | 2,030,000.00 USD | 1,990.00 USD | 0.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6210` | 2,210,000.00 USD | 2,210,000.00 USD | 4,760.00 USD | 1,860.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6220` | 2,030,000.00 USD | 2,030,000.00 USD | 2,520.00 USD | 0.00 USD | 7.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6220` | 2,200,000.00 USD | 2,200,000.00 USD | 7,960.00 USD | 2,310.00 USD | 29,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6230` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6230` | 2,160,000.00 USD | 2,160,000.00 USD | 9,770.00 USD | 4,700.00 USD | 8,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6235` | 3,250.00 USD | 36,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6240` | 2,030,000.00 USD | 2,030,000.00 USD | 4,840.00 USD | 4,260.00 USD | 76.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6240` | 2,140,000.00 USD | 2,140,000.00 USD | 18,610.00 USD | 4,720.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6245` | 1,960.00 USD | 33,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6250` | 2,020,000.00 USD | 2,020,000.00 USD | 1,800.00 USD | 2,630.00 USD | 85.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6250` | 2,110,000.00 USD | 2,110,000.00 USD | 16,120.00 USD | 3,830.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6255` | 286.65 USD | 31,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6260` | 2,010,000.00 USD | 2,010,000.00 USD | 10,030.00 USD | 1,310.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6260` | 2,090,000.00 USD | 2,090,000.00 USD | 20,890.00 USD | 7,660.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6265` | 10,530.00 USD | 30,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6270` | 1,990,000.00 USD | 1,990,000.00 USD | 3,700.00 USD | 3,940.00 USD | 12,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6270` | 2,030,000.00 USD | 2,030,000.00 USD | 17,460.00 USD | 8,200.00 USD | 24,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6280` | 1,970,000.00 USD | 1,970,000.00 USD | 11,690.00 USD | 463.43 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6280` | 1,980,000.00 USD | 1,980,000.00 USD | 9,160.00 USD | 9,230.00 USD | 16,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6285` | 903.47 USD | 20,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6290` | 1,960,000.00 USD | 1,960,000.00 USD | 11,890.00 USD | 1,200.00 USD | 5,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6290` | 1,950,000.00 USD | 1,950,000.00 USD | 17,710.00 USD | 6,740.00 USD | 10,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6300` | 1,940,000.00 USD | 1,940,000.00 USD | 12,950.00 USD | 2,470.00 USD | 2,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6300` | 1,910,000.00 USD | 1,910,000.00 USD | 10,040.00 USD | 7,890.00 USD | 11,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6310` | 1,920,000.00 USD | 1,920,000.00 USD | 7,940.00 USD | 5,110.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6310` | 1,890,000.00 USD | 1,890,000.00 USD | 19,340.00 USD | 4,520.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6315` | 1,010.00 USD | 19,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6320` | 1,900,000.00 USD | 1,900,000.00 USD | 12,320.00 USD | 11,080.00 USD | 14,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6320` | 1,840,000.00 USD | 1,840,000.00 USD | 4,880.00 USD | 12,650.00 USD | 8,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6330` | 1,860,000.00 USD | 1,860,000.00 USD | 17,300.00 USD | 3,580.00 USD | 21,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6330` | 1,820,000.00 USD | 1,820,000.00 USD | 57,940.00 USD | 14,700.00 USD | 33,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6340` | 1,820,000.00 USD | 1,820,000.00 USD | 9,830.00 USD | 2,020.00 USD | 15,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6340` | 1,710,000.00 USD | 1,710,000.00 USD | 10,730.00 USD | 3,420.00 USD | 4,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6350` | 1,800,000.00 USD | 1,800,000.00 USD | 19,180.00 USD | 8,820.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6350` | 1,690,000.00 USD | 1,690,000.00 USD | 14,450.00 USD | 2,430.00 USD | 22,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6360` | 1,760,000.00 USD | 1,760,000.00 USD | 30,350.00 USD | 9,150.00 USD | 33,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6360` | 1,650,000.00 USD | 1,650,000.00 USD | 42,690.00 USD | 7,300.00 USD | 40,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6370` | 1,690,000.00 USD | 1,690,000.00 USD | 21,750.00 USD | 4,510.00 USD | 27,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6370` | 1,560,000.00 USD | 1,560,000.00 USD | 49,080.00 USD | 4,870.00 USD | 29.01 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6375` | 5,900.00 USD | 18,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6380` | 1,640,000.00 USD | 1,640,000.00 USD | 19,430.00 USD | 7,180.00 USD | 7,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6380` | 1,510,000.00 USD | 1,510,000.00 USD | 18,140.00 USD | 3,870.00 USD | 30,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6390` | 1,600,000.00 USD | 1,600,000.00 USD | 18,790.00 USD | 529.57 USD | 6,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6390` | 1,460,000.00 USD | 1,460,000.00 USD | 10,200.00 USD | 7,510.00 USD | 13,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6400` | 1,580,000.00 USD | 1,580,000.00 USD | 9,830.00 USD | 9,970.00 USD | 25,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6400` | 1,430,000.00 USD | 1,430,000.00 USD | 15,560.00 USD | 0.00 USD | 330.78 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6410` | 1,530,000.00 USD | 1,530,000.00 USD | 20,930.00 USD | 2,240.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6410` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 6,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6415` | 4,740.00 USD | 12,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6420` | 1,500,000.00 USD | 1,500,000.00 USD | 32,540.00 USD | 7,850.00 USD | 12,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6420` | 1,400,000.00 USD | 1,400,000.00 USD | 39,060.00 USD | 26,560.00 USD | 10,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6430` | 1,450,000.00 USD | 1,450,000.00 USD | 25,620.00 USD | 7,460.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6430` | 1,330,000.00 USD | 1,330,000.00 USD | 16,200.00 USD | 3,970.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6435` | 2,320.00 USD | 7,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6440` | 1,410,000.00 USD | 1,410,000.00 USD | 21,790.00 USD | 11,330.00 USD | 8,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6440` | 1,300,000.00 USD | 1,300,000.00 USD | 14,160.00 USD | 6,720.00 USD | 14,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6450` | 1,370,000.00 USD | 1,370,000.00 USD | 23,100.00 USD | 20,050.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6450` | 1,270,000.00 USD | 1,270,000.00 USD | 14,120.00 USD | 15,560.00 USD | 383.87 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6455` | 3,730.00 USD | 5,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6460` | 1,290,000.00 USD | 1,290,000.00 USD | 43,360.00 USD | 10,480.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6460` | 1,240,000.00 USD | 1,240,000.00 USD | 75,060.00 USD | 14,300.00 USD | 75,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6470` | 1,190,000.00 USD | 1,190,000.00 USD | 30,630.00 USD | 6,620.00 USD | 41,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6470` | 1,070,000.00 USD | 1,070,000.00 USD | 9,660.00 USD | 3,880.00 USD | 9,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6480` | 1,110,000.00 USD | 1,110,000.00 USD | 48,130.00 USD | 14,180.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6480` | 1,050,000.00 USD | 1,050,000.00 USD | 37,050.00 USD | 0.00 USD | 23,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6485` | 259.68 USD | 1,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6490` | 1,040,000.00 USD | 1,040,000.00 USD | 27,600.00 USD | 3,800.00 USD | 51,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6490` | 989,720.00 USD | 989,720.00 USD | 36,340.00 USD | 0.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6500` | 955,330.00 USD | 955,330.00 USD | 42,280.00 USD | 1,390.00 USD | 32,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6500` | 935,730.00 USD | 935,730.00 USD | 18,310.00 USD | 0.00 USD | 81,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6505` | 580.53 USD | 1,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6510` | 879,020.00 USD | 879,020.00 USD | 18,580.00 USD | 4,450.00 USD | 57,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6510` | 835,760.00 USD | 835,760.00 USD | 101,440.00 USD | 4,190.00 USD | 288.03 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6520` | 798,230.00 USD | 798,230.00 USD | 31,260.00 USD | 6,190.00 USD | 15,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6520` | 729,840.00 USD | 729,840.00 USD | 39,510.00 USD | 6,720.00 USD | 71,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6530` | 745,250.00 USD | 745,250.00 USD | 5,780.00 USD | 1,060.00 USD | 11,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6530` | 611,780.00 USD | 611,780.00 USD | 0.00 USD | 0.00 USD | 47,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6540` | 726,680.00 USD | 726,680.00 USD | 11,450.00 USD | 2,530.00 USD | 13,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6540` | 564,680.00 USD | 564,680.00 USD | 15,730.00 USD | 0.00 USD | 14,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6550` | 699,500.00 USD | 699,500.00 USD | 18,980.00 USD | 4,080.00 USD | 15,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6550` | 534,310.00 USD | 534,310.00 USD | 0.00 USD | 0.00 USD | 38,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6560` | 660,470.00 USD | 660,470.00 USD | 23,680.00 USD | 3,800.00 USD | 25,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6560` | 495,880.00 USD | 495,880.00 USD | 7,220.00 USD | 5,380.00 USD | 34,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6570` | 607,910.00 USD | 607,910.00 USD | 5,570.00 USD | 1,820.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6570` | 448,550.00 USD | 448,550.00 USD | 14,440.00 USD | 0.00 USD | 10,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6580` | 580,730.00 USD | 580,730.00 USD | 5,880.00 USD | 0.00 USD | 30.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6580` | 423,460.00 USD | 423,460.00 USD | 0.00 USD | 0.00 USD | 12,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6590` | 574,820.00 USD | 574,820.00 USD | 2,100.00 USD | 5,490.00 USD | 19,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6590` | 410,810.00 USD | 410,810.00 USD | 9,540.00 USD | 0.00 USD | 331.05 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6600` | 547,340.00 USD | 547,340.00 USD | 21,900.00 USD | 2,840.00 USD | 22,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6600` | 400,940.00 USD | 400,940.00 USD | 0.00 USD | 4,180.00 USD | 20,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6610` | 499,990.00 USD | 499,990.00 USD | 11,920.00 USD | 2,560.00 USD | 12,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6620` | 473,340.00 USD | 473,340.00 USD | 14,030.00 USD | 2,480.00 USD | 36,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6620` | 376,530.00 USD | 376,530.00 USD | 14,320.00 USD | 0.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6630` | 419,840.00 USD | 419,840.00 USD | 24,070.00 USD | 4,110.00 USD | 1,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6630` | 355,070.00 USD | 355,070.00 USD | 11,670.00 USD | 0.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6640` | 389,810.00 USD | 389,810.00 USD | 22,290.00 USD | 1,150.00 USD | 21,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6640` | 314,590.00 USD | 314,590.00 USD | 15,140.00 USD | 0.00 USD | 279.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6650` | 344,960.00 USD | 344,960.00 USD | 12,560.00 USD | 10,330.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6650` | 299,180.00 USD | 299,180.00 USD | 0.00 USD | 6,770.00 USD | 288.69 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6660` | 307,780.00 USD | 307,780.00 USD | 7,730.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6660` | 292,120.00 USD | 292,120.00 USD | 0.00 USD | 0.00 USD | 148.18 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6670` | 294,640.00 USD | 294,640.00 USD | 18,850.00 USD | 2,980.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6670` | 291,970.00 USD | 291,970.00 USD | 31,450.00 USD | 0.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6680` | 267,880.00 USD | 267,880.00 USD | 30,610.00 USD | 3,380.00 USD | 7,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6680` | 251,740.00 USD | 251,740.00 USD | 24,780.00 USD | 7,780.00 USD | 193.34 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6690` | 226,580.00 USD | 226,580.00 USD | 13,000.00 USD | 2,800.00 USD | 3,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6690` | 218,980.00 USD | 218,980.00 USD | 14,440.00 USD | 2,330.00 USD | 24,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6695` | 818.97 USD | 818.97 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6700` | 207,160.00 USD | 207,160.00 USD | 3,250.00 USD | 1,050.00 USD | 4,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6700` | 177,790.00 USD | 177,790.00 USD | 0.00 USD | 0.00 USD | 323.96 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6710` | 198,660.00 USD | 198,660.00 USD | 8,650.00 USD | 18,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6710` | 177,460.00 USD | 177,460.00 USD | 0.00 USD | 6,960.00 USD | 25,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6720` | 171,910.00 USD | 171,910.00 USD | 4,190.00 USD | 3,200.00 USD | 17,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6730` | 147,370.00 USD | 147,370.00 USD | 5,220.00 USD | 2,020.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6730` | 145,490.00 USD | 145,490.00 USD | 0.00 USD | 0.00 USD | 99.42 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6740` | 132,520.00 USD | 132,520.00 USD | 20,500.00 USD | 4,800.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6750` | 104,910.00 USD | 104,910.00 USD | 0.00 USD | 5,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6750` | 145,390.00 USD | 145,390.00 USD | 0.00 USD | 75,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6760` | 98,940.00 USD | 98,940.00 USD | 9,950.00 USD | 2,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6760` | 69,670.00 USD | 69,670.00 USD | 0.00 USD | 2,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6770` | 86,360.00 USD | 86,360.00 USD | 18,650.00 USD | 2,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6770` | 67,430.00 USD | 67,430.00 USD | 23,340.00 USD | 4,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6780` | 65,050.00 USD | 65,050.00 USD | 0.00 USD | 12,640.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6780` | 39,900.00 USD | 39,900.00 USD | 13,090.00 USD | 10,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6790` | 43,640.00 USD | 43,640.00 USD | 10,840.00 USD | 18,610.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6790` | 16,590.00 USD | 16,590.00 USD | 0.00 USD | 16,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6810` | 15,720.00 USD | 15,720.00 USD | 0.00 USD | 15,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6820` | 4,920.00 USD | 4,920.00 USD | 0.00 USD | 0.00 USD | 4,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6820` | 53,450.00 USD | 53,450.00 USD | 0.00 USD | 37,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6830` | 50,850.00 USD | 50,850.00 USD | 0.00 USD | 20,240.00 USD | 25,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6830` | 106,370.00 USD | 106,370.00 USD | 0.00 USD | 4,670.00 USD | 48,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6840` | 81,710.00 USD | 81,710.00 USD | 6,510.00 USD | 15,960.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6840` | 160,120.00 USD | 160,120.00 USD | 0.00 USD | 14,650.00 USD | 39,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6850` | 128,210.00 USD | 128,210.00 USD | 46,480.00 USD | 0.00 USD | 27.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6850` | 164,830.00 USD | 164,830.00 USD | 0.00 USD | 4,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6860` | 174,660.00 USD | 174,660.00 USD | 0.00 USD | 9,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6870` | 128,230.00 USD | 128,230.00 USD | 0.00 USD | 0.00 USD | 15.30 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6880` | 166,610.00 USD | 166,610.00 USD | 0.00 USD | 9,600.00 USD | 28,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6880` | 210,130.00 USD | 210,130.00 USD | 18,170.00 USD | 17,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6890` | 169,370.00 USD | 169,370.00 USD | 0.00 USD | 0.00 USD | 2,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6890` | 221,160.00 USD | 221,160.00 USD | 0.00 USD | 11,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6900` | 190,410.00 USD | 190,410.00 USD | 0.00 USD | 0.00 USD | 21,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6900` | 225,640.00 USD | 225,640.00 USD | 0.00 USD | 4,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6910` | 217,480.00 USD | 217,480.00 USD | 0.00 USD | 0.00 USD | 27,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6910` | 256,420.00 USD | 256,420.00 USD | 0.00 USD | 2,090.00 USD | 28,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6920` | 217,500.00 USD | 217,500.00 USD | 0.00 USD | 0.00 USD | 26.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6920` | 280,790.00 USD | 280,790.00 USD | 0.00 USD | 0.00 USD | 24,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6930` | 217,670.00 USD | 217,670.00 USD | 0.00 USD | 0.00 USD | 168.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6930` | 293,950.00 USD | 293,950.00 USD | 0.00 USD | 0.00 USD | 13,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6940` | 241,560.00 USD | 241,560.00 USD | 11,230.00 USD | 4,420.00 USD | 8,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6950` | 268,500.00 USD | 268,500.00 USD | 22,480.00 USD | 4,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6950` | 337,790.00 USD | 337,790.00 USD | 31,450.00 USD | 0.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6960` | 315,570.00 USD | 315,570.00 USD | 47,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6960` | 350,010.00 USD | 350,010.00 USD | 12,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6970` | 338,980.00 USD | 338,980.00 USD | 23,380.00 USD | 0.00 USD | 34.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6970` | 371,660.00 USD | 371,660.00 USD | 21,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6980` | 339,000.00 USD | 339,000.00 USD | 0.00 USD | 0.00 USD | 17.79 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6990` | 340,980.00 USD | 340,980.00 USD | 0.00 USD | 1,940.00 USD | 38.35 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6990` | 401,390.00 USD | 401,390.00 USD | 4,770.00 USD | 0.00 USD | 24,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7000` | 358,280.00 USD | 358,280.00 USD | 4,190.00 USD | 2,120.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7000` | 411,380.00 USD | 411,380.00 USD | 0.00 USD | 0.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7010` | 358,320.00 USD | 358,320.00 USD | 0.00 USD | 0.00 USD | 42.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7020` | 372,700.00 USD | 372,700.00 USD | 14,360.00 USD | 0.00 USD | 22.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7020` | 480,810.00 USD | 480,810.00 USD | 16,350.00 USD | 0.00 USD | 53,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7030` | 383,210.00 USD | 383,210.00 USD | 0.00 USD | 0.00 USD | 10,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7030` | 607,890.00 USD | 607,890.00 USD | 76,610.00 USD | 0.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7040` | 420,100.00 USD | 420,100.00 USD | 19,130.00 USD | 2,630.00 USD | 15,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7040` | 653,670.00 USD | 653,670.00 USD | 0.00 USD | 0.00 USD | 45,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7050` | 471,090.00 USD | 471,090.00 USD | 36,240.00 USD | 2,660.00 USD | 12,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7050` | 804,770.00 USD | 804,770.00 USD | 27,630.00 USD | 0.00 USD | 123,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7060` | 490,890.00 USD | 490,890.00 USD | 3,570.00 USD | 3,860.00 USD | 12,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7060` | 891,180.00 USD | 891,180.00 USD | 13,090.00 USD | 33,490.00 USD | 39,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7070` | 549,800.00 USD | 549,800.00 USD | 19,980.00 USD | 21,860.00 USD | 17,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7070` | 965,170.00 USD | 965,170.00 USD | 8,720.00 USD | 36,300.00 USD | 28,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7080` | 576,040.00 USD | 576,040.00 USD | 18,420.00 USD | 3,500.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7080` | 1,060,000.00 USD | 1,060,000.00 USD | 15,730.00 USD | 28,570.00 USD | 53,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7090` | 614,420.00 USD | 614,420.00 USD | 23,150.00 USD | 6,370.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7090` | 1,340,000.00 USD | 1,340,000.00 USD | 106,000.00 USD | 32,830.00 USD | 134,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7100` | 649,380.00 USD | 649,380.00 USD | 10,040.00 USD | 3,180.00 USD | 21,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7100` | 1,430,000.00 USD | 1,430,000.00 USD | 44,820.00 USD | 30,700.00 USD | 14,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7110` | 674,260.00 USD | 674,260.00 USD | 7,440.00 USD | 8,760.00 USD | 8,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7110` | 1,590,000.00 USD | 1,590,000.00 USD | 40,300.00 USD | 33,410.00 USD | 92,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7120` | 716,040.00 USD | 716,040.00 USD | 21,700.00 USD | 4,410.00 USD | 15,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7120` | 1,830,000.00 USD | 1,830,000.00 USD | 60,730.00 USD | 45,350.00 USD | 135,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7130` | 787,460.00 USD | 787,460.00 USD | 28,640.00 USD | 3,110.00 USD | 39,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7130` | 1,990,000.00 USD | 1,990,000.00 USD | 75,250.00 USD | 31,940.00 USD | 51,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7140` | 828,750.00 USD | 828,750.00 USD | 27,390.00 USD | 7,490.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7140` | 2,240,000.00 USD | 2,240,000.00 USD | 127,300.00 USD | 35,310.00 USD | 81,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7150` | 877,270.00 USD | 877,270.00 USD | 18,260.00 USD | 6,980.00 USD | 23,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7150` | 2,410,000.00 USD | 2,410,000.00 USD | 50,460.00 USD | 26,770.00 USD | 96,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7160` | 916,640.00 USD | 916,640.00 USD | 17,400.00 USD | 11,180.00 USD | 10,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7160` | 2,580,000.00 USD | 2,580,000.00 USD | 62,580.00 USD | 38,490.00 USD | 68,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7170` | 934,110.00 USD | 934,110.00 USD | 4,910.00 USD | 3,880.00 USD | 8,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7170` | 2,780,000.00 USD | 2,780,000.00 USD | 105,890.00 USD | 35,770.00 USD | 53,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7180` | 958,060.00 USD | 958,060.00 USD | 6,240.00 USD | 2,890.00 USD | 14,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7180` | 2,870,000.00 USD | 2,870,000.00 USD | 59,980.00 USD | 21,140.00 USD | 12,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7190` | 981,070.00 USD | 981,070.00 USD | 12,780.00 USD | 8,180.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7190` | 3,000,000.00 USD | 3,000,000.00 USD | 28,670.00 USD | 11,840.00 USD | 87,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7200` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 4,740.00 USD | 14,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7200` | 3,190,000.00 USD | 3,190,000.00 USD | 65,080.00 USD | 33,310.00 USD | 89,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7210` | 1,030,000.00 USD | 1,030,000.00 USD | 10,550.00 USD | 14,540.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7210` | 3,490,000.00 USD | 3,490,000.00 USD | 206,240.00 USD | 24,720.00 USD | 70,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7220` | 1,080,000.00 USD | 1,080,000.00 USD | 23,430.00 USD | 5,070.00 USD | 23,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7220` | 3,670,000.00 USD | 3,670,000.00 USD | 112,190.00 USD | 42,410.00 USD | 27,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7230` | 1,120,000.00 USD | 1,120,000.00 USD | 3,920.00 USD | 4,060.00 USD | 27,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7230` | 3,830,000.00 USD | 3,830,000.00 USD | 59,050.00 USD | 10,400.00 USD | 93,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7235` | 42,980.00 USD | 42,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7240` | 1,140,000.00 USD | 1,140,000.00 USD | 2,920.00 USD | 4,240.00 USD | 12,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7240` | 3,950,000.00 USD | 3,950,000.00 USD | 75,360.00 USD | 14,510.00 USD | 28,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7250` | 1,160,000.00 USD | 1,160,000.00 USD | 4,760.00 USD | 3,950.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7250` | 4,110,000.00 USD | 4,110,000.00 USD | 52,270.00 USD | 25,530.00 USD | 82,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7255` | 729.79 USD | 43,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7260` | 1,190,000.00 USD | 1,190,000.00 USD | 11,880.00 USD | 6,730.00 USD | 12,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7260` | 4,290,000.00 USD | 4,290,000.00 USD | 54,140.00 USD | 26,590.00 USD | 93,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7265` | 124.62 USD | 43,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7270` | 1,230,000.00 USD | 1,230,000.00 USD | 19,920.00 USD | 2,760.00 USD | 14,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7270` | 4,390,000.00 USD | 4,390,000.00 USD | 49,240.00 USD | 18,120.00 USD | 33,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7280` | 1,260,000.00 USD | 1,260,000.00 USD | 16,410.00 USD | 5,780.00 USD | 11,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7280` | 4,500,000.00 USD | 4,500,000.00 USD | 42,560.00 USD | 22,060.00 USD | 50,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7290` | 1,310,000.00 USD | 1,310,000.00 USD | 13,150.00 USD | 7,110.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7290` | 4,650,000.00 USD | 4,650,000.00 USD | 47,200.00 USD | 32,380.00 USD | 69,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7300` | 1,350,000.00 USD | 1,350,000.00 USD | 9,980.00 USD | 9,840.00 USD | 25,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7300` | 4,760,000.00 USD | 4,760,000.00 USD | 55,390.00 USD | 27,940.00 USD | 29,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7310` | 1,360,000.00 USD | 1,360,000.00 USD | 1,010.00 USD | 1,670.00 USD | 7,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7310` | 4,950,000.00 USD | 4,950,000.00 USD | 115,470.00 USD | 40,620.00 USD | 31,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7320` | 1,380,000.00 USD | 1,380,000.00 USD | 5,780.00 USD | 1,140.00 USD | 12,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7320` | 5,100,000.00 USD | 5,100,000.00 USD | 74,380.00 USD | 25,020.00 USD | 49,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7325` | 7,150.00 USD | 50,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7330` | 1,400,000.00 USD | 1,400,000.00 USD | 6,450.00 USD | 3,420.00 USD | 4,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7330` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 32,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7340` | 1,400,000.00 USD | 1,400,000.00 USD | 1,620.00 USD | 1,530.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7340` | 5,200,000.00 USD | 5,200,000.00 USD | 31,260.00 USD | 8,620.00 USD | 30,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7345` | 150.17 USD | 51,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7350` | 1,410,000.00 USD | 1,410,000.00 USD | 735.24 USD | 1,470.00 USD | 24.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7350` | 5,300,000.00 USD | 5,300,000.00 USD | 66,390.00 USD | 15,820.00 USD | 15,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7360` | 1,440,000.00 USD | 1,440,000.00 USD | 10,900.00 USD | 2,960.00 USD | 14,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7360` | 5,390,000.00 USD | 5,390,000.00 USD | 37,210.00 USD | 30,980.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7370` | 1,450,000.00 USD | 1,450,000.00 USD | 1,110.00 USD | 1,970.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7370` | 5,420,000.00 USD | 5,420,000.00 USD | 9,640.00 USD | 3,860.00 USD | 20,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7380` | 1,460,000.00 USD | 1,460,000.00 USD | 4,530.00 USD | 963.47 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7380` | 5,530,000.00 USD | 5,530,000.00 USD | 58,340.00 USD | 13,660.00 USD | 39,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7390` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 1,180.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7390` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 8,110.00 USD | 25,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7400` | 1,470,000.00 USD | 1,470,000.00 USD | 2,880.00 USD | 2,520.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7400` | 5,590,000.00 USD | 5,590,000.00 USD | 1,730.00 USD | 6,500.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7410` | 1,470,000.00 USD | 1,470,000.00 USD | 1,490.00 USD | 1,030.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7410` | 5,680,000.00 USD | 5,680,000.00 USD | 28,380.00 USD | 30,100.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7420` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 11.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7420` | 5,700,000.00 USD | 5,700,000.00 USD | 7,430.00 USD | 13,420.00 USD | 427.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7430` | 1,480,000.00 USD | 1,480,000.00 USD | 1,240.00 USD | 0.00 USD | 106.97 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7430` | 5,810,000.00 USD | 5,810,000.00 USD | 46,330.00 USD | 13,970.00 USD | 54,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7440` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 718.40 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7440` | 5,880,000.00 USD | 5,880,000.00 USD | 28,120.00 USD | 25,920.00 USD | 15,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7450` | 1,490,000.00 USD | 1,490,000.00 USD | 2,110.00 USD | 1,170.00 USD | 6,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7450` | 5,980,000.00 USD | 5,980,000.00 USD | 42,580.00 USD | 16,360.00 USD | 38,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7460` | 1,500,000.00 USD | 1,500,000.00 USD | 5,670.00 USD | 307.09 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7460` | 6,040,000.00 USD | 6,040,000.00 USD | 38,650.00 USD | 10,350.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7470` | 1,510,000.00 USD | 1,510,000.00 USD | 2,490.00 USD | 0.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7470` | 6,120,000.00 USD | 6,120,000.00 USD | 35,630.00 USD | 18,610.00 USD | 28,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7480` | 1,520,000.00 USD | 1,520,000.00 USD | 4,130.00 USD | 398.52 USD | 2,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7480` | 6,160,000.00 USD | 6,160,000.00 USD | 24,950.00 USD | 10,290.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7490` | 1,520,000.00 USD | 1,520,000.00 USD | 3,070.00 USD | 596.50 USD | 2,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7490` | 6,200,000.00 USD | 6,200,000.00 USD | 17,270.00 USD | 5,180.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7500` | 1,530,000.00 USD | 1,530,000.00 USD | 6,120.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7500` | 6,250,000.00 USD | 6,250,000.00 USD | 35,050.00 USD | 7,430.00 USD | 16,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7510` | 1,530,000.00 USD | 1,530,000.00 USD | 2,730.00 USD | 0.00 USD | 15.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7510` | 6,320,000.00 USD | 6,320,000.00 USD | 25,900.00 USD | 5,870.00 USD | 35,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7520` | 1,540,000.00 USD | 1,540,000.00 USD | 1,460.00 USD | 1,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7520` | 6,370,000.00 USD | 6,370,000.00 USD | 27,570.00 USD | 7,130.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7530` | 6,410,000.00 USD | 6,410,000.00 USD | 21,290.00 USD | 1,890.00 USD | 14,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7540` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 40.37 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7540` | 6,430,000.00 USD | 6,430,000.00 USD | 9,060.00 USD | 0.00 USD | 10,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7550` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7550` | 6,470,000.00 USD | 6,470,000.00 USD | 18,390.00 USD | 6,470.00 USD | 19,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7560` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 678.61 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7560` | 6,490,000.00 USD | 6,490,000.00 USD | 7,600.00 USD | 1,100.00 USD | 2,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7570` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 11.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7570` | 6,550,000.00 USD | 6,550,000.00 USD | 29,140.00 USD | 4,260.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7580` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 1,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7580` | 6,600,000.00 USD | 6,600,000.00 USD | 26,280.00 USD | 7,530.00 USD | 12,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7590` | 1,550,000.00 USD | 1,550,000.00 USD | 1,990.00 USD | 0.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7590` | 6,670,000.00 USD | 6,670,000.00 USD | 34,970.00 USD | 717.68 USD | 32,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7600` | 1,550,000.00 USD | 1,550,000.00 USD | 2,520.00 USD | 0.00 USD | 4.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7600` | 6,740,000.00 USD | 6,740,000.00 USD | 22,050.00 USD | 3,600.00 USD | 47,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7610` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7610` | 6,780,000.00 USD | 6,780,000.00 USD | 14,110.00 USD | 8,700.00 USD | 16,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7620` | 1,560,000.00 USD | 1,560,000.00 USD | 4,840.00 USD | 4,260.00 USD | 15.31 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7620` | 6,840,000.00 USD | 6,840,000.00 USD | 40,030.00 USD | 15,470.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7630` | 1,560,000.00 USD | 1,560,000.00 USD | 1,800.00 USD | 986.03 USD | 49.38 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7630` | 6,910,000.00 USD | 6,910,000.00 USD | 33,960.00 USD | 13,520.00 USD | 22,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7640` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 6.40 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7640` | 6,950,000.00 USD | 6,950,000.00 USD | 16,430.00 USD | 0.00 USD | 18,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7650` | 1,570,000.00 USD | 1,570,000.00 USD | 1,110.00 USD | 1,050.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7650` | 7,080,000.00 USD | 7,080,000.00 USD | 43,020.00 USD | 9,740.00 USD | 79,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7660` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 255.94 USD | 3,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7660` | 7,110,000.00 USD | 7,110,000.00 USD | 13,100.00 USD | 8,390.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7670` | 1,580,000.00 USD | 1,580,000.00 USD | 532.62 USD | 0.00 USD | 1,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7670` | 7,180,000.00 USD | 7,180,000.00 USD | 32,170.00 USD | 17,130.00 USD | 24,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7680` | 1,580,000.00 USD | 1,580,000.00 USD | 3,040.00 USD | 463.43 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7680` | 7,250,000.00 USD | 7,250,000.00 USD | 34,410.00 USD | 15,390.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7690` | 1,590,000.00 USD | 1,590,000.00 USD | 3,850.00 USD | 186.37 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7690` | 7,270,000.00 USD | 7,270,000.00 USD | 5,320.00 USD | 2,840.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7700` | 1,600,000.00 USD | 1,600,000.00 USD | 3,090.00 USD | 1,210.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7700` | 7,320,000.00 USD | 7,320,000.00 USD | 5,540.00 USD | 9,750.00 USD | 31,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7710` | 1,610,000.00 USD | 1,610,000.00 USD | 2,710.00 USD | 888.39 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7710` | 7,410,000.00 USD | 7,410,000.00 USD | 53,500.00 USD | 19,240.00 USD | 17,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7720` | 1,610,000.00 USD | 1,610,000.00 USD | 1,430.00 USD | 2,030.00 USD | 1,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7720` | 7,430,000.00 USD | 7,430,000.00 USD | 4,880.00 USD | 13,680.00 USD | 8,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7725` | 165.62 USD | 51,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7730` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 481.15 USD | 1,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7730` | 7,500,000.00 USD | 7,500,000.00 USD | 37,120.00 USD | 14,120.00 USD | 12,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7740` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 944.65 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7740` | 7,550,000.00 USD | 7,550,000.00 USD | 14,480.00 USD | 11,130.00 USD | 23,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7750` | 7,560,000.00 USD | 7,560,000.00 USD | 5,090.00 USD | 0.00 USD | 7,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7760` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 1,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7760` | 7,600,000.00 USD | 7,600,000.00 USD | 33,080.00 USD | 2,980.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7765` | 330.78 USD | 51,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7770` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 613.64 USD | 931.07 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7770` | 7,650,000.00 USD | 7,650,000.00 USD | 15,750.00 USD | 15,940.00 USD | 19,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7780` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 402.81 USD | 1.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7780` | 7,720,000.00 USD | 7,720,000.00 USD | 53,050.00 USD | 4,910.00 USD | 13,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7790` | 1,630,000.00 USD | 1,630,000.00 USD | 2,710.00 USD | 465.78 USD | 4,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7790` | 7,760,000.00 USD | 7,760,000.00 USD | 11,330.00 USD | 2,770.00 USD | 22,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7800` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7800` | 7,900,000.00 USD | 7,900,000.00 USD | 49,160.00 USD | 19,160.00 USD | 72,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7810` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 329.44 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7810` | 7,960,000.00 USD | 7,960,000.00 USD | 49,880.00 USD | 5,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7820` | 1,630,000.00 USD | 1,630,000.00 USD | 908.54 USD | 0.00 USD | 6.95 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7820` | 8,010,000.00 USD | 8,010,000.00 USD | 40,140.00 USD | 12,700.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7830` | 8,090,000.00 USD | 8,090,000.00 USD | 70,580.00 USD | 6,240.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7840` | 8,120,000.00 USD | 8,120,000.00 USD | 24,790.00 USD | 4,140.00 USD | 12.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8005` | 19,120.00 USD | 70,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8035` | 114.11 USD | 70,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8405` | 2,150.00 USD | 73,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8615` | 15,640.00 USD | 88,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8665` | 378.95 USD | 89,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9935` | 166.01 USD | 89,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.03` | 19,950.00 USD | 109,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.03` | 78,860.00 USD | 188,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 19,070.00 USD | 207,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 3,080.00 USD | 210,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 479.74 USD | 210,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.12` | 2,800.00 USD | 213,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.27` | 13,320.00 USD | 226,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 197.51 USD | 226,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 284.61 USD | 227,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.36` | 5,440.00 USD | 232,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1875` | 255,010.00 USD | 0.00 USD | 269.27 USD | `-72.43%` | `1,436.09` |
| `Live` | `Long` | `0.1995` | 254,740.00 USD | 0.00 USD | 2,250.00 USD | `-70.67%` | `11,284.25` |
| `Live` | `Long` | `0.2525` | 252,490.00 USD | 0.00 USD | 3,140.00 USD | `-62.87%` | `12,426.15` |
| `Live` | `Long` | `0.2905` | 249,350.00 USD | 0.00 USD | 581.00 USD | `-57.29%` | `2,000.00` |
| `Live` | `Long` | `0.3035` | 248,770.00 USD | 0.00 USD | 455.25 USD | `-55.37%` | `1,500.00` |
| `Live` | `Long` | `0.3175` | 248,320.00 USD | 0.00 USD | 10,620.00 USD | `-53.32%` | `33,446.85` |
| `Live` | `Long` | `0.3305` | 237,700.00 USD | 0.00 USD | 543.58 USD | `-51.40%` | `1,644.73` |
| `Live` | `Long` | `0.3345` | 237,150.00 USD | 0.00 USD | 836.25 USD | `-50.82%` | `2,500.00` |
| `Live` | `Long` | `0.3435` | 236,320.00 USD | 0.00 USD | 240.45 USD | `-49.49%` | `700.00` |
| `Live` | `Long` | `0.3545` | 236,080.00 USD | 0.00 USD | 177.25 USD | `-47.88%` | `500.00` |
| `Live` | `Long` | `0.3565` | 235,900.00 USD | 0.00 USD | 2,140.00 USD | `-47.58%` | `6,000.00` |
| `Live` | `Long` | `0.3605` | 233,760.00 USD | 0.00 USD | 3,330.00 USD | `-46.99%` | `9,243.24` |
| `Live` | `Long` | `0.3665` | 230,430.00 USD | 0.00 USD | 661.70 USD | `-46.11%` | `1,805.47` |
| `Live` | `Long` | `0.3675` | 229,770.00 USD | 0.00 USD | 194.23 USD | `-45.96%` | `528.52` |
| `Live` | `Long` | `0.3705` | 229,570.00 USD | 0.00 USD | 697.04 USD | `-45.52%` | `1,881.36` |
| `Live` | `Long` | `0.3905` | 228,880.00 USD | 0.00 USD | 359.26 USD | `-42.58%` | `919.99` |
| `Live` | `Long` | `0.3955` | 228,520.00 USD | 0.00 USD | 2,640.00 USD | `-41.85%` | `6,686.27` |
| `Live` | `Long` | `0.3985` | 225,870.00 USD | 0.00 USD | 403.46 USD | `-41.41%` | `1,012.44` |
| `Live` | `Long` | `0.3995` | 225,470.00 USD | 0.00 USD | 271.06 USD | `-41.26%` | `678.49` |
| `Live` | `Long` | `0.4035` | 225,200.00 USD | 0.00 USD | 570.81 USD | `-40.67%` | `1,414.65` |
| `Live` | `Long` | `0.4135` | 224,630.00 USD | 0.00 USD | 1,600.00 USD | `-39.20%` | `3,868.97` |
| `Live` | `Long` | `0.4185` | 223,030.00 USD | 0.00 USD | 630.86 USD | `-38.46%` | `1,507.44` |
| `Live` | `Long` | `0.4255` | 222,400.00 USD | 0.00 USD | 224.96 USD | `-37.44%` | `528.69` |
| `Live` | `Long` | `0.4405` | 222,170.00 USD | 0.00 USD | 4,300.00 USD | `-35.23%` | `9,753.33` |
| `Live` | `Long` | `0.4475` | 217,880.00 USD | 0.00 USD | 226.63 USD | `-34.20%` | `506.43` |
| `Live` | `Long` | `0.4515` | 217,650.00 USD | 0.00 USD | 27,090.00 USD | `-33.61%` | `60,000.00` |
| `Live` | `Long` | `0.4525` | 190,560.00 USD | 0.00 USD | 147.06 USD | `-33.47%` | `325.00` |
| `Live` | `Long` | `0.4605` | 190,410.00 USD | 0.00 USD | 125.38 USD | `-32.29%` | `272.27` |
| `Live` | `Long` | `0.4625` | 190,290.00 USD | 0.00 USD | 1,100.00 USD | `-32.00%` | `2,368.95` |
| `Live` | `Long` | `0.4685` | 189,190.00 USD | 0.00 USD | 468.50 USD | `-31.11%` | `1,000.00` |
| `Live` | `Long` | `0.4695` | 188,720.00 USD | 0.00 USD | 7,750.00 USD | `-30.97%` | `16,497.37` |
| `Live` | `Long` | `0.4755` | 180,980.00 USD | 0.00 USD | 5,890.00 USD | `-30.08%` | `12,386.80` |
| `Live` | `Long` | `0.4765` | 175,090.00 USD | 0.00 USD | 990.20 USD | `-29.94%` | `2,078.06` |
| `Live` | `Long` | `0.4835` | 174,100.00 USD | 0.00 USD | 135.33 USD | `-28.91%` | `279.90` |
| `Live` | `Long` | `0.4855` | 173,960.00 USD | 0.00 USD | 3,160.00 USD | `-28.61%` | `6,508.47` |
| `Live` | `Long` | `0.4985` | 170,800.00 USD | 0.00 USD | 429.90 USD | `-26.70%` | `862.38` |
| `Live` | `Long` | `0.5085` | 170,370.00 USD | 0.00 USD | 102.82 USD | `-25.23%` | `202.20` |
| `Live` | `Long` | `0.5095` | 170,270.00 USD | 0.00 USD | 2,550.00 USD | `-25.08%` | `5,003.93` |
| `Live` | `Long` | `0.5125` | 167,720.00 USD | 0.00 USD | 248.05 USD | `-24.64%` | `484.00` |
| `Live` | `Long` | `0.5135` | 167,470.00 USD | 0.00 USD | 110.50 USD | `-24.50%` | `215.19` |
| `Live` | `Long` | `0.5145` | 167,360.00 USD | 0.00 USD | 288.78 USD | `-24.35%` | `561.28` |
| `Live` | `Long` | `0.5175` | 167,070.00 USD | 0.00 USD | 9,440.00 USD | `-23.91%` | `18,249.92` |
| `Live` | `Long` | `0.5315` | 157,630.00 USD | 0.00 USD | 11,510.00 USD | `-21.85%` | `21,664.95` |
| `Live` | `Long` | `0.5335` | 146,110.00 USD | 0.00 USD | 163.22 USD | `-21.56%` | `305.95` |
| `Live` | `Long` | `0.5385` | 145,950.00 USD | 0.00 USD | 2,690.00 USD | `-20.82%` | `5,002.20` |
| `Live` | `Long` | `0.5445` | 143,260.00 USD | 0.00 USD | 330.14 USD | `-19.94%` | `606.32` |
| `Live` | `Long` | `0.5495` | 142,930.00 USD | 0.00 USD | 630.26 USD | `-19.20%` | `1,146.97` |
| `Live` | `Long` | `0.5515` | 142,300.00 USD | 0.00 USD | 3,220.00 USD | `-18.91%` | `5,839.42` |
| `Live` | `Long` | `0.5545` | 139,070.00 USD | 0.00 USD | 47,450.00 USD | `-18.47%` | `85,578.81` |
| `Live` | `Long` | `0.5585` | 91,620.00 USD | 0.00 USD | 10,520.00 USD | `-17.88%` | `18,834.52` |
| `Live` | `Long` | `0.5615` | 81,100.00 USD | 0.00 USD | 1,720.00 USD | `-17.44%` | `3,064.43` |
| `Live` | `Long` | `0.5695` | 79,380.00 USD | 0.00 USD | 164.24 USD | `-16.26%` | `288.40` |
| `Live` | `Long` | `0.5715` | 79,220.00 USD | 0.00 USD | 289.08 USD | `-15.97%` | `505.82` |
| `Live` | `Long` | `0.5735` | 78,930.00 USD | 0.00 USD | 214.84 USD | `-15.67%` | `374.62` |
| `Live` | `Long` | `0.5745` | 78,710.00 USD | 0.00 USD | 22,080.00 USD | `-15.53%` | `38,425.61` |
| `Live` | `Long` | `0.5785` | 56,640.00 USD | 0.00 USD | 2,730.00 USD | `-14.94%` | `4,721.26` |
| `Live` | `Long` | `0.5795` | 53,910.00 USD | 0.00 USD | 663.74 USD | `-14.79%` | `1,145.36` |
| `Live` | `Long` | `0.5835` | 53,240.00 USD | 0.00 USD | 132.92 USD | `-14.20%` | `227.80` |
| `Live` | `Long` | `0.5845` | 53,110.00 USD | 0.00 USD | 210.96 USD | `-14.06%` | `360.92` |
| `Live` | `Long` | `0.5865` | 52,900.00 USD | 0.00 USD | 586.80 USD | `-13.76%` | `1,000.51` |
| `Live` | `Long` | `0.5885` | 52,310.00 USD | 0.00 USD | 440.16 USD | `-13.47%` | `747.93` |
| `Live` | `Long` | `0.5895` | 51,870.00 USD | 0.00 USD | 1,690.00 USD | `-13.32%` | `2,865.95` |
| `Live` | `Long` | `0.5925` | 50,180.00 USD | 0.00 USD | 609.14 USD | `-12.88%` | `1,028.09` |
| `Live` | `Long` | `0.5935` | 49,570.00 USD | 0.00 USD | 572.40 USD | `-12.73%` | `964.45` |
| `Live` | `Long` | `0.5945` | 49,000.00 USD | 0.00 USD | 3,850.00 USD | `-12.59%` | `6,467.73` |
| `Live` | `Long` | `0.5975` | 45,160.00 USD | 0.00 USD | 157.22 USD | `-12.15%` | `263.13` |
| `Live` | `Long` | `0.6005` | 45,000.00 USD | 0.00 USD | 852.06 USD | `-11.70%` | `1,418.92` |
| `Live` | `Long` | `0.6045` | 44,150.00 USD | 0.00 USD | 527.44 USD | `-11.12%` | `872.53` |
| `Live` | `Long` | `0.6055` | 43,620.00 USD | 0.00 USD | 453.44 USD | `-10.97%` | `748.87` |
| `Live` | `Long` | `0.6105` | 43,170.00 USD | 0.00 USD | 6,090.00 USD | `-10.23%` | `9,974.00` |
| `Live` | `Long` | `0.6195` | 37,080.00 USD | 0.00 USD | 3,170.00 USD | `-8.91%` | `5,109.42` |
| `Live` | `Long` | `0.6235` | 33,910.00 USD | 0.00 USD | 3,250.00 USD | `-8.32%` | `5,220.30` |
| `Live` | `Long` | `0.6255` | 30,660.00 USD | 0.00 USD | 286.65 USD | `-8.03%` | `458.28` |
| `Live` | `Long` | `0.6265` | 30,370.00 USD | 0.00 USD | 10,530.00 USD | `-7.88%` | `16,808.62` |
| `Live` | `Long` | `0.6285` | 19,840.00 USD | 0.00 USD | 903.47 USD | `-7.59%` | `1,437.50` |
| `Live` | `Long` | `0.6315` | 18,940.00 USD | 0.00 USD | 1,010.00 USD | `-7.15%` | `1,599.74` |
| `Live` | `Long` | `0.6375` | 17,930.00 USD | 0.00 USD | 5,900.00 USD | `-6.26%` | `9,256.34` |
| `Live` | `Long` | `0.6415` | 12,020.00 USD | 0.00 USD | 4,740.00 USD | `-5.68%` | `7,394.26` |
| `Live` | `Long` | `0.6435` | 7,280.00 USD | 0.00 USD | 2,320.00 USD | `-5.38%` | `3,602.46` |
| `Live` | `Long` | `0.6455` | 4,960.00 USD | 0.00 USD | 3,730.00 USD | `-5.09%` | `5,780.73` |
| `Live` | `Short` | `0.6475` | 574.36 USD | 574.36 USD | 0.00 USD | `-4.79%` | `887.04` |
| `Live` | `Long` | `0.6485` | 1,230.00 USD | 0.00 USD | 259.68 USD | `-4.65%` | `400.43` |
| `Live` | `Long` | `0.6535` | 972.07 USD | 0.00 USD | 153.10 USD | `-3.91%` | `234.27` |
| `Live` | `Long` | `0.6695` | 818.97 USD | 0.00 USD | 818.97 USD | `-1.56%` | `1,223.26` |
| `Live` | `Short` | `0.7125` | 676.22 USD | 101.87 USD | 0.00 USD | `+4.76%` | `142.97` |
| `Live` | `Short` | `0.7185` | 2,780.00 USD | 2,110.00 USD | 0.00 USD | `+5.65%` | `2,934.09` |
| `Live` | `Short` | `0.7245` | 45,820.00 USD | 43,040.00 USD | 0.00 USD | `+6.53%` | `59,401.36` |
| `Live` | `Short` | `0.7255` | 46,670.00 USD | 853.84 USD | 0.00 USD | `+6.68%` | `1,176.90` |
| `Live` | `Short` | `0.7265` | 46,800.00 USD | 124.62 USD | 0.00 USD | `+6.82%` | `171.53` |
| `Live` | `Short` | `0.7345` | 46,950.00 USD | 150.17 USD | 0.00 USD | `+8.00%` | `204.45` |
| `Live` | `Short` | `0.7635` | 47,090.00 USD | 143.11 USD | 0.00 USD | `+12.26%` | `187.44` |
| `Live` | `Short` | `0.7725` | 47,260.00 USD | 165.62 USD | 0.00 USD | `+13.59%` | `214.40` |
| `Live` | `Short` | `0.7765` | 47,590.00 USD | 330.78 USD | 0.00 USD | `+14.17%` | `425.99` |
| `Live` | `Short` | `0.7865` | 47,700.00 USD | 114.35 USD | 0.00 USD | `+15.64%` | `145.39` |
| `Live` | `Short` | `0.8005` | 66,820.00 USD | 19,120.00 USD | 0.00 USD | `+17.70%` | `23,882.80` |
| `Live` | `Short` | `0.8035` | 66,940.00 USD | 114.11 USD | 0.00 USD | `+18.14%` | `142.02` |
| `Live` | `Short` | `0.8615` | 82,580.00 USD | 15,640.00 USD | 0.00 USD | `+26.67%` | `18,155.35` |
| `Live` | `Short` | `0.8665` | 82,960.00 USD | 378.95 USD | 0.00 USD | `+27.41%` | `437.33` |
| `Live` | `Short` | `0.9935` | 83,120.00 USD | 166.01 USD | 0.00 USD | `+46.08%` | `167.10` |
| `Live` | `Short` | `1.02` | 103,720.00 USD | 20,600.00 USD | 0.00 USD | `+49.61%` | `20,242.35` |
| `Live` | `Short` | `1.07` | 185,020.00 USD | 81,300.00 USD | 0.00 USD | `+56.67%` | `76,300.00` |
| `Live` | `Short` | `1.07` | 203,890.00 USD | 18,870.00 USD | 0.00 USD | `+57.26%` | `17,648.14` |
| `Live` | `Short` | `1.09` | 206,970.00 USD | 3,080.00 USD | 0.00 USD | `+59.90%` | `2,829.20` |
| `Live` | `Short` | `1.09` | 207,450.00 USD | 479.74 USD | 0.00 USD | `+60.49%` | `439.52` |
| `Live` | `Short` | `1.10` | 207,640.00 USD | 192.76 USD | 0.00 USD | `+62.40%` | `174.52` |
| `Live` | `Short` | `1.12` | 210,440.00 USD | 2,800.00 USD | 0.00 USD | `+64.61%` | `2,500.00` |
| `Live` | `Short` | `1.27` | 223,760.00 USD | 13,320.00 USD | 0.00 USD | `+86.52%` | `10,500.00` |
| `Live` | `Short` | `1.32` | 223,950.00 USD | 197.51 USD | 0.00 USD | `+94.31%` | `149.46` |
| `Live` | `Short` | `1.33` | 224,240.00 USD | 284.61 USD | 0.00 USD | `+95.49%` | `214.07` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.3505` | 122,250.00 USD | 0.00 USD | 340.19 USD | `-48.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4635` | 121,910.00 USD | 0.00 USD | 104.57 USD | `-31.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4805` | 121,810.00 USD | 0.00 USD | 14,740.00 USD | `-29.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 107,070.00 USD | 0.00 USD | 604.46 USD | `-26.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5125` | 106,460.00 USD | 0.00 USD | 5,380.00 USD | `-24.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5205` | 101,080.00 USD | 0.00 USD | 228.77 USD | `-23.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5305` | 100,850.00 USD | 0.00 USD | 770.19 USD | `-22.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5445` | 100,080.00 USD | 0.00 USD | 14,110.00 USD | `-19.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5455` | 85,970.00 USD | 0.00 USD | 7,540.00 USD | `-19.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5485` | 78,440.00 USD | 0.00 USD | 4,500.00 USD | `-19.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5555` | 73,940.00 USD | 0.00 USD | 33,000.00 USD | `-18.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5565` | 40,940.00 USD | 0.00 USD | 173.58 USD | `-18.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 40,770.00 USD | 0.00 USD | 339.84 USD | `-17.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5835` | 40,430.00 USD | 0.00 USD | 178.88 USD | `-14.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5865` | 40,250.00 USD | 0.00 USD | 128.36 USD | `-13.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5875` | 40,120.00 USD | 0.00 USD | 128.34 USD | `-13.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5895` | 39,990.00 USD | 0.00 USD | 128.45 USD | `-13.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5925` | 39,870.00 USD | 0.00 USD | 128.33 USD | `-12.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5975` | 39,740.00 USD | 0.00 USD | 597.80 USD | `-12.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 39,140.00 USD | 0.00 USD | 3,510.00 USD | `-11.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 35,630.00 USD | 0.00 USD | 1,510.00 USD | `-10.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6085` | 34,130.00 USD | 0.00 USD | 301.32 USD | `-10.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6115` | 33,820.00 USD | 0.00 USD | 2,230.00 USD | `-10.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6125` | 31,600.00 USD | 0.00 USD | 108.68 USD | `-9.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6185` | 31,490.00 USD | 0.00 USD | 177.58 USD | `-9.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 31,310.00 USD | 0.00 USD | 541.40 USD | `-8.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6285` | 30,770.00 USD | 0.00 USD | 469.94 USD | `-7.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 30,300.00 USD | 0.00 USD | 4,430.00 USD | `-7.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6315` | 25,870.00 USD | 0.00 USD | 160.16 USD | `-7.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6335` | 25,710.00 USD | 0.00 USD | 8,390.00 USD | `-6.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6345` | 17,320.00 USD | 0.00 USD | 276.40 USD | `-6.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6395` | 17,040.00 USD | 0.00 USD | 1,200.00 USD | `-5.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6405` | 15,840.00 USD | 0.00 USD | 145.91 USD | `-5.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6485` | 15,700.00 USD | 0.00 USD | 447.03 USD | `-4.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 15,250.00 USD | 0.00 USD | 567.58 USD | `-4.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6525` | 14,680.00 USD | 0.00 USD | 111.92 USD | `-4.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 14,570.00 USD | 0.00 USD | 349.76 USD | `-3.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 14,220.00 USD | 0.00 USD | 4,080.00 USD | `-3.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6565` | 10,140.00 USD | 0.00 USD | 284.88 USD | `-3.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6575` | 9,860.00 USD | 0.00 USD | 195.39 USD | `-3.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6585` | 9,660.00 USD | 0.00 USD | 1,440.00 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6595` | 8,220.00 USD | 0.00 USD | 746.46 USD | `-3.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6605` | 7,480.00 USD | 0.00 USD | 580.23 USD | `-2.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6655` | 6,900.00 USD | 0.00 USD | 1,110.00 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6665` | 5,790.00 USD | 0.00 USD | 151.65 USD | `-2.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6675` | 5,640.00 USD | 0.00 USD | 290.78 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6685` | 5,350.00 USD | 0.00 USD | 170.95 USD | `-1.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6695` | 5,180.00 USD | 0.00 USD | 1,670.00 USD | `-1.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 3,510.00 USD | 0.00 USD | 162.91 USD | `-1.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6715` | 3,350.00 USD | 0.00 USD | 202.63 USD | `-1.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6725` | 3,140.00 USD | 0.00 USD | 1,670.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6745` | 1,470.00 USD | 0.00 USD | 995.25 USD | `-0.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6755` | 473.04 USD | 0.00 USD | 361.53 USD | `-0.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6765` | 111.50 USD | 0.00 USD | 111.50 USD | `-0.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6805` | 214.20 USD | 214.20 USD | 0.00 USD | `+0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6815` | 10,770.00 USD | 10,560.00 USD | 0.00 USD | `+0.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6825` | 10,890.00 USD | 112.49 USD | 0.00 USD | `+0.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6835` | 11,000.00 USD | 108.41 USD | 0.00 USD | `+0.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6855` | 11,110.00 USD | 112.98 USD | 0.00 USD | `+0.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6865` | 11,400.00 USD | 292.33 USD | 0.00 USD | `+0.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6875` | 11,540.00 USD | 140.41 USD | 0.00 USD | `+1.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6885` | 12,060.00 USD | 514.80 USD | 0.00 USD | `+1.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6895` | 12,250.00 USD | 194.09 USD | 0.00 USD | `+1.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6905` | 15,080.00 USD | 2,830.00 USD | 0.00 USD | `+1.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6915` | 15,180.00 USD | 101.96 USD | 0.00 USD | `+1.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6925` | 16,200.00 USD | 1,020.00 USD | 0.00 USD | `+1.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6945` | 16,810.00 USD | 610.10 USD | 0.00 USD | `+2.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6955` | 17,780.00 USD | 972.94 USD | 0.00 USD | `+2.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6965` | 23,180.00 USD | 5,390.00 USD | 0.00 USD | `+2.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6985` | 23,280.00 USD | 102.99 USD | 0.00 USD | `+2.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7005` | 23,420.00 USD | 137.19 USD | 0.00 USD | `+3.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7015` | 23,980.00 USD | 561.40 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7025` | 25,020.00 USD | 1,030.00 USD | 0.00 USD | `+3.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7045` | 25,710.00 USD | 692.13 USD | 0.00 USD | `+3.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7055` | 29,720.00 USD | 4,010.00 USD | 0.00 USD | `+3.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7075` | 32,300.00 USD | 2,580.00 USD | 0.00 USD | `+4.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7085` | 33,240.00 USD | 947.29 USD | 0.00 USD | `+4.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7095` | 33,400.00 USD | 150.80 USD | 0.00 USD | `+4.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7115` | 33,520.00 USD | 122.04 USD | 0.00 USD | `+4.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7125` | 33,680.00 USD | 162.12 USD | 0.00 USD | `+4.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7135` | 33,990.00 USD | 307.58 USD | 0.00 USD | `+4.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7155` | 35,080.00 USD | 1,090.00 USD | 0.00 USD | `+5.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7165` | 36,920.00 USD | 1,830.00 USD | 0.00 USD | `+5.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7195` | 37,290.00 USD | 373.99 USD | 0.00 USD | `+5.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7205` | 37,440.00 USD | 147.15 USD | 0.00 USD | `+5.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7215` | 40,700.00 USD | 3,260.00 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7225` | 40,850.00 USD | 150.08 USD | 0.00 USD | `+6.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7265` | 47,270.00 USD | 6,410.00 USD | 0.00 USD | `+6.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7305` | 62,860.00 USD | 15,600.00 USD | 0.00 USD | `+7.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7325` | 63,030.00 USD | 165.17 USD | 0.00 USD | `+7.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7345` | 64,060.00 USD | 1,030.00 USD | 0.00 USD | `+8.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7375` | 64,160.00 USD | 106.75 USD | 0.00 USD | `+8.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7395` | 64,370.00 USD | 208.16 USD | 0.00 USD | `+8.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7405` | 65,100.00 USD | 733.09 USD | 0.00 USD | `+8.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7415` | 65,260.00 USD | 156.98 USD | 0.00 USD | `+9.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7425` | 65,390.00 USD | 132.95 USD | 0.00 USD | `+9.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7445` | 66,150.00 USD | 757.16 USD | 0.00 USD | `+9.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7455` | 68,320.00 USD | 2,170.00 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7475` | 68,640.00 USD | 318.43 USD | 0.00 USD | `+9.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7495` | 68,770.00 USD | 132.98 USD | 0.00 USD | `+10.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7505` | 68,880.00 USD | 110.33 USD | 0.00 USD | `+10.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7525` | 69,010.00 USD | 134.74 USD | 0.00 USD | `+10.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7565` | 73,130.00 USD | 4,120.00 USD | 0.00 USD | `+11.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7575` | 73,640.00 USD | 511.82 USD | 0.00 USD | `+11.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7585` | 73,780.00 USD | 135.82 USD | 0.00 USD | `+11.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7615` | 74,650.00 USD | 875.23 USD | 0.00 USD | `+11.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7635` | 74,760.00 USD | 103.35 USD | 0.00 USD | `+12.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7665` | 74,880.00 USD | 127.48 USD | 0.00 USD | `+12.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7675` | 74,980.00 USD | 101.61 USD | 0.00 USD | `+12.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7695` | 75,170.00 USD | 186.97 USD | 0.00 USD | `+13.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7705` | 75,280.00 USD | 109.43 USD | 0.00 USD | `+13.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7775` | 75,450.00 USD | 166.70 USD | 0.00 USD | `+14.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7815` | 76,580.00 USD | 1,140.00 USD | 0.00 USD | `+14.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7865` | 82,900.00 USD | 6,310.00 USD | 0.00 USD | `+15.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8095` | 83,030.00 USD | 133.42 USD | 0.00 USD | `+19.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8125` | 95,100.00 USD | 12,070.00 USD | 0.00 USD | `+19.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8235` | 97,990.00 USD | 2,890.00 USD | 0.00 USD | `+21.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8335` | 98,920.00 USD | 929.08 USD | 0.00 USD | `+22.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8475` | 139,510.00 USD | 40,590.00 USD | 0.00 USD | `+24.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8505` | 142,580.00 USD | 3,060.00 USD | 0.00 USD | `+25.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8515` | 153,610.00 USD | 11,030.00 USD | 0.00 USD | `+25.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8525` | 165,390.00 USD | 11,780.00 USD | 0.00 USD | `+25.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8705` | 166,670.00 USD | 1,280.00 USD | 0.00 USD | `+28.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8725` | 166,830.00 USD | 159.86 USD | 0.00 USD | `+28.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 170,110.00 USD | 3,290.00 USD | 0.00 USD | `+37.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 170,450.00 USD | 340.54 USD | 0.00 USD | `+39.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 170,600.00 USD | 145.72 USD | 0.00 USD | `+42.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 171,590.00 USD | 987.50 USD | 0.00 USD | `+45.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 171,720.00 USD | 136.10 USD | 0.00 USD | `+47.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 172,270.00 USD | 550.48 USD | 0.00 USD | `+47.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 172,590.00 USD | 314.99 USD | 0.00 USD | `+51.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 173,190.00 USD | 602.17 USD | 0.00 USD | `+54.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 173,550.00 USD | 360.61 USD | 0.00 USD | `+55.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 174,490.00 USD | 942.77 USD | 0.00 USD | `+58.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 174,830.00 USD | 337.31 USD | 0.00 USD | `+59.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 175,230.00 USD | 397.19 USD | 0.00 USD | `+61.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 188,360.00 USD | 13,130.00 USD | 0.00 USD | `+83.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 189,680.00 USD | 1,320.00 USD | 0.00 USD | `+85.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 226,540.00 USD | 36,850.00 USD | 0.00 USD | `+90.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 253,750.00 USD | 27,210.00 USD | 0.00 USD | `+100.04%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.5870` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 0.00 USD | 1,400.00 USD | 65.70 USD |
| `7D` | `0.5880` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 3,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.5890` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 15.37 USD |
| `7D` | `0.5900` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 3,120.00 USD | 1,560.00 USD | 0.00 USD |
| `7D` | `0.5920` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 0.00 USD | 2,820.00 USD | 0.00 USD |
| `7D` | `0.5930` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 10,090.00 USD | 0.00 USD | 9,780.00 USD |
| `7D` | `0.5950` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 5,120.00 USD | 0.00 USD | 4,530.00 USD |
| `7D` | `0.5960` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 5,120.00 USD | 1,640.00 USD | 46.83 USD |
| `7D` | `0.5970` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 9,710.00 USD |
| `7D` | `0.5980` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 7,660.00 USD | 826.53 USD | 3.00 USD |
| `7D` | `0.5990` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 3,320.00 USD | 1,340.00 USD | 14,100.00 USD |
| `7D` | `0.6000` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 0.00 USD | 796.28 USD | 4,700.00 USD |
| `7D` | `0.6020` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 4,890.00 USD | 8,040.00 USD | 4,010.00 USD |
| `1D` | `0.6030` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 5,230.00 USD | 1,970.00 USD | 3,690.00 USD |
| `7D` | `0.6030` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 2,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6040` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 4,530.00 USD | 963.47 USD | 1,860.00 USD |
| `7D` | `0.6040` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 7,830.00 USD |
| `1D` | `0.6050` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 0.00 USD | 599.00 USD | 1,200.00 USD |
| `1D` | `0.6060` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 2,880.00 USD | 606.70 USD | 3,070.00 USD |
| `7D` | `0.6060` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 2,850.00 USD | 0.00 USD | 32.95 USD |
| `1D` | `0.6070` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 1,490.00 USD | 1,030.00 USD | 4,730.00 USD |
| `7D` | `0.6070` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 32.69 USD |
| `1D` | `0.6080` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 1,240.00 USD | 0.00 USD | 3,970.00 USD |
| `7D` | `0.6080` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 2,860.00 USD | 0.00 USD | 124.87 USD |
| `1D` | `0.6090` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 2,110.00 USD | 0.00 USD | 42.25 USD |
| `7D` | `0.6090` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 6,360.00 USD | 0.00 USD | 9,570.00 USD |
| `1D` | `0.6100` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 3,960.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `0.6100` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 7,480.00 USD | 2,570.00 USD | 0.00 USD |
| `1D` | `0.6110` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 1,430.00 USD | 0.00 USD | 1,100.00 USD |
| `7D` | `0.6110` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 0.00 USD | 2,210.00 USD | 12,860.00 USD |
| `1D` | `0.6120` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 902.06 USD | 398.52 USD | 2,380.00 USD |
| `7D` | `0.6120` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 2,100.00 USD | 3,510.00 USD | 7,130.00 USD |
| `1D` | `0.6130` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 3,070.00 USD | 596.50 USD | 2,320.00 USD |
| `7D` | `0.6130` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 8,870.00 USD | 1,050.00 USD | 4,110.00 USD |
| `1D` | `0.6140` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 6,120.00 USD | 0.00 USD | 2,750.00 USD |
| `7D` | `0.6140` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 4,540.00 USD | 7,000.00 USD | 6,660.00 USD |
| `1D` | `0.6150` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 2,730.00 USD | 0.00 USD | 16.03 USD |
| `7D` | `0.6150` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 11,130.00 USD | 5,870.00 USD | 2,780.00 USD |
| `1D` | `0.6160` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 1,460.00 USD | 1,690.00 USD | 129.60 USD |
| `7D` | `0.6160` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 1,790.00 USD | 2,510.00 USD | 3,820.00 USD |
| `1D` | `0.6170` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 3,470.00 USD |
| `7D` | `0.6170` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 13,260.00 USD | 2,610.00 USD | 14,640.00 USD |
| `1D` | `0.6180` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 0.00 USD | 678.61 USD | 11.35 USD |
| `7D` | `0.6180` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 7,600.00 USD | 1,190.00 USD | 6,150.00 USD |
| `1D` | `0.6190` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 95.50 USD |
| `7D` | `0.6190` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 9,560.00 USD | 1,930.00 USD | 9,510.00 USD |
| `1D` | `0.6200` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 1,760.00 USD |
| `7D` | `0.6200` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 13,870.00 USD | 5,230.00 USD | 6,120.00 USD |
| `1D` | `0.6210` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 1,990.00 USD | 0.00 USD | 2,050.00 USD |
| `7D` | `0.6210` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 4,760.00 USD | 1,860.00 USD | 5,170.00 USD |
| `1D` | `0.6220` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 2,520.00 USD | 0.00 USD | 46.01 USD |
| `7D` | `0.6220` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 7,960.00 USD | 2,310.00 USD | 29,850.00 USD |
| `1D` | `0.6230` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 1,130.00 USD |
| `7D` | `0.6230` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 9,770.00 USD | 4,700.00 USD | 8,310.00 USD |
| `1D` | `0.6240` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 4,840.00 USD | 4,260.00 USD | 58.21 USD |
| `7D` | `0.6240` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 18,610.00 USD | 4,720.00 USD | 4,990.00 USD |
| `1D` | `0.6250` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 1,800.00 USD | 2,630.00 USD | 68.39 USD |
| `7D` | `0.6250` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 16,120.00 USD | 3,830.00 USD | 2,470.00 USD |
| `1D` | `0.6260` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 10,030.00 USD | 1,310.00 USD | 9,260.00 USD |
| `7D` | `0.6260` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 20,890.00 USD | 7,660.00 USD | 26,000.00 USD |
| `1D` | `0.6270` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 3,700.00 USD | 3,940.00 USD | 12,850.00 USD |
| `7D` | `0.6270` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 17,460.00 USD | 8,200.00 USD | 24,500.00 USD |
| `1D` | `0.6280` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 11,690.00 USD | 463.43 USD | 2,070.00 USD |
| `7D` | `0.6280` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 9,160.00 USD | 9,230.00 USD | 16,640.00 USD |
| `1D` | `0.6290` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 11,890.00 USD | 1,200.00 USD | 5,090.00 USD |
| `7D` | `0.6290` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 17,710.00 USD | 6,740.00 USD | 10,220.00 USD |
| `1D` | `0.6300` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 12,950.00 USD | 2,470.00 USD | 2,980.00 USD |
| `7D` | `0.6300` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 10,040.00 USD | 7,890.00 USD | 11,260.00 USD |
| `1D` | `0.6310` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 7,940.00 USD | 5,110.00 USD | 4,180.00 USD |
| `7D` | `0.6310` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 19,340.00 USD | 4,520.00 USD | 17,260.00 USD |
| `1D` | `0.6320` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 12,320.00 USD | 11,080.00 USD | 14,790.00 USD |
| `7D` | `0.6320` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 4,880.00 USD | 12,650.00 USD | 8,800.00 USD |
| `1D` | `0.6330` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 17,300.00 USD | 3,580.00 USD | 21,000.00 USD |
| `7D` | `0.6330` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 57,940.00 USD | 14,700.00 USD | 33,780.00 USD |
| `1D` | `0.6340` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 9,830.00 USD | 2,020.00 USD | 15,370.00 USD |
| `7D` | `0.6340` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 10,730.00 USD | 3,420.00 USD | 4,590.00 USD |
| `1D` | `0.6350` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 19,180.00 USD | 8,820.00 USD | 4,210.00 USD |
| `7D` | `0.6350` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 14,450.00 USD | 2,430.00 USD | 22,930.00 USD |
| `1D` | `0.6360` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 30,350.00 USD | 9,150.00 USD | 33,320.00 USD |
| `7D` | `0.6360` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 42,690.00 USD | 7,300.00 USD | 40,420.00 USD |
| `1D` | `0.6370` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 21,750.00 USD | 4,510.00 USD | 27,350.00 USD |
| `7D` | `0.6370` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 49,080.00 USD | 4,870.00 USD | 29.01 USD |
| `1D` | `0.6380` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 19,430.00 USD | 7,180.00 USD | 7,690.00 USD |
| `7D` | `0.6380` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 18,140.00 USD | 3,870.00 USD | 30,350.00 USD |
| `1D` | `0.6390` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 18,790.00 USD | 529.57 USD | 6,770.00 USD |
| `7D` | `0.6390` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 10,200.00 USD | 7,510.00 USD | 13,080.00 USD |
| `1D` | `0.6400` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 9,830.00 USD | 9,970.00 USD | 25,420.00 USD |
| `7D` | `0.6400` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 15,560.00 USD | 0.00 USD | 330.78 USD |
| `1D` | `0.6410` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 20,930.00 USD | 2,240.00 USD | 3,690.00 USD |
| `7D` | `0.6410` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 6,310.00 USD |
| `1D` | `0.6420` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 32,540.00 USD | 7,850.00 USD | 12,640.00 USD |
| `7D` | `0.6420` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 39,060.00 USD | 26,560.00 USD | 10,220.00 USD |
| `1D` | `0.6430` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 25,620.00 USD | 7,460.00 USD | 9,260.00 USD |
| `7D` | `0.6430` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 16,200.00 USD | 3,970.00 USD | 3,180.00 USD |
| `1D` | `0.6440` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 21,790.00 USD | 11,330.00 USD | 8,430.00 USD |
| `7D` | `0.6440` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 14,160.00 USD | 6,720.00 USD | 14,690.00 USD |
| `1D` | `0.6450` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 23,100.00 USD | 20,050.00 USD | 31,380.00 USD |
| `7D` | `0.6450` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 14,120.00 USD | 15,560.00 USD | 383.87 USD |
| `1D` | `0.6460` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 43,360.00 USD | 10,480.00 USD | 51,710.00 USD |
| `7D` | `0.6460` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 75,060.00 USD | 14,300.00 USD | 75,640.00 USD |
| `1D` | `0.6470` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 30,630.00 USD | 6,620.00 USD | 41,860.00 USD |
| `7D` | `0.6470` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 9,660.00 USD | 3,880.00 USD | 9,220.00 USD |
| `1D` | `0.6480` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 48,130.00 USD | 14,180.00 USD | 7,800.00 USD |
| `7D` | `0.6480` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 37,050.00 USD | 0.00 USD | 23,780.00 USD |
| `1D` | `0.6490` | 983,050.00 USD | 0.00 USD | 983,050.00 USD | 27,600.00 USD | 3,800.00 USD | 51,260.00 USD |
| `7D` | `0.6490` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 36,340.00 USD | 0.00 USD | 17,650.00 USD |
| `1D` | `0.6500` | 900,380.00 USD | 0.00 USD | 900,380.00 USD | 42,280.00 USD | 1,390.00 USD | 32,600.00 USD |
| `7D` | `0.6500` | 961,330.00 USD | 0.00 USD | 961,330.00 USD | 18,310.00 USD | 0.00 USD | 81,650.00 USD |
| `1D` | `0.6510` | 824,110.00 USD | 0.00 USD | 824,110.00 USD | 18,580.00 USD | 4,450.00 USD | 54,300.00 USD |
| `7D` | `0.6510` | 861,370.00 USD | 0.00 USD | 861,370.00 USD | 101,440.00 USD | 4,190.00 USD | 288.03 USD |
| `1D` | `0.6520` | 746,780.00 USD | 0.00 USD | 746,780.00 USD | 36,270.00 USD | 6,190.00 USD | 14,090.00 USD |
| `7D` | `0.6520` | 755,450.00 USD | 0.00 USD | 755,450.00 USD | 46,620.00 USD | 6,720.00 USD | 86,550.00 USD |
| `1D` | `0.6530` | 690,230.00 USD | 0.00 USD | 690,230.00 USD | 5,780.00 USD | 1,060.00 USD | 11,730.00 USD |
| `7D` | `0.6530` | 615,560.00 USD | 0.00 USD | 615,560.00 USD | 0.00 USD | 0.00 USD | 47,100.00 USD |
| `1D` | `0.6540` | 671,660.00 USD | 0.00 USD | 671,660.00 USD | 11,450.00 USD | 2,530.00 USD | 13,200.00 USD |
| `7D` | `0.6540` | 568,450.00 USD | 0.00 USD | 568,450.00 USD | 15,730.00 USD | 0.00 USD | 14,640.00 USD |
| `1D` | `0.6550` | 644,480.00 USD | 0.00 USD | 644,480.00 USD | 18,980.00 USD | 4,080.00 USD | 15,950.00 USD |
| `7D` | `0.6550` | 538,080.00 USD | 0.00 USD | 538,080.00 USD | 0.00 USD | 0.00 USD | 38,430.00 USD |
| `1D` | `0.6560` | 605,470.00 USD | 0.00 USD | 605,470.00 USD | 23,680.00 USD | 3,800.00 USD | 25,090.00 USD |
| `7D` | `0.6560` | 499,650.00 USD | 0.00 USD | 499,650.00 USD | 7,220.00 USD | 5,380.00 USD | 34,730.00 USD |
| `1D` | `0.6570` | 552,900.00 USD | 0.00 USD | 552,900.00 USD | 5,570.00 USD | 1,820.00 USD | 19,870.00 USD |
| `7D` | `0.6570` | 452,320.00 USD | 0.00 USD | 452,320.00 USD | 14,440.00 USD | 0.00 USD | 10,650.00 USD |
| `1D` | `0.6580` | 525,630.00 USD | 0.00 USD | 525,630.00 USD | 5,880.00 USD | 0.00 USD | 122.68 USD |
| `7D` | `0.6580` | 427,240.00 USD | 0.00 USD | 427,240.00 USD | 0.00 USD | 0.00 USD | 12,650.00 USD |
| `1D` | `0.6590` | 519,630.00 USD | 0.00 USD | 519,630.00 USD | 2,100.00 USD | 5,490.00 USD | 19,880.00 USD |
| `7D` | `0.6590` | 414,580.00 USD | 0.00 USD | 414,580.00 USD | 9,540.00 USD | 0.00 USD | 331.05 USD |
| `1D` | `0.6600` | 492,170.00 USD | 0.00 USD | 492,170.00 USD | 21,900.00 USD | 2,840.00 USD | 22,600.00 USD |
| `7D` | `0.6600` | 404,710.00 USD | 0.00 USD | 404,710.00 USD | 0.00 USD | 4,180.00 USD | 20,230.00 USD |
| `1D` | `0.6610` | 444,820.00 USD | 0.00 USD | 444,820.00 USD | 11,920.00 USD | 2,560.00 USD | 12,040.00 USD |
| `1D` | `0.6620` | 418,300.00 USD | 0.00 USD | 418,300.00 USD | 14,030.00 USD | 2,480.00 USD | 36,930.00 USD |
| `7D` | `0.6620` | 380,300.00 USD | 0.00 USD | 380,300.00 USD | 14,320.00 USD | 0.00 USD | 7,130.00 USD |
| `1D` | `0.6630` | 364,860.00 USD | 0.00 USD | 364,860.00 USD | 24,070.00 USD | 4,110.00 USD | 1,880.00 USD |
| `7D` | `0.6630` | 358,840.00 USD | 0.00 USD | 358,840.00 USD | 11,670.00 USD | 0.00 USD | 28,810.00 USD |
| `1D` | `0.6640` | 334,790.00 USD | 0.00 USD | 334,790.00 USD | 22,290.00 USD | 1,150.00 USD | 21,420.00 USD |
| `7D` | `0.6640` | 318,360.00 USD | 0.00 USD | 318,360.00 USD | 15,140.00 USD | 0.00 USD | 279.64 USD |
| `1D` | `0.6650` | 289,930.00 USD | 0.00 USD | 289,930.00 USD | 22,590.00 USD | 10,330.00 USD | 14,290.00 USD |
| `7D` | `0.6650` | 302,950.00 USD | 0.00 USD | 302,950.00 USD | 14,220.00 USD | 6,770.00 USD | 29,730.00 USD |
| `1D` | `0.6660` | 242,730.00 USD | 0.00 USD | 242,730.00 USD | 7,730.00 USD | 0.00 USD | 5,410.00 USD |
| `7D` | `0.6660` | 252,220.00 USD | 0.00 USD | 252,220.00 USD | 0.00 USD | 0.00 USD | 148.18 USD |
| `1D` | `0.6670` | 229,580.00 USD | 0.00 USD | 229,580.00 USD | 18,850.00 USD | 2,980.00 USD | 4,920.00 USD |
| `7D` | `0.6670` | 252,070.00 USD | 0.00 USD | 252,070.00 USD | 31,450.00 USD | 0.00 USD | 8,780.00 USD |
| `1D` | `0.6680` | 202,840.00 USD | 0.00 USD | 202,840.00 USD | 30,610.00 USD | 3,380.00 USD | 7,310.00 USD |
| `7D` | `0.6680` | 211,840.00 USD | 0.00 USD | 211,840.00 USD | 24,780.00 USD | 7,780.00 USD | 193.34 USD |
| `1D` | `0.6690` | 161,530.00 USD | 0.00 USD | 161,530.00 USD | 13,000.00 USD | 2,800.00 USD | 3,630.00 USD |
| `7D` | `0.6690` | 179,090.00 USD | 0.00 USD | 179,090.00 USD | 14,440.00 USD | 2,330.00 USD | 24,430.00 USD |
| `1D` | `0.6700` | 142,110.00 USD | 0.00 USD | 142,110.00 USD | 3,250.00 USD | 1,050.00 USD | 4,190.00 USD |
| `7D` | `0.6700` | 137,890.00 USD | 0.00 USD | 137,890.00 USD | 0.00 USD | 0.00 USD | 323.96 USD |
| `1D` | `0.6710` | 133,620.00 USD | 0.00 USD | 133,620.00 USD | 8,650.00 USD | 18,100.00 USD | 0.00 USD |
| `7D` | `0.6710` | 137,560.00 USD | 0.00 USD | 137,560.00 USD | 0.00 USD | 6,960.00 USD | 25,020.00 USD |
| `1D` | `0.6720` | 106,870.00 USD | 0.00 USD | 106,870.00 USD | 4,190.00 USD | 3,200.00 USD | 17,150.00 USD |
| `1D` | `0.6730` | 82,330.00 USD | 0.00 USD | 82,330.00 USD | 5,220.00 USD | 2,020.00 USD | 7,600.00 USD |
| `7D` | `0.6730` | 105,590.00 USD | 0.00 USD | 105,590.00 USD | 0.00 USD | 0.00 USD | 99.42 USD |
| `1D` | `0.6740` | 67,480.00 USD | 0.00 USD | 67,480.00 USD | 20,500.00 USD | 4,800.00 USD | 2,330.00 USD |
| `1D` | `0.6750` | 39,860.00 USD | 0.00 USD | 39,860.00 USD | 0.00 USD | 5,970.00 USD | 0.00 USD |
| `7D` | `0.6750` | 105,490.00 USD | 0.00 USD | 105,490.00 USD | 0.00 USD | 75,730.00 USD | 0.00 USD |
| `1D` | `0.6760` | 33,880.00 USD | 0.00 USD | 33,880.00 USD | 9,950.00 USD | 2,630.00 USD | 0.00 USD |
| `7D` | `0.6760` | 29,770.00 USD | 0.00 USD | 29,770.00 USD | 0.00 USD | 2,240.00 USD | 0.00 USD |
| `1D` | `0.6770` | 21,310.00 USD | 0.00 USD | 21,310.00 USD | 18,650.00 USD | 2,660.00 USD | 0.00 USD |
| `7D` | `0.6770` | 27,530.00 USD | 0.00 USD | 27,530.00 USD | 23,340.00 USD | 4,190.00 USD | 0.00 USD |
| `1D` | `0.6780` | 21,410.00 USD | 21,410.00 USD | 0.00 USD | 0.00 USD | 12,640.00 USD | 8,770.00 USD |
| `1D` | `0.6780` | 42,820.00 USD | 42,820.00 USD | 0.00 USD | 0.00 USD | 12,640.00 USD | 8,770.00 USD |
| `7D` | `0.6780` | 10,220.00 USD | 10,220.00 USD | 0.00 USD | 0.00 USD | 10,220.00 USD | 0.00 USD |
| `7D` | `0.6780` | 20,430.00 USD | 20,430.00 USD | 0.00 USD | 0.00 USD | 10,220.00 USD | 0.00 USD |
| `1D` | `0.6790` | 75,640.00 USD | 75,640.00 USD | 0.00 USD | 0.00 USD | 18,610.00 USD | 14,210.00 USD |
| `7D` | `0.6790` | 37,020.00 USD | 37,020.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 0.00 USD |
| `7D` | `0.6810` | 52,740.00 USD | 52,740.00 USD | 0.00 USD | 0.00 USD | 15,720.00 USD | 0.00 USD |
| `1D` | `0.6820` | 80,560.00 USD | 80,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,920.00 USD |
| `7D` | `0.6820` | 90,470.00 USD | 90,470.00 USD | 0.00 USD | 0.00 USD | 37,730.00 USD | 0.00 USD |
| `1D` | `0.6830` | 126,490.00 USD | 126,490.00 USD | 0.00 USD | 0.00 USD | 20,240.00 USD | 25,690.00 USD |
| `7D` | `0.6830` | 143,390.00 USD | 143,390.00 USD | 0.00 USD | 0.00 USD | 4,670.00 USD | 48,260.00 USD |
| `1D` | `0.6840` | 157,350.00 USD | 157,350.00 USD | 0.00 USD | 6,510.00 USD | 15,960.00 USD | 8,380.00 USD |
| `7D` | `0.6840` | 197,140.00 USD | 197,140.00 USD | 0.00 USD | 0.00 USD | 14,650.00 USD | 39,100.00 USD |
| `1D` | `0.6850` | 203,830.00 USD | 203,830.00 USD | 0.00 USD | 46,480.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6850` | 201,850.00 USD | 201,850.00 USD | 0.00 USD | 0.00 USD | 4,710.00 USD | 0.00 USD |
| `1D` | `0.6860` | 203,870.00 USD | 203,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43.12 USD |
| `7D` | `0.6860` | 211,690.00 USD | 211,690.00 USD | 0.00 USD | 0.00 USD | 9,830.00 USD | 0.00 USD |
| `1D` | `0.6870` | 203,880.00 USD | 203,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7.22 USD |
| `1D` | `0.6880` | 242,280.00 USD | 242,280.00 USD | 0.00 USD | 0.00 USD | 9,600.00 USD | 28,800.00 USD |
| `7D` | `0.6880` | 247,150.00 USD | 247,150.00 USD | 0.00 USD | 18,170.00 USD | 17,300.00 USD | 0.00 USD |
| `1D` | `0.6890` | 245,040.00 USD | 245,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,750.00 USD |
| `7D` | `0.6890` | 258,190.00 USD | 258,190.00 USD | 0.00 USD | 0.00 USD | 11,030.00 USD | 0.00 USD |
| `1D` | `0.6900` | 266,050.00 USD | 266,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,010.00 USD |
| `7D` | `0.6900` | 262,670.00 USD | 262,670.00 USD | 0.00 USD | 0.00 USD | 4,480.00 USD | 0.00 USD |
| `1D` | `0.6910` | 293,110.00 USD | 293,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 27,060.00 USD |
| `7D` | `0.6910` | 293,450.00 USD | 293,450.00 USD | 0.00 USD | 0.00 USD | 2,090.00 USD | 28,680.00 USD |
| `1D` | `0.6920` | 293,130.00 USD | 293,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20.06 USD |
| `7D` | `0.6920` | 317,810.00 USD | 317,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,370.00 USD |
| `1D` | `0.6930` | 303,340.00 USD | 303,340.00 USD | 0.00 USD | 10,030.00 USD | 0.00 USD | 172.88 USD |
| `7D` | `0.6930` | 374,640.00 USD | 374,640.00 USD | 0.00 USD | 14,220.00 USD | 0.00 USD | 42,600.00 USD |
| `1D` | `0.6940` | 327,220.00 USD | 327,220.00 USD | 0.00 USD | 11,230.00 USD | 4,420.00 USD | 8,240.00 USD |
| `1D` | `0.6950` | 354,180.00 USD | 354,180.00 USD | 0.00 USD | 22,480.00 USD | 4,460.00 USD | 15.14 USD |
| `7D` | `0.6950` | 418,480.00 USD | 418,480.00 USD | 0.00 USD | 31,450.00 USD | 0.00 USD | 12,390.00 USD |
| `1D` | `0.6960` | 401,370.00 USD | 401,370.00 USD | 0.00 USD | 47,070.00 USD | 0.00 USD | 127.40 USD |
| `7D` | `0.6960` | 430,700.00 USD | 430,700.00 USD | 0.00 USD | 12,220.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6970` | 424,810.00 USD | 424,810.00 USD | 0.00 USD | 23,380.00 USD | 0.00 USD | 53.96 USD |
| `7D` | `0.6970` | 452,350.00 USD | 452,350.00 USD | 0.00 USD | 21,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6980` | 424,820.00 USD | 424,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11.73 USD |
| `1D` | `0.6990` | 426,810.00 USD | 426,810.00 USD | 0.00 USD | 0.00 USD | 1,940.00 USD | 52.56 USD |
| `7D` | `0.6990` | 482,080.00 USD | 482,080.00 USD | 0.00 USD | 4,770.00 USD | 0.00 USD | 24,960.00 USD |
| `1D` | `0.7000` | 444,120.00 USD | 444,120.00 USD | 0.00 USD | 4,190.00 USD | 2,120.00 USD | 10,990.00 USD |
| `7D` | `0.7000` | 492,070.00 USD | 492,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,990.00 USD |
| `1D` | `0.7010` | 444,140.00 USD | 444,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20.98 USD |
| `1D` | `0.7020` | 458,520.00 USD | 458,520.00 USD | 0.00 USD | 14,360.00 USD | 0.00 USD | 22.18 USD |
| `7D` | `0.7020` | 561,500.00 USD | 561,500.00 USD | 0.00 USD | 16,350.00 USD | 0.00 USD | 53,080.00 USD |
| `1D` | `0.7030` | 469,030.00 USD | 469,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,510.00 USD |
| `7D` | `0.7030` | 688,580.00 USD | 688,580.00 USD | 0.00 USD | 76,610.00 USD | 0.00 USD | 50,470.00 USD |
| `1D` | `0.7040` | 505,910.00 USD | 505,910.00 USD | 0.00 USD | 19,130.00 USD | 2,630.00 USD | 15,120.00 USD |
| `7D` | `0.7040` | 734,360.00 USD | 734,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 45,780.00 USD |
| `1D` | `0.7050` | 556,900.00 USD | 556,900.00 USD | 0.00 USD | 36,240.00 USD | 2,660.00 USD | 12,090.00 USD |
| `7D` | `0.7050` | 885,460.00 USD | 885,460.00 USD | 0.00 USD | 27,630.00 USD | 0.00 USD | 123,470.00 USD |
| `1D` | `0.7060` | 581,720.00 USD | 581,720.00 USD | 0.00 USD | 8,590.00 USD | 3,860.00 USD | 12,370.00 USD |
| `7D` | `0.7060` | 993,710.00 USD | 993,710.00 USD | 0.00 USD | 20,200.00 USD | 33,490.00 USD | 54,560.00 USD |
| `1D` | `0.7070` | 640,690.00 USD | 640,690.00 USD | 0.00 USD | 19,980.00 USD | 21,860.00 USD | 17,120.00 USD |
| `7D` | `0.7070` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 8,720.00 USD | 36,300.00 USD | 28,970.00 USD |
| `1D` | `0.7080` | 666,860.00 USD | 666,860.00 USD | 0.00 USD | 18,420.00 USD | 3,500.00 USD | 4,240.00 USD |
| `7D` | `0.7080` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 15,730.00 USD | 28,570.00 USD | 53,590.00 USD |
| `1D` | `0.7090` | 705,320.00 USD | 705,320.00 USD | 0.00 USD | 23,150.00 USD | 6,370.00 USD | 8,940.00 USD |
| `7D` | `0.7090` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 106,000.00 USD | 32,830.00 USD | 134,470.00 USD |
| `1D` | `0.7100` | 740,290.00 USD | 740,290.00 USD | 0.00 USD | 10,040.00 USD | 3,180.00 USD | 21,740.00 USD |
| `7D` | `0.7100` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 44,820.00 USD | 30,700.00 USD | 14,310.00 USD |
| `1D` | `0.7110` | 763,940.00 USD | 763,940.00 USD | 0.00 USD | 6,300.00 USD | 8,760.00 USD | 8,600.00 USD |
| `7D` | `0.7110` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 40,300.00 USD | 33,410.00 USD | 92,890.00 USD |
| `1D` | `0.7120` | 805,730.00 USD | 805,730.00 USD | 0.00 USD | 21,700.00 USD | 4,410.00 USD | 15,680.00 USD |
| `7D` | `0.7120` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 60,730.00 USD | 45,350.00 USD | 135,200.00 USD |
| `1D` | `0.7130` | 877,170.00 USD | 877,170.00 USD | 0.00 USD | 28,640.00 USD | 3,110.00 USD | 39,690.00 USD |
| `7D` | `0.7130` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 75,250.00 USD | 31,940.00 USD | 51,140.00 USD |
| `1D` | `0.7140` | 918,460.00 USD | 918,460.00 USD | 0.00 USD | 27,390.00 USD | 7,490.00 USD | 6,410.00 USD |
| `7D` | `0.7140` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 127,300.00 USD | 35,310.00 USD | 81,980.00 USD |
| `1D` | `0.7150` | 966,980.00 USD | 966,980.00 USD | 0.00 USD | 18,260.00 USD | 6,980.00 USD | 23,280.00 USD |
| `7D` | `0.7150` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 50,460.00 USD | 26,770.00 USD | 96,210.00 USD |
| `1D` | `0.7160` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 17,400.00 USD | 11,180.00 USD | 10,820.00 USD |
| `7D` | `0.7160` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 62,580.00 USD | 38,490.00 USD | 68,020.00 USD |
| `1D` | `0.7170` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 4,910.00 USD | 3,880.00 USD | 8,640.00 USD |
| `7D` | `0.7170` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 105,890.00 USD | 35,770.00 USD | 53,830.00 USD |
| `1D` | `0.7180` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 6,240.00 USD | 2,890.00 USD | 14,890.00 USD |
| `7D` | `0.7180` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 59,980.00 USD | 21,140.00 USD | 12,710.00 USD |
| `1D` | `0.7190` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 12,780.00 USD | 8,180.00 USD | 1,990.00 USD |
| `7D` | `0.7190` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 28,670.00 USD | 11,840.00 USD | 87,990.00 USD |
| `1D` | `0.7200` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 4,740.00 USD | 14,740.00 USD |
| `7D` | `0.7200` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 65,080.00 USD | 33,310.00 USD | 89,960.00 USD |
| `1D` | `0.7210` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 10,550.00 USD | 14,540.00 USD | 7,200.00 USD |
| `7D` | `0.7210` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 206,240.00 USD | 24,720.00 USD | 70,620.00 USD |
| `1D` | `0.7220` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 23,430.00 USD | 5,070.00 USD | 23,250.00 USD |
| `7D` | `0.7220` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 112,190.00 USD | 42,410.00 USD | 27,520.00 USD |
| `1D` | `0.7230` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 3,920.00 USD | 4,060.00 USD | 27,860.00 USD |
| `7D` | `0.7230` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 59,050.00 USD | 10,400.00 USD | 93,940.00 USD |
| `1D` | `0.7240` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 2,920.00 USD | 4,240.00 USD | 12,020.00 USD |
| `7D` | `0.7240` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 75,360.00 USD | 14,510.00 USD | 28,980.00 USD |
| `1D` | `0.7250` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 4,760.00 USD | 3,950.00 USD | 9,380.00 USD |
| `7D` | `0.7250` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 52,270.00 USD | 25,530.00 USD | 82,450.00 USD |
| `1D` | `0.7260` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 11,880.00 USD | 6,730.00 USD | 12,310.00 USD |
| `7D` | `0.7260` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 54,140.00 USD | 26,590.00 USD | 93,000.00 USD |
| `1D` | `0.7270` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 19,920.00 USD | 2,760.00 USD | 14,500.00 USD |
| `7D` | `0.7270` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 49,240.00 USD | 18,120.00 USD | 33,460.00 USD |
| `1D` | `0.7280` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 16,410.00 USD | 5,780.00 USD | 11,740.00 USD |
| `7D` | `0.7280` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 42,560.00 USD | 22,060.00 USD | 50,400.00 USD |
| `1D` | `0.7290` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 13,150.00 USD | 7,110.00 USD | 27,190.00 USD |
| `7D` | `0.7290` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 47,200.00 USD | 32,380.00 USD | 69,820.00 USD |
| `1D` | `0.7300` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 9,980.00 USD | 9,840.00 USD | 25,690.00 USD |
| `7D` | `0.7300` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 55,390.00 USD | 27,940.00 USD | 29,400.00 USD |
| `1D` | `0.7310` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 1,010.00 USD | 1,670.00 USD | 7,070.00 USD |
| `7D` | `0.7310` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 115,470.00 USD | 40,620.00 USD | 31,210.00 USD |
| `1D` | `0.7320` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 5,780.00 USD | 1,140.00 USD | 12,420.00 USD |
| `7D` | `0.7320` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 74,380.00 USD | 25,020.00 USD | 49,250.00 USD |
| `1D` | `0.7330` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 6,450.00 USD | 3,420.00 USD | 4,460.00 USD |
| `7D` | `0.7330` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 32,440.00 USD |
| `1D` | `0.7340` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 1,620.00 USD | 1,530.00 USD | 5,220.00 USD |
| `7D` | `0.7340` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 31,260.00 USD | 8,620.00 USD | 30,810.00 USD |
| `1D` | `0.7350` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 735.24 USD | 1,470.00 USD | 21.86 USD |
| `7D` | `0.7350` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 66,390.00 USD | 15,820.00 USD | 15,550.00 USD |
| `1D` | `0.7360` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 10,900.00 USD | 2,960.00 USD | 14,920.00 USD |
| `7D` | `0.7360` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 37,210.00 USD | 30,980.00 USD | 19,430.00 USD |
| `1D` | `0.7370` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 1,110.00 USD | 1,970.00 USD | 9,870.00 USD |
| `7D` | `0.7370` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 9,640.00 USD | 3,860.00 USD | 20,980.00 USD |
| `1D` | `0.7380` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 4,530.00 USD | 963.47 USD | 1,960.00 USD |
| `7D` | `0.7380` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 58,340.00 USD | 13,660.00 USD | 39,550.00 USD |
| `1D` | `0.7390` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 1,180.00 USD | 1,290.00 USD |
| `7D` | `0.7390` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 8,110.00 USD | 25,420.00 USD |
| `1D` | `0.7400` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 2,880.00 USD | 2,520.00 USD | 3,120.00 USD |
| `7D` | `0.7400` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 1,730.00 USD | 6,500.00 USD | 11,600.00 USD |
| `1D` | `0.7410` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 1,490.00 USD | 1,030.00 USD | 4,730.00 USD |
| `7D` | `0.7410` | 5,780,000.00 USD | 5,780,000.00 USD | 0.00 USD | 28,380.00 USD | 30,100.00 USD | 30,960.00 USD |
| `1D` | `0.7420` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25.76 USD |
| `7D` | `0.7420` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 7,430.00 USD | 13,420.00 USD | 427.42 USD |
| `1D` | `0.7430` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 1,240.00 USD | 0.00 USD | 8.80 USD |
| `7D` | `0.7430` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 46,330.00 USD | 13,970.00 USD | 54,630.00 USD |
| `1D` | `0.7440` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 718.40 USD | 7,560.00 USD |
| `7D` | `0.7440` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 28,120.00 USD | 25,920.00 USD | 15,750.00 USD |
| `1D` | `0.7450` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 2,110.00 USD | 1,170.00 USD | 6,050.00 USD |
| `7D` | `0.7450` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 42,580.00 USD | 16,360.00 USD | 38,470.00 USD |
| `1D` | `0.7460` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 3,960.00 USD | 0.00 USD | 3,060.00 USD |
| `7D` | `0.7460` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 38,650.00 USD | 10,350.00 USD | 13,310.00 USD |
| `1D` | `0.7470` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 1,430.00 USD | 0.00 USD | 4,540.00 USD |
| `7D` | `0.7470` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 35,630.00 USD | 18,610.00 USD | 34,040.00 USD |
| `1D` | `0.7480` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 4,130.00 USD | 398.52 USD | 2,380.00 USD |
| `7D` | `0.7480` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 24,950.00 USD | 10,290.00 USD | 4,240.00 USD |
| `1D` | `0.7490` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 3,070.00 USD | 596.50 USD | 2,310.00 USD |
| `7D` | `0.7490` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 17,270.00 USD | 5,180.00 USD | 8,950.00 USD |
| `1D` | `0.7500` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 6,120.00 USD | 0.00 USD | 2,740.00 USD |
| `7D` | `0.7500` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 35,050.00 USD | 7,430.00 USD | 16,190.00 USD |
| `1D` | `0.7510` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 2,730.00 USD | 0.00 USD | 11.47 USD |
| `7D` | `0.7510` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 25,900.00 USD | 5,870.00 USD | 35,700.00 USD |
| `1D` | `0.7520` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 1,460.00 USD | 1,690.00 USD | 0.00 USD |
| `7D` | `0.7520` | 6,480,000.00 USD | 6,480,000.00 USD | 0.00 USD | 27,570.00 USD | 7,130.00 USD | 15,070.00 USD |
| `7D` | `0.7530` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 21,290.00 USD | 1,890.00 USD | 14,560.00 USD |
| `1D` | `0.7540` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 42.99 USD |
| `7D` | `0.7540` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 9,060.00 USD | 0.00 USD | 10,870.00 USD |
| `1D` | `0.7550` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,440.00 USD |
| `7D` | `0.7550` | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 18,390.00 USD | 6,470.00 USD | 19,610.00 USD |
| `1D` | `0.7560` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 678.61 USD | 0.00 USD |
| `7D` | `0.7560` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 7,600.00 USD | 1,100.00 USD | 2,650.00 USD |
| `1D` | `0.7570` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11.00 USD |
| `7D` | `0.7570` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 29,140.00 USD | 4,260.00 USD | 33,390.00 USD |
| `1D` | `0.7580` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,700.00 USD |
| `7D` | `0.7580` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 26,280.00 USD | 7,530.00 USD | 12,540.00 USD |
| `1D` | `0.7590` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 1,990.00 USD | 0.00 USD | 2,030.00 USD |
| `7D` | `0.7590` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 34,970.00 USD | 717.68 USD | 32,980.00 USD |
| `1D` | `0.7600` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 2,520.00 USD | 0.00 USD | 11.73 USD |
| `7D` | `0.7600` | 6,850,000.00 USD | 6,850,000.00 USD | 0.00 USD | 22,050.00 USD | 3,600.00 USD | 47,770.00 USD |
| `1D` | `0.7610` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,130.00 USD |
| `7D` | `0.7610` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 14,110.00 USD | 8,700.00 USD | 16,510.00 USD |
| `1D` | `0.7620` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 4,840.00 USD | 4,260.00 USD | 31.64 USD |
| `7D` | `0.7620` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 40,030.00 USD | 15,470.00 USD | 5,030.00 USD |
| `1D` | `0.7630` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 1,800.00 USD | 986.03 USD | 40.21 USD |
| `7D` | `0.7630` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 33,960.00 USD | 13,520.00 USD | 22,550.00 USD |
| `7D` | `0.7640` | 7,050,000.00 USD | 7,050,000.00 USD | 0.00 USD | 16,430.00 USD | 0.00 USD | 18,990.00 USD |
| `1D` | `0.7650` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 1,110.00 USD | 1,050.00 USD | 5,880.00 USD |
| `7D` | `0.7650` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 43,020.00 USD | 9,740.00 USD | 79,400.00 USD |
| `1D` | `0.7660` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 255.94 USD | 3,370.00 USD |
| `7D` | `0.7660` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 13,100.00 USD | 8,390.00 USD | 11,690.00 USD |
| `1D` | `0.7670` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 532.62 USD | 0.00 USD | 1,450.00 USD |
| `7D` | `0.7670` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 32,170.00 USD | 17,130.00 USD | 24,290.00 USD |
| `1D` | `0.7680` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 3,040.00 USD | 463.43 USD | 1,980.00 USD |
| `7D` | `0.7680` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 34,410.00 USD | 15,390.00 USD | 16,720.00 USD |
| `1D` | `0.7690` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 3,850.00 USD | 186.37 USD | 4,970.00 USD |
| `7D` | `0.7690` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 5,320.00 USD | 2,840.00 USD | 9,960.00 USD |
| `1D` | `0.7700` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 3,090.00 USD | 1,210.00 USD | 2,800.00 USD |
| `7D` | `0.7700` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 5,540.00 USD | 9,750.00 USD | 31,770.00 USD |
| `1D` | `0.7710` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 2,710.00 USD | 888.39 USD | 4,080.00 USD |
| `7D` | `0.7710` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 53,500.00 USD | 19,240.00 USD | 17,220.00 USD |
| `1D` | `0.7720` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 1,430.00 USD | 2,030.00 USD | 1,900.00 USD |
| `7D` | `0.7720` | 7,540,000.00 USD | 7,540,000.00 USD | 0.00 USD | 4,880.00 USD | 13,680.00 USD | 8,560.00 USD |
| `1D` | `0.7730` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 481.15 USD | 1,920.00 USD |
| `7D` | `0.7730` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 37,120.00 USD | 14,120.00 USD | 12,590.00 USD |
| `1D` | `0.7740` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 944.65 USD |
| `7D` | `0.7740` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 14,480.00 USD | 11,130.00 USD | 23,150.00 USD |
| `7D` | `0.7750` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 5,090.00 USD | 0.00 USD | 7,800.00 USD |
| `1D` | `0.7760` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD | 0.00 USD |
| `7D` | `0.7760` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 33,080.00 USD | 2,980.00 USD | 4,950.00 USD |
| `1D` | `0.7770` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 613.64 USD | 926.27 USD |
| `7D` | `0.7770` | 7,760,000.00 USD | 7,760,000.00 USD | 0.00 USD | 15,750.00 USD | 15,940.00 USD | 19,320.00 USD |
| `1D` | `0.7780` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 402.81 USD | 8.87 USD |
| `7D` | `0.7780` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 53,050.00 USD | 4,910.00 USD | 13,260.00 USD |
| `1D` | `0.7790` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 2,710.00 USD | 465.78 USD | 4,490.00 USD |
| `7D` | `0.7790` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 11,330.00 USD | 2,770.00 USD | 22,770.00 USD |
| `7D` | `0.7800` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 49,160.00 USD | 19,160.00 USD | 72,680.00 USD |
| `7D` | `0.7810` | 8,060,000.00 USD | 8,060,000.00 USD | 0.00 USD | 49,880.00 USD | 5,150.00 USD | 0.00 USD |
| `7D` | `0.7820` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 40,140.00 USD | 12,700.00 USD | 6,240.00 USD |
| `7D` | `0.7830` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 70,580.00 USD | 6,240.00 USD | 2,170.00 USD |
| `7D` | `0.7840` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 24,790.00 USD | 4,140.00 USD | 12.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `97.44M` | Total OI Tokens: `143,644,650.5 APT`
  * 1h OI Change: `-2.50%` | 4h OI Change: `-1.44%` | 24h OI Change: `-4.31%`
  * Exchange Breakdown: Binance=`18.56M` | Bybit=`19.94M` | OKX=`4.62M` | Hyperliquid=`3.71M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `4.27K` | Last 24h: `8.88K` | Last 3d: `10.89K` | Last 7d: `5.22K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0033%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `APT` | `53.08%` | `46.92%` | `1.13` | 5,620,000.00 USD |
| `15M` | `Binance` | `57.68%` | `42.32%` | `1.36` | 1,920,000.00 USD |
| `15M` | `OKX` | `56.84%` | `43.16%` | `1.32` | 1,100,000.00 USD |
| `15M` | `Bybit` | `51.32%` | `48.68%` | `1.05` | 530,260.00 USD |
| `15M` | `KuCoin` | `51.37%` | `48.63%` | `1.06` | 179,520.00 USD |
| `15M` | `Gate` | `34.39%` | `65.61%` | `0.52` | 101,580.00 USD |
| `15M` | `Bitget` | `28.84%` | `71.16%` | `0.41` | 225,610.00 USD |
| `15M` | `BingX` | `37.14%` | `62.86%` | `0.59` | 149,730.00 USD |
| `15M` | `MEXC` | `62.82%` | `37.18%` | `1.69` | 149,150.00 USD |
| `15M` | `Bitunix` | `79.33%` | `20.67%` | `3.84` | 191,490.00 USD |
| `15M` | `Hyperliquid` | `28.77%` | `71.23%` | `0.40` | 11,550.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `56.52%` | `43.48%` | `1.30` | 856,200.00 USD |
| `15M` | `Crypto.com` | `33.33%` | `66.67%` | `0.50` | 8.65 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 208,960.00 USD |
| `15M` | `HTX` | `64.1%` | `35.9%` | `1.79` | 895.33 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `56.86%` | `43.14%` | `1.32` | 1,160.00 USD |
| `15M` | `Aster` | `21.38%` | `78.62%` | `0.27` | 747.74 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `57.13%` | `42.87%` | `1.33` | 698.98 USD |
| `15M` | `Whale Positions` | `57.68%` | `42.32%` | `1.36` | 1,920,000.00 USD |
| `15M` | `Global Accounts` | `53.08%` | `46.92%` | `1.13` | 5,620,000.00 USD |
| `1H` | `APT` | `37.14%` | `62.86%` | `0.59` | 8,480,000.00 USD |
| `1H` | `Binance` | `37.27%` | `62.73%` | `0.59` | 3,040,000.00 USD |
| `1H` | `OKX` | `38.82%` | `61.18%` | `0.63` | 915,070.00 USD |
| `1H` | `Bybit` | `31.73%` | `68.27%` | `0.46` | 1,180,000.00 USD |
| `1H` | `KuCoin` | `50.49%` | `49.51%` | `1.02` | 645,570.00 USD |
| `1H` | `Gate` | `39.84%` | `60.16%` | `0.66` | 162,680.00 USD |
| `1H` | `Bitget` | `14.03%` | `85.97%` | `0.16` | 259,940.00 USD |
| `1H` | `BingX` | `26.01%` | `73.99%` | `0.35` | 584,790.00 USD |
| `1H` | `MEXC` | `34.43%` | `65.57%` | `0.53` | 787,450.00 USD |
| `1H` | `Bitunix` | `33.36%` | `66.64%` | `0.50` | 94,730.00 USD |
| `1H` | `Hyperliquid` | `16.28%` | `83.72%` | `0.19` | 160,110.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.91%` | `47.09%` | `1.12` | 370,560.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `66.42%` | `33.58%` | `1.98` | 258,180.00 USD |
| `1H` | `HTX` | `88.43%` | `11.57%` | `7.64` | 1,480.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `39.81%` | `60.19%` | `0.66` | 6,250.00 USD |
| `1H` | `Aster` | `9.28%` | `90.72%` | `0.10` | 6,060.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `96.54%` | `3.46%` | `27.90` | 6,560.00 USD |
| `1H` | `Whale Positions` | `37.27%` | `62.73%` | `0.59` | 3,040,000.00 USD |
| `1H` | `Global Accounts` | `37.14%` | `62.86%` | `0.59` | 8,480,000.00 USD |
| `4H` | `APT` | `43.58%` | `56.42%` | `0.77` | 32,030,000.00 USD |
| `4H` | `Binance` | `44.01%` | `55.99%` | `0.79` | 12,660,000.00 USD |
| `4H` | `OKX` | `45.2%` | `54.8%` | `0.82` | 3,600,000.00 USD |
| `4H` | `Bybit` | `41.34%` | `58.66%` | `0.70` | 3,790,000.00 USD |
| `4H` | `KuCoin` | `49.74%` | `50.26%` | `0.99` | 2,660,000.00 USD |
| `4H` | `Gate` | `47.53%` | `52.47%` | `0.91` | 537,840.00 USD |
| `4H` | `Bitget` | `39.48%` | `60.52%` | `0.65` | 806,300.00 USD |
| `4H` | `BingX` | `35.26%` | `64.74%` | `0.54` | 1,910,000.00 USD |
| `4H` | `MEXC` | `35.89%` | `64.11%` | `0.56` | 2,450,000.00 USD |
| `4H` | `Bitunix` | `37.76%` | `62.24%` | `0.61` | 595,430.00 USD |
| `4H` | `Hyperliquid` | `55.83%` | `44.17%` | `1.26` | 639,910.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.57%` | `49.43%` | `1.02` | 1,280,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `46.73%` | `53.27%` | `0.88` | 1,000,000.00 USD |
| `4H` | `HTX` | `92.17%` | `7.83%` | `11.77` | 7,470.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `38.92%` | `61.08%` | `0.64` | 65,650.00 USD |
| `4H` | `Aster` | `40.87%` | `59.13%` | `0.69` | 12,920.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `77.24%` | `22.76%` | `3.39` | 9,800.00 USD |
| `4H` | `Whale Positions` | `44.01%` | `55.99%` | `0.79` | 12,660,000.00 USD |
| `4H` | `Global Accounts` | `43.58%` | `56.42%` | `0.77` | 32,030,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.6990` | `0.7007` | `0.6990` | `0.7047` | `0.6974` | 804,696.05 USD | 466,627.01 USD | 338,069.04 USD | 128,557.97 USD | `+15.98%` | `21B / 12S` |
| `0:00 UTC` | `0.7013` | `0.7032` | `0.7013` | `0.7077` | `0.6997` | 1,483,040.97 USD | 758,743.98 USD | 724,296.99 USD | 34,446.99 USD | `+2.32%` | `9B / 11S` |
| `5:00 UTC` | `0.6961` | `0.6973` | `0.6961` | `0.7023` | `0.6946` | 1,215,291.53 USD | 404,512.82 USD | 810,778.71 USD | -406,265.88 USD | `-33.43%` | `8B / 18S` |
| `0:00 UTC` | `0.6948` | `0.6936` | `0.6948` | `0.6970` | `0.6912` | 798,941.07 USD | 368,954.34 USD | 429,986.74 USD | -61,032.40 USD | `-7.64%` | `6B / 6S` |
| `5:00 UTC` | `0.6923` | `0.6924` | `0.6923` | `0.6936` | `0.6913` | 552,207.56 USD | 239,483.72 USD | 312,723.84 USD | -73,240.12 USD | `-13.26%` | `1B / 2S` |
| `0:00 UTC` | `0.6888` | `0.6909` | `0.6888` | `0.6946` | `0.6875` | 808,356.30 USD | 277,065.63 USD | 531,290.67 USD | -254,225.03 USD | `-31.45%` | `8B / 26S` |
| `5:00 UTC` | `0.6872` | `0.6878` | `0.6872` | `0.6892` | `0.6863` | 391,857.65 USD | 178,103.21 USD | 213,754.44 USD | -35,651.23 USD | `-9.10%` | `2B / 6S` |
| `0:00 UTC` | `0.6846` | `0.6843` | `0.6846` | `0.6898` | `0.6793` | 929,091.57 USD | 323,978.58 USD | 605,112.99 USD | -281,134.41 USD | `-30.26%` | `9B / 28S` |
| `5:00 UTC` | `0.6777` | `0.6776` | `0.6777` | `0.6816` | `0.6731` | 1,052,942.47 USD | 434,240.65 USD | 618,701.82 USD | -184,461.17 USD | `-17.52%` | `7B / 24S` |
| `0:00 UTC` | `0.6777` | `0.6787` | `0.6777` | `0.6803` | `0.6776` | 75,684.63 USD | 28,962.84 USD | 46,721.79 USD | -17,758.94 USD | `-23.46%` | `2B / 5S` |

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
| `5m` | -6,230.00 USD | 17,740.00 USD | **`ACCUMULATION`** |
| `15m` | 6,810.00 USD | 85,780.00 USD | **`ACCUMULATION`** |
| `30m` | -101,820.00 USD | -826,890.00 USD | **`DISTRIBUTION`** |
| `1h` | -149,290.00 USD | -1,390,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -22,060.00 USD | -2,060,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 220,310.00 USD | -2,530,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 239,420.00 USD | -2,480,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 307,330.00 USD | -2,840,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 69,990.00 USD | -3,340,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -790,050.00 USD | -7,180,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -4,710,000.00 USD | -19,790,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,600,000.00 USD | -101,220,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-6.23K` | 15m=`+6.81K` | 1h=`-149.29K` | 24h=`-790.05K`
* Futures Capital Netflows: 5m=`+17.74K` | 15m=`+85.78K` | 1h=`-1.39M` | 24h=`-7.18M`
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
  * `2026-10-29 23:31:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:35 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:35 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:35 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:35 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:35 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:35 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
