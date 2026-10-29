# 🏛️ SOVEREIGN CANDIDATE DOSSIER: APT
**Canonical Key**: `APT` | **Broker Instrument**: `APTUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 22:33:52 IST` (`2026-10-29 17:03:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.6927` | `0.6930` | `0.6915` | `0.6919` | `195,710` | 135,442.15 USD | 6,760.23 USD | `+4.99%` | -2,770,499.74 USD | `+0.25` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.6920` | `0.6936` | `0.6916` | `0.6926` | `294,376` | 203,884.09 USD | -98,501.11 USD | `-48.31%` | -2,869,000.86 USD | `-1.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.6926` | `0.6943` | `0.6917` | `0.6923` | `198,198` | 137,404.63 USD | 84,716.99 USD | `+61.66%` | -2,784,283.87 USD | `+1.14` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.6962` | `0.6970` | `0.6911` | `0.6926` | `1,152,028` | 798,941.07 USD | -61,032.40 USD | `-7.64%` | -2,809,550.17 USD | `-0.27` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.6927` | `0.6936` | `0.6912` | `0.6926` | `797,540` | 552,207.56 USD | -73,240.12 USD | `-13.26%` | -2,882,790.29 USD | `-0.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.6926` | `0.6943` | `0.6917` | `0.6923` | `198,198` | 137,404.63 USD | 84,716.99 USD | `+61.66%` | -2,798,073.30 USD | `+0.91` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.6868` | `0.7047` | `0.6852` | `0.7036` | `3,879,858` | 2,697,535.23 USD | 26,927.71 USD | `+1.00%` | -2,408,403.96 USD | `+0.64` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.7037` | `0.7077` | `0.6911` | `0.6926` | `5,801,752` | 4,049,481.14 USD | -506,091.42 USD | `-12.50%` | -2,914,495.37 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.6926` | `0.6943` | `0.6917` | `0.6924` | `195,434` | 135,491.62 USD | 85,873.18 USD | `+63.38%` | -2,828,622.19 USD | `+0.86` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.6561` | `0.6774` | `0.6549` | `0.6712` | `7,448,343` | 4,965,296.85 USD | -60,141.40 USD | `-1.21%` | -2,083,618.45 USD | `+1.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -2,231,705.21 USD | `+0.80` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6911` | `0.6923` | `5,999,949` | 4,186,885.77 USD | -421,374.43 USD | `-10.06%` | -2,653,079.63 USD | `+0.06` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.7002` | `0.7012` | `0.6555` | `0.6611` | `16,465,880` | 11,061,810.70 USD | -1,103,761.29 USD | `-9.98%` | -1,656,578.37 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6611` | `0.6759` | `0.6485` | `0.6561` | `10,656,422` | 7,044,804.33 USD | -366,898.68 USD | `-5.21%` | -2,023,477.05 USD | `+0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6561` | `0.6774` | `0.6549` | `0.6712` | `7,448,343` | 4,965,296.85 USD | -60,141.40 USD | `-1.21%` | -2,083,618.45 USD | `+1.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -2,231,705.21 USD | `+0.80` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6911` | `0.6923` | `5,999,949` | 4,186,885.77 USD | -421,374.43 USD | `-10.06%` | -2,653,079.63 USD | `+0.06` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:31:36 IST` |

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
| `7D` | `Long Liquidation` | `0.5810` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 5,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5820` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5835` | 132.92 USD | 49,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 210.96 USD | 49,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 586.80 USD | 49,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5870` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 1,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5880` | 2,400,000.00 USD | 2,400,000.00 USD | 3,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5885` | 440.16 USD | 48,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5890` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 81.07 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5895` | 1,690.00 USD | 48,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5900` | 2,390,000.00 USD | 2,390,000.00 USD | 3,120.00 USD | 1,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5920` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 2,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5925` | 609.14 USD | 46,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5930` | 2,390,000.00 USD | 2,390,000.00 USD | 10,090.00 USD | 0.00 USD | 9,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5935` | 572.40 USD | 46,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5945` | 3,850.00 USD | 45,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5950` | 2,370,000.00 USD | 2,370,000.00 USD | 5,120.00 USD | 0.00 USD | 4,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5960` | 2,360,000.00 USD | 2,360,000.00 USD | 5,120.00 USD | 1,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5970` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5975` | 157.22 USD | 41,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5980` | 2,340,000.00 USD | 2,340,000.00 USD | 7,660.00 USD | 826.53 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5990` | 2,330,000.00 USD | 2,330,000.00 USD | 3,320.00 USD | 1,340.00 USD | 14,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6000` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 796.28 USD | 4,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6005` | 852.06 USD | 41,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6010` | 1,850,000.00 USD | 1,850,000.00 USD | 735.24 USD | 461.96 USD | 1,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6020` | 1,840,000.00 USD | 1,840,000.00 USD | 4,120.00 USD | 1,800.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6020` | 2,310,000.00 USD | 2,310,000.00 USD | 10,590.00 USD | 8,040.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6025` | 451.19 USD | 40,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6030` | 1,830,000.00 USD | 1,830,000.00 USD | 1,110.00 USD | 1,970.00 USD | 3,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6030` | 2,290,000.00 USD | 2,290,000.00 USD | 2,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6040` | 1,830,000.00 USD | 1,830,000.00 USD | 4,530.00 USD | 963.47 USD | 1,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6040` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6045` | 527.44 USD | 40,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6050` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 599.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6050` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 36.57 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6060` | 1,820,000.00 USD | 1,820,000.00 USD | 2,880.00 USD | 606.70 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6060` | 2,270,000.00 USD | 2,270,000.00 USD | 2,850.00 USD | 0.00 USD | 55.47 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6070` | 1,810,000.00 USD | 1,810,000.00 USD | 1,490.00 USD | 1,030.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6070` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 148.03 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6080` | 1,800,000.00 USD | 1,800,000.00 USD | 1,920.00 USD | 0.00 USD | 1,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6080` | 2,270,000.00 USD | 2,270,000.00 USD | 2,860.00 USD | 0.00 USD | 72.33 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6090` | 1,800,000.00 USD | 1,800,000.00 USD | 3,670.00 USD | 0.00 USD | 45.55 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6090` | 2,270,000.00 USD | 2,270,000.00 USD | 6,360.00 USD | 0.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6100` | 1,800,000.00 USD | 1,800,000.00 USD | 4,520.00 USD | 1,370.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6100` | 2,260,000.00 USD | 2,260,000.00 USD | 7,480.00 USD | 2,570.00 USD | 98.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6105` | 126.47 USD | 39,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6110` | 1,780,000.00 USD | 1,780,000.00 USD | 2,490.00 USD | 0.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6110` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 2,210.00 USD | 6,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6120` | 1,780,000.00 USD | 1,780,000.00 USD | 2,530.00 USD | 1,230.00 USD | 8,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6120` | 2,240,000.00 USD | 2,240,000.00 USD | 2,100.00 USD | 3,510.00 USD | 7,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6130` | 1,770,000.00 USD | 1,770,000.00 USD | 5,110.00 USD | 798.62 USD | 3,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6130` | 2,230,000.00 USD | 2,230,000.00 USD | 8,870.00 USD | 1,050.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6140` | 1,760,000.00 USD | 1,760,000.00 USD | 5,860.00 USD | 407.44 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6140` | 2,210,000.00 USD | 2,210,000.00 USD | 4,540.00 USD | 7,000.00 USD | 6,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6150` | 1,750,000.00 USD | 1,750,000.00 USD | 3,750.00 USD | 0.00 USD | 1,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6150` | 2,190,000.00 USD | 2,190,000.00 USD | 8,250.00 USD | 5,870.00 USD | 2,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6160` | 1,740,000.00 USD | 1,740,000.00 USD | 1,460.00 USD | 1,690.00 USD | 681.25 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6160` | 2,180,000.00 USD | 2,180,000.00 USD | 1,790.00 USD | 2,510.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6170` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 1,000.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6170` | 2,170,000.00 USD | 2,170,000.00 USD | 13,260.00 USD | 2,610.00 USD | 9,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6180` | 1,730,000.00 USD | 1,730,000.00 USD | 676.84 USD | 1,010.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6180` | 2,140,000.00 USD | 2,140,000.00 USD | 7,600.00 USD | 1,190.00 USD | 6,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6190` | 1,730,000.00 USD | 1,730,000.00 USD | 3,170.00 USD | 492.27 USD | 1,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6190` | 2,130,000.00 USD | 2,130,000.00 USD | 9,560.00 USD | 1,930.00 USD | 9,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6195` | 3,170.00 USD | 39,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6200` | 1,720,000.00 USD | 1,720,000.00 USD | 1,010.00 USD | 0.00 USD | 855.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6200` | 2,110,000.00 USD | 2,110,000.00 USD | 13,870.00 USD | 5,230.00 USD | 6,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6210` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 922.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6210` | 2,080,000.00 USD | 2,080,000.00 USD | 4,760.00 USD | 1,860.00 USD | 2,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6220` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 7.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6220` | 2,070,000.00 USD | 2,070,000.00 USD | 3,290.00 USD | 2,310.00 USD | 29,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6230` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 11.55 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6230` | 2,040,000.00 USD | 2,040,000.00 USD | 9,770.00 USD | 4,700.00 USD | 8,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6235` | 3,250.00 USD | 36,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6240` | 1,720,000.00 USD | 1,720,000.00 USD | 2,670.00 USD | 1,130.00 USD | 60.89 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6240` | 2,020,000.00 USD | 2,020,000.00 USD | 18,610.00 USD | 2,010.00 USD | 5,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6245` | 1,960.00 USD | 33,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6250` | 1,720,000.00 USD | 1,720,000.00 USD | 1,800.00 USD | 2,630.00 USD | 36.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6250` | 1,990,000.00 USD | 1,990,000.00 USD | 16,120.00 USD | 3,830.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6255` | 286.65 USD | 31,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6260` | 1,710,000.00 USD | 1,710,000.00 USD | 10,030.00 USD | 1,310.00 USD | 8,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6260` | 1,970,000.00 USD | 1,970,000.00 USD | 20,890.00 USD | 7,660.00 USD | 25,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6265` | 10,530.00 USD | 30,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6270` | 1,690,000.00 USD | 1,690,000.00 USD | 3,700.00 USD | 3,940.00 USD | 11,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6270` | 1,910,000.00 USD | 1,910,000.00 USD | 17,460.00 USD | 8,200.00 USD | 14,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6280` | 1,670,000.00 USD | 1,670,000.00 USD | 11,690.00 USD | 463.43 USD | 870.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6280` | 1,870,000.00 USD | 1,870,000.00 USD | 9,160.00 USD | 9,230.00 USD | 16,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6285` | 903.47 USD | 20,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6290` | 1,660,000.00 USD | 1,660,000.00 USD | 8,430.00 USD | 1,200.00 USD | 5,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6290` | 1,840,000.00 USD | 1,840,000.00 USD | 17,710.00 USD | 6,740.00 USD | 10,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6300` | 1,650,000.00 USD | 1,650,000.00 USD | 12,950.00 USD | 2,470.00 USD | 2,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6300` | 1,800,000.00 USD | 1,800,000.00 USD | 10,040.00 USD | 7,890.00 USD | 11,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6310` | 1,630,000.00 USD | 1,630,000.00 USD | 5,850.00 USD | 5,110.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6310` | 1,770,000.00 USD | 1,770,000.00 USD | 19,340.00 USD | 4,520.00 USD | 17,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6315` | 1,010.00 USD | 19,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6320` | 1,620,000.00 USD | 1,620,000.00 USD | 12,320.00 USD | 9,530.00 USD | 13,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6320` | 1,730,000.00 USD | 1,730,000.00 USD | 4,880.00 USD | 12,650.00 USD | 8,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6330` | 1,580,000.00 USD | 1,580,000.00 USD | 17,300.00 USD | 3,580.00 USD | 21,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6330` | 1,710,000.00 USD | 1,710,000.00 USD | 57,940.00 USD | 12,500.00 USD | 33,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6340` | 1,540,000.00 USD | 1,540,000.00 USD | 9,830.00 USD | 2,020.00 USD | 15,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6340` | 1,600,000.00 USD | 1,600,000.00 USD | 10,730.00 USD | 3,420.00 USD | 4,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6350` | 1,510,000.00 USD | 1,510,000.00 USD | 19,180.00 USD | 8,820.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6350` | 1,580,000.00 USD | 1,580,000.00 USD | 14,450.00 USD | 2,430.00 USD | 22,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6360` | 1,480,000.00 USD | 1,480,000.00 USD | 30,350.00 USD | 9,150.00 USD | 33,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6360` | 1,540,000.00 USD | 1,540,000.00 USD | 42,690.00 USD | 7,300.00 USD | 40,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6370` | 1,410,000.00 USD | 1,410,000.00 USD | 21,750.00 USD | 4,510.00 USD | 27,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6370` | 1,450,000.00 USD | 1,450,000.00 USD | 49,080.00 USD | 4,870.00 USD | 93.41 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6375` | 5,900.00 USD | 18,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6380` | 1,350,000.00 USD | 1,350,000.00 USD | 19,430.00 USD | 7,180.00 USD | 7,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6380` | 1,400,000.00 USD | 1,400,000.00 USD | 18,140.00 USD | 3,870.00 USD | 30,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6390` | 1,320,000.00 USD | 1,320,000.00 USD | 18,790.00 USD | 529.57 USD | 6,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6390` | 1,350,000.00 USD | 1,350,000.00 USD | 10,200.00 USD | 7,510.00 USD | 13,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6400` | 1,290,000.00 USD | 1,290,000.00 USD | 9,830.00 USD | 9,970.00 USD | 25,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6400` | 1,320,000.00 USD | 1,320,000.00 USD | 15,560.00 USD | 0.00 USD | 526.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6410` | 1,250,000.00 USD | 1,250,000.00 USD | 20,930.00 USD | 2,240.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6410` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 6,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6415` | 4,740.00 USD | 12,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6420` | 1,220,000.00 USD | 1,220,000.00 USD | 32,540.00 USD | 7,850.00 USD | 12,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6420` | 1,290,000.00 USD | 1,290,000.00 USD | 39,060.00 USD | 26,560.00 USD | 10,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6430` | 1,170,000.00 USD | 1,170,000.00 USD | 25,620.00 USD | 7,460.00 USD | 9,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6430` | 1,220,000.00 USD | 1,220,000.00 USD | 16,200.00 USD | 3,970.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6435` | 2,320.00 USD | 7,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6440` | 1,120,000.00 USD | 1,120,000.00 USD | 21,790.00 USD | 11,330.00 USD | 8,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6440` | 1,190,000.00 USD | 1,190,000.00 USD | 14,160.00 USD | 6,720.00 USD | 15,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6450` | 1,080,000.00 USD | 1,080,000.00 USD | 23,100.00 USD | 20,050.00 USD | 31,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6450` | 1,160,000.00 USD | 1,160,000.00 USD | 14,120.00 USD | 15,560.00 USD | 311.53 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6455` | 3,730.00 USD | 5,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6460` | 1,010,000.00 USD | 1,010,000.00 USD | 43,360.00 USD | 10,480.00 USD | 51,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6460` | 1,130,000.00 USD | 1,130,000.00 USD | 75,060.00 USD | 14,300.00 USD | 75,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6470` | 903,010.00 USD | 903,010.00 USD | 30,630.00 USD | 6,620.00 USD | 41,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6470` | 964,030.00 USD | 964,030.00 USD | 9,660.00 USD | 3,880.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6480` | 823,990.00 USD | 823,990.00 USD | 48,130.00 USD | 14,180.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6480` | 941,210.00 USD | 941,210.00 USD | 37,050.00 USD | 0.00 USD | 23,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6485` | 259.68 USD | 1,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6490` | 753,930.00 USD | 753,930.00 USD | 30,360.00 USD | 3,800.00 USD | 40,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6490` | 880,730.00 USD | 880,730.00 USD | 36,340.00 USD | 0.00 USD | 17,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6500` | 678,960.00 USD | 678,960.00 USD | 48,860.00 USD | 1,390.00 USD | 32,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6500` | 826,540.00 USD | 826,540.00 USD | 18,310.00 USD | 0.00 USD | 67,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6505` | 580.53 USD | 1,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6510` | 596,110.00 USD | 596,110.00 USD | 15,700.00 USD | 4,450.00 USD | 66,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6510` | 741,120.00 USD | 741,120.00 USD | 101,440.00 USD | 4,190.00 USD | 328.84 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6520` | 509,170.00 USD | 509,170.00 USD | 31,260.00 USD | 5,680.00 USD | 19,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6520` | 635,150.00 USD | 635,150.00 USD | 39,510.00 USD | 6,720.00 USD | 72,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6530` | 452,780.00 USD | 452,780.00 USD | 5,780.00 USD | 1,060.00 USD | 11,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6530` | 516,860.00 USD | 516,860.00 USD | 0.00 USD | 0.00 USD | 46,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6540` | 434,200.00 USD | 434,200.00 USD | 11,450.00 USD | 2,530.00 USD | 15,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6540` | 469,920.00 USD | 469,920.00 USD | 15,730.00 USD | 0.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6550` | 404,920.00 USD | 404,920.00 USD | 13,860.00 USD | 5,390.00 USD | 20,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6550` | 439,670.00 USD | 439,670.00 USD | 0.00 USD | 0.00 USD | 38,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6560` | 365,260.00 USD | 365,260.00 USD | 23,680.00 USD | 3,800.00 USD | 33,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6560` | 401,330.00 USD | 401,330.00 USD | 0.00 USD | 5,380.00 USD | 34,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6570` | 303,980.00 USD | 303,980.00 USD | 5,570.00 USD | 1,820.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6570` | 361,240.00 USD | 361,240.00 USD | 14,440.00 USD | 0.00 USD | 10,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6580` | 273,030.00 USD | 273,030.00 USD | 5,880.00 USD | 0.00 USD | 0.08 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6580` | 336,090.00 USD | 336,090.00 USD | 0.00 USD | 0.00 USD | 240.54 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6590` | 267,140.00 USD | 267,140.00 USD | 0.00 USD | 3,890.00 USD | 11,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6590` | 335,850.00 USD | 335,850.00 USD | 9,540.00 USD | 0.00 USD | 61.15 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6600` | 252,030.00 USD | 252,030.00 USD | 11,650.00 USD | 2,120.00 USD | 22,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6600` | 326,250.00 USD | 326,250.00 USD | 0.00 USD | 4,180.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6610` | 215,650.00 USD | 215,650.00 USD | 11,920.00 USD | 2,560.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6610` | 301,620.00 USD | 301,620.00 USD | 0.00 USD | 0.00 USD | 379.61 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6620` | 193,340.00 USD | 193,340.00 USD | 9,060.00 USD | 1,160.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6620` | 301,240.00 USD | 301,240.00 USD | 14,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6630` | 171,450.00 USD | 171,450.00 USD | 14,750.00 USD | 2,780.00 USD | 2.53 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6630` | 286,920.00 USD | 286,920.00 USD | 0.00 USD | 0.00 USD | 271.36 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6640` | 153,910.00 USD | 153,910.00 USD | 16,520.00 USD | 0.00 USD | 11,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6640` | 286,650.00 USD | 286,650.00 USD | 8,590.00 USD | 0.00 USD | 102.26 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6650` | 126,010.00 USD | 126,010.00 USD | 7,140.00 USD | 0.00 USD | 1,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6650` | 277,960.00 USD | 277,960.00 USD | 0.00 USD | 0.00 USD | 231.32 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6660` | 117,000.00 USD | 117,000.00 USD | 7,730.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6660` | 277,730.00 USD | 277,730.00 USD | 0.00 USD | 0.00 USD | 244.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6670` | 103,860.00 USD | 103,860.00 USD | 18,850.00 USD | 2,980.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6670` | 277,480.00 USD | 277,480.00 USD | 31,450.00 USD | 0.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6680` | 77,100.00 USD | 77,100.00 USD | 20,370.00 USD | 3,380.00 USD | 4,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6680` | 237,260.00 USD | 237,260.00 USD | 24,780.00 USD | 7,780.00 USD | 771.72 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6690` | 48,500.00 USD | 48,500.00 USD | 13,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6690` | 203,930.00 USD | 203,930.00 USD | 0.00 USD | 0.00 USD | 145.17 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6695` | 818.97 USD | 818.97 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.6700` | 203,780.00 USD | 203,780.00 USD | 0.00 USD | 0.00 USD | 72.32 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6710` | 35,500.00 USD | 35,500.00 USD | 0.00 USD | 18,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6710` | 203,710.00 USD | 203,710.00 USD | 0.00 USD | 6,960.00 USD | 62.19 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6720` | 17,400.00 USD | 17,400.00 USD | 0.00 USD | 0.00 USD | 3.80 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6720` | 196,690.00 USD | 196,690.00 USD | 0.00 USD | 0.00 USD | 131.11 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6730` | 17,390.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD | 5.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6740` | 196,560.00 USD | 196,560.00 USD | 0.00 USD | 0.00 USD | 164.10 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6750` | 17,390.00 USD | 17,390.00 USD | 0.00 USD | 7,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6750` | 196,400.00 USD | 196,400.00 USD | 0.00 USD | 70,210.00 USD | 62.35 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6760` | 126,130.00 USD | 126,130.00 USD | 0.00 USD | 2,240.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6770` | 66,200.00 USD | 66,200.00 USD | 0.00 USD | 4,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6780` | 10,340.00 USD | 10,340.00 USD | 0.00 USD | 10,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6780` | 62,010.00 USD | 62,010.00 USD | 0.00 USD | 10,220.00 USD | 48,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6790` | 3,050.00 USD | 3,050.00 USD | 0.00 USD | 3,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6810` | 15,720.00 USD | 15,720.00 USD | 0.00 USD | 15,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6810` | 31,440.00 USD | 31,440.00 USD | 0.00 USD | 15,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6820` | 69,160.00 USD | 69,160.00 USD | 0.00 USD | 37,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6830` | 33,090.00 USD | 33,090.00 USD | 0.00 USD | 14,650.00 USD | 18,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6840` | 71,880.00 USD | 71,880.00 USD | 0.00 USD | 13,870.00 USD | 24,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6840` | 122,920.00 USD | 122,920.00 USD | 0.00 USD | 14,650.00 USD | 39,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6850` | 139,860.00 USD | 139,860.00 USD | 29,190.00 USD | 8,490.00 USD | 30,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6850` | 244,830.00 USD | 244,830.00 USD | 79,030.00 USD | 4,710.00 USD | 38,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6860` | 258,000.00 USD | 258,000.00 USD | 54,730.00 USD | 21,960.00 USD | 41,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6860` | 303,640.00 USD | 303,640.00 USD | 24,530.00 USD | 9,830.00 USD | 24,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6870` | 352,770.00 USD | 352,770.00 USD | 46,360.00 USD | 19,230.00 USD | 29,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6870` | 327,890.00 USD | 327,890.00 USD | 12,790.00 USD | 0.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6880` | 399,490.00 USD | 399,490.00 USD | 20,950.00 USD | 1,610.00 USD | 24,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6880` | 370,230.00 USD | 370,230.00 USD | 18,170.00 USD | 17,300.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6890` | 423,250.00 USD | 423,250.00 USD | 21,560.00 USD | 0.00 USD | 2,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6890` | 384,550.00 USD | 384,550.00 USD | 14,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6900` | 481,600.00 USD | 481,600.00 USD | 25,280.00 USD | 8,300.00 USD | 24,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6900` | 423,220.00 USD | 423,220.00 USD | 5,340.00 USD | 4,480.00 USD | 28,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6910` | 559,770.00 USD | 559,770.00 USD | 37,420.00 USD | 13,680.00 USD | 27,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6910` | 475,570.00 USD | 475,570.00 USD | 37,750.00 USD | 2,090.00 USD | 12,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6920` | 624,280.00 USD | 624,280.00 USD | 35,960.00 USD | 3,880.00 USD | 24,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6920` | 530,030.00 USD | 530,030.00 USD | 26,730.00 USD | 3,360.00 USD | 24,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6930` | 641,530.00 USD | 641,530.00 USD | 8,100.00 USD | 529.57 USD | 8,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6930` | 543,040.00 USD | 543,040.00 USD | 0.00 USD | 0.00 USD | 13,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6940` | 665,420.00 USD | 665,420.00 USD | 11,230.00 USD | 4,420.00 USD | 8,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6940` | 543,180.00 USD | 543,180.00 USD | 0.00 USD | 0.00 USD | 140.50 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6950` | 700,870.00 USD | 700,870.00 USD | 22,480.00 USD | 4,460.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6950` | 587,170.00 USD | 587,170.00 USD | 31,450.00 USD | 0.00 USD | 12,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6960` | 762,420.00 USD | 762,420.00 USD | 36,830.00 USD | 7,190.00 USD | 17,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6960` | 627,280.00 USD | 627,280.00 USD | 12,220.00 USD | 17,870.00 USD | 10,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6970` | 801,130.00 USD | 801,130.00 USD | 23,380.00 USD | 6,080.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6970` | 634,500.00 USD | 634,500.00 USD | 7,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6980` | 829,850.00 USD | 829,850.00 USD | 11,320.00 USD | 8,750.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6980` | 651,180.00 USD | 651,180.00 USD | 0.00 USD | 2,100.00 USD | 14,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6990` | 838,760.00 USD | 838,760.00 USD | 1,320.00 USD | 1,940.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6990` | 656,110.00 USD | 656,110.00 USD | 4,770.00 USD | 0.00 USD | 158.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7000` | 871,510.00 USD | 871,510.00 USD | 8,760.00 USD | 4,290.00 USD | 19,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7000` | 668,190.00 USD | 668,190.00 USD | 0.00 USD | 2,090.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7010` | 896,760.00 USD | 896,760.00 USD | 9,680.00 USD | 2,580.00 USD | 12,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7020` | 907,650.00 USD | 907,650.00 USD | 9,770.00 USD | 0.00 USD | 1,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7020` | 737,610.00 USD | 737,610.00 USD | 16,350.00 USD | 0.00 USD | 53,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7030` | 914,070.00 USD | 914,070.00 USD | 0.00 USD | 1,660.00 USD | 4,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7030` | 864,690.00 USD | 864,690.00 USD | 76,610.00 USD | 0.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7040` | 941,550.00 USD | 941,550.00 USD | 17,790.00 USD | 3,130.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7040` | 882,080.00 USD | 882,080.00 USD | 0.00 USD | 0.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7050` | 961,970.00 USD | 961,970.00 USD | 14,710.00 USD | 0.00 USD | 5,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7050` | 1,010,000.00 USD | 1,010,000.00 USD | 4,290.00 USD | 0.00 USD | 123,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7060` | 967,510.00 USD | 967,510.00 USD | 3,570.00 USD | 1,040.00 USD | 933.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7060` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 33,490.00 USD | 39,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7070` | 982,780.00 USD | 982,780.00 USD | 9,150.00 USD | 3,260.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7070` | 1,140,000.00 USD | 1,140,000.00 USD | 8,720.00 USD | 22,760.00 USD | 29,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7080` | 1,010,000.00 USD | 1,010,000.00 USD | 18,420.00 USD | 3,500.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7080` | 1,240,000.00 USD | 1,240,000.00 USD | 15,730.00 USD | 28,570.00 USD | 53,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7090` | 1,050,000.00 USD | 1,050,000.00 USD | 22,500.00 USD | 7,680.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7090` | 1,520,000.00 USD | 1,520,000.00 USD | 106,000.00 USD | 32,830.00 USD | 134,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7100` | 1,090,000.00 USD | 1,090,000.00 USD | 12,610.00 USD | 3,930.00 USD | 25,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7100` | 1,600,000.00 USD | 1,600,000.00 USD | 37,600.00 USD | 30,700.00 USD | 14,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7110` | 1,110,000.00 USD | 1,110,000.00 USD | 8,750.00 USD | 3,170.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7110` | 1,710,000.00 USD | 1,710,000.00 USD | 40,300.00 USD | 28,740.00 USD | 44,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7120` | 1,140,000.00 USD | 1,140,000.00 USD | 15,190.00 USD | 2,320.00 USD | 13,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7120` | 1,940,000.00 USD | 1,940,000.00 USD | 60,730.00 USD | 45,350.00 USD | 122,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7130` | 1,180,000.00 USD | 1,180,000.00 USD | 9,250.00 USD | 2,640.00 USD | 34,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7130` | 2,100,000.00 USD | 2,100,000.00 USD | 75,250.00 USD | 31,940.00 USD | 51,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7140` | 1,230,000.00 USD | 1,230,000.00 USD | 30,330.00 USD | 6,770.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7140` | 2,340,000.00 USD | 2,340,000.00 USD | 127,300.00 USD | 35,310.00 USD | 82,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7150` | 1,250,000.00 USD | 1,250,000.00 USD | 7,820.00 USD | 5,800.00 USD | 8,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7150` | 2,520,000.00 USD | 2,520,000.00 USD | 50,460.00 USD | 26,770.00 USD | 96,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7160` | 1,270,000.00 USD | 1,270,000.00 USD | 15,080.00 USD | 1,570.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7160` | 2,690,000.00 USD | 2,690,000.00 USD | 62,580.00 USD | 38,490.00 USD | 68,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7170` | 1,290,000.00 USD | 1,290,000.00 USD | 8,450.00 USD | 3,880.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7170` | 2,870,000.00 USD | 2,870,000.00 USD | 105,890.00 USD | 24,740.00 USD | 53,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7180` | 1,300,000.00 USD | 1,300,000.00 USD | 1,270.00 USD | 1,580.00 USD | 10,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7180` | 2,960,000.00 USD | 2,960,000.00 USD | 59,980.00 USD | 21,140.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7190` | 1,310,000.00 USD | 1,310,000.00 USD | 3,460.00 USD | 6,850.00 USD | 180.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7190` | 3,070,000.00 USD | 3,070,000.00 USD | 17,000.00 USD | 11,840.00 USD | 88,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7200` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 3,590.00 USD | 10,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7200` | 3,260,000.00 USD | 3,260,000.00 USD | 58,530.00 USD | 33,310.00 USD | 90,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7210` | 1,340,000.00 USD | 1,340,000.00 USD | 5,130.00 USD | 5,240.00 USD | 84.07 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7210` | 3,550,000.00 USD | 3,550,000.00 USD | 206,240.00 USD | 17,950.00 USD | 70,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7220` | 1,390,000.00 USD | 1,390,000.00 USD | 23,430.00 USD | 5,070.00 USD | 23,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7220` | 3,730,000.00 USD | 3,730,000.00 USD | 112,190.00 USD | 42,410.00 USD | 27,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7230` | 1,420,000.00 USD | 1,420,000.00 USD | 3,920.00 USD | 4,060.00 USD | 27,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7230` | 3,900,000.00 USD | 3,900,000.00 USD | 59,050.00 USD | 10,400.00 USD | 94,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7235` | 42,980.00 USD | 42,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7240` | 1,440,000.00 USD | 1,440,000.00 USD | 2,920.00 USD | 4,240.00 USD | 9,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7240` | 4,020,000.00 USD | 4,020,000.00 USD | 75,360.00 USD | 14,510.00 USD | 29,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7250` | 1,450,000.00 USD | 1,450,000.00 USD | 4,760.00 USD | 1,150.00 USD | 5,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7250` | 4,150,000.00 USD | 4,150,000.00 USD | 52,270.00 USD | 23,200.00 USD | 58,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7255` | 729.79 USD | 43,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7260` | 1,470,000.00 USD | 1,470,000.00 USD | 8,620.00 USD | 5,680.00 USD | 8,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7260` | 4,320,000.00 USD | 4,320,000.00 USD | 54,140.00 USD | 26,590.00 USD | 93,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7265` | 124.62 USD | 43,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7270` | 1,500,000.00 USD | 1,500,000.00 USD | 11,280.00 USD | 2,760.00 USD | 14,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7270` | 4,420,000.00 USD | 4,420,000.00 USD | 49,240.00 USD | 18,120.00 USD | 33,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7280` | 1,540,000.00 USD | 1,540,000.00 USD | 16,410.00 USD | 5,780.00 USD | 11,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7280` | 4,540,000.00 USD | 4,540,000.00 USD | 42,560.00 USD | 22,060.00 USD | 50,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7290` | 1,570,000.00 USD | 1,570,000.00 USD | 7,920.00 USD | 6,520.00 USD | 19,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7290` | 4,690,000.00 USD | 4,690,000.00 USD | 47,200.00 USD | 32,380.00 USD | 69,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7300` | 1,610,000.00 USD | 1,610,000.00 USD | 9,980.00 USD | 5,040.00 USD | 23,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7300` | 4,800,000.00 USD | 4,800,000.00 USD | 55,390.00 USD | 27,940.00 USD | 29,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7310` | 1,620,000.00 USD | 1,620,000.00 USD | 1,010.00 USD | 1,670.00 USD | 5,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7310` | 4,980,000.00 USD | 4,980,000.00 USD | 115,470.00 USD | 35,110.00 USD | 31,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7320` | 1,640,000.00 USD | 1,640,000.00 USD | 5,780.00 USD | 1,140.00 USD | 12,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7320` | 5,130,000.00 USD | 5,130,000.00 USD | 74,380.00 USD | 25,020.00 USD | 48,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7325` | 7,150.00 USD | 50,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7330` | 1,650,000.00 USD | 1,650,000.00 USD | 6,450.00 USD | 3,420.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7330` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 32,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7340` | 1,660,000.00 USD | 1,660,000.00 USD | 1,620.00 USD | 1,530.00 USD | 5,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7340` | 5,230,000.00 USD | 5,230,000.00 USD | 31,260.00 USD | 8,620.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7345` | 150.17 USD | 51,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7350` | 1,660,000.00 USD | 1,660,000.00 USD | 735.24 USD | 1,470.00 USD | 8.40 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7350` | 5,330,000.00 USD | 5,330,000.00 USD | 66,390.00 USD | 15,820.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7360` | 1,690,000.00 USD | 1,690,000.00 USD | 10,900.00 USD | 2,960.00 USD | 14,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7360` | 5,420,000.00 USD | 5,420,000.00 USD | 37,210.00 USD | 30,980.00 USD | 19,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7370` | 1,700,000.00 USD | 1,700,000.00 USD | 1,110.00 USD | 1,970.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7370` | 5,450,000.00 USD | 5,450,000.00 USD | 9,640.00 USD | 3,860.00 USD | 20,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7380` | 1,710,000.00 USD | 1,710,000.00 USD | 4,530.00 USD | 963.47 USD | 1,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7380` | 5,570,000.00 USD | 5,570,000.00 USD | 58,340.00 USD | 13,660.00 USD | 39,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7390` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 1,180.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7390` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 8,110.00 USD | 25,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7400` | 1,720,000.00 USD | 1,720,000.00 USD | 2,880.00 USD | 2,520.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7400` | 5,620,000.00 USD | 5,620,000.00 USD | 1,730.00 USD | 6,500.00 USD | 11,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7410` | 1,730,000.00 USD | 1,730,000.00 USD | 1,490.00 USD | 1,030.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7410` | 5,710,000.00 USD | 5,710,000.00 USD | 28,380.00 USD | 30,100.00 USD | 31,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7420` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 11.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7420` | 5,730,000.00 USD | 5,730,000.00 USD | 7,430.00 USD | 13,420.00 USD | 382.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7430` | 1,730,000.00 USD | 1,730,000.00 USD | 1,240.00 USD | 0.00 USD | 5.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7430` | 5,850,000.00 USD | 5,850,000.00 USD | 46,330.00 USD | 13,970.00 USD | 54,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7440` | 1,740,000.00 USD | 1,740,000.00 USD | 682.77 USD | 718.40 USD | 5,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7440` | 5,920,000.00 USD | 5,920,000.00 USD | 28,120.00 USD | 25,920.00 USD | 15,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7450` | 1,750,000.00 USD | 1,750,000.00 USD | 3,670.00 USD | 1,170.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7450` | 6,010,000.00 USD | 6,010,000.00 USD | 42,580.00 USD | 16,360.00 USD | 32,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7460` | 1,760,000.00 USD | 1,760,000.00 USD | 4,520.00 USD | 1,370.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7460` | 6,070,000.00 USD | 6,070,000.00 USD | 38,650.00 USD | 10,350.00 USD | 13,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7470` | 1,770,000.00 USD | 1,770,000.00 USD | 2,490.00 USD | 0.00 USD | 4,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7470` | 6,150,000.00 USD | 6,150,000.00 USD | 35,630.00 USD | 18,610.00 USD | 28,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7480` | 1,780,000.00 USD | 1,780,000.00 USD | 5,750.00 USD | 1,230.00 USD | 8,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7480` | 6,190,000.00 USD | 6,190,000.00 USD | 24,950.00 USD | 10,290.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7490` | 1,790,000.00 USD | 1,790,000.00 USD | 5,110.00 USD | 798.62 USD | 3,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7490` | 6,220,000.00 USD | 6,220,000.00 USD | 17,270.00 USD | 5,180.00 USD | 8,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7500` | 1,800,000.00 USD | 1,800,000.00 USD | 5,860.00 USD | 407.44 USD | 4,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7500` | 6,280,000.00 USD | 6,280,000.00 USD | 35,050.00 USD | 7,430.00 USD | 16,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7510` | 1,810,000.00 USD | 1,810,000.00 USD | 3,750.00 USD | 0.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7510` | 6,350,000.00 USD | 6,350,000.00 USD | 23,010.00 USD | 5,870.00 USD | 35,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7520` | 1,810,000.00 USD | 1,810,000.00 USD | 1,460.00 USD | 1,690.00 USD | 555.19 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7520` | 6,400,000.00 USD | 6,400,000.00 USD | 27,570.00 USD | 7,130.00 USD | 15,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7530` | 6,430,000.00 USD | 6,430,000.00 USD | 21,290.00 USD | 1,890.00 USD | 14,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7540` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 1,000.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7540` | 6,450,000.00 USD | 6,450,000.00 USD | 9,060.00 USD | 0.00 USD | 5,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7550` | 6,490,000.00 USD | 6,490,000.00 USD | 18,390.00 USD | 6,470.00 USD | 19,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7560` | 6,500,000.00 USD | 6,500,000.00 USD | 7,600.00 USD | 1,100.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7570` | 6,540,000.00 USD | 6,540,000.00 USD | 29,140.00 USD | 4,260.00 USD | 96.75 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7725` | 165.62 USD | 51,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.7765` | 330.78 USD | 51,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long` | `0.1875` | 246,420.00 USD | 0.00 USD | 269.27 USD | `-72.92%` | `1,436.09` |
| `Live` | `Long` | `0.1935` | 246,150.00 USD | 0.00 USD | 2,180.00 USD | `-72.06%` | `11,284.25` |
| `Live` | `Long` | `0.2025` | 243,970.00 USD | 0.00 USD | 506.25 USD | `-70.76%` | `2,500.00` |
| `Live` | `Long` | `0.2175` | 243,460.00 USD | 0.00 USD | 2,700.00 USD | `-68.59%` | `12,426.15` |
| `Live` | `Long` | `0.2555` | 240,760.00 USD | 0.00 USD | 511.00 USD | `-63.10%` | `2,000.00` |
| `Live` | `Long` | `0.2855` | 240,250.00 USD | 0.00 USD | 428.25 USD | `-58.77%` | `1,500.00` |
| `Live` | `Long` | `0.3155` | 239,820.00 USD | 0.00 USD | 8,970.00 USD | `-54.44%` | `28,446.85` |
| `Live` | `Long` | `0.3175` | 230,840.00 USD | 0.00 USD | 1,590.00 USD | `-54.15%` | `5,000.00` |
| `Live` | `Long` | `0.3225` | 229,260.00 USD | 0.00 USD | 415.54 USD | `-53.43%` | `1,288.49` |
| `Live` | `Long` | `0.3275` | 228,840.00 USD | 0.00 USD | 3,030.00 USD | `-52.71%` | `9,243.24` |
| `Live` | `Long` | `0.3305` | 225,810.00 USD | 0.00 USD | 543.58 USD | `-52.27%` | `1,644.73` |
| `Live` | `Long` | `0.3335` | 225,270.00 USD | 0.00 USD | 233.45 USD | `-51.84%` | `700.00` |
| `Live` | `Long` | `0.3405` | 225,040.00 USD | 0.00 USD | 640.60 USD | `-50.83%` | `1,881.36` |
| `Live` | `Long` | `0.3545` | 224,390.00 USD | 0.00 USD | 177.25 USD | `-48.81%` | `500.00` |
| `Live` | `Long` | `0.3565` | 224,220.00 USD | 0.00 USD | 2,140.00 USD | `-48.52%` | `6,000.00` |
| `Live` | `Long` | `0.3665` | 222,080.00 USD | 0.00 USD | 189.47 USD | `-47.08%` | `516.98` |
| `Live` | `Long` | `0.3675` | 221,890.00 USD | 0.00 USD | 194.23 USD | `-46.93%` | `528.52` |
| `Live` | `Long` | `0.3895` | 221,690.00 USD | 0.00 USD | 394.35 USD | `-43.75%` | `1,012.44` |
| `Live` | `Long` | `0.3905` | 221,300.00 USD | 0.00 USD | 359.26 USD | `-43.61%` | `919.99` |
| `Live` | `Long` | `0.3955` | 220,940.00 USD | 0.00 USD | 2,640.00 USD | `-42.89%` | `6,686.27` |
| `Live` | `Long` | `0.3995` | 218,300.00 USD | 0.00 USD | 271.06 USD | `-42.31%` | `678.49` |
| `Live` | `Long` | `0.4035` | 218,030.00 USD | 0.00 USD | 570.81 USD | `-41.73%` | `1,414.65` |
| `Live` | `Long` | `0.4135` | 217,450.00 USD | 0.00 USD | 1,600.00 USD | `-40.29%` | `3,868.97` |
| `Live` | `Long` | `0.4185` | 215,860.00 USD | 0.00 USD | 630.86 USD | `-39.57%` | `1,507.44` |
| `Live` | `Long` | `0.4255` | 215,220.00 USD | 0.00 USD | 224.96 USD | `-38.56%` | `528.69` |
| `Live` | `Long` | `0.4405` | 215,000.00 USD | 0.00 USD | 4,300.00 USD | `-36.39%` | `9,753.33` |
| `Live` | `Long` | `0.4455` | 210,700.00 USD | 0.00 USD | 5,080.00 USD | `-35.67%` | `11,392.84` |
| `Live` | `Long` | `0.4475` | 205,630.00 USD | 0.00 USD | 226.63 USD | `-35.38%` | `506.43` |
| `Live` | `Long` | `0.4515` | 205,400.00 USD | 0.00 USD | 27,090.00 USD | `-34.80%` | `60,000.00` |
| `Live` | `Long` | `0.4525` | 178,310.00 USD | 0.00 USD | 147.06 USD | `-34.66%` | `325.00` |
| `Live` | `Long` | `0.4605` | 178,160.00 USD | 0.00 USD | 1,080.00 USD | `-33.50%` | `2,350.33` |
| `Live` | `Long` | `0.4625` | 177,080.00 USD | 0.00 USD | 1,100.00 USD | `-33.21%` | `2,368.95` |
| `Live` | `Long` | `0.4675` | 175,990.00 USD | 0.00 USD | 7,710.00 USD | `-32.49%` | `16,497.37` |
| `Live` | `Long` | `0.4685` | 168,270.00 USD | 0.00 USD | 468.50 USD | `-32.35%` | `1,000.00` |
| `Live` | `Long` | `0.4755` | 167,800.00 USD | 0.00 USD | 472.63 USD | `-31.34%` | `993.96` |
| `Live` | `Long` | `0.4835` | 167,330.00 USD | 0.00 USD | 135.33 USD | `-30.18%` | `279.90` |
| `Live` | `Long` | `0.4855` | 167,200.00 USD | 0.00 USD | 3,160.00 USD | `-29.89%` | `6,508.47` |
| `Live` | `Long` | `0.4985` | 164,040.00 USD | 0.00 USD | 429.90 USD | `-28.01%` | `862.38` |
| `Live` | `Long` | `0.5085` | 163,610.00 USD | 0.00 USD | 102.82 USD | `-26.57%` | `202.20` |
| `Live` | `Long` | `0.5095` | 163,500.00 USD | 0.00 USD | 2,550.00 USD | `-26.43%` | `5,003.93` |
| `Live` | `Long` | `0.5125` | 160,950.00 USD | 0.00 USD | 248.05 USD | `-25.99%` | `484.00` |
| `Live` | `Long` | `0.5135` | 160,710.00 USD | 0.00 USD | 110.50 USD | `-25.85%` | `215.19` |
| `Live` | `Long` | `0.5145` | 160,600.00 USD | 0.00 USD | 288.78 USD | `-25.70%` | `561.28` |
| `Live` | `Long` | `0.5175` | 160,310.00 USD | 0.00 USD | 9,440.00 USD | `-25.27%` | `18,249.92` |
| `Live` | `Long` | `0.5315` | 150,860.00 USD | 0.00 USD | 11,510.00 USD | `-23.25%` | `21,664.95` |
| `Live` | `Long` | `0.5325` | 139,350.00 USD | 0.00 USD | 3,110.00 USD | `-23.10%` | `5,839.42` |
| `Live` | `Long` | `0.5335` | 136,240.00 USD | 0.00 USD | 163.22 USD | `-22.96%` | `305.95` |
| `Live` | `Long` | `0.5365` | 136,080.00 USD | 0.00 USD | 1,430.00 USD | `-22.53%` | `2,671.49` |
| `Live` | `Long` | `0.5385` | 134,640.00 USD | 0.00 USD | 2,690.00 USD | `-22.24%` | `5,002.20` |
| `Live` | `Long` | `0.5445` | 131,950.00 USD | 0.00 USD | 330.14 USD | `-21.37%` | `606.32` |
| `Live` | `Long` | `0.5475` | 131,620.00 USD | 0.00 USD | 482.65 USD | `-20.94%` | `881.55` |
| `Live` | `Long` | `0.5495` | 131,140.00 USD | 0.00 USD | 630.26 USD | `-20.65%` | `1,146.97` |
| `Live` | `Long` | `0.5545` | 130,510.00 USD | 0.00 USD | 67,280.00 USD | `-19.93%` | `121,332.93` |
| `Live` | `Long` | `0.5585` | 63,230.00 USD | 0.00 USD | 10,520.00 USD | `-19.35%` | `18,834.52` |
| `Live` | `Long` | `0.5615` | 52,710.00 USD | 0.00 USD | 1,720.00 USD | `-18.92%` | `3,064.43` |
| `Live` | `Long` | `0.5675` | 50,990.00 USD | 0.00 USD | 649.99 USD | `-18.05%` | `1,145.36` |
| `Live` | `Long` | `0.5695` | 50,340.00 USD | 0.00 USD | 164.24 USD | `-17.76%` | `288.40` |
| `Live` | `Long` | `0.5715` | 50,170.00 USD | 0.00 USD | 289.08 USD | `-17.47%` | `505.82` |
| `Live` | `Long` | `0.5735` | 49,880.00 USD | 0.00 USD | 214.84 USD | `-17.18%` | `374.62` |
| `Live` | `Long` | `0.5835` | 49,670.00 USD | 0.00 USD | 132.92 USD | `-15.74%` | `227.80` |
| `Live` | `Long` | `0.5845` | 49,540.00 USD | 0.00 USD | 210.96 USD | `-15.60%` | `360.92` |
| `Live` | `Long` | `0.5865` | 49,320.00 USD | 0.00 USD | 586.80 USD | `-15.31%` | `1,000.51` |
| `Live` | `Long` | `0.5885` | 48,740.00 USD | 0.00 USD | 440.16 USD | `-15.02%` | `747.93` |
| `Live` | `Long` | `0.5895` | 48,300.00 USD | 0.00 USD | 1,690.00 USD | `-14.87%` | `2,865.95` |
| `Live` | `Long` | `0.5925` | 46,610.00 USD | 0.00 USD | 609.14 USD | `-14.44%` | `1,028.09` |
| `Live` | `Long` | `0.5935` | 46,000.00 USD | 0.00 USD | 572.40 USD | `-14.30%` | `964.45` |
| `Live` | `Long` | `0.5945` | 45,430.00 USD | 0.00 USD | 3,850.00 USD | `-14.15%` | `6,467.73` |
| `Live` | `Long` | `0.5975` | 41,580.00 USD | 0.00 USD | 157.22 USD | `-13.72%` | `263.13` |
| `Live` | `Long` | `0.6005` | 41,420.00 USD | 0.00 USD | 852.06 USD | `-13.29%` | `1,418.92` |
| `Live` | `Long` | `0.6025` | 40,570.00 USD | 0.00 USD | 451.19 USD | `-13.00%` | `748.87` |
| `Live` | `Long` | `0.6045` | 40,120.00 USD | 0.00 USD | 527.44 USD | `-12.71%` | `872.53` |
| `Live` | `Long` | `0.6105` | 39,590.00 USD | 0.00 USD | 126.47 USD | `-11.84%` | `207.16` |
| `Live` | `Long` | `0.6195` | 39,470.00 USD | 0.00 USD | 3,170.00 USD | `-10.54%` | `5,109.42` |
| `Live` | `Long` | `0.6235` | 36,300.00 USD | 0.00 USD | 3,250.00 USD | `-9.96%` | `5,220.30` |
| `Live` | `Long` | `0.6245` | 33,050.00 USD | 0.00 USD | 1,960.00 USD | `-9.82%` | `3,142.95` |
| `Live` | `Long` | `0.6255` | 31,080.00 USD | 0.00 USD | 286.65 USD | `-9.68%` | `458.28` |
| `Live` | `Long` | `0.6265` | 30,800.00 USD | 0.00 USD | 10,530.00 USD | `-9.53%` | `16,808.62` |
| `Live` | `Long` | `0.6285` | 20,270.00 USD | 0.00 USD | 903.47 USD | `-9.24%` | `1,437.50` |
| `Live` | `Long` | `0.6315` | 19,360.00 USD | 0.00 USD | 1,010.00 USD | `-8.81%` | `1,599.74` |
| `Live` | `Long` | `0.6375` | 18,350.00 USD | 0.00 USD | 5,900.00 USD | `-7.94%` | `9,256.34` |
| `Live` | `Long` | `0.6415` | 12,450.00 USD | 0.00 USD | 4,740.00 USD | `-7.36%` | `7,394.26` |
| `Live` | `Long` | `0.6435` | 7,710.00 USD | 0.00 USD | 2,320.00 USD | `-7.08%` | `3,602.46` |
| `Live` | `Long` | `0.6455` | 5,390.00 USD | 0.00 USD | 3,730.00 USD | `-6.79%` | `5,780.73` |
| `Live` | `Long` | `0.6485` | 1,660.00 USD | 0.00 USD | 259.68 USD | `-6.35%` | `400.43` |
| `Live` | `Long` | `0.6505` | 1,400.00 USD | 0.00 USD | 580.53 USD | `-6.06%` | `892.44` |
| `Live` | `Long` | `0.6695` | 818.97 USD | 0.00 USD | 818.97 USD | `-3.32%` | `1,223.26` |
| `Live` | `Short` | `0.7235` | 42,980.00 USD | 42,980.00 USD | 0.00 USD | `+4.48%` | `59,401.36` |
| `Live` | `Short` | `0.7255` | 43,710.00 USD | 729.79 USD | 0.00 USD | `+4.77%` | `1,005.92` |
| `Live` | `Short` | `0.7265` | 43,830.00 USD | 124.62 USD | 0.00 USD | `+4.91%` | `171.53` |
| `Live` | `Short` | `0.7325` | 50,990.00 USD | 7,150.00 USD | 0.00 USD | `+5.78%` | `9,766.84` |
| `Live` | `Short` | `0.7345` | 51,140.00 USD | 150.17 USD | 0.00 USD | `+6.06%` | `204.45` |
| `Live` | `Short` | `0.7725` | 51,300.00 USD | 165.62 USD | 0.00 USD | `+11.55%` | `214.40` |
| `Live` | `Short` | `0.7765` | 51,630.00 USD | 330.78 USD | 0.00 USD | `+12.13%` | `425.99` |
| `Live` | `Short` | `0.8005` | 70,750.00 USD | 19,120.00 USD | 0.00 USD | `+15.60%` | `23,882.80` |
| `Live` | `Short` | `0.8035` | 70,860.00 USD | 114.11 USD | 0.00 USD | `+16.03%` | `142.02` |
| `Live` | `Short` | `0.8405` | 73,020.00 USD | 2,150.00 USD | 0.00 USD | `+21.37%` | `2,560.86` |
| `Live` | `Short` | `0.8615` | 88,660.00 USD | 15,640.00 USD | 0.00 USD | `+24.40%` | `18,155.35` |
| `Live` | `Short` | `0.8665` | 89,040.00 USD | 378.95 USD | 0.00 USD | `+25.13%` | `437.33` |
| `Live` | `Short` | `0.9935` | 89,200.00 USD | 166.01 USD | 0.00 USD | `+43.47%` | `167.10` |
| `Live` | `Short` | `1.03` | 109,150.00 USD | 19,950.00 USD | 0.00 USD | `+48.23%` | `19,437.03` |
| `Live` | `Short` | `1.03` | 188,010.00 USD | 78,860.00 USD | 0.00 USD | `+49.24%` | `76,300.00` |
| `Live` | `Short` | `1.08` | 207,080.00 USD | 19,070.00 USD | 0.00 USD | `+56.03%` | `17,648.14` |
| `Live` | `Short` | `1.09` | 210,160.00 USD | 3,080.00 USD | 0.00 USD | `+57.04%` | `2,829.20` |
| `Live` | `Short` | `1.09` | 210,640.00 USD | 479.74 USD | 0.00 USD | `+57.62%` | `439.52` |
| `Live` | `Short` | `1.12` | 213,430.00 USD | 2,800.00 USD | 0.00 USD | `+61.66%` | `2,500.00` |
| `Live` | `Short` | `1.27` | 226,750.00 USD | 13,320.00 USD | 0.00 USD | `+83.18%` | `10,500.00` |
| `Live` | `Short` | `1.32` | 226,950.00 USD | 197.51 USD | 0.00 USD | `+90.83%` | `149.46` |
| `Live` | `Short` | `1.33` | 227,240.00 USD | 284.61 USD | 0.00 USD | `+91.99%` | `214.07` |
| `Live` | `Short` | `1.36` | 232,680.00 USD | 5,440.00 USD | 0.00 USD | `+96.46%` | `4,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.3505` | 130,060.00 USD | 0.00 USD | 340.19 USD | `-49.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4635` | 129,710.00 USD | 0.00 USD | 104.57 USD | `-33.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4805` | 129,610.00 USD | 0.00 USD | 14,740.00 USD | `-30.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 114,870.00 USD | 0.00 USD | 604.46 USD | `-27.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5125` | 114,270.00 USD | 0.00 USD | 5,380.00 USD | `-25.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5205` | 108,890.00 USD | 0.00 USD | 228.77 USD | `-24.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5305` | 108,660.00 USD | 0.00 USD | 770.19 USD | `-23.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5445` | 107,890.00 USD | 0.00 USD | 14,110.00 USD | `-21.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5485` | 93,780.00 USD | 0.00 USD | 4,500.00 USD | `-20.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5555` | 89,280.00 USD | 0.00 USD | 33,000.00 USD | `-19.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5565` | 56,290.00 USD | 0.00 USD | 173.58 USD | `-19.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 56,110.00 USD | 0.00 USD | 339.84 USD | `-19.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5835` | 55,770.00 USD | 0.00 USD | 178.88 USD | `-15.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5865` | 55,590.00 USD | 0.00 USD | 128.36 USD | `-15.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5875` | 55,460.00 USD | 0.00 USD | 128.34 USD | `-15.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5895` | 55,340.00 USD | 0.00 USD | 128.45 USD | `-14.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5925` | 55,210.00 USD | 0.00 USD | 128.33 USD | `-14.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5975` | 55,080.00 USD | 0.00 USD | 597.80 USD | `-13.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 54,480.00 USD | 0.00 USD | 3,640.00 USD | `-13.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 50,840.00 USD | 0.00 USD | 1,510.00 USD | `-12.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6085` | 49,330.00 USD | 0.00 USD | 301.32 USD | `-12.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6115` | 49,030.00 USD | 0.00 USD | 2,230.00 USD | `-11.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6125` | 46,800.00 USD | 0.00 USD | 108.68 USD | `-11.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6185` | 46,700.00 USD | 0.00 USD | 177.58 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 46,520.00 USD | 0.00 USD | 541.40 USD | `-10.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6285` | 45,980.00 USD | 0.00 USD | 469.94 USD | `-9.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 45,510.00 USD | 0.00 USD | 4,430.00 USD | `-8.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6315` | 41,080.00 USD | 0.00 USD | 160.16 USD | `-8.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6335` | 40,920.00 USD | 0.00 USD | 8,390.00 USD | `-8.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6345` | 32,520.00 USD | 0.00 USD | 276.40 USD | `-8.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6395` | 32,250.00 USD | 0.00 USD | 1,200.00 USD | `-7.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6405` | 31,050.00 USD | 0.00 USD | 145.91 USD | `-7.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6485` | 30,900.00 USD | 0.00 USD | 447.03 USD | `-6.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 30,460.00 USD | 0.00 USD | 594.15 USD | `-6.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6525` | 29,860.00 USD | 0.00 USD | 111.92 USD | `-5.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 29,750.00 USD | 0.00 USD | 349.76 USD | `-5.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 29,400.00 USD | 0.00 USD | 4,080.00 USD | `-5.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6565` | 25,320.00 USD | 0.00 USD | 284.88 USD | `-5.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6575` | 25,040.00 USD | 0.00 USD | 195.39 USD | `-5.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6585` | 24,840.00 USD | 0.00 USD | 1,440.00 USD | `-4.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6595` | 23,400.00 USD | 0.00 USD | 746.46 USD | `-4.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6605` | 22,660.00 USD | 0.00 USD | 580.23 USD | `-4.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6655` | 22,080.00 USD | 0.00 USD | 1,110.00 USD | `-3.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6665` | 20,970.00 USD | 0.00 USD | 151.65 USD | `-3.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6675` | 20,820.00 USD | 0.00 USD | 290.78 USD | `-3.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6685` | 20,530.00 USD | 0.00 USD | 170.95 USD | `-3.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6695` | 20,360.00 USD | 0.00 USD | 1,670.00 USD | `-3.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 18,690.00 USD | 0.00 USD | 162.91 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6715` | 18,530.00 USD | 0.00 USD | 202.63 USD | `-3.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6725` | 18,320.00 USD | 0.00 USD | 1,670.00 USD | `-2.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6745` | 16,650.00 USD | 0.00 USD | 995.25 USD | `-2.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6755` | 15,650.00 USD | 0.00 USD | 361.53 USD | `-2.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6765` | 15,290.00 USD | 0.00 USD | 111.50 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6805` | 15,180.00 USD | 0.00 USD | 214.20 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6815` | 14,970.00 USD | 0.00 USD | 10,560.00 USD | `-1.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6825` | 4,410.00 USD | 0.00 USD | 112.49 USD | `-1.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6835` | 4,290.00 USD | 0.00 USD | 108.41 USD | `-1.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6855` | 4,180.00 USD | 0.00 USD | 112.98 USD | `-1.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6865` | 4,070.00 USD | 0.00 USD | 292.33 USD | `-0.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6875` | 3,780.00 USD | 0.00 USD | 140.41 USD | `-0.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6885` | 3,640.00 USD | 0.00 USD | 514.80 USD | `-0.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6895` | 3,120.00 USD | 0.00 USD | 194.09 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6905` | 2,930.00 USD | 0.00 USD | 2,830.00 USD | `-0.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6915` | 101.96 USD | 0.00 USD | 101.96 USD | `-0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6925` | 1,020.00 USD | 1,020.00 USD | 0.00 USD | `+0.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6945` | 1,630.00 USD | 610.10 USD | 0.00 USD | `+0.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6955` | 2,600.00 USD | 972.94 USD | 0.00 USD | `+0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6965` | 8,000.00 USD | 5,390.00 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6985` | 8,100.00 USD | 102.99 USD | 0.00 USD | `+0.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7005` | 8,240.00 USD | 137.19 USD | 0.00 USD | `+1.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7015` | 8,800.00 USD | 561.40 USD | 0.00 USD | `+1.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7025` | 9,840.00 USD | 1,030.00 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7045` | 10,530.00 USD | 692.13 USD | 0.00 USD | `+1.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7055` | 14,540.00 USD | 4,010.00 USD | 0.00 USD | `+1.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7075` | 17,120.00 USD | 2,580.00 USD | 0.00 USD | `+2.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7085` | 18,070.00 USD | 947.29 USD | 0.00 USD | `+2.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7095` | 18,220.00 USD | 150.80 USD | 0.00 USD | `+2.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7115` | 18,340.00 USD | 122.04 USD | 0.00 USD | `+2.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7125` | 18,500.00 USD | 162.12 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7135` | 18,810.00 USD | 307.58 USD | 0.00 USD | `+3.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7155` | 19,900.00 USD | 1,090.00 USD | 0.00 USD | `+3.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7165` | 21,740.00 USD | 1,830.00 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7195` | 22,110.00 USD | 373.99 USD | 0.00 USD | `+3.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7205` | 22,260.00 USD | 147.15 USD | 0.00 USD | `+4.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7215` | 25,520.00 USD | 3,260.00 USD | 0.00 USD | `+4.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7225` | 25,670.00 USD | 150.08 USD | 0.00 USD | `+4.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7265` | 31,960.00 USD | 6,290.00 USD | 0.00 USD | `+4.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7305` | 47,560.00 USD | 15,600.00 USD | 0.00 USD | `+5.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7325` | 47,720.00 USD | 165.17 USD | 0.00 USD | `+5.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7345` | 48,750.00 USD | 1,030.00 USD | 0.00 USD | `+6.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7375` | 48,860.00 USD | 106.75 USD | 0.00 USD | `+6.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7395` | 49,070.00 USD | 208.16 USD | 0.00 USD | `+6.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7405` | 49,800.00 USD | 733.09 USD | 0.00 USD | `+6.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7415` | 49,960.00 USD | 156.98 USD | 0.00 USD | `+7.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7425` | 50,090.00 USD | 132.95 USD | 0.00 USD | `+7.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7445` | 50,850.00 USD | 757.16 USD | 0.00 USD | `+7.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7455` | 53,010.00 USD | 2,170.00 USD | 0.00 USD | `+7.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7475` | 53,330.00 USD | 318.43 USD | 0.00 USD | `+7.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7495` | 53,460.00 USD | 132.98 USD | 0.00 USD | `+8.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7505` | 53,580.00 USD | 110.33 USD | 0.00 USD | `+8.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7525` | 53,710.00 USD | 134.74 USD | 0.00 USD | `+8.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7565` | 57,830.00 USD | 4,120.00 USD | 0.00 USD | `+9.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7575` | 58,340.00 USD | 511.82 USD | 0.00 USD | `+9.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7585` | 58,470.00 USD | 135.82 USD | 0.00 USD | `+9.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7615` | 59,350.00 USD | 875.23 USD | 0.00 USD | `+9.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7635` | 59,450.00 USD | 103.35 USD | 0.00 USD | `+10.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7665` | 59,580.00 USD | 127.48 USD | 0.00 USD | `+10.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7675` | 59,680.00 USD | 101.61 USD | 0.00 USD | `+10.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7695` | 59,870.00 USD | 186.97 USD | 0.00 USD | `+11.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7775` | 60,030.00 USD | 166.70 USD | 0.00 USD | `+12.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7815` | 61,170.00 USD | 1,140.00 USD | 0.00 USD | `+12.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7865` | 67,480.00 USD | 6,310.00 USD | 0.00 USD | `+13.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8095` | 67,620.00 USD | 133.42 USD | 0.00 USD | `+16.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8125` | 79,690.00 USD | 12,070.00 USD | 0.00 USD | `+17.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8235` | 82,580.00 USD | 2,890.00 USD | 0.00 USD | `+18.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8335` | 83,510.00 USD | 929.08 USD | 0.00 USD | `+20.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8475` | 114,630.00 USD | 31,120.00 USD | 0.00 USD | `+22.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8505` | 117,690.00 USD | 3,060.00 USD | 0.00 USD | `+22.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8515` | 128,720.00 USD | 11,030.00 USD | 0.00 USD | `+22.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8705` | 130,000.00 USD | 1,280.00 USD | 0.00 USD | `+25.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8725` | 130,160.00 USD | 159.86 USD | 0.00 USD | `+25.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 133,450.00 USD | 3,290.00 USD | 0.00 USD | `+35.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 133,790.00 USD | 340.54 USD | 0.00 USD | `+37.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 133,930.00 USD | 145.72 USD | 0.00 USD | `+40.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 134,920.00 USD | 987.50 USD | 0.00 USD | `+42.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 135,060.00 USD | 136.10 USD | 0.00 USD | `+44.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 135,610.00 USD | 550.48 USD | 0.00 USD | `+44.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 135,920.00 USD | 314.99 USD | 0.00 USD | `+48.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 136,520.00 USD | 602.17 USD | 0.00 USD | `+51.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 136,890.00 USD | 360.61 USD | 0.00 USD | `+53.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 137,830.00 USD | 942.77 USD | 0.00 USD | `+56.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 138,170.00 USD | 337.31 USD | 0.00 USD | `+56.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 138,560.00 USD | 397.19 USD | 0.00 USD | `+58.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 151,690.00 USD | 13,130.00 USD | 0.00 USD | `+80.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 153,020.00 USD | 1,320.00 USD | 0.00 USD | `+82.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 189,870.00 USD | 36,850.00 USD | 0.00 USD | `+87.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 217,080.00 USD | 27,210.00 USD | 0.00 USD | `+96.46%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.5810` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 5,930.00 USD |
| `7D` | `0.5820` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD |
| `7D` | `0.5870` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 0.00 USD | 1,400.00 USD | 0.00 USD |
| `7D` | `0.5880` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 3,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.5890` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 81.07 USD |
| `7D` | `0.5900` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 3,120.00 USD | 1,560.00 USD | 0.00 USD |
| `7D` | `0.5920` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 0.00 USD | 2,820.00 USD | 0.00 USD |
| `7D` | `0.5930` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 10,090.00 USD | 0.00 USD | 9,780.00 USD |
| `7D` | `0.5950` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 5,120.00 USD | 0.00 USD | 4,580.00 USD |
| `7D` | `0.5960` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 5,120.00 USD | 1,640.00 USD | 0.00 USD |
| `7D` | `0.5970` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 9,710.00 USD |
| `7D` | `0.5980` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 7,660.00 USD | 826.53 USD | 0.00 USD |
| `7D` | `0.5990` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 3,320.00 USD | 1,340.00 USD | 14,110.00 USD |
| `7D` | `0.6000` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 0.00 USD | 796.28 USD | 4,700.00 USD |
| `1D` | `0.6010` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 735.24 USD | 461.96 USD | 1,230.00 USD |
| `1D` | `0.6020` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 4,120.00 USD | 1,800.00 USD | 3,710.00 USD |
| `7D` | `0.6020` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 10,590.00 USD | 8,040.00 USD | 4,010.00 USD |
| `1D` | `0.6030` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 1,110.00 USD | 1,970.00 USD | 3,690.00 USD |
| `7D` | `0.6030` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 2,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6040` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 4,530.00 USD | 963.47 USD | 1,860.00 USD |
| `7D` | `0.6040` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 7,830.00 USD |
| `1D` | `0.6050` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 599.00 USD | 1,200.00 USD |
| `7D` | `0.6050` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 36.57 USD |
| `1D` | `0.6060` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 2,880.00 USD | 606.70 USD | 3,020.00 USD |
| `7D` | `0.6060` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 2,850.00 USD | 0.00 USD | 55.47 USD |
| `1D` | `0.6070` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 1,490.00 USD | 1,030.00 USD | 4,740.00 USD |
| `7D` | `0.6070` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 148.03 USD |
| `1D` | `0.6080` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 1,920.00 USD | 0.00 USD | 1,530.00 USD |
| `7D` | `0.6080` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 2,860.00 USD | 0.00 USD | 72.33 USD |
| `1D` | `0.6090` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 3,670.00 USD | 0.00 USD | 45.55 USD |
| `7D` | `0.6090` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 6,360.00 USD | 0.00 USD | 3,680.00 USD |
| `1D` | `0.6100` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 4,520.00 USD | 1,370.00 USD | 6,210.00 USD |
| `7D` | `0.6100` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 7,480.00 USD | 2,570.00 USD | 98.50 USD |
| `1D` | `0.6110` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 2,490.00 USD | 0.00 USD | 1,220.00 USD |
| `7D` | `0.6110` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 0.00 USD | 2,210.00 USD | 6,970.00 USD |
| `1D` | `0.6120` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 2,530.00 USD | 1,230.00 USD | 8,310.00 USD |
| `7D` | `0.6120` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 2,100.00 USD | 3,510.00 USD | 7,160.00 USD |
| `1D` | `0.6130` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 5,110.00 USD | 798.62 USD | 3,190.00 USD |
| `7D` | `0.6130` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 8,870.00 USD | 1,050.00 USD | 4,040.00 USD |
| `1D` | `0.6140` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 5,860.00 USD | 407.44 USD | 4,540.00 USD |
| `7D` | `0.6140` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 4,540.00 USD | 7,000.00 USD | 6,650.00 USD |
| `1D` | `0.6150` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 3,750.00 USD | 0.00 USD | 1,490.00 USD |
| `7D` | `0.6150` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 8,250.00 USD | 5,870.00 USD | 2,820.00 USD |
| `1D` | `0.6160` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 1,460.00 USD | 1,690.00 USD | 681.25 USD |
| `7D` | `0.6160` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 1,790.00 USD | 2,510.00 USD | 3,710.00 USD |
| `1D` | `0.6170` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 0.00 USD | 1,000.00 USD | 5,210.00 USD |
| `7D` | `0.6170` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 13,260.00 USD | 2,610.00 USD | 9,800.00 USD |
| `1D` | `0.6180` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 676.84 USD | 1,010.00 USD | 1,550.00 USD |
| `7D` | `0.6180` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 7,600.00 USD | 1,190.00 USD | 6,130.00 USD |
| `1D` | `0.6190` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 3,170.00 USD | 492.27 USD | 1,560.00 USD |
| `7D` | `0.6190` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 9,560.00 USD | 1,930.00 USD | 9,330.00 USD |
| `1D` | `0.6200` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 1,010.00 USD | 0.00 USD | 855.60 USD |
| `7D` | `0.6200` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 13,870.00 USD | 5,230.00 USD | 6,050.00 USD |
| `1D` | `0.6210` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 922.83 USD |
| `7D` | `0.6210` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 4,760.00 USD | 1,860.00 USD | 2,520.00 USD |
| `1D` | `0.6220` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 7.22 USD |
| `7D` | `0.6220` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 3,290.00 USD | 2,310.00 USD | 29,860.00 USD |
| `1D` | `0.6230` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 11.55 USD |
| `7D` | `0.6230` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 9,770.00 USD | 4,700.00 USD | 8,350.00 USD |
| `1D` | `0.6240` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 2,670.00 USD | 1,130.00 USD | 60.89 USD |
| `7D` | `0.6240` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 18,610.00 USD | 2,010.00 USD | 5,000.00 USD |
| `1D` | `0.6250` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 1,800.00 USD | 2,630.00 USD | 36.04 USD |
| `7D` | `0.6250` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 16,120.00 USD | 3,830.00 USD | 2,340.00 USD |
| `1D` | `0.6260` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 10,030.00 USD | 1,310.00 USD | 8,290.00 USD |
| `7D` | `0.6260` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 20,890.00 USD | 7,660.00 USD | 25,960.00 USD |
| `1D` | `0.6270` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 3,700.00 USD | 3,940.00 USD | 11,400.00 USD |
| `7D` | `0.6270` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 17,460.00 USD | 8,200.00 USD | 14,540.00 USD |
| `1D` | `0.6280` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 11,690.00 USD | 463.43 USD | 870.18 USD |
| `7D` | `0.6280` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 9,160.00 USD | 9,230.00 USD | 16,780.00 USD |
| `1D` | `0.6290` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 8,430.00 USD | 1,200.00 USD | 5,090.00 USD |
| `7D` | `0.6290` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 17,710.00 USD | 6,740.00 USD | 10,350.00 USD |
| `1D` | `0.6300` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 12,950.00 USD | 2,470.00 USD | 2,930.00 USD |
| `7D` | `0.6300` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 10,040.00 USD | 7,890.00 USD | 11,300.00 USD |
| `1D` | `0.6310` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 5,850.00 USD | 5,110.00 USD | 1,730.00 USD |
| `7D` | `0.6310` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 19,340.00 USD | 4,520.00 USD | 17,330.00 USD |
| `1D` | `0.6320` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 12,320.00 USD | 9,530.00 USD | 13,920.00 USD |
| `7D` | `0.6320` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 4,880.00 USD | 12,650.00 USD | 8,610.00 USD |
| `1D` | `0.6330` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 17,300.00 USD | 3,580.00 USD | 21,040.00 USD |
| `7D` | `0.6330` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 57,940.00 USD | 12,500.00 USD | 33,780.00 USD |
| `1D` | `0.6340` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 9,830.00 USD | 2,020.00 USD | 15,400.00 USD |
| `7D` | `0.6340` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 10,730.00 USD | 3,420.00 USD | 4,630.00 USD |
| `1D` | `0.6350` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 19,180.00 USD | 8,820.00 USD | 4,220.00 USD |
| `7D` | `0.6350` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 14,450.00 USD | 2,430.00 USD | 22,910.00 USD |
| `1D` | `0.6360` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 30,350.00 USD | 9,150.00 USD | 33,320.00 USD |
| `7D` | `0.6360` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 42,690.00 USD | 7,300.00 USD | 40,390.00 USD |
| `1D` | `0.6370` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 21,750.00 USD | 4,510.00 USD | 27,390.00 USD |
| `7D` | `0.6370` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 49,080.00 USD | 4,870.00 USD | 93.41 USD |
| `1D` | `0.6380` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 19,430.00 USD | 7,180.00 USD | 7,690.00 USD |
| `7D` | `0.6380` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 18,140.00 USD | 3,870.00 USD | 30,290.00 USD |
| `1D` | `0.6390` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 18,790.00 USD | 529.57 USD | 6,670.00 USD |
| `7D` | `0.6390` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 10,200.00 USD | 7,510.00 USD | 13,200.00 USD |
| `1D` | `0.6400` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 9,830.00 USD | 9,970.00 USD | 25,490.00 USD |
| `7D` | `0.6400` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 15,560.00 USD | 0.00 USD | 526.14 USD |
| `1D` | `0.6410` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 20,930.00 USD | 2,240.00 USD | 3,610.00 USD |
| `7D` | `0.6410` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 6,290.00 USD |
| `1D` | `0.6420` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 32,540.00 USD | 7,850.00 USD | 12,640.00 USD |
| `7D` | `0.6420` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 39,060.00 USD | 26,560.00 USD | 10,110.00 USD |
| `1D` | `0.6430` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 25,620.00 USD | 7,460.00 USD | 9,320.00 USD |
| `7D` | `0.6430` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 16,200.00 USD | 3,970.00 USD | 2,800.00 USD |
| `1D` | `0.6440` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 21,790.00 USD | 11,330.00 USD | 8,490.00 USD |
| `7D` | `0.6440` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 14,160.00 USD | 6,720.00 USD | 15,060.00 USD |
| `1D` | `0.6450` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 23,100.00 USD | 20,050.00 USD | 31,390.00 USD |
| `7D` | `0.6450` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 14,120.00 USD | 15,560.00 USD | 311.53 USD |
| `1D` | `0.6460` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 43,360.00 USD | 10,480.00 USD | 51,640.00 USD |
| `7D` | `0.6460` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 75,060.00 USD | 14,300.00 USD | 75,510.00 USD |
| `1D` | `0.6470` | 903,010.00 USD | 0.00 USD | 903,010.00 USD | 30,630.00 USD | 6,620.00 USD | 41,780.00 USD |
| `7D` | `0.6470` | 964,030.00 USD | 0.00 USD | 964,030.00 USD | 9,660.00 USD | 3,880.00 USD | 9,280.00 USD |
| `1D` | `0.6480` | 823,990.00 USD | 0.00 USD | 823,990.00 USD | 48,130.00 USD | 14,180.00 USD | 7,740.00 USD |
| `7D` | `0.6480` | 941,210.00 USD | 0.00 USD | 941,210.00 USD | 37,050.00 USD | 0.00 USD | 23,440.00 USD |
| `1D` | `0.6490` | 753,930.00 USD | 0.00 USD | 753,930.00 USD | 30,360.00 USD | 3,800.00 USD | 40,810.00 USD |
| `7D` | `0.6490` | 880,730.00 USD | 0.00 USD | 880,730.00 USD | 36,340.00 USD | 0.00 USD | 17,850.00 USD |
| `1D` | `0.6500` | 678,960.00 USD | 0.00 USD | 678,960.00 USD | 48,860.00 USD | 1,390.00 USD | 32,600.00 USD |
| `7D` | `0.6500` | 826,540.00 USD | 0.00 USD | 826,540.00 USD | 18,310.00 USD | 0.00 USD | 67,120.00 USD |
| `1D` | `0.6510` | 596,110.00 USD | 0.00 USD | 596,110.00 USD | 15,700.00 USD | 4,450.00 USD | 66,790.00 USD |
| `7D` | `0.6510` | 741,120.00 USD | 0.00 USD | 741,120.00 USD | 101,440.00 USD | 4,190.00 USD | 328.84 USD |
| `1D` | `0.6520` | 509,170.00 USD | 0.00 USD | 509,170.00 USD | 31,260.00 USD | 5,680.00 USD | 19,450.00 USD |
| `7D` | `0.6520` | 635,150.00 USD | 0.00 USD | 635,150.00 USD | 39,510.00 USD | 6,720.00 USD | 72,070.00 USD |
| `1D` | `0.6530` | 452,780.00 USD | 0.00 USD | 452,780.00 USD | 5,780.00 USD | 1,060.00 USD | 11,740.00 USD |
| `7D` | `0.6530` | 516,860.00 USD | 0.00 USD | 516,860.00 USD | 0.00 USD | 0.00 USD | 46,940.00 USD |
| `1D` | `0.6540` | 434,200.00 USD | 0.00 USD | 434,200.00 USD | 11,450.00 USD | 2,530.00 USD | 15,300.00 USD |
| `7D` | `0.6540` | 469,920.00 USD | 0.00 USD | 469,920.00 USD | 15,730.00 USD | 0.00 USD | 14,520.00 USD |
| `1D` | `0.6550` | 404,920.00 USD | 0.00 USD | 404,920.00 USD | 13,860.00 USD | 5,390.00 USD | 20,410.00 USD |
| `7D` | `0.6550` | 439,670.00 USD | 0.00 USD | 439,670.00 USD | 0.00 USD | 0.00 USD | 38,340.00 USD |
| `1D` | `0.6560` | 365,260.00 USD | 0.00 USD | 365,260.00 USD | 23,680.00 USD | 3,800.00 USD | 33,800.00 USD |
| `7D` | `0.6560` | 401,330.00 USD | 0.00 USD | 401,330.00 USD | 0.00 USD | 5,380.00 USD | 34,710.00 USD |
| `1D` | `0.6570` | 303,980.00 USD | 0.00 USD | 303,980.00 USD | 5,570.00 USD | 1,820.00 USD | 23,560.00 USD |
| `7D` | `0.6570` | 361,240.00 USD | 0.00 USD | 361,240.00 USD | 14,440.00 USD | 0.00 USD | 10,710.00 USD |
| `1D` | `0.6580` | 273,030.00 USD | 0.00 USD | 273,030.00 USD | 5,880.00 USD | 0.00 USD | 0.08 USD |
| `7D` | `0.6580` | 336,090.00 USD | 0.00 USD | 336,090.00 USD | 0.00 USD | 0.00 USD | 240.54 USD |
| `1D` | `0.6590` | 267,140.00 USD | 0.00 USD | 267,140.00 USD | 0.00 USD | 3,890.00 USD | 11,220.00 USD |
| `7D` | `0.6590` | 335,850.00 USD | 0.00 USD | 335,850.00 USD | 9,540.00 USD | 0.00 USD | 61.15 USD |
| `1D` | `0.6600` | 252,030.00 USD | 0.00 USD | 252,030.00 USD | 11,650.00 USD | 2,120.00 USD | 22,600.00 USD |
| `7D` | `0.6600` | 326,250.00 USD | 0.00 USD | 326,250.00 USD | 0.00 USD | 4,180.00 USD | 20,450.00 USD |
| `1D` | `0.6610` | 215,650.00 USD | 0.00 USD | 215,650.00 USD | 11,920.00 USD | 2,560.00 USD | 7,830.00 USD |
| `7D` | `0.6610` | 301,620.00 USD | 0.00 USD | 301,620.00 USD | 0.00 USD | 0.00 USD | 379.61 USD |
| `1D` | `0.6620` | 193,340.00 USD | 0.00 USD | 193,340.00 USD | 9,060.00 USD | 1,160.00 USD | 11,670.00 USD |
| `7D` | `0.6620` | 301,240.00 USD | 0.00 USD | 301,240.00 USD | 14,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6630` | 171,450.00 USD | 0.00 USD | 171,450.00 USD | 14,750.00 USD | 2,780.00 USD | 2.53 USD |
| `7D` | `0.6630` | 286,920.00 USD | 0.00 USD | 286,920.00 USD | 0.00 USD | 0.00 USD | 271.36 USD |
| `1D` | `0.6640` | 153,910.00 USD | 0.00 USD | 153,910.00 USD | 16,520.00 USD | 0.00 USD | 11,380.00 USD |
| `7D` | `0.6640` | 286,650.00 USD | 0.00 USD | 286,650.00 USD | 8,590.00 USD | 0.00 USD | 102.26 USD |
| `1D` | `0.6650` | 126,010.00 USD | 0.00 USD | 126,010.00 USD | 7,140.00 USD | 0.00 USD | 1,870.00 USD |
| `7D` | `0.6650` | 277,960.00 USD | 0.00 USD | 277,960.00 USD | 0.00 USD | 0.00 USD | 231.32 USD |
| `1D` | `0.6660` | 117,000.00 USD | 0.00 USD | 117,000.00 USD | 7,730.00 USD | 0.00 USD | 5,410.00 USD |
| `7D` | `0.6660` | 277,730.00 USD | 0.00 USD | 277,730.00 USD | 0.00 USD | 0.00 USD | 244.64 USD |
| `1D` | `0.6670` | 103,860.00 USD | 0.00 USD | 103,860.00 USD | 18,850.00 USD | 2,980.00 USD | 4,930.00 USD |
| `7D` | `0.6670` | 277,480.00 USD | 0.00 USD | 277,480.00 USD | 31,450.00 USD | 0.00 USD | 8,770.00 USD |
| `1D` | `0.6680` | 77,100.00 USD | 0.00 USD | 77,100.00 USD | 20,370.00 USD | 3,380.00 USD | 4,850.00 USD |
| `7D` | `0.6680` | 237,260.00 USD | 0.00 USD | 237,260.00 USD | 24,780.00 USD | 7,780.00 USD | 771.72 USD |
| `1D` | `0.6690` | 48,500.00 USD | 0.00 USD | 48,500.00 USD | 13,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6690` | 203,930.00 USD | 0.00 USD | 203,930.00 USD | 0.00 USD | 0.00 USD | 145.17 USD |
| `7D` | `0.6700` | 203,780.00 USD | 0.00 USD | 203,780.00 USD | 0.00 USD | 0.00 USD | 72.32 USD |
| `1D` | `0.6710` | 35,500.00 USD | 0.00 USD | 35,500.00 USD | 0.00 USD | 18,100.00 USD | 0.00 USD |
| `7D` | `0.6710` | 203,710.00 USD | 0.00 USD | 203,710.00 USD | 0.00 USD | 6,960.00 USD | 62.19 USD |
| `1D` | `0.6720` | 17,400.00 USD | 0.00 USD | 17,400.00 USD | 0.00 USD | 0.00 USD | 3.80 USD |
| `7D` | `0.6720` | 196,690.00 USD | 0.00 USD | 196,690.00 USD | 0.00 USD | 0.00 USD | 131.11 USD |
| `1D` | `0.6730` | 17,390.00 USD | 0.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD | 5.00 USD |
| `7D` | `0.6740` | 196,560.00 USD | 0.00 USD | 196,560.00 USD | 0.00 USD | 0.00 USD | 164.10 USD |
| `1D` | `0.6750` | 17,390.00 USD | 0.00 USD | 17,390.00 USD | 0.00 USD | 7,050.00 USD | 0.00 USD |
| `7D` | `0.6750` | 196,400.00 USD | 0.00 USD | 196,400.00 USD | 0.00 USD | 70,210.00 USD | 62.35 USD |
| `7D` | `0.6760` | 126,130.00 USD | 0.00 USD | 126,130.00 USD | 0.00 USD | 2,240.00 USD | 57,690.00 USD |
| `7D` | `0.6770` | 66,200.00 USD | 0.00 USD | 66,200.00 USD | 0.00 USD | 4,190.00 USD | 0.00 USD |
| `1D` | `0.6780` | 10,340.00 USD | 0.00 USD | 10,340.00 USD | 0.00 USD | 10,340.00 USD | 0.00 USD |
| `7D` | `0.6780` | 62,010.00 USD | 0.00 USD | 62,010.00 USD | 0.00 USD | 10,220.00 USD | 48,740.00 USD |
| `7D` | `0.6790` | 3,050.00 USD | 0.00 USD | 3,050.00 USD | 0.00 USD | 3,050.00 USD | 0.00 USD |
| `7D` | `0.6810` | 15,720.00 USD | 15,720.00 USD | 0.00 USD | 0.00 USD | 15,720.00 USD | 0.00 USD |
| `7D` | `0.6810` | 31,440.00 USD | 31,440.00 USD | 0.00 USD | 0.00 USD | 15,720.00 USD | 0.00 USD |
| `1D` | `0.6820` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6820` | 69,160.00 USD | 69,160.00 USD | 0.00 USD | 0.00 USD | 37,730.00 USD | 0.00 USD |
| `1D` | `0.6830` | 33,090.00 USD | 33,090.00 USD | 0.00 USD | 0.00 USD | 14,650.00 USD | 18,440.00 USD |
| `1D` | `0.6840` | 71,880.00 USD | 71,880.00 USD | 0.00 USD | 0.00 USD | 13,870.00 USD | 24,920.00 USD |
| `7D` | `0.6840` | 122,920.00 USD | 122,920.00 USD | 0.00 USD | 0.00 USD | 14,650.00 USD | 39,100.00 USD |
| `1D` | `0.6850` | 139,860.00 USD | 139,860.00 USD | 0.00 USD | 29,190.00 USD | 8,490.00 USD | 30,300.00 USD |
| `7D` | `0.6850` | 244,830.00 USD | 244,830.00 USD | 0.00 USD | 79,030.00 USD | 4,710.00 USD | 38,170.00 USD |
| `1D` | `0.6860` | 258,000.00 USD | 258,000.00 USD | 0.00 USD | 54,730.00 USD | 21,960.00 USD | 41,450.00 USD |
| `7D` | `0.6860` | 303,640.00 USD | 303,640.00 USD | 0.00 USD | 24,530.00 USD | 9,830.00 USD | 24,450.00 USD |
| `1D` | `0.6870` | 352,770.00 USD | 352,770.00 USD | 0.00 USD | 46,360.00 USD | 19,230.00 USD | 29,180.00 USD |
| `7D` | `0.6870` | 327,890.00 USD | 327,890.00 USD | 0.00 USD | 12,790.00 USD | 0.00 USD | 11,460.00 USD |
| `1D` | `0.6880` | 399,490.00 USD | 399,490.00 USD | 0.00 USD | 20,950.00 USD | 1,610.00 USD | 24,160.00 USD |
| `7D` | `0.6880` | 370,230.00 USD | 370,230.00 USD | 0.00 USD | 18,170.00 USD | 17,300.00 USD | 6,870.00 USD |
| `1D` | `0.6890` | 423,250.00 USD | 423,250.00 USD | 0.00 USD | 21,560.00 USD | 0.00 USD | 2,200.00 USD |
| `7D` | `0.6890` | 384,550.00 USD | 384,550.00 USD | 0.00 USD | 14,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6900` | 481,600.00 USD | 481,600.00 USD | 0.00 USD | 25,280.00 USD | 8,300.00 USD | 24,780.00 USD |
| `7D` | `0.6900` | 423,220.00 USD | 423,220.00 USD | 0.00 USD | 5,340.00 USD | 4,480.00 USD | 28,850.00 USD |
| `1D` | `0.6910` | 559,770.00 USD | 559,770.00 USD | 0.00 USD | 37,420.00 USD | 13,680.00 USD | 27,060.00 USD |
| `7D` | `0.6910` | 475,570.00 USD | 475,570.00 USD | 0.00 USD | 37,750.00 USD | 2,090.00 USD | 12,500.00 USD |
| `1D` | `0.6920` | 624,280.00 USD | 624,280.00 USD | 0.00 USD | 35,960.00 USD | 3,880.00 USD | 24,670.00 USD |
| `7D` | `0.6920` | 530,030.00 USD | 530,030.00 USD | 0.00 USD | 26,730.00 USD | 3,360.00 USD | 24,370.00 USD |
| `1D` | `0.6930` | 641,530.00 USD | 641,530.00 USD | 0.00 USD | 8,100.00 USD | 529.57 USD | 8,630.00 USD |
| `7D` | `0.6930` | 543,040.00 USD | 543,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,010.00 USD |
| `1D` | `0.6940` | 665,420.00 USD | 665,420.00 USD | 0.00 USD | 11,230.00 USD | 4,420.00 USD | 8,240.00 USD |
| `7D` | `0.6940` | 543,180.00 USD | 543,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 140.50 USD |
| `1D` | `0.6950` | 700,870.00 USD | 700,870.00 USD | 0.00 USD | 22,480.00 USD | 4,460.00 USD | 8,520.00 USD |
| `7D` | `0.6950` | 587,170.00 USD | 587,170.00 USD | 0.00 USD | 31,450.00 USD | 0.00 USD | 12,530.00 USD |
| `1D` | `0.6960` | 762,420.00 USD | 762,420.00 USD | 0.00 USD | 36,830.00 USD | 7,190.00 USD | 17,530.00 USD |
| `7D` | `0.6960` | 627,280.00 USD | 627,280.00 USD | 0.00 USD | 12,220.00 USD | 17,870.00 USD | 10,020.00 USD |
| `1D` | `0.6970` | 801,130.00 USD | 801,130.00 USD | 0.00 USD | 23,380.00 USD | 6,080.00 USD | 9,250.00 USD |
| `7D` | `0.6970` | 634,500.00 USD | 634,500.00 USD | 0.00 USD | 7,220.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6980` | 829,850.00 USD | 829,850.00 USD | 0.00 USD | 11,320.00 USD | 8,750.00 USD | 8,660.00 USD |
| `7D` | `0.6980` | 651,180.00 USD | 651,180.00 USD | 0.00 USD | 0.00 USD | 2,100.00 USD | 14,580.00 USD |
| `1D` | `0.6990` | 838,760.00 USD | 838,760.00 USD | 0.00 USD | 1,320.00 USD | 1,940.00 USD | 5,650.00 USD |
| `7D` | `0.6990` | 656,110.00 USD | 656,110.00 USD | 0.00 USD | 4,770.00 USD | 0.00 USD | 158.10 USD |
| `1D` | `0.7000` | 871,510.00 USD | 871,510.00 USD | 0.00 USD | 8,760.00 USD | 4,290.00 USD | 19,700.00 USD |
| `7D` | `0.7000` | 668,190.00 USD | 668,190.00 USD | 0.00 USD | 0.00 USD | 2,090.00 USD | 9,990.00 USD |
| `1D` | `0.7010` | 896,760.00 USD | 896,760.00 USD | 0.00 USD | 9,680.00 USD | 2,580.00 USD | 12,980.00 USD |
| `1D` | `0.7020` | 907,650.00 USD | 907,650.00 USD | 0.00 USD | 9,770.00 USD | 0.00 USD | 1,120.00 USD |
| `7D` | `0.7020` | 737,610.00 USD | 737,610.00 USD | 0.00 USD | 16,350.00 USD | 0.00 USD | 53,080.00 USD |
| `1D` | `0.7030` | 914,070.00 USD | 914,070.00 USD | 0.00 USD | 0.00 USD | 1,660.00 USD | 4,750.00 USD |
| `7D` | `0.7030` | 864,690.00 USD | 864,690.00 USD | 0.00 USD | 76,610.00 USD | 0.00 USD | 50,470.00 USD |
| `1D` | `0.7040` | 941,550.00 USD | 941,550.00 USD | 0.00 USD | 17,790.00 USD | 3,130.00 USD | 6,570.00 USD |
| `7D` | `0.7040` | 882,080.00 USD | 882,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,380.00 USD |
| `1D` | `0.7050` | 961,970.00 USD | 961,970.00 USD | 0.00 USD | 14,710.00 USD | 0.00 USD | 5,700.00 USD |
| `7D` | `0.7050` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 4,290.00 USD | 0.00 USD | 123,570.00 USD |
| `1D` | `0.7060` | 967,510.00 USD | 967,510.00 USD | 0.00 USD | 3,570.00 USD | 1,040.00 USD | 933.36 USD |
| `7D` | `0.7060` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 33,490.00 USD | 39,740.00 USD |
| `1D` | `0.7070` | 982,780.00 USD | 982,780.00 USD | 0.00 USD | 9,150.00 USD | 3,260.00 USD | 2,870.00 USD |
| `7D` | `0.7070` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 8,720.00 USD | 22,760.00 USD | 29,060.00 USD |
| `1D` | `0.7080` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 18,420.00 USD | 3,500.00 USD | 4,310.00 USD |
| `7D` | `0.7080` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 15,730.00 USD | 28,570.00 USD | 53,820.00 USD |
| `1D` | `0.7090` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 22,500.00 USD | 7,680.00 USD | 8,860.00 USD |
| `7D` | `0.7090` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 106,000.00 USD | 32,830.00 USD | 134,530.00 USD |
| `1D` | `0.7100` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 12,610.00 USD | 3,930.00 USD | 25,520.00 USD |
| `7D` | `0.7100` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 37,600.00 USD | 30,700.00 USD | 14,350.00 USD |
| `1D` | `0.7110` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 8,750.00 USD | 3,170.00 USD | 5,210.00 USD |
| `7D` | `0.7110` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 40,300.00 USD | 28,740.00 USD | 44,310.00 USD |
| `1D` | `0.7120` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 15,190.00 USD | 2,320.00 USD | 13,580.00 USD |
| `7D` | `0.7120` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 60,730.00 USD | 45,350.00 USD | 122,730.00 USD |
| `1D` | `0.7130` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 9,250.00 USD | 2,640.00 USD | 34,700.00 USD |
| `7D` | `0.7130` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 75,250.00 USD | 31,940.00 USD | 51,290.00 USD |
| `1D` | `0.7140` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 30,330.00 USD | 6,770.00 USD | 6,410.00 USD |
| `7D` | `0.7140` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 127,300.00 USD | 35,310.00 USD | 82,050.00 USD |
| `1D` | `0.7150` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 7,820.00 USD | 5,800.00 USD | 8,090.00 USD |
| `7D` | `0.7150` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 50,460.00 USD | 26,770.00 USD | 96,410.00 USD |
| `1D` | `0.7160` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 15,080.00 USD | 1,570.00 USD | 6,210.00 USD |
| `7D` | `0.7160` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 62,580.00 USD | 38,490.00 USD | 68,030.00 USD |
| `1D` | `0.7170` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 8,450.00 USD | 3,880.00 USD | 1,740.00 USD |
| `7D` | `0.7170` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 105,890.00 USD | 24,740.00 USD | 53,780.00 USD |
| `1D` | `0.7180` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 1,270.00 USD | 1,580.00 USD | 10,550.00 USD |
| `7D` | `0.7180` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 59,980.00 USD | 21,140.00 USD | 5,670.00 USD |
| `1D` | `0.7190` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 3,460.00 USD | 6,850.00 USD | 180.08 USD |
| `7D` | `0.7190` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 17,000.00 USD | 11,840.00 USD | 88,130.00 USD |
| `1D` | `0.7200` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 3,590.00 USD | 10,300.00 USD |
| `7D` | `0.7200` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 58,530.00 USD | 33,310.00 USD | 90,380.00 USD |
| `1D` | `0.7210` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 5,130.00 USD | 5,240.00 USD | 84.07 USD |
| `7D` | `0.7210` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 206,240.00 USD | 17,950.00 USD | 70,970.00 USD |
| `1D` | `0.7220` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 23,430.00 USD | 5,070.00 USD | 23,300.00 USD |
| `7D` | `0.7220` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 112,190.00 USD | 42,410.00 USD | 27,350.00 USD |
| `1D` | `0.7230` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 3,920.00 USD | 4,060.00 USD | 27,840.00 USD |
| `7D` | `0.7230` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 59,050.00 USD | 10,400.00 USD | 94,140.00 USD |
| `1D` | `0.7240` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 2,920.00 USD | 4,240.00 USD | 9,550.00 USD |
| `7D` | `0.7240` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 75,360.00 USD | 14,510.00 USD | 29,090.00 USD |
| `1D` | `0.7250` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 4,760.00 USD | 1,150.00 USD | 5,760.00 USD |
| `7D` | `0.7250` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 52,270.00 USD | 23,200.00 USD | 58,470.00 USD |
| `1D` | `0.7260` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 8,620.00 USD | 5,680.00 USD | 8,090.00 USD |
| `7D` | `0.7260` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 54,140.00 USD | 26,590.00 USD | 93,220.00 USD |
| `1D` | `0.7270` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 11,280.00 USD | 2,760.00 USD | 14,370.00 USD |
| `7D` | `0.7270` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 49,240.00 USD | 18,120.00 USD | 33,770.00 USD |
| `1D` | `0.7280` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 16,410.00 USD | 5,780.00 USD | 11,620.00 USD |
| `7D` | `0.7280` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 42,560.00 USD | 22,060.00 USD | 50,400.00 USD |
| `1D` | `0.7290` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 7,920.00 USD | 6,520.00 USD | 19,550.00 USD |
| `7D` | `0.7290` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 47,200.00 USD | 32,380.00 USD | 69,630.00 USD |
| `1D` | `0.7300` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 9,980.00 USD | 5,040.00 USD | 23,380.00 USD |
| `7D` | `0.7300` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 55,390.00 USD | 27,940.00 USD | 29,310.00 USD |
| `1D` | `0.7310` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 1,010.00 USD | 1,670.00 USD | 5,660.00 USD |
| `7D` | `0.7310` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 115,470.00 USD | 35,110.00 USD | 31,380.00 USD |
| `1D` | `0.7320` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 5,780.00 USD | 1,140.00 USD | 12,420.00 USD |
| `7D` | `0.7320` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 74,380.00 USD | 25,020.00 USD | 48,950.00 USD |
| `1D` | `0.7330` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 6,450.00 USD | 3,420.00 USD | 4,390.00 USD |
| `7D` | `0.7330` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 32,180.00 USD |
| `1D` | `0.7340` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 1,620.00 USD | 1,530.00 USD | 5,150.00 USD |
| `7D` | `0.7340` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 31,260.00 USD | 8,620.00 USD | 30,500.00 USD |
| `1D` | `0.7350` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 735.24 USD | 1,470.00 USD | 8.40 USD |
| `7D` | `0.7350` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 66,390.00 USD | 15,820.00 USD | 15,500.00 USD |
| `1D` | `0.7360` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 10,900.00 USD | 2,960.00 USD | 14,950.00 USD |
| `7D` | `0.7360` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 37,210.00 USD | 30,980.00 USD | 19,530.00 USD |
| `1D` | `0.7370` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 1,110.00 USD | 1,970.00 USD | 9,870.00 USD |
| `7D` | `0.7370` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 9,640.00 USD | 3,860.00 USD | 20,950.00 USD |
| `1D` | `0.7380` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 4,530.00 USD | 963.47 USD | 1,880.00 USD |
| `7D` | `0.7380` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 58,340.00 USD | 13,660.00 USD | 39,670.00 USD |
| `1D` | `0.7390` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 1,180.00 USD | 1,200.00 USD |
| `7D` | `0.7390` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 0.00 USD | 8,110.00 USD | 25,560.00 USD |
| `1D` | `0.7400` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 2,880.00 USD | 2,520.00 USD | 3,020.00 USD |
| `7D` | `0.7400` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 1,730.00 USD | 6,500.00 USD | 11,420.00 USD |
| `1D` | `0.7410` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 1,490.00 USD | 1,030.00 USD | 4,740.00 USD |
| `7D` | `0.7410` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 28,380.00 USD | 30,100.00 USD | 31,130.00 USD |
| `1D` | `0.7420` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11.18 USD |
| `7D` | `0.7420` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 7,430.00 USD | 13,420.00 USD | 382.20 USD |
| `1D` | `0.7430` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 1,240.00 USD | 0.00 USD | 5.00 USD |
| `7D` | `0.7430` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 46,330.00 USD | 13,970.00 USD | 54,780.00 USD |
| `1D` | `0.7440` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 682.77 USD | 718.40 USD | 5,090.00 USD |
| `7D` | `0.7440` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 28,120.00 USD | 25,920.00 USD | 15,640.00 USD |
| `1D` | `0.7450` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 3,670.00 USD | 1,170.00 USD | 6,030.00 USD |
| `7D` | `0.7450` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 42,580.00 USD | 16,360.00 USD | 32,440.00 USD |
| `1D` | `0.7460` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 4,520.00 USD | 1,370.00 USD | 6,190.00 USD |
| `7D` | `0.7460` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 38,650.00 USD | 10,350.00 USD | 13,170.00 USD |
| `1D` | `0.7470` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 2,490.00 USD | 0.00 USD | 4,680.00 USD |
| `7D` | `0.7470` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 35,630.00 USD | 18,610.00 USD | 28,070.00 USD |
| `1D` | `0.7480` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 5,750.00 USD | 1,230.00 USD | 8,310.00 USD |
| `7D` | `0.7480` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 24,950.00 USD | 10,290.00 USD | 4,350.00 USD |
| `1D` | `0.7490` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 5,110.00 USD | 798.62 USD | 3,170.00 USD |
| `7D` | `0.7490` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 17,270.00 USD | 5,180.00 USD | 8,850.00 USD |
| `1D` | `0.7500` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 5,860.00 USD | 407.44 USD | 4,520.00 USD |
| `7D` | `0.7500` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 35,050.00 USD | 7,430.00 USD | 16,180.00 USD |
| `1D` | `0.7510` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 3,750.00 USD | 0.00 USD | 1,480.00 USD |
| `7D` | `0.7510` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 23,010.00 USD | 5,870.00 USD | 35,790.00 USD |
| `1D` | `0.7520` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 1,460.00 USD | 1,690.00 USD | 555.19 USD |
| `7D` | `0.7520` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 27,570.00 USD | 7,130.00 USD | 15,790.00 USD |
| `7D` | `0.7530` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 21,290.00 USD | 1,890.00 USD | 14,310.00 USD |
| `1D` | `0.7540` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 1,000.00 USD | 2,530.00 USD |
| `7D` | `0.7540` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 9,060.00 USD | 0.00 USD | 5,640.00 USD |
| `7D` | `0.7550` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 18,390.00 USD | 6,470.00 USD | 19,600.00 USD |
| `7D` | `0.7560` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 7,600.00 USD | 1,100.00 USD | 2,590.00 USD |
| `7D` | `0.7570` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 29,140.00 USD | 4,260.00 USD | 96.75 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `98.50M` | Total OI Tokens: `144,948,827.9 APT`
  * 1h OI Change: `-0.50%` | 4h OI Change: `+1.78%` | 24h OI Change: `-2.59%`
  * Exchange Breakdown: Binance=`19.33M` | Bybit=`20.15M` | OKX=`4.77M` | Hyperliquid=`3.73M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.51K` | Last 24h: `7.04K` | Last 3d: `8.52K` | Last 7d: `3.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0094%` | **USDT OKX** | `0.0067%` |
| **USDT Bybit** | `0.0016%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0094%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0038%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `APT` | `40.57%` | `59.43%` | `0.68` | 3,650,000.00 USD |
| `15M` | `Binance` | `48.28%` | `51.72%` | `0.93` | 1,150,000.00 USD |
| `15M` | `OKX` | `59.25%` | `40.75%` | `1.45` | 174,680.00 USD |
| `15M` | `Bybit` | `43.36%` | `56.64%` | `0.77` | 93,100.00 USD |
| `15M` | `KuCoin` | `50.58%` | `49.42%` | `1.02` | 16,350.00 USD |
| `15M` | `Gate` | `48%` | `52%` | `0.92` | 33,910.00 USD |
| `15M` | `Bitget` | `50.61%` | `49.39%` | `1.02` | 76,240.00 USD |
| `15M` | `BingX` | `38.79%` | `61.21%` | `0.63` | 848,590.00 USD |
| `15M` | `MEXC` | `41.2%` | `58.8%` | `0.70` | 148,240.00 USD |
| `15M` | `Bitunix` | `46.16%` | `53.84%` | `0.86` | 53,320.00 USD |
| `15M` | `Hyperliquid` | `23.03%` | `76.97%` | `0.30` | 121,100.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.93%` | `51.07%` | `0.96` | 555,850.00 USD |
| `15M` | `Crypto.com` | `100%` | `0%` | `1.00` | 0.88 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 371,170.00 USD |
| `15M` | `HTX` | `42.86%` | `57.14%` | `0.75` | 740.61 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `85.8%` | `14.2%` | `6.04` | 1,380.00 USD |
| `15M` | `Aster` | `99.08%` | `0.92%` | `107.70` | 1,910.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `26.45%` | `73.55%` | `0.36` | 5,250.00 USD |
| `15M` | `Whale Positions` | `48.28%` | `51.72%` | `0.93` | 1,150,000.00 USD |
| `15M` | `Global Accounts` | `40.57%` | `59.43%` | `0.68` | 3,650,000.00 USD |
| `1H` | `APT` | `52.22%` | `47.78%` | `1.09` | 27,110,000.00 USD |
| `1H` | `Binance` | `54.92%` | `45.08%` | `1.22` | 11,420,000.00 USD |
| `1H` | `OKX` | `52.55%` | `47.45%` | `1.11` | 4,000,000.00 USD |
| `1H` | `Bybit` | `48.79%` | `51.21%` | `0.95` | 2,870,000.00 USD |
| `1H` | `KuCoin` | `55.08%` | `44.92%` | `1.23` | 367,350.00 USD |
| `1H` | `Gate` | `44.89%` | `55.11%` | `0.81` | 862,720.00 USD |
| `1H` | `Bitget` | `48.81%` | `51.19%` | `0.95` | 889,080.00 USD |
| `1H` | `BingX` | `47.45%` | `52.55%` | `0.90` | 1,460,000.00 USD |
| `1H` | `MEXC` | `55.56%` | `44.44%` | `1.25` | 2,370,000.00 USD |
| `1H` | `Bitunix` | `54.21%` | `45.79%` | `1.18` | 756,140.00 USD |
| `1H` | `Hyperliquid` | `43.52%` | `56.48%` | `0.77` | 412,500.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `40.75%` | `59.25%` | `0.69` | 298,540.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `44.75%` | `55.25%` | `0.81` | 1,100,000.00 USD |
| `1H` | `HTX` | `44.37%` | `55.63%` | `0.80` | 29,020.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `47.46%` | `52.54%` | `0.90` | 176,060.00 USD |
| `1H` | `Aster` | `51.57%` | `48.43%` | `1.06` | 81,190.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50.83%` | `49.17%` | `1.03` | 20,660.00 USD |
| `1H` | `Whale Positions` | `54.92%` | `45.08%` | `1.22` | 11,420,000.00 USD |
| `1H` | `Global Accounts` | `52.22%` | `47.78%` | `1.09` | 27,110,000.00 USD |
| `4H` | `APT` | `45.62%` | `54.38%` | `0.84` | 28,010,000.00 USD |
| `4H` | `Binance` | `49.99%` | `50.01%` | `1.00` | 9,160,000.00 USD |
| `4H` | `OKX` | `44.81%` | `55.19%` | `0.81` | 3,370,000.00 USD |
| `4H` | `Bybit` | `44.44%` | `55.56%` | `0.80` | 1,560,000.00 USD |
| `4H` | `KuCoin` | `50.56%` | `49.44%` | `1.02` | 2,100,000.00 USD |
| `4H` | `Gate` | `47.95%` | `52.05%` | `0.92` | 718,920.00 USD |
| `4H` | `Bitget` | `46.24%` | `53.76%` | `0.86` | 615,950.00 USD |
| `4H` | `BingX` | `30.24%` | `69.76%` | `0.43` | 3,810,000.00 USD |
| `4H` | `MEXC` | `48.59%` | `51.41%` | `0.95` | 1,380,000.00 USD |
| `4H` | `Bitunix` | `49.23%` | `50.77%` | `0.97` | 724,230.00 USD |
| `4H` | `Hyperliquid` | `33.86%` | `66.14%` | `0.51` | 207,640.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.04%` | `49.96%` | `1.00` | 3,140,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `30.81%` | `69.19%` | `0.45` | 827,870.00 USD |
| `4H` | `HTX` | `61.08%` | `38.92%` | `1.57` | 13,160.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `52.51%` | `47.49%` | `1.11` | 310,530.00 USD |
| `4H` | `Aster` | `81.91%` | `18.09%` | `4.53` | 75,970.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `49.99%` | `50.01%` | `1.00` | 9,160,000.00 USD |
| `4H` | `Global Accounts` | `45.62%` | `54.38%` | `0.84` | 28,010,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.6713` | `0.6721` | `0.6713` | `0.6739` | `0.6704` | 176,908.60 USD | 85,172.02 USD | 91,736.58 USD | -6,564.56 USD | `-3.71%` | `4B / 10S` |
| `0:00 UTC` | `0.6685` | `0.6690` | `0.6685` | `0.6719` | `0.6676` | 334,090.04 USD | 140,959.11 USD | 193,130.93 USD | -52,171.82 USD | `-15.62%` | `7B / 11S` |
| `5:00 UTC` | `0.6692` | `0.6700` | `0.6692` | `0.6727` | `0.6684` | 278,832.17 USD | 158,405.05 USD | 120,427.12 USD | 37,977.93 USD | `+13.62%` | `12B / 4S` |
| `0:00 UTC` | `0.6787` | `0.6761` | `0.6787` | `0.6802` | `0.6712` | 746,760.99 USD | 451,682.53 USD | 295,078.46 USD | 156,604.07 USD | `+20.97%` | `25B / 4S` |
| `5:00 UTC` | `0.6761` | `0.6772` | `0.6761` | `0.6794` | `0.6750` | 345,957.15 USD | 137,629.01 USD | 208,328.14 USD | -70,699.13 USD | `-20.44%` | `11B / 15S` |
| `0:00 UTC` | `0.6826` | `0.6817` | `0.6826` | `0.6832` | `0.6774` | 689,683.95 USD | 288,086.52 USD | 401,597.43 USD | -113,510.91 USD | `-16.46%` | `6B / 10S` |
| `5:00 UTC` | `0.6811` | `0.6809` | `0.6811` | `0.6841` | `0.6784` | 348,817.67 USD | 197,256.69 USD | 151,560.98 USD | 45,695.71 USD | `+13.10%` | `18B / 7S` |
| `0:00 UTC` | `0.6777` | `0.6782` | `0.6777` | `0.6811` | `0.6757` | 498,585.09 USD | 273,063.96 USD | 225,521.13 USD | 47,542.83 USD | `+9.54%` | `12B / 6S` |
| `5:00 UTC` | `0.6832` | `0.6818` | `0.6832` | `0.6845` | `0.6784` | 502,488.77 USD | 285,377.95 USD | 217,110.82 USD | 68,267.13 USD | `+13.59%` | `13B / 6S` |
| `0:00 UTC` | `0.6801` | `0.6812` | `0.6801` | `0.6832` | `0.6785` | 464,416.15 USD | 219,480.65 USD | 244,935.49 USD | -25,454.84 USD | `-5.48%` | `6B / 10S` |

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
| `5m` | -5,570.00 USD | -46,090.00 USD | **`DISTRIBUTION`** |
| `15m` | 57,720.00 USD | -77,520.00 USD | **`DISTRIBUTION`** |
| `30m` | 47,920.00 USD | -20,720.00 USD | **`ACCUMULATION`** |
| `1h` | 140,460.00 USD | 58,170.00 USD | **`ACCUMULATION`** |
| `2h` | 35,430.00 USD | 27.77 USD | **`ACCUMULATION`** |
| `4h` | 83,800.00 USD | -533,330.00 USD | **`DISTRIBUTION`** |
| `6h` | 68,190.00 USD | -171,500.00 USD | **`DISTRIBUTION`** |
| `8h` | -78,450.00 USD | -1,100,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -428,010.00 USD | -1,650,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -915,210.00 USD | -4,250,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,470,000.00 USD | -18,320,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,870,000.00 USD | -101,530,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-5.57K` | 15m=`+57.72K` | 1h=`+140.46K` | 24h=`-915.21K`
* Futures Capital Netflows: 5m=`-46.09K` | 15m=`-77.52K` | 1h=`+58.17K` | 24h=`-4.25M`
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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
