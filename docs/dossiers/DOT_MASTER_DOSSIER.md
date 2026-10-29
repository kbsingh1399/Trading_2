# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 23:07:13 IST` (`2026-10-29 17:37:13 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9900` | **Live Ask Quote**: `1.01` | **Mid Price**: `1.00`
- **Spread Points**: `21.00` | **Spread BPS**: `209.90 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9777` | VWAP Z-Score: `+0.84` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0072` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `51.60` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.02` | Lower -3.00σ Band: `0.9333`
  * Upper +2.51σ Band: `1.01` | Lower -2.51σ Band: `0.9406`
  * Upper +2.01σ Band: `1.01` | Lower -2.01σ Band: `0.9480`
  * Upper +2.00σ Band: `1.01` | Lower -2.00σ Band: `0.9481`
  * Upper +1.28σ Band: `0.9966` | Lower -1.28σ Band: `0.9587`
  * Upper +1.00σ Band: `0.9924` | Lower -1.00σ Band: `0.9629`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9935` | EMA-20=`0.9905` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9844` (Slope: `+0.0000`) | EMA-100=`0.9840`
  * Institutional Anchors: EMA-144=`0.9849` | EMA-200=`0.9853` (Slope: `+0.1450`) | EMA-233=`0.9851`
- **Range Boundaries**: 24H High=`1.03` | 24H Low=`0.9510` | Weekly High=`1.03` | Weekly Low=`0.9510`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9952` (Distance: `+0.48%`)
  * Point of Control (POC) = `0.9630` (Distance: `+3.84%`)
  * Value Area Low (VAL) = `0.9530` (Distance: `+4.93%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.00` | POC=`0.9890` | VAL=`0.9812`
  * Prior Day Extremes: PDH=`1.03` | PDL=`0.9690` | PDC=`1.01`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.01` | Weekly POC=`0.9929` | Weekly VAL=`0.9779`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.02` | Low=`0.9510`
  * London Session (08:00-16:00 UTC): High=`0.9850` | Low=`0.9600`
  * New York Session (13:00-21:00 UTC): High=`1.01` | Low=`0.9680`
  * Initial Balance (First Hour): IB High=`0.9800` | IB Low=`0.9670`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9965` - `1.00`
  * Optimal Trade Entry (OTE 0.705): `1.00`
  * Structural Invalidation Anchor (0.786): `1.01`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.00` | `1.00` | `0.9990` | `0.9994` | `178,562` | 178,731.05 USD | -66,703.44 USD | `-37.32%` | -1,614,277.98 USD | `-0.46` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.9993` | `1.00` | `0.9973` | `0.9997` | `679,343` | 679,390.62 USD | 212,345.47 USD | `+31.26%` | -1,401,932.51 USD | `+1.75` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.9997` | `1.00` | `0.9993` | `1.00` | `93,631` | 93,847.33 USD | 13,947.38 USD | `+14.86%` | -1,387,985.14 USD | `+0.15` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `1.01` | `1.01` | `1.00` | `1.01` | `365,323` | 367,151.31 USD | -135,823.89 USD | `-36.99%` | -1,488,952.87 USD | `-0.48` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `1.01` | `1.01` | `0.9990` | `0.9994` | `613,584` | 615,154.97 USD | -169,038.50 USD | `-27.48%` | -1,657,991.37 USD | `-0.62` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9993` | `1.00` | `0.9973` | `1.00` | `773,508` | 773,773.43 USD | 225,942.75 USD | `+29.20%` | -1,432,048.62 USD | `+1.34` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.00` | `1.02` | `1.00` | `1.02` | `3,661,852` | 3,701,825.02 USD | 193,813.22 USD | `+5.24%` | -902,386.24 USD | `+0.71` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.02` | `1.02` | `1.00` | `1.01` | `2,867,696` | 2,902,881.51 USD | -734,347.44 USD | `-25.30%` | -1,636,733.68 USD | `-2.29` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.01` | `1.01` | `0.9973` | `1.00` | `1,387,092` | 1,388,928.39 USD | 56,904.25 USD | `+4.10%` | -1,579,829.44 USD | `+0.21` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | -137,778.42 USD | `+0.23` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -315,355.23 USD | `-0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9973` | `1.00` | `4,254,766` | 4,291,788.46 USD | -677,464.64 USD | `-15.79%` | -992,819.87 USD | `-1.07` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.01` | `1.01` | `0.9612` | `0.9700` | `15,616,467` | 15,304,422.31 USD | 595,816.59 USD | `+3.89%` | -236,044.76 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.9699` | `0.9906` | `0.9674` | `0.9732` | `8,505,701` | 8,320,368.15 USD | 13,201.93 USD | `+0.16%` | -222,842.83 USD | `+0.15` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | -137,778.42 USD | `+0.23` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -315,355.23 USD | `-0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9973` | `1.00` | `4,254,766` | 4,291,788.46 USD | -677,464.64 USD | `-15.79%` | -992,819.87 USD | `-1.07` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `ANNOUNCEMENT` | `INFO` | `0.9992` | 5,498.96 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale SELL: 5.50K USD at 0.9992 USD [API] | `2026-10-27 22:26:23` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.04` (Vol: 74,700.00 USD, Dist: `+3.53%`) | Long MP=`0.9649` (Vol: 113,700.00 USD, Dist: `--3.68%`)
  * 48H Horizon: Short MP=`1.04` (Vol: 74,700.00 USD, Dist: `+3.53%`) | Long MP=`0.9649` (Vol: 113,700.00 USD, Dist: `--3.68%`)
  * 3D Horizon: Short MP=`1.04` (Vol: 74,700.00 USD, Dist: `+3.53%`) | Long MP=`0.9511` (Vol: 130,500.00 USD, Dist: `--5.07%`)
  * 7D Horizon: Short MP=`1.07` (Vol: 211,000.00 USD, Dist: `+6.64%`) | Long MP=`0.9606` (Vol: 177,500.00 USD, Dist: `--4.11%`)
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
| `7D` | `Long Liquidation` | `0.8710` | 5,310,000.00 USD | 5,310,000.00 USD | 21,960.00 USD | 3,060.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 2,120.00 USD | 295.31 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8750` | 1,110.00 USD | 346,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8770` | 5,270,000.00 USD | 5,270,000.00 USD | 20,650.00 USD | 6,200.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 5,240,000.00 USD | 5,240,000.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 5,230,000.00 USD | 5,230,000.00 USD | 228.30 USD | 114.50 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 5,230,000.00 USD | 5,230,000.00 USD | 8,430.00 USD | 5,730.00 USD | 360.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8850` | 5,220,000.00 USD | 5,220,000.00 USD | 8,630.00 USD | 3,180.00 USD | 698.60 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8850` | 9,090.00 USD | 344,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8870` | 5,200,000.00 USD | 5,200,000.00 USD | 11,700.00 USD | 5,060.00 USD | 6,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8890` | 5,180,000.00 USD | 5,180,000.00 USD | 13,840.00 USD | 5,370.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8910` | 5,150,000.00 USD | 5,150,000.00 USD | 30,330.00 USD | 7,940.00 USD | 24,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8930` | 5,090,000.00 USD | 5,090,000.00 USD | 24,780.00 USD | 5,820.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8950` | 5,050,000.00 USD | 5,050,000.00 USD | 7,380.00 USD | 10,730.00 USD | 27,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8950` | 4,330.00 USD | 335,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8970` | 2,580,000.00 USD | 2,580,000.00 USD | 8,810.00 USD | 6,780.00 USD | 11,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8970` | 5,000,000.00 USD | 5,000,000.00 USD | 43,430.00 USD | 5,400.00 USD | 31,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8990` | 2,550,000.00 USD | 2,550,000.00 USD | 5,550.00 USD | 757.19 USD | 3,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8990` | 4,920,000.00 USD | 4,920,000.00 USD | 52,250.00 USD | 14,640.00 USD | 20,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9010` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 1,530.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9010` | 4,830,000.00 USD | 4,830,000.00 USD | 20,170.00 USD | 11,570.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9030` | 2,540,000.00 USD | 2,540,000.00 USD | 4,100.00 USD | 3,760.00 USD | 2,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9030` | 4,800,000.00 USD | 4,800,000.00 USD | 12,700.00 USD | 8,710.00 USD | 21,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9050` | 2,530,000.00 USD | 2,530,000.00 USD | 8,300.00 USD | 3,640.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9050` | 4,750,000.00 USD | 4,750,000.00 USD | 35,230.00 USD | 25,240.00 USD | 27,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9050` | 946.63 USD | 331,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9070` | 2,520,000.00 USD | 2,520,000.00 USD | 3,810.00 USD | 488.01 USD | 803.91 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9070` | 4,670,000.00 USD | 4,670,000.00 USD | 37,740.00 USD | 7,720.00 USD | 15,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9090` | 2,510,000.00 USD | 2,510,000.00 USD | 18,830.00 USD | 4,070.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9090` | 4,610,000.00 USD | 4,610,000.00 USD | 13,790.00 USD | 8,050.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9110` | 2,480,000.00 USD | 2,480,000.00 USD | 13,080.00 USD | 791.28 USD | 10,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9110` | 4,580,000.00 USD | 4,580,000.00 USD | 8,490.00 USD | 7,760.00 USD | 17,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9130` | 2,460,000.00 USD | 2,460,000.00 USD | 4,770.00 USD | 441.47 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9130` | 4,540,000.00 USD | 4,540,000.00 USD | 26,980.00 USD | 2,110.00 USD | 680.66 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9150` | 2,450,000.00 USD | 2,450,000.00 USD | 14,130.00 USD | 2,620.00 USD | 8,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9150` | 4,510,000.00 USD | 4,510,000.00 USD | 41,000.00 USD | 10,660.00 USD | 34,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9150` | 45,280.00 USD | 330,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9170` | 2,420,000.00 USD | 2,420,000.00 USD | 3,440.00 USD | 435.13 USD | 452.67 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9170` | 4,430,000.00 USD | 4,430,000.00 USD | 22,610.00 USD | 14,810.00 USD | 18,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9190` | 2,420,000.00 USD | 2,420,000.00 USD | 2,770.00 USD | 138.43 USD | 186.24 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9190` | 4,370,000.00 USD | 4,370,000.00 USD | 33,980.00 USD | 4,860.00 USD | 19,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9210` | 2,420,000.00 USD | 2,420,000.00 USD | 1,580.00 USD | 48.64 USD | 2,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9210` | 4,310,000.00 USD | 4,310,000.00 USD | 22,070.00 USD | 7,060.00 USD | 15,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9230` | 2,410,000.00 USD | 2,410,000.00 USD | 10,750.00 USD | 2,010.00 USD | 907.53 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9230` | 4,270,000.00 USD | 4,270,000.00 USD | 35,230.00 USD | 11,030.00 USD | 37,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9250` | 2,400,000.00 USD | 2,400,000.00 USD | 19,910.00 USD | 8,910.00 USD | 14,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9250` | 4,190,000.00 USD | 4,190,000.00 USD | 56,800.00 USD | 9,090.00 USD | 30,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9250` | 53,190.00 USD | 285,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9270` | 2,350,000.00 USD | 2,350,000.00 USD | 15,110.00 USD | 5,250.00 USD | 10,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9270` | 4,090,000.00 USD | 4,090,000.00 USD | 70,300.00 USD | 9,380.00 USD | 21,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9290` | 2,320,000.00 USD | 2,320,000.00 USD | 25,710.00 USD | 4,260.00 USD | 6,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9290` | 3,990,000.00 USD | 3,990,000.00 USD | 39,160.00 USD | 8,340.00 USD | 31,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9310` | 2,290,000.00 USD | 2,290,000.00 USD | 10,550.00 USD | 12,130.00 USD | 21,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9310` | 3,910,000.00 USD | 3,910,000.00 USD | 26,530.00 USD | 10,070.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9330` | 2,240,000.00 USD | 2,240,000.00 USD | 21,780.00 USD | 9,020.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9330` | 3,870,000.00 USD | 3,870,000.00 USD | 33,550.00 USD | 9,510.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9350` | 2,200,000.00 USD | 2,200,000.00 USD | 36,280.00 USD | 10,930.00 USD | 13,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9350` | 3,800,000.00 USD | 3,800,000.00 USD | 82,010.00 USD | 29,330.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9350` | 7,100.00 USD | 232,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9370` | 2,140,000.00 USD | 2,140,000.00 USD | 38,570.00 USD | 12,840.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9370` | 3,670,000.00 USD | 3,670,000.00 USD | 29,580.00 USD | 14,910.00 USD | 7,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9390` | 2,070,000.00 USD | 2,070,000.00 USD | 17,730.00 USD | 14,390.00 USD | 13,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9390` | 3,620,000.00 USD | 3,620,000.00 USD | 18,750.00 USD | 14,310.00 USD | 12,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9410` | 2,020,000.00 USD | 2,020,000.00 USD | 35,920.00 USD | 11,380.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9410` | 3,570,000.00 USD | 3,570,000.00 USD | 45,790.00 USD | 14,500.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9430` | 1,970,000.00 USD | 1,970,000.00 USD | 21,480.00 USD | 8,450.00 USD | 3,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9430` | 3,510,000.00 USD | 3,510,000.00 USD | 54,680.00 USD | 11,100.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9450` | 1,940,000.00 USD | 1,940,000.00 USD | 36,850.00 USD | 20,360.00 USD | 40,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9450` | 3,430,000.00 USD | 3,430,000.00 USD | 77,230.00 USD | 33,720.00 USD | 41,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9450` | 216,520.00 USD | 225,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9470` | 1,840,000.00 USD | 1,840,000.00 USD | 45,400.00 USD | 24,750.00 USD | 40,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9470` | 3,280,000.00 USD | 3,280,000.00 USD | 108,740.00 USD | 24,210.00 USD | 50,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9490` | 1,730,000.00 USD | 1,730,000.00 USD | 74,440.00 USD | 15,840.00 USD | 21,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9490` | 3,090,000.00 USD | 3,090,000.00 USD | 129,370.00 USD | 34,600.00 USD | 113,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9510` | 1,620,000.00 USD | 1,620,000.00 USD | 34,350.00 USD | 30,330.00 USD | 48,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9510` | 2,820,000.00 USD | 2,820,000.00 USD | 198,910.00 USD | 37,160.00 USD | 81,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9530` | 1,510,000.00 USD | 1,510,000.00 USD | 50,320.00 USD | 22,180.00 USD | 21,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9530` | 2,500,000.00 USD | 2,500,000.00 USD | 79,700.00 USD | 27,910.00 USD | 123,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9550` | 1,410,000.00 USD | 1,410,000.00 USD | 78,960.00 USD | 38,020.00 USD | 38,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9550` | 2,270,000.00 USD | 2,270,000.00 USD | 172,820.00 USD | 90,890.00 USD | 56,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9550` | 8,260.00 USD | 8,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9570` | 1,260,000.00 USD | 1,260,000.00 USD | 130,660.00 USD | 45,370.00 USD | 68,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9570` | 1,950,000.00 USD | 1,950,000.00 USD | 129,820.00 USD | 45,870.00 USD | 128,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9590` | 1,010,000.00 USD | 1,010,000.00 USD | 49,590.00 USD | 20,710.00 USD | 37,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9590` | 1,640,000.00 USD | 1,640,000.00 USD | 176,280.00 USD | 56,660.00 USD | 72,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9610` | 906,220.00 USD | 906,220.00 USD | 53,350.00 USD | 25,860.00 USD | 11,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9610` | 1,340,000.00 USD | 1,340,000.00 USD | 183,020.00 USD | 77,580.00 USD | 32,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9630` | 815,010.00 USD | 815,010.00 USD | 27,750.00 USD | 19,430.00 USD | 17,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9630` | 1,040,000.00 USD | 1,040,000.00 USD | 95,260.00 USD | 281.90 USD | 12,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9650` | 750,310.00 USD | 750,310.00 USD | 25,320.00 USD | 13,180.00 USD | 31,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9650` | 937,000.00 USD | 937,000.00 USD | 65,160.00 USD | 1,120.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9670` | 680,530.00 USD | 680,530.00 USD | 28,790.00 USD | 14,700.00 USD | 21,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9670` | 861,590.00 USD | 861,590.00 USD | 31,440.00 USD | 12,830.00 USD | 45,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9690` | 615,450.00 USD | 615,450.00 USD | 37,870.00 USD | 22,640.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9690` | 771,400.00 USD | 771,400.00 USD | 3,040.00 USD | 11,390.00 USD | 37,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9710` | 523,720.00 USD | 523,720.00 USD | 54,360.00 USD | 12,350.00 USD | 21,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9710` | 719,050.00 USD | 719,050.00 USD | 64,680.00 USD | 619.85 USD | 9,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9730` | 435,890.00 USD | 435,890.00 USD | 13,580.00 USD | 691.66 USD | 13,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9730` | 643,960.00 USD | 643,960.00 USD | 0.00 USD | 0.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9750` | 407,950.00 USD | 407,950.00 USD | 10,430.00 USD | 18,900.00 USD | 5,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9750` | 636,450.00 USD | 636,450.00 USD | 0.00 USD | 16,590.00 USD | 3,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9750` | 224.54 USD | 224.54 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9770` | 372,960.00 USD | 372,960.00 USD | 35,620.00 USD | 2,870.00 USD | 10,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9770` | 616,580.00 USD | 616,580.00 USD | 15,320.00 USD | 5,480.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9790` | 323,590.00 USD | 323,590.00 USD | 9,790.00 USD | 4,480.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9790` | 564,370.00 USD | 564,370.00 USD | 0.00 USD | 15,440.00 USD | 89,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9810` | 301,140.00 USD | 301,140.00 USD | 4,500.00 USD | 376.40 USD | 8,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9810` | 459,400.00 USD | 459,400.00 USD | 7,900.00 USD | 0.00 USD | 132,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9830` | 287,330.00 USD | 287,330.00 USD | 9,030.00 USD | 13,960.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9830` | 318,550.00 USD | 318,550.00 USD | 2,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9850` | 258,330.00 USD | 258,330.00 USD | 575.70 USD | 0.00 USD | 10,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9850` | 316,360.00 USD | 316,360.00 USD | 0.00 USD | 16,440.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9870` | 247,020.00 USD | 247,020.00 USD | 13,720.00 USD | 10,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9870` | 277,100.00 USD | 277,100.00 USD | 40,020.00 USD | 16,870.00 USD | 12,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9890` | 223,250.00 USD | 223,250.00 USD | 0.00 USD | 8,270.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9890` | 207,510.00 USD | 207,510.00 USD | 0.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9910` | 202,650.00 USD | 202,650.00 USD | 59,500.00 USD | 0.00 USD | 19,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9910` | 206,070.00 USD | 206,070.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9930` | 123,380.00 USD | 123,380.00 USD | 6,920.00 USD | 13,250.00 USD | 13,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9930` | 186,480.00 USD | 186,480.00 USD | 0.00 USD | 0.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9950` | 89,840.00 USD | 89,840.00 USD | 0.00 USD | 3,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9950` | 185,260.00 USD | 185,260.00 USD | 16,510.00 USD | 0.00 USD | 42,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9970` | 86,830.00 USD | 86,830.00 USD | 26,250.00 USD | 1,000.00 USD | 1,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9970` | 125,980.00 USD | 125,980.00 USD | 68,870.00 USD | 0.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9990` | 57,970.00 USD | 57,970.00 USD | 0.00 USD | 1,760.00 USD | 1,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.00` | 54,810.00 USD | 54,810.00 USD | 31,780.00 USD | 22,180.00 USD | 848.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.00` | 53,360.00 USD | 53,360.00 USD | 52,850.00 USD | 0.00 USD | 514.14 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 76,030.00 USD | 76,030.00 USD | 53,480.00 USD | 0.00 USD | 22,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 18,570.00 USD | 18,570.00 USD | 0.00 USD | 0.00 USD | 18,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 36,140.00 USD | 36,140.00 USD | 1,190.00 USD | 16,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 76,140.00 USD | 76,140.00 USD | 0.00 USD | 110.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 48,100.00 USD | 48,100.00 USD | 0.00 USD | 11,600.00 USD | 352.75 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 127,320.00 USD | 127,320.00 USD | 16,020.00 USD | 34,770.00 USD | 388.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 98,230.00 USD | 98,230.00 USD | 20,120.00 USD | 21.80 USD | 29,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 160,750.00 USD | 160,750.00 USD | 0.00 USD | 26,360.00 USD | 7,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 130,990.00 USD | 130,990.00 USD | 1,130.00 USD | 7,410.00 USD | 24,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 208,700.00 USD | 208,700.00 USD | 0.00 USD | 21,770.00 USD | 26,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 171,570.00 USD | 171,570.00 USD | 29,890.00 USD | 0.00 USD | 10,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 296,270.00 USD | 296,270.00 USD | 0.00 USD | 75,760.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 215,980.00 USD | 215,980.00 USD | 27,370.00 USD | 2,230.00 USD | 14,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 433,340.00 USD | 433,340.00 USD | 44,170.00 USD | 25,870.00 USD | 67,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 286,180.00 USD | 286,180.00 USD | 37,350.00 USD | 2,990.00 USD | 29,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 700,460.00 USD | 700,460.00 USD | 56,570.00 USD | 85,890.00 USD | 124,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 380,980.00 USD | 380,980.00 USD | 29,910.00 USD | 28,580.00 USD | 36,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 789,390.00 USD | 789,390.00 USD | 11,270.00 USD | 48,490.00 USD | 29,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 422,350.00 USD | 422,350.00 USD | 26,670.00 USD | 10,240.00 USD | 4,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,100,000.00 USD | 1,100,000.00 USD | 160,800.00 USD | 126,720.00 USD | 24,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 504,720.00 USD | 504,720.00 USD | 26,960.00 USD | 20,190.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,300,000.00 USD | 1,300,000.00 USD | 141,540.00 USD | 38,750.00 USD | 22,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 691,880.00 USD | 691,880.00 USD | 132,620.00 USD | 14,130.00 USD | 40,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,490,000.00 USD | 1,490,000.00 USD | 160,920.00 USD | 118.80 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 769,550.00 USD | 769,550.00 USD | 52,980.00 USD | 104.84 USD | 24,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,610,000.00 USD | 1,610,000.00 USD | 122,520.00 USD | 95.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 853,590.00 USD | 853,590.00 USD | 24,170.00 USD | 27,460.00 USD | 32,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 1,920,000.00 USD | 1,920,000.00 USD | 259,060.00 USD | 8,290.00 USD | 43,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,020,000.00 USD | 1,020,000.00 USD | 87,410.00 USD | 14,180.00 USD | 67,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 2,230,000.00 USD | 2,230,000.00 USD | 192,080.00 USD | 3,170.00 USD | 109,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,060,000.00 USD | 1,060,000.00 USD | 10,510.00 USD | 4,170.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 2,590,000.00 USD | 2,590,000.00 USD | 239,200.00 USD | 9,010.00 USD | 117,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,070,000.00 USD | 1,070,000.00 USD | 4,190.00 USD | 4,310.00 USD | 6,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,030,000.00 USD | 3,030,000.00 USD | 276,890.00 USD | 1,930.00 USD | 159,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,120,000.00 USD | 1,120,000.00 USD | 8,860.00 USD | 12,900.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,220,000.00 USD | 3,220,000.00 USD | 49,280.00 USD | 32,550.00 USD | 103,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 1,150,000.00 USD | 1,150,000.00 USD | 5,920.00 USD | 11,350.00 USD | 13,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 3,490,000.00 USD | 3,490,000.00 USD | 184,670.00 USD | 23,650.00 USD | 59,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,190,000.00 USD | 1,190,000.00 USD | 29,850.00 USD | 7,430.00 USD | 1,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,000,000.00 USD | 4,000,000.00 USD | 178,360.00 USD | 96,250.00 USD | 238,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,220,000.00 USD | 1,220,000.00 USD | 2,200.00 USD | 8,000.00 USD | 17,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,210,000.00 USD | 4,210,000.00 USD | 116,670.00 USD | 13,780.00 USD | 77,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,300,000.00 USD | 1,300,000.00 USD | 62,460.00 USD | 4,130.00 USD | 22,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,510,000.00 USD | 4,510,000.00 USD | 175,210.00 USD | 43,690.00 USD | 87,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,350,000.00 USD | 1,350,000.00 USD | 15,580.00 USD | 6,190.00 USD | 27,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,700,000.00 USD | 4,700,000.00 USD | 61,670.00 USD | 55,920.00 USD | 74,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 1,400,000.00 USD | 1,400,000.00 USD | 14,400.00 USD | 979.80 USD | 27,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 4,940,000.00 USD | 4,940,000.00 USD | 127,180.00 USD | 33,860.00 USD | 72,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 156.98 USD | 156.98 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,430,000.00 USD | 1,430,000.00 USD | 5,830.00 USD | 6,460.00 USD | 20,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 5,330,000.00 USD | 5,330,000.00 USD | 220,920.00 USD | 69,880.00 USD | 106,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,470,000.00 USD | 1,470,000.00 USD | 27,860.00 USD | 3,010.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 5,780,000.00 USD | 5,780,000.00 USD | 232,260.00 USD | 71,180.00 USD | 139,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,490,000.00 USD | 1,490,000.00 USD | 1,630.00 USD | 8,320.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,040,000.00 USD | 6,040,000.00 USD | 130,860.00 USD | 56,310.00 USD | 78,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,500,000.00 USD | 1,500,000.00 USD | 4,990.00 USD | 3,010.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,330,000.00 USD | 6,330,000.00 USD | 141,700.00 USD | 73,690.00 USD | 71,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 1,530,000.00 USD | 1,530,000.00 USD | 7,310.00 USD | 3,890.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 6,530,000.00 USD | 6,530,000.00 USD | 90,400.00 USD | 28,390.00 USD | 83,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.06` | 66,030.00 USD | 66,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,550,000.00 USD | 1,550,000.00 USD | 13,460.00 USD | 4,670.00 USD | 6,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 6,740,000.00 USD | 6,740,000.00 USD | 86,760.00 USD | 43,390.00 USD | 82,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,570,000.00 USD | 1,570,000.00 USD | 6,330.00 USD | 4,160.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,040,000.00 USD | 7,040,000.00 USD | 219,670.00 USD | 14,440.00 USD | 62,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,590,000.00 USD | 1,590,000.00 USD | 16,300.00 USD | 3,230.00 USD | 4,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,270,000.00 USD | 7,270,000.00 USD | 141,570.00 USD | 36,670.00 USD | 52,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,610,000.00 USD | 1,610,000.00 USD | 5,820.00 USD | 4,330.00 USD | 12,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,510,000.00 USD | 7,510,000.00 USD | 96,630.00 USD | 42,960.00 USD | 95,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.07` | 1,630,000.00 USD | 1,630,000.00 USD | 4,510.00 USD | 5,370.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 7,690,000.00 USD | 7,690,000.00 USD | 97,650.00 USD | 27,560.00 USD | 60,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 1,650,000.00 USD | 1,650,000.00 USD | 8,480.00 USD | 3,520.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 7,850,000.00 USD | 7,850,000.00 USD | 75,040.00 USD | 29,850.00 USD | 48,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 1,660,000.00 USD | 1,660,000.00 USD | 7,600.00 USD | 3,640.00 USD | 36.19 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,090,000.00 USD | 8,090,000.00 USD | 166,380.00 USD | 21,060.00 USD | 52,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 1,670,000.00 USD | 1,670,000.00 USD | 8,690.00 USD | 1,510.00 USD | 2,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,310,000.00 USD | 8,310,000.00 USD | 164,440.00 USD | 23,690.00 USD | 33,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 1,680,000.00 USD | 1,680,000.00 USD | 2,390.00 USD | 3,030.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,510,000.00 USD | 8,510,000.00 USD | 61,330.00 USD | 41,110.00 USD | 100,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.08` | 1,700,000.00 USD | 1,700,000.00 USD | 5,310.00 USD | 3,010.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 8,660,000.00 USD | 8,660,000.00 USD | 79,580.00 USD | 18,540.00 USD | 46,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 1,710,000.00 USD | 1,710,000.00 USD | 4,440.00 USD | 3,320.00 USD | 3,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 8,880,000.00 USD | 8,880,000.00 USD | 102,510.00 USD | 58,170.00 USD | 66,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 1,710,000.00 USD | 1,710,000.00 USD | 2,400.00 USD | 765.55 USD | 2,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,060,000.00 USD | 9,060,000.00 USD | 71,650.00 USD | 20,280.00 USD | 85,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 1,730,000.00 USD | 1,730,000.00 USD | 5,680.00 USD | 3,410.00 USD | 4,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,190,000.00 USD | 9,190,000.00 USD | 70,660.00 USD | 25,660.00 USD | 32,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 1,730,000.00 USD | 1,730,000.00 USD | 126.39 USD | 2,110.00 USD | 1,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,400,000.00 USD | 9,400,000.00 USD | 92,880.00 USD | 39,220.00 USD | 81,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.09` | 1,740,000.00 USD | 1,740,000.00 USD | 2,430.00 USD | 4,020.00 USD | 90.33 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 9,570,000.00 USD | 9,570,000.00 USD | 56,240.00 USD | 22,740.00 USD | 92,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 1,760,000.00 USD | 1,760,000.00 USD | 7,070.00 USD | 2,710.00 USD | 9,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 9,730,000.00 USD | 9,730,000.00 USD | 88,860.00 USD | 24,770.00 USD | 43,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 1,760,000.00 USD | 1,760,000.00 USD | 2,310.00 USD | 775.48 USD | 3,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,060,000.00 USD | 10,060,000.00 USD | 188,000.00 USD | 49,370.00 USD | 89,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 1,770,000.00 USD | 1,770,000.00 USD | 116.94 USD | 1,520.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,250,000.00 USD | 10,250,000.00 USD | 122,300.00 USD | 44,140.00 USD | 26,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 1,780,000.00 USD | 1,780,000.00 USD | 2,730.00 USD | 3,840.00 USD | 2,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,470,000.00 USD | 10,470,000.00 USD | 91,720.00 USD | 19,430.00 USD | 106,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.10` | 1,780,000.00 USD | 1,780,000.00 USD | 37.25 USD | 2,030.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 10,550,000.00 USD | 10,550,000.00 USD | 36,570.00 USD | 10,390.00 USD | 31,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.10` | 169.18 USD | 66,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.11` | 1,790,000.00 USD | 1,790,000.00 USD | 4,080.00 USD | 1,690.00 USD | 111.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 10,660,000.00 USD | 10,660,000.00 USD | 51,840.00 USD | 24,280.00 USD | 34,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.11` | 1,790,000.00 USD | 1,790,000.00 USD | 1,670.00 USD | 87.40 USD | 803.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 10,850,000.00 USD | 10,850,000.00 USD | 80,930.00 USD | 42,230.00 USD | 63,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.11` | 1,810,000.00 USD | 1,810,000.00 USD | 12,800.00 USD | 3,460.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,000,000.00 USD | 11,000,000.00 USD | 69,040.00 USD | 16,050.00 USD | 64,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.11` | 1,830,000.00 USD | 1,830,000.00 USD | 11,280.00 USD | 260.69 USD | 10,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,080,000.00 USD | 11,080,000.00 USD | 20,190.00 USD | 43,570.00 USD | 25,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.11` | 1,840,000.00 USD | 1,840,000.00 USD | 3,720.00 USD | 294.76 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 11,140,000.00 USD | 11,140,000.00 USD | 34,700.00 USD | 15,310.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.12` | 1,850,000.00 USD | 1,850,000.00 USD | 56.85 USD | 1,860.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,290,000.00 USD | 11,290,000.00 USD | 68,170.00 USD | 45,980.00 USD | 32,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.12` | 1,860,000.00 USD | 1,860,000.00 USD | 10,810.00 USD | 658.54 USD | 4,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,350,000.00 USD | 11,350,000.00 USD | 24,700.00 USD | 22,760.00 USD | 13,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.12` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 382.75 USD | 452.67 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,460,000.00 USD | 11,460,000.00 USD | 48,980.00 USD | 30,950.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.12` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 12.35 USD | 186.24 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,550,000.00 USD | 11,550,000.00 USD | 61,780.00 USD | 5,220.00 USD | 25,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.12` | 1,870,000.00 USD | 1,870,000.00 USD | 199.10 USD | 12.50 USD | 2,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 11,610,000.00 USD | 11,610,000.00 USD | 18,300.00 USD | 10,940.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.13` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 1,020.00 USD | 870.54 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 11,630,000.00 USD | 11,630,000.00 USD | 14,700.00 USD | 342.11 USD | 8,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.13` | 1,870,000.00 USD | 1,870,000.00 USD | 2,860.00 USD | 432.73 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 11,750,000.00 USD | 11,750,000.00 USD | 56,500.00 USD | 19,160.00 USD | 45,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 11,960,000.00 USD | 11,960,000.00 USD | 106,510.00 USD | 12,710.00 USD | 90,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 12,000,000.00 USD | 12,000,000.00 USD | 16,560.00 USD | 0.00 USD | 22,800.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.8710` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 21,960.00 USD | 3,060.00 USD | 6,140.00 USD |
| `7D` | `0.8730` | 5,280,000.00 USD | 0.00 USD | 5,280,000.00 USD | 0.00 USD | 2,120.00 USD | 295.31 USD |
| `7D` | `0.8750` | 5,280,000.00 USD | 0.00 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 5,750.00 USD |
| `7D` | `0.8770` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 20,650.00 USD | 6,200.00 USD | 2,760.00 USD |
| `7D` | `0.8790` | 5,240,000.00 USD | 0.00 USD | 5,240,000.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD |
| `7D` | `0.8810` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 228.30 USD | 114.50 USD | 0.00 USD |
| `7D` | `0.8830` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 8,430.00 USD | 5,730.00 USD | 360.61 USD |
| `7D` | `0.8850` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 8,630.00 USD | 3,180.00 USD | 698.60 USD |
| `7D` | `0.8870` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 11,700.00 USD | 5,060.00 USD | 6,640.00 USD |
| `7D` | `0.8890` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 13,840.00 USD | 5,370.00 USD | 11,560.00 USD |
| `7D` | `0.8910` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 30,330.00 USD | 7,940.00 USD | 24,650.00 USD |
| `7D` | `0.8930` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 24,780.00 USD | 5,820.00 USD | 9,960.00 USD |
| `7D` | `0.8950` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 7,380.00 USD | 10,730.00 USD | 27,510.00 USD |
| `1D` | `0.8970` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 8,810.00 USD | 6,780.00 USD | 11,750.00 USD |
| `7D` | `0.8970` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 43,430.00 USD | 5,400.00 USD | 31,920.00 USD |
| `1D` | `0.8990` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 5,550.00 USD | 757.19 USD | 3,550.00 USD |
| `7D` | `0.8990` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 52,250.00 USD | 14,640.00 USD | 20,000.00 USD |
| `1D` | `0.9010` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 0.00 USD | 1,530.00 USD | 1,880.00 USD |
| `7D` | `0.9010` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 20,170.00 USD | 11,570.00 USD | 4,600.00 USD |
| `1D` | `0.9030` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 4,100.00 USD | 3,760.00 USD | 2,370.00 USD |
| `7D` | `0.9030` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 12,700.00 USD | 8,710.00 USD | 21,670.00 USD |
| `1D` | `0.9050` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 8,300.00 USD | 3,640.00 USD | 3,200.00 USD |
| `7D` | `0.9050` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 35,230.00 USD | 25,240.00 USD | 27,300.00 USD |
| `1D` | `0.9070` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 3,810.00 USD | 488.01 USD | 803.91 USD |
| `7D` | `0.9070` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 37,740.00 USD | 7,720.00 USD | 15,280.00 USD |
| `1D` | `0.9090` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 18,830.00 USD | 4,070.00 USD | 4,140.00 USD |
| `7D` | `0.9090` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 13,790.00 USD | 8,050.00 USD | 6,240.00 USD |
| `1D` | `0.9110` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 13,080.00 USD | 791.28 USD | 10,580.00 USD |
| `7D` | `0.9110` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 8,490.00 USD | 7,760.00 USD | 17,140.00 USD |
| `1D` | `0.9130` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 4,770.00 USD | 441.47 USD | 4,830.00 USD |
| `7D` | `0.9130` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 26,980.00 USD | 2,110.00 USD | 680.66 USD |
| `1D` | `0.9150` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 14,130.00 USD | 2,620.00 USD | 8,480.00 USD |
| `7D` | `0.9150` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 41,000.00 USD | 10,660.00 USD | 34,610.00 USD |
| `1D` | `0.9170` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 3,440.00 USD | 435.13 USD | 452.67 USD |
| `7D` | `0.9170` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 22,610.00 USD | 14,810.00 USD | 18,060.00 USD |
| `1D` | `0.9190` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 2,770.00 USD | 138.43 USD | 186.24 USD |
| `7D` | `0.9190` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 33,980.00 USD | 4,860.00 USD | 19,620.00 USD |
| `1D` | `0.9210` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 1,580.00 USD | 48.64 USD | 2,330.00 USD |
| `7D` | `0.9210` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 22,070.00 USD | 7,060.00 USD | 15,880.00 USD |
| `1D` | `0.9230` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 10,750.00 USD | 2,010.00 USD | 907.53 USD |
| `7D` | `0.9230` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 35,230.00 USD | 11,030.00 USD | 37,340.00 USD |
| `1D` | `0.9250` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 19,910.00 USD | 8,910.00 USD | 14,770.00 USD |
| `7D` | `0.9250` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 56,800.00 USD | 9,090.00 USD | 30,000.00 USD |
| `1D` | `0.9270` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 15,110.00 USD | 5,250.00 USD | 10,980.00 USD |
| `7D` | `0.9270` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 70,300.00 USD | 9,380.00 USD | 21,390.00 USD |
| `1D` | `0.9290` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 25,710.00 USD | 4,260.00 USD | 6,800.00 USD |
| `7D` | `0.9290` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 39,160.00 USD | 8,340.00 USD | 31,560.00 USD |
| `1D` | `0.9310` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 10,550.00 USD | 12,130.00 USD | 21,600.00 USD |
| `7D` | `0.9310` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 26,530.00 USD | 10,070.00 USD | 7,590.00 USD |
| `1D` | `0.9330` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 21,780.00 USD | 9,020.00 USD | 9,250.00 USD |
| `7D` | `0.9330` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 33,550.00 USD | 9,510.00 USD | 25,450.00 USD |
| `1D` | `0.9350` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 36,280.00 USD | 10,930.00 USD | 13,660.00 USD |
| `7D` | `0.9350` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 82,010.00 USD | 29,330.00 USD | 17,380.00 USD |
| `1D` | `0.9370` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 38,570.00 USD | 12,840.00 USD | 20,310.00 USD |
| `7D` | `0.9370` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 29,580.00 USD | 14,910.00 USD | 7,230.00 USD |
| `1D` | `0.9390` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 17,730.00 USD | 14,390.00 USD | 13,920.00 USD |
| `7D` | `0.9390` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 18,750.00 USD | 14,310.00 USD | 12,300.00 USD |
| `1D` | `0.9410` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 35,920.00 USD | 11,380.00 USD | 2,030.00 USD |
| `7D` | `0.9410` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 45,790.00 USD | 14,500.00 USD | 4,310.00 USD |
| `1D` | `0.9430` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 21,480.00 USD | 8,450.00 USD | 3,110.00 USD |
| `7D` | `0.9430` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 54,680.00 USD | 11,100.00 USD | 10,990.00 USD |
| `1D` | `0.9450` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 36,850.00 USD | 20,360.00 USD | 40,150.00 USD |
| `7D` | `0.9450` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 77,230.00 USD | 33,720.00 USD | 41,460.00 USD |
| `1D` | `0.9470` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 45,400.00 USD | 24,750.00 USD | 40,860.00 USD |
| `7D` | `0.9470` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 108,740.00 USD | 24,210.00 USD | 50,080.00 USD |
| `1D` | `0.9490` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 74,440.00 USD | 15,840.00 USD | 21,110.00 USD |
| `7D` | `0.9490` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 129,370.00 USD | 34,600.00 USD | 113,810.00 USD |
| `1D` | `0.9510` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 34,350.00 USD | 30,330.00 USD | 48,430.00 USD |
| `7D` | `0.9510` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 198,910.00 USD | 37,160.00 USD | 81,400.00 USD |
| `1D` | `0.9530` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 50,320.00 USD | 22,180.00 USD | 21,850.00 USD |
| `7D` | `0.9530` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 79,700.00 USD | 27,910.00 USD | 123,120.00 USD |
| `1D` | `0.9550` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 78,960.00 USD | 38,020.00 USD | 38,490.00 USD |
| `7D` | `0.9550` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 172,820.00 USD | 90,890.00 USD | 56,600.00 USD |
| `1D` | `0.9570` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 130,660.00 USD | 45,370.00 USD | 68,880.00 USD |
| `7D` | `0.9570` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 129,820.00 USD | 45,870.00 USD | 128,830.00 USD |
| `1D` | `0.9590` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 49,590.00 USD | 20,710.00 USD | 37,020.00 USD |
| `7D` | `0.9590` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 176,280.00 USD | 56,660.00 USD | 72,780.00 USD |
| `1D` | `0.9610` | 906,220.00 USD | 0.00 USD | 906,220.00 USD | 53,350.00 USD | 25,860.00 USD | 11,990.00 USD |
| `7D` | `0.9610` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 183,020.00 USD | 77,580.00 USD | 32,500.00 USD |
| `1D` | `0.9630` | 815,010.00 USD | 0.00 USD | 815,010.00 USD | 27,750.00 USD | 19,430.00 USD | 17,520.00 USD |
| `7D` | `0.9630` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 95,260.00 USD | 281.90 USD | 12,410.00 USD |
| `1D` | `0.9650` | 750,310.00 USD | 0.00 USD | 750,310.00 USD | 25,320.00 USD | 13,180.00 USD | 31,270.00 USD |
| `7D` | `0.9650` | 937,000.00 USD | 0.00 USD | 937,000.00 USD | 65,160.00 USD | 1,120.00 USD | 9,130.00 USD |
| `1D` | `0.9670` | 680,530.00 USD | 0.00 USD | 680,530.00 USD | 28,790.00 USD | 14,700.00 USD | 21,600.00 USD |
| `7D` | `0.9670` | 861,590.00 USD | 0.00 USD | 861,590.00 USD | 31,440.00 USD | 12,830.00 USD | 45,920.00 USD |
| `1D` | `0.9690` | 615,450.00 USD | 0.00 USD | 615,450.00 USD | 37,870.00 USD | 22,640.00 USD | 31,220.00 USD |
| `7D` | `0.9690` | 771,400.00 USD | 0.00 USD | 771,400.00 USD | 3,040.00 USD | 11,390.00 USD | 37,920.00 USD |
| `1D` | `0.9710` | 523,720.00 USD | 0.00 USD | 523,720.00 USD | 54,360.00 USD | 12,350.00 USD | 21,140.00 USD |
| `7D` | `0.9710` | 719,050.00 USD | 0.00 USD | 719,050.00 USD | 64,680.00 USD | 619.85 USD | 9,790.00 USD |
| `1D` | `0.9730` | 435,890.00 USD | 0.00 USD | 435,890.00 USD | 13,580.00 USD | 691.66 USD | 13,670.00 USD |
| `7D` | `0.9730` | 643,960.00 USD | 0.00 USD | 643,960.00 USD | 0.00 USD | 0.00 USD | 7,510.00 USD |
| `1D` | `0.9750` | 407,950.00 USD | 0.00 USD | 407,950.00 USD | 10,430.00 USD | 18,900.00 USD | 5,660.00 USD |
| `7D` | `0.9750` | 636,450.00 USD | 0.00 USD | 636,450.00 USD | 0.00 USD | 16,590.00 USD | 3,280.00 USD |
| `1D` | `0.9770` | 372,960.00 USD | 0.00 USD | 372,960.00 USD | 35,620.00 USD | 2,870.00 USD | 10,900.00 USD |
| `7D` | `0.9770` | 616,580.00 USD | 0.00 USD | 616,580.00 USD | 15,320.00 USD | 5,480.00 USD | 31,410.00 USD |
| `1D` | `0.9790` | 323,590.00 USD | 0.00 USD | 323,590.00 USD | 9,790.00 USD | 4,480.00 USD | 8,180.00 USD |
| `7D` | `0.9790` | 564,370.00 USD | 0.00 USD | 564,370.00 USD | 0.00 USD | 15,440.00 USD | 89,530.00 USD |
| `1D` | `0.9810` | 301,140.00 USD | 0.00 USD | 301,140.00 USD | 4,500.00 USD | 376.40 USD | 8,930.00 USD |
| `7D` | `0.9810` | 459,400.00 USD | 0.00 USD | 459,400.00 USD | 7,900.00 USD | 0.00 USD | 132,960.00 USD |
| `1D` | `0.9830` | 287,330.00 USD | 0.00 USD | 287,330.00 USD | 9,030.00 USD | 13,960.00 USD | 6,020.00 USD |
| `7D` | `0.9830` | 318,550.00 USD | 0.00 USD | 318,550.00 USD | 2,190.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9850` | 258,330.00 USD | 0.00 USD | 258,330.00 USD | 575.70 USD | 0.00 USD | 10,740.00 USD |
| `7D` | `0.9850` | 316,360.00 USD | 0.00 USD | 316,360.00 USD | 0.00 USD | 16,440.00 USD | 22,820.00 USD |
| `1D` | `0.9870` | 247,020.00 USD | 0.00 USD | 247,020.00 USD | 13,720.00 USD | 10,040.00 USD | 0.00 USD |
| `7D` | `0.9870` | 277,100.00 USD | 0.00 USD | 277,100.00 USD | 40,020.00 USD | 16,870.00 USD | 12,710.00 USD |
| `1D` | `0.9890` | 223,250.00 USD | 0.00 USD | 223,250.00 USD | 0.00 USD | 8,270.00 USD | 12,330.00 USD |
| `7D` | `0.9890` | 207,510.00 USD | 0.00 USD | 207,510.00 USD | 0.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `0.9910` | 202,650.00 USD | 0.00 USD | 202,650.00 USD | 59,500.00 USD | 0.00 USD | 19,770.00 USD |
| `7D` | `0.9910` | 206,070.00 USD | 0.00 USD | 206,070.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD |
| `1D` | `0.9930` | 123,380.00 USD | 0.00 USD | 123,380.00 USD | 6,920.00 USD | 13,250.00 USD | 13,370.00 USD |
| `7D` | `0.9930` | 186,480.00 USD | 0.00 USD | 186,480.00 USD | 0.00 USD | 0.00 USD | 1,220.00 USD |
| `1D` | `0.9950` | 89,840.00 USD | 0.00 USD | 89,840.00 USD | 0.00 USD | 3,020.00 USD | 0.00 USD |
| `7D` | `0.9950` | 185,260.00 USD | 0.00 USD | 185,260.00 USD | 16,510.00 USD | 0.00 USD | 42,770.00 USD |
| `1D` | `0.9970` | 86,830.00 USD | 0.00 USD | 86,830.00 USD | 26,250.00 USD | 1,000.00 USD | 1,610.00 USD |
| `7D` | `0.9970` | 125,980.00 USD | 0.00 USD | 125,980.00 USD | 68,870.00 USD | 0.00 USD | 3,750.00 USD |
| `1D` | `0.9990` | 57,970.00 USD | 0.00 USD | 57,970.00 USD | 0.00 USD | 1,760.00 USD | 1,400.00 USD |
| `1D` | `1.00` | 54,810.00 USD | 0.00 USD | 54,810.00 USD | 31,780.00 USD | 22,180.00 USD | 848.87 USD |
| `7D` | `1.00` | 53,360.00 USD | 0.00 USD | 53,360.00 USD | 52,850.00 USD | 0.00 USD | 514.14 USD |
| `1D` | `1.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.00` | 76,030.00 USD | 76,030.00 USD | 0.00 USD | 53,480.00 USD | 0.00 USD | 22,550.00 USD |
| `1D` | `1.01` | 18,570.00 USD | 18,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,570.00 USD |
| `1D` | `1.01` | 36,140.00 USD | 36,140.00 USD | 0.00 USD | 1,190.00 USD | 16,390.00 USD | 0.00 USD |
| `7D` | `1.01` | 76,140.00 USD | 76,140.00 USD | 0.00 USD | 0.00 USD | 110.10 USD | 0.00 USD |
| `1D` | `1.01` | 48,100.00 USD | 48,100.00 USD | 0.00 USD | 0.00 USD | 11,600.00 USD | 352.75 USD |
| `7D` | `1.01` | 127,320.00 USD | 127,320.00 USD | 0.00 USD | 16,020.00 USD | 34,770.00 USD | 388.43 USD |
| `1D` | `1.01` | 98,230.00 USD | 98,230.00 USD | 0.00 USD | 20,120.00 USD | 21.80 USD | 29,990.00 USD |
| `7D` | `1.01` | 160,750.00 USD | 160,750.00 USD | 0.00 USD | 0.00 USD | 26,360.00 USD | 7,070.00 USD |
| `1D` | `1.02` | 130,990.00 USD | 130,990.00 USD | 0.00 USD | 1,130.00 USD | 7,410.00 USD | 24,210.00 USD |
| `7D` | `1.02` | 208,700.00 USD | 208,700.00 USD | 0.00 USD | 0.00 USD | 21,770.00 USD | 26,170.00 USD |
| `1D` | `1.02` | 171,570.00 USD | 171,570.00 USD | 0.00 USD | 29,890.00 USD | 0.00 USD | 10,690.00 USD |
| `7D` | `1.02` | 296,270.00 USD | 296,270.00 USD | 0.00 USD | 0.00 USD | 75,760.00 USD | 11,810.00 USD |
| `1D` | `1.02` | 215,980.00 USD | 215,980.00 USD | 0.00 USD | 27,370.00 USD | 2,230.00 USD | 14,810.00 USD |
| `7D` | `1.02` | 433,340.00 USD | 433,340.00 USD | 0.00 USD | 44,170.00 USD | 25,870.00 USD | 67,030.00 USD |
| `1D` | `1.02` | 286,180.00 USD | 286,180.00 USD | 0.00 USD | 37,350.00 USD | 2,990.00 USD | 29,870.00 USD |
| `7D` | `1.02` | 700,460.00 USD | 700,460.00 USD | 0.00 USD | 56,570.00 USD | 85,890.00 USD | 124,660.00 USD |
| `1D` | `1.02` | 380,980.00 USD | 380,980.00 USD | 0.00 USD | 29,910.00 USD | 28,580.00 USD | 36,320.00 USD |
| `7D` | `1.02` | 789,390.00 USD | 789,390.00 USD | 0.00 USD | 11,270.00 USD | 48,490.00 USD | 29,170.00 USD |
| `1D` | `1.03` | 422,350.00 USD | 422,350.00 USD | 0.00 USD | 26,670.00 USD | 10,240.00 USD | 4,450.00 USD |
| `7D` | `1.03` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 160,800.00 USD | 126,720.00 USD | 24,880.00 USD |
| `1D` | `1.03` | 504,720.00 USD | 504,720.00 USD | 0.00 USD | 26,960.00 USD | 20,190.00 USD | 35,230.00 USD |
| `7D` | `1.03` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 141,540.00 USD | 38,750.00 USD | 22,910.00 USD |
| `1D` | `1.03` | 691,880.00 USD | 691,880.00 USD | 0.00 USD | 132,620.00 USD | 14,130.00 USD | 40,410.00 USD |
| `7D` | `1.03` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 160,920.00 USD | 118.80 USD | 19,590.00 USD |
| `1D` | `1.03` | 769,550.00 USD | 769,550.00 USD | 0.00 USD | 52,980.00 USD | 104.84 USD | 24,580.00 USD |
| `7D` | `1.03` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 122,520.00 USD | 95.00 USD | 3,750.00 USD |
| `1D` | `1.03` | 853,590.00 USD | 853,590.00 USD | 0.00 USD | 24,170.00 USD | 27,460.00 USD | 32,400.00 USD |
| `7D` | `1.03` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 259,060.00 USD | 8,290.00 USD | 43,490.00 USD |
| `1D` | `1.04` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 87,410.00 USD | 14,180.00 USD | 67,970.00 USD |
| `7D` | `1.04` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 192,080.00 USD | 3,170.00 USD | 109,460.00 USD |
| `1D` | `1.04` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 10,510.00 USD | 4,170.00 USD | 18,230.00 USD |
| `7D` | `1.04` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 239,200.00 USD | 9,010.00 USD | 117,630.00 USD |
| `1D` | `1.04` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 4,190.00 USD | 4,310.00 USD | 6,890.00 USD |
| `7D` | `1.04` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 276,890.00 USD | 1,930.00 USD | 159,290.00 USD |
| `1D` | `1.04` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 8,860.00 USD | 12,900.00 USD | 24,280.00 USD |
| `7D` | `1.04` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 49,280.00 USD | 32,550.00 USD | 103,800.00 USD |
| `1D` | `1.04` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 5,920.00 USD | 11,350.00 USD | 13,170.00 USD |
| `7D` | `1.04` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 184,670.00 USD | 23,650.00 USD | 59,810.00 USD |
| `1D` | `1.05` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 29,850.00 USD | 7,430.00 USD | 1,860.00 USD |
| `7D` | `1.05` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 178,360.00 USD | 96,250.00 USD | 238,570.00 USD |
| `1D` | `1.05` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 2,200.00 USD | 8,000.00 USD | 17,750.00 USD |
| `7D` | `1.05` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 116,670.00 USD | 13,780.00 USD | 77,320.00 USD |
| `1D` | `1.05` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 62,460.00 USD | 4,130.00 USD | 22,780.00 USD |
| `7D` | `1.05` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 175,210.00 USD | 43,690.00 USD | 87,050.00 USD |
| `1D` | `1.05` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 15,580.00 USD | 6,190.00 USD | 27,030.00 USD |
| `7D` | `1.05` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 61,670.00 USD | 55,920.00 USD | 74,380.00 USD |
| `1D` | `1.05` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 14,400.00 USD | 979.80 USD | 27,520.00 USD |
| `7D` | `1.05` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 127,180.00 USD | 33,860.00 USD | 72,330.00 USD |
| `1D` | `1.06` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 5,830.00 USD | 6,460.00 USD | 20,020.00 USD |
| `7D` | `1.06` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 220,920.00 USD | 69,880.00 USD | 106,190.00 USD |
| `1D` | `1.06` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 27,860.00 USD | 3,010.00 USD | 13,590.00 USD |
| `7D` | `1.06` | 5,780,000.00 USD | 5,780,000.00 USD | 0.00 USD | 232,260.00 USD | 71,180.00 USD | 139,220.00 USD |
| `1D` | `1.06` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 1,630.00 USD | 8,320.00 USD | 10,800.00 USD |
| `7D` | `1.06` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 130,860.00 USD | 56,310.00 USD | 78,020.00 USD |
| `1D` | `1.06` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 4,990.00 USD | 3,010.00 USD | 2,590.00 USD |
| `7D` | `1.06` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 141,700.00 USD | 73,690.00 USD | 71,060.00 USD |
| `1D` | `1.06` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 7,310.00 USD | 3,890.00 USD | 9,680.00 USD |
| `7D` | `1.06` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 90,400.00 USD | 28,390.00 USD | 83,920.00 USD |
| `1D` | `1.07` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 13,460.00 USD | 4,670.00 USD | 6,100.00 USD |
| `7D` | `1.07` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 86,760.00 USD | 43,390.00 USD | 82,980.00 USD |
| `1D` | `1.07` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 6,330.00 USD | 4,160.00 USD | 6,120.00 USD |
| `7D` | `1.07` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 219,670.00 USD | 14,440.00 USD | 62,270.00 USD |
| `1D` | `1.07` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 16,300.00 USD | 3,230.00 USD | 4,120.00 USD |
| `7D` | `1.07` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 141,570.00 USD | 36,670.00 USD | 52,290.00 USD |
| `1D` | `1.07` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 5,820.00 USD | 4,330.00 USD | 12,130.00 USD |
| `7D` | `1.07` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 96,630.00 USD | 42,960.00 USD | 95,510.00 USD |
| `1D` | `1.07` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 4,510.00 USD | 5,370.00 USD | 10,050.00 USD |
| `7D` | `1.07` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 97,650.00 USD | 27,560.00 USD | 60,670.00 USD |
| `1D` | `1.08` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 8,480.00 USD | 3,520.00 USD | 5,470.00 USD |
| `7D` | `1.08` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 75,040.00 USD | 29,850.00 USD | 48,910.00 USD |
| `1D` | `1.08` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 7,600.00 USD | 3,640.00 USD | 36.19 USD |
| `7D` | `1.08` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 166,380.00 USD | 21,060.00 USD | 52,480.00 USD |
| `1D` | `1.08` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 8,690.00 USD | 1,510.00 USD | 2,570.00 USD |
| `7D` | `1.08` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 164,440.00 USD | 23,690.00 USD | 33,710.00 USD |
| `1D` | `1.08` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 2,390.00 USD | 3,030.00 USD | 2,640.00 USD |
| `7D` | `1.08` | 8,510,000.00 USD | 8,510,000.00 USD | 0.00 USD | 61,330.00 USD | 41,110.00 USD | 100,590.00 USD |
| `1D` | `1.08` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 5,310.00 USD | 3,010.00 USD | 6,150.00 USD |
| `7D` | `1.08` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 79,580.00 USD | 18,540.00 USD | 46,440.00 USD |
| `1D` | `1.09` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 4,440.00 USD | 3,320.00 USD | 3,800.00 USD |
| `7D` | `1.09` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 102,510.00 USD | 58,170.00 USD | 66,160.00 USD |
| `1D` | `1.09` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 2,400.00 USD | 765.55 USD | 2,270.00 USD |
| `7D` | `1.09` | 9,060,000.00 USD | 9,060,000.00 USD | 0.00 USD | 71,650.00 USD | 20,280.00 USD | 85,930.00 USD |
| `1D` | `1.09` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 5,680.00 USD | 3,410.00 USD | 4,050.00 USD |
| `7D` | `1.09` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 70,660.00 USD | 25,660.00 USD | 32,870.00 USD |
| `1D` | `1.09` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 126.39 USD | 2,110.00 USD | 1,930.00 USD |
| `7D` | `1.09` | 9,400,000.00 USD | 9,400,000.00 USD | 0.00 USD | 92,880.00 USD | 39,220.00 USD | 81,630.00 USD |
| `1D` | `1.09` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 2,430.00 USD | 4,020.00 USD | 90.33 USD |
| `7D` | `1.09` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 56,240.00 USD | 22,740.00 USD | 92,520.00 USD |
| `1D` | `1.10` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 7,070.00 USD | 2,710.00 USD | 9,740.00 USD |
| `7D` | `1.10` | 9,730,000.00 USD | 9,730,000.00 USD | 0.00 USD | 88,860.00 USD | 24,770.00 USD | 43,830.00 USD |
| `1D` | `1.10` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 2,310.00 USD | 775.48 USD | 3,550.00 USD |
| `7D` | `1.10` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 188,000.00 USD | 49,370.00 USD | 89,650.00 USD |
| `1D` | `1.10` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 116.94 USD | 1,520.00 USD | 1,880.00 USD |
| `7D` | `1.10` | 10,250,000.00 USD | 10,250,000.00 USD | 0.00 USD | 122,300.00 USD | 44,140.00 USD | 26,760.00 USD |
| `1D` | `1.10` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 2,730.00 USD | 3,840.00 USD | 2,370.00 USD |
| `7D` | `1.10` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 91,720.00 USD | 19,430.00 USD | 106,290.00 USD |
| `1D` | `1.10` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 37.25 USD | 2,030.00 USD | 3,090.00 USD |
| `7D` | `1.10` | 10,550,000.00 USD | 10,550,000.00 USD | 0.00 USD | 36,570.00 USD | 10,390.00 USD | 31,450.00 USD |
| `1D` | `1.11` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 4,080.00 USD | 1,690.00 USD | 111.00 USD |
| `7D` | `1.11` | 10,660,000.00 USD | 10,660,000.00 USD | 0.00 USD | 51,840.00 USD | 24,280.00 USD | 34,190.00 USD |
| `1D` | `1.11` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 1,670.00 USD | 87.40 USD | 803.91 USD |
| `7D` | `1.11` | 10,850,000.00 USD | 10,850,000.00 USD | 0.00 USD | 80,930.00 USD | 42,230.00 USD | 63,380.00 USD |
| `1D` | `1.11` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 12,800.00 USD | 3,460.00 USD | 4,140.00 USD |
| `7D` | `1.11` | 11,000,000.00 USD | 11,000,000.00 USD | 0.00 USD | 69,040.00 USD | 16,050.00 USD | 64,910.00 USD |
| `1D` | `1.11` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 11,280.00 USD | 260.69 USD | 10,580.00 USD |
| `7D` | `1.11` | 11,080,000.00 USD | 11,080,000.00 USD | 0.00 USD | 20,190.00 USD | 43,570.00 USD | 25,640.00 USD |
| `1D` | `1.11` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 3,720.00 USD | 294.76 USD | 4,830.00 USD |
| `7D` | `1.11` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 34,700.00 USD | 15,310.00 USD | 9,990.00 USD |
| `1D` | `1.12` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 56.85 USD | 1,860.00 USD | 4,080.00 USD |
| `7D` | `1.12` | 11,290,000.00 USD | 11,290,000.00 USD | 0.00 USD | 68,170.00 USD | 45,980.00 USD | 32,030.00 USD |
| `1D` | `1.12` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 10,810.00 USD | 658.54 USD | 4,390.00 USD |
| `7D` | `1.12` | 11,350,000.00 USD | 11,350,000.00 USD | 0.00 USD | 24,700.00 USD | 22,760.00 USD | 13,750.00 USD |
| `1D` | `1.12` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 382.75 USD | 452.67 USD |
| `7D` | `1.12` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 48,980.00 USD | 30,950.00 USD | 23,330.00 USD |
| `1D` | `1.12` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 12.35 USD | 186.24 USD |
| `7D` | `1.12` | 11,550,000.00 USD | 11,550,000.00 USD | 0.00 USD | 61,780.00 USD | 5,220.00 USD | 25,460.00 USD |
| `1D` | `1.12` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 199.10 USD | 12.50 USD | 2,330.00 USD |
| `7D` | `1.12` | 11,610,000.00 USD | 11,610,000.00 USD | 0.00 USD | 18,300.00 USD | 10,940.00 USD | 29,890.00 USD |
| `1D` | `1.13` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 1,020.00 USD | 870.54 USD |
| `7D` | `1.13` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 14,700.00 USD | 342.11 USD | 8,690.00 USD |
| `1D` | `1.13` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 2,860.00 USD | 432.73 USD | 0.00 USD |
| `7D` | `1.13` | 11,750,000.00 USD | 11,750,000.00 USD | 0.00 USD | 56,500.00 USD | 19,160.00 USD | 45,770.00 USD |
| `7D` | `1.13` | 11,960,000.00 USD | 11,960,000.00 USD | 0.00 USD | 106,510.00 USD | 12,710.00 USD | 90,000.00 USD |
| `7D` | `1.13` | 12,000,000.00 USD | 12,000,000.00 USD | 0.00 USD | 16,560.00 USD | 0.00 USD | 22,800.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `BALANCED` | 9,850.00 USD | 0.00 USD | 9,850.00 USD | -9,850.00 USD | `1` | `2026-10-29 17:35:00 UTC - 2026-10-29 17:40:00 UTC` |
| `15m` | `BALANCED` | 9,850.00 USD | 0.00 USD | 9,850.00 USD | -9,850.00 USD | `1` | `2026-10-29 17:30:00 UTC - 2026-10-29 17:45:00 UTC` |
| `1h` | `BALANCED` | 9,850.00 USD | 0.00 USD | 9,850.00 USD | -9,850.00 USD | `1` | `2026-10-29 17:00:00 UTC - 2026-10-29 18:00:00 UTC` |
| `4h` | `BALANCED` | 9,850.00 USD | 0.00 USD | 9,850.00 USD | -9,850.00 USD | `1` | `2026-10-29 16:00:00 UTC - 2026-10-29 20:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `211.62M` | Total OI Tokens: `211,468,463.5 DOT`
  * 1h OI Change: `-1.27%` | 4h OI Change: `0.00%` | 24h OI Change: `-1.89%`
  * Exchange Breakdown: Binance=`36.99M` | Bybit=`24.87M` | OKX=`10.36M` | Hyperliquid=`5.83M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.44K` | Last 24h: `7.91K` | Last 3d: `-10.37K` | Last 7d: `-19.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0081%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `52.65%` | `47.35%` | `1.11` | 7,800,000.00 USD |
