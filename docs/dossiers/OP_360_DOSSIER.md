# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 16:42:50 IST` (`2026-10-30 11:12:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1048` | `0.1050` | `0.1045` | `0.1046` | `898,783` | 94,126.64 USD | -17,169.07 USD | `-18.24%` | -1,936,840.15 USD | `-0.94` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1047` | `0.1050` | `0.1046` | `0.1049` | `730,834` | 76,611.60 USD | -11,937.99 USD | `-15.58%` | -1,948,778.14 USD | `-0.60` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.1049` | `0.1050` | `0.1047` | `0.1047` | `138,764` | 14,542.03 USD | 1,129.24 USD | `+7.77%` | -1,947,648.90 USD | `+0.06` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1032` | `0.1041` | `0.1032` | `0.1040` | `2,532,549` | 262,943.08 USD | -17,690.08 USD | `-6.73%` | -1,951,640.84 USD | `-0.71` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1040` | `0.1049` | `0.1038` | `0.1048` | `2,143,056` | 223,592.72 USD | 31,969.77 USD | `+14.30%` | -1,919,671.07 USD | `+0.65` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1048` | `0.1050` | `0.1045` | `0.1047` | `1,768,381` | 185,280.26 USD | -27,977.83 USD | `-15.10%` | -1,947,648.90 USD | `-0.92` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1024` | `0.1034` | `0.1019` | `0.1034` | `10,854,845` | 1,111,003.69 USD | -28,977.96 USD | `-2.61%` | -1,820,323.01 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1034` | `0.1049` | `0.1028` | `0.1048` | `11,125,022` | 1,152,363.79 USD | -8,063.78 USD | `-0.70%` | -1,828,386.79 USD | `+0.22` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1048` | `0.1050` | `0.1045` | `0.1047` | `1,768,440` | 185,286.38 USD | -27,971.72 USD | `-15.10%` | -1,856,358.50 USD | `+0.18` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,490,108.93 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1040` | `0.0988` | `0.1027` | `54,609,324` | 5,566,939.91 USD | 608,714.61 USD | `+10.93%` | -1,881,394.33 USD | `+1.21` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1027` | `0.1050` | `0.1019` | `0.1047` | `34,484,949` | 3,552,782.02 USD | 25,029.71 USD | `+0.70%` | -1,856,364.62 USD | `+0.44` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | 165,115.32 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -1,152,082.54 USD | `-1.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,490,108.93 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1040` | `0.0988` | `0.1027` | `54,609,324` | 5,566,939.91 USD | 608,714.61 USD | `+10.93%` | -1,881,394.33 USD | `+1.21` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1027` | `0.1050` | `0.1019` | `0.1047` | `34,484,949` | 3,552,782.02 USD | 25,029.71 USD | `+0.70%` | -1,856,364.62 USD | `+0.44` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:42:20 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `Live` | `Long Liquidation` | `0.0305` | 1,320.00 USD | 122,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0385` | 231.00 USD | 121,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 277.89 USD | 120,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0555` | 425.34 USD | 120,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 3,940.00 USD | 120,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 844.12 USD | 116,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 315.09 USD | 115,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 353.81 USD | 115,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 518.48 USD | 114,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 1,920.00 USD | 114,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 1,090.00 USD | 112,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 40,420.00 USD | 111,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 23,910.00 USD | 70,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,530.00 USD | 46,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,300.00 USD | 44,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 12,440.00 USD | 42,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 1,170.00 USD | 29,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 878.62 USD | 28,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 1,920.00 USD | 27,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 1,110.00 USD | 25,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 223.98 USD | 24,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 1,560.00 USD | 24,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 140.74 USD | 22,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 14,300.00 USD | 22,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 1,710.00 USD | 8,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0862` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 1,880.00 USD | 6,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0864` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 1,980.00 USD | 15,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0865` | 318.30 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0866` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0868` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0870` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0872` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 1,200.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0874` | 2,750,000.00 USD | 2,750,000.00 USD | 6,010.00 USD | 0.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0875` | 793.17 USD | 6,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0876` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 1,770.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0878` | 2,730,000.00 USD | 2,730,000.00 USD | 9,200.00 USD | 5,890.00 USD | 25,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0880` | 2,690,000.00 USD | 2,690,000.00 USD | 3,770.00 USD | 2,200.00 USD | 11,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0882` | 2,670,000.00 USD | 2,670,000.00 USD | 12,660.00 USD | 7,260.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0884` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 1,220.00 USD | 13,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0886` | 2,630,000.00 USD | 2,630,000.00 USD | 9,350.00 USD | 2,470.00 USD | 11,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0888` | 2,610,000.00 USD | 2,610,000.00 USD | 3,370.00 USD | 2,720.00 USD | 8,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0890` | 2,590,000.00 USD | 2,590,000.00 USD | 13,510.00 USD | 3,610.00 USD | 13,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0892` | 2,560,000.00 USD | 2,560,000.00 USD | 3,620.00 USD | 3,060.00 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0894` | 2,550,000.00 USD | 2,550,000.00 USD | 5,480.00 USD | 3,400.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,270.00 USD | 5,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0896` | 2,540,000.00 USD | 2,540,000.00 USD | 4,300.00 USD | 0.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0898` | 2,530,000.00 USD | 2,530,000.00 USD | 3,390.00 USD | 927.82 USD | 4,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0900` | 2,520,000.00 USD | 2,520,000.00 USD | 1,250.00 USD | 428.11 USD | 77.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0902` | 2,520,000.00 USD | 2,520,000.00 USD | 1,030.00 USD | 482.67 USD | 1,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0904` | 2,520,000.00 USD | 2,520,000.00 USD | 5,730.00 USD | 996.61 USD | 1,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0905` | 2,230.00 USD | 2,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0906` | 2,510,000.00 USD | 2,510,000.00 USD | 6,040.00 USD | 1,900.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0908` | 2,500,000.00 USD | 2,500,000.00 USD | 2,540.00 USD | 2,570.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0910` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 606.54 USD | 48.03 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0912` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 2,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0914` | 2,490,000.00 USD | 2,490,000.00 USD | 1,670.00 USD | 903.90 USD | 56.36 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0916` | 2,380,000.00 USD | 2,380,000.00 USD | 6,590.00 USD | 2,510.00 USD | 257.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0916` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 6,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0918` | 2,370,000.00 USD | 2,370,000.00 USD | 6,400.00 USD | 4,060.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0918` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0920` | 2,360,000.00 USD | 2,360,000.00 USD | 6,400.00 USD | 1,320.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0920` | 2,470,000.00 USD | 2,470,000.00 USD | 7,440.00 USD | 2,030.00 USD | 223.39 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0922` | 2,330,000.00 USD | 2,330,000.00 USD | 2,430.00 USD | 4,100.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0922` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 7,660.00 USD | 34,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0924` | 2,310,000.00 USD | 2,310,000.00 USD | 4,790.00 USD | 4,700.00 USD | 43,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0924` | 2,420,000.00 USD | 2,420,000.00 USD | 1,790.00 USD | 2,020.00 USD | 11,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0926` | 2,250,000.00 USD | 2,250,000.00 USD | 5,130.00 USD | 4,460.00 USD | 555.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0926` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0928` | 2,240,000.00 USD | 2,240,000.00 USD | 2,600.00 USD | 1,100.00 USD | 1,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0928` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0930` | 2,240,000.00 USD | 2,240,000.00 USD | 7,300.00 USD | 2,440.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0930` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 5,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0932` | 2,220,000.00 USD | 2,220,000.00 USD | 2,710.00 USD | 1,300.00 USD | 5,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0932` | 2,390,000.00 USD | 2,390,000.00 USD | 2,220.00 USD | 0.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0934` | 2,210,000.00 USD | 2,210,000.00 USD | 22,030.00 USD | 3,830.00 USD | 17,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0936` | 2,170,000.00 USD | 2,170,000.00 USD | 7,080.00 USD | 9,360.00 USD | 16,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0936` | 2,380,000.00 USD | 2,380,000.00 USD | 19,560.00 USD | 6,840.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0938` | 2,130,000.00 USD | 2,130,000.00 USD | 8,170.00 USD | 2,920.00 USD | 46,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0938` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 248.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0940` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0940` | 2,320,000.00 USD | 2,320,000.00 USD | 14,050.00 USD | 0.00 USD | 10,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0942` | 2,080,000.00 USD | 2,080,000.00 USD | 3,500.00 USD | 16,110.00 USD | 49,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0942` | 2,300,000.00 USD | 2,300,000.00 USD | 6,170.00 USD | 18,340.00 USD | 114,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0944` | 2,010,000.00 USD | 2,010,000.00 USD | 11,620.00 USD | 4,860.00 USD | 36,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0944` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 2,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0946` | 1,950,000.00 USD | 1,950,000.00 USD | 4,130.00 USD | 5,280.00 USD | 10,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0946` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 1,810.00 USD | 154.22 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0948` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 1,100.00 USD | 101.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0948` | 2,160,000.00 USD | 2,160,000.00 USD | 3,770.00 USD | 0.00 USD | 26,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0950` | 1,930,000.00 USD | 1,930,000.00 USD | 12,180.00 USD | 6,710.00 USD | 22,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0950` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 9,700.00 USD | 134.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0952` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 853.02 USD | 6,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0952` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 4,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0954` | 1,880,000.00 USD | 1,880,000.00 USD | 41,470.00 USD | 11,160.00 USD | 21,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0954` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 3,740.00 USD | 187.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0956` | 1,810,000.00 USD | 1,810,000.00 USD | 18,680.00 USD | 9,390.00 USD | 37,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0956` | 2,110,000.00 USD | 2,110,000.00 USD | 39,120.00 USD | 13,670.00 USD | 50,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0958` | 1,740,000.00 USD | 1,740,000.00 USD | 7,180.00 USD | 4,290.00 USD | 22,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0958` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0960` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 16,940.00 USD | 146.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0960` | 1,980,000.00 USD | 1,980,000.00 USD | 28,110.00 USD | 16,920.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0962` | 1,690,000.00 USD | 1,690,000.00 USD | 8,920.00 USD | 15,440.00 USD | 27,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0962` | 1,920,000.00 USD | 1,920,000.00 USD | 12,340.00 USD | 0.00 USD | 75,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0964` | 1,640,000.00 USD | 1,640,000.00 USD | 31,490.00 USD | 10,380.00 USD | 27,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0964` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 4,020.00 USD | 86.68 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0966` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 3,880.00 USD | 815.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0966` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 2,390.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0968` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 2,960.00 USD | 2,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0968` | 1,820,000.00 USD | 1,820,000.00 USD | 7,490.00 USD | 0.00 USD | 56,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0970` | 1,560,000.00 USD | 1,560,000.00 USD | 8,360.00 USD | 8,640.00 USD | 16,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0970` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 7,090.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0972` | 1,530,000.00 USD | 1,530,000.00 USD | 2,860.00 USD | 3,220.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0972` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 8,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0974` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 7,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0974` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 7,480.00 USD | 104.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0976` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 765.93 USD | 1,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0976` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 179.57 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0978` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 817.22 USD | 67.90 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0980` | 1,510,000.00 USD | 1,510,000.00 USD | 12,700.00 USD | 4,570.00 USD | 21,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0980` | 1,730,000.00 USD | 1,730,000.00 USD | 22,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0982` | 1,470,000.00 USD | 1,470,000.00 USD | 10,790.00 USD | 7,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0982` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 5,070.00 USD | 11,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0984` | 1,450,000.00 USD | 1,450,000.00 USD | 10,310.00 USD | 19,740.00 USD | 15,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0984` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 16,160.00 USD | 90.68 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0986` | 1,410,000.00 USD | 1,410,000.00 USD | 7,260.00 USD | 8,960.00 USD | 11,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0986` | 1,670,000.00 USD | 1,670,000.00 USD | 5,330.00 USD | 16,520.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0988` | 1,380,000.00 USD | 1,380,000.00 USD | 30,450.00 USD | 7,150.00 USD | 33,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0988` | 1,650,000.00 USD | 1,650,000.00 USD | 10,360.00 USD | 7,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0990` | 1,310,000.00 USD | 1,310,000.00 USD | 12,880.00 USD | 4,730.00 USD | 4,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0990` | 1,630,000.00 USD | 1,630,000.00 USD | 30,090.00 USD | 6,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0992` | 1,290,000.00 USD | 1,290,000.00 USD | 84,750.00 USD | 7,620.00 USD | 30,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0992` | 1,590,000.00 USD | 1,590,000.00 USD | 12,790.00 USD | 11,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0994` | 1,160,000.00 USD | 1,160,000.00 USD | 32,970.00 USD | 3,250.00 USD | 20,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0994` | 1,570,000.00 USD | 1,570,000.00 USD | 55,790.00 USD | 0.00 USD | 65,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0996` | 1,110,000.00 USD | 1,110,000.00 USD | 15,040.00 USD | 2,450.00 USD | 74,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0996` | 1,450,000.00 USD | 1,450,000.00 USD | 27,010.00 USD | 5,500.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0998` | 1,020,000.00 USD | 1,020,000.00 USD | 12,990.00 USD | 5,820.00 USD | 57,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0998` | 1,380,000.00 USD | 1,380,000.00 USD | 21,180.00 USD | 11,540.00 USD | 113,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1000` | 939,040.00 USD | 939,040.00 USD | 10,360.00 USD | 16,010.00 USD | 35,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1000` | 1,230,000.00 USD | 1,230,000.00 USD | 54,220.00 USD | 25,020.00 USD | 33,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1002` | 877,210.00 USD | 877,210.00 USD | 17,830.00 USD | 4,080.00 USD | 42,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1002` | 1,120,000.00 USD | 1,120,000.00 USD | 70,060.00 USD | 10,690.00 USD | 74,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1004` | 812,380.00 USD | 812,380.00 USD | 53,750.00 USD | 30,530.00 USD | 49,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1004` | 965,740.00 USD | 965,740.00 USD | 19,310.00 USD | 17,550.00 USD | 46,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1006` | 678,810.00 USD | 678,810.00 USD | 24,030.00 USD | 23,800.00 USD | 29,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1006` | 882,750.00 USD | 882,750.00 USD | 23,200.00 USD | 23,170.00 USD | 67,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1008` | 601,160.00 USD | 601,160.00 USD | 17,840.00 USD | 11,220.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1008` | 769,250.00 USD | 769,250.00 USD | 13,040.00 USD | 5,470.00 USD | 96,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1010` | 568,340.00 USD | 568,340.00 USD | 23,240.00 USD | 13,530.00 USD | 23,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1010` | 654,220.00 USD | 654,220.00 USD | 29,550.00 USD | 24,610.00 USD | 3,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1012` | 507,830.00 USD | 507,830.00 USD | 16,360.00 USD | 9,190.00 USD | 19,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1012` | 596,070.00 USD | 596,070.00 USD | 6,490.00 USD | 35,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1014` | 462,740.00 USD | 462,740.00 USD | 13,540.00 USD | 6,940.00 USD | 16,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1014` | 553,910.00 USD | 553,910.00 USD | 40,860.00 USD | 15,590.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1016` | 425,270.00 USD | 425,270.00 USD | 8,170.00 USD | 775.38 USD | 23,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1016` | 472,010.00 USD | 472,010.00 USD | 14,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1018` | 393,170.00 USD | 393,170.00 USD | 18,090.00 USD | 1,550.00 USD | 3,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1018` | 458,010.00 USD | 458,010.00 USD | 39,450.00 USD | 0.00 USD | 10,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1020` | 370,110.00 USD | 370,110.00 USD | 0.00 USD | 0.00 USD | 11,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1020` | 407,930.00 USD | 407,930.00 USD | 0.00 USD | 8,460.00 USD | 47,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1022` | 358,530.00 USD | 358,530.00 USD | 0.00 USD | 0.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1026` | 352,500.00 USD | 352,500.00 USD | 0.00 USD | 1,650.00 USD | 1,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1032` | 352,040.00 USD | 352,040.00 USD | 13,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1036` | 349,250.00 USD | 349,250.00 USD | 2,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1036` | 338,860.00 USD | 338,860.00 USD | 0.00 USD | 0.00 USD | 108.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1038` | 347,090.00 USD | 347,090.00 USD | 0.00 USD | 14,190.00 USD | 24.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1038` | 338,750.00 USD | 338,750.00 USD | 0.00 USD | 10,870.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1040` | 332,880.00 USD | 332,880.00 USD | 0.00 USD | 19,120.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1040` | 296,530.00 USD | 296,530.00 USD | 0.00 USD | 5,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1042` | 298,610.00 USD | 298,610.00 USD | 22,890.00 USD | 9,410.00 USD | 25,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1042` | 291,390.00 USD | 291,390.00 USD | 49,380.00 USD | 12,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1044` | 240,540.00 USD | 240,540.00 USD | 24,130.00 USD | 36,390.00 USD | 23,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1044` | 229,820.00 USD | 229,820.00 USD | 11,140.00 USD | 25,310.00 USD | 22,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1046` | 156,490.00 USD | 156,490.00 USD | 16,570.00 USD | 0.00 USD | 31.28 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1046` | 170,670.00 USD | 170,670.00 USD | 0.00 USD | 23,140.00 USD | 60,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1048` | 139,890.00 USD | 139,890.00 USD | 36,040.00 USD | 17,510.00 USD | 86,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1048` | 87,380.00 USD | 87,380.00 USD | 30,640.00 USD | 14,940.00 USD | 41,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1050` | 58,710.00 USD | 58,710.00 USD | 32,940.00 USD | 21,980.00 USD | 3,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1050` | 90,920.00 USD | 90,920.00 USD | 27,290.00 USD | 0.00 USD | 63,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1052` | 143,940.00 USD | 143,940.00 USD | 39,930.00 USD | 15,010.00 USD | 30,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1052` | 262,040.00 USD | 262,040.00 USD | 32,640.00 USD | 34,840.00 USD | 103,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1054` | 265,840.00 USD | 265,840.00 USD | 45,620.00 USD | 18,770.00 USD | 57,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1054` | 493,860.00 USD | 493,860.00 USD | 85,290.00 USD | 53,700.00 USD | 92,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1056` | 343,490.00 USD | 343,490.00 USD | 25,800.00 USD | 23,260.00 USD | 28,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1056` | 803,320.00 USD | 803,320.00 USD | 87,170.00 USD | 47,540.00 USD | 174,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1058` | 442,790.00 USD | 442,790.00 USD | 25,860.00 USD | 6,490.00 USD | 66,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1058` | 1,020,000.00 USD | 1,020,000.00 USD | 54,790.00 USD | 24,600.00 USD | 136,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1060` | 516,960.00 USD | 516,960.00 USD | 44,720.00 USD | 2,700.00 USD | 26,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1060` | 1,210,000.00 USD | 1,210,000.00 USD | 55,680.00 USD | 51,150.00 USD | 79,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1062` | 617,110.00 USD | 617,110.00 USD | 44,570.00 USD | 4,130.00 USD | 51,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1062` | 1,360,000.00 USD | 1,360,000.00 USD | 46,950.00 USD | 28,310.00 USD | 82,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1064` | 660,590.00 USD | 660,590.00 USD | 6,960.00 USD | 7,730.00 USD | 28,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1064` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 42,470.00 USD | 144,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1066` | 734,360.00 USD | 734,360.00 USD | 15,590.00 USD | 15,700.00 USD | 42,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1066` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 42,670.00 USD | 107,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1068` | 806,920.00 USD | 806,920.00 USD | 11,970.00 USD | 9,310.00 USD | 51,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1068` | 1,830,000.00 USD | 1,830,000.00 USD | 5,330.00 USD | 41,360.00 USD | 79,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1070` | 858,600.00 USD | 858,600.00 USD | 23,200.00 USD | 11,060.00 USD | 17,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1070` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 45,840.00 USD | 98,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1072` | 878,460.00 USD | 878,460.00 USD | 9,010.00 USD | 6,120.00 USD | 4,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1072` | 2,010,000.00 USD | 2,010,000.00 USD | 16,280.00 USD | 9,400.00 USD | 10,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1074` | 900,230.00 USD | 900,230.00 USD | 8,180.00 USD | 4,590.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1074` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 29,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1076` | 918,410.00 USD | 918,410.00 USD | 8,210.00 USD | 4,100.00 USD | 5,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1076` | 2,070,000.00 USD | 2,070,000.00 USD | 5,540.00 USD | 0.00 USD | 22,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1078` | 944,160.00 USD | 944,160.00 USD | 0.00 USD | 3,440.00 USD | 22,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1078` | 2,070,000.00 USD | 2,070,000.00 USD | 5,620.00 USD | 3,380.00 USD | 290.65 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1080` | 955,400.00 USD | 955,400.00 USD | 3,230.00 USD | 1,480.00 USD | 6,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1080` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1082` | 980,450.00 USD | 980,450.00 USD | 11,630.00 USD | 7,440.00 USD | 5,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1082` | 2,090,000.00 USD | 2,090,000.00 USD | 6,650.00 USD | 0.00 USD | 154.22 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1084` | 1,020,000.00 USD | 1,020,000.00 USD | 7,990.00 USD | 385.06 USD | 35,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1084` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1086` | 1,080,000.00 USD | 1,080,000.00 USD | 4,220.00 USD | 2,240.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1086` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 65.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1088` | 1,130,000.00 USD | 1,130,000.00 USD | 40,240.00 USD | 1,860.00 USD | 10,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1088` | 2,110,000.00 USD | 2,110,000.00 USD | 5,290.00 USD | 1,420.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1090` | 1,180,000.00 USD | 1,180,000.00 USD | 39,470.00 USD | 813.86 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1090` | 2,120,000.00 USD | 2,120,000.00 USD | 16,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1092` | 1,190,000.00 USD | 1,190,000.00 USD | 10,290.00 USD | 1,080.00 USD | 79.59 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1092` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 1,500.00 USD | 17,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1094` | 1,210,000.00 USD | 1,210,000.00 USD | 13,100.00 USD | 0.00 USD | 14,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1094` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 78.56 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1096` | 1,230,000.00 USD | 1,230,000.00 USD | 4,110.00 USD | 1,890.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1096` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 111.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1098` | 1,270,000.00 USD | 1,270,000.00 USD | 13,380.00 USD | 4,460.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1098` | 2,180,000.00 USD | 2,180,000.00 USD | 18,600.00 USD | 0.00 USD | 21,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1100` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 3,310.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1100` | 2,200,000.00 USD | 2,200,000.00 USD | 11,470.00 USD | 0.00 USD | 34.51 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1102` | 1,280,000.00 USD | 1,280,000.00 USD | 5,570.00 USD | 509.08 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1102` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1104` | 1,300,000.00 USD | 1,300,000.00 USD | 6,920.00 USD | 11,640.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1104` | 2,240,000.00 USD | 2,240,000.00 USD | 17,490.00 USD | 4,450.00 USD | 93.57 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1106` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 12,720.00 USD | 30,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1106` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 18,420.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1108` | 1,370,000.00 USD | 1,370,000.00 USD | 5,220.00 USD | 1,610.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1108` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 4,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1110` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 494.75 USD | 916.88 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1110` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 12,430.00 USD | 35.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1112` | 1,380,000.00 USD | 1,380,000.00 USD | 10,780.00 USD | 747.13 USD | 140.10 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1112` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 11,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1114` | 1,420,000.00 USD | 1,420,000.00 USD | 15,810.00 USD | 5,880.00 USD | 13,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1116` | 1,440,000.00 USD | 1,440,000.00 USD | 6,690.00 USD | 8,250.00 USD | 6,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1116` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 60.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1118` | 1,500,000.00 USD | 1,500,000.00 USD | 15,830.00 USD | 5,300.00 USD | 41,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1118` | 2,380,000.00 USD | 2,380,000.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1120` | 1,550,000.00 USD | 1,550,000.00 USD | 27,100.00 USD | 10,220.00 USD | 9,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1120` | 2,430,000.00 USD | 2,430,000.00 USD | 17,760.00 USD | 0.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1122` | 1,590,000.00 USD | 1,590,000.00 USD | 17,920.00 USD | 5,820.00 USD | 15,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1122` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 23,980.00 USD | 34,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1124` | 1,620,000.00 USD | 1,620,000.00 USD | 18,340.00 USD | 6,940.00 USD | 9,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1124` | 2,550,000.00 USD | 2,550,000.00 USD | 19,800.00 USD | 2,030.00 USD | 40,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1126` | 1,660,000.00 USD | 1,660,000.00 USD | 11,790.00 USD | 7,720.00 USD | 20,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1126` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 4,950.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1128` | 1,690,000.00 USD | 1,690,000.00 USD | 11,080.00 USD | 485.32 USD | 12,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1128` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 2,020.00 USD | 17,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1130` | 1,720,000.00 USD | 1,720,000.00 USD | 10,390.00 USD | 3,780.00 USD | 20,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1130` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1132` | 1,770,000.00 USD | 1,770,000.00 USD | 21,250.00 USD | 12,190.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1132` | 2,620,000.00 USD | 2,620,000.00 USD | 12,540.00 USD | 0.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1134` | 1,810,000.00 USD | 1,810,000.00 USD | 6,630.00 USD | 13,000.00 USD | 15,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1134` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 14,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1136` | 1,820,000.00 USD | 1,820,000.00 USD | 2,940.00 USD | 2,030.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1136` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 7,760.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1138` | 1,830,000.00 USD | 1,830,000.00 USD | 2,710.00 USD | 453.87 USD | 6,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1138` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1140` | 1,840,000.00 USD | 1,840,000.00 USD | 5,070.00 USD | 844.95 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1140` | 2,670,000.00 USD | 2,670,000.00 USD | 2,220.00 USD | 0.00 USD | 7,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1142` | 1,890,000.00 USD | 1,890,000.00 USD | 23,040.00 USD | 9,520.00 USD | 21,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1142` | 2,680,000.00 USD | 2,680,000.00 USD | 10,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1144` | 1,940,000.00 USD | 1,940,000.00 USD | 7,010.00 USD | 18,270.00 USD | 20,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1144` | 2,840,000.00 USD | 2,840,000.00 USD | 10,360.00 USD | 2,730.00 USD | 143,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1146` | 1,980,000.00 USD | 1,980,000.00 USD | 5,090.00 USD | 8,780.00 USD | 23,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1146` | 3,040,000.00 USD | 3,040,000.00 USD | 16,060.00 USD | 0.00 USD | 188,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1148` | 2,010,000.00 USD | 2,010,000.00 USD | 18,620.00 USD | 624.71 USD | 14,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1148` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 63,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1150` | 2,060,000.00 USD | 2,060,000.00 USD | 19,260.00 USD | 13,020.00 USD | 19,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1150` | 3,220,000.00 USD | 3,220,000.00 USD | 18,520.00 USD | 0.00 USD | 89,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1152` | 2,140,000.00 USD | 2,140,000.00 USD | 15,750.00 USD | 16,590.00 USD | 45,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1152` | 3,530,000.00 USD | 3,530,000.00 USD | 165,860.00 USD | 12,610.00 USD | 132,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1154` | 2,200,000.00 USD | 2,200,000.00 USD | 13,300.00 USD | 4,450.00 USD | 39,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1154` | 3,840,000.00 USD | 3,840,000.00 USD | 149,770.00 USD | 18,580.00 USD | 143,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1156` | 2,260,000.00 USD | 2,260,000.00 USD | 40,920.00 USD | 5,950.00 USD | 16,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1156` | 4,060,000.00 USD | 4,060,000.00 USD | 128,780.00 USD | 21,540.00 USD | 74,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1158` | 2,280,000.00 USD | 2,280,000.00 USD | 3,660.00 USD | 0.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1158` | 4,230,000.00 USD | 4,230,000.00 USD | 94,470.00 USD | 16,470.00 USD | 56,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1160` | 4,380,000.00 USD | 4,380,000.00 USD | 51,910.00 USD | 20,120.00 USD | 76,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1162` | 4,590,000.00 USD | 4,590,000.00 USD | 108,900.00 USD | 22,900.00 USD | 81,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1164` | 4,680,000.00 USD | 4,680,000.00 USD | 51,700.00 USD | 5,700.00 USD | 30,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1165` | 3,130.00 USD | 3,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1185` | 1,360.00 USD | 4,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1225` | 721.08 USD | 5,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1245` | 637.29 USD | 5,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1345` | 22,860.00 USD | 28,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1505` | 20,770.00 USD | 49,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1525` | 6,090.00 USD | 55,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1565` | 550.61 USD | 56,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1695` | 169.25 USD | 56,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1705` | 268.33 USD | 56,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1745` | 131.08 USD | 56,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1755` | 147.21 USD | 56,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1825` | 616.85 USD | 57,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1855` | 166.95 USD | 57,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1865` | 199.93 USD | 57,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2065` | 998.16 USD | 58,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

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
| `Buy Stop` | `0.1635` | 233,500.00 USD | 498.14 USD | 0.00 USD | `+56.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 235,530.00 USD | 2,030.00 USD | 0.00 USD | `+61.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 235,750.00 USD | 216.55 USD | 0.00 USD | `+66.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 235,860.00 USD | 117.26 USD | 0.00 USD | `+88.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 256,400.00 USD | 20,530.00 USD | 0.00 USD | `+91.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 256,590.00 USD | 189.30 USD | 0.00 USD | `+94.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 256,800.00 USD | 219.22 USD | 0.00 USD | `+95.23%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0862` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 0.00 USD | 1,880.00 USD | 6,880.00 USD |
| `7D` | `0.0864` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 1,980.00 USD | 15,640.00 USD |
| `7D` | `0.0866` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 2,080.00 USD |
| `7D` | `0.0868` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 2,880.00 USD |
| `7D` | `0.0870` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 2,870.00 USD |
| `7D` | `0.0872` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 0.00 USD | 1,200.00 USD | 2,980.00 USD |
| `7D` | `0.0874` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 6,010.00 USD | 0.00 USD | 4,500.00 USD |
| `7D` | `0.0876` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 0.00 USD | 1,770.00 USD | 4,890.00 USD |
| `7D` | `0.0878` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 9,200.00 USD | 5,890.00 USD | 25,110.00 USD |
| `7D` | `0.0880` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 3,770.00 USD | 2,200.00 USD | 11,840.00 USD |
| `7D` | `0.0882` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 12,660.00 USD | 7,260.00 USD | 9,180.00 USD |
| `7D` | `0.0884` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 0.00 USD | 1,220.00 USD | 13,650.00 USD |
| `7D` | `0.0886` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 9,350.00 USD | 2,470.00 USD | 11,320.00 USD |
| `7D` | `0.0888` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 3,370.00 USD | 2,720.00 USD | 8,290.00 USD |
| `7D` | `0.0890` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 13,510.00 USD | 3,610.00 USD | 13,150.00 USD |
| `7D` | `0.0892` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 3,620.00 USD | 3,060.00 USD | 2,090.00 USD |
| `7D` | `0.0894` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 5,480.00 USD | 3,400.00 USD | 7,750.00 USD |
| `7D` | `0.0896` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 4,300.00 USD | 0.00 USD | 4,200.00 USD |
| `7D` | `0.0898` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 3,390.00 USD | 927.82 USD | 4,460.00 USD |
| `7D` | `0.0900` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 1,250.00 USD | 428.11 USD | 77.78 USD |
| `7D` | `0.0902` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 1,030.00 USD | 482.67 USD | 1,300.00 USD |
| `7D` | `0.0904` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 5,730.00 USD | 996.61 USD | 1,700.00 USD |
| `7D` | `0.0906` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 6,040.00 USD | 1,900.00 USD | 4,140.00 USD |
| `7D` | `0.0908` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 2,540.00 USD | 2,570.00 USD | 1,290.00 USD |
| `7D` | `0.0910` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 0.00 USD | 606.54 USD | 48.03 USD |
| `7D` | `0.0912` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 2,650.00 USD |
| `7D` | `0.0914` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 1,670.00 USD | 903.90 USD | 56.36 USD |
| `1D` | `0.0916` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 6,590.00 USD | 2,510.00 USD | 257.88 USD |
| `7D` | `0.0916` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 6,310.00 USD |
| `1D` | `0.0918` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 6,400.00 USD | 4,060.00 USD | 2,530.00 USD |
| `7D` | `0.0918` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 1,740.00 USD |
| `1D` | `0.0920` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 6,400.00 USD | 1,320.00 USD | 20,360.00 USD |
| `7D` | `0.0920` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 7,440.00 USD | 2,030.00 USD | 223.39 USD |
| `1D` | `0.0922` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 2,430.00 USD | 4,100.00 USD | 14,030.00 USD |
| `7D` | `0.0922` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 0.00 USD | 7,660.00 USD | 34,750.00 USD |
| `1D` | `0.0924` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 4,790.00 USD | 4,700.00 USD | 43,420.00 USD |
| `7D` | `0.0924` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 1,790.00 USD | 2,020.00 USD | 11,850.00 USD |
| `1D` | `0.0926` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 5,130.00 USD | 4,460.00 USD | 555.49 USD |
| `7D` | `0.0926` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 8,180.00 USD |
| `1D` | `0.0928` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 2,600.00 USD | 1,100.00 USD | 1,530.00 USD |
| `7D` | `0.0928` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD |
| `1D` | `0.0930` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 7,300.00 USD | 2,440.00 USD | 8,690.00 USD |
| `7D` | `0.0930` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 0.00 USD | 5,320.00 USD | 0.00 USD |
| `1D` | `0.0932` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 2,710.00 USD | 1,300.00 USD | 5,080.00 USD |
| `7D` | `0.0932` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 2,220.00 USD | 0.00 USD | 12,330.00 USD |
| `1D` | `0.0934` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 22,030.00 USD | 3,830.00 USD | 17,910.00 USD |
| `1D` | `0.0936` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 7,080.00 USD | 9,360.00 USD | 16,330.00 USD |
| `7D` | `0.0936` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 19,560.00 USD | 6,840.00 USD | 25,450.00 USD |
| `1D` | `0.0938` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 8,170.00 USD | 2,920.00 USD | 46,580.00 USD |
| `7D` | `0.0938` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 248.29 USD |
| `1D` | `0.0940` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD |
| `7D` | `0.0940` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 14,050.00 USD | 0.00 USD | 10,640.00 USD |
| `1D` | `0.0942` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 3,500.00 USD | 16,110.00 USD | 49,230.00 USD |
| `7D` | `0.0942` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 6,170.00 USD | 18,340.00 USD | 114,170.00 USD |
| `1D` | `0.0944` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 11,620.00 USD | 4,860.00 USD | 36,500.00 USD |
| `7D` | `0.0944` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 0.00 USD | 2,010.00 USD | 0.00 USD |
| `1D` | `0.0946` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 4,130.00 USD | 5,280.00 USD | 10,220.00 USD |
| `7D` | `0.0946` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 0.00 USD | 1,810.00 USD | 154.22 USD |
| `1D` | `0.0948` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 0.00 USD | 1,100.00 USD | 101.09 USD |
| `7D` | `0.0948` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 3,770.00 USD | 0.00 USD | 26,920.00 USD |
| `1D` | `0.0950` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 12,180.00 USD | 6,710.00 USD | 22,900.00 USD |
| `7D` | `0.0950` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 0.00 USD | 9,700.00 USD | 134.31 USD |
| `1D` | `0.0952` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 0.00 USD | 853.02 USD | 6,660.00 USD |
| `7D` | `0.0952` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 0.00 USD | 4,410.00 USD | 0.00 USD |
| `1D` | `0.0954` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 41,470.00 USD | 11,160.00 USD | 21,160.00 USD |
| `7D` | `0.0954` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 0.00 USD | 3,740.00 USD | 187.14 USD |
| `1D` | `0.0956` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 18,680.00 USD | 9,390.00 USD | 37,070.00 USD |
| `7D` | `0.0956` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 39,120.00 USD | 13,670.00 USD | 50,980.00 USD |
| `1D` | `0.0958` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 7,180.00 USD | 4,290.00 USD | 22,320.00 USD |
| `7D` | `0.0958` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 21,370.00 USD |
| `1D` | `0.0960` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 0.00 USD | 16,940.00 USD | 146.83 USD |
| `7D` | `0.0960` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 28,110.00 USD | 16,920.00 USD | 20,150.00 USD |
| `1D` | `0.0962` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 8,920.00 USD | 15,440.00 USD | 27,750.00 USD |
| `7D` | `0.0962` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 12,340.00 USD | 0.00 USD | 75,010.00 USD |
| `1D` | `0.0964` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 31,490.00 USD | 10,380.00 USD | 27,840.00 USD |
| `7D` | `0.0964` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 0.00 USD | 4,020.00 USD | 86.68 USD |
| `1D` | `0.0966` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 0.00 USD | 3,880.00 USD | 815.14 USD |
| `7D` | `0.0966` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 0.00 USD | 2,390.00 USD | 2,830.00 USD |
| `1D` | `0.0968` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 0.00 USD | 2,960.00 USD | 2,380.00 USD |
| `7D` | `0.0968` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 7,490.00 USD | 0.00 USD | 56,240.00 USD |
| `1D` | `0.0970` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 8,360.00 USD | 8,640.00 USD | 16,030.00 USD |
| `7D` | `0.0970` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 0.00 USD | 7,090.00 USD | 5,010.00 USD |
| `1D` | `0.0972` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 2,860.00 USD | 3,220.00 USD | 1,980.00 USD |
| `7D` | `0.0972` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 0.00 USD | 8,830.00 USD | 0.00 USD |
| `1D` | `0.0974` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 0.00 USD | 7,010.00 USD | 0.00 USD |
| `7D` | `0.0974` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 0.00 USD | 7,480.00 USD | 104.80 USD |
| `1D` | `0.0976` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 0.00 USD | 765.93 USD | 1,060.00 USD |
| `7D` | `0.0976` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 179.57 USD |
| `1D` | `0.0978` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 0.00 USD | 817.22 USD | 67.90 USD |
| `1D` | `0.0980` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 12,700.00 USD | 4,570.00 USD | 21,130.00 USD |
| `7D` | `0.0980` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 22,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0982` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 10,790.00 USD | 7,650.00 USD | 0.00 USD |
| `7D` | `0.0982` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 0.00 USD | 5,070.00 USD | 11,350.00 USD |
| `1D` | `0.0984` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 10,310.00 USD | 19,740.00 USD | 15,450.00 USD |
| `7D` | `0.0984` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 0.00 USD | 16,160.00 USD | 90.68 USD |
| `1D` | `0.0986` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 7,260.00 USD | 8,960.00 USD | 11,390.00 USD |
| `7D` | `0.0986` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 5,330.00 USD | 16,520.00 USD | 6,690.00 USD |
| `1D` | `0.0988` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 30,450.00 USD | 7,150.00 USD | 33,720.00 USD |
| `7D` | `0.0988` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 10,360.00 USD | 7,820.00 USD | 0.00 USD |
| `1D` | `0.0990` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 12,880.00 USD | 4,730.00 USD | 4,590.00 USD |
| `7D` | `0.0990` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 30,090.00 USD | 6,660.00 USD | 0.00 USD |
| `1D` | `0.0992` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 84,750.00 USD | 7,620.00 USD | 30,750.00 USD |
| `7D` | `0.0992` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 12,790.00 USD | 11,440.00 USD | 0.00 USD |
| `1D` | `0.0994` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 32,970.00 USD | 3,250.00 USD | 20,460.00 USD |
| `7D` | `0.0994` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 55,790.00 USD | 0.00 USD | 65,130.00 USD |
| `1D` | `0.0996` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 15,040.00 USD | 2,450.00 USD | 74,900.00 USD |
| `7D` | `0.0996` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 27,010.00 USD | 5,500.00 USD | 32,940.00 USD |
| `1D` | `0.0998` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 12,990.00 USD | 5,820.00 USD | 57,790.00 USD |
| `7D` | `0.0998` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 21,180.00 USD | 11,540.00 USD | 113,290.00 USD |
| `1D` | `0.1000` | 939,040.00 USD | 0.00 USD | 939,040.00 USD | 10,360.00 USD | 16,010.00 USD | 35,460.00 USD |
| `7D` | `0.1000` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 54,220.00 USD | 25,020.00 USD | 33,080.00 USD |
| `1D` | `0.1002` | 877,210.00 USD | 0.00 USD | 877,210.00 USD | 17,830.00 USD | 4,080.00 USD | 42,920.00 USD |
| `7D` | `0.1002` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 70,060.00 USD | 10,690.00 USD | 74,890.00 USD |
| `1D` | `0.1004` | 812,380.00 USD | 0.00 USD | 812,380.00 USD | 53,750.00 USD | 30,530.00 USD | 49,300.00 USD |
| `7D` | `0.1004` | 965,740.00 USD | 0.00 USD | 965,740.00 USD | 19,310.00 USD | 17,550.00 USD | 46,130.00 USD |
| `1D` | `0.1006` | 678,810.00 USD | 0.00 USD | 678,810.00 USD | 24,030.00 USD | 23,800.00 USD | 29,820.00 USD |
| `7D` | `0.1006` | 882,750.00 USD | 0.00 USD | 882,750.00 USD | 23,200.00 USD | 23,170.00 USD | 67,130.00 USD |
| `1D` | `0.1008` | 601,160.00 USD | 0.00 USD | 601,160.00 USD | 17,840.00 USD | 11,220.00 USD | 3,770.00 USD |
| `7D` | `0.1008` | 769,250.00 USD | 0.00 USD | 769,250.00 USD | 13,040.00 USD | 5,470.00 USD | 96,530.00 USD |
| `1D` | `0.1010` | 568,340.00 USD | 0.00 USD | 568,340.00 USD | 23,240.00 USD | 13,530.00 USD | 23,750.00 USD |
| `7D` | `0.1010` | 654,220.00 USD | 0.00 USD | 654,220.00 USD | 29,550.00 USD | 24,610.00 USD | 3,990.00 USD |
| `1D` | `0.1012` | 507,830.00 USD | 0.00 USD | 507,830.00 USD | 16,360.00 USD | 9,190.00 USD | 19,550.00 USD |
| `7D` | `0.1012` | 596,070.00 USD | 0.00 USD | 596,070.00 USD | 6,490.00 USD | 35,670.00 USD | 0.00 USD |
| `1D` | `0.1014` | 462,740.00 USD | 0.00 USD | 462,740.00 USD | 13,540.00 USD | 6,940.00 USD | 16,970.00 USD |
| `7D` | `0.1014` | 553,910.00 USD | 0.00 USD | 553,910.00 USD | 40,860.00 USD | 15,590.00 USD | 25,450.00 USD |
| `1D` | `0.1016` | 425,270.00 USD | 0.00 USD | 425,270.00 USD | 8,170.00 USD | 775.38 USD | 23,150.00 USD |
| `7D` | `0.1016` | 472,010.00 USD | 0.00 USD | 472,010.00 USD | 14,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1018` | 393,170.00 USD | 0.00 USD | 393,170.00 USD | 18,090.00 USD | 1,550.00 USD | 3,430.00 USD |
| `7D` | `0.1018` | 458,010.00 USD | 0.00 USD | 458,010.00 USD | 39,450.00 USD | 0.00 USD | 10,630.00 USD |
| `1D` | `0.1020` | 370,110.00 USD | 0.00 USD | 370,110.00 USD | 0.00 USD | 0.00 USD | 11,590.00 USD |
| `7D` | `0.1020` | 407,930.00 USD | 0.00 USD | 407,930.00 USD | 0.00 USD | 8,460.00 USD | 47,420.00 USD |
| `1D` | `0.1022` | 358,530.00 USD | 0.00 USD | 358,530.00 USD | 0.00 USD | 0.00 USD | 6,020.00 USD |
| `1D` | `0.1026` | 352,500.00 USD | 0.00 USD | 352,500.00 USD | 0.00 USD | 1,650.00 USD | 1,610.00 USD |
| `7D` | `0.1032` | 352,040.00 USD | 0.00 USD | 352,040.00 USD | 13,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1036` | 349,250.00 USD | 0.00 USD | 349,250.00 USD | 2,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1036` | 338,860.00 USD | 0.00 USD | 338,860.00 USD | 0.00 USD | 0.00 USD | 108.00 USD |
| `1D` | `0.1038` | 347,090.00 USD | 0.00 USD | 347,090.00 USD | 0.00 USD | 14,190.00 USD | 24.05 USD |
| `7D` | `0.1038` | 338,750.00 USD | 0.00 USD | 338,750.00 USD | 0.00 USD | 10,870.00 USD | 31,350.00 USD |
| `1D` | `0.1040` | 332,880.00 USD | 0.00 USD | 332,880.00 USD | 0.00 USD | 19,120.00 USD | 15,140.00 USD |
| `7D` | `0.1040` | 296,530.00 USD | 0.00 USD | 296,530.00 USD | 0.00 USD | 5,130.00 USD | 0.00 USD |
| `1D` | `0.1042` | 298,610.00 USD | 0.00 USD | 298,610.00 USD | 22,890.00 USD | 9,410.00 USD | 25,770.00 USD |
| `7D` | `0.1042` | 291,390.00 USD | 0.00 USD | 291,390.00 USD | 49,380.00 USD | 12,190.00 USD | 0.00 USD |
| `1D` | `0.1044` | 240,540.00 USD | 0.00 USD | 240,540.00 USD | 24,130.00 USD | 36,390.00 USD | 23,540.00 USD |
| `7D` | `0.1044` | 229,820.00 USD | 0.00 USD | 229,820.00 USD | 11,140.00 USD | 25,310.00 USD | 22,700.00 USD |
| `1D` | `0.1046` | 156,490.00 USD | 0.00 USD | 156,490.00 USD | 16,570.00 USD | 0.00 USD | 31.28 USD |
| `7D` | `0.1046` | 170,670.00 USD | 0.00 USD | 170,670.00 USD | 0.00 USD | 23,140.00 USD | 60,160.00 USD |
| `1D` | `0.1048` | 139,890.00 USD | 0.00 USD | 139,890.00 USD | 36,040.00 USD | 17,510.00 USD | 86,340.00 USD |
| `7D` | `0.1048` | 87,380.00 USD | 0.00 USD | 87,380.00 USD | 30,640.00 USD | 14,940.00 USD | 41,800.00 USD |
| `1D` | `0.1049` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1049` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1050` | 58,710.00 USD | 58,710.00 USD | 0.00 USD | 32,940.00 USD | 21,980.00 USD | 3,780.00 USD |
| `7D` | `0.1050` | 90,920.00 USD | 90,920.00 USD | 0.00 USD | 27,290.00 USD | 0.00 USD | 63,630.00 USD |
| `1D` | `0.1052` | 143,940.00 USD | 143,940.00 USD | 0.00 USD | 39,930.00 USD | 15,010.00 USD | 30,300.00 USD |
| `7D` | `0.1052` | 262,040.00 USD | 262,040.00 USD | 0.00 USD | 32,640.00 USD | 34,840.00 USD | 103,650.00 USD |
| `1D` | `0.1054` | 265,840.00 USD | 265,840.00 USD | 0.00 USD | 45,620.00 USD | 18,770.00 USD | 57,510.00 USD |
| `7D` | `0.1054` | 493,860.00 USD | 493,860.00 USD | 0.00 USD | 85,290.00 USD | 53,700.00 USD | 92,830.00 USD |
| `1D` | `0.1056` | 343,490.00 USD | 343,490.00 USD | 0.00 USD | 25,800.00 USD | 23,260.00 USD | 28,580.00 USD |
| `7D` | `0.1056` | 803,320.00 USD | 803,320.00 USD | 0.00 USD | 87,170.00 USD | 47,540.00 USD | 174,740.00 USD |
| `1D` | `0.1058` | 442,790.00 USD | 442,790.00 USD | 0.00 USD | 25,860.00 USD | 6,490.00 USD | 66,950.00 USD |
| `7D` | `0.1058` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 54,790.00 USD | 24,600.00 USD | 136,660.00 USD |
| `1D` | `0.1060` | 516,960.00 USD | 516,960.00 USD | 0.00 USD | 44,720.00 USD | 2,700.00 USD | 26,750.00 USD |
| `7D` | `0.1060` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 55,680.00 USD | 51,150.00 USD | 79,920.00 USD |
| `1D` | `0.1062` | 617,110.00 USD | 617,110.00 USD | 0.00 USD | 44,570.00 USD | 4,130.00 USD | 51,450.00 USD |
| `7D` | `0.1062` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 46,950.00 USD | 28,310.00 USD | 82,360.00 USD |
| `1D` | `0.1064` | 660,590.00 USD | 660,590.00 USD | 0.00 USD | 6,960.00 USD | 7,730.00 USD | 28,790.00 USD |
| `7D` | `0.1064` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 42,470.00 USD | 144,960.00 USD |
| `1D` | `0.1066` | 734,360.00 USD | 734,360.00 USD | 0.00 USD | 15,590.00 USD | 15,700.00 USD | 42,490.00 USD |
| `7D` | `0.1066` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 42,670.00 USD | 107,620.00 USD |
| `1D` | `0.1068` | 806,920.00 USD | 806,920.00 USD | 0.00 USD | 11,970.00 USD | 9,310.00 USD | 51,280.00 USD |
| `7D` | `0.1068` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 5,330.00 USD | 41,360.00 USD | 79,350.00 USD |
| `1D` | `0.1070` | 858,600.00 USD | 858,600.00 USD | 0.00 USD | 23,200.00 USD | 11,060.00 USD | 17,420.00 USD |
| `7D` | `0.1070` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 45,840.00 USD | 98,490.00 USD |
| `1D` | `0.1072` | 878,460.00 USD | 878,460.00 USD | 0.00 USD | 9,010.00 USD | 6,120.00 USD | 4,730.00 USD |
| `7D` | `0.1072` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 16,280.00 USD | 9,400.00 USD | 10,320.00 USD |
| `1D` | `0.1074` | 900,230.00 USD | 900,230.00 USD | 0.00 USD | 8,180.00 USD | 4,590.00 USD | 9,000.00 USD |
| `7D` | `0.1074` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 29,150.00 USD | 0.00 USD |
| `1D` | `0.1076` | 918,410.00 USD | 918,410.00 USD | 0.00 USD | 8,210.00 USD | 4,100.00 USD | 5,870.00 USD |
| `7D` | `0.1076` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD | 22,600.00 USD |
| `1D` | `0.1078` | 944,160.00 USD | 944,160.00 USD | 0.00 USD | 0.00 USD | 3,440.00 USD | 22,300.00 USD |
| `7D` | `0.1078` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 5,620.00 USD | 3,380.00 USD | 290.65 USD |
| `1D` | `0.1080` | 955,400.00 USD | 955,400.00 USD | 0.00 USD | 3,230.00 USD | 1,480.00 USD | 6,540.00 USD |
| `7D` | `0.1080` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,860.00 USD |
| `1D` | `0.1082` | 980,450.00 USD | 980,450.00 USD | 0.00 USD | 11,630.00 USD | 7,440.00 USD | 5,980.00 USD |
| `7D` | `0.1082` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 6,650.00 USD | 0.00 USD | 154.22 USD |
| `1D` | `0.1084` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 7,990.00 USD | 385.06 USD | 35,900.00 USD |
| `7D` | `0.1084` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1086` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 4,220.00 USD | 2,240.00 USD | 50,470.00 USD |
| `7D` | `0.1086` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65.29 USD |
| `1D` | `0.1088` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 40,240.00 USD | 1,860.00 USD | 10,080.00 USD |
| `7D` | `0.1088` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 5,290.00 USD | 1,420.00 USD | 9,680.00 USD |
| `1D` | `0.1090` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 39,470.00 USD | 813.86 USD | 2,170.00 USD |
| `7D` | `0.1090` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1092` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 10,290.00 USD | 1,080.00 USD | 79.59 USD |
| `7D` | `0.1092` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 1,500.00 USD | 17,740.00 USD |
| `1D` | `0.1094` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 13,100.00 USD | 0.00 USD | 14,050.00 USD |
| `7D` | `0.1094` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78.56 USD |
| `1D` | `0.1096` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 7,780.00 USD |
| `7D` | `0.1096` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 111.29 USD |
| `1D` | `0.1098` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 13,380.00 USD | 4,460.00 USD | 22,850.00 USD |
| `7D` | `0.1098` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 21,880.00 USD |
| `1D` | `0.1100` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 3,310.00 USD | 4,310.00 USD |
| `7D` | `0.1100` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 34.51 USD |
| `1D` | `0.1102` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 5,570.00 USD | 509.08 USD | 0.00 USD |
| `7D` | `0.1102` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1104` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 6,920.00 USD | 11,640.00 USD | 1,170.00 USD |
| `7D` | `0.1104` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 17,490.00 USD | 4,450.00 USD | 93.57 USD |
| `1D` | `0.1106` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 12,720.00 USD | 30,870.00 USD |
| `7D` | `0.1106` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 18,420.00 USD | 16,110.00 USD |
| `1D` | `0.1108` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 5,220.00 USD | 1,610.00 USD | 17,380.00 USD |
| `7D` | `0.1108` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 4,120.00 USD | 0.00 USD |
| `1D` | `0.1110` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 494.75 USD | 916.88 USD |
| `7D` | `0.1110` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 12,430.00 USD | 35.29 USD |
| `1D` | `0.1112` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 10,780.00 USD | 747.13 USD | 140.10 USD |
| `7D` | `0.1112` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 0.00 USD |
| `1D` | `0.1114` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 15,810.00 USD | 5,880.00 USD | 13,520.00 USD |
| `1D` | `0.1116` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 6,690.00 USD | 8,250.00 USD | 6,940.00 USD |
| `7D` | `0.1116` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 60.00 USD |
| `1D` | `0.1118` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 15,830.00 USD | 5,300.00 USD | 41,210.00 USD |
| `7D` | `0.1118` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD |
| `1D` | `0.1120` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 27,100.00 USD | 10,220.00 USD | 9,850.00 USD |
| `7D` | `0.1120` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 17,760.00 USD | 0.00 USD | 29,770.00 USD |
| `1D` | `0.1122` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 17,920.00 USD | 5,820.00 USD | 15,000.00 USD |
| `7D` | `0.1122` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 23,980.00 USD | 34,740.00 USD |
| `1D` | `0.1124` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 18,340.00 USD | 6,940.00 USD | 9,800.00 USD |
| `7D` | `0.1124` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 19,800.00 USD | 2,030.00 USD | 40,520.00 USD |
| `1D` | `0.1126` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 11,790.00 USD | 7,720.00 USD | 20,400.00 USD |
| `7D` | `0.1126` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 4,950.00 USD | 7,340.00 USD |
| `1D` | `0.1128` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 11,080.00 USD | 485.32 USD | 12,900.00 USD |
| `7D` | `0.1128` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD | 17,130.00 USD |
| `1D` | `0.1130` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 10,390.00 USD | 3,780.00 USD | 20,030.00 USD |
| `7D` | `0.1130` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,870.00 USD |
| `1D` | `0.1132` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 21,250.00 USD | 12,190.00 USD | 16,650.00 USD |
| `7D` | `0.1132` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 12,540.00 USD | 0.00 USD | 8,170.00 USD |
| `1D` | `0.1134` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 6,630.00 USD | 13,000.00 USD | 15,360.00 USD |
| `7D` | `0.1134` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 14,090.00 USD | 0.00 USD |
| `1D` | `0.1136` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 2,940.00 USD | 2,030.00 USD | 5,340.00 USD |
| `7D` | `0.1136` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 7,760.00 USD | 9,010.00 USD |
| `1D` | `0.1138` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 2,710.00 USD | 453.87 USD | 6,160.00 USD |
| `7D` | `0.1138` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD |
| `1D` | `0.1140` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 5,070.00 USD | 844.95 USD | 7,040.00 USD |
| `7D` | `0.1140` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 2,220.00 USD | 0.00 USD | 7,640.00 USD |
| `1D` | `0.1142` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 23,040.00 USD | 9,520.00 USD | 21,440.00 USD |
| `7D` | `0.1142` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1144` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 7,010.00 USD | 18,270.00 USD | 20,320.00 USD |
| `7D` | `0.1144` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 10,360.00 USD | 2,730.00 USD | 143,410.00 USD |
| `1D` | `0.1146` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 5,090.00 USD | 8,780.00 USD | 23,060.00 USD |
| `7D` | `0.1146` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 16,060.00 USD | 0.00 USD | 188,440.00 USD |
| `1D` | `0.1148` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 18,620.00 USD | 624.71 USD | 14,350.00 USD |
| `7D` | `0.1148` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 63,900.00 USD |
| `1D` | `0.1150` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 19,260.00 USD | 13,020.00 USD | 19,710.00 USD |
| `7D` | `0.1150` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 18,520.00 USD | 0.00 USD | 89,710.00 USD |
| `1D` | `0.1152` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 15,750.00 USD | 16,590.00 USD | 45,400.00 USD |
| `7D` | `0.1152` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 165,860.00 USD | 12,610.00 USD | 132,470.00 USD |
| `1D` | `0.1154` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 13,300.00 USD | 4,450.00 USD | 39,970.00 USD |
| `7D` | `0.1154` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 149,770.00 USD | 18,580.00 USD | 143,460.00 USD |
| `1D` | `0.1156` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 40,920.00 USD | 5,950.00 USD | 16,740.00 USD |
| `7D` | `0.1156` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 128,780.00 USD | 21,540.00 USD | 74,860.00 USD |
| `1D` | `0.1158` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 3,660.00 USD | 0.00 USD | 11,030.00 USD |
| `7D` | `0.1158` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 94,470.00 USD | 16,470.00 USD | 56,240.00 USD |
| `7D` | `0.1160` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 51,910.00 USD | 20,120.00 USD | 76,420.00 USD |
| `7D` | `0.1162` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 108,900.00 USD | 22,900.00 USD | 81,410.00 USD |
| `7D` | `0.1164` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 51,700.00 USD | 5,700.00 USD | 30,640.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `65.67M` | Total OI Tokens: `628,005,232.7 OP`
  * 1h OI Change: `+1.99%` | 4h OI Change: `+2.01%` | 24h OI Change: `-11.25%`
  * Exchange Breakdown: Binance=`14.25M` | Bybit=`13.01M` | OKX=`4.14M` | Hyperliquid=`3.23M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-2.48K` | Last 24h: `-4.25K` | Last 3d: `-11.30K` | Last 7d: `-13.94K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0153%` | **USDT OKX** | `-0.0287%` |
