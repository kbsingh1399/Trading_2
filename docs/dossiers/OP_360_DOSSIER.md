# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 02:39:45 IST` (`2026-10-29 21:09:45 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1017` | `0.1019` | `0.1008` | `0.1012` | `6,922,501` | 702,263.47 USD | -48,889.62 USD | `-6.96%` | -2,712,450.44 USD | `+0.15` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.1012` | `0.1024` | `0.1007` | `0.1014` | `8,756,092` | 889,491.46 USD | 38,684.39 USD | `+4.35%` | -2,673,766.05 USD | `+0.61` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.1014` | `0.1016` | `0.1012` | `0.1015` | `919,363` | 93,238.83 USD | 9,564.72 USD | `+10.26%` | -2,664,201.32 USD | `+0.45` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1082` | `0.1088` | `0.1013` | `0.1025` | `52,998,820` | 5,548,996.22 USD | -1,004,076.47 USD | `-18.09%` | -2,369,190.51 USD | `-3.98` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1024` | `0.1029` | `0.0989` | `0.1012` | `56,419,228` | 5,717,098.88 USD | -371,390.75 USD | `-6.50%` | -2,740,581.26 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1012` | `0.1024` | `0.1007` | `0.1015` | `9,675,455` | 982,730.29 USD | 48,249.11 USD | `+4.91%` | -2,692,332.15 USD | `+0.58` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1100` | `0.1106` | `0.1096` | `0.1101` | `7,910,873` | 870,770.93 USD | 117,397.34 USD | `+13.48%` | -1,177,554.63 USD | `+0.73` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `136,699,709` | 14,218,772.66 USD | -1,614,985.67 USD | `-11.36%` | -2,792,540.30 USD | `-3.57` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1012` | `0.1024` | `0.1007` | `0.1015` | `9,316,195` | 946,273.01 USD | 52,878.09 USD | `+5.59%` | -2,739,662.21 USD | `+0.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -935,828.18 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | -1,111,968.46 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1014` | `145,894,911` | 15,152,761.24 USD | -1,560,581.03 USD | `-10.30%` | -2,672,549.49 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1085` | `0.1106` | `0.1071` | `0.1076` | `47,048,931` | 5,111,570.05 USD | 108,567.99 USD | `+2.12%` | -1,419,806.61 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,277,083.78 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -935,828.18 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | -1,111,968.46 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1014` | `145,894,911` | 15,152,761.24 USD | -1,560,581.03 USD | `-10.30%` | -2,672,549.49 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:35:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1122` | 6,295.13 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale BUY: 6.30K USD at 0.1122 USD [API] | `2026-10-28 07:11:36` |
| `ANNOUNCEMENT` | `INFO` | `0.1122` | 5,560.99 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale BUY: 5.56K USD at 0.1122 USD [API] | `2026-10-28 07:11:36` |
| `ANNOUNCEMENT` | `INFO` | `0.1125` | 10,180.05 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 10.18K USD at 0.1125 USD [API] | `2026-10-28 08:39:49` |
| `ANNOUNCEMENT` | `INFO` | `0.1124` | 10,171.00 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 10.17K USD at 0.1124 USD [API] | `2026-10-28 09:34:54` |
| `ANNOUNCEMENT` | `INFO` | `0.1124` | 10,000.00 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 10.00K USD at 0.1124 USD [API] | `2026-10-28 09:37:11` |
| `ANNOUNCEMENT` | `INFO` | `0.1124` | 10,000.89 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 10.00K USD at 0.1124 USD [API] | `2026-10-28 11:06:21` |
| `ANNOUNCEMENT` | `INFO` | `0.1124` | 5,048.00 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 5.05K USD at 0.1124 USD [API] | `2026-10-28 11:24:37` |


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
| `Live` | `Long Liquidation` | `0.0395` | 416.18 USD | 242,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 3,450.00 USD | 242,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 262.59 USD | 239,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 3,460.00 USD | 238,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 829.69 USD | 235,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 1,100.00 USD | 234,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 353.81 USD | 233,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 509.64 USD | 233,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 518.48 USD | 232,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 1,920.00 USD | 232,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 25,370.00 USD | 230,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 4,380.00 USD | 204,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 44,410.00 USD | 200,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 1,020.00 USD | 155,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 1,280.00 USD | 154,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 1,730.00 USD | 153,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 1,320.00 USD | 151,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 223.98 USD | 150,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 1,560.00 USD | 150,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 2,380.00 USD | 148,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0878` | 872,720.00 USD | 872,720.00 USD | 1,370.00 USD | 4,930.00 USD | 27,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0881` | 507,660.00 USD | 507,660.00 USD | 2,400.00 USD | 1,300.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0881` | 839,160.00 USD | 839,160.00 USD | 3,770.00 USD | 2,660.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0883` | 499,260.00 USD | 499,260.00 USD | 2,370.00 USD | 659.34 USD | 5,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0884` | 819,790.00 USD | 819,790.00 USD | 7,040.00 USD | 4,640.00 USD | 11,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0885` | 490,250.00 USD | 490,250.00 USD | 0.00 USD | 312.16 USD | 2,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0887` | 487,420.00 USD | 487,420.00 USD | 1,740.00 USD | 655.48 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0887` | 796,240.00 USD | 796,240.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0889` | 480,500.00 USD | 480,500.00 USD | 727.20 USD | 1,690.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0890` | 762,100.00 USD | 762,100.00 USD | 14,610.00 USD | 4,470.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0891` | 475,970.00 USD | 475,970.00 USD | 1,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0893` | 474,650.00 USD | 474,650.00 USD | 983.61 USD | 0.00 USD | 542.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0893` | 739,350.00 USD | 739,350.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0895` | 473,120.00 USD | 473,120.00 USD | 0.00 USD | 215.06 USD | 394.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,120.00 USD | 146,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0896` | 720,180.00 USD | 720,180.00 USD | 5,760.00 USD | 611.80 USD | 6,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0897` | 472,510.00 USD | 472,510.00 USD | 0.00 USD | 772.87 USD | 0.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0899` | 471,740.00 USD | 471,740.00 USD | 0.00 USD | 287.77 USD | 601.21 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0899` | 706,930.00 USD | 706,930.00 USD | 3,390.00 USD | 927.82 USD | 4,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0901` | 470,850.00 USD | 470,850.00 USD | 2,450.00 USD | 0.00 USD | 293.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0902` | 698,130.00 USD | 698,130.00 USD | 2,270.00 USD | 910.78 USD | 1,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0903` | 468,100.00 USD | 468,100.00 USD | 831.11 USD | 2,190.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0905` | 464,020.00 USD | 464,020.00 USD | 413.91 USD | 998.41 USD | 2,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0905` | 693,730.00 USD | 693,730.00 USD | 10,350.00 USD | 996.61 USD | 4,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0905` | 443.16 USD | 143,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0907` | 459,770.00 USD | 459,770.00 USD | 2,290.00 USD | 909.44 USD | 974.67 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0908` | 678,310.00 USD | 678,310.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0909` | 455,590.00 USD | 455,590.00 USD | 938.76 USD | 957.38 USD | 785.45 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0911` | 452,910.00 USD | 452,910.00 USD | 5,580.00 USD | 778.50 USD | 10.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0911` | 666,910.00 USD | 666,910.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0913` | 446,540.00 USD | 446,540.00 USD | 0.00 USD | 468.08 USD | 796.07 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0914` | 663,630.00 USD | 663,630.00 USD | 1,670.00 USD | 903.90 USD | 45.81 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0915` | 445,280.00 USD | 445,280.00 USD | 6,590.00 USD | 0.00 USD | 52.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0917` | 438,640.00 USD | 438,640.00 USD | 2,550.00 USD | 0.00 USD | 2.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0917` | 661,010.00 USD | 661,010.00 USD | 0.00 USD | 0.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0919` | 436,080.00 USD | 436,080.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0923` | 432,390.00 USD | 432,390.00 USD | 0.00 USD | 0.00 USD | 42.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0923` | 659,270.00 USD | 659,270.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0925` | 432,350.00 USD | 432,350.00 USD | 3,270.00 USD | 1,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0925` | 16,670.00 USD | 142,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0926` | 657,810.00 USD | 657,810.00 USD | 1,790.00 USD | 0.00 USD | 6.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0932` | 656,010.00 USD | 656,010.00 USD | 0.00 USD | 0.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0935` | 652,830.00 USD | 652,830.00 USD | 0.00 USD | 1,320.00 USD | 6,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0938` | 645,020.00 USD | 645,020.00 USD | 0.00 USD | 0.00 USD | 8.57 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0939` | 427,430.00 USD | 427,430.00 USD | 0.00 USD | 0.00 USD | 76.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0941` | 645,010.00 USD | 645,010.00 USD | 2,050.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0944` | 639,940.00 USD | 639,940.00 USD | 1,870.00 USD | 0.00 USD | 7,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0945` | 69,120.00 USD | 126,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0947` | 427,350.00 USD | 427,350.00 USD | 0.00 USD | 0.00 USD | 69.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0947` | 630,540.00 USD | 630,540.00 USD | 3,790.00 USD | 1,810.00 USD | 22.82 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0950` | 624,920.00 USD | 624,920.00 USD | 3,770.00 USD | 0.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0953` | 614,480.00 USD | 614,480.00 USD | 0.00 USD | 0.00 USD | 4.65 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0955` | 427,280.00 USD | 427,280.00 USD | 0.00 USD | 1,180.00 USD | 166.88 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0955` | 5,610.00 USD | 57,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0959` | 614,480.00 USD | 614,480.00 USD | 0.00 USD | 1,140.00 USD | 115.48 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0961` | 425,930.00 USD | 425,930.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0962` | 613,230.00 USD | 613,230.00 USD | 0.00 USD | 0.00 USD | 2.60 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0963` | 423,850.00 USD | 423,850.00 USD | 0.00 USD | 0.00 USD | 1.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0965` | 423,850.00 USD | 423,850.00 USD | 1,280.00 USD | 282.32 USD | 1,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0965` | 613,220.00 USD | 613,220.00 USD | 0.00 USD | 0.00 USD | 1,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0965` | 419.87 USD | 51,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0967` | 420,410.00 USD | 420,410.00 USD | 2,660.00 USD | 1,100.00 USD | 7,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0968` | 612,010.00 USD | 612,010.00 USD | 7,490.00 USD | 3,720.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0969` | 409,150.00 USD | 409,150.00 USD | 4,590.00 USD | 2,640.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0971` | 392,910.00 USD | 392,910.00 USD | 16,100.00 USD | 3,330.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 589,260.00 USD | 589,260.00 USD | 0.00 USD | 3,760.00 USD | 9,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0973` | 369,080.00 USD | 369,080.00 USD | 0.00 USD | 2,120.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0974` | 575,780.00 USD | 575,780.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0975` | 362,560.00 USD | 362,560.00 USD | 0.00 USD | 1,810.00 USD | 5,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0975` | 12,670.00 USD | 51,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0977` | 355,200.00 USD | 355,200.00 USD | 24,760.00 USD | 2,510.00 USD | 11,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0977` | 571,500.00 USD | 571,500.00 USD | 0.00 USD | 1,160.00 USD | 13,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0979` | 316,700.00 USD | 316,700.00 USD | 12,620.00 USD | 1,040.00 USD | 8.08 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0980` | 557,210.00 USD | 557,210.00 USD | 0.00 USD | 3,920.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0981` | 303,030.00 USD | 303,030.00 USD | 9,220.00 USD | 431.42 USD | 3,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0983` | 290,350.00 USD | 290,350.00 USD | 3,250.00 USD | 1,390.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 547,590.00 USD | 547,590.00 USD | 7,990.00 USD | 1,230.00 USD | 14,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0985` | 269,600.00 USD | 269,600.00 USD | 5,670.00 USD | 413.94 USD | 2,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0985` | 19,960.00 USD | 38,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0986` | 523,590.00 USD | 523,590.00 USD | 7,110.00 USD | 7,530.00 USD | 38,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0987` | 260,830.00 USD | 260,830.00 USD | 15,960.00 USD | 6,330.00 USD | 4,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0989` | 233,730.00 USD | 233,730.00 USD | 2,820.00 USD | 3,290.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 470,790.00 USD | 470,790.00 USD | 17,640.00 USD | 6,190.00 USD | 32,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0991` | 225,440.00 USD | 225,440.00 USD | 32,710.00 USD | 2,950.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0992` | 414,200.00 USD | 414,200.00 USD | 27,140.00 USD | 11,490.00 USD | 28,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0993` | 186,580.00 USD | 186,580.00 USD | 3,080.00 USD | 1,720.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0995` | 170,310.00 USD | 170,310.00 USD | 2,740.00 USD | 624.33 USD | 11,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 347,070.00 USD | 347,070.00 USD | 24,220.00 USD | 15,150.00 USD | 34,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0997` | 155,460.00 USD | 155,460.00 USD | 35,260.00 USD | 718.82 USD | 10,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0998` | 273,650.00 USD | 273,650.00 USD | 28,450.00 USD | 6,400.00 USD | 49,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0999` | 109,440.00 USD | 109,440.00 USD | 29,920.00 USD | 2,940.00 USD | 16,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1001` | 59,790.00 USD | 59,790.00 USD | 21,100.00 USD | 1,410.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 189,430.00 USD | 189,430.00 USD | 36,110.00 USD | 8,650.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1003` | 33,090.00 USD | 33,090.00 USD | 0.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1004` | 131,540.00 USD | 131,540.00 USD | 22,470.00 USD | 16,470.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1005` | 32,530.00 USD | 32,530.00 USD | 1,970.00 USD | 403.62 USD | 13,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1005` | 427.25 USD | 18,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1007` | 16,210.00 USD | 16,210.00 USD | 0.00 USD | 8,710.00 USD | 789.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 69,170.00 USD | 69,170.00 USD | 20,870.00 USD | 3,870.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1009` | 6,720.00 USD | 6,720.00 USD | 0.00 USD | 2,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1010` | 30,560.00 USD | 30,560.00 USD | 17,340.00 USD | 6,580.00 USD | 6,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1011` | 3,970.00 USD | 3,970.00 USD | 0.00 USD | 575.54 USD | 3,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1013` | 1,390.00 USD | 1,390.00 USD | 0.00 USD | 800.79 USD | 587.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1013` | 31,990.00 USD | 31,990.00 USD | 15,270.00 USD | 5,230.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1013` | 63,970.00 USD | 63,970.00 USD | 15,270.00 USD | 5,230.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1015` | 4,880.00 USD | 4,880.00 USD | 0.00 USD | 1,830.00 USD | 1,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1015` | 622.37 USD | 17,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1016` | 90,420.00 USD | 90,420.00 USD | 15,440.00 USD | 5,490.00 USD | 5,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1017` | 8,320.00 USD | 8,320.00 USD | 0.00 USD | 3,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1019` | 14,700.00 USD | 14,700.00 USD | 0.00 USD | 6,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1019` | 122,580.00 USD | 122,580.00 USD | 12,100.00 USD | 5,790.00 USD | 14,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1021` | 16,020.00 USD | 16,020.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1022` | 155,770.00 USD | 155,770.00 USD | 11,930.00 USD | 8,250.00 USD | 13,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1025` | 171,690.00 USD | 171,690.00 USD | 1,550.00 USD | 0.00 USD | 14,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1025` | 17,360.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1028` | 180,460.00 USD | 180,460.00 USD | 3,800.00 USD | 4,390.00 USD | 581.37 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1029` | 22,250.00 USD | 22,250.00 USD | 0.00 USD | 0.00 USD | 6,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1031` | 69,050.00 USD | 69,050.00 USD | 27,910.00 USD | 0.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1031` | 217,080.00 USD | 217,080.00 USD | 19,560.00 USD | 6,260.00 USD | 10,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1033` | 90,910.00 USD | 90,910.00 USD | 0.00 USD | 0.00 USD | 21,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1034` | 281,860.00 USD | 281,860.00 USD | 18,920.00 USD | 7,030.00 USD | 38,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1035` | 112,980.00 USD | 112,980.00 USD | 4,780.00 USD | 4,880.00 USD | 12,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1037` | 171,520.00 USD | 171,520.00 USD | 37,310.00 USD | 11,960.00 USD | 9,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1037` | 324,060.00 USD | 324,060.00 USD | 2,710.00 USD | 5,010.00 USD | 34,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1039` | 234,280.00 USD | 234,280.00 USD | 32,370.00 USD | 5,450.00 USD | 24,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1040` | 351,040.00 USD | 351,040.00 USD | 5,940.00 USD | 10,300.00 USD | 10,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1041` | 290,690.00 USD | 290,690.00 USD | 24,950.00 USD | 12,830.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1043` | 323,400.00 USD | 323,400.00 USD | 19,210.00 USD | 5,650.00 USD | 7,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1043` | 402,200.00 USD | 402,200.00 USD | 15,960.00 USD | 5,980.00 USD | 29,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1045` | 351,550.00 USD | 351,550.00 USD | 4,220.00 USD | 4,840.00 USD | 19,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1046` | 441,850.00 USD | 441,850.00 USD | 0.00 USD | 9,810.00 USD | 29,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1047` | 390,580.00 USD | 390,580.00 USD | 15,000.00 USD | 3,400.00 USD | 20,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1049` | 449,510.00 USD | 449,510.00 USD | 37,390.00 USD | 10,710.00 USD | 10,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1049` | 526,380.00 USD | 526,380.00 USD | 34,790.00 USD | 6,530.00 USD | 43,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1051` | 512,890.00 USD | 512,890.00 USD | 30,370.00 USD | 8,750.00 USD | 24,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1052` | 704,950.00 USD | 704,950.00 USD | 28,200.00 USD | 24,160.00 USD | 126,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1053` | 607,700.00 USD | 607,700.00 USD | 35,030.00 USD | 8,930.00 USD | 50,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1055` | 736,510.00 USD | 736,510.00 USD | 43,960.00 USD | 25,140.00 USD | 59,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1055` | 1,040,000.00 USD | 1,040,000.00 USD | 122,840.00 USD | 44,430.00 USD | 166,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1057` | 829,060.00 USD | 829,060.00 USD | 27,300.00 USD | 15,170.00 USD | 50,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1058` | 1,390,000.00 USD | 1,390,000.00 USD | 105,620.00 USD | 53,680.00 USD | 189,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1059` | 930,730.00 USD | 930,730.00 USD | 39,020.00 USD | 0.00 USD | 62,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1061` | 1,020,000.00 USD | 1,020,000.00 USD | 26,970.00 USD | 0.00 USD | 58,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1061` | 1,640,000.00 USD | 1,640,000.00 USD | 75,540.00 USD | 72,260.00 USD | 102,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1063` | 1,070,000.00 USD | 1,070,000.00 USD | 9,220.00 USD | 0.00 USD | 48,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1064` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 52,580.00 USD | 192,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1065` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 25,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1067` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 33,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1067` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 51,740.00 USD | 133,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1069` | 1,190,000.00 USD | 1,190,000.00 USD | 8,170.00 USD | 4,140.00 USD | 42,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1070` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 57,770.00 USD | 114,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1071` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 3,140.00 USD | 16,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1073` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 100.67 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1073` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 17,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1075` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 104.34 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1077` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 93.46 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1079` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 26.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1079` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 79.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1083` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 5,910.00 USD | 91.27 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1085` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 65,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1085` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1087` | 1,350,000.00 USD | 1,350,000.00 USD | 28,490.00 USD | 2,240.00 USD | 44,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1088` | 2,260,000.00 USD | 2,260,000.00 USD | 5,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1089` | 1,390,000.00 USD | 1,390,000.00 USD | 39,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1091` | 1,430,000.00 USD | 1,430,000.00 USD | 33,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1091` | 2,290,000.00 USD | 2,290,000.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1093` | 1,440,000.00 USD | 1,440,000.00 USD | 15,480.00 USD | 0.00 USD | 64.27 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1094` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1095` | 1,470,000.00 USD | 1,470,000.00 USD | 4,110.00 USD | 1,890.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1097` | 1,500,000.00 USD | 1,500,000.00 USD | 7,260.00 USD | 1,970.00 USD | 22,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1097` | 2,320,000.00 USD | 2,320,000.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1099` | 1,510,000.00 USD | 1,510,000.00 USD | 6,130.00 USD | 1,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1100` | 2,350,000.00 USD | 2,350,000.00 USD | 11,470.00 USD | 0.00 USD | 21,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1101` | 1,520,000.00 USD | 1,520,000.00 USD | 4,310.00 USD | 2,820.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1103` | 1,530,000.00 USD | 1,530,000.00 USD | 3,540.00 USD | 5,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 2,390,000.00 USD | 2,390,000.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1105` | 1,550,000.00 USD | 1,550,000.00 USD | 3,380.00 USD | 4,740.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1106` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 22,880.00 USD | 15,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1107` | 1,600,000.00 USD | 1,600,000.00 USD | 3,110.00 USD | 12,720.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1109` | 1,600,000.00 USD | 1,600,000.00 USD | 2,110.00 USD | 1,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1111` | 1,610,000.00 USD | 1,610,000.00 USD | 5,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1112` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1113` | 1,680,000.00 USD | 1,680,000.00 USD | 21,390.00 USD | 5,210.00 USD | 39,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1115` | 1,680,000.00 USD | 1,680,000.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1117` | 1,740,000.00 USD | 1,740,000.00 USD | 2,060.00 USD | 25,630.00 USD | 34,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1118` | 2,540,000.00 USD | 2,540,000.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1119` | 1,820,000.00 USD | 1,820,000.00 USD | 36,940.00 USD | 6,980.00 USD | 36,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1121` | 1,870,000.00 USD | 1,870,000.00 USD | 20,000.00 USD | 12,060.00 USD | 12,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 2,590,000.00 USD | 2,590,000.00 USD | 17,760.00 USD | 0.00 USD | 32,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1123` | 1,920,000.00 USD | 1,920,000.00 USD | 40,400.00 USD | 1,780.00 USD | 5,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1124` | 2,690,000.00 USD | 2,690,000.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1125` | 1,950,000.00 USD | 1,950,000.00 USD | 11,130.00 USD | 13,240.00 USD | 7,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1127` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 1,250.00 USD | 19,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1127` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1129` | 1,980,000.00 USD | 1,980,000.00 USD | 8,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1130` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 15,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1131` | 2,020,000.00 USD | 2,020,000.00 USD | 20,830.00 USD | 8,010.00 USD | 11,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1133` | 2,070,000.00 USD | 2,070,000.00 USD | 6,530.00 USD | 22,520.00 USD | 23,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 2,750,000.00 USD | 2,750,000.00 USD | 12,540.00 USD | 11,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1135` | 2,080,000.00 USD | 2,080,000.00 USD | 4,040.00 USD | 3,670.00 USD | 4,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1136` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1137` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 856.93 USD | 40.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1139` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 14,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1141` | 2,130,000.00 USD | 2,130,000.00 USD | 13,860.00 USD | 2,800.00 USD | 13,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1142` | 2,780,000.00 USD | 2,780,000.00 USD | 10,380.00 USD | 0.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1143` | 2,190,000.00 USD | 2,190,000.00 USD | 20,300.00 USD | 27,990.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1145` | 2,250,000.00 USD | 2,250,000.00 USD | 13,430.00 USD | 11,690.00 USD | 38,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 3,020,000.00 USD | 3,020,000.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1147` | 2,300,000.00 USD | 2,300,000.00 USD | 10,640.00 USD | 10,080.00 USD | 30,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1148` | 3,200,000.00 USD | 3,200,000.00 USD | 9,880.00 USD | 0.00 USD | 176,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1149` | 2,370,000.00 USD | 2,370,000.00 USD | 35,170.00 USD | 624.71 USD | 31,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1151` | 2,430,000.00 USD | 2,430,000.00 USD | 16,450.00 USD | 14,620.00 USD | 33,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 3,470,000.00 USD | 3,470,000.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1153` | 2,550,000.00 USD | 2,550,000.00 USD | 31,350.00 USD | 23,630.00 USD | 59,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1154` | 3,940,000.00 USD | 3,940,000.00 USD | 243,190.00 USD | 26,970.00 USD | 195,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1155` | 2,670,000.00 USD | 2,670,000.00 USD | 38,430.00 USD | 27,080.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1157` | 2,720,000.00 USD | 2,720,000.00 USD | 33,550.00 USD | 9,850.00 USD | 7,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 4,250,000.00 USD | 4,250,000.00 USD | 188,950.00 USD | 25,290.00 USD | 98,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1159` | 2,770,000.00 USD | 2,770,000.00 USD | 22,990.00 USD | 12,000.00 USD | 17,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1160` | 4,530,000.00 USD | 4,530,000.00 USD | 139,350.00 USD | 32,830.00 USD | 109,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1161` | 2,800,000.00 USD | 2,800,000.00 USD | 23,670.00 USD | 0.00 USD | 5,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1163` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 9,380.00 USD | 17,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 4,820,000.00 USD | 4,820,000.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1165` | 2,850,000.00 USD | 2,850,000.00 USD | 8,820.00 USD | 11,680.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1166` | 5,040,000.00 USD | 5,040,000.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1167` | 2,870,000.00 USD | 2,870,000.00 USD | 5,680.00 USD | 7,220.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1169` | 2,890,000.00 USD | 2,890,000.00 USD | 5,480.00 USD | 2,440.00 USD | 5,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 5,260,000.00 USD | 5,260,000.00 USD | 82,770.00 USD | 26,150.00 USD | 112,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1171` | 2,910,000.00 USD | 2,910,000.00 USD | 13,800.00 USD | 0.00 USD | 4,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1172` | 5,390,000.00 USD | 5,390,000.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1173` | 2,920,000.00 USD | 2,920,000.00 USD | 9,320.00 USD | 5,440.00 USD | 4,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1175` | 2,960,000.00 USD | 2,960,000.00 USD | 9,530.00 USD | 9,020.00 USD | 19,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 5,560,000.00 USD | 5,560,000.00 USD | 72,770.00 USD | 17,930.00 USD | 81,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1177` | 3,000,000.00 USD | 3,000,000.00 USD | 14,360.00 USD | 8,560.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1178` | 5,730,000.00 USD | 5,730,000.00 USD | 89,510.00 USD | 23,660.00 USD | 55,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1179` | 3,020,000.00 USD | 3,020,000.00 USD | 10,640.00 USD | 4,760.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1181` | 3,060,000.00 USD | 3,060,000.00 USD | 14,160.00 USD | 6,410.00 USD | 15,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 5,810,000.00 USD | 5,810,000.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1183` | 3,070,000.00 USD | 3,070,000.00 USD | 8,760.00 USD | 677.63 USD | 4,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1184` | 5,880,000.00 USD | 5,880,000.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1185` | 3,090,000.00 USD | 3,090,000.00 USD | 4,390.00 USD | 5,850.00 USD | 6,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1187` | 3,110,000.00 USD | 3,110,000.00 USD | 4,060.00 USD | 6,500.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 5,960,000.00 USD | 5,960,000.00 USD | 5,620.00 USD | 17,120.00 USD | 54,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1189` | 3,120,000.00 USD | 3,120,000.00 USD | 2,840.00 USD | 2,120.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1190` | 6,100,000.00 USD | 6,100,000.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1191` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 1,810.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1193` | 3,140,000.00 USD | 3,140,000.00 USD | 4,720.00 USD | 1,040.00 USD | 3,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 6,180,000.00 USD | 6,180,000.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1195` | 3,150,000.00 USD | 3,150,000.00 USD | 9,550.00 USD | 1,470.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1196` | 6,240,000.00 USD | 6,240,000.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1197` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 1,040.00 USD | 93.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1199` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 431.42 USD | 3,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 6,330,000.00 USD | 6,330,000.00 USD | 9,100.00 USD | 13,190.00 USD | 67,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1201` | 3,170,000.00 USD | 3,170,000.00 USD | 3,250.00 USD | 1,390.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1202` | 6,530,000.00 USD | 6,530,000.00 USD | 138,430.00 USD | 21,430.00 USD | 32,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1203` | 3,180,000.00 USD | 3,180,000.00 USD | 5,670.00 USD | 413.94 USD | 2,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1205` | 3,190,000.00 USD | 3,190,000.00 USD | 2,250.00 USD | 1,670.00 USD | 741.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 6,860,000.00 USD | 6,860,000.00 USD | 132,960.00 USD | 72,910.00 USD | 130,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1207` | 3,200,000.00 USD | 3,200,000.00 USD | 5,540.00 USD | 524.23 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1208` | 6,990,000.00 USD | 6,990,000.00 USD | 39,480.00 USD | 25,720.00 USD | 66,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1209` | 3,200,000.00 USD | 3,200,000.00 USD | 2,820.00 USD | 3,290.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1211` | 3,220,000.00 USD | 3,220,000.00 USD | 4,800.00 USD | 2,950.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 7,200,000.00 USD | 7,200,000.00 USD | 72,500.00 USD | 25,920.00 USD | 111,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1213` | 3,230,000.00 USD | 3,230,000.00 USD | 5,870.00 USD | 1,720.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1214` | 7,320,000.00 USD | 7,320,000.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1215` | 3,240,000.00 USD | 3,240,000.00 USD | 1,650.00 USD | 0.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1217` | 3,250,000.00 USD | 3,250,000.00 USD | 1,090.00 USD | 624.33 USD | 6,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 7,370,000.00 USD | 7,370,000.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1219` | 3,260,000.00 USD | 3,260,000.00 USD | 2,320.00 USD | 718.82 USD | 10,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1220` | 7,480,000.00 USD | 7,480,000.00 USD | 45,700.00 USD | 10,970.00 USD | 54,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1221` | 3,280,000.00 USD | 3,280,000.00 USD | 7,970.00 USD | 2,940.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1223` | 3,290,000.00 USD | 3,290,000.00 USD | 2,660.00 USD | 1,410.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 7,650,000.00 USD | 7,650,000.00 USD | 76,930.00 USD | 36,110.00 USD | 50,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1225` | 3,290,000.00 USD | 3,290,000.00 USD | 1,840.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 16,560.00 USD | 16,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1226` | 7,740,000.00 USD | 7,740,000.00 USD | 54,940.00 USD | 32,070.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1227` | 3,290,000.00 USD | 3,290,000.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1229` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 403.62 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 7,960,000.00 USD | 7,960,000.00 USD | 91,580.00 USD | 42,230.00 USD | 91,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1230` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 789.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1232` | 8,140,000.00 USD | 8,140,000.00 USD | 67,800.00 USD | 41,730.00 USD | 63,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1235` | 8,170,000.00 USD | 8,170,000.00 USD | 15,040.00 USD | 5,390.00 USD | 13,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1238` | 8,190,000.00 USD | 8,190,000.00 USD | 8,310.00 USD | 3,610.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1241` | 8,200,000.00 USD | 8,200,000.00 USD | 11,380.00 USD | 1,380.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1244` | 8,250,000.00 USD | 8,250,000.00 USD | 26,540.00 USD | 8,130.00 USD | 9,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1247` | 8,290,000.00 USD | 8,290,000.00 USD | 7,900.00 USD | 18,280.00 USD | 17,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1250` | 8,310,000.00 USD | 8,310,000.00 USD | 8,540.00 USD | 7,270.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1253` | 8,350,000.00 USD | 8,350,000.00 USD | 11,420.00 USD | 2,100.00 USD | 22,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1256` | 8,380,000.00 USD | 8,380,000.00 USD | 11,990.00 USD | 18,000.00 USD | 220.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1259` | 8,380,000.00 USD | 8,380,000.00 USD | 5,870.00 USD | 1,190.00 USD | 151.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1262` | 8,390,000.00 USD | 8,390,000.00 USD | 4,270.00 USD | 0.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1265` | 8,400,000.00 USD | 8,400,000.00 USD | 2,710.00 USD | 0.00 USD | 7,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1268` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1271` | 8,410,000.00 USD | 8,410,000.00 USD | 5,940.00 USD | 0.00 USD | 30.15 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1274` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 0.00 USD | 12.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1277` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 0.00 USD | 31.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1280` | 8,420,000.00 USD | 8,420,000.00 USD | 0.00 USD | 0.00 USD | 6,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1355` | 1,330.00 USD | 17,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1505` | 15,050.00 USD | 32,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1555` | 6,210.00 USD | 39,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1565` | 550.61 USD | 39,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1615` | 21,050.00 USD | 60,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1695` | 169.25 USD | 60,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1865` | 272.66 USD | 61,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1935` | 935.32 USD | 62,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0375` | 199,310.00 USD | 0.00 USD | 225.00 USD | `-62.92%` | `6,000.00` |
| `Live` | `Long` | `0.0475` | 199,090.00 USD | 0.00 USD | 2,650.00 USD | `-53.03%` | `55,786.40` |
| `Live` | `Long` | `0.0495` | 196,440.00 USD | 0.00 USD | 223.67 USD | `-51.05%` | `4,518.50` |
| `Live` | `Long` | `0.0575` | 196,210.00 USD | 0.00 USD | 829.69 USD | `-43.14%` | `14,429.40` |
| `Live` | `Long` | `0.0595` | 195,380.00 USD | 0.00 USD | 4,150.00 USD | `-41.16%` | `69,790.10` |
| `Live` | `Long` | `0.0615` | 191,230.00 USD | 0.00 USD | 1,100.00 USD | `-39.19%` | `17,943.80` |
| `Live` | `Long` | `0.0635` | 190,130.00 USD | 0.00 USD | 486.65 USD | `-37.21%` | `7,663.80` |
| `Live` | `Long` | `0.0645` | 189,640.00 USD | 0.00 USD | 353.81 USD | `-36.22%` | `5,485.40` |
| `Live` | `Long` | `0.0655` | 189,290.00 USD | 0.00 USD | 333.98 USD | `-35.23%` | `5,098.90` |
| `Live` | `Long` | `0.0675` | 188,950.00 USD | 0.00 USD | 518.48 USD | `-33.25%` | `7,681.20` |
| `Live` | `Long` | `0.0685` | 188,440.00 USD | 0.00 USD | 1,920.00 USD | `-32.27%` | `28,000.00` |
| `Live` | `Long` | `0.0725` | 186,520.00 USD | 0.00 USD | 23,910.00 USD | `-28.31%` | `329,855.60` |
| `Live` | `Long` | `0.0745` | 162,600.00 USD | 0.00 USD | 2,300.00 USD | `-26.33%` | `30,851.90` |
| `Live` | `Long` | `0.0755` | 160,300.00 USD | 0.00 USD | 1,020.00 USD | `-25.34%` | `13,481.90` |
| `Live` | `Long` | `0.0765` | 159,290.00 USD | 0.00 USD | 2,710.00 USD | `-24.35%` | `35,396.30` |
| `Live` | `Long` | `0.0775` | 156,580.00 USD | 0.00 USD | 44,690.00 USD | `-23.37%` | `576,624.50` |
| `Live` | `Long` | `0.0795` | 111,890.00 USD | 0.00 USD | 1,320.00 USD | `-21.39%` | `16,641.80` |
| `Live` | `Long` | `0.0805` | 110,570.00 USD | 0.00 USD | 223.98 USD | `-20.40%` | `2,782.40` |
| `Live` | `Long` | `0.0815` | 110,340.00 USD | 0.00 USD | 1,560.00 USD | `-19.41%` | `19,181.40` |
| `Live` | `Long` | `0.0895` | 108,780.00 USD | 0.00 USD | 3,120.00 USD | `-11.50%` | `34,873.20` |
| `Live` | `Long` | `0.0905` | 105,660.00 USD | 0.00 USD | 1,260.00 USD | `-10.51%` | `13,961.60` |
| `Live` | `Long` | `0.0945` | 104,400.00 USD | 0.00 USD | 69,120.00 USD | `-6.56%` | `731,405.60` |
| `Live` | `Long` | `0.0955` | 35,280.00 USD | 0.00 USD | 2,040.00 USD | `-5.57%` | `21,390.40` |
| `Live` | `Long` | `0.0965` | 33,230.00 USD | 0.00 USD | 1,160.00 USD | `-4.58%` | `12,006.40` |
| `Live` | `Long` | `0.0975` | 32,080.00 USD | 0.00 USD | 11,950.00 USD | `-3.59%` | `122,573.60` |
| `Live` | `Long` | `0.0985` | 20,130.00 USD | 0.00 USD | 20,130.00 USD | `-2.60%` | `204,315.90` |
| `Live` | `Short` | `0.1135` | 557.61 USD | 557.61 USD | 0.00 USD | `+12.23%` | `4,912.90` |
| `Live` | `Short` | `0.1225` | 1,280.00 USD | 721.08 USD | 0.00 USD | `+21.13%` | `5,886.40` |
| `Live` | `Short` | `0.1235` | 10,450.00 USD | 9,170.00 USD | 0.00 USD | `+22.12%` | `74,243.50` |
| `Live` | `Short` | `0.1355` | 11,780.00 USD | 1,330.00 USD | 0.00 USD | `+33.99%` | `9,843.80` |
| `Live` | `Short` | `0.1465` | 37,510.00 USD | 25,730.00 USD | 0.00 USD | `+44.86%` | `175,640.10` |
| `Live` | `Short` | `0.1525` | 43,600.00 USD | 6,090.00 USD | 0.00 USD | `+50.80%` | `39,929.50` |
| `Live` | `Short` | `0.1555` | 59,150.00 USD | 15,550.00 USD | 0.00 USD | `+53.76%` | `100,000.40` |
| `Live` | `Short` | `0.1565` | 59,700.00 USD | 550.61 USD | 0.00 USD | `+54.75%` | `3,518.30` |
| `Live` | `Short` | `0.1695` | 59,870.00 USD | 169.25 USD | 0.00 USD | `+67.61%` | `998.50` |
| `Live` | `Short` | `0.1865` | 60,040.00 USD | 167.85 USD | 0.00 USD | `+84.42%` | `900.00` |
| `Live` | `Short` | `0.1945` | 60,150.00 USD | 109.31 USD | 0.00 USD | `+92.33%` | `562.00` |
| `Live` | `Short` | `0.1995` | 61,110.00 USD | 964.32 USD | 0.00 USD | `+97.27%` | `4,833.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0635` | 12,880.00 USD | 0.00 USD | 1,140.00 USD | `-37.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 11,750.00 USD | 0.00 USD | 773.46 USD | `-30.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 10,970.00 USD | 0.00 USD | 592.27 USD | `-29.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 10,380.00 USD | 0.00 USD | 755.00 USD | `-25.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0805` | 9,620.00 USD | 0.00 USD | 411.06 USD | `-20.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0815` | 9,210.00 USD | 0.00 USD | 183.49 USD | `-19.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0835` | 9,030.00 USD | 0.00 USD | 456.70 USD | `-17.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 8,570.00 USD | 0.00 USD | 631.58 USD | `-15.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 7,940.00 USD | 0.00 USD | 653.74 USD | `-12.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 7,290.00 USD | 0.00 USD | 444.62 USD | `-10.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0915` | 6,840.00 USD | 0.00 USD | 1,460.00 USD | `-9.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 5,380.00 USD | 0.00 USD | 485.13 USD | `-6.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0975` | 4,890.00 USD | 0.00 USD | 985.89 USD | `-3.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0985` | 3,910.00 USD | 0.00 USD | 931.75 USD | `-2.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0995` | 2,980.00 USD | 0.00 USD | 801.64 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 2,180.00 USD | 0.00 USD | 2,180.00 USD | `-0.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1015` | 903.42 USD | 903.42 USD | 0.00 USD | `+0.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1025` | 1,680.00 USD | 780.70 USD | 0.00 USD | `+1.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1035` | 6,330.00 USD | 4,650.00 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 25,280.00 USD | 18,950.00 USD | 0.00 USD | `+3.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 33,050.00 USD | 7,770.00 USD | 0.00 USD | `+4.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 142,330.00 USD | 109,280.00 USD | 0.00 USD | `+5.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1075` | 164,240.00 USD | 21,900.00 USD | 0.00 USD | `+6.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1085` | 164,390.00 USD | 150.04 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1095` | 165,030.00 USD | 639.36 USD | 0.00 USD | `+8.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 165,190.00 USD | 162.59 USD | 0.00 USD | `+9.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 166,030.00 USD | 839.64 USD | 0.00 USD | `+10.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1125` | 166,820.00 USD | 786.65 USD | 0.00 USD | `+11.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1135` | 166,930.00 USD | 116.27 USD | 0.00 USD | `+12.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1145` | 167,070.00 USD | 134.61 USD | 0.00 USD | `+13.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 167,210.00 USD | 137.71 USD | 0.00 USD | `+14.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1165` | 167,390.00 USD | 180.81 USD | 0.00 USD | `+15.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1175` | 167,750.00 USD | 363.49 USD | 0.00 USD | `+16.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1185` | 168,800.00 USD | 1,050.00 USD | 0.00 USD | `+17.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1195` | 183,440.00 USD | 14,640.00 USD | 0.00 USD | `+18.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1205` | 183,840.00 USD | 398.42 USD | 0.00 USD | `+19.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1225` | 184,820.00 USD | 980.00 USD | 0.00 USD | `+21.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1235` | 197,170.00 USD | 12,350.00 USD | 0.00 USD | `+22.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1255` | 201,540.00 USD | 4,380.00 USD | 0.00 USD | `+24.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1275` | 202,040.00 USD | 492.06 USD | 0.00 USD | `+26.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1305` | 202,480.00 USD | 444.24 USD | 0.00 USD | `+29.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1315` | 234,040.00 USD | 31,560.00 USD | 0.00 USD | `+30.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1335` | 235,360.00 USD | 1,310.00 USD | 0.00 USD | `+32.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1345` | 239,510.00 USD | 4,150.00 USD | 0.00 USD | `+33.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1365` | 247,100.00 USD | 7,590.00 USD | 0.00 USD | `+34.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1405` | 260,200.00 USD | 13,110.00 USD | 0.00 USD | `+38.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1425` | 260,310.00 USD | 102.22 USD | 0.00 USD | `+40.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1435` | 267,480.00 USD | 7,180.00 USD | 0.00 USD | `+41.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1485` | 270,130.00 USD | 2,650.00 USD | 0.00 USD | `+46.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1495` | 270,920.00 USD | 792.53 USD | 0.00 USD | `+47.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1525` | 274,690.00 USD | 3,770.00 USD | 0.00 USD | `+50.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 274,870.00 USD | 184.49 USD | 0.00 USD | `+53.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 277,680.00 USD | 2,810.00 USD | 0.00 USD | `+54.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 277,900.00 USD | 219.81 USD | 0.00 USD | `+55.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 278,180.00 USD | 277.62 USD | 0.00 USD | `+61.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 279,970.00 USD | 1,800.00 USD | 0.00 USD | `+67.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 280,190.00 USD | 216.55 USD | 0.00 USD | `+72.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 280,310.00 USD | 117.26 USD | 0.00 USD | `+95.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 300,840.00 USD | 20,530.00 USD | 0.00 USD | `+98.26%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0878` | 872,720.00 USD | 0.00 USD | 872,720.00 USD | 1,370.00 USD | 4,930.00 USD | 27,260.00 USD |
| `1D` | `0.0881` | 523,410.00 USD | 0.00 USD | 523,410.00 USD | 2,400.00 USD | 1,300.00 USD | 4,700.00 USD |
| `7D` | `0.0881` | 839,160.00 USD | 0.00 USD | 839,160.00 USD | 3,770.00 USD | 2,660.00 USD | 12,940.00 USD |
| `1D` | `0.0883` | 515,010.00 USD | 0.00 USD | 515,010.00 USD | 2,370.00 USD | 659.34 USD | 5,980.00 USD |
| `7D` | `0.0884` | 819,790.00 USD | 0.00 USD | 819,790.00 USD | 7,040.00 USD | 4,640.00 USD | 11,870.00 USD |
| `1D` | `0.0885` | 506,000.00 USD | 0.00 USD | 506,000.00 USD | 0.00 USD | 312.16 USD | 2,520.00 USD |
| `1D` | `0.0887` | 503,170.00 USD | 0.00 USD | 503,170.00 USD | 1,740.00 USD | 655.48 USD | 4,540.00 USD |
| `7D` | `0.0887` | 796,240.00 USD | 0.00 USD | 796,240.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD |
| `1D` | `0.0889` | 496,240.00 USD | 0.00 USD | 496,240.00 USD | 727.20 USD | 1,690.00 USD | 2,110.00 USD |
| `7D` | `0.0890` | 762,100.00 USD | 0.00 USD | 762,100.00 USD | 14,610.00 USD | 4,470.00 USD | 3,680.00 USD |
| `1D` | `0.0891` | 491,720.00 USD | 0.00 USD | 491,720.00 USD | 1,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0893` | 490,390.00 USD | 0.00 USD | 490,390.00 USD | 983.61 USD | 0.00 USD | 542.23 USD |
| `7D` | `0.0893` | 739,350.00 USD | 0.00 USD | 739,350.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD |
| `1D` | `0.0895` | 488,870.00 USD | 0.00 USD | 488,870.00 USD | 0.00 USD | 215.06 USD | 394.61 USD |
| `7D` | `0.0896` | 720,180.00 USD | 0.00 USD | 720,180.00 USD | 5,760.00 USD | 611.80 USD | 6,870.00 USD |
| `1D` | `0.0897` | 488,260.00 USD | 0.00 USD | 488,260.00 USD | 0.00 USD | 772.87 USD | 0.02 USD |
| `1D` | `0.0899` | 487,480.00 USD | 0.00 USD | 487,480.00 USD | 0.00 USD | 287.77 USD | 601.21 USD |
| `7D` | `0.0899` | 706,930.00 USD | 0.00 USD | 706,930.00 USD | 3,390.00 USD | 927.82 USD | 4,490.00 USD |
| `1D` | `0.0901` | 486,590.00 USD | 0.00 USD | 486,590.00 USD | 2,450.00 USD | 0.00 USD | 293.66 USD |
| `7D` | `0.0902` | 698,130.00 USD | 0.00 USD | 698,130.00 USD | 2,270.00 USD | 910.78 USD | 1,210.00 USD |
| `1D` | `0.0903` | 483,850.00 USD | 0.00 USD | 483,850.00 USD | 831.11 USD | 2,190.00 USD | 1,070.00 USD |
| `1D` | `0.0905` | 479,760.00 USD | 0.00 USD | 479,760.00 USD | 413.91 USD | 998.41 USD | 2,840.00 USD |
| `7D` | `0.0905` | 693,730.00 USD | 0.00 USD | 693,730.00 USD | 10,350.00 USD | 996.61 USD | 4,080.00 USD |
| `1D` | `0.0907` | 475,510.00 USD | 0.00 USD | 475,510.00 USD | 2,290.00 USD | 909.44 USD | 974.67 USD |
| `7D` | `0.0908` | 678,310.00 USD | 0.00 USD | 678,310.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD |
| `1D` | `0.0909` | 471,340.00 USD | 0.00 USD | 471,340.00 USD | 938.76 USD | 957.38 USD | 785.45 USD |
| `1D` | `0.0911` | 468,660.00 USD | 0.00 USD | 468,660.00 USD | 5,580.00 USD | 778.50 USD | 10.60 USD |
| `7D` | `0.0911` | 666,910.00 USD | 0.00 USD | 666,910.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD |
| `1D` | `0.0913` | 462,290.00 USD | 0.00 USD | 462,290.00 USD | 0.00 USD | 0.00 USD | 787.25 USD |
| `7D` | `0.0914` | 663,630.00 USD | 0.00 USD | 663,630.00 USD | 1,670.00 USD | 903.90 USD | 45.81 USD |
| `1D` | `0.0915` | 461,500.00 USD | 0.00 USD | 461,500.00 USD | 6,590.00 USD | 0.00 USD | 52.64 USD |
| `1D` | `0.0917` | 454,860.00 USD | 0.00 USD | 454,860.00 USD | 2,550.00 USD | 0.00 USD | 2.87 USD |
| `7D` | `0.0917` | 661,010.00 USD | 0.00 USD | 661,010.00 USD | 0.00 USD | 0.00 USD | 1,740.00 USD |
| `1D` | `0.0919` | 452,300.00 USD | 0.00 USD | 452,300.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0923` | 448,610.00 USD | 0.00 USD | 448,610.00 USD | 0.00 USD | 0.00 USD | 42.87 USD |
| `7D` | `0.0923` | 659,270.00 USD | 0.00 USD | 659,270.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `0.0925` | 448,570.00 USD | 0.00 USD | 448,570.00 USD | 3,270.00 USD | 1,660.00 USD | 0.00 USD |
| `7D` | `0.0926` | 657,810.00 USD | 0.00 USD | 657,810.00 USD | 1,790.00 USD | 0.00 USD | 6.00 USD |
| `7D` | `0.0932` | 656,010.00 USD | 0.00 USD | 656,010.00 USD | 0.00 USD | 0.00 USD | 3,180.00 USD |
| `7D` | `0.0935` | 652,830.00 USD | 0.00 USD | 652,830.00 USD | 0.00 USD | 1,320.00 USD | 6,490.00 USD |
| `7D` | `0.0938` | 645,020.00 USD | 0.00 USD | 645,020.00 USD | 0.00 USD | 0.00 USD | 8.57 USD |
| `1D` | `0.0939` | 443,650.00 USD | 0.00 USD | 443,650.00 USD | 0.00 USD | 0.00 USD | 76.92 USD |
| `7D` | `0.0941` | 645,010.00 USD | 0.00 USD | 645,010.00 USD | 2,050.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `0.0944` | 639,940.00 USD | 0.00 USD | 639,940.00 USD | 1,870.00 USD | 0.00 USD | 7,520.00 USD |
| `1D` | `0.0947` | 443,570.00 USD | 0.00 USD | 443,570.00 USD | 0.00 USD | 0.00 USD | 69.61 USD |
| `7D` | `0.0947` | 630,540.00 USD | 0.00 USD | 630,540.00 USD | 3,790.00 USD | 1,810.00 USD | 22.82 USD |
| `7D` | `0.0950` | 624,920.00 USD | 0.00 USD | 624,920.00 USD | 3,770.00 USD | 0.00 USD | 6,660.00 USD |
| `1D` | `0.0953` | 443,500.00 USD | 0.00 USD | 443,500.00 USD | 0.00 USD | 0.00 USD | 87.96 USD |
| `7D` | `0.0953` | 614,480.00 USD | 0.00 USD | 614,480.00 USD | 0.00 USD | 0.00 USD | 4.65 USD |
| `1D` | `0.0955` | 443,410.00 USD | 0.00 USD | 443,410.00 USD | 0.00 USD | 1,180.00 USD | 166.88 USD |
| `7D` | `0.0959` | 614,480.00 USD | 0.00 USD | 614,480.00 USD | 0.00 USD | 1,140.00 USD | 115.48 USD |
| `1D` | `0.0961` | 442,060.00 USD | 0.00 USD | 442,060.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0962` | 613,230.00 USD | 0.00 USD | 613,230.00 USD | 0.00 USD | 0.00 USD | 2.60 USD |
| `1D` | `0.0963` | 439,990.00 USD | 0.00 USD | 439,990.00 USD | 0.00 USD | 0.00 USD | 1.02 USD |
| `1D` | `0.0965` | 439,990.00 USD | 0.00 USD | 439,990.00 USD | 1,280.00 USD | 282.32 USD | 1,880.00 USD |
| `7D` | `0.0965` | 613,220.00 USD | 0.00 USD | 613,220.00 USD | 0.00 USD | 0.00 USD | 1,210.00 USD |
| `1D` | `0.0967` | 436,540.00 USD | 0.00 USD | 436,540.00 USD | 2,660.00 USD | 1,100.00 USD | 7,500.00 USD |
| `7D` | `0.0968` | 612,010.00 USD | 0.00 USD | 612,010.00 USD | 7,490.00 USD | 3,720.00 USD | 11,550.00 USD |
| `1D` | `0.0969` | 425,280.00 USD | 0.00 USD | 425,280.00 USD | 4,590.00 USD | 2,640.00 USD | 9,010.00 USD |
| `1D` | `0.0971` | 409,040.00 USD | 0.00 USD | 409,040.00 USD | 16,100.00 USD | 3,330.00 USD | 4,510.00 USD |
| `7D` | `0.0971` | 589,260.00 USD | 0.00 USD | 589,260.00 USD | 0.00 USD | 3,760.00 USD | 9,720.00 USD |
| `1D` | `0.0973` | 385,100.00 USD | 0.00 USD | 385,100.00 USD | 0.00 USD | 2,120.00 USD | 4,400.00 USD |
| `7D` | `0.0974` | 575,780.00 USD | 0.00 USD | 575,780.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD |
| `1D` | `0.0975` | 378,580.00 USD | 0.00 USD | 378,580.00 USD | 0.00 USD | 1,810.00 USD | 5,550.00 USD |
| `1D` | `0.0977` | 371,210.00 USD | 0.00 USD | 371,210.00 USD | 24,760.00 USD | 2,510.00 USD | 11,230.00 USD |
| `7D` | `0.0977` | 571,500.00 USD | 0.00 USD | 571,500.00 USD | 0.00 USD | 1,160.00 USD | 13,130.00 USD |
| `1D` | `0.0979` | 332,710.00 USD | 0.00 USD | 332,710.00 USD | 12,620.00 USD | 1,040.00 USD | 8.08 USD |
| `7D` | `0.0980` | 557,210.00 USD | 0.00 USD | 557,210.00 USD | 0.00 USD | 3,920.00 USD | 5,710.00 USD |
| `1D` | `0.0981` | 319,040.00 USD | 0.00 USD | 319,040.00 USD | 9,220.00 USD | 431.42 USD | 3,030.00 USD |
| `1D` | `0.0983` | 306,360.00 USD | 0.00 USD | 306,360.00 USD | 3,250.00 USD | 1,390.00 USD | 16,110.00 USD |
| `7D` | `0.0983` | 547,590.00 USD | 0.00 USD | 547,590.00 USD | 7,990.00 USD | 1,230.00 USD | 14,770.00 USD |
| `1D` | `0.0985` | 285,620.00 USD | 0.00 USD | 285,620.00 USD | 5,670.00 USD | 413.94 USD | 2,690.00 USD |
| `7D` | `0.0986` | 523,590.00 USD | 0.00 USD | 523,590.00 USD | 7,110.00 USD | 7,530.00 USD | 38,150.00 USD |
| `1D` | `0.0987` | 276,850.00 USD | 0.00 USD | 276,850.00 USD | 15,960.00 USD | 6,330.00 USD | 4,810.00 USD |
| `1D` | `0.0989` | 249,750.00 USD | 0.00 USD | 249,750.00 USD | 2,820.00 USD | 3,290.00 USD | 2,180.00 USD |
| `7D` | `0.0989` | 470,790.00 USD | 0.00 USD | 470,790.00 USD | 17,640.00 USD | 6,190.00 USD | 32,770.00 USD |
| `1D` | `0.0991` | 241,450.00 USD | 0.00 USD | 241,450.00 USD | 32,710.00 USD | 2,950.00 USD | 3,200.00 USD |
| `7D` | `0.0992` | 414,200.00 USD | 0.00 USD | 414,200.00 USD | 27,140.00 USD | 11,490.00 USD | 28,490.00 USD |
| `1D` | `0.0993` | 202,600.00 USD | 0.00 USD | 202,600.00 USD | 3,080.00 USD | 1,720.00 USD | 11,460.00 USD |
| `1D` | `0.0995` | 186,330.00 USD | 0.00 USD | 186,330.00 USD | 2,740.00 USD | 624.33 USD | 11,480.00 USD |
| `7D` | `0.0995` | 347,070.00 USD | 0.00 USD | 347,070.00 USD | 24,220.00 USD | 15,150.00 USD | 34,050.00 USD |
| `1D` | `0.0997` | 171,480.00 USD | 0.00 USD | 171,480.00 USD | 35,260.00 USD | 718.82 USD | 10,040.00 USD |
| `7D` | `0.0998` | 273,650.00 USD | 0.00 USD | 273,650.00 USD | 28,450.00 USD | 6,400.00 USD | 49,360.00 USD |
| `1D` | `0.0999` | 125,460.00 USD | 0.00 USD | 125,460.00 USD | 29,920.00 USD | 2,940.00 USD | 16,790.00 USD |
| `1D` | `0.1001` | 75,810.00 USD | 0.00 USD | 75,810.00 USD | 21,100.00 USD | 1,410.00 USD | 4,200.00 USD |
| `7D` | `0.1001` | 189,430.00 USD | 0.00 USD | 189,430.00 USD | 36,110.00 USD | 8,650.00 USD | 13,120.00 USD |
| `1D` | `0.1003` | 49,110.00 USD | 0.00 USD | 49,110.00 USD | 0.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1004` | 131,540.00 USD | 0.00 USD | 131,540.00 USD | 22,470.00 USD | 16,470.00 USD | 23,430.00 USD |
| `1D` | `0.1005` | 48,550.00 USD | 0.00 USD | 48,550.00 USD | 1,970.00 USD | 403.62 USD | 13,950.00 USD |
| `1D` | `0.1007` | 32,230.00 USD | 0.00 USD | 32,230.00 USD | 0.00 USD | 8,710.00 USD | 789.22 USD |
| `7D` | `0.1007` | 69,170.00 USD | 0.00 USD | 69,170.00 USD | 20,870.00 USD | 3,870.00 USD | 13,880.00 USD |
| `1D` | `0.1009` | 22,730.00 USD | 0.00 USD | 22,730.00 USD | 0.00 USD | 2,750.00 USD | 0.00 USD |
| `7D` | `0.1010` | 30,560.00 USD | 0.00 USD | 30,560.00 USD | 17,340.00 USD | 6,580.00 USD | 6,630.00 USD |
| `1D` | `0.1011` | 19,990.00 USD | 0.00 USD | 19,990.00 USD | 0.00 USD | 575.54 USD | 3,390.00 USD |
| `1D` | `0.1013` | 16,020.00 USD | 0.00 USD | 16,020.00 USD | 0.00 USD | 800.79 USD | 587.32 USD |
| `7D` | `0.1013` | 31,990.00 USD | 31,990.00 USD | 0.00 USD | 15,270.00 USD | 5,230.00 USD | 11,490.00 USD |
| `7D` | `0.1013` | 63,970.00 USD | 63,970.00 USD | 0.00 USD | 15,270.00 USD | 5,230.00 USD | 11,490.00 USD |
| `1D` | `0.1015` | 14,630.00 USD | 0.00 USD | 14,630.00 USD | 0.00 USD | 1,830.00 USD | 1,660.00 USD |
| `7D` | `0.1016` | 90,420.00 USD | 90,420.00 USD | 0.00 USD | 15,440.00 USD | 5,490.00 USD | 5,510.00 USD |
| `1D` | `0.1017` | 11,140.00 USD | 0.00 USD | 11,140.00 USD | 0.00 USD | 3,440.00 USD | 0.00 USD |
| `1D` | `0.1019` | 7,700.00 USD | 0.00 USD | 7,700.00 USD | 0.00 USD | 6,380.00 USD | 0.00 USD |
| `7D` | `0.1019` | 122,580.00 USD | 122,580.00 USD | 0.00 USD | 12,100.00 USD | 5,790.00 USD | 14,260.00 USD |
| `1D` | `0.1021` | 1,320.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD |
| `7D` | `0.1022` | 155,770.00 USD | 155,770.00 USD | 0.00 USD | 11,930.00 USD | 8,250.00 USD | 13,010.00 USD |
| `7D` | `0.1025` | 171,690.00 USD | 171,690.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | 14,370.00 USD |
| `1D` | `0.1026` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1028` | 180,460.00 USD | 180,460.00 USD | 0.00 USD | 3,800.00 USD | 4,390.00 USD | 581.37 USD |
| `1D` | `0.1029` | 6,230.00 USD | 6,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,230.00 USD |
| `1D` | `0.1031` | 53,030.00 USD | 53,030.00 USD | 0.00 USD | 27,910.00 USD | 0.00 USD | 18,890.00 USD |
| `7D` | `0.1031` | 217,080.00 USD | 217,080.00 USD | 0.00 USD | 19,560.00 USD | 6,260.00 USD | 10,790.00 USD |
| `1D` | `0.1033` | 74,890.00 USD | 74,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,860.00 USD |
| `7D` | `0.1034` | 281,860.00 USD | 281,860.00 USD | 0.00 USD | 18,920.00 USD | 7,030.00 USD | 38,840.00 USD |
| `1D` | `0.1035` | 96,970.00 USD | 96,970.00 USD | 0.00 USD | 4,780.00 USD | 4,880.00 USD | 12,410.00 USD |
| `1D` | `0.1037` | 155,500.00 USD | 155,500.00 USD | 0.00 USD | 37,310.00 USD | 11,960.00 USD | 9,270.00 USD |
| `7D` | `0.1037` | 324,060.00 USD | 324,060.00 USD | 0.00 USD | 2,710.00 USD | 5,010.00 USD | 34,470.00 USD |
| `1D` | `0.1039` | 218,260.00 USD | 218,260.00 USD | 0.00 USD | 32,370.00 USD | 5,450.00 USD | 24,950.00 USD |
| `7D` | `0.1040` | 351,040.00 USD | 351,040.00 USD | 0.00 USD | 5,940.00 USD | 10,300.00 USD | 10,740.00 USD |
| `1D` | `0.1041` | 274,670.00 USD | 274,670.00 USD | 0.00 USD | 24,950.00 USD | 12,830.00 USD | 18,640.00 USD |
| `1D` | `0.1043` | 307,390.00 USD | 307,390.00 USD | 0.00 USD | 19,210.00 USD | 5,650.00 USD | 7,860.00 USD |
| `7D` | `0.1043` | 402,200.00 USD | 402,200.00 USD | 0.00 USD | 15,960.00 USD | 5,980.00 USD | 29,210.00 USD |
| `1D` | `0.1045` | 335,530.00 USD | 335,530.00 USD | 0.00 USD | 4,220.00 USD | 4,840.00 USD | 19,080.00 USD |
| `7D` | `0.1046` | 441,850.00 USD | 441,850.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD | 29,840.00 USD |
| `1D` | `0.1047` | 374,560.00 USD | 374,560.00 USD | 0.00 USD | 15,000.00 USD | 3,400.00 USD | 20,630.00 USD |
| `1D` | `0.1049` | 433,500.00 USD | 433,500.00 USD | 0.00 USD | 37,390.00 USD | 10,710.00 USD | 10,840.00 USD |
| `7D` | `0.1049` | 526,380.00 USD | 526,380.00 USD | 0.00 USD | 34,790.00 USD | 6,530.00 USD | 43,210.00 USD |
| `1D` | `0.1051` | 496,870.00 USD | 496,870.00 USD | 0.00 USD | 30,370.00 USD | 8,750.00 USD | 24,260.00 USD |
| `7D` | `0.1052` | 704,950.00 USD | 704,950.00 USD | 0.00 USD | 28,200.00 USD | 24,160.00 USD | 126,200.00 USD |
| `1D` | `0.1053` | 591,690.00 USD | 591,690.00 USD | 0.00 USD | 35,030.00 USD | 8,930.00 USD | 50,850.00 USD |
| `1D` | `0.1055` | 720,500.00 USD | 720,500.00 USD | 0.00 USD | 43,960.00 USD | 25,140.00 USD | 59,710.00 USD |
| `7D` | `0.1055` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 122,840.00 USD | 44,430.00 USD | 166,470.00 USD |
| `1D` | `0.1057` | 813,050.00 USD | 813,050.00 USD | 0.00 USD | 27,300.00 USD | 15,170.00 USD | 50,080.00 USD |
| `7D` | `0.1058` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 105,620.00 USD | 53,680.00 USD | 189,110.00 USD |
| `1D` | `0.1059` | 914,710.00 USD | 914,710.00 USD | 0.00 USD | 39,020.00 USD | 0.00 USD | 62,640.00 USD |
| `1D` | `0.1061` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 26,970.00 USD | 0.00 USD | 58,940.00 USD |
| `7D` | `0.1061` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 75,540.00 USD | 72,260.00 USD | 102,650.00 USD |
| `1D` | `0.1063` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 9,220.00 USD | 0.00 USD | 48,890.00 USD |
| `7D` | `0.1064` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 52,580.00 USD | 192,400.00 USD |
| `1D` | `0.1065` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25,740.00 USD |
| `1D` | `0.1067` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33,160.00 USD |
| `7D` | `0.1067` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 51,740.00 USD | 133,410.00 USD |
| `1D` | `0.1069` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 8,170.00 USD | 4,140.00 USD | 42,640.00 USD |
| `7D` | `0.1070` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 57,770.00 USD | 114,240.00 USD |
| `1D` | `0.1071` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 3,140.00 USD | 16,220.00 USD |
| `1D` | `0.1073` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 218.01 USD |
| `7D` | `0.1073` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 17,700.00 USD | 0.00 USD |
| `1D` | `0.1075` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 104.34 USD |
| `1D` | `0.1077` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 93.46 USD |
| `1D` | `0.1079` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26.80 USD |
| `7D` | `0.1079` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 79.36 USD |
| `1D` | `0.1083` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 5,910.00 USD | 91.27 USD |
| `1D` | `0.1085` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65,020.00 USD |
| `7D` | `0.1085` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1087` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 28,490.00 USD | 2,240.00 USD | 44,670.00 USD |
| `7D` | `0.1088` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 5,290.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1089` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 39,160.00 USD | 0.00 USD | 87.96 USD |
| `1D` | `0.1091` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 33,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1091` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD |
| `1D` | `0.1093` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 15,480.00 USD | 0.00 USD | 64.27 USD |
| `7D` | `0.1094` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD |
| `1D` | `0.1095` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 21,520.00 USD |
| `1D` | `0.1097` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 7,260.00 USD | 1,970.00 USD | 22,790.00 USD |
| `7D` | `0.1097` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1099` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 6,130.00 USD | 1,940.00 USD | 0.00 USD |
| `7D` | `0.1100` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 21,840.00 USD |
| `1D` | `0.1101` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 4,310.00 USD | 2,820.00 USD | 4,290.00 USD |
| `1D` | `0.1103` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 3,540.00 USD | 5,640.00 USD | 0.00 USD |
| `7D` | `0.1103` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1105` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 3,380.00 USD | 4,740.00 USD | 10,700.00 USD |
| `7D` | `0.1106` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 22,880.00 USD | 15,950.00 USD |
| `1D` | `0.1107` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 3,110.00 USD | 12,720.00 USD | 35,750.00 USD |
| `1D` | `0.1109` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 2,110.00 USD | 1,120.00 USD | 0.00 USD |
| `7D` | `0.1109` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD |
| `1D` | `0.1111` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 5,200.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1112` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD |
| `1D` | `0.1113` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 21,390.00 USD | 5,210.00 USD | 39,070.00 USD |
| `1D` | `0.1115` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1117` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 2,060.00 USD | 25,630.00 USD | 34,770.00 USD |
| `7D` | `0.1118` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD |
| `1D` | `0.1119` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 36,940.00 USD | 6,980.00 USD | 36,740.00 USD |
| `1D` | `0.1121` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 20,000.00 USD | 12,060.00 USD | 12,320.00 USD |
| `7D` | `0.1121` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 17,760.00 USD | 0.00 USD | 32,100.00 USD |
| `1D` | `0.1123` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 40,400.00 USD | 1,780.00 USD | 5,930.00 USD |
| `7D` | `0.1124` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD |
| `1D` | `0.1125` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 11,130.00 USD | 13,240.00 USD | 7,950.00 USD |
| `1D` | `0.1127` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 1,250.00 USD | 19,520.00 USD |
| `7D` | `0.1127` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD |
| `1D` | `0.1129` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 8,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1130` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,170.00 USD |
| `1D` | `0.1131` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 20,830.00 USD | 8,010.00 USD | 11,620.00 USD |
| `1D` | `0.1133` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 6,530.00 USD | 22,520.00 USD | 23,470.00 USD |
| `7D` | `0.1133` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 12,540.00 USD | 11,430.00 USD | 0.00 USD |
| `1D` | `0.1135` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 4,040.00 USD | 3,670.00 USD | 4,090.00 USD |
| `7D` | `0.1136` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD |
| `1D` | `0.1137` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 856.93 USD | 40.44 USD |
| `1D` | `0.1139` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,270.00 USD |
| `1D` | `0.1141` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 13,860.00 USD | 2,800.00 USD | 13,480.00 USD |
| `7D` | `0.1142` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,540.00 USD |
| `1D` | `0.1143` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 20,300.00 USD | 27,990.00 USD | 11,820.00 USD |
| `1D` | `0.1145` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 13,430.00 USD | 11,690.00 USD | 38,030.00 USD |
| `7D` | `0.1145` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD |
| `1D` | `0.1147` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 10,640.00 USD | 10,080.00 USD | 30,680.00 USD |
| `7D` | `0.1148` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 176,010.00 USD |
| `1D` | `0.1149` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 35,170.00 USD | 624.71 USD | 31,820.00 USD |
| `1D` | `0.1151` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 16,450.00 USD | 14,620.00 USD | 33,180.00 USD |
| `7D` | `0.1151` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD |
| `1D` | `0.1153` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 31,350.00 USD | 23,630.00 USD | 59,030.00 USD |
| `7D` | `0.1154` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 243,190.00 USD | 26,970.00 USD | 195,390.00 USD |
| `1D` | `0.1155` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 38,430.00 USD | 27,080.00 USD | 54,030.00 USD |
| `1D` | `0.1157` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 33,550.00 USD | 9,850.00 USD | 7,870.00 USD |
| `7D` | `0.1157` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 188,950.00 USD | 25,290.00 USD | 98,310.00 USD |
| `1D` | `0.1159` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 22,990.00 USD | 12,000.00 USD | 17,950.00 USD |
| `7D` | `0.1160` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 139,350.00 USD | 32,830.00 USD | 109,320.00 USD |
| `1D` | `0.1161` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 23,670.00 USD | 0.00 USD | 5,160.00 USD |
| `1D` | `0.1163` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 9,380.00 USD | 17,460.00 USD |
| `7D` | `0.1163` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD |
| `1D` | `0.1165` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 8,820.00 USD | 5,320.00 USD | 5,490.00 USD |
| `7D` | `0.1166` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD |
| `1D` | `0.1167` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 7,220.00 USD | 6,170.00 USD |
| `1D` | `0.1169` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 5,480.00 USD | 2,440.00 USD | 5,990.00 USD |
| `7D` | `0.1169` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 82,770.00 USD | 26,150.00 USD | 112,810.00 USD |
| `1D` | `0.1171` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 13,800.00 USD | 0.00 USD | 4,510.00 USD |
| `7D` | `0.1172` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD |
| `1D` | `0.1173` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 9,320.00 USD | 5,440.00 USD | 4,840.00 USD |
| `1D` | `0.1175` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 9,530.00 USD | 9,020.00 USD | 19,930.00 USD |
| `7D` | `0.1175` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 72,770.00 USD | 17,930.00 USD | 81,630.00 USD |
| `1D` | `0.1177` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 14,360.00 USD | 8,560.00 USD | 16,650.00 USD |
| `7D` | `0.1178` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 89,510.00 USD | 23,660.00 USD | 55,770.00 USD |
| `1D` | `0.1179` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 10,640.00 USD | 4,760.00 USD | 5,770.00 USD |
| `1D` | `0.1181` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 14,160.00 USD | 6,410.00 USD | 15,670.00 USD |
| `7D` | `0.1181` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD |
| `1D` | `0.1183` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 8,760.00 USD | 677.63 USD | 4,580.00 USD |
| `7D` | `0.1184` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD |
| `1D` | `0.1185` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 4,390.00 USD | 5,850.00 USD | 6,770.00 USD |
| `1D` | `0.1187` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 4,060.00 USD | 3,330.00 USD | 11,670.00 USD |
| `7D` | `0.1187` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 5,620.00 USD | 17,120.00 USD | 54,960.00 USD |
| `1D` | `0.1189` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 2,120.00 USD | 4,350.00 USD |
| `7D` | `0.1190` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD |
| `1D` | `0.1191` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 1,810.00 USD | 5,650.00 USD |
| `1D` | `0.1193` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 4,720.00 USD | 1,040.00 USD | 3,840.00 USD |
| `7D` | `0.1193` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD |
| `1D` | `0.1195` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 9,550.00 USD | 1,470.00 USD | 2,800.00 USD |
| `7D` | `0.1196` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD |
| `1D` | `0.1197` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 1,040.00 USD | 93.72 USD |
| `1D` | `0.1199` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 431.42 USD | 3,050.00 USD |
| `7D` | `0.1199` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 9,100.00 USD | 13,190.00 USD | 67,980.00 USD |
| `1D` | `0.1201` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 3,250.00 USD | 1,390.00 USD | 9,700.00 USD |
| `7D` | `0.1202` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 138,430.00 USD | 21,430.00 USD | 32,790.00 USD |
| `1D` | `0.1203` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 5,670.00 USD | 413.94 USD | 2,710.00 USD |
| `1D` | `0.1205` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 2,250.00 USD | 1,670.00 USD | 741.32 USD |
| `7D` | `0.1205` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 132,960.00 USD | 72,910.00 USD | 130,900.00 USD |
| `1D` | `0.1207` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 5,540.00 USD | 524.23 USD | 4,100.00 USD |
| `7D` | `0.1208` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 39,480.00 USD | 25,720.00 USD | 66,520.00 USD |
| `1D` | `0.1209` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 2,820.00 USD | 3,290.00 USD | 2,240.00 USD |
| `1D` | `0.1211` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 4,800.00 USD | 2,950.00 USD | 3,240.00 USD |
| `7D` | `0.1211` | 7,200,000.00 USD | 7,200,000.00 USD | 0.00 USD | 72,500.00 USD | 25,920.00 USD | 111,160.00 USD |
| `1D` | `0.1213` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 5,870.00 USD | 1,720.00 USD | 11,460.00 USD |
| `7D` | `0.1214` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD |
| `1D` | `0.1215` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD | 5,450.00 USD |
| `1D` | `0.1217` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 1,090.00 USD | 624.33 USD | 6,070.00 USD |
| `7D` | `0.1217` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD |
| `1D` | `0.1219` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 2,320.00 USD | 718.82 USD | 10,060.00 USD |
| `7D` | `0.1220` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 45,700.00 USD | 10,970.00 USD | 54,700.00 USD |
| `1D` | `0.1221` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 7,970.00 USD | 2,940.00 USD | 3,670.00 USD |
| `1D` | `0.1223` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 2,660.00 USD | 1,410.00 USD | 4,210.00 USD |
| `7D` | `0.1223` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 76,930.00 USD | 36,110.00 USD | 50,790.00 USD |
| `1D` | `0.1225` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 1,840.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1226` | 7,740,000.00 USD | 7,740,000.00 USD | 0.00 USD | 54,940.00 USD | 32,070.00 USD | 5,210.00 USD |
| `1D` | `0.1227` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1229` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 403.62 USD | 1,080.00 USD |
| `7D` | `0.1229` | 7,960,000.00 USD | 7,960,000.00 USD | 0.00 USD | 91,580.00 USD | 42,230.00 USD | 91,160.00 USD |
| `1D` | `0.1230` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 789.22 USD |
| `7D` | `0.1232` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 67,800.00 USD | 41,730.00 USD | 63,720.00 USD |
| `7D` | `0.1235` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 15,040.00 USD | 5,390.00 USD | 13,040.00 USD |
| `7D` | `0.1238` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 8,310.00 USD | 3,610.00 USD | 3,100.00 USD |
| `7D` | `0.1241` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 11,380.00 USD | 1,380.00 USD | 2,590.00 USD |
| `7D` | `0.1244` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 26,540.00 USD | 8,130.00 USD | 9,630.00 USD |
| `7D` | `0.1247` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 7,900.00 USD | 18,280.00 USD | 17,680.00 USD |
| `7D` | `0.1250` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 8,540.00 USD | 7,270.00 USD | 5,780.00 USD |
| `7D` | `0.1253` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 11,420.00 USD | 2,100.00 USD | 22,530.00 USD |
| `7D` | `0.1256` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 11,990.00 USD | 18,000.00 USD | 220.44 USD |
| `7D` | `0.1259` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 5,870.00 USD | 1,190.00 USD | 151.34 USD |
| `7D` | `0.1262` | 8,390,000.00 USD | 8,390,000.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | 3,530.00 USD |
| `7D` | `0.1265` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 2,710.00 USD | 0.00 USD | 7,350.00 USD |
| `7D` | `0.1268` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD |
| `7D` | `0.1271` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 5,940.00 USD | 0.00 USD | 30.15 USD |
| `7D` | `0.1274` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12.00 USD |
| `7D` | `0.1277` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31.66 USD |
| `7D` | `0.1280` | 8,420,000.00 USD | 8,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,390.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `64.93M` | Total OI Tokens: `634,321,661.2 OP`
  * 1h OI Change: `-7.70%` | 4h OI Change: `-13.70%` | 24h OI Change: `-16.32%`
  * Exchange Breakdown: Binance=`15.00M` | Bybit=`12.72M` | OKX=`3.61M` | Hyperliquid=`3.34M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-1.90K` | Last 24h: `270.64` | Last 3d: `-2.23K` | Last 7d: `-15.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0143%` | **USDT OKX** | `0.0037%` |
