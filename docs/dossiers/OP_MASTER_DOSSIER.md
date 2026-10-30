# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 16:24:41 IST` (`2026-10-30 10:54:41 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `15m` | `0.1034` | `0.1037` | `0.1029` | `0.1032` | `2,175,357` | 224,777.59 USD | -5,821.65 USD | `-2.59%` | -1,965,822.45 USD | `-0.44` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1032` | `0.1041` | `0.1032` | `0.1040` | `2,532,549` | 262,943.08 USD | -17,690.08 USD | `-6.73%` | -1,983,512.53 USD | `-0.71` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1040` | `0.1042` | `0.1038` | `0.1042` | `844,103` | 87,785.30 USD | 32,458.20 USD | `+36.97%` | -1,951,054.33 USD | `+0.66` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.1027` | `0.1038` | `0.1023` | `0.1024` | `10,736,702` | 1,104,134.28 USD | 90,049.28 USD | `+8.16%` | -1,914,501.02 USD | `+0.40` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1024` | `0.1034` | `0.1019` | `0.1034` | `10,854,845` | 1,111,003.69 USD | -28,977.96 USD | `-2.61%` | -1,943,478.98 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1034` | `0.1043` | `0.1028` | `0.1043` | `9,826,670` | 1,016,618.93 USD | -7,512.79 USD | `-0.74%` | -1,950,991.77 USD | `+0.22` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,490,108.93 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1040` | `0.0988` | `0.1027` | `54,609,324` | 5,566,939.91 USD | 608,714.61 USD | `+10.93%` | -1,881,394.33 USD | `+1.21` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1027` | `0.1042` | `0.1019` | `0.1042` | `31,415,684` | 3,231,492.88 USD | 53,306.02 USD | `+1.65%` | -1,828,088.31 USD | `+0.47` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | 165,115.32 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -1,152,082.54 USD | `-1.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,490,108.93 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1040` | `0.0988` | `0.1027` | `54,609,324` | 5,566,939.91 USD | 608,714.61 USD | `+10.93%` | -1,881,394.33 USD | `+1.21` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1027` | `0.1042` | `0.1019` | `0.1042` | `31,415,684` | 3,231,492.88 USD | 53,306.02 USD | `+1.65%` | -1,828,088.31 USD | `+0.47` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:23:13 IST` |

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
| `7D` | `Long Liquidation` | `0.0863` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 1,880.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0865` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 1,980.00 USD | 13,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0865` | 318.30 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0867` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0869` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0871` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 1,200.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0873` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 4,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0875` | 2,420,000.00 USD | 2,420,000.00 USD | 6,010.00 USD | 0.00 USD | 4,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0875` | 793.17 USD | 6,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0877` | 2,410,000.00 USD | 2,410,000.00 USD | 7,820.00 USD | 6,050.00 USD | 22,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0879` | 2,370,000.00 USD | 2,370,000.00 USD | 1,370.00 USD | 2,010.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0881` | 2,350,000.00 USD | 2,350,000.00 USD | 9,390.00 USD | 2,270.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0883` | 2,330,000.00 USD | 2,330,000.00 USD | 7,040.00 USD | 6,800.00 USD | 21,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0885` | 2,300,000.00 USD | 2,300,000.00 USD | 1,000.00 USD | 1,220.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0887` | 2,290,000.00 USD | 2,290,000.00 USD | 10,610.00 USD | 2,920.00 USD | 17,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0889` | 2,260,000.00 USD | 2,260,000.00 USD | 10,710.00 USD | 3,200.00 USD | 13,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0891` | 2,240,000.00 USD | 2,240,000.00 USD | 6,310.00 USD | 3,960.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0893` | 2,220,000.00 USD | 2,220,000.00 USD | 5,230.00 USD | 3,080.00 USD | 5,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0895` | 2,210,000.00 USD | 2,210,000.00 USD | 4,480.00 USD | 2,110.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,270.00 USD | 5,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0897` | 2,200,000.00 USD | 2,200,000.00 USD | 4,670.00 USD | 0.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0899` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 927.82 USD | 4,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0901` | 2,190,000.00 USD | 2,190,000.00 USD | 1,250.00 USD | 428.11 USD | 17.63 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0903` | 2,190,000.00 USD | 2,190,000.00 USD | 5,330.00 USD | 1,480.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0905` | 2,180,000.00 USD | 2,180,000.00 USD | 6,050.00 USD | 0.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0905` | 2,230.00 USD | 2,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0907` | 2,170,000.00 USD | 2,170,000.00 USD | 2,780.00 USD | 2,880.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0909` | 2,160,000.00 USD | 2,160,000.00 USD | 1,180.00 USD | 2,200.00 USD | 83.37 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0911` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0913` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 74.70 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0915` | 2,150,000.00 USD | 2,150,000.00 USD | 1,670.00 USD | 903.90 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0917` | 2,050,000.00 USD | 2,050,000.00 USD | 10,440.00 USD | 5,980.00 USD | 269.80 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0917` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0919` | 2,040,000.00 USD | 2,040,000.00 USD | 8,950.00 USD | 1,090.00 USD | 19,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0919` | 2,140,000.00 USD | 2,140,000.00 USD | 7,440.00 USD | 0.00 USD | 142.43 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0921` | 2,010,000.00 USD | 2,010,000.00 USD | 758.20 USD | 2,040.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0921` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 2,030.00 USD | 80.96 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0923` | 2,000,000.00 USD | 2,000,000.00 USD | 4,040.00 USD | 6,180.00 USD | 30,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0923` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 9,670.00 USD | 43,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0925` | 1,960,000.00 USD | 1,960,000.00 USD | 6,480.00 USD | 4,210.00 USD | 27,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0925` | 2,080,000.00 USD | 2,080,000.00 USD | 1,790.00 USD | 0.00 USD | 10,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0927` | 1,920,000.00 USD | 1,920,000.00 USD | 1,820.00 USD | 2,740.00 USD | 1,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0927` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 1,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0929` | 1,920,000.00 USD | 1,920,000.00 USD | 7,820.00 USD | 1,800.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0929` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 4,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0931` | 1,910,000.00 USD | 1,910,000.00 USD | 4,040.00 USD | 1,090.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0931` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 2,240.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0933` | 1,890,000.00 USD | 1,890,000.00 USD | 16,500.00 USD | 844.95 USD | 11,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0933` | 2,050,000.00 USD | 2,050,000.00 USD | 2,220.00 USD | 0.00 USD | 154.06 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0935` | 1,860,000.00 USD | 1,860,000.00 USD | 12,610.00 USD | 7,300.00 USD | 15,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0935` | 2,040,000.00 USD | 2,040,000.00 USD | 19,560.00 USD | 6,840.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0937` | 1,830,000.00 USD | 1,830,000.00 USD | 4,580.00 USD | 6,660.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0937` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 248.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0939` | 1,800,000.00 USD | 1,800,000.00 USD | 3,590.00 USD | 2,140.00 USD | 44,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0939` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 10,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0941` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 9,410.00 USD | 21,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0941` | 1,980,000.00 USD | 1,980,000.00 USD | 14,050.00 USD | 18,340.00 USD | 76,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0943` | 1,720,000.00 USD | 1,720,000.00 USD | 3,500.00 USD | 10,920.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0943` | 1,870,000.00 USD | 1,870,000.00 USD | 6,170.00 USD | 0.00 USD | 37,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0945` | 1,680,000.00 USD | 1,680,000.00 USD | 15,750.00 USD | 6,510.00 USD | 44,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0945` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 3,820.00 USD | 89.24 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0947` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 962.66 USD | 91.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0947` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 64.98 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0949` | 1,610,000.00 USD | 1,610,000.00 USD | 12,180.00 USD | 5,770.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0949` | 1,820,000.00 USD | 1,820,000.00 USD | 3,770.00 USD | 9,700.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0951` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 2,030.00 USD | 19,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0951` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 65.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0953` | 1,570,000.00 USD | 1,570,000.00 USD | 33,000.00 USD | 4,360.00 USD | 6,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0953` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 8,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0955` | 1,520,000.00 USD | 1,520,000.00 USD | 17,990.00 USD | 14,600.00 USD | 31,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0955` | 1,780,000.00 USD | 1,780,000.00 USD | 39,120.00 USD | 13,670.00 USD | 51,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0957` | 1,460,000.00 USD | 1,460,000.00 USD | 16,340.00 USD | 6,740.00 USD | 48,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0957` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 189.85 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0959` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 3,100.00 USD | 50.26 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0959` | 1,670,000.00 USD | 1,670,000.00 USD | 28,110.00 USD | 0.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0961` | 1,380,000.00 USD | 1,380,000.00 USD | 8,920.00 USD | 23,950.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0961` | 1,620,000.00 USD | 1,620,000.00 USD | 12,340.00 USD | 16,920.00 USD | 94,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0963` | 1,330,000.00 USD | 1,330,000.00 USD | 23,240.00 USD | 11,750.00 USD | 11,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0963` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 4,020.00 USD | 205.72 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0965` | 1,280,000.00 USD | 1,280,000.00 USD | 8,250.00 USD | 5,890.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0965` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 2,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0967` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 1,960.00 USD | 863.46 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0967` | 1,490,000.00 USD | 1,490,000.00 USD | 3,770.00 USD | 0.00 USD | 2,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0969` | 1,240,000.00 USD | 1,240,000.00 USD | 6,930.00 USD | 7,530.00 USD | 8,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0969` | 1,480,000.00 USD | 1,480,000.00 USD | 3,720.00 USD | 7,090.00 USD | 61,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0971` | 1,220,000.00 USD | 1,220,000.00 USD | 2,840.00 USD | 4,070.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0973` | 1,200,000.00 USD | 1,200,000.00 USD | 1,440.00 USD | 10,220.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0973` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0975` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 114.54 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0975` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 253.26 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0977` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 765.93 USD | 978.56 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0979` | 1,190,000.00 USD | 1,190,000.00 USD | 5,180.00 USD | 2,920.00 USD | 21,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0981` | 1,160,000.00 USD | 1,160,000.00 USD | 12,740.00 USD | 7,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0981` | 1,400,000.00 USD | 1,400,000.00 USD | 22,280.00 USD | 5,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0983` | 1,140,000.00 USD | 1,140,000.00 USD | 11,130.00 USD | 16,910.00 USD | 10,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 8,770.00 USD | 11,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0985` | 1,100,000.00 USD | 1,100,000.00 USD | 5,970.00 USD | 8,750.00 USD | 12,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0985` | 1,350,000.00 USD | 1,350,000.00 USD | 5,330.00 USD | 16,370.00 USD | 90.68 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0987` | 1,070,000.00 USD | 1,070,000.00 USD | 30,280.00 USD | 7,610.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0987` | 1,330,000.00 USD | 1,330,000.00 USD | 5,390.00 USD | 15,350.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0989` | 1,020,000.00 USD | 1,020,000.00 USD | 8,920.00 USD | 10,380.00 USD | 24,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 1,300,000.00 USD | 1,300,000.00 USD | 20,710.00 USD | 3,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0991` | 975,740.00 USD | 975,740.00 USD | 79,410.00 USD | 1,530.00 USD | 4,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0991` | 1,270,000.00 USD | 1,270,000.00 USD | 14,350.00 USD | 5,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0993` | 889,950.00 USD | 889,950.00 USD | 33,340.00 USD | 7,220.00 USD | 45,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0993` | 1,260,000.00 USD | 1,260,000.00 USD | 63,040.00 USD | 9,430.00 USD | 50,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0995` | 803,540.00 USD | 803,540.00 USD | 16,240.00 USD | 3,010.00 USD | 50,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 1,130,000.00 USD | 1,130,000.00 USD | 18,620.00 USD | 0.00 USD | 25,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0997` | 733,810.00 USD | 733,810.00 USD | 26,940.00 USD | 7,370.00 USD | 58,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0997` | 1,090,000.00 USD | 1,090,000.00 USD | 27,750.00 USD | 11,200.00 USD | 32,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0999` | 640,820.00 USD | 640,820.00 USD | 0.00 USD | 11,820.00 USD | 47,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0999` | 1,020,000.00 USD | 1,020,000.00 USD | 42,340.00 USD | 11,480.00 USD | 104,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1001` | 581,120.00 USD | 581,120.00 USD | 25,400.00 USD | 4,200.00 USD | 42,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 857,780.00 USD | 857,780.00 USD | 86,120.00 USD | 19,930.00 USD | 105,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1003` | 509,010.00 USD | 509,010.00 USD | 37,160.00 USD | 10,200.00 USD | 27,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1003` | 645,990.00 USD | 645,990.00 USD | 8,010.00 USD | 10,130.00 USD | 27,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1005` | 434,450.00 USD | 434,450.00 USD | 31,310.00 USD | 43,010.00 USD | 66,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1005` | 599,950.00 USD | 599,950.00 USD | 35,740.00 USD | 40,720.00 USD | 63,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1007` | 294,130.00 USD | 294,130.00 USD | 21,860.00 USD | 7,380.00 USD | 8,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 459,780.00 USD | 459,780.00 USD | 10,260.00 USD | 3,080.00 USD | 68,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1009` | 256,260.00 USD | 256,260.00 USD | 20,400.00 USD | 17,660.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1009` | 378,300.00 USD | 378,300.00 USD | 32,230.00 USD | 17,090.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1011` | 212,600.00 USD | 212,600.00 USD | 18,940.00 USD | 7,120.00 USD | 25,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1011` | 274,960.00 USD | 274,960.00 USD | 4,430.00 USD | 15,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1013` | 161,090.00 USD | 161,090.00 USD | 21,860.00 USD | 8,400.00 USD | 18,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 255,390.00 USD | 255,390.00 USD | 32,420.00 USD | 46,040.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1015` | 112,680.00 USD | 112,680.00 USD | 4,580.00 USD | 5,450.00 USD | 20,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1015` | 151,480.00 USD | 151,480.00 USD | 17,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1017` | 82,450.00 USD | 82,450.00 USD | 10,050.00 USD | 0.00 USD | 15,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1017` | 133,570.00 USD | 133,570.00 USD | 11,450.00 USD | 0.00 USD | 10,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1019` | 56,660.00 USD | 56,660.00 USD | 11,630.00 USD | 1,550.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1019` | 111,490.00 USD | 111,490.00 USD | 36,610.00 USD | 8,460.00 USD | 9,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1021` | 41,760.00 USD | 41,760.00 USD | 0.00 USD | 0.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1021` | 56,440.00 USD | 56,440.00 USD | 0.00 USD | 0.00 USD | 37,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1023` | 27,870.00 USD | 27,870.00 USD | 0.00 USD | 0.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1033` | 18,990.00 USD | 18,990.00 USD | 13,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1035` | 5,810.00 USD | 5,810.00 USD | 0.00 USD | 0.00 USD | 108.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1037` | 24,150.00 USD | 24,150.00 USD | 2,150.00 USD | 12,850.00 USD | 24.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1037` | 5,700.00 USD | 5,700.00 USD | 0.00 USD | 5,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1039` | 9,120.00 USD | 9,120.00 USD | 0.00 USD | 9,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1039` | 38,750.00 USD | 38,750.00 USD | 0.00 USD | 7,400.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1039` | 77,500.00 USD | 77,500.00 USD | 0.00 USD | 7,400.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1041` | 56,410.00 USD | 56,410.00 USD | 20,110.00 USD | 16,680.00 USD | 19,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1041` | 124,960.00 USD | 124,960.00 USD | 44,560.00 USD | 2,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1043` | 113,110.00 USD | 113,110.00 USD | 13,920.00 USD | 18,610.00 USD | 24,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1043` | 179,740.00 USD | 179,740.00 USD | 15,960.00 USD | 16,120.00 USD | 22,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1045` | 168,610.00 USD | 168,610.00 USD | 12,990.00 USD | 21,860.00 USD | 20,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1045` | 209,500.00 USD | 209,500.00 USD | 0.00 USD | 29,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1047` | 282,300.00 USD | 282,300.00 USD | 40,510.00 USD | 22,900.00 USD | 50,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1047` | 312,750.00 USD | 312,750.00 USD | 10,670.00 USD | 24,890.00 USD | 67,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1049` | 404,940.00 USD | 404,940.00 USD | 35,540.00 USD | 20,260.00 USD | 66,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1049` | 441,380.00 USD | 441,380.00 USD | 34,790.00 USD | 4,810.00 USD | 89,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1051` | 465,260.00 USD | 465,260.00 USD | 32,010.00 USD | 21,250.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1051` | 526,330.00 USD | 526,330.00 USD | 34,200.00 USD | 15,780.00 USD | 34,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1053` | 554,330.00 USD | 554,330.00 USD | 32,610.00 USD | 8,780.00 USD | 47,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1053` | 715,800.00 USD | 715,800.00 USD | 53,590.00 USD | 40,230.00 USD | 95,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1055` | 670,610.00 USD | 670,610.00 USD | 51,550.00 USD | 21,730.00 USD | 43,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1055` | 1,040,000.00 USD | 1,040,000.00 USD | 80,160.00 USD | 46,150.00 USD | 193,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1057` | 732,530.00 USD | 732,530.00 USD | 14,080.00 USD | 16,120.00 USD | 31,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1057` | 1,260,000.00 USD | 1,260,000.00 USD | 61,450.00 USD | 47,740.00 USD | 110,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1059` | 842,060.00 USD | 842,060.00 USD | 30,300.00 USD | 5,730.00 USD | 73,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1059` | 1,510,000.00 USD | 1,510,000.00 USD | 77,800.00 USD | 51,220.00 USD | 123,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1061` | 924,210.00 USD | 924,210.00 USD | 42,730.00 USD | 4,800.00 USD | 34,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1061` | 1,660,000.00 USD | 1,660,000.00 USD | 45,510.00 USD | 27,410.00 USD | 76,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1063` | 1,010,000.00 USD | 1,010,000.00 USD | 34,110.00 USD | 4,070.00 USD | 50,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1063` | 1,870,000.00 USD | 1,870,000.00 USD | 22,280.00 USD | 43,390.00 USD | 149,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1065` | 1,080,000.00 USD | 1,080,000.00 USD | 12,870.00 USD | 15,500.00 USD | 35,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1065` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 24,310.00 USD | 99,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1067` | 1,150,000.00 USD | 1,150,000.00 USD | 14,200.00 USD | 10,080.00 USD | 44,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1067` | 2,150,000.00 USD | 2,150,000.00 USD | 5,330.00 USD | 60,270.00 USD | 83,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1069` | 1,220,000.00 USD | 1,220,000.00 USD | 23,520.00 USD | 9,120.00 USD | 43,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1069` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 31,620.00 USD | 98,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1071` | 1,250,000.00 USD | 1,250,000.00 USD | 9,290.00 USD | 11,540.00 USD | 8,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1071` | 2,380,000.00 USD | 2,380,000.00 USD | 16,280.00 USD | 32,350.00 USD | 52,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1073` | 1,270,000.00 USD | 1,270,000.00 USD | 9,470.00 USD | 1,530.00 USD | 9,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1073` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 22,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1075` | 1,300,000.00 USD | 1,300,000.00 USD | 12,370.00 USD | 5,060.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1075` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 9,430.00 USD | 22,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1077` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 2,730.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1077` | 2,440,000.00 USD | 2,440,000.00 USD | 11,160.00 USD | 0.00 USD | 332.62 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1079` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 4,300.00 USD | 23,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1079` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 3,380.00 USD | 9,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1081` | 1,350,000.00 USD | 1,350,000.00 USD | 13,690.00 USD | 732.74 USD | 4,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1081` | 2,460,000.00 USD | 2,460,000.00 USD | 6,650.00 USD | 0.00 USD | 89.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1083` | 1,380,000.00 USD | 1,380,000.00 USD | 9,160.00 USD | 6,710.00 USD | 10,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1083` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 64.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1085` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 385.06 USD | 65,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1085` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1087` | 1,520,000.00 USD | 1,520,000.00 USD | 28,490.00 USD | 2,510.00 USD | 44,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1087` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1089` | 1,550,000.00 USD | 1,550,000.00 USD | 29,650.00 USD | 1,580.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1089` | 2,480,000.00 USD | 2,480,000.00 USD | 5,290.00 USD | 1,420.00 USD | 204.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1091` | 1,580,000.00 USD | 1,580,000.00 USD | 33,700.00 USD | 0.00 USD | 16.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1091` | 2,510,000.00 USD | 2,510,000.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1093` | 1,600,000.00 USD | 1,600,000.00 USD | 15,480.00 USD | 1,080.00 USD | 272.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1093` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 1,500.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1095` | 1,630,000.00 USD | 1,630,000.00 USD | 4,110.00 USD | 1,890.00 USD | 21,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1095` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 189.85 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1097` | 1,660,000.00 USD | 1,660,000.00 USD | 7,260.00 USD | 2,530.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1097` | 2,540,000.00 USD | 2,540,000.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1099` | 1,670,000.00 USD | 1,670,000.00 USD | 6,130.00 USD | 1,940.00 USD | 32.38 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1099` | 2,570,000.00 USD | 2,570,000.00 USD | 11,470.00 USD | 0.00 USD | 21,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1101` | 1,680,000.00 USD | 1,680,000.00 USD | 5,570.00 USD | 3,820.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1101` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1103` | 1,700,000.00 USD | 1,700,000.00 USD | 3,540.00 USD | 6,900.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 2,610,000.00 USD | 2,610,000.00 USD | 17,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1105` | 1,710,000.00 USD | 1,710,000.00 USD | 3,380.00 USD | 4,740.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1105` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 14,480.00 USD | 246.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1107` | 1,770,000.00 USD | 1,770,000.00 USD | 3,110.00 USD | 13,200.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1107` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 12,510.00 USD | 15,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1109` | 1,770,000.00 USD | 1,770,000.00 USD | 2,110.00 USD | 1,370.00 USD | 2,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 12,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1111` | 1,780,000.00 USD | 1,780,000.00 USD | 5,200.00 USD | 996.46 USD | 104.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1111` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1113` | 1,820,000.00 USD | 1,820,000.00 USD | 21,390.00 USD | 5,880.00 USD | 13,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1115` | 1,830,000.00 USD | 1,830,000.00 USD | 6,690.00 USD | 465.26 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1115` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 28.89 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1115` | 1,880.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1117` | 1,860,000.00 USD | 1,860,000.00 USD | 2,060.00 USD | 10,810.00 USD | 24,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1117` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 22,780.00 USD | 16,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1119` | 1,920,000.00 USD | 1,920,000.00 USD | 23,420.00 USD | 4,920.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1119` | 2,780,000.00 USD | 2,780,000.00 USD | 34,550.00 USD | 7,050.00 USD | 21,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1121` | 1,970,000.00 USD | 1,970,000.00 USD | 21,300.00 USD | 12,810.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 2,810,000.00 USD | 2,810,000.00 USD | 5,730.00 USD | 0.00 USD | 27,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1123` | 2,010,000.00 USD | 2,010,000.00 USD | 30,640.00 USD | 2,870.00 USD | 8,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1123` | 2,890,000.00 USD | 2,890,000.00 USD | 19,800.00 USD | 23,980.00 USD | 37,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1125` | 2,040,000.00 USD | 2,040,000.00 USD | 11,890.00 USD | 8,250.00 USD | 11,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1125` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 4,250.00 USD | 36,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1127` | 2,070,000.00 USD | 2,070,000.00 USD | 1,670.00 USD | 4,120.00 USD | 22,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1127` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 2,720.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1129` | 2,090,000.00 USD | 2,090,000.00 USD | 11,080.00 USD | 1,390.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1129` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 2,020.00 USD | 9,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1131` | 2,150,000.00 USD | 2,150,000.00 USD | 24,040.00 USD | 6,440.00 USD | 24,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1131` | 3,000,000.00 USD | 3,000,000.00 USD | 12,540.00 USD | 0.00 USD | 25,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1133` | 2,200,000.00 USD | 2,200,000.00 USD | 8,350.00 USD | 19,820.00 USD | 24,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 12,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1135` | 2,220,000.00 USD | 2,220,000.00 USD | 7,500.00 USD | 3,200.00 USD | 5,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1135` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 6,800.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1137` | 2,220,000.00 USD | 2,220,000.00 USD | 4,040.00 USD | 1,090.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1137` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 2,240.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1139` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 844.95 USD | 5,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1139` | 3,040,000.00 USD | 3,040,000.00 USD | 2,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1141` | 2,260,000.00 USD | 2,260,000.00 USD | 8,110.00 USD | 0.00 USD | 21,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1141` | 3,060,000.00 USD | 3,060,000.00 USD | 10,380.00 USD | 0.00 USD | 7,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1143` | 2,310,000.00 USD | 2,310,000.00 USD | 22,320.00 USD | 22,390.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1143` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 78,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1145` | 2,350,000.00 USD | 2,350,000.00 USD | 9,770.00 USD | 6,840.00 USD | 23,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 3,290,000.00 USD | 3,290,000.00 USD | 16,540.00 USD | 2,730.00 USD | 141,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1147` | 2,380,000.00 USD | 2,380,000.00 USD | 3,840.00 USD | 7,350.00 USD | 18,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1147` | 3,440,000.00 USD | 3,440,000.00 USD | 9,880.00 USD | 0.00 USD | 138,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1148` | 2,400,000.00 USD | 2,400,000.00 USD | 14,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1149` | 3,530,000.00 USD | 3,530,000.00 USD | 10,560.00 USD | 0.00 USD | 72,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 3,750,000.00 USD | 3,750,000.00 USD | 92,570.00 USD | 4,210.00 USD | 128,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1153` | 4,040,000.00 USD | 4,040,000.00 USD | 136,660.00 USD | 8,400.00 USD | 146,040.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.0285` | 122,680.00 USD | 0.00 USD | 171.00 USD | `-72.34%` | `6,000.00` |
| `Live` | `Long` | `0.0305` | 122,510.00 USD | 0.00 USD | 1,320.00 USD | `-70.40%` | `43,265.90` |
| `Live` | `Long` | `0.0485` | 121,190.00 USD | 0.00 USD | 247.30 USD | `-52.93%` | `5,098.90` |
| `Live` | `Long` | `0.0565` | 120,950.00 USD | 0.00 USD | 433.00 USD | `-45.17%` | `7,663.80` |
| `Live` | `Long` | `0.0585` | 120,510.00 USD | 0.00 USD | 844.12 USD | `-43.23%` | `14,429.40` |
| `Live` | `Long` | `0.0605` | 119,670.00 USD | 0.00 USD | 4,220.00 USD | `-41.28%` | `69,790.10` |
| `Live` | `Long` | `0.0615` | 115,450.00 USD | 0.00 USD | 315.09 USD | `-40.31%` | `5,123.40` |
| `Live` | `Long` | `0.0645` | 115,130.00 USD | 0.00 USD | 353.81 USD | `-37.40%` | `5,485.40` |
| `Live` | `Long` | `0.0675` | 114,780.00 USD | 0.00 USD | 518.48 USD | `-34.49%` | `7,681.20` |
| `Live` | `Long` | `0.0685` | 114,260.00 USD | 0.00 USD | 1,920.00 USD | `-33.52%` | `28,000.00` |
| `Live` | `Long` | `0.0705` | 112,340.00 USD | 0.00 USD | 1,090.00 USD | `-31.58%` | `15,500.00` |
| `Live` | `Long` | `0.0715` | 111,250.00 USD | 0.00 USD | 40,420.00 USD | `-30.61%` | `565,287.50` |
| `Live` | `Long` | `0.0725` | 70,830.00 USD | 0.00 USD | 23,910.00 USD | `-29.64%` | `329,855.60` |
| `Live` | `Long` | `0.0735` | 46,920.00 USD | 0.00 USD | 2,530.00 USD | `-28.67%` | `34,439.60` |
| `Live` | `Long` | `0.0745` | 44,390.00 USD | 0.00 USD | 2,300.00 USD | `-27.70%` | `30,851.90` |
| `Live` | `Long` | `0.0755` | 42,090.00 USD | 0.00 USD | 12,440.00 USD | `-26.73%` | `164,709.50` |
| `Live` | `Long` | `0.0765` | 29,650.00 USD | 0.00 USD | 1,170.00 USD | `-25.76%` | `15,263.30` |
| `Live` | `Long` | `0.0775` | 28,480.00 USD | 0.00 USD | 878.62 USD | `-24.79%` | `11,337.00` |
| `Live` | `Long` | `0.0785` | 27,600.00 USD | 0.00 USD | 339.50 USD | `-23.82%` | `4,324.80` |
| `Live` | `Long` | `0.0795` | 27,270.00 USD | 0.00 USD | 2,710.00 USD | `-22.85%` | `34,073.20` |
| `Live` | `Long` | `0.0805` | 24,560.00 USD | 0.00 USD | 223.98 USD | `-21.88%` | `2,782.40` |
| `Live` | `Long` | `0.0815` | 24,330.00 USD | 0.00 USD | 1,560.00 USD | `-20.90%` | `19,181.40` |
| `Live` | `Long` | `0.0825` | 22,770.00 USD | 0.00 USD | 140.74 USD | `-19.93%` | `1,705.90` |
| `Live` | `Long` | `0.0845` | 22,630.00 USD | 0.00 USD | 14,300.00 USD | `-17.99%` | `169,238.60` |
| `Live` | `Long` | `0.0855` | 8,330.00 USD | 0.00 USD | 1,710.00 USD | `-17.02%` | `20,000.00` |
| `Live` | `Long` | `0.0865` | 6,620.00 USD | 0.00 USD | 318.30 USD | `-16.05%` | `3,679.80` |
| `Live` | `Long` | `0.0875` | 6,300.00 USD | 0.00 USD | 793.17 USD | `-15.08%` | `9,064.80` |
| `Live` | `Long` | `0.0895` | 5,510.00 USD | 0.00 USD | 3,270.00 USD | `-13.14%` | `36,562.50` |
| `Live` | `Long` | `0.0905` | 2,230.00 USD | 0.00 USD | 2,230.00 USD | `-12.17%` | `24,685.10` |
| `Live` | `Short` | `0.1115` | 1,880.00 USD | 1,880.00 USD | 0.00 USD | `+8.21%` | `16,853.90` |
| `Live` | `Short` | `0.1185` | 5,190.00 USD | 3,310.00 USD | 0.00 USD | `+15.00%` | `27,930.30` |
| `Live` | `Short` | `0.1225` | 5,910.00 USD | 721.08 USD | 0.00 USD | `+18.89%` | `5,886.40` |
| `Live` | `Short` | `0.1375` | 27,860.00 USD | 21,950.00 USD | 0.00 USD | `+33.44%` | `159,649.00` |
| `Live` | `Short` | `0.1415` | 31,670.00 USD | 3,800.00 USD | 0.00 USD | `+37.33%` | `26,889.40` |
| `Live` | `Short` | `0.1495` | 53,490.00 USD | 21,820.00 USD | 0.00 USD | `+45.09%` | `145,985.00` |
| `Live` | `Short` | `0.1525` | 59,580.00 USD | 6,090.00 USD | 0.00 USD | `+48.00%` | `39,929.50` |
| `Live` | `Short` | `0.1565` | 60,130.00 USD | 550.61 USD | 0.00 USD | `+51.88%` | `3,518.30` |
| `Live` | `Short` | `0.1615` | 60,390.00 USD | 254.17 USD | 0.00 USD | `+56.74%` | `1,573.80` |
| `Live` | `Short` | `0.1695` | 60,550.00 USD | 169.25 USD | 0.00 USD | `+64.50%` | `998.50` |
| `Live` | `Short` | `0.1745` | 60,690.00 USD | 131.08 USD | 0.00 USD | `+69.35%` | `751.20` |
| `Live` | `Short` | `0.1755` | 60,830.00 USD | 147.21 USD | 0.00 USD | `+70.32%` | `838.80` |
| `Live` | `Short` | `0.1815` | 60,930.00 USD | 102.00 USD | 0.00 USD | `+76.15%` | `562.00` |
| `Live` | `Short` | `0.1825` | 61,450.00 USD | 514.28 USD | 0.00 USD | `+77.12%` | `2,818.00` |
| `Live` | `Short` | `0.1855` | 61,620.00 USD | 166.95 USD | 0.00 USD | `+80.03%` | `900.00` |
| `Live` | `Short` | `0.1865` | 61,820.00 USD | 199.93 USD | 0.00 USD | `+81.00%` | `1,072.00` |
| `Live` | `Short` | `0.2065` | 62,810.00 USD | 998.16 USD | 0.00 USD | `+100.41%` | `4,833.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0635` | 35,080.00 USD | 0.00 USD | 1,140.00 USD | `-38.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 33,940.00 USD | 0.00 USD | 773.46 USD | `-31.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 33,170.00 USD | 0.00 USD | 592.27 USD | `-30.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 32,580.00 USD | 0.00 USD | 755.00 USD | `-26.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0805` | 31,820.00 USD | 0.00 USD | 411.06 USD | `-21.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0815` | 31,410.00 USD | 0.00 USD | 285.01 USD | `-20.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0835` | 31,120.00 USD | 0.00 USD | 456.70 USD | `-18.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0845` | 30,670.00 USD | 0.00 USD | 171.09 USD | `-17.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 30,500.00 USD | 0.00 USD | 631.58 USD | `-17.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 29,860.00 USD | 0.00 USD | 380.89 USD | `-16.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 29,480.00 USD | 0.00 USD | 782.05 USD | `-14.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 28,700.00 USD | 0.00 USD | 444.62 USD | `-12.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0915` | 28,260.00 USD | 0.00 USD | 623.91 USD | `-11.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 27,630.00 USD | 0.00 USD | 485.13 USD | `-8.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0965` | 27,150.00 USD | 0.00 USD | 5,700.00 USD | `-6.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0975` | 21,450.00 USD | 0.00 USD | 216.41 USD | `-5.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0985` | 21,230.00 USD | 0.00 USD | 144.62 USD | `-4.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0995` | 21,090.00 USD | 0.00 USD | 17,230.00 USD | `-3.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 3,860.00 USD | 0.00 USD | 2,180.00 USD | `-2.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1015` | 1,680.00 USD | 0.00 USD | 903.42 USD | `-1.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 780.70 USD | 0.00 USD | 780.70 USD | `-0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1035` | 1,640.00 USD | 1,640.00 USD | 0.00 USD | `+0.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 1,750.00 USD | 105.53 USD | 0.00 USD | `+1.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 1,980.00 USD | 227.76 USD | 0.00 USD | `+2.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 111,260.00 USD | 109,280.00 USD | 0.00 USD | `+3.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1075` | 111,730.00 USD | 473.35 USD | 0.00 USD | `+4.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1095` | 130,350.00 USD | 18,610.00 USD | 0.00 USD | `+6.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 130,510.00 USD | 160.20 USD | 0.00 USD | `+7.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 130,750.00 USD | 247.49 USD | 0.00 USD | `+8.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1125` | 131,540.00 USD | 786.65 USD | 0.00 USD | `+9.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1135` | 131,660.00 USD | 116.27 USD | 0.00 USD | `+10.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 131,800.00 USD | 137.71 USD | 0.00 USD | `+12.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1165` | 131,980.00 USD | 180.81 USD | 0.00 USD | `+13.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1175` | 132,340.00 USD | 363.49 USD | 0.00 USD | `+14.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1185` | 132,610.00 USD | 265.74 USD | 0.00 USD | `+15.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1195` | 147,240.00 USD | 14,640.00 USD | 0.00 USD | `+15.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1225` | 148,220.00 USD | 980.00 USD | 0.00 USD | `+18.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1235` | 155,590.00 USD | 7,370.00 USD | 0.00 USD | `+19.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1255` | 159,960.00 USD | 4,380.00 USD | 0.00 USD | `+21.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1315` | 191,530.00 USD | 31,560.00 USD | 0.00 USD | `+27.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1335` | 192,840.00 USD | 1,310.00 USD | 0.00 USD | `+29.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1345` | 196,990.00 USD | 4,150.00 USD | 0.00 USD | `+30.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1365` | 204,740.00 USD | 7,750.00 USD | 0.00 USD | `+32.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1405` | 217,850.00 USD | 13,110.00 USD | 0.00 USD | `+36.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1425` | 217,950.00 USD | 102.22 USD | 0.00 USD | `+38.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1435` | 225,120.00 USD | 7,180.00 USD | 0.00 USD | `+39.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1485` | 227,770.00 USD | 2,650.00 USD | 0.00 USD | `+44.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1525` | 231,540.00 USD | 3,770.00 USD | 0.00 USD | `+48.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 231,720.00 USD | 184.49 USD | 0.00 USD | `+50.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 234,530.00 USD | 2,810.00 USD | 0.00 USD | `+51.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 234,750.00 USD | 219.81 USD | 0.00 USD | `+52.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 235,030.00 USD | 277.62 USD | 0.00 USD | `+58.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 237,060.00 USD | 2,030.00 USD | 0.00 USD | `+64.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 237,270.00 USD | 216.55 USD | 0.00 USD | `+69.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 237,390.00 USD | 117.26 USD | 0.00 USD | `+91.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 257,920.00 USD | 20,530.00 USD | 0.00 USD | `+94.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 258,110.00 USD | 189.30 USD | 0.00 USD | `+97.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 258,330.00 USD | 219.22 USD | 0.00 USD | `+98.47%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0863` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 0.00 USD | 1,880.00 USD | 7,040.00 USD |
| `7D` | `0.0865` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 0.00 USD | 1,980.00 USD | 13,330.00 USD |
| `7D` | `0.0867` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 2,070.00 USD |
| `7D` | `0.0869` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 2,900.00 USD |
| `7D` | `0.0871` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 0.00 USD | 1,200.00 USD | 2,850.00 USD |
| `7D` | `0.0873` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 4,480.00 USD |
| `7D` | `0.0875` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 6,010.00 USD | 0.00 USD | 4,270.00 USD |
| `7D` | `0.0877` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 7,820.00 USD | 6,050.00 USD | 22,770.00 USD |
| `7D` | `0.0879` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 1,370.00 USD | 2,010.00 USD | 13,390.00 USD |
| `7D` | `0.0881` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 9,390.00 USD | 2,270.00 USD | 5,500.00 USD |
| `7D` | `0.0883` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 7,040.00 USD | 6,800.00 USD | 21,710.00 USD |
| `7D` | `0.0885` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 1,000.00 USD | 1,220.00 USD | 2,070.00 USD |
| `7D` | `0.0887` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 10,610.00 USD | 2,920.00 USD | 17,560.00 USD |
| `7D` | `0.0889` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 10,710.00 USD | 3,200.00 USD | 13,140.00 USD |
| `7D` | `0.0891` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 6,310.00 USD | 3,960.00 USD | 2,080.00 USD |
| `7D` | `0.0893` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 5,230.00 USD | 3,080.00 USD | 5,100.00 USD |
| `7D` | `0.0895` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 4,480.00 USD | 2,110.00 USD | 5,490.00 USD |
| `7D` | `0.0897` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 4,670.00 USD | 0.00 USD | 1,390.00 USD |
| `7D` | `0.0899` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 0.00 USD | 927.82 USD | 4,510.00 USD |
| `7D` | `0.0901` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 1,250.00 USD | 428.11 USD | 17.63 USD |
| `7D` | `0.0903` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 5,330.00 USD | 1,480.00 USD | 2,870.00 USD |
| `7D` | `0.0905` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 6,050.00 USD | 0.00 USD | 2,610.00 USD |
| `7D` | `0.0907` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 2,780.00 USD | 2,880.00 USD | 2,920.00 USD |
| `7D` | `0.0909` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 1,180.00 USD | 2,200.00 USD | 83.37 USD |
| `7D` | `0.0911` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD |
| `7D` | `0.0913` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 74.70 USD |
| `7D` | `0.0915` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 1,670.00 USD | 903.90 USD | 0.00 USD |
| `1D` | `0.0917` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 10,440.00 USD | 5,980.00 USD | 269.80 USD |
| `7D` | `0.0917` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 8,050.00 USD |
| `1D` | `0.0919` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 8,950.00 USD | 1,090.00 USD | 19,100.00 USD |
| `7D` | `0.0919` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 7,440.00 USD | 0.00 USD | 142.43 USD |
| `1D` | `0.0921` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 758.20 USD | 2,040.00 USD | 3,820.00 USD |
| `7D` | `0.0921` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 0.00 USD | 2,030.00 USD | 80.96 USD |
| `1D` | `0.0923` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 4,040.00 USD | 6,180.00 USD | 30,020.00 USD |
| `7D` | `0.0923` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 0.00 USD | 9,670.00 USD | 43,930.00 USD |
| `1D` | `0.0925` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 6,480.00 USD | 4,210.00 USD | 27,920.00 USD |
| `7D` | `0.0925` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 1,790.00 USD | 0.00 USD | 10,860.00 USD |
| `1D` | `0.0927` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 1,820.00 USD | 2,740.00 USD | 1,130.00 USD |
| `7D` | `0.0927` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 0.00 USD | 1,390.00 USD | 0.00 USD |
| `1D` | `0.0929` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 7,820.00 USD | 1,800.00 USD | 1,320.00 USD |
| `7D` | `0.0929` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 0.00 USD | 4,360.00 USD | 0.00 USD |
| `1D` | `0.0931` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 4,040.00 USD | 1,090.00 USD | 8,520.00 USD |
| `7D` | `0.0931` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 0.00 USD | 2,240.00 USD | 12,180.00 USD |
| `1D` | `0.0933` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 16,500.00 USD | 844.95 USD | 11,780.00 USD |
| `7D` | `0.0933` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 2,220.00 USD | 0.00 USD | 154.06 USD |
| `1D` | `0.0935` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 12,610.00 USD | 7,300.00 USD | 15,690.00 USD |
| `7D` | `0.0935` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 19,560.00 USD | 6,840.00 USD | 25,450.00 USD |
| `1D` | `0.0937` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 4,580.00 USD | 6,660.00 USD | 13,310.00 USD |
| `7D` | `0.0937` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 248.29 USD |
| `1D` | `0.0939` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 3,590.00 USD | 2,140.00 USD | 44,370.00 USD |
| `7D` | `0.0939` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 10,640.00 USD |
| `1D` | `0.0941` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 0.00 USD | 9,410.00 USD | 21,110.00 USD |
| `7D` | `0.0941` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 14,050.00 USD | 18,340.00 USD | 76,650.00 USD |
| `1D` | `0.0943` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 3,500.00 USD | 10,920.00 USD | 30,420.00 USD |
| `7D` | `0.0943` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 6,170.00 USD | 0.00 USD | 37,530.00 USD |
| `1D` | `0.0945` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 15,750.00 USD | 6,510.00 USD | 44,380.00 USD |
| `7D` | `0.0945` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 0.00 USD | 3,820.00 USD | 89.24 USD |
| `1D` | `0.0947` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 0.00 USD | 962.66 USD | 91.75 USD |
| `7D` | `0.0947` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 64.98 USD |
| `1D` | `0.0949` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 12,180.00 USD | 5,770.00 USD | 2,940.00 USD |
| `7D` | `0.0949` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 3,770.00 USD | 9,700.00 USD | 26,990.00 USD |
| `1D` | `0.0951` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 0.00 USD | 2,030.00 USD | 19,990.00 USD |
| `7D` | `0.0951` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 65.29 USD |
| `1D` | `0.0953` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 33,000.00 USD | 4,360.00 USD | 6,780.00 USD |
| `7D` | `0.0953` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 0.00 USD | 8,150.00 USD | 0.00 USD |
| `1D` | `0.0955` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 17,990.00 USD | 14,600.00 USD | 31,680.00 USD |
| `7D` | `0.0955` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 39,120.00 USD | 13,670.00 USD | 51,090.00 USD |
| `1D` | `0.0957` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 16,340.00 USD | 6,740.00 USD | 48,740.00 USD |
| `7D` | `0.0957` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 189.85 USD |
| `1D` | `0.0959` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 0.00 USD | 3,100.00 USD | 50.26 USD |
| `7D` | `0.0959` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 28,110.00 USD | 0.00 USD | 21,370.00 USD |
| `1D` | `0.0961` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 8,920.00 USD | 23,950.00 USD | 23,330.00 USD |
| `7D` | `0.0961` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 12,340.00 USD | 16,920.00 USD | 94,930.00 USD |
| `1D` | `0.0963` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 23,240.00 USD | 11,750.00 USD | 11,980.00 USD |
| `7D` | `0.0963` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 0.00 USD | 4,020.00 USD | 205.72 USD |
| `1D` | `0.0965` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 8,250.00 USD | 5,890.00 USD | 20,440.00 USD |
| `7D` | `0.0965` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 0.00 USD | 2,390.00 USD | 0.00 USD |
| `1D` | `0.0967` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 0.00 USD | 1,960.00 USD | 863.46 USD |
| `7D` | `0.0967` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 3,770.00 USD | 0.00 USD | 2,990.00 USD |
| `1D` | `0.0969` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 6,930.00 USD | 7,530.00 USD | 8,080.00 USD |
| `7D` | `0.0969` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 3,720.00 USD | 7,090.00 USD | 61,090.00 USD |
| `1D` | `0.0971` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 2,840.00 USD | 4,070.00 USD | 10,240.00 USD |
| `1D` | `0.0973` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 1,440.00 USD | 10,220.00 USD | 1,980.00 USD |
| `7D` | `0.0973` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD |
| `1D` | `0.0975` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 114.54 USD |
| `7D` | `0.0975` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 253.26 USD |
| `1D` | `0.0977` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 765.93 USD | 978.56 USD |
| `1D` | `0.0979` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 5,180.00 USD | 2,920.00 USD | 21,150.00 USD |
| `1D` | `0.0981` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 12,740.00 USD | 7,060.00 USD | 0.00 USD |
| `7D` | `0.0981` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 22,280.00 USD | 5,070.00 USD | 0.00 USD |
| `1D` | `0.0983` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 11,130.00 USD | 16,910.00 USD | 10,320.00 USD |
| `7D` | `0.0983` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 0.00 USD | 8,770.00 USD | 11,350.00 USD |
| `1D` | `0.0985` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 5,970.00 USD | 8,750.00 USD | 12,540.00 USD |
| `7D` | `0.0985` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 5,330.00 USD | 16,370.00 USD | 90.68 USD |
| `1D` | `0.0987` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 30,280.00 USD | 7,610.00 USD | 16,110.00 USD |
| `7D` | `0.0987` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 5,390.00 USD | 15,350.00 USD | 6,690.00 USD |
| `1D` | `0.0989` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 8,920.00 USD | 10,380.00 USD | 24,510.00 USD |
| `7D` | `0.0989` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 20,710.00 USD | 3,470.00 USD | 0.00 USD |
| `1D` | `0.0991` | 975,740.00 USD | 0.00 USD | 975,740.00 USD | 79,410.00 USD | 1,530.00 USD | 4,850.00 USD |
| `7D` | `0.0991` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 14,350.00 USD | 5,210.00 USD | 0.00 USD |
| `1D` | `0.0993` | 889,950.00 USD | 0.00 USD | 889,950.00 USD | 33,340.00 USD | 7,220.00 USD | 45,850.00 USD |
| `7D` | `0.0993` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 63,040.00 USD | 9,430.00 USD | 50,900.00 USD |
| `1D` | `0.0995` | 803,540.00 USD | 0.00 USD | 803,540.00 USD | 16,240.00 USD | 3,010.00 USD | 50,480.00 USD |
| `7D` | `0.0995` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 18,620.00 USD | 0.00 USD | 25,130.00 USD |
| `1D` | `0.0997` | 733,810.00 USD | 0.00 USD | 733,810.00 USD | 26,940.00 USD | 7,370.00 USD | 58,680.00 USD |
| `7D` | `0.0997` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 27,750.00 USD | 11,200.00 USD | 32,880.00 USD |
| `1D` | `0.0999` | 640,820.00 USD | 0.00 USD | 640,820.00 USD | 0.00 USD | 11,820.00 USD | 47,880.00 USD |
| `7D` | `0.0999` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 42,340.00 USD | 11,480.00 USD | 104,630.00 USD |
| `1D` | `0.1001` | 581,120.00 USD | 0.00 USD | 581,120.00 USD | 25,400.00 USD | 4,200.00 USD | 42,510.00 USD |
| `7D` | `0.1001` | 857,780.00 USD | 0.00 USD | 857,780.00 USD | 86,120.00 USD | 19,930.00 USD | 105,740.00 USD |
| `1D` | `0.1003` | 509,010.00 USD | 0.00 USD | 509,010.00 USD | 37,160.00 USD | 10,200.00 USD | 27,200.00 USD |
| `7D` | `0.1003` | 645,990.00 USD | 0.00 USD | 645,990.00 USD | 8,010.00 USD | 10,130.00 USD | 27,910.00 USD |
| `1D` | `0.1005` | 434,450.00 USD | 0.00 USD | 434,450.00 USD | 31,310.00 USD | 43,010.00 USD | 66,000.00 USD |
| `7D` | `0.1005` | 599,950.00 USD | 0.00 USD | 599,950.00 USD | 35,740.00 USD | 40,720.00 USD | 63,710.00 USD |
| `1D` | `0.1007` | 294,130.00 USD | 0.00 USD | 294,130.00 USD | 21,860.00 USD | 7,380.00 USD | 8,630.00 USD |
| `7D` | `0.1007` | 459,780.00 USD | 0.00 USD | 459,780.00 USD | 10,260.00 USD | 3,080.00 USD | 68,140.00 USD |
| `1D` | `0.1009` | 256,260.00 USD | 0.00 USD | 256,260.00 USD | 20,400.00 USD | 17,660.00 USD | 5,600.00 USD |
| `7D` | `0.1009` | 378,300.00 USD | 0.00 USD | 378,300.00 USD | 32,230.00 USD | 17,090.00 USD | 54,030.00 USD |
| `1D` | `0.1011` | 212,600.00 USD | 0.00 USD | 212,600.00 USD | 18,940.00 USD | 7,120.00 USD | 25,440.00 USD |
| `7D` | `0.1011` | 274,960.00 USD | 0.00 USD | 274,960.00 USD | 4,430.00 USD | 15,140.00 USD | 0.00 USD |
| `1D` | `0.1013` | 161,090.00 USD | 0.00 USD | 161,090.00 USD | 21,860.00 USD | 8,400.00 USD | 18,140.00 USD |
| `7D` | `0.1013` | 255,390.00 USD | 0.00 USD | 255,390.00 USD | 32,420.00 USD | 46,040.00 USD | 25,450.00 USD |
| `1D` | `0.1015` | 112,680.00 USD | 0.00 USD | 112,680.00 USD | 4,580.00 USD | 5,450.00 USD | 20,200.00 USD |
| `7D` | `0.1015` | 151,480.00 USD | 0.00 USD | 151,480.00 USD | 17,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1017` | 82,450.00 USD | 0.00 USD | 82,450.00 USD | 10,050.00 USD | 0.00 USD | 15,750.00 USD |
| `7D` | `0.1017` | 133,570.00 USD | 0.00 USD | 133,570.00 USD | 11,450.00 USD | 0.00 USD | 10,630.00 USD |
| `1D` | `0.1019` | 56,660.00 USD | 0.00 USD | 56,660.00 USD | 11,630.00 USD | 1,550.00 USD | 1,730.00 USD |
| `7D` | `0.1019` | 111,490.00 USD | 0.00 USD | 111,490.00 USD | 36,610.00 USD | 8,460.00 USD | 9,980.00 USD |
| `1D` | `0.1021` | 41,760.00 USD | 0.00 USD | 41,760.00 USD | 0.00 USD | 0.00 USD | 13,880.00 USD |
| `7D` | `0.1021` | 56,440.00 USD | 0.00 USD | 56,440.00 USD | 0.00 USD | 0.00 USD | 37,440.00 USD |
| `1D` | `0.1023` | 27,870.00 USD | 0.00 USD | 27,870.00 USD | 0.00 USD | 0.00 USD | 3,720.00 USD |
| `7D` | `0.1033` | 18,990.00 USD | 0.00 USD | 18,990.00 USD | 13,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1035` | 5,810.00 USD | 0.00 USD | 5,810.00 USD | 0.00 USD | 0.00 USD | 108.00 USD |
| `1D` | `0.1037` | 24,150.00 USD | 0.00 USD | 24,150.00 USD | 2,150.00 USD | 12,850.00 USD | 24.05 USD |
| `7D` | `0.1037` | 5,700.00 USD | 0.00 USD | 5,700.00 USD | 0.00 USD | 5,700.00 USD | 0.00 USD |
| `1D` | `0.1039` | 9,120.00 USD | 0.00 USD | 9,120.00 USD | 0.00 USD | 9,120.00 USD | 0.00 USD |
| `7D` | `0.1039` | 38,750.00 USD | 38,750.00 USD | 0.00 USD | 0.00 USD | 7,400.00 USD | 31,350.00 USD |
| `7D` | `0.1039` | 77,500.00 USD | 77,500.00 USD | 0.00 USD | 0.00 USD | 7,400.00 USD | 31,350.00 USD |
| `1D` | `0.1040` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1041` | 56,410.00 USD | 56,410.00 USD | 0.00 USD | 20,110.00 USD | 16,680.00 USD | 19,630.00 USD |
| `7D` | `0.1041` | 124,960.00 USD | 124,960.00 USD | 0.00 USD | 44,560.00 USD | 2,910.00 USD | 0.00 USD |
| `1D` | `0.1043` | 113,110.00 USD | 113,110.00 USD | 0.00 USD | 13,920.00 USD | 18,610.00 USD | 24,170.00 USD |
| `7D` | `0.1043` | 179,740.00 USD | 179,740.00 USD | 0.00 USD | 15,960.00 USD | 16,120.00 USD | 22,700.00 USD |
| `1D` | `0.1045` | 168,610.00 USD | 168,610.00 USD | 0.00 USD | 12,990.00 USD | 21,860.00 USD | 20,650.00 USD |
| `7D` | `0.1045` | 209,500.00 USD | 209,500.00 USD | 0.00 USD | 0.00 USD | 29,750.00 USD | 0.00 USD |
| `1D` | `0.1047` | 282,300.00 USD | 282,300.00 USD | 0.00 USD | 40,510.00 USD | 22,900.00 USD | 50,280.00 USD |
| `7D` | `0.1047` | 312,750.00 USD | 312,750.00 USD | 0.00 USD | 10,670.00 USD | 24,890.00 USD | 67,690.00 USD |
| `1D` | `0.1049` | 404,940.00 USD | 404,940.00 USD | 0.00 USD | 35,540.00 USD | 20,260.00 USD | 66,840.00 USD |
| `7D` | `0.1049` | 441,380.00 USD | 441,380.00 USD | 0.00 USD | 34,790.00 USD | 4,810.00 USD | 89,030.00 USD |
| `1D` | `0.1051` | 465,260.00 USD | 465,260.00 USD | 0.00 USD | 32,010.00 USD | 21,250.00 USD | 7,060.00 USD |
| `7D` | `0.1051` | 526,330.00 USD | 526,330.00 USD | 0.00 USD | 34,200.00 USD | 15,780.00 USD | 34,970.00 USD |
| `1D` | `0.1053` | 554,330.00 USD | 554,330.00 USD | 0.00 USD | 32,610.00 USD | 8,780.00 USD | 47,680.00 USD |
| `7D` | `0.1053` | 715,800.00 USD | 715,800.00 USD | 0.00 USD | 53,590.00 USD | 40,230.00 USD | 95,640.00 USD |
| `1D` | `0.1055` | 670,610.00 USD | 670,610.00 USD | 0.00 USD | 51,550.00 USD | 21,730.00 USD | 43,010.00 USD |
| `7D` | `0.1055` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 80,160.00 USD | 46,150.00 USD | 193,520.00 USD |
| `1D` | `0.1057` | 732,530.00 USD | 732,530.00 USD | 0.00 USD | 14,080.00 USD | 16,120.00 USD | 31,720.00 USD |
| `7D` | `0.1057` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 61,450.00 USD | 47,740.00 USD | 110,830.00 USD |
| `1D` | `0.1059` | 842,060.00 USD | 842,060.00 USD | 0.00 USD | 30,300.00 USD | 5,730.00 USD | 73,500.00 USD |
| `7D` | `0.1059` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 77,800.00 USD | 51,220.00 USD | 123,770.00 USD |
| `1D` | `0.1061` | 924,210.00 USD | 924,210.00 USD | 0.00 USD | 42,730.00 USD | 4,800.00 USD | 34,620.00 USD |
| `7D` | `0.1061` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 45,510.00 USD | 27,410.00 USD | 76,420.00 USD |
| `1D` | `0.1063` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 34,110.00 USD | 4,070.00 USD | 50,880.00 USD |
| `7D` | `0.1063` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 22,280.00 USD | 43,390.00 USD | 149,630.00 USD |
| `1D` | `0.1065` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 12,870.00 USD | 15,500.00 USD | 35,010.00 USD |
| `7D` | `0.1065` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 24,310.00 USD | 99,810.00 USD |
| `1D` | `0.1067` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 14,200.00 USD | 10,080.00 USD | 44,390.00 USD |
| `7D` | `0.1067` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 5,330.00 USD | 60,270.00 USD | 83,410.00 USD |
| `1D` | `0.1069` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 23,520.00 USD | 9,120.00 USD | 43,350.00 USD |
| `7D` | `0.1069` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD | 98,960.00 USD |
| `1D` | `0.1071` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 9,290.00 USD | 11,540.00 USD | 8,620.00 USD |
| `7D` | `0.1071` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 16,280.00 USD | 32,350.00 USD | 52,820.00 USD |
| `1D` | `0.1073` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 9,470.00 USD | 1,530.00 USD | 9,050.00 USD |
| `7D` | `0.1073` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 22,920.00 USD | 0.00 USD |
| `1D` | `0.1075` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 12,370.00 USD | 5,060.00 USD | 7,670.00 USD |
| `7D` | `0.1075` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 9,430.00 USD | 22,500.00 USD |
| `1D` | `0.1077` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD | 3,680.00 USD |
| `7D` | `0.1077` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 11,160.00 USD | 0.00 USD | 332.62 USD |
| `1D` | `0.1079` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 4,300.00 USD | 23,410.00 USD |
| `7D` | `0.1079` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 3,380.00 USD | 9,930.00 USD |
| `1D` | `0.1081` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 13,690.00 USD | 732.74 USD | 4,150.00 USD |
| `7D` | `0.1081` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 6,650.00 USD | 0.00 USD | 89.24 USD |
| `1D` | `0.1083` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 9,160.00 USD | 6,710.00 USD | 10,790.00 USD |
| `7D` | `0.1083` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 64.98 USD |
| `1D` | `0.1085` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 385.06 USD | 65,050.00 USD |
| `7D` | `0.1085` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1087` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 28,490.00 USD | 2,510.00 USD | 44,700.00 USD |
| `7D` | `0.1087` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,540.00 USD |
| `1D` | `0.1089` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 29,650.00 USD | 1,580.00 USD | 3,370.00 USD |
| `7D` | `0.1089` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 5,290.00 USD | 1,420.00 USD | 204.64 USD |
| `1D` | `0.1091` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 33,700.00 USD | 0.00 USD | 16.51 USD |
| `7D` | `0.1091` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD |
| `1D` | `0.1093` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 15,480.00 USD | 1,080.00 USD | 272.04 USD |
| `7D` | `0.1093` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 1,500.00 USD | 8,730.00 USD |
| `1D` | `0.1095` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 21,610.00 USD |
| `7D` | `0.1095` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 189.85 USD |
| `1D` | `0.1097` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 7,260.00 USD | 2,530.00 USD | 22,850.00 USD |
| `7D` | `0.1097` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1099` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 6,130.00 USD | 1,940.00 USD | 32.38 USD |
| `7D` | `0.1099` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 21,880.00 USD |
| `1D` | `0.1101` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 5,570.00 USD | 3,820.00 USD | 4,290.00 USD |
| `7D` | `0.1101` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1103` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 3,540.00 USD | 6,900.00 USD | 1,160.00 USD |
| `7D` | `0.1103` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 17,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1105` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 3,380.00 USD | 4,740.00 USD | 10,760.00 USD |
| `7D` | `0.1105` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 14,480.00 USD | 246.98 USD |
| `1D` | `0.1107` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 3,110.00 USD | 13,200.00 USD | 35,750.00 USD |
| `7D` | `0.1107` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 12,510.00 USD | 15,950.00 USD |
| `1D` | `0.1109` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 2,110.00 USD | 1,370.00 USD | 2,670.00 USD |
| `7D` | `0.1109` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 12,430.00 USD | 0.00 USD |
| `1D` | `0.1111` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 5,200.00 USD | 996.46 USD | 104.00 USD |
| `7D` | `0.1111` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD |
| `1D` | `0.1113` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 21,390.00 USD | 5,880.00 USD | 13,550.00 USD |
| `1D` | `0.1115` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 6,690.00 USD | 465.26 USD | 0.00 USD |
| `7D` | `0.1115` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28.89 USD |
| `1D` | `0.1117` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 2,060.00 USD | 10,810.00 USD | 24,630.00 USD |
| `7D` | `0.1117` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | 16,490.00 USD |
| `1D` | `0.1119` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 23,420.00 USD | 4,920.00 USD | 31,040.00 USD |
| `7D` | `0.1119` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 34,550.00 USD | 7,050.00 USD | 21,720.00 USD |
| `1D` | `0.1121` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 21,300.00 USD | 12,810.00 USD | 12,350.00 USD |
| `7D` | `0.1121` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 5,730.00 USD | 0.00 USD | 27,490.00 USD |
| `1D` | `0.1123` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 30,640.00 USD | 2,870.00 USD | 8,450.00 USD |
| `7D` | `0.1123` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 19,800.00 USD | 23,980.00 USD | 37,780.00 USD |
| `1D` | `0.1125` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 11,890.00 USD | 8,250.00 USD | 11,740.00 USD |
| `7D` | `0.1125` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 4,250.00 USD | 36,160.00 USD |
| `1D` | `0.1127` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 1,670.00 USD | 4,120.00 USD | 22,900.00 USD |
| `7D` | `0.1127` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 2,720.00 USD | 7,980.00 USD |
| `1D` | `0.1129` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 11,080.00 USD | 1,390.00 USD | 7,770.00 USD |
| `7D` | `0.1129` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD | 9,320.00 USD |
| `1D` | `0.1131` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 24,040.00 USD | 6,440.00 USD | 24,260.00 USD |
| `7D` | `0.1131` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 12,540.00 USD | 0.00 USD | 25,870.00 USD |
| `1D` | `0.1133` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 8,350.00 USD | 19,820.00 USD | 24,600.00 USD |
| `7D` | `0.1133` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 12,810.00 USD | 0.00 USD |
| `1D` | `0.1135` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 7,500.00 USD | 3,200.00 USD | 5,390.00 USD |
| `7D` | `0.1135` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 6,800.00 USD | 9,010.00 USD |
| `1D` | `0.1137` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 4,040.00 USD | 1,090.00 USD | 1,090.00 USD |
| `7D` | `0.1137` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 2,240.00 USD | 9,000.00 USD |
| `1D` | `0.1139` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 844.95 USD | 5,420.00 USD |
| `7D` | `0.1139` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 2,220.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1141` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 8,110.00 USD | 0.00 USD | 21,920.00 USD |
| `7D` | `0.1141` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,640.00 USD |
| `1D` | `0.1143` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 22,320.00 USD | 22,390.00 USD | 10,500.00 USD |
| `7D` | `0.1143` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78,600.00 USD |
| `1D` | `0.1145` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 9,770.00 USD | 6,840.00 USD | 23,700.00 USD |
| `7D` | `0.1145` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 16,540.00 USD | 2,730.00 USD | 141,160.00 USD |
| `1D` | `0.1147` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 3,840.00 USD | 7,350.00 USD | 18,360.00 USD |
| `7D` | `0.1147` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 138,160.00 USD |
| `1D` | `0.1148` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 14,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1149` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 10,560.00 USD | 0.00 USD | 72,820.00 USD |
| `7D` | `0.1151` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 92,570.00 USD | 4,210.00 USD | 128,190.00 USD |
| `7D` | `0.1153` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 136,660.00 USD | 8,400.00 USD | 146,040.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `65.23M` | Total OI Tokens: `627,551,589.4 OP`
  * 1h OI Change: `+1.26%` | 4h OI Change: `+1.22%` | 24h OI Change: `-11.48%`
  * Exchange Breakdown: Binance=`14.19M` | Bybit=`12.97M` | OKX=`4.11M` | Hyperliquid=`3.21M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-3.22K` | Last 24h: `-4.25K` | Last 3d: `-11.30K` | Last 7d: `-13.94K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0172%` | **USDT OKX** | `-0.0296%` |
