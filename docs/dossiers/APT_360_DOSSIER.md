# 🏛️ SOVEREIGN CANDIDATE DOSSIER: APT
**Canonical Key**: `APT` | **Broker Instrument**: `APTUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 23:13:20 IST` (`2026-10-29 17:43:20 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.6900` | `0.6906` | `0.6874` | `0.6874` | `373,739` | 257,509.58 USD | -155,385.79 USD | `-60.34%` | -3,161,920.39 USD | `-1.31` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.6874` | `0.6885` | `0.6862` | `0.6873` | `247,362` | 170,049.65 USD | -57,518.45 USD | `-33.82%` | -3,219,438.85 USD | `-0.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.6873` | `0.6890` | `0.6870` | `0.6881` | `169,274` | 116,507.26 USD | 39,389.26 USD | `+33.81%` | -3,180,049.59 USD | `+0.75` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.6927` | `0.6936` | `0.6912` | `0.6926` | `797,540` | 552,207.56 USD | -73,240.12 USD | `-13.26%` | -2,859,735.44 USD | `-0.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.6926` | `0.6945` | `0.6874` | `0.6874` | `1,170,068` | 808,356.30 USD | -254,225.03 USD | `-31.45%` | -3,113,960.47 USD | `-1.65` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.6874` | `0.6890` | `0.6862` | `0.6881` | `416,627` | 286,550.65 USD | -18,135.46 USD | `-6.33%` | -3,132,095.93 USD | `+0.22` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.6868` | `0.7047` | `0.6852` | `0.7036` | `3,879,858` | 2,697,535.23 USD | 26,927.71 USD | `+1.00%` | -2,408,403.96 USD | `+0.64` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.7037` | `0.7077` | `0.6911` | `0.6926` | `5,801,752` | 4,049,481.14 USD | -506,091.42 USD | `-12.50%` | -2,914,495.37 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.6926` | `0.6945` | `0.6862` | `0.6881` | `1,586,695` | 1,094,906.95 USD | -272,360.49 USD | `-24.88%` | -3,186,855.86 USD | `-0.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.6561` | `0.6774` | `0.6549` | `0.6712` | `7,448,343` | 4,965,296.85 USD | -60,141.40 USD | `-1.21%` | -2,083,618.45 USD | `+1.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -2,231,705.21 USD | `+0.80` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6862` | `0.6879` | `7,387,185` | 5,143,520.10 USD | -778,453.69 USD | `-15.13%` | -3,010,158.90 USD | `-0.77` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.7002` | `0.7012` | `0.6555` | `0.6611` | `16,465,880` | 11,061,810.70 USD | -1,103,761.29 USD | `-9.98%` | -1,656,578.37 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6611` | `0.6759` | `0.6485` | `0.6561` | `10,656,422` | 7,044,804.33 USD | -366,898.68 USD | `-5.21%` | -2,023,477.05 USD | `+0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6561` | `0.6774` | `0.6549` | `0.6712` | `7,448,343` | 4,965,296.85 USD | -60,141.40 USD | `-1.21%` | -2,083,618.45 USD | `+1.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -2,231,705.21 USD | `+0.80` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6862` | `0.6879` | `7,387,185` | 5,143,520.10 USD | -778,453.69 USD | `-15.13%` | -3,010,158.90 USD | `-0.77` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:06:38 IST` |

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
| `7D` | `Long Liquidation` | `0.5870` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 1,400.00 USD | 65.70 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5880` | 2,820,000.00 USD | 2,820,000.00 USD | 3,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5885` | 440.16 USD | 48,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5890` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 15.37 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5895` | 1,690.00 USD | 48,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5900` | 2,820,000.00 USD | 2,820,000.00 USD | 3,120.00 USD | 1,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5920` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 2,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5925` | 609.14 USD | 46,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5930` | 2,810,000.00 USD | 2,810,000.00 USD | 10,090.00 USD | 0.00 USD | 9,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5935` | 572.40 USD | 46,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5945` | 3,850.00 USD | 45,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5950` | 2,790,000.00 USD | 2,790,000.00 USD | 5,120.00 USD | 0.00 USD | 4,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5960` | 2,780,000.00 USD | 2,780,000.00 USD | 5,120.00 USD | 1,640.00 USD | 46.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5970` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5975` | 157.22 USD | 41,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5980` | 2,760,000.00 USD | 2,760,000.00 USD | 7,660.00 USD | 826.53 USD | 3.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5990` | 2,760,000.00 USD | 2,760,000.00 USD | 3,320.00 USD | 1,340.00 USD | 14,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6000` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 796.28 USD | 4,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6005` | 852.06 USD | 41,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.6020` | 2,730,000.00 USD | 2,730,000.00 USD | 10,590.00 USD | 8,040.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6025` | 451.19 USD | 40,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.6030` | 2,710,000.00 USD | 2,710,000.00 USD | 2,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6040` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6045` | 527.44 USD | 40,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.6060` | 2,700,000.00 USD | 2,700,000.00 USD | 2,850.00 USD | 0.00 USD | 32.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6070` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 32.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6080` | 2,700,000.00 USD | 2,700,000.00 USD | 2,860.00 USD | 0.00 USD | 124.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6090` | 2,690,000.00 USD | 2,690,000.00 USD | 6,360.00 USD | 0.00 USD | 3,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6100` | 2,680,000.00 USD | 2,680,000.00 USD | 7,480.00 USD | 2,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6105` | 126.47 USD | 39,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.6110` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 2,210.00 USD | 6,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6120` | 2,660,000.00 USD | 2,660,000.00 USD | 2,100.00 USD | 3,510.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6130` | 2,650,000.00 USD | 2,650,000.00 USD | 8,870.00 USD | 1,050.00 USD | 4,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6140` | 2,640,000.00 USD | 2,640,000.00 USD | 4,540.00 USD | 7,000.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6150` | 2,620,000.00 USD | 2,620,000.00 USD | 11,130.00 USD | 5,870.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6160` | 2,300,000.00 USD | 2,300,000.00 USD | 4,180.00 USD | 1,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6160` | 2,600,000.00 USD | 2,600,000.00 USD | 1,790.00 USD | 2,510.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6170` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6170` | 2,590,000.00 USD | 2,590,000.00 USD | 13,260.00 USD | 2,610.00 USD | 9,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6180` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 678.61 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6180` | 2,560,000.00 USD | 2,560,000.00 USD | 7,600.00 USD | 1,190.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6190` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 126.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6190` | 2,550,000.00 USD | 2,550,000.00 USD | 9,560.00 USD | 1,930.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6195` | 3,170.00 USD | 39,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6200` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6200` | 2,530,000.00 USD | 2,530,000.00 USD | 13,870.00 USD | 5,230.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6210` | 2,290,000.00 USD | 2,290,000.00 USD | 1,990.00 USD | 0.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6210` | 2,500,000.00 USD | 2,500,000.00 USD | 4,760.00 USD | 1,860.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6220` | 2,290,000.00 USD | 2,290,000.00 USD | 2,520.00 USD | 0.00 USD | 7.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6220` | 2,490,000.00 USD | 2,490,000.00 USD | 7,960.00 USD | 2,310.00 USD | 29,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6230` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6230` | 2,450,000.00 USD | 2,450,000.00 USD | 9,770.00 USD | 4,700.00 USD | 8,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6235` | 3,250.00 USD | 36,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6240` | 2,280,000.00 USD | 2,280,000.00 USD | 4,840.00 USD | 4,260.00 USD | 76.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6240` | 2,430,000.00 USD | 2,430,000.00 USD | 18,610.00 USD | 4,720.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6245` | 1,960.00 USD | 33,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6250` | 2,270,000.00 USD | 2,270,000.00 USD | 1,800.00 USD | 2,630.00 USD | 85.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6250` | 2,400,000.00 USD | 2,400,000.00 USD | 16,120.00 USD | 3,830.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6255` | 286.65 USD | 31,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6260` | 2,270,000.00 USD | 2,270,000.00 USD | 10,030.00 USD | 1,310.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6260` | 2,380,000.00 USD | 2,380,000.00 USD | 20,890.00 USD | 7,660.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6265` | 10,530.00 USD | 30,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6270` | 2,250,000.00 USD | 2,250,000.00 USD | 3,700.00 USD | 3,940.00 USD | 12,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6270` | 2,320,000.00 USD | 2,320,000.00 USD | 17,460.00 USD | 8,200.00 USD | 24,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6280` | 2,230,000.00 USD | 2,230,000.00 USD | 11,690.00 USD | 463.43 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6280` | 2,270,000.00 USD | 2,270,000.00 USD | 9,160.00 USD | 9,230.00 USD | 16,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6285` | 903.47 USD | 20,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6290` | 2,210,000.00 USD | 2,210,000.00 USD | 11,890.00 USD | 1,200.00 USD | 5,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6290` | 2,240,000.00 USD | 2,240,000.00 USD | 17,710.00 USD | 6,740.00 USD | 10,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6300` | 2,190,000.00 USD | 2,190,000.00 USD | 12,950.00 USD | 2,470.00 USD | 2,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6300` | 2,200,000.00 USD | 2,200,000.00 USD | 10,040.00 USD | 7,890.00 USD | 11,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6310` | 2,180,000.00 USD | 2,180,000.00 USD | 7,940.00 USD | 5,110.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6310` | 2,170,000.00 USD | 2,170,000.00 USD | 19,340.00 USD | 4,520.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6315` | 1,010.00 USD | 19,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6320` | 2,160,000.00 USD | 2,160,000.00 USD | 12,320.00 USD | 11,080.00 USD | 14,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6320` | 2,130,000.00 USD | 2,130,000.00 USD | 4,880.00 USD | 12,650.00 USD | 8,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6330` | 2,120,000.00 USD | 2,120,000.00 USD | 17,300.00 USD | 3,580.00 USD | 21,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6330` | 2,110,000.00 USD | 2,110,000.00 USD | 57,940.00 USD | 14,700.00 USD | 33,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6340` | 2,080,000.00 USD | 2,080,000.00 USD | 9,830.00 USD | 2,020.00 USD | 15,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6340` | 2,000,000.00 USD | 2,000,000.00 USD | 10,730.00 USD | 3,420.00 USD | 4,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6350` | 2,050,000.00 USD | 2,050,000.00 USD | 19,180.00 USD | 8,820.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6350` | 1,980,000.00 USD | 1,980,000.00 USD | 14,450.00 USD | 2,430.00 USD | 22,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6360` | 2,020,000.00 USD | 2,020,000.00 USD | 30,350.00 USD | 9,150.00 USD | 33,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6360` | 1,940,000.00 USD | 1,940,000.00 USD | 42,690.00 USD | 7,300.00 USD | 40,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6370` | 1,950,000.00 USD | 1,950,000.00 USD | 21,750.00 USD | 4,510.00 USD | 27,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6370` | 1,850,000.00 USD | 1,850,000.00 USD | 49,080.00 USD | 4,870.00 USD | 29.01 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6375` | 5,900.00 USD | 18,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6380` | 1,890,000.00 USD | 1,890,000.00 USD | 19,430.00 USD | 7,180.00 USD | 7,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6380` | 1,800,000.00 USD | 1,800,000.00 USD | 18,140.00 USD | 3,870.00 USD | 30,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6390` | 1,860,000.00 USD | 1,860,000.00 USD | 18,790.00 USD | 529.57 USD | 6,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6390` | 1,740,000.00 USD | 1,740,000.00 USD | 10,200.00 USD | 7,510.00 USD | 13,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6400` | 1,830,000.00 USD | 1,830,000.00 USD | 9,830.00 USD | 9,970.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6400` | 1,710,000.00 USD | 1,710,000.00 USD | 15,560.00 USD | 0.00 USD | 330.78 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6410` | 1,790,000.00 USD | 1,790,000.00 USD | 20,930.00 USD | 2,240.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6410` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 6,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6415` | 4,740.00 USD | 12,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6420` | 1,760,000.00 USD | 1,760,000.00 USD | 32,540.00 USD | 7,850.00 USD | 12,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6420` | 1,690,000.00 USD | 1,690,000.00 USD | 39,060.00 USD | 26,560.00 USD | 10,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6430` | 1,710,000.00 USD | 1,710,000.00 USD | 25,620.00 USD | 7,460.00 USD | 9,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6430` | 1,620,000.00 USD | 1,620,000.00 USD | 16,200.00 USD | 3,970.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6435` | 2,320.00 USD | 7,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6440` | 1,660,000.00 USD | 1,660,000.00 USD | 21,790.00 USD | 11,330.00 USD | 8,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6440` | 1,590,000.00 USD | 1,590,000.00 USD | 14,160.00 USD | 6,720.00 USD | 14,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6450` | 1,620,000.00 USD | 1,620,000.00 USD | 23,100.00 USD | 20,050.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6450` | 1,560,000.00 USD | 1,560,000.00 USD | 14,120.00 USD | 15,560.00 USD | 383.87 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6455` | 3,730.00 USD | 5,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6460` | 1,550,000.00 USD | 1,550,000.00 USD | 43,360.00 USD | 10,480.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6460` | 1,530,000.00 USD | 1,530,000.00 USD | 75,060.00 USD | 14,300.00 USD | 75,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6470` | 1,440,000.00 USD | 1,440,000.00 USD | 30,630.00 USD | 6,620.00 USD | 41,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6470` | 1,360,000.00 USD | 1,360,000.00 USD | 9,660.00 USD | 3,880.00 USD | 9,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6480` | 1,360,000.00 USD | 1,360,000.00 USD | 48,130.00 USD | 14,180.00 USD | 7,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6480` | 1,340,000.00 USD | 1,340,000.00 USD | 37,050.00 USD | 0.00 USD | 23,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6485` | 259.68 USD | 1,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6490` | 1,290,000.00 USD | 1,290,000.00 USD | 28,650.00 USD | 3,800.00 USD | 40,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6490` | 1,280,000.00 USD | 1,280,000.00 USD | 36,340.00 USD | 0.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6500` | 1,220,000.00 USD | 1,220,000.00 USD | 43,350.00 USD | 1,390.00 USD | 32,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6500` | 1,220,000.00 USD | 1,220,000.00 USD | 18,310.00 USD | 0.00 USD | 67,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6505` | 580.53 USD | 1,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6510` | 1,140,000.00 USD | 1,140,000.00 USD | 18,580.00 USD | 4,450.00 USD | 63,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6510` | 1,140,000.00 USD | 1,140,000.00 USD | 101,440.00 USD | 4,190.00 USD | 288.03 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6520` | 1,060,000.00 USD | 1,060,000.00 USD | 31,260.00 USD | 6,190.00 USD | 18,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6520` | 1,030,000.00 USD | 1,030,000.00 USD | 39,510.00 USD | 6,720.00 USD | 71,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6530` | 1,000,000.00 USD | 1,000,000.00 USD | 5,780.00 USD | 1,060.00 USD | 11,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6530` | 914,850.00 USD | 914,850.00 USD | 0.00 USD | 0.00 USD | 47,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6540` | 982,890.00 USD | 982,890.00 USD | 11,450.00 USD | 2,530.00 USD | 15,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6540` | 867,750.00 USD | 867,750.00 USD | 15,730.00 USD | 0.00 USD | 14,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6550` | 953,600.00 USD | 953,600.00 USD | 18,980.00 USD | 4,080.00 USD | 15,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6550` | 837,380.00 USD | 837,380.00 USD | 0.00 USD | 0.00 USD | 38,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6560` | 914,570.00 USD | 914,570.00 USD | 23,680.00 USD | 3,800.00 USD | 25,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6560` | 798,950.00 USD | 798,950.00 USD | 7,220.00 USD | 5,380.00 USD | 34,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6570` | 862,010.00 USD | 862,010.00 USD | 5,570.00 USD | 1,820.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6570` | 751,620.00 USD | 751,620.00 USD | 14,440.00 USD | 0.00 USD | 10,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6580` | 834,830.00 USD | 834,830.00 USD | 5,880.00 USD | 0.00 USD | 30.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6580` | 726,530.00 USD | 726,530.00 USD | 0.00 USD | 0.00 USD | 173.50 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6590` | 828,920.00 USD | 828,920.00 USD | 0.00 USD | 4,430.00 USD | 14,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6590` | 726,360.00 USD | 726,360.00 USD | 9,540.00 USD | 0.00 USD | 331.05 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6600` | 810,090.00 USD | 810,090.00 USD | 19,830.00 USD | 2,840.00 USD | 22,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6600` | 716,480.00 USD | 716,480.00 USD | 0.00 USD | 4,180.00 USD | 20,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6610` | 764,810.00 USD | 764,810.00 USD | 11,920.00 USD | 2,560.00 USD | 12,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6620` | 738,160.00 USD | 738,160.00 USD | 14,030.00 USD | 2,480.00 USD | 16,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6620` | 692,070.00 USD | 692,070.00 USD | 14,320.00 USD | 0.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6630` | 705,650.00 USD | 705,650.00 USD | 24,070.00 USD | 4,110.00 USD | 1,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6630` | 670,620.00 USD | 670,620.00 USD | 11,670.00 USD | 0.00 USD | 254.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6640` | 675,610.00 USD | 675,610.00 USD | 22,290.00 USD | 1,150.00 USD | 21,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6640` | 658,690.00 USD | 658,690.00 USD | 15,140.00 USD | 0.00 USD | 279.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6650` | 630,770.00 USD | 630,770.00 USD | 12,560.00 USD | 10,330.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6650` | 643,280.00 USD | 643,280.00 USD | 0.00 USD | 6,770.00 USD | 288.69 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6660` | 593,590.00 USD | 593,590.00 USD | 7,730.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6660` | 636,220.00 USD | 636,220.00 USD | 0.00 USD | 0.00 USD | 148.18 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6670` | 580,450.00 USD | 580,450.00 USD | 18,850.00 USD | 2,980.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6670` | 636,070.00 USD | 636,070.00 USD | 31,450.00 USD | 0.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6680` | 553,690.00 USD | 553,690.00 USD | 30,610.00 USD | 3,380.00 USD | 7,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6680` | 595,840.00 USD | 595,840.00 USD | 24,780.00 USD | 7,780.00 USD | 193.34 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6690` | 512,390.00 USD | 512,390.00 USD | 13,000.00 USD | 2,800.00 USD | 3,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6690` | 563,090.00 USD | 563,090.00 USD | 14,440.00 USD | 2,330.00 USD | 24,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6695` | 818.97 USD | 818.97 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6700` | 492,960.00 USD | 492,960.00 USD | 3,250.00 USD | 1,050.00 USD | 4,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6700` | 521,890.00 USD | 521,890.00 USD | 0.00 USD | 0.00 USD | 323.96 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6710` | 484,470.00 USD | 484,470.00 USD | 8,650.00 USD | 18,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6710` | 521,560.00 USD | 521,560.00 USD | 0.00 USD | 6,960.00 USD | 55.88 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6720` | 457,720.00 USD | 457,720.00 USD | 0.00 USD | 1,080.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6730` | 450,480.00 USD | 450,480.00 USD | 5,220.00 USD | 2,020.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6730` | 514,550.00 USD | 514,550.00 USD | 0.00 USD | 0.00 USD | 99.42 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6740` | 435,630.00 USD | 435,630.00 USD | 16,360.00 USD | 4,800.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6750` | 412,160.00 USD | 412,160.00 USD | 0.00 USD | 5,970.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6750` | 514,450.00 USD | 514,450.00 USD | 0.00 USD | 75,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6760` | 396,390.00 USD | 396,390.00 USD | 9,950.00 USD | 2,630.00 USD | 8,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6760` | 438,730.00 USD | 438,730.00 USD | 0.00 USD | 2,240.00 USD | 71,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6770` | 375,270.00 USD | 375,270.00 USD | 18,650.00 USD | 2,660.00 USD | 3,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6770` | 364,780.00 USD | 364,780.00 USD | 23,340.00 USD | 4,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6780` | 350,360.00 USD | 350,360.00 USD | 0.00 USD | 12,640.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6780` | 337,250.00 USD | 337,250.00 USD | 13,090.00 USD | 10,220.00 USD | 48,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6790` | 328,950.00 USD | 328,950.00 USD | 10,840.00 USD | 18,610.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6790` | 265,210.00 USD | 265,210.00 USD | 0.00 USD | 16,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6810` | 248,620.00 USD | 248,620.00 USD | 0.00 USD | 15,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6820` | 285,300.00 USD | 285,300.00 USD | 0.00 USD | 0.00 USD | 4,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6820` | 232,900.00 USD | 232,900.00 USD | 0.00 USD | 37,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6830` | 280,380.00 USD | 280,380.00 USD | 0.00 USD | 20,240.00 USD | 25,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6830` | 195,170.00 USD | 195,170.00 USD | 0.00 USD | 4,670.00 USD | 48,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6840` | 234,450.00 USD | 234,450.00 USD | 6,510.00 USD | 15,960.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6840` | 142,250.00 USD | 142,250.00 USD | 0.00 USD | 14,650.00 USD | 39,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6850` | 203,600.00 USD | 203,600.00 USD | 46,480.00 USD | 0.00 USD | 27.82 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6850` | 88,500.00 USD | 88,500.00 USD | 0.00 USD | 4,710.00 USD | 38,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6860` | 157,090.00 USD | 157,090.00 USD | 54,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6860` | 45,610.00 USD | 45,610.00 USD | 0.00 USD | 9,830.00 USD | 24,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6870` | 102,360.00 USD | 102,360.00 USD | 56,810.00 USD | 1,170.00 USD | 44,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6870` | 11,330.00 USD | 11,330.00 USD | 0.00 USD | 0.00 USD | 11,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6880` | 38,390.00 USD | 38,390.00 USD | 0.00 USD | 9,600.00 USD | 28,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6880` | 76,770.00 USD | 76,770.00 USD | 0.00 USD | 9,600.00 USD | 28,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6880` | 35,470.00 USD | 35,470.00 USD | 18,170.00 USD | 17,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6880` | 70,940.00 USD | 70,940.00 USD | 18,170.00 USD | 17,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6890` | 79,520.00 USD | 79,520.00 USD | 0.00 USD | 0.00 USD | 2,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6890` | 81,970.00 USD | 81,970.00 USD | 0.00 USD | 11,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6900` | 79,580.00 USD | 79,580.00 USD | 0.00 USD | 0.00 USD | 56.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6900` | 86,450.00 USD | 86,450.00 USD | 0.00 USD | 4,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6910` | 106,640.00 USD | 106,640.00 USD | 0.00 USD | 0.00 USD | 27,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6910` | 88,670.00 USD | 88,670.00 USD | 0.00 USD | 2,090.00 USD | 131.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6920` | 106,670.00 USD | 106,670.00 USD | 0.00 USD | 0.00 USD | 26.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6920` | 113,040.00 USD | 113,040.00 USD | 0.00 USD | 0.00 USD | 24,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6930` | 106,840.00 USD | 106,840.00 USD | 0.00 USD | 0.00 USD | 168.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6930` | 126,200.00 USD | 126,200.00 USD | 0.00 USD | 0.00 USD | 13,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6940` | 130,720.00 USD | 130,720.00 USD | 11,230.00 USD | 4,420.00 USD | 8,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6950` | 157,660.00 USD | 157,660.00 USD | 22,480.00 USD | 4,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6950` | 170,040.00 USD | 170,040.00 USD | 31,450.00 USD | 0.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6960` | 204,730.00 USD | 204,730.00 USD | 47,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6960` | 182,260.00 USD | 182,260.00 USD | 12,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6970` | 228,140.00 USD | 228,140.00 USD | 23,380.00 USD | 0.00 USD | 34.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6970` | 203,910.00 USD | 203,910.00 USD | 21,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6980` | 228,160.00 USD | 228,160.00 USD | 0.00 USD | 0.00 USD | 17.79 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6990` | 230,140.00 USD | 230,140.00 USD | 0.00 USD | 1,940.00 USD | 38.35 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6990` | 208,680.00 USD | 208,680.00 USD | 4,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7000` | 218,670.00 USD | 218,670.00 USD | 0.00 USD | 0.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7010` | 230,190.00 USD | 230,190.00 USD | 0.00 USD | 0.00 USD | 42.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7020` | 240,430.00 USD | 240,430.00 USD | 10,220.00 USD | 0.00 USD | 22.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7020` | 288,100.00 USD | 288,100.00 USD | 16,350.00 USD | 0.00 USD | 53,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7030` | 240,450.00 USD | 240,450.00 USD | 0.00 USD | 0.00 USD | 15.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7030` | 415,180.00 USD | 415,180.00 USD | 76,610.00 USD | 0.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7040` | 278,410.00 USD | 278,410.00 USD | 20,210.00 USD | 2,630.00 USD | 15,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7040` | 446,680.00 USD | 446,680.00 USD | 0.00 USD | 0.00 USD | 31,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7050` | 329,400.00 USD | 329,400.00 USD | 36,240.00 USD | 2,660.00 USD | 12,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7050` | 597,790.00 USD | 597,790.00 USD | 27,630.00 USD | 0.00 USD | 123,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7060` | 349,190.00 USD | 349,190.00 USD | 3,570.00 USD | 3,860.00 USD | 12,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7060` | 684,200.00 USD | 684,200.00 USD | 13,090.00 USD | 33,490.00 USD | 39,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7070` | 408,110.00 USD | 408,110.00 USD | 19,980.00 USD | 21,860.00 USD | 17,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7070` | 758,190.00 USD | 758,190.00 USD | 8,720.00 USD | 36,300.00 USD | 28,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7080` | 434,350.00 USD | 434,350.00 USD | 18,420.00 USD | 3,500.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7080` | 856,070.00 USD | 856,070.00 USD | 15,730.00 USD | 28,570.00 USD | 53,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7090` | 472,730.00 USD | 472,730.00 USD | 23,150.00 USD | 6,370.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7090` | 1,130,000.00 USD | 1,130,000.00 USD | 106,000.00 USD | 32,830.00 USD | 134,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7100` | 507,690.00 USD | 507,690.00 USD | 10,040.00 USD | 3,180.00 USD | 21,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7100` | 1,220,000.00 USD | 1,220,000.00 USD | 44,820.00 USD | 30,700.00 USD | 14,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7110` | 532,560.00 USD | 532,560.00 USD | 7,440.00 USD | 8,760.00 USD | 8,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7110` | 1,390,000.00 USD | 1,390,000.00 USD | 40,300.00 USD | 33,410.00 USD | 92,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7120` | 574,350.00 USD | 574,350.00 USD | 21,700.00 USD | 4,410.00 USD | 15,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7120` | 1,610,000.00 USD | 1,610,000.00 USD | 60,730.00 USD | 45,350.00 USD | 122,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7130` | 637,110.00 USD | 637,110.00 USD | 26,550.00 USD | 2,050.00 USD | 34,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7130` | 1,770,000.00 USD | 1,770,000.00 USD | 75,250.00 USD | 31,940.00 USD | 51,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7140` | 678,400.00 USD | 678,400.00 USD | 27,390.00 USD | 7,490.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7140` | 2,020,000.00 USD | 2,020,000.00 USD | 127,300.00 USD | 35,310.00 USD | 81,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7150` | 726,930.00 USD | 726,930.00 USD | 18,260.00 USD | 6,980.00 USD | 23,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7150` | 2,190,000.00 USD | 2,190,000.00 USD | 50,460.00 USD | 26,770.00 USD | 96,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7160` | 764,240.00 USD | 764,240.00 USD | 15,330.00 USD | 11,180.00 USD | 10,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7160` | 2,360,000.00 USD | 2,360,000.00 USD | 62,580.00 USD | 38,490.00 USD | 68,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7170` | 781,710.00 USD | 781,710.00 USD | 4,910.00 USD | 3,880.00 USD | 8,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7170` | 2,560,000.00 USD | 2,560,000.00 USD | 105,890.00 USD | 35,770.00 USD | 53,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7180` | 805,670.00 USD | 805,670.00 USD | 6,240.00 USD | 2,890.00 USD | 14,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7180` | 2,650,000.00 USD | 2,650,000.00 USD | 59,980.00 USD | 21,140.00 USD | 12,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7190` | 828,680.00 USD | 828,680.00 USD | 12,780.00 USD | 8,180.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7190` | 2,780,000.00 USD | 2,780,000.00 USD | 28,670.00 USD | 11,840.00 USD | 87,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7200` | 848,130.00 USD | 848,130.00 USD | 0.00 USD | 4,740.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7200` | 2,970,000.00 USD | 2,970,000.00 USD | 65,080.00 USD | 33,310.00 USD | 89,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7210` | 880,400.00 USD | 880,400.00 USD | 10,550.00 USD | 14,540.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7210` | 3,270,000.00 USD | 3,270,000.00 USD | 206,240.00 USD | 24,720.00 USD | 70,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7220` | 932,210.00 USD | 932,210.00 USD | 23,430.00 USD | 5,070.00 USD | 23,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7220` | 3,450,000.00 USD | 3,450,000.00 USD | 112,190.00 USD | 42,410.00 USD | 27,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7230` | 968,070.00 USD | 968,070.00 USD | 3,920.00 USD | 4,060.00 USD | 27,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7230` | 3,610,000.00 USD | 3,610,000.00 USD | 59,050.00 USD | 10,400.00 USD | 93,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7235` | 42,980.00 USD | 42,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7240` | 987,230.00 USD | 987,230.00 USD | 2,920.00 USD | 4,240.00 USD | 12,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7240` | 3,730,000.00 USD | 3,730,000.00 USD | 75,360.00 USD | 14,510.00 USD | 28,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7250` | 1,010,000.00 USD | 1,010,000.00 USD | 4,760.00 USD | 3,950.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7250` | 3,890,000.00 USD | 3,890,000.00 USD | 52,270.00 USD | 25,530.00 USD | 82,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7255` | 729.79 USD | 43,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7260` | 1,040,000.00 USD | 1,040,000.00 USD | 11,880.00 USD | 6,730.00 USD | 12,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7260` | 4,070,000.00 USD | 4,070,000.00 USD | 54,140.00 USD | 26,590.00 USD | 93,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7265` | 124.62 USD | 43,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7270` | 1,070,000.00 USD | 1,070,000.00 USD | 19,920.00 USD | 2,760.00 USD | 14,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7270` | 4,170,000.00 USD | 4,170,000.00 USD | 49,240.00 USD | 18,120.00 USD | 33,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7280` | 1,110,000.00 USD | 1,110,000.00 USD | 16,410.00 USD | 5,780.00 USD | 11,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7280` | 4,280,000.00 USD | 4,280,000.00 USD | 42,560.00 USD | 22,060.00 USD | 50,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7290` | 1,150,000.00 USD | 1,150,000.00 USD | 13,150.00 USD | 7,110.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7290` | 4,430,000.00 USD | 4,430,000.00 USD | 47,200.00 USD | 32,380.00 USD | 69,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7300` | 1,200,000.00 USD | 1,200,000.00 USD | 9,980.00 USD | 9,840.00 USD | 25,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7300` | 4,540,000.00 USD | 4,540,000.00 USD | 55,390.00 USD | 27,940.00 USD | 29,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7310` | 1,210,000.00 USD | 1,210,000.00 USD | 1,010.00 USD | 1,670.00 USD | 7,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7310` | 4,730,000.00 USD | 4,730,000.00 USD | 115,470.00 USD | 40,620.00 USD | 31,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7320` | 1,230,000.00 USD | 1,230,000.00 USD | 5,780.00 USD | 1,140.00 USD | 12,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7320` | 4,880,000.00 USD | 4,880,000.00 USD | 74,380.00 USD | 25,020.00 USD | 49,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7325` | 7,150.00 USD | 50,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7330` | 1,240,000.00 USD | 1,240,000.00 USD | 6,450.00 USD | 3,420.00 USD | 4,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7330` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 32,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7340` | 1,250,000.00 USD | 1,250,000.00 USD | 1,620.00 USD | 1,530.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7340` | 4,980,000.00 USD | 4,980,000.00 USD | 31,260.00 USD | 8,620.00 USD | 30,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7345` | 150.17 USD | 51,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7350` | 1,250,000.00 USD | 1,250,000.00 USD | 735.24 USD | 1,470.00 USD | 24.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7350` | 5,080,000.00 USD | 5,080,000.00 USD | 66,390.00 USD | 15,820.00 USD | 15,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7360` | 1,280,000.00 USD | 1,280,000.00 USD | 10,900.00 USD | 2,960.00 USD | 14,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7360` | 5,170,000.00 USD | 5,170,000.00 USD | 37,210.00 USD | 30,980.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7370` | 1,300,000.00 USD | 1,300,000.00 USD | 1,110.00 USD | 1,970.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7370` | 5,200,000.00 USD | 5,200,000.00 USD | 9,640.00 USD | 3,860.00 USD | 20,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7380` | 1,300,000.00 USD | 1,300,000.00 USD | 4,530.00 USD | 963.47 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7380` | 5,310,000.00 USD | 5,310,000.00 USD | 58,340.00 USD | 13,660.00 USD | 39,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7390` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 1,180.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7390` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 8,110.00 USD | 25,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7400` | 1,310,000.00 USD | 1,310,000.00 USD | 2,880.00 USD | 2,520.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7400` | 5,370,000.00 USD | 5,370,000.00 USD | 1,730.00 USD | 6,500.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7410` | 1,320,000.00 USD | 1,320,000.00 USD | 1,490.00 USD | 1,030.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7410` | 5,460,000.00 USD | 5,460,000.00 USD | 28,380.00 USD | 30,100.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7420` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 11.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7420` | 5,480,000.00 USD | 5,480,000.00 USD | 7,430.00 USD | 13,420.00 USD | 427.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7430` | 1,320,000.00 USD | 1,320,000.00 USD | 1,240.00 USD | 0.00 USD | 106.97 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7430` | 5,590,000.00 USD | 5,590,000.00 USD | 46,330.00 USD | 13,970.00 USD | 54,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7440` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 718.40 USD | 5,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7440` | 5,660,000.00 USD | 5,660,000.00 USD | 28,120.00 USD | 25,920.00 USD | 15,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7450` | 1,340,000.00 USD | 1,340,000.00 USD | 2,110.00 USD | 1,170.00 USD | 6,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7450` | 5,760,000.00 USD | 5,760,000.00 USD | 42,580.00 USD | 16,360.00 USD | 32,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7460` | 1,350,000.00 USD | 1,350,000.00 USD | 5,670.00 USD | 307.09 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7460` | 5,820,000.00 USD | 5,820,000.00 USD | 38,650.00 USD | 10,350.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7470` | 1,360,000.00 USD | 1,360,000.00 USD | 2,490.00 USD | 0.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7470` | 5,900,000.00 USD | 5,900,000.00 USD | 35,630.00 USD | 18,610.00 USD | 28,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7480` | 1,370,000.00 USD | 1,370,000.00 USD | 4,130.00 USD | 398.52 USD | 6,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7480` | 5,940,000.00 USD | 5,940,000.00 USD | 24,950.00 USD | 10,290.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7490` | 1,380,000.00 USD | 1,380,000.00 USD | 4,140.00 USD | 596.50 USD | 3,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7490` | 5,970,000.00 USD | 5,970,000.00 USD | 17,270.00 USD | 5,180.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7500` | 1,380,000.00 USD | 1,380,000.00 USD | 6,120.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7500` | 6,030,000.00 USD | 6,030,000.00 USD | 35,050.00 USD | 7,430.00 USD | 16,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7510` | 1,390,000.00 USD | 1,390,000.00 USD | 2,730.00 USD | 0.00 USD | 15.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7510` | 6,100,000.00 USD | 6,100,000.00 USD | 25,900.00 USD | 5,870.00 USD | 35,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7520` | 1,390,000.00 USD | 1,390,000.00 USD | 1,460.00 USD | 1,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7520` | 6,150,000.00 USD | 6,150,000.00 USD | 27,570.00 USD | 7,130.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7530` | 6,180,000.00 USD | 6,180,000.00 USD | 21,290.00 USD | 1,890.00 USD | 14,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7540` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 39.38 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7540` | 6,200,000.00 USD | 6,200,000.00 USD | 9,060.00 USD | 0.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7550` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 1,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7550` | 6,240,000.00 USD | 6,240,000.00 USD | 18,390.00 USD | 6,470.00 USD | 19,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7560` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 678.61 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7560` | 6,260,000.00 USD | 6,260,000.00 USD | 7,600.00 USD | 1,100.00 USD | 2,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7570` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 11.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7570` | 6,320,000.00 USD | 6,320,000.00 USD | 29,140.00 USD | 4,260.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7580` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 1,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7580` | 6,370,000.00 USD | 6,370,000.00 USD | 26,280.00 USD | 7,530.00 USD | 12,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7590` | 1,400,000.00 USD | 1,400,000.00 USD | 1,990.00 USD | 0.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7590` | 6,440,000.00 USD | 6,440,000.00 USD | 34,970.00 USD | 717.68 USD | 32,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7600` | 1,400,000.00 USD | 1,400,000.00 USD | 2,520.00 USD | 0.00 USD | 4.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7600` | 6,510,000.00 USD | 6,510,000.00 USD | 22,050.00 USD | 3,600.00 USD | 47,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7610` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7610` | 6,550,000.00 USD | 6,550,000.00 USD | 14,110.00 USD | 8,700.00 USD | 16,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7620` | 1,410,000.00 USD | 1,410,000.00 USD | 4,840.00 USD | 4,260.00 USD | 15.31 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7620` | 6,610,000.00 USD | 6,610,000.00 USD | 40,030.00 USD | 15,470.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7630` | 1,410,000.00 USD | 1,410,000.00 USD | 1,800.00 USD | 986.03 USD | 49.38 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7630` | 6,680,000.00 USD | 6,680,000.00 USD | 33,960.00 USD | 13,520.00 USD | 22,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7640` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 6.40 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7640` | 6,720,000.00 USD | 6,720,000.00 USD | 16,430.00 USD | 0.00 USD | 18,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7650` | 1,420,000.00 USD | 1,420,000.00 USD | 1,110.00 USD | 1,050.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7650` | 6,850,000.00 USD | 6,850,000.00 USD | 43,020.00 USD | 9,740.00 USD | 79,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7660` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 255.94 USD | 3,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7660` | 6,880,000.00 USD | 6,880,000.00 USD | 13,100.00 USD | 8,390.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7670` | 1,430,000.00 USD | 1,430,000.00 USD | 532.62 USD | 0.00 USD | 1,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7670` | 6,950,000.00 USD | 6,950,000.00 USD | 32,170.00 USD | 17,130.00 USD | 24,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7680` | 1,430,000.00 USD | 1,430,000.00 USD | 3,040.00 USD | 463.43 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7680` | 7,020,000.00 USD | 7,020,000.00 USD | 34,410.00 USD | 15,390.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7690` | 1,440,000.00 USD | 1,440,000.00 USD | 3,850.00 USD | 186.37 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7690` | 7,040,000.00 USD | 7,040,000.00 USD | 5,320.00 USD | 2,840.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7700` | 1,450,000.00 USD | 1,450,000.00 USD | 3,090.00 USD | 1,210.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7700` | 7,090,000.00 USD | 7,090,000.00 USD | 5,540.00 USD | 9,750.00 USD | 31,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7710` | 1,460,000.00 USD | 1,460,000.00 USD | 2,710.00 USD | 888.39 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7710` | 7,180,000.00 USD | 7,180,000.00 USD | 53,500.00 USD | 19,240.00 USD | 17,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7720` | 1,460,000.00 USD | 1,460,000.00 USD | 1,430.00 USD | 2,030.00 USD | 1,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7720` | 7,200,000.00 USD | 7,200,000.00 USD | 4,880.00 USD | 13,680.00 USD | 8,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7725` | 165.62 USD | 51,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7730` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 481.15 USD | 1,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7730` | 7,270,000.00 USD | 7,270,000.00 USD | 37,120.00 USD | 14,120.00 USD | 12,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7740` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 944.65 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7740` | 7,320,000.00 USD | 7,320,000.00 USD | 14,480.00 USD | 11,130.00 USD | 23,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7750` | 7,330,000.00 USD | 7,330,000.00 USD | 5,090.00 USD | 0.00 USD | 7,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7760` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 1,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7760` | 7,370,000.00 USD | 7,370,000.00 USD | 33,080.00 USD | 2,980.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7765` | 330.78 USD | 51,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7770` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 613.64 USD | 931.07 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7770` | 7,420,000.00 USD | 7,420,000.00 USD | 15,750.00 USD | 15,940.00 USD | 19,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7780` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 402.81 USD | 1.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7780` | 7,490,000.00 USD | 7,490,000.00 USD | 53,050.00 USD | 4,910.00 USD | 13,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7790` | 1,480,000.00 USD | 1,480,000.00 USD | 2,710.00 USD | 465.78 USD | 4,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7790` | 7,530,000.00 USD | 7,530,000.00 USD | 11,330.00 USD | 2,770.00 USD | 22,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7800` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7800` | 7,670,000.00 USD | 7,670,000.00 USD | 49,160.00 USD | 19,160.00 USD | 72,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7810` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 329.44 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7810` | 7,730,000.00 USD | 7,730,000.00 USD | 49,880.00 USD | 5,150.00 USD | 3,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7820` | 7,830,000.00 USD | 7,830,000.00 USD | 83,980.00 USD | 12,700.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7830` | 7,910,000.00 USD | 7,910,000.00 USD | 70,580.00 USD | 6,240.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7840` | 7,940,000.00 USD | 7,940,000.00 USD | 24,790.00 USD | 4,140.00 USD | 12.00 USD | `Tier 1 CEX` |
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
| `Sell Stop` | `0.3505` | 137,430.00 USD | 0.00 USD | 340.19 USD | `-49.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4635` | 137,090.00 USD | 0.00 USD | 104.57 USD | `-33.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4805` | 136,990.00 USD | 0.00 USD | 14,740.00 USD | `-30.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 122,250.00 USD | 0.00 USD | 604.46 USD | `-27.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5125` | 121,640.00 USD | 0.00 USD | 5,380.00 USD | `-25.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5205` | 116,260.00 USD | 0.00 USD | 228.77 USD | `-24.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5305` | 116,030.00 USD | 0.00 USD | 770.19 USD | `-23.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5445` | 115,260.00 USD | 0.00 USD | 14,110.00 USD | `-21.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5455` | 101,150.00 USD | 0.00 USD | 7,540.00 USD | `-21.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5485` | 93,620.00 USD | 0.00 USD | 4,500.00 USD | `-20.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5555` | 89,120.00 USD | 0.00 USD | 33,000.00 USD | `-19.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5565` | 56,120.00 USD | 0.00 USD | 173.58 USD | `-19.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 55,950.00 USD | 0.00 USD | 339.84 USD | `-19.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5835` | 55,610.00 USD | 0.00 USD | 178.88 USD | `-15.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5865` | 55,430.00 USD | 0.00 USD | 128.36 USD | `-15.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5875` | 55,300.00 USD | 0.00 USD | 128.34 USD | `-15.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5895` | 55,170.00 USD | 0.00 USD | 128.45 USD | `-14.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5925` | 55,050.00 USD | 0.00 USD | 128.33 USD | `-14.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5975` | 54,920.00 USD | 0.00 USD | 597.80 USD | `-13.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 54,320.00 USD | 0.00 USD | 3,510.00 USD | `-13.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 50,810.00 USD | 0.00 USD | 1,510.00 USD | `-12.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6085` | 49,310.00 USD | 0.00 USD | 301.32 USD | `-12.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6115` | 49,000.00 USD | 0.00 USD | 2,230.00 USD | `-11.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6125` | 46,780.00 USD | 0.00 USD | 108.68 USD | `-11.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6185` | 46,670.00 USD | 0.00 USD | 177.58 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 46,490.00 USD | 0.00 USD | 541.40 USD | `-10.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6285` | 45,950.00 USD | 0.00 USD | 469.94 USD | `-9.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 45,480.00 USD | 0.00 USD | 4,430.00 USD | `-8.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6315` | 41,050.00 USD | 0.00 USD | 160.16 USD | `-8.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6335` | 40,890.00 USD | 0.00 USD | 8,390.00 USD | `-8.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6345` | 32,500.00 USD | 0.00 USD | 276.40 USD | `-8.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6395` | 32,220.00 USD | 0.00 USD | 1,200.00 USD | `-7.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6405` | 31,020.00 USD | 0.00 USD | 145.91 USD | `-7.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6485` | 30,880.00 USD | 0.00 USD | 447.03 USD | `-6.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 30,430.00 USD | 0.00 USD | 567.58 USD | `-6.06%` | `TACTICAL (Retail Cluster)` |
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
| `Buy Stop` | `0.7265` | 32,090.00 USD | 6,410.00 USD | 0.00 USD | `+4.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7305` | 47,680.00 USD | 15,600.00 USD | 0.00 USD | `+5.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7325` | 47,850.00 USD | 165.17 USD | 0.00 USD | `+5.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7345` | 48,880.00 USD | 1,030.00 USD | 0.00 USD | `+6.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7375` | 48,980.00 USD | 106.75 USD | 0.00 USD | `+6.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7395` | 49,190.00 USD | 208.16 USD | 0.00 USD | `+6.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7405` | 49,920.00 USD | 733.09 USD | 0.00 USD | `+6.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7415` | 50,080.00 USD | 156.98 USD | 0.00 USD | `+7.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7425` | 50,210.00 USD | 132.95 USD | 0.00 USD | `+7.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7445` | 50,970.00 USD | 757.16 USD | 0.00 USD | `+7.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7455` | 53,140.00 USD | 2,170.00 USD | 0.00 USD | `+7.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7475` | 53,460.00 USD | 318.43 USD | 0.00 USD | `+7.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7495` | 53,590.00 USD | 132.98 USD | 0.00 USD | `+8.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7505` | 53,700.00 USD | 110.33 USD | 0.00 USD | `+8.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7525` | 53,830.00 USD | 134.74 USD | 0.00 USD | `+8.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7565` | 57,950.00 USD | 4,120.00 USD | 0.00 USD | `+9.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7575` | 58,460.00 USD | 511.82 USD | 0.00 USD | `+9.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7585` | 58,600.00 USD | 135.82 USD | 0.00 USD | `+9.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7615` | 59,470.00 USD | 875.23 USD | 0.00 USD | `+9.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7635` | 59,580.00 USD | 103.35 USD | 0.00 USD | `+10.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7665` | 59,700.00 USD | 127.48 USD | 0.00 USD | `+10.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7675` | 59,800.00 USD | 101.61 USD | 0.00 USD | `+10.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7695` | 59,990.00 USD | 186.97 USD | 0.00 USD | `+11.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7705` | 60,100.00 USD | 109.43 USD | 0.00 USD | `+11.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7775` | 60,270.00 USD | 166.70 USD | 0.00 USD | `+12.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7815` | 61,400.00 USD | 1,140.00 USD | 0.00 USD | `+12.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7865` | 67,720.00 USD | 6,310.00 USD | 0.00 USD | `+13.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8095` | 67,850.00 USD | 133.42 USD | 0.00 USD | `+16.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8125` | 79,920.00 USD | 12,070.00 USD | 0.00 USD | `+17.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8235` | 82,810.00 USD | 2,890.00 USD | 0.00 USD | `+18.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8335` | 83,740.00 USD | 929.08 USD | 0.00 USD | `+20.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8475` | 124,330.00 USD | 40,590.00 USD | 0.00 USD | `+22.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8505` | 127,400.00 USD | 3,060.00 USD | 0.00 USD | `+22.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8515` | 138,430.00 USD | 11,030.00 USD | 0.00 USD | `+22.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8525` | 150,210.00 USD | 11,780.00 USD | 0.00 USD | `+23.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8705` | 151,490.00 USD | 1,280.00 USD | 0.00 USD | `+25.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8725` | 151,650.00 USD | 159.86 USD | 0.00 USD | `+25.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 154,930.00 USD | 3,290.00 USD | 0.00 USD | `+35.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 155,270.00 USD | 340.54 USD | 0.00 USD | `+37.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 155,420.00 USD | 145.72 USD | 0.00 USD | `+40.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 156,410.00 USD | 987.50 USD | 0.00 USD | `+42.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 156,540.00 USD | 136.10 USD | 0.00 USD | `+44.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 157,090.00 USD | 550.48 USD | 0.00 USD | `+44.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 157,410.00 USD | 314.99 USD | 0.00 USD | `+48.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 158,010.00 USD | 602.17 USD | 0.00 USD | `+51.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 158,370.00 USD | 360.61 USD | 0.00 USD | `+53.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 159,310.00 USD | 942.77 USD | 0.00 USD | `+56.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 159,650.00 USD | 337.31 USD | 0.00 USD | `+56.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 160,050.00 USD | 397.19 USD | 0.00 USD | `+58.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 173,180.00 USD | 13,130.00 USD | 0.00 USD | `+80.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 174,500.00 USD | 1,320.00 USD | 0.00 USD | `+82.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 211,360.00 USD | 36,850.00 USD | 0.00 USD | `+87.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 238,570.00 USD | 27,210.00 USD | 0.00 USD | `+96.46%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.5870` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 0.00 USD | 1,400.00 USD | 65.70 USD |
| `7D` | `0.5880` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 3,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.5890` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 15.37 USD |
| `7D` | `0.5900` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 3,120.00 USD | 1,560.00 USD | 0.00 USD |
| `7D` | `0.5920` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 0.00 USD | 2,820.00 USD | 0.00 USD |
| `7D` | `0.5930` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 10,090.00 USD | 0.00 USD | 9,780.00 USD |
| `7D` | `0.5950` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 5,120.00 USD | 0.00 USD | 4,530.00 USD |
| `7D` | `0.5960` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 5,120.00 USD | 1,640.00 USD | 46.83 USD |
| `7D` | `0.5970` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 9,710.00 USD |
| `7D` | `0.5980` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 7,660.00 USD | 826.53 USD | 3.00 USD |
| `7D` | `0.5990` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 3,320.00 USD | 1,340.00 USD | 14,100.00 USD |
| `7D` | `0.6000` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 0.00 USD | 796.28 USD | 4,700.00 USD |
| `7D` | `0.6020` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 7,890.00 USD | 8,040.00 USD | 4,010.00 USD |
| `7D` | `0.6030` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 2,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6040` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 7,830.00 USD |
| `7D` | `0.6060` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 2,850.00 USD | 0.00 USD | 32.95 USD |
| `7D` | `0.6070` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 32.69 USD |
| `7D` | `0.6080` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 2,860.00 USD | 0.00 USD | 124.87 USD |
| `7D` | `0.6090` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 6,360.00 USD | 0.00 USD | 3,860.00 USD |
| `7D` | `0.6100` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 7,480.00 USD | 2,570.00 USD | 0.00 USD |
| `7D` | `0.6110` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 0.00 USD | 2,210.00 USD | 6,970.00 USD |
| `1D` | `0.6120` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 3,390.00 USD | 398.52 USD | 11,750.00 USD |
| `7D` | `0.6120` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 2,100.00 USD | 3,510.00 USD | 7,130.00 USD |
| `1D` | `0.6130` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 4,140.00 USD | 596.50 USD | 3,150.00 USD |
| `7D` | `0.6130` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 8,870.00 USD | 1,050.00 USD | 4,110.00 USD |
| `1D` | `0.6140` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 6,120.00 USD | 0.00 USD | 2,740.00 USD |
| `7D` | `0.6140` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 4,540.00 USD | 7,000.00 USD | 6,660.00 USD |
| `1D` | `0.6150` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 2,730.00 USD | 0.00 USD | 30.06 USD |
| `7D` | `0.6150` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 11,130.00 USD | 5,870.00 USD | 2,780.00 USD |
| `1D` | `0.6160` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 1,460.00 USD | 1,690.00 USD | 126.06 USD |
| `7D` | `0.6160` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 1,790.00 USD | 2,510.00 USD | 3,820.00 USD |
| `1D` | `0.6170` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 3,480.00 USD |
| `7D` | `0.6170` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 13,260.00 USD | 2,610.00 USD | 14,640.00 USD |
| `1D` | `0.6180` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 0.00 USD | 678.61 USD | 0.00 USD |
| `7D` | `0.6180` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 7,600.00 USD | 1,190.00 USD | 6,150.00 USD |
| `1D` | `0.6190` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 126.86 USD |
| `7D` | `0.6190` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 9,560.00 USD | 1,930.00 USD | 9,510.00 USD |
| `1D` | `0.6200` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD |
| `7D` | `0.6200` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 13,870.00 USD | 5,230.00 USD | 6,120.00 USD |
| `1D` | `0.6210` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 1,990.00 USD | 0.00 USD | 2,070.00 USD |
| `7D` | `0.6210` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 4,760.00 USD | 1,860.00 USD | 5,170.00 USD |
| `1D` | `0.6220` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 2,520.00 USD | 0.00 USD | 7.22 USD |
| `7D` | `0.6220` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 7,960.00 USD | 2,310.00 USD | 29,850.00 USD |
| `1D` | `0.6230` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD |
| `7D` | `0.6230` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 9,770.00 USD | 4,700.00 USD | 8,310.00 USD |
| `1D` | `0.6240` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 4,840.00 USD | 4,260.00 USD | 76.16 USD |
| `7D` | `0.6240` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 18,610.00 USD | 4,720.00 USD | 4,990.00 USD |
| `1D` | `0.6250` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 1,800.00 USD | 2,630.00 USD | 85.42 USD |
| `7D` | `0.6250` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 16,120.00 USD | 3,830.00 USD | 2,470.00 USD |
| `1D` | `0.6260` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 10,030.00 USD | 1,310.00 USD | 9,340.00 USD |
| `7D` | `0.6260` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 20,890.00 USD | 7,660.00 USD | 26,000.00 USD |
| `1D` | `0.6270` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 3,700.00 USD | 3,940.00 USD | 12,850.00 USD |
| `7D` | `0.6270` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 17,460.00 USD | 8,200.00 USD | 24,500.00 USD |
| `1D` | `0.6280` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 11,690.00 USD | 463.43 USD | 2,010.00 USD |
| `7D` | `0.6280` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 9,160.00 USD | 9,230.00 USD | 16,640.00 USD |
| `1D` | `0.6290` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 11,890.00 USD | 1,200.00 USD | 5,120.00 USD |
| `7D` | `0.6290` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 17,710.00 USD | 6,740.00 USD | 10,220.00 USD |
| `1D` | `0.6300` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 12,950.00 USD | 2,470.00 USD | 2,930.00 USD |
| `7D` | `0.6300` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 10,040.00 USD | 7,890.00 USD | 11,260.00 USD |
| `1D` | `0.6310` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 7,940.00 USD | 5,110.00 USD | 4,200.00 USD |
| `7D` | `0.6310` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 19,340.00 USD | 4,520.00 USD | 17,260.00 USD |
| `1D` | `0.6320` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 12,320.00 USD | 11,080.00 USD | 14,850.00 USD |
| `7D` | `0.6320` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 4,880.00 USD | 12,650.00 USD | 8,800.00 USD |
| `1D` | `0.6330` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 17,300.00 USD | 3,580.00 USD | 21,010.00 USD |
| `7D` | `0.6330` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 57,940.00 USD | 14,700.00 USD | 33,780.00 USD |
| `1D` | `0.6340` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 9,830.00 USD | 2,020.00 USD | 15,370.00 USD |
| `7D` | `0.6340` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 10,730.00 USD | 3,420.00 USD | 4,590.00 USD |
| `1D` | `0.6350` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 19,180.00 USD | 8,820.00 USD | 4,220.00 USD |
| `7D` | `0.6350` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 14,450.00 USD | 2,430.00 USD | 22,930.00 USD |
| `1D` | `0.6360` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 30,350.00 USD | 9,150.00 USD | 33,300.00 USD |
| `7D` | `0.6360` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 42,690.00 USD | 7,300.00 USD | 40,420.00 USD |
| `1D` | `0.6370` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 21,750.00 USD | 4,510.00 USD | 27,380.00 USD |
| `7D` | `0.6370` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 49,080.00 USD | 4,870.00 USD | 29.01 USD |
| `1D` | `0.6380` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 19,430.00 USD | 7,180.00 USD | 7,690.00 USD |
| `7D` | `0.6380` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 18,140.00 USD | 3,870.00 USD | 30,350.00 USD |
| `1D` | `0.6390` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 18,790.00 USD | 529.57 USD | 6,720.00 USD |
| `7D` | `0.6390` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 10,200.00 USD | 7,510.00 USD | 13,080.00 USD |
| `1D` | `0.6400` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 9,830.00 USD | 9,970.00 USD | 25,500.00 USD |
| `7D` | `0.6400` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 15,560.00 USD | 0.00 USD | 330.78 USD |
| `1D` | `0.6410` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 20,930.00 USD | 2,240.00 USD | 3,610.00 USD |
| `7D` | `0.6410` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 6,310.00 USD |
| `1D` | `0.6420` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 32,540.00 USD | 7,850.00 USD | 12,640.00 USD |
| `7D` | `0.6420` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 39,060.00 USD | 26,560.00 USD | 10,220.00 USD |
| `1D` | `0.6430` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 25,620.00 USD | 7,460.00 USD | 9,330.00 USD |
| `7D` | `0.6430` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 16,200.00 USD | 3,970.00 USD | 3,180.00 USD |
| `1D` | `0.6440` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 21,790.00 USD | 11,330.00 USD | 8,430.00 USD |
| `7D` | `0.6440` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 14,160.00 USD | 6,720.00 USD | 14,690.00 USD |
| `1D` | `0.6450` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 23,100.00 USD | 20,050.00 USD | 31,350.00 USD |
| `7D` | `0.6450` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 14,120.00 USD | 15,560.00 USD | 383.87 USD |
| `1D` | `0.6460` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 43,360.00 USD | 10,480.00 USD | 51,650.00 USD |
| `7D` | `0.6460` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 75,060.00 USD | 14,300.00 USD | 75,640.00 USD |
| `1D` | `0.6470` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 30,630.00 USD | 6,620.00 USD | 41,800.00 USD |
| `7D` | `0.6470` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 9,660.00 USD | 3,880.00 USD | 9,220.00 USD |
| `1D` | `0.6480` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 48,130.00 USD | 14,180.00 USD | 7,790.00 USD |
| `7D` | `0.6480` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 37,050.00 USD | 0.00 USD | 23,780.00 USD |
| `1D` | `0.6490` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 27,600.00 USD | 3,800.00 USD | 40,900.00 USD |
| `7D` | `0.6490` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 36,340.00 USD | 0.00 USD | 17,650.00 USD |
| `1D` | `0.6500` | 959,670.00 USD | 0.00 USD | 959,670.00 USD | 42,280.00 USD | 1,390.00 USD | 32,640.00 USD |
| `7D` | `0.6500` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 18,310.00 USD | 0.00 USD | 67,380.00 USD |
| `1D` | `0.6510` | 883,360.00 USD | 0.00 USD | 883,360.00 USD | 18,580.00 USD | 4,450.00 USD | 57,750.00 USD |
| `7D` | `0.6510` | 927,650.00 USD | 0.00 USD | 927,650.00 USD | 101,440.00 USD | 4,190.00 USD | 288.03 USD |
| `1D` | `0.6520` | 802,570.00 USD | 0.00 USD | 802,570.00 USD | 31,260.00 USD | 6,190.00 USD | 16,810.00 USD |
| `7D` | `0.6520` | 821,730.00 USD | 0.00 USD | 821,730.00 USD | 39,510.00 USD | 6,720.00 USD | 71,830.00 USD |
| `1D` | `0.6530` | 748,310.00 USD | 0.00 USD | 748,310.00 USD | 5,780.00 USD | 1,060.00 USD | 11,730.00 USD |
| `7D` | `0.6530` | 703,670.00 USD | 0.00 USD | 703,670.00 USD | 0.00 USD | 0.00 USD | 47,100.00 USD |
| `1D` | `0.6540` | 729,740.00 USD | 0.00 USD | 729,740.00 USD | 11,450.00 USD | 2,530.00 USD | 15,300.00 USD |
| `7D` | `0.6540` | 656,570.00 USD | 0.00 USD | 656,570.00 USD | 15,730.00 USD | 0.00 USD | 14,640.00 USD |
| `1D` | `0.6550` | 700,450.00 USD | 0.00 USD | 700,450.00 USD | 18,980.00 USD | 4,080.00 USD | 15,970.00 USD |
| `7D` | `0.6550` | 626,200.00 USD | 0.00 USD | 626,200.00 USD | 0.00 USD | 0.00 USD | 38,430.00 USD |
| `1D` | `0.6560` | 661,420.00 USD | 0.00 USD | 661,420.00 USD | 23,680.00 USD | 3,800.00 USD | 25,070.00 USD |
| `7D` | `0.6560` | 587,770.00 USD | 0.00 USD | 587,770.00 USD | 7,220.00 USD | 5,380.00 USD | 34,730.00 USD |
| `1D` | `0.6570` | 608,870.00 USD | 0.00 USD | 608,870.00 USD | 5,570.00 USD | 1,820.00 USD | 19,780.00 USD |
| `7D` | `0.6570` | 540,440.00 USD | 0.00 USD | 540,440.00 USD | 14,440.00 USD | 0.00 USD | 10,650.00 USD |
| `1D` | `0.6580` | 581,690.00 USD | 0.00 USD | 581,690.00 USD | 5,880.00 USD | 0.00 USD | 30.62 USD |
| `7D` | `0.6580` | 515,350.00 USD | 0.00 USD | 515,350.00 USD | 0.00 USD | 0.00 USD | 12,650.00 USD |
| `1D` | `0.6590` | 575,780.00 USD | 0.00 USD | 575,780.00 USD | 2,100.00 USD | 5,490.00 USD | 19,900.00 USD |
| `7D` | `0.6590` | 502,700.00 USD | 0.00 USD | 502,700.00 USD | 9,540.00 USD | 0.00 USD | 331.05 USD |
| `1D` | `0.6600` | 548,300.00 USD | 0.00 USD | 548,300.00 USD | 21,900.00 USD | 2,840.00 USD | 22,600.00 USD |
| `7D` | `0.6600` | 492,830.00 USD | 0.00 USD | 492,830.00 USD | 0.00 USD | 4,180.00 USD | 20,230.00 USD |
| `1D` | `0.6610` | 500,950.00 USD | 0.00 USD | 500,950.00 USD | 11,920.00 USD | 2,560.00 USD | 12,170.00 USD |
| `1D` | `0.6620` | 474,300.00 USD | 0.00 USD | 474,300.00 USD | 14,030.00 USD | 2,480.00 USD | 16,000.00 USD |
| `7D` | `0.6620` | 468,420.00 USD | 0.00 USD | 468,420.00 USD | 14,320.00 USD | 0.00 USD | 7,130.00 USD |
| `1D` | `0.6630` | 441,780.00 USD | 0.00 USD | 441,780.00 USD | 24,070.00 USD | 4,110.00 USD | 1,840.00 USD |
| `7D` | `0.6630` | 446,960.00 USD | 0.00 USD | 446,960.00 USD | 11,670.00 USD | 0.00 USD | 254.70 USD |
| `1D` | `0.6640` | 411,750.00 USD | 0.00 USD | 411,750.00 USD | 22,290.00 USD | 1,150.00 USD | 21,410.00 USD |
| `7D` | `0.6640` | 435,030.00 USD | 0.00 USD | 435,030.00 USD | 15,140.00 USD | 0.00 USD | 279.64 USD |
| `1D` | `0.6650` | 366,900.00 USD | 0.00 USD | 366,900.00 USD | 12,560.00 USD | 10,330.00 USD | 14,290.00 USD |
| `7D` | `0.6650` | 419,620.00 USD | 0.00 USD | 419,620.00 USD | 0.00 USD | 6,770.00 USD | 288.69 USD |
| `1D` | `0.6660` | 329,730.00 USD | 0.00 USD | 329,730.00 USD | 7,730.00 USD | 0.00 USD | 5,410.00 USD |
| `7D` | `0.6660` | 412,560.00 USD | 0.00 USD | 412,560.00 USD | 0.00 USD | 0.00 USD | 148.18 USD |
| `1D` | `0.6670` | 316,580.00 USD | 0.00 USD | 316,580.00 USD | 18,850.00 USD | 2,980.00 USD | 4,930.00 USD |
| `7D` | `0.6670` | 412,410.00 USD | 0.00 USD | 412,410.00 USD | 31,450.00 USD | 0.00 USD | 8,780.00 USD |
| `1D` | `0.6680` | 289,830.00 USD | 0.00 USD | 289,830.00 USD | 30,610.00 USD | 3,380.00 USD | 7,310.00 USD |
| `7D` | `0.6680` | 372,180.00 USD | 0.00 USD | 372,180.00 USD | 24,780.00 USD | 7,780.00 USD | 193.34 USD |
| `1D` | `0.6690` | 248,530.00 USD | 0.00 USD | 248,530.00 USD | 13,000.00 USD | 2,800.00 USD | 3,630.00 USD |
| `7D` | `0.6690` | 339,430.00 USD | 0.00 USD | 339,430.00 USD | 14,440.00 USD | 2,330.00 USD | 24,430.00 USD |
| `1D` | `0.6700` | 229,100.00 USD | 0.00 USD | 229,100.00 USD | 3,250.00 USD | 1,050.00 USD | 4,190.00 USD |
| `7D` | `0.6700` | 298,230.00 USD | 0.00 USD | 298,230.00 USD | 0.00 USD | 0.00 USD | 323.96 USD |
| `1D` | `0.6710` | 220,610.00 USD | 0.00 USD | 220,610.00 USD | 8,650.00 USD | 18,100.00 USD | 0.00 USD |
| `7D` | `0.6710` | 297,900.00 USD | 0.00 USD | 297,900.00 USD | 0.00 USD | 6,960.00 USD | 25,020.00 USD |
| `1D` | `0.6720` | 193,860.00 USD | 0.00 USD | 193,860.00 USD | 4,190.00 USD | 3,200.00 USD | 17,150.00 USD |
| `1D` | `0.6730` | 169,320.00 USD | 0.00 USD | 169,320.00 USD | 5,220.00 USD | 2,020.00 USD | 7,600.00 USD |
| `7D` | `0.6730` | 265,930.00 USD | 0.00 USD | 265,930.00 USD | 0.00 USD | 0.00 USD | 99.42 USD |
| `1D` | `0.6740` | 154,470.00 USD | 0.00 USD | 154,470.00 USD | 20,500.00 USD | 4,800.00 USD | 2,310.00 USD |
| `1D` | `0.6750` | 126,860.00 USD | 0.00 USD | 126,860.00 USD | 0.00 USD | 5,970.00 USD | 9,790.00 USD |
| `7D` | `0.6750` | 265,830.00 USD | 0.00 USD | 265,830.00 USD | 0.00 USD | 75,730.00 USD | 0.00 USD |
| `1D` | `0.6760` | 111,090.00 USD | 0.00 USD | 111,090.00 USD | 9,950.00 USD | 2,630.00 USD | 8,550.00 USD |
| `7D` | `0.6760` | 190,110.00 USD | 0.00 USD | 190,110.00 USD | 0.00 USD | 2,240.00 USD | 71,700.00 USD |
| `1D` | `0.6770` | 89,960.00 USD | 0.00 USD | 89,960.00 USD | 18,650.00 USD | 2,660.00 USD | 3,600.00 USD |
| `7D` | `0.6770` | 116,160.00 USD | 0.00 USD | 116,160.00 USD | 23,340.00 USD | 4,190.00 USD | 0.00 USD |
| `1D` | `0.6780` | 65,050.00 USD | 0.00 USD | 65,050.00 USD | 0.00 USD | 12,640.00 USD | 8,770.00 USD |
| `7D` | `0.6780` | 88,640.00 USD | 0.00 USD | 88,640.00 USD | 13,090.00 USD | 10,220.00 USD | 48,740.00 USD |
| `1D` | `0.6790` | 43,640.00 USD | 0.00 USD | 43,640.00 USD | 10,840.00 USD | 18,610.00 USD | 14,200.00 USD |
| `7D` | `0.6790` | 16,590.00 USD | 0.00 USD | 16,590.00 USD | 0.00 USD | 16,590.00 USD | 0.00 USD |
| `7D` | `0.6810` | 15,720.00 USD | 15,720.00 USD | 0.00 USD | 0.00 USD | 15,720.00 USD | 0.00 USD |
| `7D` | `0.6810` | 31,440.00 USD | 31,440.00 USD | 0.00 USD | 0.00 USD | 15,720.00 USD | 0.00 USD |
| `1D` | `0.6820` | 4,920.00 USD | 4,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,920.00 USD |
| `1D` | `0.6820` | 9,840.00 USD | 9,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,920.00 USD |
| `7D` | `0.6820` | 69,160.00 USD | 69,160.00 USD | 0.00 USD | 0.00 USD | 37,730.00 USD | 0.00 USD |
| `1D` | `0.6830` | 55,770.00 USD | 55,770.00 USD | 0.00 USD | 0.00 USD | 20,240.00 USD | 25,690.00 USD |
| `7D` | `0.6830` | 122,090.00 USD | 122,090.00 USD | 0.00 USD | 0.00 USD | 4,670.00 USD | 48,260.00 USD |
| `1D` | `0.6840` | 86,620.00 USD | 86,620.00 USD | 0.00 USD | 6,510.00 USD | 15,960.00 USD | 8,380.00 USD |
| `7D` | `0.6840` | 175,840.00 USD | 175,840.00 USD | 0.00 USD | 0.00 USD | 14,650.00 USD | 39,100.00 USD |
| `1D` | `0.6850` | 133,130.00 USD | 133,130.00 USD | 0.00 USD | 46,480.00 USD | 0.00 USD | 27.82 USD |
| `7D` | `0.6850` | 180,550.00 USD | 180,550.00 USD | 0.00 USD | 0.00 USD | 4,710.00 USD | 0.00 USD |
| `7D` | `0.6860` | 190,380.00 USD | 190,380.00 USD | 0.00 USD | 0.00 USD | 9,830.00 USD | 0.00 USD |
| `1D` | `0.6870` | 133,150.00 USD | 133,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15.30 USD |
| `1D` | `0.6880` | 171,530.00 USD | 171,530.00 USD | 0.00 USD | 0.00 USD | 9,600.00 USD | 28,780.00 USD |
| `7D` | `0.6880` | 225,850.00 USD | 225,850.00 USD | 0.00 USD | 18,170.00 USD | 17,300.00 USD | 0.00 USD |
| `1D` | `0.6890` | 174,290.00 USD | 174,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,750.00 USD |
| `7D` | `0.6890` | 236,880.00 USD | 236,880.00 USD | 0.00 USD | 0.00 USD | 11,030.00 USD | 0.00 USD |
| `1D` | `0.6900` | 174,340.00 USD | 174,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 56.98 USD |
| `7D` | `0.6900` | 241,360.00 USD | 241,360.00 USD | 0.00 USD | 0.00 USD | 4,480.00 USD | 0.00 USD |
| `1D` | `0.6910` | 201,410.00 USD | 201,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 27,060.00 USD |
| `7D` | `0.6910` | 243,590.00 USD | 243,590.00 USD | 0.00 USD | 0.00 USD | 2,090.00 USD | 131.80 USD |
| `1D` | `0.6920` | 201,430.00 USD | 201,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.46 USD |
| `7D` | `0.6920` | 267,960.00 USD | 267,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,370.00 USD |
| `1D` | `0.6930` | 201,600.00 USD | 201,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 168.16 USD |
| `7D` | `0.6930` | 281,110.00 USD | 281,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,150.00 USD |
| `1D` | `0.6940` | 225,480.00 USD | 225,480.00 USD | 0.00 USD | 11,230.00 USD | 4,420.00 USD | 8,240.00 USD |
| `1D` | `0.6950` | 252,430.00 USD | 252,430.00 USD | 0.00 USD | 22,480.00 USD | 4,460.00 USD | 0.00 USD |
| `7D` | `0.6950` | 324,950.00 USD | 324,950.00 USD | 0.00 USD | 31,450.00 USD | 0.00 USD | 12,390.00 USD |
| `1D` | `0.6960` | 299,490.00 USD | 299,490.00 USD | 0.00 USD | 47,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6960` | 337,170.00 USD | 337,170.00 USD | 0.00 USD | 12,220.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6970` | 322,910.00 USD | 322,910.00 USD | 0.00 USD | 23,380.00 USD | 0.00 USD | 34.66 USD |
| `7D` | `0.6970` | 358,830.00 USD | 358,830.00 USD | 0.00 USD | 21,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6980` | 322,920.00 USD | 322,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17.79 USD |
| `1D` | `0.6990` | 324,910.00 USD | 324,910.00 USD | 0.00 USD | 0.00 USD | 1,940.00 USD | 38.35 USD |
| `7D` | `0.6990` | 388,560.00 USD | 388,560.00 USD | 0.00 USD | 4,770.00 USD | 0.00 USD | 24,960.00 USD |
| `1D` | `0.7000` | 342,210.00 USD | 342,210.00 USD | 0.00 USD | 4,190.00 USD | 2,120.00 USD | 10,990.00 USD |
| `7D` | `0.7000` | 398,550.00 USD | 398,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,990.00 USD |
| `1D` | `0.7010` | 342,250.00 USD | 342,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 42.72 USD |
| `1D` | `0.7020` | 356,630.00 USD | 356,630.00 USD | 0.00 USD | 14,360.00 USD | 0.00 USD | 22.18 USD |
| `7D` | `0.7020` | 467,970.00 USD | 467,970.00 USD | 0.00 USD | 16,350.00 USD | 0.00 USD | 53,080.00 USD |
| `1D` | `0.7030` | 356,650.00 USD | 356,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15.04 USD |
| `7D` | `0.7030` | 595,050.00 USD | 595,050.00 USD | 0.00 USD | 76,610.00 USD | 0.00 USD | 50,470.00 USD |
| `1D` | `0.7040` | 393,530.00 USD | 393,530.00 USD | 0.00 USD | 19,130.00 USD | 2,630.00 USD | 15,120.00 USD |
| `7D` | `0.7040` | 626,550.00 USD | 626,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,500.00 USD |
| `1D` | `0.7050` | 444,530.00 USD | 444,530.00 USD | 0.00 USD | 36,240.00 USD | 2,660.00 USD | 12,090.00 USD |
| `7D` | `0.7050` | 777,660.00 USD | 777,660.00 USD | 0.00 USD | 27,630.00 USD | 0.00 USD | 123,470.00 USD |
| `1D` | `0.7060` | 464,320.00 USD | 464,320.00 USD | 0.00 USD | 3,570.00 USD | 3,860.00 USD | 12,360.00 USD |
| `7D` | `0.7060` | 864,070.00 USD | 864,070.00 USD | 0.00 USD | 13,090.00 USD | 33,490.00 USD | 39,830.00 USD |
| `1D` | `0.7070` | 523,240.00 USD | 523,240.00 USD | 0.00 USD | 19,980.00 USD | 21,860.00 USD | 17,070.00 USD |
| `7D` | `0.7070` | 938,060.00 USD | 938,060.00 USD | 0.00 USD | 8,720.00 USD | 36,300.00 USD | 28,970.00 USD |
| `1D` | `0.7080` | 549,470.00 USD | 549,470.00 USD | 0.00 USD | 18,420.00 USD | 3,500.00 USD | 4,310.00 USD |
| `7D` | `0.7080` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 15,730.00 USD | 28,570.00 USD | 53,590.00 USD |
| `1D` | `0.7090` | 587,850.00 USD | 587,850.00 USD | 0.00 USD | 23,150.00 USD | 6,370.00 USD | 8,860.00 USD |
| `7D` | `0.7090` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 106,000.00 USD | 32,830.00 USD | 134,470.00 USD |
| `1D` | `0.7100` | 622,820.00 USD | 622,820.00 USD | 0.00 USD | 10,040.00 USD | 3,180.00 USD | 21,740.00 USD |
| `7D` | `0.7100` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 44,820.00 USD | 30,700.00 USD | 14,310.00 USD |
| `1D` | `0.7110` | 647,690.00 USD | 647,690.00 USD | 0.00 USD | 7,440.00 USD | 8,760.00 USD | 8,670.00 USD |
| `7D` | `0.7110` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 40,300.00 USD | 33,410.00 USD | 92,890.00 USD |
| `1D` | `0.7120` | 689,480.00 USD | 689,480.00 USD | 0.00 USD | 21,700.00 USD | 4,410.00 USD | 15,670.00 USD |
| `7D` | `0.7120` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 60,730.00 USD | 45,350.00 USD | 135,200.00 USD |
| `1D` | `0.7130` | 760,890.00 USD | 760,890.00 USD | 0.00 USD | 28,640.00 USD | 3,110.00 USD | 39,670.00 USD |
| `7D` | `0.7130` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 75,250.00 USD | 31,940.00 USD | 51,140.00 USD |
| `1D` | `0.7140` | 802,180.00 USD | 802,180.00 USD | 0.00 USD | 27,390.00 USD | 7,490.00 USD | 6,410.00 USD |
| `7D` | `0.7140` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 127,300.00 USD | 35,310.00 USD | 81,980.00 USD |
| `1D` | `0.7150` | 850,700.00 USD | 850,700.00 USD | 0.00 USD | 18,260.00 USD | 6,980.00 USD | 23,290.00 USD |
| `7D` | `0.7150` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 50,460.00 USD | 26,770.00 USD | 96,210.00 USD |
| `1D` | `0.7160` | 890,090.00 USD | 890,090.00 USD | 0.00 USD | 17,400.00 USD | 11,180.00 USD | 10,810.00 USD |
| `7D` | `0.7160` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 62,580.00 USD | 38,490.00 USD | 68,020.00 USD |
| `1D` | `0.7170` | 907,560.00 USD | 907,560.00 USD | 0.00 USD | 4,910.00 USD | 3,880.00 USD | 8,680.00 USD |
| `7D` | `0.7170` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 105,890.00 USD | 35,770.00 USD | 53,830.00 USD |
| `1D` | `0.7180` | 931,510.00 USD | 931,510.00 USD | 0.00 USD | 6,240.00 USD | 2,890.00 USD | 14,820.00 USD |
| `7D` | `0.7180` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 59,980.00 USD | 21,140.00 USD | 12,710.00 USD |
| `1D` | `0.7190` | 954,530.00 USD | 954,530.00 USD | 0.00 USD | 12,780.00 USD | 8,180.00 USD | 2,050.00 USD |
| `7D` | `0.7190` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 28,670.00 USD | 11,840.00 USD | 87,990.00 USD |
| `1D` | `0.7200` | 973,970.00 USD | 973,970.00 USD | 0.00 USD | 0.00 USD | 4,740.00 USD | 14,700.00 USD |
| `7D` | `0.7200` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 65,080.00 USD | 33,310.00 USD | 89,960.00 USD |
| `1D` | `0.7210` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 10,550.00 USD | 14,540.00 USD | 7,190.00 USD |
| `7D` | `0.7210` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 206,240.00 USD | 24,720.00 USD | 70,620.00 USD |
| `1D` | `0.7220` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 23,430.00 USD | 5,070.00 USD | 23,300.00 USD |
| `7D` | `0.7220` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 112,190.00 USD | 42,410.00 USD | 27,520.00 USD |
| `1D` | `0.7230` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 3,920.00 USD | 4,060.00 USD | 27,880.00 USD |
| `7D` | `0.7230` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 59,050.00 USD | 10,400.00 USD | 93,940.00 USD |
| `1D` | `0.7240` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 2,920.00 USD | 4,240.00 USD | 12,010.00 USD |
| `7D` | `0.7240` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 75,360.00 USD | 14,510.00 USD | 28,980.00 USD |
| `1D` | `0.7250` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 4,760.00 USD | 3,950.00 USD | 9,380.00 USD |
| `7D` | `0.7250` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 52,270.00 USD | 25,530.00 USD | 82,450.00 USD |
| `1D` | `0.7260` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 11,880.00 USD | 6,730.00 USD | 12,280.00 USD |
| `7D` | `0.7260` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 54,140.00 USD | 26,590.00 USD | 93,000.00 USD |
| `1D` | `0.7270` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 19,920.00 USD | 2,760.00 USD | 14,410.00 USD |
| `7D` | `0.7270` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 49,240.00 USD | 18,120.00 USD | 33,460.00 USD |
| `1D` | `0.7280` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 16,410.00 USD | 5,780.00 USD | 11,630.00 USD |
| `7D` | `0.7280` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 42,560.00 USD | 22,060.00 USD | 50,400.00 USD |
| `1D` | `0.7290` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 13,150.00 USD | 7,110.00 USD | 27,230.00 USD |
| `7D` | `0.7290` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 47,200.00 USD | 32,380.00 USD | 69,820.00 USD |
| `1D` | `0.7300` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 9,980.00 USD | 9,840.00 USD | 25,690.00 USD |
| `7D` | `0.7300` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 55,390.00 USD | 27,940.00 USD | 29,400.00 USD |
| `1D` | `0.7310` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 1,010.00 USD | 1,670.00 USD | 7,220.00 USD |
| `7D` | `0.7310` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 115,470.00 USD | 40,620.00 USD | 31,210.00 USD |
| `1D` | `0.7320` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 5,780.00 USD | 1,140.00 USD | 12,500.00 USD |
| `7D` | `0.7320` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 74,380.00 USD | 25,020.00 USD | 49,250.00 USD |
| `1D` | `0.7330` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 6,450.00 USD | 3,420.00 USD | 4,430.00 USD |
| `7D` | `0.7330` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 32,440.00 USD |
| `1D` | `0.7340` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 1,620.00 USD | 1,530.00 USD | 5,210.00 USD |
| `7D` | `0.7340` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 31,260.00 USD | 8,620.00 USD | 30,810.00 USD |
| `1D` | `0.7350` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 735.24 USD | 1,470.00 USD | 24.90 USD |
| `7D` | `0.7350` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 66,390.00 USD | 15,820.00 USD | 15,550.00 USD |
| `1D` | `0.7360` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 10,900.00 USD | 2,960.00 USD | 14,930.00 USD |
| `7D` | `0.7360` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 37,210.00 USD | 30,980.00 USD | 19,430.00 USD |
| `1D` | `0.7370` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 1,110.00 USD | 1,970.00 USD | 9,870.00 USD |
| `7D` | `0.7370` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 9,640.00 USD | 3,860.00 USD | 20,980.00 USD |
| `1D` | `0.7380` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 4,530.00 USD | 963.47 USD | 1,890.00 USD |
| `7D` | `0.7380` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 58,340.00 USD | 13,660.00 USD | 39,550.00 USD |
| `1D` | `0.7390` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 1,180.00 USD | 1,220.00 USD |
| `7D` | `0.7390` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 8,110.00 USD | 25,420.00 USD |
| `1D` | `0.7400` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 2,880.00 USD | 2,520.00 USD | 3,090.00 USD |
| `7D` | `0.7400` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 1,730.00 USD | 6,500.00 USD | 11,600.00 USD |
| `1D` | `0.7410` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 1,490.00 USD | 1,030.00 USD | 4,740.00 USD |
| `7D` | `0.7410` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 28,380.00 USD | 30,100.00 USD | 30,960.00 USD |
| `1D` | `0.7420` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11.18 USD |
| `7D` | `0.7420` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 7,430.00 USD | 13,420.00 USD | 427.42 USD |
| `1D` | `0.7430` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 1,240.00 USD | 0.00 USD | 106.97 USD |
| `7D` | `0.7430` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 46,330.00 USD | 13,970.00 USD | 54,630.00 USD |
| `1D` | `0.7440` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 718.40 USD | 5,140.00 USD |
| `7D` | `0.7440` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 28,120.00 USD | 25,920.00 USD | 15,750.00 USD |
| `1D` | `0.7450` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 2,110.00 USD | 1,170.00 USD | 6,060.00 USD |
| `7D` | `0.7450` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 42,580.00 USD | 16,360.00 USD | 32,760.00 USD |
| `1D` | `0.7460` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 5,670.00 USD | 307.09 USD | 4,440.00 USD |
| `7D` | `0.7460` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 38,650.00 USD | 10,350.00 USD | 13,310.00 USD |
| `1D` | `0.7470` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 2,490.00 USD | 0.00 USD | 4,540.00 USD |
| `7D` | `0.7470` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 35,630.00 USD | 18,610.00 USD | 28,150.00 USD |
| `1D` | `0.7480` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 4,130.00 USD | 398.52 USD | 6,290.00 USD |
| `7D` | `0.7480` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 24,950.00 USD | 10,290.00 USD | 4,240.00 USD |
| `1D` | `0.7490` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 4,140.00 USD | 596.50 USD | 3,170.00 USD |
| `7D` | `0.7490` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 17,270.00 USD | 5,180.00 USD | 8,950.00 USD |
| `1D` | `0.7500` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 6,120.00 USD | 0.00 USD | 2,720.00 USD |
| `7D` | `0.7500` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 35,050.00 USD | 7,430.00 USD | 16,190.00 USD |
| `1D` | `0.7510` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 2,730.00 USD | 0.00 USD | 15.02 USD |
| `7D` | `0.7510` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 25,900.00 USD | 5,870.00 USD | 35,700.00 USD |
| `1D` | `0.7520` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 1,460.00 USD | 1,690.00 USD | 0.00 USD |
| `7D` | `0.7520` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 27,570.00 USD | 7,130.00 USD | 15,070.00 USD |
| `7D` | `0.7530` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 21,290.00 USD | 1,890.00 USD | 14,560.00 USD |
| `1D` | `0.7540` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 40.37 USD |
| `7D` | `0.7540` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 9,060.00 USD | 0.00 USD | 10,870.00 USD |
| `1D` | `0.7550` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,450.00 USD |
| `7D` | `0.7550` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 18,390.00 USD | 6,470.00 USD | 19,610.00 USD |
| `1D` | `0.7560` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 678.61 USD | 0.00 USD |
| `7D` | `0.7560` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 7,600.00 USD | 1,100.00 USD | 2,650.00 USD |
| `1D` | `0.7570` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11.00 USD |
| `7D` | `0.7570` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 29,140.00 USD | 4,260.00 USD | 33,390.00 USD |
| `1D` | `0.7580` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,700.00 USD |
| `7D` | `0.7580` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 26,280.00 USD | 7,530.00 USD | 12,540.00 USD |
| `1D` | `0.7590` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 1,990.00 USD | 0.00 USD | 2,030.00 USD |
| `7D` | `0.7590` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 34,970.00 USD | 717.68 USD | 32,980.00 USD |
| `1D` | `0.7600` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 2,520.00 USD | 0.00 USD | 4.08 USD |
| `7D` | `0.7600` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 22,050.00 USD | 3,600.00 USD | 47,770.00 USD |
| `1D` | `0.7610` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD |
| `7D` | `0.7610` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 14,110.00 USD | 8,700.00 USD | 16,510.00 USD |
| `1D` | `0.7620` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 4,840.00 USD | 4,260.00 USD | 15.31 USD |
| `7D` | `0.7620` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 40,030.00 USD | 15,470.00 USD | 5,030.00 USD |
| `1D` | `0.7630` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 1,800.00 USD | 986.03 USD | 49.38 USD |
| `7D` | `0.7630` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 33,960.00 USD | 13,520.00 USD | 22,550.00 USD |
| `1D` | `0.7640` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6.40 USD |
| `7D` | `0.7640` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 16,430.00 USD | 0.00 USD | 18,990.00 USD |
| `1D` | `0.7650` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 1,110.00 USD | 1,050.00 USD | 5,880.00 USD |
| `7D` | `0.7650` | 7,050,000.00 USD | 7,050,000.00 USD | 0.00 USD | 43,020.00 USD | 9,740.00 USD | 79,400.00 USD |
| `1D` | `0.7660` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 255.94 USD | 3,430.00 USD |
| `7D` | `0.7660` | 7,080,000.00 USD | 7,080,000.00 USD | 0.00 USD | 13,100.00 USD | 8,390.00 USD | 11,690.00 USD |
| `1D` | `0.7670` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 532.62 USD | 0.00 USD | 1,450.00 USD |
| `7D` | `0.7670` | 7,150,000.00 USD | 7,150,000.00 USD | 0.00 USD | 32,170.00 USD | 17,130.00 USD | 24,290.00 USD |
| `1D` | `0.7680` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 3,040.00 USD | 463.43 USD | 1,960.00 USD |
| `7D` | `0.7680` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 34,410.00 USD | 15,390.00 USD | 16,720.00 USD |
| `1D` | `0.7690` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 3,850.00 USD | 186.37 USD | 4,970.00 USD |
| `7D` | `0.7690` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 5,320.00 USD | 2,840.00 USD | 9,960.00 USD |
| `1D` | `0.7700` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 3,090.00 USD | 1,210.00 USD | 2,800.00 USD |
| `7D` | `0.7700` | 7,280,000.00 USD | 7,280,000.00 USD | 0.00 USD | 5,540.00 USD | 9,750.00 USD | 31,770.00 USD |
| `1D` | `0.7710` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 2,710.00 USD | 888.39 USD | 4,080.00 USD |
| `7D` | `0.7710` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 53,500.00 USD | 19,240.00 USD | 17,220.00 USD |
| `1D` | `0.7720` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 1,430.00 USD | 2,030.00 USD | 1,910.00 USD |
| `7D` | `0.7720` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 4,880.00 USD | 13,680.00 USD | 8,560.00 USD |
| `1D` | `0.7730` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 481.15 USD | 1,920.00 USD |
| `7D` | `0.7730` | 7,460,000.00 USD | 7,460,000.00 USD | 0.00 USD | 37,120.00 USD | 14,120.00 USD | 12,590.00 USD |
| `1D` | `0.7740` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 944.65 USD |
| `7D` | `0.7740` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 14,480.00 USD | 11,130.00 USD | 23,150.00 USD |
| `7D` | `0.7750` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 5,090.00 USD | 0.00 USD | 7,800.00 USD |
| `1D` | `0.7760` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD | 0.00 USD |
| `7D` | `0.7760` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 33,080.00 USD | 2,980.00 USD | 4,950.00 USD |
| `1D` | `0.7770` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 613.64 USD | 931.07 USD |
| `7D` | `0.7770` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 15,750.00 USD | 15,940.00 USD | 19,320.00 USD |
| `1D` | `0.7780` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 402.81 USD | 1.90 USD |
| `7D` | `0.7780` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 53,050.00 USD | 4,910.00 USD | 13,260.00 USD |
| `1D` | `0.7790` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 2,710.00 USD | 465.78 USD | 4,490.00 USD |
| `7D` | `0.7790` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 11,330.00 USD | 2,770.00 USD | 22,770.00 USD |
| `1D` | `0.7800` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,470.00 USD |
| `7D` | `0.7800` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 49,160.00 USD | 19,160.00 USD | 72,680.00 USD |
| `1D` | `0.7810` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 329.44 USD | 0.00 USD |
| `7D` | `0.7810` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 49,880.00 USD | 5,150.00 USD | 3,900.00 USD |
| `7D` | `0.7820` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 65,310.00 USD | 12,700.00 USD | 6,240.00 USD |
| `7D` | `0.7830` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 70,580.00 USD | 6,240.00 USD | 2,170.00 USD |
| `7D` | `0.7840` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 24,790.00 USD | 4,140.00 USD | 12.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `99.23M` | Total OI Tokens: `144,820,193.2 APT`
  * 1h OI Change: `-0.27%` | 4h OI Change: `+1.04%` | 24h OI Change: `-1.45%`
  * Exchange Breakdown: Binance=`18.81M` | Bybit=`20.22M` | OKX=`4.78M` | Hyperliquid=`3.79M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `4.35K` | Last 24h: `8.88K` | Last 3d: `10.89K` | Last 7d: `5.22K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0073%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `APT` | `47.63%` | `52.37%` | `0.91` | 4,180,000.00 USD |
| `15M` | `Binance` | `45.06%` | `54.94%` | `0.82` | 1,330,000.00 USD |
| `15M` | `OKX` | `60.83%` | `39.17%` | `1.55` | 851,320.00 USD |
| `15M` | `Bybit` | `52.69%` | `47.31%` | `1.11` | 464,960.00 USD |
| `15M` | `KuCoin` | `47.71%` | `52.29%` | `0.91` | 137,220.00 USD |
| `15M` | `Gate` | `34.84%` | `65.16%` | `0.53` | 49,650.00 USD |
| `15M` | `Bitget` | `24.03%` | `75.97%` | `0.32` | 146,080.00 USD |
| `15M` | `BingX` | `52.22%` | `47.78%` | `1.09` | 72,270.00 USD |
| `15M` | `MEXC` | `51.99%` | `48.01%` | `1.08` | 106,550.00 USD |
| `15M` | `Bitunix` | `73.64%` | `26.36%` | `2.79` | 148,190.00 USD |
| `15M` | `Hyperliquid` | `63.42%` | `36.58%` | `1.73` | 14,220.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.87%` | `53.13%` | `0.88` | 635,820.00 USD |
| `15M` | `Crypto.com` | `33.37%` | `66.63%` | `0.50` | 17.41 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 220,400.00 USD |
| `15M` | `HTX` | `70.22%` | `29.78%` | `2.36` | 575.27 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `18.51%` | `81.49%` | `0.23` | 1,210.00 USD |
| `15M` | `Aster` | `90.74%` | `9.26%` | `9.80` | 417.29 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `99.86%` | `0.14%` | `713.29` | 644.13 USD |
| `15M` | `Whale Positions` | `45.06%` | `54.94%` | `0.82` | 1,330,000.00 USD |
| `15M` | `Global Accounts` | `47.63%` | `52.37%` | `0.91` | 4,180,000.00 USD |
| `1H` | `APT` | `51.53%` | `48.47%` | `1.06` | 17,620,000.00 USD |
| `1H` | `Binance` | `53.73%` | `46.27%` | `1.16` | 6,240,000.00 USD |
| `1H` | `OKX` | `54.77%` | `45.23%` | `1.21` | 3,340,000.00 USD |
| `1H` | `Bybit` | `65.99%` | `34.01%` | `1.94` | 1,640,000.00 USD |
| `1H` | `KuCoin` | `48.78%` | `51.22%` | `0.95` | 545,530.00 USD |
| `1H` | `Gate` | `45.75%` | `54.25%` | `0.84` | 218,840.00 USD |
| `1H` | `Bitget` | `34.79%` | `65.21%` | `0.53` | 342,690.00 USD |
| `1H` | `BingX` | `46.72%` | `53.28%` | `0.88` | 630,090.00 USD |
| `1H` | `MEXC` | `50.92%` | `49.08%` | `1.04` | 408,250.00 USD |
| `1H` | `Bitunix` | `63.12%` | `36.88%` | `1.71` | 469,520.00 USD |
| `1H` | `Hyperliquid` | `54.31%` | `45.69%` | `1.19` | 76,360.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.57%` | `48.43%` | `1.06` | 2,830,000.00 USD |
| `1H` | `Crypto.com` | `50.04%` | `49.96%` | `1.00` | 40.56 USD |
| `1H` | `WhiteBIT` | `0.29%` | `99.71%` | `0.00` | 781,400.00 USD |
| `1H` | `HTX` | `64.95%` | `35.05%` | `1.85` | 4,190.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `37.79%` | `62.21%` | `0.61` | 42,240.00 USD |
| `1H` | `Aster` | `8.53%` | `91.47%` | `0.09` | 32,820.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `45.92%` | `54.08%` | `0.85` | 14,700.00 USD |
| `1H` | `Whale Positions` | `53.73%` | `46.27%` | `1.16` | 6,240,000.00 USD |
| `1H` | `Global Accounts` | `51.53%` | `48.47%` | `1.06` | 17,620,000.00 USD |
| `4H` | `APT` | `47.42%` | `52.58%` | `0.90` | 100,480,000.00 USD |
| `4H` | `Binance` | `48.68%` | `51.32%` | `0.95` | 36,110,000.00 USD |
| `4H` | `OKX` | `48.03%` | `51.97%` | `0.92` | 21,720,000.00 USD |
| `4H` | `Bybit` | `51.55%` | `48.45%` | `1.06` | 7,760,000.00 USD |
| `4H` | `KuCoin` | `49.89%` | `50.11%` | `1.00` | 2,610,000.00 USD |
| `4H` | `Gate` | `52.44%` | `47.56%` | `1.10` | 1,950,000.00 USD |
| `4H` | `Bitget` | `53.64%` | `46.36%` | `1.16` | 2,760,000.00 USD |
| `4H` | `BingX` | `36.6%` | `63.4%` | `0.58` | 2,670,000.00 USD |
| `4H` | `MEXC` | `52.77%` | `47.23%` | `1.12` | 1,370,000.00 USD |
| `4H` | `Bitunix` | `51.77%` | `48.23%` | `1.07` | 2,570,000.00 USD |
| `4H` | `Hyperliquid` | `66.59%` | `33.41%` | `1.99` | 797,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.25%` | `50.75%` | `0.97` | 16,140,000.00 USD |
| `4H` | `Crypto.com` | `26.48%` | `73.52%` | `0.36` | 387.25 USD |
| `4H` | `WhiteBIT` | `0.29%` | `99.71%` | `0.00` | 3,390,000.00 USD |
| `4H` | `HTX` | `44.64%` | `55.36%` | `0.81` | 65,460.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `47.27%` | `52.73%` | `0.90` | 298,140.00 USD |
| `4H` | `Aster` | `52.76%` | `47.24%` | `1.12` | 136,570.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.29%` | `48.71%` | `1.05` | 110,110.00 USD |
| `4H` | `Whale Positions` | `48.68%` | `51.32%` | `0.95` | 36,110,000.00 USD |
| `4H` | `Global Accounts` | `47.42%` | `52.58%` | `0.90` | 100,480,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.6922` | `0.6925` | `0.6922` | `0.6956` | `0.6901` | 688,596.56 USD | 298,303.27 USD | 390,293.30 USD | -91,990.03 USD | `-13.36%` | `4B / 12S` |
| `0:00 UTC` | `0.6973` | `0.6968` | `0.6973` | `0.6988` | `0.6909` | 545,079.30 USD | 308,821.71 USD | 236,257.59 USD | 72,564.12 USD | `+13.31%` | `17B / 10S` |
| `5:00 UTC` | `0.6990` | `0.7007` | `0.6990` | `0.7047` | `0.6974` | 804,696.05 USD | 466,627.01 USD | 338,069.04 USD | 128,557.97 USD | `+15.98%` | `21B / 12S` |
| `0:00 UTC` | `0.7013` | `0.7032` | `0.7013` | `0.7077` | `0.6997` | 1,483,040.97 USD | 758,743.98 USD | 724,296.99 USD | 34,446.99 USD | `+2.32%` | `9B / 11S` |
| `5:00 UTC` | `0.6961` | `0.6973` | `0.6961` | `0.7023` | `0.6946` | 1,215,291.53 USD | 404,512.82 USD | 810,778.71 USD | -406,265.88 USD | `-33.43%` | `8B / 18S` |
| `0:00 UTC` | `0.6948` | `0.6936` | `0.6948` | `0.6970` | `0.6912` | 798,941.07 USD | 368,954.34 USD | 429,986.74 USD | -61,032.40 USD | `-7.64%` | `6B / 6S` |
| `5:00 UTC` | `0.6923` | `0.6924` | `0.6923` | `0.6936` | `0.6913` | 552,207.56 USD | 239,483.72 USD | 312,723.84 USD | -73,240.12 USD | `-13.26%` | `1B / 2S` |
| `0:00 UTC` | `0.6888` | `0.6909` | `0.6888` | `0.6946` | `0.6875` | 808,356.30 USD | 277,065.63 USD | 531,290.67 USD | -254,225.03 USD | `-31.45%` | `8B / 26S` |
| `5:00 UTC` | `0.6872` | `0.6878` | `0.6872` | `0.6892` | `0.6863` | 391,857.65 USD | 178,103.21 USD | 213,754.44 USD | -35,651.23 USD | `-9.10%` | `2B / 6S` |
| `0:00 UTC` | `0.6890` | `0.6886` | `0.6890` | `0.6898` | `0.6865` | 105,569.97 USD | 67,655.18 USD | 37,914.79 USD | 29,740.39 USD | `+28.17%` | `8B / 3S` |

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
| `5m` | -25,220.00 USD | -2,790.00 USD | **`DISTRIBUTION`** |
| `15m` | -55,070.00 USD | 809.47 USD | **`DISTRIBUTION`** |
| `30m` | -46,340.00 USD | -475,010.00 USD | **`DISTRIBUTION`** |
| `1h` | 43,330.00 USD | -464,730.00 USD | **`DISTRIBUTION`** |
| `2h` | 188,880.00 USD | -698,070.00 USD | **`DISTRIBUTION`** |
| `4h` | 388,930.00 USD | -1,510,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 319,780.00 USD | -1,750,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 397,920.00 USD | -1,730,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 40,860.00 USD | -2,610,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -690,270.00 USD | -6,170,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -4,710,000.00 USD | -18,810,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,780,000.00 USD | -98,320,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-25.22K` | 15m=`-55.07K` | 1h=`+43.33K` | 24h=`-690.27K`
* Futures Capital Netflows: 5m=`-2.79K` | 15m=`+809.47` | 1h=`-464.73K` | 24h=`-6.17M`
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
  * `2026-10-29 23:01:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:02:06 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)


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
