# 🏛️ SOVEREIGN CANDIDATE DOSSIER: APT
**Canonical Key**: `APT` | **Broker Instrument**: `APTUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 03:16:11 IST` (`2026-10-29 21:46:11 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.6316` | `0.6371` | `0.6316` | `0.6361` | `655,338` | 416,006.86 USD | 68,662.91 USD | `+16.51%` | -6,331,729.29 USD | `+0.46` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.6360` | `0.6411` | `0.6356` | `0.6377` | `660,696` | 421,792.40 USD | 32,292.71 USD | `+7.66%` | -6,299,436.58 USD | `+0.38` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.6377` | `0.6377` | `0.6277` | `0.6286` | `815,294` | 514,510.63 USD | -186,182.59 USD | `-36.19%` | -6,485,619.17 USD | `-0.09` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.6198` | `0.6331` | `0.6164` | `0.6316` | `4,414,654` | 2,767,755.14 USD | 121,847.15 USD | `+4.40%` | -6,473,329.24 USD | `+0.64` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.6317` | `0.6400` | `0.6245` | `0.6315` | `3,588,784` | 2,269,133.84 USD | 72,937.03 USD | `+3.21%` | -6,400,392.20 USD | `+0.51` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.6316` | `0.6411` | `0.6277` | `0.6285` | `2,131,906` | 1,352,673.01 USD | -85,134.73 USD | `-6.29%` | -6,485,526.93 USD | `+0.23` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.6700` | `0.6740` | `0.6665` | `0.6721` | `2,120,904` | 1,422,528.11 USD | 209,427.40 USD | `+14.72%` | -3,354,697.35 USD | `+1.29` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.6721` | `0.6728` | `0.6003` | `0.6199` | `31,822,286` | 20,211,912.01 USD | -3,344,538.21 USD | `-16.55%` | -6,699,235.56 USD | `-4.04` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.6198` | `0.6411` | `0.6164` | `0.6285` | `10,135,344` | 6,389,561.99 USD | 109,649.46 USD | `+1.72%` | -6,589,586.10 USD | `+0.53` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -1,678,888.13 USD | `+0.66` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -3,147,816.26 USD | `-1.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6003` | `0.6285` | `41,957,630` | 26,601,474.00 USD | -3,234,888.75 USD | `-12.16%` | -6,382,705.01 USD | `-1.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6611` | `0.6759` | `0.6485` | `0.6561` | `10,656,422` | 7,044,804.33 USD | -366,898.68 USD | `-5.21%` | -1,470,659.97 USD | `+1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6561` | `0.6774` | `0.6549` | `0.6712` | `7,448,343` | 4,965,296.85 USD | -60,141.40 USD | `-1.21%` | -1,530,801.38 USD | `+1.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -1,678,888.13 USD | `+0.66` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -3,147,816.26 USD | `-1.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6003` | `0.6285` | `41,957,630` | 26,601,474.00 USD | -3,234,888.75 USD | `-12.16%` | -6,382,705.01 USD | `-1.98` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:15:37 IST` |

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
| `Live` | `Long Liquidation` | `0.1395` | 419.65 USD | 268,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 274.34 USD | 268,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 231.16 USD | 267,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1815` | 214.89 USD | 267,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 269.27 USD | 267,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2085` | 1,520.00 USD | 267,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2185` | 2,470.00 USD | 265,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 233.06 USD | 263,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2765` | 35,670.00 USD | 262,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3175` | 1,590.00 USD | 227,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3275` | 9,320.00 USD | 225,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3305` | 543.58 USD | 216,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3545` | 177.25 USD | 215,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3615` | 2,170.00 USD | 215,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3655` | 913.75 USD | 213,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 189.47 USD | 212,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3875` | 271.25 USD | 212,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3905` | 5,210.00 USD | 212,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3925` | 392.50 USD | 206,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3935` | 590.25 USD | 206,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3955` | 2,640.00 USD | 205,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3995` | 271.06 USD | 203,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 570.81 USD | 203,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4135` | 1,600.00 USD | 202,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 630.86 USD | 200,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4255` | 224.96 USD | 200,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4325` | 437.88 USD | 199,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4405` | 4,300.00 USD | 199,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 226.63 USD | 195,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4515` | 27,090.00 USD | 195,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4605` | 286.56 USD | 167,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4615` | 830.07 USD | 167,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4625` | 1,680.00 USD | 166,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4635` | 273.41 USD | 165,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4675` | 4,320.00 USD | 164,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4685` | 468.50 USD | 160,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4695` | 883.30 USD | 160,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4755` | 1,220.00 USD | 159,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4795` | 118.14 USD | 157,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 135.33 USD | 157,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 3,170.00 USD | 157,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4905` | 166.28 USD | 154,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 3,180.00 USD | 154,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 429.90 USD | 151,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 102.82 USD | 150,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 248.05 USD | 150,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5135` | 110.50 USD | 150,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5145` | 288.78 USD | 150,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 9,440.00 USD | 150,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5315` | 11,510.00 USD | 140,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5320` | 1,070,000.00 USD | 1,070,000.00 USD | 11,240.00 USD | 0.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5335` | 284.94 USD | 129,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5340` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5350` | 1,050,000.00 USD | 1,050,000.00 USD | 2,650.00 USD | 1,850.00 USD | 1,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5360` | 1,050,000.00 USD | 1,050,000.00 USD | 2,440.00 USD | 3,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5370` | 1,040,000.00 USD | 1,040,000.00 USD | 4,720.00 USD | 2,450.00 USD | 1,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5380` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 1,550.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5390` | 1,030,000.00 USD | 1,030,000.00 USD | 6,850.00 USD | 1,140.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5410` | 1,020,000.00 USD | 1,020,000.00 USD | 618.50 USD | 0.00 USD | 2,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5420` | 1,040,000.00 USD | 1,040,000.00 USD | 7,660.00 USD | 1,290.00 USD | 2,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5430` | 1,010,000.00 USD | 1,010,000.00 USD | 3,300.00 USD | 0.00 USD | 3,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5440` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 1,150.00 USD | 6,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5445` | 330.14 USD | 128,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5450` | 1,010,000.00 USD | 1,010,000.00 USD | 1,070.00 USD | 298.25 USD | 1,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5460` | 1,020,000.00 USD | 1,020,000.00 USD | 2,250.00 USD | 3,030.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5470` | 1,000,000.00 USD | 1,000,000.00 USD | 3,980.00 USD | 633.67 USD | 499.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5480` | 1,010,000.00 USD | 1,010,000.00 USD | 2,000.00 USD | 795.70 USD | 4,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5485` | 1,390.00 USD | 128,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5490` | 999,560.00 USD | 999,560.00 USD | 0.00 USD | 0.00 USD | 7,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5495` | 630.26 USD | 127,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5500` | 1,010,000.00 USD | 1,010,000.00 USD | 5,990.00 USD | 1,440.00 USD | 6,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5510` | 992,330.00 USD | 992,330.00 USD | 0.00 USD | 0.00 USD | 849.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5520` | 991,540.00 USD | 991,540.00 USD | 4,110.00 USD | 1,920.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5525` | 159.34 USD | 126,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5530` | 991,480.00 USD | 991,480.00 USD | 1,260.00 USD | 0.00 USD | 432.53 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5540` | 983,630.00 USD | 983,630.00 USD | 12,840.00 USD | 4,860.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5545` | 47,450.00 USD | 126,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5550` | 989,790.00 USD | 989,790.00 USD | 1,090.00 USD | 1,520.00 USD | 32.36 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5560` | 947,460.00 USD | 947,460.00 USD | 13,490.00 USD | 1,920.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5570` | 987,150.00 USD | 987,150.00 USD | 0.00 USD | 1,940.00 USD | 553.28 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5575` | 41,140.00 USD | 78,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5580` | 925,800.00 USD | 925,800.00 USD | 6,000.00 USD | 6,820.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5585` | 10,520.00 USD | 37,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5590` | 984,650.00 USD | 984,650.00 USD | 1,100.00 USD | 2,960.00 USD | 2,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5600` | 894,690.00 USD | 894,690.00 USD | 4,070.00 USD | 8,160.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5610` | 978,260.00 USD | 978,260.00 USD | 1,550.00 USD | 2,040.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5615` | 211.33 USD | 27,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5620` | 879,960.00 USD | 879,960.00 USD | 19,480.00 USD | 7,420.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5630` | 972,720.00 USD | 972,720.00 USD | 715.25 USD | 1,020.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5640` | 841,510.00 USD | 841,510.00 USD | 2,950.00 USD | 741.21 USD | 27.20 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5650` | 965,960.00 USD | 965,960.00 USD | 0.00 USD | 2,730.00 USD | 463.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5660` | 837,800.00 USD | 837,800.00 USD | 11,490.00 USD | 2,990.00 USD | 4,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5670` | 962,760.00 USD | 962,760.00 USD | 0.00 USD | 232.89 USD | 2.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5680` | 818,900.00 USD | 818,900.00 USD | 5,100.00 USD | 0.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5685` | 10,360.00 USD | 26,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5700` | 810,910.00 USD | 810,910.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5705` | 1,710.00 USD | 16,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5710` | 962,530.00 USD | 962,530.00 USD | 0.00 USD | 2,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5715` | 289.08 USD | 14,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5720` | 808,330.00 USD | 808,330.00 USD | 0.00 USD | 4,370.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5725` | 4,880.00 USD | 14,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 767.96 USD | 9,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5740` | 802,600.00 USD | 802,600.00 USD | 8,160.00 USD | 1,100.00 USD | 1,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5760` | 791,720.00 USD | 791,720.00 USD | 2,150.00 USD | 0.00 USD | 19.23 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5770` | 960,170.00 USD | 960,170.00 USD | 0.00 USD | 0.00 USD | 34.98 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5780` | 789,550.00 USD | 789,550.00 USD | 0.00 USD | 0.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5790` | 960,140.00 USD | 960,140.00 USD | 0.00 USD | 0.00 USD | 59.63 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5800` | 787,980.00 USD | 787,980.00 USD | 1,610.00 USD | 0.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5820` | 783,530.00 USD | 783,530.00 USD | 0.00 USD | 0.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5830` | 960,080.00 USD | 960,080.00 USD | 0.00 USD | 1,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5845` | 210.96 USD | 8,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 1,070.00 USD | 8,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5870` | 959,080.00 USD | 959,080.00 USD | 2,890.00 USD | 1,290.00 USD | 18,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5880` | 777,010.00 USD | 777,010.00 USD | 3,110.00 USD | 1,400.00 USD | 65.70 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5885` | 440.16 USD | 7,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5890` | 936,520.00 USD | 936,520.00 USD | 4,730.00 USD | 1,580.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5895` | 1,690.00 USD | 7,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5900` | 772,430.00 USD | 772,430.00 USD | 3,120.00 USD | 1,560.00 USD | 15.37 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5910` | 926,520.00 USD | 926,520.00 USD | 4,730.00 USD | 3,210.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5920` | 767,740.00 USD | 767,740.00 USD | 11,690.00 USD | 2,820.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5925` | 609.14 USD | 5,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5930` | 914,480.00 USD | 914,480.00 USD | 14,740.00 USD | 4,790.00 USD | 13,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5940` | 747,200.00 USD | 747,200.00 USD | 10,090.00 USD | 0.00 USD | 9,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5950` | 881,410.00 USD | 881,410.00 USD | 25,410.00 USD | 17,240.00 USD | 6,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5955` | 3,850.00 USD | 4,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5960` | 727,330.00 USD | 727,330.00 USD | 18,180.00 USD | 18,410.00 USD | 13,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5970` | 832,410.00 USD | 832,410.00 USD | 12,480.00 USD | 7,520.00 USD | 17,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5980` | 677,550.00 USD | 677,550.00 USD | 20,380.00 USD | 826.53 USD | 19,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5990` | 794,690.00 USD | 794,690.00 USD | 18,900.00 USD | 2,880.00 USD | 44,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6000` | 636,420.00 USD | 636,420.00 USD | 3,320.00 USD | 2,140.00 USD | 18,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6005` | 852.06 USD | 1,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6010` | 728,070.00 USD | 728,070.00 USD | 735.24 USD | 461.96 USD | 12,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6020` | 612,150.00 USD | 612,150.00 USD | 23,960.00 USD | 8,040.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6030` | 714,340.00 USD | 714,340.00 USD | 26,000.00 USD | 16,180.00 USD | 27.08 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6040` | 576,090.00 USD | 576,090.00 USD | 8,620.00 USD | 3,100.00 USD | 7,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6050` | 672,140.00 USD | 672,140.00 USD | 6,990.00 USD | 4,070.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6060` | 556,460.00 USD | 556,460.00 USD | 0.00 USD | 0.00 USD | 227.43 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6070` | 640,920.00 USD | 640,920.00 USD | 16,200.00 USD | 15,620.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6075` | 196.03 USD | 196.03 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.6080` | 556,230.00 USD | 556,230.00 USD | 2,860.00 USD | 0.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6090` | 601,130.00 USD | 601,130.00 USD | 9,390.00 USD | 29,040.00 USD | 14,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6100` | 544,000.00 USD | 544,000.00 USD | 21,400.00 USD | 47,430.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6110` | 548,460.00 USD | 548,460.00 USD | 5,380.00 USD | 11,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6120` | 449,860.00 USD | 449,860.00 USD | 22,270.00 USD | 5,720.00 USD | 18,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6130` | 531,210.00 USD | 531,210.00 USD | 13,330.00 USD | 596.50 USD | 22,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6140` | 403,360.00 USD | 403,360.00 USD | 51,550.00 USD | 8,040.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6150` | 494,510.00 USD | 494,510.00 USD | 36,090.00 USD | 18,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6160` | 332,990.00 USD | 332,990.00 USD | 12,920.00 USD | 7,460.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6170` | 440,350.00 USD | 440,350.00 USD | 0.00 USD | 0.00 USD | 13,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6180` | 306,000.00 USD | 306,000.00 USD | 20,870.00 USD | 2,610.00 USD | 228.92 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6190` | 426,440.00 USD | 426,440.00 USD | 0.00 USD | 0.00 USD | 15,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6200` | 282,290.00 USD | 282,290.00 USD | 23,430.00 USD | 0.00 USD | 18,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6210` | 410,490.00 USD | 410,490.00 USD | 1,990.00 USD | 18,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6220` | 240,190.00 USD | 240,190.00 USD | 4,760.00 USD | 22,640.00 USD | 224.68 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6230` | 390,100.00 USD | 390,100.00 USD | 2,520.00 USD | 6,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6240` | 212,560.00 USD | 212,560.00 USD | 0.00 USD | 0.00 USD | 171.81 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6250` | 380,800.00 USD | 380,800.00 USD | 25,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6260` | 212,390.00 USD | 212,390.00 USD | 40,330.00 USD | 0.00 USD | 595.48 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6280` | 171,470.00 USD | 171,470.00 USD | 0.00 USD | 0.00 USD | 463.59 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6300` | 171,000.00 USD | 171,000.00 USD | 0.00 USD | 0.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6310` | 355,200.00 USD | 355,200.00 USD | 25,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6320` | 160,710.00 USD | 160,710.00 USD | 0.00 USD | 0.00 USD | 369.35 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6330` | 329,890.00 USD | 329,890.00 USD | 50,610.00 USD | 0.00 USD | 33,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6335` | 203.53 USD | 203.53 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.6340` | 160,340.00 USD | 160,340.00 USD | 68,660.00 USD | 0.00 USD | 381.22 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6350` | 245,920.00 USD | 245,920.00 USD | 73,350.00 USD | 0.00 USD | 40,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6360` | 91,300.00 USD | 91,300.00 USD | 34,320.00 USD | 0.00 USD | 56,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6370` | 132,030.00 USD | 132,030.00 USD | 50,620.00 USD | 6,240.00 USD | 75,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6380` | 39,090.00 USD | 39,090.00 USD | 0.00 USD | 0.00 USD | 39,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6380` | 78,170.00 USD | 78,170.00 USD | 0.00 USD | 0.00 USD | 39,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6390` | 81,860.00 USD | 81,860.00 USD | 18,790.00 USD | 10,860.00 USD | 52,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6400` | 98,690.00 USD | 98,690.00 USD | 0.00 USD | 7,510.00 USD | 13,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6410` | 203,560.00 USD | 203,560.00 USD | 58,000.00 USD | 29,530.00 USD | 34,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6420` | 197,130.00 USD | 197,130.00 USD | 55,350.00 USD | 26,560.00 USD | 16,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6430` | 359,390.00 USD | 359,390.00 USD | 79,540.00 USD | 29,430.00 USD | 46,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6440` | 284,520.00 USD | 284,520.00 USD | 44,690.00 USD | 24,820.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6450` | 581,360.00 USD | 581,360.00 USD | 110,010.00 USD | 31,650.00 USD | 80,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6460` | 642,050.00 USD | 642,050.00 USD | 172,610.00 USD | 46,630.00 USD | 138,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6470` | 737,710.00 USD | 737,710.00 USD | 126,580.00 USD | 22,630.00 USD | 7,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6480` | 788,010.00 USD | 788,010.00 USD | 86,440.00 USD | 26,520.00 USD | 33,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6490` | 917,860.00 USD | 917,860.00 USD | 173,130.00 USD | 6,780.00 USD | 234.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6500` | 993,970.00 USD | 993,970.00 USD | 73,560.00 USD | 0.00 USD | 132,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6510` | 1,050,000.00 USD | 1,050,000.00 USD | 120,420.00 USD | 0.00 USD | 11,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6520` | 1,380,000.00 USD | 1,380,000.00 USD | 271,060.00 USD | 10,910.00 USD | 104,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6530` | 1,150,000.00 USD | 1,150,000.00 USD | 89,280.00 USD | 9,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6540` | 1,460,000.00 USD | 1,460,000.00 USD | 15,730.00 USD | 0.00 USD | 61,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6550` | 1,180,000.00 USD | 1,180,000.00 USD | 11,450.00 USD | 0.00 USD | 17,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6555` | 171.17 USD | 374.70 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.6560` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 5,380.00 USD | 847.61 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6565` | 2,330.00 USD | 2,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6570` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6580` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 28,280.00 USD | 9,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6590` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 9,200.00 USD | 98.76 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6600` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 15,500.00 USD | 580.13 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6610` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 8,400.00 USD | 199.40 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6620` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 128.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6630` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6640` | 1,540,000.00 USD | 1,540,000.00 USD | 20,160.00 USD | 0.00 USD | 534.34 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6650` | 1,240,000.00 USD | 1,240,000.00 USD | 11,190.00 USD | 3,160.00 USD | 17,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6660` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 6,770.00 USD | 436.87 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6670` | 1,270,000.00 USD | 1,270,000.00 USD | 18,850.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6680` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 308.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6690` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 3,550.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6700` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 820.19 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6710` | 1,360,000.00 USD | 1,360,000.00 USD | 50,800.00 USD | 1,920.00 USD | 30,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6720` | 1,640,000.00 USD | 1,640,000.00 USD | 58,470.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6730` | 1,390,000.00 USD | 1,390,000.00 USD | 24,320.00 USD | 3,670.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6740` | 1,680,000.00 USD | 1,680,000.00 USD | 39,730.00 USD | 0.00 USD | 99.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6750` | 1,520,000.00 USD | 1,520,000.00 USD | 93,070.00 USD | 13,090.00 USD | 21,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6760` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 77,970.00 USD | 33,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6770` | 1,570,000.00 USD | 1,570,000.00 USD | 26,380.00 USD | 11,960.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6780` | 1,880,000.00 USD | 1,880,000.00 USD | 63,600.00 USD | 14,400.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6790` | 1,660,000.00 USD | 1,660,000.00 USD | 33,610.00 USD | 31,290.00 USD | 23,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6800` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 16,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6810` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 1,940.00 USD | 10,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6820` | 1,990,000.00 USD | 1,990,000.00 USD | 32,570.00 USD | 53,450.00 USD | 145.79 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6830` | 1,800,000.00 USD | 1,800,000.00 USD | 47,170.00 USD | 42,080.00 USD | 44,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6840` | 2,200,000.00 USD | 2,200,000.00 USD | 57,890.00 USD | 54,300.00 USD | 102,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6850` | 1,960,000.00 USD | 1,960,000.00 USD | 96,870.00 USD | 31,640.00 USD | 21,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6860` | 2,280,000.00 USD | 2,280,000.00 USD | 49,930.00 USD | 14,540.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6870` | 2,080,000.00 USD | 2,080,000.00 USD | 103,470.00 USD | 5,540.00 USD | 16,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6880` | 2,330,000.00 USD | 2,330,000.00 USD | 38,030.00 USD | 17,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6890` | 2,140,000.00 USD | 2,140,000.00 USD | 14,350.00 USD | 9,600.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6900` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 15,510.00 USD | 16,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6910` | 2,250,000.00 USD | 2,250,000.00 USD | 43,430.00 USD | 5,760.00 USD | 60,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6920` | 2,500,000.00 USD | 2,500,000.00 USD | 69,620.00 USD | 2,090.00 USD | 62,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6930` | 2,290,000.00 USD | 2,290,000.00 USD | 26,830.00 USD | 0.00 USD | 13,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6940` | 2,550,000.00 USD | 2,550,000.00 USD | 14,220.00 USD | 0.00 USD | 42,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6950` | 2,350,000.00 USD | 2,350,000.00 USD | 33,700.00 USD | 8,880.00 USD | 13,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6960` | 2,630,000.00 USD | 2,630,000.00 USD | 59,960.00 USD | 0.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6970` | 2,450,000.00 USD | 2,450,000.00 USD | 91,820.00 USD | 10,780.00 USD | 34.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6980` | 2,680,000.00 USD | 2,680,000.00 USD | 35,980.00 USD | 16,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6990` | 2,480,000.00 USD | 2,480,000.00 USD | 14,320.00 USD | 8,940.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7000` | 2,750,000.00 USD | 2,750,000.00 USD | 29,740.00 USD | 0.00 USD | 40,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7010` | 2,540,000.00 USD | 2,540,000.00 USD | 33,760.00 USD | 4,020.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7020` | 2,820,000.00 USD | 2,820,000.00 USD | 16,350.00 USD | 0.00 USD | 53,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7030` | 2,570,000.00 USD | 2,570,000.00 USD | 18,690.00 USD | 0.00 USD | 10,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7040` | 3,010,000.00 USD | 3,010,000.00 USD | 95,520.00 USD | 0.00 USD | 96,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7050` | 2,660,000.00 USD | 2,660,000.00 USD | 59,720.00 USD | 5,290.00 USD | 27,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7060` | 3,270,000.00 USD | 3,270,000.00 USD | 47,840.00 USD | 33,490.00 USD | 178,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7070` | 2,740,000.00 USD | 2,740,000.00 USD | 28,570.00 USD | 25,720.00 USD | 30,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7080` | 3,440,000.00 USD | 3,440,000.00 USD | 24,440.00 USD | 64,870.00 USD | 82,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7090` | 2,800,000.00 USD | 2,800,000.00 USD | 36,000.00 USD | 6,660.00 USD | 13,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7100` | 3,800,000.00 USD | 3,800,000.00 USD | 150,830.00 USD | 63,530.00 USD | 148,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7110` | 2,840,000.00 USD | 2,840,000.00 USD | 11,400.00 USD | 10,040.00 USD | 15,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7120` | 4,210,000.00 USD | 4,210,000.00 USD | 101,040.00 USD | 78,760.00 USD | 228,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7130` | 2,940,000.00 USD | 2,940,000.00 USD | 44,600.00 USD | 8,520.00 USD | 48,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7140` | 4,620,000.00 USD | 4,620,000.00 USD | 202,560.00 USD | 67,260.00 USD | 133,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7150` | 3,020,000.00 USD | 3,020,000.00 USD | 42,280.00 USD | 11,520.00 USD | 30,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7160` | 4,960,000.00 USD | 4,960,000.00 USD | 113,040.00 USD | 65,260.00 USD | 164,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7170` | 3,080,000.00 USD | 3,080,000.00 USD | 22,310.00 USD | 15,690.00 USD | 19,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7180` | 5,250,000.00 USD | 5,250,000.00 USD | 165,860.00 USD | 56,910.00 USD | 66,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7190` | 3,130,000.00 USD | 3,130,000.00 USD | 19,020.00 USD | 8,580.00 USD | 20,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7200` | 5,560,000.00 USD | 5,560,000.00 USD | 93,750.00 USD | 45,160.00 USD | 177,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7210` | 3,170,000.00 USD | 3,170,000.00 USD | 10,550.00 USD | 13,010.00 USD | 16,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7220` | 6,050,000.00 USD | 6,050,000.00 USD | 318,420.00 USD | 67,130.00 USD | 98,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7230` | 3,190,000.00 USD | 3,190,000.00 USD | 7,870.00 USD | 7,380.00 USD | 8,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7240` | 6,350,000.00 USD | 6,350,000.00 USD | 146,110.00 USD | 24,910.00 USD | 128,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7250` | 3,230,000.00 USD | 3,230,000.00 USD | 16,070.00 USD | 6,080.00 USD | 13,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7255` | 853.84 USD | 3,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7260` | 6,680,000.00 USD | 6,680,000.00 USD | 106,410.00 USD | 52,120.00 USD | 175,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7270` | 3,310,000.00 USD | 3,310,000.00 USD | 46,660.00 USD | 5,430.00 USD | 24,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7280` | 6,910,000.00 USD | 6,910,000.00 USD | 99,750.00 USD | 40,180.00 USD | 83,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7290` | 3,370,000.00 USD | 3,370,000.00 USD | 33,620.00 USD | 8,680.00 USD | 25,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7295` | 43,330.00 USD | 46,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7300` | 7,190,000.00 USD | 7,190,000.00 USD | 115,310.00 USD | 60,310.00 USD | 109,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7310` | 3,410,000.00 USD | 3,410,000.00 USD | 10,990.00 USD | 8,670.00 USD | 17,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7320` | 7,530,000.00 USD | 7,530,000.00 USD | 189,840.00 USD | 65,640.00 USD | 80,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7330` | 3,440,000.00 USD | 3,440,000.00 USD | 12,500.00 USD | 3,310.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7340` | 7,630,000.00 USD | 7,630,000.00 USD | 31,260.00 USD | 8,620.00 USD | 63,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7345` | 150.17 USD | 47,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.7350` | 3,440,000.00 USD | 3,440,000.00 USD | 735.24 USD | 461.96 USD | 3,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7360` | 7,810,000.00 USD | 7,810,000.00 USD | 103,600.00 USD | 46,790.00 USD | 35,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7370` | 3,470,000.00 USD | 3,470,000.00 USD | 12,380.00 USD | 8,300.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7380` | 7,970,000.00 USD | 7,970,000.00 USD | 73,710.00 USD | 19,000.00 USD | 60,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7390` | 3,490,000.00 USD | 3,490,000.00 USD | 6,990.00 USD | 4,070.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7400` | 8,010,000.00 USD | 8,010,000.00 USD | 1,730.00 USD | 4,760.00 USD | 37,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7410` | 3,510,000.00 USD | 3,510,000.00 USD | 16,200.00 USD | 1,640.00 USD | 9,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7420` | 8,120,000.00 USD | 8,120,000.00 USD | 35,810.00 USD | 41,830.00 USD | 31,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7430` | 3,520,000.00 USD | 3,520,000.00 USD | 1,240.00 USD | 969.00 USD | 149.25 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7440` | 8,310,000.00 USD | 8,310,000.00 USD | 74,450.00 USD | 39,890.00 USD | 70,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7450` | 3,530,000.00 USD | 3,530,000.00 USD | 8,160.00 USD | 1,410.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7460` | 8,470,000.00 USD | 8,470,000.00 USD | 88,800.00 USD | 28,800.00 USD | 51,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7470` | 3,540,000.00 USD | 3,540,000.00 USD | 5,380.00 USD | 0.00 USD | 6,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7480` | 8,600,000.00 USD | 8,600,000.00 USD | 60,580.00 USD | 28,900.00 USD | 38,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7490` | 3,550,000.00 USD | 3,550,000.00 USD | 2,140.00 USD | 596.50 USD | 2,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7500` | 3,550,000.00 USD | 3,550,000.00 USD | 6,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7500` | 8,690,000.00 USD | 8,690,000.00 USD | 52,320.00 USD | 12,610.00 USD | 25,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7520` | 8,810,000.00 USD | 8,810,000.00 USD | 53,470.00 USD | 13,000.00 USD | 50,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7540` | 8,870,000.00 USD | 8,870,000.00 USD | 30,340.00 USD | 1,890.00 USD | 25,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7560` | 8,920,000.00 USD | 8,920,000.00 USD | 26,000.00 USD | 7,570.00 USD | 22,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7580` | 9,040,000.00 USD | 9,040,000.00 USD | 55,420.00 USD | 11,790.00 USD | 45,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7600` | 9,180,000.00 USD | 9,180,000.00 USD | 57,020.00 USD | 4,320.00 USD | 80,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7620` | 9,280,000.00 USD | 9,280,000.00 USD | 54,140.00 USD | 24,170.00 USD | 21,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7640` | 9,380,000.00 USD | 9,380,000.00 USD | 50,390.00 USD | 13,520.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7660` | 9,550,000.00 USD | 9,550,000.00 USD | 56,130.00 USD | 18,130.00 USD | 91,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7680` | 9,690,000.00 USD | 9,690,000.00 USD | 66,570.00 USD | 32,520.00 USD | 41,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7700` | 9,750,000.00 USD | 9,750,000.00 USD | 10,860.00 USD | 12,600.00 USD | 41,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7720` | 9,870,000.00 USD | 9,870,000.00 USD | 58,380.00 USD | 32,920.00 USD | 25,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7725` | 165.62 USD | 47,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7740` | 9,980,000.00 USD | 9,980,000.00 USD | 51,600.00 USD | 25,250.00 USD | 35,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7760` | 10,040,000.00 USD | 10,040,000.00 USD | 38,170.00 USD | 2,980.00 USD | 12,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7765` | 330.78 USD | 47,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7780` | 10,160,000.00 USD | 10,160,000.00 USD | 68,800.00 USD | 20,860.00 USD | 32,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7800` | 10,320,000.00 USD | 10,320,000.00 USD | 60,490.00 USD | 21,940.00 USD | 80,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7820` | 10,440,000.00 USD | 10,440,000.00 USD | 90,020.00 USD | 17,850.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7840` | 10,540,000.00 USD | 10,540,000.00 USD | 95,370.00 USD | 7,150.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7860` | 10,650,000.00 USD | 10,650,000.00 USD | 32,690.00 USD | 9,290.00 USD | 63,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7880` | 10,710,000.00 USD | 10,710,000.00 USD | 11,900.00 USD | 22,650.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7900` | 10,810,000.00 USD | 10,810,000.00 USD | 59,120.00 USD | 16,710.00 USD | 17,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7910` | 10,840,000.00 USD | 10,840,000.00 USD | 30,620.00 USD | 5,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8005` | 19,120.00 USD | 66,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8665` | 378.95 USD | 67,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8725` | 12,500.00 USD | 79,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8825` | 377.09 USD | 79,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9145` | 26,070.00 USD | 105,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9825` | 17,340.00 USD | 123,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9935` | 166.01 USD | 123,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 479.74 USD | 123,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.12` | 2,800.00 USD | 126,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.14` | 86,710.00 USD | 213,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1395` | 268,570.00 USD | 0.00 USD | 419.65 USD | `-77.50%` | `3,008.22` |
| `Live` | `Long` | `0.1475` | 268,150.00 USD | 0.00 USD | 274.34 USD | `-76.21%` | `1,859.93` |
| `Live` | `Long` | `0.1665` | 267,870.00 USD | 0.00 USD | 231.16 USD | `-73.15%` | `1,388.32` |
| `Live` | `Long` | `0.1815` | 267,640.00 USD | 0.00 USD | 214.89 USD | `-70.73%` | `1,183.99` |
| `Live` | `Long` | `0.1875` | 267,430.00 USD | 0.00 USD | 269.27 USD | `-69.76%` | `1,436.09` |
| `Live` | `Long` | `0.2085` | 267,160.00 USD | 0.00 USD | 1,520.00 USD | `-66.37%` | `7,272.07` |
| `Live` | `Long` | `0.2185` | 265,640.00 USD | 0.00 USD | 2,470.00 USD | `-64.76%` | `11,284.25` |
| `Live` | `Long` | `0.2245` | 263,180.00 USD | 0.00 USD | 233.06 USD | `-63.79%` | `1,038.12` |
| `Live` | `Long` | `0.2765` | 262,940.00 USD | 0.00 USD | 35,670.00 USD | `-55.40%` | `129,000.00` |
| `Live` | `Long` | `0.3175` | 227,280.00 USD | 0.00 USD | 1,590.00 USD | `-48.79%` | `5,000.00` |
| `Live` | `Long` | `0.3275` | 225,690.00 USD | 0.00 USD | 9,320.00 USD | `-47.18%` | `28,446.85` |
| `Live` | `Long` | `0.3305` | 216,370.00 USD | 0.00 USD | 543.58 USD | `-46.69%` | `1,644.73` |
| `Live` | `Long` | `0.3545` | 215,830.00 USD | 0.00 USD | 177.25 USD | `-42.82%` | `500.00` |
| `Live` | `Long` | `0.3615` | 215,650.00 USD | 0.00 USD | 2,170.00 USD | `-41.69%` | `6,000.00` |
| `Live` | `Long` | `0.3655` | 213,480.00 USD | 0.00 USD | 913.75 USD | `-41.05%` | `2,500.00` |
| `Live` | `Long` | `0.3665` | 212,570.00 USD | 0.00 USD | 189.47 USD | `-40.89%` | `516.98` |
| `Live` | `Long` | `0.3875` | 212,380.00 USD | 0.00 USD | 271.25 USD | `-37.50%` | `700.00` |
| `Live` | `Long` | `0.3905` | 212,110.00 USD | 0.00 USD | 5,210.00 USD | `-37.02%` | `13,346.14` |
| `Live` | `Long` | `0.3925` | 206,900.00 USD | 0.00 USD | 392.50 USD | `-36.69%` | `1,000.00` |
| `Live` | `Long` | `0.3935` | 206,500.00 USD | 0.00 USD | 590.25 USD | `-36.53%` | `1,500.00` |
| `Live` | `Long` | `0.3955` | 205,910.00 USD | 0.00 USD | 2,640.00 USD | `-36.21%` | `6,686.27` |
| `Live` | `Long` | `0.3995` | 203,270.00 USD | 0.00 USD | 271.06 USD | `-35.56%` | `678.49` |
| `Live` | `Long` | `0.4035` | 203,000.00 USD | 0.00 USD | 570.81 USD | `-34.92%` | `1,414.65` |
| `Live` | `Long` | `0.4135` | 202,430.00 USD | 0.00 USD | 1,600.00 USD | `-33.31%` | `3,868.97` |
| `Live` | `Long` | `0.4185` | 200,830.00 USD | 0.00 USD | 630.86 USD | `-32.50%` | `1,507.44` |
| `Live` | `Long` | `0.4255` | 200,200.00 USD | 0.00 USD | 224.96 USD | `-31.37%` | `528.69` |
| `Live` | `Long` | `0.4325` | 199,970.00 USD | 0.00 USD | 437.88 USD | `-30.24%` | `1,012.44` |
| `Live` | `Long` | `0.4405` | 199,530.00 USD | 0.00 USD | 4,300.00 USD | `-28.95%` | `9,753.33` |
| `Live` | `Long` | `0.4475` | 195,240.00 USD | 0.00 USD | 226.63 USD | `-27.82%` | `506.43` |
| `Live` | `Long` | `0.4515` | 195,010.00 USD | 0.00 USD | 27,090.00 USD | `-27.18%` | `60,000.00` |
| `Live` | `Long` | `0.4605` | 167,920.00 USD | 0.00 USD | 286.56 USD | `-25.73%` | `622.27` |
| `Live` | `Long` | `0.4615` | 167,630.00 USD | 0.00 USD | 830.07 USD | `-25.56%` | `1,798.64` |
| `Live` | `Long` | `0.4625` | 166,800.00 USD | 0.00 USD | 1,680.00 USD | `-25.40%` | `3,622.78` |
| `Live` | `Long` | `0.4635` | 165,130.00 USD | 0.00 USD | 273.41 USD | `-25.24%` | `589.89` |
| `Live` | `Long` | `0.4675` | 164,850.00 USD | 0.00 USD | 4,320.00 USD | `-24.60%` | `9,243.24` |
| `Live` | `Long` | `0.4685` | 160,530.00 USD | 0.00 USD | 468.50 USD | `-24.44%` | `1,000.00` |
| `Live` | `Long` | `0.4695` | 160,060.00 USD | 0.00 USD | 883.30 USD | `-24.27%` | `1,881.36` |
| `Live` | `Long` | `0.4755` | 159,180.00 USD | 0.00 USD | 1,220.00 USD | `-23.31%` | `2,570.84` |
| `Live` | `Long` | `0.4795` | 157,960.00 USD | 0.00 USD | 118.14 USD | `-22.66%` | `246.38` |
| `Live` | `Long` | `0.4835` | 157,840.00 USD | 0.00 USD | 135.33 USD | `-22.02%` | `279.90` |
| `Live` | `Long` | `0.4865` | 157,710.00 USD | 0.00 USD | 3,170.00 USD | `-21.53%` | `6,508.47` |
| `Live` | `Long` | `0.4905` | 154,540.00 USD | 0.00 USD | 166.28 USD | `-20.89%` | `339.00` |
| `Live` | `Long` | `0.4955` | 154,370.00 USD | 0.00 USD | 3,180.00 USD | `-20.08%` | `6,422.59` |
| `Live` | `Long` | `0.4985` | 151,190.00 USD | 0.00 USD | 429.90 USD | `-19.60%` | `862.38` |
| `Live` | `Long` | `0.5085` | 150,760.00 USD | 0.00 USD | 102.82 USD | `-17.98%` | `202.20` |
| `Live` | `Long` | `0.5125` | 150,660.00 USD | 0.00 USD | 248.05 USD | `-17.34%` | `484.00` |
| `Live` | `Long` | `0.5135` | 150,410.00 USD | 0.00 USD | 110.50 USD | `-17.18%` | `215.19` |
| `Live` | `Long` | `0.5145` | 150,300.00 USD | 0.00 USD | 288.78 USD | `-17.02%` | `561.28` |
| `Live` | `Long` | `0.5175` | 150,010.00 USD | 0.00 USD | 9,440.00 USD | `-16.53%` | `18,249.92` |
| `Live` | `Long` | `0.5315` | 140,570.00 USD | 0.00 USD | 11,510.00 USD | `-14.27%` | `21,664.95` |
| `Live` | `Long` | `0.5335` | 129,050.00 USD | 0.00 USD | 284.94 USD | `-13.95%` | `534.10` |
| `Live` | `Long` | `0.5445` | 128,770.00 USD | 0.00 USD | 330.14 USD | `-12.18%` | `606.32` |
| `Live` | `Long` | `0.5485` | 128,440.00 USD | 0.00 USD | 1,390.00 USD | `-11.53%` | `2,536.99` |
| `Live` | `Long` | `0.5495` | 127,040.00 USD | 0.00 USD | 630.26 USD | `-11.37%` | `1,146.97` |
| `Live` | `Long` | `0.5525` | 126,410.00 USD | 0.00 USD | 159.34 USD | `-10.89%` | `288.40` |
| `Live` | `Long` | `0.5545` | 126,260.00 USD | 0.00 USD | 47,450.00 USD | `-10.56%` | `85,578.81` |
| `Live` | `Long` | `0.5575` | 78,800.00 USD | 0.00 USD | 41,140.00 USD | `-10.08%` | `73,785.90` |
| `Live` | `Long` | `0.5585` | 37,670.00 USD | 0.00 USD | 10,520.00 USD | `-9.92%` | `18,834.52` |
| `Live` | `Long` | `0.5615` | 27,150.00 USD | 0.00 USD | 211.33 USD | `-9.44%` | `376.36` |
| `Live` | `Long` | `0.5685` | 26,940.00 USD | 0.00 USD | 10,360.00 USD | `-8.31%` | `18,230.19` |
| `Live` | `Long` | `0.5705` | 16,570.00 USD | 0.00 USD | 1,710.00 USD | `-7.98%` | `3,002.78` |
| `Live` | `Long` | `0.5715` | 14,860.00 USD | 0.00 USD | 289.08 USD | `-7.82%` | `505.82` |
| `Live` | `Long` | `0.5725` | 14,570.00 USD | 0.00 USD | 4,880.00 USD | `-7.66%` | `8,530.92` |
| `Live` | `Long` | `0.5735` | 9,690.00 USD | 0.00 USD | 767.96 USD | `-7.50%` | `1,339.07` |
| `Live` | `Long` | `0.5845` | 8,920.00 USD | 0.00 USD | 210.96 USD | `-5.73%` | `360.92` |
| `Live` | `Long` | `0.5865` | 8,710.00 USD | 0.00 USD | 1,070.00 USD | `-5.40%` | `1,821.70` |
| `Live` | `Long` | `0.5885` | 7,640.00 USD | 0.00 USD | 440.16 USD | `-5.08%` | `747.93` |
| `Live` | `Long` | `0.5895` | 7,200.00 USD | 0.00 USD | 1,690.00 USD | `-4.92%` | `2,865.95` |
| `Live` | `Long` | `0.5925` | 5,510.00 USD | 0.00 USD | 609.14 USD | `-4.44%` | `1,028.09` |
| `Live` | `Long` | `0.5955` | 4,900.00 USD | 0.00 USD | 3,850.00 USD | `-3.95%` | `6,467.73` |
| `Live` | `Long` | `0.6005` | 1,050.00 USD | 0.00 USD | 852.06 USD | `-3.15%` | `1,418.92` |
| `Live` | `Long` | `0.6075` | 196.03 USD | 0.00 USD | 196.03 USD | `-2.02%` | `322.68` |
| `Live` | `Short` | `0.6335` | 203.53 USD | 203.53 USD | 0.00 USD | `+2.18%` | `321.28` |
| `Live` | `Short` | `0.6555` | 374.70 USD | 171.17 USD | 0.00 USD | `+5.73%` | `261.13` |
| `Live` | `Short` | `0.6565` | 2,700.00 USD | 2,330.00 USD | 0.00 USD | `+5.89%` | `3,542.99` |
| `Live` | `Short` | `0.7255` | 3,550.00 USD | 853.84 USD | 0.00 USD | `+17.02%` | `1,176.90` |
| `Live` | `Short` | `0.7295` | 46,890.00 USD | 43,330.00 USD | 0.00 USD | `+17.66%` | `59,401.36` |
| `Live` | `Short` | `0.7345` | 47,040.00 USD | 150.17 USD | 0.00 USD | `+18.47%` | `204.45` |
| `Live` | `Short` | `0.7725` | 47,200.00 USD | 165.62 USD | 0.00 USD | `+24.60%` | `214.40` |
| `Live` | `Short` | `0.7765` | 47,530.00 USD | 330.78 USD | 0.00 USD | `+25.24%` | `425.99` |
| `Live` | `Short` | `0.8005` | 66,650.00 USD | 19,120.00 USD | 0.00 USD | `+29.11%` | `23,882.80` |
| `Live` | `Short` | `0.8665` | 67,030.00 USD | 378.95 USD | 0.00 USD | `+39.76%` | `437.33` |
| `Live` | `Short` | `0.8725` | 79,530.00 USD | 12,500.00 USD | 0.00 USD | `+40.73%` | `14,330.43` |
| `Live` | `Short` | `0.8825` | 79,910.00 USD | 377.09 USD | 0.00 USD | `+42.34%` | `427.30` |
| `Live` | `Short` | `0.9145` | 105,980.00 USD | 26,070.00 USD | 0.00 USD | `+47.50%` | `28,505.55` |
| `Live` | `Short` | `0.9825` | 123,320.00 USD | 17,340.00 USD | 0.00 USD | `+58.47%` | `17,648.14` |
| `Live` | `Short` | `0.9935` | 123,490.00 USD | 166.01 USD | 0.00 USD | `+60.24%` | `167.10` |
| `Live` | `Short` | `1.09` | 123,970.00 USD | 479.74 USD | 0.00 USD | `+76.05%` | `439.52` |
| `Live` | `Short` | `1.12` | 126,760.00 USD | 2,800.00 USD | 0.00 USD | `+80.56%` | `2,500.00` |
| `Live` | `Short` | `1.14` | 213,480.00 USD | 86,710.00 USD | 0.00 USD | `+83.31%` | `76,300.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.3505` | 88,320.00 USD | 0.00 USD | 340.19 USD | `-43.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4635` | 87,980.00 USD | 0.00 USD | 104.57 USD | `-25.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4805` | 87,880.00 USD | 0.00 USD | 14,740.00 USD | `-22.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 73,140.00 USD | 0.00 USD | 604.46 USD | `-19.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5125` | 72,530.00 USD | 0.00 USD | 5,380.00 USD | `-17.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5205` | 67,150.00 USD | 0.00 USD | 228.77 USD | `-16.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5305` | 66,920.00 USD | 0.00 USD | 770.19 USD | `-14.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5445` | 66,150.00 USD | 0.00 USD | 8,750.00 USD | `-12.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5455` | 57,400.00 USD | 0.00 USD | 8,150.00 USD | `-12.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5485` | 49,250.00 USD | 0.00 USD | 4,500.00 USD | `-11.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5515` | 44,750.00 USD | 0.00 USD | 126.71 USD | `-11.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5525` | 44,630.00 USD | 0.00 USD | 126.90 USD | `-10.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5555` | 44,500.00 USD | 0.00 USD | 33,000.00 USD | `-10.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5565` | 11,500.00 USD | 0.00 USD | 173.58 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5595` | 11,330.00 USD | 0.00 USD | 127.61 USD | `-9.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 11,200.00 USD | 0.00 USD | 339.84 USD | `-9.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5625` | 10,860.00 USD | 0.00 USD | 126.55 USD | `-9.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5655` | 10,730.00 USD | 0.00 USD | 127.62 USD | `-8.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5695` | 10,610.00 USD | 0.00 USD | 127.30 USD | `-8.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5715` | 10,480.00 USD | 0.00 USD | 127.63 USD | `-7.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5755` | 10,350.00 USD | 0.00 USD | 127.29 USD | `-7.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5785` | 10,220.00 USD | 0.00 USD | 127.36 USD | `-6.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5815` | 10,100.00 USD | 0.00 USD | 127.27 USD | `-6.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5835` | 9,970.00 USD | 0.00 USD | 178.88 USD | `-5.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5845` | 9,790.00 USD | 0.00 USD | 127.33 USD | `-5.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5865` | 9,660.00 USD | 0.00 USD | 128.36 USD | `-5.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5875` | 9,530.00 USD | 0.00 USD | 128.34 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5895` | 9,410.00 USD | 0.00 USD | 128.45 USD | `-4.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5905` | 9,280.00 USD | 0.00 USD | 127.30 USD | `-4.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5925` | 9,150.00 USD | 0.00 USD | 265.69 USD | `-4.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5975` | 8,880.00 USD | 0.00 USD | 784.58 USD | `-3.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 8,100.00 USD | 0.00 USD | 3,510.00 USD | `-3.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 4,590.00 USD | 0.00 USD | 1,510.00 USD | `-2.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6065` | 3,090.00 USD | 0.00 USD | 1,910.00 USD | `-2.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6085` | 1,180.00 USD | 0.00 USD | 301.32 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6175` | 877.25 USD | 0.00 USD | 699.67 USD | `-0.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6185` | 177.58 USD | 0.00 USD | 177.58 USD | `-0.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6205` | 541.40 USD | 541.40 USD | 0.00 USD | `+0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6275` | 974.51 USD | 433.11 USD | 0.00 USD | `+1.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6285` | 1,440.00 USD | 469.94 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 5,870.00 USD | 4,430.00 USD | 0.00 USD | `+1.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6315` | 6,030.00 USD | 160.16 USD | 0.00 USD | `+1.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6335` | 14,430.00 USD | 8,390.00 USD | 0.00 USD | `+2.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6345` | 14,700.00 USD | 276.40 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6395` | 15,900.00 USD | 1,200.00 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6405` | 16,050.00 USD | 145.91 USD | 0.00 USD | `+3.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6445` | 16,170.00 USD | 121.42 USD | 0.00 USD | `+3.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6485` | 16,620.00 USD | 447.03 USD | 0.00 USD | `+4.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6505` | 17,180.00 USD | 567.58 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6525` | 17,300.00 USD | 111.92 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6535` | 17,650.00 USD | 349.76 USD | 0.00 USD | `+5.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6555` | 21,720.00 USD | 4,080.00 USD | 0.00 USD | `+5.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6565` | 22,010.00 USD | 284.88 USD | 0.00 USD | `+5.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6585` | 23,450.00 USD | 1,440.00 USD | 0.00 USD | `+6.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6595` | 24,190.00 USD | 746.46 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6605` | 24,770.00 USD | 580.23 USD | 0.00 USD | `+6.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6645` | 24,900.00 USD | 124.55 USD | 0.00 USD | `+7.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6655` | 25,180.00 USD | 283.50 USD | 0.00 USD | `+7.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6675` | 25,470.00 USD | 290.78 USD | 0.00 USD | `+7.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6685` | 25,640.00 USD | 170.95 USD | 0.00 USD | `+7.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6695` | 27,310.00 USD | 1,670.00 USD | 0.00 USD | `+7.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6705` | 27,470.00 USD | 162.91 USD | 0.00 USD | `+8.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6715` | 27,680.00 USD | 202.63 USD | 0.00 USD | `+8.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6725` | 29,350.00 USD | 1,670.00 USD | 0.00 USD | `+8.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6745` | 29,950.00 USD | 598.31 USD | 0.00 USD | `+8.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6755` | 30,310.00 USD | 361.53 USD | 0.00 USD | `+8.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 32,440.00 USD | 2,130.00 USD | 0.00 USD | `+9.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6805` | 32,650.00 USD | 214.20 USD | 0.00 USD | `+9.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6815` | 43,210.00 USD | 10,560.00 USD | 0.00 USD | `+9.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6825` | 43,330.00 USD | 112.49 USD | 0.00 USD | `+10.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6835` | 43,430.00 USD | 108.41 USD | 0.00 USD | `+10.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6855` | 43,550.00 USD | 112.98 USD | 0.00 USD | `+10.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6865` | 43,840.00 USD | 292.33 USD | 0.00 USD | `+10.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6875` | 43,980.00 USD | 140.41 USD | 0.00 USD | `+10.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6885` | 44,490.00 USD | 514.80 USD | 0.00 USD | `+11.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6895` | 44,690.00 USD | 194.09 USD | 0.00 USD | `+11.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6915` | 44,790.00 USD | 101.96 USD | 0.00 USD | `+11.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6925` | 45,810.00 USD | 1,020.00 USD | 0.00 USD | `+11.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6945` | 46,420.00 USD | 610.10 USD | 0.00 USD | `+12.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6955` | 46,520.00 USD | 101.38 USD | 0.00 USD | `+12.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6965` | 47,310.00 USD | 789.18 USD | 0.00 USD | `+12.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6985` | 47,420.00 USD | 102.99 USD | 0.00 USD | `+12.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7005` | 47,550.00 USD | 137.19 USD | 0.00 USD | `+12.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7015` | 48,110.00 USD | 561.40 USD | 0.00 USD | `+13.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7085` | 49,060.00 USD | 947.29 USD | 0.00 USD | `+14.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7095` | 49,190.00 USD | 132.99 USD | 0.00 USD | `+14.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7115` | 49,320.00 USD | 122.04 USD | 0.00 USD | `+14.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7135` | 49,620.00 USD | 307.58 USD | 0.00 USD | `+15.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7165` | 51,460.00 USD | 1,830.00 USD | 0.00 USD | `+15.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7195` | 51,640.00 USD | 183.26 USD | 0.00 USD | `+16.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7205` | 51,790.00 USD | 147.15 USD | 0.00 USD | `+16.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7215` | 55,050.00 USD | 3,260.00 USD | 0.00 USD | `+16.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7225` | 55,200.00 USD | 150.08 USD | 0.00 USD | `+16.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7265` | 61,620.00 USD | 6,410.00 USD | 0.00 USD | `+17.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7325` | 61,780.00 USD | 165.17 USD | 0.00 USD | `+18.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7345` | 62,810.00 USD | 1,030.00 USD | 0.00 USD | `+18.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7375` | 62,920.00 USD | 106.75 USD | 0.00 USD | `+18.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7395` | 63,130.00 USD | 208.16 USD | 0.00 USD | `+19.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7405` | 63,860.00 USD | 733.09 USD | 0.00 USD | `+19.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7415` | 64,020.00 USD | 156.98 USD | 0.00 USD | `+19.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7425` | 64,150.00 USD | 132.95 USD | 0.00 USD | `+19.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7445` | 64,580.00 USD | 432.66 USD | 0.00 USD | `+20.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7455` | 66,750.00 USD | 2,170.00 USD | 0.00 USD | `+20.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7475` | 67,070.00 USD | 318.43 USD | 0.00 USD | `+20.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7505` | 67,210.00 USD | 141.39 USD | 0.00 USD | `+21.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7525` | 67,340.00 USD | 134.74 USD | 0.00 USD | `+21.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7565` | 71,460.00 USD | 4,120.00 USD | 0.00 USD | `+22.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7575` | 71,970.00 USD | 511.82 USD | 0.00 USD | `+22.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7585` | 72,110.00 USD | 135.82 USD | 0.00 USD | `+22.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7615` | 72,980.00 USD | 875.23 USD | 0.00 USD | `+22.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7635` | 73,080.00 USD | 103.35 USD | 0.00 USD | `+23.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7665` | 73,210.00 USD | 127.48 USD | 0.00 USD | `+23.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7675` | 73,310.00 USD | 101.61 USD | 0.00 USD | `+23.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7695` | 73,500.00 USD | 186.97 USD | 0.00 USD | `+24.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7705` | 73,610.00 USD | 109.43 USD | 0.00 USD | `+24.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7775` | 73,780.00 USD | 166.70 USD | 0.00 USD | `+25.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7815` | 74,910.00 USD | 1,140.00 USD | 0.00 USD | `+26.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7865` | 81,230.00 USD | 6,310.00 USD | 0.00 USD | `+26.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8095` | 81,360.00 USD | 133.42 USD | 0.00 USD | `+30.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8125` | 93,430.00 USD | 12,070.00 USD | 0.00 USD | `+31.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8335` | 94,360.00 USD | 929.08 USD | 0.00 USD | `+34.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8475` | 134,950.00 USD | 40,590.00 USD | 0.00 USD | `+36.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8505` | 151,690.00 USD | 16,740.00 USD | 0.00 USD | `+37.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8515` | 164,410.00 USD | 12,720.00 USD | 0.00 USD | `+37.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8525` | 176,190.00 USD | 11,780.00 USD | 0.00 USD | `+37.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8705` | 177,470.00 USD | 1,280.00 USD | 0.00 USD | `+40.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8725` | 177,630.00 USD | 159.86 USD | 0.00 USD | `+40.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 177,820.00 USD | 193.62 USD | 0.00 USD | `+46.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 178,160.00 USD | 340.54 USD | 0.00 USD | `+53.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 178,310.00 USD | 145.72 USD | 0.00 USD | `+56.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 180,340.00 USD | 2,030.00 USD | 0.00 USD | `+59.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 180,480.00 USD | 136.10 USD | 0.00 USD | `+61.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 181,030.00 USD | 550.48 USD | 0.00 USD | `+61.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 181,340.00 USD | 314.99 USD | 0.00 USD | `+65.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 181,940.00 USD | 602.17 USD | 0.00 USD | `+69.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 182,310.00 USD | 360.61 USD | 0.00 USD | `+71.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 183,250.00 USD | 942.77 USD | 0.00 USD | `+74.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 183,590.00 USD | 337.31 USD | 0.00 USD | `+74.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 183,980.00 USD | 397.19 USD | 0.00 USD | `+77.50%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.5320` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 11,240.00 USD | 0.00 USD | 3,480.00 USD |
| `7D` | `0.5340` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD |
| `1D` | `0.5350` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 2,650.00 USD | 1,850.00 USD | 1,870.00 USD |
| `7D` | `0.5360` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 2,440.00 USD | 3,040.00 USD | 0.00 USD |
| `1D` | `0.5370` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 4,720.00 USD | 2,450.00 USD | 1,860.00 USD |
| `7D` | `0.5380` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 0.00 USD | 1,550.00 USD | 2,940.00 USD |
| `1D` | `0.5390` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 6,850.00 USD | 1,140.00 USD | 5,480.00 USD |
| `1D` | `0.5410` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 618.50 USD | 0.00 USD | 2,000.00 USD |
| `7D` | `0.5420` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 7,660.00 USD | 1,290.00 USD | 2,950.00 USD |
| `1D` | `0.5430` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 3,300.00 USD | 0.00 USD | 3,430.00 USD |
| `7D` | `0.5440` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 0.00 USD | 1,150.00 USD | 6,970.00 USD |
| `1D` | `0.5450` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 1,070.00 USD | 298.25 USD | 1,030.00 USD |
| `7D` | `0.5460` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 2,250.00 USD | 3,030.00 USD | 5,190.00 USD |
| `1D` | `0.5470` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 3,980.00 USD | 633.67 USD | 499.51 USD |
| `7D` | `0.5480` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 2,000.00 USD | 795.70 USD | 4,470.00 USD |
| `1D` | `0.5490` | 999,560.00 USD | 0.00 USD | 999,560.00 USD | 0.00 USD | 0.00 USD | 7,230.00 USD |
| `7D` | `0.5500` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 5,990.00 USD | 1,440.00 USD | 6,710.00 USD |
| `1D` | `0.5510` | 992,330.00 USD | 0.00 USD | 992,330.00 USD | 0.00 USD | 0.00 USD | 849.87 USD |
| `7D` | `0.5520` | 991,540.00 USD | 0.00 USD | 991,540.00 USD | 4,110.00 USD | 1,920.00 USD | 1,880.00 USD |
| `1D` | `0.5530` | 991,480.00 USD | 0.00 USD | 991,480.00 USD | 1,260.00 USD | 0.00 USD | 432.53 USD |
| `7D` | `0.5540` | 983,630.00 USD | 0.00 USD | 983,630.00 USD | 12,840.00 USD | 4,860.00 USD | 18,470.00 USD |
| `1D` | `0.5550` | 989,790.00 USD | 0.00 USD | 989,790.00 USD | 1,090.00 USD | 1,520.00 USD | 32.36 USD |
| `7D` | `0.5560` | 947,460.00 USD | 0.00 USD | 947,460.00 USD | 13,490.00 USD | 1,920.00 USD | 6,250.00 USD |
| `1D` | `0.5570` | 987,150.00 USD | 0.00 USD | 987,150.00 USD | 0.00 USD | 1,940.00 USD | 553.28 USD |
| `7D` | `0.5580` | 925,800.00 USD | 0.00 USD | 925,800.00 USD | 6,000.00 USD | 6,820.00 USD | 18,300.00 USD |
| `1D` | `0.5590` | 984,650.00 USD | 0.00 USD | 984,650.00 USD | 1,100.00 USD | 2,960.00 USD | 2,330.00 USD |
| `7D` | `0.5600` | 894,690.00 USD | 0.00 USD | 894,690.00 USD | 4,070.00 USD | 8,160.00 USD | 2,500.00 USD |
| `1D` | `0.5610` | 978,260.00 USD | 0.00 USD | 978,260.00 USD | 1,550.00 USD | 2,040.00 USD | 1,950.00 USD |
| `7D` | `0.5620` | 879,960.00 USD | 0.00 USD | 879,960.00 USD | 19,480.00 USD | 7,420.00 USD | 11,550.00 USD |
| `1D` | `0.5630` | 972,720.00 USD | 0.00 USD | 972,720.00 USD | 715.25 USD | 1,020.00 USD | 5,030.00 USD |
| `7D` | `0.5640` | 841,510.00 USD | 0.00 USD | 841,510.00 USD | 2,950.00 USD | 741.21 USD | 27.20 USD |
| `1D` | `0.5650` | 965,960.00 USD | 0.00 USD | 965,960.00 USD | 0.00 USD | 2,730.00 USD | 463.14 USD |
| `7D` | `0.5660` | 837,800.00 USD | 0.00 USD | 837,800.00 USD | 11,490.00 USD | 2,990.00 USD | 4,430.00 USD |
| `1D` | `0.5670` | 962,760.00 USD | 0.00 USD | 962,760.00 USD | 0.00 USD | 232.89 USD | 2.20 USD |
| `7D` | `0.5680` | 818,900.00 USD | 0.00 USD | 818,900.00 USD | 5,100.00 USD | 0.00 USD | 2,890.00 USD |
| `7D` | `0.5700` | 810,910.00 USD | 0.00 USD | 810,910.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD |
| `1D` | `0.5710` | 962,530.00 USD | 0.00 USD | 962,530.00 USD | 0.00 USD | 2,350.00 USD | 0.00 USD |
| `7D` | `0.5720` | 808,330.00 USD | 0.00 USD | 808,330.00 USD | 0.00 USD | 4,370.00 USD | 1,360.00 USD |
| `7D` | `0.5740` | 802,600.00 USD | 0.00 USD | 802,600.00 USD | 8,160.00 USD | 1,100.00 USD | 1,610.00 USD |
| `7D` | `0.5760` | 791,720.00 USD | 0.00 USD | 791,720.00 USD | 2,150.00 USD | 0.00 USD | 19.23 USD |
| `1D` | `0.5770` | 960,170.00 USD | 0.00 USD | 960,170.00 USD | 0.00 USD | 0.00 USD | 34.98 USD |
| `7D` | `0.5780` | 789,550.00 USD | 0.00 USD | 789,550.00 USD | 0.00 USD | 0.00 USD | 1,570.00 USD |
| `1D` | `0.5790` | 960,140.00 USD | 0.00 USD | 960,140.00 USD | 0.00 USD | 0.00 USD | 59.63 USD |
| `7D` | `0.5800` | 787,980.00 USD | 0.00 USD | 787,980.00 USD | 1,610.00 USD | 0.00 USD | 2,850.00 USD |
| `7D` | `0.5820` | 783,530.00 USD | 0.00 USD | 783,530.00 USD | 0.00 USD | 0.00 USD | 6,520.00 USD |
| `1D` | `0.5830` | 960,080.00 USD | 0.00 USD | 960,080.00 USD | 0.00 USD | 1,000.00 USD | 0.00 USD |
| `1D` | `0.5870` | 959,080.00 USD | 0.00 USD | 959,080.00 USD | 2,890.00 USD | 1,290.00 USD | 18,370.00 USD |
| `7D` | `0.5880` | 777,010.00 USD | 0.00 USD | 777,010.00 USD | 3,110.00 USD | 1,400.00 USD | 65.70 USD |
| `1D` | `0.5890` | 936,520.00 USD | 0.00 USD | 936,520.00 USD | 4,730.00 USD | 1,580.00 USD | 3,700.00 USD |
| `7D` | `0.5900` | 772,430.00 USD | 0.00 USD | 772,430.00 USD | 3,120.00 USD | 1,560.00 USD | 15.37 USD |
| `1D` | `0.5910` | 926,520.00 USD | 0.00 USD | 926,520.00 USD | 4,730.00 USD | 3,210.00 USD | 4,100.00 USD |
| `7D` | `0.5920` | 767,740.00 USD | 0.00 USD | 767,740.00 USD | 11,690.00 USD | 2,820.00 USD | 6,030.00 USD |
| `1D` | `0.5930` | 914,480.00 USD | 0.00 USD | 914,480.00 USD | 14,740.00 USD | 4,790.00 USD | 13,540.00 USD |
| `7D` | `0.5940` | 747,200.00 USD | 0.00 USD | 747,200.00 USD | 10,090.00 USD | 0.00 USD | 9,780.00 USD |
| `1D` | `0.5950` | 881,410.00 USD | 0.00 USD | 881,410.00 USD | 25,410.00 USD | 17,240.00 USD | 6,340.00 USD |
| `7D` | `0.5960` | 727,330.00 USD | 0.00 USD | 727,330.00 USD | 18,180.00 USD | 18,410.00 USD | 13,190.00 USD |
| `1D` | `0.5970` | 832,410.00 USD | 0.00 USD | 832,410.00 USD | 12,480.00 USD | 7,520.00 USD | 17,730.00 USD |
| `7D` | `0.5980` | 677,550.00 USD | 0.00 USD | 677,550.00 USD | 20,380.00 USD | 826.53 USD | 19,920.00 USD |
| `1D` | `0.5990` | 794,690.00 USD | 0.00 USD | 794,690.00 USD | 18,900.00 USD | 2,880.00 USD | 44,840.00 USD |
| `7D` | `0.6000` | 636,420.00 USD | 0.00 USD | 636,420.00 USD | 3,320.00 USD | 2,140.00 USD | 18,810.00 USD |
| `1D` | `0.6010` | 728,070.00 USD | 0.00 USD | 728,070.00 USD | 735.24 USD | 461.96 USD | 12,530.00 USD |
| `7D` | `0.6020` | 612,150.00 USD | 0.00 USD | 612,150.00 USD | 23,960.00 USD | 8,040.00 USD | 4,060.00 USD |
| `1D` | `0.6030` | 714,340.00 USD | 0.00 USD | 714,340.00 USD | 26,000.00 USD | 16,180.00 USD | 27.08 USD |
| `7D` | `0.6040` | 576,090.00 USD | 0.00 USD | 576,090.00 USD | 8,620.00 USD | 3,100.00 USD | 7,920.00 USD |
| `1D` | `0.6050` | 672,140.00 USD | 0.00 USD | 672,140.00 USD | 6,990.00 USD | 4,070.00 USD | 20,150.00 USD |
| `7D` | `0.6060` | 556,460.00 USD | 0.00 USD | 556,460.00 USD | 0.00 USD | 0.00 USD | 227.43 USD |
| `1D` | `0.6070` | 640,920.00 USD | 0.00 USD | 640,920.00 USD | 16,200.00 USD | 15,620.00 USD | 7,980.00 USD |
| `7D` | `0.6080` | 556,230.00 USD | 0.00 USD | 556,230.00 USD | 2,860.00 USD | 0.00 USD | 9,370.00 USD |
| `1D` | `0.6090` | 601,130.00 USD | 0.00 USD | 601,130.00 USD | 9,390.00 USD | 29,040.00 USD | 14,240.00 USD |
| `7D` | `0.6100` | 544,000.00 USD | 0.00 USD | 544,000.00 USD | 21,400.00 USD | 47,430.00 USD | 25,300.00 USD |
| `1D` | `0.6110` | 548,460.00 USD | 0.00 USD | 548,460.00 USD | 5,380.00 USD | 11,860.00 USD | 0.00 USD |
| `7D` | `0.6120` | 449,860.00 USD | 0.00 USD | 449,860.00 USD | 22,270.00 USD | 5,720.00 USD | 18,510.00 USD |
| `1D` | `0.6130` | 531,210.00 USD | 0.00 USD | 531,210.00 USD | 13,330.00 USD | 596.50 USD | 22,770.00 USD |
| `7D` | `0.6140` | 403,360.00 USD | 0.00 USD | 403,360.00 USD | 51,550.00 USD | 8,040.00 USD | 10,780.00 USD |
| `1D` | `0.6150` | 494,510.00 USD | 0.00 USD | 494,510.00 USD | 36,090.00 USD | 18,080.00 USD | 0.00 USD |
| `7D` | `0.6160` | 332,990.00 USD | 0.00 USD | 332,990.00 USD | 12,920.00 USD | 7,460.00 USD | 6,600.00 USD |
| `1D` | `0.6170` | 440,350.00 USD | 0.00 USD | 440,350.00 USD | 0.00 USD | 0.00 USD | 13,910.00 USD |
| `7D` | `0.6180` | 306,000.00 USD | 0.00 USD | 306,000.00 USD | 20,870.00 USD | 2,610.00 USD | 228.92 USD |
| `1D` | `0.6190` | 426,440.00 USD | 0.00 USD | 426,440.00 USD | 0.00 USD | 0.00 USD | 15,950.00 USD |
| `7D` | `0.6200` | 282,290.00 USD | 0.00 USD | 282,290.00 USD | 23,430.00 USD | 0.00 USD | 18,670.00 USD |
| `1D` | `0.6210` | 410,490.00 USD | 0.00 USD | 410,490.00 USD | 1,990.00 USD | 18,390.00 USD | 0.00 USD |
| `7D` | `0.6220` | 240,190.00 USD | 0.00 USD | 240,190.00 USD | 4,760.00 USD | 22,640.00 USD | 224.68 USD |
| `1D` | `0.6230` | 390,100.00 USD | 0.00 USD | 390,100.00 USD | 2,520.00 USD | 6,780.00 USD | 0.00 USD |
| `7D` | `0.6240` | 212,560.00 USD | 0.00 USD | 212,560.00 USD | 0.00 USD | 0.00 USD | 171.81 USD |
| `1D` | `0.6250` | 380,800.00 USD | 0.00 USD | 380,800.00 USD | 25,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6260` | 212,390.00 USD | 0.00 USD | 212,390.00 USD | 40,330.00 USD | 0.00 USD | 595.48 USD |
| `7D` | `0.6280` | 171,470.00 USD | 0.00 USD | 171,470.00 USD | 0.00 USD | 0.00 USD | 463.59 USD |
| `7D` | `0.6300` | 171,000.00 USD | 0.00 USD | 171,000.00 USD | 0.00 USD | 0.00 USD | 10,290.00 USD |
| `1D` | `0.6310` | 355,200.00 USD | 0.00 USD | 355,200.00 USD | 25,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6320` | 160,710.00 USD | 0.00 USD | 160,710.00 USD | 0.00 USD | 0.00 USD | 369.35 USD |
| `1D` | `0.6330` | 329,890.00 USD | 0.00 USD | 329,890.00 USD | 50,610.00 USD | 0.00 USD | 33,350.00 USD |
| `7D` | `0.6340` | 160,340.00 USD | 0.00 USD | 160,340.00 USD | 68,660.00 USD | 0.00 USD | 381.22 USD |
| `1D` | `0.6350` | 245,920.00 USD | 0.00 USD | 245,920.00 USD | 73,350.00 USD | 0.00 USD | 40,540.00 USD |
| `7D` | `0.6360` | 91,300.00 USD | 0.00 USD | 91,300.00 USD | 34,320.00 USD | 0.00 USD | 56,980.00 USD |
| `1D` | `0.6370` | 132,030.00 USD | 0.00 USD | 132,030.00 USD | 50,620.00 USD | 6,240.00 USD | 75,170.00 USD |
| `1D` | `0.6380` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6380` | 39,090.00 USD | 39,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39,090.00 USD |
| `7D` | `0.6380` | 78,170.00 USD | 78,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39,090.00 USD |
| `1D` | `0.6390` | 81,860.00 USD | 81,860.00 USD | 0.00 USD | 18,790.00 USD | 10,860.00 USD | 52,210.00 USD |
| `7D` | `0.6400` | 98,690.00 USD | 98,690.00 USD | 0.00 USD | 0.00 USD | 7,510.00 USD | 13,010.00 USD |
| `1D` | `0.6410` | 203,560.00 USD | 203,560.00 USD | 0.00 USD | 58,000.00 USD | 29,530.00 USD | 34,170.00 USD |
| `7D` | `0.6420` | 197,130.00 USD | 197,130.00 USD | 0.00 USD | 55,350.00 USD | 26,560.00 USD | 16,530.00 USD |
| `1D` | `0.6430` | 359,390.00 USD | 359,390.00 USD | 0.00 USD | 79,540.00 USD | 29,430.00 USD | 46,870.00 USD |
| `7D` | `0.6440` | 284,520.00 USD | 284,520.00 USD | 0.00 USD | 44,690.00 USD | 24,820.00 USD | 17,870.00 USD |
| `1D` | `0.6450` | 581,360.00 USD | 581,360.00 USD | 0.00 USD | 110,010.00 USD | 31,650.00 USD | 80,310.00 USD |
| `7D` | `0.6460` | 642,050.00 USD | 642,050.00 USD | 0.00 USD | 172,610.00 USD | 46,630.00 USD | 138,290.00 USD |
| `1D` | `0.6470` | 737,710.00 USD | 737,710.00 USD | 0.00 USD | 126,580.00 USD | 22,630.00 USD | 7,140.00 USD |
| `7D` | `0.6480` | 788,010.00 USD | 788,010.00 USD | 0.00 USD | 86,440.00 USD | 26,520.00 USD | 33,000.00 USD |
| `1D` | `0.6490` | 917,860.00 USD | 917,860.00 USD | 0.00 USD | 173,130.00 USD | 6,780.00 USD | 234.70 USD |
| `7D` | `0.6500` | 993,970.00 USD | 993,970.00 USD | 0.00 USD | 73,560.00 USD | 0.00 USD | 132,400.00 USD |
| `1D` | `0.6510` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 120,420.00 USD | 0.00 USD | 11,630.00 USD |
| `7D` | `0.6520` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 271,060.00 USD | 10,910.00 USD | 104,780.00 USD |
| `1D` | `0.6530` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 89,280.00 USD | 9,040.00 USD | 0.00 USD |
| `7D` | `0.6540` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 15,730.00 USD | 0.00 USD | 61,750.00 USD |
| `1D` | `0.6550` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 11,450.00 USD | 0.00 USD | 17,520.00 USD |
| `7D` | `0.6560` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 5,380.00 USD | 847.61 USD |
| `1D` | `0.6570` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,980.00 USD |
| `7D` | `0.6580` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 28,280.00 USD | 9,490.00 USD |
| `1D` | `0.6590` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 9,200.00 USD | 98.76 USD |
| `7D` | `0.6600` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 15,500.00 USD | 580.13 USD |
| `1D` | `0.6610` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 8,400.00 USD | 199.40 USD |
| `7D` | `0.6620` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 128.16 USD |
| `1D` | `0.6630` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,740.00 USD |
| `7D` | `0.6640` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 20,160.00 USD | 0.00 USD | 534.34 USD |
| `1D` | `0.6650` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 11,190.00 USD | 3,160.00 USD | 17,480.00 USD |
| `7D` | `0.6660` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 6,770.00 USD | 436.87 USD |
| `1D` | `0.6670` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 18,850.00 USD | 0.00 USD | 5,410.00 USD |
| `7D` | `0.6680` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 308.18 USD |
| `1D` | `0.6690` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 3,550.00 USD | 4,390.00 USD |
| `7D` | `0.6700` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 820.19 USD |
| `1D` | `0.6710` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 50,800.00 USD | 1,920.00 USD | 30,710.00 USD |
| `7D` | `0.6720` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 58,470.00 USD | 0.00 USD | 30,140.00 USD |
| `1D` | `0.6730` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 24,320.00 USD | 3,670.00 USD | 4,570.00 USD |
| `7D` | `0.6740` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 39,730.00 USD | 0.00 USD | 99.42 USD |
| `1D` | `0.6750` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 93,070.00 USD | 13,090.00 USD | 21,290.00 USD |
| `7D` | `0.6760` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 77,970.00 USD | 33,090.00 USD |
| `1D` | `0.6770` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 26,380.00 USD | 11,960.00 USD | 14,290.00 USD |
| `7D` | `0.6780` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 63,600.00 USD | 14,400.00 USD | 17,930.00 USD |
| `1D` | `0.6790` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 33,610.00 USD | 31,290.00 USD | 23,290.00 USD |
| `7D` | `0.6800` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 0.00 USD |
| `1D` | `0.6810` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 1,940.00 USD | 10,080.00 USD |
| `7D` | `0.6820` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 32,570.00 USD | 53,450.00 USD | 145.79 USD |
| `1D` | `0.6830` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 47,170.00 USD | 42,080.00 USD | 44,580.00 USD |
| `7D` | `0.6840` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 57,890.00 USD | 54,300.00 USD | 102,430.00 USD |
| `1D` | `0.6850` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 96,870.00 USD | 31,640.00 USD | 21,980.00 USD |
| `7D` | `0.6860` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 49,930.00 USD | 14,540.00 USD | 10,480.00 USD |
| `1D` | `0.6870` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 103,470.00 USD | 5,540.00 USD | 16,430.00 USD |
| `7D` | `0.6880` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 38,030.00 USD | 17,300.00 USD | 0.00 USD |
| `1D` | `0.6890` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 14,350.00 USD | 9,600.00 USD | 38,800.00 USD |
| `7D` | `0.6900` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 15,510.00 USD | 16,550.00 USD |
| `1D` | `0.6910` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 43,430.00 USD | 5,760.00 USD | 60,800.00 USD |
| `7D` | `0.6920` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 69,620.00 USD | 2,090.00 USD | 62,020.00 USD |
| `1D` | `0.6930` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 26,830.00 USD | 0.00 USD | 13,840.00 USD |
| `7D` | `0.6940` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 14,220.00 USD | 0.00 USD | 42,600.00 USD |
| `1D` | `0.6950` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 33,700.00 USD | 8,880.00 USD | 13,260.00 USD |
| `7D` | `0.6960` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 59,960.00 USD | 0.00 USD | 12,390.00 USD |
| `1D` | `0.6970` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 91,820.00 USD | 10,780.00 USD | 34.66 USD |
| `7D` | `0.6980` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 35,980.00 USD | 16,990.00 USD | 0.00 USD |
| `1D` | `0.6990` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 14,320.00 USD | 8,940.00 USD | 6,660.00 USD |
| `7D` | `0.7000` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 29,740.00 USD | 0.00 USD | 40,190.00 USD |
| `1D` | `0.7010` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 33,760.00 USD | 4,020.00 USD | 16,240.00 USD |
| `7D` | `0.7020` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 16,350.00 USD | 0.00 USD | 53,230.00 USD |
| `1D` | `0.7030` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 18,690.00 USD | 0.00 USD | 10,530.00 USD |
| `7D` | `0.7040` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 95,520.00 USD | 0.00 USD | 96,250.00 USD |
| `1D` | `0.7050` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 59,720.00 USD | 5,290.00 USD | 27,750.00 USD |
| `7D` | `0.7060` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 47,840.00 USD | 33,490.00 USD | 178,200.00 USD |
| `1D` | `0.7070` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 28,570.00 USD | 25,720.00 USD | 30,900.00 USD |
| `7D` | `0.7080` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 24,440.00 USD | 64,870.00 USD | 82,560.00 USD |
| `1D` | `0.7090` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 36,000.00 USD | 6,660.00 USD | 13,210.00 USD |
| `7D` | `0.7100` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 150,830.00 USD | 63,530.00 USD | 148,790.00 USD |
| `1D` | `0.7110` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 11,400.00 USD | 10,040.00 USD | 15,290.00 USD |
| `7D` | `0.7120` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 101,040.00 USD | 78,760.00 USD | 228,080.00 USD |
| `1D` | `0.7130` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 44,600.00 USD | 8,520.00 USD | 48,930.00 USD |
| `7D` | `0.7140` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 202,560.00 USD | 67,260.00 USD | 133,230.00 USD |
| `1D` | `0.7150` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 42,280.00 USD | 11,520.00 USD | 30,350.00 USD |
| `7D` | `0.7160` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 113,040.00 USD | 65,260.00 USD | 164,360.00 USD |
| `1D` | `0.7170` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 22,310.00 USD | 15,690.00 USD | 19,840.00 USD |
| `7D` | `0.7180` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 165,860.00 USD | 56,910.00 USD | 66,540.00 USD |
| `1D` | `0.7190` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 19,020.00 USD | 8,580.00 USD | 20,180.00 USD |
| `7D` | `0.7200` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 93,750.00 USD | 45,160.00 USD | 177,940.00 USD |
| `1D` | `0.7210` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 10,550.00 USD | 13,010.00 USD | 16,940.00 USD |
| `7D` | `0.7220` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 318,420.00 USD | 67,130.00 USD | 98,130.00 USD |
| `1D` | `0.7230` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 7,870.00 USD | 7,380.00 USD | 8,260.00 USD |
| `7D` | `0.7240` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 146,110.00 USD | 24,910.00 USD | 128,950.00 USD |
| `1D` | `0.7250` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 16,070.00 USD | 6,080.00 USD | 13,820.00 USD |
| `7D` | `0.7260` | 6,680,000.00 USD | 6,680,000.00 USD | 0.00 USD | 106,410.00 USD | 52,120.00 USD | 175,450.00 USD |
| `1D` | `0.7270` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 46,660.00 USD | 5,430.00 USD | 24,990.00 USD |
| `7D` | `0.7280` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 99,750.00 USD | 40,180.00 USD | 83,870.00 USD |
| `1D` | `0.7290` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 33,620.00 USD | 8,680.00 USD | 25,970.00 USD |
| `7D` | `0.7300` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 115,310.00 USD | 60,310.00 USD | 109,420.00 USD |
| `1D` | `0.7310` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 10,990.00 USD | 8,670.00 USD | 17,420.00 USD |
| `7D` | `0.7320` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 189,840.00 USD | 65,640.00 USD | 80,460.00 USD |
| `1D` | `0.7330` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 12,500.00 USD | 3,310.00 USD | 10,920.00 USD |
| `7D` | `0.7340` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 31,260.00 USD | 8,620.00 USD | 63,250.00 USD |
| `1D` | `0.7350` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 735.24 USD | 461.96 USD | 3,550.00 USD |
| `7D` | `0.7360` | 7,810,000.00 USD | 7,810,000.00 USD | 0.00 USD | 103,600.00 USD | 46,790.00 USD | 35,030.00 USD |
| `1D` | `0.7370` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 12,380.00 USD | 8,300.00 USD | 7,420.00 USD |
| `7D` | `0.7380` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 73,710.00 USD | 19,000.00 USD | 60,620.00 USD |
| `1D` | `0.7390` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 6,990.00 USD | 4,070.00 USD | 4,100.00 USD |
| `7D` | `0.7400` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 1,730.00 USD | 4,760.00 USD | 37,020.00 USD |
| `1D` | `0.7410` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 16,200.00 USD | 1,640.00 USD | 9,550.00 USD |
| `7D` | `0.7420` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 35,810.00 USD | 41,830.00 USD | 31,380.00 USD |
| `1D` | `0.7430` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 1,240.00 USD | 969.00 USD | 149.25 USD |
| `7D` | `0.7440` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 74,450.00 USD | 39,890.00 USD | 70,380.00 USD |
| `1D` | `0.7450` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 8,160.00 USD | 1,410.00 USD | 4,100.00 USD |
| `7D` | `0.7460` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 88,800.00 USD | 28,800.00 USD | 51,780.00 USD |
| `1D` | `0.7470` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 5,380.00 USD | 0.00 USD | 6,850.00 USD |
| `7D` | `0.7480` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 60,580.00 USD | 28,900.00 USD | 38,290.00 USD |
| `1D` | `0.7490` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 2,140.00 USD | 596.50 USD | 2,060.00 USD |
| `1D` | `0.7500` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 6,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.7500` | 8,690,000.00 USD | 8,690,000.00 USD | 0.00 USD | 52,320.00 USD | 12,610.00 USD | 25,140.00 USD |
| `7D` | `0.7520` | 8,810,000.00 USD | 8,810,000.00 USD | 0.00 USD | 53,470.00 USD | 13,000.00 USD | 50,770.00 USD |
| `7D` | `0.7540` | 8,870,000.00 USD | 8,870,000.00 USD | 0.00 USD | 30,340.00 USD | 1,890.00 USD | 25,430.00 USD |
| `7D` | `0.7560` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 26,000.00 USD | 7,570.00 USD | 22,260.00 USD |
| `7D` | `0.7580` | 9,040,000.00 USD | 9,040,000.00 USD | 0.00 USD | 55,420.00 USD | 11,790.00 USD | 45,930.00 USD |
| `7D` | `0.7600` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 57,020.00 USD | 4,320.00 USD | 80,740.00 USD |
| `7D` | `0.7620` | 9,280,000.00 USD | 9,280,000.00 USD | 0.00 USD | 54,140.00 USD | 24,170.00 USD | 21,540.00 USD |
| `7D` | `0.7640` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 50,390.00 USD | 13,520.00 USD | 41,540.00 USD |
| `7D` | `0.7660` | 9,550,000.00 USD | 9,550,000.00 USD | 0.00 USD | 56,130.00 USD | 18,130.00 USD | 91,090.00 USD |
| `7D` | `0.7680` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 66,570.00 USD | 32,520.00 USD | 41,010.00 USD |
| `7D` | `0.7700` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 10,860.00 USD | 12,600.00 USD | 41,730.00 USD |
| `7D` | `0.7720` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 58,380.00 USD | 32,920.00 USD | 25,780.00 USD |
| `7D` | `0.7740` | 9,980,000.00 USD | 9,980,000.00 USD | 0.00 USD | 51,600.00 USD | 25,250.00 USD | 35,740.00 USD |
| `7D` | `0.7760` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 38,170.00 USD | 2,980.00 USD | 12,740.00 USD |
| `7D` | `0.7780` | 10,160,000.00 USD | 10,160,000.00 USD | 0.00 USD | 68,800.00 USD | 20,860.00 USD | 32,580.00 USD |
| `7D` | `0.7800` | 10,320,000.00 USD | 10,320,000.00 USD | 0.00 USD | 60,490.00 USD | 21,940.00 USD | 80,690.00 USD |
| `7D` | `0.7820` | 10,440,000.00 USD | 10,440,000.00 USD | 0.00 USD | 90,020.00 USD | 17,850.00 USD | 6,240.00 USD |
| `7D` | `0.7840` | 10,540,000.00 USD | 10,540,000.00 USD | 0.00 USD | 95,370.00 USD | 7,150.00 USD | 2,180.00 USD |
| `7D` | `0.7860` | 10,650,000.00 USD | 10,650,000.00 USD | 0.00 USD | 32,690.00 USD | 9,290.00 USD | 63,600.00 USD |
| `7D` | `0.7880` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 11,900.00 USD | 22,650.00 USD | 29,500.00 USD |
| `7D` | `0.7900` | 10,810,000.00 USD | 10,810,000.00 USD | 0.00 USD | 59,120.00 USD | 16,710.00 USD | 17,430.00 USD |
| `7D` | `0.7910` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 30,620.00 USD | 5,860.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `91.12M` | Total OI Tokens: `142,707,468.6 APT`
  * 1h OI Change: `-3.97%` | 4h OI Change: `-8.33%` | 24h OI Change: `-9.89%`
  * Exchange Breakdown: Binance=`16.88M` | Bybit=`18.53M` | OKX=`4.39M` | Hyperliquid=`3.70M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-86.08` | Last 24h: `8.88K` | Last 3d: `10.89K` | Last 7d: `5.22K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0030%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0012%` | **USDT KuCoin** | `0.0076%` |
| **USDT MEXC** | `-0.0030%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0018%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `APT` | `47.35%` | `52.65%` | `0.90` | 4,940,000.00 USD |
| `15M` | `Binance` | `40.65%` | `59.35%` | `0.68` | 1,990,000.00 USD |
| `15M` | `OKX` | `51%` | `49%` | `1.04` | 563,820.00 USD |
| `15M` | `Bybit` | `47.24%` | `52.76%` | `0.90` | 440,380.00 USD |
| `15M` | `KuCoin` | `60.03%` | `39.97%` | `1.50` | 215,200.00 USD |
| `15M` | `Gate` | `37.56%` | `62.44%` | `0.60` | 52,830.00 USD |
| `15M` | `Bitget` | `47.25%` | `52.75%` | `0.90` | 203,620.00 USD |
| `15M` | `BingX` | `53.5%` | `46.5%` | `1.15` | 90,010.00 USD |
| `15M` | `MEXC` | `84.42%` | `15.58%` | `5.42` | 85,920.00 USD |
| `15M` | `Bitunix` | `60.18%` | `39.82%` | `1.51` | 294,680.00 USD |
| `15M` | `Hyperliquid` | `68.81%` | `31.19%` | `2.21` | 16,990.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.32%` | `50.68%` | `0.97` | 787,870.00 USD |
| `15M` | `Crypto.com` | `5.87%` | `94.13%` | `0.06` | 47.23 USD |
| `15M` | `WhiteBIT` | `49.9%` | `50.1%` | `1.00` | 177,720.00 USD |
| `15M` | `HTX` | `47.55%` | `52.45%` | `0.91` | 2,080.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `85.9%` | `14.1%` | `6.09` | 2,100.00 USD |
| `15M` | `Aster` | `0.7%` | `99.3%` | `0.01` | 15,470.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `23.44%` | `76.56%` | `0.31` | 3,510.00 USD |
| `15M` | `Whale Positions` | `40.65%` | `59.35%` | `0.68` | 1,990,000.00 USD |
| `15M` | `Global Accounts` | `47.35%` | `52.65%` | `0.90` | 4,940,000.00 USD |
| `1H` | `APT` | `48.33%` | `51.67%` | `0.94` | 75,090,000.00 USD |
| `1H` | `Binance` | `45.75%` | `54.25%` | `0.84` | 29,010,000.00 USD |
| `1H` | `OKX` | `48.15%` | `51.85%` | `0.93` | 9,990,000.00 USD |
| `1H` | `Bybit` | `58.63%` | `41.37%` | `1.42` | 9,470,000.00 USD |
| `1H` | `KuCoin` | `43.61%` | `56.39%` | `0.77` | 542,340.00 USD |
| `1H` | `Gate` | `47.46%` | `52.54%` | `0.90` | 4,210,000.00 USD |
| `1H` | `Bitget` | `39.06%` | `60.94%` | `0.64` | 3,000,000.00 USD |
| `1H` | `BingX` | `47.65%` | `52.35%` | `0.91` | 2,600,000.00 USD |
| `1H` | `MEXC` | `26.18%` | `73.82%` | `0.35` | 4,060,000.00 USD |
| `1H` | `Bitunix` | `51.84%` | `48.16%` | `1.08` | 1,450,000.00 USD |
| `1H` | `Hyperliquid` | `46.09%` | `53.91%` | `0.85` | 1,200,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `46.56%` | `53.44%` | `0.87` | 1,410,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `62.2%` | `37.8%` | `1.65` | 6,700,000.00 USD |
| `1H` | `HTX` | `42.49%` | `57.51%` | `0.74` | 431,730.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `71.59%` | `28.41%` | `2.52` | 569,220.00 USD |
| `1H` | `Aster` | `58.07%` | `41.93%` | `1.38` | 330,550.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `30.56%` | `69.44%` | `0.44` | 117,920.00 USD |
| `1H` | `Whale Positions` | `45.75%` | `54.25%` | `0.84` | 29,010,000.00 USD |
| `1H` | `Global Accounts` | `48.33%` | `51.67%` | `0.94` | 75,090,000.00 USD |
| `4H` | `APT` | `49.06%` | `50.94%` | `0.96` | 122,160,000.00 USD |
| `4H` | `Binance` | `46.18%` | `53.82%` | `0.86` | 43,200,000.00 USD |
| `4H` | `OKX` | `48.5%` | `51.5%` | `0.94` | 14,990,000.00 USD |
| `4H` | `Bybit` | `53.81%` | `46.19%` | `1.16` | 14,680,000.00 USD |
| `4H` | `KuCoin` | `47.28%` | `52.72%` | `0.90` | 835,230.00 USD |
| `4H` | `Gate` | `48.22%` | `51.78%` | `0.93` | 9,870,000.00 USD |
| `4H` | `Bitget` | `41.61%` | `58.39%` | `0.71` | 4,040,000.00 USD |
| `4H` | `BingX` | `48.05%` | `51.95%` | `0.92` | 9,370,000.00 USD |
| `4H` | `MEXC` | `30.84%` | `69.16%` | `0.45` | 5,840,000.00 USD |
| `4H` | `Bitunix` | `49.4%` | `50.6%` | `0.98` | 2,290,000.00 USD |
| `4H` | `Hyperliquid` | `42.87%` | `57.13%` | `0.75` | 1,560,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.62%` | `52.38%` | `0.91` | 2,890,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `69.98%` | `30.02%` | `2.33` | 10,700,000.00 USD |
| `4H` | `HTX` | `44.64%` | `55.36%` | `0.81` | 626,580.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `67.22%` | `32.78%` | `2.05` | 656,170.00 USD |
| `4H` | `Aster` | `58.22%` | `41.78%` | `1.39` | 410,560.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `23.04%` | `76.96%` | `0.30` | 171,510.00 USD |
| `4H` | `Whale Positions` | `46.18%` | `53.82%` | `0.86` | 43,200,000.00 USD |
| `4H` | `Global Accounts` | `49.06%` | `50.94%` | `0.96` | 122,160,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.6715` | `0.6701` | `0.6715` | `0.6721` | `0.6670` | 386,689.12 USD | 212,109.34 USD | 174,579.78 USD | 37,529.57 USD | `+9.71%` | `19B / 4S` |
| `0:00 UTC` | `0.6734` | `0.6731` | `0.6734` | `0.6741` | `0.6704` | 427,696.28 USD | 267,875.40 USD | 159,820.88 USD | 108,054.53 USD | `+25.26%` | `9B / 2S` |
| `5:00 UTC` | `0.6713` | `0.6715` | `0.6713` | `0.6739` | `0.6704` | 216,510.95 USD | 86,107.15 USD | 130,403.80 USD | -44,296.65 USD | `-20.46%` | `5B / 11S` |
| `0:00 UTC` | `0.6618` | `0.6610` | `0.6618` | `0.6728` | `0.6545` | 3,111,032.57 USD | 1,289,720.42 USD | 1,821,312.14 USD | -531,591.72 USD | `-17.09%` | `14B / 47S` |
| `5:00 UTC` | `0.6646` | `0.6634` | `0.6646` | `0.6663` | `0.6601` | 1,040,684.48 USD | 553,372.77 USD | 487,311.70 USD | 66,061.07 USD | `+6.35%` | `21B / 6S` |
| `0:00 UTC` | `0.6256` | `0.6358` | `0.6256` | `0.6640` | `0.6136` | 10,130,057.36 USD | 3,799,647.14 USD | 6,330,410.22 USD | -2,530,763.08 USD | `-24.98%` | `3B / 31S` |
| `5:00 UTC` | `0.6208` | `0.6173` | `0.6208` | `0.6292` | `0.6004` | 5,930,137.61 USD | 2,790,946.56 USD | 3,139,191.05 USD | -348,244.48 USD | `-5.87%` | `7B / 8S` |
| `0:00 UTC` | `0.6268` | `0.6270` | `0.6268` | `0.6331` | `0.6164` | 2,767,755.14 USD | 1,444,801.14 USD | 1,322,953.99 USD | 121,847.15 USD | `+4.40%` | `10B / 14S` |
| `5:00 UTC` | `0.6356` | `0.6324` | `0.6356` | `0.6401` | `0.6246` | 2,269,133.84 USD | 1,171,035.44 USD | 1,098,098.41 USD | 72,937.03 USD | `+3.21%` | `20B / 14S` |
| `0:00 UTC` | `0.6381` | `0.6362` | `0.6381` | `0.6411` | `0.6316` | 1,026,868.32 USD | 534,199.81 USD | 492,668.51 USD | 41,531.30 USD | `+4.04%` | `23B / 13S` |

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
| `5m` | -13,370.00 USD | 55,740.00 USD | **`ACCUMULATION`** |
| `15m` | -28,520.00 USD | -31,040.00 USD | **`DISTRIBUTION`** |
| `30m` | 99,350.00 USD | 483,530.00 USD | **`ACCUMULATION`** |
| `1h` | 285,940.00 USD | -3,340,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -176,390.00 USD | -3,880,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -324,760.00 USD | -4,860,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -150,200.00 USD | -5,490,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -46,310.00 USD | -6,360,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -3,490.00 USD | -6,740,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,400,000.00 USD | -10,010,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,070,000.00 USD | -24,070,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,610,000.00 USD | -104,810,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-13.37K` | 15m=`-28.52K` | 1h=`+285.94K` | 24h=`-1.40M`
* Futures Capital Netflows: 5m=`+55.74K` | 15m=`-31.04K` | 1h=`-3.34M` | 24h=`-10.01M`
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
  * `2026-10-30 02:54:26 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:10:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:11:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:11:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:11:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