| **USDT Bybit** | `0.0008%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0141%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0141%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `49.14%` | `50.86%` | `0.97` | 8,010,000.00 USD |
| `15M` | `Binance` | `49.45%` | `50.55%` | `0.98` | 3,140,000.00 USD |
| `15M` | `OKX` | `46.7%` | `53.3%` | `0.88` | 841,940.00 USD |
| `15M` | `Bybit` | `45.81%` | `54.19%` | `0.85` | 1,270,000.00 USD |
| `15M` | `KuCoin` | `52.81%` | `47.19%` | `1.12` | 58,740.00 USD |
| `15M` | `Gate` | `63.13%` | `36.87%` | `1.71` | 173,030.00 USD |
| `15M` | `Bitget` | `50.12%` | `49.88%` | `1.00` | 471,680.00 USD |
| `15M` | `BingX` | `37.19%` | `62.81%` | `0.59` | 240,340.00 USD |
| `15M` | `MEXC` | `53.23%` | `46.77%` | `1.14` | 383,230.00 USD |
| `15M` | `Bitunix` | `50.96%` | `49.04%` | `1.04` | 76,310.00 USD |
| `15M` | `Hyperliquid` | `38.21%` | `61.79%` | `0.62` | 45,250.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.64%` | `49.36%` | `1.03` | 1,230,000.00 USD |
| `15M` | `Crypto.com` | `100%` | `0%` | `1.00` | 101.74 USD |
| `15M` | `WhiteBIT` | `87.6%` | `12.4%` | `7.06` | 46,050.00 USD |
| `15M` | `HTX` | `48.1%` | `51.9%` | `0.93` | 5,800.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `77.49%` | `22.51%` | `3.44` | 10,070.00 USD |
| `15M` | `Aster` | `39.8%` | `60.2%` | `0.66` | 8,870.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `52.69%` | `47.31%` | `1.11` | 8,780.00 USD |
| `15M` | `Whale Positions` | `49.45%` | `50.55%` | `0.98` | 3,140,000.00 USD |
| `15M` | `Global Accounts` | `49.14%` | `50.86%` | `0.97` | 8,010,000.00 USD |
| `1H` | `OP` | `45.48%` | `54.52%` | `0.83` | 34,340,000.00 USD |
| `1H` | `Binance` | `45.53%` | `54.47%` | `0.84` | 13,420,000.00 USD |
| `1H` | `OKX` | `44.5%` | `55.5%` | `0.80` | 4,610,000.00 USD |
| `1H` | `Bybit` | `43.51%` | `56.49%` | `0.77` | 5,770,000.00 USD |
| `1H` | `KuCoin` | `46.79%` | `53.21%` | `0.88` | 417,330.00 USD |
| `1H` | `Gate` | `53.63%` | `46.37%` | `1.16` | 335,280.00 USD |
| `1H` | `Bitget` | `50.67%` | `49.33%` | `1.03` | 2,670,000.00 USD |
| `1H` | `BingX` | `38.67%` | `61.33%` | `0.63` | 760,140.00 USD |
| `1H` | `MEXC` | `42.7%` | `57.3%` | `0.75` | 1,280,000.00 USD |
| `1H` | `Bitunix` | `45.74%` | `54.26%` | `0.84` | 390,520.00 USD |
| `1H` | `Hyperliquid` | `35.42%` | `64.58%` | `0.55` | 551,690.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.25%` | `52.75%` | `0.90` | 3,690,000.00 USD |
| `1H` | `Crypto.com` | `27.55%` | `72.45%` | `0.38` | 18,610.00 USD |
| `1H` | `WhiteBIT` | `70.33%` | `29.67%` | `2.37` | 203,300.00 USD |
| `1H` | `HTX` | `48.58%` | `51.42%` | `0.94` | 44,710.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `57.83%` | `42.17%` | `1.37` | 48,990.00 USD |
| `1H` | `Aster` | `39.59%` | `60.41%` | `0.66` | 42,660.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `55.87%` | `44.13%` | `1.27` | 64,710.00 USD |
| `1H` | `Whale Positions` | `45.53%` | `54.47%` | `0.84` | 13,420,000.00 USD |
| `1H` | `Global Accounts` | `45.48%` | `54.52%` | `0.83` | 34,340,000.00 USD |
| `4H` | `OP` | `41.92%` | `58.08%` | `0.72` | 72,860,000.00 USD |
| `4H` | `Binance` | `42.52%` | `57.48%` | `0.74` | 28,790,000.00 USD |
| `4H` | `OKX` | `47.84%` | `52.16%` | `0.92` | 8,490,000.00 USD |
| `4H` | `Bybit` | `44.9%` | `55.1%` | `0.81` | 10,900,000.00 USD |
| `4H` | `KuCoin` | `48.54%` | `51.46%` | `0.94` | 2,410,000.00 USD |
| `4H` | `Gate` | `50.84%` | `49.16%` | `1.03` | 1,500,000.00 USD |
| `4H` | `Bitget` | `41.94%` | `58.06%` | `0.72` | 2,910,000.00 USD |
| `4H` | `BingX` | `16.53%` | `83.47%` | `0.20` | 6,730,000.00 USD |
| `4H` | `MEXC` | `41.77%` | `58.23%` | `0.72` | 4,380,000.00 USD |
| `4H` | `Bitunix` | `45.7%` | `54.3%` | `0.84` | 1,130,000.00 USD |
| `4H` | `Hyperliquid` | `43.11%` | `56.89%` | `0.76` | 1,600,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.37%` | `50.63%` | `0.98` | 1,370,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `47.11%` | `52.89%` | `0.89` | 1,950,000.00 USD |
| `4H` | `HTX` | `55.27%` | `44.73%` | `1.24` | 75,530.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `73.68%` | `26.32%` | `2.80` | 400,710.00 USD |
| `4H` | `Aster` | `57.67%` | `42.33%` | `1.36` | 157,540.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `27.08%` | `72.92%` | `0.37` | 60,820.00 USD |
| `4H` | `Whale Positions` | `42.52%` | `57.48%` | `0.74` | 28,790,000.00 USD |
| `4H` | `Global Accounts` | `41.92%` | `58.08%` | `0.72` | 72,860,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1102` | `0.1100` | `0.1102` | `0.1104` | `0.1095` | 273,714.46 USD | 165,910.77 USD | 107,803.69 USD | 58,107.08 USD | `+21.23%` | `25B / 9S` |
| `0:00 UTC` | `0.1097` | `0.1098` | `0.1097` | `0.1101` | `0.1096` | 225,346.74 USD | 116,304.67 USD | 109,042.07 USD | 7,262.60 USD | `+3.22%` | `6B / 4S` |
| `5:00 UTC` | `0.1098` | `0.1100` | `0.1098` | `0.1102` | `0.1096` | 199,782.25 USD | 121,152.98 USD | 78,629.27 USD | 42,523.71 USD | `+21.29%` | `24B / 5S` |
| `0:00 UTC` | `0.1103` | `0.1104` | `0.1103` | `0.1106` | `0.1100` | 230,285.46 USD | 143,965.28 USD | 86,320.18 USD | 57,645.10 USD | `+25.03%` | `14B / 4S` |
| `5:00 UTC` | `0.1102` | `0.1102` | `0.1102` | `0.1105` | `0.1099` | 215,356.47 USD | 112,661.20 USD | 102,695.27 USD | 9,965.93 USD | `+4.63%` | `7B / 11S` |
| `0:00 UTC` | `0.1077` | `0.1082` | `0.1077` | `0.1102` | `0.1070` | 2,425,114.31 USD | 1,046,280.57 USD | 1,378,833.74 USD | -332,553.17 USD | `-13.71%` | `8B / 30S` |
| `5:00 UTC` | `0.1084` | `0.1083` | `0.1084` | `0.1087` | `0.1080` | 527,563.25 USD | 310,298.99 USD | 217,264.26 USD | 93,034.72 USD | `+17.63%` | `19B / 3S` |
| `0:00 UTC` | `0.1063` | `0.1047` | `0.1063` | `0.1088` | `0.1013` | 5,548,996.22 USD | 2,272,459.88 USD | 3,276,536.35 USD | -1,004,076.47 USD | `-18.09%` | `5B / 37S` |
| `5:00 UTC` | `0.1014` | `0.1013` | `0.1014` | `0.1029` | `0.0990` | 5,717,098.88 USD | 2,672,854.06 USD | 3,044,244.81 USD | -371,390.75 USD | `-6.50%` | `7B / 23S` |
| `0:00 UTC` | `0.1014` | `0.1015` | `0.1014` | `0.1023` | `0.1007` | 622,495.35 USD | 333,527.11 USD | 288,968.24 USD | 44,558.87 USD | `+7.16%` | `36B / 17S` |

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
| `5m` | 150,950.00 USD | 45,330.00 USD | **`ACCUMULATION`** |
| `15m` | 142,270.00 USD | -109,920.00 USD | **`ACCUMULATION`** |
| `30m` | -306,000.00 USD | -2,730,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -180,340.00 USD | -2,710,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -302,980.00 USD | -2,830,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -361,770.00 USD | -3,240,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -314,090.00 USD | -3,240,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -181,380.00 USD | -2,730,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -86,380.00 USD | -2,670,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -233,360.00 USD | -4,990,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -415,000.00 USD | -12,730,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,840,000.00 USD | -81,570,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+150.95K` | 15m=`+142.27K` | 1h=`-180.34K` | 24h=`-233.36K`
* Futures Capital Netflows: 5m=`+45.33K` | 15m=`-109.92K` | 1h=`-2.71M` | 24h=`-4.99M`
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
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:30:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