| `15M` | `Binance` | `53.95%` | `46.05%` | `1.17` | 2,870,000.00 USD |
| `15M` | `OKX` | `44.74%` | `55.26%` | `0.81` | 967,020.00 USD |
| `15M` | `Bybit` | `62.81%` | `37.19%` | `1.69` | 945,520.00 USD |
| `15M` | `KuCoin` | `60.98%` | `39.02%` | `1.56` | 114,040.00 USD |
| `15M` | `Gate` | `65.81%` | `34.19%` | `1.92` | 229,650.00 USD |
| `15M` | `Bitget` | `43.91%` | `56.09%` | `0.78` | 559,830.00 USD |
| `15M` | `BingX` | `45.33%` | `54.67%` | `0.83` | 229,970.00 USD |
| `15M` | `MEXC` | `52.62%` | `47.38%` | `1.11` | 868,920.00 USD |
| `15M` | `Bitunix` | `55.5%` | `44.5%` | `1.25` | 187,060.00 USD |
| `15M` | `Hyperliquid` | `29.05%` | `70.95%` | `0.41` | 327,290.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.12%` | `49.88%` | `1.00` | 54,650.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `62.42%` | `37.58%` | `1.66` | 347,610.00 USD |
| `15M` | `HTX` | `55.4%` | `44.6%` | `1.24` | 9,500.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `67.11%` | `32.89%` | `2.04` | 80,520.00 USD |
| `15M` | `Aster` | `8.8%` | `91.2%` | `0.10` | 8,230.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `68.68%` | `31.32%` | `2.19` | 3,220.00 USD |
| `15M` | `Whale Positions` | `53.95%` | `46.05%` | `1.17` | 2,870,000.00 USD |
| `15M` | `Global Accounts` | `52.65%` | `47.35%` | `1.11` | 7,800,000.00 USD |
| `1H` | `DOT` | `45.61%` | `54.39%` | `0.84` | 23,700,000.00 USD |
| `1H` | `Binance` | `44.96%` | `55.04%` | `0.82` | 6,580,000.00 USD |
| `1H` | `OKX` | `42.48%` | `57.52%` | `0.74` | 1,900,000.00 USD |
| `1H` | `Bybit` | `45.64%` | `54.36%` | `0.84` | 1,800,000.00 USD |
| `1H` | `KuCoin` | `55.07%` | `44.93%` | `1.23` | 232,340.00 USD |
| `1H` | `Gate` | `55.07%` | `44.93%` | `1.23` | 349,770.00 USD |
| `1H` | `Bitget` | `36.78%` | `63.22%` | `0.58` | 744,440.00 USD |
| `1H` | `BingX` | `45.24%` | `54.76%` | `0.83` | 771,750.00 USD |
| `1H` | `MEXC` | `49.71%` | `50.29%` | `0.99` | 8,670,000.00 USD |
| `1H` | `Bitunix` | `40.95%` | `59.05%` | `0.69` | 655,010.00 USD |
| `1H` | `Hyperliquid` | `65.26%` | `34.74%` | `1.88` | 560,800.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.27%` | `50.73%` | `0.97` | 566,110.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `0.26%` | `99.74%` | `0.00` | 571,360.00 USD |
| `1H` | `HTX` | `87.22%` | `12.78%` | `6.82` | 21,060.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `23.38%` | `76.62%` | `0.31` | 160,340.00 USD |
| `1H` | `Aster` | `1.55%` | `98.45%` | `0.02` | 128,910.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `98.03%` | `1.97%` | `49.76` | 2,830.00 USD |
| `1H` | `Whale Positions` | `44.96%` | `55.04%` | `0.82` | 6,580,000.00 USD |
| `1H` | `Global Accounts` | `45.61%` | `54.39%` | `0.84` | 23,700,000.00 USD |
| `4H` | `DOT` | `45.37%` | `54.63%` | `0.83` | 88,860,000.00 USD |
| `4H` | `Binance` | `46.84%` | `53.16%` | `0.88` | 30,830,000.00 USD |
| `4H` | `OKX` | `50.8%` | `49.2%` | `1.03` | 5,390,000.00 USD |
| `4H` | `Bybit` | `48.93%` | `51.07%` | `0.96` | 4,640,000.00 USD |
| `4H` | `KuCoin` | `53.02%` | `46.98%` | `1.13` | 661,870.00 USD |
| `4H` | `Gate` | `45.85%` | `54.15%` | `0.85` | 1,980,000.00 USD |
| `4H` | `Bitget` | `47.18%` | `52.82%` | `0.89` | 1,760,000.00 USD |
| `4H` | `BingX` | `46.87%` | `53.13%` | `0.88` | 13,690,000.00 USD |
| `4H` | `MEXC` | `42.39%` | `57.61%` | `0.74` | 5,000,000.00 USD |
| `4H` | `Bitunix` | `53.49%` | `46.51%` | `1.15` | 3,290,000.00 USD |
| `4H` | `Hyperliquid` | `61.48%` | `38.52%` | `1.60` | 1,080,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.52%` | `49.48%` | `1.02` | 14,880,000.00 USD |
| `4H` | `Crypto.com` | `97.97%` | `2.03%` | `48.26` | 9,760.00 USD |
| `4H` | `WhiteBIT` | `0.2%` | `99.8%` | `0.00` | 5,090,000.00 USD |
| `4H` | `HTX` | `27.01%` | `72.99%` | `0.37` | 25,550.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `46.95%` | `53.05%` | `0.89` | 295,130.00 USD |
| `4H` | `Aster` | `60%` | `40%` | `1.50` | 85,880.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `54.52%` | `45.48%` | `1.20` | 154,680.00 USD |
| `4H` | `Whale Positions` | `46.84%` | `53.16%` | `0.88` | 30,830,000.00 USD |
| `4H` | `Global Accounts` | `45.37%` | `54.63%` | `0.83` | 88,860,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.01` | `1.01` | `1.01` | `1.01` | `1.00` | 469,322.85 USD | 154,724.12 USD | 314,598.73 USD | -159,874.62 USD | `-34.06%` | `11B / 34S` |
| `0:00 UTC` | `1.01` | `1.01` | `1.01` | `1.01` | `1.00` | 1,036,474.58 USD | 416,595.02 USD | 619,879.56 USD | -203,284.54 USD | `-19.61%` | `14B / 24S` |
| `5:00 UTC` | `1.02` | `1.02` | `1.02` | `1.02` | `1.01` | 1,420,574.95 USD | 1,000,262.40 USD | 420,312.55 USD | 579,949.86 USD | `+40.83%` | `13B / 20S` |
| `0:00 UTC` | `1.02` | `1.02` | `1.02` | `1.02` | `1.01` | 1,273,423.64 USD | 481,734.41 USD | 791,689.23 USD | -309,954.82 USD | `-24.34%` | `9B / 29S` |
| `5:00 UTC` | `1.01` | `1.01` | `1.01` | `1.01` | `1.01` | 657,161.08 USD | 244,063.77 USD | 413,097.31 USD | -169,033.55 USD | `-25.72%` | `3B / 15S` |
| `0:00 UTC` | `1.01` | `1.01` | `1.01` | `1.01` | `1.00` | 605,145.48 USD | 242,805.14 USD | 362,340.33 USD | -119,535.19 USD | `-19.75%` | `3B / 20S` |
| `5:00 UTC` | `1.01` | `1.01` | `1.01` | `1.01` | `1.00` | 367,151.31 USD | 115,663.71 USD | 251,487.60 USD | -135,823.89 USD | `-36.99%` | `2B / 13S` |
| `0:00 UTC` | `1.00` | `1.00` | `1.00` | `1.01` | `0.9990` | 615,154.97 USD | 223,058.23 USD | 392,096.73 USD | -169,038.50 USD | `-27.48%` | `6B / 35S` |
| `5:00 UTC` | `1.00` | `1.00` | `1.00` | `1.00` | `0.9973` | 953,336.44 USD | 578,861.35 USD | 374,475.09 USD | 204,386.27 USD | `+21.44%` | `11B / 7S` |
| `0:00 UTC` | `1.00` | `1.00` | `1.00` | `1.00` | `1.00` | 89,060.13 USD | 36,113.03 USD | 52,947.10 USD | -16,834.07 USD | `-18.90%` | `3B / 15S` |

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
| `5m` | 5,620.00 USD | 23,910.00 USD | **`ACCUMULATION`** |
| `15m` | 15,830.00 USD | 188,380.00 USD | **`ACCUMULATION`** |
| `30m` | 1,360.00 USD | -61,060.00 USD | **`DISTRIBUTION`** |
| `1h` | -13,390.00 USD | -496,870.00 USD | **`DISTRIBUTION`** |
| `2h` | -22,820.00 USD | -844,690.00 USD | **`DISTRIBUTION`** |
| `4h` | 1,000.00 USD | -1,130,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -35,440.00 USD | -1,180,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -185,770.00 USD | -1,400,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -50,320.00 USD | -864,410.00 USD | **`DISTRIBUTION`** |
| `24h` | -131,420.00 USD | -3,090,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,400,000.00 USD | -17,450,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,490,000.00 USD | -72,230,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+5.62K` | 15m=`+15.83K` | 1h=`-13.39K` | 24h=`-131.42K`
* Futures Capital Netflows: 5m=`+23.91K` | 15m=`+188.38K` | 1h=`-496.87K` | 24h=`-3.09M`
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
  * Execution Entry: `0.9530` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.9128` (Risk Distance: `0.0420` pts)
  * +2.5R Take Profit: `1.06`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9952` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.04` (Risk Distance: `0.0420` pts)
  * +2.5R Take Profit: `0.8902`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.01`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
