# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-29 23:46:55 IST` (`2026-10-29 18:16:55 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1111` | `0.1113` | `0.1109` | `0.1111` | `924,520` | 102,737.62 USD | -26,558.97 USD | `-25.85%` | -866,997.09 USD | `-0.09` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1111` | `0.1111` | `0.1106` | `0.1110` | `384,825` | 42,664.79 USD | 12,025.17 USD | `+28.19%` | -854,971.92 USD | `+0.55` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1110` | `0.1111` | `0.1110` | `0.1111` | `15,854` | 1,761.00 USD | 681.05 USD | `+38.67%` | -854,290.87 USD | `+0.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1110` | `0.1112` | `0.1101` | `0.1112` | `8,308,770` | 919,895.36 USD | -39,685.74 USD | `-4.31%` | -928,272.20 USD | `-0.51` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1112` | `0.1113` | `0.1106` | `0.1110` | `2,352,924` | 261,230.00 USD | -13,482.93 USD | `-5.16%` | -941,755.13 USD | `-0.17` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1110` | `0.1111` | `0.1110` | `0.1111` | `17,775` | 1,974.45 USD | 894.49 USD | `+45.30%` | -940,860.64 USD | `+0.05` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.1140` | `0.1148` | `0.1126` | `0.1129` | `21,471,756` | 2,437,488.22 USD | -123,745.56 USD | `-5.08%` | -700,951.75 USD | `-0.29` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1129` | `0.1132` | `0.1101` | `0.1112` | `18,847,741` | 2,100,824.13 USD | -168,750.74 USD | `-8.03%` | -869,702.50 USD | `-0.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1112` | `0.1113` | `0.1106` | `0.1111` | `2,370,700` | 263,204.45 USD | -12,588.44 USD | `-4.78%` | -882,290.93 USD | `+0.22` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,229,700.44 USD | `+0.64` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -888,444.84 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1101` | `0.1111` | `42,690,196` | 4,801,516.80 USD | -305,084.75 USD | `-6.35%` | -1,193,529.59 USD | `-0.17` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1131` | `0.1136` | `0.1072` | `0.1085` | `76,338,549` | 8,353,905.81 USD | -1,528,374.61 USD | `-18.30%` | -1,480,991.26 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1085` | `0.1106` | `0.1071` | `0.1076` | `47,048,931` | 5,111,570.05 USD | 108,567.99 USD | `+2.12%` | -1,372,423.27 USD | `+0.75` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,229,700.44 USD | `+0.64` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -888,444.84 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1101` | `0.1111` | `42,690,196` | 4,801,516.80 USD | -305,084.75 USD | `-6.35%` | -1,193,529.59 USD | `-0.17` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:45:33 IST` |

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
| `7D` | `Long Liquidation` | `0.0967` | 4,080,000.00 USD | 4,080,000.00 USD | 3,770.00 USD | 2,660.00 USD | 2,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0969` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 2,810.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 2,000.00 USD | 34.36 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0973` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0975` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 1,160.00 USD | 4,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0975` | 12,670.00 USD | 51,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0977` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 5,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0979` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 1,530.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0981` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 4,020,000.00 USD | 4,020,000.00 USD | 7,990.00 USD | 1,230.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0985` | 4,010,000.00 USD | 4,010,000.00 USD | 7,110.00 USD | 0.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0985` | 19,960.00 USD | 38,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0987` | 3,990,000.00 USD | 3,990,000.00 USD | 5,390.00 USD | 9,190.00 USD | 37,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0989` | 2,030,000.00 USD | 2,030,000.00 USD | 3,060.00 USD | 1,370.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 3,940,000.00 USD | 3,940,000.00 USD | 12,260.00 USD | 4,520.00 USD | 27,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0991` | 2,020,000.00 USD | 2,020,000.00 USD | 3,340.00 USD | 2,600.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0991` | 3,900,000.00 USD | 3,900,000.00 USD | 14,350.00 USD | 10,350.00 USD | 13,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0993` | 2,010,000.00 USD | 2,010,000.00 USD | 1,550.00 USD | 1,220.00 USD | 10,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0993` | 3,860,000.00 USD | 3,860,000.00 USD | 23,920.00 USD | 10,140.00 USD | 24,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0995` | 2,000,000.00 USD | 2,000,000.00 USD | 4,080.00 USD | 624.33 USD | 11,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 3,800,000.00 USD | 3,800,000.00 USD | 13,090.00 USD | 6,160.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0997` | 1,980,000.00 USD | 1,980,000.00 USD | 2,320.00 USD | 718.82 USD | 10,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0997` | 3,760,000.00 USD | 3,760,000.00 USD | 21,100.00 USD | 5,500.00 USD | 32,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0999` | 1,970,000.00 USD | 1,970,000.00 USD | 4,680.00 USD | 2,940.00 USD | 3,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0999` | 3,700,000.00 USD | 3,700,000.00 USD | 14,230.00 USD | 6,540.00 USD | 18,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1001` | 1,960,000.00 USD | 1,960,000.00 USD | 4,190.00 USD | 1,410.00 USD | 7,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 3,660,000.00 USD | 3,660,000.00 USD | 29,230.00 USD | 3,010.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1003` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 558.39 USD | 30.31 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1003` | 3,610,000.00 USD | 3,610,000.00 USD | 8,010.00 USD | 7,060.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1005` | 1,950,000.00 USD | 1,950,000.00 USD | 1,970.00 USD | 403.62 USD | 1,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1005` | 3,590,000.00 USD | 3,590,000.00 USD | 25,070.00 USD | 11,000.00 USD | 18,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1005` | 427.25 USD | 18,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1007` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 430.11 USD | 827.99 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 3,540,000.00 USD | 3,540,000.00 USD | 10,260.00 USD | 2,280.00 USD | 14,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1009` | 1,940,000.00 USD | 1,940,000.00 USD | 2,320.00 USD | 3,210.00 USD | 59.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1009` | 3,510,000.00 USD | 3,510,000.00 USD | 15,320.00 USD | 3,070.00 USD | 6,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1011` | 1,940,000.00 USD | 1,940,000.00 USD | 1,570.00 USD | 1,240.00 USD | 3,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1011` | 3,490,000.00 USD | 3,490,000.00 USD | 4,430.00 USD | 4,720.00 USD | 8,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1013` | 1,930,000.00 USD | 1,930,000.00 USD | 4,900.00 USD | 2,290.00 USD | 629.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 3,470,000.00 USD | 3,470,000.00 USD | 12,870.00 USD | 4,030.00 USD | 3,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1015` | 1,920,000.00 USD | 1,920,000.00 USD | 2,790.00 USD | 1,830.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1015` | 3,450,000.00 USD | 3,450,000.00 USD | 6,830.00 USD | 965.35 USD | 2,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1015` | 622.37 USD | 17,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1017` | 1,910,000.00 USD | 1,910,000.00 USD | 1,660.00 USD | 4,600.00 USD | 7,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1017` | 3,440,000.00 USD | 3,440,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1019` | 1,900,000.00 USD | 1,900,000.00 USD | 6,600.00 USD | 3,420.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1019` | 3,420,000.00 USD | 3,420,000.00 USD | 9,260.00 USD | 5,790.00 USD | 12,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1021` | 1,880,000.00 USD | 1,880,000.00 USD | 2,580.00 USD | 1,320.00 USD | 4,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1021` | 3,390,000.00 USD | 3,390,000.00 USD | 7,900.00 USD | 3,270.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1023` | 1,870,000.00 USD | 1,870,000.00 USD | 4,600.00 USD | 2,120.00 USD | 4,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1023` | 3,370,000.00 USD | 3,370,000.00 USD | 4,030.00 USD | 4,990.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1025` | 1,860,000.00 USD | 1,860,000.00 USD | 855.19 USD | 2,500.00 USD | 3,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1025` | 3,350,000.00 USD | 3,350,000.00 USD | 1,550.00 USD | 0.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1025` | 17,360.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1027` | 1,860,000.00 USD | 1,860,000.00 USD | 2,780.00 USD | 1,590.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1027` | 3,340,000.00 USD | 3,340,000.00 USD | 2,250.00 USD | 2,580.00 USD | 359.07 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1029` | 1,850,000.00 USD | 1,850,000.00 USD | 4,340.00 USD | 705.79 USD | 6,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1029` | 3,340,000.00 USD | 3,340,000.00 USD | 7,420.00 USD | 3,000.00 USD | 332.49 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1031` | 1,840,000.00 USD | 1,840,000.00 USD | 11,600.00 USD | 3,910.00 USD | 8,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1031` | 3,320,000.00 USD | 3,320,000.00 USD | 13,690.00 USD | 5,070.00 USD | 10,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1033` | 1,810,000.00 USD | 1,810,000.00 USD | 8,760.00 USD | 2,790.00 USD | 10,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1033` | 3,300,000.00 USD | 3,300,000.00 USD | 3,880.00 USD | 2,640.00 USD | 15,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1035` | 1,790,000.00 USD | 1,790,000.00 USD | 7,450.00 USD | 6,850.00 USD | 10,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1035` | 3,270,000.00 USD | 3,270,000.00 USD | 2,710.00 USD | 9,400.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1037` | 1,770,000.00 USD | 1,770,000.00 USD | 2,220.00 USD | 13,000.00 USD | 9,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1037` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 19,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1039` | 1,740,000.00 USD | 1,740,000.00 USD | 3,660.00 USD | 1,730.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1039` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 5,170.00 USD | 167.04 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1041` | 1,730,000.00 USD | 1,730,000.00 USD | 7,790.00 USD | 6,910.00 USD | 13,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1041` | 3,220,000.00 USD | 3,220,000.00 USD | 5,940.00 USD | 2,910.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1043` | 1,700,000.00 USD | 1,700,000.00 USD | 17,650.00 USD | 5,650.00 USD | 7,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1043` | 3,200,000.00 USD | 3,200,000.00 USD | 15,960.00 USD | 5,980.00 USD | 21,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1045` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 2,600.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1045` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 3,830.00 USD | 15,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1047` | 1,660,000.00 USD | 1,660,000.00 USD | 4,610.00 USD | 2,610.00 USD | 16,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1047` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 1,720.00 USD | 22,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1049` | 1,630,000.00 USD | 1,630,000.00 USD | 21,050.00 USD | 2,430.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1049` | 3,110,000.00 USD | 3,110,000.00 USD | 34,790.00 USD | 4,810.00 USD | 35,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1051` | 1,600,000.00 USD | 1,600,000.00 USD | 16,410.00 USD | 8,750.00 USD | 24,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1051` | 3,040,000.00 USD | 3,040,000.00 USD | 17,290.00 USD | 11,500.00 USD | 48,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1053` | 1,550,000.00 USD | 1,550,000.00 USD | 25,850.00 USD | 7,040.00 USD | 19,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1053` | 2,960,000.00 USD | 2,960,000.00 USD | 47,580.00 USD | 29,800.00 USD | 95,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1055` | 1,500,000.00 USD | 1,500,000.00 USD | 21,850.00 USD | 15,910.00 USD | 31,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1055` | 2,790,000.00 USD | 2,790,000.00 USD | 50,090.00 USD | 27,290.00 USD | 122,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1057` | 1,430,000.00 USD | 1,430,000.00 USD | 21,550.00 USD | 21,720.00 USD | 42,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1057` | 2,590,000.00 USD | 2,590,000.00 USD | 44,200.00 USD | 43,030.00 USD | 74,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1059` | 1,340,000.00 USD | 1,340,000.00 USD | 15,180.00 USD | 21,000.00 USD | 52,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1059` | 2,430,000.00 USD | 2,430,000.00 USD | 92,510.00 USD | 49,670.00 USD | 114,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1061` | 1,250,000.00 USD | 1,250,000.00 USD | 15,660.00 USD | 9,870.00 USD | 51,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1061` | 2,170,000.00 USD | 2,170,000.00 USD | 38,260.00 USD | 28,040.00 USD | 76,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1063` | 1,180,000.00 USD | 1,180,000.00 USD | 56,400.00 USD | 14,600.00 USD | 51,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1063` | 2,030,000.00 USD | 2,030,000.00 USD | 88,520.00 USD | 38,330.00 USD | 148,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1065` | 1,050,000.00 USD | 1,050,000.00 USD | 16,250.00 USD | 13,370.00 USD | 19,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1065` | 1,750,000.00 USD | 1,750,000.00 USD | 91,170.00 USD | 21,040.00 USD | 93,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1067` | 1,010,000.00 USD | 1,010,000.00 USD | 13,530.00 USD | 15,160.00 USD | 33,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1067` | 1,550,000.00 USD | 1,550,000.00 USD | 97,290.00 USD | 36,720.00 USD | 67,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1069` | 943,830.00 USD | 943,830.00 USD | 24,070.00 USD | 7,520.00 USD | 43,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1069` | 1,350,000.00 USD | 1,350,000.00 USD | 76,900.00 USD | 32,620.00 USD | 72,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1071` | 868,920.00 USD | 868,920.00 USD | 48,660.00 USD | 4,860.00 USD | 18,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1071` | 1,160,000.00 USD | 1,160,000.00 USD | 119,440.00 USD | 27,240.00 USD | 42,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1073` | 796,460.00 USD | 796,460.00 USD | 8,740.00 USD | 10,680.00 USD | 20,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1073` | 975,370.00 USD | 975,370.00 USD | 58,480.00 USD | 17,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1075` | 756,170.00 USD | 756,170.00 USD | 16,520.00 USD | 6,770.00 USD | 1,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1075` | 899,190.00 USD | 899,190.00 USD | 8,720.00 USD | 3,500.00 USD | 58.62 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1077` | 731,020.00 USD | 731,020.00 USD | 3,180.00 USD | 10,810.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1079` | 703,040.00 USD | 703,040.00 USD | 9,370.00 USD | 13,900.00 USD | 25,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1079` | 886,900.00 USD | 886,900.00 USD | 128,090.00 USD | 18,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1081` | 654,030.00 USD | 654,030.00 USD | 17,730.00 USD | 7,210.00 USD | 50,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1081` | 740,290.00 USD | 740,290.00 USD | 205,390.00 USD | 11,660.00 USD | 28,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1083` | 579,090.00 USD | 579,090.00 USD | 30,270.00 USD | 5,440.00 USD | 33,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1083` | 494,380.00 USD | 494,380.00 USD | 94,800.00 USD | 2,110.00 USD | 42,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1085` | 509,530.00 USD | 509,530.00 USD | 22,270.00 USD | 13,850.00 USD | 65,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1085` | 355,070.00 USD | 355,070.00 USD | 15,920.00 USD | 4,200.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1087` | 408,400.00 USD | 408,400.00 USD | 40,320.00 USD | 6,720.00 USD | 44,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1087` | 334,920.00 USD | 334,920.00 USD | 55,430.00 USD | 6,210.00 USD | 60,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1089` | 316,690.00 USD | 316,690.00 USD | 38,530.00 USD | 17,080.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1089` | 213,210.00 USD | 213,210.00 USD | 5,290.00 USD | 14,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1091` | 219,550.00 USD | 219,550.00 USD | 33,700.00 USD | 6,410.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1091` | 193,350.00 USD | 193,350.00 USD | 16,310.00 USD | 3,800.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1093` | 171,260.00 USD | 171,260.00 USD | 15,480.00 USD | 3,890.00 USD | 8,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1093` | 164,240.00 USD | 164,240.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1095` | 143,390.00 USD | 143,390.00 USD | 0.00 USD | 0.00 USD | 10,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1095` | 155,510.00 USD | 155,510.00 USD | 18,840.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1097` | 132,530.00 USD | 132,530.00 USD | 0.00 USD | 0.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1097` | 133,140.00 USD | 133,140.00 USD | 0.00 USD | 2,970.00 USD | 21,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1099` | 128,860.00 USD | 128,860.00 USD | 9,980.00 USD | 14,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1099` | 108,570.00 USD | 108,570.00 USD | 0.00 USD | 7,010.00 USD | 25,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1101` | 103,960.00 USD | 103,960.00 USD | 0.00 USD | 0.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1103` | 93,140.00 USD | 93,140.00 USD | 23,720.00 USD | 4,000.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1103` | 76,500.00 USD | 76,500.00 USD | 27,370.00 USD | 4,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1105` | 59,340.00 USD | 59,340.00 USD | 0.00 USD | 10,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1105` | 44,680.00 USD | 44,680.00 USD | 0.00 USD | 10,030.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1107` | 48,460.00 USD | 48,460.00 USD | 0.00 USD | 12,720.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1107` | 24,940.00 USD | 24,940.00 USD | 0.00 USD | 12,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1109` | 12,430.00 USD | 12,430.00 USD | 0.00 USD | 12,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1113` | 50,340.00 USD | 50,340.00 USD | 15,810.00 USD | 3,630.00 USD | 30,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1115` | 55,110.00 USD | 55,110.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1117` | 103,750.00 USD | 103,750.00 USD | 0.00 USD | 24,680.00 USD | 23,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1117` | 39,270.00 USD | 39,270.00 USD | 0.00 USD | 22,780.00 USD | 16,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1119` | 130,740.00 USD | 130,740.00 USD | 16,250.00 USD | 5,030.00 USD | 5,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1119` | 70,340.00 USD | 70,340.00 USD | 13,220.00 USD | 7,050.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 82,870.00 USD | 82,870.00 USD | 0.00 USD | 0.00 USD | 12,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1123` | 160,200.00 USD | 160,200.00 USD | 29,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1123` | 127,560.00 USD | 127,560.00 USD | 0.00 USD | 18,520.00 USD | 26,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1125` | 167,240.00 USD | 167,240.00 USD | 0.00 USD | 7,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1125` | 156,390.00 USD | 156,390.00 USD | 0.00 USD | 0.00 USD | 28,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1127` | 170,180.00 USD | 170,180.00 USD | 0.00 USD | 0.00 USD | 2,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1129` | 175,670.00 USD | 175,670.00 USD | 5,450.00 USD | 0.00 USD | 40.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1131` | 205,620.00 USD | 205,620.00 USD | 13,530.00 USD | 4,870.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1131` | 183,960.00 USD | 183,960.00 USD | 12,540.00 USD | 0.00 USD | 15,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1133` | 258,190.00 USD | 258,190.00 USD | 6,530.00 USD | 22,520.00 USD | 23,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 189,410.00 USD | 189,410.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1135` | 265,170.00 USD | 265,170.00 USD | 4,040.00 USD | 2,880.00 USD | 57.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1135` | 203,930.00 USD | 203,930.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1137` | 266,170.00 USD | 266,170.00 USD | 0.00 USD | 856.93 USD | 142.78 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1139` | 280,450.00 USD | 280,450.00 USD | 0.00 USD | 0.00 USD | 14,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1141` | 295,720.00 USD | 295,720.00 USD | 8,780.00 USD | 2,800.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1141` | 215,830.00 USD | 215,830.00 USD | 4,360.00 USD | 0.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1143` | 336,700.00 USD | 336,700.00 USD | 11,570.00 USD | 22,660.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1143` | 290,110.00 USD | 290,110.00 USD | 0.00 USD | 0.00 USD | 74,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1145` | 390,920.00 USD | 390,920.00 USD | 8,350.00 USD | 10,790.00 USD | 35,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 441,640.00 USD | 441,640.00 USD | 10,360.00 USD | 0.00 USD | 141,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1147` | 433,300.00 USD | 433,300.00 USD | 6,800.00 USD | 8,840.00 USD | 26,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1147` | 585,910.00 USD | 585,910.00 USD | 9,880.00 USD | 0.00 USD | 134,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1149` | 503,900.00 USD | 503,900.00 USD | 35,170.00 USD | 0.00 USD | 35,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1149` | 669,340.00 USD | 669,340.00 USD | 10,560.00 USD | 0.00 USD | 72,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1151` | 589,090.00 USD | 589,090.00 USD | 21,360.00 USD | 14,620.00 USD | 49,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 894,670.00 USD | 894,670.00 USD | 92,570.00 USD | 4,210.00 USD | 128,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1153` | 723,190.00 USD | 723,190.00 USD | 37,440.00 USD | 28,670.00 USD | 67,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1153` | 1,200,000.00 USD | 1,200,000.00 USD | 153,720.00 USD | 8,400.00 USD | 139,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1155` | 852,620.00 USD | 852,620.00 USD | 48,310.00 USD | 27,080.00 USD | 54,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1155` | 1,490,000.00 USD | 1,490,000.00 USD | 149,360.00 USD | 40,110.00 USD | 105,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1157` | 936,580.00 USD | 936,580.00 USD | 37,790.00 USD | 12,010.00 USD | 34,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 1,700,000.00 USD | 1,700,000.00 USD | 155,250.00 USD | 3,760.00 USD | 48,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1159` | 1,000,000.00 USD | 1,000,000.00 USD | 27,270.00 USD | 12,000.00 USD | 25,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1159` | 1,870,000.00 USD | 1,870,000.00 USD | 105,000.00 USD | 12,710.00 USD | 53,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1161` | 1,080,000.00 USD | 1,080,000.00 USD | 30,570.00 USD | 6,970.00 USD | 36,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1161` | 2,150,000.00 USD | 2,150,000.00 USD | 146,810.00 USD | 37,250.00 USD | 99,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1163` | 1,130,000.00 USD | 1,130,000.00 USD | 18,210.00 USD | 14,540.00 USD | 17,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 2,300,000.00 USD | 2,300,000.00 USD | 66,560.00 USD | 11,460.00 USD | 68,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1165` | 1,160,000.00 USD | 1,160,000.00 USD | 14,300.00 USD | 14,710.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1165` | 2,430,000.00 USD | 2,430,000.00 USD | 68,620.00 USD | 35,720.00 USD | 27,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1167` | 1,200,000.00 USD | 1,200,000.00 USD | 15,040.00 USD | 17,950.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1167` | 2,570,000.00 USD | 2,570,000.00 USD | 79,610.00 USD | 21,620.00 USD | 41,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1169` | 1,240,000.00 USD | 1,240,000.00 USD | 16,040.00 USD | 6,020.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 2,740,000.00 USD | 2,740,000.00 USD | 65,340.00 USD | 14,840.00 USD | 86,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1171` | 1,270,000.00 USD | 1,270,000.00 USD | 17,090.00 USD | 4,520.00 USD | 4,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1171` | 2,850,000.00 USD | 2,850,000.00 USD | 57,350.00 USD | 11,370.00 USD | 35,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1173` | 1,300,000.00 USD | 1,300,000.00 USD | 14,960.00 USD | 8,910.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1173` | 2,930,000.00 USD | 2,930,000.00 USD | 40,860.00 USD | 9,190.00 USD | 36,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1175` | 1,350,000.00 USD | 1,350,000.00 USD | 11,510.00 USD | 17,150.00 USD | 24,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 3,040,000.00 USD | 3,040,000.00 USD | 38,840.00 USD | 12,300.00 USD | 58,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1177` | 1,400,000.00 USD | 1,400,000.00 USD | 19,300.00 USD | 8,560.00 USD | 16,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1177` | 3,140,000.00 USD | 3,140,000.00 USD | 33,330.00 USD | 20,350.00 USD | 44,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1179` | 1,440,000.00 USD | 1,440,000.00 USD | 19,180.00 USD | 5,840.00 USD | 14,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1179` | 3,240,000.00 USD | 3,240,000.00 USD | 66,670.00 USD | 10,940.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1181` | 1,470,000.00 USD | 1,470,000.00 USD | 15,480.00 USD | 6,030.00 USD | 15,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 3,300,000.00 USD | 3,300,000.00 USD | 22,290.00 USD | 15,780.00 USD | 17,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1183` | 1,490,000.00 USD | 1,490,000.00 USD | 7,310.00 USD | 1,400.00 USD | 9,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1183` | 3,340,000.00 USD | 3,340,000.00 USD | 4,040.00 USD | 1,800.00 USD | 39,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1185` | 1,520,000.00 USD | 1,520,000.00 USD | 8,760.00 USD | 7,830.00 USD | 13,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1185` | 3,370,000.00 USD | 3,370,000.00 USD | 3,880.00 USD | 5,130.00 USD | 22,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1187` | 1,550,000.00 USD | 1,550,000.00 USD | 11,520.00 USD | 8,520.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 3,430,000.00 USD | 3,430,000.00 USD | 5,620.00 USD | 15,370.00 USD | 32,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1189` | 1,570,000.00 USD | 1,570,000.00 USD | 4,220.00 USD | 3,060.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1189` | 3,470,000.00 USD | 3,470,000.00 USD | 27,240.00 USD | 15,060.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1191` | 1,580,000.00 USD | 1,580,000.00 USD | 4,940.00 USD | 6,690.00 USD | 3,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1191` | 3,620,000.00 USD | 3,620,000.00 USD | 22,650.00 USD | 15,330.00 USD | 109,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1193` | 1,590,000.00 USD | 1,590,000.00 USD | 4,720.00 USD | 2,080.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 3,650,000.00 USD | 3,650,000.00 USD | 21,260.00 USD | 0.00 USD | 9,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1195` | 1,610,000.00 USD | 1,610,000.00 USD | 9,550.00 USD | 3,210.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1195` | 3,690,000.00 USD | 3,690,000.00 USD | 11,190.00 USD | 1,780.00 USD | 29,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1197` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 1,040.00 USD | 105.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1197` | 3,720,000.00 USD | 3,720,000.00 USD | 6,780.00 USD | 10,800.00 USD | 14,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1199` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 3,050.00 USD | 3,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 3,800,000.00 USD | 3,800,000.00 USD | 9,100.00 USD | 0.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1201` | 1,630,000.00 USD | 1,630,000.00 USD | 6,460.00 USD | 1,070.00 USD | 8,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1201` | 3,960,000.00 USD | 3,960,000.00 USD | 114,140.00 USD | 16,380.00 USD | 29,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1203` | 1,640,000.00 USD | 1,640,000.00 USD | 5,670.00 USD | 413.94 USD | 2,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1203` | 4,060,000.00 USD | 4,060,000.00 USD | 70,770.00 USD | 29,250.00 USD | 6,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1205` | 1,640,000.00 USD | 1,640,000.00 USD | 2,250.00 USD | 1,670.00 USD | 750.19 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 4,330,000.00 USD | 4,330,000.00 USD | 86,480.00 USD | 48,720.00 USD | 128,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1207` | 1,650,000.00 USD | 1,650,000.00 USD | 3,510.00 USD | 524.23 USD | 885.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1207` | 4,420,000.00 USD | 4,420,000.00 USD | 12,460.00 USD | 19,400.00 USD | 59,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1209` | 1,650,000.00 USD | 1,650,000.00 USD | 636.93 USD | 1,370.00 USD | 2,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1209` | 4,620,000.00 USD | 4,620,000.00 USD | 85,160.00 USD | 19,340.00 USD | 94,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1211` | 1,660,000.00 USD | 1,660,000.00 USD | 3,340.00 USD | 2,600.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 4,690,000.00 USD | 4,690,000.00 USD | 27,400.00 USD | 16,260.00 USD | 29,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1213` | 1,670,000.00 USD | 1,670,000.00 USD | 1,550.00 USD | 1,220.00 USD | 10,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1213` | 4,770,000.00 USD | 4,770,000.00 USD | 23,920.00 USD | 26,740.00 USD | 24,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1215` | 1,680,000.00 USD | 1,680,000.00 USD | 1,650.00 USD | 0.00 USD | 4,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1215` | 4,840,000.00 USD | 4,840,000.00 USD | 5,900.00 USD | 6,620.00 USD | 59,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1217` | 1,690,000.00 USD | 1,690,000.00 USD | 2,420.00 USD | 624.33 USD | 7,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 4,890,000.00 USD | 4,890,000.00 USD | 18,490.00 USD | 23,600.00 USD | 11,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1219` | 1,700,000.00 USD | 1,700,000.00 USD | 2,320.00 USD | 718.82 USD | 10,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1219` | 4,960,000.00 USD | 4,960,000.00 USD | 26,700.00 USD | 5,500.00 USD | 38,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1221` | 1,720,000.00 USD | 1,720,000.00 USD | 4,680.00 USD | 2,940.00 USD | 3,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1221` | 5,050,000.00 USD | 5,050,000.00 USD | 47,890.00 USD | 21,770.00 USD | 18,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1223` | 1,730,000.00 USD | 1,730,000.00 USD | 4,190.00 USD | 1,410.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 5,240,000.00 USD | 5,240,000.00 USD | 103,180.00 USD | 36,290.00 USD | 48,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1225` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1225` | 5,310,000.00 USD | 5,310,000.00 USD | 43,040.00 USD | 24,950.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 16,900.00 USD | 16,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1227` | 1,730,000.00 USD | 1,730,000.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1227` | 5,470,000.00 USD | 5,470,000.00 USD | 68,750.00 USD | 31,790.00 USD | 55,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1229` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 403.62 USD | 1,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 5,630,000.00 USD | 5,630,000.00 USD | 77,860.00 USD | 40,000.00 USD | 43,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1231` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 430.11 USD | 793.30 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1231` | 5,720,000.00 USD | 5,720,000.00 USD | 29,380.00 USD | 31,660.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1233` | 1,740,000.00 USD | 1,740,000.00 USD | 2,320.00 USD | 3,210.00 USD | 15.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1233` | 5,830,000.00 USD | 5,830,000.00 USD | 57,130.00 USD | 13,020.00 USD | 40,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1235` | 1,750,000.00 USD | 1,750,000.00 USD | 1,570.00 USD | 1,240.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1235` | 5,860,000.00 USD | 5,860,000.00 USD | 10,950.00 USD | 6,400.00 USD | 8,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1237` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 1,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1237` | 5,870,000.00 USD | 5,870,000.00 USD | 4,080.00 USD | 9,720.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1239` | 1,750,000.00 USD | 1,750,000.00 USD | 4,900.00 USD | 724.40 USD | 629.61 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1239` | 5,880,000.00 USD | 5,880,000.00 USD | 8,780.00 USD | 1,270.00 USD | 220.25 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1241` | 1,760,000.00 USD | 1,760,000.00 USD | 2,790.00 USD | 1,830.00 USD | 4,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1241` | 5,900,000.00 USD | 5,900,000.00 USD | 6,830.00 USD | 9,690.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1243` | 1,780,000.00 USD | 1,780,000.00 USD | 1,660.00 USD | 4,600.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1243` | 5,920,000.00 USD | 5,920,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1245` | 1,790,000.00 USD | 1,790,000.00 USD | 6,600.00 USD | 3,420.00 USD | 5,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1245` | 5,970,000.00 USD | 5,970,000.00 USD | 26,080.00 USD | 11,090.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1247` | 1,800,000.00 USD | 1,800,000.00 USD | 2,580.00 USD | 1,320.00 USD | 4,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1247` | 6,030,000.00 USD | 6,030,000.00 USD | 24,470.00 USD | 19,030.00 USD | 9,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1249` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 1,190.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1249` | 6,050,000.00 USD | 6,050,000.00 USD | 13,440.00 USD | 5,480.00 USD | 5,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1251` | 1,810,000.00 USD | 1,810,000.00 USD | 4,600.00 USD | 932.33 USD | 3,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1251` | 6,070,000.00 USD | 6,070,000.00 USD | 7,660.00 USD | 5,070.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1253` | 1,820,000.00 USD | 1,820,000.00 USD | 855.19 USD | 2,500.00 USD | 3,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1253` | 6,100,000.00 USD | 6,100,000.00 USD | 11,420.00 USD | 2,100.00 USD | 14,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1255` | 1,820,000.00 USD | 1,820,000.00 USD | 2,780.00 USD | 1,590.00 USD | 1,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1255` | 6,120,000.00 USD | 6,120,000.00 USD | 2,250.00 USD | 13,990.00 USD | 91.62 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1257` | 1,830,000.00 USD | 1,830,000.00 USD | 1,140.00 USD | 0.00 USD | 0.01 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1257` | 6,140,000.00 USD | 6,140,000.00 USD | 15,610.00 USD | 5,200.00 USD | 163.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1259` | 1,830,000.00 USD | 1,830,000.00 USD | 962.72 USD | 1,690.00 USD | 22.77 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1259` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 154.62 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1261` | 1,830,000.00 USD | 1,830,000.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1261` | 6,150,000.00 USD | 6,150,000.00 USD | 4,270.00 USD | 0.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1263` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1264` | 1,830,000.00 USD | 1,830,000.00 USD | 1,300.00 USD | 694.78 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1265` | 6,160,000.00 USD | 6,160,000.00 USD | 2,710.00 USD | 0.00 USD | 3,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1267` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1269` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 0.00 USD | 16.21 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1271` | 6,170,000.00 USD | 6,170,000.00 USD | 5,940.00 USD | 0.00 USD | 13.94 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.0385` | 242,890.00 USD | 0.00 USD | 174.65 USD | `-65.38%` | `4,536.30` |
| `Live` | `Long` | `0.0395` | 242,720.00 USD | 0.00 USD | 237.00 USD | `-64.48%` | `6,000.00` |
| `Live` | `Long` | `0.0485` | 242,480.00 USD | 0.00 USD | 247.30 USD | `-56.38%` | `5,098.90` |
| `Live` | `Long` | `0.0495` | 242,230.00 USD | 0.00 USD | 3,450.00 USD | `-55.49%` | `69,790.10` |
| `Live` | `Long` | `0.0545` | 238,780.00 USD | 0.00 USD | 3,460.00 USD | `-50.99%` | `63,403.00` |
| `Live` | `Long` | `0.0575` | 235,320.00 USD | 0.00 USD | 829.69 USD | `-48.29%` | `14,429.40` |
| `Live` | `Long` | `0.0615` | 234,490.00 USD | 0.00 USD | 1,100.00 USD | `-44.69%` | `17,943.80` |
| `Live` | `Long` | `0.0645` | 233,390.00 USD | 0.00 USD | 353.81 USD | `-42.00%` | `5,485.40` |
| `Live` | `Long` | `0.0665` | 233,040.00 USD | 0.00 USD | 509.64 USD | `-40.20%` | `7,663.80` |
| `Live` | `Long` | `0.0675` | 232,530.00 USD | 0.00 USD | 518.48 USD | `-39.30%` | `7,681.20` |
| `Live` | `Long` | `0.0685` | 232,010.00 USD | 0.00 USD | 1,920.00 USD | `-38.40%` | `28,000.00` |
| `Live` | `Long` | `0.0725` | 230,090.00 USD | 0.00 USD | 25,370.00 USD | `-34.80%` | `349,988.60` |
| `Live` | `Long` | `0.0735` | 204,720.00 USD | 0.00 USD | 110.79 USD | `-33.90%` | `1,507.30` |
| `Live` | `Long` | `0.0745` | 204,600.00 USD | 0.00 USD | 48,850.00 USD | `-33.00%` | `655,702.20` |
| `Live` | `Long` | `0.0755` | 155,750.00 USD | 0.00 USD | 1,020.00 USD | `-32.10%` | `13,481.90` |
| `Live` | `Long` | `0.0765` | 154,740.00 USD | 0.00 USD | 2,010.00 USD | `-31.21%` | `26,234.30` |
| `Live` | `Long` | `0.0775` | 152,730.00 USD | 0.00 USD | 878.62 USD | `-30.31%` | `11,337.00` |
| `Live` | `Long` | `0.0795` | 151,850.00 USD | 0.00 USD | 1,320.00 USD | `-28.51%` | `16,641.80` |
| `Live` | `Long` | `0.0805` | 150,530.00 USD | 0.00 USD | 223.98 USD | `-27.61%` | `2,782.40` |
| `Live` | `Long` | `0.0815` | 150,300.00 USD | 0.00 USD | 1,560.00 USD | `-26.71%` | `19,181.40` |
| `Live` | `Long` | `0.0865` | 148,740.00 USD | 0.00 USD | 2,350.00 USD | `-22.21%` | `27,146.60` |
| `Live` | `Long` | `0.0895` | 146,390.00 USD | 0.00 USD | 3,120.00 USD | `-19.51%` | `34,873.20` |
| `Live` | `Long` | `0.0905` | 143,270.00 USD | 0.00 USD | 443.16 USD | `-18.62%` | `4,896.80` |
| `Live` | `Long` | `0.0925` | 142,830.00 USD | 0.00 USD | 17,600.00 USD | `-16.82%` | `190,304.90` |
| `Live` | `Long` | `0.0945` | 125,230.00 USD | 0.00 USD | 69,120.00 USD | `-15.02%` | `731,405.60` |
| `Live` | `Long` | `0.0955` | 56,110.00 USD | 0.00 USD | 4,640.00 USD | `-14.12%` | `48,598.80` |
| `Live` | `Long` | `0.0965` | 51,470.00 USD | 0.00 USD | 419.87 USD | `-13.22%` | `4,351.00` |
| `Live` | `Long` | `0.0975` | 51,050.00 USD | 0.00 USD | 12,670.00 USD | `-12.32%` | `129,987.90` |
| `Live` | `Long` | `0.0985` | 38,370.00 USD | 0.00 USD | 19,960.00 USD | `-11.42%` | `202,627.30` |
| `Live` | `Long` | `0.1005` | 18,410.00 USD | 0.00 USD | 427.25 USD | `-9.62%` | `4,251.20` |
| `Live` | `Long` | `0.1015` | 17,990.00 USD | 0.00 USD | 622.37 USD | `-8.72%` | `6,131.70` |
| `Live` | `Long` | `0.1025` | 17,360.00 USD | 0.00 USD | 17,360.00 USD | `-7.82%` | `169,408.50` |
| `Live` | `Short` | `0.1225` | 16,900.00 USD | 16,900.00 USD | 0.00 USD | `+10.16%` | `137,980.90` |
| `Live` | `Short` | `0.1355` | 18,240.00 USD | 1,330.00 USD | 0.00 USD | `+21.85%` | `9,843.80` |
| `Live` | `Short` | `0.1515` | 33,390.00 USD | 15,150.00 USD | 0.00 USD | `+36.24%` | `100,000.40` |
| `Live` | `Short` | `0.1555` | 39,600.00 USD | 6,210.00 USD | 0.00 USD | `+39.84%` | `39,929.50` |
| `Live` | `Short` | `0.1565` | 40,150.00 USD | 550.61 USD | 0.00 USD | `+40.74%` | `3,518.30` |
| `Live` | `Short` | `0.1635` | 60,350.00 USD | 20,210.00 USD | 0.00 USD | `+47.03%` | `123,580.80` |
| `Live` | `Short` | `0.1695` | 60,520.00 USD | 169.25 USD | 0.00 USD | `+52.43%` | `998.50` |
| `Live` | `Short` | `0.1865` | 60,690.00 USD | 167.85 USD | 0.00 USD | `+67.72%` | `900.00` |
| `Live` | `Short` | `0.1925` | 61,620.00 USD | 930.49 USD | 0.00 USD | `+73.11%` | `4,833.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0635` | 176,420.00 USD | 0.00 USD | 1,140.00 USD | `-42.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 175,280.00 USD | 0.00 USD | 773.46 USD | `-36.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 174,510.00 USD | 0.00 USD | 592.27 USD | `-35.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 173,920.00 USD | 0.00 USD | 755.00 USD | `-32.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0805` | 173,160.00 USD | 0.00 USD | 411.06 USD | `-27.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0815` | 172,750.00 USD | 0.00 USD | 183.49 USD | `-26.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0835` | 172,570.00 USD | 0.00 USD | 456.70 USD | `-24.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 172,110.00 USD | 0.00 USD | 631.58 USD | `-23.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 171,480.00 USD | 0.00 USD | 653.74 USD | `-20.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0915` | 170,830.00 USD | 0.00 USD | 1,460.00 USD | `-17.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 169,360.00 USD | 0.00 USD | 485.13 USD | `-15.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0975` | 168,880.00 USD | 0.00 USD | 720.22 USD | `-12.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0985` | 168,160.00 USD | 0.00 USD | 931.75 USD | `-11.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0995` | 167,230.00 USD | 0.00 USD | 801.64 USD | `-10.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 166,420.00 USD | 0.00 USD | 1,470.00 USD | `-9.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1015` | 164,950.00 USD | 0.00 USD | 903.42 USD | `-8.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 164,050.00 USD | 0.00 USD | 780.70 USD | `-7.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1035` | 163,270.00 USD | 0.00 USD | 4,650.00 USD | `-6.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1045` | 158,620.00 USD | 0.00 USD | 18,950.00 USD | `-6.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1055` | 139,670.00 USD | 0.00 USD | 7,770.00 USD | `-5.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1065` | 131,900.00 USD | 0.00 USD | 109,280.00 USD | `-4.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 22,620.00 USD | 0.00 USD | 21,670.00 USD | `-3.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 951.99 USD | 0.00 USD | 150.04 USD | `-2.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1095` | 801.95 USD | 0.00 USD | 639.36 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 162.59 USD | 0.00 USD | 162.59 USD | `-0.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 839.64 USD | 839.64 USD | 0.00 USD | `+0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1125` | 2,520.00 USD | 1,680.00 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1135` | 2,640.00 USD | 116.27 USD | 0.00 USD | `+2.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1145` | 2,770.00 USD | 134.61 USD | 0.00 USD | `+2.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 3,260.00 USD | 489.97 USD | 0.00 USD | `+3.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1165` | 3,730.00 USD | 466.94 USD | 0.00 USD | `+4.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1175` | 31,260.00 USD | 27,530.00 USD | 0.00 USD | `+5.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1185` | 32,310.00 USD | 1,050.00 USD | 0.00 USD | `+6.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1195` | 46,950.00 USD | 14,640.00 USD | 0.00 USD | `+7.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1205` | 47,350.00 USD | 398.42 USD | 0.00 USD | `+8.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1225` | 48,330.00 USD | 980.00 USD | 0.00 USD | `+10.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1235` | 61,310.00 USD | 12,980.00 USD | 0.00 USD | `+11.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1255` | 65,680.00 USD | 4,380.00 USD | 0.00 USD | `+12.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1265` | 76,140.00 USD | 10,460.00 USD | 0.00 USD | `+13.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1275` | 76,640.00 USD | 492.06 USD | 0.00 USD | `+14.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1305` | 77,080.00 USD | 444.24 USD | 0.00 USD | `+17.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1315` | 108,640.00 USD | 31,560.00 USD | 0.00 USD | `+18.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1335` | 109,960.00 USD | 1,310.00 USD | 0.00 USD | `+20.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1345` | 114,110.00 USD | 4,150.00 USD | 0.00 USD | `+20.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1365` | 124,800.00 USD | 10,690.00 USD | 0.00 USD | `+22.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1405` | 137,910.00 USD | 13,110.00 USD | 0.00 USD | `+26.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1425` | 138,010.00 USD | 102.22 USD | 0.00 USD | `+28.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1435` | 145,180.00 USD | 7,180.00 USD | 0.00 USD | `+29.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1485` | 147,830.00 USD | 2,650.00 USD | 0.00 USD | `+33.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1495` | 148,620.00 USD | 792.53 USD | 0.00 USD | `+34.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1525` | 152,390.00 USD | 3,770.00 USD | 0.00 USD | `+37.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 152,570.00 USD | 184.49 USD | 0.00 USD | `+39.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 159,300.00 USD | 6,720.00 USD | 0.00 USD | `+40.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 159,520.00 USD | 219.81 USD | 0.00 USD | `+41.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 159,790.00 USD | 277.62 USD | 0.00 USD | `+47.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 161,590.00 USD | 1,800.00 USD | 0.00 USD | `+52.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 161,800.00 USD | 216.55 USD | 0.00 USD | `+56.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 161,920.00 USD | 117.26 USD | 0.00 USD | `+77.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 182,460.00 USD | 20,530.00 USD | 0.00 USD | `+80.31%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0967` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 3,770.00 USD | 2,660.00 USD | 2,840.00 USD |
| `7D` | `0.0969` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 0.00 USD | 2,810.00 USD | 9,360.00 USD |
| `7D` | `0.0971` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 0.00 USD | 2,000.00 USD | 34.36 USD |
| `7D` | `0.0973` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD |
| `7D` | `0.0975` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 0.00 USD | 1,160.00 USD | 4,130.00 USD |
| `7D` | `0.0977` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 5,800.00 USD |
| `7D` | `0.0979` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 0.00 USD | 1,530.00 USD | 5,710.00 USD |
| `7D` | `0.0981` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD |
| `7D` | `0.0983` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 7,990.00 USD | 1,230.00 USD | 8,820.00 USD |
| `7D` | `0.0985` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 7,110.00 USD | 0.00 USD | 6,320.00 USD |
| `7D` | `0.0987` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 5,390.00 USD | 9,190.00 USD | 37,360.00 USD |
| `1D` | `0.0989` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 3,060.00 USD | 1,370.00 USD | 2,180.00 USD |
| `7D` | `0.0989` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 12,260.00 USD | 4,520.00 USD | 27,240.00 USD |
| `1D` | `0.0991` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 3,340.00 USD | 2,600.00 USD | 3,210.00 USD |
| `7D` | `0.0991` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 14,350.00 USD | 10,350.00 USD | 13,520.00 USD |
| `1D` | `0.0993` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 1,550.00 USD | 1,220.00 USD | 10,430.00 USD |
| `7D` | `0.0993` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 23,920.00 USD | 10,140.00 USD | 24,060.00 USD |
| `1D` | `0.0995` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 4,080.00 USD | 624.33 USD | 11,850.00 USD |
| `7D` | `0.0995` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 13,090.00 USD | 6,160.00 USD | 25,300.00 USD |
| `1D` | `0.0997` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 2,320.00 USD | 718.82 USD | 10,030.00 USD |
| `7D` | `0.0997` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 21,100.00 USD | 5,500.00 USD | 32,960.00 USD |
| `1D` | `0.0999` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 4,680.00 USD | 2,940.00 USD | 3,630.00 USD |
| `7D` | `0.0999` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 14,230.00 USD | 6,540.00 USD | 18,820.00 USD |
| `1D` | `0.1001` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 4,190.00 USD | 1,410.00 USD | 7,700.00 USD |
| `7D` | `0.1001` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 29,230.00 USD | 3,010.00 USD | 10,920.00 USD |
| `1D` | `0.1003` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 0.00 USD | 558.39 USD | 30.31 USD |
| `7D` | `0.1003` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 8,010.00 USD | 7,060.00 USD | 5,210.00 USD |
| `1D` | `0.1005` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 1,970.00 USD | 403.62 USD | 1,090.00 USD |
| `7D` | `0.1005` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 25,070.00 USD | 11,000.00 USD | 18,310.00 USD |
| `1D` | `0.1007` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 0.00 USD | 430.11 USD | 827.99 USD |
| `7D` | `0.1007` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 10,260.00 USD | 2,280.00 USD | 14,060.00 USD |
| `1D` | `0.1009` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 2,320.00 USD | 3,210.00 USD | 59.05 USD |
| `7D` | `0.1009` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 15,320.00 USD | 3,070.00 USD | 6,940.00 USD |
| `1D` | `0.1011` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 1,570.00 USD | 1,240.00 USD | 3,490.00 USD |
| `7D` | `0.1011` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 4,430.00 USD | 4,720.00 USD | 8,900.00 USD |
| `1D` | `0.1013` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 4,900.00 USD | 2,290.00 USD | 629.61 USD |
| `7D` | `0.1013` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 12,870.00 USD | 4,030.00 USD | 3,080.00 USD |
| `1D` | `0.1015` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 2,790.00 USD | 1,830.00 USD | 4,330.00 USD |
| `7D` | `0.1015` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 6,830.00 USD | 965.35 USD | 2,430.00 USD |
| `1D` | `0.1017` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 1,660.00 USD | 4,600.00 USD | 7,520.00 USD |
| `7D` | `0.1017` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,790.00 USD |
| `1D` | `0.1019` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 6,600.00 USD | 3,420.00 USD | 5,560.00 USD |
| `7D` | `0.1019` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 9,260.00 USD | 5,790.00 USD | 12,990.00 USD |
| `1D` | `0.1021` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 2,580.00 USD | 1,320.00 USD | 4,790.00 USD |
| `7D` | `0.1021` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 7,900.00 USD | 3,270.00 USD | 7,150.00 USD |
| `1D` | `0.1023` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 4,600.00 USD | 2,120.00 USD | 4,650.00 USD |
| `7D` | `0.1023` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 4,030.00 USD | 4,990.00 USD | 14,520.00 USD |
| `1D` | `0.1025` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 855.19 USD | 2,500.00 USD | 3,630.00 USD |
| `7D` | `0.1025` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 1,550.00 USD | 0.00 USD | 5,690.00 USD |
| `1D` | `0.1027` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 2,780.00 USD | 1,590.00 USD | 1,670.00 USD |
| `7D` | `0.1027` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 2,250.00 USD | 2,580.00 USD | 359.07 USD |
| `1D` | `0.1029` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 4,340.00 USD | 705.79 USD | 6,430.00 USD |
| `7D` | `0.1029` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 7,420.00 USD | 3,000.00 USD | 332.49 USD |
| `1D` | `0.1031` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 11,600.00 USD | 3,910.00 USD | 8,030.00 USD |
| `7D` | `0.1031` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 13,690.00 USD | 5,070.00 USD | 10,680.00 USD |
| `1D` | `0.1033` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 8,760.00 USD | 2,790.00 USD | 10,470.00 USD |
| `7D` | `0.1033` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 3,880.00 USD | 2,640.00 USD | 15,240.00 USD |
| `1D` | `0.1035` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 7,450.00 USD | 6,850.00 USD | 10,220.00 USD |
| `7D` | `0.1035` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 2,710.00 USD | 9,400.00 USD | 16,150.00 USD |
| `1D` | `0.1037` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 2,220.00 USD | 13,000.00 USD | 9,220.00 USD |
| `7D` | `0.1037` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 19,410.00 USD |
| `1D` | `0.1039` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 3,660.00 USD | 1,730.00 USD | 11,820.00 USD |
| `7D` | `0.1039` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 0.00 USD | 5,170.00 USD | 167.04 USD |
| `1D` | `0.1041` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 7,790.00 USD | 6,910.00 USD | 13,300.00 USD |
| `7D` | `0.1041` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 5,940.00 USD | 2,910.00 USD | 10,820.00 USD |
| `1D` | `0.1043` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 17,650.00 USD | 5,650.00 USD | 7,860.00 USD |
| `7D` | `0.1043` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 15,960.00 USD | 5,980.00 USD | 21,000.00 USD |
| `1D` | `0.1045` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 0.00 USD | 2,600.00 USD | 6,170.00 USD |
| `7D` | `0.1045` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 0.00 USD | 3,830.00 USD | 15,000.00 USD |
| `1D` | `0.1047` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 4,610.00 USD | 2,610.00 USD | 16,600.00 USD |
| `7D` | `0.1047` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 0.00 USD | 1,720.00 USD | 22,650.00 USD |
| `1D` | `0.1049` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 21,050.00 USD | 2,430.00 USD | 10,910.00 USD |
| `7D` | `0.1049` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 34,790.00 USD | 4,810.00 USD | 35,410.00 USD |
| `1D` | `0.1051` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 16,410.00 USD | 8,750.00 USD | 24,360.00 USD |
| `7D` | `0.1051` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 17,290.00 USD | 11,500.00 USD | 48,700.00 USD |
| `1D` | `0.1053` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 25,850.00 USD | 7,040.00 USD | 19,520.00 USD |
| `7D` | `0.1053` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 47,580.00 USD | 29,800.00 USD | 95,610.00 USD |
| `1D` | `0.1055` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 21,850.00 USD | 15,910.00 USD | 31,710.00 USD |
| `7D` | `0.1055` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 50,090.00 USD | 27,290.00 USD | 122,200.00 USD |
| `1D` | `0.1057` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 21,550.00 USD | 21,720.00 USD | 42,810.00 USD |
| `7D` | `0.1057` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 44,200.00 USD | 43,030.00 USD | 74,320.00 USD |
| `1D` | `0.1059` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 15,180.00 USD | 21,000.00 USD | 52,100.00 USD |
| `7D` | `0.1059` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 92,510.00 USD | 49,670.00 USD | 114,120.00 USD |
| `1D` | `0.1061` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 15,660.00 USD | 9,870.00 USD | 51,940.00 USD |
| `7D` | `0.1061` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 38,260.00 USD | 28,040.00 USD | 76,340.00 USD |
| `1D` | `0.1063` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 56,400.00 USD | 14,600.00 USD | 51,590.00 USD |
| `7D` | `0.1063` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 88,520.00 USD | 38,330.00 USD | 148,680.00 USD |
| `1D` | `0.1065` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 16,250.00 USD | 13,370.00 USD | 19,480.00 USD |
| `7D` | `0.1065` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 91,170.00 USD | 21,040.00 USD | 93,660.00 USD |
| `1D` | `0.1067` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 13,530.00 USD | 15,160.00 USD | 33,100.00 USD |
| `7D` | `0.1067` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 97,290.00 USD | 36,720.00 USD | 67,520.00 USD |
| `1D` | `0.1069` | 943,830.00 USD | 0.00 USD | 943,830.00 USD | 24,070.00 USD | 7,520.00 USD | 43,320.00 USD |
| `7D` | `0.1069` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 76,900.00 USD | 32,620.00 USD | 72,020.00 USD |
| `1D` | `0.1071` | 868,920.00 USD | 0.00 USD | 868,920.00 USD | 48,660.00 USD | 4,860.00 USD | 18,950.00 USD |
| `7D` | `0.1071` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 119,440.00 USD | 27,240.00 USD | 42,730.00 USD |
| `1D` | `0.1073` | 796,460.00 USD | 0.00 USD | 796,460.00 USD | 8,740.00 USD | 10,680.00 USD | 20,870.00 USD |
| `7D` | `0.1073` | 975,370.00 USD | 0.00 USD | 975,370.00 USD | 58,480.00 USD | 17,700.00 USD | 0.00 USD |
| `1D` | `0.1075` | 756,170.00 USD | 0.00 USD | 756,170.00 USD | 16,520.00 USD | 6,770.00 USD | 1,850.00 USD |
| `7D` | `0.1075` | 899,190.00 USD | 0.00 USD | 899,190.00 USD | 8,720.00 USD | 3,500.00 USD | 58.62 USD |
| `1D` | `0.1077` | 731,020.00 USD | 0.00 USD | 731,020.00 USD | 3,180.00 USD | 10,810.00 USD | 13,980.00 USD |
| `1D` | `0.1079` | 703,040.00 USD | 0.00 USD | 703,040.00 USD | 9,370.00 USD | 13,900.00 USD | 25,740.00 USD |
| `7D` | `0.1079` | 886,900.00 USD | 0.00 USD | 886,900.00 USD | 128,090.00 USD | 18,520.00 USD | 0.00 USD |
| `1D` | `0.1081` | 654,030.00 USD | 0.00 USD | 654,030.00 USD | 17,730.00 USD | 7,210.00 USD | 50,010.00 USD |
| `7D` | `0.1081` | 740,290.00 USD | 0.00 USD | 740,290.00 USD | 205,390.00 USD | 11,660.00 USD | 28,860.00 USD |
| `1D` | `0.1083` | 579,090.00 USD | 0.00 USD | 579,090.00 USD | 30,270.00 USD | 5,440.00 USD | 33,850.00 USD |
| `7D` | `0.1083` | 494,380.00 USD | 0.00 USD | 494,380.00 USD | 94,800.00 USD | 2,110.00 USD | 42,410.00 USD |
| `1D` | `0.1085` | 509,530.00 USD | 0.00 USD | 509,530.00 USD | 22,270.00 USD | 13,850.00 USD | 65,000.00 USD |
| `7D` | `0.1085` | 355,070.00 USD | 0.00 USD | 355,070.00 USD | 15,920.00 USD | 4,200.00 USD | 29.20 USD |
| `1D` | `0.1087` | 408,400.00 USD | 0.00 USD | 408,400.00 USD | 40,320.00 USD | 6,720.00 USD | 44,670.00 USD |
| `7D` | `0.1087` | 334,920.00 USD | 0.00 USD | 334,920.00 USD | 55,430.00 USD | 6,210.00 USD | 60,070.00 USD |
| `1D` | `0.1089` | 316,690.00 USD | 0.00 USD | 316,690.00 USD | 38,530.00 USD | 17,080.00 USD | 41,540.00 USD |
| `7D` | `0.1089` | 213,210.00 USD | 0.00 USD | 213,210.00 USD | 5,290.00 USD | 14,560.00 USD | 0.00 USD |
| `1D` | `0.1091` | 219,550.00 USD | 0.00 USD | 219,550.00 USD | 33,700.00 USD | 6,410.00 USD | 8,180.00 USD |
| `7D` | `0.1091` | 193,350.00 USD | 0.00 USD | 193,350.00 USD | 16,310.00 USD | 3,800.00 USD | 9,010.00 USD |
| `1D` | `0.1093` | 171,260.00 USD | 0.00 USD | 171,260.00 USD | 15,480.00 USD | 3,890.00 USD | 8,500.00 USD |
| `7D` | `0.1093` | 164,240.00 USD | 0.00 USD | 164,240.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD |
| `1D` | `0.1095` | 143,390.00 USD | 0.00 USD | 143,390.00 USD | 0.00 USD | 0.00 USD | 10,860.00 USD |
| `7D` | `0.1095` | 155,510.00 USD | 0.00 USD | 155,510.00 USD | 18,840.00 USD | 3,530.00 USD | 0.00 USD |
| `1D` | `0.1097` | 132,530.00 USD | 0.00 USD | 132,530.00 USD | 0.00 USD | 0.00 USD | 3,670.00 USD |
| `7D` | `0.1097` | 133,140.00 USD | 0.00 USD | 133,140.00 USD | 0.00 USD | 2,970.00 USD | 21,590.00 USD |
| `1D` | `0.1099` | 128,860.00 USD | 0.00 USD | 128,860.00 USD | 9,980.00 USD | 14,920.00 USD | 0.00 USD |
| `7D` | `0.1099` | 108,570.00 USD | 0.00 USD | 108,570.00 USD | 0.00 USD | 7,010.00 USD | 25,060.00 USD |
| `1D` | `0.1101` | 103,960.00 USD | 0.00 USD | 103,960.00 USD | 0.00 USD | 0.00 USD | 10,820.00 USD |
| `1D` | `0.1103` | 93,140.00 USD | 0.00 USD | 93,140.00 USD | 23,720.00 USD | 4,000.00 USD | 6,070.00 USD |
| `7D` | `0.1103` | 76,500.00 USD | 0.00 USD | 76,500.00 USD | 27,370.00 USD | 4,460.00 USD | 0.00 USD |
| `1D` | `0.1105` | 59,340.00 USD | 0.00 USD | 59,340.00 USD | 0.00 USD | 10,880.00 USD | 0.00 USD |
| `7D` | `0.1105` | 44,680.00 USD | 0.00 USD | 44,680.00 USD | 0.00 USD | 10,030.00 USD | 9,710.00 USD |
| `1D` | `0.1107` | 48,460.00 USD | 0.00 USD | 48,460.00 USD | 0.00 USD | 12,720.00 USD | 35,750.00 USD |
| `7D` | `0.1107` | 24,940.00 USD | 0.00 USD | 24,940.00 USD | 0.00 USD | 12,510.00 USD | 0.00 USD |
| `7D` | `0.1109` | 12,430.00 USD | 0.00 USD | 12,430.00 USD | 0.00 USD | 12,430.00 USD | 0.00 USD |
| `1D` | `0.1110` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1110` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1113` | 50,340.00 USD | 50,340.00 USD | 0.00 USD | 15,810.00 USD | 3,630.00 USD | 30,900.00 USD |
| `1D` | `0.1115` | 55,110.00 USD | 55,110.00 USD | 0.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1117` | 103,750.00 USD | 103,750.00 USD | 0.00 USD | 0.00 USD | 24,680.00 USD | 23,960.00 USD |
| `7D` | `0.1117` | 39,270.00 USD | 39,270.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | 16,490.00 USD |
| `1D` | `0.1119` | 130,740.00 USD | 130,740.00 USD | 0.00 USD | 16,250.00 USD | 5,030.00 USD | 5,720.00 USD |
| `7D` | `0.1119` | 70,340.00 USD | 70,340.00 USD | 0.00 USD | 13,220.00 USD | 7,050.00 USD | 10,800.00 USD |
| `7D` | `0.1121` | 82,870.00 USD | 82,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,530.00 USD |
| `1D` | `0.1123` | 160,200.00 USD | 160,200.00 USD | 0.00 USD | 29,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1123` | 127,560.00 USD | 127,560.00 USD | 0.00 USD | 0.00 USD | 18,520.00 USD | 26,180.00 USD |
| `1D` | `0.1125` | 167,240.00 USD | 167,240.00 USD | 0.00 USD | 0.00 USD | 7,040.00 USD | 0.00 USD |
| `7D` | `0.1125` | 156,390.00 USD | 156,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,830.00 USD |
| `1D` | `0.1127` | 170,180.00 USD | 170,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,950.00 USD |
| `1D` | `0.1129` | 175,670.00 USD | 175,670.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD | 40.44 USD |
| `1D` | `0.1131` | 205,620.00 USD | 205,620.00 USD | 0.00 USD | 13,530.00 USD | 4,870.00 USD | 11,550.00 USD |
| `7D` | `0.1131` | 183,960.00 USD | 183,960.00 USD | 0.00 USD | 12,540.00 USD | 0.00 USD | 15,020.00 USD |
| `1D` | `0.1133` | 258,190.00 USD | 258,190.00 USD | 0.00 USD | 6,530.00 USD | 22,520.00 USD | 23,520.00 USD |
| `7D` | `0.1133` | 189,410.00 USD | 189,410.00 USD | 0.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD |
| `1D` | `0.1135` | 265,170.00 USD | 265,170.00 USD | 0.00 USD | 4,040.00 USD | 2,880.00 USD | 57.64 USD |
| `7D` | `0.1135` | 203,930.00 USD | 203,930.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD |
| `1D` | `0.1137` | 266,170.00 USD | 266,170.00 USD | 0.00 USD | 0.00 USD | 856.93 USD | 142.78 USD |
| `1D` | `0.1139` | 280,450.00 USD | 280,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,280.00 USD |
| `1D` | `0.1141` | 295,720.00 USD | 295,720.00 USD | 0.00 USD | 8,780.00 USD | 2,800.00 USD | 3,680.00 USD |
| `7D` | `0.1141` | 215,830.00 USD | 215,830.00 USD | 0.00 USD | 4,360.00 USD | 0.00 USD | 7,540.00 USD |
| `1D` | `0.1143` | 336,700.00 USD | 336,700.00 USD | 0.00 USD | 11,570.00 USD | 22,660.00 USD | 6,750.00 USD |
| `7D` | `0.1143` | 290,110.00 USD | 290,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 74,280.00 USD |
| `1D` | `0.1145` | 390,920.00 USD | 390,920.00 USD | 0.00 USD | 8,350.00 USD | 10,790.00 USD | 35,080.00 USD |
| `7D` | `0.1145` | 441,640.00 USD | 441,640.00 USD | 0.00 USD | 10,360.00 USD | 0.00 USD | 141,160.00 USD |
| `1D` | `0.1147` | 433,300.00 USD | 433,300.00 USD | 0.00 USD | 6,800.00 USD | 8,840.00 USD | 26,740.00 USD |
| `7D` | `0.1147` | 585,910.00 USD | 585,910.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 134,400.00 USD |
| `1D` | `0.1149` | 503,900.00 USD | 503,900.00 USD | 0.00 USD | 35,170.00 USD | 0.00 USD | 35,420.00 USD |
| `7D` | `0.1149` | 669,340.00 USD | 669,340.00 USD | 0.00 USD | 10,560.00 USD | 0.00 USD | 72,860.00 USD |
| `1D` | `0.1151` | 589,090.00 USD | 589,090.00 USD | 0.00 USD | 21,360.00 USD | 14,620.00 USD | 49,210.00 USD |
| `7D` | `0.1151` | 894,670.00 USD | 894,670.00 USD | 0.00 USD | 92,570.00 USD | 4,210.00 USD | 128,550.00 USD |
| `1D` | `0.1153` | 723,190.00 USD | 723,190.00 USD | 0.00 USD | 37,440.00 USD | 28,670.00 USD | 67,990.00 USD |
| `7D` | `0.1153` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 153,720.00 USD | 8,400.00 USD | 139,800.00 USD |
| `1D` | `0.1155` | 852,620.00 USD | 852,620.00 USD | 0.00 USD | 48,310.00 USD | 27,080.00 USD | 54,040.00 USD |
| `7D` | `0.1155` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 149,360.00 USD | 40,110.00 USD | 105,680.00 USD |
| `1D` | `0.1157` | 936,580.00 USD | 936,580.00 USD | 0.00 USD | 37,790.00 USD | 12,010.00 USD | 34,150.00 USD |
| `7D` | `0.1157` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 155,250.00 USD | 3,760.00 USD | 48,220.00 USD |
| `1D` | `0.1159` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 27,270.00 USD | 12,000.00 USD | 25,180.00 USD |
| `7D` | `0.1159` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 105,000.00 USD | 12,710.00 USD | 53,290.00 USD |
| `1D` | `0.1161` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 30,570.00 USD | 6,970.00 USD | 36,480.00 USD |
| `7D` | `0.1161` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 146,810.00 USD | 37,250.00 USD | 99,980.00 USD |
| `1D` | `0.1163` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 18,210.00 USD | 14,540.00 USD | 17,410.00 USD |
| `7D` | `0.1163` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 66,560.00 USD | 11,460.00 USD | 68,760.00 USD |
| `1D` | `0.1165` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 14,300.00 USD | 14,710.00 USD | 5,480.00 USD |
| `7D` | `0.1165` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 68,620.00 USD | 35,720.00 USD | 27,180.00 USD |
| `1D` | `0.1167` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 15,040.00 USD | 17,950.00 USD | 6,140.00 USD |
| `7D` | `0.1167` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 79,610.00 USD | 21,620.00 USD | 41,250.00 USD |
| `1D` | `0.1169` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 16,040.00 USD | 6,020.00 USD | 18,200.00 USD |
| `7D` | `0.1169` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 65,340.00 USD | 14,840.00 USD | 86,730.00 USD |
| `1D` | `0.1171` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 17,090.00 USD | 4,520.00 USD | 4,530.00 USD |
| `7D` | `0.1171` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 57,350.00 USD | 11,370.00 USD | 35,080.00 USD |
| `1D` | `0.1173` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 14,960.00 USD | 8,910.00 USD | 11,410.00 USD |
| `7D` | `0.1173` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 40,860.00 USD | 9,190.00 USD | 36,700.00 USD |
| `1D` | `0.1175` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 11,510.00 USD | 17,150.00 USD | 24,370.00 USD |
| `7D` | `0.1175` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 38,840.00 USD | 12,300.00 USD | 58,660.00 USD |
| `1D` | `0.1177` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 19,300.00 USD | 8,560.00 USD | 16,790.00 USD |
| `7D` | `0.1177` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 33,330.00 USD | 20,350.00 USD | 44,380.00 USD |
| `1D` | `0.1179` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 19,180.00 USD | 5,840.00 USD | 14,460.00 USD |
| `7D` | `0.1179` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 66,670.00 USD | 10,940.00 USD | 23,430.00 USD |
| `1D` | `0.1181` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 15,480.00 USD | 6,030.00 USD | 15,120.00 USD |
| `7D` | `0.1181` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 22,290.00 USD | 15,780.00 USD | 17,730.00 USD |
| `1D` | `0.1183` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 7,310.00 USD | 1,400.00 USD | 9,120.00 USD |
| `7D` | `0.1183` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 4,040.00 USD | 1,800.00 USD | 39,630.00 USD |
| `1D` | `0.1185` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 8,760.00 USD | 7,830.00 USD | 13,320.00 USD |
| `7D` | `0.1185` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 3,880.00 USD | 5,130.00 USD | 22,280.00 USD |
| `1D` | `0.1187` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 11,520.00 USD | 8,520.00 USD | 11,690.00 USD |
| `7D` | `0.1187` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 5,620.00 USD | 15,370.00 USD | 32,090.00 USD |
| `1D` | `0.1189` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 4,220.00 USD | 3,060.00 USD | 4,390.00 USD |
| `7D` | `0.1189` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 27,240.00 USD | 15,060.00 USD | 3,240.00 USD |
| `1D` | `0.1191` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 4,940.00 USD | 6,690.00 USD | 3,490.00 USD |
| `7D` | `0.1191` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 22,650.00 USD | 15,330.00 USD | 109,070.00 USD |
| `1D` | `0.1193` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 4,720.00 USD | 2,080.00 USD | 3,810.00 USD |
| `7D` | `0.1193` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 21,260.00 USD | 0.00 USD | 9,460.00 USD |
| `1D` | `0.1195` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 9,550.00 USD | 3,210.00 USD | 2,760.00 USD |
| `7D` | `0.1195` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 11,190.00 USD | 1,780.00 USD | 29,550.00 USD |
| `1D` | `0.1197` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 1,040.00 USD | 105.90 USD |
| `7D` | `0.1197` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 6,780.00 USD | 10,800.00 USD | 14,080.00 USD |
| `1D` | `0.1199` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 3,050.00 USD | 3,050.00 USD |
| `7D` | `0.1199` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 9,100.00 USD | 0.00 USD | 64,690.00 USD |
| `1D` | `0.1201` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 6,460.00 USD | 1,070.00 USD | 8,190.00 USD |
| `7D` | `0.1201` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 114,140.00 USD | 16,380.00 USD | 29,030.00 USD |
| `1D` | `0.1203` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 5,670.00 USD | 413.94 USD | 2,700.00 USD |
| `7D` | `0.1203` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 70,770.00 USD | 29,250.00 USD | 6,330.00 USD |
| `1D` | `0.1205` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 2,250.00 USD | 1,670.00 USD | 750.19 USD |
| `7D` | `0.1205` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 86,480.00 USD | 48,720.00 USD | 128,340.00 USD |
| `1D` | `0.1207` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 3,510.00 USD | 524.23 USD | 885.46 USD |
| `7D` | `0.1207` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 12,460.00 USD | 19,400.00 USD | 59,650.00 USD |
| `1D` | `0.1209` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 636.93 USD | 1,370.00 USD | 2,200.00 USD |
| `7D` | `0.1209` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 85,160.00 USD | 19,340.00 USD | 94,160.00 USD |
| `1D` | `0.1211` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 3,340.00 USD | 2,600.00 USD | 3,230.00 USD |
| `7D` | `0.1211` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 27,400.00 USD | 16,260.00 USD | 29,580.00 USD |
| `1D` | `0.1213` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 1,550.00 USD | 1,220.00 USD | 10,450.00 USD |
| `7D` | `0.1213` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 23,920.00 USD | 26,740.00 USD | 24,260.00 USD |
| `1D` | `0.1215` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD | 4,190.00 USD |
| `7D` | `0.1215` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 5,900.00 USD | 6,620.00 USD | 59,120.00 USD |
| `1D` | `0.1217` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 2,420.00 USD | 624.33 USD | 7,700.00 USD |
| `7D` | `0.1217` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 18,490.00 USD | 23,600.00 USD | 11,230.00 USD |
| `1D` | `0.1219` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 2,320.00 USD | 718.82 USD | 10,030.00 USD |
| `7D` | `0.1219` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 26,700.00 USD | 5,500.00 USD | 38,090.00 USD |
| `1D` | `0.1221` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 4,680.00 USD | 2,940.00 USD | 3,660.00 USD |
| `7D` | `0.1221` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 47,890.00 USD | 21,770.00 USD | 18,930.00 USD |
| `1D` | `0.1223` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 4,190.00 USD | 1,410.00 USD | 7,680.00 USD |
| `7D` | `0.1223` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 103,180.00 USD | 36,290.00 USD | 48,470.00 USD |
| `1D` | `0.1225` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1225` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 43,040.00 USD | 24,950.00 USD | 5,210.00 USD |
| `1D` | `0.1227` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1227` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 68,750.00 USD | 31,790.00 USD | 55,610.00 USD |
| `1D` | `0.1229` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 403.62 USD | 1,090.00 USD |
| `7D` | `0.1229` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 77,860.00 USD | 40,000.00 USD | 43,220.00 USD |
| `1D` | `0.1231` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 430.11 USD | 793.30 USD |
| `7D` | `0.1231` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 29,380.00 USD | 31,660.00 USD | 30,420.00 USD |
| `1D` | `0.1233` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 2,320.00 USD | 3,210.00 USD | 15.85 USD |
| `7D` | `0.1233` | 5,830,000.00 USD | 5,830,000.00 USD | 0.00 USD | 57,130.00 USD | 13,020.00 USD | 40,300.00 USD |
| `1D` | `0.1235` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 1,570.00 USD | 1,240.00 USD | 3,370.00 USD |
| `7D` | `0.1235` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 10,950.00 USD | 6,400.00 USD | 8,900.00 USD |
| `1D` | `0.1237` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 1,560.00 USD | 0.00 USD |
| `7D` | `0.1237` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 4,080.00 USD | 9,720.00 USD | 3,030.00 USD |
| `1D` | `0.1239` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 4,900.00 USD | 724.40 USD | 629.61 USD |
| `7D` | `0.1239` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 8,780.00 USD | 1,270.00 USD | 220.25 USD |
| `1D` | `0.1241` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 2,790.00 USD | 1,830.00 USD | 4,320.00 USD |
| `7D` | `0.1241` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 6,830.00 USD | 9,690.00 USD | 2,450.00 USD |
| `1D` | `0.1243` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 1,660.00 USD | 4,600.00 USD | 7,510.00 USD |
| `7D` | `0.1243` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 11,450.00 USD | 4,530.00 USD | 4,700.00 USD |
| `1D` | `0.1245` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 6,600.00 USD | 3,420.00 USD | 5,530.00 USD |
| `7D` | `0.1245` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 26,080.00 USD | 11,090.00 USD | 13,000.00 USD |
| `1D` | `0.1247` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 2,580.00 USD | 1,320.00 USD | 4,750.00 USD |
| `7D` | `0.1247` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 24,470.00 USD | 19,030.00 USD | 9,630.00 USD |
| `1D` | `0.1249` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 1,190.00 USD | 1,560.00 USD |
| `7D` | `0.1249` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 13,440.00 USD | 5,480.00 USD | 5,680.00 USD |
| `1D` | `0.1251` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 4,600.00 USD | 932.33 USD | 3,070.00 USD |
| `7D` | `0.1251` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 7,660.00 USD | 5,070.00 USD | 11,120.00 USD |
| `1D` | `0.1253` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 855.19 USD | 2,500.00 USD | 3,560.00 USD |
| `7D` | `0.1253` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 11,420.00 USD | 2,100.00 USD | 14,010.00 USD |
| `1D` | `0.1255` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 2,780.00 USD | 1,590.00 USD | 1,580.00 USD |
| `7D` | `0.1255` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 2,250.00 USD | 13,990.00 USD | 91.62 USD |
| `1D` | `0.1257` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 1,140.00 USD | 0.00 USD | 0.01 USD |
| `7D` | `0.1257` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 15,610.00 USD | 5,200.00 USD | 163.16 USD |
| `1D` | `0.1259` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 962.72 USD | 1,690.00 USD | 22.77 USD |
| `7D` | `0.1259` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 154.62 USD |
| `1D` | `0.1261` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1261` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | 3,530.00 USD |
| `7D` | `0.1263` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,100.00 USD |
| `1D` | `0.1264` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 1,300.00 USD | 694.78 USD | 0.00 USD |
| `7D` | `0.1265` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 2,710.00 USD | 0.00 USD | 3,260.00 USD |
| `7D` | `0.1267` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD |
| `7D` | `0.1269` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16.21 USD |
| `7D` | `0.1271` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 5,940.00 USD | 0.00 USD | 13.94 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `73.67M` | Total OI Tokens: `663,656,125.8 OP`
  * 1h OI Change: `-2.09%` | 4h OI Change: `-1.70%` | 24h OI Change: `-3.78%`
  * Exchange Breakdown: Binance=`16.71M` | Bybit=`14.25M` | OKX=`4.15M` | Hyperliquid=`3.92M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.34K` | Last 24h: `270.64` | Last 3d: `-2.23K` | Last 7d: `-15.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0079%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0042%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0079%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0090%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `53.67%` | `46.33%` | `1.16` | 667,440.00 USD |
| `15M` | `Binance` | `45.92%` | `54.08%` | `0.85` | 266,690.00 USD |
| `15M` | `OKX` | `59.67%` | `40.33%` | `1.48` | 69,660.00 USD |
| `15M` | `Bybit` | `56.45%` | `43.55%` | `1.30` | 48,020.00 USD |
| `15M` | `KuCoin` | `78.08%` | `21.92%` | `3.56` | 2,930.00 USD |
| `15M` | `Gate` | `27.36%` | `72.64%` | `0.38` | 813.57 USD |
| `15M` | `Bitget` | `60.54%` | `39.46%` | `1.53` | 9,200.00 USD |
| `15M` | `BingX` | `57.99%` | `42.01%` | `1.38` | 58,910.00 USD |
| `15M` | `MEXC` | `23.63%` | `76.37%` | `0.31` | 20,660.00 USD |
| `15M` | `Bitunix` | `40.47%` | `59.53%` | `0.68` | 6,590.00 USD |
| `15M` | `Hyperliquid` | `21.97%` | `78.03%` | `0.28` | 1,630.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `53.36%` | `46.64%` | `1.14` | 138,980.00 USD |
| `15M` | `Crypto.com` | `0%` | `100%` | `0.00` | 0.22 USD |
| `15M` | `WhiteBIT` | `99.31%` | `0.69%` | `143.93` | 42,900.00 USD |
| `15M` | `HTX` | `83.04%` | `16.96%` | `4.90` | 31.03 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `100%` | `0%` | `1.00` | 127.94 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 5.50 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 275.48 USD |
| `15M` | `Whale Positions` | `45.92%` | `54.08%` | `0.85` | 266,690.00 USD |
| `15M` | `Global Accounts` | `53.67%` | `46.33%` | `1.16` | 667,440.00 USD |
| `1H` | `OP` | `49.32%` | `50.68%` | `0.97` | 5,510,000.00 USD |
| `1H` | `Binance` | `46.27%` | `53.73%` | `0.86` | 2,100,000.00 USD |
| `1H` | `OKX` | `39.25%` | `60.75%` | `0.65` | 567,360.00 USD |
| `1H` | `Bybit` | `54.28%` | `45.72%` | `1.19` | 596,850.00 USD |
| `1H` | `KuCoin` | `47.77%` | `52.23%` | `0.91` | 18,040.00 USD |
| `1H` | `Gate` | `39.77%` | `60.23%` | `0.66` | 47,790.00 USD |
| `1H` | `Bitget` | `46.97%` | `53.03%` | `0.89` | 95,530.00 USD |
| `1H` | `BingX` | `60.87%` | `39.13%` | `1.56` | 242,100.00 USD |
| `1H` | `MEXC` | `54.42%` | `45.58%` | `1.19` | 495,850.00 USD |
| `1H` | `Bitunix` | `48.84%` | `51.16%` | `0.95` | 46,990.00 USD |
| `1H` | `Hyperliquid` | `35.42%` | `64.58%` | `0.55` | 44,860.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.14%` | `52.86%` | `0.89` | 1,080,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `100%` | `0.00` | 0.44 USD |
| `1H` | `WhiteBIT` | `97.53%` | `2.47%` | `39.49` | 162,840.00 USD |
| `1H` | `HTX` | `15.34%` | `84.66%` | `0.18` | 123.59 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `7%` | `93%` | `0.08` | 4,000.00 USD |
| `1H` | `Aster` | `0.41%` | `99.59%` | `0.00` | 1,360.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `21.38%` | `78.62%` | `0.27` | 2,800.00 USD |
| `1H` | `Whale Positions` | `46.27%` | `53.73%` | `0.86` | 2,100,000.00 USD |
| `1H` | `Global Accounts` | `49.32%` | `50.68%` | `0.97` | 5,510,000.00 USD |
| `4H` | `OP` | `50.20%` | `49.80%` | `1.01` | 24,220,000.00 USD |
| `4H` | `Binance` | `48.74%` | `51.26%` | `0.95` | 8,740,000.00 USD |
| `4H` | `OKX` | `50.01%` | `49.99%` | `1.00` | 2,980,000.00 USD |
| `4H` | `Bybit` | `50.68%` | `49.32%` | `1.03` | 2,450,000.00 USD |
| `4H` | `KuCoin` | `25.47%` | `74.53%` | `0.34` | 98,080.00 USD |
| `4H` | `Gate` | `54.78%` | `45.22%` | `1.21` | 264,730.00 USD |
| `4H` | `Bitget` | `45.2%` | `54.8%` | `0.82` | 563,380.00 USD |
| `4H` | `BingX` | `41.33%` | `58.67%` | `0.70` | 1,840,000.00 USD |
| `4H` | `MEXC` | `49.52%` | `50.48%` | `0.98` | 1,740,000.00 USD |
| `4H` | `Bitunix` | `48.55%` | `51.45%` | `0.94` | 262,920.00 USD |
| `4H` | `Hyperliquid` | `77.66%` | `22.34%` | `3.48` | 335,210.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.52%` | `50.48%` | `0.98` | 4,300,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `100%` | `0.00` | 3.15 USD |
| `4H` | `WhiteBIT` | `95.54%` | `4.46%` | `21.42` | 624,970.00 USD |
| `4H` | `HTX` | `50.33%` | `49.67%` | `1.01` | 3,800.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `31.33%` | `68.67%` | `0.46` | 17,740.00 USD |
| `4H` | `Aster` | `4.93%` | `95.07%` | `0.05` | 4,800.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `45.35%` | `54.65%` | `0.83` | 15,300.00 USD |
| `4H` | `Whale Positions` | `48.74%` | `51.26%` | `0.95` | 8,740,000.00 USD |
| `4H` | `Global Accounts` | `50.20%` | `49.80%` | `1.01` | 24,220,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1136` | `0.1136` | `0.1136` | `0.1141` | `0.1130` | 571,492.98 USD | 299,278.35 USD | 272,214.63 USD | 27,063.72 USD | `+4.74%` | `24B / 17S` |
| `0:00 UTC` | `0.1137` | `0.1140` | `0.1137` | `0.1149` | `0.1134` | 877,269.44 USD | 486,783.19 USD | 390,486.24 USD | 96,296.95 USD | `+10.98%` | `34B / 22S` |
| `5:00 UTC` | `0.1134` | `0.1136` | `0.1134` | `0.1142` | `0.1132` | 635,625.25 USD | 325,080.19 USD | 310,545.06 USD | 14,535.13 USD | `+2.29%` | `15B / 17S` |
| `0:00 UTC` | `0.1133` | `0.1131` | `0.1133` | `0.1135` | `0.1126` | 680,945.05 USD | 236,805.84 USD | 444,139.21 USD | -207,333.38 USD | `-30.45%` | `14B / 19S` |
| `5:00 UTC` | `0.1128` | `0.1128` | `0.1128` | `0.1130` | `0.1127` | 243,648.48 USD | 108,202.11 USD | 135,446.38 USD | -27,244.27 USD | `-11.18%` | `2B / 9S` |
| `0:00 UTC` | `0.1126` | `0.1127` | `0.1126` | `0.1132` | `0.1123` | 269,778.58 USD | 124,825.75 USD | 144,952.84 USD | -20,127.09 USD | `-7.46%` | `11B / 20S` |
| `5:00 UTC` | `0.1123` | `0.1122` | `0.1123` | `0.1124` | `0.1119` | 385,611.74 USD | 157,293.82 USD | 228,317.92 USD | -71,024.10 USD | `-18.42%` | `5B / 10S` |
| `0:00 UTC` | `0.1114` | `0.1117` | `0.1114` | `0.1124` | `0.1110` | 525,538.44 USD | 243,812.31 USD | 281,726.13 USD | -37,913.82 USD | `-7.21%` | `25B / 41S` |
| `5:00 UTC` | `0.1107` | `0.1107` | `0.1107` | `0.1112` | `0.1101` | 919,895.36 USD | 440,104.81 USD | 479,790.55 USD | -39,685.74 USD | `-4.31%` | `22B / 21S` |
| `0:00 UTC` | `0.1113` | `0.1110` | `0.1113` | `0.1113` | `0.1108` | 239,678.37 USD | 112,001.98 USD | 127,676.39 USD | -15,674.41 USD | `-6.54%` | `11B / 6S` |

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
| `5m` | -3,180.00 USD | 5,740.00 USD | **`ACCUMULATION`** |
| `15m` | 5,870.00 USD | -1,690.00 USD | **`ACCUMULATION`** |
| `30m` | -28,030.00 USD | -65,740.00 USD | **`DISTRIBUTION`** |
| `1h` | -20,410.00 USD | -222,250.00 USD | **`DISTRIBUTION`** |
| `2h` | -41,990.00 USD | -585,140.00 USD | **`DISTRIBUTION`** |
| `4h` | 118,160.00 USD | -222,040.00 USD | **`DISTRIBUTION`** |
| `6h` | 211,800.00 USD | 408,890.00 USD | **`ACCUMULATION`** |
| `8h` | 225,540.00 USD | 542,760.00 USD | **`ACCUMULATION`** |
| `12h` | 244,760.00 USD | 635,390.00 USD | **`ACCUMULATION`** |
| `24h` | 157,610.00 USD | -1,030,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -128,520.00 USD | -9,820,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,570,000.00 USD | -78,650,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-3.18K` | 15m=`+5.87K` | 1h=`-20.41K` | 24h=`+157.61K`
* Futures Capital Netflows: 5m=`+5.74K` | 15m=`-1.69K` | 1h=`-222.25K` | 24h=`-1.03M`
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
  * `2026-10-29 23:30:59 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:59 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:59 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:59 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:54:59 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:44:59 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:40:59 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:41:59 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:41:59 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:41:59 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:41:59 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
