# 🏛️ SOVEREIGN CANDIDATE DOSSIER: APT
**Canonical Key**: `APT` | **Broker Instrument**: `APTUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 00:59:36 IST` (`2026-10-29 19:29:36 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.6675` | `0.6696` | `0.6673` | `0.6676` | `81,403` | 54,402.23 USD | 24,237.06 USD | `+44.55%` | -3,789,224.75 USD | `+0.75` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.6676` | `0.6690` | `0.6669` | `0.6682` | `100,100` | 66,873.59 USD | 18,918.67 USD | `+28.29%` | -3,770,306.08 USD | `+0.61` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.6681` | `0.6708` | `0.6674` | `0.6706` | `194,947` | 130,520.24 USD | 35,156.12 USD | `+26.94%` | -3,735,149.96 USD | `+0.74` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.6697` | `0.6727` | `0.6676` | `0.6699` | `499,108` | 334,763.13 USD | 93,040.30 USD | `+27.79%` | -3,908,672.33 USD | `+1.41` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.6700` | `0.6703` | `0.6665` | `0.6676` | `585,854` | 391,631.76 USD | 108,139.96 USD | `+27.61%` | -3,800,532.37 USD | `+1.42` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.6676` | `0.6708` | `0.6669` | `0.6706` | `295,047` | 197,393.83 USD | 54,074.79 USD | `+27.39%` | -3,746,457.58 USD | `+0.98` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.6926` | `0.6945` | `0.6730` | `0.6795` | `4,651,736` | 3,182,247.98 USD | -755,471.85 USD | `-23.74%` | -3,493,268.47 USD | `-2.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.6796` | `0.6804` | `0.6673` | `0.6699` | `4,032,719` | 2,714,496.22 USD | -416,792.27 USD | `-15.35%` | -3,910,060.74 USD | `-0.90` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.6700` | `0.6708` | `0.6665` | `0.6706` | `880,901` | 589,025.59 USD | 162,214.75 USD | `+27.54%` | -3,747,845.99 USD | `+1.14` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.6561` | `0.6774` | `0.6549` | `0.6712` | `7,448,343` | 4,965,296.85 USD | -60,141.40 USD | `-1.21%` | -2,083,618.45 USD | `+1.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -2,231,705.21 USD | `+0.80` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6706` | `15,367,108` | 10,535,250.93 USD | -1,516,140.78 USD | `-14.39%` | -3,747,845.99 USD | `-1.70` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.7002` | `0.7012` | `0.6555` | `0.6611` | `16,465,880` | 11,061,810.70 USD | -1,103,761.29 USD | `-9.98%` | -1,656,578.37 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6611` | `0.6759` | `0.6485` | `0.6561` | `10,656,422` | 7,044,804.33 USD | -366,898.68 USD | `-5.21%` | -2,023,477.05 USD | `+0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6561` | `0.6774` | `0.6549` | `0.6712` | `7,448,343` | 4,965,296.85 USD | -60,141.40 USD | `-1.21%` | -2,083,618.45 USD | `+1.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -2,231,705.21 USD | `+0.80` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6706` | `15,367,108` | 10,535,250.93 USD | -1,516,140.78 USD | `-14.39%` | -3,747,845.99 USD | `-1.70` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:53:52 IST` |

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
| `Live` | `Long Liquidation` | `0.1465` | 152.08 USD | 259,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 269.27 USD | 258,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1935` | 107.11 USD | 258,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2035` | 2,300.00 USD | 258,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 3,620.00 USD | 256,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3155` | 1,100.00 USD | 252,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3175` | 1,590.00 USD | 251,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3185` | 9,060.00 USD | 249,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3305` | 543.58 USD | 240,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3545` | 177.25 USD | 240,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3555` | 248.85 USD | 240,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3565` | 2,140.00 USD | 239,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 189.47 USD | 237,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3675` | 194.23 USD | 237,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3735` | 933.75 USD | 237,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3805` | 3,520.00 USD | 236,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3905` | 359.26 USD | 232,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3925` | 738.43 USD | 232,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3955` | 2,640.00 USD | 231,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3995` | 271.06 USD | 229,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4005` | 516.04 USD | 228,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4015` | 406.49 USD | 228,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 570.81 USD | 228,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4135` | 1,600.00 USD | 227,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 630.86 USD | 225,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4255` | 224.96 USD | 225,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4405` | 4,300.00 USD | 225,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 226.63 USD | 220,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4515` | 27,090.00 USD | 220,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4525` | 147.06 USD | 193,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4605` | 125.38 USD | 193,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4625` | 1,100.00 USD | 193,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4685` | 468.50 USD | 192,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4705` | 8,190.00 USD | 191,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4755` | 472.63 USD | 183,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 135.33 USD | 182,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4855` | 1,010.00 USD | 182,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 3,170.00 USD | 181,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 429.90 USD | 178,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5055` | 5,760.00 USD | 178,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 102.82 USD | 172,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5095` | 2,550.00 USD | 172,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 248.05 USD | 169,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5135` | 110.50 USD | 169,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5145` | 288.78 USD | 169,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 9,440.00 USD | 169,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5315` | 11,510.00 USD | 159,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5335` | 163.22 USD | 148,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5385` | 2,690.00 USD | 147,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5445` | 330.14 USD | 145,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5495` | 630.26 USD | 144,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5545` | 47,450.00 USD | 144,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5585` | 10,520.00 USD | 96,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5615` | 1,720.00 USD | 86,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5625` | 3,280.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 164.24 USD | 81,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5715` | 289.08 USD | 81,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 214.84 USD | 80,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5785` | 662.59 USD | 80,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5805` | 20,760.00 USD | 80,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5835` | 132.92 USD | 59,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 210.96 USD | 59,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 586.80 USD | 58,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5885` | 440.16 USD | 58,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 1,690.00 USD | 57,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5910` | 2,480,000.00 USD | 2,480,000.00 USD | 3,120.00 USD | 1,560.00 USD | 15.37 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5920` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 2,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5925` | 609.14 USD | 56,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5930` | 2,470,000.00 USD | 2,470,000.00 USD | 10,090.00 USD | 0.00 USD | 9,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5935` | 572.40 USD | 55,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5945` | 3,850.00 USD | 55,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5950` | 2,450,000.00 USD | 2,450,000.00 USD | 5,120.00 USD | 0.00 USD | 4,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5960` | 2,440,000.00 USD | 2,440,000.00 USD | 5,120.00 USD | 1,640.00 USD | 46.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5970` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5975` | 157.22 USD | 51,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5980` | 2,420,000.00 USD | 2,420,000.00 USD | 7,660.00 USD | 826.53 USD | 3.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5990` | 2,120,000.00 USD | 2,120,000.00 USD | 12,180.00 USD | 2,190.00 USD | 16,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5990` | 2,410,000.00 USD | 2,410,000.00 USD | 3,320.00 USD | 1,340.00 USD | 14,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6000` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 1,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6000` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 796.28 USD | 4,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6005` | 2,460.00 USD | 51,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6010` | 2,090,000.00 USD | 2,090,000.00 USD | 735.24 USD | 461.96 USD | 6.89 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6010` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 50.15 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6020` | 2,090,000.00 USD | 2,090,000.00 USD | 7,230.00 USD | 3,830.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6020` | 2,390,000.00 USD | 2,390,000.00 USD | 4,890.00 USD | 8,040.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6030` | 2,080,000.00 USD | 2,080,000.00 USD | 1,110.00 USD | 2,940.00 USD | 3,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6030` | 2,370,000.00 USD | 2,370,000.00 USD | 2,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6040` | 2,070,000.00 USD | 2,070,000.00 USD | 4,530.00 USD | 2,320.00 USD | 1,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6040` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 3,100.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6045` | 527.44 USD | 48,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6050` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 1,750.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6060` | 2,060,000.00 USD | 2,060,000.00 USD | 2,880.00 USD | 606.70 USD | 3,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6060` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 32.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6070` | 2,050,000.00 USD | 2,050,000.00 USD | 7,700.00 USD | 1,030.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6070` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 32.69 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6080` | 2,040,000.00 USD | 2,040,000.00 USD | 2,970.00 USD | 0.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6080` | 2,360,000.00 USD | 2,360,000.00 USD | 2,860.00 USD | 0.00 USD | 124.87 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6085` | 455.69 USD | 48,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6090` | 2,030,000.00 USD | 2,030,000.00 USD | 6,430.00 USD | 0.00 USD | 47.82 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6090` | 2,360,000.00 USD | 2,360,000.00 USD | 13,920.00 USD | 0.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6100` | 2,020,000.00 USD | 2,020,000.00 USD | 3,960.00 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6100` | 2,330,000.00 USD | 2,330,000.00 USD | 7,480.00 USD | 2,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6105` | 6,090.00 USD | 47,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6110` | 2,010,000.00 USD | 2,010,000.00 USD | 1,430.00 USD | 0.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6110` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 2,210.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6115` | 5,220.00 USD | 41,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6120` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6120` | 2,310,000.00 USD | 2,310,000.00 USD | 2,100.00 USD | 3,510.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6130` | 2,010,000.00 USD | 2,010,000.00 USD | 2,140.00 USD | 596.50 USD | 1,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6130` | 2,300,000.00 USD | 2,300,000.00 USD | 8,870.00 USD | 1,050.00 USD | 4,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6140` | 2,010,000.00 USD | 2,010,000.00 USD | 6,120.00 USD | 0.00 USD | 1,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6140` | 2,280,000.00 USD | 2,280,000.00 USD | 4,540.00 USD | 7,000.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6150` | 2,000,000.00 USD | 2,000,000.00 USD | 2,730.00 USD | 0.00 USD | 30.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6150` | 2,260,000.00 USD | 2,260,000.00 USD | 11,130.00 USD | 5,870.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6160` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 1,270.00 USD | 126.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6160` | 2,240,000.00 USD | 2,240,000.00 USD | 1,790.00 USD | 2,510.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6170` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6170` | 2,230,000.00 USD | 2,230,000.00 USD | 13,260.00 USD | 2,610.00 USD | 14,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6180` | 2,200,000.00 USD | 2,200,000.00 USD | 7,600.00 USD | 1,190.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6190` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 126.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6190` | 2,190,000.00 USD | 2,190,000.00 USD | 9,560.00 USD | 1,930.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6195` | 3,170.00 USD | 36,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6200` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6200` | 2,170,000.00 USD | 2,170,000.00 USD | 13,870.00 USD | 5,230.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6210` | 1,990,000.00 USD | 1,990,000.00 USD | 1,990.00 USD | 0.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6210` | 2,140,000.00 USD | 2,140,000.00 USD | 4,760.00 USD | 1,860.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6220` | 1,990,000.00 USD | 1,990,000.00 USD | 2,520.00 USD | 0.00 USD | 7.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6220` | 2,130,000.00 USD | 2,130,000.00 USD | 7,960.00 USD | 2,310.00 USD | 29,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6230` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6230` | 2,090,000.00 USD | 2,090,000.00 USD | 9,770.00 USD | 4,700.00 USD | 8,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6235` | 3,250.00 USD | 33,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6240` | 1,980,000.00 USD | 1,980,000.00 USD | 3,220.00 USD | 3,780.00 USD | 76.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6240` | 2,070,000.00 USD | 2,070,000.00 USD | 18,610.00 USD | 4,720.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6250` | 1,970,000.00 USD | 1,970,000.00 USD | 1,800.00 USD | 2,050.00 USD | 85.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6250` | 2,040,000.00 USD | 2,040,000.00 USD | 16,120.00 USD | 3,830.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6255` | 286.65 USD | 29,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6260` | 1,970,000.00 USD | 1,970,000.00 USD | 8,920.00 USD | 751.16 USD | 2,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6260` | 2,020,000.00 USD | 2,020,000.00 USD | 20,890.00 USD | 7,660.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6265` | 10,530.00 USD | 29,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6270` | 1,960,000.00 USD | 1,960,000.00 USD | 3,700.00 USD | 3,940.00 USD | 12,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6270` | 1,960,000.00 USD | 1,960,000.00 USD | 17,460.00 USD | 8,200.00 USD | 24,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6280` | 1,940,000.00 USD | 1,940,000.00 USD | 11,690.00 USD | 463.43 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6280` | 1,910,000.00 USD | 1,910,000.00 USD | 9,160.00 USD | 9,230.00 USD | 16,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6285` | 903.47 USD | 19,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6290` | 1,920,000.00 USD | 1,920,000.00 USD | 11,890.00 USD | 1,200.00 USD | 5,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6290` | 1,880,000.00 USD | 1,880,000.00 USD | 17,710.00 USD | 6,740.00 USD | 10,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6300` | 1,910,000.00 USD | 1,910,000.00 USD | 12,950.00 USD | 2,470.00 USD | 2,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6300` | 1,840,000.00 USD | 1,840,000.00 USD | 10,040.00 USD | 7,890.00 USD | 11,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6310` | 1,890,000.00 USD | 1,890,000.00 USD | 7,940.00 USD | 5,110.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6310` | 1,810,000.00 USD | 1,810,000.00 USD | 19,340.00 USD | 4,520.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6315` | 1,010.00 USD | 18,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6320` | 1,870,000.00 USD | 1,870,000.00 USD | 12,320.00 USD | 11,080.00 USD | 14,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6320` | 1,770,000.00 USD | 1,770,000.00 USD | 4,880.00 USD | 12,650.00 USD | 8,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6330` | 1,830,000.00 USD | 1,830,000.00 USD | 17,300.00 USD | 3,580.00 USD | 21,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6330` | 1,750,000.00 USD | 1,750,000.00 USD | 57,940.00 USD | 14,700.00 USD | 33,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6340` | 1,790,000.00 USD | 1,790,000.00 USD | 9,830.00 USD | 2,020.00 USD | 15,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6340` | 1,640,000.00 USD | 1,640,000.00 USD | 10,730.00 USD | 3,420.00 USD | 4,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6350` | 1,760,000.00 USD | 1,760,000.00 USD | 19,180.00 USD | 8,820.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6350` | 1,620,000.00 USD | 1,620,000.00 USD | 14,450.00 USD | 2,430.00 USD | 23,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6360` | 1,730,000.00 USD | 1,730,000.00 USD | 30,350.00 USD | 9,150.00 USD | 33,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6360` | 1,580,000.00 USD | 1,580,000.00 USD | 42,690.00 USD | 7,300.00 USD | 40,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6370` | 1,660,000.00 USD | 1,660,000.00 USD | 21,750.00 USD | 4,510.00 USD | 27,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6370` | 1,490,000.00 USD | 1,490,000.00 USD | 49,080.00 USD | 4,870.00 USD | 29.01 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6375` | 5,900.00 USD | 17,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6380` | 1,600,000.00 USD | 1,600,000.00 USD | 19,430.00 USD | 7,180.00 USD | 7,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6380` | 1,440,000.00 USD | 1,440,000.00 USD | 18,140.00 USD | 3,870.00 USD | 30,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6390` | 1,570,000.00 USD | 1,570,000.00 USD | 18,790.00 USD | 529.57 USD | 6,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6390` | 1,380,000.00 USD | 1,380,000.00 USD | 10,200.00 USD | 7,510.00 USD | 13,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6400` | 1,540,000.00 USD | 1,540,000.00 USD | 9,830.00 USD | 9,970.00 USD | 25,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6400` | 1,350,000.00 USD | 1,350,000.00 USD | 15,560.00 USD | 0.00 USD | 330.78 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6410` | 1,500,000.00 USD | 1,500,000.00 USD | 20,930.00 USD | 2,240.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6410` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 6,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6415` | 4,740.00 USD | 11,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6420` | 1,470,000.00 USD | 1,470,000.00 USD | 43,840.00 USD | 12,930.00 USD | 12,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6420` | 1,330,000.00 USD | 1,330,000.00 USD | 47,150.00 USD | 26,560.00 USD | 10,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6430` | 1,400,000.00 USD | 1,400,000.00 USD | 25,620.00 USD | 9,880.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6430` | 1,250,000.00 USD | 1,250,000.00 USD | 16,200.00 USD | 7,140.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6435` | 2,320.00 USD | 6,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6440` | 1,350,000.00 USD | 1,350,000.00 USD | 24,780.00 USD | 14,720.00 USD | 8,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6440` | 1,220,000.00 USD | 1,220,000.00 USD | 14,160.00 USD | 17,680.00 USD | 14,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6450` | 1,310,000.00 USD | 1,310,000.00 USD | 26,090.00 USD | 22,940.00 USD | 34,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6450` | 1,170,000.00 USD | 1,170,000.00 USD | 14,120.00 USD | 15,560.00 USD | 383.87 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6455` | 3,730.00 USD | 4,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6460` | 1,220,000.00 USD | 1,220,000.00 USD | 43,360.00 USD | 11,650.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6460` | 1,140,000.00 USD | 1,140,000.00 USD | 82,710.00 USD | 14,300.00 USD | 75,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6470` | 1,120,000.00 USD | 1,120,000.00 USD | 46,150.00 USD | 6,620.00 USD | 41,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6470` | 972,110.00 USD | 972,110.00 USD | 9,660.00 USD | 3,880.00 USD | 9,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6480` | 1,020,000.00 USD | 1,020,000.00 USD | 48,130.00 USD | 14,180.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6480` | 949,350.00 USD | 949,350.00 USD | 37,050.00 USD | 0.00 USD | 23,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6485` | 259.68 USD | 412.77 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6490` | 951,630.00 USD | 951,630.00 USD | 31,930.00 USD | 3,800.00 USD | 51,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6490` | 888,520.00 USD | 888,520.00 USD | 36,340.00 USD | 0.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6500` | 864,500.00 USD | 864,500.00 USD | 53,070.00 USD | 1,390.00 USD | 35,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6500` | 834,530.00 USD | 834,530.00 USD | 37,220.00 USD | 0.00 USD | 81,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6510` | 774,620.00 USD | 774,620.00 USD | 18,580.00 USD | 4,450.00 USD | 61,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6510` | 715,660.00 USD | 715,660.00 USD | 101,440.00 USD | 4,190.00 USD | 288.03 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6520` | 690,480.00 USD | 690,480.00 USD | 36,270.00 USD | 6,190.00 USD | 14,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6520` | 609,740.00 USD | 609,740.00 USD | 46,620.00 USD | 6,720.00 USD | 86,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6530` | 633,900.00 USD | 633,900.00 USD | 5,780.00 USD | 1,060.00 USD | 11,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6530` | 469,840.00 USD | 469,840.00 USD | 0.00 USD | 0.00 USD | 47,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6535` | 153.10 USD | 153.10 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6540` | 615,340.00 USD | 615,340.00 USD | 11,450.00 USD | 2,530.00 USD | 8,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6540` | 422,740.00 USD | 422,740.00 USD | 15,730.00 USD | 0.00 USD | 14,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6550` | 593,240.00 USD | 593,240.00 USD | 18,980.00 USD | 3,640.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6550` | 392,370.00 USD | 392,370.00 USD | 0.00 USD | 0.00 USD | 38,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6560` | 553,350.00 USD | 553,350.00 USD | 46,280.00 USD | 13,960.00 USD | 25,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6560` | 353,940.00 USD | 353,940.00 USD | 23,390.00 USD | 5,380.00 USD | 34,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6570` | 468,050.00 USD | 468,050.00 USD | 5,570.00 USD | 6,680.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6570` | 290,430.00 USD | 290,430.00 USD | 14,440.00 USD | 6,350.00 USD | 10,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6580` | 436,010.00 USD | 436,010.00 USD | 11,870.00 USD | 6,780.00 USD | 30.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6580` | 258,990.00 USD | 258,990.00 USD | 0.00 USD | 21,920.00 USD | 12,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6590` | 417,330.00 USD | 417,330.00 USD | 8,070.00 USD | 11,260.00 USD | 25,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6590` | 224,420.00 USD | 224,420.00 USD | 9,540.00 USD | 0.00 USD | 331.05 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6600` | 372,310.00 USD | 372,310.00 USD | 21,900.00 USD | 5,170.00 USD | 22,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6600` | 214,540.00 USD | 214,540.00 USD | 15,310.00 USD | 4,180.00 USD | 20,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6610` | 322,630.00 USD | 322,630.00 USD | 42,960.00 USD | 2,560.00 USD | 12,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6620` | 264,940.00 USD | 264,940.00 USD | 22,690.00 USD | 2,480.00 USD | 36,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6620` | 174,820.00 USD | 174,820.00 USD | 14,320.00 USD | 0.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6630` | 202,780.00 USD | 202,780.00 USD | 45,660.00 USD | 4,110.00 USD | 7,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6630` | 153,370.00 USD | 153,370.00 USD | 49,490.00 USD | 0.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6640` | 145,610.00 USD | 145,610.00 USD | 22,290.00 USD | 1,150.00 USD | 35,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6640` | 75,070.00 USD | 75,070.00 USD | 15,140.00 USD | 0.00 USD | 279.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6650` | 87,110.00 USD | 87,110.00 USD | 22,590.00 USD | 10,330.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6650` | 59,650.00 USD | 59,650.00 USD | 14,220.00 USD | 6,770.00 USD | 29,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6660` | 39,900.00 USD | 39,900.00 USD | 7,730.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6660` | 8,930.00 USD | 8,930.00 USD | 0.00 USD | 0.00 USD | 148.18 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6670` | 26,760.00 USD | 26,760.00 USD | 18,850.00 USD | 2,980.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6670` | 8,780.00 USD | 8,780.00 USD | 0.00 USD | 0.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6690` | 24,430.00 USD | 24,430.00 USD | 0.00 USD | 0.00 USD | 24,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6690` | 48,860.00 USD | 48,860.00 USD | 0.00 USD | 0.00 USD | 24,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6700` | 4,190.00 USD | 4,190.00 USD | 0.00 USD | 0.00 USD | 4,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6700` | 49,180.00 USD | 49,180.00 USD | 0.00 USD | 0.00 USD | 323.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6710` | 74,200.00 USD | 74,200.00 USD | 0.00 USD | 0.00 USD | 25,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6720` | 21,340.00 USD | 21,340.00 USD | 0.00 USD | 0.00 USD | 17,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6730` | 34,170.00 USD | 34,170.00 USD | 5,220.00 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6730` | 74,300.00 USD | 74,300.00 USD | 0.00 USD | 0.00 USD | 99.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6740` | 41,280.00 USD | 41,280.00 USD | 0.00 USD | 4,800.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6750` | 47,260.00 USD | 47,260.00 USD | 0.00 USD | 5,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6750` | 150,030.00 USD | 150,030.00 USD | 0.00 USD | 75,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6760` | 49,890.00 USD | 49,890.00 USD | 0.00 USD | 2,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6760` | 152,270.00 USD | 152,270.00 USD | 0.00 USD | 2,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6770` | 52,550.00 USD | 52,550.00 USD | 0.00 USD | 2,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6770` | 156,450.00 USD | 156,450.00 USD | 0.00 USD | 4,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6780` | 65,190.00 USD | 65,190.00 USD | 0.00 USD | 12,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6780` | 166,670.00 USD | 166,670.00 USD | 0.00 USD | 10,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6790` | 98,000.00 USD | 98,000.00 USD | 0.00 USD | 18,610.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6790` | 183,260.00 USD | 183,260.00 USD | 0.00 USD | 16,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6810` | 105,580.00 USD | 105,580.00 USD | 0.00 USD | 0.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6810` | 198,980.00 USD | 198,980.00 USD | 0.00 USD | 15,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6820` | 143,260.00 USD | 143,260.00 USD | 22,600.00 USD | 10,160.00 USD | 4,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6820` | 252,880.00 USD | 252,880.00 USD | 16,170.00 USD | 37,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6830` | 194,050.00 USD | 194,050.00 USD | 0.00 USD | 25,100.00 USD | 25,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6830` | 312,160.00 USD | 312,160.00 USD | 0.00 USD | 11,020.00 USD | 48,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6840` | 237,670.00 USD | 237,670.00 USD | 12,500.00 USD | 22,740.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6840` | 387,830.00 USD | 387,830.00 USD | 0.00 USD | 36,580.00 USD | 39,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6850` | 301,720.00 USD | 301,720.00 USD | 52,450.00 USD | 5,780.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6850` | 392,540.00 USD | 392,540.00 USD | 0.00 USD | 4,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6860` | 304,050.00 USD | 304,050.00 USD | 0.00 USD | 2,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6860` | 417,690.00 USD | 417,690.00 USD | 15,310.00 USD | 9,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6870` | 335,110.00 USD | 335,110.00 USD | 31,040.00 USD | 0.00 USD | 15.30 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6880` | 373,490.00 USD | 373,490.00 USD | 0.00 USD | 9,600.00 USD | 28,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6880` | 453,150.00 USD | 453,150.00 USD | 18,170.00 USD | 17,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6890` | 376,240.00 USD | 376,240.00 USD | 0.00 USD | 0.00 USD | 2,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6890` | 464,190.00 USD | 464,190.00 USD | 0.00 USD | 11,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6900` | 405,950.00 USD | 405,950.00 USD | 8,650.00 USD | 0.00 USD | 21,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6900` | 468,670.00 USD | 468,670.00 USD | 0.00 USD | 4,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6910` | 460,150.00 USD | 460,150.00 USD | 21,590.00 USD | 0.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6910` | 537,260.00 USD | 537,260.00 USD | 37,820.00 USD | 2,090.00 USD | 28,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6920` | 473,830.00 USD | 473,830.00 USD | 0.00 USD | 0.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6920` | 561,630.00 USD | 561,630.00 USD | 0.00 USD | 0.00 USD | 24,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6930` | 484,030.00 USD | 484,030.00 USD | 10,030.00 USD | 0.00 USD | 168.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6930` | 618,460.00 USD | 618,460.00 USD | 14,220.00 USD | 0.00 USD | 42,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6940` | 507,910.00 USD | 507,910.00 USD | 11,230.00 USD | 4,420.00 USD | 8,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6950` | 538,650.00 USD | 538,650.00 USD | 22,480.00 USD | 4,460.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6950` | 662,300.00 USD | 662,300.00 USD | 31,450.00 USD | 0.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6960` | 602,090.00 USD | 602,090.00 USD | 58,370.00 USD | 5,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6960` | 682,600.00 USD | 682,600.00 USD | 20,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6970` | 627,930.00 USD | 627,930.00 USD | 23,380.00 USD | 2,430.00 USD | 34.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6970` | 707,430.00 USD | 707,430.00 USD | 21,650.00 USD | 3,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6980` | 634,330.00 USD | 634,330.00 USD | 3,000.00 USD | 3,390.00 USD | 17.79 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6980` | 718,400.00 USD | 718,400.00 USD | 0.00 USD | 10,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6990` | 645,090.00 USD | 645,090.00 USD | 2,990.00 USD | 4,830.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6990` | 748,130.00 USD | 748,130.00 USD | 4,770.00 USD | 0.00 USD | 24,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7000` | 663,560.00 USD | 663,560.00 USD | 4,190.00 USD | 3,290.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7000` | 765,770.00 USD | 765,770.00 USD | 7,660.00 USD | 0.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7010` | 679,130.00 USD | 679,130.00 USD | 15,520.00 USD | 0.00 USD | 56.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7010` | 765,920.00 USD | 765,920.00 USD | 0.00 USD | 0.00 USD | 150.46 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7020` | 693,510.00 USD | 693,510.00 USD | 14,360.00 USD | 0.00 USD | 22.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7020` | 835,350.00 USD | 835,350.00 USD | 16,350.00 USD | 0.00 USD | 53,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7030` | 708,350.00 USD | 708,350.00 USD | 4,330.00 USD | 0.00 USD | 10,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7030` | 962,430.00 USD | 962,430.00 USD | 76,610.00 USD | 0.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7040` | 758,800.00 USD | 758,800.00 USD | 29,930.00 USD | 2,630.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7040` | 1,030,000.00 USD | 1,030,000.00 USD | 18,910.00 USD | 0.00 USD | 45,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7050` | 816,630.00 USD | 816,630.00 USD | 36,240.00 USD | 2,660.00 USD | 18,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7050` | 1,180,000.00 USD | 1,180,000.00 USD | 27,630.00 USD | 0.00 USD | 123,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7060` | 841,430.00 USD | 841,430.00 USD | 8,590.00 USD | 3,860.00 USD | 12,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7060` | 1,290,000.00 USD | 1,290,000.00 USD | 20,200.00 USD | 33,490.00 USD | 54,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7070` | 900,430.00 USD | 900,430.00 USD | 19,980.00 USD | 21,860.00 USD | 17,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7070` | 1,360,000.00 USD | 1,360,000.00 USD | 8,720.00 USD | 36,300.00 USD | 28,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7075` | 2,220.00 USD | 2,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7080` | 926,660.00 USD | 926,660.00 USD | 18,420.00 USD | 3,500.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7080` | 1,460,000.00 USD | 1,460,000.00 USD | 15,730.00 USD | 28,570.00 USD | 53,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7090` | 956,300.00 USD | 956,300.00 USD | 17,580.00 USD | 3,160.00 USD | 8,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7090` | 1,730,000.00 USD | 1,730,000.00 USD | 106,000.00 USD | 32,830.00 USD | 134,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7100` | 971,340.00 USD | 971,340.00 USD | 8,730.00 USD | 1,280.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7100` | 1,820,000.00 USD | 1,820,000.00 USD | 44,820.00 USD | 30,700.00 USD | 14,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7110` | 991,440.00 USD | 991,440.00 USD | 2,660.00 USD | 8,760.00 USD | 8,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7110` | 1,990,000.00 USD | 1,990,000.00 USD | 40,300.00 USD | 33,410.00 USD | 92,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7120` | 1,030,000.00 USD | 1,030,000.00 USD | 21,700.00 USD | 4,410.00 USD | 15,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7120` | 2,230,000.00 USD | 2,230,000.00 USD | 60,730.00 USD | 45,350.00 USD | 135,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7125` | 632.02 USD | 2,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7130` | 1,100,000.00 USD | 1,100,000.00 USD | 28,640.00 USD | 3,110.00 USD | 39,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7130` | 2,390,000.00 USD | 2,390,000.00 USD | 75,250.00 USD | 31,940.00 USD | 51,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7140` | 1,150,000.00 USD | 1,150,000.00 USD | 27,390.00 USD | 7,490.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7140` | 2,630,000.00 USD | 2,630,000.00 USD | 127,300.00 USD | 35,310.00 USD | 81,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7150` | 1,190,000.00 USD | 1,190,000.00 USD | 18,260.00 USD | 6,980.00 USD | 23,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7150` | 2,810,000.00 USD | 2,810,000.00 USD | 50,460.00 USD | 26,770.00 USD | 96,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7160` | 1,230,000.00 USD | 1,230,000.00 USD | 17,400.00 USD | 11,180.00 USD | 10,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7160` | 2,970,000.00 USD | 2,970,000.00 USD | 62,580.00 USD | 38,490.00 USD | 68,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7170` | 1,250,000.00 USD | 1,250,000.00 USD | 4,910.00 USD | 3,880.00 USD | 8,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7170` | 3,170,000.00 USD | 3,170,000.00 USD | 105,890.00 USD | 35,770.00 USD | 53,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7180` | 1,280,000.00 USD | 1,280,000.00 USD | 6,240.00 USD | 2,890.00 USD | 14,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7180` | 3,260,000.00 USD | 3,260,000.00 USD | 59,980.00 USD | 21,140.00 USD | 12,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7190` | 1,300,000.00 USD | 1,300,000.00 USD | 12,780.00 USD | 8,180.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7190` | 3,390,000.00 USD | 3,390,000.00 USD | 28,670.00 USD | 11,840.00 USD | 87,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7200` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 4,740.00 USD | 12,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7200` | 3,580,000.00 USD | 3,580,000.00 USD | 65,080.00 USD | 33,310.00 USD | 89,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7210` | 1,350,000.00 USD | 1,350,000.00 USD | 10,550.00 USD | 13,350.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7210` | 3,880,000.00 USD | 3,880,000.00 USD | 206,240.00 USD | 24,720.00 USD | 70,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7220` | 1,390,000.00 USD | 1,390,000.00 USD | 20,300.00 USD | 3,610.00 USD | 23,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7220` | 4,060,000.00 USD | 4,060,000.00 USD | 112,190.00 USD | 42,410.00 USD | 27,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7230` | 1,410,000.00 USD | 1,410,000.00 USD | 1,140.00 USD | 2,670.00 USD | 15,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7230` | 4,230,000.00 USD | 4,230,000.00 USD | 59,050.00 USD | 10,400.00 USD | 93,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7240` | 1,420,000.00 USD | 1,420,000.00 USD | 2,920.00 USD | 3,290.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7240` | 4,350,000.00 USD | 4,350,000.00 USD | 75,360.00 USD | 14,510.00 USD | 28,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7250` | 1,440,000.00 USD | 1,440,000.00 USD | 4,760.00 USD | 3,950.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7250` | 4,510,000.00 USD | 4,510,000.00 USD | 52,270.00 USD | 25,530.00 USD | 82,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7255` | 43,950.00 USD | 46,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7260` | 1,470,000.00 USD | 1,470,000.00 USD | 11,880.00 USD | 6,730.00 USD | 12,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7260` | 4,680,000.00 USD | 4,680,000.00 USD | 54,140.00 USD | 26,590.00 USD | 93,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7270` | 1,510,000.00 USD | 1,510,000.00 USD | 19,920.00 USD | 2,760.00 USD | 14,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7270` | 4,780,000.00 USD | 4,780,000.00 USD | 49,240.00 USD | 18,120.00 USD | 33,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7280` | 1,540,000.00 USD | 1,540,000.00 USD | 16,410.00 USD | 5,780.00 USD | 11,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7280` | 4,900,000.00 USD | 4,900,000.00 USD | 42,560.00 USD | 22,060.00 USD | 50,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7290` | 1,590,000.00 USD | 1,590,000.00 USD | 13,150.00 USD | 7,110.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7290` | 5,050,000.00 USD | 5,050,000.00 USD | 47,200.00 USD | 32,380.00 USD | 69,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7300` | 1,640,000.00 USD | 1,640,000.00 USD | 9,980.00 USD | 9,840.00 USD | 25,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7300` | 5,160,000.00 USD | 5,160,000.00 USD | 55,390.00 USD | 27,940.00 USD | 29,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7310` | 1,650,000.00 USD | 1,650,000.00 USD | 1,010.00 USD | 1,670.00 USD | 7,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7310` | 5,350,000.00 USD | 5,350,000.00 USD | 115,470.00 USD | 40,620.00 USD | 31,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7320` | 1,670,000.00 USD | 1,670,000.00 USD | 5,780.00 USD | 1,140.00 USD | 12,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7320` | 5,490,000.00 USD | 5,490,000.00 USD | 74,380.00 USD | 25,020.00 USD | 49,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7330` | 1,680,000.00 USD | 1,680,000.00 USD | 6,450.00 USD | 3,420.00 USD | 4,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7330` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 32,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7340` | 1,690,000.00 USD | 1,690,000.00 USD | 1,620.00 USD | 1,530.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7340` | 5,600,000.00 USD | 5,600,000.00 USD | 31,260.00 USD | 8,620.00 USD | 30,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7345` | 150.17 USD | 46,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7350` | 1,690,000.00 USD | 1,690,000.00 USD | 735.24 USD | 1,470.00 USD | 31.79 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7350` | 5,700,000.00 USD | 5,700,000.00 USD | 66,390.00 USD | 15,820.00 USD | 15,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7360` | 1,720,000.00 USD | 1,720,000.00 USD | 14,020.00 USD | 4,990.00 USD | 14,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7360` | 5,780,000.00 USD | 5,780,000.00 USD | 37,210.00 USD | 30,980.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7370` | 1,740,000.00 USD | 1,740,000.00 USD | 1,110.00 USD | 2,940.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7370` | 5,820,000.00 USD | 5,820,000.00 USD | 9,640.00 USD | 3,860.00 USD | 20,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7380` | 1,750,000.00 USD | 1,750,000.00 USD | 4,530.00 USD | 2,320.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7380` | 5,930,000.00 USD | 5,930,000.00 USD | 58,340.00 USD | 16,760.00 USD | 39,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7390` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 2,330.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7390` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 8,110.00 USD | 25,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7400` | 1,760,000.00 USD | 1,760,000.00 USD | 2,880.00 USD | 2,520.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7400` | 5,990,000.00 USD | 5,990,000.00 USD | 1,730.00 USD | 6,500.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7410` | 1,770,000.00 USD | 1,770,000.00 USD | 7,700.00 USD | 1,030.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7410` | 6,080,000.00 USD | 6,080,000.00 USD | 28,380.00 USD | 30,100.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7420` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 3.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7420` | 6,100,000.00 USD | 6,100,000.00 USD | 7,430.00 USD | 13,420.00 USD | 427.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7430` | 1,770,000.00 USD | 1,770,000.00 USD | 1,240.00 USD | 0.00 USD | 125.56 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7430` | 6,210,000.00 USD | 6,210,000.00 USD | 46,330.00 USD | 13,970.00 USD | 54,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7440` | 1,780,000.00 USD | 1,780,000.00 USD | 1,730.00 USD | 718.40 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7440` | 6,280,000.00 USD | 6,280,000.00 USD | 28,120.00 USD | 25,920.00 USD | 15,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7450` | 1,800,000.00 USD | 1,800,000.00 USD | 6,430.00 USD | 1,170.00 USD | 6,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7450` | 6,390,000.00 USD | 6,390,000.00 USD | 50,150.00 USD | 16,360.00 USD | 38,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7460` | 1,810,000.00 USD | 1,810,000.00 USD | 3,960.00 USD | 0.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7460` | 6,450,000.00 USD | 6,450,000.00 USD | 38,650.00 USD | 10,350.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7470` | 1,810,000.00 USD | 1,810,000.00 USD | 1,430.00 USD | 0.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7470` | 6,540,000.00 USD | 6,540,000.00 USD | 35,630.00 USD | 18,610.00 USD | 34,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7480` | 1,820,000.00 USD | 1,820,000.00 USD | 3,230.00 USD | 0.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7480` | 6,580,000.00 USD | 6,580,000.00 USD | 24,950.00 USD | 10,290.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7490` | 1,820,000.00 USD | 1,820,000.00 USD | 2,140.00 USD | 596.50 USD | 995.01 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7490` | 6,610,000.00 USD | 6,610,000.00 USD | 17,270.00 USD | 5,180.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7500` | 1,830,000.00 USD | 1,830,000.00 USD | 6,120.00 USD | 0.00 USD | 984.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7500` | 6,670,000.00 USD | 6,670,000.00 USD | 35,050.00 USD | 7,430.00 USD | 16,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7510` | 1,830,000.00 USD | 1,830,000.00 USD | 2,730.00 USD | 0.00 USD | 15.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7510` | 6,730,000.00 USD | 6,730,000.00 USD | 25,900.00 USD | 5,870.00 USD | 35,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7520` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 1,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7520` | 6,780,000.00 USD | 6,780,000.00 USD | 27,570.00 USD | 7,130.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7530` | 6,820,000.00 USD | 6,820,000.00 USD | 21,290.00 USD | 1,890.00 USD | 14,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7540` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 40.37 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7540` | 6,840,000.00 USD | 6,840,000.00 USD | 9,060.00 USD | 0.00 USD | 10,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7550` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7550` | 6,890,000.00 USD | 6,890,000.00 USD | 18,390.00 USD | 6,470.00 USD | 19,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7560` | 6,900,000.00 USD | 6,900,000.00 USD | 7,600.00 USD | 1,100.00 USD | 2,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7570` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 11.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7570` | 6,960,000.00 USD | 6,960,000.00 USD | 29,140.00 USD | 4,260.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7580` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 1,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7580` | 7,010,000.00 USD | 7,010,000.00 USD | 26,280.00 USD | 7,530.00 USD | 12,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7590` | 1,840,000.00 USD | 1,840,000.00 USD | 1,990.00 USD | 0.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7590` | 7,080,000.00 USD | 7,080,000.00 USD | 34,970.00 USD | 717.68 USD | 32,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7600` | 1,840,000.00 USD | 1,840,000.00 USD | 2,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7600` | 7,150,000.00 USD | 7,150,000.00 USD | 22,050.00 USD | 3,600.00 USD | 47,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7610` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7610` | 7,190,000.00 USD | 7,190,000.00 USD | 14,110.00 USD | 8,700.00 USD | 16,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7620` | 7,250,000.00 USD | 7,250,000.00 USD | 40,030.00 USD | 15,470.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7630` | 7,320,000.00 USD | 7,320,000.00 USD | 33,960.00 USD | 13,520.00 USD | 22,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7635` | 143.11 USD | 47,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7640` | 7,360,000.00 USD | 7,360,000.00 USD | 16,430.00 USD | 0.00 USD | 18,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7650` | 7,490,000.00 USD | 7,490,000.00 USD | 43,020.00 USD | 9,740.00 USD | 79,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7660` | 7,520,000.00 USD | 7,520,000.00 USD | 13,100.00 USD | 8,390.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7670` | 7,600,000.00 USD | 7,600,000.00 USD | 32,170.00 USD | 17,130.00 USD | 24,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7680` | 7,660,000.00 USD | 7,660,000.00 USD | 34,410.00 USD | 15,390.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7690` | 7,680,000.00 USD | 7,680,000.00 USD | 5,320.00 USD | 2,840.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7700` | 7,730,000.00 USD | 7,730,000.00 USD | 5,540.00 USD | 9,750.00 USD | 31,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7710` | 7,820,000.00 USD | 7,820,000.00 USD | 53,500.00 USD | 19,240.00 USD | 17,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7720` | 7,850,000.00 USD | 7,850,000.00 USD | 4,880.00 USD | 13,680.00 USD | 8,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7725` | 165.62 USD | 47,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7730` | 7,910,000.00 USD | 7,910,000.00 USD | 37,120.00 USD | 14,120.00 USD | 12,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7740` | 7,960,000.00 USD | 7,960,000.00 USD | 14,480.00 USD | 11,130.00 USD | 23,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7750` | 7,970,000.00 USD | 7,970,000.00 USD | 5,090.00 USD | 0.00 USD | 7,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7760` | 8,010,000.00 USD | 8,010,000.00 USD | 33,080.00 USD | 2,980.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7765` | 330.78 USD | 47,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7770` | 8,060,000.00 USD | 8,060,000.00 USD | 15,750.00 USD | 15,940.00 USD | 19,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7780` | 8,130,000.00 USD | 8,130,000.00 USD | 53,050.00 USD | 4,910.00 USD | 13,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7790` | 8,170,000.00 USD | 8,170,000.00 USD | 11,330.00 USD | 2,770.00 USD | 22,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7800` | 8,310,000.00 USD | 8,310,000.00 USD | 49,160.00 USD | 19,160.00 USD | 72,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7810` | 8,370,000.00 USD | 8,370,000.00 USD | 49,880.00 USD | 5,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7820` | 8,430,000.00 USD | 8,430,000.00 USD | 40,140.00 USD | 12,700.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7830` | 8,510,000.00 USD | 8,510,000.00 USD | 70,580.00 USD | 6,240.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7840` | 8,530,000.00 USD | 8,530,000.00 USD | 24,790.00 USD | 0.00 USD | 12.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8005` | 19,120.00 USD | 66,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8035` | 114.11 USD | 66,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8615` | 15,640.00 USD | 82,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8665` | 378.95 USD | 82,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9935` | 166.01 USD | 83,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.00` | 21,080.00 USD | 104,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.06` | 18,720.00 USD | 122,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 82,670.00 USD | 205,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 3,080.00 USD | 208,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 479.74 USD | 209,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.12` | 2,800.00 USD | 211,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.27` | 13,320.00 USD | 225,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 197.51 USD | 225,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 284.61 USD | 225,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1465` | 259,100.00 USD | 0.00 USD | 152.08 USD | `-78.15%` | `1,038.12` |
| `Live` | `Long` | `0.1875` | 258,950.00 USD | 0.00 USD | 269.27 USD | `-72.03%` | `1,436.09` |
| `Live` | `Long` | `0.1935` | 258,680.00 USD | 0.00 USD | 107.11 USD | `-71.14%` | `553.52` |
| `Live` | `Long` | `0.2035` | 258,570.00 USD | 0.00 USD | 2,300.00 USD | `-69.64%` | `11,284.25` |
| `Live` | `Long` | `0.2915` | 256,280.00 USD | 0.00 USD | 3,620.00 USD | `-56.52%` | `12,426.15` |
| `Live` | `Long` | `0.3155` | 252,650.00 USD | 0.00 USD | 1,100.00 USD | `-52.94%` | `3,500.00` |
| `Live` | `Long` | `0.3175` | 251,550.00 USD | 0.00 USD | 1,590.00 USD | `-52.64%` | `5,000.00` |
| `Live` | `Long` | `0.3185` | 249,960.00 USD | 0.00 USD | 9,060.00 USD | `-52.49%` | `28,446.85` |
| `Live` | `Long` | `0.3305` | 240,900.00 USD | 0.00 USD | 543.58 USD | `-50.70%` | `1,644.73` |
| `Live` | `Long` | `0.3545` | 240,360.00 USD | 0.00 USD | 177.25 USD | `-47.12%` | `500.00` |
| `Live` | `Long` | `0.3555` | 240,180.00 USD | 0.00 USD | 248.85 USD | `-46.97%` | `700.00` |
| `Live` | `Long` | `0.3565` | 239,930.00 USD | 0.00 USD | 2,140.00 USD | `-46.82%` | `6,000.00` |
| `Live` | `Long` | `0.3665` | 237,790.00 USD | 0.00 USD | 189.47 USD | `-45.33%` | `516.98` |
| `Live` | `Long` | `0.3675` | 237,600.00 USD | 0.00 USD | 194.23 USD | `-45.18%` | `528.52` |
| `Live` | `Long` | `0.3735` | 237,410.00 USD | 0.00 USD | 933.75 USD | `-44.29%` | `2,500.00` |
| `Live` | `Long` | `0.3805` | 236,480.00 USD | 0.00 USD | 3,520.00 USD | `-43.24%` | `9,243.24` |
| `Live` | `Long` | `0.3905` | 232,960.00 USD | 0.00 USD | 359.26 USD | `-41.75%` | `919.99` |
| `Live` | `Long` | `0.3925` | 232,600.00 USD | 0.00 USD | 738.43 USD | `-41.45%` | `1,881.36` |
| `Live` | `Long` | `0.3955` | 231,860.00 USD | 0.00 USD | 2,640.00 USD | `-41.01%` | `6,686.27` |
| `Live` | `Long` | `0.3995` | 229,220.00 USD | 0.00 USD | 271.06 USD | `-40.41%` | `678.49` |
| `Live` | `Long` | `0.4005` | 228,950.00 USD | 0.00 USD | 516.04 USD | `-40.26%` | `1,288.49` |
| `Live` | `Long` | `0.4015` | 228,430.00 USD | 0.00 USD | 406.49 USD | `-40.11%` | `1,012.44` |
| `Live` | `Long` | `0.4035` | 228,020.00 USD | 0.00 USD | 570.81 USD | `-39.81%` | `1,414.65` |
| `Live` | `Long` | `0.4135` | 227,450.00 USD | 0.00 USD | 1,600.00 USD | `-38.32%` | `3,868.97` |
| `Live` | `Long` | `0.4185` | 225,850.00 USD | 0.00 USD | 630.86 USD | `-37.57%` | `1,507.44` |
| `Live` | `Long` | `0.4255` | 225,220.00 USD | 0.00 USD | 224.96 USD | `-36.53%` | `528.69` |
| `Live` | `Long` | `0.4405` | 225,000.00 USD | 0.00 USD | 4,300.00 USD | `-34.29%` | `9,753.33` |
| `Live` | `Long` | `0.4475` | 220,700.00 USD | 0.00 USD | 226.63 USD | `-33.25%` | `506.43` |
| `Live` | `Long` | `0.4515` | 220,470.00 USD | 0.00 USD | 27,090.00 USD | `-32.65%` | `60,000.00` |
| `Live` | `Long` | `0.4525` | 193,380.00 USD | 0.00 USD | 147.06 USD | `-32.50%` | `325.00` |
| `Live` | `Long` | `0.4605` | 193,240.00 USD | 0.00 USD | 125.38 USD | `-31.31%` | `272.27` |
| `Live` | `Long` | `0.4625` | 193,110.00 USD | 0.00 USD | 1,100.00 USD | `-31.01%` | `2,368.95` |
| `Live` | `Long` | `0.4685` | 192,020.00 USD | 0.00 USD | 468.50 USD | `-30.12%` | `1,000.00` |
| `Live` | `Long` | `0.4705` | 191,550.00 USD | 0.00 USD | 8,190.00 USD | `-29.82%` | `17,402.53` |
| `Live` | `Long` | `0.4755` | 183,360.00 USD | 0.00 USD | 472.63 USD | `-29.07%` | `993.96` |
| `Live` | `Long` | `0.4835` | 182,890.00 USD | 0.00 USD | 135.33 USD | `-27.88%` | `279.90` |
| `Live` | `Long` | `0.4855` | 182,750.00 USD | 0.00 USD | 1,010.00 USD | `-27.58%` | `2,078.06` |
| `Live` | `Long` | `0.4865` | 181,740.00 USD | 0.00 USD | 3,170.00 USD | `-27.43%` | `6,508.47` |
| `Live` | `Long` | `0.4985` | 178,580.00 USD | 0.00 USD | 429.90 USD | `-25.64%` | `862.38` |
| `Live` | `Long` | `0.5055` | 178,150.00 USD | 0.00 USD | 5,760.00 USD | `-24.60%` | `11,392.84` |
| `Live` | `Long` | `0.5085` | 172,390.00 USD | 0.00 USD | 102.82 USD | `-24.15%` | `202.20` |
| `Live` | `Long` | `0.5095` | 172,280.00 USD | 0.00 USD | 2,550.00 USD | `-24.00%` | `5,003.93` |
| `Live` | `Long` | `0.5125` | 169,740.00 USD | 0.00 USD | 248.05 USD | `-23.55%` | `484.00` |
| `Live` | `Long` | `0.5135` | 169,490.00 USD | 0.00 USD | 110.50 USD | `-23.40%` | `215.19` |
| `Live` | `Long` | `0.5145` | 169,380.00 USD | 0.00 USD | 288.78 USD | `-23.25%` | `561.28` |
| `Live` | `Long` | `0.5175` | 169,090.00 USD | 0.00 USD | 9,440.00 USD | `-22.81%` | `18,249.92` |
| `Live` | `Long` | `0.5315` | 159,640.00 USD | 0.00 USD | 11,510.00 USD | `-20.72%` | `21,664.95` |
| `Live` | `Long` | `0.5335` | 148,130.00 USD | 0.00 USD | 163.22 USD | `-20.42%` | `305.95` |
| `Live` | `Long` | `0.5385` | 147,970.00 USD | 0.00 USD | 2,690.00 USD | `-19.67%` | `5,002.20` |
| `Live` | `Long` | `0.5445` | 145,270.00 USD | 0.00 USD | 330.14 USD | `-18.78%` | `606.32` |
| `Live` | `Long` | `0.5495` | 144,940.00 USD | 0.00 USD | 630.26 USD | `-18.03%` | `1,146.97` |
| `Live` | `Long` | `0.5545` | 144,310.00 USD | 0.00 USD | 47,450.00 USD | `-17.29%` | `85,578.81` |
| `Live` | `Long` | `0.5585` | 96,860.00 USD | 0.00 USD | 10,520.00 USD | `-16.69%` | `18,834.52` |
| `Live` | `Long` | `0.5615` | 86,340.00 USD | 0.00 USD | 1,720.00 USD | `-16.24%` | `3,064.43` |
| `Live` | `Long` | `0.5625` | 84,620.00 USD | 0.00 USD | 3,280.00 USD | `-16.09%` | `5,839.42` |
| `Live` | `Long` | `0.5695` | 81,330.00 USD | 0.00 USD | 164.24 USD | `-15.05%` | `288.40` |
| `Live` | `Long` | `0.5715` | 81,170.00 USD | 0.00 USD | 289.08 USD | `-14.75%` | `505.82` |
| `Live` | `Long` | `0.5735` | 80,880.00 USD | 0.00 USD | 214.84 USD | `-14.45%` | `374.62` |
| `Live` | `Long` | `0.5785` | 80,670.00 USD | 0.00 USD | 662.59 USD | `-13.71%` | `1,145.36` |
| `Live` | `Long` | `0.5805` | 80,000.00 USD | 0.00 USD | 20,760.00 USD | `-13.41%` | `35,754.12` |
| `Live` | `Long` | `0.5835` | 59,250.00 USD | 0.00 USD | 132.92 USD | `-12.96%` | `227.80` |
| `Live` | `Long` | `0.5845` | 59,110.00 USD | 0.00 USD | 210.96 USD | `-12.81%` | `360.92` |
| `Live` | `Long` | `0.5865` | 58,900.00 USD | 0.00 USD | 586.80 USD | `-12.51%` | `1,000.51` |
| `Live` | `Long` | `0.5885` | 58,320.00 USD | 0.00 USD | 440.16 USD | `-12.22%` | `747.93` |
| `Live` | `Long` | `0.5895` | 57,880.00 USD | 0.00 USD | 1,690.00 USD | `-12.07%` | `2,865.95` |
| `Live` | `Long` | `0.5925` | 56,190.00 USD | 0.00 USD | 609.14 USD | `-11.62%` | `1,028.09` |
| `Live` | `Long` | `0.5935` | 55,580.00 USD | 0.00 USD | 572.40 USD | `-11.47%` | `964.45` |
| `Live` | `Long` | `0.5945` | 55,010.00 USD | 0.00 USD | 3,850.00 USD | `-11.32%` | `6,467.73` |
| `Live` | `Long` | `0.5975` | 51,160.00 USD | 0.00 USD | 157.22 USD | `-10.87%` | `263.13` |
| `Live` | `Long` | `0.6005` | 51,000.00 USD | 0.00 USD | 2,460.00 USD | `-10.43%` | `4,090.41` |
| `Live` | `Long` | `0.6045` | 48,550.00 USD | 0.00 USD | 527.44 USD | `-9.83%` | `872.53` |
| `Live` | `Long` | `0.6085` | 48,020.00 USD | 0.00 USD | 455.69 USD | `-9.23%` | `748.87` |
| `Live` | `Long` | `0.6105` | 47,560.00 USD | 0.00 USD | 6,090.00 USD | `-8.93%` | `9,974.00` |
| `Live` | `Long` | `0.6115` | 41,470.00 USD | 0.00 USD | 5,220.00 USD | `-8.79%` | `8,530.92` |
| `Live` | `Long` | `0.6195` | 36,260.00 USD | 0.00 USD | 3,170.00 USD | `-7.59%` | `5,109.42` |
| `Live` | `Long` | `0.6235` | 33,090.00 USD | 0.00 USD | 3,250.00 USD | `-7.00%` | `5,220.30` |
| `Live` | `Long` | `0.6255` | 29,840.00 USD | 0.00 USD | 286.65 USD | `-6.70%` | `458.28` |
| `Live` | `Long` | `0.6265` | 29,550.00 USD | 0.00 USD | 10,530.00 USD | `-6.55%` | `16,808.62` |
| `Live` | `Long` | `0.6285` | 19,020.00 USD | 0.00 USD | 903.47 USD | `-6.25%` | `1,437.50` |
| `Live` | `Long` | `0.6315` | 18,120.00 USD | 0.00 USD | 1,010.00 USD | `-5.80%` | `1,599.74` |
| `Live` | `Long` | `0.6375` | 17,110.00 USD | 0.00 USD | 5,900.00 USD | `-4.91%` | `9,256.34` |
| `Live` | `Long` | `0.6415` | 11,210.00 USD | 0.00 USD | 4,740.00 USD | `-4.31%` | `7,394.26` |
| `Live` | `Long` | `0.6435` | 6,460.00 USD | 0.00 USD | 2,320.00 USD | `-4.01%` | `3,602.46` |
| `Live` | `Long` | `0.6455` | 4,140.00 USD | 0.00 USD | 3,730.00 USD | `-3.71%` | `5,780.73` |
| `Live` | `Long` | `0.6485` | 412.77 USD | 0.00 USD | 259.68 USD | `-3.27%` | `400.43` |
| `Live` | `Long` | `0.6535` | 153.10 USD | 0.00 USD | 153.10 USD | `-2.52%` | `234.27` |
| `Live` | `Short` | `0.7075` | 2,220.00 USD | 2,220.00 USD | 0.00 USD | `+5.53%` | `3,144.75` |
| `Live` | `Short` | `0.7125` | 2,860.00 USD | 632.02 USD | 0.00 USD | `+6.28%` | `887.04` |
| `Live` | `Short` | `0.7255` | 46,810.00 USD | 43,950.00 USD | 0.00 USD | `+8.22%` | `60,578.26` |
| `Live` | `Short` | `0.7345` | 46,960.00 USD | 150.17 USD | 0.00 USD | `+9.56%` | `204.45` |
| `Live` | `Short` | `0.7635` | 47,100.00 USD | 143.11 USD | 0.00 USD | `+13.89%` | `187.44` |
| `Live` | `Short` | `0.7725` | 47,270.00 USD | 165.62 USD | 0.00 USD | `+15.23%` | `214.40` |
| `Live` | `Short` | `0.7765` | 47,600.00 USD | 330.78 USD | 0.00 USD | `+15.83%` | `425.99` |
| `Live` | `Short` | `0.8005` | 66,710.00 USD | 19,120.00 USD | 0.00 USD | `+19.41%` | `23,882.80` |
| `Live` | `Short` | `0.8035` | 66,830.00 USD | 114.11 USD | 0.00 USD | `+19.85%` | `142.02` |
| `Live` | `Short` | `0.8615` | 82,470.00 USD | 15,640.00 USD | 0.00 USD | `+28.51%` | `18,155.35` |
| `Live` | `Short` | `0.8665` | 82,850.00 USD | 378.95 USD | 0.00 USD | `+29.25%` | `437.33` |
| `Live` | `Short` | `0.9935` | 83,010.00 USD | 166.01 USD | 0.00 USD | `+48.20%` | `167.10` |
| `Live` | `Short` | `1.00` | 104,090.00 USD | 21,080.00 USD | 0.00 USD | `+49.84%` | `20,986.17` |
| `Live` | `Short` | `1.06` | 122,810.00 USD | 18,720.00 USD | 0.00 USD | `+58.19%` | `17,648.14` |
| `Live` | `Short` | `1.08` | 205,480.00 USD | 82,670.00 USD | 0.00 USD | `+61.62%` | `76,300.00` |
| `Live` | `Short` | `1.09` | 208,560.00 USD | 3,080.00 USD | 0.00 USD | `+62.22%` | `2,829.20` |
| `Live` | `Short` | `1.09` | 209,040.00 USD | 479.74 USD | 0.00 USD | `+62.81%` | `439.52` |
| `Live` | `Short` | `1.12` | 211,840.00 USD | 2,800.00 USD | 0.00 USD | `+66.99%` | `2,500.00` |
| `Live` | `Short` | `1.27` | 225,160.00 USD | 13,320.00 USD | 0.00 USD | `+89.22%` | `10,500.00` |
| `Live` | `Short` | `1.32` | 225,350.00 USD | 197.51 USD | 0.00 USD | `+97.12%` | `149.46` |
| `Live` | `Short` | `1.33` | 225,640.00 USD | 284.61 USD | 0.00 USD | `+98.31%` | `214.07` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.3505` | 121,490.00 USD | 0.00 USD | 340.19 USD | `-47.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4635` | 121,150.00 USD | 0.00 USD | 104.57 USD | `-30.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4805` | 121,040.00 USD | 0.00 USD | 14,740.00 USD | `-28.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 106,300.00 USD | 0.00 USD | 604.46 USD | `-25.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5125` | 105,700.00 USD | 0.00 USD | 5,380.00 USD | `-23.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5205` | 100,320.00 USD | 0.00 USD | 228.77 USD | `-22.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5305` | 100,090.00 USD | 0.00 USD | 770.19 USD | `-20.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5445` | 99,320.00 USD | 0.00 USD | 14,110.00 USD | `-18.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5455` | 85,210.00 USD | 0.00 USD | 8,150.00 USD | `-18.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5485` | 77,060.00 USD | 0.00 USD | 4,500.00 USD | `-18.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5515` | 72,560.00 USD | 0.00 USD | 126.71 USD | `-17.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5555` | 72,440.00 USD | 0.00 USD | 33,000.00 USD | `-17.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5565` | 39,440.00 USD | 0.00 USD | 300.09 USD | `-16.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5595` | 39,140.00 USD | 0.00 USD | 127.61 USD | `-16.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 39,010.00 USD | 0.00 USD | 339.84 USD | `-16.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5625` | 38,670.00 USD | 0.00 USD | 126.55 USD | `-16.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5655` | 38,540.00 USD | 0.00 USD | 127.62 USD | `-15.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5695` | 38,420.00 USD | 0.00 USD | 127.30 USD | `-15.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5715` | 38,290.00 USD | 0.00 USD | 127.63 USD | `-14.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5755` | 38,160.00 USD | 0.00 USD | 127.29 USD | `-14.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5785` | 38,030.00 USD | 0.00 USD | 127.36 USD | `-13.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5815` | 37,910.00 USD | 0.00 USD | 127.27 USD | `-13.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5835` | 37,780.00 USD | 0.00 USD | 178.88 USD | `-12.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5845` | 37,600.00 USD | 0.00 USD | 127.33 USD | `-12.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5865` | 37,470.00 USD | 0.00 USD | 128.36 USD | `-12.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5875` | 37,350.00 USD | 0.00 USD | 128.34 USD | `-12.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5895` | 37,220.00 USD | 0.00 USD | 128.45 USD | `-12.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5905` | 37,090.00 USD | 0.00 USD | 127.30 USD | `-11.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5925` | 36,960.00 USD | 0.00 USD | 128.33 USD | `-11.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5975` | 36,830.00 USD | 0.00 USD | 597.80 USD | `-10.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 36,240.00 USD | 0.00 USD | 3,510.00 USD | `-10.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 32,730.00 USD | 0.00 USD | 1,510.00 USD | `-9.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6065` | 31,220.00 USD | 0.00 USD | 1,910.00 USD | `-9.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6085` | 29,310.00 USD | 0.00 USD | 301.32 USD | `-9.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6175` | 29,010.00 USD | 0.00 USD | 699.67 USD | `-7.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6185` | 28,310.00 USD | 0.00 USD | 177.58 USD | `-7.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 28,130.00 USD | 0.00 USD | 541.40 USD | `-7.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6275` | 27,590.00 USD | 0.00 USD | 433.11 USD | `-6.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6285` | 27,160.00 USD | 0.00 USD | 469.94 USD | `-6.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 26,690.00 USD | 0.00 USD | 4,430.00 USD | `-5.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6315` | 22,260.00 USD | 0.00 USD | 160.16 USD | `-5.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6335` | 22,100.00 USD | 0.00 USD | 8,390.00 USD | `-5.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6345` | 13,710.00 USD | 0.00 USD | 276.40 USD | `-5.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6395` | 13,430.00 USD | 0.00 USD | 1,200.00 USD | `-4.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6405` | 12,230.00 USD | 0.00 USD | 145.91 USD | `-4.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6445` | 12,090.00 USD | 0.00 USD | 121.42 USD | `-3.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6485` | 11,970.00 USD | 0.00 USD | 447.03 USD | `-3.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 11,520.00 USD | 0.00 USD | 567.58 USD | `-2.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6525` | 10,950.00 USD | 0.00 USD | 111.92 USD | `-2.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 10,840.00 USD | 0.00 USD | 349.76 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 10,490.00 USD | 0.00 USD | 4,080.00 USD | `-2.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6565` | 6,410.00 USD | 0.00 USD | 284.88 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6585` | 6,130.00 USD | 0.00 USD | 1,440.00 USD | `-1.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6595` | 4,690.00 USD | 0.00 USD | 746.46 USD | `-1.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6605` | 3,940.00 USD | 0.00 USD | 580.23 USD | `-1.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6645` | 3,360.00 USD | 0.00 USD | 124.55 USD | `-0.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6655` | 3,240.00 USD | 0.00 USD | 1,110.00 USD | `-0.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6675` | 2,130.00 USD | 0.00 USD | 290.78 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6685` | 1,840.00 USD | 0.00 USD | 170.95 USD | `-0.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6695` | 1,670.00 USD | 0.00 USD | 1,670.00 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6705` | 162.91 USD | 162.91 USD | 0.00 USD | `+0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6715` | 365.54 USD | 202.63 USD | 0.00 USD | `+0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6725` | 2,040.00 USD | 1,670.00 USD | 0.00 USD | `+0.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6745` | 2,640.00 USD | 598.31 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6755` | 3,000.00 USD | 361.53 USD | 0.00 USD | `+0.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 5,130.00 USD | 2,130.00 USD | 0.00 USD | `+0.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6805` | 5,340.00 USD | 214.20 USD | 0.00 USD | `+1.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6815` | 15,900.00 USD | 10,560.00 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6825` | 16,010.00 USD | 112.49 USD | 0.00 USD | `+1.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6835` | 16,120.00 USD | 108.41 USD | 0.00 USD | `+1.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6855` | 16,240.00 USD | 112.98 USD | 0.00 USD | `+2.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6865` | 16,530.00 USD | 292.33 USD | 0.00 USD | `+2.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6875` | 16,670.00 USD | 140.41 USD | 0.00 USD | `+2.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6885` | 17,180.00 USD | 514.80 USD | 0.00 USD | `+2.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6895` | 17,380.00 USD | 194.09 USD | 0.00 USD | `+2.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6915` | 17,480.00 USD | 101.96 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6925` | 18,500.00 USD | 1,020.00 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6945` | 19,110.00 USD | 610.10 USD | 0.00 USD | `+3.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6955` | 19,210.00 USD | 101.38 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6965` | 20,000.00 USD | 789.18 USD | 0.00 USD | `+3.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6985` | 20,100.00 USD | 102.99 USD | 0.00 USD | `+4.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7005` | 20,240.00 USD | 137.19 USD | 0.00 USD | `+4.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7015` | 20,800.00 USD | 561.40 USD | 0.00 USD | `+4.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7085` | 21,750.00 USD | 947.29 USD | 0.00 USD | `+5.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7095` | 21,880.00 USD | 132.99 USD | 0.00 USD | `+5.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7115` | 22,010.00 USD | 122.04 USD | 0.00 USD | `+6.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7135` | 22,310.00 USD | 307.58 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7165` | 24,150.00 USD | 1,830.00 USD | 0.00 USD | `+6.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7195` | 24,520.00 USD | 373.99 USD | 0.00 USD | `+7.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7205` | 24,670.00 USD | 147.15 USD | 0.00 USD | `+7.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7215` | 27,930.00 USD | 3,260.00 USD | 0.00 USD | `+7.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7225` | 28,080.00 USD | 150.08 USD | 0.00 USD | `+7.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7265` | 34,500.00 USD | 6,410.00 USD | 0.00 USD | `+8.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7305` | 50,100.00 USD | 15,600.00 USD | 0.00 USD | `+8.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7325` | 50,260.00 USD | 165.17 USD | 0.00 USD | `+9.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7345` | 51,290.00 USD | 1,030.00 USD | 0.00 USD | `+9.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7375` | 51,400.00 USD | 106.75 USD | 0.00 USD | `+10.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7395` | 51,600.00 USD | 208.16 USD | 0.00 USD | `+10.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7405` | 52,340.00 USD | 733.09 USD | 0.00 USD | `+10.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7415` | 52,490.00 USD | 156.98 USD | 0.00 USD | `+10.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7425` | 52,630.00 USD | 132.95 USD | 0.00 USD | `+10.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7445` | 53,380.00 USD | 757.16 USD | 0.00 USD | `+11.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7455` | 55,550.00 USD | 2,170.00 USD | 0.00 USD | `+11.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7475` | 55,870.00 USD | 318.43 USD | 0.00 USD | `+11.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7505` | 56,010.00 USD | 141.39 USD | 0.00 USD | `+11.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7525` | 56,140.00 USD | 134.74 USD | 0.00 USD | `+12.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7565` | 60,260.00 USD | 4,120.00 USD | 0.00 USD | `+12.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7575` | 60,770.00 USD | 511.82 USD | 0.00 USD | `+12.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7585` | 60,910.00 USD | 135.82 USD | 0.00 USD | `+13.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7615` | 61,780.00 USD | 875.23 USD | 0.00 USD | `+13.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7635` | 61,890.00 USD | 103.35 USD | 0.00 USD | `+13.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7665` | 62,010.00 USD | 127.48 USD | 0.00 USD | `+14.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7675` | 62,120.00 USD | 101.61 USD | 0.00 USD | `+14.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7695` | 62,300.00 USD | 186.97 USD | 0.00 USD | `+14.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7705` | 62,410.00 USD | 109.43 USD | 0.00 USD | `+14.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7775` | 62,580.00 USD | 166.70 USD | 0.00 USD | `+15.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7815` | 63,710.00 USD | 1,140.00 USD | 0.00 USD | `+16.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7865` | 70,030.00 USD | 6,310.00 USD | 0.00 USD | `+17.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8095` | 70,160.00 USD | 133.42 USD | 0.00 USD | `+20.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8125` | 82,230.00 USD | 12,070.00 USD | 0.00 USD | `+21.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8335` | 83,160.00 USD | 929.08 USD | 0.00 USD | `+24.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8475` | 123,750.00 USD | 40,590.00 USD | 0.00 USD | `+26.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8505` | 126,820.00 USD | 3,060.00 USD | 0.00 USD | `+26.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8515` | 139,540.00 USD | 12,720.00 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8525` | 151,320.00 USD | 11,780.00 USD | 0.00 USD | `+27.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8705` | 152,600.00 USD | 1,280.00 USD | 0.00 USD | `+29.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8725` | 152,760.00 USD | 159.86 USD | 0.00 USD | `+30.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 156,040.00 USD | 3,290.00 USD | 0.00 USD | `+39.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 156,380.00 USD | 340.54 USD | 0.00 USD | `+41.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 156,530.00 USD | 145.72 USD | 0.00 USD | `+44.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 157,520.00 USD | 987.50 USD | 0.00 USD | `+47.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 157,650.00 USD | 136.10 USD | 0.00 USD | `+49.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 158,200.00 USD | 550.48 USD | 0.00 USD | `+49.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 158,520.00 USD | 314.99 USD | 0.00 USD | `+53.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 159,120.00 USD | 602.17 USD | 0.00 USD | `+56.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 159,480.00 USD | 360.61 USD | 0.00 USD | `+58.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 160,420.00 USD | 942.77 USD | 0.00 USD | `+61.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 160,760.00 USD | 337.31 USD | 0.00 USD | `+61.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 161,160.00 USD | 397.19 USD | 0.00 USD | `+64.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 174,290.00 USD | 13,130.00 USD | 0.00 USD | `+86.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 175,610.00 USD | 1,320.00 USD | 0.00 USD | `+88.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 212,470.00 USD | 36,850.00 USD | 0.00 USD | `+93.24%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.5910` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 3,120.00 USD | 1,560.00 USD | 81.07 USD |
| `7D` | `0.5920` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 0.00 USD | 2,820.00 USD | 0.00 USD |
| `7D` | `0.5930` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 10,090.00 USD | 0.00 USD | 9,780.00 USD |
| `7D` | `0.5950` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 5,120.00 USD | 0.00 USD | 4,530.00 USD |
| `7D` | `0.5960` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 5,120.00 USD | 1,640.00 USD | 0.00 USD |
| `7D` | `0.5970` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 9,760.00 USD |
| `7D` | `0.5980` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 7,660.00 USD | 826.53 USD | 0.00 USD |
| `1D` | `0.5990` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 12,180.00 USD | 2,190.00 USD | 16,600.00 USD |
| `7D` | `0.5990` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 3,320.00 USD | 1,340.00 USD | 14,050.00 USD |
| `1D` | `0.6000` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 1,130.00 USD |
| `7D` | `0.6000` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 0.00 USD | 796.28 USD | 4,700.00 USD |
| `1D` | `0.6010` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 735.24 USD | 461.96 USD | 15.46 USD |
| `1D` | `0.6020` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 7,230.00 USD | 3,830.00 USD | 3,710.00 USD |
| `7D` | `0.6020` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 4,890.00 USD | 8,040.00 USD | 4,010.00 USD |
| `1D` | `0.6030` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 3,730.00 USD | 2,940.00 USD | 3,690.00 USD |
| `7D` | `0.6030` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 2,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6040` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 6,990.00 USD | 2,320.00 USD | 1,880.00 USD |
| `7D` | `0.6040` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 5,670.00 USD | 3,100.00 USD | 7,880.00 USD |
| `1D` | `0.6050` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 0.00 USD | 1,750.00 USD | 1,200.00 USD |
| `1D` | `0.6060` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 2,880.00 USD | 606.70 USD | 3,050.00 USD |
| `7D` | `0.6060` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 78.65 USD |
| `1D` | `0.6070` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 7,700.00 USD | 1,030.00 USD | 4,740.00 USD |
| `7D` | `0.6070` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 85.65 USD |
| `1D` | `0.6080` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 2,970.00 USD | 0.00 USD | 4,010.00 USD |
| `7D` | `0.6080` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 2,860.00 USD | 0.00 USD | 115.34 USD |
| `1D` | `0.6090` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 6,430.00 USD | 0.00 USD | 47.82 USD |
| `7D` | `0.6090` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 13,920.00 USD | 0.00 USD | 8,210.00 USD |
| `1D` | `0.6100` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 3,960.00 USD | 0.00 USD | 5,750.00 USD |
| `7D` | `0.6100` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 7,480.00 USD | 2,570.00 USD | 22.52 USD |
| `1D` | `0.6110` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 1,430.00 USD | 0.00 USD | 1,070.00 USD |
| `7D` | `0.6110` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 0.00 USD | 2,210.00 USD | 12,880.00 USD |
| `1D` | `0.6120` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD |
| `7D` | `0.6120` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 2,100.00 USD | 3,510.00 USD | 7,160.00 USD |
| `1D` | `0.6130` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 2,140.00 USD | 596.50 USD | 1,020.00 USD |
| `7D` | `0.6130` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 8,870.00 USD | 1,050.00 USD | 4,290.00 USD |
| `1D` | `0.6140` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 6,120.00 USD | 0.00 USD | 1,000.00 USD |
| `7D` | `0.6140` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 4,540.00 USD | 7,000.00 USD | 6,550.00 USD |
| `1D` | `0.6150` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 2,730.00 USD | 0.00 USD | 30.06 USD |
| `7D` | `0.6150` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 11,130.00 USD | 5,870.00 USD | 2,820.00 USD |
| `1D` | `0.6160` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 0.00 USD | 1,270.00 USD | 126.06 USD |
| `7D` | `0.6160` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 1,790.00 USD | 2,510.00 USD | 3,680.00 USD |
| `1D` | `0.6170` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 3,480.00 USD |
| `7D` | `0.6170` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 13,260.00 USD | 2,610.00 USD | 14,690.00 USD |
| `7D` | `0.6180` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 7,600.00 USD | 1,190.00 USD | 5,990.00 USD |
| `1D` | `0.6190` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 126.86 USD |
| `7D` | `0.6190` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 9,560.00 USD | 1,930.00 USD | 9,570.00 USD |
| `1D` | `0.6200` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD |
| `7D` | `0.6200` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 13,870.00 USD | 5,230.00 USD | 6,050.00 USD |
| `1D` | `0.6210` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 1,990.00 USD | 0.00 USD | 2,070.00 USD |
| `7D` | `0.6210` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 4,760.00 USD | 1,860.00 USD | 5,050.00 USD |
| `1D` | `0.6220` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 2,520.00 USD | 0.00 USD | 7.22 USD |
| `7D` | `0.6220` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 7,960.00 USD | 2,310.00 USD | 29,940.00 USD |
| `1D` | `0.6230` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 1,100.00 USD |
| `7D` | `0.6230` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 9,770.00 USD | 4,700.00 USD | 8,310.00 USD |
| `1D` | `0.6240` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 3,220.00 USD | 3,780.00 USD | 76.16 USD |
| `7D` | `0.6240` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 18,610.00 USD | 4,720.00 USD | 5,320.00 USD |
| `1D` | `0.6250` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 1,800.00 USD | 2,050.00 USD | 85.42 USD |
| `7D` | `0.6250` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 16,120.00 USD | 3,830.00 USD | 2,320.00 USD |
| `1D` | `0.6260` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 8,920.00 USD | 751.16 USD | 2,060.00 USD |
| `7D` | `0.6260` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 20,890.00 USD | 7,660.00 USD | 26,060.00 USD |
| `1D` | `0.6270` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 3,700.00 USD | 3,940.00 USD | 12,850.00 USD |
| `7D` | `0.6270` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 17,460.00 USD | 8,200.00 USD | 24,260.00 USD |
| `1D` | `0.6280` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 11,690.00 USD | 463.43 USD | 2,070.00 USD |
| `7D` | `0.6280` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 9,160.00 USD | 9,230.00 USD | 16,910.00 USD |
| `1D` | `0.6290` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 11,890.00 USD | 1,200.00 USD | 5,120.00 USD |
| `7D` | `0.6290` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 17,710.00 USD | 6,740.00 USD | 10,090.00 USD |
| `1D` | `0.6300` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 12,950.00 USD | 2,470.00 USD | 2,960.00 USD |
| `7D` | `0.6300` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 10,040.00 USD | 7,890.00 USD | 11,580.00 USD |
| `1D` | `0.6310` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 7,940.00 USD | 5,110.00 USD | 4,200.00 USD |
| `7D` | `0.6310` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 19,340.00 USD | 4,520.00 USD | 17,300.00 USD |
| `1D` | `0.6320` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 12,320.00 USD | 11,080.00 USD | 14,850.00 USD |
| `7D` | `0.6320` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 4,880.00 USD | 12,650.00 USD | 8,630.00 USD |
| `1D` | `0.6330` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 17,300.00 USD | 3,580.00 USD | 21,030.00 USD |
| `7D` | `0.6330` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 57,940.00 USD | 14,700.00 USD | 33,590.00 USD |
| `1D` | `0.6340` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 9,830.00 USD | 2,020.00 USD | 15,360.00 USD |
| `7D` | `0.6340` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 10,730.00 USD | 3,420.00 USD | 4,840.00 USD |
| `1D` | `0.6350` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 19,180.00 USD | 8,820.00 USD | 4,240.00 USD |
| `7D` | `0.6350` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 14,450.00 USD | 2,430.00 USD | 22,830.00 USD |
| `1D` | `0.6360` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 30,350.00 USD | 9,150.00 USD | 33,290.00 USD |
| `7D` | `0.6360` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 42,690.00 USD | 7,300.00 USD | 40,300.00 USD |
| `1D` | `0.6370` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 21,750.00 USD | 4,510.00 USD | 27,410.00 USD |
| `7D` | `0.6370` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 49,080.00 USD | 4,870.00 USD | 334.25 USD |
| `1D` | `0.6380` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 19,430.00 USD | 7,180.00 USD | 7,690.00 USD |
| `7D` | `0.6380` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 18,140.00 USD | 3,870.00 USD | 30,320.00 USD |
| `1D` | `0.6390` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 18,790.00 USD | 529.57 USD | 6,800.00 USD |
| `7D` | `0.6390` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 10,200.00 USD | 7,510.00 USD | 13,390.00 USD |
| `1D` | `0.6400` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 9,830.00 USD | 9,970.00 USD | 26,730.00 USD |
| `7D` | `0.6400` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 15,560.00 USD | 0.00 USD | 307.33 USD |
| `1D` | `0.6410` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 20,930.00 USD | 2,240.00 USD | 7,440.00 USD |
| `7D` | `0.6410` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 6,340.00 USD |
| `1D` | `0.6420` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 43,840.00 USD | 12,930.00 USD | 12,640.00 USD |
| `7D` | `0.6420` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 55,350.00 USD | 26,560.00 USD | 10,320.00 USD |
| `1D` | `0.6430` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 32,170.00 USD | 9,880.00 USD | 9,340.00 USD |
| `7D` | `0.6430` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 16,200.00 USD | 7,140.00 USD | 2,810.00 USD |
| `1D` | `0.6440` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 30,930.00 USD | 14,720.00 USD | 9,730.00 USD |
| `7D` | `0.6440` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 28,340.00 USD | 17,680.00 USD | 14,770.00 USD |
| `1D` | `0.6450` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 26,090.00 USD | 22,940.00 USD | 34,240.00 USD |
| `7D` | `0.6450` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 14,120.00 USD | 15,560.00 USD | 731.44 USD |
| `1D` | `0.6460` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 43,360.00 USD | 11,650.00 USD | 51,650.00 USD |
| `7D` | `0.6460` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 82,710.00 USD | 14,300.00 USD | 75,480.00 USD |
| `1D` | `0.6470` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 46,150.00 USD | 6,620.00 USD | 41,790.00 USD |
| `7D` | `0.6470` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 9,660.00 USD | 3,880.00 USD | 9,440.00 USD |
| `1D` | `0.6480` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 48,130.00 USD | 14,180.00 USD | 7,770.00 USD |
| `7D` | `0.6480` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 37,050.00 USD | 0.00 USD | 23,520.00 USD |
| `1D` | `0.6490` | 977,080.00 USD | 0.00 USD | 977,080.00 USD | 31,930.00 USD | 3,800.00 USD | 51,390.00 USD |
| `7D` | `0.6490` | 959,830.00 USD | 0.00 USD | 959,830.00 USD | 36,340.00 USD | 0.00 USD | 17,840.00 USD |
| `1D` | `0.6500` | 889,960.00 USD | 0.00 USD | 889,960.00 USD | 53,070.00 USD | 1,390.00 USD | 35,410.00 USD |
| `7D` | `0.6500` | 905,650.00 USD | 0.00 USD | 905,650.00 USD | 37,220.00 USD | 0.00 USD | 81,520.00 USD |
| `1D` | `0.6510` | 800,080.00 USD | 0.00 USD | 800,080.00 USD | 18,580.00 USD | 4,450.00 USD | 61,110.00 USD |
| `7D` | `0.6510` | 786,910.00 USD | 0.00 USD | 786,910.00 USD | 101,440.00 USD | 4,190.00 USD | 587.21 USD |
| `1D` | `0.6520` | 715,940.00 USD | 0.00 USD | 715,940.00 USD | 36,270.00 USD | 6,190.00 USD | 14,110.00 USD |
| `7D` | `0.6520` | 680,690.00 USD | 0.00 USD | 680,690.00 USD | 46,620.00 USD | 6,720.00 USD | 86,780.00 USD |
| `1D` | `0.6530` | 659,360.00 USD | 0.00 USD | 659,360.00 USD | 5,780.00 USD | 1,060.00 USD | 11,730.00 USD |
| `7D` | `0.6530` | 540,570.00 USD | 0.00 USD | 540,570.00 USD | 0.00 USD | 0.00 USD | 46,770.00 USD |
| `1D` | `0.6540` | 640,800.00 USD | 0.00 USD | 640,800.00 USD | 11,450.00 USD | 2,530.00 USD | 10,560.00 USD |
| `7D` | `0.6540` | 493,800.00 USD | 0.00 USD | 493,800.00 USD | 15,730.00 USD | 0.00 USD | 14,730.00 USD |
| `1D` | `0.6550` | 616,250.00 USD | 0.00 USD | 616,250.00 USD | 18,980.00 USD | 3,640.00 USD | 17,280.00 USD |
| `7D` | `0.6550` | 463,350.00 USD | 0.00 USD | 463,350.00 USD | 0.00 USD | 0.00 USD | 38,320.00 USD |
| `1D` | `0.6560` | 576,350.00 USD | 0.00 USD | 576,350.00 USD | 46,280.00 USD | 13,960.00 USD | 25,060.00 USD |
| `7D` | `0.6560` | 425,020.00 USD | 0.00 USD | 425,020.00 USD | 39,780.00 USD | 5,380.00 USD | 34,730.00 USD |
| `1D` | `0.6570` | 491,050.00 USD | 0.00 USD | 491,050.00 USD | 18,660.00 USD | 6,680.00 USD | 19,780.00 USD |
| `7D` | `0.6570` | 345,120.00 USD | 0.00 USD | 345,120.00 USD | 14,440.00 USD | 6,350.00 USD | 10,770.00 USD |
| `1D` | `0.6580` | 445,930.00 USD | 0.00 USD | 445,930.00 USD | 24,160.00 USD | 6,780.00 USD | 2,570.00 USD |
| `7D` | `0.6580` | 313,560.00 USD | 0.00 USD | 313,560.00 USD | 28,360.00 USD | 21,920.00 USD | 13,060.00 USD |
| `1D` | `0.6590` | 412,420.00 USD | 0.00 USD | 412,420.00 USD | 8,070.00 USD | 11,260.00 USD | 25,690.00 USD |
| `7D` | `0.6590` | 250,220.00 USD | 0.00 USD | 250,220.00 USD | 9,540.00 USD | 0.00 USD | 275.76 USD |
| `1D` | `0.6600` | 367,400.00 USD | 0.00 USD | 367,400.00 USD | 21,900.00 USD | 5,170.00 USD | 22,600.00 USD |
| `7D` | `0.6600` | 240,400.00 USD | 0.00 USD | 240,400.00 USD | 15,310.00 USD | 4,180.00 USD | 20,480.00 USD |
| `1D` | `0.6610` | 317,720.00 USD | 0.00 USD | 317,720.00 USD | 42,960.00 USD | 2,560.00 USD | 12,170.00 USD |
| `7D` | `0.6610` | 200,430.00 USD | 0.00 USD | 200,430.00 USD | 0.00 USD | 0.00 USD | 223.47 USD |
| `1D` | `0.6620` | 260,030.00 USD | 0.00 USD | 260,030.00 USD | 22,690.00 USD | 2,480.00 USD | 36,990.00 USD |
| `7D` | `0.6620` | 200,200.00 USD | 0.00 USD | 200,200.00 USD | 14,320.00 USD | 0.00 USD | 7,200.00 USD |
| `1D` | `0.6630` | 197,870.00 USD | 0.00 USD | 197,870.00 USD | 45,660.00 USD | 4,110.00 USD | 7,390.00 USD |
| `7D` | `0.6630` | 178,680.00 USD | 0.00 USD | 178,680.00 USD | 49,490.00 USD | 0.00 USD | 29,210.00 USD |
| `1D` | `0.6640` | 140,700.00 USD | 0.00 USD | 140,700.00 USD | 22,290.00 USD | 1,150.00 USD | 35,060.00 USD |
| `7D` | `0.6640` | 99,980.00 USD | 0.00 USD | 99,980.00 USD | 15,140.00 USD | 0.00 USD | 172.36 USD |
| `1D` | `0.6650` | 82,200.00 USD | 0.00 USD | 82,200.00 USD | 22,590.00 USD | 10,330.00 USD | 14,290.00 USD |
| `7D` | `0.6650` | 84,670.00 USD | 0.00 USD | 84,670.00 USD | 14,220.00 USD | 6,770.00 USD | 29,680.00 USD |
| `1D` | `0.6660` | 34,990.00 USD | 0.00 USD | 34,990.00 USD | 7,730.00 USD | 0.00 USD | 5,410.00 USD |
| `7D` | `0.6660` | 34,000.00 USD | 0.00 USD | 34,000.00 USD | 0.00 USD | 0.00 USD | 149.20 USD |
| `1D` | `0.6670` | 21,850.00 USD | 0.00 USD | 21,850.00 USD | 18,850.00 USD | 2,980.00 USD | 17.74 USD |
| `7D` | `0.6670` | 33,850.00 USD | 0.00 USD | 33,850.00 USD | 0.00 USD | 0.00 USD | 8,990.00 USD |
| `7D` | `0.6680` | 24,860.00 USD | 0.00 USD | 24,860.00 USD | 0.00 USD | 0.00 USD | 96.11 USD |
| `7D` | `0.6690` | 24,760.00 USD | 0.00 USD | 24,760.00 USD | 0.00 USD | 0.00 USD | 24,760.00 USD |
| `1D` | `0.6700` | 4,190.00 USD | 4,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,190.00 USD |
| `1D` | `0.6700` | 8,380.00 USD | 8,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,190.00 USD |
| `7D` | `0.6700` | 123.34 USD | 123.34 USD | 0.00 USD | 0.00 USD | 0.00 USD | 123.34 USD |
| `7D` | `0.6700` | 246.68 USD | 246.68 USD | 0.00 USD | 0.00 USD | 0.00 USD | 123.34 USD |
| `7D` | `0.6710` | 25,290.00 USD | 25,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25,050.00 USD |
| `1D` | `0.6720` | 25,530.00 USD | 25,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,150.00 USD |
| `1D` | `0.6730` | 38,360.00 USD | 38,360.00 USD | 0.00 USD | 5,220.00 USD | 0.00 USD | 7,600.00 USD |
| `1D` | `0.6740` | 45,470.00 USD | 45,470.00 USD | 0.00 USD | 0.00 USD | 4,800.00 USD | 2,310.00 USD |
| `1D` | `0.6750` | 51,450.00 USD | 51,450.00 USD | 0.00 USD | 0.00 USD | 5,970.00 USD | 0.00 USD |
| `7D` | `0.6750` | 101,020.00 USD | 101,020.00 USD | 0.00 USD | 0.00 USD | 75,730.00 USD | 0.00 USD |
| `1D` | `0.6760` | 54,080.00 USD | 54,080.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD | 0.00 USD |
| `7D` | `0.6760` | 103,260.00 USD | 103,260.00 USD | 0.00 USD | 0.00 USD | 2,240.00 USD | 0.00 USD |
| `1D` | `0.6770` | 56,740.00 USD | 56,740.00 USD | 0.00 USD | 0.00 USD | 2,660.00 USD | 0.00 USD |
| `7D` | `0.6770` | 107,450.00 USD | 107,450.00 USD | 0.00 USD | 0.00 USD | 4,190.00 USD | 0.00 USD |
| `1D` | `0.6780` | 69,380.00 USD | 69,380.00 USD | 0.00 USD | 0.00 USD | 12,640.00 USD | 0.00 USD |
| `7D` | `0.6780` | 117,660.00 USD | 117,660.00 USD | 0.00 USD | 0.00 USD | 10,220.00 USD | 0.00 USD |
| `1D` | `0.6790` | 102,190.00 USD | 102,190.00 USD | 0.00 USD | 0.00 USD | 18,610.00 USD | 14,200.00 USD |
| `7D` | `0.6790` | 134,250.00 USD | 134,250.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 0.00 USD |
| `1D` | `0.6800` | 104,640.00 USD | 104,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,450.00 USD |
| `1D` | `0.6810` | 112,230.00 USD | 112,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,590.00 USD |
| `7D` | `0.6810` | 149,970.00 USD | 149,970.00 USD | 0.00 USD | 0.00 USD | 15,720.00 USD | 0.00 USD |
| `1D` | `0.6820` | 149,900.00 USD | 149,900.00 USD | 0.00 USD | 22,600.00 USD | 10,160.00 USD | 4,920.00 USD |
| `7D` | `0.6820` | 220,270.00 USD | 220,270.00 USD | 0.00 USD | 32,570.00 USD | 37,730.00 USD | 0.00 USD |
| `1D` | `0.6830` | 213,780.00 USD | 213,780.00 USD | 0.00 USD | 13,080.00 USD | 25,100.00 USD | 25,690.00 USD |
| `7D` | `0.6830` | 279,540.00 USD | 279,540.00 USD | 0.00 USD | 0.00 USD | 11,020.00 USD | 48,260.00 USD |
| `1D` | `0.6840` | 272,220.00 USD | 272,220.00 USD | 0.00 USD | 24,790.00 USD | 22,740.00 USD | 10,920.00 USD |
| `7D` | `0.6840` | 383,580.00 USD | 383,580.00 USD | 0.00 USD | 28,360.00 USD | 36,580.00 USD | 39,100.00 USD |
| `1D` | `0.6850` | 336,280.00 USD | 336,280.00 USD | 0.00 USD | 52,450.00 USD | 5,780.00 USD | 5,820.00 USD |
| `7D` | `0.6850` | 388,290.00 USD | 388,290.00 USD | 0.00 USD | 0.00 USD | 4,710.00 USD | 0.00 USD |
| `1D` | `0.6860` | 338,610.00 USD | 338,610.00 USD | 0.00 USD | 0.00 USD | 2,330.00 USD | 0.00 USD |
| `7D` | `0.6860` | 413,430.00 USD | 413,430.00 USD | 0.00 USD | 15,310.00 USD | 9,830.00 USD | 0.00 USD |
| `1D` | `0.6870` | 369,660.00 USD | 369,660.00 USD | 0.00 USD | 31,040.00 USD | 0.00 USD | 15.30 USD |
| `1D` | `0.6880` | 408,050.00 USD | 408,050.00 USD | 0.00 USD | 0.00 USD | 9,600.00 USD | 28,780.00 USD |
| `7D` | `0.6880` | 449,030.00 USD | 449,030.00 USD | 0.00 USD | 18,170.00 USD | 17,300.00 USD | 125.32 USD |
| `1D` | `0.6890` | 410,800.00 USD | 410,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,750.00 USD |
| `7D` | `0.6890` | 460,060.00 USD | 460,060.00 USD | 0.00 USD | 0.00 USD | 11,030.00 USD | 0.00 USD |
| `1D` | `0.6900` | 440,500.00 USD | 440,500.00 USD | 0.00 USD | 8,650.00 USD | 0.00 USD | 21,050.00 USD |
| `7D` | `0.6900` | 464,800.00 USD | 464,800.00 USD | 0.00 USD | 0.00 USD | 4,480.00 USD | 263.20 USD |
| `1D` | `0.6910` | 494,700.00 USD | 494,700.00 USD | 0.00 USD | 21,590.00 USD | 0.00 USD | 32,610.00 USD |
| `7D` | `0.6910` | 533,270.00 USD | 533,270.00 USD | 0.00 USD | 37,820.00 USD | 2,090.00 USD | 28,550.00 USD |
| `1D` | `0.6920` | 508,390.00 USD | 508,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,680.00 USD |
| `7D` | `0.6920` | 557,640.00 USD | 557,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,370.00 USD |
| `1D` | `0.6930` | 518,590.00 USD | 518,590.00 USD | 0.00 USD | 10,030.00 USD | 0.00 USD | 168.16 USD |
| `7D` | `0.6930` | 614,320.00 USD | 614,320.00 USD | 0.00 USD | 14,220.00 USD | 0.00 USD | 42,460.00 USD |
| `1D` | `0.6940` | 543,700.00 USD | 543,700.00 USD | 0.00 USD | 11,230.00 USD | 4,420.00 USD | 9,470.00 USD |
| `1D` | `0.6950` | 574,430.00 USD | 574,430.00 USD | 0.00 USD | 22,480.00 USD | 4,460.00 USD | 3,790.00 USD |
| `7D` | `0.6950` | 658,160.00 USD | 658,160.00 USD | 0.00 USD | 31,450.00 USD | 0.00 USD | 12,390.00 USD |
| `1D` | `0.6960` | 637,880.00 USD | 637,880.00 USD | 0.00 USD | 58,370.00 USD | 5,080.00 USD | 0.00 USD |
| `7D` | `0.6960` | 686,800.00 USD | 686,800.00 USD | 0.00 USD | 28,500.00 USD | 0.00 USD | 140.50 USD |
| `1D` | `0.6970` | 670,260.00 USD | 670,260.00 USD | 0.00 USD | 29,920.00 USD | 2,430.00 USD | 34.66 USD |
| `7D` | `0.6970` | 711,630.00 USD | 711,630.00 USD | 0.00 USD | 21,650.00 USD | 3,180.00 USD | 0.00 USD |
| `1D` | `0.6980` | 684,080.00 USD | 684,080.00 USD | 0.00 USD | 9,140.00 USD | 3,390.00 USD | 1,290.00 USD |
| `7D` | `0.6980` | 736,770.00 USD | 736,770.00 USD | 0.00 USD | 14,180.00 USD | 10,960.00 USD | 0.00 USD |
| `1D` | `0.6990` | 694,830.00 USD | 694,830.00 USD | 0.00 USD | 2,990.00 USD | 4,830.00 USD | 2,940.00 USD |
| `7D` | `0.6990` | 766,510.00 USD | 766,510.00 USD | 0.00 USD | 4,770.00 USD | 0.00 USD | 24,960.00 USD |
| `1D` | `0.7000` | 713,300.00 USD | 713,300.00 USD | 0.00 USD | 4,190.00 USD | 3,290.00 USD | 10,990.00 USD |
| `7D` | `0.7000` | 784,150.00 USD | 784,150.00 USD | 0.00 USD | 7,660.00 USD | 0.00 USD | 9,990.00 USD |
| `1D` | `0.7010` | 728,890.00 USD | 728,890.00 USD | 0.00 USD | 15,520.00 USD | 0.00 USD | 73.64 USD |
| `7D` | `0.7010` | 784,350.00 USD | 784,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 197.30 USD |
| `1D` | `0.7020` | 743,270.00 USD | 743,270.00 USD | 0.00 USD | 14,360.00 USD | 0.00 USD | 22.18 USD |
| `7D` | `0.7020` | 853,670.00 USD | 853,670.00 USD | 0.00 USD | 16,350.00 USD | 0.00 USD | 52,980.00 USD |
| `1D` | `0.7030` | 758,110.00 USD | 758,110.00 USD | 0.00 USD | 4,330.00 USD | 0.00 USD | 10,510.00 USD |
| `7D` | `0.7030` | 980,750.00 USD | 980,750.00 USD | 0.00 USD | 76,610.00 USD | 0.00 USD | 50,470.00 USD |
| `1D` | `0.7040` | 808,560.00 USD | 808,560.00 USD | 0.00 USD | 29,930.00 USD | 2,630.00 USD | 17,890.00 USD |
| `7D` | `0.7040` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 18,910.00 USD | 0.00 USD | 45,670.00 USD |
| `1D` | `0.7050` | 866,420.00 USD | 866,420.00 USD | 0.00 USD | 36,240.00 USD | 2,660.00 USD | 18,960.00 USD |
| `7D` | `0.7050` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 27,630.00 USD | 0.00 USD | 123,620.00 USD |
| `1D` | `0.7060` | 891,230.00 USD | 891,230.00 USD | 0.00 USD | 8,590.00 USD | 3,860.00 USD | 12,360.00 USD |
| `7D` | `0.7060` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 20,200.00 USD | 33,490.00 USD | 54,360.00 USD |
| `1D` | `0.7070` | 950,220.00 USD | 950,220.00 USD | 0.00 USD | 19,980.00 USD | 21,860.00 USD | 17,150.00 USD |
| `7D` | `0.7070` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 8,720.00 USD | 36,300.00 USD | 29,360.00 USD |
| `1D` | `0.7080` | 976,460.00 USD | 976,460.00 USD | 0.00 USD | 18,420.00 USD | 3,500.00 USD | 4,310.00 USD |
| `7D` | `0.7080` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 15,730.00 USD | 28,570.00 USD | 53,650.00 USD |
| `1D` | `0.7090` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 17,580.00 USD | 3,160.00 USD | 8,900.00 USD |
| `7D` | `0.7090` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 106,000.00 USD | 32,830.00 USD | 134,700.00 USD |
| `1D` | `0.7100` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 8,730.00 USD | 1,280.00 USD | 5,030.00 USD |
| `7D` | `0.7100` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 44,820.00 USD | 30,700.00 USD | 14,350.00 USD |
| `1D` | `0.7110` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 2,660.00 USD | 8,760.00 USD | 8,680.00 USD |
| `7D` | `0.7110` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 40,300.00 USD | 33,410.00 USD | 92,500.00 USD |
| `1D` | `0.7120` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 21,700.00 USD | 4,410.00 USD | 15,710.00 USD |
| `7D` | `0.7120` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 60,730.00 USD | 45,350.00 USD | 135,240.00 USD |
| `1D` | `0.7130` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 28,640.00 USD | 3,110.00 USD | 39,690.00 USD |
| `7D` | `0.7130` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 75,250.00 USD | 31,940.00 USD | 51,140.00 USD |
| `1D` | `0.7140` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 27,390.00 USD | 7,490.00 USD | 6,410.00 USD |
| `7D` | `0.7140` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 127,300.00 USD | 35,310.00 USD | 81,980.00 USD |
| `1D` | `0.7150` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 18,260.00 USD | 6,980.00 USD | 23,280.00 USD |
| `7D` | `0.7150` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 50,460.00 USD | 26,770.00 USD | 96,310.00 USD |
| `1D` | `0.7160` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 17,400.00 USD | 11,180.00 USD | 10,820.00 USD |
| `7D` | `0.7160` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 62,580.00 USD | 38,490.00 USD | 68,180.00 USD |
| `1D` | `0.7170` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 4,910.00 USD | 3,880.00 USD | 8,680.00 USD |
| `7D` | `0.7170` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 105,890.00 USD | 35,770.00 USD | 53,900.00 USD |
| `1D` | `0.7180` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 6,240.00 USD | 2,890.00 USD | 14,880.00 USD |
| `7D` | `0.7180` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 59,980.00 USD | 21,140.00 USD | 13,030.00 USD |
| `1D` | `0.7190` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 12,780.00 USD | 8,180.00 USD | 2,050.00 USD |
| `7D` | `0.7190` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 28,670.00 USD | 11,840.00 USD | 88,060.00 USD |
| `1D` | `0.7200` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 4,740.00 USD | 12,480.00 USD |
| `7D` | `0.7200` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 65,080.00 USD | 33,310.00 USD | 90,230.00 USD |
| `1D` | `0.7210` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 10,550.00 USD | 13,350.00 USD | 7,190.00 USD |
| `7D` | `0.7210` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 206,240.00 USD | 24,720.00 USD | 70,810.00 USD |
| `1D` | `0.7220` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 20,300.00 USD | 3,610.00 USD | 23,310.00 USD |
| `7D` | `0.7220` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 112,190.00 USD | 42,410.00 USD | 27,590.00 USD |
| `1D` | `0.7230` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 1,140.00 USD | 2,670.00 USD | 15,620.00 USD |
| `7D` | `0.7230` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 59,050.00 USD | 10,400.00 USD | 94,140.00 USD |
| `1D` | `0.7240` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 2,920.00 USD | 3,290.00 USD | 3,650.00 USD |
| `7D` | `0.7240` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 75,360.00 USD | 14,510.00 USD | 29,140.00 USD |
| `1D` | `0.7250` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 4,760.00 USD | 3,950.00 USD | 9,380.00 USD |
| `7D` | `0.7250` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 52,270.00 USD | 25,530.00 USD | 82,640.00 USD |
| `1D` | `0.7260` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 11,880.00 USD | 6,730.00 USD | 12,280.00 USD |
| `7D` | `0.7260` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 54,140.00 USD | 26,590.00 USD | 93,520.00 USD |
| `1D` | `0.7270` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 19,920.00 USD | 2,760.00 USD | 14,410.00 USD |
| `7D` | `0.7270` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 49,240.00 USD | 18,120.00 USD | 33,600.00 USD |
| `1D` | `0.7280` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 16,410.00 USD | 5,780.00 USD | 11,620.00 USD |
| `7D` | `0.7280` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 42,560.00 USD | 22,060.00 USD | 50,620.00 USD |
| `1D` | `0.7290` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 13,150.00 USD | 7,110.00 USD | 27,230.00 USD |
| `7D` | `0.7290` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 47,200.00 USD | 32,380.00 USD | 69,990.00 USD |
| `1D` | `0.7300` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 9,980.00 USD | 9,840.00 USD | 25,680.00 USD |
| `7D` | `0.7300` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 55,390.00 USD | 27,940.00 USD | 29,400.00 USD |
| `1D` | `0.7310` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 1,010.00 USD | 1,670.00 USD | 7,220.00 USD |
| `7D` | `0.7310` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 115,470.00 USD | 40,620.00 USD | 31,240.00 USD |
| `1D` | `0.7320` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 5,780.00 USD | 1,140.00 USD | 12,500.00 USD |
| `7D` | `0.7320` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 74,380.00 USD | 25,020.00 USD | 49,070.00 USD |
| `1D` | `0.7330` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 6,450.00 USD | 3,420.00 USD | 4,430.00 USD |
| `7D` | `0.7330` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 32,360.00 USD |
| `1D` | `0.7340` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 1,620.00 USD | 1,530.00 USD | 5,210.00 USD |
| `7D` | `0.7340` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 31,260.00 USD | 8,620.00 USD | 30,760.00 USD |
| `1D` | `0.7350` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 735.24 USD | 1,470.00 USD | 40.36 USD |
| `7D` | `0.7350` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 66,390.00 USD | 15,820.00 USD | 15,460.00 USD |
| `1D` | `0.7360` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 14,020.00 USD | 4,990.00 USD | 14,920.00 USD |
| `7D` | `0.7360` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 37,210.00 USD | 30,980.00 USD | 19,410.00 USD |
| `1D` | `0.7370` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 3,730.00 USD | 2,940.00 USD | 9,870.00 USD |
| `7D` | `0.7370` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 9,640.00 USD | 3,860.00 USD | 21,110.00 USD |
| `1D` | `0.7380` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 6,990.00 USD | 2,320.00 USD | 1,910.00 USD |
| `7D` | `0.7380` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 64,010.00 USD | 16,760.00 USD | 39,540.00 USD |
| `1D` | `0.7390` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 2,330.00 USD | 1,220.00 USD |
| `7D` | `0.7390` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 0.00 USD | 8,110.00 USD | 25,900.00 USD |
| `1D` | `0.7400` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 2,880.00 USD | 2,520.00 USD | 3,130.00 USD |
| `7D` | `0.7400` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 1,730.00 USD | 6,500.00 USD | 11,730.00 USD |
| `1D` | `0.7410` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 7,700.00 USD | 1,030.00 USD | 4,740.00 USD |
| `7D` | `0.7410` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 28,380.00 USD | 30,100.00 USD | 31,000.00 USD |
| `1D` | `0.7420` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.80 USD |
| `7D` | `0.7420` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 7,430.00 USD | 13,420.00 USD | 399.37 USD |
| `1D` | `0.7430` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 1,240.00 USD | 0.00 USD | 125.56 USD |
| `7D` | `0.7430` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 46,330.00 USD | 13,970.00 USD | 54,780.00 USD |
| `1D` | `0.7440` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 1,730.00 USD | 718.40 USD | 7,600.00 USD |
| `7D` | `0.7440` | 6,310,000.00 USD | 6,310,000.00 USD | 0.00 USD | 28,120.00 USD | 25,920.00 USD | 15,670.00 USD |
| `1D` | `0.7450` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 6,430.00 USD | 1,170.00 USD | 6,060.00 USD |
| `7D` | `0.7450` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 50,150.00 USD | 16,360.00 USD | 38,440.00 USD |
| `1D` | `0.7460` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 3,960.00 USD | 0.00 USD | 5,780.00 USD |
| `7D` | `0.7460` | 6,480,000.00 USD | 6,480,000.00 USD | 0.00 USD | 38,650.00 USD | 10,350.00 USD | 13,230.00 USD |
| `1D` | `0.7470` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 1,430.00 USD | 0.00 USD | 4,540.00 USD |
| `7D` | `0.7470` | 6,560,000.00 USD | 6,560,000.00 USD | 0.00 USD | 35,630.00 USD | 18,610.00 USD | 34,000.00 USD |
| `1D` | `0.7480` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 3,230.00 USD | 0.00 USD | 1,080.00 USD |
| `7D` | `0.7480` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 24,950.00 USD | 10,290.00 USD | 4,270.00 USD |
| `1D` | `0.7490` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 2,140.00 USD | 596.50 USD | 995.01 USD |
| `7D` | `0.7490` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 17,270.00 USD | 5,180.00 USD | 8,950.00 USD |
| `1D` | `0.7500` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 6,120.00 USD | 0.00 USD | 984.02 USD |
| `7D` | `0.7500` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 35,050.00 USD | 7,430.00 USD | 16,110.00 USD |
| `1D` | `0.7510` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 2,730.00 USD | 0.00 USD | 15.02 USD |
| `7D` | `0.7510` | 6,760,000.00 USD | 6,760,000.00 USD | 0.00 USD | 25,900.00 USD | 5,870.00 USD | 36,090.00 USD |
| `1D` | `0.7520` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD | 0.00 USD |
| `7D` | `0.7520` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 27,570.00 USD | 7,130.00 USD | 15,040.00 USD |
| `7D` | `0.7530` | 6,850,000.00 USD | 6,850,000.00 USD | 0.00 USD | 21,290.00 USD | 1,890.00 USD | 14,780.00 USD |
| `1D` | `0.7540` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 40.37 USD |
| `7D` | `0.7540` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 9,060.00 USD | 0.00 USD | 10,650.00 USD |
| `1D` | `0.7550` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,450.00 USD |
| `7D` | `0.7550` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 18,390.00 USD | 6,470.00 USD | 19,660.00 USD |
| `7D` | `0.7560` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 7,600.00 USD | 1,100.00 USD | 2,480.00 USD |
| `1D` | `0.7570` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11.00 USD |
| `7D` | `0.7570` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 29,140.00 USD | 4,260.00 USD | 33,440.00 USD |
| `1D` | `0.7580` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,700.00 USD |
| `7D` | `0.7580` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 26,280.00 USD | 7,530.00 USD | 12,300.00 USD |
| `1D` | `0.7590` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 1,990.00 USD | 0.00 USD | 2,030.00 USD |
| `7D` | `0.7590` | 7,110,000.00 USD | 7,110,000.00 USD | 0.00 USD | 34,970.00 USD | 717.68 USD | 32,970.00 USD |
| `1D` | `0.7600` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 2,520.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.7600` | 7,180,000.00 USD | 7,180,000.00 USD | 0.00 USD | 22,050.00 USD | 3,600.00 USD | 47,800.00 USD |
| `1D` | `0.7610` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,070.00 USD |
| `7D` | `0.7610` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 14,110.00 USD | 8,700.00 USD | 16,470.00 USD |
| `7D` | `0.7620` | 7,280,000.00 USD | 7,280,000.00 USD | 0.00 USD | 40,030.00 USD | 15,470.00 USD | 5,060.00 USD |
| `7D` | `0.7630` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 33,960.00 USD | 13,520.00 USD | 22,700.00 USD |
| `7D` | `0.7640` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 16,430.00 USD | 0.00 USD | 18,990.00 USD |
| `7D` | `0.7650` | 7,520,000.00 USD | 7,520,000.00 USD | 0.00 USD | 43,020.00 USD | 9,740.00 USD | 79,550.00 USD |
| `7D` | `0.7660` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 13,100.00 USD | 8,390.00 USD | 11,450.00 USD |
| `7D` | `0.7670` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 32,170.00 USD | 17,130.00 USD | 24,360.00 USD |
| `7D` | `0.7680` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 34,410.00 USD | 15,390.00 USD | 16,740.00 USD |
| `7D` | `0.7690` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 5,320.00 USD | 2,840.00 USD | 9,900.00 USD |
| `7D` | `0.7700` | 7,760,000.00 USD | 7,760,000.00 USD | 0.00 USD | 5,540.00 USD | 9,750.00 USD | 31,650.00 USD |
| `7D` | `0.7710` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 53,500.00 USD | 19,240.00 USD | 17,230.00 USD |
| `7D` | `0.7720` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 4,880.00 USD | 13,680.00 USD | 8,590.00 USD |
| `7D` | `0.7730` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 37,120.00 USD | 14,120.00 USD | 12,590.00 USD |
| `7D` | `0.7740` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 14,480.00 USD | 11,130.00 USD | 23,140.00 USD |
| `7D` | `0.7750` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 5,090.00 USD | 0.00 USD | 7,770.00 USD |
| `7D` | `0.7760` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 33,080.00 USD | 2,980.00 USD | 4,930.00 USD |
| `7D` | `0.7770` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 15,750.00 USD | 15,940.00 USD | 19,300.00 USD |
| `7D` | `0.7780` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 53,050.00 USD | 4,910.00 USD | 13,290.00 USD |
| `7D` | `0.7790` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 11,330.00 USD | 2,770.00 USD | 22,800.00 USD |
| `7D` | `0.7800` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 49,160.00 USD | 19,160.00 USD | 72,700.00 USD |
| `7D` | `0.7810` | 8,390,000.00 USD | 8,390,000.00 USD | 0.00 USD | 49,880.00 USD | 5,150.00 USD | 0.00 USD |
| `7D` | `0.7820` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 40,140.00 USD | 12,700.00 USD | 6,210.00 USD |
| `7D` | `0.7830` | 8,530,000.00 USD | 8,530,000.00 USD | 0.00 USD | 70,580.00 USD | 6,240.00 USD | 2,170.00 USD |
| `7D` | `0.7840` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 24,790.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `96.58M` | Total OI Tokens: `143,849,037.2 APT`
  * 1h OI Change: `-0.26%` | 4h OI Change: `-3.16%` | 24h OI Change: `-6.37%`
  * Exchange Breakdown: Binance=`18.65M` | Bybit=`19.73M` | OKX=`4.66M` | Hyperliquid=`3.63M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.38K` | Last 24h: `8.88K` | Last 3d: `10.89K` | Last 7d: `5.22K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0081%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0073%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0080%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0054%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `APT` | `54.36%` | `45.64%` | `1.19` | 1,840,000.00 USD |
| `15M` | `Binance` | `62.39%` | `37.61%` | `1.66` | 679,030.00 USD |
| `15M` | `OKX` | `70.22%` | `29.78%` | `2.36` | 210,850.00 USD |
| `15M` | `Bybit` | `76.06%` | `23.94%` | `3.18` | 148,560.00 USD |
| `15M` | `KuCoin` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Gate` | `56.61%` | `43.39%` | `1.30` | 22,560.00 USD |
| `15M` | `Bitget` | `72.14%` | `27.86%` | `2.59` | 16,310.00 USD |
| `15M` | `BingX` | `38.07%` | `61.93%` | `0.61` | 126,150.00 USD |
| `15M` | `MEXC` | `65.26%` | `34.74%` | `1.88` | 12,550.00 USD |
| `15M` | `Bitunix` | `68.08%` | `31.92%` | `2.13` | 56,070.00 USD |
| `15M` | `Hyperliquid` | `97.07%` | `2.93%` | `33.13` | 31,720.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.82%` | `48.18%` | `1.08` | 308,970.00 USD |
| `15M` | `Crypto.com` | `50%` | `50%` | `1.00` | 5.74 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 223,090.00 USD |
| `15M` | `HTX` | `63.25%` | `36.75%` | `1.72` | 391.78 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 22.97 USD |
| `15M` | `Aster` | `99.84%` | `0.16%` | `624.00` | 7,250.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 99.76 USD |
| `15M` | `Whale Positions` | `62.39%` | `37.61%` | `1.66` | 679,030.00 USD |
| `15M` | `Global Accounts` | `54.36%` | `45.64%` | `1.19` | 1,840,000.00 USD |
| `1H` | `APT` | `49.20%` | `50.80%` | `0.97` | 11,550,000.00 USD |
| `1H` | `Binance` | `53.96%` | `46.04%` | `1.17` | 4,010,000.00 USD |
| `1H` | `OKX` | `55.86%` | `44.14%` | `1.27` | 1,510,000.00 USD |
| `1H` | `Bybit` | `57.78%` | `42.22%` | `1.37` | 1,260,000.00 USD |
| `1H` | `KuCoin` | `44.8%` | `55.2%` | `0.81` | 272,230.00 USD |
| `1H` | `Gate` | `40.21%` | `59.79%` | `0.67` | 135,370.00 USD |
| `1H` | `Bitget` | `36.05%` | `63.95%` | `0.56` | 312,510.00 USD |
| `1H` | `BingX` | `47.19%` | `52.81%` | `0.89` | 813,560.00 USD |
| `1H` | `MEXC` | `47.85%` | `52.15%` | `0.92` | 141,150.00 USD |
| `1H` | `Bitunix` | `58%` | `42%` | `1.38` | 352,820.00 USD |
| `1H` | `Hyperliquid` | `46.44%` | `53.56%` | `0.87` | 80,570.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.46%` | `50.54%` | `0.98` | 1,880,000.00 USD |
| `1H` | `Crypto.com` | `49.98%` | `50.02%` | `1.00` | 28.77 USD |
| `1H` | `WhiteBIT` | `1.41%` | `98.59%` | `0.01` | 736,600.00 USD |
| `1H` | `HTX` | `47.75%` | `52.25%` | `0.91` | 7,280.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `23.61%` | `76.39%` | `0.31` | 23,130.00 USD |
| `1H` | `Aster` | `98.65%` | `1.35%` | `73.07` | 17,200.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `22.68%` | `77.32%` | `0.29` | 1,940.00 USD |
| `1H` | `Whale Positions` | `53.96%` | `46.04%` | `1.17` | 4,010,000.00 USD |
| `1H` | `Global Accounts` | `49.20%` | `50.80%` | `0.97` | 11,550,000.00 USD |
| `4H` | `APT` | `46.35%` | `53.65%` | `0.86` | 91,450,000.00 USD |
| `4H` | `Binance` | `47.93%` | `52.07%` | `0.92` | 33,020,000.00 USD |
| `4H` | `OKX` | `48.04%` | `51.96%` | `0.92` | 17,650,000.00 USD |
| `4H` | `Bybit` | `48.65%` | `51.35%` | `0.95` | 8,590,000.00 USD |
| `4H` | `KuCoin` | `49.02%` | `50.98%` | `0.96` | 2,240,000.00 USD |
| `4H` | `Gate` | `49.34%` | `50.66%` | `0.97` | 1,500,000.00 USD |
| `4H` | `Bitget` | `41.62%` | `58.38%` | `0.71` | 2,530,000.00 USD |
| `4H` | `BingX` | `43.44%` | `56.56%` | `0.77` | 2,620,000.00 USD |
| `4H` | `MEXC` | `53.23%` | `46.77%` | `1.14` | 1,450,000.00 USD |
| `4H` | `Bitunix` | `49.3%` | `50.7%` | `0.97` | 2,590,000.00 USD |
| `4H` | `Hyperliquid` | `52.38%` | `47.62%` | `1.10` | 431,010.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.97%` | `50.03%` | `1.00` | 14,850,000.00 USD |
| `4H` | `Crypto.com` | `24.43%` | `75.57%` | `0.32` | 389.32 USD |
| `4H` | `WhiteBIT` | `0.56%` | `99.44%` | `0.01` | 3,430,000.00 USD |
| `4H` | `HTX` | `41.18%` | `58.82%` | `0.70` | 42,880.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `21.93%` | `78.07%` | `0.28` | 219,330.00 USD |
| `4H` | `Aster` | `27.64%` | `72.36%` | `0.38` | 203,630.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `44.5%` | `55.5%` | `0.80` | 86,360.00 USD |
| `4H` | `Whale Positions` | `47.93%` | `52.07%` | `0.92` | 33,020,000.00 USD |
| `4H` | `Global Accounts` | `46.35%` | `53.65%` | `0.86` | 91,450,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.6888` | `0.6909` | `0.6888` | `0.6946` | `0.6875` | 808,356.30 USD | 277,065.63 USD | 531,290.67 USD | -254,225.03 USD | `-31.45%` | `8B / 26S` |
| `5:00 UTC` | `0.6872` | `0.6878` | `0.6872` | `0.6892` | `0.6863` | 391,857.65 USD | 178,103.21 USD | 213,754.44 USD | -35,651.23 USD | `-9.10%` | `2B / 6S` |
| `0:00 UTC` | `0.6846` | `0.6843` | `0.6846` | `0.6898` | `0.6793` | 929,091.57 USD | 323,978.58 USD | 605,112.99 USD | -281,134.41 USD | `-30.26%` | `9B / 28S` |
| `5:00 UTC` | `0.6777` | `0.6776` | `0.6777` | `0.6816` | `0.6731` | 1,052,942.47 USD | 434,240.65 USD | 618,701.82 USD | -184,461.17 USD | `-17.52%` | `7B / 24S` |
| `0:00 UTC` | `0.6792` | `0.6779` | `0.6792` | `0.6804` | `0.6751` | 597,580.45 USD | 231,458.06 USD | 366,122.39 USD | -134,664.34 USD | `-22.53%` | `11B / 12S` |
| `5:00 UTC` | `0.6769` | `0.6744` | `0.6769` | `0.6780` | `0.6712` | 1,016,262.60 USD | 354,802.44 USD | 661,460.16 USD | -306,657.72 USD | `-30.18%` | `8B / 14S` |
| `0:00 UTC` | `0.6692` | `0.6690` | `0.6692` | `0.6736` | `0.6673` | 765,890.04 USD | 348,689.76 USD | 417,200.28 USD | -68,510.51 USD | `-8.95%` | `4B / 13S` |
| `5:00 UTC` | `0.6717` | `0.6708` | `0.6717` | `0.6727` | `0.6676` | 334,763.13 USD | 213,901.71 USD | 120,861.42 USD | 93,040.30 USD | `+27.79%` | `17B / 7S` |
| `0:00 UTC` | `0.6677` | `0.6685` | `0.6677` | `0.6704` | `0.6665` | 391,631.76 USD | 249,885.86 USD | 141,745.90 USD | 108,139.96 USD | `+27.61%` | `10B / 3S` |
| `5:00 UTC` | `0.6683` | `0.6681` | `0.6683` | `0.6691` | `0.6670` | 70,879.08 USD | 44,325.21 USD | 26,553.87 USD | 17,771.34 USD | `+25.07%` | `7B / 2S` |

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
| `5m` | 1,380.00 USD | 16,150.00 USD | **`ACCUMULATION`** |
| `15m` | -2,580.00 USD | 65,350.00 USD | **`ACCUMULATION`** |
| `30m` | -12,940.00 USD | 235,840.00 USD | **`ACCUMULATION`** |
| `1h` | -74,960.00 USD | -99,670.00 USD | **`DISTRIBUTION`** |
| `2h` | -217,940.00 USD | -993,330.00 USD | **`DISTRIBUTION`** |
| `4h` | 92,610.00 USD | -1,650,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 257,750.00 USD | -2,490,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 160,060.00 USD | -3,090,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 281,320.00 USD | -2,740,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -927,290.00 USD | -7,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -4,790,000.00 USD | -20,330,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,840,000.00 USD | -101,160,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+1.38K` | 15m=`-2.58K` | 1h=`-74.96K` | 24h=`-927.29K`
* Futures Capital Netflows: 5m=`+16.15K` | 15m=`+65.35K` | 1h=`-99.67K` | 24h=`-7.00M`
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
  * `2026-10-30 00:48:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:17:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)


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
