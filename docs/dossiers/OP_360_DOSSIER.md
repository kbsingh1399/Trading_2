# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 15:36:15 IST` (`2026-10-30 10:06:15 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1027` | `0.1029` | `0.1023` | `0.1029` | `853,443` | 87,486.86 USD | -12,786.95 USD | `-14.62%` | -1,959,835.98 USD | `-0.48` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.1029` | `0.1033` | `0.1027` | `0.1032` | `807,258` | 83,110.54 USD | 36,334.57 USD | `+43.72%` | -1,923,501.41 USD | `+1.51` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.1032` | `0.1034` | `0.1031` | `0.1033` | `605,027` | 62,481.83 USD | 1,976.52 USD | `+3.16%` | -1,921,524.90 USD | `+0.13` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1020` | `0.1024` | `0.1019` | `0.1022` | `3,083,099` | 314,873.64 USD | 20,191.27 USD | `+6.41%` | -1,941,349.29 USD | `-0.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1022` | `0.1029` | `0.1019` | `0.1027` | `1,868,664` | 191,273.46 USD | -5,699.74 USD | `-2.98%` | -1,947,049.04 USD | `-0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1027` | `0.1034` | `0.1023` | `0.1034` | `2,198,121` | 226,093.62 USD | 32,486.60 USD | `+14.37%` | -1,914,562.43 USD | `+0.38` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1030` | `0.1035` | `0.1022` | `0.1027` | `9,646,320` | 992,142.11 USD | 40,207.23 USD | `+4.05%` | -1,978,421.78 USD | `+0.29` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1027` | `0.1038` | `0.1023` | `0.1024` | `10,736,702` | 1,104,134.28 USD | 90,049.28 USD | `+8.16%` | -1,888,372.51 USD | `+0.40` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1024` | `0.1034` | `0.1019` | `0.1034` | `10,739,837` | 1,099,117.65 USD | -26,217.34 USD | `-2.39%` | -1,914,589.85 USD | `+0.17` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,490,108.93 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1040` | `0.0988` | `0.1027` | `54,609,324` | 5,566,939.91 USD | 608,714.61 USD | `+10.93%` | -1,881,394.33 USD | `+1.21` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1027` | `0.1038` | `0.1019` | `0.1034` | `21,476,804` | 2,203,279.35 USD | 63,859.35 USD | `+2.90%` | -1,817,534.98 USD | `+0.48` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | 165,115.32 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -1,152,082.54 USD | `-1.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,490,108.93 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1040` | `0.0988` | `0.1027` | `54,609,324` | 5,566,939.91 USD | 608,714.61 USD | `+10.93%` | -1,881,394.33 USD | `+1.21` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1027` | `0.1038` | `0.1019` | `0.1034` | `21,476,804` | 2,203,279.35 USD | 63,859.35 USD | `+2.90%` | -1,817,534.98 USD | `+0.48` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:30:10 IST` |

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
| `Live` | `Long Liquidation` | `0.0305` | 1,500.00 USD | 122,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0395` | 201.41 USD | 121,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0555` | 991.96 USD | 121,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 829.69 USD | 120,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 4,220.00 USD | 119,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `7D` | `Long Liquidation` | `0.0860` | 2,360,000.00 USD | 2,360,000.00 USD | 1,880.00 USD | 0.00 USD | 2,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0862` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 1,880.00 USD | 4,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0864` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 1,980.00 USD | 15,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0865` | 318.30 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0866` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0868` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0870` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0872` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 1,200.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0874` | 2,320,000.00 USD | 2,320,000.00 USD | 6,010.00 USD | 0.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0875` | 793.17 USD | 6,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0876` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 1,770.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0878` | 2,310,000.00 USD | 2,310,000.00 USD | 9,200.00 USD | 5,890.00 USD | 25,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0880` | 2,270,000.00 USD | 2,270,000.00 USD | 3,770.00 USD | 2,200.00 USD | 11,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0882` | 2,250,000.00 USD | 2,250,000.00 USD | 12,660.00 USD | 7,260.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0884` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 1,220.00 USD | 13,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0886` | 2,200,000.00 USD | 2,200,000.00 USD | 9,350.00 USD | 2,470.00 USD | 11,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0888` | 2,180,000.00 USD | 2,180,000.00 USD | 3,370.00 USD | 2,720.00 USD | 8,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0890` | 2,170,000.00 USD | 2,170,000.00 USD | 13,510.00 USD | 3,610.00 USD | 13,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0892` | 2,140,000.00 USD | 2,140,000.00 USD | 3,620.00 USD | 3,060.00 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0894` | 2,130,000.00 USD | 2,130,000.00 USD | 5,480.00 USD | 3,400.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,270.00 USD | 5,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0896` | 2,110,000.00 USD | 2,110,000.00 USD | 4,300.00 USD | 0.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0898` | 2,100,000.00 USD | 2,100,000.00 USD | 3,390.00 USD | 927.82 USD | 4,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0900` | 2,090,000.00 USD | 2,090,000.00 USD | 1,250.00 USD | 428.11 USD | 77.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0902` | 2,090,000.00 USD | 2,090,000.00 USD | 1,030.00 USD | 482.67 USD | 1,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0904` | 2,090,000.00 USD | 2,090,000.00 USD | 5,730.00 USD | 996.61 USD | 1,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0905` | 2,230.00 USD | 2,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0906` | 2,080,000.00 USD | 2,080,000.00 USD | 6,040.00 USD | 1,900.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0908` | 2,070,000.00 USD | 2,070,000.00 USD | 2,540.00 USD | 2,570.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0910` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 606.54 USD | 48.03 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0912` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 2,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0914` | 2,060,000.00 USD | 2,060,000.00 USD | 1,670.00 USD | 903.90 USD | 56.36 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0916` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 6,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0917` | 1,910,000.00 USD | 1,910,000.00 USD | 10,440.00 USD | 5,150.00 USD | 269.80 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0918` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0919` | 1,890,000.00 USD | 1,890,000.00 USD | 8,950.00 USD | 1,090.00 USD | 19,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0920` | 2,050,000.00 USD | 2,050,000.00 USD | 7,440.00 USD | 2,030.00 USD | 223.39 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0921` | 1,870,000.00 USD | 1,870,000.00 USD | 758.20 USD | 2,040.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0922` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 7,660.00 USD | 34,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0923` | 1,860,000.00 USD | 1,860,000.00 USD | 4,040.00 USD | 6,180.00 USD | 30,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0924` | 2,000,000.00 USD | 2,000,000.00 USD | 1,790.00 USD | 2,020.00 USD | 11,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0925` | 1,820,000.00 USD | 1,820,000.00 USD | 6,480.00 USD | 4,210.00 USD | 27,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0926` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0927` | 1,780,000.00 USD | 1,780,000.00 USD | 1,820.00 USD | 2,300.00 USD | 1,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0928` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0929` | 1,770,000.00 USD | 1,770,000.00 USD | 5,660.00 USD | 1,800.00 USD | 919.58 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0930` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0931` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 635.90 USD | 7,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0932` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 12,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0933` | 1,760,000.00 USD | 1,760,000.00 USD | 16,500.00 USD | 0.00 USD | 11,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0935` | 1,730,000.00 USD | 1,730,000.00 USD | 8,990.00 USD | 7,300.00 USD | 15,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0936` | 1,950,000.00 USD | 1,950,000.00 USD | 19,560.00 USD | 6,840.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0937` | 1,700,000.00 USD | 1,700,000.00 USD | 4,580.00 USD | 6,660.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0938` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 248.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0939` | 1,670,000.00 USD | 1,670,000.00 USD | 3,590.00 USD | 2,140.00 USD | 44,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0940` | 1,900,000.00 USD | 1,900,000.00 USD | 14,050.00 USD | 0.00 USD | 10,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0941` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 9,410.00 USD | 21,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0942` | 1,880,000.00 USD | 1,880,000.00 USD | 6,170.00 USD | 18,340.00 USD | 114,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0943` | 1,590,000.00 USD | 1,590,000.00 USD | 3,500.00 USD | 10,920.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0944` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 2,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0945` | 1,550,000.00 USD | 1,550,000.00 USD | 15,750.00 USD | 6,510.00 USD | 44,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0946` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 1,810.00 USD | 154.22 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0947` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 962.66 USD | 91.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0948` | 1,740,000.00 USD | 1,740,000.00 USD | 3,770.00 USD | 0.00 USD | 26,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0949` | 1,480,000.00 USD | 1,480,000.00 USD | 12,180.00 USD | 5,770.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0950` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 9,700.00 USD | 134.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0951` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 2,030.00 USD | 19,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0952` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 4,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0953` | 1,440,000.00 USD | 1,440,000.00 USD | 33,000.00 USD | 4,360.00 USD | 6,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0954` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 3,740.00 USD | 187.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0955` | 1,390,000.00 USD | 1,390,000.00 USD | 17,990.00 USD | 14,600.00 USD | 31,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0956` | 1,690,000.00 USD | 1,690,000.00 USD | 39,120.00 USD | 13,670.00 USD | 50,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0957` | 1,330,000.00 USD | 1,330,000.00 USD | 16,340.00 USD | 6,740.00 USD | 48,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0958` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0959` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 3,100.00 USD | 50.26 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0960` | 1,560,000.00 USD | 1,560,000.00 USD | 28,110.00 USD | 16,920.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0961` | 1,250,000.00 USD | 1,250,000.00 USD | 8,920.00 USD | 23,950.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0962` | 1,500,000.00 USD | 1,500,000.00 USD | 12,340.00 USD | 0.00 USD | 75,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0963` | 1,200,000.00 USD | 1,200,000.00 USD | 23,240.00 USD | 11,750.00 USD | 11,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0964` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 4,020.00 USD | 86.68 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0965` | 1,150,000.00 USD | 1,150,000.00 USD | 8,250.00 USD | 5,890.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0966` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 2,390.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0967` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 1,960.00 USD | 818.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0968` | 1,400,000.00 USD | 1,400,000.00 USD | 7,490.00 USD | 0.00 USD | 56,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0969` | 1,110,000.00 USD | 1,110,000.00 USD | 6,930.00 USD | 7,530.00 USD | 8,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0970` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 7,090.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0971` | 1,090,000.00 USD | 1,090,000.00 USD | 2,840.00 USD | 4,070.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0972` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 8,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0973` | 1,070,000.00 USD | 1,070,000.00 USD | 1,440.00 USD | 10,220.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0974` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 7,480.00 USD | 104.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0975` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 114.54 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0976` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 148.46 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0977` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 765.93 USD | 978.56 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0979` | 1,060,000.00 USD | 1,060,000.00 USD | 5,180.00 USD | 2,920.00 USD | 21,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0980` | 1,310,000.00 USD | 1,310,000.00 USD | 22,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0981` | 1,030,000.00 USD | 1,030,000.00 USD | 12,740.00 USD | 7,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0982` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 5,070.00 USD | 11,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0983` | 1,010,000.00 USD | 1,010,000.00 USD | 11,130.00 USD | 16,910.00 USD | 10,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0984` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 16,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0985` | 970,900.00 USD | 970,900.00 USD | 5,970.00 USD | 8,750.00 USD | 12,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0986` | 1,250,000.00 USD | 1,250,000.00 USD | 5,330.00 USD | 16,520.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0987` | 943,700.00 USD | 943,700.00 USD | 30,280.00 USD | 7,610.00 USD | 16,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0988` | 1,220,000.00 USD | 1,220,000.00 USD | 10,360.00 USD | 7,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0989` | 889,700.00 USD | 889,700.00 USD | 8,920.00 USD | 9,270.00 USD | 24,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0990` | 1,210,000.00 USD | 1,210,000.00 USD | 26,690.00 USD | 6,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0991` | 846,990.00 USD | 846,990.00 USD | 74,010.00 USD | 1,530.00 USD | 3,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0992` | 1,170,000.00 USD | 1,170,000.00 USD | 12,790.00 USD | 3,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0993` | 768,270.00 USD | 768,270.00 USD | 23,230.00 USD | 5,240.00 USD | 45,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0994` | 1,160,000.00 USD | 1,160,000.00 USD | 50,250.00 USD | 0.00 USD | 65,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0995` | 694,620.00 USD | 694,620.00 USD | 16,240.00 USD | 898.20 USD | 52,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0996` | 1,040,000.00 USD | 1,040,000.00 USD | 27,010.00 USD | 5,500.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0997` | 624,560.00 USD | 624,560.00 USD | 17,900.00 USD | 7,370.00 USD | 55,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0998` | 974,820.00 USD | 974,820.00 USD | 14,530.00 USD | 11,540.00 USD | 113,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0999` | 543,790.00 USD | 543,790.00 USD | 0.00 USD | 11,820.00 USD | 47,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1000` | 835,470.00 USD | 835,470.00 USD | 54,220.00 USD | 25,020.00 USD | 33,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1001` | 484,090.00 USD | 484,090.00 USD | 25,400.00 USD | 4,200.00 USD | 42,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1002` | 723,140.00 USD | 723,140.00 USD | 70,060.00 USD | 10,690.00 USD | 74,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1003` | 411,980.00 USD | 411,980.00 USD | 37,160.00 USD | 10,200.00 USD | 27,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1004` | 567,500.00 USD | 567,500.00 USD | 19,310.00 USD | 17,550.00 USD | 46,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1005` | 337,420.00 USD | 337,420.00 USD | 31,310.00 USD | 43,010.00 USD | 66,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1006` | 484,520.00 USD | 484,520.00 USD | 23,200.00 USD | 23,170.00 USD | 67,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1007` | 197,100.00 USD | 197,100.00 USD | 21,860.00 USD | 7,380.00 USD | 8,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1008` | 371,020.00 USD | 371,020.00 USD | 13,040.00 USD | 5,470.00 USD | 96,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1009` | 159,230.00 USD | 159,230.00 USD | 20,400.00 USD | 15,460.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1010` | 255,980.00 USD | 255,980.00 USD | 22,770.00 USD | 24,610.00 USD | 3,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1011` | 117,780.00 USD | 117,780.00 USD | 8,150.00 USD | 7,120.00 USD | 22,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1012` | 204,620.00 USD | 204,620.00 USD | 6,490.00 USD | 20,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1013` | 80,400.00 USD | 80,400.00 USD | 1,640.00 USD | 4,430.00 USD | 14,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1014` | 177,490.00 USD | 177,490.00 USD | 29,790.00 USD | 15,590.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1015` | 59,860.00 USD | 59,860.00 USD | 4,580.00 USD | 1,220.00 USD | 20,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1016` | 106,670.00 USD | 106,670.00 USD | 14,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1017` | 33,860.00 USD | 33,860.00 USD | 3,590.00 USD | 0.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1018` | 92,670.00 USD | 92,670.00 USD | 26,150.00 USD | 0.00 USD | 10,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1019` | 19,160.00 USD | 19,160.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1020` | 55,890.00 USD | 55,890.00 USD | 0.00 USD | 8,460.00 USD | 47,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1021` | 17,610.00 USD | 17,610.00 USD | 0.00 USD | 0.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1023` | 3,720.00 USD | 3,720.00 USD | 0.00 USD | 0.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1032` | 13,180.00 USD | 13,180.00 USD | 13,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1032` | 26,370.00 USD | 26,370.00 USD | 13,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1034` | 32,100.00 USD | 32,100.00 USD | 5,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1035` | 7,220.00 USD | 7,220.00 USD | 0.00 USD | 7,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1036` | 34,920.00 USD | 34,920.00 USD | 2,710.00 USD | 0.00 USD | 108.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1037` | 55,180.00 USD | 55,180.00 USD | 35,090.00 USD | 12,850.00 USD | 24.05 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1038` | 77,150.00 USD | 77,150.00 USD | 0.00 USD | 10,870.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1039` | 76,020.00 USD | 76,020.00 USD | 6,500.00 USD | 9,120.00 USD | 5,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1040` | 88,220.00 USD | 88,220.00 USD | 5,940.00 USD | 5,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1041` | 149,240.00 USD | 149,240.00 USD | 36,920.00 USD | 16,680.00 USD | 19,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1042` | 149,790.00 USD | 149,790.00 USD | 49,380.00 USD | 12,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1043` | 205,940.00 USD | 205,940.00 USD | 13,920.00 USD | 18,610.00 USD | 24,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1044` | 208,940.00 USD | 208,940.00 USD | 11,140.00 USD | 25,310.00 USD | 22,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1045` | 261,440.00 USD | 261,440.00 USD | 12,990.00 USD | 21,860.00 USD | 20,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1046` | 292,240.00 USD | 292,240.00 USD | 0.00 USD | 23,140.00 USD | 60,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1047` | 375,130.00 USD | 375,130.00 USD | 40,510.00 USD | 22,900.00 USD | 50,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1048` | 379,610.00 USD | 379,610.00 USD | 30,640.00 USD | 14,940.00 USD | 41,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1049` | 498,280.00 USD | 498,280.00 USD | 35,540.00 USD | 20,770.00 USD | 66,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1050` | 470,530.00 USD | 470,530.00 USD | 27,290.00 USD | 0.00 USD | 63,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1051` | 571,050.00 USD | 571,050.00 USD | 33,470.00 USD | 23,280.00 USD | 16,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1052` | 634,870.00 USD | 634,870.00 USD | 25,850.00 USD | 34,840.00 USD | 103,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1053` | 647,320.00 USD | 647,320.00 USD | 21,820.00 USD | 10,090.00 USD | 44,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1054` | 851,660.00 USD | 851,660.00 USD | 85,290.00 USD | 38,660.00 USD | 92,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1055` | 735,730.00 USD | 735,730.00 USD | 31,320.00 USD | 17,760.00 USD | 39,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1056` | 1,150,000.00 USD | 1,150,000.00 USD | 76,100.00 USD | 47,540.00 USD | 174,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1057` | 795,220.00 USD | 795,220.00 USD | 14,080.00 USD | 11,900.00 USD | 33,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1058` | 1,370,000.00 USD | 1,370,000.00 USD | 59,100.00 USD | 24,600.00 USD | 136,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1059` | 900,250.00 USD | 900,250.00 USD | 26,780.00 USD | 5,730.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1060` | 1,540,000.00 USD | 1,540,000.00 USD | 42,390.00 USD | 51,150.00 USD | 79,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1061` | 975,160.00 USD | 975,160.00 USD | 31,100.00 USD | 4,800.00 USD | 39,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1062` | 1,700,000.00 USD | 1,700,000.00 USD | 46,950.00 USD | 28,310.00 USD | 82,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1063` | 1,060,000.00 USD | 1,060,000.00 USD | 34,110.00 USD | 4,070.00 USD | 50,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1064` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 44,270.00 USD | 144,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1065` | 1,130,000.00 USD | 1,130,000.00 USD | 12,870.00 USD | 15,500.00 USD | 35,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1066` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 42,670.00 USD | 107,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1067` | 1,200,000.00 USD | 1,200,000.00 USD | 14,200.00 USD | 10,080.00 USD | 44,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1068` | 2,170,000.00 USD | 2,170,000.00 USD | 5,330.00 USD | 41,360.00 USD | 79,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1069` | 1,270,000.00 USD | 1,270,000.00 USD | 23,520.00 USD | 9,120.00 USD | 43,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1070` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 45,840.00 USD | 98,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1071` | 1,300,000.00 USD | 1,300,000.00 USD | 9,290.00 USD | 10,430.00 USD | 8,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1072` | 2,340,000.00 USD | 2,340,000.00 USD | 12,890.00 USD | 9,400.00 USD | 10,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1073` | 1,310,000.00 USD | 1,310,000.00 USD | 4,070.00 USD | 1,530.00 USD | 7,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1074` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 21,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1075` | 1,320,000.00 USD | 1,320,000.00 USD | 2,260.00 USD | 3,070.00 USD | 5,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1076` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 22,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1077` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 619.42 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1078` | 2,400,000.00 USD | 2,400,000.00 USD | 5,620.00 USD | 3,380.00 USD | 290.65 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1079` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 4,300.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1080` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1081` | 1,360,000.00 USD | 1,360,000.00 USD | 4,650.00 USD | 732.74 USD | 2,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1082` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 154.22 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1083` | 1,390,000.00 USD | 1,390,000.00 USD | 9,160.00 USD | 6,710.00 USD | 10,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1084` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1085` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 385.06 USD | 65,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1086` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 65.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1087` | 1,530,000.00 USD | 1,530,000.00 USD | 28,490.00 USD | 2,510.00 USD | 44,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1088` | 2,420,000.00 USD | 2,420,000.00 USD | 5,290.00 USD | 1,420.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1089` | 1,570,000.00 USD | 1,570,000.00 USD | 29,650.00 USD | 1,580.00 USD | 3,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1090` | 2,440,000.00 USD | 2,440,000.00 USD | 16,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1091` | 1,600,000.00 USD | 1,600,000.00 USD | 33,700.00 USD | 0.00 USD | 16.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1092` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 1,500.00 USD | 17,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1093` | 1,620,000.00 USD | 1,620,000.00 USD | 15,480.00 USD | 1,080.00 USD | 272.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1094` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 78.56 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1095` | 1,640,000.00 USD | 1,640,000.00 USD | 4,110.00 USD | 1,890.00 USD | 21,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1096` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 111.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1097` | 1,680,000.00 USD | 1,680,000.00 USD | 7,260.00 USD | 2,530.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1098` | 2,500,000.00 USD | 2,500,000.00 USD | 18,600.00 USD | 0.00 USD | 21,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1099` | 1,680,000.00 USD | 1,680,000.00 USD | 6,130.00 USD | 1,940.00 USD | 32.38 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1100` | 2,510,000.00 USD | 2,510,000.00 USD | 11,470.00 USD | 0.00 USD | 34.51 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1101` | 1,700,000.00 USD | 1,700,000.00 USD | 5,570.00 USD | 3,820.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1102` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1103` | 1,710,000.00 USD | 1,710,000.00 USD | 3,540.00 USD | 6,900.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1104` | 2,560,000.00 USD | 2,560,000.00 USD | 17,490.00 USD | 4,450.00 USD | 93.57 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1105` | 1,730,000.00 USD | 1,730,000.00 USD | 3,380.00 USD | 4,740.00 USD | 10,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1106` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 18,420.00 USD | 16,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1107` | 1,780,000.00 USD | 1,780,000.00 USD | 3,110.00 USD | 13,200.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1108` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 4,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1109` | 1,790,000.00 USD | 1,790,000.00 USD | 2,110.00 USD | 1,370.00 USD | 2,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1110` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 12,430.00 USD | 35.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1111` | 1,790,000.00 USD | 1,790,000.00 USD | 5,200.00 USD | 996.46 USD | 104.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1112` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 11,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1113` | 1,830,000.00 USD | 1,830,000.00 USD | 21,390.00 USD | 5,880.00 USD | 13,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1115` | 1,840,000.00 USD | 1,840,000.00 USD | 6,690.00 USD | 465.26 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1115` | 1,770.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1116` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 28.89 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1117` | 1,890,000.00 USD | 1,890,000.00 USD | 2,060.00 USD | 19,290.00 USD | 28,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1118` | 2,700,000.00 USD | 2,700,000.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1119` | 1,950,000.00 USD | 1,950,000.00 USD | 23,420.00 USD | 7,540.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1120` | 2,750,000.00 USD | 2,750,000.00 USD | 17,760.00 USD | 0.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1121` | 2,000,000.00 USD | 2,000,000.00 USD | 21,300.00 USD | 12,810.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1122` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 23,980.00 USD | 34,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1123` | 2,040,000.00 USD | 2,040,000.00 USD | 30,640.00 USD | 2,870.00 USD | 8,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1124` | 2,870,000.00 USD | 2,870,000.00 USD | 19,800.00 USD | 2,030.00 USD | 40,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1125` | 2,080,000.00 USD | 2,080,000.00 USD | 11,890.00 USD | 12,350.00 USD | 11,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1126` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 4,950.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1127` | 2,110,000.00 USD | 2,110,000.00 USD | 1,670.00 USD | 4,120.00 USD | 22,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1128` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 2,020.00 USD | 17,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1129` | 2,130,000.00 USD | 2,130,000.00 USD | 11,080.00 USD | 1,390.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1130` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1131` | 2,180,000.00 USD | 2,180,000.00 USD | 24,040.00 USD | 6,440.00 USD | 24,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1132` | 2,940,000.00 USD | 2,940,000.00 USD | 12,540.00 USD | 0.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1133` | 2,230,000.00 USD | 2,230,000.00 USD | 8,350.00 USD | 19,380.00 USD | 24,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1134` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 14,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1135` | 2,250,000.00 USD | 2,250,000.00 USD | 5,340.00 USD | 3,200.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1136` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1137` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 1,140.00 USD | 356.31 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1138` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1139` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1140` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1141` | 2,290,000.00 USD | 2,290,000.00 USD | 8,110.00 USD | 0.00 USD | 21,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1142` | 2,990,000.00 USD | 2,990,000.00 USD | 10,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1143` | 2,340,000.00 USD | 2,340,000.00 USD | 18,700.00 USD | 22,390.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1144` | 2,360,000.00 USD | 2,360,000.00 USD | 4,680.00 USD | 0.00 USD | 18,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1144` | 3,150,000.00 USD | 3,150,000.00 USD | 10,360.00 USD | 2,730.00 USD | 143,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1146` | 3,350,000.00 USD | 3,350,000.00 USD | 16,060.00 USD | 0.00 USD | 188,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1148` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 63,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1150` | 3,530,000.00 USD | 3,530,000.00 USD | 18,520.00 USD | 0.00 USD | 89,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1152` | 3,840,000.00 USD | 3,840,000.00 USD | 165,860.00 USD | 12,610.00 USD | 132,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1154` | 4,150,000.00 USD | 4,150,000.00 USD | 149,770.00 USD | 18,580.00 USD | 143,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1156` | 4,370,000.00 USD | 4,370,000.00 USD | 128,780.00 USD | 21,540.00 USD | 74,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1185` | 4,330.00 USD | 6,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1225` | 721.08 USD | 6,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1315` | 206.95 USD | 7,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1385` | 3,720.00 USD | 10,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1485` | 21,680.00 USD | 32,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1525` | 6,090.00 USD | 38,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1565` | 550.61 USD | 39,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1695` | 169.25 USD | 39,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1745` | 131.08 USD | 39,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1755` | 147.21 USD | 39,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1795` | 100.88 USD | 39,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1825` | 514.28 USD | 40,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1855` | 166.95 USD | 40,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1865` | 199.93 USD | 40,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1885` | 741.37 USD | 41,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0305` | 122,880.00 USD | 0.00 USD | 1,500.00 USD | `-70.10%` | `49,265.90` |
| `Live` | `Long` | `0.0395` | 121,380.00 USD | 0.00 USD | 201.41 USD | `-61.28%` | `5,098.90` |
| `Live` | `Long` | `0.0555` | 121,180.00 USD | 0.00 USD | 991.96 USD | `-45.60%` | `17,873.20` |
| `Live` | `Long` | `0.0575` | 120,180.00 USD | 0.00 USD | 829.69 USD | `-43.64%` | `14,429.40` |
| `Live` | `Long` | `0.0605` | 119,350.00 USD | 0.00 USD | 4,220.00 USD | `-40.70%` | `69,790.10` |
| `Live` | `Long` | `0.0645` | 115,130.00 USD | 0.00 USD | 353.81 USD | `-36.78%` | `5,485.40` |
| `Live` | `Long` | `0.0675` | 114,780.00 USD | 0.00 USD | 518.48 USD | `-33.84%` | `7,681.20` |
| `Live` | `Long` | `0.0685` | 114,260.00 USD | 0.00 USD | 1,920.00 USD | `-32.86%` | `28,000.00` |
| `Live` | `Long` | `0.0705` | 112,340.00 USD | 0.00 USD | 1,090.00 USD | `-30.90%` | `15,500.00` |
| `Live` | `Long` | `0.0715` | 111,250.00 USD | 0.00 USD | 40,420.00 USD | `-29.92%` | `565,287.50` |
| `Live` | `Long` | `0.0725` | 70,830.00 USD | 0.00 USD | 23,910.00 USD | `-28.94%` | `329,855.60` |
| `Live` | `Long` | `0.0735` | 46,920.00 USD | 0.00 USD | 2,530.00 USD | `-27.96%` | `34,439.60` |
| `Live` | `Long` | `0.0745` | 44,390.00 USD | 0.00 USD | 2,300.00 USD | `-26.98%` | `30,851.90` |
| `Live` | `Long` | `0.0755` | 42,090.00 USD | 0.00 USD | 12,440.00 USD | `-25.99%` | `164,709.50` |
| `Live` | `Long` | `0.0765` | 29,650.00 USD | 0.00 USD | 1,170.00 USD | `-25.01%` | `15,263.30` |
| `Live` | `Long` | `0.0775` | 28,480.00 USD | 0.00 USD | 878.62 USD | `-24.03%` | `11,337.00` |
| `Live` | `Long` | `0.0785` | 27,600.00 USD | 0.00 USD | 339.50 USD | `-23.05%` | `4,324.80` |
| `Live` | `Long` | `0.0795` | 27,270.00 USD | 0.00 USD | 2,710.00 USD | `-22.07%` | `34,073.20` |
| `Live` | `Long` | `0.0805` | 24,560.00 USD | 0.00 USD | 223.98 USD | `-21.09%` | `2,782.40` |
| `Live` | `Long` | `0.0815` | 24,330.00 USD | 0.00 USD | 1,560.00 USD | `-20.11%` | `19,181.40` |
| `Live` | `Long` | `0.0825` | 22,770.00 USD | 0.00 USD | 140.74 USD | `-19.13%` | `1,705.90` |
| `Live` | `Long` | `0.0845` | 22,630.00 USD | 0.00 USD | 14,300.00 USD | `-17.17%` | `169,238.60` |
| `Live` | `Long` | `0.0855` | 8,330.00 USD | 0.00 USD | 1,710.00 USD | `-16.19%` | `20,000.00` |
| `Live` | `Long` | `0.0865` | 6,620.00 USD | 0.00 USD | 318.30 USD | `-15.21%` | `3,679.80` |
| `Live` | `Long` | `0.0875` | 6,300.00 USD | 0.00 USD | 793.17 USD | `-14.23%` | `9,064.80` |
| `Live` | `Long` | `0.0895` | 5,510.00 USD | 0.00 USD | 3,270.00 USD | `-12.27%` | `36,562.50` |
| `Live` | `Long` | `0.0905` | 2,230.00 USD | 0.00 USD | 2,230.00 USD | `-11.29%` | `24,685.10` |
| `Live` | `Short` | `0.1115` | 1,770.00 USD | 1,770.00 USD | 0.00 USD | `+9.29%` | `15,878.10` |
| `Live` | `Short` | `0.1185` | 6,100.00 USD | 4,330.00 USD | 0.00 USD | `+16.15%` | `36,507.20` |
| `Live` | `Short` | `0.1225` | 6,820.00 USD | 721.08 USD | 0.00 USD | `+20.07%` | `5,886.40` |
| `Live` | `Short` | `0.1315` | 7,020.00 USD | 206.95 USD | 0.00 USD | `+28.90%` | `1,573.80` |
| `Live` | `Short` | `0.1385` | 10,750.00 USD | 3,720.00 USD | 0.00 USD | `+35.76%` | `26,889.40` |
| `Live` | `Short` | `0.1485` | 32,430.00 USD | 21,680.00 USD | 0.00 USD | `+45.56%` | `145,985.00` |
| `Live` | `Short` | `0.1525` | 38,520.00 USD | 6,090.00 USD | 0.00 USD | `+49.48%` | `39,929.50` |
| `Live` | `Short` | `0.1565` | 39,070.00 USD | 550.61 USD | 0.00 USD | `+53.40%` | `3,518.30` |
| `Live` | `Short` | `0.1695` | 39,240.00 USD | 169.25 USD | 0.00 USD | `+66.14%` | `998.50` |
| `Live` | `Short` | `0.1745` | 39,370.00 USD | 131.08 USD | 0.00 USD | `+71.04%` | `751.20` |
| `Live` | `Short` | `0.1755` | 39,510.00 USD | 147.21 USD | 0.00 USD | `+72.03%` | `838.80` |
| `Live` | `Short` | `0.1795` | 39,620.00 USD | 100.88 USD | 0.00 USD | `+75.95%` | `562.00` |
| `Live` | `Short` | `0.1825` | 40,130.00 USD | 514.28 USD | 0.00 USD | `+78.89%` | `2,818.00` |
| `Live` | `Short` | `0.1855` | 40,300.00 USD | 166.95 USD | 0.00 USD | `+81.83%` | `900.00` |
| `Live` | `Short` | `0.1865` | 40,500.00 USD | 199.93 USD | 0.00 USD | `+82.81%` | `1,072.00` |
| `Live` | `Short` | `0.1885` | 41,240.00 USD | 741.37 USD | 0.00 USD | `+84.77%` | `3,933.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0635` | 34,300.00 USD | 0.00 USD | 1,140.00 USD | `-37.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 33,160.00 USD | 0.00 USD | 773.46 USD | `-30.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 32,390.00 USD | 0.00 USD | 592.27 USD | `-29.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 31,790.00 USD | 0.00 USD | 755.00 USD | `-25.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0805` | 31,040.00 USD | 0.00 USD | 411.06 USD | `-21.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0815` | 30,630.00 USD | 0.00 USD | 285.01 USD | `-20.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0835` | 30,340.00 USD | 0.00 USD | 456.70 USD | `-18.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0845` | 29,890.00 USD | 0.00 USD | 171.09 USD | `-17.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 29,720.00 USD | 0.00 USD | 631.58 USD | `-16.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 29,080.00 USD | 0.00 USD | 380.89 USD | `-15.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 28,700.00 USD | 0.00 USD | 782.05 USD | `-13.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 27,920.00 USD | 0.00 USD | 444.62 USD | `-11.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0915` | 27,480.00 USD | 0.00 USD | 623.91 USD | `-10.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 26,850.00 USD | 0.00 USD | 485.13 USD | `-7.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0965` | 26,370.00 USD | 0.00 USD | 5,700.00 USD | `-5.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0975` | 20,670.00 USD | 0.00 USD | 216.41 USD | `-4.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0985` | 20,450.00 USD | 0.00 USD | 144.62 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0995` | 20,310.00 USD | 0.00 USD | 17,230.00 USD | `-2.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 3,080.00 USD | 0.00 USD | 2,180.00 USD | `-1.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1015` | 903.42 USD | 0.00 USD | 903.42 USD | `-0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1025` | 780.70 USD | 780.70 USD | 0.00 USD | `+0.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1035` | 2,420.00 USD | 1,640.00 USD | 0.00 USD | `+1.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,530.00 USD | 105.53 USD | 0.00 USD | `+2.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 3,270.00 USD | 737.12 USD | 0.00 USD | `+3.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 112,550.00 USD | 109,280.00 USD | 0.00 USD | `+4.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1075` | 113,020.00 USD | 473.35 USD | 0.00 USD | `+5.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 113,180.00 USD | 160.20 USD | 0.00 USD | `+8.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 113,430.00 USD | 247.49 USD | 0.00 USD | `+9.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1125` | 114,220.00 USD | 786.65 USD | 0.00 USD | `+10.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1135` | 114,330.00 USD | 116.27 USD | 0.00 USD | `+11.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 114,470.00 USD | 137.71 USD | 0.00 USD | `+13.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1165` | 114,650.00 USD | 180.81 USD | 0.00 USD | `+14.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1175` | 115,010.00 USD | 363.49 USD | 0.00 USD | `+15.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1185` | 115,280.00 USD | 265.74 USD | 0.00 USD | `+16.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1195` | 129,920.00 USD | 14,640.00 USD | 0.00 USD | `+17.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1225` | 130,900.00 USD | 980.00 USD | 0.00 USD | `+20.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1235` | 138,260.00 USD | 7,370.00 USD | 0.00 USD | `+21.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1255` | 142,640.00 USD | 4,380.00 USD | 0.00 USD | `+23.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1315` | 174,200.00 USD | 31,560.00 USD | 0.00 USD | `+28.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1335` | 175,520.00 USD | 1,310.00 USD | 0.00 USD | `+30.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1345` | 179,670.00 USD | 4,150.00 USD | 0.00 USD | `+31.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1365` | 187,410.00 USD | 7,750.00 USD | 0.00 USD | `+33.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1405` | 200,520.00 USD | 13,110.00 USD | 0.00 USD | `+37.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1425` | 200,620.00 USD | 102.22 USD | 0.00 USD | `+39.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1435` | 207,800.00 USD | 7,180.00 USD | 0.00 USD | `+40.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1485` | 210,450.00 USD | 2,650.00 USD | 0.00 USD | `+45.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1525` | 214,210.00 USD | 3,770.00 USD | 0.00 USD | `+49.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 214,400.00 USD | 184.49 USD | 0.00 USD | `+52.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 217,210.00 USD | 2,810.00 USD | 0.00 USD | `+53.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 217,430.00 USD | 219.81 USD | 0.00 USD | `+54.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 217,700.00 USD | 277.62 USD | 0.00 USD | `+60.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 219,730.00 USD | 2,030.00 USD | 0.00 USD | `+66.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 219,950.00 USD | 216.55 USD | 0.00 USD | `+71.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 220,070.00 USD | 117.26 USD | 0.00 USD | `+93.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 240,600.00 USD | 20,530.00 USD | 0.00 USD | `+96.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 240,790.00 USD | 189.30 USD | 0.00 USD | `+99.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 241,010.00 USD | 219.22 USD | 0.00 USD | `+100.45%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0860` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 1,880.00 USD | 0.00 USD | 2,160.00 USD |
| `7D` | `0.0862` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 0.00 USD | 1,880.00 USD | 4,720.00 USD |
| `7D` | `0.0864` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 0.00 USD | 1,980.00 USD | 15,640.00 USD |
| `7D` | `0.0866` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 2,080.00 USD |
| `7D` | `0.0868` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 2,880.00 USD |
| `7D` | `0.0870` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 2,870.00 USD |
| `7D` | `0.0872` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 0.00 USD | 1,200.00 USD | 2,980.00 USD |
| `7D` | `0.0874` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 6,010.00 USD | 0.00 USD | 4,500.00 USD |
| `7D` | `0.0876` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 0.00 USD | 1,770.00 USD | 4,890.00 USD |
| `7D` | `0.0878` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 9,200.00 USD | 5,890.00 USD | 25,110.00 USD |
| `7D` | `0.0880` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 3,770.00 USD | 2,200.00 USD | 11,840.00 USD |
| `7D` | `0.0882` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 12,660.00 USD | 7,260.00 USD | 9,180.00 USD |
| `7D` | `0.0884` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 0.00 USD | 1,220.00 USD | 13,650.00 USD |
| `7D` | `0.0886` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 9,350.00 USD | 2,470.00 USD | 11,320.00 USD |
| `7D` | `0.0888` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 3,370.00 USD | 2,720.00 USD | 8,290.00 USD |
| `7D` | `0.0890` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 13,510.00 USD | 3,610.00 USD | 13,150.00 USD |
| `7D` | `0.0892` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 3,620.00 USD | 3,060.00 USD | 2,090.00 USD |
| `7D` | `0.0894` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 5,480.00 USD | 3,400.00 USD | 7,750.00 USD |
| `7D` | `0.0896` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 4,300.00 USD | 0.00 USD | 4,200.00 USD |
| `7D` | `0.0898` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 3,390.00 USD | 927.82 USD | 4,460.00 USD |
| `7D` | `0.0900` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 1,250.00 USD | 428.11 USD | 77.78 USD |
| `7D` | `0.0902` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 1,030.00 USD | 482.67 USD | 1,300.00 USD |
| `7D` | `0.0904` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 5,730.00 USD | 996.61 USD | 1,700.00 USD |
| `7D` | `0.0906` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 6,040.00 USD | 1,900.00 USD | 4,140.00 USD |
| `7D` | `0.0908` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 2,540.00 USD | 2,570.00 USD | 1,290.00 USD |
| `7D` | `0.0910` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 0.00 USD | 606.54 USD | 48.03 USD |
| `7D` | `0.0912` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 2,650.00 USD |
| `7D` | `0.0914` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 1,670.00 USD | 903.90 USD | 56.36 USD |
| `7D` | `0.0916` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 6,310.00 USD |
| `1D` | `0.0917` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 10,440.00 USD | 5,150.00 USD | 269.80 USD |
| `7D` | `0.0918` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 1,740.00 USD |
| `1D` | `0.0919` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 8,950.00 USD | 1,090.00 USD | 19,100.00 USD |
| `7D` | `0.0920` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 7,440.00 USD | 2,030.00 USD | 223.39 USD |
| `1D` | `0.0921` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 758.20 USD | 2,040.00 USD | 3,820.00 USD |
| `7D` | `0.0922` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 0.00 USD | 7,660.00 USD | 34,750.00 USD |
| `1D` | `0.0923` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 4,040.00 USD | 6,180.00 USD | 30,020.00 USD |
| `7D` | `0.0924` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 1,790.00 USD | 2,020.00 USD | 11,850.00 USD |
| `1D` | `0.0925` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 6,480.00 USD | 4,210.00 USD | 27,920.00 USD |
| `7D` | `0.0926` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 8,180.00 USD |
| `1D` | `0.0927` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 1,820.00 USD | 2,300.00 USD | 1,130.00 USD |
| `7D` | `0.0928` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD |
| `1D` | `0.0929` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 5,660.00 USD | 1,800.00 USD | 1,320.00 USD |
| `7D` | `0.0930` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD |
| `1D` | `0.0931` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | 635.90 USD | 7,790.00 USD |
| `7D` | `0.0932` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 12,290.00 USD |
| `1D` | `0.0933` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 16,500.00 USD | 0.00 USD | 11,170.00 USD |
| `1D` | `0.0935` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 8,990.00 USD | 7,300.00 USD | 15,690.00 USD |
| `7D` | `0.0936` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 19,560.00 USD | 6,840.00 USD | 25,450.00 USD |
| `1D` | `0.0937` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 4,580.00 USD | 6,660.00 USD | 13,310.00 USD |
| `7D` | `0.0938` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 248.29 USD |
| `1D` | `0.0939` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 3,590.00 USD | 2,140.00 USD | 44,370.00 USD |
| `7D` | `0.0940` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 14,050.00 USD | 0.00 USD | 10,640.00 USD |
| `1D` | `0.0941` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 0.00 USD | 9,410.00 USD | 21,110.00 USD |
| `7D` | `0.0942` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 6,170.00 USD | 18,340.00 USD | 114,170.00 USD |
| `1D` | `0.0943` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 3,500.00 USD | 10,920.00 USD | 30,420.00 USD |
| `7D` | `0.0944` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 0.00 USD | 2,010.00 USD | 0.00 USD |
| `1D` | `0.0945` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 15,750.00 USD | 6,510.00 USD | 44,380.00 USD |
| `7D` | `0.0946` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 0.00 USD | 1,810.00 USD | 154.22 USD |
| `1D` | `0.0947` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 0.00 USD | 962.66 USD | 91.75 USD |
| `7D` | `0.0948` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 3,770.00 USD | 0.00 USD | 26,920.00 USD |
| `1D` | `0.0949` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 12,180.00 USD | 5,770.00 USD | 2,940.00 USD |
| `7D` | `0.0950` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 0.00 USD | 9,700.00 USD | 134.31 USD |
| `1D` | `0.0951` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 2,030.00 USD | 19,990.00 USD |
| `7D` | `0.0952` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 0.00 USD | 4,410.00 USD | 0.00 USD |
| `1D` | `0.0953` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 33,000.00 USD | 4,360.00 USD | 6,780.00 USD |
| `7D` | `0.0954` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 0.00 USD | 3,740.00 USD | 187.14 USD |
| `1D` | `0.0955` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 17,990.00 USD | 14,600.00 USD | 31,680.00 USD |
| `7D` | `0.0956` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 39,120.00 USD | 13,670.00 USD | 50,980.00 USD |
| `1D` | `0.0957` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 16,340.00 USD | 6,740.00 USD | 48,740.00 USD |
| `7D` | `0.0958` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 21,370.00 USD |
| `1D` | `0.0959` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 0.00 USD | 3,100.00 USD | 50.26 USD |
| `7D` | `0.0960` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 28,110.00 USD | 16,920.00 USD | 20,150.00 USD |
| `1D` | `0.0961` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 8,920.00 USD | 23,950.00 USD | 23,330.00 USD |
| `7D` | `0.0962` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 12,340.00 USD | 0.00 USD | 75,010.00 USD |
| `1D` | `0.0963` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 23,240.00 USD | 11,750.00 USD | 11,980.00 USD |
| `7D` | `0.0964` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | 4,020.00 USD | 86.68 USD |
| `1D` | `0.0965` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 8,250.00 USD | 5,890.00 USD | 20,440.00 USD |
| `7D` | `0.0966` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | 2,390.00 USD | 2,830.00 USD |
| `1D` | `0.0967` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 1,960.00 USD | 818.32 USD |
| `7D` | `0.0968` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 7,490.00 USD | 0.00 USD | 56,170.00 USD |
| `1D` | `0.0969` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 6,930.00 USD | 7,530.00 USD | 8,080.00 USD |
| `7D` | `0.0970` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 0.00 USD | 7,090.00 USD | 5,010.00 USD |
| `1D` | `0.0971` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 2,840.00 USD | 4,070.00 USD | 10,240.00 USD |
| `7D` | `0.0972` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 0.00 USD | 8,830.00 USD | 0.00 USD |
| `1D` | `0.0973` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 1,440.00 USD | 10,220.00 USD | 1,980.00 USD |
| `7D` | `0.0974` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 0.00 USD | 7,480.00 USD | 104.80 USD |
| `1D` | `0.0975` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 114.54 USD |
| `7D` | `0.0976` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 148.46 USD |
| `1D` | `0.0977` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 0.00 USD | 765.93 USD | 978.56 USD |
| `1D` | `0.0979` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 5,180.00 USD | 2,920.00 USD | 21,150.00 USD |
| `7D` | `0.0980` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 22,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0981` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 12,740.00 USD | 7,060.00 USD | 0.00 USD |
| `7D` | `0.0982` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 0.00 USD | 5,070.00 USD | 11,350.00 USD |
| `1D` | `0.0983` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 11,130.00 USD | 16,910.00 USD | 10,320.00 USD |
| `7D` | `0.0984` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 16,160.00 USD | 0.00 USD |
| `1D` | `0.0985` | 973,910.00 USD | 0.00 USD | 973,910.00 USD | 5,970.00 USD | 8,750.00 USD | 12,480.00 USD |
| `7D` | `0.0986` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 5,330.00 USD | 16,520.00 USD | 6,690.00 USD |
| `1D` | `0.0987` | 946,710.00 USD | 0.00 USD | 946,710.00 USD | 30,280.00 USD | 7,610.00 USD | 16,110.00 USD |
| `7D` | `0.0988` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 10,360.00 USD | 7,820.00 USD | 0.00 USD |
| `1D` | `0.0989` | 892,720.00 USD | 0.00 USD | 892,720.00 USD | 8,920.00 USD | 9,270.00 USD | 24,520.00 USD |
| `7D` | `0.0990` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 26,690.00 USD | 6,660.00 USD | 0.00 USD |
| `1D` | `0.0991` | 850,010.00 USD | 0.00 USD | 850,010.00 USD | 74,010.00 USD | 1,530.00 USD | 4,190.00 USD |
| `7D` | `0.0992` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 12,790.00 USD | 3,930.00 USD | 0.00 USD |
| `1D` | `0.0993` | 770,280.00 USD | 0.00 USD | 770,280.00 USD | 23,230.00 USD | 5,240.00 USD | 45,180.00 USD |
| `7D` | `0.0994` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 50,250.00 USD | 0.00 USD | 65,080.00 USD |
| `1D` | `0.0995` | 696,640.00 USD | 0.00 USD | 696,640.00 USD | 16,240.00 USD | 898.20 USD | 52,930.00 USD |
| `7D` | `0.0996` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 27,010.00 USD | 5,500.00 USD | 32,940.00 USD |
| `1D` | `0.0997` | 626,570.00 USD | 0.00 USD | 626,570.00 USD | 17,900.00 USD | 7,370.00 USD | 55,500.00 USD |
| `7D` | `0.0998` | 974,820.00 USD | 0.00 USD | 974,820.00 USD | 14,530.00 USD | 11,540.00 USD | 113,290.00 USD |
| `1D` | `0.0999` | 545,810.00 USD | 0.00 USD | 545,810.00 USD | 0.00 USD | 11,820.00 USD | 47,880.00 USD |
| `7D` | `0.1000` | 835,470.00 USD | 0.00 USD | 835,470.00 USD | 54,220.00 USD | 25,020.00 USD | 33,080.00 USD |
| `1D` | `0.1001` | 486,110.00 USD | 0.00 USD | 486,110.00 USD | 25,400.00 USD | 4,200.00 USD | 42,510.00 USD |
| `7D` | `0.1002` | 723,140.00 USD | 0.00 USD | 723,140.00 USD | 70,060.00 USD | 10,690.00 USD | 74,890.00 USD |
| `1D` | `0.1003` | 413,990.00 USD | 0.00 USD | 413,990.00 USD | 37,160.00 USD | 10,200.00 USD | 27,200.00 USD |
| `7D` | `0.1004` | 567,500.00 USD | 0.00 USD | 567,500.00 USD | 19,310.00 USD | 17,550.00 USD | 46,130.00 USD |
| `1D` | `0.1005` | 339,440.00 USD | 0.00 USD | 339,440.00 USD | 31,310.00 USD | 43,010.00 USD | 66,000.00 USD |
| `7D` | `0.1006` | 484,520.00 USD | 0.00 USD | 484,520.00 USD | 23,200.00 USD | 23,170.00 USD | 67,130.00 USD |
| `1D` | `0.1007` | 199,120.00 USD | 0.00 USD | 199,120.00 USD | 21,860.00 USD | 7,380.00 USD | 8,630.00 USD |
| `7D` | `0.1008` | 371,020.00 USD | 0.00 USD | 371,020.00 USD | 13,040.00 USD | 5,470.00 USD | 96,530.00 USD |
| `1D` | `0.1009` | 161,250.00 USD | 0.00 USD | 161,250.00 USD | 20,400.00 USD | 15,460.00 USD | 5,600.00 USD |
| `7D` | `0.1010` | 255,980.00 USD | 0.00 USD | 255,980.00 USD | 22,770.00 USD | 24,610.00 USD | 3,990.00 USD |
| `1D` | `0.1011` | 119,790.00 USD | 0.00 USD | 119,790.00 USD | 8,150.00 USD | 7,120.00 USD | 24,120.00 USD |
| `7D` | `0.1012` | 204,620.00 USD | 0.00 USD | 204,620.00 USD | 6,490.00 USD | 20,640.00 USD | 0.00 USD |
| `1D` | `0.1013` | 80,400.00 USD | 0.00 USD | 80,400.00 USD | 1,640.00 USD | 4,430.00 USD | 14,470.00 USD |
| `7D` | `0.1014` | 177,490.00 USD | 0.00 USD | 177,490.00 USD | 29,790.00 USD | 15,590.00 USD | 25,450.00 USD |
| `1D` | `0.1015` | 59,860.00 USD | 0.00 USD | 59,860.00 USD | 4,580.00 USD | 1,220.00 USD | 20,200.00 USD |
| `7D` | `0.1016` | 106,670.00 USD | 0.00 USD | 106,670.00 USD | 14,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1017` | 33,860.00 USD | 0.00 USD | 33,860.00 USD | 3,590.00 USD | 0.00 USD | 11,110.00 USD |
| `7D` | `0.1018` | 92,670.00 USD | 0.00 USD | 92,670.00 USD | 26,150.00 USD | 0.00 USD | 10,630.00 USD |
| `1D` | `0.1019` | 19,160.00 USD | 0.00 USD | 19,160.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD |
| `7D` | `0.1020` | 55,890.00 USD | 0.00 USD | 55,890.00 USD | 0.00 USD | 8,460.00 USD | 47,420.00 USD |
| `1D` | `0.1021` | 17,610.00 USD | 0.00 USD | 17,610.00 USD | 0.00 USD | 0.00 USD | 13,880.00 USD |
| `1D` | `0.1023` | 3,720.00 USD | 0.00 USD | 3,720.00 USD | 0.00 USD | 0.00 USD | 3,720.00 USD |
| `1D` | `0.1030` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1031` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1032` | 13,180.00 USD | 13,180.00 USD | 0.00 USD | 13,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1034` | 18,920.00 USD | 18,920.00 USD | 0.00 USD | 5,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1035` | 7,220.00 USD | 7,220.00 USD | 0.00 USD | 0.00 USD | 7,220.00 USD | 0.00 USD |
| `7D` | `0.1036` | 21,740.00 USD | 21,740.00 USD | 0.00 USD | 2,710.00 USD | 0.00 USD | 108.00 USD |
| `1D` | `0.1037` | 55,180.00 USD | 55,180.00 USD | 0.00 USD | 35,090.00 USD | 12,850.00 USD | 24.05 USD |
| `7D` | `0.1038` | 63,960.00 USD | 63,960.00 USD | 0.00 USD | 0.00 USD | 10,870.00 USD | 31,350.00 USD |
| `1D` | `0.1039` | 76,020.00 USD | 76,020.00 USD | 0.00 USD | 6,500.00 USD | 9,120.00 USD | 5,220.00 USD |
| `7D` | `0.1040` | 75,040.00 USD | 75,040.00 USD | 0.00 USD | 5,940.00 USD | 5,130.00 USD | 0.00 USD |
| `1D` | `0.1041` | 149,240.00 USD | 149,240.00 USD | 0.00 USD | 36,920.00 USD | 16,680.00 USD | 19,630.00 USD |
| `7D` | `0.1042` | 136,600.00 USD | 136,600.00 USD | 0.00 USD | 49,380.00 USD | 12,190.00 USD | 0.00 USD |
| `1D` | `0.1043` | 205,940.00 USD | 205,940.00 USD | 0.00 USD | 13,920.00 USD | 18,610.00 USD | 24,170.00 USD |
| `7D` | `0.1044` | 195,750.00 USD | 195,750.00 USD | 0.00 USD | 11,140.00 USD | 25,310.00 USD | 22,700.00 USD |
| `1D` | `0.1045` | 261,440.00 USD | 261,440.00 USD | 0.00 USD | 12,990.00 USD | 21,860.00 USD | 20,650.00 USD |
| `7D` | `0.1046` | 279,050.00 USD | 279,050.00 USD | 0.00 USD | 0.00 USD | 23,140.00 USD | 60,160.00 USD |
| `1D` | `0.1047` | 375,130.00 USD | 375,130.00 USD | 0.00 USD | 40,510.00 USD | 22,900.00 USD | 50,280.00 USD |
| `7D` | `0.1048` | 366,430.00 USD | 366,430.00 USD | 0.00 USD | 30,640.00 USD | 14,940.00 USD | 41,800.00 USD |
| `1D` | `0.1049` | 498,280.00 USD | 498,280.00 USD | 0.00 USD | 35,540.00 USD | 20,770.00 USD | 66,840.00 USD |
| `7D` | `0.1050` | 457,350.00 USD | 457,350.00 USD | 0.00 USD | 27,290.00 USD | 0.00 USD | 63,630.00 USD |
| `1D` | `0.1051` | 569,560.00 USD | 569,560.00 USD | 0.00 USD | 33,470.00 USD | 21,790.00 USD | 16,030.00 USD |
| `7D` | `0.1052` | 621,680.00 USD | 621,680.00 USD | 0.00 USD | 25,850.00 USD | 34,840.00 USD | 103,650.00 USD |
| `1D` | `0.1053` | 647,840.00 USD | 647,840.00 USD | 0.00 USD | 21,820.00 USD | 10,090.00 USD | 46,360.00 USD |
| `7D` | `0.1054` | 838,470.00 USD | 838,470.00 USD | 0.00 USD | 85,290.00 USD | 38,660.00 USD | 92,830.00 USD |
| `1D` | `0.1055` | 736,250.00 USD | 736,250.00 USD | 0.00 USD | 31,320.00 USD | 17,760.00 USD | 39,330.00 USD |
| `7D` | `0.1056` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 76,100.00 USD | 47,540.00 USD | 174,740.00 USD |
| `1D` | `0.1057` | 795,750.00 USD | 795,750.00 USD | 0.00 USD | 14,080.00 USD | 11,900.00 USD | 33,530.00 USD |
| `7D` | `0.1058` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 59,100.00 USD | 24,600.00 USD | 136,660.00 USD |
| `1D` | `0.1059` | 900,770.00 USD | 900,770.00 USD | 0.00 USD | 26,780.00 USD | 5,730.00 USD | 72,520.00 USD |
| `7D` | `0.1060` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 42,390.00 USD | 51,150.00 USD | 79,920.00 USD |
| `1D` | `0.1061` | 975,680.00 USD | 975,680.00 USD | 0.00 USD | 31,100.00 USD | 4,800.00 USD | 39,010.00 USD |
| `7D` | `0.1062` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 46,950.00 USD | 28,310.00 USD | 82,360.00 USD |
| `1D` | `0.1063` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 34,110.00 USD | 4,070.00 USD | 50,880.00 USD |
| `7D` | `0.1064` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 44,270.00 USD | 144,960.00 USD |
| `1D` | `0.1065` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 12,870.00 USD | 15,500.00 USD | 35,010.00 USD |
| `7D` | `0.1066` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 42,670.00 USD | 107,620.00 USD |
| `1D` | `0.1067` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 14,200.00 USD | 10,080.00 USD | 44,390.00 USD |
| `7D` | `0.1068` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 5,330.00 USD | 41,360.00 USD | 79,350.00 USD |
| `1D` | `0.1069` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 23,520.00 USD | 9,120.00 USD | 43,350.00 USD |
| `7D` | `0.1070` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 45,840.00 USD | 98,490.00 USD |
| `1D` | `0.1071` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 9,290.00 USD | 10,430.00 USD | 8,620.00 USD |
| `7D` | `0.1072` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 12,890.00 USD | 9,400.00 USD | 10,320.00 USD |
| `1D` | `0.1073` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 4,070.00 USD | 1,530.00 USD | 8,390.00 USD |
| `7D` | `0.1074` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 21,630.00 USD | 0.00 USD |
| `1D` | `0.1075` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 2,260.00 USD | 3,070.00 USD | 5,830.00 USD |
| `7D` | `0.1076` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,600.00 USD |
| `1D` | `0.1077` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 619.42 USD | 3,680.00 USD |
| `7D` | `0.1078` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 5,620.00 USD | 3,380.00 USD | 290.65 USD |
| `1D` | `0.1079` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 4,300.00 USD | 21,940.00 USD |
| `7D` | `0.1080` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,860.00 USD |
| `1D` | `0.1081` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 4,650.00 USD | 732.74 USD | 2,440.00 USD |
| `7D` | `0.1082` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 154.22 USD |
| `1D` | `0.1083` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 9,160.00 USD | 6,710.00 USD | 10,790.00 USD |
| `7D` | `0.1084` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1085` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 385.06 USD | 65,050.00 USD |
| `7D` | `0.1086` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65.29 USD |
| `1D` | `0.1087` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 28,490.00 USD | 2,510.00 USD | 44,700.00 USD |
| `7D` | `0.1088` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 5,290.00 USD | 1,420.00 USD | 9,590.00 USD |
| `1D` | `0.1089` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 29,650.00 USD | 1,580.00 USD | 3,310.00 USD |
| `7D` | `0.1090` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1091` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 33,700.00 USD | 0.00 USD | 16.51 USD |
| `7D` | `0.1092` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 1,500.00 USD | 17,740.00 USD |
| `1D` | `0.1093` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 15,480.00 USD | 1,080.00 USD | 272.04 USD |
| `7D` | `0.1094` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78.56 USD |
| `1D` | `0.1095` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 21,610.00 USD |
| `7D` | `0.1096` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 111.29 USD |
| `1D` | `0.1097` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 7,260.00 USD | 2,530.00 USD | 22,850.00 USD |
| `7D` | `0.1098` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 21,840.00 USD |
| `1D` | `0.1099` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 6,130.00 USD | 1,940.00 USD | 32.38 USD |
| `7D` | `0.1100` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 34.51 USD |
| `1D` | `0.1101` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 5,570.00 USD | 3,820.00 USD | 4,290.00 USD |
| `7D` | `0.1102` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1103` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 3,540.00 USD | 6,900.00 USD | 1,160.00 USD |
| `7D` | `0.1104` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 17,490.00 USD | 4,450.00 USD | 93.57 USD |
| `1D` | `0.1105` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 3,380.00 USD | 4,740.00 USD | 10,710.00 USD |
| `7D` | `0.1106` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 18,420.00 USD | 16,040.00 USD |
| `1D` | `0.1107` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 3,110.00 USD | 13,200.00 USD | 35,750.00 USD |
| `7D` | `0.1108` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 4,120.00 USD | 0.00 USD |
| `1D` | `0.1109` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 2,110.00 USD | 1,370.00 USD | 2,670.00 USD |
| `7D` | `0.1110` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 12,430.00 USD | 35.29 USD |
| `1D` | `0.1111` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 5,200.00 USD | 996.46 USD | 104.00 USD |
| `7D` | `0.1112` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 0.00 USD |
| `1D` | `0.1113` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 21,390.00 USD | 5,880.00 USD | 13,550.00 USD |
| `1D` | `0.1115` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 6,690.00 USD | 465.26 USD | 0.00 USD |
| `7D` | `0.1116` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28.89 USD |
| `1D` | `0.1117` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 2,060.00 USD | 16,310.00 USD | 28,210.00 USD |
| `7D` | `0.1118` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD |
| `1D` | `0.1119` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 23,420.00 USD | 7,540.00 USD | 31,040.00 USD |
| `7D` | `0.1120` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 17,760.00 USD | 0.00 USD | 29,770.00 USD |
| `1D` | `0.1121` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 21,300.00 USD | 12,810.00 USD | 12,350.00 USD |
| `7D` | `0.1122` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 23,980.00 USD | 34,740.00 USD |
| `1D` | `0.1123` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 30,640.00 USD | 2,870.00 USD | 8,450.00 USD |
| `7D` | `0.1124` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 19,800.00 USD | 2,030.00 USD | 40,520.00 USD |
| `1D` | `0.1125` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 11,890.00 USD | 12,350.00 USD | 11,740.00 USD |
| `7D` | `0.1126` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 4,950.00 USD | 7,340.00 USD |
| `1D` | `0.1127` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 1,670.00 USD | 4,120.00 USD | 22,900.00 USD |
| `7D` | `0.1128` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD | 17,130.00 USD |
| `1D` | `0.1129` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 11,080.00 USD | 1,390.00 USD | 7,770.00 USD |
| `7D` | `0.1130` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,870.00 USD |
| `1D` | `0.1131` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 24,040.00 USD | 6,440.00 USD | 24,260.00 USD |
| `7D` | `0.1132` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 12,540.00 USD | 0.00 USD | 8,170.00 USD |
| `1D` | `0.1133` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 8,350.00 USD | 19,380.00 USD | 24,600.00 USD |
| `7D` | `0.1134` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 14,090.00 USD | 0.00 USD |
| `1D` | `0.1135` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 5,340.00 USD | 3,200.00 USD | 5,390.00 USD |
| `7D` | `0.1136` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD |
| `1D` | `0.1137` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 1,140.00 USD | 356.31 USD |
| `7D` | `0.1138` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD |
| `1D` | `0.1139` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,600.00 USD |
| `7D` | `0.1140` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,600.00 USD |
| `1D` | `0.1141` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 8,110.00 USD | 0.00 USD | 21,310.00 USD |
| `7D` | `0.1142` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1143` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 18,700.00 USD | 22,390.00 USD | 10,490.00 USD |
| `1D` | `0.1144` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 4,680.00 USD | 0.00 USD | 18,190.00 USD |
| `7D` | `0.1144` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 10,360.00 USD | 2,730.00 USD | 143,410.00 USD |
| `7D` | `0.1146` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 16,060.00 USD | 0.00 USD | 188,440.00 USD |
| `7D` | `0.1148` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 63,900.00 USD |
| `7D` | `0.1150` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 18,520.00 USD | 0.00 USD | 89,510.00 USD |
| `7D` | `0.1152` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 165,860.00 USD | 12,610.00 USD | 132,130.00 USD |
| `7D` | `0.1154` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 149,770.00 USD | 18,580.00 USD | 143,090.00 USD |
| `7D` | `0.1156` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 128,780.00 USD | 21,540.00 USD | 74,660.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `64.50M` | Total OI Tokens: `625,037,283.4 OP`
  * 1h OI Change: `+0.75%` | 4h OI Change: `+1.64%` | 24h OI Change: `-12.24%`
  * Exchange Breakdown: Binance=`14.00M` | Bybit=`12.87M` | OKX=`3.97M` | Hyperliquid=`3.14M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-5.25K` | Last 24h: `-4.25K` | Last 3d: `-11.30K` | Last 7d: `-13.94K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0224%` | **USDT OKX** | `-0.0299%` |
| **USDT Bybit** | `-0.0071%` | **USDT KuCoin** | `-0.0119%` |
| **USDT MEXC** | `-0.0225%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `40.88%` | `59.12%` | `0.69` | 1,790,000.00 USD |
| `15M` | `Binance` | `50.5%` | `49.5%` | `1.02` | 510,760.00 USD |
| `15M` | `OKX` | `51.29%` | `48.71%` | `1.05` | 146,420.00 USD |
| `15M` | `Bybit` | `58.2%` | `41.8%` | `1.39` | 199,120.00 USD |
| `15M` | `KuCoin` | `48.13%` | `51.87%` | `0.93` | 147,750.00 USD |
| `15M` | `Gate` | `42.22%` | `57.78%` | `0.73` | 20,410.00 USD |
| `15M` | `Bitget` | `66.94%` | `33.06%` | `2.02` | 13,800.00 USD |
| `15M` | `BingX` | `47.99%` | `52.01%` | `0.92` | 38,520.00 USD |
| `15M` | `MEXC` | `29.36%` | `70.64%` | `0.42` | 12,090.00 USD |
| `15M` | `Bitunix` | `41.74%` | `58.26%` | `0.72` | 32,470.00 USD |
| `15M` | `Hyperliquid` | `65.94%` | `34.06%` | `1.94` | 22,770.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `36.4%` | `63.6%` | `0.57` | 222,190.00 USD |
| `15M` | `Crypto.com` | `100%` | `0%` | `1.00` | 2.81 USD |
| `15M` | `WhiteBIT` | `13.69%` | `86.31%` | `0.16` | 419,470.00 USD |
| `15M` | `HTX` | `64.05%` | `35.95%` | `1.78` | 250.17 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `95.97%` | `4.03%` | `23.81` | 278.40 USD |
| `15M` | `Aster` | `83.44%` | `16.56%` | `5.04` | 169.58 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 5,000.00 USD |
| `15M` | `Whale Positions` | `50.5%` | `49.5%` | `1.02` | 510,760.00 USD |
| `15M` | `Global Accounts` | `40.88%` | `59.12%` | `0.69` | 1,790,000.00 USD |
| `1H` | `OP` | `42.17%` | `57.83%` | `0.73` | 11,440,000.00 USD |
| `1H` | `Binance` | `45.68%` | `54.32%` | `0.84` | 2,520,000.00 USD |
| `1H` | `OKX` | `39.21%` | `60.79%` | `0.65` | 1,080,000.00 USD |
| `1H` | `Bybit` | `47.97%` | `52.03%` | `0.92` | 497,450.00 USD |
| `1H` | `KuCoin` | `34.03%` | `65.97%` | `0.52` | 92,880.00 USD |
| `1H` | `Gate` | `49.77%` | `50.23%` | `0.99` | 948,780.00 USD |
| `1H` | `Bitget` | `38.34%` | `61.66%` | `0.62` | 230,450.00 USD |
| `1H` | `BingX` | `23.21%` | `76.79%` | `0.30` | 3,490,000.00 USD |
| `1H` | `MEXC` | `52.14%` | `47.86%` | `1.09` | 350,140.00 USD |
| `1H` | `Bitunix` | `54.3%` | `45.7%` | `1.19` | 292,970.00 USD |
| `1H` | `Hyperliquid` | `21.39%` | `78.61%` | `0.27` | 41,870.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.58%` | `49.42%` | `1.02` | 219,410.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `96.13%` | `3.87%` | `24.84` | 969,650.00 USD |
| `1H` | `HTX` | `62.43%` | `37.57%` | `1.66` | 22,850.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `42.28%` | `57.72%` | `0.73` | 60,750.00 USD |
| `1H` | `Aster` | `58.1%` | `41.9%` | `1.39` | 3,200.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `28.12%` | `71.88%` | `0.39` | 620,140.00 USD |
| `1H` | `Whale Positions` | `45.68%` | `54.32%` | `0.84` | 2,520,000.00 USD |
| `1H` | `Global Accounts` | `42.17%` | `57.83%` | `0.73` | 11,440,000.00 USD |
| `4H` | `OP` | `46.24%` | `53.76%` | `0.86` | 30,510,000.00 USD |
| `4H` | `Binance` | `43.21%` | `56.79%` | `0.76` | 7,830,000.00 USD |
| `4H` | `OKX` | `44.31%` | `55.69%` | `0.80` | 2,480,000.00 USD |
| `4H` | `Bybit` | `47.79%` | `52.21%` | `0.92` | 2,130,000.00 USD |
| `4H` | `KuCoin` | `49.24%` | `50.76%` | `0.97` | 1,870,000.00 USD |
| `4H` | `Gate` | `39.97%` | `60.03%` | `0.67` | 1,100,000.00 USD |
| `4H` | `Bitget` | `53.37%` | `46.63%` | `1.14` | 698,120.00 USD |
| `4H` | `BingX` | `20.23%` | `79.77%` | `0.25` | 3,450,000.00 USD |
| `4H` | `MEXC` | `50.26%` | `49.74%` | `1.01` | 1,080,000.00 USD |
| `4H` | `Bitunix` | `48.51%` | `51.49%` | `0.94` | 566,070.00 USD |
| `4H` | `Hyperliquid` | `32.29%` | `67.71%` | `0.48` | 463,050.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.89%` | `50.11%` | `1.00` | 6,470,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `93.65%` | `6.35%` | `14.75` | 2,060,000.00 USD |
| `4H` | `HTX` | `39.16%` | `60.84%` | `0.64` | 18,880.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `11.45%` | `88.55%` | `0.13` | 276,490.00 USD |
| `4H` | `Aster` | `30.83%` | `69.17%` | `0.45` | 4,060.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `77.45%` | `22.55%` | `3.43` | 28,350.00 USD |
| `4H` | `Whale Positions` | `43.21%` | `56.79%` | `0.76` | 7,830,000.00 USD |
| `4H` | `Global Accounts` | `46.24%` | `53.76%` | `0.86` | 30,510,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1032` | `0.1029` | `0.1032` | `0.1035` | `0.1022` | 287,615.17 USD | 126,080.17 USD | 161,535.00 USD | -35,454.83 USD | `-12.33%` | `22B / 36S` |
| `5:00 UTC` | `0.1025` | `0.1026` | `0.1025` | `0.1030` | `0.1024` | 241,478.30 USD | 150,665.97 USD | 90,812.34 USD | 59,853.63 USD | `+24.79%` | `12B / 6S` |
| `0:00 UTC` | `0.1024` | `0.1027` | `0.1024` | `0.1036` | `0.1023` | 359,716.26 USD | 217,752.22 USD | 141,964.04 USD | 75,788.18 USD | `+21.07%` | `25B / 11S` |
| `5:00 UTC` | `0.1033` | `0.1034` | `0.1033` | `0.1038` | `0.1032` | 260,043.89 USD | 128,207.87 USD | 131,836.02 USD | -3,628.15 USD | `-1.40%` | `11B / 2S` |
| `0:00 UTC` | `0.1024` | `0.1027` | `0.1024` | `0.1032` | `0.1023` | 294,713.35 USD | 140,222.38 USD | 154,490.97 USD | -14,268.58 USD | `-4.84%` | `9B / 14S` |
| `5:00 UTC` | `0.1024` | `0.1025` | `0.1024` | `0.1030` | `0.1023` | 189,660.77 USD | 110,909.31 USD | 78,751.47 USD | 32,157.84 USD | `+16.96%` | `13B / 15S` |
| `0:00 UTC` | `0.1021` | `0.1022` | `0.1021` | `0.1027` | `0.1019` | 366,904.35 USD | 146,868.15 USD | 220,036.20 USD | -73,168.05 USD | `-19.94%` | `9B / 16S` |
| `5:00 UTC` | `0.1020` | `0.1021` | `0.1020` | `0.1024` | `0.1019` | 314,873.64 USD | 167,532.45 USD | 147,341.19 USD | 20,191.27 USD | `+6.41%` | `10B / 2S` |
| `0:00 UTC` | `0.1019` | `0.1024` | `0.1019` | `0.1029` | `0.1019` | 191,273.46 USD | 92,786.86 USD | 98,486.60 USD | -5,699.74 USD | `-2.98%` | `22B / 16S` |
| `5:00 UTC` | `0.1028` | `0.1028` | `0.1028` | `0.1033` | `0.1023` | 193,218.77 USD | 110,864.10 USD | 82,354.67 USD | 28,509.43 USD | `+14.76%` | `21B / 23S` |

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
| `5m` | 4,300.00 USD | 18,530.00 USD | **`ACCUMULATION`** |
| `15m` | 10,600.00 USD | 68,070.00 USD | **`ACCUMULATION`** |
| `30m` | 4,800.00 USD | 68,500.00 USD | **`ACCUMULATION`** |
| `1h` | -30,010.00 USD | 11,620.00 USD | **`DISTRIBUTION`** |
| `2h` | 2,800.00 USD | 827.85 USD | **`ACCUMULATION`** |
| `4h` | 25,360.00 USD | 31,460.00 USD | **`ACCUMULATION`** |
| `6h` | 144,960.00 USD | 692,840.00 USD | **`ACCUMULATION`** |
| `8h` | -106,550.00 USD | 504,030.00 USD | **`ACCUMULATION`** |
| `12h` | 160,110.00 USD | -1,360,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 232,070.00 USD | -3,830,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -295,350.00 USD | -12,640,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,840,000.00 USD | -83,130,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+4.30K` | 15m=`+10.60K` | 1h=`-30.01K` | 24h=`+232.07K`
* Futures Capital Netflows: 5m=`+18.53K` | 15m=`+68.07K` | 1h=`+11.62K` | 24h=`-3.83M`
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
  * `2026-10-30 15:18:36 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:36 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:36 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:37:36 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:36 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:32:36 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)


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
