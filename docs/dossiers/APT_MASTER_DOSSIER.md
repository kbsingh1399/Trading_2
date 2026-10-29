# 🏛️ SOVEREIGN CANDIDATE DOSSIER: APT
**Canonical Key**: `APT` | **Broker Instrument**: `APTUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 04:50:10 IST` (`2026-10-29 23:20:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.6167` | `0.6194` | `0.6144` | `0.6185` | `368,840` | 227,488.19 USD | 4,183.22 USD | `+1.84%` | -6,750,004.80 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.6185` | `0.6226` | `0.6173` | `0.6210` | `267,519` | 165,827.69 USD | -23,897.56 USD | `-14.41%` | -6,773,902.37 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.6211` | `0.6214` | `0.6200` | `0.6205` | `50,074` | 31,086.79 USD | 8,661.79 USD | `+27.86%` | -6,765,240.58 USD | `+0.40` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.6260` | `0.6264` | `0.6193` | `0.6222` | `1,606,656` | 1,000,191.04 USD | 28,746.14 USD | `+2.87%` | -6,656,373.67 USD | `+0.38` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.6221` | `0.6226` | `0.6144` | `0.6210` | `1,218,885` | 753,276.60 USD | -114,424.33 USD | `-15.19%` | -6,770,798.00 USD | `+0.12` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.6211` | `0.6214` | `0.6200` | `0.6202` | `49,238` | 30,568.07 USD | 8,184.12 USD | `+26.77%` | -6,762,613.88 USD | `+0.31` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.6198` | `0.6411` | `0.6164` | `0.6226` | `11,690,306` | 7,362,985.80 USD | 19,097.99 USD | `+0.26%` | -6,473,256.48 USD | `+0.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.6227` | `0.6308` | `0.6136` | `0.6222` | `9,745,852` | 6,078,131.70 USD | -159,486.24 USD | `-2.62%` | -6,632,742.73 USD | `+0.16` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.6221` | `0.6226` | `0.6144` | `0.6202` | `1,268,123` | 783,844.67 USD | -106,240.21 USD | `-13.55%` | -6,738,982.94 USD | `+0.24` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -1,678,888.13 USD | `+0.66` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -3,147,816.26 USD | `-1.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6003` | `0.6208` | `54,528,185` | 34,437,878.46 USD | -3,590,344.23 USD | `-10.43%` | -6,738,160.49 USD | `-2.03` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6611` | `0.6759` | `0.6485` | `0.6561` | `10,656,422` | 7,044,804.33 USD | -366,898.68 USD | `-5.21%` | -1,470,659.97 USD | `+1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6561` | `0.6774` | `0.6549` | `0.6712` | `7,448,343` | 4,965,296.85 USD | -60,141.40 USD | `-1.21%` | -1,530,801.38 USD | `+1.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -1,678,888.13 USD | `+0.66` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -3,147,816.26 USD | `-1.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6003` | `0.6208` | `54,528,185` | 34,437,878.46 USD | -3,590,344.23 USD | `-10.43%` | -6,738,160.49 USD | `-2.03` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:46:31 IST` |

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
| `Live` | `Long Liquidation` | `0.1395` | 419.65 USD | 312,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 249.20 USD | 312,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 269.27 USD | 311,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 228.91 USD | 311,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 2,600.00 USD | 311,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 240.00 USD | 308,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 1,460.00 USD | 308,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2705` | 1,970.00 USD | 307,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 35,540.00 USD | 305,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3175` | 1,590.00 USD | 269,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3255` | 9,260.00 USD | 268,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3305` | 543.58 USD | 258,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3545` | 177.25 USD | 258,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 189.47 USD | 258,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3895` | 272.65 USD | 257,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3905` | 359.26 USD | 257,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3925` | 588.75 USD | 257,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3955` | 2,640.00 USD | 256,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3995` | 271.06 USD | 253,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 570.81 USD | 253,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4115` | 5,110.00 USD | 253,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4135` | 1,600.00 USD | 248,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 630.86 USD | 246,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4255` | 224.96 USD | 245,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4335` | 4,010.00 USD | 245,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4345` | 439.91 USD | 241,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4365` | 436.50 USD | 241,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4405` | 4,300.00 USD | 240,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4425` | 101.06 USD | 236,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 226.63 USD | 236,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4515` | 27,090.00 USD | 236,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4575` | 112.72 USD | 208,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4605` | 125.38 USD | 208,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4615` | 1,120.00 USD | 208,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4625` | 1,680.00 USD | 207,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4645` | 876.05 USD | 205,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4685` | 468.50 USD | 205,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4725` | 888.94 USD | 204,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4755` | 325.64 USD | 203,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 135.33 USD | 203,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 39,060.00 USD | 203,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4925` | 10,520.00 USD | 164,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4935` | 1,580.00 USD | 153,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 3,180.00 USD | 152,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4965` | 143.19 USD | 148,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 429.90 USD | 148,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5015` | 1,250.00 USD | 148,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 102.82 USD | 147,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 248.05 USD | 146,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5135` | 110.50 USD | 146,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5145` | 288.78 USD | 146,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 9,440.00 USD | 146,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5195` | 176.11 USD | 136,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5245` | 3,590.00 USD | 136,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5255` | 197.06 USD | 133,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5295` | 1,840.00 USD | 132,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5315` | 12,360.00 USD | 131,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5320` | 827,200.00 USD | 827,200.00 USD | 11,240.00 USD | 0.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5335` | 374.06 USD | 118,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5340` | 812,480.00 USD | 812,480.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5345` | 1,110.00 USD | 118,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5360` | 809,880.00 USD | 809,880.00 USD | 2,440.00 USD | 3,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5380` | 804,400.00 USD | 804,400.00 USD | 0.00 USD | 1,550.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5420` | 799,910.00 USD | 799,910.00 USD | 7,660.00 USD | 1,290.00 USD | 2,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5440` | 788,010.00 USD | 788,010.00 USD | 0.00 USD | 1,150.00 USD | 6,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5445` | 330.14 USD | 117,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5460` | 779,890.00 USD | 779,890.00 USD | 2,250.00 USD | 3,030.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5465` | 204.73 USD | 116,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5480` | 769,420.00 USD | 769,420.00 USD | 2,000.00 USD | 795.70 USD | 4,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5485` | 1,780.00 USD | 116,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5495` | 630.26 USD | 114,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5500` | 801,260.00 USD | 801,260.00 USD | 0.00 USD | 0.00 USD | 19.90 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5500` | 762,150.00 USD | 762,150.00 USD | 5,990.00 USD | 1,440.00 USD | 6,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5510` | 801,240.00 USD | 801,240.00 USD | 0.00 USD | 0.00 USD | 849.87 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5520` | 800,390.00 USD | 800,390.00 USD | 0.00 USD | 0.00 USD | 432.53 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5520` | 748,010.00 USD | 748,010.00 USD | 4,110.00 USD | 1,920.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5530` | 799,960.00 USD | 799,960.00 USD | 1,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5540` | 798,700.00 USD | 798,700.00 USD | 528.00 USD | 1,320.00 USD | 7.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5540` | 740,100.00 USD | 740,100.00 USD | 12,840.00 USD | 4,860.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5545` | 47,580.00 USD | 114,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5550` | 796,840.00 USD | 796,840.00 USD | 557.27 USD | 201.08 USD | 41.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5560` | 796,040.00 USD | 796,040.00 USD | 0.00 USD | 0.00 USD | 479.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5560` | 703,930.00 USD | 703,930.00 USD | 13,490.00 USD | 1,920.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5570` | 795,560.00 USD | 795,560.00 USD | 0.00 USD | 1,940.00 USD | 2,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5580` | 791,300.00 USD | 791,300.00 USD | 1,100.00 USD | 2,960.00 USD | 1,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5580` | 682,270.00 USD | 682,270.00 USD | 6,000.00 USD | 6,820.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5585` | 10,520.00 USD | 66,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5590` | 786,000.00 USD | 786,000.00 USD | 0.00 USD | 1,080.00 USD | 15.63 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5600` | 784,910.00 USD | 784,910.00 USD | 1,550.00 USD | 1,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5600` | 651,160.00 USD | 651,160.00 USD | 4,070.00 USD | 8,160.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5610` | 781,530.00 USD | 781,530.00 USD | 0.00 USD | 0.00 USD | 772.54 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5615` | 211.33 USD | 56,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5620` | 780,750.00 USD | 780,750.00 USD | 0.00 USD | 776.64 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5620` | 636,430.00 USD | 636,430.00 USD | 19,480.00 USD | 7,420.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5630` | 777,800.00 USD | 777,800.00 USD | 0.00 USD | 1,560.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5640` | 771,630.00 USD | 771,630.00 USD | 4,020.00 USD | 2,420.00 USD | 12.64 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5640` | 597,980.00 USD | 597,980.00 USD | 2,950.00 USD | 741.21 USD | 27.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5660` | 594,270.00 USD | 594,270.00 USD | 11,490.00 USD | 2,990.00 USD | 4,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5680` | 575,370.00 USD | 575,370.00 USD | 5,100.00 USD | 0.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5700` | 567,380.00 USD | 567,380.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5710` | 765,180.00 USD | 765,180.00 USD | 0.00 USD | 2,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5715` | 289.08 USD | 55,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5720` | 564,800.00 USD | 564,800.00 USD | 0.00 USD | 4,370.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5735` | 553.11 USD | 55,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5740` | 559,070.00 USD | 559,070.00 USD | 21,620.00 USD | 1,100.00 USD | 1,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5760` | 534,730.00 USD | 534,730.00 USD | 2,150.00 USD | 0.00 USD | 19.23 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5765` | 209.21 USD | 55,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5770` | 762,820.00 USD | 762,820.00 USD | 0.00 USD | 0.00 USD | 34.98 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5780` | 762,790.00 USD | 762,790.00 USD | 0.00 USD | 0.00 USD | 59.63 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5780` | 532,560.00 USD | 532,560.00 USD | 0.00 USD | 0.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5800` | 530,990.00 USD | 530,990.00 USD | 1,610.00 USD | 0.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5815` | 6,620.00 USD | 54,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5820` | 762,730.00 USD | 762,730.00 USD | 0.00 USD | 1,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5820` | 526,530.00 USD | 526,530.00 USD | 0.00 USD | 0.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5830` | 761,730.00 USD | 761,730.00 USD | 0.00 USD | 0.00 USD | 24.36 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5840` | 761,700.00 USD | 761,700.00 USD | 0.00 USD | 0.00 USD | 44.63 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5845` | 210.96 USD | 48,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5850` | 761,660.00 USD | 761,660.00 USD | 0.00 USD | 0.00 USD | 18.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5860` | 761,640.00 USD | 761,640.00 USD | 0.00 USD | 658.88 USD | 14,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5860` | 520,010.00 USD | 520,010.00 USD | 0.00 USD | 0.00 USD | 146.30 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5865` | 1,260.00 USD | 48,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5870` | 746,110.00 USD | 746,110.00 USD | 2,890.00 USD | 631.19 USD | 3,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5880` | 739,090.00 USD | 739,090.00 USD | 1,270.00 USD | 1,580.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5880` | 519,870.00 USD | 519,870.00 USD | 3,110.00 USD | 1,400.00 USD | 65.70 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5885` | 35,180.00 USD | 46,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5890` | 732,550.00 USD | 732,550.00 USD | 3,460.00 USD | 0.00 USD | 7.65 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5895` | 1,840.00 USD | 11,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5900` | 729,080.00 USD | 729,080.00 USD | 4,730.00 USD | 1,390.00 USD | 3.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5900` | 515,290.00 USD | 515,290.00 USD | 3,120.00 USD | 1,560.00 USD | 15.37 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5905` | 1,950.00 USD | 9,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5910` | 722,960.00 USD | 722,960.00 USD | 0.00 USD | 1,820.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5920` | 717,040.00 USD | 717,040.00 USD | 11,320.00 USD | 3,660.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5920` | 510,600.00 USD | 510,600.00 USD | 11,690.00 USD | 2,820.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5925` | 609.14 USD | 7,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5930` | 694,290.00 USD | 694,290.00 USD | 3,420.00 USD | 2,150.00 USD | 5,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5940` | 682,960.00 USD | 682,960.00 USD | 5,890.00 USD | 6,830.00 USD | 10,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5940` | 490,060.00 USD | 490,060.00 USD | 10,090.00 USD | 0.00 USD | 9,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5945` | 612.32 USD | 7,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5950` | 660,150.00 USD | 660,150.00 USD | 19,520.00 USD | 12,400.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5955` | 4,800.00 USD | 6,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5960` | 626,280.00 USD | 626,280.00 USD | 8,460.00 USD | 3,150.00 USD | 13,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5960` | 470,190.00 USD | 470,190.00 USD | 18,180.00 USD | 18,410.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5970` | 601,330.00 USD | 601,330.00 USD | 9,250.00 USD | 7,060.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5980` | 578,330.00 USD | 578,330.00 USD | 6,400.00 USD | 1,740.00 USD | 41,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5980` | 420,210.00 USD | 420,210.00 USD | 20,380.00 USD | 826.53 USD | 19,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5990` | 529,180.00 USD | 529,180.00 USD | 18,690.00 USD | 2,370.00 USD | 13,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6000` | 494,670.00 USD | 494,670.00 USD | 0.00 USD | 5,920.00 USD | 1,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6000` | 379,080.00 USD | 379,080.00 USD | 3,320.00 USD | 2,140.00 USD | 18,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6005` | 852.06 USD | 1,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6010` | 487,630.00 USD | 487,630.00 USD | 735.24 USD | 461.96 USD | 11,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.6015` | 995.49 USD | 995.49 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.6020` | 475,030.00 USD | 475,030.00 USD | 30,900.00 USD | 13,240.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6020` | 354,810.00 USD | 354,810.00 USD | 23,960.00 USD | 8,040.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6030` | 428,870.00 USD | 428,870.00 USD | 10,880.00 USD | 6,850.00 USD | 24.50 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6040` | 411,110.00 USD | 411,110.00 USD | 19,810.00 USD | 2,320.00 USD | 21.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6040` | 318,760.00 USD | 318,760.00 USD | 8,620.00 USD | 7,530.00 USD | 7,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6050` | 388,960.00 USD | 388,960.00 USD | 0.00 USD | 3,770.00 USD | 20,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6060` | 365,050.00 USD | 365,050.00 USD | 8,500.00 USD | 4,900.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6060` | 294,690.00 USD | 294,690.00 USD | 0.00 USD | 0.00 USD | 227.43 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6070` | 343,680.00 USD | 343,680.00 USD | 7,700.00 USD | 14,690.00 USD | 11,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6080` | 310,070.00 USD | 310,070.00 USD | 2,970.00 USD | 23,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6080` | 294,460.00 USD | 294,460.00 USD | 2,860.00 USD | 0.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6090` | 283,950.00 USD | 283,950.00 USD | 6,430.00 USD | 11,280.00 USD | 14,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6100` | 252,010.00 USD | 252,010.00 USD | 14,420.00 USD | 11,860.00 USD | 4,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6100` | 282,230.00 USD | 282,230.00 USD | 21,400.00 USD | 47,430.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6110` | 221,180.00 USD | 221,180.00 USD | 1,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6120` | 219,750.00 USD | 219,750.00 USD | 23,580.00 USD | 2,470.00 USD | 19,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6120` | 188,090.00 USD | 188,090.00 USD | 35,760.00 USD | 5,720.00 USD | 18,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6130` | 174,500.00 USD | 174,500.00 USD | 2,140.00 USD | 12,430.00 USD | 22,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6140` | 137,150.00 USD | 137,150.00 USD | 53,460.00 USD | 18,080.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6140` | 128,100.00 USD | 128,100.00 USD | 51,550.00 USD | 8,040.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6150` | 61,570.00 USD | 61,570.00 USD | 14,190.00 USD | 7,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6160` | 39,560.00 USD | 39,560.00 USD | 25,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6160` | 57,720.00 USD | 57,720.00 USD | 12,920.00 USD | 16,340.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6170` | 13,910.00 USD | 13,910.00 USD | 0.00 USD | 0.00 USD | 13,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6180` | 23,710.00 USD | 23,710.00 USD | 20,870.00 USD | 2,610.00 USD | 228.92 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6200` | 42,100.00 USD | 42,100.00 USD | 23,430.00 USD | 0.00 USD | 18,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6220` | 69,720.00 USD | 69,720.00 USD | 4,760.00 USD | 22,640.00 USD | 215.59 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6240` | 69,900.00 USD | 69,900.00 USD | 0.00 USD | 0.00 USD | 171.81 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6260` | 137,210.00 USD | 137,210.00 USD | 67,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6290` | 2,020.00 USD | 2,020.00 USD | 0.00 USD | 2,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6300` | 147,130.00 USD | 147,130.00 USD | 0.00 USD | 0.00 USD | 9,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6310` | 28,950.00 USD | 28,950.00 USD | 11,740.00 USD | 3,970.00 USD | 11,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6320` | 60,910.00 USD | 60,910.00 USD | 31,880.00 USD | 0.00 USD | 78.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6320` | 147,500.00 USD | 147,500.00 USD | 0.00 USD | 0.00 USD | 369.35 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6330` | 116,870.00 USD | 116,870.00 USD | 17,300.00 USD | 5,390.00 USD | 33,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6340` | 185,410.00 USD | 185,410.00 USD | 32,460.00 USD | 0.00 USD | 36,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6340` | 216,540.00 USD | 216,540.00 USD | 68,660.00 USD | 0.00 USD | 381.22 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6350` | 243,910.00 USD | 243,910.00 USD | 51,360.00 USD | 0.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6360` | 373,650.00 USD | 373,650.00 USD | 63,010.00 USD | 2,470.00 USD | 64,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6360` | 307,840.00 USD | 307,840.00 USD | 34,320.00 USD | 0.00 USD | 56,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6370` | 409,530.00 USD | 409,530.00 USD | 0.00 USD | 5,770.00 USD | 30,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6380` | 433,770.00 USD | 433,770.00 USD | 0.00 USD | 19,010.00 USD | 5,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6380` | 346,930.00 USD | 346,930.00 USD | 0.00 USD | 0.00 USD | 39,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6390` | 503,230.00 USD | 503,230.00 USD | 18,790.00 USD | 3,690.00 USD | 47,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6400` | 619,220.00 USD | 619,220.00 USD | 57,170.00 USD | 28,050.00 USD | 30,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6400` | 367,450.00 USD | 367,450.00 USD | 0.00 USD | 7,510.00 USD | 13,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6410` | 668,360.00 USD | 668,360.00 USD | 32,400.00 USD | 9,300.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6420` | 771,930.00 USD | 771,930.00 USD | 69,490.00 USD | 14,860.00 USD | 19,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6420` | 474,760.00 USD | 474,760.00 USD | 55,350.00 USD | 35,430.00 USD | 16,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6430` | 850,850.00 USD | 850,850.00 USD | 35,700.00 USD | 15,580.00 USD | 27,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6440` | 963,600.00 USD | 963,600.00 USD | 39,760.00 USD | 23,720.00 USD | 49,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6440` | 562,140.00 USD | 562,140.00 USD | 44,690.00 USD | 24,820.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6450` | 1,080,000.00 USD | 1,080,000.00 USD | 70,250.00 USD | 9,920.00 USD | 36,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6460` | 1,150,000.00 USD | 1,150,000.00 USD | 57,400.00 USD | 9,320.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6460` | 919,670.00 USD | 919,670.00 USD | 172,610.00 USD | 46,630.00 USD | 138,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6470` | 1,250,000.00 USD | 1,250,000.00 USD | 74,410.00 USD | 16,010.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6480` | 1,370,000.00 USD | 1,370,000.00 USD | 112,500.00 USD | 6,780.00 USD | 151.61 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6480` | 1,070,000.00 USD | 1,070,000.00 USD | 86,440.00 USD | 26,520.00 USD | 33,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6490` | 1,440,000.00 USD | 1,440,000.00 USD | 66,830.00 USD | 1,230.00 USD | 9,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6500` | 1,520,000.00 USD | 1,520,000.00 USD | 64,920.00 USD | 5,920.00 USD | 128.67 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6500` | 1,270,000.00 USD | 1,270,000.00 USD | 73,560.00 USD | 0.00 USD | 132,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6510` | 1,580,000.00 USD | 1,580,000.00 USD | 55,500.00 USD | 0.00 USD | 11,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6520` | 1,690,000.00 USD | 1,690,000.00 USD | 93,550.00 USD | 9,040.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6520` | 1,690,000.00 USD | 1,690,000.00 USD | 298,050.00 USD | 10,910.00 USD | 104,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6530` | 1,700,000.00 USD | 1,700,000.00 USD | 11,510.00 USD | 3,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6540` | 1,740,000.00 USD | 1,740,000.00 USD | 24,280.00 USD | 0.00 USD | 10,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6540` | 1,770,000.00 USD | 1,770,000.00 USD | 15,730.00 USD | 4,440.00 USD | 61,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6550` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 6,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6560` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6560` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 5,380.00 USD | 847.61 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6570` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 59.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6580` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 3,310.00 USD | 25.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6580` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 28,280.00 USD | 9,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6590` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 5,890.00 USD | 164.02 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6600` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 8,400.00 USD | 59.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6600` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 15,500.00 USD | 580.13 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6610` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 142.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6620` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6620` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 128.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6630` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 39.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6640` | 1,790,000.00 USD | 1,790,000.00 USD | 11,190.00 USD | 0.00 USD | 126.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6640` | 1,860,000.00 USD | 1,860,000.00 USD | 33,660.00 USD | 0.00 USD | 534.34 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6650` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 3,160.00 USD | 17,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6660` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6660` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 6,770.00 USD | 436.87 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6670` | 1,830,000.00 USD | 1,830,000.00 USD | 18,850.00 USD | 0.00 USD | 24.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6680` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 44.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6680` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 308.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6690` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 3,550.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6700` | 1,880,000.00 USD | 1,880,000.00 USD | 8,830.00 USD | 1,920.00 USD | 24,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6700` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 966.49 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6710` | 1,930,000.00 USD | 1,930,000.00 USD | 41,970.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6720` | 1,960,000.00 USD | 1,960,000.00 USD | 58,470.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6730` | 1,960,000.00 USD | 1,960,000.00 USD | 24,320.00 USD | 3,670.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6740` | 2,040,000.00 USD | 2,040,000.00 USD | 64,370.00 USD | 7,120.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6740` | 2,000,000.00 USD | 2,000,000.00 USD | 39,730.00 USD | 0.00 USD | 99.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6750` | 2,080,000.00 USD | 2,080,000.00 USD | 28,700.00 USD | 4,300.00 USD | 12,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6760` | 2,100,000.00 USD | 2,100,000.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6760` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 77,970.00 USD | 33,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6770` | 2,140,000.00 USD | 2,140,000.00 USD | 14,540.00 USD | 6,110.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6780` | 2,190,000.00 USD | 2,190,000.00 USD | 33,610.00 USD | 12,680.00 USD | 8,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6780` | 2,210,000.00 USD | 2,210,000.00 USD | 63,600.00 USD | 14,400.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6790` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 18,610.00 USD | 14,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6800` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6800` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 16,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6810` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 1,940.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6820` | 2,290,000.00 USD | 2,290,000.00 USD | 22,600.00 USD | 16,590.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6820` | 2,310,000.00 USD | 2,310,000.00 USD | 32,570.00 USD | 53,450.00 USD | 145.79 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6830` | 2,370,000.00 USD | 2,370,000.00 USD | 24,570.00 USD | 26,560.00 USD | 36,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6840` | 2,460,000.00 USD | 2,460,000.00 USD | 45,780.00 USD | 25,860.00 USD | 11,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6840` | 2,520,000.00 USD | 2,520,000.00 USD | 57,890.00 USD | 54,300.00 USD | 102,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6850` | 2,520,000.00 USD | 2,520,000.00 USD | 51,090.00 USD | 5,780.00 USD | 10,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6860` | 2,580,000.00 USD | 2,580,000.00 USD | 40,250.00 USD | 4,380.00 USD | 14,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6860` | 2,600,000.00 USD | 2,600,000.00 USD | 49,930.00 USD | 14,540.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6870` | 2,650,000.00 USD | 2,650,000.00 USD | 63,220.00 USD | 1,160.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6880` | 2,700,000.00 USD | 2,700,000.00 USD | 14,350.00 USD | 11,160.00 USD | 25,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6880` | 2,650,000.00 USD | 2,650,000.00 USD | 38,030.00 USD | 17,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6890` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6900` | 2,750,000.00 USD | 2,750,000.00 USD | 18,600.00 USD | 4,030.00 USD | 21,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6900` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 15,510.00 USD | 16,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6910` | 2,820,000.00 USD | 2,820,000.00 USD | 28,860.00 USD | 1,730.00 USD | 39,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6920` | 2,850,000.00 USD | 2,850,000.00 USD | 16,800.00 USD | 0.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6920` | 2,820,000.00 USD | 2,820,000.00 USD | 69,620.00 USD | 2,090.00 USD | 62,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6930` | 2,860,000.00 USD | 2,860,000.00 USD | 10,030.00 USD | 0.00 USD | 168.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6940` | 2,890,000.00 USD | 2,890,000.00 USD | 11,230.00 USD | 2,090.00 USD | 9,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6940` | 2,880,000.00 USD | 2,880,000.00 USD | 14,220.00 USD | 0.00 USD | 42,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6950` | 2,920,000.00 USD | 2,920,000.00 USD | 22,480.00 USD | 4,460.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6960` | 2,980,000.00 USD | 2,980,000.00 USD | 58,370.00 USD | 6,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6960` | 2,950,000.00 USD | 2,950,000.00 USD | 59,960.00 USD | 0.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6970` | 3,020,000.00 USD | 3,020,000.00 USD | 33,460.00 USD | 4,780.00 USD | 34.66 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6980` | 3,040,000.00 USD | 3,040,000.00 USD | 9,140.00 USD | 4,100.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6980` | 3,000,000.00 USD | 3,000,000.00 USD | 35,980.00 USD | 16,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6990` | 3,050,000.00 USD | 3,050,000.00 USD | 5,180.00 USD | 4,830.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7000` | 3,090,000.00 USD | 3,090,000.00 USD | 18,240.00 USD | 4,020.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7000` | 3,070,000.00 USD | 3,070,000.00 USD | 29,740.00 USD | 0.00 USD | 40,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7010` | 3,100,000.00 USD | 3,100,000.00 USD | 15,520.00 USD | 0.00 USD | 73.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7020` | 3,120,000.00 USD | 3,120,000.00 USD | 14,360.00 USD | 0.00 USD | 22.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7020` | 3,150,000.00 USD | 3,150,000.00 USD | 29,810.00 USD | 0.00 USD | 53,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7030` | 3,130,000.00 USD | 3,130,000.00 USD | 4,330.00 USD | 0.00 USD | 10,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7040` | 3,180,000.00 USD | 3,180,000.00 USD | 29,930.00 USD | 2,630.00 USD | 8,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7040` | 3,350,000.00 USD | 3,350,000.00 USD | 95,520.00 USD | 0.00 USD | 96,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7050` | 3,230,000.00 USD | 3,230,000.00 USD | 29,790.00 USD | 2,660.00 USD | 18,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7060` | 3,250,000.00 USD | 3,250,000.00 USD | 8,590.00 USD | 3,860.00 USD | 13,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7060` | 3,610,000.00 USD | 3,610,000.00 USD | 47,840.00 USD | 33,490.00 USD | 178,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7070` | 3,310,000.00 USD | 3,310,000.00 USD | 19,980.00 USD | 21,860.00 USD | 17,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7080` | 3,330,000.00 USD | 3,330,000.00 USD | 18,420.00 USD | 0.00 USD | 228.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7080` | 3,780,000.00 USD | 3,780,000.00 USD | 24,440.00 USD | 64,870.00 USD | 82,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7100` | 4,140,000.00 USD | 4,140,000.00 USD | 150,830.00 USD | 63,530.00 USD | 148,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7120` | 4,550,000.00 USD | 4,550,000.00 USD | 101,040.00 USD | 78,760.00 USD | 228,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7140` | 4,950,000.00 USD | 4,950,000.00 USD | 202,560.00 USD | 67,260.00 USD | 133,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7160` | 5,290,000.00 USD | 5,290,000.00 USD | 113,040.00 USD | 65,260.00 USD | 164,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7180` | 5,580,000.00 USD | 5,580,000.00 USD | 165,860.00 USD | 56,910.00 USD | 66,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7200` | 5,900,000.00 USD | 5,900,000.00 USD | 93,750.00 USD | 45,160.00 USD | 177,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7220` | 6,380,000.00 USD | 6,380,000.00 USD | 318,420.00 USD | 67,130.00 USD | 98,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7240` | 6,680,000.00 USD | 6,680,000.00 USD | 146,110.00 USD | 24,910.00 USD | 128,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7245` | 364.39 USD | 364.39 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.7255` | 124.05 USD | 488.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7260` | 7,020,000.00 USD | 7,020,000.00 USD | 106,410.00 USD | 52,120.00 USD | 175,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7280` | 7,240,000.00 USD | 7,240,000.00 USD | 99,750.00 USD | 40,180.00 USD | 83,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7295` | 43,330.00 USD | 43,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7300` | 7,530,000.00 USD | 7,530,000.00 USD | 115,310.00 USD | 60,310.00 USD | 109,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7320` | 7,860,000.00 USD | 7,860,000.00 USD | 189,840.00 USD | 65,640.00 USD | 80,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7340` | 7,970,000.00 USD | 7,970,000.00 USD | 31,260.00 USD | 8,620.00 USD | 63,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7360` | 8,150,000.00 USD | 8,150,000.00 USD | 103,600.00 USD | 46,790.00 USD | 35,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7380` | 8,300,000.00 USD | 8,300,000.00 USD | 73,710.00 USD | 19,000.00 USD | 60,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7400` | 8,330,000.00 USD | 8,330,000.00 USD | 1,730.00 USD | 4,760.00 USD | 20,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7420` | 8,440,000.00 USD | 8,440,000.00 USD | 35,810.00 USD | 35,860.00 USD | 31,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7440` | 8,620,000.00 USD | 8,620,000.00 USD | 74,450.00 USD | 39,890.00 USD | 70,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7460` | 8,790,000.00 USD | 8,790,000.00 USD | 88,800.00 USD | 28,800.00 USD | 51,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7480` | 8,920,000.00 USD | 8,920,000.00 USD | 60,580.00 USD | 28,900.00 USD | 38,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7500` | 9,010,000.00 USD | 9,010,000.00 USD | 52,320.00 USD | 12,610.00 USD | 25,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7520` | 9,120,000.00 USD | 9,120,000.00 USD | 53,470.00 USD | 13,000.00 USD | 50,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7540` | 9,180,000.00 USD | 9,180,000.00 USD | 30,340.00 USD | 1,890.00 USD | 25,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7560` | 9,240,000.00 USD | 9,240,000.00 USD | 26,000.00 USD | 7,570.00 USD | 22,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7580` | 9,350,000.00 USD | 9,350,000.00 USD | 55,420.00 USD | 11,790.00 USD | 45,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7600` | 9,490,000.00 USD | 9,490,000.00 USD | 57,020.00 USD | 4,320.00 USD | 80,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7620` | 9,590,000.00 USD | 9,590,000.00 USD | 54,140.00 USD | 24,170.00 USD | 21,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7640` | 9,700,000.00 USD | 9,700,000.00 USD | 50,390.00 USD | 13,520.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7660` | 9,860,000.00 USD | 9,860,000.00 USD | 56,130.00 USD | 18,130.00 USD | 91,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7680` | 10,000,000.00 USD | 10,000,000.00 USD | 66,570.00 USD | 32,520.00 USD | 41,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7700` | 10,070,000.00 USD | 10,070,000.00 USD | 10,860.00 USD | 12,600.00 USD | 41,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7720` | 10,190,000.00 USD | 10,190,000.00 USD | 58,380.00 USD | 32,920.00 USD | 25,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7725` | 165.62 USD | 43,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7740` | 10,300,000.00 USD | 10,300,000.00 USD | 51,600.00 USD | 25,250.00 USD | 35,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7760` | 10,350,000.00 USD | 10,350,000.00 USD | 38,170.00 USD | 2,980.00 USD | 12,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7765` | 330.78 USD | 44,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7780` | 10,470,000.00 USD | 10,470,000.00 USD | 68,800.00 USD | 20,860.00 USD | 32,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7800` | 10,640,000.00 USD | 10,640,000.00 USD | 60,490.00 USD | 21,940.00 USD | 80,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7820` | 10,750,000.00 USD | 10,750,000.00 USD | 90,020.00 USD | 17,850.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7840` | 10,830,000.00 USD | 10,830,000.00 USD | 72,650.00 USD | 7,150.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7860` | 10,910,000.00 USD | 10,910,000.00 USD | 32,690.00 USD | 9,290.00 USD | 31,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7880` | 10,950,000.00 USD | 10,950,000.00 USD | 11,900.00 USD | 10,710.00 USD | 22,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7900` | 11,030,000.00 USD | 11,030,000.00 USD | 44,050.00 USD | 16,710.00 USD | 17,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7910` | 11,070,000.00 USD | 11,070,000.00 USD | 30,620.00 USD | 5,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8005` | 19,120.00 USD | 63,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8665` | 378.95 USD | 63,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9215` | 25,670.00 USD | 89,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9265` | 16,350.00 USD | 105,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9935` | 166.01 USD | 106,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.07` | 81,680.00 USD | 187,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 7,290.00 USD | 194,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 479.74 USD | 195,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.12` | 2,800.00 USD | 198,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.17` | 501.44 USD | 198,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.23` | 138.70 USD | 198,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1395` | 312,580.00 USD | 0.00 USD | 419.65 USD | `-77.58%` | `3,008.22` |
| `Live` | `Long` | `0.1795` | 312,160.00 USD | 0.00 USD | 249.20 USD | `-71.15%` | `1,388.32` |
| `Live` | `Long` | `0.1875` | 311,910.00 USD | 0.00 USD | 269.27 USD | `-69.86%` | `1,436.09` |
| `Live` | `Long` | `0.2205` | 311,640.00 USD | 0.00 USD | 228.91 USD | `-64.56%` | `1,038.12` |
| `Live` | `Long` | `0.2305` | 311,410.00 USD | 0.00 USD | 2,600.00 USD | `-62.95%` | `11,284.25` |
| `Live` | `Long` | `0.2385` | 308,810.00 USD | 0.00 USD | 240.00 USD | `-61.67%` | `1,006.27` |
| `Live` | `Long` | `0.2425` | 308,570.00 USD | 0.00 USD | 1,460.00 USD | `-61.03%` | `6,000.00` |
| `Live` | `Long` | `0.2705` | 307,120.00 USD | 0.00 USD | 1,970.00 USD | `-56.53%` | `7,272.07` |
| `Live` | `Long` | `0.2755` | 305,150.00 USD | 0.00 USD | 35,540.00 USD | `-55.72%` | `129,000.00` |
| `Live` | `Long` | `0.3175` | 269,610.00 USD | 0.00 USD | 1,590.00 USD | `-48.97%` | `5,000.00` |
| `Live` | `Long` | `0.3255` | 268,020.00 USD | 0.00 USD | 9,260.00 USD | `-47.69%` | `28,446.85` |
| `Live` | `Long` | `0.3305` | 258,760.00 USD | 0.00 USD | 543.58 USD | `-46.88%` | `1,644.73` |
| `Live` | `Long` | `0.3545` | 258,220.00 USD | 0.00 USD | 177.25 USD | `-43.02%` | `500.00` |
| `Live` | `Long` | `0.3665` | 258,040.00 USD | 0.00 USD | 189.47 USD | `-41.10%` | `516.98` |
| `Live` | `Long` | `0.3895` | 257,850.00 USD | 0.00 USD | 272.65 USD | `-37.40%` | `700.00` |
| `Live` | `Long` | `0.3905` | 257,580.00 USD | 0.00 USD | 359.26 USD | `-37.24%` | `919.99` |
| `Live` | `Long` | `0.3925` | 257,220.00 USD | 0.00 USD | 588.75 USD | `-36.92%` | `1,500.00` |
| `Live` | `Long` | `0.3955` | 256,630.00 USD | 0.00 USD | 2,640.00 USD | `-36.44%` | `6,686.27` |
| `Live` | `Long` | `0.3995` | 253,990.00 USD | 0.00 USD | 271.06 USD | `-35.79%` | `678.49` |
| `Live` | `Long` | `0.4035` | 253,720.00 USD | 0.00 USD | 570.81 USD | `-35.15%` | `1,414.65` |
| `Live` | `Long` | `0.4115` | 253,150.00 USD | 0.00 USD | 5,110.00 USD | `-33.86%` | `12,426.15` |
| `Live` | `Long` | `0.4135` | 248,030.00 USD | 0.00 USD | 1,600.00 USD | `-33.54%` | `3,868.97` |
| `Live` | `Long` | `0.4185` | 246,430.00 USD | 0.00 USD | 630.86 USD | `-32.74%` | `1,507.44` |
| `Live` | `Long` | `0.4255` | 245,800.00 USD | 0.00 USD | 224.96 USD | `-31.61%` | `528.69` |
| `Live` | `Long` | `0.4335` | 245,580.00 USD | 0.00 USD | 4,010.00 USD | `-30.33%` | `9,243.24` |
| `Live` | `Long` | `0.4345` | 241,570.00 USD | 0.00 USD | 439.91 USD | `-30.17%` | `1,012.44` |
| `Live` | `Long` | `0.4365` | 241,130.00 USD | 0.00 USD | 436.50 USD | `-29.85%` | `1,000.00` |
| `Live` | `Long` | `0.4405` | 240,690.00 USD | 0.00 USD | 4,300.00 USD | `-29.20%` | `9,753.33` |
| `Live` | `Long` | `0.4425` | 236,400.00 USD | 0.00 USD | 101.06 USD | `-28.88%` | `228.39` |
| `Live` | `Long` | `0.4475` | 236,300.00 USD | 0.00 USD | 226.63 USD | `-28.08%` | `506.43` |
| `Live` | `Long` | `0.4515` | 236,070.00 USD | 0.00 USD | 27,090.00 USD | `-27.43%` | `60,000.00` |
| `Live` | `Long` | `0.4575` | 208,980.00 USD | 0.00 USD | 112.72 USD | `-26.47%` | `246.38` |
| `Live` | `Long` | `0.4605` | 208,870.00 USD | 0.00 USD | 125.38 USD | `-25.99%` | `272.27` |
| `Live` | `Long` | `0.4615` | 208,740.00 USD | 0.00 USD | 1,120.00 USD | `-25.83%` | `2,420.08` |
| `Live` | `Long` | `0.4625` | 207,620.00 USD | 0.00 USD | 1,680.00 USD | `-25.67%` | `3,622.78` |
| `Live` | `Long` | `0.4645` | 205,950.00 USD | 0.00 USD | 876.05 USD | `-25.35%` | `1,886.00` |
| `Live` | `Long` | `0.4685` | 205,070.00 USD | 0.00 USD | 468.50 USD | `-24.70%` | `1,000.00` |
| `Live` | `Long` | `0.4725` | 204,600.00 USD | 0.00 USD | 888.94 USD | `-24.06%` | `1,881.36` |
| `Live` | `Long` | `0.4755` | 203,720.00 USD | 0.00 USD | 325.64 USD | `-23.58%` | `684.84` |
| `Live` | `Long` | `0.4835` | 203,390.00 USD | 0.00 USD | 135.33 USD | `-22.29%` | `279.90` |
| `Live` | `Long` | `0.4865` | 203,250.00 USD | 0.00 USD | 39,060.00 USD | `-21.81%` | `80,294.37` |
| `Live` | `Long` | `0.4925` | 164,190.00 USD | 0.00 USD | 10,520.00 USD | `-20.85%` | `21,364.96` |
| `Live` | `Long` | `0.4935` | 153,670.00 USD | 0.00 USD | 1,580.00 USD | `-20.68%` | `3,199.85` |
| `Live` | `Long` | `0.4955` | 152,090.00 USD | 0.00 USD | 3,180.00 USD | `-20.36%` | `6,422.59` |
| `Live` | `Long` | `0.4965` | 148,910.00 USD | 0.00 USD | 143.19 USD | `-20.20%` | `288.40` |
| `Live` | `Long` | `0.4985` | 148,760.00 USD | 0.00 USD | 429.90 USD | `-19.88%` | `862.38` |
| `Live` | `Long` | `0.5015` | 148,330.00 USD | 0.00 USD | 1,250.00 USD | `-19.40%` | `2,500.00` |
| `Live` | `Long` | `0.5085` | 147,080.00 USD | 0.00 USD | 102.82 USD | `-18.27%` | `202.20` |
| `Live` | `Long` | `0.5125` | 146,980.00 USD | 0.00 USD | 248.05 USD | `-17.63%` | `484.00` |
| `Live` | `Long` | `0.5135` | 146,730.00 USD | 0.00 USD | 110.50 USD | `-17.47%` | `215.19` |
| `Live` | `Long` | `0.5145` | 146,620.00 USD | 0.00 USD | 288.78 USD | `-17.31%` | `561.28` |
| `Live` | `Long` | `0.5175` | 146,330.00 USD | 0.00 USD | 9,440.00 USD | `-16.83%` | `18,249.92` |
| `Live` | `Long` | `0.5195` | 136,890.00 USD | 0.00 USD | 176.11 USD | `-16.51%` | `339.00` |
| `Live` | `Long` | `0.5245` | 136,710.00 USD | 0.00 USD | 3,590.00 USD | `-15.70%` | `6,837.35` |
| `Live` | `Long` | `0.5255` | 133,120.00 USD | 0.00 USD | 197.06 USD | `-15.54%` | `375.00` |
| `Live` | `Long` | `0.5295` | 132,930.00 USD | 0.00 USD | 1,840.00 USD | `-14.90%` | `3,467.51` |
| `Live` | `Long` | `0.5315` | 131,090.00 USD | 0.00 USD | 12,360.00 USD | `-14.58%` | `23,252.00` |
| `Live` | `Long` | `0.5335` | 118,730.00 USD | 0.00 USD | 374.06 USD | `-14.26%` | `701.14` |
| `Live` | `Long` | `0.5345` | 118,360.00 USD | 0.00 USD | 1,110.00 USD | `-14.10%` | `2,078.06` |
| `Live` | `Long` | `0.5445` | 117,250.00 USD | 0.00 USD | 330.14 USD | `-12.49%` | `606.32` |
| `Live` | `Long` | `0.5465` | 116,920.00 USD | 0.00 USD | 204.73 USD | `-12.17%` | `374.62` |
| `Live` | `Long` | `0.5485` | 116,710.00 USD | 0.00 USD | 1,780.00 USD | `-11.85%` | `3,249.73` |
| `Live` | `Long` | `0.5495` | 114,930.00 USD | 0.00 USD | 630.26 USD | `-11.68%` | `1,146.97` |
| `Live` | `Long` | `0.5545` | 114,300.00 USD | 0.00 USD | 47,580.00 USD | `-10.88%` | `85,806.96` |
| `Live` | `Long` | `0.5585` | 66,720.00 USD | 0.00 USD | 10,520.00 USD | `-10.24%` | `18,834.52` |
| `Live` | `Long` | `0.5615` | 56,200.00 USD | 0.00 USD | 211.33 USD | `-9.76%` | `376.36` |
| `Live` | `Long` | `0.5715` | 55,990.00 USD | 0.00 USD | 289.08 USD | `-8.15%` | `505.82` |
| `Live` | `Long` | `0.5735` | 55,700.00 USD | 0.00 USD | 553.11 USD | `-7.83%` | `964.45` |
| `Live` | `Long` | `0.5765` | 55,150.00 USD | 0.00 USD | 209.21 USD | `-7.34%` | `362.90` |
| `Live` | `Long` | `0.5815` | 54,940.00 USD | 0.00 USD | 6,620.00 USD | `-6.54%` | `11,392.84` |
| `Live` | `Long` | `0.5845` | 48,310.00 USD | 0.00 USD | 210.96 USD | `-6.06%` | `360.92` |
| `Live` | `Long` | `0.5865` | 48,100.00 USD | 0.00 USD | 1,260.00 USD | `-5.74%` | `2,142.98` |
| `Live` | `Long` | `0.5885` | 46,850.00 USD | 0.00 USD | 35,180.00 USD | `-5.42%` | `59,785.55` |
| `Live` | `Long` | `0.5895` | 11,660.00 USD | 0.00 USD | 1,840.00 USD | `-5.26%` | `3,127.08` |
| `Live` | `Long` | `0.5905` | 9,820.00 USD | 0.00 USD | 1,950.00 USD | `-5.09%` | `3,302.26` |
| `Live` | `Long` | `0.5925` | 7,870.00 USD | 0.00 USD | 609.14 USD | `-4.77%` | `1,028.09` |
| `Live` | `Long` | `0.5945` | 7,260.00 USD | 0.00 USD | 612.32 USD | `-4.45%` | `1,029.97` |
| `Live` | `Long` | `0.5955` | 6,650.00 USD | 0.00 USD | 4,800.00 USD | `-4.29%` | `8,059.33` |
| `Live` | `Long` | `0.6005` | 1,850.00 USD | 0.00 USD | 852.06 USD | `-3.49%` | `1,418.92` |
| `Live` | `Long` | `0.6015` | 995.49 USD | 0.00 USD | 995.49 USD | `-3.33%` | `1,655.01` |
| `Live` | `Short` | `0.7245` | 364.39 USD | 364.39 USD | 0.00 USD | `+16.44%` | `502.96` |
| `Live` | `Short` | `0.7255` | 488.44 USD | 124.05 USD | 0.00 USD | `+16.60%` | `170.98` |
| `Live` | `Short` | `0.7295` | 43,820.00 USD | 43,330.00 USD | 0.00 USD | `+17.25%` | `59,401.36` |
| `Live` | `Short` | `0.7725` | 43,990.00 USD | 165.62 USD | 0.00 USD | `+24.16%` | `214.40` |
| `Live` | `Short` | `0.7765` | 44,320.00 USD | 330.78 USD | 0.00 USD | `+24.80%` | `425.99` |
| `Live` | `Short` | `0.8005` | 63,440.00 USD | 19,120.00 USD | 0.00 USD | `+28.66%` | `23,882.80` |
| `Live` | `Short` | `0.8665` | 63,820.00 USD | 378.95 USD | 0.00 USD | `+39.26%` | `437.33` |
| `Live` | `Short` | `0.9215` | 89,490.00 USD | 25,670.00 USD | 0.00 USD | `+48.10%` | `27,860.03` |
| `Live` | `Short` | `0.9265` | 105,840.00 USD | 16,350.00 USD | 0.00 USD | `+48.91%` | `17,648.14` |
| `Live` | `Short` | `0.9935` | 106,010.00 USD | 166.01 USD | 0.00 USD | `+59.68%` | `167.10` |
| `Live` | `Short` | `1.07` | 187,680.00 USD | 81,680.00 USD | 0.00 USD | `+72.05%` | `76,300.00` |
| `Live` | `Short` | `1.09` | 194,980.00 USD | 7,290.00 USD | 0.00 USD | `+75.27%` | `6,689.45` |
| `Live` | `Short` | `1.09` | 195,460.00 USD | 479.74 USD | 0.00 USD | `+75.43%` | `439.52` |
| `Live` | `Short` | `1.12` | 198,260.00 USD | 2,800.00 USD | 0.00 USD | `+79.93%` | `2,500.00` |
| `Live` | `Short` | `1.17` | 198,760.00 USD | 501.44 USD | 0.00 USD | `+88.60%` | `427.30` |
| `Live` | `Short` | `1.23` | 198,900.00 USD | 138.70 USD | 0.00 USD | `+97.44%` | `112.90` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.3505` | 89,670.00 USD | 0.00 USD | 340.19 USD | `-43.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4635` | 89,330.00 USD | 0.00 USD | 104.57 USD | `-25.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4805` | 89,230.00 USD | 0.00 USD | 14,740.00 USD | `-22.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 74,490.00 USD | 0.00 USD | 2,210.00 USD | `-19.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5085` | 72,280.00 USD | 0.00 USD | 101.97 USD | `-18.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5125` | 72,180.00 USD | 0.00 USD | 5,380.00 USD | `-17.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5205` | 66,800.00 USD | 0.00 USD | 228.77 USD | `-16.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5305` | 66,570.00 USD | 0.00 USD | 770.19 USD | `-14.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5445` | 65,800.00 USD | 0.00 USD | 8,750.00 USD | `-12.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5455` | 57,040.00 USD | 0.00 USD | 8,150.00 USD | `-12.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5485` | 48,890.00 USD | 0.00 USD | 4,500.00 USD | `-11.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5515` | 44,400.00 USD | 0.00 USD | 126.71 USD | `-11.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5525` | 44,270.00 USD | 0.00 USD | 126.90 USD | `-11.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5555` | 44,140.00 USD | 0.00 USD | 33,000.00 USD | `-10.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5565` | 11,150.00 USD | 0.00 USD | 173.58 USD | `-10.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5595` | 10,970.00 USD | 0.00 USD | 127.61 USD | `-10.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 10,840.00 USD | 0.00 USD | 339.84 USD | `-9.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5625` | 10,500.00 USD | 0.00 USD | 126.55 USD | `-9.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5655` | 10,380.00 USD | 0.00 USD | 127.62 USD | `-9.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5695` | 10,250.00 USD | 0.00 USD | 127.30 USD | `-8.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5715` | 10,120.00 USD | 0.00 USD | 127.63 USD | `-8.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5735` | 10,000.00 USD | 0.00 USD | 151.62 USD | `-7.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5755` | 9,840.00 USD | 0.00 USD | 127.29 USD | `-7.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5785` | 9,720.00 USD | 0.00 USD | 127.36 USD | `-7.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5815` | 9,590.00 USD | 0.00 USD | 127.27 USD | `-6.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5835` | 9,460.00 USD | 0.00 USD | 178.88 USD | `-6.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5845` | 9,280.00 USD | 0.00 USD | 127.33 USD | `-6.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5865` | 9,160.00 USD | 0.00 USD | 128.36 USD | `-5.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5875` | 9,030.00 USD | 0.00 USD | 128.34 USD | `-5.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5895` | 8,900.00 USD | 0.00 USD | 128.45 USD | `-5.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5905` | 8,770.00 USD | 0.00 USD | 127.30 USD | `-5.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5925` | 8,640.00 USD | 0.00 USD | 265.69 USD | `-4.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5975` | 8,380.00 USD | 0.00 USD | 597.80 USD | `-3.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 7,780.00 USD | 0.00 USD | 953.02 USD | `-3.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6045` | 6,830.00 USD | 0.00 USD | 999.99 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 5,830.00 USD | 0.00 USD | 1,510.00 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6065` | 4,320.00 USD | 0.00 USD | 1,910.00 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6085` | 2,410.00 USD | 0.00 USD | 301.32 USD | `-2.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6115` | 2,110.00 USD | 0.00 USD | 629.83 USD | `-1.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6135` | 1,480.00 USD | 0.00 USD | 242.45 USD | `-1.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6175` | 1,240.00 USD | 0.00 USD | 519.13 USD | `-0.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6185` | 718.99 USD | 0.00 USD | 177.58 USD | `-0.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 541.40 USD | 0.00 USD | 541.40 USD | `-0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6275` | 433.11 USD | 433.11 USD | 0.00 USD | `+0.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6285` | 903.04 USD | 469.94 USD | 0.00 USD | `+1.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 5,330.00 USD | 4,430.00 USD | 0.00 USD | `+1.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6315` | 5,490.00 USD | 160.16 USD | 0.00 USD | `+1.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 6,480.00 USD | 987.19 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6335` | 14,870.00 USD | 8,390.00 USD | 0.00 USD | `+1.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6345` | 15,150.00 USD | 276.40 USD | 0.00 USD | `+1.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6395` | 16,350.00 USD | 1,200.00 USD | 0.00 USD | `+2.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6405` | 16,490.00 USD | 145.91 USD | 0.00 USD | `+2.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6445` | 16,610.00 USD | 121.42 USD | 0.00 USD | `+3.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6465` | 17,020.00 USD | 410.21 USD | 0.00 USD | `+3.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6485` | 17,470.00 USD | 447.03 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6505` | 18,040.00 USD | 567.58 USD | 0.00 USD | `+4.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6525` | 18,210.00 USD | 172.51 USD | 0.00 USD | `+4.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6535` | 18,560.00 USD | 349.76 USD | 0.00 USD | `+5.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6555` | 22,640.00 USD | 4,080.00 USD | 0.00 USD | `+5.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6565` | 22,920.00 USD | 284.88 USD | 0.00 USD | `+5.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6585` | 24,360.00 USD | 1,440.00 USD | 0.00 USD | `+5.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6595` | 25,110.00 USD | 746.46 USD | 0.00 USD | `+5.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6605` | 25,690.00 USD | 580.23 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6645` | 25,950.00 USD | 262.60 USD | 0.00 USD | `+6.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6655` | 26,240.00 USD | 283.50 USD | 0.00 USD | `+6.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6675` | 26,530.00 USD | 290.78 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6685` | 26,700.00 USD | 170.95 USD | 0.00 USD | `+7.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6695` | 28,370.00 USD | 1,670.00 USD | 0.00 USD | `+7.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6705` | 28,530.00 USD | 162.91 USD | 0.00 USD | `+7.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6715` | 28,730.00 USD | 202.63 USD | 0.00 USD | `+7.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6725` | 30,410.00 USD | 1,670.00 USD | 0.00 USD | `+8.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6745` | 31,000.00 USD | 598.31 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6755` | 31,370.00 USD | 361.53 USD | 0.00 USD | `+8.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 33,490.00 USD | 2,130.00 USD | 0.00 USD | `+8.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6805` | 33,710.00 USD | 214.20 USD | 0.00 USD | `+9.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6815` | 44,270.00 USD | 10,560.00 USD | 0.00 USD | `+9.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6825` | 44,380.00 USD | 112.49 USD | 0.00 USD | `+9.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6835` | 44,490.00 USD | 108.41 USD | 0.00 USD | `+9.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6855` | 44,600.00 USD | 112.98 USD | 0.00 USD | `+10.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6865` | 44,890.00 USD | 292.33 USD | 0.00 USD | `+10.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6875` | 45,030.00 USD | 140.41 USD | 0.00 USD | `+10.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6885` | 45,550.00 USD | 514.80 USD | 0.00 USD | `+10.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6895` | 45,740.00 USD | 194.09 USD | 0.00 USD | `+10.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6915` | 45,850.00 USD | 101.96 USD | 0.00 USD | `+11.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6925` | 46,870.00 USD | 1,020.00 USD | 0.00 USD | `+11.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6945` | 47,480.00 USD | 610.10 USD | 0.00 USD | `+11.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6955` | 47,580.00 USD | 101.38 USD | 0.00 USD | `+11.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6965` | 48,370.00 USD | 789.18 USD | 0.00 USD | `+11.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6985` | 48,470.00 USD | 102.99 USD | 0.00 USD | `+12.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7005` | 48,580.00 USD | 111.08 USD | 0.00 USD | `+12.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7015` | 49,140.00 USD | 561.40 USD | 0.00 USD | `+12.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7085` | 50,090.00 USD | 947.29 USD | 0.00 USD | `+13.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7095` | 50,220.00 USD | 132.99 USD | 0.00 USD | `+14.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7115` | 50,350.00 USD | 122.04 USD | 0.00 USD | `+14.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7135` | 50,650.00 USD | 307.58 USD | 0.00 USD | `+14.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7165` | 52,490.00 USD | 1,830.00 USD | 0.00 USD | `+15.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7195` | 52,670.00 USD | 183.26 USD | 0.00 USD | `+15.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7205` | 52,820.00 USD | 147.15 USD | 0.00 USD | `+15.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7215` | 56,080.00 USD | 3,260.00 USD | 0.00 USD | `+15.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7225` | 56,230.00 USD | 150.08 USD | 0.00 USD | `+16.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7265` | 62,650.00 USD | 6,410.00 USD | 0.00 USD | `+16.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7325` | 62,810.00 USD | 165.17 USD | 0.00 USD | `+17.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7345` | 63,840.00 USD | 1,030.00 USD | 0.00 USD | `+18.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7375` | 63,950.00 USD | 106.75 USD | 0.00 USD | `+18.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7395` | 64,150.00 USD | 208.16 USD | 0.00 USD | `+18.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7405` | 64,890.00 USD | 733.09 USD | 0.00 USD | `+19.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7415` | 65,040.00 USD | 156.98 USD | 0.00 USD | `+19.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7425` | 65,180.00 USD | 132.95 USD | 0.00 USD | `+19.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7445` | 65,610.00 USD | 432.66 USD | 0.00 USD | `+19.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7455` | 67,780.00 USD | 2,170.00 USD | 0.00 USD | `+19.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7475` | 68,100.00 USD | 318.43 USD | 0.00 USD | `+20.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7505` | 68,240.00 USD | 141.39 USD | 0.00 USD | `+20.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7525` | 68,370.00 USD | 134.74 USD | 0.00 USD | `+20.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7565` | 72,490.00 USD | 4,120.00 USD | 0.00 USD | `+21.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7575` | 73,000.00 USD | 511.82 USD | 0.00 USD | `+21.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7585` | 73,130.00 USD | 135.82 USD | 0.00 USD | `+21.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7615` | 74,010.00 USD | 875.23 USD | 0.00 USD | `+22.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7635` | 74,110.00 USD | 103.35 USD | 0.00 USD | `+22.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7665` | 74,240.00 USD | 127.48 USD | 0.00 USD | `+23.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7675` | 74,340.00 USD | 101.61 USD | 0.00 USD | `+23.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7695` | 74,530.00 USD | 186.97 USD | 0.00 USD | `+23.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7705` | 74,640.00 USD | 109.43 USD | 0.00 USD | `+23.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7775` | 74,810.00 USD | 166.70 USD | 0.00 USD | `+24.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7815` | 75,940.00 USD | 1,140.00 USD | 0.00 USD | `+25.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7865` | 82,260.00 USD | 6,310.00 USD | 0.00 USD | `+26.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8095` | 82,390.00 USD | 133.42 USD | 0.00 USD | `+30.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8125` | 94,460.00 USD | 12,070.00 USD | 0.00 USD | `+30.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8335` | 95,390.00 USD | 929.08 USD | 0.00 USD | `+33.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8475` | 135,980.00 USD | 40,590.00 USD | 0.00 USD | `+36.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8505` | 152,720.00 USD | 16,740.00 USD | 0.00 USD | `+36.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8515` | 165,440.00 USD | 12,720.00 USD | 0.00 USD | `+36.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8525` | 177,220.00 USD | 11,780.00 USD | 0.00 USD | `+37.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8705` | 178,500.00 USD | 1,280.00 USD | 0.00 USD | `+39.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8725` | 178,660.00 USD | 159.86 USD | 0.00 USD | `+40.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 180,090.00 USD | 1,430.00 USD | 0.00 USD | `+44.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 180,280.00 USD | 193.62 USD | 0.00 USD | `+46.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 180,630.00 USD | 340.54 USD | 0.00 USD | `+52.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 180,770.00 USD | 145.72 USD | 0.00 USD | `+56.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 182,800.00 USD | 2,030.00 USD | 0.00 USD | `+58.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 182,940.00 USD | 136.10 USD | 0.00 USD | `+60.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 183,490.00 USD | 550.48 USD | 0.00 USD | `+60.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 183,800.00 USD | 314.99 USD | 0.00 USD | `+65.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 184,410.00 USD | 602.17 USD | 0.00 USD | `+68.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 184,770.00 USD | 360.61 USD | 0.00 USD | `+70.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 185,710.00 USD | 942.77 USD | 0.00 USD | `+73.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 186,050.00 USD | 337.31 USD | 0.00 USD | `+73.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 186,440.00 USD | 397.19 USD | 0.00 USD | `+76.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 186,970.00 USD | 525.37 USD | 0.00 USD | `+97.61%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.5320` | 827,200.00 USD | 0.00 USD | 827,200.00 USD | 11,240.00 USD | 0.00 USD | 3,480.00 USD |
| `7D` | `0.5340` | 812,480.00 USD | 0.00 USD | 812,480.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD |
| `7D` | `0.5360` | 809,880.00 USD | 0.00 USD | 809,880.00 USD | 2,440.00 USD | 3,040.00 USD | 0.00 USD |
| `7D` | `0.5380` | 804,400.00 USD | 0.00 USD | 804,400.00 USD | 0.00 USD | 1,550.00 USD | 2,940.00 USD |
| `7D` | `0.5420` | 799,910.00 USD | 0.00 USD | 799,910.00 USD | 7,660.00 USD | 1,290.00 USD | 2,950.00 USD |
| `7D` | `0.5440` | 788,010.00 USD | 0.00 USD | 788,010.00 USD | 0.00 USD | 1,150.00 USD | 6,970.00 USD |
| `7D` | `0.5460` | 779,890.00 USD | 0.00 USD | 779,890.00 USD | 2,250.00 USD | 3,030.00 USD | 5,190.00 USD |
| `7D` | `0.5480` | 769,420.00 USD | 0.00 USD | 769,420.00 USD | 2,000.00 USD | 795.70 USD | 4,470.00 USD |
| `1D` | `0.5500` | 801,260.00 USD | 0.00 USD | 801,260.00 USD | 0.00 USD | 0.00 USD | 19.90 USD |
| `7D` | `0.5500` | 762,150.00 USD | 0.00 USD | 762,150.00 USD | 5,990.00 USD | 1,440.00 USD | 6,710.00 USD |
| `1D` | `0.5510` | 801,240.00 USD | 0.00 USD | 801,240.00 USD | 0.00 USD | 0.00 USD | 849.87 USD |
| `1D` | `0.5520` | 800,390.00 USD | 0.00 USD | 800,390.00 USD | 0.00 USD | 0.00 USD | 432.53 USD |
| `7D` | `0.5520` | 748,010.00 USD | 0.00 USD | 748,010.00 USD | 4,110.00 USD | 1,920.00 USD | 1,880.00 USD |
| `1D` | `0.5530` | 799,960.00 USD | 0.00 USD | 799,960.00 USD | 1,260.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.5540` | 798,700.00 USD | 0.00 USD | 798,700.00 USD | 528.00 USD | 1,320.00 USD | 7.66 USD |
| `7D` | `0.5540` | 740,100.00 USD | 0.00 USD | 740,100.00 USD | 12,840.00 USD | 4,860.00 USD | 18,470.00 USD |
| `1D` | `0.5550` | 796,840.00 USD | 0.00 USD | 796,840.00 USD | 557.27 USD | 201.08 USD | 41.02 USD |
| `1D` | `0.5560` | 796,040.00 USD | 0.00 USD | 796,040.00 USD | 0.00 USD | 0.00 USD | 479.50 USD |
| `7D` | `0.5560` | 703,930.00 USD | 0.00 USD | 703,930.00 USD | 13,490.00 USD | 1,920.00 USD | 6,250.00 USD |
| `1D` | `0.5570` | 795,560.00 USD | 0.00 USD | 795,560.00 USD | 0.00 USD | 1,940.00 USD | 2,320.00 USD |
| `1D` | `0.5580` | 791,300.00 USD | 0.00 USD | 791,300.00 USD | 1,100.00 USD | 2,960.00 USD | 1,240.00 USD |
| `7D` | `0.5580` | 682,270.00 USD | 0.00 USD | 682,270.00 USD | 6,000.00 USD | 6,820.00 USD | 18,300.00 USD |
| `1D` | `0.5590` | 786,000.00 USD | 0.00 USD | 786,000.00 USD | 0.00 USD | 1,080.00 USD | 15.63 USD |
| `1D` | `0.5600` | 784,910.00 USD | 0.00 USD | 784,910.00 USD | 1,550.00 USD | 1,830.00 USD | 0.00 USD |
| `7D` | `0.5600` | 651,160.00 USD | 0.00 USD | 651,160.00 USD | 4,070.00 USD | 8,160.00 USD | 2,500.00 USD |
| `1D` | `0.5610` | 781,530.00 USD | 0.00 USD | 781,530.00 USD | 0.00 USD | 0.00 USD | 772.54 USD |
| `1D` | `0.5620` | 780,750.00 USD | 0.00 USD | 780,750.00 USD | 0.00 USD | 776.64 USD | 2,180.00 USD |
| `7D` | `0.5620` | 636,430.00 USD | 0.00 USD | 636,430.00 USD | 19,480.00 USD | 7,420.00 USD | 11,550.00 USD |
| `1D` | `0.5630` | 777,800.00 USD | 0.00 USD | 777,800.00 USD | 0.00 USD | 1,560.00 USD | 4,600.00 USD |
| `1D` | `0.5640` | 771,630.00 USD | 0.00 USD | 771,630.00 USD | 4,020.00 USD | 2,420.00 USD | 12.64 USD |
| `7D` | `0.5640` | 597,980.00 USD | 0.00 USD | 597,980.00 USD | 2,950.00 USD | 741.21 USD | 27.20 USD |
| `7D` | `0.5660` | 594,270.00 USD | 0.00 USD | 594,270.00 USD | 11,490.00 USD | 2,990.00 USD | 4,430.00 USD |
| `7D` | `0.5680` | 575,370.00 USD | 0.00 USD | 575,370.00 USD | 5,100.00 USD | 0.00 USD | 2,890.00 USD |
| `7D` | `0.5700` | 567,380.00 USD | 0.00 USD | 567,380.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD |
| `1D` | `0.5710` | 765,180.00 USD | 0.00 USD | 765,180.00 USD | 0.00 USD | 2,350.00 USD | 0.00 USD |
| `7D` | `0.5720` | 564,800.00 USD | 0.00 USD | 564,800.00 USD | 0.00 USD | 4,370.00 USD | 1,360.00 USD |
| `7D` | `0.5740` | 559,070.00 USD | 0.00 USD | 559,070.00 USD | 21,620.00 USD | 1,100.00 USD | 1,610.00 USD |
| `7D` | `0.5760` | 534,730.00 USD | 0.00 USD | 534,730.00 USD | 2,150.00 USD | 0.00 USD | 19.23 USD |
| `1D` | `0.5770` | 762,820.00 USD | 0.00 USD | 762,820.00 USD | 0.00 USD | 0.00 USD | 34.98 USD |
| `1D` | `0.5780` | 762,790.00 USD | 0.00 USD | 762,790.00 USD | 0.00 USD | 0.00 USD | 59.63 USD |
| `7D` | `0.5780` | 532,560.00 USD | 0.00 USD | 532,560.00 USD | 0.00 USD | 0.00 USD | 1,570.00 USD |
| `7D` | `0.5800` | 530,990.00 USD | 0.00 USD | 530,990.00 USD | 1,610.00 USD | 0.00 USD | 2,850.00 USD |
| `1D` | `0.5820` | 762,730.00 USD | 0.00 USD | 762,730.00 USD | 0.00 USD | 1,000.00 USD | 0.00 USD |
| `7D` | `0.5820` | 526,530.00 USD | 0.00 USD | 526,530.00 USD | 0.00 USD | 0.00 USD | 6,520.00 USD |
| `1D` | `0.5830` | 761,730.00 USD | 0.00 USD | 761,730.00 USD | 0.00 USD | 0.00 USD | 24.36 USD |
| `1D` | `0.5840` | 761,700.00 USD | 0.00 USD | 761,700.00 USD | 0.00 USD | 0.00 USD | 44.63 USD |
| `1D` | `0.5850` | 761,660.00 USD | 0.00 USD | 761,660.00 USD | 0.00 USD | 0.00 USD | 18.95 USD |
| `1D` | `0.5860` | 761,640.00 USD | 0.00 USD | 761,640.00 USD | 0.00 USD | 658.88 USD | 14,870.00 USD |
| `7D` | `0.5860` | 520,010.00 USD | 0.00 USD | 520,010.00 USD | 0.00 USD | 0.00 USD | 146.30 USD |
| `1D` | `0.5870` | 746,110.00 USD | 0.00 USD | 746,110.00 USD | 2,890.00 USD | 631.19 USD | 3,500.00 USD |
| `1D` | `0.5880` | 739,090.00 USD | 0.00 USD | 739,090.00 USD | 1,270.00 USD | 1,580.00 USD | 3,700.00 USD |
| `7D` | `0.5880` | 519,870.00 USD | 0.00 USD | 519,870.00 USD | 3,110.00 USD | 1,400.00 USD | 65.70 USD |
| `1D` | `0.5890` | 732,550.00 USD | 0.00 USD | 732,550.00 USD | 3,460.00 USD | 0.00 USD | 7.65 USD |
| `1D` | `0.5900` | 729,080.00 USD | 0.00 USD | 729,080.00 USD | 4,730.00 USD | 1,390.00 USD | 3.61 USD |
| `7D` | `0.5900` | 515,290.00 USD | 0.00 USD | 515,290.00 USD | 3,120.00 USD | 1,560.00 USD | 15.37 USD |
| `1D` | `0.5910` | 722,960.00 USD | 0.00 USD | 722,960.00 USD | 0.00 USD | 1,820.00 USD | 4,100.00 USD |
| `1D` | `0.5920` | 717,040.00 USD | 0.00 USD | 717,040.00 USD | 11,320.00 USD | 3,660.00 USD | 7,780.00 USD |
| `7D` | `0.5920` | 510,600.00 USD | 0.00 USD | 510,600.00 USD | 11,690.00 USD | 2,820.00 USD | 6,030.00 USD |
| `1D` | `0.5930` | 694,290.00 USD | 0.00 USD | 694,290.00 USD | 3,420.00 USD | 2,150.00 USD | 5,760.00 USD |
| `1D` | `0.5940` | 682,960.00 USD | 0.00 USD | 682,960.00 USD | 5,890.00 USD | 6,830.00 USD | 10,090.00 USD |
| `7D` | `0.5940` | 490,060.00 USD | 0.00 USD | 490,060.00 USD | 10,090.00 USD | 0.00 USD | 9,780.00 USD |
| `1D` | `0.5950` | 660,150.00 USD | 0.00 USD | 660,150.00 USD | 19,520.00 USD | 12,400.00 USD | 1,950.00 USD |
| `1D` | `0.5960` | 626,280.00 USD | 0.00 USD | 626,280.00 USD | 8,460.00 USD | 3,150.00 USD | 13,330.00 USD |
| `7D` | `0.5960` | 470,190.00 USD | 0.00 USD | 470,190.00 USD | 18,180.00 USD | 18,410.00 USD | 13,390.00 USD |
| `1D` | `0.5970` | 601,330.00 USD | 0.00 USD | 601,330.00 USD | 9,250.00 USD | 7,060.00 USD | 6,690.00 USD |
| `1D` | `0.5980` | 578,330.00 USD | 0.00 USD | 578,330.00 USD | 6,400.00 USD | 1,740.00 USD | 41,000.00 USD |
| `7D` | `0.5980` | 420,210.00 USD | 0.00 USD | 420,210.00 USD | 20,380.00 USD | 826.53 USD | 19,920.00 USD |
| `1D` | `0.5990` | 529,180.00 USD | 0.00 USD | 529,180.00 USD | 18,690.00 USD | 2,370.00 USD | 13,440.00 USD |
| `1D` | `0.6000` | 494,670.00 USD | 0.00 USD | 494,670.00 USD | 0.00 USD | 5,920.00 USD | 1,130.00 USD |
| `7D` | `0.6000` | 379,080.00 USD | 0.00 USD | 379,080.00 USD | 3,320.00 USD | 2,140.00 USD | 18,810.00 USD |
| `1D` | `0.6010` | 487,630.00 USD | 0.00 USD | 487,630.00 USD | 735.24 USD | 461.96 USD | 11,400.00 USD |
| `1D` | `0.6020` | 475,030.00 USD | 0.00 USD | 475,030.00 USD | 30,900.00 USD | 13,240.00 USD | 2,020.00 USD |
| `7D` | `0.6020` | 354,810.00 USD | 0.00 USD | 354,810.00 USD | 23,960.00 USD | 8,040.00 USD | 4,060.00 USD |
| `1D` | `0.6030` | 428,870.00 USD | 0.00 USD | 428,870.00 USD | 10,880.00 USD | 6,850.00 USD | 24.50 USD |
| `1D` | `0.6040` | 411,110.00 USD | 0.00 USD | 411,110.00 USD | 19,810.00 USD | 2,320.00 USD | 21.93 USD |
| `7D` | `0.6040` | 318,760.00 USD | 0.00 USD | 318,760.00 USD | 8,620.00 USD | 7,530.00 USD | 7,920.00 USD |
| `1D` | `0.6050` | 388,960.00 USD | 0.00 USD | 388,960.00 USD | 0.00 USD | 3,770.00 USD | 20,130.00 USD |
| `1D` | `0.6060` | 365,050.00 USD | 0.00 USD | 365,050.00 USD | 8,500.00 USD | 4,900.00 USD | 7,980.00 USD |
| `7D` | `0.6060` | 294,690.00 USD | 0.00 USD | 294,690.00 USD | 0.00 USD | 0.00 USD | 227.43 USD |
| `1D` | `0.6070` | 343,680.00 USD | 0.00 USD | 343,680.00 USD | 7,700.00 USD | 14,690.00 USD | 11,220.00 USD |
| `1D` | `0.6080` | 310,070.00 USD | 0.00 USD | 310,070.00 USD | 2,970.00 USD | 23,150.00 USD | 0.00 USD |
| `7D` | `0.6080` | 294,460.00 USD | 0.00 USD | 294,460.00 USD | 2,860.00 USD | 0.00 USD | 9,370.00 USD |
| `1D` | `0.6090` | 283,950.00 USD | 0.00 USD | 283,950.00 USD | 6,430.00 USD | 11,280.00 USD | 14,240.00 USD |
| `1D` | `0.6100` | 252,010.00 USD | 0.00 USD | 252,010.00 USD | 14,420.00 USD | 11,860.00 USD | 4,550.00 USD |
| `7D` | `0.6100` | 282,230.00 USD | 0.00 USD | 282,230.00 USD | 21,400.00 USD | 47,430.00 USD | 25,300.00 USD |
| `1D` | `0.6110` | 221,180.00 USD | 0.00 USD | 221,180.00 USD | 1,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6120` | 219,750.00 USD | 0.00 USD | 219,750.00 USD | 23,580.00 USD | 2,470.00 USD | 19,200.00 USD |
| `7D` | `0.6120` | 188,090.00 USD | 0.00 USD | 188,090.00 USD | 35,760.00 USD | 5,720.00 USD | 18,510.00 USD |
| `1D` | `0.6130` | 174,500.00 USD | 0.00 USD | 174,500.00 USD | 2,140.00 USD | 12,430.00 USD | 22,770.00 USD |
| `1D` | `0.6140` | 137,150.00 USD | 0.00 USD | 137,150.00 USD | 53,460.00 USD | 18,080.00 USD | 4,040.00 USD |
| `7D` | `0.6140` | 128,100.00 USD | 0.00 USD | 128,100.00 USD | 51,550.00 USD | 8,040.00 USD | 10,780.00 USD |
| `1D` | `0.6150` | 61,570.00 USD | 0.00 USD | 61,570.00 USD | 14,190.00 USD | 7,820.00 USD | 0.00 USD |
| `1D` | `0.6160` | 39,560.00 USD | 0.00 USD | 39,560.00 USD | 25,650.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6160` | 57,720.00 USD | 0.00 USD | 57,720.00 USD | 12,920.00 USD | 16,340.00 USD | 4,760.00 USD |
| `1D` | `0.6170` | 13,910.00 USD | 0.00 USD | 13,910.00 USD | 0.00 USD | 0.00 USD | 13,910.00 USD |
| `7D` | `0.6180` | 23,710.00 USD | 0.00 USD | 23,710.00 USD | 20,870.00 USD | 2,610.00 USD | 228.92 USD |
| `1D` | `0.6190` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6190` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6200` | 42,100.00 USD | 42,100.00 USD | 0.00 USD | 23,430.00 USD | 0.00 USD | 18,670.00 USD |
| `7D` | `0.6220` | 69,720.00 USD | 69,720.00 USD | 0.00 USD | 4,760.00 USD | 22,640.00 USD | 215.59 USD |
| `7D` | `0.6240` | 69,900.00 USD | 69,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 171.81 USD |
| `7D` | `0.6260` | 137,210.00 USD | 137,210.00 USD | 0.00 USD | 67,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6290` | 2,020.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD | 0.00 USD |
| `7D` | `0.6300` | 147,130.00 USD | 147,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,920.00 USD |
| `1D` | `0.6310` | 28,950.00 USD | 28,950.00 USD | 0.00 USD | 11,740.00 USD | 3,970.00 USD | 11,220.00 USD |
| `1D` | `0.6320` | 60,910.00 USD | 60,910.00 USD | 0.00 USD | 31,880.00 USD | 0.00 USD | 78.00 USD |
| `7D` | `0.6320` | 147,500.00 USD | 147,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 369.35 USD |
| `1D` | `0.6330` | 116,870.00 USD | 116,870.00 USD | 0.00 USD | 17,300.00 USD | 5,390.00 USD | 33,280.00 USD |
| `1D` | `0.6340` | 185,410.00 USD | 185,410.00 USD | 0.00 USD | 32,460.00 USD | 0.00 USD | 36,080.00 USD |
| `7D` | `0.6340` | 216,540.00 USD | 216,540.00 USD | 0.00 USD | 68,660.00 USD | 0.00 USD | 381.22 USD |
| `1D` | `0.6350` | 243,910.00 USD | 243,910.00 USD | 0.00 USD | 51,360.00 USD | 0.00 USD | 7,130.00 USD |
| `1D` | `0.6360` | 373,650.00 USD | 373,650.00 USD | 0.00 USD | 63,010.00 USD | 2,470.00 USD | 64,260.00 USD |
| `7D` | `0.6360` | 307,840.00 USD | 307,840.00 USD | 0.00 USD | 34,320.00 USD | 0.00 USD | 56,980.00 USD |
| `1D` | `0.6370` | 409,530.00 USD | 409,530.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD | 30,110.00 USD |
| `1D` | `0.6380` | 433,770.00 USD | 433,770.00 USD | 0.00 USD | 0.00 USD | 19,010.00 USD | 5,220.00 USD |
| `7D` | `0.6380` | 346,930.00 USD | 346,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39,090.00 USD |
| `1D` | `0.6390` | 503,230.00 USD | 503,230.00 USD | 0.00 USD | 18,790.00 USD | 3,690.00 USD | 47,000.00 USD |
| `1D` | `0.6400` | 619,220.00 USD | 619,220.00 USD | 0.00 USD | 57,170.00 USD | 28,050.00 USD | 30,770.00 USD |
| `7D` | `0.6400` | 367,450.00 USD | 367,450.00 USD | 0.00 USD | 0.00 USD | 7,510.00 USD | 13,010.00 USD |
| `1D` | `0.6410` | 668,360.00 USD | 668,360.00 USD | 0.00 USD | 32,400.00 USD | 9,300.00 USD | 7,440.00 USD |
| `1D` | `0.6420` | 771,930.00 USD | 771,930.00 USD | 0.00 USD | 69,490.00 USD | 14,860.00 USD | 19,230.00 USD |
| `7D` | `0.6420` | 474,760.00 USD | 474,760.00 USD | 0.00 USD | 55,350.00 USD | 35,430.00 USD | 16,530.00 USD |
| `1D` | `0.6430` | 850,850.00 USD | 850,850.00 USD | 0.00 USD | 35,700.00 USD | 15,580.00 USD | 27,640.00 USD |
| `1D` | `0.6440` | 963,600.00 USD | 963,600.00 USD | 0.00 USD | 39,760.00 USD | 23,720.00 USD | 49,280.00 USD |
| `7D` | `0.6440` | 562,140.00 USD | 562,140.00 USD | 0.00 USD | 44,690.00 USD | 24,820.00 USD | 17,870.00 USD |
| `1D` | `0.6450` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 70,250.00 USD | 9,920.00 USD | 36,640.00 USD |
| `1D` | `0.6460` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 57,400.00 USD | 9,320.00 USD | 7,110.00 USD |
| `7D` | `0.6460` | 919,670.00 USD | 919,670.00 USD | 0.00 USD | 172,610.00 USD | 46,630.00 USD | 138,290.00 USD |
| `1D` | `0.6470` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 74,410.00 USD | 16,010.00 USD | 2,300.00 USD |
| `1D` | `0.6480` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 112,500.00 USD | 6,780.00 USD | 151.61 USD |
| `7D` | `0.6480` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 86,440.00 USD | 26,520.00 USD | 33,000.00 USD |
| `1D` | `0.6490` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 66,830.00 USD | 1,230.00 USD | 9,740.00 USD |
| `1D` | `0.6500` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 64,920.00 USD | 5,920.00 USD | 128.67 USD |
| `7D` | `0.6500` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 73,560.00 USD | 0.00 USD | 132,400.00 USD |
| `1D` | `0.6510` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 55,500.00 USD | 0.00 USD | 11,510.00 USD |
| `1D` | `0.6520` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 93,550.00 USD | 9,040.00 USD | 2,020.00 USD |
| `7D` | `0.6520` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 298,050.00 USD | 10,910.00 USD | 104,780.00 USD |
| `1D` | `0.6530` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 11,510.00 USD | 3,910.00 USD | 0.00 USD |
| `1D` | `0.6540` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 24,280.00 USD | 0.00 USD | 10,560.00 USD |
| `7D` | `0.6540` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 15,730.00 USD | 4,440.00 USD | 61,750.00 USD |
| `1D` | `0.6550` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,950.00 USD |
| `1D` | `0.6560` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD |
| `7D` | `0.6560` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 5,380.00 USD | 847.61 USD |
| `1D` | `0.6570` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 59.54 USD |
| `1D` | `0.6580` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 3,310.00 USD | 25.28 USD |
| `7D` | `0.6580` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 28,280.00 USD | 9,690.00 USD |
| `1D` | `0.6590` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 5,890.00 USD | 164.02 USD |
| `1D` | `0.6600` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 8,400.00 USD | 59.63 USD |
| `7D` | `0.6600` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 15,500.00 USD | 580.13 USD |
| `1D` | `0.6610` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 142.10 USD |
| `1D` | `0.6620` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,710.00 USD |
| `7D` | `0.6620` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 128.16 USD |
| `1D` | `0.6630` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39.16 USD |
| `1D` | `0.6640` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 11,190.00 USD | 0.00 USD | 126.28 USD |
| `7D` | `0.6640` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 33,660.00 USD | 0.00 USD | 534.34 USD |
| `1D` | `0.6650` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 3,160.00 USD | 17,420.00 USD |
| `1D` | `0.6660` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,410.00 USD |
| `7D` | `0.6660` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 6,770.00 USD | 436.87 USD |
| `1D` | `0.6670` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 18,850.00 USD | 0.00 USD | 24.36 USD |
| `1D` | `0.6680` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44.63 USD |
| `7D` | `0.6680` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 308.18 USD |
| `1D` | `0.6690` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 3,550.00 USD | 4,410.00 USD |
| `1D` | `0.6700` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 8,830.00 USD | 1,920.00 USD | 24,760.00 USD |
| `7D` | `0.6700` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 966.49 USD |
| `1D` | `0.6710` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 41,970.00 USD | 0.00 USD | 5,950.00 USD |
| `7D` | `0.6720` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 58,470.00 USD | 0.00 USD | 30,140.00 USD |
| `1D` | `0.6730` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 24,320.00 USD | 3,670.00 USD | 4,560.00 USD |
| `1D` | `0.6740` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 64,370.00 USD | 7,120.00 USD | 9,210.00 USD |
| `7D` | `0.6740` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 39,730.00 USD | 0.00 USD | 99.42 USD |
| `1D` | `0.6750` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 28,700.00 USD | 4,300.00 USD | 12,070.00 USD |
| `1D` | `0.6760` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.6760` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 77,970.00 USD | 33,090.00 USD |
| `1D` | `0.6770` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 14,540.00 USD | 6,110.00 USD | 14,290.00 USD |
| `1D` | `0.6780` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 33,610.00 USD | 12,680.00 USD | 8,710.00 USD |
| `7D` | `0.6780` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 63,600.00 USD | 14,400.00 USD | 17,930.00 USD |
| `1D` | `0.6790` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 18,610.00 USD | 14,580.00 USD |
| `1D` | `0.6800` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,450.00 USD |
| `7D` | `0.6800` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 0.00 USD |
| `1D` | `0.6810` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 1,940.00 USD | 9,870.00 USD |
| `1D` | `0.6820` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 22,600.00 USD | 16,590.00 USD | 7,740.00 USD |
| `7D` | `0.6820` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 32,570.00 USD | 53,450.00 USD | 145.79 USD |
| `1D` | `0.6830` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 24,570.00 USD | 26,560.00 USD | 36,830.00 USD |
| `1D` | `0.6840` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 45,780.00 USD | 25,860.00 USD | 11,350.00 USD |
| `7D` | `0.6840` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 57,890.00 USD | 54,300.00 USD | 102,430.00 USD |
| `1D` | `0.6850` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 51,090.00 USD | 5,780.00 USD | 10,620.00 USD |
| `1D` | `0.6860` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 40,250.00 USD | 4,380.00 USD | 14,780.00 USD |
| `7D` | `0.6860` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 49,930.00 USD | 14,540.00 USD | 10,480.00 USD |
| `1D` | `0.6870` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 63,220.00 USD | 1,160.00 USD | 3,830.00 USD |
| `1D` | `0.6880` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 14,350.00 USD | 11,160.00 USD | 25,380.00 USD |
| `7D` | `0.6880` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 38,030.00 USD | 17,300.00 USD | 0.00 USD |
| `1D` | `0.6890` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,340.00 USD |
| `1D` | `0.6900` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 18,600.00 USD | 4,030.00 USD | 21,060.00 USD |
| `7D` | `0.6900` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 15,510.00 USD | 16,550.00 USD |
| `1D` | `0.6910` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 28,860.00 USD | 1,730.00 USD | 39,760.00 USD |
| `1D` | `0.6920` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 16,800.00 USD | 0.00 USD | 13,680.00 USD |
| `7D` | `0.6920` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 69,620.00 USD | 2,090.00 USD | 62,020.00 USD |
| `1D` | `0.6930` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 10,030.00 USD | 0.00 USD | 168.16 USD |
| `1D` | `0.6940` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 11,230.00 USD | 2,090.00 USD | 9,470.00 USD |
| `7D` | `0.6940` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 14,220.00 USD | 0.00 USD | 42,600.00 USD |
| `1D` | `0.6950` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 22,480.00 USD | 4,460.00 USD | 3,790.00 USD |
| `1D` | `0.6960` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 58,370.00 USD | 6,000.00 USD | 0.00 USD |
| `7D` | `0.6960` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 59,960.00 USD | 0.00 USD | 12,390.00 USD |
| `1D` | `0.6970` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 33,460.00 USD | 4,780.00 USD | 34.66 USD |
| `1D` | `0.6980` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 9,140.00 USD | 4,100.00 USD | 1,290.00 USD |
| `7D` | `0.6980` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 35,980.00 USD | 16,990.00 USD | 0.00 USD |
| `1D` | `0.6990` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 5,180.00 USD | 4,830.00 USD | 5,380.00 USD |
| `1D` | `0.7000` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 18,240.00 USD | 4,020.00 USD | 16,170.00 USD |
| `7D` | `0.7000` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 29,740.00 USD | 0.00 USD | 40,190.00 USD |
| `1D` | `0.7010` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 15,520.00 USD | 0.00 USD | 73.64 USD |
| `1D` | `0.7020` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 14,360.00 USD | 0.00 USD | 22.18 USD |
| `7D` | `0.7020` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 29,810.00 USD | 0.00 USD | 53,230.00 USD |
| `1D` | `0.7030` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 4,330.00 USD | 0.00 USD | 10,510.00 USD |
| `1D` | `0.7040` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 29,930.00 USD | 2,630.00 USD | 8,760.00 USD |
| `7D` | `0.7040` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 95,520.00 USD | 0.00 USD | 96,250.00 USD |
| `1D` | `0.7050` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 29,790.00 USD | 2,660.00 USD | 18,990.00 USD |
| `1D` | `0.7060` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 8,590.00 USD | 3,860.00 USD | 13,370.00 USD |
| `7D` | `0.7060` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 47,840.00 USD | 33,490.00 USD | 178,200.00 USD |
| `1D` | `0.7070` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 19,980.00 USD | 21,860.00 USD | 17,530.00 USD |
| `1D` | `0.7080` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 18,420.00 USD | 0.00 USD | 228.82 USD |
| `7D` | `0.7080` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 24,440.00 USD | 64,870.00 USD | 82,560.00 USD |
| `7D` | `0.7100` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 150,830.00 USD | 63,530.00 USD | 148,790.00 USD |
| `7D` | `0.7120` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 101,040.00 USD | 78,760.00 USD | 228,080.00 USD |
| `7D` | `0.7140` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 202,560.00 USD | 67,260.00 USD | 133,230.00 USD |
| `7D` | `0.7160` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 113,040.00 USD | 65,260.00 USD | 164,360.00 USD |
| `7D` | `0.7180` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 165,860.00 USD | 56,910.00 USD | 66,540.00 USD |
| `7D` | `0.7200` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 93,750.00 USD | 45,160.00 USD | 177,940.00 USD |
| `7D` | `0.7220` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 318,420.00 USD | 67,130.00 USD | 98,130.00 USD |
| `7D` | `0.7240` | 6,680,000.00 USD | 6,680,000.00 USD | 0.00 USD | 146,110.00 USD | 24,910.00 USD | 128,950.00 USD |
| `7D` | `0.7260` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 106,410.00 USD | 52,120.00 USD | 175,450.00 USD |
| `7D` | `0.7280` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 99,750.00 USD | 40,180.00 USD | 83,870.00 USD |
| `7D` | `0.7300` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 115,310.00 USD | 60,310.00 USD | 109,420.00 USD |
| `7D` | `0.7320` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 189,840.00 USD | 65,640.00 USD | 80,460.00 USD |
| `7D` | `0.7340` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 31,260.00 USD | 8,620.00 USD | 63,250.00 USD |
| `7D` | `0.7360` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 103,600.00 USD | 46,790.00 USD | 35,030.00 USD |
| `7D` | `0.7380` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 73,710.00 USD | 19,000.00 USD | 60,620.00 USD |
| `7D` | `0.7400` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 1,730.00 USD | 4,760.00 USD | 20,970.00 USD |
| `7D` | `0.7420` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 35,810.00 USD | 35,860.00 USD | 31,380.00 USD |
| `7D` | `0.7440` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 74,450.00 USD | 39,890.00 USD | 70,380.00 USD |
| `7D` | `0.7460` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 88,800.00 USD | 28,800.00 USD | 51,780.00 USD |
| `7D` | `0.7480` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 60,580.00 USD | 28,900.00 USD | 38,290.00 USD |
| `7D` | `0.7500` | 9,010,000.00 USD | 9,010,000.00 USD | 0.00 USD | 52,320.00 USD | 12,610.00 USD | 25,140.00 USD |
| `7D` | `0.7520` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 53,470.00 USD | 13,000.00 USD | 50,770.00 USD |
| `7D` | `0.7540` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 30,340.00 USD | 1,890.00 USD | 25,430.00 USD |
| `7D` | `0.7560` | 9,240,000.00 USD | 9,240,000.00 USD | 0.00 USD | 26,000.00 USD | 7,570.00 USD | 22,260.00 USD |
| `7D` | `0.7580` | 9,350,000.00 USD | 9,350,000.00 USD | 0.00 USD | 55,420.00 USD | 11,790.00 USD | 45,930.00 USD |
| `7D` | `0.7600` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 57,020.00 USD | 4,320.00 USD | 80,740.00 USD |
| `7D` | `0.7620` | 9,590,000.00 USD | 9,590,000.00 USD | 0.00 USD | 54,140.00 USD | 24,170.00 USD | 21,540.00 USD |
| `7D` | `0.7640` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 50,390.00 USD | 13,520.00 USD | 41,540.00 USD |
| `7D` | `0.7660` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 56,130.00 USD | 18,130.00 USD | 91,090.00 USD |
| `7D` | `0.7680` | 10,000,000.00 USD | 10,000,000.00 USD | 0.00 USD | 66,570.00 USD | 32,520.00 USD | 41,010.00 USD |
| `7D` | `0.7700` | 10,070,000.00 USD | 10,070,000.00 USD | 0.00 USD | 10,860.00 USD | 12,600.00 USD | 41,730.00 USD |
| `7D` | `0.7720` | 10,190,000.00 USD | 10,190,000.00 USD | 0.00 USD | 58,380.00 USD | 32,920.00 USD | 25,780.00 USD |
| `7D` | `0.7740` | 10,300,000.00 USD | 10,300,000.00 USD | 0.00 USD | 51,600.00 USD | 25,250.00 USD | 35,740.00 USD |
| `7D` | `0.7760` | 10,350,000.00 USD | 10,350,000.00 USD | 0.00 USD | 38,170.00 USD | 2,980.00 USD | 12,740.00 USD |
| `7D` | `0.7780` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 68,800.00 USD | 20,860.00 USD | 32,580.00 USD |
| `7D` | `0.7800` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 60,490.00 USD | 21,940.00 USD | 80,690.00 USD |
| `7D` | `0.7820` | 10,750,000.00 USD | 10,750,000.00 USD | 0.00 USD | 90,020.00 USD | 17,850.00 USD | 6,240.00 USD |
| `7D` | `0.7840` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 72,650.00 USD | 7,150.00 USD | 2,180.00 USD |
| `7D` | `0.7860` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 32,690.00 USD | 9,290.00 USD | 31,500.00 USD |
| `7D` | `0.7880` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 11,900.00 USD | 10,710.00 USD | 22,510.00 USD |
| `7D` | `0.7900` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 44,050.00 USD | 16,710.00 USD | 17,430.00 USD |
| `7D` | `0.7910` | 11,070,000.00 USD | 11,070,000.00 USD | 0.00 USD | 30,620.00 USD | 5,860.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `87.35M` | Total OI Tokens: `140,471,075.9 APT`
  * 1h OI Change: `-2.26%` | 4h OI Change: `-9.21%` | 24h OI Change: `-12.91%`
  * Exchange Breakdown: Binance=`16.03M` | Bybit=`17.76M` | OKX=`4.19M` | Hyperliquid=`3.55M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-1.01K` | Last 24h: `8.88K` | Last 3d: `10.89K` | Last 7d: `5.22K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0072%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0019%` | **USDT KuCoin** | `0.0070%` |
| **USDT MEXC** | `-0.0071%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0015%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `APT` | `59.08%` | `40.92%` | `1.44` | 2,270,000.00 USD |
| `15M` | `Binance` | `48.61%` | `51.39%` | `0.95` | 689,300.00 USD |
| `15M` | `OKX` | `41.9%` | `58.1%` | `0.72` | 273,430.00 USD |
| `15M` | `Bybit` | `55.82%` | `44.18%` | `1.26` | 172,150.00 USD |
| `15M` | `KuCoin` | `50.51%` | `49.49%` | `1.02` | 166,160.00 USD |
| `15M` | `Gate` | `42.76%` | `57.24%` | `0.75` | 61,930.00 USD |
| `15M` | `Bitget` | `51.06%` | `48.94%` | `1.04` | 33,410.00 USD |
| `15M` | `BingX` | `96.16%` | `3.84%` | `25.04` | 474,770.00 USD |
| `15M` | `MEXC` | `50.35%` | `49.65%` | `1.01` | 67,600.00 USD |
| `15M` | `Bitunix` | `66.4%` | `33.6%` | `1.98` | 37,050.00 USD |
| `15M` | `Hyperliquid` | `41.52%` | `58.48%` | `0.71` | 99,140.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.56%` | `49.44%` | `1.02` | 79,250.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `63.54%` | `36.46%` | `1.74` | 115,620.00 USD |
| `15M` | `HTX` | `53.21%` | `46.79%` | `1.14` | 293.48 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `19.1%` | `80.9%` | `0.24` | 5,760.00 USD |
| `15M` | `Aster` | `42.11%` | `57.89%` | `0.73` | 72.40 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `97.88%` | `2.12%` | `46.17` | 466.57 USD |
| `15M` | `Whale Positions` | `48.61%` | `51.39%` | `0.95` | 689,300.00 USD |
| `15M` | `Global Accounts` | `59.08%` | `40.92%` | `1.44` | 2,270,000.00 USD |
| `1H` | `APT` | `50.54%` | `49.46%` | `1.02` | 10,920,000.00 USD |
| `1H` | `Binance` | `48.14%` | `51.86%` | `0.93` | 4,530,000.00 USD |
| `1H` | `OKX` | `46.95%` | `53.05%` | `0.89` | 980,190.00 USD |
| `1H` | `Bybit` | `53.51%` | `46.49%` | `1.15` | 945,930.00 USD |
| `1H` | `KuCoin` | `50.5%` | `49.5%` | `1.02` | 713,060.00 USD |
| `1H` | `Gate` | `40.2%` | `59.8%` | `0.67` | 248,320.00 USD |
| `1H` | `Bitget` | `47.58%` | `52.42%` | `0.91` | 336,380.00 USD |
| `1H` | `BingX` | `74.02%` | `25.98%` | `2.85` | 1,190,000.00 USD |
| `1H` | `MEXC` | `47.91%` | `52.09%` | `0.92` | 540,440.00 USD |
| `1H` | `Bitunix` | `22.72%` | `77.28%` | `0.29` | 302,290.00 USD |
| `1H` | `Hyperliquid` | `29.18%` | `70.82%` | `0.41` | 330,280.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.41%` | `49.59%` | `1.02` | 311,820.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `59.83%` | `40.17%` | `1.49` | 445,720.00 USD |
| `1H` | `HTX` | `32.97%` | `67.03%` | `0.49` | 1,290.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `50.95%` | `49.05%` | `1.04` | 31,350.00 USD |
| `1H` | `Aster` | `29.92%` | `70.08%` | `0.43` | 2,040.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `97.17%` | `2.83%` | `34.34` | 1,650.00 USD |
| `1H` | `Whale Positions` | `48.14%` | `51.86%` | `0.93` | 4,530,000.00 USD |
| `1H` | `Global Accounts` | `50.54%` | `49.46%` | `1.02` | 10,920,000.00 USD |
| `4H` | `APT` | `44.77%` | `55.23%` | `0.81` | 122,610,000.00 USD |
| `4H` | `Binance` | `45.1%` | `54.9%` | `0.82` | 50,090,000.00 USD |
| `4H` | `OKX` | `48.32%` | `51.68%` | `0.93` | 16,510,000.00 USD |
| `4H` | `Bybit` | `47.8%` | `52.2%` | `0.92` | 12,370,000.00 USD |
| `4H` | `KuCoin` | `49.01%` | `50.99%` | `0.96` | 2,500,000.00 USD |
| `4H` | `Gate` | `49.55%` | `50.45%` | `0.98` | 3,010,000.00 USD |
| `4H` | `Bitget` | `46.03%` | `53.97%` | `0.85` | 4,810,000.00 USD |
| `4H` | `BingX` | `29.07%` | `70.93%` | `0.41` | 2,640,000.00 USD |
| `4H` | `MEXC` | `41.89%` | `58.11%` | `0.72` | 1,820,000.00 USD |
| `4H` | `Bitunix` | `41.79%` | `58.21%` | `0.72` | 4,060,000.00 USD |
| `4H` | `Hyperliquid` | `43.06%` | `56.94%` | `0.76` | 1,480,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.89%` | `52.11%` | `0.92` | 19,390,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 5,430.00 USD |
| `4H` | `WhiteBIT` | `48.48%` | `51.52%` | `0.94` | 3,100,000.00 USD |
| `4H` | `HTX` | `53.91%` | `46.09%` | `1.17` | 119,400.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `51.54%` | `48.46%` | `1.06` | 297,210.00 USD |
| `4H` | `Aster` | `55.93%` | `44.07%` | `1.27` | 265,660.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `20.63%` | `79.37%` | `0.26` | 141,190.00 USD |
| `4H` | `Whale Positions` | `45.1%` | `54.9%` | `0.82` | 50,090,000.00 USD |
| `4H` | `Global Accounts` | `44.77%` | `55.23%` | `0.81` | 122,610,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.6208` | `0.6173` | `0.6208` | `0.6292` | `0.6004` | 5,930,137.61 USD | 2,790,946.56 USD | 3,139,191.05 USD | -348,244.48 USD | `-5.87%` | `7B / 8S` |
| `0:00 UTC` | `0.6268` | `0.6270` | `0.6268` | `0.6331` | `0.6164` | 2,767,755.14 USD | 1,444,801.14 USD | 1,322,953.99 USD | 121,847.15 USD | `+4.40%` | `10B / 14S` |
| `5:00 UTC` | `0.6356` | `0.6324` | `0.6356` | `0.6401` | `0.6246` | 2,269,133.84 USD | 1,171,035.44 USD | 1,098,098.41 USD | 72,937.03 USD | `+3.21%` | `20B / 14S` |
| `0:00 UTC` | `0.6381` | `0.6343` | `0.6381` | `0.6411` | `0.6278` | 1,411,771.88 USD | 641,300.89 USD | 770,470.99 USD | -129,170.10 USD | `-9.15%` | `24B / 26S` |
| `5:00 UTC` | `0.6253` | `0.6259` | `0.6253` | `0.6310` | `0.6218` | 914,324.95 USD | 433,904.43 USD | 480,420.52 USD | -46,516.10 USD | `-5.09%` | `13B / 14S` |
| `0:00 UTC` | `0.6226` | `0.6209` | `0.6226` | `0.6270` | `0.6137` | 2,182,990.34 USD | 1,041,911.64 USD | 1,141,078.70 USD | -99,167.06 USD | `-4.54%` | `6B / 23S` |
| `5:00 UTC` | `0.6283` | `0.6256` | `0.6283` | `0.6296` | `0.6176` | 1,926,940.09 USD | 938,665.17 USD | 988,274.92 USD | -49,609.74 USD | `-2.57%` | `8B / 17S` |
| `0:00 UTC` | `0.6267` | `0.6276` | `0.6267` | `0.6309` | `0.6230` | 968,010.23 USD | 464,277.32 USD | 503,732.91 USD | -39,455.58 USD | `-4.08%` | `5B / 12S` |
| `5:00 UTC` | `0.6237` | `0.6226` | `0.6237` | `0.6264` | `0.6193` | 1,000,191.04 USD | 514,468.59 USD | 485,722.45 USD | 28,746.14 USD | `+2.87%` | `7B / 16S` |
| `0:00 UTC` | `0.6164` | `0.6178` | `0.6164` | `0.6224` | `0.6144` | 694,757.44 USD | 296,408.28 USD | 398,349.16 USD | -101,940.87 USD | `-14.67%` | `4B / 20S` |

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
| `5m` | -5,650.00 USD | 26,990.00 USD | **`ACCUMULATION`** |
| `15m` | -41,560.00 USD | -25,150.00 USD | **`DISTRIBUTION`** |
| `30m` | -177,090.00 USD | -32,320.00 USD | **`DISTRIBUTION`** |
| `1h` | -206,560.00 USD | -129,150.00 USD | **`DISTRIBUTION`** |
| `2h` | -427,790.00 USD | -461,540.00 USD | **`DISTRIBUTION`** |
| `4h` | -645,180.00 USD | -4,310,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -928,690.00 USD | -5,340,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -545,170.00 USD | -6,930,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -487,000.00 USD | -7,060,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,710,000.00 USD | -10,390,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,470,000.00 USD | -24,330,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,890,000.00 USD | -104,960,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-5.65K` | 15m=`-41.56K` | 1h=`-206.56K` | 24h=`-1.71M`
* Futures Capital Netflows: 5m=`+26.99K` | 15m=`-25.15K` | 1h=`-129.15K` | 24h=`-10.39M`
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
  * `2026-10-30 04:15:34 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:40:34 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:34 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
