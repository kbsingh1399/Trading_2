# 🏛️ SOVEREIGN CANDIDATE DOSSIER: APT
**Canonical Key**: `APT` | **Broker Instrument**: `APTUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 11:38:27 IST` (`2026-10-30 06:08:27 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `4h` | `0.6161` | `0.6282` | `0.6117` | `0.6220` | `4,866,986` | 3,018,326.79 USD | -300,631.91 USD | `-9.96%` | -6,021,880.07 USD | `+0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:33:47 IST` |

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
| `7D` | `Long Liquidation` | `0.5220` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 32.85 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5245` | 209.80 USD | 82,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5260` | 1,190,000.00 USD | 1,190,000.00 USD | 5,850.00 USD | 0.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5280` | 1,180,000.00 USD | 1,180,000.00 USD | 5,050.00 USD | 0.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5295` | 1,840.00 USD | 82,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5300` | 1,180,000.00 USD | 1,180,000.00 USD | 5,120.00 USD | 0.00 USD | 9,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5315` | 11,510.00 USD | 80,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5320` | 1,160,000.00 USD | 1,160,000.00 USD | 8,680.00 USD | 0.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5325` | 2,260.00 USD | 68,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5335` | 163.22 USD | 66,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5340` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5360` | 1,150,000.00 USD | 1,150,000.00 USD | 2,440.00 USD | 3,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5380` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 1,550.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5400` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 2,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5420` | 1,130,000.00 USD | 1,130,000.00 USD | 16,260.00 USD | 1,290.00 USD | 2,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5440` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 1,150.00 USD | 13,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5445` | 855.28 USD | 66,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5460` | 1,100,000.00 USD | 1,100,000.00 USD | 2,250.00 USD | 3,030.00 USD | 5,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,630.00 USD | 65,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5480` | 1,090,000.00 USD | 1,090,000.00 USD | 2,000.00 USD | 795.70 USD | 4,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5500` | 1,130,000.00 USD | 1,130,000.00 USD | 1,410.00 USD | 0.00 USD | 6,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5500` | 1,080,000.00 USD | 1,080,000.00 USD | 5,990.00 USD | 1,440.00 USD | 6,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5510` | 1,130,000.00 USD | 1,130,000.00 USD | 1,340.00 USD | 0.00 USD | 1,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5520` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 1,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5520` | 1,070,000.00 USD | 1,070,000.00 USD | 4,110.00 USD | 1,920.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5530` | 1,120,000.00 USD | 1,120,000.00 USD | 1,260.00 USD | 1,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5540` | 1,120,000.00 USD | 1,120,000.00 USD | 5,390.00 USD | 5,750.00 USD | 4,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5540` | 1,060,000.00 USD | 1,060,000.00 USD | 12,840.00 USD | 7,260.00 USD | 18,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5545` | 48,560.00 USD | 63,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5550` | 1,100,000.00 USD | 1,100,000.00 USD | 2,940.00 USD | 0.00 USD | 1,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5560` | 1,100,000.00 USD | 1,100,000.00 USD | 1,680.00 USD | 686.25 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5560` | 1,020,000.00 USD | 1,020,000.00 USD | 13,490.00 USD | 1,920.00 USD | 10,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5570` | 1,100,000.00 USD | 1,100,000.00 USD | 1,690.00 USD | 2,460.00 USD | 4,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5580` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 2,820.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5580` | 993,880.00 USD | 993,880.00 USD | 6,000.00 USD | 6,820.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5585` | 10,520.00 USD | 15,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5590` | 1,080,000.00 USD | 1,080,000.00 USD | 1,670.00 USD | 1,870.00 USD | 1,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5600` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 1,690.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5600` | 962,770.00 USD | 962,770.00 USD | 4,070.00 USD | 8,160.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5610` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 823.46 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5615` | 258.48 USD | 4,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5620` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 776.64 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5620` | 947,960.00 USD | 947,960.00 USD | 19,480.00 USD | 7,420.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5630` | 1,070,000.00 USD | 1,070,000.00 USD | 2,260.00 USD | 1,560.00 USD | 6,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5635` | 244.90 USD | 4,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5640` | 1,060,000.00 USD | 1,060,000.00 USD | 4,020.00 USD | 3,380.00 USD | 10,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5640` | 909,520.00 USD | 909,520.00 USD | 2,950.00 USD | 2,380.00 USD | 2,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5655` | 1,920.00 USD | 4,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5660` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 3,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5660` | 901,270.00 USD | 901,270.00 USD | 11,490.00 USD | 2,990.00 USD | 4,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5665` | 1,370.00 USD | 2,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5680` | 882,210.00 USD | 882,210.00 USD | 5,100.00 USD | 0.00 USD | 2,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5690` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 5,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5700` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5700` | 874,180.00 USD | 874,180.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5710` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 2,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5715` | 289.08 USD | 995.18 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5720` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 832.92 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5720` | 871,600.00 USD | 871,600.00 USD | 0.00 USD | 4,370.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5730` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5740` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 839.21 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5740` | 855,290.00 USD | 855,290.00 USD | 21,620.00 USD | 1,100.00 USD | 1,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5745` | 706.11 USD | 706.11 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5750` | 1,010,000.00 USD | 1,010,000.00 USD | 4,330.00 USD | 840.09 USD | 20,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5760` | 981,170.00 USD | 981,170.00 USD | 15,020.00 USD | 2,220.00 USD | 2,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5760` | 830,950.00 USD | 830,950.00 USD | 2,150.00 USD | 7,300.00 USD | 122.71 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5770` | 961,830.00 USD | 961,830.00 USD | 16,730.00 USD | 3,970.00 USD | 279.20 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5780` | 940,850.00 USD | 940,850.00 USD | 3,070.00 USD | 1,330.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5780` | 821,370.00 USD | 821,370.00 USD | 40,930.00 USD | 0.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5790` | 925,550.00 USD | 925,550.00 USD | 11,420.00 USD | 2,690.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5800` | 903,700.00 USD | 903,700.00 USD | 3,310.00 USD | 2,750.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5800` | 778,660.00 USD | 778,660.00 USD | 1,610.00 USD | 3,900.00 USD | 27,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5810` | 896,050.00 USD | 896,050.00 USD | 0.00 USD | 3,190.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5820` | 876,210.00 USD | 876,210.00 USD | 2,580.00 USD | 4,510.00 USD | 4,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5820` | 745,220.00 USD | 745,220.00 USD | 0.00 USD | 0.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5830` | 864,940.00 USD | 864,940.00 USD | 4,910.00 USD | 819.33 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5840` | 859,200.00 USD | 859,200.00 USD | 0.00 USD | 2,190.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5840` | 738,700.00 USD | 738,700.00 USD | 0.00 USD | 0.00 USD | 21,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5850` | 852,730.00 USD | 852,730.00 USD | 2,950.00 USD | 0.00 USD | 30,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5860` | 818,930.00 USD | 818,930.00 USD | 2,810.00 USD | 3,110.00 USD | 7,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5860` | 717,540.00 USD | 717,540.00 USD | 0.00 USD | 0.00 USD | 284.34 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5870` | 805,130.00 USD | 805,130.00 USD | 15,080.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5880` | 787,740.00 USD | 787,740.00 USD | 34,650.00 USD | 10,250.00 USD | 7,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5880` | 717,260.00 USD | 717,260.00 USD | 3,110.00 USD | 16,010.00 USD | 65.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5890` | 735,050.00 USD | 735,050.00 USD | 38,270.00 USD | 11,450.00 USD | 7.65 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5900` | 685,310.00 USD | 685,310.00 USD | 29,060.00 USD | 13,050.00 USD | 10,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5900` | 698,080.00 USD | 698,080.00 USD | 104,240.00 USD | 1,560.00 USD | 15.37 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5910` | 633,060.00 USD | 633,060.00 USD | 26,100.00 USD | 13,220.00 USD | 18,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5920` | 575,710.00 USD | 575,710.00 USD | 25,960.00 USD | 6,190.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5920` | 592,260.00 USD | 592,260.00 USD | 11,690.00 USD | 19,960.00 USD | 75,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5930` | 536,450.00 USD | 536,450.00 USD | 6,060.00 USD | 6,380.00 USD | 12,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5940` | 511,060.00 USD | 511,060.00 USD | 15,260.00 USD | 1,300.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5940` | 485,130.00 USD | 485,130.00 USD | 10,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5950` | 486,100.00 USD | 486,100.00 USD | 26,720.00 USD | 3,220.00 USD | 70.10 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5960` | 456,090.00 USD | 456,090.00 USD | 12,010.00 USD | 1,860.00 USD | 8,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5960` | 475,040.00 USD | 475,040.00 USD | 18,180.00 USD | 18,410.00 USD | 387.78 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5970` | 433,640.00 USD | 433,640.00 USD | 13,040.00 USD | 0.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5980` | 415,420.00 USD | 415,420.00 USD | 10,410.00 USD | 2,390.00 USD | 62.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5980` | 438,060.00 USD | 438,060.00 USD | 20,380.00 USD | 0.00 USD | 3.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5990` | 402,560.00 USD | 402,560.00 USD | 0.00 USD | 836.21 USD | 1,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6000` | 400,620.00 USD | 400,620.00 USD | 2,680.00 USD | 2,480.00 USD | 7,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6000` | 417,670.00 USD | 417,670.00 USD | 3,320.00 USD | 0.00 USD | 12,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6010` | 387,580.00 USD | 387,580.00 USD | 2,960.00 USD | 6,370.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6020` | 373,220.00 USD | 373,220.00 USD | 2,680.00 USD | 7,430.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6020` | 402,350.00 USD | 402,350.00 USD | 0.00 USD | 12,130.00 USD | 50.15 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6030` | 361,390.00 USD | 361,390.00 USD | 34,080.00 USD | 14,050.00 USD | 3,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6040` | 309,620.00 USD | 309,620.00 USD | 6,530.00 USD | 9,900.00 USD | 5,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6040` | 390,170.00 USD | 390,170.00 USD | 38,530.00 USD | 18,680.00 USD | 89.59 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6050` | 288,190.00 USD | 288,190.00 USD | 20,690.00 USD | 1,370.00 USD | 7,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6060` | 258,190.00 USD | 258,190.00 USD | 8,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6060` | 332,870.00 USD | 332,870.00 USD | 0.00 USD | 0.00 USD | 20,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6070` | 249,780.00 USD | 249,780.00 USD | 8,430.00 USD | 2,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6080` | 238,760.00 USD | 238,760.00 USD | 3,650.00 USD | 3,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6080` | 312,060.00 USD | 312,060.00 USD | 2,860.00 USD | 0.00 USD | 30,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6090` | 231,940.00 USD | 231,940.00 USD | 8,370.00 USD | 1,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6100` | 221,940.00 USD | 221,940.00 USD | 0.00 USD | 0.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6100` | 278,830.00 USD | 278,830.00 USD | 21,400.00 USD | 47,430.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6110` | 180,400.00 USD | 180,400.00 USD | 12,430.00 USD | 3,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6120` | 164,590.00 USD | 164,590.00 USD | 30,040.00 USD | 1,670.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6120` | 184,880.00 USD | 184,880.00 USD | 35,760.00 USD | 20,330.00 USD | 18,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6130` | 130,700.00 USD | 130,700.00 USD | 44,750.00 USD | 4,950.00 USD | 34,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6140` | 46,850.00 USD | 46,850.00 USD | 6,130.00 USD | 8,290.00 USD | 19,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6140` | 110,280.00 USD | 110,280.00 USD | 51,900.00 USD | 15,390.00 USD | 18,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6160` | 13,240.00 USD | 13,240.00 USD | 0.00 USD | 0.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6160` | 24,300.00 USD | 24,300.00 USD | 0.00 USD | 0.00 USD | 16,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6180` | 10,120.00 USD | 10,120.00 USD | 0.00 USD | 1,760.00 USD | 8,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6180` | 7,780.00 USD | 7,780.00 USD | 7,600.00 USD | 0.00 USD | 173.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6200` | 8,600.00 USD | 8,600.00 USD | 0.00 USD | 0.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6200` | 17,210.00 USD | 17,210.00 USD | 0.00 USD | 0.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6200` | 50,530.00 USD | 50,530.00 USD | 21,280.00 USD | 0.00 USD | 29,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6210` | 34,070.00 USD | 34,070.00 USD | 0.00 USD | 0.00 USD | 16,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6220` | 36,450.00 USD | 36,450.00 USD | 0.00 USD | 2,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6220` | 77,940.00 USD | 77,940.00 USD | 4,760.00 USD | 22,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6240` | 58,160.00 USD | 58,160.00 USD | 21,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6240` | 85,410.00 USD | 85,410.00 USD | 0.00 USD | 7,300.00 USD | 171.81 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6250` | 74,900.00 USD | 74,900.00 USD | 16,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6260` | 83,270.00 USD | 83,270.00 USD | 0.00 USD | 8,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6260` | 193,650.00 USD | 193,650.00 USD | 108,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6270` | 131,100.00 USD | 131,100.00 USD | 47,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6280` | 180,190.00 USD | 180,190.00 USD | 9,840.00 USD | 16,420.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6280` | 279,680.00 USD | 279,680.00 USD | 38,530.00 USD | 22,580.00 USD | 24,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6285` | 10,370.00 USD | 10,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6290` | 221,870.00 USD | 221,870.00 USD | 20,690.00 USD | 6,580.00 USD | 14,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6300` | 245,520.00 USD | 245,520.00 USD | 10,980.00 USD | 3,430.00 USD | 9,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6300` | 328,560.00 USD | 328,560.00 USD | 0.00 USD | 0.00 USD | 48,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6310` | 297,490.00 USD | 297,490.00 USD | 22,880.00 USD | 7,390.00 USD | 21,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6320` | 348,700.00 USD | 348,700.00 USD | 34,120.00 USD | 6,080.00 USD | 11,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6320` | 328,930.00 USD | 328,930.00 USD | 0.00 USD | 0.00 USD | 369.35 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6330` | 400,830.00 USD | 400,830.00 USD | 22,870.00 USD | 10,960.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6340` | 474,420.00 USD | 474,420.00 USD | 29,640.00 USD | 3,190.00 USD | 40,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6340` | 397,980.00 USD | 397,980.00 USD | 68,660.00 USD | 0.00 USD | 381.22 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6350` | 521,810.00 USD | 521,810.00 USD | 39,480.00 USD | 1,700.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6360` | 640,480.00 USD | 640,480.00 USD | 54,130.00 USD | 4,140.00 USD | 60,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6360` | 489,270.00 USD | 489,270.00 USD | 34,320.00 USD | 0.00 USD | 56,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6370` | 672,630.00 USD | 672,630.00 USD | 0.00 USD | 5,010.00 USD | 27,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6380` | 718,280.00 USD | 718,280.00 USD | 5,370.00 USD | 28,210.00 USD | 12,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6380` | 543,070.00 USD | 543,070.00 USD | 0.00 USD | 0.00 USD | 53,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6390` | 802,080.00 USD | 802,080.00 USD | 26,050.00 USD | 7,210.00 USD | 50,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6400` | 954,670.00 USD | 954,670.00 USD | 72,890.00 USD | 43,770.00 USD | 35,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6400` | 591,080.00 USD | 591,080.00 USD | 19,270.00 USD | 15,680.00 USD | 13,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6410` | 1,020,000.00 USD | 1,020,000.00 USD | 35,660.00 USD | 14,660.00 USD | 14,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6420` | 1,130,000.00 USD | 1,130,000.00 USD | 71,960.00 USD | 15,540.00 USD | 23,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6420` | 727,220.00 USD | 727,220.00 USD | 55,350.00 USD | 44,770.00 USD | 36,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6430` | 1,200,000.00 USD | 1,200,000.00 USD | 36,780.00 USD | 13,280.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6440` | 1,300,000.00 USD | 1,300,000.00 USD | 31,190.00 USD | 18,570.00 USD | 48,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6440` | 814,600.00 USD | 814,600.00 USD | 44,690.00 USD | 24,820.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6450` | 1,410,000.00 USD | 1,410,000.00 USD | 61,360.00 USD | 12,700.00 USD | 35,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6460` | 1,480,000.00 USD | 1,480,000.00 USD | 47,150.00 USD | 12,100.00 USD | 9,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6460` | 1,170,000.00 USD | 1,170,000.00 USD | 172,610.00 USD | 46,630.00 USD | 138,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6465` | 867.43 USD | 11,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6470` | 1,570,000.00 USD | 1,570,000.00 USD | 59,430.00 USD | 17,210.00 USD | 11,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6475` | 209.47 USD | 11,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6480` | 1,650,000.00 USD | 1,650,000.00 USD | 70,780.00 USD | 7,630.00 USD | 373.19 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6480` | 1,320,000.00 USD | 1,320,000.00 USD | 86,440.00 USD | 26,520.00 USD | 33,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6490` | 1,730,000.00 USD | 1,730,000.00 USD | 63,670.00 USD | 2,070.00 USD | 12,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6500` | 1,780,000.00 USD | 1,780,000.00 USD | 44,490.00 USD | 8,390.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6500` | 1,530,000.00 USD | 1,530,000.00 USD | 73,560.00 USD | 0.00 USD | 139,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6510` | 1,850,000.00 USD | 1,850,000.00 USD | 58,460.00 USD | 0.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6520` | 1,970,000.00 USD | 1,970,000.00 USD | 93,550.00 USD | 13,180.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6520` | 1,950,000.00 USD | 1,950,000.00 USD | 298,050.00 USD | 15,000.00 USD | 104,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6530` | 1,980,000.00 USD | 1,980,000.00 USD | 11,510.00 USD | 3,910.00 USD | 11.74 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6540` | 2,020,000.00 USD | 2,020,000.00 USD | 24,280.00 USD | 0.00 USD | 10,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6540` | 2,030,000.00 USD | 2,030,000.00 USD | 15,730.00 USD | 4,440.00 USD | 61,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6550` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 6,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6560` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6560` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 5,380.00 USD | 847.61 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6570` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 4,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6580` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 3,310.00 USD | 34.49 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6580` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 28,280.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6590` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 5,890.00 USD | 164.02 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6600` | 2,060,000.00 USD | 2,060,000.00 USD | 6,010.00 USD | 9,280.00 USD | 59.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6600` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 18,420.00 USD | 580.13 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6610` | 2,070,000.00 USD | 2,070,000.00 USD | 6,690.00 USD | 835.70 USD | 142.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6620` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 530.84 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6620` | 2,100,000.00 USD | 2,100,000.00 USD | 8,600.00 USD | 0.00 USD | 128.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6630` | 2,080,000.00 USD | 2,080,000.00 USD | 2,590.00 USD | 0.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6640` | 2,090,000.00 USD | 2,090,000.00 USD | 11,190.00 USD | 837.01 USD | 135.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6640` | 2,140,000.00 USD | 2,140,000.00 USD | 33,660.00 USD | 0.00 USD | 7,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6650` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 3,160.00 USD | 17,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6660` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 839.67 USD | 7,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6660` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 6,770.00 USD | 436.87 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6670` | 2,140,000.00 USD | 2,140,000.00 USD | 18,850.00 USD | 0.00 USD | 24.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6680` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 138.15 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6680` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 415.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6690` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 3,550.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6700` | 2,190,000.00 USD | 2,190,000.00 USD | 8,830.00 USD | 1,920.00 USD | 24,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6700` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 994.50 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6710` | 2,240,000.00 USD | 2,240,000.00 USD | 41,970.00 USD | 0.00 USD | 5,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6720` | 2,240,000.00 USD | 2,240,000.00 USD | 1,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6720` | 2,240,000.00 USD | 2,240,000.00 USD | 58,470.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6730` | 2,270,000.00 USD | 2,270,000.00 USD | 25,660.00 USD | 3,670.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6740` | 2,350,000.00 USD | 2,350,000.00 USD | 64,370.00 USD | 8,170.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6740` | 2,280,000.00 USD | 2,280,000.00 USD | 39,730.00 USD | 0.00 USD | 99.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6750` | 2,400,000.00 USD | 2,400,000.00 USD | 28,700.00 USD | 4,630.00 USD | 12,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6760` | 2,420,000.00 USD | 2,420,000.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6760` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 77,970.00 USD | 33,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6770` | 2,460,000.00 USD | 2,460,000.00 USD | 19,930.00 USD | 8,320.00 USD | 15,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6780` | 2,520,000.00 USD | 2,520,000.00 USD | 33,610.00 USD | 13,860.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6780` | 2,490,000.00 USD | 2,490,000.00 USD | 63,600.00 USD | 16,810.00 USD | 18,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6790` | 2,550,000.00 USD | 2,550,000.00 USD | 2,940.00 USD | 18,610.00 USD | 12,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6800` | 2,560,000.00 USD | 2,560,000.00 USD | 1,680.00 USD | 686.25 USD | 2,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6800` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 16,590.00 USD | 4,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6810` | 2,570,000.00 USD | 2,570,000.00 USD | 1,690.00 USD | 2,460.00 USD | 11,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6820` | 2,620,000.00 USD | 2,620,000.00 USD | 22,600.00 USD | 16,590.00 USD | 9,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6820` | 2,600,000.00 USD | 2,600,000.00 USD | 32,570.00 USD | 53,450.00 USD | 145.79 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6830` | 2,700,000.00 USD | 2,700,000.00 USD | 26,250.00 USD | 17,300.00 USD | 36,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6840` | 2,780,000.00 USD | 2,780,000.00 USD | 45,780.00 USD | 17,210.00 USD | 15,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6840` | 2,810,000.00 USD | 2,810,000.00 USD | 57,890.00 USD | 54,300.00 USD | 102,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6850` | 2,850,000.00 USD | 2,850,000.00 USD | 39,200.00 USD | 5,780.00 USD | 24,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6860` | 2,910,000.00 USD | 2,910,000.00 USD | 40,250.00 USD | 4,380.00 USD | 14,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6860` | 2,890,000.00 USD | 2,890,000.00 USD | 49,930.00 USD | 14,540.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6870` | 2,980,000.00 USD | 2,980,000.00 USD | 63,220.00 USD | 1,160.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6880` | 3,030,000.00 USD | 3,030,000.00 USD | 15,430.00 USD | 11,160.00 USD | 26,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6880` | 2,950,000.00 USD | 2,950,000.00 USD | 38,030.00 USD | 17,300.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6890` | 3,040,000.00 USD | 3,040,000.00 USD | 1,180.00 USD | 0.00 USD | 8,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6900` | 3,090,000.00 USD | 3,090,000.00 USD | 18,600.00 USD | 4,990.00 USD | 21,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6900` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 17,150.00 USD | 16,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6910` | 3,150,000.00 USD | 3,150,000.00 USD | 28,860.00 USD | 1,730.00 USD | 32,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6920` | 3,180,000.00 USD | 3,180,000.00 USD | 16,800.00 USD | 0.00 USD | 13,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6920` | 3,110,000.00 USD | 3,110,000.00 USD | 69,620.00 USD | 2,090.00 USD | 62,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6930` | 3,190,000.00 USD | 3,190,000.00 USD | 10,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6940` | 3,170,000.00 USD | 3,170,000.00 USD | 14,220.00 USD | 0.00 USD | 42,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6960` | 3,240,000.00 USD | 3,240,000.00 USD | 59,960.00 USD | 0.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6980` | 3,300,000.00 USD | 3,300,000.00 USD | 35,980.00 USD | 16,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6995` | 52,350.00 USD | 63,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7000` | 3,370,000.00 USD | 3,370,000.00 USD | 29,740.00 USD | 0.00 USD | 40,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7020` | 3,450,000.00 USD | 3,450,000.00 USD | 29,810.00 USD | 0.00 USD | 53,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7040` | 3,640,000.00 USD | 3,640,000.00 USD | 95,520.00 USD | 0.00 USD | 96,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7060` | 3,900,000.00 USD | 3,900,000.00 USD | 47,840.00 USD | 33,490.00 USD | 178,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7080` | 4,070,000.00 USD | 4,070,000.00 USD | 24,440.00 USD | 64,870.00 USD | 82,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7100` | 4,430,000.00 USD | 4,430,000.00 USD | 150,830.00 USD | 63,530.00 USD | 148,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7120` | 4,840,000.00 USD | 4,840,000.00 USD | 101,040.00 USD | 78,760.00 USD | 228,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7140` | 5,250,000.00 USD | 5,250,000.00 USD | 202,560.00 USD | 67,260.00 USD | 133,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7160` | 5,590,000.00 USD | 5,590,000.00 USD | 113,040.00 USD | 65,260.00 USD | 164,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7180` | 5,880,000.00 USD | 5,880,000.00 USD | 165,860.00 USD | 56,910.00 USD | 66,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7200` | 6,190,000.00 USD | 6,190,000.00 USD | 93,750.00 USD | 45,160.00 USD | 177,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7220` | 6,680,000.00 USD | 6,680,000.00 USD | 318,420.00 USD | 67,130.00 USD | 98,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7240` | 6,980,000.00 USD | 6,980,000.00 USD | 146,110.00 USD | 24,910.00 USD | 128,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7245` | 364.39 USD | 64,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7260` | 7,310,000.00 USD | 7,310,000.00 USD | 106,410.00 USD | 52,120.00 USD | 175,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7280` | 7,540,000.00 USD | 7,540,000.00 USD | 99,750.00 USD | 40,180.00 USD | 83,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7300` | 7,820,000.00 USD | 7,820,000.00 USD | 115,310.00 USD | 60,310.00 USD | 109,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7320` | 8,160,000.00 USD | 8,160,000.00 USD | 189,840.00 USD | 65,640.00 USD | 80,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7340` | 8,250,000.00 USD | 8,250,000.00 USD | 31,260.00 USD | 8,620.00 USD | 56,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7360` | 8,430,000.00 USD | 8,430,000.00 USD | 103,600.00 USD | 42,680.00 USD | 35,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7380` | 8,590,000.00 USD | 8,590,000.00 USD | 73,710.00 USD | 19,000.00 USD | 60,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7400` | 8,610,000.00 USD | 8,610,000.00 USD | 1,730.00 USD | 4,760.00 USD | 11,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7420` | 8,710,000.00 USD | 8,710,000.00 USD | 35,810.00 USD | 35,860.00 USD | 31,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7440` | 8,890,000.00 USD | 8,890,000.00 USD | 74,450.00 USD | 33,900.00 USD | 70,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7460` | 9,050,000.00 USD | 9,050,000.00 USD | 88,800.00 USD | 17,230.00 USD | 51,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7480` | 9,170,000.00 USD | 9,170,000.00 USD | 60,580.00 USD | 28,900.00 USD | 38,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7500` | 9,260,000.00 USD | 9,260,000.00 USD | 52,320.00 USD | 12,610.00 USD | 25,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7520` | 9,370,000.00 USD | 9,370,000.00 USD | 53,470.00 USD | 13,000.00 USD | 35,610.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.1805` | 213,880.00 USD | 0.00 USD | 802.26 USD | `-70.87%` | `4,444.65` |
| `Live` | `Long` | `0.1875` | 213,080.00 USD | 0.00 USD | 269.27 USD | `-69.74%` | `1,436.09` |
| `Live` | `Long` | `0.2195` | 212,810.00 USD | 0.00 USD | 227.87 USD | `-64.57%` | `1,038.12` |
| `Live` | `Long` | `0.2205` | 212,580.00 USD | 0.00 USD | 221.88 USD | `-64.41%` | `1,006.27` |
| `Live` | `Long` | `0.2355` | 212,360.00 USD | 0.00 USD | 2,660.00 USD | `-61.99%` | `11,284.25` |
| `Live` | `Long` | `0.2425` | 209,700.00 USD | 0.00 USD | 1,460.00 USD | `-60.86%` | `6,000.00` |
| `Live` | `Long` | `0.3175` | 208,250.00 USD | 0.00 USD | 1,590.00 USD | `-48.76%` | `5,000.00` |
| `Live` | `Long` | `0.3295` | 206,660.00 USD | 0.00 USD | 9,370.00 USD | `-46.82%` | `28,446.85` |
| `Live` | `Long` | `0.3305` | 197,290.00 USD | 0.00 USD | 543.58 USD | `-46.66%` | `1,644.73` |
| `Live` | `Long` | `0.3545` | 196,740.00 USD | 0.00 USD | 177.25 USD | `-42.79%` | `500.00` |
| `Live` | `Long` | `0.3585` | 196,570.00 USD | 0.00 USD | 12,850.00 USD | `-42.14%` | `35,856.81` |
| `Live` | `Long` | `0.3615` | 183,710.00 USD | 0.00 USD | 542.25 USD | `-41.66%` | `1,500.00` |
| `Live` | `Long` | `0.3675` | 183,170.00 USD | 0.00 USD | 189.99 USD | `-40.69%` | `516.98` |
| `Live` | `Long` | `0.3905` | 182,980.00 USD | 0.00 USD | 359.26 USD | `-36.98%` | `919.99` |
| `Live` | `Long` | `0.3955` | 182,620.00 USD | 0.00 USD | 2,640.00 USD | `-36.17%` | `6,686.27` |
| `Live` | `Long` | `0.3995` | 179,980.00 USD | 0.00 USD | 271.06 USD | `-35.52%` | `678.49` |
| `Live` | `Long` | `0.4005` | 179,710.00 USD | 0.00 USD | 280.35 USD | `-35.36%` | `700.00` |
| `Live` | `Long` | `0.4095` | 179,430.00 USD | 0.00 USD | 414.59 USD | `-33.91%` | `1,012.44` |
| `Live` | `Long` | `0.4125` | 179,010.00 USD | 0.00 USD | 1,070.00 USD | `-33.42%` | `2,600.00` |
| `Live` | `Long` | `0.4135` | 177,940.00 USD | 0.00 USD | 1,600.00 USD | `-33.26%` | `3,868.97` |
| `Live` | `Long` | `0.4185` | 176,340.00 USD | 0.00 USD | 5,830.00 USD | `-32.46%` | `13,933.59` |
| `Live` | `Long` | `0.4255` | 170,510.00 USD | 0.00 USD | 224.96 USD | `-31.33%` | `528.69` |
| `Live` | `Long` | `0.4325` | 170,280.00 USD | 0.00 USD | 813.69 USD | `-30.20%` | `1,881.36` |
| `Live` | `Long` | `0.4475` | 169,470.00 USD | 0.00 USD | 226.63 USD | `-27.78%` | `506.43` |
| `Live` | `Long` | `0.4515` | 169,240.00 USD | 0.00 USD | 27,090.00 USD | `-27.13%` | `60,000.00` |
| `Live` | `Long` | `0.4535` | 142,150.00 USD | 0.00 USD | 5,530.00 USD | `-26.81%` | `12,191.83` |
| `Live` | `Long` | `0.4605` | 136,620.00 USD | 0.00 USD | 430.79 USD | `-25.68%` | `935.49` |
| `Live` | `Long` | `0.4615` | 136,190.00 USD | 0.00 USD | 4,860.00 USD | `-25.52%` | `10,534.29` |
| `Live` | `Long` | `0.4625` | 131,330.00 USD | 0.00 USD | 1,460.00 USD | `-25.36%` | `3,156.35` |
| `Live` | `Long` | `0.4645` | 129,870.00 USD | 0.00 USD | 876.05 USD | `-25.03%` | `1,886.00` |
| `Live` | `Long` | `0.4685` | 128,990.00 USD | 0.00 USD | 468.50 USD | `-24.39%` | `1,000.00` |
| `Live` | `Long` | `0.4835` | 128,530.00 USD | 0.00 USD | 135.33 USD | `-21.97%` | `279.90` |
| `Live` | `Long` | `0.4845` | 128,390.00 USD | 0.00 USD | 164.25 USD | `-21.80%` | `339.00` |
| `Live` | `Long` | `0.4855` | 128,230.00 USD | 0.00 USD | 181.88 USD | `-21.64%` | `374.62` |
| `Live` | `Long` | `0.4865` | 128,040.00 USD | 0.00 USD | 3,170.00 USD | `-21.48%` | `6,508.47` |
| `Live` | `Long` | `0.4925` | 124,880.00 USD | 0.00 USD | 10,520.00 USD | `-20.51%` | `21,364.96` |
| `Live` | `Long` | `0.4935` | 114,360.00 USD | 0.00 USD | 1,580.00 USD | `-20.35%` | `3,199.85` |
| `Live` | `Long` | `0.4945` | 112,780.00 USD | 0.00 USD | 7,030.00 USD | `-20.19%` | `14,223.31` |
| `Live` | `Long` | `0.4955` | 105,740.00 USD | 0.00 USD | 3,180.00 USD | `-20.03%` | `6,422.59` |
| `Live` | `Long` | `0.4965` | 102,560.00 USD | 0.00 USD | 143.19 USD | `-19.87%` | `288.40` |
| `Live` | `Long` | `0.4975` | 102,420.00 USD | 0.00 USD | 667.49 USD | `-19.71%` | `1,341.68` |
| `Live` | `Long` | `0.4985` | 101,750.00 USD | 0.00 USD | 429.90 USD | `-19.54%` | `862.38` |
| `Live` | `Long` | `0.5075` | 101,320.00 USD | 0.00 USD | 303.42 USD | `-18.09%` | `597.87` |
| `Live` | `Long` | `0.5085` | 101,020.00 USD | 0.00 USD | 102.82 USD | `-17.93%` | `202.20` |
| `Live` | `Long` | `0.5105` | 100,910.00 USD | 0.00 USD | 519.77 USD | `-17.61%` | `1,018.15` |
| `Live` | `Long` | `0.5125` | 100,390.00 USD | 0.00 USD | 248.05 USD | `-17.29%` | `484.00` |
| `Live` | `Long` | `0.5135` | 100,150.00 USD | 0.00 USD | 298.60 USD | `-17.12%` | `581.49` |
| `Live` | `Long` | `0.5175` | 99,850.00 USD | 0.00 USD | 9,440.00 USD | `-16.48%` | `18,249.92` |
| `Live` | `Long` | `0.5185` | 90,400.00 USD | 0.00 USD | 281.56 USD | `-16.32%` | `543.02` |
| `Live` | `Long` | `0.5245` | 90,120.00 USD | 0.00 USD | 209.80 USD | `-15.35%` | `400.00` |
| `Live` | `Long` | `0.5295` | 89,910.00 USD | 0.00 USD | 1,840.00 USD | `-14.54%` | `3,467.51` |
| `Live` | `Long` | `0.5315` | 88,080.00 USD | 0.00 USD | 11,510.00 USD | `-14.22%` | `21,664.95` |
| `Live` | `Long` | `0.5325` | 76,560.00 USD | 0.00 USD | 2,260.00 USD | `-14.06%` | `4,240.81` |
| `Live` | `Long` | `0.5335` | 74,300.00 USD | 0.00 USD | 163.22 USD | `-13.90%` | `305.95` |
| `Live` | `Long` | `0.5445` | 74,140.00 USD | 0.00 USD | 855.28 USD | `-12.12%` | `1,570.77` |
| `Live` | `Long` | `0.5475` | 73,280.00 USD | 0.00 USD | 1,630.00 USD | `-11.64%` | `2,968.46` |
| `Live` | `Long` | `0.5545` | 71,660.00 USD | 0.00 USD | 47,450.00 USD | `-10.51%` | `85,578.81` |
| `Live` | `Long` | `0.5585` | 24,210.00 USD | 0.00 USD | 10,520.00 USD | `-9.86%` | `18,834.52` |
| `Live` | `Long` | `0.5615` | 13,690.00 USD | 0.00 USD | 258.48 USD | `-9.38%` | `460.33` |
| `Live` | `Long` | `0.5635` | 13,430.00 USD | 0.00 USD | 244.90 USD | `-9.05%` | `434.61` |
| `Live` | `Long` | `0.5655` | 13,180.00 USD | 0.00 USD | 1,920.00 USD | `-8.73%` | `3,394.98` |
| `Live` | `Long` | `0.5665` | 11,260.00 USD | 0.00 USD | 1,370.00 USD | `-8.57%` | `2,421.90` |
| `Live` | `Long` | `0.5715` | 9,890.00 USD | 0.00 USD | 289.08 USD | `-7.76%` | `505.82` |
| `Live` | `Long` | `0.5745` | 9,600.00 USD | 0.00 USD | 706.11 USD | `-7.28%` | `1,229.08` |
| `Live` | `Long` | `0.5885` | 8,900.00 USD | 0.00 USD | 8,900.00 USD | `-5.02%` | `15,117.28` |
| `Live` | `Short` | `0.6475` | 209.47 USD | 209.47 USD | 0.00 USD | `+4.50%` | `323.51` |
| `Live` | `Short` | `0.6605` | 845.30 USD | 635.82 USD | 0.00 USD | `+6.60%` | `962.64` |
| `Live` | `Short` | `0.6885` | 58,030.00 USD | 57,180.00 USD | 0.00 USD | `+11.12%` | `83,055.27` |
| `Live` | `Short` | `0.7245` | 58,390.00 USD | 364.39 USD | 0.00 USD | `+16.93%` | `502.96` |
| `Live` | `Short` | `0.7685` | 60,460.00 USD | 2,060.00 USD | 0.00 USD | `+24.03%` | `2,683.46` |
| `Live` | `Short` | `0.7725` | 60,620.00 USD | 165.62 USD | 0.00 USD | `+24.68%` | `214.40` |
| `Live` | `Short` | `0.8005` | 79,740.00 USD | 19,120.00 USD | 0.00 USD | `+29.20%` | `23,882.80` |
| `Live` | `Short` | `0.8665` | 80,120.00 USD | 378.95 USD | 0.00 USD | `+39.85%` | `437.33` |
| `Live` | `Short` | `0.9215` | 102,410.00 USD | 22,290.00 USD | 0.00 USD | `+48.72%` | `24,191.51` |
| `Live` | `Short` | `0.9905` | 119,890.00 USD | 17,480.00 USD | 0.00 USD | `+59.86%` | `17,648.14` |
| `Live` | `Short` | `0.9935` | 120,060.00 USD | 166.01 USD | 0.00 USD | `+60.35%` | `167.10` |
| `Live` | `Short` | `1.02` | 146,030.00 USD | 25,970.00 USD | 0.00 USD | `+64.86%` | `25,423.72` |
| `Live` | `Short` | `1.04` | 151,220.00 USD | 5,190.00 USD | 0.00 USD | `+67.61%` | `5,000.00` |
| `Live` | `Short` | `1.07` | 233,130.00 USD | 81,910.00 USD | 0.00 USD | `+73.26%` | `76,300.00` |
| `Live` | `Short` | `1.09` | 233,610.00 USD | 479.74 USD | 0.00 USD | `+76.16%` | `439.52` |
| `Live` | `Short` | `1.12` | 236,410.00 USD | 2,800.00 USD | 0.00 USD | `+80.68%` | `2,500.00` |
| `Live` | `Short` | `1.17` | 236,910.00 USD | 501.44 USD | 0.00 USD | `+89.40%` | `427.30` |
| `Live` | `Short` | `1.19` | 237,140.00 USD | 227.46 USD | 0.00 USD | `+91.49%` | `191.71` |
| `Live` | `Short` | `1.19` | 237,340.00 USD | 199.98 USD | 0.00 USD | `+91.82%` | `168.26` |
| `Live` | `Short` | `1.22` | 238,130.00 USD | 796.83 USD | 0.00 USD | `+97.14%` | `652.34` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.3505` | 167,110.00 USD | 0.00 USD | 340.19 USD | `-43.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4635` | 166,770.00 USD | 0.00 USD | 104.57 USD | `-25.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4955` | 166,670.00 USD | 0.00 USD | 111.62 USD | `-20.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4965` | 166,560.00 USD | 0.00 USD | 111.85 USD | `-19.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 166,440.00 USD | 0.00 USD | 67,850.00 USD | `-19.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5015` | 98,600.00 USD | 0.00 USD | 112.97 USD | `-19.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5065` | 98,480.00 USD | 0.00 USD | 225.65 USD | `-18.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5085` | 98,260.00 USD | 0.00 USD | 101.97 USD | `-17.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5115` | 98,160.00 USD | 0.00 USD | 111.69 USD | `-17.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5125` | 98,050.00 USD | 0.00 USD | 5,380.00 USD | `-17.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 92,660.00 USD | 0.00 USD | 115.47 USD | `-16.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5175` | 92,550.00 USD | 0.00 USD | 116.58 USD | `-16.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5185` | 92,430.00 USD | 0.00 USD | 116.96 USD | `-16.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5205` | 92,320.00 USD | 0.00 USD | 539.96 USD | `-15.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5225` | 91,780.00 USD | 0.00 USD | 117.70 USD | `-15.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5235` | 91,660.00 USD | 0.00 USD | 117.93 USD | `-15.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5305` | 91,540.00 USD | 0.00 USD | 770.19 USD | `-14.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5445` | 90,770.00 USD | 0.00 USD | 8,750.00 USD | `-12.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5455` | 82,010.00 USD | 0.00 USD | 8,150.00 USD | `-11.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5485` | 73,860.00 USD | 0.00 USD | 4,500.00 USD | `-11.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5515` | 69,370.00 USD | 0.00 USD | 126.71 USD | `-10.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5525` | 69,240.00 USD | 0.00 USD | 126.90 USD | `-10.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5555` | 69,110.00 USD | 0.00 USD | 33,000.00 USD | `-10.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5565` | 36,120.00 USD | 0.00 USD | 173.58 USD | `-10.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5595` | 35,940.00 USD | 0.00 USD | 10,540.00 USD | `-9.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 25,410.00 USD | 0.00 USD | 339.84 USD | `-9.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5625` | 25,070.00 USD | 0.00 USD | 930.52 USD | `-9.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5655` | 24,140.00 USD | 0.00 USD | 127.62 USD | `-8.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5695` | 24,010.00 USD | 0.00 USD | 127.30 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5705` | 23,880.00 USD | 0.00 USD | 9,410.00 USD | `-7.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5715` | 14,470.00 USD | 0.00 USD | 127.63 USD | `-7.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5735` | 14,340.00 USD | 0.00 USD | 151.62 USD | `-7.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5755` | 14,190.00 USD | 0.00 USD | 999.82 USD | `-7.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5775` | 13,190.00 USD | 0.00 USD | 1,710.00 USD | `-6.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5785` | 11,470.00 USD | 0.00 USD | 127.36 USD | `-6.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5795` | 11,350.00 USD | 0.00 USD | 780.04 USD | `-6.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5815` | 10,570.00 USD | 0.00 USD | 127.27 USD | `-6.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5835` | 10,440.00 USD | 0.00 USD | 999.65 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5845` | 9,440.00 USD | 0.00 USD | 533.37 USD | `-5.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5905` | 8,910.00 USD | 0.00 USD | 127.30 USD | `-4.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5925` | 8,780.00 USD | 0.00 USD | 265.69 USD | `-4.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5975` | 8,510.00 USD | 0.00 USD | 597.80 USD | `-3.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5995` | 7,920.00 USD | 0.00 USD | 509.04 USD | `-3.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 7,410.00 USD | 0.00 USD | 953.02 USD | `-3.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6045` | 6,450.00 USD | 0.00 USD | 999.99 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 5,450.00 USD | 0.00 USD | 1,510.00 USD | `-2.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6065` | 3,950.00 USD | 0.00 USD | 1,910.00 USD | `-2.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6085` | 2,040.00 USD | 0.00 USD | 301.32 USD | `-1.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6115` | 1,740.00 USD | 0.00 USD | 629.83 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6135` | 1,110.00 USD | 0.00 USD | 410.30 USD | `-0.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6175` | 696.72 USD | 0.00 USD | 519.13 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6185` | 177.58 USD | 0.00 USD | 177.58 USD | `-0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6205` | 1,120.00 USD | 1,120.00 USD | 0.00 USD | `+0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6225` | 2,120.00 USD | 1,000.00 USD | 0.00 USD | `+0.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6275` | 2,560.00 USD | 433.11 USD | 0.00 USD | `+1.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6285` | 3,030.00 USD | 469.94 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 7,450.00 USD | 4,430.00 USD | 0.00 USD | `+1.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 7,720.00 USD | 269.44 USD | 0.00 USD | `+2.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6335` | 16,120.00 USD | 8,390.00 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6345` | 16,390.00 USD | 276.40 USD | 0.00 USD | `+2.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6395` | 17,590.00 USD | 1,200.00 USD | 0.00 USD | `+3.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6405` | 17,740.00 USD | 145.91 USD | 0.00 USD | `+3.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6445` | 17,860.00 USD | 121.42 USD | 0.00 USD | `+4.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6465` | 18,270.00 USD | 410.21 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6485` | 18,720.00 USD | 447.03 USD | 0.00 USD | `+4.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6505` | 19,290.00 USD | 567.58 USD | 0.00 USD | `+4.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6525` | 19,460.00 USD | 172.51 USD | 0.00 USD | `+5.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6555` | 23,540.00 USD | 4,080.00 USD | 0.00 USD | `+5.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6585` | 24,980.00 USD | 1,440.00 USD | 0.00 USD | `+6.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6595` | 25,720.00 USD | 746.46 USD | 0.00 USD | `+6.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6605` | 26,300.00 USD | 580.23 USD | 0.00 USD | `+6.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6635` | 26,590.00 USD | 289.66 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6645` | 26,850.00 USD | 262.60 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6655` | 27,140.00 USD | 283.50 USD | 0.00 USD | `+7.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6675` | 27,430.00 USD | 290.78 USD | 0.00 USD | `+7.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6695` | 29,100.00 USD | 1,670.00 USD | 0.00 USD | `+8.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6705` | 29,260.00 USD | 162.91 USD | 0.00 USD | `+8.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6745` | 29,860.00 USD | 598.31 USD | 0.00 USD | `+8.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 30,010.00 USD | 154.30 USD | 0.00 USD | `+9.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6805` | 30,230.00 USD | 214.20 USD | 0.00 USD | `+9.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6815` | 40,790.00 USD | 10,560.00 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6825` | 40,900.00 USD | 112.49 USD | 0.00 USD | `+10.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6845` | 42,030.00 USD | 1,130.00 USD | 0.00 USD | `+10.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6875` | 42,170.00 USD | 140.41 USD | 0.00 USD | `+10.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6885` | 42,690.00 USD | 514.80 USD | 0.00 USD | `+11.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6915` | 42,790.00 USD | 101.96 USD | 0.00 USD | `+11.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6925` | 43,810.00 USD | 1,020.00 USD | 0.00 USD | `+11.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6945` | 44,420.00 USD | 610.10 USD | 0.00 USD | `+12.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6955` | 44,520.00 USD | 101.38 USD | 0.00 USD | `+12.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6965` | 45,310.00 USD | 789.18 USD | 0.00 USD | `+12.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6985` | 45,410.00 USD | 102.99 USD | 0.00 USD | `+12.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7005` | 45,520.00 USD | 111.08 USD | 0.00 USD | `+13.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7015` | 46,220.00 USD | 694.49 USD | 0.00 USD | `+13.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7095` | 46,350.00 USD | 132.99 USD | 0.00 USD | `+14.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7115` | 46,470.00 USD | 122.04 USD | 0.00 USD | `+14.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7165` | 48,310.00 USD | 1,830.00 USD | 0.00 USD | `+15.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7195` | 48,490.00 USD | 183.26 USD | 0.00 USD | `+16.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7205` | 48,640.00 USD | 147.15 USD | 0.00 USD | `+16.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7265` | 54,930.00 USD | 6,290.00 USD | 0.00 USD | `+17.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7275` | 55,240.00 USD | 309.91 USD | 0.00 USD | `+17.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7325` | 55,400.00 USD | 165.17 USD | 0.00 USD | `+18.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7345` | 56,430.00 USD | 1,030.00 USD | 0.00 USD | `+18.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7405` | 57,160.00 USD | 733.09 USD | 0.00 USD | `+19.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7415` | 57,320.00 USD | 156.98 USD | 0.00 USD | `+19.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7445` | 57,510.00 USD | 185.43 USD | 0.00 USD | `+20.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7455` | 59,670.00 USD | 2,170.00 USD | 0.00 USD | `+20.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7475` | 59,990.00 USD | 318.43 USD | 0.00 USD | `+20.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7505` | 60,130.00 USD | 141.39 USD | 0.00 USD | `+21.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7565` | 64,250.00 USD | 4,120.00 USD | 0.00 USD | `+22.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7575` | 64,760.00 USD | 511.82 USD | 0.00 USD | `+22.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7615` | 65,640.00 USD | 875.23 USD | 0.00 USD | `+22.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7635` | 65,740.00 USD | 103.35 USD | 0.00 USD | `+23.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7665` | 65,870.00 USD | 127.48 USD | 0.00 USD | `+23.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7675` | 65,970.00 USD | 101.61 USD | 0.00 USD | `+23.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7695` | 66,160.00 USD | 186.97 USD | 0.00 USD | `+24.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7705` | 66,260.00 USD | 109.43 USD | 0.00 USD | `+24.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7775` | 66,430.00 USD | 166.70 USD | 0.00 USD | `+25.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7815` | 67,570.00 USD | 1,140.00 USD | 0.00 USD | `+26.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7865` | 73,880.00 USD | 6,310.00 USD | 0.00 USD | `+26.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8125` | 85,950.00 USD | 12,070.00 USD | 0.00 USD | `+31.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8265` | 87,610.00 USD | 1,650.00 USD | 0.00 USD | `+33.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8335` | 88,540.00 USD | 929.08 USD | 0.00 USD | `+34.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8475` | 129,130.00 USD | 40,590.00 USD | 0.00 USD | `+36.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8505` | 145,860.00 USD | 16,740.00 USD | 0.00 USD | `+37.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8515` | 158,590.00 USD | 12,720.00 USD | 0.00 USD | `+37.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8525` | 170,370.00 USD | 11,780.00 USD | 0.00 USD | `+37.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8725` | 170,530.00 USD | 159.86 USD | 0.00 USD | `+40.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 171,230.00 USD | 702.20 USD | 0.00 USD | `+45.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 171,420.00 USD | 193.62 USD | 0.00 USD | `+46.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 171,850.00 USD | 424.63 USD | 0.00 USD | `+51.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 174,640.00 USD | 2,790.00 USD | 0.00 USD | `+51.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 174,980.00 USD | 340.54 USD | 0.00 USD | `+53.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 175,090.00 USD | 108.83 USD | 0.00 USD | `+55.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 175,230.00 USD | 145.72 USD | 0.00 USD | `+56.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 177,270.00 USD | 2,030.00 USD | 0.00 USD | `+59.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 177,400.00 USD | 136.10 USD | 0.00 USD | `+61.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 177,950.00 USD | 550.48 USD | 0.00 USD | `+61.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 178,270.00 USD | 314.99 USD | 0.00 USD | `+65.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 178,870.00 USD | 602.17 USD | 0.00 USD | `+69.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 179,230.00 USD | 360.61 USD | 0.00 USD | `+71.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 180,170.00 USD | 942.77 USD | 0.00 USD | `+74.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 180,570.00 USD | 397.19 USD | 0.00 USD | `+77.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 181,090.00 USD | 525.37 USD | 0.00 USD | `+98.43%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.5230` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 32.85 USD |
| `7D` | `0.5270` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 10,890.00 USD | 0.00 USD | 5,570.00 USD |
| `7D` | `0.5290` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 2,560.00 USD | 0.00 USD | 2,270.00 USD |
| `7D` | `0.5310` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 11,240.00 USD | 0.00 USD | 6,810.00 USD |
| `7D` | `0.5330` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 6,080.00 USD |
| `7D` | `0.5350` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 2,440.00 USD | 3,040.00 USD | 0.00 USD |
| `7D` | `0.5370` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 0.00 USD | 1,550.00 USD | 2,940.00 USD |
| `7D` | `0.5390` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 57.67 USD |
| `7D` | `0.5410` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 8,600.00 USD | 2,920.00 USD | 36.17 USD |
| `7D` | `0.5430` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 7,660.00 USD | 1,910.00 USD | 7,760.00 USD |
| `7D` | `0.5450` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 2,250.00 USD | 523.59 USD | 10,760.00 USD |
| `7D` | `0.5470` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 3,830.00 USD | 3,210.00 USD |
| `7D` | `0.5490` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 4,100.00 USD | 474.54 USD | 6,610.00 USD |
| `1D` | `0.5510` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 2,750.00 USD | 0.00 USD | 1,920.00 USD |
| `7D` | `0.5510` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 5,620.00 USD | 2,890.00 USD | 6,470.00 USD |
| `1D` | `0.5520` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 0.00 USD | 1,050.00 USD | 0.00 USD |
| `1D` | `0.5530` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 1,260.00 USD | 1,410.00 USD | 0.00 USD |
| `7D` | `0.5530` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 4,030.00 USD | 1,150.00 USD | 12,810.00 USD |
| `1D` | `0.5540` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 5,390.00 USD | 5,750.00 USD | 4,170.00 USD |
| `1D` | `0.5550` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 2,940.00 USD | 0.00 USD | 1,640.00 USD |
| `7D` | `0.5550` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 18,260.00 USD | 8,030.00 USD | 11,100.00 USD |
| `1D` | `0.5560` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 1,680.00 USD | 686.25 USD | 0.00 USD |
| `1D` | `0.5570` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 2,710.00 USD | 2,460.00 USD | 4,420.00 USD |
| `7D` | `0.5570` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 6,420.00 USD | 812.74 USD | 8,360.00 USD |
| `1D` | `0.5580` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 0.00 USD | 2,820.00 USD | 2,530.00 USD |
| `1D` | `0.5590` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 1,670.00 USD | 1,870.00 USD | 1,370.00 USD |
| `7D` | `0.5590` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 8,660.00 USD | 13,230.00 USD | 17,560.00 USD |
| `1D` | `0.5600` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 0.00 USD | 1,690.00 USD | 3,830.00 USD |
| `1D` | `0.5610` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 823.46 USD |
| `7D` | `0.5610` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 8,030.00 USD | 2,900.00 USD | 7,930.00 USD |
| `1D` | `0.5620` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 0.00 USD | 776.64 USD | 2,180.00 USD |
| `1D` | `0.5630` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 2,260.00 USD | 1,560.00 USD | 6,880.00 USD |
| `7D` | `0.5630` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 15,810.00 USD | 7,840.00 USD | 6,580.00 USD |
| `1D` | `0.5640` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 4,020.00 USD | 3,380.00 USD | 10,730.00 USD |
| `7D` | `0.5650` | 977,760.00 USD | 0.00 USD | 977,760.00 USD | 0.00 USD | 1,210.00 USD | 2,270.00 USD |
| `1D` | `0.5660` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 3,580.00 USD |
| `7D` | `0.5670` | 974,280.00 USD | 0.00 USD | 974,280.00 USD | 11,490.00 USD | 1,780.00 USD | 5,130.00 USD |
| `1D` | `0.5690` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 5,100.00 USD |
| `7D` | `0.5690` | 955,880.00 USD | 0.00 USD | 955,880.00 USD | 5,100.00 USD | 0.00 USD | 137.49 USD |
| `1D` | `0.5700` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD |
| `1D` | `0.5710` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 0.00 USD | 2,350.00 USD | 0.00 USD |
| `7D` | `0.5710` | 950,640.00 USD | 0.00 USD | 950,640.00 USD | 1,030.00 USD | 3,310.00 USD | 2,430.00 USD |
| `1D` | `0.5720` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 0.00 USD | 832.92 USD | 0.00 USD |
| `1D` | `0.5730` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD |
| `7D` | `0.5730` | 943,870.00 USD | 0.00 USD | 943,870.00 USD | 2,690.00 USD | 2,050.00 USD | 10,780.00 USD |
| `1D` | `0.5740` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | 839.21 USD | 3,930.00 USD |
| `1D` | `0.5750` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 4,330.00 USD | 840.09 USD | 20,140.00 USD |
| `7D` | `0.5750` | 928,360.00 USD | 0.00 USD | 928,360.00 USD | 18,940.00 USD | 574.82 USD | 1,580.00 USD |
| `1D` | `0.5760` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 15,020.00 USD | 2,220.00 USD | 2,100.00 USD |
| `1D` | `0.5770` | 985,640.00 USD | 0.00 USD | 985,640.00 USD | 16,730.00 USD | 3,970.00 USD | 279.20 USD |
| `7D` | `0.5770` | 907,270.00 USD | 0.00 USD | 907,270.00 USD | 23,670.00 USD | 7,300.00 USD | 106.15 USD |
| `1D` | `0.5780` | 964,660.00 USD | 0.00 USD | 964,660.00 USD | 3,070.00 USD | 1,330.00 USD | 10,910.00 USD |
| `1D` | `0.5790` | 949,360.00 USD | 0.00 USD | 949,360.00 USD | 11,420.00 USD | 2,690.00 USD | 7,750.00 USD |
| `7D` | `0.5790` | 876,190.00 USD | 0.00 USD | 876,190.00 USD | 21,020.00 USD | 0.00 USD | 12,740.00 USD |
| `1D` | `0.5800` | 927,500.00 USD | 0.00 USD | 927,500.00 USD | 3,310.00 USD | 2,750.00 USD | 1,590.00 USD |
| `1D` | `0.5810` | 919,850.00 USD | 0.00 USD | 919,850.00 USD | 0.00 USD | 3,190.00 USD | 16,650.00 USD |
| `7D` | `0.5810` | 842,430.00 USD | 0.00 USD | 842,430.00 USD | 0.00 USD | 3,900.00 USD | 19,920.00 USD |
| `1D` | `0.5820` | 900,020.00 USD | 0.00 USD | 900,020.00 USD | 2,580.00 USD | 4,510.00 USD | 4,180.00 USD |
| `1D` | `0.5830` | 888,740.00 USD | 0.00 USD | 888,740.00 USD | 4,910.00 USD | 819.33 USD | 0.00 USD |
| `7D` | `0.5830` | 818,600.00 USD | 0.00 USD | 818,600.00 USD | 0.00 USD | 0.00 USD | 3,560.00 USD |
| `1D` | `0.5840` | 883,010.00 USD | 0.00 USD | 883,010.00 USD | 0.00 USD | 2,190.00 USD | 4,280.00 USD |
| `1D` | `0.5850` | 876,540.00 USD | 0.00 USD | 876,540.00 USD | 2,950.00 USD | 0.00 USD | 30,860.00 USD |
| `7D` | `0.5850` | 815,030.00 USD | 0.00 USD | 815,030.00 USD | 0.00 USD | 0.00 USD | 21,300.00 USD |
| `1D` | `0.5860` | 842,730.00 USD | 0.00 USD | 842,730.00 USD | 2,810.00 USD | 3,110.00 USD | 7,880.00 USD |
| `1D` | `0.5870` | 828,930.00 USD | 0.00 USD | 828,930.00 USD | 15,080.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.5870` | 793,740.00 USD | 0.00 USD | 793,740.00 USD | 0.00 USD | 1,400.00 USD | 0.00 USD |
| `1D` | `0.5880` | 811,540.00 USD | 0.00 USD | 811,540.00 USD | 34,650.00 USD | 10,250.00 USD | 7,790.00 USD |
| `1D` | `0.5890` | 758,850.00 USD | 0.00 USD | 758,850.00 USD | 38,270.00 USD | 11,450.00 USD | 7.65 USD |
| `7D` | `0.5890` | 792,340.00 USD | 0.00 USD | 792,340.00 USD | 46,140.00 USD | 14,610.00 USD | 228.75 USD |
| `1D` | `0.5900` | 709,120.00 USD | 0.00 USD | 709,120.00 USD | 29,060.00 USD | 13,050.00 USD | 10,140.00 USD |
| `1D` | `0.5910` | 656,870.00 USD | 0.00 USD | 656,870.00 USD | 26,100.00 USD | 13,220.00 USD | 18,030.00 USD |
| `7D` | `0.5910` | 731,360.00 USD | 0.00 USD | 731,360.00 USD | 61,220.00 USD | 10,900.00 USD | 16,520.00 USD |
| `1D` | `0.5920` | 599,520.00 USD | 0.00 USD | 599,520.00 USD | 25,960.00 USD | 6,190.00 USD | 7,110.00 USD |
| `1D` | `0.5930` | 560,260.00 USD | 0.00 USD | 560,260.00 USD | 6,060.00 USD | 6,380.00 USD | 12,950.00 USD |
| `7D` | `0.5930` | 642,730.00 USD | 0.00 USD | 642,730.00 USD | 21,790.00 USD | 10,620.00 USD | 59,150.00 USD |
| `1D` | `0.5940` | 534,870.00 USD | 0.00 USD | 534,870.00 USD | 17,830.00 USD | 2,040.00 USD | 8,400.00 USD |
| `1D` | `0.5950` | 506,600.00 USD | 0.00 USD | 506,600.00 USD | 28,480.00 USD | 3,220.00 USD | 70.10 USD |
| `7D` | `0.5950` | 551,170.00 USD | 0.00 USD | 551,170.00 USD | 13,060.00 USD | 0.00 USD | 46.83 USD |
| `1D` | `0.5960` | 474,820.00 USD | 0.00 USD | 474,820.00 USD | 12,010.00 USD | 1,860.00 USD | 8,580.00 USD |
| `1D` | `0.5970` | 452,380.00 USD | 0.00 USD | 452,380.00 USD | 13,040.00 USD | 0.00 USD | 5,180.00 USD |
| `7D` | `0.5970` | 538,060.00 USD | 0.00 USD | 538,060.00 USD | 5,120.00 USD | 18,410.00 USD | 0.00 USD |
| `1D` | `0.5980` | 434,160.00 USD | 0.00 USD | 434,160.00 USD | 10,410.00 USD | 2,390.00 USD | 62.20 USD |
| `1D` | `0.5990` | 421,300.00 USD | 0.00 USD | 421,300.00 USD | 0.00 USD | 836.21 USD | 1,100.00 USD |
| `7D` | `0.5990` | 514,540.00 USD | 0.00 USD | 514,540.00 USD | 23,710.00 USD | 0.00 USD | 55.70 USD |
| `1D` | `0.6000` | 419,360.00 USD | 0.00 USD | 419,360.00 USD | 2,680.00 USD | 2,480.00 USD | 7,880.00 USD |
| `1D` | `0.6010` | 406,320.00 USD | 0.00 USD | 406,320.00 USD | 2,960.00 USD | 6,370.00 USD | 5,020.00 USD |
| `7D` | `0.6010` | 490,770.00 USD | 0.00 USD | 490,770.00 USD | 0.00 USD | 4,090.00 USD | 12,000.00 USD |
| `1D` | `0.6020` | 391,960.00 USD | 0.00 USD | 391,960.00 USD | 2,680.00 USD | 7,430.00 USD | 1,720.00 USD |
| `1D` | `0.6030` | 380,130.00 USD | 0.00 USD | 380,130.00 USD | 34,080.00 USD | 14,050.00 USD | 3,630.00 USD |
| `7D` | `0.6030` | 474,690.00 USD | 0.00 USD | 474,690.00 USD | 38,530.00 USD | 8,040.00 USD | 284.07 USD |
| `1D` | `0.6040` | 328,360.00 USD | 0.00 USD | 328,360.00 USD | 6,530.00 USD | 9,900.00 USD | 5,000.00 USD |
| `1D` | `0.6050` | 306,930.00 USD | 0.00 USD | 306,930.00 USD | 20,690.00 USD | 1,370.00 USD | 7,950.00 USD |
| `7D` | `0.6050` | 427,830.00 USD | 0.00 USD | 427,830.00 USD | 0.00 USD | 18,680.00 USD | 20,810.00 USD |
| `1D` | `0.6060` | 276,930.00 USD | 0.00 USD | 276,930.00 USD | 8,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6070` | 268,520.00 USD | 0.00 USD | 268,520.00 USD | 13,570.00 USD | 4,080.00 USD | 0.00 USD |
| `7D` | `0.6070` | 388,340.00 USD | 0.00 USD | 388,340.00 USD | 0.00 USD | 0.00 USD | 203.50 USD |
| `1D` | `0.6080` | 250,880.00 USD | 0.00 USD | 250,880.00 USD | 7,170.00 USD | 3,170.00 USD | 0.00 USD |
| `1D` | `0.6090` | 240,540.00 USD | 0.00 USD | 240,540.00 USD | 8,370.00 USD | 1,620.00 USD | 0.00 USD |
| `7D` | `0.6090` | 388,140.00 USD | 0.00 USD | 388,140.00 USD | 16,780.00 USD | 44,860.00 USD | 55,560.00 USD |
| `1D` | `0.6100` | 230,550.00 USD | 0.00 USD | 230,550.00 USD | 0.00 USD | 0.00 USD | 41,540.00 USD |
| `1D` | `0.6110` | 189,000.00 USD | 0.00 USD | 189,000.00 USD | 12,430.00 USD | 3,380.00 USD | 0.00 USD |
| `7D` | `0.6110` | 270,930.00 USD | 0.00 USD | 270,930.00 USD | 7,480.00 USD | 4,780.00 USD | 12,860.00 USD |
| `1D` | `0.6120` | 173,190.00 USD | 0.00 USD | 173,190.00 USD | 30,040.00 USD | 1,670.00 USD | 2,170.00 USD |
| `1D` | `0.6130` | 139,310.00 USD | 0.00 USD | 139,310.00 USD | 44,750.00 USD | 4,950.00 USD | 34,140.00 USD |
| `7D` | `0.6130` | 245,810.00 USD | 0.00 USD | 245,810.00 USD | 85,290.00 USD | 27,340.00 USD | 24,220.00 USD |
| `1D` | `0.6140` | 55,450.00 USD | 0.00 USD | 55,450.00 USD | 6,130.00 USD | 8,290.00 USD | 19,180.00 USD |
| `7D` | `0.6150` | 108,970.00 USD | 0.00 USD | 108,970.00 USD | 0.00 USD | 6,170.00 USD | 16,700.00 USD |
| `1D` | `0.6160` | 21,850.00 USD | 0.00 USD | 21,850.00 USD | 0.00 USD | 0.00 USD | 3,130.00 USD |
| `7D` | `0.6170` | 86,090.00 USD | 0.00 USD | 86,090.00 USD | 0.00 USD | 0.00 USD | 283.86 USD |
| `1D` | `0.6180` | 18,720.00 USD | 0.00 USD | 18,720.00 USD | 0.00 USD | 1,760.00 USD | 8,360.00 USD |
| `7D` | `0.6190` | 85,810.00 USD | 0.00 USD | 85,810.00 USD | 15,010.00 USD | 0.00 USD | 155.14 USD |
| `1D` | `0.6200` | 8,600.00 USD | 0.00 USD | 8,600.00 USD | 0.00 USD | 0.00 USD | 8,600.00 USD |
| `1D` | `0.6210` | 16,860.00 USD | 16,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,860.00 USD |
| `1D` | `0.6210` | 33,730.00 USD | 33,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,860.00 USD |
| `7D` | `0.6210` | 70,640.00 USD | 0.00 USD | 70,640.00 USD | 18,630.00 USD | 22,640.00 USD | 29,370.00 USD |
| `1D` | `0.6220` | 36,110.00 USD | 36,110.00 USD | 0.00 USD | 0.00 USD | 2,380.00 USD | 0.00 USD |
| `7D` | `0.6220` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6230` | 270.47 USD | 270.47 USD | 0.00 USD | 0.00 USD | 0.00 USD | 270.47 USD |
| `1D` | `0.6240` | 57,820.00 USD | 57,820.00 USD | 0.00 USD | 21,710.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6250` | 74,560.00 USD | 74,560.00 USD | 0.00 USD | 16,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6250` | 96,400.00 USD | 96,400.00 USD | 0.00 USD | 88,830.00 USD | 7,300.00 USD | 0.00 USD |
| `1D` | `0.6260` | 82,930.00 USD | 82,930.00 USD | 0.00 USD | 0.00 USD | 8,370.00 USD | 0.00 USD |
| `1D` | `0.6270` | 130,760.00 USD | 130,760.00 USD | 0.00 USD | 47,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6270` | 162,620.00 USD | 162,620.00 USD | 0.00 USD | 57,950.00 USD | 0.00 USD | 8,270.00 USD |
| `1D` | `0.6280` | 179,840.00 USD | 179,840.00 USD | 0.00 USD | 9,840.00 USD | 16,420.00 USD | 22,820.00 USD |
| `1D` | `0.6290` | 221,530.00 USD | 221,530.00 USD | 0.00 USD | 20,690.00 USD | 6,580.00 USD | 14,420.00 USD |
| `7D` | `0.6290` | 251,590.00 USD | 251,590.00 USD | 0.00 USD | 0.00 USD | 22,580.00 USD | 66,380.00 USD |
| `1D` | `0.6300` | 245,180.00 USD | 245,180.00 USD | 0.00 USD | 10,980.00 USD | 3,430.00 USD | 9,240.00 USD |
| `1D` | `0.6310` | 303,770.00 USD | 303,770.00 USD | 0.00 USD | 28,020.00 USD | 8,860.00 USD | 21,710.00 USD |
| `7D` | `0.6310` | 251,700.00 USD | 251,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 112.68 USD |
| `1D` | `0.6320` | 358,500.00 USD | 358,500.00 USD | 0.00 USD | 37,640.00 USD | 6,080.00 USD | 11,010.00 USD |
| `1D` | `0.6330` | 410,620.00 USD | 410,620.00 USD | 0.00 USD | 22,870.00 USD | 10,960.00 USD | 18,300.00 USD |
| `7D` | `0.6330` | 309,640.00 USD | 309,640.00 USD | 0.00 USD | 57,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6340` | 484,220.00 USD | 484,220.00 USD | 0.00 USD | 29,640.00 USD | 3,190.00 USD | 40,770.00 USD |
| `1D` | `0.6350` | 531,610.00 USD | 531,610.00 USD | 0.00 USD | 39,480.00 USD | 1,700.00 USD | 6,210.00 USD |
| `7D` | `0.6350` | 354,890.00 USD | 354,890.00 USD | 0.00 USD | 45,040.00 USD | 0.00 USD | 213.86 USD |
| `1D` | `0.6360` | 650,270.00 USD | 650,270.00 USD | 0.00 USD | 54,130.00 USD | 4,140.00 USD | 60,390.00 USD |
| `1D` | `0.6370` | 682,420.00 USD | 682,420.00 USD | 0.00 USD | 0.00 USD | 5,010.00 USD | 27,150.00 USD |
| `7D` | `0.6370` | 421,160.00 USD | 421,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 66,260.00 USD |
| `1D` | `0.6380` | 728,080.00 USD | 728,080.00 USD | 0.00 USD | 5,370.00 USD | 28,210.00 USD | 12,070.00 USD |
| `1D` | `0.6390` | 811,870.00 USD | 811,870.00 USD | 0.00 USD | 26,050.00 USD | 7,210.00 USD | 50,540.00 USD |
| `7D` | `0.6390` | 494,820.00 USD | 494,820.00 USD | 0.00 USD | 0.00 USD | 15,680.00 USD | 57,980.00 USD |
| `1D` | `0.6400` | 964,460.00 USD | 964,460.00 USD | 0.00 USD | 72,890.00 USD | 43,770.00 USD | 35,930.00 USD |
| `1D` | `0.6410` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 35,660.00 USD | 14,660.00 USD | 14,480.00 USD |
| `7D` | `0.6410` | 539,290.00 USD | 539,290.00 USD | 0.00 USD | 19,270.00 USD | 18,210.00 USD | 7,000.00 USD |
| `1D` | `0.6420` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 71,960.00 USD | 11,610.00 USD | 12,130.00 USD |
| `1D` | `0.6430` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 36,780.00 USD | 13,280.00 USD | 23,760.00 USD |
| `7D` | `0.6430` | 676,950.00 USD | 676,950.00 USD | 0.00 USD | 71,550.00 USD | 33,700.00 USD | 32,400.00 USD |
| `1D` | `0.6440` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 33,760.00 USD | 19,310.00 USD | 48,490.00 USD |
| `1D` | `0.6450` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 63,120.00 USD | 12,700.00 USD | 35,590.00 USD |
| `7D` | `0.6450` | 870,720.00 USD | 870,720.00 USD | 0.00 USD | 109,710.00 USD | 33,240.00 USD | 50,830.00 USD |
| `1D` | `0.6460` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 47,150.00 USD | 12,100.00 USD | 9,690.00 USD |
| `1D` | `0.6470` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 59,430.00 USD | 17,210.00 USD | 11,970.00 USD |
| `7D` | `0.6470` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 101,050.00 USD | 57,590.00 USD | 112,010.00 USD |
| `1D` | `0.6480` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 70,780.00 USD | 7,630.00 USD | 373.19 USD |
| `1D` | `0.6490` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 63,670.00 USD | 2,070.00 USD | 12,200.00 USD |
| `7D` | `0.6490` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 113,110.00 USD | 0.00 USD | 41,530.00 USD |
| `1D` | `0.6500` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 44,490.00 USD | 8,390.00 USD | 3,010.00 USD |
| `1D` | `0.6510` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 58,460.00 USD | 0.00 USD | 14,330.00 USD |
| `7D` | `0.6510` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 269,580.00 USD | 8,270.00 USD | 140,660.00 USD |
| `1D` | `0.6520` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 93,550.00 USD | 13,180.00 USD | 5,780.00 USD |
| `1D` | `0.6530` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 11,510.00 USD | 3,910.00 USD | 11.74 USD |
| `7D` | `0.6530` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 65,690.00 USD | 11,160.00 USD | 133,730.00 USD |
| `1D` | `0.6540` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 24,280.00 USD | 0.00 USD | 10,560.00 USD |
| `1D` | `0.6550` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,950.00 USD |
| `7D` | `0.6550` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 15,730.00 USD | 0.00 USD | 15,040.00 USD |
| `1D` | `0.6560` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD |
| `1D` | `0.6570` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,420.00 USD |
| `7D` | `0.6570` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 11,730.00 USD | 899.30 USD |
| `1D` | `0.6580` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 3,310.00 USD | 34.49 USD |
| `1D` | `0.6590` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 5,890.00 USD | 164.02 USD |
| `7D` | `0.6590` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 33,250.00 USD | 9,780.00 USD |
| `1D` | `0.6600` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 6,010.00 USD | 9,280.00 USD | 59.63 USD |
| `1D` | `0.6610` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 6,690.00 USD | 835.70 USD | 142.10 USD |
| `7D` | `0.6610` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 8,600.00 USD | 7,100.00 USD | 957.97 USD |
| `1D` | `0.6620` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 530.84 USD | 7,710.00 USD |
| `1D` | `0.6630` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 2,590.00 USD | 0.00 USD | 2,310.00 USD |
| `7D` | `0.6630` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 889.52 USD |
| `1D` | `0.6640` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 11,190.00 USD | 837.01 USD | 135.08 USD |
| `1D` | `0.6650` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 3,160.00 USD | 17,420.00 USD |
| `7D` | `0.6650` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 33,660.00 USD | 6,770.00 USD | 6,990.00 USD |
| `1D` | `0.6660` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 839.67 USD | 7,590.00 USD |
| `1D` | `0.6670` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 18,850.00 USD | 0.00 USD | 24.36 USD |
| `7D` | `0.6670` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 880.88 USD |
| `1D` | `0.6680` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 138.15 USD |
| `1D` | `0.6690` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 3,550.00 USD | 5,500.00 USD |
| `7D` | `0.6690` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 960.81 USD |
| `1D` | `0.6700` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 8,830.00 USD | 1,920.00 USD | 24,760.00 USD |
| `1D` | `0.6710` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 41,970.00 USD | 0.00 USD | 5,960.00 USD |
| `7D` | `0.6710` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 58,470.00 USD | 0.00 USD | 30,360.00 USD |
| `1D` | `0.6720` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 1,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6730` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 25,660.00 USD | 3,670.00 USD | 5,560.00 USD |
| `7D` | `0.6730` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 131.11 USD |
| `1D` | `0.6740` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 64,370.00 USD | 8,170.00 USD | 9,210.00 USD |
| `1D` | `0.6750` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 28,700.00 USD | 4,630.00 USD | 12,070.00 USD |
| `7D` | `0.6750` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 39,730.00 USD | 75,730.00 USD | 226.45 USD |
| `1D` | `0.6760` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD |
| `1D` | `0.6770` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 19,930.00 USD | 8,320.00 USD | 15,020.00 USD |
| `7D` | `0.6770` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 63,600.00 USD | 6,430.00 USD | 51,170.00 USD |
| `1D` | `0.6780` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 33,610.00 USD | 13,860.00 USD | 12,140.00 USD |
| `1D` | `0.6790` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 2,940.00 USD | 18,610.00 USD | 12,520.00 USD |
| `7D` | `0.6790` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 29,210.00 USD | 4,230.00 USD |
| `1D` | `0.6800` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 1,680.00 USD | 686.25 USD | 2,450.00 USD |
| `1D` | `0.6810` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 2,710.00 USD | 2,460.00 USD | 11,970.00 USD |
| `7D` | `0.6810` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 15,720.00 USD | 0.00 USD |
| `1D` | `0.6820` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 22,600.00 USD | 16,590.00 USD | 9,030.00 USD |
| `1D` | `0.6830` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 26,250.00 USD | 17,300.00 USD | 36,820.00 USD |
| `7D` | `0.6830` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 32,570.00 USD | 55,460.00 USD | 48,330.00 USD |
| `1D` | `0.6840` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 45,780.00 USD | 17,210.00 USD | 15,180.00 USD |
| `1D` | `0.6850` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 39,200.00 USD | 5,780.00 USD | 24,130.00 USD |
| `7D` | `0.6850` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 75,160.00 USD | 41,290.00 USD | 64,650.00 USD |
| `1D` | `0.6860` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 40,250.00 USD | 4,380.00 USD | 14,780.00 USD |
| `1D` | `0.6870` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 63,220.00 USD | 1,160.00 USD | 3,830.00 USD |
| `7D` | `0.6870` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 52,530.00 USD | 9,830.00 USD | 131.40 USD |
| `1D` | `0.6880` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 15,430.00 USD | 11,160.00 USD | 26,530.00 USD |
| `1D` | `0.6890` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 1,180.00 USD | 0.00 USD | 8,460.00 USD |
| `7D` | `0.6890` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 18,170.00 USD | 29,960.00 USD | 2,900.00 USD |
| `1D` | `0.6900` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 18,600.00 USD | 4,990.00 USD | 21,750.00 USD |
| `1D` | `0.6910` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 28,860.00 USD | 1,730.00 USD | 32,320.00 USD |
| `7D` | `0.6910` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 69,620.00 USD | 6,570.00 USD | 54,070.00 USD |
| `1D` | `0.6920` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 16,800.00 USD | 0.00 USD | 13,660.00 USD |
| `1D` | `0.6930` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 10,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6930` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 14,220.00 USD | 0.00 USD | 66,830.00 USD |
| `7D` | `0.6950` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 31,450.00 USD | 0.00 USD | 12,530.00 USD |
| `7D` | `0.6970` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 50,160.00 USD | 6,030.00 USD | 0.00 USD |
| `7D` | `0.6990` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 27,730.00 USD | 10,960.00 USD | 30,360.00 USD |
| `7D` | `0.7010` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 16,330.00 USD | 0.00 USD | 10,140.00 USD |
| `7D` | `0.7030` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 106,430.00 USD | 0.00 USD | 103,540.00 USD |
| `7D` | `0.7050` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 46,540.00 USD | 0.00 USD | 169,430.00 USD |
| `7D` | `0.7070` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 28,920.00 USD | 69,790.00 USD | 83,530.00 USD |
| `7D` | `0.7090` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 121,730.00 USD | 61,400.00 USD | 188,340.00 USD |
| `7D` | `0.7110` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 85,130.00 USD | 64,110.00 USD | 106,920.00 USD |
| `7D` | `0.7130` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 135,980.00 USD | 77,290.00 USD | 186,620.00 USD |
| `7D` | `0.7150` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 177,760.00 USD | 62,090.00 USD | 178,590.00 USD |
| `7D` | `0.7170` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 168,460.00 USD | 74,260.00 USD | 121,810.00 USD |
| `7D` | `0.7190` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 88,650.00 USD | 32,980.00 USD | 100,810.00 USD |
| `7D` | `0.7210` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 271,310.00 USD | 58,030.00 USD | 161,320.00 USD |
| `7D` | `0.7230` | 6,770,000.00 USD | 6,770,000.00 USD | 0.00 USD | 171,240.00 USD | 52,810.00 USD | 121,410.00 USD |
| `7D` | `0.7250` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 139,330.00 USD | 40,040.00 USD | 117,790.00 USD |
| `7D` | `0.7270` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 111,330.00 USD | 44,700.00 USD | 127,100.00 USD |
| `7D` | `0.7290` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 89,770.00 USD | 54,440.00 USD | 126,930.00 USD |
| `7D` | `0.7310` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 183,580.00 USD | 68,560.00 USD | 64,380.00 USD |
| `7D` | `0.7330` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 74,380.00 USD | 25,020.00 USD | 75,020.00 USD |
| `7D` | `0.7350` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 97,650.00 USD | 24,440.00 USD | 46,040.00 USD |
| `7D` | `0.7370` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 46,860.00 USD | 30,720.00 USD | 40,630.00 USD |
| `7D` | `0.7390` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 64,070.00 USD | 15,140.00 USD | 40,070.00 USD |
| `7D` | `0.7410` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 30,110.00 USD | 27,200.00 USD | 42,650.00 USD |
| `7D` | `0.7430` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 53,760.00 USD | 23,580.00 USD | 55,250.00 USD |
| `7D` | `0.7440` | 8,780,000.00 USD | 8,780,000.00 USD | 0.00 USD | 28,120.00 USD | 0.00 USD | 329.40 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `86.94M` | Total OI Tokens: `140,146,578.8 APT`
  * 1h OI Change: `-0.57%` | 4h OI Change: `+2.08%` | 24h OI Change: `-9.49%`
  * Exchange Breakdown: Binance=`15.52M` | Bybit=`17.27M` | OKX=`4.10M` | Hyperliquid=`3.43M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-4.21K` | Last 24h: `2.90K` | Last 3d: `7.60K` | Last 7d: `2.85K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0138%` | **USDT OKX** | `-0.0171%` |
| **USDT Bybit** | `-0.0081%` | **USDT KuCoin** | `-0.0247%` |
| **USDT MEXC** | `-0.0140%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0190%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `APT` | `45.11%` | `54.89%` | `0.82` | 2,970,000.00 USD |
| `15M` | `Binance` | `32.51%` | `67.49%` | `0.48` | 783,510.00 USD |
| `15M` | `OKX` | `42.1%` | `57.9%` | `0.73` | 875,890.00 USD |
| `15M` | `Bybit` | `69.26%` | `30.74%` | `2.25` | 451,420.00 USD |
| `15M` | `KuCoin` | `46.67%` | `53.33%` | `0.88` | 110,460.00 USD |
| `15M` | `Gate` | `68.35%` | `31.65%` | `2.16` | 74,120.00 USD |
| `15M` | `Bitget` | `44.18%` | `55.82%` | `0.79` | 23,320.00 USD |
| `15M` | `BingX` | `39.56%` | `60.44%` | `0.65` | 34,660.00 USD |
| `15M` | `MEXC` | `31.45%` | `68.55%` | `0.46` | 144,680.00 USD |
| `15M` | `Bitunix` | `81.83%` | `18.17%` | `4.50` | 98,310.00 USD |
| `15M` | `Hyperliquid` | `71.09%` | `28.91%` | `2.46` | 5,950.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.02%` | `49.98%` | `1.00` | 299,740.00 USD |
| `15M` | `Crypto.com` | `50.26%` | `49.74%` | `1.01` | 5.68 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 73,110.00 USD |
| `15M` | `HTX` | `28.37%` | `71.63%` | `0.40` | 2,530.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `2.25%` | `97.75%` | `0.02` | 253.30 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 0.86 USD |
| `15M` | `Whale Positions` | `32.51%` | `67.49%` | `0.48` | 783,510.00 USD |
| `15M` | `Global Accounts` | `45.11%` | `54.89%` | `0.82` | 2,970,000.00 USD |
| `1H` | `APT` | `49.35%` | `50.65%` | `0.97` | 10,800,000.00 USD |
| `1H` | `Binance` | `47.99%` | `52.01%` | `0.92` | 3,290,000.00 USD |
| `1H` | `OKX` | `38.32%` | `61.68%` | `0.62` | 1,540,000.00 USD |
| `1H` | `Bybit` | `55.35%` | `44.65%` | `1.24` | 1,270,000.00 USD |
| `1H` | `KuCoin` | `49.39%` | `50.61%` | `0.98` | 110,000.00 USD |
| `1H` | `Gate` | `44.16%` | `55.84%` | `0.79` | 1,120,000.00 USD |
| `1H` | `Bitget` | `65.25%` | `34.75%` | `1.88` | 368,080.00 USD |
| `1H` | `BingX` | `48.16%` | `51.84%` | `0.93` | 1,720,000.00 USD |
| `1H` | `MEXC` | `35.5%` | `64.5%` | `0.55` | 256,140.00 USD |
| `1H` | `Bitunix` | `41.27%` | `58.73%` | `0.70` | 266,190.00 USD |
| `1H` | `Hyperliquid` | `68.7%` | `31.3%` | `2.19` | 61,410.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.2%` | `49.8%` | `1.01` | 372,190.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `97.07%` | `2.93%` | `33.13` | 403,300.00 USD |
| `1H` | `HTX` | `81.21%` | `18.79%` | `4.32` | 15,100.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `47.45%` | `52.55%` | `0.90` | 824.43 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `82.94%` | `17.06%` | `4.86` | 9,220.00 USD |
| `1H` | `Whale Positions` | `47.99%` | `52.01%` | `0.92` | 3,290,000.00 USD |
| `1H` | `Global Accounts` | `49.35%` | `50.65%` | `0.97` | 10,800,000.00 USD |
| `4H` | `APT` | `48.18%` | `51.82%` | `0.93` | 52,440,000.00 USD |
| `4H` | `Binance` | `46.14%` | `53.86%` | `0.86` | 16,780,000.00 USD |
| `4H` | `OKX` | `45.13%` | `54.87%` | `0.82` | 6,840,000.00 USD |
| `4H` | `Bybit` | `53.53%` | `46.47%` | `1.15` | 4,460,000.00 USD |
| `4H` | `KuCoin` | `51.72%` | `48.28%` | `1.07` | 445,590.00 USD |
| `4H` | `Gate` | `47.69%` | `52.31%` | `0.91` | 4,820,000.00 USD |
| `4H` | `Bitget` | `59.63%` | `40.37%` | `1.48` | 1,860,000.00 USD |
| `4H` | `BingX` | `40.86%` | `59.14%` | `0.69` | 9,500,000.00 USD |
| `4H` | `MEXC` | `51.23%` | `48.77%` | `1.05` | 2,510,000.00 USD |
| `4H` | `Bitunix` | `47.27%` | `52.73%` | `0.90` | 1,580,000.00 USD |
| `4H` | `Hyperliquid` | `56.47%` | `43.53%` | `1.30` | 548,350.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.07%` | `49.93%` | `1.00` | 1,600,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `98.47%` | `1.53%` | `64.36` | 1,260,000.00 USD |
| `4H` | `HTX` | `54.74%` | `45.26%` | `1.21` | 109,400.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `24.1%` | `75.9%` | `0.32` | 3,980.00 USD |
| `4H` | `Aster` | `67.92%` | `32.08%` | `2.12` | 86,400.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `81.01%` | `18.99%` | `4.27` | 25,840.00 USD |
| `4H` | `Whale Positions` | `46.14%` | `53.86%` | `0.86` | 16,780,000.00 USD |
| `4H` | `Global Accounts` | `48.18%` | `51.82%` | `0.93` | 52,440,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.6161` | `0.6160` | `0.6161` | `0.6176` | `0.6147` | 319,675.12 USD | 174,523.38 USD | 145,151.74 USD | 29,371.64 USD | `+9.19%` | `4B / 6S` |
| `0:00 UTC` | `0.6151` | `0.6150` | `0.6151` | `0.6187` | `0.6118` | 468,512.46 USD | 237,013.59 USD | 231,498.87 USD | 5,514.73 USD | `+1.18%` | `14B / 9S` |
| `5:00 UTC` | `0.6179` | `0.6169` | `0.6179` | `0.6184` | `0.6149` | 312,659.38 USD | 170,069.09 USD | 142,590.29 USD | 27,478.79 USD | `+8.79%` | `4B / 2S` |
| `0:00 UTC` | `0.6169` | `0.6172` | `0.6169` | `0.6184` | `0.6159` | 332,795.97 USD | 159,318.96 USD | 173,477.01 USD | -14,158.04 USD | `-4.25%` | `4B / 4S` |
| `5:00 UTC` | `0.6199` | `0.6197` | `0.6199` | `0.6222` | `0.6170` | 660,978.35 USD | 238,264.86 USD | 422,713.49 USD | -184,448.63 USD | `-27.91%` | `8B / 10S` |
| `0:00 UTC` | `0.6210` | `0.6225` | `0.6210` | `0.6265` | `0.6192` | 529,221.91 USD | 223,718.81 USD | 305,503.09 USD | -81,784.28 USD | `-15.45%` | `7B / 16S` |
| `5:00 UTC` | `0.6250` | `0.6249` | `0.6250` | `0.6265` | `0.6227` | 233,847.44 USD | 95,835.18 USD | 138,012.26 USD | -42,177.08 USD | `-18.04%` | `7B / 7S` |
| `0:00 UTC` | `0.6256` | `0.6266` | `0.6256` | `0.6282` | `0.6250` | 249,222.56 USD | 96,254.76 USD | 152,967.81 USD | -56,713.05 USD | `-22.76%` | `4B / 10S` |
| `5:00 UTC` | `0.6249` | `0.6222` | `0.6249` | `0.6258` | `0.6190` | 531,684.34 USD | 301,525.47 USD | 230,158.87 USD | 71,366.59 USD | `+13.42%` | `17B / 21S` |
| `0:00 UTC` | `0.6200` | `0.6198` | `0.6200` | `0.6201` | `0.6193` | 8,523.05 USD | 4,835.33 USD | 3,687.71 USD | 1,147.62 USD | `+13.46%` | `1B / 5S` |

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
| `5m` | 22,060.00 USD | 41,520.00 USD | **`ACCUMULATION`** |
| `15m` | 26,600.00 USD | 10,940.00 USD | **`ACCUMULATION`** |
| `30m` | -69,490.00 USD | 31,860.00 USD | **`DISTRIBUTION`** |
| `1h` | -191,440.00 USD | -73,550.00 USD | **`DISTRIBUTION`** |
| `2h` | -234,130.00 USD | -366,030.00 USD | **`DISTRIBUTION`** |
| `4h` | -57,910.00 USD | 61,320.00 USD | **`ACCUMULATION`** |
| `6h` | -551,490.00 USD | -988,860.00 USD | **`DISTRIBUTION`** |
| `8h` | -950,880.00 USD | -1,410,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,360,000.00 USD | -5,450,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,290,000.00 USD | -8,800,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,990,000.00 USD | -26,320,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,650,000.00 USD | -106,290,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+22.06K` | 15m=`+26.60K` | 1h=`-191.44K` | 24h=`-1.29M`
* Futures Capital Netflows: 5m=`+41.52K` | 15m=`+10.94K` | 1h=`-73.55K` | 24h=`-8.80M`
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
  * `2026-10-30 11:03:56 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:28:56 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:29:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
