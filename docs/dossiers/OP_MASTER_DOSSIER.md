# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 03:01:01 IST` (`2026-10-29 21:31:01 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1014` | `0.1027` | `0.1012` | `0.1027` | `5,964,116` | 609,080.47 USD | -41,629.23 USD | `-6.83%` | -2,750,026.33 USD | `+0.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.1027` | `0.1032` | `0.1024` | `0.1029` | `3,496,067` | 359,057.68 USD | 37,468.38 USD | `+10.44%` | -2,712,557.94 USD | `+0.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1029` | `0.1030` | `0.1028` | `0.1029` | `62,150` | 6,397.31 USD | 3,375.79 USD | `+52.77%` | -2,709,182.15 USD | `+0.44` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1024` | `0.1029` | `0.0989` | `0.1012` | `56,419,228` | 5,717,098.88 USD | -371,390.75 USD | `-6.50%` | -2,739,413.30 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1012` | `0.1032` | `0.1007` | `0.1029` | `18,216,274` | 1,857,629.60 USD | 34,523.54 USD | `+1.86%` | -2,704,889.75 USD | `+0.53` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1029` | `0.1030` | `0.1028` | `0.1029` | `62,150` | 6,397.31 USD | 3,375.79 USD | `+52.77%` | -2,701,513.96 USD | `+0.40` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.1100` | `0.1106` | `0.1096` | `0.1101` | `7,910,873` | 870,770.93 USD | 117,397.34 USD | `+13.48%` | -1,177,554.63 USD | `+0.73` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `136,699,709` | 14,218,772.66 USD | -1,614,985.67 USD | `-11.36%` | -2,792,540.30 USD | `-3.57` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1012` | `0.1032` | `0.1007` | `0.1029` | `18,306,302` | 1,866,896.97 USD | 40,732.27 USD | `+2.18%` | -2,751,808.02 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -935,828.18 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | -1,111,968.46 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1029` | `155,006,011` | 16,085,669.63 USD | -1,574,253.39 USD | `-9.79%` | -2,686,221.86 USD | `-1.42` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1085` | `0.1106` | `0.1071` | `0.1076` | `47,048,931` | 5,111,570.05 USD | 108,567.99 USD | `+2.12%` | -1,419,806.61 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,277,083.78 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -935,828.18 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | -1,111,968.46 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1029` | `155,006,011` | 16,085,669.63 USD | -1,574,253.39 USD | `-9.79%` | -2,686,221.86 USD | `-1.42` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:55:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1101` | 5,182.99 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 5.18K USD at 0.1101 USD [API] | `2026-10-28 13:20:09` |
| `ANNOUNCEMENT` | `INFO` | `0.1100` | 5,889.99 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale BUY: 5.89K USD at 0.1100 USD [API] | `2026-10-28 14:48:40` |


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
| `7D` | `Long Liquidation` | `0.0878` | 1,210,000.00 USD | 1,210,000.00 USD | 1,370.00 USD | 4,930.00 USD | 27,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0881` | 833,500.00 USD | 833,500.00 USD | 2,400.00 USD | 1,300.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0881` | 1,180,000.00 USD | 1,180,000.00 USD | 3,770.00 USD | 2,660.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0883` | 825,100.00 USD | 825,100.00 USD | 2,370.00 USD | 659.34 USD | 5,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0884` | 1,160,000.00 USD | 1,160,000.00 USD | 7,040.00 USD | 4,640.00 USD | 11,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0885` | 816,090.00 USD | 816,090.00 USD | 0.00 USD | 312.16 USD | 2,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0887` | 813,260.00 USD | 813,260.00 USD | 1,740.00 USD | 655.48 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0887` | 1,130,000.00 USD | 1,130,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0889` | 806,330.00 USD | 806,330.00 USD | 727.20 USD | 1,690.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0890` | 1,100,000.00 USD | 1,100,000.00 USD | 14,610.00 USD | 4,470.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0891` | 801,810.00 USD | 801,810.00 USD | 1,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0893` | 800,480.00 USD | 800,480.00 USD | 983.61 USD | 0.00 USD | 542.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0893` | 1,080,000.00 USD | 1,080,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0895` | 798,960.00 USD | 798,960.00 USD | 0.00 USD | 215.06 USD | 394.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,120.00 USD | 108,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0896` | 1,060,000.00 USD | 1,060,000.00 USD | 5,760.00 USD | 611.80 USD | 6,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0897` | 798,350.00 USD | 798,350.00 USD | 0.00 USD | 772.87 USD | 0.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0899` | 797,570.00 USD | 797,570.00 USD | 0.00 USD | 287.77 USD | 601.21 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0899` | 1,040,000.00 USD | 1,040,000.00 USD | 3,390.00 USD | 927.82 USD | 4,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0901` | 796,680.00 USD | 796,680.00 USD | 2,450.00 USD | 0.00 USD | 293.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0902` | 1,040,000.00 USD | 1,040,000.00 USD | 2,270.00 USD | 910.78 USD | 1,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0903` | 793,940.00 USD | 793,940.00 USD | 831.11 USD | 2,190.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0905` | 789,850.00 USD | 789,850.00 USD | 413.91 USD | 998.41 USD | 2,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0905` | 1,030,000.00 USD | 1,030,000.00 USD | 10,350.00 USD | 996.61 USD | 4,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0905` | 1,260.00 USD | 105,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0907` | 785,600.00 USD | 785,600.00 USD | 2,290.00 USD | 909.44 USD | 974.67 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0908` | 1,020,000.00 USD | 1,020,000.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0909` | 781,430.00 USD | 781,430.00 USD | 938.76 USD | 957.38 USD | 785.45 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0911` | 778,750.00 USD | 778,750.00 USD | 5,580.00 USD | 778.50 USD | 5.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0911` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0913` | 772,380.00 USD | 772,380.00 USD | 0.00 USD | 0.00 USD | 787.25 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0914` | 1,000,000.00 USD | 1,000,000.00 USD | 1,670.00 USD | 903.90 USD | 45.81 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0915` | 771,590.00 USD | 771,590.00 USD | 6,590.00 USD | 0.00 USD | 52.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0917` | 764,950.00 USD | 764,950.00 USD | 2,550.00 USD | 0.00 USD | 2.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0917` | 998,600.00 USD | 998,600.00 USD | 0.00 USD | 0.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0919` | 762,400.00 USD | 762,400.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0923` | 758,710.00 USD | 758,710.00 USD | 0.00 USD | 0.00 USD | 42.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0923` | 996,860.00 USD | 996,860.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0925` | 758,670.00 USD | 758,670.00 USD | 3,270.00 USD | 1,660.00 USD | 6,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0926` | 995,400.00 USD | 995,400.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0932` | 985,420.00 USD | 985,420.00 USD | 0.00 USD | 0.00 USD | 12,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0933` | 747,380.00 USD | 747,380.00 USD | 0.00 USD | 0.00 USD | 6,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0935` | 973,310.00 USD | 973,310.00 USD | 0.00 USD | 1,320.00 USD | 6,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0937` | 740,520.00 USD | 740,520.00 USD | 0.00 USD | 0.00 USD | 64.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0938` | 965,500.00 USD | 965,500.00 USD | 0.00 USD | 0.00 USD | 8.57 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0939` | 740,450.00 USD | 740,450.00 USD | 0.00 USD | 0.00 USD | 76.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0941` | 965,490.00 USD | 965,490.00 USD | 2,050.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0944` | 960,420.00 USD | 960,420.00 USD | 1,870.00 USD | 0.00 USD | 7,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0945` | 69,120.00 USD | 104,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0947` | 740,380.00 USD | 740,380.00 USD | 0.00 USD | 0.00 USD | 69.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0947` | 951,030.00 USD | 951,030.00 USD | 3,790.00 USD | 1,810.00 USD | 112.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0950` | 945,310.00 USD | 945,310.00 USD | 3,770.00 USD | 0.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0953` | 740,310.00 USD | 740,310.00 USD | 0.00 USD | 0.00 USD | 87.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0953` | 934,880.00 USD | 934,880.00 USD | 0.00 USD | 0.00 USD | 4.65 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0955` | 740,220.00 USD | 740,220.00 USD | 0.00 USD | 1,180.00 USD | 166.88 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0955` | 2,040.00 USD | 35,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0959` | 934,870.00 USD | 934,870.00 USD | 0.00 USD | 1,140.00 USD | 115.48 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0961` | 738,870.00 USD | 738,870.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0962` | 933,620.00 USD | 933,620.00 USD | 0.00 USD | 0.00 USD | 121.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0963` | 736,790.00 USD | 736,790.00 USD | 0.00 USD | 0.00 USD | 1.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0965` | 736,790.00 USD | 736,790.00 USD | 1,280.00 USD | 282.32 USD | 1,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0965` | 1,160.00 USD | 33,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0967` | 733,350.00 USD | 733,350.00 USD | 2,660.00 USD | 1,100.00 USD | 7,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0968` | 933,500.00 USD | 933,500.00 USD | 7,490.00 USD | 3,720.00 USD | 11,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0969` | 722,090.00 USD | 722,090.00 USD | 4,590.00 USD | 2,640.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0971` | 705,850.00 USD | 705,850.00 USD | 16,100.00 USD | 3,330.00 USD | 4,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 910,660.00 USD | 910,660.00 USD | 0.00 USD | 3,760.00 USD | 9,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0973` | 681,810.00 USD | 681,810.00 USD | 0.00 USD | 2,120.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0974` | 897,180.00 USD | 897,180.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0975` | 675,290.00 USD | 675,290.00 USD | 0.00 USD | 1,810.00 USD | 5,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0975` | 11,950.00 USD | 32,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0977` | 667,920.00 USD | 667,920.00 USD | 24,760.00 USD | 2,510.00 USD | 11,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0977` | 892,910.00 USD | 892,910.00 USD | 0.00 USD | 1,160.00 USD | 13,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0979` | 629,420.00 USD | 629,420.00 USD | 12,620.00 USD | 1,040.00 USD | 8.08 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0980` | 878,620.00 USD | 878,620.00 USD | 0.00 USD | 3,920.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0981` | 615,750.00 USD | 615,750.00 USD | 9,220.00 USD | 431.42 USD | 3,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0983` | 603,070.00 USD | 603,070.00 USD | 3,250.00 USD | 1,390.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 868,990.00 USD | 868,990.00 USD | 7,990.00 USD | 1,230.00 USD | 14,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0985` | 582,320.00 USD | 582,320.00 USD | 5,670.00 USD | 413.94 USD | 2,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0985` | 20,130.00 USD | 20,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0986` | 844,990.00 USD | 844,990.00 USD | 7,110.00 USD | 7,530.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0987` | 573,560.00 USD | 573,560.00 USD | 15,960.00 USD | 6,330.00 USD | 20,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0989` | 530,560.00 USD | 530,560.00 USD | 2,820.00 USD | 3,290.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 792,080.00 USD | 792,080.00 USD | 17,640.00 USD | 6,190.00 USD | 53,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0991` | 522,130.00 USD | 522,130.00 USD | 32,710.00 USD | 2,950.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0992` | 715,050.00 USD | 715,050.00 USD | 27,140.00 USD | 11,490.00 USD | 28,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0993` | 483,270.00 USD | 483,270.00 USD | 3,080.00 USD | 1,720.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0995` | 467,010.00 USD | 467,010.00 USD | 2,740.00 USD | 624.33 USD | 11,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 647,920.00 USD | 647,920.00 USD | 24,220.00 USD | 15,150.00 USD | 56,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0997` | 452,160.00 USD | 452,160.00 USD | 35,260.00 USD | 718.82 USD | 27,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0998` | 552,310.00 USD | 552,310.00 USD | 28,450.00 USD | 6,400.00 USD | 49,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0999` | 388,980.00 USD | 388,980.00 USD | 37,910.00 USD | 2,940.00 USD | 23,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1001` | 324,240.00 USD | 324,240.00 USD | 21,100.00 USD | 1,410.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 468,100.00 USD | 468,100.00 USD | 36,110.00 USD | 8,650.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1003` | 297,540.00 USD | 297,540.00 USD | 0.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1004` | 410,210.00 USD | 410,210.00 USD | 22,470.00 USD | 16,470.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1005` | 296,980.00 USD | 296,980.00 USD | 1,970.00 USD | 403.62 USD | 13,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1007` | 280,670.00 USD | 280,670.00 USD | 0.00 USD | 8,710.00 USD | 32,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 347,840.00 USD | 347,840.00 USD | 20,870.00 USD | 3,870.00 USD | 54,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1009` | 239,360.00 USD | 239,360.00 USD | 0.00 USD | 2,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1010` | 268,350.00 USD | 268,350.00 USD | 17,340.00 USD | 6,580.00 USD | 6,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1011` | 236,610.00 USD | 236,610.00 USD | 0.00 USD | 575.54 USD | 3,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1013` | 232,650.00 USD | 232,650.00 USD | 0.00 USD | 800.79 USD | 587.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 237,790.00 USD | 237,790.00 USD | 15,270.00 USD | 5,230.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1015` | 231,260.00 USD | 231,260.00 USD | 0.00 USD | 1,830.00 USD | 1,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1016` | 205,810.00 USD | 205,810.00 USD | 15,440.00 USD | 5,490.00 USD | 49,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1017` | 227,770.00 USD | 227,770.00 USD | 0.00 USD | 3,440.00 USD | 34,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1019` | 190,010.00 USD | 190,010.00 USD | 0.00 USD | 6,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1019` | 134,990.00 USD | 134,990.00 USD | 12,100.00 USD | 5,790.00 USD | 14,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1021` | 183,630.00 USD | 183,630.00 USD | 15,980.00 USD | 1,320.00 USD | 14,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1022` | 102,840.00 USD | 102,840.00 USD | 11,930.00 USD | 8,250.00 USD | 12,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1025` | 70,000.00 USD | 70,000.00 USD | 1,550.00 USD | 0.00 USD | 8,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1028` | 59,960.00 USD | 59,960.00 USD | 3,800.00 USD | 4,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1029` | 152,150.00 USD | 152,150.00 USD | 0.00 USD | 0.00 USD | 6,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1031` | 145,910.00 USD | 145,910.00 USD | 27,910.00 USD | 0.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1031` | 51,770.00 USD | 51,770.00 USD | 19,560.00 USD | 6,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1033` | 99,110.00 USD | 99,110.00 USD | 0.00 USD | 0.00 USD | 21,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1034` | 25,950.00 USD | 25,950.00 USD | 18,920.00 USD | 7,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1035` | 77,250.00 USD | 77,250.00 USD | 4,780.00 USD | 4,880.00 USD | 54.66 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1037` | 67,540.00 USD | 67,540.00 USD | 37,310.00 USD | 11,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1037` | 7,720.00 USD | 7,720.00 USD | 2,710.00 USD | 5,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1039` | 18,270.00 USD | 18,270.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1040` | 23,960.00 USD | 23,960.00 USD | 5,940.00 USD | 10,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1041` | 12,830.00 USD | 12,830.00 USD | 0.00 USD | 12,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1043` | 5,650.00 USD | 5,650.00 USD | 0.00 USD | 5,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1043` | 45,910.00 USD | 45,910.00 USD | 15,960.00 USD | 5,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1045` | 15,440.00 USD | 15,440.00 USD | 0.00 USD | 4,840.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1046` | 70,400.00 USD | 70,400.00 USD | 0.00 USD | 9,810.00 USD | 14,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1047` | 54,400.00 USD | 54,400.00 USD | 15,000.00 USD | 3,400.00 USD | 20,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1049` | 145,130.00 USD | 145,130.00 USD | 37,390.00 USD | 10,710.00 USD | 42,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1049` | 194,820.00 USD | 194,820.00 USD | 34,790.00 USD | 6,530.00 USD | 83,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1051` | 208,480.00 USD | 208,480.00 USD | 30,370.00 USD | 8,750.00 USD | 24,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1052` | 372,590.00 USD | 372,590.00 USD | 28,200.00 USD | 24,160.00 USD | 125,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1053` | 303,290.00 USD | 303,290.00 USD | 35,030.00 USD | 8,930.00 USD | 50,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1055` | 432,100.00 USD | 432,100.00 USD | 43,960.00 USD | 25,140.00 USD | 59,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1055` | 706,330.00 USD | 706,330.00 USD | 122,840.00 USD | 44,430.00 USD | 166,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1057` | 524,650.00 USD | 524,650.00 USD | 27,300.00 USD | 15,170.00 USD | 50,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1058` | 1,100,000.00 USD | 1,100,000.00 USD | 105,620.00 USD | 53,680.00 USD | 233,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1059` | 660,630.00 USD | 660,630.00 USD | 39,020.00 USD | 0.00 USD | 96,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1061` | 746,540.00 USD | 746,540.00 USD | 26,970.00 USD | 0.00 USD | 58,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1061` | 1,350,000.00 USD | 1,350,000.00 USD | 75,540.00 USD | 72,260.00 USD | 102,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1063` | 834,790.00 USD | 834,790.00 USD | 25,200.00 USD | 0.00 USD | 63,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1064` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 52,580.00 USD | 192,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1065` | 860,540.00 USD | 860,540.00 USD | 0.00 USD | 0.00 USD | 25,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1067` | 893,700.00 USD | 893,700.00 USD | 0.00 USD | 0.00 USD | 33,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1067` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 51,740.00 USD | 133,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1069` | 964,550.00 USD | 964,550.00 USD | 8,170.00 USD | 4,140.00 USD | 58,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1070` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 57,770.00 USD | 134,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1071` | 983,920.00 USD | 983,920.00 USD | 0.00 USD | 3,140.00 USD | 16,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1073` | 984,140.00 USD | 984,140.00 USD | 0.00 USD | 0.00 USD | 218.01 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1073` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 17,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1075` | 984,240.00 USD | 984,240.00 USD | 0.00 USD | 0.00 USD | 104.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1076` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1077` | 984,330.00 USD | 984,330.00 USD | 0.00 USD | 0.00 USD | 93.46 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1079` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 17,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1079` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 79.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1082` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 89.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1083` | 1,020,000.00 USD | 1,020,000.00 USD | 7,990.00 USD | 5,910.00 USD | 7,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1085` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 65,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1085` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1087` | 1,160,000.00 USD | 1,160,000.00 USD | 28,490.00 USD | 2,240.00 USD | 44,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1088` | 2,020,000.00 USD | 2,020,000.00 USD | 5,290.00 USD | 0.00 USD | 113.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1089` | 1,200,000.00 USD | 1,200,000.00 USD | 39,160.00 USD | 0.00 USD | 87.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1091` | 1,240,000.00 USD | 1,240,000.00 USD | 33,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1091` | 2,040,000.00 USD | 2,040,000.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1093` | 1,250,000.00 USD | 1,250,000.00 USD | 15,480.00 USD | 0.00 USD | 192.45 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1094` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1095` | 1,280,000.00 USD | 1,280,000.00 USD | 4,110.00 USD | 1,890.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1097` | 1,310,000.00 USD | 1,310,000.00 USD | 7,260.00 USD | 1,970.00 USD | 22,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1097` | 2,070,000.00 USD | 2,070,000.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1099` | 1,320,000.00 USD | 1,320,000.00 USD | 6,130.00 USD | 1,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1100` | 2,100,000.00 USD | 2,100,000.00 USD | 11,470.00 USD | 0.00 USD | 21,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1101` | 1,330,000.00 USD | 1,330,000.00 USD | 4,310.00 USD | 2,820.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1103` | 1,340,000.00 USD | 1,340,000.00 USD | 3,540.00 USD | 5,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 2,140,000.00 USD | 2,140,000.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1105` | 1,360,000.00 USD | 1,360,000.00 USD | 3,380.00 USD | 4,740.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1106` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 22,880.00 USD | 16,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1107` | 1,410,000.00 USD | 1,410,000.00 USD | 3,110.00 USD | 12,720.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1109` | 1,410,000.00 USD | 1,410,000.00 USD | 2,110.00 USD | 1,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1111` | 1,420,000.00 USD | 1,420,000.00 USD | 5,200.00 USD | 0.00 USD | 96.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1112` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1113` | 1,480,000.00 USD | 1,480,000.00 USD | 21,390.00 USD | 5,210.00 USD | 39,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1115` | 1,490,000.00 USD | 1,490,000.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1117` | 1,550,000.00 USD | 1,550,000.00 USD | 2,060.00 USD | 25,630.00 USD | 34,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1118` | 2,290,000.00 USD | 2,290,000.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1119` | 1,630,000.00 USD | 1,630,000.00 USD | 33,110.00 USD | 6,980.00 USD | 36,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1121` | 1,670,000.00 USD | 1,670,000.00 USD | 20,000.00 USD | 12,060.00 USD | 12,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 2,340,000.00 USD | 2,340,000.00 USD | 17,760.00 USD | 0.00 USD | 32,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1123` | 1,720,000.00 USD | 1,720,000.00 USD | 40,400.00 USD | 1,780.00 USD | 5,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1124` | 2,440,000.00 USD | 2,440,000.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1125` | 1,750,000.00 USD | 1,750,000.00 USD | 11,130.00 USD | 13,240.00 USD | 7,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1127` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 1,250.00 USD | 19,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1127` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1129` | 1,780,000.00 USD | 1,780,000.00 USD | 8,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1130` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 15,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1131` | 1,830,000.00 USD | 1,830,000.00 USD | 20,830.00 USD | 8,010.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1133` | 1,880,000.00 USD | 1,880,000.00 USD | 6,530.00 USD | 22,520.00 USD | 23,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 2,510,000.00 USD | 2,510,000.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1135` | 1,890,000.00 USD | 1,890,000.00 USD | 4,040.00 USD | 3,670.00 USD | 4,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1135` | 557.61 USD | 557.61 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1136` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1137` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 856.93 USD | 40.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1139` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 14,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1139` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 8,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1141` | 1,950,000.00 USD | 1,950,000.00 USD | 13,860.00 USD | 2,800.00 USD | 20,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1142` | 2,550,000.00 USD | 2,550,000.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1143` | 2,010,000.00 USD | 2,010,000.00 USD | 20,300.00 USD | 27,990.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1145` | 2,070,000.00 USD | 2,070,000.00 USD | 13,430.00 USD | 11,690.00 USD | 38,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 2,790,000.00 USD | 2,790,000.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1147` | 2,120,000.00 USD | 2,120,000.00 USD | 10,640.00 USD | 10,080.00 USD | 30,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1148` | 2,980,000.00 USD | 2,980,000.00 USD | 9,880.00 USD | 0.00 USD | 176,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1149` | 2,190,000.00 USD | 2,190,000.00 USD | 35,170.00 USD | 624.71 USD | 31,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1151` | 2,250,000.00 USD | 2,250,000.00 USD | 16,450.00 USD | 14,620.00 USD | 33,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 3,250,000.00 USD | 3,250,000.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1153` | 2,370,000.00 USD | 2,370,000.00 USD | 31,350.00 USD | 23,630.00 USD | 59,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1154` | 3,710,000.00 USD | 3,710,000.00 USD | 243,190.00 USD | 26,970.00 USD | 195,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1155` | 2,490,000.00 USD | 2,490,000.00 USD | 38,430.00 USD | 27,080.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1157` | 2,540,000.00 USD | 2,540,000.00 USD | 33,550.00 USD | 9,850.00 USD | 7,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 4,020,000.00 USD | 4,020,000.00 USD | 188,950.00 USD | 25,290.00 USD | 98,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1159` | 2,590,000.00 USD | 2,590,000.00 USD | 22,990.00 USD | 12,000.00 USD | 17,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1160` | 4,310,000.00 USD | 4,310,000.00 USD | 139,350.00 USD | 32,830.00 USD | 109,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1161` | 2,620,000.00 USD | 2,620,000.00 USD | 23,670.00 USD | 0.00 USD | 5,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1163` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 9,380.00 USD | 17,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 4,590,000.00 USD | 4,590,000.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1165` | 2,660,000.00 USD | 2,660,000.00 USD | 4,990.00 USD | 5,320.00 USD | 1,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1166` | 4,810,000.00 USD | 4,810,000.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1167` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 7,220.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1169` | 2,680,000.00 USD | 2,680,000.00 USD | 5,480.00 USD | 2,440.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 5,030,000.00 USD | 5,030,000.00 USD | 82,770.00 USD | 26,150.00 USD | 112,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1171` | 2,700,000.00 USD | 2,700,000.00 USD | 13,800.00 USD | 0.00 USD | 4,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1172` | 5,160,000.00 USD | 5,160,000.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1173` | 2,720,000.00 USD | 2,720,000.00 USD | 9,320.00 USD | 5,440.00 USD | 4,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1175` | 2,760,000.00 USD | 2,760,000.00 USD | 9,530.00 USD | 9,020.00 USD | 19,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 5,330,000.00 USD | 5,330,000.00 USD | 72,770.00 USD | 17,930.00 USD | 81,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1177` | 2,800,000.00 USD | 2,800,000.00 USD | 14,360.00 USD | 8,560.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1178` | 5,500,000.00 USD | 5,500,000.00 USD | 89,510.00 USD | 23,660.00 USD | 55,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1179` | 2,820,000.00 USD | 2,820,000.00 USD | 10,640.00 USD | 4,760.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1181` | 2,860,000.00 USD | 2,860,000.00 USD | 14,160.00 USD | 6,410.00 USD | 15,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 5,590,000.00 USD | 5,590,000.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1183` | 2,870,000.00 USD | 2,870,000.00 USD | 8,760.00 USD | 677.63 USD | 4,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1184` | 5,650,000.00 USD | 5,650,000.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1185` | 2,890,000.00 USD | 2,890,000.00 USD | 4,390.00 USD | 5,850.00 USD | 6,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1187` | 2,900,000.00 USD | 2,900,000.00 USD | 2,150.00 USD | 3,330.00 USD | 9,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 5,730,000.00 USD | 5,730,000.00 USD | 5,620.00 USD | 17,120.00 USD | 54,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1189` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 2,120.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1190` | 5,870,000.00 USD | 5,870,000.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1191` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 1,810.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1193` | 2,920,000.00 USD | 2,920,000.00 USD | 4,720.00 USD | 1,040.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 5,950,000.00 USD | 5,950,000.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1195` | 2,940,000.00 USD | 2,940,000.00 USD | 9,550.00 USD | 1,470.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1196` | 6,010,000.00 USD | 6,010,000.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1197` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 1,040.00 USD | 93.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1199` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 431.42 USD | 3,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 6,100,000.00 USD | 6,100,000.00 USD | 9,100.00 USD | 13,190.00 USD | 67,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1201` | 2,960,000.00 USD | 2,960,000.00 USD | 3,250.00 USD | 1,390.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1202` | 6,300,000.00 USD | 6,300,000.00 USD | 138,430.00 USD | 21,430.00 USD | 32,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1203` | 2,960,000.00 USD | 2,960,000.00 USD | 5,670.00 USD | 413.94 USD | 2,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1205` | 2,970,000.00 USD | 2,970,000.00 USD | 2,250.00 USD | 1,670.00 USD | 741.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 6,630,000.00 USD | 6,630,000.00 USD | 132,960.00 USD | 72,910.00 USD | 130,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1207` | 2,980,000.00 USD | 2,980,000.00 USD | 5,540.00 USD | 524.23 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1208` | 6,770,000.00 USD | 6,770,000.00 USD | 39,480.00 USD | 25,720.00 USD | 66,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1209` | 2,990,000.00 USD | 2,990,000.00 USD | 2,820.00 USD | 3,290.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1211` | 3,000,000.00 USD | 3,000,000.00 USD | 4,800.00 USD | 2,950.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 6,980,000.00 USD | 6,980,000.00 USD | 72,500.00 USD | 25,920.00 USD | 111,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1213` | 3,020,000.00 USD | 3,020,000.00 USD | 5,870.00 USD | 1,720.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1214` | 7,100,000.00 USD | 7,100,000.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1215` | 3,030,000.00 USD | 3,030,000.00 USD | 1,650.00 USD | 0.00 USD | 5,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1217` | 3,030,000.00 USD | 3,030,000.00 USD | 1,090.00 USD | 624.33 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 7,140,000.00 USD | 7,140,000.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1219` | 3,050,000.00 USD | 3,050,000.00 USD | 2,320.00 USD | 718.82 USD | 10,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1220` | 7,260,000.00 USD | 7,260,000.00 USD | 45,700.00 USD | 10,970.00 USD | 54,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1221` | 3,060,000.00 USD | 3,060,000.00 USD | 7,970.00 USD | 2,940.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1223` | 3,070,000.00 USD | 3,070,000.00 USD | 2,660.00 USD | 1,410.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 7,420,000.00 USD | 7,420,000.00 USD | 76,930.00 USD | 36,110.00 USD | 50,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1225` | 3,070,000.00 USD | 3,070,000.00 USD | 1,840.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 721.08 USD | 1,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1226` | 7,510,000.00 USD | 7,510,000.00 USD | 54,940.00 USD | 32,070.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1227` | 3,070,000.00 USD | 3,070,000.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1229` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 403.62 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 7,710,000.00 USD | 7,710,000.00 USD | 81,840.00 USD | 38,040.00 USD | 79,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1230` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 789.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1232` | 7,880,000.00 USD | 7,880,000.00 USD | 67,800.00 USD | 41,730.00 USD | 63,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1235` | 7,920,000.00 USD | 7,920,000.00 USD | 15,040.00 USD | 5,390.00 USD | 17,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1235` | 9,170.00 USD | 10,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1238` | 7,940,000.00 USD | 7,940,000.00 USD | 8,310.00 USD | 3,610.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1241` | 7,950,000.00 USD | 7,950,000.00 USD | 11,380.00 USD | 1,380.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1244` | 8,000,000.00 USD | 8,000,000.00 USD | 26,540.00 USD | 8,130.00 USD | 14,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1247` | 8,040,000.00 USD | 8,040,000.00 USD | 7,900.00 USD | 18,280.00 USD | 17,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1250` | 8,070,000.00 USD | 8,070,000.00 USD | 8,540.00 USD | 7,270.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1253` | 8,090,000.00 USD | 8,090,000.00 USD | 6,550.00 USD | 0.00 USD | 16,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1256` | 8,120,000.00 USD | 8,120,000.00 USD | 11,990.00 USD | 18,000.00 USD | 220.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1259` | 8,130,000.00 USD | 8,130,000.00 USD | 5,870.00 USD | 1,190.00 USD | 151.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1262` | 8,130,000.00 USD | 8,130,000.00 USD | 4,270.00 USD | 0.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1265` | 8,140,000.00 USD | 8,140,000.00 USD | 2,710.00 USD | 0.00 USD | 7,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1268` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1271` | 8,150,000.00 USD | 8,150,000.00 USD | 5,940.00 USD | 0.00 USD | 30.15 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1274` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 0.00 USD | 12.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1277` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 0.00 USD | 31.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1280` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 6,390.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.0878` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 1,370.00 USD | 4,930.00 USD | 27,260.00 USD |
| `1D` | `0.0881` | 687,580.00 USD | 0.00 USD | 687,580.00 USD | 2,400.00 USD | 1,300.00 USD | 4,700.00 USD |
| `7D` | `0.0881` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 3,770.00 USD | 2,660.00 USD | 12,940.00 USD |
| `1D` | `0.0883` | 679,180.00 USD | 0.00 USD | 679,180.00 USD | 2,370.00 USD | 659.34 USD | 5,980.00 USD |
| `7D` | `0.0884` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 7,040.00 USD | 4,640.00 USD | 11,870.00 USD |
| `1D` | `0.0885` | 670,170.00 USD | 0.00 USD | 670,170.00 USD | 0.00 USD | 312.16 USD | 2,520.00 USD |
| `1D` | `0.0887` | 667,340.00 USD | 0.00 USD | 667,340.00 USD | 1,740.00 USD | 655.48 USD | 4,540.00 USD |
| `7D` | `0.0887` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD |
| `1D` | `0.0889` | 660,410.00 USD | 0.00 USD | 660,410.00 USD | 727.20 USD | 1,690.00 USD | 2,110.00 USD |
| `7D` | `0.0890` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 14,610.00 USD | 4,470.00 USD | 3,680.00 USD |
| `1D` | `0.0891` | 655,890.00 USD | 0.00 USD | 655,890.00 USD | 1,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0893` | 654,560.00 USD | 0.00 USD | 654,560.00 USD | 983.61 USD | 0.00 USD | 542.23 USD |
| `7D` | `0.0893` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD |
| `1D` | `0.0895` | 653,040.00 USD | 0.00 USD | 653,040.00 USD | 0.00 USD | 215.06 USD | 394.61 USD |
| `7D` | `0.0896` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 5,760.00 USD | 611.80 USD | 6,870.00 USD |
| `1D` | `0.0897` | 652,430.00 USD | 0.00 USD | 652,430.00 USD | 0.00 USD | 772.87 USD | 0.02 USD |
| `1D` | `0.0899` | 651,650.00 USD | 0.00 USD | 651,650.00 USD | 0.00 USD | 287.77 USD | 601.21 USD |
| `7D` | `0.0899` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 3,390.00 USD | 927.82 USD | 4,490.00 USD |
| `1D` | `0.0901` | 650,760.00 USD | 0.00 USD | 650,760.00 USD | 2,450.00 USD | 0.00 USD | 293.66 USD |
| `7D` | `0.0902` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 2,270.00 USD | 910.78 USD | 1,210.00 USD |
| `1D` | `0.0903` | 648,020.00 USD | 0.00 USD | 648,020.00 USD | 831.11 USD | 2,190.00 USD | 1,070.00 USD |
| `1D` | `0.0905` | 643,930.00 USD | 0.00 USD | 643,930.00 USD | 413.91 USD | 998.41 USD | 2,840.00 USD |
| `7D` | `0.0905` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 10,350.00 USD | 996.61 USD | 4,080.00 USD |
| `1D` | `0.0907` | 639,680.00 USD | 0.00 USD | 639,680.00 USD | 2,290.00 USD | 909.44 USD | 974.67 USD |
| `7D` | `0.0908` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD |
| `1D` | `0.0909` | 635,510.00 USD | 0.00 USD | 635,510.00 USD | 938.76 USD | 957.38 USD | 785.45 USD |
| `1D` | `0.0911` | 632,830.00 USD | 0.00 USD | 632,830.00 USD | 5,580.00 USD | 778.50 USD | 5.42 USD |
| `7D` | `0.0911` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD |
| `1D` | `0.0913` | 626,460.00 USD | 0.00 USD | 626,460.00 USD | 0.00 USD | 0.00 USD | 787.25 USD |
| `7D` | `0.0914` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 1,670.00 USD | 903.90 USD | 45.81 USD |
| `1D` | `0.0915` | 625,670.00 USD | 0.00 USD | 625,670.00 USD | 6,590.00 USD | 0.00 USD | 46.43 USD |
| `1D` | `0.0917` | 619,040.00 USD | 0.00 USD | 619,040.00 USD | 2,550.00 USD | 0.00 USD | 2.87 USD |
| `7D` | `0.0917` | 999,660.00 USD | 0.00 USD | 999,660.00 USD | 0.00 USD | 0.00 USD | 1,740.00 USD |
| `1D` | `0.0919` | 616,480.00 USD | 0.00 USD | 616,480.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0923` | 612,800.00 USD | 0.00 USD | 612,800.00 USD | 0.00 USD | 0.00 USD | 42.87 USD |
| `7D` | `0.0923` | 997,920.00 USD | 0.00 USD | 997,920.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `0.0925` | 612,750.00 USD | 0.00 USD | 612,750.00 USD | 3,270.00 USD | 1,660.00 USD | 6,360.00 USD |
| `7D` | `0.0926` | 996,460.00 USD | 0.00 USD | 996,460.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD |
| `7D` | `0.0932` | 986,480.00 USD | 0.00 USD | 986,480.00 USD | 0.00 USD | 0.00 USD | 12,240.00 USD |
| `1D` | `0.0933` | 601,470.00 USD | 0.00 USD | 601,470.00 USD | 0.00 USD | 0.00 USD | 6,860.00 USD |
| `7D` | `0.0935` | 974,250.00 USD | 0.00 USD | 974,250.00 USD | 0.00 USD | 1,320.00 USD | 6,490.00 USD |
| `1D` | `0.0937` | 594,610.00 USD | 0.00 USD | 594,610.00 USD | 0.00 USD | 0.00 USD | 64.09 USD |
| `7D` | `0.0938` | 966,440.00 USD | 0.00 USD | 966,440.00 USD | 0.00 USD | 0.00 USD | 8.57 USD |
| `1D` | `0.0939` | 594,540.00 USD | 0.00 USD | 594,540.00 USD | 0.00 USD | 0.00 USD | 76.92 USD |
| `7D` | `0.0941` | 966,430.00 USD | 0.00 USD | 966,430.00 USD | 2,050.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `0.0944` | 961,360.00 USD | 0.00 USD | 961,360.00 USD | 1,870.00 USD | 0.00 USD | 7,520.00 USD |
| `1D` | `0.0947` | 594,460.00 USD | 0.00 USD | 594,460.00 USD | 0.00 USD | 0.00 USD | 69.61 USD |
| `7D` | `0.0947` | 951,960.00 USD | 0.00 USD | 951,960.00 USD | 3,790.00 USD | 1,810.00 USD | 112.06 USD |
| `7D` | `0.0950` | 946,250.00 USD | 0.00 USD | 946,250.00 USD | 3,770.00 USD | 0.00 USD | 6,660.00 USD |
| `1D` | `0.0953` | 594,390.00 USD | 0.00 USD | 594,390.00 USD | 0.00 USD | 0.00 USD | 87.96 USD |
| `7D` | `0.0953` | 935,820.00 USD | 0.00 USD | 935,820.00 USD | 0.00 USD | 0.00 USD | 4.65 USD |
| `1D` | `0.0955` | 594,310.00 USD | 0.00 USD | 594,310.00 USD | 0.00 USD | 1,180.00 USD | 166.88 USD |
| `7D` | `0.0959` | 935,810.00 USD | 0.00 USD | 935,810.00 USD | 0.00 USD | 1,140.00 USD | 115.48 USD |
| `1D` | `0.0961` | 592,960.00 USD | 0.00 USD | 592,960.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0962` | 934,560.00 USD | 0.00 USD | 934,560.00 USD | 0.00 USD | 0.00 USD | 121.64 USD |
| `1D` | `0.0963` | 590,880.00 USD | 0.00 USD | 590,880.00 USD | 0.00 USD | 0.00 USD | 1.02 USD |
| `1D` | `0.0965` | 590,880.00 USD | 0.00 USD | 590,880.00 USD | 1,280.00 USD | 282.32 USD | 1,880.00 USD |
| `1D` | `0.0967` | 587,430.00 USD | 0.00 USD | 587,430.00 USD | 2,660.00 USD | 1,100.00 USD | 7,500.00 USD |
| `7D` | `0.0968` | 934,440.00 USD | 0.00 USD | 934,440.00 USD | 7,490.00 USD | 3,720.00 USD | 11,630.00 USD |
| `1D` | `0.0969` | 576,170.00 USD | 0.00 USD | 576,170.00 USD | 4,590.00 USD | 2,640.00 USD | 9,010.00 USD |
| `1D` | `0.0971` | 559,930.00 USD | 0.00 USD | 559,930.00 USD | 16,100.00 USD | 3,330.00 USD | 4,610.00 USD |
| `7D` | `0.0971` | 911,600.00 USD | 0.00 USD | 911,600.00 USD | 0.00 USD | 3,760.00 USD | 9,720.00 USD |
| `1D` | `0.0973` | 535,900.00 USD | 0.00 USD | 535,900.00 USD | 0.00 USD | 2,120.00 USD | 4,400.00 USD |
| `7D` | `0.0974` | 898,120.00 USD | 0.00 USD | 898,120.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD |
| `1D` | `0.0975` | 529,370.00 USD | 0.00 USD | 529,370.00 USD | 0.00 USD | 1,810.00 USD | 5,550.00 USD |
| `1D` | `0.0977` | 522,010.00 USD | 0.00 USD | 522,010.00 USD | 24,760.00 USD | 2,510.00 USD | 11,230.00 USD |
| `7D` | `0.0977` | 893,840.00 USD | 0.00 USD | 893,840.00 USD | 0.00 USD | 1,160.00 USD | 13,130.00 USD |
| `1D` | `0.0979` | 483,510.00 USD | 0.00 USD | 483,510.00 USD | 12,620.00 USD | 1,040.00 USD | 8.08 USD |
| `7D` | `0.0980` | 879,550.00 USD | 0.00 USD | 879,550.00 USD | 0.00 USD | 3,920.00 USD | 5,710.00 USD |
| `1D` | `0.0981` | 469,840.00 USD | 0.00 USD | 469,840.00 USD | 9,220.00 USD | 431.42 USD | 3,030.00 USD |
| `1D` | `0.0983` | 457,160.00 USD | 0.00 USD | 457,160.00 USD | 3,250.00 USD | 1,390.00 USD | 16,110.00 USD |
| `7D` | `0.0983` | 869,920.00 USD | 0.00 USD | 869,920.00 USD | 7,990.00 USD | 1,230.00 USD | 14,770.00 USD |
| `1D` | `0.0985` | 436,410.00 USD | 0.00 USD | 436,410.00 USD | 5,670.00 USD | 413.94 USD | 2,690.00 USD |
| `7D` | `0.0986` | 845,930.00 USD | 0.00 USD | 845,930.00 USD | 7,110.00 USD | 7,530.00 USD | 38,270.00 USD |
| `1D` | `0.0987` | 427,640.00 USD | 0.00 USD | 427,640.00 USD | 15,960.00 USD | 6,330.00 USD | 20,710.00 USD |
| `1D` | `0.0989` | 384,640.00 USD | 0.00 USD | 384,640.00 USD | 2,820.00 USD | 3,290.00 USD | 2,310.00 USD |
| `7D` | `0.0989` | 793,020.00 USD | 0.00 USD | 793,020.00 USD | 17,640.00 USD | 6,190.00 USD | 53,200.00 USD |
| `1D` | `0.0991` | 376,220.00 USD | 0.00 USD | 376,220.00 USD | 32,710.00 USD | 2,950.00 USD | 3,200.00 USD |
| `7D` | `0.0992` | 715,980.00 USD | 0.00 USD | 715,980.00 USD | 27,140.00 USD | 11,490.00 USD | 28,490.00 USD |
| `1D` | `0.0993` | 337,360.00 USD | 0.00 USD | 337,360.00 USD | 3,080.00 USD | 1,720.00 USD | 11,460.00 USD |
| `1D` | `0.0995` | 321,090.00 USD | 0.00 USD | 321,090.00 USD | 2,740.00 USD | 624.33 USD | 11,480.00 USD |
| `7D` | `0.0995` | 648,860.00 USD | 0.00 USD | 648,860.00 USD | 24,220.00 USD | 15,150.00 USD | 56,550.00 USD |
| `1D` | `0.0997` | 306,240.00 USD | 0.00 USD | 306,240.00 USD | 35,260.00 USD | 718.82 USD | 27,200.00 USD |
| `7D` | `0.0998` | 552,940.00 USD | 0.00 USD | 552,940.00 USD | 28,450.00 USD | 6,400.00 USD | 49,360.00 USD |
| `1D` | `0.0999` | 243,060.00 USD | 0.00 USD | 243,060.00 USD | 37,910.00 USD | 2,940.00 USD | 23,880.00 USD |
| `1D` | `0.1001` | 178,330.00 USD | 0.00 USD | 178,330.00 USD | 21,100.00 USD | 1,410.00 USD | 4,200.00 USD |
| `7D` | `0.1001` | 468,720.00 USD | 0.00 USD | 468,720.00 USD | 36,110.00 USD | 8,650.00 USD | 13,120.00 USD |
| `1D` | `0.1003` | 151,630.00 USD | 0.00 USD | 151,630.00 USD | 0.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1004` | 410,840.00 USD | 0.00 USD | 410,840.00 USD | 22,470.00 USD | 16,470.00 USD | 23,430.00 USD |
| `1D` | `0.1005` | 151,070.00 USD | 0.00 USD | 151,070.00 USD | 1,970.00 USD | 403.62 USD | 13,950.00 USD |
| `1D` | `0.1007` | 134,750.00 USD | 0.00 USD | 134,750.00 USD | 0.00 USD | 8,710.00 USD | 32,600.00 USD |
| `7D` | `0.1007` | 348,470.00 USD | 0.00 USD | 348,470.00 USD | 20,870.00 USD | 3,870.00 USD | 54,750.00 USD |
| `1D` | `0.1009` | 93,450.00 USD | 0.00 USD | 93,450.00 USD | 0.00 USD | 2,750.00 USD | 0.00 USD |
| `7D` | `0.1010` | 268,970.00 USD | 0.00 USD | 268,970.00 USD | 17,340.00 USD | 6,580.00 USD | 6,630.00 USD |
| `1D` | `0.1011` | 90,700.00 USD | 0.00 USD | 90,700.00 USD | 0.00 USD | 575.54 USD | 3,390.00 USD |
| `1D` | `0.1013` | 86,730.00 USD | 0.00 USD | 86,730.00 USD | 0.00 USD | 800.79 USD | 587.32 USD |
| `7D` | `0.1013` | 238,420.00 USD | 0.00 USD | 238,420.00 USD | 15,270.00 USD | 5,230.00 USD | 56,480.00 USD |
| `1D` | `0.1015` | 85,340.00 USD | 0.00 USD | 85,340.00 USD | 0.00 USD | 1,830.00 USD | 1,660.00 USD |
| `7D` | `0.1016` | 161,440.00 USD | 0.00 USD | 161,440.00 USD | 15,440.00 USD | 5,490.00 USD | 5,510.00 USD |
| `1D` | `0.1017` | 81,850.00 USD | 0.00 USD | 81,850.00 USD | 0.00 USD | 3,440.00 USD | 34,320.00 USD |
| `1D` | `0.1019` | 44,090.00 USD | 0.00 USD | 44,090.00 USD | 0.00 USD | 6,380.00 USD | 0.00 USD |
| `7D` | `0.1019` | 134,990.00 USD | 0.00 USD | 134,990.00 USD | 12,100.00 USD | 5,790.00 USD | 14,260.00 USD |
| `1D` | `0.1021` | 37,710.00 USD | 0.00 USD | 37,710.00 USD | 15,980.00 USD | 1,320.00 USD | 14,190.00 USD |
| `7D` | `0.1022` | 102,840.00 USD | 0.00 USD | 102,840.00 USD | 11,930.00 USD | 8,250.00 USD | 12,650.00 USD |
| `7D` | `0.1025` | 70,000.00 USD | 0.00 USD | 70,000.00 USD | 1,550.00 USD | 0.00 USD | 8,490.00 USD |
| `7D` | `0.1028` | 59,960.00 USD | 0.00 USD | 59,960.00 USD | 3,800.00 USD | 4,390.00 USD | 0.00 USD |
| `1D` | `0.1029` | 6,230.00 USD | 0.00 USD | 6,230.00 USD | 0.00 USD | 0.00 USD | 6,230.00 USD |
| `1D` | `0.1030` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1031` | 46,790.00 USD | 46,790.00 USD | 0.00 USD | 27,910.00 USD | 0.00 USD | 18,880.00 USD |
| `7D` | `0.1031` | 51,770.00 USD | 0.00 USD | 51,770.00 USD | 19,560.00 USD | 6,260.00 USD | 0.00 USD |
| `1D` | `0.1033` | 68,650.00 USD | 68,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,860.00 USD |
| `7D` | `0.1034` | 25,950.00 USD | 0.00 USD | 25,950.00 USD | 18,920.00 USD | 7,030.00 USD | 0.00 USD |
| `1D` | `0.1035` | 78,360.00 USD | 78,360.00 USD | 0.00 USD | 4,780.00 USD | 4,880.00 USD | 54.66 USD |
| `7D` | `0.1035` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1037` | 127,630.00 USD | 127,630.00 USD | 0.00 USD | 37,310.00 USD | 11,960.00 USD | 0.00 USD |
| `7D` | `0.1037` | 7,720.00 USD | 7,720.00 USD | 0.00 USD | 2,710.00 USD | 5,010.00 USD | 0.00 USD |
| `1D` | `0.1039` | 133,080.00 USD | 133,080.00 USD | 0.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD |
| `7D` | `0.1040` | 23,960.00 USD | 23,960.00 USD | 0.00 USD | 5,940.00 USD | 10,300.00 USD | 0.00 USD |
| `1D` | `0.1041` | 145,900.00 USD | 145,900.00 USD | 0.00 USD | 0.00 USD | 12,830.00 USD | 0.00 USD |
| `1D` | `0.1043` | 151,550.00 USD | 151,550.00 USD | 0.00 USD | 0.00 USD | 5,650.00 USD | 0.00 USD |
| `7D` | `0.1043` | 45,910.00 USD | 45,910.00 USD | 0.00 USD | 15,960.00 USD | 5,980.00 USD | 0.00 USD |
| `1D` | `0.1045` | 161,340.00 USD | 161,340.00 USD | 0.00 USD | 0.00 USD | 4,840.00 USD | 4,950.00 USD |
| `7D` | `0.1046` | 70,400.00 USD | 70,400.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD | 14,680.00 USD |
| `1D` | `0.1047` | 200,310.00 USD | 200,310.00 USD | 0.00 USD | 15,000.00 USD | 3,400.00 USD | 20,560.00 USD |
| `1D` | `0.1049` | 291,030.00 USD | 291,030.00 USD | 0.00 USD | 37,390.00 USD | 10,710.00 USD | 42,630.00 USD |
| `7D` | `0.1049` | 194,820.00 USD | 194,820.00 USD | 0.00 USD | 34,790.00 USD | 6,530.00 USD | 83,110.00 USD |
| `1D` | `0.1051` | 354,380.00 USD | 354,380.00 USD | 0.00 USD | 30,370.00 USD | 8,750.00 USD | 24,230.00 USD |
| `7D` | `0.1052` | 372,590.00 USD | 372,590.00 USD | 0.00 USD | 28,200.00 USD | 24,160.00 USD | 125,400.00 USD |
| `1D` | `0.1053` | 449,190.00 USD | 449,190.00 USD | 0.00 USD | 35,030.00 USD | 8,930.00 USD | 50,850.00 USD |
| `1D` | `0.1055` | 578,000.00 USD | 578,000.00 USD | 0.00 USD | 43,960.00 USD | 25,140.00 USD | 59,710.00 USD |
| `7D` | `0.1055` | 751,320.00 USD | 751,320.00 USD | 0.00 USD | 122,840.00 USD | 44,430.00 USD | 211,460.00 USD |
| `1D` | `0.1057` | 670,550.00 USD | 670,550.00 USD | 0.00 USD | 27,300.00 USD | 15,170.00 USD | 50,080.00 USD |
| `7D` | `0.1058` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 105,620.00 USD | 53,680.00 USD | 189,110.00 USD |
| `1D` | `0.1059` | 806,530.00 USD | 806,530.00 USD | 0.00 USD | 39,020.00 USD | 0.00 USD | 96,960.00 USD |
| `1D` | `0.1061` | 892,440.00 USD | 892,440.00 USD | 0.00 USD | 26,970.00 USD | 0.00 USD | 58,940.00 USD |
| `7D` | `0.1061` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 75,540.00 USD | 72,260.00 USD | 102,650.00 USD |
| `1D` | `0.1063` | 980,690.00 USD | 980,690.00 USD | 0.00 USD | 25,200.00 USD | 0.00 USD | 63,060.00 USD |
| `7D` | `0.1064` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 52,580.00 USD | 192,520.00 USD |
| `1D` | `0.1065` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25,740.00 USD |
| `1D` | `0.1067` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33,160.00 USD |
| `7D` | `0.1067` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 51,740.00 USD | 133,410.00 USD |
| `1D` | `0.1069` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 8,170.00 USD | 4,140.00 USD | 58,550.00 USD |
| `7D` | `0.1070` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 57,770.00 USD | 134,670.00 USD |
| `1D` | `0.1071` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 3,140.00 USD | 16,220.00 USD |
| `1D` | `0.1073` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 218.01 USD |
| `7D` | `0.1073` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 17,700.00 USD | 0.00 USD |
| `1D` | `0.1075` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 104.34 USD |
| `7D` | `0.1076` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,500.00 USD |
| `1D` | `0.1077` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 93.46 USD |
| `1D` | `0.1079` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,190.00 USD |
| `7D` | `0.1079` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 79.36 USD |
| `7D` | `0.1082` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 89.24 USD |
| `1D` | `0.1083` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 7,990.00 USD | 5,910.00 USD | 7,180.00 USD |
| `1D` | `0.1085` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65,020.00 USD |
| `7D` | `0.1085` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1087` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 28,490.00 USD | 2,240.00 USD | 44,670.00 USD |
| `7D` | `0.1088` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 5,290.00 USD | 0.00 USD | 113.96 USD |
| `1D` | `0.1089` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 39,160.00 USD | 0.00 USD | 87.96 USD |
| `1D` | `0.1091` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 33,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1091` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD |
| `1D` | `0.1093` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 15,480.00 USD | 0.00 USD | 192.45 USD |
| `7D` | `0.1094` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD |
| `1D` | `0.1095` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 21,520.00 USD |
| `1D` | `0.1097` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 7,260.00 USD | 1,970.00 USD | 22,790.00 USD |
| `7D` | `0.1097` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1099` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 6,130.00 USD | 1,940.00 USD | 0.00 USD |
| `7D` | `0.1100` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 21,840.00 USD |
| `1D` | `0.1101` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 4,310.00 USD | 2,820.00 USD | 4,290.00 USD |
| `1D` | `0.1103` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 3,540.00 USD | 5,640.00 USD | 0.00 USD |
| `7D` | `0.1103` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1105` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 3,380.00 USD | 4,740.00 USD | 10,700.00 USD |
| `7D` | `0.1106` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 22,880.00 USD | 16,040.00 USD |
| `1D` | `0.1107` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 3,110.00 USD | 12,720.00 USD | 35,750.00 USD |
| `1D` | `0.1109` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 2,110.00 USD | 1,120.00 USD | 0.00 USD |
| `7D` | `0.1109` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD |
| `1D` | `0.1111` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 5,200.00 USD | 0.00 USD | 96.09 USD |
| `7D` | `0.1112` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD |
| `1D` | `0.1113` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 21,390.00 USD | 5,210.00 USD | 39,070.00 USD |
| `1D` | `0.1115` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1117` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 2,060.00 USD | 25,630.00 USD | 34,770.00 USD |
| `7D` | `0.1118` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD |
| `1D` | `0.1119` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 33,110.00 USD | 6,980.00 USD | 36,740.00 USD |
| `1D` | `0.1121` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 20,000.00 USD | 12,060.00 USD | 12,320.00 USD |
| `7D` | `0.1121` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 17,760.00 USD | 0.00 USD | 32,100.00 USD |
| `1D` | `0.1123` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 40,400.00 USD | 1,780.00 USD | 5,930.00 USD |
| `7D` | `0.1124` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD |
| `1D` | `0.1125` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 11,130.00 USD | 13,240.00 USD | 7,950.00 USD |
| `1D` | `0.1127` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 1,250.00 USD | 19,520.00 USD |
| `7D` | `0.1127` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD |
| `1D` | `0.1129` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 8,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1130` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,170.00 USD |
| `1D` | `0.1131` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 20,830.00 USD | 8,010.00 USD | 17,980.00 USD |
| `1D` | `0.1133` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 6,530.00 USD | 22,520.00 USD | 23,470.00 USD |
| `7D` | `0.1133` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD |
| `1D` | `0.1135` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 4,040.00 USD | 3,670.00 USD | 4,090.00 USD |
| `7D` | `0.1136` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD |
| `1D` | `0.1137` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 856.93 USD | 40.44 USD |
| `1D` | `0.1139` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,270.00 USD |
| `7D` | `0.1139` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD |
| `1D` | `0.1141` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 13,860.00 USD | 2,800.00 USD | 20,340.00 USD |
| `7D` | `0.1142` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD |
| `1D` | `0.1143` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 20,300.00 USD | 27,990.00 USD | 11,820.00 USD |
| `1D` | `0.1145` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 13,430.00 USD | 11,690.00 USD | 38,100.00 USD |
| `7D` | `0.1145` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD |
| `1D` | `0.1147` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 10,640.00 USD | 10,080.00 USD | 30,680.00 USD |
| `7D` | `0.1148` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 176,010.00 USD |
| `1D` | `0.1149` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 35,170.00 USD | 624.71 USD | 31,820.00 USD |
| `1D` | `0.1151` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 16,450.00 USD | 14,620.00 USD | 33,180.00 USD |
| `7D` | `0.1151` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD |
| `1D` | `0.1153` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 31,350.00 USD | 23,630.00 USD | 59,030.00 USD |
| `7D` | `0.1154` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 243,190.00 USD | 26,970.00 USD | 195,390.00 USD |
| `1D` | `0.1155` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 38,430.00 USD | 27,080.00 USD | 54,030.00 USD |
| `1D` | `0.1157` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 33,550.00 USD | 9,850.00 USD | 7,870.00 USD |
| `7D` | `0.1157` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 188,950.00 USD | 25,290.00 USD | 98,310.00 USD |
| `1D` | `0.1159` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 22,990.00 USD | 12,000.00 USD | 17,950.00 USD |
| `7D` | `0.1160` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 139,350.00 USD | 32,830.00 USD | 109,320.00 USD |
| `1D` | `0.1161` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 23,670.00 USD | 0.00 USD | 5,160.00 USD |
| `1D` | `0.1163` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 9,380.00 USD | 17,460.00 USD |
| `7D` | `0.1163` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD |
| `1D` | `0.1165` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 4,990.00 USD | 5,320.00 USD | 1,840.00 USD |
| `7D` | `0.1166` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD |
| `1D` | `0.1167` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 7,220.00 USD | 6,170.00 USD |
| `1D` | `0.1169` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 5,480.00 USD | 2,440.00 USD | 2,290.00 USD |
| `7D` | `0.1169` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 82,770.00 USD | 26,150.00 USD | 112,810.00 USD |
| `1D` | `0.1171` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 13,800.00 USD | 0.00 USD | 4,510.00 USD |
| `7D` | `0.1172` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD |
| `1D` | `0.1173` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 2,840.00 USD | 5,440.00 USD | 4,840.00 USD |
| `1D` | `0.1175` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 9,530.00 USD | 9,020.00 USD | 19,930.00 USD |
| `7D` | `0.1175` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 72,770.00 USD | 17,930.00 USD | 81,630.00 USD |
| `1D` | `0.1177` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 14,360.00 USD | 8,560.00 USD | 16,650.00 USD |
| `7D` | `0.1178` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 89,510.00 USD | 23,660.00 USD | 55,770.00 USD |
| `1D` | `0.1179` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 10,640.00 USD | 4,760.00 USD | 5,770.00 USD |
| `1D` | `0.1181` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 14,160.00 USD | 6,410.00 USD | 15,670.00 USD |
| `7D` | `0.1181` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD |
| `1D` | `0.1183` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 8,760.00 USD | 677.63 USD | 4,580.00 USD |
| `7D` | `0.1184` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD |
| `1D` | `0.1185` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 4,390.00 USD | 5,850.00 USD | 6,770.00 USD |
| `1D` | `0.1187` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 2,150.00 USD | 3,330.00 USD | 9,840.00 USD |
| `7D` | `0.1187` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 5,620.00 USD | 17,120.00 USD | 54,960.00 USD |
| `1D` | `0.1189` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 2,120.00 USD | 4,350.00 USD |
| `7D` | `0.1190` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD |
| `1D` | `0.1191` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 1,810.00 USD | 5,650.00 USD |
| `1D` | `0.1193` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 4,720.00 USD | 1,040.00 USD | 1,990.00 USD |
| `7D` | `0.1193` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD |
| `1D` | `0.1195` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 6,310.00 USD | 1,470.00 USD | 2,780.00 USD |
| `7D` | `0.1196` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD |
| `1D` | `0.1197` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 1,040.00 USD | 93.72 USD |
| `1D` | `0.1199` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 431.42 USD | 3,050.00 USD |
| `7D` | `0.1199` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 9,100.00 USD | 13,190.00 USD | 67,980.00 USD |
| `1D` | `0.1201` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 3,250.00 USD | 1,390.00 USD | 9,680.00 USD |
| `7D` | `0.1202` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 138,430.00 USD | 21,430.00 USD | 32,790.00 USD |
| `1D` | `0.1203` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 5,670.00 USD | 413.94 USD | 2,710.00 USD |
| `1D` | `0.1205` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 2,250.00 USD | 1,670.00 USD | 741.32 USD |
| `7D` | `0.1205` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 132,960.00 USD | 72,910.00 USD | 130,900.00 USD |
| `1D` | `0.1207` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 5,540.00 USD | 524.23 USD | 4,100.00 USD |
| `7D` | `0.1208` | 6,770,000.00 USD | 6,770,000.00 USD | 0.00 USD | 39,480.00 USD | 25,720.00 USD | 66,520.00 USD |
| `1D` | `0.1209` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 2,820.00 USD | 3,290.00 USD | 2,240.00 USD |
| `1D` | `0.1211` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 4,800.00 USD | 2,950.00 USD | 3,240.00 USD |
| `7D` | `0.1211` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 72,500.00 USD | 25,920.00 USD | 111,160.00 USD |
| `1D` | `0.1213` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 5,870.00 USD | 1,720.00 USD | 11,460.00 USD |
| `7D` | `0.1214` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD |
| `1D` | `0.1215` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD | 5,440.00 USD |
| `1D` | `0.1217` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 1,090.00 USD | 624.33 USD | 6,070.00 USD |
| `7D` | `0.1217` | 7,150,000.00 USD | 7,150,000.00 USD | 0.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD |
| `1D` | `0.1219` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 2,320.00 USD | 718.82 USD | 10,060.00 USD |
| `7D` | `0.1220` | 7,260,000.00 USD | 7,260,000.00 USD | 0.00 USD | 45,700.00 USD | 10,970.00 USD | 54,700.00 USD |
| `1D` | `0.1221` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 7,970.00 USD | 2,940.00 USD | 3,650.00 USD |
| `1D` | `0.1223` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 2,660.00 USD | 1,410.00 USD | 4,210.00 USD |
| `7D` | `0.1223` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 76,930.00 USD | 36,110.00 USD | 50,790.00 USD |
| `1D` | `0.1225` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 1,840.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1226` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 54,940.00 USD | 32,070.00 USD | 5,210.00 USD |
| `1D` | `0.1227` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1229` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 403.62 USD | 1,080.00 USD |
| `7D` | `0.1229` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 81,840.00 USD | 38,040.00 USD | 79,050.00 USD |
| `1D` | `0.1230` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 789.22 USD |
| `7D` | `0.1232` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 67,800.00 USD | 37,460.00 USD | 63,720.00 USD |
| `7D` | `0.1235` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 15,040.00 USD | 5,390.00 USD | 17,120.00 USD |
| `7D` | `0.1238` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 8,310.00 USD | 3,610.00 USD | 3,100.00 USD |
| `7D` | `0.1241` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 11,380.00 USD | 1,380.00 USD | 7,090.00 USD |
| `7D` | `0.1244` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 26,540.00 USD | 8,130.00 USD | 9,660.00 USD |
| `7D` | `0.1247` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 7,900.00 USD | 18,280.00 USD | 17,680.00 USD |
| `7D` | `0.1250` | 8,060,000.00 USD | 8,060,000.00 USD | 0.00 USD | 8,540.00 USD | 7,270.00 USD | 5,780.00 USD |
| `7D` | `0.1253` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 6,550.00 USD | 0.00 USD | 16,470.00 USD |
| `7D` | `0.1256` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 11,990.00 USD | 15,870.00 USD | 220.44 USD |
| `7D` | `0.1259` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 5,870.00 USD | 1,190.00 USD | 151.34 USD |
| `7D` | `0.1262` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | 3,530.00 USD |
| `7D` | `0.1265` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 2,710.00 USD | 0.00 USD | 7,350.00 USD |
| `7D` | `0.1268` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD |
| `7D` | `0.1271` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 5,940.00 USD | 0.00 USD | 30.15 USD |
| `7D` | `0.1274` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12.00 USD |
| `7D` | `0.1277` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31.66 USD |
| `7D` | `0.1280` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,390.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `65.29M` | Total OI Tokens: `635,586,350.0 OP`
  * 1h OI Change: `-7.84%` | 4h OI Change: `-12.89%` | 24h OI Change: `-15.86%`
  * Exchange Breakdown: Binance=`14.92M` | Bybit=`13.05M` | OKX=`3.60M` | Hyperliquid=`3.36M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-2.04K` | Last 24h: `270.64` | Last 3d: `-2.23K` | Last 7d: `-15.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0182%` | **USDT OKX** | `0.0032%` |
