# 🏛️ SOVEREIGN CANDIDATE DOSSIER: APT
**Canonical Key**: `APT` | **Broker Instrument**: `APTUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 09:43:23 IST` (`2026-10-30 04:13:23 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.6900` | **Live Ask Quote**: `0.6901` | **Mid Price**: `0.6901`
- **Spread Points**: `0.000138` | **Spread BPS**: `2.00 bps` (Charter Threshold: `12.00 bps`)
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
  * Session VWAP: `0.6901` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.6949` | Lower -3.00σ Band: `0.6852`
  * Upper +2.51σ Band: `0.6939` | Lower -2.51σ Band: `0.6863`
  * Upper +2.01σ Band: `0.6930` | Lower -2.01σ Band: `0.6872`
  * Upper +2.00σ Band: `0.6928` | Lower -2.00σ Band: `0.6873`
  * Upper +1.28σ Band: `0.6920` | Lower -1.28σ Band: `0.6881`
  * Upper +1.00σ Band: `0.6914` | Lower -1.00σ Band: `0.6887`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.6901` | EMA-20=`0.6901` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.6901` (Slope: `+0.0000`) | EMA-100=`0.6901`
  * Institutional Anchors: EMA-144=`0.6901` | EMA-200=`0.6901` (Slope: `+0.0000`) | EMA-233=`0.6901`
- **Range Boundaries**: 24H High=`0.6970` | 24H Low=`0.6832` | Weekly High=`0.7039` | Weekly Low=`0.6763`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.6921` (Distance: `+0.00%`)
  * Point of Control (POC) = `0.6901` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `0.6880` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.6928` | POC=`0.6901` | VAL=`0.6873`
  * Prior Day Extremes: PDH=`0.6942` | PDL=`0.6859` | PDC=`0.6901`
  * Monday Range Blueprint: High=`0.6935` | Mid=`0.6901` | Low=`0.6866`
  * Developing Weekly Value Area: Weekly VAH=`0.6956` | Weekly POC=`0.6901` | Weekly VAL=`0.6845`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.6914` | Low=`0.6887`
  * London Session (08:00-16:00 UTC): High=`0.6928` | Low=`0.6873`
  * New York Session (13:00-21:00 UTC): High=`0.6942` | Low=`0.6859`
  * Initial Balance (First Hour): IB High=`0.6921` | IB Low=`0.6880`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.6873` - `0.6928`
  * Optimal Trade Entry (OTE 0.705): `0.6914`
  * Structural Invalidation Anchor (0.786): `0.6956`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.6117` | `0.6147` | `0.6111` | `0.6145` | `197,571` | 121,169.01 USD | 11,193.43 USD | `+9.24%` | -6,191,997.07 USD | `+0.10` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.6145` | `0.6174` | `0.6135` | `0.6156` | `400,383` | 246,386.57 USD | 90,236.53 USD | `+36.62%` | -6,101,760.54 USD | `+1.65` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.6156` | `0.6173` | `0.6146` | `0.6169` | `248,230` | 152,901.42 USD | 51,384.08 USD | `+33.61%` | -6,050,376.46 USD | `+0.76` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.6048` | `0.6095` | `0.6042` | `0.6090` | `315,687` | 191,671.81 USD | 65,576.74 USD | `+34.21%` | -6,227,024.15 USD | `+0.42` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.6090` | `0.6174` | `0.6090` | `0.6156` | `766,132` | 470,291.39 USD | 109,505.66 USD | `+23.28%` | -6,117,518.49 USD | `+0.57` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.6156` | `0.6173` | `0.6146` | `0.6172` | `250,179` | 154,103.89 USD | 52,481.05 USD | `+34.06%` | -6,065,037.44 USD | `+0.33` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.6024` | `0.6089` | `0.5938` | `0.6023` | `4,754,374` | 2,863,554.31 USD | 298,685.20 USD | `+10.43%` | -6,338,835.94 USD | `+0.80` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.6024` | `0.6109` | `0.5966` | `0.6032` | `3,667,839` | 2,218,815.27 USD | -7,363.46 USD | `-0.33%` | -6,346,199.39 USD | `+0.40` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.6032` | `0.6174` | `0.6026` | `0.6172` | `1,811,082` | 1,106,081.10 USD | 281,161.96 USD | `+25.42%` | -6,065,037.44 USD | `+0.73` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -2,044,054.97 USD | `-1.70` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6003` | `0.6161` | `56,944,695` | 35,933,598.81 USD | -3,666,266.35 USD | `-10.20%` | -5,710,321.32 USD | `-1.86` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6162` | `0.6185` | `0.5736` | `0.6170` | `24,658,861` | 14,769,408.52 USD | -354,700.01 USD | `-2.40%` | -6,065,021.33 USD | `+0.51` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6561` | `0.6774` | `0.6549` | `0.6712` | `7,448,343` | 4,965,296.85 USD | -60,141.40 USD | `-1.21%` | -427,040.08 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -575,126.84 USD | `+0.34` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -2,044,054.97 USD | `-1.70` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6003` | `0.6161` | `56,944,695` | 35,933,598.81 USD | -3,666,266.35 USD | `-10.20%` | -5,710,321.32 USD | `-1.86` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6162` | `0.6185` | `0.5736` | `0.6170` | `24,658,861` | 14,769,408.52 USD | -354,700.01 USD | `-2.40%` | -6,065,021.33 USD | `+0.51` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`0.6901`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:33:32 IST` |

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
  * 24H Horizon: Short MP=`0.7060` (Vol: 90,823.17 USD, Dist: `+2.43%`) | Long MP=`0.6718` (Vol: 39,956.88 USD, Dist: `--2.53%`)
  * 48H Horizon: Short MP=`0.7055` (Vol: 81,903.46 USD, Dist: `+2.36%`) | Long MP=`0.6702` (Vol: 45,046.52 USD, Dist: `--2.77%`)
  * 3D Horizon: Short MP=`0.7210` (Vol: 125,191.03 USD, Dist: `+4.60%`) | Long MP=`0.6703` (Vol: 75,398.81 USD, Dist: `--2.76%`)
  * 7D Horizon: Short MP=`0.8539` (Vol: 187,280.71 USD, Dist: `+24.46%`) | Long MP=`0.6700` (Vol: 92,436.78 USD, Dist: `--2.35%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.1395` | 419.65 USD | 232,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1805` | 1,310.00 USD | 232,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 269.27 USD | 231,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1905` | 24,570.00 USD | 230,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 228.91 USD | 206,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 2,610.00 USD | 205,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 1,460.00 USD | 203,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 363.05 USD | 201,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2705` | 272.20 USD | 201,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3105` | 105.38 USD | 201,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3175` | 1,590.00 USD | 201,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3305` | 543.58 USD | 199,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3345` | 9,520.00 USD | 198,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3545` | 177.25 USD | 189,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3585` | 12,850.00 USD | 189,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3675` | 189.99 USD | 176,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3855` | 771.39 USD | 176,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3905` | 359.26 USD | 175,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3955` | 2,640.00 USD | 175,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3995` | 271.06 USD | 172,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4025` | 603.75 USD | 172,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4125` | 1,070.00 USD | 171,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4135` | 1,600.00 USD | 170,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4165` | 291.55 USD | 168,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 630.86 USD | 168,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4235` | 101.13 USD | 168,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4255` | 224.96 USD | 167,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 226.63 USD | 167,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4515` | 27,090.00 USD | 167,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 6,140.00 USD | 140,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4555` | 461.17 USD | 134,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4605` | 430.79 USD | 133,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4615` | 595.82 USD | 133,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4625` | 1,460.00 USD | 132,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4645` | 876.05 USD | 131,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4685` | 468.50 USD | 130,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 6,140.00 USD | 129,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4855` | 181.88 USD | 123,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 3,170.00 USD | 123,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4925` | 10,520.00 USD | 120,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4935` | 1,580.00 USD | 109,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 3,350.00 USD | 108,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4965` | 143.19 USD | 104,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4975` | 667.49 USD | 104,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 429.90 USD | 104,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5075` | 303.42 USD | 103,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 102.82 USD | 103,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5095` | 958.55 USD | 103,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5115` | 12,000.00 USD | 102,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 248.05 USD | 90,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5135` | 298.60 USD | 90,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 9,440.00 USD | 89,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 281.56 USD | 80,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5245` | 209.80 USD | 80,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5295` | 1,840.00 USD | 79,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5315` | 11,510.00 USD | 78,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5320` | 869,060.00 USD | 869,060.00 USD | 11,240.00 USD | 0.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5335` | 163.22 USD | 66,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5340` | 854,350.00 USD | 854,350.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5360` | 851,740.00 USD | 851,740.00 USD | 2,440.00 USD | 3,040.00 USD | 44.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5380` | 846,220.00 USD | 846,220.00 USD | 0.00 USD | 1,550.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5400` | 841,770.00 USD | 841,770.00 USD | 0.00 USD | 0.00 USD | 70.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5420` | 841,700.00 USD | 841,700.00 USD | 7,660.00 USD | 1,290.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5440` | 829,880.00 USD | 829,880.00 USD | 0.00 USD | 1,150.00 USD | 6,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5445` | 855.28 USD | 66,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5455` | 1,850.00 USD | 65,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5460` | 821,740.00 USD | 821,740.00 USD | 2,250.00 USD | 3,030.00 USD | 5,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,630.00 USD | 63,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5480` | 811,300.00 USD | 811,300.00 USD | 2,000.00 USD | 795.70 USD | 4,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5500` | 839,890.00 USD | 839,890.00 USD | 0.00 USD | 0.00 USD | 19.90 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5500` | 804,020.00 USD | 804,020.00 USD | 5,990.00 USD | 1,440.00 USD | 6,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5510` | 839,870.00 USD | 839,870.00 USD | 0.00 USD | 0.00 USD | 849.87 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5520` | 839,020.00 USD | 839,020.00 USD | 0.00 USD | 0.00 USD | 432.53 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5520` | 789,890.00 USD | 789,890.00 USD | 4,110.00 USD | 1,920.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5530` | 838,590.00 USD | 838,590.00 USD | 1,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5540` | 837,320.00 USD | 837,320.00 USD | 528.00 USD | 1,320.00 USD | 7.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5540` | 781,970.00 USD | 781,970.00 USD | 12,840.00 USD | 4,860.00 USD | 18,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5545` | 47,450.00 USD | 62,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5550` | 835,470.00 USD | 835,470.00 USD | 557.27 USD | 201.08 USD | 41.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5560` | 834,670.00 USD | 834,670.00 USD | 0.00 USD | 686.25 USD | 479.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5560` | 745,750.00 USD | 745,750.00 USD | 13,490.00 USD | 1,920.00 USD | 6,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5570` | 833,500.00 USD | 833,500.00 USD | 0.00 USD | 1,940.00 USD | 2,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5580` | 829,240.00 USD | 829,240.00 USD | 1,100.00 USD | 2,960.00 USD | 1,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5580` | 724,150.00 USD | 724,150.00 USD | 6,000.00 USD | 6,820.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5585` | 10,520.00 USD | 14,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5590` | 823,940.00 USD | 823,940.00 USD | 0.00 USD | 1,080.00 USD | 15.63 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5600` | 822,850.00 USD | 822,850.00 USD | 1,550.00 USD | 1,830.00 USD | 2,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5600` | 693,030.00 USD | 693,030.00 USD | 4,070.00 USD | 8,160.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5610` | 816,920.00 USD | 816,920.00 USD | 0.00 USD | 0.00 USD | 772.54 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5615` | 258.48 USD | 4,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5620` | 816,150.00 USD | 816,150.00 USD | 0.00 USD | 776.64 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5620` | 678,320.00 USD | 678,320.00 USD | 19,480.00 USD | 7,420.00 USD | 11,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5630` | 813,190.00 USD | 813,190.00 USD | 0.00 USD | 1,560.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5635` | 244.90 USD | 3,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5640` | 807,030.00 USD | 807,030.00 USD | 4,020.00 USD | 2,420.00 USD | 12.64 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5640` | 639,840.00 USD | 639,840.00 USD | 2,950.00 USD | 741.21 USD | 19.99 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5655` | 1,920.00 USD | 3,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5660` | 636,130.00 USD | 636,130.00 USD | 11,490.00 USD | 2,990.00 USD | 4,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5665` | 1,370.00 USD | 1,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5680` | 617,230.00 USD | 617,230.00 USD | 5,100.00 USD | 0.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5700` | 609,240.00 USD | 609,240.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5710` | 800,570.00 USD | 800,570.00 USD | 0.00 USD | 2,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5715` | 289.08 USD | 289.08 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5720` | 606,660.00 USD | 606,660.00 USD | 0.00 USD | 4,370.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5740` | 600,940.00 USD | 600,940.00 USD | 21,620.00 USD | 1,100.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.5745` | 1,530.00 USD | 1,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5760` | 576,540.00 USD | 576,540.00 USD | 2,150.00 USD | 0.00 USD | 18.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5770` | 798,220.00 USD | 798,220.00 USD | 0.00 USD | 0.00 USD | 34.98 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5780` | 798,180.00 USD | 798,180.00 USD | 0.00 USD | 0.00 USD | 59.63 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5780` | 574,370.00 USD | 574,370.00 USD | 0.00 USD | 0.00 USD | 1,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5800` | 572,840.00 USD | 572,840.00 USD | 1,610.00 USD | 0.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5820` | 798,120.00 USD | 798,120.00 USD | 0.00 USD | 1,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5820` | 568,390.00 USD | 568,390.00 USD | 0.00 USD | 0.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5830` | 797,120.00 USD | 797,120.00 USD | 0.00 USD | 0.00 USD | 24.36 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5840` | 797,100.00 USD | 797,100.00 USD | 0.00 USD | 0.00 USD | 44.63 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5850` | 797,050.00 USD | 797,050.00 USD | 0.00 USD | 0.00 USD | 18.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5860` | 797,030.00 USD | 797,030.00 USD | 0.00 USD | 658.88 USD | 14,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5870` | 781,500.00 USD | 781,500.00 USD | 2,890.00 USD | 631.19 USD | 3,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5880` | 774,480.00 USD | 774,480.00 USD | 1,270.00 USD | 1,580.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5880` | 561,730.00 USD | 561,730.00 USD | 3,110.00 USD | 1,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5890` | 767,940.00 USD | 767,940.00 USD | 3,460.00 USD | 0.00 USD | 7.65 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5900` | 764,480.00 USD | 764,480.00 USD | 4,730.00 USD | 1,390.00 USD | 3.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5900` | 557,220.00 USD | 557,220.00 USD | 3,120.00 USD | 1,560.00 USD | 81.07 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5910` | 758,360.00 USD | 758,360.00 USD | 0.00 USD | 1,820.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5920` | 752,430.00 USD | 752,430.00 USD | 11,320.00 USD | 3,660.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5920` | 552,460.00 USD | 552,460.00 USD | 11,690.00 USD | 2,820.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5930` | 729,680.00 USD | 729,680.00 USD | 3,420.00 USD | 3,860.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5940` | 714,130.00 USD | 714,130.00 USD | 5,890.00 USD | 6,830.00 USD | 10,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5940` | 531,780.00 USD | 531,780.00 USD | 10,090.00 USD | 0.00 USD | 9,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5950` | 691,320.00 USD | 691,320.00 USD | 19,520.00 USD | 12,400.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5960` | 657,440.00 USD | 657,440.00 USD | 8,460.00 USD | 3,150.00 USD | 13,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5960` | 511,710.00 USD | 511,710.00 USD | 18,180.00 USD | 18,410.00 USD | 13,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5970` | 632,500.00 USD | 632,500.00 USD | 9,250.00 USD | 8,270.00 USD | 13,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5980` | 601,920.00 USD | 601,920.00 USD | 6,400.00 USD | 1,740.00 USD | 41,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5980` | 462,080.00 USD | 462,080.00 USD | 20,380.00 USD | 826.53 USD | 19,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5990` | 552,780.00 USD | 552,780.00 USD | 18,690.00 USD | 2,370.00 USD | 13,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6000` | 518,270.00 USD | 518,270.00 USD | 0.00 USD | 5,920.00 USD | 1,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6000` | 420,950.00 USD | 420,950.00 USD | 3,320.00 USD | 2,140.00 USD | 18,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6010` | 511,220.00 USD | 511,220.00 USD | 735.24 USD | 461.96 USD | 11,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6020` | 498,620.00 USD | 498,620.00 USD | 30,900.00 USD | 13,240.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6020` | 396,630.00 USD | 396,630.00 USD | 23,960.00 USD | 8,040.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6030` | 452,460.00 USD | 452,460.00 USD | 10,880.00 USD | 6,850.00 USD | 24.50 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6040` | 434,710.00 USD | 434,710.00 USD | 19,810.00 USD | 2,320.00 USD | 21.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6040` | 360,430.00 USD | 360,430.00 USD | 8,620.00 USD | 7,530.00 USD | 7,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6050` | 412,560.00 USD | 412,560.00 USD | 0.00 USD | 3,770.00 USD | 20,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6060` | 388,650.00 USD | 388,650.00 USD | 8,500.00 USD | 8,330.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6060` | 336,360.00 USD | 336,360.00 USD | 0.00 USD | 0.00 USD | 55.47 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6070` | 358,820.00 USD | 358,820.00 USD | 7,700.00 USD | 14,690.00 USD | 11,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6080` | 325,210.00 USD | 325,210.00 USD | 2,970.00 USD | 23,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6080` | 336,300.00 USD | 336,300.00 USD | 2,860.00 USD | 0.00 USD | 9,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6090` | 299,090.00 USD | 299,090.00 USD | 6,430.00 USD | 11,280.00 USD | 14,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6100` | 267,150.00 USD | 267,150.00 USD | 14,420.00 USD | 14,280.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6100` | 324,010.00 USD | 324,010.00 USD | 21,400.00 USD | 47,430.00 USD | 25,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6110` | 221,180.00 USD | 221,180.00 USD | 1,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6120` | 219,750.00 USD | 219,750.00 USD | 23,580.00 USD | 2,470.00 USD | 19,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6120` | 229,960.00 USD | 229,960.00 USD | 35,760.00 USD | 5,720.00 USD | 18,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6130` | 174,500.00 USD | 174,500.00 USD | 2,140.00 USD | 12,430.00 USD | 22,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6140` | 137,150.00 USD | 137,150.00 USD | 53,460.00 USD | 18,080.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6140` | 169,930.00 USD | 169,930.00 USD | 51,550.00 USD | 8,040.00 USD | 10,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6150` | 61,570.00 USD | 61,570.00 USD | 14,190.00 USD | 7,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6160` | 39,560.00 USD | 39,560.00 USD | 25,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6160` | 99,640.00 USD | 99,640.00 USD | 12,920.00 USD | 16,340.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6170` | 13,910.00 USD | 13,910.00 USD | 0.00 USD | 0.00 USD | 13,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6180` | 65,700.00 USD | 65,700.00 USD | 20,870.00 USD | 2,610.00 USD | 365.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6200` | 41,850.00 USD | 41,850.00 USD | 23,430.00 USD | 0.00 USD | 18,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6220` | 27,950.00 USD | 27,950.00 USD | 4,760.00 USD | 22,640.00 USD | 542.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6240` | 28,040.00 USD | 28,040.00 USD | 0.00 USD | 0.00 USD | 90.21 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6260` | 95,350.00 USD | 95,350.00 USD | 67,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6280` | 95,780.00 USD | 95,780.00 USD | 0.00 USD | 0.00 USD | 431.03 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6285` | 10,370.00 USD | 11,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6290` | 2,020.00 USD | 2,020.00 USD | 0.00 USD | 2,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6300` | 10,470.00 USD | 10,470.00 USD | 0.00 USD | 3,430.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6300` | 106,240.00 USD | 106,240.00 USD | 0.00 USD | 0.00 USD | 10,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6310` | 37,400.00 USD | 37,400.00 USD | 11,740.00 USD | 3,970.00 USD | 11,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6320` | 69,360.00 USD | 69,360.00 USD | 31,880.00 USD | 0.00 USD | 78.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6330` | 125,320.00 USD | 125,320.00 USD | 17,300.00 USD | 5,390.00 USD | 33,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6340` | 209,010.00 USD | 209,010.00 USD | 32,460.00 USD | 2,420.00 USD | 48,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6340` | 174,910.00 USD | 174,910.00 USD | 68,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6350` | 267,500.00 USD | 267,500.00 USD | 51,360.00 USD | 0.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6360` | 397,240.00 USD | 397,240.00 USD | 63,010.00 USD | 2,470.00 USD | 64,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6360` | 266,370.00 USD | 266,370.00 USD | 34,320.00 USD | 0.00 USD | 57,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6370` | 433,130.00 USD | 433,130.00 USD | 0.00 USD | 5,770.00 USD | 30,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6380` | 457,360.00 USD | 457,360.00 USD | 0.00 USD | 19,010.00 USD | 5,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6380` | 305,900.00 USD | 305,900.00 USD | 0.00 USD | 0.00 USD | 39,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6390` | 526,830.00 USD | 526,830.00 USD | 18,790.00 USD | 3,690.00 USD | 47,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6400` | 642,810.00 USD | 642,810.00 USD | 57,170.00 USD | 28,050.00 USD | 30,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6400` | 327,130.00 USD | 327,130.00 USD | 0.00 USD | 7,510.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6410` | 691,950.00 USD | 691,950.00 USD | 32,400.00 USD | 9,300.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6420` | 795,520.00 USD | 795,520.00 USD | 69,490.00 USD | 14,860.00 USD | 19,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6420` | 434,320.00 USD | 434,320.00 USD | 55,350.00 USD | 35,430.00 USD | 16,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6430` | 878,670.00 USD | 878,670.00 USD | 35,700.00 USD | 17,300.00 USD | 30,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6440` | 991,420.00 USD | 991,420.00 USD | 39,760.00 USD | 23,720.00 USD | 49,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6440` | 521,770.00 USD | 521,770.00 USD | 44,690.00 USD | 24,820.00 USD | 17,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6450` | 1,110,000.00 USD | 1,110,000.00 USD | 70,250.00 USD | 9,920.00 USD | 36,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6460` | 1,180,000.00 USD | 1,180,000.00 USD | 57,400.00 USD | 9,320.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6460` | 879,190.00 USD | 879,190.00 USD | 172,610.00 USD | 46,630.00 USD | 138,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6470` | 1,280,000.00 USD | 1,280,000.00 USD | 74,410.00 USD | 17,210.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6475` | 209.47 USD | 12,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6480` | 1,400,000.00 USD | 1,400,000.00 USD | 112,500.00 USD | 6,780.00 USD | 151.61 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6480` | 1,030,000.00 USD | 1,030,000.00 USD | 86,440.00 USD | 26,520.00 USD | 33,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6490` | 1,480,000.00 USD | 1,480,000.00 USD | 66,830.00 USD | 1,230.00 USD | 9,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6500` | 1,550,000.00 USD | 1,550,000.00 USD | 64,920.00 USD | 5,920.00 USD | 128.67 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6500` | 1,230,000.00 USD | 1,230,000.00 USD | 73,560.00 USD | 0.00 USD | 132,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6510` | 1,620,000.00 USD | 1,620,000.00 USD | 55,500.00 USD | 0.00 USD | 11,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6520` | 1,720,000.00 USD | 1,720,000.00 USD | 93,550.00 USD | 9,040.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6520` | 1,650,000.00 USD | 1,650,000.00 USD | 298,050.00 USD | 10,910.00 USD | 105,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6530` | 1,740,000.00 USD | 1,740,000.00 USD | 11,510.00 USD | 3,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6540` | 1,770,000.00 USD | 1,770,000.00 USD | 24,280.00 USD | 0.00 USD | 10,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6540` | 1,730,000.00 USD | 1,730,000.00 USD | 15,730.00 USD | 4,440.00 USD | 61,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6550` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 6,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6560` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6560` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 5,380.00 USD | 1,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6570` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 59.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6580` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 3,310.00 USD | 25.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6580` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 28,280.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6590` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 5,890.00 USD | 164.02 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6600` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 8,400.00 USD | 59.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6600` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 15,500.00 USD | 770.13 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6610` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 142.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6620` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6620` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 507.07 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6630` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 39.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6640` | 1,820,000.00 USD | 1,820,000.00 USD | 11,190.00 USD | 0.00 USD | 126.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6640` | 1,820,000.00 USD | 1,820,000.00 USD | 33,660.00 USD | 0.00 USD | 753.62 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6650` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 3,160.00 USD | 17,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6660` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6660` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 6,770.00 USD | 816.74 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6670` | 1,870,000.00 USD | 1,870,000.00 USD | 18,850.00 USD | 0.00 USD | 24.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6680` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 44.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6680` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6690` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 3,550.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6700` | 1,910,000.00 USD | 1,910,000.00 USD | 8,830.00 USD | 1,920.00 USD | 24,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6700` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 217.49 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6710` | 1,960,000.00 USD | 1,960,000.00 USD | 41,970.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6720` | 1,920,000.00 USD | 1,920,000.00 USD | 58,470.00 USD | 0.00 USD | 30,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6730` | 1,990,000.00 USD | 1,990,000.00 USD | 24,320.00 USD | 3,670.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6740` | 2,070,000.00 USD | 2,070,000.00 USD | 64,370.00 USD | 7,120.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6740` | 1,960,000.00 USD | 1,960,000.00 USD | 39,730.00 USD | 0.00 USD | 164.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6750` | 2,120,000.00 USD | 2,120,000.00 USD | 28,700.00 USD | 4,300.00 USD | 12,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6760` | 2,140,000.00 USD | 2,140,000.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6760` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 77,970.00 USD | 33,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6770` | 2,170,000.00 USD | 2,170,000.00 USD | 14,540.00 USD | 6,110.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6780` | 2,230,000.00 USD | 2,230,000.00 USD | 33,610.00 USD | 12,680.00 USD | 8,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6780` | 2,170,000.00 USD | 2,170,000.00 USD | 63,600.00 USD | 14,400.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6790` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 18,610.00 USD | 14,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6800` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 686.25 USD | 2,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6800` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 16,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6810` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 1,940.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6820` | 2,320,000.00 USD | 2,320,000.00 USD | 22,600.00 USD | 16,590.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6820` | 2,270,000.00 USD | 2,270,000.00 USD | 32,570.00 USD | 53,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6830` | 2,410,000.00 USD | 2,410,000.00 USD | 24,570.00 USD | 26,560.00 USD | 36,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6840` | 2,500,000.00 USD | 2,500,000.00 USD | 45,780.00 USD | 25,860.00 USD | 13,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6840` | 2,480,000.00 USD | 2,480,000.00 USD | 57,890.00 USD | 54,300.00 USD | 102,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6850` | 2,560,000.00 USD | 2,560,000.00 USD | 49,540.00 USD | 5,780.00 USD | 10,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6860` | 2,620,000.00 USD | 2,620,000.00 USD | 40,250.00 USD | 4,380.00 USD | 14,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6860` | 2,560,000.00 USD | 2,560,000.00 USD | 49,930.00 USD | 14,540.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6870` | 2,690,000.00 USD | 2,690,000.00 USD | 63,220.00 USD | 1,160.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6880` | 2,740,000.00 USD | 2,740,000.00 USD | 14,350.00 USD | 11,160.00 USD | 25,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6880` | 2,620,000.00 USD | 2,620,000.00 USD | 38,030.00 USD | 17,300.00 USD | 131.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6890` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6900` | 2,790,000.00 USD | 2,790,000.00 USD | 18,600.00 USD | 4,030.00 USD | 21,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6900` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 15,510.00 USD | 16,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6910` | 2,860,000.00 USD | 2,860,000.00 USD | 28,860.00 USD | 1,730.00 USD | 39,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6920` | 2,890,000.00 USD | 2,890,000.00 USD | 16,800.00 USD | 0.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6920` | 2,780,000.00 USD | 2,780,000.00 USD | 69,620.00 USD | 2,090.00 USD | 61,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6930` | 2,900,000.00 USD | 2,900,000.00 USD | 10,030.00 USD | 0.00 USD | 168.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6940` | 2,920,000.00 USD | 2,920,000.00 USD | 11,230.00 USD | 2,090.00 USD | 9,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6940` | 2,840,000.00 USD | 2,840,000.00 USD | 14,220.00 USD | 0.00 USD | 42,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6950` | 2,960,000.00 USD | 2,960,000.00 USD | 22,480.00 USD | 4,460.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6960` | 3,020,000.00 USD | 3,020,000.00 USD | 58,370.00 USD | 6,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6960` | 2,910,000.00 USD | 2,910,000.00 USD | 59,960.00 USD | 0.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6970` | 3,060,000.00 USD | 3,060,000.00 USD | 33,460.00 USD | 4,780.00 USD | 34.66 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6980` | 3,070,000.00 USD | 3,070,000.00 USD | 9,140.00 USD | 4,100.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6980` | 2,960,000.00 USD | 2,960,000.00 USD | 35,980.00 USD | 16,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6990` | 3,090,000.00 USD | 3,090,000.00 USD | 5,180.00 USD | 4,830.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7000` | 3,130,000.00 USD | 3,130,000.00 USD | 18,240.00 USD | 4,020.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7000` | 3,030,000.00 USD | 3,030,000.00 USD | 29,740.00 USD | 0.00 USD | 40,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7010` | 3,140,000.00 USD | 3,140,000.00 USD | 15,520.00 USD | 0.00 USD | 73.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7020` | 3,160,000.00 USD | 3,160,000.00 USD | 14,360.00 USD | 0.00 USD | 22.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7020` | 3,120,000.00 USD | 3,120,000.00 USD | 29,810.00 USD | 0.00 USD | 53,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7030` | 3,170,000.00 USD | 3,170,000.00 USD | 4,330.00 USD | 0.00 USD | 10,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7040` | 3,210,000.00 USD | 3,210,000.00 USD | 29,930.00 USD | 2,630.00 USD | 8,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7040` | 3,310,000.00 USD | 3,310,000.00 USD | 95,520.00 USD | 0.00 USD | 96,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7050` | 3,260,000.00 USD | 3,260,000.00 USD | 29,790.00 USD | 2,660.00 USD | 18,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7060` | 3,290,000.00 USD | 3,290,000.00 USD | 8,590.00 USD | 3,860.00 USD | 13,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7060` | 3,570,000.00 USD | 3,570,000.00 USD | 47,840.00 USD | 33,490.00 USD | 178,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7070` | 3,350,000.00 USD | 3,350,000.00 USD | 19,980.00 USD | 21,860.00 USD | 17,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.7080` | 3,370,000.00 USD | 3,370,000.00 USD | 18,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7080` | 3,740,000.00 USD | 3,740,000.00 USD | 24,440.00 USD | 64,870.00 USD | 82,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7100` | 4,100,000.00 USD | 4,100,000.00 USD | 150,830.00 USD | 63,530.00 USD | 148,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7120` | 4,510,000.00 USD | 4,510,000.00 USD | 101,040.00 USD | 78,760.00 USD | 227,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7140` | 4,910,000.00 USD | 4,910,000.00 USD | 202,560.00 USD | 67,260.00 USD | 133,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7160` | 5,260,000.00 USD | 5,260,000.00 USD | 113,040.00 USD | 65,260.00 USD | 164,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7180` | 5,550,000.00 USD | 5,550,000.00 USD | 165,860.00 USD | 56,910.00 USD | 66,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7200` | 5,860,000.00 USD | 5,860,000.00 USD | 93,750.00 USD | 45,160.00 USD | 178,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7220` | 6,350,000.00 USD | 6,350,000.00 USD | 318,420.00 USD | 67,130.00 USD | 98,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7240` | 6,650,000.00 USD | 6,650,000.00 USD | 146,110.00 USD | 24,910.00 USD | 129,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7245` | 364.39 USD | 12,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7260` | 6,980,000.00 USD | 6,980,000.00 USD | 106,410.00 USD | 52,120.00 USD | 175,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7280` | 7,210,000.00 USD | 7,210,000.00 USD | 99,750.00 USD | 40,180.00 USD | 84,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7300` | 7,490,000.00 USD | 7,490,000.00 USD | 115,310.00 USD | 60,310.00 USD | 109,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7305` | 43,390.00 USD | 55,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7320` | 7,830,000.00 USD | 7,830,000.00 USD | 189,840.00 USD | 65,640.00 USD | 80,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7340` | 7,930,000.00 USD | 7,930,000.00 USD | 31,260.00 USD | 8,620.00 USD | 63,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7360` | 8,120,000.00 USD | 8,120,000.00 USD | 103,600.00 USD | 46,790.00 USD | 35,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7380` | 8,270,000.00 USD | 8,270,000.00 USD | 73,710.00 USD | 19,000.00 USD | 60,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7400` | 8,300,000.00 USD | 8,300,000.00 USD | 1,730.00 USD | 4,760.00 USD | 21,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7420` | 8,400,000.00 USD | 8,400,000.00 USD | 35,810.00 USD | 35,860.00 USD | 31,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7440` | 8,580,000.00 USD | 8,580,000.00 USD | 74,450.00 USD | 39,890.00 USD | 70,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7460` | 8,750,000.00 USD | 8,750,000.00 USD | 88,800.00 USD | 28,800.00 USD | 51,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7480` | 8,880,000.00 USD | 8,880,000.00 USD | 60,580.00 USD | 28,900.00 USD | 38,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7500` | 8,970,000.00 USD | 8,970,000.00 USD | 52,320.00 USD | 12,610.00 USD | 25,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7520` | 9,090,000.00 USD | 9,090,000.00 USD | 53,470.00 USD | 13,000.00 USD | 51,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7540` | 9,150,000.00 USD | 9,150,000.00 USD | 30,340.00 USD | 1,890.00 USD | 24,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7560` | 9,200,000.00 USD | 9,200,000.00 USD | 26,000.00 USD | 7,570.00 USD | 22,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7580` | 9,320,000.00 USD | 9,320,000.00 USD | 55,420.00 USD | 11,790.00 USD | 45,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7600` | 9,460,000.00 USD | 9,460,000.00 USD | 57,020.00 USD | 4,320.00 USD | 80,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7620` | 9,560,000.00 USD | 9,560,000.00 USD | 54,140.00 USD | 24,170.00 USD | 21,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7640` | 9,660,000.00 USD | 9,660,000.00 USD | 50,390.00 USD | 13,520.00 USD | 42,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7660` | 9,830,000.00 USD | 9,830,000.00 USD | 56,130.00 USD | 18,130.00 USD | 90,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7680` | 9,970,000.00 USD | 9,970,000.00 USD | 66,570.00 USD | 32,520.00 USD | 40,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7700` | 10,030,000.00 USD | 10,030,000.00 USD | 10,860.00 USD | 12,600.00 USD | 41,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7720` | 10,150,000.00 USD | 10,150,000.00 USD | 58,380.00 USD | 32,920.00 USD | 25,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7725` | 165.62 USD | 56,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7740` | 10,260,000.00 USD | 10,260,000.00 USD | 51,600.00 USD | 25,250.00 USD | 35,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7760` | 10,320,000.00 USD | 10,320,000.00 USD | 38,170.00 USD | 2,980.00 USD | 12,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7780` | 10,440,000.00 USD | 10,440,000.00 USD | 68,800.00 USD | 20,860.00 USD | 32,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7800` | 10,600,000.00 USD | 10,600,000.00 USD | 60,490.00 USD | 21,940.00 USD | 80,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7820` | 10,720,000.00 USD | 10,720,000.00 USD | 90,020.00 USD | 17,850.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7840` | 10,800,000.00 USD | 10,800,000.00 USD | 72,650.00 USD | 7,150.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7860` | 10,870,000.00 USD | 10,870,000.00 USD | 32,690.00 USD | 9,290.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7880` | 10,920,000.00 USD | 10,920,000.00 USD | 11,900.00 USD | 10,710.00 USD | 22,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7900` | 11,000,000.00 USD | 11,000,000.00 USD | 44,050.00 USD | 16,710.00 USD | 17,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7910` | 11,030,000.00 USD | 11,030,000.00 USD | 30,620.00 USD | 5,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8005` | 19,120.00 USD | 75,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8665` | 378.95 USD | 75,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8845` | 117.46 USD | 75,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8985` | 24,220.00 USD | 99,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9695` | 17,110.00 USD | 116,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9935` | 166.01 USD | 117,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.02` | 25,970.00 USD | 143,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 5,250.00 USD | 148,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 479.74 USD | 148,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.12` | 2,800.00 USD | 151,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.12` | 85,650.00 USD | 237,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.17` | 501.44 USD | 237,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.18` | 132.71 USD | 237,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 227.46 USD | 238,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 199.98 USD | 238,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1395` | 207,740.00 USD | 0.00 USD | 419.65 USD | `-77.36%` | `3,008.22` |
| `Live` | `Long` | `0.1465` | 207,320.00 USD | 0.00 USD | 1,070.00 USD | `-76.23%` | `7,272.07` |
| `Live` | `Long` | `0.1605` | 206,260.00 USD | 0.00 USD | 222.83 USD | `-73.95%` | `1,388.32` |
| `Live` | `Long` | `0.1875` | 206,040.00 USD | 0.00 USD | 269.27 USD | `-69.57%` | `1,436.09` |
| `Live` | `Long` | `0.2185` | 205,770.00 USD | 0.00 USD | 226.83 USD | `-64.54%` | `1,038.12` |
| `Live` | `Long` | `0.2355` | 205,540.00 USD | 0.00 USD | 2,660.00 USD | `-61.78%` | `11,284.25` |
| `Live` | `Long` | `0.2415` | 202,880.00 USD | 0.00 USD | 243.01 USD | `-60.81%` | `1,006.27` |
| `Live` | `Long` | `0.2425` | 202,640.00 USD | 0.00 USD | 1,460.00 USD | `-60.65%` | `6,000.00` |
| `Live` | `Long` | `0.3105` | 201,180.00 USD | 0.00 USD | 105.38 USD | `-49.61%` | `339.38` |
| `Live` | `Long` | `0.3175` | 201,080.00 USD | 0.00 USD | 1,590.00 USD | `-48.47%` | `5,000.00` |
| `Live` | `Long` | `0.3305` | 199,490.00 USD | 0.00 USD | 9,950.00 USD | `-46.36%` | `30,091.58` |
| `Live` | `Long` | `0.3395` | 189,550.00 USD | 0.00 USD | 679.34 USD | `-44.90%` | `2,001.00` |
| `Live` | `Long` | `0.3545` | 188,870.00 USD | 0.00 USD | 177.25 USD | `-42.47%` | `500.00` |
| `Live` | `Long` | `0.3585` | 188,690.00 USD | 0.00 USD | 12,850.00 USD | `-41.82%` | `35,856.81` |
| `Live` | `Long` | `0.3675` | 175,830.00 USD | 0.00 USD | 189.99 USD | `-40.36%` | `516.98` |
| `Live` | `Long` | `0.3785` | 175,640.00 USD | 0.00 USD | 567.75 USD | `-38.58%` | `1,500.00` |
| `Live` | `Long` | `0.3905` | 175,080.00 USD | 0.00 USD | 359.26 USD | `-36.63%` | `919.99` |
| `Live` | `Long` | `0.3955` | 174,720.00 USD | 0.00 USD | 2,640.00 USD | `-35.82%` | `6,686.27` |
| `Live` | `Long` | `0.3995` | 172,070.00 USD | 0.00 USD | 271.06 USD | `-35.17%` | `678.49` |
| `Live` | `Long` | `0.4035` | 171,800.00 USD | 0.00 USD | 282.45 USD | `-34.52%` | `700.00` |
| `Live` | `Long` | `0.4125` | 171,520.00 USD | 0.00 USD | 1,070.00 USD | `-33.06%` | `2,600.00` |
| `Live` | `Long` | `0.4135` | 170,450.00 USD | 0.00 USD | 1,600.00 USD | `-32.90%` | `3,868.97` |
| `Live` | `Long` | `0.4185` | 168,850.00 USD | 0.00 USD | 630.86 USD | `-32.08%` | `1,507.44` |
| `Live` | `Long` | `0.4255` | 168,220.00 USD | 0.00 USD | 224.96 USD | `-30.95%` | `528.69` |
| `Live` | `Long` | `0.4395` | 167,990.00 USD | 0.00 USD | 444.97 USD | `-28.68%` | `1,012.44` |
| `Live` | `Long` | `0.4435` | 167,550.00 USD | 0.00 USD | 5,510.00 USD | `-28.03%` | `12,426.15` |
| `Live` | `Long` | `0.4475` | 162,040.00 USD | 0.00 USD | 226.63 USD | `-27.38%` | `506.43` |
| `Live` | `Long` | `0.4515` | 161,810.00 USD | 0.00 USD | 27,090.00 USD | `-26.73%` | `60,000.00` |
| `Live` | `Long` | `0.4535` | 134,720.00 USD | 0.00 USD | 5,970.00 USD | `-26.40%` | `13,168.58` |
| `Live` | `Long` | `0.4605` | 128,750.00 USD | 0.00 USD | 430.79 USD | `-25.27%` | `935.49` |
| `Live` | `Long` | `0.4615` | 128,320.00 USD | 0.00 USD | 595.82 USD | `-25.11%` | `1,291.05` |
| `Live` | `Long` | `0.4625` | 127,720.00 USD | 0.00 USD | 1,460.00 USD | `-24.94%` | `3,156.35` |
| `Live` | `Long` | `0.4645` | 126,260.00 USD | 0.00 USD | 876.05 USD | `-24.62%` | `1,886.00` |
| `Live` | `Long` | `0.4685` | 125,380.00 USD | 0.00 USD | 1,350.00 USD | `-23.97%` | `2,881.36` |
| `Live` | `Long` | `0.4765` | 124,030.00 USD | 0.00 USD | 4,400.00 USD | `-22.67%` | `9,243.24` |
| `Live` | `Long` | `0.4835` | 119,630.00 USD | 0.00 USD | 135.33 USD | `-21.54%` | `279.90` |
| `Live` | `Long` | `0.4855` | 119,500.00 USD | 0.00 USD | 181.88 USD | `-21.21%` | `374.62` |
| `Live` | `Long` | `0.4865` | 119,310.00 USD | 0.00 USD | 3,330.00 USD | `-21.05%` | `6,847.47` |
| `Live` | `Long` | `0.4925` | 115,980.00 USD | 0.00 USD | 10,520.00 USD | `-20.07%` | `21,364.96` |
| `Live` | `Long` | `0.4935` | 105,460.00 USD | 0.00 USD | 1,580.00 USD | `-19.91%` | `3,199.85` |
| `Live` | `Long` | `0.4945` | 103,880.00 USD | 0.00 USD | 7,030.00 USD | `-19.75%` | `14,223.31` |
| `Live` | `Long` | `0.4955` | 96,850.00 USD | 0.00 USD | 3,180.00 USD | `-19.59%` | `6,422.59` |
| `Live` | `Long` | `0.4965` | 93,660.00 USD | 0.00 USD | 143.19 USD | `-19.43%` | `288.40` |
| `Live` | `Long` | `0.4975` | 93,520.00 USD | 0.00 USD | 667.49 USD | `-19.26%` | `1,341.68` |
| `Live` | `Long` | `0.4985` | 92,850.00 USD | 0.00 USD | 429.90 USD | `-19.10%` | `862.38` |
| `Live` | `Long` | `0.5075` | 92,420.00 USD | 0.00 USD | 303.42 USD | `-17.64%` | `597.87` |
| `Live` | `Long` | `0.5085` | 92,120.00 USD | 0.00 USD | 102.82 USD | `-17.48%` | `202.20` |
| `Live` | `Long` | `0.5105` | 92,020.00 USD | 0.00 USD | 519.77 USD | `-17.15%` | `1,018.15` |
| `Live` | `Long` | `0.5125` | 91,500.00 USD | 0.00 USD | 248.05 USD | `-16.83%` | `484.00` |
| `Live` | `Long` | `0.5135` | 91,250.00 USD | 0.00 USD | 298.60 USD | `-16.67%` | `581.49` |
| `Live` | `Long` | `0.5175` | 90,950.00 USD | 0.00 USD | 9,440.00 USD | `-16.02%` | `18,249.92` |
| `Live` | `Long` | `0.5185` | 81,510.00 USD | 0.00 USD | 281.56 USD | `-15.86%` | `543.02` |
| `Live` | `Long` | `0.5245` | 81,230.00 USD | 0.00 USD | 209.80 USD | `-14.88%` | `400.00` |
| `Live` | `Long` | `0.5295` | 81,020.00 USD | 0.00 USD | 1,840.00 USD | `-14.07%` | `3,467.51` |
| `Live` | `Long` | `0.5315` | 79,180.00 USD | 0.00 USD | 11,510.00 USD | `-13.75%` | `21,664.95` |
| `Live` | `Long` | `0.5325` | 67,660.00 USD | 0.00 USD | 2,260.00 USD | `-13.58%` | `4,240.81` |
| `Live` | `Long` | `0.5335` | 65,410.00 USD | 0.00 USD | 163.22 USD | `-13.42%` | `305.95` |
| `Live` | `Long` | `0.5445` | 65,240.00 USD | 0.00 USD | 855.28 USD | `-11.64%` | `1,570.77` |
| `Live` | `Long` | `0.5475` | 64,390.00 USD | 0.00 USD | 1,630.00 USD | `-11.15%` | `2,968.46` |
| `Live` | `Long` | `0.5545` | 62,760.00 USD | 0.00 USD | 47,450.00 USD | `-10.01%` | `85,578.81` |
| `Live` | `Long` | `0.5585` | 15,310.00 USD | 0.00 USD | 10,520.00 USD | `-9.36%` | `18,834.52` |
| `Live` | `Long` | `0.5615` | 4,790.00 USD | 0.00 USD | 258.48 USD | `-8.88%` | `460.33` |
| `Live` | `Long` | `0.5635` | 4,530.00 USD | 0.00 USD | 244.90 USD | `-8.55%` | `434.61` |
| `Live` | `Long` | `0.5655` | 4,290.00 USD | 0.00 USD | 1,920.00 USD | `-8.23%` | `3,394.98` |
| `Live` | `Long` | `0.5665` | 2,370.00 USD | 0.00 USD | 1,370.00 USD | `-8.07%` | `2,421.90` |
| `Live` | `Long` | `0.5715` | 995.18 USD | 0.00 USD | 289.08 USD | `-7.25%` | `505.82` |
| `Live` | `Long` | `0.5745` | 706.11 USD | 0.00 USD | 706.11 USD | `-6.77%` | `1,229.08` |
| `Live` | `Short` | `0.6285` | 10,370.00 USD | 10,370.00 USD | 0.00 USD | `+2.00%` | `16,500.00` |
| `Live` | `Short` | `0.6475` | 10,580.00 USD | 209.47 USD | 0.00 USD | `+5.08%` | `323.51` |
| `Live` | `Short` | `0.6495` | 10,740.00 USD | 157.93 USD | 0.00 USD | `+5.40%` | `243.15` |
| `Live` | `Short` | `0.7245` | 11,100.00 USD | 364.39 USD | 0.00 USD | `+17.58%` | `502.96` |
| `Live` | `Short` | `0.7295` | 54,440.00 USD | 43,330.00 USD | 0.00 USD | `+18.39%` | `59,401.36` |
| `Live` | `Short` | `0.7725` | 54,600.00 USD | 165.62 USD | 0.00 USD | `+25.37%` | `214.40` |
| `Live` | `Short` | `0.8005` | 73,720.00 USD | 19,120.00 USD | 0.00 USD | `+29.91%` | `23,882.80` |
| `Live` | `Short` | `0.8665` | 74,100.00 USD | 378.95 USD | 0.00 USD | `+40.62%` | `437.33` |
| `Live` | `Short` | `0.9065` | 98,530.00 USD | 24,440.00 USD | 0.00 USD | `+47.11%` | `26,955.72` |
| `Live` | `Short` | `0.9935` | 98,700.00 USD | 166.01 USD | 0.00 USD | `+61.23%` | `167.10` |
| `Live` | `Short` | `0.9995` | 116,340.00 USD | 17,640.00 USD | 0.00 USD | `+62.20%` | `17,648.14` |
| `Live` | `Short` | `1.02` | 142,310.00 USD | 25,970.00 USD | 0.00 USD | `+65.77%` | `25,423.72` |
| `Live` | `Short` | `1.04` | 147,520.00 USD | 5,210.00 USD | 0.00 USD | `+69.18%` | `5,000.00` |
| `Live` | `Short` | `1.09` | 230,570.00 USD | 83,050.00 USD | 0.00 USD | `+76.65%` | `76,300.00` |
| `Live` | `Short` | `1.09` | 231,050.00 USD | 479.74 USD | 0.00 USD | `+77.13%` | `439.52` |
| `Live` | `Short` | `1.12` | 233,850.00 USD | 2,800.00 USD | 0.00 USD | `+81.68%` | `2,500.00` |
| `Live` | `Short` | `1.17` | 234,350.00 USD | 501.44 USD | 0.00 USD | `+90.44%` | `427.30` |
| `Live` | `Short` | `1.19` | 234,580.00 USD | 227.46 USD | 0.00 USD | `+92.55%` | `191.71` |
| `Live` | `Short` | `1.19` | 234,780.00 USD | 199.98 USD | 0.00 USD | `+92.88%` | `168.26` |
| `Live` | `Short` | `1.20` | 234,880.00 USD | 100.76 USD | 0.00 USD | `+94.82%` | `83.93` |
| `Live` | `Short` | `1.22` | 235,680.00 USD | 796.83 USD | 0.00 USD | `+98.23%` | `652.34` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.3505` | 165,510.00 USD | 0.00 USD | 340.19 USD | `-43.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4635` | 165,170.00 USD | 0.00 USD | 104.57 USD | `-24.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4955` | 165,070.00 USD | 0.00 USD | 111.62 USD | `-19.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4965` | 164,950.00 USD | 0.00 USD | 111.85 USD | `-19.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 164,840.00 USD | 0.00 USD | 67,850.00 USD | `-18.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5015` | 97,000.00 USD | 0.00 USD | 112.97 USD | `-18.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5065` | 96,880.00 USD | 0.00 USD | 225.65 USD | `-17.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5085` | 96,660.00 USD | 0.00 USD | 101.97 USD | `-17.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5115` | 96,560.00 USD | 0.00 USD | 111.69 USD | `-16.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5125` | 96,440.00 USD | 0.00 USD | 5,380.00 USD | `-16.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 91,060.00 USD | 0.00 USD | 115.47 USD | `-16.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5175` | 90,950.00 USD | 0.00 USD | 116.58 USD | `-16.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5185` | 90,830.00 USD | 0.00 USD | 116.96 USD | `-15.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5205` | 90,710.00 USD | 0.00 USD | 539.96 USD | `-15.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5225` | 90,170.00 USD | 0.00 USD | 117.70 USD | `-15.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5235` | 90,060.00 USD | 0.00 USD | 117.93 USD | `-15.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5305` | 89,940.00 USD | 0.00 USD | 770.19 USD | `-13.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5445` | 89,170.00 USD | 0.00 USD | 8,750.00 USD | `-11.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5455` | 80,410.00 USD | 0.00 USD | 8,150.00 USD | `-11.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5485` | 72,260.00 USD | 0.00 USD | 4,500.00 USD | `-10.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5515` | 67,770.00 USD | 0.00 USD | 126.71 USD | `-10.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5525` | 67,640.00 USD | 0.00 USD | 126.90 USD | `-10.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5555` | 67,510.00 USD | 0.00 USD | 33,000.00 USD | `-9.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5565` | 34,520.00 USD | 0.00 USD | 173.58 USD | `-9.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5595` | 34,340.00 USD | 0.00 USD | 10,540.00 USD | `-9.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 23,810.00 USD | 0.00 USD | 339.84 USD | `-9.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5625` | 23,470.00 USD | 0.00 USD | 930.52 USD | `-8.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5655` | 22,530.00 USD | 0.00 USD | 127.62 USD | `-8.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5695` | 22,410.00 USD | 0.00 USD | 127.30 USD | `-7.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5705` | 22,280.00 USD | 0.00 USD | 9,410.00 USD | `-7.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5715` | 12,870.00 USD | 0.00 USD | 127.63 USD | `-7.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5735` | 12,740.00 USD | 0.00 USD | 151.62 USD | `-6.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5755` | 12,590.00 USD | 0.00 USD | 999.82 USD | `-6.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5775` | 11,590.00 USD | 0.00 USD | 1,710.00 USD | `-6.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5785` | 9,870.00 USD | 0.00 USD | 127.36 USD | `-6.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5815` | 9,750.00 USD | 0.00 USD | 127.27 USD | `-5.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5835` | 9,620.00 USD | 0.00 USD | 999.65 USD | `-5.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5845` | 8,620.00 USD | 0.00 USD | 533.37 USD | `-5.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5865` | 8,090.00 USD | 0.00 USD | 128.36 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5875` | 7,960.00 USD | 0.00 USD | 128.34 USD | `-4.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5895` | 7,830.00 USD | 0.00 USD | 128.45 USD | `-4.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5905` | 7,700.00 USD | 0.00 USD | 127.30 USD | `-4.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5925` | 7,570.00 USD | 0.00 USD | 265.69 USD | `-3.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5975` | 7,310.00 USD | 0.00 USD | 597.80 USD | `-3.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 6,710.00 USD | 0.00 USD | 953.02 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6045` | 5,760.00 USD | 0.00 USD | 999.99 USD | `-1.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 4,760.00 USD | 0.00 USD | 1,510.00 USD | `-1.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6065` | 3,250.00 USD | 0.00 USD | 1,910.00 USD | `-1.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6085` | 1,340.00 USD | 0.00 USD | 301.32 USD | `-1.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6115` | 1,040.00 USD | 0.00 USD | 629.83 USD | `-0.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6135` | 410.30 USD | 0.00 USD | 410.30 USD | `-0.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6175` | 519.13 USD | 519.13 USD | 0.00 USD | `+0.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6185` | 696.72 USD | 177.58 USD | 0.00 USD | `+0.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6205` | 1,820.00 USD | 1,120.00 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6225` | 2,820.00 USD | 1,000.00 USD | 0.00 USD | `+1.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6275` | 3,250.00 USD | 433.11 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6285` | 3,720.00 USD | 469.94 USD | 0.00 USD | `+2.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 8,150.00 USD | 4,430.00 USD | 0.00 USD | `+2.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 8,420.00 USD | 269.44 USD | 0.00 USD | `+2.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6335` | 16,820.00 USD | 8,390.00 USD | 0.00 USD | `+2.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6345` | 17,090.00 USD | 276.40 USD | 0.00 USD | `+2.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6395` | 18,290.00 USD | 1,200.00 USD | 0.00 USD | `+3.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6405` | 18,440.00 USD | 145.91 USD | 0.00 USD | `+3.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6445` | 18,560.00 USD | 121.42 USD | 0.00 USD | `+4.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6465` | 18,970.00 USD | 410.21 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6485` | 19,410.00 USD | 447.03 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6505` | 19,980.00 USD | 567.58 USD | 0.00 USD | `+5.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6525` | 20,150.00 USD | 172.51 USD | 0.00 USD | `+5.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6535` | 20,500.00 USD | 349.76 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6555` | 24,580.00 USD | 4,080.00 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6585` | 26,020.00 USD | 1,440.00 USD | 0.00 USD | `+6.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6595` | 26,770.00 USD | 746.46 USD | 0.00 USD | `+7.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6605` | 27,350.00 USD | 580.23 USD | 0.00 USD | `+7.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6635` | 27,640.00 USD | 289.66 USD | 0.00 USD | `+7.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6645` | 27,900.00 USD | 262.60 USD | 0.00 USD | `+7.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6655` | 28,180.00 USD | 283.50 USD | 0.00 USD | `+8.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6675` | 28,470.00 USD | 290.78 USD | 0.00 USD | `+8.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6685` | 28,650.00 USD | 170.95 USD | 0.00 USD | `+8.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6695` | 30,310.00 USD | 1,670.00 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6705` | 30,480.00 USD | 162.91 USD | 0.00 USD | `+8.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6715` | 30,680.00 USD | 202.63 USD | 0.00 USD | `+8.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6725` | 32,350.00 USD | 1,670.00 USD | 0.00 USD | `+9.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6745` | 32,950.00 USD | 598.31 USD | 0.00 USD | `+9.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6755` | 33,310.00 USD | 361.53 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 33,470.00 USD | 154.30 USD | 0.00 USD | `+9.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6805` | 33,680.00 USD | 214.20 USD | 0.00 USD | `+10.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6815` | 44,240.00 USD | 10,560.00 USD | 0.00 USD | `+10.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6825` | 44,350.00 USD | 112.49 USD | 0.00 USD | `+10.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6845` | 45,490.00 USD | 1,130.00 USD | 0.00 USD | `+11.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6875` | 45,630.00 USD | 140.41 USD | 0.00 USD | `+11.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6885` | 46,140.00 USD | 514.80 USD | 0.00 USD | `+11.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6915` | 46,240.00 USD | 101.96 USD | 0.00 USD | `+12.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6925` | 47,270.00 USD | 1,020.00 USD | 0.00 USD | `+12.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6945` | 47,880.00 USD | 610.10 USD | 0.00 USD | `+12.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6955` | 47,980.00 USD | 101.38 USD | 0.00 USD | `+12.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6965` | 48,770.00 USD | 789.18 USD | 0.00 USD | `+13.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6985` | 48,870.00 USD | 102.99 USD | 0.00 USD | `+13.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7005` | 48,980.00 USD | 111.08 USD | 0.00 USD | `+13.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7015` | 49,670.00 USD | 694.49 USD | 0.00 USD | `+13.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7095` | 49,810.00 USD | 132.99 USD | 0.00 USD | `+15.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7115` | 49,930.00 USD | 122.04 USD | 0.00 USD | `+15.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7165` | 51,760.00 USD | 1,830.00 USD | 0.00 USD | `+16.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7195` | 51,950.00 USD | 183.26 USD | 0.00 USD | `+16.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7205` | 52,100.00 USD | 147.15 USD | 0.00 USD | `+16.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7265` | 58,390.00 USD | 6,290.00 USD | 0.00 USD | `+17.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7275` | 58,700.00 USD | 309.91 USD | 0.00 USD | `+18.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7325` | 58,860.00 USD | 165.17 USD | 0.00 USD | `+18.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7345` | 59,890.00 USD | 1,030.00 USD | 0.00 USD | `+19.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7405` | 60,620.00 USD | 733.09 USD | 0.00 USD | `+20.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7415` | 60,780.00 USD | 156.98 USD | 0.00 USD | `+20.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7445` | 60,960.00 USD | 185.43 USD | 0.00 USD | `+20.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7455` | 63,130.00 USD | 2,170.00 USD | 0.00 USD | `+20.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7475` | 63,450.00 USD | 318.43 USD | 0.00 USD | `+21.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7505` | 63,590.00 USD | 141.39 USD | 0.00 USD | `+21.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7565` | 67,700.00 USD | 4,120.00 USD | 0.00 USD | `+22.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7575` | 68,220.00 USD | 511.82 USD | 0.00 USD | `+22.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7615` | 69,090.00 USD | 875.23 USD | 0.00 USD | `+23.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7635` | 69,200.00 USD | 103.35 USD | 0.00 USD | `+23.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7665` | 69,320.00 USD | 127.48 USD | 0.00 USD | `+24.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7675` | 69,420.00 USD | 101.61 USD | 0.00 USD | `+24.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7695` | 69,610.00 USD | 186.97 USD | 0.00 USD | `+24.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7705` | 69,720.00 USD | 109.43 USD | 0.00 USD | `+25.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7775` | 69,890.00 USD | 166.70 USD | 0.00 USD | `+26.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7815` | 71,020.00 USD | 1,140.00 USD | 0.00 USD | `+26.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7865` | 77,340.00 USD | 6,310.00 USD | 0.00 USD | `+27.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8125` | 89,410.00 USD | 12,070.00 USD | 0.00 USD | `+31.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8265` | 91,060.00 USD | 1,650.00 USD | 0.00 USD | `+34.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8335` | 91,990.00 USD | 929.08 USD | 0.00 USD | `+35.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8475` | 132,580.00 USD | 40,590.00 USD | 0.00 USD | `+37.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8505` | 149,320.00 USD | 16,740.00 USD | 0.00 USD | `+38.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8515` | 162,040.00 USD | 12,720.00 USD | 0.00 USD | `+38.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8525` | 173,820.00 USD | 11,780.00 USD | 0.00 USD | `+38.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8725` | 173,980.00 USD | 159.86 USD | 0.00 USD | `+41.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 174,680.00 USD | 702.20 USD | 0.00 USD | `+46.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 174,880.00 USD | 193.62 USD | 0.00 USD | `+47.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 175,300.00 USD | 424.63 USD | 0.00 USD | `+51.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 178,090.00 USD | 2,790.00 USD | 0.00 USD | `+52.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 178,440.00 USD | 340.54 USD | 0.00 USD | `+54.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 178,540.00 USD | 108.83 USD | 0.00 USD | `+56.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 178,690.00 USD | 145.72 USD | 0.00 USD | `+57.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 180,720.00 USD | 2,030.00 USD | 0.00 USD | `+60.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 180,860.00 USD | 136.10 USD | 0.00 USD | `+62.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 181,410.00 USD | 550.48 USD | 0.00 USD | `+62.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 181,720.00 USD | 314.99 USD | 0.00 USD | `+66.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 182,330.00 USD | 602.17 USD | 0.00 USD | `+70.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 182,690.00 USD | 360.61 USD | 0.00 USD | `+72.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 183,630.00 USD | 942.77 USD | 0.00 USD | `+75.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 184,030.00 USD | 397.19 USD | 0.00 USD | `+78.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 184,550.00 USD | 525.37 USD | 0.00 USD | `+99.53%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.5320` | 869,060.00 USD | 0.00 USD | 869,060.00 USD | 11,240.00 USD | 0.00 USD | 3,480.00 USD |
| `7D` | `0.5340` | 854,350.00 USD | 0.00 USD | 854,350.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD |
| `7D` | `0.5360` | 851,740.00 USD | 0.00 USD | 851,740.00 USD | 2,440.00 USD | 3,040.00 USD | 44.79 USD |
| `7D` | `0.5380` | 846,220.00 USD | 0.00 USD | 846,220.00 USD | 0.00 USD | 1,550.00 USD | 2,900.00 USD |
| `7D` | `0.5400` | 841,770.00 USD | 0.00 USD | 841,770.00 USD | 0.00 USD | 0.00 USD | 70.86 USD |
| `7D` | `0.5420` | 841,700.00 USD | 0.00 USD | 841,700.00 USD | 7,660.00 USD | 1,290.00 USD | 2,880.00 USD |
| `7D` | `0.5440` | 829,880.00 USD | 0.00 USD | 829,880.00 USD | 0.00 USD | 1,150.00 USD | 6,990.00 USD |
| `7D` | `0.5460` | 821,740.00 USD | 0.00 USD | 821,740.00 USD | 2,250.00 USD | 3,030.00 USD | 5,150.00 USD |
| `7D` | `0.5480` | 811,300.00 USD | 0.00 USD | 811,300.00 USD | 2,000.00 USD | 795.70 USD | 4,490.00 USD |
| `1D` | `0.5500` | 839,890.00 USD | 0.00 USD | 839,890.00 USD | 0.00 USD | 0.00 USD | 19.90 USD |
| `7D` | `0.5500` | 804,020.00 USD | 0.00 USD | 804,020.00 USD | 5,990.00 USD | 1,440.00 USD | 6,700.00 USD |
| `1D` | `0.5510` | 839,870.00 USD | 0.00 USD | 839,870.00 USD | 0.00 USD | 0.00 USD | 849.87 USD |
| `1D` | `0.5520` | 839,020.00 USD | 0.00 USD | 839,020.00 USD | 0.00 USD | 0.00 USD | 432.53 USD |
| `7D` | `0.5520` | 789,890.00 USD | 0.00 USD | 789,890.00 USD | 4,110.00 USD | 1,920.00 USD | 1,880.00 USD |
| `1D` | `0.5530` | 838,590.00 USD | 0.00 USD | 838,590.00 USD | 1,260.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.5540` | 837,320.00 USD | 0.00 USD | 837,320.00 USD | 528.00 USD | 1,320.00 USD | 7.66 USD |
| `7D` | `0.5540` | 781,970.00 USD | 0.00 USD | 781,970.00 USD | 12,840.00 USD | 4,860.00 USD | 18,520.00 USD |
| `1D` | `0.5550` | 835,470.00 USD | 0.00 USD | 835,470.00 USD | 557.27 USD | 201.08 USD | 41.02 USD |
| `1D` | `0.5560` | 834,670.00 USD | 0.00 USD | 834,670.00 USD | 0.00 USD | 686.25 USD | 479.50 USD |
| `7D` | `0.5560` | 745,750.00 USD | 0.00 USD | 745,750.00 USD | 13,490.00 USD | 1,920.00 USD | 6,200.00 USD |
| `1D` | `0.5570` | 833,500.00 USD | 0.00 USD | 833,500.00 USD | 0.00 USD | 1,940.00 USD | 2,320.00 USD |
| `1D` | `0.5580` | 829,240.00 USD | 0.00 USD | 829,240.00 USD | 1,100.00 USD | 2,960.00 USD | 1,240.00 USD |
| `7D` | `0.5580` | 724,150.00 USD | 0.00 USD | 724,150.00 USD | 6,000.00 USD | 6,820.00 USD | 18,300.00 USD |
| `1D` | `0.5590` | 823,940.00 USD | 0.00 USD | 823,940.00 USD | 0.00 USD | 1,080.00 USD | 15.63 USD |
| `1D` | `0.5600` | 822,850.00 USD | 0.00 USD | 822,850.00 USD | 1,550.00 USD | 1,830.00 USD | 2,550.00 USD |
| `7D` | `0.5600` | 693,030.00 USD | 0.00 USD | 693,030.00 USD | 4,070.00 USD | 8,160.00 USD | 2,480.00 USD |
| `1D` | `0.5610` | 816,920.00 USD | 0.00 USD | 816,920.00 USD | 0.00 USD | 0.00 USD | 772.54 USD |
| `1D` | `0.5620` | 816,150.00 USD | 0.00 USD | 816,150.00 USD | 0.00 USD | 776.64 USD | 2,180.00 USD |
| `7D` | `0.5620` | 678,320.00 USD | 0.00 USD | 678,320.00 USD | 19,480.00 USD | 7,420.00 USD | 11,580.00 USD |
| `1D` | `0.5630` | 813,190.00 USD | 0.00 USD | 813,190.00 USD | 0.00 USD | 1,560.00 USD | 4,600.00 USD |
| `1D` | `0.5640` | 807,030.00 USD | 0.00 USD | 807,030.00 USD | 4,020.00 USD | 2,420.00 USD | 12.64 USD |
| `7D` | `0.5640` | 639,840.00 USD | 0.00 USD | 639,840.00 USD | 2,950.00 USD | 741.21 USD | 19.99 USD |
| `7D` | `0.5660` | 636,130.00 USD | 0.00 USD | 636,130.00 USD | 11,490.00 USD | 2,990.00 USD | 4,430.00 USD |
| `7D` | `0.5680` | 617,230.00 USD | 0.00 USD | 617,230.00 USD | 5,100.00 USD | 0.00 USD | 2,900.00 USD |
| `7D` | `0.5700` | 609,240.00 USD | 0.00 USD | 609,240.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD |
| `1D` | `0.5710` | 800,570.00 USD | 0.00 USD | 800,570.00 USD | 0.00 USD | 2,350.00 USD | 0.00 USD |
| `7D` | `0.5720` | 606,660.00 USD | 0.00 USD | 606,660.00 USD | 0.00 USD | 4,370.00 USD | 1,350.00 USD |
| `7D` | `0.5740` | 600,940.00 USD | 0.00 USD | 600,940.00 USD | 21,620.00 USD | 1,100.00 USD | 1,670.00 USD |
| `7D` | `0.5760` | 576,540.00 USD | 0.00 USD | 576,540.00 USD | 2,150.00 USD | 0.00 USD | 18.31 USD |
| `1D` | `0.5770` | 798,220.00 USD | 0.00 USD | 798,220.00 USD | 0.00 USD | 0.00 USD | 34.98 USD |
| `1D` | `0.5780` | 798,180.00 USD | 0.00 USD | 798,180.00 USD | 0.00 USD | 0.00 USD | 59.63 USD |
| `7D` | `0.5780` | 574,370.00 USD | 0.00 USD | 574,370.00 USD | 0.00 USD | 0.00 USD | 1,530.00 USD |
| `7D` | `0.5800` | 572,840.00 USD | 0.00 USD | 572,840.00 USD | 1,610.00 USD | 0.00 USD | 2,850.00 USD |
| `1D` | `0.5820` | 798,120.00 USD | 0.00 USD | 798,120.00 USD | 0.00 USD | 1,000.00 USD | 0.00 USD |
| `7D` | `0.5820` | 568,390.00 USD | 0.00 USD | 568,390.00 USD | 0.00 USD | 0.00 USD | 6,660.00 USD |
| `1D` | `0.5830` | 797,120.00 USD | 0.00 USD | 797,120.00 USD | 0.00 USD | 0.00 USD | 24.36 USD |
| `1D` | `0.5840` | 797,100.00 USD | 0.00 USD | 797,100.00 USD | 0.00 USD | 0.00 USD | 44.63 USD |
| `1D` | `0.5850` | 797,050.00 USD | 0.00 USD | 797,050.00 USD | 0.00 USD | 0.00 USD | 18.95 USD |
| `1D` | `0.5860` | 797,030.00 USD | 0.00 USD | 797,030.00 USD | 0.00 USD | 658.88 USD | 14,870.00 USD |
| `1D` | `0.5870` | 781,500.00 USD | 0.00 USD | 781,500.00 USD | 2,890.00 USD | 631.19 USD | 3,500.00 USD |
| `1D` | `0.5880` | 774,480.00 USD | 0.00 USD | 774,480.00 USD | 1,270.00 USD | 1,580.00 USD | 3,700.00 USD |
| `7D` | `0.5880` | 561,730.00 USD | 0.00 USD | 561,730.00 USD | 3,110.00 USD | 1,400.00 USD | 0.00 USD |
| `1D` | `0.5890` | 767,940.00 USD | 0.00 USD | 767,940.00 USD | 3,460.00 USD | 0.00 USD | 7.65 USD |
| `1D` | `0.5900` | 764,480.00 USD | 0.00 USD | 764,480.00 USD | 4,730.00 USD | 1,390.00 USD | 3.61 USD |
| `7D` | `0.5900` | 557,220.00 USD | 0.00 USD | 557,220.00 USD | 3,120.00 USD | 1,560.00 USD | 81.07 USD |
| `1D` | `0.5910` | 758,360.00 USD | 0.00 USD | 758,360.00 USD | 0.00 USD | 1,820.00 USD | 4,100.00 USD |
| `1D` | `0.5920` | 752,430.00 USD | 0.00 USD | 752,430.00 USD | 11,320.00 USD | 3,660.00 USD | 7,780.00 USD |
| `7D` | `0.5920` | 552,460.00 USD | 0.00 USD | 552,460.00 USD | 11,690.00 USD | 2,820.00 USD | 6,170.00 USD |
| `1D` | `0.5930` | 729,680.00 USD | 0.00 USD | 729,680.00 USD | 3,420.00 USD | 3,860.00 USD | 8,270.00 USD |
| `1D` | `0.5940` | 714,130.00 USD | 0.00 USD | 714,130.00 USD | 5,890.00 USD | 6,830.00 USD | 10,090.00 USD |
| `7D` | `0.5940` | 531,780.00 USD | 0.00 USD | 531,780.00 USD | 10,090.00 USD | 0.00 USD | 9,970.00 USD |
| `1D` | `0.5950` | 691,320.00 USD | 0.00 USD | 691,320.00 USD | 19,520.00 USD | 12,400.00 USD | 1,950.00 USD |
| `1D` | `0.5960` | 657,440.00 USD | 0.00 USD | 657,440.00 USD | 8,460.00 USD | 3,150.00 USD | 13,330.00 USD |
| `7D` | `0.5960` | 511,710.00 USD | 0.00 USD | 511,710.00 USD | 18,180.00 USD | 18,410.00 USD | 13,040.00 USD |
| `1D` | `0.5970` | 632,500.00 USD | 0.00 USD | 632,500.00 USD | 9,250.00 USD | 8,270.00 USD | 13,060.00 USD |
| `1D` | `0.5980` | 601,920.00 USD | 0.00 USD | 601,920.00 USD | 6,400.00 USD | 1,740.00 USD | 41,000.00 USD |
| `7D` | `0.5980` | 462,080.00 USD | 0.00 USD | 462,080.00 USD | 20,380.00 USD | 826.53 USD | 19,920.00 USD |
| `1D` | `0.5990` | 552,780.00 USD | 0.00 USD | 552,780.00 USD | 18,690.00 USD | 2,370.00 USD | 13,440.00 USD |
| `1D` | `0.6000` | 518,270.00 USD | 0.00 USD | 518,270.00 USD | 0.00 USD | 5,920.00 USD | 1,130.00 USD |
| `7D` | `0.6000` | 420,950.00 USD | 0.00 USD | 420,950.00 USD | 3,320.00 USD | 2,140.00 USD | 18,860.00 USD |
| `1D` | `0.6010` | 511,220.00 USD | 0.00 USD | 511,220.00 USD | 735.24 USD | 461.96 USD | 11,400.00 USD |
| `1D` | `0.6020` | 498,620.00 USD | 0.00 USD | 498,620.00 USD | 30,900.00 USD | 13,240.00 USD | 2,020.00 USD |
| `7D` | `0.6020` | 396,630.00 USD | 0.00 USD | 396,630.00 USD | 23,960.00 USD | 8,040.00 USD | 4,200.00 USD |
| `1D` | `0.6030` | 452,460.00 USD | 0.00 USD | 452,460.00 USD | 10,880.00 USD | 6,850.00 USD | 24.50 USD |
| `1D` | `0.6040` | 434,710.00 USD | 0.00 USD | 434,710.00 USD | 19,810.00 USD | 2,320.00 USD | 21.93 USD |
| `7D` | `0.6040` | 360,430.00 USD | 0.00 USD | 360,430.00 USD | 8,620.00 USD | 7,530.00 USD | 7,920.00 USD |
| `1D` | `0.6050` | 412,560.00 USD | 0.00 USD | 412,560.00 USD | 0.00 USD | 3,770.00 USD | 20,130.00 USD |
| `1D` | `0.6060` | 388,650.00 USD | 0.00 USD | 388,650.00 USD | 8,500.00 USD | 8,330.00 USD | 13,000.00 USD |
| `7D` | `0.6060` | 336,360.00 USD | 0.00 USD | 336,360.00 USD | 0.00 USD | 0.00 USD | 55.47 USD |
| `1D` | `0.6070` | 358,820.00 USD | 0.00 USD | 358,820.00 USD | 7,700.00 USD | 14,690.00 USD | 11,220.00 USD |
| `1D` | `0.6080` | 325,210.00 USD | 0.00 USD | 325,210.00 USD | 2,970.00 USD | 23,150.00 USD | 0.00 USD |
| `7D` | `0.6080` | 336,300.00 USD | 0.00 USD | 336,300.00 USD | 2,860.00 USD | 0.00 USD | 9,430.00 USD |
| `1D` | `0.6090` | 299,090.00 USD | 0.00 USD | 299,090.00 USD | 6,430.00 USD | 11,280.00 USD | 14,240.00 USD |
| `1D` | `0.6100` | 267,150.00 USD | 0.00 USD | 267,150.00 USD | 14,420.00 USD | 14,280.00 USD | 17,280.00 USD |
| `7D` | `0.6100` | 324,010.00 USD | 0.00 USD | 324,010.00 USD | 21,400.00 USD | 47,430.00 USD | 25,210.00 USD |
| `1D` | `0.6110` | 221,180.00 USD | 0.00 USD | 221,180.00 USD | 1,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6120` | 219,750.00 USD | 0.00 USD | 219,750.00 USD | 23,580.00 USD | 2,470.00 USD | 19,200.00 USD |
| `7D` | `0.6120` | 229,960.00 USD | 0.00 USD | 229,960.00 USD | 35,760.00 USD | 5,720.00 USD | 18,550.00 USD |
| `1D` | `0.6130` | 174,500.00 USD | 0.00 USD | 174,500.00 USD | 2,140.00 USD | 12,430.00 USD | 22,770.00 USD |
| `1D` | `0.6140` | 137,150.00 USD | 0.00 USD | 137,150.00 USD | 53,460.00 USD | 18,080.00 USD | 4,040.00 USD |
| `7D` | `0.6140` | 169,930.00 USD | 0.00 USD | 169,930.00 USD | 51,550.00 USD | 8,040.00 USD | 10,690.00 USD |
| `1D` | `0.6150` | 61,570.00 USD | 0.00 USD | 61,570.00 USD | 14,190.00 USD | 7,820.00 USD | 0.00 USD |
| `1D` | `0.6160` | 39,560.00 USD | 0.00 USD | 39,560.00 USD | 25,650.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6160` | 99,640.00 USD | 0.00 USD | 99,640.00 USD | 12,920.00 USD | 16,340.00 USD | 4,690.00 USD |
| `1D` | `0.6170` | 13,910.00 USD | 0.00 USD | 13,910.00 USD | 0.00 USD | 0.00 USD | 13,910.00 USD |
| `7D` | `0.6180` | 65,700.00 USD | 0.00 USD | 65,700.00 USD | 20,870.00 USD | 2,610.00 USD | 365.52 USD |
| `7D` | `0.6200` | 41,850.00 USD | 0.00 USD | 41,850.00 USD | 23,430.00 USD | 0.00 USD | 18,420.00 USD |
| `1D` | `0.6210` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6210` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6220` | 27,950.00 USD | 27,950.00 USD | 0.00 USD | 4,760.00 USD | 22,640.00 USD | 542.09 USD |
| `7D` | `0.6240` | 28,040.00 USD | 28,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 90.21 USD |
| `7D` | `0.6260` | 95,350.00 USD | 95,350.00 USD | 0.00 USD | 67,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6280` | 95,780.00 USD | 95,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 431.03 USD |
| `1D` | `0.6290` | 2,020.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD | 0.00 USD |
| `1D` | `0.6300` | 10,470.00 USD | 10,470.00 USD | 0.00 USD | 0.00 USD | 3,430.00 USD | 5,020.00 USD |
| `7D` | `0.6300` | 106,240.00 USD | 106,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,460.00 USD |
| `1D` | `0.6310` | 37,400.00 USD | 37,400.00 USD | 0.00 USD | 11,740.00 USD | 3,970.00 USD | 11,220.00 USD |
| `1D` | `0.6320` | 69,360.00 USD | 69,360.00 USD | 0.00 USD | 31,880.00 USD | 0.00 USD | 78.00 USD |
| `1D` | `0.6330` | 125,320.00 USD | 125,320.00 USD | 0.00 USD | 17,300.00 USD | 5,390.00 USD | 33,280.00 USD |
| `1D` | `0.6340` | 209,010.00 USD | 209,010.00 USD | 0.00 USD | 32,460.00 USD | 2,420.00 USD | 48,810.00 USD |
| `7D` | `0.6340` | 174,910.00 USD | 174,910.00 USD | 0.00 USD | 68,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6350` | 267,500.00 USD | 267,500.00 USD | 0.00 USD | 51,360.00 USD | 0.00 USD | 7,130.00 USD |
| `1D` | `0.6360` | 397,240.00 USD | 397,240.00 USD | 0.00 USD | 63,010.00 USD | 2,470.00 USD | 64,260.00 USD |
| `7D` | `0.6360` | 266,370.00 USD | 266,370.00 USD | 0.00 USD | 34,320.00 USD | 0.00 USD | 57,150.00 USD |
| `1D` | `0.6370` | 433,130.00 USD | 433,130.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD | 30,110.00 USD |
| `1D` | `0.6380` | 457,360.00 USD | 457,360.00 USD | 0.00 USD | 0.00 USD | 19,010.00 USD | 5,220.00 USD |
| `7D` | `0.6380` | 305,900.00 USD | 305,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39,530.00 USD |
| `1D` | `0.6390` | 526,830.00 USD | 526,830.00 USD | 0.00 USD | 18,790.00 USD | 3,690.00 USD | 47,000.00 USD |
| `1D` | `0.6400` | 642,810.00 USD | 642,810.00 USD | 0.00 USD | 57,170.00 USD | 28,050.00 USD | 30,770.00 USD |
| `7D` | `0.6400` | 327,130.00 USD | 327,130.00 USD | 0.00 USD | 0.00 USD | 7,510.00 USD | 13,730.00 USD |
| `1D` | `0.6410` | 691,950.00 USD | 691,950.00 USD | 0.00 USD | 32,400.00 USD | 9,300.00 USD | 7,440.00 USD |
| `1D` | `0.6420` | 795,520.00 USD | 795,520.00 USD | 0.00 USD | 69,490.00 USD | 14,860.00 USD | 19,230.00 USD |
| `7D` | `0.6420` | 434,320.00 USD | 434,320.00 USD | 0.00 USD | 55,350.00 USD | 35,430.00 USD | 16,400.00 USD |
| `1D` | `0.6430` | 878,670.00 USD | 878,670.00 USD | 0.00 USD | 35,700.00 USD | 17,300.00 USD | 30,150.00 USD |
| `1D` | `0.6440` | 991,420.00 USD | 991,420.00 USD | 0.00 USD | 39,760.00 USD | 23,720.00 USD | 49,280.00 USD |
| `7D` | `0.6440` | 521,770.00 USD | 521,770.00 USD | 0.00 USD | 44,690.00 USD | 24,820.00 USD | 17,940.00 USD |
| `1D` | `0.6450` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 70,250.00 USD | 9,920.00 USD | 36,640.00 USD |
| `1D` | `0.6460` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 57,400.00 USD | 9,320.00 USD | 7,110.00 USD |
| `7D` | `0.6460` | 879,190.00 USD | 879,190.00 USD | 0.00 USD | 172,610.00 USD | 46,630.00 USD | 138,180.00 USD |
| `1D` | `0.6470` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 74,410.00 USD | 17,210.00 USD | 8,660.00 USD |
| `1D` | `0.6480` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 112,500.00 USD | 6,780.00 USD | 151.61 USD |
| `7D` | `0.6480` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 86,440.00 USD | 26,520.00 USD | 33,000.00 USD |
| `1D` | `0.6490` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 66,830.00 USD | 1,230.00 USD | 9,740.00 USD |
| `1D` | `0.6500` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 64,920.00 USD | 5,920.00 USD | 128.67 USD |
| `7D` | `0.6500` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 73,560.00 USD | 0.00 USD | 132,430.00 USD |
| `1D` | `0.6510` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 55,500.00 USD | 0.00 USD | 11,510.00 USD |
| `1D` | `0.6520` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 93,550.00 USD | 9,040.00 USD | 2,020.00 USD |
| `7D` | `0.6520` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 298,050.00 USD | 10,910.00 USD | 105,340.00 USD |
| `1D` | `0.6530` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 11,510.00 USD | 3,910.00 USD | 0.00 USD |
| `1D` | `0.6540` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 24,280.00 USD | 0.00 USD | 10,560.00 USD |
| `7D` | `0.6540` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 15,730.00 USD | 4,440.00 USD | 61,460.00 USD |
| `1D` | `0.6550` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,950.00 USD |
| `1D` | `0.6560` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD |
| `7D` | `0.6560` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 5,380.00 USD | 1,030.00 USD |
| `1D` | `0.6570` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 59.54 USD |
| `1D` | `0.6580` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 3,310.00 USD | 25.28 USD |
| `7D` | `0.6580` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 28,280.00 USD | 9,870.00 USD |
| `1D` | `0.6590` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 5,890.00 USD | 164.02 USD |
| `1D` | `0.6600` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 8,400.00 USD | 59.63 USD |
| `7D` | `0.6600` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 15,500.00 USD | 770.13 USD |
| `1D` | `0.6610` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 142.10 USD |
| `1D` | `0.6620` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,710.00 USD |
| `7D` | `0.6620` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 507.07 USD |
| `1D` | `0.6630` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39.16 USD |
| `1D` | `0.6640` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 11,190.00 USD | 0.00 USD | 126.28 USD |
| `7D` | `0.6640` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 33,660.00 USD | 0.00 USD | 753.62 USD |
| `1D` | `0.6650` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 3,160.00 USD | 17,420.00 USD |
| `1D` | `0.6660` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,410.00 USD |
| `7D` | `0.6660` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 6,770.00 USD | 816.74 USD |
| `1D` | `0.6670` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 18,850.00 USD | 0.00 USD | 24.36 USD |
| `1D` | `0.6680` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44.63 USD |
| `7D` | `0.6680` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,070.00 USD |
| `1D` | `0.6690` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 3,550.00 USD | 4,410.00 USD |
| `1D` | `0.6700` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 8,830.00 USD | 1,920.00 USD | 24,760.00 USD |
| `7D` | `0.6700` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 217.49 USD |
| `1D` | `0.6710` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 41,970.00 USD | 0.00 USD | 5,950.00 USD |
| `7D` | `0.6720` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 58,470.00 USD | 0.00 USD | 30,330.00 USD |
| `1D` | `0.6730` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 24,320.00 USD | 3,670.00 USD | 4,560.00 USD |
| `1D` | `0.6740` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 64,370.00 USD | 7,120.00 USD | 9,210.00 USD |
| `7D` | `0.6740` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 39,730.00 USD | 0.00 USD | 164.10 USD |
| `1D` | `0.6750` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 28,700.00 USD | 4,300.00 USD | 12,070.00 USD |
| `1D` | `0.6760` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.6760` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 77,970.00 USD | 33,300.00 USD |
| `1D` | `0.6770` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 14,540.00 USD | 6,110.00 USD | 14,290.00 USD |
| `1D` | `0.6780` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 33,610.00 USD | 12,680.00 USD | 8,710.00 USD |
| `7D` | `0.6780` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 63,600.00 USD | 14,400.00 USD | 17,930.00 USD |
| `1D` | `0.6790` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 18,610.00 USD | 14,580.00 USD |
| `1D` | `0.6800` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 686.25 USD | 2,450.00 USD |
| `7D` | `0.6800` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 0.00 USD |
| `1D` | `0.6810` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 1,940.00 USD | 9,870.00 USD |
| `1D` | `0.6820` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 22,600.00 USD | 16,590.00 USD | 7,740.00 USD |
| `7D` | `0.6820` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 32,570.00 USD | 53,450.00 USD | 0.00 USD |
| `1D` | `0.6830` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 24,570.00 USD | 26,560.00 USD | 36,830.00 USD |
| `1D` | `0.6840` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 45,780.00 USD | 25,860.00 USD | 13,900.00 USD |
| `7D` | `0.6840` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 57,890.00 USD | 54,300.00 USD | 102,430.00 USD |
| `1D` | `0.6850` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 49,540.00 USD | 5,780.00 USD | 10,620.00 USD |
| `1D` | `0.6860` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 40,250.00 USD | 4,380.00 USD | 14,780.00 USD |
| `7D` | `0.6860` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 49,930.00 USD | 14,540.00 USD | 10,480.00 USD |
| `1D` | `0.6870` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 63,220.00 USD | 1,160.00 USD | 3,830.00 USD |
| `1D` | `0.6880` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 14,350.00 USD | 11,160.00 USD | 25,380.00 USD |
| `7D` | `0.6880` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 38,030.00 USD | 17,300.00 USD | 131.40 USD |
| `1D` | `0.6890` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,340.00 USD |
| `1D` | `0.6900` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 18,600.00 USD | 4,030.00 USD | 21,060.00 USD |
| `7D` | `0.6900` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 15,510.00 USD | 16,550.00 USD |
| `1D` | `0.6910` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 28,860.00 USD | 1,730.00 USD | 39,760.00 USD |
| `1D` | `0.6920` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 16,800.00 USD | 0.00 USD | 13,680.00 USD |
| `7D` | `0.6920` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 69,620.00 USD | 2,090.00 USD | 61,890.00 USD |
| `1D` | `0.6930` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 10,030.00 USD | 0.00 USD | 168.16 USD |
| `1D` | `0.6940` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 11,230.00 USD | 2,090.00 USD | 9,470.00 USD |
| `7D` | `0.6940` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 14,220.00 USD | 0.00 USD | 42,600.00 USD |
| `1D` | `0.6950` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 22,480.00 USD | 4,460.00 USD | 3,790.00 USD |
| `1D` | `0.6960` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 58,370.00 USD | 6,000.00 USD | 0.00 USD |
| `7D` | `0.6960` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 59,960.00 USD | 0.00 USD | 12,390.00 USD |
| `1D` | `0.6970` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 33,460.00 USD | 4,780.00 USD | 34.66 USD |
| `1D` | `0.6980` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 9,140.00 USD | 4,100.00 USD | 1,290.00 USD |
| `7D` | `0.6980` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 35,980.00 USD | 16,990.00 USD | 0.00 USD |
| `1D` | `0.6990` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 5,180.00 USD | 4,830.00 USD | 5,380.00 USD |
| `1D` | `0.7000` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 18,240.00 USD | 4,020.00 USD | 16,170.00 USD |
| `7D` | `0.7000` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 29,740.00 USD | 0.00 USD | 40,500.00 USD |
| `1D` | `0.7010` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 15,520.00 USD | 0.00 USD | 73.64 USD |
| `1D` | `0.7020` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 14,360.00 USD | 0.00 USD | 22.18 USD |
| `7D` | `0.7020` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 29,810.00 USD | 0.00 USD | 53,080.00 USD |
| `1D` | `0.7030` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 4,330.00 USD | 0.00 USD | 10,510.00 USD |
| `1D` | `0.7040` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 29,930.00 USD | 2,630.00 USD | 8,760.00 USD |
| `7D` | `0.7040` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 95,520.00 USD | 0.00 USD | 96,320.00 USD |
| `1D` | `0.7050` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 29,790.00 USD | 2,660.00 USD | 18,910.00 USD |
| `1D` | `0.7060` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 8,590.00 USD | 3,860.00 USD | 13,370.00 USD |
| `7D` | `0.7060` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 47,840.00 USD | 33,490.00 USD | 178,040.00 USD |
| `1D` | `0.7070` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 19,980.00 USD | 21,860.00 USD | 17,290.00 USD |
| `1D` | `0.7080` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 18,420.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.7080` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 24,440.00 USD | 64,870.00 USD | 82,880.00 USD |
| `7D` | `0.7100` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 150,830.00 USD | 63,530.00 USD | 148,880.00 USD |
| `7D` | `0.7120` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 101,040.00 USD | 78,760.00 USD | 227,890.00 USD |
| `7D` | `0.7140` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 202,560.00 USD | 67,260.00 USD | 133,340.00 USD |
| `7D` | `0.7160` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 113,040.00 USD | 65,260.00 USD | 164,570.00 USD |
| `7D` | `0.7180` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 165,860.00 USD | 56,910.00 USD | 66,460.00 USD |
| `7D` | `0.7200` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 93,750.00 USD | 45,160.00 USD | 178,510.00 USD |
| `7D` | `0.7220` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 318,420.00 USD | 67,130.00 USD | 98,240.00 USD |
| `7D` | `0.7240` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 146,110.00 USD | 24,910.00 USD | 129,260.00 USD |
| `7D` | `0.7260` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 106,410.00 USD | 52,120.00 USD | 175,880.00 USD |
| `7D` | `0.7280` | 7,210,000.00 USD | 7,210,000.00 USD | 0.00 USD | 99,750.00 USD | 40,180.00 USD | 84,430.00 USD |
| `7D` | `0.7300` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 115,310.00 USD | 60,310.00 USD | 109,390.00 USD |
| `7D` | `0.7320` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 189,840.00 USD | 65,640.00 USD | 80,450.00 USD |
| `7D` | `0.7340` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 31,260.00 USD | 8,620.00 USD | 63,100.00 USD |
| `7D` | `0.7360` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 103,600.00 USD | 46,790.00 USD | 35,110.00 USD |
| `7D` | `0.7380` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 73,710.00 USD | 19,000.00 USD | 60,750.00 USD |
| `7D` | `0.7400` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 1,730.00 USD | 4,760.00 USD | 21,120.00 USD |
| `7D` | `0.7420` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 35,810.00 USD | 35,860.00 USD | 31,590.00 USD |
| `7D` | `0.7440` | 8,580,000.00 USD | 8,580,000.00 USD | 0.00 USD | 74,450.00 USD | 39,890.00 USD | 70,520.00 USD |
| `7D` | `0.7460` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 88,800.00 USD | 28,800.00 USD | 51,610.00 USD |
| `7D` | `0.7480` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 60,580.00 USD | 28,900.00 USD | 38,310.00 USD |
| `7D` | `0.7500` | 8,970,000.00 USD | 8,970,000.00 USD | 0.00 USD | 52,320.00 USD | 12,610.00 USD | 25,030.00 USD |
| `7D` | `0.7520` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 53,470.00 USD | 13,000.00 USD | 51,580.00 USD |
| `7D` | `0.7540` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 30,340.00 USD | 1,890.00 USD | 24,940.00 USD |
| `7D` | `0.7560` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 26,000.00 USD | 7,570.00 USD | 22,190.00 USD |
| `7D` | `0.7580` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 55,420.00 USD | 11,790.00 USD | 45,660.00 USD |
| `7D` | `0.7600` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 57,020.00 USD | 4,320.00 USD | 80,830.00 USD |
| `7D` | `0.7620` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 54,140.00 USD | 24,170.00 USD | 21,620.00 USD |
| `7D` | `0.7640` | 9,660,000.00 USD | 9,660,000.00 USD | 0.00 USD | 50,390.00 USD | 13,520.00 USD | 42,010.00 USD |
| `7D` | `0.7660` | 9,830,000.00 USD | 9,830,000.00 USD | 0.00 USD | 56,130.00 USD | 18,130.00 USD | 90,710.00 USD |
| `7D` | `0.7680` | 9,970,000.00 USD | 9,970,000.00 USD | 0.00 USD | 66,570.00 USD | 32,520.00 USD | 40,950.00 USD |
| `7D` | `0.7700` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 10,860.00 USD | 12,600.00 USD | 41,550.00 USD |
| `7D` | `0.7720` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 58,380.00 USD | 32,920.00 USD | 25,860.00 USD |
| `7D` | `0.7740` | 10,260,000.00 USD | 10,260,000.00 USD | 0.00 USD | 51,600.00 USD | 25,250.00 USD | 35,730.00 USD |
| `7D` | `0.7760` | 10,320,000.00 USD | 10,320,000.00 USD | 0.00 USD | 38,170.00 USD | 2,980.00 USD | 12,680.00 USD |
| `7D` | `0.7780` | 10,440,000.00 USD | 10,440,000.00 USD | 0.00 USD | 68,800.00 USD | 20,860.00 USD | 32,630.00 USD |
| `7D` | `0.7800` | 10,600,000.00 USD | 10,600,000.00 USD | 0.00 USD | 60,490.00 USD | 21,940.00 USD | 80,690.00 USD |
| `7D` | `0.7820` | 10,720,000.00 USD | 10,720,000.00 USD | 0.00 USD | 90,020.00 USD | 17,850.00 USD | 6,210.00 USD |
| `7D` | `0.7840` | 10,800,000.00 USD | 10,800,000.00 USD | 0.00 USD | 72,650.00 USD | 7,150.00 USD | 2,170.00 USD |
| `7D` | `0.7860` | 10,870,000.00 USD | 10,870,000.00 USD | 0.00 USD | 32,690.00 USD | 9,290.00 USD | 31,550.00 USD |
| `7D` | `0.7880` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 11,900.00 USD | 10,710.00 USD | 22,880.00 USD |
| `7D` | `0.7900` | 11,000,000.00 USD | 11,000,000.00 USD | 0.00 USD | 44,050.00 USD | 16,710.00 USD | 17,150.00 USD |
| `7D` | `0.7910` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 30,620.00 USD | 5,860.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `86.49M` | Total OI Tokens: `141,277,270.9 APT`
  * 1h OI Change: `+0.90%` | 4h OI Change: `-0.13%` | 24h OI Change: `-8.85%`
  * Exchange Breakdown: Binance=`15.36M` | Bybit=`17.18M` | OKX=`4.05M` | Hyperliquid=`3.36M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-6.05K` | Last 24h: `2.90K` | Last 3d: `7.60K` | Last 7d: `2.85K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0162%` | **USDT OKX** | `-0.0158%` |
| **USDT Bybit** | `-0.0185%` | **USDT KuCoin** | `-0.0129%` |
| **USDT MEXC** | `-0.0162%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0002%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `APT` | `49.36%` | `50.64%` | `0.97` | 16,490,000.00 USD |
| `15M` | `Binance` | `50.47%` | `49.53%` | `1.02` | 6,720,000.00 USD |
| `15M` | `OKX` | `55.28%` | `44.72%` | `1.24` | 2,280,000.00 USD |
| `15M` | `Bybit` | `40.26%` | `59.74%` | `0.67` | 1,990,000.00 USD |
| `15M` | `KuCoin` | `50.31%` | `49.69%` | `1.01` | 75,750.00 USD |
| `15M` | `Gate` | `41.01%` | `58.99%` | `0.70` | 396,040.00 USD |
| `15M` | `Bitget` | `47.75%` | `52.25%` | `0.91` | 1,520,000.00 USD |
| `15M` | `BingX` | `32.62%` | `67.38%` | `0.48` | 739,350.00 USD |
| `15M` | `MEXC` | `56.57%` | `43.43%` | `1.30` | 937,920.00 USD |
| `15M` | `Bitunix` | `49.6%` | `50.4%` | `0.98` | 577,370.00 USD |
| `15M` | `Hyperliquid` | `46.13%` | `53.87%` | `0.86` | 833,720.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `45.94%` | `54.06%` | `0.85` | 62,040.00 USD |
| `15M` | `Crypto.com` | `40.77%` | `59.23%` | `0.69` | 2,400.00 USD |
| `15M` | `WhiteBIT` | `99.62%` | `0.38%` | `262.16` | 238,130.00 USD |
| `15M` | `HTX` | `25.9%` | `74.1%` | `0.35` | 6,880.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `42.81%` | `57.19%` | `0.75` | 57,700.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `48.91%` | `51.09%` | `0.96` | 42,020.00 USD |
| `15M` | `Whale Positions` | `50.47%` | `49.53%` | `1.02` | 6,720,000.00 USD |
| `15M` | `Global Accounts` | `49.36%` | `50.64%` | `0.97` | 16,490,000.00 USD |
| `1H` | `APT` | `48.75%` | `51.25%` | `0.95` | 20,860,000.00 USD |
| `1H` | `Binance` | `48.69%` | `51.31%` | `0.95` | 7,250,000.00 USD |
| `1H` | `OKX` | `50.92%` | `49.08%` | `1.04` | 5,270,000.00 USD |
| `1H` | `Bybit` | `54.25%` | `45.75%` | `1.19` | 1,670,000.00 USD |
| `1H` | `KuCoin` | `50.48%` | `49.52%` | `1.02` | 610,280.00 USD |
| `1H` | `Gate` | `50.77%` | `49.23%` | `1.03` | 366,550.00 USD |
| `1H` | `Bitget` | `62.29%` | `37.71%` | `1.65` | 400,340.00 USD |
| `1H` | `BingX` | `22.21%` | `77.79%` | `0.29` | 837,540.00 USD |
| `1H` | `MEXC` | `44.36%` | `55.64%` | `0.80` | 182,310.00 USD |
| `1H` | `Bitunix` | `52.89%` | `47.11%` | `1.12` | 621,300.00 USD |
| `1H` | `Hyperliquid` | `74.13%` | `25.87%` | `2.87` | 115,080.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.08%` | `49.92%` | `1.00` | 3,150,000.00 USD |
| `1H` | `Crypto.com` | `34.34%` | `65.66%` | `0.52` | 188.30 USD |
| `1H` | `WhiteBIT` | `6.92%` | `93.08%` | `0.07` | 331,260.00 USD |
| `1H` | `HTX` | `83.12%` | `16.88%` | `4.92` | 9,590.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `100%` | `0.00` | 1,540.00 USD |
| `1H` | `Aster` | `50.14%` | `49.86%` | `1.01` | 25,090.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `9.62%` | `90.38%` | `0.11` | 11,450.00 USD |
| `1H` | `Whale Positions` | `48.69%` | `51.31%` | `0.95` | 7,250,000.00 USD |
| `1H` | `Global Accounts` | `48.75%` | `51.25%` | `0.95` | 20,860,000.00 USD |
| `4H` | `APT` | `49.92%` | `50.08%` | `1.00` | 110,200,000.00 USD |
| `4H` | `Binance` | `49.97%` | `50.03%` | `1.00` | 41,270,000.00 USD |
| `4H` | `OKX` | `52.42%` | `47.58%` | `1.10` | 24,060,000.00 USD |
| `4H` | `Bybit` | `55.01%` | `44.99%` | `1.22` | 8,800,000.00 USD |
| `4H` | `KuCoin` | `51.87%` | `48.13%` | `1.08` | 2,740,000.00 USD |
| `4H` | `Gate` | `49.82%` | `50.18%` | `0.99` | 2,970,000.00 USD |
| `4H` | `Bitget` | `51.08%` | `48.92%` | `1.04` | 3,800,000.00 USD |
| `4H` | `BingX` | `34.13%` | `65.87%` | `0.52` | 2,760,000.00 USD |
| `4H` | `MEXC` | `47.86%` | `52.14%` | `0.92` | 1,980,000.00 USD |
| `4H` | `Bitunix` | `54.71%` | `45.29%` | `1.21` | 3,340,000.00 USD |
| `4H` | `Hyperliquid` | `39.6%` | `60.4%` | `0.66` | 1,380,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.88%` | `51.12%` | `0.96` | 15,200,000.00 USD |
| `4H` | `Crypto.com` | `48.1%` | `51.9%` | `0.93` | 2,410.00 USD |
| `4H` | `WhiteBIT` | `6.91%` | `93.09%` | `0.07` | 1,380,000.00 USD |
| `4H` | `HTX` | `49.23%` | `50.77%` | `0.97` | 105,500.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `69.56%` | `30.44%` | `2.29` | 187,870.00 USD |
| `4H` | `Aster` | `59.18%` | `40.82%` | `1.45` | 144,350.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `38.7%` | `61.3%` | `0.63` | 77,020.00 USD |
| `4H` | `Whale Positions` | `49.97%` | `50.03%` | `1.00` | 41,270,000.00 USD |
| `4H` | `Global Accounts` | `49.92%` | `50.08%` | `1.00` | 110,200,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.6009` | `0.6009` | `0.6009` | `0.6031` | `0.5985` | 579,759.86 USD | 375,952.93 USD | 203,806.94 USD | 172,145.99 USD | `+29.69%` | `13B / 4S` |
| `0:00 UTC` | `0.5984` | `0.6002` | `0.5984` | `0.6042` | `0.5967` | 484,315.17 USD | 239,896.11 USD | 244,419.06 USD | -4,522.96 USD | `-0.93%` | `11B / 9S` |
| `5:00 UTC` | `0.6038` | `0.6063` | `0.6038` | `0.6109` | `0.6034` | 423,653.18 USD | 219,431.45 USD | 204,221.73 USD | 15,209.72 USD | `+3.59%` | `23B / 9S` |
| `0:00 UTC` | `0.6099` | `0.6090` | `0.6099` | `0.6109` | `0.6063` | 539,317.21 USD | 218,354.05 USD | 320,963.16 USD | -102,609.12 USD | `-19.03%` | `3B / 5S` |
| `5:00 UTC` | `0.6071` | `0.6045` | `0.6071` | `0.6092` | `0.6016` | 771,529.71 USD | 428,044.31 USD | 343,485.41 USD | 84,558.90 USD | `+10.96%` | `12B / 18S` |
| `0:00 UTC` | `0.6067` | `0.6054` | `0.6067` | `0.6069` | `0.6027` | 290,014.01 USD | 171,806.26 USD | 118,207.75 USD | 53,598.51 USD | `+18.48%` | `8B / 3S` |
| `5:00 UTC` | `0.6083` | `0.6072` | `0.6083` | `0.6096` | `0.6042` | 191,671.81 USD | 128,624.28 USD | 63,047.54 USD | 65,576.74 USD | `+34.21%` | `17B / 3S` |
| `0:00 UTC` | `0.6152` | `0.6139` | `0.6152` | `0.6175` | `0.6090` | 470,291.39 USD | 289,898.53 USD | 180,392.87 USD | 109,505.66 USD | `+23.28%` | `29B / 6S` |
| `5:00 UTC` | `0.6161` | `0.6160` | `0.6161` | `0.6176` | `0.6147` | 319,675.12 USD | 174,523.38 USD | 145,151.74 USD | 29,371.64 USD | `+9.19%` | `4B / 6S` |
| `0:00 UTC` | `0.6163` | `0.6162` | `0.6163` | `0.6163` | `0.6159` | 2,747.58 USD | 1,483.92 USD | 1,263.66 USD | 220.26 USD | `+8.02%` | `0B / 0S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 21:06` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6898` | 0.00 USD | 0.00 USD |
| `10-28 21:06` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6871` | 68,000.00 USD | 0.00 USD |
| `10-28 21:02` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6867` | 0.00 USD | 0.00 USD |
| `10-28 20:37` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6858` | 33,000.00 USD | 0.00 USD |
| `10-28 20:01` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6782` | 0.00 USD | 0.00 USD |
| `10-28 20:01` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6808` | 79,000.00 USD | 0.00 USD |
| `10-28 19:48` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6764` | 22,000.00 USD | 0.00 USD |
| `10-28 19:46` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6752` | 44,000.00 USD | 0.00 USD |
| `10-28 19:46` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6752` | 44,000.00 USD | 0.00 USD |
| `10-28 19:43` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6771` | 0.00 USD | 0.00 USD |
| `10-28 19:43` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6793` | 39,000.00 USD | 0.00 USD |
| `10-28 19:41` | `Volume 1.0M APT` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6752` | 361,000.00 USD | 0.00 USD |
| `10-28 19:35` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6807` | 0.00 USD | 0.00 USD |
| `10-28 19:31` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6762` | 79,000.00 USD | 0.00 USD |
| `10-28 19:31` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6762` | 79,000.00 USD | 0.00 USD |
| `10-28 19:31` | `Range 0.002` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `0.6762` | 106,000.00 USD | 0.00 USD |
| `10-28 19:21` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6771` | 75,000.00 USD | 0.00 USD |
| `10-28 19:07` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6859` | 121,000.00 USD | 0.00 USD |
| `10-28 18:48` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6796` | 47,000.00 USD | 0.00 USD |
| `10-28 18:44` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6793` | 107,000.00 USD | 0.00 USD |
| `10-28 18:37` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6818` | 0.00 USD | 0.00 USD |
| `10-28 17:54` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6887` | 177,000.00 USD | 0.00 USD |
| `10-28 17:46` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6884` | 112,000.00 USD | 0.00 USD |
| `10-28 17:43` | `Volume 1.0M APT` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6842` | 275,000.00 USD | 0.00 USD |
| `10-28 17:36` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6934` | 22,000.00 USD | 0.00 USD |
| `10-28 17:03` | `Volume 1.0M APT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6995` | 234,000.00 USD | 0.00 USD |
| `10-28 16:15` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6994` | 140,000.00 USD | 0.00 USD |
| `10-28 16:02` | `Volume 1.0M APT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6994` | 223,000.00 USD | 0.00 USD |
| `10-28 14:46` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6950` | 67,000.00 USD | 0.00 USD |
| `10-28 14:31` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6922` | 0.00 USD | 0.00 USD |
| `10-28 14:31` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6896` | 58,000.00 USD | 0.00 USD |
| `10-28 14:31` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6896` | 58,000.00 USD | 0.00 USD |
| `10-28 14:09` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6972` | 0.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6976` | 0.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.7006` | 0.00 USD | 0.00 USD |
| `10-28 13:57` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6962` | 0.00 USD | 0.00 USD |
| `10-28 13:33` | `Volume 1.0M APT` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6929` | 351,000.00 USD | 0.00 USD |
| `10-28 12:44` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6912` | 0.00 USD | 0.00 USD |
| `10-28 12:22` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6924` | 0.00 USD | 0.00 USD |
| `10-28 10:16` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6976` | 25,000.00 USD | 0.00 USD |
| `10-28 09:48` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6958` | 18,000.00 USD | 0.00 USD |
| `10-28 09:29` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6985` | 55,000.00 USD | 0.00 USD |
| `10-28 09:11` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.7008` | 0.00 USD | 0.00 USD |
| `10-28 09:04` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.7021` | 0.00 USD | 0.00 USD |
| `10-28 09:00` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.7001` | 27,000.00 USD | 0.00 USD |
| `10-28 08:49` | `Range 0.002` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `0.6966` | 73,000.00 USD | 0.00 USD |
| `10-28 08:31` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6974` | 0.00 USD | 0.00 USD |
| `10-28 07:29` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.7003` | 0.00 USD | 0.00 USD |
| `10-28 07:23` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6977` | 10,000.00 USD | 0.00 USD |
| `10-28 06:12` | `Range 0.002` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.6982` | 122,000.00 USD | 0.00 USD |
| `10-28 05:31` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6963` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -27,540.00 USD | -37,550.00 USD | **`DISTRIBUTION`** |
| `15m` | -2,490.00 USD | -29,780.00 USD | **`DISTRIBUTION`** |
| `30m` | 78,520.00 USD | 173,220.00 USD | **`ACCUMULATION`** |
| `1h` | 151,650.00 USD | 374,150.00 USD | **`ACCUMULATION`** |
| `2h` | 176,520.00 USD | 427,340.00 USD | **`ACCUMULATION`** |
| `4h` | -317,070.00 USD | -547,870.00 USD | **`DISTRIBUTION`** |
| `6h` | -716,480.00 USD | -967,910.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,040,000.00 USD | -4,650,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,160,000.00 USD | -6,790,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,140,000.00 USD | -8,550,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,730,000.00 USD | -25,370,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,400,000.00 USD | -106,130,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-27.54K` | 15m=`-2.49K` | 1h=`+151.65K` | 24h=`-1.14M`
* Futures Capital Netflows: 5m=`-37.55K` | 15m=`-29.78K` | 1h=`+374.15K` | 24h=`-8.55M`
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
  * `2026-10-30 09:09:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:28:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:29:56 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.6880` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-0.5122` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.69`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.6921` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.89` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.31`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.6956`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
