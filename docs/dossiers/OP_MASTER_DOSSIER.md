# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 03:16:11 IST` (`2026-10-29 21:46:11 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1032` | `0.1041` | `0.1032` | `0.1038` | `3,929,923` | 407,609.63 USD | -35,206.13 USD | `-8.64%` | -2,869,507.46 USD | `+0.27` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.1038` | `0.1042` | `0.1037` | `0.1038` | `1,678,371` | 174,466.92 USD | -8,511.79 USD | `-4.88%` | -2,878,019.24 USD | `+0.42` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.1038` | `0.1038` | `0.1025` | `0.1025` | `1,494,614` | 154,052.46 USD | -48,345.80 USD | `-31.38%` | -2,926,365.04 USD | `+0.13` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1012` | `0.1032` | `0.1007` | `0.1029` | `18,216,274` | 1,857,629.60 USD | 34,523.54 USD | `+1.86%` | -2,752,345.40 USD | `+0.53` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1029` | `0.1044` | `0.1026` | `0.1031` | `12,411,436` | 1,285,007.52 USD | -81,955.93 USD | `-6.38%` | -2,834,301.33 USD | `+0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1032` | `0.1042` | `0.1024` | `0.1024` | `7,119,668` | 737,846.16 USD | -91,212.49 USD | `-12.36%` | -2,925,513.82 USD | `+0.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1100` | `0.1106` | `0.1096` | `0.1101` | `7,910,873` | 870,770.93 USD | 117,397.34 USD | `+13.48%` | -1,177,554.63 USD | `+0.73` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `136,699,709` | 14,218,772.66 USD | -1,614,985.67 USD | `-11.36%` | -2,792,540.30 USD | `-3.57` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1012` | `0.1044` | `0.1007` | `0.1024` | `37,734,634` | 3,879,177.63 USD | -139,907.60 USD | `-3.61%` | -2,932,447.90 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -935,828.18 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | -1,111,968.46 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1025` | `174,415,996` | 18,096,070.08 USD | -1,753,013.06 USD | `-9.69%` | -2,864,981.52 USD | `-1.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1085` | `0.1106` | `0.1071` | `0.1076` | `47,048,931` | 5,111,570.05 USD | 108,567.99 USD | `+2.12%` | -1,419,806.61 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,277,083.78 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -935,828.18 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | -1,111,968.46 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1025` | `174,415,996` | 18,096,070.08 USD | -1,753,013.06 USD | `-9.69%` | -2,864,981.52 USD | `-1.52` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:15:37 IST` |

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
| `7D` | `Long Liquidation` | `0.0878` | 1,220,000.00 USD | 1,220,000.00 USD | 1,370.00 USD | 4,930.00 USD | 27,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0881` | 814,810.00 USD | 814,810.00 USD | 2,400.00 USD | 1,300.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0881` | 1,190,000.00 USD | 1,190,000.00 USD | 3,770.00 USD | 2,660.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0883` | 806,770.00 USD | 806,770.00 USD | 2,370.00 USD | 659.34 USD | 5,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0884` | 1,170,000.00 USD | 1,170,000.00 USD | 7,040.00 USD | 4,640.00 USD | 11,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0885` | 797,760.00 USD | 797,760.00 USD | 0.00 USD | 312.16 USD | 2,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0887` | 794,930.00 USD | 794,930.00 USD | 1,740.00 USD | 655.48 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0887` | 1,140,000.00 USD | 1,140,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0889` | 788,000.00 USD | 788,000.00 USD | 727.20 USD | 1,690.00 USD | 2,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0890` | 1,110,000.00 USD | 1,110,000.00 USD | 14,610.00 USD | 4,470.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0891` | 783,490.00 USD | 783,490.00 USD | 1,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0893` | 782,160.00 USD | 782,160.00 USD | 983.61 USD | 0.00 USD | 543.57 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0893` | 1,090,000.00 USD | 1,090,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0895` | 780,630.00 USD | 780,630.00 USD | 0.00 USD | 215.06 USD | 394.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,120.00 USD | 108,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0896` | 1,070,000.00 USD | 1,070,000.00 USD | 5,760.00 USD | 611.80 USD | 6,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0897` | 780,020.00 USD | 780,020.00 USD | 0.00 USD | 772.87 USD | 0.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0899` | 779,250.00 USD | 779,250.00 USD | 0.00 USD | 287.77 USD | 609.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0899` | 1,050,000.00 USD | 1,050,000.00 USD | 3,390.00 USD | 927.82 USD | 4,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0901` | 778,350.00 USD | 778,350.00 USD | 2,450.00 USD | 0.00 USD | 306.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0902` | 1,040,000.00 USD | 1,040,000.00 USD | 2,270.00 USD | 910.78 USD | 1,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0903` | 775,590.00 USD | 775,590.00 USD | 831.11 USD | 2,190.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0905` | 771,500.00 USD | 771,500.00 USD | 413.91 USD | 998.41 USD | 2,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0905` | 1,040,000.00 USD | 1,040,000.00 USD | 10,350.00 USD | 996.61 USD | 4,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0905` | 1,260.00 USD | 105,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0907` | 767,250.00 USD | 767,250.00 USD | 2,290.00 USD | 909.44 USD | 962.97 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0908` | 1,020,000.00 USD | 1,020,000.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0909` | 763,090.00 USD | 763,090.00 USD | 938.76 USD | 499.80 USD | 778.75 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0911` | 760,870.00 USD | 760,870.00 USD | 5,580.00 USD | 778.50 USD | 4.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0911` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0913` | 754,510.00 USD | 754,510.00 USD | 0.00 USD | 0.00 USD | 782.37 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0914` | 1,010,000.00 USD | 1,010,000.00 USD | 1,670.00 USD | 903.90 USD | 45.81 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0915` | 753,730.00 USD | 753,730.00 USD | 6,590.00 USD | 0.00 USD | 49.30 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0917` | 747,090.00 USD | 747,090.00 USD | 2,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0917` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0919` | 744,540.00 USD | 744,540.00 USD | 3,690.00 USD | 0.00 USD | 42.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0923` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0925` | 740,810.00 USD | 740,810.00 USD | 3,270.00 USD | 1,660.00 USD | 6,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0926` | 1,000,000.00 USD | 1,000,000.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0931` | 729,520.00 USD | 729,520.00 USD | 0.00 USD | 0.00 USD | 64.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0932` | 994,200.00 USD | 994,200.00 USD | 0.00 USD | 0.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0933` | 729,460.00 USD | 729,460.00 USD | 0.00 USD | 0.00 USD | 6,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0935` | 981,970.00 USD | 981,970.00 USD | 0.00 USD | 1,320.00 USD | 6,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0938` | 974,160.00 USD | 974,160.00 USD | 0.00 USD | 0.00 USD | 8.57 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0941` | 974,150.00 USD | 974,150.00 USD | 2,050.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0944` | 969,080.00 USD | 969,080.00 USD | 1,870.00 USD | 0.00 USD | 7,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0945` | 69,120.00 USD | 104,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0947` | 722,590.00 USD | 722,590.00 USD | 0.00 USD | 0.00 USD | 69.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0947` | 959,690.00 USD | 959,690.00 USD | 3,790.00 USD | 1,810.00 USD | 112.06 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0949` | 722,520.00 USD | 722,520.00 USD | 0.00 USD | 0.00 USD | 76.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0950` | 953,970.00 USD | 953,970.00 USD | 3,770.00 USD | 0.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0953` | 722,450.00 USD | 722,450.00 USD | 0.00 USD | 0.00 USD | 152.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0953` | 943,540.00 USD | 943,540.00 USD | 0.00 USD | 0.00 USD | 4.65 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0955` | 722,290.00 USD | 722,290.00 USD | 0.00 USD | 1,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0955` | 2,040.00 USD | 35,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0959` | 943,530.00 USD | 943,530.00 USD | 0.00 USD | 1,140.00 USD | 115.48 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0961` | 721,110.00 USD | 721,110.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0962` | 942,280.00 USD | 942,280.00 USD | 0.00 USD | 0.00 USD | 121.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0965` | 719,030.00 USD | 719,030.00 USD | 1,280.00 USD | 282.32 USD | 1,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0965` | 1,160.00 USD | 33,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0967` | 715,510.00 USD | 715,510.00 USD | 2,660.00 USD | 1,100.00 USD | 7,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0968` | 942,160.00 USD | 942,160.00 USD | 7,490.00 USD | 3,720.00 USD | 11,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0969` | 704,130.00 USD | 704,130.00 USD | 4,590.00 USD | 2,640.00 USD | 9,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0971` | 687,700.00 USD | 687,700.00 USD | 16,100.00 USD | 3,330.00 USD | 4,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 919,320.00 USD | 919,320.00 USD | 0.00 USD | 3,760.00 USD | 9,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0973` | 663,850.00 USD | 663,850.00 USD | 0.00 USD | 2,120.00 USD | 4,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0974` | 905,840.00 USD | 905,840.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0975` | 657,430.00 USD | 657,430.00 USD | 0.00 USD | 1,810.00 USD | 5,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0975` | 11,950.00 USD | 32,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0977` | 650,000.00 USD | 650,000.00 USD | 24,760.00 USD | 2,510.00 USD | 11,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0977` | 901,560.00 USD | 901,560.00 USD | 0.00 USD | 1,160.00 USD | 13,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0979` | 611,540.00 USD | 611,540.00 USD | 12,620.00 USD | 1,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0980` | 887,270.00 USD | 887,270.00 USD | 0.00 USD | 3,920.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0981` | 597,880.00 USD | 597,880.00 USD | 9,220.00 USD | 431.42 USD | 3,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0983` | 585,200.00 USD | 585,200.00 USD | 3,250.00 USD | 1,390.00 USD | 16,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 877,650.00 USD | 877,650.00 USD | 7,990.00 USD | 1,230.00 USD | 14,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0985` | 564,330.00 USD | 564,330.00 USD | 5,670.00 USD | 413.94 USD | 2,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0985` | 20,130.00 USD | 20,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0986` | 853,650.00 USD | 853,650.00 USD | 7,110.00 USD | 7,530.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0987` | 555,570.00 USD | 555,570.00 USD | 15,960.00 USD | 6,330.00 USD | 20,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0989` | 512,550.00 USD | 512,550.00 USD | 2,820.00 USD | 3,290.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 800,740.00 USD | 800,740.00 USD | 17,640.00 USD | 6,190.00 USD | 53,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0991` | 504,270.00 USD | 504,270.00 USD | 32,710.00 USD | 2,950.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0992` | 723,700.00 USD | 723,700.00 USD | 27,140.00 USD | 11,490.00 USD | 28,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0993` | 465,400.00 USD | 465,400.00 USD | 3,080.00 USD | 1,720.00 USD | 11,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0995` | 449,120.00 USD | 449,120.00 USD | 2,740.00 USD | 624.33 USD | 11,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 656,580.00 USD | 656,580.00 USD | 24,220.00 USD | 15,150.00 USD | 56,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0997` | 434,280.00 USD | 434,280.00 USD | 35,260.00 USD | 718.82 USD | 27,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0998` | 560,660.00 USD | 560,660.00 USD | 28,450.00 USD | 6,400.00 USD | 49,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0999` | 371,100.00 USD | 371,100.00 USD | 37,910.00 USD | 2,940.00 USD | 23,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1001` | 306,410.00 USD | 306,410.00 USD | 21,100.00 USD | 1,410.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 476,440.00 USD | 476,440.00 USD | 36,110.00 USD | 8,650.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1003` | 279,690.00 USD | 279,690.00 USD | 0.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1004` | 418,560.00 USD | 418,560.00 USD | 22,470.00 USD | 16,470.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1005` | 279,130.00 USD | 279,130.00 USD | 1,970.00 USD | 403.62 USD | 13,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1007` | 262,770.00 USD | 262,770.00 USD | 0.00 USD | 8,710.00 USD | 32,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 356,190.00 USD | 356,190.00 USD | 20,870.00 USD | 3,870.00 USD | 54,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1009` | 221,400.00 USD | 221,400.00 USD | 0.00 USD | 2,750.00 USD | 18.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1010` | 276,690.00 USD | 276,690.00 USD | 17,340.00 USD | 6,580.00 USD | 6,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1011` | 218,630.00 USD | 218,630.00 USD | 0.00 USD | 575.54 USD | 3,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1013` | 214,530.00 USD | 214,530.00 USD | 0.00 USD | 800.79 USD | 613.37 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 246,140.00 USD | 246,140.00 USD | 15,270.00 USD | 5,230.00 USD | 56,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1015` | 213,110.00 USD | 213,110.00 USD | 0.00 USD | 1,830.00 USD | 1,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1016` | 169,160.00 USD | 169,160.00 USD | 15,440.00 USD | 5,490.00 USD | 5,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1017` | 209,620.00 USD | 209,620.00 USD | 0.00 USD | 3,440.00 USD | 34,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1019` | 171,860.00 USD | 171,860.00 USD | 0.00 USD | 6,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1019` | 142,710.00 USD | 142,710.00 USD | 12,100.00 USD | 5,790.00 USD | 14,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1021` | 165,480.00 USD | 165,480.00 USD | 15,980.00 USD | 1,320.00 USD | 14,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1022` | 110,560.00 USD | 110,560.00 USD | 11,930.00 USD | 8,250.00 USD | 12,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1025` | 134,000.00 USD | 134,000.00 USD | 0.00 USD | 0.00 USD | 121.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1025` | 77,720.00 USD | 77,720.00 USD | 1,550.00 USD | 0.00 USD | 8,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1027` | 133,880.00 USD | 133,880.00 USD | 0.00 USD | 0.00 USD | 19.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1028` | 67,680.00 USD | 67,680.00 USD | 3,800.00 USD | 4,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1029` | 133,860.00 USD | 133,860.00 USD | 0.00 USD | 0.00 USD | 6,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1031` | 127,440.00 USD | 127,440.00 USD | 27,910.00 USD | 0.00 USD | 18,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1031` | 59,490.00 USD | 59,490.00 USD | 19,560.00 USD | 6,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1033` | 80,770.00 USD | 80,770.00 USD | 0.00 USD | 0.00 USD | 21,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1034` | 33,670.00 USD | 33,670.00 USD | 18,920.00 USD | 7,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1035` | 58,930.00 USD | 58,930.00 USD | 4,780.00 USD | 4,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1037` | 49,270.00 USD | 49,270.00 USD | 37,310.00 USD | 11,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1037` | 7,720.00 USD | 7,720.00 USD | 2,710.00 USD | 5,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1039` | 5,450.00 USD | 5,450.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1039` | 10,890.00 USD | 10,890.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1040` | 16,240.00 USD | 16,240.00 USD | 5,940.00 USD | 10,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1041` | 23,720.00 USD | 23,720.00 USD | 0.00 USD | 12,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1043` | 29,370.00 USD | 29,370.00 USD | 0.00 USD | 5,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1043` | 38,190.00 USD | 38,190.00 USD | 15,960.00 USD | 5,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1045` | 39,150.00 USD | 39,150.00 USD | 0.00 USD | 4,840.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1046` | 62,680.00 USD | 62,680.00 USD | 0.00 USD | 9,810.00 USD | 14,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1047` | 78,120.00 USD | 78,120.00 USD | 15,000.00 USD | 3,400.00 USD | 20,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1049` | 168,850.00 USD | 168,850.00 USD | 37,390.00 USD | 10,710.00 USD | 42,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1049` | 187,100.00 USD | 187,100.00 USD | 34,790.00 USD | 6,530.00 USD | 83,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1051` | 232,200.00 USD | 232,200.00 USD | 30,370.00 USD | 8,750.00 USD | 24,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1052` | 364,870.00 USD | 364,870.00 USD | 28,200.00 USD | 24,160.00 USD | 125,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1053` | 327,050.00 USD | 327,050.00 USD | 35,030.00 USD | 8,930.00 USD | 50,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1055` | 455,720.00 USD | 455,720.00 USD | 43,960.00 USD | 25,140.00 USD | 59,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1055` | 743,600.00 USD | 743,600.00 USD | 122,840.00 USD | 44,430.00 USD | 211,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1057` | 548,240.00 USD | 548,240.00 USD | 27,300.00 USD | 15,170.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1058` | 1,090,000.00 USD | 1,090,000.00 USD | 105,620.00 USD | 53,680.00 USD | 189,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1059` | 684,200.00 USD | 684,200.00 USD | 39,020.00 USD | 0.00 USD | 96,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1061` | 770,160.00 USD | 770,160.00 USD | 26,970.00 USD | 0.00 USD | 59,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1061` | 1,340,000.00 USD | 1,340,000.00 USD | 75,540.00 USD | 72,260.00 USD | 102,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1063` | 858,310.00 USD | 858,310.00 USD | 25,200.00 USD | 0.00 USD | 62,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1064` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 52,580.00 USD | 192,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1065` | 884,200.00 USD | 884,200.00 USD | 0.00 USD | 0.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1067` | 917,400.00 USD | 917,400.00 USD | 0.00 USD | 0.00 USD | 33,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1067` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 51,740.00 USD | 133,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1069` | 988,400.00 USD | 988,400.00 USD | 8,170.00 USD | 4,140.00 USD | 58,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1070` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 57,770.00 USD | 134,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1071` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 3,140.00 USD | 16,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1073` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 57.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1073` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 17,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1076` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 22,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1079` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1079` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 79.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1082` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 89.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1083` | 1,050,000.00 USD | 1,050,000.00 USD | 7,990.00 USD | 5,910.00 USD | 7,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1085` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 65,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1085` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1087` | 1,190,000.00 USD | 1,190,000.00 USD | 28,490.00 USD | 2,240.00 USD | 44,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1088` | 2,010,000.00 USD | 2,010,000.00 USD | 5,290.00 USD | 0.00 USD | 113.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1089` | 1,230,000.00 USD | 1,230,000.00 USD | 39,160.00 USD | 0.00 USD | 152.23 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1091` | 1,260,000.00 USD | 1,260,000.00 USD | 33,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1091` | 2,040,000.00 USD | 2,040,000.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1093` | 1,280,000.00 USD | 1,280,000.00 USD | 15,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1094` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1095` | 1,300,000.00 USD | 1,300,000.00 USD | 4,110.00 USD | 1,890.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1097` | 1,330,000.00 USD | 1,330,000.00 USD | 7,260.00 USD | 1,970.00 USD | 22,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1097` | 2,060,000.00 USD | 2,060,000.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1099` | 1,340,000.00 USD | 1,340,000.00 USD | 6,130.00 USD | 1,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1100` | 2,100,000.00 USD | 2,100,000.00 USD | 11,470.00 USD | 0.00 USD | 21,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1101` | 1,350,000.00 USD | 1,350,000.00 USD | 4,310.00 USD | 2,820.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1103` | 1,360,000.00 USD | 1,360,000.00 USD | 3,540.00 USD | 5,640.00 USD | 96.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 2,140,000.00 USD | 2,140,000.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1105` | 1,380,000.00 USD | 1,380,000.00 USD | 3,380.00 USD | 4,740.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1106` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 22,880.00 USD | 16,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1107` | 1,430,000.00 USD | 1,430,000.00 USD | 3,110.00 USD | 12,720.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1109` | 1,440,000.00 USD | 1,440,000.00 USD | 2,110.00 USD | 1,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1111` | 1,440,000.00 USD | 1,440,000.00 USD | 5,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1112` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1113` | 1,510,000.00 USD | 1,510,000.00 USD | 21,390.00 USD | 5,210.00 USD | 39,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1115` | 1,510,000.00 USD | 1,510,000.00 USD | 4,760.00 USD | 0.00 USD | 8.95 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1117` | 1,580,000.00 USD | 1,580,000.00 USD | 2,060.00 USD | 25,630.00 USD | 34,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1118` | 2,280,000.00 USD | 2,280,000.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1119` | 1,650,000.00 USD | 1,650,000.00 USD | 33,110.00 USD | 6,980.00 USD | 36,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1121` | 1,700,000.00 USD | 1,700,000.00 USD | 20,000.00 USD | 12,060.00 USD | 12,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 2,330,000.00 USD | 2,330,000.00 USD | 17,760.00 USD | 0.00 USD | 32,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1123` | 1,740,000.00 USD | 1,740,000.00 USD | 40,400.00 USD | 1,780.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1124` | 2,440,000.00 USD | 2,440,000.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1125` | 1,780,000.00 USD | 1,780,000.00 USD | 11,130.00 USD | 13,240.00 USD | 7,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1127` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 1,250.00 USD | 19,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1127` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1129` | 1,810,000.00 USD | 1,810,000.00 USD | 8,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1130` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 15,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1131` | 1,850,000.00 USD | 1,850,000.00 USD | 20,830.00 USD | 8,010.00 USD | 17,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1133` | 1,910,000.00 USD | 1,910,000.00 USD | 6,530.00 USD | 22,520.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 2,500,000.00 USD | 2,500,000.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1135` | 1,920,000.00 USD | 1,920,000.00 USD | 4,040.00 USD | 3,670.00 USD | 4,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1135` | 557.61 USD | 557.61 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1136` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1137` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 856.93 USD | 244.57 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1139` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 14,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1139` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1141` | 1,970,000.00 USD | 1,970,000.00 USD | 13,860.00 USD | 2,800.00 USD | 20,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1142` | 2,540,000.00 USD | 2,540,000.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1143` | 2,030,000.00 USD | 2,030,000.00 USD | 20,300.00 USD | 27,990.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1145` | 2,090,000.00 USD | 2,090,000.00 USD | 13,430.00 USD | 11,690.00 USD | 38,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 2,780,000.00 USD | 2,780,000.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1147` | 2,140,000.00 USD | 2,140,000.00 USD | 10,640.00 USD | 10,080.00 USD | 30,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1148` | 2,970,000.00 USD | 2,970,000.00 USD | 9,880.00 USD | 0.00 USD | 176,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1149` | 2,210,000.00 USD | 2,210,000.00 USD | 35,170.00 USD | 624.71 USD | 31,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1151` | 2,280,000.00 USD | 2,280,000.00 USD | 16,450.00 USD | 14,620.00 USD | 33,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 3,240,000.00 USD | 3,240,000.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1153` | 2,390,000.00 USD | 2,390,000.00 USD | 31,350.00 USD | 23,630.00 USD | 59,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1154` | 3,710,000.00 USD | 3,710,000.00 USD | 243,190.00 USD | 26,970.00 USD | 195,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1155` | 2,510,000.00 USD | 2,510,000.00 USD | 38,430.00 USD | 27,080.00 USD | 54,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1157` | 2,560,000.00 USD | 2,560,000.00 USD | 33,550.00 USD | 8,310.00 USD | 7,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 4,020,000.00 USD | 4,020,000.00 USD | 188,950.00 USD | 25,290.00 USD | 98,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1159` | 2,600,000.00 USD | 2,600,000.00 USD | 19,470.00 USD | 7,420.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1160` | 4,300,000.00 USD | 4,300,000.00 USD | 139,350.00 USD | 32,830.00 USD | 109,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1161` | 2,630,000.00 USD | 2,630,000.00 USD | 23,670.00 USD | 0.00 USD | 5,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1163` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 9,380.00 USD | 17,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 4,580,000.00 USD | 4,580,000.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1165` | 2,670,000.00 USD | 2,670,000.00 USD | 4,990.00 USD | 5,320.00 USD | 1,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1166` | 4,800,000.00 USD | 4,800,000.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1167` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 7,220.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1169` | 2,700,000.00 USD | 2,700,000.00 USD | 5,480.00 USD | 2,440.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 5,020,000.00 USD | 5,020,000.00 USD | 82,770.00 USD | 26,150.00 USD | 112,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1171` | 2,710,000.00 USD | 2,710,000.00 USD | 13,800.00 USD | 0.00 USD | 4,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1172` | 5,150,000.00 USD | 5,150,000.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1173` | 2,730,000.00 USD | 2,730,000.00 USD | 2,840.00 USD | 5,440.00 USD | 4,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1175` | 2,770,000.00 USD | 2,770,000.00 USD | 9,530.00 USD | 9,020.00 USD | 19,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 5,320,000.00 USD | 5,320,000.00 USD | 72,770.00 USD | 17,930.00 USD | 81,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1177` | 2,810,000.00 USD | 2,810,000.00 USD | 14,360.00 USD | 8,560.00 USD | 16,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1178` | 5,490,000.00 USD | 5,490,000.00 USD | 89,510.00 USD | 23,660.00 USD | 55,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1179` | 2,830,000.00 USD | 2,830,000.00 USD | 10,640.00 USD | 3,990.00 USD | 5,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1181` | 2,860,000.00 USD | 2,860,000.00 USD | 12,400.00 USD | 4,120.00 USD | 15,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 5,580,000.00 USD | 5,580,000.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1183` | 2,870,000.00 USD | 2,870,000.00 USD | 8,760.00 USD | 677.63 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1184` | 5,640,000.00 USD | 5,640,000.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1185` | 2,890,000.00 USD | 2,890,000.00 USD | 4,390.00 USD | 5,850.00 USD | 6,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1187` | 2,900,000.00 USD | 2,900,000.00 USD | 2,150.00 USD | 3,330.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 5,720,000.00 USD | 5,720,000.00 USD | 5,620.00 USD | 17,120.00 USD | 54,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1189` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 2,120.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1190` | 5,870,000.00 USD | 5,870,000.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1191` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 1,810.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1193` | 2,930,000.00 USD | 2,930,000.00 USD | 4,720.00 USD | 1,040.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 5,950,000.00 USD | 5,950,000.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1195` | 2,940,000.00 USD | 2,940,000.00 USD | 6,310.00 USD | 1,470.00 USD | 2,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1196` | 6,010,000.00 USD | 6,010,000.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1197` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 1,040.00 USD | 129.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1199` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 431.42 USD | 3,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 6,100,000.00 USD | 6,100,000.00 USD | 9,100.00 USD | 13,190.00 USD | 67,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1201` | 2,960,000.00 USD | 2,960,000.00 USD | 3,250.00 USD | 1,390.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1202` | 6,290,000.00 USD | 6,290,000.00 USD | 138,430.00 USD | 21,430.00 USD | 32,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1203` | 2,960,000.00 USD | 2,960,000.00 USD | 5,670.00 USD | 413.94 USD | 2,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1205` | 2,970,000.00 USD | 2,970,000.00 USD | 2,250.00 USD | 1,670.00 USD | 770.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 6,630,000.00 USD | 6,630,000.00 USD | 132,960.00 USD | 72,910.00 USD | 130,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1207` | 2,980,000.00 USD | 2,980,000.00 USD | 5,540.00 USD | 524.23 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1208` | 6,760,000.00 USD | 6,760,000.00 USD | 39,480.00 USD | 25,720.00 USD | 66,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1209` | 2,990,000.00 USD | 2,990,000.00 USD | 2,820.00 USD | 3,290.00 USD | 2,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1211` | 3,000,000.00 USD | 3,000,000.00 USD | 4,800.00 USD | 2,950.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 6,970,000.00 USD | 6,970,000.00 USD | 72,500.00 USD | 25,920.00 USD | 111,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1213` | 3,020,000.00 USD | 3,020,000.00 USD | 5,870.00 USD | 1,720.00 USD | 11,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1214` | 7,090,000.00 USD | 7,090,000.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1215` | 3,020,000.00 USD | 3,020,000.00 USD | 1,650.00 USD | 0.00 USD | 5,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1217` | 3,030,000.00 USD | 3,030,000.00 USD | 1,090.00 USD | 624.33 USD | 6,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 7,140,000.00 USD | 7,140,000.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1219` | 3,050,000.00 USD | 3,050,000.00 USD | 2,320.00 USD | 718.82 USD | 10,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1220` | 7,250,000.00 USD | 7,250,000.00 USD | 45,700.00 USD | 10,970.00 USD | 54,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1221` | 3,060,000.00 USD | 3,060,000.00 USD | 7,970.00 USD | 2,940.00 USD | 3,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1223` | 3,070,000.00 USD | 3,070,000.00 USD | 2,660.00 USD | 1,410.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 7,410,000.00 USD | 7,410,000.00 USD | 76,930.00 USD | 36,110.00 USD | 50,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1225` | 3,070,000.00 USD | 3,070,000.00 USD | 1,840.00 USD | 558.39 USD | 21.44 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 721.08 USD | 1,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1226` | 7,500,000.00 USD | 7,500,000.00 USD | 54,940.00 USD | 32,070.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1227` | 3,070,000.00 USD | 3,070,000.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1229` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 7,700,000.00 USD | 7,700,000.00 USD | 81,840.00 USD | 38,040.00 USD | 79,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1232` | 7,870,000.00 USD | 7,870,000.00 USD | 67,800.00 USD | 33,050.00 USD | 63,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1235` | 7,910,000.00 USD | 7,910,000.00 USD | 15,040.00 USD | 5,390.00 USD | 17,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1235` | 9,170.00 USD | 10,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1238` | 7,920,000.00 USD | 7,920,000.00 USD | 8,310.00 USD | 3,610.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1241` | 7,940,000.00 USD | 7,940,000.00 USD | 11,380.00 USD | 1,380.00 USD | 7,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1244` | 7,990,000.00 USD | 7,990,000.00 USD | 26,540.00 USD | 8,130.00 USD | 9,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1247` | 8,030,000.00 USD | 8,030,000.00 USD | 7,900.00 USD | 18,280.00 USD | 17,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1250` | 8,050,000.00 USD | 8,050,000.00 USD | 8,540.00 USD | 7,270.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1253` | 8,070,000.00 USD | 8,070,000.00 USD | 6,550.00 USD | 0.00 USD | 16,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1256` | 8,100,000.00 USD | 8,100,000.00 USD | 11,990.00 USD | 13,660.00 USD | 220.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1259` | 8,110,000.00 USD | 8,110,000.00 USD | 5,870.00 USD | 1,190.00 USD | 151.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1262` | 8,110,000.00 USD | 8,110,000.00 USD | 4,270.00 USD | 0.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1265` | 8,120,000.00 USD | 8,120,000.00 USD | 2,710.00 USD | 0.00 USD | 7,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1268` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1271` | 8,130,000.00 USD | 8,130,000.00 USD | 5,940.00 USD | 0.00 USD | 30.15 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1274` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 12.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1277` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 31.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1280` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 0.00 USD | 6,390.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.0878` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 1,370.00 USD | 4,930.00 USD | 27,260.00 USD |
| `1D` | `0.0881` | 814,810.00 USD | 0.00 USD | 814,810.00 USD | 2,400.00 USD | 1,300.00 USD | 4,340.00 USD |
| `7D` | `0.0881` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 3,770.00 USD | 2,660.00 USD | 12,940.00 USD |
| `1D` | `0.0883` | 806,770.00 USD | 0.00 USD | 806,770.00 USD | 2,370.00 USD | 659.34 USD | 5,980.00 USD |
| `7D` | `0.0884` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 7,040.00 USD | 4,640.00 USD | 11,870.00 USD |
| `1D` | `0.0885` | 797,760.00 USD | 0.00 USD | 797,760.00 USD | 0.00 USD | 312.16 USD | 2,510.00 USD |
| `1D` | `0.0887` | 794,930.00 USD | 0.00 USD | 794,930.00 USD | 1,740.00 USD | 655.48 USD | 4,540.00 USD |
| `7D` | `0.0887` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD |
| `1D` | `0.0889` | 788,000.00 USD | 0.00 USD | 788,000.00 USD | 727.20 USD | 1,690.00 USD | 2,100.00 USD |
| `7D` | `0.0890` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 14,610.00 USD | 4,470.00 USD | 3,680.00 USD |
| `1D` | `0.0891` | 783,490.00 USD | 0.00 USD | 783,490.00 USD | 1,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0893` | 782,160.00 USD | 0.00 USD | 782,160.00 USD | 983.61 USD | 0.00 USD | 543.57 USD |
| `7D` | `0.0893` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD |
| `1D` | `0.0895` | 780,630.00 USD | 0.00 USD | 780,630.00 USD | 0.00 USD | 215.06 USD | 394.61 USD |
| `7D` | `0.0896` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 5,760.00 USD | 611.80 USD | 6,870.00 USD |
| `1D` | `0.0897` | 780,020.00 USD | 0.00 USD | 780,020.00 USD | 0.00 USD | 772.87 USD | 0.02 USD |
| `1D` | `0.0899` | 779,250.00 USD | 0.00 USD | 779,250.00 USD | 0.00 USD | 287.77 USD | 609.04 USD |
| `7D` | `0.0899` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 3,390.00 USD | 927.82 USD | 4,490.00 USD |
| `1D` | `0.0901` | 778,350.00 USD | 0.00 USD | 778,350.00 USD | 2,450.00 USD | 0.00 USD | 306.52 USD |
| `7D` | `0.0902` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 2,270.00 USD | 910.78 USD | 1,210.00 USD |
| `1D` | `0.0903` | 775,590.00 USD | 0.00 USD | 775,590.00 USD | 831.11 USD | 2,190.00 USD | 1,070.00 USD |
| `1D` | `0.0905` | 771,500.00 USD | 0.00 USD | 771,500.00 USD | 413.91 USD | 998.41 USD | 2,840.00 USD |
| `7D` | `0.0905` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 10,350.00 USD | 996.61 USD | 4,080.00 USD |
| `1D` | `0.0907` | 767,250.00 USD | 0.00 USD | 767,250.00 USD | 2,290.00 USD | 909.44 USD | 962.97 USD |
| `7D` | `0.0908` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD |
| `1D` | `0.0909` | 763,090.00 USD | 0.00 USD | 763,090.00 USD | 938.76 USD | 499.80 USD | 778.75 USD |
| `1D` | `0.0911` | 760,870.00 USD | 0.00 USD | 760,870.00 USD | 5,580.00 USD | 778.50 USD | 4.88 USD |
| `7D` | `0.0911` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD |
| `1D` | `0.0913` | 754,510.00 USD | 0.00 USD | 754,510.00 USD | 0.00 USD | 0.00 USD | 782.37 USD |
| `7D` | `0.0914` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 1,670.00 USD | 903.90 USD | 45.81 USD |
| `1D` | `0.0915` | 753,730.00 USD | 0.00 USD | 753,730.00 USD | 6,590.00 USD | 0.00 USD | 49.30 USD |
| `1D` | `0.0917` | 747,090.00 USD | 0.00 USD | 747,090.00 USD | 2,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0917` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 1,740.00 USD |
| `1D` | `0.0919` | 744,540.00 USD | 0.00 USD | 744,540.00 USD | 3,690.00 USD | 0.00 USD | 42.87 USD |
| `7D` | `0.0923` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `0.0925` | 740,810.00 USD | 0.00 USD | 740,810.00 USD | 3,270.00 USD | 1,660.00 USD | 6,360.00 USD |
| `7D` | `0.0926` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD |
| `1D` | `0.0931` | 729,520.00 USD | 0.00 USD | 729,520.00 USD | 0.00 USD | 0.00 USD | 64.09 USD |
| `7D` | `0.0932` | 994,200.00 USD | 0.00 USD | 994,200.00 USD | 0.00 USD | 0.00 USD | 12,240.00 USD |
| `1D` | `0.0933` | 729,460.00 USD | 0.00 USD | 729,460.00 USD | 0.00 USD | 0.00 USD | 6,860.00 USD |
| `7D` | `0.0935` | 981,970.00 USD | 0.00 USD | 981,970.00 USD | 0.00 USD | 1,320.00 USD | 6,490.00 USD |
| `7D` | `0.0938` | 974,160.00 USD | 0.00 USD | 974,160.00 USD | 0.00 USD | 0.00 USD | 8.57 USD |
| `7D` | `0.0941` | 974,150.00 USD | 0.00 USD | 974,150.00 USD | 2,050.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `0.0944` | 969,080.00 USD | 0.00 USD | 969,080.00 USD | 1,870.00 USD | 0.00 USD | 7,520.00 USD |
| `1D` | `0.0947` | 722,590.00 USD | 0.00 USD | 722,590.00 USD | 0.00 USD | 0.00 USD | 69.61 USD |
| `7D` | `0.0947` | 959,690.00 USD | 0.00 USD | 959,690.00 USD | 3,790.00 USD | 1,810.00 USD | 112.06 USD |
| `1D` | `0.0949` | 722,520.00 USD | 0.00 USD | 722,520.00 USD | 0.00 USD | 0.00 USD | 76.92 USD |
| `7D` | `0.0950` | 953,970.00 USD | 0.00 USD | 953,970.00 USD | 3,770.00 USD | 0.00 USD | 6,660.00 USD |
| `1D` | `0.0953` | 722,450.00 USD | 0.00 USD | 722,450.00 USD | 0.00 USD | 0.00 USD | 152.23 USD |
| `7D` | `0.0953` | 943,540.00 USD | 0.00 USD | 943,540.00 USD | 0.00 USD | 0.00 USD | 4.65 USD |
| `1D` | `0.0955` | 722,290.00 USD | 0.00 USD | 722,290.00 USD | 0.00 USD | 1,180.00 USD | 0.00 USD |
| `7D` | `0.0959` | 943,530.00 USD | 0.00 USD | 943,530.00 USD | 0.00 USD | 1,140.00 USD | 115.48 USD |
| `1D` | `0.0961` | 721,110.00 USD | 0.00 USD | 721,110.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0962` | 942,280.00 USD | 0.00 USD | 942,280.00 USD | 0.00 USD | 0.00 USD | 121.64 USD |
| `1D` | `0.0965` | 719,030.00 USD | 0.00 USD | 719,030.00 USD | 1,280.00 USD | 282.32 USD | 1,960.00 USD |
| `1D` | `0.0967` | 715,510.00 USD | 0.00 USD | 715,510.00 USD | 2,660.00 USD | 1,100.00 USD | 7,610.00 USD |
| `7D` | `0.0968` | 942,160.00 USD | 0.00 USD | 942,160.00 USD | 7,490.00 USD | 3,720.00 USD | 11,630.00 USD |
| `1D` | `0.0969` | 704,130.00 USD | 0.00 USD | 704,130.00 USD | 4,590.00 USD | 2,640.00 USD | 9,200.00 USD |
| `1D` | `0.0971` | 687,700.00 USD | 0.00 USD | 687,700.00 USD | 16,100.00 USD | 3,330.00 USD | 4,420.00 USD |
| `7D` | `0.0971` | 919,320.00 USD | 0.00 USD | 919,320.00 USD | 0.00 USD | 3,760.00 USD | 9,720.00 USD |
| `1D` | `0.0973` | 663,850.00 USD | 0.00 USD | 663,850.00 USD | 0.00 USD | 2,120.00 USD | 4,300.00 USD |
| `7D` | `0.0974` | 905,840.00 USD | 0.00 USD | 905,840.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD |
| `1D` | `0.0975` | 657,430.00 USD | 0.00 USD | 657,430.00 USD | 0.00 USD | 1,810.00 USD | 5,610.00 USD |
| `1D` | `0.0977` | 650,000.00 USD | 0.00 USD | 650,000.00 USD | 24,760.00 USD | 2,510.00 USD | 11,200.00 USD |
| `7D` | `0.0977` | 901,560.00 USD | 0.00 USD | 901,560.00 USD | 0.00 USD | 1,160.00 USD | 13,130.00 USD |
| `1D` | `0.0979` | 611,540.00 USD | 0.00 USD | 611,540.00 USD | 12,620.00 USD | 1,040.00 USD | 0.00 USD |
| `7D` | `0.0980` | 887,270.00 USD | 0.00 USD | 887,270.00 USD | 0.00 USD | 3,920.00 USD | 5,710.00 USD |
| `1D` | `0.0981` | 597,880.00 USD | 0.00 USD | 597,880.00 USD | 9,220.00 USD | 431.42 USD | 3,020.00 USD |
| `1D` | `0.0983` | 585,200.00 USD | 0.00 USD | 585,200.00 USD | 3,250.00 USD | 1,390.00 USD | 16,230.00 USD |
| `7D` | `0.0983` | 877,650.00 USD | 0.00 USD | 877,650.00 USD | 7,990.00 USD | 1,230.00 USD | 14,770.00 USD |
| `1D` | `0.0985` | 564,330.00 USD | 0.00 USD | 564,330.00 USD | 5,670.00 USD | 413.94 USD | 2,680.00 USD |
| `7D` | `0.0986` | 853,650.00 USD | 0.00 USD | 853,650.00 USD | 7,110.00 USD | 7,530.00 USD | 38,270.00 USD |
| `1D` | `0.0987` | 555,570.00 USD | 0.00 USD | 555,570.00 USD | 15,960.00 USD | 6,330.00 USD | 20,730.00 USD |
| `1D` | `0.0989` | 512,550.00 USD | 0.00 USD | 512,550.00 USD | 2,820.00 USD | 3,290.00 USD | 2,170.00 USD |
| `7D` | `0.0989` | 800,740.00 USD | 0.00 USD | 800,740.00 USD | 17,640.00 USD | 6,190.00 USD | 53,200.00 USD |
| `1D` | `0.0991` | 504,270.00 USD | 0.00 USD | 504,270.00 USD | 32,710.00 USD | 2,950.00 USD | 3,200.00 USD |
| `7D` | `0.0992` | 723,700.00 USD | 0.00 USD | 723,700.00 USD | 27,140.00 USD | 11,490.00 USD | 28,490.00 USD |
| `1D` | `0.0993` | 465,400.00 USD | 0.00 USD | 465,400.00 USD | 3,080.00 USD | 1,720.00 USD | 11,480.00 USD |
| `1D` | `0.0995` | 449,120.00 USD | 0.00 USD | 449,120.00 USD | 2,740.00 USD | 624.33 USD | 11,470.00 USD |
| `7D` | `0.0995` | 656,580.00 USD | 0.00 USD | 656,580.00 USD | 24,220.00 USD | 15,150.00 USD | 56,550.00 USD |
| `1D` | `0.0997` | 434,280.00 USD | 0.00 USD | 434,280.00 USD | 35,260.00 USD | 718.82 USD | 27,200.00 USD |
| `7D` | `0.0998` | 560,660.00 USD | 0.00 USD | 560,660.00 USD | 28,450.00 USD | 6,400.00 USD | 49,360.00 USD |
| `1D` | `0.0999` | 371,100.00 USD | 0.00 USD | 371,100.00 USD | 37,910.00 USD | 2,940.00 USD | 23,840.00 USD |
| `1D` | `0.1001` | 306,410.00 USD | 0.00 USD | 306,410.00 USD | 21,100.00 USD | 1,410.00 USD | 4,220.00 USD |
| `7D` | `0.1001` | 476,440.00 USD | 0.00 USD | 476,440.00 USD | 36,110.00 USD | 8,650.00 USD | 13,120.00 USD |
| `1D` | `0.1003` | 279,690.00 USD | 0.00 USD | 279,690.00 USD | 0.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1004` | 418,560.00 USD | 0.00 USD | 418,560.00 USD | 22,470.00 USD | 16,470.00 USD | 23,430.00 USD |
| `1D` | `0.1005` | 279,130.00 USD | 0.00 USD | 279,130.00 USD | 1,970.00 USD | 403.62 USD | 13,990.00 USD |
| `1D` | `0.1007` | 262,770.00 USD | 0.00 USD | 262,770.00 USD | 0.00 USD | 8,710.00 USD | 32,660.00 USD |
| `7D` | `0.1007` | 356,190.00 USD | 0.00 USD | 356,190.00 USD | 20,870.00 USD | 3,870.00 USD | 54,750.00 USD |
| `1D` | `0.1009` | 221,400.00 USD | 0.00 USD | 221,400.00 USD | 0.00 USD | 2,750.00 USD | 18.20 USD |
| `7D` | `0.1010` | 276,690.00 USD | 0.00 USD | 276,690.00 USD | 17,340.00 USD | 6,580.00 USD | 6,630.00 USD |
| `1D` | `0.1011` | 218,630.00 USD | 0.00 USD | 218,630.00 USD | 0.00 USD | 575.54 USD | 3,530.00 USD |
| `1D` | `0.1013` | 214,530.00 USD | 0.00 USD | 214,530.00 USD | 0.00 USD | 800.79 USD | 613.37 USD |
| `7D` | `0.1013` | 246,140.00 USD | 0.00 USD | 246,140.00 USD | 15,270.00 USD | 5,230.00 USD | 56,480.00 USD |
| `1D` | `0.1015` | 213,110.00 USD | 0.00 USD | 213,110.00 USD | 0.00 USD | 1,830.00 USD | 1,660.00 USD |
| `7D` | `0.1016` | 169,160.00 USD | 0.00 USD | 169,160.00 USD | 15,440.00 USD | 5,490.00 USD | 5,510.00 USD |
| `1D` | `0.1017` | 209,620.00 USD | 0.00 USD | 209,620.00 USD | 0.00 USD | 3,440.00 USD | 34,320.00 USD |
| `1D` | `0.1019` | 171,860.00 USD | 0.00 USD | 171,860.00 USD | 0.00 USD | 6,380.00 USD | 0.00 USD |
| `7D` | `0.1019` | 142,710.00 USD | 0.00 USD | 142,710.00 USD | 12,100.00 USD | 5,790.00 USD | 14,260.00 USD |
| `1D` | `0.1021` | 165,480.00 USD | 0.00 USD | 165,480.00 USD | 15,980.00 USD | 1,320.00 USD | 14,190.00 USD |
| `7D` | `0.1022` | 110,560.00 USD | 0.00 USD | 110,560.00 USD | 11,930.00 USD | 8,250.00 USD | 12,650.00 USD |
| `1D` | `0.1025` | 134,000.00 USD | 0.00 USD | 134,000.00 USD | 0.00 USD | 0.00 USD | 121.42 USD |
| `7D` | `0.1025` | 77,720.00 USD | 0.00 USD | 77,720.00 USD | 1,550.00 USD | 0.00 USD | 8,490.00 USD |
| `1D` | `0.1027` | 133,880.00 USD | 0.00 USD | 133,880.00 USD | 0.00 USD | 0.00 USD | 19.39 USD |
| `7D` | `0.1028` | 67,680.00 USD | 0.00 USD | 67,680.00 USD | 3,800.00 USD | 4,390.00 USD | 0.00 USD |
| `1D` | `0.1029` | 133,860.00 USD | 0.00 USD | 133,860.00 USD | 0.00 USD | 0.00 USD | 6,420.00 USD |
| `1D` | `0.1031` | 127,440.00 USD | 0.00 USD | 127,440.00 USD | 27,910.00 USD | 0.00 USD | 18,770.00 USD |
| `7D` | `0.1031` | 59,490.00 USD | 0.00 USD | 59,490.00 USD | 19,560.00 USD | 6,260.00 USD | 0.00 USD |
| `1D` | `0.1033` | 80,770.00 USD | 0.00 USD | 80,770.00 USD | 0.00 USD | 0.00 USD | 21,840.00 USD |
| `7D` | `0.1034` | 33,670.00 USD | 0.00 USD | 33,670.00 USD | 18,920.00 USD | 7,030.00 USD | 0.00 USD |
| `1D` | `0.1035` | 58,930.00 USD | 0.00 USD | 58,930.00 USD | 4,780.00 USD | 4,880.00 USD | 0.00 USD |
| `1D` | `0.1037` | 49,270.00 USD | 0.00 USD | 49,270.00 USD | 37,310.00 USD | 11,960.00 USD | 0.00 USD |
| `7D` | `0.1037` | 7,720.00 USD | 0.00 USD | 7,720.00 USD | 2,710.00 USD | 5,010.00 USD | 0.00 USD |
| `1D` | `0.1039` | 5,450.00 USD | 5,450.00 USD | 0.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD |
| `1D` | `0.1039` | 10,890.00 USD | 10,890.00 USD | 0.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD |
| `7D` | `0.1039` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1040` | 16,240.00 USD | 16,240.00 USD | 0.00 USD | 5,940.00 USD | 10,300.00 USD | 0.00 USD |
| `1D` | `0.1041` | 23,720.00 USD | 23,720.00 USD | 0.00 USD | 0.00 USD | 12,830.00 USD | 0.00 USD |
| `1D` | `0.1043` | 29,370.00 USD | 29,370.00 USD | 0.00 USD | 0.00 USD | 5,650.00 USD | 0.00 USD |
| `7D` | `0.1043` | 38,190.00 USD | 38,190.00 USD | 0.00 USD | 15,960.00 USD | 5,980.00 USD | 0.00 USD |
| `1D` | `0.1045` | 39,150.00 USD | 39,150.00 USD | 0.00 USD | 0.00 USD | 4,840.00 USD | 4,950.00 USD |
| `7D` | `0.1046` | 62,680.00 USD | 62,680.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD | 14,680.00 USD |
| `1D` | `0.1047` | 78,120.00 USD | 78,120.00 USD | 0.00 USD | 15,000.00 USD | 3,400.00 USD | 20,560.00 USD |
| `1D` | `0.1049` | 168,850.00 USD | 168,850.00 USD | 0.00 USD | 37,390.00 USD | 10,710.00 USD | 42,630.00 USD |
| `7D` | `0.1049` | 187,100.00 USD | 187,100.00 USD | 0.00 USD | 34,790.00 USD | 6,530.00 USD | 83,110.00 USD |
| `1D` | `0.1051` | 232,200.00 USD | 232,200.00 USD | 0.00 USD | 30,370.00 USD | 8,750.00 USD | 24,230.00 USD |
| `7D` | `0.1052` | 364,870.00 USD | 364,870.00 USD | 0.00 USD | 28,200.00 USD | 24,160.00 USD | 125,400.00 USD |
| `1D` | `0.1053` | 327,050.00 USD | 327,050.00 USD | 0.00 USD | 35,030.00 USD | 8,930.00 USD | 50,890.00 USD |
| `1D` | `0.1055` | 455,720.00 USD | 455,720.00 USD | 0.00 USD | 43,960.00 USD | 25,140.00 USD | 59,570.00 USD |
| `7D` | `0.1055` | 743,600.00 USD | 743,600.00 USD | 0.00 USD | 122,840.00 USD | 44,430.00 USD | 211,460.00 USD |
| `1D` | `0.1057` | 548,240.00 USD | 548,240.00 USD | 0.00 USD | 27,300.00 USD | 15,170.00 USD | 50,050.00 USD |
| `7D` | `0.1058` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 105,620.00 USD | 53,680.00 USD | 189,110.00 USD |
| `1D` | `0.1059` | 684,200.00 USD | 684,200.00 USD | 0.00 USD | 39,020.00 USD | 0.00 USD | 96,930.00 USD |
| `1D` | `0.1061` | 770,160.00 USD | 770,160.00 USD | 0.00 USD | 26,970.00 USD | 0.00 USD | 59,000.00 USD |
| `7D` | `0.1061` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 75,540.00 USD | 72,260.00 USD | 102,650.00 USD |
| `1D` | `0.1063` | 858,310.00 USD | 858,310.00 USD | 0.00 USD | 25,200.00 USD | 0.00 USD | 62,950.00 USD |
| `7D` | `0.1064` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 52,580.00 USD | 192,520.00 USD |
| `1D` | `0.1065` | 884,200.00 USD | 884,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25,890.00 USD |
| `1D` | `0.1067` | 917,400.00 USD | 917,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33,190.00 USD |
| `7D` | `0.1067` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 51,740.00 USD | 133,410.00 USD |
| `1D` | `0.1069` | 988,400.00 USD | 988,400.00 USD | 0.00 USD | 8,170.00 USD | 4,140.00 USD | 58,700.00 USD |
| `7D` | `0.1070` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 57,770.00 USD | 134,670.00 USD |
| `1D` | `0.1071` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 3,140.00 USD | 16,410.00 USD |
| `1D` | `0.1073` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 57.02 USD |
| `7D` | `0.1073` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 17,700.00 USD | 0.00 USD |
| `7D` | `0.1076` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,500.00 USD |
| `1D` | `0.1079` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,160.00 USD |
| `7D` | `0.1079` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 79.36 USD |
| `7D` | `0.1082` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 89.24 USD |
| `1D` | `0.1083` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 7,990.00 USD | 5,910.00 USD | 7,160.00 USD |
| `1D` | `0.1085` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65,090.00 USD |
| `7D` | `0.1085` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1087` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 28,490.00 USD | 2,240.00 USD | 44,800.00 USD |
| `7D` | `0.1088` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 5,290.00 USD | 0.00 USD | 113.96 USD |
| `1D` | `0.1089` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 39,160.00 USD | 0.00 USD | 152.23 USD |
| `1D` | `0.1091` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 33,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1091` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD |
| `1D` | `0.1093` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 15,480.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1094` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD |
| `1D` | `0.1095` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 21,520.00 USD |
| `1D` | `0.1097` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 7,260.00 USD | 1,970.00 USD | 22,800.00 USD |
| `7D` | `0.1097` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1099` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 6,130.00 USD | 1,940.00 USD | 0.00 USD |
| `7D` | `0.1100` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 21,840.00 USD |
| `1D` | `0.1101` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 4,310.00 USD | 2,820.00 USD | 4,290.00 USD |
| `1D` | `0.1103` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 3,540.00 USD | 5,640.00 USD | 96.09 USD |
| `7D` | `0.1103` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1105` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 3,380.00 USD | 4,740.00 USD | 10,700.00 USD |
| `7D` | `0.1106` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 22,880.00 USD | 16,040.00 USD |
| `1D` | `0.1107` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 3,110.00 USD | 12,720.00 USD | 35,750.00 USD |
| `1D` | `0.1109` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 2,110.00 USD | 1,120.00 USD | 0.00 USD |
| `7D` | `0.1109` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD |
| `1D` | `0.1111` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 5,200.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1112` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD |
| `1D` | `0.1113` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 21,390.00 USD | 5,210.00 USD | 39,070.00 USD |
| `1D` | `0.1115` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 4,760.00 USD | 0.00 USD | 8.95 USD |
| `1D` | `0.1117` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 2,060.00 USD | 25,630.00 USD | 34,770.00 USD |
| `7D` | `0.1118` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD |
| `1D` | `0.1119` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 33,110.00 USD | 6,980.00 USD | 36,740.00 USD |
| `1D` | `0.1121` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 20,000.00 USD | 12,060.00 USD | 12,310.00 USD |
| `7D` | `0.1121` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 17,760.00 USD | 0.00 USD | 32,100.00 USD |
| `1D` | `0.1123` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 40,400.00 USD | 1,780.00 USD | 5,970.00 USD |
| `7D` | `0.1124` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD |
| `1D` | `0.1125` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 11,130.00 USD | 13,240.00 USD | 7,920.00 USD |
| `1D` | `0.1127` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 1,250.00 USD | 19,510.00 USD |
| `7D` | `0.1127` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD |
| `1D` | `0.1129` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 8,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1130` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,170.00 USD |
| `1D` | `0.1131` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 20,830.00 USD | 8,010.00 USD | 17,960.00 USD |
| `1D` | `0.1133` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 6,530.00 USD | 22,520.00 USD | 23,560.00 USD |
| `7D` | `0.1133` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD |
| `1D` | `0.1135` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 4,040.00 USD | 3,670.00 USD | 4,090.00 USD |
| `7D` | `0.1136` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD |
| `1D` | `0.1137` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 856.93 USD | 244.57 USD |
| `1D` | `0.1139` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,280.00 USD |
| `7D` | `0.1139` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD |
| `1D` | `0.1141` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 13,860.00 USD | 2,800.00 USD | 20,340.00 USD |
| `7D` | `0.1142` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD |
| `1D` | `0.1143` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 20,300.00 USD | 27,990.00 USD | 11,830.00 USD |
| `1D` | `0.1145` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 13,430.00 USD | 11,690.00 USD | 38,040.00 USD |
| `7D` | `0.1145` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD |
| `1D` | `0.1147` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 10,640.00 USD | 10,080.00 USD | 30,670.00 USD |
| `7D` | `0.1148` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 176,010.00 USD |
| `1D` | `0.1149` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 35,170.00 USD | 624.71 USD | 31,790.00 USD |
| `1D` | `0.1151` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 16,450.00 USD | 14,620.00 USD | 33,250.00 USD |
| `7D` | `0.1151` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD |
| `1D` | `0.1153` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 31,350.00 USD | 23,630.00 USD | 59,020.00 USD |
| `7D` | `0.1154` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 243,190.00 USD | 26,970.00 USD | 195,390.00 USD |
| `1D` | `0.1155` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 38,430.00 USD | 27,080.00 USD | 54,070.00 USD |
| `1D` | `0.1157` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 33,550.00 USD | 8,310.00 USD | 7,920.00 USD |
| `7D` | `0.1157` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 188,950.00 USD | 25,290.00 USD | 98,310.00 USD |
| `1D` | `0.1159` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 19,470.00 USD | 7,420.00 USD | 17,890.00 USD |
| `7D` | `0.1160` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 139,350.00 USD | 32,830.00 USD | 109,320.00 USD |
| `1D` | `0.1161` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 23,670.00 USD | 0.00 USD | 5,140.00 USD |
| `1D` | `0.1163` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 9,380.00 USD | 17,430.00 USD |
| `7D` | `0.1163` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD |
| `1D` | `0.1165` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 4,990.00 USD | 5,320.00 USD | 1,830.00 USD |
| `7D` | `0.1166` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD |
| `1D` | `0.1167` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 7,220.00 USD | 6,140.00 USD |
| `1D` | `0.1169` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 5,480.00 USD | 2,440.00 USD | 2,290.00 USD |
| `7D` | `0.1169` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 82,770.00 USD | 26,150.00 USD | 112,810.00 USD |
| `1D` | `0.1171` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 13,800.00 USD | 0.00 USD | 4,530.00 USD |
| `7D` | `0.1172` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD |
| `1D` | `0.1173` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 2,840.00 USD | 5,440.00 USD | 4,860.00 USD |
| `1D` | `0.1175` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 9,530.00 USD | 9,020.00 USD | 19,850.00 USD |
| `7D` | `0.1175` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 72,770.00 USD | 17,930.00 USD | 81,630.00 USD |
| `1D` | `0.1177` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 14,360.00 USD | 8,560.00 USD | 16,740.00 USD |
| `7D` | `0.1178` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 89,510.00 USD | 23,660.00 USD | 55,770.00 USD |
| `1D` | `0.1179` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 10,640.00 USD | 3,990.00 USD | 5,740.00 USD |
| `1D` | `0.1181` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 12,400.00 USD | 4,120.00 USD | 15,740.00 USD |
| `7D` | `0.1181` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD |
| `1D` | `0.1183` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 8,760.00 USD | 677.63 USD | 4,570.00 USD |
| `7D` | `0.1184` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD |
| `1D` | `0.1185` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 4,390.00 USD | 5,850.00 USD | 6,770.00 USD |
| `1D` | `0.1187` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 2,150.00 USD | 3,330.00 USD | 9,870.00 USD |
| `7D` | `0.1187` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 5,620.00 USD | 17,120.00 USD | 54,960.00 USD |
| `1D` | `0.1189` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 2,120.00 USD | 4,330.00 USD |
| `7D` | `0.1190` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD |
| `1D` | `0.1191` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 1,810.00 USD | 5,650.00 USD |
| `1D` | `0.1193` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 4,720.00 USD | 1,040.00 USD | 1,950.00 USD |
| `7D` | `0.1193` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD |
| `1D` | `0.1195` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 6,310.00 USD | 1,470.00 USD | 2,730.00 USD |
| `7D` | `0.1196` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD |
| `1D` | `0.1197` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 1,040.00 USD | 129.36 USD |
| `1D` | `0.1199` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 431.42 USD | 3,030.00 USD |
| `7D` | `0.1199` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 9,100.00 USD | 13,190.00 USD | 67,980.00 USD |
| `1D` | `0.1201` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 3,250.00 USD | 1,390.00 USD | 9,710.00 USD |
| `7D` | `0.1202` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 138,430.00 USD | 21,430.00 USD | 32,790.00 USD |
| `1D` | `0.1203` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 5,670.00 USD | 413.94 USD | 2,680.00 USD |
| `1D` | `0.1205` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 2,250.00 USD | 1,670.00 USD | 770.70 USD |
| `7D` | `0.1205` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 132,960.00 USD | 72,910.00 USD | 130,900.00 USD |
| `1D` | `0.1207` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 5,540.00 USD | 524.23 USD | 4,100.00 USD |
| `7D` | `0.1208` | 6,760,000.00 USD | 6,760,000.00 USD | 0.00 USD | 39,480.00 USD | 25,720.00 USD | 66,520.00 USD |
| `1D` | `0.1209` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 2,820.00 USD | 3,290.00 USD | 2,200.00 USD |
| `1D` | `0.1211` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 4,800.00 USD | 2,950.00 USD | 3,220.00 USD |
| `7D` | `0.1211` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 72,500.00 USD | 25,920.00 USD | 111,160.00 USD |
| `1D` | `0.1213` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 5,870.00 USD | 1,720.00 USD | 11,480.00 USD |
| `7D` | `0.1214` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD |
| `1D` | `0.1215` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD | 5,420.00 USD |
| `1D` | `0.1217` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 1,090.00 USD | 624.33 USD | 6,050.00 USD |
| `7D` | `0.1217` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD |
| `1D` | `0.1219` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 2,320.00 USD | 718.82 USD | 10,070.00 USD |
| `7D` | `0.1220` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 45,700.00 USD | 10,970.00 USD | 54,700.00 USD |
| `1D` | `0.1221` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 7,970.00 USD | 2,940.00 USD | 3,630.00 USD |
| `1D` | `0.1223` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 2,660.00 USD | 1,410.00 USD | 4,200.00 USD |
| `7D` | `0.1223` | 7,410,000.00 USD | 7,410,000.00 USD | 0.00 USD | 76,930.00 USD | 36,110.00 USD | 50,790.00 USD |
| `1D` | `0.1225` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 1,840.00 USD | 558.39 USD | 21.44 USD |
| `7D` | `0.1226` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 54,940.00 USD | 32,070.00 USD | 5,210.00 USD |
| `1D` | `0.1227` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1229` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD |
| `7D` | `0.1229` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 81,840.00 USD | 38,040.00 USD | 79,050.00 USD |
| `7D` | `0.1232` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 67,800.00 USD | 33,050.00 USD | 63,720.00 USD |
| `7D` | `0.1235` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 15,040.00 USD | 5,390.00 USD | 17,120.00 USD |
| `7D` | `0.1238` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 8,310.00 USD | 3,610.00 USD | 3,100.00 USD |
| `7D` | `0.1241` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 11,380.00 USD | 1,380.00 USD | 7,090.00 USD |
| `7D` | `0.1244` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 26,540.00 USD | 8,130.00 USD | 9,660.00 USD |
| `7D` | `0.1247` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 7,900.00 USD | 18,280.00 USD | 17,680.00 USD |
| `7D` | `0.1250` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 8,540.00 USD | 7,270.00 USD | 5,780.00 USD |
| `7D` | `0.1253` | 8,070,000.00 USD | 8,070,000.00 USD | 0.00 USD | 6,550.00 USD | 0.00 USD | 16,470.00 USD |
| `7D` | `0.1256` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 11,990.00 USD | 13,660.00 USD | 220.44 USD |
| `7D` | `0.1259` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 5,870.00 USD | 1,190.00 USD | 151.34 USD |
| `7D` | `0.1262` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | 3,530.00 USD |
| `7D` | `0.1265` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 2,710.00 USD | 0.00 USD | 7,350.00 USD |
| `7D` | `0.1268` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD |
| `7D` | `0.1271` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 5,940.00 USD | 0.00 USD | 30.15 USD |
| `7D` | `0.1274` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12.00 USD |
| `7D` | `0.1277` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31.66 USD |
| `7D` | `0.1280` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,390.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `66.12M` | Total OI Tokens: `635,474,851.0 OP`
  * 1h OI Change: `-5.13%` | 4h OI Change: `-11.37%` | 24h OI Change: `-13.94%`
  * Exchange Breakdown: Binance=`15.11M` | Bybit=`13.21M` | OKX=`3.66M` | Hyperliquid=`3.40M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-2.08K` | Last 24h: `270.64` | Last 3d: `-2.23K` | Last 7d: `-15.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0185%` | **USDT OKX** | `0.0027%` |
| **USDT Bybit** | `0.0050%` | **USDT KuCoin** | `0.0097%` |
| **USDT MEXC** | `-0.0183%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0034%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `47.35%` | `52.65%` | `0.90` | 4,940,000.00 USD |
| `15M` | `Binance` | `40.65%` | `59.35%` | `0.68` | 1,990,000.00 USD |
| `15M` | `OKX` | `51%` | `49%` | `1.04` | 563,820.00 USD |
| `15M` | `Bybit` | `47.24%` | `52.76%` | `0.90` | 440,380.00 USD |
| `15M` | `KuCoin` | `60.03%` | `39.97%` | `1.50` | 215,200.00 USD |
| `15M` | `Gate` | `37.56%` | `62.44%` | `0.60` | 52,830.00 USD |
| `15M` | `Bitget` | `47.25%` | `52.75%` | `0.90` | 203,620.00 USD |
| `15M` | `BingX` | `53.5%` | `46.5%` | `1.15` | 90,010.00 USD |
| `15M` | `MEXC` | `84.42%` | `15.58%` | `5.42` | 85,920.00 USD |
| `15M` | `Bitunix` | `60.18%` | `39.82%` | `1.51` | 294,680.00 USD |
| `15M` | `Hyperliquid` | `68.81%` | `31.19%` | `2.21` | 16,990.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.32%` | `50.68%` | `0.97` | 787,870.00 USD |
| `15M` | `Crypto.com` | `5.87%` | `94.13%` | `0.06` | 47.23 USD |
| `15M` | `WhiteBIT` | `49.9%` | `50.1%` | `1.00` | 177,720.00 USD |
| `15M` | `HTX` | `47.55%` | `52.45%` | `0.91` | 2,080.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `85.9%` | `14.1%` | `6.09` | 2,100.00 USD |
| `15M` | `Aster` | `0.7%` | `99.3%` | `0.01` | 15,470.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `23.44%` | `76.56%` | `0.31` | 3,510.00 USD |
| `15M` | `Whale Positions` | `40.65%` | `59.35%` | `0.68` | 1,990,000.00 USD |
| `15M` | `Global Accounts` | `47.35%` | `52.65%` | `0.90` | 4,940,000.00 USD |
| `1H` | `OP` | `44.79%` | `55.21%` | `0.81` | 45,990,000.00 USD |
| `1H` | `Binance` | `44.06%` | `55.94%` | `0.79` | 19,350,000.00 USD |
| `1H` | `OKX` | `49.44%` | `50.56%` | `0.98` | 6,150,000.00 USD |
| `1H` | `Bybit` | `47.91%` | `52.09%` | `0.92` | 8,220,000.00 USD |
| `1H` | `KuCoin` | `47.29%` | `52.71%` | `0.90` | 997,220.00 USD |
| `1H` | `Gate` | `46.39%` | `53.61%` | `0.87` | 938,140.00 USD |
| `1H` | `Bitget` | `47.69%` | `52.31%` | `0.91` | 2,110,000.00 USD |
| `1H` | `BingX` | `22%` | `78%` | `0.28` | 2,470,000.00 USD |
| `1H` | `MEXC` | `39.65%` | `60.35%` | `0.66` | 1,990,000.00 USD |
| `1H` | `Bitunix` | `46.81%` | `53.19%` | `0.88` | 706,420.00 USD |
| `1H` | `Hyperliquid` | `52.01%` | `47.99%` | `1.08` | 1,220,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `44.24%` | `55.76%` | `0.79` | 290,040.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `48.68%` | `51.32%` | `0.95` | 1,120,000.00 USD |
| `1H` | `HTX` | `55.33%` | `44.67%` | `1.24` | 71,750.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `55.48%` | `44.52%` | `1.25` | 127,050.00 USD |
| `1H` | `Aster` | `57.48%` | `42.52%` | `1.35` | 149,450.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `11.45%` | `88.55%` | `0.13` | 61,830.00 USD |
| `1H` | `Whale Positions` | `44.06%` | `55.94%` | `0.79` | 19,350,000.00 USD |
| `1H` | `Global Accounts` | `44.79%` | `55.21%` | `0.81` | 45,990,000.00 USD |
| `4H` | `OP` | `48.25%` | `51.75%` | `0.93` | 113,050,000.00 USD |
| `4H` | `Binance` | `49.96%` | `50.04%` | `1.00` | 43,920,000.00 USD |
| `4H` | `OKX` | `49.63%` | `50.37%` | `0.99` | 16,420,000.00 USD |
| `4H` | `Bybit` | `48.39%` | `51.61%` | `0.94` | 12,310,000.00 USD |
| `4H` | `KuCoin` | `49.58%` | `50.42%` | `0.98` | 2,280,000.00 USD |
| `4H` | `Gate` | `53.56%` | `46.44%` | `1.15` | 2,800,000.00 USD |
| `4H` | `Bitget` | `47.73%` | `52.27%` | `0.91` | 3,940,000.00 USD |
| `4H` | `BingX` | `47.1%` | `52.9%` | `0.89` | 2,780,000.00 USD |
| `4H` | `MEXC` | `44.79%` | `55.21%` | `0.81` | 1,760,000.00 USD |
| `4H` | `Bitunix` | `52.64%` | `47.36%` | `1.11` | 4,120,000.00 USD |
| `4H` | `Hyperliquid` | `32.04%` | `67.96%` | `0.47` | 1,370,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.76%` | `50.24%` | `0.99` | 17,690,000.00 USD |
| `4H` | `Crypto.com` | `48.51%` | `51.49%` | `0.94` | 2,520.00 USD |
| `4H` | `WhiteBIT` | `6.49%` | `93.51%` | `0.07` | 2,930,000.00 USD |
| `4H` | `HTX` | `43.78%` | `56.22%` | `0.78` | 114,230.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `38.94%` | `61.06%` | `0.64` | 190,060.00 USD |
| `4H` | `Aster` | `41.1%` | `58.9%` | `0.70` | 306,350.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `35.3%` | `64.7%` | `0.55` | 110,240.00 USD |
| `4H` | `Whale Positions` | `49.96%` | `50.04%` | `1.00` | 43,920,000.00 USD |
| `4H` | `Global Accounts` | `48.25%` | `51.75%` | `0.93` | 113,050,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1098` | `0.1100` | `0.1098` | `0.1102` | `0.1096` | 199,782.25 USD | 121,152.98 USD | 78,629.27 USD | 42,523.71 USD | `+21.29%` | `24B / 5S` |
| `0:00 UTC` | `0.1103` | `0.1104` | `0.1103` | `0.1106` | `0.1100` | 230,285.46 USD | 143,965.28 USD | 86,320.18 USD | 57,645.10 USD | `+25.03%` | `14B / 4S` |
| `5:00 UTC` | `0.1102` | `0.1102` | `0.1102` | `0.1105` | `0.1099` | 215,356.47 USD | 112,661.20 USD | 102,695.27 USD | 9,965.93 USD | `+4.63%` | `7B / 11S` |
| `0:00 UTC` | `0.1077` | `0.1082` | `0.1077` | `0.1102` | `0.1070` | 2,425,114.31 USD | 1,046,280.57 USD | 1,378,833.74 USD | -332,553.17 USD | `-13.71%` | `8B / 30S` |
| `5:00 UTC` | `0.1084` | `0.1083` | `0.1084` | `0.1087` | `0.1080` | 527,563.25 USD | 310,298.99 USD | 217,264.26 USD | 93,034.72 USD | `+17.63%` | `19B / 3S` |
| `0:00 UTC` | `0.1063` | `0.1047` | `0.1063` | `0.1088` | `0.1013` | 5,548,996.22 USD | 2,272,459.88 USD | 3,276,536.35 USD | -1,004,076.47 USD | `-18.09%` | `5B / 37S` |
| `5:00 UTC` | `0.1014` | `0.1013` | `0.1014` | `0.1029` | `0.0990` | 5,717,098.88 USD | 2,672,854.06 USD | 3,044,244.81 USD | -371,390.75 USD | `-6.50%` | `7B / 23S` |
| `0:00 UTC` | `0.1025` | `0.1020` | `0.1025` | `0.1033` | `0.1007` | 1,857,629.60 USD | 946,076.57 USD | 911,553.03 USD | 34,523.54 USD | `+1.86%` | `19B / 6S` |
| `5:00 UTC` | `0.1043` | `0.1035` | `0.1043` | `0.1044` | `0.1026` | 1,285,007.52 USD | 601,525.80 USD | 683,481.72 USD | -81,955.93 USD | `-6.38%` | `27B / 29S` |
| `0:00 UTC` | `0.1037` | `0.1038` | `0.1037` | `0.1042` | `0.1032` | 619,636.89 USD | 289,821.87 USD | 329,815.02 USD | -39,993.15 USD | `-6.45%` | `20B / 16S` |

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
| `5m` | -3,550.00 USD | 4,730.00 USD | **`ACCUMULATION`** |
| `15m` | 23,300.00 USD | -107,690.00 USD | **`DISTRIBUTION`** |
| `30m` | 104,790.00 USD | 92,800.00 USD | **`ACCUMULATION`** |
| `1h` | 31,900.00 USD | -2,640,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -172,650.00 USD | -2,920,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -200,090.00 USD | -2,920,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -199,900.00 USD | -3,170,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -81,210.00 USD | -2,380,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 53,110.00 USD | -2,270,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -77,350.00 USD | -4,850,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -268,630.00 USD | -12,630,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,650,000.00 USD | -81,480,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-3.55K` | 15m=`+23.30K` | 1h=`+31.90K` | 24h=`-77.35K`
* Futures Capital Netflows: 5m=`+4.73K` | 15m=`-107.69K` | 1h=`-2.64M` | 24h=`-4.85M`
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
  * `2026-10-30 02:54:26 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:10:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:11:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:11:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:11:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
