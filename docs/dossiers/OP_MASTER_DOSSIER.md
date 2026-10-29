# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-29 22:55:04 IST` (`2026-10-29 17:25:04 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1126` | `0.1127` | `0.1123` | `0.1123` | `746,349` | 83,957.23 USD | -6,079.56 USD | `-7.24%` | -617,870.78 USD | `+0.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.1123` | `0.1124` | `0.1119` | `0.1121` | `1,547,643` | 173,583.04 USD | -51,094.98 USD | `-29.44%` | -668,965.76 USD | `-0.79` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1121` | `0.1124` | `0.1120` | `0.1120` | `1,043,001` | 117,026.92 USD | -30,333.30 USD | `-25.92%` | -699,299.06 USD | `-0.39` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1130` | `0.1130` | `0.1127` | `0.1129` | `2,159,370` | 243,648.48 USD | -27,244.27 USD | `-11.18%` | -582,210.41 USD | `-0.49` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1129` | `0.1132` | `0.1123` | `0.1123` | `2,393,701` | 269,778.58 USD | -20,127.09 USD | `-7.46%` | -602,337.50 USD | `-0.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1123` | `0.1124` | `0.1119` | `0.1120` | `2,590,945` | 290,643.70 USD | -81,394.54 USD | `-28.00%` | -683,732.04 USD | `-1.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1119` | `0.1141` | `0.1117` | `0.1139` | `17,968,115` | 2,030,636.79 USD | 9,855.25 USD | `+0.49%` | -531,384.47 USD | `+0.23` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1140` | `0.1148` | `0.1126` | `0.1129` | `21,471,756` | 2,437,488.22 USD | -123,745.56 USD | `-5.08%` | -655,130.03 USD | `-0.29` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1129` | `0.1132` | `0.1119` | `0.1120` | `4,984,434` | 560,398.54 USD | -101,545.37 USD | `-18.12%` | -756,675.40 USD | `-0.17` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,229,700.44 USD | `+0.64` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -888,444.84 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1119` | `0.1120` | `26,456,402` | 2,997,910.51 USD | -225,267.19 USD | `-7.51%` | -1,113,712.03 USD | `-0.06` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1131` | `0.1136` | `0.1072` | `0.1085` | `76,338,549` | 8,353,905.81 USD | -1,528,374.61 USD | `-18.30%` | -1,480,991.26 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1085` | `0.1106` | `0.1071` | `0.1076` | `47,048,931` | 5,111,570.05 USD | 108,567.99 USD | `+2.12%` | -1,372,423.27 USD | `+0.75` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,229,700.44 USD | `+0.64` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -888,444.84 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1119` | `0.1120` | `26,456,402` | 2,997,910.51 USD | -225,267.19 USD | `-7.51%` | -1,113,712.03 USD | `-0.06` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:54:46 IST` |

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
| `Live` | `Long Liquidation` | `0.0385` | 196.31 USD | 242,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0405` | 183.72 USD | 241,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0475` | 3,600.00 USD | 241,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 3,460.00 USD | 238,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 829.69 USD | 234,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 1,100.00 USD | 233,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 353.81 USD | 232,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 501.98 USD | 232,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 100.24 USD | 231,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 518.48 USD | 231,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 1,920.00 USD | 231,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 762.48 USD | 229,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 1,440.00 USD | 228,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 23,910.00 USD | 227,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 41,550.00 USD | 203,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,300.00 USD | 161,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 1,020.00 USD | 159,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 5,720.00 USD | 158,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 878.62 USD | 152,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 1,320.00 USD | 151,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 223.98 USD | 150,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 1,560.00 USD | 150,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 2,240.00 USD | 148,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 883.92 USD | 146,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,120.00 USD | 145,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 443.16 USD | 142,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 16,670.00 USD | 141,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 69,120.00 USD | 125,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 4,640.00 USD | 56,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0959` | 4,310,000.00 USD | 4,310,000.00 USD | 4,610.00 USD | 1,140.00 USD | 16.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0961` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 8.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0963` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 1,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0965` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 34.36 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0965` | 419.87 USD | 51,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0967` | 4,300,000.00 USD | 4,300,000.00 USD | 3,770.00 USD | 2,660.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0969` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 2,810.00 USD | 9,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 2,000.00 USD | 18.27 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0973` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 1,390.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0975` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 1,160.00 USD | 4,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0975` | 12,670.00 USD | 51,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0977` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0979` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 1,530.00 USD | 5,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0981` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 5,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 4,250,000.00 USD | 4,250,000.00 USD | 7,990.00 USD | 1,230.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0985` | 4,230,000.00 USD | 4,230,000.00 USD | 7,110.00 USD | 0.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0985` | 19,960.00 USD | 38,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0987` | 4,220,000.00 USD | 4,220,000.00 USD | 5,390.00 USD | 9,190.00 USD | 37,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 4,170,000.00 USD | 4,170,000.00 USD | 12,260.00 USD | 4,520.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0991` | 4,120,000.00 USD | 4,120,000.00 USD | 14,350.00 USD | 10,350.00 USD | 13,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0993` | 4,080,000.00 USD | 4,080,000.00 USD | 23,920.00 USD | 10,140.00 USD | 24,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 4,030,000.00 USD | 4,030,000.00 USD | 13,090.00 USD | 6,160.00 USD | 25,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0997` | 3,980,000.00 USD | 3,980,000.00 USD | 21,100.00 USD | 5,500.00 USD | 30,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0999` | 3,920,000.00 USD | 3,920,000.00 USD | 14,230.00 USD | 6,540.00 USD | 18,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 3,880,000.00 USD | 3,880,000.00 USD | 29,230.00 USD | 3,010.00 USD | 10,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1003` | 3,840,000.00 USD | 3,840,000.00 USD | 8,010.00 USD | 7,060.00 USD | 5,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1005` | 3,820,000.00 USD | 3,820,000.00 USD | 25,070.00 USD | 11,000.00 USD | 18,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1005` | 427.25 USD | 18,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1007` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 833.73 USD | 906.44 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 3,770,000.00 USD | 3,770,000.00 USD | 10,260.00 USD | 2,280.00 USD | 14,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1009` | 2,070,000.00 USD | 2,070,000.00 USD | 2,320.00 USD | 2,390.00 USD | 23.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1009` | 3,740,000.00 USD | 3,740,000.00 USD | 15,320.00 USD | 3,070.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1011` | 2,060,000.00 USD | 2,060,000.00 USD | 1,570.00 USD | 1,240.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1011` | 3,720,000.00 USD | 3,720,000.00 USD | 4,430.00 USD | 4,720.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1013` | 2,050,000.00 USD | 2,050,000.00 USD | 4,900.00 USD | 1,490.00 USD | 645.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 3,700,000.00 USD | 3,700,000.00 USD | 12,870.00 USD | 4,030.00 USD | 3,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1015` | 2,050,000.00 USD | 2,050,000.00 USD | 2,790.00 USD | 1,830.00 USD | 4,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1015` | 3,680,000.00 USD | 3,680,000.00 USD | 6,830.00 USD | 965.35 USD | 2,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1015` | 622.37 USD | 17,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1017` | 2,040,000.00 USD | 2,040,000.00 USD | 1,660.00 USD | 4,600.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1017` | 3,670,000.00 USD | 3,670,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1019` | 2,030,000.00 USD | 2,030,000.00 USD | 6,600.00 USD | 3,420.00 USD | 5,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1019` | 3,650,000.00 USD | 3,650,000.00 USD | 9,260.00 USD | 5,790.00 USD | 13,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1021` | 2,010,000.00 USD | 2,010,000.00 USD | 2,580.00 USD | 1,320.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1021` | 3,620,000.00 USD | 3,620,000.00 USD | 7,900.00 USD | 3,270.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1023` | 2,000,000.00 USD | 2,000,000.00 USD | 4,600.00 USD | 2,120.00 USD | 4,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1023` | 3,600,000.00 USD | 3,600,000.00 USD | 4,030.00 USD | 4,990.00 USD | 14,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1025` | 1,990,000.00 USD | 1,990,000.00 USD | 855.19 USD | 2,500.00 USD | 3,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1025` | 3,580,000.00 USD | 3,580,000.00 USD | 1,550.00 USD | 0.00 USD | 5,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1025` | 17,360.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1027` | 1,980,000.00 USD | 1,980,000.00 USD | 2,780.00 USD | 1,590.00 USD | 1,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1027` | 3,570,000.00 USD | 3,570,000.00 USD | 2,250.00 USD | 2,580.00 USD | 282.63 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1029` | 1,980,000.00 USD | 1,980,000.00 USD | 4,340.00 USD | 705.79 USD | 6,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1029` | 3,560,000.00 USD | 3,560,000.00 USD | 7,420.00 USD | 3,000.00 USD | 470.94 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1031` | 1,960,000.00 USD | 1,960,000.00 USD | 11,600.00 USD | 3,910.00 USD | 8,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1031` | 3,550,000.00 USD | 3,550,000.00 USD | 13,690.00 USD | 5,070.00 USD | 10,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1033` | 1,940,000.00 USD | 1,940,000.00 USD | 8,760.00 USD | 2,790.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1033` | 3,520,000.00 USD | 3,520,000.00 USD | 3,880.00 USD | 2,640.00 USD | 15,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1035` | 1,920,000.00 USD | 1,920,000.00 USD | 7,450.00 USD | 6,850.00 USD | 10,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1035` | 3,500,000.00 USD | 3,500,000.00 USD | 2,710.00 USD | 9,400.00 USD | 16,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1037` | 1,890,000.00 USD | 1,890,000.00 USD | 2,220.00 USD | 13,000.00 USD | 9,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1037` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 19,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1039` | 1,870,000.00 USD | 1,870,000.00 USD | 3,660.00 USD | 1,730.00 USD | 11,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1039` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 5,170.00 USD | 75.48 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1041` | 1,850,000.00 USD | 1,850,000.00 USD | 7,790.00 USD | 6,910.00 USD | 13,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1041` | 3,450,000.00 USD | 3,450,000.00 USD | 5,940.00 USD | 2,910.00 USD | 10,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1043` | 1,830,000.00 USD | 1,830,000.00 USD | 17,650.00 USD | 5,650.00 USD | 7,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1043` | 3,430,000.00 USD | 3,430,000.00 USD | 15,960.00 USD | 5,980.00 USD | 20,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1045` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 2,600.00 USD | 6,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1045` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 3,830.00 USD | 15,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1047` | 1,790,000.00 USD | 1,790,000.00 USD | 4,610.00 USD | 2,610.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1047` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 1,720.00 USD | 22,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1049` | 1,760,000.00 USD | 1,760,000.00 USD | 21,050.00 USD | 2,430.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1049` | 3,340,000.00 USD | 3,340,000.00 USD | 34,790.00 USD | 4,810.00 USD | 35,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1051` | 1,730,000.00 USD | 1,730,000.00 USD | 16,410.00 USD | 10,250.00 USD | 25,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1051` | 3,270,000.00 USD | 3,270,000.00 USD | 17,290.00 USD | 11,500.00 USD | 48,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1053` | 1,670,000.00 USD | 1,670,000.00 USD | 29,550.00 USD | 7,780.00 USD | 27,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1053` | 3,190,000.00 USD | 3,190,000.00 USD | 47,580.00 USD | 29,800.00 USD | 95,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1055` | 1,610,000.00 USD | 1,610,000.00 USD | 21,850.00 USD | 20,210.00 USD | 32,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1055` | 3,020,000.00 USD | 3,020,000.00 USD | 50,090.00 USD | 27,290.00 USD | 121,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1057` | 1,530,000.00 USD | 1,530,000.00 USD | 23,460.00 USD | 25,970.00 USD | 44,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1057` | 2,820,000.00 USD | 2,820,000.00 USD | 44,200.00 USD | 43,030.00 USD | 74,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1059` | 1,440,000.00 USD | 1,440,000.00 USD | 17,220.00 USD | 21,000.00 USD | 52,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1059` | 2,660,000.00 USD | 2,660,000.00 USD | 92,510.00 USD | 49,670.00 USD | 114,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1061` | 1,350,000.00 USD | 1,350,000.00 USD | 15,660.00 USD | 9,870.00 USD | 50,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1061` | 2,400,000.00 USD | 2,400,000.00 USD | 38,260.00 USD | 28,780.00 USD | 76,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1063` | 1,270,000.00 USD | 1,270,000.00 USD | 53,680.00 USD | 14,600.00 USD | 51,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1063` | 2,260,000.00 USD | 2,260,000.00 USD | 92,290.00 USD | 38,330.00 USD | 148,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1065` | 1,150,000.00 USD | 1,150,000.00 USD | 9,490.00 USD | 15,010.00 USD | 13,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1065` | 1,980,000.00 USD | 1,980,000.00 USD | 84,890.00 USD | 21,040.00 USD | 85,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1067` | 1,120,000.00 USD | 1,120,000.00 USD | 10,260.00 USD | 13,310.00 USD | 21,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1067` | 1,790,000.00 USD | 1,790,000.00 USD | 97,290.00 USD | 34,000.00 USD | 68,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1069` | 1,070,000.00 USD | 1,070,000.00 USD | 22,050.00 USD | 6,620.00 USD | 43,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1069` | 1,590,000.00 USD | 1,590,000.00 USD | 76,900.00 USD | 32,620.00 USD | 67,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1071` | 999,570.00 USD | 999,570.00 USD | 48,660.00 USD | 4,860.00 USD | 16,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1071` | 1,410,000.00 USD | 1,410,000.00 USD | 119,440.00 USD | 27,240.00 USD | 42,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1073` | 929,840.00 USD | 929,840.00 USD | 8,740.00 USD | 10,680.00 USD | 20,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1073` | 1,220,000.00 USD | 1,220,000.00 USD | 58,480.00 USD | 17,700.00 USD | 84.54 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1075` | 889,520.00 USD | 889,520.00 USD | 16,520.00 USD | 4,720.00 USD | 18.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1075` | 1,140,000.00 USD | 1,140,000.00 USD | 8,720.00 USD | 3,500.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1077` | 868,260.00 USD | 868,260.00 USD | 3,180.00 USD | 10,810.00 USD | 14,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1079` | 840,220.00 USD | 840,220.00 USD | 9,370.00 USD | 11,900.00 USD | 25,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1079` | 1,130,000.00 USD | 1,130,000.00 USD | 128,090.00 USD | 18,520.00 USD | 110.55 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1081` | 793,180.00 USD | 793,180.00 USD | 17,730.00 USD | 7,210.00 USD | 49,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1081` | 984,920.00 USD | 984,920.00 USD | 205,390.00 USD | 11,660.00 USD | 28,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1083` | 718,270.00 USD | 718,270.00 USD | 30,270.00 USD | 5,440.00 USD | 30,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1083` | 739,030.00 USD | 739,030.00 USD | 94,800.00 USD | 2,110.00 USD | 42,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1085` | 651,630.00 USD | 651,630.00 USD | 16,830.00 USD | 13,850.00 USD | 65,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1085` | 599,720.00 USD | 599,720.00 USD | 15,920.00 USD | 4,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1087` | 555,930.00 USD | 555,930.00 USD | 26,790.00 USD | 6,720.00 USD | 33,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1087` | 579,600.00 USD | 579,600.00 USD | 42,890.00 USD | 6,210.00 USD | 45,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1089` | 489,300.00 USD | 489,300.00 USD | 32,000.00 USD | 13,380.00 USD | 18,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1089` | 485,450.00 USD | 485,450.00 USD | 5,290.00 USD | 9,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1091` | 425,840.00 USD | 425,840.00 USD | 29,660.00 USD | 4,610.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1091` | 471,040.00 USD | 471,040.00 USD | 16,310.00 USD | 3,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1093` | 383,400.00 USD | 383,400.00 USD | 15,480.00 USD | 3,890.00 USD | 8,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1093` | 450,940.00 USD | 450,940.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1095` | 355,530.00 USD | 355,530.00 USD | 0.00 USD | 0.00 USD | 5,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1095` | 442,210.00 USD | 442,210.00 USD | 18,840.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1097` | 419,840.00 USD | 419,840.00 USD | 0.00 USD | 2,970.00 USD | 21,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1099` | 350,080.00 USD | 350,080.00 USD | 9,980.00 USD | 10,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1099` | 395,270.00 USD | 395,270.00 USD | 0.00 USD | 7,010.00 USD | 25,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1101` | 329,280.00 USD | 329,280.00 USD | 0.00 USD | 0.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1103` | 318,470.00 USD | 318,470.00 USD | 23,720.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1103` | 363,200.00 USD | 363,200.00 USD | 27,370.00 USD | 4,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1105` | 288,670.00 USD | 288,670.00 USD | 0.00 USD | 10,880.00 USD | 7,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1105` | 331,380.00 USD | 331,380.00 USD | 0.00 USD | 10,030.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1107` | 270,550.00 USD | 270,550.00 USD | 4,910.00 USD | 12,720.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1107` | 311,640.00 USD | 311,640.00 USD | 0.00 USD | 12,510.00 USD | 10.82 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1109` | 217,180.00 USD | 217,180.00 USD | 22,960.00 USD | 0.00 USD | 16,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1109` | 299,110.00 USD | 299,110.00 USD | 40,420.00 USD | 12,430.00 USD | 34,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1111` | 177,900.00 USD | 177,900.00 USD | 4,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1111` | 211,630.00 USD | 211,630.00 USD | 10,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1113` | 173,560.00 USD | 173,560.00 USD | 19,470.00 USD | 3,630.00 USD | 41,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1113` | 201,040.00 USD | 201,040.00 USD | 0.00 USD | 0.00 USD | 57,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1115` | 108,540.00 USD | 108,540.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1115` | 143,550.00 USD | 143,550.00 USD | 0.00 USD | 0.00 USD | 53,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1117` | 103,770.00 USD | 103,770.00 USD | 0.00 USD | 24,680.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1117` | 89,950.00 USD | 89,950.00 USD | 0.00 USD | 22,780.00 USD | 23,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1119` | 48,050.00 USD | 48,050.00 USD | 16,250.00 USD | 5,030.00 USD | 26,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1119` | 43,600.00 USD | 43,600.00 USD | 13,220.00 USD | 7,050.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1121` | 15,500.00 USD | 15,500.00 USD | 0.00 USD | 0.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1121` | 31,000.00 USD | 31,000.00 USD | 0.00 USD | 0.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1121` | 12,530.00 USD | 12,530.00 USD | 0.00 USD | 0.00 USD | 12,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1123` | 71,800.00 USD | 71,800.00 USD | 29,460.00 USD | 11,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1123` | 44,690.00 USD | 44,690.00 USD | 0.00 USD | 18,520.00 USD | 26,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1123` | 89,390.00 USD | 89,390.00 USD | 0.00 USD | 18,520.00 USD | 26,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1125` | 85,300.00 USD | 85,300.00 USD | 0.00 USD | 13,480.00 USD | 26.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1125` | 118,280.00 USD | 118,280.00 USD | 0.00 USD | 0.00 USD | 28,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1129` | 118,300.00 USD | 118,300.00 USD | 0.00 USD | 0.00 USD | 14.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1131` | 90,240.00 USD | 90,240.00 USD | 0.00 USD | 4,870.00 USD | 68.06 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1133` | 109,070.00 USD | 109,070.00 USD | 0.00 USD | 18,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1135` | 110,150.00 USD | 110,150.00 USD | 0.00 USD | 1,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1135` | 123,820.00 USD | 123,820.00 USD | 0.00 USD | 5,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1137` | 111,040.00 USD | 111,040.00 USD | 0.00 USD | 856.93 USD | 40.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1137` | 124,020.00 USD | 124,020.00 USD | 0.00 USD | 0.00 USD | 208.30 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1139` | 119,890.00 USD | 119,890.00 USD | 0.00 USD | 0.00 USD | 8,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1139` | 124,050.00 USD | 124,050.00 USD | 0.00 USD | 0.00 USD | 21.32 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1141` | 131,480.00 USD | 131,480.00 USD | 8,780.00 USD | 2,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1141` | 136,000.00 USD | 136,000.00 USD | 4,360.00 USD | 0.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1143` | 169,560.00 USD | 169,560.00 USD | 11,570.00 USD | 18,560.00 USD | 7,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1143` | 210,330.00 USD | 210,330.00 USD | 0.00 USD | 0.00 USD | 74,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1145` | 225,700.00 USD | 225,700.00 USD | 8,350.00 USD | 10,790.00 USD | 37,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 361,870.00 USD | 361,870.00 USD | 10,360.00 USD | 0.00 USD | 141,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1147` | 266,100.00 USD | 266,100.00 USD | 8,840.00 USD | 4,840.00 USD | 26,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1147` | 506,450.00 USD | 506,450.00 USD | 9,880.00 USD | 0.00 USD | 134,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1149` | 335,280.00 USD | 335,280.00 USD | 35,170.00 USD | 0.00 USD | 34,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1149` | 589,800.00 USD | 589,800.00 USD | 10,560.00 USD | 0.00 USD | 72,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1151` | 417,700.00 USD | 417,700.00 USD | 18,640.00 USD | 14,620.00 USD | 49,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 814,940.00 USD | 814,940.00 USD | 92,570.00 USD | 4,210.00 USD | 128,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1153` | 539,270.00 USD | 539,270.00 USD | 30,670.00 USD | 28,670.00 USD | 62,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1153` | 1,100,000.00 USD | 1,100,000.00 USD | 147,450.00 USD | 8,400.00 USD | 132,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1155` | 651,840.00 USD | 651,840.00 USD | 45,040.00 USD | 25,230.00 USD | 42,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1155` | 1,400,000.00 USD | 1,400,000.00 USD | 149,360.00 USD | 37,390.00 USD | 105,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1157` | 732,910.00 USD | 732,910.00 USD | 35,770.00 USD | 11,110.00 USD | 34,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 1,620,000.00 USD | 1,620,000.00 USD | 174,080.00 USD | 3,760.00 USD | 48,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1159` | 797,420.00 USD | 797,420.00 USD | 27,270.00 USD | 12,000.00 USD | 25,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1159` | 1,790,000.00 USD | 1,790,000.00 USD | 105,000.00 USD | 12,710.00 USD | 48,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1161` | 868,760.00 USD | 868,760.00 USD | 30,570.00 USD | 6,970.00 USD | 33,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1161` | 2,070,000.00 USD | 2,070,000.00 USD | 146,810.00 USD | 37,250.00 USD | 99,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1163` | 918,970.00 USD | 918,970.00 USD | 18,210.00 USD | 14,540.00 USD | 17,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 2,220,000.00 USD | 2,220,000.00 USD | 66,560.00 USD | 11,460.00 USD | 68,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1165` | 949,590.00 USD | 949,590.00 USD | 14,300.00 USD | 12,660.00 USD | 3,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1165` | 2,350,000.00 USD | 2,350,000.00 USD | 68,620.00 USD | 35,720.00 USD | 27,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1167` | 988,750.00 USD | 988,750.00 USD | 15,040.00 USD | 17,950.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1167` | 2,490,000.00 USD | 2,490,000.00 USD | 79,610.00 USD | 21,620.00 USD | 41,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1169` | 1,030,000.00 USD | 1,030,000.00 USD | 16,040.00 USD | 4,020.00 USD | 18,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 2,660,000.00 USD | 2,660,000.00 USD | 65,340.00 USD | 14,840.00 USD | 86,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1171` | 1,050,000.00 USD | 1,050,000.00 USD | 17,090.00 USD | 4,520.00 USD | 4,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1171` | 2,760,000.00 USD | 2,760,000.00 USD | 57,350.00 USD | 11,370.00 USD | 35,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1173` | 1,090,000.00 USD | 1,090,000.00 USD | 14,960.00 USD | 8,910.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1173` | 2,850,000.00 USD | 2,850,000.00 USD | 40,860.00 USD | 9,190.00 USD | 36,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1175` | 1,140,000.00 USD | 1,140,000.00 USD | 11,510.00 USD | 17,150.00 USD | 24,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 2,960,000.00 USD | 2,960,000.00 USD | 38,840.00 USD | 12,300.00 USD | 58,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1177` | 1,190,000.00 USD | 1,190,000.00 USD | 19,300.00 USD | 8,560.00 USD | 16,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1177` | 3,060,000.00 USD | 3,060,000.00 USD | 33,330.00 USD | 20,350.00 USD | 44,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1179` | 1,230,000.00 USD | 1,230,000.00 USD | 19,180.00 USD | 5,840.00 USD | 14,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1179` | 3,160,000.00 USD | 3,160,000.00 USD | 66,670.00 USD | 10,940.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1181` | 1,260,000.00 USD | 1,260,000.00 USD | 15,480.00 USD | 6,030.00 USD | 15,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 3,220,000.00 USD | 3,220,000.00 USD | 22,290.00 USD | 15,780.00 USD | 17,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1183` | 1,280,000.00 USD | 1,280,000.00 USD | 7,310.00 USD | 1,400.00 USD | 9,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1183` | 3,260,000.00 USD | 3,260,000.00 USD | 4,040.00 USD | 1,800.00 USD | 39,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1185` | 1,310,000.00 USD | 1,310,000.00 USD | 8,760.00 USD | 7,830.00 USD | 13,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1185` | 3,290,000.00 USD | 3,290,000.00 USD | 3,880.00 USD | 5,130.00 USD | 22,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1187` | 1,340,000.00 USD | 1,340,000.00 USD | 11,520.00 USD | 8,520.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 3,340,000.00 USD | 3,340,000.00 USD | 5,620.00 USD | 15,370.00 USD | 31,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1189` | 1,350,000.00 USD | 1,350,000.00 USD | 4,220.00 USD | 3,060.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1189` | 3,390,000.00 USD | 3,390,000.00 USD | 27,240.00 USD | 15,060.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1191` | 1,370,000.00 USD | 1,370,000.00 USD | 4,940.00 USD | 6,690.00 USD | 3,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1191` | 3,540,000.00 USD | 3,540,000.00 USD | 22,650.00 USD | 15,330.00 USD | 109,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1193` | 1,380,000.00 USD | 1,380,000.00 USD | 4,720.00 USD | 2,080.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 3,570,000.00 USD | 3,570,000.00 USD | 21,260.00 USD | 0.00 USD | 9,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1195` | 1,390,000.00 USD | 1,390,000.00 USD | 9,550.00 USD | 3,210.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1195` | 3,610,000.00 USD | 3,610,000.00 USD | 11,190.00 USD | 1,780.00 USD | 29,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1197` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 1,040.00 USD | 57.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1197` | 3,640,000.00 USD | 3,640,000.00 USD | 6,780.00 USD | 10,800.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1199` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 3,050.00 USD | 3,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 3,720,000.00 USD | 3,720,000.00 USD | 9,100.00 USD | 0.00 USD | 64,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1201` | 1,420,000.00 USD | 1,420,000.00 USD | 6,460.00 USD | 1,070.00 USD | 8,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1201` | 3,880,000.00 USD | 3,880,000.00 USD | 114,140.00 USD | 16,380.00 USD | 29,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1203` | 1,430,000.00 USD | 1,430,000.00 USD | 5,670.00 USD | 769.98 USD | 2,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1203` | 3,980,000.00 USD | 3,980,000.00 USD | 70,770.00 USD | 29,250.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1205` | 1,430,000.00 USD | 1,430,000.00 USD | 2,250.00 USD | 1,910.00 USD | 745.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 4,250,000.00 USD | 4,250,000.00 USD | 86,480.00 USD | 48,720.00 USD | 128,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1207` | 1,440,000.00 USD | 1,440,000.00 USD | 4,610.00 USD | 524.23 USD | 4,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1207` | 4,340,000.00 USD | 4,340,000.00 USD | 12,460.00 USD | 19,400.00 USD | 59,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1209` | 1,450,000.00 USD | 1,450,000.00 USD | 636.93 USD | 3,080.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1209` | 4,540,000.00 USD | 4,540,000.00 USD | 85,160.00 USD | 19,340.00 USD | 94,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1211` | 1,460,000.00 USD | 1,460,000.00 USD | 3,340.00 USD | 3,880.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 4,610,000.00 USD | 4,610,000.00 USD | 27,400.00 USD | 16,260.00 USD | 29,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1213` | 1,470,000.00 USD | 1,470,000.00 USD | 2,360.00 USD | 1,220.00 USD | 10,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1213` | 4,680,000.00 USD | 4,680,000.00 USD | 23,920.00 USD | 26,740.00 USD | 24,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1215` | 1,480,000.00 USD | 1,480,000.00 USD | 1,650.00 USD | 0.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1215` | 4,760,000.00 USD | 4,760,000.00 USD | 5,900.00 USD | 6,620.00 USD | 59,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1217` | 1,490,000.00 USD | 1,490,000.00 USD | 1,330.00 USD | 624.33 USD | 7,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 4,810,000.00 USD | 4,810,000.00 USD | 18,490.00 USD | 23,600.00 USD | 11,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1219` | 1,500,000.00 USD | 1,500,000.00 USD | 2,320.00 USD | 718.82 USD | 9,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1219` | 4,880,000.00 USD | 4,880,000.00 USD | 26,700.00 USD | 5,500.00 USD | 35,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1221` | 1,510,000.00 USD | 1,510,000.00 USD | 1,450.00 USD | 3,590.00 USD | 1,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1221` | 4,960,000.00 USD | 4,960,000.00 USD | 47,890.00 USD | 21,770.00 USD | 18,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1223` | 1,520,000.00 USD | 1,520,000.00 USD | 4,190.00 USD | 668.73 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 5,150,000.00 USD | 5,150,000.00 USD | 103,180.00 USD | 36,290.00 USD | 48,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1225` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1225` | 5,230,000.00 USD | 5,230,000.00 USD | 46,760.00 USD | 26,800.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 16,000.00 USD | 16,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1227` | 1,520,000.00 USD | 1,520,000.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1227` | 5,390,000.00 USD | 5,390,000.00 USD | 68,750.00 USD | 31,790.00 USD | 58,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1229` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 403.62 USD | 1.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 5,560,000.00 USD | 5,560,000.00 USD | 87,270.00 USD | 40,000.00 USD | 43,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1231` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 430.11 USD | 793.30 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1231` | 5,650,000.00 USD | 5,650,000.00 USD | 29,380.00 USD | 31,660.00 USD | 30,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1233` | 1,520,000.00 USD | 1,520,000.00 USD | 2,320.00 USD | 2,390.00 USD | 0.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1233` | 5,760,000.00 USD | 5,760,000.00 USD | 57,130.00 USD | 13,020.00 USD | 40,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1235` | 1,530,000.00 USD | 1,530,000.00 USD | 1,570.00 USD | 1,240.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1235` | 5,790,000.00 USD | 5,790,000.00 USD | 10,950.00 USD | 6,400.00 USD | 9,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1237` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 763.58 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1237` | 5,810,000.00 USD | 5,810,000.00 USD | 4,080.00 USD | 9,720.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1239` | 1,540,000.00 USD | 1,540,000.00 USD | 4,900.00 USD | 724.40 USD | 587.65 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1239` | 5,820,000.00 USD | 5,820,000.00 USD | 8,780.00 USD | 1,270.00 USD | 208.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1241` | 1,550,000.00 USD | 1,550,000.00 USD | 2,790.00 USD | 1,830.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1241` | 5,840,000.00 USD | 5,840,000.00 USD | 6,830.00 USD | 9,690.00 USD | 2,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1243` | 1,560,000.00 USD | 1,560,000.00 USD | 1,660.00 USD | 4,600.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1243` | 5,860,000.00 USD | 5,860,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1245` | 1,580,000.00 USD | 1,580,000.00 USD | 6,600.00 USD | 3,420.00 USD | 5,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1245` | 5,910,000.00 USD | 5,910,000.00 USD | 26,080.00 USD | 11,090.00 USD | 13,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1247` | 1,580,000.00 USD | 1,580,000.00 USD | 2,580.00 USD | 1,320.00 USD | 4,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1247` | 5,960,000.00 USD | 5,960,000.00 USD | 24,470.00 USD | 19,030.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1249` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 1,190.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1249` | 5,980,000.00 USD | 5,980,000.00 USD | 13,440.00 USD | 5,480.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1251` | 1,600,000.00 USD | 1,600,000.00 USD | 4,600.00 USD | 932.33 USD | 3,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1251` | 6,010,000.00 USD | 6,010,000.00 USD | 7,660.00 USD | 5,070.00 USD | 11,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1253` | 1,600,000.00 USD | 1,600,000.00 USD | 855.19 USD | 2,500.00 USD | 3,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1253` | 6,040,000.00 USD | 6,040,000.00 USD | 11,420.00 USD | 2,100.00 USD | 14,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1255` | 1,610,000.00 USD | 1,610,000.00 USD | 2,780.00 USD | 1,590.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1255` | 6,050,000.00 USD | 6,050,000.00 USD | 2,250.00 USD | 13,990.00 USD | 33.05 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1257` | 1,610,000.00 USD | 1,610,000.00 USD | 1,140.00 USD | 0.00 USD | 0.01 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1257` | 6,070,000.00 USD | 6,070,000.00 USD | 15,610.00 USD | 5,200.00 USD | 88.39 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1259` | 1,610,000.00 USD | 1,610,000.00 USD | 962.72 USD | 1,690.00 USD | 12.41 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1259` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 138.58 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1261` | 1,610,000.00 USD | 1,610,000.00 USD | 2,110.00 USD | 0.00 USD | 5.73 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1261` | 6,080,000.00 USD | 6,080,000.00 USD | 4,270.00 USD | 0.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1263` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1265` | 1,620,000.00 USD | 1,620,000.00 USD | 1,300.00 USD | 694.78 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1265` | 6,090,000.00 USD | 6,090,000.00 USD | 2,710.00 USD | 0.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1267` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 2,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1269` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 16.21 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1271` | 6,100,000.00 USD | 6,100,000.00 USD | 5,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1272` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 0.00 USD | 10.64 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1355` | 1,330.00 USD | 17,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1515` | 15,150.00 USD | 32,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1555` | 6,210.00 USD | 38,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1565` | 550.61 USD | 39,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1645` | 19,830.00 USD | 59,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1695` | 169.25 USD | 59,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1865` | 167.85 USD | 59,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1915` | 925.65 USD | 60,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0385` | 242,040.00 USD | 0.00 USD | 196.31 USD | `-65.88%` | `5,098.90` |
| `Live` | `Long` | `0.0405` | 241,840.00 USD | 0.00 USD | 183.72 USD | `-64.11%` | `4,536.30` |
| `Live` | `Long` | `0.0475` | 241,660.00 USD | 0.00 USD | 3,600.00 USD | `-57.90%` | `75,790.10` |
| `Live` | `Long` | `0.0545` | 238,060.00 USD | 0.00 USD | 3,460.00 USD | `-51.70%` | `63,403.00` |
| `Live` | `Long` | `0.0575` | 234,600.00 USD | 0.00 USD | 829.69 USD | `-49.04%` | `14,429.40` |
| `Live` | `Long` | `0.0615` | 233,770.00 USD | 0.00 USD | 1,100.00 USD | `-45.50%` | `17,943.80` |
| `Live` | `Long` | `0.0645` | 232,670.00 USD | 0.00 USD | 353.81 USD | `-42.84%` | `5,485.40` |
| `Live` | `Long` | `0.0655` | 232,320.00 USD | 0.00 USD | 501.98 USD | `-41.95%` | `7,663.80` |
| `Live` | `Long` | `0.0665` | 231,810.00 USD | 0.00 USD | 100.24 USD | `-41.07%` | `1,507.30` |
| `Live` | `Long` | `0.0675` | 231,710.00 USD | 0.00 USD | 518.48 USD | `-40.18%` | `7,681.20` |
| `Live` | `Long` | `0.0685` | 231,190.00 USD | 0.00 USD | 1,920.00 USD | `-39.29%` | `28,000.00` |
| `Live` | `Long` | `0.0695` | 229,280.00 USD | 0.00 USD | 762.48 USD | `-38.41%` | `10,971.00` |
| `Live` | `Long` | `0.0715` | 228,510.00 USD | 0.00 USD | 1,440.00 USD | `-36.64%` | `20,133.00` |
| `Live` | `Long` | `0.0725` | 227,070.00 USD | 0.00 USD | 23,910.00 USD | `-35.75%` | `329,855.60` |
| `Live` | `Long` | `0.0735` | 203,160.00 USD | 0.00 USD | 41,550.00 USD | `-34.86%` | `565,287.50` |
| `Live` | `Long` | `0.0745` | 161,610.00 USD | 0.00 USD | 2,300.00 USD | `-33.98%` | `30,851.90` |
| `Live` | `Long` | `0.0755` | 159,310.00 USD | 0.00 USD | 1,020.00 USD | `-33.09%` | `13,481.90` |
| `Live` | `Long` | `0.0765` | 158,300.00 USD | 0.00 USD | 5,720.00 USD | `-32.20%` | `74,826.10` |
| `Live` | `Long` | `0.0775` | 152,570.00 USD | 0.00 USD | 878.62 USD | `-31.32%` | `11,337.00` |
| `Live` | `Long` | `0.0795` | 151,690.00 USD | 0.00 USD | 1,320.00 USD | `-29.55%` | `16,641.80` |
| `Live` | `Long` | `0.0805` | 150,370.00 USD | 0.00 USD | 223.98 USD | `-28.66%` | `2,782.40` |
| `Live` | `Long` | `0.0815` | 150,150.00 USD | 0.00 USD | 1,560.00 USD | `-27.77%` | `19,181.40` |
| `Live` | `Long` | `0.0825` | 148,580.00 USD | 0.00 USD | 2,240.00 USD | `-26.89%` | `27,146.60` |
| `Live` | `Long` | `0.0875` | 146,340.00 USD | 0.00 USD | 883.92 USD | `-22.46%` | `10,101.90` |
| `Live` | `Long` | `0.0895` | 145,460.00 USD | 0.00 USD | 3,120.00 USD | `-20.68%` | `34,873.20` |
| `Live` | `Long` | `0.0905` | 142,340.00 USD | 0.00 USD | 443.16 USD | `-19.80%` | `4,896.80` |
| `Live` | `Long` | `0.0925` | 141,890.00 USD | 0.00 USD | 16,670.00 USD | `-18.03%` | `180,203.00` |
| `Live` | `Long` | `0.0945` | 125,230.00 USD | 0.00 USD | 69,120.00 USD | `-16.25%` | `731,405.60` |
| `Live` | `Long` | `0.0955` | 56,110.00 USD | 0.00 USD | 4,640.00 USD | `-15.37%` | `48,598.80` |
| `Live` | `Long` | `0.0965` | 51,470.00 USD | 0.00 USD | 419.87 USD | `-14.48%` | `4,351.00` |
| `Live` | `Long` | `0.0975` | 51,050.00 USD | 0.00 USD | 12,670.00 USD | `-13.59%` | `129,987.90` |
| `Live` | `Long` | `0.0985` | 38,370.00 USD | 0.00 USD | 19,960.00 USD | `-12.71%` | `202,627.30` |
| `Live` | `Long` | `0.1005` | 18,410.00 USD | 0.00 USD | 427.25 USD | `-10.94%` | `4,251.20` |
| `Live` | `Long` | `0.1015` | 17,990.00 USD | 0.00 USD | 622.37 USD | `-10.05%` | `6,131.70` |
| `Live` | `Long` | `0.1025` | 17,360.00 USD | 0.00 USD | 17,360.00 USD | `-9.16%` | `169,408.50` |
| `Live` | `Short` | `0.1225` | 16,000.00 USD | 16,000.00 USD | 0.00 USD | `+8.56%` | `130,621.40` |
| `Live` | `Short` | `0.1355` | 17,330.00 USD | 1,330.00 USD | 0.00 USD | `+20.08%` | `9,843.80` |
| `Live` | `Short` | `0.1515` | 32,490.00 USD | 15,150.00 USD | 0.00 USD | `+34.26%` | `100,000.40` |
| `Live` | `Short` | `0.1555` | 38,690.00 USD | 6,210.00 USD | 0.00 USD | `+37.81%` | `39,929.50` |
| `Live` | `Short` | `0.1565` | 39,240.00 USD | 550.61 USD | 0.00 USD | `+38.69%` | `3,518.30` |
| `Live` | `Short` | `0.1645` | 59,080.00 USD | 19,830.00 USD | 0.00 USD | `+45.78%` | `120,571.30` |
| `Live` | `Short` | `0.1695` | 59,250.00 USD | 169.25 USD | 0.00 USD | `+50.21%` | `998.50` |
| `Live` | `Short` | `0.1865` | 59,420.00 USD | 167.85 USD | 0.00 USD | `+65.28%` | `900.00` |
| `Live` | `Short` | `0.1915` | 60,340.00 USD | 925.65 USD | 0.00 USD | `+69.71%` | `4,833.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0635` | 178,950.00 USD | 0.00 USD | 1,140.00 USD | `-43.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 177,810.00 USD | 0.00 USD | 773.46 USD | `-37.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 177,040.00 USD | 0.00 USD | 592.27 USD | `-36.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 176,440.00 USD | 0.00 USD | 755.00 USD | `-33.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0805` | 175,690.00 USD | 0.00 USD | 411.06 USD | `-28.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0815` | 175,280.00 USD | 0.00 USD | 183.49 USD | `-27.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0835` | 175,090.00 USD | 0.00 USD | 456.70 USD | `-26.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 174,640.00 USD | 0.00 USD | 631.58 USD | `-24.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 174,010.00 USD | 0.00 USD | 653.74 USD | `-21.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0915` | 173,350.00 USD | 0.00 USD | 1,460.00 USD | `-18.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 171,890.00 USD | 0.00 USD | 485.13 USD | `-16.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0975` | 171,400.00 USD | 0.00 USD | 720.22 USD | `-13.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0985` | 170,680.00 USD | 0.00 USD | 931.75 USD | `-12.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0995` | 169,750.00 USD | 0.00 USD | 801.64 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 168,950.00 USD | 0.00 USD | 1,470.00 USD | `-10.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1015` | 167,480.00 USD | 0.00 USD | 903.42 USD | `-10.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 166,570.00 USD | 0.00 USD | 780.70 USD | `-9.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1035` | 165,790.00 USD | 0.00 USD | 4,650.00 USD | `-8.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1045` | 161,140.00 USD | 0.00 USD | 18,950.00 USD | `-7.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1055` | 142,190.00 USD | 0.00 USD | 7,770.00 USD | `-6.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1065` | 134,420.00 USD | 0.00 USD | 109,280.00 USD | `-5.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 25,140.00 USD | 0.00 USD | 21,670.00 USD | `-4.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 3,480.00 USD | 0.00 USD | 150.04 USD | `-3.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1095` | 3,330.00 USD | 0.00 USD | 639.36 USD | `-2.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 2,690.00 USD | 0.00 USD | 162.59 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 2,520.00 USD | 0.00 USD | 839.64 USD | `-1.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1125` | 1,680.00 USD | 0.00 USD | 1,680.00 USD | `-0.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1135` | 116.27 USD | 116.27 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1145` | 250.88 USD | 134.61 USD | 0.00 USD | `+1.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 740.85 USD | 489.97 USD | 0.00 USD | `+2.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1165` | 1,210.00 USD | 466.94 USD | 0.00 USD | `+3.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1175` | 28,730.00 USD | 27,530.00 USD | 0.00 USD | `+4.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1185` | 29,790.00 USD | 1,050.00 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1195` | 44,420.00 USD | 14,640.00 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1205` | 44,820.00 USD | 398.42 USD | 0.00 USD | `+6.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1225` | 45,800.00 USD | 980.00 USD | 0.00 USD | `+8.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1235` | 58,780.00 USD | 12,980.00 USD | 0.00 USD | `+9.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1255` | 63,160.00 USD | 4,380.00 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1265` | 73,620.00 USD | 10,460.00 USD | 0.00 USD | `+12.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1275` | 74,110.00 USD | 492.06 USD | 0.00 USD | `+12.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1305` | 74,560.00 USD | 444.24 USD | 0.00 USD | `+15.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1315` | 106,120.00 USD | 31,560.00 USD | 0.00 USD | `+16.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1335` | 107,430.00 USD | 1,310.00 USD | 0.00 USD | `+18.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1345` | 111,580.00 USD | 4,150.00 USD | 0.00 USD | `+19.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1365` | 122,280.00 USD | 10,690.00 USD | 0.00 USD | `+20.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1405` | 135,380.00 USD | 13,110.00 USD | 0.00 USD | `+24.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1425` | 135,490.00 USD | 102.22 USD | 0.00 USD | `+26.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1435` | 142,660.00 USD | 7,180.00 USD | 0.00 USD | `+27.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1485` | 145,310.00 USD | 2,650.00 USD | 0.00 USD | `+31.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1495` | 146,100.00 USD | 792.53 USD | 0.00 USD | `+32.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1525` | 149,870.00 USD | 3,770.00 USD | 0.00 USD | `+35.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 150,050.00 USD | 184.49 USD | 0.00 USD | `+37.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 156,770.00 USD | 6,720.00 USD | 0.00 USD | `+38.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 156,990.00 USD | 219.81 USD | 0.00 USD | `+39.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 157,270.00 USD | 277.62 USD | 0.00 USD | `+44.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 159,060.00 USD | 1,800.00 USD | 0.00 USD | `+50.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 159,280.00 USD | 216.55 USD | 0.00 USD | `+54.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 159,400.00 USD | 117.26 USD | 0.00 USD | `+75.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 179,930.00 USD | 20,530.00 USD | 0.00 USD | `+77.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 180,130.00 USD | 201.02 USD | 0.00 USD | `+98.07%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0959` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 4,610.00 USD | 1,140.00 USD | 16.87 USD |
| `7D` | `0.0961` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 8.04 USD |
| `7D` | `0.0963` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 1,210.00 USD |
| `7D` | `0.0965` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 34.36 USD |
| `7D` | `0.0967` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 3,770.00 USD | 2,660.00 USD | 2,830.00 USD |
| `7D` | `0.0969` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 0.00 USD | 2,810.00 USD | 9,390.00 USD |
| `7D` | `0.0971` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 0.00 USD | 2,000.00 USD | 18.27 USD |
| `7D` | `0.0973` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 0.00 USD | 1,390.00 USD | 2,830.00 USD |
| `7D` | `0.0975` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 0.00 USD | 1,160.00 USD | 4,230.00 USD |
| `7D` | `0.0977` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD |
| `7D` | `0.0979` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 0.00 USD | 1,530.00 USD | 5,680.00 USD |
| `7D` | `0.0981` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 5,910.00 USD |
| `7D` | `0.0983` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 7,990.00 USD | 1,230.00 USD | 8,920.00 USD |
| `7D` | `0.0985` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 7,110.00 USD | 0.00 USD | 6,320.00 USD |
| `7D` | `0.0987` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 5,390.00 USD | 9,190.00 USD | 37,300.00 USD |
| `7D` | `0.0989` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 12,260.00 USD | 4,520.00 USD | 27,230.00 USD |
| `7D` | `0.0991` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 14,350.00 USD | 10,350.00 USD | 13,610.00 USD |
| `7D` | `0.0993` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 23,920.00 USD | 10,140.00 USD | 24,010.00 USD |
| `7D` | `0.0995` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 13,090.00 USD | 6,160.00 USD | 25,240.00 USD |
| `7D` | `0.0997` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 21,100.00 USD | 5,500.00 USD | 30,040.00 USD |
| `7D` | `0.0999` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 14,230.00 USD | 6,540.00 USD | 18,810.00 USD |
| `7D` | `0.1001` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 29,230.00 USD | 3,010.00 USD | 10,890.00 USD |
| `7D` | `0.1003` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 8,010.00 USD | 7,060.00 USD | 5,200.00 USD |
| `7D` | `0.1005` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 25,070.00 USD | 11,000.00 USD | 18,400.00 USD |
| `1D` | `0.1007` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 0.00 USD | 833.73 USD | 906.44 USD |
| `7D` | `0.1007` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 10,260.00 USD | 2,280.00 USD | 14,080.00 USD |
| `1D` | `0.1009` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 2,320.00 USD | 2,390.00 USD | 23.95 USD |
| `7D` | `0.1009` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 15,320.00 USD | 3,070.00 USD | 6,790.00 USD |
| `1D` | `0.1011` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 1,570.00 USD | 1,240.00 USD | 3,420.00 USD |
| `7D` | `0.1011` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 4,430.00 USD | 4,720.00 USD | 9,190.00 USD |
| `1D` | `0.1013` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 4,900.00 USD | 1,490.00 USD | 645.83 USD |
| `7D` | `0.1013` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 12,870.00 USD | 4,030.00 USD | 3,000.00 USD |
| `1D` | `0.1015` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 2,790.00 USD | 1,830.00 USD | 4,320.00 USD |
| `7D` | `0.1015` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 6,830.00 USD | 965.35 USD | 2,380.00 USD |
| `1D` | `0.1017` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 1,660.00 USD | 4,600.00 USD | 7,590.00 USD |
| `7D` | `0.1017` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,750.00 USD |
| `1D` | `0.1019` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 6,600.00 USD | 3,420.00 USD | 5,520.00 USD |
| `7D` | `0.1019` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 9,260.00 USD | 5,790.00 USD | 13,210.00 USD |
| `1D` | `0.1021` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 2,580.00 USD | 1,320.00 USD | 4,780.00 USD |
| `7D` | `0.1021` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 7,900.00 USD | 3,270.00 USD | 7,130.00 USD |
| `1D` | `0.1023` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 4,600.00 USD | 2,120.00 USD | 4,710.00 USD |
| `7D` | `0.1023` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 4,030.00 USD | 4,990.00 USD | 14,420.00 USD |
| `1D` | `0.1025` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 855.19 USD | 2,500.00 USD | 3,640.00 USD |
| `7D` | `0.1025` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 1,550.00 USD | 0.00 USD | 5,700.00 USD |
| `1D` | `0.1027` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 2,780.00 USD | 1,590.00 USD | 1,680.00 USD |
| `7D` | `0.1027` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 2,250.00 USD | 2,580.00 USD | 282.63 USD |
| `1D` | `0.1029` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 4,340.00 USD | 705.79 USD | 6,340.00 USD |
| `7D` | `0.1029` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 7,420.00 USD | 3,000.00 USD | 470.94 USD |
| `1D` | `0.1031` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 11,600.00 USD | 3,910.00 USD | 8,120.00 USD |
| `7D` | `0.1031` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 13,690.00 USD | 5,070.00 USD | 10,770.00 USD |
| `1D` | `0.1033` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 8,760.00 USD | 2,790.00 USD | 10,490.00 USD |
| `7D` | `0.1033` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 3,880.00 USD | 2,640.00 USD | 15,060.00 USD |
| `1D` | `0.1035` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 7,450.00 USD | 6,850.00 USD | 10,270.00 USD |
| `7D` | `0.1035` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 2,710.00 USD | 9,400.00 USD | 16,090.00 USD |
| `1D` | `0.1037` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 2,220.00 USD | 13,000.00 USD | 9,270.00 USD |
| `7D` | `0.1037` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 19,550.00 USD |
| `1D` | `0.1039` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 3,660.00 USD | 1,730.00 USD | 11,870.00 USD |
| `7D` | `0.1039` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 0.00 USD | 5,170.00 USD | 75.48 USD |
| `1D` | `0.1041` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 7,790.00 USD | 6,910.00 USD | 13,290.00 USD |
| `7D` | `0.1041` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 5,940.00 USD | 2,910.00 USD | 10,730.00 USD |
| `1D` | `0.1043` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 17,650.00 USD | 5,650.00 USD | 7,850.00 USD |
| `7D` | `0.1043` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 15,960.00 USD | 5,980.00 USD | 20,830.00 USD |
| `1D` | `0.1045` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 0.00 USD | 2,600.00 USD | 6,180.00 USD |
| `7D` | `0.1045` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 0.00 USD | 3,830.00 USD | 15,260.00 USD |
| `1D` | `0.1047` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 4,610.00 USD | 2,610.00 USD | 16,590.00 USD |
| `7D` | `0.1047` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 0.00 USD | 1,720.00 USD | 22,670.00 USD |
| `1D` | `0.1049` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 21,050.00 USD | 2,430.00 USD | 10,910.00 USD |
| `7D` | `0.1049` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 34,790.00 USD | 4,810.00 USD | 35,700.00 USD |
| `1D` | `0.1051` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 16,410.00 USD | 10,250.00 USD | 25,550.00 USD |
| `7D` | `0.1051` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 17,290.00 USD | 11,500.00 USD | 48,410.00 USD |
| `1D` | `0.1053` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 29,550.00 USD | 7,780.00 USD | 27,430.00 USD |
| `7D` | `0.1053` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 47,580.00 USD | 29,800.00 USD | 95,890.00 USD |
| `1D` | `0.1055` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 21,850.00 USD | 20,210.00 USD | 32,950.00 USD |
| `7D` | `0.1055` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 50,090.00 USD | 27,290.00 USD | 121,900.00 USD |
| `1D` | `0.1057` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 23,460.00 USD | 25,970.00 USD | 44,760.00 USD |
| `7D` | `0.1057` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 44,200.00 USD | 43,030.00 USD | 74,340.00 USD |
| `1D` | `0.1059` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 17,220.00 USD | 21,000.00 USD | 52,170.00 USD |
| `7D` | `0.1059` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 92,510.00 USD | 49,670.00 USD | 114,280.00 USD |
| `1D` | `0.1061` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 15,660.00 USD | 9,870.00 USD | 50,440.00 USD |
| `7D` | `0.1061` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 38,260.00 USD | 28,780.00 USD | 76,280.00 USD |
| `1D` | `0.1063` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 53,680.00 USD | 14,600.00 USD | 51,580.00 USD |
| `7D` | `0.1063` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 92,290.00 USD | 38,330.00 USD | 148,620.00 USD |
| `1D` | `0.1065` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 9,490.00 USD | 15,010.00 USD | 13,580.00 USD |
| `7D` | `0.1065` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 84,890.00 USD | 21,040.00 USD | 85,890.00 USD |
| `1D` | `0.1067` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 10,260.00 USD | 13,310.00 USD | 21,390.00 USD |
| `7D` | `0.1067` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 97,290.00 USD | 34,000.00 USD | 68,010.00 USD |
| `1D` | `0.1069` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 22,050.00 USD | 6,620.00 USD | 43,200.00 USD |
| `7D` | `0.1069` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 76,900.00 USD | 32,620.00 USD | 67,130.00 USD |
| `1D` | `0.1071` | 999,570.00 USD | 0.00 USD | 999,570.00 USD | 48,660.00 USD | 4,860.00 USD | 16,220.00 USD |
| `7D` | `0.1071` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 119,440.00 USD | 27,240.00 USD | 42,580.00 USD |
| `1D` | `0.1073` | 929,840.00 USD | 0.00 USD | 929,840.00 USD | 8,740.00 USD | 10,680.00 USD | 20,900.00 USD |
| `7D` | `0.1073` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 58,480.00 USD | 17,700.00 USD | 84.54 USD |
| `1D` | `0.1075` | 889,520.00 USD | 0.00 USD | 889,520.00 USD | 16,520.00 USD | 4,720.00 USD | 18.60 USD |
| `7D` | `0.1075` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 8,720.00 USD | 3,500.00 USD | 29.20 USD |
| `1D` | `0.1077` | 868,260.00 USD | 0.00 USD | 868,260.00 USD | 3,180.00 USD | 10,810.00 USD | 14,050.00 USD |
| `1D` | `0.1079` | 840,220.00 USD | 0.00 USD | 840,220.00 USD | 9,370.00 USD | 11,900.00 USD | 25,770.00 USD |
| `7D` | `0.1079` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 128,090.00 USD | 18,520.00 USD | 110.55 USD |
| `1D` | `0.1081` | 793,180.00 USD | 0.00 USD | 793,180.00 USD | 17,730.00 USD | 7,210.00 USD | 49,980.00 USD |
| `7D` | `0.1081` | 984,920.00 USD | 0.00 USD | 984,920.00 USD | 205,390.00 USD | 11,660.00 USD | 28,830.00 USD |
| `1D` | `0.1083` | 718,270.00 USD | 0.00 USD | 718,270.00 USD | 30,270.00 USD | 5,440.00 USD | 30,920.00 USD |
| `7D` | `0.1083` | 739,030.00 USD | 0.00 USD | 739,030.00 USD | 94,800.00 USD | 2,110.00 USD | 42,410.00 USD |
| `1D` | `0.1085` | 651,630.00 USD | 0.00 USD | 651,630.00 USD | 16,830.00 USD | 13,850.00 USD | 65,020.00 USD |
| `7D` | `0.1085` | 599,720.00 USD | 0.00 USD | 599,720.00 USD | 15,920.00 USD | 4,200.00 USD | 0.00 USD |
| `1D` | `0.1087` | 555,930.00 USD | 0.00 USD | 555,930.00 USD | 26,790.00 USD | 6,720.00 USD | 33,120.00 USD |
| `7D` | `0.1087` | 579,600.00 USD | 0.00 USD | 579,600.00 USD | 42,890.00 USD | 6,210.00 USD | 45,050.00 USD |
| `1D` | `0.1089` | 489,300.00 USD | 0.00 USD | 489,300.00 USD | 32,000.00 USD | 13,380.00 USD | 18,080.00 USD |
| `7D` | `0.1089` | 485,450.00 USD | 0.00 USD | 485,450.00 USD | 5,290.00 USD | 9,110.00 USD | 0.00 USD |
| `1D` | `0.1091` | 425,840.00 USD | 0.00 USD | 425,840.00 USD | 29,660.00 USD | 4,610.00 USD | 8,180.00 USD |
| `7D` | `0.1091` | 471,040.00 USD | 0.00 USD | 471,040.00 USD | 16,310.00 USD | 3,800.00 USD | 0.00 USD |
| `1D` | `0.1093` | 383,400.00 USD | 0.00 USD | 383,400.00 USD | 15,480.00 USD | 3,890.00 USD | 8,500.00 USD |
| `7D` | `0.1093` | 450,940.00 USD | 0.00 USD | 450,940.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD |
| `1D` | `0.1095` | 355,530.00 USD | 0.00 USD | 355,530.00 USD | 0.00 USD | 0.00 USD | 5,440.00 USD |
| `7D` | `0.1095` | 442,210.00 USD | 0.00 USD | 442,210.00 USD | 18,840.00 USD | 3,530.00 USD | 0.00 USD |
| `7D` | `0.1097` | 419,840.00 USD | 0.00 USD | 419,840.00 USD | 0.00 USD | 2,970.00 USD | 21,590.00 USD |
| `1D` | `0.1099` | 350,080.00 USD | 0.00 USD | 350,080.00 USD | 9,980.00 USD | 10,820.00 USD | 0.00 USD |
| `7D` | `0.1099` | 395,270.00 USD | 0.00 USD | 395,270.00 USD | 0.00 USD | 7,010.00 USD | 25,060.00 USD |
| `1D` | `0.1101` | 329,280.00 USD | 0.00 USD | 329,280.00 USD | 0.00 USD | 0.00 USD | 10,820.00 USD |
| `1D` | `0.1103` | 318,470.00 USD | 0.00 USD | 318,470.00 USD | 23,720.00 USD | 0.00 USD | 6,070.00 USD |
| `7D` | `0.1103` | 363,200.00 USD | 0.00 USD | 363,200.00 USD | 27,370.00 USD | 4,460.00 USD | 0.00 USD |
| `1D` | `0.1105` | 288,670.00 USD | 0.00 USD | 288,670.00 USD | 0.00 USD | 10,880.00 USD | 7,240.00 USD |
| `7D` | `0.1105` | 331,380.00 USD | 0.00 USD | 331,380.00 USD | 0.00 USD | 10,030.00 USD | 9,710.00 USD |
| `1D` | `0.1107` | 270,550.00 USD | 0.00 USD | 270,550.00 USD | 4,910.00 USD | 12,720.00 USD | 35,750.00 USD |
| `7D` | `0.1107` | 311,640.00 USD | 0.00 USD | 311,640.00 USD | 0.00 USD | 12,510.00 USD | 10.82 USD |
| `1D` | `0.1109` | 217,180.00 USD | 0.00 USD | 217,180.00 USD | 22,960.00 USD | 0.00 USD | 16,330.00 USD |
| `7D` | `0.1109` | 299,110.00 USD | 0.00 USD | 299,110.00 USD | 40,420.00 USD | 12,430.00 USD | 34,640.00 USD |
| `1D` | `0.1111` | 177,900.00 USD | 0.00 USD | 177,900.00 USD | 4,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1111` | 211,630.00 USD | 0.00 USD | 211,630.00 USD | 10,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1113` | 173,560.00 USD | 0.00 USD | 173,560.00 USD | 19,470.00 USD | 3,630.00 USD | 41,930.00 USD |
| `7D` | `0.1113` | 201,040.00 USD | 0.00 USD | 201,040.00 USD | 0.00 USD | 0.00 USD | 57,490.00 USD |
| `1D` | `0.1115` | 108,540.00 USD | 0.00 USD | 108,540.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1115` | 143,550.00 USD | 0.00 USD | 143,550.00 USD | 0.00 USD | 0.00 USD | 53,600.00 USD |
| `1D` | `0.1117` | 103,770.00 USD | 0.00 USD | 103,770.00 USD | 0.00 USD | 24,680.00 USD | 31,040.00 USD |
| `7D` | `0.1117` | 89,950.00 USD | 0.00 USD | 89,950.00 USD | 0.00 USD | 22,780.00 USD | 23,580.00 USD |
| `1D` | `0.1119` | 48,050.00 USD | 0.00 USD | 48,050.00 USD | 16,250.00 USD | 5,030.00 USD | 26,780.00 USD |
| `7D` | `0.1119` | 43,600.00 USD | 0.00 USD | 43,600.00 USD | 13,220.00 USD | 7,050.00 USD | 10,800.00 USD |
| `1D` | `0.1121` | 15,500.00 USD | 15,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,500.00 USD |
| `1D` | `0.1121` | 31,000.00 USD | 31,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,500.00 USD |
| `7D` | `0.1121` | 12,530.00 USD | 0.00 USD | 12,530.00 USD | 0.00 USD | 0.00 USD | 12,530.00 USD |
| `1D` | `0.1123` | 71,800.00 USD | 71,800.00 USD | 0.00 USD | 29,460.00 USD | 11,340.00 USD | 0.00 USD |
| `7D` | `0.1123` | 44,690.00 USD | 44,690.00 USD | 0.00 USD | 0.00 USD | 18,520.00 USD | 26,180.00 USD |
| `7D` | `0.1123` | 89,390.00 USD | 89,390.00 USD | 0.00 USD | 0.00 USD | 18,520.00 USD | 26,180.00 USD |
| `1D` | `0.1125` | 85,300.00 USD | 85,300.00 USD | 0.00 USD | 0.00 USD | 13,480.00 USD | 26.51 USD |
| `7D` | `0.1125` | 118,280.00 USD | 118,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,900.00 USD |
| `7D` | `0.1129` | 118,300.00 USD | 118,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14.44 USD |
| `1D` | `0.1131` | 90,240.00 USD | 90,240.00 USD | 0.00 USD | 0.00 USD | 4,870.00 USD | 68.06 USD |
| `1D` | `0.1133` | 109,070.00 USD | 109,070.00 USD | 0.00 USD | 0.00 USD | 18,820.00 USD | 0.00 USD |
| `1D` | `0.1135` | 110,150.00 USD | 110,150.00 USD | 0.00 USD | 0.00 USD | 1,080.00 USD | 0.00 USD |
| `7D` | `0.1135` | 123,820.00 USD | 123,820.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 0.00 USD |
| `1D` | `0.1137` | 111,040.00 USD | 111,040.00 USD | 0.00 USD | 0.00 USD | 856.93 USD | 40.44 USD |
| `7D` | `0.1137` | 124,020.00 USD | 124,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 208.30 USD |
| `1D` | `0.1139` | 119,890.00 USD | 119,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,850.00 USD |
| `7D` | `0.1139` | 124,050.00 USD | 124,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21.32 USD |
| `1D` | `0.1141` | 131,480.00 USD | 131,480.00 USD | 0.00 USD | 8,780.00 USD | 2,800.00 USD | 0.00 USD |
| `7D` | `0.1141` | 136,000.00 USD | 136,000.00 USD | 0.00 USD | 4,360.00 USD | 0.00 USD | 7,590.00 USD |
| `1D` | `0.1143` | 169,560.00 USD | 169,560.00 USD | 0.00 USD | 11,570.00 USD | 18,560.00 USD | 7,950.00 USD |
| `7D` | `0.1143` | 210,330.00 USD | 210,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 74,330.00 USD |
| `1D` | `0.1145` | 225,700.00 USD | 225,700.00 USD | 0.00 USD | 8,350.00 USD | 10,790.00 USD | 37,000.00 USD |
| `7D` | `0.1145` | 361,870.00 USD | 361,870.00 USD | 0.00 USD | 10,360.00 USD | 0.00 USD | 141,180.00 USD |
| `1D` | `0.1147` | 266,100.00 USD | 266,100.00 USD | 0.00 USD | 8,840.00 USD | 4,840.00 USD | 26,720.00 USD |
| `7D` | `0.1147` | 506,450.00 USD | 506,450.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 134,700.00 USD |
| `1D` | `0.1149` | 335,280.00 USD | 335,280.00 USD | 0.00 USD | 35,170.00 USD | 0.00 USD | 34,010.00 USD |
| `7D` | `0.1149` | 589,800.00 USD | 589,800.00 USD | 0.00 USD | 10,560.00 USD | 0.00 USD | 72,790.00 USD |
| `1D` | `0.1151` | 417,700.00 USD | 417,700.00 USD | 0.00 USD | 18,640.00 USD | 14,620.00 USD | 49,170.00 USD |
| `7D` | `0.1151` | 814,940.00 USD | 814,940.00 USD | 0.00 USD | 92,570.00 USD | 4,210.00 USD | 128,360.00 USD |
| `1D` | `0.1153` | 539,270.00 USD | 539,270.00 USD | 0.00 USD | 30,670.00 USD | 28,670.00 USD | 62,220.00 USD |
| `7D` | `0.1153` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 147,450.00 USD | 8,400.00 USD | 132,330.00 USD |
| `1D` | `0.1155` | 651,840.00 USD | 651,840.00 USD | 0.00 USD | 45,040.00 USD | 25,230.00 USD | 42,290.00 USD |
| `7D` | `0.1155` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 149,360.00 USD | 37,390.00 USD | 105,730.00 USD |
| `1D` | `0.1157` | 732,910.00 USD | 732,910.00 USD | 0.00 USD | 35,770.00 USD | 11,110.00 USD | 34,190.00 USD |
| `7D` | `0.1157` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 174,080.00 USD | 3,760.00 USD | 48,310.00 USD |
| `1D` | `0.1159` | 797,420.00 USD | 797,420.00 USD | 0.00 USD | 27,270.00 USD | 12,000.00 USD | 25,240.00 USD |
| `7D` | `0.1159` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 105,000.00 USD | 12,710.00 USD | 48,850.00 USD |
| `1D` | `0.1161` | 868,760.00 USD | 868,760.00 USD | 0.00 USD | 30,570.00 USD | 6,970.00 USD | 33,810.00 USD |
| `7D` | `0.1161` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 146,810.00 USD | 37,250.00 USD | 99,780.00 USD |
| `1D` | `0.1163` | 918,970.00 USD | 918,970.00 USD | 0.00 USD | 18,210.00 USD | 14,540.00 USD | 17,460.00 USD |
| `7D` | `0.1163` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 66,560.00 USD | 11,460.00 USD | 68,950.00 USD |
| `1D` | `0.1165` | 949,590.00 USD | 949,590.00 USD | 0.00 USD | 14,300.00 USD | 12,660.00 USD | 3,660.00 USD |
| `7D` | `0.1165` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 68,620.00 USD | 35,720.00 USD | 27,170.00 USD |
| `1D` | `0.1167` | 988,750.00 USD | 988,750.00 USD | 0.00 USD | 15,040.00 USD | 17,950.00 USD | 6,170.00 USD |
| `7D` | `0.1167` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 79,610.00 USD | 21,620.00 USD | 41,210.00 USD |
| `1D` | `0.1169` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 16,040.00 USD | 4,020.00 USD | 18,190.00 USD |
| `7D` | `0.1169` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 65,340.00 USD | 14,840.00 USD | 86,480.00 USD |
| `1D` | `0.1171` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 17,090.00 USD | 4,520.00 USD | 4,580.00 USD |
| `7D` | `0.1171` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 57,350.00 USD | 11,370.00 USD | 35,340.00 USD |
| `1D` | `0.1173` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 14,960.00 USD | 8,910.00 USD | 11,440.00 USD |
| `7D` | `0.1173` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 40,860.00 USD | 9,190.00 USD | 36,600.00 USD |
| `1D` | `0.1175` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 11,510.00 USD | 17,150.00 USD | 24,360.00 USD |
| `7D` | `0.1175` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 38,840.00 USD | 12,300.00 USD | 58,820.00 USD |
| `1D` | `0.1177` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 19,300.00 USD | 8,560.00 USD | 16,660.00 USD |
| `7D` | `0.1177` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 33,330.00 USD | 20,350.00 USD | 44,230.00 USD |
| `1D` | `0.1179` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 19,180.00 USD | 5,840.00 USD | 14,510.00 USD |
| `7D` | `0.1179` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 66,670.00 USD | 10,940.00 USD | 23,970.00 USD |
| `1D` | `0.1181` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 15,480.00 USD | 6,030.00 USD | 15,010.00 USD |
| `7D` | `0.1181` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 22,290.00 USD | 15,780.00 USD | 17,490.00 USD |
| `1D` | `0.1183` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 7,310.00 USD | 1,400.00 USD | 9,080.00 USD |
| `7D` | `0.1183` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 4,040.00 USD | 1,800.00 USD | 39,420.00 USD |
| `1D` | `0.1185` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 8,760.00 USD | 7,830.00 USD | 13,370.00 USD |
| `7D` | `0.1185` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 3,880.00 USD | 5,130.00 USD | 22,400.00 USD |
| `1D` | `0.1187` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 11,520.00 USD | 8,520.00 USD | 11,670.00 USD |
| `7D` | `0.1187` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 5,620.00 USD | 15,370.00 USD | 31,880.00 USD |
| `1D` | `0.1189` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 4,220.00 USD | 3,060.00 USD | 4,390.00 USD |
| `7D` | `0.1189` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 27,240.00 USD | 15,060.00 USD | 3,230.00 USD |
| `1D` | `0.1191` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 4,940.00 USD | 6,690.00 USD | 3,510.00 USD |
| `7D` | `0.1191` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 22,650.00 USD | 15,330.00 USD | 109,520.00 USD |
| `1D` | `0.1193` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 4,720.00 USD | 2,080.00 USD | 3,810.00 USD |
| `7D` | `0.1193` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 21,260.00 USD | 0.00 USD | 9,060.00 USD |
| `1D` | `0.1195` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 9,550.00 USD | 3,210.00 USD | 2,780.00 USD |
| `7D` | `0.1195` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 11,190.00 USD | 1,780.00 USD | 29,710.00 USD |
| `1D` | `0.1197` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 1,040.00 USD | 57.42 USD |
| `7D` | `0.1197` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 6,780.00 USD | 10,800.00 USD | 13,950.00 USD |
| `1D` | `0.1199` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 3,050.00 USD | 3,080.00 USD |
| `7D` | `0.1199` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 9,100.00 USD | 0.00 USD | 64,660.00 USD |
| `1D` | `0.1201` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 6,460.00 USD | 1,070.00 USD | 8,070.00 USD |
| `7D` | `0.1201` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 114,140.00 USD | 16,380.00 USD | 29,080.00 USD |
| `1D` | `0.1203` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 5,670.00 USD | 769.98 USD | 2,710.00 USD |
| `7D` | `0.1203` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 70,770.00 USD | 29,250.00 USD | 6,320.00 USD |
| `1D` | `0.1205` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 2,250.00 USD | 1,910.00 USD | 745.16 USD |
| `7D` | `0.1205` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 86,480.00 USD | 48,720.00 USD | 128,300.00 USD |
| `1D` | `0.1207` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 4,610.00 USD | 524.23 USD | 4,050.00 USD |
| `7D` | `0.1207` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 12,460.00 USD | 19,400.00 USD | 59,560.00 USD |
| `1D` | `0.1209` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 636.93 USD | 3,080.00 USD | 2,240.00 USD |
| `7D` | `0.1209` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 85,160.00 USD | 19,340.00 USD | 94,230.00 USD |
| `1D` | `0.1211` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 3,340.00 USD | 3,880.00 USD | 4,040.00 USD |
| `7D` | `0.1211` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 27,400.00 USD | 16,260.00 USD | 29,750.00 USD |
| `1D` | `0.1213` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 2,360.00 USD | 1,220.00 USD | 10,440.00 USD |
| `7D` | `0.1213` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 23,920.00 USD | 26,740.00 USD | 24,080.00 USD |
| `1D` | `0.1215` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD | 4,220.00 USD |
| `7D` | `0.1215` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 5,900.00 USD | 6,620.00 USD | 59,080.00 USD |
| `1D` | `0.1217` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 1,330.00 USD | 624.33 USD | 7,740.00 USD |
| `7D` | `0.1217` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 18,490.00 USD | 23,600.00 USD | 11,070.00 USD |
| `1D` | `0.1219` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 2,320.00 USD | 718.82 USD | 9,020.00 USD |
| `7D` | `0.1219` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 26,700.00 USD | 5,500.00 USD | 35,100.00 USD |
| `1D` | `0.1221` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 1,450.00 USD | 3,590.00 USD | 1,610.00 USD |
| `7D` | `0.1221` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 47,890.00 USD | 21,770.00 USD | 18,940.00 USD |
| `1D` | `0.1223` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 4,190.00 USD | 668.73 USD | 4,930.00 USD |
| `7D` | `0.1223` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 103,180.00 USD | 36,290.00 USD | 48,480.00 USD |
| `1D` | `0.1225` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1225` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 46,760.00 USD | 26,800.00 USD | 5,300.00 USD |
| `1D` | `0.1227` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1227` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 68,750.00 USD | 31,790.00 USD | 58,740.00 USD |
| `1D` | `0.1229` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 403.62 USD | 1.91 USD |
| `7D` | `0.1229` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 87,270.00 USD | 40,000.00 USD | 43,190.00 USD |
| `1D` | `0.1231` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 430.11 USD | 793.30 USD |
| `7D` | `0.1231` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 29,380.00 USD | 31,660.00 USD | 30,400.00 USD |
| `1D` | `0.1233` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 2,320.00 USD | 2,390.00 USD | 0.04 USD |
| `7D` | `0.1233` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 57,130.00 USD | 13,020.00 USD | 40,290.00 USD |
| `1D` | `0.1235` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 1,570.00 USD | 1,240.00 USD | 3,370.00 USD |
| `7D` | `0.1235` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 10,950.00 USD | 6,400.00 USD | 9,050.00 USD |
| `1D` | `0.1237` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 763.58 USD | 0.00 USD |
| `7D` | `0.1237` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 4,080.00 USD | 9,720.00 USD | 2,920.00 USD |
| `1D` | `0.1239` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 4,900.00 USD | 724.40 USD | 587.65 USD |
| `7D` | `0.1239` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 8,780.00 USD | 1,270.00 USD | 208.80 USD |
| `1D` | `0.1241` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 2,790.00 USD | 1,830.00 USD | 4,310.00 USD |
| `7D` | `0.1241` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 6,830.00 USD | 9,690.00 USD | 2,400.00 USD |
| `1D` | `0.1243` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 1,660.00 USD | 4,600.00 USD | 7,510.00 USD |
| `7D` | `0.1243` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 11,450.00 USD | 4,530.00 USD | 4,680.00 USD |
| `1D` | `0.1245` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 6,600.00 USD | 3,420.00 USD | 5,520.00 USD |
| `7D` | `0.1245` | 5,910,000.00 USD | 5,910,000.00 USD | 0.00 USD | 26,080.00 USD | 11,090.00 USD | 13,060.00 USD |
| `1D` | `0.1247` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 2,580.00 USD | 1,320.00 USD | 4,770.00 USD |
| `7D` | `0.1247` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 24,470.00 USD | 19,030.00 USD | 9,710.00 USD |
| `1D` | `0.1249` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 1,190.00 USD | 1,570.00 USD |
| `7D` | `0.1249` | 5,980,000.00 USD | 5,980,000.00 USD | 0.00 USD | 13,440.00 USD | 5,480.00 USD | 5,670.00 USD |
| `1D` | `0.1251` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 4,600.00 USD | 932.33 USD | 3,060.00 USD |
| `7D` | `0.1251` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 7,660.00 USD | 5,070.00 USD | 11,040.00 USD |
| `1D` | `0.1253` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 855.19 USD | 2,500.00 USD | 3,580.00 USD |
| `7D` | `0.1253` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 11,420.00 USD | 2,100.00 USD | 14,020.00 USD |
| `1D` | `0.1255` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 2,780.00 USD | 1,590.00 USD | 1,590.00 USD |
| `7D` | `0.1255` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 2,250.00 USD | 13,990.00 USD | 33.05 USD |
| `1D` | `0.1257` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 1,140.00 USD | 0.00 USD | 0.01 USD |
| `7D` | `0.1257` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 15,610.00 USD | 5,200.00 USD | 88.39 USD |
| `1D` | `0.1259` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 962.72 USD | 1,690.00 USD | 12.41 USD |
| `7D` | `0.1259` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 138.58 USD |
| `1D` | `0.1261` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 2,110.00 USD | 0.00 USD | 5.73 USD |
| `7D` | `0.1261` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | 3,530.00 USD |
| `7D` | `0.1263` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,100.00 USD |
| `1D` | `0.1265` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 1,300.00 USD | 694.78 USD | 0.00 USD |
| `7D` | `0.1265` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 2,710.00 USD | 0.00 USD | 3,250.00 USD |
| `7D` | `0.1267` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,930.00 USD |
| `7D` | `0.1269` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16.21 USD |
| `7D` | `0.1271` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 5,940.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1272` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10.64 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `74.97M` | Total OI Tokens: `668,516,041.2 OP`
  * 1h OI Change: `-1.52%` | 4h OI Change: `+0.82%` | 24h OI Change: `-1.33%`
  * Exchange Breakdown: Binance=`17.09M` | Bybit=`14.33M` | OKX=`4.22M` | Hyperliquid=`3.97M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.79K` | Last 24h: `270.64` | Last 3d: `-2.23K` | Last 7d: `-15.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0080%` | **USDT OKX** | `0.0090%` |
