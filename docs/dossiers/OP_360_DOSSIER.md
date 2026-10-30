# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 10:56:00 IST` (`2026-10-30 05:26:00 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1022` | `0.1027` | `0.1021` | `0.1022` | `2,425,078` | 248,383.42 USD | -10,147.92 USD | `-4.09%` | -1,938,140.27 USD | `-1.25` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `0.1022` | `0.1025` | `0.1021` | `0.1024` | `1,429,426` | 146,307.33 USD | 18,848.41 USD | `+12.88%` | -1,919,291.86 USD | `-0.04` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1024` | `0.1025` | `0.1022` | `0.1025` | `1,051,157` | 107,543.52 USD | 37,810.23 USD | `+35.16%` | -1,881,481.63 USD | `+0.68` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1009` | `0.1013` | `0.1006` | `0.1012` | `5,910,996` | 597,276.02 USD | 89,511.23 USD | `+14.99%` | -2,049,421.64 USD | `+0.61` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1012` | `0.1027` | `0.1012` | `0.1022` | `6,059,384` | 617,993.11 USD | 41,591.66 USD | `+6.73%` | -2,007,829.98 USD | `+0.38` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1022` | `0.1025` | `0.1021` | `0.1025` | `2,481,525` | 253,947.44 USD | 56,755.24 USD | `+22.35%` | -1,951,074.74 USD | `+0.49` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.0981` | `0.0995` | `0.0970` | `0.0993` | `30,519,947` | 2,992,768.64 USD | -441,148.19 USD | `-14.74%` | -2,239,239.62 USD | `-0.72` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.0993` | `0.1013` | `0.0988` | `0.1012` | `16,216,904` | 1,626,948.60 USD | 318,721.56 USD | `+19.59%` | -1,920,518.05 USD | `+0.94` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.1012` | `0.1027` | `0.1012` | `0.1025` | `8,540,909` | 871,940.55 USD | 98,346.90 USD | `+11.28%` | -1,822,171.16 USD | `+0.46` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -1,009,359.71 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,347,386.10 USD | `-1.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1027` | `0.0988` | `0.1025` | `24,757,814` | 2,498,889.15 USD | 417,068.46 USD | `+16.69%` | -1,930,317.64 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | 483,978.43 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | 307,838.15 USD | `-1.31` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -1,009,359.71 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,347,386.10 USD | `-1.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1027` | `0.0988` | `0.1025` | `24,757,814` | 2,498,889.15 USD | 417,068.46 USD | `+16.69%` | -1,930,317.64 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:53:16 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1099` | 9,518.97 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 9.52K USD at 0.1099 USD [API] | `2026-10-29 01:52:47` |
| `ANNOUNCEMENT` | `INFO` | `0.1099` | 7,294.20 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 7.29K USD at 0.1099 USD [API] | `2026-10-29 01:52:47` |
| `ANNOUNCEMENT` | `INFO` | `0.1099` | 9,522.44 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 9.52K USD at 0.1099 USD [API] | `2026-10-29 01:52:47` |
| `ANNOUNCEMENT` | `INFO` | `0.1100` | 5,425.00 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 5.42K USD at 0.1100 USD [API] | `2026-10-29 01:52:47` |


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
| `7D` | `Long Liquidation` | `0.0827` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 8,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0830` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 28.49 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0845` | 14,300.00 USD | 22,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 1,710.00 USD | 8,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0860` | 2,160,000.00 USD | 2,160,000.00 USD | 1,880.00 USD | 0.00 USD | 2,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0863` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 1,880.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0865` | 146.06 USD | 6,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0866` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 1,980.00 USD | 15,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0869` | 1,690,000.00 USD | 1,690,000.00 USD | 2,790.00 USD | 0.00 USD | 50.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0869` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0871` | 1,680,000.00 USD | 1,680,000.00 USD | 1,740.00 USD | 0.00 USD | 997.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0872` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 1,200.00 USD | 5,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0873` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 680.22 USD | 5,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0875` | 1,670,000.00 USD | 1,670,000.00 USD | 9,010.00 USD | 437.13 USD | 3,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0875` | 2,120,000.00 USD | 2,120,000.00 USD | 6,010.00 USD | 0.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0875` | 793.17 USD | 6,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0877` | 1,660,000.00 USD | 1,660,000.00 USD | 4,110.00 USD | 3,520.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0878` | 2,110,000.00 USD | 2,110,000.00 USD | 9,200.00 USD | 7,660.00 USD | 28,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0879` | 1,650,000.00 USD | 1,650,000.00 USD | 2,340.00 USD | 2,000.00 USD | 9,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0881` | 1,630,000.00 USD | 1,630,000.00 USD | 1,670.00 USD | 1,700.00 USD | 530.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0881` | 2,070,000.00 USD | 2,070,000.00 USD | 9,390.00 USD | 2,660.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0883` | 1,630,000.00 USD | 1,630,000.00 USD | 2,370.00 USD | 4,960.00 USD | 9,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0884` | 2,040,000.00 USD | 2,040,000.00 USD | 7,040.00 USD | 8,030.00 USD | 21,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0885` | 1,610,000.00 USD | 1,610,000.00 USD | 4,650.00 USD | 1,040.00 USD | 4,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0887` | 1,600,000.00 USD | 1,600,000.00 USD | 2,910.00 USD | 1,540.00 USD | 8,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0887` | 2,000,000.00 USD | 2,000,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0889` | 1,590,000.00 USD | 1,590,000.00 USD | 727.20 USD | 1,680.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0890` | 1,970,000.00 USD | 1,970,000.00 USD | 14,610.00 USD | 5,880.00 USD | 13,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0891` | 1,580,000.00 USD | 1,580,000.00 USD | 755.35 USD | 1,580.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0893` | 1,580,000.00 USD | 1,580,000.00 USD | 983.61 USD | 0.00 USD | 542.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0893` | 1,940,000.00 USD | 1,940,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0895` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 1,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,270.00 USD | 5,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0896` | 1,920,000.00 USD | 1,920,000.00 USD | 5,760.00 USD | 2,110.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0897` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 1,330.00 USD | 11.07 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0899` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 21.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0899` | 1,900,000.00 USD | 1,900,000.00 USD | 3,390.00 USD | 927.82 USD | 4,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0901` | 1,580,000.00 USD | 1,580,000.00 USD | 3,320.00 USD | 1,000.00 USD | 18.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0902` | 1,890,000.00 USD | 1,890,000.00 USD | 2,270.00 USD | 910.78 USD | 1,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0903` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 3,440.00 USD | 2,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0905` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 486.35 USD | 2,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0905` | 1,890,000.00 USD | 1,890,000.00 USD | 10,350.00 USD | 996.61 USD | 4,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0905` | 2,230.00 USD | 2,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0907` | 1,560,000.00 USD | 1,560,000.00 USD | 1,250.00 USD | 245.42 USD | 2,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0908` | 1,870,000.00 USD | 1,870,000.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0909` | 1,560,000.00 USD | 1,560,000.00 USD | 938.76 USD | 1,360.00 USD | 786.66 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0911` | 1,560,000.00 USD | 1,560,000.00 USD | 5,580.00 USD | 1,450.00 USD | 58.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0911` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0913` | 1,550,000.00 USD | 1,550,000.00 USD | 1,930.00 USD | 465.26 USD | 787.25 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0914` | 1,860,000.00 USD | 1,860,000.00 USD | 1,670.00 USD | 903.90 USD | 74.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0915` | 1,550,000.00 USD | 1,550,000.00 USD | 6,590.00 USD | 2,510.00 USD | 76.57 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0917` | 1,540,000.00 USD | 1,540,000.00 USD | 3,850.00 USD | 3,470.00 USD | 71.54 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0917` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0919` | 1,530,000.00 USD | 1,530,000.00 USD | 4,980.00 USD | 504.78 USD | 19,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0920` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 223.39 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0921` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 750.63 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0923` | 1,500,000.00 USD | 1,500,000.00 USD | 1,410.00 USD | 1,920.00 USD | 25,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0923` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 4,940.00 USD | 43,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0925` | 1,470,000.00 USD | 1,470,000.00 USD | 3,270.00 USD | 3,340.00 USD | 26,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0926` | 1,800,000.00 USD | 1,800,000.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0929` | 1,440,000.00 USD | 1,440,000.00 USD | 4,360.00 USD | 1,190.00 USD | 16.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0929` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0931` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 7,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0932` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 12,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0933` | 1,420,000.00 USD | 1,420,000.00 USD | 16,500.00 USD | 0.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0935` | 1,400,000.00 USD | 1,400,000.00 USD | 8,990.00 USD | 7,300.00 USD | 15,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0935` | 1,770,000.00 USD | 1,770,000.00 USD | 19,560.00 USD | 8,160.00 USD | 31,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0937` | 1,370,000.00 USD | 1,370,000.00 USD | 4,580.00 USD | 6,660.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0938` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 248.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0939` | 1,340,000.00 USD | 1,340,000.00 USD | 3,590.00 USD | 2,140.00 USD | 44,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0941` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 9,410.00 USD | 21,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0941` | 1,710,000.00 USD | 1,710,000.00 USD | 16,100.00 USD | 18,340.00 USD | 90,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0943` | 1,260,000.00 USD | 1,260,000.00 USD | 3,500.00 USD | 10,920.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0944` | 1,590,000.00 USD | 1,590,000.00 USD | 8,040.00 USD | 2,010.00 USD | 37,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0945` | 1,220,000.00 USD | 1,220,000.00 USD | 15,750.00 USD | 6,510.00 USD | 44,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0947` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 962.66 USD | 91.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0947` | 1,540,000.00 USD | 1,540,000.00 USD | 2,200.00 USD | 1,810.00 USD | 177.04 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0949` | 1,150,000.00 USD | 1,150,000.00 USD | 12,180.00 USD | 5,770.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0950` | 1,540,000.00 USD | 1,540,000.00 USD | 3,770.00 USD | 9,700.00 USD | 27,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0951` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 2,030.00 USD | 19,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0953` | 1,110,000.00 USD | 1,110,000.00 USD | 33,000.00 USD | 4,360.00 USD | 6,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0953` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 8,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0955` | 1,060,000.00 USD | 1,060,000.00 USD | 17,990.00 USD | 14,600.00 USD | 31,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0956` | 1,490,000.00 USD | 1,490,000.00 USD | 39,120.00 USD | 13,670.00 USD | 51,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0957` | 997,030.00 USD | 997,030.00 USD | 16,340.00 USD | 6,740.00 USD | 48,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0959` | 925,260.00 USD | 925,260.00 USD | 0.00 USD | 3,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0959` | 1,380,000.00 USD | 1,380,000.00 USD | 28,110.00 USD | 0.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0961` | 922,160.00 USD | 922,160.00 USD | 8,920.00 USD | 23,950.00 USD | 23,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0962` | 1,340,000.00 USD | 1,340,000.00 USD | 12,340.00 USD | 16,920.00 USD | 95,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0963` | 865,990.00 USD | 865,990.00 USD | 23,240.00 USD | 11,750.00 USD | 11,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0965` | 819,020.00 USD | 819,020.00 USD | 8,250.00 USD | 5,890.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0965` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 6,410.00 USD | 86.68 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0967` | 784,440.00 USD | 784,440.00 USD | 0.00 USD | 1,960.00 USD | 818.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0968` | 1,200,000.00 USD | 1,200,000.00 USD | 7,490.00 USD | 0.00 USD | 59,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0969` | 781,660.00 USD | 781,660.00 USD | 6,930.00 USD | 7,530.00 USD | 8,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0971` | 759,120.00 USD | 759,120.00 USD | 2,840.00 USD | 4,070.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 7,090.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0973` | 741,970.00 USD | 741,970.00 USD | 1,440.00 USD | 10,220.00 USD | 1,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0974` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 16,310.00 USD | 104.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0975` | 728,320.00 USD | 728,320.00 USD | 0.00 USD | 0.00 USD | 56.06 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0977` | 728,270.00 USD | 728,270.00 USD | 0.00 USD | 765.93 USD | 911.50 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0979` | 726,590.00 USD | 726,590.00 USD | 0.00 USD | 817.22 USD | 21,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0981` | 704,660.00 USD | 704,660.00 USD | 3,830.00 USD | 5,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0983` | 695,810.00 USD | 695,810.00 USD | 1,640.00 USD | 4,970.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 11,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0985` | 685,390.00 USD | 685,390.00 USD | 1,670.00 USD | 913.91 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0986` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 12,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0987` | 678,370.00 USD | 678,370.00 USD | 21,530.00 USD | 3,920.00 USD | 11,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0989` | 641,120.00 USD | 641,120.00 USD | 2,180.00 USD | 1,540.00 USD | 21,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 1,090,000.00 USD | 1,090,000.00 USD | 17,640.00 USD | 7,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0991` | 615,680.00 USD | 615,680.00 USD | 69,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0992` | 1,060,000.00 USD | 1,060,000.00 USD | 27,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0993` | 545,740.00 USD | 545,740.00 USD | 23,960.00 USD | 3,020.00 USD | 45,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0995` | 473,400.00 USD | 473,400.00 USD | 17,890.00 USD | 898.20 USD | 50,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 1,030,000.00 USD | 1,030,000.00 USD | 63,330.00 USD | 0.00 USD | 76,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0997` | 404,360.00 USD | 404,360.00 USD | 17,900.00 USD | 7,370.00 USD | 55,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0998` | 893,820.00 USD | 893,820.00 USD | 28,450.00 USD | 17,040.00 USD | 135,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0999` | 323,590.00 USD | 323,590.00 USD | 0.00 USD | 11,820.00 USD | 47,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1001` | 263,870.00 USD | 263,870.00 USD | 0.00 USD | 0.00 USD | 42,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 713,060.00 USD | 713,060.00 USD | 76,560.00 USD | 25,570.00 USD | 107,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1003` | 221,360.00 USD | 221,360.00 USD | 26,520.00 USD | 0.00 USD | 27,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1004` | 502,950.00 USD | 502,950.00 USD | 22,470.00 USD | 0.00 USD | 46,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1005` | 167,640.00 USD | 167,640.00 USD | 11,590.00 USD | 9,580.00 USD | 36,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1007` | 109,590.00 USD | 109,590.00 USD | 4,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 434,350.00 USD | 434,350.00 USD | 20,870.00 USD | 3,080.00 USD | 100,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1009` | 105,240.00 USD | 105,240.00 USD | 6,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1010` | 310,170.00 USD | 310,170.00 USD | 17,340.00 USD | 13,670.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1011` | 98,310.00 USD | 98,310.00 USD | 0.00 USD | 4,070.00 USD | 15,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1013` | 78,500.00 USD | 78,500.00 USD | 0.00 USD | 0.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 225,130.00 USD | 225,130.00 USD | 34,830.00 USD | 28,370.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1015` | 68,000.00 USD | 68,000.00 USD | 4,580.00 USD | 1,220.00 USD | 13,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1016` | 136,470.00 USD | 136,470.00 USD | 15,440.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1017` | 48,970.00 USD | 48,970.00 USD | 3,590.00 USD | 0.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1019` | 34,270.00 USD | 34,270.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1019` | 121,030.00 USD | 121,030.00 USD | 26,150.00 USD | 8,460.00 USD | 20,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1021` | 32,720.00 USD | 32,720.00 USD | 13,630.00 USD | 5,210.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1022` | 65,810.00 USD | 65,810.00 USD | 18,100.00 USD | 10,260.00 USD | 37,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1023` | 14,190.00 USD | 14,190.00 USD | 0.00 USD | 10,470.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1023` | 28,380.00 USD | 28,380.00 USD | 0.00 USD | 10,470.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1025` | 6,340.00 USD | 6,340.00 USD | 1,550.00 USD | 4,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1027` | 40,550.00 USD | 40,550.00 USD | 3,430.00 USD | 0.00 USD | 8,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1028` | 38,230.00 USD | 38,230.00 USD | 3,800.00 USD | 4,390.00 USD | 23,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1029` | 62,300.00 USD | 62,300.00 USD | 6,870.00 USD | 7,400.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1031` | 125,520.00 USD | 125,520.00 USD | 33,590.00 USD | 5,770.00 USD | 23,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1031` | 67,590.00 USD | 67,590.00 USD | 19,560.00 USD | 9,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1033` | 164,820.00 USD | 164,820.00 USD | 2,890.00 USD | 10,740.00 USD | 25,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1034` | 101,690.00 USD | 101,690.00 USD | 18,920.00 USD | 15,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1035` | 191,120.00 USD | 191,120.00 USD | 15,150.00 USD | 11,130.00 USD | 17.34 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1037` | 243,740.00 USD | 243,740.00 USD | 36,550.00 USD | 14,230.00 USD | 1,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1037` | 115,220.00 USD | 115,220.00 USD | 2,710.00 USD | 10,710.00 USD | 108.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1039` | 265,590.00 USD | 265,590.00 USD | 6,500.00 USD | 10,140.00 USD | 5,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1040` | 162,820.00 USD | 162,820.00 USD | 5,940.00 USD | 10,300.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1041` | 313,600.00 USD | 313,600.00 USD | 11,520.00 USD | 16,860.00 USD | 19,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1043` | 351,020.00 USD | 351,020.00 USD | 3,280.00 USD | 9,960.00 USD | 24,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1043` | 207,470.00 USD | 207,470.00 USD | 15,960.00 USD | 5,980.00 USD | 22,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1045` | 369,550.00 USD | 369,550.00 USD | 1,870.00 USD | 4,110.00 USD | 12,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1046` | 279,830.00 USD | 279,830.00 USD | 0.00 USD | 12,200.00 USD | 60,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1047` | 457,400.00 USD | 457,400.00 USD | 31,910.00 USD | 9,830.00 USD | 46,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1049` | 575,200.00 USD | 575,200.00 USD | 33,450.00 USD | 15,310.00 USD | 69,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1049` | 404,330.00 USD | 404,330.00 USD | 34,790.00 USD | 6,530.00 USD | 83,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1051` | 640,150.00 USD | 640,150.00 USD | 30,440.00 USD | 10,280.00 USD | 24,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1052` | 582,170.00 USD | 582,170.00 USD | 28,200.00 USD | 24,160.00 USD | 125,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1053` | 739,670.00 USD | 739,670.00 USD | 33,460.00 USD | 12,130.00 USD | 53,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1055` | 875,080.00 USD | 875,080.00 USD | 51,530.00 USD | 26,280.00 USD | 57,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1055` | 961,070.00 USD | 961,070.00 USD | 122,840.00 USD | 44,430.00 USD | 211,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1057` | 930,170.00 USD | 930,170.00 USD | 14,080.00 USD | 11,900.00 USD | 29,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1058` | 1,330,000.00 USD | 1,330,000.00 USD | 105,620.00 USD | 58,510.00 USD | 202,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1059` | 1,050,000.00 USD | 1,050,000.00 USD | 35,730.00 USD | 5,730.00 USD | 77,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1061` | 1,140,000.00 USD | 1,140,000.00 USD | 30,060.00 USD | 2,700.00 USD | 60,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1061` | 1,590,000.00 USD | 1,590,000.00 USD | 75,540.00 USD | 69,160.00 USD | 118,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1063` | 1,240,000.00 USD | 1,240,000.00 USD | 25,200.00 USD | 2,030.00 USD | 65,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1064` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 52,580.00 USD | 188,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1065` | 1,270,000.00 USD | 1,270,000.00 USD | 3,380.00 USD | 3,560.00 USD | 28,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1067` | 1,330,000.00 USD | 1,330,000.00 USD | 9,900.00 USD | 2,240.00 USD | 48,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1067` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 51,740.00 USD | 144,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1069` | 1,410,000.00 USD | 1,410,000.00 USD | 14,770.00 USD | 5,440.00 USD | 62,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1070` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 57,770.00 USD | 134,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1071` | 1,440,000.00 USD | 1,440,000.00 USD | 2,550.00 USD | 5,850.00 USD | 20,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1073` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1073` | 2,260,000.00 USD | 2,260,000.00 USD | 7,820.00 USD | 20,440.00 USD | 10,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1075` | 1,450,000.00 USD | 1,450,000.00 USD | 1,440.00 USD | 857.82 USD | 3,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1076` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 22,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1077` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 619.42 USD | 133.34 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1079` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 4,300.00 USD | 21,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1079` | 2,300,000.00 USD | 2,300,000.00 USD | 5,620.00 USD | 3,380.00 USD | 10,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1081` | 1,490,000.00 USD | 1,490,000.00 USD | 4,650.00 USD | 732.74 USD | 2,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1082` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 154.22 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1083` | 1,520,000.00 USD | 1,520,000.00 USD | 9,160.00 USD | 6,710.00 USD | 10,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1085` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 385.06 USD | 65,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1085` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1087` | 1,660,000.00 USD | 1,660,000.00 USD | 28,490.00 USD | 2,510.00 USD | 44,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1088` | 2,320,000.00 USD | 2,320,000.00 USD | 5,290.00 USD | 1,420.00 USD | 9,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1089` | 1,690,000.00 USD | 1,690,000.00 USD | 29,650.00 USD | 1,580.00 USD | 3,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1091` | 1,720,000.00 USD | 1,720,000.00 USD | 33,700.00 USD | 0.00 USD | 16.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1091` | 2,340,000.00 USD | 2,340,000.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1093` | 1,740,000.00 USD | 1,740,000.00 USD | 15,480.00 USD | 1,080.00 USD | 269.69 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1094` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 1,500.00 USD | 8,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1095` | 1,770,000.00 USD | 1,770,000.00 USD | 4,110.00 USD | 1,890.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1097` | 1,800,000.00 USD | 1,800,000.00 USD | 7,260.00 USD | 2,530.00 USD | 22,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1097` | 2,370,000.00 USD | 2,370,000.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1099` | 1,810,000.00 USD | 1,810,000.00 USD | 6,130.00 USD | 1,940.00 USD | 5.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1100` | 2,400,000.00 USD | 2,400,000.00 USD | 11,470.00 USD | 0.00 USD | 21,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1101` | 1,820,000.00 USD | 1,820,000.00 USD | 5,570.00 USD | 3,820.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1103` | 1,830,000.00 USD | 1,830,000.00 USD | 3,540.00 USD | 6,900.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 2,450,000.00 USD | 2,450,000.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1105` | 1,850,000.00 USD | 1,850,000.00 USD | 3,380.00 USD | 4,740.00 USD | 10,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1106` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 22,880.00 USD | 16,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1107` | 1,910,000.00 USD | 1,910,000.00 USD | 3,110.00 USD | 13,200.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1109` | 1,910,000.00 USD | 1,910,000.00 USD | 2,110.00 USD | 1,370.00 USD | 2,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1111` | 1,920,000.00 USD | 1,920,000.00 USD | 5,200.00 USD | 996.46 USD | 104.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1112` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1113` | 1,980,000.00 USD | 1,980,000.00 USD | 21,390.00 USD | 5,880.00 USD | 29,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1115` | 1,980,000.00 USD | 1,980,000.00 USD | 6,690.00 USD | 465.26 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1115` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 28.89 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1117` | 2,040,000.00 USD | 2,040,000.00 USD | 2,060.00 USD | 23,600.00 USD | 34,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1118` | 2,590,000.00 USD | 2,590,000.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1119` | 2,120,000.00 USD | 2,120,000.00 USD | 33,110.00 USD | 8,660.00 USD | 32,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1121` | 2,160,000.00 USD | 2,160,000.00 USD | 21,300.00 USD | 12,810.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 2,650,000.00 USD | 2,650,000.00 USD | 17,760.00 USD | 0.00 USD | 38,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1123` | 2,200,000.00 USD | 2,200,000.00 USD | 28,130.00 USD | 2,290.00 USD | 8,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1124` | 2,750,000.00 USD | 2,750,000.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1125` | 2,240,000.00 USD | 2,240,000.00 USD | 11,130.00 USD | 13,270.00 USD | 11,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1127` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 1,250.00 USD | 21,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1127` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1129` | 2,280,000.00 USD | 2,280,000.00 USD | 10,120.00 USD | 0.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1130` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 24,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1131` | 2,330,000.00 USD | 2,330,000.00 USD | 20,830.00 USD | 5,570.00 USD | 22,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1133` | 2,370,000.00 USD | 2,370,000.00 USD | 6,530.00 USD | 17,080.00 USD | 23,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 2,830,000.00 USD | 2,830,000.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1135` | 2,380,000.00 USD | 2,380,000.00 USD | 4,040.00 USD | 3,670.00 USD | 4,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1136` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 40.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1136` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1139` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1142` | 2,870,000.00 USD | 2,870,000.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 3,110,000.00 USD | 3,110,000.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1148` | 3,290,000.00 USD | 3,290,000.00 USD | 9,880.00 USD | 0.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 3,560,000.00 USD | 3,560,000.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1154` | 4,040,000.00 USD | 4,040,000.00 USD | 243,190.00 USD | 26,970.00 USD | 202,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 4,330,000.00 USD | 4,330,000.00 USD | 173,120.00 USD | 25,290.00 USD | 98,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1160` | 4,610,000.00 USD | 4,610,000.00 USD | 131,160.00 USD | 32,830.00 USD | 109,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 4,890,000.00 USD | 4,890,000.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1166` | 5,110,000.00 USD | 5,110,000.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 5,330,000.00 USD | 5,330,000.00 USD | 82,770.00 USD | 26,150.00 USD | 117,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1172` | 5,460,000.00 USD | 5,460,000.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 5,640,000.00 USD | 5,640,000.00 USD | 75,590.00 USD | 17,930.00 USD | 81,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1178` | 5,810,000.00 USD | 5,810,000.00 USD | 89,510.00 USD | 25,350.00 USD | 60,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 5,900,000.00 USD | 5,900,000.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1184` | 5,960,000.00 USD | 5,960,000.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 6,050,000.00 USD | 6,050,000.00 USD | 5,620.00 USD | 17,120.00 USD | 59,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1190` | 6,190,000.00 USD | 6,190,000.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 6,270,000.00 USD | 6,270,000.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1196` | 6,330,000.00 USD | 6,330,000.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 6,400,000.00 USD | 6,400,000.00 USD | 2,470.00 USD | 13,190.00 USD | 52,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1202` | 6,590,000.00 USD | 6,590,000.00 USD | 131,660.00 USD | 21,430.00 USD | 32,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 6,790,000.00 USD | 6,790,000.00 USD | 117,120.00 USD | 48,510.00 USD | 40,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1205` | 3,590.00 USD | 3,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1208` | 6,890,000.00 USD | 6,890,000.00 USD | 39,480.00 USD | 20,870.00 USD | 39,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 7,070,000.00 USD | 7,070,000.00 USD | 72,500.00 USD | 25,920.00 USD | 76,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1214` | 7,190,000.00 USD | 7,190,000.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 7,240,000.00 USD | 7,240,000.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1220` | 7,330,000.00 USD | 7,330,000.00 USD | 34,050.00 USD | 6,400.00 USD | 54,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 7,460,000.00 USD | 7,460,000.00 USD | 73,610.00 USD | 15,050.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 721.08 USD | 4,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1226` | 7,530,000.00 USD | 7,530,000.00 USD | 42,530.00 USD | 19,760.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 7,650,000.00 USD | 7,650,000.00 USD | 63,930.00 USD | 33,570.00 USD | 28,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1232` | 7,750,000.00 USD | 7,750,000.00 USD | 51,420.00 USD | 12,080.00 USD | 37,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1235` | 7,790,000.00 USD | 7,790,000.00 USD | 15,040.00 USD | 5,390.00 USD | 16,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1237` | 7,800,000.00 USD | 7,800,000.00 USD | 4,080.00 USD | 2,760.00 USD | 2,800.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.0827` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 8,590.00 USD |
| `7D` | `0.0830` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 28.49 USD |
| `7D` | `0.0860` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 1,880.00 USD | 0.00 USD | 2,160.00 USD |
| `7D` | `0.0863` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 0.00 USD | 1,880.00 USD | 7,040.00 USD |
| `7D` | `0.0866` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 0.00 USD | 1,980.00 USD | 15,400.00 USD |
| `1D` | `0.0869` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 2,790.00 USD | 0.00 USD | 50.76 USD |
| `7D` | `0.0869` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 2,900.00 USD |
| `1D` | `0.0871` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 1,740.00 USD | 0.00 USD | 997.60 USD |
| `7D` | `0.0872` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 0.00 USD | 1,200.00 USD | 5,830.00 USD |
| `1D` | `0.0873` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 0.00 USD | 680.22 USD | 5,950.00 USD |
| `1D` | `0.0875` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 9,010.00 USD | 437.13 USD | 3,520.00 USD |
| `7D` | `0.0875` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 6,010.00 USD | 0.00 USD | 5,780.00 USD |
| `1D` | `0.0877` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 4,110.00 USD | 3,520.00 USD | 5,410.00 USD |
| `7D` | `0.0878` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 9,200.00 USD | 7,660.00 USD | 28,720.00 USD |
| `1D` | `0.0879` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 2,340.00 USD | 2,000.00 USD | 9,430.00 USD |
| `1D` | `0.0881` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 1,670.00 USD | 1,700.00 USD | 530.96 USD |
| `7D` | `0.0881` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 9,390.00 USD | 2,660.00 USD | 12,940.00 USD |
| `1D` | `0.0883` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 2,370.00 USD | 4,960.00 USD | 9,970.00 USD |
| `7D` | `0.0884` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 7,040.00 USD | 8,030.00 USD | 21,730.00 USD |
| `1D` | `0.0885` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 4,650.00 USD | 1,040.00 USD | 4,920.00 USD |
| `1D` | `0.0887` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 2,910.00 USD | 1,540.00 USD | 8,120.00 USD |
| `7D` | `0.0887` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD |
| `1D` | `0.0889` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 727.20 USD | 1,680.00 USD | 2,110.00 USD |
| `7D` | `0.0890` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 14,610.00 USD | 5,880.00 USD | 13,160.00 USD |
| `1D` | `0.0891` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 755.35 USD | 1,580.00 USD | 3,210.00 USD |
| `1D` | `0.0893` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 983.61 USD | 0.00 USD | 542.23 USD |
| `7D` | `0.0893` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD |
| `1D` | `0.0895` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 0.00 USD | 1,080.00 USD | 0.00 USD |
| `7D` | `0.0896` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 5,760.00 USD | 2,110.00 USD | 6,870.00 USD |
| `1D` | `0.0897` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 0.00 USD | 1,330.00 USD | 11.07 USD |
| `1D` | `0.0899` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 21.52 USD |
| `7D` | `0.0899` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 3,390.00 USD | 927.82 USD | 4,520.00 USD |
| `1D` | `0.0901` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 3,320.00 USD | 1,000.00 USD | 18.94 USD |
| `7D` | `0.0902` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 2,270.00 USD | 910.78 USD | 1,320.00 USD |
| `1D` | `0.0903` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 0.00 USD | 3,440.00 USD | 2,230.00 USD |
| `1D` | `0.0905` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 0.00 USD | 486.35 USD | 2,150.00 USD |
| `7D` | `0.0905` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 10,350.00 USD | 996.61 USD | 4,170.00 USD |
| `1D` | `0.0907` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 1,250.00 USD | 245.42 USD | 2,710.00 USD |
| `7D` | `0.0908` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD |
| `1D` | `0.0909` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 938.76 USD | 1,360.00 USD | 786.66 USD |
| `1D` | `0.0911` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 5,580.00 USD | 1,450.00 USD | 58.17 USD |
| `7D` | `0.0911` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD |
| `1D` | `0.0913` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 1,930.00 USD | 465.26 USD | 787.25 USD |
| `7D` | `0.0914` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 1,670.00 USD | 903.90 USD | 74.70 USD |
| `1D` | `0.0915` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 6,590.00 USD | 2,510.00 USD | 76.57 USD |
| `1D` | `0.0917` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 3,850.00 USD | 3,470.00 USD | 71.54 USD |
| `7D` | `0.0917` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 8,050.00 USD |
| `1D` | `0.0919` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 4,980.00 USD | 504.78 USD | 19,100.00 USD |
| `7D` | `0.0920` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 223.39 USD |
| `1D` | `0.0921` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 0.00 USD | 750.63 USD | 3,810.00 USD |
| `1D` | `0.0923` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 1,410.00 USD | 1,920.00 USD | 25,420.00 USD |
| `7D` | `0.0923` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 0.00 USD | 4,940.00 USD | 43,900.00 USD |
| `1D` | `0.0925` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 3,270.00 USD | 3,340.00 USD | 26,400.00 USD |
| `7D` | `0.0926` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD |
| `1D` | `0.0929` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 4,360.00 USD | 1,190.00 USD | 16.60 USD |
| `7D` | `0.0929` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD |
| `1D` | `0.0931` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 7,430.00 USD |
| `7D` | `0.0932` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 12,290.00 USD |
| `1D` | `0.0933` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 16,500.00 USD | 0.00 USD | 10,200.00 USD |
| `1D` | `0.0935` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 8,990.00 USD | 7,300.00 USD | 15,690.00 USD |
| `7D` | `0.0935` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 19,560.00 USD | 8,160.00 USD | 31,940.00 USD |
| `1D` | `0.0937` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 4,580.00 USD | 6,660.00 USD | 13,310.00 USD |
| `7D` | `0.0938` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 248.29 USD |
| `1D` | `0.0939` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 3,590.00 USD | 2,140.00 USD | 44,370.00 USD |
| `1D` | `0.0941` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 0.00 USD | 9,410.00 USD | 21,110.00 USD |
| `7D` | `0.0941` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 16,100.00 USD | 18,340.00 USD | 90,220.00 USD |
| `1D` | `0.0943` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 3,500.00 USD | 10,920.00 USD | 30,420.00 USD |
| `7D` | `0.0944` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 8,040.00 USD | 2,010.00 USD | 37,540.00 USD |
| `1D` | `0.0945` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 15,750.00 USD | 6,510.00 USD | 44,380.00 USD |
| `1D` | `0.0947` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 0.00 USD | 962.66 USD | 91.75 USD |
| `7D` | `0.0947` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 2,200.00 USD | 1,810.00 USD | 177.04 USD |
| `1D` | `0.0949` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 12,180.00 USD | 5,770.00 USD | 2,940.00 USD |
| `7D` | `0.0950` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 3,770.00 USD | 9,700.00 USD | 27,060.00 USD |
| `1D` | `0.0951` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 0.00 USD | 2,030.00 USD | 19,990.00 USD |
| `1D` | `0.0953` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 33,000.00 USD | 4,360.00 USD | 6,780.00 USD |
| `7D` | `0.0953` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 0.00 USD | 8,150.00 USD | 0.00 USD |
| `1D` | `0.0955` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 17,990.00 USD | 14,600.00 USD | 31,680.00 USD |
| `7D` | `0.0956` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 39,120.00 USD | 13,670.00 USD | 51,170.00 USD |
| `1D` | `0.0957` | 997,030.00 USD | 0.00 USD | 997,030.00 USD | 16,340.00 USD | 6,740.00 USD | 48,700.00 USD |
| `1D` | `0.0959` | 925,260.00 USD | 0.00 USD | 925,260.00 USD | 0.00 USD | 3,100.00 USD | 0.00 USD |
| `7D` | `0.0959` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 28,110.00 USD | 0.00 USD | 21,370.00 USD |
| `1D` | `0.0961` | 922,160.00 USD | 0.00 USD | 922,160.00 USD | 8,920.00 USD | 23,950.00 USD | 23,300.00 USD |
| `7D` | `0.0962` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 12,340.00 USD | 16,920.00 USD | 95,050.00 USD |
| `1D` | `0.0963` | 865,990.00 USD | 0.00 USD | 865,990.00 USD | 23,240.00 USD | 11,750.00 USD | 11,980.00 USD |
| `1D` | `0.0965` | 819,020.00 USD | 0.00 USD | 819,020.00 USD | 8,250.00 USD | 5,890.00 USD | 20,440.00 USD |
| `7D` | `0.0965` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 0.00 USD | 6,410.00 USD | 86.68 USD |
| `1D` | `0.0967` | 784,440.00 USD | 0.00 USD | 784,440.00 USD | 0.00 USD | 1,960.00 USD | 818.32 USD |
| `7D` | `0.0968` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 7,490.00 USD | 0.00 USD | 59,000.00 USD |
| `1D` | `0.0969` | 781,660.00 USD | 0.00 USD | 781,660.00 USD | 6,930.00 USD | 7,530.00 USD | 8,080.00 USD |
| `1D` | `0.0971` | 759,120.00 USD | 0.00 USD | 759,120.00 USD | 2,840.00 USD | 4,070.00 USD | 10,240.00 USD |
| `7D` | `0.0971` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 7,090.00 USD | 5,010.00 USD |
| `1D` | `0.0973` | 741,970.00 USD | 0.00 USD | 741,970.00 USD | 1,440.00 USD | 10,220.00 USD | 1,970.00 USD |
| `7D` | `0.0974` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 0.00 USD | 16,310.00 USD | 104.80 USD |
| `1D` | `0.0975` | 728,320.00 USD | 0.00 USD | 728,320.00 USD | 0.00 USD | 0.00 USD | 56.06 USD |
| `1D` | `0.0977` | 728,270.00 USD | 0.00 USD | 728,270.00 USD | 0.00 USD | 765.93 USD | 911.50 USD |
| `1D` | `0.0979` | 726,590.00 USD | 0.00 USD | 726,590.00 USD | 0.00 USD | 817.22 USD | 21,110.00 USD |
| `1D` | `0.0981` | 704,660.00 USD | 0.00 USD | 704,660.00 USD | 3,830.00 USD | 5,020.00 USD | 0.00 USD |
| `1D` | `0.0983` | 695,810.00 USD | 0.00 USD | 695,810.00 USD | 1,640.00 USD | 4,970.00 USD | 3,810.00 USD |
| `7D` | `0.0983` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 11,350.00 USD |
| `1D` | `0.0985` | 685,390.00 USD | 0.00 USD | 685,390.00 USD | 1,670.00 USD | 913.91 USD | 4,440.00 USD |
| `7D` | `0.0986` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 0.00 USD | 12,320.00 USD | 0.00 USD |
| `1D` | `0.0987` | 678,370.00 USD | 0.00 USD | 678,370.00 USD | 21,530.00 USD | 3,920.00 USD | 11,800.00 USD |
| `1D` | `0.0989` | 641,120.00 USD | 0.00 USD | 641,120.00 USD | 2,180.00 USD | 1,540.00 USD | 21,720.00 USD |
| `7D` | `0.0989` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 17,640.00 USD | 7,820.00 USD | 0.00 USD |
| `1D` | `0.0991` | 615,680.00 USD | 0.00 USD | 615,680.00 USD | 69,940.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0992` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 27,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0993` | 545,740.00 USD | 0.00 USD | 545,740.00 USD | 23,960.00 USD | 3,020.00 USD | 45,360.00 USD |
| `1D` | `0.0995` | 473,400.00 USD | 0.00 USD | 473,400.00 USD | 17,890.00 USD | 898.20 USD | 50,250.00 USD |
| `7D` | `0.0995` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 63,330.00 USD | 0.00 USD | 76,030.00 USD |
| `1D` | `0.0997` | 404,360.00 USD | 0.00 USD | 404,360.00 USD | 17,900.00 USD | 7,370.00 USD | 55,500.00 USD |
| `7D` | `0.0998` | 893,820.00 USD | 0.00 USD | 893,820.00 USD | 28,450.00 USD | 17,040.00 USD | 135,270.00 USD |
| `1D` | `0.0999` | 323,590.00 USD | 0.00 USD | 323,590.00 USD | 0.00 USD | 11,820.00 USD | 47,900.00 USD |
| `1D` | `0.1001` | 263,870.00 USD | 0.00 USD | 263,870.00 USD | 0.00 USD | 0.00 USD | 42,510.00 USD |
| `7D` | `0.1001` | 713,060.00 USD | 0.00 USD | 713,060.00 USD | 76,560.00 USD | 25,570.00 USD | 107,970.00 USD |
| `1D` | `0.1003` | 221,360.00 USD | 0.00 USD | 221,360.00 USD | 26,520.00 USD | 0.00 USD | 27,200.00 USD |
| `7D` | `0.1004` | 502,950.00 USD | 0.00 USD | 502,950.00 USD | 22,470.00 USD | 0.00 USD | 46,130.00 USD |
| `1D` | `0.1005` | 167,640.00 USD | 0.00 USD | 167,640.00 USD | 11,590.00 USD | 9,580.00 USD | 36,880.00 USD |
| `1D` | `0.1007` | 109,590.00 USD | 0.00 USD | 109,590.00 USD | 4,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1007` | 434,350.00 USD | 0.00 USD | 434,350.00 USD | 20,870.00 USD | 3,080.00 USD | 100,230.00 USD |
| `1D` | `0.1009` | 105,240.00 USD | 0.00 USD | 105,240.00 USD | 6,930.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1010` | 310,170.00 USD | 0.00 USD | 310,170.00 USD | 17,340.00 USD | 13,670.00 USD | 54,030.00 USD |
| `1D` | `0.1011` | 98,310.00 USD | 0.00 USD | 98,310.00 USD | 0.00 USD | 4,070.00 USD | 15,740.00 USD |
| `1D` | `0.1013` | 78,500.00 USD | 0.00 USD | 78,500.00 USD | 0.00 USD | 0.00 USD | 10,500.00 USD |
| `7D` | `0.1013` | 225,130.00 USD | 0.00 USD | 225,130.00 USD | 34,830.00 USD | 28,370.00 USD | 25,450.00 USD |
| `1D` | `0.1015` | 68,000.00 USD | 0.00 USD | 68,000.00 USD | 4,580.00 USD | 1,220.00 USD | 13,220.00 USD |
| `7D` | `0.1016` | 136,470.00 USD | 0.00 USD | 136,470.00 USD | 15,440.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1017` | 48,970.00 USD | 0.00 USD | 48,970.00 USD | 3,590.00 USD | 0.00 USD | 11,110.00 USD |
| `1D` | `0.1019` | 34,270.00 USD | 0.00 USD | 34,270.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD |
| `7D` | `0.1019` | 121,030.00 USD | 0.00 USD | 121,030.00 USD | 26,150.00 USD | 8,460.00 USD | 20,610.00 USD |
| `1D` | `0.1021` | 32,720.00 USD | 0.00 USD | 32,720.00 USD | 13,630.00 USD | 5,210.00 USD | 13,880.00 USD |
| `7D` | `0.1022` | 65,810.00 USD | 0.00 USD | 65,810.00 USD | 18,100.00 USD | 10,260.00 USD | 37,440.00 USD |
| `1D` | `0.1023` | 14,190.00 USD | 14,190.00 USD | 0.00 USD | 0.00 USD | 10,470.00 USD | 3,720.00 USD |
| `1D` | `0.1023` | 28,380.00 USD | 28,380.00 USD | 0.00 USD | 0.00 USD | 10,470.00 USD | 3,720.00 USD |
| `7D` | `0.1024` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1025` | 6,340.00 USD | 6,340.00 USD | 0.00 USD | 1,550.00 USD | 4,790.00 USD | 0.00 USD |
| `1D` | `0.1027` | 40,550.00 USD | 40,550.00 USD | 0.00 USD | 3,430.00 USD | 0.00 USD | 8,740.00 USD |
| `7D` | `0.1028` | 38,230.00 USD | 38,230.00 USD | 0.00 USD | 3,800.00 USD | 4,390.00 USD | 23,700.00 USD |
| `1D` | `0.1029` | 62,300.00 USD | 62,300.00 USD | 0.00 USD | 6,870.00 USD | 7,400.00 USD | 7,480.00 USD |
| `1D` | `0.1031` | 125,520.00 USD | 125,520.00 USD | 0.00 USD | 33,590.00 USD | 5,770.00 USD | 23,860.00 USD |
| `7D` | `0.1031` | 67,590.00 USD | 67,590.00 USD | 0.00 USD | 19,560.00 USD | 9,810.00 USD | 0.00 USD |
| `1D` | `0.1033` | 164,820.00 USD | 164,820.00 USD | 0.00 USD | 2,890.00 USD | 10,740.00 USD | 25,670.00 USD |
| `7D` | `0.1034` | 101,690.00 USD | 101,690.00 USD | 0.00 USD | 18,920.00 USD | 15,180.00 USD | 0.00 USD |
| `1D` | `0.1035` | 191,120.00 USD | 191,120.00 USD | 0.00 USD | 15,150.00 USD | 11,130.00 USD | 17.34 USD |
| `1D` | `0.1037` | 243,740.00 USD | 243,740.00 USD | 0.00 USD | 36,550.00 USD | 14,230.00 USD | 1,850.00 USD |
| `7D` | `0.1037` | 115,220.00 USD | 115,220.00 USD | 0.00 USD | 2,710.00 USD | 10,710.00 USD | 108.00 USD |
| `1D` | `0.1039` | 265,590.00 USD | 265,590.00 USD | 0.00 USD | 6,500.00 USD | 10,140.00 USD | 5,220.00 USD |
| `7D` | `0.1040` | 162,820.00 USD | 162,820.00 USD | 0.00 USD | 5,940.00 USD | 10,300.00 USD | 31,350.00 USD |
| `1D` | `0.1041` | 313,600.00 USD | 313,600.00 USD | 0.00 USD | 11,520.00 USD | 16,860.00 USD | 19,630.00 USD |
| `1D` | `0.1043` | 351,020.00 USD | 351,020.00 USD | 0.00 USD | 3,280.00 USD | 9,960.00 USD | 24,170.00 USD |
| `7D` | `0.1043` | 207,470.00 USD | 207,470.00 USD | 0.00 USD | 15,960.00 USD | 5,980.00 USD | 22,700.00 USD |
| `1D` | `0.1045` | 369,550.00 USD | 369,550.00 USD | 0.00 USD | 1,870.00 USD | 4,110.00 USD | 12,560.00 USD |
| `7D` | `0.1046` | 279,830.00 USD | 279,830.00 USD | 0.00 USD | 0.00 USD | 12,200.00 USD | 60,160.00 USD |
| `1D` | `0.1047` | 457,400.00 USD | 457,400.00 USD | 0.00 USD | 31,910.00 USD | 9,830.00 USD | 46,100.00 USD |
| `1D` | `0.1049` | 575,200.00 USD | 575,200.00 USD | 0.00 USD | 33,450.00 USD | 15,310.00 USD | 69,040.00 USD |
| `7D` | `0.1049` | 404,330.00 USD | 404,330.00 USD | 0.00 USD | 34,790.00 USD | 6,530.00 USD | 83,180.00 USD |
| `1D` | `0.1051` | 640,150.00 USD | 640,150.00 USD | 0.00 USD | 30,440.00 USD | 10,280.00 USD | 24,230.00 USD |
| `7D` | `0.1052` | 582,170.00 USD | 582,170.00 USD | 0.00 USD | 28,200.00 USD | 24,160.00 USD | 125,480.00 USD |
| `1D` | `0.1053` | 739,670.00 USD | 739,670.00 USD | 0.00 USD | 33,460.00 USD | 12,130.00 USD | 53,930.00 USD |
| `1D` | `0.1055` | 875,080.00 USD | 875,080.00 USD | 0.00 USD | 51,530.00 USD | 26,280.00 USD | 57,600.00 USD |
| `7D` | `0.1055` | 961,070.00 USD | 961,070.00 USD | 0.00 USD | 122,840.00 USD | 44,430.00 USD | 211,630.00 USD |
| `1D` | `0.1057` | 930,170.00 USD | 930,170.00 USD | 0.00 USD | 14,080.00 USD | 11,900.00 USD | 29,110.00 USD |
| `7D` | `0.1058` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 105,620.00 USD | 58,510.00 USD | 202,430.00 USD |
| `1D` | `0.1059` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 35,730.00 USD | 5,730.00 USD | 77,930.00 USD |
| `1D` | `0.1061` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 30,060.00 USD | 2,700.00 USD | 60,440.00 USD |
| `7D` | `0.1061` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 75,540.00 USD | 69,160.00 USD | 118,420.00 USD |
| `1D` | `0.1063` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 25,200.00 USD | 2,030.00 USD | 65,380.00 USD |
| `7D` | `0.1064` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 52,580.00 USD | 188,900.00 USD |
| `1D` | `0.1065` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 3,380.00 USD | 3,560.00 USD | 28,490.00 USD |
| `1D` | `0.1067` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 9,900.00 USD | 2,240.00 USD | 48,650.00 USD |
| `7D` | `0.1067` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 51,740.00 USD | 144,020.00 USD |
| `1D` | `0.1069` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 14,770.00 USD | 5,440.00 USD | 62,860.00 USD |
| `7D` | `0.1070` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 57,770.00 USD | 134,760.00 USD |
| `1D` | `0.1071` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 2,550.00 USD | 5,850.00 USD | 20,430.00 USD |
| `1D` | `0.1073` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,200.00 USD |
| `7D` | `0.1073` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 7,820.00 USD | 20,440.00 USD | 10,320.00 USD |
| `1D` | `0.1075` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 1,440.00 USD | 857.82 USD | 3,840.00 USD |
| `7D` | `0.1076` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,600.00 USD |
| `1D` | `0.1077` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 619.42 USD | 133.34 USD |
| `1D` | `0.1079` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 4,300.00 USD | 21,870.00 USD |
| `7D` | `0.1079` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 5,620.00 USD | 3,380.00 USD | 10,010.00 USD |
| `1D` | `0.1081` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 4,650.00 USD | 732.74 USD | 2,420.00 USD |
| `7D` | `0.1082` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 154.22 USD |
| `1D` | `0.1083` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 9,160.00 USD | 6,710.00 USD | 10,770.00 USD |
| `1D` | `0.1085` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 385.06 USD | 65,050.00 USD |
| `7D` | `0.1085` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1087` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 28,490.00 USD | 2,510.00 USD | 44,700.00 USD |
| `7D` | `0.1088` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 5,290.00 USD | 1,420.00 USD | 9,660.00 USD |
| `1D` | `0.1089` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 29,650.00 USD | 1,580.00 USD | 3,310.00 USD |
| `1D` | `0.1091` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 33,700.00 USD | 0.00 USD | 16.51 USD |
| `7D` | `0.1091` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD |
| `1D` | `0.1093` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 15,480.00 USD | 1,080.00 USD | 269.69 USD |
| `7D` | `0.1094` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 1,500.00 USD | 8,810.00 USD |
| `1D` | `0.1095` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 21,560.00 USD |
| `1D` | `0.1097` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 7,260.00 USD | 2,530.00 USD | 22,800.00 USD |
| `7D` | `0.1097` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1099` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 6,130.00 USD | 1,940.00 USD | 5.91 USD |
| `7D` | `0.1100` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 21,880.00 USD |
| `1D` | `0.1101` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 5,570.00 USD | 3,820.00 USD | 4,290.00 USD |
| `1D` | `0.1103` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 3,540.00 USD | 6,900.00 USD | 1,160.00 USD |
| `7D` | `0.1103` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1105` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 3,380.00 USD | 4,740.00 USD | 10,710.00 USD |
| `7D` | `0.1106` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 22,880.00 USD | 16,130.00 USD |
| `1D` | `0.1107` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 3,110.00 USD | 13,200.00 USD | 35,750.00 USD |
| `1D` | `0.1109` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 2,110.00 USD | 1,370.00 USD | 2,670.00 USD |
| `7D` | `0.1109` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD |
| `1D` | `0.1111` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 5,200.00 USD | 996.46 USD | 104.00 USD |
| `7D` | `0.1112` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD |
| `1D` | `0.1113` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 21,390.00 USD | 5,880.00 USD | 29,990.00 USD |
| `1D` | `0.1115` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 6,690.00 USD | 465.26 USD | 0.00 USD |
| `7D` | `0.1115` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28.89 USD |
| `1D` | `0.1117` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 2,060.00 USD | 23,600.00 USD | 34,770.00 USD |
| `7D` | `0.1118` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD |
| `1D` | `0.1119` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 33,110.00 USD | 8,660.00 USD | 32,490.00 USD |
| `1D` | `0.1121` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 21,300.00 USD | 12,810.00 USD | 12,350.00 USD |
| `7D` | `0.1121` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 17,760.00 USD | 0.00 USD | 38,410.00 USD |
| `1D` | `0.1123` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 28,130.00 USD | 2,290.00 USD | 8,450.00 USD |
| `7D` | `0.1124` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD |
| `1D` | `0.1125` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 11,130.00 USD | 13,270.00 USD | 11,760.00 USD |
| `1D` | `0.1127` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 1,250.00 USD | 21,050.00 USD |
| `7D` | `0.1127` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD |
| `1D` | `0.1129` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 10,120.00 USD | 0.00 USD | 5,010.00 USD |
| `7D` | `0.1130` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,320.00 USD |
| `1D` | `0.1131` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 20,830.00 USD | 5,570.00 USD | 22,790.00 USD |
| `1D` | `0.1133` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 6,530.00 USD | 17,080.00 USD | 23,470.00 USD |
| `7D` | `0.1133` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD |
| `1D` | `0.1135` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 4,040.00 USD | 3,670.00 USD | 4,090.00 USD |
| `1D` | `0.1136` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 40.44 USD |
| `7D` | `0.1136` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD |
| `7D` | `0.1139` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD |
| `7D` | `0.1142` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD |
| `7D` | `0.1145` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD |
| `7D` | `0.1148` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 175,990.00 USD |
| `7D` | `0.1151` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD |
| `7D` | `0.1154` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 243,190.00 USD | 26,970.00 USD | 202,050.00 USD |
| `7D` | `0.1157` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 173,120.00 USD | 25,290.00 USD | 98,310.00 USD |
| `7D` | `0.1160` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 131,160.00 USD | 32,830.00 USD | 109,320.00 USD |
| `7D` | `0.1163` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD |
| `7D` | `0.1166` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD |
| `7D` | `0.1169` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 82,770.00 USD | 26,150.00 USD | 117,900.00 USD |
| `7D` | `0.1172` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD |
| `7D` | `0.1175` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 75,590.00 USD | 17,930.00 USD | 81,630.00 USD |
| `7D` | `0.1178` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 89,510.00 USD | 25,350.00 USD | 60,700.00 USD |
| `7D` | `0.1181` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD |
| `7D` | `0.1184` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD |
| `7D` | `0.1187` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 5,620.00 USD | 17,120.00 USD | 59,700.00 USD |
| `7D` | `0.1190` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD |
| `7D` | `0.1193` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD |
| `7D` | `0.1196` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD |
| `7D` | `0.1199` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 2,470.00 USD | 13,190.00 USD | 52,120.00 USD |
| `7D` | `0.1202` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 131,660.00 USD | 21,430.00 USD | 32,790.00 USD |
| `7D` | `0.1205` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 117,120.00 USD | 48,510.00 USD | 40,590.00 USD |
| `7D` | `0.1208` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 39,480.00 USD | 20,870.00 USD | 39,590.00 USD |
| `7D` | `0.1211` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 72,500.00 USD | 25,920.00 USD | 76,780.00 USD |
| `7D` | `0.1214` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD |
| `7D` | `0.1217` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD |
| `7D` | `0.1220` | 7,330,000.00 USD | 7,330,000.00 USD | 0.00 USD | 34,050.00 USD | 6,400.00 USD | 54,700.00 USD |
| `7D` | `0.1223` | 7,460,000.00 USD | 7,460,000.00 USD | 0.00 USD | 73,610.00 USD | 15,050.00 USD | 37,740.00 USD |
| `7D` | `0.1226` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 42,530.00 USD | 19,760.00 USD | 5,210.00 USD |
| `7D` | `0.1229` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 63,930.00 USD | 33,570.00 USD | 28,680.00 USD |
| `7D` | `0.1232` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 51,420.00 USD | 12,080.00 USD | 37,600.00 USD |
| `7D` | `0.1235` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 15,040.00 USD | 5,390.00 USD | 16,760.00 USD |
| `7D` | `0.1237` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 4,080.00 USD | 2,760.00 USD | 2,800.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `63.77M` | Total OI Tokens: `623,304,142.6 OP`
  * 1h OI Change: `+1.17%` | 4h OI Change: `+4.33%` | 24h OI Change: `-13.02%`
  * Exchange Breakdown: Binance=`13.86M` | Bybit=`13.00M` | OKX=`3.77M` | Hyperliquid=`3.14M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-2.33K` | Last 24h: `-2.42K` | Last 3d: `-6.63K` | Last 7d: `-14.48K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0286%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0286%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0062%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `55.70%` | `44.30%` | `1.26` | 1,920,000.00 USD |
