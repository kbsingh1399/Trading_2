# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 02:00:21 IST` (`2026-10-29 20:30:21 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1077` | `0.1085` | `0.1072` | `0.1084` | `2,947,821` | 318,236.70 USD | 42,752.64 USD | `+13.43%` | -1,322,501.72 USD | `+0.56` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1084` | `0.1087` | `0.1081` | `0.1085` | `1,501,976` | 162,857.87 USD | 53,278.35 USD | `+32.71%` | -1,269,223.37 USD | `+0.70` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.1085` | `0.1086` | `0.1080` | `0.1082` | `1,126,970` | 122,103.33 USD | -20,759.38 USD | `-17.00%` | -1,289,982.75 USD | `-0.18` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1103` | `0.1105` | `0.1099` | `0.1101` | `1,955,015` | 215,356.47 USD | 9,965.93 USD | `+4.63%` | -1,018,199.50 USD | `+0.28` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1101` | `0.1103` | `0.1070` | `0.1084` | `22,410,691` | 2,425,114.31 USD | -332,553.17 USD | `-13.71%` | -1,350,752.67 USD | `-3.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1084` | `0.1087` | `0.1080` | `0.1082` | `2,628,946` | 284,961.20 USD | 32,518.97 USD | `+11.41%` | -1,318,233.70 USD | `+0.57` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1112` | `0.1113` | `0.1094` | `0.1100` | `13,608,224` | 1,499,374.47 USD | -1,041.31 USD | `-0.07%` | -1,303,410.19 USD | `+0.26` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1100` | `0.1106` | `0.1096` | `0.1101` | `7,910,873` | 870,770.93 USD | 117,397.34 USD | `+13.48%` | -1,186,012.85 USD | `+0.73` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1101` | `0.1103` | `0.1070` | `0.1082` | `25,047,061` | 2,710,879.18 USD | -299,496.76 USD | `-11.05%` | -1,485,509.61 USD | `-0.93` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -935,828.18 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | -1,111,968.46 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.1070` | `0.1083` | `25,043,990` | 2,710,546.68 USD | -299,563.02 USD | `-11.05%` | -1,411,531.48 USD | `-0.10` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1085` | `0.1106` | `0.1071` | `0.1076` | `47,048,931` | 5,111,570.05 USD | 108,567.99 USD | `+2.12%` | -1,419,806.61 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,277,083.78 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -935,828.18 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | -1,111,968.46 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.1070` | `0.1083` | `25,043,990` | 2,710,546.68 USD | -299,563.02 USD | `-11.05%` | -1,411,531.48 USD | `-0.10` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:54:30 IST` |

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
| `Live` | `Long Liquidation` | `0.0395` | 416.18 USD | 242,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 3,450.00 USD | 242,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 262.59 USD | 239,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 3,460.00 USD | 238,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 829.69 USD | 235,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 1,100.00 USD | 234,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 353.81 USD | 233,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 509.64 USD | 233,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 518.48 USD | 232,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 1,920.00 USD | 232,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 25,370.00 USD | 230,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 4,380.00 USD | 204,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 44,410.00 USD | 200,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 1,020.00 USD | 155,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 1,280.00 USD | 154,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 1,730.00 USD | 153,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 1,320.00 USD | 151,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 223.98 USD | 150,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 1,560.00 USD | 150,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 2,380.00 USD | 148,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 3,120.00 USD | 146,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 443.16 USD | 143,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 16,670.00 USD | 142,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 69,120.00 USD | 126,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 5,610.00 USD | 57,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0957` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 8.26 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0959` | 3,210,000.00 USD | 3,210,000.00 USD | 2,410.00 USD | 1,140.00 USD | 5.33 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0963` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 1.02 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0963` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0965` | 1,500,000.00 USD | 1,500,000.00 USD | 1,280.00 USD | 282.32 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0965` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 66.99 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0965` | 419.87 USD | 51,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0967` | 1,500,000.00 USD | 1,500,000.00 USD | 2,660.00 USD | 1,100.00 USD | 7,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0967` | 3,210,000.00 USD | 3,210,000.00 USD | 3,770.00 USD | 2,660.00 USD | 2,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0969` | 1,490,000.00 USD | 1,490,000.00 USD | 4,590.00 USD | 2,640.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0969` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 2,810.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0971` | 1,470,000.00 USD | 1,470,000.00 USD | 2,150.00 USD | 3,330.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 2,000.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0973` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 2,120.00 USD | 4,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0973` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 1,390.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0975` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 1,360.00 USD | 5,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0975` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 1,160.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0975` | 12,670.00 USD | 51,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0977` | 1,450,000.00 USD | 1,450,000.00 USD | 8,290.00 USD | 2,510.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0977` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0979` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 1,040.00 USD | 8.08 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0979` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 1,530.00 USD | 5,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0981` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 431.42 USD | 3,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0981` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 2,390.00 USD | 5,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0983` | 1,430,000.00 USD | 1,430,000.00 USD | 3,250.00 USD | 1,390.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 3,140,000.00 USD | 3,140,000.00 USD | 7,990.00 USD | 1,230.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0985` | 1,420,000.00 USD | 1,420,000.00 USD | 5,670.00 USD | 413.94 USD | 2,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0985` | 3,120,000.00 USD | 3,120,000.00 USD | 7,110.00 USD | 0.00 USD | 6,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0985` | 19,960.00 USD | 38,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0987` | 1,410,000.00 USD | 1,410,000.00 USD | 7,790.00 USD | 2,190.00 USD | 4,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0987` | 3,110,000.00 USD | 3,110,000.00 USD | 5,390.00 USD | 9,190.00 USD | 37,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0989` | 1,390,000.00 USD | 1,390,000.00 USD | 2,820.00 USD | 3,290.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 3,060,000.00 USD | 3,060,000.00 USD | 12,260.00 USD | 4,520.00 USD | 27,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0991` | 1,380,000.00 USD | 1,380,000.00 USD | 4,800.00 USD | 2,950.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0991` | 3,010,000.00 USD | 3,010,000.00 USD | 14,350.00 USD | 10,350.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0993` | 1,370,000.00 USD | 1,370,000.00 USD | 3,080.00 USD | 1,720.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0993` | 2,980,000.00 USD | 2,980,000.00 USD | 23,920.00 USD | 10,140.00 USD | 24,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0995` | 1,360,000.00 USD | 1,360,000.00 USD | 2,740.00 USD | 624.33 USD | 11,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 2,920,000.00 USD | 2,920,000.00 USD | 13,090.00 USD | 6,160.00 USD | 25,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0997` | 1,340,000.00 USD | 1,340,000.00 USD | 2,320.00 USD | 718.82 USD | 10,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0997` | 2,870,000.00 USD | 2,870,000.00 USD | 21,100.00 USD | 5,500.00 USD | 33,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0999` | 1,330,000.00 USD | 1,330,000.00 USD | 4,680.00 USD | 2,940.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0999` | 2,810,000.00 USD | 2,810,000.00 USD | 14,230.00 USD | 6,540.00 USD | 18,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1001` | 1,320,000.00 USD | 1,320,000.00 USD | 2,660.00 USD | 1,410.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 2,770,000.00 USD | 2,770,000.00 USD | 29,230.00 USD | 3,010.00 USD | 10,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1003` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1003` | 2,730,000.00 USD | 2,730,000.00 USD | 8,010.00 USD | 7,060.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1005` | 1,310,000.00 USD | 1,310,000.00 USD | 1,970.00 USD | 403.62 USD | 1,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1005` | 2,710,000.00 USD | 2,710,000.00 USD | 25,070.00 USD | 11,000.00 USD | 18,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1005` | 427.25 USD | 18,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1007` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 430.11 USD | 807.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 2,660,000.00 USD | 2,660,000.00 USD | 10,260.00 USD | 2,280.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1009` | 1,300,000.00 USD | 1,300,000.00 USD | 1,250.00 USD | 2,750.00 USD | 23.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1009` | 2,630,000.00 USD | 2,630,000.00 USD | 15,320.00 USD | 3,070.00 USD | 6,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1011` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 575.54 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1011` | 2,600,000.00 USD | 2,600,000.00 USD | 4,430.00 USD | 4,720.00 USD | 9,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1013` | 1,300,000.00 USD | 1,300,000.00 USD | 4,900.00 USD | 800.79 USD | 645.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 2,590,000.00 USD | 2,590,000.00 USD | 12,870.00 USD | 4,030.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1015` | 1,290,000.00 USD | 1,290,000.00 USD | 540.82 USD | 1,830.00 USD | 1,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1015` | 2,570,000.00 USD | 2,570,000.00 USD | 6,830.00 USD | 965.35 USD | 2,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1015` | 622.37 USD | 17,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1017` | 1,290,000.00 USD | 1,290,000.00 USD | 1,660.00 USD | 4,600.00 USD | 5,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1017` | 2,560,000.00 USD | 2,560,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1019` | 1,270,000.00 USD | 1,270,000.00 USD | 6,600.00 USD | 3,420.00 USD | 5,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1019` | 2,530,000.00 USD | 2,530,000.00 USD | 9,260.00 USD | 5,790.00 USD | 13,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1021` | 1,260,000.00 USD | 1,260,000.00 USD | 2,580.00 USD | 1,320.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1021` | 2,510,000.00 USD | 2,510,000.00 USD | 7,900.00 USD | 3,270.00 USD | 7,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1023` | 1,250,000.00 USD | 1,250,000.00 USD | 4,600.00 USD | 2,120.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1023` | 2,490,000.00 USD | 2,490,000.00 USD | 4,030.00 USD | 4,990.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1025` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 1,560.00 USD | 974.29 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1025` | 2,460,000.00 USD | 2,460,000.00 USD | 1,550.00 USD | 0.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1025` | 17,360.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1027` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 936.16 USD | 1,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1027` | 2,460,000.00 USD | 2,460,000.00 USD | 2,250.00 USD | 2,580.00 USD | 312.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1029` | 1,240,000.00 USD | 1,240,000.00 USD | 4,340.00 USD | 705.79 USD | 6,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1029` | 2,450,000.00 USD | 2,450,000.00 USD | 7,420.00 USD | 3,000.00 USD | 488.11 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1031` | 1,220,000.00 USD | 1,220,000.00 USD | 11,680.00 USD | 3,170.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1031` | 2,440,000.00 USD | 2,440,000.00 USD | 13,690.00 USD | 5,070.00 USD | 10,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1033` | 1,190,000.00 USD | 1,190,000.00 USD | 15,450.00 USD | 4,740.00 USD | 21,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1033` | 2,410,000.00 USD | 2,410,000.00 USD | 3,880.00 USD | 2,640.00 USD | 25,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1035` | 1,150,000.00 USD | 1,150,000.00 USD | 7,450.00 USD | 7,560.00 USD | 12,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1035` | 2,380,000.00 USD | 2,380,000.00 USD | 8,450.00 USD | 9,400.00 USD | 16,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1037` | 1,120,000.00 USD | 1,120,000.00 USD | 4,370.00 USD | 11,960.00 USD | 9,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1037` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1039` | 1,100,000.00 USD | 1,100,000.00 USD | 3,660.00 USD | 2,350.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1039` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 5,170.00 USD | 389.58 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1041` | 1,080,000.00 USD | 1,080,000.00 USD | 6,510.00 USD | 6,910.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1041` | 2,310,000.00 USD | 2,310,000.00 USD | 5,940.00 USD | 2,910.00 USD | 18,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1043` | 1,050,000.00 USD | 1,050,000.00 USD | 17,650.00 USD | 5,650.00 USD | 7,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1043` | 2,280,000.00 USD | 2,280,000.00 USD | 15,960.00 USD | 5,980.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1045` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 2,600.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1045` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 9,810.00 USD | 14,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1047` | 1,010,000.00 USD | 1,010,000.00 USD | 4,610.00 USD | 3,400.00 USD | 20,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1047` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 1,720.00 USD | 23,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1049` | 976,770.00 USD | 976,770.00 USD | 21,050.00 USD | 2,430.00 USD | 10,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1049` | 2,190,000.00 USD | 2,190,000.00 USD | 34,790.00 USD | 4,810.00 USD | 35,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1051` | 942,450.00 USD | 942,450.00 USD | 16,410.00 USD | 8,750.00 USD | 24,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1051` | 2,110,000.00 USD | 2,110,000.00 USD | 17,290.00 USD | 11,500.00 USD | 48,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1053` | 893,030.00 USD | 893,030.00 USD | 35,030.00 USD | 8,930.00 USD | 50,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1053` | 2,040,000.00 USD | 2,040,000.00 USD | 53,590.00 USD | 29,800.00 USD | 95,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1055` | 798,210.00 USD | 798,210.00 USD | 43,960.00 USD | 25,140.00 USD | 59,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1055` | 1,860,000.00 USD | 1,860,000.00 USD | 61,560.00 USD | 27,290.00 USD | 147,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1057` | 669,510.00 USD | 669,510.00 USD | 27,300.00 USD | 25,430.00 USD | 50,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1057` | 1,620,000.00 USD | 1,620,000.00 USD | 50,380.00 USD | 45,760.00 USD | 97,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1059` | 566,690.00 USD | 566,690.00 USD | 19,020.00 USD | 22,240.00 USD | 56,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1059` | 1,430,000.00 USD | 1,430,000.00 USD | 92,510.00 USD | 49,670.00 USD | 117,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1061` | 469,350.00 USD | 469,350.00 USD | 10,960.00 USD | 11,050.00 USD | 58,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1061` | 1,170,000.00 USD | 1,170,000.00 USD | 38,260.00 USD | 26,050.00 USD | 92,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1063` | 388,400.00 USD | 388,400.00 USD | 57,260.00 USD | 14,600.00 USD | 48,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1063` | 1,010,000.00 USD | 1,010,000.00 USD | 84,260.00 USD | 38,330.00 USD | 148,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1065` | 267,640.00 USD | 267,640.00 USD | 18,270.00 USD | 14,110.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1065` | 738,920.00 USD | 738,920.00 USD | 91,170.00 USD | 17,310.00 USD | 93,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1067` | 215,850.00 USD | 215,850.00 USD | 9,710.00 USD | 15,160.00 USD | 33,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1067` | 537,330.00 USD | 537,330.00 USD | 97,290.00 USD | 48,680.00 USD | 67,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1069` | 157,860.00 USD | 157,860.00 USD | 24,070.00 USD | 9,100.00 USD | 42,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1069` | 323,950.00 USD | 323,950.00 USD | 74,290.00 USD | 31,620.00 USD | 71,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1071` | 82,040.00 USD | 82,040.00 USD | 48,660.00 USD | 3,140.00 USD | 16,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1071` | 146,560.00 USD | 146,560.00 USD | 59,900.00 USD | 26,150.00 USD | 42,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1073` | 14,020.00 USD | 14,020.00 USD | 0.00 USD | 0.00 USD | 23.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1073` | 17,950.00 USD | 17,950.00 USD | 0.00 USD | 17,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1075` | 13,990.00 USD | 13,990.00 USD | 0.00 USD | 0.00 USD | 18.60 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1077` | 13,980.00 USD | 13,980.00 USD | 0.00 USD | 0.00 USD | 93.46 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1079` | 13,880.00 USD | 13,880.00 USD | 0.00 USD | 0.00 USD | 26.80 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1079` | 250.77 USD | 250.77 USD | 0.00 USD | 0.00 USD | 186.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1081` | 13,860.00 USD | 13,860.00 USD | 0.00 USD | 4,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1081` | 63.94 USD | 63.94 USD | 0.00 USD | 0.00 USD | 63.94 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1083` | 9,750.00 USD | 9,750.00 USD | 9,730.00 USD | 0.00 USD | 21.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1083` | 69,800.00 USD | 69,800.00 USD | 69,720.00 USD | 0.00 USD | 76.60 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1083` | 139,600.00 USD | 139,600.00 USD | 69,720.00 USD | 0.00 USD | 76.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1085` | 92,220.00 USD | 92,220.00 USD | 23,990.00 USD | 3,210.00 USD | 65,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1085` | 184,450.00 USD | 184,450.00 USD | 23,990.00 USD | 3,210.00 USD | 65,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1085` | 155,610.00 USD | 155,610.00 USD | 15,920.00 USD | 0.00 USD | 96.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1087` | 279,760.00 USD | 279,760.00 USD | 44,350.00 USD | 6,300.00 USD | 44,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1087` | 211,110.00 USD | 211,110.00 USD | 55,430.00 USD | 0.00 USD | 59.31 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1089` | 310,640.00 USD | 310,640.00 USD | 30,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1089` | 216,400.00 USD | 216,400.00 USD | 5,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1091` | 344,340.00 USD | 344,340.00 USD | 33,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1091` | 241,720.00 USD | 241,720.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1093` | 359,820.00 USD | 359,820.00 USD | 15,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1093` | 250,450.00 USD | 250,450.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1095` | 387,350.00 USD | 387,350.00 USD | 4,110.00 USD | 1,890.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1097` | 419,360.00 USD | 419,360.00 USD | 7,260.00 USD | 1,970.00 USD | 22,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1099` | 427,430.00 USD | 427,430.00 USD | 6,130.00 USD | 1,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1099` | 283,760.00 USD | 283,760.00 USD | 11,470.00 USD | 0.00 USD | 21,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1101` | 438,840.00 USD | 438,840.00 USD | 4,310.00 USD | 2,820.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1101` | 306,960.00 USD | 306,960.00 USD | 0.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 324,450.00 USD | 324,450.00 USD | 17,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1105` | 450,770.00 USD | 450,770.00 USD | 0.00 USD | 1,230.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1105` | 350,420.00 USD | 350,420.00 USD | 0.00 USD | 10,030.00 USD | 15,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1107` | 499,230.00 USD | 499,230.00 USD | 0.00 USD | 12,720.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1107` | 362,940.00 USD | 362,940.00 USD | 0.00 USD | 12,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 375,360.00 USD | 375,360.00 USD | 0.00 USD | 12,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1111` | 387,330.00 USD | 387,330.00 USD | 0.00 USD | 11,960.00 USD | 13.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1113` | 559,320.00 USD | 559,320.00 USD | 15,810.00 USD | 5,210.00 USD | 39,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1115` | 564,080.00 USD | 564,080.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1117` | 626,490.00 USD | 626,490.00 USD | 2,060.00 USD | 25,630.00 USD | 34,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1117` | 426,600.00 USD | 426,600.00 USD | 0.00 USD | 22,780.00 USD | 16,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1119` | 700,560.00 USD | 700,560.00 USD | 30,350.00 USD | 6,980.00 USD | 36,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1119` | 480,620.00 USD | 480,620.00 USD | 25,250.00 USD | 7,050.00 USD | 21,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1121` | 742,380.00 USD | 742,380.00 USD | 17,450.00 USD | 12,060.00 USD | 12,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 507,530.00 USD | 507,530.00 USD | 5,730.00 USD | 0.00 USD | 21,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1123` | 786,800.00 USD | 786,800.00 USD | 36,720.00 USD | 1,780.00 USD | 5,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1123` | 581,650.00 USD | 581,650.00 USD | 12,360.00 USD | 23,980.00 USD | 37,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1125` | 812,570.00 USD | 812,570.00 USD | 7,670.00 USD | 10,140.00 USD | 7,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1125` | 617,820.00 USD | 617,820.00 USD | 0.00 USD | 0.00 USD | 36,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1127` | 833,300.00 USD | 833,300.00 USD | 0.00 USD | 1,250.00 USD | 19,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1127` | 625,790.00 USD | 625,790.00 USD | 0.00 USD | 0.00 USD | 7,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1129` | 840,460.00 USD | 840,460.00 USD | 7,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1129` | 625,910.00 USD | 625,910.00 USD | 0.00 USD | 0.00 USD | 124.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1131` | 876,000.00 USD | 876,000.00 USD | 17,560.00 USD | 6,360.00 USD | 11,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1131` | 653,480.00 USD | 653,480.00 USD | 12,540.00 USD | 0.00 USD | 15,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1133` | 928,520.00 USD | 928,520.00 USD | 6,530.00 USD | 22,520.00 USD | 23,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 665,020.00 USD | 665,020.00 USD | 0.00 USD | 11,430.00 USD | 113.26 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1135` | 940,310.00 USD | 940,310.00 USD | 4,040.00 USD | 3,670.00 USD | 4,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1135` | 679,540.00 USD | 679,540.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1137` | 941,210.00 USD | 941,210.00 USD | 0.00 USD | 856.93 USD | 40.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1137` | 679,550.00 USD | 679,550.00 USD | 0.00 USD | 0.00 USD | 10.92 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1139` | 955,470.00 USD | 955,470.00 USD | 0.00 USD | 0.00 USD | 14,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1139` | 679,560.00 USD | 679,560.00 USD | 0.00 USD | 0.00 USD | 10.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1141` | 985,600.00 USD | 985,600.00 USD | 13,860.00 USD | 2,800.00 USD | 13,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1141` | 697,500.00 USD | 697,500.00 USD | 10,380.00 USD | 0.00 USD | 7,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1143` | 1,050,000.00 USD | 1,050,000.00 USD | 20,300.00 USD | 27,990.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1143` | 776,220.00 USD | 776,220.00 USD | 0.00 USD | 0.00 USD | 78,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1145` | 1,110,000.00 USD | 1,110,000.00 USD | 13,430.00 USD | 11,690.00 USD | 38,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 936,620.00 USD | 936,620.00 USD | 16,540.00 USD | 2,730.00 USD | 141,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1147` | 1,160,000.00 USD | 1,160,000.00 USD | 10,640.00 USD | 10,080.00 USD | 30,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1147` | 1,080,000.00 USD | 1,080,000.00 USD | 9,880.00 USD | 0.00 USD | 138,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1149` | 1,230,000.00 USD | 1,230,000.00 USD | 35,170.00 USD | 624.71 USD | 31,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1149` | 1,170,000.00 USD | 1,170,000.00 USD | 10,560.00 USD | 0.00 USD | 72,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1151` | 1,290,000.00 USD | 1,290,000.00 USD | 16,450.00 USD | 14,620.00 USD | 33,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 1,390,000.00 USD | 1,390,000.00 USD | 92,570.00 USD | 4,210.00 USD | 128,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1153` | 1,420,000.00 USD | 1,420,000.00 USD | 39,450.00 USD | 29,420.00 USD | 59,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1153` | 1,700,000.00 USD | 1,700,000.00 USD | 153,720.00 USD | 8,400.00 USD | 139,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1155` | 1,550,000.00 USD | 1,550,000.00 USD | 48,310.00 USD | 27,080.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1155` | 1,990,000.00 USD | 1,990,000.00 USD | 149,360.00 USD | 40,110.00 USD | 105,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1157` | 1,620,000.00 USD | 1,620,000.00 USD | 37,790.00 USD | 12,010.00 USD | 25,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 2,180,000.00 USD | 2,180,000.00 USD | 133,960.00 USD | 3,760.00 USD | 48,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1159` | 1,690,000.00 USD | 1,690,000.00 USD | 27,270.00 USD | 12,000.00 USD | 25,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1159` | 2,320,000.00 USD | 2,320,000.00 USD | 81,080.00 USD | 12,710.00 USD | 53,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1161` | 1,730,000.00 USD | 1,730,000.00 USD | 23,670.00 USD | 2,230.00 USD | 13,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1161` | 2,610,000.00 USD | 2,610,000.00 USD | 146,810.00 USD | 37,250.00 USD | 99,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1163` | 1,760,000.00 USD | 1,760,000.00 USD | 4,290.00 USD | 9,380.00 USD | 17,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 2,740,000.00 USD | 2,740,000.00 USD | 53,510.00 USD | 11,460.00 USD | 68,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1165` | 1,790,000.00 USD | 1,790,000.00 USD | 8,820.00 USD | 11,680.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1165` | 2,870,000.00 USD | 2,870,000.00 USD | 68,620.00 USD | 35,720.00 USD | 26,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1167` | 1,800,000.00 USD | 1,800,000.00 USD | 5,680.00 USD | 6,040.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1167` | 3,020,000.00 USD | 3,020,000.00 USD | 79,610.00 USD | 21,620.00 USD | 41,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1169` | 1,820,000.00 USD | 1,820,000.00 USD | 5,480.00 USD | 2,440.00 USD | 5,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 3,180,000.00 USD | 3,180,000.00 USD | 65,340.00 USD | 14,840.00 USD | 86,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1171` | 1,840,000.00 USD | 1,840,000.00 USD | 13,800.00 USD | 0.00 USD | 4,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1171` | 3,290,000.00 USD | 3,290,000.00 USD | 57,350.00 USD | 11,370.00 USD | 35,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1173` | 1,860,000.00 USD | 1,860,000.00 USD | 9,320.00 USD | 5,440.00 USD | 4,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1173` | 3,370,000.00 USD | 3,370,000.00 USD | 40,860.00 USD | 9,190.00 USD | 36,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1175` | 1,900,000.00 USD | 1,900,000.00 USD | 11,510.00 USD | 11,920.00 USD | 19,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 3,480,000.00 USD | 3,480,000.00 USD | 38,840.00 USD | 12,300.00 USD | 58,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1177` | 1,940,000.00 USD | 1,940,000.00 USD | 19,300.00 USD | 8,560.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1177` | 3,580,000.00 USD | 3,580,000.00 USD | 33,330.00 USD | 20,350.00 USD | 44,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1179` | 1,980,000.00 USD | 1,980,000.00 USD | 12,760.00 USD | 5,840.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1179` | 3,680,000.00 USD | 3,680,000.00 USD | 66,670.00 USD | 10,940.00 USD | 24,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1181` | 2,020,000.00 USD | 2,020,000.00 USD | 16,300.00 USD | 6,410.00 USD | 19,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 3,740,000.00 USD | 3,740,000.00 USD | 22,290.00 USD | 15,780.00 USD | 17,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1183` | 2,040,000.00 USD | 2,040,000.00 USD | 8,760.00 USD | 1,790.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1183` | 3,780,000.00 USD | 3,780,000.00 USD | 4,040.00 USD | 1,800.00 USD | 39,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1185` | 2,060,000.00 USD | 2,060,000.00 USD | 6,530.00 USD | 5,850.00 USD | 6,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1185` | 3,820,000.00 USD | 3,820,000.00 USD | 3,880.00 USD | 5,130.00 USD | 26,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1187` | 2,080,000.00 USD | 2,080,000.00 USD | 4,060.00 USD | 6,500.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 3,880,000.00 USD | 3,880,000.00 USD | 5,620.00 USD | 15,370.00 USD | 36,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1189` | 2,090,000.00 USD | 2,090,000.00 USD | 2,840.00 USD | 2,120.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1189` | 3,920,000.00 USD | 3,920,000.00 USD | 27,240.00 USD | 15,060.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1191` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 1,360.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1191` | 4,070,000.00 USD | 4,070,000.00 USD | 22,650.00 USD | 15,330.00 USD | 112,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1193` | 2,100,000.00 USD | 2,100,000.00 USD | 4,720.00 USD | 1,040.00 USD | 3,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 4,100,000.00 USD | 4,100,000.00 USD | 21,260.00 USD | 0.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1195` | 2,120,000.00 USD | 2,120,000.00 USD | 9,550.00 USD | 1,470.00 USD | 2,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1195` | 4,150,000.00 USD | 4,150,000.00 USD | 11,190.00 USD | 1,780.00 USD | 29,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1197` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 1,040.00 USD | 93.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1197` | 4,180,000.00 USD | 4,180,000.00 USD | 6,780.00 USD | 10,800.00 USD | 14,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1199` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 431.42 USD | 3,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 4,250,000.00 USD | 4,250,000.00 USD | 9,100.00 USD | 2,390.00 USD | 64,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1201` | 2,140,000.00 USD | 2,140,000.00 USD | 3,250.00 USD | 1,390.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1201` | 4,410,000.00 USD | 4,410,000.00 USD | 114,140.00 USD | 16,380.00 USD | 29,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1203` | 2,150,000.00 USD | 2,150,000.00 USD | 5,670.00 USD | 413.94 USD | 2,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1203` | 4,520,000.00 USD | 4,520,000.00 USD | 70,770.00 USD | 29,250.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1205` | 2,150,000.00 USD | 2,150,000.00 USD | 2,250.00 USD | 1,670.00 USD | 741.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 4,780,000.00 USD | 4,780,000.00 USD | 86,480.00 USD | 48,720.00 USD | 128,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1207` | 2,160,000.00 USD | 2,160,000.00 USD | 5,540.00 USD | 524.23 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1207` | 4,870,000.00 USD | 4,870,000.00 USD | 12,460.00 USD | 19,400.00 USD | 53,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1209` | 2,170,000.00 USD | 2,170,000.00 USD | 2,820.00 USD | 3,290.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1209` | 5,070,000.00 USD | 5,070,000.00 USD | 85,160.00 USD | 19,340.00 USD | 94,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1211` | 2,180,000.00 USD | 2,180,000.00 USD | 4,800.00 USD | 2,950.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 5,120,000.00 USD | 5,120,000.00 USD | 14,350.00 USD | 12,900.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1213` | 2,200,000.00 USD | 2,200,000.00 USD | 3,080.00 USD | 1,720.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1213` | 5,190,000.00 USD | 5,190,000.00 USD | 23,920.00 USD | 12,800.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1215` | 2,200,000.00 USD | 2,200,000.00 USD | 1,650.00 USD | 0.00 USD | 5,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1215` | 5,260,000.00 USD | 5,260,000.00 USD | 5,900.00 USD | 6,620.00 USD | 59,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1217` | 2,210,000.00 USD | 2,210,000.00 USD | 1,090.00 USD | 624.33 USD | 6,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 5,290,000.00 USD | 5,290,000.00 USD | 18,490.00 USD | 6,160.00 USD | 11,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1219` | 2,220,000.00 USD | 2,220,000.00 USD | 2,320.00 USD | 718.82 USD | 10,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1219` | 5,360,000.00 USD | 5,360,000.00 USD | 26,700.00 USD | 5,500.00 USD | 38,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1221` | 2,240,000.00 USD | 2,240,000.00 USD | 4,680.00 USD | 2,940.00 USD | 3,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1221` | 5,420,000.00 USD | 5,420,000.00 USD | 25,890.00 USD | 15,750.00 USD | 18,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1223` | 2,240,000.00 USD | 2,240,000.00 USD | 2,660.00 USD | 1,410.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 5,600,000.00 USD | 5,600,000.00 USD | 94,150.00 USD | 29,980.00 USD | 48,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1225` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1225` | 5,660,000.00 USD | 5,660,000.00 USD | 43,040.00 USD | 19,970.00 USD | 5,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 16,560.00 USD | 16,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1227` | 5,810,000.00 USD | 5,810,000.00 USD | 65,240.00 USD | 30,390.00 USD | 50,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 5,940,000.00 USD | 5,940,000.00 USD | 63,350.00 USD | 30,490.00 USD | 40,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1231` | 6,020,000.00 USD | 6,020,000.00 USD | 21,280.00 USD | 29,380.00 USD | 27,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1233` | 6,130,000.00 USD | 6,130,000.00 USD | 57,130.00 USD | 13,020.00 USD | 40,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1235` | 6,150,000.00 USD | 6,150,000.00 USD | 4,430.00 USD | 4,720.00 USD | 9,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1237` | 6,160,000.00 USD | 6,160,000.00 USD | 4,080.00 USD | 2,760.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1239` | 6,170,000.00 USD | 6,170,000.00 USD | 8,780.00 USD | 1,270.00 USD | 352.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1241` | 6,180,000.00 USD | 6,180,000.00 USD | 6,830.00 USD | 965.35 USD | 2,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1243` | 6,200,000.00 USD | 6,200,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1245` | 6,240,000.00 USD | 6,240,000.00 USD | 15,080.00 USD | 8,080.00 USD | 12,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1247` | 6,280,000.00 USD | 6,280,000.00 USD | 19,950.00 USD | 15,870.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1249` | 6,310,000.00 USD | 6,310,000.00 USD | 13,440.00 USD | 5,480.00 USD | 5,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1251` | 6,330,000.00 USD | 6,330,000.00 USD | 7,660.00 USD | 5,070.00 USD | 8,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1253` | 6,360,000.00 USD | 6,360,000.00 USD | 11,420.00 USD | 2,100.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1255` | 6,370,000.00 USD | 6,370,000.00 USD | 2,250.00 USD | 13,990.00 USD | 78.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1257` | 6,390,000.00 USD | 6,390,000.00 USD | 15,610.00 USD | 5,200.00 USD | 61.49 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1259` | 6,390,000.00 USD | 6,390,000.00 USD | 0.00 USD | 0.00 USD | 68.78 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1261` | 6,400,000.00 USD | 6,400,000.00 USD | 4,270.00 USD | 0.00 USD | 3,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1263` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 0.00 USD | 4,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1265` | 6,410,000.00 USD | 6,410,000.00 USD | 2,710.00 USD | 0.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1267` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 0.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1269` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 0.00 USD | 31.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1271` | 6,420,000.00 USD | 6,420,000.00 USD | 5,940.00 USD | 0.00 USD | 13.94 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1355` | 1,330.00 USD | 17,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1505` | 15,050.00 USD | 32,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1555` | 6,210.00 USD | 39,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1565` | 550.61 USD | 39,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1615` | 21,050.00 USD | 60,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1695` | 169.25 USD | 60,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1865` | 272.66 USD | 61,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1935` | 935.32 USD | 62,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0395` | 242,930.00 USD | 0.00 USD | 416.18 USD | `-64.12%` | `10,536.30` |
| `Live` | `Long` | `0.0495` | 242,510.00 USD | 0.00 USD | 3,450.00 USD | `-55.04%` | `69,790.10` |
| `Live` | `Long` | `0.0515` | 239,050.00 USD | 0.00 USD | 262.59 USD | `-53.22%` | `5,098.90` |
| `Live` | `Long` | `0.0545` | 238,790.00 USD | 0.00 USD | 3,460.00 USD | `-50.50%` | `63,403.00` |
| `Live` | `Long` | `0.0575` | 235,340.00 USD | 0.00 USD | 829.69 USD | `-47.77%` | `14,429.40` |
| `Live` | `Long` | `0.0615` | 234,510.00 USD | 0.00 USD | 1,100.00 USD | `-44.14%` | `17,943.80` |
| `Live` | `Long` | `0.0645` | 233,400.00 USD | 0.00 USD | 353.81 USD | `-41.42%` | `5,485.40` |
| `Live` | `Long` | `0.0665` | 233,050.00 USD | 0.00 USD | 509.64 USD | `-39.60%` | `7,663.80` |
| `Live` | `Long` | `0.0675` | 232,540.00 USD | 0.00 USD | 518.48 USD | `-38.69%` | `7,681.20` |
| `Live` | `Long` | `0.0685` | 232,020.00 USD | 0.00 USD | 1,920.00 USD | `-37.78%` | `28,000.00` |
| `Live` | `Long` | `0.0725` | 230,100.00 USD | 0.00 USD | 25,370.00 USD | `-34.15%` | `349,988.60` |
| `Live` | `Long` | `0.0735` | 204,730.00 USD | 0.00 USD | 4,380.00 USD | `-33.24%` | `59,562.80` |
| `Live` | `Long` | `0.0745` | 200,350.00 USD | 0.00 USD | 44,410.00 USD | `-32.33%` | `596,139.40` |
| `Live` | `Long` | `0.0755` | 155,940.00 USD | 0.00 USD | 1,020.00 USD | `-31.43%` | `13,481.90` |
| `Live` | `Long` | `0.0765` | 154,920.00 USD | 0.00 USD | 1,280.00 USD | `-30.52%` | `16,770.60` |
| `Live` | `Long` | `0.0775` | 153,640.00 USD | 0.00 USD | 1,730.00 USD | `-29.61%` | `22,308.00` |
| `Live` | `Long` | `0.0795` | 151,910.00 USD | 0.00 USD | 1,320.00 USD | `-27.79%` | `16,641.80` |
| `Live` | `Long` | `0.0805` | 150,590.00 USD | 0.00 USD | 223.98 USD | `-26.88%` | `2,782.40` |
| `Live` | `Long` | `0.0815` | 150,360.00 USD | 0.00 USD | 1,560.00 USD | `-25.98%` | `19,181.40` |
| `Live` | `Long` | `0.0875` | 148,800.00 USD | 0.00 USD | 2,380.00 USD | `-20.53%` | `27,146.60` |
| `Live` | `Long` | `0.0895` | 146,420.00 USD | 0.00 USD | 3,120.00 USD | `-18.71%` | `34,873.20` |
| `Live` | `Long` | `0.0905` | 143,300.00 USD | 0.00 USD | 443.16 USD | `-17.80%` | `4,896.80` |
| `Live` | `Long` | `0.0925` | 142,860.00 USD | 0.00 USD | 16,670.00 USD | `-15.99%` | `180,203.00` |
| `Live` | `Long` | `0.0945` | 126,190.00 USD | 0.00 USD | 69,120.00 USD | `-14.17%` | `731,405.60` |
| `Live` | `Long` | `0.0955` | 57,070.00 USD | 0.00 USD | 5,610.00 USD | `-13.26%` | `58,700.70` |
| `Live` | `Long` | `0.0965` | 51,470.00 USD | 0.00 USD | 419.87 USD | `-12.35%` | `4,351.00` |
| `Live` | `Long` | `0.0975` | 51,050.00 USD | 0.00 USD | 12,670.00 USD | `-11.44%` | `129,987.90` |
| `Live` | `Long` | `0.0985` | 38,370.00 USD | 0.00 USD | 19,960.00 USD | `-10.54%` | `202,627.30` |
| `Live` | `Long` | `0.1005` | 18,410.00 USD | 0.00 USD | 427.25 USD | `-8.72%` | `4,251.20` |
| `Live` | `Long` | `0.1015` | 17,990.00 USD | 0.00 USD | 622.37 USD | `-7.81%` | `6,131.70` |
| `Live` | `Long` | `0.1025` | 17,360.00 USD | 0.00 USD | 17,360.00 USD | `-6.90%` | `169,408.50` |
| `Live` | `Short` | `0.1225` | 16,560.00 USD | 16,560.00 USD | 0.00 USD | `+11.26%` | `135,191.80` |
| `Live` | `Short` | `0.1355` | 17,890.00 USD | 1,330.00 USD | 0.00 USD | `+23.07%` | `9,843.80` |
| `Live` | `Short` | `0.1505` | 32,940.00 USD | 15,050.00 USD | 0.00 USD | `+36.69%` | `100,000.40` |
| `Live` | `Short` | `0.1555` | 39,150.00 USD | 6,210.00 USD | 0.00 USD | `+41.24%` | `39,929.50` |
| `Live` | `Short` | `0.1565` | 39,700.00 USD | 550.61 USD | 0.00 USD | `+42.14%` | `3,518.30` |
| `Live` | `Short` | `0.1615` | 60,750.00 USD | 21,050.00 USD | 0.00 USD | `+46.68%` | `130,332.00` |
| `Live` | `Short` | `0.1695` | 60,920.00 USD | 169.25 USD | 0.00 USD | `+53.95%` | `998.50` |
| `Live` | `Short` | `0.1865` | 61,200.00 USD | 272.66 USD | 0.00 USD | `+69.39%` | `1,462.00` |
| `Live` | `Short` | `0.1935` | 62,130.00 USD | 935.32 USD | 0.00 USD | `+75.75%` | `4,833.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0635` | 177,200.00 USD | 0.00 USD | 1,140.00 USD | `-42.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 176,060.00 USD | 0.00 USD | 773.46 USD | `-35.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 175,290.00 USD | 0.00 USD | 592.27 USD | `-35.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 174,700.00 USD | 0.00 USD | 755.00 USD | `-31.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0805` | 173,940.00 USD | 0.00 USD | 411.06 USD | `-26.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0815` | 173,530.00 USD | 0.00 USD | 183.49 USD | `-25.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0835` | 173,350.00 USD | 0.00 USD | 456.70 USD | `-24.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 172,890.00 USD | 0.00 USD | 631.58 USD | `-22.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 172,260.00 USD | 0.00 USD | 653.74 USD | `-19.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0915` | 171,610.00 USD | 0.00 USD | 1,460.00 USD | `-16.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 170,140.00 USD | 0.00 USD | 485.13 USD | `-14.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0975` | 169,660.00 USD | 0.00 USD | 720.22 USD | `-11.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0985` | 168,940.00 USD | 0.00 USD | 931.75 USD | `-10.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0995` | 168,010.00 USD | 0.00 USD | 801.64 USD | `-9.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 167,200.00 USD | 0.00 USD | 2,180.00 USD | `-8.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1015` | 165,030.00 USD | 0.00 USD | 903.42 USD | `-7.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 164,120.00 USD | 0.00 USD | 780.70 USD | `-6.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1035` | 163,340.00 USD | 0.00 USD | 4,650.00 USD | `-5.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1045` | 158,690.00 USD | 0.00 USD | 18,950.00 USD | `-5.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1055` | 139,750.00 USD | 0.00 USD | 7,770.00 USD | `-4.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1065` | 131,970.00 USD | 0.00 USD | 109,280.00 USD | `-3.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 22,690.00 USD | 0.00 USD | 21,900.00 USD | `-2.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 789.40 USD | 0.00 USD | 150.04 USD | `-1.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1095` | 639.36 USD | 0.00 USD | 639.36 USD | `-0.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 162.59 USD | 162.59 USD | 0.00 USD | `+0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 1,000.00 USD | 839.64 USD | 0.00 USD | `+1.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1125` | 1,790.00 USD | 786.65 USD | 0.00 USD | `+2.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1135` | 1,910.00 USD | 116.27 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1145` | 2,040.00 USD | 134.61 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,530.00 USD | 489.97 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1165` | 2,710.00 USD | 180.81 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1175` | 30,240.00 USD | 27,530.00 USD | 0.00 USD | `+6.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1185` | 31,290.00 USD | 1,050.00 USD | 0.00 USD | `+7.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1195` | 45,930.00 USD | 14,640.00 USD | 0.00 USD | `+8.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1205` | 46,330.00 USD | 398.42 USD | 0.00 USD | `+9.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1225` | 47,310.00 USD | 980.00 USD | 0.00 USD | `+11.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1235` | 60,290.00 USD | 12,980.00 USD | 0.00 USD | `+12.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1255` | 64,660.00 USD | 4,380.00 USD | 0.00 USD | `+13.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1265` | 75,120.00 USD | 10,460.00 USD | 0.00 USD | `+14.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1275` | 75,620.00 USD | 492.06 USD | 0.00 USD | `+15.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1305` | 76,060.00 USD | 444.24 USD | 0.00 USD | `+18.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1315` | 107,620.00 USD | 31,560.00 USD | 0.00 USD | `+19.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1335` | 108,940.00 USD | 1,310.00 USD | 0.00 USD | `+21.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1345` | 113,090.00 USD | 4,150.00 USD | 0.00 USD | `+22.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1365` | 123,780.00 USD | 10,690.00 USD | 0.00 USD | `+23.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1405` | 136,890.00 USD | 13,110.00 USD | 0.00 USD | `+27.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1425` | 136,990.00 USD | 102.22 USD | 0.00 USD | `+29.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1435` | 144,160.00 USD | 7,180.00 USD | 0.00 USD | `+30.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1485` | 146,810.00 USD | 2,650.00 USD | 0.00 USD | `+34.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1495` | 147,600.00 USD | 792.53 USD | 0.00 USD | `+35.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1525` | 151,370.00 USD | 3,770.00 USD | 0.00 USD | `+38.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 151,550.00 USD | 184.49 USD | 0.00 USD | `+41.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 158,270.00 USD | 6,720.00 USD | 0.00 USD | `+42.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 158,490.00 USD | 219.81 USD | 0.00 USD | `+43.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 158,770.00 USD | 277.62 USD | 0.00 USD | `+48.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 160,570.00 USD | 1,800.00 USD | 0.00 USD | `+53.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 160,780.00 USD | 216.55 USD | 0.00 USD | `+58.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 160,900.00 USD | 117.26 USD | 0.00 USD | `+79.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 181,430.00 USD | 20,530.00 USD | 0.00 USD | `+82.11%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0957` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 7.93 USD |
| `7D` | `0.0959` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 2,410.00 USD | 1,140.00 USD | 5.33 USD |
| `7D` | `0.0961` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 4.23 USD |
| `1D` | `0.0963` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 1.02 USD |
| `7D` | `0.0963` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 1,210.00 USD |
| `1D` | `0.0965` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 1,280.00 USD | 282.32 USD | 1,790.00 USD |
| `7D` | `0.0965` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 34.36 USD |
| `1D` | `0.0967` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 2,660.00 USD | 1,100.00 USD | 7,500.00 USD |
| `7D` | `0.0967` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 3,770.00 USD | 2,660.00 USD | 2,830.00 USD |
| `1D` | `0.0969` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 4,590.00 USD | 2,640.00 USD | 9,010.00 USD |
| `7D` | `0.0969` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 0.00 USD | 2,810.00 USD | 13,760.00 USD |
| `1D` | `0.0971` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 2,150.00 USD | 3,330.00 USD | 4,400.00 USD |
| `7D` | `0.0971` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 0.00 USD | 2,000.00 USD | 4,660.00 USD |
| `1D` | `0.0973` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 2,120.00 USD | 4,320.00 USD |
| `7D` | `0.0973` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 0.00 USD | 1,390.00 USD | 2,830.00 USD |
| `1D` | `0.0975` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | 1,810.00 USD | 5,550.00 USD |
| `7D` | `0.0975` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 0.00 USD | 1,160.00 USD | 4,230.00 USD |
| `1D` | `0.0977` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 8,290.00 USD | 2,510.00 USD | 4,670.00 USD |
| `7D` | `0.0977` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 8,960.00 USD |
| `1D` | `0.0979` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 0.00 USD | 1,040.00 USD | 8.08 USD |
| `7D` | `0.0979` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 0.00 USD | 1,530.00 USD | 5,680.00 USD |
| `1D` | `0.0981` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 0.00 USD | 431.42 USD | 3,030.00 USD |
| `7D` | `0.0981` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 0.00 USD | 2,390.00 USD | 5,910.00 USD |
| `1D` | `0.0983` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 3,250.00 USD | 1,390.00 USD | 9,680.00 USD |
| `7D` | `0.0983` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 7,990.00 USD | 1,230.00 USD | 8,920.00 USD |
| `1D` | `0.0985` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 5,670.00 USD | 413.94 USD | 2,690.00 USD |
| `7D` | `0.0985` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 7,110.00 USD | 0.00 USD | 6,320.00 USD |
| `1D` | `0.0987` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 7,790.00 USD | 2,190.00 USD | 4,810.00 USD |
| `7D` | `0.0987` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 5,390.00 USD | 9,190.00 USD | 37,300.00 USD |
| `1D` | `0.0989` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 2,820.00 USD | 3,290.00 USD | 2,180.00 USD |
| `7D` | `0.0989` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 12,260.00 USD | 4,520.00 USD | 27,230.00 USD |
| `1D` | `0.0991` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 4,800.00 USD | 2,950.00 USD | 3,200.00 USD |
| `7D` | `0.0991` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 14,350.00 USD | 10,350.00 USD | 13,610.00 USD |
| `1D` | `0.0993` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 3,080.00 USD | 1,720.00 USD | 11,460.00 USD |
| `7D` | `0.0993` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 23,920.00 USD | 10,140.00 USD | 24,010.00 USD |
| `1D` | `0.0995` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 2,740.00 USD | 624.33 USD | 11,480.00 USD |
| `7D` | `0.0995` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 13,090.00 USD | 6,160.00 USD | 25,260.00 USD |
| `1D` | `0.0997` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 2,320.00 USD | 718.82 USD | 10,030.00 USD |
| `7D` | `0.0997` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 21,100.00 USD | 5,500.00 USD | 33,050.00 USD |
| `1D` | `0.0999` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 4,680.00 USD | 2,940.00 USD | 3,670.00 USD |
| `7D` | `0.0999` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 14,230.00 USD | 6,540.00 USD | 18,810.00 USD |
| `1D` | `0.1001` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 2,660.00 USD | 1,410.00 USD | 4,200.00 USD |
| `7D` | `0.1001` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 29,230.00 USD | 3,010.00 USD | 10,890.00 USD |
| `1D` | `0.1003` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 0.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1003` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 8,010.00 USD | 7,060.00 USD | 5,200.00 USD |
| `1D` | `0.1005` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 1,970.00 USD | 403.62 USD | 1,140.00 USD |
| `7D` | `0.1005` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 25,070.00 USD | 11,000.00 USD | 18,400.00 USD |
| `1D` | `0.1007` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 430.11 USD | 807.50 USD |
| `7D` | `0.1007` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 10,260.00 USD | 2,280.00 USD | 14,080.00 USD |
| `1D` | `0.1009` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 1,250.00 USD | 2,750.00 USD | 23.95 USD |
| `7D` | `0.1009` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 15,320.00 USD | 3,070.00 USD | 6,790.00 USD |
| `1D` | `0.1011` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 575.54 USD | 3,420.00 USD |
| `7D` | `0.1011` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 4,430.00 USD | 4,720.00 USD | 9,190.00 USD |
| `1D` | `0.1013` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 4,900.00 USD | 800.79 USD | 645.83 USD |
| `7D` | `0.1013` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 12,870.00 USD | 4,030.00 USD | 3,000.00 USD |
| `1D` | `0.1015` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 540.82 USD | 1,830.00 USD | 1,680.00 USD |
| `7D` | `0.1015` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 6,830.00 USD | 965.35 USD | 2,380.00 USD |
| `1D` | `0.1017` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 1,660.00 USD | 4,600.00 USD | 5,800.00 USD |
| `7D` | `0.1017` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,750.00 USD |
| `1D` | `0.1019` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 4,630.00 USD | 3,420.00 USD | 5,520.00 USD |
| `7D` | `0.1019` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 9,260.00 USD | 5,790.00 USD | 13,210.00 USD |
| `1D` | `0.1021` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 2,580.00 USD | 1,320.00 USD | 4,780.00 USD |
| `7D` | `0.1021` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 7,900.00 USD | 3,270.00 USD | 7,130.00 USD |
| `1D` | `0.1023` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 4,600.00 USD | 2,120.00 USD | 2,720.00 USD |
| `7D` | `0.1023` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 4,030.00 USD | 4,990.00 USD | 14,420.00 USD |
| `1D` | `0.1025` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 1,560.00 USD | 974.29 USD |
| `7D` | `0.1025` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 1,550.00 USD | 0.00 USD | 5,700.00 USD |
| `1D` | `0.1027` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 936.16 USD | 1,620.00 USD |
| `7D` | `0.1027` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 2,250.00 USD | 2,580.00 USD | 282.63 USD |
| `1D` | `0.1029` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 4,340.00 USD | 705.79 USD | 6,270.00 USD |
| `7D` | `0.1029` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 7,420.00 USD | 3,000.00 USD | 470.94 USD |
| `1D` | `0.1031` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 11,680.00 USD | 3,170.00 USD | 18,890.00 USD |
| `7D` | `0.1031` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 13,690.00 USD | 5,070.00 USD | 10,820.00 USD |
| `1D` | `0.1033` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 15,450.00 USD | 4,740.00 USD | 21,860.00 USD |
| `7D` | `0.1033` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 3,880.00 USD | 2,640.00 USD | 25,980.00 USD |
| `1D` | `0.1035` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 7,450.00 USD | 7,560.00 USD | 12,410.00 USD |
| `7D` | `0.1035` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 8,450.00 USD | 9,400.00 USD | 16,090.00 USD |
| `1D` | `0.1037` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 4,370.00 USD | 11,960.00 USD | 9,270.00 USD |
| `7D` | `0.1037` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 31,160.00 USD |
| `1D` | `0.1039` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 3,660.00 USD | 4,750.00 USD | 11,830.00 USD |
| `7D` | `0.1039` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 0.00 USD | 7,390.00 USD | 75.48 USD |
| `1D` | `0.1041` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 6,510.00 USD | 6,910.00 USD | 18,640.00 USD |
| `7D` | `0.1041` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 5,940.00 USD | 2,910.00 USD | 18,710.00 USD |
| `1D` | `0.1043` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 19,210.00 USD | 5,650.00 USD | 7,860.00 USD |
| `7D` | `0.1043` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 15,960.00 USD | 5,980.00 USD | 20,830.00 USD |
| `1D` | `0.1045` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 0.00 USD | 2,600.00 USD | 6,210.00 USD |
| `7D` | `0.1045` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 0.00 USD | 9,810.00 USD | 15,260.00 USD |
| `1D` | `0.1047` | 999,480.00 USD | 0.00 USD | 999,480.00 USD | 4,610.00 USD | 3,400.00 USD | 20,630.00 USD |
| `7D` | `0.1047` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 0.00 USD | 1,720.00 USD | 22,670.00 USD |
| `1D` | `0.1049` | 970,840.00 USD | 0.00 USD | 970,840.00 USD | 21,050.00 USD | 2,430.00 USD | 10,840.00 USD |
| `7D` | `0.1049` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 34,790.00 USD | 4,810.00 USD | 35,700.00 USD |
| `1D` | `0.1051` | 936,520.00 USD | 0.00 USD | 936,520.00 USD | 16,410.00 USD | 8,750.00 USD | 24,260.00 USD |
| `7D` | `0.1051` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 17,290.00 USD | 11,500.00 USD | 48,480.00 USD |
| `1D` | `0.1053` | 887,090.00 USD | 0.00 USD | 887,090.00 USD | 35,030.00 USD | 8,930.00 USD | 50,850.00 USD |
| `7D` | `0.1053` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 53,590.00 USD | 29,800.00 USD | 95,890.00 USD |
| `1D` | `0.1055` | 792,280.00 USD | 0.00 USD | 792,280.00 USD | 43,960.00 USD | 25,140.00 USD | 59,610.00 USD |
| `7D` | `0.1055` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 61,560.00 USD | 27,290.00 USD | 148,060.00 USD |
| `1D` | `0.1057` | 663,570.00 USD | 0.00 USD | 663,570.00 USD | 27,300.00 USD | 25,430.00 USD | 50,080.00 USD |
| `7D` | `0.1057` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 50,380.00 USD | 45,760.00 USD | 97,550.00 USD |
| `1D` | `0.1059` | 560,750.00 USD | 0.00 USD | 560,750.00 USD | 19,020.00 USD | 23,540.00 USD | 56,080.00 USD |
| `7D` | `0.1059` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 92,510.00 USD | 49,670.00 USD | 117,940.00 USD |
| `1D` | `0.1061` | 462,120.00 USD | 0.00 USD | 462,120.00 USD | 10,960.00 USD | 14,570.00 USD | 58,940.00 USD |
| `7D` | `0.1061` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 38,260.00 USD | 30,500.00 USD | 76,280.00 USD |
| `1D` | `0.1063` | 377,650.00 USD | 0.00 USD | 377,650.00 USD | 60,370.00 USD | 14,600.00 USD | 48,900.00 USD |
| `7D` | `0.1063` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 84,260.00 USD | 38,330.00 USD | 164,570.00 USD |
| `1D` | `0.1065` | 253,780.00 USD | 0.00 USD | 253,780.00 USD | 18,270.00 USD | 14,110.00 USD | 19,400.00 USD |
| `7D` | `0.1065` | 739,970.00 USD | 0.00 USD | 739,970.00 USD | 91,170.00 USD | 17,310.00 USD | 93,400.00 USD |
| `1D` | `0.1067` | 202,000.00 USD | 0.00 USD | 202,000.00 USD | 9,710.00 USD | 15,160.00 USD | 33,130.00 USD |
| `7D` | `0.1067` | 538,090.00 USD | 0.00 USD | 538,090.00 USD | 97,290.00 USD | 48,680.00 USD | 68,010.00 USD |
| `1D` | `0.1069` | 144,000.00 USD | 0.00 USD | 144,000.00 USD | 24,070.00 USD | 9,100.00 USD | 42,650.00 USD |
| `7D` | `0.1069` | 324,110.00 USD | 0.00 USD | 324,110.00 USD | 74,290.00 USD | 31,620.00 USD | 71,630.00 USD |
| `1D` | `0.1071` | 68,180.00 USD | 0.00 USD | 68,180.00 USD | 48,660.00 USD | 3,140.00 USD | 16,220.00 USD |
| `7D` | `0.1071` | 146,560.00 USD | 0.00 USD | 146,560.00 USD | 59,900.00 USD | 26,150.00 USD | 42,580.00 USD |
| `1D` | `0.1073` | 162.61 USD | 0.00 USD | 162.61 USD | 0.00 USD | 0.00 USD | 23.75 USD |
| `7D` | `0.1073` | 17,930.00 USD | 0.00 USD | 17,930.00 USD | 0.00 USD | 17,700.00 USD | 84.54 USD |
| `1D` | `0.1075` | 138.86 USD | 0.00 USD | 138.86 USD | 0.00 USD | 0.00 USD | 18.60 USD |
| `7D` | `0.1075` | 139.75 USD | 0.00 USD | 139.75 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1077` | 120.26 USD | 0.00 USD | 120.26 USD | 0.00 USD | 0.00 USD | 93.46 USD |
| `1D` | `0.1079` | 26.80 USD | 0.00 USD | 26.80 USD | 0.00 USD | 0.00 USD | 26.80 USD |
| `7D` | `0.1079` | 110.55 USD | 0.00 USD | 110.55 USD | 0.00 USD | 0.00 USD | 110.55 USD |
| `7D` | `0.1081` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1082` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1083` | 9,750.00 USD | 9,750.00 USD | 0.00 USD | 9,730.00 USD | 0.00 USD | 21.66 USD |
| `7D` | `0.1083` | 69,720.00 USD | 69,720.00 USD | 0.00 USD | 69,720.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1085` | 77,990.00 USD | 77,990.00 USD | 0.00 USD | 0.00 USD | 3,210.00 USD | 65,020.00 USD |
| `7D` | `0.1085` | 85,640.00 USD | 85,640.00 USD | 0.00 USD | 15,920.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1087` | 173,300.00 USD | 173,300.00 USD | 0.00 USD | 44,350.00 USD | 6,300.00 USD | 44,670.00 USD |
| `7D` | `0.1087` | 141,080.00 USD | 141,080.00 USD | 0.00 USD | 55,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1089` | 204,190.00 USD | 204,190.00 USD | 0.00 USD | 30,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1089` | 146,370.00 USD | 146,370.00 USD | 0.00 USD | 5,290.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1091` | 237,890.00 USD | 237,890.00 USD | 0.00 USD | 33,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1091` | 171,680.00 USD | 171,680.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD |
| `1D` | `0.1093` | 253,370.00 USD | 253,370.00 USD | 0.00 USD | 15,480.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1093` | 180,420.00 USD | 180,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,730.00 USD |
| `1D` | `0.1095` | 280,890.00 USD | 280,890.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 21,520.00 USD |
| `1D` | `0.1097` | 312,900.00 USD | 312,900.00 USD | 0.00 USD | 7,260.00 USD | 1,970.00 USD | 22,790.00 USD |
| `1D` | `0.1099` | 320,970.00 USD | 320,970.00 USD | 0.00 USD | 6,130.00 USD | 1,940.00 USD | 0.00 USD |
| `7D` | `0.1099` | 213,720.00 USD | 213,720.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 21,840.00 USD |
| `1D` | `0.1101` | 332,380.00 USD | 332,380.00 USD | 0.00 USD | 4,310.00 USD | 2,820.00 USD | 4,290.00 USD |
| `7D` | `0.1101` | 236,930.00 USD | 236,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1103` | 333,680.00 USD | 333,680.00 USD | 0.00 USD | 0.00 USD | 1,300.00 USD | 0.00 USD |
| `7D` | `0.1103` | 254,420.00 USD | 254,420.00 USD | 0.00 USD | 17,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1105` | 349,120.00 USD | 349,120.00 USD | 0.00 USD | 0.00 USD | 4,740.00 USD | 10,700.00 USD |
| `7D` | `0.1105` | 268,900.00 USD | 268,900.00 USD | 0.00 USD | 0.00 USD | 14,480.00 USD | 0.00 USD |
| `1D` | `0.1107` | 400,690.00 USD | 400,690.00 USD | 0.00 USD | 3,110.00 USD | 12,720.00 USD | 35,750.00 USD |
| `7D` | `0.1107` | 297,360.00 USD | 297,360.00 USD | 0.00 USD | 0.00 USD | 12,510.00 USD | 15,950.00 USD |
| `7D` | `0.1109` | 309,890.00 USD | 309,890.00 USD | 0.00 USD | 0.00 USD | 12,430.00 USD | 97.30 USD |
| `7D` | `0.1111` | 321,840.00 USD | 321,840.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 0.00 USD |
| `1D` | `0.1113` | 460,780.00 USD | 460,780.00 USD | 0.00 USD | 15,810.00 USD | 5,210.00 USD | 39,070.00 USD |
| `1D` | `0.1115` | 465,540.00 USD | 465,540.00 USD | 0.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1115` | 321,850.00 USD | 321,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9.84 USD |
| `1D` | `0.1117` | 527,950.00 USD | 527,950.00 USD | 0.00 USD | 2,060.00 USD | 25,630.00 USD | 34,720.00 USD |
| `7D` | `0.1117` | 361,120.00 USD | 361,120.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | 16,490.00 USD |
| `1D` | `0.1119` | 602,020.00 USD | 602,020.00 USD | 0.00 USD | 30,350.00 USD | 6,980.00 USD | 36,740.00 USD |
| `7D` | `0.1119` | 415,140.00 USD | 415,140.00 USD | 0.00 USD | 25,250.00 USD | 7,050.00 USD | 21,720.00 USD |
| `1D` | `0.1121` | 643,840.00 USD | 643,840.00 USD | 0.00 USD | 17,450.00 USD | 12,060.00 USD | 12,310.00 USD |
| `7D` | `0.1121` | 442,050.00 USD | 442,050.00 USD | 0.00 USD | 5,730.00 USD | 0.00 USD | 21,180.00 USD |
| `1D` | `0.1123` | 688,260.00 USD | 688,260.00 USD | 0.00 USD | 36,720.00 USD | 1,780.00 USD | 5,930.00 USD |
| `7D` | `0.1123` | 516,170.00 USD | 516,170.00 USD | 0.00 USD | 12,360.00 USD | 23,980.00 USD | 37,780.00 USD |
| `1D` | `0.1125` | 716,430.00 USD | 716,430.00 USD | 0.00 USD | 7,670.00 USD | 12,550.00 USD | 7,950.00 USD |
| `7D` | `0.1125` | 554,630.00 USD | 554,630.00 USD | 0.00 USD | 0.00 USD | 2,230.00 USD | 36,230.00 USD |
| `1D` | `0.1127` | 737,160.00 USD | 737,160.00 USD | 0.00 USD | 0.00 USD | 1,250.00 USD | 19,480.00 USD |
| `7D` | `0.1127` | 562,610.00 USD | 562,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,980.00 USD |
| `1D` | `0.1129` | 745,880.00 USD | 745,880.00 USD | 0.00 USD | 8,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1129` | 562,620.00 USD | 562,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14.44 USD |
| `1D` | `0.1131` | 781,420.00 USD | 781,420.00 USD | 0.00 USD | 17,560.00 USD | 6,360.00 USD | 11,620.00 USD |
| `7D` | `0.1131` | 590,190.00 USD | 590,190.00 USD | 0.00 USD | 12,540.00 USD | 0.00 USD | 15,020.00 USD |
| `1D` | `0.1133` | 833,930.00 USD | 833,930.00 USD | 0.00 USD | 6,530.00 USD | 22,520.00 USD | 23,470.00 USD |
| `7D` | `0.1133` | 601,610.00 USD | 601,610.00 USD | 0.00 USD | 0.00 USD | 11,430.00 USD | 0.00 USD |
| `1D` | `0.1135` | 845,730.00 USD | 845,730.00 USD | 0.00 USD | 4,040.00 USD | 3,670.00 USD | 4,090.00 USD |
| `7D` | `0.1135` | 616,140.00 USD | 616,140.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD |
| `1D` | `0.1137` | 846,630.00 USD | 846,630.00 USD | 0.00 USD | 0.00 USD | 856.93 USD | 40.44 USD |
| `7D` | `0.1137` | 616,330.00 USD | 616,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 192.92 USD |
| `1D` | `0.1139` | 860,890.00 USD | 860,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,260.00 USD |
| `7D` | `0.1139` | 616,350.00 USD | 616,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21.32 USD |
| `1D` | `0.1141` | 891,020.00 USD | 891,020.00 USD | 0.00 USD | 13,860.00 USD | 2,800.00 USD | 13,480.00 USD |
| `7D` | `0.1141` | 634,300.00 USD | 634,300.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,570.00 USD |
| `1D` | `0.1143` | 951,130.00 USD | 951,130.00 USD | 0.00 USD | 20,300.00 USD | 27,990.00 USD | 11,820.00 USD |
| `7D` | `0.1143` | 712,960.00 USD | 712,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78,660.00 USD |
| `1D` | `0.1145` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 13,430.00 USD | 11,690.00 USD | 38,030.00 USD |
| `7D` | `0.1145` | 873,410.00 USD | 873,410.00 USD | 0.00 USD | 16,540.00 USD | 2,730.00 USD | 141,180.00 USD |
| `1D` | `0.1147` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 10,640.00 USD | 10,080.00 USD | 30,680.00 USD |
| `7D` | `0.1147` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 138,370.00 USD |
| `1D` | `0.1149` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 35,170.00 USD | 624.71 USD | 31,820.00 USD |
| `7D` | `0.1149` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 10,560.00 USD | 0.00 USD | 72,790.00 USD |
| `1D` | `0.1151` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 16,450.00 USD | 14,620.00 USD | 33,180.00 USD |
| `7D` | `0.1151` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 92,570.00 USD | 4,210.00 USD | 128,360.00 USD |
| `1D` | `0.1153` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 39,450.00 USD | 29,420.00 USD | 59,030.00 USD |
| `7D` | `0.1153` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 153,720.00 USD | 8,400.00 USD | 139,840.00 USD |
| `1D` | `0.1155` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 38,430.00 USD | 27,080.00 USD | 54,030.00 USD |
| `7D` | `0.1155` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 149,360.00 USD | 40,110.00 USD | 105,730.00 USD |
| `1D` | `0.1157` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 37,790.00 USD | 12,010.00 USD | 25,390.00 USD |
| `7D` | `0.1157` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 133,960.00 USD | 3,760.00 USD | 48,310.00 USD |
| `1D` | `0.1159` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 27,270.00 USD | 12,000.00 USD | 25,170.00 USD |
| `7D` | `0.1159` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 81,080.00 USD | 12,710.00 USD | 53,350.00 USD |
| `1D` | `0.1161` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 23,670.00 USD | 0.00 USD | 5,160.00 USD |
| `7D` | `0.1161` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 146,810.00 USD | 37,250.00 USD | 99,850.00 USD |
| `1D` | `0.1163` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 4,290.00 USD | 9,380.00 USD | 17,460.00 USD |
| `7D` | `0.1163` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 53,510.00 USD | 11,460.00 USD | 68,950.00 USD |
| `1D` | `0.1165` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 8,820.00 USD | 11,680.00 USD | 5,490.00 USD |
| `7D` | `0.1165` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 68,620.00 USD | 35,720.00 USD | 27,170.00 USD |
| `1D` | `0.1167` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 5,680.00 USD | 6,040.00 USD | 6,170.00 USD |
| `7D` | `0.1167` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 79,610.00 USD | 21,620.00 USD | 41,210.00 USD |
| `1D` | `0.1169` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 5,480.00 USD | 2,440.00 USD | 5,990.00 USD |
| `7D` | `0.1169` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 65,340.00 USD | 14,840.00 USD | 86,480.00 USD |
| `1D` | `0.1171` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 13,800.00 USD | 0.00 USD | 4,510.00 USD |
| `7D` | `0.1171` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 57,350.00 USD | 11,370.00 USD | 35,340.00 USD |
| `1D` | `0.1173` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 9,320.00 USD | 5,440.00 USD | 4,840.00 USD |
| `7D` | `0.1173` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 40,860.00 USD | 9,190.00 USD | 36,600.00 USD |
| `1D` | `0.1175` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 11,510.00 USD | 11,920.00 USD | 19,930.00 USD |
| `7D` | `0.1175` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 38,840.00 USD | 12,300.00 USD | 58,820.00 USD |
| `1D` | `0.1177` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 14,360.00 USD | 8,560.00 USD | 16,650.00 USD |
| `7D` | `0.1177` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 33,330.00 USD | 20,350.00 USD | 44,230.00 USD |
| `1D` | `0.1179` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 12,760.00 USD | 5,840.00 USD | 14,520.00 USD |
| `7D` | `0.1179` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 66,670.00 USD | 10,940.00 USD | 24,020.00 USD |
| `1D` | `0.1181` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 16,300.00 USD | 6,410.00 USD | 19,280.00 USD |
| `7D` | `0.1181` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 22,290.00 USD | 15,780.00 USD | 17,490.00 USD |
| `1D` | `0.1183` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 8,760.00 USD | 677.63 USD | 4,580.00 USD |
| `7D` | `0.1183` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 4,040.00 USD | 1,800.00 USD | 39,420.00 USD |
| `1D` | `0.1185` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 6,530.00 USD | 5,850.00 USD | 6,770.00 USD |
| `7D` | `0.1185` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 3,880.00 USD | 5,130.00 USD | 26,770.00 USD |
| `1D` | `0.1187` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 4,060.00 USD | 6,500.00 USD | 11,670.00 USD |
| `7D` | `0.1187` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 5,620.00 USD | 15,370.00 USD | 36,520.00 USD |
| `1D` | `0.1189` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 2,840.00 USD | 2,120.00 USD | 4,350.00 USD |
| `7D` | `0.1189` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 27,240.00 USD | 15,060.00 USD | 3,230.00 USD |
| `1D` | `0.1191` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 1,810.00 USD | 5,650.00 USD |
| `7D` | `0.1191` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 22,650.00 USD | 15,330.00 USD | 109,520.00 USD |
| `1D` | `0.1193` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 4,720.00 USD | 1,040.00 USD | 3,840.00 USD |
| `7D` | `0.1193` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 21,260.00 USD | 0.00 USD | 12,250.00 USD |
| `1D` | `0.1195` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 9,550.00 USD | 1,470.00 USD | 2,810.00 USD |
| `7D` | `0.1195` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 11,190.00 USD | 1,780.00 USD | 29,710.00 USD |
| `1D` | `0.1197` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 1,040.00 USD | 93.72 USD |
| `7D` | `0.1197` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 6,780.00 USD | 10,800.00 USD | 13,950.00 USD |
| `1D` | `0.1199` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 431.42 USD | 3,080.00 USD |
| `7D` | `0.1199` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 9,100.00 USD | 2,390.00 USD | 64,660.00 USD |
| `1D` | `0.1201` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 3,250.00 USD | 1,390.00 USD | 9,700.00 USD |
| `7D` | `0.1201` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 114,140.00 USD | 16,380.00 USD | 29,080.00 USD |
| `1D` | `0.1203` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 5,670.00 USD | 413.94 USD | 2,710.00 USD |
| `7D` | `0.1203` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 70,770.00 USD | 29,250.00 USD | 6,320.00 USD |
| `1D` | `0.1205` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 2,250.00 USD | 1,670.00 USD | 741.32 USD |
| `7D` | `0.1205` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 86,480.00 USD | 48,720.00 USD | 128,300.00 USD |
| `1D` | `0.1207` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 5,540.00 USD | 524.23 USD | 4,100.00 USD |
| `7D` | `0.1207` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 12,460.00 USD | 19,400.00 USD | 53,850.00 USD |
| `1D` | `0.1209` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 2,820.00 USD | 3,290.00 USD | 2,240.00 USD |
| `7D` | `0.1209` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 85,160.00 USD | 19,340.00 USD | 94,230.00 USD |
| `1D` | `0.1211` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 4,800.00 USD | 2,950.00 USD | 3,240.00 USD |
| `7D` | `0.1211` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 14,350.00 USD | 12,900.00 USD | 29,750.00 USD |
| `1D` | `0.1213` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 3,080.00 USD | 1,720.00 USD | 11,460.00 USD |
| `7D` | `0.1213` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 23,920.00 USD | 12,800.00 USD | 24,080.00 USD |
| `1D` | `0.1215` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD | 5,460.00 USD |
| `7D` | `0.1215` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 5,900.00 USD | 6,620.00 USD | 59,080.00 USD |
| `1D` | `0.1217` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 1,090.00 USD | 624.33 USD | 6,060.00 USD |
| `7D` | `0.1217` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 18,490.00 USD | 6,160.00 USD | 11,090.00 USD |
| `1D` | `0.1219` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 2,320.00 USD | 718.82 USD | 10,030.00 USD |
| `7D` | `0.1219` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 26,700.00 USD | 5,500.00 USD | 38,100.00 USD |
| `1D` | `0.1221` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 4,680.00 USD | 974.21 USD | 1,290.00 USD |
| `7D` | `0.1221` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 25,890.00 USD | 15,750.00 USD | 18,940.00 USD |
| `7D` | `0.1223` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 94,150.00 USD | 29,980.00 USD | 48,480.00 USD |
| `7D` | `0.1225` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 43,040.00 USD | 19,970.00 USD | 5,300.00 USD |
| `7D` | `0.1227` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 49,930.00 USD | 23,840.00 USD | 50,600.00 USD |
| `7D` | `0.1229` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 63,350.00 USD | 30,490.00 USD | 40,530.00 USD |
| `7D` | `0.1231` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 21,280.00 USD | 29,380.00 USD | 27,540.00 USD |
| `7D` | `0.1233` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 57,130.00 USD | 13,020.00 USD | 40,290.00 USD |
| `7D` | `0.1235` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 4,430.00 USD | 4,720.00 USD | 9,050.00 USD |
| `7D` | `0.1237` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 4,080.00 USD | 2,760.00 USD | 2,910.00 USD |
| `7D` | `0.1239` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 8,780.00 USD | 1,270.00 USD | 197.68 USD |
| `7D` | `0.1241` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 6,830.00 USD | 965.35 USD | 2,400.00 USD |
| `7D` | `0.1243` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 11,450.00 USD | 4,530.00 USD | 4,680.00 USD |
| `7D` | `0.1245` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 15,080.00 USD | 8,080.00 USD | 13,060.00 USD |
| `7D` | `0.1247` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 19,950.00 USD | 15,870.00 USD | 9,710.00 USD |
| `7D` | `0.1249` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 13,440.00 USD | 5,480.00 USD | 5,670.00 USD |
| `7D` | `0.1251` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 0.00 USD | 1,800.00 USD | 8,540.00 USD |
| `7D` | `0.1253` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 11,420.00 USD | 2,100.00 USD | 14,020.00 USD |
| `7D` | `0.1255` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 2,250.00 USD | 13,990.00 USD | 33.05 USD |
| `7D` | `0.1257` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 15,610.00 USD | 5,200.00 USD | 66.47 USD |
| `7D` | `0.1259` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 130.24 USD |
| `7D` | `0.1261` | 6,310,000.00 USD | 6,310,000.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `0.1263` | 6,310,000.00 USD | 6,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,100.00 USD |
| `7D` | `0.1265` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 2,710.00 USD | 0.00 USD | 3,250.00 USD |
| `7D` | `0.1267` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,930.00 USD |
| `7D` | `0.1269` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16.21 USD |
| `7D` | `0.1271` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 5,940.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1272` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10.64 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `70.93M` | Total OI Tokens: `655,586,254.4 OP`
  * 1h OI Change: `-2.32%` | 4h OI Change: `-6.57%` | 24h OI Change: `-7.64%`
  * Exchange Breakdown: Binance=`16.26M` | Bybit=`14.15M` | OKX=`4.11M` | Hyperliquid=`3.81M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-1.40K` | Last 24h: `270.64` | Last 3d: `-2.23K` | Last 7d: `-15.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0066%` | **USDT OKX** | `0.0067%` |
