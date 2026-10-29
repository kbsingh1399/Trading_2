# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 00:35:21 IST` (`2026-10-29 19:05:21 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1099` | `0.1103` | `0.1099` | `0.1102` | `1,164,909` | 128,313.20 USD | 35,802.18 USD | `+27.90%` | -917,755.27 USD | `+0.89` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.1102` | `0.1104` | `0.1100` | `0.1100` | `586,840` | 64,668.64 USD | 11,033.57 USD | `+17.06%` | -906,721.69 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1100` | `0.1101` | `0.1096` | `0.1098` | `839,131` | 92,117.07 USD | -5,473.29 USD | `-5.94%` | -912,194.98 USD | `-0.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1103` | `0.1103` | `0.1094` | `0.1099` | `6,360,854` | 698,148.28 USD | -7,018.38 USD | `-1.01%` | -980,702.13 USD | `+0.01` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1099` | `0.1104` | `0.1095` | `0.1100` | `2,487,385` | 273,714.46 USD | 58,107.08 USD | `+21.23%` | -922,595.05 USD | `+0.90` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1100` | `0.1101` | `0.1096` | `0.1098` | `839,131` | 92,117.07 USD | -5,473.29 USD | `-5.94%` | -928,068.34 USD | `+0.09` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1129` | `0.1132` | `0.1101` | `0.1112` | `18,847,741` | 2,100,824.13 USD | -168,750.74 USD | `-8.03%` | -1,180,941.15 USD | `-0.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1112` | `0.1113` | `0.1094` | `0.1100` | `13,608,224` | 1,499,374.47 USD | -1,041.31 USD | `-0.07%` | -1,181,982.46 USD | `+0.26` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1100` | `0.1101` | `0.1096` | `0.1098` | `839,131` | 92,117.07 USD | -5,473.29 USD | `-5.94%` | -1,187,455.75 USD | `+0.24` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,229,700.44 USD | `+0.64` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -888,444.84 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1098` | `54,766,596` | 6,129,775.80 USD | -298,982.81 USD | `-4.88%` | -1,187,427.65 USD | `-0.16` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1131` | `0.1136` | `0.1072` | `0.1085` | `76,338,549` | 8,353,905.81 USD | -1,528,374.61 USD | `-18.30%` | -1,480,991.26 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1085` | `0.1106` | `0.1071` | `0.1076` | `47,048,931` | 5,111,570.05 USD | 108,567.99 USD | `+2.12%` | -1,372,423.27 USD | `+0.75` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,229,700.44 USD | `+0.64` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -888,444.84 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1098` | `54,766,596` | 6,129,775.80 USD | -298,982.81 USD | `-4.88%` | -1,187,427.65 USD | `-0.16` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:34:35 IST` |

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
| `Live` | `Long Liquidation` | `0.0385` | 174.65 USD | 242,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0395` | 237.00 USD | 242,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 247.30 USD | 242,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 3,450.00 USD | 242,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 3,460.00 USD | 238,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 829.69 USD | 235,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 1,100.00 USD | 234,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 353.81 USD | 233,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 509.64 USD | 233,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 518.48 USD | 232,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 1,920.00 USD | 232,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 25,370.00 USD | 230,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 110.79 USD | 204,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 48,850.00 USD | 204,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 1,020.00 USD | 155,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 2,010.00 USD | 154,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 878.62 USD | 152,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 1,320.00 USD | 151,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 223.98 USD | 150,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 1,560.00 USD | 150,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 2,350.00 USD | 148,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,120.00 USD | 146,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 443.16 USD | 143,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 17,600.00 USD | 142,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 69,120.00 USD | 125,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 4,640.00 USD | 56,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 419.87 USD | 51,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0975` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 2,560.00 USD | 7,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0975` | 12,670.00 USD | 51,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0977` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0979` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 1,530.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0981` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 5,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0983` | 1,980,000.00 USD | 1,980,000.00 USD | 3,250.00 USD | 1,070.00 USD | 9,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 3,920,000.00 USD | 3,920,000.00 USD | 7,990.00 USD | 1,230.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0985` | 1,970,000.00 USD | 1,970,000.00 USD | 5,670.00 USD | 413.94 USD | 2,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0985` | 3,900,000.00 USD | 3,900,000.00 USD | 7,110.00 USD | 0.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0985` | 19,960.00 USD | 38,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0987` | 1,960,000.00 USD | 1,960,000.00 USD | 7,790.00 USD | 2,190.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0987` | 3,890,000.00 USD | 3,890,000.00 USD | 5,390.00 USD | 9,190.00 USD | 37,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0989` | 1,950,000.00 USD | 1,950,000.00 USD | 2,450.00 USD | 2,550.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 3,830,000.00 USD | 3,830,000.00 USD | 12,260.00 USD | 4,520.00 USD | 27,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0991` | 1,940,000.00 USD | 1,940,000.00 USD | 4,800.00 USD | 2,950.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0991` | 3,790,000.00 USD | 3,790,000.00 USD | 14,350.00 USD | 10,350.00 USD | 13,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0993` | 1,930,000.00 USD | 1,930,000.00 USD | 1,550.00 USD | 1,220.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0993` | 3,750,000.00 USD | 3,750,000.00 USD | 23,920.00 USD | 10,140.00 USD | 24,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0995` | 1,910,000.00 USD | 1,910,000.00 USD | 2,740.00 USD | 624.33 USD | 9,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 3,690,000.00 USD | 3,690,000.00 USD | 13,090.00 USD | 6,160.00 USD | 25,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0997` | 1,900,000.00 USD | 1,900,000.00 USD | 2,320.00 USD | 718.82 USD | 10,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0997` | 3,650,000.00 USD | 3,650,000.00 USD | 21,100.00 USD | 5,500.00 USD | 32,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0999` | 1,890,000.00 USD | 1,890,000.00 USD | 4,680.00 USD | 2,940.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0999` | 3,590,000.00 USD | 3,590,000.00 USD | 14,230.00 USD | 6,540.00 USD | 18,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1001` | 1,880,000.00 USD | 1,880,000.00 USD | 2,660.00 USD | 1,410.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 3,550,000.00 USD | 3,550,000.00 USD | 29,230.00 USD | 3,010.00 USD | 10,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1003` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1003` | 3,510,000.00 USD | 3,510,000.00 USD | 8,010.00 USD | 7,060.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1005` | 1,870,000.00 USD | 1,870,000.00 USD | 1,970.00 USD | 403.62 USD | 1,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1005` | 3,490,000.00 USD | 3,490,000.00 USD | 25,070.00 USD | 11,000.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1005` | 427.25 USD | 18,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1007` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 430.11 USD | 807.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 3,430,000.00 USD | 3,430,000.00 USD | 10,260.00 USD | 2,280.00 USD | 14,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1009` | 1,860,000.00 USD | 1,860,000.00 USD | 1,250.00 USD | 2,750.00 USD | 23.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1009` | 3,410,000.00 USD | 3,410,000.00 USD | 15,320.00 USD | 3,070.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1011` | 1,860,000.00 USD | 1,860,000.00 USD | 1,570.00 USD | 575.54 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1011` | 3,380,000.00 USD | 3,380,000.00 USD | 4,430.00 USD | 4,720.00 USD | 8,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1013` | 1,850,000.00 USD | 1,850,000.00 USD | 4,900.00 USD | 2,290.00 USD | 645.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 3,360,000.00 USD | 3,360,000.00 USD | 12,870.00 USD | 4,030.00 USD | 3,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1015` | 1,850,000.00 USD | 1,850,000.00 USD | 2,790.00 USD | 1,830.00 USD | 4,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1015` | 3,340,000.00 USD | 3,340,000.00 USD | 6,830.00 USD | 965.35 USD | 2,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1015` | 622.37 USD | 17,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1017` | 1,840,000.00 USD | 1,840,000.00 USD | 1,660.00 USD | 4,600.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1017` | 3,330,000.00 USD | 3,330,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1019` | 1,820,000.00 USD | 1,820,000.00 USD | 6,600.00 USD | 3,420.00 USD | 5,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1019` | 3,310,000.00 USD | 3,310,000.00 USD | 9,260.00 USD | 5,790.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1021` | 1,810,000.00 USD | 1,810,000.00 USD | 2,580.00 USD | 1,320.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1021` | 3,280,000.00 USD | 3,280,000.00 USD | 7,900.00 USD | 3,270.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1023` | 1,800,000.00 USD | 1,800,000.00 USD | 4,600.00 USD | 2,120.00 USD | 4,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1023` | 3,270,000.00 USD | 3,270,000.00 USD | 4,030.00 USD | 4,990.00 USD | 14,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1025` | 1,790,000.00 USD | 1,790,000.00 USD | 855.19 USD | 2,500.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1025` | 3,240,000.00 USD | 3,240,000.00 USD | 1,550.00 USD | 0.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1025` | 17,360.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1027` | 1,780,000.00 USD | 1,780,000.00 USD | 2,780.00 USD | 1,590.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1027` | 3,230,000.00 USD | 3,230,000.00 USD | 2,250.00 USD | 2,580.00 USD | 378.73 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1029` | 1,780,000.00 USD | 1,780,000.00 USD | 4,340.00 USD | 705.79 USD | 6,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1029` | 3,230,000.00 USD | 3,230,000.00 USD | 7,420.00 USD | 3,000.00 USD | 395.35 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1031` | 1,760,000.00 USD | 1,760,000.00 USD | 11,600.00 USD | 3,910.00 USD | 8,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1031` | 3,220,000.00 USD | 3,220,000.00 USD | 13,690.00 USD | 5,070.00 USD | 10,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1033` | 1,740,000.00 USD | 1,740,000.00 USD | 8,760.00 USD | 2,790.00 USD | 10,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1033` | 3,190,000.00 USD | 3,190,000.00 USD | 3,880.00 USD | 2,640.00 USD | 15,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1035` | 1,720,000.00 USD | 1,720,000.00 USD | 7,450.00 USD | 6,850.00 USD | 10,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1035` | 3,170,000.00 USD | 3,170,000.00 USD | 2,710.00 USD | 9,400.00 USD | 15,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1037` | 1,690,000.00 USD | 1,690,000.00 USD | 2,220.00 USD | 13,000.00 USD | 9,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1037` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 19,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1039` | 1,670,000.00 USD | 1,670,000.00 USD | 3,660.00 USD | 1,730.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1039` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 5,170.00 USD | 95.01 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1041` | 1,650,000.00 USD | 1,650,000.00 USD | 7,790.00 USD | 6,910.00 USD | 13,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1041` | 3,110,000.00 USD | 3,110,000.00 USD | 5,940.00 USD | 2,910.00 USD | 10,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1043` | 1,620,000.00 USD | 1,620,000.00 USD | 17,650.00 USD | 5,650.00 USD | 7,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1043` | 3,090,000.00 USD | 3,090,000.00 USD | 15,960.00 USD | 5,980.00 USD | 21,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1045` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 2,600.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1045` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 3,830.00 USD | 14,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1047` | 1,580,000.00 USD | 1,580,000.00 USD | 4,610.00 USD | 2,610.00 USD | 16,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1047` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 1,720.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1049` | 1,560,000.00 USD | 1,560,000.00 USD | 21,050.00 USD | 2,430.00 USD | 10,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1049` | 3,010,000.00 USD | 3,010,000.00 USD | 34,790.00 USD | 4,810.00 USD | 35,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1051` | 1,530,000.00 USD | 1,530,000.00 USD | 16,410.00 USD | 8,750.00 USD | 24,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1051` | 2,930,000.00 USD | 2,930,000.00 USD | 17,290.00 USD | 11,500.00 USD | 48,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1053` | 1,480,000.00 USD | 1,480,000.00 USD | 30,920.00 USD | 7,040.00 USD | 25,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1053` | 2,860,000.00 USD | 2,860,000.00 USD | 53,590.00 USD | 29,800.00 USD | 95,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1055` | 1,410,000.00 USD | 1,410,000.00 USD | 28,440.00 USD | 19,380.00 USD | 34,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1055` | 2,680,000.00 USD | 2,680,000.00 USD | 50,090.00 USD | 27,290.00 USD | 126,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1057` | 1,330,000.00 USD | 1,330,000.00 USD | 23,000.00 USD | 22,610.00 USD | 44,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1057` | 2,470,000.00 USD | 2,470,000.00 USD | 50,380.00 USD | 45,760.00 USD | 74,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1059` | 1,240,000.00 USD | 1,240,000.00 USD | 15,180.00 USD | 21,000.00 USD | 53,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1059` | 2,300,000.00 USD | 2,300,000.00 USD | 92,510.00 USD | 49,670.00 USD | 114,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1061` | 1,150,000.00 USD | 1,150,000.00 USD | 10,960.00 USD | 9,820.00 USD | 42,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1061` | 2,050,000.00 USD | 2,050,000.00 USD | 38,260.00 USD | 26,050.00 USD | 76,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1063` | 1,090,000.00 USD | 1,090,000.00 USD | 56,400.00 USD | 14,600.00 USD | 48,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1063` | 1,910,000.00 USD | 1,910,000.00 USD | 84,260.00 USD | 38,330.00 USD | 148,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1065` | 967,880.00 USD | 967,880.00 USD | 18,270.00 USD | 14,110.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1065` | 1,630,000.00 USD | 1,630,000.00 USD | 91,170.00 USD | 18,790.00 USD | 93,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1067` | 916,090.00 USD | 916,090.00 USD | 9,710.00 USD | 15,160.00 USD | 33,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1067` | 1,430,000.00 USD | 1,430,000.00 USD | 97,290.00 USD | 36,720.00 USD | 67,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1069` | 858,100.00 USD | 858,100.00 USD | 24,070.00 USD | 7,520.00 USD | 34,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1069` | 1,230,000.00 USD | 1,230,000.00 USD | 76,900.00 USD | 32,620.00 USD | 72,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1071` | 792,020.00 USD | 792,020.00 USD | 48,660.00 USD | 4,860.00 USD | 18,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1071` | 1,050,000.00 USD | 1,050,000.00 USD | 119,440.00 USD | 27,240.00 USD | 42,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1073` | 719,590.00 USD | 719,590.00 USD | 8,740.00 USD | 10,680.00 USD | 20,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1073` | 858,500.00 USD | 858,500.00 USD | 58,480.00 USD | 17,700.00 USD | 31.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1075` | 679,270.00 USD | 679,270.00 USD | 26,670.00 USD | 6,770.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1075` | 782,290.00 USD | 782,290.00 USD | 20,750.00 USD | 3,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1077` | 631,890.00 USD | 631,890.00 USD | 16,370.00 USD | 17,750.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1077` | 758,030.00 USD | 758,030.00 USD | 0.00 USD | 0.00 USD | 8,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1079` | 578,270.00 USD | 578,270.00 USD | 19,540.00 USD | 15,690.00 USD | 29,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1079` | 749,390.00 USD | 749,390.00 USD | 140,450.00 USD | 23,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1081` | 513,810.00 USD | 513,810.00 USD | 17,730.00 USD | 7,210.00 USD | 52,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1081` | 584,950.00 USD | 584,950.00 USD | 205,390.00 USD | 11,660.00 USD | 28,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1083` | 436,340.00 USD | 436,340.00 USD | 20,890.00 USD | 6,690.00 USD | 33,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1083` | 339,040.00 USD | 339,040.00 USD | 94,800.00 USD | 2,110.00 USD | 42,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1085` | 374,890.00 USD | 374,890.00 USD | 22,270.00 USD | 13,850.00 USD | 65,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1085` | 199,730.00 USD | 199,730.00 USD | 15,920.00 USD | 4,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1087` | 273,750.00 USD | 273,750.00 USD | 44,350.00 USD | 8,210.00 USD | 44,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1087` | 179,610.00 USD | 179,610.00 USD | 55,430.00 USD | 6,210.00 USD | 60,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1089` | 176,530.00 USD | 176,530.00 USD | 30,880.00 USD | 17,080.00 USD | 41,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1089` | 57,900.00 USD | 57,900.00 USD | 5,290.00 USD | 14,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1091` | 87,010.00 USD | 87,010.00 USD | 33,700.00 USD | 6,410.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1091` | 38,040.00 USD | 38,040.00 USD | 16,310.00 USD | 3,800.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1093` | 38,730.00 USD | 38,730.00 USD | 15,480.00 USD | 3,890.00 USD | 8,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1093` | 8,930.00 USD | 8,930.00 USD | 0.00 USD | 0.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1095` | 10,860.00 USD | 10,860.00 USD | 0.00 USD | 0.00 USD | 10,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1095` | 181.59 USD | 181.59 USD | 0.00 USD | 0.00 USD | 181.59 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1103` | 29,800.00 USD | 29,800.00 USD | 23,720.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 17,490.00 USD | 17,490.00 USD | 17,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1105` | 37,230.00 USD | 37,230.00 USD | 0.00 USD | 10,030.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1107` | 78,260.00 USD | 78,260.00 USD | 0.00 USD | 12,720.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1107` | 49,740.00 USD | 49,740.00 USD | 0.00 USD | 12,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 62,170.00 USD | 62,170.00 USD | 0.00 USD | 12,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1113` | 128,600.00 USD | 128,600.00 USD | 15,810.00 USD | 3,630.00 USD | 30,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1115` | 133,370.00 USD | 133,370.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1117` | 182,010.00 USD | 182,010.00 USD | 0.00 USD | 24,680.00 USD | 23,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1117` | 101,440.00 USD | 101,440.00 USD | 0.00 USD | 22,780.00 USD | 16,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1119` | 231,240.00 USD | 231,240.00 USD | 26,390.00 USD | 5,030.00 USD | 17,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1119` | 144,540.00 USD | 144,540.00 USD | 25,250.00 USD | 7,050.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1121` | 256,820.00 USD | 256,820.00 USD | 13,180.00 USD | 6,940.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 165,720.00 USD | 165,720.00 USD | 0.00 USD | 0.00 USD | 21,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1123` | 301,700.00 USD | 301,700.00 USD | 39,630.00 USD | 1,780.00 USD | 3,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1123` | 228,230.00 USD | 228,230.00 USD | 12,360.00 USD | 23,980.00 USD | 26,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1125` | 311,320.00 USD | 311,320.00 USD | 0.00 USD | 7,040.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1125` | 257,060.00 USD | 257,060.00 USD | 0.00 USD | 0.00 USD | 28,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1127` | 315,510.00 USD | 315,510.00 USD | 0.00 USD | 1,250.00 USD | 2,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1129` | 320,960.00 USD | 320,960.00 USD | 5,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1129` | 257,130.00 USD | 257,130.00 USD | 0.00 USD | 0.00 USD | 65.26 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1131` | 356,490.00 USD | 356,490.00 USD | 17,560.00 USD | 6,360.00 USD | 11,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1131` | 284,760.00 USD | 284,760.00 USD | 12,540.00 USD | 0.00 USD | 15,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1133` | 409,010.00 USD | 409,010.00 USD | 6,530.00 USD | 22,520.00 USD | 23,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 290,320.00 USD | 290,320.00 USD | 0.00 USD | 5,450.00 USD | 110.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1135` | 415,930.00 USD | 415,930.00 USD | 4,040.00 USD | 2,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1135` | 304,840.00 USD | 304,840.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1137` | 416,830.00 USD | 416,830.00 USD | 0.00 USD | 856.93 USD | 40.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1139` | 431,100.00 USD | 431,100.00 USD | 0.00 USD | 0.00 USD | 14,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1141` | 457,460.00 USD | 457,460.00 USD | 13,860.00 USD | 2,800.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1141` | 322,760.00 USD | 322,760.00 USD | 10,380.00 USD | 0.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1143` | 511,220.00 USD | 511,220.00 USD | 18,160.00 USD | 26,130.00 USD | 9,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1143` | 401,370.00 USD | 401,370.00 USD | 0.00 USD | 0.00 USD | 78,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1145` | 573,140.00 USD | 573,140.00 USD | 13,430.00 USD | 11,690.00 USD | 36,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 561,810.00 USD | 561,810.00 USD | 16,540.00 USD | 2,730.00 USD | 141,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1147` | 616,790.00 USD | 616,790.00 USD | 6,800.00 USD | 8,840.00 USD | 28,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1147` | 706,300.00 USD | 706,300.00 USD | 9,880.00 USD | 0.00 USD | 134,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1149` | 678,800.00 USD | 678,800.00 USD | 35,170.00 USD | 624.71 USD | 26,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1149` | 789,610.00 USD | 789,610.00 USD | 10,560.00 USD | 0.00 USD | 72,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1151` | 761,180.00 USD | 761,180.00 USD | 21,360.00 USD | 14,620.00 USD | 46,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 1,010,000.00 USD | 1,010,000.00 USD | 92,570.00 USD | 4,210.00 USD | 128,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1153` | 898,010.00 USD | 898,010.00 USD | 39,450.00 USD | 29,420.00 USD | 67,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1153` | 1,320,000.00 USD | 1,320,000.00 USD | 153,720.00 USD | 8,400.00 USD | 139,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1155` | 1,030,000.00 USD | 1,030,000.00 USD | 48,310.00 USD | 27,080.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1155` | 1,610,000.00 USD | 1,610,000.00 USD | 149,360.00 USD | 40,110.00 USD | 105,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1157` | 1,100,000.00 USD | 1,100,000.00 USD | 37,790.00 USD | 12,010.00 USD | 25,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 1,800,000.00 USD | 1,800,000.00 USD | 133,960.00 USD | 3,760.00 USD | 48,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1159` | 1,170,000.00 USD | 1,170,000.00 USD | 27,270.00 USD | 12,000.00 USD | 25,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1159` | 1,950,000.00 USD | 1,950,000.00 USD | 89,430.00 USD | 12,710.00 USD | 53,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1161` | 1,240,000.00 USD | 1,240,000.00 USD | 30,570.00 USD | 6,970.00 USD | 36,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1161` | 2,240,000.00 USD | 2,240,000.00 USD | 146,810.00 USD | 37,250.00 USD | 100,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1163` | 1,290,000.00 USD | 1,290,000.00 USD | 18,210.00 USD | 14,540.00 USD | 17,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 2,380,000.00 USD | 2,380,000.00 USD | 66,560.00 USD | 11,460.00 USD | 68,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1165` | 1,320,000.00 USD | 1,320,000.00 USD | 14,300.00 USD | 13,560.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1165` | 2,520,000.00 USD | 2,520,000.00 USD | 68,620.00 USD | 35,720.00 USD | 27,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1167` | 1,360,000.00 USD | 1,360,000.00 USD | 10,500.00 USD | 16,690.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1167` | 2,660,000.00 USD | 2,660,000.00 USD | 79,610.00 USD | 21,620.00 USD | 41,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1169` | 1,390,000.00 USD | 1,390,000.00 USD | 16,040.00 USD | 4,350.00 USD | 9,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 2,830,000.00 USD | 2,830,000.00 USD | 65,340.00 USD | 14,840.00 USD | 86,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1171` | 1,410,000.00 USD | 1,410,000.00 USD | 17,090.00 USD | 3,890.00 USD | 4,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1171` | 2,930,000.00 USD | 2,930,000.00 USD | 57,350.00 USD | 11,370.00 USD | 35,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1173` | 1,450,000.00 USD | 1,450,000.00 USD | 14,960.00 USD | 8,910.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1173` | 3,020,000.00 USD | 3,020,000.00 USD | 40,860.00 USD | 9,190.00 USD | 36,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1175` | 1,500,000.00 USD | 1,500,000.00 USD | 11,510.00 USD | 17,150.00 USD | 24,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 3,130,000.00 USD | 3,130,000.00 USD | 38,840.00 USD | 12,300.00 USD | 58,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1177` | 1,550,000.00 USD | 1,550,000.00 USD | 19,300.00 USD | 8,560.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1177` | 3,220,000.00 USD | 3,220,000.00 USD | 33,330.00 USD | 20,350.00 USD | 43,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1179` | 1,590,000.00 USD | 1,590,000.00 USD | 19,180.00 USD | 5,840.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1179` | 3,320,000.00 USD | 3,320,000.00 USD | 66,670.00 USD | 10,940.00 USD | 23,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1181` | 1,620,000.00 USD | 1,620,000.00 USD | 15,480.00 USD | 6,030.00 USD | 14,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 3,380,000.00 USD | 3,380,000.00 USD | 22,290.00 USD | 15,780.00 USD | 17,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1183` | 1,640,000.00 USD | 1,640,000.00 USD | 7,310.00 USD | 1,400.00 USD | 9,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1183` | 3,430,000.00 USD | 3,430,000.00 USD | 4,040.00 USD | 1,800.00 USD | 39,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1185` | 1,670,000.00 USD | 1,670,000.00 USD | 8,760.00 USD | 7,830.00 USD | 13,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1185` | 3,460,000.00 USD | 3,460,000.00 USD | 3,880.00 USD | 5,130.00 USD | 22,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1187` | 1,700,000.00 USD | 1,700,000.00 USD | 11,520.00 USD | 8,520.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 3,510,000.00 USD | 3,510,000.00 USD | 5,620.00 USD | 15,370.00 USD | 32,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1189` | 1,710,000.00 USD | 1,710,000.00 USD | 4,220.00 USD | 3,060.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1189` | 3,560,000.00 USD | 3,560,000.00 USD | 27,240.00 USD | 15,060.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1191` | 1,730,000.00 USD | 1,730,000.00 USD | 4,940.00 USD | 6,690.00 USD | 3,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1191` | 3,700,000.00 USD | 3,700,000.00 USD | 22,650.00 USD | 15,330.00 USD | 109,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1193` | 1,740,000.00 USD | 1,740,000.00 USD | 4,720.00 USD | 2,080.00 USD | 3,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 3,730,000.00 USD | 3,730,000.00 USD | 21,260.00 USD | 0.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1195` | 1,760,000.00 USD | 1,760,000.00 USD | 9,550.00 USD | 3,210.00 USD | 2,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1195` | 3,780,000.00 USD | 3,780,000.00 USD | 11,190.00 USD | 1,780.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1197` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 1,040.00 USD | 93.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1197` | 3,810,000.00 USD | 3,810,000.00 USD | 6,780.00 USD | 10,800.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1199` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 3,050.00 USD | 3,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 3,880,000.00 USD | 3,880,000.00 USD | 9,100.00 USD | 0.00 USD | 64,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1201` | 1,780,000.00 USD | 1,780,000.00 USD | 6,460.00 USD | 1,070.00 USD | 8,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1201` | 4,040,000.00 USD | 4,040,000.00 USD | 114,140.00 USD | 16,380.00 USD | 29,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1203` | 1,790,000.00 USD | 1,790,000.00 USD | 5,670.00 USD | 413.94 USD | 2,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1203` | 4,150,000.00 USD | 4,150,000.00 USD | 70,770.00 USD | 29,250.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1205` | 1,790,000.00 USD | 1,790,000.00 USD | 2,250.00 USD | 1,670.00 USD | 745.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 4,410,000.00 USD | 4,410,000.00 USD | 86,480.00 USD | 48,720.00 USD | 128,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1207` | 1,800,000.00 USD | 1,800,000.00 USD | 5,540.00 USD | 524.23 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1207` | 4,500,000.00 USD | 4,500,000.00 USD | 12,460.00 USD | 19,400.00 USD | 53,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1209` | 1,810,000.00 USD | 1,810,000.00 USD | 2,450.00 USD | 2,550.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1209` | 4,700,000.00 USD | 4,700,000.00 USD | 85,160.00 USD | 19,340.00 USD | 94,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1211` | 1,820,000.00 USD | 1,820,000.00 USD | 4,800.00 USD | 2,950.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 4,770,000.00 USD | 4,770,000.00 USD | 27,400.00 USD | 16,260.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1213` | 1,830,000.00 USD | 1,830,000.00 USD | 1,550.00 USD | 1,220.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1213` | 4,840,000.00 USD | 4,840,000.00 USD | 23,920.00 USD | 26,740.00 USD | 24,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1215` | 1,840,000.00 USD | 1,840,000.00 USD | 1,650.00 USD | 0.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1215` | 4,920,000.00 USD | 4,920,000.00 USD | 5,900.00 USD | 6,620.00 USD | 59,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1217` | 1,840,000.00 USD | 1,840,000.00 USD | 1,090.00 USD | 624.33 USD | 5,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 4,970,000.00 USD | 4,970,000.00 USD | 18,490.00 USD | 23,600.00 USD | 11,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1219` | 1,860,000.00 USD | 1,860,000.00 USD | 2,320.00 USD | 718.82 USD | 10,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1219` | 5,040,000.00 USD | 5,040,000.00 USD | 26,700.00 USD | 5,500.00 USD | 38,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1221` | 1,870,000.00 USD | 1,870,000.00 USD | 4,680.00 USD | 2,940.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1221` | 5,130,000.00 USD | 5,130,000.00 USD | 47,890.00 USD | 21,770.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1223` | 1,880,000.00 USD | 1,880,000.00 USD | 2,660.00 USD | 1,410.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 5,320,000.00 USD | 5,320,000.00 USD | 103,180.00 USD | 36,290.00 USD | 48,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1225` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1225` | 5,380,000.00 USD | 5,380,000.00 USD | 43,040.00 USD | 19,970.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 16,900.00 USD | 16,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1227` | 1,880,000.00 USD | 1,880,000.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1227` | 5,540,000.00 USD | 5,540,000.00 USD | 65,240.00 USD | 31,790.00 USD | 55,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1229` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 403.62 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 5,670,000.00 USD | 5,670,000.00 USD | 63,350.00 USD | 34,190.00 USD | 40,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1231` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 430.11 USD | 809.11 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1231` | 5,760,000.00 USD | 5,760,000.00 USD | 25,460.00 USD | 29,380.00 USD | 27,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1233` | 1,890,000.00 USD | 1,890,000.00 USD | 1,250.00 USD | 2,750.00 USD | 0.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1233` | 5,870,000.00 USD | 5,870,000.00 USD | 57,130.00 USD | 13,020.00 USD | 40,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1235` | 1,890,000.00 USD | 1,890,000.00 USD | 1,570.00 USD | 575.54 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1235` | 5,890,000.00 USD | 5,890,000.00 USD | 10,950.00 USD | 6,400.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1237` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 1,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1237` | 5,910,000.00 USD | 5,910,000.00 USD | 4,080.00 USD | 9,720.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1239` | 1,900,000.00 USD | 1,900,000.00 USD | 4,900.00 USD | 724.40 USD | 587.65 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1239` | 5,920,000.00 USD | 5,920,000.00 USD | 8,780.00 USD | 1,270.00 USD | 479.13 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1241` | 1,910,000.00 USD | 1,910,000.00 USD | 2,790.00 USD | 1,830.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1241` | 5,940,000.00 USD | 5,940,000.00 USD | 6,830.00 USD | 9,690.00 USD | 2,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1243` | 1,920,000.00 USD | 1,920,000.00 USD | 1,660.00 USD | 4,600.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1243` | 5,960,000.00 USD | 5,960,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1245` | 1,940,000.00 USD | 1,940,000.00 USD | 6,600.00 USD | 3,420.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1245` | 6,010,000.00 USD | 6,010,000.00 USD | 26,080.00 USD | 11,090.00 USD | 12,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1247` | 1,950,000.00 USD | 1,950,000.00 USD | 2,580.00 USD | 1,320.00 USD | 4,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1247` | 6,060,000.00 USD | 6,060,000.00 USD | 24,470.00 USD | 19,030.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1249` | 6,090,000.00 USD | 6,090,000.00 USD | 13,440.00 USD | 5,480.00 USD | 5,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1251` | 6,110,000.00 USD | 6,110,000.00 USD | 7,660.00 USD | 5,070.00 USD | 11,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1253` | 6,140,000.00 USD | 6,140,000.00 USD | 11,420.00 USD | 2,100.00 USD | 14,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1255` | 6,160,000.00 USD | 6,160,000.00 USD | 2,250.00 USD | 13,990.00 USD | 33.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1257` | 6,180,000.00 USD | 6,180,000.00 USD | 15,610.00 USD | 5,200.00 USD | 54.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1259` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 288.60 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1261` | 6,180,000.00 USD | 6,180,000.00 USD | 4,270.00 USD | 0.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1263` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1265` | 6,190,000.00 USD | 6,190,000.00 USD | 2,710.00 USD | 0.00 USD | 3,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1267` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 0.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1269` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 0.00 USD | 16.21 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1355` | 1,330.00 USD | 18,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1515` | 15,150.00 USD | 33,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1555` | 6,210.00 USD | 39,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1565` | 550.61 USD | 40,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1635` | 20,210.00 USD | 60,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1695` | 169.25 USD | 60,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1865` | 167.85 USD | 60,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1925` | 930.49 USD | 61,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

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
| `Sell Stop` | `0.0635` | 176,260.00 USD | 0.00 USD | 1,140.00 USD | `-42.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 175,120.00 USD | 0.00 USD | 773.46 USD | `-35.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 174,350.00 USD | 0.00 USD | 592.27 USD | `-35.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 173,760.00 USD | 0.00 USD | 755.00 USD | `-31.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0805` | 173,000.00 USD | 0.00 USD | 411.06 USD | `-26.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0815` | 172,590.00 USD | 0.00 USD | 183.49 USD | `-25.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0835` | 172,410.00 USD | 0.00 USD | 456.70 USD | `-24.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 171,950.00 USD | 0.00 USD | 631.58 USD | `-22.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 171,320.00 USD | 0.00 USD | 653.74 USD | `-19.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0915` | 170,660.00 USD | 0.00 USD | 1,460.00 USD | `-16.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 169,200.00 USD | 0.00 USD | 485.13 USD | `-14.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0975` | 168,720.00 USD | 0.00 USD | 720.22 USD | `-11.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0985` | 168,000.00 USD | 0.00 USD | 931.75 USD | `-10.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0995` | 167,060.00 USD | 0.00 USD | 801.64 USD | `-9.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 166,260.00 USD | 0.00 USD | 1,470.00 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1015` | 164,790.00 USD | 0.00 USD | 903.42 USD | `-7.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 163,890.00 USD | 0.00 USD | 780.70 USD | `-6.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1035` | 163,110.00 USD | 0.00 USD | 4,650.00 USD | `-5.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1045` | 158,460.00 USD | 0.00 USD | 18,950.00 USD | `-5.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1055` | 139,510.00 USD | 0.00 USD | 7,770.00 USD | `-4.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1065` | 131,740.00 USD | 0.00 USD | 109,280.00 USD | `-3.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 22,450.00 USD | 0.00 USD | 21,670.00 USD | `-2.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 789.40 USD | 0.00 USD | 150.04 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1095` | 639.36 USD | 0.00 USD | 639.36 USD | `-0.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 162.59 USD | 162.59 USD | 0.00 USD | `+0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 1,000.00 USD | 839.64 USD | 0.00 USD | `+1.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1125` | 2,690.00 USD | 1,680.00 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1135` | 2,800.00 USD | 116.27 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1145` | 2,940.00 USD | 134.61 USD | 0.00 USD | `+4.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 3,430.00 USD | 489.97 USD | 0.00 USD | `+4.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1165` | 3,890.00 USD | 466.94 USD | 0.00 USD | `+5.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1175` | 31,420.00 USD | 27,530.00 USD | 0.00 USD | `+6.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1185` | 32,480.00 USD | 1,050.00 USD | 0.00 USD | `+7.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1195` | 47,110.00 USD | 14,640.00 USD | 0.00 USD | `+8.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1205` | 47,510.00 USD | 398.42 USD | 0.00 USD | `+9.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1225` | 48,490.00 USD | 980.00 USD | 0.00 USD | `+11.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1235` | 61,470.00 USD | 12,980.00 USD | 0.00 USD | `+12.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1255` | 65,850.00 USD | 4,380.00 USD | 0.00 USD | `+14.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1265` | 76,310.00 USD | 10,460.00 USD | 0.00 USD | `+14.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1275` | 76,800.00 USD | 492.06 USD | 0.00 USD | `+15.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1305` | 77,240.00 USD | 444.24 USD | 0.00 USD | `+18.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1315` | 108,810.00 USD | 31,560.00 USD | 0.00 USD | `+19.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1335` | 110,120.00 USD | 1,310.00 USD | 0.00 USD | `+21.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1345` | 114,270.00 USD | 4,150.00 USD | 0.00 USD | `+22.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1365` | 124,960.00 USD | 10,690.00 USD | 0.00 USD | `+24.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1405` | 138,070.00 USD | 13,110.00 USD | 0.00 USD | `+27.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1425` | 138,170.00 USD | 102.22 USD | 0.00 USD | `+29.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1435` | 145,350.00 USD | 7,180.00 USD | 0.00 USD | `+30.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1485` | 147,990.00 USD | 2,650.00 USD | 0.00 USD | `+34.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1495` | 148,790.00 USD | 792.53 USD | 0.00 USD | `+35.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1525` | 152,550.00 USD | 3,770.00 USD | 0.00 USD | `+38.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 152,740.00 USD | 184.49 USD | 0.00 USD | `+41.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 159,460.00 USD | 6,720.00 USD | 0.00 USD | `+42.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 159,680.00 USD | 219.81 USD | 0.00 USD | `+43.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 159,960.00 USD | 277.62 USD | 0.00 USD | `+48.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 161,750.00 USD | 1,800.00 USD | 0.00 USD | `+54.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 161,970.00 USD | 216.55 USD | 0.00 USD | `+58.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 162,080.00 USD | 117.26 USD | 0.00 USD | `+79.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 182,620.00 USD | 20,530.00 USD | 0.00 USD | `+82.22%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0975` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 0.00 USD | 2,560.00 USD | 7,140.00 USD |
| `7D` | `0.0977` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD |
| `7D` | `0.0979` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 0.00 USD | 1,530.00 USD | 5,710.00 USD |
| `7D` | `0.0981` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 5,910.00 USD |
| `1D` | `0.0983` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 3,250.00 USD | 1,070.00 USD | 9,080.00 USD |
| `7D` | `0.0983` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 7,990.00 USD | 1,230.00 USD | 8,890.00 USD |
| `1D` | `0.0985` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 5,670.00 USD | 413.94 USD | 2,690.00 USD |
| `7D` | `0.0985` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 7,110.00 USD | 0.00 USD | 6,320.00 USD |
| `1D` | `0.0987` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 7,790.00 USD | 2,190.00 USD | 3,300.00 USD |
| `7D` | `0.0987` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 5,390.00 USD | 9,190.00 USD | 37,300.00 USD |
| `1D` | `0.0989` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 2,450.00 USD | 2,550.00 USD | 2,180.00 USD |
| `7D` | `0.0989` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 12,260.00 USD | 4,520.00 USD | 27,250.00 USD |
| `1D` | `0.0991` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 4,800.00 USD | 2,950.00 USD | 3,200.00 USD |
| `7D` | `0.0991` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 14,350.00 USD | 10,350.00 USD | 13,620.00 USD |
| `1D` | `0.0993` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 1,550.00 USD | 1,220.00 USD | 10,390.00 USD |
| `7D` | `0.0993` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 23,920.00 USD | 10,140.00 USD | 24,070.00 USD |
| `1D` | `0.0995` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 2,740.00 USD | 624.33 USD | 9,240.00 USD |
| `7D` | `0.0995` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 13,090.00 USD | 6,160.00 USD | 25,320.00 USD |
| `1D` | `0.0997` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 2,320.00 USD | 718.82 USD | 10,030.00 USD |
| `7D` | `0.0997` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 21,100.00 USD | 5,500.00 USD | 32,910.00 USD |
| `1D` | `0.0999` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 4,680.00 USD | 2,940.00 USD | 3,670.00 USD |
| `7D` | `0.0999` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 14,230.00 USD | 6,540.00 USD | 18,750.00 USD |
| `1D` | `0.1001` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 2,660.00 USD | 1,410.00 USD | 4,200.00 USD |
| `7D` | `0.1001` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 29,230.00 USD | 3,010.00 USD | 10,890.00 USD |
| `1D` | `0.1003` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 0.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1003` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 8,010.00 USD | 7,060.00 USD | 5,300.00 USD |
| `1D` | `0.1005` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 1,970.00 USD | 403.62 USD | 1,140.00 USD |
| `7D` | `0.1005` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 25,070.00 USD | 11,000.00 USD | 18,380.00 USD |
| `1D` | `0.1007` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 0.00 USD | 430.11 USD | 807.50 USD |
| `7D` | `0.1007` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 10,260.00 USD | 2,280.00 USD | 14,140.00 USD |
| `1D` | `0.1009` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 1,250.00 USD | 2,750.00 USD | 23.95 USD |
| `7D` | `0.1009` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 15,320.00 USD | 3,070.00 USD | 6,750.00 USD |
| `1D` | `0.1011` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 1,570.00 USD | 575.54 USD | 3,420.00 USD |
| `7D` | `0.1011` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 4,430.00 USD | 4,720.00 USD | 8,990.00 USD |
| `1D` | `0.1013` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 4,900.00 USD | 2,290.00 USD | 645.83 USD |
| `7D` | `0.1013` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 12,870.00 USD | 4,030.00 USD | 3,110.00 USD |
| `1D` | `0.1015` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 2,790.00 USD | 1,830.00 USD | 4,320.00 USD |
| `7D` | `0.1015` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 6,830.00 USD | 965.35 USD | 2,450.00 USD |
| `1D` | `0.1017` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 1,660.00 USD | 4,600.00 USD | 7,590.00 USD |
| `7D` | `0.1017` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,730.00 USD |
| `1D` | `0.1019` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 6,600.00 USD | 3,420.00 USD | 5,520.00 USD |
| `7D` | `0.1019` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 9,260.00 USD | 5,790.00 USD | 13,110.00 USD |
| `1D` | `0.1021` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 2,580.00 USD | 1,320.00 USD | 4,780.00 USD |
| `7D` | `0.1021` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 7,900.00 USD | 3,270.00 USD | 7,150.00 USD |
| `1D` | `0.1023` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 4,600.00 USD | 2,120.00 USD | 4,710.00 USD |
| `7D` | `0.1023` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 4,030.00 USD | 4,990.00 USD | 14,400.00 USD |
| `1D` | `0.1025` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 855.19 USD | 2,500.00 USD | 3,620.00 USD |
| `7D` | `0.1025` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 1,550.00 USD | 0.00 USD | 5,780.00 USD |
| `1D` | `0.1027` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 2,780.00 USD | 1,590.00 USD | 1,620.00 USD |
| `7D` | `0.1027` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 2,250.00 USD | 2,580.00 USD | 378.73 USD |
| `1D` | `0.1029` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 4,340.00 USD | 705.79 USD | 6,270.00 USD |
| `7D` | `0.1029` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 7,420.00 USD | 3,000.00 USD | 395.35 USD |
| `1D` | `0.1031` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 11,600.00 USD | 3,910.00 USD | 8,130.00 USD |
| `7D` | `0.1031` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 13,690.00 USD | 5,070.00 USD | 10,810.00 USD |
| `1D` | `0.1033` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 8,760.00 USD | 2,790.00 USD | 10,470.00 USD |
| `7D` | `0.1033` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 3,880.00 USD | 2,640.00 USD | 15,230.00 USD |
| `1D` | `0.1035` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 7,450.00 USD | 6,850.00 USD | 10,270.00 USD |
| `7D` | `0.1035` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 2,710.00 USD | 9,400.00 USD | 15,870.00 USD |
| `1D` | `0.1037` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 2,220.00 USD | 13,000.00 USD | 9,270.00 USD |
| `7D` | `0.1037` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 19,530.00 USD |
| `1D` | `0.1039` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 3,660.00 USD | 1,730.00 USD | 11,830.00 USD |
| `7D` | `0.1039` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 0.00 USD | 5,170.00 USD | 95.01 USD |
| `1D` | `0.1041` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 7,790.00 USD | 6,910.00 USD | 13,290.00 USD |
| `7D` | `0.1041` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 5,940.00 USD | 2,910.00 USD | 10,710.00 USD |
| `1D` | `0.1043` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 17,650.00 USD | 5,650.00 USD | 7,860.00 USD |
| `7D` | `0.1043` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 15,960.00 USD | 5,980.00 USD | 21,040.00 USD |
| `1D` | `0.1045` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 0.00 USD | 2,600.00 USD | 6,210.00 USD |
| `7D` | `0.1045` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 0.00 USD | 3,830.00 USD | 14,910.00 USD |
| `1D` | `0.1047` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 4,610.00 USD | 2,610.00 USD | 16,540.00 USD |
| `7D` | `0.1047` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 0.00 USD | 1,720.00 USD | 23,040.00 USD |
| `1D` | `0.1049` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 21,050.00 USD | 2,430.00 USD | 10,840.00 USD |
| `7D` | `0.1049` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 34,790.00 USD | 4,810.00 USD | 35,460.00 USD |
| `1D` | `0.1051` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 16,410.00 USD | 8,750.00 USD | 24,260.00 USD |
| `7D` | `0.1051` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 17,290.00 USD | 11,500.00 USD | 48,850.00 USD |
| `1D` | `0.1053` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 30,920.00 USD | 7,040.00 USD | 25,570.00 USD |
| `7D` | `0.1053` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 53,590.00 USD | 29,800.00 USD | 95,520.00 USD |
| `1D` | `0.1055` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 28,440.00 USD | 19,380.00 USD | 34,470.00 USD |
| `7D` | `0.1055` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 50,090.00 USD | 27,290.00 USD | 126,380.00 USD |
| `1D` | `0.1057` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 23,000.00 USD | 22,610.00 USD | 44,560.00 USD |
| `7D` | `0.1057` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 50,380.00 USD | 45,760.00 USD | 74,280.00 USD |
| `1D` | `0.1059` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 15,180.00 USD | 21,000.00 USD | 53,400.00 USD |
| `7D` | `0.1059` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 92,510.00 USD | 49,670.00 USD | 114,090.00 USD |
| `1D` | `0.1061` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 10,960.00 USD | 9,820.00 USD | 42,650.00 USD |
| `7D` | `0.1061` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 38,260.00 USD | 26,050.00 USD | 76,350.00 USD |
| `1D` | `0.1063` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 56,400.00 USD | 14,600.00 USD | 48,900.00 USD |
| `7D` | `0.1063` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 84,260.00 USD | 38,330.00 USD | 148,850.00 USD |
| `1D` | `0.1065` | 967,880.00 USD | 0.00 USD | 967,880.00 USD | 18,270.00 USD | 14,110.00 USD | 19,400.00 USD |
| `7D` | `0.1065` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 91,170.00 USD | 18,790.00 USD | 93,040.00 USD |
| `1D` | `0.1067` | 916,090.00 USD | 0.00 USD | 916,090.00 USD | 9,710.00 USD | 15,160.00 USD | 33,130.00 USD |
| `7D` | `0.1067` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 97,290.00 USD | 36,720.00 USD | 67,930.00 USD |
| `1D` | `0.1069` | 858,100.00 USD | 0.00 USD | 858,100.00 USD | 24,070.00 USD | 7,520.00 USD | 34,480.00 USD |
| `7D` | `0.1069` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 76,900.00 USD | 32,620.00 USD | 72,030.00 USD |
| `1D` | `0.1071` | 792,020.00 USD | 0.00 USD | 792,020.00 USD | 48,660.00 USD | 4,860.00 USD | 18,930.00 USD |
| `7D` | `0.1071` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 119,440.00 USD | 27,240.00 USD | 42,640.00 USD |
| `1D` | `0.1073` | 719,590.00 USD | 0.00 USD | 719,590.00 USD | 8,740.00 USD | 10,680.00 USD | 20,900.00 USD |
| `7D` | `0.1073` | 858,500.00 USD | 0.00 USD | 858,500.00 USD | 58,480.00 USD | 17,700.00 USD | 31.64 USD |
| `1D` | `0.1075` | 679,270.00 USD | 0.00 USD | 679,270.00 USD | 26,670.00 USD | 6,770.00 USD | 13,950.00 USD |
| `7D` | `0.1075` | 782,290.00 USD | 0.00 USD | 782,290.00 USD | 20,750.00 USD | 3,500.00 USD | 0.00 USD |
| `1D` | `0.1077` | 631,890.00 USD | 0.00 USD | 631,890.00 USD | 16,370.00 USD | 17,750.00 USD | 19,500.00 USD |
| `7D` | `0.1077` | 758,030.00 USD | 0.00 USD | 758,030.00 USD | 0.00 USD | 0.00 USD | 8,640.00 USD |
| `1D` | `0.1079` | 578,270.00 USD | 0.00 USD | 578,270.00 USD | 19,540.00 USD | 15,690.00 USD | 29,230.00 USD |
| `7D` | `0.1079` | 749,390.00 USD | 0.00 USD | 749,390.00 USD | 140,450.00 USD | 23,980.00 USD | 0.00 USD |
| `1D` | `0.1081` | 513,810.00 USD | 0.00 USD | 513,810.00 USD | 17,730.00 USD | 7,210.00 USD | 52,540.00 USD |
| `7D` | `0.1081` | 584,950.00 USD | 0.00 USD | 584,950.00 USD | 205,390.00 USD | 11,660.00 USD | 28,860.00 USD |
| `1D` | `0.1083` | 436,340.00 USD | 0.00 USD | 436,340.00 USD | 20,890.00 USD | 6,690.00 USD | 33,870.00 USD |
| `7D` | `0.1083` | 339,040.00 USD | 0.00 USD | 339,040.00 USD | 94,800.00 USD | 2,110.00 USD | 42,410.00 USD |
| `1D` | `0.1085` | 374,890.00 USD | 0.00 USD | 374,890.00 USD | 22,270.00 USD | 13,850.00 USD | 65,020.00 USD |
| `7D` | `0.1085` | 199,730.00 USD | 0.00 USD | 199,730.00 USD | 15,920.00 USD | 4,200.00 USD | 0.00 USD |
| `1D` | `0.1087` | 273,750.00 USD | 0.00 USD | 273,750.00 USD | 44,350.00 USD | 8,210.00 USD | 44,670.00 USD |
| `7D` | `0.1087` | 179,610.00 USD | 0.00 USD | 179,610.00 USD | 55,430.00 USD | 6,210.00 USD | 60,070.00 USD |
| `1D` | `0.1089` | 176,530.00 USD | 0.00 USD | 176,530.00 USD | 30,880.00 USD | 17,080.00 USD | 41,550.00 USD |
| `7D` | `0.1089` | 57,900.00 USD | 0.00 USD | 57,900.00 USD | 5,290.00 USD | 14,560.00 USD | 0.00 USD |
| `1D` | `0.1091` | 87,010.00 USD | 0.00 USD | 87,010.00 USD | 33,700.00 USD | 6,410.00 USD | 8,180.00 USD |
| `7D` | `0.1091` | 38,040.00 USD | 0.00 USD | 38,040.00 USD | 16,310.00 USD | 3,800.00 USD | 9,010.00 USD |
| `1D` | `0.1093` | 38,730.00 USD | 0.00 USD | 38,730.00 USD | 15,480.00 USD | 3,890.00 USD | 8,500.00 USD |
| `7D` | `0.1093` | 8,930.00 USD | 0.00 USD | 8,930.00 USD | 0.00 USD | 0.00 USD | 8,750.00 USD |
| `1D` | `0.1095` | 10,860.00 USD | 0.00 USD | 10,860.00 USD | 0.00 USD | 0.00 USD | 10,860.00 USD |
| `7D` | `0.1095` | 181.59 USD | 0.00 USD | 181.59 USD | 0.00 USD | 0.00 USD | 181.59 USD |
| `1D` | `0.1101` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1101` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1103` | 29,800.00 USD | 29,800.00 USD | 0.00 USD | 23,720.00 USD | 0.00 USD | 6,070.00 USD |
| `7D` | `0.1103` | 17,490.00 USD | 17,490.00 USD | 0.00 USD | 17,490.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1105` | 37,230.00 USD | 37,230.00 USD | 0.00 USD | 0.00 USD | 10,030.00 USD | 9,710.00 USD |
| `1D` | `0.1107` | 78,260.00 USD | 78,260.00 USD | 0.00 USD | 0.00 USD | 12,720.00 USD | 35,750.00 USD |
| `7D` | `0.1107` | 49,740.00 USD | 49,740.00 USD | 0.00 USD | 0.00 USD | 12,510.00 USD | 0.00 USD |
| `7D` | `0.1109` | 62,170.00 USD | 62,170.00 USD | 0.00 USD | 0.00 USD | 12,430.00 USD | 0.00 USD |
| `1D` | `0.1113` | 128,600.00 USD | 128,600.00 USD | 0.00 USD | 15,810.00 USD | 3,630.00 USD | 30,900.00 USD |
| `1D` | `0.1115` | 133,370.00 USD | 133,370.00 USD | 0.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1117` | 182,010.00 USD | 182,010.00 USD | 0.00 USD | 0.00 USD | 24,680.00 USD | 23,960.00 USD |
| `7D` | `0.1117` | 101,440.00 USD | 101,440.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | 16,490.00 USD |
| `1D` | `0.1119` | 231,240.00 USD | 231,240.00 USD | 0.00 USD | 26,390.00 USD | 5,030.00 USD | 17,820.00 USD |
| `7D` | `0.1119` | 144,540.00 USD | 144,540.00 USD | 0.00 USD | 25,250.00 USD | 7,050.00 USD | 10,800.00 USD |
| `1D` | `0.1121` | 256,820.00 USD | 256,820.00 USD | 0.00 USD | 13,180.00 USD | 6,940.00 USD | 5,450.00 USD |
| `7D` | `0.1121` | 165,720.00 USD | 165,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,180.00 USD |
| `1D` | `0.1123` | 301,700.00 USD | 301,700.00 USD | 0.00 USD | 39,630.00 USD | 1,780.00 USD | 3,460.00 USD |
| `7D` | `0.1123` | 228,230.00 USD | 228,230.00 USD | 0.00 USD | 12,360.00 USD | 23,980.00 USD | 26,180.00 USD |
| `1D` | `0.1125` | 311,320.00 USD | 311,320.00 USD | 0.00 USD | 0.00 USD | 7,040.00 USD | 2,590.00 USD |
| `7D` | `0.1125` | 257,060.00 USD | 257,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,830.00 USD |
| `1D` | `0.1127` | 315,510.00 USD | 315,510.00 USD | 0.00 USD | 0.00 USD | 1,250.00 USD | 2,950.00 USD |
| `1D` | `0.1129` | 320,960.00 USD | 320,960.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1129` | 257,130.00 USD | 257,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65.26 USD |
| `1D` | `0.1131` | 356,490.00 USD | 356,490.00 USD | 0.00 USD | 17,560.00 USD | 6,360.00 USD | 11,620.00 USD |
| `7D` | `0.1131` | 284,760.00 USD | 284,760.00 USD | 0.00 USD | 12,540.00 USD | 0.00 USD | 15,090.00 USD |
| `1D` | `0.1133` | 409,010.00 USD | 409,010.00 USD | 0.00 USD | 6,530.00 USD | 22,520.00 USD | 23,470.00 USD |
| `7D` | `0.1133` | 290,320.00 USD | 290,320.00 USD | 0.00 USD | 0.00 USD | 5,450.00 USD | 110.20 USD |
| `1D` | `0.1135` | 415,930.00 USD | 415,930.00 USD | 0.00 USD | 4,040.00 USD | 2,880.00 USD | 0.00 USD |
| `7D` | `0.1135` | 304,840.00 USD | 304,840.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD |
| `1D` | `0.1137` | 416,830.00 USD | 416,830.00 USD | 0.00 USD | 0.00 USD | 856.93 USD | 40.44 USD |
| `1D` | `0.1139` | 431,100.00 USD | 431,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,260.00 USD |
| `1D` | `0.1141` | 457,460.00 USD | 457,460.00 USD | 0.00 USD | 13,860.00 USD | 2,800.00 USD | 9,710.00 USD |
| `7D` | `0.1141` | 322,760.00 USD | 322,760.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,540.00 USD |
| `1D` | `0.1143` | 511,220.00 USD | 511,220.00 USD | 0.00 USD | 18,160.00 USD | 26,130.00 USD | 9,470.00 USD |
| `7D` | `0.1143` | 401,370.00 USD | 401,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78,600.00 USD |
| `1D` | `0.1145` | 573,140.00 USD | 573,140.00 USD | 0.00 USD | 13,430.00 USD | 11,690.00 USD | 36,800.00 USD |
| `7D` | `0.1145` | 561,810.00 USD | 561,810.00 USD | 0.00 USD | 16,540.00 USD | 2,730.00 USD | 141,180.00 USD |
| `1D` | `0.1147` | 616,790.00 USD | 616,790.00 USD | 0.00 USD | 6,800.00 USD | 8,840.00 USD | 28,000.00 USD |
| `7D` | `0.1147` | 706,300.00 USD | 706,300.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 134,610.00 USD |
| `1D` | `0.1149` | 678,800.00 USD | 678,800.00 USD | 0.00 USD | 35,170.00 USD | 624.71 USD | 26,220.00 USD |
| `7D` | `0.1149` | 789,610.00 USD | 789,610.00 USD | 0.00 USD | 10,560.00 USD | 0.00 USD | 72,750.00 USD |
| `1D` | `0.1151` | 761,180.00 USD | 761,180.00 USD | 0.00 USD | 21,360.00 USD | 14,620.00 USD | 46,390.00 USD |
| `7D` | `0.1151` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 92,570.00 USD | 4,210.00 USD | 128,500.00 USD |
| `1D` | `0.1153` | 898,010.00 USD | 898,010.00 USD | 0.00 USD | 39,450.00 USD | 29,420.00 USD | 67,960.00 USD |
| `7D` | `0.1153` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 153,720.00 USD | 8,400.00 USD | 139,830.00 USD |
| `1D` | `0.1155` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 48,310.00 USD | 27,080.00 USD | 54,030.00 USD |
| `7D` | `0.1155` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 149,360.00 USD | 40,110.00 USD | 105,750.00 USD |
| `1D` | `0.1157` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 37,790.00 USD | 12,010.00 USD | 25,390.00 USD |
| `7D` | `0.1157` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 133,960.00 USD | 3,760.00 USD | 48,320.00 USD |
| `1D` | `0.1159` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 27,270.00 USD | 12,000.00 USD | 25,170.00 USD |
| `7D` | `0.1159` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 89,430.00 USD | 12,710.00 USD | 53,380.00 USD |
| `1D` | `0.1161` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 30,570.00 USD | 6,970.00 USD | 36,500.00 USD |
| `7D` | `0.1161` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 146,810.00 USD | 37,250.00 USD | 100,110.00 USD |
| `1D` | `0.1163` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 18,210.00 USD | 14,540.00 USD | 17,460.00 USD |
| `7D` | `0.1163` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 66,560.00 USD | 11,460.00 USD | 68,560.00 USD |
| `1D` | `0.1165` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 14,300.00 USD | 13,560.00 USD | 5,490.00 USD |
| `7D` | `0.1165` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 68,620.00 USD | 35,720.00 USD | 27,080.00 USD |
| `1D` | `0.1167` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 10,500.00 USD | 16,690.00 USD | 6,170.00 USD |
| `7D` | `0.1167` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 79,610.00 USD | 21,620.00 USD | 41,290.00 USD |
| `1D` | `0.1169` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 16,040.00 USD | 4,350.00 USD | 9,830.00 USD |
| `7D` | `0.1169` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 65,340.00 USD | 14,840.00 USD | 86,630.00 USD |
| `1D` | `0.1171` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 17,090.00 USD | 3,890.00 USD | 4,510.00 USD |
| `7D` | `0.1171` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 57,350.00 USD | 11,370.00 USD | 35,090.00 USD |
| `1D` | `0.1173` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 14,960.00 USD | 8,910.00 USD | 11,440.00 USD |
| `7D` | `0.1173` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 40,860.00 USD | 9,190.00 USD | 36,730.00 USD |
| `1D` | `0.1175` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 11,510.00 USD | 17,150.00 USD | 24,400.00 USD |
| `7D` | `0.1175` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 38,840.00 USD | 12,300.00 USD | 58,980.00 USD |
| `1D` | `0.1177` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 19,300.00 USD | 8,560.00 USD | 16,650.00 USD |
| `7D` | `0.1177` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 33,330.00 USD | 20,350.00 USD | 43,940.00 USD |
| `1D` | `0.1179` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 19,180.00 USD | 5,840.00 USD | 14,520.00 USD |
| `7D` | `0.1179` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 66,670.00 USD | 10,940.00 USD | 23,910.00 USD |
| `1D` | `0.1181` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 15,480.00 USD | 6,030.00 USD | 14,980.00 USD |
| `7D` | `0.1181` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 22,290.00 USD | 15,780.00 USD | 17,780.00 USD |
| `1D` | `0.1183` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 7,310.00 USD | 1,400.00 USD | 9,080.00 USD |
| `7D` | `0.1183` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 4,040.00 USD | 1,800.00 USD | 39,300.00 USD |
| `1D` | `0.1185` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 8,760.00 USD | 7,830.00 USD | 13,370.00 USD |
| `7D` | `0.1185` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 3,880.00 USD | 5,130.00 USD | 22,460.00 USD |
| `1D` | `0.1187` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 11,520.00 USD | 8,520.00 USD | 11,670.00 USD |
| `7D` | `0.1187` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 5,620.00 USD | 15,370.00 USD | 32,000.00 USD |
| `1D` | `0.1189` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 4,220.00 USD | 3,060.00 USD | 4,350.00 USD |
| `7D` | `0.1189` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 27,240.00 USD | 15,060.00 USD | 3,250.00 USD |
| `1D` | `0.1191` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 4,940.00 USD | 6,690.00 USD | 3,510.00 USD |
| `7D` | `0.1191` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 22,650.00 USD | 15,330.00 USD | 109,210.00 USD |
| `1D` | `0.1193` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 4,720.00 USD | 2,080.00 USD | 3,840.00 USD |
| `7D` | `0.1193` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 21,260.00 USD | 0.00 USD | 9,310.00 USD |
| `1D` | `0.1195` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 9,550.00 USD | 3,210.00 USD | 2,810.00 USD |
| `7D` | `0.1195` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 11,190.00 USD | 1,780.00 USD | 29,380.00 USD |
| `1D` | `0.1197` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 1,040.00 USD | 93.72 USD |
| `7D` | `0.1197` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 6,780.00 USD | 10,800.00 USD | 14,300.00 USD |
| `1D` | `0.1199` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 3,050.00 USD | 3,080.00 USD |
| `7D` | `0.1199` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 9,100.00 USD | 0.00 USD | 64,440.00 USD |
| `1D` | `0.1201` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 6,460.00 USD | 1,070.00 USD | 8,070.00 USD |
| `7D` | `0.1201` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 114,140.00 USD | 16,380.00 USD | 29,150.00 USD |
| `1D` | `0.1203` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 5,670.00 USD | 413.94 USD | 2,710.00 USD |
| `7D` | `0.1203` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 70,770.00 USD | 29,250.00 USD | 6,320.00 USD |
| `1D` | `0.1205` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 2,250.00 USD | 1,670.00 USD | 745.16 USD |
| `7D` | `0.1205` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 86,480.00 USD | 48,720.00 USD | 128,320.00 USD |
| `1D` | `0.1207` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 5,540.00 USD | 524.23 USD | 2,590.00 USD |
| `7D` | `0.1207` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 12,460.00 USD | 19,400.00 USD | 53,940.00 USD |
| `1D` | `0.1209` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 2,450.00 USD | 2,550.00 USD | 2,240.00 USD |
| `7D` | `0.1209` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 85,160.00 USD | 19,340.00 USD | 94,170.00 USD |
| `1D` | `0.1211` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 4,800.00 USD | 2,950.00 USD | 3,240.00 USD |
| `7D` | `0.1211` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 27,400.00 USD | 16,260.00 USD | 29,770.00 USD |
| `1D` | `0.1213` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 1,550.00 USD | 1,220.00 USD | 10,400.00 USD |
| `7D` | `0.1213` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 23,920.00 USD | 26,740.00 USD | 24,130.00 USD |
| `1D` | `0.1215` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD | 4,220.00 USD |
| `7D` | `0.1215` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 5,900.00 USD | 6,620.00 USD | 59,130.00 USD |
| `1D` | `0.1217` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 1,090.00 USD | 624.33 USD | 5,110.00 USD |
| `7D` | `0.1217` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 18,490.00 USD | 23,600.00 USD | 11,080.00 USD |
| `1D` | `0.1219` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 2,320.00 USD | 718.82 USD | 10,030.00 USD |
| `7D` | `0.1219` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 26,700.00 USD | 5,500.00 USD | 38,020.00 USD |
| `1D` | `0.1221` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 4,680.00 USD | 2,940.00 USD | 3,670.00 USD |
| `7D` | `0.1221` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 47,890.00 USD | 21,770.00 USD | 18,890.00 USD |
| `1D` | `0.1223` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 2,660.00 USD | 1,410.00 USD | 4,210.00 USD |
| `7D` | `0.1223` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 103,180.00 USD | 36,290.00 USD | 48,450.00 USD |
| `1D` | `0.1225` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1225` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 43,040.00 USD | 19,970.00 USD | 5,260.00 USD |
| `1D` | `0.1227` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1227` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 65,240.00 USD | 31,790.00 USD | 55,660.00 USD |
| `1D` | `0.1229` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 403.62 USD | 1,080.00 USD |
| `7D` | `0.1229` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 63,350.00 USD | 34,190.00 USD | 40,620.00 USD |
| `1D` | `0.1231` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 430.11 USD | 809.11 USD |
| `7D` | `0.1231` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 25,460.00 USD | 29,380.00 USD | 27,570.00 USD |
| `1D` | `0.1233` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 1,250.00 USD | 2,750.00 USD | 0.04 USD |
| `7D` | `0.1233` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 57,130.00 USD | 13,020.00 USD | 40,130.00 USD |
| `1D` | `0.1235` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 1,570.00 USD | 575.54 USD | 3,370.00 USD |
| `7D` | `0.1235` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 10,950.00 USD | 6,400.00 USD | 8,950.00 USD |
| `1D` | `0.1237` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 1,560.00 USD | 0.00 USD |
| `7D` | `0.1237` | 5,910,000.00 USD | 5,910,000.00 USD | 0.00 USD | 4,080.00 USD | 9,720.00 USD | 2,890.00 USD |
| `1D` | `0.1239` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 4,900.00 USD | 724.40 USD | 587.65 USD |
| `7D` | `0.1239` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 8,780.00 USD | 1,270.00 USD | 479.13 USD |
| `1D` | `0.1241` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 2,790.00 USD | 1,830.00 USD | 4,310.00 USD |
| `7D` | `0.1241` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 6,830.00 USD | 9,690.00 USD | 2,400.00 USD |
| `1D` | `0.1243` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 1,660.00 USD | 4,600.00 USD | 7,510.00 USD |
| `7D` | `0.1243` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 11,450.00 USD | 4,530.00 USD | 4,670.00 USD |
| `1D` | `0.1245` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 6,600.00 USD | 3,420.00 USD | 5,500.00 USD |
| `7D` | `0.1245` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 26,080.00 USD | 11,090.00 USD | 12,970.00 USD |
| `1D` | `0.1247` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 2,580.00 USD | 1,320.00 USD | 4,730.00 USD |
| `7D` | `0.1247` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 24,470.00 USD | 19,030.00 USD | 9,710.00 USD |
| `7D` | `0.1249` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 13,440.00 USD | 5,480.00 USD | 5,660.00 USD |
| `7D` | `0.1251` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 7,660.00 USD | 5,070.00 USD | 11,040.00 USD |
| `7D` | `0.1253` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 11,420.00 USD | 2,100.00 USD | 14,010.00 USD |
| `7D` | `0.1255` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 2,250.00 USD | 13,990.00 USD | 33.04 USD |
| `7D` | `0.1257` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 15,610.00 USD | 5,200.00 USD | 54.64 USD |
| `7D` | `0.1259` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 288.60 USD |
| `7D` | `0.1261` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | 3,500.00 USD |
| `7D` | `0.1263` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,080.00 USD |
| `7D` | `0.1265` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 2,710.00 USD | 0.00 USD | 3,280.00 USD |
| `7D` | `0.1267` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,920.00 USD |
| `7D` | `0.1269` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16.21 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `72.86M` | Total OI Tokens: `660,913,316.6 OP`
  * 1h OI Change: `-0.83%` | 4h OI Change: `-3.11%` | 24h OI Change: `-6.08%`
  * Exchange Breakdown: Binance=`16.62M` | Bybit=`14.15M` | OKX=`4.16M` | Hyperliquid=`3.89M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `973.99` | Last 24h: `270.64` | Last 3d: `-2.23K` | Last 7d: `-15.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0034%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0017%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0033%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0193%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `43.33%` | `56.67%` | `0.76` | 1,470,000.00 USD |
