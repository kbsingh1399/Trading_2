# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 11:47:32 IST` (`2026-10-30 06:17:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1021` | `0.1023` | `0.1015` | `0.1023` | `1,204,426` | 122,783.29 USD | 25,511.83 USD | `+20.78%` | -1,702,793.39 USD | `+0.15` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.1023` | `0.1031` | `0.1023` | `0.1029` | `1,789,964` | 183,947.57 USD | 26,265.91 USD | `+14.28%` | -1,676,527.48 USD | `+0.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1029` | `0.1031` | `0.1026` | `0.1030` | `690,675` | 71,026.24 USD | 11,346.58 USD | `+15.98%` | -1,665,180.91 USD | `-0.35` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1023` | `0.1029` | `0.1022` | `0.1027` | `3,621,694` | 371,349.35 USD | 23,454.63 USD | `+6.32%` | -1,751,148.65 USD | `+0.11` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1027` | `0.1027` | `0.1019` | `0.1021` | `3,669,678` | 375,921.80 USD | 22,843.43 USD | `+6.08%` | -1,728,305.22 USD | `+0.09` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1021` | `0.1031` | `0.1015` | `0.1030` | `3,685,247` | 377,775.86 USD | 63,143.08 USD | `+16.71%` | -1,665,162.14 USD | `+0.43` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.0993` | `0.1013` | `0.0988` | `0.1012` | `16,216,904` | 1,626,948.60 USD | 318,721.56 USD | `+19.59%` | -1,821,164.58 USD | `+0.94` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.1012` | `0.1029` | `0.1012` | `0.1021` | `17,484,743` | 1,788,683.49 USD | 174,243.22 USD | `+9.74%` | -1,646,921.37 USD | `+0.61` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1021` | `0.1031` | `0.1015` | `0.1030` | `3,685,065` | 377,757.10 USD | 63,124.31 USD | `+16.71%` | -1,583,797.05 USD | `+0.36` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -1,009,359.71 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,347,386.10 USD | `-1.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1031` | `0.0988` | `0.1030` | `37,386,713` | 3,793,389.18 USD | 556,089.09 USD | `+14.66%` | -1,791,297.01 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | 483,978.43 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | 307,838.15 USD | `-1.31` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -1,009,359.71 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,347,386.10 USD | `-1.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1031` | `0.0988` | `0.1030` | `37,386,713` | 3,793,389.18 USD | 556,089.09 USD | `+14.66%` | -1,791,297.01 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:43:56 IST` |

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
| `Live` | `Long Liquidation` | `0.0285` | 145.32 USD | 124,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0305` | 1,320.00 USD | 124,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0375` | 225.00 USD | 122,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0395` | 271.86 USD | 122,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 410.01 USD | 122,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 4,840.00 USD | 121,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 1,100.00 USD | 117,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 353.81 USD | 116,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 361.16 USD | 115,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 518.48 USD | 115,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 1,920.00 USD | 114,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 1,090.00 USD | 112,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 64,900.00 USD | 111,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,530.00 USD | 46,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,300.00 USD | 44,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 12,440.00 USD | 42,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 1,320.00 USD | 29,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 878.62 USD | 28,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 339.50 USD | 27,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 2,710.00 USD | 27,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 223.98 USD | 24,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 1,560.00 USD | 24,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 140.74 USD | 22,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0827` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0829` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 28.49 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0845` | 14,300.00 USD | 22,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 1,710.00 USD | 8,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0859` | 2,200,000.00 USD | 2,200,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0861` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0863` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 1,880.00 USD | 4,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0865` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 1,980.00 USD | 13,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0865` | 146.06 USD | 6,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0867` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0869` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0871` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 1,200.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0873` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 4,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0875` | 2,160,000.00 USD | 2,160,000.00 USD | 6,010.00 USD | 0.00 USD | 4,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0875` | 793.17 USD | 6,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0877` | 2,150,000.00 USD | 2,150,000.00 USD | 7,820.00 USD | 6,050.00 USD | 22,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0879` | 2,110,000.00 USD | 2,110,000.00 USD | 1,370.00 USD | 2,010.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0881` | 2,090,000.00 USD | 2,090,000.00 USD | 9,390.00 USD | 2,270.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0883` | 2,080,000.00 USD | 2,080,000.00 USD | 7,040.00 USD | 6,800.00 USD | 21,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0885` | 2,040,000.00 USD | 2,040,000.00 USD | 1,000.00 USD | 1,220.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0887` | 1,670,000.00 USD | 1,670,000.00 USD | 7,550.00 USD | 2,580.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0887` | 2,040,000.00 USD | 2,040,000.00 USD | 10,610.00 USD | 2,920.00 USD | 17,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0889` | 1,650,000.00 USD | 1,650,000.00 USD | 727.20 USD | 1,680.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0889` | 2,010,000.00 USD | 2,010,000.00 USD | 10,710.00 USD | 3,200.00 USD | 13,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0891` | 1,640,000.00 USD | 1,640,000.00 USD | 755.35 USD | 1,580.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0891` | 1,980,000.00 USD | 1,980,000.00 USD | 6,310.00 USD | 3,960.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0893` | 1,640,000.00 USD | 1,640,000.00 USD | 983.61 USD | 0.00 USD | 542.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0893` | 1,970,000.00 USD | 1,970,000.00 USD | 5,230.00 USD | 3,080.00 USD | 5,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0895` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 1,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0895` | 1,950,000.00 USD | 1,950,000.00 USD | 4,480.00 USD | 2,110.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,270.00 USD | 5,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0897` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 1,330.00 USD | 11.07 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0897` | 1,940,000.00 USD | 1,940,000.00 USD | 4,670.00 USD | 0.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0899` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 21.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0899` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 927.82 USD | 4,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0901` | 1,630,000.00 USD | 1,630,000.00 USD | 3,320.00 USD | 1,000.00 USD | 18.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0901` | 1,930,000.00 USD | 1,930,000.00 USD | 1,250.00 USD | 428.11 USD | 17.63 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0903` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 3,440.00 USD | 2,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0903` | 1,930,000.00 USD | 1,930,000.00 USD | 5,330.00 USD | 1,480.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0905` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 486.35 USD | 2,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0905` | 1,920,000.00 USD | 1,920,000.00 USD | 6,050.00 USD | 0.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0905` | 2,230.00 USD | 2,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0907` | 1,620,000.00 USD | 1,620,000.00 USD | 1,250.00 USD | 245.42 USD | 2,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0907` | 1,910,000.00 USD | 1,910,000.00 USD | 2,780.00 USD | 2,880.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0909` | 1,620,000.00 USD | 1,620,000.00 USD | 938.76 USD | 1,360.00 USD | 786.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0909` | 1,900,000.00 USD | 1,900,000.00 USD | 1,180.00 USD | 2,200.00 USD | 83.37 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0911` | 1,610,000.00 USD | 1,610,000.00 USD | 5,580.00 USD | 1,450.00 USD | 58.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0911` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0913` | 1,610,000.00 USD | 1,610,000.00 USD | 1,930.00 USD | 465.26 USD | 787.25 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0913` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 74.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0915` | 1,600,000.00 USD | 1,600,000.00 USD | 6,590.00 USD | 2,510.00 USD | 76.57 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0915` | 1,890,000.00 USD | 1,890,000.00 USD | 1,670.00 USD | 903.90 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0917` | 1,590,000.00 USD | 1,590,000.00 USD | 3,850.00 USD | 3,470.00 USD | 71.54 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0917` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0919` | 1,590,000.00 USD | 1,590,000.00 USD | 4,980.00 USD | 1,090.00 USD | 19,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0919` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 142.43 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0921` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 750.63 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0921` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 80.96 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0923` | 1,560,000.00 USD | 1,560,000.00 USD | 3,300.00 USD | 3,620.00 USD | 25,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0923` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 6,430.00 USD | 43,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0925` | 1,520,000.00 USD | 1,520,000.00 USD | 4,780.00 USD | 3,340.00 USD | 26,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0925` | 1,830,000.00 USD | 1,830,000.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0929` | 1,490,000.00 USD | 1,490,000.00 USD | 4,360.00 USD | 1,190.00 USD | 16.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0929` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0931` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 7,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0931` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0933` | 1,480,000.00 USD | 1,480,000.00 USD | 16,500.00 USD | 0.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0933` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 108.72 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0935` | 1,450,000.00 USD | 1,450,000.00 USD | 8,990.00 USD | 7,300.00 USD | 15,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0935` | 1,810,000.00 USD | 1,810,000.00 USD | 19,560.00 USD | 8,160.00 USD | 31,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0937` | 1,420,000.00 USD | 1,420,000.00 USD | 4,580.00 USD | 6,660.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0937` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 248.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0939` | 1,390,000.00 USD | 1,390,000.00 USD | 3,590.00 USD | 2,140.00 USD | 44,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0939` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 10,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0941` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 9,410.00 USD | 21,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0941` | 1,740,000.00 USD | 1,740,000.00 USD | 16,100.00 USD | 18,340.00 USD | 79,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0943` | 1,310,000.00 USD | 1,310,000.00 USD | 3,500.00 USD | 10,920.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0943` | 1,620,000.00 USD | 1,620,000.00 USD | 8,040.00 USD | 0.00 USD | 37,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0945` | 1,270,000.00 USD | 1,270,000.00 USD | 15,750.00 USD | 6,510.00 USD | 44,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0945` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 3,820.00 USD | 106.10 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0947` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 962.66 USD | 91.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0947` | 1,570,000.00 USD | 1,570,000.00 USD | 2,200.00 USD | 0.00 USD | 87.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0949` | 1,200,000.00 USD | 1,200,000.00 USD | 12,180.00 USD | 5,770.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0949` | 1,570,000.00 USD | 1,570,000.00 USD | 3,770.00 USD | 9,700.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0951` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 2,030.00 USD | 19,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0951` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 65.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0953` | 1,160,000.00 USD | 1,160,000.00 USD | 33,000.00 USD | 4,360.00 USD | 6,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0953` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 8,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0955` | 1,110,000.00 USD | 1,110,000.00 USD | 17,990.00 USD | 14,600.00 USD | 31,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0955` | 1,520,000.00 USD | 1,520,000.00 USD | 39,120.00 USD | 13,670.00 USD | 51,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0957` | 1,050,000.00 USD | 1,050,000.00 USD | 16,340.00 USD | 6,740.00 USD | 48,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0957` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 132.97 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0959` | 976,670.00 USD | 976,670.00 USD | 0.00 USD | 3,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0959` | 1,420,000.00 USD | 1,420,000.00 USD | 28,110.00 USD | 0.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0961` | 973,570.00 USD | 973,570.00 USD | 8,920.00 USD | 23,950.00 USD | 23,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0961` | 1,370,000.00 USD | 1,370,000.00 USD | 12,340.00 USD | 16,920.00 USD | 94,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0963` | 917,400.00 USD | 917,400.00 USD | 23,240.00 USD | 11,750.00 USD | 11,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0963` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 4,020.00 USD | 205.72 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0965` | 870,430.00 USD | 870,430.00 USD | 8,250.00 USD | 5,890.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0965` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 2,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0967` | 835,860.00 USD | 835,860.00 USD | 0.00 USD | 1,960.00 USD | 818.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0967` | 1,240,000.00 USD | 1,240,000.00 USD | 3,770.00 USD | 0.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0969` | 833,080.00 USD | 833,080.00 USD | 6,930.00 USD | 7,530.00 USD | 8,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0969` | 1,230,000.00 USD | 1,230,000.00 USD | 3,720.00 USD | 7,090.00 USD | 61,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0971` | 810,530.00 USD | 810,530.00 USD | 2,840.00 USD | 4,070.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0973` | 793,380.00 USD | 793,380.00 USD | 1,440.00 USD | 10,220.00 USD | 1,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0973` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0975` | 779,740.00 USD | 779,740.00 USD | 0.00 USD | 0.00 USD | 56.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0975` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 177.38 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0977` | 779,680.00 USD | 779,680.00 USD | 0.00 USD | 765.93 USD | 911.50 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0979` | 778,010.00 USD | 778,010.00 USD | 1,330.00 USD | 2,280.00 USD | 21,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0981` | 753,280.00 USD | 753,280.00 USD | 3,830.00 USD | 5,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0983` | 744,440.00 USD | 744,440.00 USD | 5,270.00 USD | 7,660.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 3,720.00 USD | 11,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0985` | 727,700.00 USD | 727,700.00 USD | 4,060.00 USD | 4,210.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0985` | 1,130,000.00 USD | 1,130,000.00 USD | 5,310.00 USD | 9,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0987` | 714,990.00 USD | 714,990.00 USD | 25,300.00 USD | 3,920.00 USD | 11,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0987` | 1,110,000.00 USD | 1,110,000.00 USD | 5,390.00 USD | 15,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0989` | 673,970.00 USD | 673,970.00 USD | 2,180.00 USD | 1,540.00 USD | 21,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 1,090,000.00 USD | 1,090,000.00 USD | 12,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0991` | 648,530.00 USD | 648,530.00 USD | 69,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0991` | 1,080,000.00 USD | 1,080,000.00 USD | 14,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0993` | 578,590.00 USD | 578,590.00 USD | 22,410.00 USD | 3,020.00 USD | 43,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0993` | 1,070,000.00 USD | 1,070,000.00 USD | 63,040.00 USD | 0.00 USD | 50,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0995` | 509,960.00 USD | 509,960.00 USD | 16,240.00 USD | 898.20 USD | 49,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 952,170.00 USD | 952,170.00 USD | 13,090.00 USD | 0.00 USD | 25,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0997` | 443,390.00 USD | 443,390.00 USD | 17,900.00 USD | 7,370.00 USD | 55,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0997` | 913,950.00 USD | 913,950.00 USD | 21,100.00 USD | 11,200.00 USD | 32,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0999` | 362,620.00 USD | 362,620.00 USD | 0.00 USD | 11,820.00 USD | 47,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0999` | 848,760.00 USD | 848,760.00 USD | 42,340.00 USD | 11,480.00 USD | 104,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1001` | 302,900.00 USD | 302,900.00 USD | 2,670.00 USD | 2,920.00 USD | 42,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 690,310.00 USD | 690,310.00 USD | 41,570.00 USD | 19,930.00 USD | 105,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1003` | 254,810.00 USD | 254,810.00 USD | 29,140.00 USD | 0.00 USD | 27,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1003` | 523,080.00 USD | 523,080.00 USD | 8,010.00 USD | 0.00 USD | 27,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1005` | 198,470.00 USD | 198,470.00 USD | 21,010.00 USD | 21,540.00 USD | 36,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1005` | 487,170.00 USD | 487,170.00 USD | 35,700.00 USD | 16,500.00 USD | 63,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1007` | 119,040.00 USD | 119,040.00 USD | 11,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 371,270.00 USD | 371,270.00 USD | 10,260.00 USD | 3,080.00 USD | 54,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1009` | 107,130.00 USD | 107,130.00 USD | 6,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1009` | 303,170.00 USD | 303,170.00 USD | 15,320.00 USD | 10,160.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1011` | 100,200.00 USD | 100,200.00 USD | 0.00 USD | 4,070.00 USD | 15,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1011` | 223,670.00 USD | 223,670.00 USD | 4,430.00 USD | 4,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1013` | 80,400.00 USD | 80,400.00 USD | 0.00 USD | 0.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 214,530.00 USD | 214,530.00 USD | 32,420.00 USD | 27,180.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1015` | 69,890.00 USD | 69,890.00 USD | 4,580.00 USD | 1,220.00 USD | 13,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1015` | 129,480.00 USD | 129,480.00 USD | 6,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1017` | 50,870.00 USD | 50,870.00 USD | 3,590.00 USD | 0.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1017` | 122,650.00 USD | 122,650.00 USD | 11,450.00 USD | 0.00 USD | 10,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1019` | 36,170.00 USD | 36,170.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1019` | 100,560.00 USD | 100,560.00 USD | 23,310.00 USD | 8,460.00 USD | 9,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1021` | 34,620.00 USD | 34,620.00 USD | 0.00 USD | 0.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1021` | 58,810.00 USD | 58,810.00 USD | 14,070.00 USD | 3,270.00 USD | 37,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1023` | 20,730.00 USD | 20,730.00 USD | 0.00 USD | 8,270.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1023` | 4,030.00 USD | 4,030.00 USD | 4,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1027` | 8,740.00 USD | 8,740.00 USD | 0.00 USD | 0.00 USD | 8,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1029` | 21,750.00 USD | 21,750.00 USD | 6,870.00 USD | 7,400.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1029` | 23,700.00 USD | 23,700.00 USD | 0.00 USD | 0.00 USD | 23,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1029` | 47,390.00 USD | 47,390.00 USD | 0.00 USD | 0.00 USD | 23,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1031` | 84,970.00 USD | 84,970.00 USD | 33,590.00 USD | 5,770.00 USD | 23,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1031` | 66,160.00 USD | 66,160.00 USD | 13,690.00 USD | 5,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1033` | 124,260.00 USD | 124,260.00 USD | 2,890.00 USD | 10,740.00 USD | 25,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1033` | 90,130.00 USD | 90,130.00 USD | 13,180.00 USD | 10,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1035` | 150,560.00 USD | 150,560.00 USD | 15,150.00 USD | 11,130.00 USD | 17.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1035` | 108,090.00 USD | 108,090.00 USD | 8,450.00 USD | 9,400.00 USD | 108.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1037` | 203,190.00 USD | 203,190.00 USD | 36,550.00 USD | 14,230.00 USD | 1,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1037` | 113,790.00 USD | 113,790.00 USD | 0.00 USD | 5,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1039` | 225,040.00 USD | 225,040.00 USD | 6,500.00 USD | 10,140.00 USD | 5,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1039` | 152,540.00 USD | 152,540.00 USD | 0.00 USD | 7,400.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1041` | 278,630.00 USD | 278,630.00 USD | 14,180.00 USD | 19,780.00 USD | 19,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1041` | 161,390.00 USD | 161,390.00 USD | 5,940.00 USD | 2,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1043` | 318,660.00 USD | 318,660.00 USD | 5,900.00 USD | 9,960.00 USD | 24,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1043` | 206,030.00 USD | 206,030.00 USD | 15,960.00 USD | 5,980.00 USD | 22,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1045` | 347,220.00 USD | 347,220.00 USD | 6,520.00 USD | 9,480.00 USD | 12,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1045` | 225,680.00 USD | 225,680.00 USD | 0.00 USD | 19,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1047` | 446,430.00 USD | 446,430.00 USD | 36,690.00 USD | 16,420.00 USD | 46,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1047` | 314,770.00 USD | 314,770.00 USD | 10,630.00 USD | 10,770.00 USD | 67,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1049` | 568,260.00 USD | 568,260.00 USD | 41,000.00 USD | 15,310.00 USD | 65,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1049` | 430,010.00 USD | 430,010.00 USD | 34,790.00 USD | 4,810.00 USD | 75,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1051` | 629,020.00 USD | 629,020.00 USD | 27,580.00 USD | 10,280.00 USD | 22,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1051` | 506,750.00 USD | 506,750.00 USD | 17,290.00 USD | 11,500.00 USD | 47,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1053` | 727,900.00 USD | 727,900.00 USD | 33,460.00 USD | 11,480.00 USD | 53,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1053` | 685,790.00 USD | 685,790.00 USD | 53,590.00 USD | 29,800.00 USD | 95,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1055` | 860,930.00 USD | 860,930.00 USD | 51,530.00 USD | 25,230.00 USD | 56,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1055` | 986,760.00 USD | 986,760.00 USD | 80,160.00 USD | 27,290.00 USD | 193,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1057` | 916,010.00 USD | 916,010.00 USD | 14,080.00 USD | 11,900.00 USD | 29,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1057` | 1,200,000.00 USD | 1,200,000.00 USD | 50,380.00 USD | 47,740.00 USD | 110,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1059` | 1,030,000.00 USD | 1,030,000.00 USD | 31,860.00 USD | 5,730.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1059` | 1,470,000.00 USD | 1,470,000.00 USD | 92,510.00 USD | 51,220.00 USD | 133,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1061` | 1,120,000.00 USD | 1,120,000.00 USD | 27,260.00 USD | 4,160.00 USD | 58,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1061` | 1,610,000.00 USD | 1,610,000.00 USD | 35,960.00 USD | 27,410.00 USD | 76,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1063` | 1,210,000.00 USD | 1,210,000.00 USD | 25,200.00 USD | 2,030.00 USD | 65,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1063` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 38,330.00 USD | 149,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1065` | 1,250,000.00 USD | 1,250,000.00 USD | 7,010.00 USD | 6,250.00 USD | 28,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1065` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 21,040.00 USD | 99,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1067` | 1,320,000.00 USD | 1,320,000.00 USD | 12,290.00 USD | 5,530.00 USD | 48,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1067` | 2,060,000.00 USD | 2,060,000.00 USD | 5,310.00 USD | 53,210.00 USD | 83,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1069` | 1,400,000.00 USD | 1,400,000.00 USD | 18,540.00 USD | 5,440.00 USD | 62,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1069` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 31,620.00 USD | 92,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1071` | 1,430,000.00 USD | 1,430,000.00 USD | 2,550.00 USD | 5,850.00 USD | 20,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1071` | 2,280,000.00 USD | 2,280,000.00 USD | 7,820.00 USD | 28,880.00 USD | 52,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1073` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1073` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 17,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1075` | 1,440,000.00 USD | 1,440,000.00 USD | 1,440.00 USD | 857.82 USD | 3,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1075` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 22,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1077` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 619.42 USD | 133.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1077` | 2,320,000.00 USD | 2,320,000.00 USD | 5,620.00 USD | 0.00 USD | 256.74 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1079` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 4,300.00 USD | 21,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1079` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 3,380.00 USD | 9,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1081` | 1,480,000.00 USD | 1,480,000.00 USD | 4,650.00 USD | 732.74 USD | 2,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1081` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 89.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1083` | 1,500,000.00 USD | 1,500,000.00 USD | 9,160.00 USD | 6,710.00 USD | 10,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1083` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 64.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1085` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 385.06 USD | 65,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1085` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1087` | 1,650,000.00 USD | 1,650,000.00 USD | 28,490.00 USD | 2,510.00 USD | 44,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1087` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1089` | 1,680,000.00 USD | 1,680,000.00 USD | 29,650.00 USD | 1,580.00 USD | 3,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1089` | 2,350,000.00 USD | 2,350,000.00 USD | 5,290.00 USD | 1,420.00 USD | 113.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1091` | 1,710,000.00 USD | 1,710,000.00 USD | 33,700.00 USD | 0.00 USD | 16.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1091` | 2,380,000.00 USD | 2,380,000.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1093` | 1,730,000.00 USD | 1,730,000.00 USD | 15,480.00 USD | 1,080.00 USD | 269.69 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1093` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 1,500.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1095` | 1,760,000.00 USD | 1,760,000.00 USD | 4,110.00 USD | 1,890.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1095` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 132.97 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1097` | 1,790,000.00 USD | 1,790,000.00 USD | 7,260.00 USD | 2,530.00 USD | 22,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1097` | 2,410,000.00 USD | 2,410,000.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1099` | 1,800,000.00 USD | 1,800,000.00 USD | 6,130.00 USD | 1,940.00 USD | 5.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1099` | 2,440,000.00 USD | 2,440,000.00 USD | 11,470.00 USD | 0.00 USD | 21,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1101` | 1,810,000.00 USD | 1,810,000.00 USD | 5,570.00 USD | 3,820.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1101` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1103` | 1,820,000.00 USD | 1,820,000.00 USD | 3,540.00 USD | 6,900.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 2,480,000.00 USD | 2,480,000.00 USD | 17,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1105` | 1,840,000.00 USD | 1,840,000.00 USD | 3,380.00 USD | 4,740.00 USD | 10,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1105` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 14,480.00 USD | 179.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1107` | 1,890,000.00 USD | 1,890,000.00 USD | 3,110.00 USD | 13,200.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1107` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 12,510.00 USD | 15,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1109` | 1,900,000.00 USD | 1,900,000.00 USD | 2,110.00 USD | 1,370.00 USD | 2,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 12,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1111` | 1,910,000.00 USD | 1,910,000.00 USD | 5,200.00 USD | 996.46 USD | 104.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1111` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1113` | 1,960,000.00 USD | 1,960,000.00 USD | 21,390.00 USD | 5,880.00 USD | 29,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1115` | 1,970,000.00 USD | 1,970,000.00 USD | 6,690.00 USD | 465.26 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1115` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 28.89 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1117` | 2,030,000.00 USD | 2,030,000.00 USD | 2,060.00 USD | 23,600.00 USD | 32,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1117` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 22,780.00 USD | 16,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1119` | 2,100,000.00 USD | 2,100,000.00 USD | 33,110.00 USD | 8,660.00 USD | 32,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1119` | 2,650,000.00 USD | 2,650,000.00 USD | 34,550.00 USD | 7,050.00 USD | 21,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1121` | 2,150,000.00 USD | 2,150,000.00 USD | 21,300.00 USD | 12,810.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 2,680,000.00 USD | 2,680,000.00 USD | 5,730.00 USD | 0.00 USD | 27,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1123` | 2,190,000.00 USD | 2,190,000.00 USD | 28,130.00 USD | 2,870.00 USD | 8,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1123` | 2,760,000.00 USD | 2,760,000.00 USD | 12,360.00 USD | 23,980.00 USD | 37,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1125` | 2,220,000.00 USD | 2,220,000.00 USD | 11,130.00 USD | 12,070.00 USD | 11,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1125` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 2,230.00 USD | 36,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1127` | 2,250,000.00 USD | 2,250,000.00 USD | 928.93 USD | 2,320.00 USD | 21,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1127` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 1,490.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1129` | 2,270,000.00 USD | 2,270,000.00 USD | 11,080.00 USD | 624.95 USD | 5,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1129` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 9,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1131` | 2,320,000.00 USD | 2,320,000.00 USD | 22,340.00 USD | 5,570.00 USD | 22,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1131` | 2,850,000.00 USD | 2,850,000.00 USD | 12,540.00 USD | 0.00 USD | 23,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1133` | 2,360,000.00 USD | 2,360,000.00 USD | 6,530.00 USD | 17,080.00 USD | 23,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 11,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1135` | 2,380,000.00 USD | 2,380,000.00 USD | 4,040.00 USD | 3,670.00 USD | 4,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1135` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1137` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 856.93 USD | 40.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1137` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1141` | 2,900,000.00 USD | 2,900,000.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1143` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 78,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 3,140,000.00 USD | 3,140,000.00 USD | 16,540.00 USD | 2,730.00 USD | 141,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1147` | 3,290,000.00 USD | 3,290,000.00 USD | 9,880.00 USD | 0.00 USD | 138,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1149` | 3,380,000.00 USD | 3,380,000.00 USD | 10,560.00 USD | 0.00 USD | 72,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 3,600,000.00 USD | 3,600,000.00 USD | 92,570.00 USD | 4,210.00 USD | 128,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1153` | 3,900,000.00 USD | 3,900,000.00 USD | 148,820.00 USD | 8,400.00 USD | 146,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1155` | 4,200,000.00 USD | 4,200,000.00 USD | 149,360.00 USD | 40,110.00 USD | 105,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 4,370,000.00 USD | 4,370,000.00 USD | 118,120.00 USD | 3,760.00 USD | 48,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1159` | 4,520,000.00 USD | 4,520,000.00 USD | 81,080.00 USD | 12,710.00 USD | 53,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1161` | 4,790,000.00 USD | 4,790,000.00 USD | 138,620.00 USD | 37,250.00 USD | 99,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 4,930,000.00 USD | 4,930,000.00 USD | 53,510.00 USD | 11,460.00 USD | 68,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1165` | 5,060,000.00 USD | 5,060,000.00 USD | 68,620.00 USD | 35,720.00 USD | 27,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1167` | 5,200,000.00 USD | 5,200,000.00 USD | 79,610.00 USD | 21,620.00 USD | 41,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 5,370,000.00 USD | 5,370,000.00 USD | 65,340.00 USD | 14,840.00 USD | 91,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1171` | 5,480,000.00 USD | 5,480,000.00 USD | 57,350.00 USD | 11,370.00 USD | 35,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1173` | 5,560,000.00 USD | 5,560,000.00 USD | 40,860.00 USD | 9,190.00 USD | 36,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 5,680,000.00 USD | 5,680,000.00 USD | 41,650.00 USD | 12,300.00 USD | 58,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1177` | 5,780,000.00 USD | 5,780,000.00 USD | 33,330.00 USD | 22,040.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1179` | 5,880,000.00 USD | 5,880,000.00 USD | 66,670.00 USD | 10,940.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 5,940,000.00 USD | 5,940,000.00 USD | 22,290.00 USD | 15,780.00 USD | 17,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1183` | 5,990,000.00 USD | 5,990,000.00 USD | 7,760.00 USD | 1,800.00 USD | 39,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1185` | 6,020,000.00 USD | 6,020,000.00 USD | 3,880.00 USD | 5,130.00 USD | 26,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1185` | 4,490.00 USD | 4,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1187` | 6,080,000.00 USD | 6,080,000.00 USD | 5,620.00 USD | 15,370.00 USD | 41,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1189` | 6,130,000.00 USD | 6,130,000.00 USD | 27,240.00 USD | 15,060.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1191` | 6,280,000.00 USD | 6,280,000.00 USD | 22,650.00 USD | 15,330.00 USD | 109,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 6,310,000.00 USD | 6,310,000.00 USD | 21,260.00 USD | 0.00 USD | 12,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1195` | 6,350,000.00 USD | 6,350,000.00 USD | 11,190.00 USD | 1,780.00 USD | 29,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1197` | 6,380,000.00 USD | 6,380,000.00 USD | 6,780.00 USD | 10,800.00 USD | 14,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 6,440,000.00 USD | 6,440,000.00 USD | 2,470.00 USD | 2,390.00 USD | 48,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1201` | 6,590,000.00 USD | 6,590,000.00 USD | 114,140.00 USD | 9,880.00 USD | 29,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1203` | 6,660,000.00 USD | 6,660,000.00 USD | 52,500.00 USD | 13,780.00 USD | 6,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 6,810,000.00 USD | 6,810,000.00 USD | 63,900.00 USD | 39,780.00 USD | 38,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1207` | 6,860,000.00 USD | 6,860,000.00 USD | 12,460.00 USD | 14,560.00 USD | 27,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1209` | 7,020,000.00 USD | 7,020,000.00 USD | 85,160.00 USD | 19,340.00 USD | 59,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 7,080,000.00 USD | 7,080,000.00 USD | 14,350.00 USD | 12,900.00 USD | 29,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1213` | 7,140,000.00 USD | 7,140,000.00 USD | 23,920.00 USD | 12,800.00 USD | 23,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1215` | 7,210,000.00 USD | 7,210,000.00 USD | 5,900.00 USD | 6,620.00 USD | 51,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 721.08 USD | 5,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1315` | 3,540.00 USD | 8,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1405` | 221.12 USD | 8,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1495` | 21,630.00 USD | 30,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1525` | 6,090.00 USD | 36,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1565` | 550.61 USD | 37,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1695` | 169.25 USD | 37,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1745` | 131.08 USD | 37,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1755` | 147.21 USD | 37,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1795` | 100.88 USD | 37,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1825` | 514.28 USD | 38,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1855` | 166.95 USD | 38,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1865` | 199.93 USD | 38,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2035` | 983.66 USD | 39,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0285` | 124,360.00 USD | 0.00 USD | 145.32 USD | `-72.30%` | `5,098.90` |
| `Live` | `Long` | `0.0305` | 124,210.00 USD | 0.00 USD | 1,320.00 USD | `-70.35%` | `43,265.90` |
| `Live` | `Long` | `0.0375` | 122,890.00 USD | 0.00 USD | 225.00 USD | `-63.55%` | `6,000.00` |
| `Live` | `Long` | `0.0395` | 122,670.00 USD | 0.00 USD | 271.86 USD | `-61.60%` | `6,882.60` |
| `Live` | `Long` | `0.0535` | 122,390.00 USD | 0.00 USD | 410.01 USD | `-47.99%` | `7,663.80` |
| `Live` | `Long` | `0.0575` | 121,980.00 USD | 0.00 USD | 4,840.00 USD | `-44.10%` | `84,219.50` |
| `Live` | `Long` | `0.0615` | 117,140.00 USD | 0.00 USD | 1,100.00 USD | `-40.22%` | `17,943.80` |
| `Live` | `Long` | `0.0645` | 116,040.00 USD | 0.00 USD | 353.81 USD | `-37.30%` | `5,485.40` |
| `Live` | `Long` | `0.0655` | 115,680.00 USD | 0.00 USD | 361.16 USD | `-36.33%` | `5,513.90` |
| `Live` | `Long` | `0.0675` | 115,320.00 USD | 0.00 USD | 518.48 USD | `-34.38%` | `7,681.20` |
| `Live` | `Long` | `0.0685` | 114,810.00 USD | 0.00 USD | 1,920.00 USD | `-33.41%` | `28,000.00` |
| `Live` | `Long` | `0.0705` | 112,890.00 USD | 0.00 USD | 1,090.00 USD | `-31.47%` | `15,500.00` |
| `Live` | `Long` | `0.0725` | 111,790.00 USD | 0.00 USD | 64,900.00 USD | `-29.52%` | `895,143.10` |
| `Live` | `Long` | `0.0735` | 46,900.00 USD | 0.00 USD | 2,530.00 USD | `-28.55%` | `34,439.60` |
| `Live` | `Long` | `0.0745` | 44,370.00 USD | 0.00 USD | 2,300.00 USD | `-27.58%` | `30,851.90` |
| `Live` | `Long` | `0.0755` | 42,070.00 USD | 0.00 USD | 12,440.00 USD | `-26.61%` | `164,709.50` |
| `Live` | `Long` | `0.0765` | 29,630.00 USD | 0.00 USD | 1,320.00 USD | `-25.63%` | `17,254.50` |
| `Live` | `Long` | `0.0775` | 28,310.00 USD | 0.00 USD | 878.62 USD | `-24.66%` | `11,337.00` |
| `Live` | `Long` | `0.0785` | 27,430.00 USD | 0.00 USD | 339.50 USD | `-23.69%` | `4,324.80` |
| `Live` | `Long` | `0.0795` | 27,090.00 USD | 0.00 USD | 2,710.00 USD | `-22.72%` | `34,073.20` |
| `Live` | `Long` | `0.0805` | 24,380.00 USD | 0.00 USD | 223.98 USD | `-21.75%` | `2,782.40` |
| `Live` | `Long` | `0.0815` | 24,160.00 USD | 0.00 USD | 1,560.00 USD | `-20.77%` | `19,181.40` |
| `Live` | `Long` | `0.0825` | 22,600.00 USD | 0.00 USD | 140.74 USD | `-19.80%` | `1,705.90` |
| `Live` | `Long` | `0.0845` | 22,460.00 USD | 0.00 USD | 14,300.00 USD | `-17.86%` | `169,238.60` |
| `Live` | `Long` | `0.0855` | 8,160.00 USD | 0.00 USD | 1,710.00 USD | `-16.89%` | `20,000.00` |
| `Live` | `Long` | `0.0865` | 6,450.00 USD | 0.00 USD | 146.06 USD | `-15.91%` | `1,688.60` |
| `Live` | `Long` | `0.0875` | 6,300.00 USD | 0.00 USD | 793.17 USD | `-14.94%` | `9,064.80` |
| `Live` | `Long` | `0.0895` | 5,510.00 USD | 0.00 USD | 3,270.00 USD | `-13.00%` | `36,562.50` |
| `Live` | `Long` | `0.0905` | 2,230.00 USD | 0.00 USD | 2,230.00 USD | `-12.02%` | `24,685.10` |
| `Live` | `Short` | `0.1185` | 4,490.00 USD | 4,490.00 USD | 0.00 USD | `+15.19%` | `37,931.30` |
| `Live` | `Short` | `0.1225` | 5,220.00 USD | 721.08 USD | 0.00 USD | `+19.08%` | `5,886.40` |
| `Live` | `Short` | `0.1315` | 8,750.00 USD | 3,540.00 USD | 0.00 USD | `+27.83%` | `26,889.40` |
| `Live` | `Short` | `0.1405` | 8,970.00 USD | 221.12 USD | 0.00 USD | `+36.58%` | `1,573.80` |
| `Live` | `Short` | `0.1495` | 30,600.00 USD | 21,630.00 USD | 0.00 USD | `+45.33%` | `144,681.60` |
| `Live` | `Short` | `0.1525` | 36,690.00 USD | 6,090.00 USD | 0.00 USD | `+48.25%` | `39,929.50` |
| `Live` | `Short` | `0.1565` | 37,240.00 USD | 550.61 USD | 0.00 USD | `+52.13%` | `3,518.30` |
| `Live` | `Short` | `0.1695` | 37,410.00 USD | 169.25 USD | 0.00 USD | `+64.77%` | `998.50` |
| `Live` | `Short` | `0.1745` | 37,540.00 USD | 131.08 USD | 0.00 USD | `+69.63%` | `751.20` |
| `Live` | `Short` | `0.1755` | 37,690.00 USD | 147.21 USD | 0.00 USD | `+70.60%` | `838.80` |
| `Live` | `Short` | `0.1795` | 37,790.00 USD | 100.88 USD | 0.00 USD | `+74.49%` | `562.00` |
| `Live` | `Short` | `0.1825` | 38,310.00 USD | 514.28 USD | 0.00 USD | `+77.41%` | `2,818.00` |
| `Live` | `Short` | `0.1855` | 38,470.00 USD | 166.95 USD | 0.00 USD | `+80.32%` | `900.00` |
| `Live` | `Short` | `0.1865` | 38,670.00 USD | 199.93 USD | 0.00 USD | `+81.30%` | `1,072.00` |
| `Live` | `Short` | `0.2035` | 39,660.00 USD | 983.66 USD | 0.00 USD | `+97.82%` | `4,833.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0635` | 36,680.00 USD | 0.00 USD | 1,140.00 USD | `-38.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 35,540.00 USD | 0.00 USD | 773.46 USD | `-31.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 34,760.00 USD | 0.00 USD | 592.27 USD | `-30.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 34,170.00 USD | 0.00 USD | 755.00 USD | `-26.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0805` | 33,420.00 USD | 0.00 USD | 411.06 USD | `-21.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0815` | 33,000.00 USD | 0.00 USD | 285.01 USD | `-20.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0835` | 32,720.00 USD | 0.00 USD | 456.70 USD | `-18.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0845` | 32,260.00 USD | 0.00 USD | 171.09 USD | `-17.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 32,090.00 USD | 0.00 USD | 631.58 USD | `-16.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 31,460.00 USD | 0.00 USD | 782.05 USD | `-13.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 30,680.00 USD | 0.00 USD | 444.62 USD | `-12.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0915` | 30,230.00 USD | 0.00 USD | 623.91 USD | `-11.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 29,610.00 USD | 0.00 USD | 485.13 USD | `-8.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0965` | 29,120.00 USD | 0.00 USD | 5,700.00 USD | `-6.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0975` | 23,430.00 USD | 0.00 USD | 720.22 USD | `-5.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0985` | 22,710.00 USD | 0.00 USD | 931.75 USD | `-4.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0995` | 21,770.00 USD | 0.00 USD | 17,910.00 USD | `-3.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 3,860.00 USD | 0.00 USD | 2,180.00 USD | `-2.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1015` | 1,680.00 USD | 0.00 USD | 903.42 USD | `-1.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 780.70 USD | 0.00 USD | 780.70 USD | `-0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1035` | 1,850.00 USD | 1,850.00 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 1,960.00 USD | 105.53 USD | 0.00 USD | `+1.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 9,730.00 USD | 7,770.00 USD | 0.00 USD | `+2.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 119,010.00 USD | 109,280.00 USD | 0.00 USD | `+3.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1075` | 140,910.00 USD | 21,900.00 USD | 0.00 USD | `+4.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 141,070.00 USD | 160.20 USD | 0.00 USD | `+7.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 141,910.00 USD | 839.64 USD | 0.00 USD | `+8.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1125` | 142,700.00 USD | 786.65 USD | 0.00 USD | `+9.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1135` | 142,820.00 USD | 116.27 USD | 0.00 USD | `+10.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 142,960.00 USD | 137.71 USD | 0.00 USD | `+12.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1165` | 143,140.00 USD | 180.81 USD | 0.00 USD | `+13.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1175` | 143,500.00 USD | 363.49 USD | 0.00 USD | `+14.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1185` | 143,770.00 USD | 265.74 USD | 0.00 USD | `+15.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1195` | 158,400.00 USD | 14,640.00 USD | 0.00 USD | `+16.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1225` | 159,380.00 USD | 980.00 USD | 0.00 USD | `+19.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1235` | 166,750.00 USD | 7,370.00 USD | 0.00 USD | `+20.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1255` | 171,120.00 USD | 4,380.00 USD | 0.00 USD | `+22.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1315` | 202,690.00 USD | 31,560.00 USD | 0.00 USD | `+27.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1335` | 204,000.00 USD | 1,310.00 USD | 0.00 USD | `+29.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1345` | 208,150.00 USD | 4,150.00 USD | 0.00 USD | `+30.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1365` | 215,900.00 USD | 7,750.00 USD | 0.00 USD | `+32.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1405` | 229,010.00 USD | 13,110.00 USD | 0.00 USD | `+36.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1425` | 229,110.00 USD | 102.22 USD | 0.00 USD | `+38.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1435` | 236,280.00 USD | 7,180.00 USD | 0.00 USD | `+39.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1485` | 238,930.00 USD | 2,650.00 USD | 0.00 USD | `+44.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1525` | 242,700.00 USD | 3,770.00 USD | 0.00 USD | `+48.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 242,880.00 USD | 184.49 USD | 0.00 USD | `+51.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 245,690.00 USD | 2,810.00 USD | 0.00 USD | `+52.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 245,910.00 USD | 219.81 USD | 0.00 USD | `+53.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 246,190.00 USD | 277.62 USD | 0.00 USD | `+58.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 248,220.00 USD | 2,030.00 USD | 0.00 USD | `+64.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 248,430.00 USD | 216.55 USD | 0.00 USD | `+69.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 248,550.00 USD | 117.26 USD | 0.00 USD | `+91.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 269,080.00 USD | 20,530.00 USD | 0.00 USD | `+94.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 269,270.00 USD | 189.30 USD | 0.00 USD | `+97.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 269,490.00 USD | 219.22 USD | 0.00 USD | `+98.79%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0827` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 4,500.00 USD |
| `7D` | `0.0829` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 28.49 USD |
| `7D` | `0.0859` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0861` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 4,340.00 USD |
| `7D` | `0.0863` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 0.00 USD | 1,880.00 USD | 4,860.00 USD |
| `7D` | `0.0865` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 0.00 USD | 1,980.00 USD | 13,330.00 USD |
| `7D` | `0.0867` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 2,070.00 USD |
| `7D` | `0.0869` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 2,900.00 USD |
| `7D` | `0.0871` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 0.00 USD | 1,200.00 USD | 2,850.00 USD |
| `7D` | `0.0873` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 4,480.00 USD |
| `7D` | `0.0875` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 6,010.00 USD | 0.00 USD | 4,270.00 USD |
| `7D` | `0.0877` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 7,820.00 USD | 6,050.00 USD | 22,770.00 USD |
| `7D` | `0.0879` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 1,370.00 USD | 2,010.00 USD | 13,390.00 USD |
| `7D` | `0.0881` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 9,390.00 USD | 2,270.00 USD | 5,500.00 USD |
| `7D` | `0.0883` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 7,040.00 USD | 6,800.00 USD | 21,710.00 USD |
| `7D` | `0.0885` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 1,000.00 USD | 1,220.00 USD | 2,070.00 USD |
| `1D` | `0.0887` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 7,550.00 USD | 2,580.00 USD | 10,970.00 USD |
| `7D` | `0.0887` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 10,610.00 USD | 2,920.00 USD | 17,560.00 USD |
| `1D` | `0.0889` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 727.20 USD | 1,680.00 USD | 2,110.00 USD |
| `7D` | `0.0889` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 10,710.00 USD | 3,200.00 USD | 13,140.00 USD |
| `1D` | `0.0891` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 755.35 USD | 1,580.00 USD | 3,210.00 USD |
| `7D` | `0.0891` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 6,310.00 USD | 3,960.00 USD | 2,080.00 USD |
| `1D` | `0.0893` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 983.61 USD | 0.00 USD | 542.23 USD |
| `7D` | `0.0893` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 5,230.00 USD | 3,080.00 USD | 5,100.00 USD |
| `1D` | `0.0895` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 0.00 USD | 1,080.00 USD | 0.00 USD |
| `7D` | `0.0895` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 4,480.00 USD | 2,110.00 USD | 5,490.00 USD |
| `1D` | `0.0897` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 0.00 USD | 1,330.00 USD | 11.07 USD |
| `7D` | `0.0897` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 4,670.00 USD | 0.00 USD | 1,390.00 USD |
| `1D` | `0.0899` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 21.52 USD |
| `7D` | `0.0899` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 0.00 USD | 927.82 USD | 4,510.00 USD |
| `1D` | `0.0901` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 3,320.00 USD | 1,000.00 USD | 18.94 USD |
| `7D` | `0.0901` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 1,250.00 USD | 428.11 USD | 17.63 USD |
| `1D` | `0.0903` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 0.00 USD | 3,440.00 USD | 2,230.00 USD |
| `7D` | `0.0903` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 5,330.00 USD | 1,480.00 USD | 2,870.00 USD |
| `1D` | `0.0905` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 0.00 USD | 486.35 USD | 2,150.00 USD |
| `7D` | `0.0905` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 6,050.00 USD | 0.00 USD | 2,610.00 USD |
| `1D` | `0.0907` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 1,250.00 USD | 245.42 USD | 2,710.00 USD |
| `7D` | `0.0907` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 2,780.00 USD | 2,880.00 USD | 2,920.00 USD |
| `1D` | `0.0909` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 938.76 USD | 1,360.00 USD | 786.66 USD |
| `7D` | `0.0909` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 1,180.00 USD | 2,200.00 USD | 83.37 USD |
| `1D` | `0.0911` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 5,580.00 USD | 1,450.00 USD | 58.17 USD |
| `7D` | `0.0911` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD |
| `1D` | `0.0913` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 1,930.00 USD | 465.26 USD | 787.25 USD |
| `7D` | `0.0913` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 74.70 USD |
| `1D` | `0.0915` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 6,590.00 USD | 2,510.00 USD | 76.57 USD |
| `7D` | `0.0915` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 1,670.00 USD | 903.90 USD | 0.00 USD |
| `1D` | `0.0917` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 3,850.00 USD | 3,470.00 USD | 71.54 USD |
| `7D` | `0.0917` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 8,050.00 USD |
| `1D` | `0.0919` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 4,980.00 USD | 1,090.00 USD | 19,100.00 USD |
| `7D` | `0.0919` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 142.43 USD |
| `1D` | `0.0921` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 0.00 USD | 750.63 USD | 3,810.00 USD |
| `7D` | `0.0921` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 80.96 USD |
| `1D` | `0.0923` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 3,300.00 USD | 3,620.00 USD | 25,420.00 USD |
| `7D` | `0.0923` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 0.00 USD | 6,430.00 USD | 43,930.00 USD |
| `1D` | `0.0925` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 4,780.00 USD | 3,340.00 USD | 26,400.00 USD |
| `7D` | `0.0925` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD |
| `1D` | `0.0929` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 4,360.00 USD | 1,190.00 USD | 16.60 USD |
| `7D` | `0.0929` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD |
| `1D` | `0.0931` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 7,430.00 USD |
| `7D` | `0.0931` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 12,180.00 USD |
| `1D` | `0.0933` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 16,500.00 USD | 0.00 USD | 10,200.00 USD |
| `7D` | `0.0933` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 108.72 USD |
| `1D` | `0.0935` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 8,990.00 USD | 7,300.00 USD | 15,690.00 USD |
| `7D` | `0.0935` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 19,560.00 USD | 8,160.00 USD | 31,940.00 USD |
| `1D` | `0.0937` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 4,580.00 USD | 6,660.00 USD | 13,310.00 USD |
| `7D` | `0.0937` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 248.29 USD |
| `1D` | `0.0939` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 3,590.00 USD | 2,140.00 USD | 44,370.00 USD |
| `7D` | `0.0939` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 10,650.00 USD |
| `1D` | `0.0941` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 0.00 USD | 9,410.00 USD | 21,110.00 USD |
| `7D` | `0.0941` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 16,100.00 USD | 18,340.00 USD | 79,570.00 USD |
| `1D` | `0.0943` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 3,500.00 USD | 10,920.00 USD | 30,420.00 USD |
| `7D` | `0.0943` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 8,040.00 USD | 0.00 USD | 37,530.00 USD |
| `1D` | `0.0945` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 15,750.00 USD | 6,510.00 USD | 44,380.00 USD |
| `7D` | `0.0945` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 0.00 USD | 3,820.00 USD | 106.10 USD |
| `1D` | `0.0947` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 0.00 USD | 962.66 USD | 91.75 USD |
| `7D` | `0.0947` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 2,200.00 USD | 0.00 USD | 87.80 USD |
| `1D` | `0.0949` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 12,180.00 USD | 5,770.00 USD | 2,940.00 USD |
| `7D` | `0.0949` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 3,770.00 USD | 9,700.00 USD | 26,990.00 USD |
| `1D` | `0.0951` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | 2,030.00 USD | 19,990.00 USD |
| `7D` | `0.0951` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 65.29 USD |
| `1D` | `0.0953` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 33,000.00 USD | 4,360.00 USD | 6,780.00 USD |
| `7D` | `0.0953` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 0.00 USD | 8,150.00 USD | 0.00 USD |
| `1D` | `0.0955` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 17,990.00 USD | 14,600.00 USD | 31,680.00 USD |
| `7D` | `0.0955` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 39,120.00 USD | 13,670.00 USD | 51,090.00 USD |
| `1D` | `0.0957` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 16,340.00 USD | 6,740.00 USD | 48,700.00 USD |
| `7D` | `0.0957` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 132.97 USD |
| `1D` | `0.0959` | 976,670.00 USD | 0.00 USD | 976,670.00 USD | 0.00 USD | 3,100.00 USD | 0.00 USD |
| `7D` | `0.0959` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 28,110.00 USD | 0.00 USD | 21,370.00 USD |
| `1D` | `0.0961` | 973,570.00 USD | 0.00 USD | 973,570.00 USD | 8,920.00 USD | 23,950.00 USD | 23,300.00 USD |
| `7D` | `0.0961` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 12,340.00 USD | 16,920.00 USD | 94,930.00 USD |
| `1D` | `0.0963` | 917,400.00 USD | 0.00 USD | 917,400.00 USD | 23,240.00 USD | 11,750.00 USD | 11,980.00 USD |
| `7D` | `0.0963` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 4,020.00 USD | 205.72 USD |
| `1D` | `0.0965` | 870,430.00 USD | 0.00 USD | 870,430.00 USD | 8,250.00 USD | 5,890.00 USD | 20,440.00 USD |
| `7D` | `0.0965` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 2,390.00 USD | 0.00 USD |
| `1D` | `0.0967` | 835,860.00 USD | 0.00 USD | 835,860.00 USD | 0.00 USD | 1,960.00 USD | 818.32 USD |
| `7D` | `0.0967` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 3,770.00 USD | 0.00 USD | 2,920.00 USD |
| `1D` | `0.0969` | 833,080.00 USD | 0.00 USD | 833,080.00 USD | 6,930.00 USD | 7,530.00 USD | 8,080.00 USD |
| `7D` | `0.0969` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 3,720.00 USD | 7,090.00 USD | 61,090.00 USD |
| `1D` | `0.0971` | 810,530.00 USD | 0.00 USD | 810,530.00 USD | 2,840.00 USD | 4,070.00 USD | 10,240.00 USD |
| `1D` | `0.0973` | 793,380.00 USD | 0.00 USD | 793,380.00 USD | 1,440.00 USD | 10,220.00 USD | 1,970.00 USD |
| `7D` | `0.0973` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD |
| `1D` | `0.0975` | 779,740.00 USD | 0.00 USD | 779,740.00 USD | 0.00 USD | 0.00 USD | 56.06 USD |
| `7D` | `0.0975` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 177.38 USD |
| `1D` | `0.0977` | 779,680.00 USD | 0.00 USD | 779,680.00 USD | 0.00 USD | 765.93 USD | 911.50 USD |
| `1D` | `0.0979` | 778,010.00 USD | 0.00 USD | 778,010.00 USD | 1,330.00 USD | 2,280.00 USD | 21,110.00 USD |
| `1D` | `0.0981` | 753,280.00 USD | 0.00 USD | 753,280.00 USD | 3,830.00 USD | 5,020.00 USD | 0.00 USD |
| `1D` | `0.0983` | 744,440.00 USD | 0.00 USD | 744,440.00 USD | 5,270.00 USD | 7,660.00 USD | 3,810.00 USD |
| `7D` | `0.0983` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 3,720.00 USD | 11,350.00 USD |
| `1D` | `0.0985` | 727,700.00 USD | 0.00 USD | 727,700.00 USD | 4,060.00 USD | 4,210.00 USD | 4,440.00 USD |
| `7D` | `0.0985` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 5,310.00 USD | 9,310.00 USD | 0.00 USD |
| `1D` | `0.0987` | 714,990.00 USD | 0.00 USD | 714,990.00 USD | 25,300.00 USD | 3,920.00 USD | 11,800.00 USD |
| `7D` | `0.0987` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 5,390.00 USD | 15,350.00 USD | 0.00 USD |
| `1D` | `0.0989` | 673,970.00 USD | 0.00 USD | 673,970.00 USD | 2,180.00 USD | 1,540.00 USD | 21,720.00 USD |
| `7D` | `0.0989` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 12,260.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0991` | 648,530.00 USD | 0.00 USD | 648,530.00 USD | 69,940.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0991` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 14,350.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0993` | 578,590.00 USD | 0.00 USD | 578,590.00 USD | 22,410.00 USD | 3,020.00 USD | 43,200.00 USD |
| `7D` | `0.0993` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 63,040.00 USD | 0.00 USD | 50,900.00 USD |
| `1D` | `0.0995` | 509,960.00 USD | 0.00 USD | 509,960.00 USD | 16,240.00 USD | 898.20 USD | 49,440.00 USD |
| `7D` | `0.0995` | 952,170.00 USD | 0.00 USD | 952,170.00 USD | 13,090.00 USD | 0.00 USD | 25,130.00 USD |
| `1D` | `0.0997` | 443,390.00 USD | 0.00 USD | 443,390.00 USD | 17,900.00 USD | 7,370.00 USD | 55,500.00 USD |
| `7D` | `0.0997` | 913,950.00 USD | 0.00 USD | 913,950.00 USD | 21,100.00 USD | 11,200.00 USD | 32,880.00 USD |
| `1D` | `0.0999` | 362,620.00 USD | 0.00 USD | 362,620.00 USD | 0.00 USD | 11,820.00 USD | 47,900.00 USD |
| `7D` | `0.0999` | 848,760.00 USD | 0.00 USD | 848,760.00 USD | 42,340.00 USD | 11,480.00 USD | 104,630.00 USD |
| `1D` | `0.1001` | 302,900.00 USD | 0.00 USD | 302,900.00 USD | 2,670.00 USD | 2,920.00 USD | 42,510.00 USD |
| `7D` | `0.1001` | 690,310.00 USD | 0.00 USD | 690,310.00 USD | 41,570.00 USD | 19,930.00 USD | 105,740.00 USD |
| `1D` | `0.1003` | 254,810.00 USD | 0.00 USD | 254,810.00 USD | 29,140.00 USD | 0.00 USD | 27,200.00 USD |
| `7D` | `0.1003` | 523,080.00 USD | 0.00 USD | 523,080.00 USD | 8,010.00 USD | 0.00 USD | 27,910.00 USD |
| `1D` | `0.1005` | 198,470.00 USD | 0.00 USD | 198,470.00 USD | 21,010.00 USD | 21,540.00 USD | 36,880.00 USD |
| `7D` | `0.1005` | 487,170.00 USD | 0.00 USD | 487,170.00 USD | 35,700.00 USD | 16,500.00 USD | 63,710.00 USD |
| `1D` | `0.1007` | 119,040.00 USD | 0.00 USD | 119,040.00 USD | 11,910.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1007` | 371,270.00 USD | 0.00 USD | 371,270.00 USD | 10,260.00 USD | 3,080.00 USD | 54,750.00 USD |
| `1D` | `0.1009` | 107,130.00 USD | 0.00 USD | 107,130.00 USD | 6,930.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1009` | 303,170.00 USD | 0.00 USD | 303,170.00 USD | 15,320.00 USD | 10,160.00 USD | 54,030.00 USD |
| `1D` | `0.1011` | 100,200.00 USD | 0.00 USD | 100,200.00 USD | 0.00 USD | 4,070.00 USD | 15,740.00 USD |
| `7D` | `0.1011` | 223,670.00 USD | 0.00 USD | 223,670.00 USD | 4,430.00 USD | 4,720.00 USD | 0.00 USD |
| `1D` | `0.1013` | 80,400.00 USD | 0.00 USD | 80,400.00 USD | 0.00 USD | 0.00 USD | 10,500.00 USD |
| `7D` | `0.1013` | 214,530.00 USD | 0.00 USD | 214,530.00 USD | 32,420.00 USD | 27,180.00 USD | 25,450.00 USD |
| `1D` | `0.1015` | 69,890.00 USD | 0.00 USD | 69,890.00 USD | 4,580.00 USD | 1,220.00 USD | 13,220.00 USD |
| `7D` | `0.1015` | 129,480.00 USD | 0.00 USD | 129,480.00 USD | 6,830.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1017` | 50,870.00 USD | 0.00 USD | 50,870.00 USD | 3,590.00 USD | 0.00 USD | 11,110.00 USD |
| `7D` | `0.1017` | 122,650.00 USD | 0.00 USD | 122,650.00 USD | 11,450.00 USD | 0.00 USD | 10,630.00 USD |
| `1D` | `0.1019` | 36,170.00 USD | 0.00 USD | 36,170.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD |
| `7D` | `0.1019` | 100,560.00 USD | 0.00 USD | 100,560.00 USD | 23,310.00 USD | 8,460.00 USD | 9,980.00 USD |
| `1D` | `0.1021` | 34,620.00 USD | 0.00 USD | 34,620.00 USD | 0.00 USD | 0.00 USD | 13,880.00 USD |
| `7D` | `0.1021` | 58,810.00 USD | 0.00 USD | 58,810.00 USD | 14,070.00 USD | 3,270.00 USD | 37,440.00 USD |
| `1D` | `0.1023` | 20,730.00 USD | 0.00 USD | 20,730.00 USD | 0.00 USD | 8,270.00 USD | 3,720.00 USD |
| `7D` | `0.1023` | 4,030.00 USD | 0.00 USD | 4,030.00 USD | 4,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1027` | 8,740.00 USD | 0.00 USD | 8,740.00 USD | 0.00 USD | 0.00 USD | 8,740.00 USD |
| `1D` | `0.1028` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1029` | 21,750.00 USD | 21,750.00 USD | 0.00 USD | 6,870.00 USD | 7,400.00 USD | 7,480.00 USD |
| `7D` | `0.1029` | 23,700.00 USD | 23,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23,700.00 USD |
| `7D` | `0.1029` | 47,390.00 USD | 47,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23,700.00 USD |
| `1D` | `0.1031` | 84,970.00 USD | 84,970.00 USD | 0.00 USD | 33,590.00 USD | 5,770.00 USD | 23,860.00 USD |
| `7D` | `0.1031` | 66,160.00 USD | 66,160.00 USD | 0.00 USD | 13,690.00 USD | 5,070.00 USD | 0.00 USD |
| `1D` | `0.1033` | 124,260.00 USD | 124,260.00 USD | 0.00 USD | 2,890.00 USD | 10,740.00 USD | 25,670.00 USD |
| `7D` | `0.1033` | 90,130.00 USD | 90,130.00 USD | 0.00 USD | 13,180.00 USD | 10,790.00 USD | 0.00 USD |
| `1D` | `0.1035` | 150,560.00 USD | 150,560.00 USD | 0.00 USD | 15,150.00 USD | 11,130.00 USD | 17.34 USD |
| `7D` | `0.1035` | 108,090.00 USD | 108,090.00 USD | 0.00 USD | 8,450.00 USD | 9,400.00 USD | 108.00 USD |
| `1D` | `0.1037` | 203,190.00 USD | 203,190.00 USD | 0.00 USD | 36,550.00 USD | 14,230.00 USD | 1,850.00 USD |
| `7D` | `0.1037` | 113,790.00 USD | 113,790.00 USD | 0.00 USD | 0.00 USD | 5,700.00 USD | 0.00 USD |
| `1D` | `0.1039` | 225,040.00 USD | 225,040.00 USD | 0.00 USD | 6,500.00 USD | 10,140.00 USD | 5,220.00 USD |
| `7D` | `0.1039` | 152,540.00 USD | 152,540.00 USD | 0.00 USD | 0.00 USD | 7,400.00 USD | 31,350.00 USD |
| `1D` | `0.1041` | 278,630.00 USD | 278,630.00 USD | 0.00 USD | 14,180.00 USD | 19,780.00 USD | 19,630.00 USD |
| `7D` | `0.1041` | 161,390.00 USD | 161,390.00 USD | 0.00 USD | 5,940.00 USD | 2,910.00 USD | 0.00 USD |
| `1D` | `0.1043` | 318,660.00 USD | 318,660.00 USD | 0.00 USD | 5,900.00 USD | 9,960.00 USD | 24,170.00 USD |
| `7D` | `0.1043` | 206,030.00 USD | 206,030.00 USD | 0.00 USD | 15,960.00 USD | 5,980.00 USD | 22,700.00 USD |
| `1D` | `0.1045` | 347,220.00 USD | 347,220.00 USD | 0.00 USD | 6,520.00 USD | 9,480.00 USD | 12,560.00 USD |
| `7D` | `0.1045` | 225,680.00 USD | 225,680.00 USD | 0.00 USD | 0.00 USD | 19,650.00 USD | 0.00 USD |
| `1D` | `0.1047` | 446,430.00 USD | 446,430.00 USD | 0.00 USD | 36,690.00 USD | 16,420.00 USD | 46,100.00 USD |
| `7D` | `0.1047` | 314,770.00 USD | 314,770.00 USD | 0.00 USD | 10,630.00 USD | 10,770.00 USD | 67,690.00 USD |
| `1D` | `0.1049` | 568,260.00 USD | 568,260.00 USD | 0.00 USD | 41,000.00 USD | 15,310.00 USD | 65,520.00 USD |
| `7D` | `0.1049` | 430,010.00 USD | 430,010.00 USD | 0.00 USD | 34,790.00 USD | 4,810.00 USD | 75,640.00 USD |
| `1D` | `0.1051` | 629,020.00 USD | 629,020.00 USD | 0.00 USD | 27,580.00 USD | 10,280.00 USD | 22,900.00 USD |
| `7D` | `0.1051` | 506,750.00 USD | 506,750.00 USD | 0.00 USD | 17,290.00 USD | 11,500.00 USD | 47,950.00 USD |
| `1D` | `0.1053` | 727,900.00 USD | 727,900.00 USD | 0.00 USD | 33,460.00 USD | 11,480.00 USD | 53,930.00 USD |
| `7D` | `0.1053` | 685,790.00 USD | 685,790.00 USD | 0.00 USD | 53,590.00 USD | 29,800.00 USD | 95,640.00 USD |
| `1D` | `0.1055` | 860,930.00 USD | 860,930.00 USD | 0.00 USD | 51,530.00 USD | 25,230.00 USD | 56,270.00 USD |
| `7D` | `0.1055` | 986,760.00 USD | 986,760.00 USD | 0.00 USD | 80,160.00 USD | 27,290.00 USD | 193,520.00 USD |
| `1D` | `0.1057` | 916,010.00 USD | 916,010.00 USD | 0.00 USD | 14,080.00 USD | 11,900.00 USD | 29,110.00 USD |
| `7D` | `0.1057` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 50,380.00 USD | 47,740.00 USD | 110,850.00 USD |
| `1D` | `0.1059` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 31,860.00 USD | 5,730.00 USD | 72,520.00 USD |
| `7D` | `0.1059` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 92,510.00 USD | 51,220.00 USD | 133,580.00 USD |
| `1D` | `0.1061` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 27,260.00 USD | 4,160.00 USD | 58,410.00 USD |
| `7D` | `0.1061` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 35,960.00 USD | 27,410.00 USD | 76,420.00 USD |
| `1D` | `0.1063` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 25,200.00 USD | 2,030.00 USD | 65,380.00 USD |
| `7D` | `0.1063` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 38,330.00 USD | 149,670.00 USD |
| `1D` | `0.1065` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 7,010.00 USD | 6,250.00 USD | 28,490.00 USD |
| `7D` | `0.1065` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 21,040.00 USD | 99,840.00 USD |
| `1D` | `0.1067` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 12,290.00 USD | 5,530.00 USD | 48,650.00 USD |
| `7D` | `0.1067` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 5,310.00 USD | 53,210.00 USD | 83,420.00 USD |
| `1D` | `0.1069` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 18,540.00 USD | 5,440.00 USD | 62,860.00 USD |
| `7D` | `0.1069` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD | 92,260.00 USD |
| `1D` | `0.1071` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 2,550.00 USD | 5,850.00 USD | 20,430.00 USD |
| `7D` | `0.1071` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 7,820.00 USD | 28,880.00 USD | 52,820.00 USD |
| `1D` | `0.1073` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,200.00 USD |
| `7D` | `0.1073` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 17,700.00 USD | 0.00 USD |
| `1D` | `0.1075` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 1,440.00 USD | 857.82 USD | 3,840.00 USD |
| `7D` | `0.1075` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,500.00 USD |
| `1D` | `0.1077` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 619.42 USD | 133.34 USD |
| `7D` | `0.1077` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 5,620.00 USD | 0.00 USD | 256.74 USD |
| `1D` | `0.1079` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 4,300.00 USD | 21,870.00 USD |
| `7D` | `0.1079` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 3,380.00 USD | 9,930.00 USD |
| `1D` | `0.1081` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 4,650.00 USD | 732.74 USD | 2,420.00 USD |
| `7D` | `0.1081` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 89.24 USD |
| `1D` | `0.1083` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 9,160.00 USD | 6,710.00 USD | 10,770.00 USD |
| `7D` | `0.1083` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 64.98 USD |
| `1D` | `0.1085` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 385.06 USD | 65,050.00 USD |
| `7D` | `0.1085` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1087` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 28,490.00 USD | 2,510.00 USD | 44,700.00 USD |
| `7D` | `0.1087` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,540.00 USD |
| `1D` | `0.1089` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 29,650.00 USD | 1,580.00 USD | 3,310.00 USD |
| `7D` | `0.1089` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 5,290.00 USD | 1,420.00 USD | 113.96 USD |
| `1D` | `0.1091` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 33,700.00 USD | 0.00 USD | 16.51 USD |
| `7D` | `0.1091` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD |
| `1D` | `0.1093` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 15,480.00 USD | 1,080.00 USD | 269.69 USD |
| `7D` | `0.1093` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 1,500.00 USD | 8,730.00 USD |
| `1D` | `0.1095` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 21,560.00 USD |
| `7D` | `0.1095` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 132.97 USD |
| `1D` | `0.1097` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 7,260.00 USD | 2,530.00 USD | 22,800.00 USD |
| `7D` | `0.1097` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1099` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 6,130.00 USD | 1,940.00 USD | 5.91 USD |
| `7D` | `0.1099` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 21,880.00 USD |
| `1D` | `0.1101` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 5,570.00 USD | 3,820.00 USD | 4,290.00 USD |
| `7D` | `0.1101` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1103` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 3,540.00 USD | 6,900.00 USD | 1,160.00 USD |
| `7D` | `0.1103` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 17,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1105` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 3,380.00 USD | 4,740.00 USD | 10,710.00 USD |
| `7D` | `0.1105` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 14,480.00 USD | 179.00 USD |
| `1D` | `0.1107` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 3,110.00 USD | 13,200.00 USD | 35,750.00 USD |
| `7D` | `0.1107` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 12,510.00 USD | 15,950.00 USD |
| `1D` | `0.1109` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 2,110.00 USD | 1,370.00 USD | 2,670.00 USD |
| `7D` | `0.1109` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 12,430.00 USD | 0.00 USD |
| `1D` | `0.1111` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 5,200.00 USD | 996.46 USD | 104.00 USD |
| `7D` | `0.1111` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD |
| `1D` | `0.1113` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 21,390.00 USD | 5,880.00 USD | 29,990.00 USD |
| `1D` | `0.1115` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 6,690.00 USD | 465.26 USD | 0.00 USD |
| `7D` | `0.1115` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28.89 USD |
| `1D` | `0.1117` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 2,060.00 USD | 23,600.00 USD | 32,100.00 USD |
| `7D` | `0.1117` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | 16,490.00 USD |
| `1D` | `0.1119` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 33,110.00 USD | 8,660.00 USD | 32,490.00 USD |
| `7D` | `0.1119` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 34,550.00 USD | 7,050.00 USD | 21,720.00 USD |
| `1D` | `0.1121` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 21,300.00 USD | 12,810.00 USD | 12,350.00 USD |
| `7D` | `0.1121` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 5,730.00 USD | 0.00 USD | 27,490.00 USD |
| `1D` | `0.1123` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 28,130.00 USD | 2,870.00 USD | 8,450.00 USD |
| `7D` | `0.1123` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 12,360.00 USD | 23,980.00 USD | 37,780.00 USD |
| `1D` | `0.1125` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 11,130.00 USD | 12,070.00 USD | 11,760.00 USD |
| `7D` | `0.1125` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 2,230.00 USD | 36,160.00 USD |
| `1D` | `0.1127` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 928.93 USD | 2,320.00 USD | 21,050.00 USD |
| `7D` | `0.1127` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 1,490.00 USD | 7,980.00 USD |
| `1D` | `0.1129` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 11,080.00 USD | 624.95 USD | 5,010.00 USD |
| `7D` | `0.1129` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,320.00 USD |
| `1D` | `0.1131` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 22,340.00 USD | 5,570.00 USD | 22,790.00 USD |
| `7D` | `0.1131` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 12,540.00 USD | 0.00 USD | 23,190.00 USD |
| `1D` | `0.1133` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 6,530.00 USD | 17,080.00 USD | 23,470.00 USD |
| `7D` | `0.1133` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 11,430.00 USD | 0.00 USD |
| `1D` | `0.1135` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 4,040.00 USD | 3,670.00 USD | 4,090.00 USD |
| `7D` | `0.1135` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD |
| `1D` | `0.1137` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 856.93 USD | 40.44 USD |
| `7D` | `0.1137` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD |
| `7D` | `0.1141` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD |
| `7D` | `0.1143` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78,600.00 USD |
| `7D` | `0.1145` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 16,540.00 USD | 2,730.00 USD | 141,160.00 USD |
| `7D` | `0.1147` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 138,160.00 USD |
| `7D` | `0.1149` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 10,560.00 USD | 0.00 USD | 72,860.00 USD |
| `7D` | `0.1151` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 92,570.00 USD | 4,210.00 USD | 128,550.00 USD |
| `7D` | `0.1153` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 148,820.00 USD | 8,400.00 USD | 146,460.00 USD |
| `7D` | `0.1155` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 149,360.00 USD | 40,110.00 USD | 105,680.00 USD |
| `7D` | `0.1157` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 118,120.00 USD | 3,760.00 USD | 48,220.00 USD |
| `7D` | `0.1159` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 81,080.00 USD | 12,710.00 USD | 53,290.00 USD |
| `7D` | `0.1161` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 138,620.00 USD | 37,250.00 USD | 99,980.00 USD |
| `7D` | `0.1163` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 53,510.00 USD | 11,460.00 USD | 68,760.00 USD |
| `7D` | `0.1165` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 68,620.00 USD | 35,720.00 USD | 27,180.00 USD |
| `7D` | `0.1167` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 79,610.00 USD | 21,620.00 USD | 41,250.00 USD |
| `7D` | `0.1169` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 65,340.00 USD | 14,840.00 USD | 91,820.00 USD |
| `7D` | `0.1171` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 57,350.00 USD | 11,370.00 USD | 35,080.00 USD |
| `7D` | `0.1173` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 40,860.00 USD | 9,190.00 USD | 36,700.00 USD |
| `7D` | `0.1175` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 41,650.00 USD | 12,300.00 USD | 58,660.00 USD |
| `7D` | `0.1177` | 5,780,000.00 USD | 5,780,000.00 USD | 0.00 USD | 33,330.00 USD | 22,040.00 USD | 49,310.00 USD |
| `7D` | `0.1179` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 66,670.00 USD | 10,940.00 USD | 23,430.00 USD |
| `7D` | `0.1181` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 22,290.00 USD | 15,780.00 USD | 17,730.00 USD |
| `7D` | `0.1183` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 7,760.00 USD | 1,800.00 USD | 39,650.00 USD |
| `7D` | `0.1185` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 3,880.00 USD | 5,130.00 USD | 26,650.00 USD |
| `7D` | `0.1187` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 5,620.00 USD | 15,370.00 USD | 41,470.00 USD |
| `7D` | `0.1189` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 27,240.00 USD | 15,060.00 USD | 3,240.00 USD |
| `7D` | `0.1191` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 22,650.00 USD | 15,330.00 USD | 109,070.00 USD |
| `7D` | `0.1193` | 6,310,000.00 USD | 6,310,000.00 USD | 0.00 USD | 21,260.00 USD | 0.00 USD | 12,650.00 USD |
| `7D` | `0.1195` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 11,190.00 USD | 1,780.00 USD | 29,550.00 USD |
| `7D` | `0.1197` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 6,780.00 USD | 10,800.00 USD | 14,080.00 USD |
| `7D` | `0.1199` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 2,470.00 USD | 2,390.00 USD | 48,830.00 USD |
| `7D` | `0.1201` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 114,140.00 USD | 9,880.00 USD | 29,030.00 USD |
| `7D` | `0.1203` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 52,500.00 USD | 13,780.00 USD | 6,330.00 USD |
| `7D` | `0.1205` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 63,900.00 USD | 39,780.00 USD | 38,020.00 USD |
| `7D` | `0.1207` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 12,460.00 USD | 14,560.00 USD | 27,010.00 USD |
| `7D` | `0.1209` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 85,160.00 USD | 19,340.00 USD | 59,780.00 USD |
| `7D` | `0.1211` | 7,080,000.00 USD | 7,080,000.00 USD | 0.00 USD | 14,350.00 USD | 12,900.00 USD | 29,490.00 USD |
| `7D` | `0.1213` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 23,920.00 USD | 12,800.00 USD | 23,890.00 USD |
| `7D` | `0.1215` | 7,210,000.00 USD | 7,210,000.00 USD | 0.00 USD | 5,900.00 USD | 6,620.00 USD | 51,930.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `64.02M` | Total OI Tokens: `624,050,952.0 OP`
  * 1h OI Change: `+0.39%` | 4h OI Change: `+4.95%` | 24h OI Change: `-11.81%`
  * Exchange Breakdown: Binance=`13.86M` | Bybit=`12.93M` | OKX=`3.79M` | Hyperliquid=`3.16M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-3.27K` | Last 24h: `-2.42K` | Last 3d: `-6.63K` | Last 7d: `-14.48K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0337%` | **USDT OKX** | `0.0035%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0018%` |
| **USDT MEXC** | `-0.0337%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0079%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `55.23%` | `44.77%` | `1.23` | 4,290,000.00 USD |
| `15M` | `Binance` | `57.05%` | `42.95%` | `1.33` | 1,360,000.00 USD |
| `15M` | `OKX` | `56.24%` | `43.76%` | `1.29` | 240,260.00 USD |
| `15M` | `Bybit` | `66.24%` | `33.76%` | `1.96` | 431,130.00 USD |
| `15M` | `KuCoin` | `59.29%` | `40.71%` | `1.46` | 24,150.00 USD |
| `15M` | `Gate` | `80.57%` | `19.43%` | `4.15` | 233,040.00 USD |
| `15M` | `Bitget` | `37.5%` | `62.5%` | `0.60` | 68,340.00 USD |
| `15M` | `BingX` | `49.69%` | `50.31%` | `0.99` | 713,010.00 USD |
| `15M` | `MEXC` | `52.3%` | `47.7%` | `1.10` | 332,150.00 USD |
| `15M` | `Bitunix` | `42.59%` | `57.41%` | `0.74` | 71,680.00 USD |
| `15M` | `Hyperliquid` | `91.71%` | `8.29%` | `11.06` | 21,480.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.9%` | `53.1%` | `0.88` | 660,420.00 USD |
| `15M` | `Crypto.com` | `49.92%` | `50.08%` | `1.00` | 12.00 USD |
| `15M` | `WhiteBIT` | `41.68%` | `58.32%` | `0.71` | 127,830.00 USD |
| `15M` | `HTX` | `59.48%` | `40.52%` | `1.47` | 2,090.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `39.49%` | `60.51%` | `0.65` | 565.06 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `55.16%` | `44.84%` | `1.23` | 7,870.00 USD |
| `15M` | `Whale Positions` | `57.05%` | `42.95%` | `1.33` | 1,360,000.00 USD |
| `15M` | `Global Accounts` | `55.23%` | `44.77%` | `1.23` | 4,290,000.00 USD |
| `1H` | `OP` | `48.85%` | `51.15%` | `0.96` | 8,950,000.00 USD |
| `1H` | `Binance` | `43.89%` | `56.11%` | `0.78` | 2,560,000.00 USD |
| `1H` | `OKX` | `53.19%` | `46.81%` | `1.14` | 2,220,000.00 USD |
| `1H` | `Bybit` | `71.16%` | `28.84%` | `2.47` | 1,210,000.00 USD |
| `1H` | `KuCoin` | `51.65%` | `48.35%` | `1.07` | 503,340.00 USD |
| `1H` | `Gate` | `58.73%` | `41.27%` | `1.42` | 161,710.00 USD |
| `1H` | `Bitget` | `59.13%` | `40.87%` | `1.45` | 93,300.00 USD |
| `1H` | `BingX` | `15.22%` | `84.78%` | `0.18` | 411,500.00 USD |
| `1H` | `MEXC` | `41.36%` | `58.64%` | `0.71` | 275,710.00 USD |
| `1H` | `Bitunix` | `67.28%` | `32.72%` | `2.06` | 198,050.00 USD |
| `1H` | `Hyperliquid` | `54.94%` | `45.06%` | `1.22` | 16,490.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.09%` | `52.91%` | `0.89` | 954,640.00 USD |
| `1H` | `Crypto.com` | `82.62%` | `17.38%` | `4.75` | 65.31 USD |
| `1H` | `WhiteBIT` | `5.85%` | `94.15%` | `0.06` | 331,180.00 USD |
| `1H` | `HTX` | `57.43%` | `42.57%` | `1.35` | 5,900.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `38.62%` | `61.38%` | `0.63` | 484.72 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `98.32%` | `1.68%` | `58.52` | 101.60 USD |
| `1H` | `Whale Positions` | `43.89%` | `56.11%` | `0.78` | 2,560,000.00 USD |
| `1H` | `Global Accounts` | `48.85%` | `51.15%` | `0.96` | 8,950,000.00 USD |
| `4H` | `OP` | `50.15%` | `49.85%` | `1.01` | 34,400,000.00 USD |
| `4H` | `Binance` | `48.43%` | `51.57%` | `0.94` | 12,880,000.00 USD |
| `4H` | `OKX` | `48.6%` | `51.4%` | `0.95` | 4,340,000.00 USD |
| `4H` | `Bybit` | `56.59%` | `43.41%` | `1.30` | 3,570,000.00 USD |
| `4H` | `KuCoin` | `49.35%` | `50.65%` | `0.97` | 2,350,000.00 USD |
| `4H` | `Gate` | `44.75%` | `55.25%` | `0.81` | 1,500,000.00 USD |
| `4H` | `Bitget` | `47.73%` | `52.27%` | `0.91` | 948,280.00 USD |
| `4H` | `BingX` | `37.71%` | `62.29%` | `0.61` | 2,120,000.00 USD |
| `4H` | `MEXC` | `49.52%` | `50.48%` | `0.98` | 1,510,000.00 USD |
| `4H` | `Bitunix` | `47.81%` | `52.19%` | `0.92` | 791,060.00 USD |
| `4H` | `Hyperliquid` | `61.16%` | `38.84%` | `1.57` | 687,540.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.5%` | `50.5%` | `0.98` | 2,690,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `95.52%` | `4.48%` | `21.32` | 937,610.00 USD |
| `4H` | `HTX` | `35.69%` | `64.31%` | `0.55` | 12,180.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `97.62%` | `2.38%` | `41.02` | 18,280.00 USD |
| `4H` | `Aster` | `13.4%` | `86.6%` | `0.15` | 48,600.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `48.43%` | `51.57%` | `0.94` | 12,880,000.00 USD |
| `4H` | `Global Accounts` | `50.15%` | `49.85%` | `1.01` | 34,400,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0992` | `0.0992` | `0.0992` | `0.0995` | `0.0989` | 394,380.07 USD | 199,715.01 USD | 194,665.06 USD | 5,049.95 USD | `+1.28%` | `10B / 6S` |
| `0:00 UTC` | `0.0989` | `0.0992` | `0.0989` | `0.0999` | `0.0988` | 347,230.40 USD | 177,310.87 USD | 169,919.53 USD | 7,391.34 USD | `+2.13%` | `21B / 7S` |
| `5:00 UTC` | `0.1001` | `0.1001` | `0.1001` | `0.1004` | `0.0996` | 360,867.60 USD | 243,343.04 USD | 117,524.56 USD | 125,818.48 USD | `+34.87%` | `30B / 1S` |
| `0:00 UTC` | `0.1005` | `0.1006` | `0.1005` | `0.1009` | `0.1002` | 321,574.58 USD | 208,787.55 USD | 112,787.03 USD | 96,000.52 USD | `+29.85%` | `23B / 4S` |
| `5:00 UTC` | `0.1009` | `0.1011` | `0.1009` | `0.1014` | `0.1006` | 597,276.02 USD | 343,393.62 USD | 253,882.40 USD | 89,511.23 USD | `+14.99%` | `17B / 7S` |
| `0:00 UTC` | `0.1017` | `0.1020` | `0.1017` | `0.1027` | `0.1012` | 617,993.11 USD | 329,792.38 USD | 288,200.73 USD | 41,591.66 USD | `+6.73%` | `38B / 17S` |
| `5:00 UTC` | `0.1023` | `0.1024` | `0.1023` | `0.1028` | `0.1021` | 423,419.23 USD | 254,886.37 USD | 168,532.86 USD | 86,353.50 USD | `+20.39%` | `21B / 4S` |
| `0:00 UTC` | `0.1026` | `0.1025` | `0.1026` | `0.1029` | `0.1022` | 371,349.35 USD | 197,401.99 USD | 173,947.36 USD | 23,454.63 USD | `+6.32%` | `23B / 9S` |
| `5:00 UTC` | `0.1025` | `0.1024` | `0.1025` | `0.1027` | `0.1019` | 375,921.80 USD | 199,382.61 USD | 176,539.19 USD | 22,843.43 USD | `+6.08%` | `14B / 11S` |
| `0:00 UTC` | `0.1029` | `0.1024` | `0.1029` | `0.1031` | `0.1015` | 306,799.31 USD | 179,294.07 USD | 127,505.24 USD | 51,788.83 USD | `+16.88%` | `41B / 15S` |

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
| `5m` | -5,260.00 USD | 42,900.00 USD | **`ACCUMULATION`** |
| `15m` | 2,530.00 USD | 68,640.00 USD | **`ACCUMULATION`** |
| `30m` | -14,950.00 USD | 84,090.00 USD | **`ACCUMULATION`** |
| `1h` | -106,800.00 USD | 239,160.00 USD | **`ACCUMULATION`** |
| `2h` | 110,170.00 USD | 731,800.00 USD | **`ACCUMULATION`** |
| `4h` | -117,070.00 USD | 282,480.00 USD | **`ACCUMULATION`** |
| `6h` | -133,580.00 USD | -1,620,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 165,200.00 USD | -1,310,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -6,680.00 USD | -4,120,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 238,010.00 USD | -3,490,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -194,100.00 USD | -14,260,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,350,000.00 USD | -82,740,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-5.26K` | 15m=`+2.53K` | 1h=`-106.80K` | 24h=`+238.01K`
* Futures Capital Netflows: 5m=`+42.90K` | 15m=`+68.64K` | 1h=`+239.16K` | 24h=`-3.49M`
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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
