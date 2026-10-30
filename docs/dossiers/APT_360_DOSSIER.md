# 🏛️ SOVEREIGN CANDIDATE DOSSIER: APT
**Canonical Key**: `APT` | **Broker Instrument**: `APTUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 11:14:10 IST` (`2026-10-30 05:44:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.6263` | `0.6282` | `0.6250` | `0.6266` | `158,969` | 99,608.07 USD | -16,383.00 USD | `-16.45%` | -6,429,525.74 USD | `-0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.6266` | `0.6281` | `0.6258` | `0.6261` | `132,680` | 83,169.08 USD | -38,703.52 USD | `-46.54%` | -6,468,229.26 USD | `-0.55` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.6261` | `0.6278` | `0.6249` | `0.6272` | `86,965` | 54,447.69 USD | 3,619.36 USD | `+6.65%` | -6,464,609.90 USD | `+0.46` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.6200` | `0.6265` | `0.6192` | `0.6230` | `850,201` | 529,221.91 USD | -81,784.28 USD | `-15.45%` | -6,370,965.66 USD | `-0.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.6231` | `0.6265` | `0.6226` | `0.6262` | `374,269` | 233,847.44 USD | -42,177.08 USD | `-18.04%` | -6,413,142.74 USD | `-0.75` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.6263` | `0.6282` | `0.6249` | `0.6272` | `378,513` | 237,162.00 USD | -51,486.24 USD | `-21.71%` | -6,464,628.98 USD | `-0.81` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.6032` | `0.6175` | `0.6026` | `0.6161` | `2,079,930` | 1,271,652.33 USD | 258,052.55 USD | `+20.29%` | -6,034,035.00 USD | `+0.71` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.6161` | `0.6222` | `0.6117` | `0.6199` | `2,874,646` | 1,774,946.15 USD | -165,613.15 USD | `-9.33%` | -6,199,648.15 USD | `+0.18` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.6200` | `0.6282` | `0.6192` | `0.6272` | `1,603,069` | 1,000,285.41 USD | -175,419.75 USD | `-17.54%` | -6,375,067.90 USD | `+0.18` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6721` | `0.6728` | `0.6003` | `0.6161` | `56,944,695` | 35,933,598.81 USD | -3,666,266.35 USD | `-10.20%` | -5,343,422.64 USD | `-1.60` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6162` | `0.6185` | `0.5736` | `0.6161` | `24,927,742` | 14,934,999.44 USD | -377,825.53 USD | `-2.53%` | -5,721,248.17 USD | `+0.56` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.6161` | `0.6282` | `0.6117` | `0.6272` | `4,477,629` | 2,775,177.50 USD | -341,060.76 USD | `-12.29%` | -6,062,308.92 USD | `+0.52` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -208,228.16 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -1,677,156.29 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6003` | `0.6161` | `56,944,695` | 35,933,598.81 USD | -3,666,266.35 USD | `-10.20%` | -5,343,422.64 USD | `-1.60` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6162` | `0.6185` | `0.5736` | `0.6161` | `24,927,742` | 14,934,999.44 USD | -377,825.53 USD | `-2.53%` | -5,721,248.17 USD | `+0.56` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.6161` | `0.6282` | `0.6117` | `0.6272` | `4,477,629` | 2,775,177.50 USD | -341,060.76 USD | `-12.29%` | -6,062,308.92 USD | `+0.52` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:13:49 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.6610` | 105.51 USD | `-` | `NEWS_INTEL` | `-` | #APT Liquidated Short: 0.11K USD at 0.6610 USD [API] | `2026-10-29 02:35:44` |
| `ANNOUNCEMENT` | `INFO` | `0.6668` | 238.82 USD | `-` | `NEWS_INTEL` | `-` | #APT Liquidated Short: 0.24K USD at 0.6668 USD [API] | `2026-10-29 02:05:24` |


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
| `Live` | `Long Liquidation` | `0.1395` | 419.65 USD | 210,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1855` | 824.48 USD | 209,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 269.27 USD | 208,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 227.87 USD | 208,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 230.94 USD | 208,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 2,660.00 USD | 208,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 1,460.00 USD | 205,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3165` | 426.03 USD | 204,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3175` | 1,590.00 USD | 203,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3295` | 9,370.00 USD | 202,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3305` | 543.58 USD | 192,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3545` | 177.25 USD | 192,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3585` | 12,850.00 USD | 192,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3675` | 189.99 USD | 179,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3705` | 555.75 USD | 178,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3905` | 359.26 USD | 178,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3955` | 2,640.00 USD | 178,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3995` | 271.06 USD | 175,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4025` | 281.75 USD | 175,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4125` | 1,070.00 USD | 174,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4135` | 2,020.00 USD | 173,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 630.86 USD | 171,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4255` | 224.96 USD | 171,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4365` | 5,420.00 USD | 170,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 226.63 USD | 165,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4505` | 847.55 USD | 165,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4515` | 27,090.00 USD | 164,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 5,530.00 USD | 137,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4605` | 430.79 USD | 131,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4615` | 595.82 USD | 131,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4625` | 1,460.00 USD | 130,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4645` | 876.05 USD | 129,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4685` | 468.50 USD | 128,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4735` | 4,380.00 USD | 127,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 135.33 USD | 123,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4855` | 181.88 USD | 123,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 6,000.00 USD | 123,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4875` | 165.26 USD | 117,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4925` | 10,520.00 USD | 117,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4935` | 1,580.00 USD | 106,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4945` | 7,030.00 USD | 104,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 3,180.00 USD | 97,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4965` | 143.19 USD | 94,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4975` | 667.49 USD | 94,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 429.90 USD | 93,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5075` | 303.42 USD | 93,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 102.82 USD | 93,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5105` | 519.77 USD | 93,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 248.05 USD | 92,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5135` | 298.60 USD | 92,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 9,440.00 USD | 92,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 281.56 USD | 82,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5245` | 209.80 USD | 82,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5260` | 1,350,000.00 USD | 1,350,000.00 USD | 5,850.00 USD | 0.00 USD | 3,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5280` | 1,340,000.00 USD | 1,340,000.00 USD | 5,050.00 USD | 0.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5295` | 1,840.00 USD | 82,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5300` | 1,330,000.00 USD | 1,330,000.00 USD | 5,120.00 USD | 0.00 USD | 9,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5315` | 11,510.00 USD | 80,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5320` | 1,320,000.00 USD | 1,320,000.00 USD | 8,680.00 USD | 0.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5325` | 2,260.00 USD | 68,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5335` | 163.22 USD | 66,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5340` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5360` | 1,300,000.00 USD | 1,300,000.00 USD | 2,440.00 USD | 3,040.00 USD | 44.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5380` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 1,550.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5400` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 2,920.00 USD | 57.67 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5420` | 1,290,000.00 USD | 1,290,000.00 USD | 16,260.00 USD | 1,290.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5440` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 1,150.00 USD | 13,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5445` | 855.28 USD | 66,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5460` | 1,250,000.00 USD | 1,250,000.00 USD | 2,250.00 USD | 3,030.00 USD | 5,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,630.00 USD | 65,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5480` | 1,240,000.00 USD | 1,240,000.00 USD | 2,000.00 USD | 795.70 USD | 4,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5500` | 1,170,000.00 USD | 1,170,000.00 USD | 1,410.00 USD | 0.00 USD | 6,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5500` | 1,240,000.00 USD | 1,240,000.00 USD | 5,990.00 USD | 1,440.00 USD | 6,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5510` | 1,160,000.00 USD | 1,160,000.00 USD | 1,340.00 USD | 0.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5520` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 1,050.00 USD | 38.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5520` | 1,220,000.00 USD | 1,220,000.00 USD | 4,110.00 USD | 1,920.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5530` | 1,160,000.00 USD | 1,160,000.00 USD | 1,260.00 USD | 1,410.00 USD | 5.87 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5540` | 1,160,000.00 USD | 1,160,000.00 USD | 5,390.00 USD | 5,750.00 USD | 4,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5540` | 1,210,000.00 USD | 1,210,000.00 USD | 12,840.00 USD | 7,260.00 USD | 18,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5545` | 48,560.00 USD | 63,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5550` | 1,140,000.00 USD | 1,140,000.00 USD | 2,940.00 USD | 0.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5560` | 1,140,000.00 USD | 1,140,000.00 USD | 1,680.00 USD | 686.25 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5560` | 1,180,000.00 USD | 1,180,000.00 USD | 13,490.00 USD | 1,920.00 USD | 10,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5570` | 1,140,000.00 USD | 1,140,000.00 USD | 1,690.00 USD | 2,460.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5580` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 2,820.00 USD | 2,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5580` | 1,150,000.00 USD | 1,150,000.00 USD | 6,000.00 USD | 6,820.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5585` | 10,520.00 USD | 15,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5590` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 1,870.00 USD | 1,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5600` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 1,690.00 USD | 2,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5600` | 1,120,000.00 USD | 1,120,000.00 USD | 4,070.00 USD | 8,160.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5610` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 858.33 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5615` | 258.48 USD | 4,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5620` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 776.64 USD | 2,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5620` | 1,100,000.00 USD | 1,100,000.00 USD | 19,480.00 USD | 7,420.00 USD | 11,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5630` | 1,110,000.00 USD | 1,110,000.00 USD | 1,180.00 USD | 1,560.00 USD | 5,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5635` | 244.90 USD | 4,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5640` | 1,100,000.00 USD | 1,100,000.00 USD | 4,020.00 USD | 2,420.00 USD | 10,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5640` | 1,060,000.00 USD | 1,060,000.00 USD | 2,950.00 USD | 741.21 USD | 75.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5655` | 1,920.00 USD | 4,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5660` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 3,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5660` | 1,060,000.00 USD | 1,060,000.00 USD | 11,490.00 USD | 2,990.00 USD | 4,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5665` | 1,370.00 USD | 2,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5680` | 1,040,000.00 USD | 1,040,000.00 USD | 5,100.00 USD | 0.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5690` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 5,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5700` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 1,760.00 USD | 209.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5700` | 1,030,000.00 USD | 1,030,000.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5710` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 2,350.00 USD | 77.72 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5715` | 289.08 USD | 995.18 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5720` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 832.92 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5720` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 4,370.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5730` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5740` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 839.21 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5740` | 1,020,000.00 USD | 1,020,000.00 USD | 21,620.00 USD | 1,100.00 USD | 1,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5745` | 706.11 USD | 706.11 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5750` | 1,050,000.00 USD | 1,050,000.00 USD | 4,330.00 USD | 840.09 USD | 20,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5760` | 1,030,000.00 USD | 1,030,000.00 USD | 15,020.00 USD | 2,220.00 USD | 2,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5760` | 990,890.00 USD | 990,890.00 USD | 2,150.00 USD | 7,300.00 USD | 179.10 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5770` | 1,010,000.00 USD | 1,010,000.00 USD | 16,730.00 USD | 3,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5780` | 985,830.00 USD | 985,830.00 USD | 3,070.00 USD | 1,330.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5780` | 981,260.00 USD | 981,260.00 USD | 40,930.00 USD | 0.00 USD | 1,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5790` | 970,520.00 USD | 970,520.00 USD | 11,420.00 USD | 2,690.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5800` | 948,660.00 USD | 948,660.00 USD | 3,310.00 USD | 2,750.00 USD | 1,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5800` | 938,810.00 USD | 938,810.00 USD | 1,610.00 USD | 3,900.00 USD | 27,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5810` | 940,740.00 USD | 940,740.00 USD | 0.00 USD | 3,190.00 USD | 16,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5820` | 920,670.00 USD | 920,670.00 USD | 2,580.00 USD | 4,510.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5820` | 905,540.00 USD | 905,540.00 USD | 0.00 USD | 0.00 USD | 6,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5830` | 909,360.00 USD | 909,360.00 USD | 4,910.00 USD | 819.33 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5840` | 903,630.00 USD | 903,630.00 USD | 0.00 USD | 2,190.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5840` | 898,690.00 USD | 898,690.00 USD | 0.00 USD | 0.00 USD | 21,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5850` | 897,160.00 USD | 897,160.00 USD | 2,950.00 USD | 0.00 USD | 30,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5860` | 863,440.00 USD | 863,440.00 USD | 2,810.00 USD | 3,110.00 USD | 7,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5860` | 877,390.00 USD | 877,390.00 USD | 0.00 USD | 0.00 USD | 138.04 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5870` | 849,640.00 USD | 849,640.00 USD | 15,080.00 USD | 2,310.00 USD | 52.44 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5880` | 832,200.00 USD | 832,200.00 USD | 34,650.00 USD | 10,250.00 USD | 7,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5880` | 877,250.00 USD | 877,250.00 USD | 3,110.00 USD | 16,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5890` | 779,490.00 USD | 779,490.00 USD | 38,270.00 USD | 11,450.00 USD | 15.35 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5900` | 729,750.00 USD | 729,750.00 USD | 29,060.00 USD | 13,050.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5900` | 858,140.00 USD | 858,140.00 USD | 104,240.00 USD | 1,560.00 USD | 15.37 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5910` | 677,480.00 USD | 677,480.00 USD | 26,100.00 USD | 13,220.00 USD | 18,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5920` | 620,160.00 USD | 620,160.00 USD | 25,960.00 USD | 6,190.00 USD | 7,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5920` | 752,320.00 USD | 752,320.00 USD | 11,690.00 USD | 19,960.00 USD | 75,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5930` | 580,720.00 USD | 580,720.00 USD | 6,060.00 USD | 6,380.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5940` | 555,280.00 USD | 555,280.00 USD | 15,260.00 USD | 1,300.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5940` | 645,080.00 USD | 645,080.00 USD | 10,090.00 USD | 0.00 USD | 293.47 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5950` | 530,350.00 USD | 530,350.00 USD | 26,720.00 USD | 3,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5960` | 500,410.00 USD | 500,410.00 USD | 7,830.00 USD | 1,860.00 USD | 8,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5960` | 634,690.00 USD | 634,690.00 USD | 18,180.00 USD | 18,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5970` | 482,150.00 USD | 482,150.00 USD | 13,040.00 USD | 0.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5980` | 467,110.00 USD | 467,110.00 USD | 10,410.00 USD | 2,390.00 USD | 80.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5980` | 598,100.00 USD | 598,100.00 USD | 20,380.00 USD | 0.00 USD | 46.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5990` | 454,230.00 USD | 454,230.00 USD | 0.00 USD | 836.21 USD | 1,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6000` | 452,300.00 USD | 452,300.00 USD | 0.00 USD | 2,480.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6000` | 577,670.00 USD | 577,670.00 USD | 3,320.00 USD | 0.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6010` | 444,810.00 USD | 444,810.00 USD | 2,960.00 USD | 6,370.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6020` | 430,450.00 USD | 430,450.00 USD | 2,680.00 USD | 5,050.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6020` | 569,640.00 USD | 569,640.00 USD | 0.00 USD | 8,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6030` | 421,000.00 USD | 421,000.00 USD | 34,080.00 USD | 14,050.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6040` | 369,210.00 USD | 369,210.00 USD | 6,530.00 USD | 9,900.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6040` | 561,600.00 USD | 561,600.00 USD | 38,530.00 USD | 18,680.00 USD | 139.74 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6050` | 347,750.00 USD | 347,750.00 USD | 20,690.00 USD | 1,370.00 USD | 7,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6060` | 317,750.00 USD | 317,750.00 USD | 8,400.00 USD | 0.00 USD | 50.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6060` | 504,250.00 USD | 504,250.00 USD | 0.00 USD | 0.00 USD | 20,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6070` | 309,300.00 USD | 309,300.00 USD | 8,430.00 USD | 2,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6080` | 298,270.00 USD | 298,270.00 USD | 3,650.00 USD | 3,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6080` | 483,360.00 USD | 483,360.00 USD | 2,860.00 USD | 0.00 USD | 30,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6090` | 291,450.00 USD | 291,450.00 USD | 0.00 USD | 1,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6100` | 289,830.00 USD | 289,830.00 USD | 0.00 USD | 0.00 USD | 35,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6100` | 449,930.00 USD | 449,930.00 USD | 21,400.00 USD | 47,430.00 USD | 25,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6110` | 254,660.00 USD | 254,660.00 USD | 12,430.00 USD | 3,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6120` | 238,850.00 USD | 238,850.00 USD | 30,040.00 USD | 1,670.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6120` | 355,930.00 USD | 355,930.00 USD | 35,760.00 USD | 20,330.00 USD | 18,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6130` | 204,960.00 USD | 204,960.00 USD | 39,390.00 USD | 4,950.00 USD | 28,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6140` | 132,230.00 USD | 132,230.00 USD | 6,130.00 USD | 3,530.00 USD | 19,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6140` | 281,270.00 USD | 281,270.00 USD | 51,900.00 USD | 7,220.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6160` | 103,380.00 USD | 103,380.00 USD | 0.00 USD | 0.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6160` | 217,820.00 USD | 217,820.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6180` | 100,260.00 USD | 100,260.00 USD | 0.00 USD | 1,760.00 USD | 8,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6180` | 201,230.00 USD | 201,230.00 USD | 7,600.00 USD | 0.00 USD | 107.38 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6200` | 90,140.00 USD | 90,140.00 USD | 0.00 USD | 0.00 USD | 8,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6200` | 193,520.00 USD | 193,520.00 USD | 21,280.00 USD | 0.00 USD | 29,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6210` | 81,590.00 USD | 81,590.00 USD | 5,900.00 USD | 0.00 USD | 16,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6220` | 58,820.00 USD | 58,820.00 USD | 5,630.00 USD | 2,380.00 USD | 3,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6220` | 142,990.00 USD | 142,990.00 USD | 4,760.00 USD | 22,640.00 USD | 41.73 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6240` | 46,820.00 USD | 46,820.00 USD | 21,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6240` | 115,550.00 USD | 115,550.00 USD | 0.00 USD | 7,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6250` | 25,110.00 USD | 25,110.00 USD | 16,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6260` | 8,370.00 USD | 8,370.00 USD | 0.00 USD | 8,370.00 USD | 0.07 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6260` | 108,240.00 USD | 108,240.00 USD | 108,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6270` | 47,830.00 USD | 47,830.00 USD | 47,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6270` | 95,660.00 USD | 95,660.00 USD | 47,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6280` | 144,740.00 USD | 144,740.00 USD | 9,840.00 USD | 16,420.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6280` | 86,520.00 USD | 86,520.00 USD | 38,530.00 USD | 22,580.00 USD | 25,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6285` | 10,370.00 USD | 10,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6290` | 186,430.00 USD | 186,430.00 USD | 20,690.00 USD | 6,580.00 USD | 14,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6300` | 210,040.00 USD | 210,040.00 USD | 10,980.00 USD | 3,430.00 USD | 9,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6300` | 135,980.00 USD | 135,980.00 USD | 0.00 USD | 0.00 USD | 49,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6310` | 262,010.00 USD | 262,010.00 USD | 22,880.00 USD | 7,390.00 USD | 21,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6320` | 313,180.00 USD | 313,180.00 USD | 34,120.00 USD | 6,080.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6320` | 136,210.00 USD | 136,210.00 USD | 0.00 USD | 0.00 USD | 233.05 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6330` | 356,890.00 USD | 356,890.00 USD | 14,500.00 USD | 10,960.00 USD | 18,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6340` | 424,110.00 USD | 424,110.00 USD | 29,640.00 USD | 3,190.00 USD | 34,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6340` | 205,330.00 USD | 205,330.00 USD | 68,660.00 USD | 0.00 USD | 448.08 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6350` | 471,470.00 USD | 471,470.00 USD | 39,480.00 USD | 1,700.00 USD | 6,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6360` | 590,100.00 USD | 590,100.00 USD | 54,130.00 USD | 4,140.00 USD | 60,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6360` | 296,680.00 USD | 296,680.00 USD | 34,320.00 USD | 0.00 USD | 57,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6370` | 621,870.00 USD | 621,870.00 USD | 0.00 USD | 5,010.00 USD | 26,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6380` | 656,400.00 USD | 656,400.00 USD | 0.00 USD | 28,210.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6380` | 335,980.00 USD | 335,980.00 USD | 0.00 USD | 0.00 USD | 39,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6390` | 740,160.00 USD | 740,160.00 USD | 26,050.00 USD | 7,210.00 USD | 50,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6400` | 887,910.00 USD | 887,910.00 USD | 72,890.00 USD | 39,010.00 USD | 35,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6400` | 376,440.00 USD | 376,440.00 USD | 19,270.00 USD | 7,510.00 USD | 13,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6410` | 952,670.00 USD | 952,670.00 USD | 35,660.00 USD | 14,660.00 USD | 14,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6420` | 1,070,000.00 USD | 1,070,000.00 USD | 75,040.00 USD | 15,540.00 USD | 23,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6420` | 512,710.00 USD | 512,710.00 USD | 55,350.00 USD | 44,770.00 USD | 36,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6430` | 1,140,000.00 USD | 1,140,000.00 USD | 36,780.00 USD | 13,280.00 USD | 23,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6440` | 1,240,000.00 USD | 1,240,000.00 USD | 31,190.00 USD | 18,570.00 USD | 48,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6440` | 599,880.00 USD | 599,880.00 USD | 44,690.00 USD | 24,820.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6450` | 1,350,000.00 USD | 1,350,000.00 USD | 61,360.00 USD | 12,700.00 USD | 35,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6460` | 1,410,000.00 USD | 1,410,000.00 USD | 42,970.00 USD | 12,100.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6460` | 957,770.00 USD | 957,770.00 USD | 172,610.00 USD | 46,630.00 USD | 138,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6465` | 867.43 USD | 11,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6470` | 1,500,000.00 USD | 1,500,000.00 USD | 59,430.00 USD | 17,210.00 USD | 8,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6475` | 209.47 USD | 11,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6480` | 1,580,000.00 USD | 1,580,000.00 USD | 70,780.00 USD | 7,630.00 USD | 132.92 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6480` | 1,100,000.00 USD | 1,100,000.00 USD | 86,440.00 USD | 26,520.00 USD | 33,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6490` | 1,660,000.00 USD | 1,660,000.00 USD | 63,670.00 USD | 2,070.00 USD | 12,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6500` | 1,710,000.00 USD | 1,710,000.00 USD | 41,800.00 USD | 8,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6500` | 1,310,000.00 USD | 1,310,000.00 USD | 73,560.00 USD | 0.00 USD | 132,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6510` | 1,780,000.00 USD | 1,780,000.00 USD | 58,460.00 USD | 0.00 USD | 14,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6520` | 1,890,000.00 USD | 1,890,000.00 USD | 93,550.00 USD | 10,800.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6520` | 1,720,000.00 USD | 1,720,000.00 USD | 298,050.00 USD | 10,910.00 USD | 105,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6530` | 1,900,000.00 USD | 1,900,000.00 USD | 11,510.00 USD | 3,910.00 USD | 77.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6540` | 1,940,000.00 USD | 1,940,000.00 USD | 24,280.00 USD | 0.00 USD | 10,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6540` | 1,810,000.00 USD | 1,810,000.00 USD | 15,730.00 USD | 4,440.00 USD | 61,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6550` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 7,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6560` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 8,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6560` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 5,380.00 USD | 982.82 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6570` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6580` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 3,310.00 USD | 234.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6580` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 28,280.00 USD | 10,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6590` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 5,890.00 USD | 77.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6600` | 1,980,000.00 USD | 1,980,000.00 USD | 6,010.00 USD | 9,280.00 USD | 69.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6600` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 18,420.00 USD | 776.62 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6610` | 1,990,000.00 USD | 1,990,000.00 USD | 6,690.00 USD | 835.70 USD | 63.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6620` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 530.84 USD | 7,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6620` | 1,880,000.00 USD | 1,880,000.00 USD | 8,600.00 USD | 0.00 USD | 420.03 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6630` | 2,000,000.00 USD | 2,000,000.00 USD | 2,590.00 USD | 0.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6640` | 2,020,000.00 USD | 2,020,000.00 USD | 11,190.00 USD | 837.01 USD | 62.52 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6640` | 1,920,000.00 USD | 1,920,000.00 USD | 33,660.00 USD | 0.00 USD | 7,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6650` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 3,160.00 USD | 17,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6660` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 839.67 USD | 7,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6660` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 6,770.00 USD | 667.93 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6670` | 2,060,000.00 USD | 2,060,000.00 USD | 18,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6680` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 617.06 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6690` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 3,550.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6700` | 2,110,000.00 USD | 2,110,000.00 USD | 8,830.00 USD | 1,920.00 USD | 24,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6700` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 953.62 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6710` | 2,160,000.00 USD | 2,160,000.00 USD | 41,970.00 USD | 0.00 USD | 6,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6720` | 2,160,000.00 USD | 2,160,000.00 USD | 1,410.00 USD | 0.00 USD | 85.60 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6720` | 2,020,000.00 USD | 2,020,000.00 USD | 58,470.00 USD | 0.00 USD | 30,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6730` | 2,190,000.00 USD | 2,190,000.00 USD | 25,660.00 USD | 3,670.00 USD | 5,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6740` | 2,270,000.00 USD | 2,270,000.00 USD | 64,370.00 USD | 8,170.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6740` | 2,060,000.00 USD | 2,060,000.00 USD | 39,730.00 USD | 0.00 USD | 43.92 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6750` | 2,320,000.00 USD | 2,320,000.00 USD | 28,700.00 USD | 4,630.00 USD | 12,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6760` | 2,340,000.00 USD | 2,340,000.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6760` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 77,970.00 USD | 33,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6770` | 2,380,000.00 USD | 2,380,000.00 USD | 19,930.00 USD | 8,320.00 USD | 15,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6780` | 2,440,000.00 USD | 2,440,000.00 USD | 33,610.00 USD | 13,860.00 USD | 12,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6780` | 2,270,000.00 USD | 2,270,000.00 USD | 63,600.00 USD | 16,810.00 USD | 18,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6790` | 2,470,000.00 USD | 2,470,000.00 USD | 2,940.00 USD | 18,610.00 USD | 12,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6800` | 2,480,000.00 USD | 2,480,000.00 USD | 1,680.00 USD | 686.25 USD | 2,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6800` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 16,590.00 USD | 4,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6810` | 2,500,000.00 USD | 2,500,000.00 USD | 1,690.00 USD | 2,460.00 USD | 11,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6820` | 2,540,000.00 USD | 2,540,000.00 USD | 22,600.00 USD | 16,590.00 USD | 9,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6820` | 2,370,000.00 USD | 2,370,000.00 USD | 32,570.00 USD | 53,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6830` | 2,620,000.00 USD | 2,620,000.00 USD | 24,570.00 USD | 17,300.00 USD | 36,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6840` | 2,700,000.00 USD | 2,700,000.00 USD | 45,780.00 USD | 17,210.00 USD | 13,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6840` | 2,590,000.00 USD | 2,590,000.00 USD | 57,890.00 USD | 54,300.00 USD | 102,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6850` | 2,770,000.00 USD | 2,770,000.00 USD | 39,200.00 USD | 5,780.00 USD | 24,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6860` | 2,830,000.00 USD | 2,830,000.00 USD | 40,250.00 USD | 4,380.00 USD | 14,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6860` | 2,660,000.00 USD | 2,660,000.00 USD | 49,930.00 USD | 14,540.00 USD | 10,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6870` | 2,900,000.00 USD | 2,900,000.00 USD | 63,220.00 USD | 1,160.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6880` | 2,950,000.00 USD | 2,950,000.00 USD | 14,350.00 USD | 11,160.00 USD | 25,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6880` | 2,720,000.00 USD | 2,720,000.00 USD | 38,030.00 USD | 17,300.00 USD | 125.32 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6890` | 2,960,000.00 USD | 2,960,000.00 USD | 1,180.00 USD | 0.00 USD | 8,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6900` | 3,000,000.00 USD | 3,000,000.00 USD | 18,600.00 USD | 4,030.00 USD | 21,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6900` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 15,510.00 USD | 16,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6910` | 3,060,000.00 USD | 3,060,000.00 USD | 28,860.00 USD | 1,730.00 USD | 32,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6920` | 3,090,000.00 USD | 3,090,000.00 USD | 16,800.00 USD | 0.00 USD | 13,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6920` | 2,890,000.00 USD | 2,890,000.00 USD | 69,620.00 USD | 2,090.00 USD | 61,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6930` | 3,100,000.00 USD | 3,100,000.00 USD | 10,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6940` | 2,940,000.00 USD | 2,940,000.00 USD | 14,220.00 USD | 0.00 USD | 42,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6960` | 3,010,000.00 USD | 3,010,000.00 USD | 59,960.00 USD | 0.00 USD | 12,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6980` | 3,070,000.00 USD | 3,070,000.00 USD | 35,980.00 USD | 16,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6995` | 52,350.00 USD | 63,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7000` | 3,140,000.00 USD | 3,140,000.00 USD | 29,740.00 USD | 0.00 USD | 40,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7020` | 3,220,000.00 USD | 3,220,000.00 USD | 29,810.00 USD | 0.00 USD | 53,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7040` | 3,410,000.00 USD | 3,410,000.00 USD | 95,520.00 USD | 0.00 USD | 96,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7060` | 3,670,000.00 USD | 3,670,000.00 USD | 47,840.00 USD | 33,490.00 USD | 177,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7080` | 3,840,000.00 USD | 3,840,000.00 USD | 24,440.00 USD | 64,870.00 USD | 83,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7100` | 4,210,000.00 USD | 4,210,000.00 USD | 150,830.00 USD | 63,530.00 USD | 149,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7120` | 4,610,000.00 USD | 4,610,000.00 USD | 101,040.00 USD | 78,760.00 USD | 227,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7140` | 5,020,000.00 USD | 5,020,000.00 USD | 202,560.00 USD | 67,260.00 USD | 133,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7160` | 5,360,000.00 USD | 5,360,000.00 USD | 113,040.00 USD | 65,260.00 USD | 164,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7180` | 5,650,000.00 USD | 5,650,000.00 USD | 165,860.00 USD | 56,910.00 USD | 66,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7200` | 5,970,000.00 USD | 5,970,000.00 USD | 93,750.00 USD | 45,160.00 USD | 178,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7220` | 6,450,000.00 USD | 6,450,000.00 USD | 318,420.00 USD | 67,130.00 USD | 98,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7240` | 6,750,000.00 USD | 6,750,000.00 USD | 146,110.00 USD | 24,910.00 USD | 129,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7245` | 364.39 USD | 64,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7260` | 7,090,000.00 USD | 7,090,000.00 USD | 106,410.00 USD | 52,120.00 USD | 176,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7280` | 7,310,000.00 USD | 7,310,000.00 USD | 99,750.00 USD | 40,180.00 USD | 84,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7300` | 7,600,000.00 USD | 7,600,000.00 USD | 115,310.00 USD | 60,310.00 USD | 109,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7320` | 7,930,000.00 USD | 7,930,000.00 USD | 189,840.00 USD | 65,640.00 USD | 80,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7340` | 8,030,000.00 USD | 8,030,000.00 USD | 31,260.00 USD | 8,620.00 USD | 56,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7360` | 8,210,000.00 USD | 8,210,000.00 USD | 103,600.00 USD | 42,680.00 USD | 34,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7380` | 8,360,000.00 USD | 8,360,000.00 USD | 73,710.00 USD | 19,000.00 USD | 60,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7400` | 8,380,000.00 USD | 8,380,000.00 USD | 1,730.00 USD | 4,760.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7420` | 8,480,000.00 USD | 8,480,000.00 USD | 35,810.00 USD | 35,860.00 USD | 31,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7440` | 8,660,000.00 USD | 8,660,000.00 USD | 74,450.00 USD | 33,900.00 USD | 70,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7460` | 8,820,000.00 USD | 8,820,000.00 USD | 88,800.00 USD | 17,230.00 USD | 51,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7480` | 8,950,000.00 USD | 8,950,000.00 USD | 60,580.00 USD | 28,900.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7500` | 9,040,000.00 USD | 9,040,000.00 USD | 52,320.00 USD | 12,610.00 USD | 25,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7520` | 9,160,000.00 USD | 9,160,000.00 USD | 53,470.00 USD | 13,000.00 USD | 50,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7530` | 9,190,000.00 USD | 9,190,000.00 USD | 21,290.00 USD | 1,890.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7725` | 165.62 USD | 64,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8005` | 19,120.00 USD | 83,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8665` | 378.95 USD | 83,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9055` | 23,320.00 USD | 107,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9935` | 17,700.00 USD | 124,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.02` | 25,970.00 USD | 150,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.04` | 5,200.00 USD | 156,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 82,980.00 USD | 238,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 479.74 USD | 239,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.12` | 2,800.00 USD | 242,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.17` | 501.44 USD | 242,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 227.46 USD | 243,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 199.98 USD | 243,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 796.83 USD | 243,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1395` | 210,190.00 USD | 0.00 USD | 419.65 USD | `-77.51%` | `3,008.22` |
| `Live` | `Long` | `0.1855` | 209,770.00 USD | 0.00 USD | 824.48 USD | `-70.09%` | `4,444.65` |
| `Live` | `Long` | `0.1875` | 208,950.00 USD | 0.00 USD | 269.27 USD | `-69.77%` | `1,436.09` |
| `Live` | `Long` | `0.2195` | 208,680.00 USD | 0.00 USD | 227.87 USD | `-64.61%` | `1,038.12` |
| `Live` | `Long` | `0.2295` | 208,450.00 USD | 0.00 USD | 230.94 USD | `-63.00%` | `1,006.27` |
| `Live` | `Long` | `0.2355` | 208,220.00 USD | 0.00 USD | 2,660.00 USD | `-62.03%` | `11,284.25` |
| `Live` | `Long` | `0.2425` | 205,560.00 USD | 0.00 USD | 1,460.00 USD | `-60.90%` | `6,000.00` |
| `Live` | `Long` | `0.3165` | 204,110.00 USD | 0.00 USD | 426.03 USD | `-48.97%` | `1,346.06` |
| `Live` | `Long` | `0.3175` | 203,680.00 USD | 0.00 USD | 1,590.00 USD | `-48.81%` | `5,000.00` |
| `Live` | `Long` | `0.3295` | 202,100.00 USD | 0.00 USD | 9,370.00 USD | `-46.87%` | `28,446.85` |
| `Live` | `Long` | `0.3305` | 192,720.00 USD | 0.00 USD | 543.58 USD | `-46.71%` | `1,644.73` |
| `Live` | `Long` | `0.3545` | 192,180.00 USD | 0.00 USD | 177.25 USD | `-42.84%` | `500.00` |
| `Live` | `Long` | `0.3585` | 192,000.00 USD | 0.00 USD | 12,850.00 USD | `-42.20%` | `35,856.81` |
| `Live` | `Long` | `0.3675` | 179,150.00 USD | 0.00 USD | 189.99 USD | `-40.74%` | `516.98` |
| `Live` | `Long` | `0.3705` | 178,960.00 USD | 0.00 USD | 555.75 USD | `-40.26%` | `1,500.00` |
| `Live` | `Long` | `0.3905` | 178,400.00 USD | 0.00 USD | 359.26 USD | `-37.04%` | `919.99` |
| `Live` | `Long` | `0.3955` | 178,040.00 USD | 0.00 USD | 2,640.00 USD | `-36.23%` | `6,686.27` |
| `Live` | `Long` | `0.3995` | 175,400.00 USD | 0.00 USD | 271.06 USD | `-35.59%` | `678.49` |
| `Live` | `Long` | `0.4025` | 175,130.00 USD | 0.00 USD | 281.75 USD | `-35.10%` | `700.00` |
| `Live` | `Long` | `0.4125` | 174,850.00 USD | 0.00 USD | 1,070.00 USD | `-33.49%` | `2,600.00` |
| `Live` | `Long` | `0.4135` | 173,770.00 USD | 0.00 USD | 2,020.00 USD | `-33.33%` | `4,881.41` |
| `Live` | `Long` | `0.4185` | 171,750.00 USD | 0.00 USD | 630.86 USD | `-32.52%` | `1,507.44` |
| `Live` | `Long` | `0.4255` | 171,120.00 USD | 0.00 USD | 224.96 USD | `-31.39%` | `528.69` |
| `Live` | `Long` | `0.4365` | 170,900.00 USD | 0.00 USD | 5,420.00 USD | `-29.62%` | `12,426.15` |
| `Live` | `Long` | `0.4475` | 165,470.00 USD | 0.00 USD | 226.63 USD | `-27.85%` | `506.43` |
| `Live` | `Long` | `0.4505` | 165,250.00 USD | 0.00 USD | 847.55 USD | `-27.36%` | `1,881.36` |
| `Live` | `Long` | `0.4515` | 164,400.00 USD | 0.00 USD | 27,090.00 USD | `-27.20%` | `60,000.00` |
| `Live` | `Long` | `0.4535` | 137,310.00 USD | 0.00 USD | 5,530.00 USD | `-26.88%` | `12,191.83` |
| `Live` | `Long` | `0.4605` | 131,780.00 USD | 0.00 USD | 430.79 USD | `-25.75%` | `935.49` |
| `Live` | `Long` | `0.4615` | 131,350.00 USD | 0.00 USD | 595.82 USD | `-25.59%` | `1,291.05` |
| `Live` | `Long` | `0.4625` | 130,750.00 USD | 0.00 USD | 1,460.00 USD | `-25.43%` | `3,156.35` |
| `Live` | `Long` | `0.4645` | 129,290.00 USD | 0.00 USD | 876.05 USD | `-25.10%` | `1,886.00` |
| `Live` | `Long` | `0.4685` | 128,420.00 USD | 0.00 USD | 468.50 USD | `-24.46%` | `1,000.00` |
| `Live` | `Long` | `0.4735` | 127,950.00 USD | 0.00 USD | 4,380.00 USD | `-23.65%` | `9,243.24` |
| `Live` | `Long` | `0.4835` | 123,570.00 USD | 0.00 USD | 135.33 USD | `-22.04%` | `279.90` |
| `Live` | `Long` | `0.4855` | 123,440.00 USD | 0.00 USD | 181.88 USD | `-21.72%` | `374.62` |
| `Live` | `Long` | `0.4865` | 123,260.00 USD | 0.00 USD | 6,000.00 USD | `-21.56%` | `12,332.05` |
| `Live` | `Long` | `0.4875` | 117,260.00 USD | 0.00 USD | 165.26 USD | `-21.40%` | `339.00` |
| `Live` | `Long` | `0.4925` | 117,090.00 USD | 0.00 USD | 10,520.00 USD | `-20.59%` | `21,364.96` |
| `Live` | `Long` | `0.4935` | 106,570.00 USD | 0.00 USD | 1,580.00 USD | `-20.43%` | `3,199.85` |
| `Live` | `Long` | `0.4945` | 104,990.00 USD | 0.00 USD | 7,030.00 USD | `-20.27%` | `14,223.31` |
| `Live` | `Long` | `0.4955` | 97,960.00 USD | 0.00 USD | 3,180.00 USD | `-20.11%` | `6,422.59` |
| `Live` | `Long` | `0.4965` | 94,770.00 USD | 0.00 USD | 143.19 USD | `-19.95%` | `288.40` |
| `Live` | `Long` | `0.4975` | 94,630.00 USD | 0.00 USD | 667.49 USD | `-19.78%` | `1,341.68` |
| `Live` | `Long` | `0.4985` | 93,960.00 USD | 0.00 USD | 429.90 USD | `-19.62%` | `862.38` |
| `Live` | `Long` | `0.5075` | 93,530.00 USD | 0.00 USD | 303.42 USD | `-18.17%` | `597.87` |
| `Live` | `Long` | `0.5085` | 93,230.00 USD | 0.00 USD | 102.82 USD | `-18.01%` | `202.20` |
| `Live` | `Long` | `0.5105` | 93,130.00 USD | 0.00 USD | 519.77 USD | `-17.69%` | `1,018.15` |
| `Live` | `Long` | `0.5125` | 92,610.00 USD | 0.00 USD | 248.05 USD | `-17.37%` | `484.00` |
| `Live` | `Long` | `0.5135` | 92,360.00 USD | 0.00 USD | 298.60 USD | `-17.20%` | `581.49` |
| `Live` | `Long` | `0.5175` | 92,060.00 USD | 0.00 USD | 9,440.00 USD | `-16.56%` | `18,249.92` |
| `Live` | `Long` | `0.5185` | 82,620.00 USD | 0.00 USD | 281.56 USD | `-16.40%` | `543.02` |
| `Live` | `Long` | `0.5245` | 82,340.00 USD | 0.00 USD | 209.80 USD | `-15.43%` | `400.00` |
| `Live` | `Long` | `0.5295` | 82,130.00 USD | 0.00 USD | 1,840.00 USD | `-14.62%` | `3,467.51` |
| `Live` | `Long` | `0.5315` | 80,290.00 USD | 0.00 USD | 11,510.00 USD | `-14.30%` | `21,664.95` |
| `Live` | `Long` | `0.5325` | 68,770.00 USD | 0.00 USD | 2,260.00 USD | `-14.14%` | `4,240.81` |
| `Live` | `Long` | `0.5335` | 66,520.00 USD | 0.00 USD | 163.22 USD | `-13.98%` | `305.95` |
| `Live` | `Long` | `0.5445` | 66,350.00 USD | 0.00 USD | 855.28 USD | `-12.21%` | `1,570.77` |
| `Live` | `Long` | `0.5475` | 65,500.00 USD | 0.00 USD | 1,630.00 USD | `-11.72%` | `2,968.46` |
| `Live` | `Long` | `0.5545` | 63,870.00 USD | 0.00 USD | 48,560.00 USD | `-10.59%` | `87,579.81` |
| `Live` | `Long` | `0.5585` | 15,310.00 USD | 0.00 USD | 10,520.00 USD | `-9.95%` | `18,834.52` |
| `Live` | `Long` | `0.5615` | 4,790.00 USD | 0.00 USD | 258.48 USD | `-9.46%` | `460.33` |
| `Live` | `Long` | `0.5635` | 4,530.00 USD | 0.00 USD | 244.90 USD | `-9.14%` | `434.61` |
| `Live` | `Long` | `0.5655` | 4,290.00 USD | 0.00 USD | 1,920.00 USD | `-8.82%` | `3,394.98` |
| `Live` | `Long` | `0.5665` | 2,370.00 USD | 0.00 USD | 1,370.00 USD | `-8.66%` | `2,421.90` |
| `Live` | `Long` | `0.5715` | 995.18 USD | 0.00 USD | 289.08 USD | `-7.85%` | `505.82` |
| `Live` | `Long` | `0.5745` | 706.11 USD | 0.00 USD | 706.11 USD | `-7.37%` | `1,229.08` |
| `Live` | `Short` | `0.6285` | 10,370.00 USD | 10,370.00 USD | 0.00 USD | `+1.34%` | `16,500.00` |
| `Live` | `Short` | `0.6465` | 11,240.00 USD | 867.43 USD | 0.00 USD | `+4.24%` | `1,341.73` |
| `Live` | `Short` | `0.6475` | 11,450.00 USD | 209.47 USD | 0.00 USD | `+4.40%` | `323.51` |
| `Live` | `Short` | `0.6995` | 63,800.00 USD | 52,350.00 USD | 0.00 USD | `+12.79%` | `74,837.79` |
| `Live` | `Short` | `0.7245` | 64,160.00 USD | 364.39 USD | 0.00 USD | `+16.82%` | `502.96` |
| `Live` | `Short` | `0.7725` | 64,330.00 USD | 165.62 USD | 0.00 USD | `+24.56%` | `214.40` |
| `Live` | `Short` | `0.8005` | 83,440.00 USD | 19,120.00 USD | 0.00 USD | `+29.07%` | `23,882.80` |
| `Live` | `Short` | `0.8665` | 83,820.00 USD | 378.95 USD | 0.00 USD | `+39.71%` | `437.33` |
| `Live` | `Short` | `0.9055` | 107,150.00 USD | 23,320.00 USD | 0.00 USD | `+46.00%` | `25,756.98` |
| `Live` | `Short` | `0.9935` | 124,850.00 USD | 17,700.00 USD | 0.00 USD | `+60.19%` | `17,815.24` |
| `Live` | `Short` | `1.02` | 150,820.00 USD | 25,970.00 USD | 0.00 USD | `+64.70%` | `25,423.72` |
| `Live` | `Short` | `1.04` | 156,010.00 USD | 5,200.00 USD | 0.00 USD | `+67.61%` | `5,000.00` |
| `Live` | `Short` | `1.09` | 238,990.00 USD | 82,980.00 USD | 0.00 USD | `+75.35%` | `76,300.00` |
| `Live` | `Short` | `1.09` | 239,470.00 USD | 479.74 USD | 0.00 USD | `+75.99%` | `439.52` |
| `Live` | `Short` | `1.12` | 242,270.00 USD | 2,800.00 USD | 0.00 USD | `+80.51%` | `2,500.00` |
| `Live` | `Short` | `1.17` | 242,770.00 USD | 501.44 USD | 0.00 USD | `+89.21%` | `427.30` |
| `Live` | `Short` | `1.19` | 243,000.00 USD | 227.46 USD | 0.00 USD | `+91.31%` | `191.71` |
| `Live` | `Short` | `1.19` | 243,200.00 USD | 199.98 USD | 0.00 USD | `+91.63%` | `168.26` |
| `Live` | `Short` | `1.22` | 243,990.00 USD | 796.83 USD | 0.00 USD | `+96.95%` | `652.34` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.3505` | 167,110.00 USD | 0.00 USD | 340.19 USD | `-43.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4635` | 166,770.00 USD | 0.00 USD | 104.57 USD | `-25.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4955` | 166,670.00 USD | 0.00 USD | 111.62 USD | `-20.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4965` | 166,560.00 USD | 0.00 USD | 111.85 USD | `-19.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 166,440.00 USD | 0.00 USD | 67,850.00 USD | `-19.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5015` | 98,600.00 USD | 0.00 USD | 112.97 USD | `-19.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5065` | 98,480.00 USD | 0.00 USD | 225.65 USD | `-18.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5085` | 98,260.00 USD | 0.00 USD | 101.97 USD | `-18.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5115` | 98,160.00 USD | 0.00 USD | 111.69 USD | `-17.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5125` | 98,050.00 USD | 0.00 USD | 5,380.00 USD | `-17.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 92,660.00 USD | 0.00 USD | 115.47 USD | `-16.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5175` | 92,550.00 USD | 0.00 USD | 116.58 USD | `-16.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5185` | 92,430.00 USD | 0.00 USD | 116.96 USD | `-16.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5205` | 92,320.00 USD | 0.00 USD | 539.96 USD | `-16.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5225` | 91,780.00 USD | 0.00 USD | 117.70 USD | `-15.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5235` | 91,660.00 USD | 0.00 USD | 117.93 USD | `-15.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5305` | 91,540.00 USD | 0.00 USD | 770.19 USD | `-14.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5445` | 90,770.00 USD | 0.00 USD | 8,750.00 USD | `-12.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5455` | 82,010.00 USD | 0.00 USD | 8,150.00 USD | `-12.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5485` | 73,860.00 USD | 0.00 USD | 4,500.00 USD | `-11.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5515` | 69,370.00 USD | 0.00 USD | 126.71 USD | `-11.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5525` | 69,240.00 USD | 0.00 USD | 126.90 USD | `-10.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5555` | 69,110.00 USD | 0.00 USD | 33,000.00 USD | `-10.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5565` | 36,120.00 USD | 0.00 USD | 173.58 USD | `-10.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5595` | 35,940.00 USD | 0.00 USD | 10,540.00 USD | `-9.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 25,410.00 USD | 0.00 USD | 339.84 USD | `-9.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5625` | 25,070.00 USD | 0.00 USD | 930.52 USD | `-9.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5655` | 24,140.00 USD | 0.00 USD | 127.62 USD | `-8.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5695` | 24,010.00 USD | 0.00 USD | 127.30 USD | `-8.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5705` | 23,880.00 USD | 0.00 USD | 9,410.00 USD | `-8.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5715` | 14,470.00 USD | 0.00 USD | 127.63 USD | `-7.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5735` | 14,340.00 USD | 0.00 USD | 151.62 USD | `-7.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5755` | 14,190.00 USD | 0.00 USD | 999.82 USD | `-7.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5775` | 13,190.00 USD | 0.00 USD | 1,710.00 USD | `-6.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5785` | 11,470.00 USD | 0.00 USD | 127.36 USD | `-6.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5795` | 11,350.00 USD | 0.00 USD | 780.04 USD | `-6.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5815` | 10,570.00 USD | 0.00 USD | 127.27 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5835` | 10,440.00 USD | 0.00 USD | 999.65 USD | `-5.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5845` | 9,440.00 USD | 0.00 USD | 533.37 USD | `-5.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5905` | 8,910.00 USD | 0.00 USD | 127.30 USD | `-4.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5925` | 8,780.00 USD | 0.00 USD | 265.69 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5975` | 8,510.00 USD | 0.00 USD | 597.80 USD | `-3.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5995` | 7,920.00 USD | 0.00 USD | 509.04 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 7,410.00 USD | 0.00 USD | 953.02 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6045` | 6,450.00 USD | 0.00 USD | 999.99 USD | `-2.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 5,450.00 USD | 0.00 USD | 1,510.00 USD | `-2.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6065` | 3,950.00 USD | 0.00 USD | 1,910.00 USD | `-2.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6085` | 2,040.00 USD | 0.00 USD | 301.32 USD | `-1.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6115` | 1,740.00 USD | 0.00 USD | 629.83 USD | `-1.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6135` | 1,110.00 USD | 0.00 USD | 410.30 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6175` | 696.72 USD | 0.00 USD | 519.13 USD | `-0.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6185` | 177.58 USD | 0.00 USD | 177.58 USD | `-0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6205` | 1,120.00 USD | 1,120.00 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6225` | 2,120.00 USD | 1,000.00 USD | 0.00 USD | `+0.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6275` | 2,560.00 USD | 433.11 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6285` | 3,030.00 USD | 469.94 USD | 0.00 USD | `+1.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 7,450.00 USD | 4,430.00 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 7,720.00 USD | 269.44 USD | 0.00 USD | `+1.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6335` | 16,120.00 USD | 8,390.00 USD | 0.00 USD | `+2.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6345` | 16,390.00 USD | 276.40 USD | 0.00 USD | `+2.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6395` | 17,590.00 USD | 1,200.00 USD | 0.00 USD | `+3.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6405` | 17,740.00 USD | 145.91 USD | 0.00 USD | `+3.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6445` | 17,860.00 USD | 121.42 USD | 0.00 USD | `+3.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6465` | 18,270.00 USD | 410.21 USD | 0.00 USD | `+4.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6485` | 18,720.00 USD | 447.03 USD | 0.00 USD | `+4.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6505` | 19,290.00 USD | 567.58 USD | 0.00 USD | `+4.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6525` | 19,460.00 USD | 172.51 USD | 0.00 USD | `+5.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6555` | 23,540.00 USD | 4,080.00 USD | 0.00 USD | `+5.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6585` | 24,980.00 USD | 1,440.00 USD | 0.00 USD | `+6.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6595` | 25,720.00 USD | 746.46 USD | 0.00 USD | `+6.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6605` | 26,300.00 USD | 580.23 USD | 0.00 USD | `+6.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6635` | 26,590.00 USD | 289.66 USD | 0.00 USD | `+6.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6645` | 26,850.00 USD | 262.60 USD | 0.00 USD | `+7.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6655` | 27,140.00 USD | 283.50 USD | 0.00 USD | `+7.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6675` | 27,430.00 USD | 290.78 USD | 0.00 USD | `+7.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6695` | 29,100.00 USD | 1,670.00 USD | 0.00 USD | `+7.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6705` | 29,260.00 USD | 162.91 USD | 0.00 USD | `+8.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6725` | 30,930.00 USD | 1,670.00 USD | 0.00 USD | `+8.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6745` | 31,530.00 USD | 598.31 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 31,690.00 USD | 154.30 USD | 0.00 USD | `+9.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6805` | 31,900.00 USD | 214.20 USD | 0.00 USD | `+9.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6815` | 42,460.00 USD | 10,560.00 USD | 0.00 USD | `+9.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6825` | 42,570.00 USD | 112.49 USD | 0.00 USD | `+10.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6845` | 43,710.00 USD | 1,130.00 USD | 0.00 USD | `+10.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6875` | 43,850.00 USD | 140.41 USD | 0.00 USD | `+10.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6885` | 44,360.00 USD | 514.80 USD | 0.00 USD | `+11.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6915` | 44,460.00 USD | 101.96 USD | 0.00 USD | `+11.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6925` | 45,480.00 USD | 1,020.00 USD | 0.00 USD | `+11.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6945` | 46,090.00 USD | 610.10 USD | 0.00 USD | `+11.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6955` | 46,200.00 USD | 101.38 USD | 0.00 USD | `+12.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6965` | 46,980.00 USD | 789.18 USD | 0.00 USD | `+12.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6985` | 47,090.00 USD | 102.99 USD | 0.00 USD | `+12.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7005` | 47,200.00 USD | 111.08 USD | 0.00 USD | `+12.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7015` | 47,890.00 USD | 694.49 USD | 0.00 USD | `+13.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7095` | 48,030.00 USD | 132.99 USD | 0.00 USD | `+14.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7115` | 48,150.00 USD | 122.04 USD | 0.00 USD | `+14.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7165` | 49,980.00 USD | 1,830.00 USD | 0.00 USD | `+15.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7195` | 50,170.00 USD | 183.26 USD | 0.00 USD | `+16.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7205` | 50,310.00 USD | 147.15 USD | 0.00 USD | `+16.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7265` | 56,600.00 USD | 6,290.00 USD | 0.00 USD | `+17.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7275` | 56,910.00 USD | 309.91 USD | 0.00 USD | `+17.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7325` | 57,080.00 USD | 165.17 USD | 0.00 USD | `+18.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7345` | 58,110.00 USD | 1,030.00 USD | 0.00 USD | `+18.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7405` | 58,840.00 USD | 733.09 USD | 0.00 USD | `+19.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7415` | 59,000.00 USD | 156.98 USD | 0.00 USD | `+19.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7445` | 59,180.00 USD | 185.43 USD | 0.00 USD | `+20.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7455` | 61,350.00 USD | 2,170.00 USD | 0.00 USD | `+20.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7475` | 61,670.00 USD | 318.43 USD | 0.00 USD | `+20.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7505` | 61,810.00 USD | 141.39 USD | 0.00 USD | `+21.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7565` | 65,920.00 USD | 4,120.00 USD | 0.00 USD | `+21.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7575` | 66,440.00 USD | 511.82 USD | 0.00 USD | `+22.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7615` | 67,310.00 USD | 875.23 USD | 0.00 USD | `+22.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7635` | 67,410.00 USD | 103.35 USD | 0.00 USD | `+23.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7665` | 67,540.00 USD | 127.48 USD | 0.00 USD | `+23.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7675` | 67,640.00 USD | 101.61 USD | 0.00 USD | `+23.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7695` | 67,830.00 USD | 186.97 USD | 0.00 USD | `+24.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7705` | 67,940.00 USD | 109.43 USD | 0.00 USD | `+24.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7775` | 68,110.00 USD | 166.70 USD | 0.00 USD | `+25.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7815` | 69,240.00 USD | 1,140.00 USD | 0.00 USD | `+26.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7865` | 75,560.00 USD | 6,310.00 USD | 0.00 USD | `+26.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8125` | 87,630.00 USD | 12,070.00 USD | 0.00 USD | `+31.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8265` | 89,280.00 USD | 1,650.00 USD | 0.00 USD | `+33.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8335` | 90,210.00 USD | 929.08 USD | 0.00 USD | `+34.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8475` | 130,800.00 USD | 40,590.00 USD | 0.00 USD | `+36.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8505` | 147,540.00 USD | 16,740.00 USD | 0.00 USD | `+37.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8515` | 160,260.00 USD | 12,720.00 USD | 0.00 USD | `+37.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8525` | 172,040.00 USD | 11,780.00 USD | 0.00 USD | `+37.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8725` | 172,200.00 USD | 159.86 USD | 0.00 USD | `+40.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 172,900.00 USD | 702.20 USD | 0.00 USD | `+45.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 173,100.00 USD | 193.62 USD | 0.00 USD | `+46.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 173,520.00 USD | 424.63 USD | 0.00 USD | `+51.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 176,310.00 USD | 2,790.00 USD | 0.00 USD | `+51.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 176,650.00 USD | 340.54 USD | 0.00 USD | `+53.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 176,760.00 USD | 108.83 USD | 0.00 USD | `+55.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 176,910.00 USD | 145.72 USD | 0.00 USD | `+56.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 178,940.00 USD | 2,030.00 USD | 0.00 USD | `+59.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 179,080.00 USD | 136.10 USD | 0.00 USD | `+61.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 179,630.00 USD | 550.48 USD | 0.00 USD | `+61.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 179,940.00 USD | 314.99 USD | 0.00 USD | `+65.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 180,540.00 USD | 602.17 USD | 0.00 USD | `+69.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 180,900.00 USD | 360.61 USD | 0.00 USD | `+70.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 181,850.00 USD | 942.77 USD | 0.00 USD | `+74.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 182,240.00 USD | 397.19 USD | 0.00 USD | `+77.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 182,770.00 USD | 525.37 USD | 0.00 USD | `+98.24%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.5260` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 5,850.00 USD | 0.00 USD | 3,050.00 USD |
| `7D` | `0.5280` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 5,050.00 USD | 0.00 USD | 2,560.00 USD |
| `7D` | `0.5300` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 5,120.00 USD | 0.00 USD | 9,070.00 USD |
| `7D` | `0.5320` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 8,680.00 USD | 0.00 USD | 3,480.00 USD |
| `7D` | `0.5340` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD |
| `7D` | `0.5360` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 2,440.00 USD | 3,040.00 USD | 44.79 USD |
| `7D` | `0.5380` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 1,550.00 USD | 2,920.00 USD |
| `7D` | `0.5400` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 0.00 USD | 2,920.00 USD | 57.67 USD |
| `7D` | `0.5420` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 16,260.00 USD | 1,290.00 USD | 2,870.00 USD |
| `7D` | `0.5440` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 1,150.00 USD | 13,640.00 USD |
| `7D` | `0.5460` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 2,250.00 USD | 3,030.00 USD | 5,220.00 USD |
| `7D` | `0.5480` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 2,000.00 USD | 795.70 USD | 4,490.00 USD |
| `1D` | `0.5500` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 1,410.00 USD | 0.00 USD | 6,700.00 USD |
| `7D` | `0.5500` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 5,990.00 USD | 1,440.00 USD | 6,730.00 USD |
| `1D` | `0.5510` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 1,340.00 USD | 0.00 USD | 1,900.00 USD |
| `1D` | `0.5520` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 0.00 USD | 1,050.00 USD | 38.17 USD |
| `7D` | `0.5520` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 4,110.00 USD | 1,920.00 USD | 1,890.00 USD |
| `1D` | `0.5530` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 1,260.00 USD | 1,410.00 USD | 5.87 USD |
| `1D` | `0.5540` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 5,390.00 USD | 5,750.00 USD | 4,180.00 USD |
| `7D` | `0.5540` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 12,840.00 USD | 7,260.00 USD | 18,570.00 USD |
| `1D` | `0.5550` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 2,940.00 USD | 0.00 USD | 1,600.00 USD |
| `1D` | `0.5560` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 1,680.00 USD | 686.25 USD | 0.00 USD |
| `7D` | `0.5560` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 13,490.00 USD | 1,920.00 USD | 10,460.00 USD |
| `1D` | `0.5570` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 1,690.00 USD | 2,460.00 USD | 4,340.00 USD |
| `1D` | `0.5580` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 0.00 USD | 2,820.00 USD | 2,540.00 USD |
| `7D` | `0.5580` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 6,000.00 USD | 6,820.00 USD | 18,280.00 USD |
| `1D` | `0.5590` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 1,870.00 USD | 1,370.00 USD |
| `1D` | `0.5600` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 1,690.00 USD | 2,550.00 USD |
| `7D` | `0.5600` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 4,070.00 USD | 8,160.00 USD | 2,490.00 USD |
| `1D` | `0.5610` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 858.33 USD |
| `1D` | `0.5620` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 0.00 USD | 776.64 USD | 2,230.00 USD |
| `7D` | `0.5620` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 19,480.00 USD | 7,420.00 USD | 11,640.00 USD |
| `1D` | `0.5630` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 1,180.00 USD | 1,560.00 USD | 5,680.00 USD |
| `1D` | `0.5640` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 4,020.00 USD | 2,420.00 USD | 10,730.00 USD |
| `7D` | `0.5640` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 2,950.00 USD | 741.21 USD | 75.02 USD |
| `1D` | `0.5660` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 3,400.00 USD |
| `7D` | `0.5660` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 11,490.00 USD | 2,990.00 USD | 4,420.00 USD |
| `7D` | `0.5680` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 5,100.00 USD | 0.00 USD | 2,890.00 USD |
| `1D` | `0.5690` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 5,100.00 USD |
| `1D` | `0.5700` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 0.00 USD | 1,760.00 USD | 209.30 USD |
| `7D` | `0.5700` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD |
| `1D` | `0.5710` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 0.00 USD | 2,350.00 USD | 77.72 USD |
| `1D` | `0.5720` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 0.00 USD | 832.92 USD | 0.00 USD |
| `7D` | `0.5720` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 0.00 USD | 4,370.00 USD | 12,050.00 USD |
| `1D` | `0.5730` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD |
| `1D` | `0.5740` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 0.00 USD | 839.21 USD | 3,930.00 USD |
| `7D` | `0.5740` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 21,620.00 USD | 1,100.00 USD | 1,700.00 USD |
| `1D` | `0.5750` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 4,330.00 USD | 840.09 USD | 20,070.00 USD |
| `1D` | `0.5760` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 15,020.00 USD | 2,220.00 USD | 2,100.00 USD |
| `7D` | `0.5760` | 990,890.00 USD | 0.00 USD | 990,890.00 USD | 2,150.00 USD | 7,300.00 USD | 179.10 USD |
| `1D` | `0.5770` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 16,730.00 USD | 3,970.00 USD | 0.00 USD |
| `1D` | `0.5780` | 985,830.00 USD | 0.00 USD | 985,830.00 USD | 3,070.00 USD | 1,330.00 USD | 10,920.00 USD |
| `7D` | `0.5780` | 981,260.00 USD | 0.00 USD | 981,260.00 USD | 40,930.00 USD | 0.00 USD | 1,520.00 USD |
| `1D` | `0.5790` | 970,520.00 USD | 0.00 USD | 970,520.00 USD | 11,420.00 USD | 2,690.00 USD | 7,750.00 USD |
| `1D` | `0.5800` | 948,660.00 USD | 0.00 USD | 948,660.00 USD | 3,310.00 USD | 2,750.00 USD | 1,860.00 USD |
| `7D` | `0.5800` | 938,810.00 USD | 0.00 USD | 938,810.00 USD | 1,610.00 USD | 3,900.00 USD | 27,760.00 USD |
| `1D` | `0.5810` | 940,740.00 USD | 0.00 USD | 940,740.00 USD | 0.00 USD | 3,190.00 USD | 16,880.00 USD |
| `1D` | `0.5820` | 920,670.00 USD | 0.00 USD | 920,670.00 USD | 2,580.00 USD | 4,510.00 USD | 4,220.00 USD |
| `7D` | `0.5820` | 905,540.00 USD | 0.00 USD | 905,540.00 USD | 0.00 USD | 0.00 USD | 6,860.00 USD |
| `1D` | `0.5830` | 909,360.00 USD | 0.00 USD | 909,360.00 USD | 4,910.00 USD | 819.33 USD | 0.00 USD |
| `1D` | `0.5840` | 903,630.00 USD | 0.00 USD | 903,630.00 USD | 0.00 USD | 2,190.00 USD | 4,280.00 USD |
| `7D` | `0.5840` | 898,690.00 USD | 0.00 USD | 898,690.00 USD | 0.00 USD | 0.00 USD | 21,300.00 USD |
| `1D` | `0.5850` | 897,160.00 USD | 0.00 USD | 897,160.00 USD | 2,950.00 USD | 0.00 USD | 30,770.00 USD |
| `1D` | `0.5860` | 863,440.00 USD | 0.00 USD | 863,440.00 USD | 2,810.00 USD | 3,110.00 USD | 7,880.00 USD |
| `7D` | `0.5860` | 877,390.00 USD | 0.00 USD | 877,390.00 USD | 0.00 USD | 0.00 USD | 138.04 USD |
| `1D` | `0.5870` | 849,640.00 USD | 0.00 USD | 849,640.00 USD | 15,080.00 USD | 2,310.00 USD | 52.44 USD |
| `1D` | `0.5880` | 832,200.00 USD | 0.00 USD | 832,200.00 USD | 34,650.00 USD | 10,250.00 USD | 7,810.00 USD |
| `7D` | `0.5880` | 877,250.00 USD | 0.00 USD | 877,250.00 USD | 3,110.00 USD | 16,010.00 USD | 0.00 USD |
| `1D` | `0.5890` | 779,490.00 USD | 0.00 USD | 779,490.00 USD | 38,270.00 USD | 11,450.00 USD | 15.35 USD |
| `1D` | `0.5900` | 729,750.00 USD | 0.00 USD | 729,750.00 USD | 29,060.00 USD | 13,050.00 USD | 10,160.00 USD |
| `7D` | `0.5900` | 858,140.00 USD | 0.00 USD | 858,140.00 USD | 104,240.00 USD | 1,560.00 USD | 15.37 USD |
| `1D` | `0.5910` | 677,480.00 USD | 0.00 USD | 677,480.00 USD | 26,100.00 USD | 13,220.00 USD | 18,000.00 USD |
| `1D` | `0.5920` | 620,160.00 USD | 0.00 USD | 620,160.00 USD | 25,960.00 USD | 6,190.00 USD | 7,280.00 USD |
| `7D` | `0.5920` | 752,320.00 USD | 0.00 USD | 752,320.00 USD | 11,690.00 USD | 19,960.00 USD | 75,590.00 USD |
| `1D` | `0.5930` | 580,720.00 USD | 0.00 USD | 580,720.00 USD | 6,060.00 USD | 6,380.00 USD | 13,000.00 USD |
| `1D` | `0.5940` | 555,280.00 USD | 0.00 USD | 555,280.00 USD | 15,260.00 USD | 1,300.00 USD | 8,370.00 USD |
| `7D` | `0.5940` | 645,080.00 USD | 0.00 USD | 645,080.00 USD | 10,090.00 USD | 0.00 USD | 293.47 USD |
| `1D` | `0.5950` | 530,350.00 USD | 0.00 USD | 530,350.00 USD | 26,720.00 USD | 3,220.00 USD | 0.00 USD |
| `1D` | `0.5960` | 500,410.00 USD | 0.00 USD | 500,410.00 USD | 7,830.00 USD | 1,860.00 USD | 8,580.00 USD |
| `7D` | `0.5960` | 634,690.00 USD | 0.00 USD | 634,690.00 USD | 18,180.00 USD | 18,410.00 USD | 0.00 USD |
| `1D` | `0.5970` | 482,150.00 USD | 0.00 USD | 482,150.00 USD | 13,040.00 USD | 0.00 USD | 1,990.00 USD |
| `1D` | `0.5980` | 467,110.00 USD | 0.00 USD | 467,110.00 USD | 10,410.00 USD | 2,390.00 USD | 80.78 USD |
| `7D` | `0.5980` | 598,100.00 USD | 0.00 USD | 598,100.00 USD | 20,380.00 USD | 0.00 USD | 46.83 USD |
| `1D` | `0.5990` | 454,230.00 USD | 0.00 USD | 454,230.00 USD | 0.00 USD | 836.21 USD | 1,100.00 USD |
| `1D` | `0.6000` | 452,300.00 USD | 0.00 USD | 452,300.00 USD | 0.00 USD | 2,480.00 USD | 5,010.00 USD |
| `7D` | `0.6000` | 577,670.00 USD | 0.00 USD | 577,670.00 USD | 3,320.00 USD | 0.00 USD | 4,700.00 USD |
| `1D` | `0.6010` | 444,810.00 USD | 0.00 USD | 444,810.00 USD | 2,960.00 USD | 6,370.00 USD | 5,030.00 USD |
| `1D` | `0.6020` | 430,450.00 USD | 0.00 USD | 430,450.00 USD | 2,680.00 USD | 5,050.00 USD | 1,720.00 USD |
| `7D` | `0.6020` | 569,640.00 USD | 0.00 USD | 569,640.00 USD | 0.00 USD | 8,040.00 USD | 0.00 USD |
| `1D` | `0.6030` | 421,000.00 USD | 0.00 USD | 421,000.00 USD | 34,080.00 USD | 14,050.00 USD | 3,650.00 USD |
| `1D` | `0.6040` | 369,210.00 USD | 0.00 USD | 369,210.00 USD | 6,530.00 USD | 9,900.00 USD | 5,030.00 USD |
| `7D` | `0.6040` | 561,600.00 USD | 0.00 USD | 561,600.00 USD | 38,530.00 USD | 18,680.00 USD | 139.74 USD |
| `1D` | `0.6050` | 347,750.00 USD | 0.00 USD | 347,750.00 USD | 20,690.00 USD | 1,370.00 USD | 7,950.00 USD |
| `1D` | `0.6060` | 317,750.00 USD | 0.00 USD | 317,750.00 USD | 8,400.00 USD | 0.00 USD | 50.34 USD |
| `7D` | `0.6060` | 504,250.00 USD | 0.00 USD | 504,250.00 USD | 0.00 USD | 0.00 USD | 20,890.00 USD |
| `1D` | `0.6070` | 309,300.00 USD | 0.00 USD | 309,300.00 USD | 8,430.00 USD | 2,600.00 USD | 0.00 USD |
| `1D` | `0.6080` | 298,270.00 USD | 0.00 USD | 298,270.00 USD | 3,650.00 USD | 3,170.00 USD | 0.00 USD |
| `7D` | `0.6080` | 483,360.00 USD | 0.00 USD | 483,360.00 USD | 2,860.00 USD | 0.00 USD | 30,570.00 USD |
| `1D` | `0.6090` | 291,450.00 USD | 0.00 USD | 291,450.00 USD | 0.00 USD | 1,620.00 USD | 0.00 USD |
| `1D` | `0.6100` | 289,830.00 USD | 0.00 USD | 289,830.00 USD | 0.00 USD | 0.00 USD | 35,170.00 USD |
| `7D` | `0.6100` | 449,930.00 USD | 0.00 USD | 449,930.00 USD | 21,400.00 USD | 47,430.00 USD | 25,160.00 USD |
| `1D` | `0.6110` | 254,660.00 USD | 0.00 USD | 254,660.00 USD | 12,430.00 USD | 3,380.00 USD | 0.00 USD |
| `1D` | `0.6120` | 238,850.00 USD | 0.00 USD | 238,850.00 USD | 30,040.00 USD | 1,670.00 USD | 2,170.00 USD |
| `7D` | `0.6120` | 355,930.00 USD | 0.00 USD | 355,930.00 USD | 35,760.00 USD | 20,330.00 USD | 18,560.00 USD |
| `1D` | `0.6130` | 204,960.00 USD | 0.00 USD | 204,960.00 USD | 39,390.00 USD | 4,950.00 USD | 28,390.00 USD |
| `1D` | `0.6140` | 132,230.00 USD | 0.00 USD | 132,230.00 USD | 6,130.00 USD | 3,530.00 USD | 19,180.00 USD |
| `7D` | `0.6140` | 281,270.00 USD | 0.00 USD | 281,270.00 USD | 51,900.00 USD | 7,220.00 USD | 4,330.00 USD |
| `1D` | `0.6160` | 103,380.00 USD | 0.00 USD | 103,380.00 USD | 0.00 USD | 0.00 USD | 3,130.00 USD |
| `7D` | `0.6160` | 217,820.00 USD | 0.00 USD | 217,820.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD |
| `1D` | `0.6180` | 100,260.00 USD | 0.00 USD | 100,260.00 USD | 0.00 USD | 1,760.00 USD | 8,360.00 USD |
| `7D` | `0.6180` | 201,230.00 USD | 0.00 USD | 201,230.00 USD | 7,600.00 USD | 0.00 USD | 107.38 USD |
| `1D` | `0.6200` | 90,140.00 USD | 0.00 USD | 90,140.00 USD | 0.00 USD | 0.00 USD | 8,550.00 USD |
| `7D` | `0.6200` | 193,520.00 USD | 0.00 USD | 193,520.00 USD | 21,280.00 USD | 0.00 USD | 29,250.00 USD |
| `1D` | `0.6210` | 81,590.00 USD | 0.00 USD | 81,590.00 USD | 5,900.00 USD | 0.00 USD | 16,860.00 USD |
| `1D` | `0.6220` | 58,820.00 USD | 0.00 USD | 58,820.00 USD | 5,630.00 USD | 2,380.00 USD | 3,990.00 USD |
| `7D` | `0.6220` | 142,990.00 USD | 0.00 USD | 142,990.00 USD | 4,760.00 USD | 22,640.00 USD | 41.73 USD |
| `1D` | `0.6240` | 46,820.00 USD | 0.00 USD | 46,820.00 USD | 21,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6240` | 115,550.00 USD | 0.00 USD | 115,550.00 USD | 0.00 USD | 7,300.00 USD | 0.00 USD |
| `1D` | `0.6250` | 25,110.00 USD | 0.00 USD | 25,110.00 USD | 16,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6260` | 8,370.00 USD | 0.00 USD | 8,370.00 USD | 0.00 USD | 8,370.00 USD | 0.07 USD |
| `7D` | `0.6260` | 108,240.00 USD | 0.00 USD | 108,240.00 USD | 108,240.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6270` | 47,830.00 USD | 47,830.00 USD | 0.00 USD | 47,830.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6270` | 95,660.00 USD | 95,660.00 USD | 0.00 USD | 47,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6270` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6280` | 144,740.00 USD | 144,740.00 USD | 0.00 USD | 9,840.00 USD | 16,420.00 USD | 22,820.00 USD |
| `7D` | `0.6280` | 86,520.00 USD | 86,520.00 USD | 0.00 USD | 38,530.00 USD | 22,580.00 USD | 25,410.00 USD |
| `1D` | `0.6290` | 186,430.00 USD | 186,430.00 USD | 0.00 USD | 20,690.00 USD | 6,580.00 USD | 14,420.00 USD |
| `1D` | `0.6300` | 210,040.00 USD | 210,040.00 USD | 0.00 USD | 10,980.00 USD | 3,430.00 USD | 9,200.00 USD |
| `7D` | `0.6300` | 135,980.00 USD | 135,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 49,460.00 USD |
| `1D` | `0.6310` | 262,010.00 USD | 262,010.00 USD | 0.00 USD | 22,880.00 USD | 7,390.00 USD | 21,710.00 USD |
| `1D` | `0.6320` | 313,180.00 USD | 313,180.00 USD | 0.00 USD | 34,120.00 USD | 6,080.00 USD | 10,970.00 USD |
| `7D` | `0.6320` | 136,210.00 USD | 136,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 233.05 USD |
| `1D` | `0.6330` | 356,890.00 USD | 356,890.00 USD | 0.00 USD | 14,500.00 USD | 10,960.00 USD | 18,250.00 USD |
| `1D` | `0.6340` | 424,110.00 USD | 424,110.00 USD | 0.00 USD | 29,640.00 USD | 3,190.00 USD | 34,390.00 USD |
| `7D` | `0.6340` | 205,330.00 USD | 205,330.00 USD | 0.00 USD | 68,660.00 USD | 0.00 USD | 448.08 USD |
| `1D` | `0.6350` | 471,470.00 USD | 471,470.00 USD | 0.00 USD | 39,480.00 USD | 1,700.00 USD | 6,180.00 USD |
| `1D` | `0.6360` | 590,100.00 USD | 590,100.00 USD | 0.00 USD | 54,130.00 USD | 4,140.00 USD | 60,370.00 USD |
| `7D` | `0.6360` | 296,680.00 USD | 296,680.00 USD | 0.00 USD | 34,320.00 USD | 0.00 USD | 57,040.00 USD |
| `1D` | `0.6370` | 621,870.00 USD | 621,870.00 USD | 0.00 USD | 0.00 USD | 5,010.00 USD | 26,750.00 USD |
| `1D` | `0.6380` | 656,400.00 USD | 656,400.00 USD | 0.00 USD | 0.00 USD | 28,210.00 USD | 6,320.00 USD |
| `7D` | `0.6380` | 335,980.00 USD | 335,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39,290.00 USD |
| `1D` | `0.6390` | 740,160.00 USD | 740,160.00 USD | 0.00 USD | 26,050.00 USD | 7,210.00 USD | 50,500.00 USD |
| `1D` | `0.6400` | 887,910.00 USD | 887,910.00 USD | 0.00 USD | 72,890.00 USD | 39,010.00 USD | 35,860.00 USD |
| `7D` | `0.6400` | 376,440.00 USD | 376,440.00 USD | 0.00 USD | 19,270.00 USD | 7,510.00 USD | 13,690.00 USD |
| `1D` | `0.6410` | 952,670.00 USD | 952,670.00 USD | 0.00 USD | 35,660.00 USD | 14,660.00 USD | 14,450.00 USD |
| `1D` | `0.6420` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 75,040.00 USD | 15,540.00 USD | 23,520.00 USD |
| `7D` | `0.6420` | 512,710.00 USD | 512,710.00 USD | 0.00 USD | 55,350.00 USD | 44,770.00 USD | 36,140.00 USD |
| `1D` | `0.6430` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 36,780.00 USD | 13,280.00 USD | 23,770.00 USD |
| `1D` | `0.6440` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 31,190.00 USD | 18,570.00 USD | 48,460.00 USD |
| `7D` | `0.6440` | 599,880.00 USD | 599,880.00 USD | 0.00 USD | 44,690.00 USD | 24,820.00 USD | 17,660.00 USD |
| `1D` | `0.6450` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 61,360.00 USD | 12,700.00 USD | 35,620.00 USD |
| `1D` | `0.6460` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 42,970.00 USD | 12,100.00 USD | 9,760.00 USD |
| `7D` | `0.6460` | 957,770.00 USD | 957,770.00 USD | 0.00 USD | 172,610.00 USD | 46,630.00 USD | 138,640.00 USD |
| `1D` | `0.6470` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 59,430.00 USD | 17,210.00 USD | 8,800.00 USD |
| `1D` | `0.6480` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 70,780.00 USD | 7,630.00 USD | 132.92 USD |
| `7D` | `0.6480` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 86,440.00 USD | 26,520.00 USD | 33,090.00 USD |
| `1D` | `0.6490` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 63,670.00 USD | 2,070.00 USD | 12,090.00 USD |
| `1D` | `0.6500` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 41,800.00 USD | 8,390.00 USD | 0.00 USD |
| `7D` | `0.6500` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 73,560.00 USD | 0.00 USD | 132,460.00 USD |
| `1D` | `0.6510` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 58,460.00 USD | 0.00 USD | 14,370.00 USD |
| `1D` | `0.6520` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 93,550.00 USD | 10,800.00 USD | 6,030.00 USD |
| `7D` | `0.6520` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 298,050.00 USD | 10,910.00 USD | 105,300.00 USD |
| `1D` | `0.6530` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 11,510.00 USD | 3,910.00 USD | 77.72 USD |
| `1D` | `0.6540` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 24,280.00 USD | 0.00 USD | 10,730.00 USD |
| `7D` | `0.6540` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 15,730.00 USD | 4,440.00 USD | 61,760.00 USD |
| `1D` | `0.6550` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,030.00 USD |
| `1D` | `0.6560` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,000.00 USD |
| `7D` | `0.6560` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 5,380.00 USD | 982.82 USD |
| `1D` | `0.6570` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,400.00 USD |
| `1D` | `0.6580` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 3,310.00 USD | 234.51 USD |
| `7D` | `0.6580` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 28,280.00 USD | 10,120.00 USD |
| `1D` | `0.6590` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 5,890.00 USD | 77.98 USD |
| `1D` | `0.6600` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 6,010.00 USD | 9,280.00 USD | 69.96 USD |
| `7D` | `0.6600` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 18,420.00 USD | 776.62 USD |
| `1D` | `0.6610` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 6,690.00 USD | 835.70 USD | 63.76 USD |
| `1D` | `0.6620` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 530.84 USD | 7,650.00 USD |
| `7D` | `0.6620` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 8,600.00 USD | 0.00 USD | 420.03 USD |
| `1D` | `0.6630` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 2,590.00 USD | 0.00 USD | 2,350.00 USD |
| `1D` | `0.6640` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 11,190.00 USD | 837.01 USD | 62.52 USD |
| `7D` | `0.6640` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 33,660.00 USD | 0.00 USD | 7,490.00 USD |
| `1D` | `0.6650` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 3,160.00 USD | 17,550.00 USD |
| `1D` | `0.6660` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 839.67 USD | 7,630.00 USD |
| `7D` | `0.6660` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 6,770.00 USD | 667.93 USD |
| `1D` | `0.6670` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 18,850.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6680` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 617.06 USD |
| `1D` | `0.6690` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 3,550.00 USD | 5,500.00 USD |
| `1D` | `0.6700` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 8,830.00 USD | 1,920.00 USD | 24,760.00 USD |
| `7D` | `0.6700` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 953.62 USD |
| `1D` | `0.6710` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 41,970.00 USD | 0.00 USD | 6,010.00 USD |
| `1D` | `0.6720` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 1,410.00 USD | 0.00 USD | 85.60 USD |
| `7D` | `0.6720` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 58,470.00 USD | 0.00 USD | 30,220.00 USD |
| `1D` | `0.6730` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 25,660.00 USD | 3,670.00 USD | 5,540.00 USD |
| `1D` | `0.6740` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 64,370.00 USD | 8,170.00 USD | 9,210.00 USD |
| `7D` | `0.6740` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 39,730.00 USD | 0.00 USD | 43.92 USD |
| `1D` | `0.6750` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 28,700.00 USD | 4,630.00 USD | 12,070.00 USD |
| `1D` | `0.6760` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.6760` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 77,970.00 USD | 33,090.00 USD |
| `1D` | `0.6770` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 19,930.00 USD | 8,320.00 USD | 15,020.00 USD |
| `1D` | `0.6780` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 33,610.00 USD | 13,860.00 USD | 12,090.00 USD |
| `7D` | `0.6780` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 63,600.00 USD | 16,810.00 USD | 18,000.00 USD |
| `1D` | `0.6790` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 2,940.00 USD | 18,610.00 USD | 12,520.00 USD |
| `1D` | `0.6800` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 1,680.00 USD | 686.25 USD | 2,450.00 USD |
| `7D` | `0.6800` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 4,380.00 USD |
| `1D` | `0.6810` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 1,690.00 USD | 2,460.00 USD | 11,930.00 USD |
| `1D` | `0.6820` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 22,600.00 USD | 16,590.00 USD | 9,040.00 USD |
| `7D` | `0.6820` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 32,570.00 USD | 53,450.00 USD | 0.00 USD |
| `1D` | `0.6830` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 24,570.00 USD | 17,300.00 USD | 36,820.00 USD |
| `1D` | `0.6840` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 45,780.00 USD | 17,210.00 USD | 13,850.00 USD |
| `7D` | `0.6840` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 57,890.00 USD | 54,300.00 USD | 102,430.00 USD |
| `1D` | `0.6850` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 39,200.00 USD | 5,780.00 USD | 24,180.00 USD |
| `1D` | `0.6860` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 40,250.00 USD | 4,380.00 USD | 14,820.00 USD |
| `7D` | `0.6860` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 49,930.00 USD | 14,540.00 USD | 10,550.00 USD |
| `1D` | `0.6870` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 63,220.00 USD | 1,160.00 USD | 3,830.00 USD |
| `1D` | `0.6880` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 14,350.00 USD | 11,160.00 USD | 25,330.00 USD |
| `7D` | `0.6880` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 38,030.00 USD | 17,300.00 USD | 125.32 USD |
| `1D` | `0.6890` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 1,180.00 USD | 0.00 USD | 8,430.00 USD |
| `1D` | `0.6900` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 18,600.00 USD | 4,030.00 USD | 21,710.00 USD |
| `7D` | `0.6900` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 15,510.00 USD | 16,810.00 USD |
| `1D` | `0.6910` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 28,860.00 USD | 1,730.00 USD | 32,320.00 USD |
| `1D` | `0.6920` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 16,800.00 USD | 0.00 USD | 13,660.00 USD |
| `7D` | `0.6920` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 69,620.00 USD | 2,090.00 USD | 61,890.00 USD |
| `1D` | `0.6930` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 10,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6940` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 14,220.00 USD | 0.00 USD | 42,460.00 USD |
| `7D` | `0.6960` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 59,960.00 USD | 0.00 USD | 12,530.00 USD |
| `7D` | `0.6980` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 35,980.00 USD | 16,990.00 USD | 0.00 USD |
| `7D` | `0.7000` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 29,740.00 USD | 0.00 USD | 40,190.00 USD |
| `7D` | `0.7020` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 29,810.00 USD | 0.00 USD | 53,170.00 USD |
| `7D` | `0.7040` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 95,520.00 USD | 0.00 USD | 96,320.00 USD |
| `7D` | `0.7060` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 47,840.00 USD | 33,490.00 USD | 177,970.00 USD |
| `7D` | `0.7080` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 24,440.00 USD | 64,870.00 USD | 83,010.00 USD |
| `7D` | `0.7100` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 150,830.00 USD | 63,530.00 USD | 149,060.00 USD |
| `7D` | `0.7120` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 101,040.00 USD | 78,760.00 USD | 227,740.00 USD |
| `7D` | `0.7140` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 202,560.00 USD | 67,260.00 USD | 133,120.00 USD |
| `7D` | `0.7160` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 113,040.00 USD | 65,260.00 USD | 164,620.00 USD |
| `7D` | `0.7180` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 165,860.00 USD | 56,910.00 USD | 66,940.00 USD |
| `7D` | `0.7200` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 93,750.00 USD | 45,160.00 USD | 178,260.00 USD |
| `7D` | `0.7220` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 318,420.00 USD | 67,130.00 USD | 98,390.00 USD |
| `7D` | `0.7240` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 146,110.00 USD | 24,910.00 USD | 129,300.00 USD |
| `7D` | `0.7260` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 106,410.00 USD | 52,120.00 USD | 176,160.00 USD |
| `7D` | `0.7280` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 99,750.00 USD | 40,180.00 USD | 84,220.00 USD |
| `7D` | `0.7300` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 115,310.00 USD | 60,310.00 USD | 109,590.00 USD |
| `7D` | `0.7320` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 189,840.00 USD | 65,640.00 USD | 80,250.00 USD |
| `7D` | `0.7340` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 31,260.00 USD | 8,620.00 USD | 56,450.00 USD |
| `7D` | `0.7360` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 103,600.00 USD | 42,680.00 USD | 34,890.00 USD |
| `7D` | `0.7380` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 73,710.00 USD | 19,000.00 USD | 60,760.00 USD |
| `7D` | `0.7400` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 1,730.00 USD | 4,760.00 USD | 12,330.00 USD |
| `7D` | `0.7420` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 35,810.00 USD | 35,860.00 USD | 31,400.00 USD |
| `7D` | `0.7440` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 74,450.00 USD | 33,900.00 USD | 70,450.00 USD |
| `7D` | `0.7460` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 88,800.00 USD | 17,230.00 USD | 51,670.00 USD |
| `7D` | `0.7480` | 8,950,000.00 USD | 8,950,000.00 USD | 0.00 USD | 60,580.00 USD | 28,900.00 USD | 38,270.00 USD |
| `7D` | `0.7500` | 9,040,000.00 USD | 9,040,000.00 USD | 0.00 USD | 52,320.00 USD | 12,610.00 USD | 25,090.00 USD |
| `7D` | `0.7520` | 9,160,000.00 USD | 9,160,000.00 USD | 0.00 USD | 53,470.00 USD | 13,000.00 USD | 50,460.00 USD |
| `7D` | `0.7530` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 21,290.00 USD | 1,890.00 USD | 14,180.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `88.18M` | Total OI Tokens: `140,571,888.9 APT`
  * 1h OI Change: `+1.21%` | 4h OI Change: `+3.22%` | 24h OI Change: `-9.03%`
  * Exchange Breakdown: Binance=`15.77M` | Bybit=`17.47M` | OKX=`4.15M` | Hyperliquid=`3.47M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-5.53K` | Last 24h: `2.90K` | Last 3d: `7.60K` | Last 7d: `2.85K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0146%` | **USDT OKX** | `-0.0191%` |
| **USDT Bybit** | `-0.0135%` | **USDT KuCoin** | `-0.0230%` |
| **USDT MEXC** | `-0.0146%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0146%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `APT` | `44.14%` | `55.86%` | `0.79` | 1,950,000.00 USD |
| `15M` | `Binance` | `52.45%` | `47.55%` | `1.10` | 526,400.00 USD |
| `15M` | `OKX` | `61%` | `39%` | `1.56` | 450,060.00 USD |
| `15M` | `Bybit` | `54.03%` | `45.97%` | `1.18` | 132,210.00 USD |
| `15M` | `KuCoin` | `47.38%` | `52.62%` | `0.90` | 166,050.00 USD |
| `15M` | `Gate` | `29.17%` | `70.83%` | `0.41` | 37,640.00 USD |
| `15M` | `Bitget` | `82.93%` | `17.07%` | `4.86` | 21,770.00 USD |
| `15M` | `BingX` | `5.4%` | `94.6%` | `0.06` | 306,560.00 USD |
| `15M` | `MEXC` | `58.68%` | `41.32%` | `1.42` | 5,250.00 USD |
| `15M` | `Bitunix` | `56.92%` | `43.08%` | `1.32` | 25,770.00 USD |
| `15M` | `Hyperliquid` | `76.44%` | `23.56%` | `3.24` | 2,490.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.12%` | `53.88%` | `0.86` | 201,720.00 USD |
| `15M` | `Crypto.com` | `100%` | `0%` | `1.00` | 28.39 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 72,990.00 USD |
| `15M` | `HTX` | `91.49%` | `8.51%` | `10.75` | 2,580.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `88.24%` | `11.76%` | `7.50` | 48.45 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 152.08 USD |
| `15M` | `Whale Positions` | `52.45%` | `47.55%` | `1.10` | 526,400.00 USD |
| `15M` | `Global Accounts` | `44.14%` | `55.86%` | `0.79` | 1,950,000.00 USD |
| `1H` | `APT` | `50.70%` | `49.30%` | `1.03` | 11,680,000.00 USD |
| `1H` | `Binance` | `53.61%` | `46.39%` | `1.16` | 3,940,000.00 USD |
| `1H` | `OKX` | `56.44%` | `43.56%` | `1.30` | 2,620,000.00 USD |
| `1H` | `Bybit` | `62.79%` | `37.21%` | `1.69` | 1,020,000.00 USD |
| `1H` | `KuCoin` | `51.5%` | `48.5%` | `1.06` | 621,110.00 USD |
| `1H` | `Gate` | `49.78%` | `50.22%` | `0.99` | 216,980.00 USD |
| `1H` | `Bitget` | `60.56%` | `39.44%` | `1.54` | 144,940.00 USD |
| `1H` | `BingX` | `21.7%` | `78.3%` | `0.28` | 457,970.00 USD |
| `1H` | `MEXC` | `66.52%` | `33.48%` | `1.99` | 176,020.00 USD |
| `1H` | `Bitunix` | `27.68%` | `72.32%` | `0.38` | 290,220.00 USD |
| `1H` | `Hyperliquid` | `84.67%` | `15.33%` | `5.52` | 43,640.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `45.07%` | `54.93%` | `0.82` | 1,710,000.00 USD |
| `1H` | `Crypto.com` | `85.7%` | `14.3%` | `5.99` | 178.80 USD |
| `1H` | `WhiteBIT` | `11.82%` | `88.18%` | `0.13` | 387,290.00 USD |
| `1H` | `HTX` | `16.96%` | `83.04%` | `0.20` | 25,670.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `96.35%` | `3.65%` | `26.40` | 14,070.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `37.72%` | `62.28%` | `0.61` | 1,070.00 USD |
| `1H` | `Whale Positions` | `53.61%` | `46.39%` | `1.16` | 3,940,000.00 USD |
| `1H` | `Global Accounts` | `50.70%` | `49.30%` | `1.03` | 11,680,000.00 USD |
| `4H` | `APT` | `46.49%` | `53.51%` | `0.87` | 77,920,000.00 USD |
| `4H` | `Binance` | `46.53%` | `53.47%` | `0.87` | 26,910,000.00 USD |
| `4H` | `OKX` | `50.59%` | `49.41%` | `1.02` | 18,580,000.00 USD |
| `4H` | `Bybit` | `50.49%` | `49.51%` | `1.02` | 6,140,000.00 USD |
| `4H` | `KuCoin` | `50.05%` | `49.95%` | `1.00` | 2,560,000.00 USD |
| `4H` | `Gate` | `47%` | `53%` | `0.89` | 1,660,000.00 USD |
| `4H` | `Bitget` | `49.53%` | `50.47%` | `0.98` | 2,040,000.00 USD |
| `4H` | `BingX` | `19.16%` | `80.84%` | `0.24` | 3,060,000.00 USD |
| `4H` | `MEXC` | `55.28%` | `44.72%` | `1.24` | 960,840.00 USD |
| `4H` | `Bitunix` | `50.57%` | `49.43%` | `1.02` | 2,680,000.00 USD |
| `4H` | `Hyperliquid` | `35.01%` | `64.99%` | `0.54` | 637,400.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.65%` | `52.35%` | `0.91` | 11,060,000.00 USD |
| `4H` | `Crypto.com` | `80.31%` | `19.69%` | `4.08` | 1,410.00 USD |
| `4H` | `WhiteBIT` | `5.68%` | `94.32%` | `0.06` | 1,420,000.00 USD |
| `4H` | `HTX` | `39.98%` | `60.02%` | `0.67` | 61,130.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `10.44%` | `89.56%` | `0.12` | 26,160.00 USD |
| `4H` | `Aster` | `43.4%` | `56.6%` | `0.77` | 96,630.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.3%` | `47.7%` | `1.10` | 40,440.00 USD |
| `4H` | `Whale Positions` | `46.53%` | `53.47%` | `0.87` | 26,910,000.00 USD |
| `4H` | `Global Accounts` | `46.49%` | `53.51%` | `0.87` | 77,920,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.6083` | `0.6072` | `0.6083` | `0.6096` | `0.6042` | 191,671.81 USD | 128,624.28 USD | 63,047.54 USD | 65,576.74 USD | `+34.21%` | `17B / 3S` |
| `0:00 UTC` | `0.6152` | `0.6139` | `0.6152` | `0.6175` | `0.6090` | 470,291.39 USD | 289,898.53 USD | 180,392.87 USD | 109,505.66 USD | `+23.28%` | `29B / 6S` |
| `5:00 UTC` | `0.6161` | `0.6160` | `0.6161` | `0.6176` | `0.6147` | 319,675.12 USD | 174,523.38 USD | 145,151.74 USD | 29,371.64 USD | `+9.19%` | `4B / 6S` |
| `0:00 UTC` | `0.6151` | `0.6150` | `0.6151` | `0.6187` | `0.6118` | 468,512.46 USD | 237,013.59 USD | 231,498.87 USD | 5,514.73 USD | `+1.18%` | `14B / 9S` |
| `5:00 UTC` | `0.6179` | `0.6169` | `0.6179` | `0.6184` | `0.6149` | 312,659.38 USD | 170,069.09 USD | 142,590.29 USD | 27,478.79 USD | `+8.79%` | `4B / 2S` |
| `0:00 UTC` | `0.6169` | `0.6172` | `0.6169` | `0.6184` | `0.6159` | 332,795.97 USD | 159,318.96 USD | 173,477.01 USD | -14,158.04 USD | `-4.25%` | `4B / 4S` |
| `5:00 UTC` | `0.6199` | `0.6197` | `0.6199` | `0.6222` | `0.6170` | 660,978.35 USD | 238,264.86 USD | 422,713.49 USD | -184,448.63 USD | `-27.91%` | `8B / 10S` |
| `0:00 UTC` | `0.6210` | `0.6225` | `0.6210` | `0.6265` | `0.6192` | 529,221.91 USD | 223,718.81 USD | 305,503.09 USD | -81,784.28 USD | `-15.45%` | `7B / 16S` |
| `5:00 UTC` | `0.6250` | `0.6249` | `0.6250` | `0.6265` | `0.6227` | 233,847.44 USD | 95,835.18 USD | 138,012.26 USD | -42,177.08 USD | `-18.04%` | `7B / 7S` |
| `0:00 UTC` | `0.6256` | `0.6267` | `0.6256` | `0.6282` | `0.6250` | 192,388.38 USD | 67,433.48 USD | 124,954.90 USD | -57,521.42 USD | `-29.90%` | `5B / 11S` |

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
| `5m` | 6,790.00 USD | 1,650.00 USD | **`ACCUMULATION`** |
| `15m` | -33,800.00 USD | -11,510.00 USD | **`DISTRIBUTION`** |
| `30m` | -106,100.00 USD | -108,500.00 USD | **`DISTRIBUTION`** |
| `1h` | -112,550.00 USD | -462,240.00 USD | **`DISTRIBUTION`** |
| `2h` | -86,390.00 USD | -237,930.00 USD | **`DISTRIBUTION`** |
| `4h` | -22,760.00 USD | 268,650.00 USD | **`ACCUMULATION`** |
| `6h` | -523,790.00 USD | -1,140,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,000,000.00 USD | -4,810,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,390,000.00 USD | -6,440,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,330,000.00 USD | -9,050,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,880,000.00 USD | -25,970,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,530,000.00 USD | -106,620,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+6.79K` | 15m=`-33.80K` | 1h=`-112.55K` | 24h=`-1.33M`
* Futures Capital Netflows: 5m=`+1.65K` | 15m=`-11.51K` | 1h=`-462.24K` | 24h=`-9.05M`
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
  * `2026-10-30 11:03:23 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:09:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:10:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