| `15M` | `Binance` | `67.5%` | `32.5%` | `2.08` | 387,860.00 USD |
| `15M` | `OKX` | `68.68%` | `31.32%` | `2.19` | 150,800.00 USD |
| `15M` | `Bybit` | `63.33%` | `36.67%` | `1.73` | 93,490.00 USD |
| `15M` | `KuCoin` | `66.69%` | `33.31%` | `2.00` | 39,710.00 USD |
| `15M` | `Gate` | `57.9%` | `42.1%` | `1.38` | 18,930.00 USD |
| `15M` | `Bitget` | `64.35%` | `35.65%` | `1.81` | 19,660.00 USD |
| `15M` | `BingX` | `3.78%` | `96.22%` | `0.04` | 529,100.00 USD |
| `15M` | `MEXC` | `64.91%` | `35.09%` | `1.85` | 55,050.00 USD |
| `15M` | `Bitunix` | `66.23%` | `33.77%` | `1.96` | 11,850.00 USD |
| `15M` | `Hyperliquid` | `53.03%` | `46.97%` | `1.13` | 12,140.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `56.1%` | `43.9%` | `1.28` | 96,780.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `65.01%` | `34.99%` | `1.86` | 52,910.00 USD |
| `15M` | `HTX` | `100%` | `0%` | `1.00` | 0.60 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `99.28%` | `0.72%` | `137.89` | 4,570.00 USD |
| `15M` | `Aster` | `80.39%` | `19.61%` | `4.10` | 380.55 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `89.01%` | `10.99%` | `8.10` | 44.87 USD |
| `15M` | `Whale Positions` | `67.5%` | `32.5%` | `2.08` | 387,860.00 USD |
| `15M` | `Global Accounts` | `43.33%` | `56.67%` | `0.76` | 1,470,000.00 USD |
| `1H` | `OP` | `42.68%` | `57.32%` | `0.74` | 7,780,000.00 USD |
| `1H` | `Binance` | `42.47%` | `57.53%` | `0.74` | 2,730,000.00 USD |
| `1H` | `OKX` | `55.81%` | `44.19%` | `1.26` | 760,440.00 USD |
| `1H` | `Bybit` | `45.53%` | `54.47%` | `0.84` | 685,350.00 USD |
| `1H` | `KuCoin` | `49.65%` | `50.35%` | `0.99` | 497,650.00 USD |
| `1H` | `Gate` | `59.64%` | `40.36%` | `1.48` | 109,780.00 USD |
| `1H` | `Bitget` | `31.6%` | `68.4%` | `0.46` | 238,780.00 USD |
| `1H` | `BingX` | `7.47%` | `92.53%` | `0.08` | 1,210,000.00 USD |
| `1H` | `MEXC` | `62.95%` | `37.05%` | `1.70` | 497,120.00 USD |
| `1H` | `Bitunix` | `57.34%` | `42.66%` | `1.34` | 103,180.00 USD |
| `1H` | `Hyperliquid` | `27.84%` | `72.16%` | `0.39` | 107,090.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.35%` | `46.65%` | `1.14` | 350,880.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `61.01%` | `38.99%` | `1.56` | 243,850.00 USD |
| `1H` | `HTX` | `89.02%` | `10.98%` | `8.11` | 1,450.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `84.22%` | `15.78%` | `5.34` | 243,330.00 USD |
| `1H` | `Aster` | `19.81%` | `80.19%` | `0.25` | 2,060.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `86.81%` | `13.19%` | `6.58` | 2,000.00 USD |
| `1H` | `Whale Positions` | `42.47%` | `57.53%` | `0.74` | 2,730,000.00 USD |
| `1H` | `Global Accounts` | `42.68%` | `57.32%` | `0.74` | 7,780,000.00 USD |
| `4H` | `OP` | `43.39%` | `56.61%` | `0.77` | 33,000,000.00 USD |
| `4H` | `Binance` | `43.42%` | `56.58%` | `0.77` | 12,670,000.00 USD |
| `4H` | `OKX` | `47.76%` | `52.24%` | `0.91` | 3,810,000.00 USD |
| `4H` | `Bybit` | `44.44%` | `55.56%` | `0.80` | 3,610,000.00 USD |
| `4H` | `KuCoin` | `49.78%` | `50.22%` | `0.99` | 2,510,000.00 USD |
| `4H` | `Gate` | `49.74%` | `50.26%` | `0.99` | 510,400.00 USD |
| `4H` | `Bitget` | `33.63%` | `66.37%` | `0.51` | 899,950.00 USD |
| `4H` | `BingX` | `23.33%` | `76.67%` | `0.30` | 2,740,000.00 USD |
| `4H` | `MEXC` | `40.13%` | `59.87%` | `0.67` | 2,510,000.00 USD |
| `4H` | `Bitunix` | `41.93%` | `58.07%` | `0.72` | 569,490.00 USD |
| `4H` | `Hyperliquid` | `55.57%` | `44.43%` | `1.25` | 606,440.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.55%` | `49.45%` | `1.02` | 1,230,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `49.35%` | `50.65%` | `0.97` | 1,010,000.00 USD |
| `4H` | `HTX` | `89.76%` | `10.24%` | `8.77` | 7,150.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `76.38%` | `23.62%` | `3.23` | 298,640.00 USD |
| `4H` | `Aster` | `31.61%` | `68.39%` | `0.46` | 13,250.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `78.73%` | `21.27%` | `3.70` | 9,060.00 USD |
| `4H` | `Whale Positions` | `43.42%` | `56.58%` | `0.77` | 12,670,000.00 USD |
| `4H` | `Global Accounts` | `43.39%` | `56.61%` | `0.77` | 33,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1128` | `0.1128` | `0.1128` | `0.1130` | `0.1127` | 243,648.48 USD | 108,202.11 USD | 135,446.38 USD | -27,244.27 USD | `-11.18%` | `2B / 9S` |
| `0:00 UTC` | `0.1126` | `0.1127` | `0.1126` | `0.1132` | `0.1123` | 269,778.58 USD | 124,825.75 USD | 144,952.84 USD | -20,127.09 USD | `-7.46%` | `11B / 20S` |
| `5:00 UTC` | `0.1123` | `0.1122` | `0.1123` | `0.1124` | `0.1119` | 385,611.74 USD | 157,293.82 USD | 228,317.92 USD | -71,024.10 USD | `-18.42%` | `5B / 10S` |
| `0:00 UTC` | `0.1114` | `0.1117` | `0.1114` | `0.1124` | `0.1110` | 525,538.44 USD | 243,812.31 USD | 281,726.13 USD | -37,913.82 USD | `-7.21%` | `25B / 41S` |
| `5:00 UTC` | `0.1107` | `0.1107` | `0.1107` | `0.1112` | `0.1101` | 919,895.36 USD | 440,104.81 USD | 479,790.55 USD | -39,685.74 USD | `-4.31%` | `22B / 21S` |
| `0:00 UTC` | `0.1113` | `0.1110` | `0.1113` | `0.1113` | `0.1106` | 261,230.00 USD | 123,873.54 USD | 137,356.46 USD | -13,482.93 USD | `-5.16%` | `17B / 9S` |
| `5:00 UTC` | `0.1108` | `0.1106` | `0.1108` | `0.1112` | `0.1101` | 266,281.73 USD | 113,817.33 USD | 152,464.41 USD | -38,647.08 USD | `-14.51%` | `15B / 30S` |
| `0:00 UTC` | `0.1097` | `0.1098` | `0.1097` | `0.1103` | `0.1094` | 698,148.28 USD | 345,564.95 USD | 352,583.33 USD | -7,018.38 USD | `-1.01%` | `13B / 19S` |
| `5:00 UTC` | `0.1102` | `0.1100` | `0.1102` | `0.1104` | `0.1095` | 273,714.46 USD | 165,910.77 USD | 107,803.69 USD | 58,107.08 USD | `+21.23%` | `25B / 9S` |
| `0:00 UTC` | `0.1099` | `0.1099` | `0.1099` | `0.1101` | `0.1097` | 37,108.59 USD | 16,264.63 USD | 20,843.96 USD | -4,579.33 USD | `-12.34%` | `10B / 10S` |

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
| `5m` | -1,350.00 USD | -19,920.00 USD | **`DISTRIBUTION`** |
| `15m` | 13,470.00 USD | 71,230.00 USD | **`ACCUMULATION`** |
| `30m` | -907.28 USD | 140,240.00 USD | **`ACCUMULATION`** |
| `1h` | -10,000.00 USD | -52,530.00 USD | **`DISTRIBUTION`** |
| `2h` | -48,870.00 USD | -384,120.00 USD | **`DISTRIBUTION`** |
| `4h` | 7,020.00 USD | -359,360.00 USD | **`DISTRIBUTION`** |
| `6h` | 118,240.00 USD | 57,290.00 USD | **`ACCUMULATION`** |
| `8h` | 182,920.00 USD | 331,110.00 USD | **`ACCUMULATION`** |
| `12h` | 196,710.00 USD | 771,710.00 USD | **`ACCUMULATION`** |
| `24h` | 57,330.00 USD | -1,380,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -110,170.00 USD | -9,590,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,460,000.00 USD | -78,690,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.35K` | 15m=`+13.47K` | 1h=`-10.00K` | 24h=`+57.33K`
* Futures Capital Netflows: 5m=`-19.92K` | 15m=`+71.23K` | 1h=`-52.53K` | 24h=`-1.38M`
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
  * `2026-10-30 00:17:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:29:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