| `15M` | `Binance` | `60.43%` | `39.57%` | `1.53` | 724,010.00 USD |
| `15M` | `OKX` | `59.87%` | `40.13%` | `1.49` | 291,030.00 USD |
| `15M` | `Bybit` | `69.51%` | `30.49%` | `2.28` | 177,130.00 USD |
| `15M` | `KuCoin` | `49.13%` | `50.87%` | `0.97` | 141,090.00 USD |
| `15M` | `Gate` | `77.28%` | `22.72%` | `3.40` | 32,920.00 USD |
| `15M` | `Bitget` | `47.44%` | `52.56%` | `0.90` | 50,530.00 USD |
| `15M` | `BingX` | `69.16%` | `30.84%` | `2.24` | 62,550.00 USD |
| `15M` | `MEXC` | `14.92%` | `85.08%` | `0.18` | 12,400.00 USD |
| `15M` | `Bitunix` | `57.97%` | `42.03%` | `1.38` | 22,820.00 USD |
| `15M` | `Hyperliquid` | `31.36%` | `68.64%` | `0.46` | 2,770.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.98%` | `51.02%` | `0.96` | 310,230.00 USD |
| `15M` | `Crypto.com` | `83.32%` | `16.68%` | `5.00` | 34.05 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 84,280.00 USD |
| `15M` | `HTX` | `71.67%` | `28.33%` | `2.53` | 1,470.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `44.51%` | `55.49%` | `0.80` | 51.25 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `31.83%` | `68.17%` | `0.47` | 514.50 USD |
| `15M` | `Whale Positions` | `60.43%` | `39.57%` | `1.53` | 724,010.00 USD |
| `15M` | `Global Accounts` | `55.70%` | `44.30%` | `1.26` | 1,920,000.00 USD |
| `1H` | `OP` | `48.45%` | `51.55%` | `0.94` | 12,650,000.00 USD |
| `1H` | `Binance` | `51.27%` | `48.73%` | `1.05` | 4,260,000.00 USD |
| `1H` | `OKX` | `52.8%` | `47.2%` | `1.12` | 2,810,000.00 USD |
| `1H` | `Bybit` | `62.44%` | `37.56%` | `1.66` | 1,010,000.00 USD |
| `1H` | `KuCoin` | `51.02%` | `48.98%` | `1.04` | 623,900.00 USD |
| `1H` | `Gate` | `53.52%` | `46.48%` | `1.15` | 219,130.00 USD |
| `1H` | `Bitget` | `44.09%` | `55.91%` | `0.79` | 208,170.00 USD |
| `1H` | `BingX` | `16.68%` | `83.32%` | `0.20` | 593,570.00 USD |
| `1H` | `MEXC` | `64.29%` | `35.71%` | `1.80` | 236,560.00 USD |
| `1H` | `Bitunix` | `25.4%` | `74.6%` | `0.34` | 315,140.00 USD |
| `1H` | `Hyperliquid` | `81.11%` | `18.89%` | `4.29` | 45,300.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `46.15%` | `53.85%` | `0.86` | 1,880,000.00 USD |
| `1H` | `Crypto.com` | `96.12%` | `3.88%` | `24.77` | 804.93 USD |
| `1H` | `WhiteBIT` | `11.39%` | `88.61%` | `0.13` | 401,640.00 USD |
| `1H` | `HTX` | `9.03%` | `90.97%` | `0.10` | 23,490.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `96.83%` | `3.17%` | `30.55` | 19,030.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `29.46%` | `70.54%` | `0.42` | 1,370.00 USD |
| `1H` | `Whale Positions` | `51.27%` | `48.73%` | `1.05` | 4,260,000.00 USD |
| `1H` | `Global Accounts` | `48.45%` | `51.55%` | `0.94` | 12,650,000.00 USD |
| `4H` | `OP` | `48.37%` | `51.63%` | `0.94` | 21,500,000.00 USD |
| `4H` | `Binance` | `50.78%` | `49.22%` | `1.03` | 7,660,000.00 USD |
| `4H` | `OKX` | `49.76%` | `50.24%` | `0.99` | 2,250,000.00 USD |
| `4H` | `Bybit` | `53.99%` | `46.01%` | `1.17` | 2,300,000.00 USD |
| `4H` | `KuCoin` | `50.26%` | `49.74%` | `1.01` | 1,750,000.00 USD |
| `4H` | `Gate` | `48.28%` | `51.72%` | `0.93` | 587,720.00 USD |
| `4H` | `Bitget` | `50.14%` | `49.86%` | `1.01` | 1,950,000.00 USD |
| `4H` | `BingX` | `32.13%` | `67.87%` | `0.47` | 2,210,000.00 USD |
| `4H` | `MEXC` | `50.79%` | `49.21%` | `1.03` | 927,970.00 USD |
| `4H` | `Bitunix` | `44.16%` | `55.84%` | `0.79` | 384,850.00 USD |
| `4H` | `Hyperliquid` | `57.48%` | `42.52%` | `1.35` | 274,290.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.18%` | `49.82%` | `1.01` | 759,240.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `27.36%` | `72.64%` | `0.38` | 302,130.00 USD |
| `4H` | `HTX` | `31%` | `69%` | `0.45` | 12,250.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `40.43%` | `59.57%` | `0.68` | 40,620.00 USD |
| `4H` | `Aster` | `14.28%` | `85.72%` | `0.17` | 72,020.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `14.36%` | `85.64%` | `0.17` | 14,130.00 USD |
| `4H` | `Whale Positions` | `50.78%` | `49.22%` | `1.03` | 7,660,000.00 USD |
| `4H` | `Global Accounts` | `48.37%` | `51.63%` | `0.94` | 21,500,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.0985` | `0.0980` | `0.0985` | `0.0986` | `0.0972` | 782,641.49 USD | 272,807.16 USD | 509,834.33 USD | -237,027.16 USD | `-30.29%` | `4B / 30S` |
| `5:00 UTC` | `0.0976` | `0.0974` | `0.0976` | `0.0979` | `0.0970` | 1,011,824.45 USD | 364,728.70 USD | 647,095.75 USD | -282,367.05 USD | `-27.91%` | `6B / 15S` |
| `0:00 UTC` | `0.0984` | `0.0984` | `0.0984` | `0.0992` | `0.0978` | 803,922.63 USD | 438,559.35 USD | 365,363.29 USD | 73,196.06 USD | `+9.10%` | `32B / 10S` |
| `5:00 UTC` | `0.0992` | `0.0992` | `0.0992` | `0.0995` | `0.0989` | 394,380.07 USD | 199,715.01 USD | 194,665.06 USD | 5,049.95 USD | `+1.28%` | `10B / 6S` |
| `0:00 UTC` | `0.0989` | `0.0992` | `0.0989` | `0.0999` | `0.0988` | 347,230.40 USD | 177,310.87 USD | 169,919.53 USD | 7,391.34 USD | `+2.13%` | `21B / 7S` |
| `5:00 UTC` | `0.1001` | `0.1001` | `0.1001` | `0.1004` | `0.0996` | 360,867.60 USD | 243,343.04 USD | 117,524.56 USD | 125,818.48 USD | `+34.87%` | `30B / 1S` |
| `0:00 UTC` | `0.1005` | `0.1006` | `0.1005` | `0.1009` | `0.1002` | 321,574.58 USD | 208,787.55 USD | 112,787.03 USD | 96,000.52 USD | `+29.85%` | `23B / 4S` |
| `5:00 UTC` | `0.1009` | `0.1011` | `0.1009` | `0.1014` | `0.1006` | 597,276.02 USD | 343,393.62 USD | 253,882.40 USD | 89,511.23 USD | `+14.99%` | `17B / 7S` |
| `0:00 UTC` | `0.1017` | `0.1020` | `0.1017` | `0.1027` | `0.1012` | 617,993.11 USD | 329,792.38 USD | 288,200.73 USD | 41,591.66 USD | `+6.73%` | `38B / 17S` |
| `5:00 UTC` | `0.1024` | `0.1024` | `0.1024` | `0.1025` | `0.1021` | 142,654.84 USD | 79,345.02 USD | 63,309.82 USD | 16,035.20 USD | `+11.24%` | `10B / 3S` |

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
| `5m` | -10,220.00 USD | 51,750.00 USD | **`ACCUMULATION`** |
| `15m` | -23,500.00 USD | 61,270.00 USD | **`ACCUMULATION`** |
| `30m` | 15,410.00 USD | 269,820.00 USD | **`ACCUMULATION`** |
| `1h` | 115,690.00 USD | 468,560.00 USD | **`ACCUMULATION`** |
| `2h` | 387,190.00 USD | 650,650.00 USD | **`ACCUMULATION`** |
| `4h` | -68,440.00 USD | 403,840.00 USD | **`ACCUMULATION`** |
| `6h` | -82,520.00 USD | -1,710,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 260,060.00 USD | -3,950,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 35,270.00 USD | -4,430,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 246,770.00 USD | -3,830,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -116,060.00 USD | -14,430,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,300,000.00 USD | -82,990,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-10.22K` | 15m=`-23.50K` | 1h=`+115.69K` | 24h=`+246.77K`
* Futures Capital Netflows: 5m=`+51.75K` | 15m=`+61.27K` | 1h=`+468.56K` | 24h=`-3.83M`
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
  * `2026-10-30 09:50:40 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:48:40 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:49:40 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
