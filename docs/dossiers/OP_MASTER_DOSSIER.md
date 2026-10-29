# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 01:02:38 IST` (`2026-10-29 19:32:38 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1097` | `0.1101` | `0.1096` | `0.1097` | `421,028` | 46,248.11 USD | 8,176.43 USD | `+17.68%` | -968,888.40 USD | `+0.22` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1097` | `0.1099` | `0.1096` | `0.1098` | `611,121` | 67,073.30 USD | 12,546.06 USD | `+18.71%` | -956,342.34 USD | `+0.27` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.1098` | `0.1101` | `0.1097` | `0.1101` | `496,652` | 54,619.33 USD | 13,991.79 USD | `+25.62%` | -942,350.55 USD | `+0.31` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1099` | `0.1104` | `0.1095` | `0.1100` | `2,487,385` | 273,714.46 USD | 58,107.08 USD | `+21.23%` | -945,303.97 USD | `+0.90` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1100` | `0.1101` | `0.1096` | `0.1097` | `2,052,238` | 225,346.74 USD | 7,262.60 USD | `+3.22%` | -938,041.37 USD | `+0.25` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1097` | `0.1101` | `0.1096` | `0.1101` | `1,107,772` | 121,692.63 USD | 26,537.86 USD | `+21.81%` | -911,503.51 USD | `+0.49` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.1129` | `0.1132` | `0.1101` | `0.1112` | `18,847,741` | 2,100,824.13 USD | -168,750.74 USD | `-8.03%` | -1,180,941.15 USD | `-0.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1112` | `0.1113` | `0.1094` | `0.1100` | `13,608,224` | 1,499,374.47 USD | -1,041.31 USD | `-0.07%` | -1,181,982.46 USD | `+0.26` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1100` | `0.1101` | `0.1096` | `0.1101` | `3,160,010` | 347,039.37 USD | 33,800.46 USD | `+9.74%` | -1,148,182.00 USD | `+0.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,229,700.44 USD | `+0.64` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -888,444.84 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `57,087,731` | 6,384,726.20 USD | -259,737.16 USD | `-4.07%` | -1,148,182.00 USD | `-0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1131` | `0.1136` | `0.1072` | `0.1085` | `76,338,549` | 8,353,905.81 USD | -1,528,374.61 USD | `-18.30%` | -1,480,991.26 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1085` | `0.1106` | `0.1071` | `0.1076` | `47,048,931` | 5,111,570.05 USD | 108,567.99 USD | `+2.12%` | -1,372,423.27 USD | `+0.75` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,229,700.44 USD | `+0.64` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -888,444.84 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `57,087,731` | 6,384,726.20 USD | -259,737.16 USD | `-4.07%` | -1,148,182.00 USD | `-0.11` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:53:52 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1113` | 5,402.00 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 5.40K USD at 0.1113 USD [API] | `2026-10-27 22:27:10` |
| `ANNOUNCEMENT` | `INFO` | `0.1113` | 5,401.99 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale SELL: 5.40K USD at 0.1113 USD [API] | `2026-10-27 22:27:10` |


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
| `Live` | `Long Liquidation` | `0.0405` | 183.72 USD | 243,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0445` | 267.00 USD | 242,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 3,520.00 USD | 242,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 3,460.00 USD | 239,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0555` | 282.99 USD | 235,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 829.69 USD | 235,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 1,100.00 USD | 234,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 353.81 USD | 233,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 1,040.00 USD | 233,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 1,920.00 USD | 232,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 25,370.00 USD | 230,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 48,850.00 USD | 204,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 1,020.00 USD | 156,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 1,170.00 USD | 154,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 995.43 USD | 153,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 1,320.00 USD | 152,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 1,110.00 USD | 151,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 1,560.00 USD | 150,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 2,400.00 USD | 148,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,120.00 USD | 146,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 443.16 USD | 143,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 16,670.00 USD | 142,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 69,120.00 USD | 126,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 5,610.00 USD | 57,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 419.87 USD | 51,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0975` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 2,560.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0975` | 12,670.00 USD | 51,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0977` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 5,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0979` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 1,530.00 USD | 5,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0981` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 5,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 3,920,000.00 USD | 3,920,000.00 USD | 7,990.00 USD | 1,230.00 USD | 8,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0984` | 1,990,000.00 USD | 1,990,000.00 USD | 8,920.00 USD | 1,070.00 USD | 9,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0985` | 3,900,000.00 USD | 3,900,000.00 USD | 7,110.00 USD | 0.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0985` | 19,960.00 USD | 38,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0986` | 1,970,000.00 USD | 1,970,000.00 USD | 5,370.00 USD | 2,610.00 USD | 4,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0987` | 3,880,000.00 USD | 3,880,000.00 USD | 5,390.00 USD | 9,190.00 USD | 37,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0988` | 1,960,000.00 USD | 1,960,000.00 USD | 4,240.00 USD | 1,920.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 3,830,000.00 USD | 3,830,000.00 USD | 12,260.00 USD | 4,520.00 USD | 27,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0990` | 1,950,000.00 USD | 1,950,000.00 USD | 3,980.00 USD | 3,340.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0991` | 3,790,000.00 USD | 3,790,000.00 USD | 14,350.00 USD | 10,350.00 USD | 13,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0992` | 1,940,000.00 USD | 1,940,000.00 USD | 1,470.00 USD | 1,190.00 USD | 7,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0993` | 3,750,000.00 USD | 3,750,000.00 USD | 23,920.00 USD | 10,140.00 USD | 24,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0994` | 1,930,000.00 USD | 1,930,000.00 USD | 3,200.00 USD | 820.70 USD | 7,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 3,690,000.00 USD | 3,690,000.00 USD | 13,090.00 USD | 6,160.00 USD | 25,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0996` | 1,920,000.00 USD | 1,920,000.00 USD | 2,640.00 USD | 624.33 USD | 10,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0997` | 3,650,000.00 USD | 3,650,000.00 USD | 21,100.00 USD | 5,500.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0998` | 1,900,000.00 USD | 1,900,000.00 USD | 2,690.00 USD | 1,690.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0999` | 3,590,000.00 USD | 3,590,000.00 USD | 14,230.00 USD | 6,540.00 USD | 18,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1000` | 1,890,000.00 USD | 1,890,000.00 USD | 2,760.00 USD | 3,370.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 3,550,000.00 USD | 3,550,000.00 USD | 29,230.00 USD | 3,010.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1002` | 1,880,000.00 USD | 1,880,000.00 USD | 2,660.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1003` | 3,510,000.00 USD | 3,510,000.00 USD | 8,010.00 USD | 7,060.00 USD | 5,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1004` | 1,880,000.00 USD | 1,880,000.00 USD | 1,970.00 USD | 0.00 USD | 1,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1005` | 3,480,000.00 USD | 3,480,000.00 USD | 25,070.00 USD | 11,000.00 USD | 18,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1005` | 427.25 USD | 18,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1006` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 403.62 USD | 803.25 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 3,430,000.00 USD | 3,430,000.00 USD | 10,260.00 USD | 2,280.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1008` | 1,870,000.00 USD | 1,870,000.00 USD | 1,250.00 USD | 1,630.00 USD | 26.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1009` | 3,400,000.00 USD | 3,400,000.00 USD | 15,320.00 USD | 3,070.00 USD | 6,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1010` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 2,120.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1011` | 3,380,000.00 USD | 3,380,000.00 USD | 4,430.00 USD | 4,720.00 USD | 9,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1012` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 800.79 USD | 997.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 3,360,000.00 USD | 3,360,000.00 USD | 12,870.00 USD | 4,030.00 USD | 3,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1014` | 1,860,000.00 USD | 1,860,000.00 USD | 4,900.00 USD | 1,830.00 USD | 608.26 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1015` | 3,340,000.00 USD | 3,340,000.00 USD | 6,830.00 USD | 965.35 USD | 2,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1015` | 622.37 USD | 17,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1016` | 1,860,000.00 USD | 1,860,000.00 USD | 2,200.00 USD | 2,540.00 USD | 5,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1017` | 3,330,000.00 USD | 3,330,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1018` | 1,850,000.00 USD | 1,850,000.00 USD | 827.81 USD | 4,170.00 USD | 7,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1019` | 3,310,000.00 USD | 3,310,000.00 USD | 9,260.00 USD | 5,790.00 USD | 13,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1020` | 1,830,000.00 USD | 1,830,000.00 USD | 6,440.00 USD | 2,630.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1021` | 3,280,000.00 USD | 3,280,000.00 USD | 7,900.00 USD | 3,270.00 USD | 7,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1022` | 1,820,000.00 USD | 1,820,000.00 USD | 5,070.00 USD | 2,120.00 USD | 7,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1023` | 3,260,000.00 USD | 3,260,000.00 USD | 4,030.00 USD | 4,990.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1024` | 1,810,000.00 USD | 1,810,000.00 USD | 2,300.00 USD | 947.50 USD | 4,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1025` | 3,240,000.00 USD | 3,240,000.00 USD | 1,550.00 USD | 0.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1025` | 17,360.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1026` | 1,800,000.00 USD | 1,800,000.00 USD | 2,780.00 USD | 2,210.00 USD | 2,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1027` | 3,230,000.00 USD | 3,230,000.00 USD | 2,250.00 USD | 2,580.00 USD | 466.12 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1028` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 936.16 USD | 88.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1029` | 3,230,000.00 USD | 3,230,000.00 USD | 7,420.00 USD | 3,000.00 USD | 735.27 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1030` | 1,790,000.00 USD | 1,790,000.00 USD | 8,870.00 USD | 3,480.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1031` | 3,220,000.00 USD | 3,220,000.00 USD | 13,690.00 USD | 5,070.00 USD | 10,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1032` | 1,770,000.00 USD | 1,770,000.00 USD | 11,310.00 USD | 2,260.00 USD | 5,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1033` | 3,190,000.00 USD | 3,190,000.00 USD | 3,880.00 USD | 2,640.00 USD | 15,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1034` | 1,750,000.00 USD | 1,750,000.00 USD | 7,190.00 USD | 5,040.00 USD | 11,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1035` | 3,160,000.00 USD | 3,160,000.00 USD | 2,710.00 USD | 9,400.00 USD | 15,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1036` | 1,730,000.00 USD | 1,730,000.00 USD | 4,780.00 USD | 7,340.00 USD | 12,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1037` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1038` | 1,700,000.00 USD | 1,700,000.00 USD | 4,190.00 USD | 9,130.00 USD | 12,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1039` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 5,170.00 USD | 139.84 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1040` | 1,680,000.00 USD | 1,680,000.00 USD | 2,980.00 USD | 4,600.00 USD | 12,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1041` | 3,110,000.00 USD | 3,110,000.00 USD | 5,940.00 USD | 2,910.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1042` | 1,660,000.00 USD | 1,660,000.00 USD | 23,250.00 USD | 5,430.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1043` | 3,090,000.00 USD | 3,090,000.00 USD | 15,960.00 USD | 5,980.00 USD | 20,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1044` | 1,610,000.00 USD | 1,610,000.00 USD | 917.34 USD | 6,870.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1045` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 3,830.00 USD | 15,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1046` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 1,080.00 USD | 8,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1047` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 1,720.00 USD | 22,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1048` | 1,600,000.00 USD | 1,600,000.00 USD | 8,130.00 USD | 3,110.00 USD | 20,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1049` | 3,010,000.00 USD | 3,010,000.00 USD | 34,790.00 USD | 4,810.00 USD | 35,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1050` | 1,560,000.00 USD | 1,560,000.00 USD | 19,000.00 USD | 2,470.00 USD | 10,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1051` | 2,930,000.00 USD | 2,930,000.00 USD | 17,290.00 USD | 11,500.00 USD | 48,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1052` | 1,530,000.00 USD | 1,530,000.00 USD | 29,880.00 USD | 11,260.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1053` | 2,850,000.00 USD | 2,850,000.00 USD | 53,590.00 USD | 29,800.00 USD | 95,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1054` | 1,460,000.00 USD | 1,460,000.00 USD | 41,310.00 USD | 13,810.00 USD | 37,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1055` | 2,670,000.00 USD | 2,670,000.00 USD | 50,090.00 USD | 27,290.00 USD | 126,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1056` | 1,360,000.00 USD | 1,360,000.00 USD | 22,250.00 USD | 22,210.00 USD | 39,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1057` | 2,470,000.00 USD | 2,470,000.00 USD | 50,380.00 USD | 45,760.00 USD | 74,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1058` | 1,280,000.00 USD | 1,280,000.00 USD | 9,530.00 USD | 28,610.00 USD | 43,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1059` | 2,300,000.00 USD | 2,300,000.00 USD | 92,510.00 USD | 49,670.00 USD | 114,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1060` | 1,200,000.00 USD | 1,200,000.00 USD | 18,260.00 USD | 6,740.00 USD | 42,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1061` | 2,040,000.00 USD | 2,040,000.00 USD | 38,260.00 USD | 26,050.00 USD | 76,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1062` | 1,130,000.00 USD | 1,130,000.00 USD | 22,490.00 USD | 15,960.00 USD | 42,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1063` | 1,900,000.00 USD | 1,900,000.00 USD | 84,260.00 USD | 38,330.00 USD | 148,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1064` | 1,050,000.00 USD | 1,050,000.00 USD | 49,230.00 USD | 16,060.00 USD | 44,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1065` | 1,630,000.00 USD | 1,630,000.00 USD | 91,170.00 USD | 17,310.00 USD | 93,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1066` | 938,760.00 USD | 938,760.00 USD | 14,460.00 USD | 12,550.00 USD | 17,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1067` | 1,430,000.00 USD | 1,430,000.00 USD | 97,290.00 USD | 36,720.00 USD | 67,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1068` | 894,650.00 USD | 894,650.00 USD | 16,490.00 USD | 9,500.00 USD | 27,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1069` | 1,230,000.00 USD | 1,230,000.00 USD | 76,900.00 USD | 31,620.00 USD | 72,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1070` | 840,860.00 USD | 840,860.00 USD | 22,800.00 USD | 6,210.00 USD | 43,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1071` | 1,050,000.00 USD | 1,050,000.00 USD | 119,440.00 USD | 27,240.00 USD | 42,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1072` | 768,550.00 USD | 768,550.00 USD | 38,000.00 USD | 3,780.00 USD | 17,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1073` | 858,650.00 USD | 858,650.00 USD | 58,480.00 USD | 17,700.00 USD | 58.62 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1074` | 709,700.00 USD | 709,700.00 USD | 21,410.00 USD | 12,510.00 USD | 20,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1075` | 782,410.00 USD | 782,410.00 USD | 20,750.00 USD | 3,500.00 USD | 31.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1076` | 655,280.00 USD | 655,280.00 USD | 26,690.00 USD | 15,990.00 USD | 13,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1077` | 758,120.00 USD | 758,120.00 USD | 0.00 USD | 0.00 USD | 8,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1078` | 599,430.00 USD | 599,430.00 USD | 12,550.00 USD | 18,160.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1079` | 749,470.00 USD | 749,470.00 USD | 140,450.00 USD | 23,980.00 USD | 5.46 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1080` | 531,510.00 USD | 531,510.00 USD | 17,560.00 USD | 7,980.00 USD | 39,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1081` | 585,030.00 USD | 585,030.00 USD | 205,390.00 USD | 11,660.00 USD | 28,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1082` | 466,130.00 USD | 466,130.00 USD | 18,610.00 USD | 10,790.00 USD | 35,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1083` | 339,120.00 USD | 339,120.00 USD | 94,800.00 USD | 2,110.00 USD | 42,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1084` | 401,700.00 USD | 401,700.00 USD | 24,240.00 USD | 10,630.00 USD | 45,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1085` | 199,810.00 USD | 199,810.00 USD | 15,920.00 USD | 4,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1086` | 321,050.00 USD | 321,050.00 USD | 27,840.00 USD | 9,510.00 USD | 72,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1087` | 179,690.00 USD | 179,690.00 USD | 55,430.00 USD | 6,210.00 USD | 60,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1088` | 210,760.00 USD | 210,760.00 USD | 44,230.00 USD | 8,890.00 USD | 28,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1089` | 57,980.00 USD | 57,980.00 USD | 5,290.00 USD | 14,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1090` | 129,020.00 USD | 129,020.00 USD | 36,710.00 USD | 11,900.00 USD | 26,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1091` | 38,120.00 USD | 38,120.00 USD | 16,310.00 USD | 3,800.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1092` | 53,910.00 USD | 53,910.00 USD | 10,290.00 USD | 4,610.00 USD | 5,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1093` | 9,010.00 USD | 9,010.00 USD | 0.00 USD | 0.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1094` | 33,300.00 USD | 33,300.00 USD | 13,100.00 USD | 3,890.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1095` | 225.65 USD | 225.65 USD | 0.00 USD | 0.00 USD | 177.01 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1097` | 48.64 USD | 48.64 USD | 0.00 USD | 0.00 USD | 48.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 17,490.00 USD | 17,490.00 USD | 17,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1104` | 29,800.00 USD | 29,800.00 USD | 23,720.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1105` | 37,230.00 USD | 37,230.00 USD | 0.00 USD | 10,030.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1106` | 62,630.00 USD | 62,630.00 USD | 0.00 USD | 12,720.00 USD | 20,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1107` | 49,740.00 USD | 49,740.00 USD | 0.00 USD | 12,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1108` | 78,260.00 USD | 78,260.00 USD | 0.00 USD | 0.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 62,170.00 USD | 62,170.00 USD | 0.00 USD | 12,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1114` | 128,600.00 USD | 128,600.00 USD | 15,810.00 USD | 3,630.00 USD | 30,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1116` | 145,450.00 USD | 145,450.00 USD | 4,760.00 USD | 12,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1117` | 101,440.00 USD | 101,440.00 USD | 0.00 USD | 22,780.00 USD | 16,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1118` | 231,240.00 USD | 231,240.00 USD | 26,390.00 USD | 17,620.00 USD | 41,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1119` | 144,540.00 USD | 144,540.00 USD | 25,250.00 USD | 7,050.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1120` | 255,740.00 USD | 255,740.00 USD | 15,610.00 USD | 6,590.00 USD | 2,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 165,720.00 USD | 165,720.00 USD | 0.00 USD | 0.00 USD | 21,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1122` | 290,920.00 USD | 290,920.00 USD | 21,760.00 USD | 3,070.00 USD | 10,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1123` | 228,230.00 USD | 228,230.00 USD | 12,360.00 USD | 23,980.00 USD | 26,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1124` | 316,590.00 USD | 316,590.00 USD | 17,870.00 USD | 1,780.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1125` | 257,060.00 USD | 257,060.00 USD | 0.00 USD | 0.00 USD | 28,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1126` | 324,900.00 USD | 324,900.00 USD | 0.00 USD | 8,280.00 USD | 26.51 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1128` | 333,300.00 USD | 333,300.00 USD | 5,450.00 USD | 0.00 USD | 2,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1129` | 257,150.00 USD | 257,150.00 USD | 0.00 USD | 0.00 USD | 87.32 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1130` | 347,890.00 USD | 347,890.00 USD | 7,970.00 USD | 1,490.00 USD | 5,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1131` | 284,710.00 USD | 284,710.00 USD | 12,540.00 USD | 0.00 USD | 15,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1132` | 397,420.00 USD | 397,420.00 USD | 16,120.00 USD | 17,300.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 290,160.00 USD | 290,160.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1134` | 428,270.00 USD | 428,270.00 USD | 4,040.00 USD | 12,980.00 USD | 13,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1135` | 304,740.00 USD | 304,740.00 USD | 0.00 USD | 5,520.00 USD | 9,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1136` | 428,310.00 USD | 428,310.00 USD | 0.00 USD | 0.00 USD | 40.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1137` | 305,000.00 USD | 305,000.00 USD | 0.00 USD | 0.00 USD | 258.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1138` | 443,430.00 USD | 443,430.00 USD | 0.00 USD | 856.93 USD | 14,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1140` | 457,280.00 USD | 457,280.00 USD | 7,800.00 USD | 0.00 USD | 6,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1141` | 322,970.00 USD | 322,970.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1142` | 509,280.00 USD | 509,280.00 USD | 23,850.00 USD | 16,610.00 USD | 11,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1143` | 401,580.00 USD | 401,580.00 USD | 0.00 USD | 0.00 USD | 78,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1144` | 572,760.00 USD | 572,760.00 USD | 9,940.00 USD | 21,970.00 USD | 31,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 562,010.00 USD | 562,010.00 USD | 16,540.00 USD | 2,730.00 USD | 141,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1146` | 617,490.00 USD | 617,490.00 USD | 5,090.00 USD | 9,590.00 USD | 30,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1147` | 706,540.00 USD | 706,540.00 USD | 9,880.00 USD | 0.00 USD | 134,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1148` | 675,070.00 USD | 675,070.00 USD | 29,590.00 USD | 3,280.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1149` | 789,800.00 USD | 789,800.00 USD | 10,560.00 USD | 0.00 USD | 72,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1150` | 725,670.00 USD | 725,670.00 USD | 18,410.00 USD | 13,020.00 USD | 19,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 1,010,000.00 USD | 1,010,000.00 USD | 92,570.00 USD | 4,210.00 USD | 128,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1152` | 846,270.00 USD | 846,270.00 USD | 34,520.00 USD | 17,470.00 USD | 68,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1153` | 1,320,000.00 USD | 1,320,000.00 USD | 153,720.00 USD | 8,400.00 USD | 139,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1154` | 956,760.00 USD | 956,760.00 USD | 26,700.00 USD | 29,020.00 USD | 54,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1155` | 1,610,000.00 USD | 1,610,000.00 USD | 149,360.00 USD | 40,110.00 USD | 105,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1156` | 1,060,000.00 USD | 1,060,000.00 USD | 58,640.00 USD | 21,470.00 USD | 24,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 1,800,000.00 USD | 1,800,000.00 USD | 133,960.00 USD | 3,760.00 USD | 48,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1158` | 1,140,000.00 USD | 1,140,000.00 USD | 26,730.00 USD | 9,500.00 USD | 41,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1159` | 1,950,000.00 USD | 1,950,000.00 USD | 81,080.00 USD | 12,710.00 USD | 53,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1160` | 1,210,000.00 USD | 1,210,000.00 USD | 34,710.00 USD | 6,890.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1161` | 2,230,000.00 USD | 2,230,000.00 USD | 146,810.00 USD | 37,250.00 USD | 99,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1162` | 1,260,000.00 USD | 1,260,000.00 USD | 15,950.00 USD | 13,530.00 USD | 21,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 2,380,000.00 USD | 2,380,000.00 USD | 66,560.00 USD | 11,460.00 USD | 68,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1164` | 1,310,000.00 USD | 1,310,000.00 USD | 20,480.00 USD | 13,180.00 USD | 18,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1165` | 2,510,000.00 USD | 2,510,000.00 USD | 68,620.00 USD | 35,720.00 USD | 27,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1166` | 1,330,000.00 USD | 1,330,000.00 USD | 13,420.00 USD | 10,720.00 USD | 40.24 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1167` | 2,650,000.00 USD | 2,650,000.00 USD | 79,610.00 USD | 21,620.00 USD | 41,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1168` | 1,370,000.00 USD | 1,370,000.00 USD | 9,880.00 USD | 12,540.00 USD | 8,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 2,820,000.00 USD | 2,820,000.00 USD | 65,340.00 USD | 14,840.00 USD | 86,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1170` | 1,390,000.00 USD | 1,390,000.00 USD | 16,450.00 USD | 4,080.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1171` | 2,920,000.00 USD | 2,920,000.00 USD | 57,350.00 USD | 11,370.00 USD | 35,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1172` | 1,410,000.00 USD | 1,410,000.00 USD | 10,950.00 USD | 8,910.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1173` | 3,010,000.00 USD | 3,010,000.00 USD | 40,860.00 USD | 9,190.00 USD | 36,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1174` | 1,450,000.00 USD | 1,450,000.00 USD | 10,300.00 USD | 6,360.00 USD | 19,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 3,120,000.00 USD | 3,120,000.00 USD | 38,840.00 USD | 12,300.00 USD | 59,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1176` | 1,490,000.00 USD | 1,490,000.00 USD | 6,120.00 USD | 16,060.00 USD | 20,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1177` | 3,220,000.00 USD | 3,220,000.00 USD | 33,330.00 USD | 20,350.00 USD | 44,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1178` | 1,530,000.00 USD | 1,530,000.00 USD | 27,500.00 USD | 7,760.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1179` | 3,320,000.00 USD | 3,320,000.00 USD | 66,670.00 USD | 10,940.00 USD | 23,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1180` | 1,580,000.00 USD | 1,580,000.00 USD | 15,510.00 USD | 4,770.00 USD | 24,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 3,370,000.00 USD | 3,370,000.00 USD | 22,290.00 USD | 15,780.00 USD | 17,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1182` | 1,610,000.00 USD | 1,610,000.00 USD | 15,060.00 USD | 3,740.00 USD | 13,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1183` | 3,420,000.00 USD | 3,420,000.00 USD | 4,040.00 USD | 1,800.00 USD | 39,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1184` | 1,630,000.00 USD | 1,630,000.00 USD | 7,750.00 USD | 3,320.00 USD | 10,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1185` | 3,450,000.00 USD | 3,450,000.00 USD | 3,880.00 USD | 5,130.00 USD | 22,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1186` | 1,660,000.00 USD | 1,660,000.00 USD | 10,390.00 USD | 8,770.00 USD | 11,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 3,500,000.00 USD | 3,500,000.00 USD | 5,620.00 USD | 15,370.00 USD | 31,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1188` | 1,680,000.00 USD | 1,680,000.00 USD | 4,660.00 USD | 7,610.00 USD | 4,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1189` | 3,550,000.00 USD | 3,550,000.00 USD | 27,240.00 USD | 15,060.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1190` | 1,690,000.00 USD | 1,690,000.00 USD | 5,250.00 USD | 5,740.00 USD | 2,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1191` | 3,690,000.00 USD | 3,690,000.00 USD | 22,650.00 USD | 15,330.00 USD | 109,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1192` | 1,710,000.00 USD | 1,710,000.00 USD | 7,250.00 USD | 1,990.00 USD | 7,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 3,730,000.00 USD | 3,730,000.00 USD | 21,260.00 USD | 0.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1194` | 1,720,000.00 USD | 1,720,000.00 USD | 6,310.00 USD | 1,390.00 USD | 2,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1195` | 3,770,000.00 USD | 3,770,000.00 USD | 11,190.00 USD | 1,780.00 USD | 29,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1196` | 1,730,000.00 USD | 1,730,000.00 USD | 3,240.00 USD | 2,860.00 USD | 100.88 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1197` | 3,800,000.00 USD | 3,800,000.00 USD | 6,780.00 USD | 10,800.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1198` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 3,660.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 3,870,000.00 USD | 3,870,000.00 USD | 9,100.00 USD | 0.00 USD | 64,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1200` | 1,740,000.00 USD | 1,740,000.00 USD | 1,840.00 USD | 1,050.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1201` | 4,030,000.00 USD | 4,030,000.00 USD | 114,140.00 USD | 16,380.00 USD | 28,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1202` | 1,760,000.00 USD | 1,760,000.00 USD | 10,280.00 USD | 460.32 USD | 4,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1203` | 4,140,000.00 USD | 4,140,000.00 USD | 70,770.00 USD | 29,250.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1204` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 413.94 USD | 1,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 4,400,000.00 USD | 4,400,000.00 USD | 86,480.00 USD | 48,720.00 USD | 128,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1206` | 1,770,000.00 USD | 1,770,000.00 USD | 5,370.00 USD | 2,190.00 USD | 3,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1207` | 4,490,000.00 USD | 4,490,000.00 USD | 12,460.00 USD | 19,400.00 USD | 53,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1208` | 1,780,000.00 USD | 1,780,000.00 USD | 4,240.00 USD | 1,920.00 USD | 2,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1209` | 4,690,000.00 USD | 4,690,000.00 USD | 85,160.00 USD | 19,340.00 USD | 94,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1210` | 1,790,000.00 USD | 1,790,000.00 USD | 3,980.00 USD | 3,340.00 USD | 2,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 4,760,000.00 USD | 4,760,000.00 USD | 27,400.00 USD | 16,260.00 USD | 29,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1212` | 1,800,000.00 USD | 1,800,000.00 USD | 1,470.00 USD | 1,190.00 USD | 7,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1213` | 4,830,000.00 USD | 4,830,000.00 USD | 23,920.00 USD | 21,730.00 USD | 24,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1214` | 1,810,000.00 USD | 1,810,000.00 USD | 3,200.00 USD | 820.70 USD | 7,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1215` | 4,900,000.00 USD | 4,900,000.00 USD | 5,900.00 USD | 6,620.00 USD | 59,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1216` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 4,960,000.00 USD | 4,960,000.00 USD | 18,490.00 USD | 23,600.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1218` | 1,820,000.00 USD | 1,820,000.00 USD | 2,640.00 USD | 624.33 USD | 8,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1219` | 5,030,000.00 USD | 5,030,000.00 USD | 26,700.00 USD | 5,500.00 USD | 38,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1220` | 1,830,000.00 USD | 1,830,000.00 USD | 2,690.00 USD | 1,690.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1221` | 5,110,000.00 USD | 5,110,000.00 USD | 47,890.00 USD | 21,770.00 USD | 18,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1222` | 1,850,000.00 USD | 1,850,000.00 USD | 2,760.00 USD | 3,370.00 USD | 6,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 5,300,000.00 USD | 5,300,000.00 USD | 103,180.00 USD | 36,290.00 USD | 48,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1224` | 1,850,000.00 USD | 1,850,000.00 USD | 2,660.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1225` | 5,370,000.00 USD | 5,370,000.00 USD | 43,040.00 USD | 19,970.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 16,900.00 USD | 16,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1227` | 5,520,000.00 USD | 5,520,000.00 USD | 65,240.00 USD | 30,390.00 USD | 55,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1228` | 1,850,000.00 USD | 1,850,000.00 USD | 1,970.00 USD | 0.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 5,660,000.00 USD | 5,660,000.00 USD | 63,350.00 USD | 30,490.00 USD | 40,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1230` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 403.62 USD | 789.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1231` | 5,730,000.00 USD | 5,730,000.00 USD | 21,280.00 USD | 29,380.00 USD | 27,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1232` | 1,860,000.00 USD | 1,860,000.00 USD | 1,250.00 USD | 1,630.00 USD | 19.93 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1233` | 5,840,000.00 USD | 5,840,000.00 USD | 57,130.00 USD | 13,020.00 USD | 40,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1234` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 2,120.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1235` | 5,870,000.00 USD | 5,870,000.00 USD | 10,950.00 USD | 6,400.00 USD | 8,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1236` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 800.79 USD | 911.21 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1237` | 5,890,000.00 USD | 5,890,000.00 USD | 4,080.00 USD | 7,220.00 USD | 2,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1238` | 1,870,000.00 USD | 1,870,000.00 USD | 3,120.00 USD | 0.00 USD | 587.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1239` | 5,900,000.00 USD | 5,900,000.00 USD | 8,780.00 USD | 1,270.00 USD | 232.47 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1240` | 1,870,000.00 USD | 1,870,000.00 USD | 1,790.00 USD | 1,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1241` | 5,910,000.00 USD | 5,910,000.00 USD | 6,830.00 USD | 9,690.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1243` | 5,940,000.00 USD | 5,940,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1245` | 5,990,000.00 USD | 5,990,000.00 USD | 26,080.00 USD | 11,090.00 USD | 13,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1247` | 6,040,000.00 USD | 6,040,000.00 USD | 24,470.00 USD | 19,030.00 USD | 9,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1249` | 6,060,000.00 USD | 6,060,000.00 USD | 13,440.00 USD | 5,480.00 USD | 5,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1251` | 6,090,000.00 USD | 6,090,000.00 USD | 7,660.00 USD | 5,070.00 USD | 11,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1253` | 6,110,000.00 USD | 6,110,000.00 USD | 11,420.00 USD | 2,100.00 USD | 14,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1255` | 6,130,000.00 USD | 6,130,000.00 USD | 2,250.00 USD | 13,990.00 USD | 25.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1257` | 6,150,000.00 USD | 6,150,000.00 USD | 15,610.00 USD | 5,200.00 USD | 71.45 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1259` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 224.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1261` | 6,160,000.00 USD | 6,160,000.00 USD | 4,270.00 USD | 0.00 USD | 3,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1263` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 0.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1265` | 6,170,000.00 USD | 6,170,000.00 USD | 2,710.00 USD | 0.00 USD | 3,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1267` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 0.00 USD | 2,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1269` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 0.00 USD | 16.21 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1355` | 1,330.00 USD | 18,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1525` | 15,250.00 USD | 33,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1555` | 6,210.00 USD | 39,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1565` | 550.61 USD | 40,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1615` | 20,770.00 USD | 61,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1695` | 169.25 USD | 61,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1865` | 167.85 USD | 61,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1945` | 940.15 USD | 62,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0405` | 243,180.00 USD | 0.00 USD | 183.72 USD | `-63.19%` | `4,536.30` |
| `Live` | `Long` | `0.0445` | 242,990.00 USD | 0.00 USD | 267.00 USD | `-59.56%` | `6,000.00` |
| `Live` | `Long` | `0.0505` | 242,730.00 USD | 0.00 USD | 3,520.00 USD | `-54.10%` | `69,790.10` |
| `Live` | `Long` | `0.0545` | 239,200.00 USD | 0.00 USD | 3,460.00 USD | `-50.47%` | `63,403.00` |
| `Live` | `Long` | `0.0555` | 235,750.00 USD | 0.00 USD | 282.99 USD | `-49.56%` | `5,098.90` |
| `Live` | `Long` | `0.0575` | 235,470.00 USD | 0.00 USD | 829.69 USD | `-47.74%` | `14,429.40` |
| `Live` | `Long` | `0.0615` | 234,640.00 USD | 0.00 USD | 1,100.00 USD | `-44.11%` | `17,943.80` |
| `Live` | `Long` | `0.0645` | 233,530.00 USD | 0.00 USD | 353.81 USD | `-41.38%` | `5,485.40` |
| `Live` | `Long` | `0.0675` | 233,180.00 USD | 0.00 USD | 1,040.00 USD | `-38.65%` | `15,345.00` |
| `Live` | `Long` | `0.0685` | 232,140.00 USD | 0.00 USD | 1,920.00 USD | `-37.74%` | `28,000.00` |
| `Live` | `Long` | `0.0725` | 230,220.00 USD | 0.00 USD | 25,370.00 USD | `-34.11%` | `349,988.60` |
| `Live` | `Long` | `0.0745` | 204,850.00 USD | 0.00 USD | 48,850.00 USD | `-32.29%` | `655,702.20` |
| `Live` | `Long` | `0.0755` | 156,000.00 USD | 0.00 USD | 1,020.00 USD | `-31.38%` | `13,481.90` |
| `Live` | `Long` | `0.0765` | 154,980.00 USD | 0.00 USD | 1,170.00 USD | `-30.47%` | `15,263.30` |
| `Live` | `Long` | `0.0775` | 153,810.00 USD | 0.00 USD | 995.43 USD | `-29.56%` | `12,844.30` |
| `Live` | `Long` | `0.0795` | 152,820.00 USD | 0.00 USD | 1,320.00 USD | `-27.75%` | `16,641.80` |
| `Live` | `Long` | `0.0805` | 151,500.00 USD | 0.00 USD | 1,110.00 USD | `-26.84%` | `13,753.40` |
| `Live` | `Long` | `0.0815` | 150,390.00 USD | 0.00 USD | 1,560.00 USD | `-25.93%` | `19,181.40` |
| `Live` | `Long` | `0.0885` | 148,830.00 USD | 0.00 USD | 2,400.00 USD | `-19.57%` | `27,146.60` |
| `Live` | `Long` | `0.0895` | 146,420.00 USD | 0.00 USD | 3,120.00 USD | `-18.66%` | `34,873.20` |
| `Live` | `Long` | `0.0905` | 143,300.00 USD | 0.00 USD | 443.16 USD | `-17.75%` | `4,896.80` |
| `Live` | `Long` | `0.0925` | 142,860.00 USD | 0.00 USD | 16,670.00 USD | `-15.93%` | `180,203.00` |
| `Live` | `Long` | `0.0945` | 126,190.00 USD | 0.00 USD | 69,120.00 USD | `-14.11%` | `731,405.60` |
| `Live` | `Long` | `0.0955` | 57,070.00 USD | 0.00 USD | 5,610.00 USD | `-13.21%` | `58,700.70` |
| `Live` | `Long` | `0.0965` | 51,470.00 USD | 0.00 USD | 419.87 USD | `-12.30%` | `4,351.00` |
| `Live` | `Long` | `0.0975` | 51,050.00 USD | 0.00 USD | 12,670.00 USD | `-11.39%` | `129,987.90` |
| `Live` | `Long` | `0.0985` | 38,370.00 USD | 0.00 USD | 19,960.00 USD | `-10.48%` | `202,627.30` |
| `Live` | `Long` | `0.1005` | 18,410.00 USD | 0.00 USD | 427.25 USD | `-8.66%` | `4,251.20` |
| `Live` | `Long` | `0.1015` | 17,990.00 USD | 0.00 USD | 622.37 USD | `-7.75%` | `6,131.70` |
| `Live` | `Long` | `0.1025` | 17,360.00 USD | 0.00 USD | 17,360.00 USD | `-6.84%` | `169,408.50` |
| `Live` | `Short` | `0.1225` | 16,900.00 USD | 16,900.00 USD | 0.00 USD | `+11.33%` | `137,980.90` |
| `Live` | `Short` | `0.1355` | 18,240.00 USD | 1,330.00 USD | 0.00 USD | `+23.15%` | `9,843.80` |
| `Live` | `Short` | `0.1525` | 33,490.00 USD | 15,250.00 USD | 0.00 USD | `+38.60%` | `100,000.40` |
| `Live` | `Short` | `0.1555` | 39,700.00 USD | 6,210.00 USD | 0.00 USD | `+41.33%` | `39,929.50` |
| `Live` | `Short` | `0.1565` | 40,250.00 USD | 550.61 USD | 0.00 USD | `+42.23%` | `3,518.30` |
| `Live` | `Short` | `0.1615` | 61,020.00 USD | 20,770.00 USD | 0.00 USD | `+46.78%` | `128,602.50` |
| `Live` | `Short` | `0.1695` | 61,180.00 USD | 169.25 USD | 0.00 USD | `+54.05%` | `998.50` |
| `Live` | `Short` | `0.1865` | 61,350.00 USD | 167.85 USD | 0.00 USD | `+69.50%` | `900.00` |
| `Live` | `Short` | `0.1945` | 62,290.00 USD | 940.15 USD | 0.00 USD | `+76.77%` | `4,833.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0635` | 177,200.00 USD | 0.00 USD | 1,140.00 USD | `-42.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 176,060.00 USD | 0.00 USD | 773.46 USD | `-35.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 175,290.00 USD | 0.00 USD | 592.27 USD | `-35.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 174,700.00 USD | 0.00 USD | 755.00 USD | `-31.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0805` | 173,940.00 USD | 0.00 USD | 411.06 USD | `-26.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0815` | 173,530.00 USD | 0.00 USD | 183.49 USD | `-25.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0835` | 173,350.00 USD | 0.00 USD | 456.70 USD | `-24.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 172,890.00 USD | 0.00 USD | 631.58 USD | `-22.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 172,260.00 USD | 0.00 USD | 653.74 USD | `-19.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0915` | 171,610.00 USD | 0.00 USD | 1,460.00 USD | `-16.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 170,140.00 USD | 0.00 USD | 485.13 USD | `-14.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0975` | 169,660.00 USD | 0.00 USD | 720.22 USD | `-11.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0985` | 168,940.00 USD | 0.00 USD | 931.75 USD | `-10.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0995` | 168,010.00 USD | 0.00 USD | 801.64 USD | `-9.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 167,200.00 USD | 0.00 USD | 2,180.00 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1015` | 165,030.00 USD | 0.00 USD | 903.42 USD | `-7.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 164,120.00 USD | 0.00 USD | 780.70 USD | `-6.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1035` | 163,340.00 USD | 0.00 USD | 4,650.00 USD | `-5.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1045` | 158,690.00 USD | 0.00 USD | 18,950.00 USD | `-5.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1055` | 139,750.00 USD | 0.00 USD | 7,770.00 USD | `-4.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1065` | 131,970.00 USD | 0.00 USD | 109,280.00 USD | `-3.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 22,690.00 USD | 0.00 USD | 21,900.00 USD | `-2.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 789.40 USD | 0.00 USD | 150.04 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1095` | 639.36 USD | 0.00 USD | 639.36 USD | `-0.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 162.59 USD | 162.59 USD | 0.00 USD | `+0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 1,000.00 USD | 839.64 USD | 0.00 USD | `+1.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1125` | 1,790.00 USD | 786.65 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1135` | 1,910.00 USD | 116.27 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1145` | 2,040.00 USD | 134.61 USD | 0.00 USD | `+4.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,530.00 USD | 489.97 USD | 0.00 USD | `+4.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1165` | 2,710.00 USD | 180.81 USD | 0.00 USD | `+5.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1175` | 30,240.00 USD | 27,530.00 USD | 0.00 USD | `+6.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1185` | 31,290.00 USD | 1,050.00 USD | 0.00 USD | `+7.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1195` | 45,930.00 USD | 14,640.00 USD | 0.00 USD | `+8.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1205` | 46,330.00 USD | 398.42 USD | 0.00 USD | `+9.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1225` | 47,310.00 USD | 980.00 USD | 0.00 USD | `+11.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1235` | 60,290.00 USD | 12,980.00 USD | 0.00 USD | `+12.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1255` | 64,660.00 USD | 4,380.00 USD | 0.00 USD | `+14.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1265` | 75,120.00 USD | 10,460.00 USD | 0.00 USD | `+14.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1275` | 75,620.00 USD | 492.06 USD | 0.00 USD | `+15.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1305` | 76,060.00 USD | 444.24 USD | 0.00 USD | `+18.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1315` | 107,620.00 USD | 31,560.00 USD | 0.00 USD | `+19.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1335` | 108,940.00 USD | 1,310.00 USD | 0.00 USD | `+21.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1345` | 113,090.00 USD | 4,150.00 USD | 0.00 USD | `+22.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1365` | 123,780.00 USD | 10,690.00 USD | 0.00 USD | `+24.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1405` | 136,890.00 USD | 13,110.00 USD | 0.00 USD | `+27.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1425` | 136,990.00 USD | 102.22 USD | 0.00 USD | `+29.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1435` | 144,160.00 USD | 7,180.00 USD | 0.00 USD | `+30.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1485` | 146,810.00 USD | 2,650.00 USD | 0.00 USD | `+34.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1495` | 147,600.00 USD | 792.53 USD | 0.00 USD | `+35.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1525` | 151,370.00 USD | 3,770.00 USD | 0.00 USD | `+38.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 151,550.00 USD | 184.49 USD | 0.00 USD | `+41.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 158,270.00 USD | 6,720.00 USD | 0.00 USD | `+42.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 158,490.00 USD | 219.81 USD | 0.00 USD | `+43.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 158,770.00 USD | 277.62 USD | 0.00 USD | `+48.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 160,570.00 USD | 1,800.00 USD | 0.00 USD | `+54.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 160,780.00 USD | 216.55 USD | 0.00 USD | `+58.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 160,900.00 USD | 117.26 USD | 0.00 USD | `+79.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 181,430.00 USD | 20,530.00 USD | 0.00 USD | `+82.22%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0975` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 0.00 USD | 2,560.00 USD | 7,150.00 USD |
| `7D` | `0.0977` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 5,800.00 USD |
| `7D` | `0.0979` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 0.00 USD | 1,530.00 USD | 5,680.00 USD |
| `7D` | `0.0981` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 5,910.00 USD |
| `7D` | `0.0983` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 7,990.00 USD | 1,230.00 USD | 8,900.00 USD |
| `1D` | `0.0984` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 8,920.00 USD | 1,070.00 USD | 9,450.00 USD |
| `7D` | `0.0985` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 7,110.00 USD | 0.00 USD | 6,320.00 USD |
| `1D` | `0.0986` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 5,370.00 USD | 2,610.00 USD | 4,580.00 USD |
| `7D` | `0.0987` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 5,390.00 USD | 9,190.00 USD | 37,270.00 USD |
| `1D` | `0.0988` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 4,240.00 USD | 1,920.00 USD | 2,170.00 USD |
| `7D` | `0.0989` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 12,260.00 USD | 4,520.00 USD | 27,190.00 USD |
| `1D` | `0.0990` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 3,980.00 USD | 3,340.00 USD | 2,450.00 USD |
| `7D` | `0.0991` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 14,350.00 USD | 10,350.00 USD | 13,610.00 USD |
| `1D` | `0.0992` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 1,470.00 USD | 1,190.00 USD | 7,820.00 USD |
| `7D` | `0.0993` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 23,920.00 USD | 10,140.00 USD | 24,170.00 USD |
| `1D` | `0.0994` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 3,200.00 USD | 820.70 USD | 7,510.00 USD |
| `7D` | `0.0995` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 13,090.00 USD | 6,160.00 USD | 25,280.00 USD |
| `1D` | `0.0996` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 2,640.00 USD | 624.33 USD | 10,110.00 USD |
| `7D` | `0.0997` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 21,100.00 USD | 5,500.00 USD | 32,940.00 USD |
| `1D` | `0.0998` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 2,690.00 USD | 1,690.00 USD | 6,280.00 USD |
| `7D` | `0.0999` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 14,230.00 USD | 6,540.00 USD | 18,730.00 USD |
| `1D` | `0.1000` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 2,760.00 USD | 3,370.00 USD | 6,570.00 USD |
| `7D` | `0.1001` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 29,230.00 USD | 3,010.00 USD | 10,920.00 USD |
| `1D` | `0.1002` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 2,660.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1003` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 8,010.00 USD | 7,060.00 USD | 5,290.00 USD |
| `1D` | `0.1004` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 1,970.00 USD | 0.00 USD | 1,120.00 USD |
| `7D` | `0.1005` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 25,070.00 USD | 11,000.00 USD | 18,330.00 USD |
| `1D` | `0.1006` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 0.00 USD | 403.62 USD | 803.25 USD |
| `7D` | `0.1007` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 10,260.00 USD | 2,280.00 USD | 14,030.00 USD |
| `1D` | `0.1008` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 1,250.00 USD | 1,630.00 USD | 26.69 USD |
| `7D` | `0.1009` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 15,320.00 USD | 3,070.00 USD | 6,730.00 USD |
| `1D` | `0.1010` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 0.00 USD | 2,120.00 USD | 2,500.00 USD |
| `7D` | `0.1011` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 4,430.00 USD | 4,720.00 USD | 9,160.00 USD |
| `1D` | `0.1012` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 0.00 USD | 800.79 USD | 997.22 USD |
| `7D` | `0.1013` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 12,870.00 USD | 4,030.00 USD | 3,070.00 USD |
| `1D` | `0.1014` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 4,900.00 USD | 1,830.00 USD | 608.26 USD |
| `7D` | `0.1015` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 6,830.00 USD | 965.35 USD | 2,410.00 USD |
| `1D` | `0.1016` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 2,200.00 USD | 2,540.00 USD | 5,620.00 USD |
| `7D` | `0.1017` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,690.00 USD |
| `1D` | `0.1018` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 827.81 USD | 4,170.00 USD | 7,380.00 USD |
| `7D` | `0.1019` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 9,260.00 USD | 5,790.00 USD | 13,190.00 USD |
| `1D` | `0.1020` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 6,440.00 USD | 2,630.00 USD | 2,020.00 USD |
| `7D` | `0.1021` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 7,900.00 USD | 3,270.00 USD | 7,180.00 USD |
| `1D` | `0.1022` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 5,070.00 USD | 2,120.00 USD | 7,230.00 USD |
| `7D` | `0.1023` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 4,030.00 USD | 4,990.00 USD | 14,300.00 USD |
| `1D` | `0.1024` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 2,300.00 USD | 947.50 USD | 4,680.00 USD |
| `7D` | `0.1025` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 1,550.00 USD | 0.00 USD | 5,480.00 USD |
| `1D` | `0.1026` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 2,780.00 USD | 2,210.00 USD | 2,520.00 USD |
| `7D` | `0.1027` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 2,250.00 USD | 2,580.00 USD | 466.12 USD |
| `1D` | `0.1028` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 0.00 USD | 936.16 USD | 88.60 USD |
| `7D` | `0.1029` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 7,420.00 USD | 3,000.00 USD | 735.27 USD |
| `1D` | `0.1030` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 8,870.00 USD | 3,480.00 USD | 10,390.00 USD |
| `7D` | `0.1031` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 13,690.00 USD | 5,070.00 USD | 10,730.00 USD |
| `1D` | `0.1032` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 11,310.00 USD | 2,260.00 USD | 5,420.00 USD |
| `7D` | `0.1033` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 3,880.00 USD | 2,640.00 USD | 15,170.00 USD |
| `1D` | `0.1034` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 7,190.00 USD | 5,040.00 USD | 11,050.00 USD |
| `7D` | `0.1035` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 2,710.00 USD | 9,400.00 USD | 15,950.00 USD |
| `1D` | `0.1036` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 4,780.00 USD | 7,340.00 USD | 12,360.00 USD |
| `7D` | `0.1037` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 19,500.00 USD |
| `1D` | `0.1038` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 4,190.00 USD | 9,130.00 USD | 12,700.00 USD |
| `7D` | `0.1039` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 0.00 USD | 5,170.00 USD | 139.84 USD |
| `1D` | `0.1040` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 2,980.00 USD | 4,600.00 USD | 12,770.00 USD |
| `7D` | `0.1041` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 5,940.00 USD | 2,910.00 USD | 10,670.00 USD |
| `1D` | `0.1042` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 23,250.00 USD | 5,430.00 USD | 12,600.00 USD |
| `7D` | `0.1043` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 15,960.00 USD | 5,980.00 USD | 20,650.00 USD |
| `1D` | `0.1044` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 917.34 USD | 6,870.00 USD | 1,320.00 USD |
| `7D` | `0.1045` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 0.00 USD | 3,830.00 USD | 15,150.00 USD |
| `1D` | `0.1046` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 0.00 USD | 1,080.00 USD | 8,670.00 USD |
| `7D` | `0.1047` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 0.00 USD | 1,720.00 USD | 22,830.00 USD |
| `1D` | `0.1048` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 8,130.00 USD | 3,110.00 USD | 20,120.00 USD |
| `7D` | `0.1049` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 34,790.00 USD | 4,810.00 USD | 35,960.00 USD |
| `1D` | `0.1050` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 19,000.00 USD | 2,470.00 USD | 10,720.00 USD |
| `7D` | `0.1051` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 17,290.00 USD | 11,500.00 USD | 48,310.00 USD |
| `1D` | `0.1052` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 29,880.00 USD | 11,260.00 USD | 33,450.00 USD |
| `7D` | `0.1053` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 53,590.00 USD | 29,800.00 USD | 95,690.00 USD |
| `1D` | `0.1054` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 41,310.00 USD | 13,810.00 USD | 37,970.00 USD |
| `7D` | `0.1055` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 50,090.00 USD | 27,290.00 USD | 126,320.00 USD |
| `1D` | `0.1056` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 22,250.00 USD | 22,210.00 USD | 39,790.00 USD |
| `7D` | `0.1057` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 50,380.00 USD | 45,760.00 USD | 74,510.00 USD |
| `1D` | `0.1058` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 9,530.00 USD | 28,610.00 USD | 43,990.00 USD |
| `7D` | `0.1059` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 92,510.00 USD | 49,670.00 USD | 114,080.00 USD |
| `1D` | `0.1060` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 18,260.00 USD | 6,740.00 USD | 42,420.00 USD |
| `7D` | `0.1061` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 38,260.00 USD | 26,050.00 USD | 76,270.00 USD |
| `1D` | `0.1062` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 22,490.00 USD | 15,960.00 USD | 42,660.00 USD |
| `7D` | `0.1063` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 84,260.00 USD | 38,330.00 USD | 148,860.00 USD |
| `1D` | `0.1064` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 49,230.00 USD | 16,060.00 USD | 44,950.00 USD |
| `7D` | `0.1065` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 91,170.00 USD | 17,310.00 USD | 93,300.00 USD |
| `1D` | `0.1066` | 938,760.00 USD | 0.00 USD | 938,760.00 USD | 14,460.00 USD | 12,550.00 USD | 17,100.00 USD |
| `7D` | `0.1067` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 97,290.00 USD | 36,720.00 USD | 67,820.00 USD |
| `1D` | `0.1068` | 894,650.00 USD | 0.00 USD | 894,650.00 USD | 16,490.00 USD | 9,500.00 USD | 27,800.00 USD |
| `7D` | `0.1069` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 76,900.00 USD | 31,620.00 USD | 72,050.00 USD |
| `1D` | `0.1070` | 840,860.00 USD | 0.00 USD | 840,860.00 USD | 22,800.00 USD | 6,210.00 USD | 43,290.00 USD |
| `7D` | `0.1071` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 119,440.00 USD | 27,240.00 USD | 42,500.00 USD |
| `1D` | `0.1072` | 768,550.00 USD | 0.00 USD | 768,550.00 USD | 38,000.00 USD | 3,780.00 USD | 17,070.00 USD |
| `7D` | `0.1073` | 858,650.00 USD | 0.00 USD | 858,650.00 USD | 58,480.00 USD | 17,700.00 USD | 58.62 USD |
| `1D` | `0.1074` | 709,700.00 USD | 0.00 USD | 709,700.00 USD | 21,410.00 USD | 12,510.00 USD | 20,500.00 USD |
| `7D` | `0.1075` | 782,410.00 USD | 0.00 USD | 782,410.00 USD | 20,750.00 USD | 3,500.00 USD | 31.64 USD |
| `1D` | `0.1076` | 655,280.00 USD | 0.00 USD | 655,280.00 USD | 26,690.00 USD | 15,990.00 USD | 13,170.00 USD |
| `7D` | `0.1077` | 758,120.00 USD | 0.00 USD | 758,120.00 USD | 0.00 USD | 0.00 USD | 8,640.00 USD |
| `1D` | `0.1078` | 599,430.00 USD | 0.00 USD | 599,430.00 USD | 12,550.00 USD | 18,160.00 USD | 37,210.00 USD |
| `7D` | `0.1079` | 749,470.00 USD | 0.00 USD | 749,470.00 USD | 140,450.00 USD | 23,980.00 USD | 5.46 USD |
| `1D` | `0.1080` | 531,510.00 USD | 0.00 USD | 531,510.00 USD | 17,560.00 USD | 7,980.00 USD | 39,830.00 USD |
| `7D` | `0.1081` | 585,030.00 USD | 0.00 USD | 585,030.00 USD | 205,390.00 USD | 11,660.00 USD | 28,860.00 USD |
| `1D` | `0.1082` | 466,130.00 USD | 0.00 USD | 466,130.00 USD | 18,610.00 USD | 10,790.00 USD | 35,030.00 USD |
| `7D` | `0.1083` | 339,120.00 USD | 0.00 USD | 339,120.00 USD | 94,800.00 USD | 2,110.00 USD | 42,410.00 USD |
| `1D` | `0.1084` | 401,700.00 USD | 0.00 USD | 401,700.00 USD | 24,240.00 USD | 10,630.00 USD | 45,770.00 USD |
| `7D` | `0.1085` | 199,810.00 USD | 0.00 USD | 199,810.00 USD | 15,920.00 USD | 4,200.00 USD | 0.00 USD |
| `1D` | `0.1086` | 321,050.00 USD | 0.00 USD | 321,050.00 USD | 27,840.00 USD | 9,510.00 USD | 72,930.00 USD |
| `7D` | `0.1087` | 179,690.00 USD | 0.00 USD | 179,690.00 USD | 55,430.00 USD | 6,210.00 USD | 60,070.00 USD |
| `1D` | `0.1088` | 210,760.00 USD | 0.00 USD | 210,760.00 USD | 44,230.00 USD | 8,890.00 USD | 28,620.00 USD |
| `7D` | `0.1089` | 57,980.00 USD | 0.00 USD | 57,980.00 USD | 5,290.00 USD | 14,560.00 USD | 0.00 USD |
| `1D` | `0.1090` | 129,020.00 USD | 0.00 USD | 129,020.00 USD | 36,710.00 USD | 11,900.00 USD | 26,500.00 USD |
| `7D` | `0.1091` | 38,120.00 USD | 0.00 USD | 38,120.00 USD | 16,310.00 USD | 3,800.00 USD | 9,010.00 USD |
| `1D` | `0.1092` | 53,910.00 USD | 0.00 USD | 53,910.00 USD | 10,290.00 USD | 4,610.00 USD | 5,700.00 USD |
| `7D` | `0.1093` | 9,010.00 USD | 0.00 USD | 9,010.00 USD | 0.00 USD | 0.00 USD | 8,780.00 USD |
| `1D` | `0.1094` | 33,300.00 USD | 0.00 USD | 33,300.00 USD | 13,100.00 USD | 3,890.00 USD | 16,310.00 USD |
| `7D` | `0.1095` | 225.65 USD | 0.00 USD | 225.65 USD | 0.00 USD | 0.00 USD | 177.01 USD |
| `7D` | `0.1097` | 48.64 USD | 0.00 USD | 48.64 USD | 0.00 USD | 0.00 USD | 48.64 USD |
| `1D` | `0.1100` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1100` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1103` | 17,490.00 USD | 17,490.00 USD | 0.00 USD | 17,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1104` | 29,800.00 USD | 29,800.00 USD | 0.00 USD | 23,720.00 USD | 0.00 USD | 6,070.00 USD |
| `7D` | `0.1105` | 37,230.00 USD | 37,230.00 USD | 0.00 USD | 0.00 USD | 10,030.00 USD | 9,710.00 USD |
| `1D` | `0.1106` | 62,630.00 USD | 62,630.00 USD | 0.00 USD | 0.00 USD | 12,720.00 USD | 20,120.00 USD |
| `7D` | `0.1107` | 49,740.00 USD | 49,740.00 USD | 0.00 USD | 0.00 USD | 12,510.00 USD | 0.00 USD |
| `1D` | `0.1108` | 78,260.00 USD | 78,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,630.00 USD |
| `7D` | `0.1109` | 62,170.00 USD | 62,170.00 USD | 0.00 USD | 0.00 USD | 12,430.00 USD | 0.00 USD |
| `1D` | `0.1114` | 128,600.00 USD | 128,600.00 USD | 0.00 USD | 15,810.00 USD | 3,630.00 USD | 30,900.00 USD |
| `1D` | `0.1116` | 145,450.00 USD | 145,450.00 USD | 0.00 USD | 4,760.00 USD | 12,080.00 USD | 0.00 USD |
| `7D` | `0.1117` | 101,440.00 USD | 101,440.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | 16,490.00 USD |
| `1D` | `0.1118` | 231,240.00 USD | 231,240.00 USD | 0.00 USD | 26,390.00 USD | 17,620.00 USD | 41,780.00 USD |
| `7D` | `0.1119` | 144,540.00 USD | 144,540.00 USD | 0.00 USD | 25,250.00 USD | 7,050.00 USD | 10,800.00 USD |
| `1D` | `0.1120` | 255,740.00 USD | 255,740.00 USD | 0.00 USD | 15,610.00 USD | 6,590.00 USD | 2,280.00 USD |
| `7D` | `0.1121` | 165,720.00 USD | 165,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,180.00 USD |
| `1D` | `0.1122` | 290,920.00 USD | 290,920.00 USD | 0.00 USD | 21,760.00 USD | 3,070.00 USD | 10,350.00 USD |
| `7D` | `0.1123` | 228,230.00 USD | 228,230.00 USD | 0.00 USD | 12,360.00 USD | 23,980.00 USD | 26,180.00 USD |
| `1D` | `0.1124` | 316,590.00 USD | 316,590.00 USD | 0.00 USD | 17,870.00 USD | 1,780.00 USD | 6,020.00 USD |
| `7D` | `0.1125` | 257,060.00 USD | 257,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,830.00 USD |
| `1D` | `0.1126` | 324,900.00 USD | 324,900.00 USD | 0.00 USD | 0.00 USD | 8,280.00 USD | 26.51 USD |
| `1D` | `0.1128` | 333,300.00 USD | 333,300.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD | 2,950.00 USD |
| `7D` | `0.1129` | 257,150.00 USD | 257,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 87.32 USD |
| `1D` | `0.1130` | 347,890.00 USD | 347,890.00 USD | 0.00 USD | 7,970.00 USD | 1,490.00 USD | 5,140.00 USD |
| `7D` | `0.1131` | 284,710.00 USD | 284,710.00 USD | 0.00 USD | 12,540.00 USD | 0.00 USD | 15,020.00 USD |
| `1D` | `0.1132` | 397,420.00 USD | 397,420.00 USD | 0.00 USD | 16,120.00 USD | 17,300.00 USD | 16,110.00 USD |
| `7D` | `0.1133` | 290,160.00 USD | 290,160.00 USD | 0.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD |
| `1D` | `0.1134` | 428,270.00 USD | 428,270.00 USD | 0.00 USD | 4,040.00 USD | 12,980.00 USD | 13,830.00 USD |
| `7D` | `0.1135` | 304,740.00 USD | 304,740.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,060.00 USD |
| `1D` | `0.1136` | 428,310.00 USD | 428,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 40.44 USD |
| `7D` | `0.1137` | 305,000.00 USD | 305,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 258.18 USD |
| `1D` | `0.1138` | 443,430.00 USD | 443,430.00 USD | 0.00 USD | 0.00 USD | 856.93 USD | 14,260.00 USD |
| `1D` | `0.1140` | 457,280.00 USD | 457,280.00 USD | 0.00 USD | 7,800.00 USD | 0.00 USD | 6,050.00 USD |
| `7D` | `0.1141` | 322,970.00 USD | 322,970.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,600.00 USD |
| `1D` | `0.1142` | 509,280.00 USD | 509,280.00 USD | 0.00 USD | 23,850.00 USD | 16,610.00 USD | 11,540.00 USD |
| `7D` | `0.1143` | 401,580.00 USD | 401,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78,600.00 USD |
| `1D` | `0.1144` | 572,760.00 USD | 572,760.00 USD | 0.00 USD | 9,940.00 USD | 21,970.00 USD | 31,580.00 USD |
| `7D` | `0.1145` | 562,010.00 USD | 562,010.00 USD | 0.00 USD | 16,540.00 USD | 2,730.00 USD | 141,160.00 USD |
| `1D` | `0.1146` | 617,490.00 USD | 617,490.00 USD | 0.00 USD | 5,090.00 USD | 9,590.00 USD | 30,050.00 USD |
| `7D` | `0.1147` | 706,540.00 USD | 706,540.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 134,650.00 USD |
| `1D` | `0.1148` | 675,070.00 USD | 675,070.00 USD | 0.00 USD | 29,590.00 USD | 3,280.00 USD | 24,710.00 USD |
| `7D` | `0.1149` | 789,800.00 USD | 789,800.00 USD | 0.00 USD | 10,560.00 USD | 0.00 USD | 72,700.00 USD |
| `1D` | `0.1150` | 725,670.00 USD | 725,670.00 USD | 0.00 USD | 18,410.00 USD | 13,020.00 USD | 19,180.00 USD |
| `7D` | `0.1151` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 92,570.00 USD | 4,210.00 USD | 128,390.00 USD |
| `1D` | `0.1152` | 846,270.00 USD | 846,270.00 USD | 0.00 USD | 34,520.00 USD | 17,470.00 USD | 68,600.00 USD |
| `7D` | `0.1153` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 153,720.00 USD | 8,400.00 USD | 139,620.00 USD |
| `1D` | `0.1154` | 956,760.00 USD | 956,760.00 USD | 0.00 USD | 26,700.00 USD | 29,020.00 USD | 54,770.00 USD |
| `7D` | `0.1155` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 149,360.00 USD | 40,110.00 USD | 105,850.00 USD |
| `1D` | `0.1156` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 58,640.00 USD | 21,470.00 USD | 24,350.00 USD |
| `7D` | `0.1157` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 133,960.00 USD | 3,760.00 USD | 48,500.00 USD |
| `1D` | `0.1158` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 26,730.00 USD | 9,500.00 USD | 41,820.00 USD |
| `7D` | `0.1159` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 81,080.00 USD | 12,710.00 USD | 53,480.00 USD |
| `1D` | `0.1160` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 34,710.00 USD | 6,890.00 USD | 26,610.00 USD |
| `7D` | `0.1161` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 146,810.00 USD | 37,250.00 USD | 99,800.00 USD |
| `1D` | `0.1162` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 15,950.00 USD | 13,530.00 USD | 21,330.00 USD |
| `7D` | `0.1163` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 66,560.00 USD | 11,460.00 USD | 68,700.00 USD |
| `1D` | `0.1164` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 20,480.00 USD | 13,180.00 USD | 18,360.00 USD |
| `7D` | `0.1165` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 68,620.00 USD | 35,720.00 USD | 27,180.00 USD |
| `1D` | `0.1166` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 13,420.00 USD | 10,720.00 USD | 40.24 USD |
| `7D` | `0.1167` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 79,610.00 USD | 21,620.00 USD | 41,140.00 USD |
| `1D` | `0.1168` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 9,880.00 USD | 12,540.00 USD | 8,430.00 USD |
| `7D` | `0.1169` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 65,340.00 USD | 14,840.00 USD | 86,710.00 USD |
| `1D` | `0.1170` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 16,450.00 USD | 4,080.00 USD | 6,660.00 USD |
| `7D` | `0.1171` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 57,350.00 USD | 11,370.00 USD | 35,080.00 USD |
| `1D` | `0.1172` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 10,950.00 USD | 8,910.00 USD | 1,570.00 USD |
| `7D` | `0.1173` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 40,860.00 USD | 9,190.00 USD | 36,520.00 USD |
| `1D` | `0.1174` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 10,300.00 USD | 6,360.00 USD | 19,720.00 USD |
| `7D` | `0.1175` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 38,840.00 USD | 12,300.00 USD | 59,080.00 USD |
| `1D` | `0.1176` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 6,120.00 USD | 16,060.00 USD | 20,110.00 USD |
| `7D` | `0.1177` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 33,330.00 USD | 20,350.00 USD | 44,240.00 USD |
| `1D` | `0.1178` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 27,500.00 USD | 7,760.00 USD | 7,040.00 USD |
| `7D` | `0.1179` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 66,670.00 USD | 10,940.00 USD | 23,740.00 USD |
| `1D` | `0.1180` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 15,510.00 USD | 4,770.00 USD | 24,290.00 USD |
| `7D` | `0.1181` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 22,290.00 USD | 15,780.00 USD | 17,750.00 USD |
| `1D` | `0.1182` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 15,060.00 USD | 3,740.00 USD | 13,280.00 USD |
| `7D` | `0.1183` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 4,040.00 USD | 1,800.00 USD | 39,220.00 USD |
| `1D` | `0.1184` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 7,750.00 USD | 3,320.00 USD | 10,270.00 USD |
| `7D` | `0.1185` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 3,880.00 USD | 5,130.00 USD | 22,340.00 USD |
| `1D` | `0.1186` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 10,390.00 USD | 8,770.00 USD | 11,840.00 USD |
| `7D` | `0.1187` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 5,620.00 USD | 15,370.00 USD | 31,960.00 USD |
| `1D` | `0.1188` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 4,660.00 USD | 7,610.00 USD | 4,640.00 USD |
| `7D` | `0.1189` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 27,240.00 USD | 15,060.00 USD | 3,410.00 USD |
| `1D` | `0.1190` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 5,250.00 USD | 5,740.00 USD | 2,740.00 USD |
| `7D` | `0.1191` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 22,650.00 USD | 15,330.00 USD | 109,350.00 USD |
| `1D` | `0.1192` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 7,250.00 USD | 1,990.00 USD | 7,230.00 USD |
| `7D` | `0.1193` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 21,260.00 USD | 0.00 USD | 9,000.00 USD |
| `1D` | `0.1194` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 6,310.00 USD | 1,390.00 USD | 2,810.00 USD |
| `7D` | `0.1195` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 11,190.00 USD | 1,780.00 USD | 29,720.00 USD |
| `1D` | `0.1196` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 3,240.00 USD | 2,860.00 USD | 100.88 USD |
| `7D` | `0.1197` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 6,780.00 USD | 10,800.00 USD | 13,930.00 USD |
| `1D` | `0.1198` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 3,660.00 USD | 2,070.00 USD |
| `7D` | `0.1199` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 9,100.00 USD | 0.00 USD | 64,970.00 USD |
| `1D` | `0.1200` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 1,840.00 USD | 1,050.00 USD | 6,160.00 USD |
| `7D` | `0.1201` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 114,140.00 USD | 16,380.00 USD | 28,870.00 USD |
| `1D` | `0.1202` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 10,280.00 USD | 460.32 USD | 4,370.00 USD |
| `7D` | `0.1203` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 70,770.00 USD | 29,250.00 USD | 6,320.00 USD |
| `1D` | `0.1204` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 413.94 USD | 1,290.00 USD |
| `7D` | `0.1205` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 86,480.00 USD | 48,720.00 USD | 128,380.00 USD |
| `1D` | `0.1206` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 5,370.00 USD | 2,190.00 USD | 3,320.00 USD |
| `7D` | `0.1207` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 12,460.00 USD | 19,400.00 USD | 53,860.00 USD |
| `1D` | `0.1208` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 4,240.00 USD | 1,920.00 USD | 2,190.00 USD |
| `7D` | `0.1209` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 85,160.00 USD | 19,340.00 USD | 94,230.00 USD |
| `1D` | `0.1210` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 3,980.00 USD | 3,340.00 USD | 2,520.00 USD |
| `7D` | `0.1211` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 27,400.00 USD | 16,260.00 USD | 29,670.00 USD |
| `1D` | `0.1212` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 1,470.00 USD | 1,190.00 USD | 7,840.00 USD |
| `7D` | `0.1213` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 23,920.00 USD | 21,730.00 USD | 24,290.00 USD |
| `1D` | `0.1214` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 3,200.00 USD | 820.70 USD | 7,540.00 USD |
| `7D` | `0.1215` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 5,900.00 USD | 6,620.00 USD | 59,100.00 USD |
| `1D` | `0.1216` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,360.00 USD |
| `7D` | `0.1217` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 18,490.00 USD | 23,600.00 USD | 11,120.00 USD |
| `1D` | `0.1218` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 2,640.00 USD | 624.33 USD | 8,810.00 USD |
| `7D` | `0.1219` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 26,700.00 USD | 5,500.00 USD | 38,060.00 USD |
| `1D` | `0.1220` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 2,690.00 USD | 1,690.00 USD | 6,280.00 USD |
| `7D` | `0.1221` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 47,890.00 USD | 21,770.00 USD | 18,850.00 USD |
| `1D` | `0.1222` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 2,760.00 USD | 3,370.00 USD | 6,580.00 USD |
| `7D` | `0.1223` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 103,180.00 USD | 36,290.00 USD | 48,470.00 USD |
| `1D` | `0.1224` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 2,660.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1225` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 43,040.00 USD | 19,970.00 USD | 5,260.00 USD |
| `7D` | `0.1227` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 65,240.00 USD | 30,390.00 USD | 55,600.00 USD |
| `1D` | `0.1228` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 1,970.00 USD | 0.00 USD | 1,080.00 USD |
| `7D` | `0.1229` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 63,350.00 USD | 30,490.00 USD | 40,630.00 USD |
| `1D` | `0.1230` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 403.62 USD | 789.22 USD |
| `7D` | `0.1231` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 21,280.00 USD | 29,380.00 USD | 27,570.00 USD |
| `1D` | `0.1232` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 1,250.00 USD | 1,630.00 USD | 19.93 USD |
| `7D` | `0.1233` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 57,130.00 USD | 13,020.00 USD | 40,160.00 USD |
| `1D` | `0.1234` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 2,120.00 USD | 2,450.00 USD |
| `7D` | `0.1235` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 10,950.00 USD | 6,400.00 USD | 8,970.00 USD |
| `1D` | `0.1236` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 800.79 USD | 911.21 USD |
| `7D` | `0.1237` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 4,080.00 USD | 7,220.00 USD | 2,990.00 USD |
| `1D` | `0.1238` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 3,120.00 USD | 0.00 USD | 587.32 USD |
| `7D` | `0.1239` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 8,780.00 USD | 1,270.00 USD | 232.47 USD |
| `1D` | `0.1240` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 1,790.00 USD | 1,830.00 USD | 0.00 USD |
| `7D` | `0.1241` | 5,910,000.00 USD | 5,910,000.00 USD | 0.00 USD | 6,830.00 USD | 9,690.00 USD | 2,480.00 USD |
| `7D` | `0.1243` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 11,450.00 USD | 4,530.00 USD | 4,640.00 USD |
| `7D` | `0.1245` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 26,080.00 USD | 11,090.00 USD | 13,070.00 USD |
| `7D` | `0.1247` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 24,470.00 USD | 19,030.00 USD | 9,690.00 USD |
| `7D` | `0.1249` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 13,440.00 USD | 5,480.00 USD | 5,640.00 USD |
| `7D` | `0.1251` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 7,660.00 USD | 5,070.00 USD | 11,040.00 USD |
| `7D` | `0.1253` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 11,420.00 USD | 2,100.00 USD | 14,050.00 USD |
| `7D` | `0.1255` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 2,250.00 USD | 13,990.00 USD | 25.51 USD |
| `7D` | `0.1257` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 15,610.00 USD | 5,200.00 USD | 71.45 USD |
| `7D` | `0.1259` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 224.70 USD |
| `7D` | `0.1261` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | 3,590.00 USD |
| `7D` | `0.1263` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,080.00 USD |
| `7D` | `0.1265` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 2,710.00 USD | 0.00 USD | 3,270.00 USD |
| `7D` | `0.1267` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,950.00 USD |
| `7D` | `0.1269` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16.21 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `72.68M` | Total OI Tokens: `660,268,855.5 OP`
  * 1h OI Change: `-0.78%` | 4h OI Change: `-3.68%` | 24h OI Change: `-6.29%`
  * Exchange Breakdown: Binance=`16.59M` | Bybit=`14.13M` | OKX=`4.13M` | Hyperliquid=`3.89M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `337.86` | Last 24h: `270.64` | Last 3d: `-2.23K` | Last 7d: `-15.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0005%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0011%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0003%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0208%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `53.08%` | `46.92%` | `1.13` | 813,560.00 USD |
