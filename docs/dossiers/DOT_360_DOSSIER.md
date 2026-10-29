# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 22:42:57 IST` (`2026-10-29 17:12:57 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9930` | **Live Ask Quote**: `1.01` | **Mid Price**: `1.00`
- **Spread Points**: `20.00` | **Spread BPS**: `199.40 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9773` | VWAP Z-Score: `+1.13` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0073` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `55.39` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.02` | Lower -3.00σ Band: `0.9328`
  * Upper +2.51σ Band: `1.01` | Lower -2.51σ Band: `0.9401`
  * Upper +2.01σ Band: `1.01` | Lower -2.01σ Band: `0.9475`
  * Upper +2.00σ Band: `1.01` | Lower -2.00σ Band: `0.9476`
  * Upper +1.28σ Band: `0.9963` | Lower -1.28σ Band: `0.9583`
  * Upper +1.00σ Band: `0.9921` | Lower -1.00σ Band: `0.9624`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9960` | EMA-20=`0.9909` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9840` (Slope: `+0.0000`) | EMA-100=`0.9838`
  * Institutional Anchors: EMA-144=`0.9848` | EMA-200=`0.9853` (Slope: `+0.1400`) | EMA-233=`0.9851`
- **Range Boundaries**: 24H High=`1.03` | 24H Low=`0.9510` | Weekly High=`1.03` | Weekly Low=`0.9510`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9952` (Distance: `+0.73%`)
  * Point of Control (POC) = `0.9630` (Distance: `+4.10%`)
  * Value Area Low (VAL) = `0.9512` (Distance: `+5.39%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.00` | POC=`0.9890` | VAL=`0.9812`
  * Prior Day Extremes: PDH=`1.03` | PDL=`0.9690` | PDC=`1.01`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.01` | Weekly POC=`0.9929` | Weekly VAL=`0.9785`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.02` | Low=`0.9510`
  * London Session (08:00-16:00 UTC): High=`0.9850` | Low=`0.9600`
  * New York Session (13:00-21:00 UTC): High=`1.01` | Low=`0.9680`
  * Initial Balance (First Hour): IB High=`0.9800` | IB Low=`0.9670`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9990` - `1.01`
  * Optimal Trade Entry (OTE 0.705): `1.01`
  * Structural Invalidation Anchor (0.786): `1.01`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.01` | `1.01` | `1.00` | `1.00` | `129,278` | 129,921.52 USD | -62,807.96 USD | `-48.34%` | -1,565,438.25 USD | `-0.30` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.00` | `1.01` | `1.00` | `1.01` | `90,476` | 90,950.37 USD | -23,214.13 USD | `-25.52%` | -1,588,652.38 USD | `-0.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `1.01` | `1.01` | `1.00` | `1.00` | `129,929` | 130,580.82 USD | -7,806.81 USD | `-5.98%` | -1,596,459.18 USD | `+0.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `1.01` | `1.01` | `1.00` | `1.01` | `600,859` | 605,145.48 USD | -119,535.19 USD | `-19.75%` | -1,452,155.87 USD | `-0.41` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.01` | `1.01` | `1.00` | `1.01` | `365,323` | 367,151.31 USD | -135,823.89 USD | `-36.99%` | -1,587,979.76 USD | `-0.48` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `1.01` | `1.01` | `1.00` | `1.00` | `138,986` | 139,664.41 USD | -15,321.78 USD | `-10.97%` | -1,603,301.54 USD | `+0.15` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.00` | `1.02` | `1.00` | `1.02` | `3,661,852` | 3,701,825.02 USD | 193,813.22 USD | `+5.24%` | -902,386.24 USD | `+0.71` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.02` | `1.02` | `1.00` | `1.01` | `2,867,696` | 2,902,881.51 USD | -734,347.44 USD | `-25.30%` | -1,636,733.68 USD | `-2.29` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.01` | `1.01` | `1.00` | `1.00` | `129,929` | 130,580.82 USD | -7,806.81 USD | `-5.98%` | -1,644,540.49 USD | `+0.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | -137,778.42 USD | `+0.23` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -315,355.23 USD | `-0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `1.00` | `1.00` | `2,997,625` | 3,033,462.33 USD | -742,154.25 USD | `-24.47%` | -1,057,509.48 USD | `-1.15` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.01` | `1.01` | `0.9612` | `0.9700` | `15,616,467` | 15,304,422.31 USD | 595,816.59 USD | `+3.89%` | -236,044.76 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.9699` | `0.9906` | `0.9674` | `0.9732` | `8,505,701` | 8,320,368.15 USD | 13,201.93 USD | `+0.16%` | -222,842.83 USD | `+0.15` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | -137,778.42 USD | `+0.23` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -315,355.23 USD | `-0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `1.00` | `1.00` | `2,997,625` | 3,033,462.33 USD | -742,154.25 USD | `-24.47%` | -1,057,509.48 USD | `-1.15` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`1.00`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:34:53 IST` |

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
  * 24H Horizon: Short MP=`1.01` (Vol: 78,500.00 USD, Dist: `+1.08%`) | Long MP=`0.9649` (Vol: 113,700.00 USD, Dist: `--3.29%`)
  * 48H Horizon: Short MP=`1.01` (Vol: 80,100.00 USD, Dist: `+1.28%`) | Long MP=`0.9510` (Vol: 124,200.00 USD, Dist: `--4.68%`)
  * 3D Horizon: Short MP=`1.05` (Vol: 92,800.00 USD, Dist: `+4.85%`) | Long MP=`0.9510` (Vol: 130,500.00 USD, Dist: `--4.68%`)
  * 7D Horizon: Short MP=`1.07` (Vol: 211,000.00 USD, Dist: `+7.08%`) | Long MP=`0.9606` (Vol: 177,500.00 USD, Dist: `--3.72%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2350` | 424.34 USD | 495,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2550` | 127.50 USD | 495,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3250` | 717.93 USD | 494,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 106.97 USD | 494,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 1,970.00 USD | 494,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 722.66 USD | 492,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 9,150.00 USD | 491,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 156.62 USD | 482,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 2,770.00 USD | 482,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 182.32 USD | 479,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 2,560.00 USD | 479,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 4,770.00 USD | 476,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 106.55 USD | 471,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 173.88 USD | 471,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 572.80 USD | 471,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 140.64 USD | 470,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 136.48 USD | 470,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 3,390.00 USD | 470,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 3,280.00 USD | 467,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 254.00 USD | 463,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 526.19 USD | 463,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 867.92 USD | 463,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 24,800.00 USD | 462,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 148.42 USD | 437,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 421.54 USD | 437,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 3,460.00 USD | 436,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 321.92 USD | 433,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 16,630.00 USD | 433,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 1,310.00 USD | 416,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 3,720.00 USD | 415,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 3,740.00 USD | 411,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 2,720.00 USD | 407,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 839.82 USD | 405,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 1,590.00 USD | 404,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 20,560.00 USD | 402,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 16,510.00 USD | 382,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 1,510.00 USD | 365,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 648.98 USD | 364,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 3,840.00 USD | 363,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 9,330.00 USD | 359,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 2,500.00 USD | 350,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 618.51 USD | 347,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 1,080.00 USD | 347,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 1,110.00 USD | 346,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 9,090.00 USD | 344,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 4,330.00 USD | 335,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9000` | 2,550,000.00 USD | 2,550,000.00 USD | 5,710.00 USD | 2,320.00 USD | 2,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9000` | 2,560,000.00 USD | 2,560,000.00 USD | 5,710.00 USD | 2,320.00 USD | 2,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 2,540,000.00 USD | 2,540,000.00 USD | 1,850.00 USD | 3,210.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9020` | 2,550,000.00 USD | 2,550,000.00 USD | 1,850.00 USD | 3,210.00 USD | 2,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9040` | 2,540,000.00 USD | 2,540,000.00 USD | 3,130.00 USD | 2,520.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9040` | 2,540,000.00 USD | 2,540,000.00 USD | 3,130.00 USD | 2,520.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9050` | 946.63 USD | 331,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9060` | 2,530,000.00 USD | 2,530,000.00 USD | 9,620.00 USD | 1,660.00 USD | 111.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9060` | 2,530,000.00 USD | 2,530,000.00 USD | 9,620.00 USD | 1,660.00 USD | 111.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9080` | 2,520,000.00 USD | 2,520,000.00 USD | 5,800.00 USD | 3,150.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9080` | 2,520,000.00 USD | 2,520,000.00 USD | 5,800.00 USD | 3,150.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9100` | 2,500,000.00 USD | 2,500,000.00 USD | 21,910.00 USD | 2,110.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9100` | 2,510,000.00 USD | 2,510,000.00 USD | 21,910.00 USD | 2,110.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9120` | 2,470,000.00 USD | 2,470,000.00 USD | 8,100.00 USD | 228.71 USD | 9,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9120` | 2,480,000.00 USD | 2,480,000.00 USD | 8,100.00 USD | 228.71 USD | 9,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9140` | 2,450,000.00 USD | 2,450,000.00 USD | 5,920.00 USD | 2,890.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9140` | 2,460,000.00 USD | 2,460,000.00 USD | 5,920.00 USD | 2,890.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9150` | 45,280.00 USD | 330,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9160` | 2,440,000.00 USD | 2,440,000.00 USD | 14,110.00 USD | 57.95 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9160` | 2,450,000.00 USD | 2,450,000.00 USD | 14,110.00 USD | 57.95 USD | 4,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9180` | 2,420,000.00 USD | 2,420,000.00 USD | 49.41 USD | 452.74 USD | 583.97 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9180` | 2,430,000.00 USD | 2,430,000.00 USD | 49.41 USD | 452.74 USD | 583.97 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9200` | 2,420,000.00 USD | 2,420,000.00 USD | 2,950.00 USD | 112.72 USD | 192.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9200` | 2,430,000.00 USD | 2,430,000.00 USD | 2,950.00 USD | 112.72 USD | 192.17 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9220` | 2,420,000.00 USD | 2,420,000.00 USD | 7,970.00 USD | 1,070.00 USD | 3,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9220` | 2,420,000.00 USD | 2,420,000.00 USD | 7,970.00 USD | 1,070.00 USD | 3,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9240` | 2,410,000.00 USD | 2,410,000.00 USD | 14,860.00 USD | 5,390.00 USD | 36.99 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9240` | 2,410,000.00 USD | 2,410,000.00 USD | 14,860.00 USD | 5,390.00 USD | 36.99 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9250` | 53,190.00 USD | 285,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9260` | 2,390,000.00 USD | 2,390,000.00 USD | 11,000.00 USD | 9,670.00 USD | 21,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9260` | 2,390,000.00 USD | 2,390,000.00 USD | 11,000.00 USD | 9,670.00 USD | 21,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9280` | 2,340,000.00 USD | 2,340,000.00 USD | 24,160.00 USD | 4,120.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9280` | 2,350,000.00 USD | 2,350,000.00 USD | 24,160.00 USD | 4,120.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9300` | 2,310,000.00 USD | 2,310,000.00 USD | 15,130.00 USD | 1,370.00 USD | 16,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9300` | 2,310,000.00 USD | 2,310,000.00 USD | 15,130.00 USD | 1,370.00 USD | 16,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9320` | 2,280,000.00 USD | 2,280,000.00 USD | 24,390.00 USD | 12,710.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9320` | 2,280,000.00 USD | 2,280,000.00 USD | 24,390.00 USD | 12,710.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9340` | 2,230,000.00 USD | 2,230,000.00 USD | 21,330.00 USD | 11,340.00 USD | 10,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9340` | 2,230,000.00 USD | 2,230,000.00 USD | 21,330.00 USD | 11,340.00 USD | 10,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9350` | 7,100.00 USD | 232,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9360` | 2,180,000.00 USD | 2,180,000.00 USD | 49,310.00 USD | 11,940.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9360` | 2,190,000.00 USD | 2,190,000.00 USD | 49,310.00 USD | 11,940.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9380` | 2,100,000.00 USD | 2,100,000.00 USD | 25,820.00 USD | 14,670.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9380` | 2,110,000.00 USD | 2,110,000.00 USD | 25,820.00 USD | 14,670.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9400` | 2,050,000.00 USD | 2,050,000.00 USD | 23,270.00 USD | 9,580.00 USD | 13,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9400` | 2,060,000.00 USD | 2,060,000.00 USD | 23,270.00 USD | 9,580.00 USD | 13,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9420` | 2,000,000.00 USD | 2,000,000.00 USD | 26,160.00 USD | 11,140.00 USD | 3,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9420` | 2,010,000.00 USD | 2,010,000.00 USD | 26,160.00 USD | 11,140.00 USD | 3,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9440` | 1,960,000.00 USD | 1,960,000.00 USD | 30,630.00 USD | 16,080.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9440` | 1,970,000.00 USD | 1,970,000.00 USD | 30,630.00 USD | 16,080.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9450` | 216,520.00 USD | 225,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9460` | 1,910,000.00 USD | 1,910,000.00 USD | 29,420.00 USD | 29,010.00 USD | 59,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9460` | 1,920,000.00 USD | 1,920,000.00 USD | 29,420.00 USD | 29,010.00 USD | 59,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9480` | 1,790,000.00 USD | 1,790,000.00 USD | 75,700.00 USD | 20,490.00 USD | 27,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9480` | 1,800,000.00 USD | 1,800,000.00 USD | 75,700.00 USD | 20,490.00 USD | 27,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9500` | 1,670,000.00 USD | 1,670,000.00 USD | 56,450.00 USD | 8,300.00 USD | 44,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9500` | 1,670,000.00 USD | 1,670,000.00 USD | 56,450.00 USD | 8,300.00 USD | 44,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9520` | 1,560,000.00 USD | 1,560,000.00 USD | 60,750.00 USD | 33,850.00 USD | 29,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9520` | 1,570,000.00 USD | 1,570,000.00 USD | 60,750.00 USD | 33,850.00 USD | 29,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9540` | 1,440,000.00 USD | 1,440,000.00 USD | 49,960.00 USD | 29,630.00 USD | 31,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9540` | 1,440,000.00 USD | 1,440,000.00 USD | 49,960.00 USD | 29,630.00 USD | 31,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9550` | 8,260.00 USD | 8,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9560` | 1,330,000.00 USD | 1,330,000.00 USD | 133,850.00 USD | 53,740.00 USD | 77,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9560` | 1,330,000.00 USD | 1,330,000.00 USD | 133,850.00 USD | 53,740.00 USD | 77,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9580` | 1,060,000.00 USD | 1,060,000.00 USD | 52,680.00 USD | 30,810.00 USD | 39,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9580` | 1,070,000.00 USD | 1,070,000.00 USD | 52,680.00 USD | 30,810.00 USD | 39,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9600` | 938,020.00 USD | 938,020.00 USD | 75,810.00 USD | 28,100.00 USD | 9,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9600` | 943,490.00 USD | 943,490.00 USD | 75,810.00 USD | 28,100.00 USD | 9,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9620` | 824,290.00 USD | 824,290.00 USD | 40,260.00 USD | 18,850.00 USD | 11,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9620` | 829,770.00 USD | 829,770.00 USD | 40,260.00 USD | 18,850.00 USD | 13,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9640` | 753,850.00 USD | 753,850.00 USD | 11,580.00 USD | 9,650.00 USD | 25,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9640` | 757,500.00 USD | 757,500.00 USD | 11,580.00 USD | 9,650.00 USD | 25,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9660` | 707,350.00 USD | 707,350.00 USD | 31,400.00 USD | 21,230.00 USD | 35,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9660` | 710,990.00 USD | 710,990.00 USD | 31,400.00 USD | 21,230.00 USD | 35,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9680` | 619,570.00 USD | 619,570.00 USD | 39,890.00 USD | 17,500.00 USD | 24,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9680` | 623,220.00 USD | 623,220.00 USD | 39,890.00 USD | 17,500.00 USD | 24,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9700` | 537,910.00 USD | 537,910.00 USD | 46,160.00 USD | 9,430.00 USD | 19,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9700` | 541,560.00 USD | 541,560.00 USD | 46,160.00 USD | 9,430.00 USD | 19,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9720` | 462,620.00 USD | 462,620.00 USD | 33,600.00 USD | 9,090.00 USD | 22,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9720` | 466,270.00 USD | 466,270.00 USD | 33,600.00 USD | 9,090.00 USD | 22,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9740` | 397,900.00 USD | 397,900.00 USD | 3,950.00 USD | 8,490.00 USD | 4,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9740` | 401,550.00 USD | 401,550.00 USD | 3,950.00 USD | 8,490.00 USD | 4,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9750` | 224.54 USD | 224.54 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9760` | 381,150.00 USD | 381,150.00 USD | 19,600.00 USD | 13,960.00 USD | 8,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9760` | 384,800.00 USD | 384,800.00 USD | 19,600.00 USD | 13,960.00 USD | 8,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9780` | 339,240.00 USD | 339,240.00 USD | 23,150.00 USD | 881.37 USD | 8,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9780` | 342,890.00 USD | 342,890.00 USD | 23,150.00 USD | 881.37 USD | 8,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9800` | 306,690.00 USD | 306,690.00 USD | 9,130.00 USD | 3,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9800` | 310,340.00 USD | 310,340.00 USD | 9,130.00 USD | 3,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9820` | 293,960.00 USD | 293,960.00 USD | 0.00 USD | 12,160.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9820` | 297,610.00 USD | 297,610.00 USD | 0.00 USD | 12,160.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9840` | 278,580.00 USD | 278,580.00 USD | 4,700.00 USD | 2,170.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9840` | 278,580.00 USD | 278,580.00 USD | 4,700.00 USD | 2,170.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9860` | 259,760.00 USD | 259,760.00 USD | 8,720.00 USD | 8,090.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9860` | 259,760.00 USD | 259,760.00 USD | 8,720.00 USD | 8,090.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9880` | 241,790.00 USD | 241,790.00 USD | 5,570.00 USD | 1,950.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9880` | 241,790.00 USD | 241,790.00 USD | 5,570.00 USD | 1,950.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9900` | 228,240.00 USD | 228,240.00 USD | 50,430.00 USD | 8,270.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9900` | 228,240.00 USD | 228,240.00 USD | 50,430.00 USD | 8,270.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9920` | 156,150.00 USD | 156,150.00 USD | 9,070.00 USD | 0.00 USD | 20,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9920` | 156,150.00 USD | 156,150.00 USD | 9,070.00 USD | 0.00 USD | 20,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9940` | 126,920.00 USD | 126,920.00 USD | 6,920.00 USD | 14,630.00 USD | 5,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9940` | 126,920.00 USD | 126,920.00 USD | 6,920.00 USD | 14,630.00 USD | 5,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9960` | 99,470.00 USD | 99,470.00 USD | 0.00 USD | 2,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9960` | 99,470.00 USD | 99,470.00 USD | 0.00 USD | 2,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9980` | 96,840.00 USD | 96,840.00 USD | 26,250.00 USD | 0.00 USD | 1,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9980` | 96,840.00 USD | 96,840.00 USD | 26,250.00 USD | 0.00 USD | 1,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.00` | 68,980.00 USD | 68,980.00 USD | 31,780.00 USD | 23,940.00 USD | 13,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.00` | 68,980.00 USD | 68,980.00 USD | 31,780.00 USD | 23,940.00 USD | 13,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 20,100.00 USD | 20,100.00 USD | 17,270.00 USD | 0.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 40,200.00 USD | 40,200.00 USD | 17,270.00 USD | 0.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 17,460.00 USD | 17,460.00 USD | 17,270.00 USD | 0.00 USD | 192.37 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 58,770.00 USD | 58,770.00 USD | 0.00 USD | 0.00 USD | 18,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 36,030.00 USD | 36,030.00 USD | 0.00 USD | 0.00 USD | 18,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 60,010.00 USD | 60,010.00 USD | 1,190.00 USD | 49.40 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 37,260.00 USD | 37,260.00 USD | 1,190.00 USD | 49.40 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 87,930.00 USD | 87,930.00 USD | 0.00 USD | 27,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 65,190.00 USD | 65,190.00 USD | 0.00 USD | 27,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 102,670.00 USD | 102,670.00 USD | 0.00 USD | 21.50 USD | 14,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 79,930.00 USD | 79,930.00 USD | 0.00 USD | 21.50 USD | 14,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 142,800.00 USD | 142,800.00 USD | 20,120.00 USD | 21.80 USD | 19,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 120,060.00 USD | 120,060.00 USD | 20,120.00 USD | 21.80 USD | 19,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 174,020.00 USD | 174,020.00 USD | 1,130.00 USD | 7,410.00 USD | 22,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 151,280.00 USD | 151,280.00 USD | 1,130.00 USD | 7,410.00 USD | 22,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 218,870.00 USD | 218,870.00 USD | 40,090.00 USD | 1,690.00 USD | 3,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 196,130.00 USD | 196,130.00 USD | 40,090.00 USD | 1,690.00 USD | 3,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 262,160.00 USD | 262,160.00 USD | 25,850.00 USD | 991.70 USD | 16,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 243,060.00 USD | 243,060.00 USD | 25,850.00 USD | 991.70 USD | 20,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 362,780.00 USD | 362,780.00 USD | 32,250.00 USD | 24,720.00 USD | 43,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 343,680.00 USD | 343,680.00 USD | 32,250.00 USD | 24,720.00 USD | 43,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 420,870.00 USD | 420,870.00 USD | 32,060.00 USD | 14,590.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 401,770.00 USD | 401,770.00 USD | 32,060.00 USD | 14,590.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 479,230.00 USD | 479,230.00 USD | 31,210.00 USD | 8,670.00 USD | 18,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 460,140.00 USD | 460,140.00 USD | 31,210.00 USD | 8,670.00 USD | 18,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 642,620.00 USD | 642,620.00 USD | 100,250.00 USD | 23,640.00 USD | 39,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 623,530.00 USD | 623,530.00 USD | 100,250.00 USD | 23,640.00 USD | 39,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 768,650.00 USD | 768,650.00 USD | 83,270.00 USD | 6,480.00 USD | 36,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 749,550.00 USD | 749,550.00 USD | 83,270.00 USD | 6,480.00 USD | 36,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 829,080.00 USD | 829,080.00 USD | 35,180.00 USD | 7,080.00 USD | 18,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 809,990.00 USD | 809,990.00 USD | 35,180.00 USD | 7,080.00 USD | 18,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 946,810.00 USD | 946,810.00 USD | 29,120.00 USD | 29,520.00 USD | 59,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 927,720.00 USD | 927,720.00 USD | 29,120.00 USD | 29,520.00 USD | 59,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,060,000.00 USD | 1,060,000.00 USD | 69,240.00 USD | 5,430.00 USD | 38,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 1,040,000.00 USD | 1,040,000.00 USD | 69,240.00 USD | 5,430.00 USD | 38,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,090,000.00 USD | 1,090,000.00 USD | 7,710.00 USD | 8,040.00 USD | 14,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 1,070,000.00 USD | 1,070,000.00 USD | 7,710.00 USD | 8,040.00 USD | 14,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,110,000.00 USD | 1,110,000.00 USD | 1,190.00 USD | 9,870.00 USD | 6,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 1,090,000.00 USD | 1,090,000.00 USD | 1,190.00 USD | 9,870.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,160,000.00 USD | 1,160,000.00 USD | 7,360.00 USD | 14,490.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 1,150,000.00 USD | 1,150,000.00 USD | 7,360.00 USD | 14,490.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,190,000.00 USD | 1,190,000.00 USD | 21,760.00 USD | 4,260.00 USD | 321.14 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 1,170,000.00 USD | 1,170,000.00 USD | 21,760.00 USD | 4,260.00 USD | 321.14 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,210,000.00 USD | 1,210,000.00 USD | 15,080.00 USD | 3,170.00 USD | 4,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 1,190,000.00 USD | 1,190,000.00 USD | 15,080.00 USD | 3,170.00 USD | 4,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,290,000.00 USD | 1,290,000.00 USD | 43,530.00 USD | 11,120.00 USD | 20,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 1,270,000.00 USD | 1,270,000.00 USD | 43,530.00 USD | 11,120.00 USD | 20,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,370,000.00 USD | 1,370,000.00 USD | 32,960.00 USD | 6,990.00 USD | 44,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 1,350,000.00 USD | 1,350,000.00 USD | 32,960.00 USD | 6,990.00 USD | 44,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,390,000.00 USD | 1,390,000.00 USD | 9,000.00 USD | 311.68 USD | 12,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 1,380,000.00 USD | 1,380,000.00 USD | 9,000.00 USD | 311.68 USD | 12,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 156.98 USD | 156.98 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,430,000.00 USD | 1,430,000.00 USD | 7,850.00 USD | 5,710.00 USD | 28,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 1,420,000.00 USD | 1,420,000.00 USD | 7,850.00 USD | 5,710.00 USD | 28,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,490,000.00 USD | 1,490,000.00 USD | 29,750.00 USD | 3,000.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 1,470,000.00 USD | 1,470,000.00 USD | 29,750.00 USD | 3,000.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,510,000.00 USD | 1,510,000.00 USD | 3,730.00 USD | 3,810.00 USD | 10,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 1,490,000.00 USD | 1,490,000.00 USD | 3,730.00 USD | 3,810.00 USD | 10,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,520,000.00 USD | 1,520,000.00 USD | 2,110.00 USD | 7,870.00 USD | 2,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 1,500,000.00 USD | 1,500,000.00 USD | 2,110.00 USD | 7,870.00 USD | 2,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,530,000.00 USD | 1,530,000.00 USD | 5,350.00 USD | 2,520.00 USD | 7,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 1,520,000.00 USD | 1,520,000.00 USD | 5,350.00 USD | 2,520.00 USD | 7,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.06` | 66,030.00 USD | 66,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,560,000.00 USD | 1,560,000.00 USD | 12,610.00 USD | 3,010.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 1,540,000.00 USD | 1,540,000.00 USD | 12,610.00 USD | 3,010.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,570,000.00 USD | 1,570,000.00 USD | 10,690.00 USD | 4,390.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 1,560,000.00 USD | 1,560,000.00 USD | 10,690.00 USD | 4,390.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,590,000.00 USD | 1,590,000.00 USD | 9,230.00 USD | 5,010.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 1,580,000.00 USD | 1,580,000.00 USD | 9,230.00 USD | 5,010.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,620,000.00 USD | 1,620,000.00 USD | 9,330.00 USD | 5,210.00 USD | 11,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 1,600,000.00 USD | 1,600,000.00 USD | 9,330.00 USD | 5,210.00 USD | 11,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,640,000.00 USD | 1,640,000.00 USD | 7,810.00 USD | 4,630.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 1,620,000.00 USD | 1,620,000.00 USD | 7,810.00 USD | 4,630.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 1,660,000.00 USD | 1,660,000.00 USD | 6,260.00 USD | 5,300.00 USD | 12,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 1,650,000.00 USD | 1,650,000.00 USD | 6,260.00 USD | 5,300.00 USD | 12,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 1,680,000.00 USD | 1,680,000.00 USD | 9,310.00 USD | 3,460.00 USD | 150.13 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 1,660,000.00 USD | 1,660,000.00 USD | 9,310.00 USD | 3,460.00 USD | 150.13 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 1,690,000.00 USD | 1,690,000.00 USD | 8,540.00 USD | 1,900.00 USD | 711.93 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 1,670,000.00 USD | 1,670,000.00 USD | 8,540.00 USD | 1,900.00 USD | 711.93 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 1,700,000.00 USD | 1,700,000.00 USD | 5,340.00 USD | 2,850.00 USD | 4,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 1,680,000.00 USD | 1,680,000.00 USD | 5,340.00 USD | 2,850.00 USD | 4,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 1,710,000.00 USD | 1,710,000.00 USD | 3,920.00 USD | 1,710.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 1,690,000.00 USD | 1,690,000.00 USD | 3,920.00 USD | 1,710.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 1,720,000.00 USD | 1,720,000.00 USD | 2,440.00 USD | 1,730.00 USD | 3,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 1,700,000.00 USD | 1,700,000.00 USD | 2,440.00 USD | 1,730.00 USD | 3,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 1,740,000.00 USD | 1,740,000.00 USD | 8,100.00 USD | 4,200.00 USD | 7,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 1,720,000.00 USD | 1,720,000.00 USD | 8,100.00 USD | 4,200.00 USD | 7,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 1,750,000.00 USD | 1,750,000.00 USD | 7,330.00 USD | 2,600.00 USD | 4,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 1,730,000.00 USD | 1,730,000.00 USD | 7,330.00 USD | 2,600.00 USD | 4,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 1,760,000.00 USD | 1,760,000.00 USD | 2,340.00 USD | 2,180.00 USD | 966.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 1,740,000.00 USD | 1,740,000.00 USD | 2,340.00 USD | 2,180.00 USD | 966.50 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 1,760,000.00 USD | 1,760,000.00 USD | 687.18 USD | 1,950.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 1,740,000.00 USD | 1,740,000.00 USD | 687.18 USD | 1,950.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 1,780,000.00 USD | 1,780,000.00 USD | 3,790.00 USD | 5,770.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 1,760,000.00 USD | 1,760,000.00 USD | 3,790.00 USD | 5,770.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 1,790,000.00 USD | 1,790,000.00 USD | 5,520.00 USD | 905.53 USD | 4,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 1,770,000.00 USD | 1,770,000.00 USD | 5,520.00 USD | 905.53 USD | 4,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 1,790,000.00 USD | 1,790,000.00 USD | 1,910.00 USD | 2,290.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 1,780,000.00 USD | 1,780,000.00 USD | 1,910.00 USD | 2,290.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 3,240.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 3,240.00 USD | 2,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 1,810,000.00 USD | 1,810,000.00 USD | 2,770.00 USD | 2,620.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 1,790,000.00 USD | 1,790,000.00 USD | 2,770.00 USD | 2,620.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.10` | 169.18 USD | 66,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.11` | 1,810,000.00 USD | 1,810,000.00 USD | 2,020.00 USD | 50.69 USD | 111.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 1,790,000.00 USD | 1,790,000.00 USD | 2,020.00 USD | 50.69 USD | 111.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.11` | 1,810,000.00 USD | 1,810,000.00 USD | 3,090.00 USD | 1,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 1,800,000.00 USD | 1,800,000.00 USD | 3,090.00 USD | 1,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.11` | 1,820,000.00 USD | 1,820,000.00 USD | 888.25 USD | 2,410.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 1,800,000.00 USD | 1,800,000.00 USD | 888.25 USD | 2,410.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.11` | 1,850,000.00 USD | 1,850,000.00 USD | 18,680.00 USD | 1,360.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 1,830,000.00 USD | 1,830,000.00 USD | 18,680.00 USD | 1,360.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.11` | 1,860,000.00 USD | 1,860,000.00 USD | 6,380.00 USD | 50.07 USD | 9,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 1,850,000.00 USD | 1,850,000.00 USD | 6,380.00 USD | 50.07 USD | 9,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.12` | 1,870,000.00 USD | 1,870,000.00 USD | 2,490.00 USD | 276.66 USD | 191.23 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 1,850,000.00 USD | 1,850,000.00 USD | 2,490.00 USD | 276.66 USD | 191.23 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.12` | 1,880,000.00 USD | 1,880,000.00 USD | 2,240.00 USD | 2,500.00 USD | 4,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 1,860,000.00 USD | 1,860,000.00 USD | 2,240.00 USD | 2,500.00 USD | 4,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.12` | 1,890,000.00 USD | 1,890,000.00 USD | 8,620.00 USD | 49.03 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 1,870,000.00 USD | 1,870,000.00 USD | 8,620.00 USD | 49.03 USD | 4,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.12` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 364.90 USD | 583.97 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 364.90 USD | 583.97 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.12` | 1,890,000.00 USD | 1,890,000.00 USD | 199.10 USD | 12.50 USD | 192.17 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 1,870,000.00 USD | 1,870,000.00 USD | 199.10 USD | 12.50 USD | 192.17 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.13` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 1,020.00 USD | 3,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 1,020.00 USD | 3,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.13` | 1,900,000.00 USD | 1,900,000.00 USD | 2,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 1,880,000.00 USD | 1,880,000.00 USD | 2,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.13` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 432.73 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 432.73 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.18` | 228.30 USD | 66,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 22,120.00 USD | 88,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,740.00 USD | 100,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 388.62 USD | 100,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.42` | 4,310.00 USD | 105,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 512,400.00 USD | 617,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 232.56 USD | 617,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.59 USD | 617,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 9,580.00 USD | 627,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 239.20 USD | 627,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 1,080.00 USD | 628,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 299.70 USD | 629,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 87,830.00 USD | 716,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 208.32 USD | 717,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 182.31 USD | 717,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 2,950.00 USD | 720,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.99` | 1,600.00 USD | 721,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2350` | 495,430.00 USD | 0.00 USD | 424.34 USD | `-76.64%` | `1,805.70` |
| `Live` | `Long` | `0.2550` | 495,000.00 USD | 0.00 USD | 127.50 USD | `-74.65%` | `500.00` |
| `Live` | `Long` | `0.3250` | 494,880.00 USD | 0.00 USD | 717.93 USD | `-67.69%` | `2,209.00` |
| `Live` | `Long` | `0.3350` | 494,160.00 USD | 0.00 USD | 106.97 USD | `-66.69%` | `319.30` |
| `Live` | `Long` | `0.3450` | 494,050.00 USD | 0.00 USD | 1,970.00 USD | `-65.70%` | `5,698.80` |
| `Live` | `Long` | `0.3650` | 492,090.00 USD | 0.00 USD | 722.66 USD | `-63.71%` | `1,979.90` |
| `Live` | `Long` | `0.3750` | 491,360.00 USD | 0.00 USD | 9,150.00 USD | `-62.72%` | `24,390.20` |
| `Live` | `Long` | `0.3950` | 482,220.00 USD | 0.00 USD | 156.62 USD | `-60.73%` | `396.50` |
| `Live` | `Long` | `0.4150` | 482,060.00 USD | 0.00 USD | 2,770.00 USD | `-58.74%` | `6,675.20` |
| `Live` | `Long` | `0.4550` | 479,290.00 USD | 0.00 USD | 182.32 USD | `-54.76%` | `400.70` |
| `Live` | `Long` | `0.4650` | 479,110.00 USD | 0.00 USD | 2,560.00 USD | `-53.77%` | `5,500.00` |
| `Live` | `Long` | `0.5150` | 476,550.00 USD | 0.00 USD | 4,770.00 USD | `-48.80%` | `9,252.60` |
| `Live` | `Long` | `0.5450` | 471,790.00 USD | 0.00 USD | 106.55 USD | `-45.81%` | `195.50` |
| `Live` | `Long` | `0.5550` | 471,680.00 USD | 0.00 USD | 173.88 USD | `-44.82%` | `313.30` |
| `Live` | `Long` | `0.5650` | 471,510.00 USD | 0.00 USD | 572.80 USD | `-43.83%` | `1,013.80` |
| `Live` | `Long` | `0.5750` | 470,930.00 USD | 0.00 USD | 140.64 USD | `-42.83%` | `244.60` |
| `Live` | `Long` | `0.5850` | 470,790.00 USD | 0.00 USD | 136.48 USD | `-41.84%` | `233.30` |
| `Live` | `Long` | `0.5950` | 470,660.00 USD | 0.00 USD | 3,390.00 USD | `-40.84%` | `5,695.60` |
| `Live` | `Long` | `0.6050` | 467,270.00 USD | 0.00 USD | 3,280.00 USD | `-39.85%` | `5,420.30` |
| `Live` | `Long` | `0.6150` | 463,990.00 USD | 0.00 USD | 254.00 USD | `-38.85%` | `413.00` |
| `Live` | `Long` | `0.6250` | 463,730.00 USD | 0.00 USD | 526.19 USD | `-37.86%` | `841.90` |
| `Live` | `Long` | `0.6350` | 463,210.00 USD | 0.00 USD | 867.92 USD | `-36.87%` | `1,366.80` |
| `Live` | `Long` | `0.6450` | 462,340.00 USD | 0.00 USD | 24,800.00 USD | `-35.87%` | `38,448.00` |
| `Live` | `Long` | `0.6550` | 437,540.00 USD | 0.00 USD | 148.42 USD | `-34.88%` | `226.60` |
| `Live` | `Long` | `0.6750` | 437,390.00 USD | 0.00 USD | 421.54 USD | `-32.89%` | `624.50` |
| `Live` | `Long` | `0.6850` | 436,970.00 USD | 0.00 USD | 3,460.00 USD | `-31.90%` | `5,049.60` |
| `Live` | `Long` | `0.6950` | 433,510.00 USD | 0.00 USD | 321.92 USD | `-30.90%` | `463.20` |
| `Live` | `Long` | `0.7050` | 433,190.00 USD | 0.00 USD | 16,630.00 USD | `-29.91%` | `23,594.30` |
| `Live` | `Long` | `0.7150` | 416,560.00 USD | 0.00 USD | 1,310.00 USD | `-28.91%` | `1,834.00` |
| `Live` | `Long` | `0.7250` | 415,240.00 USD | 0.00 USD | 3,720.00 USD | `-27.92%` | `5,135.70` |
| `Live` | `Long` | `0.7350` | 411,520.00 USD | 0.00 USD | 3,740.00 USD | `-26.92%` | `5,083.90` |
| `Live` | `Long` | `0.7550` | 407,780.00 USD | 0.00 USD | 2,720.00 USD | `-24.94%` | `3,601.10` |
| `Live` | `Long` | `0.7650` | 405,060.00 USD | 0.00 USD | 839.82 USD | `-23.94%` | `1,097.80` |
| `Live` | `Long` | `0.7750` | 404,230.00 USD | 0.00 USD | 1,590.00 USD | `-22.95%` | `2,046.10` |
| `Live` | `Long` | `0.7850` | 402,640.00 USD | 0.00 USD | 20,560.00 USD | `-21.95%` | `26,187.90` |
| `Live` | `Long` | `0.7950` | 382,080.00 USD | 0.00 USD | 16,510.00 USD | `-20.96%` | `20,761.30` |
| `Live` | `Long` | `0.8050` | 365,580.00 USD | 0.00 USD | 1,510.00 USD | `-19.96%` | `1,869.80` |
| `Live` | `Long` | `0.8150` | 364,070.00 USD | 0.00 USD | 648.98 USD | `-18.97%` | `796.30` |
| `Live` | `Long` | `0.8250` | 363,420.00 USD | 0.00 USD | 3,840.00 USD | `-17.98%` | `4,654.00` |
| `Live` | `Long` | `0.8350` | 359,580.00 USD | 0.00 USD | 9,330.00 USD | `-16.98%` | `11,174.20` |
| `Live` | `Long` | `0.8450` | 350,250.00 USD | 0.00 USD | 2,500.00 USD | `-15.99%` | `2,956.50` |
| `Live` | `Long` | `0.8550` | 347,750.00 USD | 0.00 USD | 618.51 USD | `-14.99%` | `723.40` |
| `Live` | `Long` | `0.8650` | 347,140.00 USD | 0.00 USD | 1,080.00 USD | `-14.00%` | `1,243.60` |
| `Live` | `Long` | `0.8750` | 346,060.00 USD | 0.00 USD | 1,110.00 USD | `-13.00%` | `1,274.00` |
| `Live` | `Long` | `0.8850` | 344,950.00 USD | 0.00 USD | 9,090.00 USD | `-12.01%` | `10,267.00` |
| `Live` | `Long` | `0.8950` | 335,860.00 USD | 0.00 USD | 4,330.00 USD | `-11.02%` | `4,840.60` |
| `Live` | `Long` | `0.9050` | 331,530.00 USD | 0.00 USD | 946.63 USD | `-10.02%` | `1,046.00` |
| `Live` | `Long` | `0.9150` | 330,580.00 USD | 0.00 USD | 45,280.00 USD | `-9.03%` | `49,487.90` |
| `Live` | `Long` | `0.9250` | 285,300.00 USD | 0.00 USD | 53,190.00 USD | `-8.03%` | `57,498.90` |
| `Live` | `Long` | `0.9350` | 232,110.00 USD | 0.00 USD | 7,100.00 USD | `-7.04%` | `7,597.30` |
| `Live` | `Long` | `0.9450` | 225,010.00 USD | 0.00 USD | 216,520.00 USD | `-6.04%` | `229,123.70` |
| `Live` | `Long` | `0.9550` | 8,490.00 USD | 0.00 USD | 8,260.00 USD | `-5.05%` | `8,651.40` |
| `Live` | `Long` | `0.9750` | 224.54 USD | 0.00 USD | 224.54 USD | `-3.06%` | `230.30` |
| `Live` | `Short` | `1.05` | 156.98 USD | 156.98 USD | 0.00 USD | `+4.89%` | `148.80` |
| `Live` | `Short` | `1.06` | 66,190.00 USD | 66,030.00 USD | 0.00 USD | `+5.89%` | `62,000.00` |
| `Live` | `Short` | `1.10` | 66,360.00 USD | 169.18 USD | 0.00 USD | `+9.86%` | `153.10` |
| `Live` | `Short` | `1.18` | 66,580.00 USD | 228.30 USD | 0.00 USD | `+16.82%` | `194.30` |
| `Live` | `Short` | `1.19` | 88,700.00 USD | 22,120.00 USD | 0.00 USD | `+17.82%` | `18,664.00` |
| `Live` | `Short` | `1.32` | 100,440.00 USD | 11,740.00 USD | 0.00 USD | `+31.74%` | `8,862.90` |
| `Live` | `Short` | `1.33` | 100,830.00 USD | 388.62 USD | 0.00 USD | `+32.73%` | `291.10` |
| `Live` | `Short` | `1.42` | 105,150.00 USD | 4,310.00 USD | 0.00 USD | `+40.68%` | `3,049.30` |
| `Live` | `Short` | `1.49` | 617,550.00 USD | 512,400.00 USD | 0.00 USD | `+47.64%` | `345,051.20` |
| `Live` | `Short` | `1.52` | 617,780.00 USD | 232.56 USD | 0.00 USD | `+51.62%` | `152.50` |
| `Live` | `Short` | `1.54` | 617,960.00 USD | 176.59 USD | 0.00 USD | `+53.61%` | `114.30` |
| `Live` | `Short` | `1.55` | 627,540.00 USD | 9,580.00 USD | 0.00 USD | `+54.60%` | `6,161.90` |
| `Live` | `Short` | `1.64` | 627,780.00 USD | 239.20 USD | 0.00 USD | `+62.56%` | `146.30` |
| `Live` | `Short` | `1.65` | 628,860.00 USD | 1,080.00 USD | 0.00 USD | `+63.55%` | `655.90` |
| `Live` | `Short` | `1.67` | 629,160.00 USD | 299.70 USD | 0.00 USD | `+65.54%` | `180.00` |
| `Live` | `Short` | `1.76` | 716,980.00 USD | 87,830.00 USD | 0.00 USD | `+75.48%` | `49,759.80` |
| `Live` | `Short` | `1.85` | 717,190.00 USD | 208.32 USD | 0.00 USD | `+84.43%` | `112.30` |
| `Live` | `Short` | `1.91` | 717,370.00 USD | 182.31 USD | 0.00 USD | `+89.40%` | `95.70` |
| `Live` | `Short` | `1.97` | 720,320.00 USD | 2,950.00 USD | 0.00 USD | `+95.37%` | `1,500.00` |
| `Live` | `Short` | `1.99` | 721,930.00 USD | 1,600.00 USD | 0.00 USD | `+97.36%` | `808.40` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4050` | 420,980.00 USD | 0.00 USD | 121.50 USD | `-59.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 420,860.00 USD | 0.00 USD | 151.50 USD | `-49.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 420,710.00 USD | 0.00 USD | 786.92 USD | `-29.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7150` | 419,920.00 USD | 0.00 USD | 819.60 USD | `-28.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7250` | 419,100.00 USD | 0.00 USD | 978.90 USD | `-27.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7350` | 418,120.00 USD | 0.00 USD | 161.19 USD | `-26.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7450` | 417,960.00 USD | 0.00 USD | 288.91 USD | `-25.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7850` | 417,670.00 USD | 0.00 USD | 14,650.00 USD | `-21.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 403,020.00 USD | 0.00 USD | 274,320.00 USD | `-20.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8150` | 128,700.00 USD | 0.00 USD | 407.50 USD | `-18.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8350` | 128,300.00 USD | 0.00 USD | 771.46 USD | `-16.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8450` | 127,520.00 USD | 0.00 USD | 3,450.00 USD | `-15.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 124,070.00 USD | 0.00 USD | 10,000.00 USD | `-14.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8650` | 114,070.00 USD | 0.00 USD | 1,820.00 USD | `-14.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 112,260.00 USD | 0.00 USD | 781.10 USD | `-12.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 111,480.00 USD | 0.00 USD | 294.63 USD | `-11.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 111,180.00 USD | 0.00 USD | 362.00 USD | `-10.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 110,820.00 USD | 0.00 USD | 1,140.00 USD | `-9.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 109,680.00 USD | 0.00 USD | 2,360.00 USD | `-8.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 107,320.00 USD | 0.00 USD | 9,670.00 USD | `-7.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 97,650.00 USD | 0.00 USD | 2,140.00 USD | `-6.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 95,510.00 USD | 0.00 USD | 547.98 USD | `-5.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 94,970.00 USD | 0.00 USD | 2,860.00 USD | `-4.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 92,110.00 USD | 0.00 USD | 1,270.00 USD | `-3.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 90,830.00 USD | 0.00 USD | 8,390.00 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 82,440.00 USD | 0.00 USD | 40,710.00 USD | `-1.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 41,730.00 USD | 0.00 USD | 41,730.00 USD | `-0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,180.00 USD | 1,180.00 USD | 0.00 USD | `+0.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,380.00 USD | 201.82 USD | 0.00 USD | `+1.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 2,250.00 USD | 866.19 USD | 0.00 USD | `+2.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 5,480.00 USD | 3,230.00 USD | 0.00 USD | `+3.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 5,590.00 USD | 108.35 USD | 0.00 USD | `+4.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 71,620.00 USD | 66,030.00 USD | 0.00 USD | `+5.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 72,160.00 USD | 547.18 USD | 0.00 USD | `+6.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 72,320.00 USD | 157.76 USD | 0.00 USD | `+7.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 85,960.00 USD | 13,640.00 USD | 0.00 USD | `+8.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 86,940.00 USD | 980.36 USD | 0.00 USD | `+9.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 87,110.00 USD | 170.71 USD | 0.00 USD | `+10.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 89,150.00 USD | 2,040.00 USD | 0.00 USD | `+11.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 91,810.00 USD | 2,660.00 USD | 0.00 USD | `+12.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 91,960.00 USD | 150.57 USD | 0.00 USD | `+13.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 92,120.00 USD | 151.88 USD | 0.00 USD | `+14.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 94,160.00 USD | 2,050.00 USD | 0.00 USD | `+15.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 94,270.00 USD | 110.33 USD | 0.00 USD | `+16.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 94,510.00 USD | 237.00 USD | 0.00 USD | `+17.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 138,700.00 USD | 44,190.00 USD | 0.00 USD | `+19.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 140,710.00 USD | 2,000.00 USD | 0.00 USD | `+22.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 140,950.00 USD | 244.93 USD | 0.00 USD | `+26.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 148,330.00 USD | 7,380.00 USD | 0.00 USD | `+28.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 155,270.00 USD | 6,940.00 USD | 0.00 USD | `+29.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 614,480.00 USD | 459,210.00 USD | 0.00 USD | `+30.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 630,210.00 USD | 15,730.00 USD | 0.00 USD | `+33.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 631,460.00 USD | 1,250.00 USD | 0.00 USD | `+34.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 633,540.00 USD | 2,070.00 USD | 0.00 USD | `+38.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 633,840.00 USD | 301.09 USD | 0.00 USD | `+39.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 634,440.00 USD | 599.82 USD | 0.00 USD | `+40.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 668,620.00 USD | 34,180.00 USD | 0.00 USD | `+42.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 669,500.00 USD | 882.50 USD | 0.00 USD | `+48.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 670,100.00 USD | 591.46 USD | 0.00 USD | `+49.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 673,150.00 USD | 3,050.00 USD | 0.00 USD | `+50.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 673,450.00 USD | 297.94 USD | 0.00 USD | `+54.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 681,980.00 USD | 8,540.00 USD | 0.00 USD | `+64.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 682,130.00 USD | 143.69 USD | 0.00 USD | `+65.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 682,310.00 USD | 177.50 USD | 0.00 USD | `+76.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 682,740.00 USD | 432.48 USD | 0.00 USD | `+79.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 687,830.00 USD | 5,090.00 USD | 0.00 USD | `+89.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.92` | 690,320.00 USD | 2,490.00 USD | 0.00 USD | `+90.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 696,160.00 USD | 5,840.00 USD | 0.00 USD | `+97.36%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.9000` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 5,710.00 USD | 2,320.00 USD | 2,370.00 USD |
| `7D` | `0.9000` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 5,710.00 USD | 2,320.00 USD | 2,370.00 USD |
| `1D` | `0.9020` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 1,850.00 USD | 3,210.00 USD | 1,590.00 USD |
| `7D` | `0.9020` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 1,850.00 USD | 3,210.00 USD | 2,320.00 USD |
| `1D` | `0.9040` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 3,130.00 USD | 2,520.00 USD | 3,880.00 USD |
| `7D` | `0.9040` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 3,130.00 USD | 2,520.00 USD | 3,880.00 USD |
| `1D` | `0.9060` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 9,620.00 USD | 1,660.00 USD | 111.00 USD |
| `7D` | `0.9060` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 9,620.00 USD | 1,660.00 USD | 111.00 USD |
| `1D` | `0.9080` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 5,800.00 USD | 3,150.00 USD | 3,500.00 USD |
| `7D` | `0.9080` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 5,800.00 USD | 3,150.00 USD | 3,500.00 USD |
| `1D` | `0.9100` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 21,910.00 USD | 2,110.00 USD | 7,630.00 USD |
| `7D` | `0.9100` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 21,910.00 USD | 2,110.00 USD | 7,630.00 USD |
| `1D` | `0.9120` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 8,100.00 USD | 228.71 USD | 9,030.00 USD |
| `7D` | `0.9120` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 8,100.00 USD | 228.71 USD | 9,030.00 USD |
| `1D` | `0.9140` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 5,920.00 USD | 2,890.00 USD | 4,570.00 USD |
| `7D` | `0.9140` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 5,920.00 USD | 2,890.00 USD | 4,570.00 USD |
| `1D` | `0.9160` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 14,110.00 USD | 57.95 USD | 4,100.00 USD |
| `7D` | `0.9160` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 14,110.00 USD | 57.95 USD | 4,100.00 USD |
| `1D` | `0.9180` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 49.41 USD | 452.74 USD | 583.97 USD |
| `7D` | `0.9180` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 49.41 USD | 452.74 USD | 583.97 USD |
| `1D` | `0.9200` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 2,950.00 USD | 112.72 USD | 192.17 USD |
| `7D` | `0.9200` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 2,950.00 USD | 112.72 USD | 192.17 USD |
| `1D` | `0.9220` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 7,970.00 USD | 1,070.00 USD | 3,060.00 USD |
| `7D` | `0.9220` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 7,970.00 USD | 1,070.00 USD | 3,060.00 USD |
| `1D` | `0.9240` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 14,860.00 USD | 5,390.00 USD | 36.99 USD |
| `7D` | `0.9240` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 14,860.00 USD | 5,390.00 USD | 36.99 USD |
| `1D` | `0.9260` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 11,000.00 USD | 9,670.00 USD | 21,980.00 USD |
| `7D` | `0.9260` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 11,000.00 USD | 9,670.00 USD | 21,980.00 USD |
| `1D` | `0.9280` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 24,160.00 USD | 4,120.00 USD | 6,930.00 USD |
| `7D` | `0.9280` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 24,160.00 USD | 4,120.00 USD | 6,930.00 USD |
| `1D` | `0.9300` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 15,130.00 USD | 1,370.00 USD | 16,060.00 USD |
| `7D` | `0.9300` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 15,130.00 USD | 1,370.00 USD | 16,060.00 USD |
| `1D` | `0.9320` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 24,390.00 USD | 12,710.00 USD | 12,400.00 USD |
| `7D` | `0.9320` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 24,390.00 USD | 12,710.00 USD | 12,400.00 USD |
| `1D` | `0.9340` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 21,330.00 USD | 11,340.00 USD | 10,720.00 USD |
| `7D` | `0.9340` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 21,330.00 USD | 11,340.00 USD | 10,720.00 USD |
| `1D` | `0.9360` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 49,310.00 USD | 11,940.00 USD | 19,500.00 USD |
| `7D` | `0.9360` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 49,310.00 USD | 11,940.00 USD | 19,500.00 USD |
| `1D` | `0.9380` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 25,820.00 USD | 14,670.00 USD | 10,400.00 USD |
| `7D` | `0.9380` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 25,820.00 USD | 14,670.00 USD | 10,400.00 USD |
| `1D` | `0.9400` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 23,270.00 USD | 9,580.00 USD | 13,670.00 USD |
| `7D` | `0.9400` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 23,270.00 USD | 9,580.00 USD | 13,670.00 USD |
| `1D` | `0.9420` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 26,160.00 USD | 11,140.00 USD | 3,070.00 USD |
| `7D` | `0.9420` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 26,160.00 USD | 11,140.00 USD | 3,070.00 USD |
| `1D` | `0.9440` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 30,630.00 USD | 16,080.00 USD | 6,190.00 USD |
| `7D` | `0.9440` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 30,630.00 USD | 16,080.00 USD | 6,190.00 USD |
| `1D` | `0.9460` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 29,420.00 USD | 29,010.00 USD | 59,500.00 USD |
| `7D` | `0.9460` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 29,420.00 USD | 29,010.00 USD | 59,500.00 USD |
| `1D` | `0.9480` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 75,700.00 USD | 20,490.00 USD | 27,640.00 USD |
| `7D` | `0.9480` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 75,700.00 USD | 20,490.00 USD | 27,640.00 USD |
| `1D` | `0.9500` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 56,450.00 USD | 8,300.00 USD | 44,510.00 USD |
| `7D` | `0.9500` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 56,450.00 USD | 8,300.00 USD | 44,510.00 USD |
| `1D` | `0.9520` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 60,750.00 USD | 33,850.00 USD | 29,060.00 USD |
| `7D` | `0.9520` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 60,750.00 USD | 33,850.00 USD | 29,060.00 USD |
| `1D` | `0.9540` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 49,960.00 USD | 29,630.00 USD | 31,000.00 USD |
| `7D` | `0.9540` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 49,960.00 USD | 29,630.00 USD | 31,000.00 USD |
| `1D` | `0.9560` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 133,850.00 USD | 53,740.00 USD | 77,270.00 USD |
| `7D` | `0.9560` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 133,850.00 USD | 53,740.00 USD | 77,270.00 USD |
| `1D` | `0.9580` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 52,680.00 USD | 30,810.00 USD | 39,600.00 USD |
| `7D` | `0.9580` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 52,680.00 USD | 30,810.00 USD | 39,600.00 USD |
| `1D` | `0.9600` | 938,020.00 USD | 0.00 USD | 938,020.00 USD | 75,810.00 USD | 28,100.00 USD | 9,820.00 USD |
| `7D` | `0.9600` | 943,490.00 USD | 0.00 USD | 943,490.00 USD | 75,810.00 USD | 28,100.00 USD | 9,820.00 USD |
| `1D` | `0.9620` | 824,290.00 USD | 0.00 USD | 824,290.00 USD | 40,260.00 USD | 18,850.00 USD | 11,340.00 USD |
| `7D` | `0.9620` | 829,770.00 USD | 0.00 USD | 829,770.00 USD | 40,260.00 USD | 18,850.00 USD | 13,160.00 USD |
| `1D` | `0.9640` | 753,850.00 USD | 0.00 USD | 753,850.00 USD | 11,580.00 USD | 9,650.00 USD | 25,280.00 USD |
| `7D` | `0.9640` | 757,500.00 USD | 0.00 USD | 757,500.00 USD | 11,580.00 USD | 9,650.00 USD | 25,280.00 USD |
| `1D` | `0.9660` | 707,350.00 USD | 0.00 USD | 707,350.00 USD | 31,400.00 USD | 21,230.00 USD | 35,150.00 USD |
| `7D` | `0.9660` | 710,990.00 USD | 0.00 USD | 710,990.00 USD | 31,400.00 USD | 21,230.00 USD | 35,150.00 USD |
| `1D` | `0.9680` | 619,570.00 USD | 0.00 USD | 619,570.00 USD | 39,890.00 USD | 17,500.00 USD | 24,270.00 USD |
| `7D` | `0.9680` | 623,220.00 USD | 0.00 USD | 623,220.00 USD | 39,890.00 USD | 17,500.00 USD | 24,270.00 USD |
| `1D` | `0.9700` | 537,910.00 USD | 0.00 USD | 537,910.00 USD | 46,160.00 USD | 9,430.00 USD | 19,710.00 USD |
| `7D` | `0.9700` | 541,560.00 USD | 0.00 USD | 541,560.00 USD | 46,160.00 USD | 9,430.00 USD | 19,710.00 USD |
| `1D` | `0.9720` | 462,620.00 USD | 0.00 USD | 462,620.00 USD | 33,600.00 USD | 9,090.00 USD | 22,030.00 USD |
| `7D` | `0.9720` | 466,270.00 USD | 0.00 USD | 466,270.00 USD | 33,600.00 USD | 9,090.00 USD | 22,030.00 USD |
| `1D` | `0.9740` | 397,900.00 USD | 0.00 USD | 397,900.00 USD | 3,950.00 USD | 8,490.00 USD | 4,300.00 USD |
| `7D` | `0.9740` | 401,550.00 USD | 0.00 USD | 401,550.00 USD | 3,950.00 USD | 8,490.00 USD | 4,300.00 USD |
| `1D` | `0.9760` | 381,150.00 USD | 0.00 USD | 381,150.00 USD | 19,600.00 USD | 13,960.00 USD | 8,350.00 USD |
| `7D` | `0.9760` | 384,800.00 USD | 0.00 USD | 384,800.00 USD | 19,600.00 USD | 13,960.00 USD | 8,350.00 USD |
| `1D` | `0.9780` | 339,240.00 USD | 0.00 USD | 339,240.00 USD | 23,150.00 USD | 881.37 USD | 8,520.00 USD |
| `7D` | `0.9780` | 342,890.00 USD | 0.00 USD | 342,890.00 USD | 23,150.00 USD | 881.37 USD | 8,520.00 USD |
| `1D` | `0.9800` | 306,690.00 USD | 0.00 USD | 306,690.00 USD | 9,130.00 USD | 3,600.00 USD | 0.00 USD |
| `7D` | `0.9800` | 310,340.00 USD | 0.00 USD | 310,340.00 USD | 9,130.00 USD | 3,600.00 USD | 0.00 USD |
| `1D` | `0.9820` | 293,960.00 USD | 0.00 USD | 293,960.00 USD | 0.00 USD | 12,160.00 USD | 3,220.00 USD |
| `7D` | `0.9820` | 297,610.00 USD | 0.00 USD | 297,610.00 USD | 0.00 USD | 12,160.00 USD | 6,870.00 USD |
| `1D` | `0.9840` | 278,580.00 USD | 0.00 USD | 278,580.00 USD | 4,700.00 USD | 2,170.00 USD | 11,940.00 USD |
| `7D` | `0.9840` | 278,580.00 USD | 0.00 USD | 278,580.00 USD | 4,700.00 USD | 2,170.00 USD | 11,940.00 USD |
| `1D` | `0.9860` | 259,760.00 USD | 0.00 USD | 259,760.00 USD | 8,720.00 USD | 8,090.00 USD | 1,160.00 USD |
| `7D` | `0.9860` | 259,760.00 USD | 0.00 USD | 259,760.00 USD | 8,720.00 USD | 8,090.00 USD | 1,160.00 USD |
| `1D` | `0.9880` | 241,790.00 USD | 0.00 USD | 241,790.00 USD | 5,570.00 USD | 1,950.00 USD | 6,020.00 USD |
| `7D` | `0.9880` | 241,790.00 USD | 0.00 USD | 241,790.00 USD | 5,570.00 USD | 1,950.00 USD | 6,020.00 USD |
| `1D` | `0.9900` | 228,240.00 USD | 0.00 USD | 228,240.00 USD | 50,430.00 USD | 8,270.00 USD | 13,390.00 USD |
| `7D` | `0.9900` | 228,240.00 USD | 0.00 USD | 228,240.00 USD | 50,430.00 USD | 8,270.00 USD | 13,390.00 USD |
| `1D` | `0.9920` | 156,150.00 USD | 0.00 USD | 156,150.00 USD | 9,070.00 USD | 0.00 USD | 20,160.00 USD |
| `7D` | `0.9920` | 156,150.00 USD | 0.00 USD | 156,150.00 USD | 9,070.00 USD | 0.00 USD | 20,160.00 USD |
| `1D` | `0.9940` | 126,920.00 USD | 0.00 USD | 126,920.00 USD | 6,920.00 USD | 14,630.00 USD | 5,910.00 USD |
| `7D` | `0.9940` | 126,920.00 USD | 0.00 USD | 126,920.00 USD | 6,920.00 USD | 14,630.00 USD | 5,910.00 USD |
| `1D` | `0.9960` | 99,470.00 USD | 0.00 USD | 99,470.00 USD | 0.00 USD | 2,630.00 USD | 0.00 USD |
| `7D` | `0.9960` | 99,470.00 USD | 0.00 USD | 99,470.00 USD | 0.00 USD | 2,630.00 USD | 0.00 USD |
| `1D` | `0.9980` | 96,840.00 USD | 0.00 USD | 96,840.00 USD | 26,250.00 USD | 0.00 USD | 1,610.00 USD |
| `7D` | `0.9980` | 96,840.00 USD | 0.00 USD | 96,840.00 USD | 26,250.00 USD | 0.00 USD | 1,610.00 USD |
| `1D` | `1.00` | 68,980.00 USD | 0.00 USD | 68,980.00 USD | 31,780.00 USD | 23,940.00 USD | 13,250.00 USD |
| `7D` | `1.00` | 68,980.00 USD | 0.00 USD | 68,980.00 USD | 31,780.00 USD | 23,940.00 USD | 13,250.00 USD |
| `7D` | `1.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.00` | 20,100.00 USD | 20,100.00 USD | 0.00 USD | 17,270.00 USD | 0.00 USD | 2,830.00 USD |
| `1D` | `1.00` | 40,200.00 USD | 40,200.00 USD | 0.00 USD | 17,270.00 USD | 0.00 USD | 2,830.00 USD |
| `7D` | `1.00` | 17,460.00 USD | 17,460.00 USD | 0.00 USD | 17,270.00 USD | 0.00 USD | 192.37 USD |
| `1D` | `1.01` | 58,770.00 USD | 58,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,570.00 USD |
| `7D` | `1.01` | 36,030.00 USD | 36,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,570.00 USD |
| `1D` | `1.01` | 60,010.00 USD | 60,010.00 USD | 0.00 USD | 1,190.00 USD | 49.40 USD | 0.00 USD |
| `7D` | `1.01` | 37,260.00 USD | 37,260.00 USD | 0.00 USD | 1,190.00 USD | 49.40 USD | 0.00 USD |
| `1D` | `1.01` | 87,930.00 USD | 87,930.00 USD | 0.00 USD | 0.00 USD | 27,920.00 USD | 0.00 USD |
| `7D` | `1.01` | 65,190.00 USD | 65,190.00 USD | 0.00 USD | 0.00 USD | 27,920.00 USD | 0.00 USD |
| `1D` | `1.01` | 102,670.00 USD | 102,670.00 USD | 0.00 USD | 0.00 USD | 21.50 USD | 14,720.00 USD |
| `7D` | `1.01` | 79,930.00 USD | 79,930.00 USD | 0.00 USD | 0.00 USD | 21.50 USD | 14,720.00 USD |
| `1D` | `1.02` | 142,800.00 USD | 142,800.00 USD | 0.00 USD | 20,120.00 USD | 21.80 USD | 19,990.00 USD |
| `7D` | `1.02` | 120,060.00 USD | 120,060.00 USD | 0.00 USD | 20,120.00 USD | 21.80 USD | 19,990.00 USD |
| `1D` | `1.02` | 174,020.00 USD | 174,020.00 USD | 0.00 USD | 1,130.00 USD | 7,410.00 USD | 22,680.00 USD |
| `7D` | `1.02` | 151,280.00 USD | 151,280.00 USD | 0.00 USD | 1,130.00 USD | 7,410.00 USD | 22,680.00 USD |
| `1D` | `1.02` | 218,870.00 USD | 218,870.00 USD | 0.00 USD | 40,090.00 USD | 1,690.00 USD | 3,070.00 USD |
| `7D` | `1.02` | 196,130.00 USD | 196,130.00 USD | 0.00 USD | 40,090.00 USD | 1,690.00 USD | 3,070.00 USD |
| `1D` | `1.02` | 262,160.00 USD | 262,160.00 USD | 0.00 USD | 25,850.00 USD | 991.70 USD | 16,450.00 USD |
| `7D` | `1.02` | 243,060.00 USD | 243,060.00 USD | 0.00 USD | 25,850.00 USD | 991.70 USD | 20,090.00 USD |
| `1D` | `1.02` | 362,780.00 USD | 362,780.00 USD | 0.00 USD | 32,250.00 USD | 24,720.00 USD | 43,640.00 USD |
| `7D` | `1.02` | 343,680.00 USD | 343,680.00 USD | 0.00 USD | 32,250.00 USD | 24,720.00 USD | 43,640.00 USD |
| `1D` | `1.03` | 420,870.00 USD | 420,870.00 USD | 0.00 USD | 32,060.00 USD | 14,590.00 USD | 11,440.00 USD |
| `7D` | `1.03` | 401,770.00 USD | 401,770.00 USD | 0.00 USD | 32,060.00 USD | 14,590.00 USD | 11,440.00 USD |
| `1D` | `1.03` | 479,230.00 USD | 479,230.00 USD | 0.00 USD | 31,210.00 USD | 8,670.00 USD | 18,480.00 USD |
| `7D` | `1.03` | 460,140.00 USD | 460,140.00 USD | 0.00 USD | 31,210.00 USD | 8,670.00 USD | 18,480.00 USD |
| `1D` | `1.03` | 642,620.00 USD | 642,620.00 USD | 0.00 USD | 100,250.00 USD | 23,640.00 USD | 39,490.00 USD |
| `7D` | `1.03` | 623,530.00 USD | 623,530.00 USD | 0.00 USD | 100,250.00 USD | 23,640.00 USD | 39,490.00 USD |
| `1D` | `1.03` | 768,650.00 USD | 768,650.00 USD | 0.00 USD | 83,270.00 USD | 6,480.00 USD | 36,280.00 USD |
| `7D` | `1.03` | 749,550.00 USD | 749,550.00 USD | 0.00 USD | 83,270.00 USD | 6,480.00 USD | 36,280.00 USD |
| `1D` | `1.03` | 829,080.00 USD | 829,080.00 USD | 0.00 USD | 35,180.00 USD | 7,080.00 USD | 18,170.00 USD |
| `7D` | `1.03` | 809,990.00 USD | 809,990.00 USD | 0.00 USD | 35,180.00 USD | 7,080.00 USD | 18,170.00 USD |
| `1D` | `1.04` | 946,810.00 USD | 946,810.00 USD | 0.00 USD | 29,120.00 USD | 29,520.00 USD | 59,090.00 USD |
| `7D` | `1.04` | 927,720.00 USD | 927,720.00 USD | 0.00 USD | 29,120.00 USD | 29,520.00 USD | 59,090.00 USD |
| `1D` | `1.04` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 69,240.00 USD | 5,430.00 USD | 38,930.00 USD |
| `7D` | `1.04` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 69,240.00 USD | 5,430.00 USD | 38,930.00 USD |
| `1D` | `1.04` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 7,710.00 USD | 8,040.00 USD | 14,960.00 USD |
| `7D` | `1.04` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 7,710.00 USD | 8,040.00 USD | 14,960.00 USD |
| `1D` | `1.04` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 1,190.00 USD | 9,870.00 USD | 6,550.00 USD |
| `7D` | `1.04` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190.00 USD | 9,870.00 USD | 8,370.00 USD |
| `1D` | `1.04` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 7,360.00 USD | 14,490.00 USD | 32,130.00 USD |
| `7D` | `1.04` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 7,360.00 USD | 14,490.00 USD | 32,130.00 USD |
| `1D` | `1.05` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 21,760.00 USD | 4,260.00 USD | 321.14 USD |
| `7D` | `1.05` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 21,760.00 USD | 4,260.00 USD | 321.14 USD |
| `1D` | `1.05` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 15,080.00 USD | 3,170.00 USD | 4,880.00 USD |
| `7D` | `1.05` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 15,080.00 USD | 3,170.00 USD | 4,880.00 USD |
| `1D` | `1.05` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 43,530.00 USD | 11,120.00 USD | 20,030.00 USD |
| `7D` | `1.05` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 43,530.00 USD | 11,120.00 USD | 20,030.00 USD |
| `1D` | `1.05` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 32,960.00 USD | 6,990.00 USD | 44,510.00 USD |
| `7D` | `1.05` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 32,960.00 USD | 6,990.00 USD | 44,510.00 USD |
| `1D` | `1.05` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 9,000.00 USD | 311.68 USD | 12,280.00 USD |
| `7D` | `1.05` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 9,000.00 USD | 311.68 USD | 12,280.00 USD |
| `1D` | `1.06` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 7,850.00 USD | 5,710.00 USD | 28,370.00 USD |
| `7D` | `1.06` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 7,850.00 USD | 5,710.00 USD | 28,370.00 USD |
| `1D` | `1.06` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 29,750.00 USD | 3,000.00 USD | 20,480.00 USD |
| `7D` | `1.06` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 29,750.00 USD | 3,000.00 USD | 20,480.00 USD |
| `1D` | `1.06` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 3,730.00 USD | 3,810.00 USD | 10,470.00 USD |
| `7D` | `1.06` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 3,730.00 USD | 3,810.00 USD | 10,470.00 USD |
| `1D` | `1.06` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 2,110.00 USD | 7,870.00 USD | 2,400.00 USD |
| `7D` | `1.06` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 2,110.00 USD | 7,870.00 USD | 2,400.00 USD |
| `1D` | `1.06` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 5,350.00 USD | 2,520.00 USD | 7,970.00 USD |
| `7D` | `1.06` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 5,350.00 USD | 2,520.00 USD | 7,970.00 USD |
| `1D` | `1.07` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 12,610.00 USD | 3,010.00 USD | 5,690.00 USD |
| `7D` | `1.07` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 12,610.00 USD | 3,010.00 USD | 5,690.00 USD |
| `1D` | `1.07` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 10,690.00 USD | 4,390.00 USD | 3,180.00 USD |
| `7D` | `1.07` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 10,690.00 USD | 4,390.00 USD | 3,180.00 USD |
| `1D` | `1.07` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 9,230.00 USD | 5,010.00 USD | 6,410.00 USD |
| `7D` | `1.07` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 9,230.00 USD | 5,010.00 USD | 6,410.00 USD |
| `1D` | `1.07` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 9,330.00 USD | 5,210.00 USD | 11,220.00 USD |
| `7D` | `1.07` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 9,330.00 USD | 5,210.00 USD | 11,220.00 USD |
| `1D` | `1.07` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 7,810.00 USD | 4,630.00 USD | 6,930.00 USD |
| `7D` | `1.07` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 7,810.00 USD | 4,630.00 USD | 6,930.00 USD |
| `1D` | `1.08` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 6,260.00 USD | 5,300.00 USD | 12,650.00 USD |
| `7D` | `1.08` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 6,260.00 USD | 5,300.00 USD | 12,650.00 USD |
| `1D` | `1.08` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 9,310.00 USD | 3,460.00 USD | 150.13 USD |
| `7D` | `1.08` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 9,310.00 USD | 3,460.00 USD | 150.13 USD |
| `1D` | `1.08` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 8,540.00 USD | 1,900.00 USD | 711.93 USD |
| `7D` | `1.08` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 8,540.00 USD | 1,900.00 USD | 711.93 USD |
| `1D` | `1.08` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 5,340.00 USD | 2,850.00 USD | 4,530.00 USD |
| `7D` | `1.08` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 5,340.00 USD | 2,850.00 USD | 4,530.00 USD |
| `1D` | `1.08` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 3,920.00 USD | 1,710.00 USD | 2,780.00 USD |
| `7D` | `1.08` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 3,920.00 USD | 1,710.00 USD | 2,780.00 USD |
| `1D` | `1.09` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 2,440.00 USD | 1,730.00 USD | 3,470.00 USD |
| `7D` | `1.09` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 2,440.00 USD | 1,730.00 USD | 3,470.00 USD |
| `1D` | `1.09` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 8,100.00 USD | 4,200.00 USD | 7,350.00 USD |
| `7D` | `1.09` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 8,100.00 USD | 4,200.00 USD | 7,350.00 USD |
| `1D` | `1.09` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 7,330.00 USD | 2,600.00 USD | 4,110.00 USD |
| `7D` | `1.09` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 7,330.00 USD | 2,600.00 USD | 4,110.00 USD |
| `1D` | `1.09` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 2,340.00 USD | 2,180.00 USD | 966.50 USD |
| `7D` | `1.09` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 2,340.00 USD | 2,180.00 USD | 966.50 USD |
| `1D` | `1.09` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 687.18 USD | 1,950.00 USD | 1,890.00 USD |
| `7D` | `1.09` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 687.18 USD | 1,950.00 USD | 1,890.00 USD |
| `1D` | `1.10` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 3,790.00 USD | 5,770.00 USD | 5,780.00 USD |
| `7D` | `1.10` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 3,790.00 USD | 5,770.00 USD | 5,780.00 USD |
| `1D` | `1.10` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 5,520.00 USD | 905.53 USD | 4,040.00 USD |
| `7D` | `1.10` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 5,520.00 USD | 905.53 USD | 4,040.00 USD |
| `1D` | `1.10` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 1,910.00 USD | 2,290.00 USD | 2,300.00 USD |
| `7D` | `1.10` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 1,910.00 USD | 2,290.00 USD | 2,300.00 USD |
| `1D` | `1.10` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 3,240.00 USD | 1,590.00 USD |
| `7D` | `1.10` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 3,240.00 USD | 2,320.00 USD |
| `1D` | `1.10` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 2,770.00 USD | 2,620.00 USD | 3,880.00 USD |
| `7D` | `1.10` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 2,770.00 USD | 2,620.00 USD | 3,880.00 USD |
| `1D` | `1.11` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 2,020.00 USD | 50.69 USD | 111.00 USD |
| `7D` | `1.11` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 2,020.00 USD | 50.69 USD | 111.00 USD |
| `1D` | `1.11` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 3,090.00 USD | 1,650.00 USD | 0.00 USD |
| `7D` | `1.11` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 3,090.00 USD | 1,650.00 USD | 0.00 USD |
| `1D` | `1.11` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 888.25 USD | 2,410.00 USD | 3,500.00 USD |
| `7D` | `1.11` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 888.25 USD | 2,410.00 USD | 3,500.00 USD |
| `1D` | `1.11` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 18,680.00 USD | 1,360.00 USD | 7,630.00 USD |
| `7D` | `1.11` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 18,680.00 USD | 1,360.00 USD | 7,630.00 USD |
| `1D` | `1.11` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 6,380.00 USD | 50.07 USD | 9,030.00 USD |
| `7D` | `1.11` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 6,380.00 USD | 50.07 USD | 9,030.00 USD |
| `1D` | `1.12` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 2,490.00 USD | 276.66 USD | 191.23 USD |
| `7D` | `1.12` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 2,490.00 USD | 276.66 USD | 191.23 USD |
| `1D` | `1.12` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 2,240.00 USD | 2,500.00 USD | 4,370.00 USD |
| `7D` | `1.12` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 2,240.00 USD | 2,500.00 USD | 4,370.00 USD |
| `1D` | `1.12` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 8,620.00 USD | 49.03 USD | 4,100.00 USD |
| `7D` | `1.12` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 8,620.00 USD | 49.03 USD | 4,100.00 USD |
| `1D` | `1.12` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 364.90 USD | 583.97 USD |
| `7D` | `1.12` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 364.90 USD | 583.97 USD |
| `1D` | `1.12` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 199.10 USD | 12.50 USD | 192.17 USD |
| `7D` | `1.12` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 199.10 USD | 12.50 USD | 192.17 USD |
| `1D` | `1.13` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 1,020.00 USD | 3,060.00 USD |
| `7D` | `1.13` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 1,020.00 USD | 3,060.00 USD |
| `1D` | `1.13` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.13` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.13` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 432.73 USD | 0.00 USD |
| `7D` | `1.13` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 432.73 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `BALANCED` | 9,850.00 USD | 0.00 USD | 9,850.00 USD | -9,850.00 USD | `1` | `2026-10-29 17:00:00 UTC - 2026-10-29 17:05:00 UTC` |
| `15m` | `BALANCED` | 9,850.00 USD | 0.00 USD | 9,850.00 USD | -9,850.00 USD | `1` | `2026-10-29 17:00:00 UTC - 2026-10-29 17:15:00 UTC` |
| `1h` | `BALANCED` | 9,850.00 USD | 0.00 USD | 9,850.00 USD | -9,850.00 USD | `1` | `2026-10-29 17:00:00 UTC - 2026-10-29 18:00:00 UTC` |
| `4h` | `BALANCED` | 9,850.00 USD | 0.00 USD | 9,850.00 USD | -9,850.00 USD | `1` | `2026-10-29 16:00:00 UTC - 2026-10-29 20:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `212.00M` | Total OI Tokens: `211,491,380.7 DOT`
  * 1h OI Change: `-1.85%` | 4h OI Change: `+0.49%` | 24h OI Change: `-1.85%`
  * Exchange Breakdown: Binance=`37.18M` | Bybit=`24.89M` | OKX=`10.40M` | Hyperliquid=`5.76M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.46K` | Last 24h: `7.91K` | Last 3d: `-10.37K` | Last 7d: `-19.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0071%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `39.62%` | `60.38%` | `0.66` | 4,180,000.00 USD |
| `15M` | `Binance` | `38.73%` | `61.27%` | `0.63` | 1,620,000.00 USD |
| `15M` | `OKX` | `25.32%` | `74.68%` | `0.34` | 580,800.00 USD |
| `15M` | `Bybit` | `41.33%` | `58.67%` | `0.70` | 419,530.00 USD |
| `15M` | `KuCoin` | `15.06%` | `84.94%` | `0.18` | 68,160.00 USD |
| `15M` | `Gate` | `47.86%` | `52.14%` | `0.92` | 118,340.00 USD |
| `15M` | `Bitget` | `47%` | `53%` | `0.89` | 114,480.00 USD |
| `15M` | `BingX` | `37.78%` | `62.22%` | `0.61` | 147,730.00 USD |
| `15M` | `MEXC` | `46.73%` | `53.27%` | `0.88` | 428,090.00 USD |
| `15M` | `Bitunix` | `46.71%` | `53.29%` | `0.88` | 100,100.00 USD |
| `15M` | `Hyperliquid` | `24.59%` | `75.41%` | `0.33` | 142,600.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.21%` | `49.79%` | `1.01` | 40,040.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `62.01%` | `37.99%` | `1.63` | 348,870.00 USD |
| `15M` | `HTX` | `4.4%` | `95.6%` | `0.05` | 8,010.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `31.91%` | `68.09%` | `0.47` | 32,610.00 USD |
| `15M` | `Aster` | `5.08%` | `94.92%` | `0.05` | 3,610.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `30.32%` | `69.68%` | `0.44` | 2,070.00 USD |
| `15M` | `Whale Positions` | `38.73%` | `61.27%` | `0.63` | 1,620,000.00 USD |
| `15M` | `Global Accounts` | `39.62%` | `60.38%` | `0.66` | 4,180,000.00 USD |
| `1H` | `DOT` | `44.87%` | `55.13%` | `0.81` | 40,840,000.00 USD |
| `1H` | `Binance` | `44.6%` | `55.4%` | `0.81` | 15,340,000.00 USD |
| `1H` | `OKX` | `38.28%` | `61.72%` | `0.62` | 6,080,000.00 USD |
| `1H` | `Bybit` | `44.87%` | `55.13%` | `0.81` | 4,370,000.00 USD |
| `1H` | `KuCoin` | `45.3%` | `54.7%` | `0.83` | 495,760.00 USD |
| `1H` | `Gate` | `50.64%` | `49.36%` | `1.03` | 1,300,000.00 USD |
| `1H` | `Bitget` | `47.88%` | `52.12%` | `0.92` | 2,300,000.00 USD |
| `1H` | `BingX` | `41.46%` | `58.54%` | `0.71` | 1,060,000.00 USD |
| `1H` | `MEXC` | `52.15%` | `47.85%` | `1.09` | 4,890,000.00 USD |
| `1H` | `Bitunix` | `51.45%` | `48.55%` | `1.06` | 1,480,000.00 USD |
| `1H` | `Hyperliquid` | `29.06%` | `70.94%` | `0.41` | 980,190.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `45.98%` | `54.02%` | `0.85` | 214,940.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `64.97%` | `35.03%` | `1.85` | 1,340,000.00 USD |
| `1H` | `HTX` | `40.07%` | `59.93%` | `0.67` | 90,920.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `17.77%` | `82.23%` | `0.22` | 800,000.00 USD |
| `1H` | `Aster` | `27.91%` | `72.09%` | `0.39` | 57,310.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `15.27%` | `84.73%` | `0.18` | 32,200.00 USD |
| `1H` | `Whale Positions` | `44.6%` | `55.4%` | `0.81` | 15,340,000.00 USD |
| `1H` | `Global Accounts` | `44.87%` | `55.13%` | `0.81` | 40,840,000.00 USD |
| `4H` | `DOT` | `48.56%` | `51.44%` | `0.94` | 491,690,000.00 USD |
| `4H` | `Binance` | `50.53%` | `49.47%` | `1.02` | 209,640,000.00 USD |
| `4H` | `OKX` | `46.93%` | `53.07%` | `0.88` | 83,010,000.00 USD |
| `4H` | `Bybit` | `48.07%` | `51.93%` | `0.93` | 59,620,000.00 USD |
| `4H` | `KuCoin` | `49.18%` | `50.82%` | `0.97` | 3,870,000.00 USD |
| `4H` | `Gate` | `47.14%` | `52.86%` | `0.89` | 8,260,000.00 USD |
| `4H` | `Bitget` | `48.52%` | `51.48%` | `0.94` | 19,900,000.00 USD |
| `4H` | `BingX` | `49.44%` | `50.56%` | `0.98` | 16,190,000.00 USD |
| `4H` | `MEXC` | `45.09%` | `54.91%` | `0.82` | 26,590,000.00 USD |
| `4H` | `Bitunix` | `49.51%` | `50.49%` | `0.98` | 12,120,000.00 USD |
| `4H` | `Hyperliquid` | `48.04%` | `51.96%` | `0.92` | 28,930,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.44%` | `48.56%` | `1.06` | 2,520,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 27,160.00 USD |
| `4H` | `WhiteBIT` | `52.85%` | `47.15%` | `1.12` | 10,950,000.00 USD |
| `4H` | `HTX` | `47.34%` | `52.66%` | `0.90` | 608,260.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `32.52%` | `67.48%` | `0.48` | 4,930,000.00 USD |
| `4H` | `Aster` | `48.28%` | `51.72%` | `0.93` | 877,120.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `39.11%` | `60.89%` | `0.64` | 3,660,000.00 USD |
| `4H` | `Whale Positions` | `50.53%` | `49.47%` | `1.02` | 209,640,000.00 USD |
| `4H` | `Global Accounts` | `48.56%` | `51.44%` | `0.94` | 491,690,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.01` | `1.01` | `1.01` | `1.01` | `1.00` | 941,624.33 USD | 291,132.42 USD | 650,491.91 USD | -359,359.48 USD | `-38.16%` | `7B / 37S` |
| `0:00 UTC` | `1.01` | `1.01` | `1.01` | `1.01` | `1.00` | 775,452.64 USD | 376,237.58 USD | 399,215.06 USD | -22,977.48 USD | `-2.96%` | `22B / 25S` |
| `5:00 UTC` | `1.01` | `1.01` | `1.01` | `1.01` | `1.00` | 469,322.85 USD | 154,724.12 USD | 314,598.73 USD | -159,874.62 USD | `-34.06%` | `11B / 34S` |
| `0:00 UTC` | `1.01` | `1.01` | `1.01` | `1.01` | `1.00` | 1,036,474.58 USD | 416,595.02 USD | 619,879.56 USD | -203,284.54 USD | `-19.61%` | `14B / 24S` |
| `5:00 UTC` | `1.02` | `1.02` | `1.02` | `1.02` | `1.01` | 1,420,574.95 USD | 1,000,262.40 USD | 420,312.55 USD | 579,949.86 USD | `+40.83%` | `13B / 20S` |
| `0:00 UTC` | `1.02` | `1.02` | `1.02` | `1.02` | `1.01` | 1,273,423.64 USD | 481,734.41 USD | 791,689.23 USD | -309,954.82 USD | `-24.34%` | `9B / 29S` |
| `5:00 UTC` | `1.01` | `1.01` | `1.01` | `1.01` | `1.01` | 657,161.08 USD | 244,063.77 USD | 413,097.31 USD | -169,033.55 USD | `-25.72%` | `3B / 15S` |
| `0:00 UTC` | `1.01` | `1.01` | `1.01` | `1.01` | `1.00` | 605,145.48 USD | 242,805.14 USD | 362,340.33 USD | -119,535.19 USD | `-19.75%` | `3B / 20S` |
| `5:00 UTC` | `1.01` | `1.01` | `1.01` | `1.01` | `1.00` | 367,151.31 USD | 115,663.71 USD | 251,487.60 USD | -135,823.89 USD | `-36.99%` | `2B / 13S` |
| `0:00 UTC` | `1.00` | `1.00` | `1.00` | `1.01` | `1.00` | 473,848.50 USD | 176,428.76 USD | 297,419.74 USD | -120,990.98 USD | `-25.53%` | `5B / 26S` |

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
| `5m` | 2,300.00 USD | -17,090.00 USD | **`DISTRIBUTION`** |
| `15m` | -11,330.00 USD | -241,340.00 USD | **`DISTRIBUTION`** |
| `30m` | 23,890.00 USD | -319,120.00 USD | **`DISTRIBUTION`** |
| `1h` | -52,880.00 USD | -1,090,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -49,790.00 USD | -1,080,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -970.87 USD | -1,480,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -46,980.00 USD | -1,510,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -157,620.00 USD | -1,490,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -42,560.00 USD | -1,290,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -184,020.00 USD | -3,330,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,410,000.00 USD | -17,550,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,540,000.00 USD | -72,330,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+2.30K` | 15m=`-11.33K` | 1h=`-52.88K` | 24h=`-184.02K`
* Futures Capital Netflows: 5m=`-17.09K` | 15m=`-241.34K` | 1h=`-1.09M` | 24h=`-3.33M`
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
  * `2026-10-29 22:05:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [bea.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.9512` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.9124` (Risk Distance: `0.0400` pts)
  * +2.5R Take Profit: `1.05`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9952` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.03` (Risk Distance: `0.0400` pts)
  * +2.5R Take Profit: `0.8952`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.01`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
