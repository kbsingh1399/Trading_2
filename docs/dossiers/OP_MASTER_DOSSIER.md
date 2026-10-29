# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 00:20:14 IST` (`2026-10-29 18:50:14 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1104` | `0.1104` | `0.1101` | `0.1103` | `601,103` | 66,256.63 USD | -6,798.28 USD | `-10.26%` | -960,851.77 USD | `+0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.1103` | `0.1103` | `0.1094` | `0.1097` | `3,423,994` | 375,927.18 USD | -90,349.62 USD | `-24.03%` | -1,051,201.39 USD | `-1.69` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1097` | `0.1097` | `0.1096` | `0.1096` | `86,228` | 9,455.34 USD | -3,169.39 USD | `-33.52%` | -1,054,370.78 USD | `+0.28` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1112` | `0.1113` | `0.1106` | `0.1110` | `2,352,924` | 261,230.00 USD | -13,482.93 USD | `-5.16%` | -896,880.21 USD | `-0.17` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1110` | `0.1112` | `0.1101` | `0.1103` | `2,407,060` | 266,281.73 USD | -38,647.08 USD | `-14.51%` | -935,527.29 USD | `-0.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1103` | `0.1103` | `0.1094` | `0.1096` | `3,510,287` | 385,389.64 USD | -93,526.13 USD | `-24.27%` | -1,029,053.43 USD | `-1.04` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1140` | `0.1148` | `0.1126` | `0.1129` | `21,471,756` | 2,437,488.22 USD | -123,745.56 USD | `-5.08%` | -700,951.75 USD | `-0.29` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1129` | `0.1132` | `0.1101` | `0.1112` | `18,847,741` | 2,100,824.13 USD | -168,750.74 USD | `-8.03%` | -869,702.50 USD | `-0.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1112` | `0.1113` | `0.1094` | `0.1096` | `8,270,207` | 912,894.25 USD | -145,649.02 USD | `-15.95%` | -1,015,351.52 USD | `-0.32` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,229,700.44 USD | `+0.64` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -888,444.84 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1096` | `48,589,768` | 5,451,213.73 USD | -438,152.45 USD | `-8.04%` | -1,326,597.29 USD | `-0.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1131` | `0.1136` | `0.1072` | `0.1085` | `76,338,549` | 8,353,905.81 USD | -1,528,374.61 USD | `-18.30%` | -1,480,991.26 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1085` | `0.1106` | `0.1071` | `0.1076` | `47,048,931` | 5,111,570.05 USD | 108,567.99 USD | `+2.12%` | -1,372,423.27 USD | `+0.75` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,229,700.44 USD | `+0.64` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -888,444.84 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1099` | `51,518,581` | 5,772,568.94 USD | -345,523.46 USD | `-5.99%` | -1,233,968.30 USD | `-0.22` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:15:45 IST` |

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
| `7D` | `Long Liquidation` | `0.0967` | 3,960,000.00 USD | 3,960,000.00 USD | 3,770.00 USD | 2,660.00 USD | 2,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0969` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 2,810.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 2,000.00 USD | 34.36 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0973` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0975` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 1,160.00 USD | 4,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0975` | 12,670.00 USD | 51,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0977` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 5,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0979` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 1,530.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0981` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0983` | 1,930,000.00 USD | 1,930,000.00 USD | 3,250.00 USD | 1,510.00 USD | 9,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 3,900,000.00 USD | 3,900,000.00 USD | 7,990.00 USD | 1,230.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0985` | 1,920,000.00 USD | 1,920,000.00 USD | 5,670.00 USD | 413.94 USD | 2,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0985` | 3,890,000.00 USD | 3,890,000.00 USD | 7,110.00 USD | 0.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0985` | 19,960.00 USD | 38,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0987` | 1,910,000.00 USD | 1,910,000.00 USD | 7,790.00 USD | 2,190.00 USD | 3,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0987` | 3,870,000.00 USD | 3,870,000.00 USD | 5,390.00 USD | 9,190.00 USD | 37,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0989` | 1,890,000.00 USD | 1,890,000.00 USD | 636.93 USD | 1,980.00 USD | 2,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 3,820,000.00 USD | 3,820,000.00 USD | 12,260.00 USD | 4,520.00 USD | 27,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0991` | 1,890,000.00 USD | 1,890,000.00 USD | 3,340.00 USD | 2,600.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0991` | 3,780,000.00 USD | 3,780,000.00 USD | 14,350.00 USD | 10,350.00 USD | 13,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0993` | 1,880,000.00 USD | 1,880,000.00 USD | 1,550.00 USD | 1,220.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0993` | 3,740,000.00 USD | 3,740,000.00 USD | 23,920.00 USD | 10,140.00 USD | 24,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0995` | 1,870,000.00 USD | 1,870,000.00 USD | 2,740.00 USD | 624.33 USD | 9,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 3,680,000.00 USD | 3,680,000.00 USD | 13,090.00 USD | 6,160.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0997` | 1,850,000.00 USD | 1,850,000.00 USD | 2,320.00 USD | 718.82 USD | 10,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0997` | 3,640,000.00 USD | 3,640,000.00 USD | 21,100.00 USD | 5,500.00 USD | 32,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0999` | 1,840,000.00 USD | 1,840,000.00 USD | 4,680.00 USD | 2,940.00 USD | 3,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0999` | 3,580,000.00 USD | 3,580,000.00 USD | 14,230.00 USD | 6,540.00 USD | 18,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1001` | 1,830,000.00 USD | 1,830,000.00 USD | 2,660.00 USD | 1,410.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 3,540,000.00 USD | 3,540,000.00 USD | 29,230.00 USD | 3,010.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1003` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 558.39 USD | 16.71 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1003` | 3,490,000.00 USD | 3,490,000.00 USD | 8,010.00 USD | 7,060.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1005` | 1,820,000.00 USD | 1,820,000.00 USD | 1,970.00 USD | 403.62 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1005` | 3,470,000.00 USD | 3,470,000.00 USD | 25,070.00 USD | 11,000.00 USD | 18,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1005` | 427.25 USD | 18,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1007` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 430.11 USD | 882.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 3,420,000.00 USD | 3,420,000.00 USD | 10,260.00 USD | 2,280.00 USD | 14,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1009` | 1,820,000.00 USD | 1,820,000.00 USD | 1,250.00 USD | 3,210.00 USD | 58.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1009` | 3,390,000.00 USD | 3,390,000.00 USD | 15,320.00 USD | 3,070.00 USD | 6,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1011` | 1,810,000.00 USD | 1,810,000.00 USD | 1,570.00 USD | 1,240.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1011` | 3,370,000.00 USD | 3,370,000.00 USD | 4,430.00 USD | 4,720.00 USD | 8,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1013` | 1,810,000.00 USD | 1,810,000.00 USD | 4,900.00 USD | 2,290.00 USD | 655.70 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 3,350,000.00 USD | 3,350,000.00 USD | 12,870.00 USD | 4,030.00 USD | 3,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1015` | 1,800,000.00 USD | 1,800,000.00 USD | 2,790.00 USD | 1,830.00 USD | 4,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1015` | 3,330,000.00 USD | 3,330,000.00 USD | 6,830.00 USD | 965.35 USD | 2,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1015` | 622.37 USD | 17,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1017` | 1,790,000.00 USD | 1,790,000.00 USD | 1,660.00 USD | 4,600.00 USD | 7,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1017` | 3,320,000.00 USD | 3,320,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1019` | 1,770,000.00 USD | 1,770,000.00 USD | 6,600.00 USD | 3,420.00 USD | 5,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1019` | 3,300,000.00 USD | 3,300,000.00 USD | 9,260.00 USD | 5,790.00 USD | 12,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1021` | 1,760,000.00 USD | 1,760,000.00 USD | 2,580.00 USD | 1,320.00 USD | 4,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1021` | 3,270,000.00 USD | 3,270,000.00 USD | 7,900.00 USD | 3,270.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1023` | 1,750,000.00 USD | 1,750,000.00 USD | 4,600.00 USD | 2,120.00 USD | 4,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1023` | 3,250,000.00 USD | 3,250,000.00 USD | 4,030.00 USD | 4,990.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1025` | 1,740,000.00 USD | 1,740,000.00 USD | 855.19 USD | 2,500.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1025` | 3,230,000.00 USD | 3,230,000.00 USD | 1,550.00 USD | 0.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1025` | 17,360.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1027` | 1,730,000.00 USD | 1,730,000.00 USD | 2,780.00 USD | 1,590.00 USD | 1,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1027` | 3,220,000.00 USD | 3,220,000.00 USD | 2,250.00 USD | 2,580.00 USD | 359.07 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1029` | 1,730,000.00 USD | 1,730,000.00 USD | 4,340.00 USD | 705.79 USD | 6,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1029` | 3,220,000.00 USD | 3,220,000.00 USD | 7,420.00 USD | 3,000.00 USD | 332.49 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1031` | 1,710,000.00 USD | 1,710,000.00 USD | 11,600.00 USD | 3,910.00 USD | 8,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1031` | 3,210,000.00 USD | 3,210,000.00 USD | 13,690.00 USD | 5,070.00 USD | 10,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1033` | 1,690,000.00 USD | 1,690,000.00 USD | 8,760.00 USD | 2,790.00 USD | 10,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1033` | 3,180,000.00 USD | 3,180,000.00 USD | 3,880.00 USD | 2,640.00 USD | 15,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1035` | 1,670,000.00 USD | 1,670,000.00 USD | 7,450.00 USD | 6,850.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1035` | 3,150,000.00 USD | 3,150,000.00 USD | 2,710.00 USD | 9,400.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1037` | 1,640,000.00 USD | 1,640,000.00 USD | 2,220.00 USD | 13,000.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1037` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 19,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1039` | 1,620,000.00 USD | 1,620,000.00 USD | 3,660.00 USD | 1,730.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1039` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 5,170.00 USD | 167.04 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1041` | 1,600,000.00 USD | 1,600,000.00 USD | 7,790.00 USD | 6,910.00 USD | 13,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1041` | 3,100,000.00 USD | 3,100,000.00 USD | 5,940.00 USD | 2,910.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1043` | 1,570,000.00 USD | 1,570,000.00 USD | 17,650.00 USD | 5,650.00 USD | 7,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1043` | 3,080,000.00 USD | 3,080,000.00 USD | 15,960.00 USD | 5,980.00 USD | 21,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1045` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 2,600.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1045` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 3,830.00 USD | 15,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1047` | 1,530,000.00 USD | 1,530,000.00 USD | 4,610.00 USD | 2,610.00 USD | 16,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1047` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 1,720.00 USD | 22,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1049` | 1,510,000.00 USD | 1,510,000.00 USD | 21,050.00 USD | 2,430.00 USD | 10,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1049` | 3,000,000.00 USD | 3,000,000.00 USD | 34,790.00 USD | 4,810.00 USD | 35,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1051` | 1,480,000.00 USD | 1,480,000.00 USD | 16,410.00 USD | 8,750.00 USD | 24,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1051` | 2,920,000.00 USD | 2,920,000.00 USD | 17,290.00 USD | 11,500.00 USD | 48,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1053` | 1,430,000.00 USD | 1,430,000.00 USD | 30,920.00 USD | 7,040.00 USD | 25,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1053` | 2,840,000.00 USD | 2,840,000.00 USD | 53,590.00 USD | 29,800.00 USD | 95,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1055` | 1,360,000.00 USD | 1,360,000.00 USD | 23,910.00 USD | 17,450.00 USD | 31,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1055` | 2,660,000.00 USD | 2,660,000.00 USD | 50,090.00 USD | 27,290.00 USD | 126,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1057` | 1,290,000.00 USD | 1,290,000.00 USD | 17,910.00 USD | 21,720.00 USD | 44,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1057` | 2,460,000.00 USD | 2,460,000.00 USD | 44,200.00 USD | 45,760.00 USD | 74,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1059` | 1,210,000.00 USD | 1,210,000.00 USD | 15,180.00 USD | 21,000.00 USD | 52,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1059` | 2,300,000.00 USD | 2,300,000.00 USD | 92,510.00 USD | 49,670.00 USD | 114,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1061` | 1,120,000.00 USD | 1,120,000.00 USD | 10,960.00 USD | 9,820.00 USD | 42,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1061` | 2,040,000.00 USD | 2,040,000.00 USD | 38,260.00 USD | 26,050.00 USD | 76,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1063` | 1,050,000.00 USD | 1,050,000.00 USD | 56,400.00 USD | 14,600.00 USD | 48,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1063` | 1,900,000.00 USD | 1,900,000.00 USD | 88,520.00 USD | 38,330.00 USD | 148,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1065` | 935,000.00 USD | 935,000.00 USD | 18,270.00 USD | 14,110.00 USD | 19,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1065` | 1,620,000.00 USD | 1,620,000.00 USD | 91,170.00 USD | 19,700.00 USD | 93,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1067` | 883,110.00 USD | 883,110.00 USD | 9,710.00 USD | 15,160.00 USD | 33,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1067` | 1,420,000.00 USD | 1,420,000.00 USD | 97,290.00 USD | 36,720.00 USD | 67,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1069` | 825,120.00 USD | 825,120.00 USD | 24,070.00 USD | 7,520.00 USD | 34,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1069` | 1,220,000.00 USD | 1,220,000.00 USD | 76,900.00 USD | 32,620.00 USD | 72,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1071` | 758,980.00 USD | 758,980.00 USD | 48,660.00 USD | 4,860.00 USD | 18,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1071` | 1,040,000.00 USD | 1,040,000.00 USD | 119,440.00 USD | 27,240.00 USD | 42,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1073` | 686,550.00 USD | 686,550.00 USD | 8,740.00 USD | 10,680.00 USD | 20,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1073` | 846,010.00 USD | 846,010.00 USD | 58,480.00 USD | 17,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1075` | 646,230.00 USD | 646,230.00 USD | 26,670.00 USD | 6,770.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1075` | 769,820.00 USD | 769,820.00 USD | 20,750.00 USD | 3,500.00 USD | 58.62 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1077` | 598,870.00 USD | 598,870.00 USD | 7,300.00 USD | 13,880.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1077` | 745,510.00 USD | 745,510.00 USD | 0.00 USD | 0.00 USD | 8,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1079` | 563,710.00 USD | 563,710.00 USD | 9,370.00 USD | 13,900.00 USD | 29,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1079` | 736,860.00 USD | 736,860.00 USD | 128,090.00 USD | 23,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1081` | 511,230.00 USD | 511,230.00 USD | 17,730.00 USD | 7,210.00 USD | 50,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1081` | 584,790.00 USD | 584,790.00 USD | 205,390.00 USD | 11,660.00 USD | 28,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1083` | 436,290.00 USD | 436,290.00 USD | 20,890.00 USD | 6,690.00 USD | 33,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1083` | 338,880.00 USD | 338,880.00 USD | 94,800.00 USD | 2,110.00 USD | 42,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1085` | 374,860.00 USD | 374,860.00 USD | 22,270.00 USD | 13,850.00 USD | 65,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1085` | 199,560.00 USD | 199,560.00 USD | 15,920.00 USD | 4,200.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1087` | 273,740.00 USD | 273,740.00 USD | 44,350.00 USD | 8,210.00 USD | 44,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1087` | 179,420.00 USD | 179,420.00 USD | 55,430.00 USD | 6,210.00 USD | 60,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1089` | 176,510.00 USD | 176,510.00 USD | 30,880.00 USD | 17,080.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1089` | 57,700.00 USD | 57,700.00 USD | 5,290.00 USD | 14,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1091` | 87,010.00 USD | 87,010.00 USD | 33,700.00 USD | 6,410.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1091` | 37,840.00 USD | 37,840.00 USD | 16,310.00 USD | 3,800.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1093` | 38,730.00 USD | 38,730.00 USD | 15,480.00 USD | 3,890.00 USD | 8,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1093` | 8,730.00 USD | 8,730.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1095` | 10,860.00 USD | 10,860.00 USD | 0.00 USD | 0.00 USD | 10,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1101` | 6,260.00 USD | 6,260.00 USD | 0.00 USD | 0.00 USD | 6,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1103` | 40,060.00 USD | 40,060.00 USD | 23,720.00 USD | 4,000.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 27,370.00 USD | 27,370.00 USD | 27,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1105` | 47,110.00 USD | 47,110.00 USD | 0.00 USD | 10,030.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1107` | 88,520.00 USD | 88,520.00 USD | 0.00 USD | 12,720.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1107` | 59,620.00 USD | 59,620.00 USD | 0.00 USD | 12,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 72,050.00 USD | 72,050.00 USD | 0.00 USD | 12,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1113` | 138,870.00 USD | 138,870.00 USD | 15,810.00 USD | 3,630.00 USD | 30,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1115` | 143,630.00 USD | 143,630.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1117` | 192,280.00 USD | 192,280.00 USD | 0.00 USD | 24,680.00 USD | 23,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1117` | 111,320.00 USD | 111,320.00 USD | 0.00 USD | 22,780.00 USD | 16,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1119` | 241,510.00 USD | 241,510.00 USD | 26,390.00 USD | 5,030.00 USD | 17,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1119` | 154,420.00 USD | 154,420.00 USD | 25,250.00 USD | 7,050.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1121` | 248,700.00 USD | 248,700.00 USD | 4,120.00 USD | 3,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 175,590.00 USD | 175,590.00 USD | 0.00 USD | 0.00 USD | 21,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1123` | 281,620.00 USD | 281,620.00 USD | 29,460.00 USD | 0.00 USD | 3,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1123` | 225,750.00 USD | 225,750.00 USD | 0.00 USD | 23,980.00 USD | 26,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1125` | 288,650.00 USD | 288,650.00 USD | 0.00 USD | 7,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1125` | 254,580.00 USD | 254,580.00 USD | 0.00 USD | 0.00 USD | 28,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1127` | 292,880.00 USD | 292,880.00 USD | 0.00 USD | 1,250.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1129` | 298,350.00 USD | 298,350.00 USD | 5,450.00 USD | 0.00 USD | 22.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1131` | 333,850.00 USD | 333,850.00 USD | 17,560.00 USD | 6,360.00 USD | 11,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1131` | 282,140.00 USD | 282,140.00 USD | 12,540.00 USD | 0.00 USD | 15,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1133` | 386,490.00 USD | 386,490.00 USD | 6,530.00 USD | 22,520.00 USD | 23,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 287,590.00 USD | 287,590.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1135` | 393,410.00 USD | 393,410.00 USD | 4,040.00 USD | 2,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1135` | 302,110.00 USD | 302,110.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1137` | 394,310.00 USD | 394,310.00 USD | 0.00 USD | 856.93 USD | 38.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1139` | 408,640.00 USD | 408,640.00 USD | 0.00 USD | 0.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1141` | 435,000.00 USD | 435,000.00 USD | 13,860.00 USD | 2,800.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1141` | 320,030.00 USD | 320,030.00 USD | 10,380.00 USD | 0.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1143` | 479,570.00 USD | 479,570.00 USD | 13,630.00 USD | 24,200.00 USD | 6,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1143` | 398,640.00 USD | 398,640.00 USD | 0.00 USD | 0.00 USD | 78,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1145` | 535,550.00 USD | 535,550.00 USD | 8,350.00 USD | 10,790.00 USD | 36,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 552,890.00 USD | 552,890.00 USD | 10,360.00 USD | 2,730.00 USD | 141,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1147` | 577,920.00 USD | 577,920.00 USD | 6,800.00 USD | 8,840.00 USD | 26,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1147` | 697,170.00 USD | 697,170.00 USD | 9,880.00 USD | 0.00 USD | 134,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1149` | 639,900.00 USD | 639,900.00 USD | 35,170.00 USD | 624.71 USD | 26,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1149` | 780,600.00 USD | 780,600.00 USD | 10,560.00 USD | 0.00 USD | 72,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1151` | 722,370.00 USD | 722,370.00 USD | 21,360.00 USD | 14,620.00 USD | 46,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 1,010,000.00 USD | 1,010,000.00 USD | 92,570.00 USD | 4,210.00 USD | 128,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1153` | 859,220.00 USD | 859,220.00 USD | 39,450.00 USD | 29,420.00 USD | 67,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1153` | 1,310,000.00 USD | 1,310,000.00 USD | 153,720.00 USD | 8,400.00 USD | 139,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1155` | 988,590.00 USD | 988,590.00 USD | 48,310.00 USD | 27,080.00 USD | 53,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1155` | 1,600,000.00 USD | 1,600,000.00 USD | 149,360.00 USD | 40,110.00 USD | 105,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1157` | 1,060,000.00 USD | 1,060,000.00 USD | 37,790.00 USD | 12,010.00 USD | 25,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 1,810,000.00 USD | 1,810,000.00 USD | 155,250.00 USD | 3,760.00 USD | 48,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1159` | 1,130,000.00 USD | 1,130,000.00 USD | 27,270.00 USD | 12,000.00 USD | 25,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1159` | 1,970,000.00 USD | 1,970,000.00 USD | 97,270.00 USD | 12,710.00 USD | 53,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1161` | 1,200,000.00 USD | 1,200,000.00 USD | 30,570.00 USD | 6,970.00 USD | 36,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1161` | 2,260,000.00 USD | 2,260,000.00 USD | 146,810.00 USD | 37,250.00 USD | 99,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1163` | 1,250,000.00 USD | 1,250,000.00 USD | 18,210.00 USD | 14,540.00 USD | 17,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 2,400,000.00 USD | 2,400,000.00 USD | 66,560.00 USD | 11,460.00 USD | 68,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1165` | 1,290,000.00 USD | 1,290,000.00 USD | 14,300.00 USD | 14,710.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1165` | 2,540,000.00 USD | 2,540,000.00 USD | 68,620.00 USD | 35,720.00 USD | 27,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1167` | 1,320,000.00 USD | 1,320,000.00 USD | 12,360.00 USD | 17,950.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1167` | 2,680,000.00 USD | 2,680,000.00 USD | 79,610.00 USD | 21,620.00 USD | 41,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1169` | 1,360,000.00 USD | 1,360,000.00 USD | 16,040.00 USD | 6,020.00 USD | 14,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 2,850,000.00 USD | 2,850,000.00 USD | 65,340.00 USD | 14,840.00 USD | 86,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1171` | 1,390,000.00 USD | 1,390,000.00 USD | 17,090.00 USD | 4,520.00 USD | 4,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1171` | 2,950,000.00 USD | 2,950,000.00 USD | 57,350.00 USD | 11,370.00 USD | 35,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1173` | 1,420,000.00 USD | 1,420,000.00 USD | 14,960.00 USD | 8,910.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1173` | 3,040,000.00 USD | 3,040,000.00 USD | 40,860.00 USD | 9,190.00 USD | 36,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1175` | 1,470,000.00 USD | 1,470,000.00 USD | 11,510.00 USD | 17,150.00 USD | 24,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 3,150,000.00 USD | 3,150,000.00 USD | 38,840.00 USD | 12,300.00 USD | 58,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1177` | 1,520,000.00 USD | 1,520,000.00 USD | 19,300.00 USD | 8,560.00 USD | 16,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1177` | 3,240,000.00 USD | 3,240,000.00 USD | 33,330.00 USD | 20,350.00 USD | 44,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1179` | 1,560,000.00 USD | 1,560,000.00 USD | 19,180.00 USD | 5,840.00 USD | 14,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1179` | 3,340,000.00 USD | 3,340,000.00 USD | 66,670.00 USD | 10,940.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1181` | 1,590,000.00 USD | 1,590,000.00 USD | 15,480.00 USD | 6,030.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 3,400,000.00 USD | 3,400,000.00 USD | 22,290.00 USD | 15,780.00 USD | 17,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1183` | 1,610,000.00 USD | 1,610,000.00 USD | 7,310.00 USD | 1,400.00 USD | 9,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1183` | 3,450,000.00 USD | 3,450,000.00 USD | 4,040.00 USD | 1,800.00 USD | 39,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1185` | 1,640,000.00 USD | 1,640,000.00 USD | 8,760.00 USD | 7,830.00 USD | 13,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1185` | 3,480,000.00 USD | 3,480,000.00 USD | 3,880.00 USD | 5,130.00 USD | 22,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1187` | 1,670,000.00 USD | 1,670,000.00 USD | 11,520.00 USD | 8,520.00 USD | 11,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 3,530,000.00 USD | 3,530,000.00 USD | 5,620.00 USD | 15,370.00 USD | 32,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1189` | 1,690,000.00 USD | 1,690,000.00 USD | 4,220.00 USD | 3,060.00 USD | 4,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1189` | 3,580,000.00 USD | 3,580,000.00 USD | 27,240.00 USD | 15,060.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1191` | 1,700,000.00 USD | 1,700,000.00 USD | 4,940.00 USD | 6,690.00 USD | 3,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1191` | 3,720,000.00 USD | 3,720,000.00 USD | 22,650.00 USD | 15,330.00 USD | 109,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1193` | 1,710,000.00 USD | 1,710,000.00 USD | 4,720.00 USD | 2,080.00 USD | 3,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 3,750,000.00 USD | 3,750,000.00 USD | 21,260.00 USD | 0.00 USD | 9,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1195` | 1,730,000.00 USD | 1,730,000.00 USD | 9,550.00 USD | 3,210.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1195` | 3,800,000.00 USD | 3,800,000.00 USD | 11,190.00 USD | 1,780.00 USD | 29,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1197` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 1,040.00 USD | 139.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1197` | 3,830,000.00 USD | 3,830,000.00 USD | 6,780.00 USD | 10,800.00 USD | 14,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1199` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 3,050.00 USD | 3,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 3,900,000.00 USD | 3,900,000.00 USD | 9,100.00 USD | 0.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1201` | 1,750,000.00 USD | 1,750,000.00 USD | 6,460.00 USD | 1,070.00 USD | 8,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1201` | 4,060,000.00 USD | 4,060,000.00 USD | 114,140.00 USD | 16,380.00 USD | 29,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1203` | 1,760,000.00 USD | 1,760,000.00 USD | 5,670.00 USD | 413.94 USD | 2,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1203` | 4,170,000.00 USD | 4,170,000.00 USD | 70,770.00 USD | 29,250.00 USD | 6,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1205` | 1,760,000.00 USD | 1,760,000.00 USD | 2,250.00 USD | 1,670.00 USD | 766.95 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 4,430,000.00 USD | 4,430,000.00 USD | 86,480.00 USD | 48,720.00 USD | 128,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1207` | 1,770,000.00 USD | 1,770,000.00 USD | 5,540.00 USD | 524.23 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1207` | 4,520,000.00 USD | 4,520,000.00 USD | 12,460.00 USD | 19,400.00 USD | 59,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1209` | 1,780,000.00 USD | 1,780,000.00 USD | 636.93 USD | 1,980.00 USD | 2,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1209` | 4,720,000.00 USD | 4,720,000.00 USD | 85,160.00 USD | 19,340.00 USD | 94,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1211` | 1,790,000.00 USD | 1,790,000.00 USD | 3,340.00 USD | 2,600.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 4,790,000.00 USD | 4,790,000.00 USD | 27,400.00 USD | 16,260.00 USD | 29,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1213` | 1,800,000.00 USD | 1,800,000.00 USD | 1,550.00 USD | 1,220.00 USD | 10,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1213` | 4,870,000.00 USD | 4,870,000.00 USD | 23,920.00 USD | 26,740.00 USD | 24,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1215` | 1,810,000.00 USD | 1,810,000.00 USD | 1,650.00 USD | 0.00 USD | 4,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1215` | 4,940,000.00 USD | 4,940,000.00 USD | 5,900.00 USD | 6,620.00 USD | 59,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1217` | 1,810,000.00 USD | 1,810,000.00 USD | 1,090.00 USD | 624.33 USD | 5,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 4,990,000.00 USD | 4,990,000.00 USD | 18,490.00 USD | 23,600.00 USD | 11,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1219` | 1,830,000.00 USD | 1,830,000.00 USD | 2,320.00 USD | 718.82 USD | 10,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1219` | 5,060,000.00 USD | 5,060,000.00 USD | 26,700.00 USD | 5,500.00 USD | 38,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1221` | 1,840,000.00 USD | 1,840,000.00 USD | 4,680.00 USD | 2,940.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1221` | 5,150,000.00 USD | 5,150,000.00 USD | 47,890.00 USD | 21,770.00 USD | 18,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1223` | 1,840,000.00 USD | 1,840,000.00 USD | 2,660.00 USD | 1,410.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 5,340,000.00 USD | 5,340,000.00 USD | 103,180.00 USD | 36,290.00 USD | 48,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1225` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1225` | 5,410,000.00 USD | 5,410,000.00 USD | 43,040.00 USD | 19,970.00 USD | 5,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 16,900.00 USD | 16,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1227` | 1,850,000.00 USD | 1,850,000.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1227` | 5,560,000.00 USD | 5,560,000.00 USD | 65,240.00 USD | 31,790.00 USD | 55,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1229` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 403.62 USD | 1,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 5,710,000.00 USD | 5,710,000.00 USD | 73,990.00 USD | 35,570.00 USD | 43,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1231` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 430.11 USD | 789.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1231` | 5,810,000.00 USD | 5,810,000.00 USD | 29,380.00 USD | 31,660.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1233` | 1,850,000.00 USD | 1,850,000.00 USD | 1,250.00 USD | 3,210.00 USD | 19.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1233` | 5,920,000.00 USD | 5,920,000.00 USD | 57,130.00 USD | 13,020.00 USD | 40,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1235` | 1,860,000.00 USD | 1,860,000.00 USD | 1,570.00 USD | 1,240.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1235` | 5,940,000.00 USD | 5,940,000.00 USD | 10,950.00 USD | 6,400.00 USD | 8,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1237` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 1,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1237` | 5,960,000.00 USD | 5,960,000.00 USD | 4,080.00 USD | 9,720.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1239` | 1,870,000.00 USD | 1,870,000.00 USD | 4,900.00 USD | 724.40 USD | 627.87 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1239` | 5,970,000.00 USD | 5,970,000.00 USD | 8,780.00 USD | 1,270.00 USD | 220.25 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1241` | 1,880,000.00 USD | 1,880,000.00 USD | 2,790.00 USD | 1,830.00 USD | 4,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1241` | 5,990,000.00 USD | 5,990,000.00 USD | 6,830.00 USD | 9,690.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1243` | 1,890,000.00 USD | 1,890,000.00 USD | 1,660.00 USD | 4,600.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1243` | 6,010,000.00 USD | 6,010,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1245` | 1,910,000.00 USD | 1,910,000.00 USD | 6,600.00 USD | 3,420.00 USD | 5,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1245` | 6,060,000.00 USD | 6,060,000.00 USD | 26,080.00 USD | 11,090.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1247` | 1,920,000.00 USD | 1,920,000.00 USD | 2,580.00 USD | 1,320.00 USD | 4,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1247` | 6,110,000.00 USD | 6,110,000.00 USD | 24,470.00 USD | 19,030.00 USD | 9,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1249` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 1,190.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1249` | 6,140,000.00 USD | 6,140,000.00 USD | 13,440.00 USD | 5,480.00 USD | 5,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1251` | 1,930,000.00 USD | 1,930,000.00 USD | 4,600.00 USD | 932.33 USD | 3,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1251` | 6,160,000.00 USD | 6,160,000.00 USD | 7,660.00 USD | 5,070.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1253` | 6,190,000.00 USD | 6,190,000.00 USD | 11,420.00 USD | 2,100.00 USD | 14,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1255` | 6,210,000.00 USD | 6,210,000.00 USD | 2,250.00 USD | 13,990.00 USD | 91.62 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1257` | 6,230,000.00 USD | 6,230,000.00 USD | 15,610.00 USD | 5,200.00 USD | 156.62 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1259` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 0.00 USD | 154.62 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1261` | 6,230,000.00 USD | 6,230,000.00 USD | 4,270.00 USD | 0.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1263` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1265` | 6,240,000.00 USD | 6,240,000.00 USD | 2,710.00 USD | 0.00 USD | 3,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1267` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1269` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 16.21 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1271` | 6,250,000.00 USD | 6,250,000.00 USD | 5,940.00 USD | 0.00 USD | 13.94 USD | `Tier 1 CEX` |
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
| `7D` | `0.0967` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 3,770.00 USD | 2,660.00 USD | 2,840.00 USD |
| `7D` | `0.0969` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 0.00 USD | 2,810.00 USD | 9,360.00 USD |
| `7D` | `0.0971` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 0.00 USD | 2,000.00 USD | 34.36 USD |
| `7D` | `0.0973` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 0.00 USD | 1,390.00 USD | 2,880.00 USD |
| `7D` | `0.0975` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 0.00 USD | 1,160.00 USD | 4,130.00 USD |
| `7D` | `0.0977` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 5,800.00 USD |
| `7D` | `0.0979` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 0.00 USD | 1,530.00 USD | 5,710.00 USD |
| `7D` | `0.0981` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD |
| `1D` | `0.0983` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 3,250.00 USD | 1,070.00 USD | 9,080.00 USD |
| `7D` | `0.0983` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 7,990.00 USD | 1,230.00 USD | 8,820.00 USD |
| `1D` | `0.0985` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 5,670.00 USD | 413.94 USD | 2,690.00 USD |
| `7D` | `0.0985` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 7,110.00 USD | 0.00 USD | 6,320.00 USD |
| `1D` | `0.0987` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 7,790.00 USD | 2,190.00 USD | 3,310.00 USD |
| `7D` | `0.0987` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 5,390.00 USD | 9,190.00 USD | 37,360.00 USD |
| `1D` | `0.0989` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 2,450.00 USD | 2,550.00 USD | 2,180.00 USD |
| `7D` | `0.0989` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 12,260.00 USD | 4,520.00 USD | 27,240.00 USD |
| `1D` | `0.0991` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 3,340.00 USD | 2,600.00 USD | 3,200.00 USD |
| `7D` | `0.0991` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 14,350.00 USD | 10,350.00 USD | 13,520.00 USD |
| `1D` | `0.0993` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 1,550.00 USD | 1,220.00 USD | 10,400.00 USD |
| `7D` | `0.0993` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 23,920.00 USD | 10,140.00 USD | 24,060.00 USD |
| `1D` | `0.0995` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 2,740.00 USD | 624.33 USD | 9,230.00 USD |
| `7D` | `0.0995` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 13,090.00 USD | 6,160.00 USD | 25,300.00 USD |
| `1D` | `0.0997` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 2,320.00 USD | 718.82 USD | 10,040.00 USD |
| `7D` | `0.0997` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 21,100.00 USD | 5,500.00 USD | 32,960.00 USD |
| `1D` | `0.0999` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 4,680.00 USD | 2,940.00 USD | 3,650.00 USD |
| `7D` | `0.0999` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 14,230.00 USD | 6,540.00 USD | 18,820.00 USD |
| `1D` | `0.1001` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 2,660.00 USD | 1,410.00 USD | 4,250.00 USD |
| `7D` | `0.1001` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 29,230.00 USD | 3,010.00 USD | 10,920.00 USD |
| `1D` | `0.1003` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 0.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1003` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 8,010.00 USD | 7,060.00 USD | 5,210.00 USD |
| `1D` | `0.1005` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 1,970.00 USD | 403.62 USD | 1,100.00 USD |
| `7D` | `0.1005` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 25,070.00 USD | 11,000.00 USD | 18,310.00 USD |
| `1D` | `0.1007` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 0.00 USD | 430.11 USD | 791.00 USD |
| `7D` | `0.1007` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 10,260.00 USD | 2,280.00 USD | 14,060.00 USD |
| `1D` | `0.1009` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 1,250.00 USD | 3,210.00 USD | 61.47 USD |
| `7D` | `0.1009` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 15,320.00 USD | 3,070.00 USD | 6,940.00 USD |
| `1D` | `0.1011` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 1,570.00 USD | 1,240.00 USD | 3,440.00 USD |
| `7D` | `0.1011` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 4,430.00 USD | 4,720.00 USD | 8,900.00 USD |
| `1D` | `0.1013` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 4,900.00 USD | 2,290.00 USD | 627.59 USD |
| `7D` | `0.1013` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 12,870.00 USD | 4,030.00 USD | 3,080.00 USD |
| `1D` | `0.1015` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 2,790.00 USD | 1,830.00 USD | 4,300.00 USD |
| `7D` | `0.1015` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 6,830.00 USD | 965.35 USD | 2,430.00 USD |
| `1D` | `0.1017` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 1,660.00 USD | 4,600.00 USD | 7,550.00 USD |
| `7D` | `0.1017` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,790.00 USD |
| `1D` | `0.1019` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 6,600.00 USD | 3,420.00 USD | 5,640.00 USD |
| `7D` | `0.1019` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 9,260.00 USD | 5,790.00 USD | 12,990.00 USD |
| `1D` | `0.1021` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 2,580.00 USD | 1,320.00 USD | 4,760.00 USD |
| `7D` | `0.1021` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 7,900.00 USD | 3,270.00 USD | 7,150.00 USD |
| `1D` | `0.1023` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 4,600.00 USD | 2,120.00 USD | 4,660.00 USD |
| `7D` | `0.1023` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 4,030.00 USD | 4,990.00 USD | 14,520.00 USD |
| `1D` | `0.1025` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 855.19 USD | 2,500.00 USD | 3,600.00 USD |
| `7D` | `0.1025` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 1,550.00 USD | 0.00 USD | 5,690.00 USD |
| `1D` | `0.1027` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 2,780.00 USD | 1,590.00 USD | 1,640.00 USD |
| `7D` | `0.1027` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 2,250.00 USD | 2,580.00 USD | 359.07 USD |
| `1D` | `0.1029` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 4,340.00 USD | 705.79 USD | 6,310.00 USD |
| `7D` | `0.1029` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 7,420.00 USD | 3,000.00 USD | 332.49 USD |
| `1D` | `0.1031` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 11,600.00 USD | 3,910.00 USD | 8,080.00 USD |
| `7D` | `0.1031` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 13,690.00 USD | 5,070.00 USD | 10,680.00 USD |
| `1D` | `0.1033` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 8,760.00 USD | 2,790.00 USD | 10,450.00 USD |
| `7D` | `0.1033` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 3,880.00 USD | 2,640.00 USD | 15,240.00 USD |
| `1D` | `0.1035` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 7,450.00 USD | 6,850.00 USD | 10,240.00 USD |
| `7D` | `0.1035` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 2,710.00 USD | 9,400.00 USD | 16,150.00 USD |
| `1D` | `0.1037` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 2,220.00 USD | 13,000.00 USD | 9,290.00 USD |
| `7D` | `0.1037` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 19,410.00 USD |
| `1D` | `0.1039` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 3,660.00 USD | 1,730.00 USD | 11,840.00 USD |
| `7D` | `0.1039` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 0.00 USD | 5,170.00 USD | 167.04 USD |
| `1D` | `0.1041` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 7,790.00 USD | 6,910.00 USD | 13,290.00 USD |
| `7D` | `0.1041` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 5,940.00 USD | 2,910.00 USD | 10,820.00 USD |
| `1D` | `0.1043` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 17,650.00 USD | 5,650.00 USD | 7,820.00 USD |
| `7D` | `0.1043` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 15,960.00 USD | 5,980.00 USD | 21,000.00 USD |
| `1D` | `0.1045` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 0.00 USD | 2,600.00 USD | 6,220.00 USD |
| `7D` | `0.1045` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 0.00 USD | 3,830.00 USD | 15,000.00 USD |
| `1D` | `0.1047` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 4,610.00 USD | 2,610.00 USD | 16,580.00 USD |
| `7D` | `0.1047` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 0.00 USD | 1,720.00 USD | 22,650.00 USD |
| `1D` | `0.1049` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 21,050.00 USD | 2,430.00 USD | 10,840.00 USD |
| `7D` | `0.1049` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 34,790.00 USD | 4,810.00 USD | 35,410.00 USD |
| `1D` | `0.1051` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 16,410.00 USD | 8,750.00 USD | 24,230.00 USD |
| `7D` | `0.1051` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 17,290.00 USD | 11,500.00 USD | 48,700.00 USD |
| `1D` | `0.1053` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 30,920.00 USD | 7,040.00 USD | 25,590.00 USD |
| `7D` | `0.1053` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 53,590.00 USD | 29,800.00 USD | 95,610.00 USD |
| `1D` | `0.1055` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 28,440.00 USD | 18,880.00 USD | 33,210.00 USD |
| `7D` | `0.1055` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 50,090.00 USD | 27,290.00 USD | 126,520.00 USD |
| `1D` | `0.1057` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 17,910.00 USD | 21,720.00 USD | 44,560.00 USD |
| `7D` | `0.1057` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 44,200.00 USD | 45,760.00 USD | 74,320.00 USD |
| `1D` | `0.1059` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 15,180.00 USD | 21,000.00 USD | 52,110.00 USD |
| `7D` | `0.1059` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 92,510.00 USD | 49,670.00 USD | 114,120.00 USD |
| `1D` | `0.1061` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 10,960.00 USD | 9,820.00 USD | 42,660.00 USD |
| `7D` | `0.1061` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 38,260.00 USD | 26,050.00 USD | 76,340.00 USD |
| `1D` | `0.1063` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 56,400.00 USD | 14,600.00 USD | 48,830.00 USD |
| `7D` | `0.1063` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 88,520.00 USD | 38,330.00 USD | 148,680.00 USD |
| `1D` | `0.1065` | 949,840.00 USD | 0.00 USD | 949,840.00 USD | 18,270.00 USD | 14,110.00 USD | 19,500.00 USD |
| `7D` | `0.1065` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 91,170.00 USD | 19,700.00 USD | 93,660.00 USD |
| `1D` | `0.1067` | 897,950.00 USD | 0.00 USD | 897,950.00 USD | 9,710.00 USD | 15,160.00 USD | 33,090.00 USD |
| `7D` | `0.1067` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 97,290.00 USD | 36,720.00 USD | 67,520.00 USD |
| `1D` | `0.1069` | 839,990.00 USD | 0.00 USD | 839,990.00 USD | 24,070.00 USD | 7,520.00 USD | 34,470.00 USD |
| `7D` | `0.1069` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 76,900.00 USD | 32,620.00 USD | 72,020.00 USD |
| `1D` | `0.1071` | 773,920.00 USD | 0.00 USD | 773,920.00 USD | 48,660.00 USD | 4,860.00 USD | 18,910.00 USD |
| `7D` | `0.1071` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 119,440.00 USD | 27,240.00 USD | 42,730.00 USD |
| `1D` | `0.1073` | 701,500.00 USD | 0.00 USD | 701,500.00 USD | 8,740.00 USD | 10,680.00 USD | 20,870.00 USD |
| `7D` | `0.1073` | 846,010.00 USD | 0.00 USD | 846,010.00 USD | 58,480.00 USD | 17,700.00 USD | 0.00 USD |
| `1D` | `0.1075` | 661,200.00 USD | 0.00 USD | 661,200.00 USD | 26,670.00 USD | 6,770.00 USD | 14,010.00 USD |
| `7D` | `0.1075` | 769,820.00 USD | 0.00 USD | 769,820.00 USD | 20,750.00 USD | 3,500.00 USD | 58.62 USD |
| `1D` | `0.1077` | 613,760.00 USD | 0.00 USD | 613,760.00 USD | 16,370.00 USD | 16,740.00 USD | 16,920.00 USD |
| `7D` | `0.1077` | 745,510.00 USD | 0.00 USD | 745,510.00 USD | 0.00 USD | 0.00 USD | 8,640.00 USD |
| `1D` | `0.1079` | 563,730.00 USD | 0.00 USD | 563,730.00 USD | 9,370.00 USD | 13,900.00 USD | 29,200.00 USD |
| `7D` | `0.1079` | 736,860.00 USD | 0.00 USD | 736,860.00 USD | 128,090.00 USD | 23,980.00 USD | 0.00 USD |
| `1D` | `0.1081` | 511,250.00 USD | 0.00 USD | 511,250.00 USD | 17,730.00 USD | 7,210.00 USD | 50,000.00 USD |
| `7D` | `0.1081` | 584,790.00 USD | 0.00 USD | 584,790.00 USD | 205,390.00 USD | 11,660.00 USD | 28,860.00 USD |
| `1D` | `0.1083` | 436,320.00 USD | 0.00 USD | 436,320.00 USD | 20,890.00 USD | 6,690.00 USD | 33,850.00 USD |
| `7D` | `0.1083` | 338,880.00 USD | 0.00 USD | 338,880.00 USD | 94,800.00 USD | 2,110.00 USD | 42,410.00 USD |
| `1D` | `0.1085` | 374,890.00 USD | 0.00 USD | 374,890.00 USD | 22,270.00 USD | 13,850.00 USD | 65,030.00 USD |
| `7D` | `0.1085` | 199,560.00 USD | 0.00 USD | 199,560.00 USD | 15,920.00 USD | 4,200.00 USD | 29.20 USD |
| `1D` | `0.1087` | 273,740.00 USD | 0.00 USD | 273,740.00 USD | 44,350.00 USD | 8,210.00 USD | 44,670.00 USD |
| `7D` | `0.1087` | 179,420.00 USD | 0.00 USD | 179,420.00 USD | 55,430.00 USD | 6,210.00 USD | 60,070.00 USD |
| `1D` | `0.1089` | 176,510.00 USD | 0.00 USD | 176,510.00 USD | 30,880.00 USD | 17,080.00 USD | 41,540.00 USD |
| `7D` | `0.1089` | 57,700.00 USD | 0.00 USD | 57,700.00 USD | 5,290.00 USD | 14,560.00 USD | 0.00 USD |
| `1D` | `0.1091` | 87,010.00 USD | 0.00 USD | 87,010.00 USD | 33,700.00 USD | 6,410.00 USD | 8,180.00 USD |
| `7D` | `0.1091` | 37,840.00 USD | 0.00 USD | 37,840.00 USD | 16,310.00 USD | 3,800.00 USD | 9,010.00 USD |
| `1D` | `0.1093` | 38,730.00 USD | 0.00 USD | 38,730.00 USD | 15,480.00 USD | 3,890.00 USD | 8,500.00 USD |
| `7D` | `0.1093` | 8,730.00 USD | 0.00 USD | 8,730.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD |
| `1D` | `0.1095` | 10,860.00 USD | 0.00 USD | 10,860.00 USD | 0.00 USD | 0.00 USD | 10,860.00 USD |
| `7D` | `0.1095` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1097` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1101` | 6,260.00 USD | 6,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,260.00 USD |
| `1D` | `0.1103` | 40,060.00 USD | 40,060.00 USD | 0.00 USD | 23,720.00 USD | 4,000.00 USD | 6,070.00 USD |
| `7D` | `0.1103` | 27,370.00 USD | 27,370.00 USD | 0.00 USD | 27,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1105` | 47,110.00 USD | 47,110.00 USD | 0.00 USD | 0.00 USD | 10,030.00 USD | 9,710.00 USD |
| `1D` | `0.1107` | 88,520.00 USD | 88,520.00 USD | 0.00 USD | 0.00 USD | 12,720.00 USD | 35,750.00 USD |
| `7D` | `0.1107` | 59,620.00 USD | 59,620.00 USD | 0.00 USD | 0.00 USD | 12,510.00 USD | 0.00 USD |
| `7D` | `0.1109` | 72,050.00 USD | 72,050.00 USD | 0.00 USD | 0.00 USD | 12,430.00 USD | 0.00 USD |
| `1D` | `0.1113` | 138,870.00 USD | 138,870.00 USD | 0.00 USD | 15,810.00 USD | 3,630.00 USD | 30,900.00 USD |
| `1D` | `0.1115` | 143,630.00 USD | 143,630.00 USD | 0.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1117` | 192,280.00 USD | 192,280.00 USD | 0.00 USD | 0.00 USD | 24,680.00 USD | 23,960.00 USD |
| `7D` | `0.1117` | 111,320.00 USD | 111,320.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | 16,490.00 USD |
| `1D` | `0.1119` | 241,510.00 USD | 241,510.00 USD | 0.00 USD | 26,390.00 USD | 5,030.00 USD | 17,820.00 USD |
| `7D` | `0.1119` | 154,420.00 USD | 154,420.00 USD | 0.00 USD | 25,250.00 USD | 7,050.00 USD | 10,800.00 USD |
| `1D` | `0.1121` | 263,550.00 USD | 263,550.00 USD | 0.00 USD | 13,180.00 USD | 5,930.00 USD | 2,920.00 USD |
| `7D` | `0.1121` | 175,590.00 USD | 175,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,180.00 USD |
| `1D` | `0.1123` | 296,470.00 USD | 296,470.00 USD | 0.00 USD | 29,460.00 USD | 0.00 USD | 3,460.00 USD |
| `7D` | `0.1123` | 225,750.00 USD | 225,750.00 USD | 0.00 USD | 0.00 USD | 23,980.00 USD | 26,180.00 USD |
| `1D` | `0.1125` | 303,500.00 USD | 303,500.00 USD | 0.00 USD | 0.00 USD | 7,040.00 USD | 0.00 USD |
| `7D` | `0.1125` | 254,580.00 USD | 254,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,830.00 USD |
| `1D` | `0.1127` | 307,780.00 USD | 307,780.00 USD | 0.00 USD | 0.00 USD | 1,250.00 USD | 3,020.00 USD |
| `1D` | `0.1129` | 313,220.00 USD | 313,220.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1131` | 348,710.00 USD | 348,710.00 USD | 0.00 USD | 17,560.00 USD | 6,360.00 USD | 11,570.00 USD |
| `7D` | `0.1131` | 282,140.00 USD | 282,140.00 USD | 0.00 USD | 12,540.00 USD | 0.00 USD | 15,020.00 USD |
| `1D` | `0.1133` | 401,230.00 USD | 401,230.00 USD | 0.00 USD | 6,530.00 USD | 22,520.00 USD | 23,470.00 USD |
| `7D` | `0.1133` | 287,590.00 USD | 287,590.00 USD | 0.00 USD | 0.00 USD | 5,450.00 USD | 0.00 USD |
| `1D` | `0.1135` | 408,200.00 USD | 408,200.00 USD | 0.00 USD | 4,040.00 USD | 2,880.00 USD | 54.75 USD |
| `7D` | `0.1135` | 302,110.00 USD | 302,110.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD |
| `1D` | `0.1137` | 409,120.00 USD | 409,120.00 USD | 0.00 USD | 0.00 USD | 856.93 USD | 60.15 USD |
| `1D` | `0.1139` | 423,420.00 USD | 423,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,300.00 USD |
| `1D` | `0.1141` | 449,790.00 USD | 449,790.00 USD | 0.00 USD | 13,860.00 USD | 2,800.00 USD | 9,710.00 USD |
| `7D` | `0.1141` | 320,030.00 USD | 320,030.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,540.00 USD |
| `1D` | `0.1143` | 501,800.00 USD | 501,800.00 USD | 0.00 USD | 18,160.00 USD | 25,630.00 USD | 8,220.00 USD |
| `7D` | `0.1143` | 398,640.00 USD | 398,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78,600.00 USD |
| `1D` | `0.1145` | 557,820.00 USD | 557,820.00 USD | 0.00 USD | 8,350.00 USD | 10,790.00 USD | 36,880.00 USD |
| `7D` | `0.1145` | 552,890.00 USD | 552,890.00 USD | 0.00 USD | 10,360.00 USD | 2,730.00 USD | 141,160.00 USD |
| `1D` | `0.1147` | 600,180.00 USD | 600,180.00 USD | 0.00 USD | 6,800.00 USD | 8,840.00 USD | 26,720.00 USD |
| `7D` | `0.1147` | 697,170.00 USD | 697,170.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 134,400.00 USD |
| `1D` | `0.1149` | 662,180.00 USD | 662,180.00 USD | 0.00 USD | 35,170.00 USD | 624.71 USD | 26,200.00 USD |
| `7D` | `0.1149` | 780,600.00 USD | 780,600.00 USD | 0.00 USD | 10,560.00 USD | 0.00 USD | 72,860.00 USD |
| `1D` | `0.1151` | 744,550.00 USD | 744,550.00 USD | 0.00 USD | 21,360.00 USD | 14,620.00 USD | 46,390.00 USD |
| `7D` | `0.1151` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 92,570.00 USD | 4,210.00 USD | 128,550.00 USD |
| `1D` | `0.1153` | 881,400.00 USD | 881,400.00 USD | 0.00 USD | 39,450.00 USD | 29,420.00 USD | 67,980.00 USD |
| `7D` | `0.1153` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 153,720.00 USD | 8,400.00 USD | 139,800.00 USD |
| `1D` | `0.1155` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 48,310.00 USD | 27,080.00 USD | 54,000.00 USD |
| `7D` | `0.1155` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 149,360.00 USD | 40,110.00 USD | 105,680.00 USD |
| `1D` | `0.1157` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 37,790.00 USD | 12,010.00 USD | 25,430.00 USD |
| `7D` | `0.1157` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 155,250.00 USD | 3,760.00 USD | 48,220.00 USD |
| `1D` | `0.1159` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 27,270.00 USD | 12,000.00 USD | 25,150.00 USD |
| `7D` | `0.1159` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 97,270.00 USD | 12,710.00 USD | 53,290.00 USD |
| `1D` | `0.1161` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 30,570.00 USD | 6,970.00 USD | 36,470.00 USD |
| `7D` | `0.1161` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 146,810.00 USD | 37,250.00 USD | 99,980.00 USD |
| `1D` | `0.1163` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 18,210.00 USD | 14,540.00 USD | 17,460.00 USD |
| `7D` | `0.1163` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 66,560.00 USD | 11,460.00 USD | 68,760.00 USD |
| `1D` | `0.1165` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 14,300.00 USD | 14,710.00 USD | 5,490.00 USD |
| `7D` | `0.1165` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 68,620.00 USD | 35,720.00 USD | 27,180.00 USD |
| `1D` | `0.1167` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 12,360.00 USD | 17,370.00 USD | 6,180.00 USD |
| `7D` | `0.1167` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 79,610.00 USD | 21,620.00 USD | 41,250.00 USD |
| `1D` | `0.1169` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 16,040.00 USD | 6,020.00 USD | 14,310.00 USD |
| `7D` | `0.1169` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 65,340.00 USD | 14,840.00 USD | 86,730.00 USD |
| `1D` | `0.1171` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 17,090.00 USD | 4,520.00 USD | 4,520.00 USD |
| `7D` | `0.1171` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 57,350.00 USD | 11,370.00 USD | 35,080.00 USD |
| `1D` | `0.1173` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 14,960.00 USD | 8,910.00 USD | 11,420.00 USD |
| `7D` | `0.1173` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 40,860.00 USD | 9,190.00 USD | 36,700.00 USD |
| `1D` | `0.1175` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 11,510.00 USD | 17,150.00 USD | 24,350.00 USD |
| `7D` | `0.1175` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 38,840.00 USD | 12,300.00 USD | 58,660.00 USD |
| `1D` | `0.1177` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 19,300.00 USD | 8,560.00 USD | 16,750.00 USD |
| `7D` | `0.1177` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 33,330.00 USD | 20,350.00 USD | 44,380.00 USD |
| `1D` | `0.1179` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 19,180.00 USD | 5,840.00 USD | 14,460.00 USD |
| `7D` | `0.1179` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 66,670.00 USD | 10,940.00 USD | 23,430.00 USD |
| `1D` | `0.1181` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 15,480.00 USD | 6,030.00 USD | 15,020.00 USD |
| `7D` | `0.1181` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 22,290.00 USD | 15,780.00 USD | 17,730.00 USD |
| `1D` | `0.1183` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 7,310.00 USD | 1,400.00 USD | 9,080.00 USD |
| `7D` | `0.1183` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 4,040.00 USD | 1,800.00 USD | 39,630.00 USD |
| `1D` | `0.1185` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 8,760.00 USD | 7,830.00 USD | 13,350.00 USD |
| `7D` | `0.1185` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 3,880.00 USD | 5,130.00 USD | 22,280.00 USD |
| `1D` | `0.1187` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 11,520.00 USD | 8,520.00 USD | 11,670.00 USD |
| `7D` | `0.1187` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 5,620.00 USD | 15,370.00 USD | 32,090.00 USD |
| `1D` | `0.1189` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 4,220.00 USD | 3,060.00 USD | 4,440.00 USD |
| `7D` | `0.1189` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 27,240.00 USD | 15,060.00 USD | 3,240.00 USD |
| `1D` | `0.1191` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 4,940.00 USD | 6,690.00 USD | 3,460.00 USD |
| `7D` | `0.1191` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 22,650.00 USD | 15,330.00 USD | 109,070.00 USD |
| `1D` | `0.1193` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 4,720.00 USD | 2,080.00 USD | 3,790.00 USD |
| `7D` | `0.1193` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 21,260.00 USD | 0.00 USD | 9,460.00 USD |
| `1D` | `0.1195` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 9,550.00 USD | 3,210.00 USD | 2,820.00 USD |
| `7D` | `0.1195` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 11,190.00 USD | 1,780.00 USD | 29,550.00 USD |
| `1D` | `0.1197` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 1,040.00 USD | 116.45 USD |
| `7D` | `0.1197` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 6,780.00 USD | 10,800.00 USD | 14,080.00 USD |
| `1D` | `0.1199` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 3,050.00 USD | 3,090.00 USD |
| `7D` | `0.1199` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 9,100.00 USD | 0.00 USD | 64,690.00 USD |
| `1D` | `0.1201` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 6,460.00 USD | 1,070.00 USD | 8,070.00 USD |
| `7D` | `0.1201` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 114,140.00 USD | 16,380.00 USD | 29,030.00 USD |
| `1D` | `0.1203` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 5,670.00 USD | 413.94 USD | 2,690.00 USD |
| `7D` | `0.1203` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 70,770.00 USD | 29,250.00 USD | 6,330.00 USD |
| `1D` | `0.1205` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 2,250.00 USD | 1,670.00 USD | 749.41 USD |
| `7D` | `0.1205` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 86,480.00 USD | 48,720.00 USD | 128,340.00 USD |
| `1D` | `0.1207` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 5,540.00 USD | 524.23 USD | 2,600.00 USD |
| `7D` | `0.1207` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 12,460.00 USD | 19,400.00 USD | 59,650.00 USD |
| `1D` | `0.1209` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 2,450.00 USD | 2,550.00 USD | 2,240.00 USD |
| `7D` | `0.1209` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 85,160.00 USD | 19,340.00 USD | 94,160.00 USD |
| `1D` | `0.1211` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 3,340.00 USD | 2,600.00 USD | 3,230.00 USD |
| `7D` | `0.1211` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 27,400.00 USD | 16,260.00 USD | 29,580.00 USD |
| `1D` | `0.1213` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 1,550.00 USD | 1,220.00 USD | 10,420.00 USD |
| `7D` | `0.1213` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 23,920.00 USD | 26,740.00 USD | 24,260.00 USD |
| `1D` | `0.1215` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD | 4,200.00 USD |
| `7D` | `0.1215` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 5,900.00 USD | 6,620.00 USD | 59,120.00 USD |
| `1D` | `0.1217` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 1,090.00 USD | 624.33 USD | 5,090.00 USD |
| `7D` | `0.1217` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 18,490.00 USD | 23,600.00 USD | 11,230.00 USD |
| `1D` | `0.1219` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 2,320.00 USD | 718.82 USD | 10,060.00 USD |
| `7D` | `0.1219` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 26,700.00 USD | 5,500.00 USD | 38,090.00 USD |
| `1D` | `0.1221` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 4,680.00 USD | 2,940.00 USD | 3,670.00 USD |
| `7D` | `0.1221` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 47,890.00 USD | 21,770.00 USD | 18,930.00 USD |
| `1D` | `0.1223` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 2,660.00 USD | 1,410.00 USD | 4,200.00 USD |
| `7D` | `0.1223` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 103,180.00 USD | 36,290.00 USD | 48,470.00 USD |
| `1D` | `0.1225` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1225` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 43,040.00 USD | 19,970.00 USD | 5,210.00 USD |
| `1D` | `0.1227` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1227` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 65,240.00 USD | 31,790.00 USD | 55,610.00 USD |
| `1D` | `0.1229` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 403.62 USD | 1,080.00 USD |
| `7D` | `0.1229` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 73,990.00 USD | 35,570.00 USD | 43,220.00 USD |
| `1D` | `0.1231` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 430.11 USD | 793.30 USD |
| `7D` | `0.1231` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 29,380.00 USD | 31,660.00 USD | 30,420.00 USD |
| `1D` | `0.1233` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 1,250.00 USD | 3,210.00 USD | 20.44 USD |
| `7D` | `0.1233` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 57,130.00 USD | 13,020.00 USD | 40,300.00 USD |
| `1D` | `0.1235` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 1,570.00 USD | 1,240.00 USD | 3,370.00 USD |
| `7D` | `0.1235` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 10,950.00 USD | 6,400.00 USD | 8,900.00 USD |
| `1D` | `0.1237` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 1,560.00 USD | 0.00 USD |
| `7D` | `0.1237` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 4,080.00 USD | 9,720.00 USD | 3,020.00 USD |
| `1D` | `0.1239` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 4,900.00 USD | 724.40 USD | 587.65 USD |
| `7D` | `0.1239` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 8,780.00 USD | 1,270.00 USD | 220.25 USD |
| `1D` | `0.1241` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 2,790.00 USD | 1,830.00 USD | 4,300.00 USD |
| `7D` | `0.1241` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 6,830.00 USD | 9,690.00 USD | 2,450.00 USD |
| `1D` | `0.1243` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 1,660.00 USD | 4,600.00 USD | 7,510.00 USD |
| `7D` | `0.1243` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 11,450.00 USD | 4,530.00 USD | 4,700.00 USD |
| `1D` | `0.1245` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 6,600.00 USD | 3,420.00 USD | 5,500.00 USD |
| `7D` | `0.1245` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 26,080.00 USD | 11,090.00 USD | 13,000.00 USD |
| `1D` | `0.1247` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 2,580.00 USD | 1,320.00 USD | 4,730.00 USD |
| `7D` | `0.1247` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 24,470.00 USD | 19,030.00 USD | 9,630.00 USD |
| `7D` | `0.1249` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 13,440.00 USD | 5,480.00 USD | 5,680.00 USD |
| `7D` | `0.1251` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 7,660.00 USD | 5,070.00 USD | 11,120.00 USD |
| `7D` | `0.1253` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 11,420.00 USD | 2,100.00 USD | 14,010.00 USD |
| `7D` | `0.1255` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 2,250.00 USD | 13,990.00 USD | 91.62 USD |
| `7D` | `0.1257` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 15,610.00 USD | 5,200.00 USD | 156.62 USD |
| `7D` | `0.1259` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 154.62 USD |
| `7D` | `0.1261` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | 3,530.00 USD |
| `7D` | `0.1263` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,100.00 USD |
| `7D` | `0.1265` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 2,710.00 USD | 0.00 USD | 3,260.00 USD |
| `7D` | `0.1267` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,940.00 USD |
| `7D` | `0.1269` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16.21 USD |
| `7D` | `0.1271` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 5,940.00 USD | 0.00 USD | 13.94 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `72.54M` | Total OI Tokens: `661,974,904.3 OP`
  * 1h OI Change: `-1.12%` | 4h OI Change: `-3.90%` | 24h OI Change: `-6.62%`
  * Exchange Breakdown: Binance=`16.49M` | Bybit=`14.07M` | OKX=`4.13M` | Hyperliquid=`3.87M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `876.09` | Last 24h: `270.64` | Last 3d: `-2.23K` | Last 7d: `-15.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0035%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0002%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0036%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0200%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `47.82%` | `52.18%` | `0.92` | 4,280,000.00 USD |
