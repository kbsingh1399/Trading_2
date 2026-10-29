# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-29 21:43:08 IST` (`2026-10-29 16:13:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1113` | `0.1115` | `0.1109` | `0.1114` | `1,702,806` | 189,336.93 USD | 12,018.79 USD | `+6.35%` | -668,610.61 USD | `-0.13` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1114` | `0.1115` | `0.1111` | `0.1111` | `646,195` | 71,914.13 USD | 6,159.12 USD | `+8.56%` | -662,451.49 USD | `-0.44` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1111` | `0.1116` | `0.1110` | `0.1116` | `514,243` | 57,214.55 USD | 18,153.52 USD | `+31.73%` | -644,297.97 USD | `+0.17` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1109` | `0.1112` | `0.1103` | `0.1109` | `4,978,593` | 551,290.91 USD | 63,892.46 USD | `+11.59%` | -760,371.72 USD | `+0.92` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1109` | `0.1118` | `0.1108` | `0.1113` | `4,586,213` | 510,110.63 USD | 79,742.32 USD | `+15.63%` | -680,629.40 USD | `+1.11` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1113` | `0.1116` | `0.1109` | `0.1116` | `2,864,448` | 318,599.98 USD | 36,449.79 USD | `+11.44%` | -644,179.61 USD | `+0.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1099` | `0.1107` | `0.1093` | `0.1105` | `13,054,448` | 1,435,720.86 USD | 52,800.07 USD | `+3.68%` | -981,526.18 USD | `+0.36` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1105` | `0.1118` | `0.1103` | `0.1113` | `18,319,494` | 2,032,262.74 USD | 179,409.65 USD | `+8.83%` | -802,116.53 USD | `+0.85` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1113` | `0.1116` | `0.1109` | `0.1116` | `2,863,244` | 318,465.62 USD | 36,331.43 USD | `+11.41%` | -765,785.10 USD | `+0.28` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1085` | `0.1106` | `0.1071` | `0.1076` | `47,048,931` | 5,111,570.05 USD | 108,567.99 USD | `+2.12%` | -1,161,630.37 USD | `+0.56` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,018,907.54 USD | `+0.52` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1118` | `0.1093` | `0.1116` | `34,238,319` | 3,786,575.59 USD | 268,667.51 USD | `+7.10%` | -750,240.03 USD | `+0.62` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1145` | `0.1159` | `0.1127` | `0.1131` | `52,002,024` | 5,926,200.82 USD | 47,383.34 USD | `+0.80%` | 258,176.24 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1131` | `0.1136` | `0.1072` | `0.1085` | `76,338,549` | 8,353,905.81 USD | -1,528,374.61 USD | `-18.30%` | -1,270,198.37 USD | `-1.41` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1085` | `0.1106` | `0.1071` | `0.1076` | `47,048,931` | 5,111,570.05 USD | 108,567.99 USD | `+2.12%` | -1,161,630.37 USD | `+0.56` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,018,907.54 USD | `+0.52` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1118` | `0.1093` | `0.1116` | `34,238,319` | 3,786,575.59 USD | 268,667.51 USD | `+7.10%` | -750,240.03 USD | `+0.62` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 19:44:05 IST` |

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
| `Live` | `Long Liquidation` | `0.0235` | 141.00 USD | 244,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0355` | 161.04 USD | 244,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 3,520.00 USD | 244,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 262.59 USD | 240,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 3,460.00 USD | 240,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 829.69 USD | 236,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 1,100.00 USD | 236,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 353.81 USD | 234,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 518.48 USD | 234,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 1,920.00 USD | 234,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 106.26 USD | 232,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 25,370.00 USD | 232,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,300.00 USD | 206,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 44,530.00 USD | 204,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 1,170.00 USD | 159,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 878.62 USD | 158,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 4,680.00 USD | 157,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 1,320.00 USD | 153,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 223.98 USD | 151,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 1,560.00 USD | 151,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 2,380.00 USD | 150,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,120.00 USD | 147,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 443.16 USD | 144,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 16,670.00 USD | 144,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 69,120.00 USD | 127,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 5,610.00 USD | 58,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0961` | 3,850,000.00 USD | 3,850,000.00 USD | 2,410.00 USD | 1,140.00 USD | 20.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0963` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 1,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0965` | 419.87 USD | 52,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0967` | 3,840,000.00 USD | 3,840,000.00 USD | 3,770.00 USD | 2,660.00 USD | 2,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0969` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 2,810.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 2,000.00 USD | 34.36 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0973` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0975` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 1,160.00 USD | 4,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0975` | 13,250.00 USD | 52,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0977` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 5,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0979` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 1,530.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0981` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 3,790,000.00 USD | 3,790,000.00 USD | 7,990.00 USD | 1,230.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0984` | 1,790,000.00 USD | 1,790,000.00 USD | 8,920.00 USD | 1,310.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0985` | 3,770,000.00 USD | 3,770,000.00 USD | 7,110.00 USD | 0.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0985` | 20,640.00 USD | 39,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0986` | 1,770,000.00 USD | 1,770,000.00 USD | 6,230.00 USD | 3,450.00 USD | 7,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0987` | 3,760,000.00 USD | 3,760,000.00 USD | 5,390.00 USD | 9,190.00 USD | 37,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0988` | 1,750,000.00 USD | 1,750,000.00 USD | 8,730.00 USD | 1,770.00 USD | 4,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 3,710,000.00 USD | 3,710,000.00 USD | 12,260.00 USD | 4,520.00 USD | 27,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0990` | 1,740,000.00 USD | 1,740,000.00 USD | 3,980.00 USD | 4,820.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0991` | 3,660,000.00 USD | 3,660,000.00 USD | 14,350.00 USD | 10,350.00 USD | 13,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0992` | 1,730,000.00 USD | 1,730,000.00 USD | 1,020.00 USD | 1,360.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0993` | 3,630,000.00 USD | 3,630,000.00 USD | 23,920.00 USD | 10,140.00 USD | 24,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0994` | 1,720,000.00 USD | 1,720,000.00 USD | 4,020.00 USD | 820.70 USD | 8,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 3,570,000.00 USD | 3,570,000.00 USD | 13,090.00 USD | 6,160.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0996` | 1,700,000.00 USD | 1,700,000.00 USD | 3,910.00 USD | 1,320.00 USD | 13,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0997` | 3,520,000.00 USD | 3,520,000.00 USD | 21,100.00 USD | 5,500.00 USD | 29,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0998` | 1,680,000.00 USD | 1,680,000.00 USD | 4,340.00 USD | 2,350.00 USD | 4,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0999` | 3,470,000.00 USD | 3,470,000.00 USD | 14,230.00 USD | 6,540.00 USD | 18,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1000` | 1,670,000.00 USD | 1,670,000.00 USD | 4,260.00 USD | 3,110.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 3,430,000.00 USD | 3,430,000.00 USD | 29,230.00 USD | 3,010.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1002` | 1,660,000.00 USD | 1,660,000.00 USD | 2,660.00 USD | 558.39 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1003` | 3,380,000.00 USD | 3,380,000.00 USD | 8,010.00 USD | 7,060.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1004` | 1,650,000.00 USD | 1,650,000.00 USD | 1,970.00 USD | 0.00 USD | 61.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1005` | 3,360,000.00 USD | 3,360,000.00 USD | 25,070.00 USD | 11,000.00 USD | 18,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1005` | 427.25 USD | 18,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1006` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 403.62 USD | 818.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 3,310,000.00 USD | 3,310,000.00 USD | 10,260.00 USD | 2,280.00 USD | 14,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1008` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 1,270.00 USD | 0.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1009` | 3,280,000.00 USD | 3,280,000.00 USD | 15,320.00 USD | 1,660.00 USD | 6,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1010` | 1,650,000.00 USD | 1,650,000.00 USD | 1,070.00 USD | 575.54 USD | 1,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1011` | 3,260,000.00 USD | 3,260,000.00 USD | 4,430.00 USD | 4,720.00 USD | 8,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1012` | 1,650,000.00 USD | 1,650,000.00 USD | 1,570.00 USD | 1,430.00 USD | 16.77 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 3,240,000.00 USD | 3,240,000.00 USD | 12,870.00 USD | 4,030.00 USD | 3,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1014` | 1,640,000.00 USD | 1,640,000.00 USD | 1,870.00 USD | 724.40 USD | 623.59 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1015` | 3,220,000.00 USD | 3,220,000.00 USD | 6,830.00 USD | 965.35 USD | 2,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1015` | 622.37 USD | 17,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1016` | 1,640,000.00 USD | 1,640,000.00 USD | 3,360.00 USD | 0.00 USD | 4,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1017` | 3,210,000.00 USD | 3,210,000.00 USD | 11,450.00 USD | 2,850.00 USD | 4,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1018` | 1,630,000.00 USD | 1,630,000.00 USD | 827.81 USD | 4,170.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1019` | 3,190,000.00 USD | 3,190,000.00 USD | 3,160.00 USD | 3,310.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1020` | 1,630,000.00 USD | 1,630,000.00 USD | 2,640.00 USD | 2,630.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1021` | 3,180,000.00 USD | 3,180,000.00 USD | 7,900.00 USD | 3,270.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1022` | 1,620,000.00 USD | 1,620,000.00 USD | 1,910.00 USD | 1,390.00 USD | 4,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1023` | 3,160,000.00 USD | 3,160,000.00 USD | 4,030.00 USD | 4,990.00 USD | 11,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1024` | 1,610,000.00 USD | 1,610,000.00 USD | 2,300.00 USD | 947.50 USD | 4,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1025` | 3,140,000.00 USD | 3,140,000.00 USD | 1,550.00 USD | 0.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1025` | 17,360.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1026` | 1,600,000.00 USD | 1,600,000.00 USD | 2,780.00 USD | 654.25 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1027` | 3,130,000.00 USD | 3,130,000.00 USD | 2,250.00 USD | 1,170.00 USD | 344.47 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1028` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 936.16 USD | 36.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1029` | 3,130,000.00 USD | 3,130,000.00 USD | 7,420.00 USD | 3,000.00 USD | 332.49 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1030` | 1,600,000.00 USD | 1,600,000.00 USD | 8,870.00 USD | 3,480.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1031` | 3,120,000.00 USD | 3,120,000.00 USD | 13,690.00 USD | 5,070.00 USD | 10,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1032` | 1,580,000.00 USD | 1,580,000.00 USD | 11,310.00 USD | 2,260.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1033` | 3,090,000.00 USD | 3,090,000.00 USD | 3,880.00 USD | 2,640.00 USD | 15,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1034` | 1,560,000.00 USD | 1,560,000.00 USD | 7,190.00 USD | 5,040.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1035` | 3,070,000.00 USD | 3,070,000.00 USD | 2,710.00 USD | 9,400.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1036` | 1,530,000.00 USD | 1,530,000.00 USD | 4,780.00 USD | 7,340.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1037` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1038` | 1,510,000.00 USD | 1,510,000.00 USD | 4,190.00 USD | 9,130.00 USD | 12,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1039` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 5,170.00 USD | 167.04 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1040` | 1,480,000.00 USD | 1,480,000.00 USD | 2,980.00 USD | 4,600.00 USD | 12,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1041` | 3,010,000.00 USD | 3,010,000.00 USD | 5,940.00 USD | 2,910.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1042` | 1,460,000.00 USD | 1,460,000.00 USD | 23,250.00 USD | 5,430.00 USD | 12,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1043` | 2,990,000.00 USD | 2,990,000.00 USD | 15,960.00 USD | 5,980.00 USD | 21,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1044` | 1,420,000.00 USD | 1,420,000.00 USD | 917.34 USD | 6,870.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1045` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 3,830.00 USD | 14,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1046` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 1,080.00 USD | 8,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1047` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 1,720.00 USD | 22,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1048` | 1,400,000.00 USD | 1,400,000.00 USD | 8,130.00 USD | 3,110.00 USD | 25,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1049` | 2,910,000.00 USD | 2,910,000.00 USD | 34,790.00 USD | 4,810.00 USD | 35,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1050` | 1,370,000.00 USD | 1,370,000.00 USD | 22,700.00 USD | 5,610.00 USD | 16,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1051` | 2,830,000.00 USD | 2,830,000.00 USD | 17,290.00 USD | 11,500.00 USD | 48,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1052` | 1,320,000.00 USD | 1,320,000.00 USD | 28,330.00 USD | 12,260.00 USD | 37,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1053` | 2,760,000.00 USD | 2,760,000.00 USD | 47,580.00 USD | 29,800.00 USD | 95,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1054` | 1,240,000.00 USD | 1,240,000.00 USD | 52,400.00 USD | 15,020.00 USD | 43,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1055` | 2,580,000.00 USD | 2,580,000.00 USD | 50,090.00 USD | 27,290.00 USD | 122,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1056` | 1,130,000.00 USD | 1,130,000.00 USD | 24,440.00 USD | 26,930.00 USD | 39,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1057` | 2,380,000.00 USD | 2,380,000.00 USD | 44,200.00 USD | 43,030.00 USD | 74,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1058` | 1,040,000.00 USD | 1,040,000.00 USD | 10,330.00 USD | 29,030.00 USD | 42,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1059` | 2,220,000.00 USD | 2,220,000.00 USD | 92,510.00 USD | 49,670.00 USD | 116,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1060` | 960,460.00 USD | 960,460.00 USD | 20,300.00 USD | 6,530.00 USD | 47,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1061` | 1,960,000.00 USD | 1,960,000.00 USD | 38,260.00 USD | 28,780.00 USD | 76,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1062` | 886,290.00 USD | 886,290.00 USD | 25,860.00 USD | 16,630.00 USD | 49,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1063` | 1,820,000.00 USD | 1,820,000.00 USD | 95,080.00 USD | 38,330.00 USD | 151,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1064` | 794,270.00 USD | 794,270.00 USD | 52,110.00 USD | 17,050.00 USD | 45,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1065` | 1,530,000.00 USD | 1,530,000.00 USD | 84,890.00 USD | 21,040.00 USD | 86,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1066` | 679,900.00 USD | 679,900.00 USD | 16,810.00 USD | 16,760.00 USD | 10,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1067` | 1,340,000.00 USD | 1,340,000.00 USD | 97,290.00 USD | 34,000.00 USD | 67,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1068` | 635,910.00 USD | 635,910.00 USD | 16,220.00 USD | 6,080.00 USD | 33,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1069` | 1,140,000.00 USD | 1,140,000.00 USD | 76,900.00 USD | 30,720.00 USD | 67,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1070` | 580,590.00 USD | 580,590.00 USD | 21,170.00 USD | 6,210.00 USD | 51,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1071` | 968,210.00 USD | 968,210.00 USD | 119,440.00 USD | 27,240.00 USD | 42,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1072` | 501,350.00 USD | 501,350.00 USD | 38,000.00 USD | 7,100.00 USD | 14,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1073` | 778,790.00 USD | 778,790.00 USD | 62,850.00 USD | 17,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1074` | 441,900.00 USD | 441,900.00 USD | 11,270.00 USD | 12,510.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1075` | 698,240.00 USD | 698,240.00 USD | 8,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1076` | 411,600.00 USD | 411,600.00 USD | 6,090.00 USD | 1,930.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1078` | 392,760.00 USD | 392,760.00 USD | 12,550.00 USD | 15,090.00 USD | 21,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1079` | 689,520.00 USD | 689,520.00 USD | 123,150.00 USD | 18,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1080` | 343,660.00 USD | 343,660.00 USD | 0.00 USD | 4,200.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1081` | 547,850.00 USD | 547,850.00 USD | 200,110.00 USD | 9,430.00 USD | 28,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1082` | 307,110.00 USD | 307,110.00 USD | 14,140.00 USD | 4,100.00 USD | 33,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1083` | 309,480.00 USD | 309,480.00 USD | 94,800.00 USD | 0.00 USD | 37,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1084` | 255,410.00 USD | 255,410.00 USD | 28,610.00 USD | 4,270.00 USD | 29,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1085` | 177,130.00 USD | 177,130.00 USD | 15,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1086` | 193,400.00 USD | 193,400.00 USD | 19,870.00 USD | 8,030.00 USD | 51,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1087` | 161,210.00 USD | 161,210.00 USD | 22,680.00 USD | 0.00 USD | 27,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1088` | 114,120.00 USD | 114,120.00 USD | 23,840.00 USD | 8,890.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1089` | 110,750.00 USD | 110,750.00 USD | 0.00 USD | 9,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1090` | 70,470.00 USD | 70,470.00 USD | 34,340.00 USD | 5,060.00 USD | 7,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1091` | 101,630.00 USD | 101,630.00 USD | 16,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1092` | 23,910.00 USD | 23,910.00 USD | 0.00 USD | 2,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1094` | 21,120.00 USD | 21,120.00 USD | 9,840.00 USD | 0.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1095` | 85,330.00 USD | 85,330.00 USD | 18,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1097` | 66,490.00 USD | 66,490.00 USD | 0.00 USD | 2,970.00 USD | 21,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1099` | 41,920.00 USD | 41,920.00 USD | 0.00 USD | 0.00 USD | 25,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1103` | 16,860.00 USD | 16,860.00 USD | 6,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1105` | 9,930.00 USD | 9,930.00 USD | 0.00 USD | 5,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1107` | 4,120.00 USD | 4,120.00 USD | 0.00 USD | 4,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1112` | 8,100.00 USD | 8,100.00 USD | 0.00 USD | 8,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1113` | 60,930.00 USD | 60,930.00 USD | 0.00 USD | 3,440.00 USD | 57,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1114` | 25,570.00 USD | 25,570.00 USD | 0.00 USD | 0.00 USD | 25,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1115` | 104,110.00 USD | 104,110.00 USD | 0.00 USD | 7,050.00 USD | 36,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1116` | 29,870.00 USD | 29,870.00 USD | 0.00 USD | 4,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1117` | 150,460.00 USD | 150,460.00 USD | 0.00 USD | 22,780.00 USD | 23,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1118` | 85,070.00 USD | 85,070.00 USD | 16,250.00 USD | 17,620.00 USD | 21,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1119` | 209,120.00 USD | 209,120.00 USD | 45,230.00 USD | 2,640.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1120` | 161,190.00 USD | 161,190.00 USD | 26,440.00 USD | 9,670.00 USD | 40,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 260,400.00 USD | 260,400.00 USD | 29,340.00 USD | 9,400.00 USD | 12,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1122` | 260,390.00 USD | 260,390.00 USD | 34,540.00 USD | 24,070.00 USD | 40,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1123` | 353,770.00 USD | 353,770.00 USD | 48,680.00 USD | 18,520.00 USD | 26,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1124` | 349,160.00 USD | 349,160.00 USD | 9,670.00 USD | 17,780.00 USD | 61,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1125` | 404,760.00 USD | 404,760.00 USD | 7,560.00 USD | 14,600.00 USD | 28,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1126` | 436,370.00 USD | 436,370.00 USD | 23,570.00 USD | 13,380.00 USD | 50,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1127` | 459,110.00 USD | 459,110.00 USD | 0.00 USD | 6,460.00 USD | 47,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1128` | 524,620.00 USD | 524,620.00 USD | 36,740.00 USD | 9,700.00 USD | 41,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1129` | 517,160.00 USD | 517,160.00 USD | 31,880.00 USD | 5,980.00 USD | 20,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1130` | 609,160.00 USD | 609,160.00 USD | 20,790.00 USD | 12,290.00 USD | 51,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1131` | 573,870.00 USD | 573,870.00 USD | 22,680.00 USD | 0.00 USD | 34,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1132` | 646,250.00 USD | 646,250.00 USD | 5,520.00 USD | 17,300.00 USD | 14,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 586,880.00 USD | 586,880.00 USD | 0.00 USD | 12,940.00 USD | 68.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1134` | 690,850.00 USD | 690,850.00 USD | 22,660.00 USD | 6,140.00 USD | 15,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1135` | 635,550.00 USD | 635,550.00 USD | 32,150.00 USD | 1,720.00 USD | 14,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1136` | 725,000.00 USD | 725,000.00 USD | 8,130.00 USD | 5,900.00 USD | 20,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1137` | 672,890.00 USD | 672,890.00 USD | 30,030.00 USD | 1,730.00 USD | 5,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1138` | 771,910.00 USD | 771,910.00 USD | 28,830.00 USD | 2,470.00 USD | 15,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1139` | 689,980.00 USD | 689,980.00 USD | 0.00 USD | 8,850.00 USD | 8,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1140` | 804,720.00 USD | 804,720.00 USD | 11,260.00 USD | 10,870.00 USD | 10,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1141` | 707,280.00 USD | 707,280.00 USD | 4,360.00 USD | 5,280.00 USD | 7,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1142` | 826,530.00 USD | 826,530.00 USD | 6,060.00 USD | 7,580.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1143` | 781,570.00 USD | 781,570.00 USD | 0.00 USD | 0.00 USD | 74,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1144` | 872,590.00 USD | 872,590.00 USD | 9,940.00 USD | 11,240.00 USD | 24,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 942,350.00 USD | 942,350.00 USD | 10,360.00 USD | 9,260.00 USD | 141,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1146` | 900,290.00 USD | 900,290.00 USD | 0.00 USD | 4,690.00 USD | 23,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1147` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 4,720.00 USD | 134,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1148` | 944,310.00 USD | 944,310.00 USD | 16,850.00 USD | 2,650.00 USD | 24,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1149` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 72,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1150` | 976,230.00 USD | 976,230.00 USD | 6,750.00 USD | 2,140.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 1,370,000.00 USD | 1,370,000.00 USD | 92,570.00 USD | 0.00 USD | 118,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1152` | 1,070,000.00 USD | 1,070,000.00 USD | 38,250.00 USD | 4,010.00 USD | 54,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1153` | 1,650,000.00 USD | 1,650,000.00 USD | 147,450.00 USD | 0.00 USD | 132,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1154` | 1,140,000.00 USD | 1,140,000.00 USD | 15,000.00 USD | 30,910.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1155` | 1,850,000.00 USD | 1,850,000.00 USD | 108,940.00 USD | 24,970.00 USD | 71,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1156` | 1,210,000.00 USD | 1,210,000.00 USD | 26,190.00 USD | 18,050.00 USD | 26,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 2,070,000.00 USD | 2,070,000.00 USD | 163,490.00 USD | 3,760.00 USD | 48,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1158` | 1,270,000.00 USD | 1,270,000.00 USD | 23,070.00 USD | 9,500.00 USD | 30,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1159` | 2,230,000.00 USD | 2,230,000.00 USD | 105,000.00 USD | 10,810.00 USD | 48,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1160` | 1,310,000.00 USD | 1,310,000.00 USD | 17,270.00 USD | 3,260.00 USD | 19,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1161` | 2,510,000.00 USD | 2,510,000.00 USD | 155,210.00 USD | 37,250.00 USD | 82,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1162` | 1,340,000.00 USD | 1,340,000.00 USD | 11,190.00 USD | 5,750.00 USD | 14,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 2,660,000.00 USD | 2,660,000.00 USD | 74,250.00 USD | 11,460.00 USD | 68,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1164` | 1,380,000.00 USD | 1,380,000.00 USD | 20,480.00 USD | 13,180.00 USD | 5,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1165` | 2,790,000.00 USD | 2,790,000.00 USD | 77,390.00 USD | 25,170.00 USD | 27,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1166` | 1,400,000.00 USD | 1,400,000.00 USD | 12,970.00 USD | 4,410.00 USD | 29.55 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1167` | 2,930,000.00 USD | 2,930,000.00 USD | 79,610.00 USD | 21,620.00 USD | 41,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1168` | 1,430,000.00 USD | 1,430,000.00 USD | 13,800.00 USD | 15,460.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 3,090,000.00 USD | 3,090,000.00 USD | 60,400.00 USD | 14,840.00 USD | 86,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1170` | 1,470,000.00 USD | 1,470,000.00 USD | 12,280.00 USD | 5,800.00 USD | 17,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1171` | 3,190,000.00 USD | 3,190,000.00 USD | 52,070.00 USD | 9,140.00 USD | 35,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1172` | 1,480,000.00 USD | 1,480,000.00 USD | 9,230.00 USD | 4,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1173` | 3,270,000.00 USD | 3,270,000.00 USD | 40,860.00 USD | 7,080.00 USD | 31,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1174` | 1,510,000.00 USD | 1,510,000.00 USD | 10,730.00 USD | 0.00 USD | 12,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 3,380,000.00 USD | 3,380,000.00 USD | 38,840.00 USD | 8,100.00 USD | 58,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1176` | 1,530,000.00 USD | 1,530,000.00 USD | 6,120.00 USD | 16,060.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1177` | 3,430,000.00 USD | 3,430,000.00 USD | 13,120.00 USD | 14,140.00 USD | 27,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1178` | 1,560,000.00 USD | 1,560,000.00 USD | 13,850.00 USD | 7,760.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1179` | 3,530,000.00 USD | 3,530,000.00 USD | 61,380.00 USD | 10,940.00 USD | 23,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1180` | 1,600,000.00 USD | 1,600,000.00 USD | 13,680.00 USD | 4,770.00 USD | 18,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 3,580,000.00 USD | 3,580,000.00 USD | 22,290.00 USD | 15,780.00 USD | 17,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1182` | 1,620,000.00 USD | 1,620,000.00 USD | 7,160.00 USD | 1,920.00 USD | 10,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1183` | 3,620,000.00 USD | 3,620,000.00 USD | 4,040.00 USD | 1,800.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1184` | 1,640,000.00 USD | 1,640,000.00 USD | 5,370.00 USD | 3,320.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1185` | 3,650,000.00 USD | 3,650,000.00 USD | 3,880.00 USD | 5,130.00 USD | 22,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1186` | 1,660,000.00 USD | 1,660,000.00 USD | 10,390.00 USD | 4,870.00 USD | 4,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 3,700,000.00 USD | 3,700,000.00 USD | 5,620.00 USD | 11,840.00 USD | 32,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1188` | 1,670,000.00 USD | 1,670,000.00 USD | 4,660.00 USD | 7,610.00 USD | 4,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1189` | 3,740,000.00 USD | 3,740,000.00 USD | 27,240.00 USD | 15,060.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1190` | 1,690,000.00 USD | 1,690,000.00 USD | 5,250.00 USD | 5,740.00 USD | 2,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1191` | 3,890,000.00 USD | 3,890,000.00 USD | 22,650.00 USD | 15,330.00 USD | 109,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1192` | 1,700,000.00 USD | 1,700,000.00 USD | 7,250.00 USD | 1,990.00 USD | 7,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 3,920,000.00 USD | 3,920,000.00 USD | 21,260.00 USD | 0.00 USD | 9,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1194` | 1,710,000.00 USD | 1,710,000.00 USD | 6,310.00 USD | 1,390.00 USD | 2,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1195` | 3,960,000.00 USD | 3,960,000.00 USD | 11,190.00 USD | 1,780.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1195` | 899.88 USD | 899.88 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1196` | 1,720,000.00 USD | 1,720,000.00 USD | 3,240.00 USD | 2,860.00 USD | 0.73 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1197` | 4,000,000.00 USD | 4,000,000.00 USD | 6,780.00 USD | 10,800.00 USD | 14,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1198` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 3,660.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 4,070,000.00 USD | 4,070,000.00 USD | 9,100.00 USD | 0.00 USD | 64,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1200` | 1,740,000.00 USD | 1,740,000.00 USD | 1,840.00 USD | 1,050.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1201` | 4,230,000.00 USD | 4,230,000.00 USD | 114,140.00 USD | 16,380.00 USD | 29,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1202` | 1,750,000.00 USD | 1,750,000.00 USD | 10,280.00 USD | 700.19 USD | 4,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1203` | 4,340,000.00 USD | 4,340,000.00 USD | 70,770.00 USD | 29,250.00 USD | 6,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1204` | 1,760,000.00 USD | 1,760,000.00 USD | 1,480.00 USD | 1,010.00 USD | 3,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 4,600,000.00 USD | 4,600,000.00 USD | 86,480.00 USD | 48,720.00 USD | 128,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1205` | 2,250.00 USD | 3,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1206` | 1,770,000.00 USD | 1,770,000.00 USD | 4,750.00 USD | 2,440.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1207` | 4,690,000.00 USD | 4,690,000.00 USD | 12,460.00 USD | 19,400.00 USD | 59,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1208` | 1,780,000.00 USD | 1,780,000.00 USD | 8,730.00 USD | 1,770.00 USD | 4,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1209` | 4,890,000.00 USD | 4,890,000.00 USD | 85,160.00 USD | 19,340.00 USD | 94,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1210` | 1,800,000.00 USD | 1,800,000.00 USD | 3,980.00 USD | 4,820.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 4,970,000.00 USD | 4,970,000.00 USD | 35,090.00 USD | 18,720.00 USD | 29,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1212` | 1,810,000.00 USD | 1,810,000.00 USD | 1,020.00 USD | 1,360.00 USD | 8,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1213` | 5,060,000.00 USD | 5,060,000.00 USD | 32,700.00 USD | 29,060.00 USD | 24,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1214` | 1,820,000.00 USD | 1,820,000.00 USD | 4,020.00 USD | 820.70 USD | 8,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1215` | 5,160,000.00 USD | 5,160,000.00 USD | 27,750.00 USD | 9,240.00 USD | 59,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1216` | 1,830,000.00 USD | 1,830,000.00 USD | 1,330.00 USD | 0.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 5,210,000.00 USD | 5,210,000.00 USD | 18,490.00 USD | 26,300.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1218` | 1,840,000.00 USD | 1,840,000.00 USD | 2,580.00 USD | 1,320.00 USD | 9,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1219` | 5,280,000.00 USD | 5,280,000.00 USD | 26,700.00 USD | 5,500.00 USD | 35,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1220` | 1,850,000.00 USD | 1,850,000.00 USD | 4,340.00 USD | 2,350.00 USD | 3,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1221` | 5,370,000.00 USD | 5,370,000.00 USD | 47,890.00 USD | 21,770.00 USD | 18,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1222` | 1,860,000.00 USD | 1,860,000.00 USD | 4,260.00 USD | 3,110.00 USD | 3,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 5,560,000.00 USD | 5,560,000.00 USD | 103,180.00 USD | 36,290.00 USD | 48,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1224` | 1,870,000.00 USD | 1,870,000.00 USD | 2,660.00 USD | 558.39 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1225` | 5,640,000.00 USD | 5,640,000.00 USD | 50,540.00 USD | 26,800.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 1,810.00 USD | 4,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1227` | 5,810,000.00 USD | 5,810,000.00 USD | 75,750.00 USD | 31,790.00 USD | 58,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1228` | 1,870,000.00 USD | 1,870,000.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 5,990,000.00 USD | 5,990,000.00 USD | 87,270.00 USD | 41,310.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1230` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 403.62 USD | 789.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1231` | 6,080,000.00 USD | 6,080,000.00 USD | 29,380.00 USD | 31,660.00 USD | 30,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1232` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 430.11 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1233` | 6,200,000.00 USD | 6,200,000.00 USD | 65,180.00 USD | 12,850.00 USD | 39,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1234` | 6,210,000.00 USD | 6,210,000.00 USD | 8,540.00 USD | 5,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1305` | 119.84 USD | 5,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1355` | 1,330.00 USD | 6,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1555` | 6,910.00 USD | 13,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1565` | 550.61 USD | 13,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1605` | 14,450.00 USD | 28,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1615` | 19,540.00 USD | 47,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1695` | 169.25 USD | 48,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1855` | 1,640.00 USD | 49,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1865` | 167.85 USD | 49,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1935` | 935.32 USD | 50,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 2,240.00 USD | 53,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0235` | 244,460.00 USD | 0.00 USD | 141.00 USD | `-78.90%` | `6,000.00` |
| `Live` | `Long` | `0.0355` | 244,320.00 USD | 0.00 USD | 161.04 USD | `-68.13%` | `4,536.30` |
| `Live` | `Long` | `0.0505` | 244,160.00 USD | 0.00 USD | 3,520.00 USD | `-54.66%` | `69,790.10` |
| `Live` | `Long` | `0.0515` | 240,630.00 USD | 0.00 USD | 262.59 USD | `-53.76%` | `5,098.90` |
| `Live` | `Long` | `0.0545` | 240,370.00 USD | 0.00 USD | 3,460.00 USD | `-51.07%` | `63,403.00` |
| `Live` | `Long` | `0.0575` | 236,920.00 USD | 0.00 USD | 829.69 USD | `-48.37%` | `14,429.40` |
| `Live` | `Long` | `0.0615` | 236,090.00 USD | 0.00 USD | 1,100.00 USD | `-44.78%` | `17,943.80` |
| `Live` | `Long` | `0.0645` | 234,980.00 USD | 0.00 USD | 353.81 USD | `-42.09%` | `5,485.40` |
| `Live` | `Long` | `0.0675` | 234,630.00 USD | 0.00 USD | 518.48 USD | `-39.40%` | `7,681.20` |
| `Live` | `Long` | `0.0685` | 234,110.00 USD | 0.00 USD | 1,920.00 USD | `-38.50%` | `28,000.00` |
| `Live` | `Long` | `0.0705` | 232,190.00 USD | 0.00 USD | 106.26 USD | `-36.70%` | `1,507.30` |
| `Live` | `Long` | `0.0725` | 232,090.00 USD | 0.00 USD | 25,370.00 USD | `-34.91%` | `349,988.60` |
| `Live` | `Long` | `0.0745` | 206,710.00 USD | 0.00 USD | 2,300.00 USD | `-33.11%` | `30,851.90` |
| `Live` | `Long` | `0.0755` | 204,410.00 USD | 0.00 USD | 44,530.00 USD | `-32.21%` | `589,740.40` |
| `Live` | `Long` | `0.0765` | 159,890.00 USD | 0.00 USD | 1,170.00 USD | `-31.32%` | `15,263.30` |
| `Live` | `Long` | `0.0775` | 158,720.00 USD | 0.00 USD | 878.62 USD | `-30.42%` | `11,337.00` |
| `Live` | `Long` | `0.0785` | 157,840.00 USD | 0.00 USD | 4,680.00 USD | `-29.52%` | `59,562.80` |
| `Live` | `Long` | `0.0795` | 153,170.00 USD | 0.00 USD | 1,320.00 USD | `-28.62%` | `16,641.80` |
| `Live` | `Long` | `0.0805` | 151,840.00 USD | 0.00 USD | 223.98 USD | `-27.72%` | `2,782.40` |
| `Live` | `Long` | `0.0815` | 151,620.00 USD | 0.00 USD | 1,560.00 USD | `-26.83%` | `19,181.40` |
| `Live` | `Long` | `0.0875` | 150,060.00 USD | 0.00 USD | 2,380.00 USD | `-21.44%` | `27,146.60` |
| `Live` | `Long` | `0.0895` | 147,680.00 USD | 0.00 USD | 3,120.00 USD | `-19.64%` | `34,873.20` |
| `Live` | `Long` | `0.0905` | 144,560.00 USD | 0.00 USD | 443.16 USD | `-18.75%` | `4,896.80` |
| `Live` | `Long` | `0.0925` | 144,120.00 USD | 0.00 USD | 16,670.00 USD | `-16.95%` | `180,203.00` |
| `Live` | `Long` | `0.0945` | 127,450.00 USD | 0.00 USD | 69,120.00 USD | `-15.16%` | `731,405.60` |
| `Live` | `Long` | `0.0955` | 58,330.00 USD | 0.00 USD | 5,610.00 USD | `-14.26%` | `58,700.70` |
| `Live` | `Long` | `0.0965` | 52,720.00 USD | 0.00 USD | 419.87 USD | `-13.36%` | `4,351.00` |
| `Live` | `Long` | `0.0975` | 52,300.00 USD | 0.00 USD | 13,250.00 USD | `-12.46%` | `135,935.70` |
| `Live` | `Long` | `0.0985` | 39,050.00 USD | 0.00 USD | 20,640.00 USD | `-11.56%` | `209,504.10` |
| `Live` | `Long` | `0.1005` | 18,410.00 USD | 0.00 USD | 427.25 USD | `-9.77%` | `4,251.20` |
| `Live` | `Long` | `0.1015` | 17,990.00 USD | 0.00 USD | 622.37 USD | `-8.87%` | `6,131.70` |
| `Live` | `Long` | `0.1025` | 17,360.00 USD | 0.00 USD | 17,360.00 USD | `-7.97%` | `169,408.50` |
| `Live` | `Short` | `0.1195` | 899.88 USD | 899.88 USD | 0.00 USD | `+7.29%` | `7,530.40` |
| `Live` | `Short` | `0.1205` | 3,150.00 USD | 2,250.00 USD | 0.00 USD | `+8.19%` | `18,689.00` |
| `Live` | `Short` | `0.1225` | 4,960.00 USD | 1,810.00 USD | 0.00 USD | `+9.98%` | `14,787.10` |
| `Live` | `Short` | `0.1305` | 5,080.00 USD | 119.84 USD | 0.00 USD | `+17.17%` | `918.30` |
| `Live` | `Short` | `0.1355` | 6,420.00 USD | 1,330.00 USD | 0.00 USD | `+21.66%` | `9,843.80` |
| `Live` | `Short` | `0.1555` | 13,330.00 USD | 6,910.00 USD | 0.00 USD | `+39.61%` | `44,438.90` |
| `Live` | `Short` | `0.1565` | 13,880.00 USD | 550.61 USD | 0.00 USD | `+40.51%` | `3,518.30` |
| `Live` | `Short` | `0.1605` | 28,320.00 USD | 14,450.00 USD | 0.00 USD | `+44.10%` | `90,000.40` |
| `Live` | `Short` | `0.1615` | 47,870.00 USD | 19,540.00 USD | 0.00 USD | `+45.00%` | `121,006.70` |
| `Live` | `Short` | `0.1695` | 48,030.00 USD | 169.25 USD | 0.00 USD | `+52.18%` | `998.50` |
| `Live` | `Short` | `0.1855` | 49,670.00 USD | 1,640.00 USD | 0.00 USD | `+66.55%` | `8,827.60` |
| `Live` | `Short` | `0.1865` | 49,840.00 USD | 167.85 USD | 0.00 USD | `+67.44%` | `900.00` |
| `Live` | `Short` | `0.1935` | 50,780.00 USD | 935.32 USD | 0.00 USD | `+73.73%` | `4,833.70` |
| `Live` | `Short` | `0.2155` | 53,010.00 USD | 2,240.00 USD | 0.00 USD | `+93.48%` | `10,387.60` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0635` | 176,240.00 USD | 0.00 USD | 1,140.00 USD | `-42.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 175,100.00 USD | 0.00 USD | 773.46 USD | `-36.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 174,320.00 USD | 0.00 USD | 592.27 USD | `-35.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 173,730.00 USD | 0.00 USD | 755.00 USD | `-32.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0805` | 172,980.00 USD | 0.00 USD | 411.06 USD | `-27.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0815` | 172,570.00 USD | 0.00 USD | 183.49 USD | `-26.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0835` | 172,380.00 USD | 0.00 USD | 456.70 USD | `-25.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 171,930.00 USD | 0.00 USD | 631.58 USD | `-23.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 171,290.00 USD | 0.00 USD | 653.74 USD | `-20.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0915` | 170,640.00 USD | 0.00 USD | 623.91 USD | `-17.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 170,020.00 USD | 0.00 USD | 485.13 USD | `-15.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0975` | 169,530.00 USD | 0.00 USD | 720.22 USD | `-12.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0985` | 168,810.00 USD | 0.00 USD | 1,330.00 USD | `-11.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0995` | 167,480.00 USD | 0.00 USD | 801.64 USD | `-10.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 166,680.00 USD | 0.00 USD | 1,470.00 USD | `-9.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1015` | 165,210.00 USD | 0.00 USD | 903.42 USD | `-8.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 164,300.00 USD | 0.00 USD | 780.70 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1035` | 163,520.00 USD | 0.00 USD | 4,650.00 USD | `-7.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1045` | 158,870.00 USD | 0.00 USD | 18,950.00 USD | `-6.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1055` | 139,920.00 USD | 0.00 USD | 7,770.00 USD | `-5.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1065` | 132,150.00 USD | 0.00 USD | 109,280.00 USD | `-4.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 22,870.00 USD | 0.00 USD | 21,920.00 USD | `-3.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 951.99 USD | 0.00 USD | 150.04 USD | `-2.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1095` | 801.95 USD | 0.00 USD | 639.36 USD | `-1.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 162.59 USD | 0.00 USD | 162.59 USD | `-0.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 839.64 USD | 839.64 USD | 0.00 USD | `+0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1125` | 2,520.00 USD | 1,680.00 USD | 0.00 USD | `+1.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1135` | 2,640.00 USD | 116.27 USD | 0.00 USD | `+1.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1145` | 2,770.00 USD | 134.61 USD | 0.00 USD | `+2.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 3,790.00 USD | 1,020.00 USD | 0.00 USD | `+3.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1165` | 4,260.00 USD | 466.94 USD | 0.00 USD | `+4.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1175` | 4,620.00 USD | 363.49 USD | 0.00 USD | `+5.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1185` | 5,680.00 USD | 1,050.00 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1195` | 20,320.00 USD | 14,640.00 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1205` | 20,710.00 USD | 398.42 USD | 0.00 USD | `+8.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1225` | 180,480.00 USD | 159,770.00 USD | 0.00 USD | `+9.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1235` | 181,110.00 USD | 631.28 USD | 0.00 USD | `+10.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1255` | 196,780.00 USD | 15,670.00 USD | 0.00 USD | `+12.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1265` | 207,240.00 USD | 10,460.00 USD | 0.00 USD | `+13.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1275` | 207,740.00 USD | 492.06 USD | 0.00 USD | `+14.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1305` | 208,180.00 USD | 444.24 USD | 0.00 USD | `+17.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1315` | 208,510.00 USD | 326.09 USD | 0.00 USD | `+18.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1335` | 209,820.00 USD | 1,310.00 USD | 0.00 USD | `+19.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1345` | 213,970.00 USD | 4,150.00 USD | 0.00 USD | `+20.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1365` | 224,660.00 USD | 10,690.00 USD | 0.00 USD | `+22.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1405` | 237,770.00 USD | 13,110.00 USD | 0.00 USD | `+26.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1425` | 237,870.00 USD | 102.22 USD | 0.00 USD | `+27.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1435` | 245,050.00 USD | 7,180.00 USD | 0.00 USD | `+28.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1485` | 247,690.00 USD | 2,650.00 USD | 0.00 USD | `+33.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1495` | 248,490.00 USD | 792.53 USD | 0.00 USD | `+34.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1525` | 252,250.00 USD | 3,770.00 USD | 0.00 USD | `+36.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 252,440.00 USD | 184.49 USD | 0.00 USD | `+39.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 259,160.00 USD | 6,720.00 USD | 0.00 USD | `+40.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 259,380.00 USD | 219.81 USD | 0.00 USD | `+41.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 259,660.00 USD | 277.62 USD | 0.00 USD | `+46.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 261,450.00 USD | 1,800.00 USD | 0.00 USD | `+52.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 261,670.00 USD | 216.55 USD | 0.00 USD | `+56.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 261,780.00 USD | 117.26 USD | 0.00 USD | `+77.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 282,320.00 USD | 20,530.00 USD | 0.00 USD | `+80.01%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0961` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 2,410.00 USD | 1,140.00 USD | 20.68 USD |
| `7D` | `0.0963` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 1,210.00 USD |
| `7D` | `0.0967` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 3,770.00 USD | 2,660.00 USD | 2,840.00 USD |
| `7D` | `0.0969` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 0.00 USD | 2,810.00 USD | 9,360.00 USD |
| `7D` | `0.0971` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 0.00 USD | 2,000.00 USD | 34.36 USD |
| `7D` | `0.0973` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD |
| `7D` | `0.0975` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 0.00 USD | 1,160.00 USD | 4,130.00 USD |
| `7D` | `0.0977` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 5,800.00 USD |
| `7D` | `0.0979` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 0.00 USD | 1,530.00 USD | 5,710.00 USD |
| `7D` | `0.0981` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD |
| `7D` | `0.0983` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 7,990.00 USD | 1,230.00 USD | 8,820.00 USD |
| `1D` | `0.0985` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 8,560.00 USD | 1,710.00 USD | 5,670.00 USD |
| `7D` | `0.0985` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 7,110.00 USD | 0.00 USD | 6,320.00 USD |
| `1D` | `0.0987` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 11,770.00 USD | 2,440.00 USD | 5,600.00 USD |
| `7D` | `0.0987` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 5,390.00 USD | 9,190.00 USD | 37,360.00 USD |
| `1D` | `0.0989` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 2,350.00 USD | 3,330.00 USD | 2,850.00 USD |
| `7D` | `0.0989` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 12,260.00 USD | 4,520.00 USD | 27,240.00 USD |
| `1D` | `0.0991` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 4,350.00 USD | 4,220.00 USD | 4,440.00 USD |
| `7D` | `0.0991` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 14,350.00 USD | 10,350.00 USD | 13,520.00 USD |
| `1D` | `0.0993` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 2,360.00 USD | 1,220.00 USD | 11,780.00 USD |
| `7D` | `0.0993` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 23,920.00 USD | 10,140.00 USD | 24,060.00 USD |
| `1D` | `0.0995` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 2,990.00 USD | 624.33 USD | 12,320.00 USD |
| `7D` | `0.0995` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 13,090.00 USD | 6,160.00 USD | 25,300.00 USD |
| `1D` | `0.0997` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 5,070.00 USD | 1,410.00 USD | 9,320.00 USD |
| `7D` | `0.0997` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 21,100.00 USD | 5,500.00 USD | 29,960.00 USD |
| `1D` | `0.0999` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 4,590.00 USD | 4,070.00 USD | 1,580.00 USD |
| `7D` | `0.0999` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 14,230.00 USD | 6,540.00 USD | 18,810.00 USD |
| `1D` | `0.1001` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 4,190.00 USD | 668.73 USD | 6,190.00 USD |
| `7D` | `0.1001` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 29,230.00 USD | 3,010.00 USD | 10,920.00 USD |
| `1D` | `0.1003` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 0.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1003` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 8,010.00 USD | 7,060.00 USD | 5,210.00 USD |
| `1D` | `0.1005` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 1,970.00 USD | 403.62 USD | 47.02 USD |
| `7D` | `0.1005` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 25,070.00 USD | 11,000.00 USD | 18,310.00 USD |
| `1D` | `0.1007` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 0.00 USD | 430.11 USD | 826.91 USD |
| `7D` | `0.1007` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 10,260.00 USD | 2,280.00 USD | 14,060.00 USD |
| `1D` | `0.1009` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 1,070.00 USD | 842.63 USD | 28.75 USD |
| `7D` | `0.1009` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 15,320.00 USD | 1,660.00 USD | 6,920.00 USD |
| `1D` | `0.1011` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 1,570.00 USD | 1,240.00 USD | 1,300.00 USD |
| `7D` | `0.1011` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 4,430.00 USD | 4,720.00 USD | 8,880.00 USD |
| `1D` | `0.1013` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 774.15 USD | 1,490.00 USD | 587.32 USD |
| `7D` | `0.1013` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 12,870.00 USD | 4,030.00 USD | 3,080.00 USD |
| `1D` | `0.1015` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 2,790.00 USD | 0.00 USD | 2,870.00 USD |
| `7D` | `0.1015` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 6,830.00 USD | 965.35 USD | 2,430.00 USD |
| `1D` | `0.1017` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 1,660.00 USD | 2,060.00 USD | 2,280.00 USD |
| `7D` | `0.1017` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 11,450.00 USD | 2,850.00 USD | 4,790.00 USD |
| `1D` | `0.1019` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 2,800.00 USD | 3,420.00 USD | 2,990.00 USD |
| `7D` | `0.1019` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 3,160.00 USD | 3,310.00 USD | 8,040.00 USD |
| `1D` | `0.1021` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 2,580.00 USD | 1,320.00 USD | 4,740.00 USD |
| `7D` | `0.1021` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 7,900.00 USD | 3,270.00 USD | 7,150.00 USD |
| `1D` | `0.1023` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 1,440.00 USD | 1,390.00 USD | 2,060.00 USD |
| `7D` | `0.1023` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 4,030.00 USD | 4,990.00 USD | 11,010.00 USD |
| `1D` | `0.1025` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 855.19 USD | 947.50 USD | 2,750.00 USD |
| `7D` | `0.1025` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 1,550.00 USD | 0.00 USD | 5,690.00 USD |
| `1D` | `0.1027` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 2,780.00 USD | 1,590.00 USD | 73.56 USD |
| `7D` | `0.1027` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 2,250.00 USD | 1,170.00 USD | 344.47 USD |
| `1D` | `0.1029` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 4,340.00 USD | 705.79 USD | 6,460.00 USD |
| `7D` | `0.1029` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 7,420.00 USD | 3,000.00 USD | 332.49 USD |
| `1D` | `0.1031` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 11,600.00 USD | 3,910.00 USD | 8,060.00 USD |
| `7D` | `0.1031` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 13,690.00 USD | 5,070.00 USD | 10,680.00 USD |
| `1D` | `0.1033` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 8,760.00 USD | 2,790.00 USD | 10,510.00 USD |
| `7D` | `0.1033` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 3,880.00 USD | 2,640.00 USD | 15,240.00 USD |
| `1D` | `0.1035` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 7,450.00 USD | 6,850.00 USD | 10,230.00 USD |
| `7D` | `0.1035` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 2,710.00 USD | 9,400.00 USD | 16,150.00 USD |
| `1D` | `0.1037` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 2,220.00 USD | 13,000.00 USD | 9,240.00 USD |
| `7D` | `0.1037` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 19,390.00 USD |
| `1D` | `0.1039` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 3,660.00 USD | 1,730.00 USD | 11,820.00 USD |
| `7D` | `0.1039` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 0.00 USD | 5,170.00 USD | 167.04 USD |
| `1D` | `0.1041` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 7,790.00 USD | 6,910.00 USD | 13,280.00 USD |
| `7D` | `0.1041` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 5,940.00 USD | 2,910.00 USD | 10,820.00 USD |
| `1D` | `0.1043` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 17,650.00 USD | 5,650.00 USD | 7,840.00 USD |
| `7D` | `0.1043` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 15,960.00 USD | 5,980.00 USD | 21,000.00 USD |
| `1D` | `0.1045` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | 2,600.00 USD | 6,220.00 USD |
| `7D` | `0.1045` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 0.00 USD | 3,830.00 USD | 14,950.00 USD |
| `1D` | `0.1047` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 4,610.00 USD | 2,610.00 USD | 21,540.00 USD |
| `7D` | `0.1047` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 0.00 USD | 1,720.00 USD | 22,630.00 USD |
| `1D` | `0.1049` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 21,050.00 USD | 4,090.00 USD | 10,940.00 USD |
| `7D` | `0.1049` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 34,790.00 USD | 4,810.00 USD | 35,410.00 USD |
| `1D` | `0.1051` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 20,120.00 USD | 10,840.00 USD | 26,370.00 USD |
| `7D` | `0.1051` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 17,290.00 USD | 11,500.00 USD | 48,700.00 USD |
| `1D` | `0.1053` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 41,820.00 USD | 8,170.00 USD | 29,580.00 USD |
| `7D` | `0.1053` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 47,580.00 USD | 29,800.00 USD | 95,610.00 USD |
| `1D` | `0.1055` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 28,290.00 USD | 21,140.00 USD | 35,070.00 USD |
| `7D` | `0.1055` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 50,090.00 USD | 27,290.00 USD | 122,170.00 USD |
| `1D` | `0.1057` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 26,000.00 USD | 26,820.00 USD | 46,300.00 USD |
| `7D` | `0.1057` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 44,200.00 USD | 43,030.00 USD | 74,290.00 USD |
| `1D` | `0.1059` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 17,220.00 USD | 21,420.00 USD | 55,440.00 USD |
| `7D` | `0.1059` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 92,510.00 USD | 49,670.00 USD | 116,360.00 USD |
| `1D` | `0.1061` | 958,950.00 USD | 0.00 USD | 958,950.00 USD | 15,660.00 USD | 9,870.00 USD | 51,490.00 USD |
| `7D` | `0.1061` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 38,260.00 USD | 28,780.00 USD | 76,320.00 USD |
| `1D` | `0.1063` | 881,930.00 USD | 0.00 USD | 881,930.00 USD | 57,650.00 USD | 16,340.00 USD | 53,520.00 USD |
| `7D` | `0.1063` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 95,080.00 USD | 38,330.00 USD | 151,610.00 USD |
| `1D` | `0.1065` | 754,430.00 USD | 0.00 USD | 754,430.00 USD | 19,500.00 USD | 15,700.00 USD | 13,400.00 USD |
| `7D` | `0.1065` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 84,890.00 USD | 21,040.00 USD | 86,060.00 USD |
| `1D` | `0.1067` | 705,830.00 USD | 0.00 USD | 705,830.00 USD | 16,020.00 USD | 14,530.00 USD | 23,940.00 USD |
| `7D` | `0.1067` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 97,290.00 USD | 34,000.00 USD | 67,490.00 USD |
| `1D` | `0.1069` | 651,340.00 USD | 0.00 USD | 651,340.00 USD | 20,560.00 USD | 6,620.00 USD | 54,820.00 USD |
| `7D` | `0.1069` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 76,900.00 USD | 32,620.00 USD | 67,520.00 USD |
| `1D` | `0.1071` | 569,340.00 USD | 0.00 USD | 569,340.00 USD | 48,660.00 USD | 8,170.00 USD | 16,200.00 USD |
| `7D` | `0.1071` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 119,440.00 USD | 27,240.00 USD | 42,730.00 USD |
| `1D` | `0.1073` | 496,310.00 USD | 0.00 USD | 496,310.00 USD | 8,740.00 USD | 10,680.00 USD | 20,870.00 USD |
| `7D` | `0.1073` | 840,080.00 USD | 0.00 USD | 840,080.00 USD | 62,850.00 USD | 17,700.00 USD | 0.00 USD |
| `1D` | `0.1075` | 456,030.00 USD | 0.00 USD | 456,030.00 USD | 11,540.00 USD | 3,900.00 USD | 0.00 USD |
| `7D` | `0.1075` | 759,530.00 USD | 0.00 USD | 759,530.00 USD | 8,720.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1077` | 440,590.00 USD | 0.00 USD | 440,590.00 USD | 3,180.00 USD | 6,210.00 USD | 10,820.00 USD |
| `1D` | `0.1079` | 420,370.00 USD | 0.00 USD | 420,370.00 USD | 9,370.00 USD | 11,900.00 USD | 23,460.00 USD |
| `7D` | `0.1079` | 750,810.00 USD | 0.00 USD | 750,810.00 USD | 123,150.00 USD | 18,520.00 USD | 0.00 USD |
| `1D` | `0.1081` | 375,640.00 USD | 0.00 USD | 375,640.00 USD | 5,870.00 USD | 7,210.00 USD | 46,940.00 USD |
| `7D` | `0.1081` | 609,130.00 USD | 0.00 USD | 609,130.00 USD | 200,110.00 USD | 9,430.00 USD | 28,830.00 USD |
| `1D` | `0.1083` | 315,620.00 USD | 0.00 USD | 315,620.00 USD | 30,270.00 USD | 0.00 USD | 27,290.00 USD |
| `7D` | `0.1083` | 370,770.00 USD | 0.00 USD | 370,770.00 USD | 94,800.00 USD | 0.00 USD | 37,550.00 USD |
| `1D` | `0.1085` | 258,060.00 USD | 0.00 USD | 258,060.00 USD | 14,370.00 USD | 7,490.00 USD | 47,130.00 USD |
| `7D` | `0.1085` | 238,420.00 USD | 0.00 USD | 238,420.00 USD | 15,920.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1087` | 189,070.00 USD | 0.00 USD | 189,070.00 USD | 15,310.00 USD | 6,720.00 USD | 22,870.00 USD |
| `7D` | `0.1087` | 222,500.00 USD | 0.00 USD | 222,500.00 USD | 22,680.00 USD | 0.00 USD | 27,780.00 USD |
| `1D` | `0.1089` | 144,170.00 USD | 0.00 USD | 144,170.00 USD | 41,340.00 USD | 12,040.00 USD | 18,070.00 USD |
| `7D` | `0.1089` | 172,040.00 USD | 0.00 USD | 172,040.00 USD | 0.00 USD | 9,110.00 USD | 0.00 USD |
| `1D` | `0.1091` | 72,720.00 USD | 0.00 USD | 72,720.00 USD | 16,940.00 USD | 2,790.00 USD | 0.00 USD |
| `7D` | `0.1091` | 162,920.00 USD | 0.00 USD | 162,920.00 USD | 16,310.00 USD | 3,800.00 USD | 0.00 USD |
| `1D` | `0.1093` | 52,990.00 USD | 0.00 USD | 52,990.00 USD | 13,100.00 USD | 0.00 USD | 6,220.00 USD |
| `7D` | `0.1095` | 142,820.00 USD | 0.00 USD | 142,820.00 USD | 18,840.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1097` | 123,980.00 USD | 0.00 USD | 123,980.00 USD | 0.00 USD | 2,970.00 USD | 21,590.00 USD |
| `7D` | `0.1099` | 99,410.00 USD | 0.00 USD | 99,410.00 USD | 0.00 USD | 0.00 USD | 25,060.00 USD |
| `7D` | `0.1103` | 74,350.00 USD | 0.00 USD | 74,350.00 USD | 6,930.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1105` | 67,420.00 USD | 0.00 USD | 67,420.00 USD | 0.00 USD | 5,810.00 USD | 0.00 USD |
| `7D` | `0.1107` | 61,610.00 USD | 0.00 USD | 61,610.00 USD | 0.00 USD | 4,120.00 USD | 0.00 USD |
| `1D` | `0.1113` | 33,670.00 USD | 0.00 USD | 33,670.00 USD | 0.00 USD | 8,100.00 USD | 25,570.00 USD |
| `7D` | `0.1113` | 57,490.00 USD | 0.00 USD | 57,490.00 USD | 0.00 USD | 0.00 USD | 57,490.00 USD |
| `7D` | `0.1114` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1115` | 36,130.00 USD | 36,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 36,130.00 USD |
| `1D` | `0.1116` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1117` | 32,500.00 USD | 32,500.00 USD | 0.00 USD | 0.00 USD | 16,900.00 USD | 15,610.00 USD |
| `7D` | `0.1117` | 82,480.00 USD | 82,480.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | 23,580.00 USD |
| `1D` | `0.1119` | 102,900.00 USD | 102,900.00 USD | 0.00 USD | 35,630.00 USD | 7,980.00 USD | 26,780.00 USD |
| `7D` | `0.1119` | 141,140.00 USD | 141,140.00 USD | 0.00 USD | 45,230.00 USD | 2,640.00 USD | 10,800.00 USD |
| `1D` | `0.1121` | 165,970.00 USD | 165,970.00 USD | 0.00 USD | 19,830.00 USD | 16,100.00 USD | 27,140.00 USD |
| `7D` | `0.1121` | 192,410.00 USD | 192,410.00 USD | 0.00 USD | 29,340.00 USD | 9,400.00 USD | 12,530.00 USD |
| `1D` | `0.1123` | 270,830.00 USD | 270,830.00 USD | 0.00 USD | 29,460.00 USD | 26,020.00 USD | 49,380.00 USD |
| `7D` | `0.1123` | 285,790.00 USD | 285,790.00 USD | 0.00 USD | 48,680.00 USD | 18,520.00 USD | 26,180.00 USD |
| `1D` | `0.1125` | 366,810.00 USD | 366,810.00 USD | 0.00 USD | 17,260.00 USD | 13,480.00 USD | 65,240.00 USD |
| `7D` | `0.1125` | 336,770.00 USD | 336,770.00 USD | 0.00 USD | 7,560.00 USD | 14,600.00 USD | 28,830.00 USD |
| `1D` | `0.1127` | 443,580.00 USD | 443,580.00 USD | 0.00 USD | 21,670.00 USD | 10,390.00 USD | 44,720.00 USD |
| `7D` | `0.1127` | 391,130.00 USD | 391,130.00 USD | 0.00 USD | 0.00 USD | 6,460.00 USD | 47,890.00 USD |
| `1D` | `0.1129` | 543,680.00 USD | 543,680.00 USD | 0.00 USD | 32,030.00 USD | 13,140.00 USD | 54,940.00 USD |
| `7D` | `0.1129` | 449,170.00 USD | 449,170.00 USD | 0.00 USD | 31,880.00 USD | 5,980.00 USD | 20,180.00 USD |
| `1D` | `0.1131` | 593,730.00 USD | 593,730.00 USD | 0.00 USD | 15,310.00 USD | 9,680.00 USD | 25,050.00 USD |
| `7D` | `0.1131` | 505,890.00 USD | 505,890.00 USD | 0.00 USD | 22,680.00 USD | 0.00 USD | 34,030.00 USD |
| `1D` | `0.1133` | 641,090.00 USD | 641,090.00 USD | 0.00 USD | 5,610.00 USD | 17,490.00 USD | 24,270.00 USD |
| `7D` | `0.1133` | 518,900.00 USD | 518,900.00 USD | 0.00 USD | 0.00 USD | 12,940.00 USD | 68.72 USD |
| `1D` | `0.1135` | 690,290.00 USD | 690,290.00 USD | 0.00 USD | 27,280.00 USD | 5,410.00 USD | 16,510.00 USD |
| `7D` | `0.1135` | 571,370.00 USD | 571,370.00 USD | 0.00 USD | 32,150.00 USD | 5,520.00 USD | 14,800.00 USD |
| `1D` | `0.1137` | 744,050.00 USD | 744,050.00 USD | 0.00 USD | 34,150.00 USD | 2,430.00 USD | 17,180.00 USD |
| `7D` | `0.1137` | 608,700.00 USD | 608,700.00 USD | 0.00 USD | 30,030.00 USD | 1,730.00 USD | 5,570.00 USD |
| `1D` | `0.1139` | 776,850.00 USD | 776,850.00 USD | 0.00 USD | 10,000.00 USD | 9,360.00 USD | 13,450.00 USD |
| `7D` | `0.1139` | 625,800.00 USD | 625,800.00 USD | 0.00 USD | 0.00 USD | 8,850.00 USD | 8,250.00 USD |
| `1D` | `0.1141` | 799,060.00 USD | 799,060.00 USD | 0.00 USD | 8,780.00 USD | 5,920.00 USD | 7,500.00 USD |
| `7D` | `0.1141` | 643,100.00 USD | 643,100.00 USD | 0.00 USD | 4,360.00 USD | 5,280.00 USD | 7,660.00 USD |
| `1D` | `0.1143` | 816,770.00 USD | 816,770.00 USD | 0.00 USD | 1,590.00 USD | 7,740.00 USD | 8,380.00 USD |
| `7D` | `0.1143` | 717,380.00 USD | 717,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 74,280.00 USD |
| `1D` | `0.1145` | 863,730.00 USD | 863,730.00 USD | 0.00 USD | 8,350.00 USD | 10,790.00 USD | 27,820.00 USD |
| `7D` | `0.1145` | 878,170.00 USD | 878,170.00 USD | 0.00 USD | 10,360.00 USD | 9,260.00 USD | 141,160.00 USD |
| `1D` | `0.1147` | 904,140.00 USD | 904,140.00 USD | 0.00 USD | 8,840.00 USD | 4,840.00 USD | 26,730.00 USD |
| `7D` | `0.1147` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 4,720.00 USD | 134,400.00 USD |
| `1D` | `0.1149` | 944,560.00 USD | 944,560.00 USD | 0.00 USD | 11,450.00 USD | 0.00 USD | 28,970.00 USD |
| `7D` | `0.1149` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 72,860.00 USD |
| `1D` | `0.1151` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 21,200.00 USD | 3,740.00 USD | 43,920.00 USD |
| `7D` | `0.1151` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 92,570.00 USD | 0.00 USD | 118,840.00 USD |
| `1D` | `0.1153` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 30,050.00 USD | 15,960.00 USD | 26,300.00 USD |
| `7D` | `0.1153` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 147,450.00 USD | 0.00 USD | 132,290.00 USD |
| `1D` | `0.1155` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 18,450.00 USD | 26,450.00 USD | 28,590.00 USD |
| `7D` | `0.1155` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 108,940.00 USD | 24,970.00 USD | 71,140.00 USD |
| `1D` | `0.1157` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 29,940.00 USD | 11,110.00 USD | 35,640.00 USD |
| `7D` | `0.1157` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 163,490.00 USD | 3,760.00 USD | 48,220.00 USD |
| `1D` | `0.1159` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 7,810.00 USD | 8,370.00 USD | 8,850.00 USD |
| `7D` | `0.1159` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 105,000.00 USD | 12,710.00 USD | 48,790.00 USD |
| `1D` | `0.1161` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 25,800.00 USD | 6,970.00 USD | 33,890.00 USD |
| `7D` | `0.1161` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 155,210.00 USD | 37,250.00 USD | 82,510.00 USD |
| `1D` | `0.1163` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 18,210.00 USD | 6,750.00 USD | 1,990.00 USD |
| `7D` | `0.1163` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 74,250.00 USD | 11,460.00 USD | 68,760.00 USD |
| `1D` | `0.1165` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 9,310.00 USD | 11,840.00 USD | 3,670.00 USD |
| `7D` | `0.1165` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 77,390.00 USD | 25,170.00 USD | 27,180.00 USD |
| `1D` | `0.1167` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 15,040.00 USD | 13,350.00 USD | 3,010.00 USD |
| `7D` | `0.1167` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 79,610.00 USD | 21,620.00 USD | 41,230.00 USD |
| `1D` | `0.1169` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 16,040.00 USD | 4,020.00 USD | 15,910.00 USD |
| `7D` | `0.1169` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 60,400.00 USD | 14,840.00 USD | 86,730.00 USD |
| `1D` | `0.1171` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 5,230.00 USD | 4,520.00 USD | 1,490.00 USD |
| `7D` | `0.1171` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 52,070.00 USD | 9,140.00 USD | 35,080.00 USD |
| `1D` | `0.1173` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 14,960.00 USD | 3,470.00 USD | 7,820.00 USD |
| `7D` | `0.1173` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 40,860.00 USD | 7,080.00 USD | 31,840.00 USD |
| `1D` | `0.1175` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 9,050.00 USD | 10,790.00 USD | 6,450.00 USD |
| `7D` | `0.1175` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 38,840.00 USD | 8,100.00 USD | 58,660.00 USD |
| `1D` | `0.1177` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 7,820.00 USD | 8,560.00 USD | 8,530.00 USD |
| `7D` | `0.1177` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 13,120.00 USD | 14,140.00 USD | 27,040.00 USD |
| `1D` | `0.1179` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 17,010.00 USD | 5,840.00 USD | 14,500.00 USD |
| `7D` | `0.1179` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 61,380.00 USD | 10,940.00 USD | 23,410.00 USD |
| `1D` | `0.1181` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 5,740.00 USD | 4,210.00 USD | 6,940.00 USD |
| `7D` | `0.1181` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 22,290.00 USD | 15,780.00 USD | 17,730.00 USD |
| `1D` | `0.1183` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 7,310.00 USD | 1,400.00 USD | 9,080.00 USD |
| `7D` | `0.1183` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 4,040.00 USD | 1,800.00 USD | 30,890.00 USD |
| `1D` | `0.1185` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 6,370.00 USD | 3,940.00 USD | 11,100.00 USD |
| `7D` | `0.1185` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 3,880.00 USD | 5,130.00 USD | 22,270.00 USD |
| `1D` | `0.1187` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 11,520.00 USD | 8,520.00 USD | 6,250.00 USD |
| `7D` | `0.1187` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 5,620.00 USD | 11,840.00 USD | 32,090.00 USD |
| `1D` | `0.1189` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 4,220.00 USD | 3,060.00 USD | 4,330.00 USD |
| `7D` | `0.1189` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 27,240.00 USD | 15,060.00 USD | 3,180.00 USD |
| `1D` | `0.1191` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 4,940.00 USD | 6,690.00 USD | 3,460.00 USD |
| `7D` | `0.1191` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 22,650.00 USD | 15,330.00 USD | 109,070.00 USD |
| `1D` | `0.1193` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 4,720.00 USD | 2,080.00 USD | 3,770.00 USD |
| `7D` | `0.1193` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 21,260.00 USD | 0.00 USD | 9,460.00 USD |
| `1D` | `0.1195` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 9,550.00 USD | 3,210.00 USD | 2,730.00 USD |
| `7D` | `0.1195` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 11,190.00 USD | 1,780.00 USD | 29,460.00 USD |
| `1D` | `0.1197` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 1,040.00 USD | 13.79 USD |
| `7D` | `0.1197` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 6,780.00 USD | 10,800.00 USD | 14,060.00 USD |
| `1D` | `0.1199` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 3,050.00 USD | 3,040.00 USD |
| `7D` | `0.1199` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 9,100.00 USD | 0.00 USD | 64,660.00 USD |
| `1D` | `0.1201` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 6,460.00 USD | 1,070.00 USD | 10,160.00 USD |
| `7D` | `0.1201` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 114,140.00 USD | 16,380.00 USD | 29,030.00 USD |
| `1D` | `0.1203` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 7,150.00 USD | 1,250.00 USD | 2,680.00 USD |
| `7D` | `0.1203` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 70,770.00 USD | 29,250.00 USD | 6,330.00 USD |
| `1D` | `0.1205` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 2,250.00 USD | 1,910.00 USD | 759.49 USD |
| `7D` | `0.1205` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 86,480.00 USD | 48,720.00 USD | 128,340.00 USD |
| `1D` | `0.1207` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 9,520.00 USD | 524.23 USD | 4,880.00 USD |
| `7D` | `0.1207` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 12,460.00 USD | 19,400.00 USD | 59,650.00 USD |
| `1D` | `0.1209` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 2,350.00 USD | 3,330.00 USD | 2,870.00 USD |
| `7D` | `0.1209` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 85,160.00 USD | 19,340.00 USD | 94,120.00 USD |
| `1D` | `0.1211` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 4,350.00 USD | 4,220.00 USD | 4,460.00 USD |
| `7D` | `0.1211` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 35,090.00 USD | 18,720.00 USD | 29,580.00 USD |
| `1D` | `0.1213` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 2,360.00 USD | 1,220.00 USD | 11,780.00 USD |
| `7D` | `0.1213` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 32,700.00 USD | 29,060.00 USD | 24,230.00 USD |
| `1D` | `0.1215` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD | 4,180.00 USD |
| `7D` | `0.1215` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 27,750.00 USD | 9,240.00 USD | 59,120.00 USD |
| `1D` | `0.1217` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 1,330.00 USD | 624.33 USD | 8,180.00 USD |
| `7D` | `0.1217` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 18,490.00 USD | 26,300.00 USD | 11,210.00 USD |
| `1D` | `0.1219` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 5,070.00 USD | 1,410.00 USD | 9,320.00 USD |
| `7D` | `0.1219` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 26,700.00 USD | 5,500.00 USD | 35,080.00 USD |
| `1D` | `0.1221` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 4,590.00 USD | 4,070.00 USD | 1,620.00 USD |
| `7D` | `0.1221` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 47,890.00 USD | 21,770.00 USD | 18,920.00 USD |
| `1D` | `0.1223` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 4,190.00 USD | 668.73 USD | 6,120.00 USD |
| `7D` | `0.1223` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 103,180.00 USD | 36,290.00 USD | 48,470.00 USD |
| `1D` | `0.1225` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1225` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 50,540.00 USD | 26,800.00 USD | 10,780.00 USD |
| `1D` | `0.1227` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1227` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 75,750.00 USD | 31,790.00 USD | 58,740.00 USD |
| `1D` | `0.1229` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 403.62 USD | 0.00 USD |
| `7D` | `0.1229` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 87,270.00 USD | 41,310.00 USD | 50,470.00 USD |
| `1D` | `0.1231` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 430.11 USD | 789.22 USD |
| `7D` | `0.1231` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 29,380.00 USD | 31,660.00 USD | 30,200.00 USD |
| `1D` | `0.1232` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 842.63 USD | 0.00 USD |
| `7D` | `0.1233` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 65,180.00 USD | 12,850.00 USD | 39,960.00 USD |
| `7D` | `0.1234` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 8,540.00 USD | 5,200.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `75.49M` | Total OI Tokens: `678,330,540.3 OP`
  * 1h OI Change: `+1.83%` | 4h OI Change: `+3.16%` | 24h OI Change: `-1.83%`
  * Exchange Breakdown: Binance=`17.19M` | Bybit=`14.40M` | OKX=`4.31M` | Hyperliquid=`4.01M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.21K` | Last 24h: `-2.15K` | Last 3d: `-6.96K` | Last 7d: `-22.41K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0037%` | **USDT OKX** | `0.0052%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0036%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0139%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `48.59%` | `51.41%` | `0.95` | 11,690,000.00 USD |
| `15M` | `Binance` | `48.03%` | `51.97%` | `0.92` | 4,370,000.00 USD |
| `15M` | `OKX` | `45.62%` | `54.38%` | `0.84` | 1,480,000.00 USD |
| `15M` | `Bybit` | `44.23%` | `55.77%` | `0.79` | 1,370,000.00 USD |
| `15M` | `KuCoin` | `44.91%` | `55.09%` | `0.82` | 77,430.00 USD |
| `15M` | `Gate` | `71.08%` | `28.92%` | `2.46` | 170,510.00 USD |
| `15M` | `Bitget` | `61.77%` | `38.23%` | `1.62` | 776,430.00 USD |
| `15M` | `BingX` | `58.18%` | `41.82%` | `1.39` | 524,850.00 USD |
| `15M` | `MEXC` | `49.32%` | `50.68%` | `0.97` | 815,770.00 USD |
| `15M` | `Bitunix` | `54.75%` | `45.25%` | `1.21` | 263,360.00 USD |
| `15M` | `Hyperliquid` | `19.74%` | `80.26%` | `0.25` | 960,880.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.02%` | `50.98%` | `0.96` | 160,960.00 USD |
| `15M` | `Crypto.com` | `2.98%` | `97.02%` | `0.03` | 894.21 USD |
| `15M` | `WhiteBIT` | `78.91%` | `21.09%` | `3.74` | 608,560.00 USD |
| `15M` | `HTX` | `31.08%` | `68.92%` | `0.45` | 3,160.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `50.39%` | `49.61%` | `1.02` | 80,050.00 USD |
| `15M` | `Aster` | `87.2%` | `12.8%` | `6.81` | 10,330.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `69.31%` | `30.69%` | `2.26` | 26,140.00 USD |
| `15M` | `Whale Positions` | `48.03%` | `51.97%` | `0.92` | 4,370,000.00 USD |
| `15M` | `Global Accounts` | `48.59%` | `51.41%` | `0.95` | 11,690,000.00 USD |
| `1H` | `OP` | `48.74%` | `51.26%` | `0.95` | 105,400,000.00 USD |
| `1H` | `Binance` | `47.74%` | `52.26%` | `0.91` | 44,070,000.00 USD |
| `1H` | `OKX` | `49.09%` | `50.91%` | `0.96` | 15,990,000.00 USD |
| `1H` | `Bybit` | `50.11%` | `49.89%` | `1.00` | 14,790,000.00 USD |
| `1H` | `KuCoin` | `52.18%` | `47.82%` | `1.09` | 654,980.00 USD |
| `1H` | `Gate` | `45.8%` | `54.2%` | `0.85` | 1,490,000.00 USD |
| `1H` | `Bitget` | `52.93%` | `47.07%` | `1.12` | 5,690,000.00 USD |
| `1H` | `BingX` | `44.95%` | `55.05%` | `0.82` | 3,620,000.00 USD |
| `1H` | `MEXC` | `47.63%` | `52.37%` | `0.91` | 4,990,000.00 USD |
| `1H` | `Bitunix` | `49.16%` | `50.84%` | `0.97` | 3,050,000.00 USD |
| `1H` | `Hyperliquid` | `40.68%` | `59.32%` | `0.69` | 4,990,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.63%` | `52.37%` | `0.91` | 832,510.00 USD |
| `1H` | `Crypto.com` | `47.76%` | `52.24%` | `0.91` | 17,040.00 USD |
| `1H` | `WhiteBIT` | `68.96%` | `31.04%` | `2.22` | 2,630,000.00 USD |
| `1H` | `HTX` | `51.53%` | `48.47%` | `1.06` | 254,090.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `52.07%` | `47.93%` | `1.09` | 1,520,000.00 USD |
| `1H` | `Aster` | `49.96%` | `50.04%` | `1.00` | 31,510.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `44.44%` | `55.56%` | `0.80` | 783,090.00 USD |
| `1H` | `Whale Positions` | `47.74%` | `52.26%` | `0.91` | 44,070,000.00 USD |
| `1H` | `Global Accounts` | `48.74%` | `51.26%` | `0.95` | 105,400,000.00 USD |
| `4H` | `OP` | `50.58%` | `49.42%` | `1.02` | 305,880,000.00 USD |
| `4H` | `Binance` | `48.76%` | `51.24%` | `0.95` | 119,940,000.00 USD |
| `4H` | `OKX` | `50.54%` | `49.46%` | `1.02` | 43,230,000.00 USD |
| `4H` | `Bybit` | `50.37%` | `49.63%` | `1.01` | 39,860,000.00 USD |
| `4H` | `KuCoin` | `50.56%` | `49.44%` | `1.02` | 2,310,000.00 USD |
| `4H` | `Gate` | `49.81%` | `50.19%` | `0.99` | 4,900,000.00 USD |
| `4H` | `Bitget` | `49.55%` | `50.45%` | `0.98` | 15,710,000.00 USD |
| `4H` | `BingX` | `44.32%` | `55.68%` | `0.80` | 14,100,000.00 USD |
| `4H` | `MEXC` | `44.95%` | `55.05%` | `0.82` | 15,360,000.00 USD |
| `4H` | `Bitunix` | `48.83%` | `51.17%` | `0.95` | 10,200,000.00 USD |
| `4H` | `Hyperliquid` | `48.32%` | `51.68%` | `0.93` | 18,580,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.26%` | `49.74%` | `1.01` | 2,290,000.00 USD |
| `4H` | `Crypto.com` | `50.89%` | `49.11%` | `1.04` | 28,550.00 USD |
| `4H` | `WhiteBIT` | `86.12%` | `13.88%` | `6.20` | 9,900,000.00 USD |
| `4H` | `HTX` | `51.32%` | `48.68%` | `1.05` | 504,520.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `58.6%` | `41.4%` | `1.42` | 3,160,000.00 USD |
| `4H` | `Aster` | `90.41%` | `9.59%` | `9.43` | 2,750,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.8%` | `51.2%` | `0.95` | 3,060,000.00 USD |
| `4H` | `Whale Positions` | `48.76%` | `51.24%` | `0.95` | 119,940,000.00 USD |
| `4H` | `Global Accounts` | `50.58%` | `49.42%` | `1.02` | 305,880,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1102` | `0.1101` | `0.1102` | `0.1104` | `0.1098` | 211,329.98 USD | 98,190.43 USD | 113,139.54 USD | -14,949.11 USD | `-7.07%` | `6B / 13S` |
| `0:00 UTC` | `0.1094` | `0.1095` | `0.1094` | `0.1100` | `0.1093` | 411,857.05 USD | 168,352.47 USD | 243,504.58 USD | -75,152.12 USD | `-18.25%` | `7B / 12S` |
| `5:00 UTC` | `0.1097` | `0.1097` | `0.1097` | `0.1099` | `0.1095` | 231,727.41 USD | 134,913.35 USD | 96,814.06 USD | 38,099.28 USD | `+16.44%` | `11B / 4S` |
| `0:00 UTC` | `0.1100` | `0.1102` | `0.1100` | `0.1107` | `0.1097` | 522,440.60 USD | 292,430.01 USD | 230,010.59 USD | 62,419.42 USD | `+11.95%` | `25B / 7S` |
| `5:00 UTC` | `0.1105` | `0.1104` | `0.1105` | `0.1106` | `0.1101` | 269,695.80 USD | 148,564.64 USD | 121,131.16 USD | 27,433.48 USD | `+10.17%` | `14B / 11S` |
| `0:00 UTC` | `0.1112` | `0.1110` | `0.1112` | `0.1114` | `0.1105` | 559,599.22 USD | 273,423.88 USD | 286,175.34 USD | -12,751.46 USD | `-2.28%` | `16B / 12S` |
| `5:00 UTC` | `0.1108` | `0.1107` | `0.1108` | `0.1112` | `0.1104` | 411,261.97 USD | 229,894.15 USD | 181,367.82 USD | 48,526.33 USD | `+11.80%` | `24B / 9S` |
| `0:00 UTC` | `0.1107` | `0.1107` | `0.1107` | `0.1112` | `0.1103` | 551,290.91 USD | 307,591.69 USD | 243,699.23 USD | 63,892.46 USD | `+11.59%` | `17B / 5S` |
| `5:00 UTC` | `0.1110` | `0.1112` | `0.1110` | `0.1118` | `0.1108` | 510,110.63 USD | 294,926.48 USD | 215,184.15 USD | 79,742.32 USD | `+15.63%` | `19B / 5S` |
| `0:00 UTC` | `0.1110` | `0.1112` | `0.1110` | `0.1116` | `0.1109` | 277,464.97 USD | 150,217.56 USD | 127,247.41 USD | 22,970.16 USD | `+8.28%` | `16B / 8S` |

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
| `5m` | 59.89 USD | 369.04 USD | **`ACCUMULATION`** |
| `15m` | 8,020.00 USD | 120,150.00 USD | **`ACCUMULATION`** |
| `30m` | -16,380.00 USD | 261,590.00 USD | **`ACCUMULATION`** |
| `1h` | 19,260.00 USD | 326,730.00 USD | **`ACCUMULATION`** |
| `2h` | 98,020.00 USD | 495,500.00 USD | **`ACCUMULATION`** |
| `4h` | 120,530.00 USD | 542,020.00 USD | **`ACCUMULATION`** |
| `6h` | 130,190.00 USD | 717,270.00 USD | **`ACCUMULATION`** |
| `8h` | 135,390.00 USD | 899,210.00 USD | **`ACCUMULATION`** |
| `12h` | 98,710.00 USD | -436,670.00 USD | **`DISTRIBUTION`** |
| `24h` | 148,090.00 USD | -783,100.00 USD | **`DISTRIBUTION`** |
| `1w` | -323,650.00 USD | -10,660,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,860,000.00 USD | -79,930,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+59.89` | 15m=`+8.02K` | 1h=`+19.26K` | 24h=`+148.09K`
* Futures Capital Netflows: 5m=`+369.04` | 15m=`+120.15K` | 1h=`+326.73K` | 24h=`-783.10K`
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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
