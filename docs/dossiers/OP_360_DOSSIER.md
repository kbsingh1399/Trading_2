# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-29 22:33:52 IST` (`2026-10-29 17:03:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1129` | `0.1129` | `0.1127` | `0.1128` | `773,265` | 87,213.04 USD | -30,416.86 USD | `-34.88%` | -552,479.81 USD | `-0.40` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1128` | `0.1129` | `0.1127` | `0.1129` | `671,373` | 75,775.71 USD | 4,001.16 USD | `+5.28%` | -548,478.65 USD | `+0.22` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1129` | `0.1130` | `0.1128` | `0.1129` | `180,736` | 20,402.28 USD | 8,960.62 USD | `+43.92%` | -539,518.03 USD | `+0.27` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1132` | `0.1135` | `0.1126` | `0.1130` | `6,020,436` | 680,945.05 USD | -207,333.38 USD | `-30.45%` | -498,481.71 USD | `-2.81` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1130` | `0.1130` | `0.1127` | `0.1129` | `2,159,370` | 243,648.48 USD | -27,244.27 USD | `-11.18%` | -525,725.97 USD | `-0.49` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1129` | `0.1130` | `0.1128` | `0.1129` | `187,494` | 21,165.09 USD | 8,197.82 USD | `+38.73%` | -517,528.15 USD | `-0.09` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.1119` | `0.1141` | `0.1117` | `0.1139` | `17,968,115` | 2,030,636.79 USD | 9,855.25 USD | `+0.49%` | -531,384.47 USD | `+0.23` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1140` | `0.1148` | `0.1126` | `0.1129` | `21,471,756` | 2,437,488.22 USD | -123,745.56 USD | `-5.08%` | -655,130.03 USD | `-0.29` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1129` | `0.1130` | `0.1128` | `0.1129` | `187,494` | 21,165.09 USD | 8,197.82 USD | `+38.73%` | -646,932.21 USD | `+0.27` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,229,700.44 USD | `+0.64` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -888,444.84 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1126` | `0.1129` | `21,661,648` | 2,458,924.01 USD | -115,277.04 USD | `-4.69%` | -1,003,721.88 USD | `+0.08` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1131` | `0.1136` | `0.1072` | `0.1085` | `76,338,549` | 8,353,905.81 USD | -1,528,374.61 USD | `-18.30%` | -1,480,991.26 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1085` | `0.1106` | `0.1071` | `0.1076` | `47,048,931` | 5,111,570.05 USD | 108,567.99 USD | `+2.12%` | -1,372,423.27 USD | `+0.75` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,229,700.44 USD | `+0.64` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -888,444.84 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1126` | `0.1129` | `21,661,648` | 2,458,924.01 USD | -115,277.04 USD | `-4.69%` | -1,003,721.88 USD | `+0.08` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:31:36 IST` |

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
| `7D` | `Long Liquidation` | `0.0961` | 3,910,000.00 USD | 3,910,000.00 USD | 2,410.00 USD | 1,140.00 USD | 20.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0963` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 1,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0965` | 419.87 USD | 51,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0967` | 3,910,000.00 USD | 3,910,000.00 USD | 3,770.00 USD | 2,660.00 USD | 2,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0969` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 2,810.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 2,000.00 USD | 34.36 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0973` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0975` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 1,160.00 USD | 4,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0975` | 12,670.00 USD | 51,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0977` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 5,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0979` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 1,530.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0981` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 3,860,000.00 USD | 3,860,000.00 USD | 7,990.00 USD | 1,230.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0985` | 1,810,000.00 USD | 1,810,000.00 USD | 8,560.00 USD | 1,710.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0985` | 3,840,000.00 USD | 3,840,000.00 USD | 7,110.00 USD | 0.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0985` | 19,960.00 USD | 38,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0987` | 1,800,000.00 USD | 1,800,000.00 USD | 11,770.00 USD | 2,440.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0987` | 3,820,000.00 USD | 3,820,000.00 USD | 5,390.00 USD | 9,190.00 USD | 37,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0989` | 1,780,000.00 USD | 1,780,000.00 USD | 2,350.00 USD | 3,330.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 3,770,000.00 USD | 3,770,000.00 USD | 12,260.00 USD | 4,520.00 USD | 27,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0991` | 1,770,000.00 USD | 1,770,000.00 USD | 4,350.00 USD | 4,220.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0991` | 3,730,000.00 USD | 3,730,000.00 USD | 14,350.00 USD | 10,350.00 USD | 13,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0993` | 1,750,000.00 USD | 1,750,000.00 USD | 2,360.00 USD | 1,220.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0993` | 3,690,000.00 USD | 3,690,000.00 USD | 23,920.00 USD | 10,140.00 USD | 24,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0995` | 1,740,000.00 USD | 1,740,000.00 USD | 2,990.00 USD | 624.33 USD | 12,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 3,630,000.00 USD | 3,630,000.00 USD | 13,090.00 USD | 6,160.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0997` | 1,720,000.00 USD | 1,720,000.00 USD | 5,070.00 USD | 1,410.00 USD | 9,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0997` | 3,590,000.00 USD | 3,590,000.00 USD | 21,100.00 USD | 5,500.00 USD | 29,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0999` | 1,710,000.00 USD | 1,710,000.00 USD | 4,590.00 USD | 4,070.00 USD | 1,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0999` | 3,530,000.00 USD | 3,530,000.00 USD | 14,230.00 USD | 6,540.00 USD | 18,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1001` | 1,700,000.00 USD | 1,700,000.00 USD | 4,190.00 USD | 668.73 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 3,490,000.00 USD | 3,490,000.00 USD | 29,230.00 USD | 3,010.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1003` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1003` | 3,450,000.00 USD | 3,450,000.00 USD | 8,010.00 USD | 7,060.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1005` | 1,690,000.00 USD | 1,690,000.00 USD | 1,970.00 USD | 403.62 USD | 47.02 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1005` | 3,430,000.00 USD | 3,430,000.00 USD | 25,070.00 USD | 11,000.00 USD | 18,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1005` | 427.25 USD | 18,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1007` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 430.11 USD | 826.91 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 3,370,000.00 USD | 3,370,000.00 USD | 10,260.00 USD | 2,280.00 USD | 14,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1009` | 1,680,000.00 USD | 1,680,000.00 USD | 1,070.00 USD | 842.63 USD | 28.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1009` | 3,350,000.00 USD | 3,350,000.00 USD | 15,320.00 USD | 1,660.00 USD | 6,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1011` | 1,680,000.00 USD | 1,680,000.00 USD | 1,570.00 USD | 1,240.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1011` | 3,320,000.00 USD | 3,320,000.00 USD | 4,430.00 USD | 4,720.00 USD | 8,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1013` | 1,680,000.00 USD | 1,680,000.00 USD | 774.15 USD | 1,490.00 USD | 587.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 3,300,000.00 USD | 3,300,000.00 USD | 12,870.00 USD | 4,030.00 USD | 3,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1015` | 1,670,000.00 USD | 1,670,000.00 USD | 2,790.00 USD | 0.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1015` | 3,280,000.00 USD | 3,280,000.00 USD | 6,830.00 USD | 965.35 USD | 2,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1015` | 622.37 USD | 17,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1017` | 1,670,000.00 USD | 1,670,000.00 USD | 1,660.00 USD | 2,060.00 USD | 2,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1017` | 3,270,000.00 USD | 3,270,000.00 USD | 11,450.00 USD | 2,850.00 USD | 4,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1019` | 1,660,000.00 USD | 1,660,000.00 USD | 2,800.00 USD | 3,420.00 USD | 2,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1019` | 3,260,000.00 USD | 3,260,000.00 USD | 3,160.00 USD | 3,310.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1021` | 1,650,000.00 USD | 1,650,000.00 USD | 2,580.00 USD | 1,320.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1021` | 3,240,000.00 USD | 3,240,000.00 USD | 7,900.00 USD | 3,270.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1023` | 1,640,000.00 USD | 1,640,000.00 USD | 1,440.00 USD | 1,390.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1023` | 3,220,000.00 USD | 3,220,000.00 USD | 4,030.00 USD | 4,990.00 USD | 11,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1025` | 1,640,000.00 USD | 1,640,000.00 USD | 855.19 USD | 947.50 USD | 2,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1025` | 3,200,000.00 USD | 3,200,000.00 USD | 1,550.00 USD | 0.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1025` | 17,360.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1027` | 1,630,000.00 USD | 1,630,000.00 USD | 2,780.00 USD | 1,590.00 USD | 73.56 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1027` | 3,200,000.00 USD | 3,200,000.00 USD | 2,250.00 USD | 1,170.00 USD | 344.47 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1029` | 1,630,000.00 USD | 1,630,000.00 USD | 4,340.00 USD | 705.79 USD | 6,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1029` | 3,190,000.00 USD | 3,190,000.00 USD | 7,420.00 USD | 3,000.00 USD | 332.49 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1031` | 1,620,000.00 USD | 1,620,000.00 USD | 11,600.00 USD | 3,910.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1031` | 3,180,000.00 USD | 3,180,000.00 USD | 13,690.00 USD | 5,070.00 USD | 10,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1033` | 1,590,000.00 USD | 1,590,000.00 USD | 8,760.00 USD | 2,790.00 USD | 10,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1033` | 3,150,000.00 USD | 3,150,000.00 USD | 3,880.00 USD | 2,640.00 USD | 15,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1035` | 1,570,000.00 USD | 1,570,000.00 USD | 7,450.00 USD | 6,850.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1035` | 3,130,000.00 USD | 3,130,000.00 USD | 2,710.00 USD | 9,400.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1037` | 1,550,000.00 USD | 1,550,000.00 USD | 2,220.00 USD | 13,000.00 USD | 9,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1037` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1039` | 1,520,000.00 USD | 1,520,000.00 USD | 3,660.00 USD | 1,730.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1039` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 5,170.00 USD | 167.04 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1041` | 1,510,000.00 USD | 1,510,000.00 USD | 7,790.00 USD | 6,910.00 USD | 13,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1041` | 3,080,000.00 USD | 3,080,000.00 USD | 5,940.00 USD | 2,910.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1043` | 1,480,000.00 USD | 1,480,000.00 USD | 17,650.00 USD | 5,650.00 USD | 7,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1043` | 3,060,000.00 USD | 3,060,000.00 USD | 15,960.00 USD | 5,980.00 USD | 21,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1045` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 2,600.00 USD | 6,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1045` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 3,830.00 USD | 14,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1047` | 1,440,000.00 USD | 1,440,000.00 USD | 4,610.00 USD | 2,610.00 USD | 21,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1047` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 1,720.00 USD | 22,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1049` | 1,410,000.00 USD | 1,410,000.00 USD | 21,050.00 USD | 4,090.00 USD | 10,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1049` | 2,970,000.00 USD | 2,970,000.00 USD | 34,790.00 USD | 4,810.00 USD | 35,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1051` | 1,370,000.00 USD | 1,370,000.00 USD | 20,120.00 USD | 10,840.00 USD | 26,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1051` | 2,900,000.00 USD | 2,900,000.00 USD | 17,290.00 USD | 11,500.00 USD | 48,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1053` | 1,320,000.00 USD | 1,320,000.00 USD | 41,820.00 USD | 8,170.00 USD | 29,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1053` | 2,820,000.00 USD | 2,820,000.00 USD | 47,580.00 USD | 29,800.00 USD | 95,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1055` | 1,240,000.00 USD | 1,240,000.00 USD | 28,290.00 USD | 21,140.00 USD | 35,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1055` | 2,650,000.00 USD | 2,650,000.00 USD | 50,090.00 USD | 27,290.00 USD | 122,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1057` | 1,150,000.00 USD | 1,150,000.00 USD | 26,000.00 USD | 26,820.00 USD | 46,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1057` | 2,450,000.00 USD | 2,450,000.00 USD | 44,200.00 USD | 43,030.00 USD | 74,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1059` | 1,050,000.00 USD | 1,050,000.00 USD | 17,220.00 USD | 21,420.00 USD | 55,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1059` | 2,280,000.00 USD | 2,280,000.00 USD | 92,510.00 USD | 49,670.00 USD | 116,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1061` | 958,950.00 USD | 958,950.00 USD | 15,660.00 USD | 9,870.00 USD | 51,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1061` | 2,030,000.00 USD | 2,030,000.00 USD | 38,260.00 USD | 28,780.00 USD | 76,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1063` | 881,930.00 USD | 881,930.00 USD | 57,650.00 USD | 16,340.00 USD | 53,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1063` | 1,880,000.00 USD | 1,880,000.00 USD | 95,080.00 USD | 38,330.00 USD | 151,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1065` | 754,430.00 USD | 754,430.00 USD | 19,500.00 USD | 15,700.00 USD | 13,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1065` | 1,600,000.00 USD | 1,600,000.00 USD | 84,890.00 USD | 21,040.00 USD | 86,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1067` | 705,830.00 USD | 705,830.00 USD | 16,020.00 USD | 14,530.00 USD | 23,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1067` | 1,410,000.00 USD | 1,410,000.00 USD | 97,290.00 USD | 34,000.00 USD | 67,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1069` | 651,340.00 USD | 651,340.00 USD | 20,560.00 USD | 6,620.00 USD | 54,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1069` | 1,210,000.00 USD | 1,210,000.00 USD | 76,900.00 USD | 32,620.00 USD | 67,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1071` | 569,340.00 USD | 569,340.00 USD | 48,660.00 USD | 8,170.00 USD | 16,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1071` | 1,030,000.00 USD | 1,030,000.00 USD | 119,440.00 USD | 27,240.00 USD | 42,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1073` | 496,310.00 USD | 496,310.00 USD | 8,740.00 USD | 10,680.00 USD | 20,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1073` | 840,080.00 USD | 840,080.00 USD | 62,850.00 USD | 17,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1075` | 456,030.00 USD | 456,030.00 USD | 11,540.00 USD | 3,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1075` | 759,530.00 USD | 759,530.00 USD | 8,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1077` | 440,590.00 USD | 440,590.00 USD | 3,180.00 USD | 6,210.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1079` | 420,370.00 USD | 420,370.00 USD | 9,370.00 USD | 11,900.00 USD | 23,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1079` | 750,810.00 USD | 750,810.00 USD | 123,150.00 USD | 18,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1081` | 375,640.00 USD | 375,640.00 USD | 5,870.00 USD | 7,210.00 USD | 46,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1081` | 609,130.00 USD | 609,130.00 USD | 200,110.00 USD | 9,430.00 USD | 28,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1083` | 315,620.00 USD | 315,620.00 USD | 30,270.00 USD | 0.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1083` | 370,770.00 USD | 370,770.00 USD | 94,800.00 USD | 0.00 USD | 37,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1085` | 258,060.00 USD | 258,060.00 USD | 14,370.00 USD | 7,490.00 USD | 47,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1085` | 238,420.00 USD | 238,420.00 USD | 15,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1087` | 189,070.00 USD | 189,070.00 USD | 15,310.00 USD | 6,720.00 USD | 22,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1087` | 222,500.00 USD | 222,500.00 USD | 22,680.00 USD | 0.00 USD | 27,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1089` | 144,170.00 USD | 144,170.00 USD | 41,340.00 USD | 12,040.00 USD | 18,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1089` | 172,040.00 USD | 172,040.00 USD | 0.00 USD | 9,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1091` | 72,720.00 USD | 72,720.00 USD | 16,940.00 USD | 2,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1091` | 162,920.00 USD | 162,920.00 USD | 16,310.00 USD | 3,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1093` | 52,990.00 USD | 52,990.00 USD | 13,100.00 USD | 0.00 USD | 6,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1095` | 142,820.00 USD | 142,820.00 USD | 18,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1097` | 123,980.00 USD | 123,980.00 USD | 0.00 USD | 2,970.00 USD | 21,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1099` | 99,410.00 USD | 99,410.00 USD | 0.00 USD | 0.00 USD | 25,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1103` | 74,350.00 USD | 74,350.00 USD | 6,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1105` | 67,420.00 USD | 67,420.00 USD | 0.00 USD | 5,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1107` | 61,610.00 USD | 61,610.00 USD | 0.00 USD | 4,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1113` | 33,670.00 USD | 33,670.00 USD | 0.00 USD | 8,100.00 USD | 25,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1113` | 57,490.00 USD | 57,490.00 USD | 0.00 USD | 0.00 USD | 57,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1115` | 36,130.00 USD | 36,130.00 USD | 0.00 USD | 0.00 USD | 36,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1117` | 32,500.00 USD | 32,500.00 USD | 0.00 USD | 16,900.00 USD | 15,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1117` | 82,480.00 USD | 82,480.00 USD | 0.00 USD | 22,780.00 USD | 23,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1119` | 102,900.00 USD | 102,900.00 USD | 35,630.00 USD | 7,980.00 USD | 26,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1119` | 141,140.00 USD | 141,140.00 USD | 45,230.00 USD | 2,640.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1121` | 165,970.00 USD | 165,970.00 USD | 19,830.00 USD | 16,100.00 USD | 27,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 192,410.00 USD | 192,410.00 USD | 29,340.00 USD | 9,400.00 USD | 12,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1123` | 270,830.00 USD | 270,830.00 USD | 29,460.00 USD | 26,020.00 USD | 49,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1123` | 285,790.00 USD | 285,790.00 USD | 48,680.00 USD | 18,520.00 USD | 26,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1125` | 366,810.00 USD | 366,810.00 USD | 17,260.00 USD | 13,480.00 USD | 65,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1125` | 336,770.00 USD | 336,770.00 USD | 7,560.00 USD | 14,600.00 USD | 28,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1127` | 443,580.00 USD | 443,580.00 USD | 21,670.00 USD | 10,390.00 USD | 44,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1127` | 391,130.00 USD | 391,130.00 USD | 0.00 USD | 6,460.00 USD | 47,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1129` | 543,680.00 USD | 543,680.00 USD | 32,030.00 USD | 13,140.00 USD | 54,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1129` | 449,170.00 USD | 449,170.00 USD | 31,880.00 USD | 5,980.00 USD | 20,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1131` | 593,730.00 USD | 593,730.00 USD | 15,310.00 USD | 9,680.00 USD | 25,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1131` | 505,890.00 USD | 505,890.00 USD | 22,680.00 USD | 0.00 USD | 34,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1133` | 641,090.00 USD | 641,090.00 USD | 5,610.00 USD | 17,490.00 USD | 24,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 518,900.00 USD | 518,900.00 USD | 0.00 USD | 12,940.00 USD | 68.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1135` | 690,290.00 USD | 690,290.00 USD | 27,280.00 USD | 5,410.00 USD | 16,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1135` | 571,370.00 USD | 571,370.00 USD | 32,150.00 USD | 5,520.00 USD | 14,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1137` | 744,050.00 USD | 744,050.00 USD | 34,150.00 USD | 2,430.00 USD | 17,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1137` | 608,700.00 USD | 608,700.00 USD | 30,030.00 USD | 1,730.00 USD | 5,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1139` | 776,850.00 USD | 776,850.00 USD | 10,000.00 USD | 9,360.00 USD | 13,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1139` | 625,800.00 USD | 625,800.00 USD | 0.00 USD | 8,850.00 USD | 8,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1141` | 799,060.00 USD | 799,060.00 USD | 8,780.00 USD | 5,920.00 USD | 7,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1141` | 643,100.00 USD | 643,100.00 USD | 4,360.00 USD | 5,280.00 USD | 7,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1143` | 816,770.00 USD | 816,770.00 USD | 1,590.00 USD | 7,740.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1143` | 717,380.00 USD | 717,380.00 USD | 0.00 USD | 0.00 USD | 74,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1145` | 863,730.00 USD | 863,730.00 USD | 8,350.00 USD | 10,790.00 USD | 27,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 878,170.00 USD | 878,170.00 USD | 10,360.00 USD | 9,260.00 USD | 141,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1147` | 904,140.00 USD | 904,140.00 USD | 8,840.00 USD | 4,840.00 USD | 26,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1147` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 4,720.00 USD | 134,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1149` | 944,560.00 USD | 944,560.00 USD | 11,450.00 USD | 0.00 USD | 28,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1149` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 72,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1151` | 1,010,000.00 USD | 1,010,000.00 USD | 21,200.00 USD | 3,740.00 USD | 43,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 1,300,000.00 USD | 1,300,000.00 USD | 92,570.00 USD | 0.00 USD | 118,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1153` | 1,090,000.00 USD | 1,090,000.00 USD | 30,050.00 USD | 15,960.00 USD | 26,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1153` | 1,580,000.00 USD | 1,580,000.00 USD | 147,450.00 USD | 0.00 USD | 132,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1155` | 1,160,000.00 USD | 1,160,000.00 USD | 18,450.00 USD | 26,450.00 USD | 28,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1155` | 1,790,000.00 USD | 1,790,000.00 USD | 108,940.00 USD | 24,970.00 USD | 71,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1157` | 1,240,000.00 USD | 1,240,000.00 USD | 29,940.00 USD | 11,110.00 USD | 35,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 2,000,000.00 USD | 2,000,000.00 USD | 163,490.00 USD | 3,760.00 USD | 48,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1159` | 1,260,000.00 USD | 1,260,000.00 USD | 7,810.00 USD | 8,370.00 USD | 8,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1159` | 2,170,000.00 USD | 2,170,000.00 USD | 105,000.00 USD | 12,710.00 USD | 48,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1161` | 1,330,000.00 USD | 1,330,000.00 USD | 25,800.00 USD | 6,970.00 USD | 33,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1161` | 2,440,000.00 USD | 2,440,000.00 USD | 155,210.00 USD | 37,250.00 USD | 82,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1163` | 1,350,000.00 USD | 1,350,000.00 USD | 18,210.00 USD | 6,750.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 2,600,000.00 USD | 2,600,000.00 USD | 74,250.00 USD | 11,460.00 USD | 68,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1165` | 1,380,000.00 USD | 1,380,000.00 USD | 9,310.00 USD | 11,840.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1165` | 2,730,000.00 USD | 2,730,000.00 USD | 77,390.00 USD | 25,170.00 USD | 27,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1167` | 1,410,000.00 USD | 1,410,000.00 USD | 15,040.00 USD | 13,350.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1167` | 2,870,000.00 USD | 2,870,000.00 USD | 79,610.00 USD | 21,620.00 USD | 41,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1169` | 1,450,000.00 USD | 1,450,000.00 USD | 16,040.00 USD | 4,020.00 USD | 15,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 3,030,000.00 USD | 3,030,000.00 USD | 60,400.00 USD | 14,840.00 USD | 86,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1171` | 1,460,000.00 USD | 1,460,000.00 USD | 5,230.00 USD | 4,520.00 USD | 1,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1171` | 3,130,000.00 USD | 3,130,000.00 USD | 52,070.00 USD | 9,140.00 USD | 35,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1173` | 1,480,000.00 USD | 1,480,000.00 USD | 14,960.00 USD | 3,470.00 USD | 7,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1173` | 3,210,000.00 USD | 3,210,000.00 USD | 40,860.00 USD | 7,080.00 USD | 31,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1175` | 1,510,000.00 USD | 1,510,000.00 USD | 9,050.00 USD | 10,790.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 3,310,000.00 USD | 3,310,000.00 USD | 38,840.00 USD | 8,100.00 USD | 58,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1177` | 1,540,000.00 USD | 1,540,000.00 USD | 7,820.00 USD | 8,560.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1177` | 3,370,000.00 USD | 3,370,000.00 USD | 13,120.00 USD | 14,140.00 USD | 27,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1179` | 1,570,000.00 USD | 1,570,000.00 USD | 17,010.00 USD | 5,840.00 USD | 14,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1179` | 3,460,000.00 USD | 3,460,000.00 USD | 61,380.00 USD | 10,940.00 USD | 23,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1181` | 1,590,000.00 USD | 1,590,000.00 USD | 5,740.00 USD | 4,210.00 USD | 6,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 3,520,000.00 USD | 3,520,000.00 USD | 22,290.00 USD | 15,780.00 USD | 17,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1183` | 1,610,000.00 USD | 1,610,000.00 USD | 7,310.00 USD | 1,400.00 USD | 9,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1183` | 3,560,000.00 USD | 3,560,000.00 USD | 4,040.00 USD | 1,800.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1185` | 1,630,000.00 USD | 1,630,000.00 USD | 6,370.00 USD | 3,940.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1185` | 3,590,000.00 USD | 3,590,000.00 USD | 3,880.00 USD | 5,130.00 USD | 22,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1187` | 1,660,000.00 USD | 1,660,000.00 USD | 11,520.00 USD | 8,520.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 3,640,000.00 USD | 3,640,000.00 USD | 5,620.00 USD | 11,840.00 USD | 32,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1189` | 1,670,000.00 USD | 1,670,000.00 USD | 4,220.00 USD | 3,060.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1189` | 3,680,000.00 USD | 3,680,000.00 USD | 27,240.00 USD | 15,060.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1191` | 1,680,000.00 USD | 1,680,000.00 USD | 4,940.00 USD | 6,690.00 USD | 3,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1191` | 3,830,000.00 USD | 3,830,000.00 USD | 22,650.00 USD | 15,330.00 USD | 109,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1193` | 1,690,000.00 USD | 1,690,000.00 USD | 4,720.00 USD | 2,080.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 3,860,000.00 USD | 3,860,000.00 USD | 21,260.00 USD | 0.00 USD | 9,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1195` | 1,710,000.00 USD | 1,710,000.00 USD | 9,550.00 USD | 3,210.00 USD | 2,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1195` | 3,900,000.00 USD | 3,900,000.00 USD | 11,190.00 USD | 1,780.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1197` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 1,040.00 USD | 13.79 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1197` | 3,930,000.00 USD | 3,930,000.00 USD | 6,780.00 USD | 10,800.00 USD | 14,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1199` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 3,050.00 USD | 3,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 4,010,000.00 USD | 4,010,000.00 USD | 9,100.00 USD | 0.00 USD | 64,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1201` | 1,730,000.00 USD | 1,730,000.00 USD | 6,460.00 USD | 1,070.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1201` | 4,170,000.00 USD | 4,170,000.00 USD | 114,140.00 USD | 16,380.00 USD | 29,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1203` | 1,740,000.00 USD | 1,740,000.00 USD | 7,150.00 USD | 1,250.00 USD | 2,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1203` | 4,270,000.00 USD | 4,270,000.00 USD | 70,770.00 USD | 29,250.00 USD | 6,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1205` | 1,750,000.00 USD | 1,750,000.00 USD | 2,250.00 USD | 1,910.00 USD | 759.49 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 4,540,000.00 USD | 4,540,000.00 USD | 86,480.00 USD | 48,720.00 USD | 128,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1207` | 1,760,000.00 USD | 1,760,000.00 USD | 9,520.00 USD | 524.23 USD | 4,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1207` | 4,630,000.00 USD | 4,630,000.00 USD | 12,460.00 USD | 19,400.00 USD | 59,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1209` | 1,770,000.00 USD | 1,770,000.00 USD | 2,350.00 USD | 3,330.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1209` | 4,830,000.00 USD | 4,830,000.00 USD | 85,160.00 USD | 19,340.00 USD | 94,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1211` | 1,790,000.00 USD | 1,790,000.00 USD | 4,350.00 USD | 4,220.00 USD | 4,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 4,910,000.00 USD | 4,910,000.00 USD | 35,090.00 USD | 18,720.00 USD | 29,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1213` | 1,800,000.00 USD | 1,800,000.00 USD | 2,360.00 USD | 1,220.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1213` | 5,000,000.00 USD | 5,000,000.00 USD | 32,700.00 USD | 29,060.00 USD | 24,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1215` | 1,810,000.00 USD | 1,810,000.00 USD | 1,650.00 USD | 0.00 USD | 4,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1215` | 5,090,000.00 USD | 5,090,000.00 USD | 27,750.00 USD | 9,240.00 USD | 59,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1217` | 1,820,000.00 USD | 1,820,000.00 USD | 1,330.00 USD | 624.33 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 5,150,000.00 USD | 5,150,000.00 USD | 18,490.00 USD | 26,300.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1219` | 1,830,000.00 USD | 1,830,000.00 USD | 5,070.00 USD | 1,410.00 USD | 9,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1219` | 5,220,000.00 USD | 5,220,000.00 USD | 26,700.00 USD | 5,500.00 USD | 35,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1221` | 1,840,000.00 USD | 1,840,000.00 USD | 4,590.00 USD | 4,070.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1221` | 5,300,000.00 USD | 5,300,000.00 USD | 47,890.00 USD | 21,770.00 USD | 18,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1223` | 1,850,000.00 USD | 1,850,000.00 USD | 4,190.00 USD | 668.73 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 5,490,000.00 USD | 5,490,000.00 USD | 103,180.00 USD | 36,290.00 USD | 48,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1225` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1225` | 5,580,000.00 USD | 5,580,000.00 USD | 50,540.00 USD | 26,800.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 16,000.00 USD | 16,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1227` | 1,860,000.00 USD | 1,860,000.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1227` | 5,750,000.00 USD | 5,750,000.00 USD | 75,750.00 USD | 31,790.00 USD | 58,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1229` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 403.62 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 5,930,000.00 USD | 5,930,000.00 USD | 87,270.00 USD | 41,310.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1231` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 430.11 USD | 789.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1231` | 6,020,000.00 USD | 6,020,000.00 USD | 29,380.00 USD | 31,660.00 USD | 30,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1232` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 842.63 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1233` | 6,140,000.00 USD | 6,140,000.00 USD | 65,180.00 USD | 12,850.00 USD | 39,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1234` | 6,150,000.00 USD | 6,150,000.00 USD | 8,540.00 USD | 5,200.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `Sell Stop` | `0.0635` | 179,600.00 USD | 0.00 USD | 1,140.00 USD | `-43.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 178,460.00 USD | 0.00 USD | 773.46 USD | `-37.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 177,690.00 USD | 0.00 USD | 592.27 USD | `-36.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 177,100.00 USD | 0.00 USD | 755.00 USD | `-33.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0805` | 176,340.00 USD | 0.00 USD | 411.06 USD | `-28.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0815` | 175,930.00 USD | 0.00 USD | 183.49 USD | `-27.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0835` | 175,750.00 USD | 0.00 USD | 456.70 USD | `-26.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 175,290.00 USD | 0.00 USD | 631.58 USD | `-24.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 174,660.00 USD | 0.00 USD | 653.74 USD | `-21.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0915` | 174,000.00 USD | 0.00 USD | 1,460.00 USD | `-18.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 172,540.00 USD | 0.00 USD | 485.13 USD | `-16.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0975` | 172,060.00 USD | 0.00 USD | 720.22 USD | `-13.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0985` | 171,340.00 USD | 0.00 USD | 1,330.00 USD | `-12.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0995` | 170,000.00 USD | 0.00 USD | 801.64 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 169,200.00 USD | 0.00 USD | 1,470.00 USD | `-10.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1015` | 167,730.00 USD | 0.00 USD | 903.42 USD | `-10.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 166,830.00 USD | 0.00 USD | 780.70 USD | `-9.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1035` | 166,050.00 USD | 0.00 USD | 4,650.00 USD | `-8.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1045` | 161,400.00 USD | 0.00 USD | 18,950.00 USD | `-7.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1055` | 142,450.00 USD | 0.00 USD | 7,770.00 USD | `-6.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1065` | 134,680.00 USD | 0.00 USD | 109,280.00 USD | `-5.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 25,390.00 USD | 0.00 USD | 21,920.00 USD | `-4.73%` | `TACTICAL (Retail Cluster)` |
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
| `7D` | `0.0961` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 2,410.00 USD | 1,140.00 USD | 20.68 USD |
| `7D` | `0.0963` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 1,210.00 USD |
| `7D` | `0.0967` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 3,770.00 USD | 2,660.00 USD | 2,840.00 USD |
| `7D` | `0.0969` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 0.00 USD | 2,810.00 USD | 9,360.00 USD |
| `7D` | `0.0971` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 0.00 USD | 2,000.00 USD | 34.36 USD |
| `7D` | `0.0973` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD |
| `7D` | `0.0975` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 0.00 USD | 1,160.00 USD | 4,130.00 USD |
| `7D` | `0.0977` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 5,800.00 USD |
| `7D` | `0.0979` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 0.00 USD | 1,530.00 USD | 5,710.00 USD |
| `7D` | `0.0981` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD |
| `7D` | `0.0983` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 7,990.00 USD | 1,230.00 USD | 8,820.00 USD |
| `1D` | `0.0985` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 8,560.00 USD | 1,710.00 USD | 5,670.00 USD |
| `7D` | `0.0985` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 7,110.00 USD | 0.00 USD | 6,320.00 USD |
| `1D` | `0.0987` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 11,770.00 USD | 2,440.00 USD | 5,600.00 USD |
| `7D` | `0.0987` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 5,390.00 USD | 9,190.00 USD | 37,360.00 USD |
| `1D` | `0.0989` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 2,350.00 USD | 3,330.00 USD | 2,850.00 USD |
| `7D` | `0.0989` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 12,260.00 USD | 4,520.00 USD | 27,240.00 USD |
| `1D` | `0.0991` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 4,350.00 USD | 4,220.00 USD | 4,440.00 USD |
| `7D` | `0.0991` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 14,350.00 USD | 10,350.00 USD | 13,520.00 USD |
| `1D` | `0.0993` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 2,360.00 USD | 1,220.00 USD | 11,780.00 USD |
| `7D` | `0.0993` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 23,920.00 USD | 10,140.00 USD | 24,060.00 USD |
| `1D` | `0.0995` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 2,990.00 USD | 624.33 USD | 12,320.00 USD |
| `7D` | `0.0995` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 13,090.00 USD | 6,160.00 USD | 25,300.00 USD |
| `1D` | `0.0997` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 5,070.00 USD | 1,410.00 USD | 9,320.00 USD |
| `7D` | `0.0997` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 21,100.00 USD | 5,500.00 USD | 29,960.00 USD |
| `1D` | `0.0999` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 4,590.00 USD | 4,070.00 USD | 1,580.00 USD |
| `7D` | `0.0999` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 14,230.00 USD | 6,540.00 USD | 18,810.00 USD |
| `1D` | `0.1001` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 4,190.00 USD | 668.73 USD | 6,190.00 USD |
| `7D` | `0.1001` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 29,230.00 USD | 3,010.00 USD | 10,920.00 USD |
| `1D` | `0.1003` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 0.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1003` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 8,010.00 USD | 7,060.00 USD | 5,210.00 USD |
| `1D` | `0.1005` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 1,970.00 USD | 403.62 USD | 47.02 USD |
| `7D` | `0.1005` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 25,070.00 USD | 11,000.00 USD | 18,310.00 USD |
| `1D` | `0.1007` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 0.00 USD | 430.11 USD | 826.91 USD |
| `7D` | `0.1007` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 10,260.00 USD | 2,280.00 USD | 14,060.00 USD |
| `1D` | `0.1009` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 1,070.00 USD | 842.63 USD | 28.75 USD |
| `7D` | `0.1009` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 15,320.00 USD | 1,660.00 USD | 6,920.00 USD |
| `1D` | `0.1011` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 1,570.00 USD | 1,240.00 USD | 1,300.00 USD |
| `7D` | `0.1011` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 4,430.00 USD | 4,720.00 USD | 8,880.00 USD |
| `1D` | `0.1013` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 774.15 USD | 1,490.00 USD | 587.32 USD |
| `7D` | `0.1013` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 12,870.00 USD | 4,030.00 USD | 3,080.00 USD |
| `1D` | `0.1015` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 2,790.00 USD | 0.00 USD | 2,870.00 USD |
| `7D` | `0.1015` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 6,830.00 USD | 965.35 USD | 2,430.00 USD |
| `1D` | `0.1017` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 1,660.00 USD | 2,060.00 USD | 2,280.00 USD |
| `7D` | `0.1017` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 11,450.00 USD | 2,850.00 USD | 4,790.00 USD |
| `1D` | `0.1019` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 2,800.00 USD | 3,420.00 USD | 2,990.00 USD |
| `7D` | `0.1019` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 3,160.00 USD | 3,310.00 USD | 8,040.00 USD |
| `1D` | `0.1021` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 2,580.00 USD | 1,320.00 USD | 4,740.00 USD |
| `7D` | `0.1021` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 7,900.00 USD | 3,270.00 USD | 7,150.00 USD |
| `1D` | `0.1023` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 1,440.00 USD | 1,390.00 USD | 2,060.00 USD |
| `7D` | `0.1023` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 4,030.00 USD | 4,990.00 USD | 11,010.00 USD |
| `1D` | `0.1025` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 855.19 USD | 947.50 USD | 2,750.00 USD |
| `7D` | `0.1025` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 1,550.00 USD | 0.00 USD | 5,690.00 USD |
| `1D` | `0.1027` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 2,780.00 USD | 1,590.00 USD | 73.56 USD |
| `7D` | `0.1027` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 2,250.00 USD | 1,170.00 USD | 344.47 USD |
| `1D` | `0.1029` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 4,340.00 USD | 705.79 USD | 6,460.00 USD |
| `7D` | `0.1029` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 7,420.00 USD | 3,000.00 USD | 332.49 USD |
| `1D` | `0.1031` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 11,600.00 USD | 3,910.00 USD | 8,060.00 USD |
| `7D` | `0.1031` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 13,690.00 USD | 5,070.00 USD | 10,680.00 USD |
| `1D` | `0.1033` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 8,760.00 USD | 2,790.00 USD | 10,510.00 USD |
| `7D` | `0.1033` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 3,880.00 USD | 2,640.00 USD | 15,240.00 USD |
| `1D` | `0.1035` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 7,450.00 USD | 6,850.00 USD | 10,230.00 USD |
| `7D` | `0.1035` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 2,710.00 USD | 9,400.00 USD | 16,150.00 USD |
| `1D` | `0.1037` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 2,220.00 USD | 13,000.00 USD | 9,240.00 USD |
| `7D` | `0.1037` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 19,390.00 USD |
| `1D` | `0.1039` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 3,660.00 USD | 1,730.00 USD | 11,820.00 USD |
| `7D` | `0.1039` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 0.00 USD | 5,170.00 USD | 167.04 USD |
| `1D` | `0.1041` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 7,790.00 USD | 6,910.00 USD | 13,280.00 USD |
| `7D` | `0.1041` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 5,940.00 USD | 2,910.00 USD | 10,820.00 USD |
| `1D` | `0.1043` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 17,650.00 USD | 5,650.00 USD | 7,840.00 USD |
| `7D` | `0.1043` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 15,960.00 USD | 5,980.00 USD | 21,000.00 USD |
| `1D` | `0.1045` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | 2,600.00 USD | 6,220.00 USD |
| `7D` | `0.1045` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 0.00 USD | 3,830.00 USD | 14,950.00 USD |
| `1D` | `0.1047` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 4,610.00 USD | 2,610.00 USD | 21,540.00 USD |
| `7D` | `0.1047` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 0.00 USD | 1,720.00 USD | 22,630.00 USD |
| `1D` | `0.1049` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 21,050.00 USD | 4,090.00 USD | 10,940.00 USD |
| `7D` | `0.1049` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 34,790.00 USD | 4,810.00 USD | 35,410.00 USD |
| `1D` | `0.1051` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 20,120.00 USD | 10,840.00 USD | 26,370.00 USD |
| `7D` | `0.1051` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 17,290.00 USD | 11,500.00 USD | 48,700.00 USD |
| `1D` | `0.1053` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 41,820.00 USD | 8,170.00 USD | 29,580.00 USD |
| `7D` | `0.1053` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 47,580.00 USD | 29,800.00 USD | 95,610.00 USD |
| `1D` | `0.1055` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 28,290.00 USD | 21,140.00 USD | 35,070.00 USD |
| `7D` | `0.1055` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 50,090.00 USD | 27,290.00 USD | 122,170.00 USD |
| `1D` | `0.1057` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 26,000.00 USD | 26,820.00 USD | 46,300.00 USD |
| `7D` | `0.1057` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 44,200.00 USD | 43,030.00 USD | 74,290.00 USD |
| `1D` | `0.1059` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 17,220.00 USD | 21,420.00 USD | 55,440.00 USD |
| `7D` | `0.1059` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 92,510.00 USD | 49,670.00 USD | 116,360.00 USD |
| `1D` | `0.1061` | 958,950.00 USD | 0.00 USD | 958,950.00 USD | 15,660.00 USD | 9,870.00 USD | 51,490.00 USD |
| `7D` | `0.1061` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 38,260.00 USD | 28,780.00 USD | 76,320.00 USD |
| `1D` | `0.1063` | 881,930.00 USD | 0.00 USD | 881,930.00 USD | 57,650.00 USD | 16,340.00 USD | 53,520.00 USD |
| `7D` | `0.1063` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 95,080.00 USD | 38,330.00 USD | 151,610.00 USD |
| `1D` | `0.1065` | 754,430.00 USD | 0.00 USD | 754,430.00 USD | 19,500.00 USD | 15,700.00 USD | 13,400.00 USD |
| `7D` | `0.1065` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 84,890.00 USD | 21,040.00 USD | 86,060.00 USD |
| `1D` | `0.1067` | 705,830.00 USD | 0.00 USD | 705,830.00 USD | 16,020.00 USD | 14,530.00 USD | 23,940.00 USD |
| `7D` | `0.1067` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 97,290.00 USD | 34,000.00 USD | 67,490.00 USD |
| `1D` | `0.1069` | 651,340.00 USD | 0.00 USD | 651,340.00 USD | 20,560.00 USD | 6,620.00 USD | 54,820.00 USD |
| `7D` | `0.1069` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 76,900.00 USD | 32,620.00 USD | 67,520.00 USD |
| `1D` | `0.1071` | 569,340.00 USD | 0.00 USD | 569,340.00 USD | 48,660.00 USD | 8,170.00 USD | 16,200.00 USD |
| `7D` | `0.1071` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 119,440.00 USD | 27,240.00 USD | 42,730.00 USD |
| `1D` | `0.1073` | 496,310.00 USD | 0.00 USD | 496,310.00 USD | 8,740.00 USD | 10,680.00 USD | 20,870.00 USD |
| `7D` | `0.1073` | 840,080.00 USD | 0.00 USD | 840,080.00 USD | 62,850.00 USD | 17,700.00 USD | 0.00 USD |
| `1D` | `0.1075` | 456,030.00 USD | 0.00 USD | 456,030.00 USD | 11,540.00 USD | 3,900.00 USD | 0.00 USD |
| `7D` | `0.1075` | 759,530.00 USD | 0.00 USD | 759,530.00 USD | 8,720.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1077` | 440,590.00 USD | 0.00 USD | 440,590.00 USD | 3,180.00 USD | 6,210.00 USD | 10,820.00 USD |
| `1D` | `0.1079` | 420,370.00 USD | 0.00 USD | 420,370.00 USD | 9,370.00 USD | 11,900.00 USD | 23,460.00 USD |
| `7D` | `0.1079` | 750,810.00 USD | 0.00 USD | 750,810.00 USD | 123,150.00 USD | 18,520.00 USD | 0.00 USD |
| `1D` | `0.1081` | 375,640.00 USD | 0.00 USD | 375,640.00 USD | 5,870.00 USD | 7,210.00 USD | 46,940.00 USD |
| `7D` | `0.1081` | 609,130.00 USD | 0.00 USD | 609,130.00 USD | 200,110.00 USD | 9,430.00 USD | 28,830.00 USD |
| `1D` | `0.1083` | 315,620.00 USD | 0.00 USD | 315,620.00 USD | 30,270.00 USD | 0.00 USD | 27,290.00 USD |
| `7D` | `0.1083` | 370,770.00 USD | 0.00 USD | 370,770.00 USD | 94,800.00 USD | 0.00 USD | 37,550.00 USD |
| `1D` | `0.1085` | 258,060.00 USD | 0.00 USD | 258,060.00 USD | 14,370.00 USD | 7,490.00 USD | 47,130.00 USD |
| `7D` | `0.1085` | 238,420.00 USD | 0.00 USD | 238,420.00 USD | 15,920.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1087` | 189,070.00 USD | 0.00 USD | 189,070.00 USD | 15,310.00 USD | 6,720.00 USD | 22,870.00 USD |
| `7D` | `0.1087` | 222,500.00 USD | 0.00 USD | 222,500.00 USD | 22,680.00 USD | 0.00 USD | 27,780.00 USD |
| `1D` | `0.1089` | 144,170.00 USD | 0.00 USD | 144,170.00 USD | 41,340.00 USD | 12,040.00 USD | 18,070.00 USD |
| `7D` | `0.1089` | 172,040.00 USD | 0.00 USD | 172,040.00 USD | 0.00 USD | 9,110.00 USD | 0.00 USD |
| `1D` | `0.1091` | 72,720.00 USD | 0.00 USD | 72,720.00 USD | 16,940.00 USD | 2,790.00 USD | 0.00 USD |
| `7D` | `0.1091` | 162,920.00 USD | 0.00 USD | 162,920.00 USD | 16,310.00 USD | 3,800.00 USD | 0.00 USD |
| `1D` | `0.1093` | 52,990.00 USD | 0.00 USD | 52,990.00 USD | 13,100.00 USD | 0.00 USD | 6,220.00 USD |
| `7D` | `0.1095` | 142,820.00 USD | 0.00 USD | 142,820.00 USD | 18,840.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1097` | 123,980.00 USD | 0.00 USD | 123,980.00 USD | 0.00 USD | 2,970.00 USD | 21,590.00 USD |
| `7D` | `0.1099` | 99,410.00 USD | 0.00 USD | 99,410.00 USD | 0.00 USD | 0.00 USD | 25,060.00 USD |
| `7D` | `0.1103` | 74,350.00 USD | 0.00 USD | 74,350.00 USD | 6,930.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1105` | 67,420.00 USD | 0.00 USD | 67,420.00 USD | 0.00 USD | 5,810.00 USD | 0.00 USD |
| `7D` | `0.1107` | 61,610.00 USD | 0.00 USD | 61,610.00 USD | 0.00 USD | 4,120.00 USD | 0.00 USD |
| `1D` | `0.1113` | 33,670.00 USD | 0.00 USD | 33,670.00 USD | 0.00 USD | 8,100.00 USD | 25,570.00 USD |
| `7D` | `0.1113` | 57,490.00 USD | 0.00 USD | 57,490.00 USD | 0.00 USD | 0.00 USD | 57,490.00 USD |
| `7D` | `0.1114` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1115` | 36,130.00 USD | 36,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 36,130.00 USD |
| `1D` | `0.1116` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1117` | 32,500.00 USD | 32,500.00 USD | 0.00 USD | 0.00 USD | 16,900.00 USD | 15,610.00 USD |
| `7D` | `0.1117` | 82,480.00 USD | 82,480.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | 23,580.00 USD |
| `1D` | `0.1119` | 102,900.00 USD | 102,900.00 USD | 0.00 USD | 35,630.00 USD | 7,980.00 USD | 26,780.00 USD |
| `7D` | `0.1119` | 141,140.00 USD | 141,140.00 USD | 0.00 USD | 45,230.00 USD | 2,640.00 USD | 10,800.00 USD |
| `1D` | `0.1121` | 165,970.00 USD | 165,970.00 USD | 0.00 USD | 19,830.00 USD | 16,100.00 USD | 27,140.00 USD |
| `7D` | `0.1121` | 192,410.00 USD | 192,410.00 USD | 0.00 USD | 29,340.00 USD | 9,400.00 USD | 12,530.00 USD |
| `1D` | `0.1123` | 270,830.00 USD | 270,830.00 USD | 0.00 USD | 29,460.00 USD | 26,020.00 USD | 49,380.00 USD |
| `7D` | `0.1123` | 285,790.00 USD | 285,790.00 USD | 0.00 USD | 48,680.00 USD | 18,520.00 USD | 26,180.00 USD |
| `1D` | `0.1125` | 366,810.00 USD | 366,810.00 USD | 0.00 USD | 17,260.00 USD | 13,480.00 USD | 65,240.00 USD |
| `7D` | `0.1125` | 336,770.00 USD | 336,770.00 USD | 0.00 USD | 7,560.00 USD | 14,600.00 USD | 28,830.00 USD |
| `1D` | `0.1127` | 443,580.00 USD | 443,580.00 USD | 0.00 USD | 21,670.00 USD | 10,390.00 USD | 44,720.00 USD |
| `7D` | `0.1127` | 391,130.00 USD | 391,130.00 USD | 0.00 USD | 0.00 USD | 6,460.00 USD | 47,890.00 USD |
| `1D` | `0.1129` | 543,680.00 USD | 543,680.00 USD | 0.00 USD | 32,030.00 USD | 13,140.00 USD | 54,940.00 USD |
| `7D` | `0.1129` | 449,170.00 USD | 449,170.00 USD | 0.00 USD | 31,880.00 USD | 5,980.00 USD | 20,180.00 USD |
| `1D` | `0.1131` | 593,730.00 USD | 593,730.00 USD | 0.00 USD | 15,310.00 USD | 9,680.00 USD | 25,050.00 USD |
| `7D` | `0.1131` | 505,890.00 USD | 505,890.00 USD | 0.00 USD | 22,680.00 USD | 0.00 USD | 34,030.00 USD |
| `1D` | `0.1133` | 641,090.00 USD | 641,090.00 USD | 0.00 USD | 5,610.00 USD | 17,490.00 USD | 24,270.00 USD |
| `7D` | `0.1133` | 518,900.00 USD | 518,900.00 USD | 0.00 USD | 0.00 USD | 12,940.00 USD | 68.72 USD |
| `1D` | `0.1135` | 690,290.00 USD | 690,290.00 USD | 0.00 USD | 27,280.00 USD | 5,410.00 USD | 16,510.00 USD |
| `7D` | `0.1135` | 571,370.00 USD | 571,370.00 USD | 0.00 USD | 32,150.00 USD | 5,520.00 USD | 14,800.00 USD |
| `1D` | `0.1137` | 744,050.00 USD | 744,050.00 USD | 0.00 USD | 34,150.00 USD | 2,430.00 USD | 17,180.00 USD |
| `7D` | `0.1137` | 608,700.00 USD | 608,700.00 USD | 0.00 USD | 30,030.00 USD | 1,730.00 USD | 5,570.00 USD |
| `1D` | `0.1139` | 776,850.00 USD | 776,850.00 USD | 0.00 USD | 10,000.00 USD | 9,360.00 USD | 13,450.00 USD |
| `7D` | `0.1139` | 625,800.00 USD | 625,800.00 USD | 0.00 USD | 0.00 USD | 8,850.00 USD | 8,250.00 USD |
| `1D` | `0.1141` | 799,060.00 USD | 799,060.00 USD | 0.00 USD | 8,780.00 USD | 5,920.00 USD | 7,500.00 USD |
| `7D` | `0.1141` | 643,100.00 USD | 643,100.00 USD | 0.00 USD | 4,360.00 USD | 5,280.00 USD | 7,660.00 USD |
| `1D` | `0.1143` | 816,770.00 USD | 816,770.00 USD | 0.00 USD | 1,590.00 USD | 7,740.00 USD | 8,380.00 USD |
| `7D` | `0.1143` | 717,380.00 USD | 717,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 74,280.00 USD |
| `1D` | `0.1145` | 863,730.00 USD | 863,730.00 USD | 0.00 USD | 8,350.00 USD | 10,790.00 USD | 27,820.00 USD |
| `7D` | `0.1145` | 878,170.00 USD | 878,170.00 USD | 0.00 USD | 10,360.00 USD | 9,260.00 USD | 141,160.00 USD |
| `1D` | `0.1147` | 904,140.00 USD | 904,140.00 USD | 0.00 USD | 8,840.00 USD | 4,840.00 USD | 26,730.00 USD |
| `7D` | `0.1147` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 4,720.00 USD | 134,400.00 USD |
| `1D` | `0.1149` | 944,560.00 USD | 944,560.00 USD | 0.00 USD | 11,450.00 USD | 0.00 USD | 28,970.00 USD |
| `7D` | `0.1149` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 72,860.00 USD |
| `1D` | `0.1151` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 21,200.00 USD | 3,740.00 USD | 43,920.00 USD |
| `7D` | `0.1151` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 92,570.00 USD | 0.00 USD | 118,840.00 USD |
| `1D` | `0.1153` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 30,050.00 USD | 15,960.00 USD | 26,300.00 USD |
| `7D` | `0.1153` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 147,450.00 USD | 0.00 USD | 132,290.00 USD |
| `1D` | `0.1155` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 18,450.00 USD | 26,450.00 USD | 28,590.00 USD |
| `7D` | `0.1155` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 108,940.00 USD | 24,970.00 USD | 71,140.00 USD |
| `1D` | `0.1157` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 29,940.00 USD | 11,110.00 USD | 35,640.00 USD |
| `7D` | `0.1157` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 163,490.00 USD | 3,760.00 USD | 48,220.00 USD |
| `1D` | `0.1159` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 7,810.00 USD | 8,370.00 USD | 8,850.00 USD |
| `7D` | `0.1159` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 105,000.00 USD | 12,710.00 USD | 48,790.00 USD |
| `1D` | `0.1161` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 25,800.00 USD | 6,970.00 USD | 33,890.00 USD |
| `7D` | `0.1161` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 155,210.00 USD | 37,250.00 USD | 82,510.00 USD |
| `1D` | `0.1163` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 18,210.00 USD | 6,750.00 USD | 1,990.00 USD |
| `7D` | `0.1163` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 74,250.00 USD | 11,460.00 USD | 68,760.00 USD |
| `1D` | `0.1165` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 9,310.00 USD | 11,840.00 USD | 3,670.00 USD |
| `7D` | `0.1165` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 77,390.00 USD | 25,170.00 USD | 27,180.00 USD |
| `1D` | `0.1167` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 15,040.00 USD | 13,350.00 USD | 3,010.00 USD |
| `7D` | `0.1167` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 79,610.00 USD | 21,620.00 USD | 41,230.00 USD |
| `1D` | `0.1169` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 16,040.00 USD | 4,020.00 USD | 15,910.00 USD |
| `7D` | `0.1169` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 60,400.00 USD | 14,840.00 USD | 86,730.00 USD |
| `1D` | `0.1171` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 5,230.00 USD | 4,520.00 USD | 1,490.00 USD |
| `7D` | `0.1171` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 52,070.00 USD | 9,140.00 USD | 35,080.00 USD |
| `1D` | `0.1173` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 14,960.00 USD | 3,470.00 USD | 7,820.00 USD |
| `7D` | `0.1173` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 40,860.00 USD | 7,080.00 USD | 31,840.00 USD |
| `1D` | `0.1175` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 9,050.00 USD | 10,790.00 USD | 6,450.00 USD |
| `7D` | `0.1175` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 38,840.00 USD | 8,100.00 USD | 58,660.00 USD |
| `1D` | `0.1177` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 7,820.00 USD | 8,560.00 USD | 8,530.00 USD |
| `7D` | `0.1177` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 13,120.00 USD | 14,140.00 USD | 27,040.00 USD |
| `1D` | `0.1179` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 17,010.00 USD | 5,840.00 USD | 14,500.00 USD |
| `7D` | `0.1179` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 61,380.00 USD | 10,940.00 USD | 23,410.00 USD |
| `1D` | `0.1181` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 5,740.00 USD | 4,210.00 USD | 6,940.00 USD |
| `7D` | `0.1181` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 22,290.00 USD | 15,780.00 USD | 17,730.00 USD |
| `1D` | `0.1183` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 7,310.00 USD | 1,400.00 USD | 9,080.00 USD |
| `7D` | `0.1183` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 4,040.00 USD | 1,800.00 USD | 30,890.00 USD |
| `1D` | `0.1185` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 6,370.00 USD | 3,940.00 USD | 11,100.00 USD |
| `7D` | `0.1185` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 3,880.00 USD | 5,130.00 USD | 22,270.00 USD |
| `1D` | `0.1187` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 11,520.00 USD | 8,520.00 USD | 6,250.00 USD |
| `7D` | `0.1187` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 5,620.00 USD | 11,840.00 USD | 32,090.00 USD |
| `1D` | `0.1189` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 4,220.00 USD | 3,060.00 USD | 4,330.00 USD |
| `7D` | `0.1189` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 27,240.00 USD | 15,060.00 USD | 3,180.00 USD |
| `1D` | `0.1191` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 4,940.00 USD | 6,690.00 USD | 3,460.00 USD |
| `7D` | `0.1191` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 22,650.00 USD | 15,330.00 USD | 109,070.00 USD |
| `1D` | `0.1193` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 4,720.00 USD | 2,080.00 USD | 3,770.00 USD |
| `7D` | `0.1193` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 21,260.00 USD | 0.00 USD | 9,460.00 USD |
| `1D` | `0.1195` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 9,550.00 USD | 3,210.00 USD | 2,730.00 USD |
| `7D` | `0.1195` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 11,190.00 USD | 1,780.00 USD | 29,460.00 USD |
| `1D` | `0.1197` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 1,040.00 USD | 13.79 USD |
| `7D` | `0.1197` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 6,780.00 USD | 10,800.00 USD | 14,060.00 USD |
| `1D` | `0.1199` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 3,050.00 USD | 3,040.00 USD |
| `7D` | `0.1199` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 9,100.00 USD | 0.00 USD | 64,660.00 USD |
| `1D` | `0.1201` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 6,460.00 USD | 1,070.00 USD | 10,160.00 USD |
| `7D` | `0.1201` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 114,140.00 USD | 16,380.00 USD | 29,030.00 USD |
| `1D` | `0.1203` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 7,150.00 USD | 1,250.00 USD | 2,680.00 USD |
| `7D` | `0.1203` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 70,770.00 USD | 29,250.00 USD | 6,330.00 USD |
| `1D` | `0.1205` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 2,250.00 USD | 1,910.00 USD | 759.49 USD |
| `7D` | `0.1205` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 86,480.00 USD | 48,720.00 USD | 128,340.00 USD |
| `1D` | `0.1207` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 9,520.00 USD | 524.23 USD | 4,880.00 USD |
| `7D` | `0.1207` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 12,460.00 USD | 19,400.00 USD | 59,650.00 USD |
| `1D` | `0.1209` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 2,350.00 USD | 3,330.00 USD | 2,870.00 USD |
| `7D` | `0.1209` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 85,160.00 USD | 19,340.00 USD | 94,120.00 USD |
| `1D` | `0.1211` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 4,350.00 USD | 4,220.00 USD | 4,460.00 USD |
| `7D` | `0.1211` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 35,090.00 USD | 18,720.00 USD | 29,580.00 USD |
| `1D` | `0.1213` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 2,360.00 USD | 1,220.00 USD | 11,780.00 USD |
| `7D` | `0.1213` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 32,700.00 USD | 29,060.00 USD | 24,230.00 USD |
| `1D` | `0.1215` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD | 4,180.00 USD |
| `7D` | `0.1215` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 27,750.00 USD | 9,240.00 USD | 59,120.00 USD |
| `1D` | `0.1217` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 1,330.00 USD | 624.33 USD | 8,180.00 USD |
| `7D` | `0.1217` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 18,490.00 USD | 26,300.00 USD | 11,210.00 USD |
| `1D` | `0.1219` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 5,070.00 USD | 1,410.00 USD | 9,320.00 USD |
| `7D` | `0.1219` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 26,700.00 USD | 5,500.00 USD | 35,080.00 USD |
| `1D` | `0.1221` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 4,590.00 USD | 4,070.00 USD | 1,620.00 USD |
| `7D` | `0.1221` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 47,890.00 USD | 21,770.00 USD | 18,920.00 USD |
| `1D` | `0.1223` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 4,190.00 USD | 668.73 USD | 6,120.00 USD |
| `7D` | `0.1223` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 103,180.00 USD | 36,290.00 USD | 48,470.00 USD |
| `1D` | `0.1225` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1225` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 50,540.00 USD | 26,800.00 USD | 10,780.00 USD |
| `1D` | `0.1227` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1227` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 75,750.00 USD | 31,790.00 USD | 58,740.00 USD |
| `1D` | `0.1229` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 403.62 USD | 0.00 USD |
| `7D` | `0.1229` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 87,270.00 USD | 41,310.00 USD | 50,470.00 USD |
| `1D` | `0.1231` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 430.11 USD | 789.22 USD |
| `7D` | `0.1231` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 29,380.00 USD | 31,660.00 USD | 30,200.00 USD |
| `1D` | `0.1232` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 842.63 USD | 0.00 USD |
| `7D` | `0.1233` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 65,180.00 USD | 12,850.00 USD | 39,960.00 USD |
| `7D` | `0.1234` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 8,540.00 USD | 5,200.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `75.49M` | Total OI Tokens: `678,330,540.3 OP`
  * 1h OI Change: `+1.83%` | 4h OI Change: `+3.16%` | 24h OI Change: `-1.83%`
  * Exchange Breakdown: Binance=`17.19M` | Bybit=`14.40M` | OKX=`4.31M` | Hyperliquid=`4.01M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.21K` | Last 24h: `-2.15K` | Last 3d: `-6.96K` | Last 7d: `-22.41K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0037%` | **USDT OKX** | `0.0052%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0036%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0139%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `48.59%` | `51.41%` | `0.95` | 11,690,000.00 USD |