| `15M` | `Binance` | `52.01%` | `47.99%` | `1.08` | 1,420,000.00 USD |
| `15M` | `OKX` | `49.5%` | `50.5%` | `0.98` | 697,530.00 USD |
| `15M` | `Bybit` | `45.01%` | `54.99%` | `0.82` | 472,000.00 USD |
| `15M` | `KuCoin` | `49.36%` | `50.64%` | `0.97` | 159,270.00 USD |
| `15M` | `Gate` | `25.8%` | `74.2%` | `0.35` | 51,220.00 USD |
| `15M` | `Bitget` | `61.66%` | `38.34%` | `1.61` | 36,860.00 USD |
| `15M` | `BingX` | `58.07%` | `41.93%` | `1.38` | 275,720.00 USD |
| `15M` | `MEXC` | `43.53%` | `56.47%` | `0.77` | 92,430.00 USD |
| `15M` | `Bitunix` | `62.16%` | `37.84%` | `1.64` | 111,320.00 USD |
| `15M` | `Hyperliquid` | `7%` | `93%` | `0.08` | 42,490.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.83%` | `50.17%` | `0.99` | 697,280.00 USD |
| `15M` | `Crypto.com` | `50%` | `50%` | `1.00` | 5.73 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 200,460.00 USD |
| `15M` | `HTX` | `47.19%` | `52.81%` | `0.89` | 6,040.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `85.58%` | `14.42%` | `5.93` | 6,160.00 USD |
| `15M` | `Aster` | `97.19%` | `2.81%` | `34.59` | 5,780.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `4.71%` | `95.29%` | `0.05` | 1,480.00 USD |
| `15M` | `Whale Positions` | `52.01%` | `47.99%` | `1.08` | 1,420,000.00 USD |
| `15M` | `Global Accounts` | `47.82%` | `52.18%` | `0.92` | 4,280,000.00 USD |
| `1H` | `OP` | `39.30%` | `60.70%` | `0.65` | 9,690,000.00 USD |
| `1H` | `Binance` | `38.94%` | `61.06%` | `0.64` | 3,310,000.00 USD |
| `1H` | `OKX` | `51.6%` | `48.4%` | `1.07` | 942,070.00 USD |
| `1H` | `Bybit` | `38.42%` | `61.58%` | `0.62` | 1,120,000.00 USD |
| `1H` | `KuCoin` | `49.93%` | `50.07%` | `1.00` | 588,610.00 USD |
| `1H` | `Gate` | `56.78%` | `43.22%` | `1.31` | 163,150.00 USD |
| `1H` | `Bitget` | `21.91%` | `78.09%` | `0.28` | 363,260.00 USD |
| `1H` | `BingX` | `9.75%` | `90.25%` | `0.11` | 1,260,000.00 USD |
| `1H` | `MEXC` | `43.61%` | `56.39%` | `0.77` | 789,860.00 USD |
| `1H` | `Bitunix` | `51.04%` | `48.96%` | `1.04` | 121,690.00 USD |
| `1H` | `Hyperliquid` | `21.97%` | `78.03%` | `0.28` | 142,310.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.89%` | `45.11%` | `1.22` | 374,750.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `63.55%` | `36.45%` | `1.74` | 259,780.00 USD |
| `1H` | `HTX` | `83.05%` | `16.95%` | `4.90` | 1,650.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `83.65%` | `16.35%` | `5.12` | 239,660.00 USD |
| `1H` | `Aster` | `1.59%` | `98.41%` | `0.02` | 6,460.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `86.9%` | `13.1%` | `6.63` | 1,980.00 USD |
| `1H` | `Whale Positions` | `38.94%` | `61.06%` | `0.64` | 3,310,000.00 USD |
| `1H` | `Global Accounts` | `39.30%` | `60.70%` | `0.65` | 9,690,000.00 USD |
| `4H` | `OP` | `42.98%` | `57.02%` | `0.75` | 33,310,000.00 USD |
| `4H` | `Binance` | `42.79%` | `57.21%` | `0.75` | 12,830,000.00 USD |
| `4H` | `OKX` | `47.03%` | `52.97%` | `0.89` | 3,810,000.00 USD |
| `4H` | `Bybit` | `44.17%` | `55.83%` | `0.79` | 3,630,000.00 USD |
| `4H` | `KuCoin` | `49.76%` | `50.24%` | `0.99` | 2,590,000.00 USD |
| `4H` | `Gate` | `49.71%` | `50.29%` | `0.99` | 508,150.00 USD |
| `4H` | `Bitget` | `33.22%` | `66.78%` | `0.50` | 902,280.00 USD |
| `4H` | `BingX` | `23.18%` | `76.82%` | `0.30` | 2,750,000.00 USD |
| `4H` | `MEXC` | `40.25%` | `59.75%` | `0.67` | 2,540,000.00 USD |
| `4H` | `Bitunix` | `42.07%` | `57.93%` | `0.73` | 575,400.00 USD |
| `4H` | `Hyperliquid` | `55.33%` | `44.67%` | `1.24` | 602,650.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.77%` | `49.23%` | `1.03` | 1,250,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `47.94%` | `52.06%` | `0.92` | 1,000,000.00 USD |
| `4H` | `HTX` | `90.34%` | `9.66%` | `9.35` | 7,690.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `76.01%` | `23.99%` | `3.17` | 294,100.00 USD |
| `4H` | `Aster` | `31.22%` | `68.78%` | `0.45` | 13,100.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `78.69%` | `21.31%` | `3.69` | 9,020.00 USD |
| `4H` | `Whale Positions` | `42.79%` | `57.21%` | `0.75` | 12,830,000.00 USD |
| `4H` | `Global Accounts` | `42.98%` | `57.02%` | `0.75` | 33,310,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1134` | `0.1136` | `0.1134` | `0.1142` | `0.1132` | 635,625.25 USD | 325,080.19 USD | 310,545.06 USD | 14,535.13 USD | `+2.29%` | `15B / 17S` |
| `0:00 UTC` | `0.1133` | `0.1131` | `0.1133` | `0.1135` | `0.1126` | 680,945.05 USD | 236,805.84 USD | 444,139.21 USD | -207,333.38 USD | `-30.45%` | `14B / 19S` |
| `5:00 UTC` | `0.1128` | `0.1128` | `0.1128` | `0.1130` | `0.1127` | 243,648.48 USD | 108,202.11 USD | 135,446.38 USD | -27,244.27 USD | `-11.18%` | `2B / 9S` |
| `0:00 UTC` | `0.1126` | `0.1127` | `0.1126` | `0.1132` | `0.1123` | 269,778.58 USD | 124,825.75 USD | 144,952.84 USD | -20,127.09 USD | `-7.46%` | `11B / 20S` |
| `5:00 UTC` | `0.1123` | `0.1122` | `0.1123` | `0.1124` | `0.1119` | 385,611.74 USD | 157,293.82 USD | 228,317.92 USD | -71,024.10 USD | `-18.42%` | `5B / 10S` |
| `0:00 UTC` | `0.1114` | `0.1117` | `0.1114` | `0.1124` | `0.1110` | 525,538.44 USD | 243,812.31 USD | 281,726.13 USD | -37,913.82 USD | `-7.21%` | `25B / 41S` |
| `5:00 UTC` | `0.1107` | `0.1107` | `0.1107` | `0.1112` | `0.1101` | 919,895.36 USD | 440,104.81 USD | 479,790.55 USD | -39,685.74 USD | `-4.31%` | `22B / 21S` |
| `0:00 UTC` | `0.1113` | `0.1110` | `0.1113` | `0.1113` | `0.1106` | 261,230.00 USD | 123,873.54 USD | 137,356.46 USD | -13,482.93 USD | `-5.16%` | `17B / 9S` |
| `5:00 UTC` | `0.1108` | `0.1106` | `0.1108` | `0.1112` | `0.1101` | 266,281.73 USD | 113,817.33 USD | 152,464.41 USD | -38,647.08 USD | `-14.51%` | `15B / 30S` |
| `0:00 UTC` | `0.1097` | `0.1098` | `0.1097` | `0.1103` | `0.1094` | 633,720.09 USD | 297,803.44 USD | 335,916.65 USD | -38,113.21 USD | `-6.01%` | `11B / 20S` |

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
| `5m` | 2,230.00 USD | -4,080.00 USD | **`DISTRIBUTION`** |
| `15m` | -24,480.00 USD | -71,890.00 USD | **`DISTRIBUTION`** |
| `30m` | -23,160.00 USD | -138,120.00 USD | **`DISTRIBUTION`** |
| `1h` | -50,360.00 USD | -191,890.00 USD | **`DISTRIBUTION`** |
| `2h` | -41,760.00 USD | -493,550.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,410.00 USD | -599,240.00 USD | **`DISTRIBUTION`** |
| `6h` | 134,930.00 USD | 80,000.00 USD | **`ACCUMULATION`** |
| `8h` | 184,760.00 USD | 179,480.00 USD | **`ACCUMULATION`** |
| `12h` | 202,590.00 USD | 671,670.00 USD | **`ACCUMULATION`** |
| `24h` | 42,950.00 USD | -1,340,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -124,650.00 USD | -9,950,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,450,000.00 USD | -78,770,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+2.23K` | 15m=`-24.48K` | 1h=`-50.36K` | 24h=`+42.95K`
* Futures Capital Netflows: 5m=`-4.08K` | 15m=`-71.89K` | 1h=`-191.89K` | 24h=`-1.34M`
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
  * `2026-10-29 23:31:18 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:18 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:10:18 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:10:18 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
