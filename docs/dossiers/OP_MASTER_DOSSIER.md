# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 10:25:43 IST` (`2026-10-30 04:55:43 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1100` | **Live Ask Quote**: `0.1100` | **Mid Price**: `0.1100`
- **Spread Points**: `0.000022` | **Spread BPS**: `2.00 bps` (Charter Threshold: `12.00 bps`)
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
  * Session VWAP: `0.1100` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1108` | Lower -3.00σ Band: `0.1092`
  * Upper +2.51σ Band: `0.1106` | Lower -2.51σ Band: `0.1094`
  * Upper +2.01σ Band: `0.1105` | Lower -2.01σ Band: `0.1095`
  * Upper +2.00σ Band: `0.1105` | Lower -2.00σ Band: `0.1096`
  * Upper +1.28σ Band: `0.1103` | Lower -1.28σ Band: `0.1097`
  * Upper +1.00σ Band: `0.1102` | Lower -1.00σ Band: `0.1098`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1100` | EMA-20=`0.1100` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1100` (Slope: `+0.0000`) | EMA-100=`0.1100`
  * Institutional Anchors: EMA-144=`0.1100` | EMA-200=`0.1100` (Slope: `+0.0000`) | EMA-233=`0.1100`
- **Range Boundaries**: 24H High=`0.1111` | 24H Low=`0.1089` | Weekly High=`0.1122` | Weekly Low=`0.1078`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1103` (Distance: `+0.00%`)
  * Point of Control (POC) = `0.1100` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `0.1097` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.1105` | POC=`0.1100` | VAL=`0.1096`
  * Prior Day Extremes: PDH=`0.1107` | PDL=`0.1094` | PDC=`0.1100`
  * Monday Range Blueprint: High=`0.1106` | Mid=`0.1100` | Low=`0.1095`
  * Developing Weekly Value Area: Weekly VAH=`0.1109` | Weekly POC=`0.1100` | Weekly VAL=`0.1091`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1102` | Low=`0.1098`
  * London Session (08:00-16:00 UTC): High=`0.1105` | Low=`0.1096`
  * New York Session (13:00-21:00 UTC): High=`0.1107` | Low=`0.1094`
  * Initial Balance (First Hour): IB High=`0.1103` | IB Low=`0.1097`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1096` - `0.1105`
  * Optimal Trade Entry (OTE 0.705): `0.1102`
  * Structural Invalidation Anchor (0.786): `0.1109`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1004` | `0.1007` | `0.1002` | `0.1006` | `1,182,620` | 118,825.88 USD | 24,350.12 USD | `+20.49%` | -2,002,524.51 USD | `+0.54` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.1006` | `0.1007` | `0.1003` | `0.1005` | `1,069,885` | 107,522.60 USD | 35,696.40 USD | `+33.20%` | -1,966,828.12 USD | `+0.68` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1005` | `0.1008` | `0.1004` | `0.1008` | `594,041` | 59,765.81 USD | 30,257.07 USD | `+50.63%` | -1,936,571.04 USD | `+0.57` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.0999` | `0.1004` | `0.0996` | `0.1004` | `3,605,793` | 360,867.60 USD | 125,818.48 USD | `+34.87%` | -2,063,321.31 USD | `+0.80` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1004` | `0.1009` | `0.1002` | `0.1008` | `3,198,294` | 321,574.58 USD | 96,000.52 USD | `+29.85%` | -1,967,320.79 USD | `+0.67` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1009` | `0.1013` | `0.1006` | `0.1013` | `4,052,381` | 409,127.59 USD | 80,087.68 USD | `+19.58%` | -1,887,233.11 USD | `+0.57` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.0975` | `0.0991` | `0.0965` | `0.0981` | `16,150,698` | 1,585,412.30 USD | 111,043.46 USD | `+7.00%` | -1,755,382.94 USD | `+0.44` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.0981` | `0.0995` | `0.0970` | `0.0993` | `30,519,947` | 2,992,768.64 USD | -441,148.19 USD | `-14.74%` | -2,196,531.13 USD | `-0.72` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.0993` | `0.1013` | `0.0988` | `0.1013` | `14,359,730` | 1,438,946.07 USD | 309,443.92 USD | `+21.50%` | -1,887,087.21 USD | `+0.92` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -1,009,359.71 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,347,386.10 USD | `-1.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1008` | `0.0988` | `0.1008` | `9,955,194` | 994,316.35 USD | 223,617.50 USD | `+22.49%` | -2,123,768.60 USD | `+0.82` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | 483,978.43 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | 307,838.15 USD | `-1.31` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -1,009,359.71 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,347,386.10 USD | `-1.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1013` | `0.0988` | `0.1013` | `14,358,290` | 1,438,800.16 USD | 309,298.02 USD | `+21.50%` | -2,038,088.08 USD | `+0.90` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| --- | **`0.1100`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:24:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1099` | 9,518.97 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 9.52K USD at 0.1099 USD [API] | `2026-10-29 01:52:47` |
| `ANNOUNCEMENT` | `INFO` | `0.1099` | 7,294.20 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 7.29K USD at 0.1099 USD [API] | `2026-10-29 01:52:47` |
| `ANNOUNCEMENT` | `INFO` | `0.1099` | 9,522.44 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 9.52K USD at 0.1099 USD [API] | `2026-10-29 01:52:47` |
| `ANNOUNCEMENT` | `INFO` | `0.1100` | 5,425.00 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 5.42K USD at 0.1100 USD [API] | `2026-10-29 01:52:47` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.1135` (Vol: 51,287.72 USD, Dist: `+1.67%`) | Long MP=`0.1090` (Vol: 46,178.28 USD, Dist: `--2.31%`)
  * 48H Horizon: Short MP=`0.1145` (Vol: 58,548.38 USD, Dist: `+2.57%`) | Long MP=`0.1081` (Vol: 88,789.99 USD, Dist: `--3.11%`)
  * 3D Horizon: Short MP=`0.1144` (Vol: 74,407.19 USD, Dist: `+2.52%`) | Long MP=`0.1080` (Vol: 74,547.74 USD, Dist: `--3.19%`)
  * 7D Horizon: Short MP=`0.1345` (Vol: 124,572.90 USD, Dist: `+21.07%`) | Long MP=`0.1086` (Vol: 138,703.74 USD, Dist: `--2.21%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `0.0827` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 8,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0830` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 28.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0860` | 1,820,000.00 USD | 1,820,000.00 USD | 1,880.00 USD | 0.00 USD | 2,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0863` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 1,880.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0866` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 1,980.00 USD | 15,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0869` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0871` | 1,510,000.00 USD | 1,510,000.00 USD | 1,740.00 USD | 353.10 USD | 1,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0872` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 1,200.00 USD | 5,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0873` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 680.22 USD | 5,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0875` | 1,500,000.00 USD | 1,500,000.00 USD | 9,010.00 USD | 437.13 USD | 3,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0875` | 1,780,000.00 USD | 1,780,000.00 USD | 6,010.00 USD | 0.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0877` | 1,490,000.00 USD | 1,490,000.00 USD | 4,660.00 USD | 3,520.00 USD | 5,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0878` | 1,770,000.00 USD | 1,770,000.00 USD | 9,200.00 USD | 7,660.00 USD | 28,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0879` | 1,480,000.00 USD | 1,480,000.00 USD | 2,950.00 USD | 2,000.00 USD | 9,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0881` | 1,460,000.00 USD | 1,460,000.00 USD | 1,670.00 USD | 1,920.00 USD | 531.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0881` | 1,720,000.00 USD | 1,720,000.00 USD | 9,390.00 USD | 2,660.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0883` | 1,460,000.00 USD | 1,460,000.00 USD | 2,370.00 USD | 4,960.00 USD | 9,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0884` | 1,700,000.00 USD | 1,700,000.00 USD | 7,040.00 USD | 8,030.00 USD | 21,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0885` | 1,440,000.00 USD | 1,440,000.00 USD | 4,650.00 USD | 1,040.00 USD | 4,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0887` | 1,430,000.00 USD | 1,430,000.00 USD | 2,910.00 USD | 1,540.00 USD | 8,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0887` | 1,660,000.00 USD | 1,660,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0889` | 1,420,000.00 USD | 1,420,000.00 USD | 727.20 USD | 1,680.00 USD | 2,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0890` | 1,620,000.00 USD | 1,620,000.00 USD | 14,610.00 USD | 5,880.00 USD | 13,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0891` | 1,410,000.00 USD | 1,410,000.00 USD | 755.35 USD | 1,580.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0893` | 1,410,000.00 USD | 1,410,000.00 USD | 983.61 USD | 0.00 USD | 543.57 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0893` | 1,590,000.00 USD | 1,590,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0895` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 1,080.00 USD | 16.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0896` | 1,570,000.00 USD | 1,570,000.00 USD | 5,760.00 USD | 2,110.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0897` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 1,330.00 USD | 4.58 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0899` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 37.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0899` | 1,560,000.00 USD | 1,560,000.00 USD | 3,390.00 USD | 927.82 USD | 4,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0901` | 1,400,000.00 USD | 1,400,000.00 USD | 3,320.00 USD | 1,000.00 USD | 25.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0902` | 1,550,000.00 USD | 1,550,000.00 USD | 2,270.00 USD | 910.78 USD | 1,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0903` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 3,440.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0905` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 486.35 USD | 2,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0905` | 1,540,000.00 USD | 1,540,000.00 USD | 10,350.00 USD | 996.61 USD | 4,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0907` | 1,390,000.00 USD | 1,390,000.00 USD | 1,250.00 USD | 245.42 USD | 2,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0908` | 1,530,000.00 USD | 1,530,000.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0909` | 1,390,000.00 USD | 1,390,000.00 USD | 938.76 USD | 1,360.00 USD | 784.66 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0911` | 1,380,000.00 USD | 1,380,000.00 USD | 5,580.00 USD | 1,450.00 USD | 72.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0911` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0913` | 1,380,000.00 USD | 1,380,000.00 USD | 1,930.00 USD | 465.26 USD | 782.37 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0914` | 1,510,000.00 USD | 1,510,000.00 USD | 1,670.00 USD | 903.90 USD | 45.81 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0915` | 1,370,000.00 USD | 1,370,000.00 USD | 6,590.00 USD | 2,510.00 USD | 77.39 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0917` | 1,370,000.00 USD | 1,370,000.00 USD | 3,850.00 USD | 3,470.00 USD | 46.08 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0917` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0919` | 1,360,000.00 USD | 1,360,000.00 USD | 4,980.00 USD | 504.78 USD | 19,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0920` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 223.39 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0921` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 750.63 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0923` | 1,330,000.00 USD | 1,330,000.00 USD | 1,410.00 USD | 1,920.00 USD | 22,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0923` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 4,940.00 USD | 43,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0925` | 1,300,000.00 USD | 1,300,000.00 USD | 3,270.00 USD | 3,340.00 USD | 26,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0926` | 1,450,000.00 USD | 1,450,000.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0929` | 1,270,000.00 USD | 1,270,000.00 USD | 4,360.00 USD | 1,190.00 USD | 6.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0929` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0931` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 7,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0932` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 12,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0933` | 1,260,000.00 USD | 1,260,000.00 USD | 16,500.00 USD | 0.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0935` | 1,230,000.00 USD | 1,230,000.00 USD | 8,990.00 USD | 7,300.00 USD | 15,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0935` | 1,430,000.00 USD | 1,430,000.00 USD | 19,560.00 USD | 8,160.00 USD | 31,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0937` | 1,200,000.00 USD | 1,200,000.00 USD | 4,580.00 USD | 6,660.00 USD | 13,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0938` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 248.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0939` | 1,170,000.00 USD | 1,170,000.00 USD | 3,590.00 USD | 2,140.00 USD | 44,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0941` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 9,410.00 USD | 21,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0941` | 1,370,000.00 USD | 1,370,000.00 USD | 16,100.00 USD | 18,340.00 USD | 90,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0943` | 1,090,000.00 USD | 1,090,000.00 USD | 3,500.00 USD | 10,920.00 USD | 30,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0944` | 1,240,000.00 USD | 1,240,000.00 USD | 8,040.00 USD | 2,010.00 USD | 37,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0945` | 1,050,000.00 USD | 1,050,000.00 USD | 15,750.00 USD | 6,510.00 USD | 44,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0947` | 981,970.00 USD | 981,970.00 USD | 0.00 USD | 962.66 USD | 25.67 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0947` | 1,200,000.00 USD | 1,200,000.00 USD | 2,200.00 USD | 1,810.00 USD | 112.06 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0949` | 980,980.00 USD | 980,980.00 USD | 12,180.00 USD | 5,770.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0950` | 1,190,000.00 USD | 1,190,000.00 USD | 3,770.00 USD | 9,700.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0951` | 959,940.00 USD | 959,940.00 USD | 0.00 USD | 2,030.00 USD | 19,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0953` | 937,950.00 USD | 937,950.00 USD | 33,000.00 USD | 4,360.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0953` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 8,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0955` | 893,900.00 USD | 893,900.00 USD | 17,990.00 USD | 14,600.00 USD | 31,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0956` | 1,140,000.00 USD | 1,140,000.00 USD | 39,120.00 USD | 13,670.00 USD | 51,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0957` | 829,940.00 USD | 829,940.00 USD | 16,340.00 USD | 6,740.00 USD | 48,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0959` | 758,200.00 USD | 758,200.00 USD | 0.00 USD | 3,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0959` | 1,040,000.00 USD | 1,040,000.00 USD | 28,110.00 USD | 0.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0961` | 755,100.00 USD | 755,100.00 USD | 8,920.00 USD | 23,950.00 USD | 23,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0962` | 990,700.00 USD | 990,700.00 USD | 12,340.00 USD | 16,920.00 USD | 94,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0963` | 699,050.00 USD | 699,050.00 USD | 23,240.00 USD | 11,750.00 USD | 11,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0965` | 652,080.00 USD | 652,080.00 USD | 8,250.00 USD | 5,890.00 USD | 20,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0965` | 866,470.00 USD | 866,470.00 USD | 0.00 USD | 6,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0967` | 617,550.00 USD | 617,550.00 USD | 0.00 USD | 1,960.00 USD | 786.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0968` | 860,060.00 USD | 860,060.00 USD | 7,490.00 USD | 0.00 USD | 58,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0969` | 614,800.00 USD | 614,800.00 USD | 6,930.00 USD | 7,530.00 USD | 8,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0971` | 592,210.00 USD | 592,210.00 USD | 0.00 USD | 4,070.00 USD | 10,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 793,650.00 USD | 793,650.00 USD | 0.00 USD | 7,090.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0973` | 577,880.00 USD | 577,880.00 USD | 0.00 USD | 8,710.00 USD | 149.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0974` | 781,550.00 USD | 781,550.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0975` | 569,020.00 USD | 569,020.00 USD | 0.00 USD | 0.00 USD | 19.74 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0977` | 569,000.00 USD | 569,000.00 USD | 0.00 USD | 0.00 USD | 136.85 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0979` | 568,860.00 USD | 568,860.00 USD | 0.00 USD | 0.00 USD | 21,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0981` | 547,740.00 USD | 547,740.00 USD | 3,830.00 USD | 5,020.00 USD | 5.60 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0983` | 538,890.00 USD | 538,890.00 USD | 0.00 USD | 4,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0986` | 765,240.00 USD | 765,240.00 USD | 0.00 USD | 12,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0987` | 534,850.00 USD | 534,850.00 USD | 22,740.00 USD | 3,920.00 USD | 11,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0989` | 496,400.00 USD | 496,400.00 USD | 2,180.00 USD | 1,540.00 USD | 21,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 752,930.00 USD | 752,930.00 USD | 17,640.00 USD | 7,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0991` | 471,090.00 USD | 471,090.00 USD | 64,250.00 USD | 0.00 USD | 773.63 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0992` | 727,460.00 USD | 727,460.00 USD | 27,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0993` | 406,060.00 USD | 406,060.00 USD | 21,070.00 USD | 0.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0995` | 343,460.00 USD | 343,460.00 USD | 17,890.00 USD | 898.20 USD | 50,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 700,320.00 USD | 700,320.00 USD | 63,330.00 USD | 0.00 USD | 76,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0997` | 274,430.00 USD | 274,430.00 USD | 17,900.00 USD | 5,840.00 USD | 53,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0998` | 560,950.00 USD | 560,950.00 USD | 28,450.00 USD | 17,040.00 USD | 135,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0999` | 197,030.00 USD | 197,030.00 USD | 0.00 USD | 10,180.00 USD | 47,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1001` | 138,980.00 USD | 138,980.00 USD | 0.00 USD | 0.00 USD | 42,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 380,190.00 USD | 380,190.00 USD | 76,560.00 USD | 25,570.00 USD | 107,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1003` | 96,470.00 USD | 96,470.00 USD | 23,240.00 USD | 0.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1004` | 170,080.00 USD | 170,080.00 USD | 22,470.00 USD | 0.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1005` | 46,000.00 USD | 46,000.00 USD | 8,250.00 USD | 5,890.00 USD | 20,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1007` | 11,380.00 USD | 11,380.00 USD | 4,360.00 USD | 0.00 USD | 49.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 124,180.00 USD | 124,180.00 USD | 20,870.00 USD | 3,080.00 USD | 100,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1009` | 6,980.00 USD | 6,980.00 USD | 6,930.00 USD | 0.00 USD | 46.40 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1010` | 85,040.00 USD | 85,040.00 USD | 17,340.00 USD | 13,670.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1010` | 170,080.00 USD | 170,080.00 USD | 17,340.00 USD | 13,670.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1011` | 36,340.00 USD | 36,340.00 USD | 16,500.00 USD | 4,070.00 USD | 15,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1013` | 77,150.00 USD | 77,150.00 USD | 8,990.00 USD | 16,010.00 USD | 15,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1013` | 258,730.00 USD | 258,730.00 USD | 34,830.00 USD | 28,370.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1015` | 96,210.00 USD | 96,210.00 USD | 4,580.00 USD | 1,220.00 USD | 13,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1016` | 274,320.00 USD | 274,320.00 USD | 15,440.00 USD | 0.00 USD | 142.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1017` | 115,840.00 USD | 115,840.00 USD | 3,590.00 USD | 4,930.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1019` | 125,270.00 USD | 125,270.00 USD | 0.00 USD | 9,410.00 USD | 25.31 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1019` | 329,540.00 USD | 329,540.00 USD | 26,150.00 USD | 8,460.00 USD | 20,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1021` | 164,860.00 USD | 164,860.00 USD | 13,630.00 USD | 12,100.00 USD | 13,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1022` | 395,350.00 USD | 395,350.00 USD | 18,100.00 USD | 10,260.00 USD | 37,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1023` | 210,790.00 USD | 210,790.00 USD | 15,750.00 USD | 10,470.00 USD | 19,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1025` | 215,490.00 USD | 215,490.00 USD | 3,740.00 USD | 962.66 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1025` | 401,690.00 USD | 401,690.00 USD | 1,550.00 USD | 4,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1027` | 233,130.00 USD | 233,130.00 USD | 3,430.00 USD | 3,920.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1028` | 433,570.00 USD | 433,570.00 USD | 3,800.00 USD | 4,390.00 USD | 23,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1029` | 254,900.00 USD | 254,900.00 USD | 6,870.00 USD | 7,400.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1031` | 312,490.00 USD | 312,490.00 USD | 27,910.00 USD | 5,770.00 USD | 23,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1031` | 462,940.00 USD | 462,940.00 USD | 19,560.00 USD | 9,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1033` | 342,080.00 USD | 342,080.00 USD | 0.00 USD | 7,720.00 USD | 21,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1034` | 497,150.00 USD | 497,150.00 USD | 18,920.00 USD | 15,180.00 USD | 106.77 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1035` | 368,390.00 USD | 368,390.00 USD | 15,150.00 USD | 11,130.00 USD | 23.79 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1037` | 417,640.00 USD | 417,640.00 USD | 36,550.00 USD | 12,700.00 USD | 0.40 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1037` | 510,680.00 USD | 510,680.00 USD | 2,710.00 USD | 10,710.00 USD | 108.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1039` | 437,850.00 USD | 437,850.00 USD | 6,500.00 USD | 8,500.00 USD | 5,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1040` | 558,270.00 USD | 558,270.00 USD | 5,940.00 USD | 10,300.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1041` | 485,880.00 USD | 485,880.00 USD | 11,520.00 USD | 16,860.00 USD | 19,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1043` | 523,010.00 USD | 523,010.00 USD | 0.00 USD | 12,950.00 USD | 24,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1043` | 580,220.00 USD | 580,220.00 USD | 15,960.00 USD | 5,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1045` | 532,110.00 USD | 532,110.00 USD | 1,870.00 USD | 2,240.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1046` | 652,580.00 USD | 652,580.00 USD | 0.00 USD | 12,200.00 USD | 60,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1047` | 606,030.00 USD | 606,030.00 USD | 28,580.00 USD | 8,010.00 USD | 37,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1049` | 723,850.00 USD | 723,850.00 USD | 33,450.00 USD | 15,310.00 USD | 69,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1049` | 777,080.00 USD | 777,080.00 USD | 34,790.00 USD | 6,530.00 USD | 83,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1051` | 788,810.00 USD | 788,810.00 USD | 30,370.00 USD | 10,280.00 USD | 24,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1052` | 954,920.00 USD | 954,920.00 USD | 28,200.00 USD | 24,160.00 USD | 125,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1053` | 890,590.00 USD | 890,590.00 USD | 35,030.00 USD | 10,620.00 USD | 56,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1055` | 1,020,000.00 USD | 1,020,000.00 USD | 51,530.00 USD | 26,280.00 USD | 55,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1055` | 1,330,000.00 USD | 1,330,000.00 USD | 122,840.00 USD | 44,430.00 USD | 211,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1057` | 1,080,000.00 USD | 1,080,000.00 USD | 14,080.00 USD | 11,900.00 USD | 32,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1058` | 1,700,000.00 USD | 1,700,000.00 USD | 105,620.00 USD | 58,510.00 USD | 202,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1059` | 1,200,000.00 USD | 1,200,000.00 USD | 35,730.00 USD | 4,960.00 USD | 77,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1061` | 1,290,000.00 USD | 1,290,000.00 USD | 30,060.00 USD | 1,890.00 USD | 60,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1061` | 1,960,000.00 USD | 1,960,000.00 USD | 75,540.00 USD | 69,160.00 USD | 118,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1063` | 1,380,000.00 USD | 1,380,000.00 USD | 25,200.00 USD | 2,030.00 USD | 65,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1064` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 52,580.00 USD | 177,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1065` | 1,410,000.00 USD | 1,410,000.00 USD | 1,740.00 USD | 2,630.00 USD | 24,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1067` | 1,470,000.00 USD | 1,470,000.00 USD | 8,230.00 USD | 1,320.00 USD | 44,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1067` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 51,740.00 USD | 143,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1069` | 1,550,000.00 USD | 1,550,000.00 USD | 14,770.00 USD | 5,440.00 USD | 62,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1070` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 57,770.00 USD | 134,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1071` | 1,580,000.00 USD | 1,580,000.00 USD | 2,550.00 USD | 5,850.00 USD | 20,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1073` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 3,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1073` | 2,620,000.00 USD | 2,620,000.00 USD | 7,820.00 USD | 20,440.00 USD | 10,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1075` | 1,590,000.00 USD | 1,590,000.00 USD | 1,440.00 USD | 857.82 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1076` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 22,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1077` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 619.42 USD | 20.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1079` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 4,300.00 USD | 21,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1079` | 2,660,000.00 USD | 2,660,000.00 USD | 5,620.00 USD | 3,380.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1081` | 1,620,000.00 USD | 1,620,000.00 USD | 4,650.00 USD | 732.74 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1082` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 89.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1083` | 1,650,000.00 USD | 1,650,000.00 USD | 9,160.00 USD | 6,710.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1085` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 385.06 USD | 65,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1085` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1087` | 1,790,000.00 USD | 1,790,000.00 USD | 28,490.00 USD | 2,510.00 USD | 44,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1088` | 2,680,000.00 USD | 2,680,000.00 USD | 5,290.00 USD | 1,420.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1089` | 1,830,000.00 USD | 1,830,000.00 USD | 29,650.00 USD | 1,580.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1091` | 1,860,000.00 USD | 1,860,000.00 USD | 33,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1091` | 2,700,000.00 USD | 2,700,000.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1093` | 1,880,000.00 USD | 1,880,000.00 USD | 15,480.00 USD | 1,080.00 USD | 96.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1094` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 1,500.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1095` | 1,900,000.00 USD | 1,900,000.00 USD | 4,110.00 USD | 1,890.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1097` | 1,940,000.00 USD | 1,940,000.00 USD | 7,260.00 USD | 2,530.00 USD | 22,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1097` | 2,730,000.00 USD | 2,730,000.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1099` | 1,950,000.00 USD | 1,950,000.00 USD | 6,130.00 USD | 1,940.00 USD | 7.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1100` | 2,770,000.00 USD | 2,770,000.00 USD | 11,470.00 USD | 0.00 USD | 21,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1101` | 1,960,000.00 USD | 1,960,000.00 USD | 5,570.00 USD | 3,820.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1103` | 1,970,000.00 USD | 1,970,000.00 USD | 3,540.00 USD | 6,900.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 2,810,000.00 USD | 2,810,000.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1105` | 1,990,000.00 USD | 1,990,000.00 USD | 3,380.00 USD | 4,740.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1106` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 22,880.00 USD | 16,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1107` | 2,040,000.00 USD | 2,040,000.00 USD | 3,110.00 USD | 13,200.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1109` | 2,050,000.00 USD | 2,050,000.00 USD | 2,110.00 USD | 1,370.00 USD | 2,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1111` | 2,050,000.00 USD | 2,050,000.00 USD | 5,200.00 USD | 996.46 USD | 5.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1112` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1113` | 2,110,000.00 USD | 2,110,000.00 USD | 21,390.00 USD | 5,880.00 USD | 29,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1115` | 2,120,000.00 USD | 2,120,000.00 USD | 6,690.00 USD | 465.26 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1118` | 2,950,000.00 USD | 2,950,000.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 3,010,000.00 USD | 3,010,000.00 USD | 17,760.00 USD | 0.00 USD | 38,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1124` | 3,110,000.00 USD | 3,110,000.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1127` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1130` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 24,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 3,190,000.00 USD | 3,190,000.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1136` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1139` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1142` | 3,230,000.00 USD | 3,230,000.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 3,470,000.00 USD | 3,470,000.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1148` | 3,650,000.00 USD | 3,650,000.00 USD | 9,880.00 USD | 0.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 3,920,000.00 USD | 3,920,000.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1154` | 4,400,000.00 USD | 4,400,000.00 USD | 243,190.00 USD | 26,970.00 USD | 202,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 4,690,000.00 USD | 4,690,000.00 USD | 173,120.00 USD | 25,290.00 USD | 98,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1160` | 4,970,000.00 USD | 4,970,000.00 USD | 131,160.00 USD | 32,830.00 USD | 109,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 5,250,000.00 USD | 5,250,000.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1166` | 5,470,000.00 USD | 5,470,000.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 5,700,000.00 USD | 5,700,000.00 USD | 82,770.00 USD | 26,150.00 USD | 117,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1172` | 5,820,000.00 USD | 5,820,000.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 6,000,000.00 USD | 6,000,000.00 USD | 75,590.00 USD | 17,930.00 USD | 81,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1178` | 6,170,000.00 USD | 6,170,000.00 USD | 89,510.00 USD | 25,350.00 USD | 60,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 6,260,000.00 USD | 6,260,000.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1184` | 6,330,000.00 USD | 6,330,000.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 6,410,000.00 USD | 6,410,000.00 USD | 5,620.00 USD | 17,120.00 USD | 59,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1190` | 6,550,000.00 USD | 6,550,000.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 6,630,000.00 USD | 6,630,000.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1196` | 6,690,000.00 USD | 6,690,000.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 6,780,000.00 USD | 6,780,000.00 USD | 9,100.00 USD | 13,190.00 USD | 68,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1202` | 6,980,000.00 USD | 6,980,000.00 USD | 138,430.00 USD | 21,430.00 USD | 32,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 7,180,000.00 USD | 7,180,000.00 USD | 117,120.00 USD | 48,510.00 USD | 40,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1208` | 7,280,000.00 USD | 7,280,000.00 USD | 39,480.00 USD | 20,870.00 USD | 39,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 7,460,000.00 USD | 7,460,000.00 USD | 72,500.00 USD | 25,920.00 USD | 76,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1214` | 7,580,000.00 USD | 7,580,000.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 7,630,000.00 USD | 7,630,000.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1220` | 7,720,000.00 USD | 7,720,000.00 USD | 34,050.00 USD | 6,400.00 USD | 54,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 7,860,000.00 USD | 7,860,000.00 USD | 76,930.00 USD | 15,050.00 USD | 45,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1226` | 7,930,000.00 USD | 7,930,000.00 USD | 45,920.00 USD | 19,760.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 8,060,000.00 USD | 8,060,000.00 USD | 63,930.00 USD | 33,570.00 USD | 28,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1232` | 8,160,000.00 USD | 8,160,000.00 USD | 51,420.00 USD | 12,080.00 USD | 37,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1235` | 8,190,000.00 USD | 8,190,000.00 USD | 15,040.00 USD | 5,390.00 USD | 16,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1237` | 8,200,000.00 USD | 8,200,000.00 USD | 4,080.00 USD | 2,760.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1805` | 18,490.00 USD | 18,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Short` | `0.1805` | 18,490.00 USD | 18,490.00 USD | 0.00 USD | `+82.49%` | `102,410.90` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0827` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 8,590.00 USD |
| `7D` | `0.0830` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 28.49 USD |
| `7D` | `0.0860` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 1,880.00 USD | 0.00 USD | 2,160.00 USD |
| `7D` | `0.0863` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 0.00 USD | 1,880.00 USD | 7,040.00 USD |
| `7D` | `0.0866` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 0.00 USD | 1,980.00 USD | 15,400.00 USD |
| `7D` | `0.0869` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 2,900.00 USD |
| `1D` | `0.0871` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 1,740.00 USD | 353.10 USD | 1,020.00 USD |
| `7D` | `0.0872` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 0.00 USD | 1,200.00 USD | 5,830.00 USD |
| `1D` | `0.0873` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 0.00 USD | 680.22 USD | 5,950.00 USD |
| `1D` | `0.0875` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 9,010.00 USD | 437.13 USD | 3,500.00 USD |
| `7D` | `0.0875` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 6,010.00 USD | 0.00 USD | 5,780.00 USD |
| `1D` | `0.0877` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 4,660.00 USD | 3,520.00 USD | 5,830.00 USD |
| `7D` | `0.0878` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 9,200.00 USD | 7,660.00 USD | 28,720.00 USD |
| `1D` | `0.0879` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 2,950.00 USD | 2,000.00 USD | 9,430.00 USD |
| `1D` | `0.0881` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 1,670.00 USD | 1,920.00 USD | 531.95 USD |
| `7D` | `0.0881` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 9,390.00 USD | 2,660.00 USD | 12,940.00 USD |
| `1D` | `0.0883` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 2,370.00 USD | 4,960.00 USD | 9,970.00 USD |
| `7D` | `0.0884` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 7,040.00 USD | 8,030.00 USD | 21,730.00 USD |
| `1D` | `0.0885` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 4,650.00 USD | 1,040.00 USD | 4,910.00 USD |
| `1D` | `0.0887` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 2,910.00 USD | 1,540.00 USD | 8,130.00 USD |
| `7D` | `0.0887` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD |
| `1D` | `0.0889` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 727.20 USD | 1,680.00 USD | 2,100.00 USD |
| `7D` | `0.0890` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 14,610.00 USD | 5,880.00 USD | 13,160.00 USD |
| `1D` | `0.0891` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 755.35 USD | 1,580.00 USD | 3,230.00 USD |
| `1D` | `0.0893` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 983.61 USD | 0.00 USD | 543.57 USD |
| `7D` | `0.0893` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD |
| `1D` | `0.0895` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | 1,080.00 USD | 16.60 USD |
| `7D` | `0.0896` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 5,760.00 USD | 2,110.00 USD | 6,870.00 USD |
| `1D` | `0.0897` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | 1,330.00 USD | 4.58 USD |
| `1D` | `0.0899` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 37.83 USD |
| `7D` | `0.0899` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 3,390.00 USD | 927.82 USD | 4,520.00 USD |
| `1D` | `0.0901` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 3,320.00 USD | 1,000.00 USD | 25.06 USD |
| `7D` | `0.0902` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 2,270.00 USD | 910.78 USD | 1,320.00 USD |
| `1D` | `0.0903` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | 3,440.00 USD | 2,240.00 USD |
| `1D` | `0.0905` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 0.00 USD | 486.35 USD | 2,130.00 USD |
| `7D` | `0.0905` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 10,350.00 USD | 996.61 USD | 4,170.00 USD |
| `1D` | `0.0907` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 1,250.00 USD | 245.42 USD | 2,710.00 USD |
| `7D` | `0.0908` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD |
| `1D` | `0.0909` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 938.76 USD | 1,360.00 USD | 784.66 USD |
| `1D` | `0.0911` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 5,580.00 USD | 1,450.00 USD | 72.76 USD |
| `7D` | `0.0911` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD |
| `1D` | `0.0913` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 1,930.00 USD | 465.26 USD | 782.37 USD |
| `7D` | `0.0914` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 1,670.00 USD | 903.90 USD | 45.81 USD |
| `1D` | `0.0915` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 6,590.00 USD | 2,510.00 USD | 77.39 USD |
| `1D` | `0.0917` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 3,850.00 USD | 3,470.00 USD | 46.08 USD |
| `7D` | `0.0917` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD |
| `1D` | `0.0919` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 4,980.00 USD | 504.78 USD | 19,100.00 USD |
| `7D` | `0.0920` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 223.39 USD |
| `1D` | `0.0921` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 0.00 USD | 750.63 USD | 3,750.00 USD |
| `1D` | `0.0923` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 1,410.00 USD | 1,920.00 USD | 22,020.00 USD |
| `7D` | `0.0923` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 0.00 USD | 4,940.00 USD | 43,850.00 USD |
| `1D` | `0.0925` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 3,270.00 USD | 3,340.00 USD | 26,460.00 USD |
| `7D` | `0.0926` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD |
| `1D` | `0.0929` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 4,360.00 USD | 1,190.00 USD | 6.87 USD |
| `7D` | `0.0929` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD |
| `1D` | `0.0931` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 7,430.00 USD |
| `7D` | `0.0932` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 12,290.00 USD |
| `1D` | `0.0933` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 16,500.00 USD | 0.00 USD | 10,200.00 USD |
| `1D` | `0.0935` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 8,990.00 USD | 7,300.00 USD | 15,700.00 USD |
| `7D` | `0.0935` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 19,560.00 USD | 8,160.00 USD | 31,940.00 USD |
| `1D` | `0.0937` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 4,580.00 USD | 6,660.00 USD | 13,240.00 USD |
| `7D` | `0.0938` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 248.29 USD |
| `1D` | `0.0939` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 3,590.00 USD | 2,140.00 USD | 44,280.00 USD |
| `1D` | `0.0941` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 9,410.00 USD | 21,130.00 USD |
| `7D` | `0.0941` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 16,100.00 USD | 18,340.00 USD | 90,220.00 USD |
| `1D` | `0.0943` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 3,500.00 USD | 10,920.00 USD | 30,430.00 USD |
| `7D` | `0.0944` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 8,040.00 USD | 2,010.00 USD | 37,480.00 USD |
| `1D` | `0.0945` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 15,750.00 USD | 6,510.00 USD | 44,350.00 USD |
| `1D` | `0.0947` | 981,970.00 USD | 0.00 USD | 981,970.00 USD | 0.00 USD | 962.66 USD | 25.67 USD |
| `7D` | `0.0947` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 2,200.00 USD | 1,810.00 USD | 112.06 USD |
| `1D` | `0.0949` | 980,980.00 USD | 0.00 USD | 980,980.00 USD | 12,180.00 USD | 5,770.00 USD | 3,090.00 USD |
| `7D` | `0.0950` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 3,770.00 USD | 9,700.00 USD | 26,990.00 USD |
| `1D` | `0.0951` | 959,940.00 USD | 0.00 USD | 959,940.00 USD | 0.00 USD | 2,030.00 USD | 19,960.00 USD |
| `1D` | `0.0953` | 937,950.00 USD | 0.00 USD | 937,950.00 USD | 33,000.00 USD | 4,360.00 USD | 6,690.00 USD |
| `7D` | `0.0953` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 0.00 USD | 8,150.00 USD | 0.00 USD |
| `1D` | `0.0955` | 893,900.00 USD | 0.00 USD | 893,900.00 USD | 17,990.00 USD | 14,600.00 USD | 31,370.00 USD |
| `7D` | `0.0956` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 39,120.00 USD | 13,670.00 USD | 51,090.00 USD |
| `1D` | `0.0957` | 829,940.00 USD | 0.00 USD | 829,940.00 USD | 16,340.00 USD | 6,740.00 USD | 48,660.00 USD |
| `1D` | `0.0959` | 758,200.00 USD | 0.00 USD | 758,200.00 USD | 0.00 USD | 3,100.00 USD | 0.00 USD |
| `7D` | `0.0959` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 28,110.00 USD | 0.00 USD | 21,370.00 USD |
| `1D` | `0.0961` | 755,100.00 USD | 0.00 USD | 755,100.00 USD | 8,920.00 USD | 23,950.00 USD | 23,180.00 USD |
| `7D` | `0.0962` | 990,700.00 USD | 0.00 USD | 990,700.00 USD | 12,340.00 USD | 16,920.00 USD | 94,970.00 USD |
| `1D` | `0.0963` | 699,050.00 USD | 0.00 USD | 699,050.00 USD | 23,240.00 USD | 11,750.00 USD | 11,980.00 USD |
| `1D` | `0.0965` | 652,080.00 USD | 0.00 USD | 652,080.00 USD | 8,250.00 USD | 5,890.00 USD | 20,390.00 USD |
| `7D` | `0.0965` | 866,470.00 USD | 0.00 USD | 866,470.00 USD | 0.00 USD | 6,410.00 USD | 0.00 USD |
| `1D` | `0.0967` | 617,550.00 USD | 0.00 USD | 617,550.00 USD | 0.00 USD | 1,960.00 USD | 786.39 USD |
| `7D` | `0.0968` | 860,060.00 USD | 0.00 USD | 860,060.00 USD | 7,490.00 USD | 0.00 USD | 58,910.00 USD |
| `1D` | `0.0969` | 614,800.00 USD | 0.00 USD | 614,800.00 USD | 6,930.00 USD | 7,530.00 USD | 8,130.00 USD |
| `1D` | `0.0971` | 592,210.00 USD | 0.00 USD | 592,210.00 USD | 0.00 USD | 4,070.00 USD | 10,260.00 USD |
| `7D` | `0.0971` | 793,650.00 USD | 0.00 USD | 793,650.00 USD | 0.00 USD | 7,090.00 USD | 5,010.00 USD |
| `1D` | `0.0973` | 577,880.00 USD | 0.00 USD | 577,880.00 USD | 0.00 USD | 8,710.00 USD | 149.69 USD |
| `7D` | `0.0974` | 781,550.00 USD | 0.00 USD | 781,550.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD |
| `1D` | `0.0975` | 569,020.00 USD | 0.00 USD | 569,020.00 USD | 0.00 USD | 0.00 USD | 19.74 USD |
| `1D` | `0.0977` | 569,000.00 USD | 0.00 USD | 569,000.00 USD | 0.00 USD | 0.00 USD | 136.85 USD |
| `1D` | `0.0979` | 568,860.00 USD | 0.00 USD | 568,860.00 USD | 0.00 USD | 0.00 USD | 21,120.00 USD |
| `1D` | `0.0981` | 547,740.00 USD | 0.00 USD | 547,740.00 USD | 3,830.00 USD | 5,020.00 USD | 5.60 USD |
| `1D` | `0.0983` | 538,890.00 USD | 0.00 USD | 538,890.00 USD | 0.00 USD | 4,040.00 USD | 0.00 USD |
| `7D` | `0.0986` | 765,240.00 USD | 0.00 USD | 765,240.00 USD | 0.00 USD | 12,320.00 USD | 0.00 USD |
| `1D` | `0.0987` | 534,850.00 USD | 0.00 USD | 534,850.00 USD | 22,740.00 USD | 3,920.00 USD | 11,800.00 USD |
| `1D` | `0.0989` | 496,400.00 USD | 0.00 USD | 496,400.00 USD | 2,180.00 USD | 1,540.00 USD | 21,580.00 USD |
| `7D` | `0.0989` | 752,930.00 USD | 0.00 USD | 752,930.00 USD | 17,640.00 USD | 7,820.00 USD | 0.00 USD |
| `1D` | `0.0991` | 471,090.00 USD | 0.00 USD | 471,090.00 USD | 64,250.00 USD | 0.00 USD | 773.63 USD |
| `7D` | `0.0992` | 727,460.00 USD | 0.00 USD | 727,460.00 USD | 27,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0993` | 406,060.00 USD | 0.00 USD | 406,060.00 USD | 21,070.00 USD | 0.00 USD | 41,540.00 USD |
| `1D` | `0.0995` | 343,460.00 USD | 0.00 USD | 343,460.00 USD | 17,890.00 USD | 898.20 USD | 50,230.00 USD |
| `7D` | `0.0995` | 700,320.00 USD | 0.00 USD | 700,320.00 USD | 63,330.00 USD | 0.00 USD | 76,030.00 USD |
| `1D` | `0.0997` | 274,430.00 USD | 0.00 USD | 274,430.00 USD | 17,900.00 USD | 5,840.00 USD | 53,670.00 USD |
| `7D` | `0.0998` | 560,950.00 USD | 0.00 USD | 560,950.00 USD | 28,450.00 USD | 17,040.00 USD | 135,270.00 USD |
| `1D` | `0.0999` | 197,030.00 USD | 0.00 USD | 197,030.00 USD | 0.00 USD | 10,180.00 USD | 47,870.00 USD |
| `1D` | `0.1001` | 138,980.00 USD | 0.00 USD | 138,980.00 USD | 0.00 USD | 0.00 USD | 42,510.00 USD |
| `7D` | `0.1001` | 380,190.00 USD | 0.00 USD | 380,190.00 USD | 76,560.00 USD | 25,570.00 USD | 107,970.00 USD |
| `1D` | `0.1003` | 96,470.00 USD | 0.00 USD | 96,470.00 USD | 23,240.00 USD | 0.00 USD | 27,230.00 USD |
| `7D` | `0.1004` | 170,080.00 USD | 0.00 USD | 170,080.00 USD | 22,470.00 USD | 0.00 USD | 23,430.00 USD |
| `1D` | `0.1005` | 46,000.00 USD | 0.00 USD | 46,000.00 USD | 8,250.00 USD | 5,890.00 USD | 20,470.00 USD |
| `1D` | `0.1007` | 11,380.00 USD | 0.00 USD | 11,380.00 USD | 4,360.00 USD | 0.00 USD | 49.14 USD |
| `7D` | `0.1007` | 124,180.00 USD | 0.00 USD | 124,180.00 USD | 20,870.00 USD | 3,080.00 USD | 100,230.00 USD |
| `1D` | `0.1009` | 6,980.00 USD | 0.00 USD | 6,980.00 USD | 6,930.00 USD | 0.00 USD | 46.40 USD |
| `1D` | `0.1010` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1010` | 85,040.00 USD | 85,040.00 USD | 0.00 USD | 17,340.00 USD | 13,670.00 USD | 54,030.00 USD |
| `7D` | `0.1010` | 170,080.00 USD | 170,080.00 USD | 0.00 USD | 17,340.00 USD | 13,670.00 USD | 54,030.00 USD |
| `1D` | `0.1011` | 36,340.00 USD | 36,340.00 USD | 0.00 USD | 16,500.00 USD | 4,070.00 USD | 15,770.00 USD |
| `1D` | `0.1013` | 77,150.00 USD | 77,150.00 USD | 0.00 USD | 8,990.00 USD | 16,010.00 USD | 15,800.00 USD |
| `7D` | `0.1013` | 258,730.00 USD | 258,730.00 USD | 0.00 USD | 34,830.00 USD | 28,370.00 USD | 25,450.00 USD |
| `1D` | `0.1015` | 96,210.00 USD | 96,210.00 USD | 0.00 USD | 4,580.00 USD | 1,220.00 USD | 13,250.00 USD |
| `7D` | `0.1016` | 274,320.00 USD | 274,320.00 USD | 0.00 USD | 15,440.00 USD | 0.00 USD | 142.43 USD |
| `1D` | `0.1017` | 115,840.00 USD | 115,840.00 USD | 0.00 USD | 3,590.00 USD | 4,930.00 USD | 11,110.00 USD |
| `1D` | `0.1019` | 125,270.00 USD | 125,270.00 USD | 0.00 USD | 0.00 USD | 9,410.00 USD | 25.31 USD |
| `7D` | `0.1019` | 329,540.00 USD | 329,540.00 USD | 0.00 USD | 26,150.00 USD | 8,460.00 USD | 20,610.00 USD |
| `1D` | `0.1021` | 164,860.00 USD | 164,860.00 USD | 0.00 USD | 13,630.00 USD | 12,100.00 USD | 13,850.00 USD |
| `7D` | `0.1022` | 395,350.00 USD | 395,350.00 USD | 0.00 USD | 18,100.00 USD | 10,260.00 USD | 37,440.00 USD |
| `1D` | `0.1023` | 210,790.00 USD | 210,790.00 USD | 0.00 USD | 15,750.00 USD | 10,470.00 USD | 19,720.00 USD |
| `1D` | `0.1025` | 215,490.00 USD | 215,490.00 USD | 0.00 USD | 3,740.00 USD | 962.66 USD | 0.00 USD |
| `7D` | `0.1025` | 401,690.00 USD | 401,690.00 USD | 0.00 USD | 1,550.00 USD | 4,790.00 USD | 0.00 USD |
| `1D` | `0.1027` | 233,130.00 USD | 233,130.00 USD | 0.00 USD | 3,430.00 USD | 3,920.00 USD | 10,290.00 USD |
| `7D` | `0.1028` | 433,570.00 USD | 433,570.00 USD | 0.00 USD | 3,800.00 USD | 4,390.00 USD | 23,700.00 USD |
| `1D` | `0.1029` | 254,900.00 USD | 254,900.00 USD | 0.00 USD | 6,870.00 USD | 7,400.00 USD | 7,510.00 USD |
| `1D` | `0.1031` | 312,490.00 USD | 312,490.00 USD | 0.00 USD | 27,910.00 USD | 5,770.00 USD | 23,910.00 USD |
| `7D` | `0.1031` | 462,940.00 USD | 462,940.00 USD | 0.00 USD | 19,560.00 USD | 9,810.00 USD | 0.00 USD |
| `1D` | `0.1033` | 342,080.00 USD | 342,080.00 USD | 0.00 USD | 0.00 USD | 7,720.00 USD | 21,870.00 USD |
| `7D` | `0.1034` | 497,150.00 USD | 497,150.00 USD | 0.00 USD | 18,920.00 USD | 15,180.00 USD | 106.77 USD |
| `1D` | `0.1035` | 368,390.00 USD | 368,390.00 USD | 0.00 USD | 15,150.00 USD | 11,130.00 USD | 23.79 USD |
| `1D` | `0.1037` | 417,640.00 USD | 417,640.00 USD | 0.00 USD | 36,550.00 USD | 12,700.00 USD | 0.40 USD |
| `7D` | `0.1037` | 510,680.00 USD | 510,680.00 USD | 0.00 USD | 2,710.00 USD | 10,710.00 USD | 108.00 USD |
| `1D` | `0.1039` | 437,850.00 USD | 437,850.00 USD | 0.00 USD | 6,500.00 USD | 8,500.00 USD | 5,220.00 USD |
| `7D` | `0.1040` | 558,270.00 USD | 558,270.00 USD | 0.00 USD | 5,940.00 USD | 10,300.00 USD | 31,350.00 USD |
| `1D` | `0.1041` | 485,880.00 USD | 485,880.00 USD | 0.00 USD | 11,520.00 USD | 16,860.00 USD | 19,650.00 USD |
| `1D` | `0.1043` | 523,010.00 USD | 523,010.00 USD | 0.00 USD | 0.00 USD | 12,950.00 USD | 24,170.00 USD |
| `7D` | `0.1043` | 580,220.00 USD | 580,220.00 USD | 0.00 USD | 15,960.00 USD | 5,980.00 USD | 0.00 USD |
| `1D` | `0.1045` | 532,110.00 USD | 532,110.00 USD | 0.00 USD | 1,870.00 USD | 2,240.00 USD | 4,990.00 USD |
| `7D` | `0.1046` | 652,580.00 USD | 652,580.00 USD | 0.00 USD | 0.00 USD | 12,200.00 USD | 60,160.00 USD |
| `1D` | `0.1047` | 606,030.00 USD | 606,030.00 USD | 0.00 USD | 28,580.00 USD | 8,010.00 USD | 37,340.00 USD |
| `1D` | `0.1049` | 723,850.00 USD | 723,850.00 USD | 0.00 USD | 33,450.00 USD | 15,310.00 USD | 69,050.00 USD |
| `7D` | `0.1049` | 777,080.00 USD | 777,080.00 USD | 0.00 USD | 34,790.00 USD | 6,530.00 USD | 83,180.00 USD |
| `1D` | `0.1051` | 788,810.00 USD | 788,810.00 USD | 0.00 USD | 30,370.00 USD | 10,280.00 USD | 24,320.00 USD |
| `7D` | `0.1052` | 954,920.00 USD | 954,920.00 USD | 0.00 USD | 28,200.00 USD | 24,160.00 USD | 125,480.00 USD |
| `1D` | `0.1053` | 890,590.00 USD | 890,590.00 USD | 0.00 USD | 35,030.00 USD | 10,620.00 USD | 56,130.00 USD |
| `1D` | `0.1055` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 51,530.00 USD | 26,280.00 USD | 55,540.00 USD |
| `7D` | `0.1055` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 122,840.00 USD | 44,430.00 USD | 211,630.00 USD |
| `1D` | `0.1057` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 14,080.00 USD | 11,900.00 USD | 32,140.00 USD |
| `7D` | `0.1058` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 105,620.00 USD | 58,510.00 USD | 202,430.00 USD |
| `1D` | `0.1059` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 35,730.00 USD | 4,960.00 USD | 77,030.00 USD |
| `1D` | `0.1061` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 30,060.00 USD | 1,890.00 USD | 60,470.00 USD |
| `7D` | `0.1061` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 75,540.00 USD | 69,160.00 USD | 118,330.00 USD |
| `1D` | `0.1063` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 25,200.00 USD | 2,030.00 USD | 65,270.00 USD |
| `7D` | `0.1064` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 52,580.00 USD | 177,550.00 USD |
| `1D` | `0.1065` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 1,740.00 USD | 2,630.00 USD | 24,840.00 USD |
| `1D` | `0.1067` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 8,230.00 USD | 1,320.00 USD | 44,330.00 USD |
| `7D` | `0.1067` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 51,740.00 USD | 143,940.00 USD |
| `1D` | `0.1069` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 14,770.00 USD | 5,440.00 USD | 62,880.00 USD |
| `7D` | `0.1070` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 57,770.00 USD | 134,670.00 USD |
| `1D` | `0.1071` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 2,550.00 USD | 5,850.00 USD | 20,410.00 USD |
| `1D` | `0.1073` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,980.00 USD |
| `7D` | `0.1073` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 7,820.00 USD | 20,440.00 USD | 10,320.00 USD |
| `1D` | `0.1075` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 1,440.00 USD | 857.82 USD | 3,810.00 USD |
| `7D` | `0.1076` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,500.00 USD |
| `1D` | `0.1077` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 619.42 USD | 20.10 USD |
| `1D` | `0.1079` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 4,300.00 USD | 21,990.00 USD |
| `7D` | `0.1079` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 5,620.00 USD | 3,380.00 USD | 9,940.00 USD |
| `1D` | `0.1081` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 4,650.00 USD | 732.74 USD | 2,430.00 USD |
| `7D` | `0.1082` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 89.24 USD |
| `1D` | `0.1083` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 9,160.00 USD | 6,710.00 USD | 10,700.00 USD |
| `1D` | `0.1085` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 385.06 USD | 65,180.00 USD |
| `7D` | `0.1085` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1087` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 28,490.00 USD | 2,510.00 USD | 44,670.00 USD |
| `7D` | `0.1088` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 5,290.00 USD | 1,420.00 USD | 9,590.00 USD |
| `1D` | `0.1089` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 29,650.00 USD | 1,580.00 USD | 3,210.00 USD |
| `1D` | `0.1091` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 33,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1091` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD |
| `1D` | `0.1093` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 15,480.00 USD | 1,080.00 USD | 96.91 USD |
| `7D` | `0.1094` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 1,500.00 USD | 8,730.00 USD |
| `1D` | `0.1095` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 21,520.00 USD |
| `1D` | `0.1097` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 7,260.00 USD | 2,530.00 USD | 22,890.00 USD |
| `7D` | `0.1097` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1099` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 6,130.00 USD | 1,940.00 USD | 7.36 USD |
| `7D` | `0.1100` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 21,880.00 USD |
| `1D` | `0.1101` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 5,570.00 USD | 3,820.00 USD | 4,290.00 USD |
| `1D` | `0.1103` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 3,540.00 USD | 6,900.00 USD | 1,170.00 USD |
| `7D` | `0.1103` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1105` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 3,380.00 USD | 4,740.00 USD | 10,700.00 USD |
| `7D` | `0.1106` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 22,880.00 USD | 16,130.00 USD |
| `1D` | `0.1107` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 3,110.00 USD | 13,200.00 USD | 35,750.00 USD |
| `1D` | `0.1109` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 2,110.00 USD | 1,370.00 USD | 2,670.00 USD |
| `7D` | `0.1109` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD |
| `1D` | `0.1111` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 5,200.00 USD | 996.46 USD | 5.91 USD |
| `7D` | `0.1112` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD |
| `1D` | `0.1113` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 21,390.00 USD | 5,880.00 USD | 29,980.00 USD |
| `1D` | `0.1115` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 6,690.00 USD | 465.26 USD | 0.00 USD |
| `7D` | `0.1118` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD |
| `7D` | `0.1121` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 17,760.00 USD | 0.00 USD | 38,370.00 USD |
| `7D` | `0.1124` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD |
| `7D` | `0.1127` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD |
| `7D` | `0.1130` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,260.00 USD |
| `7D` | `0.1133` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD |
| `7D` | `0.1136` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD |
| `7D` | `0.1139` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD |
| `7D` | `0.1142` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD |
| `7D` | `0.1145` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD |
| `7D` | `0.1148` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 175,990.00 USD |
| `7D` | `0.1151` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD |
| `7D` | `0.1154` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 243,190.00 USD | 26,970.00 USD | 202,050.00 USD |
| `7D` | `0.1157` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 173,120.00 USD | 25,290.00 USD | 98,310.00 USD |
| `7D` | `0.1160` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 131,160.00 USD | 32,830.00 USD | 109,320.00 USD |
| `7D` | `0.1163` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD |
| `7D` | `0.1166` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD |
| `7D` | `0.1169` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 82,770.00 USD | 26,150.00 USD | 117,900.00 USD |
| `7D` | `0.1172` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD |
| `7D` | `0.1175` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 75,590.00 USD | 17,930.00 USD | 81,630.00 USD |
| `7D` | `0.1178` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 89,510.00 USD | 25,350.00 USD | 60,700.00 USD |
| `7D` | `0.1181` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD |
| `7D` | `0.1184` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD |
| `7D` | `0.1187` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 5,620.00 USD | 17,120.00 USD | 59,700.00 USD |
| `7D` | `0.1190` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD |
| `7D` | `0.1193` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD |
| `7D` | `0.1196` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD |
| `7D` | `0.1199` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 9,100.00 USD | 13,190.00 USD | 68,000.00 USD |
| `7D` | `0.1202` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 138,430.00 USD | 21,430.00 USD | 32,790.00 USD |
| `7D` | `0.1205` | 7,180,000.00 USD | 7,180,000.00 USD | 0.00 USD | 117,120.00 USD | 48,510.00 USD | 40,590.00 USD |
| `7D` | `0.1208` | 7,280,000.00 USD | 7,280,000.00 USD | 0.00 USD | 39,480.00 USD | 20,870.00 USD | 39,590.00 USD |
| `7D` | `0.1211` | 7,460,000.00 USD | 7,460,000.00 USD | 0.00 USD | 72,500.00 USD | 25,920.00 USD | 76,780.00 USD |
| `7D` | `0.1214` | 7,580,000.00 USD | 7,580,000.00 USD | 0.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD |
| `7D` | `0.1217` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD |
| `7D` | `0.1220` | 7,720,000.00 USD | 7,720,000.00 USD | 0.00 USD | 34,050.00 USD | 6,400.00 USD | 54,700.00 USD |
| `7D` | `0.1223` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 76,930.00 USD | 15,050.00 USD | 45,660.00 USD |
| `7D` | `0.1226` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 45,920.00 USD | 19,760.00 USD | 5,210.00 USD |
| `7D` | `0.1229` | 8,060,000.00 USD | 8,060,000.00 USD | 0.00 USD | 63,930.00 USD | 33,570.00 USD | 28,680.00 USD |
| `7D` | `0.1232` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 51,420.00 USD | 12,080.00 USD | 37,580.00 USD |
| `7D` | `0.1235` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 15,040.00 USD | 5,390.00 USD | 16,760.00 USD |
| `7D` | `0.1237` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 4,080.00 USD | 2,760.00 USD | 2,800.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `63.35M` | Total OI Tokens: `628,842,810.9 OP`
  * 1h OI Change: `+1.43%` | 4h OI Change: `+4.99%` | 24h OI Change: `-12.25%`
  * Exchange Breakdown: Binance=`13.69M` | Bybit=`12.84M` | OKX=`3.72M` | Hyperliquid=`3.08M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-2.49K` | Last 24h: `-2.42K` | Last 3d: `-6.63K` | Last 7d: `-14.48K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0302%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0302%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0053%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `47.80%` | `52.20%` | `0.92` | 11,520,000.00 USD |
| `15M` | `Binance` | `46%` | `54%` | `0.85` | 4,770,000.00 USD |
| `15M` | `OKX` | `43.23%` | `56.77%` | `0.76` | 1,550,000.00 USD |
| `15M` | `Bybit` | `57%` | `43%` | `1.33` | 1,450,000.00 USD |
| `15M` | `KuCoin` | `49.75%` | `50.25%` | `0.99` | 87,090.00 USD |
| `15M` | `Gate` | `50.15%` | `49.85%` | `1.01` | 447,940.00 USD |
| `15M` | `Bitget` | `45.58%` | `54.42%` | `0.84` | 382,170.00 USD |
| `15M` | `BingX` | `57.16%` | `42.84%` | `1.33` | 717,620.00 USD |
| `15M` | `MEXC` | `37.31%` | `62.69%` | `0.60` | 464,890.00 USD |
| `15M` | `Bitunix` | `49.69%` | `50.31%` | `0.99` | 231,690.00 USD |
| `15M` | `Hyperliquid` | `85.29%` | `14.71%` | `5.80` | 809,430.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.59%` | `50.41%` | `0.98` | 126,840.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 731.38 USD |
| `15M` | `WhiteBIT` | `29.55%` | `70.45%` | `0.42` | 228,160.00 USD |
| `15M` | `HTX` | `42.7%` | `57.3%` | `0.75` | 994.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `10.24%` | `89.76%` | `0.11` | 2,920.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `15.55%` | `84.45%` | `0.18` | 244,930.00 USD |
| `15M` | `Whale Positions` | `46%` | `54%` | `0.85` | 4,770,000.00 USD |
| `15M` | `Global Accounts` | `47.80%` | `52.20%` | `0.92` | 11,520,000.00 USD |
| `1H` | `OP` | `47.48%` | `52.52%` | `0.90` | 4,570,000.00 USD |
| `1H` | `Binance` | `51.38%` | `48.62%` | `1.06` | 1,440,000.00 USD |
| `1H` | `OKX` | `49.65%` | `50.35%` | `0.99` | 443,710.00 USD |
| `1H` | `Bybit` | `46.31%` | `53.69%` | `0.86` | 514,530.00 USD |
| `1H` | `KuCoin` | `49.9%` | `50.1%` | `1.00` | 461,460.00 USD |
| `1H` | `Gate` | `40.6%` | `59.4%` | `0.68` | 107,870.00 USD |
| `1H` | `Bitget` | `40.82%` | `59.18%` | `0.69` | 459,220.00 USD |
| `1H` | `BingX` | `40.75%` | `59.25%` | `0.69` | 535,280.00 USD |
| `1H` | `MEXC` | `53.77%` | `46.23%` | `1.16` | 228,590.00 USD |
| `1H` | `Bitunix` | `38.57%` | `61.43%` | `0.63` | 61,370.00 USD |
| `1H` | `Hyperliquid` | `83.6%` | `16.4%` | `5.10` | 62,200.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.23%` | `49.77%` | `1.01` | 158,110.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `16.81%` | `83.19%` | `0.20` | 60,620.00 USD |
| `1H` | `HTX` | `30.28%` | `69.72%` | `0.43` | 2,330.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `11.04%` | `88.96%` | `0.12` | 30,530.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `5.86%` | `94.14%` | `0.06` | 6,180.00 USD |
| `1H` | `Whale Positions` | `51.38%` | `48.62%` | `1.06` | 1,440,000.00 USD |
| `1H` | `Global Accounts` | `47.48%` | `52.52%` | `0.90` | 4,570,000.00 USD |
| `4H` | `OP` | `47.92%` | `52.08%` | `0.92` | 21,580,000.00 USD |
| `4H` | `Binance` | `54.05%` | `45.95%` | `1.18` | 8,070,000.00 USD |
| `4H` | `OKX` | `53.21%` | `46.79%` | `1.14` | 2,300,000.00 USD |
| `4H` | `Bybit` | `55.35%` | `44.65%` | `1.24` | 2,460,000.00 USD |
| `4H` | `KuCoin` | `50.09%` | `49.91%` | `1.00` | 1,690,000.00 USD |
| `4H` | `Gate` | `51.33%` | `48.67%` | `1.05` | 703,140.00 USD |
| `4H` | `Bitget` | `49.36%` | `50.64%` | `0.97` | 997,260.00 USD |
| `4H` | `BingX` | `17.97%` | `82.03%` | `0.22` | 2,670,000.00 USD |
| `4H` | `MEXC` | `49.39%` | `50.61%` | `0.98` | 820,080.00 USD |
| `4H` | `Bitunix` | `44.51%` | `55.49%` | `0.80` | 400,300.00 USD |
| `4H` | `Hyperliquid` | `54.03%` | `45.97%` | `1.18` | 286,080.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.8%` | `50.2%` | `0.99` | 764,430.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `19.78%` | `80.22%` | `0.25` | 290,180.00 USD |
| `4H` | `HTX` | `27.16%` | `72.84%` | `0.37` | 13,080.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `40.52%` | `59.48%` | `0.68` | 46,180.00 USD |
| `4H` | `Aster` | `28.6%` | `71.4%` | `0.40` | 51,060.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `23.1%` | `76.9%` | `0.30` | 25,450.00 USD |
| `4H` | `Whale Positions` | `54.05%` | `45.95%` | `1.18` | 8,070,000.00 USD |
| `4H` | `Global Accounts` | `47.92%` | `52.08%` | `0.92` | 21,580,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.0989` | `0.0989` | `0.0989` | `0.0991` | `0.0985` | 342,650.41 USD | 155,489.22 USD | 187,161.19 USD | -31,671.96 USD | `-9.24%` | `4B / 6S` |
| `5:00 UTC` | `0.0981` | `0.0982` | `0.0981` | `0.0988` | `0.0980` | 282,587.21 USD | 127,716.82 USD | 154,870.40 USD | -27,153.58 USD | `-9.61%` | `10B / 27S` |
| `0:00 UTC` | `0.0985` | `0.0980` | `0.0985` | `0.0986` | `0.0972` | 782,641.49 USD | 272,807.16 USD | 509,834.33 USD | -237,027.16 USD | `-30.29%` | `4B / 30S` |
| `5:00 UTC` | `0.0976` | `0.0974` | `0.0976` | `0.0979` | `0.0970` | 1,011,824.45 USD | 364,728.70 USD | 647,095.75 USD | -282,367.05 USD | `-27.91%` | `6B / 15S` |
| `0:00 UTC` | `0.0984` | `0.0984` | `0.0984` | `0.0992` | `0.0978` | 803,922.63 USD | 438,559.35 USD | 365,363.29 USD | 73,196.06 USD | `+9.10%` | `32B / 10S` |
| `5:00 UTC` | `0.0992` | `0.0992` | `0.0992` | `0.0995` | `0.0989` | 394,380.07 USD | 199,715.01 USD | 194,665.06 USD | 5,049.95 USD | `+1.28%` | `10B / 6S` |
| `0:00 UTC` | `0.0989` | `0.0992` | `0.0989` | `0.0999` | `0.0988` | 347,230.40 USD | 177,310.87 USD | 169,919.53 USD | 7,391.34 USD | `+2.13%` | `21B / 7S` |
| `5:00 UTC` | `0.1001` | `0.1001` | `0.1001` | `0.1004` | `0.0996` | 360,867.60 USD | 243,343.04 USD | 117,524.56 USD | 125,818.48 USD | `+34.87%` | `30B / 1S` |
| `0:00 UTC` | `0.1005` | `0.1006` | `0.1005` | `0.1009` | `0.1002` | 321,574.58 USD | 208,787.55 USD | 112,787.03 USD | 96,000.52 USD | `+29.85%` | `23B / 4S` |
| `5:00 UTC` | `0.1009` | `0.1009` | `0.1009` | `0.1011` | `0.1006` | 323,044.64 USD | 177,388.62 USD | 145,656.02 USD | 31,732.61 USD | `+9.82%` | `12B / 8S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 19:54` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1097` | 0.00 USD | 0.00 USD |
| `10-28 19:54` | `Range 0.0005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1090` | 1,600,000.00 USD | 0.00 USD |
| `10-28 19:54` | `Range 0.0005` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.1090` | 1,600,000.00 USD | 0.00 USD |
| `10-28 19:52` | `Volume 5.0M OP` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1097` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Volume 5.0M OP` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1090` | 1,600,000.00 USD | 0.00 USD |
| `10-28 19:52` | `Volume 5.0M OP` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.1090` | 1,600,000.00 USD | 0.00 USD |
| `10-28 19:01` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1110` | 0.00 USD | 0.00 USD |
| `10-28 18:47` | `Volume 5.0M OP` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1104` | 0.00 USD | 0.00 USD |
| `10-28 18:47` | `Volume 5.0M OP` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.1100` | 1,300,000.00 USD | 0.00 USD |
| `10-28 18:42` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1107` | 0.00 USD | 0.00 USD |
| `10-28 18:42` | `Range 0.0005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1100` | 1,800,000.00 USD | 0.00 USD |
| `10-28 18:42` | `Range 0.0005` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.1100` | 1,800,000.00 USD | 0.00 USD |
| `10-28 17:08` | `Volume 5.0M OP` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1130` | 1,300,000.00 USD | 0.00 USD |
| `10-28 17:04` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1130` | 997,000.00 USD | 0.00 USD |
| `10-28 16:37` | `Volume 5.0M OP` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1122` | 834,000.00 USD | 0.00 USD |
| `10-28 15:12` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1130` | 1,100,000.00 USD | 0.00 USD |
| `10-28 15:02` | `Volume 5.0M OP` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1124` | 1,000,000.00 USD | 0.00 USD |
| `10-28 14:46` | `Range 0.0005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1124` | 980,000.00 USD | 0.00 USD |
| `10-28 14:28` | `Range 0.0005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1121` | 618,000.00 USD | 0.00 USD |
| `10-28 13:35` | `Volume 5.0M OP` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1121` | 1,200,000.00 USD | 0.00 USD |
| `10-28 13:33` | `Range 0.0005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1121` | 1,200,000.00 USD | 0.00 USD |
| `10-28 12:02` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1126` | 635,000.00 USD | 0.00 USD |
| `10-28 08:31` | `Volume 5.0M OP` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1128` | 1,200,000.00 USD | 0.00 USD |
| `10-28 08:30` | `Range 0.0005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1128` | 1,200,000.00 USD | 0.00 USD |
| `10-28 07:47` | `Volume 5.0M OP` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1136` | 995,000.00 USD | 0.00 USD |
| `10-28 07:30` | `Volume 5.0M OP` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1133` | 0.00 USD | 0.00 USD |
| `10-28 07:26` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1133` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 10,030.00 USD | 50,220.00 USD | **`ACCUMULATION`** |
| `15m` | 26,060.00 USD | 62,430.00 USD | **`ACCUMULATION`** |
| `30m` | 104,120.00 USD | 178,690.00 USD | **`ACCUMULATION`** |
| `1h` | 212,010.00 USD | 201,600.00 USD | **`ACCUMULATION`** |
| `2h` | -86,190.00 USD | -371,680.00 USD | **`DISTRIBUTION`** |
| `4h` | -89,290.00 USD | 94,710.00 USD | **`ACCUMULATION`** |
| `6h` | -21,130.00 USD | -1,970,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 492,700.00 USD | -4,710,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 24,490.00 USD | -4,930,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 314,030.00 USD | -3,890,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -71,230.00 USD | -14,800,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,340,000.00 USD | -83,250,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+10.03K` | 15m=`+26.06K` | 1h=`+212.01K` | 24h=`+314.03K`
* Futures Capital Netflows: 5m=`+50.22K` | 15m=`+62.43K` | 1h=`+201.60K` | 24h=`-3.89M`
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
  * `2026-10-30 09:51:07 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:19:07 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1097` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-1.09` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.11`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1103` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.31` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.89`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1109`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