| `15M` | `Binance` | `48.03%` | `51.97%` | `0.92` | 4,370,000.00 USD |
| `15M` | `OKX` | `45.62%` | `54.38%` | `0.84` | 1,480,000.00 USD |
| `15M` | `Bybit` | `44.23%` | `55.77%` | `0.79` | 1,370,000.00 USD |
| `15M` | `KuCoin` | `44.91%` | `55.09%` | `0.82` | 77,430.00 USD |
| `15M` | `Gate` | `71.08%` | `28.92%` | `2.46` | 170,510.00 USD |
| `15M` | `Bitget` | `61.77%` | `38.23%` | `1.62` | 776,430.00 USD |
| `15M` | `BingX` | `58.18%` | `41.82%` | `1.39` | 524,850.00 USD |
| `15M` | `MEXC` | `49.32%` | `50.68%` | `0.97` | 815,770.00 USD |
| `15M` | `Bitunix` | `54.75%` | `45.25%` | `1.21` | 263,360.00 USD |
| `15M` | `Hyperliquid` | `19.74%` | `80.26%` | `0.25` | 960,880.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.02%` | `50.98%` | `0.96` | 160,960.00 USD |
| `15M` | `Crypto.com` | `2.98%` | `97.02%` | `0.03` | 894.21 USD |
| `15M` | `WhiteBIT` | `78.91%` | `21.09%` | `3.74` | 608,560.00 USD |
| `15M` | `HTX` | `31.08%` | `68.92%` | `0.45` | 3,160.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `50.39%` | `49.61%` | `1.02` | 80,050.00 USD |
| `15M` | `Aster` | `87.2%` | `12.8%` | `6.81` | 10,330.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `69.31%` | `30.69%` | `2.26` | 26,140.00 USD |
| `15M` | `Whale Positions` | `48.03%` | `51.97%` | `0.92` | 4,370,000.00 USD |
| `15M` | `Global Accounts` | `48.59%` | `51.41%` | `0.95` | 11,690,000.00 USD |
| `1H` | `OP` | `48.74%` | `51.26%` | `0.95` | 105,400,000.00 USD |
| `1H` | `Binance` | `47.74%` | `52.26%` | `0.91` | 44,070,000.00 USD |
| `1H` | `OKX` | `49.09%` | `50.91%` | `0.96` | 15,990,000.00 USD |
| `1H` | `Bybit` | `50.11%` | `49.89%` | `1.00` | 14,790,000.00 USD |
| `1H` | `KuCoin` | `52.18%` | `47.82%` | `1.09` | 654,980.00 USD |
| `1H` | `Gate` | `45.8%` | `54.2%` | `0.85` | 1,490,000.00 USD |
| `1H` | `Bitget` | `52.93%` | `47.07%` | `1.12` | 5,690,000.00 USD |
| `1H` | `BingX` | `44.95%` | `55.05%` | `0.82` | 3,620,000.00 USD |
| `1H` | `MEXC` | `47.63%` | `52.37%` | `0.91` | 4,990,000.00 USD |
| `1H` | `Bitunix` | `49.16%` | `50.84%` | `0.97` | 3,050,000.00 USD |
| `1H` | `Hyperliquid` | `40.68%` | `59.32%` | `0.69` | 4,990,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.63%` | `52.37%` | `0.91` | 832,510.00 USD |
| `1H` | `Crypto.com` | `47.76%` | `52.24%` | `0.91` | 17,040.00 USD |
| `1H` | `WhiteBIT` | `68.96%` | `31.04%` | `2.22` | 2,630,000.00 USD |
| `1H` | `HTX` | `51.53%` | `48.47%` | `1.06` | 254,090.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `52.07%` | `47.93%` | `1.09` | 1,520,000.00 USD |
| `1H` | `Aster` | `49.96%` | `50.04%` | `1.00` | 31,510.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `44.44%` | `55.56%` | `0.80` | 783,090.00 USD |
| `1H` | `Whale Positions` | `47.74%` | `52.26%` | `0.91` | 44,070,000.00 USD |
| `1H` | `Global Accounts` | `48.74%` | `51.26%` | `0.95` | 105,400,000.00 USD |
| `4H` | `OP` | `50.58%` | `49.42%` | `1.02` | 305,880,000.00 USD |
| `4H` | `Binance` | `48.76%` | `51.24%` | `0.95` | 119,940,000.00 USD |
| `4H` | `OKX` | `50.54%` | `49.46%` | `1.02` | 43,230,000.00 USD |
| `4H` | `Bybit` | `50.37%` | `49.63%` | `1.01` | 39,860,000.00 USD |
| `4H` | `KuCoin` | `50.56%` | `49.44%` | `1.02` | 2,310,000.00 USD |
| `4H` | `Gate` | `49.81%` | `50.19%` | `0.99` | 4,900,000.00 USD |
| `4H` | `Bitget` | `49.55%` | `50.45%` | `0.98` | 15,710,000.00 USD |
| `4H` | `BingX` | `44.32%` | `55.68%` | `0.80` | 14,100,000.00 USD |
| `4H` | `MEXC` | `44.95%` | `55.05%` | `0.82` | 15,360,000.00 USD |
| `4H` | `Bitunix` | `48.83%` | `51.17%` | `0.95` | 10,200,000.00 USD |
| `4H` | `Hyperliquid` | `48.32%` | `51.68%` | `0.93` | 18,580,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.26%` | `49.74%` | `1.01` | 2,290,000.00 USD |
| `4H` | `Crypto.com` | `50.89%` | `49.11%` | `1.04` | 28,550.00 USD |
| `4H` | `WhiteBIT` | `86.12%` | `13.88%` | `6.20` | 9,900,000.00 USD |
| `4H` | `HTX` | `51.32%` | `48.68%` | `1.05` | 504,520.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `58.6%` | `41.4%` | `1.42` | 3,160,000.00 USD |
| `4H` | `Aster` | `90.41%` | `9.59%` | `9.43` | 2,750,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.8%` | `51.2%` | `0.95` | 3,060,000.00 USD |
| `4H` | `Whale Positions` | `48.76%` | `51.24%` | `0.95` | 119,940,000.00 USD |
| `4H` | `Global Accounts` | `50.58%` | `49.42%` | `1.02` | 305,880,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1102` | `0.1101` | `0.1102` | `0.1104` | `0.1098` | 211,329.98 USD | 98,190.43 USD | 113,139.54 USD | -14,949.11 USD | `-7.07%` | `6B / 13S` |
| `0:00 UTC` | `0.1094` | `0.1095` | `0.1094` | `0.1100` | `0.1093` | 411,857.05 USD | 168,352.47 USD | 243,504.58 USD | -75,152.12 USD | `-18.25%` | `7B / 12S` |
| `5:00 UTC` | `0.1097` | `0.1097` | `0.1097` | `0.1099` | `0.1095` | 231,727.41 USD | 134,913.35 USD | 96,814.06 USD | 38,099.28 USD | `+16.44%` | `11B / 4S` |
| `0:00 UTC` | `0.1100` | `0.1102` | `0.1100` | `0.1107` | `0.1097` | 522,440.60 USD | 292,430.01 USD | 230,010.59 USD | 62,419.42 USD | `+11.95%` | `25B / 7S` |
| `5:00 UTC` | `0.1105` | `0.1104` | `0.1105` | `0.1106` | `0.1101` | 269,695.80 USD | 148,564.64 USD | 121,131.16 USD | 27,433.48 USD | `+10.17%` | `14B / 11S` |
| `0:00 UTC` | `0.1112` | `0.1110` | `0.1112` | `0.1114` | `0.1105` | 559,599.22 USD | 273,423.88 USD | 286,175.34 USD | -12,751.46 USD | `-2.28%` | `16B / 12S` |
| `5:00 UTC` | `0.1108` | `0.1107` | `0.1108` | `0.1112` | `0.1104` | 411,261.97 USD | 229,894.15 USD | 181,367.82 USD | 48,526.33 USD | `+11.80%` | `24B / 9S` |
| `0:00 UTC` | `0.1107` | `0.1107` | `0.1107` | `0.1112` | `0.1103` | 551,290.91 USD | 307,591.69 USD | 243,699.23 USD | 63,892.46 USD | `+11.59%` | `17B / 5S` |
| `5:00 UTC` | `0.1110` | `0.1112` | `0.1110` | `0.1118` | `0.1108` | 510,110.63 USD | 294,926.48 USD | 215,184.15 USD | 79,742.32 USD | `+15.63%` | `19B / 5S` |
| `0:00 UTC` | `0.1110` | `0.1112` | `0.1110` | `0.1116` | `0.1109` | 277,464.97 USD | 150,217.56 USD | 127,247.41 USD | 22,970.16 USD | `+8.28%` | `16B / 8S` |

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
| `5m` | 59.89 USD | 369.04 USD | **`ACCUMULATION`** |
| `15m` | 8,020.00 USD | 120,150.00 USD | **`ACCUMULATION`** |
| `30m` | -16,380.00 USD | 261,590.00 USD | **`ACCUMULATION`** |
| `1h` | 19,260.00 USD | 326,730.00 USD | **`ACCUMULATION`** |
| `2h` | 98,020.00 USD | 495,500.00 USD | **`ACCUMULATION`** |
| `4h` | 120,530.00 USD | 542,020.00 USD | **`ACCUMULATION`** |
| `6h` | 130,190.00 USD | 717,270.00 USD | **`ACCUMULATION`** |
| `8h` | 135,390.00 USD | 899,210.00 USD | **`ACCUMULATION`** |
| `12h` | 98,710.00 USD | -436,670.00 USD | **`DISTRIBUTION`** |
| `24h` | 148,090.00 USD | -783,100.00 USD | **`DISTRIBUTION`** |
| `1w` | -323,650.00 USD | -10,660,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,860,000.00 USD | -79,930,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+59.89` | 15m=`+8.02K` | 1h=`+19.26K` | 24h=`+148.09K`
* Futures Capital Netflows: 5m=`+369.04` | 15m=`+120.15K` | 1h=`+326.73K` | 24h=`-783.10K`
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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
