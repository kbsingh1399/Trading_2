# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 16:33:46 IST` (`2026-10-30 11:03:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1040` | `0.1041` | `0.1036` | `0.1040` | `767,788` | 79,760.54 USD | -20,570.47 USD | `-25.79%` | -2,039,932.88 USD | `-0.64` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1040` | `0.1041` | `0.1038` | `0.1039` | `547,191` | 56,888.77 USD | 17,742.64 USD | `+31.19%` | -2,022,190.24 USD | `+0.76` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1039` | `0.1043` | `0.1038` | `0.1043` | `297,525` | 30,960.39 USD | 14,779.42 USD | `+47.74%` | -2,007,410.82 USD | `+0.56` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1032` | `0.1041` | `0.1032` | `0.1040` | `2,532,549` | 262,943.08 USD | -17,690.08 USD | `-6.73%` | -1,951,640.84 USD | `-0.71` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1040` | `0.1049` | `0.1038` | `0.1048` | `2,143,056` | 223,592.72 USD | 31,969.77 USD | `+14.30%` | -1,919,671.07 USD | `+0.65` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1048` | `0.1050` | `0.1047` | `0.1048` | `480,836` | 50,399.86 USD | 5,553.03 USD | `+11.02%` | -1,914,118.04 USD | `+0.01` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1024` | `0.1034` | `0.1019` | `0.1034` | `10,854,845` | 1,111,003.69 USD | -28,977.96 USD | `-2.61%` | -1,820,323.01 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1034` | `0.1049` | `0.1028` | `0.1048` | `11,125,022` | 1,152,363.79 USD | -8,063.78 USD | `-0.70%` | -1,828,386.79 USD | `+0.22` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1048` | `0.1050` | `0.1047` | `0.1048` | `477,516` | 50,051.88 USD | 5,856.61 USD | `+11.70%` | -1,822,530.18 USD | `+0.25` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,490,108.93 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1040` | `0.0988` | `0.1027` | `54,609,324` | 5,566,939.91 USD | 608,714.61 USD | `+10.93%` | -1,881,394.33 USD | `+1.21` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1027` | `0.1042` | `0.1019` | `0.1042` | `31,415,684` | 3,231,492.88 USD | 53,306.02 USD | `+1.65%` | -1,828,088.31 USD | `+0.47` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | 165,115.32 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -1,152,082.54 USD | `-1.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,490,108.93 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1040` | `0.0988` | `0.1027` | `54,609,324` | 5,566,939.91 USD | 608,714.61 USD | `+10.93%` | -1,881,394.33 USD | `+1.21` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1027` | `0.1050` | `0.1019` | `0.1048` | `33,197,404` | 3,417,901.62 USD | 58,560.57 USD | `+1.71%` | -1,822,833.75 USD | `+0.47` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:32:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1116` | 5,736.99 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale BUY: 5.74K USD at 0.1116 USD [API] | `2026-10-29 14:17:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1116` | 10,125.16 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale BUY: 10.13K USD at 0.1116 USD [API] | `2026-10-29 14:17:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1116` | 5,737.00 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale BUY: 5.74K USD at 0.1116 USD [API] | `2026-10-29 14:17:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1069` | 9,691.60 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 9.69K USD at 0.1069 USD [API] | `2026-10-29 20:33:52` |


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
| `Live` | `Long Liquidation` | `0.0285` | 171.00 USD | 122,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0305` | 1,320.00 USD | 122,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 247.30 USD | 121,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 433.00 USD | 120,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 844.12 USD | 120,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 4,220.00 USD | 119,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 315.09 USD | 115,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 353.81 USD | 115,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 518.48 USD | 114,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 1,920.00 USD | 114,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 1,090.00 USD | 112,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 40,420.00 USD | 111,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 23,910.00 USD | 70,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,530.00 USD | 46,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,300.00 USD | 44,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 12,440.00 USD | 42,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 1,170.00 USD | 29,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 878.62 USD | 28,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 339.50 USD | 27,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 2,710.00 USD | 27,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 223.98 USD | 24,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 1,560.00 USD | 24,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 140.74 USD | 22,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 14,300.00 USD | 22,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 1,710.00 USD | 8,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0862` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 1,880.00 USD | 4,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0864` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 1,980.00 USD | 15,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0865` | 318.30 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0866` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 2,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0868` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0870` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0872` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 1,200.00 USD | 2,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0874` | 2,580,000.00 USD | 2,580,000.00 USD | 6,010.00 USD | 0.00 USD | 4,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0875` | 793.17 USD | 6,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0876` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 1,770.00 USD | 4,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0878` | 2,560,000.00 USD | 2,560,000.00 USD | 9,200.00 USD | 5,890.00 USD | 25,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0880` | 2,520,000.00 USD | 2,520,000.00 USD | 3,770.00 USD | 2,200.00 USD | 11,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0882` | 2,510,000.00 USD | 2,510,000.00 USD | 12,660.00 USD | 7,260.00 USD | 9,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0884` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 1,220.00 USD | 13,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0886` | 2,460,000.00 USD | 2,460,000.00 USD | 9,350.00 USD | 2,470.00 USD | 11,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0888` | 2,440,000.00 USD | 2,440,000.00 USD | 3,370.00 USD | 2,720.00 USD | 8,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0890` | 2,430,000.00 USD | 2,430,000.00 USD | 13,510.00 USD | 3,610.00 USD | 13,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0892` | 2,390,000.00 USD | 2,390,000.00 USD | 3,620.00 USD | 3,060.00 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0894` | 2,390,000.00 USD | 2,390,000.00 USD | 5,480.00 USD | 3,400.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,270.00 USD | 5,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0896` | 2,370,000.00 USD | 2,370,000.00 USD | 4,300.00 USD | 0.00 USD | 4,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0898` | 2,360,000.00 USD | 2,360,000.00 USD | 3,390.00 USD | 927.82 USD | 4,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0900` | 2,350,000.00 USD | 2,350,000.00 USD | 1,250.00 USD | 428.11 USD | 251.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0902` | 2,350,000.00 USD | 2,350,000.00 USD | 1,030.00 USD | 482.67 USD | 1,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0904` | 2,350,000.00 USD | 2,350,000.00 USD | 5,730.00 USD | 996.61 USD | 1,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0905` | 2,230.00 USD | 2,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0906` | 2,340,000.00 USD | 2,340,000.00 USD | 6,040.00 USD | 1,900.00 USD | 4,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0908` | 2,330,000.00 USD | 2,330,000.00 USD | 2,540.00 USD | 2,570.00 USD | 1,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0910` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 606.54 USD | 27.47 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0912` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0914` | 2,320,000.00 USD | 2,320,000.00 USD | 1,670.00 USD | 903.90 USD | 108.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0916` | 2,220,000.00 USD | 2,220,000.00 USD | 6,590.00 USD | 2,510.00 USD | 244.54 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0916` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 6,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0918` | 2,210,000.00 USD | 2,210,000.00 USD | 6,400.00 USD | 4,060.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0918` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0920` | 2,200,000.00 USD | 2,200,000.00 USD | 6,400.00 USD | 1,320.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0920` | 2,310,000.00 USD | 2,310,000.00 USD | 7,440.00 USD | 2,030.00 USD | 58.40 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0922` | 2,170,000.00 USD | 2,170,000.00 USD | 2,430.00 USD | 4,100.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0922` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 7,660.00 USD | 34,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0924` | 2,150,000.00 USD | 2,150,000.00 USD | 4,790.00 USD | 4,700.00 USD | 43,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0924` | 2,250,000.00 USD | 2,250,000.00 USD | 1,790.00 USD | 2,020.00 USD | 11,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0926` | 2,100,000.00 USD | 2,100,000.00 USD | 5,130.00 USD | 4,460.00 USD | 555.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0926` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0928` | 2,090,000.00 USD | 2,090,000.00 USD | 2,600.00 USD | 1,100.00 USD | 1,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0928` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0930` | 2,080,000.00 USD | 2,080,000.00 USD | 7,300.00 USD | 2,440.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0930` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 5,320.00 USD | 56.98 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0932` | 2,060,000.00 USD | 2,060,000.00 USD | 2,710.00 USD | 1,300.00 USD | 5,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0932` | 2,220,000.00 USD | 2,220,000.00 USD | 2,220.00 USD | 0.00 USD | 12,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0934` | 2,050,000.00 USD | 2,050,000.00 USD | 22,030.00 USD | 3,830.00 USD | 17,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0934` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 5.32 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0936` | 2,010,000.00 USD | 2,010,000.00 USD | 7,080.00 USD | 9,360.00 USD | 16,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0936` | 2,210,000.00 USD | 2,210,000.00 USD | 19,560.00 USD | 6,840.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0938` | 1,980,000.00 USD | 1,980,000.00 USD | 8,170.00 USD | 2,920.00 USD | 46,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0938` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 113.42 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0940` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0940` | 2,160,000.00 USD | 2,160,000.00 USD | 14,050.00 USD | 0.00 USD | 10,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0942` | 1,920,000.00 USD | 1,920,000.00 USD | 3,500.00 USD | 16,110.00 USD | 49,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0942` | 2,130,000.00 USD | 2,130,000.00 USD | 6,170.00 USD | 18,340.00 USD | 114,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0944` | 1,850,000.00 USD | 1,850,000.00 USD | 11,620.00 USD | 4,860.00 USD | 36,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0944` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 2,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0946` | 1,790,000.00 USD | 1,790,000.00 USD | 4,130.00 USD | 5,280.00 USD | 10,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0946` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 1,810.00 USD | 62.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0948` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 1,100.00 USD | 101.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0948` | 1,990,000.00 USD | 1,990,000.00 USD | 3,770.00 USD | 0.00 USD | 26,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0950` | 1,770,000.00 USD | 1,770,000.00 USD | 12,180.00 USD | 6,710.00 USD | 22,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0950` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 9,700.00 USD | 64.98 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0952` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 853.02 USD | 6,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0952` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 4,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0954` | 1,720,000.00 USD | 1,720,000.00 USD | 41,470.00 USD | 11,160.00 USD | 21,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0954` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 3,740.00 USD | 147.58 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0956` | 1,650,000.00 USD | 1,650,000.00 USD | 18,680.00 USD | 9,390.00 USD | 37,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0956` | 1,940,000.00 USD | 1,940,000.00 USD | 39,120.00 USD | 13,670.00 USD | 51,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0958` | 1,590,000.00 USD | 1,590,000.00 USD | 7,180.00 USD | 4,290.00 USD | 22,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0958` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0960` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 16,940.00 USD | 146.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0960` | 1,820,000.00 USD | 1,820,000.00 USD | 28,110.00 USD | 16,920.00 USD | 19,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0962` | 1,540,000.00 USD | 1,540,000.00 USD | 8,920.00 USD | 15,440.00 USD | 27,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0962` | 1,750,000.00 USD | 1,750,000.00 USD | 12,340.00 USD | 0.00 USD | 74,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0964` | 1,480,000.00 USD | 1,480,000.00 USD | 31,490.00 USD | 10,380.00 USD | 27,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0964` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 4,020.00 USD | 83.82 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0966` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 3,880.00 USD | 815.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0966` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 2,390.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0968` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 2,960.00 USD | 2,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0968` | 1,650,000.00 USD | 1,650,000.00 USD | 7,490.00 USD | 0.00 USD | 56,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0970` | 1,400,000.00 USD | 1,400,000.00 USD | 8,360.00 USD | 8,640.00 USD | 16,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0970` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 7,090.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0972` | 1,370,000.00 USD | 1,370,000.00 USD | 2,860.00 USD | 3,220.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0972` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 8,830.00 USD | 104.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0974` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 7,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0974` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 7,480.00 USD | 87.10 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0976` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 765.93 USD | 1,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0976` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 73.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0978` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 817.22 USD | 67.90 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0980` | 1,350,000.00 USD | 1,350,000.00 USD | 12,700.00 USD | 4,570.00 USD | 21,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0980` | 1,560,000.00 USD | 1,560,000.00 USD | 22,280.00 USD | 0.00 USD | 75.46 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0982` | 1,310,000.00 USD | 1,310,000.00 USD | 10,790.00 USD | 7,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0982` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 5,070.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0984` | 1,300,000.00 USD | 1,300,000.00 USD | 10,310.00 USD | 19,740.00 USD | 15,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0984` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 16,160.00 USD | 126.67 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0986` | 1,250,000.00 USD | 1,250,000.00 USD | 7,260.00 USD | 8,960.00 USD | 11,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0986` | 1,510,000.00 USD | 1,510,000.00 USD | 5,330.00 USD | 16,520.00 USD | 6,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0988` | 1,220,000.00 USD | 1,220,000.00 USD | 30,450.00 USD | 7,150.00 USD | 33,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0988` | 1,480,000.00 USD | 1,480,000.00 USD | 10,360.00 USD | 7,820.00 USD | 90.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0990` | 1,150,000.00 USD | 1,150,000.00 USD | 12,880.00 USD | 4,730.00 USD | 4,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0990` | 1,460,000.00 USD | 1,460,000.00 USD | 30,090.00 USD | 6,660.00 USD | 122.11 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0992` | 1,130,000.00 USD | 1,130,000.00 USD | 84,750.00 USD | 7,620.00 USD | 30,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0992` | 1,420,000.00 USD | 1,420,000.00 USD | 12,790.00 USD | 11,440.00 USD | 221.55 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0994` | 1,010,000.00 USD | 1,010,000.00 USD | 32,970.00 USD | 3,250.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0994` | 1,400,000.00 USD | 1,400,000.00 USD | 55,790.00 USD | 0.00 USD | 65,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0996` | 949,120.00 USD | 949,120.00 USD | 15,040.00 USD | 2,450.00 USD | 74,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0996` | 1,280,000.00 USD | 1,280,000.00 USD | 27,010.00 USD | 5,500.00 USD | 33,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0998` | 856,740.00 USD | 856,740.00 USD | 12,990.00 USD | 5,820.00 USD | 57,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0998` | 1,210,000.00 USD | 1,210,000.00 USD | 21,180.00 USD | 11,540.00 USD | 113,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1000` | 780,140.00 USD | 780,140.00 USD | 10,360.00 USD | 16,010.00 USD | 35,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1000` | 1,060,000.00 USD | 1,060,000.00 USD | 54,220.00 USD | 25,020.00 USD | 33,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1002` | 718,310.00 USD | 718,310.00 USD | 17,830.00 USD | 4,080.00 USD | 42,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1002` | 952,660.00 USD | 952,660.00 USD | 70,060.00 USD | 10,690.00 USD | 74,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1004` | 653,480.00 USD | 653,480.00 USD | 53,750.00 USD | 30,530.00 USD | 48,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1004` | 797,020.00 USD | 797,020.00 USD | 19,310.00 USD | 17,550.00 USD | 46,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1006` | 520,710.00 USD | 520,710.00 USD | 24,030.00 USD | 23,800.00 USD | 29,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1006` | 714,030.00 USD | 714,030.00 USD | 23,200.00 USD | 23,170.00 USD | 67,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1008` | 443,070.00 USD | 443,070.00 USD | 17,840.00 USD | 11,220.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1008` | 600,530.00 USD | 600,530.00 USD | 13,040.00 USD | 5,470.00 USD | 96,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1010` | 410,240.00 USD | 410,240.00 USD | 23,240.00 USD | 13,530.00 USD | 23,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1010` | 485,500.00 USD | 485,500.00 USD | 29,550.00 USD | 24,610.00 USD | 3,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1012` | 349,730.00 USD | 349,730.00 USD | 16,360.00 USD | 9,190.00 USD | 19,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1012` | 427,350.00 USD | 427,350.00 USD | 6,490.00 USD | 35,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1014` | 304,640.00 USD | 304,640.00 USD | 13,540.00 USD | 6,940.00 USD | 16,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1014` | 385,190.00 USD | 385,190.00 USD | 40,860.00 USD | 15,590.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1016` | 267,170.00 USD | 267,170.00 USD | 8,170.00 USD | 775.38 USD | 23,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1016` | 303,290.00 USD | 303,290.00 USD | 14,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1018` | 235,070.00 USD | 235,070.00 USD | 18,090.00 USD | 1,550.00 USD | 3,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1018` | 289,290.00 USD | 289,290.00 USD | 39,450.00 USD | 0.00 USD | 10,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1020` | 212,010.00 USD | 212,010.00 USD | 0.00 USD | 0.00 USD | 11,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1020` | 239,210.00 USD | 239,210.00 USD | 0.00 USD | 8,460.00 USD | 47,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1022` | 200,430.00 USD | 200,430.00 USD | 0.00 USD | 0.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1026` | 194,400.00 USD | 194,400.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1032` | 183,320.00 USD | 183,320.00 USD | 13,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1034` | 170,140.00 USD | 170,140.00 USD | 0.00 USD | 0.00 USD | 52.59 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1036` | 192,760.00 USD | 192,760.00 USD | 2,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1036` | 170,090.00 USD | 170,090.00 USD | 0.00 USD | 0.00 USD | 283.46 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1038` | 190,600.00 USD | 190,600.00 USD | 0.00 USD | 14,190.00 USD | 24.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1038` | 169,800.00 USD | 169,800.00 USD | 0.00 USD | 10,870.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1040` | 176,390.00 USD | 176,390.00 USD | 0.00 USD | 19,120.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1040` | 127,260.00 USD | 127,260.00 USD | 0.00 USD | 5,130.00 USD | 199.67 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1042` | 142,120.00 USD | 142,120.00 USD | 22,890.00 USD | 9,410.00 USD | 25,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1042` | 121,930.00 USD | 121,930.00 USD | 49,380.00 USD | 12,190.00 USD | 537.52 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1044` | 84,060.00 USD | 84,060.00 USD | 24,130.00 USD | 36,390.00 USD | 23,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1044` | 59,820.00 USD | 59,820.00 USD | 11,140.00 USD | 25,310.00 USD | 23,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1046` | 43,560.00 USD | 43,560.00 USD | 16,570.00 USD | 0.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1046` | 84,090.00 USD | 84,090.00 USD | 0.00 USD | 23,140.00 USD | 60,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1046` | 168,180.00 USD | 168,180.00 USD | 0.00 USD | 23,140.00 USD | 60,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1048` | 183,450.00 USD | 183,450.00 USD | 36,040.00 USD | 17,510.00 USD | 86,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1048` | 256,680.00 USD | 256,680.00 USD | 30,640.00 USD | 14,940.00 USD | 42,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1050` | 242,160.00 USD | 242,160.00 USD | 32,940.00 USD | 21,980.00 USD | 3,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1050` | 348,230.00 USD | 348,230.00 USD | 27,290.00 USD | 0.00 USD | 64,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1052` | 327,390.00 USD | 327,390.00 USD | 39,930.00 USD | 15,010.00 USD | 30,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1052` | 519,670.00 USD | 519,670.00 USD | 32,640.00 USD | 34,840.00 USD | 103,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1054` | 449,300.00 USD | 449,300.00 USD | 45,620.00 USD | 18,770.00 USD | 57,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1054` | 751,050.00 USD | 751,050.00 USD | 85,290.00 USD | 53,700.00 USD | 92,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1056` | 526,940.00 USD | 526,940.00 USD | 25,800.00 USD | 23,260.00 USD | 28,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1056` | 1,060,000.00 USD | 1,060,000.00 USD | 87,170.00 USD | 47,540.00 USD | 174,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1058` | 626,240.00 USD | 626,240.00 USD | 25,860.00 USD | 6,490.00 USD | 66,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1058` | 1,280,000.00 USD | 1,280,000.00 USD | 54,790.00 USD | 24,600.00 USD | 136,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1060` | 700,410.00 USD | 700,410.00 USD | 44,720.00 USD | 2,700.00 USD | 26,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1060` | 1,460,000.00 USD | 1,460,000.00 USD | 55,680.00 USD | 51,150.00 USD | 79,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1062` | 800,560.00 USD | 800,560.00 USD | 44,570.00 USD | 4,130.00 USD | 51,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1062` | 1,620,000.00 USD | 1,620,000.00 USD | 46,950.00 USD | 28,310.00 USD | 82,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1064` | 844,040.00 USD | 844,040.00 USD | 6,960.00 USD | 7,730.00 USD | 28,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1064` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 44,270.00 USD | 144,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1066` | 917,810.00 USD | 917,810.00 USD | 15,590.00 USD | 15,700.00 USD | 42,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1066` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 42,670.00 USD | 107,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1068` | 988,760.00 USD | 988,760.00 USD | 11,970.00 USD | 9,310.00 USD | 49,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1068` | 2,090,000.00 USD | 2,090,000.00 USD | 5,330.00 USD | 41,360.00 USD | 80,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1070` | 1,040,000.00 USD | 1,040,000.00 USD | 23,200.00 USD | 11,060.00 USD | 17,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1070` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 45,840.00 USD | 98,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1072` | 1,060,000.00 USD | 1,060,000.00 USD | 9,010.00 USD | 6,120.00 USD | 4,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1072` | 2,270,000.00 USD | 2,270,000.00 USD | 16,280.00 USD | 9,400.00 USD | 10,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1074` | 1,080,000.00 USD | 1,080,000.00 USD | 8,180.00 USD | 4,590.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1074` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 29,150.00 USD | 104.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1076` | 1,100,000.00 USD | 1,100,000.00 USD | 8,210.00 USD | 4,100.00 USD | 5,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1076` | 2,320,000.00 USD | 2,320,000.00 USD | 5,540.00 USD | 0.00 USD | 22,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1078` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 3,440.00 USD | 22,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1078` | 2,330,000.00 USD | 2,330,000.00 USD | 5,620.00 USD | 3,380.00 USD | 73.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1080` | 1,140,000.00 USD | 1,140,000.00 USD | 3,230.00 USD | 1,480.00 USD | 6,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1080` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 9,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1082` | 1,160,000.00 USD | 1,160,000.00 USD | 11,630.00 USD | 7,440.00 USD | 5,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1082` | 2,350,000.00 USD | 2,350,000.00 USD | 6,650.00 USD | 0.00 USD | 138.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1084` | 1,210,000.00 USD | 1,210,000.00 USD | 7,990.00 USD | 385.06 USD | 35,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1084` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 89.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1086` | 1,260,000.00 USD | 1,260,000.00 USD | 4,220.00 USD | 2,240.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1086` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 258.30 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1088` | 1,310,000.00 USD | 1,310,000.00 USD | 40,240.00 USD | 1,860.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1088` | 2,370,000.00 USD | 2,370,000.00 USD | 5,290.00 USD | 1,420.00 USD | 9,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1090` | 1,360,000.00 USD | 1,360,000.00 USD | 39,470.00 USD | 813.86 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1090` | 2,380,000.00 USD | 2,380,000.00 USD | 16,310.00 USD | 0.00 USD | 78.56 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1092` | 1,370,000.00 USD | 1,370,000.00 USD | 10,290.00 USD | 1,080.00 USD | 79.59 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1092` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 1,500.00 USD | 17,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1094` | 1,400,000.00 USD | 1,400,000.00 USD | 13,100.00 USD | 0.00 USD | 14,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1094` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 184.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1096` | 1,410,000.00 USD | 1,410,000.00 USD | 4,110.00 USD | 1,890.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1096` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 162.67 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1098` | 1,450,000.00 USD | 1,450,000.00 USD | 13,380.00 USD | 4,460.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1098` | 2,440,000.00 USD | 2,440,000.00 USD | 18,600.00 USD | 0.00 USD | 21,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1100` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 3,310.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1100` | 2,460,000.00 USD | 2,460,000.00 USD | 11,470.00 USD | 0.00 USD | 109.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1102` | 1,460,000.00 USD | 1,460,000.00 USD | 5,570.00 USD | 509.08 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1102` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 23,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1104` | 1,480,000.00 USD | 1,480,000.00 USD | 6,920.00 USD | 11,640.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1104` | 2,500,000.00 USD | 2,500,000.00 USD | 17,490.00 USD | 4,450.00 USD | 34.51 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1106` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 12,720.00 USD | 30,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1106` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 18,420.00 USD | 16,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1108` | 1,550,000.00 USD | 1,550,000.00 USD | 5,220.00 USD | 1,610.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1108` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 4,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1110` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 494.75 USD | 916.88 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1110` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 12,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1112` | 1,560,000.00 USD | 1,560,000.00 USD | 10,780.00 USD | 747.13 USD | 140.10 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1112` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 11,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1114` | 1,600,000.00 USD | 1,600,000.00 USD | 15,810.00 USD | 5,880.00 USD | 13,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1115` | 1,880.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1116` | 1,620,000.00 USD | 1,620,000.00 USD | 6,690.00 USD | 8,250.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1118` | 1,680,000.00 USD | 1,680,000.00 USD | 15,830.00 USD | 5,300.00 USD | 41,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1118` | 2,640,000.00 USD | 2,640,000.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1120` | 1,730,000.00 USD | 1,730,000.00 USD | 27,100.00 USD | 10,220.00 USD | 9,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1120` | 2,690,000.00 USD | 2,690,000.00 USD | 17,760.00 USD | 0.00 USD | 29,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1122` | 1,770,000.00 USD | 1,770,000.00 USD | 17,920.00 USD | 5,820.00 USD | 15,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1122` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 23,980.00 USD | 34,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1124` | 1,810,000.00 USD | 1,810,000.00 USD | 18,340.00 USD | 6,940.00 USD | 9,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1124` | 2,810,000.00 USD | 2,810,000.00 USD | 19,800.00 USD | 2,030.00 USD | 40,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1126` | 1,850,000.00 USD | 1,850,000.00 USD | 11,790.00 USD | 7,720.00 USD | 20,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1126` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 4,950.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1128` | 1,870,000.00 USD | 1,870,000.00 USD | 11,080.00 USD | 485.32 USD | 12,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1128` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 2,020.00 USD | 17,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1130` | 1,900,000.00 USD | 1,900,000.00 USD | 10,390.00 USD | 3,780.00 USD | 20,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1130` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 17,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1132` | 1,950,000.00 USD | 1,950,000.00 USD | 21,250.00 USD | 12,190.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1132` | 2,880,000.00 USD | 2,880,000.00 USD | 12,540.00 USD | 0.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1134` | 1,990,000.00 USD | 1,990,000.00 USD | 6,630.00 USD | 13,000.00 USD | 15,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1134` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 14,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1136` | 2,000,000.00 USD | 2,000,000.00 USD | 2,940.00 USD | 2,030.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1136` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 7,760.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1138` | 2,010,000.00 USD | 2,010,000.00 USD | 2,710.00 USD | 453.87 USD | 6,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1138` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 9,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1140` | 2,020,000.00 USD | 2,020,000.00 USD | 5,070.00 USD | 844.95 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1140` | 2,930,000.00 USD | 2,930,000.00 USD | 2,220.00 USD | 0.00 USD | 7,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1142` | 2,080,000.00 USD | 2,080,000.00 USD | 23,040.00 USD | 9,520.00 USD | 21,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1142` | 2,940,000.00 USD | 2,940,000.00 USD | 10,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1144` | 2,120,000.00 USD | 2,120,000.00 USD | 7,010.00 USD | 18,270.00 USD | 20,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1144` | 3,100,000.00 USD | 3,100,000.00 USD | 10,360.00 USD | 2,730.00 USD | 143,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1146` | 2,160,000.00 USD | 2,160,000.00 USD | 5,090.00 USD | 8,780.00 USD | 23,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1146` | 3,300,000.00 USD | 3,300,000.00 USD | 16,060.00 USD | 0.00 USD | 188,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1148` | 2,190,000.00 USD | 2,190,000.00 USD | 18,620.00 USD | 624.71 USD | 14,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1148` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 63,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1150` | 2,240,000.00 USD | 2,240,000.00 USD | 19,260.00 USD | 13,020.00 USD | 19,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1150` | 3,480,000.00 USD | 3,480,000.00 USD | 18,520.00 USD | 0.00 USD | 89,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1152` | 2,320,000.00 USD | 2,320,000.00 USD | 16,910.00 USD | 16,590.00 USD | 45,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1152` | 3,790,000.00 USD | 3,790,000.00 USD | 165,860.00 USD | 12,610.00 USD | 132,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1154` | 2,380,000.00 USD | 2,380,000.00 USD | 13,300.00 USD | 4,450.00 USD | 39,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1154` | 4,100,000.00 USD | 4,100,000.00 USD | 149,770.00 USD | 18,580.00 USD | 143,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1156` | 4,320,000.00 USD | 4,320,000.00 USD | 128,780.00 USD | 21,540.00 USD | 74,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1158` | 4,490,000.00 USD | 4,490,000.00 USD | 94,470.00 USD | 16,470.00 USD | 55,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1160` | 4,640,000.00 USD | 4,640,000.00 USD | 51,910.00 USD | 20,120.00 USD | 76,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1185` | 3,310.00 USD | 5,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1225` | 721.08 USD | 5,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1375` | 21,950.00 USD | 27,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1415` | 3,800.00 USD | 31,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1495` | 21,820.00 USD | 53,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1525` | 6,090.00 USD | 59,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1565` | 550.61 USD | 60,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1615` | 254.17 USD | 60,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1695` | 169.25 USD | 60,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1745` | 131.08 USD | 60,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1755` | 147.21 USD | 60,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1815` | 102.00 USD | 60,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1825` | 514.28 USD | 61,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1855` | 166.95 USD | 61,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1865` | 199.93 USD | 61,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2065` | 998.16 USD | 62,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0305` | 122,470.00 USD | 0.00 USD | 1,320.00 USD | `-70.88%` | `43,265.90` |
| `Live` | `Long` | `0.0385` | 121,150.00 USD | 0.00 USD | 231.00 USD | `-63.25%` | `6,000.00` |
| `Live` | `Long` | `0.0545` | 120,920.00 USD | 0.00 USD | 277.89 USD | `-47.97%` | `5,098.90` |
| `Live` | `Long` | `0.0555` | 120,640.00 USD | 0.00 USD | 425.34 USD | `-47.02%` | `7,663.80` |
| `Live` | `Long` | `0.0565` | 120,210.00 USD | 0.00 USD | 3,940.00 USD | `-46.06%` | `69,790.10` |
| `Live` | `Long` | `0.0585` | 116,270.00 USD | 0.00 USD | 844.12 USD | `-44.15%` | `14,429.40` |
| `Live` | `Long` | `0.0615` | 115,430.00 USD | 0.00 USD | 315.09 USD | `-41.29%` | `5,123.40` |
| `Live` | `Long` | `0.0645` | 115,110.00 USD | 0.00 USD | 353.81 USD | `-38.42%` | `5,485.40` |
| `Live` | `Long` | `0.0675` | 114,760.00 USD | 0.00 USD | 518.48 USD | `-35.56%` | `7,681.20` |
| `Live` | `Long` | `0.0685` | 114,240.00 USD | 0.00 USD | 1,920.00 USD | `-34.61%` | `28,000.00` |
| `Live` | `Long` | `0.0705` | 112,320.00 USD | 0.00 USD | 1,090.00 USD | `-32.70%` | `15,500.00` |
| `Live` | `Long` | `0.0715` | 111,230.00 USD | 0.00 USD | 40,420.00 USD | `-31.74%` | `565,287.50` |
| `Live` | `Long` | `0.0725` | 70,810.00 USD | 0.00 USD | 23,910.00 USD | `-30.79%` | `329,855.60` |
| `Live` | `Long` | `0.0735` | 46,900.00 USD | 0.00 USD | 2,530.00 USD | `-29.83%` | `34,439.60` |
| `Live` | `Long` | `0.0745` | 44,360.00 USD | 0.00 USD | 2,300.00 USD | `-28.88%` | `30,851.90` |
| `Live` | `Long` | `0.0755` | 42,070.00 USD | 0.00 USD | 12,440.00 USD | `-27.92%` | `164,709.50` |
| `Live` | `Long` | `0.0765` | 29,630.00 USD | 0.00 USD | 1,170.00 USD | `-26.97%` | `15,263.30` |
| `Live` | `Long` | `0.0775` | 28,460.00 USD | 0.00 USD | 878.62 USD | `-26.01%` | `11,337.00` |
| `Live` | `Long` | `0.0785` | 27,580.00 USD | 0.00 USD | 1,920.00 USD | `-25.06%` | `24,457.80` |
| `Live` | `Long` | `0.0795` | 25,660.00 USD | 0.00 USD | 1,110.00 USD | `-24.11%` | `13,940.20` |
| `Live` | `Long` | `0.0805` | 24,560.00 USD | 0.00 USD | 223.98 USD | `-23.15%` | `2,782.40` |
| `Live` | `Long` | `0.0815` | 24,330.00 USD | 0.00 USD | 1,560.00 USD | `-22.20%` | `19,181.40` |
| `Live` | `Long` | `0.0825` | 22,770.00 USD | 0.00 USD | 140.74 USD | `-21.24%` | `1,705.90` |
| `Live` | `Long` | `0.0845` | 22,630.00 USD | 0.00 USD | 14,300.00 USD | `-19.33%` | `169,238.60` |
| `Live` | `Long` | `0.0855` | 8,330.00 USD | 0.00 USD | 1,710.00 USD | `-18.38%` | `20,000.00` |
| `Live` | `Long` | `0.0865` | 6,620.00 USD | 0.00 USD | 318.30 USD | `-17.42%` | `3,679.80` |
| `Live` | `Long` | `0.0875` | 6,300.00 USD | 0.00 USD | 793.17 USD | `-16.47%` | `9,064.80` |
| `Live` | `Long` | `0.0895` | 5,510.00 USD | 0.00 USD | 3,270.00 USD | `-14.56%` | `36,562.50` |
| `Live` | `Long` | `0.0905` | 2,230.00 USD | 0.00 USD | 2,230.00 USD | `-13.60%` | `24,685.10` |
| `Live` | `Short` | `0.1165` | 3,130.00 USD | 3,130.00 USD | 0.00 USD | `+11.22%` | `26,889.40` |
| `Live` | `Short` | `0.1185` | 4,490.00 USD | 1,360.00 USD | 0.00 USD | `+13.13%` | `11,447.30` |
| `Live` | `Short` | `0.1225` | 5,210.00 USD | 721.08 USD | 0.00 USD | `+16.95%` | `5,886.40` |
| `Live` | `Short` | `0.1245` | 5,850.00 USD | 637.29 USD | 0.00 USD | `+18.85%` | `5,118.80` |
| `Live` | `Short` | `0.1345` | 28,710.00 USD | 22,860.00 USD | 0.00 USD | `+28.40%` | `170,000.00` |
| `Live` | `Short` | `0.1505` | 49,480.00 USD | 20,770.00 USD | 0.00 USD | `+43.68%` | `137,988.80` |
| `Live` | `Short` | `0.1525` | 55,570.00 USD | 6,090.00 USD | 0.00 USD | `+45.58%` | `39,929.50` |
| `Live` | `Short` | `0.1565` | 56,120.00 USD | 550.61 USD | 0.00 USD | `+49.40%` | `3,518.30` |
| `Live` | `Short` | `0.1695` | 56,290.00 USD | 169.25 USD | 0.00 USD | `+61.81%` | `998.50` |
| `Live` | `Short` | `0.1705` | 56,560.00 USD | 268.33 USD | 0.00 USD | `+62.77%` | `1,573.80` |
| `Live` | `Short` | `0.1745` | 56,690.00 USD | 131.08 USD | 0.00 USD | `+66.59%` | `751.20` |
| `Live` | `Short` | `0.1755` | 56,840.00 USD | 147.21 USD | 0.00 USD | `+67.54%` | `838.80` |
| `Live` | `Short` | `0.1825` | 57,450.00 USD | 616.85 USD | 0.00 USD | `+74.22%` | `3,380.00` |
| `Live` | `Short` | `0.1855` | 57,620.00 USD | 166.95 USD | 0.00 USD | `+77.09%` | `900.00` |
| `Live` | `Short` | `0.1865` | 57,820.00 USD | 199.93 USD | 0.00 USD | `+78.04%` | `1,072.00` |
| `Live` | `Short` | `0.2065` | 58,820.00 USD | 998.16 USD | 0.00 USD | `+97.14%` | `4,833.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0635` | 36,830.00 USD | 0.00 USD | 1,140.00 USD | `-39.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 35,690.00 USD | 0.00 USD | 773.46 USD | `-32.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 34,920.00 USD | 0.00 USD | 592.27 USD | `-31.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 34,320.00 USD | 0.00 USD | 755.00 USD | `-27.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0805` | 33,570.00 USD | 0.00 USD | 411.06 USD | `-23.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0815` | 33,160.00 USD | 0.00 USD | 285.01 USD | `-22.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0835` | 32,870.00 USD | 0.00 USD | 456.70 USD | `-20.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0845` | 32,420.00 USD | 0.00 USD | 171.09 USD | `-19.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 32,250.00 USD | 0.00 USD | 631.58 USD | `-18.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 31,610.00 USD | 0.00 USD | 380.89 USD | `-17.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 31,230.00 USD | 0.00 USD | 782.05 USD | `-15.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 30,450.00 USD | 0.00 USD | 444.62 USD | `-13.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0915` | 30,010.00 USD | 0.00 USD | 623.91 USD | `-12.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 29,380.00 USD | 0.00 USD | 485.13 USD | `-9.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0965` | 28,900.00 USD | 0.00 USD | 5,700.00 USD | `-7.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0975` | 23,200.00 USD | 0.00 USD | 216.41 USD | `-6.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0985` | 22,980.00 USD | 0.00 USD | 144.62 USD | `-5.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0995` | 22,840.00 USD | 0.00 USD | 17,230.00 USD | `-5.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 5,610.00 USD | 0.00 USD | 2,180.00 USD | `-4.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1015` | 3,430.00 USD | 0.00 USD | 903.42 USD | `-3.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 2,530.00 USD | 0.00 USD | 780.70 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1035` | 1,750.00 USD | 0.00 USD | 1,640.00 USD | `-1.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1045` | 105.53 USD | 0.00 USD | 105.53 USD | `-0.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 227.76 USD | 227.76 USD | 0.00 USD | `+0.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 109,510.00 USD | 109,280.00 USD | 0.00 USD | `+1.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1075` | 109,980.00 USD | 473.35 USD | 0.00 USD | `+2.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1095` | 128,600.00 USD | 18,610.00 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 128,760.00 USD | 160.20 USD | 0.00 USD | `+5.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 129,010.00 USD | 247.49 USD | 0.00 USD | `+6.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1125` | 129,790.00 USD | 786.65 USD | 0.00 USD | `+7.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1135` | 129,910.00 USD | 116.27 USD | 0.00 USD | `+8.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 130,050.00 USD | 137.71 USD | 0.00 USD | `+10.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1165` | 130,230.00 USD | 180.81 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1175` | 130,590.00 USD | 363.49 USD | 0.00 USD | `+12.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1185` | 130,860.00 USD | 265.74 USD | 0.00 USD | `+13.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1195` | 145,490.00 USD | 14,640.00 USD | 0.00 USD | `+14.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1225` | 146,470.00 USD | 980.00 USD | 0.00 USD | `+16.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1235` | 153,840.00 USD | 7,370.00 USD | 0.00 USD | `+17.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1255` | 158,210.00 USD | 4,380.00 USD | 0.00 USD | `+19.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1315` | 189,780.00 USD | 31,560.00 USD | 0.00 USD | `+25.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1335` | 191,090.00 USD | 1,310.00 USD | 0.00 USD | `+27.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1345` | 195,240.00 USD | 4,150.00 USD | 0.00 USD | `+28.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1365` | 202,990.00 USD | 7,750.00 USD | 0.00 USD | `+30.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1405` | 216,100.00 USD | 13,110.00 USD | 0.00 USD | `+34.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1425` | 216,200.00 USD | 102.22 USD | 0.00 USD | `+36.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1435` | 223,380.00 USD | 7,180.00 USD | 0.00 USD | `+36.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1485` | 226,020.00 USD | 2,650.00 USD | 0.00 USD | `+41.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1525` | 229,790.00 USD | 3,770.00 USD | 0.00 USD | `+45.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 229,970.00 USD | 184.49 USD | 0.00 USD | `+48.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 232,780.00 USD | 2,810.00 USD | 0.00 USD | `+49.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 233,000.00 USD | 219.81 USD | 0.00 USD | `+50.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 233,280.00 USD | 277.62 USD | 0.00 USD | `+56.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 235,310.00 USD | 2,030.00 USD | 0.00 USD | `+61.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 235,520.00 USD | 216.55 USD | 0.00 USD | `+66.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 235,640.00 USD | 117.26 USD | 0.00 USD | `+88.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 256,180.00 USD | 20,530.00 USD | 0.00 USD | `+91.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 256,360.00 USD | 189.30 USD | 0.00 USD | `+94.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 256,580.00 USD | 219.22 USD | 0.00 USD | `+95.23%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0862` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 0.00 USD | 1,880.00 USD | 4,710.00 USD |
| `7D` | `0.0864` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 0.00 USD | 1,980.00 USD | 15,640.00 USD |
| `7D` | `0.0866` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 2,130.00 USD |
| `7D` | `0.0868` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 2,880.00 USD |
| `7D` | `0.0870` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 2,850.00 USD |
| `7D` | `0.0872` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 0.00 USD | 1,200.00 USD | 2,950.00 USD |
| `7D` | `0.0874` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 6,010.00 USD | 0.00 USD | 4,530.00 USD |
| `7D` | `0.0876` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 0.00 USD | 1,770.00 USD | 4,870.00 USD |
| `7D` | `0.0878` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 9,200.00 USD | 5,890.00 USD | 25,080.00 USD |
| `7D` | `0.0880` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 3,770.00 USD | 2,200.00 USD | 11,850.00 USD |
| `7D` | `0.0882` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 12,660.00 USD | 7,260.00 USD | 9,270.00 USD |
| `7D` | `0.0884` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 0.00 USD | 1,220.00 USD | 13,650.00 USD |
| `7D` | `0.0886` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 9,350.00 USD | 2,470.00 USD | 11,300.00 USD |
| `7D` | `0.0888` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 3,370.00 USD | 2,720.00 USD | 8,250.00 USD |
| `7D` | `0.0890` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 13,510.00 USD | 3,610.00 USD | 13,150.00 USD |
| `7D` | `0.0892` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 3,620.00 USD | 3,060.00 USD | 2,090.00 USD |
| `7D` | `0.0894` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 5,480.00 USD | 3,400.00 USD | 7,770.00 USD |
| `7D` | `0.0896` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 4,300.00 USD | 0.00 USD | 4,180.00 USD |
| `7D` | `0.0898` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 3,390.00 USD | 927.82 USD | 4,500.00 USD |
| `7D` | `0.0900` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 1,250.00 USD | 428.11 USD | 251.79 USD |
| `7D` | `0.0902` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 1,030.00 USD | 482.67 USD | 1,210.00 USD |
| `7D` | `0.0904` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 5,730.00 USD | 996.61 USD | 1,630.00 USD |
| `7D` | `0.0906` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 6,040.00 USD | 1,900.00 USD | 4,230.00 USD |
| `7D` | `0.0908` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 2,540.00 USD | 2,570.00 USD | 1,260.00 USD |
| `7D` | `0.0910` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 0.00 USD | 606.54 USD | 27.47 USD |
| `7D` | `0.0912` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD |
| `7D` | `0.0914` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 1,670.00 USD | 903.90 USD | 108.00 USD |
| `1D` | `0.0916` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 6,590.00 USD | 2,510.00 USD | 244.54 USD |
| `7D` | `0.0916` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 6,500.00 USD |
| `1D` | `0.0918` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 6,400.00 USD | 4,060.00 USD | 2,530.00 USD |
| `7D` | `0.0918` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 1,740.00 USD |
| `1D` | `0.0920` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 6,400.00 USD | 1,320.00 USD | 20,360.00 USD |
| `7D` | `0.0920` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 7,440.00 USD | 2,030.00 USD | 58.40 USD |
| `1D` | `0.0922` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 2,430.00 USD | 4,100.00 USD | 14,030.00 USD |
| `7D` | `0.0922` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 0.00 USD | 7,660.00 USD | 34,750.00 USD |
| `1D` | `0.0924` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 4,790.00 USD | 4,700.00 USD | 43,420.00 USD |
| `7D` | `0.0924` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 1,790.00 USD | 2,020.00 USD | 11,840.00 USD |
| `1D` | `0.0926` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 5,130.00 USD | 4,460.00 USD | 555.49 USD |
| `7D` | `0.0926` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 8,170.00 USD |
| `1D` | `0.0928` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 2,600.00 USD | 1,100.00 USD | 1,530.00 USD |
| `7D` | `0.0928` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD |
| `1D` | `0.0930` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 7,300.00 USD | 2,440.00 USD | 8,690.00 USD |
| `7D` | `0.0930` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 0.00 USD | 5,320.00 USD | 56.98 USD |
| `1D` | `0.0932` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 2,710.00 USD | 1,300.00 USD | 5,080.00 USD |
| `7D` | `0.0932` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 2,220.00 USD | 0.00 USD | 12,300.00 USD |
| `1D` | `0.0934` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 22,030.00 USD | 3,830.00 USD | 17,910.00 USD |
| `7D` | `0.0934` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 5.32 USD |
| `1D` | `0.0936` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 7,080.00 USD | 9,360.00 USD | 16,330.00 USD |
| `7D` | `0.0936` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 19,560.00 USD | 6,840.00 USD | 25,450.00 USD |
| `1D` | `0.0938` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 8,170.00 USD | 2,920.00 USD | 46,580.00 USD |
| `7D` | `0.0938` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 113.42 USD |
| `1D` | `0.0940` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD |
| `7D` | `0.0940` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 14,050.00 USD | 0.00 USD | 10,630.00 USD |
| `1D` | `0.0942` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 3,500.00 USD | 16,110.00 USD | 49,220.00 USD |
| `7D` | `0.0942` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 6,170.00 USD | 18,340.00 USD | 114,010.00 USD |
| `1D` | `0.0944` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 11,620.00 USD | 4,860.00 USD | 36,500.00 USD |
| `7D` | `0.0944` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 0.00 USD | 2,010.00 USD | 0.00 USD |
| `1D` | `0.0946` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 4,130.00 USD | 5,280.00 USD | 10,220.00 USD |
| `7D` | `0.0946` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 0.00 USD | 1,810.00 USD | 62.83 USD |
| `1D` | `0.0948` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 0.00 USD | 1,100.00 USD | 101.09 USD |
| `7D` | `0.0948` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 3,770.00 USD | 0.00 USD | 26,920.00 USD |
| `1D` | `0.0950` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 12,180.00 USD | 6,710.00 USD | 22,900.00 USD |
| `7D` | `0.0950` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 0.00 USD | 9,700.00 USD | 64.98 USD |
| `1D` | `0.0952` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 0.00 USD | 853.02 USD | 6,660.00 USD |
| `7D` | `0.0952` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 0.00 USD | 4,410.00 USD | 0.00 USD |
| `1D` | `0.0954` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 41,470.00 USD | 11,160.00 USD | 21,160.00 USD |
| `7D` | `0.0954` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 0.00 USD | 3,740.00 USD | 147.58 USD |
| `1D` | `0.0956` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 18,680.00 USD | 9,390.00 USD | 37,070.00 USD |
| `7D` | `0.0956` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 39,120.00 USD | 13,670.00 USD | 51,050.00 USD |
| `1D` | `0.0958` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 7,180.00 USD | 4,290.00 USD | 22,320.00 USD |
| `7D` | `0.0958` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 21,320.00 USD |
| `1D` | `0.0960` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 0.00 USD | 16,940.00 USD | 146.83 USD |
| `7D` | `0.0960` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 28,110.00 USD | 16,920.00 USD | 19,960.00 USD |
| `1D` | `0.0962` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 8,920.00 USD | 15,440.00 USD | 27,750.00 USD |
| `7D` | `0.0962` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 12,340.00 USD | 0.00 USD | 74,940.00 USD |
| `1D` | `0.0964` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 31,490.00 USD | 10,380.00 USD | 27,840.00 USD |
| `7D` | `0.0964` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 0.00 USD | 4,020.00 USD | 83.82 USD |
| `1D` | `0.0966` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | 3,880.00 USD | 815.14 USD |
| `7D` | `0.0966` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 0.00 USD | 2,390.00 USD | 2,830.00 USD |
| `1D` | `0.0968` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | 2,960.00 USD | 2,380.00 USD |
| `7D` | `0.0968` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 7,490.00 USD | 0.00 USD | 56,240.00 USD |
| `1D` | `0.0970` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 8,360.00 USD | 8,640.00 USD | 16,030.00 USD |
| `7D` | `0.0970` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 0.00 USD | 7,090.00 USD | 5,010.00 USD |
| `1D` | `0.0972` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 2,860.00 USD | 3,220.00 USD | 1,980.00 USD |
| `7D` | `0.0972` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 0.00 USD | 8,830.00 USD | 104.80 USD |
| `1D` | `0.0974` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 0.00 USD | 7,010.00 USD | 0.00 USD |
| `7D` | `0.0974` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 0.00 USD | 7,480.00 USD | 87.10 USD |
| `1D` | `0.0976` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 0.00 USD | 765.93 USD | 1,040.00 USD |
| `7D` | `0.0976` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 73.00 USD |
| `1D` | `0.0978` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 0.00 USD | 817.22 USD | 67.90 USD |
| `1D` | `0.0980` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 12,700.00 USD | 4,570.00 USD | 21,130.00 USD |
| `7D` | `0.0980` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 22,280.00 USD | 0.00 USD | 75.46 USD |
| `1D` | `0.0982` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 10,790.00 USD | 7,650.00 USD | 0.00 USD |
| `7D` | `0.0982` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 0.00 USD | 5,070.00 USD | 11,550.00 USD |
| `1D` | `0.0984` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 10,310.00 USD | 19,740.00 USD | 15,450.00 USD |
| `7D` | `0.0984` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 0.00 USD | 16,160.00 USD | 126.67 USD |
| `1D` | `0.0986` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 7,260.00 USD | 8,960.00 USD | 11,390.00 USD |
| `7D` | `0.0986` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 5,330.00 USD | 16,520.00 USD | 6,730.00 USD |
| `1D` | `0.0988` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 30,450.00 USD | 7,150.00 USD | 33,720.00 USD |
| `7D` | `0.0988` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 10,360.00 USD | 7,820.00 USD | 90.31 USD |
| `1D` | `0.0990` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 12,880.00 USD | 4,730.00 USD | 4,590.00 USD |
| `7D` | `0.0990` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 30,090.00 USD | 6,660.00 USD | 122.11 USD |
| `1D` | `0.0992` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 84,750.00 USD | 7,620.00 USD | 30,750.00 USD |
| `7D` | `0.0992` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 12,790.00 USD | 11,440.00 USD | 221.55 USD |
| `1D` | `0.0994` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 32,970.00 USD | 3,250.00 USD | 20,440.00 USD |
| `7D` | `0.0994` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 55,790.00 USD | 0.00 USD | 65,270.00 USD |
| `1D` | `0.0996` | 949,120.00 USD | 0.00 USD | 949,120.00 USD | 15,040.00 USD | 2,450.00 USD | 74,900.00 USD |
| `7D` | `0.0996` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 27,010.00 USD | 5,500.00 USD | 33,050.00 USD |
| `1D` | `0.0998` | 856,740.00 USD | 0.00 USD | 856,740.00 USD | 12,990.00 USD | 5,820.00 USD | 57,790.00 USD |
| `7D` | `0.0998` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 21,180.00 USD | 11,540.00 USD | 113,290.00 USD |
| `1D` | `0.1000` | 780,140.00 USD | 0.00 USD | 780,140.00 USD | 10,360.00 USD | 16,010.00 USD | 35,460.00 USD |
| `7D` | `0.1000` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 54,220.00 USD | 25,020.00 USD | 33,080.00 USD |
| `1D` | `0.1002` | 718,310.00 USD | 0.00 USD | 718,310.00 USD | 17,830.00 USD | 4,080.00 USD | 42,920.00 USD |
| `7D` | `0.1002` | 952,660.00 USD | 0.00 USD | 952,660.00 USD | 70,060.00 USD | 10,690.00 USD | 74,890.00 USD |
| `1D` | `0.1004` | 653,480.00 USD | 0.00 USD | 653,480.00 USD | 53,750.00 USD | 30,530.00 USD | 48,490.00 USD |
| `7D` | `0.1004` | 797,020.00 USD | 0.00 USD | 797,020.00 USD | 19,310.00 USD | 17,550.00 USD | 46,130.00 USD |
| `1D` | `0.1006` | 520,710.00 USD | 0.00 USD | 520,710.00 USD | 24,030.00 USD | 23,800.00 USD | 29,820.00 USD |
| `7D` | `0.1006` | 714,030.00 USD | 0.00 USD | 714,030.00 USD | 23,200.00 USD | 23,170.00 USD | 67,130.00 USD |
| `1D` | `0.1008` | 443,070.00 USD | 0.00 USD | 443,070.00 USD | 17,840.00 USD | 11,220.00 USD | 3,770.00 USD |
| `7D` | `0.1008` | 600,530.00 USD | 0.00 USD | 600,530.00 USD | 13,040.00 USD | 5,470.00 USD | 96,530.00 USD |
| `1D` | `0.1010` | 410,240.00 USD | 0.00 USD | 410,240.00 USD | 23,240.00 USD | 13,530.00 USD | 23,750.00 USD |
| `7D` | `0.1010` | 485,500.00 USD | 0.00 USD | 485,500.00 USD | 29,550.00 USD | 24,610.00 USD | 3,990.00 USD |
| `1D` | `0.1012` | 349,730.00 USD | 0.00 USD | 349,730.00 USD | 16,360.00 USD | 9,190.00 USD | 19,550.00 USD |
| `7D` | `0.1012` | 427,350.00 USD | 0.00 USD | 427,350.00 USD | 6,490.00 USD | 35,670.00 USD | 0.00 USD |
| `1D` | `0.1014` | 304,640.00 USD | 0.00 USD | 304,640.00 USD | 13,540.00 USD | 6,940.00 USD | 16,970.00 USD |
| `7D` | `0.1014` | 385,190.00 USD | 0.00 USD | 385,190.00 USD | 40,860.00 USD | 15,590.00 USD | 25,450.00 USD |
| `1D` | `0.1016` | 267,170.00 USD | 0.00 USD | 267,170.00 USD | 8,170.00 USD | 775.38 USD | 23,150.00 USD |
| `7D` | `0.1016` | 303,290.00 USD | 0.00 USD | 303,290.00 USD | 14,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1018` | 235,070.00 USD | 0.00 USD | 235,070.00 USD | 18,090.00 USD | 1,550.00 USD | 3,430.00 USD |
| `7D` | `0.1018` | 289,290.00 USD | 0.00 USD | 289,290.00 USD | 39,450.00 USD | 0.00 USD | 10,630.00 USD |
| `1D` | `0.1020` | 212,010.00 USD | 0.00 USD | 212,010.00 USD | 0.00 USD | 0.00 USD | 11,590.00 USD |
| `7D` | `0.1020` | 239,210.00 USD | 0.00 USD | 239,210.00 USD | 0.00 USD | 8,460.00 USD | 47,420.00 USD |
| `1D` | `0.1022` | 200,430.00 USD | 0.00 USD | 200,430.00 USD | 0.00 USD | 0.00 USD | 6,020.00 USD |
| `1D` | `0.1026` | 194,400.00 USD | 0.00 USD | 194,400.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD |
| `7D` | `0.1032` | 183,320.00 USD | 0.00 USD | 183,320.00 USD | 13,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1034` | 170,140.00 USD | 0.00 USD | 170,140.00 USD | 0.00 USD | 0.00 USD | 52.59 USD |
| `1D` | `0.1036` | 192,760.00 USD | 0.00 USD | 192,760.00 USD | 2,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1036` | 170,090.00 USD | 0.00 USD | 170,090.00 USD | 0.00 USD | 0.00 USD | 283.46 USD |
| `1D` | `0.1038` | 190,600.00 USD | 0.00 USD | 190,600.00 USD | 0.00 USD | 14,190.00 USD | 24.05 USD |
| `7D` | `0.1038` | 169,800.00 USD | 0.00 USD | 169,800.00 USD | 0.00 USD | 10,870.00 USD | 31,670.00 USD |
| `1D` | `0.1040` | 176,390.00 USD | 0.00 USD | 176,390.00 USD | 0.00 USD | 19,120.00 USD | 15,140.00 USD |
| `7D` | `0.1040` | 127,260.00 USD | 0.00 USD | 127,260.00 USD | 0.00 USD | 5,130.00 USD | 199.67 USD |
| `1D` | `0.1042` | 142,120.00 USD | 0.00 USD | 142,120.00 USD | 22,890.00 USD | 9,410.00 USD | 25,770.00 USD |
| `7D` | `0.1042` | 121,930.00 USD | 0.00 USD | 121,930.00 USD | 49,380.00 USD | 12,190.00 USD | 537.52 USD |
| `1D` | `0.1044` | 84,060.00 USD | 0.00 USD | 84,060.00 USD | 24,130.00 USD | 36,390.00 USD | 23,540.00 USD |
| `7D` | `0.1044` | 59,820.00 USD | 0.00 USD | 59,820.00 USD | 11,140.00 USD | 25,310.00 USD | 23,380.00 USD |
| `1D` | `0.1045` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1046` | 43,560.00 USD | 43,560.00 USD | 0.00 USD | 16,570.00 USD | 0.00 USD | 26,990.00 USD |
| `7D` | `0.1046` | 84,090.00 USD | 84,090.00 USD | 0.00 USD | 0.00 USD | 23,140.00 USD | 60,950.00 USD |
| `7D` | `0.1046` | 168,180.00 USD | 168,180.00 USD | 0.00 USD | 0.00 USD | 23,140.00 USD | 60,950.00 USD |
| `1D` | `0.1048` | 183,450.00 USD | 183,450.00 USD | 0.00 USD | 36,040.00 USD | 17,510.00 USD | 86,340.00 USD |
| `7D` | `0.1048` | 256,680.00 USD | 256,680.00 USD | 0.00 USD | 30,640.00 USD | 14,940.00 USD | 42,930.00 USD |
| `1D` | `0.1050` | 242,160.00 USD | 242,160.00 USD | 0.00 USD | 32,940.00 USD | 21,980.00 USD | 3,780.00 USD |
| `7D` | `0.1050` | 348,230.00 USD | 348,230.00 USD | 0.00 USD | 27,290.00 USD | 0.00 USD | 64,260.00 USD |
| `1D` | `0.1052` | 327,390.00 USD | 327,390.00 USD | 0.00 USD | 39,930.00 USD | 15,010.00 USD | 30,300.00 USD |
| `7D` | `0.1052` | 519,670.00 USD | 519,670.00 USD | 0.00 USD | 32,640.00 USD | 34,840.00 USD | 103,960.00 USD |
| `1D` | `0.1054` | 449,300.00 USD | 449,300.00 USD | 0.00 USD | 45,620.00 USD | 18,770.00 USD | 57,510.00 USD |
| `7D` | `0.1054` | 751,050.00 USD | 751,050.00 USD | 0.00 USD | 85,290.00 USD | 53,700.00 USD | 92,390.00 USD |
| `1D` | `0.1056` | 526,940.00 USD | 526,940.00 USD | 0.00 USD | 25,800.00 USD | 23,260.00 USD | 28,580.00 USD |
| `7D` | `0.1056` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 87,170.00 USD | 47,540.00 USD | 174,880.00 USD |
| `1D` | `0.1058` | 626,240.00 USD | 626,240.00 USD | 0.00 USD | 25,860.00 USD | 6,490.00 USD | 66,950.00 USD |
| `7D` | `0.1058` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 54,790.00 USD | 24,600.00 USD | 136,950.00 USD |
| `1D` | `0.1060` | 700,410.00 USD | 700,410.00 USD | 0.00 USD | 44,720.00 USD | 2,700.00 USD | 26,750.00 USD |
| `7D` | `0.1060` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 55,680.00 USD | 51,150.00 USD | 79,550.00 USD |
| `1D` | `0.1062` | 800,560.00 USD | 800,560.00 USD | 0.00 USD | 44,570.00 USD | 4,130.00 USD | 51,450.00 USD |
| `7D` | `0.1062` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 46,950.00 USD | 28,310.00 USD | 82,040.00 USD |
| `1D` | `0.1064` | 844,040.00 USD | 844,040.00 USD | 0.00 USD | 6,960.00 USD | 7,730.00 USD | 28,790.00 USD |
| `7D` | `0.1064` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 44,270.00 USD | 144,950.00 USD |
| `1D` | `0.1066` | 917,810.00 USD | 917,810.00 USD | 0.00 USD | 15,590.00 USD | 15,700.00 USD | 42,490.00 USD |
| `7D` | `0.1066` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 42,670.00 USD | 107,630.00 USD |
| `1D` | `0.1068` | 988,760.00 USD | 988,760.00 USD | 0.00 USD | 11,970.00 USD | 9,310.00 USD | 49,670.00 USD |
| `7D` | `0.1068` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 5,330.00 USD | 41,360.00 USD | 80,000.00 USD |
| `1D` | `0.1070` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 23,200.00 USD | 11,060.00 USD | 17,420.00 USD |
| `7D` | `0.1070` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 45,840.00 USD | 98,640.00 USD |
| `1D` | `0.1072` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 9,010.00 USD | 6,120.00 USD | 4,730.00 USD |
| `7D` | `0.1072` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 16,280.00 USD | 9,400.00 USD | 10,350.00 USD |
| `1D` | `0.1074` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 8,180.00 USD | 4,590.00 USD | 9,000.00 USD |
| `7D` | `0.1074` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 29,150.00 USD | 104.80 USD |
| `1D` | `0.1076` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 8,210.00 USD | 4,100.00 USD | 5,870.00 USD |
| `7D` | `0.1076` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD | 22,580.00 USD |
| `1D` | `0.1078` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 3,440.00 USD | 22,300.00 USD |
| `7D` | `0.1078` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 5,620.00 USD | 3,380.00 USD | 73.00 USD |
| `1D` | `0.1080` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 3,230.00 USD | 1,480.00 USD | 6,540.00 USD |
| `7D` | `0.1080` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,890.00 USD |
| `1D` | `0.1082` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 11,630.00 USD | 7,440.00 USD | 5,980.00 USD |
| `7D` | `0.1082` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 6,650.00 USD | 0.00 USD | 138.29 USD |
| `1D` | `0.1084` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 7,990.00 USD | 385.06 USD | 35,900.00 USD |
| `7D` | `0.1084` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 89.24 USD |
| `1D` | `0.1086` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 4,220.00 USD | 2,240.00 USD | 50,470.00 USD |
| `7D` | `0.1086` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 258.30 USD |
| `1D` | `0.1088` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 40,240.00 USD | 1,860.00 USD | 9,280.00 USD |
| `7D` | `0.1088` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 5,290.00 USD | 1,420.00 USD | 9,570.00 USD |
| `1D` | `0.1090` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 39,470.00 USD | 813.86 USD | 2,170.00 USD |
| `7D` | `0.1090` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 78.56 USD |
| `1D` | `0.1092` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 10,290.00 USD | 1,080.00 USD | 79.59 USD |
| `7D` | `0.1092` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 1,500.00 USD | 17,740.00 USD |
| `1D` | `0.1094` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 13,100.00 USD | 0.00 USD | 14,050.00 USD |
| `7D` | `0.1094` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 184.76 USD |
| `1D` | `0.1096` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 7,780.00 USD |
| `7D` | `0.1096` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 162.67 USD |
| `1D` | `0.1098` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 13,380.00 USD | 4,460.00 USD | 22,840.00 USD |
| `7D` | `0.1098` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 21,840.00 USD |
| `1D` | `0.1100` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 3,310.00 USD | 4,310.00 USD |
| `7D` | `0.1100` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 109.00 USD |
| `1D` | `0.1102` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 5,570.00 USD | 509.08 USD | 0.00 USD |
| `7D` | `0.1102` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23,290.00 USD |
| `1D` | `0.1104` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 6,920.00 USD | 11,640.00 USD | 1,170.00 USD |
| `7D` | `0.1104` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 17,490.00 USD | 4,450.00 USD | 34.51 USD |
| `1D` | `0.1106` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 12,720.00 USD | 30,870.00 USD |
| `7D` | `0.1106` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 18,420.00 USD | 16,060.00 USD |
| `1D` | `0.1108` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 5,220.00 USD | 1,610.00 USD | 17,380.00 USD |
| `7D` | `0.1108` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 4,120.00 USD | 0.00 USD |
| `1D` | `0.1110` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 494.75 USD | 916.88 USD |
| `7D` | `0.1110` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 12,430.00 USD | 0.00 USD |
| `1D` | `0.1112` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 10,780.00 USD | 747.13 USD | 140.10 USD |
| `7D` | `0.1112` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 0.00 USD |
| `1D` | `0.1114` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 15,810.00 USD | 5,880.00 USD | 13,520.00 USD |
| `1D` | `0.1116` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 6,690.00 USD | 8,250.00 USD | 6,930.00 USD |
| `1D` | `0.1118` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 15,830.00 USD | 5,300.00 USD | 41,210.00 USD |
| `7D` | `0.1118` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD |
| `1D` | `0.1120` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 27,100.00 USD | 10,220.00 USD | 9,850.00 USD |
| `7D` | `0.1120` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 17,760.00 USD | 0.00 USD | 29,790.00 USD |
| `1D` | `0.1122` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 17,920.00 USD | 5,820.00 USD | 15,000.00 USD |
| `7D` | `0.1122` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 23,980.00 USD | 34,740.00 USD |
| `1D` | `0.1124` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 18,340.00 USD | 6,940.00 USD | 9,800.00 USD |
| `7D` | `0.1124` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 19,800.00 USD | 2,030.00 USD | 40,570.00 USD |
| `1D` | `0.1126` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 11,790.00 USD | 7,720.00 USD | 20,400.00 USD |
| `7D` | `0.1126` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 4,950.00 USD | 7,340.00 USD |
| `1D` | `0.1128` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 11,080.00 USD | 485.32 USD | 12,900.00 USD |
| `7D` | `0.1128` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD | 17,120.00 USD |
| `1D` | `0.1130` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 10,390.00 USD | 3,780.00 USD | 20,030.00 USD |
| `7D` | `0.1130` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,940.00 USD |
| `1D` | `0.1132` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 21,250.00 USD | 12,190.00 USD | 16,650.00 USD |
| `7D` | `0.1132` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 12,540.00 USD | 0.00 USD | 8,170.00 USD |
| `1D` | `0.1134` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 6,630.00 USD | 13,000.00 USD | 15,360.00 USD |
| `7D` | `0.1134` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 14,090.00 USD | 0.00 USD |
| `1D` | `0.1136` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 2,940.00 USD | 2,030.00 USD | 5,340.00 USD |
| `7D` | `0.1136` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 7,760.00 USD | 9,310.00 USD |
| `1D` | `0.1138` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 2,710.00 USD | 453.87 USD | 6,160.00 USD |
| `7D` | `0.1138` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,070.00 USD |
| `1D` | `0.1140` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 5,070.00 USD | 844.95 USD | 7,040.00 USD |
| `7D` | `0.1140` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 2,220.00 USD | 0.00 USD | 7,640.00 USD |
| `1D` | `0.1142` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 23,040.00 USD | 9,520.00 USD | 21,440.00 USD |
| `7D` | `0.1142` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1144` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 7,010.00 USD | 18,270.00 USD | 20,320.00 USD |
| `7D` | `0.1144` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 10,360.00 USD | 2,730.00 USD | 143,410.00 USD |
| `1D` | `0.1146` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 5,090.00 USD | 8,780.00 USD | 23,000.00 USD |
| `7D` | `0.1146` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 16,060.00 USD | 0.00 USD | 188,530.00 USD |
| `1D` | `0.1148` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 18,620.00 USD | 624.71 USD | 14,350.00 USD |
| `7D` | `0.1148` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 63,940.00 USD |
| `1D` | `0.1150` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 19,260.00 USD | 13,020.00 USD | 19,710.00 USD |
| `7D` | `0.1150` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 18,520.00 USD | 0.00 USD | 89,460.00 USD |
| `1D` | `0.1152` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 16,910.00 USD | 16,590.00 USD | 45,390.00 USD |
| `7D` | `0.1152` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 165,860.00 USD | 12,610.00 USD | 132,130.00 USD |
| `1D` | `0.1154` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 13,300.00 USD | 4,450.00 USD | 39,970.00 USD |
| `7D` | `0.1154` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 149,770.00 USD | 18,580.00 USD | 143,090.00 USD |
| `7D` | `0.1156` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 128,780.00 USD | 21,540.00 USD | 74,660.00 USD |
| `7D` | `0.1158` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 94,470.00 USD | 16,470.00 USD | 55,830.00 USD |
| `7D` | `0.1160` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 51,910.00 USD | 20,120.00 USD | 76,320.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `65.66M` | Total OI Tokens: `628,396,976.7 OP`
  * 1h OI Change: `+1.76%` | 4h OI Change: `+2.03%` | 24h OI Change: `-11.56%`
  * Exchange Breakdown: Binance=`14.25M` | Bybit=`13.02M` | OKX=`4.14M` | Hyperliquid=`3.22M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-3.06K` | Last 24h: `-4.25K` | Last 3d: `-11.30K` | Last 7d: `-13.94K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0165%` | **USDT OKX** | `-0.0292%` |
| **USDT Bybit** | `0.0054%` | **USDT KuCoin** | `-0.0054%` |
| **USDT MEXC** | `-0.0167%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `55.41%` | `44.59%` | `1.24` | 836,560.00 USD |
| `15M` | `Binance` | `52.6%` | `47.4%` | `1.11` | 302,050.00 USD |
| `15M` | `OKX` | `58.13%` | `41.87%` | `1.39` | 72,800.00 USD |
| `15M` | `Bybit` | `48.26%` | `51.74%` | `0.93` | 129,400.00 USD |
| `15M` | `KuCoin` | `55.14%` | `44.86%` | `1.23` | 32,900.00 USD |
| `15M` | `Gate` | `52.05%` | `47.95%` | `1.09` | 31,790.00 USD |
| `15M` | `Bitget` | `41.12%` | `58.88%` | `0.70` | 45,720.00 USD |
| `15M` | `BingX` | `55.19%` | `44.81%` | `1.23` | 26,070.00 USD |
| `15M` | `MEXC` | `70.11%` | `29.89%` | `2.35` | 50,340.00 USD |
| `15M` | `Bitunix` | `57.04%` | `42.96%` | `1.33` | 10,600.00 USD |
| `15M` | `Hyperliquid` | `58.05%` | `41.95%` | `1.38` | 27,640.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `55.23%` | `44.77%` | `1.23` | 44,500.00 USD |
| `15M` | `Crypto.com` | `100%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `60.47%` | `39.53%` | `1.53` | 61,240.00 USD |
| `15M` | `HTX` | `70.43%` | `29.57%` | `2.38` | 10.73 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `100%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `8.81%` | `91.19%` | `0.10` | 1,480.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `2.19%` | `97.81%` | `0.02` | 10.05 USD |
| `15M` | `Whale Positions` | `52.6%` | `47.4%` | `1.11` | 302,050.00 USD |
| `15M` | `Global Accounts` | `55.41%` | `44.59%` | `1.24` | 836,560.00 USD |
| `1H` | `OP` | `49.20%` | `50.80%` | `0.97` | 4,070,000.00 USD |
| `1H` | `Binance` | `53.61%` | `46.39%` | `1.16` | 1,210,000.00 USD |
| `1H` | `OKX` | `45.95%` | `54.05%` | `0.85` | 328,030.00 USD |
| `1H` | `Bybit` | `56.04%` | `43.96%` | `1.27` | 513,600.00 USD |
| `1H` | `KuCoin` | `51.89%` | `48.11%` | `1.08` | 448,680.00 USD |
| `1H` | `Gate` | `28.15%` | `71.85%` | `0.39` | 86,040.00 USD |
| `1H` | `Bitget` | `63.72%` | `36.28%` | `1.76` | 190,130.00 USD |
| `1H` | `BingX` | `21.54%` | `78.46%` | `0.27` | 453,200.00 USD |
| `1H` | `MEXC` | `54.64%` | `45.36%` | `1.20` | 209,750.00 USD |
| `1H` | `Bitunix` | `41.68%` | `58.32%` | `0.71` | 60,800.00 USD |
| `1H` | `Hyperliquid` | `93.61%` | `6.39%` | `14.65` | 141,540.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.15%` | `49.85%` | `1.01` | 193,550.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `28.68%` | `71.32%` | `0.40` | 225,310.00 USD |
| `1H` | `HTX` | `59.42%` | `40.58%` | `1.46` | 421.35 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `9.28%` | `90.72%` | `0.10` | 1,320.00 USD |
| `1H` | `Aster` | `90.91%` | `9.09%` | `10.00` | 3,480.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `31.71%` | `68.29%` | `0.46` | 1,440.00 USD |
| `1H` | `Whale Positions` | `53.61%` | `46.39%` | `1.16` | 1,210,000.00 USD |
| `1H` | `Global Accounts` | `49.20%` | `50.80%` | `0.97` | 4,070,000.00 USD |
| `4H` | `OP` | `50.56%` | `49.44%` | `1.02` | 13,570,000.00 USD |
| `4H` | `Binance` | `51.44%` | `48.56%` | `1.06` | 4,320,000.00 USD |
| `4H` | `OKX` | `54.41%` | `45.59%` | `1.19` | 1,840,000.00 USD |
| `4H` | `Bybit` | `49.06%` | `50.94%` | `0.96` | 1,430,000.00 USD |
| `4H` | `KuCoin` | `50.38%` | `49.62%` | `1.02` | 649,160.00 USD |
| `4H` | `Gate` | `42.46%` | `57.54%` | `0.74` | 167,150.00 USD |
| `4H` | `Bitget` | `55.51%` | `44.49%` | `1.25` | 322,860.00 USD |
| `4H` | `BingX` | `36.82%` | `63.18%` | `0.58` | 986,760.00 USD |
| `4H` | `MEXC` | `49.41%` | `50.59%` | `0.98` | 769,040.00 USD |
| `4H` | `Bitunix` | `51.62%` | `48.38%` | `1.07` | 123,670.00 USD |
| `4H` | `Hyperliquid` | `38.87%` | `61.13%` | `0.64` | 146,650.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.38%` | `47.62%` | `1.10` | 2,230,000.00 USD |
| `4H` | `Crypto.com` | `3.54%` | `96.46%` | `0.04` | 93.38 USD |
| `4H` | `WhiteBIT` | `59.98%` | `40.02%` | `1.50` | 459,990.00 USD |
| `4H` | `HTX` | `41.17%` | `58.83%` | `0.70` | 3,980.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `43.2%` | `56.8%` | `0.76` | 16,550.00 USD |
| `4H` | `Aster` | `54.28%` | `45.72%` | `1.19` | 1,910.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.48%` | `58.52%` | `0.71` | 114,690.00 USD |
| `4H` | `Whale Positions` | `51.44%` | `48.56%` | `1.06` | 4,320,000.00 USD |
| `4H` | `Global Accounts` | `50.56%` | `49.44%` | `1.02` | 13,570,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1024` | `0.1027` | `0.1024` | `0.1032` | `0.1023` | 294,713.35 USD | 140,222.38 USD | 154,490.97 USD | -14,268.58 USD | `-4.84%` | `9B / 14S` |
| `5:00 UTC` | `0.1024` | `0.1025` | `0.1024` | `0.1030` | `0.1023` | 189,660.77 USD | 110,909.31 USD | 78,751.47 USD | 32,157.84 USD | `+16.96%` | `13B / 15S` |
| `0:00 UTC` | `0.1021` | `0.1022` | `0.1021` | `0.1027` | `0.1019` | 366,904.35 USD | 146,868.15 USD | 220,036.20 USD | -73,168.05 USD | `-19.94%` | `9B / 16S` |
| `5:00 UTC` | `0.1020` | `0.1021` | `0.1020` | `0.1024` | `0.1019` | 314,873.64 USD | 167,532.45 USD | 147,341.19 USD | 20,191.27 USD | `+6.41%` | `10B / 2S` |
| `0:00 UTC` | `0.1019` | `0.1024` | `0.1019` | `0.1029` | `0.1019` | 191,273.46 USD | 92,786.86 USD | 98,486.60 USD | -5,699.74 USD | `-2.98%` | `22B / 16S` |
| `5:00 UTC` | `0.1028` | `0.1029` | `0.1028` | `0.1034` | `0.1023` | 237,952.24 USD | 133,825.41 USD | 104,126.84 USD | 29,698.57 USD | `+12.48%` | `22B / 24S` |
| `0:00 UTC` | `0.1030` | `0.1032` | `0.1030` | `0.1036` | `0.1028` | 441,050.39 USD | 212,264.29 USD | 228,786.10 USD | -16,521.82 USD | `-3.75%` | `9B / 18S` |
| `5:00 UTC` | `0.1036` | `0.1033` | `0.1036` | `0.1037` | `0.1029` | 224,777.59 USD | 109,477.97 USD | 115,299.62 USD | -5,821.65 USD | `-2.59%` | `10B / 10S` |
| `0:00 UTC` | `0.1039` | `0.1038` | `0.1039` | `0.1041` | `0.1032` | 262,943.08 USD | 122,626.50 USD | 140,316.58 USD | -17,690.08 USD | `-6.73%` | `16B / 11S` |
| `5:00 UTC` | `0.1039` | `0.1043` | `0.1039` | `0.1049` | `0.1038` | 217,991.54 USD | 126,354.74 USD | 91,636.81 USD | 34,717.93 USD | `+15.93%` | `23B / 19S` |

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
| `5m` | 5,230.00 USD | -30,740.00 USD | **`DISTRIBUTION`** |
| `15m` | 5,200.00 USD | 47,800.00 USD | **`ACCUMULATION`** |
| `30m` | 16,760.00 USD | 50,900.00 USD | **`ACCUMULATION`** |
| `1h` | -3,760.00 USD | 157,970.00 USD | **`ACCUMULATION`** |
| `2h` | -28,990.00 USD | 171,640.00 USD | **`ACCUMULATION`** |
| `4h` | -33,290.00 USD | 205,870.00 USD | **`ACCUMULATION`** |
| `6h` | -54,570.00 USD | 538,200.00 USD | **`ACCUMULATION`** |
| `8h` | -120,090.00 USD | 492,160.00 USD | **`ACCUMULATION`** |
| `12h` | -50,310.00 USD | -1,360,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 206,360.00 USD | -3,890,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -268,460.00 USD | -12,140,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,220,000.00 USD | -82,990,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+5.23K` | 15m=`+5.20K` | 1h=`-3.76K` | 24h=`+206.36K`
* Futures Capital Netflows: 5m=`-30.74K` | 15m=`+47.80K` | 1h=`+157.97K` | 24h=`-3.89M`
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
  * `2026-10-30 16:26:21 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:29:21 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)


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
