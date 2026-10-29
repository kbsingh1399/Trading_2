# 🏛️ SOVEREIGN CANDIDATE DOSSIER: OP
**Canonical Key**: `OP` | **Broker Instrument**: `OPUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 02:15:30 IST` (`2026-10-29 20:45:30 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1082` | `0.1088` | `0.1061` | `0.1070` | `10,528,226` | 1,126,079.44 USD | -211,721.91 USD | `-18.80%` | -1,556,085.23 USD | `-2.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1070` | `0.1072` | `0.1056` | `0.1061` | `9,339,777` | 993,289.97 USD | -155,980.27 USD | `-15.70%` | -1,712,065.50 USD | `-1.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1061` | `0.1061` | `0.1013` | `0.1024` | `26,301,599` | 2,727,414.33 USD | -627,427.03 USD | `-23.00%` | -2,339,492.53 USD | `-3.50` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1101` | `0.1103` | `0.1070` | `0.1084` | `22,410,691` | 2,425,114.31 USD | -332,553.17 USD | `-13.71%` | -1,437,398.04 USD | `-3.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1084` | `0.1087` | `0.1080` | `0.1082` | `4,870,971` | 527,563.25 USD | 93,034.72 USD | `+17.63%` | -1,344,363.32 USD | `+1.14` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1082` | `0.1088` | `0.1013` | `0.1023` | `46,035,363` | 4,833,044.33 USD | -996,504.06 USD | `-20.62%` | -2,340,867.38 USD | `-3.97` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1112` | `0.1113` | `0.1094` | `0.1100` | `13,608,224` | 1,499,374.47 USD | -1,041.31 USD | `-0.07%` | -1,303,410.19 USD | `+0.26` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1100` | `0.1106` | `0.1096` | `0.1101` | `7,910,873` | 870,770.93 USD | 117,397.34 USD | `+13.48%` | -1,186,012.85 USD | `+0.73` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1101` | `0.1103` | `0.1013` | `0.1027` | `72,886,778` | 7,741,601.10 USD | -1,214,154.01 USD | `-15.68%` | -2,400,166.86 USD | `-3.17` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -935,828.18 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | -1,111,968.46 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.1013` | `0.1027` | `72,939,049` | 7,746,971.67 USD | -1,216,700.29 USD | `-15.71%` | -2,328,668.75 USD | `-1.15` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1085` | `0.1106` | `0.1071` | `0.1076` | `47,048,931` | 5,111,570.05 USD | 108,567.99 USD | `+2.12%` | -1,419,806.61 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1076` | `0.1111` | `0.1075` | `0.1099` | `45,357,664` | 4,969,550.08 USD | 142,722.83 USD | `+2.87%` | -1,277,083.78 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1099` | `0.1141` | `0.1093` | `0.1139` | `69,113,404` | 7,714,245.64 USD | 341,255.60 USD | `+4.42%` | -935,828.18 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1140` | `0.1148` | `0.1094` | `0.1101` | `61,838,594` | 6,908,457.75 USD | -176,140.28 USD | `-2.55%` | -1,111,968.46 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1101` | `0.1103` | `0.1013` | `0.1027` | `72,939,049` | 7,746,971.67 USD | -1,216,700.29 USD | `-15.71%` | -2,328,668.75 USD | `-1.15` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:14:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1132` | 7,914.80 USD | `-` | `NEWS_INTEL` | `-` | #OP Whale BUY: 7.91K USD at 0.1132 USD [API] | `2026-10-28 01:55:47` |


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
| `7D` | `Long Liquidation` | `0.0943` | 2,160,000.00 USD | 2,160,000.00 USD | 3,920.00 USD | 0.00 USD | 25.13 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0945` | 2,160,000.00 USD | 2,160,000.00 USD | 1,580.00 USD | 1,810.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0945` | 69,120.00 USD | 126,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0947` | 2,150,000.00 USD | 2,150,000.00 USD | 2,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0949` | 2,150,000.00 USD | 2,150,000.00 USD | 3,770.00 USD | 0.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0955` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 3.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0955` | 5,610.00 USD | 57,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0957` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 7.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0959` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 1,140.00 USD | 2.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0961` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 2.60 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0962` | 1,020,000.00 USD | 1,020,000.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0963` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0964` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 14.27 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0965` | 419.87 USD | 51,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0966` | 1,010,000.00 USD | 1,010,000.00 USD | 2,140.00 USD | 715.37 USD | 6,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0967` | 2,130,000.00 USD | 2,130,000.00 USD | 3,770.00 USD | 2,660.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0968` | 1,000,000.00 USD | 1,000,000.00 USD | 6,400.00 USD | 2,400.00 USD | 11,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0969` | 2,120,000.00 USD | 2,120,000.00 USD | 3,720.00 USD | 2,810.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0970` | 984,090.00 USD | 984,090.00 USD | 1,290.00 USD | 2,860.00 USD | 4,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0971` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 2,000.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0972` | 975,860.00 USD | 975,860.00 USD | 861.40 USD | 3,490.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0973` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 1,390.00 USD | 2,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0974` | 968,710.00 USD | 968,710.00 USD | 0.00 USD | 856.99 USD | 2,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0975` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 1,160.00 USD | 4,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0975` | 12,670.00 USD | 51,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0976` | 965,190.00 USD | 965,190.00 USD | 1,980.00 USD | 1,990.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0977` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 8,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0978` | 953,750.00 USD | 953,750.00 USD | 6,310.00 USD | 1,470.00 USD | 2,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0979` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 1,530.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0980` | 943,220.00 USD | 943,220.00 USD | 0.00 USD | 1,040.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0981` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 2,390.00 USD | 5,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0982` | 940,190.00 USD | 940,190.00 USD | 1,840.00 USD | 1,360.00 USD | 7,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0983` | 2,060,000.00 USD | 2,060,000.00 USD | 7,990.00 USD | 1,230.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0984` | 929,200.00 USD | 929,200.00 USD | 7,070.00 USD | 460.32 USD | 4,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0985` | 2,050,000.00 USD | 2,050,000.00 USD | 7,110.00 USD | 0.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0985` | 19,960.00 USD | 38,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0986` | 917,330.00 USD | 917,330.00 USD | 5,370.00 USD | 2,610.00 USD | 4,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0987` | 2,030,000.00 USD | 2,030,000.00 USD | 5,390.00 USD | 9,190.00 USD | 37,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0988` | 904,770.00 USD | 904,770.00 USD | 4,600.00 USD | 2,120.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0989` | 1,980,000.00 USD | 1,980,000.00 USD | 12,260.00 USD | 4,520.00 USD | 27,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0990` | 894,370.00 USD | 894,370.00 USD | 3,980.00 USD | 3,340.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0991` | 1,940,000.00 USD | 1,940,000.00 USD | 14,350.00 USD | 10,350.00 USD | 13,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0992` | 884,610.00 USD | 884,610.00 USD | 1,470.00 USD | 1,690.00 USD | 7,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0993` | 1,900,000.00 USD | 1,900,000.00 USD | 23,920.00 USD | 10,140.00 USD | 24,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0994` | 873,640.00 USD | 873,640.00 USD | 4,740.00 USD | 820.70 USD | 9,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0995` | 1,840,000.00 USD | 1,840,000.00 USD | 13,090.00 USD | 6,160.00 USD | 25,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0996` | 858,250.00 USD | 858,250.00 USD | 2,640.00 USD | 624.33 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0997` | 1,790,000.00 USD | 1,790,000.00 USD | 21,100.00 USD | 5,500.00 USD | 32,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0998` | 843,870.00 USD | 843,870.00 USD | 2,690.00 USD | 1,690.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0999` | 1,740,000.00 USD | 1,740,000.00 USD | 14,230.00 USD | 6,540.00 USD | 18,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1000` | 833,210.00 USD | 833,210.00 USD | 2,760.00 USD | 3,370.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1001` | 1,700,000.00 USD | 1,700,000.00 USD | 29,230.00 USD | 3,010.00 USD | 10,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1002` | 820,500.00 USD | 820,500.00 USD | 2,660.00 USD | 558.39 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1003` | 1,650,000.00 USD | 1,650,000.00 USD | 8,010.00 USD | 7,060.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1004` | 817,290.00 USD | 817,290.00 USD | 1,970.00 USD | 0.00 USD | 1,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1005` | 1,630,000.00 USD | 1,630,000.00 USD | 25,070.00 USD | 11,000.00 USD | 18,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1005` | 427.25 USD | 18,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1006` | 814,190.00 USD | 814,190.00 USD | 0.00 USD | 403.62 USD | 803.25 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1007` | 1,580,000.00 USD | 1,580,000.00 USD | 10,260.00 USD | 2,280.00 USD | 14,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1008` | 812,990.00 USD | 812,990.00 USD | 1,250.00 USD | 1,630.00 USD | 26.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1009` | 1,550,000.00 USD | 1,550,000.00 USD | 15,320.00 USD | 3,070.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1010` | 810,080.00 USD | 810,080.00 USD | 0.00 USD | 2,120.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1011` | 1,530,000.00 USD | 1,530,000.00 USD | 4,430.00 USD | 4,720.00 USD | 8,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1012` | 805,460.00 USD | 805,460.00 USD | 0.00 USD | 800.79 USD | 997.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1013` | 1,510,000.00 USD | 1,510,000.00 USD | 12,870.00 USD | 4,030.00 USD | 3,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1014` | 803,660.00 USD | 803,660.00 USD | 4,900.00 USD | 1,830.00 USD | 620.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1015` | 1,490,000.00 USD | 1,490,000.00 USD | 6,830.00 USD | 965.35 USD | 2,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1015` | 622.37 USD | 17,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1016` | 796,300.00 USD | 796,300.00 USD | 2,200.00 USD | 2,540.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1017` | 1,480,000.00 USD | 1,480,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1018` | 787,730.00 USD | 787,730.00 USD | 827.81 USD | 3,010.00 USD | 7,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1019` | 1,460,000.00 USD | 1,460,000.00 USD | 9,260.00 USD | 5,790.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1020` | 776,510.00 USD | 776,510.00 USD | 4,470.00 USD | 2,630.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1021` | 1,430,000.00 USD | 1,430,000.00 USD | 7,900.00 USD | 3,270.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1022` | 767,390.00 USD | 767,390.00 USD | 5,070.00 USD | 2,120.00 USD | 7,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1023` | 1,410,000.00 USD | 1,410,000.00 USD | 4,030.00 USD | 7,510.00 USD | 14,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1024` | 752,960.00 USD | 752,960.00 USD | 1,440.00 USD | 0.00 USD | 52.36 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1025` | 1,380,000.00 USD | 1,380,000.00 USD | 1,550.00 USD | 0.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1025` | 17,360.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1026` | 751,470.00 USD | 751,470.00 USD | 5,200.00 USD | 1,560.00 USD | 2,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1027` | 1,380,000.00 USD | 1,380,000.00 USD | 2,250.00 USD | 2,580.00 USD | 378.73 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1028` | 742,200.00 USD | 742,200.00 USD | 0.00 USD | 936.16 USD | 88.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1029` | 1,370,000.00 USD | 1,370,000.00 USD | 7,420.00 USD | 3,000.00 USD | 395.35 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1030` | 741,170.00 USD | 741,170.00 USD | 7,910.00 USD | 1,790.00 USD | 17,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1031` | 1,360,000.00 USD | 1,360,000.00 USD | 13,690.00 USD | 5,070.00 USD | 10,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1032` | 714,160.00 USD | 714,160.00 USD | 15,980.00 USD | 4,190.00 USD | 20,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1033` | 1,330,000.00 USD | 1,330,000.00 USD | 13,180.00 USD | 2,640.00 USD | 26,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1034` | 673,340.00 USD | 673,340.00 USD | 10,250.00 USD | 5,320.00 USD | 11,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1035` | 1,290,000.00 USD | 1,290,000.00 USD | 8,450.00 USD | 9,400.00 USD | 15,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1036` | 646,720.00 USD | 646,720.00 USD | 6,930.00 USD | 8,750.00 USD | 14,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1037` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 31,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1038` | 616,520.00 USD | 616,520.00 USD | 5,960.00 USD | 9,420.00 USD | 12,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1039` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 7,400.00 USD | 95.01 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1040` | 588,440.00 USD | 588,440.00 USD | 3,380.00 USD | 6,970.00 USD | 18,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1041` | 1,220,000.00 USD | 1,220,000.00 USD | 5,940.00 USD | 2,910.00 USD | 18,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1042` | 559,970.00 USD | 559,970.00 USD | 24,800.00 USD | 5,430.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1043` | 1,190,000.00 USD | 1,190,000.00 USD | 15,960.00 USD | 5,980.00 USD | 21,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1044` | 517,140.00 USD | 517,140.00 USD | 917.34 USD | 6,870.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1045` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 14,850.00 USD | 14,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1046` | 508,040.00 USD | 508,040.00 USD | 0.00 USD | 1,080.00 USD | 8,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1047` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 1,720.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1048` | 498,280.00 USD | 498,280.00 USD | 18,520.00 USD | 3,890.00 USD | 24,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1049` | 1,090,000.00 USD | 1,090,000.00 USD | 34,790.00 USD | 4,810.00 USD | 35,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1050` | 451,670.00 USD | 451,670.00 USD | 19,000.00 USD | 2,470.00 USD | 10,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1051` | 1,020,000.00 USD | 1,020,000.00 USD | 17,290.00 USD | 11,500.00 USD | 48,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1052` | 419,480.00 USD | 419,480.00 USD | 29,880.00 USD | 11,260.00 USD | 47,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1053` | 939,270.00 USD | 939,270.00 USD | 53,590.00 USD | 29,800.00 USD | 95,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1054` | 331,030.00 USD | 331,030.00 USD | 59,720.00 USD | 20,100.00 USD | 72,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1055` | 760,350.00 USD | 760,350.00 USD | 80,160.00 USD | 27,290.00 USD | 148,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1056` | 179,030.00 USD | 179,030.00 USD | 22,250.00 USD | 25,020.00 USD | 44,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1057` | 504,680.00 USD | 504,680.00 USD | 50,380.00 USD | 31,940.00 USD | 97,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1058` | 87,680.00 USD | 87,680.00 USD | 13,830.00 USD | 29,860.00 USD | 43,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1059` | 324,880.00 USD | 324,880.00 USD | 92,510.00 USD | 0.00 USD | 117,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1060` | 91,400.00 USD | 91,400.00 USD | 29,020.00 USD | 14,170.00 USD | 48,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1061` | 114,610.00 USD | 114,610.00 USD | 38,260.00 USD | 0.00 USD | 76,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1062` | 166,640.00 USD | 166,640.00 USD | 3,440.00 USD | 15,960.00 USD | 55,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1063` | 164,810.00 USD | 164,810.00 USD | 0.00 USD | 0.00 USD | 164,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1063` | 329,610.00 USD | 329,610.00 USD | 0.00 USD | 0.00 USD | 164,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1064` | 227,640.00 USD | 227,640.00 USD | 0.00 USD | 16,060.00 USD | 44,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1065` | 422,660.00 USD | 422,660.00 USD | 0.00 USD | 0.00 USD | 93,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1066` | 257,170.00 USD | 257,170.00 USD | 0.00 USD | 12,550.00 USD | 16,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1067` | 490,590.00 USD | 490,590.00 USD | 0.00 USD | 0.00 USD | 67,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1068` | 294,440.00 USD | 294,440.00 USD | 0.00 USD | 9,500.00 USD | 27,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1069` | 562,620.00 USD | 562,620.00 USD | 0.00 USD | 0.00 USD | 72,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1070` | 353,690.00 USD | 353,690.00 USD | 0.00 USD | 7,790.00 USD | 51,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1071` | 605,260.00 USD | 605,260.00 USD | 0.00 USD | 0.00 USD | 42,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1072` | 353,710.00 USD | 353,710.00 USD | 0.00 USD | 0.00 USD | 15.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1073` | 623,000.00 USD | 623,000.00 USD | 0.00 USD | 17,700.00 USD | 31.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1074` | 353,750.00 USD | 353,750.00 USD | 0.00 USD | 0.00 USD | 42.35 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1076` | 353,820.00 USD | 353,820.00 USD | 0.00 USD | 0.00 USD | 67.62 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1078` | 353,870.00 USD | 353,870.00 USD | 0.00 USD | 0.00 USD | 52.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1081` | 623,030.00 USD | 623,030.00 USD | 0.00 USD | 0.00 USD | 29.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1082` | 353,890.00 USD | 353,890.00 USD | 0.00 USD | 0.00 USD | 21.66 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1084` | 382,590.00 USD | 382,590.00 USD | 0.00 USD | 0.00 USD | 28,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1086` | 455,520.00 USD | 455,520.00 USD | 0.00 USD | 0.00 USD | 72,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1087` | 628,070.00 USD | 628,070.00 USD | 0.00 USD | 5,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1088` | 507,810.00 USD | 507,810.00 USD | 44,230.00 USD | 0.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1089` | 633,360.00 USD | 633,360.00 USD | 5,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1090` | 554,920.00 USD | 554,920.00 USD | 47,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1091` | 658,680.00 USD | 658,680.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1092` | 565,210.00 USD | 565,210.00 USD | 10,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1093` | 667,420.00 USD | 667,420.00 USD | 0.00 USD | 0.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1094` | 592,160.00 USD | 592,160.00 USD | 13,100.00 USD | 0.00 USD | 13,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1095` | 667,600.00 USD | 667,600.00 USD | 0.00 USD | 0.00 USD | 181.59 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1096` | 605,830.00 USD | 605,830.00 USD | 4,110.00 USD | 1,890.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1097` | 686,210.00 USD | 686,210.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1098` | 645,910.00 USD | 645,910.00 USD | 13,380.00 USD | 3,910.00 USD | 22,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1099` | 719,510.00 USD | 719,510.00 USD | 11,470.00 USD | 0.00 USD | 21,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1100` | 653,020.00 USD | 653,020.00 USD | 0.00 USD | 2,820.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1101` | 742,720.00 USD | 742,720.00 USD | 0.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1102` | 657,320.00 USD | 657,320.00 USD | 4,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1103` | 760,210.00 USD | 760,210.00 USD | 17,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1104` | 671,670.00 USD | 671,670.00 USD | 6,920.00 USD | 7,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1105` | 774,690.00 USD | 774,690.00 USD | 0.00 USD | 14,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1106` | 715,210.00 USD | 715,210.00 USD | 0.00 USD | 12,720.00 USD | 30,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1107` | 803,160.00 USD | 803,160.00 USD | 0.00 USD | 12,510.00 USD | 15,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1108` | 733,940.00 USD | 733,940.00 USD | 3,110.00 USD | 0.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1109` | 818,110.00 USD | 818,110.00 USD | 0.00 USD | 14,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1111` | 830,060.00 USD | 830,060.00 USD | 0.00 USD | 11,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1112` | 739,140.00 USD | 739,140.00 USD | 5,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1114` | 799,230.00 USD | 799,230.00 USD | 15,810.00 USD | 5,210.00 USD | 39,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1116` | 823,000.00 USD | 823,000.00 USD | 4,760.00 USD | 12,080.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1117` | 869,330.00 USD | 869,330.00 USD | 0.00 USD | 22,780.00 USD | 16,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1118` | 928,900.00 USD | 928,900.00 USD | 29,340.00 USD | 19,550.00 USD | 57,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1119` | 932,650.00 USD | 932,650.00 USD | 34,550.00 USD | 7,050.00 USD | 21,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1120` | 967,790.00 USD | 967,790.00 USD | 20,510.00 USD | 8,540.00 USD | 9,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1121` | 959,560.00 USD | 959,560.00 USD | 5,730.00 USD | 0.00 USD | 21,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1122` | 1,000,000.00 USD | 1,000,000.00 USD | 18,850.00 USD | 4,480.00 USD | 12,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1123` | 1,030,000.00 USD | 1,030,000.00 USD | 12,360.00 USD | 23,980.00 USD | 37,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1124` | 1,030,000.00 USD | 1,030,000.00 USD | 19,640.00 USD | 5,620.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1125` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 2,230.00 USD | 36,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1126` | 1,070,000.00 USD | 1,070,000.00 USD | 9,370.00 USD | 10,660.00 USD | 16,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1127` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1128` | 1,090,000.00 USD | 1,090,000.00 USD | 8,710.00 USD | 0.00 USD | 7,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1129` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 65.26 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1130` | 1,100,000.00 USD | 1,100,000.00 USD | 7,970.00 USD | 1,490.00 USD | 5,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1131` | 1,110,000.00 USD | 1,110,000.00 USD | 12,540.00 USD | 0.00 USD | 15,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1132` | 1,150,000.00 USD | 1,150,000.00 USD | 16,120.00 USD | 17,300.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1133` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 11,430.00 USD | 110.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1134` | 1,180,000.00 USD | 1,180,000.00 USD | 4,040.00 USD | 12,980.00 USD | 13,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1135` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1136` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 787.70 USD | 4,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1138` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 856.93 USD | 14,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1140` | 1,220,000.00 USD | 1,220,000.00 USD | 7,800.00 USD | 0.00 USD | 6,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1141` | 1,150,000.00 USD | 1,150,000.00 USD | 10,380.00 USD | 0.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1142` | 1,270,000.00 USD | 1,270,000.00 USD | 24,760.00 USD | 17,100.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1143` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 78,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1144` | 1,340,000.00 USD | 1,340,000.00 USD | 9,940.00 USD | 21,970.00 USD | 31,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1145` | 1,390,000.00 USD | 1,390,000.00 USD | 16,540.00 USD | 2,730.00 USD | 141,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1146` | 1,380,000.00 USD | 1,380,000.00 USD | 5,090.00 USD | 10,830.00 USD | 30,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1147` | 1,540,000.00 USD | 1,540,000.00 USD | 9,880.00 USD | 0.00 USD | 138,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1148` | 1,450,000.00 USD | 1,450,000.00 USD | 33,430.00 USD | 3,280.00 USD | 30,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1149` | 1,620,000.00 USD | 1,620,000.00 USD | 10,560.00 USD | 0.00 USD | 72,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1150` | 1,510,000.00 USD | 1,510,000.00 USD | 19,260.00 USD | 13,020.00 USD | 21,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1151` | 1,850,000.00 USD | 1,850,000.00 USD | 92,570.00 USD | 4,210.00 USD | 128,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1152` | 1,620,000.00 USD | 1,620,000.00 USD | 34,520.00 USD | 17,470.00 USD | 59,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1153` | 2,150,000.00 USD | 2,150,000.00 USD | 153,720.00 USD | 8,400.00 USD | 139,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1154` | 1,710,000.00 USD | 1,710,000.00 USD | 18,600.00 USD | 23,230.00 USD | 54,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1155` | 2,440,000.00 USD | 2,440,000.00 USD | 149,360.00 USD | 40,110.00 USD | 105,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1156` | 1,810,000.00 USD | 1,810,000.00 USD | 48,760.00 USD | 21,470.00 USD | 24,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1157` | 2,630,000.00 USD | 2,630,000.00 USD | 133,960.00 USD | 3,760.00 USD | 48,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1158` | 1,890,000.00 USD | 1,890,000.00 USD | 26,730.00 USD | 9,500.00 USD | 41,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1159` | 2,780,000.00 USD | 2,780,000.00 USD | 81,080.00 USD | 12,710.00 USD | 53,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1160` | 1,930,000.00 USD | 1,930,000.00 USD | 34,710.00 USD | 4,660.00 USD | 8,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1161` | 3,060,000.00 USD | 3,060,000.00 USD | 146,810.00 USD | 37,250.00 USD | 100,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1162` | 1,960,000.00 USD | 1,960,000.00 USD | 9,050.00 USD | 8,790.00 USD | 8,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1163` | 3,200,000.00 USD | 3,200,000.00 USD | 53,510.00 USD | 11,460.00 USD | 68,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1164` | 1,990,000.00 USD | 1,990,000.00 USD | 3,830.00 USD | 8,020.00 USD | 18,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1165` | 3,330,000.00 USD | 3,330,000.00 USD | 68,620.00 USD | 35,720.00 USD | 27,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1166` | 2,010,000.00 USD | 2,010,000.00 USD | 10,670.00 USD | 8,850.00 USD | 40.24 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1167` | 3,470,000.00 USD | 3,470,000.00 USD | 79,610.00 USD | 21,620.00 USD | 41,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1168` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 1,880.00 USD | 8,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1169` | 3,640,000.00 USD | 3,640,000.00 USD | 65,340.00 USD | 14,840.00 USD | 86,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1170` | 2,040,000.00 USD | 2,040,000.00 USD | 14,800.00 USD | 2,000.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1171` | 3,740,000.00 USD | 3,740,000.00 USD | 57,350.00 USD | 11,370.00 USD | 35,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1172` | 2,060,000.00 USD | 2,060,000.00 USD | 10,950.00 USD | 5,440.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1173` | 3,830,000.00 USD | 3,830,000.00 USD | 40,860.00 USD | 9,190.00 USD | 36,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1174` | 2,090,000.00 USD | 2,090,000.00 USD | 10,300.00 USD | 6,360.00 USD | 15,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1175` | 3,940,000.00 USD | 3,940,000.00 USD | 38,840.00 USD | 12,300.00 USD | 58,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1176` | 2,130,000.00 USD | 2,130,000.00 USD | 4,150.00 USD | 7,940.00 USD | 20,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1177` | 4,030,000.00 USD | 4,030,000.00 USD | 33,330.00 USD | 20,350.00 USD | 43,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1178` | 2,160,000.00 USD | 2,160,000.00 USD | 16,140.00 USD | 7,760.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1179` | 4,140,000.00 USD | 4,140,000.00 USD | 66,670.00 USD | 10,940.00 USD | 23,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1180` | 2,200,000.00 USD | 2,200,000.00 USD | 15,510.00 USD | 4,770.00 USD | 27,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1181` | 4,190,000.00 USD | 4,190,000.00 USD | 22,290.00 USD | 15,780.00 USD | 17,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1182` | 2,230,000.00 USD | 2,230,000.00 USD | 15,890.00 USD | 3,000.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1183` | 4,240,000.00 USD | 4,240,000.00 USD | 7,760.00 USD | 1,800.00 USD | 39,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1184` | 2,250,000.00 USD | 2,250,000.00 USD | 6,980.00 USD | 1,730.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1185` | 4,280,000.00 USD | 4,280,000.00 USD | 3,880.00 USD | 5,130.00 USD | 26,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1186` | 2,270,000.00 USD | 2,270,000.00 USD | 3,430.00 USD | 6,750.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1187` | 4,330,000.00 USD | 4,330,000.00 USD | 5,620.00 USD | 15,370.00 USD | 36,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1188` | 2,280,000.00 USD | 2,280,000.00 USD | 2,780.00 USD | 6,670.00 USD | 4,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1189` | 4,380,000.00 USD | 4,380,000.00 USD | 27,240.00 USD | 15,060.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1190` | 2,290,000.00 USD | 2,290,000.00 USD | 2,840.00 USD | 856.99 USD | 2,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1191` | 4,530,000.00 USD | 4,530,000.00 USD | 22,650.00 USD | 15,330.00 USD | 109,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1192` | 2,300,000.00 USD | 2,300,000.00 USD | 4,720.00 USD | 1,990.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1193` | 4,560,000.00 USD | 4,560,000.00 USD | 21,260.00 USD | 0.00 USD | 12,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1194` | 2,310,000.00 USD | 2,310,000.00 USD | 6,310.00 USD | 347.94 USD | 2,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1195` | 4,600,000.00 USD | 4,600,000.00 USD | 11,190.00 USD | 1,780.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1196` | 2,320,000.00 USD | 2,320,000.00 USD | 3,240.00 USD | 1,120.00 USD | 100.88 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1197` | 4,640,000.00 USD | 4,640,000.00 USD | 6,780.00 USD | 10,800.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1198` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 1,040.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1199` | 4,710,000.00 USD | 4,710,000.00 USD | 9,100.00 USD | 2,390.00 USD | 64,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1200` | 2,330,000.00 USD | 2,330,000.00 USD | 1,840.00 USD | 1,360.00 USD | 7,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1201` | 4,870,000.00 USD | 4,870,000.00 USD | 114,140.00 USD | 16,380.00 USD | 29,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1202` | 2,340,000.00 USD | 2,340,000.00 USD | 7,070.00 USD | 460.32 USD | 4,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1203` | 4,980,000.00 USD | 4,980,000.00 USD | 70,770.00 USD | 29,250.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1204` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 413.94 USD | 1,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1205` | 5,240,000.00 USD | 5,240,000.00 USD | 86,480.00 USD | 48,720.00 USD | 128,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1206` | 2,360,000.00 USD | 2,360,000.00 USD | 5,370.00 USD | 2,190.00 USD | 3,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1207` | 5,330,000.00 USD | 5,330,000.00 USD | 12,460.00 USD | 19,400.00 USD | 53,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1208` | 2,370,000.00 USD | 2,370,000.00 USD | 4,600.00 USD | 2,120.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1209` | 5,530,000.00 USD | 5,530,000.00 USD | 85,160.00 USD | 19,340.00 USD | 94,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1210` | 2,380,000.00 USD | 2,380,000.00 USD | 3,980.00 USD | 3,340.00 USD | 2,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1211` | 5,580,000.00 USD | 5,580,000.00 USD | 14,350.00 USD | 12,900.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1212` | 2,390,000.00 USD | 2,390,000.00 USD | 1,470.00 USD | 1,690.00 USD | 7,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1213` | 5,640,000.00 USD | 5,640,000.00 USD | 23,920.00 USD | 12,800.00 USD | 24,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1214` | 2,400,000.00 USD | 2,400,000.00 USD | 4,740.00 USD | 820.70 USD | 9,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1215` | 5,710,000.00 USD | 5,710,000.00 USD | 5,900.00 USD | 6,620.00 USD | 59,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1216` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1217` | 5,750,000.00 USD | 5,750,000.00 USD | 18,490.00 USD | 6,160.00 USD | 11,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1218` | 2,420,000.00 USD | 2,420,000.00 USD | 2,640.00 USD | 624.33 USD | 8,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1219` | 5,820,000.00 USD | 5,820,000.00 USD | 26,700.00 USD | 5,500.00 USD | 38,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1220` | 2,430,000.00 USD | 2,430,000.00 USD | 2,690.00 USD | 1,690.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1221` | 5,880,000.00 USD | 5,880,000.00 USD | 25,890.00 USD | 15,750.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1222` | 2,440,000.00 USD | 2,440,000.00 USD | 2,760.00 USD | 3,370.00 USD | 6,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1223` | 6,030,000.00 USD | 6,030,000.00 USD | 70,040.00 USD | 25,830.00 USD | 48,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1225` | 6,090,000.00 USD | 6,090,000.00 USD | 43,040.00 USD | 19,970.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1225` | 16,560.00 USD | 16,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1227` | 6,220,000.00 USD | 6,220,000.00 USD | 49,930.00 USD | 23,840.00 USD | 50,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1229` | 6,350,000.00 USD | 6,350,000.00 USD | 63,350.00 USD | 30,490.00 USD | 40,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1231` | 6,430,000.00 USD | 6,430,000.00 USD | 21,280.00 USD | 29,380.00 USD | 27,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1233` | 6,540,000.00 USD | 6,540,000.00 USD | 57,130.00 USD | 13,020.00 USD | 40,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1235` | 6,560,000.00 USD | 6,560,000.00 USD | 4,430.00 USD | 4,720.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1237` | 6,570,000.00 USD | 6,570,000.00 USD | 4,080.00 USD | 2,760.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1239` | 6,580,000.00 USD | 6,580,000.00 USD | 8,780.00 USD | 1,270.00 USD | 479.13 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1241` | 6,590,000.00 USD | 6,590,000.00 USD | 6,830.00 USD | 965.35 USD | 2,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1243` | 6,610,000.00 USD | 6,610,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1245` | 6,650,000.00 USD | 6,650,000.00 USD | 15,080.00 USD | 8,080.00 USD | 12,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1247` | 6,680,000.00 USD | 6,680,000.00 USD | 7,900.00 USD | 13,800.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1249` | 6,700,000.00 USD | 6,700,000.00 USD | 13,440.00 USD | 5,480.00 USD | 5,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1251` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 1,800.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1253` | 6,740,000.00 USD | 6,740,000.00 USD | 11,420.00 USD | 2,100.00 USD | 14,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1255` | 6,760,000.00 USD | 6,760,000.00 USD | 2,250.00 USD | 13,990.00 USD | 33.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1257` | 6,780,000.00 USD | 6,780,000.00 USD | 15,610.00 USD | 5,200.00 USD | 54.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1259` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 288.60 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1261` | 6,790,000.00 USD | 6,790,000.00 USD | 4,270.00 USD | 0.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1263` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 0.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1265` | 6,800,000.00 USD | 6,800,000.00 USD | 2,710.00 USD | 0.00 USD | 3,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1267` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 0.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1269` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 0.00 USD | 16.21 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1271` | 6,800,000.00 USD | 6,800,000.00 USD | 5,940.00 USD | 0.00 USD | 15.40 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1273` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 0.00 USD | 10.64 USD | `Tier 1 CEX` |
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
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0943` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 3,920.00 USD | 0.00 USD | 25.13 USD |
| `7D` | `0.0945` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 1,580.00 USD | 1,810.00 USD | 7,510.00 USD |
| `7D` | `0.0947` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 2,200.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0949` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 3,770.00 USD | 0.00 USD | 6,660.00 USD |
| `7D` | `0.0955` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 3.61 USD |
| `7D` | `0.0957` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 7.93 USD |
| `7D` | `0.0959` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 0.00 USD | 1,140.00 USD | 2.73 USD |
| `7D` | `0.0961` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 2.60 USD |
| `1D` | `0.0962` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 2,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0963` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 1,220.00 USD |
| `1D` | `0.0964` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 14.27 USD |
| `1D` | `0.0966` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 2,140.00 USD | 715.37 USD | 6,180.00 USD |
| `7D` | `0.0967` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 3,770.00 USD | 2,660.00 USD | 2,830.00 USD |
| `1D` | `0.0968` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 6,400.00 USD | 2,400.00 USD | 11,270.00 USD |
| `7D` | `0.0969` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 3,720.00 USD | 2,810.00 USD | 13,790.00 USD |
| `1D` | `0.0970` | 984,090.00 USD | 0.00 USD | 984,090.00 USD | 1,290.00 USD | 2,860.00 USD | 4,090.00 USD |
| `7D` | `0.0971` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 0.00 USD | 2,000.00 USD | 4,690.00 USD |
| `1D` | `0.0972` | 975,860.00 USD | 0.00 USD | 975,860.00 USD | 861.40 USD | 3,490.00 USD | 2,800.00 USD |
| `7D` | `0.0973` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 0.00 USD | 1,390.00 USD | 2,860.00 USD |
| `1D` | `0.0974` | 968,710.00 USD | 0.00 USD | 968,710.00 USD | 0.00 USD | 856.99 USD | 2,660.00 USD |
| `7D` | `0.0975` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 0.00 USD | 1,160.00 USD | 4,160.00 USD |
| `1D` | `0.0976` | 965,190.00 USD | 0.00 USD | 965,190.00 USD | 1,980.00 USD | 1,990.00 USD | 7,460.00 USD |
| `7D` | `0.0977` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 8,960.00 USD |
| `1D` | `0.0978` | 953,750.00 USD | 0.00 USD | 953,750.00 USD | 6,310.00 USD | 1,470.00 USD | 2,750.00 USD |
| `7D` | `0.0979` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 0.00 USD | 1,530.00 USD | 5,710.00 USD |
| `1D` | `0.0980` | 943,220.00 USD | 0.00 USD | 943,220.00 USD | 0.00 USD | 1,040.00 USD | 1,990.00 USD |
| `7D` | `0.0981` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 0.00 USD | 2,390.00 USD | 5,910.00 USD |
| `1D` | `0.0982` | 940,190.00 USD | 0.00 USD | 940,190.00 USD | 1,840.00 USD | 1,360.00 USD | 7,790.00 USD |
| `7D` | `0.0983` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 7,990.00 USD | 1,230.00 USD | 8,890.00 USD |
| `1D` | `0.0984` | 929,200.00 USD | 0.00 USD | 929,200.00 USD | 7,070.00 USD | 460.32 USD | 4,340.00 USD |
| `7D` | `0.0985` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 7,110.00 USD | 0.00 USD | 6,320.00 USD |
| `1D` | `0.0986` | 917,330.00 USD | 0.00 USD | 917,330.00 USD | 5,370.00 USD | 2,610.00 USD | 4,580.00 USD |
| `7D` | `0.0987` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 5,390.00 USD | 9,190.00 USD | 37,300.00 USD |
| `1D` | `0.0988` | 904,770.00 USD | 0.00 USD | 904,770.00 USD | 4,600.00 USD | 2,120.00 USD | 3,680.00 USD |
| `7D` | `0.0989` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 12,260.00 USD | 4,520.00 USD | 27,250.00 USD |
| `1D` | `0.0990` | 894,370.00 USD | 0.00 USD | 894,370.00 USD | 3,980.00 USD | 3,340.00 USD | 2,450.00 USD |
| `7D` | `0.0991` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 14,350.00 USD | 10,350.00 USD | 13,620.00 USD |
| `1D` | `0.0992` | 884,610.00 USD | 0.00 USD | 884,610.00 USD | 1,470.00 USD | 1,690.00 USD | 7,820.00 USD |
| `7D` | `0.0993` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 23,920.00 USD | 10,140.00 USD | 24,070.00 USD |
| `1D` | `0.0994` | 873,640.00 USD | 0.00 USD | 873,640.00 USD | 4,740.00 USD | 820.70 USD | 9,830.00 USD |
| `7D` | `0.0995` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 13,090.00 USD | 6,160.00 USD | 25,320.00 USD |
| `1D` | `0.0996` | 858,250.00 USD | 0.00 USD | 858,250.00 USD | 2,640.00 USD | 624.33 USD | 11,120.00 USD |
| `7D` | `0.0997` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 21,100.00 USD | 5,500.00 USD | 32,910.00 USD |
| `1D` | `0.0998` | 843,870.00 USD | 0.00 USD | 843,870.00 USD | 2,690.00 USD | 1,690.00 USD | 6,280.00 USD |
| `7D` | `0.0999` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 14,230.00 USD | 6,540.00 USD | 18,750.00 USD |
| `1D` | `0.1000` | 833,210.00 USD | 0.00 USD | 833,210.00 USD | 2,760.00 USD | 3,370.00 USD | 6,570.00 USD |
| `7D` | `0.1001` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 29,230.00 USD | 3,010.00 USD | 10,890.00 USD |
| `1D` | `0.1002` | 820,500.00 USD | 0.00 USD | 820,500.00 USD | 2,660.00 USD | 558.39 USD | 0.00 USD |
| `7D` | `0.1003` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 8,010.00 USD | 7,060.00 USD | 5,300.00 USD |
| `1D` | `0.1004` | 817,290.00 USD | 0.00 USD | 817,290.00 USD | 1,970.00 USD | 0.00 USD | 1,130.00 USD |
| `7D` | `0.1005` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 25,070.00 USD | 11,000.00 USD | 18,490.00 USD |
| `1D` | `0.1006` | 814,190.00 USD | 0.00 USD | 814,190.00 USD | 0.00 USD | 403.62 USD | 803.25 USD |
| `7D` | `0.1007` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 10,260.00 USD | 2,280.00 USD | 14,140.00 USD |
| `1D` | `0.1008` | 812,990.00 USD | 0.00 USD | 812,990.00 USD | 1,250.00 USD | 1,630.00 USD | 26.69 USD |
| `7D` | `0.1009` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 15,320.00 USD | 3,070.00 USD | 6,750.00 USD |
| `1D` | `0.1010` | 810,080.00 USD | 0.00 USD | 810,080.00 USD | 0.00 USD | 2,120.00 USD | 2,500.00 USD |
| `7D` | `0.1011` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 4,430.00 USD | 4,720.00 USD | 8,990.00 USD |
| `1D` | `0.1012` | 805,460.00 USD | 0.00 USD | 805,460.00 USD | 0.00 USD | 800.79 USD | 997.22 USD |
| `7D` | `0.1013` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 12,870.00 USD | 4,030.00 USD | 3,110.00 USD |
| `1D` | `0.1014` | 803,660.00 USD | 0.00 USD | 803,660.00 USD | 4,900.00 USD | 1,830.00 USD | 620.20 USD |
| `7D` | `0.1015` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 6,830.00 USD | 965.35 USD | 2,450.00 USD |
| `1D` | `0.1016` | 796,300.00 USD | 0.00 USD | 796,300.00 USD | 2,200.00 USD | 2,540.00 USD | 3,830.00 USD |
| `7D` | `0.1017` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 11,450.00 USD | 4,530.00 USD | 4,730.00 USD |
| `1D` | `0.1018` | 787,730.00 USD | 0.00 USD | 787,730.00 USD | 827.81 USD | 3,010.00 USD | 7,380.00 USD |
| `7D` | `0.1019` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 9,260.00 USD | 5,790.00 USD | 13,110.00 USD |
| `1D` | `0.1020` | 776,510.00 USD | 0.00 USD | 776,510.00 USD | 4,470.00 USD | 2,630.00 USD | 2,020.00 USD |
| `7D` | `0.1021` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 7,900.00 USD | 3,270.00 USD | 7,150.00 USD |
| `1D` | `0.1022` | 767,390.00 USD | 0.00 USD | 767,390.00 USD | 5,070.00 USD | 2,120.00 USD | 7,230.00 USD |
| `7D` | `0.1023` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 4,030.00 USD | 7,510.00 USD | 14,550.00 USD |
| `1D` | `0.1024` | 752,960.00 USD | 0.00 USD | 752,960.00 USD | 1,440.00 USD | 0.00 USD | 52.36 USD |
| `7D` | `0.1025` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 1,550.00 USD | 0.00 USD | 5,780.00 USD |
| `1D` | `0.1026` | 751,470.00 USD | 0.00 USD | 751,470.00 USD | 5,200.00 USD | 1,560.00 USD | 2,520.00 USD |
| `7D` | `0.1027` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 2,250.00 USD | 2,580.00 USD | 378.73 USD |
| `1D` | `0.1028` | 742,200.00 USD | 0.00 USD | 742,200.00 USD | 0.00 USD | 936.16 USD | 88.60 USD |
| `7D` | `0.1029` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 7,420.00 USD | 3,000.00 USD | 395.35 USD |
| `1D` | `0.1030` | 741,170.00 USD | 0.00 USD | 741,170.00 USD | 7,910.00 USD | 1,790.00 USD | 17,320.00 USD |
| `7D` | `0.1031` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 13,690.00 USD | 5,070.00 USD | 10,810.00 USD |
| `1D` | `0.1032` | 714,160.00 USD | 0.00 USD | 714,160.00 USD | 15,980.00 USD | 4,190.00 USD | 20,650.00 USD |
| `7D` | `0.1033` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 13,180.00 USD | 2,640.00 USD | 26,150.00 USD |
| `1D` | `0.1034` | 673,340.00 USD | 0.00 USD | 673,340.00 USD | 10,250.00 USD | 5,320.00 USD | 11,050.00 USD |
| `7D` | `0.1035` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 8,450.00 USD | 9,400.00 USD | 15,870.00 USD |
| `1D` | `0.1036` | 646,720.00 USD | 0.00 USD | 646,720.00 USD | 6,930.00 USD | 8,750.00 USD | 14,510.00 USD |
| `7D` | `0.1037` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 31,130.00 USD |
| `1D` | `0.1038` | 616,520.00 USD | 0.00 USD | 616,520.00 USD | 5,960.00 USD | 9,420.00 USD | 12,700.00 USD |
| `7D` | `0.1039` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 0.00 USD | 7,400.00 USD | 95.01 USD |
| `1D` | `0.1040` | 588,440.00 USD | 0.00 USD | 588,440.00 USD | 3,380.00 USD | 6,970.00 USD | 18,120.00 USD |
| `7D` | `0.1041` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 5,940.00 USD | 2,910.00 USD | 18,680.00 USD |
| `1D` | `0.1042` | 559,970.00 USD | 0.00 USD | 559,970.00 USD | 24,800.00 USD | 5,430.00 USD | 12,600.00 USD |
| `7D` | `0.1043` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 15,960.00 USD | 5,980.00 USD | 21,040.00 USD |
| `1D` | `0.1044` | 517,140.00 USD | 0.00 USD | 517,140.00 USD | 917.34 USD | 6,870.00 USD | 1,320.00 USD |
| `7D` | `0.1045` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 0.00 USD | 14,850.00 USD | 14,910.00 USD |
| `1D` | `0.1046` | 508,040.00 USD | 0.00 USD | 508,040.00 USD | 0.00 USD | 1,080.00 USD | 8,670.00 USD |
| `7D` | `0.1047` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 1,720.00 USD | 23,040.00 USD |
| `1D` | `0.1048` | 498,280.00 USD | 0.00 USD | 498,280.00 USD | 18,520.00 USD | 3,890.00 USD | 24,200.00 USD |
| `7D` | `0.1049` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 34,790.00 USD | 4,810.00 USD | 35,460.00 USD |
| `1D` | `0.1050` | 451,670.00 USD | 0.00 USD | 451,670.00 USD | 19,000.00 USD | 2,470.00 USD | 10,720.00 USD |
| `7D` | `0.1051` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 17,290.00 USD | 11,500.00 USD | 48,850.00 USD |
| `1D` | `0.1052` | 419,480.00 USD | 0.00 USD | 419,480.00 USD | 29,880.00 USD | 11,260.00 USD | 47,310.00 USD |
| `7D` | `0.1053` | 939,270.00 USD | 0.00 USD | 939,270.00 USD | 53,590.00 USD | 29,800.00 USD | 95,520.00 USD |
| `1D` | `0.1054` | 331,030.00 USD | 0.00 USD | 331,030.00 USD | 59,720.00 USD | 20,100.00 USD | 72,180.00 USD |
| `7D` | `0.1055` | 760,350.00 USD | 0.00 USD | 760,350.00 USD | 80,160.00 USD | 27,290.00 USD | 148,220.00 USD |
| `1D` | `0.1056` | 179,030.00 USD | 0.00 USD | 179,030.00 USD | 22,250.00 USD | 25,020.00 USD | 44,080.00 USD |
| `7D` | `0.1057` | 504,680.00 USD | 0.00 USD | 504,680.00 USD | 50,380.00 USD | 31,940.00 USD | 97,490.00 USD |
| `1D` | `0.1058` | 87,680.00 USD | 0.00 USD | 87,680.00 USD | 13,830.00 USD | 29,860.00 USD | 43,990.00 USD |
| `1D` | `0.1059` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1059` | 324,880.00 USD | 0.00 USD | 324,880.00 USD | 92,510.00 USD | 0.00 USD | 117,750.00 USD |
| `1D` | `0.1060` | 91,400.00 USD | 91,400.00 USD | 0.00 USD | 29,020.00 USD | 14,170.00 USD | 48,210.00 USD |
| `7D` | `0.1061` | 114,610.00 USD | 0.00 USD | 114,610.00 USD | 38,260.00 USD | 0.00 USD | 76,350.00 USD |
| `1D` | `0.1062` | 166,640.00 USD | 166,640.00 USD | 0.00 USD | 3,440.00 USD | 15,960.00 USD | 55,830.00 USD |
| `7D` | `0.1063` | 164,810.00 USD | 164,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 164,810.00 USD |
| `7D` | `0.1063` | 329,610.00 USD | 329,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 164,810.00 USD |
| `1D` | `0.1064` | 227,640.00 USD | 227,640.00 USD | 0.00 USD | 0.00 USD | 16,060.00 USD | 44,950.00 USD |
| `7D` | `0.1065` | 422,660.00 USD | 422,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 93,040.00 USD |
| `1D` | `0.1066` | 257,170.00 USD | 257,170.00 USD | 0.00 USD | 0.00 USD | 12,550.00 USD | 16,970.00 USD |
| `7D` | `0.1067` | 490,590.00 USD | 490,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 67,930.00 USD |
| `1D` | `0.1068` | 294,440.00 USD | 294,440.00 USD | 0.00 USD | 0.00 USD | 9,500.00 USD | 27,770.00 USD |
| `7D` | `0.1069` | 562,620.00 USD | 562,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 72,030.00 USD |
| `1D` | `0.1070` | 353,690.00 USD | 353,690.00 USD | 0.00 USD | 0.00 USD | 7,790.00 USD | 51,460.00 USD |
| `7D` | `0.1071` | 605,260.00 USD | 605,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 42,640.00 USD |
| `1D` | `0.1072` | 353,710.00 USD | 353,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15.82 USD |
| `7D` | `0.1073` | 623,000.00 USD | 623,000.00 USD | 0.00 USD | 0.00 USD | 17,700.00 USD | 31.64 USD |
| `1D` | `0.1074` | 353,750.00 USD | 353,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 42.35 USD |
| `1D` | `0.1076` | 353,820.00 USD | 353,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 67.62 USD |
| `1D` | `0.1078` | 353,870.00 USD | 353,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 52.64 USD |
| `7D` | `0.1081` | 623,030.00 USD | 623,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29.20 USD |
| `1D` | `0.1082` | 353,890.00 USD | 353,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21.66 USD |
| `1D` | `0.1084` | 382,590.00 USD | 382,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,700.00 USD |
| `1D` | `0.1086` | 455,520.00 USD | 455,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 72,930.00 USD |
| `7D` | `0.1087` | 628,070.00 USD | 628,070.00 USD | 0.00 USD | 0.00 USD | 5,040.00 USD | 0.00 USD |
| `1D` | `0.1088` | 507,810.00 USD | 507,810.00 USD | 0.00 USD | 44,230.00 USD | 0.00 USD | 8,060.00 USD |
| `7D` | `0.1089` | 633,360.00 USD | 633,360.00 USD | 0.00 USD | 5,290.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1090` | 554,920.00 USD | 554,920.00 USD | 0.00 USD | 47,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1091` | 658,680.00 USD | 658,680.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 9,010.00 USD |
| `1D` | `0.1092` | 565,210.00 USD | 565,210.00 USD | 0.00 USD | 10,290.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1093` | 667,420.00 USD | 667,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,750.00 USD |
| `1D` | `0.1094` | 592,160.00 USD | 592,160.00 USD | 0.00 USD | 13,100.00 USD | 0.00 USD | 13,850.00 USD |
| `7D` | `0.1095` | 667,600.00 USD | 667,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 181.59 USD |
| `1D` | `0.1096` | 605,830.00 USD | 605,830.00 USD | 0.00 USD | 4,110.00 USD | 1,890.00 USD | 7,670.00 USD |
| `7D` | `0.1097` | 686,210.00 USD | 686,210.00 USD | 0.00 USD | 18,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1098` | 645,910.00 USD | 645,910.00 USD | 0.00 USD | 13,380.00 USD | 3,910.00 USD | 22,790.00 USD |
| `7D` | `0.1099` | 719,510.00 USD | 719,510.00 USD | 0.00 USD | 11,470.00 USD | 0.00 USD | 21,840.00 USD |
| `1D` | `0.1100` | 653,020.00 USD | 653,020.00 USD | 0.00 USD | 0.00 USD | 2,820.00 USD | 4,290.00 USD |
| `7D` | `0.1101` | 742,720.00 USD | 742,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23,210.00 USD |
| `1D` | `0.1102` | 657,320.00 USD | 657,320.00 USD | 0.00 USD | 4,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1103` | 760,210.00 USD | 760,210.00 USD | 0.00 USD | 17,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1104` | 671,670.00 USD | 671,670.00 USD | 0.00 USD | 6,920.00 USD | 7,430.00 USD | 0.00 USD |
| `7D` | `0.1105` | 774,690.00 USD | 774,690.00 USD | 0.00 USD | 0.00 USD | 14,480.00 USD | 0.00 USD |
| `1D` | `0.1106` | 715,210.00 USD | 715,210.00 USD | 0.00 USD | 0.00 USD | 12,720.00 USD | 30,820.00 USD |
| `7D` | `0.1107` | 803,160.00 USD | 803,160.00 USD | 0.00 USD | 0.00 USD | 12,510.00 USD | 15,950.00 USD |
| `1D` | `0.1108` | 733,940.00 USD | 733,940.00 USD | 0.00 USD | 3,110.00 USD | 0.00 USD | 15,630.00 USD |
| `7D` | `0.1109` | 818,110.00 USD | 818,110.00 USD | 0.00 USD | 0.00 USD | 14,950.00 USD | 0.00 USD |
| `7D` | `0.1111` | 830,060.00 USD | 830,060.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 0.00 USD |
| `1D` | `0.1112` | 739,140.00 USD | 739,140.00 USD | 0.00 USD | 5,200.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1114` | 799,230.00 USD | 799,230.00 USD | 0.00 USD | 15,810.00 USD | 5,210.00 USD | 39,070.00 USD |
| `1D` | `0.1116` | 823,000.00 USD | 823,000.00 USD | 0.00 USD | 4,760.00 USD | 12,080.00 USD | 6,930.00 USD |
| `7D` | `0.1117` | 869,330.00 USD | 869,330.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | 16,490.00 USD |
| `1D` | `0.1118` | 928,900.00 USD | 928,900.00 USD | 0.00 USD | 29,340.00 USD | 19,550.00 USD | 57,010.00 USD |
| `7D` | `0.1119` | 932,650.00 USD | 932,650.00 USD | 0.00 USD | 34,550.00 USD | 7,050.00 USD | 21,720.00 USD |
| `1D` | `0.1120` | 967,790.00 USD | 967,790.00 USD | 0.00 USD | 20,510.00 USD | 8,540.00 USD | 9,830.00 USD |
| `7D` | `0.1121` | 959,560.00 USD | 959,560.00 USD | 0.00 USD | 5,730.00 USD | 0.00 USD | 21,180.00 USD |
| `1D` | `0.1122` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 18,850.00 USD | 4,480.00 USD | 12,490.00 USD |
| `7D` | `0.1123` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 12,360.00 USD | 23,980.00 USD | 37,780.00 USD |
| `1D` | `0.1124` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 19,640.00 USD | 5,620.00 USD | 6,030.00 USD |
| `7D` | `0.1125` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 2,230.00 USD | 36,160.00 USD |
| `1D` | `0.1126` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 9,370.00 USD | 10,660.00 USD | 16,960.00 USD |
| `7D` | `0.1127` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,980.00 USD |
| `1D` | `0.1128` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 8,710.00 USD | 0.00 USD | 7,910.00 USD |
| `7D` | `0.1129` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65.26 USD |
| `1D` | `0.1130` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 7,970.00 USD | 1,490.00 USD | 5,150.00 USD |
| `7D` | `0.1131` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 12,540.00 USD | 0.00 USD | 15,240.00 USD |
| `1D` | `0.1132` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 16,120.00 USD | 17,300.00 USD | 16,110.00 USD |
| `7D` | `0.1133` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 11,430.00 USD | 110.20 USD |
| `1D` | `0.1134` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 4,040.00 USD | 12,980.00 USD | 13,830.00 USD |
| `7D` | `0.1135` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 9,010.00 USD |
| `1D` | `0.1136` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 787.70 USD | 4,130.00 USD |
| `1D` | `0.1138` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 856.93 USD | 14,270.00 USD |
| `1D` | `0.1140` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 7,800.00 USD | 0.00 USD | 6,050.00 USD |
| `7D` | `0.1141` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 7,540.00 USD |
| `1D` | `0.1142` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 24,760.00 USD | 17,100.00 USD | 15,310.00 USD |
| `7D` | `0.1143` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78,600.00 USD |
| `1D` | `0.1144` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 9,940.00 USD | 21,970.00 USD | 31,580.00 USD |
| `7D` | `0.1145` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 16,540.00 USD | 2,730.00 USD | 141,180.00 USD |
| `1D` | `0.1146` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 5,090.00 USD | 10,830.00 USD | 30,050.00 USD |
| `7D` | `0.1147` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 138,270.00 USD |
| `1D` | `0.1148` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 33,430.00 USD | 3,280.00 USD | 30,510.00 USD |
| `7D` | `0.1149` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 10,560.00 USD | 0.00 USD | 72,860.00 USD |
| `1D` | `0.1150` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 19,260.00 USD | 13,020.00 USD | 21,660.00 USD |
| `7D` | `0.1151` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 92,570.00 USD | 4,210.00 USD | 128,500.00 USD |
| `1D` | `0.1152` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 34,520.00 USD | 17,470.00 USD | 59,670.00 USD |
| `7D` | `0.1153` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 153,720.00 USD | 8,400.00 USD | 139,830.00 USD |
| `1D` | `0.1154` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 18,600.00 USD | 23,230.00 USD | 54,770.00 USD |
| `7D` | `0.1155` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 149,360.00 USD | 40,110.00 USD | 105,750.00 USD |
| `1D` | `0.1156` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 48,760.00 USD | 21,470.00 USD | 24,350.00 USD |
| `7D` | `0.1157` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 133,960.00 USD | 3,760.00 USD | 48,320.00 USD |
| `1D` | `0.1158` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 26,730.00 USD | 9,500.00 USD | 41,820.00 USD |
| `7D` | `0.1159` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 81,080.00 USD | 12,710.00 USD | 53,380.00 USD |
| `1D` | `0.1160` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 34,710.00 USD | 4,660.00 USD | 8,480.00 USD |
| `7D` | `0.1161` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 146,810.00 USD | 37,250.00 USD | 100,110.00 USD |
| `1D` | `0.1162` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 9,050.00 USD | 8,790.00 USD | 8,130.00 USD |
| `7D` | `0.1163` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 53,510.00 USD | 11,460.00 USD | 68,560.00 USD |
| `1D` | `0.1164` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 3,830.00 USD | 8,020.00 USD | 18,360.00 USD |
| `7D` | `0.1165` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 68,620.00 USD | 35,720.00 USD | 27,080.00 USD |
| `1D` | `0.1166` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 10,670.00 USD | 8,850.00 USD | 40.24 USD |
| `7D` | `0.1167` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 79,610.00 USD | 21,620.00 USD | 41,290.00 USD |
| `1D` | `0.1168` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 1,880.00 USD | 8,430.00 USD |
| `7D` | `0.1169` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 65,340.00 USD | 14,840.00 USD | 86,630.00 USD |
| `1D` | `0.1170` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 14,800.00 USD | 2,000.00 USD | 6,660.00 USD |
| `7D` | `0.1171` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 57,350.00 USD | 11,370.00 USD | 35,090.00 USD |
| `1D` | `0.1172` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 10,950.00 USD | 5,440.00 USD | 1,570.00 USD |
| `7D` | `0.1173` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 40,860.00 USD | 9,190.00 USD | 36,730.00 USD |
| `1D` | `0.1174` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 10,300.00 USD | 6,360.00 USD | 15,250.00 USD |
| `7D` | `0.1175` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 38,840.00 USD | 12,300.00 USD | 58,980.00 USD |
| `1D` | `0.1176` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 4,150.00 USD | 7,940.00 USD | 20,110.00 USD |
| `7D` | `0.1177` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 33,330.00 USD | 20,350.00 USD | 43,940.00 USD |
| `1D` | `0.1178` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 16,140.00 USD | 7,760.00 USD | 7,040.00 USD |
| `7D` | `0.1179` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 66,670.00 USD | 10,940.00 USD | 23,910.00 USD |
| `1D` | `0.1180` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 15,510.00 USD | 4,770.00 USD | 27,060.00 USD |
| `7D` | `0.1181` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 22,290.00 USD | 15,780.00 USD | 17,780.00 USD |
| `1D` | `0.1182` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 15,890.00 USD | 3,000.00 USD | 5,750.00 USD |
| `7D` | `0.1183` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 7,760.00 USD | 1,800.00 USD | 39,300.00 USD |
| `1D` | `0.1184` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 6,980.00 USD | 1,730.00 USD | 8,230.00 USD |
| `7D` | `0.1185` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 3,880.00 USD | 5,130.00 USD | 26,850.00 USD |
| `1D` | `0.1186` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 3,430.00 USD | 6,750.00 USD | 11,830.00 USD |
| `7D` | `0.1187` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 5,620.00 USD | 15,370.00 USD | 36,640.00 USD |
| `1D` | `0.1188` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 2,780.00 USD | 6,670.00 USD | 4,640.00 USD |
| `7D` | `0.1189` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 27,240.00 USD | 15,060.00 USD | 3,250.00 USD |
| `1D` | `0.1190` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 2,840.00 USD | 856.99 USD | 2,740.00 USD |
| `7D` | `0.1191` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 22,650.00 USD | 15,330.00 USD | 109,210.00 USD |
| `1D` | `0.1192` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 4,720.00 USD | 1,990.00 USD | 9,370.00 USD |
| `7D` | `0.1193` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 21,260.00 USD | 0.00 USD | 12,500.00 USD |
| `1D` | `0.1194` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 6,310.00 USD | 347.94 USD | 2,810.00 USD |
| `7D` | `0.1195` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 11,190.00 USD | 1,780.00 USD | 29,380.00 USD |
| `1D` | `0.1196` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 3,240.00 USD | 1,120.00 USD | 100.88 USD |
| `7D` | `0.1197` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 6,780.00 USD | 10,800.00 USD | 14,300.00 USD |
| `1D` | `0.1198` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 1,040.00 USD | 2,070.00 USD |
| `7D` | `0.1199` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 9,100.00 USD | 2,390.00 USD | 64,440.00 USD |
| `1D` | `0.1200` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 1,840.00 USD | 1,360.00 USD | 7,790.00 USD |
| `7D` | `0.1201` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 114,140.00 USD | 16,380.00 USD | 29,150.00 USD |
| `1D` | `0.1202` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 7,070.00 USD | 460.32 USD | 4,370.00 USD |
| `7D` | `0.1203` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 70,770.00 USD | 29,250.00 USD | 6,320.00 USD |
| `1D` | `0.1204` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 413.94 USD | 1,290.00 USD |
| `7D` | `0.1205` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 86,480.00 USD | 48,720.00 USD | 128,320.00 USD |
| `1D` | `0.1206` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 5,370.00 USD | 2,190.00 USD | 3,320.00 USD |
| `7D` | `0.1207` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 12,460.00 USD | 19,400.00 USD | 53,940.00 USD |
| `1D` | `0.1208` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 4,600.00 USD | 2,120.00 USD | 3,700.00 USD |
| `7D` | `0.1209` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 85,160.00 USD | 19,340.00 USD | 94,170.00 USD |
| `1D` | `0.1210` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 3,980.00 USD | 3,340.00 USD | 2,520.00 USD |
| `7D` | `0.1211` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 14,350.00 USD | 12,900.00 USD | 29,770.00 USD |
| `1D` | `0.1212` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 1,470.00 USD | 1,690.00 USD | 7,840.00 USD |
| `7D` | `0.1213` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 23,920.00 USD | 12,800.00 USD | 24,130.00 USD |
| `1D` | `0.1214` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 4,740.00 USD | 820.70 USD | 9,850.00 USD |
| `7D` | `0.1215` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 5,900.00 USD | 6,620.00 USD | 59,130.00 USD |
| `1D` | `0.1216` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,350.00 USD |
| `7D` | `0.1217` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 18,490.00 USD | 6,160.00 USD | 11,080.00 USD |
| `1D` | `0.1218` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 2,640.00 USD | 624.33 USD | 8,810.00 USD |
| `7D` | `0.1219` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 26,700.00 USD | 5,500.00 USD | 38,020.00 USD |
| `1D` | `0.1220` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 2,690.00 USD | 1,690.00 USD | 6,280.00 USD |
| `7D` | `0.1221` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 25,890.00 USD | 15,750.00 USD | 18,890.00 USD |
| `1D` | `0.1222` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 2,760.00 USD | 3,370.00 USD | 6,540.00 USD |
| `7D` | `0.1223` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 70,040.00 USD | 25,830.00 USD | 48,450.00 USD |
| `7D` | `0.1225` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 43,040.00 USD | 19,970.00 USD | 5,260.00 USD |
| `7D` | `0.1227` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 49,930.00 USD | 23,840.00 USD | 50,650.00 USD |
| `7D` | `0.1229` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 63,350.00 USD | 30,490.00 USD | 40,620.00 USD |
| `7D` | `0.1231` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 21,280.00 USD | 29,380.00 USD | 27,570.00 USD |
| `7D` | `0.1233` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 57,130.00 USD | 13,020.00 USD | 40,130.00 USD |
| `7D` | `0.1235` | 6,560,000.00 USD | 6,560,000.00 USD | 0.00 USD | 4,430.00 USD | 4,720.00 USD | 8,950.00 USD |
| `7D` | `0.1237` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 4,080.00 USD | 2,760.00 USD | 2,890.00 USD |
| `7D` | `0.1239` | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 8,780.00 USD | 1,270.00 USD | 479.13 USD |
| `7D` | `0.1241` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 6,830.00 USD | 965.35 USD | 2,400.00 USD |
| `7D` | `0.1243` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 11,450.00 USD | 4,530.00 USD | 4,670.00 USD |
| `7D` | `0.1245` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 15,080.00 USD | 8,080.00 USD | 12,970.00 USD |
| `7D` | `0.1247` | 6,680,000.00 USD | 6,680,000.00 USD | 0.00 USD | 7,900.00 USD | 13,800.00 USD | 9,710.00 USD |
| `7D` | `0.1249` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 13,440.00 USD | 5,480.00 USD | 5,660.00 USD |
| `7D` | `0.1251` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 0.00 USD | 1,800.00 USD | 8,520.00 USD |
| `7D` | `0.1253` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 11,420.00 USD | 2,100.00 USD | 14,010.00 USD |
| `7D` | `0.1255` | 6,760,000.00 USD | 6,760,000.00 USD | 0.00 USD | 2,250.00 USD | 13,990.00 USD | 33.04 USD |
| `7D` | `0.1257` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 15,610.00 USD | 5,200.00 USD | 54.64 USD |
| `7D` | `0.1259` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 288.60 USD |
| `7D` | `0.1261` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | 3,500.00 USD |
| `7D` | `0.1263` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,080.00 USD |
| `7D` | `0.1265` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 2,710.00 USD | 0.00 USD | 3,260.00 USD |
| `7D` | `0.1267` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,920.00 USD |
| `7D` | `0.1269` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16.21 USD |
| `7D` | `0.1271` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 5,940.00 USD | 0.00 USD | 15.40 USD |
| `7D` | `0.1273` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10.64 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `69.75M` | Total OI Tokens: `652,094,076.9 OP`
  * 1h OI Change: `-4.15%` | 4h OI Change: `-7.53%` | 24h OI Change: `-8.91%`
  * Exchange Breakdown: Binance=`16.16M` | Bybit=`13.91M` | OKX=`4.00M` | Hyperliquid=`3.65M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-1.56K` | Last 24h: `270.64` | Last 3d: `-2.23K` | Last 7d: `-15.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0086%` | **USDT OKX** | `0.0062%` |
| **USDT Bybit** | `-0.0033%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0082%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0210%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `OP` | `45.07%` | `54.93%` | `0.82` | 4,730,000.00 USD |
| `15M` | `Binance` | `43.71%` | `56.29%` | `0.78` | 1,620,000.00 USD |
| `15M` | `OKX` | `41.58%` | `58.42%` | `0.71` | 638,100.00 USD |
| `15M` | `Bybit` | `37.45%` | `62.55%` | `0.60` | 678,510.00 USD |
| `15M` | `KuCoin` | `44.5%` | `55.5%` | `0.80` | 83,580.00 USD |
| `15M` | `Gate` | `47.74%` | `52.26%` | `0.91` | 40,400.00 USD |
| `15M` | `Bitget` | `68.7%` | `31.3%` | `2.19` | 523,560.00 USD |
| `15M` | `BingX` | `40.7%` | `59.3%` | `0.69` | 72,970.00 USD |
| `15M` | `MEXC` | `23.31%` | `76.69%` | `0.30` | 154,980.00 USD |
| `15M` | `Bitunix` | `39.44%` | `60.56%` | `0.65` | 54,200.00 USD |
| `15M` | `Hyperliquid` | `30.42%` | `69.58%` | `0.44` | 181,700.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.17%` | `51.83%` | `0.93` | 631,070.00 USD |
| `15M` | `Crypto.com` | `0%` | `100%` | `0.00` | 236.17 USD |
| `15M` | `WhiteBIT` | `85.95%` | `14.05%` | `6.12` | 24,650.00 USD |
| `15M` | `HTX` | `58.56%` | `41.44%` | `1.41` | 1,140.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `82.47%` | `17.53%` | `4.70` | 7,480.00 USD |
| `15M` | `Aster` | `76.04%` | `23.96%` | `3.17` | 12,470.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `71.55%` | `28.45%` | `2.51` | 6,620.00 USD |
| `15M` | `Whale Positions` | `43.71%` | `56.29%` | `0.78` | 1,620,000.00 USD |
| `15M` | `Global Accounts` | `45.07%` | `54.93%` | `0.82` | 4,730,000.00 USD |
| `1H` | `OP` | `40.28%` | `59.72%` | `0.67` | 15,510,000.00 USD |
| `1H` | `Binance` | `45.44%` | `54.56%` | `0.83` | 6,340,000.00 USD |
| `1H` | `OKX` | `45.52%` | `54.48%` | `0.84` | 1,340,000.00 USD |
| `1H` | `Bybit` | `44.74%` | `55.26%` | `0.81` | 1,760,000.00 USD |
| `1H` | `KuCoin` | `49.57%` | `50.43%` | `0.98` | 698,430.00 USD |
| `1H` | `Gate` | `61.18%` | `38.82%` | `1.58` | 441,190.00 USD |
| `1H` | `Bitget` | `40.67%` | `59.33%` | `0.69` | 444,650.00 USD |
| `1H` | `BingX` | `12.88%` | `87.12%` | `0.15` | 2,220,000.00 USD |
| `1H` | `MEXC` | `31.9%` | `68.1%` | `0.47` | 936,260.00 USD |
| `1H` | `Bitunix` | `50.81%` | `49.19%` | `1.03` | 316,070.00 USD |
| `1H` | `Hyperliquid` | `30.85%` | `69.15%` | `0.45` | 188,170.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.99%` | `52.01%` | `0.92` | 319,520.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `42.1%` | `57.9%` | `0.73` | 416,950.00 USD |
| `1H` | `HTX` | `31.24%` | `68.76%` | `0.45` | 2,850.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `41.36%` | `58.64%` | `0.71` | 56,320.00 USD |
| `1H` | `Aster` | `36.74%` | `63.26%` | `0.58` | 14,320.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `62.54%` | `37.46%` | `1.67` | 11,320.00 USD |
| `1H` | `Whale Positions` | `45.44%` | `54.56%` | `0.83` | 6,340,000.00 USD |
| `1H` | `Global Accounts` | `40.28%` | `59.72%` | `0.67` | 15,510,000.00 USD |
| `4H` | `OP` | `48.81%` | `51.19%` | `0.95` | 25,770,000.00 USD |
| `4H` | `Binance` | `46.92%` | `53.08%` | `0.88` | 9,270,000.00 USD |
| `4H` | `OKX` | `46.05%` | `53.95%` | `0.85` | 2,940,000.00 USD |
| `4H` | `Bybit` | `46.68%` | `53.32%` | `0.88` | 3,510,000.00 USD |
| `4H` | `KuCoin` | `48.34%` | `51.66%` | `0.94` | 191,240.00 USD |
| `4H` | `Gate` | `47.42%` | `52.58%` | `0.90` | 257,140.00 USD |
| `4H` | `Bitget` | `54.45%` | `45.55%` | `1.20` | 1,380,000.00 USD |
| `4H` | `BingX` | `53.14%` | `46.86%` | `1.13` | 1,390,000.00 USD |
| `4H` | `MEXC` | `45.6%` | `54.4%` | `0.84` | 1,320,000.00 USD |
| `4H` | `Bitunix` | `46.35%` | `53.65%` | `0.86` | 299,820.00 USD |
| `4H` | `Hyperliquid` | `31.37%` | `68.63%` | `0.46` | 301,820.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.44%` | `50.56%` | `0.98` | 4,200,000.00 USD |
| `4H` | `Crypto.com` | `0.01%` | `99.99%` | `0.00` | 786.09 USD |
| `4H` | `WhiteBIT` | `94.17%` | `5.83%` | `16.15` | 613,390.00 USD |
| `4H` | `HTX` | `42.31%` | `57.69%` | `0.73` | 1,850.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `53.73%` | `46.27%` | `1.16` | 25,760.00 USD |
| `4H` | `Aster` | `40.07%` | `59.93%` | `0.67` | 26,930.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `40.7%` | `59.3%` | `0.69` | 25,330.00 USD |
| `4H` | `Whale Positions` | `46.92%` | `53.08%` | `0.88` | 9,270,000.00 USD |
| `4H` | `Global Accounts` | `48.81%` | `51.19%` | `0.95` | 25,770,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1108` | `0.1106` | `0.1108` | `0.1112` | `0.1101` | 266,281.73 USD | 113,817.33 USD | 152,464.41 USD | -38,647.08 USD | `-14.51%` | `15B / 30S` |
| `0:00 UTC` | `0.1097` | `0.1098` | `0.1097` | `0.1103` | `0.1094` | 698,148.28 USD | 345,564.95 USD | 352,583.33 USD | -7,018.38 USD | `-1.01%` | `13B / 19S` |
| `5:00 UTC` | `0.1102` | `0.1100` | `0.1102` | `0.1104` | `0.1095` | 273,714.46 USD | 165,910.77 USD | 107,803.69 USD | 58,107.08 USD | `+21.23%` | `25B / 9S` |
| `0:00 UTC` | `0.1097` | `0.1098` | `0.1097` | `0.1101` | `0.1096` | 225,346.74 USD | 116,304.67 USD | 109,042.07 USD | 7,262.60 USD | `+3.22%` | `6B / 4S` |
| `5:00 UTC` | `0.1098` | `0.1100` | `0.1098` | `0.1102` | `0.1096` | 199,782.25 USD | 121,152.98 USD | 78,629.27 USD | 42,523.71 USD | `+21.29%` | `24B / 5S` |
| `0:00 UTC` | `0.1103` | `0.1104` | `0.1103` | `0.1106` | `0.1100` | 230,285.46 USD | 143,965.28 USD | 86,320.18 USD | 57,645.10 USD | `+25.03%` | `14B / 4S` |
| `5:00 UTC` | `0.1102` | `0.1102` | `0.1102` | `0.1105` | `0.1099` | 215,356.47 USD | 112,661.20 USD | 102,695.27 USD | 9,965.93 USD | `+4.63%` | `7B / 11S` |
| `0:00 UTC` | `0.1077` | `0.1082` | `0.1077` | `0.1102` | `0.1070` | 2,425,114.31 USD | 1,046,280.57 USD | 1,378,833.74 USD | -332,553.17 USD | `-13.71%` | `8B / 30S` |
| `5:00 UTC` | `0.1084` | `0.1083` | `0.1084` | `0.1087` | `0.1080` | 527,563.25 USD | 310,298.99 USD | 217,264.26 USD | 93,034.72 USD | `+17.63%` | `19B / 3S` |
| `0:00 UTC` | `0.1063` | `0.1066` | `0.1063` | `0.1088` | `0.1056` | 2,223,157.35 USD | 927,615.73 USD | 1,295,541.63 USD | -367,925.90 USD | `-16.55%` | `13B / 20S` |

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
| `5m` | -31,750.00 USD | 75,810.00 USD | **`ACCUMULATION`** |
| `15m` | -16,940.00 USD | 92,330.00 USD | **`ACCUMULATION`** |
| `30m` | 78,530.00 USD | 63,030.00 USD | **`ACCUMULATION`** |
| `1h` | 11,500.00 USD | -235,440.00 USD | **`DISTRIBUTION`** |
| `2h` | 17,150.00 USD | 84,950.00 USD | **`ACCUMULATION`** |
| `4h` | -11,640.00 USD | -547,330.00 USD | **`DISTRIBUTION`** |
| `6h` | 75,350.00 USD | -345,290.00 USD | **`DISTRIBUTION`** |
| `8h` | 175,970.00 USD | 25,250.00 USD | **`ACCUMULATION`** |
| `12h` | 226,180.00 USD | 313,710.00 USD | **`ACCUMULATION`** |
| `24h` | 99,140.00 USD | -1,870,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -93,490.00 USD | -9,710,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,530,000.00 USD | -78,790,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-31.75K` | 15m=`-16.94K` | 1h=`+11.50K` | 24h=`+99.14K`
* Futures Capital Netflows: 5m=`+75.81K` | 15m=`+92.33K` | 1h=`-235.44K` | 24h=`-1.87M`
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
  * `2026-10-30 01:35:25 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:09:25 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:09:25 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:09:25 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:08:25 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:08:25 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:25 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:25 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:25 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:25 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:25 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