| **USDT Bybit** | `0.0034%` | **USDT KuCoin** | `-0.0060%` |
| **USDT MEXC** | `-0.0171%` | **USDT BingX** | `0.0100%` |
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
| `4H` | `OP` | `47.89%` | `52.11%` | `0.92` | 17,020,000.00 USD |
| `4H` | `Binance` | `49.99%` | `50.01%` | `1.00` | 5,620,000.00 USD |
| `4H` | `OKX` | `53.8%` | `46.2%` | `1.16` | 1,490,000.00 USD |
| `4H` | `Bybit` | `51.48%` | `48.52%` | `1.06` | 1,630,000.00 USD |
| `4H` | `KuCoin` | `50.69%` | `49.31%` | `1.03` | 2,050,000.00 USD |
| `4H` | `Gate` | `48.57%` | `51.43%` | `0.94` | 395,790.00 USD |
| `4H` | `Bitget` | `49.58%` | `50.42%` | `0.98` | 713,770.00 USD |
| `4H` | `BingX` | `23.97%` | `76.03%` | `0.32` | 1,930,000.00 USD |
| `4H` | `MEXC` | `50.29%` | `49.71%` | `1.01` | 799,350.00 USD |
| `4H` | `Bitunix` | `38%` | `62%` | `0.61` | 251,050.00 USD |
| `4H` | `Hyperliquid` | `57.43%` | `42.57%` | `1.35` | 462,370.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.07%` | `49.93%` | `1.00` | 852,910.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `56.92%` | `43.08%` | `1.32` | 705,320.00 USD |
| `4H` | `HTX` | `62.64%` | `37.36%` | `1.68` | 2,860.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `59.51%` | `40.49%` | `1.47` | 9,810.00 USD |
| `4H` | `Aster` | `51.45%` | `48.55%` | `1.06` | 67,950.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.48%` | `47.52%` | `1.10` | 12,670.00 USD |
| `4H` | `Whale Positions` | `49.99%` | `50.01%` | `1.00` | 5,620,000.00 USD |
| `4H` | `Global Accounts` | `47.89%` | `52.11%` | `0.92` | 17,020,000.00 USD |


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
| `5:00 UTC` | `0.1039` | `0.1040` | `0.1039` | `0.1041` | `0.1038` | 54,594.10 USD | 36,098.98 USD | 18,495.12 USD | 17,603.87 USD | `+32.25%` | `11B / 8S` |

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
| `5m` | 5,330.00 USD | 13,330.00 USD | **`ACCUMULATION`** |
| `15m` | 9,740.00 USD | -32,870.00 USD | **`DISTRIBUTION`** |
| `30m` | 24,790.00 USD | 132,070.00 USD | **`ACCUMULATION`** |
| `1h` | 12,190.00 USD | 160,140.00 USD | **`ACCUMULATION`** |
| `2h` | -24,110.00 USD | 122,100.00 USD | **`ACCUMULATION`** |
| `4h` | -26,730.00 USD | 209,500.00 USD | **`ACCUMULATION`** |
| `6h` | -27,970.00 USD | 565,810.00 USD | **`ACCUMULATION`** |
| `8h` | -120,830.00 USD | 669,880.00 USD | **`ACCUMULATION`** |
| `12h` | -60,960.00 USD | -1,430,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 199,310.00 USD | -3,940,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -310,140.00 USD | -12,520,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,280,000.00 USD | -83,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+5.33K` | 15m=`+9.74K` | 1h=`+12.19K` | 24h=`+199.31K`
* Futures Capital Netflows: 5m=`+13.33K` | 15m=`-32.87K` | 1h=`+160.14K` | 24h=`-3.94M`
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
  * `2026-10-30 15:50:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