| **USDT Bybit** | `-0.0040%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0062%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0203%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `37.17%` | `62.83%` | `0.59` | 4,030,000.00 USD |
| `15M` | `Binance` | `55.98%` | `44.02%` | `1.27` | 1,220,000.00 USD |
| `15M` | `OKX` | `60.48%` | `39.52%` | `1.53` | 224,340.00 USD |
| `15M` | `Bybit` | `59.07%` | `40.93%` | `1.44` | 342,780.00 USD |
| `15M` | `KuCoin` | `53.55%` | `46.45%` | `1.15` | 194,490.00 USD |
| `15M` | `Gate` | `50.26%` | `49.74%` | `1.01` | 88,770.00 USD |
| `15M` | `Bitget` | `64.59%` | `35.41%` | `1.82` | 71,820.00 USD |
| `15M` | `BingX` | `5.48%` | `94.52%` | `0.06` | 1,490,000.00 USD |
| `15M` | `MEXC` | `46.55%` | `53.45%` | `0.87` | 181,510.00 USD |
| `15M` | `Bitunix` | `45.64%` | `54.36%` | `0.84` | 30,960.00 USD |
| `15M` | `Hyperliquid` | `39.1%` | `60.9%` | `0.64` | 28,460.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `44.75%` | `55.25%` | `0.81` | 90,680.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `94.24%` | `5.76%` | `16.36` | 36,770.00 USD |
| `15M` | `HTX` | `99.93%` | `0.07%` | `1427.57` | 573.63 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `57.94%` | `42.06%` | `1.38` | 18,090.00 USD |
| `15M` | `Aster` | `77%` | `23%` | `3.35` | 5,590.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0.37%` | `99.63%` | `0.00` | 3,110.00 USD |
| `15M` | `Whale Positions` | `55.98%` | `44.02%` | `1.27` | 1,220,000.00 USD |
| `15M` | `Global Accounts` | `37.17%` | `62.83%` | `0.59` | 4,030,000.00 USD |
| `1H` | `OP` | `45.03%` | `54.97%` | `0.82` | 11,100,000.00 USD |
| `1H` | `Binance` | `46.53%` | `53.47%` | `0.87` | 4,600,000.00 USD |
| `1H` | `OKX` | `45.53%` | `54.47%` | `0.84` | 1,050,000.00 USD |
| `1H` | `Bybit` | `48.25%` | `51.75%` | `0.93` | 1,320,000.00 USD |
| `1H` | `KuCoin` | `49.66%` | `50.34%` | `0.99` | 582,810.00 USD |
| `1H` | `Gate` | `63.82%` | `36.18%` | `1.76` | 342,650.00 USD |
| `1H` | `Bitget` | `44.28%` | `55.72%` | `0.79` | 359,200.00 USD |
| `1H` | `BingX` | `32.7%` | `67.3%` | `0.49` | 864,800.00 USD |
| `1H` | `MEXC` | `38.75%` | `61.25%` | `0.63` | 793,110.00 USD |
| `1H` | `Bitunix` | `49.91%` | `50.09%` | `1.00` | 252,590.00 USD |
| `1H` | `Hyperliquid` | `29.5%` | `70.5%` | `0.42` | 158,810.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.27%` | `50.73%` | `0.97` | 307,940.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `31.7%` | `68.3%` | `0.46` | 396,230.00 USD |
| `1H` | `HTX` | `36.95%` | `63.05%` | `0.59` | 1,920.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `45.82%` | `54.18%` | `0.85` | 55,020.00 USD |
| `1H` | `Aster` | `57.16%` | `42.84%` | `1.33` | 8,660.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `60.11%` | `39.89%` | `1.51` | 10,010.00 USD |
| `1H` | `Whale Positions` | `46.53%` | `53.47%` | `0.87` | 4,600,000.00 USD |
| `1H` | `Global Accounts` | `45.03%` | `54.97%` | `0.82` | 11,100,000.00 USD |
| `4H` | `OP` | `41.10%` | `58.90%` | `0.70` | 35,270,000.00 USD |
| `4H` | `Binance` | `43.21%` | `56.79%` | `0.76` | 13,150,000.00 USD |
| `4H` | `OKX` | `47.17%` | `52.83%` | `0.89` | 3,440,000.00 USD |
| `4H` | `Bybit` | `42.52%` | `57.48%` | `0.74` | 3,730,000.00 USD |
| `4H` | `KuCoin` | `49.89%` | `50.11%` | `1.00` | 2,010,000.00 USD |
| `4H` | `Gate` | `56.52%` | `43.48%` | `1.30` | 703,810.00 USD |
| `4H` | `Bitget` | `34.61%` | `65.39%` | `0.53` | 1,050,000.00 USD |
| `4H` | `BingX` | `17.82%` | `82.18%` | `0.22` | 4,660,000.00 USD |
| `4H` | `MEXC` | `43.78%` | `56.22%` | `0.78` | 2,650,000.00 USD |
| `4H` | `Bitunix` | `44.57%` | `55.43%` | `0.80` | 568,240.00 USD |
| `4H` | `Hyperliquid` | `26.26%` | `73.74%` | `0.36` | 477,900.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.27%` | `48.73%` | `1.05` | 1,290,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `46.37%` | `53.63%` | `0.86` | 1,160,000.00 USD |
| `4H` | `HTX` | `56.12%` | `43.88%` | `1.28` | 3,830.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `74.84%` | `25.16%` | `2.97` | 330,110.00 USD |
| `4H` | `Aster` | `34.58%` | `65.42%` | `0.53` | 18,010.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `70.05%` | `29.95%` | `2.34` | 18,430.00 USD |
| `4H` | `Whale Positions` | `43.21%` | `56.79%` | `0.76` | 13,150,000.00 USD |
| `4H` | `Global Accounts` | `41.10%` | `58.90%` | `0.70` | 35,270,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1113` | `0.1110` | `0.1113` | `0.1113` | `0.1106` | 261,230.00 USD | 123,873.54 USD | 137,356.46 USD | -13,482.93 USD | `-5.16%` | `17B / 9S` |
| `5:00 UTC` | `0.1108` | `0.1106` | `0.1108` | `0.1112` | `0.1101` | 266,281.73 USD | 113,817.33 USD | 152,464.41 USD | -38,647.08 USD | `-14.51%` | `15B / 30S` |
| `0:00 UTC` | `0.1097` | `0.1098` | `0.1097` | `0.1103` | `0.1094` | 698,148.28 USD | 345,564.95 USD | 352,583.33 USD | -7,018.38 USD | `-1.01%` | `13B / 19S` |
| `5:00 UTC` | `0.1102` | `0.1100` | `0.1102` | `0.1104` | `0.1095` | 273,714.46 USD | 165,910.77 USD | 107,803.69 USD | 58,107.08 USD | `+21.23%` | `25B / 9S` |
| `0:00 UTC` | `0.1097` | `0.1098` | `0.1097` | `0.1101` | `0.1096` | 225,346.74 USD | 116,304.67 USD | 109,042.07 USD | 7,262.60 USD | `+3.22%` | `6B / 4S` |
| `5:00 UTC` | `0.1098` | `0.1100` | `0.1098` | `0.1102` | `0.1096` | 199,782.25 USD | 121,152.98 USD | 78,629.27 USD | 42,523.71 USD | `+21.29%` | `24B / 5S` |
| `0:00 UTC` | `0.1103` | `0.1104` | `0.1103` | `0.1106` | `0.1100` | 230,285.46 USD | 143,965.28 USD | 86,320.18 USD | 57,645.10 USD | `+25.03%` | `14B / 4S` |
| `5:00 UTC` | `0.1102` | `0.1102` | `0.1102` | `0.1105` | `0.1099` | 215,356.47 USD | 112,661.20 USD | 102,695.27 USD | 9,965.93 USD | `+4.63%` | `7B / 11S` |
| `0:00 UTC` | `0.1077` | `0.1082` | `0.1077` | `0.1102` | `0.1070` | 2,425,114.31 USD | 1,046,280.57 USD | 1,378,833.74 USD | -332,553.17 USD | `-13.71%` | `8B / 30S` |
| `5:00 UTC` | `0.1085` | `0.1085` | `0.1085` | `0.1087` | `0.1081` | 204,181.73 USD | 124,629.07 USD | 79,552.66 USD | 45,076.41 USD | `+22.08%` | `19B / 3S` |

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
| `5m` | 654.32 USD | -23,700.00 USD | **`DISTRIBUTION`** |
| `15m` | 106,840.00 USD | 151,320.00 USD | **`ACCUMULATION`** |
| `30m` | 29,840.00 USD | -382,540.00 USD | **`DISTRIBUTION`** |
| `1h` | 27,390.00 USD | -243,910.00 USD | **`DISTRIBUTION`** |
| `2h` | 18,800.00 USD | -206,200.00 USD | **`DISTRIBUTION`** |
| `4h` | 1,230.00 USD | -765,130.00 USD | **`DISTRIBUTION`** |
| `6h` | 118,980.00 USD | -504,140.00 USD | **`DISTRIBUTION`** |
| `8h` | 219,850.00 USD | -89,660.00 USD | **`ACCUMULATION`** |
| `12h` | 244,040.00 USD | 201,240.00 USD | **`ACCUMULATION`** |
| `24h` | 122,540.00 USD | -1,900,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -68,630.00 USD | -9,820,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,520,000.00 USD | -78,900,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+654.32` | 15m=`+106.84K` | 1h=`+27.39K` | 24h=`+122.54K`
* Futures Capital Netflows: 5m=`-23.70K` | 15m=`+151.32K` | 1h=`-243.91K` | 24h=`-1.90M`
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
  * `2026-10-30 01:36:09 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:09 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:51:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
