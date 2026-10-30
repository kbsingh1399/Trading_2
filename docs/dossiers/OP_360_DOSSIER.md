# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 10:37:50 IST` (`2026-10-30 05:07:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1010` | `0.1013` | `0.1009` | `0.1012` | `1,964,041` | 198,576.65 USD | 84,811.06 USD | `+42.71%` | -1,903,286.96 USD | `+1.63` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.1012` | `0.1013` | `0.1010` | `0.1012` | `1,605,100` | 162,490.80 USD | 888.58 USD | `+0.55%` | -1,902,398.39 USD | `-0.29` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.1012` | `0.1018` | `0.1012` | `0.1017` | `1,872,440` | 190,116.62 USD | 44,617.67 USD | `+23.47%` | -1,857,780.71 USD | `+0.81` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1004` | `0.1009` | `0.1002` | `0.1008` | `3,198,294` | 321,574.58 USD | 96,000.52 USD | `+29.85%` | -2,067,682.09 USD | `+0.67` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1009` | `0.1013` | `0.1006` | `0.1012` | `5,910,996` | 597,276.02 USD | 89,511.23 USD | `+14.99%` | -1,978,170.87 USD | `+0.61` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1012` | `0.1018` | `0.1012` | `0.1017` | `1,881,464` | 191,034.11 USD | 43,854.43 USD | `+22.96%` | -1,934,316.44 USD | `+0.39` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.0981` | `0.0995` | `0.0970` | `0.0993` | `30,519,947` | 2,992,768.64 USD | -441,148.19 USD | `-14.74%` | -2,239,239.62 USD | `-0.72` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.0993` | `0.1013` | `0.0988` | `0.1012` | `16,216,904` | 1,626,948.60 USD | 318,721.56 USD | `+19.59%` | -1,920,518.05 USD | `+0.94` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.1012` | `0.1018` | `0.1012` | `0.1017` | `1,883,027` | 191,192.93 USD | 44,013.24 USD | `+23.02%` | -1,876,504.81 USD | `+0.34` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -1,009,359.71 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,347,386.10 USD | `-1.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1018` | `0.0988` | `0.1017` | `18,098,369` | 1,817,982.71 USD | 362,575.99 USD | `+19.94%` | -1,984,810.11 USD | `+0.95` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | 483,978.43 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | 307,838.15 USD | `-1.31` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -1,009,359.71 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0993` | `154,779,937` | 15,105,414.22 USD | -1,338,026.39 USD | `-8.86%` | -2,347,386.10 USD | `-1.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0993` | `0.1018` | `0.0988` | `0.1017` | `18,098,369` | 1,817,982.71 USD | 362,575.99 USD | `+19.94%` | -1,984,810.11 USD | `+0.95` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:34:32 IST` |

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
| `7D` | `Long Liquidation` | `0.0827` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 8,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0830` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 28.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0860` | 1,900,000.00 USD | 1,900,000.00 USD | 1,880.00 USD | 0.00 USD | 2,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0863` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 1,880.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0866` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 1,980.00 USD | 15,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0869` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0871` | 1,550,000.00 USD | 1,550,000.00 USD | 1,740.00 USD | 0.00 USD | 1,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0872` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 1,200.00 USD | 5,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0873` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 680.22 USD | 5,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0875` | 1,540,000.00 USD | 1,540,000.00 USD | 9,010.00 USD | 437.13 USD | 3,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0875` | 1,860,000.00 USD | 1,860,000.00 USD | 6,010.00 USD | 0.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0877` | 1,530,000.00 USD | 1,530,000.00 USD | 4,660.00 USD | 3,520.00 USD | 5,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0878` | 1,850,000.00 USD | 1,850,000.00 USD | 9,200.00 USD | 7,660.00 USD | 28,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0879` | 1,520,000.00 USD | 1,520,000.00 USD | 2,950.00 USD | 2,000.00 USD | 9,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0881` | 1,500,000.00 USD | 1,500,000.00 USD | 1,670.00 USD | 1,920.00 USD | 530.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0881` | 1,810,000.00 USD | 1,810,000.00 USD | 9,390.00 USD | 2,660.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0883` | 1,500,000.00 USD | 1,500,000.00 USD | 2,370.00 USD | 4,960.00 USD | 9,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0884` | 1,780,000.00 USD | 1,780,000.00 USD | 7,040.00 USD | 8,030.00 USD | 21,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0885` | 1,480,000.00 USD | 1,480,000.00 USD | 4,650.00 USD | 1,040.00 USD | 4,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0887` | 1,470,000.00 USD | 1,470,000.00 USD | 2,910.00 USD | 1,540.00 USD | 8,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0887` | 1,740,000.00 USD | 1,740,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0889` | 1,460,000.00 USD | 1,460,000.00 USD | 727.20 USD | 1,680.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0890` | 1,710,000.00 USD | 1,710,000.00 USD | 14,610.00 USD | 5,880.00 USD | 13,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0891` | 1,450,000.00 USD | 1,450,000.00 USD | 755.35 USD | 1,580.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0893` | 1,450,000.00 USD | 1,450,000.00 USD | 983.61 USD | 0.00 USD | 542.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0893` | 1,680,000.00 USD | 1,680,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0895` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 1,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0896` | 1,660,000.00 USD | 1,660,000.00 USD | 5,760.00 USD | 2,110.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0897` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 1,330.00 USD | 11.07 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0899` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 21.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0899` | 1,640,000.00 USD | 1,640,000.00 USD | 3,390.00 USD | 927.82 USD | 4,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0901` | 1,440,000.00 USD | 1,440,000.00 USD | 3,320.00 USD | 1,000.00 USD | 18.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0902` | 1,630,000.00 USD | 1,630,000.00 USD | 2,270.00 USD | 910.78 USD | 1,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0903` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 3,440.00 USD | 2,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0905` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 486.35 USD | 2,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0905` | 1,630,000.00 USD | 1,630,000.00 USD | 10,350.00 USD | 996.61 USD | 4,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0907` | 1,430,000.00 USD | 1,430,000.00 USD | 1,250.00 USD | 245.42 USD | 2,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0908` | 1,610,000.00 USD | 1,610,000.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0909` | 1,430,000.00 USD | 1,430,000.00 USD | 938.76 USD | 1,360.00 USD | 778.75 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0911` | 1,420,000.00 USD | 1,420,000.00 USD | 5,580.00 USD | 1,450.00 USD | 27.56 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0911` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0913` | 1,420,000.00 USD | 1,420,000.00 USD | 1,930.00 USD | 465.26 USD | 787.25 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0914` | 1,600,000.00 USD | 1,600,000.00 USD | 1,670.00 USD | 903.90 USD | 45.81 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0915` | 1,410,000.00 USD | 1,410,000.00 USD | 6,590.00 USD | 2,510.00 USD | 55.57 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0917` | 1,400,000.00 USD | 1,400,000.00 USD | 3,850.00 USD | 3,470.00 USD | 48.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0917` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0919` | 1,400,000.00 USD | 1,400,000.00 USD | 4,980.00 USD | 504.78 USD | 19,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0920` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 223.39 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0921` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 750.63 USD | 3,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0923` | 1,370,000.00 USD | 1,370,000.00 USD | 1,410.00 USD | 1,920.00 USD | 22,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0923` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 4,940.00 USD | 43,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0925` | 1,340,000.00 USD | 1,340,000.00 USD | 3,270.00 USD | 3,340.00 USD | 26,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0926` | 1,540,000.00 USD | 1,540,000.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0929` | 1,310,000.00 USD | 1,310,000.00 USD | 4,360.00 USD | 1,190.00 USD | 16.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0929` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0931` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 7,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0932` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 12,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0933` | 1,290,000.00 USD | 1,290,000.00 USD | 16,500.00 USD | 0.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0935` | 1,270,000.00 USD | 1,270,000.00 USD | 8,990.00 USD | 7,300.00 USD | 15,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0935` | 1,510,000.00 USD | 1,510,000.00 USD | 19,560.00 USD | 8,160.00 USD | 31,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0937` | 1,240,000.00 USD | 1,240,000.00 USD | 4,580.00 USD | 6,660.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0938` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 248.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0939` | 1,210,000.00 USD | 1,210,000.00 USD | 3,590.00 USD | 2,140.00 USD | 44,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0941` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 9,410.00 USD | 21,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0941` | 1,450,000.00 USD | 1,450,000.00 USD | 16,100.00 USD | 18,340.00 USD | 90,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0943` | 1,130,000.00 USD | 1,130,000.00 USD | 3,500.00 USD | 10,920.00 USD | 30,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0944` | 1,330,000.00 USD | 1,330,000.00 USD | 8,040.00 USD | 2,010.00 USD | 37,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0945` | 1,090,000.00 USD | 1,090,000.00 USD | 15,750.00 USD | 6,510.00 USD | 44,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0947` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 962.66 USD | 91.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0947` | 1,280,000.00 USD | 1,280,000.00 USD | 2,200.00 USD | 1,810.00 USD | 112.06 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0949` | 1,020,000.00 USD | 1,020,000.00 USD | 12,180.00 USD | 5,770.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0950` | 1,280,000.00 USD | 1,280,000.00 USD | 3,770.00 USD | 9,700.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0951` | 997,760.00 USD | 997,760.00 USD | 0.00 USD | 2,030.00 USD | 19,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0953` | 975,760.00 USD | 975,760.00 USD | 33,000.00 USD | 4,360.00 USD | 6,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0953` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 8,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0955` | 931,620.00 USD | 931,620.00 USD | 17,990.00 USD | 14,600.00 USD | 31,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0956` | 1,230,000.00 USD | 1,230,000.00 USD | 39,120.00 USD | 13,670.00 USD | 51,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0957` | 867,410.00 USD | 867,410.00 USD | 16,340.00 USD | 6,740.00 USD | 48,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0959` | 795,670.00 USD | 795,670.00 USD | 0.00 USD | 3,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0959` | 1,130,000.00 USD | 1,130,000.00 USD | 28,110.00 USD | 0.00 USD | 21,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0961` | 792,570.00 USD | 792,570.00 USD | 8,920.00 USD | 23,950.00 USD | 23,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0962` | 1,080,000.00 USD | 1,080,000.00 USD | 12,340.00 USD | 16,920.00 USD | 94,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0963` | 736,490.00 USD | 736,490.00 USD | 23,240.00 USD | 11,750.00 USD | 11,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0965` | 689,520.00 USD | 689,520.00 USD | 8,250.00 USD | 5,890.00 USD | 20,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0965` | 951,510.00 USD | 951,510.00 USD | 0.00 USD | 6,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0967` | 654,980.00 USD | 654,980.00 USD | 0.00 USD | 1,960.00 USD | 773.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0968` | 945,100.00 USD | 945,100.00 USD | 7,490.00 USD | 0.00 USD | 58,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0969` | 652,250.00 USD | 652,250.00 USD | 6,930.00 USD | 7,530.00 USD | 8,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0971` | 629,700.00 USD | 629,700.00 USD | 2,840.00 USD | 4,070.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 878,690.00 USD | 878,690.00 USD | 0.00 USD | 7,090.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0973` | 612,550.00 USD | 612,550.00 USD | 1,440.00 USD | 9,470.00 USD | 963.13 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0974` | 866,590.00 USD | 866,590.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0979` | 600,680.00 USD | 600,680.00 USD | 0.00 USD | 0.00 USD | 21,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0981` | 579,560.00 USD | 579,560.00 USD | 3,830.00 USD | 5,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0983` | 570,720.00 USD | 570,720.00 USD | 0.00 USD | 4,040.00 USD | 5.60 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0985` | 566,670.00 USD | 566,670.00 USD | 0.00 USD | 0.00 USD | 4.44 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0986` | 850,280.00 USD | 850,280.00 USD | 0.00 USD | 12,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0987` | 566,670.00 USD | 566,670.00 USD | 22,740.00 USD | 3,920.00 USD | 11,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0989` | 528,220.00 USD | 528,220.00 USD | 2,180.00 USD | 1,540.00 USD | 21,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 837,960.00 USD | 837,960.00 USD | 17,640.00 USD | 7,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0991` | 502,770.00 USD | 502,770.00 USD | 69,940.00 USD | 0.00 USD | 760.65 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0992` | 812,500.00 USD | 812,500.00 USD | 27,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0993` | 432,080.00 USD | 432,080.00 USD | 23,960.00 USD | 1,510.00 USD | 43,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0995` | 363,140.00 USD | 363,140.00 USD | 17,890.00 USD | 898.20 USD | 50,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 785,360.00 USD | 785,360.00 USD | 63,330.00 USD | 0.00 USD | 76,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0997` | 294,100.00 USD | 294,100.00 USD | 17,900.00 USD | 5,840.00 USD | 53,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0998` | 645,990.00 USD | 645,990.00 USD | 28,450.00 USD | 17,040.00 USD | 135,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0999` | 216,690.00 USD | 216,690.00 USD | 0.00 USD | 10,180.00 USD | 47,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1001` | 158,610.00 USD | 158,610.00 USD | 0.00 USD | 0.00 USD | 42,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 465,230.00 USD | 465,230.00 USD | 76,560.00 USD | 25,570.00 USD | 107,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1003` | 116,090.00 USD | 116,090.00 USD | 23,240.00 USD | 0.00 USD | 27,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1004` | 255,120.00 USD | 255,120.00 USD | 22,470.00 USD | 0.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1005` | 65,650.00 USD | 65,650.00 USD | 8,250.00 USD | 5,890.00 USD | 20,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1007` | 31,120.00 USD | 31,120.00 USD | 4,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 209,220.00 USD | 209,220.00 USD | 20,870.00 USD | 3,080.00 USD | 100,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1009` | 26,760.00 USD | 26,760.00 USD | 6,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1010` | 85,040.00 USD | 85,040.00 USD | 17,340.00 USD | 13,670.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1011` | 19,830.00 USD | 19,830.00 USD | 0.00 USD | 4,070.00 USD | 15,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1013` | 10,500.00 USD | 10,500.00 USD | 0.00 USD | 0.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1013` | 88,650.00 USD | 88,650.00 USD | 34,830.00 USD | 28,370.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1013` | 177,310.00 USD | 177,310.00 USD | 34,830.00 USD | 28,370.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1015` | 29,530.00 USD | 29,530.00 USD | 4,580.00 USD | 1,220.00 USD | 13,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1016` | 192,890.00 USD | 192,890.00 USD | 15,440.00 USD | 0.00 USD | 142.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1017` | 49,160.00 USD | 49,160.00 USD | 3,590.00 USD | 4,930.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1019` | 58,570.00 USD | 58,570.00 USD | 0.00 USD | 9,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1019` | 248,120.00 USD | 248,120.00 USD | 26,150.00 USD | 8,460.00 USD | 20,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1021` | 98,190.00 USD | 98,190.00 USD | 13,630.00 USD | 12,100.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1022` | 313,920.00 USD | 313,920.00 USD | 18,100.00 USD | 10,260.00 USD | 37,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1023` | 144,100.00 USD | 144,100.00 USD | 15,750.00 USD | 10,470.00 USD | 19,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1025` | 148,810.00 USD | 148,810.00 USD | 3,740.00 USD | 962.66 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1025` | 320,260.00 USD | 320,260.00 USD | 1,550.00 USD | 4,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1027` | 166,440.00 USD | 166,440.00 USD | 3,430.00 USD | 3,920.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1028` | 352,150.00 USD | 352,150.00 USD | 3,800.00 USD | 4,390.00 USD | 23,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1029` | 188,210.00 USD | 188,210.00 USD | 6,870.00 USD | 7,400.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1031` | 251,600.00 USD | 251,600.00 USD | 33,590.00 USD | 5,770.00 USD | 24,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1031` | 381,510.00 USD | 381,510.00 USD | 19,560.00 USD | 9,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1033` | 287,500.00 USD | 287,500.00 USD | 2,890.00 USD | 9,230.00 USD | 23,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1034` | 415,720.00 USD | 415,720.00 USD | 18,920.00 USD | 15,180.00 USD | 106.77 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1035` | 313,800.00 USD | 313,800.00 USD | 15,150.00 USD | 11,130.00 USD | 17.34 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1037` | 363,070.00 USD | 363,070.00 USD | 36,550.00 USD | 12,700.00 USD | 24.05 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1037` | 429,250.00 USD | 429,250.00 USD | 2,710.00 USD | 10,710.00 USD | 108.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1039` | 383,290.00 USD | 383,290.00 USD | 6,500.00 USD | 8,500.00 USD | 5,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1040` | 476,850.00 USD | 476,850.00 USD | 5,940.00 USD | 10,300.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1041` | 431,290.00 USD | 431,290.00 USD | 11,520.00 USD | 16,860.00 USD | 19,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1043` | 465,430.00 USD | 465,430.00 USD | 0.00 USD | 9,960.00 USD | 24,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1043` | 498,790.00 USD | 498,790.00 USD | 15,960.00 USD | 5,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1045` | 474,490.00 USD | 474,490.00 USD | 1,870.00 USD | 2,240.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1046` | 571,160.00 USD | 571,160.00 USD | 0.00 USD | 12,200.00 USD | 60,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1047` | 548,300.00 USD | 548,300.00 USD | 28,580.00 USD | 8,010.00 USD | 37,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1049` | 666,100.00 USD | 666,100.00 USD | 33,450.00 USD | 15,310.00 USD | 69,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1049` | 695,650.00 USD | 695,650.00 USD | 34,790.00 USD | 6,530.00 USD | 83,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1051` | 733,820.00 USD | 733,820.00 USD | 33,210.00 USD | 10,280.00 USD | 24,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1052` | 873,500.00 USD | 873,500.00 USD | 28,200.00 USD | 24,160.00 USD | 125,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1053` | 837,740.00 USD | 837,740.00 USD | 36,480.00 USD | 11,370.00 USD | 56,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1055` | 972,200.00 USD | 972,200.00 USD | 51,530.00 USD | 26,280.00 USD | 56,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1055` | 1,250,000.00 USD | 1,250,000.00 USD | 122,840.00 USD | 44,430.00 USD | 211,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1057` | 1,030,000.00 USD | 1,030,000.00 USD | 14,080.00 USD | 11,900.00 USD | 32,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1058` | 1,620,000.00 USD | 1,620,000.00 USD | 105,620.00 USD | 58,510.00 USD | 202,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1059` | 1,150,000.00 USD | 1,150,000.00 USD | 35,730.00 USD | 4,960.00 USD | 77,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1061` | 1,240,000.00 USD | 1,240,000.00 USD | 30,060.00 USD | 1,890.00 USD | 60,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1061` | 1,880,000.00 USD | 1,880,000.00 USD | 75,540.00 USD | 69,160.00 USD | 118,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1063` | 1,330,000.00 USD | 1,330,000.00 USD | 25,200.00 USD | 2,030.00 USD | 65,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1064` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 52,580.00 USD | 177,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1065` | 1,360,000.00 USD | 1,360,000.00 USD | 1,740.00 USD | 2,630.00 USD | 24,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1067` | 1,420,000.00 USD | 1,420,000.00 USD | 8,230.00 USD | 1,320.00 USD | 44,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1067` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 51,740.00 USD | 143,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1069` | 1,500,000.00 USD | 1,500,000.00 USD | 14,770.00 USD | 5,440.00 USD | 62,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1070` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 57,770.00 USD | 134,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1071` | 1,530,000.00 USD | 1,530,000.00 USD | 2,550.00 USD | 5,850.00 USD | 20,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1073` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1073` | 2,540,000.00 USD | 2,540,000.00 USD | 7,820.00 USD | 20,440.00 USD | 10,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1075` | 1,540,000.00 USD | 1,540,000.00 USD | 1,440.00 USD | 857.82 USD | 3,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1076` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 22,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1077` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 619.42 USD | 77.28 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1079` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 4,300.00 USD | 21,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1079` | 2,580,000.00 USD | 2,580,000.00 USD | 5,620.00 USD | 3,380.00 USD | 10,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1081` | 1,570,000.00 USD | 1,570,000.00 USD | 4,650.00 USD | 732.74 USD | 2,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1082` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 89.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1083` | 1,600,000.00 USD | 1,600,000.00 USD | 9,160.00 USD | 6,710.00 USD | 10,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1085` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 385.06 USD | 65,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1085` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1087` | 1,740,000.00 USD | 1,740,000.00 USD | 28,490.00 USD | 2,510.00 USD | 44,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1088` | 2,600,000.00 USD | 2,600,000.00 USD | 5,290.00 USD | 1,420.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1089` | 1,770,000.00 USD | 1,770,000.00 USD | 29,650.00 USD | 1,580.00 USD | 3,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1091` | 1,810,000.00 USD | 1,810,000.00 USD | 33,700.00 USD | 0.00 USD | 16.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1091` | 2,620,000.00 USD | 2,620,000.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1093` | 1,830,000.00 USD | 1,830,000.00 USD | 15,480.00 USD | 1,080.00 USD | 222.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1094` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 1,500.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1095` | 1,850,000.00 USD | 1,850,000.00 USD | 4,110.00 USD | 1,890.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1097` | 1,890,000.00 USD | 1,890,000.00 USD | 7,260.00 USD | 2,530.00 USD | 22,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1097` | 2,650,000.00 USD | 2,650,000.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1099` | 1,890,000.00 USD | 1,890,000.00 USD | 6,130.00 USD | 1,940.00 USD | 5.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1100` | 2,680,000.00 USD | 2,680,000.00 USD | 11,470.00 USD | 0.00 USD | 21,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1101` | 1,910,000.00 USD | 1,910,000.00 USD | 5,570.00 USD | 3,820.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1103` | 1,920,000.00 USD | 1,920,000.00 USD | 3,540.00 USD | 6,900.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 2,730,000.00 USD | 2,730,000.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1105` | 1,940,000.00 USD | 1,940,000.00 USD | 3,380.00 USD | 4,740.00 USD | 10,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1106` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 22,880.00 USD | 16,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1107` | 1,990,000.00 USD | 1,990,000.00 USD | 3,110.00 USD | 13,200.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1109` | 2,000,000.00 USD | 2,000,000.00 USD | 2,110.00 USD | 1,370.00 USD | 2,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1111` | 2,000,000.00 USD | 2,000,000.00 USD | 5,200.00 USD | 996.46 USD | 96.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1112` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1113` | 2,060,000.00 USD | 2,060,000.00 USD | 21,390.00 USD | 5,880.00 USD | 29,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1115` | 2,070,000.00 USD | 2,070,000.00 USD | 6,690.00 USD | 465.26 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1117` | 2,130,000.00 USD | 2,130,000.00 USD | 2,060.00 USD | 23,600.00 USD | 34,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1118` | 2,870,000.00 USD | 2,870,000.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1119` | 2,210,000.00 USD | 2,210,000.00 USD | 33,110.00 USD | 8,660.00 USD | 36,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 2,930,000.00 USD | 2,930,000.00 USD | 17,760.00 USD | 0.00 USD | 38,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1124` | 3,030,000.00 USD | 3,030,000.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1127` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1130` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 24,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 3,110,000.00 USD | 3,110,000.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1136` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1139` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1142` | 3,150,000.00 USD | 3,150,000.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 3,390,000.00 USD | 3,390,000.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1148` | 3,570,000.00 USD | 3,570,000.00 USD | 9,880.00 USD | 0.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 3,840,000.00 USD | 3,840,000.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1154` | 4,310,000.00 USD | 4,310,000.00 USD | 243,190.00 USD | 26,970.00 USD | 202,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 4,610,000.00 USD | 4,610,000.00 USD | 173,120.00 USD | 25,290.00 USD | 98,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1160` | 4,880,000.00 USD | 4,880,000.00 USD | 131,160.00 USD | 32,830.00 USD | 109,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 5,170,000.00 USD | 5,170,000.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1166` | 5,390,000.00 USD | 5,390,000.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 5,610,000.00 USD | 5,610,000.00 USD | 82,770.00 USD | 26,150.00 USD | 117,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1172` | 5,740,000.00 USD | 5,740,000.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 5,920,000.00 USD | 5,920,000.00 USD | 75,590.00 USD | 17,930.00 USD | 81,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1178` | 6,090,000.00 USD | 6,090,000.00 USD | 89,510.00 USD | 25,350.00 USD | 60,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 6,180,000.00 USD | 6,180,000.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1184` | 6,240,000.00 USD | 6,240,000.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 6,330,000.00 USD | 6,330,000.00 USD | 5,620.00 USD | 17,120.00 USD | 59,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1190` | 6,470,000.00 USD | 6,470,000.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 6,550,000.00 USD | 6,550,000.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1196` | 6,610,000.00 USD | 6,610,000.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 6,680,000.00 USD | 6,680,000.00 USD | 2,470.00 USD | 13,190.00 USD | 52,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1202` | 6,870,000.00 USD | 6,870,000.00 USD | 138,430.00 USD | 21,430.00 USD | 32,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 7,080,000.00 USD | 7,080,000.00 USD | 117,120.00 USD | 48,510.00 USD | 40,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1208` | 7,180,000.00 USD | 7,180,000.00 USD | 39,480.00 USD | 20,870.00 USD | 39,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 7,350,000.00 USD | 7,350,000.00 USD | 72,500.00 USD | 25,920.00 USD | 76,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1214` | 7,470,000.00 USD | 7,470,000.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 7,520,000.00 USD | 7,520,000.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1220` | 7,620,000.00 USD | 7,620,000.00 USD | 34,050.00 USD | 6,400.00 USD | 54,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 7,740,000.00 USD | 7,740,000.00 USD | 73,610.00 USD | 15,050.00 USD | 37,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1226` | 7,820,000.00 USD | 7,820,000.00 USD | 45,920.00 USD | 19,760.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 7,940,000.00 USD | 7,940,000.00 USD | 63,930.00 USD | 33,570.00 USD | 28,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1232` | 8,040,000.00 USD | 8,040,000.00 USD | 51,420.00 USD | 12,080.00 USD | 37,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1235` | 8,080,000.00 USD | 8,080,000.00 USD | 15,040.00 USD | 5,390.00 USD | 16,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1237` | 8,090,000.00 USD | 8,090,000.00 USD | 4,080.00 USD | 2,760.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1805` | 18,490.00 USD | 18,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

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
| `7D` | `0.0827` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 8,590.00 USD |
| `7D` | `0.0830` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 28.49 USD |
| `7D` | `0.0860` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 1,880.00 USD | 0.00 USD | 2,160.00 USD |
| `7D` | `0.0863` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 0.00 USD | 1,880.00 USD | 7,040.00 USD |
| `7D` | `0.0866` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 0.00 USD | 1,980.00 USD | 15,400.00 USD |
| `7D` | `0.0869` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 2,900.00 USD |
| `1D` | `0.0871` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 1,740.00 USD | 0.00 USD | 1,040.00 USD |
| `7D` | `0.0872` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 0.00 USD | 1,200.00 USD | 5,830.00 USD |
| `1D` | `0.0873` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 0.00 USD | 680.22 USD | 5,950.00 USD |
| `1D` | `0.0875` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 9,010.00 USD | 437.13 USD | 3,520.00 USD |
| `7D` | `0.0875` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 6,010.00 USD | 0.00 USD | 5,780.00 USD |
| `1D` | `0.0877` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 4,660.00 USD | 3,520.00 USD | 5,830.00 USD |
| `7D` | `0.0878` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 9,200.00 USD | 7,660.00 USD | 28,720.00 USD |
| `1D` | `0.0879` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 2,950.00 USD | 2,000.00 USD | 9,430.00 USD |
| `1D` | `0.0881` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 1,670.00 USD | 1,920.00 USD | 530.96 USD |
| `7D` | `0.0881` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 9,390.00 USD | 2,660.00 USD | 12,940.00 USD |
| `1D` | `0.0883` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 2,370.00 USD | 4,960.00 USD | 9,970.00 USD |
| `7D` | `0.0884` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 7,040.00 USD | 8,030.00 USD | 21,730.00 USD |
| `1D` | `0.0885` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 4,650.00 USD | 1,040.00 USD | 4,920.00 USD |
| `1D` | `0.0887` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 2,910.00 USD | 1,540.00 USD | 8,120.00 USD |
| `7D` | `0.0887` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD |
| `1D` | `0.0889` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 727.20 USD | 1,680.00 USD | 2,110.00 USD |
| `7D` | `0.0890` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 14,610.00 USD | 5,880.00 USD | 13,160.00 USD |
| `1D` | `0.0891` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 755.35 USD | 1,580.00 USD | 3,210.00 USD |
| `1D` | `0.0893` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 983.61 USD | 0.00 USD | 542.23 USD |
| `7D` | `0.0893` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD |
| `1D` | `0.0895` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 1,080.00 USD | 0.00 USD |
| `7D` | `0.0896` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 5,760.00 USD | 2,110.00 USD | 6,870.00 USD |
| `1D` | `0.0897` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 1,330.00 USD | 11.07 USD |
| `1D` | `0.0899` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 21.52 USD |
| `7D` | `0.0899` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 3,390.00 USD | 927.82 USD | 4,520.00 USD |
| `1D` | `0.0901` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 3,320.00 USD | 1,000.00 USD | 18.94 USD |
| `7D` | `0.0902` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 2,270.00 USD | 910.78 USD | 1,320.00 USD |
| `1D` | `0.0903` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 3,440.00 USD | 2,230.00 USD |
| `1D` | `0.0905` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 0.00 USD | 486.35 USD | 2,150.00 USD |
| `7D` | `0.0905` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 10,350.00 USD | 996.61 USD | 4,170.00 USD |
| `1D` | `0.0907` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 1,250.00 USD | 245.42 USD | 2,710.00 USD |
| `7D` | `0.0908` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD |
| `1D` | `0.0909` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 938.76 USD | 1,360.00 USD | 778.75 USD |
| `1D` | `0.0911` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 5,580.00 USD | 1,450.00 USD | 27.56 USD |
| `7D` | `0.0911` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD |
| `1D` | `0.0913` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 1,930.00 USD | 465.26 USD | 787.25 USD |
| `7D` | `0.0914` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,670.00 USD | 903.90 USD | 45.81 USD |
| `1D` | `0.0915` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 6,590.00 USD | 2,510.00 USD | 55.57 USD |
| `1D` | `0.0917` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 3,850.00 USD | 3,470.00 USD | 48.95 USD |
| `7D` | `0.0917` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD |
| `1D` | `0.0919` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 4,980.00 USD | 504.78 USD | 19,100.00 USD |
| `7D` | `0.0920` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 223.39 USD |
| `1D` | `0.0921` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 0.00 USD | 750.63 USD | 3,780.00 USD |
| `1D` | `0.0923` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,410.00 USD | 1,920.00 USD | 22,090.00 USD |
| `7D` | `0.0923` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 0.00 USD | 4,940.00 USD | 43,850.00 USD |
| `1D` | `0.0925` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 3,270.00 USD | 3,340.00 USD | 26,400.00 USD |
| `7D` | `0.0926` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD |
| `1D` | `0.0929` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 4,360.00 USD | 1,190.00 USD | 16.60 USD |
| `7D` | `0.0929` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD |
| `1D` | `0.0931` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 7,430.00 USD |
| `7D` | `0.0932` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 12,290.00 USD |
| `1D` | `0.0933` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 16,500.00 USD | 0.00 USD | 10,200.00 USD |
| `1D` | `0.0935` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 8,990.00 USD | 7,300.00 USD | 15,690.00 USD |
| `7D` | `0.0935` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 19,560.00 USD | 8,160.00 USD | 31,940.00 USD |
| `1D` | `0.0937` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 4,580.00 USD | 6,660.00 USD | 13,310.00 USD |
| `7D` | `0.0938` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 248.29 USD |
| `1D` | `0.0939` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 3,590.00 USD | 2,140.00 USD | 44,370.00 USD |
| `1D` | `0.0941` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 0.00 USD | 9,410.00 USD | 21,110.00 USD |
| `7D` | `0.0941` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 16,100.00 USD | 18,340.00 USD | 90,280.00 USD |
| `1D` | `0.0943` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 3,500.00 USD | 10,920.00 USD | 30,390.00 USD |
| `7D` | `0.0944` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 8,040.00 USD | 2,010.00 USD | 37,480.00 USD |
| `1D` | `0.0945` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 15,750.00 USD | 6,510.00 USD | 44,350.00 USD |
| `1D` | `0.0947` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 0.00 USD | 962.66 USD | 91.75 USD |
| `7D` | `0.0947` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 2,200.00 USD | 1,810.00 USD | 112.06 USD |
| `1D` | `0.0949` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 12,180.00 USD | 5,770.00 USD | 2,910.00 USD |
| `7D` | `0.0950` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 3,770.00 USD | 9,700.00 USD | 26,990.00 USD |
| `1D` | `0.0951` | 997,760.00 USD | 0.00 USD | 997,760.00 USD | 0.00 USD | 2,030.00 USD | 19,960.00 USD |
| `1D` | `0.0953` | 975,760.00 USD | 0.00 USD | 975,760.00 USD | 33,000.00 USD | 4,360.00 USD | 6,780.00 USD |
| `7D` | `0.0953` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 8,150.00 USD | 0.00 USD |
| `1D` | `0.0955` | 931,620.00 USD | 0.00 USD | 931,620.00 USD | 17,990.00 USD | 14,600.00 USD | 31,630.00 USD |
| `7D` | `0.0956` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 39,120.00 USD | 13,670.00 USD | 51,090.00 USD |
| `1D` | `0.0957` | 867,410.00 USD | 0.00 USD | 867,410.00 USD | 16,340.00 USD | 6,740.00 USD | 48,660.00 USD |
| `1D` | `0.0959` | 795,670.00 USD | 0.00 USD | 795,670.00 USD | 0.00 USD | 3,100.00 USD | 0.00 USD |
| `7D` | `0.0959` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 28,110.00 USD | 0.00 USD | 21,450.00 USD |
| `1D` | `0.0961` | 792,570.00 USD | 0.00 USD | 792,570.00 USD | 8,920.00 USD | 23,950.00 USD | 23,220.00 USD |
| `7D` | `0.0962` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 12,340.00 USD | 16,920.00 USD | 94,970.00 USD |
| `1D` | `0.0963` | 736,490.00 USD | 0.00 USD | 736,490.00 USD | 23,240.00 USD | 11,750.00 USD | 11,980.00 USD |
| `1D` | `0.0965` | 689,520.00 USD | 0.00 USD | 689,520.00 USD | 8,250.00 USD | 5,890.00 USD | 20,390.00 USD |
| `7D` | `0.0965` | 951,510.00 USD | 0.00 USD | 951,510.00 USD | 0.00 USD | 6,410.00 USD | 0.00 USD |
| `1D` | `0.0967` | 654,980.00 USD | 0.00 USD | 654,980.00 USD | 0.00 USD | 1,960.00 USD | 773.14 USD |
| `7D` | `0.0968` | 945,100.00 USD | 0.00 USD | 945,100.00 USD | 7,490.00 USD | 0.00 USD | 58,910.00 USD |
| `1D` | `0.0969` | 652,250.00 USD | 0.00 USD | 652,250.00 USD | 6,930.00 USD | 7,530.00 USD | 8,080.00 USD |
| `1D` | `0.0971` | 629,700.00 USD | 0.00 USD | 629,700.00 USD | 2,840.00 USD | 4,070.00 USD | 10,240.00 USD |
| `7D` | `0.0971` | 878,690.00 USD | 0.00 USD | 878,690.00 USD | 0.00 USD | 7,090.00 USD | 5,010.00 USD |
| `1D` | `0.0973` | 612,550.00 USD | 0.00 USD | 612,550.00 USD | 1,440.00 USD | 9,470.00 USD | 963.13 USD |
| `7D` | `0.0974` | 866,590.00 USD | 0.00 USD | 866,590.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD |
| `1D` | `0.0979` | 600,680.00 USD | 0.00 USD | 600,680.00 USD | 0.00 USD | 0.00 USD | 21,110.00 USD |
| `1D` | `0.0981` | 579,560.00 USD | 0.00 USD | 579,560.00 USD | 3,830.00 USD | 5,020.00 USD | 0.00 USD |
| `1D` | `0.0983` | 570,720.00 USD | 0.00 USD | 570,720.00 USD | 0.00 USD | 4,040.00 USD | 5.60 USD |
| `1D` | `0.0985` | 566,670.00 USD | 0.00 USD | 566,670.00 USD | 0.00 USD | 0.00 USD | 4.44 USD |
| `7D` | `0.0986` | 850,280.00 USD | 0.00 USD | 850,280.00 USD | 0.00 USD | 12,320.00 USD | 0.00 USD |
| `1D` | `0.0987` | 566,670.00 USD | 0.00 USD | 566,670.00 USD | 22,740.00 USD | 3,920.00 USD | 11,800.00 USD |
| `1D` | `0.0989` | 528,220.00 USD | 0.00 USD | 528,220.00 USD | 2,180.00 USD | 1,540.00 USD | 21,720.00 USD |
| `7D` | `0.0989` | 837,960.00 USD | 0.00 USD | 837,960.00 USD | 17,640.00 USD | 7,820.00 USD | 0.00 USD |
| `1D` | `0.0991` | 502,770.00 USD | 0.00 USD | 502,770.00 USD | 69,940.00 USD | 0.00 USD | 760.65 USD |
| `7D` | `0.0992` | 812,500.00 USD | 0.00 USD | 812,500.00 USD | 27,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0993` | 432,080.00 USD | 0.00 USD | 432,080.00 USD | 23,960.00 USD | 1,510.00 USD | 43,470.00 USD |
| `1D` | `0.0995` | 363,140.00 USD | 0.00 USD | 363,140.00 USD | 17,890.00 USD | 898.20 USD | 50,250.00 USD |
| `7D` | `0.0995` | 785,360.00 USD | 0.00 USD | 785,360.00 USD | 63,330.00 USD | 0.00 USD | 76,030.00 USD |
| `1D` | `0.0997` | 294,100.00 USD | 0.00 USD | 294,100.00 USD | 17,900.00 USD | 5,840.00 USD | 53,670.00 USD |
| `7D` | `0.0998` | 645,990.00 USD | 0.00 USD | 645,990.00 USD | 28,450.00 USD | 17,040.00 USD | 135,270.00 USD |
| `1D` | `0.0999` | 216,690.00 USD | 0.00 USD | 216,690.00 USD | 0.00 USD | 10,180.00 USD | 47,900.00 USD |
| `1D` | `0.1001` | 158,610.00 USD | 0.00 USD | 158,610.00 USD | 0.00 USD | 0.00 USD | 42,510.00 USD |
| `7D` | `0.1001` | 465,230.00 USD | 0.00 USD | 465,230.00 USD | 76,560.00 USD | 25,570.00 USD | 107,970.00 USD |
| `1D` | `0.1003` | 116,090.00 USD | 0.00 USD | 116,090.00 USD | 23,240.00 USD | 0.00 USD | 27,200.00 USD |
| `7D` | `0.1004` | 255,120.00 USD | 0.00 USD | 255,120.00 USD | 22,470.00 USD | 0.00 USD | 23,430.00 USD |
| `1D` | `0.1005` | 65,650.00 USD | 0.00 USD | 65,650.00 USD | 8,250.00 USD | 5,890.00 USD | 20,390.00 USD |
| `1D` | `0.1007` | 31,120.00 USD | 0.00 USD | 31,120.00 USD | 4,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1007` | 209,220.00 USD | 0.00 USD | 209,220.00 USD | 20,870.00 USD | 3,080.00 USD | 100,230.00 USD |
| `1D` | `0.1009` | 26,760.00 USD | 0.00 USD | 26,760.00 USD | 6,930.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1010` | 85,040.00 USD | 0.00 USD | 85,040.00 USD | 17,340.00 USD | 13,670.00 USD | 54,030.00 USD |
| `1D` | `0.1011` | 19,830.00 USD | 0.00 USD | 19,830.00 USD | 0.00 USD | 4,070.00 USD | 15,760.00 USD |
| `1D` | `0.1012` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1013` | 10,500.00 USD | 10,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,500.00 USD |
| `7D` | `0.1013` | 88,650.00 USD | 88,650.00 USD | 0.00 USD | 34,830.00 USD | 28,370.00 USD | 25,450.00 USD |
| `7D` | `0.1013` | 177,310.00 USD | 177,310.00 USD | 0.00 USD | 34,830.00 USD | 28,370.00 USD | 25,450.00 USD |
| `1D` | `0.1015` | 29,530.00 USD | 29,530.00 USD | 0.00 USD | 4,580.00 USD | 1,220.00 USD | 13,220.00 USD |
| `7D` | `0.1016` | 192,890.00 USD | 192,890.00 USD | 0.00 USD | 15,440.00 USD | 0.00 USD | 142.43 USD |
| `1D` | `0.1017` | 49,160.00 USD | 49,160.00 USD | 0.00 USD | 3,590.00 USD | 4,930.00 USD | 11,110.00 USD |
| `1D` | `0.1019` | 58,570.00 USD | 58,570.00 USD | 0.00 USD | 0.00 USD | 9,410.00 USD | 0.00 USD |
| `7D` | `0.1019` | 248,120.00 USD | 248,120.00 USD | 0.00 USD | 26,150.00 USD | 8,460.00 USD | 20,610.00 USD |
| `1D` | `0.1021` | 98,190.00 USD | 98,190.00 USD | 0.00 USD | 13,630.00 USD | 12,100.00 USD | 13,880.00 USD |
| `7D` | `0.1022` | 313,920.00 USD | 313,920.00 USD | 0.00 USD | 18,100.00 USD | 10,260.00 USD | 37,440.00 USD |
| `1D` | `0.1023` | 144,100.00 USD | 144,100.00 USD | 0.00 USD | 15,750.00 USD | 10,470.00 USD | 19,700.00 USD |
| `1D` | `0.1025` | 148,810.00 USD | 148,810.00 USD | 0.00 USD | 3,740.00 USD | 962.66 USD | 0.00 USD |
| `7D` | `0.1025` | 320,260.00 USD | 320,260.00 USD | 0.00 USD | 1,550.00 USD | 4,790.00 USD | 0.00 USD |
| `1D` | `0.1027` | 166,440.00 USD | 166,440.00 USD | 0.00 USD | 3,430.00 USD | 3,920.00 USD | 10,290.00 USD |
| `7D` | `0.1028` | 352,150.00 USD | 352,150.00 USD | 0.00 USD | 3,800.00 USD | 4,390.00 USD | 23,700.00 USD |
| `1D` | `0.1029` | 188,210.00 USD | 188,210.00 USD | 0.00 USD | 6,870.00 USD | 7,400.00 USD | 7,510.00 USD |
| `1D` | `0.1031` | 251,600.00 USD | 251,600.00 USD | 0.00 USD | 33,590.00 USD | 5,770.00 USD | 24,020.00 USD |
| `7D` | `0.1031` | 381,510.00 USD | 381,510.00 USD | 0.00 USD | 19,560.00 USD | 9,810.00 USD | 0.00 USD |
| `1D` | `0.1033` | 287,500.00 USD | 287,500.00 USD | 0.00 USD | 2,890.00 USD | 9,230.00 USD | 23,790.00 USD |
| `7D` | `0.1034` | 415,720.00 USD | 415,720.00 USD | 0.00 USD | 18,920.00 USD | 15,180.00 USD | 106.77 USD |
| `1D` | `0.1035` | 313,800.00 USD | 313,800.00 USD | 0.00 USD | 15,150.00 USD | 11,130.00 USD | 17.34 USD |
| `1D` | `0.1037` | 363,070.00 USD | 363,070.00 USD | 0.00 USD | 36,550.00 USD | 12,700.00 USD | 24.05 USD |
| `7D` | `0.1037` | 429,250.00 USD | 429,250.00 USD | 0.00 USD | 2,710.00 USD | 10,710.00 USD | 108.00 USD |
| `1D` | `0.1039` | 383,290.00 USD | 383,290.00 USD | 0.00 USD | 6,500.00 USD | 8,500.00 USD | 5,220.00 USD |
| `7D` | `0.1040` | 476,850.00 USD | 476,850.00 USD | 0.00 USD | 5,940.00 USD | 10,300.00 USD | 31,350.00 USD |
| `1D` | `0.1041` | 431,290.00 USD | 431,290.00 USD | 0.00 USD | 11,520.00 USD | 16,860.00 USD | 19,630.00 USD |
| `1D` | `0.1043` | 465,430.00 USD | 465,430.00 USD | 0.00 USD | 0.00 USD | 9,960.00 USD | 24,170.00 USD |
| `7D` | `0.1043` | 498,790.00 USD | 498,790.00 USD | 0.00 USD | 15,960.00 USD | 5,980.00 USD | 0.00 USD |
| `1D` | `0.1045` | 474,490.00 USD | 474,490.00 USD | 0.00 USD | 1,870.00 USD | 2,240.00 USD | 4,950.00 USD |
| `7D` | `0.1046` | 571,160.00 USD | 571,160.00 USD | 0.00 USD | 0.00 USD | 12,200.00 USD | 60,160.00 USD |
| `1D` | `0.1047` | 548,300.00 USD | 548,300.00 USD | 0.00 USD | 28,580.00 USD | 8,010.00 USD | 37,230.00 USD |
| `1D` | `0.1049` | 666,100.00 USD | 666,100.00 USD | 0.00 USD | 33,450.00 USD | 15,310.00 USD | 69,040.00 USD |
| `7D` | `0.1049` | 695,650.00 USD | 695,650.00 USD | 0.00 USD | 34,790.00 USD | 6,530.00 USD | 83,180.00 USD |
| `1D` | `0.1051` | 733,820.00 USD | 733,820.00 USD | 0.00 USD | 33,210.00 USD | 10,280.00 USD | 24,230.00 USD |
| `7D` | `0.1052` | 873,500.00 USD | 873,500.00 USD | 0.00 USD | 28,200.00 USD | 24,160.00 USD | 125,480.00 USD |
| `1D` | `0.1053` | 837,740.00 USD | 837,740.00 USD | 0.00 USD | 36,480.00 USD | 11,370.00 USD | 56,070.00 USD |
| `1D` | `0.1055` | 972,200.00 USD | 972,200.00 USD | 0.00 USD | 51,530.00 USD | 26,280.00 USD | 56,650.00 USD |
| `7D` | `0.1055` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 122,840.00 USD | 44,430.00 USD | 211,630.00 USD |
| `1D` | `0.1057` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 14,080.00 USD | 11,900.00 USD | 32,170.00 USD |
| `7D` | `0.1058` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 105,620.00 USD | 58,510.00 USD | 202,430.00 USD |
| `1D` | `0.1059` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 35,730.00 USD | 4,960.00 USD | 77,020.00 USD |
| `1D` | `0.1061` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 30,060.00 USD | 1,890.00 USD | 60,420.00 USD |
| `7D` | `0.1061` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 75,540.00 USD | 69,160.00 USD | 118,420.00 USD |
| `1D` | `0.1063` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 25,200.00 USD | 2,030.00 USD | 65,320.00 USD |
| `7D` | `0.1064` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 52,580.00 USD | 177,550.00 USD |
| `1D` | `0.1065` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 1,740.00 USD | 2,630.00 USD | 24,690.00 USD |
| `1D` | `0.1067` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 8,230.00 USD | 1,320.00 USD | 44,170.00 USD |
| `7D` | `0.1067` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 51,740.00 USD | 143,940.00 USD |
| `1D` | `0.1069` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 14,770.00 USD | 5,440.00 USD | 62,810.00 USD |
| `7D` | `0.1070` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 57,770.00 USD | 134,670.00 USD |
| `1D` | `0.1071` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 2,550.00 USD | 5,850.00 USD | 20,430.00 USD |
| `1D` | `0.1073` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,200.00 USD |
| `7D` | `0.1073` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 7,820.00 USD | 20,440.00 USD | 10,320.00 USD |
| `1D` | `0.1075` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 1,440.00 USD | 857.82 USD | 3,780.00 USD |
| `7D` | `0.1076` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,500.00 USD |
| `1D` | `0.1077` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 619.42 USD | 77.28 USD |
| `1D` | `0.1079` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 4,300.00 USD | 21,830.00 USD |
| `7D` | `0.1079` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 5,620.00 USD | 3,380.00 USD | 10,010.00 USD |
| `1D` | `0.1081` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 4,650.00 USD | 732.74 USD | 2,400.00 USD |
| `7D` | `0.1082` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 89.24 USD |
| `1D` | `0.1083` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 9,160.00 USD | 6,710.00 USD | 10,770.00 USD |
| `1D` | `0.1085` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 385.06 USD | 65,020.00 USD |
| `7D` | `0.1085` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1087` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 28,490.00 USD | 2,510.00 USD | 44,670.00 USD |
| `7D` | `0.1088` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 5,290.00 USD | 1,420.00 USD | 9,590.00 USD |
| `1D` | `0.1089` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 29,650.00 USD | 1,580.00 USD | 3,310.00 USD |
| `1D` | `0.1091` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 33,700.00 USD | 0.00 USD | 16.51 USD |
| `7D` | `0.1091` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD |
| `1D` | `0.1093` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 15,480.00 USD | 1,080.00 USD | 222.36 USD |
| `7D` | `0.1094` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 1,500.00 USD | 8,730.00 USD |
| `1D` | `0.1095` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 21,520.00 USD |
| `1D` | `0.1097` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 7,260.00 USD | 2,530.00 USD | 22,800.00 USD |
| `7D` | `0.1097` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1099` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 6,130.00 USD | 1,940.00 USD | 5.91 USD |
| `7D` | `0.1100` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 21,880.00 USD |
| `1D` | `0.1101` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 5,570.00 USD | 3,820.00 USD | 4,290.00 USD |
| `1D` | `0.1103` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 3,540.00 USD | 6,900.00 USD | 1,160.00 USD |
| `7D` | `0.1103` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1105` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 3,380.00 USD | 4,740.00 USD | 10,710.00 USD |
| `7D` | `0.1106` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 22,880.00 USD | 16,130.00 USD |
| `1D` | `0.1107` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 3,110.00 USD | 13,200.00 USD | 35,750.00 USD |
| `1D` | `0.1109` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 2,110.00 USD | 1,370.00 USD | 2,670.00 USD |
| `7D` | `0.1109` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD |
| `1D` | `0.1111` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 5,200.00 USD | 996.46 USD | 96.09 USD |
| `7D` | `0.1112` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD |
| `1D` | `0.1113` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 21,390.00 USD | 5,880.00 USD | 29,960.00 USD |
| `1D` | `0.1115` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 6,690.00 USD | 465.26 USD | 0.00 USD |
| `1D` | `0.1117` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 2,060.00 USD | 23,600.00 USD | 34,770.00 USD |
| `7D` | `0.1118` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD |
| `1D` | `0.1119` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 33,110.00 USD | 8,660.00 USD | 36,740.00 USD |
| `7D` | `0.1121` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 17,760.00 USD | 0.00 USD | 38,370.00 USD |
| `7D` | `0.1124` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD |
| `7D` | `0.1127` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD |
| `7D` | `0.1130` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,260.00 USD |
| `7D` | `0.1133` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD |
| `7D` | `0.1136` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD |
| `7D` | `0.1139` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD |
| `7D` | `0.1142` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD |
| `7D` | `0.1145` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD |
| `7D` | `0.1148` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 175,990.00 USD |
| `7D` | `0.1151` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD |
| `7D` | `0.1154` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 243,190.00 USD | 26,970.00 USD | 202,050.00 USD |
| `7D` | `0.1157` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 173,120.00 USD | 25,290.00 USD | 98,310.00 USD |
| `7D` | `0.1160` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 131,160.00 USD | 32,830.00 USD | 109,320.00 USD |
| `7D` | `0.1163` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD |
| `7D` | `0.1166` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD |
| `7D` | `0.1169` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 82,770.00 USD | 26,150.00 USD | 117,900.00 USD |
| `7D` | `0.1172` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD |
| `7D` | `0.1175` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 75,590.00 USD | 17,930.00 USD | 81,630.00 USD |
| `7D` | `0.1178` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 89,510.00 USD | 25,350.00 USD | 60,700.00 USD |
| `7D` | `0.1181` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD |
| `7D` | `0.1184` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD |
| `7D` | `0.1187` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 5,620.00 USD | 17,120.00 USD | 59,700.00 USD |
| `7D` | `0.1190` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD |
| `7D` | `0.1193` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD |
| `7D` | `0.1196` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD |
| `7D` | `0.1199` | 6,680,000.00 USD | 6,680,000.00 USD | 0.00 USD | 2,470.00 USD | 13,190.00 USD | 52,120.00 USD |
| `7D` | `0.1202` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 138,430.00 USD | 21,430.00 USD | 32,790.00 USD |
| `7D` | `0.1205` | 7,080,000.00 USD | 7,080,000.00 USD | 0.00 USD | 117,120.00 USD | 48,510.00 USD | 40,590.00 USD |
| `7D` | `0.1208` | 7,180,000.00 USD | 7,180,000.00 USD | 0.00 USD | 39,480.00 USD | 20,870.00 USD | 39,590.00 USD |
| `7D` | `0.1211` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 72,500.00 USD | 25,920.00 USD | 76,780.00 USD |
| `7D` | `0.1214` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD |
| `7D` | `0.1217` | 7,520,000.00 USD | 7,520,000.00 USD | 0.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD |
| `7D` | `0.1220` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 34,050.00 USD | 6,400.00 USD | 54,700.00 USD |
| `7D` | `0.1223` | 7,740,000.00 USD | 7,740,000.00 USD | 0.00 USD | 73,610.00 USD | 15,050.00 USD | 37,720.00 USD |
| `7D` | `0.1226` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 45,920.00 USD | 19,760.00 USD | 5,210.00 USD |
| `7D` | `0.1229` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 63,930.00 USD | 33,570.00 USD | 28,680.00 USD |
| `7D` | `0.1232` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 51,420.00 USD | 12,080.00 USD | 37,580.00 USD |
| `7D` | `0.1235` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 15,040.00 USD | 5,390.00 USD | 16,760.00 USD |
| `7D` | `0.1237` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 4,080.00 USD | 2,760.00 USD | 2,800.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `63.69M` | Total OI Tokens: `626,844,268.1 OP`
  * 1h OI Change: `+1.76%` | 4h OI Change: `+5.56%` | 24h OI Change: `-12.36%`
  * Exchange Breakdown: Binance=`13.75M` | Bybit=`12.95M` | OKX=`3.75M` | Hyperliquid=`3.12M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-2.42K` | Last 24h: `-2.42K` | Last 3d: `-6.63K` | Last 7d: `-14.48K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0295%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0293%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0051%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `56.11%` | `43.89%` | `1.28` | 1,400,000.00 USD |
