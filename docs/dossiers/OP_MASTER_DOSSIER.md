# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 14:35:45 IST` (`2026-10-30 09:05:45 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1025` | `0.1030` | `0.1023` | `0.1029` | `560,146` | 57,450.78 USD | 18,481.69 USD | `+32.17%` | -1,795,817.15 USD | `+0.74` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.1029` | `0.1029` | `0.1024` | `0.1024` | `462,687` | 47,443.85 USD | -8,136.34 USD | `-17.15%` | -1,803,953.49 USD | `-0.89` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1024` | `0.1026` | `0.1023` | `0.1025` | `267,984` | 27,453.36 USD | 6,273.54 USD | `+22.85%` | -1,797,679.95 USD | `+0.01` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1032` | `0.1032` | `0.1023` | `0.1023` | `2,869,990` | 294,713.35 USD | -14,268.58 USD | `-4.84%` | -1,853,247.99 USD | `-1.08` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1023` | `0.1030` | `0.1023` | `0.1024` | `1,850,698` | 189,660.77 USD | 32,157.84 USD | `+16.96%` | -1,821,090.15 USD | `-0.06` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1024` | `0.1026` | `0.1023` | `0.1024` | `264,750` | 27,121.92 USD | 5,942.10 USD | `+21.91%` | -1,815,148.05 USD | `-0.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1030` | `0.1035` | `0.1022` | `0.1027` | `9,646,320` | 992,142.11 USD | 40,207.23 USD | `+4.05%` | -1,978,421.78 USD | `+0.29` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1027` | `0.1038` | `0.1023` | `0.1024` | `10,736,702` | 1,104,134.28 USD | 90,049.28 USD | `+8.16%` | -1,888,372.51 USD | `+0.40` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1024` | `0.1026` | `0.1023` | `0.1025` | `267,922` | 27,446.99 USD | 6,267.17 USD | `+22.83%` | -1,882,105.34 USD | `+0.24` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,490,108.93 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1040` | `0.0988` | `0.1027` | `54,609,324` | 5,566,939.91 USD | 608,714.61 USD | `+10.93%` | -1,881,394.33 USD | `+1.21` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1027` | `0.1038` | `0.1023` | `0.1025` | `11,004,624` | 1,131,581.27 USD | 96,316.44 USD | `+8.51%` | -1,785,077.88 USD | `+0.51` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | 165,115.32 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -1,152,082.54 USD | `-1.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,490,108.93 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1040` | `0.0988` | `0.1027` | `54,609,324` | 5,566,939.91 USD | 608,714.61 USD | `+10.93%` | -1,881,394.33 USD | `+1.21` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1027` | `0.1038` | `0.1023` | `0.1025` | `11,004,624` | 1,131,581.27 USD | 96,316.44 USD | `+8.51%` | -1,785,077.88 USD | `+0.51` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:32:27 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1103` | 5,867.99 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale BUY: 5.87K USD at 0.1103 USD [API] | `2026-10-29 11:51:44` |
| `ANNOUNCEMENT` | `INFO` | `0.1116` | 5,736.99 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale BUY: 5.74K USD at 0.1116 USD [API] | `2026-10-29 14:17:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1116` | 10,125.16 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale BUY: 10.13K USD at 0.1116 USD [API] | `2026-10-29 14:17:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1116` | 5,737.00 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale BUY: 5.74K USD at 0.1116 USD [API] | `2026-10-29 14:17:45` |


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
| `Live` | `Long Liquidation` | `0.0305` | 1,320.00 USD | 123,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0325` | 195.00 USD | 122,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0375` | 191.21 USD | 122,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 535.99 USD | 122,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 417.68 USD | 121,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 829.69 USD | 121,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 4,080.00 USD | 120,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 1,100.00 USD | 116,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 353.81 USD | 115,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 518.48 USD | 114,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 1,920.00 USD | 114,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 1,090.00 USD | 112,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 40,420.00 USD | 111,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 23,910.00 USD | 70,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,530.00 USD | 46,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,300.00 USD | 44,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 12,440.00 USD | 42,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 1,170.00 USD | 29,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 878.62 USD | 28,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 339.50 USD | 27,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 2,710.00 USD | 27,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 223.98 USD | 24,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 1,560.00 USD | 24,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 140.74 USD | 22,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 14,300.00 USD | 22,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 1,710.00 USD | 8,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0860` | 2,260,000.00 USD | 2,260,000.00 USD | 1,880.00 USD | 0.00 USD | 2,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0862` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 1,880.00 USD | 4,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0864` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 1,980.00 USD | 15,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0865` | 318.30 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0866` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0868` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0870` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0872` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 1,200.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0874` | 2,220,000.00 USD | 2,220,000.00 USD | 6,010.00 USD | 0.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0875` | 793.17 USD | 6,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0876` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 1,770.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0878` | 2,200,000.00 USD | 2,200,000.00 USD | 9,200.00 USD | 5,890.00 USD | 25,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0880` | 2,160,000.00 USD | 2,160,000.00 USD | 3,770.00 USD | 2,200.00 USD | 11,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0882` | 2,150,000.00 USD | 2,150,000.00 USD | 12,660.00 USD | 7,260.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0884` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 1,220.00 USD | 13,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0886` | 2,100,000.00 USD | 2,100,000.00 USD | 9,350.00 USD | 2,470.00 USD | 11,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0888` | 2,080,000.00 USD | 2,080,000.00 USD | 3,370.00 USD | 2,720.00 USD | 8,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0890` | 2,060,000.00 USD | 2,060,000.00 USD | 13,510.00 USD | 3,610.00 USD | 13,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0892` | 2,030,000.00 USD | 2,030,000.00 USD | 3,620.00 USD | 3,060.00 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0894` | 2,020,000.00 USD | 2,020,000.00 USD | 5,480.00 USD | 3,400.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,270.00 USD | 5,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0896` | 2,010,000.00 USD | 2,010,000.00 USD | 4,300.00 USD | 0.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0898` | 2,000,000.00 USD | 2,000,000.00 USD | 3,390.00 USD | 927.82 USD | 4,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0900` | 1,990,000.00 USD | 1,990,000.00 USD | 1,250.00 USD | 428.11 USD | 77.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0902` | 1,990,000.00 USD | 1,990,000.00 USD | 1,030.00 USD | 482.67 USD | 1,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0904` | 1,990,000.00 USD | 1,990,000.00 USD | 5,730.00 USD | 996.61 USD | 1,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0905` | 2,230.00 USD | 2,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0906` | 1,980,000.00 USD | 1,980,000.00 USD | 6,040.00 USD | 1,900.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0908` | 1,970,000.00 USD | 1,970,000.00 USD | 2,540.00 USD | 2,570.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0910` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 606.54 USD | 48.03 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0912` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 2,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0914` | 1,960,000.00 USD | 1,960,000.00 USD | 1,670.00 USD | 903.90 USD | 56.36 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0916` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 6,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0918` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0920` | 1,800,000.00 USD | 1,800,000.00 USD | 4,980.00 USD | 1,090.00 USD | 22,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0920` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 223.39 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0922` | 1,770,000.00 USD | 1,770,000.00 USD | 2,430.00 USD | 2,920.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0922` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 6,430.00 USD | 34,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0924` | 1,750,000.00 USD | 1,750,000.00 USD | 4,790.00 USD | 4,700.00 USD | 43,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0924` | 1,900,000.00 USD | 1,900,000.00 USD | 1,790.00 USD | 2,020.00 USD | 9,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0926` | 1,700,000.00 USD | 1,700,000.00 USD | 5,130.00 USD | 4,460.00 USD | 555.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0926` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0928` | 1,690,000.00 USD | 1,690,000.00 USD | 1,290.00 USD | 660.78 USD | 1,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0928` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0930` | 1,680,000.00 USD | 1,680,000.00 USD | 5,110.00 USD | 2,440.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0930` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0932` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 4,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0932` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 12,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0934` | 1,660,000.00 USD | 1,660,000.00 USD | 20,740.00 USD | 3,830.00 USD | 17,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0936` | 1,620,000.00 USD | 1,620,000.00 USD | 4,760.00 USD | 9,360.00 USD | 16,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0936` | 1,860,000.00 USD | 1,860,000.00 USD | 19,560.00 USD | 6,840.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0938` | 1,590,000.00 USD | 1,590,000.00 USD | 8,170.00 USD | 2,920.00 USD | 46,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0938` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 248.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0940` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0940` | 1,810,000.00 USD | 1,810,000.00 USD | 14,050.00 USD | 0.00 USD | 10,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0942` | 1,530,000.00 USD | 1,530,000.00 USD | 3,500.00 USD | 16,110.00 USD | 49,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0942` | 1,790,000.00 USD | 1,790,000.00 USD | 6,170.00 USD | 18,340.00 USD | 114,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0944` | 1,460,000.00 USD | 1,460,000.00 USD | 11,620.00 USD | 4,860.00 USD | 36,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0944` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 2,010.00 USD | 16.86 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0946` | 1,410,000.00 USD | 1,410,000.00 USD | 4,130.00 USD | 5,280.00 USD | 10,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0946` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 1,810.00 USD | 168.77 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0948` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 1,100.00 USD | 101.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0948` | 1,650,000.00 USD | 1,650,000.00 USD | 3,770.00 USD | 0.00 USD | 26,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0950` | 1,390,000.00 USD | 1,390,000.00 USD | 12,180.00 USD | 6,710.00 USD | 22,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0950` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 9,700.00 USD | 134.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0952` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 853.02 USD | 6,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0952` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 4,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0954` | 1,340,000.00 USD | 1,340,000.00 USD | 41,470.00 USD | 11,160.00 USD | 21,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0954` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 3,740.00 USD | 187.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0956` | 1,270,000.00 USD | 1,270,000.00 USD | 18,680.00 USD | 9,390.00 USD | 37,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0956` | 1,600,000.00 USD | 1,600,000.00 USD | 39,120.00 USD | 13,670.00 USD | 50,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0958` | 1,200,000.00 USD | 1,200,000.00 USD | 7,180.00 USD | 4,290.00 USD | 22,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0958` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0960` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 16,940.00 USD | 146.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0960` | 1,470,000.00 USD | 1,470,000.00 USD | 28,110.00 USD | 16,920.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0962` | 1,150,000.00 USD | 1,150,000.00 USD | 8,920.00 USD | 15,440.00 USD | 27,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0962` | 1,410,000.00 USD | 1,410,000.00 USD | 12,340.00 USD | 0.00 USD | 75,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0964` | 1,100,000.00 USD | 1,100,000.00 USD | 31,490.00 USD | 10,380.00 USD | 27,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0964` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 4,020.00 USD | 86.68 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0966` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 3,880.00 USD | 815.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0966` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 2,390.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0968` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 2,960.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0968` | 1,310,000.00 USD | 1,310,000.00 USD | 7,490.00 USD | 0.00 USD | 56,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0970` | 1,020,000.00 USD | 1,020,000.00 USD | 8,360.00 USD | 8,640.00 USD | 16,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0970` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 7,090.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0972` | 984,940.00 USD | 984,940.00 USD | 2,860.00 USD | 3,220.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0972` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 8,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0974` | 976,880.00 USD | 976,880.00 USD | 0.00 USD | 7,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0974` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 7,480.00 USD | 104.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0976` | 969,870.00 USD | 969,870.00 USD | 0.00 USD | 765.93 USD | 1,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0976` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 148.46 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0978` | 968,060.00 USD | 968,060.00 USD | 0.00 USD | 817.22 USD | 67.90 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0980` | 967,180.00 USD | 967,180.00 USD | 1,330.00 USD | 3,930.00 USD | 21,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0982` | 940,790.00 USD | 940,790.00 USD | 9,400.00 USD | 3,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0982` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 11,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0984` | 927,630.00 USD | 927,630.00 USD | 8,230.00 USD | 16,740.00 USD | 8,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0984` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 13,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0986` | 893,790.00 USD | 893,790.00 USD | 6,050.00 USD | 8,960.00 USD | 11,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0986` | 1,190,000.00 USD | 1,190,000.00 USD | 5,330.00 USD | 16,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0988` | 867,370.00 USD | 867,370.00 USD | 30,450.00 USD | 7,150.00 USD | 33,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0988` | 1,170,000.00 USD | 1,170,000.00 USD | 10,360.00 USD | 7,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0990` | 796,050.00 USD | 796,050.00 USD | 9,620.00 USD | 3,620.00 USD | 2,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0990` | 1,150,000.00 USD | 1,150,000.00 USD | 26,690.00 USD | 6,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0992` | 779,880.00 USD | 779,880.00 USD | 79,270.00 USD | 6,760.00 USD | 30,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0992` | 1,120,000.00 USD | 1,120,000.00 USD | 12,790.00 USD | 3,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0994` | 663,090.00 USD | 663,090.00 USD | 26,200.00 USD | 0.00 USD | 22,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0994` | 1,100,000.00 USD | 1,100,000.00 USD | 50,250.00 USD | 0.00 USD | 65,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0996` | 614,670.00 USD | 614,670.00 USD | 11,810.00 USD | 2,450.00 USD | 74,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0996` | 987,410.00 USD | 987,410.00 USD | 27,010.00 USD | 5,500.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0998` | 525,630.00 USD | 525,630.00 USD | 7,180.00 USD | 5,820.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0998` | 921,960.00 USD | 921,960.00 USD | 14,530.00 USD | 11,540.00 USD | 113,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1000` | 453,410.00 USD | 453,410.00 USD | 2,670.00 USD | 14,730.00 USD | 37,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1000` | 782,610.00 USD | 782,610.00 USD | 54,220.00 USD | 25,020.00 USD | 33,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1002` | 398,980.00 USD | 398,980.00 USD | 0.00 USD | 0.00 USD | 42,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1002` | 670,280.00 USD | 670,280.00 USD | 25,510.00 USD | 556.77 USD | 74,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1004` | 356,060.00 USD | 356,060.00 USD | 50,980.00 USD | 21,240.00 USD | 35,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1004` | 569,330.00 USD | 569,330.00 USD | 19,310.00 USD | 11,400.00 USD | 46,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1006` | 248,390.00 USD | 248,390.00 USD | 20,210.00 USD | 22,580.00 USD | 29,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1006` | 492,500.00 USD | 492,500.00 USD | 23,200.00 USD | 23,170.00 USD | 53,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1008` | 175,780.00 USD | 175,780.00 USD | 17,840.00 USD | 11,220.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1008` | 392,380.00 USD | 392,380.00 USD | 13,040.00 USD | 5,470.00 USD | 96,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1010` | 142,960.00 USD | 142,960.00 USD | 16,710.00 USD | 11,320.00 USD | 20,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1010` | 277,350.00 USD | 277,350.00 USD | 22,770.00 USD | 24,610.00 USD | 3,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1012` | 94,510.00 USD | 94,510.00 USD | 5,410.00 USD | 7,480.00 USD | 19,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1012` | 225,990.00 USD | 225,990.00 USD | 6,490.00 USD | 20,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1014` | 62,070.00 USD | 62,070.00 USD | 0.00 USD | 449.10 USD | 13,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1014` | 198,860.00 USD | 198,860.00 USD | 29,790.00 USD | 15,590.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1016` | 48,320.00 USD | 48,320.00 USD | 8,170.00 USD | 775.38 USD | 20,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1016` | 128,040.00 USD | 128,040.00 USD | 14,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1018` | 19,160.00 USD | 19,160.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1018` | 114,040.00 USD | 114,040.00 USD | 26,150.00 USD | 0.00 USD | 10,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1020` | 17,610.00 USD | 17,610.00 USD | 0.00 USD | 0.00 USD | 11,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1020` | 77,250.00 USD | 77,250.00 USD | 11,340.00 USD | 9,790.00 USD | 47,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1022` | 6,020.00 USD | 6,020.00 USD | 0.00 USD | 0.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1022` | 8,700.00 USD | 8,700.00 USD | 6,760.00 USD | 1,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1028` | 23,700.00 USD | 23,700.00 USD | 0.00 USD | 0.00 USD | 23,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1032` | 36,880.00 USD | 36,880.00 USD | 13,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1034` | 42,620.00 USD | 42,620.00 USD | 5,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1036` | 9,370.00 USD | 9,370.00 USD | 2,150.00 USD | 7,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1036` | 45,440.00 USD | 45,440.00 USD | 2,710.00 USD | 0.00 USD | 108.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1038` | 61,740.00 USD | 61,740.00 USD | 32,940.00 USD | 14,190.00 USD | 5,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1038` | 87,660.00 USD | 87,660.00 USD | 0.00 USD | 10,870.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1040` | 110,350.00 USD | 110,350.00 USD | 15,620.00 USD | 17,840.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1040` | 98,730.00 USD | 98,730.00 USD | 5,940.00 USD | 5,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1042` | 146,510.00 USD | 146,510.00 USD | 5,060.00 USD | 5,330.00 USD | 25,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1042` | 105,610.00 USD | 105,610.00 USD | 4,820.00 USD | 2,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1044` | 206,290.00 USD | 206,290.00 USD | 21,350.00 USD | 27,920.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1044` | 158,610.00 USD | 158,610.00 USD | 11,140.00 USD | 19,150.00 USD | 22,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1046` | 267,000.00 USD | 267,000.00 USD | 15,170.00 USD | 13,600.00 USD | 31,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1046` | 241,910.00 USD | 241,910.00 USD | 0.00 USD | 23,140.00 USD | 60,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1048` | 422,460.00 USD | 422,460.00 USD | 37,120.00 USD | 19,080.00 USD | 99,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1048` | 315,900.00 USD | 315,900.00 USD | 30,640.00 USD | 14,940.00 USD | 28,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1050` | 502,030.00 USD | 502,030.00 USD | 44,740.00 USD | 23,880.00 USD | 10,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1050` | 406,820.00 USD | 406,820.00 USD | 27,290.00 USD | 0.00 USD | 63,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1052` | 585,880.00 USD | 585,880.00 USD | 37,310.00 USD | 17,780.00 USD | 28,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1052` | 571,160.00 USD | 571,160.00 USD | 25,850.00 USD | 34,840.00 USD | 103,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1054` | 696,100.00 USD | 696,100.00 USD | 34,680.00 USD | 18,030.00 USD | 57,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1054` | 787,940.00 USD | 787,940.00 USD | 85,290.00 USD | 38,660.00 USD | 92,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1056` | 753,430.00 USD | 753,430.00 USD | 13,850.00 USD | 16,760.00 USD | 26,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1056` | 1,090,000.00 USD | 1,090,000.00 USD | 76,100.00 USD | 47,540.00 USD | 174,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1058` | 850,530.00 USD | 850,530.00 USD | 25,860.00 USD | 6,490.00 USD | 64,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1058` | 1,310,000.00 USD | 1,310,000.00 USD | 59,100.00 USD | 24,600.00 USD | 136,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1060` | 915,160.00 USD | 915,160.00 USD | 29,560.00 USD | 2,700.00 USD | 32,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1060` | 1,480,000.00 USD | 1,480,000.00 USD | 42,390.00 USD | 51,150.00 USD | 79,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1062` | 1,010,000.00 USD | 1,010,000.00 USD | 33,200.00 USD | 3,490.00 USD | 53,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1062` | 1,620,000.00 USD | 1,620,000.00 USD | 24,670.00 USD | 28,310.00 USD | 82,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1064` | 1,050,000.00 USD | 1,050,000.00 USD | 5,570.00 USD | 3,850.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1064` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 39,200.00 USD | 144,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1066` | 1,120,000.00 USD | 1,120,000.00 USD | 13,500.00 USD | 12,700.00 USD | 42,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1066` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 39,590.00 USD | 107,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1068` | 1,200,000.00 USD | 1,200,000.00 USD | 10,750.00 USD | 7,670.00 USD | 59,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1068` | 2,070,000.00 USD | 2,070,000.00 USD | 5,330.00 USD | 41,360.00 USD | 72,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1070` | 1,280,000.00 USD | 1,280,000.00 USD | 23,200.00 USD | 14,210.00 USD | 43,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1070` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 45,840.00 USD | 98,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1072` | 1,300,000.00 USD | 1,300,000.00 USD | 5,750.00 USD | 5,010.00 USD | 3,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1072` | 2,240,000.00 USD | 2,240,000.00 USD | 12,890.00 USD | 9,400.00 USD | 10,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1074` | 1,310,000.00 USD | 1,310,000.00 USD | 2,710.00 USD | 3,740.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1074` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 21,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1076` | 1,320,000.00 USD | 1,320,000.00 USD | 1,440.00 USD | 857.82 USD | 4,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1076` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 22,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1078` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 3,440.00 USD | 20,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1078` | 2,300,000.00 USD | 2,300,000.00 USD | 5,620.00 USD | 3,380.00 USD | 290.65 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1080` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 1,480.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1080` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1082` | 1,370,000.00 USD | 1,370,000.00 USD | 5,820.00 USD | 7,440.00 USD | 5,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1082` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 154.22 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1084` | 1,410,000.00 USD | 1,410,000.00 USD | 7,990.00 USD | 385.06 USD | 35,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1084` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1086` | 1,490,000.00 USD | 1,490,000.00 USD | 4,220.00 USD | 2,240.00 USD | 72,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1086` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 65.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1088` | 1,540,000.00 USD | 1,540,000.00 USD | 40,240.00 USD | 1,040.00 USD | 9,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1088` | 2,320,000.00 USD | 2,320,000.00 USD | 5,290.00 USD | 1,420.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1090` | 1,580,000.00 USD | 1,580,000.00 USD | 39,470.00 USD | 813.86 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1090` | 2,340,000.00 USD | 2,340,000.00 USD | 16,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1092` | 1,600,000.00 USD | 1,600,000.00 USD | 10,290.00 USD | 1,080.00 USD | 79.59 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1092` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 1,500.00 USD | 17,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1094` | 1,620,000.00 USD | 1,620,000.00 USD | 13,100.00 USD | 0.00 USD | 14,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1094` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 78.56 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1096` | 1,640,000.00 USD | 1,640,000.00 USD | 4,110.00 USD | 1,890.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1096` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 111.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1098` | 1,680,000.00 USD | 1,680,000.00 USD | 13,380.00 USD | 4,460.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1098` | 2,400,000.00 USD | 2,400,000.00 USD | 18,600.00 USD | 0.00 USD | 21,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1100` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 3,310.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1100` | 2,410,000.00 USD | 2,410,000.00 USD | 11,470.00 USD | 0.00 USD | 34.51 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1102` | 1,690,000.00 USD | 1,690,000.00 USD | 5,570.00 USD | 509.08 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1102` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1104` | 1,710,000.00 USD | 1,710,000.00 USD | 6,920.00 USD | 11,640.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1104` | 2,460,000.00 USD | 2,460,000.00 USD | 17,490.00 USD | 4,450.00 USD | 93.57 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1106` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 12,720.00 USD | 30,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1106` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 18,420.00 USD | 16,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1108` | 1,780,000.00 USD | 1,780,000.00 USD | 5,220.00 USD | 1,610.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1108` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 4,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1110` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 494.75 USD | 916.88 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1110` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 12,430.00 USD | 35.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1112` | 1,790,000.00 USD | 1,790,000.00 USD | 10,780.00 USD | 747.13 USD | 140.10 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1112` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 11,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1114` | 1,840,000.00 USD | 1,840,000.00 USD | 15,810.00 USD | 5,880.00 USD | 24,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1115` | 1,770.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1116` | 1,860,000.00 USD | 1,860,000.00 USD | 6,690.00 USD | 10,320.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1116` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 28.89 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1118` | 1,940,000.00 USD | 1,940,000.00 USD | 21,270.00 USD | 15,270.00 USD | 44,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1118` | 2,600,000.00 USD | 2,600,000.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1120` | 1,990,000.00 USD | 1,990,000.00 USD | 27,100.00 USD | 10,220.00 USD | 9,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1120` | 2,650,000.00 USD | 2,650,000.00 USD | 17,760.00 USD | 0.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1122` | 2,030,000.00 USD | 2,030,000.00 USD | 16,670.00 USD | 5,820.00 USD | 15,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1122` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 23,980.00 USD | 34,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1124` | 2,060,000.00 USD | 2,060,000.00 USD | 15,630.00 USD | 6,120.00 USD | 9,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1124` | 2,760,000.00 USD | 2,760,000.00 USD | 12,360.00 USD | 0.00 USD | 40,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1126` | 2,100,000.00 USD | 2,100,000.00 USD | 11,790.00 USD | 10,640.00 USD | 18,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1126` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 3,720.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1128` | 2,120,000.00 USD | 2,120,000.00 USD | 11,080.00 USD | 485.32 USD | 12,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1128` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 2,020.00 USD | 17,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1130` | 2,160,000.00 USD | 2,160,000.00 USD | 10,390.00 USD | 3,780.00 USD | 20,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1130` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 15,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1132` | 2,210,000.00 USD | 2,210,000.00 USD | 21,250.00 USD | 12,190.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1132` | 2,820,000.00 USD | 2,820,000.00 USD | 12,540.00 USD | 0.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1134` | 2,240,000.00 USD | 2,240,000.00 USD | 5,330.00 USD | 13,640.00 USD | 14,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1134` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 14,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1136` | 2,250,000.00 USD | 2,250,000.00 USD | 753.89 USD | 2,030.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1136` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1138` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 856.93 USD | 12,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1138` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1140` | 2,280,000.00 USD | 2,280,000.00 USD | 7,800.00 USD | 0.00 USD | 7,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1140` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1142` | 2,330,000.00 USD | 2,330,000.00 USD | 21,750.00 USD | 10,490.00 USD | 20,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1142` | 2,880,000.00 USD | 2,880,000.00 USD | 10,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1144` | 2,360,000.00 USD | 2,360,000.00 USD | 6,280.00 USD | 12,870.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1144` | 3,040,000.00 USD | 3,040,000.00 USD | 10,360.00 USD | 2,730.00 USD | 143,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1146` | 3,240,000.00 USD | 3,240,000.00 USD | 16,060.00 USD | 0.00 USD | 188,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1148` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 63,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1150` | 3,410,000.00 USD | 3,410,000.00 USD | 18,520.00 USD | 0.00 USD | 89,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1152` | 3,720,000.00 USD | 3,720,000.00 USD | 165,860.00 USD | 12,610.00 USD | 132,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1154` | 4,030,000.00 USD | 4,030,000.00 USD | 149,770.00 USD | 18,580.00 USD | 143,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1156` | 4,260,000.00 USD | 4,260,000.00 USD | 128,780.00 USD | 21,540.00 USD | 74,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1185` | 4,330.00 USD | 6,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1225` | 721.08 USD | 6,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1365` | 3,890.00 USD | 10,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1495` | 21,880.00 USD | 32,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1525` | 6,090.00 USD | 38,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1565` | 550.61 USD | 39,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1695` | 169.25 USD | 39,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1745` | 131.08 USD | 39,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1755` | 147.21 USD | 39,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1825` | 514.28 USD | 40,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1855` | 166.95 USD | 40,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1865` | 199.93 USD | 40,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2045` | 988.49 USD | 41,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0305` | 122,880.00 USD | 0.00 USD | 1,500.00 USD | `-70.21%` | `49,265.90` |
| `Live` | `Long` | `0.0395` | 121,380.00 USD | 0.00 USD | 201.41 USD | `-61.42%` | `5,098.90` |
| `Live` | `Long` | `0.0555` | 121,180.00 USD | 0.00 USD | 991.96 USD | `-45.80%` | `17,873.20` |
| `Live` | `Long` | `0.0575` | 120,180.00 USD | 0.00 USD | 829.69 USD | `-43.84%` | `14,429.40` |
| `Live` | `Long` | `0.0605` | 119,350.00 USD | 0.00 USD | 4,220.00 USD | `-40.91%` | `69,790.10` |
| `Live` | `Long` | `0.0645` | 115,130.00 USD | 0.00 USD | 353.81 USD | `-37.01%` | `5,485.40` |
| `Live` | `Long` | `0.0675` | 114,780.00 USD | 0.00 USD | 518.48 USD | `-34.08%` | `7,681.20` |
| `Live` | `Long` | `0.0685` | 114,260.00 USD | 0.00 USD | 1,920.00 USD | `-33.10%` | `28,000.00` |
| `Live` | `Long` | `0.0705` | 112,340.00 USD | 0.00 USD | 1,090.00 USD | `-31.15%` | `15,500.00` |
| `Live` | `Long` | `0.0715` | 111,250.00 USD | 0.00 USD | 40,420.00 USD | `-30.17%` | `565,287.50` |
| `Live` | `Long` | `0.0725` | 70,830.00 USD | 0.00 USD | 23,910.00 USD | `-29.19%` | `329,855.60` |
| `Live` | `Long` | `0.0735` | 46,920.00 USD | 0.00 USD | 2,530.00 USD | `-28.22%` | `34,439.60` |
| `Live` | `Long` | `0.0745` | 44,390.00 USD | 0.00 USD | 2,300.00 USD | `-27.24%` | `30,851.90` |
| `Live` | `Long` | `0.0755` | 42,090.00 USD | 0.00 USD | 12,440.00 USD | `-26.26%` | `164,709.50` |
| `Live` | `Long` | `0.0765` | 29,650.00 USD | 0.00 USD | 1,170.00 USD | `-25.29%` | `15,263.30` |
| `Live` | `Long` | `0.0775` | 28,480.00 USD | 0.00 USD | 878.62 USD | `-24.31%` | `11,337.00` |
| `Live` | `Long` | `0.0785` | 27,600.00 USD | 0.00 USD | 339.50 USD | `-23.33%` | `4,324.80` |
| `Live` | `Long` | `0.0795` | 27,270.00 USD | 0.00 USD | 2,710.00 USD | `-22.36%` | `34,073.20` |
| `Live` | `Long` | `0.0805` | 24,560.00 USD | 0.00 USD | 223.98 USD | `-21.38%` | `2,782.40` |
| `Live` | `Long` | `0.0815` | 24,330.00 USD | 0.00 USD | 1,560.00 USD | `-20.40%` | `19,181.40` |
| `Live` | `Long` | `0.0825` | 22,770.00 USD | 0.00 USD | 140.74 USD | `-19.43%` | `1,705.90` |
| `Live` | `Long` | `0.0845` | 22,630.00 USD | 0.00 USD | 14,300.00 USD | `-17.47%` | `169,238.60` |
| `Live` | `Long` | `0.0855` | 8,330.00 USD | 0.00 USD | 1,710.00 USD | `-16.50%` | `20,000.00` |
| `Live` | `Long` | `0.0865` | 6,620.00 USD | 0.00 USD | 318.30 USD | `-15.52%` | `3,679.80` |
| `Live` | `Long` | `0.0875` | 6,300.00 USD | 0.00 USD | 793.17 USD | `-14.54%` | `9,064.80` |
| `Live` | `Long` | `0.0895` | 5,510.00 USD | 0.00 USD | 3,270.00 USD | `-12.59%` | `36,562.50` |
| `Live` | `Long` | `0.0905` | 2,230.00 USD | 0.00 USD | 2,230.00 USD | `-11.61%` | `24,685.10` |
| `Live` | `Short` | `0.1115` | 1,770.00 USD | 1,770.00 USD | 0.00 USD | `+8.90%` | `15,878.10` |
| `Live` | `Short` | `0.1185` | 6,100.00 USD | 4,330.00 USD | 0.00 USD | `+15.73%` | `36,507.20` |
| `Live` | `Short` | `0.1225` | 6,820.00 USD | 721.08 USD | 0.00 USD | `+19.64%` | `5,886.40` |
| `Live` | `Short` | `0.1315` | 7,020.00 USD | 206.95 USD | 0.00 USD | `+28.43%` | `1,573.80` |
| `Live` | `Short` | `0.1385` | 10,750.00 USD | 3,720.00 USD | 0.00 USD | `+35.27%` | `26,889.40` |
| `Live` | `Short` | `0.1485` | 32,430.00 USD | 21,680.00 USD | 0.00 USD | `+45.03%` | `145,985.00` |
| `Live` | `Short` | `0.1525` | 38,520.00 USD | 6,090.00 USD | 0.00 USD | `+48.94%` | `39,929.50` |
| `Live` | `Short` | `0.1565` | 39,070.00 USD | 550.61 USD | 0.00 USD | `+52.85%` | `3,518.30` |
| `Live` | `Short` | `0.1695` | 39,240.00 USD | 169.25 USD | 0.00 USD | `+65.54%` | `998.50` |
| `Live` | `Short` | `0.1745` | 39,370.00 USD | 131.08 USD | 0.00 USD | `+70.43%` | `751.20` |
| `Live` | `Short` | `0.1755` | 39,510.00 USD | 147.21 USD | 0.00 USD | `+71.40%` | `838.80` |
| `Live` | `Short` | `0.1795` | 39,620.00 USD | 100.88 USD | 0.00 USD | `+75.31%` | `562.00` |
| `Live` | `Short` | `0.1825` | 40,130.00 USD | 514.28 USD | 0.00 USD | `+78.24%` | `2,818.00` |
| `Live` | `Short` | `0.1855` | 40,300.00 USD | 166.95 USD | 0.00 USD | `+81.17%` | `900.00` |
| `Live` | `Short` | `0.1865` | 40,500.00 USD | 199.93 USD | 0.00 USD | `+82.15%` | `1,072.00` |
| `Live` | `Short` | `0.1885` | 41,240.00 USD | 741.37 USD | 0.00 USD | `+84.10%` | `3,933.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0635` | 34,710.00 USD | 0.00 USD | 1,140.00 USD | `-37.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 33,570.00 USD | 0.00 USD | 773.46 USD | `-31.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 32,790.00 USD | 0.00 USD | 592.27 USD | `-30.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 32,200.00 USD | 0.00 USD | 755.00 USD | `-26.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0805` | 31,450.00 USD | 0.00 USD | 411.06 USD | `-21.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0815` | 31,030.00 USD | 0.00 USD | 285.01 USD | `-20.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0835` | 30,750.00 USD | 0.00 USD | 456.70 USD | `-18.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0845` | 30,290.00 USD | 0.00 USD | 171.09 USD | `-17.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 30,120.00 USD | 0.00 USD | 631.58 USD | `-16.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 29,490.00 USD | 0.00 USD | 782.05 USD | `-13.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 28,710.00 USD | 0.00 USD | 444.62 USD | `-11.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0915` | 28,260.00 USD | 0.00 USD | 623.91 USD | `-10.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 27,640.00 USD | 0.00 USD | 485.13 USD | `-7.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0965` | 27,150.00 USD | 0.00 USD | 5,700.00 USD | `-5.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0975` | 21,460.00 USD | 0.00 USD | 216.41 USD | `-4.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0985` | 21,240.00 USD | 0.00 USD | 931.75 USD | `-3.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0995` | 20,310.00 USD | 0.00 USD | 17,230.00 USD | `-2.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 3,080.00 USD | 0.00 USD | 2,180.00 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1015` | 903.42 USD | 0.00 USD | 903.42 USD | `-0.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1025` | 780.70 USD | 780.70 USD | 0.00 USD | `+0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1035` | 2,420.00 USD | 1,640.00 USD | 0.00 USD | `+1.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,530.00 USD | 105.53 USD | 0.00 USD | `+2.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 3,270.00 USD | 737.12 USD | 0.00 USD | `+3.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 112,550.00 USD | 109,280.00 USD | 0.00 USD | `+4.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1075` | 134,450.00 USD | 21,900.00 USD | 0.00 USD | `+4.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 134,610.00 USD | 160.20 USD | 0.00 USD | `+7.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 134,860.00 USD | 247.49 USD | 0.00 USD | `+8.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1125` | 135,650.00 USD | 786.65 USD | 0.00 USD | `+9.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1135` | 135,760.00 USD | 116.27 USD | 0.00 USD | `+10.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 135,900.00 USD | 137.71 USD | 0.00 USD | `+12.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1165` | 136,080.00 USD | 180.81 USD | 0.00 USD | `+13.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1175` | 136,440.00 USD | 363.49 USD | 0.00 USD | `+14.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1185` | 136,710.00 USD | 265.74 USD | 0.00 USD | `+15.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1195` | 151,350.00 USD | 14,640.00 USD | 0.00 USD | `+16.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1225` | 152,330.00 USD | 980.00 USD | 0.00 USD | `+19.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1235` | 159,690.00 USD | 7,370.00 USD | 0.00 USD | `+20.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1255` | 164,070.00 USD | 4,380.00 USD | 0.00 USD | `+22.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1315` | 195,630.00 USD | 31,560.00 USD | 0.00 USD | `+28.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1335` | 196,950.00 USD | 1,310.00 USD | 0.00 USD | `+30.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1345` | 201,100.00 USD | 4,150.00 USD | 0.00 USD | `+31.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1365` | 208,850.00 USD | 7,750.00 USD | 0.00 USD | `+33.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1405` | 221,950.00 USD | 13,110.00 USD | 0.00 USD | `+37.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1425` | 222,060.00 USD | 102.22 USD | 0.00 USD | `+39.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1435` | 229,230.00 USD | 7,180.00 USD | 0.00 USD | `+40.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1485` | 231,880.00 USD | 2,650.00 USD | 0.00 USD | `+45.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1525` | 235,640.00 USD | 3,770.00 USD | 0.00 USD | `+48.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 235,830.00 USD | 184.49 USD | 0.00 USD | `+51.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 238,640.00 USD | 2,810.00 USD | 0.00 USD | `+52.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 238,860.00 USD | 219.81 USD | 0.00 USD | `+53.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 239,130.00 USD | 277.62 USD | 0.00 USD | `+59.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 241,160.00 USD | 2,030.00 USD | 0.00 USD | `+65.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 241,380.00 USD | 216.55 USD | 0.00 USD | `+70.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 241,500.00 USD | 117.26 USD | 0.00 USD | `+92.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 262,030.00 USD | 20,530.00 USD | 0.00 USD | `+95.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 262,220.00 USD | 189.30 USD | 0.00 USD | `+98.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 262,440.00 USD | 219.22 USD | 0.00 USD | `+99.73%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0860` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 1,880.00 USD | 0.00 USD | 2,160.00 USD |
| `7D` | `0.0862` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 0.00 USD | 1,880.00 USD | 4,720.00 USD |
| `7D` | `0.0864` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 0.00 USD | 1,980.00 USD | 15,640.00 USD |
| `7D` | `0.0866` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 2,080.00 USD |
| `7D` | `0.0868` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 2,880.00 USD |
| `7D` | `0.0870` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 2,870.00 USD |
| `7D` | `0.0872` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 0.00 USD | 1,200.00 USD | 2,980.00 USD |
| `7D` | `0.0874` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 6,010.00 USD | 0.00 USD | 4,500.00 USD |
| `7D` | `0.0876` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 0.00 USD | 1,770.00 USD | 4,890.00 USD |
| `7D` | `0.0878` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 9,200.00 USD | 5,890.00 USD | 25,110.00 USD |
| `7D` | `0.0880` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 3,770.00 USD | 2,200.00 USD | 11,840.00 USD |
| `7D` | `0.0882` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 12,660.00 USD | 7,260.00 USD | 9,180.00 USD |
| `7D` | `0.0884` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 0.00 USD | 1,220.00 USD | 13,650.00 USD |
| `7D` | `0.0886` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 9,350.00 USD | 2,470.00 USD | 11,320.00 USD |
| `7D` | `0.0888` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 3,370.00 USD | 2,720.00 USD | 8,290.00 USD |
| `7D` | `0.0890` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 13,510.00 USD | 3,610.00 USD | 13,150.00 USD |
| `7D` | `0.0892` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 3,620.00 USD | 3,060.00 USD | 2,090.00 USD |
| `7D` | `0.0894` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 5,480.00 USD | 3,400.00 USD | 7,750.00 USD |
| `7D` | `0.0896` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 4,300.00 USD | 0.00 USD | 4,200.00 USD |
| `7D` | `0.0898` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 3,390.00 USD | 927.82 USD | 4,460.00 USD |
| `7D` | `0.0900` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 1,250.00 USD | 428.11 USD | 77.78 USD |
| `7D` | `0.0902` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 1,030.00 USD | 482.67 USD | 1,300.00 USD |
| `7D` | `0.0904` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 5,730.00 USD | 996.61 USD | 1,700.00 USD |
| `7D` | `0.0906` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 6,040.00 USD | 1,900.00 USD | 4,140.00 USD |
| `7D` | `0.0908` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 2,540.00 USD | 2,570.00 USD | 1,290.00 USD |
| `7D` | `0.0910` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 0.00 USD | 606.54 USD | 48.03 USD |
| `7D` | `0.0912` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 2,650.00 USD |
| `7D` | `0.0914` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 1,670.00 USD | 903.90 USD | 56.36 USD |
| `7D` | `0.0916` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 6,310.00 USD |
| `7D` | `0.0918` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 1,740.00 USD |
| `1D` | `0.0920` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 4,980.00 USD | 1,090.00 USD | 22,940.00 USD |
| `7D` | `0.0920` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 223.39 USD |
| `1D` | `0.0922` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 2,430.00 USD | 2,920.00 USD | 12,180.00 USD |
| `7D` | `0.0922` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 0.00 USD | 6,430.00 USD | 34,750.00 USD |
| `1D` | `0.0924` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 4,790.00 USD | 4,700.00 USD | 43,420.00 USD |
| `7D` | `0.0924` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 1,790.00 USD | 2,020.00 USD | 9,170.00 USD |
| `1D` | `0.0926` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 5,130.00 USD | 4,460.00 USD | 555.49 USD |
| `7D` | `0.0926` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 8,180.00 USD |
| `1D` | `0.0928` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 1,290.00 USD | 660.78 USD | 1,120.00 USD |
| `7D` | `0.0928` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD |
| `1D` | `0.0930` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 5,110.00 USD | 2,440.00 USD | 8,690.00 USD |
| `7D` | `0.0930` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD |
| `1D` | `0.0932` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 4,320.00 USD |
| `7D` | `0.0932` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 12,290.00 USD |
| `1D` | `0.0934` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 20,740.00 USD | 3,830.00 USD | 17,320.00 USD |
| `1D` | `0.0936` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 4,760.00 USD | 9,360.00 USD | 16,330.00 USD |
| `7D` | `0.0936` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 19,560.00 USD | 6,840.00 USD | 25,450.00 USD |
| `1D` | `0.0938` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 8,170.00 USD | 2,920.00 USD | 46,580.00 USD |
| `7D` | `0.0938` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 248.29 USD |
| `1D` | `0.0940` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD |
| `7D` | `0.0940` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 14,050.00 USD | 0.00 USD | 10,640.00 USD |
| `1D` | `0.0942` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 3,500.00 USD | 16,110.00 USD | 49,220.00 USD |
| `7D` | `0.0942` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 6,170.00 USD | 18,340.00 USD | 114,170.00 USD |
| `1D` | `0.0944` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 11,620.00 USD | 4,860.00 USD | 36,500.00 USD |
| `7D` | `0.0944` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 0.00 USD | 2,010.00 USD | 16.86 USD |
| `1D` | `0.0946` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 4,130.00 USD | 5,280.00 USD | 10,220.00 USD |
| `7D` | `0.0946` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 0.00 USD | 1,810.00 USD | 168.77 USD |
| `1D` | `0.0948` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 0.00 USD | 1,100.00 USD | 101.09 USD |
| `7D` | `0.0948` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 3,770.00 USD | 0.00 USD | 26,920.00 USD |
| `1D` | `0.0950` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 12,180.00 USD | 6,710.00 USD | 22,900.00 USD |
| `7D` | `0.0950` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 0.00 USD | 9,700.00 USD | 134.31 USD |
| `1D` | `0.0952` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 0.00 USD | 853.02 USD | 6,660.00 USD |
| `7D` | `0.0952` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 0.00 USD | 4,410.00 USD | 0.00 USD |
| `1D` | `0.0954` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 41,470.00 USD | 11,160.00 USD | 21,160.00 USD |
| `7D` | `0.0954` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 0.00 USD | 3,740.00 USD | 187.14 USD |
| `1D` | `0.0956` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 18,680.00 USD | 9,390.00 USD | 37,070.00 USD |
| `7D` | `0.0956` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 39,120.00 USD | 13,670.00 USD | 50,980.00 USD |
| `1D` | `0.0958` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 7,180.00 USD | 4,290.00 USD | 22,320.00 USD |
| `7D` | `0.0958` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 21,370.00 USD |
| `1D` | `0.0960` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 16,940.00 USD | 146.83 USD |
| `7D` | `0.0960` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 28,110.00 USD | 16,920.00 USD | 20,150.00 USD |
| `1D` | `0.0962` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 8,920.00 USD | 15,440.00 USD | 27,750.00 USD |
| `7D` | `0.0962` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 12,340.00 USD | 0.00 USD | 75,010.00 USD |
| `1D` | `0.0964` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 31,490.00 USD | 10,380.00 USD | 27,840.00 USD |
| `7D` | `0.0964` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 0.00 USD | 4,020.00 USD | 86.68 USD |
| `1D` | `0.0966` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 0.00 USD | 3,880.00 USD | 815.14 USD |
| `7D` | `0.0966` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 0.00 USD | 2,390.00 USD | 2,830.00 USD |
| `1D` | `0.0968` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 0.00 USD | 2,960.00 USD | 2,340.00 USD |
| `7D` | `0.0968` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 7,490.00 USD | 0.00 USD | 56,170.00 USD |
| `1D` | `0.0970` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 8,360.00 USD | 8,640.00 USD | 16,030.00 USD |
| `7D` | `0.0970` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 0.00 USD | 7,090.00 USD | 5,010.00 USD |
| `1D` | `0.0972` | 984,940.00 USD | 0.00 USD | 984,940.00 USD | 2,860.00 USD | 3,220.00 USD | 1,980.00 USD |
| `7D` | `0.0972` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 8,830.00 USD | 0.00 USD |
| `1D` | `0.0974` | 976,880.00 USD | 0.00 USD | 976,880.00 USD | 0.00 USD | 7,010.00 USD | 0.00 USD |
| `7D` | `0.0974` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 7,480.00 USD | 104.80 USD |
| `1D` | `0.0976` | 969,870.00 USD | 0.00 USD | 969,870.00 USD | 0.00 USD | 765.93 USD | 1,040.00 USD |
| `7D` | `0.0976` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 148.46 USD |
| `1D` | `0.0978` | 968,060.00 USD | 0.00 USD | 968,060.00 USD | 0.00 USD | 817.22 USD | 67.90 USD |
| `1D` | `0.0980` | 967,180.00 USD | 0.00 USD | 967,180.00 USD | 1,330.00 USD | 3,930.00 USD | 21,130.00 USD |
| `1D` | `0.0982` | 940,790.00 USD | 0.00 USD | 940,790.00 USD | 9,400.00 USD | 3,760.00 USD | 0.00 USD |
| `7D` | `0.0982` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 11,350.00 USD |
| `1D` | `0.0984` | 927,630.00 USD | 0.00 USD | 927,630.00 USD | 8,230.00 USD | 16,740.00 USD | 8,870.00 USD |
| `7D` | `0.0984` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 0.00 USD | 13,080.00 USD | 0.00 USD |
| `1D` | `0.0986` | 893,790.00 USD | 0.00 USD | 893,790.00 USD | 6,050.00 USD | 8,960.00 USD | 11,400.00 USD |
| `7D` | `0.0986` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 5,330.00 USD | 16,520.00 USD | 0.00 USD |
| `1D` | `0.0988` | 867,370.00 USD | 0.00 USD | 867,370.00 USD | 30,450.00 USD | 7,150.00 USD | 33,720.00 USD |
| `7D` | `0.0988` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 10,360.00 USD | 7,820.00 USD | 0.00 USD |
| `1D` | `0.0990` | 796,050.00 USD | 0.00 USD | 796,050.00 USD | 9,620.00 USD | 3,620.00 USD | 2,930.00 USD |
| `7D` | `0.0990` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 26,690.00 USD | 6,660.00 USD | 0.00 USD |
| `1D` | `0.0992` | 779,880.00 USD | 0.00 USD | 779,880.00 USD | 79,270.00 USD | 6,760.00 USD | 30,750.00 USD |
| `7D` | `0.0992` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 12,790.00 USD | 3,930.00 USD | 0.00 USD |
| `1D` | `0.0994` | 663,090.00 USD | 0.00 USD | 663,090.00 USD | 26,200.00 USD | 0.00 USD | 22,220.00 USD |
| `7D` | `0.0994` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 50,250.00 USD | 0.00 USD | 65,080.00 USD |
| `1D` | `0.0996` | 614,670.00 USD | 0.00 USD | 614,670.00 USD | 11,810.00 USD | 2,450.00 USD | 74,790.00 USD |
| `7D` | `0.0996` | 987,410.00 USD | 0.00 USD | 987,410.00 USD | 27,010.00 USD | 5,500.00 USD | 32,940.00 USD |
| `1D` | `0.0998` | 525,630.00 USD | 0.00 USD | 525,630.00 USD | 7,180.00 USD | 5,820.00 USD | 59,220.00 USD |
| `7D` | `0.0998` | 921,960.00 USD | 0.00 USD | 921,960.00 USD | 14,530.00 USD | 11,540.00 USD | 113,290.00 USD |
| `1D` | `0.1000` | 453,410.00 USD | 0.00 USD | 453,410.00 USD | 2,670.00 USD | 14,730.00 USD | 37,040.00 USD |
| `7D` | `0.1000` | 782,610.00 USD | 0.00 USD | 782,610.00 USD | 54,220.00 USD | 25,020.00 USD | 33,080.00 USD |
| `1D` | `0.1002` | 398,980.00 USD | 0.00 USD | 398,980.00 USD | 0.00 USD | 0.00 USD | 42,920.00 USD |
| `7D` | `0.1002` | 670,280.00 USD | 0.00 USD | 670,280.00 USD | 25,510.00 USD | 556.77 USD | 74,890.00 USD |
| `1D` | `0.1004` | 356,060.00 USD | 0.00 USD | 356,060.00 USD | 50,980.00 USD | 21,240.00 USD | 35,450.00 USD |
| `7D` | `0.1004` | 569,330.00 USD | 0.00 USD | 569,330.00 USD | 19,310.00 USD | 11,400.00 USD | 46,130.00 USD |
| `1D` | `0.1006` | 248,390.00 USD | 0.00 USD | 248,390.00 USD | 20,210.00 USD | 22,580.00 USD | 29,820.00 USD |
| `7D` | `0.1006` | 492,500.00 USD | 0.00 USD | 492,500.00 USD | 23,200.00 USD | 23,170.00 USD | 53,740.00 USD |
| `1D` | `0.1008` | 175,780.00 USD | 0.00 USD | 175,780.00 USD | 17,840.00 USD | 11,220.00 USD | 3,770.00 USD |
| `7D` | `0.1008` | 392,380.00 USD | 0.00 USD | 392,380.00 USD | 13,040.00 USD | 5,470.00 USD | 96,530.00 USD |
| `1D` | `0.1010` | 142,960.00 USD | 0.00 USD | 142,960.00 USD | 16,710.00 USD | 11,320.00 USD | 20,420.00 USD |
| `7D` | `0.1010` | 277,350.00 USD | 0.00 USD | 277,350.00 USD | 22,770.00 USD | 24,610.00 USD | 3,990.00 USD |
| `1D` | `0.1012` | 94,510.00 USD | 0.00 USD | 94,510.00 USD | 5,410.00 USD | 7,480.00 USD | 19,550.00 USD |
| `7D` | `0.1012` | 225,990.00 USD | 0.00 USD | 225,990.00 USD | 6,490.00 USD | 20,640.00 USD | 0.00 USD |
| `1D` | `0.1014` | 62,070.00 USD | 0.00 USD | 62,070.00 USD | 0.00 USD | 449.10 USD | 13,300.00 USD |
| `7D` | `0.1014` | 198,860.00 USD | 0.00 USD | 198,860.00 USD | 29,790.00 USD | 15,590.00 USD | 25,450.00 USD |
| `1D` | `0.1016` | 48,320.00 USD | 0.00 USD | 48,320.00 USD | 8,170.00 USD | 775.38 USD | 20,220.00 USD |
| `7D` | `0.1016` | 128,040.00 USD | 0.00 USD | 128,040.00 USD | 14,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1018` | 19,160.00 USD | 0.00 USD | 19,160.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD |
| `7D` | `0.1018` | 114,040.00 USD | 0.00 USD | 114,040.00 USD | 26,150.00 USD | 0.00 USD | 10,630.00 USD |
| `1D` | `0.1020` | 17,610.00 USD | 0.00 USD | 17,610.00 USD | 0.00 USD | 0.00 USD | 11,590.00 USD |
| `7D` | `0.1020` | 77,250.00 USD | 0.00 USD | 77,250.00 USD | 11,340.00 USD | 9,790.00 USD | 47,420.00 USD |
| `1D` | `0.1022` | 6,020.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD | 0.00 USD | 6,020.00 USD |
| `7D` | `0.1022` | 8,700.00 USD | 0.00 USD | 8,700.00 USD | 6,760.00 USD | 1,940.00 USD | 0.00 USD |
| `7D` | `0.1025` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1026` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1028` | 23,700.00 USD | 23,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23,700.00 USD |
| `7D` | `0.1032` | 36,880.00 USD | 36,880.00 USD | 0.00 USD | 13,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1034` | 42,620.00 USD | 42,620.00 USD | 0.00 USD | 5,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1036` | 9,370.00 USD | 9,370.00 USD | 0.00 USD | 2,150.00 USD | 7,220.00 USD | 0.00 USD |
| `7D` | `0.1036` | 45,440.00 USD | 45,440.00 USD | 0.00 USD | 2,710.00 USD | 0.00 USD | 108.00 USD |
| `1D` | `0.1038` | 61,740.00 USD | 61,740.00 USD | 0.00 USD | 32,940.00 USD | 14,190.00 USD | 5,240.00 USD |
| `7D` | `0.1038` | 87,660.00 USD | 87,660.00 USD | 0.00 USD | 0.00 USD | 10,870.00 USD | 31,350.00 USD |
| `1D` | `0.1040` | 110,350.00 USD | 110,350.00 USD | 0.00 USD | 15,620.00 USD | 17,840.00 USD | 15,140.00 USD |
| `7D` | `0.1040` | 98,730.00 USD | 98,730.00 USD | 0.00 USD | 5,940.00 USD | 5,130.00 USD | 0.00 USD |
| `1D` | `0.1042` | 146,510.00 USD | 146,510.00 USD | 0.00 USD | 5,060.00 USD | 5,330.00 USD | 25,770.00 USD |
| `7D` | `0.1042` | 105,610.00 USD | 105,610.00 USD | 0.00 USD | 4,820.00 USD | 2,060.00 USD | 0.00 USD |
| `1D` | `0.1044` | 206,290.00 USD | 206,290.00 USD | 0.00 USD | 21,350.00 USD | 27,920.00 USD | 10,500.00 USD |
| `7D` | `0.1044` | 158,610.00 USD | 158,610.00 USD | 0.00 USD | 11,140.00 USD | 19,150.00 USD | 22,700.00 USD |
| `1D` | `0.1046` | 267,000.00 USD | 267,000.00 USD | 0.00 USD | 15,170.00 USD | 13,600.00 USD | 31,940.00 USD |
| `7D` | `0.1046` | 241,910.00 USD | 241,910.00 USD | 0.00 USD | 0.00 USD | 23,140.00 USD | 60,160.00 USD |
| `1D` | `0.1048` | 422,460.00 USD | 422,460.00 USD | 0.00 USD | 37,120.00 USD | 19,080.00 USD | 99,260.00 USD |
| `7D` | `0.1048` | 315,900.00 USD | 315,900.00 USD | 0.00 USD | 30,640.00 USD | 14,940.00 USD | 28,410.00 USD |
| `1D` | `0.1050` | 502,030.00 USD | 502,030.00 USD | 0.00 USD | 44,740.00 USD | 23,880.00 USD | 10,960.00 USD |
| `7D` | `0.1050` | 406,820.00 USD | 406,820.00 USD | 0.00 USD | 27,290.00 USD | 0.00 USD | 63,630.00 USD |
| `1D` | `0.1052` | 585,880.00 USD | 585,880.00 USD | 0.00 USD | 37,310.00 USD | 17,780.00 USD | 28,760.00 USD |
| `7D` | `0.1052` | 571,160.00 USD | 571,160.00 USD | 0.00 USD | 25,850.00 USD | 34,840.00 USD | 103,650.00 USD |
| `1D` | `0.1054` | 696,100.00 USD | 696,100.00 USD | 0.00 USD | 34,680.00 USD | 18,030.00 USD | 57,510.00 USD |
| `7D` | `0.1054` | 787,940.00 USD | 787,940.00 USD | 0.00 USD | 85,290.00 USD | 38,660.00 USD | 92,830.00 USD |
| `1D` | `0.1056` | 753,430.00 USD | 753,430.00 USD | 0.00 USD | 13,850.00 USD | 16,760.00 USD | 26,710.00 USD |
| `7D` | `0.1056` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 76,100.00 USD | 47,540.00 USD | 174,740.00 USD |
| `1D` | `0.1058` | 850,530.00 USD | 850,530.00 USD | 0.00 USD | 25,860.00 USD | 6,490.00 USD | 64,740.00 USD |
| `7D` | `0.1058` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 59,100.00 USD | 24,600.00 USD | 136,660.00 USD |
| `1D` | `0.1060` | 915,160.00 USD | 915,160.00 USD | 0.00 USD | 29,560.00 USD | 2,700.00 USD | 32,370.00 USD |
| `7D` | `0.1060` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 42,390.00 USD | 51,150.00 USD | 79,920.00 USD |
| `1D` | `0.1062` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 33,200.00 USD | 3,490.00 USD | 53,370.00 USD |
| `7D` | `0.1062` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 24,670.00 USD | 28,310.00 USD | 82,400.00 USD |
| `1D` | `0.1064` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 5,570.00 USD | 3,850.00 USD | 40,030.00 USD |
| `7D` | `0.1064` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 39,200.00 USD | 144,990.00 USD |
| `1D` | `0.1066` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 13,500.00 USD | 12,700.00 USD | 42,320.00 USD |
| `7D` | `0.1066` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 39,590.00 USD | 107,620.00 USD |
| `1D` | `0.1068` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 10,750.00 USD | 7,670.00 USD | 59,560.00 USD |
| `7D` | `0.1068` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 5,330.00 USD | 41,360.00 USD | 72,650.00 USD |
| `1D` | `0.1070` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 23,200.00 USD | 14,210.00 USD | 43,250.00 USD |
| `7D` | `0.1070` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 45,840.00 USD | 98,490.00 USD |
| `1D` | `0.1072` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 5,750.00 USD | 5,010.00 USD | 3,070.00 USD |
| `7D` | `0.1072` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 12,890.00 USD | 9,400.00 USD | 10,320.00 USD |
| `1D` | `0.1074` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 2,710.00 USD | 3,740.00 USD | 9,000.00 USD |
| `7D` | `0.1074` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 21,630.00 USD | 0.00 USD |
| `1D` | `0.1076` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,440.00 USD | 857.82 USD | 4,030.00 USD |
| `7D` | `0.1076` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,600.00 USD |
| `1D` | `0.1078` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 3,440.00 USD | 20,830.00 USD |
| `7D` | `0.1078` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 5,620.00 USD | 3,380.00 USD | 290.65 USD |
| `1D` | `0.1080` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 1,480.00 USD | 5,690.00 USD |
| `7D` | `0.1080` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,860.00 USD |
| `1D` | `0.1082` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 5,820.00 USD | 7,440.00 USD | 5,110.00 USD |
| `7D` | `0.1082` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 154.22 USD |
| `1D` | `0.1084` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 7,990.00 USD | 385.06 USD | 35,900.00 USD |
| `7D` | `0.1084` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1086` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 4,220.00 USD | 2,240.00 USD | 72,960.00 USD |
| `7D` | `0.1086` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65.29 USD |
| `1D` | `0.1088` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 40,240.00 USD | 1,040.00 USD | 9,220.00 USD |
| `7D` | `0.1088` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 5,290.00 USD | 1,420.00 USD | 9,590.00 USD |
| `1D` | `0.1090` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 39,470.00 USD | 813.86 USD | 2,170.00 USD |
| `7D` | `0.1090` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1092` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 10,290.00 USD | 1,080.00 USD | 79.59 USD |
| `7D` | `0.1092` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 1,500.00 USD | 17,740.00 USD |
| `1D` | `0.1094` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 13,100.00 USD | 0.00 USD | 14,050.00 USD |
| `7D` | `0.1094` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78.56 USD |
| `1D` | `0.1096` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 7,780.00 USD |
| `7D` | `0.1096` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 111.29 USD |
| `1D` | `0.1098` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 13,380.00 USD | 4,460.00 USD | 22,840.00 USD |
| `7D` | `0.1098` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 21,840.00 USD |
| `1D` | `0.1100` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 3,310.00 USD | 4,310.00 USD |
| `7D` | `0.1100` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 34.51 USD |
| `1D` | `0.1102` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 5,570.00 USD | 509.08 USD | 0.00 USD |
| `7D` | `0.1102` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1104` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 6,920.00 USD | 11,640.00 USD | 1,170.00 USD |
| `7D` | `0.1104` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 17,490.00 USD | 4,450.00 USD | 93.57 USD |
| `1D` | `0.1106` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 12,720.00 USD | 30,820.00 USD |
| `7D` | `0.1106` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 18,420.00 USD | 16,040.00 USD |
| `1D` | `0.1108` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 5,220.00 USD | 1,610.00 USD | 17,380.00 USD |
| `7D` | `0.1108` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 4,120.00 USD | 0.00 USD |
| `1D` | `0.1110` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 494.75 USD | 916.88 USD |
| `7D` | `0.1110` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 12,430.00 USD | 35.29 USD |
| `1D` | `0.1112` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 10,780.00 USD | 747.13 USD | 140.10 USD |
| `7D` | `0.1112` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 0.00 USD |
| `1D` | `0.1114` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 15,810.00 USD | 5,880.00 USD | 24,740.00 USD |
| `1D` | `0.1116` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 6,690.00 USD | 10,320.00 USD | 6,930.00 USD |
| `7D` | `0.1116` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28.89 USD |
| `1D` | `0.1118` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 21,270.00 USD | 15,270.00 USD | 44,800.00 USD |
| `7D` | `0.1118` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD |
| `1D` | `0.1120` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 27,100.00 USD | 10,220.00 USD | 9,850.00 USD |
| `7D` | `0.1120` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 17,760.00 USD | 0.00 USD | 29,770.00 USD |
| `1D` | `0.1122` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 16,670.00 USD | 5,820.00 USD | 15,000.00 USD |
| `7D` | `0.1122` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 23,980.00 USD | 34,740.00 USD |
| `1D` | `0.1124` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 15,630.00 USD | 6,120.00 USD | 9,800.00 USD |
| `7D` | `0.1124` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 12,360.00 USD | 0.00 USD | 40,520.00 USD |
| `1D` | `0.1126` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 11,790.00 USD | 10,640.00 USD | 18,550.00 USD |
| `7D` | `0.1126` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 3,720.00 USD | 7,340.00 USD |
| `1D` | `0.1128` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 11,080.00 USD | 485.32 USD | 12,900.00 USD |
| `7D` | `0.1128` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD | 17,130.00 USD |
| `1D` | `0.1130` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 10,390.00 USD | 3,780.00 USD | 20,030.00 USD |
| `7D` | `0.1130` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,190.00 USD |
| `1D` | `0.1132` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 21,250.00 USD | 12,190.00 USD | 16,650.00 USD |
| `7D` | `0.1132` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 12,540.00 USD | 0.00 USD | 8,170.00 USD |
| `1D` | `0.1134` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 5,330.00 USD | 13,640.00 USD | 14,960.00 USD |
| `7D` | `0.1134` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 14,090.00 USD | 0.00 USD |
| `1D` | `0.1136` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 753.89 USD | 2,030.00 USD | 5,340.00 USD |
| `7D` | `0.1136` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD |
| `1D` | `0.1138` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 856.93 USD | 12,600.00 USD |
| `7D` | `0.1138` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD |
| `1D` | `0.1140` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 7,800.00 USD | 0.00 USD | 7,010.00 USD |
| `7D` | `0.1140` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,600.00 USD |
| `1D` | `0.1142` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 21,750.00 USD | 10,490.00 USD | 20,850.00 USD |
| `7D` | `0.1142` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1144` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 6,280.00 USD | 12,870.00 USD | 3,940.00 USD |
| `7D` | `0.1144` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 10,360.00 USD | 2,730.00 USD | 143,410.00 USD |
| `7D` | `0.1146` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 16,060.00 USD | 0.00 USD | 188,440.00 USD |
| `7D` | `0.1148` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 63,900.00 USD |
| `7D` | `0.1150` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 18,520.00 USD | 0.00 USD | 89,510.00 USD |
| `7D` | `0.1152` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 165,860.00 USD | 12,610.00 USD | 132,130.00 USD |
| `7D` | `0.1154` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 149,770.00 USD | 18,580.00 USD | 143,090.00 USD |
| `7D` | `0.1156` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 128,780.00 USD | 21,540.00 USD | 74,660.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `64.11M` | Total OI Tokens: `623,376,816.0 OP`
  * 1h OI Change: `+0.02%` | 4h OI Change: `+0.78%` | 24h OI Change: `-11.47%`
  * Exchange Breakdown: Binance=`13.81M` | Bybit=`12.89M` | OKX=`3.92M` | Hyperliquid=`3.17M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-5.55K` | Last 24h: `-4.25K` | Last 3d: `-11.30K` | Last 7d: `-13.94K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0297%` | **USDT OKX** | `-0.0213%` |
| **USDT Bybit** | `-0.0067%` | **USDT KuCoin** | `-0.0182%` |
| **USDT MEXC** | `-0.0299%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `55.56%` | `44.44%` | `1.25` | 30,470,000.00 USD |
| `15M` | `Binance` | `56.39%` | `43.61%` | `1.29` | 12,300,000.00 USD |
| `15M` | `OKX` | `54.19%` | `45.81%` | `1.18` | 3,340,000.00 USD |
| `15M` | `Bybit` | `54%` | `46%` | `1.17` | 4,290,000.00 USD |
| `15M` | `KuCoin` | `55.64%` | `44.36%` | `1.25` | 172,020.00 USD |
| `15M` | `Gate` | `53.73%` | `46.27%` | `1.16` | 544,500.00 USD |
| `15M` | `Bitget` | `39.83%` | `60.17%` | `0.66` | 1,310,000.00 USD |
| `15M` | `BingX` | `45.61%` | `54.39%` | `0.84` | 600,070.00 USD |
| `15M` | `MEXC` | `54.88%` | `45.12%` | `1.22` | 965,170.00 USD |
| `15M` | `Bitunix` | `48.42%` | `51.58%` | `0.94` | 633,380.00 USD |
| `15M` | `Hyperliquid` | `66.43%` | `33.57%` | `1.98` | 4,610,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.45%` | `51.55%` | `0.94` | 86,300.00 USD |
| `15M` | `Crypto.com` | `13.37%` | `86.63%` | `0.15` | 1,630.00 USD |
| `15M` | `WhiteBIT` | `42.53%` | `57.47%` | `0.74` | 1,080,000.00 USD |
| `15M` | `HTX` | `42.55%` | `57.45%` | `0.74` | 8,460.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `57.24%` | `42.76%` | `1.34` | 277,940.00 USD |
| `15M` | `Aster` | `42.61%` | `57.39%` | `0.74` | 155,200.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `56.54%` | `43.46%` | `1.30` | 92,690.00 USD |
| `15M` | `Whale Positions` | `56.39%` | `43.61%` | `1.29` | 12,300,000.00 USD |
| `15M` | `Global Accounts` | `55.56%` | `44.44%` | `1.25` | 30,470,000.00 USD |
| `1H` | `OP` | `51.94%` | `48.06%` | `1.08` | 11,360,000.00 USD |
| `1H` | `Binance` | `52.49%` | `47.51%` | `1.10` | 3,180,000.00 USD |
| `1H` | `OKX` | `35.42%` | `64.58%` | `0.55` | 1,060,000.00 USD |
| `1H` | `Bybit` | `52%` | `48%` | `1.08` | 1,000,000.00 USD |
| `1H` | `KuCoin` | `43.75%` | `56.25%` | `0.78` | 36,680.00 USD |
| `1H` | `Gate` | `50.15%` | `49.85%` | `1.01` | 978,620.00 USD |
| `1H` | `Bitget` | `46.17%` | `53.83%` | `0.86` | 781,360.00 USD |
| `1H` | `BingX` | `40.06%` | `59.94%` | `0.67` | 2,120,000.00 USD |
| `1H` | `MEXC` | `51.53%` | `48.47%` | `1.06` | 167,330.00 USD |
| `1H` | `Bitunix` | `46.5%` | `53.5%` | `0.87` | 169,120.00 USD |
| `1H` | `Hyperliquid` | `33.01%` | `66.99%` | `0.49` | 152,770.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.5%` | `48.5%` | `1.06` | 328,760.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `90.23%` | `9.77%` | `9.24` | 1,350,000.00 USD |
| `1H` | `HTX` | `43.94%` | `56.06%` | `0.78` | 14,160.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `41.76%` | `58.24%` | `0.72` | 19,130.00 USD |
| `1H` | `Aster` | `53.09%` | `46.91%` | `1.13` | 5,690.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `12.73%` | `87.27%` | `0.15` | 1,760.00 USD |
| `1H` | `Whale Positions` | `52.49%` | `47.51%` | `1.10` | 3,180,000.00 USD |
| `1H` | `Global Accounts` | `51.94%` | `48.06%` | `1.08` | 11,360,000.00 USD |
| `4H` | `OP` | `44.84%` | `55.16%` | `0.81` | 31,800,000.00 USD |
| `4H` | `Binance` | `44.96%` | `55.04%` | `0.82` | 9,770,000.00 USD |
| `4H` | `OKX` | `42.35%` | `57.65%` | `0.73` | 3,040,000.00 USD |
| `4H` | `Bybit` | `48.65%` | `51.35%` | `0.95` | 2,610,000.00 USD |
| `4H` | `KuCoin` | `49.32%` | `50.68%` | `0.97` | 2,130,000.00 USD |
| `4H` | `Gate` | `40.47%` | `59.53%` | `0.68` | 1,520,000.00 USD |
| `4H` | `Bitget` | `47.06%` | `52.94%` | `0.89` | 848,160.00 USD |
| `4H` | `BingX` | `17.88%` | `82.12%` | `0.22` | 3,700,000.00 USD |
| `4H` | `MEXC` | `51.36%` | `48.64%` | `1.06` | 1,240,000.00 USD |
| `4H` | `Bitunix` | `46.32%` | `53.68%` | `0.86` | 684,280.00 USD |
| `4H` | `Hyperliquid` | `42.9%` | `57.1%` | `0.75` | 533,130.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.64%` | `50.36%` | `0.99` | 4,070,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `98.04%` | `1.96%` | `50.02` | 1,390,000.00 USD |
| `4H` | `HTX` | `41.32%` | `58.68%` | `0.70` | 17,070.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `5.96%` | `94.04%` | `0.06` | 248,590.00 USD |
| `4H` | `Aster` | `35.44%` | `64.56%` | `0.55` | 7,990.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `37.95%` | `62.05%` | `0.61` | 7,330.00 USD |
| `4H` | `Whale Positions` | `44.96%` | `55.04%` | `0.82` | 9,770,000.00 USD |
| `4H` | `Global Accounts` | `44.84%` | `55.16%` | `0.81` | 31,800,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1035` | `0.1034` | `0.1035` | `0.1040` | `0.1030` | 262,321.00 USD | 114,307.74 USD | 148,013.25 USD | -33,705.51 USD | `-12.85%` | `21B / 35S` |
| `5:00 UTC` | `0.1027` | `0.1028` | `0.1027` | `0.1032` | `0.1025` | 193,153.71 USD | 97,068.83 USD | 96,084.88 USD | 983.95 USD | `+0.51%` | `19B / 10S` |
| `0:00 UTC` | `0.1030` | `0.1030` | `0.1030` | `0.1032` | `0.1026` | 264,794.32 USD | 131,284.83 USD | 133,509.50 USD | -2,224.67 USD | `-0.84%` | `14B / 10S` |
| `5:00 UTC` | `0.1030` | `0.1029` | `0.1030` | `0.1032` | `0.1027` | 198,254.32 USD | 108,143.71 USD | 90,110.61 USD | 18,033.10 USD | `+9.10%` | `17B / 11S` |
| `0:00 UTC` | `0.1032` | `0.1029` | `0.1032` | `0.1035` | `0.1022` | 287,615.17 USD | 126,080.17 USD | 161,535.00 USD | -35,454.83 USD | `-12.33%` | `22B / 36S` |
| `5:00 UTC` | `0.1025` | `0.1026` | `0.1025` | `0.1030` | `0.1024` | 241,478.30 USD | 150,665.97 USD | 90,812.34 USD | 59,853.63 USD | `+24.79%` | `12B / 6S` |
| `0:00 UTC` | `0.1024` | `0.1027` | `0.1024` | `0.1036` | `0.1023` | 359,716.26 USD | 217,752.22 USD | 141,964.04 USD | 75,788.18 USD | `+21.07%` | `25B / 11S` |
| `5:00 UTC` | `0.1033` | `0.1034` | `0.1033` | `0.1038` | `0.1032` | 260,043.89 USD | 128,207.87 USD | 131,836.02 USD | -3,628.15 USD | `-1.40%` | `11B / 2S` |
| `0:00 UTC` | `0.1024` | `0.1027` | `0.1024` | `0.1032` | `0.1023` | 294,713.35 USD | 140,222.38 USD | 154,490.97 USD | -14,268.58 USD | `-4.84%` | `9B / 14S` |
| `5:00 UTC` | `0.1024` | `0.1025` | `0.1024` | `0.1030` | `0.1023` | 184,209.30 USD | 108,429.68 USD | 75,779.61 USD | 32,650.07 USD | `+17.72%` | `13B / 16S` |

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
| `5m` | -1,380.00 USD | -39,480.00 USD | **`DISTRIBUTION`** |
| `15m` | -3,860.00 USD | -94,600.00 USD | **`DISTRIBUTION`** |
| `30m` | -37,550.00 USD | -147,910.00 USD | **`DISTRIBUTION`** |
| `1h` | 35,600.00 USD | -10,630.00 USD | **`ACCUMULATION`** |
| `2h` | -5,680.00 USD | 27,990.00 USD | **`ACCUMULATION`** |
| `4h` | -27,020.00 USD | 342,160.00 USD | **`ACCUMULATION`** |
| `6h` | -92,650.00 USD | 116,220.00 USD | **`ACCUMULATION`** |
| `8h` | -112,040.00 USD | -1,720,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 493,650.00 USD | -1,250,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 259,940.00 USD | -3,880,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -186,350.00 USD | -12,750,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,310,000.00 USD | -83,350,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.38K` | 15m=`-3.86K` | 1h=`+35.60K` | 24h=`+259.94K`
* Futures Capital Netflows: 5m=`-39.48K` | 15m=`-94.60K` | 1h=`-10.63K` | 24h=`-3.88M`
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
  * `2026-10-30 14:09:50 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:50:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:31:50 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