| `15M` | `Binance` | `63.79%` | `36.21%` | `1.76` | 288,090.00 USD |
| `15M` | `OKX` | `56.26%` | `43.74%` | `1.29` | 81,810.00 USD |
| `15M` | `Bybit` | `50.6%` | `49.4%` | `1.02` | 68,980.00 USD |
| `15M` | `KuCoin` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Gate` | `62.37%` | `37.63%` | `1.66` | 15,310.00 USD |
| `15M` | `Bitget` | `44.02%` | `55.98%` | `0.79` | 8,210.00 USD |
| `15M` | `BingX` | `44.33%` | `55.67%` | `0.80` | 125,850.00 USD |
| `15M` | `MEXC` | `68.82%` | `31.18%` | `2.21` | 72,620.00 USD |
| `15M` | `Bitunix` | `63.55%` | `36.45%` | `1.74` | 8,620.00 USD |
| `15M` | `Hyperliquid` | `35.74%` | `64.26%` | `0.56` | 3,030.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.99%` | `48.01%` | `1.08` | 77,860.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `1.37%` | `98.63%` | `0.01` | 62,660.00 USD |
| `15M` | `HTX` | `49.96%` | `50.04%` | `1.00` | 0.66 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 173.60 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 300.27 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `16.25%` | `83.75%` | `0.19` | 61.53 USD |
| `15M` | `Whale Positions` | `63.79%` | `36.21%` | `1.76` | 288,090.00 USD |
| `15M` | `Global Accounts` | `53.08%` | `46.92%` | `1.13` | 813,560.00 USD |
| `1H` | `OP` | `44.50%` | `55.50%` | `0.80` | 6,780,000.00 USD |
| `1H` | `Binance` | `49.94%` | `50.06%` | `1.00` | 2,240,000.00 USD |
| `1H` | `OKX` | `60.64%` | `39.36%` | `1.54` | 687,440.00 USD |
| `1H` | `Bybit` | `44.95%` | `55.05%` | `0.82` | 548,880.00 USD |
| `1H` | `KuCoin` | `48.22%` | `51.78%` | `0.93` | 196,970.00 USD |
| `1H` | `Gate` | `65.52%` | `34.48%` | `1.90` | 101,710.00 USD |
| `1H` | `Bitget` | `45.85%` | `54.15%` | `0.85` | 265,790.00 USD |
| `1H` | `BingX` | `12.57%` | `87.43%` | `0.14` | 1,360,000.00 USD |
| `1H` | `MEXC` | `69.25%` | `30.75%` | `2.25` | 572,760.00 USD |
| `1H` | `Bitunix` | `58.01%` | `41.99%` | `1.38` | 91,290.00 USD |
| `1H` | `Hyperliquid` | `33.44%` | `66.56%` | `0.50` | 91,150.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.59%` | `46.41%` | `1.15` | 336,830.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `44.17%` | `55.83%` | `0.79` | 233,940.00 USD |
| `1H` | `HTX` | `30.79%` | `69.21%` | `0.44` | 230.24 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `32.53%` | `67.47%` | `0.48` | 36,250.00 USD |
| `1H` | `Aster` | `26.18%` | `73.82%` | `0.35` | 2,320.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `16.22%` | `83.78%` | `0.19` | 400.29 USD |
| `1H` | `Whale Positions` | `49.94%` | `50.06%` | `1.00` | 2,240,000.00 USD |
| `1H` | `Global Accounts` | `44.50%` | `55.50%` | `0.80` | 6,780,000.00 USD |
| `4H` | `OP` | `46.35%` | `53.65%` | `0.86` | 91,450,000.00 USD |
| `4H` | `Binance` | `47.93%` | `52.07%` | `0.92` | 33,020,000.00 USD |
| `4H` | `OKX` | `48.04%` | `51.96%` | `0.92` | 17,650,000.00 USD |
| `4H` | `Bybit` | `48.65%` | `51.35%` | `0.95` | 8,590,000.00 USD |
| `4H` | `KuCoin` | `49.02%` | `50.98%` | `0.96` | 2,240,000.00 USD |
| `4H` | `Gate` | `49.34%` | `50.66%` | `0.97` | 1,500,000.00 USD |
| `4H` | `Bitget` | `41.62%` | `58.38%` | `0.71` | 2,530,000.00 USD |
| `4H` | `BingX` | `43.44%` | `56.56%` | `0.77` | 2,620,000.00 USD |
| `4H` | `MEXC` | `53.23%` | `46.77%` | `1.14` | 1,450,000.00 USD |
| `4H` | `Bitunix` | `49.3%` | `50.7%` | `0.97` | 2,590,000.00 USD |
| `4H` | `Hyperliquid` | `52.38%` | `47.62%` | `1.10` | 431,010.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.97%` | `50.03%` | `1.00` | 14,850,000.00 USD |
| `4H` | `Crypto.com` | `24.43%` | `75.57%` | `0.32` | 389.32 USD |
| `4H` | `WhiteBIT` | `0.56%` | `99.44%` | `0.01` | 3,430,000.00 USD |
| `4H` | `HTX` | `41.18%` | `58.82%` | `0.70` | 42,880.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `21.93%` | `78.07%` | `0.28` | 219,330.00 USD |
| `4H` | `Aster` | `27.64%` | `72.36%` | `0.38` | 203,630.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `44.5%` | `55.5%` | `0.80` | 86,360.00 USD |
| `4H` | `Whale Positions` | `47.93%` | `52.07%` | `0.92` | 33,020,000.00 USD |
| `4H` | `Global Accounts` | `46.35%` | `53.65%` | `0.86` | 91,450,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1123` | `0.1122` | `0.1123` | `0.1124` | `0.1119` | 385,611.74 USD | 157,293.82 USD | 228,317.92 USD | -71,024.10 USD | `-18.42%` | `5B / 10S` |
| `0:00 UTC` | `0.1114` | `0.1117` | `0.1114` | `0.1124` | `0.1110` | 525,538.44 USD | 243,812.31 USD | 281,726.13 USD | -37,913.82 USD | `-7.21%` | `25B / 41S` |
| `5:00 UTC` | `0.1107` | `0.1107` | `0.1107` | `0.1112` | `0.1101` | 919,895.36 USD | 440,104.81 USD | 479,790.55 USD | -39,685.74 USD | `-4.31%` | `22B / 21S` |
| `0:00 UTC` | `0.1113` | `0.1110` | `0.1113` | `0.1113` | `0.1106` | 261,230.00 USD | 123,873.54 USD | 137,356.46 USD | -13,482.93 USD | `-5.16%` | `17B / 9S` |
| `5:00 UTC` | `0.1108` | `0.1106` | `0.1108` | `0.1112` | `0.1101` | 266,281.73 USD | 113,817.33 USD | 152,464.41 USD | -38,647.08 USD | `-14.51%` | `15B / 30S` |
| `0:00 UTC` | `0.1097` | `0.1098` | `0.1097` | `0.1103` | `0.1094` | 698,148.28 USD | 345,564.95 USD | 352,583.33 USD | -7,018.38 USD | `-1.01%` | `13B / 19S` |
| `5:00 UTC` | `0.1102` | `0.1100` | `0.1102` | `0.1104` | `0.1095` | 273,714.46 USD | 165,910.77 USD | 107,803.69 USD | 58,107.08 USD | `+21.23%` | `25B / 9S` |
| `0:00 UTC` | `0.1097` | `0.1098` | `0.1097` | `0.1101` | `0.1096` | 225,346.74 USD | 116,304.67 USD | 109,042.07 USD | 7,262.60 USD | `+3.22%` | `6B / 4S` |
| `5:00 UTC` | `0.1098` | `0.1100` | `0.1098` | `0.1102` | `0.1096` | 199,782.25 USD | 121,152.98 USD | 78,629.27 USD | 42,523.71 USD | `+21.29%` | `24B / 5S` |
| `0:00 UTC` | `0.1100` | `0.1101` | `0.1100` | `0.1101` | `0.1100` | 830.70 USD | 751.30 USD | 79.40 USD | 671.91 USD | `+80.88%` | `2B / 0S` |

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
| `5m` | 3,370.00 USD | 15,770.00 USD | **`ACCUMULATION`** |
| `15m` | 8,060.00 USD | 14,080.00 USD | **`ACCUMULATION`** |
| `30m` | 16,190.00 USD | 92,750.00 USD | **`ACCUMULATION`** |
| `1h` | -8,800.00 USD | 30,860.00 USD | **`ACCUMULATION`** |
| `2h` | -24,220.00 USD | -148,160.00 USD | **`DISTRIBUTION`** |
| `4h` | -20,690.00 USD | -400,740.00 USD | **`DISTRIBUTION`** |
| `6h` | 147,040.00 USD | 201,570.00 USD | **`ACCUMULATION`** |
| `8h` | 188,150.00 USD | 350,540.00 USD | **`ACCUMULATION`** |
| `12h` | 223,300.00 USD | 881,370.00 USD | **`ACCUMULATION`** |
| `24h` | 61,050.00 USD | -1,420,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -83,670.00 USD | -9,530,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,440,000.00 USD | -78,630,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+3.37K` | 15m=`+8.06K` | 1h=`-8.80K` | 24h=`+61.05K`
* Futures Capital Netflows: 5m=`+15.77K` | 15m=`+14.08K` | 1h=`+30.86K` | 24h=`-1.42M`
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
  * `2026-10-30 00:57:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:47:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:16:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:59:49 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:59:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
