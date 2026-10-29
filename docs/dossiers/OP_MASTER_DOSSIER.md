# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 04:22:52 IST` (`2026-10-29 22:52:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1022` | `0.1026` | `0.1020` | `0.1025` | `2,109,143` | 215,736.85 USD | 21,955.81 USD | `+10.18%` | -2,810,175.94 USD | `+0.41` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1024` | `0.1029` | `0.1021` | `0.1022` | `2,612,901` | 267,801.21 USD | 63,186.15 USD | `+23.59%` | -2,746,989.79 USD | `+1.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1022` | `0.1027` | `0.1019` | `0.1025` | `2,341,813` | 239,557.33 USD | 120.91 USD | `+0.05%` | -2,746,868.88 USD | `+0.05` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1018` | `0.1023` | `0.1003` | `0.1014` | `9,565,551` | 969,689.66 USD | -62,055.28 USD | `-6.40%` | -2,883,324.62 USD | `+0.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1014` | `0.1029` | `0.1009` | `0.1022` | `7,067,788` | 722,088.27 USD | 158,302.78 USD | `+21.92%` | -2,725,021.84 USD | `+0.96` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1022` | `0.1027` | `0.1019` | `0.1026` | `2,351,708` | 240,572.63 USD | 654.23 USD | `+0.27%` | -2,724,367.61 USD | `+0.31` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `136,699,709` | 14,218,772.66 USD | -1,614,985.67 USD | `-11.36%` | -2,750,784.93 USD | `-3.57` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1012` | `0.1044` | `0.1007` | `0.1018` | `43,149,466` | 4,433,523.07 USD | -89,220.85 USD | `-2.01%` | -2,840,005.78 USD | `+0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1018` | `0.1029` | `0.1003` | `0.1025` | `18,974,916` | 1,931,311.08 USD | 96,392.60 USD | `+4.99%` | -2,743,613.18 USD | `+0.45` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -935,828.18 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | -1,111,968.46 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1025` | `198,824,326` | 20,583,630.99 USD | -1,607,838.11 USD | `-7.81%` | -2,719,806.57 USD | `-1.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1085` | `0.1106` | `0.1071` | `0.1076` | `47,048,931` | 5,111,570.05 USD | 108,567.99 USD | `+2.12%` | -1,419,806.61 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,277,083.78 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -935,828.18 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | -1,111,968.46 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1025` | `198,824,326` | 20,583,630.99 USD | -1,607,838.11 USD | `-7.81%` | -2,719,806.57 USD | `-1.44` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:16:04 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1100` | 5,889.99 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale BUY: 5.89K USD at 0.1100 USD [API] | `2026-10-28 14:48:40` |
| `ANNOUNCEMENT` | `INFO` | `0.1096` | 6,503.12 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 6.50K USD at 0.1096 USD [API] | `2026-10-28 17:22:10` |
| `ANNOUNCEMENT` | `INFO` | `0.1122` | 5,004.01 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale BUY: 5.00K USD at 0.1122 USD [API] | `2026-10-28 18:57:46` |


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
| `Live` | `Long Liquidation` | `0.0385` | 231.00 USD | 199,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0435` | 196.55 USD | 198,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0475` | 2,650.00 USD | 198,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 417.68 USD | 195,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 4,840.00 USD | 195,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 1,100.00 USD | 190,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 682.69 USD | 189,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 518.48 USD | 188,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 1,920.00 USD | 188,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 23,910.00 USD | 186,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,300.00 USD | 162,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 1,020.00 USD | 160,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 2,710.00 USD | 159,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 44,690.00 USD | 156,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 1,320.00 USD | 111,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 223.98 USD | 110,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 1,560.00 USD | 110,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0878` | 1,160,000.00 USD | 1,160,000.00 USD | 1,370.00 USD | 4,930.00 USD | 27,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0881` | 1,130,000.00 USD | 1,130,000.00 USD | 3,770.00 USD | 2,660.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0884` | 1,110,000.00 USD | 1,110,000.00 USD | 7,040.00 USD | 4,640.00 USD | 11,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0887` | 1,090,000.00 USD | 1,090,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0890` | 1,050,000.00 USD | 1,050,000.00 USD | 14,610.00 USD | 4,470.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0893` | 1,030,000.00 USD | 1,030,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,270.00 USD | 108,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0896` | 1,010,000.00 USD | 1,010,000.00 USD | 5,760.00 USD | 611.80 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0899` | 995,980.00 USD | 995,980.00 USD | 3,390.00 USD | 927.82 USD | 4,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0900` | 765,190.00 USD | 765,190.00 USD | 1,560.00 USD | 0.00 USD | 293.66 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0902` | 763,340.00 USD | 763,340.00 USD | 893.87 USD | 914.96 USD | 4.26 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0902` | 987,170.00 USD | 987,170.00 USD | 2,270.00 USD | 910.78 USD | 1,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0904` | 761,520.00 USD | 761,520.00 USD | 831.11 USD | 1,720.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0905` | 982,780.00 USD | 982,780.00 USD | 10,350.00 USD | 996.61 USD | 4,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0905` | 1,440.00 USD | 105,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0906` | 756,950.00 USD | 756,950.00 USD | 2,000.00 USD | 1,460.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0908` | 750,890.00 USD | 750,890.00 USD | 707.85 USD | 0.00 USD | 1,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0908` | 967,350.00 USD | 967,350.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0910` | 749,150.00 USD | 749,150.00 USD | 6,520.00 USD | 363.17 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0911` | 955,950.00 USD | 955,950.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0912` | 742,270.00 USD | 742,270.00 USD | 0.00 USD | 1,450.00 USD | 787.79 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0914` | 740,030.00 USD | 740,030.00 USD | 0.00 USD | 944.94 USD | 51.31 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0914` | 952,670.00 USD | 952,670.00 USD | 1,670.00 USD | 903.90 USD | 45.81 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0916` | 739,040.00 USD | 739,040.00 USD | 6,590.00 USD | 0.00 USD | 2.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0917` | 950,050.00 USD | 950,050.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0918` | 732,450.00 USD | 732,450.00 USD | 3,850.00 USD | 0.00 USD | 2,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0920` | 726,080.00 USD | 726,080.00 USD | 3,690.00 USD | 504.78 USD | 2,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0922` | 719,310.00 USD | 719,310.00 USD | 0.00 USD | 750.63 USD | 62.82 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0923` | 942,040.00 USD | 942,040.00 USD | 0.00 USD | 0.00 USD | 10,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0924` | 718,500.00 USD | 718,500.00 USD | 1,410.00 USD | 518.97 USD | 14,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0925` | 128.61 USD | 104,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0926` | 702,170.00 USD | 702,170.00 USD | 3,270.00 USD | 1,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0926` | 931,480.00 USD | 931,480.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0932` | 921,510.00 USD | 921,510.00 USD | 0.00 USD | 0.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0934` | 697,250.00 USD | 697,250.00 USD | 0.00 USD | 0.00 USD | 6,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0935` | 909,270.00 USD | 909,270.00 USD | 0.00 USD | 1,320.00 USD | 6,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0938` | 690,390.00 USD | 690,390.00 USD | 0.00 USD | 0.00 USD | 141.01 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0938` | 901,460.00 USD | 901,460.00 USD | 0.00 USD | 0.00 USD | 8.57 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0941` | 901,450.00 USD | 901,450.00 USD | 2,050.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0944` | 896,380.00 USD | 896,380.00 USD | 1,870.00 USD | 0.00 USD | 7,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0945` | 69,120.00 USD | 103,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0947` | 886,990.00 USD | 886,990.00 USD | 3,790.00 USD | 1,810.00 USD | 112.06 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0948` | 690,250.00 USD | 690,250.00 USD | 0.00 USD | 0.00 USD | 69.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0950` | 881,270.00 USD | 881,270.00 USD | 3,770.00 USD | 0.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0953` | 870,840.00 USD | 870,840.00 USD | 0.00 USD | 0.00 USD | 4.65 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0954` | 690,180.00 USD | 690,180.00 USD | 0.00 USD | 0.00 USD | 154.48 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0955` | 1,910.00 USD | 34,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0956` | 690,020.00 USD | 690,020.00 USD | 0.00 USD | 1,180.00 USD | 166.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0959` | 870,830.00 USD | 870,830.00 USD | 0.00 USD | 0.00 USD | 115.48 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0962` | 688,670.00 USD | 688,670.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0962` | 870,720.00 USD | 870,720.00 USD | 0.00 USD | 0.00 USD | 121.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0964` | 686,590.00 USD | 686,590.00 USD | 0.00 USD | 0.00 USD | 107.13 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0965` | 966.47 USD | 32,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0966` | 686,490.00 USD | 686,490.00 USD | 2,140.00 USD | 715.37 USD | 6,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0968` | 677,450.00 USD | 677,450.00 USD | 6,400.00 USD | 2,400.00 USD | 11,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0968` | 870,600.00 USD | 870,600.00 USD | 7,490.00 USD | 3,720.00 USD | 11,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0970` | 657,370.00 USD | 657,370.00 USD | 1,290.00 USD | 2,860.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 847,760.00 USD | 847,760.00 USD | 0.00 USD | 3,760.00 USD | 9,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0972` | 648,990.00 USD | 648,990.00 USD | 14,810.00 USD | 5,180.00 USD | 2,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0974` | 626,050.00 USD | 626,050.00 USD | 2,750.00 USD | 3,220.00 USD | 2,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0974` | 834,280.00 USD | 834,280.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0975` | 11,950.00 USD | 31,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0976` | 617,330.00 USD | 617,330.00 USD | 18,450.00 USD | 1,990.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0977` | 830,000.00 USD | 830,000.00 USD | 0.00 USD | 1,160.00 USD | 28,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0978` | 589,420.00 USD | 589,420.00 USD | 22,180.00 USD | 1,470.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0980` | 556,460.00 USD | 556,460.00 USD | 9,220.00 USD | 3,070.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0980` | 800,040.00 USD | 800,040.00 USD | 0.00 USD | 3,920.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0982` | 533,670.00 USD | 533,670.00 USD | 1,840.00 USD | 3,990.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 790,410.00 USD | 790,410.00 USD | 7,990.00 USD | 1,230.00 USD | 14,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0984` | 513,650.00 USD | 513,650.00 USD | 10,600.00 USD | 460.32 USD | 18,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0985` | 19,960.00 USD | 19,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0986` | 483,790.00 USD | 483,790.00 USD | 10,070.00 USD | 5,230.00 USD | 32,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0986` | 766,410.00 USD | 766,410.00 USD | 7,110.00 USD | 7,530.00 USD | 61,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0988` | 435,950.00 USD | 435,950.00 USD | 12,770.00 USD | 6,260.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 690,760.00 USD | 690,760.00 USD | 17,640.00 USD | 6,190.00 USD | 53,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0990` | 413,250.00 USD | 413,250.00 USD | 3,980.00 USD | 3,340.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0992` | 403,360.00 USD | 403,360.00 USD | 29,370.00 USD | 5,050.00 USD | 7,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0992` | 613,730.00 USD | 613,730.00 USD | 27,140.00 USD | 11,490.00 USD | 28,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0994` | 361,110.00 USD | 361,110.00 USD | 10,240.00 USD | 3,150.00 USD | 9,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 546,600.00 USD | 546,600.00 USD | 24,220.00 USD | 15,150.00 USD | 56,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0996` | 337,900.00 USD | 337,900.00 USD | 2,640.00 USD | 3,020.00 USD | 28,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0998` | 303,960.00 USD | 303,960.00 USD | 35,620.00 USD | 1,690.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0998` | 450,680.00 USD | 450,680.00 USD | 28,450.00 USD | 6,400.00 USD | 80,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1000` | 247,240.00 USD | 247,240.00 USD | 42,490.00 USD | 3,370.00 USD | 26,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 335,110.00 USD | 335,110.00 USD | 36,110.00 USD | 8,650.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1002` | 175,160.00 USD | 175,160.00 USD | 21,100.00 USD | 4,620.00 USD | 17,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1004` | 132,180.00 USD | 132,180.00 USD | 1,970.00 USD | 5,260.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1004` | 277,220.00 USD | 277,220.00 USD | 22,470.00 USD | 16,470.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1006` | 111,000.00 USD | 111,000.00 USD | 16,470.00 USD | 5,640.00 USD | 72,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 214,850.00 USD | 214,850.00 USD | 20,870.00 USD | 3,870.00 USD | 100,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1008` | 16,130.00 USD | 16,130.00 USD | 0.00 USD | 8,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1010` | 7,420.00 USD | 7,420.00 USD | 0.00 USD | 0.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1010` | 89,880.00 USD | 89,880.00 USD | 17,340.00 USD | 6,580.00 USD | 6,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1012` | 4,970.00 USD | 4,970.00 USD | 0.00 USD | 0.00 USD | 939.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 59,330.00 USD | 59,330.00 USD | 15,270.00 USD | 5,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1014` | 4,030.00 USD | 4,030.00 USD | 0.00 USD | 0.00 USD | 587.32 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1016` | 3,440.00 USD | 3,440.00 USD | 0.00 USD | 2,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1016` | 38,830.00 USD | 38,830.00 USD | 15,440.00 USD | 5,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1018` | 897.78 USD | 897.78 USD | 0.00 USD | 897.78 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1019` | 17,890.00 USD | 17,890.00 USD | 12,100.00 USD | 5,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1022` | 20,180.00 USD | 20,180.00 USD | 11,930.00 USD | 8,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1025` | 21,740.00 USD | 21,740.00 USD | 1,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1028` | 29,930.00 USD | 29,930.00 USD | 3,800.00 USD | 4,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1030` | 11,070.00 USD | 11,070.00 USD | 0.00 USD | 0.00 USD | 11,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1031` | 55,750.00 USD | 55,750.00 USD | 19,560.00 USD | 6,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1032` | 62,990.00 USD | 62,990.00 USD | 27,910.00 USD | 3,360.00 USD | 20,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1034` | 79,840.00 USD | 79,840.00 USD | 5,500.00 USD | 2,330.00 USD | 9,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1034` | 81,690.00 USD | 81,690.00 USD | 18,920.00 USD | 7,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1036` | 97,980.00 USD | 97,980.00 USD | 6,930.00 USD | 11,150.00 USD | 54.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1037` | 89,410.00 USD | 89,410.00 USD | 2,710.00 USD | 5,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1038` | 142,560.00 USD | 142,560.00 USD | 35,160.00 USD | 9,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1040` | 174,490.00 USD | 174,490.00 USD | 6,500.00 USD | 12,880.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1040` | 137,010.00 USD | 137,010.00 USD | 5,940.00 USD | 10,300.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1042` | 201,250.00 USD | 201,250.00 USD | 0.00 USD | 9,490.00 USD | 17,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1043` | 158,960.00 USD | 158,960.00 USD | 15,960.00 USD | 5,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1044` | 215,620.00 USD | 215,620.00 USD | 0.00 USD | 14,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1046` | 248,460.00 USD | 248,460.00 USD | 7,060.00 USD | 1,080.00 USD | 24,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1046` | 228,930.00 USD | 228,930.00 USD | 0.00 USD | 9,810.00 USD | 60,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1048` | 365,610.00 USD | 365,610.00 USD | 27,930.00 USD | 9,140.00 USD | 80,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1049` | 353,350.00 USD | 353,350.00 USD | 34,790.00 USD | 6,530.00 USD | 83,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1050` | 422,370.00 USD | 422,370.00 USD | 35,330.00 USD | 10,740.00 USD | 10,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1052` | 526,440.00 USD | 526,440.00 USD | 43,830.00 USD | 12,940.00 USD | 47,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1052` | 531,120.00 USD | 531,120.00 USD | 28,200.00 USD | 24,160.00 USD | 125,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1054` | 678,440.00 USD | 678,440.00 USD | 59,720.00 USD | 20,100.00 USD | 72,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1055` | 909,850.00 USD | 909,850.00 USD | 122,840.00 USD | 44,430.00 USD | 211,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1056` | 775,010.00 USD | 775,010.00 USD | 25,000.00 USD | 27,390.00 USD | 44,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1058` | 883,620.00 USD | 883,620.00 USD | 30,300.00 USD | 0.00 USD | 78,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1058` | 1,260,000.00 USD | 1,260,000.00 USD | 105,620.00 USD | 53,680.00 USD | 189,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1060` | 983,260.00 USD | 983,260.00 USD | 44,890.00 USD | 0.00 USD | 54,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1061` | 1,520,000.00 USD | 1,520,000.00 USD | 75,540.00 USD | 72,260.00 USD | 118,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1062` | 1,090,000.00 USD | 1,090,000.00 USD | 28,640.00 USD | 2,030.00 USD | 78,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1064` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 2,630.00 USD | 51,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1064` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 52,580.00 USD | 192,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1066` | 1,180,000.00 USD | 1,180,000.00 USD | 3,530.00 USD | 0.00 USD | 31,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1067` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 51,740.00 USD | 156,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1068` | 1,240,000.00 USD | 1,240,000.00 USD | 4,700.00 USD | 2,620.00 USD | 55,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1070` | 1,310,000.00 USD | 1,310,000.00 USD | 8,170.00 USD | 7,280.00 USD | 51,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1070` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 57,770.00 USD | 134,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1072` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 236.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1073` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 17,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1074` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 104.27 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1076` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 153.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1076` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 22,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1078` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 17,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1079` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 79.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1082` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 5,910.00 USD | 21.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1082` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 89.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1084` | 1,380,000.00 USD | 1,380,000.00 USD | 7,990.00 USD | 0.00 USD | 35,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1085` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1086` | 1,460,000.00 USD | 1,460,000.00 USD | 4,220.00 USD | 2,240.00 USD | 72,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1088` | 1,510,000.00 USD | 1,510,000.00 USD | 44,230.00 USD | 0.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1088` | 2,220,000.00 USD | 2,220,000.00 USD | 5,290.00 USD | 0.00 USD | 113.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1090` | 1,560,000.00 USD | 1,560,000.00 USD | 44,990.00 USD | 0.00 USD | 124.57 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1091` | 2,240,000.00 USD | 2,240,000.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1092` | 1,570,000.00 USD | 1,570,000.00 USD | 10,290.00 USD | 0.00 USD | 29.91 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1094` | 1,590,000.00 USD | 1,590,000.00 USD | 13,100.00 USD | 0.00 USD | 14,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1094` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1096` | 1,610,000.00 USD | 1,610,000.00 USD | 4,110.00 USD | 1,890.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1097` | 2,270,000.00 USD | 2,270,000.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1098` | 1,650,000.00 USD | 1,650,000.00 USD | 13,380.00 USD | 3,910.00 USD | 22,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1100` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 2,820.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1100` | 2,300,000.00 USD | 2,300,000.00 USD | 11,470.00 USD | 0.00 USD | 21,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1102` | 1,660,000.00 USD | 1,660,000.00 USD | 4,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 2,340,000.00 USD | 2,340,000.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1104` | 1,680,000.00 USD | 1,680,000.00 USD | 6,920.00 USD | 10,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1106` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 12,720.00 USD | 30,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1106` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 22,880.00 USD | 16,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1108` | 1,740,000.00 USD | 1,740,000.00 USD | 5,220.00 USD | 1,120.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1112` | 1,750,000.00 USD | 1,750,000.00 USD | 10,780.00 USD | 0.00 USD | 96.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1112` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1114` | 1,810,000.00 USD | 1,810,000.00 USD | 15,810.00 USD | 5,880.00 USD | 39,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1116` | 1,840,000.00 USD | 1,840,000.00 USD | 4,760.00 USD | 12,550.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1118` | 1,940,000.00 USD | 1,940,000.00 USD | 25,510.00 USD | 20,030.00 USD | 57,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1118` | 2,490,000.00 USD | 2,490,000.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1120` | 1,990,000.00 USD | 1,990,000.00 USD | 27,100.00 USD | 8,540.00 USD | 9,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 2,550,000.00 USD | 2,550,000.00 USD | 17,760.00 USD | 0.00 USD | 38,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1122` | 2,030,000.00 USD | 2,030,000.00 USD | 22,700.00 USD | 4,480.00 USD | 15,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1124` | 2,060,000.00 USD | 2,060,000.00 USD | 17,850.00 USD | 6,120.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1124` | 2,650,000.00 USD | 2,650,000.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1126` | 2,100,000.00 USD | 2,100,000.00 USD | 9,370.00 USD | 11,410.00 USD | 17,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1127` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1128` | 2,120,000.00 USD | 2,120,000.00 USD | 10,120.00 USD | 0.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1130` | 2,150,000.00 USD | 2,150,000.00 USD | 7,970.00 USD | 2,000.00 USD | 16,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1130` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 24,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1132` | 2,200,000.00 USD | 2,200,000.00 USD | 19,390.00 USD | 18,950.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 2,720,000.00 USD | 2,720,000.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1134` | 2,230,000.00 USD | 2,230,000.00 USD | 4,040.00 USD | 12,980.00 USD | 13,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1136` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 787.70 USD | 4,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1136` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1138` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 856.93 USD | 14,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1139` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1140` | 2,260,000.00 USD | 2,260,000.00 USD | 7,800.00 USD | 0.00 USD | 6,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1142` | 2,330,000.00 USD | 2,330,000.00 USD | 24,760.00 USD | 17,100.00 USD | 22,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1142` | 2,760,000.00 USD | 2,760,000.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1144` | 2,390,000.00 USD | 2,390,000.00 USD | 9,940.00 USD | 21,970.00 USD | 31,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 3,000,000.00 USD | 3,000,000.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1146` | 2,440,000.00 USD | 2,440,000.00 USD | 5,090.00 USD | 10,830.00 USD | 30,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1148` | 2,510,000.00 USD | 2,510,000.00 USD | 33,430.00 USD | 3,280.00 USD | 30,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1148` | 3,190,000.00 USD | 3,190,000.00 USD | 9,880.00 USD | 0.00 USD | 176,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1150` | 2,560,000.00 USD | 2,560,000.00 USD | 19,260.00 USD | 13,020.00 USD | 21,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 3,460,000.00 USD | 3,460,000.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1152` | 2,670,000.00 USD | 2,670,000.00 USD | 34,520.00 USD | 17,470.00 USD | 59,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1153` | 2,710,000.00 USD | 2,710,000.00 USD | 6,400.00 USD | 7,760.00 USD | 23,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1154` | 3,930,000.00 USD | 3,930,000.00 USD | 243,190.00 USD | 26,970.00 USD | 195,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 4,240,000.00 USD | 4,240,000.00 USD | 188,950.00 USD | 25,290.00 USD | 98,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1160` | 4,520,000.00 USD | 4,520,000.00 USD | 139,350.00 USD | 32,830.00 USD | 109,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 4,800,000.00 USD | 4,800,000.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1166` | 5,020,000.00 USD | 5,020,000.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 5,240,000.00 USD | 5,240,000.00 USD | 82,770.00 USD | 26,150.00 USD | 112,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1172` | 5,370,000.00 USD | 5,370,000.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 5,540,000.00 USD | 5,540,000.00 USD | 72,770.00 USD | 17,930.00 USD | 81,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1178` | 5,710,000.00 USD | 5,710,000.00 USD | 89,510.00 USD | 23,660.00 USD | 55,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 5,800,000.00 USD | 5,800,000.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1184` | 5,860,000.00 USD | 5,860,000.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 5,940,000.00 USD | 5,940,000.00 USD | 5,620.00 USD | 17,120.00 USD | 54,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1190` | 6,090,000.00 USD | 6,090,000.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 6,170,000.00 USD | 6,170,000.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1196` | 6,230,000.00 USD | 6,230,000.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 6,320,000.00 USD | 6,320,000.00 USD | 9,100.00 USD | 13,190.00 USD | 67,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1202` | 6,510,000.00 USD | 6,510,000.00 USD | 138,430.00 USD | 21,430.00 USD | 32,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 6,850,000.00 USD | 6,850,000.00 USD | 132,960.00 USD | 72,910.00 USD | 130,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1208` | 6,980,000.00 USD | 6,980,000.00 USD | 39,480.00 USD | 25,720.00 USD | 66,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 7,190,000.00 USD | 7,190,000.00 USD | 72,500.00 USD | 25,920.00 USD | 111,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1214` | 7,310,000.00 USD | 7,310,000.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 7,360,000.00 USD | 7,360,000.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1220` | 7,470,000.00 USD | 7,470,000.00 USD | 45,700.00 USD | 10,970.00 USD | 54,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 7,620,000.00 USD | 7,620,000.00 USD | 76,930.00 USD | 24,740.00 USD | 45,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 9,820.00 USD | 9,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1226` | 7,700,000.00 USD | 7,700,000.00 USD | 54,940.00 USD | 27,490.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 7,890,000.00 USD | 7,890,000.00 USD | 71,850.00 USD | 38,040.00 USD | 79,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1232` | 8,060,000.00 USD | 8,060,000.00 USD | 67,800.00 USD | 28,560.00 USD | 68,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1235` | 8,100,000.00 USD | 8,100,000.00 USD | 15,040.00 USD | 5,390.00 USD | 17,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1238` | 8,110,000.00 USD | 8,110,000.00 USD | 8,310.00 USD | 3,610.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1241` | 8,130,000.00 USD | 8,130,000.00 USD | 11,380.00 USD | 1,380.00 USD | 7,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1244` | 8,170,000.00 USD | 8,170,000.00 USD | 26,540.00 USD | 8,130.00 USD | 9,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1247` | 8,210,000.00 USD | 8,210,000.00 USD | 7,900.00 USD | 12,590.00 USD | 15,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1250` | 8,230,000.00 USD | 8,230,000.00 USD | 8,540.00 USD | 4,990.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1253` | 8,250,000.00 USD | 8,250,000.00 USD | 1,550.00 USD | 0.00 USD | 16,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1256` | 8,270,000.00 USD | 8,270,000.00 USD | 11,990.00 USD | 11,420.00 USD | 220.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1259` | 8,280,000.00 USD | 8,280,000.00 USD | 5,870.00 USD | 1,190.00 USD | 121.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1262` | 8,290,000.00 USD | 8,290,000.00 USD | 4,270.00 USD | 0.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1265` | 8,300,000.00 USD | 8,300,000.00 USD | 2,710.00 USD | 0.00 USD | 7,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1268` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1271` | 8,300,000.00 USD | 8,300,000.00 USD | 5,940.00 USD | 0.00 USD | 30.15 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1274` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 12.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1277` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 20.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1280` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 0.00 USD | 6,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1335` | 210.10 USD | 10,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1355` | 1,330.00 USD | 11,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1495` | 24,560.00 USD | 35,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1525` | 6,090.00 USD | 42,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1565` | 16,200.00 USD | 58,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1695` | 169.25 USD | 58,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1865` | 367.78 USD | 58,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2005` | 969.16 USD | 59,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0385` | 199,050.00 USD | 0.00 USD | 231.00 USD | `-62.21%` | `6,000.00` |
| `Live` | `Long` | `0.0435` | 198,820.00 USD | 0.00 USD | 196.55 USD | `-57.30%` | `4,518.50` |
| `Live` | `Long` | `0.0475` | 198,620.00 USD | 0.00 USD | 2,650.00 USD | `-53.38%` | `55,786.40` |
| `Live` | `Long` | `0.0545` | 195,970.00 USD | 0.00 USD | 417.68 USD | `-46.51%` | `7,663.80` |
| `Live` | `Long` | `0.0575` | 195,550.00 USD | 0.00 USD | 4,840.00 USD | `-43.56%` | `84,219.50` |
| `Live` | `Long` | `0.0615` | 190,710.00 USD | 0.00 USD | 1,100.00 USD | `-39.63%` | `17,943.80` |
| `Live` | `Long` | `0.0645` | 189,610.00 USD | 0.00 USD | 682.69 USD | `-36.69%` | `10,584.30` |
| `Live` | `Long` | `0.0675` | 188,920.00 USD | 0.00 USD | 518.48 USD | `-33.75%` | `7,681.20` |
| `Live` | `Long` | `0.0685` | 188,400.00 USD | 0.00 USD | 1,920.00 USD | `-32.76%` | `28,000.00` |
| `Live` | `Long` | `0.0725` | 186,490.00 USD | 0.00 USD | 23,910.00 USD | `-28.84%` | `329,855.60` |
| `Live` | `Long` | `0.0745` | 162,570.00 USD | 0.00 USD | 2,300.00 USD | `-26.87%` | `30,851.90` |
| `Live` | `Long` | `0.0755` | 160,270.00 USD | 0.00 USD | 1,020.00 USD | `-25.89%` | `13,481.90` |
| `Live` | `Long` | `0.0765` | 159,260.00 USD | 0.00 USD | 2,710.00 USD | `-24.91%` | `35,396.30` |
| `Live` | `Long` | `0.0775` | 156,550.00 USD | 0.00 USD | 44,690.00 USD | `-23.93%` | `576,624.50` |
| `Live` | `Long` | `0.0795` | 111,860.00 USD | 0.00 USD | 1,320.00 USD | `-21.97%` | `16,641.80` |
| `Live` | `Long` | `0.0805` | 110,540.00 USD | 0.00 USD | 223.98 USD | `-20.99%` | `2,782.40` |
| `Live` | `Long` | `0.0815` | 110,310.00 USD | 0.00 USD | 1,560.00 USD | `-20.00%` | `19,181.40` |
| `Live` | `Long` | `0.0895` | 108,750.00 USD | 0.00 USD | 3,270.00 USD | `-12.15%` | `36,561.80` |
| `Live` | `Long` | `0.0905` | 105,480.00 USD | 0.00 USD | 1,440.00 USD | `-11.17%` | `15,952.80` |
| `Live` | `Long` | `0.0925` | 104,030.00 USD | 0.00 USD | 128.61 USD | `-9.21%` | `1,390.40` |
| `Live` | `Long` | `0.0945` | 103,900.00 USD | 0.00 USD | 69,120.00 USD | `-7.24%` | `731,405.60` |
| `Live` | `Long` | `0.0955` | 34,790.00 USD | 0.00 USD | 1,910.00 USD | `-6.26%` | `20,000.00` |
| `Live` | `Long` | `0.0965` | 32,880.00 USD | 0.00 USD | 966.47 USD | `-5.28%` | `10,015.20` |
| `Live` | `Long` | `0.0975` | 31,910.00 USD | 0.00 USD | 11,950.00 USD | `-4.30%` | `122,573.60` |
| `Live` | `Long` | `0.0985` | 19,960.00 USD | 0.00 USD | 19,960.00 USD | `-3.32%` | `202,627.30` |
| `Live` | `Short` | `0.1225` | 9,820.00 USD | 9,820.00 USD | 0.00 USD | `+20.24%` | `80,129.90` |
| `Live` | `Short` | `0.1335` | 10,030.00 USD | 210.10 USD | 0.00 USD | `+31.04%` | `1,573.80` |
| `Live` | `Short` | `0.1355` | 11,360.00 USD | 1,330.00 USD | 0.00 USD | `+33.00%` | `9,843.80` |
| `Live` | `Short` | `0.1495` | 35,920.00 USD | 24,560.00 USD | 0.00 USD | `+46.74%` | `164,254.10` |
| `Live` | `Short` | `0.1525` | 42,010.00 USD | 6,090.00 USD | 0.00 USD | `+49.69%` | `39,929.50` |
| `Live` | `Short` | `0.1565` | 58,210.00 USD | 16,200.00 USD | 0.00 USD | `+53.61%` | `103,518.70` |
| `Live` | `Short` | `0.1695` | 58,380.00 USD | 169.25 USD | 0.00 USD | `+66.37%` | `998.50` |
| `Live` | `Short` | `0.1865` | 58,740.00 USD | 367.78 USD | 0.00 USD | `+83.06%` | `1,972.00` |
| `Live` | `Short` | `0.2005` | 59,710.00 USD | 969.16 USD | 0.00 USD | `+96.80%` | `4,833.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0635` | 13,890.00 USD | 0.00 USD | 1,140.00 USD | `-37.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 12,750.00 USD | 0.00 USD | 773.46 USD | `-30.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 11,980.00 USD | 0.00 USD | 592.27 USD | `-29.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 11,380.00 USD | 0.00 USD | 755.00 USD | `-25.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0805` | 10,630.00 USD | 0.00 USD | 411.06 USD | `-20.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0815` | 10,220.00 USD | 0.00 USD | 285.01 USD | `-20.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0835` | 9,930.00 USD | 0.00 USD | 456.70 USD | `-18.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 9,480.00 USD | 0.00 USD | 631.58 USD | `-16.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 8,850.00 USD | 0.00 USD | 653.74 USD | `-13.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 8,190.00 USD | 0.00 USD | 444.62 USD | `-11.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0915` | 7,750.00 USD | 0.00 USD | 1,460.00 USD | `-10.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 6,280.00 USD | 0.00 USD | 485.13 USD | `-7.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0975` | 5,800.00 USD | 0.00 USD | 985.89 USD | `-4.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0985` | 4,810.00 USD | 0.00 USD | 931.75 USD | `-3.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0995` | 3,880.00 USD | 0.00 USD | 801.64 USD | `-2.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 3,080.00 USD | 0.00 USD | 2,180.00 USD | `-1.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1015` | 903.42 USD | 0.00 USD | 903.42 USD | `-0.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1025` | 780.70 USD | 780.70 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1035` | 5,430.00 USD | 4,650.00 USD | 0.00 USD | `+1.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 24,380.00 USD | 18,950.00 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 32,150.00 USD | 7,770.00 USD | 0.00 USD | `+3.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 141,430.00 USD | 109,280.00 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1075` | 163,340.00 USD | 21,900.00 USD | 0.00 USD | `+5.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1085` | 163,490.00 USD | 150.04 USD | 0.00 USD | `+6.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1095` | 164,120.00 USD | 639.36 USD | 0.00 USD | `+7.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 164,290.00 USD | 162.59 USD | 0.00 USD | `+8.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 165,130.00 USD | 839.64 USD | 0.00 USD | `+9.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1125` | 165,910.00 USD | 786.65 USD | 0.00 USD | `+10.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1135` | 166,030.00 USD | 116.27 USD | 0.00 USD | `+11.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1145` | 166,160.00 USD | 134.61 USD | 0.00 USD | `+12.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 166,300.00 USD | 137.71 USD | 0.00 USD | `+13.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1165` | 166,480.00 USD | 180.81 USD | 0.00 USD | `+14.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1175` | 166,850.00 USD | 363.49 USD | 0.00 USD | `+15.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1185` | 167,900.00 USD | 1,050.00 USD | 0.00 USD | `+16.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1195` | 182,540.00 USD | 14,640.00 USD | 0.00 USD | `+17.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1205` | 182,930.00 USD | 398.42 USD | 0.00 USD | `+18.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1225` | 183,910.00 USD | 980.00 USD | 0.00 USD | `+20.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1235` | 196,260.00 USD | 12,350.00 USD | 0.00 USD | `+21.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1255` | 200,640.00 USD | 4,380.00 USD | 0.00 USD | `+23.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1275` | 201,130.00 USD | 492.06 USD | 0.00 USD | `+25.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1305` | 201,580.00 USD | 444.24 USD | 0.00 USD | `+28.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1315` | 233,140.00 USD | 31,560.00 USD | 0.00 USD | `+29.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1335` | 234,450.00 USD | 1,310.00 USD | 0.00 USD | `+31.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1345` | 238,600.00 USD | 4,150.00 USD | 0.00 USD | `+32.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1365` | 246,190.00 USD | 7,590.00 USD | 0.00 USD | `+33.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1405` | 259,300.00 USD | 13,110.00 USD | 0.00 USD | `+37.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1425` | 259,400.00 USD | 102.22 USD | 0.00 USD | `+39.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1435` | 266,580.00 USD | 7,180.00 USD | 0.00 USD | `+40.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1485` | 269,220.00 USD | 2,650.00 USD | 0.00 USD | `+45.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1495` | 270,020.00 USD | 792.53 USD | 0.00 USD | `+46.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1525` | 273,780.00 USD | 3,770.00 USD | 0.00 USD | `+49.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 273,970.00 USD | 184.49 USD | 0.00 USD | `+52.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 276,780.00 USD | 2,810.00 USD | 0.00 USD | `+53.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 277,000.00 USD | 219.81 USD | 0.00 USD | `+54.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 277,270.00 USD | 277.62 USD | 0.00 USD | `+60.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 279,070.00 USD | 1,800.00 USD | 0.00 USD | `+66.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 279,280.00 USD | 216.55 USD | 0.00 USD | `+71.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 279,400.00 USD | 117.26 USD | 0.00 USD | `+93.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 299,940.00 USD | 20,530.00 USD | 0.00 USD | `+96.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 300,120.00 USD | 189.30 USD | 0.00 USD | `+99.74%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0878` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 1,370.00 USD | 4,930.00 USD | 27,260.00 USD |
| `7D` | `0.0881` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 3,770.00 USD | 2,660.00 USD | 12,940.00 USD |
| `7D` | `0.0884` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 7,040.00 USD | 4,640.00 USD | 11,870.00 USD |
| `7D` | `0.0887` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD |
| `7D` | `0.0890` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 14,610.00 USD | 4,470.00 USD | 3,680.00 USD |
| `7D` | `0.0893` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD |
| `7D` | `0.0896` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 5,760.00 USD | 611.80 USD | 6,870.00 USD |
| `7D` | `0.0899` | 995,980.00 USD | 0.00 USD | 995,980.00 USD | 3,390.00 USD | 927.82 USD | 4,490.00 USD |
| `1D` | `0.0900` | 765,190.00 USD | 0.00 USD | 765,190.00 USD | 1,560.00 USD | 0.00 USD | 293.66 USD |
| `1D` | `0.0902` | 763,340.00 USD | 0.00 USD | 763,340.00 USD | 893.87 USD | 914.96 USD | 4.26 USD |
| `7D` | `0.0902` | 987,170.00 USD | 0.00 USD | 987,170.00 USD | 2,270.00 USD | 910.78 USD | 1,210.00 USD |
| `1D` | `0.0904` | 761,520.00 USD | 0.00 USD | 761,520.00 USD | 831.11 USD | 1,720.00 USD | 2,030.00 USD |
| `7D` | `0.0905` | 982,780.00 USD | 0.00 USD | 982,780.00 USD | 10,350.00 USD | 996.61 USD | 4,080.00 USD |
| `1D` | `0.0906` | 756,950.00 USD | 0.00 USD | 756,950.00 USD | 2,000.00 USD | 1,460.00 USD | 2,610.00 USD |
| `1D` | `0.0908` | 750,890.00 USD | 0.00 USD | 750,890.00 USD | 707.85 USD | 0.00 USD | 1,020.00 USD |
| `7D` | `0.0908` | 967,350.00 USD | 0.00 USD | 967,350.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD |
| `1D` | `0.0910` | 749,150.00 USD | 0.00 USD | 749,150.00 USD | 6,520.00 USD | 363.17 USD | 0.00 USD |
| `7D` | `0.0911` | 955,950.00 USD | 0.00 USD | 955,950.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD |
| `1D` | `0.0912` | 742,270.00 USD | 0.00 USD | 742,270.00 USD | 0.00 USD | 1,450.00 USD | 787.79 USD |
| `1D` | `0.0914` | 740,030.00 USD | 0.00 USD | 740,030.00 USD | 0.00 USD | 944.94 USD | 51.31 USD |
| `7D` | `0.0914` | 952,670.00 USD | 0.00 USD | 952,670.00 USD | 1,670.00 USD | 903.90 USD | 45.81 USD |
| `1D` | `0.0916` | 739,040.00 USD | 0.00 USD | 739,040.00 USD | 6,590.00 USD | 0.00 USD | 2.87 USD |
| `7D` | `0.0917` | 950,050.00 USD | 0.00 USD | 950,050.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD |
| `1D` | `0.0918` | 732,450.00 USD | 0.00 USD | 732,450.00 USD | 3,850.00 USD | 0.00 USD | 2,510.00 USD |
| `1D` | `0.0920` | 726,080.00 USD | 0.00 USD | 726,080.00 USD | 3,690.00 USD | 504.78 USD | 2,580.00 USD |
| `1D` | `0.0922` | 719,310.00 USD | 0.00 USD | 719,310.00 USD | 0.00 USD | 750.63 USD | 62.82 USD |
| `7D` | `0.0923` | 942,040.00 USD | 0.00 USD | 942,040.00 USD | 0.00 USD | 0.00 USD | 10,560.00 USD |
| `1D` | `0.0924` | 718,500.00 USD | 0.00 USD | 718,500.00 USD | 1,410.00 USD | 518.97 USD | 14,390.00 USD |
| `1D` | `0.0926` | 702,170.00 USD | 0.00 USD | 702,170.00 USD | 3,270.00 USD | 1,660.00 USD | 0.00 USD |
| `7D` | `0.0926` | 931,480.00 USD | 0.00 USD | 931,480.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD |
| `7D` | `0.0932` | 921,510.00 USD | 0.00 USD | 921,510.00 USD | 0.00 USD | 0.00 USD | 12,240.00 USD |
| `1D` | `0.0934` | 697,250.00 USD | 0.00 USD | 697,250.00 USD | 0.00 USD | 0.00 USD | 6,860.00 USD |
| `7D` | `0.0935` | 909,270.00 USD | 0.00 USD | 909,270.00 USD | 0.00 USD | 1,320.00 USD | 6,490.00 USD |
| `1D` | `0.0938` | 690,390.00 USD | 0.00 USD | 690,390.00 USD | 0.00 USD | 0.00 USD | 141.01 USD |
| `7D` | `0.0938` | 901,460.00 USD | 0.00 USD | 901,460.00 USD | 0.00 USD | 0.00 USD | 8.57 USD |
| `7D` | `0.0941` | 901,450.00 USD | 0.00 USD | 901,450.00 USD | 2,050.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `0.0944` | 896,380.00 USD | 0.00 USD | 896,380.00 USD | 1,870.00 USD | 0.00 USD | 7,520.00 USD |
| `7D` | `0.0947` | 886,990.00 USD | 0.00 USD | 886,990.00 USD | 3,790.00 USD | 1,810.00 USD | 112.06 USD |
| `1D` | `0.0948` | 690,250.00 USD | 0.00 USD | 690,250.00 USD | 0.00 USD | 0.00 USD | 69.61 USD |
| `7D` | `0.0950` | 881,270.00 USD | 0.00 USD | 881,270.00 USD | 3,770.00 USD | 0.00 USD | 6,660.00 USD |
| `7D` | `0.0953` | 870,840.00 USD | 0.00 USD | 870,840.00 USD | 0.00 USD | 0.00 USD | 4.65 USD |
| `1D` | `0.0954` | 690,180.00 USD | 0.00 USD | 690,180.00 USD | 0.00 USD | 0.00 USD | 154.48 USD |
| `1D` | `0.0956` | 690,020.00 USD | 0.00 USD | 690,020.00 USD | 0.00 USD | 1,180.00 USD | 166.88 USD |
| `7D` | `0.0959` | 870,830.00 USD | 0.00 USD | 870,830.00 USD | 0.00 USD | 0.00 USD | 115.48 USD |
| `1D` | `0.0962` | 688,670.00 USD | 0.00 USD | 688,670.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0962` | 870,720.00 USD | 0.00 USD | 870,720.00 USD | 0.00 USD | 0.00 USD | 121.64 USD |
| `1D` | `0.0964` | 686,590.00 USD | 0.00 USD | 686,590.00 USD | 0.00 USD | 0.00 USD | 107.13 USD |
| `1D` | `0.0966` | 686,490.00 USD | 0.00 USD | 686,490.00 USD | 2,140.00 USD | 715.37 USD | 6,180.00 USD |
| `1D` | `0.0968` | 677,450.00 USD | 0.00 USD | 677,450.00 USD | 6,400.00 USD | 2,400.00 USD | 11,270.00 USD |
| `7D` | `0.0968` | 870,600.00 USD | 0.00 USD | 870,600.00 USD | 7,490.00 USD | 3,720.00 USD | 11,630.00 USD |
| `1D` | `0.0970` | 657,370.00 USD | 0.00 USD | 657,370.00 USD | 1,290.00 USD | 2,860.00 USD | 4,240.00 USD |
| `7D` | `0.0971` | 847,760.00 USD | 0.00 USD | 847,760.00 USD | 0.00 USD | 3,760.00 USD | 9,720.00 USD |
| `1D` | `0.0972` | 648,990.00 USD | 0.00 USD | 648,990.00 USD | 14,810.00 USD | 5,180.00 USD | 2,950.00 USD |
| `1D` | `0.0974` | 626,050.00 USD | 0.00 USD | 626,050.00 USD | 2,750.00 USD | 3,220.00 USD | 2,750.00 USD |
| `7D` | `0.0974` | 834,280.00 USD | 0.00 USD | 834,280.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD |
| `1D` | `0.0976` | 617,330.00 USD | 0.00 USD | 617,330.00 USD | 18,450.00 USD | 1,990.00 USD | 7,460.00 USD |
| `7D` | `0.0977` | 830,000.00 USD | 0.00 USD | 830,000.00 USD | 0.00 USD | 1,160.00 USD | 28,800.00 USD |
| `1D` | `0.0978` | 589,420.00 USD | 0.00 USD | 589,420.00 USD | 22,180.00 USD | 1,470.00 USD | 9,310.00 USD |
| `1D` | `0.0980` | 556,460.00 USD | 0.00 USD | 556,460.00 USD | 9,220.00 USD | 3,070.00 USD | 10,500.00 USD |
| `7D` | `0.0980` | 800,040.00 USD | 0.00 USD | 800,040.00 USD | 0.00 USD | 3,920.00 USD | 5,710.00 USD |
| `1D` | `0.0982` | 533,670.00 USD | 0.00 USD | 533,670.00 USD | 1,840.00 USD | 3,990.00 USD | 14,180.00 USD |
| `7D` | `0.0983` | 790,410.00 USD | 0.00 USD | 790,410.00 USD | 7,990.00 USD | 1,230.00 USD | 14,770.00 USD |
| `1D` | `0.0984` | 513,650.00 USD | 0.00 USD | 513,650.00 USD | 10,600.00 USD | 460.32 USD | 18,800.00 USD |
| `1D` | `0.0986` | 483,790.00 USD | 0.00 USD | 483,790.00 USD | 10,070.00 USD | 5,230.00 USD | 32,530.00 USD |
| `7D` | `0.0986` | 766,410.00 USD | 0.00 USD | 766,410.00 USD | 7,110.00 USD | 7,530.00 USD | 61,010.00 USD |
| `1D` | `0.0988` | 435,950.00 USD | 0.00 USD | 435,950.00 USD | 12,770.00 USD | 6,260.00 USD | 3,680.00 USD |
| `7D` | `0.0989` | 690,760.00 USD | 0.00 USD | 690,760.00 USD | 17,640.00 USD | 6,190.00 USD | 53,200.00 USD |
| `1D` | `0.0990` | 413,250.00 USD | 0.00 USD | 413,250.00 USD | 3,980.00 USD | 3,340.00 USD | 2,580.00 USD |
| `1D` | `0.0992` | 403,360.00 USD | 0.00 USD | 403,360.00 USD | 29,370.00 USD | 5,050.00 USD | 7,820.00 USD |
| `7D` | `0.0992` | 613,730.00 USD | 0.00 USD | 613,730.00 USD | 27,140.00 USD | 11,490.00 USD | 28,490.00 USD |
| `1D` | `0.0994` | 361,110.00 USD | 0.00 USD | 361,110.00 USD | 10,240.00 USD | 3,150.00 USD | 9,830.00 USD |
| `7D` | `0.0995` | 546,600.00 USD | 0.00 USD | 546,600.00 USD | 24,220.00 USD | 15,150.00 USD | 56,550.00 USD |
| `1D` | `0.0996` | 337,900.00 USD | 0.00 USD | 337,900.00 USD | 2,640.00 USD | 3,020.00 USD | 28,270.00 USD |
| `1D` | `0.0998` | 303,960.00 USD | 0.00 USD | 303,960.00 USD | 35,620.00 USD | 1,690.00 USD | 19,400.00 USD |
| `7D` | `0.0998` | 450,680.00 USD | 0.00 USD | 450,680.00 USD | 28,450.00 USD | 6,400.00 USD | 80,720.00 USD |
| `1D` | `0.1000` | 247,240.00 USD | 0.00 USD | 247,240.00 USD | 42,490.00 USD | 3,370.00 USD | 26,210.00 USD |
| `7D` | `0.1001` | 335,110.00 USD | 0.00 USD | 335,110.00 USD | 36,110.00 USD | 8,650.00 USD | 13,120.00 USD |
| `1D` | `0.1002` | 175,160.00 USD | 0.00 USD | 175,160.00 USD | 21,100.00 USD | 4,620.00 USD | 17,270.00 USD |
| `1D` | `0.1004` | 132,180.00 USD | 0.00 USD | 132,180.00 USD | 1,970.00 USD | 5,260.00 USD | 13,950.00 USD |
| `7D` | `0.1004` | 277,220.00 USD | 0.00 USD | 277,220.00 USD | 22,470.00 USD | 16,470.00 USD | 23,430.00 USD |
| `1D` | `0.1006` | 111,000.00 USD | 0.00 USD | 111,000.00 USD | 16,470.00 USD | 5,640.00 USD | 72,760.00 USD |
| `7D` | `0.1007` | 214,850.00 USD | 0.00 USD | 214,850.00 USD | 20,870.00 USD | 3,870.00 USD | 100,230.00 USD |
| `1D` | `0.1008` | 16,130.00 USD | 0.00 USD | 16,130.00 USD | 0.00 USD | 8,710.00 USD | 0.00 USD |
| `1D` | `0.1010` | 7,420.00 USD | 0.00 USD | 7,420.00 USD | 0.00 USD | 0.00 USD | 2,450.00 USD |
| `7D` | `0.1010` | 89,880.00 USD | 0.00 USD | 89,880.00 USD | 17,340.00 USD | 6,580.00 USD | 6,630.00 USD |
| `1D` | `0.1012` | 4,970.00 USD | 0.00 USD | 4,970.00 USD | 0.00 USD | 0.00 USD | 939.04 USD |
| `7D` | `0.1013` | 59,330.00 USD | 0.00 USD | 59,330.00 USD | 15,270.00 USD | 5,230.00 USD | 0.00 USD |
| `1D` | `0.1014` | 4,030.00 USD | 0.00 USD | 4,030.00 USD | 0.00 USD | 0.00 USD | 587.32 USD |
| `1D` | `0.1016` | 3,440.00 USD | 0.00 USD | 3,440.00 USD | 0.00 USD | 2,540.00 USD | 0.00 USD |
| `7D` | `0.1016` | 38,830.00 USD | 0.00 USD | 38,830.00 USD | 15,440.00 USD | 5,490.00 USD | 0.00 USD |
| `1D` | `0.1018` | 897.78 USD | 0.00 USD | 897.78 USD | 0.00 USD | 897.78 USD | 0.00 USD |
| `1D` | `0.1019` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1019` | 17,890.00 USD | 0.00 USD | 17,890.00 USD | 12,100.00 USD | 5,790.00 USD | 0.00 USD |
| `7D` | `0.1020` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1022` | 20,180.00 USD | 20,180.00 USD | 0.00 USD | 11,930.00 USD | 8,250.00 USD | 0.00 USD |
| `7D` | `0.1025` | 21,740.00 USD | 21,740.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1028` | 29,930.00 USD | 29,930.00 USD | 0.00 USD | 3,800.00 USD | 4,390.00 USD | 0.00 USD |
| `1D` | `0.1030` | 11,070.00 USD | 11,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,070.00 USD |
| `7D` | `0.1031` | 55,750.00 USD | 55,750.00 USD | 0.00 USD | 19,560.00 USD | 6,260.00 USD | 0.00 USD |
| `1D` | `0.1032` | 62,990.00 USD | 62,990.00 USD | 0.00 USD | 27,910.00 USD | 3,360.00 USD | 20,650.00 USD |
| `1D` | `0.1034` | 79,840.00 USD | 79,840.00 USD | 0.00 USD | 5,500.00 USD | 2,330.00 USD | 9,020.00 USD |
| `7D` | `0.1034` | 81,690.00 USD | 81,690.00 USD | 0.00 USD | 18,920.00 USD | 7,030.00 USD | 0.00 USD |
| `1D` | `0.1036` | 97,980.00 USD | 97,980.00 USD | 0.00 USD | 6,930.00 USD | 11,150.00 USD | 54.66 USD |
| `7D` | `0.1037` | 89,410.00 USD | 89,410.00 USD | 0.00 USD | 2,710.00 USD | 5,010.00 USD | 0.00 USD |
| `1D` | `0.1038` | 142,560.00 USD | 142,560.00 USD | 0.00 USD | 35,160.00 USD | 9,420.00 USD | 0.00 USD |
| `1D` | `0.1040` | 174,490.00 USD | 174,490.00 USD | 0.00 USD | 6,500.00 USD | 12,880.00 USD | 12,550.00 USD |
| `7D` | `0.1040` | 137,010.00 USD | 137,010.00 USD | 0.00 USD | 5,940.00 USD | 10,300.00 USD | 31,350.00 USD |
| `1D` | `0.1042` | 201,250.00 USD | 201,250.00 USD | 0.00 USD | 0.00 USD | 9,490.00 USD | 17,270.00 USD |
| `7D` | `0.1043` | 158,960.00 USD | 158,960.00 USD | 0.00 USD | 15,960.00 USD | 5,980.00 USD | 0.00 USD |
| `1D` | `0.1044` | 215,620.00 USD | 215,620.00 USD | 0.00 USD | 0.00 USD | 14,370.00 USD | 0.00 USD |
| `1D` | `0.1046` | 248,460.00 USD | 248,460.00 USD | 0.00 USD | 7,060.00 USD | 1,080.00 USD | 24,700.00 USD |
| `7D` | `0.1046` | 228,930.00 USD | 228,930.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD | 60,160.00 USD |
| `1D` | `0.1048` | 365,610.00 USD | 365,610.00 USD | 0.00 USD | 27,930.00 USD | 9,140.00 USD | 80,080.00 USD |
| `7D` | `0.1049` | 353,350.00 USD | 353,350.00 USD | 0.00 USD | 34,790.00 USD | 6,530.00 USD | 83,110.00 USD |
| `1D` | `0.1050` | 422,370.00 USD | 422,370.00 USD | 0.00 USD | 35,330.00 USD | 10,740.00 USD | 10,690.00 USD |
| `1D` | `0.1052` | 526,440.00 USD | 526,440.00 USD | 0.00 USD | 43,830.00 USD | 12,940.00 USD | 47,290.00 USD |
| `7D` | `0.1052` | 531,120.00 USD | 531,120.00 USD | 0.00 USD | 28,200.00 USD | 24,160.00 USD | 125,400.00 USD |
| `1D` | `0.1054` | 678,440.00 USD | 678,440.00 USD | 0.00 USD | 59,720.00 USD | 20,100.00 USD | 72,180.00 USD |
| `7D` | `0.1055` | 909,850.00 USD | 909,850.00 USD | 0.00 USD | 122,840.00 USD | 44,430.00 USD | 211,460.00 USD |
| `1D` | `0.1056` | 775,010.00 USD | 775,010.00 USD | 0.00 USD | 25,000.00 USD | 27,390.00 USD | 44,180.00 USD |
| `1D` | `0.1058` | 883,620.00 USD | 883,620.00 USD | 0.00 USD | 30,300.00 USD | 0.00 USD | 78,310.00 USD |
| `7D` | `0.1058` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 105,620.00 USD | 53,680.00 USD | 189,110.00 USD |
| `1D` | `0.1060` | 983,260.00 USD | 983,260.00 USD | 0.00 USD | 44,890.00 USD | 0.00 USD | 54,750.00 USD |
| `7D` | `0.1061` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 75,540.00 USD | 72,260.00 USD | 118,330.00 USD |
| `1D` | `0.1062` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 28,640.00 USD | 2,030.00 USD | 78,510.00 USD |
| `1D` | `0.1064` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD | 51,350.00 USD |
| `7D` | `0.1064` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 52,580.00 USD | 192,520.00 USD |
| `1D` | `0.1066` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD | 31,530.00 USD |
| `7D` | `0.1067` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 51,740.00 USD | 156,150.00 USD |
| `1D` | `0.1068` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 4,700.00 USD | 2,620.00 USD | 55,720.00 USD |
| `1D` | `0.1070` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 8,170.00 USD | 7,280.00 USD | 51,460.00 USD |
| `7D` | `0.1070` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 57,770.00 USD | 134,670.00 USD |
| `1D` | `0.1072` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 236.90 USD |
| `7D` | `0.1073` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 17,700.00 USD | 0.00 USD |
| `1D` | `0.1074` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 104.27 USD |
| `1D` | `0.1076` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 153.36 USD |
| `7D` | `0.1076` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,500.00 USD |
| `1D` | `0.1078` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,190.00 USD |
| `7D` | `0.1079` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 79.36 USD |
| `1D` | `0.1082` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 5,910.00 USD | 21.66 USD |
| `7D` | `0.1082` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 89.24 USD |
| `1D` | `0.1084` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 7,990.00 USD | 0.00 USD | 35,870.00 USD |
| `7D` | `0.1085` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1086` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 4,220.00 USD | 2,240.00 USD | 72,930.00 USD |
| `1D` | `0.1088` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 44,230.00 USD | 0.00 USD | 8,060.00 USD |
| `7D` | `0.1088` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 5,290.00 USD | 0.00 USD | 113.96 USD |
| `1D` | `0.1090` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 44,990.00 USD | 0.00 USD | 124.57 USD |
| `7D` | `0.1091` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD |
| `1D` | `0.1092` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 10,290.00 USD | 0.00 USD | 29.91 USD |
| `1D` | `0.1094` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 13,100.00 USD | 0.00 USD | 14,050.00 USD |
| `7D` | `0.1094` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD |
| `1D` | `0.1096` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 7,670.00 USD |
| `7D` | `0.1097` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1098` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 13,380.00 USD | 3,910.00 USD | 22,790.00 USD |
| `1D` | `0.1100` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 2,820.00 USD | 4,290.00 USD |
| `7D` | `0.1100` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 21,840.00 USD |
| `1D` | `0.1102` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 4,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1103` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1104` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 6,920.00 USD | 10,390.00 USD | 0.00 USD |
| `1D` | `0.1106` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 12,720.00 USD | 30,820.00 USD |
| `7D` | `0.1106` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 22,880.00 USD | 16,040.00 USD |
| `1D` | `0.1108` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 5,220.00 USD | 1,120.00 USD | 15,630.00 USD |
| `7D` | `0.1109` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD |
| `1D` | `0.1112` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 10,780.00 USD | 0.00 USD | 96.09 USD |
| `7D` | `0.1112` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD |
| `1D` | `0.1114` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 15,810.00 USD | 5,880.00 USD | 39,070.00 USD |
| `1D` | `0.1116` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 4,760.00 USD | 12,550.00 USD | 6,930.00 USD |
| `1D` | `0.1118` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 25,510.00 USD | 20,030.00 USD | 57,050.00 USD |
| `7D` | `0.1118` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD |
| `1D` | `0.1120` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 27,100.00 USD | 8,540.00 USD | 9,830.00 USD |
| `7D` | `0.1121` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 17,760.00 USD | 0.00 USD | 38,370.00 USD |
| `1D` | `0.1122` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 22,700.00 USD | 4,480.00 USD | 15,000.00 USD |
| `1D` | `0.1124` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 17,850.00 USD | 6,120.00 USD | 8,600.00 USD |
| `7D` | `0.1124` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD |
| `1D` | `0.1126` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 9,370.00 USD | 11,410.00 USD | 17,020.00 USD |
| `7D` | `0.1127` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD |
| `1D` | `0.1128` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 10,120.00 USD | 0.00 USD | 11,120.00 USD |
| `1D` | `0.1130` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 7,970.00 USD | 2,000.00 USD | 16,330.00 USD |
| `7D` | `0.1130` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,260.00 USD |
| `1D` | `0.1132` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 19,390.00 USD | 18,950.00 USD | 16,110.00 USD |
| `7D` | `0.1133` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD |
| `1D` | `0.1134` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 4,040.00 USD | 12,980.00 USD | 13,830.00 USD |
| `1D` | `0.1136` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 787.70 USD | 4,130.00 USD |
| `7D` | `0.1136` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD |
| `1D` | `0.1138` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 856.93 USD | 14,270.00 USD |
| `7D` | `0.1139` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD |
| `1D` | `0.1140` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 7,800.00 USD | 0.00 USD | 6,050.00 USD |
| `1D` | `0.1142` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 24,760.00 USD | 17,100.00 USD | 22,170.00 USD |
| `7D` | `0.1142` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD |
| `1D` | `0.1144` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 9,940.00 USD | 21,970.00 USD | 31,580.00 USD |
| `7D` | `0.1145` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD |
| `1D` | `0.1146` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 5,090.00 USD | 10,830.00 USD | 30,120.00 USD |
| `1D` | `0.1148` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 33,430.00 USD | 3,280.00 USD | 30,510.00 USD |
| `7D` | `0.1148` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 176,010.00 USD |
| `1D` | `0.1150` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 19,260.00 USD | 13,020.00 USD | 21,660.00 USD |
| `7D` | `0.1151` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD |
| `1D` | `0.1152` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 34,520.00 USD | 17,470.00 USD | 59,670.00 USD |
| `1D` | `0.1153` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 6,400.00 USD | 7,760.00 USD | 23,220.00 USD |
| `7D` | `0.1154` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 243,190.00 USD | 26,970.00 USD | 195,390.00 USD |
| `7D` | `0.1157` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 188,950.00 USD | 25,290.00 USD | 98,310.00 USD |
| `7D` | `0.1160` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 139,350.00 USD | 32,830.00 USD | 109,320.00 USD |
| `7D` | `0.1163` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD |
| `7D` | `0.1166` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD |
| `7D` | `0.1169` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 82,770.00 USD | 26,150.00 USD | 112,810.00 USD |
| `7D` | `0.1172` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD |
| `7D` | `0.1175` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 72,770.00 USD | 17,930.00 USD | 81,630.00 USD |
| `7D` | `0.1178` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 89,510.00 USD | 23,660.00 USD | 55,770.00 USD |
| `7D` | `0.1181` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD |
| `7D` | `0.1184` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD |
| `7D` | `0.1187` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 5,620.00 USD | 17,120.00 USD | 54,960.00 USD |
| `7D` | `0.1190` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD |
| `7D` | `0.1193` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD |
| `7D` | `0.1196` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD |
| `7D` | `0.1199` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 9,100.00 USD | 13,190.00 USD | 67,980.00 USD |
| `7D` | `0.1202` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 138,430.00 USD | 21,430.00 USD | 32,790.00 USD |
| `7D` | `0.1205` | 6,850,000.00 USD | 6,850,000.00 USD | 0.00 USD | 132,960.00 USD | 72,910.00 USD | 130,900.00 USD |
| `7D` | `0.1208` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 39,480.00 USD | 25,720.00 USD | 66,520.00 USD |
| `7D` | `0.1211` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 72,500.00 USD | 25,920.00 USD | 111,160.00 USD |
| `7D` | `0.1214` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD |
| `7D` | `0.1217` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD |
| `7D` | `0.1220` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 45,700.00 USD | 10,970.00 USD | 54,700.00 USD |
| `7D` | `0.1223` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 76,930.00 USD | 24,740.00 USD | 45,660.00 USD |
| `7D` | `0.1226` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 54,940.00 USD | 27,490.00 USD | 5,210.00 USD |
| `7D` | `0.1229` | 7,890,000.00 USD | 7,890,000.00 USD | 0.00 USD | 71,850.00 USD | 38,040.00 USD | 79,050.00 USD |
| `7D` | `0.1232` | 8,060,000.00 USD | 8,060,000.00 USD | 0.00 USD | 67,800.00 USD | 28,560.00 USD | 68,270.00 USD |
| `7D` | `0.1235` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 15,040.00 USD | 5,390.00 USD | 17,120.00 USD |
| `7D` | `0.1238` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 8,310.00 USD | 3,610.00 USD | 3,100.00 USD |
| `7D` | `0.1241` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 11,380.00 USD | 1,380.00 USD | 7,090.00 USD |
| `7D` | `0.1244` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 26,540.00 USD | 8,130.00 USD | 9,660.00 USD |
| `7D` | `0.1247` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 7,900.00 USD | 12,590.00 USD | 15,120.00 USD |
| `7D` | `0.1250` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 8,540.00 USD | 4,990.00 USD | 5,780.00 USD |
| `7D` | `0.1253` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | 16,470.00 USD |
| `7D` | `0.1256` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 11,990.00 USD | 11,420.00 USD | 220.44 USD |
| `7D` | `0.1259` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 5,870.00 USD | 1,190.00 USD | 121.42 USD |
| `7D` | `0.1262` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | 3,530.00 USD |
| `7D` | `0.1265` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 2,710.00 USD | 0.00 USD | 7,350.00 USD |
| `7D` | `0.1268` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD |
| `7D` | `0.1271` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 5,940.00 USD | 0.00 USD | 30.15 USD |
| `7D` | `0.1274` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12.00 USD |
| `7D` | `0.1277` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20.66 USD |
| `7D` | `0.1280` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,380.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `64.94M` | Total OI Tokens: `636,126,175.1 OP`
  * 1h OI Change: `-0.08%` | 4h OI Change: `-10.47%` | 24h OI Change: `-15.53%`
  * Exchange Breakdown: Binance=`14.67M` | Bybit=`13.08M` | OKX=`3.61M` | Hyperliquid=`3.46M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-3.22K` | Last 24h: `270.64` | Last 3d: `-2.23K` | Last 7d: `-15.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0291%` | **USDT OKX** | `-0.0043%` |
| **USDT Bybit** | `0.0095%` | **USDT KuCoin** | `0.0032%` |
| **USDT MEXC** | `-0.0288%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0052%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `48.32%` | `51.68%` | `0.93` | 2,170,000.00 USD |
| `15M` | `Binance` | `45.02%` | `54.98%` | `0.82` | 982,050.00 USD |
| `15M` | `OKX` | `44.82%` | `55.18%` | `0.81` | 185,280.00 USD |
| `15M` | `Bybit` | `45.84%` | `54.16%` | `0.85` | 205,520.00 USD |
| `15M` | `KuCoin` | `51.08%` | `48.92%` | `1.04` | 196,790.00 USD |
| `15M` | `Gate` | `30.06%` | `69.94%` | `0.43` | 53,980.00 USD |
| `15M` | `Bitget` | `38.37%` | `61.63%` | `0.62` | 98,830.00 USD |
| `15M` | `BingX` | `48.63%` | `51.37%` | `0.95` | 30,850.00 USD |
| `15M` | `MEXC` | `70.7%` | `29.3%` | `2.41` | 182,870.00 USD |
| `15M` | `Bitunix` | `41.09%` | `58.91%` | `0.70` | 25,720.00 USD |
| `15M` | `Hyperliquid` | `40.19%` | `59.81%` | `0.67` | 12,760.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.95%` | `49.05%` | `1.04` | 82,380.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `64.21%` | `35.79%` | `1.79` | 103,380.00 USD |
| `15M` | `HTX` | `0.06%` | `99.94%` | `0.00` | 332.63 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `84.41%` | `15.59%` | `5.41` | 5,220.00 USD |
| `15M` | `Aster` | `1.74%` | `98.26%` | `0.02` | 760.63 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 166.79 USD |
| `15M` | `Whale Positions` | `45.02%` | `54.98%` | `0.82` | 982,050.00 USD |
| `15M` | `Global Accounts` | `48.32%` | `51.68%` | `0.93` | 2,170,000.00 USD |
| `1H` | `OP` | `46.41%` | `53.59%` | `0.87` | 13,060,000.00 USD |
| `1H` | `Binance` | `48.11%` | `51.89%` | `0.93` | 5,950,000.00 USD |
| `1H` | `OKX` | `50.63%` | `49.37%` | `1.03` | 1,130,000.00 USD |
| `1H` | `Bybit` | `50.09%` | `49.91%` | `1.00` | 1,220,000.00 USD |
| `1H` | `KuCoin` | `50.27%` | `49.73%` | `1.01` | 711,750.00 USD |
| `1H` | `Gate` | `47.44%` | `52.56%` | `0.90` | 313,660.00 USD |
| `1H` | `Bitget` | `38.88%` | `61.12%` | `0.64` | 537,550.00 USD |
| `1H` | `BingX` | `24.92%` | `75.08%` | `0.33` | 666,490.00 USD |
| `1H` | `MEXC` | `47.39%` | `52.61%` | `0.90` | 925,390.00 USD |
| `1H` | `Bitunix` | `24.87%` | `75.13%` | `0.33` | 426,170.00 USD |
| `1H` | `Hyperliquid` | `38.99%` | `61.01%` | `0.64` | 262,700.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.12%` | `48.88%` | `1.05` | 352,090.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `55.14%` | `44.86%` | `1.23` | 470,020.00 USD |
| `1H` | `HTX` | `23.2%` | `76.8%` | `0.30` | 1,030.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `51.09%` | `48.91%` | `1.04` | 36,520.00 USD |
| `1H` | `Aster` | `51.77%` | `48.23%` | `1.07` | 46,240.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `37.01%` | `62.99%` | `0.59` | 4,440.00 USD |
| `1H` | `Whale Positions` | `48.11%` | `51.89%` | `0.93` | 5,950,000.00 USD |
| `1H` | `Global Accounts` | `46.41%` | `53.59%` | `0.87` | 13,060,000.00 USD |
| `4H` | `OP` | `47.23%` | `52.77%` | `0.90` | 58,310,000.00 USD |
| `4H` | `Binance` | `46.95%` | `53.05%` | `0.89` | 22,180,000.00 USD |
| `4H` | `OKX` | `46.48%` | `53.52%` | `0.87` | 7,030,000.00 USD |
| `4H` | `Bybit` | `46.01%` | `53.99%` | `0.85` | 9,240,000.00 USD |
| `4H` | `KuCoin` | `46.54%` | `53.46%` | `0.87` | 522,590.00 USD |
| `4H` | `Gate` | `53.26%` | `46.74%` | `1.14` | 705,190.00 USD |
| `4H` | `Bitget` | `48.83%` | `51.17%` | `0.95` | 3,710,000.00 USD |
| `4H` | `BingX` | `45.94%` | `54.06%` | `0.85` | 1,800,000.00 USD |
| `4H` | `MEXC` | `45.51%` | `54.49%` | `0.84` | 2,880,000.00 USD |
| `4H` | `Bitunix` | `45.79%` | `54.21%` | `0.84` | 691,750.00 USD |
| `4H` | `Hyperliquid` | `36.68%` | `63.32%` | `0.58` | 920,380.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.38%` | `51.62%` | `0.94` | 7,500,000.00 USD |
| `4H` | `Crypto.com` | `23.33%` | `76.67%` | `0.30` | 23,230.00 USD |
| `4H` | `WhiteBIT` | `72.98%` | `27.02%` | `2.70` | 873,260.00 USD |
| `4H` | `HTX` | `47.62%` | `52.38%` | `0.91` | 47,580.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `57.53%` | `42.47%` | `1.35` | 66,640.00 USD |
| `4H` | `Aster` | `33.27%` | `66.73%` | `0.50` | 54,760.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.15%` | `48.85%` | `1.05` | 80,870.00 USD |
| `4H` | `Whale Positions` | `46.95%` | `53.05%` | `0.89` | 22,180,000.00 USD |
| `4H` | `Global Accounts` | `47.23%` | `52.77%` | `0.90` | 58,310,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1063` | `0.1047` | `0.1063` | `0.1088` | `0.1013` | 5,548,996.22 USD | 2,272,459.88 USD | 3,276,536.35 USD | -1,004,076.47 USD | `-18.09%` | `5B / 37S` |
| `5:00 UTC` | `0.1014` | `0.1013` | `0.1014` | `0.1029` | `0.0990` | 5,717,098.88 USD | 2,672,854.06 USD | 3,044,244.81 USD | -371,390.75 USD | `-6.50%` | `7B / 23S` |
| `0:00 UTC` | `0.1025` | `0.1020` | `0.1025` | `0.1033` | `0.1007` | 1,857,629.60 USD | 946,076.57 USD | 911,553.03 USD | 34,523.54 USD | `+1.86%` | `19B / 6S` |
| `5:00 UTC` | `0.1043` | `0.1035` | `0.1043` | `0.1044` | `0.1026` | 1,285,007.52 USD | 601,525.80 USD | 683,481.72 USD | -81,955.93 USD | `-6.38%` | `27B / 29S` |
| `0:00 UTC` | `0.1037` | `0.1036` | `0.1037` | `0.1042` | `0.1024` | 770,717.58 USD | 335,049.96 USD | 435,667.63 USD | -100,617.67 USD | `-13.06%` | `27B / 45S` |
| `5:00 UTC` | `0.1020` | `0.1024` | `0.1020` | `0.1029` | `0.1018` | 520,168.37 USD | 289,498.79 USD | 230,669.58 USD | 58,829.21 USD | `+11.31%` | `26B / 7S` |
| `0:00 UTC` | `0.1013` | `0.1014` | `0.1013` | `0.1023` | `0.1003` | 969,689.66 USD | 453,817.19 USD | 515,872.47 USD | -62,055.28 USD | `-6.40%` | `8B / 16S` |
| `5:00 UTC` | `0.1025` | `0.1022` | `0.1025` | `0.1029` | `0.1010` | 722,088.27 USD | 440,195.52 USD | 281,892.75 USD | 158,302.78 USD | `+21.92%` | `56B / 16S` |
| `0:00 UTC` | `0.1023` | `0.1024` | `0.1023` | `0.1029` | `0.1019` | 576,770.99 USD | 307,354.68 USD | 269,416.31 USD | 37,938.37 USD | `+6.58%` | `13B / 12S` |
| `5:00 UTC` | `0.1019` | `0.1020` | `0.1019` | `0.1023` | `0.1016` | 347,104.85 USD | 238,369.54 USD | 108,735.31 USD | 129,634.22 USD | `+37.35%` | `25B / 4S` |

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
| `5m` | -8,750.00 USD | -19,590.00 USD | **`DISTRIBUTION`** |
| `15m` | 127,250.00 USD | 52,630.00 USD | **`ACCUMULATION`** |
| `30m` | 199,100.00 USD | 215,340.00 USD | **`ACCUMULATION`** |
| `1h` | 213,840.00 USD | 217,200.00 USD | **`ACCUMULATION`** |
| `2h` | 22,760.00 USD | -791,820.00 USD | **`DISTRIBUTION`** |
| `4h` | 43,990.00 USD | -2,590,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -4,760.00 USD | -3,080,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 62,750.00 USD | -2,550,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 252,460.00 USD | -2,520,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 148,360.00 USD | -4,750,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -52,070.00 USD | -12,320,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,400,000.00 USD | -81,350,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-8.75K` | 15m=`+127.25K` | 1h=`+213.84K` | 24h=`+148.36K`
* Futures Capital Netflows: 5m=`-19.59K` | 15m=`+52.63K` | 1h=`+217.20K` | 24h=`-4.75M`
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
  * `2026-10-30 04:15:19 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:19 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:21:19 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:20:19 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:20:19 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:22:19 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:22:19 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:19 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