| **USDT Bybit** | `0.0036%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0167%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0075%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `53.75%` | `46.25%` | `1.16` | 4,650,000.00 USD |
| `15M` | `Binance` | `48.95%` | `51.05%` | `0.96` | 2,180,000.00 USD |
| `15M` | `OKX` | `55.01%` | `44.99%` | `1.22` | 686,350.00 USD |
| `15M` | `Bybit` | `58.84%` | `41.16%` | `1.43` | 665,940.00 USD |
| `15M` | `KuCoin` | `64.8%` | `35.2%` | `1.84` | 174,640.00 USD |
| `15M` | `Gate` | `74.87%` | `25.13%` | `2.98` | 122,920.00 USD |
| `15M` | `Bitget` | `59.94%` | `40.06%` | `1.50` | 138,800.00 USD |
| `15M` | `BingX` | `74.48%` | `25.52%` | `2.92` | 135,330.00 USD |
| `15M` | `MEXC` | `55.06%` | `44.94%` | `1.23` | 153,530.00 USD |
| `15M` | `Bitunix` | `58.3%` | `41.7%` | `1.40` | 88,840.00 USD |
| `15M` | `Hyperliquid` | `53.56%` | `46.44%` | `1.15` | 56,510.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.28%` | `53.72%` | `0.86` | 68,620.00 USD |
| `15M` | `Crypto.com` | `0.23%` | `99.77%` | `0.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `95.82%` | `4.18%` | `22.92` | 136,840.00 USD |
| `15M` | `HTX` | `29.44%` | `70.56%` | `0.42` | 206.69 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `96.29%` | `3.71%` | `25.95` | 29,070.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 7,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `28.39%` | `71.61%` | `0.40` | 17,830.00 USD |
| `15M` | `Whale Positions` | `48.95%` | `51.05%` | `0.96` | 2,180,000.00 USD |
| `15M` | `Global Accounts` | `53.75%` | `46.25%` | `1.16` | 4,650,000.00 USD |
| `1H` | `OP` | `43.89%` | `56.11%` | `0.78` | 48,870,000.00 USD |
| `1H` | `Binance` | `43.32%` | `56.68%` | `0.76` | 20,840,000.00 USD |
| `1H` | `OKX` | `48.91%` | `51.09%` | `0.96` | 6,460,000.00 USD |
| `1H` | `Bybit` | `46.68%` | `53.32%` | `0.88` | 8,640,000.00 USD |
| `1H` | `KuCoin` | `47.46%` | `52.54%` | `0.90` | 979,180.00 USD |
| `1H` | `Gate` | `46.33%` | `53.67%` | `0.86` | 1,030,000.00 USD |
| `1H` | `Bitget` | `45.49%` | `54.51%` | `0.83` | 2,160,000.00 USD |
| `1H` | `BingX` | `22.6%` | `77.4%` | `0.29` | 2,650,000.00 USD |
| `1H` | `MEXC` | `36.78%` | `63.22%` | `0.58` | 2,230,000.00 USD |
| `1H` | `Bitunix` | `46.38%` | `53.62%` | `0.86` | 777,540.00 USD |
| `1H` | `Hyperliquid` | `51.41%` | `48.59%` | `1.06` | 1,250,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `40.48%` | `59.52%` | `0.68` | 309,040.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `49.73%` | `50.27%` | `0.99` | 1,140,000.00 USD |
| `1H` | `HTX` | `55.15%` | `44.85%` | `1.23` | 72,310.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `51.91%` | `48.09%` | `1.08` | 120,900.00 USD |
| `1H` | `Aster` | `55.61%` | `44.39%` | `1.25` | 153,810.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `12.26%` | `87.74%` | `0.14` | 60,790.00 USD |
| `1H` | `Whale Positions` | `43.32%` | `56.68%` | `0.76` | 20,840,000.00 USD |
| `1H` | `Global Accounts` | `43.89%` | `56.11%` | `0.78` | 48,870,000.00 USD |
| `4H` | `OP` | `47.12%` | `52.88%` | `0.89` | 77,170,000.00 USD |
| `4H` | `Binance` | `46.19%` | `53.81%` | `0.86` | 31,160,000.00 USD |
| `4H` | `OKX` | `45.86%` | `54.14%` | `0.85` | 9,150,000.00 USD |
| `4H` | `Bybit` | `45.55%` | `54.45%` | `0.84` | 11,730,000.00 USD |
| `4H` | `KuCoin` | `47.77%` | `52.23%` | `0.91` | 2,420,000.00 USD |
| `4H` | `Gate` | `54.42%` | `45.58%` | `1.19` | 1,650,000.00 USD |
| `4H` | `Bitget` | `49.81%` | `50.19%` | `0.99` | 3,050,000.00 USD |
| `4H` | `BingX` | `47.96%` | `52.04%` | `0.92` | 6,530,000.00 USD |
| `4H` | `MEXC` | `45.93%` | `54.07%` | `0.85` | 4,420,000.00 USD |
| `4H` | `Bitunix` | `47.19%` | `52.81%` | `0.89` | 1,230,000.00 USD |
| `4H` | `Hyperliquid` | `37.54%` | `62.46%` | `0.60` | 1,670,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.31%` | `51.69%` | `0.93` | 1,360,000.00 USD |
| `4H` | `Crypto.com` | `22.51%` | `77.49%` | `0.29` | 0.00 USD |
| `4H` | `WhiteBIT` | `87.77%` | `12.23%` | `7.18` | 2,040,000.00 USD |
| `4H` | `HTX` | `48.05%` | `51.95%` | `0.92` | 75,940.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `58.38%` | `41.62%` | `1.40` | 430,890.00 USD |
| `4H` | `Aster` | `32.62%` | `67.38%` | `0.48` | 172,120.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.81%` | `49.19%` | `1.03` | 74,650.00 USD |
| `4H` | `Whale Positions` | `46.19%` | `53.81%` | `0.86` | 31,160,000.00 USD |
| `4H` | `Global Accounts` | `47.12%` | `52.88%` | `0.89` | 77,170,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1097` | `0.1098` | `0.1097` | `0.1101` | `0.1096` | 225,346.74 USD | 116,304.67 USD | 109,042.07 USD | 7,262.60 USD | `+3.22%` | `6B / 4S` |
| `5:00 UTC` | `0.1098` | `0.1100` | `0.1098` | `0.1102` | `0.1096` | 199,782.25 USD | 121,152.98 USD | 78,629.27 USD | 42,523.71 USD | `+21.29%` | `24B / 5S` |
| `0:00 UTC` | `0.1103` | `0.1104` | `0.1103` | `0.1106` | `0.1100` | 230,285.46 USD | 143,965.28 USD | 86,320.18 USD | 57,645.10 USD | `+25.03%` | `14B / 4S` |
| `5:00 UTC` | `0.1102` | `0.1102` | `0.1102` | `0.1105` | `0.1099` | 215,356.47 USD | 112,661.20 USD | 102,695.27 USD | 9,965.93 USD | `+4.63%` | `7B / 11S` |
| `0:00 UTC` | `0.1077` | `0.1082` | `0.1077` | `0.1102` | `0.1070` | 2,425,114.31 USD | 1,046,280.57 USD | 1,378,833.74 USD | -332,553.17 USD | `-13.71%` | `8B / 30S` |
| `5:00 UTC` | `0.1084` | `0.1083` | `0.1084` | `0.1087` | `0.1080` | 527,563.25 USD | 310,298.99 USD | 217,264.26 USD | 93,034.72 USD | `+17.63%` | `19B / 3S` |
| `0:00 UTC` | `0.1063` | `0.1047` | `0.1063` | `0.1088` | `0.1013` | 5,548,996.22 USD | 2,272,459.88 USD | 3,276,536.35 USD | -1,004,076.47 USD | `-18.09%` | `5B / 37S` |
| `5:00 UTC` | `0.1014` | `0.1013` | `0.1014` | `0.1029` | `0.0990` | 5,717,098.88 USD | 2,672,854.06 USD | 3,044,244.81 USD | -371,390.75 USD | `-6.50%` | `7B / 23S` |
| `0:00 UTC` | `0.1025` | `0.1020` | `0.1025` | `0.1033` | `0.1007` | 1,857,629.60 USD | 946,076.57 USD | 911,553.03 USD | 34,523.54 USD | `+1.86%` | `19B / 6S` |
| `5:00 UTC` | `0.1043` | `0.1037` | `0.1043` | `0.1044` | `0.1027` | 840,661.03 USD | 376,924.88 USD | 463,736.15 USD | -86,811.27 USD | `-10.33%` | `39B / 27S` |

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
| `5m` | 17,370.00 USD | -1,440.00 USD | **`ACCUMULATION`** |
| `15m` | 108,350.00 USD | 100,060.00 USD | **`ACCUMULATION`** |
| `30m` | 269,580.00 USD | -73,780.00 USD | **`ACCUMULATION`** |
| `1h` | -219,330.00 USD | -2,580,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -210,090.00 USD | -2,810,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -231,550.00 USD | -2,950,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -242,970.00 USD | -3,200,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -41,350.00 USD | -2,460,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 30,670.00 USD | -2,510,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -102,060.00 USD | -4,930,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -290,460.00 USD | -12,630,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,690,000.00 USD | -81,470,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+17.37K` | 15m=`+108.35K` | 1h=`-219.33K` | 24h=`-102.06K`
* Futures Capital Netflows: 5m=`-1.44K` | 15m=`+100.06K` | 1h=`-2.58M` | 24h=`-4.93M`
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
  * `2026-10-30 02:15:01 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:51:01 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:51:01 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:50:01 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:50:01 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:01 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:01 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:01 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:01 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:01 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
