# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-29 22:45:59 IST` (`2026-10-29 17:15:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1129` | `0.1132` | `0.1128` | `0.1130` | `761,689` | 86,031.08 USD | 3,576.83 USD | `+4.16%` | -522,149.15 USD | `+0.18` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.1130` | `0.1130` | `0.1125` | `0.1126` | `885,663` | 99,790.28 USD | -17,624.36 USD | `-17.66%` | -539,773.51 USD | `-0.26` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1126` | `0.1127` | `0.1124` | `0.1126` | `530,003` | 59,639.83 USD | 1,283.75 USD | `+2.15%` | -538,489.75 USD | `+0.14` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1132` | `0.1135` | `0.1126` | `0.1130` | `6,020,436` | 680,945.05 USD | -207,333.38 USD | `-30.45%` | -498,481.71 USD | `-2.81` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1130` | `0.1130` | `0.1127` | `0.1129` | `2,159,370` | 243,648.48 USD | -27,244.27 USD | `-11.18%` | -525,725.97 USD | `-0.49` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1129` | `0.1132` | `0.1124` | `0.1126` | `2,177,355` | 245,461.18 USD | -12,763.78 USD | `-5.20%` | -538,489.75 USD | `-0.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1119` | `0.1141` | `0.1117` | `0.1139` | `17,968,115` | 2,030,636.79 USD | 9,855.25 USD | `+0.49%` | -531,384.47 USD | `+0.23` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1140` | `0.1148` | `0.1126` | `0.1129` | `21,471,756` | 2,437,488.22 USD | -123,745.56 USD | `-5.08%` | -655,130.03 USD | `-0.29` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1129` | `0.1132` | `0.1124` | `0.1126` | `2,177,355` | 245,461.18 USD | -12,763.78 USD | `-5.20%` | -667,893.81 USD | `+0.19` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,229,700.44 USD | `+0.64` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -888,444.84 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1124` | `0.1126` | `23,651,197` | 2,683,184.35 USD | -136,274.40 USD | `-5.08%` | -1,024,719.24 USD | `+0.06` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1131` | `0.1136` | `0.1072` | `0.1085` | `76,338,549` | 8,353,905.81 USD | -1,528,374.61 USD | `-18.30%` | -1,480,991.26 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1085` | `0.1106` | `0.1071` | `0.1076` | `47,048,931` | 5,111,570.05 USD | 108,567.99 USD | `+2.12%` | -1,372,423.27 USD | `+0.75` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,229,700.44 USD | `+0.64` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -888,444.84 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1124` | `0.1126` | `23,651,197` | 2,683,184.35 USD | -136,274.40 USD | `-5.08%` | -1,024,719.24 USD | `+0.06` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:44:58 IST` |

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
| `Live` | `Long Liquidation` | `0.0385` | 196.31 USD | 242,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0405` | 183.72 USD | 241,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0475` | 3,600.00 USD | 241,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 3,460.00 USD | 238,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 829.69 USD | 234,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 1,100.00 USD | 233,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 353.81 USD | 232,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 501.98 USD | 232,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 100.24 USD | 231,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 518.48 USD | 231,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 1,920.00 USD | 231,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 762.48 USD | 229,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 1,440.00 USD | 228,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 23,910.00 USD | 227,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 41,550.00 USD | 203,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,300.00 USD | 161,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 1,020.00 USD | 159,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 5,720.00 USD | 158,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 878.62 USD | 152,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 1,320.00 USD | 151,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 223.98 USD | 150,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 1,560.00 USD | 150,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 2,240.00 USD | 148,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 883.92 USD | 146,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,120.00 USD | 145,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 443.16 USD | 142,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 16,670.00 USD | 141,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 69,120.00 USD | 125,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 4,640.00 USD | 56,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 419.87 USD | 51,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 12,670.00 USD | 51,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 19,960.00 USD | 38,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 427.25 USD | 18,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1010` | 2,120,000.00 USD | 2,120,000.00 USD | 2,320.00 USD | 2,960.00 USD | 1,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1010` | 2,120,000.00 USD | 2,120,000.00 USD | 2,320.00 USD | 2,960.00 USD | 1,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1012` | 2,110,000.00 USD | 2,110,000.00 USD | 1,570.00 USD | 1,430.00 USD | 997.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1012` | 2,110,000.00 USD | 2,110,000.00 USD | 1,570.00 USD | 1,430.00 USD | 997.22 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1014` | 2,110,000.00 USD | 2,110,000.00 USD | 6,000.00 USD | 2,550.00 USD | 608.26 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1014` | 2,110,000.00 USD | 2,110,000.00 USD | 6,000.00 USD | 2,550.00 USD | 608.26 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1015` | 622.37 USD | 17,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1016` | 2,100,000.00 USD | 2,100,000.00 USD | 3,360.00 USD | 2,540.00 USD | 8,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1016` | 2,100,000.00 USD | 2,100,000.00 USD | 3,360.00 USD | 2,540.00 USD | 8,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1018` | 2,080,000.00 USD | 2,080,000.00 USD | 827.81 USD | 4,170.00 USD | 7,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1018` | 2,080,000.00 USD | 2,080,000.00 USD | 827.81 USD | 4,170.00 USD | 7,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1020` | 2,070,000.00 USD | 2,070,000.00 USD | 6,440.00 USD | 2,630.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1020` | 2,070,000.00 USD | 2,070,000.00 USD | 6,440.00 USD | 2,630.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1022` | 2,060,000.00 USD | 2,060,000.00 USD | 5,070.00 USD | 2,120.00 USD | 7,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1022` | 2,060,000.00 USD | 2,060,000.00 USD | 5,070.00 USD | 2,120.00 USD | 7,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1024` | 2,050,000.00 USD | 2,050,000.00 USD | 2,300.00 USD | 947.50 USD | 4,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1024` | 2,050,000.00 USD | 2,050,000.00 USD | 2,300.00 USD | 947.50 USD | 4,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1025` | 17,360.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1026` | 2,040,000.00 USD | 2,040,000.00 USD | 2,780.00 USD | 2,210.00 USD | 2,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1026` | 2,040,000.00 USD | 2,040,000.00 USD | 2,780.00 USD | 2,210.00 USD | 2,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1028` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 936.16 USD | 156.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1028` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 936.16 USD | 156.11 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1030` | 2,030,000.00 USD | 2,030,000.00 USD | 8,870.00 USD | 3,480.00 USD | 10,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1030` | 2,030,000.00 USD | 2,030,000.00 USD | 8,870.00 USD | 3,480.00 USD | 10,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1032` | 2,010,000.00 USD | 2,010,000.00 USD | 11,310.00 USD | 2,260.00 USD | 5,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1032` | 2,010,000.00 USD | 2,010,000.00 USD | 11,310.00 USD | 2,260.00 USD | 5,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1034` | 1,990,000.00 USD | 1,990,000.00 USD | 7,190.00 USD | 5,040.00 USD | 11,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1034` | 1,990,000.00 USD | 1,990,000.00 USD | 7,190.00 USD | 5,040.00 USD | 11,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1036` | 1,960,000.00 USD | 1,960,000.00 USD | 4,780.00 USD | 7,340.00 USD | 12,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1036` | 1,960,000.00 USD | 1,960,000.00 USD | 4,780.00 USD | 7,340.00 USD | 12,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1038` | 1,940,000.00 USD | 1,940,000.00 USD | 4,190.00 USD | 9,130.00 USD | 12,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1038` | 1,940,000.00 USD | 1,940,000.00 USD | 4,190.00 USD | 9,130.00 USD | 12,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1040` | 1,910,000.00 USD | 1,910,000.00 USD | 2,980.00 USD | 4,600.00 USD | 12,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1040` | 1,910,000.00 USD | 1,910,000.00 USD | 2,980.00 USD | 4,600.00 USD | 12,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1042` | 1,890,000.00 USD | 1,890,000.00 USD | 23,250.00 USD | 5,430.00 USD | 12,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1042` | 1,890,000.00 USD | 1,890,000.00 USD | 23,250.00 USD | 5,430.00 USD | 12,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1044` | 1,850,000.00 USD | 1,850,000.00 USD | 917.34 USD | 6,870.00 USD | 1,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1044` | 1,850,000.00 USD | 1,850,000.00 USD | 917.34 USD | 6,870.00 USD | 1,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1046` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 1,080.00 USD | 8,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1046` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 1,080.00 USD | 8,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1048` | 1,830,000.00 USD | 1,830,000.00 USD | 8,130.00 USD | 3,110.00 USD | 20,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1048` | 1,830,000.00 USD | 1,830,000.00 USD | 8,130.00 USD | 3,110.00 USD | 20,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1050` | 1,800,000.00 USD | 1,800,000.00 USD | 19,000.00 USD | 3,360.00 USD | 10,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1050` | 1,800,000.00 USD | 1,800,000.00 USD | 19,000.00 USD | 3,360.00 USD | 10,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1052` | 1,770,000.00 USD | 1,770,000.00 USD | 24,810.00 USD | 12,260.00 USD | 34,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1052` | 1,770,000.00 USD | 1,770,000.00 USD | 24,810.00 USD | 12,260.00 USD | 34,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1054` | 1,700,000.00 USD | 1,700,000.00 USD | 39,370.00 USD | 13,660.00 USD | 41,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1054` | 1,700,000.00 USD | 1,700,000.00 USD | 39,370.00 USD | 13,660.00 USD | 41,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1056` | 1,600,000.00 USD | 1,600,000.00 USD | 24,440.00 USD | 25,480.00 USD | 37,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1056` | 1,600,000.00 USD | 1,600,000.00 USD | 24,440.00 USD | 25,480.00 USD | 37,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1058` | 1,520,000.00 USD | 1,520,000.00 USD | 7,800.00 USD | 29,030.00 USD | 41,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1058` | 1,520,000.00 USD | 1,520,000.00 USD | 7,800.00 USD | 29,030.00 USD | 41,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1060` | 1,440,000.00 USD | 1,440,000.00 USD | 20,300.00 USD | 6,110.00 USD | 45,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1060` | 1,440,000.00 USD | 1,440,000.00 USD | 20,300.00 USD | 6,110.00 USD | 45,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1062` | 1,370,000.00 USD | 1,370,000.00 USD | 24,460.00 USD | 16,630.00 USD | 47,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1062` | 1,370,000.00 USD | 1,370,000.00 USD | 24,460.00 USD | 16,630.00 USD | 47,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1064` | 1,280,000.00 USD | 1,280,000.00 USD | 45,250.00 USD | 15,310.00 USD | 45,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1064` | 1,280,000.00 USD | 1,280,000.00 USD | 45,250.00 USD | 15,310.00 USD | 45,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1066` | 1,170,000.00 USD | 1,170,000.00 USD | 6,400.00 USD | 14,190.00 USD | 8,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1066` | 1,170,000.00 USD | 1,170,000.00 USD | 6,400.00 USD | 14,190.00 USD | 8,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1068` | 1,140,000.00 USD | 1,140,000.00 USD | 18,290.00 USD | 6,750.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1068` | 1,140,000.00 USD | 1,140,000.00 USD | 18,290.00 USD | 6,750.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1070` | 1,090,000.00 USD | 1,090,000.00 USD | 22,800.00 USD | 6,210.00 USD | 43,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1070` | 1,090,000.00 USD | 1,090,000.00 USD | 22,800.00 USD | 6,210.00 USD | 43,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1072` | 1,020,000.00 USD | 1,020,000.00 USD | 38,000.00 USD | 3,780.00 USD | 14,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1072` | 1,020,000.00 USD | 1,020,000.00 USD | 38,000.00 USD | 3,780.00 USD | 14,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1074` | 959,230.00 USD | 959,230.00 USD | 11,270.00 USD | 12,510.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1074` | 959,230.00 USD | 959,230.00 USD | 11,270.00 USD | 12,510.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1076` | 928,880.00 USD | 928,880.00 USD | 11,080.00 USD | 7,340.00 USD | 10,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1076` | 928,880.00 USD | 928,880.00 USD | 11,080.00 USD | 7,340.00 USD | 10,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1078` | 899,570.00 USD | 899,570.00 USD | 12,550.00 USD | 15,090.00 USD | 23,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1078` | 899,570.00 USD | 899,570.00 USD | 12,550.00 USD | 15,090.00 USD | 23,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1080` | 848,200.00 USD | 848,200.00 USD | 5,850.00 USD | 4,200.00 USD | 33,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1080` | 848,200.00 USD | 848,200.00 USD | 5,850.00 USD | 4,200.00 USD | 33,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1082` | 804,340.00 USD | 804,340.00 USD | 18,610.00 USD | 9,540.00 USD | 35,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1082` | 804,340.00 USD | 804,340.00 USD | 18,610.00 USD | 9,540.00 USD | 35,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1084` | 741,160.00 USD | 741,160.00 USD | 31,060.00 USD | 10,630.00 USD | 42,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1084` | 741,160.00 USD | 741,160.00 USD | 31,060.00 USD | 10,630.00 USD | 42,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1086` | 656,630.00 USD | 656,630.00 USD | 19,870.00 USD | 8,030.00 USD | 67,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1086` | 656,630.00 USD | 656,630.00 USD | 19,870.00 USD | 8,030.00 USD | 67,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1088` | 560,900.00 USD | 560,900.00 USD | 28,110.00 USD | 8,890.00 USD | 12,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1088` | 560,900.00 USD | 560,900.00 USD | 28,110.00 USD | 8,890.00 USD | 12,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1090` | 511,360.00 USD | 511,360.00 USD | 40,320.00 USD | 6,400.00 USD | 12,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1090` | 511,360.00 USD | 511,360.00 USD | 40,320.00 USD | 6,400.00 USD | 12,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1092` | 451,980.00 USD | 451,980.00 USD | 10,290.00 USD | 4,610.00 USD | 5,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1092` | 451,980.00 USD | 451,980.00 USD | 10,290.00 USD | 4,610.00 USD | 5,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1094` | 431,380.00 USD | 431,380.00 USD | 13,100.00 USD | 3,890.00 USD | 10,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1094` | 431,380.00 USD | 431,380.00 USD | 13,100.00 USD | 3,890.00 USD | 10,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1098` | 403,490.00 USD | 403,490.00 USD | 9,980.00 USD | 1,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1098` | 403,490.00 USD | 403,490.00 USD | 9,980.00 USD | 1,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1100` | 391,880.00 USD | 391,880.00 USD | 0.00 USD | 9,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1100` | 391,880.00 USD | 391,880.00 USD | 0.00 USD | 9,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1102` | 382,680.00 USD | 382,680.00 USD | 0.00 USD | 0.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1102` | 382,680.00 USD | 382,680.00 USD | 0.00 USD | 0.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1104` | 378,130.00 USD | 378,130.00 USD | 20,640.00 USD | 10,880.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1104` | 378,130.00 USD | 378,130.00 USD | 20,640.00 USD | 10,880.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1106` | 340,530.00 USD | 340,530.00 USD | 4,910.00 USD | 12,720.00 USD | 27,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1106` | 340,530.00 USD | 340,530.00 USD | 4,910.00 USD | 12,720.00 USD | 27,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1108` | 295,550.00 USD | 295,550.00 USD | 0.00 USD | 0.00 USD | 28,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1108` | 295,550.00 USD | 295,550.00 USD | 0.00 USD | 0.00 USD | 28,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1110` | 266,790.00 USD | 266,790.00 USD | 27,290.00 USD | 0.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1110` | 266,790.00 USD | 266,790.00 USD | 27,290.00 USD | 0.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1112` | 236,300.00 USD | 236,300.00 USD | 3,660.00 USD | 0.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1112` | 236,300.00 USD | 236,300.00 USD | 3,660.00 USD | 0.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1114` | 221,620.00 USD | 221,620.00 USD | 15,810.00 USD | 3,630.00 USD | 30,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1114` | 221,620.00 USD | 221,620.00 USD | 15,810.00 USD | 3,630.00 USD | 30,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1116` | 171,280.00 USD | 171,280.00 USD | 4,760.00 USD | 12,080.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1116` | 171,280.00 USD | 171,280.00 USD | 4,760.00 USD | 12,080.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1118` | 149,880.00 USD | 149,880.00 USD | 16,250.00 USD | 17,620.00 USD | 32,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1118` | 149,880.00 USD | 149,880.00 USD | 16,250.00 USD | 17,620.00 USD | 32,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1120` | 83,800.00 USD | 83,800.00 USD | 0.00 USD | 0.00 USD | 36,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1120` | 83,800.00 USD | 83,800.00 USD | 0.00 USD | 0.00 USD | 36,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1122` | 47,240.00 USD | 47,240.00 USD | 21,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1122` | 47,240.00 USD | 47,240.00 USD | 21,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1124` | 25,480.00 USD | 25,480.00 USD | 7,700.00 USD | 17,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1124` | 25,480.00 USD | 25,480.00 USD | 7,700.00 USD | 17,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1126` | 7,060.00 USD | 7,060.00 USD | 0.00 USD | 7,040.00 USD | 26.51 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1126` | 14,120.00 USD | 14,120.00 USD | 0.00 USD | 7,040.00 USD | 26.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1126` | 7,060.00 USD | 7,060.00 USD | 0.00 USD | 7,040.00 USD | 26.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1126` | 14,120.00 USD | 14,120.00 USD | 0.00 USD | 7,040.00 USD | 26.51 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1130` | 14,170.00 USD | 14,170.00 USD | 0.00 USD | 0.00 USD | 49.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1130` | 14,170.00 USD | 14,170.00 USD | 0.00 USD | 0.00 USD | 49.34 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1132` | 31,490.00 USD | 31,490.00 USD | 0.00 USD | 17,300.00 USD | 18.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1132` | 31,490.00 USD | 31,490.00 USD | 0.00 USD | 17,300.00 USD | 18.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1134` | 38,960.00 USD | 38,960.00 USD | 0.00 USD | 7,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1134` | 38,960.00 USD | 38,960.00 USD | 0.00 USD | 7,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1136` | 39,010.00 USD | 39,010.00 USD | 0.00 USD | 0.00 USD | 40.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1136` | 39,010.00 USD | 39,010.00 USD | 0.00 USD | 0.00 USD | 40.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1138` | 48,710.00 USD | 48,710.00 USD | 0.00 USD | 856.93 USD | 8,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1138` | 48,710.00 USD | 48,710.00 USD | 0.00 USD | 856.93 USD | 8,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1140` | 51,440.00 USD | 51,440.00 USD | 2,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1140` | 51,440.00 USD | 51,440.00 USD | 2,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1142` | 83,420.00 USD | 83,420.00 USD | 16,040.00 USD | 9,210.00 USD | 6,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1142` | 83,420.00 USD | 83,420.00 USD | 16,040.00 USD | 9,210.00 USD | 6,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1144` | 137,080.00 USD | 137,080.00 USD | 9,940.00 USD | 20,430.00 USD | 23,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1144` | 137,080.00 USD | 137,080.00 USD | 9,940.00 USD | 20,430.00 USD | 23,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1146` | 168,810.00 USD | 168,810.00 USD | 0.00 USD | 4,690.00 USD | 27,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1146` | 168,810.00 USD | 168,810.00 USD | 0.00 USD | 4,690.00 USD | 27,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1148` | 227,450.00 USD | 227,450.00 USD | 28,550.00 USD | 2,650.00 USD | 27,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1148` | 227,450.00 USD | 227,450.00 USD | 28,550.00 USD | 2,650.00 USD | 27,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1150` | 280,400.00 USD | 280,400.00 USD | 15,680.00 USD | 13,020.00 USD | 24,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1150` | 280,400.00 USD | 280,400.00 USD | 15,680.00 USD | 13,020.00 USD | 24,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1152` | 415,500.00 USD | 415,500.00 USD | 36,300.00 USD | 16,730.00 USD | 82,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1152` | 415,500.00 USD | 415,500.00 USD | 36,300.00 USD | 16,730.00 USD | 82,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1154` | 509,880.00 USD | 509,880.00 USD | 18,640.00 USD | 29,020.00 USD | 46,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1154` | 509,880.00 USD | 509,880.00 USD | 18,640.00 USD | 29,020.00 USD | 46,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1156` | 611,440.00 USD | 611,440.00 USD | 56,620.00 USD | 18,720.00 USD | 26,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1156` | 611,440.00 USD | 611,440.00 USD | 56,620.00 USD | 18,720.00 USD | 26,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1158` | 689,560.00 USD | 689,560.00 USD | 26,730.00 USD | 9,500.00 USD | 41,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1158` | 689,560.00 USD | 689,560.00 USD | 26,730.00 USD | 9,500.00 USD | 41,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1160` | 757,760.00 USD | 757,760.00 USD | 34,710.00 USD | 6,890.00 USD | 26,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1160` | 757,760.00 USD | 757,760.00 USD | 34,710.00 USD | 6,890.00 USD | 26,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1162` | 805,910.00 USD | 805,910.00 USD | 15,950.00 USD | 13,530.00 USD | 18,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1162` | 805,910.00 USD | 805,910.00 USD | 15,950.00 USD | 13,530.00 USD | 18,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1164` | 856,090.00 USD | 856,090.00 USD | 20,480.00 USD | 13,180.00 USD | 16,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1164` | 856,090.00 USD | 856,090.00 USD | 20,480.00 USD | 13,180.00 USD | 16,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1166` | 883,920.00 USD | 883,920.00 USD | 17,960.00 USD | 9,820.00 USD | 40.24 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1166` | 883,920.00 USD | 883,920.00 USD | 17,960.00 USD | 9,820.00 USD | 40.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1168` | 918,480.00 USD | 918,480.00 USD | 13,800.00 USD | 15,460.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1168` | 918,480.00 USD | 918,480.00 USD | 13,800.00 USD | 15,460.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1170` | 961,340.00 USD | 961,340.00 USD | 18,140.00 USD | 5,800.00 USD | 18,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1170` | 961,340.00 USD | 961,340.00 USD | 18,140.00 USD | 5,800.00 USD | 18,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1172` | 986,160.00 USD | 986,160.00 USD | 13,700.00 USD | 9,550.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1172` | 986,160.00 USD | 986,160.00 USD | 13,700.00 USD | 9,550.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1174` | 1,030,000.00 USD | 1,030,000.00 USD | 13,180.00 USD | 6,360.00 USD | 26,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1174` | 1,030,000.00 USD | 1,030,000.00 USD | 13,180.00 USD | 6,360.00 USD | 26,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1176` | 1,070,000.00 USD | 1,070,000.00 USD | 6,120.00 USD | 16,060.00 USD | 20,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1176` | 1,070,000.00 USD | 1,070,000.00 USD | 6,120.00 USD | 16,060.00 USD | 20,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1178` | 1,120,000.00 USD | 1,120,000.00 USD | 27,500.00 USD | 7,760.00 USD | 7,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1178` | 1,120,000.00 USD | 1,120,000.00 USD | 27,500.00 USD | 7,760.00 USD | 7,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1180` | 1,160,000.00 USD | 1,160,000.00 USD | 15,510.00 USD | 4,770.00 USD | 24,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1180` | 1,160,000.00 USD | 1,160,000.00 USD | 15,510.00 USD | 4,770.00 USD | 24,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1182` | 1,190,000.00 USD | 1,190,000.00 USD | 15,060.00 USD | 3,740.00 USD | 13,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1182` | 1,190,000.00 USD | 1,190,000.00 USD | 15,060.00 USD | 3,740.00 USD | 13,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1184` | 1,210,000.00 USD | 1,210,000.00 USD | 7,750.00 USD | 3,320.00 USD | 10,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1184` | 1,210,000.00 USD | 1,210,000.00 USD | 7,750.00 USD | 3,320.00 USD | 10,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1186` | 1,250,000.00 USD | 1,250,000.00 USD | 10,390.00 USD | 8,770.00 USD | 11,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1186` | 1,250,000.00 USD | 1,250,000.00 USD | 10,390.00 USD | 8,770.00 USD | 11,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1188` | 1,260,000.00 USD | 1,260,000.00 USD | 4,660.00 USD | 7,610.00 USD | 4,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1188` | 1,260,000.00 USD | 1,260,000.00 USD | 4,660.00 USD | 7,610.00 USD | 4,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1190` | 1,280,000.00 USD | 1,280,000.00 USD | 5,250.00 USD | 5,740.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1190` | 1,280,000.00 USD | 1,280,000.00 USD | 5,250.00 USD | 5,740.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1192` | 1,290,000.00 USD | 1,290,000.00 USD | 7,250.00 USD | 1,990.00 USD | 7,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1192` | 1,290,000.00 USD | 1,290,000.00 USD | 7,250.00 USD | 1,990.00 USD | 7,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1194` | 1,300,000.00 USD | 1,300,000.00 USD | 6,310.00 USD | 1,390.00 USD | 2,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1194` | 1,300,000.00 USD | 1,300,000.00 USD | 6,310.00 USD | 1,390.00 USD | 2,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1196` | 1,310,000.00 USD | 1,310,000.00 USD | 3,240.00 USD | 2,860.00 USD | 64.58 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1196` | 1,310,000.00 USD | 1,310,000.00 USD | 3,240.00 USD | 2,860.00 USD | 64.58 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1198` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 3,660.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1198` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 3,660.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1200` | 1,320,000.00 USD | 1,320,000.00 USD | 1,840.00 USD | 1,050.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1200` | 1,320,000.00 USD | 1,320,000.00 USD | 1,840.00 USD | 1,050.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1202` | 1,340,000.00 USD | 1,340,000.00 USD | 10,280.00 USD | 460.32 USD | 4,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1202` | 1,340,000.00 USD | 1,340,000.00 USD | 10,280.00 USD | 460.32 USD | 4,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1204` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 769.98 USD | 1,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1204` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 769.98 USD | 1,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1206` | 1,350,000.00 USD | 1,350,000.00 USD | 3,340.00 USD | 2,440.00 USD | 3,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1206` | 1,350,000.00 USD | 1,350,000.00 USD | 3,340.00 USD | 2,440.00 USD | 3,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1208` | 1,360,000.00 USD | 1,360,000.00 USD | 4,380.00 USD | 1,770.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1208` | 1,360,000.00 USD | 1,360,000.00 USD | 4,380.00 USD | 1,770.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1210` | 1,370,000.00 USD | 1,370,000.00 USD | 3,980.00 USD | 4,240.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1210` | 1,370,000.00 USD | 1,370,000.00 USD | 3,980.00 USD | 4,240.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1212` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 1,360.00 USD | 7,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1212` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 1,360.00 USD | 7,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1214` | 1,390,000.00 USD | 1,390,000.00 USD | 4,020.00 USD | 820.70 USD | 7,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1214` | 1,390,000.00 USD | 1,390,000.00 USD | 4,020.00 USD | 820.70 USD | 7,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1216` | 1,400,000.00 USD | 1,400,000.00 USD | 1,330.00 USD | 0.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1216` | 1,400,000.00 USD | 1,400,000.00 USD | 1,330.00 USD | 0.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1218` | 1,410,000.00 USD | 1,410,000.00 USD | 1,550.00 USD | 624.33 USD | 8,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1218` | 1,410,000.00 USD | 1,410,000.00 USD | 1,550.00 USD | 624.33 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1220` | 1,420,000.00 USD | 1,420,000.00 USD | 769.06 USD | 2,350.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1220` | 1,420,000.00 USD | 1,420,000.00 USD | 769.06 USD | 2,350.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1222` | 1,430,000.00 USD | 1,430,000.00 USD | 2,980.00 USD | 2,630.00 USD | 3,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1222` | 1,430,000.00 USD | 1,430,000.00 USD | 2,980.00 USD | 2,630.00 USD | 3,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1224` | 1,430,000.00 USD | 1,430,000.00 USD | 2,660.00 USD | 558.39 USD | 3,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1224` | 1,430,000.00 USD | 1,430,000.00 USD | 2,660.00 USD | 558.39 USD | 3,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 16,000.00 USD | 16,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1228` | 1,430,000.00 USD | 1,430,000.00 USD | 1,970.00 USD | 0.00 USD | 1.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1228` | 1,430,000.00 USD | 1,430,000.00 USD | 1,970.00 USD | 0.00 USD | 1.91 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1230` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 403.62 USD | 789.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1230` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 403.62 USD | 789.22 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1232` | 1,440,000.00 USD | 1,440,000.00 USD | 1,250.00 USD | 1,270.00 USD | 4.12 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1232` | 1,440,000.00 USD | 1,440,000.00 USD | 1,250.00 USD | 1,270.00 USD | 4.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1234` | 1,440,000.00 USD | 1,440,000.00 USD | 1,070.00 USD | 2,120.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1234` | 1,440,000.00 USD | 1,440,000.00 USD | 1,070.00 USD | 2,120.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1236` | 1,450,000.00 USD | 1,450,000.00 USD | 1,570.00 USD | 1,430.00 USD | 911.21 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1236` | 1,450,000.00 USD | 1,450,000.00 USD | 1,570.00 USD | 1,430.00 USD | 911.21 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1238` | 1,450,000.00 USD | 1,450,000.00 USD | 3,120.00 USD | 724.40 USD | 587.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1238` | 1,450,000.00 USD | 1,450,000.00 USD | 3,120.00 USD | 724.40 USD | 587.32 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1240` | 1,460,000.00 USD | 1,460,000.00 USD | 2,890.00 USD | 1,830.00 USD | 8.83 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1240` | 1,460,000.00 USD | 1,460,000.00 USD | 2,890.00 USD | 1,830.00 USD | 8.83 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1242` | 1,470,000.00 USD | 1,470,000.00 USD | 3,360.00 USD | 2,540.00 USD | 8,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1242` | 1,470,000.00 USD | 1,470,000.00 USD | 3,360.00 USD | 2,540.00 USD | 8,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1244` | 1,480,000.00 USD | 1,480,000.00 USD | 827.81 USD | 4,170.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1244` | 1,480,000.00 USD | 1,480,000.00 USD | 827.81 USD | 4,170.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1246` | 1,490,000.00 USD | 1,490,000.00 USD | 6,440.00 USD | 2,630.00 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1246` | 1,490,000.00 USD | 1,490,000.00 USD | 6,440.00 USD | 2,630.00 USD | 2,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1248` | 1,500,000.00 USD | 1,500,000.00 USD | 1,910.00 USD | 0.00 USD | 4,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1248` | 1,500,000.00 USD | 1,500,000.00 USD | 1,910.00 USD | 0.00 USD | 4,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1250` | 1,510,000.00 USD | 1,510,000.00 USD | 3,160.00 USD | 2,120.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1250` | 1,510,000.00 USD | 1,510,000.00 USD | 3,160.00 USD | 2,120.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1252` | 1,520,000.00 USD | 1,520,000.00 USD | 2,300.00 USD | 947.50 USD | 4,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1252` | 1,520,000.00 USD | 1,520,000.00 USD | 2,300.00 USD | 947.50 USD | 4,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1254` | 1,520,000.00 USD | 1,520,000.00 USD | 2,780.00 USD | 2,210.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1254` | 1,520,000.00 USD | 1,520,000.00 USD | 2,780.00 USD | 2,210.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1256` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 936.16 USD | 27.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1256` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 936.16 USD | 27.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1258` | 1,530,000.00 USD | 1,530,000.00 USD | 2,100.00 USD | 1,690.00 USD | 12.41 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1258` | 1,530,000.00 USD | 1,530,000.00 USD | 2,100.00 USD | 1,690.00 USD | 12.41 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1260` | 1,530,000.00 USD | 1,530,000.00 USD | 1,010.00 USD | 0.00 USD | 5.73 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1260` | 1,530,000.00 USD | 1,530,000.00 USD | 1,010.00 USD | 0.00 USD | 5.73 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1262` | 1,530,000.00 USD | 1,530,000.00 USD | 1,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1262` | 1,530,000.00 USD | 1,530,000.00 USD | 1,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1264` | 1,530,000.00 USD | 1,530,000.00 USD | 1,300.00 USD | 694.78 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1264` | 1,530,000.00 USD | 1,530,000.00 USD | 1,300.00 USD | 694.78 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1355` | 1,330.00 USD | 17,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1515` | 15,150.00 USD | 32,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1555` | 6,210.00 USD | 38,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1565` | 550.61 USD | 39,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1645` | 19,830.00 USD | 59,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1695` | 169.25 USD | 59,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1865` | 167.85 USD | 59,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1915` | 925.65 USD | 60,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0385` | 242,040.00 USD | 0.00 USD | 196.31 USD | `-65.88%` | `5,098.90` |
| `Live` | `Long` | `0.0405` | 241,840.00 USD | 0.00 USD | 183.72 USD | `-64.11%` | `4,536.30` |
| `Live` | `Long` | `0.0475` | 241,660.00 USD | 0.00 USD | 3,600.00 USD | `-57.90%` | `75,790.10` |
| `Live` | `Long` | `0.0545` | 238,060.00 USD | 0.00 USD | 3,460.00 USD | `-51.70%` | `63,403.00` |
| `Live` | `Long` | `0.0575` | 234,600.00 USD | 0.00 USD | 829.69 USD | `-49.04%` | `14,429.40` |
| `Live` | `Long` | `0.0615` | 233,770.00 USD | 0.00 USD | 1,100.00 USD | `-45.50%` | `17,943.80` |
| `Live` | `Long` | `0.0645` | 232,670.00 USD | 0.00 USD | 353.81 USD | `-42.84%` | `5,485.40` |
| `Live` | `Long` | `0.0655` | 232,320.00 USD | 0.00 USD | 501.98 USD | `-41.95%` | `7,663.80` |
| `Live` | `Long` | `0.0665` | 231,810.00 USD | 0.00 USD | 100.24 USD | `-41.07%` | `1,507.30` |
| `Live` | `Long` | `0.0675` | 231,710.00 USD | 0.00 USD | 518.48 USD | `-40.18%` | `7,681.20` |
| `Live` | `Long` | `0.0685` | 231,190.00 USD | 0.00 USD | 1,920.00 USD | `-39.29%` | `28,000.00` |
| `Live` | `Long` | `0.0695` | 229,280.00 USD | 0.00 USD | 762.48 USD | `-38.41%` | `10,971.00` |
| `Live` | `Long` | `0.0715` | 228,510.00 USD | 0.00 USD | 1,440.00 USD | `-36.64%` | `20,133.00` |
| `Live` | `Long` | `0.0725` | 227,070.00 USD | 0.00 USD | 23,910.00 USD | `-35.75%` | `329,855.60` |
| `Live` | `Long` | `0.0735` | 203,160.00 USD | 0.00 USD | 41,550.00 USD | `-34.86%` | `565,287.50` |
| `Live` | `Long` | `0.0745` | 161,610.00 USD | 0.00 USD | 2,300.00 USD | `-33.98%` | `30,851.90` |
| `Live` | `Long` | `0.0755` | 159,310.00 USD | 0.00 USD | 1,020.00 USD | `-33.09%` | `13,481.90` |
| `Live` | `Long` | `0.0765` | 158,300.00 USD | 0.00 USD | 5,720.00 USD | `-32.20%` | `74,826.10` |
| `Live` | `Long` | `0.0775` | 152,570.00 USD | 0.00 USD | 878.62 USD | `-31.32%` | `11,337.00` |
| `Live` | `Long` | `0.0795` | 151,690.00 USD | 0.00 USD | 1,320.00 USD | `-29.55%` | `16,641.80` |
| `Live` | `Long` | `0.0805` | 150,370.00 USD | 0.00 USD | 223.98 USD | `-28.66%` | `2,782.40` |
| `Live` | `Long` | `0.0815` | 150,150.00 USD | 0.00 USD | 1,560.00 USD | `-27.77%` | `19,181.40` |
| `Live` | `Long` | `0.0825` | 148,580.00 USD | 0.00 USD | 2,240.00 USD | `-26.89%` | `27,146.60` |
| `Live` | `Long` | `0.0875` | 146,340.00 USD | 0.00 USD | 883.92 USD | `-22.46%` | `10,101.90` |
| `Live` | `Long` | `0.0895` | 145,460.00 USD | 0.00 USD | 3,120.00 USD | `-20.68%` | `34,873.20` |
| `Live` | `Long` | `0.0905` | 142,340.00 USD | 0.00 USD | 443.16 USD | `-19.80%` | `4,896.80` |
| `Live` | `Long` | `0.0925` | 141,890.00 USD | 0.00 USD | 16,670.00 USD | `-18.03%` | `180,203.00` |
| `Live` | `Long` | `0.0945` | 125,230.00 USD | 0.00 USD | 69,120.00 USD | `-16.25%` | `731,405.60` |
| `Live` | `Long` | `0.0955` | 56,110.00 USD | 0.00 USD | 4,640.00 USD | `-15.37%` | `48,598.80` |
| `Live` | `Long` | `0.0965` | 51,470.00 USD | 0.00 USD | 419.87 USD | `-14.48%` | `4,351.00` |
| `Live` | `Long` | `0.0975` | 51,050.00 USD | 0.00 USD | 12,670.00 USD | `-13.59%` | `129,987.90` |
| `Live` | `Long` | `0.0985` | 38,370.00 USD | 0.00 USD | 19,960.00 USD | `-12.71%` | `202,627.30` |
| `Live` | `Long` | `0.1005` | 18,410.00 USD | 0.00 USD | 427.25 USD | `-10.94%` | `4,251.20` |
| `Live` | `Long` | `0.1015` | 17,990.00 USD | 0.00 USD | 622.37 USD | `-10.05%` | `6,131.70` |
| `Live` | `Long` | `0.1025` | 17,360.00 USD | 0.00 USD | 17,360.00 USD | `-9.16%` | `169,408.50` |
| `Live` | `Short` | `0.1225` | 16,000.00 USD | 16,000.00 USD | 0.00 USD | `+8.56%` | `130,621.40` |
| `Live` | `Short` | `0.1355` | 17,330.00 USD | 1,330.00 USD | 0.00 USD | `+20.08%` | `9,843.80` |
| `Live` | `Short` | `0.1515` | 32,490.00 USD | 15,150.00 USD | 0.00 USD | `+34.26%` | `100,000.40` |
| `Live` | `Short` | `0.1555` | 38,690.00 USD | 6,210.00 USD | 0.00 USD | `+37.81%` | `39,929.50` |
| `Live` | `Short` | `0.1565` | 39,240.00 USD | 550.61 USD | 0.00 USD | `+38.69%` | `3,518.30` |
| `Live` | `Short` | `0.1645` | 59,080.00 USD | 19,830.00 USD | 0.00 USD | `+45.78%` | `120,571.30` |
| `Live` | `Short` | `0.1695` | 59,250.00 USD | 169.25 USD | 0.00 USD | `+50.21%` | `998.50` |
| `Live` | `Short` | `0.1865` | 59,420.00 USD | 167.85 USD | 0.00 USD | `+65.28%` | `900.00` |
| `Live` | `Short` | `0.1915` | 60,340.00 USD | 925.65 USD | 0.00 USD | `+69.71%` | `4,833.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0635` | 178,950.00 USD | 0.00 USD | 1,140.00 USD | `-43.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 177,810.00 USD | 0.00 USD | 773.46 USD | `-37.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 177,040.00 USD | 0.00 USD | 592.27 USD | `-36.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 176,440.00 USD | 0.00 USD | 755.00 USD | `-33.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0805` | 175,690.00 USD | 0.00 USD | 411.06 USD | `-28.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0815` | 175,280.00 USD | 0.00 USD | 183.49 USD | `-27.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0835` | 175,090.00 USD | 0.00 USD | 456.70 USD | `-26.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 174,640.00 USD | 0.00 USD | 631.58 USD | `-24.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 174,010.00 USD | 0.00 USD | 653.74 USD | `-21.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0915` | 173,350.00 USD | 0.00 USD | 1,460.00 USD | `-18.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 171,890.00 USD | 0.00 USD | 485.13 USD | `-16.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0975` | 171,400.00 USD | 0.00 USD | 720.22 USD | `-13.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0985` | 170,680.00 USD | 0.00 USD | 931.75 USD | `-12.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0995` | 169,750.00 USD | 0.00 USD | 801.64 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 168,950.00 USD | 0.00 USD | 1,470.00 USD | `-10.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1015` | 167,480.00 USD | 0.00 USD | 903.42 USD | `-10.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 166,570.00 USD | 0.00 USD | 780.70 USD | `-9.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1035` | 165,790.00 USD | 0.00 USD | 4,650.00 USD | `-8.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1045` | 161,140.00 USD | 0.00 USD | 18,950.00 USD | `-7.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1055` | 142,190.00 USD | 0.00 USD | 7,770.00 USD | `-6.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1065` | 134,420.00 USD | 0.00 USD | 109,280.00 USD | `-5.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 25,140.00 USD | 0.00 USD | 21,670.00 USD | `-4.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 3,480.00 USD | 0.00 USD | 150.04 USD | `-3.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1095` | 3,330.00 USD | 0.00 USD | 639.36 USD | `-2.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 2,690.00 USD | 0.00 USD | 162.59 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 2,520.00 USD | 0.00 USD | 839.64 USD | `-1.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1125` | 1,680.00 USD | 0.00 USD | 1,680.00 USD | `-0.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1135` | 116.27 USD | 116.27 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1145` | 250.88 USD | 134.61 USD | 0.00 USD | `+1.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 740.85 USD | 489.97 USD | 0.00 USD | `+2.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1165` | 1,210.00 USD | 466.94 USD | 0.00 USD | `+3.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1175` | 28,730.00 USD | 27,530.00 USD | 0.00 USD | `+4.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1185` | 29,790.00 USD | 1,050.00 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1195` | 44,420.00 USD | 14,640.00 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1205` | 44,820.00 USD | 398.42 USD | 0.00 USD | `+6.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1225` | 45,800.00 USD | 980.00 USD | 0.00 USD | `+8.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1235` | 58,780.00 USD | 12,980.00 USD | 0.00 USD | `+9.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1255` | 63,160.00 USD | 4,380.00 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1265` | 73,620.00 USD | 10,460.00 USD | 0.00 USD | `+12.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1275` | 74,110.00 USD | 492.06 USD | 0.00 USD | `+12.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1305` | 74,560.00 USD | 444.24 USD | 0.00 USD | `+15.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1315` | 106,120.00 USD | 31,560.00 USD | 0.00 USD | `+16.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1335` | 107,430.00 USD | 1,310.00 USD | 0.00 USD | `+18.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1345` | 111,580.00 USD | 4,150.00 USD | 0.00 USD | `+19.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1365` | 122,280.00 USD | 10,690.00 USD | 0.00 USD | `+20.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1405` | 135,380.00 USD | 13,110.00 USD | 0.00 USD | `+24.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1425` | 135,490.00 USD | 102.22 USD | 0.00 USD | `+26.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1435` | 142,660.00 USD | 7,180.00 USD | 0.00 USD | `+27.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1485` | 145,310.00 USD | 2,650.00 USD | 0.00 USD | `+31.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1495` | 146,100.00 USD | 792.53 USD | 0.00 USD | `+32.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1525` | 149,870.00 USD | 3,770.00 USD | 0.00 USD | `+35.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 150,050.00 USD | 184.49 USD | 0.00 USD | `+37.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 156,770.00 USD | 6,720.00 USD | 0.00 USD | `+38.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 156,990.00 USD | 219.81 USD | 0.00 USD | `+39.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 157,270.00 USD | 277.62 USD | 0.00 USD | `+44.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 159,060.00 USD | 1,800.00 USD | 0.00 USD | `+50.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 159,280.00 USD | 216.55 USD | 0.00 USD | `+54.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 159,400.00 USD | 117.26 USD | 0.00 USD | `+75.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 179,930.00 USD | 20,530.00 USD | 0.00 USD | `+77.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 180,130.00 USD | 201.02 USD | 0.00 USD | `+98.07%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.1010` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 2,320.00 USD | 2,960.00 USD | 1,260.00 USD |
| `7D` | `0.1010` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 2,320.00 USD | 2,960.00 USD | 1,260.00 USD |
| `1D` | `0.1012` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 1,570.00 USD | 1,430.00 USD | 997.22 USD |
| `7D` | `0.1012` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 1,570.00 USD | 1,430.00 USD | 997.22 USD |
| `1D` | `0.1014` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 6,000.00 USD | 2,550.00 USD | 608.26 USD |
| `7D` | `0.1014` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 6,000.00 USD | 2,550.00 USD | 608.26 USD |
| `1D` | `0.1016` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 3,360.00 USD | 2,540.00 USD | 8,260.00 USD |
| `7D` | `0.1016` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 3,360.00 USD | 2,540.00 USD | 8,260.00 USD |
| `1D` | `0.1018` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 827.81 USD | 4,170.00 USD | 7,380.00 USD |
| `7D` | `0.1018` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 827.81 USD | 4,170.00 USD | 7,380.00 USD |
| `1D` | `0.1020` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 6,440.00 USD | 2,630.00 USD | 2,020.00 USD |
| `7D` | `0.1020` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 6,440.00 USD | 2,630.00 USD | 2,020.00 USD |
| `1D` | `0.1022` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 5,070.00 USD | 2,120.00 USD | 7,230.00 USD |
| `7D` | `0.1022` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 5,070.00 USD | 2,120.00 USD | 7,230.00 USD |
| `1D` | `0.1024` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 2,300.00 USD | 947.50 USD | 4,710.00 USD |
| `7D` | `0.1024` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 2,300.00 USD | 947.50 USD | 4,710.00 USD |
| `1D` | `0.1026` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 2,780.00 USD | 2,210.00 USD | 2,520.00 USD |
| `7D` | `0.1026` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 2,780.00 USD | 2,210.00 USD | 2,520.00 USD |
| `1D` | `0.1028` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 0.00 USD | 936.16 USD | 156.11 USD |
| `7D` | `0.1028` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 0.00 USD | 936.16 USD | 156.11 USD |
| `1D` | `0.1030` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 8,870.00 USD | 3,480.00 USD | 10,440.00 USD |
| `7D` | `0.1030` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 8,870.00 USD | 3,480.00 USD | 10,440.00 USD |
| `1D` | `0.1032` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 11,310.00 USD | 2,260.00 USD | 5,440.00 USD |
| `7D` | `0.1032` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 11,310.00 USD | 2,260.00 USD | 5,440.00 USD |
| `1D` | `0.1034` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 7,190.00 USD | 5,040.00 USD | 11,050.00 USD |
| `7D` | `0.1034` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 7,190.00 USD | 5,040.00 USD | 11,050.00 USD |
| `1D` | `0.1036` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 4,780.00 USD | 7,340.00 USD | 12,360.00 USD |
| `7D` | `0.1036` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 4,780.00 USD | 7,340.00 USD | 12,360.00 USD |
| `1D` | `0.1038` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 4,190.00 USD | 9,130.00 USD | 12,700.00 USD |
| `7D` | `0.1038` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 4,190.00 USD | 9,130.00 USD | 12,700.00 USD |
| `1D` | `0.1040` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 2,980.00 USD | 4,600.00 USD | 12,810.00 USD |
| `7D` | `0.1040` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 2,980.00 USD | 4,600.00 USD | 12,810.00 USD |
| `1D` | `0.1042` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 23,250.00 USD | 5,430.00 USD | 12,640.00 USD |
| `7D` | `0.1042` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 23,250.00 USD | 5,430.00 USD | 12,640.00 USD |
| `1D` | `0.1044` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 917.34 USD | 6,870.00 USD | 1,250.00 USD |
| `7D` | `0.1044` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 917.34 USD | 6,870.00 USD | 1,250.00 USD |
| `1D` | `0.1046` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 0.00 USD | 1,080.00 USD | 8,710.00 USD |
| `7D` | `0.1046` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 0.00 USD | 1,080.00 USD | 8,710.00 USD |
| `1D` | `0.1048` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 8,130.00 USD | 3,110.00 USD | 20,170.00 USD |
| `7D` | `0.1048` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 8,130.00 USD | 3,110.00 USD | 20,170.00 USD |
| `1D` | `0.1050` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 19,000.00 USD | 3,360.00 USD | 10,710.00 USD |
| `7D` | `0.1050` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 19,000.00 USD | 3,360.00 USD | 10,710.00 USD |
| `1D` | `0.1052` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 24,810.00 USD | 12,260.00 USD | 34,110.00 USD |
| `7D` | `0.1052` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 24,810.00 USD | 12,260.00 USD | 34,110.00 USD |
| `1D` | `0.1054` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 39,370.00 USD | 13,660.00 USD | 41,450.00 USD |
| `7D` | `0.1054` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 39,370.00 USD | 13,660.00 USD | 41,450.00 USD |
| `1D` | `0.1056` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 24,440.00 USD | 25,480.00 USD | 37,750.00 USD |
| `7D` | `0.1056` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 24,440.00 USD | 25,480.00 USD | 37,750.00 USD |
| `1D` | `0.1058` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 7,800.00 USD | 29,030.00 USD | 41,030.00 USD |
| `7D` | `0.1058` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 7,800.00 USD | 29,030.00 USD | 41,030.00 USD |
| `1D` | `0.1060` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 20,300.00 USD | 6,110.00 USD | 45,140.00 USD |
| `7D` | `0.1060` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 20,300.00 USD | 6,110.00 USD | 45,140.00 USD |
| `1D` | `0.1062` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 24,460.00 USD | 16,630.00 USD | 47,680.00 USD |
| `7D` | `0.1062` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 24,460.00 USD | 16,630.00 USD | 47,680.00 USD |
| `1D` | `0.1064` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 45,250.00 USD | 15,310.00 USD | 45,130.00 USD |
| `7D` | `0.1064` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 45,250.00 USD | 15,310.00 USD | 45,130.00 USD |
| `1D` | `0.1066` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 6,400.00 USD | 14,190.00 USD | 8,970.00 USD |
| `7D` | `0.1066` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 6,400.00 USD | 14,190.00 USD | 8,970.00 USD |
| `1D` | `0.1068` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 18,290.00 USD | 6,750.00 USD | 29,600.00 USD |
| `7D` | `0.1068` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 18,290.00 USD | 6,750.00 USD | 29,600.00 USD |
| `1D` | `0.1070` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 22,800.00 USD | 6,210.00 USD | 43,290.00 USD |
| `7D` | `0.1070` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 22,800.00 USD | 6,210.00 USD | 43,290.00 USD |
| `1D` | `0.1072` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 38,000.00 USD | 3,780.00 USD | 14,360.00 USD |
| `7D` | `0.1072` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 38,000.00 USD | 3,780.00 USD | 14,360.00 USD |
| `1D` | `0.1074` | 959,230.00 USD | 0.00 USD | 959,230.00 USD | 11,270.00 USD | 12,510.00 USD | 6,570.00 USD |
| `7D` | `0.1074` | 959,230.00 USD | 0.00 USD | 959,230.00 USD | 11,270.00 USD | 12,510.00 USD | 6,570.00 USD |
| `1D` | `0.1076` | 928,880.00 USD | 0.00 USD | 928,880.00 USD | 11,080.00 USD | 7,340.00 USD | 10,890.00 USD |
| `7D` | `0.1076` | 928,880.00 USD | 0.00 USD | 928,880.00 USD | 11,080.00 USD | 7,340.00 USD | 10,890.00 USD |
| `1D` | `0.1078` | 899,570.00 USD | 0.00 USD | 899,570.00 USD | 12,550.00 USD | 15,090.00 USD | 23,730.00 USD |
| `7D` | `0.1078` | 899,570.00 USD | 0.00 USD | 899,570.00 USD | 12,550.00 USD | 15,090.00 USD | 23,730.00 USD |
| `1D` | `0.1080` | 848,200.00 USD | 0.00 USD | 848,200.00 USD | 5,850.00 USD | 4,200.00 USD | 33,810.00 USD |
| `7D` | `0.1080` | 848,200.00 USD | 0.00 USD | 848,200.00 USD | 5,850.00 USD | 4,200.00 USD | 33,810.00 USD |
| `1D` | `0.1082` | 804,340.00 USD | 0.00 USD | 804,340.00 USD | 18,610.00 USD | 9,540.00 USD | 35,030.00 USD |
| `7D` | `0.1082` | 804,340.00 USD | 0.00 USD | 804,340.00 USD | 18,610.00 USD | 9,540.00 USD | 35,030.00 USD |
| `1D` | `0.1084` | 741,160.00 USD | 0.00 USD | 741,160.00 USD | 31,060.00 USD | 10,630.00 USD | 42,830.00 USD |
| `7D` | `0.1084` | 741,160.00 USD | 0.00 USD | 741,160.00 USD | 31,060.00 USD | 10,630.00 USD | 42,830.00 USD |
| `1D` | `0.1086` | 656,630.00 USD | 0.00 USD | 656,630.00 USD | 19,870.00 USD | 8,030.00 USD | 67,840.00 USD |
| `7D` | `0.1086` | 656,630.00 USD | 0.00 USD | 656,630.00 USD | 19,870.00 USD | 8,030.00 USD | 67,840.00 USD |
| `1D` | `0.1088` | 560,900.00 USD | 0.00 USD | 560,900.00 USD | 28,110.00 USD | 8,890.00 USD | 12,520.00 USD |
| `7D` | `0.1088` | 560,900.00 USD | 0.00 USD | 560,900.00 USD | 28,110.00 USD | 8,890.00 USD | 12,520.00 USD |
| `1D` | `0.1090` | 511,360.00 USD | 0.00 USD | 511,360.00 USD | 40,320.00 USD | 6,400.00 USD | 12,670.00 USD |
| `7D` | `0.1090` | 511,360.00 USD | 0.00 USD | 511,360.00 USD | 40,320.00 USD | 6,400.00 USD | 12,670.00 USD |
| `1D` | `0.1092` | 451,980.00 USD | 0.00 USD | 451,980.00 USD | 10,290.00 USD | 4,610.00 USD | 5,700.00 USD |
| `7D` | `0.1092` | 451,980.00 USD | 0.00 USD | 451,980.00 USD | 10,290.00 USD | 4,610.00 USD | 5,700.00 USD |
| `1D` | `0.1094` | 431,380.00 USD | 0.00 USD | 431,380.00 USD | 13,100.00 USD | 3,890.00 USD | 10,900.00 USD |
| `7D` | `0.1094` | 431,380.00 USD | 0.00 USD | 431,380.00 USD | 13,100.00 USD | 3,890.00 USD | 10,900.00 USD |
| `1D` | `0.1098` | 403,490.00 USD | 0.00 USD | 403,490.00 USD | 9,980.00 USD | 1,630.00 USD | 0.00 USD |
| `7D` | `0.1098` | 403,490.00 USD | 0.00 USD | 403,490.00 USD | 9,980.00 USD | 1,630.00 USD | 0.00 USD |
| `1D` | `0.1100` | 391,880.00 USD | 0.00 USD | 391,880.00 USD | 0.00 USD | 9,190.00 USD | 0.00 USD |
| `7D` | `0.1100` | 391,880.00 USD | 0.00 USD | 391,880.00 USD | 0.00 USD | 9,190.00 USD | 0.00 USD |
| `1D` | `0.1102` | 382,680.00 USD | 0.00 USD | 382,680.00 USD | 0.00 USD | 0.00 USD | 4,560.00 USD |
| `7D` | `0.1102` | 382,680.00 USD | 0.00 USD | 382,680.00 USD | 0.00 USD | 0.00 USD | 4,560.00 USD |
| `1D` | `0.1104` | 378,130.00 USD | 0.00 USD | 378,130.00 USD | 20,640.00 USD | 10,880.00 USD | 6,070.00 USD |
| `7D` | `0.1104` | 378,130.00 USD | 0.00 USD | 378,130.00 USD | 20,640.00 USD | 10,880.00 USD | 6,070.00 USD |
| `1D` | `0.1106` | 340,530.00 USD | 0.00 USD | 340,530.00 USD | 4,910.00 USD | 12,720.00 USD | 27,360.00 USD |
| `7D` | `0.1106` | 340,530.00 USD | 0.00 USD | 340,530.00 USD | 4,910.00 USD | 12,720.00 USD | 27,360.00 USD |
| `1D` | `0.1108` | 295,550.00 USD | 0.00 USD | 295,550.00 USD | 0.00 USD | 0.00 USD | 28,750.00 USD |
| `7D` | `0.1108` | 295,550.00 USD | 0.00 USD | 295,550.00 USD | 0.00 USD | 0.00 USD | 28,750.00 USD |
| `1D` | `0.1110` | 266,790.00 USD | 0.00 USD | 266,790.00 USD | 27,290.00 USD | 0.00 USD | 3,200.00 USD |
| `7D` | `0.1110` | 266,790.00 USD | 0.00 USD | 266,790.00 USD | 27,290.00 USD | 0.00 USD | 3,200.00 USD |
| `1D` | `0.1112` | 236,300.00 USD | 0.00 USD | 236,300.00 USD | 3,660.00 USD | 0.00 USD | 11,030.00 USD |
| `7D` | `0.1112` | 236,300.00 USD | 0.00 USD | 236,300.00 USD | 3,660.00 USD | 0.00 USD | 11,030.00 USD |
| `1D` | `0.1114` | 221,620.00 USD | 0.00 USD | 221,620.00 USD | 15,810.00 USD | 3,630.00 USD | 30,900.00 USD |
| `7D` | `0.1114` | 221,620.00 USD | 0.00 USD | 221,620.00 USD | 15,810.00 USD | 3,630.00 USD | 30,900.00 USD |
| `1D` | `0.1116` | 171,280.00 USD | 0.00 USD | 171,280.00 USD | 4,760.00 USD | 12,080.00 USD | 4,540.00 USD |
| `7D` | `0.1116` | 171,280.00 USD | 0.00 USD | 171,280.00 USD | 4,760.00 USD | 12,080.00 USD | 4,540.00 USD |
| `1D` | `0.1118` | 149,880.00 USD | 0.00 USD | 149,880.00 USD | 16,250.00 USD | 17,620.00 USD | 32,220.00 USD |
| `7D` | `0.1118` | 149,880.00 USD | 0.00 USD | 149,880.00 USD | 16,250.00 USD | 17,620.00 USD | 32,220.00 USD |
| `1D` | `0.1120` | 83,800.00 USD | 0.00 USD | 83,800.00 USD | 0.00 USD | 0.00 USD | 36,560.00 USD |
| `7D` | `0.1120` | 83,800.00 USD | 0.00 USD | 83,800.00 USD | 0.00 USD | 0.00 USD | 36,560.00 USD |
| `1D` | `0.1122` | 47,240.00 USD | 0.00 USD | 47,240.00 USD | 21,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1122` | 47,240.00 USD | 0.00 USD | 47,240.00 USD | 21,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1124` | 25,480.00 USD | 0.00 USD | 25,480.00 USD | 7,700.00 USD | 17,780.00 USD | 0.00 USD |
| `7D` | `0.1124` | 25,480.00 USD | 0.00 USD | 25,480.00 USD | 7,700.00 USD | 17,780.00 USD | 0.00 USD |
| `1D` | `0.1126` | 7,060.00 USD | 7,060.00 USD | 0.00 USD | 0.00 USD | 7,040.00 USD | 26.51 USD |
| `1D` | `0.1126` | 14,120.00 USD | 14,120.00 USD | 0.00 USD | 0.00 USD | 7,040.00 USD | 26.51 USD |
| `7D` | `0.1126` | 7,060.00 USD | 7,060.00 USD | 0.00 USD | 0.00 USD | 7,040.00 USD | 26.51 USD |
| `7D` | `0.1126` | 14,120.00 USD | 14,120.00 USD | 0.00 USD | 0.00 USD | 7,040.00 USD | 26.51 USD |
| `1D` | `0.1130` | 14,170.00 USD | 14,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 49.34 USD |
| `7D` | `0.1130` | 14,170.00 USD | 14,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 49.34 USD |
| `1D` | `0.1132` | 31,490.00 USD | 31,490.00 USD | 0.00 USD | 0.00 USD | 17,300.00 USD | 18.72 USD |
| `7D` | `0.1132` | 31,490.00 USD | 31,490.00 USD | 0.00 USD | 0.00 USD | 17,300.00 USD | 18.72 USD |
| `1D` | `0.1134` | 38,960.00 USD | 38,960.00 USD | 0.00 USD | 0.00 USD | 7,470.00 USD | 0.00 USD |
| `7D` | `0.1134` | 38,960.00 USD | 38,960.00 USD | 0.00 USD | 0.00 USD | 7,470.00 USD | 0.00 USD |
| `1D` | `0.1136` | 39,010.00 USD | 39,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 40.44 USD |
| `7D` | `0.1136` | 39,010.00 USD | 39,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 40.44 USD |
| `1D` | `0.1138` | 48,710.00 USD | 48,710.00 USD | 0.00 USD | 0.00 USD | 856.93 USD | 8,850.00 USD |
| `7D` | `0.1138` | 48,710.00 USD | 48,710.00 USD | 0.00 USD | 0.00 USD | 856.93 USD | 8,850.00 USD |
| `1D` | `0.1140` | 51,440.00 USD | 51,440.00 USD | 0.00 USD | 2,720.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1140` | 51,440.00 USD | 51,440.00 USD | 0.00 USD | 2,720.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1142` | 83,420.00 USD | 83,420.00 USD | 0.00 USD | 16,040.00 USD | 9,210.00 USD | 6,740.00 USD |
| `7D` | `0.1142` | 83,420.00 USD | 83,420.00 USD | 0.00 USD | 16,040.00 USD | 9,210.00 USD | 6,740.00 USD |
| `1D` | `0.1144` | 137,080.00 USD | 137,080.00 USD | 0.00 USD | 9,940.00 USD | 20,430.00 USD | 23,280.00 USD |
| `7D` | `0.1144` | 137,080.00 USD | 137,080.00 USD | 0.00 USD | 9,940.00 USD | 20,430.00 USD | 23,280.00 USD |
| `1D` | `0.1146` | 168,810.00 USD | 168,810.00 USD | 0.00 USD | 0.00 USD | 4,690.00 USD | 27,040.00 USD |
| `7D` | `0.1146` | 168,810.00 USD | 168,810.00 USD | 0.00 USD | 0.00 USD | 4,690.00 USD | 27,040.00 USD |
| `1D` | `0.1148` | 227,450.00 USD | 227,450.00 USD | 0.00 USD | 28,550.00 USD | 2,650.00 USD | 27,430.00 USD |
| `7D` | `0.1148` | 227,450.00 USD | 227,450.00 USD | 0.00 USD | 28,550.00 USD | 2,650.00 USD | 27,430.00 USD |
| `1D` | `0.1150` | 280,400.00 USD | 280,400.00 USD | 0.00 USD | 15,680.00 USD | 13,020.00 USD | 24,250.00 USD |
| `7D` | `0.1150` | 280,400.00 USD | 280,400.00 USD | 0.00 USD | 15,680.00 USD | 13,020.00 USD | 24,250.00 USD |
| `1D` | `0.1152` | 415,500.00 USD | 415,500.00 USD | 0.00 USD | 36,300.00 USD | 16,730.00 USD | 82,070.00 USD |
| `7D` | `0.1152` | 415,500.00 USD | 415,500.00 USD | 0.00 USD | 36,300.00 USD | 16,730.00 USD | 82,070.00 USD |
| `1D` | `0.1154` | 509,880.00 USD | 509,880.00 USD | 0.00 USD | 18,640.00 USD | 29,020.00 USD | 46,730.00 USD |
| `7D` | `0.1154` | 509,880.00 USD | 509,880.00 USD | 0.00 USD | 18,640.00 USD | 29,020.00 USD | 46,730.00 USD |
| `1D` | `0.1156` | 611,440.00 USD | 611,440.00 USD | 0.00 USD | 56,620.00 USD | 18,720.00 USD | 26,220.00 USD |
| `7D` | `0.1156` | 611,440.00 USD | 611,440.00 USD | 0.00 USD | 56,620.00 USD | 18,720.00 USD | 26,220.00 USD |
| `1D` | `0.1158` | 689,560.00 USD | 689,560.00 USD | 0.00 USD | 26,730.00 USD | 9,500.00 USD | 41,900.00 USD |
| `7D` | `0.1158` | 689,560.00 USD | 689,560.00 USD | 0.00 USD | 26,730.00 USD | 9,500.00 USD | 41,900.00 USD |
| `1D` | `0.1160` | 757,760.00 USD | 757,760.00 USD | 0.00 USD | 34,710.00 USD | 6,890.00 USD | 26,590.00 USD |
| `7D` | `0.1160` | 757,760.00 USD | 757,760.00 USD | 0.00 USD | 34,710.00 USD | 6,890.00 USD | 26,590.00 USD |
| `1D` | `0.1162` | 805,910.00 USD | 805,910.00 USD | 0.00 USD | 15,950.00 USD | 13,530.00 USD | 18,670.00 USD |
| `7D` | `0.1162` | 805,910.00 USD | 805,910.00 USD | 0.00 USD | 15,950.00 USD | 13,530.00 USD | 18,670.00 USD |
| `1D` | `0.1164` | 856,090.00 USD | 856,090.00 USD | 0.00 USD | 20,480.00 USD | 13,180.00 USD | 16,530.00 USD |
| `7D` | `0.1164` | 856,090.00 USD | 856,090.00 USD | 0.00 USD | 20,480.00 USD | 13,180.00 USD | 16,530.00 USD |
| `1D` | `0.1166` | 883,920.00 USD | 883,920.00 USD | 0.00 USD | 17,960.00 USD | 9,820.00 USD | 40.24 USD |
| `7D` | `0.1166` | 883,920.00 USD | 883,920.00 USD | 0.00 USD | 17,960.00 USD | 9,820.00 USD | 40.24 USD |
| `1D` | `0.1168` | 918,480.00 USD | 918,480.00 USD | 0.00 USD | 13,800.00 USD | 15,460.00 USD | 5,300.00 USD |
| `7D` | `0.1168` | 918,480.00 USD | 918,480.00 USD | 0.00 USD | 13,800.00 USD | 15,460.00 USD | 5,300.00 USD |
| `1D` | `0.1170` | 961,340.00 USD | 961,340.00 USD | 0.00 USD | 18,140.00 USD | 5,800.00 USD | 18,930.00 USD |
| `7D` | `0.1170` | 961,340.00 USD | 961,340.00 USD | 0.00 USD | 18,140.00 USD | 5,800.00 USD | 18,930.00 USD |
| `1D` | `0.1172` | 986,160.00 USD | 986,160.00 USD | 0.00 USD | 13,700.00 USD | 9,550.00 USD | 1,570.00 USD |
| `7D` | `0.1172` | 986,160.00 USD | 986,160.00 USD | 0.00 USD | 13,700.00 USD | 9,550.00 USD | 1,570.00 USD |
| `1D` | `0.1174` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 13,180.00 USD | 6,360.00 USD | 26,280.00 USD |
| `7D` | `0.1174` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 13,180.00 USD | 6,360.00 USD | 26,280.00 USD |
| `1D` | `0.1176` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 6,120.00 USD | 16,060.00 USD | 20,130.00 USD |
| `7D` | `0.1176` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 6,120.00 USD | 16,060.00 USD | 20,130.00 USD |
| `1D` | `0.1178` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 27,500.00 USD | 7,760.00 USD | 7,000.00 USD |
| `7D` | `0.1178` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 27,500.00 USD | 7,760.00 USD | 7,000.00 USD |
| `1D` | `0.1180` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 15,510.00 USD | 4,770.00 USD | 24,300.00 USD |
| `7D` | `0.1180` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 15,510.00 USD | 4,770.00 USD | 24,300.00 USD |
| `1D` | `0.1182` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 15,060.00 USD | 3,740.00 USD | 13,280.00 USD |
| `7D` | `0.1182` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 15,060.00 USD | 3,740.00 USD | 13,280.00 USD |
| `1D` | `0.1184` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 7,750.00 USD | 3,320.00 USD | 10,270.00 USD |
| `7D` | `0.1184` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 7,750.00 USD | 3,320.00 USD | 10,270.00 USD |
| `1D` | `0.1186` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 10,390.00 USD | 8,770.00 USD | 11,840.00 USD |
| `7D` | `0.1186` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 10,390.00 USD | 8,770.00 USD | 11,840.00 USD |
| `1D` | `0.1188` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 4,660.00 USD | 7,610.00 USD | 4,640.00 USD |
| `7D` | `0.1188` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 4,660.00 USD | 7,610.00 USD | 4,640.00 USD |
| `1D` | `0.1190` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 5,250.00 USD | 5,740.00 USD | 2,780.00 USD |
| `7D` | `0.1190` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 5,250.00 USD | 5,740.00 USD | 2,780.00 USD |
| `1D` | `0.1192` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 7,250.00 USD | 1,990.00 USD | 7,230.00 USD |
| `7D` | `0.1192` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 7,250.00 USD | 1,990.00 USD | 7,230.00 USD |
| `1D` | `0.1194` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 6,310.00 USD | 1,390.00 USD | 2,740.00 USD |
| `7D` | `0.1194` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 6,310.00 USD | 1,390.00 USD | 2,740.00 USD |
| `1D` | `0.1196` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 3,240.00 USD | 2,860.00 USD | 64.58 USD |
| `7D` | `0.1196` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 3,240.00 USD | 2,860.00 USD | 64.58 USD |
| `1D` | `0.1198` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 3,660.00 USD | 2,040.00 USD |
| `7D` | `0.1198` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 3,660.00 USD | 2,040.00 USD |
| `1D` | `0.1200` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,840.00 USD | 1,050.00 USD | 6,160.00 USD |
| `7D` | `0.1200` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,840.00 USD | 1,050.00 USD | 6,160.00 USD |
| `1D` | `0.1202` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 10,280.00 USD | 460.32 USD | 4,370.00 USD |
| `7D` | `0.1202` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 10,280.00 USD | 460.32 USD | 4,370.00 USD |
| `1D` | `0.1204` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 769.98 USD | 1,290.00 USD |
| `7D` | `0.1204` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 769.98 USD | 1,290.00 USD |
| `1D` | `0.1206` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 3,340.00 USD | 2,440.00 USD | 3,760.00 USD |
| `7D` | `0.1206` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 3,340.00 USD | 2,440.00 USD | 3,760.00 USD |
| `1D` | `0.1208` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 4,380.00 USD | 1,770.00 USD | 4,060.00 USD |
| `7D` | `0.1208` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 4,380.00 USD | 1,770.00 USD | 4,060.00 USD |
| `1D` | `0.1210` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 3,980.00 USD | 4,240.00 USD | 3,290.00 USD |
| `7D` | `0.1210` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 3,980.00 USD | 4,240.00 USD | 3,290.00 USD |
| `1D` | `0.1212` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 1,360.00 USD | 7,880.00 USD |
| `7D` | `0.1212` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 1,360.00 USD | 7,880.00 USD |
| `1D` | `0.1214` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 4,020.00 USD | 820.70 USD | 7,570.00 USD |
| `7D` | `0.1214` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 4,020.00 USD | 820.70 USD | 7,570.00 USD |
| `1D` | `0.1216` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 1,330.00 USD | 0.00 USD | 3,970.00 USD |
| `7D` | `0.1216` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 1,330.00 USD | 0.00 USD | 3,970.00 USD |
| `1D` | `0.1218` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 1,550.00 USD | 624.33 USD | 8,830.00 USD |
| `7D` | `0.1218` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 1,550.00 USD | 624.33 USD | 8,830.00 USD |
| `1D` | `0.1220` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 769.06 USD | 2,350.00 USD | 3,970.00 USD |
| `7D` | `0.1220` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 769.06 USD | 2,350.00 USD | 3,970.00 USD |
| `1D` | `0.1222` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 2,980.00 USD | 2,630.00 USD | 3,050.00 USD |
| `7D` | `0.1222` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 2,980.00 USD | 2,630.00 USD | 3,050.00 USD |
| `1D` | `0.1224` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 2,660.00 USD | 558.39 USD | 3,490.00 USD |
| `7D` | `0.1224` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 2,660.00 USD | 558.39 USD | 3,490.00 USD |
| `1D` | `0.1228` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 1,970.00 USD | 0.00 USD | 1.91 USD |
| `7D` | `0.1228` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 1,970.00 USD | 0.00 USD | 1.91 USD |
| `1D` | `0.1230` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 403.62 USD | 789.22 USD |
| `7D` | `0.1230` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 403.62 USD | 789.22 USD |
| `1D` | `0.1232` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 1,250.00 USD | 1,270.00 USD | 4.12 USD |
| `7D` | `0.1232` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 1,250.00 USD | 1,270.00 USD | 4.12 USD |
| `1D` | `0.1234` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 1,070.00 USD | 2,120.00 USD | 1,200.00 USD |
| `7D` | `0.1234` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 1,070.00 USD | 2,120.00 USD | 1,200.00 USD |
| `1D` | `0.1236` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 1,570.00 USD | 1,430.00 USD | 911.21 USD |
| `7D` | `0.1236` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 1,570.00 USD | 1,430.00 USD | 911.21 USD |
| `1D` | `0.1238` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 3,120.00 USD | 724.40 USD | 587.32 USD |
| `7D` | `0.1238` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 3,120.00 USD | 724.40 USD | 587.32 USD |
| `1D` | `0.1240` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 2,890.00 USD | 1,830.00 USD | 8.83 USD |
| `7D` | `0.1240` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 2,890.00 USD | 1,830.00 USD | 8.83 USD |
| `1D` | `0.1242` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 3,360.00 USD | 2,540.00 USD | 8,220.00 USD |
| `7D` | `0.1242` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 3,360.00 USD | 2,540.00 USD | 8,220.00 USD |
| `1D` | `0.1244` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 827.81 USD | 4,170.00 USD | 7,340.00 USD |
| `7D` | `0.1244` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 827.81 USD | 4,170.00 USD | 7,340.00 USD |
| `1D` | `0.1246` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 6,440.00 USD | 2,630.00 USD | 2,010.00 USD |
| `7D` | `0.1246` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 6,440.00 USD | 2,630.00 USD | 2,010.00 USD |
| `1D` | `0.1248` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 1,910.00 USD | 0.00 USD | 4,520.00 USD |
| `7D` | `0.1248` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 1,910.00 USD | 0.00 USD | 4,520.00 USD |
| `1D` | `0.1250` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 3,160.00 USD | 2,120.00 USD | 2,640.00 USD |
| `7D` | `0.1250` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 3,160.00 USD | 2,120.00 USD | 2,640.00 USD |
| `1D` | `0.1252` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 2,300.00 USD | 947.50 USD | 4,650.00 USD |
| `7D` | `0.1252` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 2,300.00 USD | 947.50 USD | 4,650.00 USD |
| `1D` | `0.1254` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 2,780.00 USD | 2,210.00 USD | 2,480.00 USD |
| `7D` | `0.1254` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 2,780.00 USD | 2,210.00 USD | 2,480.00 USD |
| `1D` | `0.1256` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 936.16 USD | 27.42 USD |
| `7D` | `0.1256` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 936.16 USD | 27.42 USD |
| `1D` | `0.1258` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 2,100.00 USD | 1,690.00 USD | 12.41 USD |
| `7D` | `0.1258` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 2,100.00 USD | 1,690.00 USD | 12.41 USD |
| `1D` | `0.1260` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 1,010.00 USD | 0.00 USD | 5.73 USD |
| `7D` | `0.1260` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 1,010.00 USD | 0.00 USD | 5.73 USD |
| `1D` | `0.1262` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 1,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1262` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 1,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1264` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 1,300.00 USD | 694.78 USD | 0.00 USD |
| `7D` | `0.1264` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 1,300.00 USD | 694.78 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `75.28M` | Total OI Tokens: `667,830,574.7 OP`
  * 1h OI Change: `-1.48%` | 4h OI Change: `+1.53%` | 24h OI Change: `-0.96%`
  * Exchange Breakdown: Binance=`17.19M` | Bybit=`14.39M` | OKX=`4.25M` | Hyperliquid=`3.99M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.37K` | Last 24h: `270.64` | Last 3d: `-2.23K` | Last 7d: `-15.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0078%` | **USDT OKX** | `0.0087%` |
| **USDT Bybit** | `0.0027%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0077%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `42.05%` | `57.95%` | `0.73` | 1,760,000.00 USD |
| `15M` | `Binance` | `45.83%` | `54.17%` | `0.85` | 621,760.00 USD |
| `15M` | `OKX` | `65.96%` | `34.04%` | `1.94` | 259,680.00 USD |
| `15M` | `Bybit` | `41.38%` | `58.62%` | `0.71` | 123,850.00 USD |
| `15M` | `KuCoin` | `46.9%` | `53.1%` | `0.88` | 113,440.00 USD |
| `15M` | `Gate` | `42.48%` | `57.52%` | `0.74` | 23,850.00 USD |
| `15M` | `Bitget` | `28.71%` | `71.29%` | `0.40` | 26,580.00 USD |
| `15M` | `BingX` | `28.73%` | `71.27%` | `0.40` | 238,140.00 USD |
| `15M` | `MEXC` | `7.88%` | `92.12%` | `0.09` | 192,960.00 USD |
| `15M` | `Bitunix` | `46.34%` | `53.66%` | `0.86` | 19,280.00 USD |
| `15M` | `Hyperliquid` | `91.71%` | `8.29%` | `11.06` | 6,770.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `32.42%` | `67.58%` | `0.48` | 65,650.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `61.47%` | `38.53%` | `1.60` | 64,750.00 USD |
| `15M` | `HTX` | `99.12%` | `0.88%` | `112.64` | 39.26 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `51.09%` | `48.91%` | `1.04` | 8,860.00 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 645.92 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `12.03%` | `87.97%` | `0.14` | 200.55 USD |
| `15M` | `Whale Positions` | `45.83%` | `54.17%` | `0.85` | 621,760.00 USD |
| `15M` | `Global Accounts` | `42.05%` | `57.95%` | `0.73` | 1,760,000.00 USD |
| `1H` | `OP` | `44.95%` | `55.05%` | `0.82` | 8,480,000.00 USD |
| `1H` | `Binance` | `43.03%` | `56.97%` | `0.76` | 3,760,000.00 USD |
| `1H` | `OKX` | `43.79%` | `56.21%` | `0.78` | 990,530.00 USD |
| `1H` | `Bybit` | `55.09%` | `44.91%` | `1.23` | 1,000,000.00 USD |
| `1H` | `KuCoin` | `47.79%` | `52.21%` | `0.92` | 616,470.00 USD |
| `1H` | `Gate` | `57.37%` | `42.63%` | `1.35` | 129,220.00 USD |
| `1H` | `Bitget` | `40.66%` | `59.34%` | `0.69` | 201,400.00 USD |
| `1H` | `BingX` | `44.84%` | `55.16%` | `0.81` | 526,790.00 USD |
| `1H` | `MEXC` | `35.46%` | `64.54%` | `0.55` | 466,760.00 USD |
| `1H` | `Bitunix` | `45.07%` | `54.93%` | `0.82` | 188,280.00 USD |
| `1H` | `Hyperliquid` | `53.6%` | `46.4%` | `1.16` | 84,070.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.94%` | `49.06%` | `1.04` | 189,860.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `37.83%` | `62.17%` | `0.61` | 288,940.00 USD |
| `1H` | `HTX` | `32.77%` | `67.23%` | `0.49` | 202.48 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `57.29%` | `42.71%` | `1.34` | 27,500.00 USD |
| `1H` | `Aster` | `57.36%` | `42.64%` | `1.35` | 3,820.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `42.22%` | `57.78%` | `0.73` | 1,700.00 USD |
| `1H` | `Whale Positions` | `43.03%` | `56.97%` | `0.76` | 3,760,000.00 USD |
| `1H` | `Global Accounts` | `44.95%` | `55.05%` | `0.82` | 8,480,000.00 USD |
| `4H` | `OP` | `47.15%` | `52.85%` | `0.89` | 97,600,000.00 USD |
| `4H` | `Binance` | `48.78%` | `51.22%` | `0.95` | 35,200,000.00 USD |
| `4H` | `OKX` | `47.18%` | `52.82%` | `0.89` | 21,360,000.00 USD |
| `4H` | `Bybit` | `48.5%` | `51.5%` | `0.94` | 6,940,000.00 USD |
| `4H` | `KuCoin` | `49.78%` | `50.22%` | `0.99` | 2,630,000.00 USD |
| `4H` | `Gate` | `53.36%` | `46.64%` | `1.14` | 1,930,000.00 USD |
| `4H` | `Bitget` | `56.66%` | `43.34%` | `1.31` | 2,720,000.00 USD |
| `4H` | `BingX` | `37.32%` | `62.68%` | `0.60` | 2,550,000.00 USD |
| `4H` | `MEXC` | `50.35%` | `49.65%` | `1.01` | 1,260,000.00 USD |
| `4H` | `Bitunix` | `48.79%` | `51.21%` | `0.95` | 2,580,000.00 USD |
| `4H` | `Hyperliquid` | `66.72%` | `33.28%` | `2.00` | 798,590.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.73%` | `50.27%` | `0.99` | 15,810,000.00 USD |
| `4H` | `Crypto.com` | `23.96%` | `76.04%` | `0.32` | 355.33 USD |
| `4H` | `WhiteBIT` | `0.24%` | `99.76%` | `0.00` | 3,230,000.00 USD |
| `4H` | `HTX` | `43.31%` | `56.69%` | `0.76` | 63,840.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.4%` | `54.6%` | `0.83` | 283,200.00 USD |
| `4H` | `Aster` | `52.78%` | `47.22%` | `1.12` | 134,310.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.82%` | `51.18%` | `0.95` | 107,820.00 USD |
| `4H` | `Whale Positions` | `48.78%` | `51.22%` | `0.95` | 35,200,000.00 USD |
| `4H` | `Global Accounts` | `47.15%` | `52.85%` | `0.89` | 97,600,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1120` | `0.1122` | `0.1120` | `0.1130` | `0.1118` | 431,882.14 USD | 173,404.30 USD | 258,477.84 USD | -85,073.54 USD | `-19.70%` | `10B / 28S` |
| `0:00 UTC` | `0.1132` | `0.1126` | `0.1132` | `0.1134` | `0.1117` | 598,596.80 USD | 325,324.83 USD | 273,271.97 USD | 52,052.86 USD | `+8.70%` | `35B / 15S` |
| `5:00 UTC` | `0.1124` | `0.1128` | `0.1124` | `0.1134` | `0.1123` | 503,080.80 USD | 199,130.81 USD | 303,950.00 USD | -104,819.19 USD | `-20.84%` | `16B / 34S` |
| `0:00 UTC` | `0.1132` | `0.1131` | `0.1132` | `0.1135` | `0.1123` | 357,466.20 USD | 196,512.03 USD | 160,954.17 USD | 35,557.85 USD | `+9.95%` | `25B / 9S` |
| `5:00 UTC` | `0.1136` | `0.1136` | `0.1136` | `0.1141` | `0.1130` | 571,492.98 USD | 299,278.35 USD | 272,214.63 USD | 27,063.72 USD | `+4.74%` | `24B / 17S` |
| `0:00 UTC` | `0.1137` | `0.1140` | `0.1137` | `0.1149` | `0.1134` | 877,269.44 USD | 486,783.19 USD | 390,486.24 USD | 96,296.95 USD | `+10.98%` | `34B / 22S` |
| `5:00 UTC` | `0.1134` | `0.1136` | `0.1134` | `0.1142` | `0.1132` | 635,625.25 USD | 325,080.19 USD | 310,545.06 USD | 14,535.13 USD | `+2.29%` | `15B / 17S` |
| `0:00 UTC` | `0.1133` | `0.1131` | `0.1133` | `0.1135` | `0.1126` | 680,945.05 USD | 236,805.84 USD | 444,139.21 USD | -207,333.38 USD | `-30.45%` | `14B / 19S` |
| `5:00 UTC` | `0.1128` | `0.1128` | `0.1128` | `0.1130` | `0.1127` | 243,648.48 USD | 108,202.11 USD | 135,446.38 USD | -27,244.27 USD | `-11.18%` | `2B / 9S` |
| `0:00 UTC` | `0.1129` | `0.1128` | `0.1129` | `0.1132` | `0.1125` | 195,436.74 USD | 88,698.52 USD | 106,738.21 USD | -18,039.69 USD | `-9.23%` | `11B / 14S` |

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
| `5m` | -4,030.00 USD | -16,380.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,480.00 USD | -92,050.00 USD | **`DISTRIBUTION`** |
| `30m` | 1,020.00 USD | -180,470.00 USD | **`DISTRIBUTION`** |
| `1h` | -11,840.00 USD | -346,170.00 USD | **`DISTRIBUTION`** |
| `2h` | 15,530.00 USD | -181,200.00 USD | **`DISTRIBUTION`** |
| `4h` | 164,850.00 USD | 358,350.00 USD | **`ACCUMULATION`** |
| `6h` | 208,160.00 USD | 317,890.00 USD | **`ACCUMULATION`** |
| `8h` | 238,330.00 USD | 847,460.00 USD | **`ACCUMULATION`** |
| `12h` | 220,900.00 USD | 724,430.00 USD | **`ACCUMULATION`** |
| `24h` | 198,440.00 USD | -663,560.00 USD | **`DISTRIBUTION`** |
| `1w` | -127,360.00 USD | -9,550,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,580,000.00 USD | -77,970,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-4.03K` | 15m=`-1.48K` | 1h=`-11.84K` | 24h=`+198.44K`
* Futures Capital Netflows: 5m=`-16.38K` | 15m=`-92.05K` | 1h=`-346.17K` | 24h=`-663.56K`
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
  * `2026-10-29 22:05:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [bea.gov] - (Sentiment: `Neutral`)


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
