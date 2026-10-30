# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 16:09:32 IST` (`2026-10-30 10:39:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1031` | `0.1036` | `0.1031` | `0.1034` | `2,079,633` | 214,892.05 USD | 23,218.30 USD | `+10.80%` | -1,909,802.51 USD | `+0.93` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1034` | `0.1035` | `0.1029` | `0.1031` | `794,273` | 81,993.01 USD | 9,830.25 USD | `+11.99%` | -1,899,972.26 USD | `+0.40` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1031` | `0.1033` | `0.1031` | `0.1033` | `31,921` | 3,292.69 USD | -405.93 USD | `-12.33%` | -1,900,378.19 USD | `-0.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1027` | `0.1034` | `0.1023` | `0.1034` | `2,312,864` | 237,952.24 USD | 29,698.57 USD | `+12.48%` | -1,882,516.37 USD | `+0.31` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1034` | `0.1036` | `0.1028` | `0.1034` | `4,274,060` | 441,050.39 USD | -16,521.82 USD | `-3.75%` | -1,899,038.19 USD | `-0.79` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1034` | `0.1035` | `0.1029` | `0.1033` | `840,713` | 86,784.86 USD | 10,500.84 USD | `+12.10%` | -1,888,537.35 USD | `-0.01` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1027` | `0.1038` | `0.1023` | `0.1024` | `10,736,702` | 1,104,134.28 USD | 90,049.28 USD | `+8.16%` | -1,914,501.02 USD | `+0.40` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1024` | `0.1034` | `0.1019` | `0.1034` | `10,854,845` | 1,111,003.69 USD | -28,977.96 USD | `-2.61%` | -1,943,478.98 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1034` | `0.1036` | `0.1028` | `0.1032` | `5,102,302` | 526,547.42 USD | -7,308.82 USD | `-1.39%` | -1,950,787.80 USD | `+0.22` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,490,108.93 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1040` | `0.0988` | `0.1027` | `54,609,324` | 5,566,939.91 USD | 608,714.61 USD | `+10.93%` | -1,881,394.33 USD | `+1.21` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1027` | `0.1038` | `0.1019` | `0.1032` | `26,693,848` | 2,741,685.38 USD | 53,762.50 USD | `+1.96%` | -1,827,631.83 USD | `+0.47` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | 165,115.32 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -1,152,082.54 USD | `-1.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,490,108.93 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1040` | `0.0988` | `0.1027` | `54,609,324` | 5,566,939.91 USD | 608,714.61 USD | `+10.93%` | -1,881,394.33 USD | `+1.21` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1027` | `0.1038` | `0.1019` | `0.1036` | `28,222,511` | 2,899,724.17 USD | 39,383.00 USD | `+1.36%` | -1,842,011.33 USD | `+0.45` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:01:49 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1103` | 5,867.99 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale BUY: 5.87K USD at 0.1103 USD [API] | `2026-10-29 11:51:44` |
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
| `7D` | `Long Liquidation` | `0.0863` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 1,880.00 USD | 7,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0865` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 1,980.00 USD | 13,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0865` | 318.30 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0867` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 2,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0869` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0871` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 1,200.00 USD | 2,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0873` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 4,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0875` | 2,400,000.00 USD | 2,400,000.00 USD | 6,010.00 USD | 0.00 USD | 4,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0875` | 793.17 USD | 6,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0877` | 2,390,000.00 USD | 2,390,000.00 USD | 7,820.00 USD | 6,050.00 USD | 22,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0879` | 2,350,000.00 USD | 2,350,000.00 USD | 1,370.00 USD | 2,010.00 USD | 13,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0881` | 2,330,000.00 USD | 2,330,000.00 USD | 9,390.00 USD | 2,270.00 USD | 5,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0883` | 2,320,000.00 USD | 2,320,000.00 USD | 7,040.00 USD | 6,800.00 USD | 21,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0885` | 2,280,000.00 USD | 2,280,000.00 USD | 1,000.00 USD | 1,220.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0887` | 2,280,000.00 USD | 2,280,000.00 USD | 10,610.00 USD | 2,920.00 USD | 17,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0889` | 2,240,000.00 USD | 2,240,000.00 USD | 10,710.00 USD | 3,200.00 USD | 13,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0891` | 2,220,000.00 USD | 2,220,000.00 USD | 6,310.00 USD | 3,960.00 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0893` | 2,210,000.00 USD | 2,210,000.00 USD | 5,230.00 USD | 3,080.00 USD | 5,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0895` | 2,190,000.00 USD | 2,190,000.00 USD | 4,480.00 USD | 2,110.00 USD | 5,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,270.00 USD | 5,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0897` | 2,180,000.00 USD | 2,180,000.00 USD | 4,670.00 USD | 0.00 USD | 1,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0899` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 927.82 USD | 4,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0901` | 2,170,000.00 USD | 2,170,000.00 USD | 1,250.00 USD | 428.11 USD | 17.63 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0903` | 2,170,000.00 USD | 2,170,000.00 USD | 5,330.00 USD | 1,480.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0905` | 2,160,000.00 USD | 2,160,000.00 USD | 6,050.00 USD | 0.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0905` | 2,230.00 USD | 2,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0907` | 2,150,000.00 USD | 2,150,000.00 USD | 2,780.00 USD | 2,880.00 USD | 2,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0909` | 2,140,000.00 USD | 2,140,000.00 USD | 1,180.00 USD | 2,200.00 USD | 7.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0911` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 2,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0915` | 2,130,000.00 USD | 2,130,000.00 USD | 1,670.00 USD | 903.90 USD | 161.63 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0917` | 2,050,000.00 USD | 2,050,000.00 USD | 10,440.00 USD | 5,980.00 USD | 262.44 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0917` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0919` | 2,030,000.00 USD | 2,030,000.00 USD | 8,950.00 USD | 1,090.00 USD | 19,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0919` | 2,120,000.00 USD | 2,120,000.00 USD | 7,440.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0921` | 2,000,000.00 USD | 2,000,000.00 USD | 758.20 USD | 2,040.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0921` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 2,030.00 USD | 58.40 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0923` | 1,990,000.00 USD | 1,990,000.00 USD | 4,040.00 USD | 6,180.00 USD | 30,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0923` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 9,670.00 USD | 43,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0925` | 1,950,000.00 USD | 1,950,000.00 USD | 6,480.00 USD | 4,210.00 USD | 27,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0925` | 2,060,000.00 USD | 2,060,000.00 USD | 1,790.00 USD | 0.00 USD | 10,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0927` | 1,910,000.00 USD | 1,910,000.00 USD | 1,820.00 USD | 2,740.00 USD | 1,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0927` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 1,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0929` | 1,910,000.00 USD | 1,910,000.00 USD | 7,820.00 USD | 1,800.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0929` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 4,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0931` | 1,900,000.00 USD | 1,900,000.00 USD | 4,040.00 USD | 1,090.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0931` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 2,240.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0933` | 1,880,000.00 USD | 1,880,000.00 USD | 16,500.00 USD | 844.95 USD | 11,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0933` | 2,030,000.00 USD | 2,030,000.00 USD | 2,220.00 USD | 0.00 USD | 78.61 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0935` | 1,860,000.00 USD | 1,860,000.00 USD | 9,740.00 USD | 7,300.00 USD | 15,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0935` | 2,020,000.00 USD | 2,020,000.00 USD | 19,560.00 USD | 6,840.00 USD | 25,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0937` | 1,820,000.00 USD | 1,820,000.00 USD | 4,580.00 USD | 6,660.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0937` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 51.74 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0939` | 1,800,000.00 USD | 1,800,000.00 USD | 3,590.00 USD | 2,140.00 USD | 44,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0939` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 10,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0941` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 9,410.00 USD | 21,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0941` | 1,960,000.00 USD | 1,960,000.00 USD | 14,050.00 USD | 18,340.00 USD | 76,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0943` | 1,720,000.00 USD | 1,720,000.00 USD | 3,500.00 USD | 10,920.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0943` | 1,850,000.00 USD | 1,850,000.00 USD | 6,170.00 USD | 0.00 USD | 37,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0945` | 1,670,000.00 USD | 1,670,000.00 USD | 15,750.00 USD | 6,510.00 USD | 44,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0945` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 3,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0947` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 962.66 USD | 91.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0947` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 62.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0949` | 1,610,000.00 USD | 1,610,000.00 USD | 12,180.00 USD | 5,770.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0949` | 1,810,000.00 USD | 1,810,000.00 USD | 3,770.00 USD | 9,700.00 USD | 26,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0951` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 2,030.00 USD | 19,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0951` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 64.98 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0953` | 1,560,000.00 USD | 1,560,000.00 USD | 33,000.00 USD | 4,360.00 USD | 6,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0953` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 8,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0955` | 1,520,000.00 USD | 1,520,000.00 USD | 17,990.00 USD | 14,600.00 USD | 31,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0955` | 1,760,000.00 USD | 1,760,000.00 USD | 39,120.00 USD | 13,670.00 USD | 51,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0957` | 1,450,000.00 USD | 1,450,000.00 USD | 16,340.00 USD | 6,740.00 USD | 48,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0957` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 65.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0959` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 3,100.00 USD | 50.26 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0959` | 1,650,000.00 USD | 1,650,000.00 USD | 28,110.00 USD | 0.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0961` | 1,380,000.00 USD | 1,380,000.00 USD | 8,920.00 USD | 23,950.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0961` | 1,600,000.00 USD | 1,600,000.00 USD | 12,340.00 USD | 16,920.00 USD | 94,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0963` | 1,320,000.00 USD | 1,320,000.00 USD | 23,240.00 USD | 11,750.00 USD | 11,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0963` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 4,020.00 USD | 83.82 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0965` | 1,280,000.00 USD | 1,280,000.00 USD | 8,250.00 USD | 5,890.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0965` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 2,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0967` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 1,960.00 USD | 818.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0967` | 1,470,000.00 USD | 1,470,000.00 USD | 3,770.00 USD | 0.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0969` | 1,240,000.00 USD | 1,240,000.00 USD | 6,930.00 USD | 7,530.00 USD | 8,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0969` | 1,470,000.00 USD | 1,470,000.00 USD | 3,720.00 USD | 7,090.00 USD | 61,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0971` | 1,220,000.00 USD | 1,220,000.00 USD | 2,840.00 USD | 4,070.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 104.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0973` | 1,200,000.00 USD | 1,200,000.00 USD | 1,440.00 USD | 10,220.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0973` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0975` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 114.54 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0975` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 87.10 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0977` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 765.93 USD | 978.56 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0977` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 73.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0979` | 1,180,000.00 USD | 1,180,000.00 USD | 5,180.00 USD | 2,920.00 USD | 21,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0979` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 75.46 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0981` | 1,150,000.00 USD | 1,150,000.00 USD | 12,740.00 USD | 7,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0981` | 1,380,000.00 USD | 1,380,000.00 USD | 22,280.00 USD | 5,070.00 USD | 148.75 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0983` | 1,130,000.00 USD | 1,130,000.00 USD | 11,130.00 USD | 16,910.00 USD | 10,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 8,770.00 USD | 11,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0985` | 1,100,000.00 USD | 1,100,000.00 USD | 5,970.00 USD | 8,750.00 USD | 12,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0985` | 1,330,000.00 USD | 1,330,000.00 USD | 5,330.00 USD | 16,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0987` | 1,070,000.00 USD | 1,070,000.00 USD | 30,280.00 USD | 7,610.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0987` | 1,310,000.00 USD | 1,310,000.00 USD | 5,390.00 USD | 15,350.00 USD | 6,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0989` | 1,010,000.00 USD | 1,010,000.00 USD | 8,920.00 USD | 10,380.00 USD | 24,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 1,280,000.00 USD | 1,280,000.00 USD | 20,710.00 USD | 3,470.00 USD | 51.48 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0991` | 970,960.00 USD | 970,960.00 USD | 79,410.00 USD | 1,530.00 USD | 4,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0991` | 1,260,000.00 USD | 1,260,000.00 USD | 14,350.00 USD | 5,210.00 USD | 186.28 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0993` | 885,170.00 USD | 885,170.00 USD | 33,340.00 USD | 7,220.00 USD | 45,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0993` | 1,240,000.00 USD | 1,240,000.00 USD | 63,040.00 USD | 9,430.00 USD | 51,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0995` | 798,760.00 USD | 798,760.00 USD | 16,240.00 USD | 3,010.00 USD | 52,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 1,110,000.00 USD | 1,110,000.00 USD | 18,620.00 USD | 0.00 USD | 25,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0997` | 726,580.00 USD | 726,580.00 USD | 19,770.00 USD | 7,370.00 USD | 55,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0997` | 1,070,000.00 USD | 1,070,000.00 USD | 21,100.00 USD | 11,200.00 USD | 32,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0999` | 643,940.00 USD | 643,940.00 USD | 0.00 USD | 11,820.00 USD | 47,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0999` | 1,000,000.00 USD | 1,000,000.00 USD | 42,340.00 USD | 11,480.00 USD | 104,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1001` | 584,240.00 USD | 584,240.00 USD | 25,400.00 USD | 4,200.00 USD | 42,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 844,980.00 USD | 844,980.00 USD | 86,120.00 USD | 19,930.00 USD | 105,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1003` | 512,130.00 USD | 512,130.00 USD | 37,160.00 USD | 10,200.00 USD | 27,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1003` | 633,190.00 USD | 633,190.00 USD | 8,010.00 USD | 10,130.00 USD | 27,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1005` | 437,570.00 USD | 437,570.00 USD | 31,310.00 USD | 43,010.00 USD | 66,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1005` | 587,140.00 USD | 587,140.00 USD | 35,740.00 USD | 40,720.00 USD | 63,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1007` | 297,250.00 USD | 297,250.00 USD | 21,860.00 USD | 7,380.00 USD | 8,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 446,980.00 USD | 446,980.00 USD | 10,260.00 USD | 3,080.00 USD | 68,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1009` | 259,380.00 USD | 259,380.00 USD | 20,400.00 USD | 17,660.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1009` | 365,500.00 USD | 365,500.00 USD | 32,230.00 USD | 17,090.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1011` | 215,720.00 USD | 215,720.00 USD | 18,940.00 USD | 7,120.00 USD | 25,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1011` | 262,150.00 USD | 262,150.00 USD | 4,430.00 USD | 15,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1013` | 164,210.00 USD | 164,210.00 USD | 21,860.00 USD | 8,400.00 USD | 18,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 242,580.00 USD | 242,580.00 USD | 32,420.00 USD | 46,040.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1015` | 115,800.00 USD | 115,800.00 USD | 4,580.00 USD | 5,450.00 USD | 20,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1015` | 138,670.00 USD | 138,670.00 USD | 17,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1017` | 85,570.00 USD | 85,570.00 USD | 3,590.00 USD | 0.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1017` | 120,770.00 USD | 120,770.00 USD | 11,450.00 USD | 0.00 USD | 10,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1019` | 70,870.00 USD | 70,870.00 USD | 3,750.00 USD | 1,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1019` | 98,680.00 USD | 98,680.00 USD | 23,310.00 USD | 8,460.00 USD | 9,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1021` | 65,570.00 USD | 65,570.00 USD | 0.00 USD | 0.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1021` | 56,930.00 USD | 56,930.00 USD | 0.00 USD | 0.00 USD | 37,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1023` | 51,690.00 USD | 51,690.00 USD | 0.00 USD | 0.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1033` | 19,490.00 USD | 19,490.00 USD | 13,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1035` | 6,300.00 USD | 6,300.00 USD | 0.00 USD | 0.00 USD | 169.16 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1037` | 47,960.00 USD | 47,960.00 USD | 35,090.00 USD | 12,850.00 USD | 24.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1037` | 6,130.00 USD | 6,130.00 USD | 0.00 USD | 5,700.00 USD | 431.99 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1039` | 14,340.00 USD | 14,340.00 USD | 0.00 USD | 9,120.00 USD | 5,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1039` | 38,890.00 USD | 38,890.00 USD | 0.00 USD | 7,400.00 USD | 31,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1039` | 77,780.00 USD | 77,780.00 USD | 0.00 USD | 7,400.00 USD | 31,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1041` | 70,750.00 USD | 70,750.00 USD | 20,110.00 USD | 16,680.00 USD | 19,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1041` | 131,520.00 USD | 131,520.00 USD | 50,500.00 USD | 2,910.00 USD | 336.87 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1043` | 127,450.00 USD | 127,450.00 USD | 13,920.00 USD | 18,610.00 USD | 24,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1043` | 186,770.00 USD | 186,770.00 USD | 15,960.00 USD | 16,120.00 USD | 23,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1045` | 182,950.00 USD | 182,950.00 USD | 12,990.00 USD | 21,860.00 USD | 20,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1045` | 217,480.00 USD | 217,480.00 USD | 0.00 USD | 29,750.00 USD | 957.55 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1047` | 296,640.00 USD | 296,640.00 USD | 40,510.00 USD | 22,900.00 USD | 50,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1047` | 321,350.00 USD | 321,350.00 USD | 10,670.00 USD | 24,890.00 USD | 68,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1049` | 419,280.00 USD | 419,280.00 USD | 35,540.00 USD | 20,260.00 USD | 66,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1049` | 451,270.00 USD | 451,270.00 USD | 34,790.00 USD | 4,810.00 USD | 90,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1051` | 479,590.00 USD | 479,590.00 USD | 32,010.00 USD | 21,250.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1051` | 536,590.00 USD | 536,590.00 USD | 34,200.00 USD | 15,780.00 USD | 35,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1053` | 568,670.00 USD | 568,670.00 USD | 32,610.00 USD | 8,780.00 USD | 47,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1053` | 726,100.00 USD | 726,100.00 USD | 53,590.00 USD | 40,230.00 USD | 95,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1055` | 684,950.00 USD | 684,950.00 USD | 51,550.00 USD | 21,730.00 USD | 43,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1055` | 1,050,000.00 USD | 1,050,000.00 USD | 80,160.00 USD | 46,150.00 USD | 193,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1057` | 748,680.00 USD | 748,680.00 USD | 14,080.00 USD | 16,120.00 USD | 33,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1057` | 1,270,000.00 USD | 1,270,000.00 USD | 61,450.00 USD | 47,740.00 USD | 111,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1059` | 848,540.00 USD | 848,540.00 USD | 25,280.00 USD | 5,730.00 USD | 68,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1059` | 1,520,000.00 USD | 1,520,000.00 USD | 77,800.00 USD | 51,220.00 USD | 123,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1061` | 927,210.00 USD | 927,210.00 USD | 34,850.00 USD | 4,800.00 USD | 39,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1061` | 1,650,000.00 USD | 1,650,000.00 USD | 32,220.00 USD | 27,410.00 USD | 76,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1063` | 1,020,000.00 USD | 1,020,000.00 USD | 34,110.00 USD | 4,070.00 USD | 50,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1063` | 1,870,000.00 USD | 1,870,000.00 USD | 22,280.00 USD | 43,390.00 USD | 149,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1065` | 1,080,000.00 USD | 1,080,000.00 USD | 12,870.00 USD | 15,500.00 USD | 35,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1065` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 24,310.00 USD | 99,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1067` | 1,150,000.00 USD | 1,150,000.00 USD | 14,200.00 USD | 10,080.00 USD | 44,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1067` | 2,140,000.00 USD | 2,140,000.00 USD | 5,330.00 USD | 60,270.00 USD | 83,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1069` | 1,220,000.00 USD | 1,220,000.00 USD | 23,520.00 USD | 9,120.00 USD | 43,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1069` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 31,620.00 USD | 99,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1071` | 1,250,000.00 USD | 1,250,000.00 USD | 9,290.00 USD | 11,540.00 USD | 8,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1071` | 2,380,000.00 USD | 2,380,000.00 USD | 16,280.00 USD | 32,350.00 USD | 52,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1073` | 1,270,000.00 USD | 1,270,000.00 USD | 9,470.00 USD | 1,530.00 USD | 9,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1073` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 22,920.00 USD | 225.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1075` | 1,300,000.00 USD | 1,300,000.00 USD | 12,370.00 USD | 5,060.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1075` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 9,430.00 USD | 22,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1077` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 2,730.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1077` | 2,440,000.00 USD | 2,440,000.00 USD | 11,160.00 USD | 0.00 USD | 87.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1079` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 4,300.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1079` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 3,380.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1081` | 1,340,000.00 USD | 1,340,000.00 USD | 6,520.00 USD | 732.74 USD | 2,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1081` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1083` | 1,370,000.00 USD | 1,370,000.00 USD | 9,160.00 USD | 6,710.00 USD | 10,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1083` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 227.53 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1085` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 385.06 USD | 65,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1085` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 193.32 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1087` | 1,510,000.00 USD | 1,510,000.00 USD | 28,490.00 USD | 2,510.00 USD | 44,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1087` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1089` | 1,540,000.00 USD | 1,540,000.00 USD | 29,650.00 USD | 1,580.00 USD | 3,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1089` | 2,470,000.00 USD | 2,470,000.00 USD | 5,290.00 USD | 1,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1091` | 1,580,000.00 USD | 1,580,000.00 USD | 33,700.00 USD | 0.00 USD | 16.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1091` | 2,500,000.00 USD | 2,500,000.00 USD | 16,310.00 USD | 0.00 USD | 9,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1093` | 1,590,000.00 USD | 1,590,000.00 USD | 15,480.00 USD | 1,080.00 USD | 272.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1093` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 1,500.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1095` | 1,620,000.00 USD | 1,620,000.00 USD | 4,110.00 USD | 1,890.00 USD | 21,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1095` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 192.14 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1097` | 1,650,000.00 USD | 1,650,000.00 USD | 7,260.00 USD | 2,530.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1097` | 2,530,000.00 USD | 2,530,000.00 USD | 18,600.00 USD | 0.00 USD | 103.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1099` | 1,660,000.00 USD | 1,660,000.00 USD | 6,130.00 USD | 1,940.00 USD | 32.38 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1099` | 2,560,000.00 USD | 2,560,000.00 USD | 11,470.00 USD | 0.00 USD | 21,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1101` | 1,680,000.00 USD | 1,680,000.00 USD | 5,570.00 USD | 3,820.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1101` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1103` | 1,690,000.00 USD | 1,690,000.00 USD | 3,540.00 USD | 6,900.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 2,600,000.00 USD | 2,600,000.00 USD | 17,490.00 USD | 0.00 USD | 85.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1105` | 1,710,000.00 USD | 1,710,000.00 USD | 3,380.00 USD | 4,740.00 USD | 10,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1105` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 14,480.00 USD | 34.51 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1107` | 1,760,000.00 USD | 1,760,000.00 USD | 3,110.00 USD | 13,200.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1107` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 12,510.00 USD | 15,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1109` | 1,760,000.00 USD | 1,760,000.00 USD | 2,110.00 USD | 1,370.00 USD | 2,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 12,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1111` | 1,770,000.00 USD | 1,770,000.00 USD | 5,200.00 USD | 996.46 USD | 104.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1111` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 11,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1113` | 1,810,000.00 USD | 1,810,000.00 USD | 21,390.00 USD | 5,880.00 USD | 13,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1115` | 1,820,000.00 USD | 1,820,000.00 USD | 6,690.00 USD | 465.26 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1115` | 1,880.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1117` | 1,860,000.00 USD | 1,860,000.00 USD | 2,060.00 USD | 10,810.00 USD | 24,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1117` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 22,780.00 USD | 16,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1119` | 1,920,000.00 USD | 1,920,000.00 USD | 23,420.00 USD | 4,920.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1119` | 2,770,000.00 USD | 2,770,000.00 USD | 34,550.00 USD | 7,050.00 USD | 21,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1121` | 1,960,000.00 USD | 1,960,000.00 USD | 21,300.00 USD | 12,810.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 2,800,000.00 USD | 2,800,000.00 USD | 5,730.00 USD | 0.00 USD | 27,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1123` | 2,000,000.00 USD | 2,000,000.00 USD | 30,640.00 USD | 2,870.00 USD | 8,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1123` | 2,890,000.00 USD | 2,890,000.00 USD | 19,800.00 USD | 23,980.00 USD | 37,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1125` | 2,040,000.00 USD | 2,040,000.00 USD | 11,890.00 USD | 12,350.00 USD | 11,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1125` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 4,250.00 USD | 36,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1127` | 2,070,000.00 USD | 2,070,000.00 USD | 1,670.00 USD | 4,120.00 USD | 22,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1127` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 2,720.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1129` | 2,090,000.00 USD | 2,090,000.00 USD | 11,080.00 USD | 1,390.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1129` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 2,020.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1131` | 2,140,000.00 USD | 2,140,000.00 USD | 24,040.00 USD | 6,440.00 USD | 24,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1131` | 2,990,000.00 USD | 2,990,000.00 USD | 12,540.00 USD | 0.00 USD | 25,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1133` | 2,200,000.00 USD | 2,200,000.00 USD | 8,350.00 USD | 19,820.00 USD | 24,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 12,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1135` | 2,210,000.00 USD | 2,210,000.00 USD | 7,500.00 USD | 3,200.00 USD | 5,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1135` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 6,800.00 USD | 9,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1137` | 2,220,000.00 USD | 2,220,000.00 USD | 4,040.00 USD | 1,090.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1137` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 2,240.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1139` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 844.95 USD | 5,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1139` | 3,030,000.00 USD | 3,030,000.00 USD | 2,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1141` | 2,250,000.00 USD | 2,250,000.00 USD | 8,110.00 USD | 0.00 USD | 21,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1141` | 3,050,000.00 USD | 3,050,000.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1143` | 2,310,000.00 USD | 2,310,000.00 USD | 19,450.00 USD | 22,390.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1143` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 78,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1145` | 2,350,000.00 USD | 2,350,000.00 USD | 9,770.00 USD | 6,840.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 3,290,000.00 USD | 3,290,000.00 USD | 16,540.00 USD | 2,730.00 USD | 141,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1147` | 2,380,000.00 USD | 2,380,000.00 USD | 5,270.00 USD | 9,400.00 USD | 18,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1147` | 3,430,000.00 USD | 3,430,000.00 USD | 9,880.00 USD | 0.00 USD | 138,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1149` | 3,520,000.00 USD | 3,520,000.00 USD | 10,560.00 USD | 0.00 USD | 72,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 3,740,000.00 USD | 3,740,000.00 USD | 92,570.00 USD | 4,210.00 USD | 128,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1153` | 4,030,000.00 USD | 4,030,000.00 USD | 136,660.00 USD | 8,400.00 USD | 146,040.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.0863` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 0.00 USD | 1,880.00 USD | 7,030.00 USD |
| `7D` | `0.0865` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 0.00 USD | 1,980.00 USD | 13,320.00 USD |
| `7D` | `0.0867` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 2,130.00 USD |
| `7D` | `0.0869` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 2,900.00 USD |
| `7D` | `0.0871` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 0.00 USD | 1,200.00 USD | 2,840.00 USD |
| `7D` | `0.0873` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 4,480.00 USD |
| `7D` | `0.0875` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 6,010.00 USD | 0.00 USD | 4,270.00 USD |
| `7D` | `0.0877` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 7,820.00 USD | 6,050.00 USD | 22,760.00 USD |
| `7D` | `0.0879` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 1,370.00 USD | 2,010.00 USD | 13,370.00 USD |
| `7D` | `0.0881` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 9,390.00 USD | 2,270.00 USD | 5,520.00 USD |
| `7D` | `0.0883` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 7,040.00 USD | 6,800.00 USD | 21,780.00 USD |
| `7D` | `0.0885` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,000.00 USD | 1,220.00 USD | 2,060.00 USD |
| `7D` | `0.0887` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 10,610.00 USD | 2,920.00 USD | 17,500.00 USD |
| `7D` | `0.0889` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 10,710.00 USD | 3,200.00 USD | 13,150.00 USD |
| `7D` | `0.0891` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 6,310.00 USD | 3,960.00 USD | 2,090.00 USD |
| `7D` | `0.0893` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 5,230.00 USD | 3,080.00 USD | 5,100.00 USD |
| `7D` | `0.0895` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 4,480.00 USD | 2,110.00 USD | 5,530.00 USD |
| `7D` | `0.0897` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 4,670.00 USD | 0.00 USD | 1,330.00 USD |
| `7D` | `0.0899` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 0.00 USD | 927.82 USD | 4,720.00 USD |
| `7D` | `0.0901` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 1,250.00 USD | 428.11 USD | 17.63 USD |
| `7D` | `0.0903` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 5,330.00 USD | 1,480.00 USD | 2,780.00 USD |
| `7D` | `0.0905` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 6,050.00 USD | 0.00 USD | 2,580.00 USD |
| `7D` | `0.0907` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 2,780.00 USD | 2,880.00 USD | 2,950.00 USD |
| `7D` | `0.0909` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 1,180.00 USD | 2,200.00 USD | 7.96 USD |
| `7D` | `0.0911` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 2,650.00 USD |
| `7D` | `0.0915` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 1,670.00 USD | 903.90 USD | 161.63 USD |
| `1D` | `0.0917` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 10,440.00 USD | 5,980.00 USD | 262.44 USD |
| `7D` | `0.0917` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 8,180.00 USD |
| `1D` | `0.0919` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 8,950.00 USD | 1,090.00 USD | 19,100.00 USD |
| `7D` | `0.0919` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 7,440.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0921` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 758.20 USD | 2,040.00 USD | 3,820.00 USD |
| `7D` | `0.0921` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 0.00 USD | 2,030.00 USD | 58.40 USD |
| `1D` | `0.0923` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 4,040.00 USD | 6,180.00 USD | 30,020.00 USD |
| `7D` | `0.0923` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 0.00 USD | 9,670.00 USD | 43,890.00 USD |
| `1D` | `0.0925` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 6,480.00 USD | 4,210.00 USD | 27,920.00 USD |
| `7D` | `0.0925` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 1,790.00 USD | 0.00 USD | 10,880.00 USD |
| `1D` | `0.0927` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 1,820.00 USD | 2,740.00 USD | 1,130.00 USD |
| `7D` | `0.0927` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 0.00 USD | 1,390.00 USD | 0.00 USD |
| `1D` | `0.0929` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 7,820.00 USD | 1,800.00 USD | 1,320.00 USD |
| `7D` | `0.0929` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 0.00 USD | 4,360.00 USD | 0.00 USD |
| `1D` | `0.0931` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 4,040.00 USD | 1,090.00 USD | 8,520.00 USD |
| `7D` | `0.0931` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 0.00 USD | 2,240.00 USD | 12,240.00 USD |
| `1D` | `0.0933` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 16,500.00 USD | 844.95 USD | 11,170.00 USD |
| `7D` | `0.0933` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 2,220.00 USD | 0.00 USD | 78.61 USD |
| `1D` | `0.0935` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 9,740.00 USD | 7,300.00 USD | 15,690.00 USD |
| `7D` | `0.0935` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 19,560.00 USD | 6,840.00 USD | 25,460.00 USD |
| `1D` | `0.0937` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 4,580.00 USD | 6,660.00 USD | 13,310.00 USD |
| `7D` | `0.0937` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 51.74 USD |
| `1D` | `0.0939` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 3,590.00 USD | 2,140.00 USD | 44,370.00 USD |
| `7D` | `0.0939` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 10,690.00 USD |
| `1D` | `0.0941` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 0.00 USD | 9,410.00 USD | 21,110.00 USD |
| `7D` | `0.0941` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 14,050.00 USD | 18,340.00 USD | 76,570.00 USD |
| `1D` | `0.0943` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 3,500.00 USD | 10,920.00 USD | 30,420.00 USD |
| `7D` | `0.0943` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 6,170.00 USD | 0.00 USD | 37,440.00 USD |
| `1D` | `0.0945` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 15,750.00 USD | 6,510.00 USD | 44,380.00 USD |
| `7D` | `0.0945` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 0.00 USD | 3,820.00 USD | 0.00 USD |
| `1D` | `0.0947` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 0.00 USD | 962.66 USD | 91.75 USD |
| `7D` | `0.0947` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 62.83 USD |
| `1D` | `0.0949` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 12,180.00 USD | 5,770.00 USD | 2,940.00 USD |
| `7D` | `0.0949` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 3,770.00 USD | 9,700.00 USD | 26,920.00 USD |
| `1D` | `0.0951` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 0.00 USD | 2,030.00 USD | 19,990.00 USD |
| `7D` | `0.0951` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 64.98 USD |
| `1D` | `0.0953` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 33,000.00 USD | 4,360.00 USD | 6,780.00 USD |
| `7D` | `0.0953` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 0.00 USD | 8,150.00 USD | 0.00 USD |
| `1D` | `0.0955` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 17,990.00 USD | 14,600.00 USD | 31,680.00 USD |
| `7D` | `0.0955` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 39,120.00 USD | 13,670.00 USD | 51,130.00 USD |
| `1D` | `0.0957` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 16,340.00 USD | 6,740.00 USD | 48,740.00 USD |
| `7D` | `0.0957` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 65.29 USD |
| `1D` | `0.0959` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 0.00 USD | 3,100.00 USD | 50.26 USD |
| `7D` | `0.0959` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 28,110.00 USD | 0.00 USD | 21,320.00 USD |
| `1D` | `0.0961` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 8,920.00 USD | 23,950.00 USD | 23,330.00 USD |
| `7D` | `0.0961` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 12,340.00 USD | 16,920.00 USD | 94,900.00 USD |
| `1D` | `0.0963` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 23,240.00 USD | 11,750.00 USD | 11,980.00 USD |
| `7D` | `0.0963` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 0.00 USD | 4,020.00 USD | 83.82 USD |
| `1D` | `0.0965` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 8,250.00 USD | 5,890.00 USD | 20,440.00 USD |
| `7D` | `0.0965` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 0.00 USD | 2,390.00 USD | 0.00 USD |
| `1D` | `0.0967` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 1,960.00 USD | 818.32 USD |
| `7D` | `0.0967` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 3,770.00 USD | 0.00 USD | 2,920.00 USD |
| `1D` | `0.0969` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 6,930.00 USD | 7,530.00 USD | 8,080.00 USD |
| `7D` | `0.0969` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 3,720.00 USD | 7,090.00 USD | 61,090.00 USD |
| `1D` | `0.0971` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 2,840.00 USD | 4,070.00 USD | 10,240.00 USD |
| `7D` | `0.0971` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 104.80 USD |
| `1D` | `0.0973` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 1,440.00 USD | 10,220.00 USD | 1,980.00 USD |
| `7D` | `0.0973` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD |
| `1D` | `0.0975` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 114.54 USD |
| `7D` | `0.0975` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 87.10 USD |
| `1D` | `0.0977` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 765.93 USD | 978.56 USD |
| `7D` | `0.0977` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 73.00 USD |
| `1D` | `0.0979` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 5,180.00 USD | 2,920.00 USD | 21,150.00 USD |
| `7D` | `0.0979` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 75.46 USD |
| `1D` | `0.0981` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 12,740.00 USD | 7,060.00 USD | 0.00 USD |
| `7D` | `0.0981` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 22,280.00 USD | 5,070.00 USD | 148.75 USD |
| `1D` | `0.0983` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 11,130.00 USD | 16,910.00 USD | 10,320.00 USD |
| `7D` | `0.0983` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 0.00 USD | 8,770.00 USD | 11,430.00 USD |
| `1D` | `0.0985` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 5,970.00 USD | 8,750.00 USD | 12,480.00 USD |
| `7D` | `0.0985` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 5,330.00 USD | 16,370.00 USD | 0.00 USD |
| `1D` | `0.0987` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 30,280.00 USD | 7,610.00 USD | 16,110.00 USD |
| `7D` | `0.0987` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 5,390.00 USD | 15,350.00 USD | 6,800.00 USD |
| `1D` | `0.0989` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 8,920.00 USD | 10,380.00 USD | 24,520.00 USD |
| `7D` | `0.0989` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 20,710.00 USD | 3,470.00 USD | 51.48 USD |
| `1D` | `0.0991` | 970,960.00 USD | 0.00 USD | 970,960.00 USD | 79,410.00 USD | 1,530.00 USD | 4,850.00 USD |
| `7D` | `0.0991` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 14,350.00 USD | 5,210.00 USD | 186.28 USD |
| `1D` | `0.0993` | 885,170.00 USD | 0.00 USD | 885,170.00 USD | 33,340.00 USD | 7,220.00 USD | 45,850.00 USD |
| `7D` | `0.0993` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 63,040.00 USD | 9,430.00 USD | 51,180.00 USD |
| `1D` | `0.0995` | 798,760.00 USD | 0.00 USD | 798,760.00 USD | 16,240.00 USD | 3,010.00 USD | 52,930.00 USD |
| `7D` | `0.0995` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 18,620.00 USD | 0.00 USD | 25,280.00 USD |
| `1D` | `0.0997` | 726,580.00 USD | 0.00 USD | 726,580.00 USD | 19,770.00 USD | 7,370.00 USD | 55,500.00 USD |
| `7D` | `0.0997` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 21,100.00 USD | 11,200.00 USD | 32,880.00 USD |
| `1D` | `0.0999` | 643,940.00 USD | 0.00 USD | 643,940.00 USD | 0.00 USD | 11,820.00 USD | 47,880.00 USD |
| `7D` | `0.0999` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 42,340.00 USD | 11,480.00 USD | 104,630.00 USD |
| `1D` | `0.1001` | 584,240.00 USD | 0.00 USD | 584,240.00 USD | 25,400.00 USD | 4,200.00 USD | 42,510.00 USD |
| `7D` | `0.1001` | 844,980.00 USD | 0.00 USD | 844,980.00 USD | 86,120.00 USD | 19,930.00 USD | 105,740.00 USD |
| `1D` | `0.1003` | 512,130.00 USD | 0.00 USD | 512,130.00 USD | 37,160.00 USD | 10,200.00 USD | 27,200.00 USD |
| `7D` | `0.1003` | 633,190.00 USD | 0.00 USD | 633,190.00 USD | 8,010.00 USD | 10,130.00 USD | 27,910.00 USD |
| `1D` | `0.1005` | 437,570.00 USD | 0.00 USD | 437,570.00 USD | 31,310.00 USD | 43,010.00 USD | 66,000.00 USD |
| `7D` | `0.1005` | 587,140.00 USD | 0.00 USD | 587,140.00 USD | 35,740.00 USD | 40,720.00 USD | 63,710.00 USD |
| `1D` | `0.1007` | 297,250.00 USD | 0.00 USD | 297,250.00 USD | 21,860.00 USD | 7,380.00 USD | 8,630.00 USD |
| `7D` | `0.1007` | 446,980.00 USD | 0.00 USD | 446,980.00 USD | 10,260.00 USD | 3,080.00 USD | 68,140.00 USD |
| `1D` | `0.1009` | 259,380.00 USD | 0.00 USD | 259,380.00 USD | 20,400.00 USD | 17,660.00 USD | 5,600.00 USD |
| `7D` | `0.1009` | 365,500.00 USD | 0.00 USD | 365,500.00 USD | 32,230.00 USD | 17,090.00 USD | 54,030.00 USD |
| `1D` | `0.1011` | 215,720.00 USD | 0.00 USD | 215,720.00 USD | 18,940.00 USD | 7,120.00 USD | 25,440.00 USD |
| `7D` | `0.1011` | 262,150.00 USD | 0.00 USD | 262,150.00 USD | 4,430.00 USD | 15,140.00 USD | 0.00 USD |
| `1D` | `0.1013` | 164,210.00 USD | 0.00 USD | 164,210.00 USD | 21,860.00 USD | 8,400.00 USD | 18,140.00 USD |
| `7D` | `0.1013` | 242,580.00 USD | 0.00 USD | 242,580.00 USD | 32,420.00 USD | 46,040.00 USD | 25,450.00 USD |
| `1D` | `0.1015` | 115,800.00 USD | 0.00 USD | 115,800.00 USD | 4,580.00 USD | 5,450.00 USD | 20,200.00 USD |
| `7D` | `0.1015` | 138,670.00 USD | 0.00 USD | 138,670.00 USD | 17,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1017` | 85,570.00 USD | 0.00 USD | 85,570.00 USD | 3,590.00 USD | 0.00 USD | 11,110.00 USD |
| `7D` | `0.1017` | 120,770.00 USD | 0.00 USD | 120,770.00 USD | 11,450.00 USD | 0.00 USD | 10,630.00 USD |
| `1D` | `0.1019` | 70,870.00 USD | 0.00 USD | 70,870.00 USD | 3,750.00 USD | 1,550.00 USD | 0.00 USD |
| `7D` | `0.1019` | 98,680.00 USD | 0.00 USD | 98,680.00 USD | 23,310.00 USD | 8,460.00 USD | 9,980.00 USD |
| `1D` | `0.1021` | 65,570.00 USD | 0.00 USD | 65,570.00 USD | 0.00 USD | 0.00 USD | 13,880.00 USD |
| `7D` | `0.1021` | 56,930.00 USD | 0.00 USD | 56,930.00 USD | 0.00 USD | 0.00 USD | 37,440.00 USD |
| `1D` | `0.1023` | 51,690.00 USD | 0.00 USD | 51,690.00 USD | 0.00 USD | 0.00 USD | 3,720.00 USD |
| `7D` | `0.1033` | 19,490.00 USD | 0.00 USD | 19,490.00 USD | 13,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1035` | 6,300.00 USD | 0.00 USD | 6,300.00 USD | 0.00 USD | 0.00 USD | 169.16 USD |
| `1D` | `0.1037` | 47,960.00 USD | 0.00 USD | 47,960.00 USD | 35,090.00 USD | 12,850.00 USD | 24.05 USD |
| `7D` | `0.1037` | 6,130.00 USD | 0.00 USD | 6,130.00 USD | 0.00 USD | 5,700.00 USD | 431.99 USD |
| `1D` | `0.1038` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1039` | 14,340.00 USD | 14,340.00 USD | 0.00 USD | 0.00 USD | 9,120.00 USD | 5,220.00 USD |
| `7D` | `0.1039` | 38,890.00 USD | 38,890.00 USD | 0.00 USD | 0.00 USD | 7,400.00 USD | 31,490.00 USD |
| `7D` | `0.1039` | 77,780.00 USD | 77,780.00 USD | 0.00 USD | 0.00 USD | 7,400.00 USD | 31,490.00 USD |
| `1D` | `0.1041` | 70,750.00 USD | 70,750.00 USD | 0.00 USD | 20,110.00 USD | 16,680.00 USD | 19,630.00 USD |
| `7D` | `0.1041` | 131,520.00 USD | 131,520.00 USD | 0.00 USD | 50,500.00 USD | 2,910.00 USD | 336.87 USD |
| `1D` | `0.1043` | 127,450.00 USD | 127,450.00 USD | 0.00 USD | 13,920.00 USD | 18,610.00 USD | 24,170.00 USD |
| `7D` | `0.1043` | 186,770.00 USD | 186,770.00 USD | 0.00 USD | 15,960.00 USD | 16,120.00 USD | 23,170.00 USD |
| `1D` | `0.1045` | 182,950.00 USD | 182,950.00 USD | 0.00 USD | 12,990.00 USD | 21,860.00 USD | 20,650.00 USD |
| `7D` | `0.1045` | 217,480.00 USD | 217,480.00 USD | 0.00 USD | 0.00 USD | 29,750.00 USD | 957.55 USD |
| `1D` | `0.1047` | 296,640.00 USD | 296,640.00 USD | 0.00 USD | 40,510.00 USD | 22,900.00 USD | 50,280.00 USD |
| `7D` | `0.1047` | 321,350.00 USD | 321,350.00 USD | 0.00 USD | 10,670.00 USD | 24,890.00 USD | 68,310.00 USD |
| `1D` | `0.1049` | 419,280.00 USD | 419,280.00 USD | 0.00 USD | 35,540.00 USD | 20,260.00 USD | 66,840.00 USD |
| `7D` | `0.1049` | 451,270.00 USD | 451,270.00 USD | 0.00 USD | 34,790.00 USD | 4,810.00 USD | 90,330.00 USD |
| `1D` | `0.1051` | 479,590.00 USD | 479,590.00 USD | 0.00 USD | 32,010.00 USD | 21,250.00 USD | 7,060.00 USD |
| `7D` | `0.1051` | 536,590.00 USD | 536,590.00 USD | 0.00 USD | 34,200.00 USD | 15,780.00 USD | 35,330.00 USD |
| `1D` | `0.1053` | 568,670.00 USD | 568,670.00 USD | 0.00 USD | 32,610.00 USD | 8,780.00 USD | 47,680.00 USD |
| `7D` | `0.1053` | 726,100.00 USD | 726,100.00 USD | 0.00 USD | 53,590.00 USD | 40,230.00 USD | 95,690.00 USD |
| `1D` | `0.1055` | 684,950.00 USD | 684,950.00 USD | 0.00 USD | 51,550.00 USD | 21,730.00 USD | 43,010.00 USD |
| `7D` | `0.1055` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 80,160.00 USD | 46,150.00 USD | 193,300.00 USD |
| `1D` | `0.1057` | 748,680.00 USD | 748,680.00 USD | 0.00 USD | 14,080.00 USD | 16,120.00 USD | 33,530.00 USD |
| `7D` | `0.1057` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 61,450.00 USD | 47,740.00 USD | 111,000.00 USD |
| `1D` | `0.1059` | 848,540.00 USD | 848,540.00 USD | 0.00 USD | 25,280.00 USD | 5,730.00 USD | 68,860.00 USD |
| `7D` | `0.1059` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 77,800.00 USD | 51,220.00 USD | 123,630.00 USD |
| `1D` | `0.1061` | 927,210.00 USD | 927,210.00 USD | 0.00 USD | 34,850.00 USD | 4,800.00 USD | 39,010.00 USD |
| `7D` | `0.1061` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 32,220.00 USD | 27,410.00 USD | 76,240.00 USD |
| `1D` | `0.1063` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 34,110.00 USD | 4,070.00 USD | 50,880.00 USD |
| `7D` | `0.1063` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 22,280.00 USD | 43,390.00 USD | 149,820.00 USD |
| `1D` | `0.1065` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 12,870.00 USD | 15,500.00 USD | 35,010.00 USD |
| `7D` | `0.1065` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 24,310.00 USD | 99,320.00 USD |
| `1D` | `0.1067` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 14,200.00 USD | 10,080.00 USD | 44,390.00 USD |
| `7D` | `0.1067` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 5,330.00 USD | 60,270.00 USD | 83,870.00 USD |
| `1D` | `0.1069` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 23,520.00 USD | 9,120.00 USD | 43,350.00 USD |
| `7D` | `0.1069` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD | 99,370.00 USD |
| `1D` | `0.1071` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 9,290.00 USD | 11,540.00 USD | 8,620.00 USD |
| `7D` | `0.1071` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 16,280.00 USD | 32,350.00 USD | 52,730.00 USD |
| `1D` | `0.1073` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 9,470.00 USD | 1,530.00 USD | 9,050.00 USD |
| `7D` | `0.1073` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 22,920.00 USD | 225.10 USD |
| `1D` | `0.1075` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 12,370.00 USD | 5,060.00 USD | 7,670.00 USD |
| `7D` | `0.1075` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 9,430.00 USD | 22,500.00 USD |
| `1D` | `0.1077` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 2,730.00 USD | 3,680.00 USD |
| `7D` | `0.1077` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 11,160.00 USD | 0.00 USD | 87.10 USD |
| `1D` | `0.1079` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 4,300.00 USD | 21,940.00 USD |
| `7D` | `0.1079` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 3,380.00 USD | 9,940.00 USD |
| `1D` | `0.1081` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 6,520.00 USD | 732.74 USD | 2,440.00 USD |
| `7D` | `0.1081` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1083` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 9,160.00 USD | 6,710.00 USD | 10,790.00 USD |
| `7D` | `0.1083` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 227.53 USD |
| `1D` | `0.1085` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 385.06 USD | 65,050.00 USD |
| `7D` | `0.1085` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 193.32 USD |
| `1D` | `0.1087` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 28,490.00 USD | 2,510.00 USD | 44,700.00 USD |
| `7D` | `0.1087` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,540.00 USD |
| `1D` | `0.1089` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 29,650.00 USD | 1,580.00 USD | 3,310.00 USD |
| `7D` | `0.1089` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 5,290.00 USD | 1,420.00 USD | 0.00 USD |
| `1D` | `0.1091` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 33,700.00 USD | 0.00 USD | 16.51 USD |
| `7D` | `0.1091` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 9,080.00 USD |
| `1D` | `0.1093` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 15,480.00 USD | 1,080.00 USD | 272.04 USD |
| `7D` | `0.1093` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 1,500.00 USD | 8,780.00 USD |
| `1D` | `0.1095` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 21,610.00 USD |
| `7D` | `0.1095` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 192.14 USD |
| `1D` | `0.1097` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 7,260.00 USD | 2,530.00 USD | 22,850.00 USD |
| `7D` | `0.1097` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 103.36 USD |
| `1D` | `0.1099` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 6,130.00 USD | 1,940.00 USD | 32.38 USD |
| `7D` | `0.1099` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 21,950.00 USD |
| `1D` | `0.1101` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 5,570.00 USD | 3,820.00 USD | 4,290.00 USD |
| `7D` | `0.1101` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1103` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 3,540.00 USD | 6,900.00 USD | 1,160.00 USD |
| `7D` | `0.1103` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 17,490.00 USD | 0.00 USD | 85.43 USD |
| `1D` | `0.1105` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 3,380.00 USD | 4,740.00 USD | 10,710.00 USD |
| `7D` | `0.1105` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 14,480.00 USD | 34.51 USD |
| `1D` | `0.1107` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 3,110.00 USD | 13,200.00 USD | 35,750.00 USD |
| `7D` | `0.1107` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 12,510.00 USD | 15,990.00 USD |
| `1D` | `0.1109` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 2,110.00 USD | 1,370.00 USD | 2,670.00 USD |
| `7D` | `0.1109` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 12,430.00 USD | 0.00 USD |
| `1D` | `0.1111` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 5,200.00 USD | 996.46 USD | 104.00 USD |
| `7D` | `0.1111` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 0.00 USD |
| `1D` | `0.1113` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 21,390.00 USD | 5,880.00 USD | 13,550.00 USD |
| `1D` | `0.1115` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 6,690.00 USD | 465.26 USD | 0.00 USD |
| `1D` | `0.1117` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 2,060.00 USD | 10,810.00 USD | 24,630.00 USD |
| `7D` | `0.1117` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | 16,490.00 USD |
| `1D` | `0.1119` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 23,420.00 USD | 4,920.00 USD | 31,040.00 USD |
| `7D` | `0.1119` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 34,550.00 USD | 7,050.00 USD | 21,750.00 USD |
| `1D` | `0.1121` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 21,300.00 USD | 12,810.00 USD | 12,350.00 USD |
| `7D` | `0.1121` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 5,730.00 USD | 0.00 USD | 27,480.00 USD |
| `1D` | `0.1123` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 30,640.00 USD | 2,870.00 USD | 8,450.00 USD |
| `7D` | `0.1123` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 19,800.00 USD | 23,980.00 USD | 37,780.00 USD |
| `1D` | `0.1125` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 11,890.00 USD | 12,350.00 USD | 11,740.00 USD |
| `7D` | `0.1125` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 4,250.00 USD | 36,220.00 USD |
| `1D` | `0.1127` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 1,670.00 USD | 4,120.00 USD | 22,900.00 USD |
| `7D` | `0.1127` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 2,720.00 USD | 7,980.00 USD |
| `1D` | `0.1129` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 11,080.00 USD | 1,390.00 USD | 7,770.00 USD |
| `7D` | `0.1129` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD | 9,280.00 USD |
| `1D` | `0.1131` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 24,040.00 USD | 6,440.00 USD | 24,260.00 USD |
| `7D` | `0.1131` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 12,540.00 USD | 0.00 USD | 25,970.00 USD |
| `1D` | `0.1133` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 8,350.00 USD | 19,820.00 USD | 24,600.00 USD |
| `7D` | `0.1133` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 12,810.00 USD | 0.00 USD |
| `1D` | `0.1135` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 7,500.00 USD | 3,200.00 USD | 5,390.00 USD |
| `7D` | `0.1135` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 6,800.00 USD | 9,060.00 USD |
| `1D` | `0.1137` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 4,040.00 USD | 1,090.00 USD | 1,090.00 USD |
| `7D` | `0.1137` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 2,240.00 USD | 9,310.00 USD |
| `1D` | `0.1139` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 844.95 USD | 5,420.00 USD |
| `7D` | `0.1139` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 2,220.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1141` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 8,110.00 USD | 0.00 USD | 21,310.00 USD |
| `7D` | `0.1141` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD |
| `1D` | `0.1143` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 19,450.00 USD | 22,390.00 USD | 10,490.00 USD |
| `7D` | `0.1143` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78,600.00 USD |
| `1D` | `0.1145` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 9,770.00 USD | 6,840.00 USD | 25,510.00 USD |
| `7D` | `0.1145` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 16,540.00 USD | 2,730.00 USD | 141,160.00 USD |
| `1D` | `0.1147` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 5,270.00 USD | 9,400.00 USD | 18,360.00 USD |
| `7D` | `0.1147` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 138,350.00 USD |
| `7D` | `0.1149` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 10,560.00 USD | 0.00 USD | 72,750.00 USD |
| `7D` | `0.1151` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 92,570.00 USD | 4,210.00 USD | 128,190.00 USD |
| `7D` | `0.1153` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 136,660.00 USD | 8,400.00 USD | 146,040.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `65.04M` | Total OI Tokens: `626,217,517.8 OP`
  * 1h OI Change: `+1.46%` | 4h OI Change: `+0.61%` | 24h OI Change: `-11.22%`
  * Exchange Breakdown: Binance=`14.15M` | Bybit=`12.95M` | OKX=`4.11M` | Hyperliquid=`3.17M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-3.54K` | Last 24h: `-4.25K` | Last 3d: `-11.30K` | Last 7d: `-13.94K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0181%` | **USDT OKX** | `-0.0285%` |
| **USDT Bybit** | `0.0028%` | **USDT KuCoin** | `-0.0063%` |
| **USDT MEXC** | `-0.0187%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `45.00%` | `55.00%` | `0.82` | 1,300,000.00 USD |
| `15M` | `Binance` | `55.85%` | `44.15%` | `1.27` | 297,740.00 USD |
| `15M` | `OKX` | `52.84%` | `47.16%` | `1.12` | 100,060.00 USD |
| `15M` | `Bybit` | `60.82%` | `39.18%` | `1.55` | 131,930.00 USD |
| `15M` | `KuCoin` | `56.87%` | `43.13%` | `1.32` | 143,140.00 USD |
| `15M` | `Gate` | `39.78%` | `60.22%` | `0.66` | 16,370.00 USD |
| `15M` | `Bitget` | `63.37%` | `36.63%` | `1.73` | 80,560.00 USD |
| `15M` | `BingX` | `11.15%` | `88.85%` | `0.13` | 305,510.00 USD |
| `15M` | `MEXC` | `56.3%` | `43.7%` | `1.29` | 96,130.00 USD |
| `15M` | `Bitunix` | `60.36%` | `39.64%` | `1.52` | 11,120.00 USD |
| `15M` | `Hyperliquid` | `69.19%` | `30.81%` | `2.25` | 4,730.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.04%` | `48.96%` | `1.04` | 52,430.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `35.93%` | `64.07%` | `0.56` | 59,830.00 USD |
| `15M` | `HTX` | `55.53%` | `44.47%` | `1.25` | 0.56 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 287.96 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `28.88%` | `71.12%` | `0.41` | 727.38 USD |
| `15M` | `Whale Positions` | `55.85%` | `44.15%` | `1.27` | 297,740.00 USD |
| `15M` | `Global Accounts` | `45.00%` | `55.00%` | `0.82` | 1,300,000.00 USD |
| `1H` | `OP` | `55.22%` | `44.78%` | `1.23` | 4,020,000.00 USD |
| `1H` | `Binance` | `56.54%` | `43.46%` | `1.30` | 1,320,000.00 USD |
| `1H` | `OKX` | `55.61%` | `44.39%` | `1.25` | 315,520.00 USD |
| `1H` | `Bybit` | `56.53%` | `43.47%` | `1.30` | 450,870.00 USD |
| `1H` | `KuCoin` | `51.42%` | `48.58%` | `1.06` | 608,440.00 USD |
| `1H` | `Gate` | `43.43%` | `56.57%` | `0.77` | 80,730.00 USD |
| `1H` | `Bitget` | `68.35%` | `31.65%` | `2.16` | 213,400.00 USD |
| `1H` | `BingX` | `51.46%` | `48.54%` | `1.06` | 225,260.00 USD |
| `1H` | `MEXC` | `50.64%` | `49.36%` | `1.03` | 166,500.00 USD |
| `1H` | `Bitunix` | `34.58%` | `65.42%` | `0.53` | 72,240.00 USD |
| `1H` | `Hyperliquid` | `90.77%` | `9.23%` | `9.83` | 127,080.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.27%` | `49.73%` | `1.01` | 200,880.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `42.52%` | `57.48%` | `0.74` | 222,580.00 USD |
| `1H` | `HTX` | `44.06%` | `55.94%` | `0.79` | 667.46 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `78.81%` | `21.19%` | `3.72` | 5,800.00 USD |
| `1H` | `Aster` | `94.26%` | `5.74%` | `16.42` | 5,510.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `64.72%` | `35.28%` | `1.83` | 5,020.00 USD |
| `1H` | `Whale Positions` | `56.54%` | `43.46%` | `1.30` | 1,320,000.00 USD |
| `1H` | `Global Accounts` | `55.22%` | `44.78%` | `1.23` | 4,020,000.00 USD |
| `4H` | `OP` | `47.70%` | `52.30%` | `0.91` | 46,140,000.00 USD |
| `4H` | `Binance` | `47.86%` | `52.14%` | `0.92` | 13,000,000.00 USD |
| `4H` | `OKX` | `39.62%` | `60.38%` | `0.66` | 4,470,000.00 USD |
| `4H` | `Bybit` | `46.39%` | `53.61%` | `0.87` | 3,650,000.00 USD |
| `4H` | `KuCoin` | `46.9%` | `53.1%` | `0.88` | 315,610.00 USD |
| `4H` | `Gate` | `51.27%` | `48.73%` | `1.05` | 4,150,000.00 USD |
| `4H` | `Bitget` | `42.89%` | `57.11%` | `0.75` | 1,360,000.00 USD |
| `4H` | `BingX` | `33.64%` | `66.36%` | `0.51` | 10,760,000.00 USD |
| `4H` | `MEXC` | `57.96%` | `42.04%` | `1.38` | 1,150,000.00 USD |
| `4H` | `Bitunix` | `47.5%` | `52.5%` | `0.90` | 967,350.00 USD |
| `4H` | `Hyperliquid` | `45.04%` | `54.96%` | `0.82` | 370,400.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.76%` | `49.24%` | `1.03` | 1,080,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `93.83%` | `6.17%` | `15.21` | 3,860,000.00 USD |
| `4H` | `HTX` | `43.58%` | `56.42%` | `0.77` | 84,440.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `62.46%` | `37.54%` | `1.66` | 244,300.00 USD |
| `4H` | `Aster` | `45.78%` | `54.22%` | `0.84` | 28,160.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `27.65%` | `72.35%` | `0.38` | 645,830.00 USD |
| `4H` | `Whale Positions` | `47.86%` | `52.14%` | `0.92` | 13,000,000.00 USD |
| `4H` | `Global Accounts` | `47.70%` | `52.30%` | `0.91` | 46,140,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1033` | `0.1034` | `0.1033` | `0.1038` | `0.1032` | 260,043.89 USD | 128,207.87 USD | 131,836.02 USD | -3,628.15 USD | `-1.40%` | `11B / 2S` |
| `0:00 UTC` | `0.1024` | `0.1027` | `0.1024` | `0.1032` | `0.1023` | 294,713.35 USD | 140,222.38 USD | 154,490.97 USD | -14,268.58 USD | `-4.84%` | `9B / 14S` |
| `5:00 UTC` | `0.1024` | `0.1025` | `0.1024` | `0.1030` | `0.1023` | 189,660.77 USD | 110,909.31 USD | 78,751.47 USD | 32,157.84 USD | `+16.96%` | `13B / 15S` |
| `0:00 UTC` | `0.1021` | `0.1022` | `0.1021` | `0.1027` | `0.1019` | 366,904.35 USD | 146,868.15 USD | 220,036.20 USD | -73,168.05 USD | `-19.94%` | `9B / 16S` |
| `5:00 UTC` | `0.1020` | `0.1021` | `0.1020` | `0.1024` | `0.1019` | 314,873.64 USD | 167,532.45 USD | 147,341.19 USD | 20,191.27 USD | `+6.41%` | `10B / 2S` |
| `0:00 UTC` | `0.1019` | `0.1024` | `0.1019` | `0.1029` | `0.1019` | 191,273.46 USD | 92,786.86 USD | 98,486.60 USD | -5,699.74 USD | `-2.98%` | `22B / 16S` |
| `5:00 UTC` | `0.1028` | `0.1029` | `0.1028` | `0.1034` | `0.1023` | 237,952.24 USD | 133,825.41 USD | 104,126.84 USD | 29,698.57 USD | `+12.48%` | `22B / 24S` |
| `0:00 UTC` | `0.1030` | `0.1032` | `0.1030` | `0.1036` | `0.1028` | 441,050.39 USD | 212,264.29 USD | 228,786.10 USD | -16,521.82 USD | `-3.75%` | `9B / 18S` |
| `5:00 UTC` | `0.1036` | `0.1033` | `0.1036` | `0.1037` | `0.1029` | 224,777.59 USD | 109,477.97 USD | 115,299.62 USD | -5,821.65 USD | `-2.59%` | `10B / 10S` |
| `0:00 UTC` | `0.1039` | `0.1038` | `0.1039` | `0.1041` | `0.1032` | 162,487.90 USD | 87,544.44 USD | 74,943.45 USD | 12,600.99 USD | `+7.76%` | `18B / 9S` |

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
| `5m` | 3,270.00 USD | 124,440.00 USD | **`ACCUMULATION`** |
| `15m` | 1,800.00 USD | 147,290.00 USD | **`ACCUMULATION`** |
| `30m` | -14,070.00 USD | 109,660.00 USD | **`ACCUMULATION`** |
| `1h` | -16,500.00 USD | 190,830.00 USD | **`ACCUMULATION`** |
| `2h` | -82,430.00 USD | -16,910.00 USD | **`DISTRIBUTION`** |
| `4h` | -34,440.00 USD | 78,380.00 USD | **`ACCUMULATION`** |
| `6h` | 20,530.00 USD | 673,600.00 USD | **`ACCUMULATION`** |
| `8h` | -153,970.00 USD | 684,560.00 USD | **`ACCUMULATION`** |
| `12h` | -4,600.00 USD | -1,270,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 222,740.00 USD | -3,740,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -317,940.00 USD | -12,530,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,270,000.00 USD | -83,020,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+3.27K` | 15m=`+1.80K` | 1h=`-16.50K` | 24h=`+222.74K`
* Futures Capital Netflows: 5m=`+124.44K` | 15m=`+147.29K` | 1h=`+190.83K` | 24h=`-3.74M`
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
  * `2026-10-30 15:49:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:45 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:45 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
