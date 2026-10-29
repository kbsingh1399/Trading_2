# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 04:50:10 IST` (`2026-10-29 23:20:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1013` | `0.1018` | `0.1011` | `0.1017` | `2,220,842` | 225,271.68 USD | 27,459.42 USD | `+12.19%` | -2,534,266.25 USD | `+0.37` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1017` | `0.1023` | `0.1016` | `0.1021` | `2,114,434` | 215,488.47 USD | 10,211.22 USD | `+4.74%` | -2,524,055.03 USD | `-0.09` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.1021` | `0.1021` | `0.1019` | `0.1019` | `362,566` | 36,987.31 USD | -4,722.51 USD | `-12.77%` | -2,528,777.54 USD | `-0.45` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1022` | `0.1023` | `0.1012` | `0.1017` | `6,323,225` | 643,620.60 USD | 111,613.45 USD | `+17.34%` | -2,549,127.93 USD | `+0.71` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1017` | `0.1023` | `0.1010` | `0.1021` | `6,687,688` | 679,431.20 USD | 36,275.90 USD | `+5.34%` | -2,512,852.03 USD | `+0.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1021` | `0.1021` | `0.1019` | `0.1019` | `357,104` | 36,430.66 USD | -5,253.65 USD | `-14.42%` | -2,518,105.68 USD | `+0.23` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1012` | `0.1044` | `0.1007` | `0.1018` | `43,149,466` | 4,433,523.07 USD | -89,220.85 USD | `-2.01%` | -2,816,174.98 USD | `+0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1018` | `0.1029` | `0.1003` | `0.1017` | `28,588,718` | 2,912,169.52 USD | 245,799.32 USD | `+8.44%` | -2,570,375.66 USD | `+0.82` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1017` | `0.1023` | `0.1010` | `0.1020` | `7,082,962` | 719,754.65 USD | 33,763.08 USD | `+4.69%` | -2,536,612.59 USD | `+0.22` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -935,828.18 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | -1,111,968.46 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1020` | `215,509,145` | 22,283,025.32 USD | -1,425,811.20 USD | `-6.40%` | -2,537,779.67 USD | `-1.32` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1085` | `0.1106` | `0.1071` | `0.1076` | `47,048,931` | 5,111,570.05 USD | 108,567.99 USD | `+2.12%` | -1,419,806.61 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,277,083.78 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -935,828.18 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | -1,111,968.46 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1020` | `215,509,145` | 22,283,025.32 USD | -1,425,811.20 USD | `-6.40%` | -2,537,779.67 USD | `-1.32` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:46:31 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


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
| `Live` | `Long Liquidation` | `0.0285` | 171.00 USD | 200,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0445` | 201.07 USD | 200,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0475` | 2,650.00 USD | 200,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 417.68 USD | 197,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 3,940.00 USD | 197,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 829.69 USD | 193,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 1,100.00 USD | 192,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 353.81 USD | 191,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 518.48 USD | 191,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 1,920.00 USD | 190,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 24,280.00 USD | 188,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,300.00 USD | 164,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 1,020.00 USD | 162,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 1,170.00 USD | 161,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 46,250.00 USD | 160,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 339.50 USD | 113,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 1,110.00 USD | 113,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 223.98 USD | 112,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 1,560.00 USD | 112,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0878` | 1,150,000.00 USD | 1,150,000.00 USD | 1,370.00 USD | 4,930.00 USD | 27,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0881` | 1,120,000.00 USD | 1,120,000.00 USD | 3,770.00 USD | 2,660.00 USD | 12,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0884` | 1,100,000.00 USD | 1,100,000.00 USD | 7,040.00 USD | 4,640.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0887` | 1,070,000.00 USD | 1,070,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0890` | 1,040,000.00 USD | 1,040,000.00 USD | 14,610.00 USD | 4,470.00 USD | 3,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0893` | 1,020,000.00 USD | 1,020,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,420.00 USD | 110,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0896` | 996,160.00 USD | 996,160.00 USD | 5,760.00 USD | 611.80 USD | 6,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0899` | 982,910.00 USD | 982,910.00 USD | 3,390.00 USD | 927.82 USD | 4,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0900` | 792,470.00 USD | 792,470.00 USD | 1,560.00 USD | 0.00 USD | 293.66 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0902` | 790,620.00 USD | 790,620.00 USD | 893.87 USD | 914.96 USD | 3.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0902` | 974,120.00 USD | 974,120.00 USD | 2,270.00 USD | 910.78 USD | 1,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0904` | 788,800.00 USD | 788,800.00 USD | 831.11 USD | 1,480.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0905` | 969,700.00 USD | 969,700.00 USD | 10,350.00 USD | 996.61 USD | 4,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0905` | 3,230.00 USD | 107,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0906` | 784,460.00 USD | 784,460.00 USD | 1,580.00 USD | 1,260.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0908` | 779,030.00 USD | 779,030.00 USD | 707.85 USD | 0.00 USD | 1,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0908` | 954,270.00 USD | 954,270.00 USD | 3,950.00 USD | 4,470.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0910` | 777,290.00 USD | 777,290.00 USD | 6,520.00 USD | 363.17 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0911` | 942,860.00 USD | 942,860.00 USD | 0.00 USD | 606.54 USD | 2,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0912` | 770,410.00 USD | 770,410.00 USD | 0.00 USD | 1,450.00 USD | 787.79 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0914` | 768,170.00 USD | 768,170.00 USD | 0.00 USD | 944.94 USD | 51.31 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0914` | 939,620.00 USD | 939,620.00 USD | 1,670.00 USD | 903.90 USD | 38.51 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0916` | 767,180.00 USD | 767,180.00 USD | 6,590.00 USD | 824.99 USD | 2.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0917` | 937,010.00 USD | 937,010.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0918` | 759,760.00 USD | 759,760.00 USD | 5,140.00 USD | 754.23 USD | 2,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0920` | 751,350.00 USD | 751,350.00 USD | 3,690.00 USD | 504.78 USD | 2,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0922` | 744,580.00 USD | 744,580.00 USD | 0.00 USD | 750.63 USD | 62.82 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0923` | 928,990.00 USD | 928,990.00 USD | 0.00 USD | 0.00 USD | 10,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0924` | 743,770.00 USD | 743,770.00 USD | 1,410.00 USD | 518.97 USD | 14,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0926` | 727,440.00 USD | 727,440.00 USD | 3,270.00 USD | 1,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0926` | 918,440.00 USD | 918,440.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0929` | 908,460.00 USD | 908,460.00 USD | 0.00 USD | 0.00 USD | 56.98 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0932` | 908,410.00 USD | 908,410.00 USD | 0.00 USD | 0.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0934` | 722,520.00 USD | 722,520.00 USD | 0.00 USD | 0.00 USD | 6,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0935` | 896,220.00 USD | 896,220.00 USD | 0.00 USD | 1,320.00 USD | 6,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0938` | 715,660.00 USD | 715,660.00 USD | 0.00 USD | 0.00 USD | 141.01 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0941` | 888,390.00 USD | 888,390.00 USD | 2,050.00 USD | 0.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0944` | 883,330.00 USD | 883,330.00 USD | 1,870.00 USD | 0.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0945` | 69,120.00 USD | 103,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0947` | 873,950.00 USD | 873,950.00 USD | 3,790.00 USD | 1,810.00 USD | 22.82 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0948` | 715,520.00 USD | 715,520.00 USD | 0.00 USD | 0.00 USD | 69.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0950` | 868,320.00 USD | 868,320.00 USD | 3,770.00 USD | 0.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0954` | 715,450.00 USD | 715,450.00 USD | 0.00 USD | 0.00 USD | 154.48 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0955` | 1,910.00 USD | 34,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0956` | 715,290.00 USD | 715,290.00 USD | 0.00 USD | 1,180.00 USD | 166.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0956` | 857,880.00 USD | 857,880.00 USD | 0.00 USD | 0.00 USD | 97.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0959` | 857,790.00 USD | 857,790.00 USD | 0.00 USD | 0.00 USD | 111.87 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0962` | 713,940.00 USD | 713,940.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0962` | 857,680.00 USD | 857,680.00 USD | 0.00 USD | 0.00 USD | 88.03 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0964` | 711,860.00 USD | 711,860.00 USD | 0.00 USD | 0.00 USD | 107.13 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0965` | 966.47 USD | 32,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0966` | 711,760.00 USD | 711,760.00 USD | 2,140.00 USD | 715.37 USD | 6,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0968` | 702,720.00 USD | 702,720.00 USD | 6,400.00 USD | 2,400.00 USD | 11,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0968` | 857,590.00 USD | 857,590.00 USD | 7,490.00 USD | 3,720.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0970` | 682,640.00 USD | 682,640.00 USD | 1,290.00 USD | 2,860.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 834,830.00 USD | 834,830.00 USD | 0.00 USD | 3,760.00 USD | 9,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0972` | 674,260.00 USD | 674,260.00 USD | 14,810.00 USD | 5,180.00 USD | 2,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0974` | 651,320.00 USD | 651,320.00 USD | 2,750.00 USD | 4,850.00 USD | 2,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0974` | 821,350.00 USD | 821,350.00 USD | 0.00 USD | 1,390.00 USD | 3,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0975` | 11,950.00 USD | 31,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0976` | 640,970.00 USD | 640,970.00 USD | 18,450.00 USD | 4,820.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0977` | 816,900.00 USD | 816,900.00 USD | 0.00 USD | 4,010.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0978` | 610,230.00 USD | 610,230.00 USD | 22,180.00 USD | 3,360.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0980` | 575,390.00 USD | 575,390.00 USD | 12,450.00 USD | 3,070.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0980` | 784,080.00 USD | 784,080.00 USD | 0.00 USD | 3,920.00 USD | 5,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0982` | 549,370.00 USD | 549,370.00 USD | 1,840.00 USD | 3,990.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 774,370.00 USD | 774,370.00 USD | 7,990.00 USD | 1,230.00 USD | 14,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0984` | 529,350.00 USD | 529,350.00 USD | 10,600.00 USD | 460.32 USD | 18,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0985` | 19,960.00 USD | 19,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0986` | 499,490.00 USD | 499,490.00 USD | 10,070.00 USD | 5,230.00 USD | 32,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0986` | 750,410.00 USD | 750,410.00 USD | 7,110.00 USD | 7,530.00 USD | 60,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0988` | 451,650.00 USD | 451,650.00 USD | 12,770.00 USD | 6,260.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 674,870.00 USD | 674,870.00 USD | 17,640.00 USD | 6,190.00 USD | 53,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0990` | 428,950.00 USD | 428,950.00 USD | 3,980.00 USD | 3,340.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0992` | 419,060.00 USD | 419,060.00 USD | 29,370.00 USD | 5,050.00 USD | 7,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0992` | 597,820.00 USD | 597,820.00 USD | 27,140.00 USD | 11,490.00 USD | 28,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0994` | 376,810.00 USD | 376,810.00 USD | 10,240.00 USD | 4,740.00 USD | 9,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 530,590.00 USD | 530,590.00 USD | 24,220.00 USD | 15,150.00 USD | 56,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0996` | 352,010.00 USD | 352,010.00 USD | 2,640.00 USD | 4,700.00 USD | 28,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0998` | 316,390.00 USD | 316,390.00 USD | 35,620.00 USD | 7,340.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0998` | 434,370.00 USD | 434,370.00 USD | 28,450.00 USD | 12,100.00 USD | 80,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1000` | 254,030.00 USD | 254,030.00 USD | 48,950.00 USD | 7,140.00 USD | 26,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 313,010.00 USD | 313,010.00 USD | 36,110.00 USD | 8,650.00 USD | 13,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1002` | 171,720.00 USD | 171,720.00 USD | 21,100.00 USD | 4,620.00 USD | 17,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1004` | 128,740.00 USD | 128,740.00 USD | 1,970.00 USD | 5,260.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1004` | 255,070.00 USD | 255,070.00 USD | 22,470.00 USD | 16,470.00 USD | 23,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1006` | 107,560.00 USD | 107,560.00 USD | 16,470.00 USD | 5,640.00 USD | 72,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 192,500.00 USD | 192,500.00 USD | 20,870.00 USD | 3,870.00 USD | 100,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1008` | 12,690.00 USD | 12,690.00 USD | 0.00 USD | 8,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1010` | 3,980.00 USD | 3,980.00 USD | 0.00 USD | 0.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1010` | 67,130.00 USD | 67,130.00 USD | 17,340.00 USD | 6,580.00 USD | 6,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1012` | 1,530.00 USD | 1,530.00 USD | 0.00 USD | 0.00 USD | 939.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 36,530.00 USD | 36,530.00 USD | 15,270.00 USD | 5,230.00 USD | 553.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1014` | 587.32 USD | 587.32 USD | 0.00 USD | 0.00 USD | 587.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1016` | 15,480.00 USD | 15,480.00 USD | 15,440.00 USD | 0.00 USD | 32.62 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1019` | 12,410.00 USD | 12,410.00 USD | 12,100.00 USD | 0.00 USD | 315.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1022` | 32,950.00 USD | 32,950.00 USD | 11,930.00 USD | 8,250.00 USD | 352.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1025` | 34,500.00 USD | 34,500.00 USD | 1,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1028` | 42,690.00 USD | 42,690.00 USD | 3,800.00 USD | 4,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1030` | 11,070.00 USD | 11,070.00 USD | 0.00 USD | 0.00 USD | 11,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1031` | 68,510.00 USD | 68,510.00 USD | 19,560.00 USD | 6,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1032` | 62,990.00 USD | 62,990.00 USD | 27,910.00 USD | 3,360.00 USD | 20,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1034` | 81,430.00 USD | 81,430.00 USD | 5,500.00 USD | 3,920.00 USD | 9,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1034` | 94,460.00 USD | 94,460.00 USD | 18,920.00 USD | 7,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1036` | 101,250.00 USD | 101,250.00 USD | 6,930.00 USD | 12,830.00 USD | 54.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1037` | 108,280.00 USD | 108,280.00 USD | 2,710.00 USD | 10,710.00 USD | 403.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1038` | 151,480.00 USD | 151,480.00 USD | 35,160.00 USD | 15,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1040` | 193,640.00 USD | 193,640.00 USD | 12,950.00 USD | 16,660.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1040` | 156,190.00 USD | 156,190.00 USD | 5,940.00 USD | 10,300.00 USD | 31,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1042` | 220,390.00 USD | 220,390.00 USD | 0.00 USD | 9,490.00 USD | 17,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1043` | 179,150.00 USD | 179,150.00 USD | 15,960.00 USD | 5,980.00 USD | 1,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1044` | 234,760.00 USD | 234,760.00 USD | 0.00 USD | 14,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1046` | 267,600.00 USD | 267,600.00 USD | 7,060.00 USD | 1,080.00 USD | 24,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1046` | 250,410.00 USD | 250,410.00 USD | 0.00 USD | 9,810.00 USD | 61,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1048` | 384,750.00 USD | 384,750.00 USD | 27,930.00 USD | 9,140.00 USD | 80,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1049` | 376,170.00 USD | 376,170.00 USD | 34,790.00 USD | 6,530.00 USD | 84,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1050` | 441,510.00 USD | 441,510.00 USD | 35,330.00 USD | 10,740.00 USD | 10,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1052` | 545,580.00 USD | 545,580.00 USD | 43,830.00 USD | 12,940.00 USD | 47,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1052` | 554,500.00 USD | 554,500.00 USD | 28,200.00 USD | 24,160.00 USD | 125,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1054` | 697,580.00 USD | 697,580.00 USD | 59,720.00 USD | 20,100.00 USD | 72,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1055` | 933,130.00 USD | 933,130.00 USD | 122,840.00 USD | 44,430.00 USD | 211,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1056` | 795,770.00 USD | 795,770.00 USD | 25,000.00 USD | 29,020.00 USD | 44,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1058` | 907,190.00 USD | 907,190.00 USD | 30,300.00 USD | 2,830.00 USD | 78,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1058` | 1,280,000.00 USD | 1,280,000.00 USD | 105,620.00 USD | 56,540.00 USD | 189,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1060` | 1,010,000.00 USD | 1,010,000.00 USD | 44,890.00 USD | 1,890.00 USD | 54,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1061` | 1,550,000.00 USD | 1,550,000.00 USD | 75,540.00 USD | 72,260.00 USD | 117,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1062` | 1,120,000.00 USD | 1,120,000.00 USD | 31,870.00 USD | 2,030.00 USD | 78,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1064` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 2,630.00 USD | 51,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1064` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 52,580.00 USD | 192,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1066` | 1,210,000.00 USD | 1,210,000.00 USD | 3,530.00 USD | 0.00 USD | 31,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1067` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 51,740.00 USD | 156,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1068` | 1,270,000.00 USD | 1,270,000.00 USD | 4,700.00 USD | 2,620.00 USD | 55,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1070` | 1,340,000.00 USD | 1,340,000.00 USD | 8,170.00 USD | 7,280.00 USD | 51,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1070` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 57,770.00 USD | 134,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1072` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 236.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1073` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 17,700.00 USD | 22.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1074` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 101.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1076` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 137.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1076` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 22,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1078` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 17,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1079` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 79.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1082` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 5,910.00 USD | 21.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1082` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1084` | 1,410,000.00 USD | 1,410,000.00 USD | 7,990.00 USD | 0.00 USD | 35,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1085` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 113.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1086` | 1,490,000.00 USD | 1,490,000.00 USD | 4,220.00 USD | 2,240.00 USD | 72,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1088` | 1,540,000.00 USD | 1,540,000.00 USD | 44,230.00 USD | 0.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1088` | 2,240,000.00 USD | 2,240,000.00 USD | 5,290.00 USD | 0.00 USD | 171.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1090` | 1,580,000.00 USD | 1,580,000.00 USD | 43,010.00 USD | 0.00 USD | 124.57 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1091` | 2,270,000.00 USD | 2,270,000.00 USD | 16,310.00 USD | 0.00 USD | 9,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1092` | 1,590,000.00 USD | 1,590,000.00 USD | 10,290.00 USD | 0.00 USD | 29.91 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1094` | 1,620,000.00 USD | 1,620,000.00 USD | 13,100.00 USD | 0.00 USD | 14,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1094` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 8,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1096` | 1,630,000.00 USD | 1,630,000.00 USD | 4,110.00 USD | 1,890.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1097` | 2,300,000.00 USD | 2,300,000.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1098` | 1,670,000.00 USD | 1,670,000.00 USD | 13,380.00 USD | 3,910.00 USD | 22,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1100` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 2,820.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1100` | 2,330,000.00 USD | 2,330,000.00 USD | 11,470.00 USD | 0.00 USD | 21,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1102` | 1,690,000.00 USD | 1,690,000.00 USD | 4,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 2,370,000.00 USD | 2,370,000.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1104` | 1,700,000.00 USD | 1,700,000.00 USD | 6,920.00 USD | 10,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1106` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 12,720.00 USD | 30,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1106` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 22,880.00 USD | 15,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1108` | 1,770,000.00 USD | 1,770,000.00 USD | 5,220.00 USD | 1,120.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1112` | 1,780,000.00 USD | 1,780,000.00 USD | 10,780.00 USD | 0.00 USD | 96.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1112` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1114` | 1,840,000.00 USD | 1,840,000.00 USD | 15,810.00 USD | 5,880.00 USD | 39,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1116` | 1,860,000.00 USD | 1,860,000.00 USD | 4,760.00 USD | 12,550.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1118` | 1,970,000.00 USD | 1,970,000.00 USD | 25,510.00 USD | 20,030.00 USD | 57,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1118` | 2,520,000.00 USD | 2,520,000.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1120` | 2,010,000.00 USD | 2,010,000.00 USD | 27,100.00 USD | 9,370.00 USD | 9,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 2,570,000.00 USD | 2,570,000.00 USD | 17,760.00 USD | 0.00 USD | 38,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1122` | 2,060,000.00 USD | 2,060,000.00 USD | 23,990.00 USD | 5,240.00 USD | 15,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1124` | 2,090,000.00 USD | 2,090,000.00 USD | 17,850.00 USD | 6,120.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1124` | 2,680,000.00 USD | 2,680,000.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1126` | 2,130,000.00 USD | 2,130,000.00 USD | 9,370.00 USD | 11,410.00 USD | 17,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1127` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1128` | 2,150,000.00 USD | 2,150,000.00 USD | 10,120.00 USD | 0.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1130` | 2,170,000.00 USD | 2,170,000.00 USD | 7,970.00 USD | 2,000.00 USD | 16,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1130` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 24,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1132` | 2,230,000.00 USD | 2,230,000.00 USD | 19,390.00 USD | 18,950.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 2,750,000.00 USD | 2,750,000.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1134` | 2,260,000.00 USD | 2,260,000.00 USD | 4,040.00 USD | 12,980.00 USD | 13,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1136` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 787.70 USD | 4,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1136` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 5,520.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1138` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 856.93 USD | 14,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1139` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 9,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1140` | 2,290,000.00 USD | 2,290,000.00 USD | 7,800.00 USD | 0.00 USD | 6,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1142` | 2,360,000.00 USD | 2,360,000.00 USD | 24,760.00 USD | 17,100.00 USD | 22,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1142` | 2,790,000.00 USD | 2,790,000.00 USD | 10,380.00 USD | 0.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1144` | 2,420,000.00 USD | 2,420,000.00 USD | 9,940.00 USD | 21,970.00 USD | 31,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 3,030,000.00 USD | 3,030,000.00 USD | 16,540.00 USD | 2,730.00 USD | 219,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1146` | 2,470,000.00 USD | 2,470,000.00 USD | 5,090.00 USD | 10,830.00 USD | 30,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1148` | 2,530,000.00 USD | 2,530,000.00 USD | 33,430.00 USD | 3,280.00 USD | 30,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1148` | 3,220,000.00 USD | 3,220,000.00 USD | 9,880.00 USD | 0.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1150` | 2,590,000.00 USD | 2,590,000.00 USD | 19,260.00 USD | 13,020.00 USD | 21,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 3,490,000.00 USD | 3,490,000.00 USD | 103,130.00 USD | 4,210.00 USD | 163,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1152` | 2,700,000.00 USD | 2,700,000.00 USD | 30,190.00 USD | 17,470.00 USD | 59,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1153` | 2,730,000.00 USD | 2,730,000.00 USD | 6,400.00 USD | 4,560.00 USD | 23,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1154` | 3,950,000.00 USD | 3,950,000.00 USD | 243,190.00 USD | 26,970.00 USD | 195,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 4,270,000.00 USD | 4,270,000.00 USD | 188,950.00 USD | 25,290.00 USD | 98,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1160` | 4,550,000.00 USD | 4,550,000.00 USD | 139,350.00 USD | 32,830.00 USD | 109,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 4,830,000.00 USD | 4,830,000.00 USD | 142,050.00 USD | 28,590.00 USD | 112,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1166` | 5,050,000.00 USD | 5,050,000.00 USD | 130,810.00 USD | 46,040.00 USD | 42,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 5,270,000.00 USD | 5,270,000.00 USD | 82,770.00 USD | 26,150.00 USD | 113,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1172` | 5,400,000.00 USD | 5,400,000.00 USD | 64,270.00 USD | 14,930.00 USD | 48,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 5,570,000.00 USD | 5,570,000.00 USD | 72,770.00 USD | 17,930.00 USD | 82,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1178` | 5,740,000.00 USD | 5,740,000.00 USD | 89,510.00 USD | 23,660.00 USD | 55,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 5,830,000.00 USD | 5,830,000.00 USD | 32,770.00 USD | 23,410.00 USD | 29,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1184` | 5,890,000.00 USD | 5,890,000.00 USD | 11,640.00 USD | 5,170.00 USD | 47,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 5,970,000.00 USD | 5,970,000.00 USD | 5,620.00 USD | 17,120.00 USD | 54,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1190` | 6,110,000.00 USD | 6,110,000.00 USD | 29,530.00 USD | 29,230.00 USD | 86,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 6,200,000.00 USD | 6,200,000.00 USD | 41,630.00 USD | 1,160.00 USD | 38,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1196` | 6,260,000.00 USD | 6,260,000.00 USD | 17,970.00 USD | 1,780.00 USD | 40,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 6,350,000.00 USD | 6,350,000.00 USD | 9,100.00 USD | 13,190.00 USD | 68,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1202` | 6,540,000.00 USD | 6,540,000.00 USD | 138,430.00 USD | 21,430.00 USD | 32,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 6,880,000.00 USD | 6,880,000.00 USD | 132,960.00 USD | 72,910.00 USD | 130,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1208` | 7,010,000.00 USD | 7,010,000.00 USD | 39,480.00 USD | 25,720.00 USD | 66,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 7,220,000.00 USD | 7,220,000.00 USD | 72,500.00 USD | 25,920.00 USD | 111,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1214` | 7,340,000.00 USD | 7,340,000.00 USD | 23,920.00 USD | 19,420.00 USD | 76,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 7,380,000.00 USD | 7,380,000.00 USD | 24,400.00 USD | 6,160.00 USD | 18,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1220` | 7,500,000.00 USD | 7,500,000.00 USD | 45,700.00 USD | 10,970.00 USD | 54,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 7,640,000.00 USD | 7,640,000.00 USD | 76,930.00 USD | 24,740.00 USD | 45,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 3,770.00 USD | 3,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1226` | 7,730,000.00 USD | 7,730,000.00 USD | 54,940.00 USD | 27,490.00 USD | 5,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 7,920,000.00 USD | 7,920,000.00 USD | 71,850.00 USD | 38,040.00 USD | 73,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1232` | 8,080,000.00 USD | 8,080,000.00 USD | 67,800.00 USD | 28,560.00 USD | 68,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1235` | 8,120,000.00 USD | 8,120,000.00 USD | 15,040.00 USD | 5,390.00 USD | 17,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1238` | 8,130,000.00 USD | 8,130,000.00 USD | 8,310.00 USD | 3,610.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1241` | 8,150,000.00 USD | 8,150,000.00 USD | 11,380.00 USD | 1,380.00 USD | 7,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1244` | 8,200,000.00 USD | 8,200,000.00 USD | 26,540.00 USD | 8,130.00 USD | 9,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1245` | 195.94 USD | 3,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1247` | 8,230,000.00 USD | 8,230,000.00 USD | 7,900.00 USD | 12,590.00 USD | 15,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1250` | 8,250,000.00 USD | 8,250,000.00 USD | 8,540.00 USD | 4,990.00 USD | 5,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1253` | 8,270,000.00 USD | 8,270,000.00 USD | 1,550.00 USD | 0.00 USD | 13,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1256` | 8,290,000.00 USD | 8,290,000.00 USD | 11,990.00 USD | 11,420.00 USD | 131.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1259` | 8,300,000.00 USD | 8,300,000.00 USD | 5,870.00 USD | 1,190.00 USD | 172.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1262` | 8,310,000.00 USD | 8,310,000.00 USD | 4,270.00 USD | 0.00 USD | 3,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1265` | 8,320,000.00 USD | 8,320,000.00 USD | 2,710.00 USD | 0.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1268` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 0.00 USD | 2,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1271` | 8,320,000.00 USD | 8,320,000.00 USD | 5,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1274` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 0.00 USD | 36.76 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1277` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 0.00 USD | 9.84 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1280` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 0.00 USD | 6,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1355` | 1,330.00 USD | 5,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1475` | 25,600.00 USD | 30,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1525` | 6,090.00 USD | 37,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1565` | 550.61 USD | 37,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1575` | 15,750.00 USD | 53,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1695` | 169.25 USD | 53,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1865` | 367.78 USD | 53,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1945` | 231.28 USD | 54,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2025` | 978.82 USD | 55,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0285` | 200,920.00 USD | 0.00 USD | 171.00 USD | `-71.97%` | `6,000.00` |
| `Live` | `Long` | `0.0445` | 200,750.00 USD | 0.00 USD | 201.07 USD | `-56.23%` | `4,518.50` |
| `Live` | `Long` | `0.0475` | 200,550.00 USD | 0.00 USD | 2,650.00 USD | `-53.28%` | `55,786.40` |
| `Live` | `Long` | `0.0545` | 197,900.00 USD | 0.00 USD | 417.68 USD | `-46.39%` | `7,663.80` |
| `Live` | `Long` | `0.0565` | 197,480.00 USD | 0.00 USD | 3,940.00 USD | `-44.42%` | `69,790.10` |
| `Live` | `Long` | `0.0575` | 193,540.00 USD | 0.00 USD | 829.69 USD | `-43.44%` | `14,429.40` |
| `Live` | `Long` | `0.0615` | 192,710.00 USD | 0.00 USD | 1,100.00 USD | `-39.50%` | `17,943.80` |
| `Live` | `Long` | `0.0645` | 191,600.00 USD | 0.00 USD | 353.81 USD | `-36.55%` | `5,485.40` |
| `Live` | `Long` | `0.0675` | 191,250.00 USD | 0.00 USD | 518.48 USD | `-33.60%` | `7,681.20` |
| `Live` | `Long` | `0.0685` | 190,730.00 USD | 0.00 USD | 1,920.00 USD | `-32.62%` | `28,000.00` |
| `Live` | `Long` | `0.0725` | 188,810.00 USD | 0.00 USD | 24,280.00 USD | `-28.68%` | `334,954.50` |
| `Live` | `Long` | `0.0745` | 164,530.00 USD | 0.00 USD | 2,300.00 USD | `-26.72%` | `30,851.90` |
| `Live` | `Long` | `0.0755` | 162,230.00 USD | 0.00 USD | 1,020.00 USD | `-25.73%` | `13,481.90` |
| `Live` | `Long` | `0.0765` | 161,210.00 USD | 0.00 USD | 1,170.00 USD | `-24.75%` | `15,263.30` |
| `Live` | `Long` | `0.0775` | 160,050.00 USD | 0.00 USD | 46,250.00 USD | `-23.77%` | `596,757.50` |
| `Live` | `Long` | `0.0785` | 113,800.00 USD | 0.00 USD | 339.50 USD | `-22.78%` | `4,324.80` |
| `Live` | `Long` | `0.0795` | 113,460.00 USD | 0.00 USD | 1,110.00 USD | `-21.80%` | `13,940.20` |
| `Live` | `Long` | `0.0805` | 112,350.00 USD | 0.00 USD | 223.98 USD | `-20.81%` | `2,782.40` |
| `Live` | `Long` | `0.0815` | 112,130.00 USD | 0.00 USD | 1,560.00 USD | `-19.83%` | `19,181.40` |
| `Live` | `Long` | `0.0895` | 110,560.00 USD | 0.00 USD | 3,420.00 USD | `-11.96%` | `38,251.10` |
| `Live` | `Long` | `0.0905` | 107,140.00 USD | 0.00 USD | 3,230.00 USD | `-10.98%` | `35,741.10` |
| `Live` | `Long` | `0.0945` | 103,900.00 USD | 0.00 USD | 69,120.00 USD | `-7.04%` | `731,405.60` |
| `Live` | `Long` | `0.0955` | 34,790.00 USD | 0.00 USD | 1,910.00 USD | `-6.06%` | `20,000.00` |
| `Live` | `Long` | `0.0965` | 32,880.00 USD | 0.00 USD | 966.47 USD | `-5.08%` | `10,015.20` |
| `Live` | `Long` | `0.0975` | 31,910.00 USD | 0.00 USD | 11,950.00 USD | `-4.09%` | `122,573.60` |
| `Live` | `Long` | `0.0985` | 19,960.00 USD | 0.00 USD | 19,960.00 USD | `-3.11%` | `202,627.30` |
| `Live` | `Short` | `0.1225` | 3,770.00 USD | 3,770.00 USD | 0.00 USD | `+20.50%` | `30,808.20` |
| `Live` | `Short` | `0.1245` | 3,970.00 USD | 195.94 USD | 0.00 USD | `+22.47%` | `1,573.80` |
| `Live` | `Short` | `0.1355` | 5,300.00 USD | 1,330.00 USD | 0.00 USD | `+33.29%` | `9,843.80` |
| `Live` | `Short` | `0.1475` | 30,910.00 USD | 25,600.00 USD | 0.00 USD | `+45.09%` | `173,573.70` |
| `Live` | `Short` | `0.1525` | 37,000.00 USD | 6,090.00 USD | 0.00 USD | `+50.01%` | `39,929.50` |
| `Live` | `Short` | `0.1565` | 37,550.00 USD | 550.61 USD | 0.00 USD | `+53.94%` | `3,518.30` |
| `Live` | `Short` | `0.1575` | 53,300.00 USD | 15,750.00 USD | 0.00 USD | `+54.93%` | `100,000.40` |
| `Live` | `Short` | `0.1695` | 53,470.00 USD | 169.25 USD | 0.00 USD | `+66.73%` | `998.50` |
| `Live` | `Short` | `0.1865` | 53,830.00 USD | 367.78 USD | 0.00 USD | `+83.45%` | `1,972.00` |
| `Live` | `Short` | `0.1945` | 54,060.00 USD | 231.28 USD | 0.00 USD | `+91.32%` | `1,189.10` |
| `Live` | `Short` | `0.2025` | 55,040.00 USD | 978.82 USD | 0.00 USD | `+99.19%` | `4,833.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0635` | 19,320.00 USD | 0.00 USD | 1,140.00 USD | `-37.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 18,180.00 USD | 0.00 USD | 773.46 USD | `-30.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 17,410.00 USD | 0.00 USD | 592.27 USD | `-29.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 16,820.00 USD | 0.00 USD | 755.00 USD | `-25.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0805` | 16,060.00 USD | 0.00 USD | 411.06 USD | `-20.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0815` | 15,650.00 USD | 0.00 USD | 285.01 USD | `-19.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0835` | 15,370.00 USD | 0.00 USD | 456.70 USD | `-17.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 14,910.00 USD | 0.00 USD | 631.58 USD | `-15.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 14,280.00 USD | 0.00 USD | 653.74 USD | `-12.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 13,620.00 USD | 0.00 USD | 444.62 USD | `-10.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0915` | 13,180.00 USD | 0.00 USD | 1,460.00 USD | `-9.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 11,720.00 USD | 0.00 USD | 485.13 USD | `-7.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0965` | 11,230.00 USD | 0.00 USD | 5,700.00 USD | `-5.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0975` | 5,530.00 USD | 0.00 USD | 720.22 USD | `-4.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0985` | 4,810.00 USD | 0.00 USD | 931.75 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0995` | 3,880.00 USD | 0.00 USD | 801.64 USD | `-2.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 3,080.00 USD | 0.00 USD | 2,180.00 USD | `-1.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1015` | 903.42 USD | 0.00 USD | 903.42 USD | `-0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1025` | 780.70 USD | 780.70 USD | 0.00 USD | `+0.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1035` | 5,430.00 USD | 4,650.00 USD | 0.00 USD | `+1.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 24,380.00 USD | 18,950.00 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 32,150.00 USD | 7,770.00 USD | 0.00 USD | `+3.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 141,430.00 USD | 109,280.00 USD | 0.00 USD | `+4.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1075` | 163,340.00 USD | 21,900.00 USD | 0.00 USD | `+5.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1085` | 163,490.00 USD | 150.04 USD | 0.00 USD | `+6.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1095` | 164,120.00 USD | 639.36 USD | 0.00 USD | `+7.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 164,290.00 USD | 162.59 USD | 0.00 USD | `+8.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 165,130.00 USD | 839.64 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1125` | 165,910.00 USD | 786.65 USD | 0.00 USD | `+10.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1135` | 166,030.00 USD | 116.27 USD | 0.00 USD | `+11.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1145` | 166,160.00 USD | 134.61 USD | 0.00 USD | `+12.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 166,300.00 USD | 137.71 USD | 0.00 USD | `+13.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1165` | 166,480.00 USD | 180.81 USD | 0.00 USD | `+14.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1175` | 166,850.00 USD | 363.49 USD | 0.00 USD | `+15.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1185` | 167,900.00 USD | 1,050.00 USD | 0.00 USD | `+16.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1195` | 182,540.00 USD | 14,640.00 USD | 0.00 USD | `+17.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1205` | 182,930.00 USD | 398.42 USD | 0.00 USD | `+18.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1225` | 183,910.00 USD | 980.00 USD | 0.00 USD | `+20.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1235` | 196,260.00 USD | 12,350.00 USD | 0.00 USD | `+21.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1255` | 200,640.00 USD | 4,380.00 USD | 0.00 USD | `+23.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1275` | 201,130.00 USD | 492.06 USD | 0.00 USD | `+25.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1305` | 201,580.00 USD | 444.24 USD | 0.00 USD | `+28.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1315` | 233,140.00 USD | 31,560.00 USD | 0.00 USD | `+29.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1335` | 234,450.00 USD | 1,310.00 USD | 0.00 USD | `+31.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1345` | 238,600.00 USD | 4,150.00 USD | 0.00 USD | `+32.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1365` | 246,190.00 USD | 7,590.00 USD | 0.00 USD | `+34.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1405` | 259,300.00 USD | 13,110.00 USD | 0.00 USD | `+38.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1425` | 259,400.00 USD | 102.22 USD | 0.00 USD | `+40.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1435` | 266,580.00 USD | 7,180.00 USD | 0.00 USD | `+41.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1485` | 269,220.00 USD | 2,650.00 USD | 0.00 USD | `+46.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1495` | 270,020.00 USD | 792.53 USD | 0.00 USD | `+47.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1525` | 273,780.00 USD | 3,770.00 USD | 0.00 USD | `+50.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 273,970.00 USD | 184.49 USD | 0.00 USD | `+52.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 276,780.00 USD | 2,810.00 USD | 0.00 USD | `+53.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 277,000.00 USD | 219.81 USD | 0.00 USD | `+54.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 277,270.00 USD | 277.62 USD | 0.00 USD | `+60.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 279,070.00 USD | 1,800.00 USD | 0.00 USD | `+66.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 279,280.00 USD | 216.55 USD | 0.00 USD | `+71.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 279,400.00 USD | 117.26 USD | 0.00 USD | `+94.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 299,940.00 USD | 20,530.00 USD | 0.00 USD | `+97.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 300,120.00 USD | 189.30 USD | 0.00 USD | `+100.18%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0878` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 1,370.00 USD | 4,930.00 USD | 27,300.00 USD |
| `7D` | `0.0881` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 3,770.00 USD | 2,660.00 USD | 12,920.00 USD |
| `7D` | `0.0884` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 7,040.00 USD | 4,640.00 USD | 11,900.00 USD |
| `7D` | `0.0887` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,560.00 USD |
| `7D` | `0.0890` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 14,610.00 USD | 4,470.00 USD | 3,690.00 USD |
| `7D` | `0.0893` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD |
| `7D` | `0.0896` | 996,160.00 USD | 0.00 USD | 996,160.00 USD | 5,760.00 USD | 611.80 USD | 6,880.00 USD |
| `7D` | `0.0899` | 982,910.00 USD | 0.00 USD | 982,910.00 USD | 3,390.00 USD | 927.82 USD | 4,470.00 USD |
| `1D` | `0.0900` | 792,470.00 USD | 0.00 USD | 792,470.00 USD | 1,560.00 USD | 0.00 USD | 293.66 USD |
| `1D` | `0.0902` | 790,620.00 USD | 0.00 USD | 790,620.00 USD | 893.87 USD | 914.96 USD | 3.96 USD |
| `7D` | `0.0902` | 974,120.00 USD | 0.00 USD | 974,120.00 USD | 2,270.00 USD | 910.78 USD | 1,240.00 USD |
| `1D` | `0.0904` | 788,800.00 USD | 0.00 USD | 788,800.00 USD | 831.11 USD | 1,480.00 USD | 2,020.00 USD |
| `7D` | `0.0905` | 969,700.00 USD | 0.00 USD | 969,700.00 USD | 10,350.00 USD | 996.61 USD | 4,080.00 USD |
| `1D` | `0.0906` | 784,460.00 USD | 0.00 USD | 784,460.00 USD | 1,580.00 USD | 1,260.00 USD | 2,600.00 USD |
| `1D` | `0.0908` | 779,030.00 USD | 0.00 USD | 779,030.00 USD | 707.85 USD | 0.00 USD | 1,020.00 USD |
| `7D` | `0.0908` | 954,270.00 USD | 0.00 USD | 954,270.00 USD | 3,950.00 USD | 4,470.00 USD | 2,980.00 USD |
| `1D` | `0.0910` | 777,290.00 USD | 0.00 USD | 777,290.00 USD | 6,520.00 USD | 363.17 USD | 0.00 USD |
| `7D` | `0.0911` | 942,860.00 USD | 0.00 USD | 942,860.00 USD | 0.00 USD | 606.54 USD | 2,630.00 USD |
| `1D` | `0.0912` | 770,410.00 USD | 0.00 USD | 770,410.00 USD | 0.00 USD | 1,450.00 USD | 787.79 USD |
| `1D` | `0.0914` | 768,170.00 USD | 0.00 USD | 768,170.00 USD | 0.00 USD | 944.94 USD | 51.31 USD |
| `7D` | `0.0914` | 939,620.00 USD | 0.00 USD | 939,620.00 USD | 1,670.00 USD | 903.90 USD | 38.51 USD |
| `1D` | `0.0916` | 767,180.00 USD | 0.00 USD | 767,180.00 USD | 6,590.00 USD | 824.99 USD | 2.87 USD |
| `7D` | `0.0917` | 937,010.00 USD | 0.00 USD | 937,010.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD |
| `1D` | `0.0918` | 759,760.00 USD | 0.00 USD | 759,760.00 USD | 5,140.00 USD | 754.23 USD | 2,510.00 USD |
| `1D` | `0.0920` | 751,350.00 USD | 0.00 USD | 751,350.00 USD | 3,690.00 USD | 504.78 USD | 2,580.00 USD |
| `1D` | `0.0922` | 744,580.00 USD | 0.00 USD | 744,580.00 USD | 0.00 USD | 750.63 USD | 62.82 USD |
| `7D` | `0.0923` | 928,990.00 USD | 0.00 USD | 928,990.00 USD | 0.00 USD | 0.00 USD | 10,560.00 USD |
| `1D` | `0.0924` | 743,770.00 USD | 0.00 USD | 743,770.00 USD | 1,410.00 USD | 518.97 USD | 14,390.00 USD |
| `1D` | `0.0926` | 727,440.00 USD | 0.00 USD | 727,440.00 USD | 3,270.00 USD | 1,660.00 USD | 0.00 USD |
| `7D` | `0.0926` | 918,440.00 USD | 0.00 USD | 918,440.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD |
| `7D` | `0.0929` | 908,460.00 USD | 0.00 USD | 908,460.00 USD | 0.00 USD | 0.00 USD | 56.98 USD |
| `7D` | `0.0932` | 908,410.00 USD | 0.00 USD | 908,410.00 USD | 0.00 USD | 0.00 USD | 12,180.00 USD |
| `1D` | `0.0934` | 722,520.00 USD | 0.00 USD | 722,520.00 USD | 0.00 USD | 0.00 USD | 6,860.00 USD |
| `7D` | `0.0935` | 896,220.00 USD | 0.00 USD | 896,220.00 USD | 0.00 USD | 1,320.00 USD | 6,510.00 USD |
| `1D` | `0.0938` | 715,660.00 USD | 0.00 USD | 715,660.00 USD | 0.00 USD | 0.00 USD | 141.01 USD |
| `7D` | `0.0941` | 888,390.00 USD | 0.00 USD | 888,390.00 USD | 2,050.00 USD | 0.00 USD | 3,010.00 USD |
| `7D` | `0.0944` | 883,330.00 USD | 0.00 USD | 883,330.00 USD | 1,870.00 USD | 0.00 USD | 7,510.00 USD |
| `7D` | `0.0947` | 873,950.00 USD | 0.00 USD | 873,950.00 USD | 3,790.00 USD | 1,810.00 USD | 22.82 USD |
| `1D` | `0.0948` | 715,520.00 USD | 0.00 USD | 715,520.00 USD | 0.00 USD | 0.00 USD | 69.61 USD |
| `7D` | `0.0950` | 868,320.00 USD | 0.00 USD | 868,320.00 USD | 3,770.00 USD | 0.00 USD | 6,660.00 USD |
| `1D` | `0.0954` | 715,450.00 USD | 0.00 USD | 715,450.00 USD | 0.00 USD | 0.00 USD | 154.48 USD |
| `1D` | `0.0956` | 715,290.00 USD | 0.00 USD | 715,290.00 USD | 0.00 USD | 1,180.00 USD | 166.88 USD |
| `7D` | `0.0956` | 857,880.00 USD | 0.00 USD | 857,880.00 USD | 0.00 USD | 0.00 USD | 97.50 USD |
| `7D` | `0.0959` | 857,790.00 USD | 0.00 USD | 857,790.00 USD | 0.00 USD | 0.00 USD | 111.87 USD |
| `1D` | `0.0962` | 713,940.00 USD | 0.00 USD | 713,940.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0962` | 857,680.00 USD | 0.00 USD | 857,680.00 USD | 0.00 USD | 0.00 USD | 88.03 USD |
| `1D` | `0.0964` | 711,860.00 USD | 0.00 USD | 711,860.00 USD | 0.00 USD | 0.00 USD | 107.13 USD |
| `1D` | `0.0966` | 711,760.00 USD | 0.00 USD | 711,760.00 USD | 2,140.00 USD | 715.37 USD | 6,180.00 USD |
| `1D` | `0.0968` | 702,720.00 USD | 0.00 USD | 702,720.00 USD | 6,400.00 USD | 2,400.00 USD | 11,270.00 USD |
| `7D` | `0.0968` | 857,590.00 USD | 0.00 USD | 857,590.00 USD | 7,490.00 USD | 3,720.00 USD | 11,550.00 USD |
| `1D` | `0.0970` | 682,640.00 USD | 0.00 USD | 682,640.00 USD | 1,290.00 USD | 2,860.00 USD | 4,240.00 USD |
| `7D` | `0.0971` | 834,830.00 USD | 0.00 USD | 834,830.00 USD | 0.00 USD | 3,760.00 USD | 9,720.00 USD |
| `1D` | `0.0972` | 674,260.00 USD | 0.00 USD | 674,260.00 USD | 14,810.00 USD | 5,180.00 USD | 2,950.00 USD |
| `1D` | `0.0974` | 651,320.00 USD | 0.00 USD | 651,320.00 USD | 2,750.00 USD | 4,850.00 USD | 2,750.00 USD |
| `7D` | `0.0974` | 821,350.00 USD | 0.00 USD | 821,350.00 USD | 0.00 USD | 1,390.00 USD | 3,060.00 USD |
| `1D` | `0.0976` | 640,970.00 USD | 0.00 USD | 640,970.00 USD | 18,450.00 USD | 4,820.00 USD | 7,460.00 USD |
| `7D` | `0.0977` | 816,900.00 USD | 0.00 USD | 816,900.00 USD | 0.00 USD | 4,010.00 USD | 28,810.00 USD |
| `1D` | `0.0978` | 610,230.00 USD | 0.00 USD | 610,230.00 USD | 22,180.00 USD | 3,360.00 USD | 9,310.00 USD |
| `1D` | `0.0980` | 575,390.00 USD | 0.00 USD | 575,390.00 USD | 12,450.00 USD | 3,070.00 USD | 10,500.00 USD |
| `7D` | `0.0980` | 784,080.00 USD | 0.00 USD | 784,080.00 USD | 0.00 USD | 3,920.00 USD | 5,790.00 USD |
| `1D` | `0.0982` | 549,370.00 USD | 0.00 USD | 549,370.00 USD | 1,840.00 USD | 3,990.00 USD | 14,180.00 USD |
| `7D` | `0.0983` | 774,370.00 USD | 0.00 USD | 774,370.00 USD | 7,990.00 USD | 1,230.00 USD | 14,730.00 USD |
| `1D` | `0.0984` | 529,350.00 USD | 0.00 USD | 529,350.00 USD | 10,600.00 USD | 460.32 USD | 18,800.00 USD |
| `1D` | `0.0986` | 499,490.00 USD | 0.00 USD | 499,490.00 USD | 10,070.00 USD | 5,230.00 USD | 32,530.00 USD |
| `7D` | `0.0986` | 750,410.00 USD | 0.00 USD | 750,410.00 USD | 7,110.00 USD | 7,530.00 USD | 60,900.00 USD |
| `1D` | `0.0988` | 451,650.00 USD | 0.00 USD | 451,650.00 USD | 12,770.00 USD | 6,260.00 USD | 3,680.00 USD |
| `7D` | `0.0989` | 674,870.00 USD | 0.00 USD | 674,870.00 USD | 17,640.00 USD | 6,190.00 USD | 53,220.00 USD |
| `1D` | `0.0990` | 428,950.00 USD | 0.00 USD | 428,950.00 USD | 3,980.00 USD | 3,340.00 USD | 2,580.00 USD |
| `1D` | `0.0992` | 419,060.00 USD | 0.00 USD | 419,060.00 USD | 29,370.00 USD | 5,050.00 USD | 7,820.00 USD |
| `7D` | `0.0992` | 597,820.00 USD | 0.00 USD | 597,820.00 USD | 27,140.00 USD | 11,490.00 USD | 28,600.00 USD |
| `1D` | `0.0994` | 376,810.00 USD | 0.00 USD | 376,810.00 USD | 10,240.00 USD | 4,740.00 USD | 9,830.00 USD |
| `7D` | `0.0995` | 530,590.00 USD | 0.00 USD | 530,590.00 USD | 24,220.00 USD | 15,150.00 USD | 56,840.00 USD |
| `1D` | `0.0996` | 352,010.00 USD | 0.00 USD | 352,010.00 USD | 2,640.00 USD | 4,700.00 USD | 28,270.00 USD |
| `1D` | `0.0998` | 316,390.00 USD | 0.00 USD | 316,390.00 USD | 35,620.00 USD | 7,340.00 USD | 19,400.00 USD |
| `7D` | `0.0998` | 434,370.00 USD | 0.00 USD | 434,370.00 USD | 28,450.00 USD | 12,100.00 USD | 80,810.00 USD |
| `1D` | `0.1000` | 254,030.00 USD | 0.00 USD | 254,030.00 USD | 48,950.00 USD | 7,140.00 USD | 26,210.00 USD |
| `7D` | `0.1001` | 313,010.00 USD | 0.00 USD | 313,010.00 USD | 36,110.00 USD | 8,650.00 USD | 13,180.00 USD |
| `1D` | `0.1002` | 171,720.00 USD | 0.00 USD | 171,720.00 USD | 21,100.00 USD | 4,620.00 USD | 17,270.00 USD |
| `1D` | `0.1004` | 128,740.00 USD | 0.00 USD | 128,740.00 USD | 1,970.00 USD | 5,260.00 USD | 13,950.00 USD |
| `7D` | `0.1004` | 255,070.00 USD | 0.00 USD | 255,070.00 USD | 22,470.00 USD | 16,470.00 USD | 23,630.00 USD |
| `1D` | `0.1006` | 107,560.00 USD | 0.00 USD | 107,560.00 USD | 16,470.00 USD | 5,640.00 USD | 72,760.00 USD |
| `7D` | `0.1007` | 192,500.00 USD | 0.00 USD | 192,500.00 USD | 20,870.00 USD | 3,870.00 USD | 100,630.00 USD |
| `1D` | `0.1008` | 12,690.00 USD | 0.00 USD | 12,690.00 USD | 0.00 USD | 8,710.00 USD | 0.00 USD |
| `1D` | `0.1010` | 3,980.00 USD | 0.00 USD | 3,980.00 USD | 0.00 USD | 0.00 USD | 2,450.00 USD |
| `7D` | `0.1010` | 67,130.00 USD | 0.00 USD | 67,130.00 USD | 17,340.00 USD | 6,580.00 USD | 6,680.00 USD |
| `1D` | `0.1012` | 1,530.00 USD | 0.00 USD | 1,530.00 USD | 0.00 USD | 0.00 USD | 939.04 USD |
| `7D` | `0.1013` | 36,530.00 USD | 0.00 USD | 36,530.00 USD | 15,270.00 USD | 5,230.00 USD | 553.29 USD |
| `1D` | `0.1014` | 587.32 USD | 0.00 USD | 587.32 USD | 0.00 USD | 0.00 USD | 587.32 USD |
| `7D` | `0.1016` | 15,480.00 USD | 0.00 USD | 15,480.00 USD | 15,440.00 USD | 0.00 USD | 32.62 USD |
| `1D` | `0.1017` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1018` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1019` | 12,410.00 USD | 12,410.00 USD | 0.00 USD | 12,100.00 USD | 0.00 USD | 315.80 USD |
| `7D` | `0.1022` | 32,950.00 USD | 32,950.00 USD | 0.00 USD | 11,930.00 USD | 8,250.00 USD | 352.46 USD |
| `7D` | `0.1025` | 34,500.00 USD | 34,500.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1028` | 42,690.00 USD | 42,690.00 USD | 0.00 USD | 3,800.00 USD | 4,390.00 USD | 0.00 USD |
| `1D` | `0.1030` | 11,070.00 USD | 11,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,070.00 USD |
| `7D` | `0.1031` | 68,510.00 USD | 68,510.00 USD | 0.00 USD | 19,560.00 USD | 6,260.00 USD | 0.00 USD |
| `1D` | `0.1032` | 62,990.00 USD | 62,990.00 USD | 0.00 USD | 27,910.00 USD | 3,360.00 USD | 20,650.00 USD |
| `1D` | `0.1034` | 81,430.00 USD | 81,430.00 USD | 0.00 USD | 5,500.00 USD | 3,920.00 USD | 9,020.00 USD |
| `7D` | `0.1034` | 94,460.00 USD | 94,460.00 USD | 0.00 USD | 18,920.00 USD | 7,030.00 USD | 0.00 USD |
| `1D` | `0.1036` | 101,250.00 USD | 101,250.00 USD | 0.00 USD | 6,930.00 USD | 12,830.00 USD | 54.66 USD |
| `7D` | `0.1037` | 108,280.00 USD | 108,280.00 USD | 0.00 USD | 2,710.00 USD | 10,710.00 USD | 403.86 USD |
| `1D` | `0.1038` | 151,480.00 USD | 151,480.00 USD | 0.00 USD | 35,160.00 USD | 15,080.00 USD | 0.00 USD |
| `1D` | `0.1040` | 193,640.00 USD | 193,640.00 USD | 0.00 USD | 12,950.00 USD | 16,660.00 USD | 12,550.00 USD |
| `7D` | `0.1040` | 156,190.00 USD | 156,190.00 USD | 0.00 USD | 5,940.00 USD | 10,300.00 USD | 31,660.00 USD |
| `1D` | `0.1042` | 220,390.00 USD | 220,390.00 USD | 0.00 USD | 0.00 USD | 9,490.00 USD | 17,270.00 USD |
| `7D` | `0.1043` | 179,150.00 USD | 179,150.00 USD | 0.00 USD | 15,960.00 USD | 5,980.00 USD | 1,020.00 USD |
| `1D` | `0.1044` | 234,760.00 USD | 234,760.00 USD | 0.00 USD | 0.00 USD | 14,370.00 USD | 0.00 USD |
| `1D` | `0.1046` | 267,600.00 USD | 267,600.00 USD | 0.00 USD | 7,060.00 USD | 1,080.00 USD | 24,700.00 USD |
| `7D` | `0.1046` | 250,410.00 USD | 250,410.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD | 61,450.00 USD |
| `1D` | `0.1048` | 384,750.00 USD | 384,750.00 USD | 0.00 USD | 27,930.00 USD | 9,140.00 USD | 80,080.00 USD |
| `7D` | `0.1049` | 376,170.00 USD | 376,170.00 USD | 0.00 USD | 34,790.00 USD | 6,530.00 USD | 84,440.00 USD |
| `1D` | `0.1050` | 441,510.00 USD | 441,510.00 USD | 0.00 USD | 35,330.00 USD | 10,740.00 USD | 10,690.00 USD |
| `1D` | `0.1052` | 545,580.00 USD | 545,580.00 USD | 0.00 USD | 43,830.00 USD | 12,940.00 USD | 47,290.00 USD |
| `7D` | `0.1052` | 554,500.00 USD | 554,500.00 USD | 0.00 USD | 28,200.00 USD | 24,160.00 USD | 125,970.00 USD |
| `1D` | `0.1054` | 697,580.00 USD | 697,580.00 USD | 0.00 USD | 59,720.00 USD | 20,100.00 USD | 72,180.00 USD |
| `7D` | `0.1055` | 933,130.00 USD | 933,130.00 USD | 0.00 USD | 122,840.00 USD | 44,430.00 USD | 211,360.00 USD |
| `1D` | `0.1056` | 795,770.00 USD | 795,770.00 USD | 0.00 USD | 25,000.00 USD | 29,020.00 USD | 44,170.00 USD |
| `1D` | `0.1058` | 907,190.00 USD | 907,190.00 USD | 0.00 USD | 30,300.00 USD | 2,830.00 USD | 78,300.00 USD |
| `7D` | `0.1058` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 105,620.00 USD | 56,540.00 USD | 189,220.00 USD |
| `1D` | `0.1060` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 44,890.00 USD | 1,890.00 USD | 54,750.00 USD |
| `7D` | `0.1061` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 75,540.00 USD | 72,260.00 USD | 117,750.00 USD |
| `1D` | `0.1062` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 31,870.00 USD | 2,030.00 USD | 78,510.00 USD |
| `1D` | `0.1064` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD | 51,350.00 USD |
| `7D` | `0.1064` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 52,580.00 USD | 192,910.00 USD |
| `1D` | `0.1066` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD | 31,530.00 USD |
| `7D` | `0.1067` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 51,740.00 USD | 156,260.00 USD |
| `1D` | `0.1068` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 4,700.00 USD | 2,620.00 USD | 55,720.00 USD |
| `1D` | `0.1070` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 8,170.00 USD | 7,280.00 USD | 51,460.00 USD |
| `7D` | `0.1070` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 57,770.00 USD | 134,960.00 USD |
| `1D` | `0.1072` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 236.90 USD |
| `7D` | `0.1073` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 17,700.00 USD | 22.94 USD |
| `1D` | `0.1074` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101.24 USD |
| `1D` | `0.1076` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 137.18 USD |
| `7D` | `0.1076` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,650.00 USD |
| `1D` | `0.1078` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,190.00 USD |
| `7D` | `0.1079` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 79.36 USD |
| `1D` | `0.1082` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 5,910.00 USD | 21.66 USD |
| `7D` | `0.1082` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1084` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 7,990.00 USD | 0.00 USD | 35,870.00 USD |
| `7D` | `0.1085` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 113.96 USD |
| `1D` | `0.1086` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 4,220.00 USD | 2,240.00 USD | 72,930.00 USD |
| `1D` | `0.1088` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 44,230.00 USD | 0.00 USD | 8,060.00 USD |
| `7D` | `0.1088` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 5,290.00 USD | 0.00 USD | 171.42 USD |
| `1D` | `0.1090` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 43,010.00 USD | 0.00 USD | 124.57 USD |
| `7D` | `0.1091` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 9,060.00 USD |
| `1D` | `0.1092` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 10,290.00 USD | 0.00 USD | 29.91 USD |
| `1D` | `0.1094` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 13,100.00 USD | 0.00 USD | 14,050.00 USD |
| `7D` | `0.1094` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,990.00 USD |
| `1D` | `0.1096` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 7,670.00 USD |
| `7D` | `0.1097` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1098` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 13,380.00 USD | 3,910.00 USD | 22,790.00 USD |
| `1D` | `0.1100` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 2,820.00 USD | 4,290.00 USD |
| `7D` | `0.1100` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 21,930.00 USD |
| `1D` | `0.1102` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 4,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1103` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1104` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 6,920.00 USD | 10,390.00 USD | 0.00 USD |
| `1D` | `0.1106` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 12,720.00 USD | 30,820.00 USD |
| `7D` | `0.1106` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 22,880.00 USD | 15,950.00 USD |
| `1D` | `0.1108` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 5,220.00 USD | 1,120.00 USD | 15,630.00 USD |
| `7D` | `0.1109` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD |
| `1D` | `0.1112` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 10,780.00 USD | 0.00 USD | 96.09 USD |
| `7D` | `0.1112` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD |
| `1D` | `0.1114` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 15,810.00 USD | 5,880.00 USD | 39,070.00 USD |
| `1D` | `0.1116` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 4,760.00 USD | 12,550.00 USD | 6,930.00 USD |
| `1D` | `0.1118` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 25,510.00 USD | 20,030.00 USD | 57,050.00 USD |
| `7D` | `0.1118` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD |
| `1D` | `0.1120` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 27,100.00 USD | 9,370.00 USD | 9,830.00 USD |
| `7D` | `0.1121` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 17,760.00 USD | 0.00 USD | 38,370.00 USD |
| `1D` | `0.1122` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 23,990.00 USD | 5,240.00 USD | 15,000.00 USD |
| `1D` | `0.1124` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 17,850.00 USD | 6,120.00 USD | 8,600.00 USD |
| `7D` | `0.1124` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD |
| `1D` | `0.1126` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 9,370.00 USD | 11,410.00 USD | 17,020.00 USD |
| `7D` | `0.1127` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD |
| `1D` | `0.1128` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 10,120.00 USD | 0.00 USD | 11,120.00 USD |
| `1D` | `0.1130` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 7,970.00 USD | 2,000.00 USD | 16,330.00 USD |
| `7D` | `0.1130` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,260.00 USD |
| `1D` | `0.1132` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 19,390.00 USD | 18,950.00 USD | 16,110.00 USD |
| `7D` | `0.1133` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD |
| `1D` | `0.1134` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 4,040.00 USD | 12,980.00 USD | 13,830.00 USD |
| `1D` | `0.1136` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 787.70 USD | 4,130.00 USD |
| `7D` | `0.1136` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,180.00 USD |
| `1D` | `0.1138` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 856.93 USD | 14,270.00 USD |
| `7D` | `0.1139` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,080.00 USD |
| `1D` | `0.1140` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 7,800.00 USD | 0.00 USD | 6,050.00 USD |
| `1D` | `0.1142` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 24,760.00 USD | 17,100.00 USD | 22,170.00 USD |
| `7D` | `0.1142` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,540.00 USD |
| `1D` | `0.1144` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 9,940.00 USD | 21,970.00 USD | 31,580.00 USD |
| `7D` | `0.1145` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 16,540.00 USD | 2,730.00 USD | 219,700.00 USD |
| `1D` | `0.1146` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 5,090.00 USD | 10,830.00 USD | 30,120.00 USD |
| `1D` | `0.1148` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 33,430.00 USD | 3,280.00 USD | 30,510.00 USD |
| `7D` | `0.1148` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 175,990.00 USD |
| `1D` | `0.1150` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 19,260.00 USD | 13,020.00 USD | 21,660.00 USD |
| `7D` | `0.1151` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 103,130.00 USD | 4,210.00 USD | 163,670.00 USD |
| `1D` | `0.1152` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 30,190.00 USD | 17,470.00 USD | 59,670.00 USD |
| `1D` | `0.1153` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 6,400.00 USD | 4,560.00 USD | 23,220.00 USD |
| `7D` | `0.1154` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 243,190.00 USD | 26,970.00 USD | 195,400.00 USD |
| `7D` | `0.1157` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 188,950.00 USD | 25,290.00 USD | 98,460.00 USD |
| `7D` | `0.1160` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 139,350.00 USD | 32,830.00 USD | 109,430.00 USD |
| `7D` | `0.1163` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 142,050.00 USD | 28,590.00 USD | 112,510.00 USD |
| `7D` | `0.1166` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 130,810.00 USD | 46,040.00 USD | 42,160.00 USD |
| `7D` | `0.1169` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 82,770.00 USD | 26,150.00 USD | 113,000.00 USD |
| `7D` | `0.1172` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 64,270.00 USD | 14,930.00 USD | 48,790.00 USD |
| `7D` | `0.1175` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 72,770.00 USD | 17,930.00 USD | 82,130.00 USD |
| `7D` | `0.1178` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 89,510.00 USD | 23,660.00 USD | 55,540.00 USD |
| `7D` | `0.1181` | 5,830,000.00 USD | 5,830,000.00 USD | 0.00 USD | 32,770.00 USD | 23,410.00 USD | 29,950.00 USD |
| `7D` | `0.1184` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 11,640.00 USD | 5,170.00 USD | 47,690.00 USD |
| `7D` | `0.1187` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 5,620.00 USD | 17,120.00 USD | 54,940.00 USD |
| `7D` | `0.1190` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 29,530.00 USD | 29,230.00 USD | 86,470.00 USD |
| `7D` | `0.1193` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 41,630.00 USD | 1,160.00 USD | 38,400.00 USD |
| `7D` | `0.1196` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 17,970.00 USD | 1,780.00 USD | 40,520.00 USD |
| `7D` | `0.1199` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 9,100.00 USD | 13,190.00 USD | 68,070.00 USD |
| `7D` | `0.1202` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 138,430.00 USD | 21,430.00 USD | 32,640.00 USD |
| `7D` | `0.1205` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 132,960.00 USD | 72,910.00 USD | 130,960.00 USD |
| `7D` | `0.1208` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 39,480.00 USD | 25,720.00 USD | 66,490.00 USD |
| `7D` | `0.1211` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 72,500.00 USD | 25,920.00 USD | 111,240.00 USD |
| `7D` | `0.1214` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 23,920.00 USD | 19,420.00 USD | 76,190.00 USD |
| `7D` | `0.1217` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 24,400.00 USD | 6,160.00 USD | 18,240.00 USD |
| `7D` | `0.1220` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 45,700.00 USD | 10,970.00 USD | 54,570.00 USD |
| `7D` | `0.1223` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 76,930.00 USD | 24,740.00 USD | 45,750.00 USD |
| `7D` | `0.1226` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 54,940.00 USD | 27,490.00 USD | 5,240.00 USD |
| `7D` | `0.1229` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 71,850.00 USD | 38,040.00 USD | 73,960.00 USD |
| `7D` | `0.1232` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 67,800.00 USD | 28,560.00 USD | 68,230.00 USD |
| `7D` | `0.1235` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 15,040.00 USD | 5,390.00 USD | 17,120.00 USD |
| `7D` | `0.1238` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 8,310.00 USD | 3,610.00 USD | 3,140.00 USD |
| `7D` | `0.1241` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 11,380.00 USD | 1,380.00 USD | 7,050.00 USD |
| `7D` | `0.1244` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 26,540.00 USD | 8,130.00 USD | 9,630.00 USD |
| `7D` | `0.1247` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 7,900.00 USD | 12,590.00 USD | 15,210.00 USD |
| `7D` | `0.1250` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 8,540.00 USD | 4,990.00 USD | 5,660.00 USD |
| `7D` | `0.1253` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | 13,860.00 USD |
| `7D` | `0.1256` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 11,990.00 USD | 11,420.00 USD | 131.34 USD |
| `7D` | `0.1259` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 5,870.00 USD | 1,190.00 USD | 172.63 USD |
| `7D` | `0.1262` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | 3,520.00 USD |
| `7D` | `0.1265` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 2,710.00 USD | 0.00 USD | 7,340.00 USD |
| `7D` | `0.1268` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,950.00 USD |
| `7D` | `0.1271` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 5,940.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1274` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 36.76 USD |
| `7D` | `0.1277` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9.84 USD |
| `7D` | `0.1280` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,380.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `64.44M` | Total OI Tokens: `630,647,294.2 OP`
  * 1h OI Change: `-1.23%` | 4h OI Change: `-11.10%` | 24h OI Change: `-16.10%`
  * Exchange Breakdown: Binance=`14.55M` | Bybit=`13.01M` | OKX=`3.64M` | Hyperliquid=`3.33M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-3.43K` | Last 24h: `270.64` | Last 3d: `-2.23K` | Last 7d: `-15.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0311%` | **USDT OKX** | `-0.0058%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0032%` |
| **USDT MEXC** | `-0.0308%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0056%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `47.34%` | `52.66%` | `0.90` | 1,840,000.00 USD |
| `15M` | `Binance` | `55.17%` | `44.83%` | `1.23` | 652,740.00 USD |
| `15M` | `OKX` | `35.97%` | `64.03%` | `0.56` | 118,060.00 USD |
| `15M` | `Bybit` | `55.85%` | `44.15%` | `1.27` | 207,100.00 USD |
| `15M` | `KuCoin` | `39.38%` | `60.62%` | `0.65` | 5,690.00 USD |
| `15M` | `Gate` | `47.33%` | `52.67%` | `0.90` | 30,890.00 USD |
| `15M` | `Bitget` | `55.4%` | `44.6%` | `1.24` | 18,380.00 USD |
| `15M` | `BingX` | `9.04%` | `90.96%` | `0.10` | 266,190.00 USD |
| `15M` | `MEXC` | `32.76%` | `67.24%` | `0.49` | 46,380.00 USD |
| `15M` | `Bitunix` | `46.03%` | `53.97%` | `0.85` | 12,340.00 USD |
| `15M` | `Hyperliquid` | `65.92%` | `34.08%` | `1.93` | 131,760.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.02%` | `48.98%` | `1.04` | 288,600.00 USD |
| `15M` | `Crypto.com` | `100%` | `0%` | `1.00` | 0.80 USD |
| `15M` | `WhiteBIT` | `87.33%` | `12.67%` | `6.89` | 50,830.00 USD |
| `15M` | `HTX` | `94.28%` | `5.72%` | `16.48` | 294.03 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `6.54%` | `93.46%` | `0.07` | 544.11 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 6.19 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `5.79%` | `94.21%` | `0.06` | 6,680.00 USD |
| `15M` | `Whale Positions` | `55.17%` | `44.83%` | `1.23` | 652,740.00 USD |
| `15M` | `Global Accounts` | `47.34%` | `52.66%` | `0.90` | 1,840,000.00 USD |
| `1H` | `OP` | `50.54%` | `49.46%` | `1.02` | 10,920,000.00 USD |
| `1H` | `Binance` | `48.14%` | `51.86%` | `0.93` | 4,530,000.00 USD |
| `1H` | `OKX` | `46.95%` | `53.05%` | `0.89` | 980,190.00 USD |
| `1H` | `Bybit` | `53.51%` | `46.49%` | `1.15` | 945,930.00 USD |
| `1H` | `KuCoin` | `50.5%` | `49.5%` | `1.02` | 713,060.00 USD |
| `1H` | `Gate` | `40.2%` | `59.8%` | `0.67` | 248,320.00 USD |
| `1H` | `Bitget` | `47.58%` | `52.42%` | `0.91` | 336,380.00 USD |
| `1H` | `BingX` | `74.02%` | `25.98%` | `2.85` | 1,190,000.00 USD |
| `1H` | `MEXC` | `47.91%` | `52.09%` | `0.92` | 540,440.00 USD |
| `1H` | `Bitunix` | `22.72%` | `77.28%` | `0.29` | 302,290.00 USD |
| `1H` | `Hyperliquid` | `29.18%` | `70.82%` | `0.41` | 330,280.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.41%` | `49.59%` | `1.02` | 311,820.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `59.83%` | `40.17%` | `1.49` | 445,720.00 USD |
| `1H` | `HTX` | `32.97%` | `67.03%` | `0.49` | 1,290.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `50.95%` | `49.05%` | `1.04` | 31,350.00 USD |
| `1H` | `Aster` | `29.92%` | `70.08%` | `0.43` | 2,040.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `97.17%` | `2.83%` | `34.34` | 1,650.00 USD |
| `1H` | `Whale Positions` | `48.14%` | `51.86%` | `0.93` | 4,530,000.00 USD |
| `1H` | `Global Accounts` | `50.54%` | `49.46%` | `1.02` | 10,920,000.00 USD |
| `4H` | `OP` | `44.77%` | `55.23%` | `0.81` | 84,380,000.00 USD |
| `4H` | `Binance` | `45.1%` | `54.9%` | `0.82` | 35,520,000.00 USD |
| `4H` | `OKX` | `48.32%` | `51.68%` | `0.93` | 9,600,000.00 USD |
| `4H` | `Bybit` | `47.8%` | `52.2%` | `0.92` | 12,160,000.00 USD |
| `4H` | `KuCoin` | `49.01%` | `50.99%` | `0.96` | 2,900,000.00 USD |
| `4H` | `Gate` | `49.55%` | `50.45%` | `0.98` | 1,910,000.00 USD |
| `4H` | `Bitget` | `46.03%` | `53.97%` | `0.85` | 3,370,000.00 USD |
| `4H` | `BingX` | `29.07%` | `70.93%` | `0.41` | 6,570,000.00 USD |
| `4H` | `MEXC` | `41.89%` | `58.11%` | `0.72` | 4,370,000.00 USD |
| `4H` | `Bitunix` | `41.79%` | `58.21%` | `0.72` | 1,600,000.00 USD |
| `4H` | `Hyperliquid` | `43.06%` | `56.94%` | `0.76` | 2,070,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.89%` | `52.11%` | `0.92` | 1,280,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `48.48%` | `51.52%` | `0.94` | 2,410,000.00 USD |
| `4H` | `HTX` | `53.91%` | `46.09%` | `1.17` | 76,100.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `51.54%` | `48.46%` | `1.06` | 238,710.00 USD |
| `4H` | `Aster` | `55.93%` | `44.07%` | `1.27` | 217,100.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `20.63%` | `79.37%` | `0.26` | 80,960.00 USD |
| `4H` | `Whale Positions` | `45.1%` | `54.9%` | `0.82` | 35,520,000.00 USD |
| `4H` | `Global Accounts` | `44.77%` | `55.23%` | `0.81` | 84,380,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1014` | `0.1013` | `0.1014` | `0.1029` | `0.0990` | 5,717,098.88 USD | 2,672,854.06 USD | 3,044,244.81 USD | -371,390.75 USD | `-6.50%` | `7B / 23S` |
| `0:00 UTC` | `0.1025` | `0.1020` | `0.1025` | `0.1033` | `0.1007` | 1,857,629.60 USD | 946,076.57 USD | 911,553.03 USD | 34,523.54 USD | `+1.86%` | `19B / 6S` |
| `5:00 UTC` | `0.1043` | `0.1035` | `0.1043` | `0.1044` | `0.1026` | 1,285,007.52 USD | 601,525.80 USD | 683,481.72 USD | -81,955.93 USD | `-6.38%` | `27B / 29S` |
| `0:00 UTC` | `0.1037` | `0.1036` | `0.1037` | `0.1042` | `0.1024` | 770,717.58 USD | 335,049.96 USD | 435,667.63 USD | -100,617.67 USD | `-13.06%` | `27B / 45S` |
| `5:00 UTC` | `0.1020` | `0.1024` | `0.1020` | `0.1029` | `0.1018` | 520,168.37 USD | 289,498.79 USD | 230,669.58 USD | 58,829.21 USD | `+11.31%` | `26B / 7S` |
| `0:00 UTC` | `0.1013` | `0.1014` | `0.1013` | `0.1023` | `0.1003` | 969,689.66 USD | 453,817.19 USD | 515,872.47 USD | -62,055.28 USD | `-6.40%` | `8B / 16S` |
| `5:00 UTC` | `0.1025` | `0.1022` | `0.1025` | `0.1029` | `0.1010` | 722,088.27 USD | 440,195.52 USD | 281,892.75 USD | 158,302.78 USD | `+21.92%` | `56B / 16S` |
| `0:00 UTC` | `0.1023` | `0.1024` | `0.1023` | `0.1029` | `0.1019` | 576,770.99 USD | 307,354.68 USD | 269,416.31 USD | 37,938.37 USD | `+6.58%` | `13B / 12S` |
| `5:00 UTC` | `0.1017` | `0.1018` | `0.1017` | `0.1023` | `0.1012` | 643,660.47 USD | 377,656.89 USD | 266,003.58 USD | 111,653.31 USD | `+17.35%` | `25B / 10S` |
| `0:00 UTC` | `0.1016` | `0.1015` | `0.1016` | `0.1020` | `0.1010` | 602,325.33 USD | 318,507.42 USD | 283,817.91 USD | 34,689.51 USD | `+5.76%` | `12B / 10S` |

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
| `5m` | 31,080.00 USD | 3,320.00 USD | **`ACCUMULATION`** |
| `15m` | 70,240.00 USD | 55,980.00 USD | **`ACCUMULATION`** |
| `30m` | 90,980.00 USD | 104,470.00 USD | **`ACCUMULATION`** |
| `1h` | 285,300.00 USD | 300,160.00 USD | **`ACCUMULATION`** |
| `2h` | 396,480.00 USD | 160,940.00 USD | **`ACCUMULATION`** |
| `4h` | 140,950.00 USD | -2,630,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 114,830.00 USD | -2,790,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 124,410.00 USD | -2,710,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 317,410.00 USD | -2,480,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 241,020.00 USD | -4,560,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -2,170.00 USD | -12,050,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,290,000.00 USD | -80,810,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+31.08K` | 15m=`+70.24K` | 1h=`+285.30K` | 24h=`+241.02K`
* Futures Capital Netflows: 5m=`+3.32K` | 15m=`+55.98K` | 1h=`+300.16K` | 24h=`-4.56M`
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
  * `2026-10-30 04:15:34 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:40:34 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:34 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
