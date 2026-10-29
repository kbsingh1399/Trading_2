# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 03:37:25 IST` (`2026-10-29 22:07:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1024` | `0.1026` | `0.1018` | `0.1018` | `2,054,582` | 209,942.05 USD | 35,312.18 USD | `+16.82%` | -2,884,862.70 USD | `+0.62` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1018` | `0.1023` | `0.1012` | `0.1013` | `2,415,466` | 245,846.52 USD | 18,082.66 USD | `+7.36%` | -2,866,780.04 USD | `+0.52` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1013` | `0.1013` | `0.1007` | `0.1013` | `1,775,307` | 179,255.21 USD | -113,627.58 USD | `-63.39%` | -2,980,407.63 USD | `-0.21` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1032` | `0.1042` | `0.1023` | `0.1025` | `7,440,373` | 770,717.58 USD | -100,617.67 USD | `-13.06%` | -2,931,845.35 USD | `-0.04` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1025` | `0.1029` | `0.1018` | `0.1018` | `5,081,383` | 520,168.37 USD | 58,829.21 USD | `+11.31%` | -2,873,016.15 USD | `+0.61` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1018` | `0.1023` | `0.1007` | `0.1012` | `4,098,655` | 415,781.47 USD | -102,019.87 USD | `-24.54%` | -2,975,036.02 USD | `-0.04` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `136,699,709` | 14,218,772.66 USD | -1,614,985.67 USD | `-11.36%` | -2,750,784.93 USD | `-3.57` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1012` | `0.1044` | `0.1007` | `0.1018` | `43,149,466` | 4,433,523.07 USD | -89,220.85 USD | `-2.01%` | -2,840,005.78 USD | `+0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1018` | `0.1023` | `0.1007` | `0.1012` | `4,098,655` | 415,781.47 USD | -102,019.87 USD | `-24.54%` | -2,942,025.65 USD | `-0.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -935,828.18 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | -1,111,968.46 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `183,947,830` | 19,068,077.21 USD | -1,806,226.39 USD | `-9.47%` | -2,918,194.85 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1085` | `0.1106` | `0.1071` | `0.1076` | `47,048,931` | 5,111,570.05 USD | 108,567.99 USD | `+2.12%` | -1,419,806.61 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,277,083.78 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -935,828.18 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | -1,111,968.46 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `183,947,830` | 19,068,077.21 USD | -1,806,226.39 USD | `-9.47%` | -2,918,194.85 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:35:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1101` | 5,182.99 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 5.18K USD at 0.1101 USD [API] | `2026-10-28 13:20:09` |
| `ANNOUNCEMENT` | `INFO` | `0.1100` | 5,889.99 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale BUY: 5.89K USD at 0.1100 USD [API] | `2026-10-28 14:48:40` |
| `ANNOUNCEMENT` | `INFO` | `0.1096` | 6,503.12 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 6.50K USD at 0.1096 USD [API] | `2026-10-28 17:22:10` |


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
| `Live` | `Long Liquidation` | `0.0375` | 225.00 USD | 199,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0475` | 2,650.00 USD | 199,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 223.67 USD | 196,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 829.69 USD | 196,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 4,150.00 USD | 195,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 1,100.00 USD | 191,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 486.65 USD | 190,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 353.81 USD | 189,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 333.98 USD | 189,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 518.48 USD | 188,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 1,920.00 USD | 188,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 23,910.00 USD | 186,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,300.00 USD | 162,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 1,020.00 USD | 160,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 2,710.00 USD | 159,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 44,690.00 USD | 156,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 1,320.00 USD | 111,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 223.98 USD | 110,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 1,560.00 USD | 110,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0878` | 1,150,000.00 USD | 1,150,000.00 USD | 1,370.00 USD | 4,930.00 USD | 27,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0881` | 735,460.00 USD | 735,460.00 USD | 2,400.00 USD | 1,300.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0881` | 1,120,000.00 USD | 1,120,000.00 USD | 3,770.00 USD | 2,660.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0883` | 727,420.00 USD | 727,420.00 USD | 2,370.00 USD | 659.34 USD | 5,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0884` | 1,100,000.00 USD | 1,100,000.00 USD | 7,040.00 USD | 4,640.00 USD | 11,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0885` | 718,410.00 USD | 718,410.00 USD | 0.00 USD | 312.16 USD | 2,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0887` | 715,580.00 USD | 715,580.00 USD | 1,740.00 USD | 655.48 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0887` | 1,080,000.00 USD | 1,080,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0889` | 708,650.00 USD | 708,650.00 USD | 727.20 USD | 1,690.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0890` | 1,040,000.00 USD | 1,040,000.00 USD | 14,610.00 USD | 4,470.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0891` | 704,130.00 USD | 704,130.00 USD | 1,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0893` | 702,800.00 USD | 702,800.00 USD | 983.61 USD | 0.00 USD | 542.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0893` | 1,020,000.00 USD | 1,020,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0895` | 701,280.00 USD | 701,280.00 USD | 0.00 USD | 215.06 USD | 394.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,120.00 USD | 108,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0896` | 1,000,000.00 USD | 1,000,000.00 USD | 5,760.00 USD | 611.80 USD | 6,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0897` | 700,670.00 USD | 700,670.00 USD | 0.00 USD | 772.87 USD | 0.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0899` | 699,890.00 USD | 699,890.00 USD | 0.00 USD | 287.77 USD | 601.21 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0899` | 987,910.00 USD | 987,910.00 USD | 3,390.00 USD | 927.82 USD | 4,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0901` | 699,000.00 USD | 699,000.00 USD | 2,450.00 USD | 0.00 USD | 293.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0902` | 979,110.00 USD | 979,110.00 USD | 2,270.00 USD | 910.78 USD | 1,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0903` | 696,260.00 USD | 696,260.00 USD | 831.11 USD | 2,190.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0905` | 692,170.00 USD | 692,170.00 USD | 413.91 USD | 998.41 USD | 2,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0905` | 974,710.00 USD | 974,710.00 USD | 10,350.00 USD | 996.61 USD | 4,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0905` | 1,260.00 USD | 105,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0907` | 687,920.00 USD | 687,920.00 USD | 2,290.00 USD | 909.44 USD | 974.67 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0908` | 959,280.00 USD | 959,280.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0909` | 683,750.00 USD | 683,750.00 USD | 938.76 USD | 499.80 USD | 778.75 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0911` | 681,530.00 USD | 681,530.00 USD | 5,580.00 USD | 778.50 USD | 5.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0911` | 947,890.00 USD | 947,890.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0913` | 675,170.00 USD | 675,170.00 USD | 0.00 USD | 0.00 USD | 787.25 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0914` | 944,610.00 USD | 944,610.00 USD | 1,670.00 USD | 903.90 USD | 45.81 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0915` | 674,380.00 USD | 674,380.00 USD | 6,590.00 USD | 0.00 USD | 46.43 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0917` | 667,740.00 USD | 667,740.00 USD | 2,550.00 USD | 0.00 USD | 2.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0917` | 941,980.00 USD | 941,980.00 USD | 0.00 USD | 0.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0919` | 665,190.00 USD | 665,190.00 USD | 3,690.00 USD | 0.00 USD | 8.94 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0923` | 661,490.00 USD | 661,490.00 USD | 0.00 USD | 0.00 USD | 3,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0923` | 940,240.00 USD | 940,240.00 USD | 0.00 USD | 0.00 USD | 10,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0925` | 658,240.00 USD | 658,240.00 USD | 3,270.00 USD | 1,660.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0926` | 929,690.00 USD | 929,690.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0932` | 919,710.00 USD | 919,710.00 USD | 0.00 USD | 0.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0933` | 642,130.00 USD | 642,130.00 USD | 0.00 USD | 0.00 USD | 6,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0935` | 907,480.00 USD | 907,480.00 USD | 0.00 USD | 1,320.00 USD | 6,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0937` | 635,270.00 USD | 635,270.00 USD | 0.00 USD | 0.00 USD | 64.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0938` | 899,670.00 USD | 899,670.00 USD | 0.00 USD | 0.00 USD | 8.57 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0939` | 635,200.00 USD | 635,200.00 USD | 0.00 USD | 0.00 USD | 76.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0941` | 899,660.00 USD | 899,660.00 USD | 2,050.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0944` | 894,590.00 USD | 894,590.00 USD | 1,870.00 USD | 0.00 USD | 7,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0945` | 69,120.00 USD | 104,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0947` | 635,130.00 USD | 635,130.00 USD | 0.00 USD | 0.00 USD | 69.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0947` | 885,190.00 USD | 885,190.00 USD | 3,790.00 USD | 1,810.00 USD | 112.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0950` | 879,480.00 USD | 879,480.00 USD | 3,770.00 USD | 0.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0953` | 635,060.00 USD | 635,060.00 USD | 0.00 USD | 0.00 USD | 108.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0953` | 869,050.00 USD | 869,050.00 USD | 0.00 USD | 0.00 USD | 4.65 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0955` | 634,950.00 USD | 634,950.00 USD | 0.00 USD | 1,180.00 USD | 166.88 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0955` | 2,040.00 USD | 35,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0959` | 869,040.00 USD | 869,040.00 USD | 0.00 USD | 1,140.00 USD | 115.48 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0961` | 633,600.00 USD | 633,600.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0962` | 867,790.00 USD | 867,790.00 USD | 0.00 USD | 0.00 USD | 121.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0963` | 631,520.00 USD | 631,520.00 USD | 0.00 USD | 0.00 USD | 1.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0965` | 631,520.00 USD | 631,520.00 USD | 1,280.00 USD | 282.32 USD | 1,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0965` | 1,160.00 USD | 33,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0967` | 628,080.00 USD | 628,080.00 USD | 2,660.00 USD | 1,100.00 USD | 7,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0968` | 867,670.00 USD | 867,670.00 USD | 7,490.00 USD | 3,720.00 USD | 11,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0969` | 616,810.00 USD | 616,810.00 USD | 4,590.00 USD | 2,640.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0971` | 600,570.00 USD | 600,570.00 USD | 16,100.00 USD | 3,330.00 USD | 4,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 844,830.00 USD | 844,830.00 USD | 0.00 USD | 3,760.00 USD | 9,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0973` | 576,510.00 USD | 576,510.00 USD | 0.00 USD | 2,120.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0974` | 831,350.00 USD | 831,350.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0975` | 569,990.00 USD | 569,990.00 USD | 0.00 USD | 1,810.00 USD | 5,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0975` | 11,950.00 USD | 32,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0977` | 562,630.00 USD | 562,630.00 USD | 24,760.00 USD | 2,510.00 USD | 11,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0977` | 827,070.00 USD | 827,070.00 USD | 0.00 USD | 1,160.00 USD | 13,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0979` | 524,130.00 USD | 524,130.00 USD | 12,620.00 USD | 1,040.00 USD | 8.08 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0980` | 812,780.00 USD | 812,780.00 USD | 0.00 USD | 3,920.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0981` | 510,460.00 USD | 510,460.00 USD | 9,220.00 USD | 431.42 USD | 3,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0983` | 497,780.00 USD | 497,780.00 USD | 3,250.00 USD | 1,390.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 803,150.00 USD | 803,150.00 USD | 7,990.00 USD | 1,230.00 USD | 14,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0985` | 477,030.00 USD | 477,030.00 USD | 10,370.00 USD | 1,740.00 USD | 10,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0985` | 20,130.00 USD | 20,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0986` | 779,160.00 USD | 779,160.00 USD | 7,110.00 USD | 7,530.00 USD | 61,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0987` | 454,200.00 USD | 454,200.00 USD | 15,960.00 USD | 6,330.00 USD | 32,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0989` | 399,150.00 USD | 399,150.00 USD | 2,820.00 USD | 3,290.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 703,510.00 USD | 703,510.00 USD | 17,640.00 USD | 6,190.00 USD | 53,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0991` | 390,720.00 USD | 390,720.00 USD | 32,710.00 USD | 2,950.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0992` | 626,470.00 USD | 626,470.00 USD | 27,140.00 USD | 11,490.00 USD | 28,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0993` | 351,870.00 USD | 351,870.00 USD | 3,080.00 USD | 1,720.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0995` | 335,600.00 USD | 335,600.00 USD | 2,740.00 USD | 624.33 USD | 11,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 559,340.00 USD | 559,340.00 USD | 24,220.00 USD | 15,150.00 USD | 56,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0997` | 320,750.00 USD | 320,750.00 USD | 35,260.00 USD | 718.82 USD | 27,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0998` | 463,430.00 USD | 463,430.00 USD | 28,450.00 USD | 6,400.00 USD | 49,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0999` | 257,570.00 USD | 257,570.00 USD | 37,910.00 USD | 2,940.00 USD | 23,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1001` | 192,840.00 USD | 192,840.00 USD | 21,100.00 USD | 1,410.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 379,210.00 USD | 379,210.00 USD | 36,110.00 USD | 8,650.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1003` | 166,140.00 USD | 166,140.00 USD | 0.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1004` | 321,320.00 USD | 321,320.00 USD | 22,470.00 USD | 16,470.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1005` | 165,580.00 USD | 165,580.00 USD | 11,380.00 USD | 3,050.00 USD | 30,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1007` | 121,140.00 USD | 121,140.00 USD | 0.00 USD | 8,710.00 USD | 56,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 258,950.00 USD | 258,950.00 USD | 20,870.00 USD | 3,870.00 USD | 100,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1009` | 55,730.00 USD | 55,730.00 USD | 0.00 USD | 2,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1010` | 133,980.00 USD | 133,980.00 USD | 17,340.00 USD | 6,580.00 USD | 6,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1011` | 52,990.00 USD | 52,990.00 USD | 0.00 USD | 575.54 USD | 3,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1013` | 49,020.00 USD | 49,020.00 USD | 0.00 USD | 800.79 USD | 587.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 103,430.00 USD | 103,430.00 USD | 15,270.00 USD | 5,230.00 USD | 56,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1015` | 47,630.00 USD | 47,630.00 USD | 0.00 USD | 1,830.00 USD | 1,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1016` | 26,450.00 USD | 26,450.00 USD | 15,440.00 USD | 5,490.00 USD | 5,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1017` | 44,140.00 USD | 44,140.00 USD | 0.00 USD | 3,440.00 USD | 34,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1019` | 6,380.00 USD | 6,380.00 USD | 0.00 USD | 6,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1019` | 32,160.00 USD | 32,160.00 USD | 12,100.00 USD | 5,790.00 USD | 14,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1019` | 64,310.00 USD | 64,310.00 USD | 12,100.00 USD | 5,790.00 USD | 14,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1021` | 31,480.00 USD | 31,480.00 USD | 15,980.00 USD | 1,320.00 USD | 14,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1021` | 62,960.00 USD | 62,960.00 USD | 15,980.00 USD | 1,320.00 USD | 14,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1022` | 84,500.00 USD | 84,500.00 USD | 11,930.00 USD | 8,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1025` | 86,050.00 USD | 86,050.00 USD | 1,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1028` | 94,240.00 USD | 94,240.00 USD | 3,800.00 USD | 4,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1031` | 109,750.00 USD | 109,750.00 USD | 27,910.00 USD | 0.00 USD | 18,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1031` | 120,060.00 USD | 120,060.00 USD | 19,560.00 USD | 6,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1033` | 131,610.00 USD | 131,610.00 USD | 0.00 USD | 0.00 USD | 21,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1034` | 146,000.00 USD | 146,000.00 USD | 18,920.00 USD | 7,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1035` | 141,330.00 USD | 141,330.00 USD | 4,780.00 USD | 4,880.00 USD | 54.66 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1037` | 190,590.00 USD | 190,590.00 USD | 37,310.00 USD | 11,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1037` | 153,730.00 USD | 153,730.00 USD | 2,710.00 USD | 5,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1039` | 196,040.00 USD | 196,040.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1040` | 169,970.00 USD | 169,970.00 USD | 5,940.00 USD | 10,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1041` | 208,860.00 USD | 208,860.00 USD | 0.00 USD | 12,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1043` | 214,510.00 USD | 214,510.00 USD | 0.00 USD | 5,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1043` | 191,910.00 USD | 191,910.00 USD | 15,960.00 USD | 5,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1045` | 224,300.00 USD | 224,300.00 USD | 0.00 USD | 4,840.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1046` | 261,880.00 USD | 261,880.00 USD | 0.00 USD | 9,810.00 USD | 60,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1047` | 291,390.00 USD | 291,390.00 USD | 24,410.00 USD | 6,050.00 USD | 36,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1049` | 406,210.00 USD | 406,210.00 USD | 37,390.00 USD | 10,710.00 USD | 66,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1049` | 386,310.00 USD | 386,310.00 USD | 34,790.00 USD | 6,530.00 USD | 83,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1051` | 469,560.00 USD | 469,560.00 USD | 30,370.00 USD | 8,750.00 USD | 24,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1052` | 564,070.00 USD | 564,070.00 USD | 28,200.00 USD | 24,160.00 USD | 125,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1053` | 564,370.00 USD | 564,370.00 USD | 35,030.00 USD | 8,930.00 USD | 50,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1055` | 693,180.00 USD | 693,180.00 USD | 43,960.00 USD | 25,140.00 USD | 59,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1055` | 942,810.00 USD | 942,810.00 USD | 122,840.00 USD | 44,430.00 USD | 211,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1057` | 785,730.00 USD | 785,730.00 USD | 27,300.00 USD | 15,170.00 USD | 50,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1058` | 1,290,000.00 USD | 1,290,000.00 USD | 105,620.00 USD | 53,680.00 USD | 189,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1059` | 921,700.00 USD | 921,700.00 USD | 39,020.00 USD | 0.00 USD | 96,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1061` | 1,010,000.00 USD | 1,010,000.00 USD | 26,970.00 USD | 0.00 USD | 58,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1061` | 1,540,000.00 USD | 1,540,000.00 USD | 75,540.00 USD | 72,260.00 USD | 102,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1063` | 1,100,000.00 USD | 1,100,000.00 USD | 25,200.00 USD | 0.00 USD | 63,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1064` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 52,580.00 USD | 192,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1065` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 25,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1067` | 1,170,000.00 USD | 1,170,000.00 USD | 4,700.00 USD | 1,320.00 USD | 41,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1067` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 51,740.00 USD | 156,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1069` | 1,250,000.00 USD | 1,250,000.00 USD | 8,170.00 USD | 4,140.00 USD | 70,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1070` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 57,770.00 USD | 134,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1071` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 3,140.00 USD | 16,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1073` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 244.83 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1073` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 17,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1075` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 104.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1076` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 22,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1077` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 93.46 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1079` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1079` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 79.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1082` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 89.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1083` | 1,310,000.00 USD | 1,310,000.00 USD | 7,990.00 USD | 5,910.00 USD | 7,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1085` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 65,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1085` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1087` | 1,450,000.00 USD | 1,450,000.00 USD | 28,490.00 USD | 2,240.00 USD | 44,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1088` | 2,230,000.00 USD | 2,230,000.00 USD | 5,290.00 USD | 0.00 USD | 113.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1089` | 1,490,000.00 USD | 1,490,000.00 USD | 39,160.00 USD | 0.00 USD | 108.06 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1091` | 1,520,000.00 USD | 1,520,000.00 USD | 33,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1091` | 2,260,000.00 USD | 2,260,000.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1093` | 1,540,000.00 USD | 1,540,000.00 USD | 15,480.00 USD | 0.00 USD | 192.45 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1094` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1095` | 1,570,000.00 USD | 1,570,000.00 USD | 4,110.00 USD | 1,890.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1097` | 1,600,000.00 USD | 1,600,000.00 USD | 7,260.00 USD | 1,970.00 USD | 22,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1097` | 2,290,000.00 USD | 2,290,000.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1099` | 1,610,000.00 USD | 1,610,000.00 USD | 6,130.00 USD | 1,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1100` | 2,320,000.00 USD | 2,320,000.00 USD | 11,470.00 USD | 0.00 USD | 21,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1101` | 1,620,000.00 USD | 1,620,000.00 USD | 4,310.00 USD | 2,820.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1103` | 1,630,000.00 USD | 1,630,000.00 USD | 3,540.00 USD | 5,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 2,360,000.00 USD | 2,360,000.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1105` | 1,650,000.00 USD | 1,650,000.00 USD | 3,380.00 USD | 4,740.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1106` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 22,880.00 USD | 16,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1107` | 1,700,000.00 USD | 1,700,000.00 USD | 3,110.00 USD | 12,720.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1109` | 1,700,000.00 USD | 1,700,000.00 USD | 2,110.00 USD | 1,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1111` | 1,710,000.00 USD | 1,710,000.00 USD | 5,200.00 USD | 0.00 USD | 96.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1112` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1113` | 1,770,000.00 USD | 1,770,000.00 USD | 21,390.00 USD | 5,210.00 USD | 39,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1115` | 1,780,000.00 USD | 1,780,000.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1117` | 1,840,000.00 USD | 1,840,000.00 USD | 2,060.00 USD | 25,630.00 USD | 34,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1118` | 2,510,000.00 USD | 2,510,000.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1119` | 1,920,000.00 USD | 1,920,000.00 USD | 33,110.00 USD | 6,980.00 USD | 36,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1121` | 1,960,000.00 USD | 1,960,000.00 USD | 20,000.00 USD | 12,060.00 USD | 12,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 2,560,000.00 USD | 2,560,000.00 USD | 17,760.00 USD | 0.00 USD | 32,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1123` | 2,000,000.00 USD | 2,000,000.00 USD | 34,930.00 USD | 1,780.00 USD | 5,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1124` | 2,660,000.00 USD | 2,660,000.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1125` | 2,040,000.00 USD | 2,040,000.00 USD | 11,130.00 USD | 13,240.00 USD | 7,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1127` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 1,250.00 USD | 19,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1127` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1129` | 2,070,000.00 USD | 2,070,000.00 USD | 8,710.00 USD | 0.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1130` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 24,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1131` | 2,120,000.00 USD | 2,120,000.00 USD | 20,830.00 USD | 8,010.00 USD | 22,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1133` | 2,170,000.00 USD | 2,170,000.00 USD | 6,530.00 USD | 22,520.00 USD | 23,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 2,730,000.00 USD | 2,730,000.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1135` | 2,180,000.00 USD | 2,180,000.00 USD | 4,040.00 USD | 3,670.00 USD | 4,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1135` | 557.61 USD | 557.61 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1136` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1137` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 856.93 USD | 40.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1139` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 14,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1139` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1141` | 2,240,000.00 USD | 2,240,000.00 USD | 13,860.00 USD | 2,800.00 USD | 20,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1142` | 2,770,000.00 USD | 2,770,000.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1143` | 2,300,000.00 USD | 2,300,000.00 USD | 20,300.00 USD | 27,990.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1145` | 2,360,000.00 USD | 2,360,000.00 USD | 13,430.00 USD | 11,690.00 USD | 38,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 3,010,000.00 USD | 3,010,000.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1147` | 2,410,000.00 USD | 2,410,000.00 USD | 10,640.00 USD | 10,080.00 USD | 30,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1148` | 3,200,000.00 USD | 3,200,000.00 USD | 9,880.00 USD | 0.00 USD | 176,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1149` | 2,480,000.00 USD | 2,480,000.00 USD | 35,170.00 USD | 624.71 USD | 31,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1151` | 2,540,000.00 USD | 2,540,000.00 USD | 16,450.00 USD | 14,620.00 USD | 33,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 3,470,000.00 USD | 3,470,000.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1153` | 2,660,000.00 USD | 2,660,000.00 USD | 31,350.00 USD | 23,630.00 USD | 59,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1154` | 3,940,000.00 USD | 3,940,000.00 USD | 243,190.00 USD | 26,970.00 USD | 195,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1155` | 2,780,000.00 USD | 2,780,000.00 USD | 38,430.00 USD | 27,080.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1157` | 2,830,000.00 USD | 2,830,000.00 USD | 33,550.00 USD | 8,310.00 USD | 7,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 4,250,000.00 USD | 4,250,000.00 USD | 188,950.00 USD | 25,290.00 USD | 98,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1159` | 2,870,000.00 USD | 2,870,000.00 USD | 19,470.00 USD | 7,420.00 USD | 17,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1160` | 4,530,000.00 USD | 4,530,000.00 USD | 139,350.00 USD | 32,830.00 USD | 109,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1161` | 2,900,000.00 USD | 2,900,000.00 USD | 20,240.00 USD | 0.00 USD | 5,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1163` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 9,380.00 USD | 17,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 4,810,000.00 USD | 4,810,000.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1165` | 2,930,000.00 USD | 2,930,000.00 USD | 4,990.00 USD | 5,320.00 USD | 1,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1166` | 5,030,000.00 USD | 5,030,000.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1167` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 7,220.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1169` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 2,440.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 5,250,000.00 USD | 5,250,000.00 USD | 82,770.00 USD | 26,150.00 USD | 112,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1171` | 2,970,000.00 USD | 2,970,000.00 USD | 13,800.00 USD | 0.00 USD | 4,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1172` | 5,380,000.00 USD | 5,380,000.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1173` | 2,980,000.00 USD | 2,980,000.00 USD | 2,840.00 USD | 5,440.00 USD | 4,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1175` | 3,020,000.00 USD | 3,020,000.00 USD | 9,530.00 USD | 9,020.00 USD | 19,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 5,550,000.00 USD | 5,550,000.00 USD | 72,770.00 USD | 17,930.00 USD | 81,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1177` | 3,060,000.00 USD | 3,060,000.00 USD | 14,360.00 USD | 8,560.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1178` | 5,720,000.00 USD | 5,720,000.00 USD | 89,510.00 USD | 23,660.00 USD | 55,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1179` | 3,080,000.00 USD | 3,080,000.00 USD | 10,640.00 USD | 3,990.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1181` | 3,120,000.00 USD | 3,120,000.00 USD | 12,400.00 USD | 4,120.00 USD | 15,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 5,810,000.00 USD | 5,810,000.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1183` | 3,130,000.00 USD | 3,130,000.00 USD | 7,050.00 USD | 677.63 USD | 4,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1184` | 5,870,000.00 USD | 5,870,000.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1185` | 3,140,000.00 USD | 3,140,000.00 USD | 4,390.00 USD | 5,850.00 USD | 6,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1187` | 3,160,000.00 USD | 3,160,000.00 USD | 2,150.00 USD | 3,330.00 USD | 9,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 5,950,000.00 USD | 5,950,000.00 USD | 5,620.00 USD | 17,120.00 USD | 54,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1189` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 2,120.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1190` | 6,100,000.00 USD | 6,100,000.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1191` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 1,810.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1193` | 3,180,000.00 USD | 3,180,000.00 USD | 1,980.00 USD | 1,040.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 6,180,000.00 USD | 6,180,000.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1195` | 3,190,000.00 USD | 3,190,000.00 USD | 6,310.00 USD | 1,470.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1196` | 6,240,000.00 USD | 6,240,000.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1197` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 1,040.00 USD | 93.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1199` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 431.42 USD | 3,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 6,330,000.00 USD | 6,330,000.00 USD | 9,100.00 USD | 13,190.00 USD | 67,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1201` | 3,210,000.00 USD | 3,210,000.00 USD | 3,250.00 USD | 1,390.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1202` | 6,520,000.00 USD | 6,520,000.00 USD | 138,430.00 USD | 21,430.00 USD | 32,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1203` | 3,220,000.00 USD | 3,220,000.00 USD | 5,670.00 USD | 413.94 USD | 2,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1205` | 3,220,000.00 USD | 3,220,000.00 USD | 2,250.00 USD | 1,670.00 USD | 741.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 6,860,000.00 USD | 6,860,000.00 USD | 132,960.00 USD | 72,910.00 USD | 130,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1207` | 3,230,000.00 USD | 3,230,000.00 USD | 5,540.00 USD | 524.23 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1208` | 6,990,000.00 USD | 6,990,000.00 USD | 39,480.00 USD | 25,720.00 USD | 66,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1209` | 3,240,000.00 USD | 3,240,000.00 USD | 2,820.00 USD | 3,290.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1211` | 3,250,000.00 USD | 3,250,000.00 USD | 4,800.00 USD | 2,950.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 7,200,000.00 USD | 7,200,000.00 USD | 72,500.00 USD | 25,920.00 USD | 111,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1213` | 3,270,000.00 USD | 3,270,000.00 USD | 5,870.00 USD | 1,720.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1214` | 7,320,000.00 USD | 7,320,000.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1215` | 3,280,000.00 USD | 3,280,000.00 USD | 1,650.00 USD | 0.00 USD | 5,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1217` | 3,290,000.00 USD | 3,290,000.00 USD | 1,090.00 USD | 624.33 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 7,370,000.00 USD | 7,370,000.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1219` | 3,300,000.00 USD | 3,300,000.00 USD | 2,320.00 USD | 718.82 USD | 10,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1220` | 7,480,000.00 USD | 7,480,000.00 USD | 45,700.00 USD | 10,970.00 USD | 54,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1221` | 3,310,000.00 USD | 3,310,000.00 USD | 7,970.00 USD | 2,940.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1223` | 3,320,000.00 USD | 3,320,000.00 USD | 2,660.00 USD | 1,410.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 7,640,000.00 USD | 7,640,000.00 USD | 76,930.00 USD | 36,110.00 USD | 50,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1225` | 3,320,000.00 USD | 3,320,000.00 USD | 1,840.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 721.08 USD | 1,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1226` | 7,740,000.00 USD | 7,740,000.00 USD | 54,940.00 USD | 32,070.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 7,920,000.00 USD | 7,920,000.00 USD | 71,850.00 USD | 38,040.00 USD | 79,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1232` | 8,090,000.00 USD | 8,090,000.00 USD | 67,800.00 USD | 28,560.00 USD | 68,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1235` | 8,130,000.00 USD | 8,130,000.00 USD | 15,040.00 USD | 5,390.00 USD | 17,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1235` | 9,170.00 USD | 10,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1238` | 8,140,000.00 USD | 8,140,000.00 USD | 8,310.00 USD | 3,610.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1241` | 8,160,000.00 USD | 8,160,000.00 USD | 11,380.00 USD | 1,380.00 USD | 7,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1244` | 8,210,000.00 USD | 8,210,000.00 USD | 26,540.00 USD | 8,130.00 USD | 9,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1247` | 8,250,000.00 USD | 8,250,000.00 USD | 7,900.00 USD | 18,280.00 USD | 17,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1250` | 8,270,000.00 USD | 8,270,000.00 USD | 8,540.00 USD | 7,270.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1253` | 8,290,000.00 USD | 8,290,000.00 USD | 1,550.00 USD | 0.00 USD | 16,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1256` | 8,310,000.00 USD | 8,310,000.00 USD | 11,990.00 USD | 11,420.00 USD | 220.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1259` | 8,320,000.00 USD | 8,320,000.00 USD | 5,870.00 USD | 1,190.00 USD | 151.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1262` | 8,330,000.00 USD | 8,330,000.00 USD | 4,270.00 USD | 0.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1265` | 8,340,000.00 USD | 8,340,000.00 USD | 2,710.00 USD | 0.00 USD | 7,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1268` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1271` | 8,350,000.00 USD | 8,350,000.00 USD | 5,940.00 USD | 0.00 USD | 30.15 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1274` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 0.00 USD | 12.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1277` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 0.00 USD | 31.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1280` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 0.00 USD | 6,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1355` | 1,330.00 USD | 11,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1465` | 25,730.00 USD | 37,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1525` | 6,090.00 USD | 43,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1555` | 15,550.00 USD | 59,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1565` | 550.61 USD | 59,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1695` | 169.25 USD | 59,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1865` | 167.85 USD | 60,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1945` | 109.31 USD | 60,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1995` | 964.32 USD | 61,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

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
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0878` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 1,370.00 USD | 4,930.00 USD | 27,260.00 USD |
| `1D` | `0.0881` | 735,460.00 USD | 0.00 USD | 735,460.00 USD | 2,400.00 USD | 1,300.00 USD | 4,340.00 USD |
| `7D` | `0.0881` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 3,770.00 USD | 2,660.00 USD | 12,940.00 USD |
| `1D` | `0.0883` | 727,420.00 USD | 0.00 USD | 727,420.00 USD | 2,370.00 USD | 659.34 USD | 5,980.00 USD |
| `7D` | `0.0884` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 7,040.00 USD | 4,640.00 USD | 11,870.00 USD |
| `1D` | `0.0885` | 718,410.00 USD | 0.00 USD | 718,410.00 USD | 0.00 USD | 312.16 USD | 2,520.00 USD |
| `1D` | `0.0887` | 715,580.00 USD | 0.00 USD | 715,580.00 USD | 1,740.00 USD | 655.48 USD | 4,540.00 USD |
| `7D` | `0.0887` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD |
| `1D` | `0.0889` | 708,650.00 USD | 0.00 USD | 708,650.00 USD | 727.20 USD | 1,690.00 USD | 2,110.00 USD |
| `7D` | `0.0890` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 14,610.00 USD | 4,470.00 USD | 3,680.00 USD |
| `1D` | `0.0891` | 704,130.00 USD | 0.00 USD | 704,130.00 USD | 1,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0893` | 702,800.00 USD | 0.00 USD | 702,800.00 USD | 983.61 USD | 0.00 USD | 542.23 USD |
| `7D` | `0.0893` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD |
| `1D` | `0.0895` | 701,280.00 USD | 0.00 USD | 701,280.00 USD | 0.00 USD | 215.06 USD | 394.61 USD |
| `7D` | `0.0896` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 5,760.00 USD | 611.80 USD | 6,870.00 USD |
| `1D` | `0.0897` | 700,670.00 USD | 0.00 USD | 700,670.00 USD | 0.00 USD | 772.87 USD | 0.02 USD |
| `1D` | `0.0899` | 699,890.00 USD | 0.00 USD | 699,890.00 USD | 0.00 USD | 287.77 USD | 601.21 USD |
| `7D` | `0.0899` | 987,910.00 USD | 0.00 USD | 987,910.00 USD | 3,390.00 USD | 927.82 USD | 4,490.00 USD |
| `1D` | `0.0901` | 699,000.00 USD | 0.00 USD | 699,000.00 USD | 2,450.00 USD | 0.00 USD | 293.66 USD |
| `7D` | `0.0902` | 979,110.00 USD | 0.00 USD | 979,110.00 USD | 2,270.00 USD | 910.78 USD | 1,210.00 USD |
| `1D` | `0.0903` | 696,260.00 USD | 0.00 USD | 696,260.00 USD | 831.11 USD | 2,190.00 USD | 1,070.00 USD |
| `1D` | `0.0905` | 692,170.00 USD | 0.00 USD | 692,170.00 USD | 413.91 USD | 998.41 USD | 2,840.00 USD |
| `7D` | `0.0905` | 974,710.00 USD | 0.00 USD | 974,710.00 USD | 10,350.00 USD | 996.61 USD | 4,080.00 USD |
| `1D` | `0.0907` | 687,920.00 USD | 0.00 USD | 687,920.00 USD | 2,290.00 USD | 909.44 USD | 974.67 USD |
| `7D` | `0.0908` | 959,280.00 USD | 0.00 USD | 959,280.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD |
| `1D` | `0.0909` | 683,750.00 USD | 0.00 USD | 683,750.00 USD | 938.76 USD | 499.80 USD | 778.75 USD |
| `1D` | `0.0911` | 681,530.00 USD | 0.00 USD | 681,530.00 USD | 5,580.00 USD | 778.50 USD | 5.42 USD |
| `7D` | `0.0911` | 947,890.00 USD | 0.00 USD | 947,890.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD |
| `1D` | `0.0913` | 675,170.00 USD | 0.00 USD | 675,170.00 USD | 0.00 USD | 0.00 USD | 787.25 USD |
| `7D` | `0.0914` | 944,610.00 USD | 0.00 USD | 944,610.00 USD | 1,670.00 USD | 903.90 USD | 45.81 USD |
| `1D` | `0.0915` | 674,380.00 USD | 0.00 USD | 674,380.00 USD | 6,590.00 USD | 0.00 USD | 46.43 USD |
| `1D` | `0.0917` | 667,740.00 USD | 0.00 USD | 667,740.00 USD | 2,550.00 USD | 0.00 USD | 2.87 USD |
| `7D` | `0.0917` | 941,980.00 USD | 0.00 USD | 941,980.00 USD | 0.00 USD | 0.00 USD | 1,740.00 USD |
| `1D` | `0.0919` | 665,190.00 USD | 0.00 USD | 665,190.00 USD | 3,690.00 USD | 0.00 USD | 8.94 USD |
| `1D` | `0.0923` | 661,490.00 USD | 0.00 USD | 661,490.00 USD | 0.00 USD | 0.00 USD | 3,260.00 USD |
| `7D` | `0.0923` | 940,240.00 USD | 0.00 USD | 940,240.00 USD | 0.00 USD | 0.00 USD | 10,560.00 USD |
| `1D` | `0.0925` | 658,240.00 USD | 0.00 USD | 658,240.00 USD | 3,270.00 USD | 1,660.00 USD | 11,180.00 USD |
| `7D` | `0.0926` | 929,690.00 USD | 0.00 USD | 929,690.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD |
| `7D` | `0.0932` | 919,710.00 USD | 0.00 USD | 919,710.00 USD | 0.00 USD | 0.00 USD | 12,240.00 USD |
| `1D` | `0.0933` | 642,130.00 USD | 0.00 USD | 642,130.00 USD | 0.00 USD | 0.00 USD | 6,860.00 USD |
| `7D` | `0.0935` | 907,480.00 USD | 0.00 USD | 907,480.00 USD | 0.00 USD | 1,320.00 USD | 6,490.00 USD |
| `1D` | `0.0937` | 635,270.00 USD | 0.00 USD | 635,270.00 USD | 0.00 USD | 0.00 USD | 64.09 USD |
| `7D` | `0.0938` | 899,670.00 USD | 0.00 USD | 899,670.00 USD | 0.00 USD | 0.00 USD | 8.57 USD |
| `1D` | `0.0939` | 635,200.00 USD | 0.00 USD | 635,200.00 USD | 0.00 USD | 0.00 USD | 76.92 USD |
| `7D` | `0.0941` | 899,660.00 USD | 0.00 USD | 899,660.00 USD | 2,050.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `0.0944` | 894,590.00 USD | 0.00 USD | 894,590.00 USD | 1,870.00 USD | 0.00 USD | 7,520.00 USD |
| `1D` | `0.0947` | 635,130.00 USD | 0.00 USD | 635,130.00 USD | 0.00 USD | 0.00 USD | 69.61 USD |
| `7D` | `0.0947` | 885,190.00 USD | 0.00 USD | 885,190.00 USD | 3,790.00 USD | 1,810.00 USD | 112.06 USD |
| `7D` | `0.0950` | 879,480.00 USD | 0.00 USD | 879,480.00 USD | 3,770.00 USD | 0.00 USD | 6,660.00 USD |
| `1D` | `0.0953` | 635,060.00 USD | 0.00 USD | 635,060.00 USD | 0.00 USD | 0.00 USD | 108.06 USD |
| `7D` | `0.0953` | 869,050.00 USD | 0.00 USD | 869,050.00 USD | 0.00 USD | 0.00 USD | 4.65 USD |
| `1D` | `0.0955` | 634,950.00 USD | 0.00 USD | 634,950.00 USD | 0.00 USD | 1,180.00 USD | 166.88 USD |
| `7D` | `0.0959` | 869,040.00 USD | 0.00 USD | 869,040.00 USD | 0.00 USD | 1,140.00 USD | 115.48 USD |
| `1D` | `0.0961` | 633,600.00 USD | 0.00 USD | 633,600.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0962` | 867,790.00 USD | 0.00 USD | 867,790.00 USD | 0.00 USD | 0.00 USD | 121.64 USD |
| `1D` | `0.0963` | 631,520.00 USD | 0.00 USD | 631,520.00 USD | 0.00 USD | 0.00 USD | 1.02 USD |
| `1D` | `0.0965` | 631,520.00 USD | 0.00 USD | 631,520.00 USD | 1,280.00 USD | 282.32 USD | 1,880.00 USD |
| `1D` | `0.0967` | 628,080.00 USD | 0.00 USD | 628,080.00 USD | 2,660.00 USD | 1,100.00 USD | 7,500.00 USD |
| `7D` | `0.0968` | 867,670.00 USD | 0.00 USD | 867,670.00 USD | 7,490.00 USD | 3,720.00 USD | 11,630.00 USD |
| `1D` | `0.0969` | 616,810.00 USD | 0.00 USD | 616,810.00 USD | 4,590.00 USD | 2,640.00 USD | 9,010.00 USD |
| `1D` | `0.0971` | 600,570.00 USD | 0.00 USD | 600,570.00 USD | 16,100.00 USD | 3,330.00 USD | 4,640.00 USD |
| `7D` | `0.0971` | 844,830.00 USD | 0.00 USD | 844,830.00 USD | 0.00 USD | 3,760.00 USD | 9,720.00 USD |
| `1D` | `0.0973` | 576,510.00 USD | 0.00 USD | 576,510.00 USD | 0.00 USD | 2,120.00 USD | 4,400.00 USD |
| `7D` | `0.0974` | 831,350.00 USD | 0.00 USD | 831,350.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD |
| `1D` | `0.0975` | 569,990.00 USD | 0.00 USD | 569,990.00 USD | 0.00 USD | 1,810.00 USD | 5,550.00 USD |
| `1D` | `0.0977` | 562,630.00 USD | 0.00 USD | 562,630.00 USD | 24,760.00 USD | 2,510.00 USD | 11,230.00 USD |
| `7D` | `0.0977` | 827,070.00 USD | 0.00 USD | 827,070.00 USD | 0.00 USD | 1,160.00 USD | 13,130.00 USD |
| `1D` | `0.0979` | 524,130.00 USD | 0.00 USD | 524,130.00 USD | 12,620.00 USD | 1,040.00 USD | 8.08 USD |
| `7D` | `0.0980` | 812,780.00 USD | 0.00 USD | 812,780.00 USD | 0.00 USD | 3,920.00 USD | 5,710.00 USD |
| `1D` | `0.0981` | 510,460.00 USD | 0.00 USD | 510,460.00 USD | 9,220.00 USD | 431.42 USD | 3,030.00 USD |
| `1D` | `0.0983` | 497,780.00 USD | 0.00 USD | 497,780.00 USD | 3,250.00 USD | 1,390.00 USD | 16,110.00 USD |
| `7D` | `0.0983` | 803,150.00 USD | 0.00 USD | 803,150.00 USD | 7,990.00 USD | 1,230.00 USD | 14,770.00 USD |
| `1D` | `0.0985` | 477,030.00 USD | 0.00 USD | 477,030.00 USD | 10,370.00 USD | 1,740.00 USD | 10,720.00 USD |
| `7D` | `0.0986` | 779,160.00 USD | 0.00 USD | 779,160.00 USD | 7,110.00 USD | 7,530.00 USD | 61,010.00 USD |
| `1D` | `0.0987` | 454,200.00 USD | 0.00 USD | 454,200.00 USD | 15,960.00 USD | 6,330.00 USD | 32,760.00 USD |
| `1D` | `0.0989` | 399,150.00 USD | 0.00 USD | 399,150.00 USD | 2,820.00 USD | 3,290.00 USD | 2,310.00 USD |
| `7D` | `0.0989` | 703,510.00 USD | 0.00 USD | 703,510.00 USD | 17,640.00 USD | 6,190.00 USD | 53,200.00 USD |
| `1D` | `0.0991` | 390,720.00 USD | 0.00 USD | 390,720.00 USD | 32,710.00 USD | 2,950.00 USD | 3,200.00 USD |
| `7D` | `0.0992` | 626,470.00 USD | 0.00 USD | 626,470.00 USD | 27,140.00 USD | 11,490.00 USD | 28,490.00 USD |
| `1D` | `0.0993` | 351,870.00 USD | 0.00 USD | 351,870.00 USD | 3,080.00 USD | 1,720.00 USD | 11,460.00 USD |
| `1D` | `0.0995` | 335,600.00 USD | 0.00 USD | 335,600.00 USD | 2,740.00 USD | 624.33 USD | 11,480.00 USD |
| `7D` | `0.0995` | 559,340.00 USD | 0.00 USD | 559,340.00 USD | 24,220.00 USD | 15,150.00 USD | 56,550.00 USD |
| `1D` | `0.0997` | 320,750.00 USD | 0.00 USD | 320,750.00 USD | 35,260.00 USD | 718.82 USD | 27,200.00 USD |
| `7D` | `0.0998` | 463,430.00 USD | 0.00 USD | 463,430.00 USD | 28,450.00 USD | 6,400.00 USD | 49,360.00 USD |
| `1D` | `0.0999` | 257,570.00 USD | 0.00 USD | 257,570.00 USD | 37,910.00 USD | 2,940.00 USD | 23,880.00 USD |
| `1D` | `0.1001` | 192,840.00 USD | 0.00 USD | 192,840.00 USD | 21,100.00 USD | 1,410.00 USD | 4,200.00 USD |
| `7D` | `0.1001` | 379,210.00 USD | 0.00 USD | 379,210.00 USD | 36,110.00 USD | 8,650.00 USD | 13,120.00 USD |
| `1D` | `0.1003` | 166,140.00 USD | 0.00 USD | 166,140.00 USD | 0.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1004` | 321,320.00 USD | 0.00 USD | 321,320.00 USD | 22,470.00 USD | 16,470.00 USD | 23,430.00 USD |
| `1D` | `0.1005` | 165,580.00 USD | 0.00 USD | 165,580.00 USD | 11,380.00 USD | 3,050.00 USD | 30,010.00 USD |
| `1D` | `0.1007` | 121,140.00 USD | 0.00 USD | 121,140.00 USD | 0.00 USD | 8,710.00 USD | 56,700.00 USD |
| `7D` | `0.1007` | 258,950.00 USD | 0.00 USD | 258,950.00 USD | 20,870.00 USD | 3,870.00 USD | 100,230.00 USD |
| `1D` | `0.1009` | 55,730.00 USD | 0.00 USD | 55,730.00 USD | 0.00 USD | 2,750.00 USD | 0.00 USD |
| `7D` | `0.1010` | 133,980.00 USD | 0.00 USD | 133,980.00 USD | 17,340.00 USD | 6,580.00 USD | 6,630.00 USD |
| `1D` | `0.1011` | 52,990.00 USD | 0.00 USD | 52,990.00 USD | 0.00 USD | 575.54 USD | 3,390.00 USD |
| `1D` | `0.1013` | 49,020.00 USD | 0.00 USD | 49,020.00 USD | 0.00 USD | 800.79 USD | 587.32 USD |
| `7D` | `0.1013` | 103,430.00 USD | 0.00 USD | 103,430.00 USD | 15,270.00 USD | 5,230.00 USD | 56,480.00 USD |
| `1D` | `0.1015` | 47,630.00 USD | 0.00 USD | 47,630.00 USD | 0.00 USD | 1,830.00 USD | 1,660.00 USD |
| `7D` | `0.1016` | 26,450.00 USD | 0.00 USD | 26,450.00 USD | 15,440.00 USD | 5,490.00 USD | 5,510.00 USD |
| `1D` | `0.1017` | 44,140.00 USD | 0.00 USD | 44,140.00 USD | 0.00 USD | 3,440.00 USD | 34,320.00 USD |
| `1D` | `0.1019` | 6,380.00 USD | 0.00 USD | 6,380.00 USD | 0.00 USD | 6,380.00 USD | 0.00 USD |
| `7D` | `0.1019` | 32,160.00 USD | 32,160.00 USD | 0.00 USD | 12,100.00 USD | 5,790.00 USD | 14,260.00 USD |
| `7D` | `0.1019` | 64,310.00 USD | 64,310.00 USD | 0.00 USD | 12,100.00 USD | 5,790.00 USD | 14,260.00 USD |
| `1D` | `0.1021` | 31,480.00 USD | 31,480.00 USD | 0.00 USD | 15,980.00 USD | 1,320.00 USD | 14,190.00 USD |
| `1D` | `0.1021` | 62,960.00 USD | 62,960.00 USD | 0.00 USD | 15,980.00 USD | 1,320.00 USD | 14,190.00 USD |
| `7D` | `0.1022` | 84,500.00 USD | 84,500.00 USD | 0.00 USD | 11,930.00 USD | 8,250.00 USD | 0.00 USD |
| `7D` | `0.1025` | 86,050.00 USD | 86,050.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1028` | 94,240.00 USD | 94,240.00 USD | 0.00 USD | 3,800.00 USD | 4,390.00 USD | 0.00 USD |
| `1D` | `0.1031` | 109,750.00 USD | 109,750.00 USD | 0.00 USD | 27,910.00 USD | 0.00 USD | 18,880.00 USD |
| `7D` | `0.1031` | 120,060.00 USD | 120,060.00 USD | 0.00 USD | 19,560.00 USD | 6,260.00 USD | 0.00 USD |
| `1D` | `0.1033` | 131,610.00 USD | 131,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,860.00 USD |
| `7D` | `0.1034` | 146,000.00 USD | 146,000.00 USD | 0.00 USD | 18,920.00 USD | 7,030.00 USD | 0.00 USD |
| `1D` | `0.1035` | 141,330.00 USD | 141,330.00 USD | 0.00 USD | 4,780.00 USD | 4,880.00 USD | 54.66 USD |
| `1D` | `0.1037` | 190,590.00 USD | 190,590.00 USD | 0.00 USD | 37,310.00 USD | 11,960.00 USD | 0.00 USD |
| `7D` | `0.1037` | 153,730.00 USD | 153,730.00 USD | 0.00 USD | 2,710.00 USD | 5,010.00 USD | 0.00 USD |
| `1D` | `0.1039` | 196,040.00 USD | 196,040.00 USD | 0.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD |
| `7D` | `0.1040` | 169,970.00 USD | 169,970.00 USD | 0.00 USD | 5,940.00 USD | 10,300.00 USD | 0.00 USD |
| `1D` | `0.1041` | 208,860.00 USD | 208,860.00 USD | 0.00 USD | 0.00 USD | 12,830.00 USD | 0.00 USD |
| `1D` | `0.1043` | 214,510.00 USD | 214,510.00 USD | 0.00 USD | 0.00 USD | 5,650.00 USD | 0.00 USD |
| `7D` | `0.1043` | 191,910.00 USD | 191,910.00 USD | 0.00 USD | 15,960.00 USD | 5,980.00 USD | 0.00 USD |
| `1D` | `0.1045` | 224,300.00 USD | 224,300.00 USD | 0.00 USD | 0.00 USD | 4,840.00 USD | 4,950.00 USD |
| `7D` | `0.1046` | 261,880.00 USD | 261,880.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD | 60,160.00 USD |
| `1D` | `0.1047` | 291,390.00 USD | 291,390.00 USD | 0.00 USD | 24,410.00 USD | 6,050.00 USD | 36,620.00 USD |
| `1D` | `0.1049` | 406,210.00 USD | 406,210.00 USD | 0.00 USD | 37,390.00 USD | 10,710.00 USD | 66,730.00 USD |
| `7D` | `0.1049` | 386,310.00 USD | 386,310.00 USD | 0.00 USD | 34,790.00 USD | 6,530.00 USD | 83,110.00 USD |
| `1D` | `0.1051` | 469,560.00 USD | 469,560.00 USD | 0.00 USD | 30,370.00 USD | 8,750.00 USD | 24,230.00 USD |
| `7D` | `0.1052` | 564,070.00 USD | 564,070.00 USD | 0.00 USD | 28,200.00 USD | 24,160.00 USD | 125,400.00 USD |
| `1D` | `0.1053` | 564,370.00 USD | 564,370.00 USD | 0.00 USD | 35,030.00 USD | 8,930.00 USD | 50,850.00 USD |
| `1D` | `0.1055` | 693,180.00 USD | 693,180.00 USD | 0.00 USD | 43,960.00 USD | 25,140.00 USD | 59,710.00 USD |
| `7D` | `0.1055` | 942,810.00 USD | 942,810.00 USD | 0.00 USD | 122,840.00 USD | 44,430.00 USD | 211,460.00 USD |
| `1D` | `0.1057` | 785,730.00 USD | 785,730.00 USD | 0.00 USD | 27,300.00 USD | 15,170.00 USD | 50,080.00 USD |
| `7D` | `0.1058` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 105,620.00 USD | 53,680.00 USD | 189,110.00 USD |
| `1D` | `0.1059` | 921,700.00 USD | 921,700.00 USD | 0.00 USD | 39,020.00 USD | 0.00 USD | 96,940.00 USD |
| `1D` | `0.1061` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 26,970.00 USD | 0.00 USD | 58,940.00 USD |
| `7D` | `0.1061` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 75,540.00 USD | 72,260.00 USD | 102,650.00 USD |
| `1D` | `0.1063` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 25,200.00 USD | 0.00 USD | 63,060.00 USD |
| `7D` | `0.1064` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 52,580.00 USD | 192,520.00 USD |
| `1D` | `0.1065` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25,740.00 USD |
| `1D` | `0.1067` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 4,700.00 USD | 1,320.00 USD | 41,190.00 USD |
| `7D` | `0.1067` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 51,740.00 USD | 156,150.00 USD |
| `1D` | `0.1069` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 8,170.00 USD | 4,140.00 USD | 70,600.00 USD |
| `7D` | `0.1070` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 57,770.00 USD | 134,670.00 USD |
| `1D` | `0.1071` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 3,140.00 USD | 16,220.00 USD |
| `1D` | `0.1073` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 244.83 USD |
| `7D` | `0.1073` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 17,700.00 USD | 0.00 USD |
| `1D` | `0.1075` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 104.34 USD |
| `7D` | `0.1076` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,500.00 USD |
| `1D` | `0.1077` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 93.46 USD |
| `1D` | `0.1079` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,160.00 USD |
| `7D` | `0.1079` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 79.36 USD |
| `7D` | `0.1082` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 89.24 USD |
| `1D` | `0.1083` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 7,990.00 USD | 5,910.00 USD | 7,180.00 USD |
| `1D` | `0.1085` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65,020.00 USD |
| `7D` | `0.1085` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1087` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 28,490.00 USD | 2,240.00 USD | 44,670.00 USD |
| `7D` | `0.1088` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 5,290.00 USD | 0.00 USD | 113.96 USD |
| `1D` | `0.1089` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 39,160.00 USD | 0.00 USD | 108.06 USD |
| `1D` | `0.1091` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 33,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1091` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD |
| `1D` | `0.1093` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 15,480.00 USD | 0.00 USD | 192.45 USD |
| `7D` | `0.1094` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD |
| `1D` | `0.1095` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 21,520.00 USD |
| `1D` | `0.1097` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 7,260.00 USD | 1,970.00 USD | 22,790.00 USD |
| `7D` | `0.1097` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1099` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 6,130.00 USD | 1,940.00 USD | 0.00 USD |
| `7D` | `0.1100` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 21,840.00 USD |
| `1D` | `0.1101` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 4,310.00 USD | 2,820.00 USD | 4,290.00 USD |
| `1D` | `0.1103` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 3,540.00 USD | 5,640.00 USD | 0.00 USD |
| `7D` | `0.1103` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1105` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 3,380.00 USD | 4,740.00 USD | 10,700.00 USD |
| `7D` | `0.1106` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 22,880.00 USD | 16,040.00 USD |
| `1D` | `0.1107` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 3,110.00 USD | 12,720.00 USD | 35,750.00 USD |
| `1D` | `0.1109` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 2,110.00 USD | 1,120.00 USD | 0.00 USD |
| `7D` | `0.1109` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD |
| `1D` | `0.1111` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 5,200.00 USD | 0.00 USD | 96.09 USD |
| `7D` | `0.1112` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD |
| `1D` | `0.1113` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 21,390.00 USD | 5,210.00 USD | 39,070.00 USD |
| `1D` | `0.1115` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1117` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 2,060.00 USD | 25,630.00 USD | 34,770.00 USD |
| `7D` | `0.1118` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD |
| `1D` | `0.1119` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 33,110.00 USD | 6,980.00 USD | 36,740.00 USD |
| `1D` | `0.1121` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 20,000.00 USD | 12,060.00 USD | 12,320.00 USD |
| `7D` | `0.1121` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 17,760.00 USD | 0.00 USD | 32,100.00 USD |
| `1D` | `0.1123` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 34,930.00 USD | 1,780.00 USD | 5,940.00 USD |
| `7D` | `0.1124` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD |
| `1D` | `0.1125` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 11,130.00 USD | 13,240.00 USD | 7,950.00 USD |
| `1D` | `0.1127` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 1,250.00 USD | 19,520.00 USD |
| `7D` | `0.1127` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD |
| `1D` | `0.1129` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 8,710.00 USD | 0.00 USD | 3,210.00 USD |
| `7D` | `0.1130` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,260.00 USD |
| `1D` | `0.1131` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 20,830.00 USD | 8,010.00 USD | 22,800.00 USD |
| `1D` | `0.1133` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 6,530.00 USD | 22,520.00 USD | 23,470.00 USD |
| `7D` | `0.1133` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD |
| `1D` | `0.1135` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 4,040.00 USD | 3,670.00 USD | 4,090.00 USD |
| `7D` | `0.1136` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD |
| `1D` | `0.1137` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 856.93 USD | 40.44 USD |
| `1D` | `0.1139` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,270.00 USD |
| `7D` | `0.1139` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD |
| `1D` | `0.1141` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 13,860.00 USD | 2,800.00 USD | 20,340.00 USD |
| `7D` | `0.1142` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD |
| `1D` | `0.1143` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 20,300.00 USD | 27,990.00 USD | 11,820.00 USD |
| `1D` | `0.1145` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 13,430.00 USD | 11,690.00 USD | 38,100.00 USD |
| `7D` | `0.1145` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD |
| `1D` | `0.1147` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 10,640.00 USD | 10,080.00 USD | 30,680.00 USD |
| `7D` | `0.1148` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 176,010.00 USD |
| `1D` | `0.1149` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 35,170.00 USD | 624.71 USD | 31,820.00 USD |
| `1D` | `0.1151` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 16,450.00 USD | 14,620.00 USD | 33,180.00 USD |
| `7D` | `0.1151` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD |
| `1D` | `0.1153` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 31,350.00 USD | 23,630.00 USD | 59,030.00 USD |
| `7D` | `0.1154` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 243,190.00 USD | 26,970.00 USD | 195,390.00 USD |
| `1D` | `0.1155` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 38,430.00 USD | 27,080.00 USD | 54,030.00 USD |
| `1D` | `0.1157` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 33,550.00 USD | 8,310.00 USD | 7,870.00 USD |
| `7D` | `0.1157` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 188,950.00 USD | 25,290.00 USD | 98,310.00 USD |
| `1D` | `0.1159` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 19,470.00 USD | 7,420.00 USD | 17,950.00 USD |
| `7D` | `0.1160` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 139,350.00 USD | 32,830.00 USD | 109,320.00 USD |
| `1D` | `0.1161` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 20,240.00 USD | 0.00 USD | 5,160.00 USD |
| `1D` | `0.1163` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 9,380.00 USD | 17,460.00 USD |
| `7D` | `0.1163` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD |
| `1D` | `0.1165` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 4,990.00 USD | 5,320.00 USD | 1,840.00 USD |
| `7D` | `0.1166` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD |
| `1D` | `0.1167` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 7,220.00 USD | 6,170.00 USD |
| `1D` | `0.1169` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 2,440.00 USD | 2,290.00 USD |
| `7D` | `0.1169` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 82,770.00 USD | 26,150.00 USD | 112,810.00 USD |
| `1D` | `0.1171` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 13,800.00 USD | 0.00 USD | 4,510.00 USD |
| `7D` | `0.1172` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD |
| `1D` | `0.1173` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 2,840.00 USD | 5,440.00 USD | 4,840.00 USD |
| `1D` | `0.1175` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 9,530.00 USD | 9,020.00 USD | 19,930.00 USD |
| `7D` | `0.1175` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 72,770.00 USD | 17,930.00 USD | 81,630.00 USD |
| `1D` | `0.1177` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 14,360.00 USD | 8,560.00 USD | 16,650.00 USD |
| `7D` | `0.1178` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 89,510.00 USD | 23,660.00 USD | 55,770.00 USD |
| `1D` | `0.1179` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 10,640.00 USD | 3,990.00 USD | 5,770.00 USD |
| `1D` | `0.1181` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 12,400.00 USD | 4,120.00 USD | 15,670.00 USD |
| `7D` | `0.1181` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD |
| `1D` | `0.1183` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 7,050.00 USD | 677.63 USD | 4,580.00 USD |
| `7D` | `0.1184` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD |
| `1D` | `0.1185` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 4,390.00 USD | 5,850.00 USD | 6,770.00 USD |
| `1D` | `0.1187` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 2,150.00 USD | 3,330.00 USD | 9,840.00 USD |
| `7D` | `0.1187` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 5,620.00 USD | 17,120.00 USD | 54,960.00 USD |
| `1D` | `0.1189` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 2,120.00 USD | 4,350.00 USD |
| `7D` | `0.1190` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD |
| `1D` | `0.1191` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 1,810.00 USD | 5,650.00 USD |
| `1D` | `0.1193` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 1,980.00 USD | 1,040.00 USD | 1,960.00 USD |
| `7D` | `0.1193` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD |
| `1D` | `0.1195` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 6,310.00 USD | 1,470.00 USD | 2,780.00 USD |
| `7D` | `0.1196` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD |
| `1D` | `0.1197` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 1,040.00 USD | 93.72 USD |
| `1D` | `0.1199` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 431.42 USD | 3,050.00 USD |
| `7D` | `0.1199` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 9,100.00 USD | 13,190.00 USD | 67,980.00 USD |
| `1D` | `0.1201` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 3,250.00 USD | 1,390.00 USD | 9,680.00 USD |
| `7D` | `0.1202` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 138,430.00 USD | 21,430.00 USD | 32,790.00 USD |
| `1D` | `0.1203` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 5,670.00 USD | 413.94 USD | 2,710.00 USD |
| `1D` | `0.1205` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 2,250.00 USD | 1,670.00 USD | 741.32 USD |
| `7D` | `0.1205` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 132,960.00 USD | 72,910.00 USD | 130,900.00 USD |
| `1D` | `0.1207` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 5,540.00 USD | 524.23 USD | 4,100.00 USD |
| `7D` | `0.1208` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 39,480.00 USD | 25,720.00 USD | 66,520.00 USD |
| `1D` | `0.1209` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 2,820.00 USD | 3,290.00 USD | 2,240.00 USD |
| `1D` | `0.1211` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 4,800.00 USD | 2,950.00 USD | 3,220.00 USD |
| `7D` | `0.1211` | 7,200,000.00 USD | 7,200,000.00 USD | 0.00 USD | 72,500.00 USD | 25,920.00 USD | 111,160.00 USD |
| `1D` | `0.1213` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 5,870.00 USD | 1,720.00 USD | 11,460.00 USD |
| `7D` | `0.1214` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD |
| `1D` | `0.1215` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD | 5,440.00 USD |
| `1D` | `0.1217` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 1,090.00 USD | 624.33 USD | 6,070.00 USD |
| `7D` | `0.1217` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD |
| `1D` | `0.1219` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 2,320.00 USD | 718.82 USD | 10,060.00 USD |
| `7D` | `0.1220` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 45,700.00 USD | 10,970.00 USD | 54,700.00 USD |
| `1D` | `0.1221` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 7,970.00 USD | 2,940.00 USD | 3,650.00 USD |
| `1D` | `0.1223` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 2,660.00 USD | 1,410.00 USD | 4,210.00 USD |
| `7D` | `0.1223` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 76,930.00 USD | 36,110.00 USD | 50,790.00 USD |
| `1D` | `0.1225` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 1,840.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1226` | 7,740,000.00 USD | 7,740,000.00 USD | 0.00 USD | 54,940.00 USD | 32,070.00 USD | 5,210.00 USD |
| `7D` | `0.1229` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 71,850.00 USD | 38,040.00 USD | 79,050.00 USD |
| `7D` | `0.1232` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 67,800.00 USD | 28,560.00 USD | 68,270.00 USD |
| `7D` | `0.1235` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 15,040.00 USD | 5,390.00 USD | 17,120.00 USD |
| `7D` | `0.1238` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 8,310.00 USD | 3,610.00 USD | 3,100.00 USD |
| `7D` | `0.1241` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 11,380.00 USD | 1,380.00 USD | 7,090.00 USD |
| `7D` | `0.1244` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 26,540.00 USD | 8,130.00 USD | 9,660.00 USD |
| `7D` | `0.1247` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 7,900.00 USD | 18,280.00 USD | 17,680.00 USD |
| `7D` | `0.1250` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 8,540.00 USD | 7,270.00 USD | 5,780.00 USD |
| `7D` | `0.1253` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | 16,470.00 USD |
| `7D` | `0.1256` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 11,990.00 USD | 11,420.00 USD | 220.44 USD |
| `7D` | `0.1259` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 5,870.00 USD | 1,190.00 USD | 151.34 USD |
| `7D` | `0.1262` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | 3,530.00 USD |
| `7D` | `0.1265` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 2,710.00 USD | 0.00 USD | 7,350.00 USD |
| `7D` | `0.1268` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD |
| `7D` | `0.1271` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 5,940.00 USD | 0.00 USD | 30.15 USD |
| `7D` | `0.1274` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12.00 USD |
| `7D` | `0.1277` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31.66 USD |
| `7D` | `0.1280` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,390.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `64.96M` | Total OI Tokens: `634,698,971.5 OP`
  * 1h OI Change: `+0.20%` | 4h OI Change: `-11.74%` | 24h OI Change: `-16.54%`
  * Exchange Breakdown: Binance=`14.81M` | Bybit=`13.12M` | OKX=`3.61M` | Hyperliquid=`3.32M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-2.62K` | Last 24h: `270.64` | Last 3d: `-2.23K` | Last 7d: `-15.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0224%` | **USDT OKX** | `-0.0014%` |
| **USDT Bybit** | `0.0055%` | **USDT KuCoin** | `0.0057%` |
| **USDT MEXC** | `-0.0224%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0021%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `43.97%` | `56.03%` | `0.78` | 3,770,000.00 USD |
| `15M` | `Binance` | `42.32%` | `57.68%` | `0.73` | 1,730,000.00 USD |
| `15M` | `OKX` | `47.2%` | `52.8%` | `0.89` | 409,050.00 USD |
| `15M` | `Bybit` | `47.6%` | `52.4%` | `0.91` | 401,800.00 USD |
| `15M` | `KuCoin` | `46.69%` | `53.31%` | `0.88` | 180,530.00 USD |
| `15M` | `Gate` | `57.5%` | `42.5%` | `1.35` | 112,620.00 USD |
| `15M` | `Bitget` | `35.93%` | `64.07%` | `0.56` | 209,700.00 USD |
| `15M` | `BingX` | `42.08%` | `57.92%` | `0.73` | 62,670.00 USD |
| `15M` | `MEXC` | `39.26%` | `60.74%` | `0.65` | 163,570.00 USD |
| `15M` | `Bitunix` | `43.45%` | `56.55%` | `0.77` | 74,110.00 USD |
| `15M` | `Hyperliquid` | `37.47%` | `62.53%` | `0.60` | 175,530.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.91%` | `49.09%` | `1.04` | 102,840.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `56.12%` | `43.88%` | `1.28` | 126,270.00 USD |
| `15M` | `HTX` | `20.06%` | `79.94%` | `0.25` | 77.98 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `5.79%` | `94.21%` | `0.06` | 7,640.00 USD |
| `15M` | `Aster` | `0.17%` | `99.83%` | `0.00` | 535.70 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `4.67%` | `95.33%` | `0.05` | 2,590.00 USD |
| `15M` | `Whale Positions` | `42.32%` | `57.68%` | `0.73` | 1,730,000.00 USD |
| `15M` | `Global Accounts` | `43.97%` | `56.03%` | `0.78` | 3,770,000.00 USD |
| `1H` | `OP` | `48.60%` | `51.40%` | `0.95` | 14,630,000.00 USD |
| `1H` | `Binance` | `48.39%` | `51.61%` | `0.94` | 6,820,000.00 USD |
| `1H` | `OKX` | `49.55%` | `50.45%` | `0.98` | 1,660,000.00 USD |
| `1H` | `Bybit` | `50.51%` | `49.49%` | `1.02` | 2,020,000.00 USD |
| `1H` | `KuCoin` | `50.53%` | `49.47%` | `1.02` | 675,420.00 USD |
| `1H` | `Gate` | `49.48%` | `50.52%` | `0.98` | 358,080.00 USD |
| `1H` | `Bitget` | `52.12%` | `47.88%` | `1.09` | 560,480.00 USD |
| `1H` | `BingX` | `39.87%` | `60.13%` | `0.66` | 558,820.00 USD |
| `1H` | `MEXC` | `43.9%` | `56.1%` | `0.78` | 479,480.00 USD |
| `1H` | `Bitunix` | `53%` | `47%` | `1.13` | 247,960.00 USD |
| `1H` | `Hyperliquid` | `40.96%` | `59.04%` | `0.69` | 382,140.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.32%` | `48.68%` | `1.05` | 328,440.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `53.48%` | `46.52%` | `1.15` | 451,450.00 USD |
| `1H` | `HTX` | `26.04%` | `73.96%` | `0.35` | 882.97 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `37.04%` | `62.96%` | `0.59` | 57,670.00 USD |
| `1H` | `Aster` | `36.27%` | `63.73%` | `0.57` | 22,030.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `18.68%` | `81.32%` | `0.23` | 24,880.00 USD |
| `1H` | `Whale Positions` | `48.39%` | `51.61%` | `0.94` | 6,820,000.00 USD |
| `1H` | `Global Accounts` | `48.60%` | `51.40%` | `0.95` | 14,630,000.00 USD |
| `4H` | `OP` | `47.11%` | `52.89%` | `0.89` | 54,770,000.00 USD |
| `4H` | `Binance` | `46.4%` | `53.6%` | `0.87` | 21,030,000.00 USD |
| `4H` | `OKX` | `46.59%` | `53.41%` | `0.87` | 6,720,000.00 USD |
| `4H` | `Bybit` | `45.93%` | `54.07%` | `0.85` | 8,710,000.00 USD |
| `4H` | `KuCoin` | `47.38%` | `52.62%` | `0.90` | 502,420.00 USD |
| `4H` | `Gate` | `54.5%` | `45.5%` | `1.20` | 592,870.00 USD |
| `4H` | `Bitget` | `49.47%` | `50.53%` | `0.98` | 3,590,000.00 USD |
| `4H` | `BingX` | `46.54%` | `53.46%` | `0.87` | 1,820,000.00 USD |
| `4H` | `MEXC` | `43.15%` | `56.85%` | `0.76` | 2,360,000.00 USD |
| `4H` | `Bitunix` | `45.77%` | `54.23%` | `0.84` | 664,520.00 USD |
| `4H` | `Hyperliquid` | `38.54%` | `61.46%` | `0.63` | 735,320.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.9%` | `52.1%` | `0.92` | 7,090,000.00 USD |
| `4H` | `Crypto.com` | `23.33%` | `76.67%` | `0.30` | 23,220.00 USD |
| `4H` | `WhiteBIT` | `87.91%` | `12.09%` | `7.27` | 681,910.00 USD |
| `4H` | `HTX` | `47.73%` | `52.27%` | `0.91` | 46,660.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `60.4%` | `39.6%` | `1.53` | 63,260.00 USD |
| `4H` | `Aster` | `33.2%` | `66.8%` | `0.50` | 54,580.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.39%` | `49.61%` | `1.02` | 76,490.00 USD |
| `4H` | `Whale Positions` | `46.4%` | `53.6%` | `0.87` | 21,030,000.00 USD |
| `4H` | `Global Accounts` | `47.11%` | `52.89%` | `0.89` | 54,770,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1102` | `0.1102` | `0.1102` | `0.1105` | `0.1099` | 215,356.47 USD | 112,661.20 USD | 102,695.27 USD | 9,965.93 USD | `+4.63%` | `7B / 11S` |
| `0:00 UTC` | `0.1077` | `0.1082` | `0.1077` | `0.1102` | `0.1070` | 2,425,114.31 USD | 1,046,280.57 USD | 1,378,833.74 USD | -332,553.17 USD | `-13.71%` | `8B / 30S` |
| `5:00 UTC` | `0.1084` | `0.1083` | `0.1084` | `0.1087` | `0.1080` | 527,563.25 USD | 310,298.99 USD | 217,264.26 USD | 93,034.72 USD | `+17.63%` | `19B / 3S` |
| `0:00 UTC` | `0.1063` | `0.1047` | `0.1063` | `0.1088` | `0.1013` | 5,548,996.22 USD | 2,272,459.88 USD | 3,276,536.35 USD | -1,004,076.47 USD | `-18.09%` | `5B / 37S` |
| `5:00 UTC` | `0.1014` | `0.1013` | `0.1014` | `0.1029` | `0.0990` | 5,717,098.88 USD | 2,672,854.06 USD | 3,044,244.81 USD | -371,390.75 USD | `-6.50%` | `7B / 23S` |
| `0:00 UTC` | `0.1025` | `0.1020` | `0.1025` | `0.1033` | `0.1007` | 1,857,629.60 USD | 946,076.57 USD | 911,553.03 USD | 34,523.54 USD | `+1.86%` | `19B / 6S` |
| `5:00 UTC` | `0.1043` | `0.1035` | `0.1043` | `0.1044` | `0.1026` | 1,285,007.52 USD | 601,525.80 USD | 683,481.72 USD | -81,955.93 USD | `-6.38%` | `27B / 29S` |
| `0:00 UTC` | `0.1037` | `0.1036` | `0.1037` | `0.1042` | `0.1024` | 770,717.58 USD | 335,049.96 USD | 435,667.63 USD | -100,617.67 USD | `-13.06%` | `27B / 45S` |
| `5:00 UTC` | `0.1020` | `0.1024` | `0.1020` | `0.1029` | `0.1018` | 520,168.37 USD | 289,498.79 USD | 230,669.58 USD | 58,829.21 USD | `+11.31%` | `26B / 7S` |
| `0:00 UTC` | `0.1016` | `0.1019` | `0.1016` | `0.1023` | `0.1016` | 113,031.85 USD | 62,025.06 USD | 51,006.79 USD | 11,018.27 USD | `+9.75%` | `24B / 10S` |

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
| `5m` | -620.00 USD | -22,140.00 USD | **`DISTRIBUTION`** |
| `15m` | 18,650.00 USD | 127,740.00 USD | **`ACCUMULATION`** |
| `30m` | 22,780.00 USD | 42,530.00 USD | **`ACCUMULATION`** |
| `1h` | 311,730.00 USD | 81,420.00 USD | **`ACCUMULATION`** |
| `2h` | -57,740.00 USD | -2,420,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -147,120.00 USD | -2,800,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -188,640.00 USD | -3,230,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -42,700.00 USD | -2,590,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 78,560.00 USD | -2,460,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -45,500.00 USD | -4,890,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -246,400.00 USD | -12,400,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,600,000.00 USD | -81,440,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-620.00` | 15m=`+18.65K` | 1h=`+311.73K` | 24h=`-45.50K`
* Futures Capital Netflows: 5m=`-22.14K` | 15m=`+127.74K` | 1h=`+81.42K` | 24h=`-4.89M`
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
  * `2026-10-30 03:29:54 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:54 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:31:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