| `15M` | `Binance` | `61.37%` | `38.63%` | `1.59` | 587,570.00 USD |
| `15M` | `OKX` | `62.05%` | `37.95%` | `1.64` | 144,630.00 USD |
| `15M` | `Bybit` | `56.05%` | `43.95%` | `1.28` | 110,270.00 USD |
| `15M` | `KuCoin` | `49.35%` | `50.65%` | `0.97` | 90,980.00 USD |
| `15M` | `Gate` | `51.1%` | `48.9%` | `1.04` | 10,000.00 USD |
| `15M` | `Bitget` | `81.85%` | `18.15%` | `4.51` | 27,530.00 USD |
| `15M` | `BingX` | `43.73%` | `56.27%` | `0.78` | 29,690.00 USD |
| `15M` | `MEXC` | `20.41%` | `79.59%` | `0.26` | 51,300.00 USD |
| `15M` | `Bitunix` | `45.69%` | `54.31%` | `0.84` | 14,160.00 USD |
| `15M` | `Hyperliquid` | `95.64%` | `4.36%` | `21.94` | 22,490.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.49%` | `51.51%` | `0.94` | 289,510.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `44.25%` | `55.75%` | `0.79` | 20,010.00 USD |
| `15M` | `HTX` | `38.99%` | `61.01%` | `0.64` | 629.62 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 41.73 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 1,510.00 USD |
| `15M` | `Whale Positions` | `61.37%` | `38.63%` | `1.59` | 587,570.00 USD |
| `15M` | `Global Accounts` | `56.11%` | `43.89%` | `1.28` | 1,400,000.00 USD |
| `1H` | `OP` | `47.41%` | `52.59%` | `0.90` | 5,840,000.00 USD |
| `1H` | `Binance` | `46.32%` | `53.68%` | `0.86` | 1,800,000.00 USD |
| `1H` | `OKX` | `43.98%` | `56.02%` | `0.79` | 510,890.00 USD |
| `1H` | `Bybit` | `46.4%` | `53.6%` | `0.87` | 567,640.00 USD |
| `1H` | `KuCoin` | `50.81%` | `49.19%` | `1.03` | 522,990.00 USD |
| `1H` | `Gate` | `42.82%` | `57.18%` | `0.75` | 74,580.00 USD |
| `1H` | `Bitget` | `47.16%` | `52.84%` | `0.89` | 979,280.00 USD |
| `1H` | `BingX` | `47.84%` | `52.16%` | `0.92` | 671,410.00 USD |
| `1H` | `MEXC` | `59.64%` | `40.36%` | `1.48` | 246,040.00 USD |
| `1H` | `Bitunix` | `41.17%` | `58.83%` | `0.70` | 83,540.00 USD |
| `1H` | `Hyperliquid` | `87.92%` | `12.08%` | `7.28` | 66,400.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.01%` | `49.99%` | `1.00` | 188,060.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `40.17%` | `59.83%` | `0.67` | 75,980.00 USD |
| `1H` | `HTX` | `82.46%` | `17.54%` | `4.70` | 1,390.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `5.42%` | `94.58%` | `0.06` | 53,800.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `12.44%` | `87.56%` | `0.14` | 3,510.00 USD |
| `1H` | `Whale Positions` | `46.32%` | `53.68%` | `0.86` | 1,800,000.00 USD |
| `1H` | `Global Accounts` | `47.41%` | `52.59%` | `0.90` | 5,840,000.00 USD |
| `4H` | `OP` | `43.53%` | `56.47%` | `0.77` | 25,710,000.00 USD |
| `4H` | `Binance` | `51.14%` | `48.86%` | `1.05` | 8,490,000.00 USD |
| `4H` | `OKX` | `51.35%` | `48.65%` | `1.06` | 2,240,000.00 USD |
| `4H` | `Bybit` | `51.61%` | `48.39%` | `1.07` | 2,660,000.00 USD |
| `4H` | `KuCoin` | `50.23%` | `49.77%` | `1.01` | 1,100,000.00 USD |
| `4H` | `Gate` | `57.49%` | `42.51%` | `1.35` | 443,380.00 USD |
| `4H` | `Bitget` | `49.82%` | `50.18%` | `0.99` | 432,670.00 USD |
| `4H` | `BingX` | `8.66%` | `91.34%` | `0.09` | 4,420,000.00 USD |
| `4H` | `MEXC` | `47.02%` | `52.98%` | `0.89` | 894,660.00 USD |
| `4H` | `Bitunix` | `40.37%` | `59.63%` | `0.68` | 258,670.00 USD |
| `4H` | `Hyperliquid` | `54.89%` | `45.11%` | `1.22` | 151,380.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.32%` | `50.68%` | `0.97` | 4,340,000.00 USD |
| `4H` | `Crypto.com` | `17.92%` | `82.08%` | `0.22` | 1,440.00 USD |
| `4H` | `WhiteBIT` | `70.79%` | `29.21%` | `2.42` | 158,340.00 USD |
| `4H` | `HTX` | `54.1%` | `45.9%` | `1.18` | 9,330.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `16.8%` | `83.2%` | `0.20` | 34,300.00 USD |
| `4H` | `Aster` | `59.94%` | `40.06%` | `1.50` | 441.70 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `70.99%` | `29.01%` | `2.45` | 50,340.00 USD |
| `4H` | `Whale Positions` | `51.14%` | `48.86%` | `1.05` | 8,490,000.00 USD |
| `4H` | `Global Accounts` | `43.53%` | `56.47%` | `0.77` | 25,710,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0981` | `0.0982` | `0.0981` | `0.0988` | `0.0980` | 282,587.21 USD | 127,716.82 USD | 154,870.40 USD | -27,153.58 USD | `-9.61%` | `10B / 27S` |
| `0:00 UTC` | `0.0985` | `0.0980` | `0.0985` | `0.0986` | `0.0972` | 782,641.49 USD | 272,807.16 USD | 509,834.33 USD | -237,027.16 USD | `-30.29%` | `4B / 30S` |
| `5:00 UTC` | `0.0976` | `0.0974` | `0.0976` | `0.0979` | `0.0970` | 1,011,824.45 USD | 364,728.70 USD | 647,095.75 USD | -282,367.05 USD | `-27.91%` | `6B / 15S` |
| `0:00 UTC` | `0.0984` | `0.0984` | `0.0984` | `0.0992` | `0.0978` | 803,922.63 USD | 438,559.35 USD | 365,363.29 USD | 73,196.06 USD | `+9.10%` | `32B / 10S` |
| `5:00 UTC` | `0.0992` | `0.0992` | `0.0992` | `0.0995` | `0.0989` | 394,380.07 USD | 199,715.01 USD | 194,665.06 USD | 5,049.95 USD | `+1.28%` | `10B / 6S` |
| `0:00 UTC` | `0.0989` | `0.0992` | `0.0989` | `0.0999` | `0.0988` | 347,230.40 USD | 177,310.87 USD | 169,919.53 USD | 7,391.34 USD | `+2.13%` | `21B / 7S` |
| `5:00 UTC` | `0.1001` | `0.1001` | `0.1001` | `0.1004` | `0.0996` | 360,867.60 USD | 243,343.04 USD | 117,524.56 USD | 125,818.48 USD | `+34.87%` | `30B / 1S` |
| `0:00 UTC` | `0.1005` | `0.1006` | `0.1005` | `0.1009` | `0.1002` | 321,574.58 USD | 208,787.55 USD | 112,787.03 USD | 96,000.52 USD | `+29.85%` | `23B / 4S` |
| `5:00 UTC` | `0.1009` | `0.1011` | `0.1009` | `0.1014` | `0.1006` | 597,276.02 USD | 343,393.62 USD | 253,882.40 USD | 89,511.23 USD | `+14.99%` | `17B / 7S` |
| `0:00 UTC` | `0.1013` | `0.1013` | `0.1013` | `0.1014` | `0.1012` | 60,223.11 USD | 35,981.19 USD | 24,241.92 USD | 11,739.27 USD | `+19.49%` | `4B / 2S` |

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
| `5m` | -991.04 USD | 1,230.00 USD | **`ACCUMULATION`** |
| `15m` | 41,610.00 USD | 61,280.00 USD | **`ACCUMULATION`** |
| `30m` | 79,200.00 USD | 153,440.00 USD | **`ACCUMULATION`** |
| `1h` | 192,650.00 USD | 281,960.00 USD | **`ACCUMULATION`** |
| `2h` | -54,720.00 USD | -261,390.00 USD | **`DISTRIBUTION`** |
| `4h` | -55,270.00 USD | 149,350.00 USD | **`ACCUMULATION`** |
| `6h` | 4,620.00 USD | -1,900,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 540,010.00 USD | -4,660,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 36,240.00 USD | -4,820,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 313,160.00 USD | -3,880,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -80,960.00 USD | -14,750,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,300,000.00 USD | -83,190,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-991.04` | 15m=`+41.61K` | 1h=`+192.65K` | 24h=`+313.16K`
* Futures Capital Netflows: 5m=`+1.23K` | 15m=`+61.28K` | 1h=`+281.96K` | 24h=`-3.88M`
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
  * `2026-10-30 09:51:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:29:10 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
