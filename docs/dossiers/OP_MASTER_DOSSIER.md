# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 08:06:32 IST` (`2026-10-30 02:36:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.0975` | `0.0976` | `0.0965` | `0.0966` | `1,502,124` | 145,912.48 USD | -5,713.42 USD | `-3.92%` | -2,589,858.43 USD | `-0.13` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `0.0966` | `0.0975` | `0.0965` | `0.0973` | `2,036,613` | 197,805.57 USD | 48,302.49 USD | `+24.42%` | -2,541,555.94 USD | `+1.50` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.0973` | `0.0979` | `0.0973` | `0.0979` | `999,417` | 97,648.09 USD | 47,900.90 USD | `+49.05%` | -2,493,655.04 USD | `+1.33` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.0975` | `0.0984` | `0.0965` | `0.0980` | `7,715,203` | 753,212.73 USD | 153,350.96 USD | `+20.36%` | -2,562,766.39 USD | `+0.89` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.0980` | `0.0980` | `0.0970` | `0.0974` | `3,467,410` | 337,745.57 USD | -21,378.62 USD | `-6.33%` | -2,584,145.01 USD | `+0.06` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.0975` | `0.0979` | `0.0965` | `0.0979` | `4,544,048` | 441,943.17 USD | 90,999.73 USD | `+20.59%` | -2,493,145.29 USD | `+0.56` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.1012` | `0.1013` | `0.0934` | `0.0982` | `83,849,609` | 8,156,035.35 USD | -1,102,651.64 USD | `-13.52%` | -2,245,257.97 USD | `-2.27` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.0982` | `0.0986` | `0.0965` | `0.0974` | `24,259,683` | 2,371,197.93 USD | 94,729.98 USD | `+4.00%` | -2,150,527.99 USD | `+0.43` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.0975` | `0.0979` | `0.0965` | `0.0979` | `4,544,048` | 441,943.17 USD | 90,999.73 USD | `+20.59%` | -2,059,528.26 USD | `+0.40` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | 416,406.14 USD | `-1.52` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -900,791.72 USD | `-1.92` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0979` | `112,653,105` | 10,969,153.41 USD | -916,898.89 USD | `-8.36%` | -1,817,690.61 USD | `-1.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | 251,290.82 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | 592,546.43 USD | `+1.40` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | 416,406.14 USD | `-1.52` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.0989` | `0.1012` | `228,454,236` | 23,598,875.37 USD | -1,317,197.86 USD | `-5.58%` | -900,791.72 USD | `-1.92` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1012` | `0.1013` | `0.0934` | `0.0979` | `112,653,105` | 10,969,153.41 USD | -916,898.89 USD | `-8.36%` | -1,817,690.61 USD | `-1.01` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:57:16 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1135` | 5,015.28 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale BUY: 5.02K USD at 0.1135 USD [API] | `2026-10-28 22:45:05` |


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
| `Live` | `Long Liquidation` | `0.0221` | 132.30 USD | 99,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0262` | 2,690.00 USD | 98,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0307` | 1,330.00 USD | 96,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 287.32 USD | 94,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 828.97 USD | 94,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 442.58 USD | 93,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0619` | 1,110.00 USD | 93,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 4,490.00 USD | 92,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0648` | 355.18 USD | 87,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0674` | 230.77 USD | 87,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0677` | 288.18 USD | 87,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0688` | 1,930.00 USD | 86,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0706` | 1,090.00 USD | 84,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0723` | 23,500.00 USD | 83,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0728` | 371.99 USD | 60,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0732` | 41,410.00 USD | 59,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0743` | 2,290.00 USD | 18,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0751` | 1,010.00 USD | 16,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0761` | 807.36 USD | 15,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0767` | 510.56 USD | 14,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0776` | 880.32 USD | 13,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0781` | 337.98 USD | 13,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 1,110.00 USD | 12,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0804` | 223.57 USD | 11,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0819` | 445.92 USD | 11,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0819` | 1,130.00 USD | 10,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0822` | 1,650.00 USD | 9,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0854` | 1,710.00 USD | 8,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0863` | 145.81 USD | 6,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0877` | 794.53 USD | 6,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0878` | 1,150,000.00 USD | 1,150,000.00 USD | 1,370.00 USD | 4,930.00 USD | 27,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0881` | 1,110,000.00 USD | 1,110,000.00 USD | 3,770.00 USD | 2,660.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0884` | 1,090,000.00 USD | 1,090,000.00 USD | 7,040.00 USD | 4,640.00 USD | 11,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0887` | 1,070,000.00 USD | 1,070,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0890` | 1,030,000.00 USD | 1,030,000.00 USD | 14,610.00 USD | 4,470.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0893` | 1,010,000.00 USD | 1,010,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0893` | 150.94 USD | 5,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,120.00 USD | 5,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0896` | 992,980.00 USD | 992,980.00 USD | 5,760.00 USD | 611.80 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0899` | 979,730.00 USD | 979,730.00 USD | 3,390.00 USD | 927.82 USD | 4,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0901` | 813,420.00 USD | 813,420.00 USD | 2,450.00 USD | 0.00 USD | 293.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0902` | 970,930.00 USD | 970,930.00 USD | 2,270.00 USD | 910.78 USD | 1,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0903` | 810,670.00 USD | 810,670.00 USD | 831.11 USD | 2,190.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0903` | 1,790.00 USD | 2,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0905` | 806,590.00 USD | 806,590.00 USD | 0.00 USD | 450.11 USD | 2,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0905` | 966,540.00 USD | 966,540.00 USD | 10,350.00 USD | 996.61 USD | 4,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0907` | 803,810.00 USD | 803,810.00 USD | 2,290.00 USD | 450.82 USD | 967.41 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0907` | 444.38 USD | 444.38 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0908` | 951,110.00 USD | 951,110.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0909` | 800,100.00 USD | 800,100.00 USD | 938.76 USD | 363.17 USD | 778.75 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0911` | 798,020.00 USD | 798,020.00 USD | 5,580.00 USD | 1,450.00 USD | 5.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0911` | 939,710.00 USD | 939,710.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0913` | 790,990.00 USD | 790,990.00 USD | 0.00 USD | 465.26 USD | 787.25 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0914` | 936,430.00 USD | 936,430.00 USD | 1,670.00 USD | 903.90 USD | 45.81 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0915` | 789,730.00 USD | 789,730.00 USD | 6,590.00 USD | 1,800.00 USD | 46.43 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0917` | 781,300.00 USD | 781,300.00 USD | 3,850.00 USD | 754.23 USD | 2.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0917` | 933,810.00 USD | 933,810.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0919` | 776,690.00 USD | 776,690.00 USD | 4,980.00 USD | 504.78 USD | 2,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0921` | 768,680.00 USD | 768,680.00 USD | 0.00 USD | 750.63 USD | 3,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0923` | 764,150.00 USD | 764,150.00 USD | 1,410.00 USD | 0.00 USD | 3,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0923` | 925,800.00 USD | 925,800.00 USD | 0.00 USD | 0.00 USD | 10,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0925` | 759,480.00 USD | 759,480.00 USD | 3,270.00 USD | 2,170.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0926` | 915,240.00 USD | 915,240.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0932` | 905,270.00 USD | 905,270.00 USD | 0.00 USD | 0.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0933` | 742,860.00 USD | 742,860.00 USD | 0.00 USD | 0.00 USD | 6,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0935` | 893,030.00 USD | 893,030.00 USD | 0.00 USD | 1,320.00 USD | 6,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0937` | 736,000.00 USD | 736,000.00 USD | 0.00 USD | 0.00 USD | 64.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0938` | 885,220.00 USD | 885,220.00 USD | 0.00 USD | 0.00 USD | 8.57 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0939` | 735,930.00 USD | 735,930.00 USD | 0.00 USD | 0.00 USD | 76.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0941` | 885,210.00 USD | 885,210.00 USD | 2,050.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0944` | 880,140.00 USD | 880,140.00 USD | 1,870.00 USD | 0.00 USD | 7,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0947` | 735,860.00 USD | 735,860.00 USD | 0.00 USD | 0.00 USD | 69.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0947` | 870,750.00 USD | 870,750.00 USD | 3,790.00 USD | 1,810.00 USD | 112.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0950` | 865,030.00 USD | 865,030.00 USD | 3,770.00 USD | 0.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0953` | 735,790.00 USD | 735,790.00 USD | 0.00 USD | 0.00 USD | 108.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0953` | 854,600.00 USD | 854,600.00 USD | 0.00 USD | 0.00 USD | 4.65 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0955` | 735,680.00 USD | 735,680.00 USD | 0.00 USD | 1,180.00 USD | 213.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0959` | 854,590.00 USD | 854,590.00 USD | 0.00 USD | 0.00 USD | 115.48 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0961` | 734,280.00 USD | 734,280.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0962` | 854,480.00 USD | 854,480.00 USD | 0.00 USD | 0.00 USD | 121.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0963` | 732,200.00 USD | 732,200.00 USD | 0.00 USD | 0.00 USD | 1.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0965` | 732,200.00 USD | 732,200.00 USD | 1,280.00 USD | 282.32 USD | 1,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0967` | 728,760.00 USD | 728,760.00 USD | 2,660.00 USD | 1,100.00 USD | 7,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0968` | 854,360.00 USD | 854,360.00 USD | 7,490.00 USD | 2,310.00 USD | 11,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0969` | 717,500.00 USD | 717,500.00 USD | 4,590.00 USD | 2,640.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0971` | 701,260.00 USD | 701,260.00 USD | 16,100.00 USD | 3,330.00 USD | 4,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 832,930.00 USD | 832,930.00 USD | 0.00 USD | 3,760.00 USD | 9,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0973` | 677,170.00 USD | 677,170.00 USD | 2,750.00 USD | 5,760.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0974` | 819,450.00 USD | 819,450.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0975` | 664,220.00 USD | 664,220.00 USD | 0.00 USD | 3,850.00 USD | 5,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0977` | 654,820.00 USD | 654,820.00 USD | 24,760.00 USD | 6,580.00 USD | 12,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0977` | 815,170.00 USD | 815,170.00 USD | 0.00 USD | 4,010.00 USD | 28,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0979` | 610,960.00 USD | 610,960.00 USD | 19,100.00 USD | 2,930.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0980` | 782,350.00 USD | 782,350.00 USD | 0.00 USD | 3,920.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0981` | 582,660.00 USD | 582,660.00 USD | 9,220.00 USD | 2,460.00 USD | 15,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0983` | 555,060.00 USD | 555,060.00 USD | 3,250.00 USD | 4,020.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 772,730.00 USD | 772,730.00 USD | 7,990.00 USD | 1,230.00 USD | 14,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0985` | 531,680.00 USD | 531,680.00 USD | 13,900.00 USD | 1,740.00 USD | 10,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0986` | 748,730.00 USD | 748,730.00 USD | 7,110.00 USD | 7,530.00 USD | 61,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0987` | 505,330.00 USD | 505,330.00 USD | 15,960.00 USD | 7,630.00 USD | 32,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0989` | 448,980.00 USD | 448,980.00 USD | 2,820.00 USD | 3,290.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 673,080.00 USD | 673,080.00 USD | 17,640.00 USD | 6,190.00 USD | 53,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0991` | 440,550.00 USD | 440,550.00 USD | 32,710.00 USD | 2,950.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0992` | 596,040.00 USD | 596,040.00 USD | 27,140.00 USD | 11,490.00 USD | 28,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0993` | 401,700.00 USD | 401,700.00 USD | 3,080.00 USD | 5,090.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0995` | 382,060.00 USD | 382,060.00 USD | 8,250.00 USD | 8,610.00 USD | 11,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 528,920.00 USD | 528,920.00 USD | 24,220.00 USD | 15,150.00 USD | 56,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0997` | 353,720.00 USD | 353,720.00 USD | 35,260.00 USD | 8,860.00 USD | 27,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0998` | 433,000.00 USD | 433,000.00 USD | 28,450.00 USD | 12,100.00 USD | 80,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0999` | 282,400.00 USD | 282,400.00 USD | 44,410.00 USD | 6,710.00 USD | 26,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1001` | 204,830.00 USD | 204,830.00 USD | 27,550.00 USD | 5,470.00 USD | 21,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 311,730.00 USD | 311,730.00 USD | 36,110.00 USD | 8,650.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1003` | 150,580.00 USD | 150,580.00 USD | 0.00 USD | 5,820.00 USD | 21,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1004` | 253,840.00 USD | 253,840.00 USD | 22,470.00 USD | 16,470.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1005` | 123,480.00 USD | 123,480.00 USD | 18,440.00 USD | 3,050.00 USD | 30,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1007` | 71,980.00 USD | 71,980.00 USD | 0.00 USD | 11,300.00 USD | 56,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 191,470.00 USD | 191,470.00 USD | 20,870.00 USD | 3,870.00 USD | 100,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1010` | 66,500.00 USD | 66,500.00 USD | 17,340.00 USD | 6,580.00 USD | 6,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1011` | 3,980.00 USD | 3,980.00 USD | 0.00 USD | 0.00 USD | 3,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1013` | 587.32 USD | 587.32 USD | 0.00 USD | 0.00 USD | 587.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 35,940.00 USD | 35,940.00 USD | 15,270.00 USD | 5,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1016` | 15,440.00 USD | 15,440.00 USD | 15,440.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1019` | 12,100.00 USD | 12,100.00 USD | 12,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1022` | 32,280.00 USD | 32,280.00 USD | 11,930.00 USD | 8,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1025` | 33,830.00 USD | 33,830.00 USD | 1,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1028` | 42,020.00 USD | 42,020.00 USD | 3,800.00 USD | 4,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1031` | 46,790.00 USD | 46,790.00 USD | 27,910.00 USD | 0.00 USD | 18,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1031` | 67,840.00 USD | 67,840.00 USD | 19,560.00 USD | 6,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1033` | 72,010.00 USD | 72,010.00 USD | 0.00 USD | 3,360.00 USD | 21,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1034` | 93,790.00 USD | 93,790.00 USD | 18,920.00 USD | 7,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1035` | 95,220.00 USD | 95,220.00 USD | 10,280.00 USD | 12,870.00 USD | 54.66 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1037` | 152,630.00 USD | 152,630.00 USD | 37,310.00 USD | 20,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1037` | 107,210.00 USD | 107,210.00 USD | 2,710.00 USD | 10,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1039` | 170,920.00 USD | 170,920.00 USD | 6,500.00 USD | 9,220.00 USD | 2,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1040` | 154,810.00 USD | 154,810.00 USD | 5,940.00 USD | 10,300.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1041` | 211,290.00 USD | 211,290.00 USD | 6,450.00 USD | 16,880.00 USD | 17,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1043` | 243,480.00 USD | 243,480.00 USD | 0.00 USD | 10,910.00 USD | 21,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1043` | 176,750.00 USD | 176,750.00 USD | 15,960.00 USD | 5,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1045` | 253,270.00 USD | 253,270.00 USD | 0.00 USD | 4,840.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1046` | 246,720.00 USD | 246,720.00 USD | 0.00 USD | 9,810.00 USD | 60,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1047` | 327,410.00 USD | 327,410.00 USD | 31,470.00 USD | 6,050.00 USD | 36,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1049` | 444,830.00 USD | 444,830.00 USD | 37,390.00 USD | 13,300.00 USD | 66,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1049` | 371,150.00 USD | 371,150.00 USD | 34,790.00 USD | 6,530.00 USD | 83,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1051` | 508,180.00 USD | 508,180.00 USD | 30,370.00 USD | 8,750.00 USD | 24,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1052` | 548,910.00 USD | 548,910.00 USD | 28,200.00 USD | 24,160.00 USD | 125,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1053` | 604,660.00 USD | 604,660.00 USD | 35,030.00 USD | 10,620.00 USD | 50,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1055` | 738,160.00 USD | 738,160.00 USD | 46,710.00 USD | 27,100.00 USD | 59,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1055` | 927,650.00 USD | 927,650.00 USD | 122,840.00 USD | 44,430.00 USD | 211,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1057` | 832,730.00 USD | 832,730.00 USD | 27,300.00 USD | 17,200.00 USD | 50,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1058` | 1,280,000.00 USD | 1,280,000.00 USD | 105,620.00 USD | 56,540.00 USD | 189,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1059` | 974,050.00 USD | 974,050.00 USD | 39,020.00 USD | 4,070.00 USD | 98,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1061` | 1,070,000.00 USD | 1,070,000.00 USD | 33,450.00 USD | 1,890.00 USD | 65,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1061` | 1,550,000.00 USD | 1,550,000.00 USD | 75,540.00 USD | 72,260.00 USD | 118,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1063` | 1,180,000.00 USD | 1,180,000.00 USD | 25,200.00 USD | 2,030.00 USD | 75,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1064` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 52,580.00 USD | 192,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1065` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 2,630.00 USD | 25,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1067` | 1,260,000.00 USD | 1,260,000.00 USD | 8,230.00 USD | 1,320.00 USD | 41,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1067` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 51,740.00 USD | 156,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1069` | 1,340,000.00 USD | 1,340,000.00 USD | 8,170.00 USD | 5,440.00 USD | 70,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1070` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 57,770.00 USD | 134,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1071` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 3,140.00 USD | 16,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1073` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 243.10 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1073` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 17,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1075` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 125.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1076` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 22,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1077` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 77.28 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1079` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1079` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 79.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1082` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 89.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1083` | 1,400,000.00 USD | 1,400,000.00 USD | 7,990.00 USD | 5,910.00 USD | 7,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1085` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 65,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1085` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1087` | 1,540,000.00 USD | 1,540,000.00 USD | 28,490.00 USD | 2,240.00 USD | 44,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1088` | 2,240,000.00 USD | 2,240,000.00 USD | 5,290.00 USD | 0.00 USD | 113.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1089` | 1,580,000.00 USD | 1,580,000.00 USD | 37,180.00 USD | 0.00 USD | 108.06 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1091` | 1,610,000.00 USD | 1,610,000.00 USD | 33,700.00 USD | 0.00 USD | 16.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1091` | 2,260,000.00 USD | 2,260,000.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1093` | 1,630,000.00 USD | 1,630,000.00 USD | 15,480.00 USD | 0.00 USD | 222.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1094` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1095` | 1,650,000.00 USD | 1,650,000.00 USD | 4,110.00 USD | 1,890.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1097` | 1,690,000.00 USD | 1,690,000.00 USD | 7,260.00 USD | 1,970.00 USD | 22,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1097` | 2,290,000.00 USD | 2,290,000.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1099` | 1,690,000.00 USD | 1,690,000.00 USD | 6,130.00 USD | 1,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1100` | 2,320,000.00 USD | 2,320,000.00 USD | 11,470.00 USD | 0.00 USD | 21,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1101` | 1,710,000.00 USD | 1,710,000.00 USD | 4,310.00 USD | 2,820.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1103` | 1,710,000.00 USD | 1,710,000.00 USD | 3,540.00 USD | 5,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 2,360,000.00 USD | 2,360,000.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1105` | 1,730,000.00 USD | 1,730,000.00 USD | 3,380.00 USD | 4,740.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1106` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 22,880.00 USD | 16,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1107` | 1,780,000.00 USD | 1,780,000.00 USD | 3,110.00 USD | 12,720.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1109` | 1,790,000.00 USD | 1,790,000.00 USD | 2,110.00 USD | 1,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1109` | 252.40 USD | 252.40 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1111` | 1,790,000.00 USD | 1,790,000.00 USD | 5,200.00 USD | 0.00 USD | 96.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1112` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1113` | 1,860,000.00 USD | 1,860,000.00 USD | 21,390.00 USD | 5,880.00 USD | 39,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1115` | 1,860,000.00 USD | 1,860,000.00 USD | 4,760.00 USD | 465.26 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1117` | 1,930,000.00 USD | 1,930,000.00 USD | 2,060.00 USD | 26,110.00 USD | 34,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1118` | 2,510,000.00 USD | 2,510,000.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1119` | 2,010,000.00 USD | 2,010,000.00 USD | 33,110.00 USD | 8,300.00 USD | 36,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1121` | 2,050,000.00 USD | 2,050,000.00 USD | 21,300.00 USD | 12,810.00 USD | 12,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 2,570,000.00 USD | 2,570,000.00 USD | 17,760.00 USD | 0.00 USD | 38,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1123` | 2,100,000.00 USD | 2,100,000.00 USD | 36,220.00 USD | 2,290.00 USD | 8,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1124` | 2,670,000.00 USD | 2,670,000.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1125` | 2,140,000.00 USD | 2,140,000.00 USD | 11,130.00 USD | 13,990.00 USD | 11,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1127` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 1,250.00 USD | 19,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1127` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1129` | 2,170,000.00 USD | 2,170,000.00 USD | 10,120.00 USD | 0.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1130` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 24,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1131` | 2,220,000.00 USD | 2,220,000.00 USD | 20,830.00 USD | 8,530.00 USD | 22,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1133` | 2,280,000.00 USD | 2,280,000.00 USD | 6,530.00 USD | 22,520.00 USD | 23,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 2,740,000.00 USD | 2,740,000.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1135` | 2,290,000.00 USD | 2,290,000.00 USD | 4,040.00 USD | 3,670.00 USD | 4,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1136` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1137` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 856.93 USD | 40.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1139` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 14,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1139` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1141` | 2,340,000.00 USD | 2,340,000.00 USD | 13,860.00 USD | 2,800.00 USD | 20,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1142` | 2,780,000.00 USD | 2,780,000.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1143` | 2,400,000.00 USD | 2,400,000.00 USD | 20,300.00 USD | 27,990.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1145` | 2,460,000.00 USD | 2,460,000.00 USD | 13,430.00 USD | 11,690.00 USD | 38,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 3,020,000.00 USD | 3,020,000.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1147` | 2,510,000.00 USD | 2,510,000.00 USD | 10,640.00 USD | 10,080.00 USD | 30,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1148` | 3,210,000.00 USD | 3,210,000.00 USD | 9,880.00 USD | 0.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1149` | 2,580,000.00 USD | 2,580,000.00 USD | 35,170.00 USD | 624.71 USD | 31,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1150` | 2,610,000.00 USD | 2,610,000.00 USD | 6,880.00 USD | 13,020.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 3,480,000.00 USD | 3,480,000.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1154` | 3,950,000.00 USD | 3,950,000.00 USD | 243,190.00 USD | 26,970.00 USD | 195,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 4,260,000.00 USD | 4,260,000.00 USD | 188,950.00 USD | 25,290.00 USD | 98,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1160` | 4,530,000.00 USD | 4,530,000.00 USD | 131,160.00 USD | 32,830.00 USD | 109,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 4,820,000.00 USD | 4,820,000.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1166` | 5,030,000.00 USD | 5,030,000.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 5,260,000.00 USD | 5,260,000.00 USD | 82,770.00 USD | 26,150.00 USD | 112,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1172` | 5,380,000.00 USD | 5,380,000.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 5,560,000.00 USD | 5,560,000.00 USD | 72,770.00 USD | 17,930.00 USD | 81,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1178` | 5,730,000.00 USD | 5,730,000.00 USD | 89,510.00 USD | 23,660.00 USD | 55,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 5,810,000.00 USD | 5,810,000.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1184` | 5,880,000.00 USD | 5,880,000.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 5,950,000.00 USD | 5,950,000.00 USD | 5,620.00 USD | 17,120.00 USD | 54,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1190` | 6,100,000.00 USD | 6,100,000.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 6,180,000.00 USD | 6,180,000.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1196` | 6,240,000.00 USD | 6,240,000.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 6,330,000.00 USD | 6,330,000.00 USD | 9,100.00 USD | 13,190.00 USD | 67,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1202` | 6,520,000.00 USD | 6,520,000.00 USD | 138,430.00 USD | 21,430.00 USD | 32,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 6,860,000.00 USD | 6,860,000.00 USD | 132,960.00 USD | 72,910.00 USD | 130,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1208` | 6,990,000.00 USD | 6,990,000.00 USD | 39,480.00 USD | 25,720.00 USD | 66,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 7,200,000.00 USD | 7,200,000.00 USD | 72,500.00 USD | 25,920.00 USD | 111,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1213` | 3,310.00 USD | 3,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1214` | 7,320,000.00 USD | 7,320,000.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 7,370,000.00 USD | 7,370,000.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1220` | 7,480,000.00 USD | 7,480,000.00 USD | 45,700.00 USD | 10,970.00 USD | 54,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 7,630,000.00 USD | 7,630,000.00 USD | 76,930.00 USD | 24,740.00 USD | 45,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1226` | 721.38 USD | 4,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1226` | 7,720,000.00 USD | 7,720,000.00 USD | 54,940.00 USD | 27,490.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 7,900,000.00 USD | 7,900,000.00 USD | 71,850.00 USD | 38,040.00 USD | 73,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1232` | 8,030,000.00 USD | 8,030,000.00 USD | 51,420.00 USD | 14,500.00 USD | 68,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1235` | 8,070,000.00 USD | 8,070,000.00 USD | 15,040.00 USD | 5,390.00 USD | 17,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1238` | 8,090,000.00 USD | 8,090,000.00 USD | 8,310.00 USD | 3,610.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1241` | 8,110,000.00 USD | 8,110,000.00 USD | 11,380.00 USD | 1,380.00 USD | 7,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1244` | 8,150,000.00 USD | 8,150,000.00 USD | 26,540.00 USD | 8,130.00 USD | 9,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1245` | 196.02 USD | 4,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1247` | 8,190,000.00 USD | 8,190,000.00 USD | 7,900.00 USD | 12,590.00 USD | 15,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1250` | 8,210,000.00 USD | 8,210,000.00 USD | 8,540.00 USD | 4,990.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1253` | 8,220,000.00 USD | 8,220,000.00 USD | 1,550.00 USD | 0.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1256` | 8,230,000.00 USD | 8,230,000.00 USD | 3,800.00 USD | 4,390.00 USD | 220.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1259` | 8,240,000.00 USD | 8,240,000.00 USD | 5,870.00 USD | 1,190.00 USD | 121.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1262` | 8,240,000.00 USD | 8,240,000.00 USD | 4,270.00 USD | 0.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1265` | 8,250,000.00 USD | 8,250,000.00 USD | 2,710.00 USD | 0.00 USD | 7,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1268` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 0.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1271` | 8,260,000.00 USD | 8,260,000.00 USD | 5,940.00 USD | 0.00 USD | 30.15 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1274` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 0.00 USD | 12.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1277` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 0.00 USD | 20.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1280` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 0.00 USD | 6,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1414` | 24,550.00 USD | 29,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1524` | 6,080.00 USD | 35,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1567` | 551.14 USD | 35,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1694` | 169.20 USD | 35,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1742` | 130.90 USD | 35,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1757` | 147.34 USD | 36,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1827` | 514.71 USD | 36,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1860` | 167.44 USD | 36,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1863` | 199.77 USD | 36,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0221` | 99,030.00 USD | 0.00 USD | 132.30 USD | `-77.38%` | `6,000.00` |
| `Live` | `Long` | `0.0262` | 98,890.00 USD | 0.00 USD | 2,690.00 USD | `-73.07%` | `102,410.90` |
| `Live` | `Long` | `0.0307` | 96,210.00 USD | 0.00 USD | 1,330.00 USD | `-68.55%` | `43,265.90` |
| `Live` | `Long` | `0.0563` | 94,880.00 USD | 0.00 USD | 287.32 USD | `-42.19%` | `5,098.90` |
| `Live` | `Long` | `0.0575` | 94,590.00 USD | 0.00 USD | 828.97 USD | `-41.06%` | `14,429.40` |
| `Live` | `Long` | `0.0578` | 93,760.00 USD | 0.00 USD | 442.58 USD | `-40.75%` | `7,663.80` |
| `Live` | `Long` | `0.0619` | 93,320.00 USD | 0.00 USD | 1,110.00 USD | `-36.44%` | `17,943.80` |
| `Live` | `Long` | `0.0644` | 92,210.00 USD | 0.00 USD | 4,490.00 USD | `-33.98%` | `69,790.10` |
| `Live` | `Long` | `0.0648` | 87,720.00 USD | 0.00 USD | 355.18 USD | `-33.57%` | `5,485.40` |
| `Live` | `Long` | `0.0674` | 87,360.00 USD | 0.00 USD | 230.77 USD | `-30.80%` | `3,421.30` |
| `Live` | `Long` | `0.0677` | 87,130.00 USD | 0.00 USD | 288.18 USD | `-30.59%` | `4,259.90` |
| `Live` | `Long` | `0.0688` | 86,840.00 USD | 0.00 USD | 1,930.00 USD | `-29.47%` | `28,000.00` |
| `Live` | `Long` | `0.0706` | 84,920.00 USD | 0.00 USD | 1,090.00 USD | `-27.62%` | `15,500.00` |
| `Live` | `Long` | `0.0723` | 83,830.00 USD | 0.00 USD | 23,500.00 USD | `-25.77%` | `324,749.30` |
| `Live` | `Long` | `0.0728` | 60,330.00 USD | 0.00 USD | 371.99 USD | `-25.26%` | `5,106.30` |
| `Live` | `Long` | `0.0732` | 59,960.00 USD | 0.00 USD | 41,410.00 USD | `-24.85%` | `565,287.50` |
| `Live` | `Long` | `0.0743` | 18,550.00 USD | 0.00 USD | 2,290.00 USD | `-23.72%` | `30,851.90` |
| `Live` | `Long` | `0.0751` | 16,260.00 USD | 0.00 USD | 1,010.00 USD | `-23.00%` | `13,481.90` |
| `Live` | `Long` | `0.0761` | 15,240.00 USD | 0.00 USD | 807.36 USD | `-21.87%` | `10,602.20` |
| `Live` | `Long` | `0.0767` | 14,440.00 USD | 0.00 USD | 510.56 USD | `-21.26%` | `6,652.30` |
| `Live` | `Long` | `0.0776` | 13,930.00 USD | 0.00 USD | 880.32 USD | `-20.33%` | `11,337.00` |
| `Live` | `Long` | `0.0781` | 13,050.00 USD | 0.00 USD | 337.98 USD | `-19.82%` | `4,324.80` |
| `Live` | `Long` | `0.0795` | 12,710.00 USD | 0.00 USD | 1,110.00 USD | `-18.49%` | `13,940.20` |
| `Live` | `Long` | `0.0804` | 11,600.00 USD | 0.00 USD | 223.57 USD | `-17.56%` | `2,782.40` |
| `Live` | `Long` | `0.0819` | 11,380.00 USD | 0.00 USD | 445.92 USD | `-16.03%` | `5,448.00` |
| `Live` | `Long` | `0.0819` | 10,930.00 USD | 0.00 USD | 1,130.00 USD | `-15.92%` | `13,733.40` |
| `Live` | `Long` | `0.0822` | 9,810.00 USD | 0.00 USD | 1,650.00 USD | `-15.72%` | `20,133.00` |
| `Live` | `Long` | `0.0854` | 8,150.00 USD | 0.00 USD | 1,710.00 USD | `-12.33%` | `20,000.00` |
| `Live` | `Long` | `0.0863` | 6,440.00 USD | 0.00 USD | 145.81 USD | `-11.41%` | `1,688.60` |
| `Live` | `Long` | `0.0877` | 6,300.00 USD | 0.00 USD | 794.53 USD | `-10.07%` | `9,064.80` |
| `Live` | `Long` | `0.0893` | 5,500.00 USD | 0.00 USD | 150.94 USD | `-8.33%` | `1,689.30` |
| `Live` | `Long` | `0.0895` | 5,350.00 USD | 0.00 USD | 3,120.00 USD | `-8.23%` | `34,873.20` |
| `Live` | `Long` | `0.0903` | 2,230.00 USD | 0.00 USD | 1,790.00 USD | `-7.30%` | `19,788.30` |
| `Live` | `Long` | `0.0907` | 444.38 USD | 0.00 USD | 444.38 USD | `-6.89%` | `4,896.80` |
| `Live` | `Short` | `0.1109` | 252.40 USD | 252.40 USD | 0.00 USD | `+13.83%` | `2,274.90` |
| `Live` | `Short` | `0.1213` | 3,570.00 USD | 3,310.00 USD | 0.00 USD | `+24.50%` | `27,298.20` |
| `Live` | `Short` | `0.1226` | 4,290.00 USD | 721.38 USD | 0.00 USD | `+25.73%` | `5,886.40` |
| `Live` | `Short` | `0.1245` | 4,480.00 USD | 196.02 USD | 0.00 USD | `+27.78%` | `1,573.80` |
| `Live` | `Short` | `0.1414` | 29,030.00 USD | 24,550.00 USD | 0.00 USD | `+45.02%` | `173,673.70` |
| `Live` | `Short` | `0.1524` | 35,110.00 USD | 6,080.00 USD | 0.00 USD | `+56.30%` | `39,929.50` |
| `Live` | `Short` | `0.1567` | 35,670.00 USD | 551.14 USD | 0.00 USD | `+60.72%` | `3,518.30` |
| `Live` | `Short` | `0.1694` | 35,830.00 USD | 169.20 USD | 0.00 USD | `+73.85%` | `998.50` |
| `Live` | `Short` | `0.1742` | 35,970.00 USD | 130.90 USD | 0.00 USD | `+78.77%` | `751.20` |
| `Live` | `Short` | `0.1757` | 36,110.00 USD | 147.34 USD | 0.00 USD | `+80.21%` | `838.80` |
| `Live` | `Short` | `0.1827` | 36,630.00 USD | 514.71 USD | 0.00 USD | `+87.39%` | `2,818.00` |
| `Live` | `Short` | `0.1860` | 36,800.00 USD | 167.44 USD | 0.00 USD | `+90.88%` | `900.00` |
| `Live` | `Short` | `0.1863` | 36,990.00 USD | 199.77 USD | 0.00 USD | `+91.19%` | `1,072.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0639` | 13,920.00 USD | 0.00 USD | 1,150.00 USD | `-34.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0701` | 12,770.00 USD | 0.00 USD | 768.52 USD | `-28.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 12,010.00 USD | 0.00 USD | 591.03 USD | `-26.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 11,410.00 USD | 0.00 USD | 750.50 USD | `-23.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0806` | 10,660.00 USD | 0.00 USD | 411.82 USD | `-17.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0818` | 10,250.00 USD | 0.00 USD | 184.05 USD | `-16.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0819` | 10,070.00 USD | 0.00 USD | 102.08 USD | `-15.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0830` | 9,970.00 USD | 0.00 USD | 454.24 USD | `-14.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0856` | 9,510.00 USD | 0.00 USD | 631.95 USD | `-12.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0887` | 8,880.00 USD | 0.00 USD | 784.26 USD | `-8.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0906` | 8,100.00 USD | 0.00 USD | 444.86 USD | `-7.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0911` | 7,650.00 USD | 0.00 USD | 835.58 USD | `-6.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0919` | 6,810.00 USD | 0.00 USD | 626.30 USD | `-5.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0950` | 6,190.00 USD | 0.00 USD | 487.44 USD | `-2.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0965` | 5,700.00 USD | 0.00 USD | 5,700.00 USD | `-0.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 720.59 USD | 720.59 USD | 0.00 USD | `+0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0980` | 1,650.00 USD | 927.49 USD | 0.00 USD | `+0.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,450.00 USD | 799.63 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 3,850.00 USD | 1,400.00 USD | 0.00 USD | `+2.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1003` | 4,620.00 USD | 764.33 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1011` | 5,520.00 USD | 899.42 USD | 0.00 USD | `+3.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 6,300.00 USD | 784.13 USD | 0.00 USD | `+5.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1032` | 6,450.00 USD | 151.92 USD | 0.00 USD | `+5.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1035` | 8,810.00 USD | 2,360.00 USD | 0.00 USD | `+6.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 11,110.00 USD | 2,300.00 USD | 0.00 USD | `+6.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 30,080.00 USD | 18,980.00 USD | 0.00 USD | `+7.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 30,450.00 USD | 371.69 USD | 0.00 USD | `+7.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 37,370.00 USD | 6,920.00 USD | 0.00 USD | `+8.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1058` | 37,870.00 USD | 494.99 USD | 0.00 USD | `+8.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1061` | 38,110.00 USD | 241.22 USD | 0.00 USD | `+8.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 52,410.00 USD | 14,300.00 USD | 0.00 USD | `+9.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1066` | 147,250.00 USD | 94,840.00 USD | 0.00 USD | `+9.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 166,830.00 USD | 19,580.00 USD | 0.00 USD | `+9.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 167,070.00 USD | 238.90 USD | 0.00 USD | `+10.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1079` | 169,080.00 USD | 2,010.00 USD | 0.00 USD | `+10.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 169,330.00 USD | 254.37 USD | 0.00 USD | `+10.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 169,480.00 USD | 149.42 USD | 0.00 USD | `+10.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1101` | 169,640.00 USD | 162.07 USD | 0.00 USD | `+13.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1104` | 169,800.00 USD | 159.99 USD | 0.00 USD | `+13.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1113` | 170,060.00 USD | 254.25 USD | 0.00 USD | `+14.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1119` | 170,900.00 USD | 843.03 USD | 0.00 USD | `+14.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 171,420.00 USD | 515.63 USD | 0.00 USD | `+15.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1127` | 172,590.00 USD | 1,170.00 USD | 0.00 USD | `+15.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1129` | 173,380.00 USD | 789.09 USD | 0.00 USD | `+15.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1130` | 173,490.00 USD | 115.81 USD | 0.00 USD | `+15.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1142` | 173,630.00 USD | 134.19 USD | 0.00 USD | `+17.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 173,760.00 USD | 138.13 USD | 0.00 USD | `+18.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1166` | 173,940.00 USD | 180.89 USD | 0.00 USD | `+19.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 174,310.00 USD | 362.40 USD | 0.00 USD | `+20.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 175,360.00 USD | 1,050.00 USD | 0.00 USD | `+21.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1193` | 175,920.00 USD | 558.12 USD | 0.00 USD | `+22.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1198` | 190,030.00 USD | 14,120.00 USD | 0.00 USD | `+22.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1222` | 191,010.00 USD | 978.00 USD | 0.00 USD | `+25.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1225` | 325,000.00 USD | 133,980.00 USD | 0.00 USD | `+25.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1236` | 325,630.00 USD | 632.05 USD | 0.00 USD | `+26.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1240` | 333,020.00 USD | 7,390.00 USD | 0.00 USD | `+27.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1250` | 344,280.00 USD | 11,250.00 USD | 0.00 USD | `+28.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1258` | 348,660.00 USD | 4,390.00 USD | 0.00 USD | `+29.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1310` | 380,120.00 USD | 31,450.00 USD | 0.00 USD | `+34.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1338` | 381,440.00 USD | 1,320.00 USD | 0.00 USD | `+37.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1343` | 385,580.00 USD | 4,140.00 USD | 0.00 USD | `+37.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1361` | 393,140.00 USD | 7,560.00 USD | 0.00 USD | `+39.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1401` | 406,210.00 USD | 13,070.00 USD | 0.00 USD | `+43.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1426` | 406,310.00 USD | 102.25 USD | 0.00 USD | `+46.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1431` | 413,460.00 USD | 7,150.00 USD | 0.00 USD | `+46.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1484` | 414,510.00 USD | 1,040.00 USD | 0.00 USD | `+52.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1489` | 416,110.00 USD | 1,610.00 USD | 0.00 USD | `+52.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1524` | 419,880.00 USD | 3,760.00 USD | 0.00 USD | `+56.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1553` | 420,060.00 USD | 184.31 USD | 0.00 USD | `+59.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1560` | 423,960.00 USD | 3,900.00 USD | 0.00 USD | `+60.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1570` | 426,780.00 USD | 2,820.00 USD | 0.00 USD | `+61.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1577` | 427,000.00 USD | 220.02 USD | 0.00 USD | `+61.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1631` | 427,270.00 USD | 277.03 USD | 0.00 USD | `+67.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1691` | 429,300.00 USD | 2,020.00 USD | 0.00 USD | `+73.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1744` | 429,510.00 USD | 216.49 USD | 0.00 USD | `+78.98%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0878` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 1,370.00 USD | 4,930.00 USD | 27,260.00 USD |
| `7D` | `0.0881` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 3,770.00 USD | 2,660.00 USD | 12,940.00 USD |
| `7D` | `0.0884` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 7,040.00 USD | 4,640.00 USD | 11,870.00 USD |
| `7D` | `0.0887` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 11,620.00 USD | 2,920.00 USD | 19,610.00 USD |
| `7D` | `0.0890` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 14,610.00 USD | 4,470.00 USD | 3,680.00 USD |
| `7D` | `0.0893` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 7,650.00 USD | 4,360.00 USD | 7,170.00 USD |
| `7D` | `0.0896` | 992,980.00 USD | 0.00 USD | 992,980.00 USD | 5,760.00 USD | 611.80 USD | 6,870.00 USD |
| `7D` | `0.0899` | 979,730.00 USD | 0.00 USD | 979,730.00 USD | 3,390.00 USD | 927.82 USD | 4,490.00 USD |
| `1D` | `0.0901` | 813,420.00 USD | 0.00 USD | 813,420.00 USD | 2,450.00 USD | 0.00 USD | 293.66 USD |
| `7D` | `0.0902` | 970,930.00 USD | 0.00 USD | 970,930.00 USD | 2,270.00 USD | 910.78 USD | 1,210.00 USD |
| `1D` | `0.0903` | 810,670.00 USD | 0.00 USD | 810,670.00 USD | 831.11 USD | 2,190.00 USD | 1,070.00 USD |
| `1D` | `0.0905` | 806,590.00 USD | 0.00 USD | 806,590.00 USD | 0.00 USD | 450.11 USD | 2,320.00 USD |
| `7D` | `0.0905` | 966,540.00 USD | 0.00 USD | 966,540.00 USD | 10,350.00 USD | 996.61 USD | 4,080.00 USD |
| `1D` | `0.0907` | 803,810.00 USD | 0.00 USD | 803,810.00 USD | 2,290.00 USD | 450.82 USD | 967.41 USD |
| `7D` | `0.0908` | 951,110.00 USD | 0.00 USD | 951,110.00 USD | 3,950.00 USD | 4,470.00 USD | 2,970.00 USD |
| `1D` | `0.0909` | 800,100.00 USD | 0.00 USD | 800,100.00 USD | 938.76 USD | 363.17 USD | 778.75 USD |
| `1D` | `0.0911` | 798,020.00 USD | 0.00 USD | 798,020.00 USD | 5,580.00 USD | 1,450.00 USD | 5.42 USD |
| `7D` | `0.0911` | 939,710.00 USD | 0.00 USD | 939,710.00 USD | 0.00 USD | 606.54 USD | 2,670.00 USD |
| `1D` | `0.0913` | 790,990.00 USD | 0.00 USD | 790,990.00 USD | 0.00 USD | 465.26 USD | 787.25 USD |
| `7D` | `0.0914` | 936,430.00 USD | 0.00 USD | 936,430.00 USD | 1,670.00 USD | 903.90 USD | 45.81 USD |
| `1D` | `0.0915` | 789,730.00 USD | 0.00 USD | 789,730.00 USD | 6,590.00 USD | 1,800.00 USD | 46.43 USD |
| `1D` | `0.0917` | 781,300.00 USD | 0.00 USD | 781,300.00 USD | 3,850.00 USD | 754.23 USD | 2.87 USD |
| `7D` | `0.0917` | 933,810.00 USD | 0.00 USD | 933,810.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD |
| `1D` | `0.0919` | 776,690.00 USD | 0.00 USD | 776,690.00 USD | 4,980.00 USD | 504.78 USD | 2,520.00 USD |
| `1D` | `0.0921` | 768,680.00 USD | 0.00 USD | 768,680.00 USD | 0.00 USD | 750.63 USD | 3,780.00 USD |
| `1D` | `0.0923` | 764,150.00 USD | 0.00 USD | 764,150.00 USD | 1,410.00 USD | 0.00 USD | 3,260.00 USD |
| `7D` | `0.0923` | 925,800.00 USD | 0.00 USD | 925,800.00 USD | 0.00 USD | 0.00 USD | 10,560.00 USD |
| `1D` | `0.0925` | 759,480.00 USD | 0.00 USD | 759,480.00 USD | 3,270.00 USD | 2,170.00 USD | 11,180.00 USD |
| `7D` | `0.0926` | 915,240.00 USD | 0.00 USD | 915,240.00 USD | 1,790.00 USD | 0.00 USD | 8,180.00 USD |
| `7D` | `0.0932` | 905,270.00 USD | 0.00 USD | 905,270.00 USD | 0.00 USD | 0.00 USD | 12,240.00 USD |
| `1D` | `0.0933` | 742,860.00 USD | 0.00 USD | 742,860.00 USD | 0.00 USD | 0.00 USD | 6,860.00 USD |
| `7D` | `0.0935` | 893,030.00 USD | 0.00 USD | 893,030.00 USD | 0.00 USD | 1,320.00 USD | 6,490.00 USD |
| `1D` | `0.0937` | 736,000.00 USD | 0.00 USD | 736,000.00 USD | 0.00 USD | 0.00 USD | 64.09 USD |
| `7D` | `0.0938` | 885,220.00 USD | 0.00 USD | 885,220.00 USD | 0.00 USD | 0.00 USD | 8.57 USD |
| `1D` | `0.0939` | 735,930.00 USD | 0.00 USD | 735,930.00 USD | 0.00 USD | 0.00 USD | 76.92 USD |
| `7D` | `0.0941` | 885,210.00 USD | 0.00 USD | 885,210.00 USD | 2,050.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `0.0944` | 880,140.00 USD | 0.00 USD | 880,140.00 USD | 1,870.00 USD | 0.00 USD | 7,520.00 USD |
| `1D` | `0.0947` | 735,860.00 USD | 0.00 USD | 735,860.00 USD | 0.00 USD | 0.00 USD | 69.61 USD |
| `7D` | `0.0947` | 870,750.00 USD | 0.00 USD | 870,750.00 USD | 3,790.00 USD | 1,810.00 USD | 112.06 USD |
| `7D` | `0.0950` | 865,030.00 USD | 0.00 USD | 865,030.00 USD | 3,770.00 USD | 0.00 USD | 6,660.00 USD |
| `1D` | `0.0953` | 735,790.00 USD | 0.00 USD | 735,790.00 USD | 0.00 USD | 0.00 USD | 108.06 USD |
| `7D` | `0.0953` | 854,600.00 USD | 0.00 USD | 854,600.00 USD | 0.00 USD | 0.00 USD | 4.65 USD |
| `1D` | `0.0955` | 735,680.00 USD | 0.00 USD | 735,680.00 USD | 0.00 USD | 1,180.00 USD | 213.30 USD |
| `7D` | `0.0959` | 854,590.00 USD | 0.00 USD | 854,590.00 USD | 0.00 USD | 0.00 USD | 115.48 USD |
| `1D` | `0.0961` | 734,280.00 USD | 0.00 USD | 734,280.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0962` | 854,480.00 USD | 0.00 USD | 854,480.00 USD | 0.00 USD | 0.00 USD | 121.64 USD |
| `1D` | `0.0963` | 732,200.00 USD | 0.00 USD | 732,200.00 USD | 0.00 USD | 0.00 USD | 1.02 USD |
| `1D` | `0.0965` | 732,200.00 USD | 0.00 USD | 732,200.00 USD | 1,280.00 USD | 282.32 USD | 1,880.00 USD |
| `1D` | `0.0967` | 728,760.00 USD | 0.00 USD | 728,760.00 USD | 2,660.00 USD | 1,100.00 USD | 7,500.00 USD |
| `7D` | `0.0968` | 854,360.00 USD | 0.00 USD | 854,360.00 USD | 7,490.00 USD | 2,310.00 USD | 11,630.00 USD |
| `1D` | `0.0969` | 717,500.00 USD | 0.00 USD | 717,500.00 USD | 4,590.00 USD | 2,640.00 USD | 9,010.00 USD |
| `1D` | `0.0971` | 701,260.00 USD | 0.00 USD | 701,260.00 USD | 16,100.00 USD | 3,330.00 USD | 4,660.00 USD |
| `7D` | `0.0971` | 832,930.00 USD | 0.00 USD | 832,930.00 USD | 0.00 USD | 3,760.00 USD | 9,720.00 USD |
| `1D` | `0.0973` | 677,170.00 USD | 0.00 USD | 677,170.00 USD | 2,750.00 USD | 5,760.00 USD | 4,440.00 USD |
| `7D` | `0.0974` | 819,450.00 USD | 0.00 USD | 819,450.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD |
| `1D` | `0.0975` | 664,220.00 USD | 0.00 USD | 664,220.00 USD | 0.00 USD | 3,850.00 USD | 5,550.00 USD |
| `1D` | `0.0977` | 654,820.00 USD | 0.00 USD | 654,820.00 USD | 24,760.00 USD | 6,580.00 USD | 12,520.00 USD |
| `7D` | `0.0977` | 815,170.00 USD | 0.00 USD | 815,170.00 USD | 0.00 USD | 4,010.00 USD | 28,800.00 USD |
| `1D` | `0.0979` | 610,960.00 USD | 0.00 USD | 610,960.00 USD | 19,100.00 USD | 2,930.00 USD | 6,280.00 USD |
| `7D` | `0.0980` | 782,350.00 USD | 0.00 USD | 782,350.00 USD | 0.00 USD | 3,920.00 USD | 5,710.00 USD |
| `1D` | `0.0981` | 582,660.00 USD | 0.00 USD | 582,660.00 USD | 9,220.00 USD | 2,460.00 USD | 15,910.00 USD |
| `1D` | `0.0983` | 555,060.00 USD | 0.00 USD | 555,060.00 USD | 3,250.00 USD | 4,020.00 USD | 16,110.00 USD |
| `7D` | `0.0983` | 772,730.00 USD | 0.00 USD | 772,730.00 USD | 7,990.00 USD | 1,230.00 USD | 14,770.00 USD |
| `1D` | `0.0985` | 531,680.00 USD | 0.00 USD | 531,680.00 USD | 13,900.00 USD | 1,740.00 USD | 10,720.00 USD |
| `7D` | `0.0986` | 748,730.00 USD | 0.00 USD | 748,730.00 USD | 7,110.00 USD | 7,530.00 USD | 61,010.00 USD |
| `1D` | `0.0987` | 505,330.00 USD | 0.00 USD | 505,330.00 USD | 15,960.00 USD | 7,630.00 USD | 32,760.00 USD |
| `1D` | `0.0989` | 448,980.00 USD | 0.00 USD | 448,980.00 USD | 2,820.00 USD | 3,290.00 USD | 2,310.00 USD |
| `7D` | `0.0989` | 673,080.00 USD | 0.00 USD | 673,080.00 USD | 17,640.00 USD | 6,190.00 USD | 53,200.00 USD |
| `1D` | `0.0991` | 440,550.00 USD | 0.00 USD | 440,550.00 USD | 32,710.00 USD | 2,950.00 USD | 3,200.00 USD |
| `7D` | `0.0992` | 596,040.00 USD | 0.00 USD | 596,040.00 USD | 27,140.00 USD | 11,490.00 USD | 28,490.00 USD |
| `1D` | `0.0993` | 401,700.00 USD | 0.00 USD | 401,700.00 USD | 3,080.00 USD | 5,090.00 USD | 11,460.00 USD |
| `1D` | `0.0995` | 382,060.00 USD | 0.00 USD | 382,060.00 USD | 8,250.00 USD | 8,610.00 USD | 11,480.00 USD |
| `7D` | `0.0995` | 528,920.00 USD | 0.00 USD | 528,920.00 USD | 24,220.00 USD | 15,150.00 USD | 56,550.00 USD |
| `1D` | `0.0997` | 353,720.00 USD | 0.00 USD | 353,720.00 USD | 35,260.00 USD | 8,860.00 USD | 27,200.00 USD |
| `7D` | `0.0998` | 433,000.00 USD | 0.00 USD | 433,000.00 USD | 28,450.00 USD | 12,100.00 USD | 80,720.00 USD |
| `1D` | `0.0999` | 282,400.00 USD | 0.00 USD | 282,400.00 USD | 44,410.00 USD | 6,710.00 USD | 26,450.00 USD |
| `1D` | `0.1001` | 204,830.00 USD | 0.00 USD | 204,830.00 USD | 27,550.00 USD | 5,470.00 USD | 21,230.00 USD |
| `7D` | `0.1001` | 311,730.00 USD | 0.00 USD | 311,730.00 USD | 36,110.00 USD | 8,650.00 USD | 13,120.00 USD |
| `1D` | `0.1003` | 150,580.00 USD | 0.00 USD | 150,580.00 USD | 0.00 USD | 5,820.00 USD | 21,280.00 USD |
| `7D` | `0.1004` | 253,840.00 USD | 0.00 USD | 253,840.00 USD | 22,470.00 USD | 16,470.00 USD | 23,430.00 USD |
| `1D` | `0.1005` | 123,480.00 USD | 0.00 USD | 123,480.00 USD | 18,440.00 USD | 3,050.00 USD | 30,010.00 USD |
| `1D` | `0.1007` | 71,980.00 USD | 0.00 USD | 71,980.00 USD | 0.00 USD | 11,300.00 USD | 56,700.00 USD |
| `7D` | `0.1007` | 191,470.00 USD | 0.00 USD | 191,470.00 USD | 20,870.00 USD | 3,870.00 USD | 100,230.00 USD |
| `7D` | `0.1010` | 66,500.00 USD | 0.00 USD | 66,500.00 USD | 17,340.00 USD | 6,580.00 USD | 6,630.00 USD |
| `1D` | `0.1011` | 3,980.00 USD | 0.00 USD | 3,980.00 USD | 0.00 USD | 0.00 USD | 3,390.00 USD |
| `1D` | `0.1013` | 587.32 USD | 0.00 USD | 587.32 USD | 0.00 USD | 0.00 USD | 587.32 USD |
| `7D` | `0.1013` | 35,940.00 USD | 0.00 USD | 35,940.00 USD | 15,270.00 USD | 5,230.00 USD | 0.00 USD |
| `7D` | `0.1016` | 15,440.00 USD | 0.00 USD | 15,440.00 USD | 15,440.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1018` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1019` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1019` | 12,100.00 USD | 12,100.00 USD | 0.00 USD | 12,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1022` | 32,280.00 USD | 32,280.00 USD | 0.00 USD | 11,930.00 USD | 8,250.00 USD | 0.00 USD |
| `7D` | `0.1025` | 33,830.00 USD | 33,830.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1028` | 42,020.00 USD | 42,020.00 USD | 0.00 USD | 3,800.00 USD | 4,390.00 USD | 0.00 USD |
| `1D` | `0.1031` | 46,790.00 USD | 46,790.00 USD | 0.00 USD | 27,910.00 USD | 0.00 USD | 18,880.00 USD |
| `7D` | `0.1031` | 67,840.00 USD | 67,840.00 USD | 0.00 USD | 19,560.00 USD | 6,260.00 USD | 0.00 USD |
| `1D` | `0.1033` | 72,010.00 USD | 72,010.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | 21,860.00 USD |
| `7D` | `0.1034` | 93,790.00 USD | 93,790.00 USD | 0.00 USD | 18,920.00 USD | 7,030.00 USD | 0.00 USD |
| `1D` | `0.1035` | 95,220.00 USD | 95,220.00 USD | 0.00 USD | 10,280.00 USD | 12,870.00 USD | 54.66 USD |
| `1D` | `0.1037` | 152,630.00 USD | 152,630.00 USD | 0.00 USD | 37,310.00 USD | 20,100.00 USD | 0.00 USD |
| `7D` | `0.1037` | 107,210.00 USD | 107,210.00 USD | 0.00 USD | 2,710.00 USD | 10,710.00 USD | 0.00 USD |
| `1D` | `0.1039` | 170,920.00 USD | 170,920.00 USD | 0.00 USD | 6,500.00 USD | 9,220.00 USD | 2,570.00 USD |
| `7D` | `0.1040` | 154,810.00 USD | 154,810.00 USD | 0.00 USD | 5,940.00 USD | 10,300.00 USD | 31,350.00 USD |
| `1D` | `0.1041` | 211,290.00 USD | 211,290.00 USD | 0.00 USD | 6,450.00 USD | 16,880.00 USD | 17,030.00 USD |
| `1D` | `0.1043` | 243,480.00 USD | 243,480.00 USD | 0.00 USD | 0.00 USD | 10,910.00 USD | 21,280.00 USD |
| `7D` | `0.1043` | 176,750.00 USD | 176,750.00 USD | 0.00 USD | 15,960.00 USD | 5,980.00 USD | 0.00 USD |
| `1D` | `0.1045` | 253,270.00 USD | 253,270.00 USD | 0.00 USD | 0.00 USD | 4,840.00 USD | 4,950.00 USD |
| `7D` | `0.1046` | 246,720.00 USD | 246,720.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD | 60,160.00 USD |
| `1D` | `0.1047` | 327,410.00 USD | 327,410.00 USD | 0.00 USD | 31,470.00 USD | 6,050.00 USD | 36,620.00 USD |
| `1D` | `0.1049` | 444,830.00 USD | 444,830.00 USD | 0.00 USD | 37,390.00 USD | 13,300.00 USD | 66,730.00 USD |
| `7D` | `0.1049` | 371,150.00 USD | 371,150.00 USD | 0.00 USD | 34,790.00 USD | 6,530.00 USD | 83,110.00 USD |
| `1D` | `0.1051` | 508,180.00 USD | 508,180.00 USD | 0.00 USD | 30,370.00 USD | 8,750.00 USD | 24,230.00 USD |
| `7D` | `0.1052` | 548,910.00 USD | 548,910.00 USD | 0.00 USD | 28,200.00 USD | 24,160.00 USD | 125,400.00 USD |
| `1D` | `0.1053` | 604,660.00 USD | 604,660.00 USD | 0.00 USD | 35,030.00 USD | 10,620.00 USD | 50,830.00 USD |
| `1D` | `0.1055` | 738,160.00 USD | 738,160.00 USD | 0.00 USD | 46,710.00 USD | 27,100.00 USD | 59,700.00 USD |
| `7D` | `0.1055` | 927,650.00 USD | 927,650.00 USD | 0.00 USD | 122,840.00 USD | 44,430.00 USD | 211,460.00 USD |
| `1D` | `0.1057` | 832,730.00 USD | 832,730.00 USD | 0.00 USD | 27,300.00 USD | 17,200.00 USD | 50,060.00 USD |
| `7D` | `0.1058` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 105,620.00 USD | 56,540.00 USD | 189,110.00 USD |
| `1D` | `0.1059` | 974,050.00 USD | 974,050.00 USD | 0.00 USD | 39,020.00 USD | 4,070.00 USD | 98,230.00 USD |
| `1D` | `0.1061` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 33,450.00 USD | 1,890.00 USD | 65,210.00 USD |
| `7D` | `0.1061` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 75,540.00 USD | 72,260.00 USD | 118,330.00 USD |
| `1D` | `0.1063` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 25,200.00 USD | 2,030.00 USD | 75,940.00 USD |
| `7D` | `0.1064` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 52,580.00 USD | 192,520.00 USD |
| `1D` | `0.1065` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 2,630.00 USD | 25,740.00 USD |
| `1D` | `0.1067` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 8,230.00 USD | 1,320.00 USD | 41,190.00 USD |
| `7D` | `0.1067` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 51,740.00 USD | 156,150.00 USD |
| `1D` | `0.1069` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 8,170.00 USD | 5,440.00 USD | 70,600.00 USD |
| `7D` | `0.1070` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 57,770.00 USD | 134,670.00 USD |
| `1D` | `0.1071` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 3,140.00 USD | 16,220.00 USD |
| `1D` | `0.1073` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 243.10 USD |
| `7D` | `0.1073` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 17,700.00 USD | 0.00 USD |
| `1D` | `0.1075` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 125.64 USD |
| `7D` | `0.1076` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,500.00 USD |
| `1D` | `0.1077` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 77.28 USD |
| `1D` | `0.1079` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,160.00 USD |
| `7D` | `0.1079` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 79.36 USD |
| `7D` | `0.1082` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 89.24 USD |
| `1D` | `0.1083` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 7,990.00 USD | 5,910.00 USD | 7,180.00 USD |
| `1D` | `0.1085` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65,020.00 USD |
| `7D` | `0.1085` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1087` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 28,490.00 USD | 2,240.00 USD | 44,670.00 USD |
| `7D` | `0.1088` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 5,290.00 USD | 0.00 USD | 113.96 USD |
| `1D` | `0.1089` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 37,180.00 USD | 0.00 USD | 108.06 USD |
| `1D` | `0.1091` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 33,700.00 USD | 0.00 USD | 16.51 USD |
| `7D` | `0.1091` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD |
| `1D` | `0.1093` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 15,480.00 USD | 0.00 USD | 222.36 USD |
| `7D` | `0.1094` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD |
| `1D` | `0.1095` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 21,520.00 USD |
| `1D` | `0.1097` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 7,260.00 USD | 1,970.00 USD | 22,790.00 USD |
| `7D` | `0.1097` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1099` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 6,130.00 USD | 1,940.00 USD | 0.00 USD |
| `7D` | `0.1100` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 21,840.00 USD |
| `1D` | `0.1101` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 4,310.00 USD | 2,820.00 USD | 4,290.00 USD |
| `1D` | `0.1103` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 3,540.00 USD | 5,640.00 USD | 0.00 USD |
| `7D` | `0.1103` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 17,490.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1105` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 3,380.00 USD | 4,740.00 USD | 10,700.00 USD |
| `7D` | `0.1106` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 22,880.00 USD | 16,040.00 USD |
| `1D` | `0.1107` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 3,110.00 USD | 12,720.00 USD | 35,750.00 USD |
| `1D` | `0.1109` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 2,110.00 USD | 1,120.00 USD | 0.00 USD |
| `7D` | `0.1109` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 16,540.00 USD | 0.00 USD |
| `1D` | `0.1111` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 5,200.00 USD | 0.00 USD | 96.09 USD |
| `7D` | `0.1112` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 35.29 USD |
| `1D` | `0.1113` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 21,390.00 USD | 5,880.00 USD | 39,070.00 USD |
| `1D` | `0.1115` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 4,760.00 USD | 465.26 USD | 0.00 USD |
| `1D` | `0.1117` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 2,060.00 USD | 26,110.00 USD | 34,770.00 USD |
| `7D` | `0.1118` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 22,520.00 USD | 29,830.00 USD | 27,290.00 USD |
| `1D` | `0.1119` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 33,110.00 USD | 8,300.00 USD | 36,740.00 USD |
| `1D` | `0.1121` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 21,300.00 USD | 12,810.00 USD | 12,320.00 USD |
| `7D` | `0.1121` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 17,760.00 USD | 0.00 USD | 38,370.00 USD |
| `1D` | `0.1123` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 36,220.00 USD | 2,290.00 USD | 8,450.00 USD |
| `7D` | `0.1124` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 12,360.00 USD | 23,980.00 USD | 66,610.00 USD |
| `1D` | `0.1125` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 11,130.00 USD | 13,990.00 USD | 11,730.00 USD |
| `1D` | `0.1127` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 1,250.00 USD | 19,520.00 USD |
| `7D` | `0.1127` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 2,230.00 USD | 15,310.00 USD |
| `1D` | `0.1129` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 10,120.00 USD | 0.00 USD | 3,210.00 USD |
| `7D` | `0.1130` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,260.00 USD |
| `1D` | `0.1131` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 20,830.00 USD | 8,530.00 USD | 22,800.00 USD |
| `1D` | `0.1133` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 6,530.00 USD | 22,520.00 USD | 23,470.00 USD |
| `7D` | `0.1133` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 12,540.00 USD | 11,430.00 USD | 8,170.00 USD |
| `1D` | `0.1135` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 4,040.00 USD | 3,670.00 USD | 4,090.00 USD |
| `7D` | `0.1136` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD |
| `1D` | `0.1137` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 856.93 USD | 40.44 USD |
| `1D` | `0.1139` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,270.00 USD |
| `7D` | `0.1139` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD |
| `1D` | `0.1141` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 13,860.00 USD | 2,800.00 USD | 20,340.00 USD |
| `7D` | `0.1142` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD |
| `1D` | `0.1143` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 20,300.00 USD | 27,990.00 USD | 11,820.00 USD |
| `1D` | `0.1145` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 13,430.00 USD | 11,690.00 USD | 38,100.00 USD |
| `7D` | `0.1145` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 16,540.00 USD | 2,730.00 USD | 219,770.00 USD |
| `1D` | `0.1147` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 10,640.00 USD | 10,080.00 USD | 30,670.00 USD |
| `7D` | `0.1148` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 175,990.00 USD |
| `1D` | `0.1149` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 35,170.00 USD | 624.71 USD | 31,750.00 USD |
| `1D` | `0.1150` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 6,880.00 USD | 13,020.00 USD | 9,310.00 USD |
| `7D` | `0.1151` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 103,130.00 USD | 4,210.00 USD | 163,580.00 USD |
| `7D` | `0.1154` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 243,190.00 USD | 26,970.00 USD | 195,390.00 USD |
| `7D` | `0.1157` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 188,950.00 USD | 25,290.00 USD | 98,310.00 USD |
| `7D` | `0.1160` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 131,160.00 USD | 32,830.00 USD | 109,320.00 USD |
| `7D` | `0.1163` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 142,050.00 USD | 28,590.00 USD | 112,710.00 USD |
| `7D` | `0.1166` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 130,810.00 USD | 46,040.00 USD | 42,360.00 USD |
| `7D` | `0.1169` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 82,770.00 USD | 26,150.00 USD | 112,810.00 USD |
| `7D` | `0.1172` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 64,270.00 USD | 14,930.00 USD | 48,810.00 USD |
| `7D` | `0.1175` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 72,770.00 USD | 17,930.00 USD | 81,630.00 USD |
| `7D` | `0.1178` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 89,510.00 USD | 23,660.00 USD | 55,770.00 USD |
| `7D` | `0.1181` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 32,770.00 USD | 23,410.00 USD | 29,770.00 USD |
| `7D` | `0.1184` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 11,640.00 USD | 5,170.00 USD | 48,080.00 USD |
| `7D` | `0.1187` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 5,620.00 USD | 17,120.00 USD | 54,960.00 USD |
| `7D` | `0.1190` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 29,530.00 USD | 29,230.00 USD | 86,300.00 USD |
| `7D` | `0.1193` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 41,630.00 USD | 1,160.00 USD | 38,670.00 USD |
| `7D` | `0.1196` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 17,970.00 USD | 1,780.00 USD | 40,330.00 USD |
| `7D` | `0.1199` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 9,100.00 USD | 13,190.00 USD | 67,980.00 USD |
| `7D` | `0.1202` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 138,430.00 USD | 21,430.00 USD | 32,790.00 USD |
| `7D` | `0.1205` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 132,960.00 USD | 72,910.00 USD | 130,900.00 USD |
| `7D` | `0.1208` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 39,480.00 USD | 25,720.00 USD | 66,520.00 USD |
| `7D` | `0.1211` | 7,200,000.00 USD | 7,200,000.00 USD | 0.00 USD | 72,500.00 USD | 25,920.00 USD | 111,160.00 USD |
| `7D` | `0.1214` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 23,920.00 USD | 19,420.00 USD | 76,300.00 USD |
| `7D` | `0.1217` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 24,400.00 USD | 6,160.00 USD | 18,300.00 USD |
| `7D` | `0.1220` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 45,700.00 USD | 10,970.00 USD | 54,700.00 USD |
| `7D` | `0.1223` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 76,930.00 USD | 24,740.00 USD | 45,660.00 USD |
| `7D` | `0.1226` | 7,720,000.00 USD | 7,720,000.00 USD | 0.00 USD | 54,940.00 USD | 27,490.00 USD | 5,210.00 USD |
| `7D` | `0.1229` | 7,900,000.00 USD | 7,900,000.00 USD | 0.00 USD | 71,850.00 USD | 38,040.00 USD | 73,860.00 USD |
| `7D` | `0.1232` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 51,420.00 USD | 14,500.00 USD | 68,270.00 USD |
| `7D` | `0.1235` | 8,070,000.00 USD | 8,070,000.00 USD | 0.00 USD | 15,040.00 USD | 5,390.00 USD | 17,120.00 USD |
| `7D` | `0.1238` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 8,310.00 USD | 3,610.00 USD | 3,100.00 USD |
| `7D` | `0.1241` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 11,380.00 USD | 1,380.00 USD | 7,090.00 USD |
| `7D` | `0.1244` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 26,540.00 USD | 8,130.00 USD | 9,660.00 USD |
| `7D` | `0.1247` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 7,900.00 USD | 12,590.00 USD | 15,120.00 USD |
| `7D` | `0.1250` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 8,540.00 USD | 4,990.00 USD | 5,780.00 USD |
| `7D` | `0.1253` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 1,550.00 USD | 0.00 USD | 13,880.00 USD |
| `7D` | `0.1256` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 3,800.00 USD | 4,390.00 USD | 220.44 USD |
| `7D` | `0.1259` | 8,240,000.00 USD | 8,240,000.00 USD | 0.00 USD | 5,870.00 USD | 1,190.00 USD | 121.42 USD |
| `7D` | `0.1262` | 8,240,000.00 USD | 8,240,000.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | 3,530.00 USD |
| `7D` | `0.1265` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 2,710.00 USD | 0.00 USD | 7,330.00 USD |
| `7D` | `0.1268` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,920.00 USD |
| `7D` | `0.1271` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 5,940.00 USD | 0.00 USD | 30.15 USD |
| `7D` | `0.1274` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12.00 USD |
| `7D` | `0.1277` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20.66 USD |
| `7D` | `0.1280` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,380.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `61.42M` | Total OI Tokens: `621,147,373.4 OP`
  * 1h OI Change: `+2.04%` | 4h OI Change: `-5.81%` | 24h OI Change: `-15.31%`
  * Exchange Breakdown: Binance=`13.53M` | Bybit=`12.33M` | OKX=`3.55M` | Hyperliquid=`3.05M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-3.50K` | Last 24h: `-2.42K` | Last 3d: `-6.63K` | Last 7d: `-14.48K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0346%` | **USDT OKX** | `-0.0005%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0346%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0053%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `52.55%` | `47.45%` | `1.11` | 1,210,000.00 USD |
| `15M` | `Binance` | `50.08%` | `49.92%` | `1.00` | 466,970.00 USD |
| `15M` | `OKX` | `60.31%` | `39.69%` | `1.52` | 150,860.00 USD |
| `15M` | `Bybit` | `50.04%` | `49.96%` | `1.00` | 152,260.00 USD |
| `15M` | `KuCoin` | `49.5%` | `50.5%` | `0.98` | 123,620.00 USD |
| `15M` | `Gate` | `43.35%` | `56.65%` | `0.77` | 36,590.00 USD |
| `15M` | `Bitget` | `40.37%` | `59.63%` | `0.68` | 82,980.00 USD |
| `15M` | `BingX` | `64.32%` | `35.68%` | `1.80` | 41,870.00 USD |
| `15M` | `MEXC` | `82.79%` | `17.21%` | `4.81` | 62,190.00 USD |
| `15M` | `Bitunix` | `55.02%` | `44.98%` | `1.22` | 14,160.00 USD |
| `15M` | `Hyperliquid` | `58.15%` | `41.85%` | `1.39` | 13,240.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.16%` | `49.84%` | `1.01` | 51,670.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `32.3%` | `67.7%` | `0.48` | 12,240.00 USD |
| `15M` | `HTX` | `70.11%` | `29.89%` | `2.35` | 0.60 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `98.57%` | `1.43%` | `68.93` | 1,460.00 USD |
| `15M` | `Aster` | `81.92%` | `18.08%` | `4.53` | 764.57 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `2.04%` | `97.96%` | `0.02` | 2,180.00 USD |
| `15M` | `Whale Positions` | `50.08%` | `49.92%` | `1.00` | 466,970.00 USD |
| `15M` | `Global Accounts` | `52.55%` | `47.45%` | `1.11` | 1,210,000.00 USD |
| `1H` | `OP` | `48.46%` | `51.54%` | `0.94` | 6,000,000.00 USD |
| `1H` | `Binance` | `53.85%` | `46.15%` | `1.17` | 2,340,000.00 USD |
| `1H` | `OKX` | `55.61%` | `44.39%` | `1.25` | 620,330.00 USD |
| `1H` | `Bybit` | `53.34%` | `46.66%` | `1.14` | 778,210.00 USD |
| `1H` | `KuCoin` | `50.56%` | `49.44%` | `1.02` | 375,780.00 USD |
| `1H` | `Gate` | `59.29%` | `40.71%` | `1.46` | 255,640.00 USD |
| `1H` | `Bitget` | `56.16%` | `43.84%` | `1.28` | 147,940.00 USD |
| `1H` | `BingX` | `10.48%` | `89.52%` | `0.12` | 674,820.00 USD |
| `1H` | `MEXC` | `55.07%` | `44.93%` | `1.23` | 309,700.00 USD |
| `1H` | `Bitunix` | `54.26%` | `45.74%` | `1.19` | 126,940.00 USD |
| `1H` | `Hyperliquid` | `37.26%` | `62.74%` | `0.59` | 78,510.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.23%` | `49.77%` | `1.01` | 166,100.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `21.03%` | `78.97%` | `0.27` | 70,070.00 USD |
| `1H` | `HTX` | `65.22%` | `34.78%` | `1.88` | 3,270.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `45.59%` | `54.41%` | `0.84` | 35,530.00 USD |
| `1H` | `Aster` | `48.61%` | `51.39%` | `0.95` | 6,130.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `14.14%` | `85.86%` | `0.16` | 5,430.00 USD |
| `1H` | `Whale Positions` | `53.85%` | `46.15%` | `1.17` | 2,340,000.00 USD |
| `1H` | `Global Accounts` | `48.46%` | `51.54%` | `0.94` | 6,000,000.00 USD |
| `4H` | `OP` | `45.44%` | `54.56%` | `0.83` | 46,340,000.00 USD |
| `4H` | `Binance` | `47.51%` | `52.49%` | `0.91` | 16,570,000.00 USD |
| `4H` | `OKX` | `46.6%` | `53.4%` | `0.87` | 5,250,000.00 USD |
| `4H` | `Bybit` | `50.2%` | `49.8%` | `1.01` | 6,500,000.00 USD |
| `4H` | `KuCoin` | `49.22%` | `50.78%` | `0.97` | 2,280,000.00 USD |
| `4H` | `Gate` | `49.86%` | `50.14%` | `0.99` | 1,580,000.00 USD |
| `4H` | `Bitget` | `47.17%` | `52.83%` | `0.89` | 2,200,000.00 USD |
| `4H` | `BingX` | `28.97%` | `71.03%` | `0.41` | 5,110,000.00 USD |
| `4H` | `MEXC` | `39.76%` | `60.24%` | `0.66` | 2,190,000.00 USD |
| `4H` | `Bitunix` | `41.58%` | `58.42%` | `0.71` | 832,780.00 USD |
| `4H` | `Hyperliquid` | `45.16%` | `54.84%` | `0.82` | 1,170,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.83%` | `51.17%` | `0.95` | 904,590.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `52.07%` | `47.93%` | `1.09` | 1,250,000.00 USD |
| `4H` | `HTX` | `42.99%` | `57.01%` | `0.75` | 70,090.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `39.25%` | `60.75%` | `0.65` | 188,020.00 USD |
| `4H` | `Aster` | `43.53%` | `56.47%` | `0.77` | 214,370.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `40.5%` | `59.5%` | `0.68` | 27,440.00 USD |
| `4H` | `Whale Positions` | `47.51%` | `52.49%` | `0.91` | 16,570,000.00 USD |
| `4H` | `Global Accounts` | `45.44%` | `54.56%` | `0.83` | 46,340,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1009` | `0.1006` | `0.1009` | `0.1013` | `0.0997` | 1,149,511.09 USD | 547,931.78 USD | 601,579.31 USD | -53,647.52 USD | `-4.67%` | `21B / 22S` |
| `5:00 UTC` | `0.0960` | `0.0967` | `0.0960` | `0.1006` | `0.0934` | 4,791,089.79 USD | 1,923,208.78 USD | 2,867,881.01 USD | -944,672.24 USD | `-19.72%` | `3B / 31S` |
| `0:00 UTC` | `0.0971` | `0.0965` | `0.0971` | `0.0976` | `0.0950` | 1,644,964.43 USD | 774,292.52 USD | 870,671.91 USD | -96,379.38 USD | `-5.86%` | `7B / 10S` |
| `5:00 UTC` | `0.0980` | `0.0979` | `0.0980` | `0.0985` | `0.0973` | 570,200.75 USD | 281,124.62 USD | 289,076.13 USD | -7,951.51 USD | `-1.39%` | `14B / 18S` |
| `0:00 UTC` | `0.0975` | `0.0979` | `0.0975` | `0.0986` | `0.0974` | 804,903.10 USD | 383,442.13 USD | 421,460.97 USD | -38,018.84 USD | `-4.72%` | `19B / 10S` |
| `5:00 UTC` | `0.0975` | `0.0979` | `0.0975` | `0.0985` | `0.0974` | 475,336.52 USD | 238,056.50 USD | 237,280.02 USD | 776.48 USD | `+0.16%` | `24B / 11S` |
| `0:00 UTC` | `0.0965` | `0.0976` | `0.0965` | `0.0984` | `0.0965` | 753,212.73 USD | 453,281.85 USD | 299,930.89 USD | 153,350.96 USD | `+20.36%` | `57B / 22S` |
| `5:00 UTC` | `0.0972` | `0.0974` | `0.0972` | `0.0980` | `0.0971` | 337,745.57 USD | 158,183.47 USD | 179,562.09 USD | -21,378.62 USD | `-6.33%` | `9B / 16S` |
| `0:00 UTC` | `0.0974` | `0.0974` | `0.0974` | `0.0983` | `0.0965` | 539,770.34 USD | 320,150.60 USD | 219,619.74 USD | 100,530.85 USD | `+18.62%` | `53B / 10S` |
| `5:00 UTC` | `0.0983` | `0.0984` | `0.0983` | `0.0987` | `0.0981` | 257,595.70 USD | 148,258.10 USD | 109,337.60 USD | 38,920.50 USD | `+15.11%` | `12B / 5S` |

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
| `5m` | 6,090.00 USD | 32,850.00 USD | **`ACCUMULATION`** |
| `15m` | 25,190.00 USD | 108,440.00 USD | **`ACCUMULATION`** |
| `30m` | 25,070.00 USD | 262,150.00 USD | **`ACCUMULATION`** |
| `1h` | 23,630.00 USD | 491,900.00 USD | **`ACCUMULATION`** |
| `2h` | 55,090.00 USD | 331,170.00 USD | **`ACCUMULATION`** |
| `4h` | 222,220.00 USD | -1,450,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 108,000.00 USD | -4,040,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 140,660.00 USD | -4,450,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 233,690.00 USD | -4,410,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 328,510.00 USD | -4,720,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -18,430.00 USD | -14,410,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,170,000.00 USD | -82,730,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+6.09K` | 15m=`+25.19K` | 1h=`+23.63K` | 24h=`+328.51K`
* Futures Capital Netflows: 5m=`+32.85K` | 15m=`+108.44K` | 1h=`+491.90K` | 24h=`-4.72M`
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
  * `2026-10-30 07:16:25 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:52:25 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:52:25 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 07:52:25 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:53:25 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:53:25 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:53:25 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:25 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:53:25 IST`: [sec.gov] - (Sentiment: `Neutral`)


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
