# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 11:14:10 IST` (`2026-10-30 05:44:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1023` | `0.1027` | `0.1022` | `0.1024` | `1,141,018` | 116,869.95 USD | 15,473.89 USD | `+13.24%` | -1,823,264.65 USD | `-0.29` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1024` | `0.1027` | `0.1023` | `0.1025` | `1,174,224` | 120,335.20 USD | -23,252.38 USD | `-19.32%` | -1,846,517.04 USD | `-1.74` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.1024` | `0.1029` | `0.1023` | `0.1028` | `819,573` | 84,102.19 USD | 22,860.86 USD | `+27.18%` | -1,823,656.18 USD | `-0.03` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1012` | `0.1027` | `0.1012` | `0.1022` | `6,059,384` | 617,993.11 USD | 41,591.66 USD | `+6.73%` | -1,925,092.05 USD | `+0.38` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1022` | `0.1028` | `0.1021` | `0.1023` | `4,133,987` | 423,419.23 USD | 86,353.50 USD | `+20.39%` | -1,838,738.54 USD | `+0.75` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1023` | `0.1029` | `0.1022` | `0.1029` | `3,103,993` | 318,138.05 USD | 14,122.37 USD | `+4.44%` | -1,824,616.17 USD | `+0.03` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.0981` | `0.0995` | `0.0970` | `0.0993` | `30,519,947` | 2,992,768.64 USD | -441,148.19 USD | `-14.74%` | -2,239,239.62 USD | `-0.72` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.0993` | `0.1013` | `0.0988` | `0.1012` | `16,216,904` | 1,626,948.60 USD | 318,721.56 USD | `+19.59%` | -1,920,518.05 USD | `+0.94` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.1012` | `0.1029` | `0.1012` | `0.1028` | `13,299,437` | 1,359,763.51 USD | 141,878.99 USD | `+10.43%` | -1,778,639.06 USD | `+0.55` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -1,009,359.71 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,347,386.10 USD | `-1.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1029` | `0.0988` | `0.1028` | `29,545,091` | 2,989,668.28 USD | 461,749.09 USD | `+15.44%` | -1,885,637.01 USD | `+1.04` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | 483,978.43 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | 307,838.15 USD | `-1.31` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -1,009,359.71 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,347,386.10 USD | `-1.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1029` | `0.0988` | `0.1028` | `29,545,091` | 2,989,668.28 USD | 461,749.09 USD | `+15.44%` | -1,885,637.01 USD | `+1.04` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:13:49 IST` |

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
| `Live` | `Long Liquidation` | `0.0225` | 114.73 USD | 112,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0305` | 1,320.00 USD | 112,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0345` | 207.00 USD | 111,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 410.01 USD | 111,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 829.69 USD | 110,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 4,080.00 USD | 109,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 1,100.00 USD | 105,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 353.81 USD | 104,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 361.16 USD | 104,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 518.48 USD | 103,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 1,920.00 USD | 103,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 1,090.00 USD | 101,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 64,900.00 USD | 100,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,530.00 USD | 35,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,300.00 USD | 32,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 1,020.00 USD | 30,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 1,320.00 USD | 29,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 878.62 USD | 28,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 339.50 USD | 27,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 2,710.00 USD | 27,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 223.98 USD | 24,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 1,560.00 USD | 24,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 140.74 USD | 22,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0827` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 8,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0830` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 28.49 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0845` | 14,300.00 USD | 22,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 1,710.00 USD | 8,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0860` | 2,180,000.00 USD | 2,180,000.00 USD | 1,880.00 USD | 0.00 USD | 2,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0863` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 1,880.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0865` | 146.06 USD | 6,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0866` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 1,980.00 USD | 15,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0869` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0872` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 1,200.00 USD | 5,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0875` | 2,140,000.00 USD | 2,140,000.00 USD | 6,010.00 USD | 0.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0875` | 793.17 USD | 6,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0878` | 2,130,000.00 USD | 2,130,000.00 USD | 9,200.00 USD | 7,660.00 USD | 28,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0881` | 2,080,000.00 USD | 2,080,000.00 USD | 9,390.00 USD | 2,660.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0884` | 1,650,000.00 USD | 1,650,000.00 USD | 767.42 USD | 1,480.00 USD | 11,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0884` | 2,060,000.00 USD | 2,060,000.00 USD | 7,040.00 USD | 8,030.00 USD | 21,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0886` | 1,630,000.00 USD | 1,630,000.00 USD | 6,600.00 USD | 2,200.00 USD | 10,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0887` | 2,020,000.00 USD | 2,020,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0888` | 1,620,000.00 USD | 1,620,000.00 USD | 1,690.00 USD | 1,080.00 USD | 669.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0890` | 1,610,000.00 USD | 1,610,000.00 USD | 755.35 USD | 1,740.00 USD | 3,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0890` | 1,980,000.00 USD | 1,980,000.00 USD | 14,610.00 USD | 5,880.00 USD | 13,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0892` | 1,610,000.00 USD | 1,610,000.00 USD | 983.61 USD | 813.86 USD | 2,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0893` | 1,950,000.00 USD | 1,950,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0894` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 1,080.00 USD | 554.64 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,270.00 USD | 5,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0896` | 1,930,000.00 USD | 1,930,000.00 USD | 5,760.00 USD | 2,110.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0898` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 1,330.00 USD | 7.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0899` | 1,920,000.00 USD | 1,920,000.00 USD | 3,390.00 USD | 927.82 USD | 4,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0900` | 1,600,000.00 USD | 1,600,000.00 USD | 1,170.00 USD | 494.55 USD | 41.91 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0902` | 1,600,000.00 USD | 1,600,000.00 USD | 2,150.00 USD | 1,420.00 USD | 2.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0902` | 1,910,000.00 USD | 1,910,000.00 USD | 2,270.00 USD | 910.78 USD | 1,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0904` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 2,530.00 USD | 3,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0905` | 1,900,000.00 USD | 1,900,000.00 USD | 10,350.00 USD | 996.61 USD | 4,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0905` | 2,230.00 USD | 2,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0906` | 1,590,000.00 USD | 1,590,000.00 USD | 1,250.00 USD | 486.35 USD | 3,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0908` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 494.75 USD | 1,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0908` | 1,890,000.00 USD | 1,890,000.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0910` | 1,580,000.00 USD | 1,580,000.00 USD | 6,520.00 USD | 1,110.00 USD | 10.67 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0911` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0912` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 1,450.00 USD | 793.84 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0914` | 1,570,000.00 USD | 1,570,000.00 USD | 1,930.00 USD | 1,290.00 USD | 61.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0914` | 1,870,000.00 USD | 1,870,000.00 USD | 1,670.00 USD | 903.90 USD | 74.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0916` | 1,570,000.00 USD | 1,570,000.00 USD | 6,590.00 USD | 1,680.00 USD | 54.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0917` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0918` | 1,560,000.00 USD | 1,560,000.00 USD | 5,140.00 USD | 3,470.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0920` | 1,550,000.00 USD | 1,550,000.00 USD | 3,690.00 USD | 504.78 USD | 20,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0920` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 223.39 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0922` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 1,320.00 USD | 12,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0923` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 6,430.00 USD | 43,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0924` | 1,510,000.00 USD | 1,510,000.00 USD | 1,410.00 USD | 3,060.00 USD | 39,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0926` | 1,470,000.00 USD | 1,470,000.00 USD | 3,270.00 USD | 2,820.00 USD | 39.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0926` | 1,810,000.00 USD | 1,810,000.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0929` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0930` | 1,460,000.00 USD | 1,460,000.00 USD | 4,360.00 USD | 1,190.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0932` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 3,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0932` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 12,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0934` | 1,440,000.00 USD | 1,440,000.00 USD | 20,740.00 USD | 3,830.00 USD | 17,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0935` | 1,790,000.00 USD | 1,790,000.00 USD | 19,560.00 USD | 8,160.00 USD | 31,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0936` | 1,400,000.00 USD | 1,400,000.00 USD | 4,760.00 USD | 9,360.00 USD | 16,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0938` | 1,370,000.00 USD | 1,370,000.00 USD | 8,170.00 USD | 2,920.00 USD | 46,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0938` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 248.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0940` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0941` | 1,730,000.00 USD | 1,730,000.00 USD | 16,100.00 USD | 18,340.00 USD | 90,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0942` | 1,310,000.00 USD | 1,310,000.00 USD | 3,500.00 USD | 16,110.00 USD | 49,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0944` | 1,240,000.00 USD | 1,240,000.00 USD | 11,620.00 USD | 4,860.00 USD | 36,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0944` | 1,600,000.00 USD | 1,600,000.00 USD | 8,040.00 USD | 2,010.00 USD | 37,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0946` | 1,190,000.00 USD | 1,190,000.00 USD | 4,130.00 USD | 5,280.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0947` | 1,550,000.00 USD | 1,550,000.00 USD | 2,200.00 USD | 1,810.00 USD | 177.04 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0948` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 1,100.00 USD | 42.76 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0950` | 1,170,000.00 USD | 1,170,000.00 USD | 12,180.00 USD | 6,710.00 USD | 22,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0950` | 1,550,000.00 USD | 1,550,000.00 USD | 3,770.00 USD | 9,700.00 USD | 27,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0952` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 853.02 USD | 6,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0953` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 8,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0954` | 1,120,000.00 USD | 1,120,000.00 USD | 41,470.00 USD | 11,160.00 USD | 21,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0956` | 1,050,000.00 USD | 1,050,000.00 USD | 18,680.00 USD | 9,390.00 USD | 36,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0956` | 1,500,000.00 USD | 1,500,000.00 USD | 39,120.00 USD | 13,670.00 USD | 51,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0958` | 982,630.00 USD | 982,630.00 USD | 7,180.00 USD | 4,290.00 USD | 22,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0959` | 1,400,000.00 USD | 1,400,000.00 USD | 28,110.00 USD | 0.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0960` | 948,940.00 USD | 948,940.00 USD | 0.00 USD | 16,940.00 USD | 55.21 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0962` | 931,950.00 USD | 931,950.00 USD | 8,920.00 USD | 15,440.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0962` | 1,350,000.00 USD | 1,350,000.00 USD | 12,340.00 USD | 16,920.00 USD | 95,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0964` | 879,860.00 USD | 879,860.00 USD | 31,490.00 USD | 10,380.00 USD | 28,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0965` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 6,410.00 USD | 86.68 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0966` | 809,890.00 USD | 809,890.00 USD | 0.00 USD | 3,880.00 USD | 874.45 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0968` | 805,130.00 USD | 805,130.00 USD | 0.00 USD | 2,960.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0968` | 1,220,000.00 USD | 1,220,000.00 USD | 7,490.00 USD | 0.00 USD | 59,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0970` | 799,870.00 USD | 799,870.00 USD | 8,360.00 USD | 8,640.00 USD | 16,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 7,090.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0972` | 766,540.00 USD | 766,540.00 USD | 2,860.00 USD | 3,220.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0974` | 758,410.00 USD | 758,410.00 USD | 0.00 USD | 7,010.00 USD | 14.85 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0974` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 16,310.00 USD | 104.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0976` | 751,390.00 USD | 751,390.00 USD | 0.00 USD | 765.93 USD | 961.09 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0978` | 749,670.00 USD | 749,670.00 USD | 0.00 USD | 817.22 USD | 45.18 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0980` | 748,800.00 USD | 748,800.00 USD | 0.00 USD | 2,470.00 USD | 21,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0982` | 725,080.00 USD | 725,080.00 USD | 5,470.00 USD | 2,550.00 USD | 5.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 3,720.00 USD | 11,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0984` | 717,060.00 USD | 717,060.00 USD | 1,670.00 USD | 9,040.00 USD | 8,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0986` | 698,110.00 USD | 698,110.00 USD | 0.00 USD | 5,480.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0986` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 14,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0988` | 691,070.00 USD | 691,070.00 USD | 23,710.00 USD | 1,540.00 USD | 31,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 1,090,000.00 USD | 1,090,000.00 USD | 17,640.00 USD | 7,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0990` | 633,980.00 USD | 633,980.00 USD | 4,730.00 USD | 0.00 USD | 5.91 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0992` | 629,240.00 USD | 629,240.00 USD | 76,570.00 USD | 3,020.00 USD | 26,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0992` | 1,070,000.00 USD | 1,070,000.00 USD | 27,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0994` | 522,970.00 USD | 522,970.00 USD | 26,200.00 USD | 0.00 USD | 21,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 1,040,000.00 USD | 1,040,000.00 USD | 63,330.00 USD | 0.00 USD | 76,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0996` | 474,810.00 USD | 474,810.00 USD | 11,810.00 USD | 2,450.00 USD | 71,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0998` | 389,280.00 USD | 389,280.00 USD | 7,180.00 USD | 5,820.00 USD | 59,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0998` | 900,500.00 USD | 900,500.00 USD | 28,450.00 USD | 17,040.00 USD | 135,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1000` | 317,050.00 USD | 317,050.00 USD | 0.00 USD | 11,820.00 USD | 37,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 719,740.00 USD | 719,740.00 USD | 76,560.00 USD | 25,570.00 USD | 107,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1002` | 268,180.00 USD | 268,180.00 USD | 0.00 USD | 0.00 USD | 42,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1004` | 225,260.00 USD | 225,260.00 USD | 34,770.00 USD | 8,690.00 USD | 35,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1004` | 509,630.00 USD | 509,630.00 USD | 22,470.00 USD | 7,440.00 USD | 46,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1006` | 146,340.00 USD | 146,340.00 USD | 3,340.00 USD | 10,340.00 USD | 8,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 433,580.00 USD | 433,580.00 USD | 20,870.00 USD | 7,760.00 USD | 100,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1008` | 123,800.00 USD | 123,800.00 USD | 4,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1010` | 119,440.00 USD | 119,440.00 USD | 6,930.00 USD | 4,070.00 USD | 14,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1010` | 304,720.00 USD | 304,720.00 USD | 17,340.00 USD | 13,670.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1012` | 93,610.00 USD | 93,610.00 USD | 0.00 USD | 0.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 219,680.00 USD | 219,680.00 USD | 34,830.00 USD | 28,370.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1014` | 82,200.00 USD | 82,200.00 USD | 0.00 USD | 449.10 USD | 11,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1016` | 70,660.00 USD | 70,660.00 USD | 8,170.00 USD | 775.38 USD | 13,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1016` | 131,030.00 USD | 131,030.00 USD | 15,440.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1018` | 48,470.00 USD | 48,470.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1019` | 115,590.00 USD | 115,590.00 USD | 26,150.00 USD | 8,460.00 USD | 20,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1020` | 46,930.00 USD | 46,930.00 USD | 3,500.00 USD | 0.00 USD | 11,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1022` | 31,840.00 USD | 31,840.00 USD | 10,130.00 USD | 7,410.00 USD | 5,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1022` | 60,360.00 USD | 60,360.00 USD | 18,100.00 USD | 3,270.00 USD | 37,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1024` | 8,310.00 USD | 8,310.00 USD | 0.00 USD | 8,270.00 USD | 42.48 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1025` | 1,550.00 USD | 1,550.00 USD | 1,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1026` | 13.28 USD | 13.28 USD | 0.00 USD | 0.00 USD | 13.28 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1026` | 26.56 USD | 26.56 USD | 0.00 USD | 0.00 USD | 13.28 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1028` | 20,710.00 USD | 20,710.00 USD | 3,430.00 USD | 3,870.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1028` | 29,300.00 USD | 29,300.00 USD | 3,800.00 USD | 1,810.00 USD | 23,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1030` | 58,940.00 USD | 58,940.00 USD | 9,720.00 USD | 9,300.00 USD | 19,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1031` | 58,670.00 USD | 58,670.00 USD | 19,560.00 USD | 9,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1032` | 120,370.00 USD | 120,370.00 USD | 33,630.00 USD | 7,240.00 USD | 20,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1034` | 155,780.00 USD | 155,780.00 USD | 15,150.00 USD | 7,420.00 USD | 12,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1034` | 92,770.00 USD | 92,770.00 USD | 18,920.00 USD | 15,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1036` | 165,620.00 USD | 165,620.00 USD | 2,150.00 USD | 7,660.00 USD | 28.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1037` | 106,300.00 USD | 106,300.00 USD | 2,710.00 USD | 10,710.00 USD | 108.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1038` | 222,190.00 USD | 222,190.00 USD | 34,400.00 USD | 15,130.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1040` | 269,140.00 USD | 269,140.00 USD | 12,950.00 USD | 18,810.00 USD | 15,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1040` | 153,900.00 USD | 153,900.00 USD | 5,940.00 USD | 10,300.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1042` | 307,340.00 USD | 307,340.00 USD | 5,060.00 USD | 7,360.00 USD | 25,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1043` | 198,550.00 USD | 198,550.00 USD | 15,960.00 USD | 5,980.00 USD | 22,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1044` | 339,440.00 USD | 339,440.00 USD | 5,150.00 USD | 16,420.00 USD | 10,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1046` | 392,670.00 USD | 392,670.00 USD | 10,400.00 USD | 8,320.00 USD | 34,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1046` | 283,030.00 USD | 283,030.00 USD | 0.00 USD | 24,330.00 USD | 60,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1048` | 513,540.00 USD | 513,540.00 USD | 25,030.00 USD | 13,650.00 USD | 82,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1049` | 407,530.00 USD | 407,530.00 USD | 34,790.00 USD | 6,530.00 USD | 83,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1050` | 570,330.00 USD | 570,330.00 USD | 32,820.00 USD | 13,230.00 USD | 10,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1052` | 673,530.00 USD | 673,530.00 USD | 43,930.00 USD | 14,110.00 USD | 45,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1052` | 585,370.00 USD | 585,370.00 USD | 28,200.00 USD | 24,160.00 USD | 125,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1054` | 829,700.00 USD | 829,700.00 USD | 56,700.00 USD | 20,100.00 USD | 79,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1055` | 964,280.00 USD | 964,280.00 USD | 122,840.00 USD | 44,430.00 USD | 211,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1056` | 892,900.00 USD | 892,900.00 USD | 16,600.00 USD | 22,130.00 USD | 24,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1058` | 988,450.00 USD | 988,450.00 USD | 28,780.00 USD | 6,490.00 USD | 60,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1058` | 1,330,000.00 USD | 1,330,000.00 USD | 105,620.00 USD | 58,510.00 USD | 202,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1060` | 1,060,000.00 USD | 1,060,000.00 USD | 31,730.00 USD | 2,700.00 USD | 36,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1061` | 1,590,000.00 USD | 1,590,000.00 USD | 75,540.00 USD | 67,860.00 USD | 118,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1062` | 1,170,000.00 USD | 1,170,000.00 USD | 31,870.00 USD | 2,030.00 USD | 79,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1064` | 1,220,000.00 USD | 1,220,000.00 USD | 1,640.00 USD | 2,630.00 USD | 44,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1064` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 52,580.00 USD | 188,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1066` | 1,280,000.00 USD | 1,280,000.00 USD | 6,940.00 USD | 5,010.00 USD | 41,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1067` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 57,800.00 USD | 144,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1068` | 1,340,000.00 USD | 1,340,000.00 USD | 4,700.00 USD | 4,180.00 USD | 57,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1070` | 1,410,000.00 USD | 1,410,000.00 USD | 16,460.00 USD | 8,600.00 USD | 46,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1070` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 57,770.00 USD | 134,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1072` | 1,420,000.00 USD | 1,420,000.00 USD | 857.22 USD | 1,390.00 USD | 323.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1073` | 2,270,000.00 USD | 2,270,000.00 USD | 7,820.00 USD | 20,440.00 USD | 10,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1074` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1076` | 1,430,000.00 USD | 1,430,000.00 USD | 1,440.00 USD | 857.82 USD | 2,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1076` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 22,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1078` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 3,440.00 USD | 17,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1079` | 2,310,000.00 USD | 2,310,000.00 USD | 5,620.00 USD | 3,380.00 USD | 10,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1080` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 1,480.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1082` | 1,470,000.00 USD | 1,470,000.00 USD | 5,820.00 USD | 7,440.00 USD | 5,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1082` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 154.22 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1084` | 1,520,000.00 USD | 1,520,000.00 USD | 7,990.00 USD | 385.06 USD | 36,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1085` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1086` | 1,600,000.00 USD | 1,600,000.00 USD | 4,220.00 USD | 2,240.00 USD | 72,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1088` | 1,650,000.00 USD | 1,650,000.00 USD | 40,240.00 USD | 1,040.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1088` | 2,330,000.00 USD | 2,330,000.00 USD | 5,290.00 USD | 1,420.00 USD | 9,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1090` | 1,690,000.00 USD | 1,690,000.00 USD | 39,470.00 USD | 813.86 USD | 2,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1091` | 2,350,000.00 USD | 2,350,000.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1092` | 1,700,000.00 USD | 1,700,000.00 USD | 10,290.00 USD | 1,080.00 USD | 53.09 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1094` | 1,730,000.00 USD | 1,730,000.00 USD | 13,100.00 USD | 0.00 USD | 13,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1094` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 1,500.00 USD | 8,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1096` | 1,740,000.00 USD | 1,740,000.00 USD | 4,110.00 USD | 1,890.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1097` | 2,380,000.00 USD | 2,380,000.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1098` | 1,780,000.00 USD | 1,780,000.00 USD | 13,380.00 USD | 4,460.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1100` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 3,310.00 USD | 4,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1100` | 2,410,000.00 USD | 2,410,000.00 USD | 11,470.00 USD | 0.00 USD | 21,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1102` | 1,800,000.00 USD | 1,800,000.00 USD | 5,570.00 USD | 509.08 USD | 96.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 2,450,000.00 USD | 2,450,000.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1104` | 1,820,000.00 USD | 1,820,000.00 USD | 6,920.00 USD | 11,640.00 USD | 1,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1106` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 12,720.00 USD | 30,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1106` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 22,880.00 USD | 16,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1108` | 1,880,000.00 USD | 1,880,000.00 USD | 5,220.00 USD | 1,610.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1110` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 494.75 USD | 916.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1112` | 1,900,000.00 USD | 1,900,000.00 USD | 10,780.00 USD | 747.13 USD | 22.61 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1112` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1114` | 1,950,000.00 USD | 1,950,000.00 USD | 15,810.00 USD | 5,880.00 USD | 29,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1115` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 28.89 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1116` | 1,970,000.00 USD | 1,970,000.00 USD | 6,690.00 USD | 12,550.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1118` | 2,070,000.00 USD | 2,070,000.00 USD | 25,510.00 USD | 17,530.00 USD | 52,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1118` | 2,600,000.00 USD | 2,600,000.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1120` | 2,120,000.00 USD | 2,120,000.00 USD | 27,100.00 USD | 10,220.00 USD | 9,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 2,660,000.00 USD | 2,660,000.00 USD | 17,760.00 USD | 0.00 USD | 38,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1122` | 2,150,000.00 USD | 2,150,000.00 USD | 16,670.00 USD | 5,240.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1124` | 2,190,000.00 USD | 2,190,000.00 USD | 17,090.00 USD | 6,120.00 USD | 9,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1124` | 2,760,000.00 USD | 2,760,000.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1126` | 2,230,000.00 USD | 2,230,000.00 USD | 9,370.00 USD | 10,060.00 USD | 18,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1127` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 3,720.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1128` | 2,250,000.00 USD | 2,250,000.00 USD | 10,120.00 USD | 0.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1130` | 2,280,000.00 USD | 2,280,000.00 USD | 7,970.00 USD | 2,630.00 USD | 16,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1130` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 24,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1132` | 2,320,000.00 USD | 2,320,000.00 USD | 19,390.00 USD | 10,550.00 USD | 16,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 2,840,000.00 USD | 2,840,000.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1134` | 2,350,000.00 USD | 2,350,000.00 USD | 4,040.00 USD | 12,980.00 USD | 13,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1135` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 787.70 USD | 4,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1136` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1139` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1142` | 2,880,000.00 USD | 2,880,000.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 3,120,000.00 USD | 3,120,000.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1148` | 3,300,000.00 USD | 3,300,000.00 USD | 9,880.00 USD | 0.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 3,570,000.00 USD | 3,570,000.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1154` | 4,040,000.00 USD | 4,040,000.00 USD | 243,190.00 USD | 26,970.00 USD | 202,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 4,340,000.00 USD | 4,340,000.00 USD | 173,120.00 USD | 25,290.00 USD | 98,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1160` | 4,610,000.00 USD | 4,610,000.00 USD | 131,160.00 USD | 32,830.00 USD | 109,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 4,900,000.00 USD | 4,900,000.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1166` | 5,120,000.00 USD | 5,120,000.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 5,340,000.00 USD | 5,340,000.00 USD | 82,770.00 USD | 26,150.00 USD | 117,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1172` | 5,470,000.00 USD | 5,470,000.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 5,650,000.00 USD | 5,650,000.00 USD | 75,590.00 USD | 17,930.00 USD | 81,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1178` | 5,820,000.00 USD | 5,820,000.00 USD | 89,510.00 USD | 25,350.00 USD | 60,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 5,910,000.00 USD | 5,910,000.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1184` | 5,970,000.00 USD | 5,970,000.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 6,060,000.00 USD | 6,060,000.00 USD | 5,620.00 USD | 17,120.00 USD | 59,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1190` | 6,200,000.00 USD | 6,200,000.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 6,280,000.00 USD | 6,280,000.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1196` | 6,340,000.00 USD | 6,340,000.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 6,410,000.00 USD | 6,410,000.00 USD | 2,470.00 USD | 13,190.00 USD | 52,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1202` | 6,590,000.00 USD | 6,590,000.00 USD | 131,660.00 USD | 14,930.00 USD | 32,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 6,800,000.00 USD | 6,800,000.00 USD | 117,120.00 USD | 48,510.00 USD | 40,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1205` | 3,590.00 USD | 3,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1208` | 6,900,000.00 USD | 6,900,000.00 USD | 39,480.00 USD | 20,870.00 USD | 39,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 7,070,000.00 USD | 7,070,000.00 USD | 72,500.00 USD | 25,920.00 USD | 76,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1214` | 7,190,000.00 USD | 7,190,000.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 7,240,000.00 USD | 7,240,000.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1220` | 7,340,000.00 USD | 7,340,000.00 USD | 34,050.00 USD | 6,400.00 USD | 54,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 7,460,000.00 USD | 7,460,000.00 USD | 73,610.00 USD | 15,050.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 721.08 USD | 4,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1226` | 7,530,000.00 USD | 7,530,000.00 USD | 42,530.00 USD | 16,510.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 7,650,000.00 USD | 7,650,000.00 USD | 63,930.00 USD | 33,570.00 USD | 28,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1232` | 7,750,000.00 USD | 7,750,000.00 USD | 51,420.00 USD | 12,080.00 USD | 37,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1235` | 7,790,000.00 USD | 7,790,000.00 USD | 15,040.00 USD | 5,390.00 USD | 16,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1236` | 7,800,000.00 USD | 7,800,000.00 USD | 4,080.00 USD | 0.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1385` | 217.97 USD | 4,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1415` | 3,800.00 USD | 8,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1455` | 23,050.00 USD | 31,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1525` | 6,090.00 USD | 37,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1565` | 550.61 USD | 38,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1695` | 169.25 USD | 38,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1745` | 131.08 USD | 38,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1755` | 147.21 USD | 38,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1815` | 102.00 USD | 38,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1825` | 514.28 USD | 39,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1855` | 166.95 USD | 39,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1865` | 199.93 USD | 39,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2015` | 973.99 USD | 40,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0225` | 112,690.00 USD | 0.00 USD | 114.73 USD | `-77.78%` | `5,098.90` |
| `Live` | `Long` | `0.0305` | 112,570.00 USD | 0.00 USD | 1,320.00 USD | `-69.88%` | `43,265.90` |
| `Live` | `Long` | `0.0345` | 111,250.00 USD | 0.00 USD | 207.00 USD | `-65.93%` | `6,000.00` |
| `Live` | `Long` | `0.0535` | 111,050.00 USD | 0.00 USD | 410.01 USD | `-47.16%` | `7,663.80` |
| `Live` | `Long` | `0.0575` | 110,640.00 USD | 0.00 USD | 829.69 USD | `-43.21%` | `14,429.40` |
| `Live` | `Long` | `0.0585` | 109,810.00 USD | 0.00 USD | 4,080.00 USD | `-42.22%` | `69,790.10` |
| `Live` | `Long` | `0.0615` | 105,720.00 USD | 0.00 USD | 1,100.00 USD | `-39.26%` | `17,943.80` |
| `Live` | `Long` | `0.0645` | 104,620.00 USD | 0.00 USD | 353.81 USD | `-36.30%` | `5,485.40` |
| `Live` | `Long` | `0.0655` | 104,270.00 USD | 0.00 USD | 361.16 USD | `-35.31%` | `5,513.90` |
| `Live` | `Long` | `0.0675` | 103,910.00 USD | 0.00 USD | 518.48 USD | `-33.33%` | `7,681.20` |
| `Live` | `Long` | `0.0685` | 103,390.00 USD | 0.00 USD | 1,920.00 USD | `-32.35%` | `28,000.00` |
| `Live` | `Long` | `0.0705` | 101,470.00 USD | 0.00 USD | 1,090.00 USD | `-30.37%` | `15,500.00` |
| `Live` | `Long` | `0.0725` | 100,380.00 USD | 0.00 USD | 64,900.00 USD | `-28.40%` | `895,143.10` |
| `Live` | `Long` | `0.0735` | 35,480.00 USD | 0.00 USD | 2,530.00 USD | `-27.41%` | `34,439.60` |
| `Live` | `Long` | `0.0745` | 32,950.00 USD | 0.00 USD | 2,300.00 USD | `-26.42%` | `30,851.90` |
| `Live` | `Long` | `0.0755` | 30,650.00 USD | 0.00 USD | 1,020.00 USD | `-25.43%` | `13,481.90` |
| `Live` | `Long` | `0.0765` | 29,630.00 USD | 0.00 USD | 1,320.00 USD | `-24.44%` | `17,254.50` |
| `Live` | `Long` | `0.0775` | 28,310.00 USD | 0.00 USD | 878.62 USD | `-23.46%` | `11,337.00` |
| `Live` | `Long` | `0.0785` | 27,430.00 USD | 0.00 USD | 339.50 USD | `-22.47%` | `4,324.80` |
| `Live` | `Long` | `0.0795` | 27,090.00 USD | 0.00 USD | 2,710.00 USD | `-21.48%` | `34,073.20` |
| `Live` | `Long` | `0.0805` | 24,380.00 USD | 0.00 USD | 223.98 USD | `-20.49%` | `2,782.40` |
| `Live` | `Long` | `0.0815` | 24,160.00 USD | 0.00 USD | 1,560.00 USD | `-19.51%` | `19,181.40` |
| `Live` | `Long` | `0.0825` | 22,600.00 USD | 0.00 USD | 140.74 USD | `-18.52%` | `1,705.90` |
| `Live` | `Long` | `0.0845` | 22,460.00 USD | 0.00 USD | 14,300.00 USD | `-16.54%` | `169,238.60` |
| `Live` | `Long` | `0.0855` | 8,160.00 USD | 0.00 USD | 1,710.00 USD | `-15.56%` | `20,000.00` |
| `Live` | `Long` | `0.0865` | 6,450.00 USD | 0.00 USD | 146.06 USD | `-14.57%` | `1,688.60` |
| `Live` | `Long` | `0.0875` | 6,300.00 USD | 0.00 USD | 793.17 USD | `-13.58%` | `9,064.80` |
| `Live` | `Long` | `0.0895` | 5,510.00 USD | 0.00 USD | 3,270.00 USD | `-11.60%` | `36,562.50` |
| `Live` | `Long` | `0.0905` | 2,230.00 USD | 0.00 USD | 2,230.00 USD | `-10.62%` | `24,685.10` |
| `Live` | `Short` | `0.1205` | 3,590.00 USD | 3,590.00 USD | 0.00 USD | `+19.01%` | `29,751.90` |
| `Live` | `Short` | `0.1225` | 4,310.00 USD | 721.08 USD | 0.00 USD | `+20.99%` | `5,886.40` |
| `Live` | `Short` | `0.1385` | 4,520.00 USD | 217.97 USD | 0.00 USD | `+36.79%` | `1,573.80` |
| `Live` | `Short` | `0.1415` | 8,330.00 USD | 3,800.00 USD | 0.00 USD | `+39.75%` | `26,889.40` |
| `Live` | `Short` | `0.1455` | 31,380.00 USD | 23,050.00 USD | 0.00 USD | `+43.70%` | `158,447.40` |
| `Live` | `Short` | `0.1525` | 37,470.00 USD | 6,090.00 USD | 0.00 USD | `+50.62%` | `39,929.50` |
| `Live` | `Short` | `0.1565` | 38,020.00 USD | 550.61 USD | 0.00 USD | `+54.57%` | `3,518.30` |
| `Live` | `Short` | `0.1695` | 38,190.00 USD | 169.25 USD | 0.00 USD | `+67.41%` | `998.50` |
| `Live` | `Short` | `0.1745` | 38,320.00 USD | 131.08 USD | 0.00 USD | `+72.35%` | `751.20` |
| `Live` | `Short` | `0.1755` | 38,470.00 USD | 147.21 USD | 0.00 USD | `+73.33%` | `838.80` |
| `Live` | `Short` | `0.1815` | 38,570.00 USD | 102.00 USD | 0.00 USD | `+79.26%` | `562.00` |
| `Live` | `Short` | `0.1825` | 39,090.00 USD | 514.28 USD | 0.00 USD | `+80.25%` | `2,818.00` |
| `Live` | `Short` | `0.1855` | 39,250.00 USD | 166.95 USD | 0.00 USD | `+83.21%` | `900.00` |
| `Live` | `Short` | `0.1865` | 39,450.00 USD | 199.93 USD | 0.00 USD | `+84.20%` | `1,072.00` |
| `Live` | `Short` | `0.2015` | 40,430.00 USD | 973.99 USD | 0.00 USD | `+99.01%` | `4,833.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0635` | 17,880.00 USD | 0.00 USD | 1,140.00 USD | `-37.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 16,740.00 USD | 0.00 USD | 773.46 USD | `-30.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 15,970.00 USD | 0.00 USD | 592.27 USD | `-29.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 15,370.00 USD | 0.00 USD | 755.00 USD | `-25.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0805` | 14,620.00 USD | 0.00 USD | 411.06 USD | `-20.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0815` | 14,210.00 USD | 0.00 USD | 285.01 USD | `-19.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0835` | 13,920.00 USD | 0.00 USD | 456.70 USD | `-17.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0845` | 13,470.00 USD | 0.00 USD | 171.09 USD | `-16.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 13,290.00 USD | 0.00 USD | 631.58 USD | `-15.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 12,660.00 USD | 0.00 USD | 782.05 USD | `-12.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 11,880.00 USD | 0.00 USD | 444.62 USD | `-10.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0915` | 11,440.00 USD | 0.00 USD | 623.91 USD | `-9.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 10,810.00 USD | 0.00 USD | 485.13 USD | `-6.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0965` | 10,330.00 USD | 0.00 USD | 5,700.00 USD | `-4.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0975` | 4,630.00 USD | 0.00 USD | 720.22 USD | `-3.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0985` | 3,910.00 USD | 0.00 USD | 931.75 USD | `-2.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0995` | 2,980.00 USD | 0.00 USD | 801.64 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 2,180.00 USD | 0.00 USD | 2,180.00 USD | `-0.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1015` | 903.42 USD | 903.42 USD | 0.00 USD | `+0.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1025` | 1,680.00 USD | 780.70 USD | 0.00 USD | `+1.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1035` | 1,890.00 USD | 209.56 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,000.00 USD | 105.53 USD | 0.00 USD | `+3.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 9,770.00 USD | 7,770.00 USD | 0.00 USD | `+4.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 119,050.00 USD | 109,280.00 USD | 0.00 USD | `+5.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1075` | 140,960.00 USD | 21,900.00 USD | 0.00 USD | `+6.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 141,120.00 USD | 160.20 USD | 0.00 USD | `+9.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 141,960.00 USD | 839.64 USD | 0.00 USD | `+10.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1125` | 142,740.00 USD | 786.65 USD | 0.00 USD | `+11.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1135` | 142,860.00 USD | 116.27 USD | 0.00 USD | `+12.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 143,000.00 USD | 137.71 USD | 0.00 USD | `+14.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1165` | 143,180.00 USD | 180.81 USD | 0.00 USD | `+15.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1175` | 143,540.00 USD | 363.49 USD | 0.00 USD | `+16.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1185` | 143,810.00 USD | 265.74 USD | 0.00 USD | `+17.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1195` | 158,440.00 USD | 14,640.00 USD | 0.00 USD | `+18.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1225` | 159,420.00 USD | 980.00 USD | 0.00 USD | `+20.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1235` | 166,790.00 USD | 7,370.00 USD | 0.00 USD | `+21.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1255` | 171,160.00 USD | 4,380.00 USD | 0.00 USD | `+23.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1315` | 202,730.00 USD | 31,560.00 USD | 0.00 USD | `+29.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1335` | 204,040.00 USD | 1,310.00 USD | 0.00 USD | `+31.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1345` | 208,190.00 USD | 4,150.00 USD | 0.00 USD | `+32.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1365` | 215,940.00 USD | 7,750.00 USD | 0.00 USD | `+34.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1405` | 229,050.00 USD | 13,110.00 USD | 0.00 USD | `+38.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1425` | 229,150.00 USD | 102.22 USD | 0.00 USD | `+40.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1435` | 236,330.00 USD | 7,180.00 USD | 0.00 USD | `+41.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1485` | 238,970.00 USD | 2,650.00 USD | 0.00 USD | `+46.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1525` | 242,740.00 USD | 3,770.00 USD | 0.00 USD | `+50.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 242,920.00 USD | 184.49 USD | 0.00 USD | `+53.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 245,730.00 USD | 2,810.00 USD | 0.00 USD | `+54.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 245,950.00 USD | 219.81 USD | 0.00 USD | `+55.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 246,230.00 USD | 277.62 USD | 0.00 USD | `+61.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 248,260.00 USD | 2,030.00 USD | 0.00 USD | `+67.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 248,470.00 USD | 216.55 USD | 0.00 USD | `+72.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 248,590.00 USD | 117.26 USD | 0.00 USD | `+95.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 269,120.00 USD | 20,530.00 USD | 0.00 USD | `+98.02%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0827` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 8,590.00 USD |
| `7D` | `0.0830` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 28.49 USD |
| `7D` | `0.0860` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 1,880.00 USD | 0.00 USD | 2,160.00 USD |
| `7D` | `0.0863` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 0.00 USD | 1,880.00 USD | 7,040.00 USD |
| `7D` | `0.0866` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 0.00 USD | 1,980.00 USD | 15,400.00 USD |
| `7D` | `0.0869` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 2,900.00 USD |
| `7D` | `0.0872` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 0.00 USD | 1,200.00 USD | 5,830.00 USD |
| `7D` | `0.0875` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 6,010.00 USD | 0.00 USD | 5,780.00 USD |
| `7D` | `0.0878` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 9,200.00 USD | 7,660.00 USD | 28,720.00 USD |
| `7D` | `0.0881` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 9,390.00 USD | 2,660.00 USD | 12,940.00 USD |
| `1D` | `0.0884` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 767.42 USD | 1,480.00 USD | 11,380.00 USD |
| `7D` | `0.0884` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 7,040.00 USD | 8,030.00 USD | 21,730.00 USD |
| `1D` | `0.0886` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 6,600.00 USD | 2,200.00 USD | 10,320.00 USD |
| `7D` | `0.0887` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD |
| `1D` | `0.0888` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 1,690.00 USD | 1,080.00 USD | 669.95 USD |
| `1D` | `0.0890` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 755.35 USD | 1,740.00 USD | 3,260.00 USD |
| `7D` | `0.0890` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 14,610.00 USD | 5,880.00 USD | 13,160.00 USD |
| `1D` | `0.0892` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 983.61 USD | 813.86 USD | 2,050.00 USD |
| `7D` | `0.0893` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD |
| `1D` | `0.0894` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 0.00 USD | 1,080.00 USD | 554.64 USD |
| `7D` | `0.0896` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 5,760.00 USD | 2,110.00 USD | 6,870.00 USD |
| `1D` | `0.0898` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 0.00 USD | 1,330.00 USD | 7.83 USD |
| `7D` | `0.0899` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 3,390.00 USD | 927.82 USD | 4,520.00 USD |
| `1D` | `0.0900` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,170.00 USD | 494.55 USD | 41.91 USD |
| `1D` | `0.0902` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 2,150.00 USD | 1,420.00 USD | 2.62 USD |
| `7D` | `0.0902` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 2,270.00 USD | 910.78 USD | 1,320.00 USD |
| `1D` | `0.0904` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 0.00 USD | 2,530.00 USD | 3,080.00 USD |
| `7D` | `0.0905` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 10,350.00 USD | 996.61 USD | 4,170.00 USD |
| `1D` | `0.0906` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 1,250.00 USD | 486.35 USD | 3,130.00 USD |
| `1D` | `0.0908` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 0.00 USD | 494.75 USD | 1,700.00 USD |
| `7D` | `0.0908` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD |
| `1D` | `0.0910` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 6,520.00 USD | 1,110.00 USD | 10.67 USD |
| `7D` | `0.0911` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD |
| `1D` | `0.0912` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 0.00 USD | 1,450.00 USD | 793.84 USD |
| `1D` | `0.0914` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 1,930.00 USD | 1,290.00 USD | 61.20 USD |
| `7D` | `0.0914` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 1,670.00 USD | 903.90 USD | 74.70 USD |
| `1D` | `0.0916` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 6,590.00 USD | 1,680.00 USD | 54.60 USD |
| `7D` | `0.0917` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 8,050.00 USD |
| `1D` | `0.0918` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 5,140.00 USD | 3,470.00 USD | 2,590.00 USD |
| `1D` | `0.0920` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 3,690.00 USD | 504.78 USD | 20,380.00 USD |
| `7D` | `0.0920` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 223.39 USD |
| `1D` | `0.0922` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 0.00 USD | 1,320.00 USD | 12,110.00 USD |
| `7D` | `0.0923` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 0.00 USD | 6,430.00 USD | 43,900.00 USD |
| `1D` | `0.0924` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 1,410.00 USD | 3,060.00 USD | 39,640.00 USD |
| `1D` | `0.0926` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 3,270.00 USD | 2,820.00 USD | 39.19 USD |
| `7D` | `0.0926` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD |
| `7D` | `0.0929` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD |
| `1D` | `0.0930` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 4,360.00 USD | 1,190.00 USD | 7,480.00 USD |
| `1D` | `0.0932` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 3,330.00 USD |
| `7D` | `0.0932` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 12,290.00 USD |
| `1D` | `0.0934` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 20,740.00 USD | 3,830.00 USD | 17,340.00 USD |
| `7D` | `0.0935` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 19,560.00 USD | 8,160.00 USD | 31,940.00 USD |
| `1D` | `0.0936` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 4,760.00 USD | 9,360.00 USD | 16,350.00 USD |
| `1D` | `0.0938` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 8,170.00 USD | 2,920.00 USD | 46,410.00 USD |
| `7D` | `0.0938` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 248.29 USD |
| `1D` | `0.0940` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD |
| `7D` | `0.0941` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 16,100.00 USD | 18,340.00 USD | 90,220.00 USD |
| `1D` | `0.0942` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 3,500.00 USD | 16,110.00 USD | 49,210.00 USD |
| `1D` | `0.0944` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 11,620.00 USD | 4,860.00 USD | 36,440.00 USD |
| `7D` | `0.0944` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 8,040.00 USD | 2,010.00 USD | 37,540.00 USD |
| `1D` | `0.0946` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 4,130.00 USD | 5,280.00 USD | 10,200.00 USD |
| `7D` | `0.0947` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 2,200.00 USD | 1,810.00 USD | 177.04 USD |
| `1D` | `0.0948` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 1,100.00 USD | 42.76 USD |
| `1D` | `0.0950` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 12,180.00 USD | 6,710.00 USD | 22,870.00 USD |
| `7D` | `0.0950` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 3,770.00 USD | 9,700.00 USD | 27,060.00 USD |
| `1D` | `0.0952` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 0.00 USD | 853.02 USD | 6,700.00 USD |
| `7D` | `0.0953` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 0.00 USD | 8,150.00 USD | 0.00 USD |
| `1D` | `0.0954` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 41,470.00 USD | 11,160.00 USD | 21,050.00 USD |
| `1D` | `0.0956` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 18,680.00 USD | 9,390.00 USD | 36,890.00 USD |
| `7D` | `0.0956` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 39,120.00 USD | 13,670.00 USD | 51,170.00 USD |
| `1D` | `0.0958` | 982,630.00 USD | 0.00 USD | 982,630.00 USD | 7,180.00 USD | 4,290.00 USD | 22,220.00 USD |
| `7D` | `0.0959` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 28,110.00 USD | 0.00 USD | 21,370.00 USD |
| `1D` | `0.0960` | 948,940.00 USD | 0.00 USD | 948,940.00 USD | 0.00 USD | 16,940.00 USD | 55.21 USD |
| `1D` | `0.0962` | 931,950.00 USD | 0.00 USD | 931,950.00 USD | 8,920.00 USD | 15,440.00 USD | 27,730.00 USD |
| `7D` | `0.0962` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 12,340.00 USD | 16,920.00 USD | 95,050.00 USD |
| `1D` | `0.0964` | 879,860.00 USD | 0.00 USD | 879,860.00 USD | 31,490.00 USD | 10,380.00 USD | 28,100.00 USD |
| `7D` | `0.0965` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 0.00 USD | 6,410.00 USD | 86.68 USD |
| `1D` | `0.0966` | 809,890.00 USD | 0.00 USD | 809,890.00 USD | 0.00 USD | 3,880.00 USD | 874.45 USD |
| `1D` | `0.0968` | 805,130.00 USD | 0.00 USD | 805,130.00 USD | 0.00 USD | 2,960.00 USD | 2,300.00 USD |
| `7D` | `0.0968` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 7,490.00 USD | 0.00 USD | 59,000.00 USD |
| `1D` | `0.0970` | 799,870.00 USD | 0.00 USD | 799,870.00 USD | 8,360.00 USD | 8,640.00 USD | 16,330.00 USD |
| `7D` | `0.0971` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 0.00 USD | 7,090.00 USD | 5,010.00 USD |
| `1D` | `0.0972` | 766,540.00 USD | 0.00 USD | 766,540.00 USD | 2,860.00 USD | 3,220.00 USD | 2,050.00 USD |
| `1D` | `0.0974` | 758,410.00 USD | 0.00 USD | 758,410.00 USD | 0.00 USD | 7,010.00 USD | 14.85 USD |
| `7D` | `0.0974` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 16,310.00 USD | 104.80 USD |
| `1D` | `0.0976` | 751,390.00 USD | 0.00 USD | 751,390.00 USD | 0.00 USD | 765.93 USD | 961.09 USD |
| `1D` | `0.0978` | 749,670.00 USD | 0.00 USD | 749,670.00 USD | 0.00 USD | 817.22 USD | 45.18 USD |
| `1D` | `0.0980` | 748,800.00 USD | 0.00 USD | 748,800.00 USD | 0.00 USD | 2,470.00 USD | 21,250.00 USD |
| `1D` | `0.0982` | 725,080.00 USD | 0.00 USD | 725,080.00 USD | 5,470.00 USD | 2,550.00 USD | 5.60 USD |
| `7D` | `0.0983` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 3,720.00 USD | 11,350.00 USD |
| `1D` | `0.0984` | 717,060.00 USD | 0.00 USD | 717,060.00 USD | 1,670.00 USD | 9,040.00 USD | 8,240.00 USD |
| `1D` | `0.0986` | 698,110.00 USD | 0.00 USD | 698,110.00 USD | 0.00 USD | 5,480.00 USD | 1,560.00 USD |
| `7D` | `0.0986` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 0.00 USD | 14,660.00 USD | 0.00 USD |
| `1D` | `0.0988` | 691,070.00 USD | 0.00 USD | 691,070.00 USD | 23,710.00 USD | 1,540.00 USD | 31,840.00 USD |
| `7D` | `0.0989` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 17,640.00 USD | 7,820.00 USD | 0.00 USD |
| `1D` | `0.0990` | 633,980.00 USD | 0.00 USD | 633,980.00 USD | 4,730.00 USD | 0.00 USD | 5.91 USD |
| `1D` | `0.0992` | 629,240.00 USD | 0.00 USD | 629,240.00 USD | 76,570.00 USD | 3,020.00 USD | 26,680.00 USD |
| `7D` | `0.0992` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 27,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0994` | 522,970.00 USD | 0.00 USD | 522,970.00 USD | 26,200.00 USD | 0.00 USD | 21,960.00 USD |
| `7D` | `0.0995` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 63,330.00 USD | 0.00 USD | 76,030.00 USD |
| `1D` | `0.0996` | 474,810.00 USD | 0.00 USD | 474,810.00 USD | 11,810.00 USD | 2,450.00 USD | 71,280.00 USD |
| `1D` | `0.0998` | 389,280.00 USD | 0.00 USD | 389,280.00 USD | 7,180.00 USD | 5,820.00 USD | 59,230.00 USD |
| `7D` | `0.0998` | 900,500.00 USD | 0.00 USD | 900,500.00 USD | 28,450.00 USD | 17,040.00 USD | 135,270.00 USD |
| `1D` | `0.1000` | 317,050.00 USD | 0.00 USD | 317,050.00 USD | 0.00 USD | 11,820.00 USD | 37,050.00 USD |
| `7D` | `0.1001` | 719,740.00 USD | 0.00 USD | 719,740.00 USD | 76,560.00 USD | 25,570.00 USD | 107,970.00 USD |
| `1D` | `0.1002` | 268,180.00 USD | 0.00 USD | 268,180.00 USD | 0.00 USD | 0.00 USD | 42,920.00 USD |
| `1D` | `0.1004` | 225,260.00 USD | 0.00 USD | 225,260.00 USD | 34,770.00 USD | 8,690.00 USD | 35,450.00 USD |
| `7D` | `0.1004` | 509,630.00 USD | 0.00 USD | 509,630.00 USD | 22,470.00 USD | 7,440.00 USD | 46,130.00 USD |
| `1D` | `0.1006` | 146,340.00 USD | 0.00 USD | 146,340.00 USD | 3,340.00 USD | 10,340.00 USD | 8,870.00 USD |
| `7D` | `0.1007` | 433,580.00 USD | 0.00 USD | 433,580.00 USD | 20,870.00 USD | 7,760.00 USD | 100,230.00 USD |
| `1D` | `0.1008` | 123,800.00 USD | 0.00 USD | 123,800.00 USD | 4,360.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1010` | 119,440.00 USD | 0.00 USD | 119,440.00 USD | 6,930.00 USD | 4,070.00 USD | 14,820.00 USD |
| `7D` | `0.1010` | 304,720.00 USD | 0.00 USD | 304,720.00 USD | 17,340.00 USD | 13,670.00 USD | 54,030.00 USD |
| `1D` | `0.1012` | 93,610.00 USD | 0.00 USD | 93,610.00 USD | 0.00 USD | 0.00 USD | 11,410.00 USD |
| `7D` | `0.1013` | 219,680.00 USD | 0.00 USD | 219,680.00 USD | 34,830.00 USD | 28,370.00 USD | 25,450.00 USD |
| `1D` | `0.1014` | 82,200.00 USD | 0.00 USD | 82,200.00 USD | 0.00 USD | 449.10 USD | 11,100.00 USD |
| `1D` | `0.1016` | 70,660.00 USD | 0.00 USD | 70,660.00 USD | 8,170.00 USD | 775.38 USD | 13,240.00 USD |
| `7D` | `0.1016` | 131,030.00 USD | 0.00 USD | 131,030.00 USD | 15,440.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1018` | 48,470.00 USD | 0.00 USD | 48,470.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD |
| `7D` | `0.1019` | 115,590.00 USD | 0.00 USD | 115,590.00 USD | 26,150.00 USD | 8,460.00 USD | 20,610.00 USD |
| `1D` | `0.1020` | 46,930.00 USD | 0.00 USD | 46,930.00 USD | 3,500.00 USD | 0.00 USD | 11,590.00 USD |
| `1D` | `0.1022` | 31,840.00 USD | 0.00 USD | 31,840.00 USD | 10,130.00 USD | 7,410.00 USD | 5,990.00 USD |
| `7D` | `0.1022` | 60,360.00 USD | 0.00 USD | 60,360.00 USD | 18,100.00 USD | 3,270.00 USD | 37,440.00 USD |
| `1D` | `0.1024` | 8,310.00 USD | 0.00 USD | 8,310.00 USD | 0.00 USD | 8,270.00 USD | 42.48 USD |
| `7D` | `0.1025` | 1,550.00 USD | 0.00 USD | 1,550.00 USD | 1,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1026` | 13.28 USD | 13.28 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.28 USD |
| `1D` | `0.1026` | 26.56 USD | 26.56 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13.28 USD |
| `7D` | `0.1026` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1028` | 20,710.00 USD | 20,710.00 USD | 0.00 USD | 3,430.00 USD | 3,870.00 USD | 13,380.00 USD |
| `7D` | `0.1028` | 29,300.00 USD | 29,300.00 USD | 0.00 USD | 3,800.00 USD | 1,810.00 USD | 23,700.00 USD |
| `1D` | `0.1030` | 58,940.00 USD | 58,940.00 USD | 0.00 USD | 9,720.00 USD | 9,300.00 USD | 19,210.00 USD |
| `7D` | `0.1031` | 58,670.00 USD | 58,670.00 USD | 0.00 USD | 19,560.00 USD | 9,810.00 USD | 0.00 USD |
| `1D` | `0.1032` | 120,370.00 USD | 120,370.00 USD | 0.00 USD | 33,630.00 USD | 7,240.00 USD | 20,560.00 USD |
| `1D` | `0.1034` | 155,780.00 USD | 155,780.00 USD | 0.00 USD | 15,150.00 USD | 7,420.00 USD | 12,840.00 USD |
| `7D` | `0.1034` | 92,770.00 USD | 92,770.00 USD | 0.00 USD | 18,920.00 USD | 15,180.00 USD | 0.00 USD |
| `1D` | `0.1036` | 165,620.00 USD | 165,620.00 USD | 0.00 USD | 2,150.00 USD | 7,660.00 USD | 28.94 USD |
| `7D` | `0.1037` | 106,300.00 USD | 106,300.00 USD | 0.00 USD | 2,710.00 USD | 10,710.00 USD | 108.00 USD |
| `1D` | `0.1038` | 222,190.00 USD | 222,190.00 USD | 0.00 USD | 34,400.00 USD | 15,130.00 USD | 7,040.00 USD |
| `1D` | `0.1040` | 269,140.00 USD | 269,140.00 USD | 0.00 USD | 12,950.00 USD | 18,810.00 USD | 15,190.00 USD |
| `7D` | `0.1040` | 153,900.00 USD | 153,900.00 USD | 0.00 USD | 5,940.00 USD | 10,300.00 USD | 31,350.00 USD |
| `1D` | `0.1042` | 307,340.00 USD | 307,340.00 USD | 0.00 USD | 5,060.00 USD | 7,360.00 USD | 25,780.00 USD |
| `7D` | `0.1043` | 198,550.00 USD | 198,550.00 USD | 0.00 USD | 15,960.00 USD | 5,980.00 USD | 22,700.00 USD |
| `1D` | `0.1044` | 339,440.00 USD | 339,440.00 USD | 0.00 USD | 5,150.00 USD | 16,420.00 USD | 10,530.00 USD |
| `1D` | `0.1046` | 392,670.00 USD | 392,670.00 USD | 0.00 USD | 10,400.00 USD | 8,320.00 USD | 34,510.00 USD |
| `7D` | `0.1046` | 283,030.00 USD | 283,030.00 USD | 0.00 USD | 0.00 USD | 24,330.00 USD | 60,160.00 USD |
| `1D` | `0.1048` | 513,540.00 USD | 513,540.00 USD | 0.00 USD | 25,030.00 USD | 13,650.00 USD | 82,200.00 USD |
| `7D` | `0.1049` | 407,530.00 USD | 407,530.00 USD | 0.00 USD | 34,790.00 USD | 6,530.00 USD | 83,180.00 USD |
| `1D` | `0.1050` | 570,330.00 USD | 570,330.00 USD | 0.00 USD | 32,820.00 USD | 13,230.00 USD | 10,730.00 USD |
| `1D` | `0.1052` | 673,530.00 USD | 673,530.00 USD | 0.00 USD | 43,930.00 USD | 14,110.00 USD | 45,160.00 USD |
| `7D` | `0.1052` | 585,370.00 USD | 585,370.00 USD | 0.00 USD | 28,200.00 USD | 24,160.00 USD | 125,480.00 USD |
| `1D` | `0.1054` | 829,700.00 USD | 829,700.00 USD | 0.00 USD | 56,700.00 USD | 20,100.00 USD | 79,360.00 USD |
| `7D` | `0.1055` | 964,280.00 USD | 964,280.00 USD | 0.00 USD | 122,840.00 USD | 44,430.00 USD | 211,630.00 USD |
| `1D` | `0.1056` | 892,900.00 USD | 892,900.00 USD | 0.00 USD | 16,600.00 USD | 22,130.00 USD | 24,480.00 USD |
| `1D` | `0.1058` | 988,450.00 USD | 988,450.00 USD | 0.00 USD | 28,780.00 USD | 6,490.00 USD | 60,270.00 USD |
| `7D` | `0.1058` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 105,620.00 USD | 58,510.00 USD | 202,430.00 USD |
| `1D` | `0.1060` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 31,730.00 USD | 2,700.00 USD | 36,930.00 USD |
| `7D` | `0.1061` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 75,540.00 USD | 67,860.00 USD | 118,420.00 USD |
| `1D` | `0.1062` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 31,870.00 USD | 2,030.00 USD | 79,790.00 USD |
| `1D` | `0.1064` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 1,640.00 USD | 2,630.00 USD | 44,860.00 USD |
| `7D` | `0.1064` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 52,580.00 USD | 188,900.00 USD |
| `1D` | `0.1066` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 6,940.00 USD | 5,010.00 USD | 41,950.00 USD |
| `7D` | `0.1067` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 57,800.00 USD | 144,020.00 USD |
| `1D` | `0.1068` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 4,700.00 USD | 4,180.00 USD | 57,160.00 USD |
| `1D` | `0.1070` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 16,460.00 USD | 8,600.00 USD | 46,540.00 USD |
| `7D` | `0.1070` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 57,770.00 USD | 134,760.00 USD |
| `1D` | `0.1072` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 857.22 USD | 1,390.00 USD | 323.34 USD |
| `7D` | `0.1073` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 7,820.00 USD | 20,440.00 USD | 10,320.00 USD |
| `1D` | `0.1074` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,930.00 USD |
| `1D` | `0.1076` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 1,440.00 USD | 857.82 USD | 2,880.00 USD |
| `7D` | `0.1076` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,600.00 USD |
| `1D` | `0.1078` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 3,440.00 USD | 17,180.00 USD |
| `7D` | `0.1079` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 5,620.00 USD | 3,380.00 USD | 10,010.00 USD |
| `1D` | `0.1080` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 1,480.00 USD | 5,600.00 USD |
| `1D` | `0.1082` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 5,820.00 USD | 7,440.00 USD | 5,080.00 USD |
| `7D` | `0.1082` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 154.22 USD |
| `1D` | `0.1084` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 7,990.00 USD | 385.06 USD | 36,080.00 USD |
| `7D` | `0.1085` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1086` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 4,220.00 USD | 2,240.00 USD | 72,980.00 USD |
| `1D` | `0.1088` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 40,240.00 USD | 1,040.00 USD | 9,410.00 USD |
| `7D` | `0.1088` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 5,290.00 USD | 1,420.00 USD | 9,660.00 USD |
| `1D` | `0.1090` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 39,470.00 USD | 813.86 USD | 2,110.00 USD |
| `7D` | `0.1091` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD |
| `1D` | `0.1092` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 10,290.00 USD | 1,080.00 USD | 53.09 USD |
| `1D` | `0.1094` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 13,100.00 USD | 0.00 USD | 13,850.00 USD |
| `7D` | `0.1094` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 1,500.00 USD | 8,810.00 USD |
| `1D` | `0.1096` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 7,670.00 USD |
| `7D` | `0.1097` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1098` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 13,380.00 USD | 4,460.00 USD | 22,820.00 USD |
| `1D` | `0.1100` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 3,310.00 USD | 4,300.00 USD |
| `7D` | `0.1100` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 21,880.00 USD |
| `1D` | `0.1102` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 5,570.00 USD | 509.08 USD | 96.09 USD |
| `7D` | `0.1103` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1104` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 6,920.00 USD | 11,640.00 USD | 1,180.00 USD |
| `1D` | `0.1106` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 12,720.00 USD | 30,860.00 USD |
| `7D` | `0.1106` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 22,880.00 USD | 16,130.00 USD |
| `1D` | `0.1108` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 5,220.00 USD | 1,610.00 USD | 17,380.00 USD |
| `7D` | `0.1109` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD |
| `1D` | `0.1110` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 494.75 USD | 916.88 USD |
| `1D` | `0.1112` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 10,780.00 USD | 747.13 USD | 22.61 USD |
| `7D` | `0.1112` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD |
| `1D` | `0.1114` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 15,810.00 USD | 5,880.00 USD | 29,950.00 USD |
| `7D` | `0.1115` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28.89 USD |
| `1D` | `0.1116` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 6,690.00 USD | 12,550.00 USD | 6,930.00 USD |
| `1D` | `0.1118` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 25,510.00 USD | 17,530.00 USD | 52,780.00 USD |
| `7D` | `0.1118` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD |
| `1D` | `0.1120` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 27,100.00 USD | 10,220.00 USD | 9,830.00 USD |
| `7D` | `0.1121` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 17,760.00 USD | 0.00 USD | 38,410.00 USD |
| `1D` | `0.1122` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 16,670.00 USD | 5,240.00 USD | 15,070.00 USD |
| `1D` | `0.1124` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 17,090.00 USD | 6,120.00 USD | 9,820.00 USD |
| `7D` | `0.1124` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD |
| `1D` | `0.1126` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 9,370.00 USD | 10,060.00 USD | 18,480.00 USD |
| `7D` | `0.1127` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 3,720.00 USD | 15,310.00 USD |
| `1D` | `0.1128` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 10,120.00 USD | 0.00 USD | 12,900.00 USD |
| `1D` | `0.1130` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 7,970.00 USD | 2,630.00 USD | 16,290.00 USD |
| `7D` | `0.1130` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,320.00 USD |
| `1D` | `0.1132` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 19,390.00 USD | 10,550.00 USD | 16,210.00 USD |
| `7D` | `0.1133` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD |
| `1D` | `0.1134` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 4,040.00 USD | 12,980.00 USD | 13,830.00 USD |
| `1D` | `0.1135` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 787.70 USD | 4,160.00 USD |
| `7D` | `0.1136` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD |
| `7D` | `0.1139` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD |
| `7D` | `0.1142` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD |
| `7D` | `0.1145` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD |
| `7D` | `0.1148` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 175,990.00 USD |
| `7D` | `0.1151` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD |
| `7D` | `0.1154` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 243,190.00 USD | 26,970.00 USD | 202,050.00 USD |
| `7D` | `0.1157` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 173,120.00 USD | 25,290.00 USD | 98,310.00 USD |
| `7D` | `0.1160` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 131,160.00 USD | 32,830.00 USD | 109,320.00 USD |
| `7D` | `0.1163` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD |
| `7D` | `0.1166` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD |
| `7D` | `0.1169` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 82,770.00 USD | 26,150.00 USD | 117,900.00 USD |
| `7D` | `0.1172` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD |
| `7D` | `0.1175` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 75,590.00 USD | 17,930.00 USD | 81,630.00 USD |
| `7D` | `0.1178` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 89,510.00 USD | 25,350.00 USD | 60,700.00 USD |
| `7D` | `0.1181` | 5,910,000.00 USD | 5,910,000.00 USD | 0.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD |
| `7D` | `0.1184` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD |
| `7D` | `0.1187` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 5,620.00 USD | 17,120.00 USD | 59,700.00 USD |
| `7D` | `0.1190` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD |
| `7D` | `0.1193` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD |
| `7D` | `0.1196` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD |
| `7D` | `0.1199` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 2,470.00 USD | 13,190.00 USD | 52,120.00 USD |
| `7D` | `0.1202` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 131,660.00 USD | 14,930.00 USD | 32,790.00 USD |
| `7D` | `0.1205` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 117,120.00 USD | 48,510.00 USD | 40,590.00 USD |
| `7D` | `0.1208` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 39,480.00 USD | 20,870.00 USD | 39,590.00 USD |
| `7D` | `0.1211` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 72,500.00 USD | 25,920.00 USD | 76,780.00 USD |
| `7D` | `0.1214` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD |
| `7D` | `0.1217` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD |
| `7D` | `0.1220` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 34,050.00 USD | 6,400.00 USD | 54,700.00 USD |
| `7D` | `0.1223` | 7,460,000.00 USD | 7,460,000.00 USD | 0.00 USD | 73,610.00 USD | 15,050.00 USD | 37,740.00 USD |
| `7D` | `0.1226` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 42,530.00 USD | 16,510.00 USD | 5,210.00 USD |
| `7D` | `0.1229` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 63,930.00 USD | 33,570.00 USD | 28,680.00 USD |
| `7D` | `0.1232` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 51,420.00 USD | 12,080.00 USD | 37,600.00 USD |
| `7D` | `0.1235` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 15,040.00 USD | 5,390.00 USD | 16,760.00 USD |
| `7D` | `0.1236` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 4,080.00 USD | 0.00 USD | 2,800.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `63.80M` | Total OI Tokens: `622,517,041.2 OP`
  * 1h OI Change: `+0.81%` | 4h OI Change: `+4.72%` | 24h OI Change: `-13.11%`
  * Exchange Breakdown: Binance=`13.84M` | Bybit=`13.01M` | OKX=`3.80M` | Hyperliquid=`3.16M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-2.19K` | Last 24h: `-2.42K` | Last 3d: `-6.63K` | Last 7d: `-14.48K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0278%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0277%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0077%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `44.14%` | `55.86%` | `0.79` | 1,950,000.00 USD |
| `15M` | `Binance` | `52.45%` | `47.55%` | `1.10` | 526,400.00 USD |
| `15M` | `OKX` | `61%` | `39%` | `1.56` | 450,060.00 USD |
| `15M` | `Bybit` | `54.03%` | `45.97%` | `1.18` | 132,210.00 USD |
| `15M` | `KuCoin` | `47.38%` | `52.62%` | `0.90` | 166,050.00 USD |
| `15M` | `Gate` | `29.17%` | `70.83%` | `0.41` | 37,640.00 USD |
| `15M` | `Bitget` | `82.93%` | `17.07%` | `4.86` | 21,770.00 USD |
| `15M` | `BingX` | `5.4%` | `94.6%` | `0.06` | 306,560.00 USD |
| `15M` | `MEXC` | `58.68%` | `41.32%` | `1.42` | 5,250.00 USD |
| `15M` | `Bitunix` | `56.92%` | `43.08%` | `1.32` | 25,770.00 USD |
| `15M` | `Hyperliquid` | `76.44%` | `23.56%` | `3.24` | 2,490.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.12%` | `53.88%` | `0.86` | 201,720.00 USD |
| `15M` | `Crypto.com` | `100%` | `0%` | `1.00` | 28.39 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 72,990.00 USD |
| `15M` | `HTX` | `91.49%` | `8.51%` | `10.75` | 2,580.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `88.24%` | `11.76%` | `7.50` | 48.45 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 152.08 USD |
| `15M` | `Whale Positions` | `52.45%` | `47.55%` | `1.10` | 526,400.00 USD |
| `15M` | `Global Accounts` | `44.14%` | `55.86%` | `0.79` | 1,950,000.00 USD |
| `1H` | `OP` | `50.70%` | `49.30%` | `1.03` | 11,680,000.00 USD |
| `1H` | `Binance` | `53.61%` | `46.39%` | `1.16` | 3,940,000.00 USD |
| `1H` | `OKX` | `56.44%` | `43.56%` | `1.30` | 2,620,000.00 USD |
| `1H` | `Bybit` | `62.79%` | `37.21%` | `1.69` | 1,020,000.00 USD |
| `1H` | `KuCoin` | `51.5%` | `48.5%` | `1.06` | 621,110.00 USD |
| `1H` | `Gate` | `49.78%` | `50.22%` | `0.99` | 216,980.00 USD |
| `1H` | `Bitget` | `60.56%` | `39.44%` | `1.54` | 144,940.00 USD |
| `1H` | `BingX` | `21.7%` | `78.3%` | `0.28` | 457,970.00 USD |
| `1H` | `MEXC` | `66.52%` | `33.48%` | `1.99` | 176,020.00 USD |
| `1H` | `Bitunix` | `27.68%` | `72.32%` | `0.38` | 290,220.00 USD |
| `1H` | `Hyperliquid` | `84.67%` | `15.33%` | `5.52` | 43,640.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `45.07%` | `54.93%` | `0.82` | 1,710,000.00 USD |
| `1H` | `Crypto.com` | `85.7%` | `14.3%` | `5.99` | 178.80 USD |
| `1H` | `WhiteBIT` | `11.82%` | `88.18%` | `0.13` | 387,290.00 USD |
| `1H` | `HTX` | `16.96%` | `83.04%` | `0.20` | 25,670.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `96.35%` | `3.65%` | `26.40` | 14,070.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `37.72%` | `62.28%` | `0.61` | 1,070.00 USD |
| `1H` | `Whale Positions` | `53.61%` | `46.39%` | `1.16` | 3,940,000.00 USD |
| `1H` | `Global Accounts` | `50.70%` | `49.30%` | `1.03` | 11,680,000.00 USD |
| `4H` | `OP` | `46.49%` | `53.51%` | `0.87` | 77,920,000.00 USD |
| `4H` | `Binance` | `46.53%` | `53.47%` | `0.87` | 26,910,000.00 USD |
| `4H` | `OKX` | `50.59%` | `49.41%` | `1.02` | 18,580,000.00 USD |
| `4H` | `Bybit` | `50.49%` | `49.51%` | `1.02` | 6,140,000.00 USD |
| `4H` | `KuCoin` | `50.05%` | `49.95%` | `1.00` | 2,560,000.00 USD |
| `4H` | `Gate` | `47%` | `53%` | `0.89` | 1,660,000.00 USD |
| `4H` | `Bitget` | `49.53%` | `50.47%` | `0.98` | 2,040,000.00 USD |
| `4H` | `BingX` | `19.16%` | `80.84%` | `0.24` | 3,060,000.00 USD |
| `4H` | `MEXC` | `55.28%` | `44.72%` | `1.24` | 960,840.00 USD |
| `4H` | `Bitunix` | `50.57%` | `49.43%` | `1.02` | 2,680,000.00 USD |
| `4H` | `Hyperliquid` | `35.01%` | `64.99%` | `0.54` | 637,400.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.65%` | `52.35%` | `0.91` | 11,060,000.00 USD |
| `4H` | `Crypto.com` | `80.31%` | `19.69%` | `4.08` | 1,410.00 USD |
| `4H` | `WhiteBIT` | `5.68%` | `94.32%` | `0.06` | 1,420,000.00 USD |
| `4H` | `HTX` | `39.98%` | `60.02%` | `0.67` | 61,130.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `10.44%` | `89.56%` | `0.12` | 26,160.00 USD |
| `4H` | `Aster` | `43.4%` | `56.6%` | `0.77` | 96,630.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.3%` | `47.7%` | `1.10` | 40,440.00 USD |
| `4H` | `Whale Positions` | `46.53%` | `53.47%` | `0.87` | 26,910,000.00 USD |
| `4H` | `Global Accounts` | `46.49%` | `53.51%` | `0.87` | 77,920,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0976` | `0.0974` | `0.0976` | `0.0979` | `0.0970` | 1,011,824.45 USD | 364,728.70 USD | 647,095.75 USD | -282,367.05 USD | `-27.91%` | `6B / 15S` |
| `0:00 UTC` | `0.0984` | `0.0984` | `0.0984` | `0.0992` | `0.0978` | 803,922.63 USD | 438,559.35 USD | 365,363.29 USD | 73,196.06 USD | `+9.10%` | `32B / 10S` |
| `5:00 UTC` | `0.0992` | `0.0992` | `0.0992` | `0.0995` | `0.0989` | 394,380.07 USD | 199,715.01 USD | 194,665.06 USD | 5,049.95 USD | `+1.28%` | `10B / 6S` |
| `0:00 UTC` | `0.0989` | `0.0992` | `0.0989` | `0.0999` | `0.0988` | 347,230.40 USD | 177,310.87 USD | 169,919.53 USD | 7,391.34 USD | `+2.13%` | `21B / 7S` |
| `5:00 UTC` | `0.1001` | `0.1001` | `0.1001` | `0.1004` | `0.0996` | 360,867.60 USD | 243,343.04 USD | 117,524.56 USD | 125,818.48 USD | `+34.87%` | `30B / 1S` |
| `0:00 UTC` | `0.1005` | `0.1006` | `0.1005` | `0.1009` | `0.1002` | 321,574.58 USD | 208,787.55 USD | 112,787.03 USD | 96,000.52 USD | `+29.85%` | `23B / 4S` |
| `5:00 UTC` | `0.1009` | `0.1011` | `0.1009` | `0.1014` | `0.1006` | 597,276.02 USD | 343,393.62 USD | 253,882.40 USD | 89,511.23 USD | `+14.99%` | `17B / 7S` |
| `0:00 UTC` | `0.1017` | `0.1020` | `0.1017` | `0.1027` | `0.1012` | 617,993.11 USD | 329,792.38 USD | 288,200.73 USD | 41,591.66 USD | `+6.73%` | `38B / 17S` |
| `5:00 UTC` | `0.1023` | `0.1024` | `0.1023` | `0.1028` | `0.1021` | 423,419.23 USD | 254,886.37 USD | 168,532.86 USD | 86,353.50 USD | `+20.39%` | `21B / 4S` |
| `0:00 UTC` | `0.1026` | `0.1025` | `0.1026` | `0.1027` | `0.1022` | 249,941.60 USD | 120,390.67 USD | 129,550.93 USD | -9,160.26 USD | `-3.66%` | `13B / 7S` |

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
| `5m` | 3,670.00 USD | 19,350.00 USD | **`ACCUMULATION`** |
| `15m` | -6,340.00 USD | 93,660.00 USD | **`ACCUMULATION`** |
| `30m` | -1,920.00 USD | 218,060.00 USD | **`ACCUMULATION`** |
| `1h` | 82,560.00 USD | 440,400.00 USD | **`ACCUMULATION`** |
| `2h` | 324,860.00 USD | 657,560.00 USD | **`ACCUMULATION`** |
| `4h` | -38,620.00 USD | 374,770.00 USD | **`ACCUMULATION`** |
| `6h` | -36,430.00 USD | -1,770,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 244,810.00 USD | -3,960,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 51,420.00 USD | -4,360,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 256,200.00 USD | -3,850,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -119,000.00 USD | -14,380,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,280,000.00 USD | -82,940,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+3.67K` | 15m=`-6.34K` | 1h=`+82.56K` | 24h=`+256.20K`
* Futures Capital Netflows: 5m=`+19.35K` | 15m=`+93.66K` | 1h=`+440.40K` | 24h=`-3.85M`
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
  * `2026-10-30 11:03:23 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:09:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:10:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