| **USDT Bybit** | `0.0070%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0080%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `39.60%` | `60.40%` | `0.66` | 2,030,000.00 USD |
| `15M` | `Binance` | `34.87%` | `65.13%` | `0.54` | 833,590.00 USD |
| `15M` | `OKX` | `46.72%` | `53.28%` | `0.88` | 250,750.00 USD |
| `15M` | `Bybit` | `32.08%` | `67.92%` | `0.47` | 244,380.00 USD |
| `15M` | `KuCoin` | `50.18%` | `49.82%` | `1.01` | 144,390.00 USD |
| `15M` | `Gate` | `37.65%` | `62.35%` | `0.60` | 28,410.00 USD |
| `15M` | `Bitget` | `21.68%` | `78.32%` | `0.28` | 41,420.00 USD |
| `15M` | `BingX` | `44.67%` | `55.33%` | `0.81` | 49,610.00 USD |
| `15M` | `MEXC` | `45.52%` | `54.48%` | `0.84` | 237,100.00 USD |
| `15M` | `Bitunix` | `37.54%` | `62.46%` | `0.60` | 23,630.00 USD |
| `15M` | `Hyperliquid` | `27.96%` | `72.04%` | `0.39` | 14,410.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `43.23%` | `56.77%` | `0.76` | 83,970.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `58.66%` | `41.34%` | `1.42` | 74,580.00 USD |
| `15M` | `HTX` | `63.57%` | `36.43%` | `1.74` | 0.76 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `64.12%` | `35.88%` | `1.79` | 4,710.00 USD |
| `15M` | `Aster` | `26.34%` | `73.66%` | `0.36` | 264.77 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `6.16%` | `93.84%` | `0.07` | 391.26 USD |
| `15M` | `Whale Positions` | `34.87%` | `65.13%` | `0.54` | 833,590.00 USD |
| `15M` | `Global Accounts` | `39.60%` | `60.40%` | `0.66` | 2,030,000.00 USD |
| `1H` | `OP` | `43.10%` | `56.90%` | `0.76` | 7,770,000.00 USD |
| `1H` | `Binance` | `39.32%` | `60.68%` | `0.65` | 3,280,000.00 USD |
| `1H` | `OKX` | `44.77%` | `55.23%` | `0.81` | 906,390.00 USD |
| `1H` | `Bybit` | `50.2%` | `49.8%` | `1.01` | 1,020,000.00 USD |
| `1H` | `KuCoin` | `49.15%` | `50.85%` | `0.97` | 590,270.00 USD |
| `1H` | `Gate` | `50.34%` | `49.66%` | `1.01` | 103,090.00 USD |
| `1H` | `Bitget` | `31.91%` | `68.09%` | `0.47` | 168,680.00 USD |
| `1H` | `BingX` | `45.31%` | `54.69%` | `0.83` | 476,980.00 USD |
| `1H` | `MEXC` | `41.58%` | `58.42%` | `0.71` | 515,820.00 USD |
| `1H` | `Bitunix` | `29.82%` | `70.18%` | `0.42` | 128,210.00 USD |
| `1H` | `Hyperliquid` | `43.75%` | `56.25%` | `0.78` | 67,890.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.92%` | `49.08%` | `1.04` | 211,320.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `45.93%` | `54.07%` | `0.85` | 276,220.00 USD |
| `1H` | `HTX` | `31.27%` | `68.73%` | `0.45` | 197.74 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `52.47%` | `47.53%` | `1.10` | 26,070.00 USD |
| `1H` | `Aster` | `4.13%` | `95.87%` | `0.04` | 1,690.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `37.63%` | `62.37%` | `0.60` | 1,880.00 USD |
| `1H` | `Whale Positions` | `39.32%` | `60.68%` | `0.65` | 3,280,000.00 USD |
| `1H` | `Global Accounts` | `43.10%` | `56.90%` | `0.76` | 7,770,000.00 USD |
| `4H` | `OP` | `45.84%` | `54.16%` | `0.85` | 29,140,000.00 USD |
| `4H` | `Binance` | `46.25%` | `53.75%` | `0.86` | 11,760,000.00 USD |
| `4H` | `OKX` | `47.37%` | `52.63%` | `0.90` | 3,220,000.00 USD |
| `4H` | `Bybit` | `45.37%` | `54.63%` | `0.83` | 3,280,000.00 USD |
| `4H` | `KuCoin` | `49.53%` | `50.47%` | `0.98` | 2,710,000.00 USD |
| `4H` | `Gate` | `49.42%` | `50.58%` | `0.98` | 451,650.00 USD |
| `4H` | `Bitget` | `45.45%` | `54.55%` | `0.83` | 815,780.00 USD |
| `4H` | `BingX` | `39.39%` | `60.61%` | `0.65` | 1,520,000.00 USD |
| `4H` | `MEXC` | `39.93%` | `60.07%` | `0.66` | 1,980,000.00 USD |
| `4H` | `Bitunix` | `39.38%` | `60.62%` | `0.65` | 592,060.00 USD |
| `4H` | `Hyperliquid` | `61.25%` | `38.75%` | `1.58` | 564,080.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.57%` | `51.43%` | `0.94` | 1,180,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `40.83%` | `59.17%` | `0.69` | 947,660.00 USD |
| `4H` | `HTX` | `88.16%` | `11.84%` | `7.45` | 6,350.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `29.06%` | `70.94%` | `0.41` | 90,740.00 USD |
| `4H` | `Aster` | `52.76%` | `47.24%` | `1.12` | 8,930.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `39.63%` | `60.37%` | `0.66` | 11,380.00 USD |
| `4H` | `Whale Positions` | `46.25%` | `53.75%` | `0.86` | 11,760,000.00 USD |
| `4H` | `Global Accounts` | `45.84%` | `54.16%` | `0.85` | 29,140,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1132` | `0.1126` | `0.1132` | `0.1134` | `0.1117` | 598,596.80 USD | 325,324.83 USD | 273,271.97 USD | 52,052.86 USD | `+8.70%` | `35B / 15S` |
| `5:00 UTC` | `0.1124` | `0.1128` | `0.1124` | `0.1134` | `0.1123` | 503,080.80 USD | 199,130.81 USD | 303,950.00 USD | -104,819.19 USD | `-20.84%` | `16B / 34S` |
| `0:00 UTC` | `0.1132` | `0.1131` | `0.1132` | `0.1135` | `0.1123` | 357,466.20 USD | 196,512.03 USD | 160,954.17 USD | 35,557.85 USD | `+9.95%` | `25B / 9S` |
| `5:00 UTC` | `0.1136` | `0.1136` | `0.1136` | `0.1141` | `0.1130` | 571,492.98 USD | 299,278.35 USD | 272,214.63 USD | 27,063.72 USD | `+4.74%` | `24B / 17S` |
| `0:00 UTC` | `0.1137` | `0.1140` | `0.1137` | `0.1149` | `0.1134` | 877,269.44 USD | 486,783.19 USD | 390,486.24 USD | 96,296.95 USD | `+10.98%` | `34B / 22S` |
| `5:00 UTC` | `0.1134` | `0.1136` | `0.1134` | `0.1142` | `0.1132` | 635,625.25 USD | 325,080.19 USD | 310,545.06 USD | 14,535.13 USD | `+2.29%` | `15B / 17S` |
| `0:00 UTC` | `0.1133` | `0.1131` | `0.1133` | `0.1135` | `0.1126` | 680,945.05 USD | 236,805.84 USD | 444,139.21 USD | -207,333.38 USD | `-30.45%` | `14B / 19S` |
| `5:00 UTC` | `0.1128` | `0.1128` | `0.1128` | `0.1130` | `0.1127` | 243,648.48 USD | 108,202.11 USD | 135,446.38 USD | -27,244.27 USD | `-11.18%` | `2B / 9S` |
| `0:00 UTC` | `0.1126` | `0.1127` | `0.1126` | `0.1132` | `0.1123` | 269,778.58 USD | 124,825.75 USD | 144,952.84 USD | -20,127.09 USD | `-7.46%` | `11B / 20S` |
| `5:00 UTC` | `0.1123` | `0.1122` | `0.1123` | `0.1124` | `0.1120` | 202,376.65 USD | 76,445.27 USD | 125,931.38 USD | -49,486.10 USD | `-24.45%` | `2B / 11S` |

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
| `5m` | -4,030.00 USD | -16,380.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,480.00 USD | -92,050.00 USD | **`DISTRIBUTION`** |
| `30m` | 1,020.00 USD | -180,470.00 USD | **`DISTRIBUTION`** |
| `1h` | -11,840.00 USD | -346,170.00 USD | **`DISTRIBUTION`** |
| `2h` | 15,530.00 USD | -181,200.00 USD | **`DISTRIBUTION`** |
| `4h` | 164,850.00 USD | 358,350.00 USD | **`ACCUMULATION`** |
| `6h` | 208,160.00 USD | 317,890.00 USD | **`ACCUMULATION`** |
| `8h` | 238,330.00 USD | 847,460.00 USD | **`ACCUMULATION`** |
| `12h` | 220,900.00 USD | 724,430.00 USD | **`ACCUMULATION`** |
| `24h` | 198,440.00 USD | -663,560.00 USD | **`DISTRIBUTION`** |
| `1w` | -127,360.00 USD | -9,550,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,580,000.00 USD | -77,970,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-4.03K` | 15m=`-1.48K` | 1h=`-11.84K` | 24h=`+198.44K`
* Futures Capital Netflows: 5m=`-16.38K` | 15m=`-92.05K` | 1h=`-346.17K` | 24h=`-663.56K`
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
  * `2026-10-29 22:45:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:14 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [dol.gov] - (Sentiment: `Neutral`)


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
