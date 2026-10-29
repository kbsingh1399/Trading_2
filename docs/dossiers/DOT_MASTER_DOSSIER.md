# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 04:44:06 IST` (`2026-10-29 23:14:06 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9050` | **Live Ask Quote**: `0.9250` | **Mid Price**: `0.9150`
- **Spread Points**: `20.00` | **Spread BPS**: `218.58 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
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
  * Session VWAP: `0.9600` | VWAP Z-Score: `-1.55` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0124` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `29.87` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.05` | Lower -3.00σ Band: `0.8689`
  * Upper +2.51σ Band: `1.04` | Lower -2.51σ Band: `0.8838`
  * Upper +2.01σ Band: `1.02` | Lower -2.01σ Band: `0.8990`
  * Upper +2.00σ Band: `1.02` | Lower -2.00σ Band: `0.8993`
  * Upper +1.28σ Band: `0.9990` | Lower -1.28σ Band: `0.9211`
  * Upper +1.00σ Band: `0.9904` | Lower -1.00σ Band: `0.9297`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9196` | EMA-20=`0.9364` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9575` (Slope: `+0.0000`) | EMA-100=`0.9689`
  * Institutional Anchors: EMA-144=`0.9735` | EMA-200=`0.9761` (Slope: `-0.7278`) | EMA-233=`0.9783`
- **Range Boundaries**: 24H High=`1.01` | 24H Low=`0.8800` | Weekly High=`1.03` | Weekly Low=`0.8800`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9208` (Distance: `-0.52%`)
  * Point of Control (POC) = `0.9149` (Distance: `+0.12%`)
  * Value Area Low (VAL) = `0.9099` (Distance: `+0.67%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.01` | Weekly POC=`0.9932` | Weekly VAL=`0.9751`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9280` | Low=`0.9030`
  * London Session (08:00-16:00 UTC): High=`0.9187` | Low=`0.9113`
  * New York Session (13:00-21:00 UTC): High=`0.9205` | Low=`0.9095`
  * Initial Balance (First Hour): IB High=`0.9177` | IB Low=`0.9123`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9113` - `0.9187`
  * Optimal Trade Entry (OTE 0.705): `0.9168`
  * Structural Invalidation Anchor (0.786): `0.9223`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9233` | `0.9256` | `0.9220` | `0.9242` | `224,492` | 207,292.49 USD | -6,875.56 USD | `-3.32%` | -4,364,686.47 USD | `+0.24` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.9241` | `0.9248` | `0.9156` | `0.9170` | `475,159` | 436,907.44 USD | -29,789.00 USD | `-6.82%` | -4,394,475.47 USD | `+0.08` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.9169` | `0.9176` | `0.9161` | `0.9169` | `38,199` | 35,019.32 USD | -3,461.92 USD | `-9.89%` | -4,397,937.39 USD | `+0.22` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.9253` | `0.9323` | `0.9237` | `0.9272` | `792,359` | 735,316.47 USD | 35,640.09 USD | `+4.85%` | -4,369,374.63 USD | `+0.47` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.9273` | `0.9277` | `0.9213` | `0.9242` | `686,579` | 634,270.61 USD | 7,581.39 USD | `+1.20%` | -4,361,793.23 USD | `+0.39` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.9241` | `0.9248` | `0.9156` | `0.9165` | `512,352` | 471,004.74 USD | -34,095.94 USD | `-7.24%` | -4,395,889.17 USD | `+0.31` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.9106` | `0.9391` | `0.9075` | `0.9232` | `9,308,289` | 8,622,274.03 USD | -1,228,979.98 USD | `-14.25%` | -4,691,361.16 USD | `-1.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9232` | `0.9327` | `0.9142` | `0.9242` | `4,891,705` | 4,523,657.79 USD | 313,110.30 USD | `+6.92%` | -4,378,250.86 USD | `+0.69` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.9241` | `0.9248` | `0.9156` | `0.9165` | `512,352` | 471,004.74 USD | -34,095.94 USD | `-7.24%` | -4,412,346.80 USD | `+0.28` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | 516,506.12 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -280,559.32 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9169` | `40,455,271` | 37,599,737.53 USD | -4,131,068.16 USD | `-10.99%` | -4,411,627.48 USD | `-2.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9699` | `0.9906` | `0.9674` | `0.9732` | `8,505,701` | 8,320,368.15 USD | 13,201.93 USD | `+0.16%` | 609,018.52 USD | `-1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | 694,082.93 USD | `-0.56` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | 516,506.12 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -280,559.32 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9169` | `40,455,271` | 37,599,737.53 USD | -4,131,068.16 USD | `-10.99%` | -4,411,627.48 USD | `-2.16` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.9150`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:36:18 IST` |

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
  * 24H Horizon: Short MP=`0.9461` (Vol: 248,700.00 USD, Dist: `+2.36%`) | Long MP=`0.9083` (Vol: 248,700.00 USD, Dist: `--1.73%`)
  * 48H Horizon: Short MP=`0.9463` (Vol: 248,700.00 USD, Dist: `+2.38%`) | Long MP=`0.9085` (Vol: 248,700.00 USD, Dist: `--1.71%`)
  * 3D Horizon: Short MP=`0.9463` (Vol: 248,700.00 USD, Dist: `+2.38%`) | Long MP=`0.9085` (Vol: 248,700.00 USD, Dist: `--1.71%`)
  * 7D Horizon: Short MP=`0.9460` (Vol: 248,700.00 USD, Dist: `+2.35%`) | Long MP=`0.9102` (Vol: 172,900.00 USD, Dist: `--1.53%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2245` | 112.25 USD | 356,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3555` | 785.30 USD | 355,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4095` | 30,710.00 USD | 355,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 2,790.00 USD | 324,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4295` | 2,450.00 USD | 321,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4685` | 1,170.00 USD | 319,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4695` | 3,390.00 USD | 318,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5065` | 3,290.00 USD | 314,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5115` | 606.38 USD | 311,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 4,130.00 USD | 310,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5235` | 211.34 USD | 306,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 577.36 USD | 306,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5795` | 229.77 USD | 305,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 683.51 USD | 305,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 137.53 USD | 304,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5925` | 35,550.00 USD | 304,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 2,260.00 USD | 269,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6065` | 1,800.00 USD | 266,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 105.96 USD | 265,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 147.48 USD | 265,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 757.80 USD | 264,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 106.00 USD | 264,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 2,090.00 USD | 264,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 20,270.00 USD | 261,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 104.60 USD | 241,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 20,920.00 USD | 241,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 202.47 USD | 220,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6515` | 576.71 USD | 220,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 413.70 USD | 219,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6715` | 214.41 USD | 219,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 63,890.00 USD | 219,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 423.10 USD | 155,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 512.97 USD | 154,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6955` | 322.16 USD | 154,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7005` | 1,140.00 USD | 154,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7035` | 214.15 USD | 152,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 16,520.00 USD | 152,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 988.87 USD | 136,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 1,580.00 USD | 135,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 397.93 USD | 133,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 1,090.00 USD | 133,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 291.18 USD | 132,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 2,300.00 USD | 131,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,140.00 USD | 129,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7365` | 164.53 USD | 128,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7375` | 737.50 USD | 128,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 283.30 USD | 127,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7415` | 52,650.00 USD | 127,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 331.18 USD | 74,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 1,400.00 USD | 74,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 144.07 USD | 72,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7605` | 834.88 USD | 72,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7615` | 804.07 USD | 71,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 3,840.00 USD | 71,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7765` | 1,010.00 USD | 67,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7785` | 210.58 USD | 66,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7815` | 234.45 USD | 66,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 292.03 USD | 65,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7890` | 2,080,000.00 USD | 2,080,000.00 USD | 7,140.00 USD | 2,210.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7910` | 2,070,000.00 USD | 2,070,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7930` | 2,050,000.00 USD | 2,050,000.00 USD | 20,360.00 USD | 1,250.00 USD | 6,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7950` | 2,020,000.00 USD | 2,020,000.00 USD | 3,290.00 USD | 4,710.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7970` | 2,000,000.00 USD | 2,000,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7990` | 1,990,000.00 USD | 1,990,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8010` | 1,950,000.00 USD | 1,950,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8025` | 238.90 USD | 65,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8030` | 1,930,000.00 USD | 1,930,000.00 USD | 4,550.00 USD | 2,260.00 USD | 9,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8050` | 1,920,000.00 USD | 1,920,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8070` | 1,890,000.00 USD | 1,890,000.00 USD | 12,160.00 USD | 4,660.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8090` | 1,870,000.00 USD | 1,870,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8105` | 13,410.00 USD | 65,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8110` | 1,860,000.00 USD | 1,860,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8130` | 1,850,000.00 USD | 1,850,000.00 USD | 14,060.00 USD | 2,970.00 USD | 8,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 51,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8150` | 1,830,000.00 USD | 1,830,000.00 USD | 5,990.00 USD | 7,330.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 1,810,000.00 USD | 1,810,000.00 USD | 10,780.00 USD | 2,430.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8185` | 200.21 USD | 51,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8190` | 1,790,000.00 USD | 1,790,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8210` | 1,770,000.00 USD | 1,770,000.00 USD | 7,510.00 USD | 3,190.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 51,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8220` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 471.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8230` | 1,750,000.00 USD | 1,750,000.00 USD | 29,430.00 USD | 4,620.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 49,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8240` | 1,440,000.00 USD | 1,440,000.00 USD | 10,860.00 USD | 3,640.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8250` | 1,720,000.00 USD | 1,720,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8260` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 5,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 1,700,000.00 USD | 1,700,000.00 USD | 4,320.00 USD | 1,970.00 USD | 616.76 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8280` | 1,410,000.00 USD | 1,410,000.00 USD | 244.70 USD | 25.90 USD | 110.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8290` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8300` | 1,410,000.00 USD | 1,410,000.00 USD | 295.97 USD | 40.90 USD | 137.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8310` | 1,690,000.00 USD | 1,690,000.00 USD | 9,280.00 USD | 1,660.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8320` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 2,800.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8330` | 1,680,000.00 USD | 1,680,000.00 USD | 16,220.00 USD | 10,960.00 USD | 77.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8340` | 1,400,000.00 USD | 1,400,000.00 USD | 25,550.00 USD | 4,520.00 USD | 8,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 1,650,000.00 USD | 1,650,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8360` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 14,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 48,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8370` | 1,630,000.00 USD | 1,630,000.00 USD | 15,240.00 USD | 36.87 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8380` | 1,350,000.00 USD | 1,350,000.00 USD | 9,580.00 USD | 1,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8390` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8400` | 1,340,000.00 USD | 1,340,000.00 USD | 458.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 1,610,000.00 USD | 1,610,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,240.00 USD | 48,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 149.63 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8430` | 1,610,000.00 USD | 1,610,000.00 USD | 6,590.00 USD | 3,840.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8440` | 1,340,000.00 USD | 1,340,000.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8450` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 24.80 USD | 474.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8455` | 706.50 USD | 46,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8470` | 1,590,000.00 USD | 1,590,000.00 USD | 7,900.00 USD | 949.62 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 1,580,000.00 USD | 1,580,000.00 USD | 731.45 USD | 137.03 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 46,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 1,340,000.00 USD | 1,340,000.00 USD | 421.90 USD | 61.55 USD | 206.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 1,580,000.00 USD | 1,580,000.00 USD | 5,480.00 USD | 109.15 USD | 4,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8520` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 1,940.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 1,570,000.00 USD | 1,570,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8540` | 1,330,000.00 USD | 1,330,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 1,560,000.00 USD | 1,560,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8560` | 1,330,000.00 USD | 1,330,000.00 USD | 2,040.00 USD | 199.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8570` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 944.22 USD | 577.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 44,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8580` | 1,330,000.00 USD | 1,330,000.00 USD | 617.52 USD | 58.25 USD | 182.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8590` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8600` | 1,330,000.00 USD | 1,330,000.00 USD | 6,520.00 USD | 1,220.00 USD | 251.39 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8605` | 127.01 USD | 44,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8610` | 1,560,000.00 USD | 1,560,000.00 USD | 7,320.00 USD | 3,160.00 USD | 467.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8620` | 1,320,000.00 USD | 1,320,000.00 USD | 7,410.00 USD | 70.98 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8625` | 309.55 USD | 44,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8630` | 1,540,000.00 USD | 1,540,000.00 USD | 758.91 USD | 2,590.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 43,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 1,310,000.00 USD | 1,310,000.00 USD | 6,350.00 USD | 2,070.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 43,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8650` | 1,540,000.00 USD | 1,540,000.00 USD | 6,720.00 USD | 0.00 USD | 184.85 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8660` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 20.18 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,390.00 USD | 43,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8670` | 1,530,000.00 USD | 1,530,000.00 USD | 12,100.00 USD | 3,240.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8680` | 1,300,000.00 USD | 1,300,000.00 USD | 3,580.00 USD | 3,640.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 1,510,000.00 USD | 1,510,000.00 USD | 25,250.00 USD | 1,950.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 12,590.00 USD | 41,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 1,280,000.00 USD | 1,280,000.00 USD | 21,170.00 USD | 3,580.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 1,470,000.00 USD | 1,470,000.00 USD | 7,370.00 USD | 1,110.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8720` | 1,250,000.00 USD | 1,250,000.00 USD | 32,240.00 USD | 26.70 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 2,270.00 USD | 295.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 1,210,000.00 USD | 1,210,000.00 USD | 7,270.00 USD | 3,160.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 1,200,000.00 USD | 1,200,000.00 USD | 17,510.00 USD | 3,760.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 171.88 USD | 29,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8770` | 1,440,000.00 USD | 1,440,000.00 USD | 52,140.00 USD | 16,410.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8780` | 1,180,000.00 USD | 1,180,000.00 USD | 24,840.00 USD | 15,580.00 USD | 27,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 1,370,000.00 USD | 1,370,000.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8795` | 948.01 USD | 28,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8800` | 1,110,000.00 USD | 1,110,000.00 USD | 47,770.00 USD | 13,000.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 1,360,000.00 USD | 1,360,000.00 USD | 228.30 USD | 167.73 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8815` | 27,450.00 USD | 28,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8820` | 1,040,000.00 USD | 1,040,000.00 USD | 8,950.00 USD | 11,150.00 USD | 425.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 1,360,000.00 USD | 1,360,000.00 USD | 8,430.00 USD | 5,730.00 USD | 957.94 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 1,020,000.00 USD | 1,020,000.00 USD | 11,270.00 USD | 3,590.00 USD | 1,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8845` | 549.72 USD | 549.72 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8850` | 1,350,000.00 USD | 1,350,000.00 USD | 8,630.00 USD | 10,630.00 USD | 866.69 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8860` | 1,010,000.00 USD | 1,010,000.00 USD | 5,930.00 USD | 7,590.00 USD | 9,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8870` | 1,330,000.00 USD | 1,330,000.00 USD | 19,060.00 USD | 5,060.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8880` | 982,000.00 USD | 982,000.00 USD | 63,000.00 USD | 12,170.00 USD | 22,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8890` | 1,300,000.00 USD | 1,300,000.00 USD | 54,380.00 USD | 29,640.00 USD | 14,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8900` | 884,270.00 USD | 884,270.00 USD | 67,680.00 USD | 19,960.00 USD | 19,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8910` | 1,200,000.00 USD | 1,200,000.00 USD | 73,870.00 USD | 10,730.00 USD | 35,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8920` | 777,410.00 USD | 777,410.00 USD | 4,920.00 USD | 7,510.00 USD | 38,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8930` | 1,080,000.00 USD | 1,080,000.00 USD | 62,870.00 USD | 10,990.00 USD | 10,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8940` | 726,010.00 USD | 726,010.00 USD | 49,140.00 USD | 7,700.00 USD | 966.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8950` | 993,260.00 USD | 993,260.00 USD | 7,380.00 USD | 38,120.00 USD | 47,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8960` | 668,200.00 USD | 668,200.00 USD | 21,000.00 USD | 15,480.00 USD | 16,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8970` | 900,700.00 USD | 900,700.00 USD | 106,410.00 USD | 5,400.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8980` | 615,660.00 USD | 615,660.00 USD | 71,390.00 USD | 10,780.00 USD | 32,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8990` | 759,000.00 USD | 759,000.00 USD | 52,250.00 USD | 23,810.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9000` | 500,590.00 USD | 500,590.00 USD | 24,060.00 USD | 30,300.00 USD | 2,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9010` | 663,710.00 USD | 663,710.00 USD | 20,170.00 USD | 11,690.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 443,860.00 USD | 443,860.00 USD | 4,420.00 USD | 3,120.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9030` | 628,620.00 USD | 628,620.00 USD | 13,100.00 USD | 8,710.00 USD | 27,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9040` | 433,530.00 USD | 433,530.00 USD | 8,540.00 USD | 8,840.00 USD | 6,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9050` | 579,350.00 USD | 579,350.00 USD | 31,190.00 USD | 13,050.00 USD | 27,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9060` | 409,340.00 USD | 409,340.00 USD | 0.00 USD | 19,030.00 USD | 9,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9070` | 507,810.00 USD | 507,810.00 USD | 114,070.00 USD | 49,120.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9080` | 380,340.00 USD | 380,340.00 USD | 126,150.00 USD | 39,140.00 USD | 46,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9090` | 329,120.00 USD | 329,120.00 USD | 86,450.00 USD | 954.68 USD | 30,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9100` | 168,940.00 USD | 168,940.00 USD | 1,380.00 USD | 9,610.00 USD | 74,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9110` | 210,920.00 USD | 210,920.00 USD | 76,180.00 USD | 10,780.00 USD | 16,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9120` | 83,920.00 USD | 83,920.00 USD | 48,810.00 USD | 15,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9130` | 107,500.00 USD | 107,500.00 USD | 0.00 USD | 18,210.00 USD | 40,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9140` | 19,410.00 USD | 19,410.00 USD | 0.00 USD | 129.18 USD | 19,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9150` | 48,990.00 USD | 48,990.00 USD | 0.00 USD | 515.41 USD | 33,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9160` | 251.44 USD | 251.44 USD | 0.00 USD | 131.45 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9170` | 15,250.00 USD | 15,250.00 USD | 0.00 USD | 0.00 USD | 15,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9180` | 119.99 USD | 119.99 USD | 0.00 USD | 119.99 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9190` | 18,470.00 USD | 18,470.00 USD | 0.00 USD | 0.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9190` | 36,940.00 USD | 36,940.00 USD | 0.00 USD | 0.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9210` | 52,730.00 USD | 52,730.00 USD | 0.00 USD | 0.00 USD | 15,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9220` | 9,360.00 USD | 9,360.00 USD | 0.00 USD | 0.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9230` | 116,870.00 USD | 116,870.00 USD | 27,030.00 USD | 0.00 USD | 37,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9240` | 9,900.00 USD | 9,900.00 USD | 0.00 USD | 534.40 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9260` | 10,600.00 USD | 10,600.00 USD | 0.00 USD | 704.59 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9280` | 11,100.00 USD | 11,100.00 USD | 0.00 USD | 145.20 USD | 353.46 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9300` | 12,070.00 USD | 12,070.00 USD | 0.00 USD | 221.69 USD | 753.09 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9320` | 59,300.00 USD | 59,300.00 USD | 32,020.00 USD | 7,580.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9340` | 156,390.00 USD | 156,390.00 USD | 85,190.00 USD | 10,860.00 USD | 1,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9350` | 117,640.00 USD | 117,640.00 USD | 0.00 USD | 0.00 USD | 768.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9360` | 290,810.00 USD | 290,810.00 USD | 84,420.00 USD | 30,060.00 USD | 19,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9370` | 135,730.00 USD | 135,730.00 USD | 16,340.00 USD | 0.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9380` | 348,240.00 USD | 348,240.00 USD | 56,080.00 USD | 103.28 USD | 1,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 184,630.00 USD | 184,630.00 USD | 39,250.00 USD | 0.00 USD | 9,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9400` | 407,060.00 USD | 407,060.00 USD | 48,690.00 USD | 6,410.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 230,770.00 USD | 230,770.00 USD | 29,630.00 USD | 9,330.00 USD | 7,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9420` | 491,920.00 USD | 491,920.00 USD | 57,470.00 USD | 17,410.00 USD | 9,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9430` | 288,780.00 USD | 288,780.00 USD | 45,490.00 USD | 0.00 USD | 12,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 666,210.00 USD | 666,210.00 USD | 149,360.00 USD | 7,300.00 USD | 17,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 670,070.00 USD | 670,070.00 USD | 261,930.00 USD | 48,260.00 USD | 71,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 807,210.00 USD | 807,210.00 USD | 80,840.00 USD | 31,690.00 USD | 28,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 947,170.00 USD | 947,170.00 USD | 200,510.00 USD | 0.00 USD | 76,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9480` | 1,050,000.00 USD | 1,050,000.00 USD | 155,950.00 USD | 8,800.00 USD | 74,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 1,330,000.00 USD | 1,330,000.00 USD | 193,040.00 USD | 10,340.00 USD | 178,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 1,170,000.00 USD | 1,170,000.00 USD | 107,250.00 USD | 15,500.00 USD | 2,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 1,720,000.00 USD | 1,720,000.00 USD | 242,000.00 USD | 27,670.00 USD | 117,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 1,280,000.00 USD | 1,280,000.00 USD | 47,190.00 USD | 13,390.00 USD | 44,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 1,940.00 USD | 121,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 1,360,000.00 USD | 1,360,000.00 USD | 43,540.00 USD | 7,980.00 USD | 29,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 19,730.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 1,360,000.00 USD | 1,360,000.00 USD | 865.00 USD | 7,070.00 USD | 275.27 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 1,880,000.00 USD | 1,880,000.00 USD | 1,910.00 USD | 0.00 USD | 957.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 1,370,000.00 USD | 1,370,000.00 USD | 3,480.00 USD | 1,660.00 USD | 313.25 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 1,890,000.00 USD | 1,890,000.00 USD | 1,980.00 USD | 4,660.00 USD | 866.69 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 5,890.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 1,910,000.00 USD | 1,910,000.00 USD | 24,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 1,450,000.00 USD | 1,450,000.00 USD | 51,070.00 USD | 8,170.00 USD | 12,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 1,990,000.00 USD | 1,990,000.00 USD | 53,510.00 USD | 24,130.00 USD | 481.70 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 1,520,000.00 USD | 1,520,000.00 USD | 17,560.00 USD | 25,430.00 USD | 27,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 2,050,000.00 USD | 2,050,000.00 USD | 51,500.00 USD | 0.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 1,560,000.00 USD | 1,560,000.00 USD | 2,450.00 USD | 4,480.00 USD | 37,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 2,100,000.00 USD | 2,100,000.00 USD | 38,090.00 USD | 5,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9680` | 1,600,000.00 USD | 1,600,000.00 USD | 24,830.00 USD | 7,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9685` | 211.13 USD | 211.13 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9690` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 20,550.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 2,090.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 1,670,000.00 USD | 1,670,000.00 USD | 24,360.00 USD | 174.50 USD | 23,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 2,170,000.00 USD | 2,170,000.00 USD | 2,910.00 USD | 9,050.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 1,710,000.00 USD | 1,710,000.00 USD | 25,800.00 USD | 5,170.00 USD | 14,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 16,590.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 1,790,000.00 USD | 1,790,000.00 USD | 53,340.00 USD | 13,960.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 2,290,000.00 USD | 2,290,000.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 1,850,000.00 USD | 1,850,000.00 USD | 39,740.00 USD | 3,080.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 84,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9795` | 212.26 USD | 423.39 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9800` | 1,910,000.00 USD | 1,910,000.00 USD | 29,240.00 USD | 9,580.00 USD | 20,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 212.47 USD | 635.86 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9810` | 2,500,000.00 USD | 2,500,000.00 USD | 540.00 USD | 0.00 USD | 118,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 1,940,000.00 USD | 1,940,000.00 USD | 16,350.00 USD | 12,220.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 2,670,000.00 USD | 2,670,000.00 USD | 102,710.00 USD | 15,810.00 USD | 52,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 2,000,000.00 USD | 2,000,000.00 USD | 665.59 USD | 13,370.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 211.77 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 2,070,000.00 USD | 2,070,000.00 USD | 50,550.00 USD | 3,510.00 USD | 19,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 2,790,000.00 USD | 2,790,000.00 USD | 40,020.00 USD | 0.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9875` | 213.30 USD | 849.16 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9880` | 2,100,000.00 USD | 2,100,000.00 USD | 17,200.00 USD | 130.81 USD | 14,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9890` | 2,810,000.00 USD | 2,810,000.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 2,170,000.00 USD | 2,170,000.00 USD | 57,390.00 USD | 1,300.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 2,200,000.00 USD | 2,200,000.00 USD | 9,210.00 USD | 2,900.00 USD | 13,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9925` | 216.96 USD | 1,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9930` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 2,230,000.00 USD | 2,230,000.00 USD | 12,310.00 USD | 13,250.00 USD | 1,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 2,910,000.00 USD | 2,910,000.00 USD | 33,790.00 USD | 5,380.00 USD | 42,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9955` | 214.83 USD | 1,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9960` | 2,250,000.00 USD | 2,250,000.00 USD | 18,530.00 USD | 4,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 2,990,000.00 USD | 2,990,000.00 USD | 69,270.00 USD | 0.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 2,310,000.00 USD | 2,310,000.00 USD | 40,410.00 USD | 4,790.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 156.00 USD | 462.12 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9995` | 216.59 USD | 1,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,390,000.00 USD | 2,390,000.00 USD | 59,960.00 USD | 27,710.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 216.81 USD | 1,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,040,000.00 USD | 3,040,000.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,390,000.00 USD | 2,390,000.00 USD | 501.30 USD | 0.00 USD | 266.05 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,180,000.00 USD | 3,180,000.00 USD | 105,770.00 USD | 21,740.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,420,000.00 USD | 2,420,000.00 USD | 10,110.00 USD | 9,540.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 217.47 USD | 1,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,220,000.00 USD | 3,220,000.00 USD | 32,430.00 USD | 3,970.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,570,000.00 USD | 2,570,000.00 USD | 101,040.00 USD | 10,140.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,290,000.00 USD | 3,290,000.00 USD | 34,110.00 USD | 0.00 USD | 29,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,620,000.00 USD | 2,620,000.00 USD | 20,070.00 USD | 9,160.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,310,000.00 USD | 3,310,000.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,650,000.00 USD | 2,650,000.00 USD | 10,530.00 USD | 14,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,350,000.00 USD | 3,350,000.00 USD | 20,090.00 USD | 14,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,690,000.00 USD | 2,690,000.00 USD | 16,480.00 USD | 25,380.00 USD | 265.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,400,000.00 USD | 3,400,000.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,730,000.00 USD | 2,730,000.00 USD | 6,250.00 USD | 4,410.00 USD | 25,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 26,510.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,770,000.00 USD | 2,770,000.00 USD | 20,120.00 USD | 2,880.00 USD | 22,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 222.21 USD | 2,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,480,000.00 USD | 3,480,000.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,830,000.00 USD | 2,830,000.00 USD | 24,880.00 USD | 8,530.00 USD | 25,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,590,000.00 USD | 3,590,000.00 USD | 16,530.00 USD | 83,360.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,910,000.00 USD | 2,910,000.00 USD | 52,040.00 USD | 8,850.00 USD | 20,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,750,000.00 USD | 3,750,000.00 USD | 61,450.00 USD | 32,840.00 USD | 68,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 3,000,000.00 USD | 3,000,000.00 USD | 51,380.00 USD | 3,710.00 USD | 36,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 4,070,000.00 USD | 4,070,000.00 USD | 82,230.00 USD | 85,890.00 USD | 146,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 3,140,000.00 USD | 3,140,000.00 USD | 59,910.00 USD | 27,540.00 USD | 53,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 4,180,000.00 USD | 4,180,000.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,240,000.00 USD | 3,240,000.00 USD | 52,630.00 USD | 18,370.00 USD | 20,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,500,000.00 USD | 4,500,000.00 USD | 161,070.00 USD | 127,000.00 USD | 25,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,300,000.00 USD | 3,300,000.00 USD | 31,340.00 USD | 10,940.00 USD | 18,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,710,000.00 USD | 4,710,000.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,450,000.00 USD | 3,450,000.00 USD | 95,330.00 USD | 24,510.00 USD | 33,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,910,000.00 USD | 4,910,000.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,560,000.00 USD | 3,560,000.00 USD | 67,770.00 USD | 8,980.00 USD | 33,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 5,040,000.00 USD | 5,040,000.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,610,000.00 USD | 3,610,000.00 USD | 19,370.00 USD | 9,210.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 5,350,000.00 USD | 5,350,000.00 USD | 259,060.00 USD | 8,290.00 USD | 43,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,620,000.00 USD | 3,620,000.00 USD | 3,240.00 USD | 9,270.00 USD | 2,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,650,000.00 USD | 5,650,000.00 USD | 192,080.00 USD | 3,170.00 USD | 109,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,020,000.00 USD | 6,020,000.00 USD | 239,580.00 USD | 9,010.00 USD | 117,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,460,000.00 USD | 6,460,000.00 USD | 276,890.00 USD | 2,090.00 USD | 159,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,650,000.00 USD | 6,650,000.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,920,000.00 USD | 6,920,000.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,430,000.00 USD | 7,430,000.00 USD | 178,890.00 USD | 96,370.00 USD | 238,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 367.04 USD | 2,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,640,000.00 USD | 7,640,000.00 USD | 116,670.00 USD | 13,780.00 USD | 77,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,950,000.00 USD | 7,950,000.00 USD | 175,350.00 USD | 43,690.00 USD | 87,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 1,450.00 USD | 3,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,150,000.00 USD | 8,150,000.00 USD | 68,590.00 USD | 58,070.00 USD | 74,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,380,000.00 USD | 8,380,000.00 USD | 125,020.00 USD | 33,860.00 USD | 72,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,780,000.00 USD | 8,780,000.00 USD | 218,860.00 USD | 70,000.00 USD | 106,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,240,000.00 USD | 9,240,000.00 USD | 240,060.00 USD | 74,380.00 USD | 145,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,510,000.00 USD | 9,510,000.00 USD | 140,850.00 USD | 56,310.00 USD | 78,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,800,000.00 USD | 9,800,000.00 USD | 141,700.00 USD | 73,690.00 USD | 71,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 10,010,000.00 USD | 10,010,000.00 USD | 90,670.00 USD | 28,390.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,220,000.00 USD | 10,220,000.00 USD | 86,760.00 USD | 43,390.00 USD | 82,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,520,000.00 USD | 10,520,000.00 USD | 219,670.00 USD | 14,440.00 USD | 62,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,750,000.00 USD | 10,750,000.00 USD | 141,570.00 USD | 36,670.00 USD | 52,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.07` | 12,350.00 USD | 16,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,990,000.00 USD | 10,990,000.00 USD | 96,630.00 USD | 42,960.00 USD | 95,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 11,170,000.00 USD | 11,170,000.00 USD | 97,650.00 USD | 27,560.00 USD | 60,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,330,000.00 USD | 11,330,000.00 USD | 75,040.00 USD | 29,910.00 USD | 48,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,570,000.00 USD | 11,570,000.00 USD | 166,380.00 USD | 21,060.00 USD | 52,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,790,000.00 USD | 11,790,000.00 USD | 164,440.00 USD | 26,480.00 USD | 33,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,990,000.00 USD | 11,990,000.00 USD | 61,330.00 USD | 41,110.00 USD | 100,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 12,150,000.00 USD | 12,150,000.00 USD | 86,400.00 USD | 18,540.00 USD | 46,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,380,000.00 USD | 12,380,000.00 USD | 102,510.00 USD | 58,170.00 USD | 69,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,560,000.00 USD | 12,560,000.00 USD | 71,650.00 USD | 23,140.00 USD | 85,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,690,000.00 USD | 12,690,000.00 USD | 70,660.00 USD | 25,660.00 USD | 32,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,850,000.00 USD | 12,850,000.00 USD | 59,760.00 USD | 39,220.00 USD | 62,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 13,020,000.00 USD | 13,020,000.00 USD | 54,830.00 USD | 22,740.00 USD | 92,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,160,000.00 USD | 13,160,000.00 USD | 92,660.00 USD | 13,380.00 USD | 38,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,490,000.00 USD | 13,490,000.00 USD | 188,000.00 USD | 49,370.00 USD | 89,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,670,000.00 USD | 13,670,000.00 USD | 122,300.00 USD | 44,140.00 USD | 15,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,890,000.00 USD | 13,890,000.00 USD | 91,720.00 USD | 19,140.00 USD | 110,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,960,000.00 USD | 13,960,000.00 USD | 22,500.00 USD | 10,390.00 USD | 31,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,070,000.00 USD | 14,070,000.00 USD | 51,840.00 USD | 24,350.00 USD | 34,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,240,000.00 USD | 14,240,000.00 USD | 80,930.00 USD | 42,230.00 USD | 56,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.11` | 169.86 USD | 16,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,400,000.00 USD | 14,400,000.00 USD | 77,150.00 USD | 17,970.00 USD | 64,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,500,000.00 USD | 14,500,000.00 USD | 28,830.00 USD | 43,570.00 USD | 25,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,550,000.00 USD | 14,550,000.00 USD | 32,810.00 USD | 6,650.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,710,000.00 USD | 14,710,000.00 USD | 75,790.00 USD | 45,980.00 USD | 32,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,770,000.00 USD | 14,770,000.00 USD | 24,700.00 USD | 22,760.00 USD | 13,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,870,000.00 USD | 14,870,000.00 USD | 49,110.00 USD | 30,950.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,960,000.00 USD | 14,960,000.00 USD | 61,780.00 USD | 7,080.00 USD | 25,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 15,020,000.00 USD | 15,020,000.00 USD | 18,300.00 USD | 10,940.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,050,000.00 USD | 15,050,000.00 USD | 14,700.00 USD | 342.11 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,150,000.00 USD | 15,150,000.00 USD | 46,320.00 USD | 11,080.00 USD | 45,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,350,000.00 USD | 15,350,000.00 USD | 95,750.00 USD | 12,730.00 USD | 90,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,460,000.00 USD | 15,460,000.00 USD | 77,640.00 USD | 4,280.00 USD | 27,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,550,000.00 USD | 15,550,000.00 USD | 16,300.00 USD | 10,920.00 USD | 61,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,560,000.00 USD | 15,560,000.00 USD | 4,780.00 USD | 4,820.00 USD | 6,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,600,000.00 USD | 15,600,000.00 USD | 2,980.00 USD | 0.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,650,000.00 USD | 15,650,000.00 USD | 36,300.00 USD | 8,480.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,730,000.00 USD | 15,730,000.00 USD | 36,560.00 USD | 1,660.00 USD | 37,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.15` | 1,500.00 USD | 17,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.17` | 2,450.00 USD | 20,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 22,180.00 USD | 42,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.24` | 1,070.00 USD | 43,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 250.37 USD | 43,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,730.00 USD | 55,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 239.77 USD | 55,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,190.00 USD | 59,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 513,610.00 USD | 572,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.31 USD | 572,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 1,810.00 USD | 574,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 124.14 USD | 574,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 782.81 USD | 575,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 235.18 USD | 575,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 2,440.00 USD | 578,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 8,240.00 USD | 586,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 318.46 USD | 586,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 300.15 USD | 587,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 31,120.00 USD | 618,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 90,940.00 USD | 709,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2245` | 356,060.00 USD | 0.00 USD | 112.25 USD | `-75.69%` | `500.00` |
| `Live` | `Long` | `0.3555` | 355,950.00 USD | 0.00 USD | 785.30 USD | `-61.51%` | `2,209.00` |
| `Live` | `Long` | `0.4095` | 355,160.00 USD | 0.00 USD | 30,710.00 USD | `-55.66%` | `75,000.00` |
| `Live` | `Long` | `0.4185` | 324,450.00 USD | 0.00 USD | 2,790.00 USD | `-54.69%` | `6,675.20` |
| `Live` | `Long` | `0.4295` | 321,660.00 USD | 0.00 USD | 2,450.00 USD | `-53.50%` | `5,698.80` |
| `Live` | `Long` | `0.4685` | 319,210.00 USD | 0.00 USD | 1,170.00 USD | `-49.27%` | `2,500.00` |
| `Live` | `Long` | `0.4695` | 318,040.00 USD | 0.00 USD | 3,390.00 USD | `-49.17%` | `7,215.50` |
| `Live` | `Long` | `0.5065` | 314,650.00 USD | 0.00 USD | 3,290.00 USD | `-45.16%` | `6,504.70` |
| `Live` | `Long` | `0.5115` | 311,350.00 USD | 0.00 USD | 606.38 USD | `-44.62%` | `1,185.50` |
| `Live` | `Long` | `0.5125` | 310,750.00 USD | 0.00 USD | 4,130.00 USD | `-44.51%` | `8,067.10` |
| `Live` | `Long` | `0.5235` | 306,610.00 USD | 0.00 USD | 211.34 USD | `-43.32%` | `403.70` |
| `Live` | `Long` | `0.5695` | 306,400.00 USD | 0.00 USD | 577.36 USD | `-38.34%` | `1,013.80` |
| `Live` | `Long` | `0.5795` | 305,830.00 USD | 0.00 USD | 229.77 USD | `-37.26%` | `396.50` |
| `Live` | `Long` | `0.5845` | 305,600.00 USD | 0.00 USD | 683.51 USD | `-36.72%` | `1,169.40` |
| `Live` | `Long` | `0.5895` | 304,910.00 USD | 0.00 USD | 137.53 USD | `-36.17%` | `233.30` |
| `Live` | `Long` | `0.5925` | 304,770.00 USD | 0.00 USD | 35,550.00 USD | `-35.85%` | `60,000.00` |
| `Live` | `Long` | `0.6055` | 269,220.00 USD | 0.00 USD | 2,260.00 USD | `-34.44%` | `3,731.20` |
| `Live` | `Long` | `0.6065` | 266,970.00 USD | 0.00 USD | 1,800.00 USD | `-34.33%` | `2,971.80` |
| `Live` | `Long` | `0.6125` | 265,160.00 USD | 0.00 USD | 105.96 USD | `-33.68%` | `173.00` |
| `Live` | `Long` | `0.6145` | 265,060.00 USD | 0.00 USD | 147.48 USD | `-33.47%` | `240.00` |
| `Live` | `Long` | `0.6315` | 264,910.00 USD | 0.00 USD | 757.80 USD | `-31.63%` | `1,200.00` |
| `Live` | `Long` | `0.6355` | 264,150.00 USD | 0.00 USD | 106.00 USD | `-31.19%` | `166.80` |
| `Live` | `Long` | `0.6405` | 264,050.00 USD | 0.00 USD | 2,090.00 USD | `-30.65%` | `3,262.00` |
| `Live` | `Long` | `0.6415` | 261,960.00 USD | 0.00 USD | 20,270.00 USD | `-30.54%` | `31,595.60` |
| `Live` | `Long` | `0.6425` | 241,690.00 USD | 0.00 USD | 104.60 USD | `-30.44%` | `162.80` |
| `Live` | `Long` | `0.6465` | 241,580.00 USD | 0.00 USD | 20,920.00 USD | `-30.00%` | `32,356.30` |
| `Live` | `Long` | `0.6475` | 220,660.00 USD | 0.00 USD | 202.47 USD | `-29.89%` | `312.70` |
| `Live` | `Long` | `0.6515` | 220,460.00 USD | 0.00 USD | 576.71 USD | `-29.46%` | `885.20` |
| `Live` | `Long` | `0.6595` | 219,890.00 USD | 0.00 USD | 413.70 USD | `-28.59%` | `627.30` |
| `Live` | `Long` | `0.6715` | 219,470.00 USD | 0.00 USD | 214.41 USD | `-27.30%` | `319.30` |
| `Live` | `Long` | `0.6725` | 219,260.00 USD | 0.00 USD | 63,890.00 USD | `-27.19%` | `95,000.00` |
| `Live` | `Long` | `0.6775` | 155,370.00 USD | 0.00 USD | 423.10 USD | `-26.65%` | `624.50` |
| `Live` | `Long` | `0.6835` | 154,950.00 USD | 0.00 USD | 512.97 USD | `-26.00%` | `750.50` |
| `Live` | `Long` | `0.6955` | 154,430.00 USD | 0.00 USD | 322.16 USD | `-24.70%` | `463.20` |
| `Live` | `Long` | `0.7005` | 154,110.00 USD | 0.00 USD | 1,140.00 USD | `-24.16%` | `1,634.20` |
| `Live` | `Long` | `0.7035` | 152,970.00 USD | 0.00 USD | 214.15 USD | `-23.83%` | `304.40` |
| `Live` | `Long` | `0.7075` | 152,750.00 USD | 0.00 USD | 16,520.00 USD | `-23.40%` | `23,344.30` |
| `Live` | `Long` | `0.7145` | 136,240.00 USD | 0.00 USD | 988.87 USD | `-22.64%` | `1,384.00` |
| `Live` | `Long` | `0.7215` | 135,250.00 USD | 0.00 USD | 1,580.00 USD | `-21.88%` | `2,190.90` |
| `Live` | `Long` | `0.7235` | 133,670.00 USD | 0.00 USD | 397.93 USD | `-21.67%` | `550.00` |
| `Live` | `Long` | `0.7255` | 133,270.00 USD | 0.00 USD | 1,090.00 USD | `-21.45%` | `1,500.00` |
| `Live` | `Long` | `0.7285` | 132,180.00 USD | 0.00 USD | 291.18 USD | `-21.12%` | `399.70` |
| `Live` | `Long` | `0.7305` | 131,890.00 USD | 0.00 USD | 2,300.00 USD | `-20.91%` | `3,143.00` |
| `Live` | `Long` | `0.7335` | 129,590.00 USD | 0.00 USD | 1,140.00 USD | `-20.58%` | `1,557.80` |
| `Live` | `Long` | `0.7365` | 128,450.00 USD | 0.00 USD | 164.53 USD | `-20.26%` | `223.40` |
| `Live` | `Long` | `0.7375` | 128,290.00 USD | 0.00 USD | 737.50 USD | `-20.15%` | `1,000.00` |
| `Live` | `Long` | `0.7395` | 127,550.00 USD | 0.00 USD | 283.30 USD | `-19.93%` | `383.10` |
| `Live` | `Long` | `0.7415` | 127,270.00 USD | 0.00 USD | 52,650.00 USD | `-19.72%` | `71,003.30` |
| `Live` | `Long` | `0.7525` | 74,620.00 USD | 0.00 USD | 331.18 USD | `-18.53%` | `440.10` |
| `Live` | `Long` | `0.7535` | 74,290.00 USD | 0.00 USD | 1,400.00 USD | `-18.42%` | `1,859.90` |
| `Live` | `Long` | `0.7555` | 72,880.00 USD | 0.00 USD | 144.07 USD | `-18.20%` | `190.70` |
| `Live` | `Long` | `0.7605` | 72,740.00 USD | 0.00 USD | 834.88 USD | `-17.66%` | `1,097.80` |
| `Live` | `Long` | `0.7615` | 71,910.00 USD | 0.00 USD | 804.07 USD | `-17.55%` | `1,055.90` |
| `Live` | `Long` | `0.7725` | 71,100.00 USD | 0.00 USD | 3,840.00 USD | `-16.36%` | `4,968.90` |
| `Live` | `Long` | `0.7765` | 67,260.00 USD | 0.00 USD | 1,010.00 USD | `-15.93%` | `1,295.40` |
| `Live` | `Long` | `0.7785` | 66,260.00 USD | 0.00 USD | 210.58 USD | `-15.71%` | `270.50` |
| `Live` | `Long` | `0.7815` | 66,050.00 USD | 0.00 USD | 234.45 USD | `-15.39%` | `300.00` |
| `Live` | `Long` | `0.7865` | 65,810.00 USD | 0.00 USD | 292.03 USD | `-14.84%` | `371.30` |
| `Live` | `Long` | `0.8025` | 65,520.00 USD | 0.00 USD | 238.90 USD | `-13.11%` | `297.70` |
| `Live` | `Long` | `0.8105` | 65,280.00 USD | 0.00 USD | 13,410.00 USD | `-12.25%` | `16,544.60` |
| `Live` | `Long` | `0.8135` | 51,870.00 USD | 0.00 USD | 647.79 USD | `-11.92%` | `796.30` |
| `Live` | `Long` | `0.8185` | 51,220.00 USD | 0.00 USD | 200.21 USD | `-11.38%` | `244.60` |
| `Live` | `Long` | `0.8215` | 51,020.00 USD | 0.00 USD | 1,950.00 USD | `-11.05%` | `2,370.70` |
| `Live` | `Long` | `0.8235` | 49,080.00 USD | 0.00 USD | 749.96 USD | `-10.84%` | `910.70` |
| `Live` | `Long` | `0.8365` | 48,330.00 USD | 0.00 USD | 316.70 USD | `-9.43%` | `378.60` |
| `Live` | `Long` | `0.8415` | 48,010.00 USD | 0.00 USD | 1,240.00 USD | `-8.89%` | `1,469.60` |
| `Live` | `Long` | `0.8455` | 46,770.00 USD | 0.00 USD | 706.50 USD | `-8.46%` | `835.60` |
| `Live` | `Long` | `0.8495` | 46,070.00 USD | 0.00 USD | 1,260.00 USD | `-8.02%` | `1,486.90` |
| `Live` | `Long` | `0.8575` | 44,800.00 USD | 0.00 USD | 620.32 USD | `-7.16%` | `723.40` |
| `Live` | `Long` | `0.8605` | 44,180.00 USD | 0.00 USD | 127.01 USD | `-6.83%` | `147.60` |
| `Live` | `Long` | `0.8625` | 44,060.00 USD | 0.00 USD | 309.55 USD | `-6.62%` | `358.90` |
| `Live` | `Long` | `0.8635` | 43,750.00 USD | 0.00 USD | 208.02 USD | `-6.51%` | `240.90` |
| `Live` | `Long` | `0.8645` | 43,540.00 USD | 0.00 USD | 438.30 USD | `-6.40%` | `507.00` |
| `Live` | `Long` | `0.8665` | 43,100.00 USD | 0.00 USD | 1,390.00 USD | `-6.18%` | `1,606.10` |
| `Live` | `Long` | `0.8695` | 41,710.00 USD | 0.00 USD | 12,590.00 USD | `-5.86%` | `14,478.80` |
| `Live` | `Long` | `0.8765` | 29,120.00 USD | 0.00 USD | 171.88 USD | `-5.10%` | `196.10` |
| `Live` | `Long` | `0.8795` | 28,950.00 USD | 0.00 USD | 948.01 USD | `-4.77%` | `1,077.90` |
| `Live` | `Long` | `0.8815` | 28,000.00 USD | 0.00 USD | 27,450.00 USD | `-4.56%` | `31,139.20` |
| `Live` | `Long` | `0.8845` | 549.72 USD | 0.00 USD | 549.72 USD | `-4.23%` | `621.50` |
| `Live` | `Short` | `0.9685` | 211.13 USD | 211.13 USD | 0.00 USD | `+4.86%` | `218.00` |
| `Live` | `Short` | `0.9795` | 423.39 USD | 212.26 USD | 0.00 USD | `+6.05%` | `216.70` |
| `Live` | `Short` | `0.9805` | 635.86 USD | 212.47 USD | 0.00 USD | `+6.16%` | `216.70` |
| `Live` | `Short` | `0.9875` | 849.16 USD | 213.30 USD | 0.00 USD | `+6.92%` | `216.00` |
| `Live` | `Short` | `0.9925` | 1,070.00 USD | 216.96 USD | 0.00 USD | `+7.46%` | `218.60` |
| `Live` | `Short` | `0.9955` | 1,280.00 USD | 214.83 USD | 0.00 USD | `+7.78%` | `215.80` |
| `Live` | `Short` | `0.9995` | 1,500.00 USD | 216.59 USD | 0.00 USD | `+8.22%` | `216.70` |
| `Live` | `Short` | `1.00` | 1,710.00 USD | 216.81 USD | 0.00 USD | `+8.33%` | `216.70` |
| `Live` | `Short` | `1.00` | 1,930.00 USD | 217.47 USD | 0.00 USD | `+8.76%` | `216.50` |
| `Live` | `Short` | `1.02` | 2,150.00 USD | 222.21 USD | 0.00 USD | `+10.06%` | `218.60` |
| `Live` | `Short` | `1.05` | 2,520.00 USD | 367.04 USD | 0.00 USD | `+13.41%` | `350.40` |
| `Live` | `Short` | `1.05` | 3,970.00 USD | 1,450.00 USD | 0.00 USD | `+13.96%` | `1,376.10` |
| `Live` | `Short` | `1.07` | 16,320.00 USD | 12,350.00 USD | 0.00 USD | `+16.12%` | `11,518.80` |
| `Live` | `Short` | `1.11` | 16,490.00 USD | 169.86 USD | 0.00 USD | `+20.13%` | `153.10` |
| `Live` | `Short` | `1.15` | 17,990.00 USD | 1,500.00 USD | 0.00 USD | `+24.24%` | `1,306.30` |
| `Live` | `Short` | `1.17` | 20,450.00 USD | 2,450.00 USD | 0.00 USD | `+26.73%` | `2,096.60` |
| `Live` | `Short` | `1.19` | 42,630.00 USD | 22,180.00 USD | 0.00 USD | `+28.68%` | `18,664.00` |
| `Live` | `Short` | `1.24` | 43,700.00 USD | 1,070.00 USD | 0.00 USD | `+33.99%` | `864.60` |
| `Live` | `Short` | `1.26` | 43,950.00 USD | 250.37 USD | 0.00 USD | `+36.15%` | `199.10` |
| `Live` | `Short` | `1.32` | 55,680.00 USD | 11,730.00 USD | 0.00 USD | `+43.30%` | `8,862.90` |
| `Live` | `Short` | `1.34` | 55,920.00 USD | 239.77 USD | 0.00 USD | `+45.03%` | `179.00` |
| `Live` | `Short` | `1.42` | 59,110.00 USD | 3,190.00 USD | 0.00 USD | `+53.69%` | `2,249.30` |
| `Live` | `Short` | `1.49` | 572,720.00 USD | 513,610.00 USD | 0.00 USD | `+61.16%` | `345,051.20` |
| `Live` | `Short` | `1.54` | 572,900.00 USD | 176.31 USD | 0.00 USD | `+67.01%` | `114.30` |
| `Live` | `Short` | `1.56` | 574,700.00 USD | 1,810.00 USD | 0.00 USD | `+68.53%` | `1,161.90` |
| `Live` | `Short` | `1.56` | 574,830.00 USD | 124.14 USD | 0.00 USD | `+69.07%` | `79.50` |
| `Live` | `Short` | `1.57` | 575,610.00 USD | 782.81 USD | 0.00 USD | `+69.72%` | `499.40` |
| `Live` | `Short` | `1.61` | 575,850.00 USD | 235.18 USD | 0.00 USD | `+74.05%` | `146.30` |
| `Live` | `Short` | `1.62` | 578,280.00 USD | 2,440.00 USD | 0.00 USD | `+75.89%` | `1,500.00` |
| `Live` | `Short` | `1.65` | 586,520.00 USD | 8,240.00 USD | 0.00 USD | `+78.38%` | `5,000.00` |
| `Live` | `Short` | `1.66` | 586,840.00 USD | 318.46 USD | 0.00 USD | `+79.68%` | `191.90` |
| `Live` | `Short` | `1.67` | 587,140.00 USD | 300.15 USD | 0.00 USD | `+80.54%` | `180.00` |
| `Live` | `Short` | `1.74` | 618,260.00 USD | 31,120.00 USD | 0.00 USD | `+88.34%` | `17,887.50` |
| `Live` | `Short` | `1.83` | 709,190.00 USD | 90,940.00 USD | 0.00 USD | `+97.87%` | `49,759.80` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4015` | 332,770.00 USD | 0.00 USD | 120.45 USD | `-56.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 332,650.00 USD | 0.00 USD | 150.15 USD | `-45.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 332,500.00 USD | 0.00 USD | 1,150.00 USD | `-29.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 331,350.00 USD | 0.00 USD | 781.90 USD | `-24.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 330,570.00 USD | 0.00 USD | 477.38 USD | `-23.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 330,090.00 USD | 0.00 USD | 341.33 USD | `-22.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 329,750.00 USD | 0.00 USD | 972.82 USD | `-21.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 328,780.00 USD | 0.00 USD | 160.20 USD | `-20.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7385` | 328,620.00 USD | 0.00 USD | 102.58 USD | `-20.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 328,510.00 USD | 0.00 USD | 289.49 USD | `-19.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7615` | 328,230.00 USD | 0.00 USD | 197.53 USD | `-17.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 328,030.00 USD | 0.00 USD | 14,570.00 USD | `-15.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 313,460.00 USD | 0.00 USD | 274,830.00 USD | `-13.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 38,630.00 USD | 0.00 USD | 108.47 USD | `-13.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 38,520.00 USD | 0.00 USD | 405.75 USD | `-12.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 38,110.00 USD | 0.00 USD | 772.84 USD | `-9.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 37,340.00 USD | 0.00 USD | 3,470.00 USD | `-8.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 33,870.00 USD | 0.00 USD | 9,180.00 USD | `-7.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 24,690.00 USD | 0.00 USD | 341.94 USD | `-7.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 24,350.00 USD | 0.00 USD | 1,150.00 USD | `-7.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 23,200.00 USD | 0.00 USD | 2,020.00 USD | `-7.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 21,190.00 USD | 0.00 USD | 429.25 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 20,760.00 USD | 0.00 USD | 1,290.00 USD | `-6.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 19,470.00 USD | 0.00 USD | 518.51 USD | `-6.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 18,950.00 USD | 0.00 USD | 649.66 USD | `-5.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 18,300.00 USD | 0.00 USD | 193.35 USD | `-4.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 18,100.00 USD | 0.00 USD | 223.04 USD | `-4.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 17,880.00 USD | 0.00 USD | 10,840.00 USD | `-3.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 7,040.00 USD | 0.00 USD | 158.51 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 6,880.00 USD | 0.00 USD | 192.07 USD | `-3.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 6,690.00 USD | 0.00 USD | 195.32 USD | `-3.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8965` | 6,490.00 USD | 0.00 USD | 242.50 USD | `-2.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9035` | 6,250.00 USD | 0.00 USD | 196.96 USD | `-2.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9045` | 6,050.00 USD | 0.00 USD | 196.10 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9065` | 5,860.00 USD | 0.00 USD | 198.61 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9075` | 5,660.00 USD | 0.00 USD | 994.35 USD | `-1.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 4,660.00 USD | 0.00 USD | 363.40 USD | `-1.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9095` | 4,300.00 USD | 0.00 USD | 398.72 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9115` | 3,900.00 USD | 0.00 USD | 199.80 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9155` | 3,700.00 USD | 0.00 USD | 199.49 USD | `-0.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9165` | 3,500.00 USD | 0.00 USD | 198.06 USD | `-0.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9175` | 3,300.00 USD | 0.00 USD | 396.82 USD | `-0.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9185` | 2,910.00 USD | 0.00 USD | 796.16 USD | `-0.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9195` | 2,110.00 USD | 0.00 USD | 198.52 USD | `-0.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 1,910.00 USD | 0.00 USD | 913.41 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9215` | 997.74 USD | 0.00 USD | 795.81 USD | `-0.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9225` | 201.94 USD | 0.00 USD | 201.94 USD | `-0.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9275` | 2,120.00 USD | 2,120.00 USD | 0.00 USD | `+0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9285` | 2,360.00 USD | 246.05 USD | 0.00 USD | `+0.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9295` | 2,770.00 USD | 407.49 USD | 0.00 USD | `+0.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 2,980.00 USD | 203.97 USD | 0.00 USD | `+0.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 3,180.00 USD | 201.89 USD | 0.00 USD | `+0.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 3,380.00 USD | 201.64 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 3,580.00 USD | 201.97 USD | 0.00 USD | `+1.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 13,270.00 USD | 9,680.00 USD | 0.00 USD | `+1.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 13,820.00 USD | 555.18 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 14,640.00 USD | 816.96 USD | 0.00 USD | `+2.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 16,360.00 USD | 1,730.00 USD | 0.00 USD | `+2.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 16,750.00 USD | 383.87 USD | 0.00 USD | `+2.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 17,560.00 USD | 817.40 USD | 0.00 USD | `+2.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 17,980.00 USD | 414.68 USD | 0.00 USD | `+2.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9525` | 18,360.00 USD | 381.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 20,590.00 USD | 2,230.00 USD | 0.00 USD | `+3.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 24,480.00 USD | 3,900.00 USD | 0.00 USD | `+3.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 24,720.00 USD | 236.26 USD | 0.00 USD | `+3.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 24,890.00 USD | 166.41 USD | 0.00 USD | `+3.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 25,260.00 USD | 376.80 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 27,170.00 USD | 1,910.00 USD | 0.00 USD | `+4.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 27,740.00 USD | 568.75 USD | 0.00 USD | `+4.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 27,900.00 USD | 163.29 USD | 0.00 USD | `+4.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 28,460.00 USD | 554.58 USD | 0.00 USD | `+4.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 28,840.00 USD | 385.74 USD | 0.00 USD | `+4.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 29,000.00 USD | 153.22 USD | 0.00 USD | `+4.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 51,800.00 USD | 22,800.00 USD | 0.00 USD | `+4.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 52,060.00 USD | 262.52 USD | 0.00 USD | `+5.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 62,420.00 USD | 10,370.00 USD | 0.00 USD | `+5.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 62,810.00 USD | 387.83 USD | 0.00 USD | `+5.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 70,440.00 USD | 7,630.00 USD | 0.00 USD | `+5.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9745` | 79,190.00 USD | 8,750.00 USD | 0.00 USD | `+5.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 101,150.00 USD | 21,960.00 USD | 0.00 USD | `+5.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 101,550.00 USD | 396.17 USD | 0.00 USD | `+5.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 102,230.00 USD | 676.53 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 113,630.00 USD | 11,400.00 USD | 0.00 USD | `+5.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 113,750.00 USD | 123.61 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 122,100.00 USD | 8,350.00 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 124,160.00 USD | 2,060.00 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 125,210.00 USD | 1,050.00 USD | 0.00 USD | `+6.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 140,280.00 USD | 15,070.00 USD | 0.00 USD | `+6.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9865` | 173,080.00 USD | 32,800.00 USD | 0.00 USD | `+6.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9895` | 208,050.00 USD | 34,970.00 USD | 0.00 USD | `+7.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 211,570.00 USD | 3,520.00 USD | 0.00 USD | `+7.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 243,320.00 USD | 31,750.00 USD | 0.00 USD | `+7.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 243,730.00 USD | 403.06 USD | 0.00 USD | `+7.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 244,510.00 USD | 782.07 USD | 0.00 USD | `+7.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 244,910.00 USD | 403.28 USD | 0.00 USD | `+7.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 250,050.00 USD | 5,140.00 USD | 0.00 USD | `+8.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 287,360.00 USD | 37,310.00 USD | 0.00 USD | `+8.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 288,360.00 USD | 1,000.00 USD | 0.00 USD | `+8.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 328,960.00 USD | 40,590.00 USD | 0.00 USD | `+8.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 329,190.00 USD | 235.79 USD | 0.00 USD | `+8.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 330,540.00 USD | 1,340.00 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 330,770.00 USD | 230.39 USD | 0.00 USD | `+8.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 330,990.00 USD | 218.64 USD | 0.00 USD | `+9.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 331,400.00 USD | 409.86 USD | 0.00 USD | `+9.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 331,510.00 USD | 110.95 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 332,120.00 USD | 615.60 USD | 0.00 USD | `+9.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 332,680.00 USD | 561.17 USD | 0.00 USD | `+9.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 332,790.00 USD | 103.07 USD | 0.00 USD | `+10.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 333,190.00 USD | 401.26 USD | 0.00 USD | `+10.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 333,990.00 USD | 804.09 USD | 0.00 USD | `+10.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 334,200.00 USD | 207.97 USD | 0.00 USD | `+11.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 334,300.00 USD | 101.51 USD | 0.00 USD | `+11.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 334,510.00 USD | 208.26 USD | 0.00 USD | `+11.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 335,030.00 USD | 516.75 USD | 0.00 USD | `+11.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 335,230.00 USD | 204.93 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 335,580.00 USD | 348.86 USD | 0.00 USD | `+12.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 335,990.00 USD | 413.76 USD | 0.00 USD | `+12.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 336,350.00 USD | 354.91 USD | 0.00 USD | `+12.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 338,250.00 USD | 1,900.00 USD | 0.00 USD | `+12.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 338,460.00 USD | 207.87 USD | 0.00 USD | `+12.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 338,670.00 USD | 207.97 USD | 0.00 USD | `+12.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 339,960.00 USD | 1,290.00 USD | 0.00 USD | `+13.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 340,170.00 USD | 206.97 USD | 0.00 USD | `+13.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 340,280.00 USD | 107.99 USD | 0.00 USD | `+13.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 340,530.00 USD | 247.60 USD | 0.00 USD | `+14.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 415,360.00 USD | 74,840.00 USD | 0.00 USD | `+14.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 415,910.00 USD | 544.88 USD | 0.00 USD | `+15.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 416,060.00 USD | 157.10 USD | 0.00 USD | `+16.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 418,240.00 USD | 2,170.00 USD | 0.00 USD | `+18.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 419,770.00 USD | 1,540.00 USD | 0.00 USD | `+18.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 429,700.00 USD | 9,930.00 USD | 0.00 USD | `+18.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 430,580.00 USD | 877.63 USD | 0.00 USD | `+20.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 430,750.00 USD | 171.50 USD | 0.00 USD | `+20.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 430,920.00 USD | 171.09 USD | 0.00 USD | `+20.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 433,690.00 USD | 2,770.00 USD | 0.00 USD | `+21.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 435,730.00 USD | 2,040.00 USD | 0.00 USD | `+21.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 438,390.00 USD | 2,670.00 USD | 0.00 USD | `+22.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 438,570.00 USD | 174.38 USD | 0.00 USD | `+23.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 438,740.00 USD | 174.84 USD | 0.00 USD | `+23.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 438,890.00 USD | 150.90 USD | 0.00 USD | `+24.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 439,040.00 USD | 151.03 USD | 0.00 USD | `+24.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 439,200.00 USD | 151.16 USD | 0.00 USD | `+24.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 439,350.00 USD | 151.29 USD | 0.00 USD | `+24.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 439,500.00 USD | 151.42 USD | 0.00 USD | `+24.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 439,650.00 USD | 151.55 USD | 0.00 USD | `+24.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 439,800.00 USD | 151.69 USD | 0.00 USD | `+24.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 441,850.00 USD | 2,050.00 USD | 0.00 USD | `+26.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 441,960.00 USD | 110.00 USD | 0.00 USD | `+26.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 442,320.00 USD | 356.85 USD | 0.00 USD | `+28.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 443,520.00 USD | 1,210.00 USD | 0.00 USD | `+29.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 486,450.00 USD | 42,930.00 USD | 0.00 USD | `+30.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 488,450.00 USD | 2,000.00 USD | 0.00 USD | `+33.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 489,840.00 USD | 1,380.00 USD | 0.00 USD | `+35.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 490,080.00 USD | 245.41 USD | 0.00 USD | `+38.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 498,480.00 USD | 8,390.00 USD | 0.00 USD | `+39.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 498,890.00 USD | 415.25 USD | 0.00 USD | `+40.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 505,410.00 USD | 6,520.00 USD | 0.00 USD | `+41.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 962,400.00 USD | 456,990.00 USD | 0.00 USD | `+41.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 963,050.00 USD | 655.75 USD | 0.00 USD | `+42.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 964,870.00 USD | 1,810.00 USD | 0.00 USD | `+45.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 978,750.00 USD | 13,880.00 USD | 0.00 USD | `+45.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 980,000.00 USD | 1,250.00 USD | 0.00 USD | `+46.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 982,070.00 USD | 2,070.00 USD | 0.00 USD | `+50.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 982,210.00 USD | 140.05 USD | 0.00 USD | `+51.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 982,370.00 USD | 160.42 USD | 0.00 USD | `+51.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 982,970.00 USD | 598.33 USD | 0.00 USD | `+52.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 1,020,000.00 USD | 34,170.00 USD | 0.00 USD | `+55.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 1,020,000.00 USD | 879.84 USD | 0.00 USD | `+61.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 1,020,000.00 USD | 590.88 USD | 0.00 USD | `+62.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 1,020,000.00 USD | 3,050.00 USD | 0.00 USD | `+64.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 1,020,000.00 USD | 297.27 USD | 0.00 USD | `+67.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 1,030,000.00 USD | 8,530.00 USD | 0.00 USD | `+79.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 1,030,000.00 USD | 143.99 USD | 0.00 USD | `+80.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 1,030,000.00 USD | 177.05 USD | 0.00 USD | `+91.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 1,030,000.00 USD | 431.40 USD | 0.00 USD | `+94.94%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7890` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 7,140.00 USD | 2,210.00 USD | 2,800.00 USD |
| `7D` | `0.7910` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD |
| `7D` | `0.7930` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 20,360.00 USD | 1,250.00 USD | 6,130.00 USD |
| `7D` | `0.7950` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 3,290.00 USD | 4,710.00 USD | 14,710.00 USD |
| `7D` | `0.7970` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD |
| `7D` | `0.7990` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD |
| `7D` | `0.8010` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD |
| `7D` | `0.8030` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 4,550.00 USD | 2,260.00 USD | 9,770.00 USD |
| `7D` | `0.8050` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD |
| `7D` | `0.8070` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 12,160.00 USD | 4,660.00 USD | 6,450.00 USD |
| `7D` | `0.8090` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD |
| `7D` | `0.8110` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD |
| `7D` | `0.8130` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 14,060.00 USD | 2,970.00 USD | 8,560.00 USD |
| `7D` | `0.8150` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 5,990.00 USD | 7,330.00 USD | 4,220.00 USD |
| `7D` | `0.8170` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 10,780.00 USD | 2,430.00 USD | 9,670.00 USD |
| `7D` | `0.8190` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD |
| `7D` | `0.8210` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 7,510.00 USD | 3,190.00 USD | 10,030.00 USD |
| `1D` | `0.8220` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 471.94 USD |
| `7D` | `0.8230` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 29,430.00 USD | 4,620.00 USD | 1,960.00 USD |
| `1D` | `0.8240` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 10,860.00 USD | 3,640.00 USD | 6,790.00 USD |
| `7D` | `0.8250` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD |
| `1D` | `0.8260` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 0.00 USD | 5,920.00 USD | 0.00 USD |
| `7D` | `0.8270` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 4,320.00 USD | 1,970.00 USD | 616.76 USD |
| `1D` | `0.8280` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 244.70 USD | 25.90 USD | 110.11 USD |
| `7D` | `0.8290` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD |
| `1D` | `0.8300` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 295.97 USD | 40.90 USD | 137.17 USD |
| `7D` | `0.8310` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 9,280.00 USD | 1,660.00 USD | 2,450.00 USD |
| `1D` | `0.8320` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | 2,800.00 USD | 1,900.00 USD |
| `7D` | `0.8330` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 16,220.00 USD | 10,960.00 USD | 77.95 USD |
| `1D` | `0.8340` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 25,550.00 USD | 4,520.00 USD | 8,980.00 USD |
| `7D` | `0.8350` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD |
| `1D` | `0.8360` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 14,810.00 USD |
| `7D` | `0.8370` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 15,240.00 USD | 36.87 USD | 0.00 USD |
| `1D` | `0.8380` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 9,580.00 USD | 1,900.00 USD | 0.00 USD |
| `7D` | `0.8390` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD |
| `1D` | `0.8400` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 458.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8410` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD |
| `1D` | `0.8420` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 0.00 USD | 149.63 USD | 0.00 USD |
| `7D` | `0.8430` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 6,590.00 USD | 3,840.00 USD | 4,060.00 USD |
| `1D` | `0.8440` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8450` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 0.00 USD | 24.80 USD | 474.61 USD |
| `7D` | `0.8470` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 7,900.00 USD | 949.62 USD | 2,180.00 USD |
| `7D` | `0.8490` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 731.45 USD | 137.03 USD | 0.00 USD |
| `1D` | `0.8500` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 421.90 USD | 61.55 USD | 206.79 USD |
| `7D` | `0.8510` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 5,480.00 USD | 109.15 USD | 4,660.00 USD |
| `1D` | `0.8520` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 0.00 USD | 1,940.00 USD | 2,470.00 USD |
| `7D` | `0.8530` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD |
| `1D` | `0.8540` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8550` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD |
| `1D` | `0.8560` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 2,040.00 USD | 199.60 USD | 0.00 USD |
| `7D` | `0.8570` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 0.00 USD | 944.22 USD | 577.61 USD |
| `1D` | `0.8580` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 617.52 USD | 58.25 USD | 182.69 USD |
| `7D` | `0.8590` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD |
| `1D` | `0.8600` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 6,520.00 USD | 1,220.00 USD | 251.39 USD |
| `7D` | `0.8610` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 7,320.00 USD | 3,160.00 USD | 467.14 USD |
| `1D` | `0.8620` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 7,410.00 USD | 70.98 USD | 0.00 USD |
| `7D` | `0.8630` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 758.91 USD | 2,590.00 USD | 1,280.00 USD |
| `1D` | `0.8640` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 6,350.00 USD | 2,070.00 USD | 3,790.00 USD |
| `7D` | `0.8650` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 6,720.00 USD | 0.00 USD | 184.85 USD |
| `1D` | `0.8660` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 20.18 USD | 0.00 USD |
| `7D` | `0.8670` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 12,100.00 USD | 3,240.00 USD | 10,160.00 USD |
| `1D` | `0.8680` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 3,580.00 USD | 3,640.00 USD | 8,720.00 USD |
| `7D` | `0.8690` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 25,250.00 USD | 1,950.00 USD | 8,040.00 USD |
| `1D` | `0.8700` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 21,170.00 USD | 3,580.00 USD | 4,760.00 USD |
| `7D` | `0.8710` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 7,370.00 USD | 1,110.00 USD | 13,110.00 USD |
| `1D` | `0.8720` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 32,240.00 USD | 26.70 USD | 6,210.00 USD |
| `7D` | `0.8730` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | 2,270.00 USD | 295.31 USD |
| `1D` | `0.8740` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 7,270.00 USD | 3,160.00 USD | 3,030.00 USD |
| `7D` | `0.8750` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 6,210.00 USD |
| `1D` | `0.8760` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 17,510.00 USD | 3,760.00 USD | 4,390.00 USD |
| `7D` | `0.8770` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 52,140.00 USD | 16,410.00 USD | 2,760.00 USD |
| `1D` | `0.8780` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 24,840.00 USD | 15,580.00 USD | 27,090.00 USD |
| `7D` | `0.8790` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD |
| `1D` | `0.8800` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 47,770.00 USD | 13,000.00 USD | 5,490.00 USD |
| `7D` | `0.8810` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 228.30 USD | 167.73 USD | 0.00 USD |
| `1D` | `0.8820` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 8,950.00 USD | 11,150.00 USD | 425.40 USD |
| `7D` | `0.8830` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 8,430.00 USD | 5,730.00 USD | 957.94 USD |
| `1D` | `0.8840` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 11,270.00 USD | 3,590.00 USD | 1,030.00 USD |
| `7D` | `0.8850` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 8,630.00 USD | 10,630.00 USD | 866.69 USD |
| `1D` | `0.8860` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 5,930.00 USD | 7,590.00 USD | 9,740.00 USD |
| `7D` | `0.8870` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 19,060.00 USD | 5,060.00 USD | 7,460.00 USD |
| `1D` | `0.8880` | 982,000.00 USD | 0.00 USD | 982,000.00 USD | 63,000.00 USD | 12,170.00 USD | 22,560.00 USD |
| `7D` | `0.8890` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 54,380.00 USD | 29,640.00 USD | 14,360.00 USD |
| `1D` | `0.8900` | 884,270.00 USD | 0.00 USD | 884,270.00 USD | 67,680.00 USD | 19,960.00 USD | 19,230.00 USD |
| `7D` | `0.8910` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 73,870.00 USD | 10,730.00 USD | 35,050.00 USD |
| `1D` | `0.8920` | 777,410.00 USD | 0.00 USD | 777,410.00 USD | 4,920.00 USD | 7,510.00 USD | 38,970.00 USD |
| `7D` | `0.8930` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 62,870.00 USD | 10,990.00 USD | 10,100.00 USD |
| `1D` | `0.8940` | 726,010.00 USD | 0.00 USD | 726,010.00 USD | 49,140.00 USD | 7,700.00 USD | 966.50 USD |
| `7D` | `0.8950` | 993,260.00 USD | 0.00 USD | 993,260.00 USD | 7,380.00 USD | 38,120.00 USD | 47,060.00 USD |
| `1D` | `0.8960` | 668,200.00 USD | 0.00 USD | 668,200.00 USD | 21,000.00 USD | 15,480.00 USD | 16,060.00 USD |
| `7D` | `0.8970` | 900,700.00 USD | 0.00 USD | 900,700.00 USD | 106,410.00 USD | 5,400.00 USD | 29,890.00 USD |
| `1D` | `0.8980` | 615,660.00 USD | 0.00 USD | 615,660.00 USD | 71,390.00 USD | 10,780.00 USD | 32,910.00 USD |
| `7D` | `0.8990` | 759,000.00 USD | 0.00 USD | 759,000.00 USD | 52,250.00 USD | 23,810.00 USD | 19,220.00 USD |
| `1D` | `0.9000` | 500,590.00 USD | 0.00 USD | 500,590.00 USD | 24,060.00 USD | 30,300.00 USD | 2,370.00 USD |
| `7D` | `0.9010` | 663,710.00 USD | 0.00 USD | 663,710.00 USD | 20,170.00 USD | 11,690.00 USD | 3,230.00 USD |
| `1D` | `0.9020` | 443,860.00 USD | 0.00 USD | 443,860.00 USD | 4,420.00 USD | 3,120.00 USD | 2,790.00 USD |
| `7D` | `0.9030` | 628,620.00 USD | 0.00 USD | 628,620.00 USD | 13,100.00 USD | 8,710.00 USD | 27,460.00 USD |
| `1D` | `0.9040` | 433,530.00 USD | 0.00 USD | 433,530.00 USD | 8,540.00 USD | 8,840.00 USD | 6,810.00 USD |
| `7D` | `0.9050` | 579,350.00 USD | 0.00 USD | 579,350.00 USD | 31,190.00 USD | 13,050.00 USD | 27,300.00 USD |
| `1D` | `0.9060` | 409,340.00 USD | 0.00 USD | 409,340.00 USD | 0.00 USD | 19,030.00 USD | 9,970.00 USD |
| `7D` | `0.9070` | 507,810.00 USD | 0.00 USD | 507,810.00 USD | 114,070.00 USD | 49,120.00 USD | 15,500.00 USD |
| `1D` | `0.9080` | 380,340.00 USD | 0.00 USD | 380,340.00 USD | 126,150.00 USD | 39,140.00 USD | 46,100.00 USD |
| `7D` | `0.9090` | 329,120.00 USD | 0.00 USD | 329,120.00 USD | 86,450.00 USD | 954.68 USD | 30,800.00 USD |
| `1D` | `0.9100` | 168,940.00 USD | 0.00 USD | 168,940.00 USD | 1,380.00 USD | 9,610.00 USD | 74,030.00 USD |
| `7D` | `0.9110` | 210,920.00 USD | 0.00 USD | 210,920.00 USD | 76,180.00 USD | 10,780.00 USD | 16,450.00 USD |
| `1D` | `0.9120` | 83,920.00 USD | 0.00 USD | 83,920.00 USD | 48,810.00 USD | 15,700.00 USD | 0.00 USD |
| `7D` | `0.9130` | 107,500.00 USD | 0.00 USD | 107,500.00 USD | 0.00 USD | 18,210.00 USD | 40,290.00 USD |
| `1D` | `0.9140` | 19,410.00 USD | 0.00 USD | 19,410.00 USD | 0.00 USD | 129.18 USD | 19,030.00 USD |
| `7D` | `0.9150` | 48,990.00 USD | 0.00 USD | 48,990.00 USD | 0.00 USD | 515.41 USD | 33,220.00 USD |
| `1D` | `0.9160` | 251.44 USD | 0.00 USD | 251.44 USD | 0.00 USD | 131.45 USD | 0.00 USD |
| `7D` | `0.9170` | 15,250.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 0.00 USD | 15,250.00 USD |
| `1D` | `0.9180` | 119.99 USD | 0.00 USD | 119.99 USD | 0.00 USD | 119.99 USD | 0.00 USD |
| `1D` | `0.9190` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9190` | 18,470.00 USD | 18,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,470.00 USD |
| `7D` | `0.9190` | 36,940.00 USD | 36,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,470.00 USD |
| `7D` | `0.9210` | 52,730.00 USD | 52,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,790.00 USD |
| `1D` | `0.9220` | 9,360.00 USD | 9,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,360.00 USD |
| `7D` | `0.9230` | 116,870.00 USD | 116,870.00 USD | 0.00 USD | 27,030.00 USD | 0.00 USD | 37,100.00 USD |
| `1D` | `0.9240` | 9,900.00 USD | 9,900.00 USD | 0.00 USD | 0.00 USD | 534.40 USD | 0.00 USD |
| `1D` | `0.9260` | 10,600.00 USD | 10,600.00 USD | 0.00 USD | 0.00 USD | 704.59 USD | 0.00 USD |
| `1D` | `0.9280` | 11,100.00 USD | 11,100.00 USD | 0.00 USD | 0.00 USD | 145.20 USD | 353.46 USD |
| `1D` | `0.9300` | 12,070.00 USD | 12,070.00 USD | 0.00 USD | 0.00 USD | 221.69 USD | 753.09 USD |
| `1D` | `0.9320` | 59,300.00 USD | 59,300.00 USD | 0.00 USD | 32,020.00 USD | 7,580.00 USD | 7,630.00 USD |
| `1D` | `0.9340` | 156,390.00 USD | 156,390.00 USD | 0.00 USD | 85,190.00 USD | 10,860.00 USD | 1,050.00 USD |
| `7D` | `0.9350` | 117,640.00 USD | 117,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 768.64 USD |
| `1D` | `0.9360` | 290,810.00 USD | 290,810.00 USD | 0.00 USD | 84,420.00 USD | 30,060.00 USD | 19,940.00 USD |
| `7D` | `0.9370` | 135,730.00 USD | 135,730.00 USD | 0.00 USD | 16,340.00 USD | 0.00 USD | 1,760.00 USD |
| `1D` | `0.9380` | 348,240.00 USD | 348,240.00 USD | 0.00 USD | 56,080.00 USD | 103.28 USD | 1,250.00 USD |
| `7D` | `0.9390` | 184,630.00 USD | 184,630.00 USD | 0.00 USD | 39,250.00 USD | 0.00 USD | 9,650.00 USD |
| `1D` | `0.9400` | 407,060.00 USD | 407,060.00 USD | 0.00 USD | 48,690.00 USD | 6,410.00 USD | 3,720.00 USD |
| `7D` | `0.9410` | 230,770.00 USD | 230,770.00 USD | 0.00 USD | 29,630.00 USD | 9,330.00 USD | 7,180.00 USD |
| `1D` | `0.9420` | 491,920.00 USD | 491,920.00 USD | 0.00 USD | 57,470.00 USD | 17,410.00 USD | 9,970.00 USD |
| `7D` | `0.9430` | 288,780.00 USD | 288,780.00 USD | 0.00 USD | 45,490.00 USD | 0.00 USD | 12,520.00 USD |
| `1D` | `0.9440` | 666,210.00 USD | 666,210.00 USD | 0.00 USD | 149,360.00 USD | 7,300.00 USD | 17,630.00 USD |
| `7D` | `0.9450` | 670,070.00 USD | 670,070.00 USD | 0.00 USD | 261,930.00 USD | 48,260.00 USD | 71,090.00 USD |
| `1D` | `0.9460` | 807,210.00 USD | 807,210.00 USD | 0.00 USD | 80,840.00 USD | 31,690.00 USD | 28,470.00 USD |
| `7D` | `0.9470` | 947,170.00 USD | 947,170.00 USD | 0.00 USD | 200,510.00 USD | 0.00 USD | 76,590.00 USD |
| `1D` | `0.9480` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 155,950.00 USD | 8,800.00 USD | 74,030.00 USD |
| `7D` | `0.9490` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 193,040.00 USD | 10,340.00 USD | 178,870.00 USD |
| `1D` | `0.9500` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 107,250.00 USD | 15,500.00 USD | 2,230.00 USD |
| `7D` | `0.9510` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 242,000.00 USD | 27,670.00 USD | 117,190.00 USD |
| `1D` | `0.9520` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 47,190.00 USD | 13,390.00 USD | 44,330.00 USD |
| `7D` | `0.9530` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 1,940.00 USD | 121,100.00 USD |
| `1D` | `0.9540` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 43,540.00 USD | 7,980.00 USD | 29,110.00 USD |
| `7D` | `0.9550` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 19,730.00 USD | 18,890.00 USD |
| `1D` | `0.9560` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 865.00 USD | 7,070.00 USD | 275.27 USD |
| `7D` | `0.9570` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 1,910.00 USD | 0.00 USD | 957.94 USD |
| `1D` | `0.9580` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 3,480.00 USD | 1,660.00 USD | 313.25 USD |
| `7D` | `0.9590` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 1,980.00 USD | 4,660.00 USD | 866.69 USD |
| `1D` | `0.9600` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 5,890.00 USD | 1,550.00 USD |
| `7D` | `0.9610` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 24,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9620` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 51,070.00 USD | 8,170.00 USD | 12,810.00 USD |
| `7D` | `0.9630` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 53,510.00 USD | 24,130.00 USD | 481.70 USD |
| `1D` | `0.9640` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 17,560.00 USD | 25,430.00 USD | 27,630.00 USD |
| `7D` | `0.9650` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 51,500.00 USD | 0.00 USD | 12,330.00 USD |
| `1D` | `0.9660` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 2,450.00 USD | 4,480.00 USD | 37,020.00 USD |
| `7D` | `0.9670` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 38,090.00 USD | 5,170.00 USD | 0.00 USD |
| `1D` | `0.9680` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 24,830.00 USD | 7,940.00 USD | 0.00 USD |
| `7D` | `0.9690` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 20,550.00 USD | 20,150.00 USD |
| `1D` | `0.9700` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 2,090.00 USD | 19,970.00 USD |
| `7D` | `0.9710` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD |
| `1D` | `0.9720` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 24,360.00 USD | 174.50 USD | 23,100.00 USD |
| `7D` | `0.9730` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 2,910.00 USD | 9,050.00 USD | 7,510.00 USD |
| `1D` | `0.9740` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 25,800.00 USD | 5,170.00 USD | 14,620.00 USD |
| `7D` | `0.9750` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 4,890.00 USD |
| `1D` | `0.9760` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 53,340.00 USD | 13,960.00 USD | 8,400.00 USD |
| `7D` | `0.9770` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD |
| `1D` | `0.9780` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 39,740.00 USD | 3,080.00 USD | 17,920.00 USD |
| `7D` | `0.9790` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 84,920.00 USD |
| `1D` | `0.9800` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 29,240.00 USD | 9,580.00 USD | 20,800.00 USD |
| `7D` | `0.9810` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 540.00 USD | 0.00 USD | 118,820.00 USD |
| `1D` | `0.9820` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 16,350.00 USD | 12,220.00 USD | 6,870.00 USD |
| `7D` | `0.9830` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 102,710.00 USD | 15,810.00 USD | 52,260.00 USD |
| `1D` | `0.9840` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 665.59 USD | 13,370.00 USD | 38,710.00 USD |
| `7D` | `0.9850` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 211.77 USD | 22,300.00 USD |
| `1D` | `0.9860` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 50,550.00 USD | 3,510.00 USD | 19,890.00 USD |
| `7D` | `0.9870` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 57,740.00 USD |
| `1D` | `0.9880` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 17,200.00 USD | 130.81 USD | 14,320.00 USD |
| `7D` | `0.9890` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `0.9900` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 57,390.00 USD | 1,300.00 USD | 13,390.00 USD |
| `7D` | `0.9910` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD |
| `1D` | `0.9920` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 9,210.00 USD | 2,900.00 USD | 13,340.00 USD |
| `7D` | `0.9930` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `0.9940` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 12,310.00 USD | 13,250.00 USD | 1,420.00 USD |
| `7D` | `0.9950` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 33,790.00 USD | 5,380.00 USD | 42,770.00 USD |
| `1D` | `0.9960` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 18,530.00 USD | 4,110.00 USD | 0.00 USD |
| `7D` | `0.9970` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 69,270.00 USD | 0.00 USD | 4,670.00 USD |
| `1D` | `0.9980` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 40,410.00 USD | 4,790.00 USD | 10,500.00 USD |
| `7D` | `0.9990` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 156.00 USD | 462.12 USD |
| `1D` | `1.00` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 59,960.00 USD | 27,710.00 USD | 1,340.00 USD |
| `7D` | `1.00` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.00` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 501.30 USD | 0.00 USD | 266.05 USD |
| `7D` | `1.00` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 105,770.00 USD | 21,740.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 10,110.00 USD | 9,540.00 USD | 9,410.00 USD |
| `7D` | `1.00` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 32,430.00 USD | 3,970.00 USD | 1,470.00 USD |
| `1D` | `1.01` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 101,040.00 USD | 10,140.00 USD | 31,440.00 USD |
| `7D` | `1.01` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 34,110.00 USD | 0.00 USD | 29,210.00 USD |
| `1D` | `1.01` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 20,070.00 USD | 9,160.00 USD | 27,730.00 USD |
| `7D` | `1.01` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD |
| `1D` | `1.01` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 10,530.00 USD | 14,710.00 USD | 0.00 USD |
| `7D` | `1.01` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 20,090.00 USD | 14,180.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 16,480.00 USD | 25,380.00 USD | 265.91 USD |
| `7D` | `1.01` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD |
| `1D` | `1.01` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 6,250.00 USD | 4,410.00 USD | 25,160.00 USD |
| `7D` | `1.01` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 26,510.00 USD | 7,420.00 USD |
| `1D` | `1.02` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 20,120.00 USD | 2,880.00 USD | 22,170.00 USD |
| `7D` | `1.02` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD |
| `1D` | `1.02` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 24,880.00 USD | 8,530.00 USD | 25,750.00 USD |
| `7D` | `1.02` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 16,530.00 USD | 83,360.00 USD | 11,810.00 USD |
| `1D` | `1.02` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 52,040.00 USD | 8,850.00 USD | 20,560.00 USD |
| `7D` | `1.02` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 61,450.00 USD | 32,840.00 USD | 68,370.00 USD |
| `1D` | `1.02` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 51,380.00 USD | 3,710.00 USD | 36,250.00 USD |
| `7D` | `1.02` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 82,230.00 USD | 85,890.00 USD | 146,060.00 USD |
| `1D` | `1.02` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 59,910.00 USD | 27,540.00 USD | 53,210.00 USD |
| `7D` | `1.02` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD |
| `1D` | `1.03` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 52,630.00 USD | 18,370.00 USD | 20,210.00 USD |
| `7D` | `1.03` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 161,070.00 USD | 127,000.00 USD | 25,260.00 USD |
| `1D` | `1.03` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 31,340.00 USD | 10,940.00 USD | 18,480.00 USD |
| `7D` | `1.03` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD |
| `1D` | `1.03` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 95,330.00 USD | 24,510.00 USD | 33,610.00 USD |
| `7D` | `1.03` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD |
| `1D` | `1.03` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 67,770.00 USD | 8,980.00 USD | 33,530.00 USD |
| `7D` | `1.03` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD |
| `1D` | `1.03` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 19,370.00 USD | 9,210.00 USD | 18,890.00 USD |
| `7D` | `1.03` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 259,060.00 USD | 8,290.00 USD | 43,490.00 USD |
| `1D` | `1.04` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 3,240.00 USD | 9,270.00 USD | 2,730.00 USD |
| `7D` | `1.04` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 192,080.00 USD | 3,170.00 USD | 109,460.00 USD |
| `7D` | `1.04` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 239,580.00 USD | 9,010.00 USD | 117,630.00 USD |
| `7D` | `1.04` | 6,460,000.00 USD | 6,460,000.00 USD | 0.00 USD | 276,890.00 USD | 2,090.00 USD | 159,500.00 USD |
| `7D` | `1.04` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD |
| `7D` | `1.04` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD |
| `7D` | `1.05` | 7,430,000.00 USD | 7,430,000.00 USD | 0.00 USD | 178,890.00 USD | 96,370.00 USD | 238,570.00 USD |
| `7D` | `1.05` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 116,670.00 USD | 13,780.00 USD | 77,320.00 USD |
| `7D` | `1.05` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 175,350.00 USD | 43,690.00 USD | 87,370.00 USD |
| `7D` | `1.05` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 68,590.00 USD | 58,070.00 USD | 74,380.00 USD |
| `7D` | `1.05` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 125,020.00 USD | 33,860.00 USD | 72,330.00 USD |
| `7D` | `1.06` | 8,780,000.00 USD | 8,780,000.00 USD | 0.00 USD | 218,860.00 USD | 70,000.00 USD | 106,380.00 USD |
| `7D` | `1.06` | 9,240,000.00 USD | 9,240,000.00 USD | 0.00 USD | 240,060.00 USD | 74,380.00 USD | 145,470.00 USD |
| `7D` | `1.06` | 9,510,000.00 USD | 9,510,000.00 USD | 0.00 USD | 140,850.00 USD | 56,310.00 USD | 78,020.00 USD |
| `7D` | `1.06` | 9,800,000.00 USD | 9,800,000.00 USD | 0.00 USD | 141,700.00 USD | 73,690.00 USD | 71,340.00 USD |
| `7D` | `1.06` | 10,010,000.00 USD | 10,010,000.00 USD | 0.00 USD | 90,670.00 USD | 28,390.00 USD | 95,080.00 USD |
| `7D` | `1.07` | 10,220,000.00 USD | 10,220,000.00 USD | 0.00 USD | 86,760.00 USD | 43,390.00 USD | 82,980.00 USD |
| `7D` | `1.07` | 10,520,000.00 USD | 10,520,000.00 USD | 0.00 USD | 219,670.00 USD | 14,440.00 USD | 62,270.00 USD |
| `7D` | `1.07` | 10,750,000.00 USD | 10,750,000.00 USD | 0.00 USD | 141,570.00 USD | 36,670.00 USD | 52,290.00 USD |
| `7D` | `1.07` | 10,990,000.00 USD | 10,990,000.00 USD | 0.00 USD | 96,630.00 USD | 42,960.00 USD | 95,510.00 USD |
| `7D` | `1.07` | 11,170,000.00 USD | 11,170,000.00 USD | 0.00 USD | 97,650.00 USD | 27,560.00 USD | 60,670.00 USD |
| `7D` | `1.08` | 11,330,000.00 USD | 11,330,000.00 USD | 0.00 USD | 75,040.00 USD | 29,910.00 USD | 48,910.00 USD |
| `7D` | `1.08` | 11,570,000.00 USD | 11,570,000.00 USD | 0.00 USD | 166,380.00 USD | 21,060.00 USD | 52,480.00 USD |
| `7D` | `1.08` | 11,790,000.00 USD | 11,790,000.00 USD | 0.00 USD | 164,440.00 USD | 26,480.00 USD | 33,950.00 USD |
| `7D` | `1.08` | 11,990,000.00 USD | 11,990,000.00 USD | 0.00 USD | 61,330.00 USD | 41,110.00 USD | 100,750.00 USD |
| `7D` | `1.08` | 12,150,000.00 USD | 12,150,000.00 USD | 0.00 USD | 86,400.00 USD | 18,540.00 USD | 46,440.00 USD |
| `7D` | `1.09` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 102,510.00 USD | 58,170.00 USD | 69,640.00 USD |
| `7D` | `1.09` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 71,650.00 USD | 23,140.00 USD | 85,300.00 USD |
| `7D` | `1.09` | 12,690,000.00 USD | 12,690,000.00 USD | 0.00 USD | 70,660.00 USD | 25,660.00 USD | 32,870.00 USD |
| `7D` | `1.09` | 12,850,000.00 USD | 12,850,000.00 USD | 0.00 USD | 59,760.00 USD | 39,220.00 USD | 62,330.00 USD |
| `7D` | `1.09` | 13,020,000.00 USD | 13,020,000.00 USD | 0.00 USD | 54,830.00 USD | 22,740.00 USD | 92,520.00 USD |
| `7D` | `1.10` | 13,160,000.00 USD | 13,160,000.00 USD | 0.00 USD | 92,660.00 USD | 13,380.00 USD | 38,150.00 USD |
| `7D` | `1.10` | 13,490,000.00 USD | 13,490,000.00 USD | 0.00 USD | 188,000.00 USD | 49,370.00 USD | 89,650.00 USD |
| `7D` | `1.10` | 13,670,000.00 USD | 13,670,000.00 USD | 0.00 USD | 122,300.00 USD | 44,140.00 USD | 15,590.00 USD |
| `7D` | `1.10` | 13,890,000.00 USD | 13,890,000.00 USD | 0.00 USD | 91,720.00 USD | 19,140.00 USD | 110,190.00 USD |
| `7D` | `1.10` | 13,960,000.00 USD | 13,960,000.00 USD | 0.00 USD | 22,500.00 USD | 10,390.00 USD | 31,450.00 USD |
| `7D` | `1.11` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 51,840.00 USD | 24,350.00 USD | 34,190.00 USD |
| `7D` | `1.11` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 80,930.00 USD | 42,230.00 USD | 56,110.00 USD |
| `7D` | `1.11` | 14,400,000.00 USD | 14,400,000.00 USD | 0.00 USD | 77,150.00 USD | 17,970.00 USD | 64,910.00 USD |
| `7D` | `1.11` | 14,500,000.00 USD | 14,500,000.00 USD | 0.00 USD | 28,830.00 USD | 43,570.00 USD | 25,640.00 USD |
| `7D` | `1.11` | 14,550,000.00 USD | 14,550,000.00 USD | 0.00 USD | 32,810.00 USD | 6,650.00 USD | 9,420.00 USD |
| `7D` | `1.12` | 14,710,000.00 USD | 14,710,000.00 USD | 0.00 USD | 75,790.00 USD | 45,980.00 USD | 32,030.00 USD |
| `7D` | `1.12` | 14,770,000.00 USD | 14,770,000.00 USD | 0.00 USD | 24,700.00 USD | 22,760.00 USD | 13,750.00 USD |
| `7D` | `1.12` | 14,870,000.00 USD | 14,870,000.00 USD | 0.00 USD | 49,110.00 USD | 30,950.00 USD | 23,330.00 USD |
| `7D` | `1.12` | 14,960,000.00 USD | 14,960,000.00 USD | 0.00 USD | 61,780.00 USD | 7,080.00 USD | 25,460.00 USD |
| `7D` | `1.12` | 15,020,000.00 USD | 15,020,000.00 USD | 0.00 USD | 18,300.00 USD | 10,940.00 USD | 29,890.00 USD |
| `7D` | `1.13` | 15,050,000.00 USD | 15,050,000.00 USD | 0.00 USD | 14,700.00 USD | 342.11 USD | 8,690.00 USD |
| `7D` | `1.13` | 15,150,000.00 USD | 15,150,000.00 USD | 0.00 USD | 46,320.00 USD | 11,080.00 USD | 45,770.00 USD |
| `7D` | `1.13` | 15,350,000.00 USD | 15,350,000.00 USD | 0.00 USD | 95,750.00 USD | 12,730.00 USD | 90,150.00 USD |
| `7D` | `1.13` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 77,640.00 USD | 4,280.00 USD | 27,360.00 USD |
| `7D` | `1.14` | 15,550,000.00 USD | 15,550,000.00 USD | 0.00 USD | 16,300.00 USD | 10,920.00 USD | 61,260.00 USD |
| `7D` | `1.14` | 15,560,000.00 USD | 15,560,000.00 USD | 0.00 USD | 4,780.00 USD | 4,820.00 USD | 6,530.00 USD |
| `7D` | `1.14` | 15,600,000.00 USD | 15,600,000.00 USD | 0.00 USD | 2,980.00 USD | 0.00 USD | 35,230.00 USD |
| `7D` | `1.14` | 15,650,000.00 USD | 15,650,000.00 USD | 0.00 USD | 36,300.00 USD | 8,480.00 USD | 6,790.00 USD |
| `7D` | `1.14` | 15,730,000.00 USD | 15,730,000.00 USD | 0.00 USD | 36,560.00 USD | 1,660.00 USD | 37,230.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `193.97M` | Total OI Tokens: `211,878,788.8 DOT`
  * 1h OI Change: `-0.37%` | 4h OI Change: `-6.42%` | 24h OI Change: `-11.16%`
  * Exchange Breakdown: Binance=`33.84M` | Bybit=`21.77M` | OKX=`9.81M` | Hyperliquid=`5.46M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-1.96K` | Last 24h: `7.91K` | Last 3d: `-10.37K` | Last 7d: `-19.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0053%` | **USDT OKX** | `-0.0139%` |
| **USDT Bybit** | `0.0053%` | **USDT KuCoin** | `0.0022%` |
| **USDT MEXC** | `-0.0054%` | **USDT BingX** | `0.0049%` |
| **USDT Gate** | `-0.0005%` | **USDT Bitget** | `-0.0145%` |
| **CoinM Binance** | `-0.0043%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `42.84%` | `57.16%` | `0.75` | 29,970,000.00 USD |
| `15M` | `Binance` | `44.8%` | `55.2%` | `0.81` | 11,750,000.00 USD |
| `15M` | `OKX` | `38.87%` | `61.13%` | `0.64` | 3,220,000.00 USD |
| `15M` | `Bybit` | `40.79%` | `59.21%` | `0.69` | 4,850,000.00 USD |
| `15M` | `KuCoin` | `40.93%` | `59.07%` | `0.69` | 188,270.00 USD |
| `15M` | `Gate` | `46.57%` | `53.43%` | `0.87` | 698,740.00 USD |
| `15M` | `Bitget` | `42.29%` | `57.71%` | `0.73` | 1,080,000.00 USD |
| `15M` | `BingX` | `30.82%` | `69.18%` | `0.45` | 1,620,000.00 USD |
| `15M` | `MEXC` | `31.92%` | `68.08%` | `0.47` | 1,170,000.00 USD |
| `15M` | `Bitunix` | `44.56%` | `55.44%` | `0.80` | 591,730.00 USD |
| `15M` | `Hyperliquid` | `39.47%` | `60.53%` | `0.65` | 3,210,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `44.36%` | `55.64%` | `0.80` | 116,860.00 USD |
| `15M` | `Crypto.com` | `25.57%` | `74.43%` | `0.34` | 796.26 USD |
| `15M` | `WhiteBIT` | `85.01%` | `14.99%` | `5.67` | 966,470.00 USD |
| `15M` | `HTX` | `45.76%` | `54.24%` | `0.84` | 24,940.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `40.25%` | `59.75%` | `0.67` | 352,670.00 USD |
| `15M` | `Aster` | `10.3%` | `89.7%` | `0.11` | 13,320.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `48.49%` | `51.51%` | `0.94` | 111,600.00 USD |
| `15M` | `Whale Positions` | `44.8%` | `55.2%` | `0.81` | 11,750,000.00 USD |
| `15M` | `Global Accounts` | `42.84%` | `57.16%` | `0.75` | 29,970,000.00 USD |
| `1H` | `DOT` | `47.75%` | `52.25%` | `0.91` | 50,710,000.00 USD |
| `1H` | `Binance` | `50.91%` | `49.09%` | `1.04` | 17,680,000.00 USD |
| `1H` | `OKX` | `53.98%` | `46.02%` | `1.17` | 7,000,000.00 USD |
| `1H` | `Bybit` | `44.69%` | `55.31%` | `0.81` | 6,440,000.00 USD |
| `1H` | `KuCoin` | `42.04%` | `57.96%` | `0.73` | 614,150.00 USD |
| `1H` | `Gate` | `34.48%` | `65.52%` | `0.53` | 2,210,000.00 USD |
| `1H` | `Bitget` | `57.2%` | `42.8%` | `1.34` | 4,530,000.00 USD |
| `1H` | `BingX` | `37.01%` | `62.99%` | `0.59` | 1,620,000.00 USD |
| `1H` | `MEXC` | `41.01%` | `58.99%` | `0.70` | 4,410,000.00 USD |
| `1H` | `Bitunix` | `53.42%` | `46.58%` | `1.15` | 1,390,000.00 USD |
| `1H` | `Hyperliquid` | `54.48%` | `45.52%` | `1.20` | 1,850,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.9%` | `51.1%` | `0.96` | 454,380.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `12.81%` | `87.19%` | `0.15` | 1,760,000.00 USD |
| `1H` | `HTX` | `36.39%` | `63.61%` | `0.57` | 69,760.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `44.03%` | `55.97%` | `0.79` | 517,280.00 USD |
| `1H` | `Aster` | `60.76%` | `39.24%` | `1.55` | 110,090.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `45.02%` | `54.98%` | `0.82` | 57,600.00 USD |
| `1H` | `Whale Positions` | `50.91%` | `49.09%` | `1.04` | 17,680,000.00 USD |
| `1H` | `Global Accounts` | `47.75%` | `52.25%` | `0.91` | 50,710,000.00 USD |
| `4H` | `DOT` | `47.93%` | `52.07%` | `0.92` | 758,250,000.00 USD |
| `4H` | `Binance` | `47.99%` | `52.01%` | `0.92` | 298,920,000.00 USD |
| `4H` | `OKX` | `48.61%` | `51.39%` | `0.95` | 88,260,000.00 USD |
| `4H` | `Bybit` | `49.68%` | `50.32%` | `0.99` | 102,110,000.00 USD |
| `4H` | `KuCoin` | `49.83%` | `50.17%` | `0.99` | 5,630,000.00 USD |
| `4H` | `Gate` | `47.79%` | `52.21%` | `0.92` | 10,590,000.00 USD |
| `4H` | `Bitget` | `46.45%` | `53.55%` | `0.87` | 30,830,000.00 USD |
| `4H` | `BingX` | `44.13%` | `55.87%` | `0.79` | 33,580,000.00 USD |
| `4H` | `MEXC` | `46.76%` | `53.24%` | `0.88` | 43,970,000.00 USD |
| `4H` | `Bitunix` | `50.76%` | `49.24%` | `1.03` | 17,920,000.00 USD |
| `4H` | `Hyperliquid` | `43.72%` | `56.28%` | `0.78` | 86,210,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.68%` | `49.32%` | `1.03` | 5,070,000.00 USD |
| `4H` | `Crypto.com` | `49.5%` | `50.5%` | `0.98` | 48,410.00 USD |
| `4H` | `WhiteBIT` | `65.42%` | `34.58%` | `1.89` | 14,140,000.00 USD |
| `4H` | `HTX` | `46.85%` | `53.15%` | `0.88` | 1,010,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.26%` | `50.74%` | `0.97` | 13,450,000.00 USD |
| `4H` | `Aster` | `50.97%` | `49.03%` | `1.04` | 2,360,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `44.51%` | `55.49%` | `0.80` | 4,150,000.00 USD |
| `4H` | `Whale Positions` | `47.99%` | `52.01%` | `0.92` | 298,920,000.00 USD |
| `4H` | `Global Accounts` | `47.93%` | `52.07%` | `0.92` | 758,250,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.9157` | `0.9093` | `0.9157` | `0.9241` | `0.8893` | 9,166,573.96 USD | 4,231,807.53 USD | 4,934,766.43 USD | -702,958.89 USD | `-7.67%` | `6B / 13S` |
| `0:00 UTC` | `0.9138` | `0.9204` | `0.9138` | `0.9302` | `0.9076` | 3,388,598.53 USD | 1,615,651.50 USD | 1,772,947.04 USD | -157,295.54 USD | `-4.64%` | `11B / 8S` |
| `5:00 UTC` | `0.9302` | `0.9320` | `0.9302` | `0.9392` | `0.9254` | 2,028,309.51 USD | 996,075.55 USD | 1,032,233.96 USD | -36,158.40 USD | `-1.78%` | `11B / 12S` |
| `0:00 UTC` | `0.9301` | `0.9318` | `0.9301` | `0.9381` | `0.9248` | 1,862,169.82 USD | 558,080.50 USD | 1,304,089.32 USD | -746,008.82 USD | `-40.06%` | `17B / 36S` |
| `5:00 UTC` | `0.9251` | `0.9254` | `0.9251` | `0.9294` | `0.9219` | 1,343,196.16 USD | 526,839.48 USD | 816,356.69 USD | -289,517.21 USD | `-21.55%` | `18B / 7S` |
| `0:00 UTC` | `0.9254` | `0.9217` | `0.9254` | `0.9288` | `0.9143` | 1,982,933.95 USD | 1,080,771.49 USD | 902,162.47 USD | 178,609.02 USD | `+9.01%` | `16B / 22S` |
| `5:00 UTC` | `0.9313` | `0.9286` | `0.9313` | `0.9327` | `0.9201` | 1,171,136.75 USD | 631,208.27 USD | 539,928.48 USD | 91,279.80 USD | `+7.79%` | `19B / 8S` |
| `0:00 UTC` | `0.9294` | `0.9281` | `0.9294` | `0.9324` | `0.9237` | 735,316.47 USD | 385,478.28 USD | 349,838.19 USD | 35,640.09 USD | `+4.85%` | `10B / 6S` |
| `5:00 UTC` | `0.9227` | `0.9239` | `0.9227` | `0.9277` | `0.9214` | 634,270.61 USD | 320,926.00 USD | 313,344.61 USD | 7,581.39 USD | `+1.20%` | `5B / 8S` |
| `0:00 UTC` | `0.9151` | `0.9183` | `0.9151` | `0.9248` | `0.9144` | 969,604.37 USD | 405,159.82 USD | 564,444.55 USD | -159,284.73 USD | `-16.43%` | `11B / 17S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:39` | `Volume 1.0M DOT` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 19:19` | `Range 0.005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.9951` | 122,000.00 USD | 0.00 USD |
| `10-28 19:07` | `Volume 1.0M DOT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.01` | 333,000.00 USD | 0.00 USD |
| `10-28 19:01` | `Range 0.005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 18:58` | `Volume 1.0M DOT` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 18:40` | `Volume 1.0M DOT` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.9970` | 0.00 USD | 0.00 USD |
| `10-28 18:31` | `Range 0.005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.9987` | 0.00 USD | 0.00 USD |
| `10-28 18:31` | `Range 0.005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.00` | 219,000.00 USD | 0.00 USD |
| `10-28 18:30` | `Volume 1.0M DOT` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.9987` | 0.00 USD | 0.00 USD |
| `10-28 18:30` | `Volume 1.0M DOT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.00` | 221,000.00 USD | 0.00 USD |
| `10-28 18:19` | `Range 0.005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9972` | 0.00 USD | 0.00 USD |
| `10-28 18:16` | `Volume 1.0M DOT` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9972` | 0.00 USD | 0.00 USD |
| `10-28 17:55` | `Volume 1.0M DOT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.01` | 229,000.00 USD | 0.00 USD |
| `10-28 17:46` | `Range 0.005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.01` | 260,000.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 1.0M DOT` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.01` | 0.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 1.0M DOT` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `1.00` | 0.00 USD | 0.00 USD |
| `10-28 11:08` | `Range 0.005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1.00` | 0.00 USD | 0.00 USD |
| `10-28 09:02` | `Range 0.005` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `1.01` | 363,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 0.00 USD | -41,570.00 USD | **`DISTRIBUTION`** |
| `15m` | 0.00 USD | 68,100.00 USD | **`ACCUMULATION`** |
| `30m` | 0.00 USD | 22,450.00 USD | **`ACCUMULATION`** |
| `1h` | 0.00 USD | 403,880.00 USD | **`ACCUMULATION`** |
| `2h` | 0.00 USD | -178,600.00 USD | **`DISTRIBUTION`** |
| `4h` | 0.00 USD | -6,080,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 0.00 USD | -6,250,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 0.00 USD | -7,590,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 0.00 USD | -7,790,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 0.00 USD | -7,370,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 0.00 USD | -24,130,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 0.00 USD | -78,790,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`-41.57K` | 15m=`+68.10K` | 1h=`+403.88K` | 24h=`-7.37M`
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
  * Execution Entry: `0.9099` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8650` (Risk Distance: `0.0449` pts)
  * +2.5R Take Profit: `1.02`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9208` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9657` (Risk Distance: `0.0449` pts)
  * +2.5R Take Profit: `0.8087`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9223`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