| **USDT Bybit** | `0.0063%` | **USDT KuCoin** | `-0.0036%` |
| **USDT MEXC** | `-0.0153%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `58.06%` | `41.94%` | `1.38` | 878,090.00 USD |
| `15M` | `Binance` | `52.61%` | `47.39%` | `1.11` | 249,920.00 USD |
| `15M` | `OKX` | `57.48%` | `42.52%` | `1.35` | 92,760.00 USD |
| `15M` | `Bybit` | `44.5%` | `55.5%` | `0.80` | 126,440.00 USD |
| `15M` | `KuCoin` | `50.67%` | `49.33%` | `1.03` | 21,470.00 USD |
| `15M` | `Gate` | `67.2%` | `32.8%` | `2.05` | 19,050.00 USD |
| `15M` | `Bitget` | `28.02%` | `71.98%` | `0.39` | 11,070.00 USD |
| `15M` | `BingX` | `63.5%` | `36.5%` | `1.74` | 49,070.00 USD |
| `15M` | `MEXC` | `79.76%` | `20.24%` | `3.94` | 108,350.00 USD |
| `15M` | `Bitunix` | `91.65%` | `8.35%` | `10.98` | 34,200.00 USD |
| `15M` | `Hyperliquid` | `65.31%` | `34.69%` | `1.88` | 10,410.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `57.09%` | `42.91%` | `1.33` | 121,110.00 USD |
| `15M` | `Crypto.com` | `100%` | `0%` | `1.00` | 0.21 USD |
| `15M` | `WhiteBIT` | `59.93%` | `40.07%` | `1.50` | 28,270.00 USD |
| `15M` | `HTX` | `7.89%` | `92.11%` | `0.09` | 100.79 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `100%` | `0%` | `1.00` | 54.28 USD |
| `15M` | `Aster` | `30.23%` | `69.77%` | `0.43` | 148.29 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `1.4%` | `98.6%` | `0.01` | 5,690.00 USD |
| `15M` | `Whale Positions` | `52.61%` | `47.39%` | `1.11` | 249,920.00 USD |
| `15M` | `Global Accounts` | `58.06%` | `41.94%` | `1.38` | 878,090.00 USD |
| `1H` | `OP` | `53.64%` | `46.36%` | `1.16` | 3,540,000.00 USD |
| `1H` | `Binance` | `50.39%` | `49.61%` | `1.02` | 1,130,000.00 USD |
| `1H` | `OKX` | `64.04%` | `35.96%` | `1.78` | 478,760.00 USD |
| `1H` | `Bybit` | `51.33%` | `48.67%` | `1.05` | 351,990.00 USD |
| `1H` | `KuCoin` | `49.69%` | `50.31%` | `0.99` | 168,340.00 USD |
| `1H` | `Gate` | `32.02%` | `67.98%` | `0.47` | 59,310.00 USD |
| `1H` | `Bitget` | `34.49%` | `65.51%` | `0.53` | 69,390.00 USD |
| `1H` | `BingX` | `46.58%` | `53.42%` | `0.87` | 167,500.00 USD |
| `1H` | `MEXC` | `66.25%` | `33.75%` | `1.96` | 306,750.00 USD |
| `1H` | `Bitunix` | `68.13%` | `31.87%` | `2.14` | 43,960.00 USD |
| `1H` | `Hyperliquid` | `46.42%` | `53.58%` | `0.87` | 57,610.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54%` | `46%` | `1.17` | 575,260.00 USD |
| `1H` | `Crypto.com` | `32.43%` | `67.57%` | `0.48` | 2.59 USD |
| `1H` | `WhiteBIT` | `66.96%` | `33.04%` | `2.03` | 106,250.00 USD |
| `1H` | `HTX` | `18.02%` | `81.98%` | `0.22` | 115.15 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `73.53%` | `26.47%` | `2.78` | 99.37 USD |
| `1H` | `Aster` | `42.09%` | `57.91%` | `0.73` | 522.85 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `1.6%` | `98.4%` | `0.02` | 33,470.00 USD |
| `1H` | `Whale Positions` | `50.39%` | `49.61%` | `1.02` | 1,130,000.00 USD |
| `1H` | `Global Accounts` | `53.64%` | `46.36%` | `1.16` | 3,540,000.00 USD |
| `4H` | `OP` | `51.21%` | `48.79%` | `1.05` | 17,950,000.00 USD |
| `4H` | `Binance` | `50.89%` | `49.11%` | `1.04` | 5,710,000.00 USD |
| `4H` | `OKX` | `54.35%` | `45.65%` | `1.19` | 1,580,000.00 USD |
| `4H` | `Bybit` | `47.98%` | `52.02%` | `0.92` | 1,750,000.00 USD |
| `4H` | `KuCoin` | `49.9%` | `50.1%` | `1.00` | 2,070,000.00 USD |
| `4H` | `Gate` | `43.39%` | `56.61%` | `0.77` | 362,540.00 USD |
| `4H` | `Bitget` | `53.9%` | `46.1%` | `1.17` | 812,900.00 USD |
| `4H` | `BingX` | `47.03%` | `52.97%` | `0.89` | 2,450,000.00 USD |
| `4H` | `MEXC` | `51.27%` | `48.73%` | `1.05` | 809,010.00 USD |
| `4H` | `Bitunix` | `60.13%` | `39.87%` | `1.51` | 256,100.00 USD |
| `4H` | `Hyperliquid` | `39.61%` | `60.39%` | `0.66` | 447,670.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.53%` | `47.47%` | `1.11` | 835,020.00 USD |
| `4H` | `Crypto.com` | `3.62%` | `96.38%` | `0.04` | 0.00 USD |
| `4H` | `WhiteBIT` | `59.59%` | `40.41%` | `1.47` | 768,670.00 USD |
| `4H` | `HTX` | `40.23%` | `59.77%` | `0.67` | 3,380.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `43.2%` | `56.8%` | `0.76` | 10,050.00 USD |
| `4H` | `Aster` | `55.1%` | `44.9%` | `1.23` | 68,370.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `39.9%` | `60.1%` | `0.66` | 12,880.00 USD |
| `4H` | `Whale Positions` | `50.89%` | `49.11%` | `1.04` | 5,710,000.00 USD |
| `4H` | `Global Accounts` | `51.21%` | `48.79%` | `1.05` | 17,950,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1024` | `0.1025` | `0.1024` | `0.1030` | `0.1023` | 189,660.77 USD | 110,909.31 USD | 78,751.47 USD | 32,157.84 USD | `+16.96%` | `13B / 15S` |
| `0:00 UTC` | `0.1021` | `0.1022` | `0.1021` | `0.1027` | `0.1019` | 366,904.35 USD | 146,868.15 USD | 220,036.20 USD | -73,168.05 USD | `-19.94%` | `9B / 16S` |
| `5:00 UTC` | `0.1020` | `0.1021` | `0.1020` | `0.1024` | `0.1019` | 314,873.64 USD | 167,532.45 USD | 147,341.19 USD | 20,191.27 USD | `+6.41%` | `10B / 2S` |
| `0:00 UTC` | `0.1019` | `0.1024` | `0.1019` | `0.1029` | `0.1019` | 191,273.46 USD | 92,786.86 USD | 98,486.60 USD | -5,699.74 USD | `-2.98%` | `22B / 16S` |
| `5:00 UTC` | `0.1028` | `0.1029` | `0.1028` | `0.1034` | `0.1023` | 237,952.24 USD | 133,825.41 USD | 104,126.84 USD | 29,698.57 USD | `+12.48%` | `22B / 24S` |
| `0:00 UTC` | `0.1030` | `0.1032` | `0.1030` | `0.1036` | `0.1028` | 441,050.39 USD | 212,264.29 USD | 228,786.10 USD | -16,521.82 USD | `-3.75%` | `9B / 18S` |
| `5:00 UTC` | `0.1036` | `0.1033` | `0.1036` | `0.1037` | `0.1029` | 224,777.59 USD | 109,477.97 USD | 115,299.62 USD | -5,821.65 USD | `-2.59%` | `10B / 10S` |
| `0:00 UTC` | `0.1039` | `0.1038` | `0.1039` | `0.1041` | `0.1032` | 262,943.08 USD | 122,626.50 USD | 140,316.58 USD | -17,690.08 USD | `-6.73%` | `16B / 11S` |
| `5:00 UTC` | `0.1039` | `0.1043` | `0.1039` | `0.1049` | `0.1038` | 223,592.72 USD | 127,781.25 USD | 95,811.48 USD | 31,969.77 USD | `+14.30%` | `24B / 18S` |
| `0:00 UTC` | `0.1049` | `0.1048` | `0.1049` | `0.1050` | `0.1045` | 149,216.19 USD | 63,365.20 USD | 85,850.98 USD | -22,485.78 USD | `-15.07%` | `0B / 15S` |

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
  * `2026-10-30 16:35:32 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:32 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:32 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:38:32 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
