# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 14:29:40 IST` (`2026-10-30 08:59:40 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1032` | `0.1032` | `0.1027` | `0.1027` | `1,051,578` | 108,248.55 USD | -8,886.07 USD | `-8.21%` | -1,785,804.83 USD | `-0.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.1027` | `0.1029` | `0.1025` | `0.1026` | `809,453` | 83,110.56 USD | 2,471.72 USD | `+2.97%` | -1,783,333.11 USD | `-0.19` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1026` | `0.1026` | `0.1023` | `0.1023` | `281,247` | 28,809.62 USD | -5,638.68 USD | `-19.57%` | -1,788,971.78 USD | `-0.68` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1027` | `0.1036` | `0.1023` | `0.1035` | `3,501,804` | 359,716.26 USD | 75,788.18 USD | `+21.07%` | -1,773,290.60 USD | `+0.63` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1035` | `0.1038` | `0.1032` | `0.1032` | `2,514,209` | 260,043.89 USD | -3,628.15 USD | `-1.40%` | -1,776,918.76 USD | `-0.95` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1032` | `0.1032` | `0.1023` | `0.1023` | `2,142,277` | 220,168.73 USD | -12,053.03 USD | `-5.47%` | -1,788,971.78 USD | `-1.03` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1021` | `0.1040` | `0.1015` | `0.1030` | `11,261,356` | 1,159,165.71 USD | 75,542.59 USD | `+6.52%` | -1,922,785.86 USD | `+0.39` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1030` | `0.1035` | `0.1022` | `0.1027` | `9,646,320` | 992,142.11 USD | 40,207.23 USD | `+4.05%` | -1,882,578.62 USD | `+0.29` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1027` | `0.1038` | `0.1023` | `0.1023` | `8,158,290` | 839,928.89 USD | 60,107.00 USD | `+7.16%` | -1,822,471.63 USD | `+0.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,490,108.93 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1040` | `0.0988` | `0.1027` | `54,609,324` | 5,566,939.91 USD | 608,714.61 USD | `+10.93%` | -1,881,394.33 USD | `+1.21` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1027` | `0.1038` | `0.1023` | `0.1024` | `8,206,066` | 844,820.17 USD | 64,711.92 USD | `+7.66%` | -1,816,682.41 USD | `+0.48` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | 165,115.32 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -1,152,082.54 USD | `-1.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,490,108.93 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1040` | `0.0988` | `0.1027` | `54,609,324` | 5,566,939.91 USD | 608,714.61 USD | `+10.93%` | -1,881,394.33 USD | `+1.21` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1027` | `0.1038` | `0.1023` | `0.1024` | `8,206,066` | 844,820.17 USD | 64,711.92 USD | `+7.66%` | -1,816,682.41 USD | `+0.48` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:22:11 IST` |

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
| `Live` | `Long` | `0.0305` | 123,810.00 USD | 0.00 USD | 1,320.00 USD | `-70.30%` | `43,265.90` |
| `Live` | `Long` | `0.0325` | 122,490.00 USD | 0.00 USD | 195.00 USD | `-68.35%` | `6,000.00` |
| `Live` | `Long` | `0.0375` | 122,290.00 USD | 0.00 USD | 191.21 USD | `-63.49%` | `5,098.90` |
| `Live` | `Long` | `0.0525` | 122,100.00 USD | 0.00 USD | 535.99 USD | `-48.88%` | `10,209.40` |
| `Live` | `Long` | `0.0545` | 121,570.00 USD | 0.00 USD | 417.68 USD | `-46.93%` | `7,663.80` |
| `Live` | `Long` | `0.0575` | 121,150.00 USD | 0.00 USD | 829.69 USD | `-44.01%` | `14,429.40` |
| `Live` | `Long` | `0.0585` | 120,320.00 USD | 0.00 USD | 4,080.00 USD | `-43.04%` | `69,790.10` |
| `Live` | `Long` | `0.0615` | 116,240.00 USD | 0.00 USD | 1,100.00 USD | `-40.12%` | `17,943.80` |
| `Live` | `Long` | `0.0645` | 115,130.00 USD | 0.00 USD | 353.81 USD | `-37.20%` | `5,485.40` |
| `Live` | `Long` | `0.0675` | 114,780.00 USD | 0.00 USD | 518.48 USD | `-34.27%` | `7,681.20` |
| `Live` | `Long` | `0.0685` | 114,260.00 USD | 0.00 USD | 1,920.00 USD | `-33.30%` | `28,000.00` |
| `Live` | `Long` | `0.0705` | 112,340.00 USD | 0.00 USD | 1,090.00 USD | `-31.35%` | `15,500.00` |
| `Live` | `Long` | `0.0715` | 111,250.00 USD | 0.00 USD | 40,420.00 USD | `-30.38%` | `565,287.50` |
| `Live` | `Long` | `0.0725` | 70,830.00 USD | 0.00 USD | 23,910.00 USD | `-29.41%` | `329,855.60` |
| `Live` | `Long` | `0.0735` | 46,920.00 USD | 0.00 USD | 2,530.00 USD | `-28.43%` | `34,439.60` |
| `Live` | `Long` | `0.0745` | 44,390.00 USD | 0.00 USD | 2,300.00 USD | `-27.46%` | `30,851.90` |
| `Live` | `Long` | `0.0755` | 42,090.00 USD | 0.00 USD | 12,440.00 USD | `-26.48%` | `164,709.50` |
| `Live` | `Long` | `0.0765` | 29,650.00 USD | 0.00 USD | 1,170.00 USD | `-25.51%` | `15,263.30` |
| `Live` | `Long` | `0.0775` | 28,480.00 USD | 0.00 USD | 878.62 USD | `-24.54%` | `11,337.00` |
| `Live` | `Long` | `0.0785` | 27,600.00 USD | 0.00 USD | 339.50 USD | `-23.56%` | `4,324.80` |
| `Live` | `Long` | `0.0795` | 27,270.00 USD | 0.00 USD | 2,710.00 USD | `-22.59%` | `34,073.20` |
| `Live` | `Long` | `0.0805` | 24,560.00 USD | 0.00 USD | 223.98 USD | `-21.62%` | `2,782.40` |
| `Live` | `Long` | `0.0815` | 24,330.00 USD | 0.00 USD | 1,560.00 USD | `-20.64%` | `19,181.40` |
| `Live` | `Long` | `0.0825` | 22,770.00 USD | 0.00 USD | 140.74 USD | `-19.67%` | `1,705.90` |
| `Live` | `Long` | `0.0845` | 22,630.00 USD | 0.00 USD | 14,300.00 USD | `-17.72%` | `169,238.60` |
| `Live` | `Long` | `0.0855` | 8,330.00 USD | 0.00 USD | 1,710.00 USD | `-16.75%` | `20,000.00` |
| `Live` | `Long` | `0.0865` | 6,620.00 USD | 0.00 USD | 318.30 USD | `-15.77%` | `3,679.80` |
| `Live` | `Long` | `0.0875` | 6,300.00 USD | 0.00 USD | 793.17 USD | `-14.80%` | `9,064.80` |
| `Live` | `Long` | `0.0895` | 5,510.00 USD | 0.00 USD | 3,270.00 USD | `-12.85%` | `36,562.50` |
| `Live` | `Long` | `0.0905` | 2,230.00 USD | 0.00 USD | 2,230.00 USD | `-11.88%` | `24,685.10` |
| `Live` | `Short` | `0.1115` | 1,770.00 USD | 1,770.00 USD | 0.00 USD | `+8.57%` | `15,878.10` |
| `Live` | `Short` | `0.1185` | 6,100.00 USD | 4,330.00 USD | 0.00 USD | `+15.38%` | `36,507.20` |
| `Live` | `Short` | `0.1225` | 6,820.00 USD | 721.08 USD | 0.00 USD | `+19.28%` | `5,886.40` |
| `Live` | `Short` | `0.1365` | 10,700.00 USD | 3,890.00 USD | 0.00 USD | `+32.91%` | `28,463.20` |
| `Live` | `Short` | `0.1495` | 32,590.00 USD | 21,880.00 USD | 0.00 USD | `+45.57%` | `146,387.20` |
| `Live` | `Short` | `0.1525` | 38,680.00 USD | 6,090.00 USD | 0.00 USD | `+48.49%` | `39,929.50` |
| `Live` | `Short` | `0.1565` | 39,230.00 USD | 550.61 USD | 0.00 USD | `+52.39%` | `3,518.30` |
| `Live` | `Short` | `0.1695` | 39,400.00 USD | 169.25 USD | 0.00 USD | `+65.04%` | `998.50` |
| `Live` | `Short` | `0.1745` | 39,530.00 USD | 131.08 USD | 0.00 USD | `+69.91%` | `751.20` |
| `Live` | `Short` | `0.1755` | 39,680.00 USD | 147.21 USD | 0.00 USD | `+70.89%` | `838.80` |
| `Live` | `Short` | `0.1825` | 40,190.00 USD | 514.28 USD | 0.00 USD | `+77.70%` | `2,818.00` |
| `Live` | `Short` | `0.1855` | 40,360.00 USD | 166.95 USD | 0.00 USD | `+80.62%` | `900.00` |
| `Live` | `Short` | `0.1865` | 40,560.00 USD | 199.93 USD | 0.00 USD | `+81.60%` | `1,072.00` |
| `Live` | `Short` | `0.2045` | 41,540.00 USD | 988.49 USD | 0.00 USD | `+99.12%` | `4,833.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0635` | 35,490.00 USD | 0.00 USD | 1,140.00 USD | `-38.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 34,350.00 USD | 0.00 USD | 773.46 USD | `-31.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 33,570.00 USD | 0.00 USD | 592.27 USD | `-30.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 32,980.00 USD | 0.00 USD | 755.00 USD | `-26.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0805` | 32,230.00 USD | 0.00 USD | 411.06 USD | `-21.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0815` | 31,820.00 USD | 0.00 USD | 285.01 USD | `-20.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0835` | 31,530.00 USD | 0.00 USD | 456.70 USD | `-18.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0845` | 31,070.00 USD | 0.00 USD | 171.09 USD | `-17.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 30,900.00 USD | 0.00 USD | 631.58 USD | `-16.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 30,270.00 USD | 0.00 USD | 782.05 USD | `-13.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 29,490.00 USD | 0.00 USD | 444.62 USD | `-11.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0915` | 29,040.00 USD | 0.00 USD | 623.91 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 28,420.00 USD | 0.00 USD | 485.13 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0965` | 27,940.00 USD | 0.00 USD | 5,700.00 USD | `-6.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0975` | 22,240.00 USD | 0.00 USD | 216.41 USD | `-5.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0985` | 22,020.00 USD | 0.00 USD | 931.75 USD | `-4.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0995` | 21,090.00 USD | 0.00 USD | 17,230.00 USD | `-3.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 3,860.00 USD | 0.00 USD | 2,180.00 USD | `-2.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1015` | 1,680.00 USD | 0.00 USD | 903.42 USD | `-1.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 780.70 USD | 0.00 USD | 780.70 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1035` | 1,640.00 USD | 1,640.00 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 1,750.00 USD | 105.53 USD | 0.00 USD | `+1.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,490.00 USD | 737.12 USD | 0.00 USD | `+2.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 111,770.00 USD | 109,280.00 USD | 0.00 USD | `+3.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1075` | 133,670.00 USD | 21,900.00 USD | 0.00 USD | `+4.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 133,830.00 USD | 160.20 USD | 0.00 USD | `+7.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 134,080.00 USD | 247.49 USD | 0.00 USD | `+8.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1125` | 134,870.00 USD | 786.65 USD | 0.00 USD | `+9.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1135` | 134,980.00 USD | 116.27 USD | 0.00 USD | `+10.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 135,120.00 USD | 137.71 USD | 0.00 USD | `+12.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1165` | 135,300.00 USD | 180.81 USD | 0.00 USD | `+13.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1175` | 135,660.00 USD | 363.49 USD | 0.00 USD | `+14.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1185` | 135,930.00 USD | 265.74 USD | 0.00 USD | `+15.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1195` | 150,570.00 USD | 14,640.00 USD | 0.00 USD | `+16.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1225` | 151,550.00 USD | 980.00 USD | 0.00 USD | `+19.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1235` | 158,910.00 USD | 7,370.00 USD | 0.00 USD | `+20.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1255` | 163,290.00 USD | 4,380.00 USD | 0.00 USD | `+22.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1315` | 194,850.00 USD | 31,560.00 USD | 0.00 USD | `+28.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1335` | 196,170.00 USD | 1,310.00 USD | 0.00 USD | `+29.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1345` | 200,320.00 USD | 4,150.00 USD | 0.00 USD | `+30.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1365` | 208,060.00 USD | 7,750.00 USD | 0.00 USD | `+32.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1405` | 221,170.00 USD | 13,110.00 USD | 0.00 USD | `+36.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1425` | 221,270.00 USD | 102.22 USD | 0.00 USD | `+38.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1435` | 228,450.00 USD | 7,180.00 USD | 0.00 USD | `+39.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1485` | 231,100.00 USD | 2,650.00 USD | 0.00 USD | `+44.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1525` | 234,860.00 USD | 3,770.00 USD | 0.00 USD | `+48.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 235,050.00 USD | 184.49 USD | 0.00 USD | `+51.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 237,860.00 USD | 2,810.00 USD | 0.00 USD | `+52.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 238,080.00 USD | 219.81 USD | 0.00 USD | `+53.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 238,350.00 USD | 277.62 USD | 0.00 USD | `+59.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 240,380.00 USD | 2,030.00 USD | 0.00 USD | `+65.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 240,600.00 USD | 216.55 USD | 0.00 USD | `+69.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 240,720.00 USD | 117.26 USD | 0.00 USD | `+92.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 261,250.00 USD | 20,530.00 USD | 0.00 USD | `+95.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 261,440.00 USD | 189.30 USD | 0.00 USD | `+98.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 261,660.00 USD | 219.22 USD | 0.00 USD | `+99.12%` | `TACTICAL (Retail Cluster)` |

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
| `15M` | `OP` | `48.48%` | `51.52%` | `0.94` | 1,020,000.00 USD |
| `15M` | `Binance` | `54.6%` | `45.4%` | `1.20` | 343,780.00 USD |
| `15M` | `OKX` | `54.73%` | `45.27%` | `1.21` | 104,700.00 USD |
| `15M` | `Bybit` | `30.02%` | `69.98%` | `0.43` | 94,480.00 USD |
| `15M` | `KuCoin` | `64.15%` | `35.85%` | `1.79` | 135,420.00 USD |
| `15M` | `Gate` | `71.2%` | `28.8%` | `2.47` | 22,090.00 USD |
| `15M` | `Bitget` | `55.03%` | `44.97%` | `1.22` | 33,430.00 USD |
| `15M` | `BingX` | `30.45%` | `69.55%` | `0.44` | 106,590.00 USD |
| `15M` | `MEXC` | `68.32%` | `31.68%` | `2.16` | 31,820.00 USD |
| `15M` | `Bitunix` | `57.7%` | `42.3%` | `1.36` | 28,520.00 USD |
| `15M` | `Hyperliquid` | `48.91%` | `51.09%` | `0.96` | 10,720.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `45.93%` | `54.07%` | `0.85` | 46,860.00 USD |
| `15M` | `Crypto.com` | `0%` | `100%` | `0.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `97.14%` | `2.86%` | `33.97` | 60,550.00 USD |
| `15M` | `HTX` | `23.25%` | `76.75%` | `0.30` | 0.61 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 993.96 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 18.60 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 9.95 USD |
| `15M` | `Whale Positions` | `54.6%` | `45.4%` | `1.20` | 343,780.00 USD |
| `15M` | `Global Accounts` | `48.48%` | `51.52%` | `0.94` | 1,020,000.00 USD |
| `1H` | `OP` | `50.19%` | `49.81%` | `1.01` | 3,600,000.00 USD |
| `1H` | `Binance` | `54.88%` | `45.12%` | `1.22` | 1,120,000.00 USD |
| `1H` | `OKX` | `53.76%` | `46.24%` | `1.16` | 533,130.00 USD |
| `1H` | `Bybit` | `41.48%` | `58.52%` | `0.71` | 566,060.00 USD |
| `1H` | `KuCoin` | `49.32%` | `50.68%` | `0.97` | 156,540.00 USD |
| `1H` | `Gate` | `45.87%` | `54.13%` | `0.85` | 32,810.00 USD |
| `1H` | `Bitget` | `62.17%` | `37.83%` | `1.64` | 90,080.00 USD |
| `1H` | `BingX` | `28.47%` | `71.53%` | `0.40` | 273,430.00 USD |
| `1H` | `MEXC` | `47.23%` | `52.77%` | `0.90` | 98,990.00 USD |
| `1H` | `Bitunix` | `54.17%` | `45.83%` | `1.18` | 29,650.00 USD |
| `1H` | `Hyperliquid` | `41.4%` | `58.6%` | `0.71` | 14,740.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.05%` | `49.95%` | `1.00` | 583,490.00 USD |
| `1H` | `Crypto.com` | `2.24%` | `97.76%` | `0.02` | 27.64 USD |
| `1H` | `WhiteBIT` | `86.3%` | `13.7%` | `6.30` | 85,350.00 USD |
| `1H` | `HTX` | `22.12%` | `77.88%` | `0.28` | 1,480.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `92.8%` | `7.2%` | `12.89` | 7,090.00 USD |
| `1H` | `Aster` | `23.02%` | `76.98%` | `0.30` | 43.30 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `31.82%` | `68.18%` | `0.47` | 2,840.00 USD |
| `1H` | `Whale Positions` | `54.88%` | `45.12%` | `1.22` | 1,120,000.00 USD |
| `1H` | `Global Accounts` | `50.19%` | `49.81%` | `1.01` | 3,600,000.00 USD |
| `4H` | `OP` | `46.14%` | `53.86%` | `0.86` | 18,830,000.00 USD |
| `4H` | `Binance` | `47.6%` | `52.4%` | `0.91` | 6,090,000.00 USD |
| `4H` | `OKX` | `47.51%` | `52.49%` | `0.91` | 1,510,000.00 USD |
| `4H` | `Bybit` | `50.99%` | `49.01%` | `1.04` | 1,800,000.00 USD |
| `4H` | `KuCoin` | `49.86%` | `50.14%` | `0.99` | 2,150,000.00 USD |
| `4H` | `Gate` | `50.9%` | `49.1%` | `1.04` | 394,740.00 USD |
| `4H` | `Bitget` | `46.91%` | `53.09%` | `0.88` | 1,510,000.00 USD |
| `4H` | `BingX` | `27.96%` | `72.04%` | `0.39` | 2,320,000.00 USD |
| `4H` | `MEXC` | `45.76%` | `54.24%` | `0.84` | 988,390.00 USD |
| `4H` | `Bitunix` | `39.62%` | `60.38%` | `0.66` | 255,870.00 USD |
| `4H` | `Hyperliquid` | `48.39%` | `51.61%` | `0.94` | 305,230.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.78%` | `50.22%` | `0.99` | 942,540.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `70.42%` | `29.58%` | `2.38` | 416,890.00 USD |
| `4H` | `HTX` | `54.43%` | `45.57%` | `1.19` | 4,560.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `4.71%` | `95.29%` | `0.05` | 1,130.00 USD |
| `4H` | `Aster` | `41.49%` | `58.51%` | `0.71` | 131,180.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `16.19%` | `83.81%` | `0.19` | 6,130.00 USD |
| `4H` | `Whale Positions` | `47.6%` | `52.4%` | `0.91` | 6,090,000.00 USD |
| `4H` | `Global Accounts` | `46.14%` | `53.86%` | `0.86` | 18,830,000.00 USD |


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
| `5m` | -6,150.00 USD | -6,270.00 USD | **`DISTRIBUTION`** |
| `15m` | -20,710.00 USD | -56,340.00 USD | **`DISTRIBUTION`** |
| `30m` | -30,230.00 USD | -57,080.00 USD | **`DISTRIBUTION`** |
| `1h` | 23,110.00 USD | 124,950.00 USD | **`ACCUMULATION`** |
| `2h` | -1,140.00 USD | 199,610.00 USD | **`ACCUMULATION`** |
| `4h` | -2,770.00 USD | 575,330.00 USD | **`ACCUMULATION`** |
| `6h` | -95,740.00 USD | 95,460.00 USD | **`DISTRIBUTION`** |
| `8h` | -110,220.00 USD | -1,520,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 476,530.00 USD | -1,280,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 274,060.00 USD | -3,570,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -195,450.00 USD | -13,030,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,350,000.00 USD | -82,960,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-6.15K` | 15m=`-20.71K` | 1h=`+23.11K` | 24h=`+274.06K`
* Futures Capital Netflows: 5m=`-6.27K` | 15m=`-56.34K` | 1h=`+124.95K` | 24h=`-3.57M`
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
