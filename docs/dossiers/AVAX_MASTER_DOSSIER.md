# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 23:40:50 IST` (`2026-10-29 18:10:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.86` | **Live Ask Quote**: `8.89` | **Mid Price**: `8.88`
- **Spread Points**: `3.00` | **Spread BPS**: `33.80 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
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
  * Session VWAP: `8.76` | VWAP Z-Score: `+0.72` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0567` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `49.79` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `9.14` | Lower -3.00σ Band: `8.38`
  * Upper +2.51σ Band: `9.07` | Lower -2.51σ Band: `8.44`
  * Upper +2.01σ Band: `9.01` | Lower -2.01σ Band: `8.51`
  * Upper +2.00σ Band: `9.01` | Lower -2.00σ Band: `8.51`
  * Upper +1.28σ Band: `8.92` | Lower -1.28σ Band: `8.60`
  * Upper +1.00σ Band: `8.88` | Lower -1.00σ Band: `8.63`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.89` | EMA-20=`8.87` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.82` (Slope: `+0.0000`) | EMA-100=`8.81`
  * Institutional Anchors: EMA-144=`8.82` | EMA-200=`8.83` (Slope: `+0.1373`) | EMA-233=`8.83`
- **Range Boundaries**: 24H High=`9.14` | 24H Low=`8.53` | Weekly High=`9.14` | Weekly Low=`8.53`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.89` (Distance: `-0.19%`)
  * Point of Control (POC) = `8.74` (Distance: `+1.54%`)
  * Value Area Low (VAL) = `8.54` (Distance: `+3.94%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`9.02` | POC=`8.99` | VAL=`8.86`
  * Prior Day Extremes: PDH=`9.14` | PDL=`8.76` | PDC=`8.99`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`8.96` | Weekly POC=`8.91` | Weekly VAL=`8.75`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`9.04` | Low=`8.53`
  * London Session (08:00-16:00 UTC): High=`8.81` | Low=`8.59`
  * New York Session (13:00-21:00 UTC): High=`9.06` | Low=`8.68`
  * Initial Balance (First Hour): IB High=`8.78` | IB Low=`8.65`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.84` - `8.91`
  * Optimal Trade Entry (OTE 0.705): `8.89`
  * Structural Invalidation Anchor (0.786): `8.95`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.85` | `8.87` | `8.84` | `8.87` | `26,725` | 236,583.96 USD | 78,888.54 USD | `+33.34%` | -2,838,645.34 USD | `+1.06` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `8.87` | `8.88` | `8.86` | `8.88` | `29,652` | 262,984.44 USD | 27,384.38 USD | `+10.41%` | -2,811,260.95 USD | `+0.74` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `8.88` | `8.88` | `8.87` | `8.88` | `3,588` | 31,850.12 USD | 12,394.68 USD | `+38.92%` | -2,798,866.28 USD | `+0.65` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.92` | `8.94` | `8.85` | `8.86` | `210,364` | 1,871,719.04 USD | -338,096.31 USD | `-18.06%` | -2,752,445.46 USD | `-0.57` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `8.86` | `8.87` | `8.82` | `8.87` | `160,318` | 1,418,137.84 USD | -114,451.81 USD | `-8.07%` | -2,866,897.27 USD | `+0.05` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `8.87` | `8.88` | `8.86` | `8.88` | `33,218` | 294,639.24 USD | 39,583.74 USD | `+13.43%` | -2,827,313.52 USD | `+0.47` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `9.01` | `9.08` | `8.93` | `8.96` | `840,436` | 7,558,281.78 USD | -1,066,050.82 USD | `-14.10%` | -675,045.77 USD | `-2.27` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `8.96` | `8.96` | `8.82` | `8.87` | `732,279` | 6,517,786.37 USD | -1,600,470.16 USD | `-24.56%` | -2,275,515.94 USD | `-2.72` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `8.87` | `8.88` | `8.86` | `8.88` | `33,240` | 294,834.55 USD | 39,779.06 USD | `+13.49%` | -2,235,736.88 USD | `+0.52` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | -426,486.82 USD | `+0.25` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -480,308.79 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.82` | `8.88` | `1,605,955` | 14,370,902.70 USD | -2,626,741.92 USD | `-18.28%` | -3,107,050.71 USD | `-1.38` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `9.00` | `9.02` | `8.55` | `8.59` | `3,515,330` | 30,612,875.98 USD | -2,423,031.38 USD | `-7.92%` | -749,324.84 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.59` | `8.80` | `8.57` | `8.62` | `1,816,830` | 15,790,058.74 USD | 58,580.54 USD | `+0.37%` | -690,744.30 USD | `+0.17` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | -426,486.82 USD | `+0.25` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -480,308.79 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.82` | `8.88` | `1,605,955` | 14,370,902.70 USD | -2,626,741.92 USD | `-18.28%` | -3,107,050.71 USD | `-1.38` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`8.88`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `8.88` | `20.8000` | 184.78 USD | 184.78 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `8.88` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.88` | `0.00%` | `-` |
| `BID` | `8.88` | `104.9800` | 932.56 USD | 932.56 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `8.88` | `143.7300` | 1,276.74 USD | 2,209.30 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.88` | `52.4900` | 466.24 USD | 2,675.54 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.88` | `16.0000` | 142.12 USD | 2,817.66 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.88` | `50.0000` | 444.11 USD | 3,261.77 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.88` | `675.5000` | 5,999.86 USD | 9,261.63 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.88` | `382.6400` | 3,398.61 USD | 12,660.24 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.88` | `52.4900` | 466.21 USD | 13,126.45 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.88` | `112.3000` | 997.41 USD | 14,123.86 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.88` | `16.0000` | 142.10 USD | 14,265.96 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.88` | `52.4900` | 466.17 USD | 14,732.14 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.88` | `39.1000` | 347.25 USD | 15,079.39 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.88` | `52.4900` | 466.16 USD | 15,545.55 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.88` | `39.6400` | 352.02 USD | 15,897.57 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.88` | `900.7900` | 7,999.11 USD | 23,896.68 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.88` | `52.4900` | 466.11 USD | 24,362.79 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.88` | `1126.1700` | 9,999.94 USD | 34,362.73 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.88` | `57.7600` | 512.87 USD | 34,875.60 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.88` | `112.6200` | 999.95 USD | 35,875.55 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.88` | `456.4200` | 4,052.51 USD | 39,928.06 USD | `2 orders` | `-0.05%` | `-` |
| `ASK` | `8.89` | `52.4900` | 466.62 USD | 42,765.04 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.89` | `5.2600` | 46.76 USD | 42,298.43 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.89` | `522.5700` | 4,645.28 USD | 42,251.67 USD | `3 orders` | `+0.07%` | `-` |
| `ASK` | `8.89` | `144.1900` | 1,281.69 USD | 37,606.39 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.89` | `682.6000` | 6,067.29 USD | 36,324.69 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.89` | `200.0000` | 1,777.68 USD | 30,257.40 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.89` | `1666.8600` | 14,815.55 USD | 28,479.72 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.89` | `52.4900` | 466.54 USD | 13,664.17 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.89` | `153.8100` | 1,367.08 USD | 13,197.63 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `8.89` | `91.7000` | 815.02 USD | 11,830.55 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.89` | `169.8200` | 1,509.33 USD | 11,015.53 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `8.89` | `91.7000` | 814.97 USD | 9,506.21 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.89` | `137.5600` | 1,222.54 USD | 8,691.23 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.89` | `5.8000` | 51.55 USD | 7,468.69 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.89` | `381.4900` | 3,390.30 USD | 7,417.15 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.89` | `191.8400` | 1,704.86 USD | 4,026.85 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.89` | `52.4900` | 466.47 USD | 2,321.98 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.89` | `145.7600` | 1,295.22 USD | 1,855.52 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.89` | `42.2600` | 375.51 USD | 560.29 USD | `2 orders` | `+0.02%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:36:01 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1489` | `0x7737...bf66` | `SHORT` | 1,522,992.51 USD | `171,568.06` | `7.43` | `8.87` | `113.16` | -247,447.49 USD | `-16.25%` | `10X Cross` |
| `1566` | `0xeadc...9d55` | `LONG` | 1,420,930.35 USD | `160,070.56` | `8.11` | `8.87` | `0.000000` | 123,292.78 USD | `+8.68%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `8.94` | 5,181.55 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 5.18K USD at 8.9425 USD [API] | `2026-10-27 21:41:02` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`9.22` (Vol: 221,300.00 USD, Dist: `+4.00%`) | Long MP=`8.46` (Vol: 190,100.00 USD, Dist: `--4.62%`)
  * 48H Horizon: Short MP=`9.22` (Vol: 242,900.00 USD, Dist: `+4.00%`) | Long MP=`8.46` (Vol: 190,100.00 USD, Dist: `--4.62%`)
  * 3D Horizon: Short MP=`9.22` (Vol: 264,100.00 USD, Dist: `+4.00%`) | Long MP=`8.75` (Vol: 159,700.00 USD, Dist: `--1.31%`)
  * 7D Horizon: Short MP=`9.28` (Vol: 419,200.00 USD, Dist: `+4.67%`) | Long MP=`8.54` (Vol: 343,100.00 USD, Dist: `--3.73%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `1.86` | 205.15 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 313.47 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 159.60 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 5,130.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 670.96 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 15,410.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 256.85 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 814.80 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 534.35 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 1,540.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 1,050.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 232.67 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111.12 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 132.01 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 404.38 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 151.88 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 7,700.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 1,600.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 835.12 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 109.95 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.69` | 177.69 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 3,600.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.81` | 356.02 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.88` | 387.50 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.00` | 162.64 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 159.29 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.18` | 174.89 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 466.95 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 2,150.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.32` | 852.47 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.51` | 1,220.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.54` | 662.02 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.54` | 4,790.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 486.93 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 2,680.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 3,280.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 15,400.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 240.48 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.78` | 15,690.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.79` | 111.24 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 467.01 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.88` | 276.70 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.89` | 4,180.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 527.19 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,230.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 760.08 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.99` | 329.11 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.03` | 167.78 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 314.59 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 504.74 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 318.46 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.11` | 155,370.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 250.20 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 396.06 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 2,300.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 300.91 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.24` | 1,730.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 640.70 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 1,360.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.30` | 232.41 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 716.11 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 660.46 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 21,080.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,720.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.51` | 367.41 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 121.38 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 2,770.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.57` | 967.98 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.59` | 34,430.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 22,270.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.64` | 4,080.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.66` | 317,420.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.71` | 2,340.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 238.86 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 2,890.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 736.72 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 580.50 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 106.65 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 22,060.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.92` | 1,330.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 11,720.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.99` | 447.98 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 331.68 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 105.61 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 3,650.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 265.10 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 405.14 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,550.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.11` | 3,200.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 137.02 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 4,390.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 187.29 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 487.21 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 2,560.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.22` | 715.31 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 2,630.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.26` | 1,450.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.32` | 277.04 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 105.25 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 284,770.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 5,110.00 USD | 888,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 883,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 883,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 3,270.00 USD | 876,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 1,050.00 USD | 873,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 3,620.00 USD | 871,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 868,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 1,100.00 USD | 859,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 858,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.70` | 506.54 USD | 856,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 16,610.00 USD | 855,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 839,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 6,780.00 USD | 837,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 16,960.00 USD | 830,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 4,260.00 USD | 813,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 1,500.00 USD | 809,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 2,820.00 USD | 808,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 1,360.00 USD | 805,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 4,410.00 USD | 804,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.84` | 1,490.00 USD | 799,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.86` | 46,350.00 USD | 798,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,340.00 USD | 751,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.89` | 5,250.00 USD | 748,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.91` | 269.30 USD | 743,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 3,760.00 USD | 742,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 5,070.00 USD | 739,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 636.74 USD | 734,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.99` | 805.58 USD | 733,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 746.58 USD | 732,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 20,860.00 USD | 731,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.04` | 4,100.00 USD | 711,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 6,700.00 USD | 706,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,670.00 USD | 700,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 28,230.00 USD | 698,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 670,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 2,300.00 USD | 669,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,950.00 USD | 667,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 646,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 718.11 USD | 645,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.24` | 179.65 USD | 644,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 185.83 USD | 644,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 1,020.00 USD | 644,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,420.00 USD | 643,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 19,790.00 USD | 606,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.32` | 168.76 USD | 586,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 4,910.00 USD | 586,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 2,450.00 USD | 581,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.34` | 4,370.00 USD | 579,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.37` | 5,720.00 USD | 575,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 5,400.00 USD | 569,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 17,770.00 USD | 563,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.39` | 1,550.00 USD | 546,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.42` | 500.00 USD | 544,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 210.99 USD | 544,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 1,370.00 USD | 543,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 4,590.00 USD | 542,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 3,210.00 USD | 537,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 1,580.00 USD | 534,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 1,080.00 USD | 533,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.53` | 433.52 USD | 532,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 531,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 157.14 USD | 527,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.57` | 4,380.00 USD | 527,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.59` | 25,140.00 USD | 522,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.62` | 312.22 USD | 497,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 497,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.63` | 514.52 USD | 496,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 496,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.67` | 1,740.00 USD | 496,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.68` | 1,120.00 USD | 494,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.70` | 1,460.00 USD | 493,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.71` | 19,410.00 USD | 491,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.72` | 2,550.00 USD | 472,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.75` | 9,500,000.00 USD | 9,500,000.00 USD | 976.80 USD | 5,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.75` | 893.76 USD | 469,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 468,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.77` | 9,490,000.00 USD | 9,490,000.00 USD | 17,170.00 USD | 4,900.00 USD | 4,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.78` | 695.32 USD | 468,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.79` | 3,900.00 USD | 467,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.79` | 9,460,000.00 USD | 9,460,000.00 USD | 19,090.00 USD | 4,540.00 USD | 15,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 1,940.00 USD | 463,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.80` | 633.77 USD | 461,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.81` | 9,420,000.00 USD | 9,420,000.00 USD | 2,240.00 USD | 11,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.82` | 5,280.00 USD | 461,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.83` | 9,410,000.00 USD | 9,410,000.00 USD | 28,130.00 USD | 2,130.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 10,930.00 USD | 455,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.85` | 9,360,000.00 USD | 9,360,000.00 USD | 15,410.00 USD | 7,840.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.86` | 2,110.00 USD | 445,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.87` | 9,330,000.00 USD | 9,330,000.00 USD | 39,380.00 USD | 1,540.00 USD | 21,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 442,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.89` | 9,270,000.00 USD | 9,270,000.00 USD | 25,450.00 USD | 18,320.00 USD | 24,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 2,410.00 USD | 442,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.91` | 9,200,000.00 USD | 9,200,000.00 USD | 29,920.00 USD | 11,120.00 USD | 17,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 923.42 USD | 439,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.93` | 5,020,000.00 USD | 5,020,000.00 USD | 16,100.00 USD | 2,950.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.93` | 9,140,000.00 USD | 9,140,000.00 USD | 78,470.00 USD | 7,330.00 USD | 14,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 1,820.00 USD | 439,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 127,110.00 USD | 437,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 4,990,000.00 USD | 4,990,000.00 USD | 7,720.00 USD | 8,290.00 USD | 4,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.95` | 9,040,000.00 USD | 9,040,000.00 USD | 30,870.00 USD | 9,500.00 USD | 42,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 12,180.00 USD | 310,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.96` | 229.31 USD | 297,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.97` | 4,970,000.00 USD | 4,970,000.00 USD | 12,260.00 USD | 4,010.00 USD | 3,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.97` | 8,960,000.00 USD | 8,960,000.00 USD | 24,400.00 USD | 18,700.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,600.00 USD | 297,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 4,950,000.00 USD | 4,950,000.00 USD | 13,040.00 USD | 2,050.00 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.99` | 8,870,000.00 USD | 8,870,000.00 USD | 49,120.00 USD | 7,410.00 USD | 45,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 210.99 USD | 296,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.01` | 4,940,000.00 USD | 4,940,000.00 USD | 7,650.00 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.01` | 8,770,000.00 USD | 8,770,000.00 USD | 49,240.00 USD | 17,990.00 USD | 470.04 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 957.70 USD | 295,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.03` | 4,920,000.00 USD | 4,920,000.00 USD | 19,600.00 USD | 2,310.00 USD | 4,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.03` | 8,700,000.00 USD | 8,700,000.00 USD | 104,360.00 USD | 23,930.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 88,380.00 USD | 294,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.04` | 6,890.00 USD | 206,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.05` | 4,900,000.00 USD | 4,900,000.00 USD | 25,440.00 USD | 4,800.00 USD | 13,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.05` | 8,530,000.00 USD | 8,530,000.00 USD | 36,050.00 USD | 29,270.00 USD | 62,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.05` | 3,340.00 USD | 199,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.06` | 37,830.00 USD | 196,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.07` | 4,850,000.00 USD | 4,850,000.00 USD | 18,870.00 USD | 4,100.00 USD | 11,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.07` | 8,400,000.00 USD | 8,400,000.00 USD | 63,920.00 USD | 10,930.00 USD | 75,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.09` | 617.61 USD | 158,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.09` | 4,820,000.00 USD | 4,820,000.00 USD | 14,430.00 USD | 2,630.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.09` | 8,250,000.00 USD | 8,250,000.00 USD | 36,390.00 USD | 16,210.00 USD | 27,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.11` | 4,790,000.00 USD | 4,790,000.00 USD | 27,330.00 USD | 7,990.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.11` | 8,170,000.00 USD | 8,170,000.00 USD | 36,560.00 USD | 10,160.00 USD | 7,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 241.26 USD | 157,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.13` | 4,750,000.00 USD | 4,750,000.00 USD | 16,140.00 USD | 693.45 USD | 8,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.13` | 8,110,000.00 USD | 8,110,000.00 USD | 32,750.00 USD | 11,560.00 USD | 20,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.15` | 4,720,000.00 USD | 4,720,000.00 USD | 31,790.00 USD | 662.47 USD | 5,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.15` | 8,050,000.00 USD | 8,050,000.00 USD | 91,880.00 USD | 5,090.00 USD | 46,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.16` | 871.61 USD | 157,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.17` | 4,690,000.00 USD | 4,690,000.00 USD | 5,060.00 USD | 2,120.00 USD | 59.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.17` | 7,900,000.00 USD | 7,900,000.00 USD | 6,560.00 USD | 7,770.00 USD | 9,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.19` | 4,030.00 USD | 156,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.19` | 4,680,000.00 USD | 4,680,000.00 USD | 5,040.00 USD | 1,980.00 USD | 486.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.19` | 7,880,000.00 USD | 7,880,000.00 USD | 30,780.00 USD | 3,170.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.20` | 2,380.00 USD | 152,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.21` | 577.06 USD | 150,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.21` | 4,670,000.00 USD | 4,670,000.00 USD | 10,320.00 USD | 2,310.00 USD | 431.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.21` | 7,840,000.00 USD | 7,840,000.00 USD | 23,630.00 USD | 0.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 6,220.00 USD | 149,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.22` | 2,100.00 USD | 143,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.23` | 4,660,000.00 USD | 4,660,000.00 USD | 25,950.00 USD | 4,080.00 USD | 43,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.23` | 7,800,000.00 USD | 7,800,000.00 USD | 21,610.00 USD | 3,480.00 USD | 115,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.23` | 1,160.00 USD | 141,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.24` | 1,120.00 USD | 140,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.25` | 4,580,000.00 USD | 4,580,000.00 USD | 16,630.00 USD | 1,150.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.25` | 7,660,000.00 USD | 7,660,000.00 USD | 55,820.00 USD | 5,750.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.26` | 13,810.00 USD | 139,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.27` | 4,560,000.00 USD | 4,560,000.00 USD | 11,620.00 USD | 14,210.00 USD | 21.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.27` | 7,590,000.00 USD | 7,590,000.00 USD | 65,020.00 USD | 14,400.00 USD | 8,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.28` | 3,360.00 USD | 125,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.29` | 498.26 USD | 121,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.29` | 4,530,000.00 USD | 4,530,000.00 USD | 109,970.00 USD | 16,540.00 USD | 45,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.29` | 7,500,000.00 USD | 7,500,000.00 USD | 116,340.00 USD | 19,520.00 USD | 52,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.29` | 23,710.00 USD | 121,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.30` | 33,500.00 USD | 97,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.31` | 4,360,000.00 USD | 4,360,000.00 USD | 110,650.00 USD | 24,540.00 USD | 20,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.31` | 7,310,000.00 USD | 7,310,000.00 USD | 80,550.00 USD | 13,500.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.31` | 4,550.00 USD | 64,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.33` | 4,200,000.00 USD | 4,200,000.00 USD | 23,540.00 USD | 26,770.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.33` | 7,210,000.00 USD | 7,210,000.00 USD | 58,510.00 USD | 36,210.00 USD | 19,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.34` | 4,630.00 USD | 59,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.35` | 4,140,000.00 USD | 4,140,000.00 USD | 20,780.00 USD | 16,080.00 USD | 22,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.35` | 7,090,000.00 USD | 7,090,000.00 USD | 95,370.00 USD | 5,340.00 USD | 82,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.36` | 3,180.00 USD | 55,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.37` | 7,160.00 USD | 51,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.37` | 4,080,000.00 USD | 4,080,000.00 USD | 25,490.00 USD | 10,400.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.37` | 6,910,000.00 USD | 6,910,000.00 USD | 92,990.00 USD | 31,220.00 USD | 24,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.38` | 670.00 USD | 44,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.39` | 4,010,000.00 USD | 4,010,000.00 USD | 99,010.00 USD | 14,620.00 USD | 90,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.39` | 6,760,000.00 USD | 6,760,000.00 USD | 197,900.00 USD | 8,930.00 USD | 68,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.39` | 1,680.00 USD | 44,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.40` | 832.52 USD | 42,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.41` | 3,810,000.00 USD | 3,810,000.00 USD | 102,240.00 USD | 26,510.00 USD | 88,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.41` | 6,490,000.00 USD | 6,490,000.00 USD | 122,320.00 USD | 32,690.00 USD | 244,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.43` | 3,590,000.00 USD | 3,590,000.00 USD | 62,380.00 USD | 47,320.00 USD | 32,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.43` | 6,090,000.00 USD | 6,090,000.00 USD | 179,770.00 USD | 62,350.00 USD | 73,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.44` | 188.61 USD | 41,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 588.70 USD | 41,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.45` | 3,450,000.00 USD | 3,450,000.00 USD | 108,980.00 USD | 23,170.00 USD | 51,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.45` | 5,770,000.00 USD | 5,770,000.00 USD | 210,670.00 USD | 59,180.00 USD | 89,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.46` | 4,100.00 USD | 40,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.46` | 1,970.00 USD | 36,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.47` | 3,260,000.00 USD | 3,260,000.00 USD | 238,630.00 USD | 38,320.00 USD | 62,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.47` | 5,410,000.00 USD | 5,410,000.00 USD | 384,150.00 USD | 70,760.00 USD | 190,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.47` | 14,370.00 USD | 34,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.48` | 1,160.00 USD | 20,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.49` | 2,920,000.00 USD | 2,920,000.00 USD | 248,730.00 USD | 70,410.00 USD | 51,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.49` | 4,770,000.00 USD | 4,770,000.00 USD | 268,080.00 USD | 54,550.00 USD | 118,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.49` | 870.23 USD | 19,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.51` | 6,380.00 USD | 18,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.51` | 2,550,000.00 USD | 2,550,000.00 USD | 80,200.00 USD | 65,960.00 USD | 48,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.51` | 4,330,000.00 USD | 4,330,000.00 USD | 202,090.00 USD | 129,490.00 USD | 139,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.52` | 2,640.00 USD | 2,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.53` | 2,360,000.00 USD | 2,360,000.00 USD | 78,070.00 USD | 45,720.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.53` | 3,850,000.00 USD | 3,850,000.00 USD | 415,280.00 USD | 66,260.00 USD | 317,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 6,350.00 USD | 11,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.54` | 1,550.00 USD | 5,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.55` | 2,170,000.00 USD | 2,170,000.00 USD | 84,620.00 USD | 25,290.00 USD | 62,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.55` | 3,060,000.00 USD | 3,060,000.00 USD | 279,560.00 USD | 136,440.00 USD | 16,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.55` | 1,060.00 USD | 4,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.57` | 2,000,000.00 USD | 2,000,000.00 USD | 142,280.00 USD | 23,160.00 USD | 141,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.57` | 2,620,000.00 USD | 2,620,000.00 USD | 709,710.00 USD | 94,290.00 USD | 76,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.59` | 1,700,000.00 USD | 1,700,000.00 USD | 158,710.00 USD | 51,270.00 USD | 65,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.59` | 1,740,000.00 USD | 1,740,000.00 USD | 279,060.00 USD | 118,220.00 USD | 87,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.61` | 2,980.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.61` | 1,420,000.00 USD | 1,420,000.00 USD | 103,430.00 USD | 36,000.00 USD | 66,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.61` | 1,260,000.00 USD | 1,260,000.00 USD | 88,710.00 USD | 35,810.00 USD | 229,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.63` | 1,210,000.00 USD | 1,210,000.00 USD | 140,670.00 USD | 19,620.00 USD | 32,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.63` | 904,370.00 USD | 904,370.00 USD | 51,260.00 USD | 25,450.00 USD | 23,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.65` | 1,020,000.00 USD | 1,020,000.00 USD | 119,470.00 USD | 38,180.00 USD | 30,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.65` | 803,820.00 USD | 803,820.00 USD | 45,780.00 USD | 16,520.00 USD | 37,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.67` | 833,510.00 USD | 833,510.00 USD | 69,760.00 USD | 25,380.00 USD | 28,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.67` | 704,440.00 USD | 704,440.00 USD | 23,440.00 USD | 24,870.00 USD | 173,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.69` | 709,790.00 USD | 709,790.00 USD | 39,070.00 USD | 0.00 USD | 10,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.69` | 482,220.00 USD | 482,220.00 USD | 70,540.00 USD | 0.00 USD | 270.26 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.71` | 660,620.00 USD | 660,620.00 USD | 26,720.00 USD | 11,690.00 USD | 18,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.73` | 603,230.00 USD | 603,230.00 USD | 44,990.00 USD | 2,720.00 USD | 5,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.75` | 550,390.00 USD | 550,390.00 USD | 32,080.00 USD | 16,010.00 USD | 35,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.75` | 411,400.00 USD | 411,400.00 USD | 144,660.00 USD | 19,690.00 USD | 56,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.77` | 466,480.00 USD | 466,480.00 USD | 132,830.00 USD | 23,560.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.77` | 190,450.00 USD | 190,450.00 USD | 26,810.00 USD | 0.00 USD | 81,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.79` | 284,370.00 USD | 284,370.00 USD | 32,240.00 USD | 12,000.00 USD | 9,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.79` | 82,400.00 USD | 82,400.00 USD | 27,360.00 USD | 25,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.81` | 230,250.00 USD | 230,250.00 USD | 57,590.00 USD | 5,690.00 USD | 17,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.81` | 29,750.00 USD | 29,750.00 USD | 0.00 USD | 8,450.00 USD | 21,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.83` | 149,420.00 USD | 149,420.00 USD | 30,220.00 USD | 0.00 USD | 21,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.85` | 98,130.00 USD | 98,130.00 USD | 29,490.00 USD | 0.00 USD | 68,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.87` | 67,380.00 USD | 67,380.00 USD | 67,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.87` | 134,760.00 USD | 134,760.00 USD | 67,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.87` | 78,770.00 USD | 78,770.00 USD | 0.00 USD | 0.00 USD | 78,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.87` | 157,550.00 USD | 157,550.00 USD | 0.00 USD | 0.00 USD | 78,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.89` | 202,030.00 USD | 202,030.00 USD | 0.00 USD | 0.00 USD | 44,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.91` | 212,520.00 USD | 212,520.00 USD | 0.00 USD | 0.00 USD | 77,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.91` | 273,030.00 USD | 273,030.00 USD | 0.00 USD | 0.00 USD | 71,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.93` | 224,090.00 USD | 224,090.00 USD | 8,060.00 USD | 0.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 236,210.00 USD | 236,210.00 USD | 643.50 USD | 11,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.99` | 367,270.00 USD | 367,270.00 USD | 94,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 237,290.00 USD | 237,290.00 USD | 1,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.01` | 470,770.00 USD | 470,770.00 USD | 67,320.00 USD | 36,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 348,510.00 USD | 348,510.00 USD | 30,260.00 USD | 62,570.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.03` | 591,340.00 USD | 591,340.00 USD | 4,290.00 USD | 101,140.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 412,930.00 USD | 412,930.00 USD | 3,690.00 USD | 25,650.00 USD | 35,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.05` | 648,800.00 USD | 648,800.00 USD | 35,710.00 USD | 4,910.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.07` | 506,700.00 USD | 506,700.00 USD | 16,740.00 USD | 27,950.00 USD | 49,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.07` | 689,170.00 USD | 689,170.00 USD | 3,990.00 USD | 14,140.00 USD | 22,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 706,160.00 USD | 706,160.00 USD | 100,490.00 USD | 23,610.00 USD | 75,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.09` | 983,450.00 USD | 983,450.00 USD | 150,640.00 USD | 8,680.00 USD | 134,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.11` | 931,860.00 USD | 931,860.00 USD | 117,180.00 USD | 32,050.00 USD | 76,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.11` | 2,420,000.00 USD | 2,420,000.00 USD | 847,950.00 USD | 37,620.00 USD | 546,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 1,220,000.00 USD | 1,220,000.00 USD | 190,660.00 USD | 51,740.00 USD | 46,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.13` | 3,620,000.00 USD | 3,620,000.00 USD | 690,230.00 USD | 26,540.00 USD | 484,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.13` | 314.34 USD | 2,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.15` | 1,390,000.00 USD | 1,390,000.00 USD | 91,560.00 USD | 27,820.00 USD | 46,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.15` | 4,260,000.00 USD | 4,260,000.00 USD | 357,020.00 USD | 38,700.00 USD | 249,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 1,630,000.00 USD | 1,630,000.00 USD | 133,730.00 USD | 28,140.00 USD | 83,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.17` | 5,040,000.00 USD | 5,040,000.00 USD | 365,640.00 USD | 133,490.00 USD | 274,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 2,010,000.00 USD | 2,010,000.00 USD | 231,820.00 USD | 75,410.00 USD | 72,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.19` | 5,820,000.00 USD | 5,820,000.00 USD | 487,090.00 USD | 101,150.00 USD | 193,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 2,280,000.00 USD | 2,280,000.00 USD | 165,980.00 USD | 23,960.00 USD | 74,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.21` | 6,750,000.00 USD | 6,750,000.00 USD | 527,540.00 USD | 132,850.00 USD | 277,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.23` | 2,480,000.00 USD | 2,480,000.00 USD | 158,900.00 USD | 10,510.00 USD | 38,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.23` | 7,760,000.00 USD | 7,760,000.00 USD | 562,300.00 USD | 82,070.00 USD | 360,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 2,570,000.00 USD | 2,570,000.00 USD | 54,970.00 USD | 20,640.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.25` | 8,250,000.00 USD | 8,250,000.00 USD | 277,290.00 USD | 73,690.00 USD | 141,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 2,620,000.00 USD | 2,620,000.00 USD | 37,410.00 USD | 14,380.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.27` | 8,580,000.00 USD | 8,580,000.00 USD | 156,190.00 USD | 118,550.00 USD | 54,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 100.93 USD | 3,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.29` | 2,760,000.00 USD | 2,760,000.00 USD | 68,980.00 USD | 22,120.00 USD | 41,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.29` | 9,440,000.00 USD | 9,440,000.00 USD | 468,150.00 USD | 100,200.00 USD | 290,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 2,910,000.00 USD | 2,910,000.00 USD | 98,940.00 USD | 20,310.00 USD | 32,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.31` | 10,130,000.00 USD | 10,130,000.00 USD | 307,520.00 USD | 55,090.00 USD | 329,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 2,970,000.00 USD | 2,970,000.00 USD | 26,890.00 USD | 8,530.00 USD | 26,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.33` | 10,500,000.00 USD | 10,500,000.00 USD | 124,660.00 USD | 64,710.00 USD | 178,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.35` | 4,570.00 USD | 7,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.35` | 3,060,000.00 USD | 3,060,000.00 USD | 45,690.00 USD | 8,000.00 USD | 37,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.35` | 10,980,000.00 USD | 10,980,000.00 USD | 289,480.00 USD | 93,460.00 USD | 96,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 3,220,000.00 USD | 3,220,000.00 USD | 104,690.00 USD | 27,030.00 USD | 31,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.37` | 11,490,000.00 USD | 11,490,000.00 USD | 369,360.00 USD | 34,660.00 USD | 108,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.38` | 404,120.00 USD | 411,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.39` | 3,320,000.00 USD | 3,320,000.00 USD | 64,010.00 USD | 5,770.00 USD | 30,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.39` | 11,850,000.00 USD | 11,850,000.00 USD | 206,980.00 USD | 62,160.00 USD | 87,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.41` | 3,420,000.00 USD | 3,420,000.00 USD | 74,010.00 USD | 2,860.00 USD | 16,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.41` | 12,300,000.00 USD | 12,300,000.00 USD | 265,320.00 USD | 41,500.00 USD | 147,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 2,470.00 USD | 414,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.43` | 3,460,000.00 USD | 3,460,000.00 USD | 19,650.00 USD | 7,570.00 USD | 16,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.43` | 12,550,000.00 USD | 12,550,000.00 USD | 101,970.00 USD | 43,920.00 USD | 95,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.45` | 3,470,000.00 USD | 3,470,000.00 USD | 4,600.00 USD | 4,940.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.45` | 12,680,000.00 USD | 12,680,000.00 USD | 105,560.00 USD | 16,970.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.46` | 5,040.00 USD | 419,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.47` | 3,510,000.00 USD | 3,510,000.00 USD | 19,700.00 USD | 11,450.00 USD | 192.20 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.47` | 12,790,000.00 USD | 12,790,000.00 USD | 53,420.00 USD | 32,300.00 USD | 25,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.49` | 3,540,000.00 USD | 3,540,000.00 USD | 21,020.00 USD | 572.85 USD | 10,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.49` | 12,900,000.00 USD | 12,900,000.00 USD | 26,920.00 USD | 36,710.00 USD | 42,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.51` | 3,560,000.00 USD | 3,560,000.00 USD | 14,250.00 USD | 3,160.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.51` | 13,230,000.00 USD | 13,230,000.00 USD | 148,110.00 USD | 43,360.00 USD | 142,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.53` | 3,610,000.00 USD | 3,610,000.00 USD | 36,270.00 USD | 7,630.00 USD | 5,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.53` | 13,440,000.00 USD | 13,440,000.00 USD | 187,750.00 USD | 15,360.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.55` | 3,630,000.00 USD | 3,630,000.00 USD | 9,090.00 USD | 7,800.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.55` | 13,510,000.00 USD | 13,510,000.00 USD | 28,850.00 USD | 19,960.00 USD | 20,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.57` | 3,650,000.00 USD | 3,650,000.00 USD | 6,150.00 USD | 4,390.00 USD | 7,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.57` | 13,670,000.00 USD | 13,670,000.00 USD | 116,450.00 USD | 14,280.00 USD | 33,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.59` | 3,670,000.00 USD | 3,670,000.00 USD | 5,680.00 USD | 1,820.00 USD | 8,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.59` | 13,740,000.00 USD | 13,740,000.00 USD | 29,010.00 USD | 15,650.00 USD | 23,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.61` | 3,720,000.00 USD | 3,720,000.00 USD | 26,000.00 USD | 3,090.00 USD | 22,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.61` | 13,860,000.00 USD | 13,860,000.00 USD | 82,080.00 USD | 13,850.00 USD | 28,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.63` | 3,740,000.00 USD | 3,740,000.00 USD | 10,190.00 USD | 4,370.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.63` | 13,920,000.00 USD | 13,920,000.00 USD | 42,830.00 USD | 4,500.00 USD | 6,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.65` | 3,760,000.00 USD | 3,760,000.00 USD | 11,470.00 USD | 4,150.00 USD | 5,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.65` | 13,990,000.00 USD | 13,990,000.00 USD | 33,020.00 USD | 20,230.00 USD | 18,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.67` | 3,780,000.00 USD | 3,780,000.00 USD | 11,930.00 USD | 3,480.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.67` | 14,060,000.00 USD | 14,060,000.00 USD | 31,000.00 USD | 24,380.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.69` | 545.17 USD | 419,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.69` | 3,800,000.00 USD | 3,800,000.00 USD | 12,900.00 USD | 2,950.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.69` | 14,240,000.00 USD | 14,240,000.00 USD | 121,550.00 USD | 17,380.00 USD | 33,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.70` | 466.33 USD | 420,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.71` | 3,820,000.00 USD | 3,820,000.00 USD | 8,030.00 USD | 8,290.00 USD | 4,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.71` | 14,370,000.00 USD | 14,370,000.00 USD | 81,870.00 USD | 9,500.00 USD | 42,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.73` | 3,820,000.00 USD | 3,820,000.00 USD | 74.90 USD | 1,790.00 USD | 43.57 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.73` | 14,390,000.00 USD | 14,390,000.00 USD | 5,340.00 USD | 3,160.00 USD | 11,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 420,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.75` | 3,840,000.00 USD | 3,840,000.00 USD | 12,190.00 USD | 2,210.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.75` | 14,460,000.00 USD | 14,460,000.00 USD | 25,630.00 USD | 15,540.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.77` | 3,860,000.00 USD | 3,860,000.00 USD | 12,560.00 USD | 2,050.00 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.77` | 14,570,000.00 USD | 14,570,000.00 USD | 51,320.00 USD | 7,410.00 USD | 46,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.79` | 3,870,000.00 USD | 3,870,000.00 USD | 5,800.00 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.79` | 14,630,000.00 USD | 14,630,000.00 USD | 48,830.00 USD | 17,990.00 USD | 729.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.81` | 3,890,000.00 USD | 3,890,000.00 USD | 16,710.00 USD | 2,310.00 USD | 4,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.81` | 14,810,000.00 USD | 14,810,000.00 USD | 103,830.00 USD | 23,930.00 USD | 48,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.83` | 3,930,000.00 USD | 3,930,000.00 USD | 23,590.00 USD | 4,800.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.83` | 14,930,000.00 USD | 14,930,000.00 USD | 31,840.00 USD | 29,270.00 USD | 62,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.85` | 3,950,000.00 USD | 3,950,000.00 USD | 10,830.00 USD | 1,700.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.85` | 15,040,000.00 USD | 15,040,000.00 USD | 50,490.00 USD | 2,210.00 USD | 49,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.87` | 3,960,000.00 USD | 3,960,000.00 USD | 4,810.00 USD | 2,400.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.87` | 15,090,000.00 USD | 15,090,000.00 USD | 15,580.00 USD | 8,710.00 USD | 25,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.89` | 3,990,000.00 USD | 3,990,000.00 USD | 12,390.00 USD | 2,630.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.89` | 15,170,000.00 USD | 15,170,000.00 USD | 33,970.00 USD | 16,210.00 USD | 27,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.91` | 4,030,000.00 USD | 4,030,000.00 USD | 26,950.00 USD | 7,990.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.91` | 15,220,000.00 USD | 15,220,000.00 USD | 32,670.00 USD | 10,160.00 USD | 7,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.93` | 4,060,000.00 USD | 4,060,000.00 USD | 15,110.00 USD | 693.45 USD | 8,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.93` | 15,280,000.00 USD | 15,280,000.00 USD | 31,960.00 USD | 11,560.00 USD | 20,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.95` | 4,070,000.00 USD | 4,070,000.00 USD | 16,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.95` | 15,360,000.00 USD | 15,360,000.00 USD | 55,780.00 USD | 3,730.00 USD | 24,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.97` | 4,090,000.00 USD | 4,090,000.00 USD | 12,840.00 USD | 662.47 USD | 5,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.97` | 15,420,000.00 USD | 15,420,000.00 USD | 29,800.00 USD | 1,360.00 USD | 21,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.99` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 2,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.99` | 15,430,000.00 USD | 15,430,000.00 USD | 840.10 USD | 7,770.00 USD | 8,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.01` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 1,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.01` | 15,450,000.00 USD | 15,450,000.00 USD | 15,960.00 USD | 3,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.02` | 4,100,000.00 USD | 4,100,000.00 USD | 6,510.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.03` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 0.00 USD | 13,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.04` | 263.92 USD | 420,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `10.04` | 15,470,000.00 USD | 15,470,000.00 USD | 6,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.11` | 34,990.00 USD | 455,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.21` | 7,330.00 USD | 463,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.35` | 3,380.00 USD | 466,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 466,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.71` | 218.91 USD | 467,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.96` | 1,920.00 USD | 469,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 476,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 11,810.00 USD | 487,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.57` | 770.89 USD | 488,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 500,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.84` | 1,350.00 USD | 502,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.87` | 59,330.00 USD | 561,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.90` | 747.28 USD | 562,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.94` | 34,370.00 USD | 596,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.04` | 13,480.00 USD | 610,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.10` | 140.91 USD | 610,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 611,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 612,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.54` | 427.78 USD | 612,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.79` | 953.38 USD | 613,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.95` | 144.34 USD | 613,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.96` | 102.68 USD | 613,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 701,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 234,840.00 USD | 936,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 940,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 940,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 941,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.24` | 3,950.00 USD | 945,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.55` | 238.85 USD | 945,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.62` | 314.95 USD | 945,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 946,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.71` | 2,440.00 USD | 948,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.91` | 294.27 USD | 949,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.12` | 151,150.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.38` | 20,000.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.47` | 110.03 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.70` | 23,590.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.77` | 117.45 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.25` | 263,300.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.43` | 82,790.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 162.26 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.02` | 191.87 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.14` | 1,710.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.46` | 101.47 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.61` | 2,040.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.62` | 4,120.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.64` | 4,930.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.66` | 2,660.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.70` | 108.89 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.77` | 152.96 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.82` | 202.49 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.88` | 602.92 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.86` | 2,340,000.00 USD | 0.00 USD | 205.15 USD | `-78.98%` | `110.00` |
| `Live` | `Long` | `1.89` | 2,340,000.00 USD | 0.00 USD | 229.50 USD | `-78.76%` | `121.75` |
| `Live` | `Long` | `2.00` | 2,340,000.00 USD | 0.00 USD | 159.60 USD | `-77.52%` | `80.00` |
| `Live` | `Long` | `2.04` | 2,340,000.00 USD | 0.00 USD | 110.52 USD | `-77.07%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,340,000.00 USD | 0.00 USD | 4,920.00 USD | `-76.73%` | `2,382.76` |
| `Live` | `Long` | `2.25` | 2,330,000.00 USD | 0.00 USD | 111.40 USD | `-74.70%` | `49.62` |
| `Live` | `Long` | `2.29` | 2,330,000.00 USD | 0.00 USD | 372.09 USD | `-74.25%` | `162.84` |
| `Live` | `Long` | `2.40` | 2,330,000.00 USD | 0.00 USD | 263.45 USD | `-73.01%` | `110.00` |
| `Live` | `Long` | `2.42` | 2,330,000.00 USD | 0.00 USD | 814.80 USD | `-72.67%` | `336.00` |
| `Live` | `Long` | `2.50` | 2,330,000.00 USD | 0.00 USD | 17,510.00 USD | `-71.77%` | `6,990.57` |
| `Live` | `Long` | `2.52` | 2,310,000.00 USD | 0.00 USD | 1,680.00 USD | `-71.54%` | `666.20` |
| `Live` | `Long` | `2.58` | 2,310,000.00 USD | 0.00 USD | 268.14 USD | `-70.87%` | `103.73` |
| `Live` | `Long` | `2.69` | 2,310,000.00 USD | 0.00 USD | 600.69 USD | `-69.63%` | `222.89` |
| `Live` | `Long` | `2.87` | 2,310,000.00 USD | 0.00 USD | 232.67 USD | `-67.71%` | `81.21` |
| `Live` | `Long` | `2.90` | 2,310,000.00 USD | 0.00 USD | 1,090.00 USD | `-67.37%` | `377.71` |
| `Live` | `Long` | `2.94` | 2,310,000.00 USD | 0.00 USD | 44,510.00 USD | `-66.92%` | `15,165.76` |
| `Live` | `Long` | `2.98` | 2,260,000.00 USD | 0.00 USD | 111.12 USD | `-66.47%` | `37.35` |
| `Live` | `Long` | `3.13` | 2,260,000.00 USD | 0.00 USD | 674.12 USD | `-64.67%` | `215.03` |
| `Live` | `Long` | `3.19` | 2,260,000.00 USD | 0.00 USD | 1,500.00 USD | `-64.10%` | `470.82` |
| `Live` | `Long` | `3.23` | 2,260,000.00 USD | 0.00 USD | 404.38 USD | `-63.54%` | `125.00` |
| `Live` | `Long` | `3.31` | 2,260,000.00 USD | 0.00 USD | 293.24 USD | `-62.64%` | `88.46` |
| `Live` | `Long` | `3.37` | 2,260,000.00 USD | 0.00 USD | 389.53 USD | `-62.08%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,260,000.00 USD | 0.00 USD | 297.24 USD | `-61.96%` | `88.07` |
| `Live` | `Long` | `3.67` | 2,260,000.00 USD | 0.00 USD | 109.95 USD | `-58.69%` | `30.00` |
| `Live` | `Long` | `3.71` | 2,260,000.00 USD | 0.00 USD | 2,110.00 USD | `-58.24%` | `568.43` |
| `Live` | `Long` | `3.75` | 2,260,000.00 USD | 0.00 USD | 1,500.00 USD | `-57.68%` | `400.00` |
| `Live` | `Long` | `3.81` | 2,260,000.00 USD | 0.00 USD | 2,130.00 USD | `-57.00%` | `558.69` |
| `Live` | `Long` | `3.83` | 2,250,000.00 USD | 0.00 USD | 8,720.00 USD | `-56.78%` | `2,273.34` |
| `Live` | `Long` | `3.90` | 2,250,000.00 USD | 0.00 USD | 131.73 USD | `-56.10%` | `33.82` |
| `Live` | `Long` | `3.94` | 2,250,000.00 USD | 0.00 USD | 1,290.00 USD | `-55.54%` | `326.92` |
| `Live` | `Long` | `4.03` | 2,240,000.00 USD | 0.00 USD | 402.70 USD | `-54.64%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,240,000.00 USD | 0.00 USD | 152.29 USD | `-54.41%` | `37.65` |
| `Live` | `Long` | `4.12` | 2,240,000.00 USD | 0.00 USD | 412.50 USD | `-53.51%` | `100.00` |
| `Live` | `Long` | `4.14` | 2,240,000.00 USD | 0.00 USD | 159.29 USD | `-53.29%` | `38.43` |
| `Live` | `Long` | `4.18` | 2,240,000.00 USD | 0.00 USD | 174.89 USD | `-52.83%` | `41.79` |
| `Live` | `Long` | `4.21` | 2,240,000.00 USD | 0.00 USD | 113.53 USD | `-52.61%` | `27.00` |
| `Live` | `Long` | `4.21` | 2,240,000.00 USD | 0.00 USD | 171.17 USD | `-52.50%` | `40.61` |
| `Live` | `Long` | `4.24` | 2,240,000.00 USD | 0.00 USD | 169.40 USD | `-52.27%` | `40.00` |
| `Live` | `Long` | `4.32` | 2,240,000.00 USD | 0.00 USD | 852.47 USD | `-51.37%` | `197.56` |
| `Live` | `Long` | `4.38` | 2,240,000.00 USD | 0.00 USD | 210.96 USD | `-50.69%` | `48.22` |
| `Live` | `Long` | `4.42` | 2,240,000.00 USD | 0.00 USD | 2,230.00 USD | `-50.13%` | `504.56` |
| `Live` | `Long` | `4.59` | 2,240,000.00 USD | 0.00 USD | 30,970.00 USD | `-48.21%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,210,000.00 USD | 0.00 USD | 1,160.00 USD | `-47.99%` | `251.49` |
| `Live` | `Long` | `4.62` | 2,210,000.00 USD | 0.00 USD | 2,680.00 USD | `-47.88%` | `579.06` |
| `Live` | `Long` | `4.67` | 2,200,000.00 USD | 0.00 USD | 3,280.00 USD | `-47.42%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,200,000.00 USD | 0.00 USD | 1,490.00 USD | `-47.31%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,200,000.00 USD | 0.00 USD | 15,400.00 USD | `-47.20%` | `3,287.97` |
| `Live` | `Long` | `4.71` | 2,180,000.00 USD | 0.00 USD | 1,270.00 USD | `-46.86%` | `270.00` |
| `Live` | `Long` | `4.74` | 2,180,000.00 USD | 0.00 USD | 4,990.00 USD | `-46.64%` | `1,053.00` |
| `Live` | `Long` | `4.75` | 2,180,000.00 USD | 0.00 USD | 240.48 USD | `-46.52%` | `50.68` |
| `Live` | `Long` | `4.76` | 2,180,000.00 USD | 0.00 USD | 105.64 USD | `-46.30%` | `22.17` |
| `Live` | `Long` | `4.79` | 2,180,000.00 USD | 0.00 USD | 15,760.00 USD | `-45.96%` | `3,286.00` |
| `Live` | `Long` | `4.83` | 2,160,000.00 USD | 0.00 USD | 467.01 USD | `-45.51%` | `96.59` |
| `Live` | `Long` | `4.86` | 2,160,000.00 USD | 0.00 USD | 112.64 USD | `-45.28%` | `23.20` |
| `Live` | `Long` | `4.89` | 2,160,000.00 USD | 0.00 USD | 146.85 USD | `-44.83%` | `30.00` |
| `Live` | `Long` | `4.91` | 2,160,000.00 USD | 0.00 USD | 527.19 USD | `-44.72%` | `107.48` |
| `Live` | `Long` | `4.92` | 2,160,000.00 USD | 0.00 USD | 1,230.00 USD | `-44.61%` | `251.00` |
| `Live` | `Long` | `4.95` | 2,160,000.00 USD | 0.00 USD | 4,080.00 USD | `-44.27%` | `824.62` |
| `Live` | `Long` | `4.96` | 2,160,000.00 USD | 0.00 USD | 945.36 USD | `-44.16%` | `190.79` |
| `Live` | `Long` | `4.97` | 2,150,000.00 USD | 0.00 USD | 282.23 USD | `-43.93%` | `56.73` |
| `Live` | `Long` | `4.99` | 2,150,000.00 USD | 0.00 USD | 329.11 USD | `-43.82%` | `66.02` |
| `Live` | `Long` | `5.01` | 2,150,000.00 USD | 0.00 USD | 56,390.00 USD | `-43.48%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,100,000.00 USD | 0.00 USD | 167.78 USD | `-43.37%` | `33.39` |
| `Live` | `Long` | `5.04` | 2,100,000.00 USD | 0.00 USD | 314.59 USD | `-43.25%` | `62.48` |
| `Live` | `Long` | `5.04` | 2,100,000.00 USD | 0.00 USD | 484.57 USD | `-43.14%` | `96.05` |
| `Live` | `Long` | `5.05` | 2,100,000.00 USD | 0.00 USD | 504.74 USD | `-43.03%` | `99.85` |
| `Live` | `Long` | `5.08` | 2,100,000.00 USD | 0.00 USD | 318.46 USD | `-42.80%` | `62.75` |
| `Live` | `Long` | `5.12` | 2,100,000.00 USD | 0.00 USD | 250.20 USD | `-42.24%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,100,000.00 USD | 0.00 USD | 156,680.00 USD | `-42.13%` | `30,512.33` |
| `Live` | `Long` | `5.17` | 1,940,000.00 USD | 0.00 USD | 2,300.00 USD | `-41.79%` | `445.16` |
| `Live` | `Long` | `5.17` | 1,940,000.00 USD | 0.00 USD | 1,620.00 USD | `-41.68%` | `312.94` |
| `Live` | `Long` | `5.18` | 1,930,000.00 USD | 0.00 USD | 150.57 USD | `-41.56%` | `29.04` |
| `Live` | `Long` | `5.21` | 1,930,000.00 USD | 0.00 USD | 300.91 USD | `-41.23%` | `57.70` |
| `Live` | `Long` | `5.29` | 1,930,000.00 USD | 0.00 USD | 640.70 USD | `-40.44%` | `121.23` |
| `Live` | `Long` | `5.30` | 1,930,000.00 USD | 0.00 USD | 2,880.00 USD | `-40.21%` | `543.81` |
| `Live` | `Long` | `5.33` | 1,930,000.00 USD | 0.00 USD | 716.11 USD | `-39.99%` | `134.48` |
| `Live` | `Long` | `5.36` | 1,930,000.00 USD | 0.00 USD | 589.05 USD | `-39.65%` | `110.00` |
| `Live` | `Long` | `5.39` | 1,930,000.00 USD | 0.00 USD | 660.46 USD | `-39.20%` | `122.42` |
| `Live` | `Long` | `5.42` | 1,930,000.00 USD | 0.00 USD | 21,080.00 USD | `-38.97%` | `3,892.05` |
| `Live` | `Long` | `5.42` | 1,910,000.00 USD | 0.00 USD | 160,400.00 USD | `-38.86%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,750,000.00 USD | 0.00 USD | 1,360.00 USD | `-38.75%` | `250.00` |
| `Live` | `Long` | `5.46` | 1,750,000.00 USD | 0.00 USD | 264.72 USD | `-38.41%` | `48.44` |
| `Live` | `Long` | `5.49` | 1,750,000.00 USD | 0.00 USD | 354.06 USD | `-38.18%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,750,000.00 USD | 0.00 USD | 19,290.00 USD | `-38.07%` | `3,510.41` |
| `Live` | `Long` | `5.51` | 1,730,000.00 USD | 0.00 USD | 367.41 USD | `-37.85%` | `66.62` |
| `Live` | `Long` | `5.54` | 1,730,000.00 USD | 0.00 USD | 121.38 USD | `-37.62%` | `21.93` |
| `Live` | `Long` | `5.57` | 1,730,000.00 USD | 0.00 USD | 967.98 USD | `-37.28%` | `173.94` |
| `Live` | `Long` | `5.58` | 1,720,000.00 USD | 0.00 USD | 63,260.00 USD | `-37.17%` | `11,347.58` |
| `Live` | `Long` | `5.59` | 1,660,000.00 USD | 0.00 USD | 34,430.00 USD | `-36.94%` | `6,153.60` |
| `Live` | `Long` | `5.63` | 1,630,000.00 USD | 0.00 USD | 22,590.00 USD | `-36.49%` | `4,009.72` |
| `Live` | `Long` | `5.64` | 1,600,000.00 USD | 0.00 USD | 4,120.00 USD | `-36.38%` | `730.59` |
| `Live` | `Long` | `5.68` | 1,600,000.00 USD | 0.00 USD | 404.32 USD | `-35.93%` | `71.12` |
| `Live` | `Long` | `5.71` | 1,600,000.00 USD | 0.00 USD | 2,340.00 USD | `-35.70%` | `409.39` |
| `Live` | `Long` | `5.74` | 1,600,000.00 USD | 0.00 USD | 238.86 USD | `-35.37%` | `41.65` |
| `Live` | `Long` | `5.75` | 1,600,000.00 USD | 0.00 USD | 125.70 USD | `-35.25%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,600,000.00 USD | 0.00 USD | 3,190.00 USD | `-35.14%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,590,000.00 USD | 0.00 USD | 10,850.00 USD | `-35.03%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,580,000.00 USD | 0.00 USD | 801.40 USD | `-34.91%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,580,000.00 USD | 0.00 USD | 2,890.00 USD | `-34.80%` | `500.00` |
| `Live` | `Long` | `5.79` | 1,580,000.00 USD | 0.00 USD | 736.72 USD | `-34.69%` | `127.13` |
| `Live` | `Long` | `5.80` | 1,580,000.00 USD | 0.00 USD | 326,400.00 USD | `-34.58%` | `56,226.53` |
| `Live` | `Long` | `5.82` | 1,250,000.00 USD | 0.00 USD | 106.65 USD | `-34.46%` | `18.34` |
| `Live` | `Long` | `5.89` | 1,250,000.00 USD | 0.00 USD | 22,060.00 USD | `-33.56%` | `3,742.70` |
| `Live` | `Long` | `5.91` | 1,230,000.00 USD | 0.00 USD | 399.18 USD | `-33.45%` | `67.60` |
| `Live` | `Long` | `5.96` | 1,230,000.00 USD | 0.00 USD | 11,720.00 USD | `-32.89%` | `1,968.19` |
| `Live` | `Long` | `5.97` | 1,220,000.00 USD | 0.00 USD | 2,120.00 USD | `-32.66%` | `354.27` |
| `Live` | `Long` | `5.99` | 1,220,000.00 USD | 0.00 USD | 447.98 USD | `-32.55%` | `74.85` |
| `Live` | `Long` | `6.00` | 1,220,000.00 USD | 0.00 USD | 341.56 USD | `-32.32%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,220,000.00 USD | 0.00 USD | 446.85 USD | `-32.21%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,210,000.00 USD | 0.00 USD | 1,690.00 USD | `-31.98%` | `280.10` |
| `Live` | `Long` | `6.04` | 1,210,000.00 USD | 0.00 USD | 105.61 USD | `-31.87%` | `17.47` |
| `Live` | `Long` | `6.05` | 1,210,000.00 USD | 0.00 USD | 1,310.00 USD | `-31.76%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,210,000.00 USD | 0.00 USD | 265.10 USD | `-31.65%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,210,000.00 USD | 0.00 USD | 1,690.00 USD | `-31.53%` | `278.94` |
| `Live` | `Long` | `6.08` | 1,210,000.00 USD | 0.00 USD | 405.14 USD | `-31.42%` | `66.58` |
| `Live` | `Long` | `6.09` | 1,210,000.00 USD | 0.00 USD | 3,550.00 USD | `-31.31%` | `582.81` |
| `Live` | `Long` | `6.11` | 1,210,000.00 USD | 0.00 USD | 5,560.00 USD | `-31.20%` | `911.19` |
| `Live` | `Long` | `6.12` | 1,200,000.00 USD | 0.00 USD | 137.02 USD | `-30.97%` | `22.37` |
| `Live` | `Long` | `6.14` | 1,200,000.00 USD | 0.00 USD | 238.61 USD | `-30.74%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,200,000.00 USD | 0.00 USD | 4,390.00 USD | `-30.63%` | `713.75` |
| `Live` | `Long` | `6.17` | 1,200,000.00 USD | 0.00 USD | 187.29 USD | `-30.52%` | `30.38` |
| `Live` | `Long` | `6.17` | 1,200,000.00 USD | 0.00 USD | 104.36 USD | `-30.41%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,200,000.00 USD | 0.00 USD | 310.25 USD | `-30.07%` | `50.00` |
| `Live` | `Long` | `6.21` | 1,190,000.00 USD | 0.00 USD | 2,560.00 USD | `-29.96%` | `411.30` |
| `Live` | `Long` | `6.22` | 1,190,000.00 USD | 0.00 USD | 715.31 USD | `-29.84%` | `114.91` |
| `Live` | `Long` | `6.25` | 1,190,000.00 USD | 0.00 USD | 971.10 USD | `-29.62%` | `155.50` |
| `Live` | `Long` | `6.25` | 1,190,000.00 USD | 0.00 USD | 2,060.00 USD | `-29.51%` | `330.00` |
| `Live` | `Long` | `6.26` | 1,190,000.00 USD | 0.00 USD | 1,450.00 USD | `-29.39%` | `232.17` |
| `Live` | `Long` | `6.28` | 1,190,000.00 USD | 0.00 USD | 2,510.00 USD | `-29.28%` | `400.00` |
| `Live` | `Long` | `6.29` | 1,180,000.00 USD | 0.00 USD | 147.51 USD | `-29.17%` | `23.47` |
| `Live` | `Long` | `6.32` | 1,180,000.00 USD | 0.00 USD | 277.04 USD | `-28.83%` | `43.87` |
| `Live` | `Long` | `6.33` | 1,180,000.00 USD | 0.00 USD | 105.25 USD | `-28.72%` | `16.64` |
| `Live` | `Long` | `6.36` | 1,180,000.00 USD | 0.00 USD | 4,470.00 USD | `-28.38%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,180,000.00 USD | 0.00 USD | 284,770.00 USD | `-28.27%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 894,820.00 USD | 0.00 USD | 5,110.00 USD | `-28.15%` | `801.31` |
| `Live` | `Long` | `6.38` | 889,710.00 USD | 0.00 USD | 1,690.00 USD | `-28.04%` | `265.15` |
| `Live` | `Long` | `6.42` | 888,020.00 USD | 0.00 USD | 306.32 USD | `-27.70%` | `47.75` |
| `Live` | `Long` | `6.43` | 887,710.00 USD | 0.00 USD | 6,780.00 USD | `-27.48%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 880,940.00 USD | 0.00 USD | 1,050.00 USD | `-27.14%` | `162.75` |
| `Live` | `Long` | `6.54` | 879,880.00 USD | 0.00 USD | 3,620.00 USD | `-26.35%` | `554.55` |
| `Live` | `Long` | `6.54` | 876,260.00 USD | 0.00 USD | 8,970.00 USD | `-26.24%` | `1,370.89` |
| `Live` | `Long` | `6.58` | 867,290.00 USD | 0.00 USD | 1,100.00 USD | `-25.79%` | `166.55` |
| `Live` | `Long` | `6.59` | 866,190.00 USD | 0.00 USD | 408.89 USD | `-25.67%` | `62.00` |
| `Live` | `Long` | `6.62` | 865,780.00 USD | 0.00 USD | 2,110.00 USD | `-25.45%` | `318.57` |
| `Live` | `Long` | `6.70` | 863,670.00 USD | 0.00 USD | 506.54 USD | `-24.55%` | `75.66` |
| `Live` | `Long` | `6.71` | 863,170.00 USD | 0.00 USD | 19,850.00 USD | `-24.43%` | `2,960.22` |
| `Live` | `Long` | `6.75` | 843,320.00 USD | 0.00 USD | 1,330.00 USD | `-23.98%` | `196.95` |
| `Live` | `Long` | `6.78` | 841,990.00 USD | 0.00 USD | 6,780.00 USD | `-23.64%` | `1,000.00` |
| `Live` | `Long` | `6.79` | 835,220.00 USD | 0.00 USD | 16,960.00 USD | `-23.53%` | `2,500.00` |
| `Live` | `Long` | `6.79` | 818,250.00 USD | 0.00 USD | 4,260.00 USD | `-23.42%` | `626.24` |
| `Live` | `Long` | `6.80` | 814,000.00 USD | 0.00 USD | 1,500.00 USD | `-23.31%` | `220.95` |
| `Live` | `Long` | `6.82` | 812,490.00 USD | 0.00 USD | 2,670.00 USD | `-23.19%` | `391.11` |
| `Live` | `Long` | `6.83` | 809,830.00 USD | 0.00 USD | 158.14 USD | `-23.08%` | `23.17` |
| `Live` | `Long` | `6.83` | 809,670.00 USD | 0.00 USD | 4,410.00 USD | `-22.97%` | `644.73` |
| `Live` | `Long` | `6.86` | 805,260.00 USD | 0.00 USD | 18,930.00 USD | `-22.74%` | `2,761.63` |
| `Live` | `Long` | `6.87` | 786,330.00 USD | 0.00 USD | 3,340.00 USD | `-22.63%` | `486.46` |
| `Live` | `Long` | `6.88` | 782,990.00 USD | 0.00 USD | 1,380.00 USD | `-22.52%` | `200.00` |
| `Live` | `Long` | `6.89` | 781,620.00 USD | 0.00 USD | 32,830.00 USD | `-22.29%` | `4,761.63` |
| `Live` | `Long` | `6.91` | 748,790.00 USD | 0.00 USD | 269.30 USD | `-22.18%` | `39.00` |
| `Live` | `Long` | `6.95` | 748,520.00 USD | 0.00 USD | 3,760.00 USD | `-21.73%` | `541.68` |
| `Live` | `Long` | `6.96` | 744,760.00 USD | 0.00 USD | 3,480.00 USD | `-21.62%` | `500.00` |
| `Live` | `Long` | `6.96` | 741,280.00 USD | 0.00 USD | 636.74 USD | `-21.50%` | `91.42` |
| `Live` | `Long` | `7.00` | 740,640.00 USD | 0.00 USD | 746.58 USD | `-21.17%` | `106.73` |
| `Live` | `Long` | `7.00` | 739,890.00 USD | 0.00 USD | 22,390.00 USD | `-21.05%` | `3,195.81` |
| `Live` | `Long` | `7.04` | 717,510.00 USD | 0.00 USD | 811.35 USD | `-20.71%` | `115.33` |
| `Live` | `Long` | `7.04` | 716,700.00 USD | 0.00 USD | 4,100.00 USD | `-20.60%` | `581.44` |
| `Live` | `Long` | `7.08` | 712,600.00 USD | 0.00 USD | 6,700.00 USD | `-20.26%` | `947.44` |
| `Live` | `Long` | `7.08` | 705,900.00 USD | 0.00 USD | 1,670.00 USD | `-20.15%` | `236.20` |
| `Live` | `Long` | `7.09` | 704,220.00 USD | 0.00 USD | 1,620.00 USD | `-20.04%` | `228.41` |
| `Live` | `Long` | `7.11` | 702,600.00 USD | 0.00 USD | 28,230.00 USD | `-19.93%` | `3,972.61` |
| `Live` | `Long` | `7.12` | 674,380.00 USD | 0.00 USD | 379.66 USD | `-19.81%` | `53.36` |
| `Live` | `Long` | `7.13` | 674,000.00 USD | 0.00 USD | 2,300.00 USD | `-19.59%` | `322.72` |
| `Live` | `Long` | `7.14` | 671,700.00 USD | 0.00 USD | 20,950.00 USD | `-19.47%` | `2,931.56` |
| `Live` | `Long` | `7.18` | 650,750.00 USD | 0.00 USD | 1,440.00 USD | `-19.02%` | `200.00` |
| `Live` | `Long` | `7.21` | 649,310.00 USD | 0.00 USD | 581.02 USD | `-18.69%` | `80.53` |
| `Live` | `Long` | `7.24` | 648,730.00 USD | 0.00 USD | 179.65 USD | `-18.46%` | `24.83` |
| `Live` | `Long` | `7.25` | 648,550.00 USD | 0.00 USD | 185.83 USD | `-18.35%` | `25.65` |
| `Live` | `Long` | `7.29` | 648,370.00 USD | 0.00 USD | 36,560.00 USD | `-17.90%` | `5,019.00` |
| `Live` | `Long` | `7.29` | 611,800.00 USD | 0.00 USD | 19,790.00 USD | `-17.78%` | `2,712.69` |
| `Live` | `Long` | `7.32` | 592,010.00 USD | 0.00 USD | 168.76 USD | `-17.56%` | `23.07` |
| `Live` | `Long` | `7.33` | 591,840.00 USD | 0.00 USD | 4,910.00 USD | `-17.45%` | `669.93` |
| `Live` | `Long` | `7.33` | 586,940.00 USD | 0.00 USD | 2,450.00 USD | `-17.33%` | `333.54` |
| `Live` | `Long` | `7.34` | 584,490.00 USD | 0.00 USD | 4,370.00 USD | `-17.22%` | `594.84` |
| `Live` | `Long` | `7.36` | 580,120.00 USD | 0.00 USD | 1,030.00 USD | `-17.11%` | `140.00` |
| `Live` | `Long` | `7.37` | 579,090.00 USD | 0.00 USD | 5,720.00 USD | `-17.00%` | `776.95` |
| `Live` | `Long` | `7.38` | 573,370.00 USD | 0.00 USD | 3,920.00 USD | `-16.88%` | `531.65` |
| `Live` | `Long` | `7.38` | 569,450.00 USD | 0.00 USD | 17,770.00 USD | `-16.77%` | `2,406.10` |
| `Live` | `Long` | `7.39` | 551,680.00 USD | 0.00 USD | 1,550.00 USD | `-16.66%` | `210.17` |
| `Live` | `Long` | `7.42` | 550,130.00 USD | 0.00 USD | 1,480.00 USD | `-16.43%` | `200.00` |
| `Live` | `Long` | `7.42` | 548,640.00 USD | 0.00 USD | 500.00 USD | `-16.32%` | `67.34` |
| `Live` | `Long` | `7.45` | 548,140.00 USD | 0.00 USD | 210.99 USD | `-16.09%` | `28.34` |
| `Live` | `Long` | `7.46` | 547,930.00 USD | 0.00 USD | 1,370.00 USD | `-15.98%` | `183.84` |
| `Live` | `Long` | `7.46` | 546,560.00 USD | 0.00 USD | 4,590.00 USD | `-15.87%` | `614.36` |
| `Live` | `Long` | `7.47` | 541,980.00 USD | 0.00 USD | 3,210.00 USD | `-15.76%` | `430.09` |
| `Live` | `Long` | `7.50` | 538,760.00 USD | 0.00 USD | 1,580.00 USD | `-15.53%` | `211.22` |
| `Live` | `Long` | `7.50` | 537,180.00 USD | 0.00 USD | 1,080.00 USD | `-15.42%` | `143.74` |
| `Live` | `Long` | `7.53` | 536,100.00 USD | 0.00 USD | 995.86 USD | `-15.19%` | `132.34` |
| `Live` | `Long` | `7.54` | 535,100.00 USD | 0.00 USD | 4,210.00 USD | `-15.08%` | `559.01` |
| `Live` | `Long` | `7.55` | 530,890.00 USD | 0.00 USD | 157.14 USD | `-14.85%` | `20.80` |
| `Live` | `Long` | `7.57` | 530,730.00 USD | 0.00 USD | 4,380.00 USD | `-14.74%` | `578.50` |
| `Live` | `Long` | `7.59` | 526,360.00 USD | 0.00 USD | 25,140.00 USD | `-14.40%` | `3,310.14` |
| `Live` | `Long` | `7.62` | 501,220.00 USD | 0.00 USD | 312.22 USD | `-14.18%` | `41.00` |
| `Live` | `Long` | `7.62` | 500,900.00 USD | 0.00 USD | 787.51 USD | `-14.07%` | `103.28` |
| `Live` | `Long` | `7.63` | 500,120.00 USD | 0.00 USD | 514.52 USD | `-13.95%` | `67.39` |
| `Live` | `Long` | `7.66` | 499,600.00 USD | 0.00 USD | 135.42 USD | `-13.73%` | `17.69` |
| `Live` | `Long` | `7.67` | 499,470.00 USD | 0.00 USD | 1,740.00 USD | `-13.61%` | `226.45` |
| `Live` | `Long` | `7.68` | 497,730.00 USD | 0.00 USD | 1,120.00 USD | `-13.39%` | `145.25` |
| `Live` | `Long` | `7.70` | 496,610.00 USD | 0.00 USD | 1,460.00 USD | `-13.28%` | `190.36` |
| `Live` | `Long` | `7.71` | 495,150.00 USD | 0.00 USD | 19,410.00 USD | `-13.16%` | `2,518.82` |
| `Live` | `Long` | `7.72` | 475,740.00 USD | 0.00 USD | 2,550.00 USD | `-12.94%` | `330.65` |
| `Live` | `Long` | `7.75` | 473,190.00 USD | 0.00 USD | 893.76 USD | `-12.60%` | `115.25` |
| `Live` | `Long` | `7.76` | 472,290.00 USD | 0.00 USD | 455.73 USD | `-12.49%` | `58.69` |
| `Live` | `Long` | `7.78` | 471,840.00 USD | 0.00 USD | 695.32 USD | `-12.37%` | `89.43` |
| `Live` | `Long` | `7.79` | 471,140.00 USD | 0.00 USD | 3,900.00 USD | `-12.26%` | `500.57` |
| `Live` | `Long` | `7.79` | 467,250.00 USD | 0.00 USD | 1,940.00 USD | `-12.15%` | `248.84` |
| `Live` | `Long` | `7.80` | 465,310.00 USD | 0.00 USD | 633.77 USD | `-12.04%` | `81.20` |
| `Live` | `Long` | `7.82` | 464,670.00 USD | 0.00 USD | 5,280.00 USD | `-11.92%` | `675.43` |
| `Live` | `Long` | `7.84` | 459,390.00 USD | 0.00 USD | 10,930.00 USD | `-11.59%` | `1,393.53` |
| `Live` | `Long` | `7.86` | 448,460.00 USD | 0.00 USD | 2,110.00 USD | `-11.47%` | `269.14` |
| `Live` | `Long` | `7.87` | 446,350.00 USD | 0.00 USD | 176.18 USD | `-11.36%` | `22.40` |
| `Live` | `Long` | `7.88` | 446,170.00 USD | 0.00 USD | 555.19 USD | `-11.25%` | `70.50` |
| `Live` | `Long` | `7.91` | 445,620.00 USD | 0.00 USD | 2,410.00 USD | `-10.91%` | `304.85` |
| `Live` | `Long` | `7.92` | 443,210.00 USD | 0.00 USD | 923.42 USD | `-10.68%` | `116.52` |
| `Live` | `Long` | `7.93` | 442,280.00 USD | 0.00 USD | 1,820.00 USD | `-10.57%` | `228.88` |
| `Live` | `Long` | `7.95` | 440,470.00 USD | 0.00 USD | 127,110.00 USD | `-10.46%` | `15,999.24` |
| `Live` | `Long` | `7.96` | 313,350.00 USD | 0.00 USD | 843.15 USD | `-10.35%` | `105.99` |
| `Live` | `Long` | `7.99` | 312,510.00 USD | 0.00 USD | 1,600.00 USD | `-10.01%` | `200.68` |
| `Live` | `Long` | `8.00` | 310,910.00 USD | 0.00 USD | 210.99 USD | `-9.90%` | `26.39` |
| `Live` | `Long` | `8.03` | 310,700.00 USD | 0.00 USD | 957.70 USD | `-9.56%` | `119.34` |
| `Live` | `Long` | `8.04` | 309,740.00 USD | 0.00 USD | 88,380.00 USD | `-9.44%` | `10,999.50` |
| `Live` | `Long` | `8.04` | 221,360.00 USD | 0.00 USD | 6,890.00 USD | `-9.33%` | `856.44` |
| `Live` | `Long` | `8.05` | 214,470.00 USD | 0.00 USD | 3,340.00 USD | `-9.22%` | `414.27` |
| `Live` | `Long` | `8.06` | 211,130.00 USD | 0.00 USD | 37,830.00 USD | `-9.11%` | `4,690.67` |
| `Live` | `Long` | `8.09` | 173,300.00 USD | 0.00 USD | 617.61 USD | `-8.88%` | `76.39` |
| `Live` | `Long` | `8.10` | 172,680.00 USD | 0.00 USD | 11,700.00 USD | `-8.77%` | `1,445.70` |
| `Live` | `Long` | `8.12` | 160,980.00 USD | 0.00 USD | 241.26 USD | `-8.54%` | `29.73` |
| `Live` | `Long` | `8.12` | 160,740.00 USD | 0.00 USD | 233.92 USD | `-8.43%` | `28.79` |
| `Live` | `Long` | `8.16` | 160,500.00 USD | 0.00 USD | 871.61 USD | `-7.98%` | `106.75` |
| `Live` | `Long` | `8.19` | 159,630.00 USD | 0.00 USD | 4,030.00 USD | `-7.75%` | `492.37` |
| `Live` | `Long` | `8.20` | 155,600.00 USD | 0.00 USD | 2,380.00 USD | `-7.64%` | `290.16` |
| `Live` | `Long` | `8.21` | 153,230.00 USD | 0.00 USD | 577.06 USD | `-7.53%` | `70.33` |
| `Live` | `Long` | `8.21` | 152,650.00 USD | 0.00 USD | 147.87 USD | `-7.42%` | `18.00` |
| `Live` | `Long` | `8.22` | 152,500.00 USD | 0.00 USD | 2,100.00 USD | `-7.30%` | `255.16` |
| `Live` | `Long` | `8.23` | 150,400.00 USD | 0.00 USD | 1,160.00 USD | `-7.19%` | `140.81` |
| `Live` | `Long` | `8.24` | 149,240.00 USD | 0.00 USD | 1,300.00 USD | `-7.08%` | `158.06` |
| `Live` | `Long` | `8.26` | 147,940.00 USD | 0.00 USD | 13,810.00 USD | `-6.96%` | `1,673.14` |
| `Live` | `Long` | `8.27` | 134,130.00 USD | 0.00 USD | 6,110.00 USD | `-6.85%` | `739.00` |
| `Live` | `Long` | `8.28` | 128,020.00 USD | 0.00 USD | 3,190.00 USD | `-6.74%` | `386.07` |
| `Live` | `Long` | `8.29` | 124,820.00 USD | 0.00 USD | 498.26 USD | `-6.63%` | `60.14` |
| `Live` | `Long` | `8.29` | 124,330.00 USD | 0.00 USD | 18,970.00 USD | `-6.51%` | `2,286.62` |
| `Live` | `Long` | `8.30` | 105,360.00 USD | 0.00 USD | 33,500.00 USD | `-6.40%` | `4,033.57` |
| `Live` | `Long` | `8.31` | 71,860.00 USD | 0.00 USD | 4,550.00 USD | `-6.29%` | `547.70` |
| `Live` | `Long` | `8.34` | 67,310.00 USD | 0.00 USD | 4,630.00 USD | `-6.06%` | `555.62` |
| `Live` | `Long` | `8.36` | 62,670.00 USD | 0.00 USD | 3,180.00 USD | `-5.84%` | `380.92` |
| `Live` | `Long` | `8.37` | 59,490.00 USD | 0.00 USD | 7,160.00 USD | `-5.73%` | `856.48` |
| `Live` | `Long` | `8.38` | 52,330.00 USD | 0.00 USD | 223.70 USD | `-5.61%` | `26.71` |
| `Live` | `Long` | `8.39` | 52,100.00 USD | 0.00 USD | 1,680.00 USD | `-5.39%` | `200.00` |
| `Live` | `Long` | `8.40` | 50,430.00 USD | 0.00 USD | 1,280.00 USD | `-5.27%` | `152.34` |
| `Live` | `Long` | `8.44` | 49,140.00 USD | 0.00 USD | 188.61 USD | `-4.94%` | `22.36` |
| `Live` | `Long` | `8.45` | 48,960.00 USD | 0.00 USD | 588.70 USD | `-4.82%` | `69.71` |
| `Live` | `Long` | `8.46` | 48,370.00 USD | 0.00 USD | 4,100.00 USD | `-4.71%` | `485.34` |
| `Live` | `Long` | `8.46` | 44,260.00 USD | 0.00 USD | 2,840.00 USD | `-4.60%` | `335.62` |
| `Live` | `Long` | `8.47` | 41,420.00 USD | 0.00 USD | 12,890.00 USD | `-4.49%` | `1,520.51` |
| `Live` | `Long` | `8.48` | 28,540.00 USD | 0.00 USD | 1,160.00 USD | `-4.37%` | `136.39` |
| `Live` | `Long` | `8.49` | 27,380.00 USD | 0.00 USD | 403.51 USD | `-4.26%` | `47.50` |
| `Live` | `Long` | `8.51` | 26,980.00 USD | 0.00 USD | 6,380.00 USD | `-4.15%` | `750.34` |
| `Live` | `Long` | `8.52` | 20,590.00 USD | 0.00 USD | 8,060.00 USD | `-4.03%` | `947.05` |
| `Live` | `Long` | `8.54` | 12,530.00 USD | 0.00 USD | 6,350.00 USD | `-3.81%` | `743.78` |
| `Live` | `Long` | `8.54` | 6,180.00 USD | 0.00 USD | 1,550.00 USD | `-3.70%` | `180.95` |
| `Live` | `Long` | `8.55` | 4,640.00 USD | 0.00 USD | 1,660.00 USD | `-3.58%` | `193.54` |
| `Live` | `Long` | `8.61` | 2,980.00 USD | 0.00 USD | 2,980.00 USD | `-3.02%` | `346.30` |
| `Live` | `Short` | `9.13` | 314.34 USD | 314.34 USD | 0.00 USD | `+2.95%` | `34.41` |
| `Live` | `Short` | `9.29` | 415.26 USD | 100.93 USD | 0.00 USD | `+4.64%` | `10.87` |
| `Live` | `Short` | `9.34` | 1,470.00 USD | 1,060.00 USD | 0.00 USD | `+5.21%` | `113.04` |
| `Live` | `Short` | `9.35` | 5,400.00 USD | 3,930.00 USD | 0.00 USD | `+5.32%` | `420.07` |
| `Live` | `Short` | `9.38` | 409,510.00 USD | 404,120.00 USD | 0.00 USD | `+5.77%` | `43,059.94` |
| `Live` | `Short` | `9.41` | 411,990.00 USD | 2,470.00 USD | 0.00 USD | `+6.11%` | `262.71` |
| `Live` | `Short` | `9.46` | 414,990.00 USD | 3,010.00 USD | 0.00 USD | `+6.56%` | `318.12` |
| `Live` | `Short` | `9.73` | 415,190.00 USD | 192.95 USD | 0.00 USD | `+9.71%` | `19.82` |
| `Live` | `Short` | `9.77` | 415,740.00 USD | 549.67 USD | 0.00 USD | `+10.05%` | `56.29` |
| `Live` | `Short` | `9.79` | 416,210.00 USD | 470.66 USD | 0.00 USD | `+10.28%` | `48.10` |
| `Live` | `Short` | `9.85` | 417,620.00 USD | 1,410.00 USD | 0.00 USD | `+10.95%` | `143.31` |
| `Live` | `Short` | `10.21` | 424,950.00 USD | 7,330.00 USD | 0.00 USD | `+15.12%` | `717.30` |
| `Live` | `Short` | `10.23` | 425,060.00 USD | 114.12 USD | 0.00 USD | `+15.35%` | `11.15` |
| `Live` | `Short` | `10.35` | 428,440.00 USD | 3,380.00 USD | 0.00 USD | `+16.59%` | `326.92` |
| `Live` | `Short` | `10.46` | 464,650.00 USD | 36,200.00 USD | 0.00 USD | `+17.83%` | `3,462.73` |
| `Live` | `Short` | `10.56` | 465,170.00 USD | 523.81 USD | 0.00 USD | `+19.07%` | `49.58` |
| `Live` | `Short` | `10.71` | 465,390.00 USD | 218.91 USD | 0.00 USD | `+20.76%` | `20.43` |
| `Live` | `Short` | `10.96` | 467,300.00 USD | 1,920.00 USD | 0.00 USD | `+23.58%` | `174.67` |
| `Live` | `Short` | `11.01` | 474,270.00 USD | 6,970.00 USD | 0.00 USD | `+24.03%` | `633.00` |
| `Live` | `Short` | `11.27` | 486,080.00 USD | 11,810.00 USD | 0.00 USD | `+26.96%` | `1,048.25` |
| `Live` | `Short` | `11.51` | 493,530.00 USD | 7,460.00 USD | 0.00 USD | `+29.66%` | `648.15` |
| `Live` | `Short` | `11.62` | 505,670.00 USD | 12,140.00 USD | 0.00 USD | `+31.02%` | `1,043.90` |
| `Live` | `Short` | `11.66` | 506,450.00 USD | 776.89 USD | 0.00 USD | `+31.47%` | `66.60` |
| `Live` | `Short` | `11.69` | 507,180.00 USD | 733.47 USD | 0.00 USD | `+31.69%` | `62.77` |
| `Live` | `Short` | `11.86` | 566,460.00 USD | 59,270.00 USD | 0.00 USD | `+33.61%` | `5,000.00` |
| `Live` | `Short` | `11.98` | 567,820.00 USD | 1,360.00 USD | 0.00 USD | `+35.07%` | `113.77` |
| `Live` | `Short` | `12.30` | 569,550.00 USD | 1,730.00 USD | 0.00 USD | `+38.68%` | `140.71` |
| `Live` | `Short` | `12.40` | 569,890.00 USD | 343.62 USD | 0.00 USD | `+39.81%` | `27.70` |
| `Live` | `Short` | `12.43` | 605,670.00 USD | 35,780.00 USD | 0.00 USD | `+40.03%` | `2,879.71` |
| `Live` | `Short` | `12.60` | 619,780.00 USD | 14,110.00 USD | 0.00 USD | `+41.95%` | `1,120.14` |
| `Live` | `Short` | `12.64` | 620,210.00 USD | 431.19 USD | 0.00 USD | `+42.51%` | `34.10` |
| `Live` | `Short` | `12.79` | 621,170.00 USD | 953.38 USD | 0.00 USD | `+44.09%` | `74.57` |
| `Live` | `Short` | `12.96` | 621,270.00 USD | 102.68 USD | 0.00 USD | `+46.12%` | `7.92` |
| `Live` | `Short` | `13.20` | 709,210.00 USD | 87,940.00 USD | 0.00 USD | `+48.71%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 944,050.00 USD | 234,840.00 USD | 0.00 USD | `+49.72%` | `17,677.02` |
| `Live` | `Short` | `13.29` | 947,860.00 USD | 3,810.00 USD | 0.00 USD | `+49.84%` | `286.56` |
| `Live` | `Short` | `13.43` | 948,020.00 USD | 156.40 USD | 0.00 USD | `+51.30%` | `11.65` |
| `Live` | `Short` | `13.46` | 948,450.00 USD | 430.34 USD | 0.00 USD | `+51.75%` | `31.96` |
| `Live` | `Short` | `13.69` | 948,620.00 USD | 172.29 USD | 0.00 USD | `+54.23%` | `12.59` |
| `Live` | `Short` | `14.18` | 952,560.00 USD | 3,930.00 USD | 0.00 USD | `+59.75%` | `277.54` |
| `Live` | `Short` | `14.66` | 953,380.00 USD | 823.29 USD | 0.00 USD | `+65.28%` | `56.14` |
| `Live` | `Short` | `14.80` | 955,840.00 USD | 2,460.00 USD | 0.00 USD | `+66.85%` | `166.16` |
| `Live` | `Short` | `14.87` | 956,080.00 USD | 243.93 USD | 0.00 USD | `+67.53%` | `16.41` |
| `Live` | `Short` | `14.88` | 956,380.00 USD | 293.48 USD | 0.00 USD | `+67.64%` | `19.73` |
| `Live` | `Short` | `14.93` | 956,700.00 USD | 321.63 USD | 0.00 USD | `+68.21%` | `21.55` |
| `Live` | `Short` | `15.29` | 956,930.00 USD | 229.43 USD | 0.00 USD | `+72.38%` | `15.00` |
| `Live` | `Short` | `15.34` | 1,110,000.00 USD | 153,350.00 USD | 0.00 USD | `+72.83%` | `10,000.00` |
| `Live` | `Short` | `15.35` | 1,110,000.00 USD | 230.17 USD | 0.00 USD | `+72.94%` | `15.00` |
| `Live` | `Short` | `15.38` | 1,130,000.00 USD | 20,000.00 USD | 0.00 USD | `+73.39%` | `1,300.00` |
| `Live` | `Short` | `15.64` | 1,130,000.00 USD | 111.24 USD | 0.00 USD | `+76.32%` | `7.11` |
| `Live` | `Short` | `16.27` | 1,390,000.00 USD | 263,790.00 USD | 0.00 USD | `+83.42%` | `16,208.00` |
| `Live` | `Short` | `16.41` | 1,420,000.00 USD | 22,540.00 USD | 0.00 USD | `+84.89%` | `1,373.91` |
| `Live` | `Short` | `16.52` | 1,420,000.00 USD | 190.91 USD | 0.00 USD | `+86.13%` | `11.56` |
| `Live` | `Short` | `16.55` | 1,500,000.00 USD | 83,400.00 USD | 0.00 USD | `+86.58%` | `5,037.66` |
| `Live` | `Short` | `16.75` | 1,500,000.00 USD | 162.26 USD | 0.00 USD | `+88.72%` | `9.69` |
| `Live` | `Short` | `17.02` | 1,500,000.00 USD | 191.87 USD | 0.00 USD | `+91.87%` | `11.27` |
| `Live` | `Short` | `17.14` | 1,500,000.00 USD | 1,710.00 USD | 0.00 USD | `+93.11%` | `100.00` |
| `Live` | `Short` | `17.46` | 1,500,000.00 USD | 101.47 USD | 0.00 USD | `+96.83%` | `5.81` |
| `Live` | `Short` | `17.62` | 1,510,000.00 USD | 4,120.00 USD | 0.00 USD | `+98.64%` | `233.67` |
| `Live` | `Short` | `17.64` | 1,510,000.00 USD | 4,930.00 USD | 0.00 USD | `+98.86%` | `279.46` |
| `Live` | `Short` | `17.66` | 1,510,000.00 USD | 2,660.00 USD | 0.00 USD | `+99.09%` | `150.82` |
| `Live` | `Short` | `17.70` | 1,510,000.00 USD | 108.89 USD | 0.00 USD | `+99.54%` | `6.15` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 338,360.00 USD | 0.00 USD | 611.73 USD | `-73.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 337,750.00 USD | 0.00 USD | 793.75 USD | `-54.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.49` | 336,960.00 USD | 0.00 USD | 105.04 USD | `-49.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 336,850.00 USD | 0.00 USD | 67,970.00 USD | `-43.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 268,890.00 USD | 0.00 USD | 205.30 USD | `-40.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 268,680.00 USD | 0.00 USD | 465.42 USD | `-38.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 268,220.00 USD | 0.00 USD | 349.35 USD | `-37.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 267,870.00 USD | 0.00 USD | 1,330.00 USD | `-34.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 266,540.00 USD | 0.00 USD | 493.50 USD | `-33.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 266,040.00 USD | 0.00 USD | 100.98 USD | `-32.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 265,940.00 USD | 0.00 USD | 620.80 USD | `-32.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 265,320.00 USD | 0.00 USD | 4,160.00 USD | `-31.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 261,170.00 USD | 0.00 USD | 6,500.00 USD | `-30.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 254,670.00 USD | 0.00 USD | 864.38 USD | `-29.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 253,800.00 USD | 0.00 USD | 1,430.00 USD | `-26.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 252,370.00 USD | 0.00 USD | 4,340.00 USD | `-26.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 248,030.00 USD | 0.00 USD | 5,520.00 USD | `-24.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 242,510.00 USD | 0.00 USD | 100.72 USD | `-24.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 242,410.00 USD | 0.00 USD | 296.34 USD | `-23.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 242,110.00 USD | 0.00 USD | 921.19 USD | `-23.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 241,190.00 USD | 0.00 USD | 709.98 USD | `-22.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 240,480.00 USD | 0.00 USD | 262.44 USD | `-21.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 240,220.00 USD | 0.00 USD | 3,610.00 USD | `-21.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 236,600.00 USD | 0.00 USD | 6,790.00 USD | `-19.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 229,810.00 USD | 0.00 USD | 9,770.00 USD | `-19.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 220,050.00 USD | 0.00 USD | 103.46 USD | `-18.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 219,940.00 USD | 0.00 USD | 603.44 USD | `-18.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 219,340.00 USD | 0.00 USD | 891.57 USD | `-18.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 218,450.00 USD | 0.00 USD | 2,300.00 USD | `-17.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 216,140.00 USD | 0.00 USD | 129.58 USD | `-17.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 216,010.00 USD | 0.00 USD | 236.19 USD | `-17.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 215,780.00 USD | 0.00 USD | 199.39 USD | `-15.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 215,580.00 USD | 0.00 USD | 4,730.00 USD | `-15.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 210,850.00 USD | 0.00 USD | 37,420.00 USD | `-15.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 173,420.00 USD | 0.00 USD | 778.49 USD | `-15.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 172,640.00 USD | 0.00 USD | 799.83 USD | `-15.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.57` | 171,840.00 USD | 0.00 USD | 103.41 USD | `-14.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 171,740.00 USD | 0.00 USD | 1,370.00 USD | `-14.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 170,370.00 USD | 0.00 USD | 360.13 USD | `-13.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 170,010.00 USD | 0.00 USD | 175.42 USD | `-12.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 169,830.00 USD | 0.00 USD | 2,990.00 USD | `-12.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 166,840.00 USD | 0.00 USD | 143.51 USD | `-11.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 166,690.00 USD | 0.00 USD | 183.33 USD | `-11.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.88` | 166,510.00 USD | 0.00 USD | 194.52 USD | `-11.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 166,310.00 USD | 0.00 USD | 394.75 USD | `-11.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 165,920.00 USD | 0.00 USD | 1,350.00 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 164,570.00 USD | 0.00 USD | 1,590.00 USD | `-10.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 162,990.00 USD | 0.00 USD | 898.42 USD | `-10.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.97` | 162,090.00 USD | 0.00 USD | 107.74 USD | `-10.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 161,980.00 USD | 0.00 USD | 1,350.00 USD | `-9.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 160,630.00 USD | 0.00 USD | 7,400.00 USD | `-9.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 153,240.00 USD | 0.00 USD | 123.58 USD | `-9.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 153,110.00 USD | 0.00 USD | 2,110.00 USD | `-9.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 151,000.00 USD | 0.00 USD | 563.85 USD | `-9.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 150,440.00 USD | 0.00 USD | 105.14 USD | `-8.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 150,330.00 USD | 0.00 USD | 367.76 USD | `-8.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 149,970.00 USD | 0.00 USD | 2,330.00 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 147,630.00 USD | 0.00 USD | 120.10 USD | `-8.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 147,510.00 USD | 0.00 USD | 6,500.00 USD | `-8.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 141,010.00 USD | 0.00 USD | 462.15 USD | `-8.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 140,550.00 USD | 0.00 USD | 654.53 USD | `-8.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 139,890.00 USD | 0.00 USD | 367.91 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 139,530.00 USD | 0.00 USD | 520.75 USD | `-7.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 139,010.00 USD | 0.00 USD | 167.22 USD | `-7.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 138,840.00 USD | 0.00 USD | 141.04 USD | `-7.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 138,700.00 USD | 0.00 USD | 1,780.00 USD | `-7.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 136,910.00 USD | 0.00 USD | 515.66 USD | `-7.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.22` | 136,400.00 USD | 0.00 USD | 165.40 USD | `-7.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 136,230.00 USD | 0.00 USD | 143.54 USD | `-7.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 136,090.00 USD | 0.00 USD | 168.64 USD | `-6.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 135,920.00 USD | 0.00 USD | 201.49 USD | `-6.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 135,720.00 USD | 0.00 USD | 6,530.00 USD | `-6.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 129,190.00 USD | 0.00 USD | 1,140.00 USD | `-6.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 128,050.00 USD | 0.00 USD | 2,000.00 USD | `-6.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 126,040.00 USD | 0.00 USD | 756.06 USD | `-5.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 125,290.00 USD | 0.00 USD | 970.35 USD | `-5.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 124,320.00 USD | 0.00 USD | 5,470.00 USD | `-5.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 118,850.00 USD | 0.00 USD | 100.74 USD | `-5.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 118,750.00 USD | 0.00 USD | 3,290.00 USD | `-5.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 115,470.00 USD | 0.00 USD | 358.56 USD | `-5.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 115,110.00 USD | 0.00 USD | 1,880.00 USD | `-5.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 113,220.00 USD | 0.00 USD | 140.36 USD | `-4.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 113,080.00 USD | 0.00 USD | 138.24 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 112,950.00 USD | 0.00 USD | 954.23 USD | `-4.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.47` | 111,990.00 USD | 0.00 USD | 7,030.00 USD | `-4.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.48` | 104,960.00 USD | 0.00 USD | 489.58 USD | `-4.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.51` | 104,470.00 USD | 0.00 USD | 5,630.00 USD | `-4.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.52` | 98,840.00 USD | 0.00 USD | 5,060.00 USD | `-4.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.53` | 93,770.00 USD | 0.00 USD | 1,130.00 USD | `-3.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.54` | 92,650.00 USD | 0.00 USD | 132.45 USD | `-3.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 92,510.00 USD | 0.00 USD | 7,740.00 USD | `-3.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.57` | 84,780.00 USD | 0.00 USD | 428.58 USD | `-3.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.59` | 84,350.00 USD | 0.00 USD | 2,500.00 USD | `-3.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.60` | 81,850.00 USD | 0.00 USD | 435.59 USD | `-3.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.61` | 81,410.00 USD | 0.00 USD | 1,080.00 USD | `-3.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.62` | 80,330.00 USD | 0.00 USD | 1,980.00 USD | `-2.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.62` | 78,350.00 USD | 0.00 USD | 2,740.00 USD | `-2.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.63` | 75,610.00 USD | 0.00 USD | 103.19 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.64` | 75,510.00 USD | 0.00 USD | 103.31 USD | `-2.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 75,400.00 USD | 0.00 USD | 3,810.00 USD | `-2.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.66` | 71,600.00 USD | 0.00 USD | 196.87 USD | `-2.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.68` | 71,400.00 USD | 0.00 USD | 223.82 USD | `-2.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.69` | 71,180.00 USD | 0.00 USD | 990.09 USD | `-2.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.70` | 70,190.00 USD | 0.00 USD | 5,010.00 USD | `-2.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.71` | 65,170.00 USD | 0.00 USD | 494.27 USD | `-1.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.71` | 64,680.00 USD | 0.00 USD | 134.30 USD | `-1.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.72` | 64,550.00 USD | 0.00 USD | 315.85 USD | `-1.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.73` | 64,230.00 USD | 0.00 USD | 1,390.00 USD | `-1.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.74` | 62,840.00 USD | 0.00 USD | 933.70 USD | `-1.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.76` | 61,910.00 USD | 0.00 USD | 6,140.00 USD | `-1.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.77` | 55,770.00 USD | 0.00 USD | 39,810.00 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.78` | 15,960.00 USD | 0.00 USD | 114.25 USD | `-1.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.79` | 15,840.00 USD | 0.00 USD | 4,230.00 USD | `-0.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.79` | 11,610.00 USD | 0.00 USD | 299.65 USD | `-0.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.80` | 11,310.00 USD | 0.00 USD | 1,760.00 USD | `-0.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.81` | 9,550.00 USD | 0.00 USD | 705.20 USD | `-0.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.82` | 8,850.00 USD | 0.00 USD | 2,030.00 USD | `-0.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.84` | 6,820.00 USD | 0.00 USD | 243.40 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 6,570.00 USD | 0.00 USD | 5,760.00 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.86` | 807.74 USD | 0.00 USD | 192.86 USD | `-0.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.87` | 614.88 USD | 0.00 USD | 614.88 USD | `-0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 543.33 USD | 543.33 USD | 0.00 USD | `+0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 1,650.00 USD | 1,100.00 USD | 0.00 USD | `+0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 1,840.00 USD | 188.66 USD | 0.00 USD | `+0.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 2,620.00 USD | 788.72 USD | 0.00 USD | `+0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 5,980.00 USD | 3,360.00 USD | 0.00 USD | `+0.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 6,090.00 USD | 110.58 USD | 0.00 USD | `+0.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 7,110.00 USD | 1,020.00 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 7,340.00 USD | 223.62 USD | 0.00 USD | `+0.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 7,470.00 USD | 137.73 USD | 0.00 USD | `+0.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 10,650.00 USD | 3,170.00 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 325,800.00 USD | 315,150.00 USD | 0.00 USD | `+1.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 325,900.00 USD | 104.59 USD | 0.00 USD | `+1.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 326,680.00 USD | 776.54 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 327,210.00 USD | 531.20 USD | 0.00 USD | `+1.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 328,590.00 USD | 1,380.00 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 329,680.00 USD | 1,090.00 USD | 0.00 USD | `+1.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 330,290.00 USD | 616.37 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 330,480.00 USD | 188.59 USD | 0.00 USD | `+1.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 330,930.00 USD | 453.84 USD | 0.00 USD | `+2.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 331,100.00 USD | 160.99 USD | 0.00 USD | `+2.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 331,510.00 USD | 415.00 USD | 0.00 USD | `+2.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 333,020.00 USD | 1,510.00 USD | 0.00 USD | `+2.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 335,060.00 USD | 2,040.00 USD | 0.00 USD | `+2.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 562,690.00 USD | 227,630.00 USD | 0.00 USD | `+2.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 565,730.00 USD | 3,030.00 USD | 0.00 USD | `+2.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.13` | 569,220.00 USD | 3,500.00 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 571,220.00 USD | 2,000.00 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 965,440.00 USD | 394,210.00 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,000,000.00 USD | 39,130.00 USD | 0.00 USD | `+3.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.20` | 1,010,000.00 USD | 1,590.00 USD | 0.00 USD | `+3.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,010,000.00 USD | 8,580.00 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,010,000.00 USD | 131.87 USD | 0.00 USD | `+3.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,020,000.00 USD | 687.91 USD | 0.00 USD | `+3.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,020,000.00 USD | 954.71 USD | 0.00 USD | `+4.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,420,000.00 USD | 398,520.00 USD | 0.00 USD | `+4.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.27` | 1,420,000.00 USD | 205.87 USD | 0.00 USD | `+4.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,420,000.00 USD | 1,960.00 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,420,000.00 USD | 434.45 USD | 0.00 USD | `+4.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,440,000.00 USD | 18,610.00 USD | 0.00 USD | `+4.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,440,000.00 USD | 354.81 USD | 0.00 USD | `+4.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,440,000.00 USD | 2,180.00 USD | 0.00 USD | `+5.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,440,000.00 USD | 579.86 USD | 0.00 USD | `+5.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,770,000.00 USD | 327,430.00 USD | 0.00 USD | `+5.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,770,000.00 USD | 233.38 USD | 0.00 USD | `+5.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,770,000.00 USD | 163.41 USD | 0.00 USD | `+5.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,770,000.00 USD | 1,150.00 USD | 0.00 USD | `+5.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,770,000.00 USD | 660.84 USD | 0.00 USD | `+5.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,770,000.00 USD | 2,480.00 USD | 0.00 USD | `+6.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,770,000.00 USD | 1,110.00 USD | 0.00 USD | `+6.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,770,000.00 USD | 109.92 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.45` | 1,770,000.00 USD | 140.35 USD | 0.00 USD | `+6.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,770,000.00 USD | 1,890.00 USD | 0.00 USD | `+6.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.47` | 1,780,000.00 USD | 1,780.00 USD | 0.00 USD | `+6.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,780,000.00 USD | 2,210.00 USD | 0.00 USD | `+6.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,780,000.00 USD | 288.46 USD | 0.00 USD | `+7.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.51` | 1,780,000.00 USD | 1,600.00 USD | 0.00 USD | `+7.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,780,000.00 USD | 103.54 USD | 0.00 USD | `+7.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.54` | 1,780,000.00 USD | 1,320.00 USD | 0.00 USD | `+7.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.56` | 1,780,000.00 USD | 535.35 USD | 0.00 USD | `+7.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,780,000.00 USD | 231.00 USD | 0.00 USD | `+8.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,780,000.00 USD | 221.07 USD | 0.00 USD | `+8.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,780,000.00 USD | 1,470.00 USD | 0.00 USD | `+8.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,780,000.00 USD | 148.48 USD | 0.00 USD | `+8.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,780,000.00 USD | 329.43 USD | 0.00 USD | `+8.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,790,000.00 USD | 446.58 USD | 0.00 USD | `+9.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,790,000.00 USD | 108.21 USD | 0.00 USD | `+9.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,790,000.00 USD | 169.68 USD | 0.00 USD | `+9.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,790,000.00 USD | 121.87 USD | 0.00 USD | `+10.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.80` | 1,790,000.00 USD | 619.28 USD | 0.00 USD | `+10.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,790,000.00 USD | 5,030.00 USD | 0.00 USD | `+10.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,790,000.00 USD | 340.05 USD | 0.00 USD | `+11.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,790,000.00 USD | 742.12 USD | 0.00 USD | `+11.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,790,000.00 USD | 899.47 USD | 0.00 USD | `+11.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,860,000.00 USD | 70,020.00 USD | 0.00 USD | `+11.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,860,000.00 USD | 373.97 USD | 0.00 USD | `+11.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,870,000.00 USD | 5,280.00 USD | 0.00 USD | `+12.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,880,000.00 USD | 6,370.00 USD | 0.00 USD | `+13.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,880,000.00 USD | 202.10 USD | 0.00 USD | `+13.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 2,090,000.00 USD | 210,980.00 USD | 0.00 USD | `+14.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 2,090,000.00 USD | 1,150.00 USD | 0.00 USD | `+14.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 2,090,000.00 USD | 172.16 USD | 0.00 USD | `+15.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 2,090,000.00 USD | 868.36 USD | 0.00 USD | `+15.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 2,090,000.00 USD | 489.40 USD | 0.00 USD | `+16.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 2,090,000.00 USD | 1,200.00 USD | 0.00 USD | `+16.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 2,090,000.00 USD | 118.01 USD | 0.00 USD | `+17.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 2,090,000.00 USD | 312.31 USD | 0.00 USD | `+18.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 2,090,000.00 USD | 1,530.00 USD | 0.00 USD | `+18.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 2,090,000.00 USD | 178.46 USD | 0.00 USD | `+19.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.62` | 2,090,000.00 USD | 153.11 USD | 0.00 USD | `+19.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 2,090,000.00 USD | 173.42 USD | 0.00 USD | `+20.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 2,090,000.00 USD | 184.75 USD | 0.00 USD | `+20.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 2,090,000.00 USD | 135.78 USD | 0.00 USD | `+21.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 2,090,000.00 USD | 127.96 USD | 0.00 USD | `+22.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 2,090,000.00 USD | 476.43 USD | 0.00 USD | `+22.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 2,100,000.00 USD | 1,730.00 USD | 0.00 USD | `+22.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 2,100,000.00 USD | 118.97 USD | 0.00 USD | `+23.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 2,100,000.00 USD | 251.06 USD | 0.00 USD | `+23.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 2,100,000.00 USD | 552.44 USD | 0.00 USD | `+23.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 2,100,000.00 USD | 1,750.00 USD | 0.00 USD | `+24.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 2,100,000.00 USD | 320.29 USD | 0.00 USD | `+25.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 2,100,000.00 USD | 1,100.00 USD | 0.00 USD | `+25.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 2,100,000.00 USD | 2,610.00 USD | 0.00 USD | `+26.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 2,100,000.00 USD | 1,270.00 USD | 0.00 USD | `+26.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 2,110,000.00 USD | 1,380.00 USD | 0.00 USD | `+27.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 2,110,000.00 USD | 2,410.00 USD | 0.00 USD | `+28.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 2,120,000.00 USD | 9,520.00 USD | 0.00 USD | `+29.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 2,120,000.00 USD | 3,530.00 USD | 0.00 USD | `+29.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 2,130,000.00 USD | 7,700.00 USD | 0.00 USD | `+30.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 2,130,000.00 USD | 1,130.00 USD | 0.00 USD | `+33.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 2,130,000.00 USD | 434.61 USD | 0.00 USD | `+33.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 2,130,000.00 USD | 163.52 USD | 0.00 USD | `+33.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 2,250,000.00 USD | 124,300.00 USD | 0.00 USD | `+35.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.51` | 2,260,000.00 USD | 2,770.00 USD | 0.00 USD | `+40.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 2,260,000.00 USD | 3,350.00 USD | 0.00 USD | `+43.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 2,260,000.00 USD | 197.97 USD | 0.00 USD | `+44.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 2,260,000.00 USD | 3,200.00 USD | 0.00 USD | `+45.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 2,260,000.00 USD | 179.58 USD | 0.00 USD | `+46.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 2,260,000.00 USD | 720.74 USD | 0.00 USD | `+46.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.07` | 2,270,000.00 USD | 504.17 USD | 0.00 USD | `+47.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 2,270,000.00 USD | 169.57 USD | 0.00 USD | `+48.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.30` | 2,270,000.00 USD | 159.66 USD | 0.00 USD | `+49.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 2,270,000.00 USD | 446.52 USD | 0.00 USD | `+50.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.46` | 2,270,000.00 USD | 1,710.00 USD | 0.00 USD | `+51.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 2,270,000.00 USD | 5,320.00 USD | 0.00 USD | `+51.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,480,000.00 USD | 207,980.00 USD | 0.00 USD | `+52.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,480,000.00 USD | 407.95 USD | 0.00 USD | `+54.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,480,000.00 USD | 174.91 USD | 0.00 USD | `+55.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,490,000.00 USD | 9,230.00 USD | 0.00 USD | `+57.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,490,000.00 USD | 960.26 USD | 0.00 USD | `+60.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,490,000.00 USD | 2,710.00 USD | 0.00 USD | `+61.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,500,000.00 USD | 805.90 USD | 0.00 USD | `+63.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,500,000.00 USD | 655.55 USD | 0.00 USD | `+65.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,500,000.00 USD | 4,890.00 USD | 0.00 USD | `+66.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,500,000.00 USD | 471.09 USD | 0.00 USD | `+67.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,500,000.00 USD | 383.85 USD | 0.00 USD | `+68.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 3,150,000.00 USD | 652,070.00 USD | 0.00 USD | `+69.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 3,150,000.00 USD | 111.87 USD | 0.00 USD | `+78.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 3,150,000.00 USD | 219.91 USD | 0.00 USD | `+80.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 3,150,000.00 USD | 121.74 USD | 0.00 USD | `+91.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.00` | 3,150,000.00 USD | 297.59 USD | 0.00 USD | `+91.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.18` | 3,160,000.00 USD | 4,500.00 USD | 0.00 USD | `+93.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.20` | 3,280,000.00 USD | 120,270.00 USD | 0.00 USD | `+93.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.34` | 3,280,000.00 USD | 122.39 USD | 0.00 USD | `+95.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.50` | 3,280,000.00 USD | 586.59 USD | 0.00 USD | `+97.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.61` | 3,280,000.00 USD | 580.97 USD | 0.00 USD | `+98.41%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.75` | 9,500,000.00 USD | 0.00 USD | 9,500,000.00 USD | 976.80 USD | 5,760.00 USD | 0.00 USD |
| `7D` | `7.77` | 9,490,000.00 USD | 0.00 USD | 9,490,000.00 USD | 17,170.00 USD | 4,900.00 USD | 4,850.00 USD |
| `7D` | `7.79` | 9,460,000.00 USD | 0.00 USD | 9,460,000.00 USD | 19,090.00 USD | 4,540.00 USD | 15,300.00 USD |
| `7D` | `7.81` | 9,420,000.00 USD | 0.00 USD | 9,420,000.00 USD | 2,240.00 USD | 11,570.00 USD | 0.00 USD |
| `7D` | `7.83` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 28,130.00 USD | 2,130.00 USD | 23,900.00 USD |
| `7D` | `7.85` | 9,360,000.00 USD | 0.00 USD | 9,360,000.00 USD | 15,410.00 USD | 7,840.00 USD | 6,560.00 USD |
| `7D` | `7.87` | 9,330,000.00 USD | 0.00 USD | 9,330,000.00 USD | 39,380.00 USD | 1,540.00 USD | 21,020.00 USD |
| `7D` | `7.89` | 9,270,000.00 USD | 0.00 USD | 9,270,000.00 USD | 25,450.00 USD | 18,320.00 USD | 24,180.00 USD |
| `7D` | `7.91` | 9,200,000.00 USD | 0.00 USD | 9,200,000.00 USD | 29,920.00 USD | 11,120.00 USD | 17,910.00 USD |
| `1D` | `7.93` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 16,090.00 USD | 2,950.00 USD | 6,200.00 USD |
| `7D` | `7.93` | 9,140,000.00 USD | 0.00 USD | 9,140,000.00 USD | 78,470.00 USD | 7,330.00 USD | 14,550.00 USD |
| `1D` | `7.95` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 7,790.00 USD | 8,290.00 USD | 4,160.00 USD |
| `7D` | `7.95` | 9,040,000.00 USD | 0.00 USD | 9,040,000.00 USD | 30,870.00 USD | 9,500.00 USD | 42,480.00 USD |
| `1D` | `7.97` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 8,510.00 USD | 2,460.00 USD | 3,640.00 USD |
| `7D` | `7.97` | 8,960,000.00 USD | 0.00 USD | 8,960,000.00 USD | 24,400.00 USD | 18,700.00 USD | 39,940.00 USD |
| `1D` | `7.99` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 7,350.00 USD | 2,050.00 USD | 4,440.00 USD |
| `7D` | `7.99` | 8,870,000.00 USD | 0.00 USD | 8,870,000.00 USD | 49,120.00 USD | 7,410.00 USD | 45,910.00 USD |
| `1D` | `8.01` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 6,600.00 USD | 1,840.00 USD | 1,800.00 USD |
| `7D` | `8.01` | 8,770,000.00 USD | 0.00 USD | 8,770,000.00 USD | 49,240.00 USD | 17,990.00 USD | 470.04 USD |
| `1D` | `8.03` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 18,240.00 USD | 2,310.00 USD | 4,750.00 USD |
| `7D` | `8.03` | 8,700,000.00 USD | 0.00 USD | 8,700,000.00 USD | 104,360.00 USD | 23,930.00 USD | 48,290.00 USD |
| `1D` | `8.05` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 27,010.00 USD | 4,800.00 USD | 13,380.00 USD |
| `7D` | `8.05` | 8,530,000.00 USD | 0.00 USD | 8,530,000.00 USD | 36,050.00 USD | 29,270.00 USD | 62,790.00 USD |
| `1D` | `8.07` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 18,230.00 USD | 4,100.00 USD | 11,910.00 USD |
| `7D` | `8.07` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 63,920.00 USD | 10,930.00 USD | 75,680.00 USD |
| `1D` | `8.09` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 14,330.00 USD | 2,630.00 USD | 9,600.00 USD |
| `7D` | `8.09` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 36,390.00 USD | 16,210.00 USD | 27,480.00 USD |
| `1D` | `8.11` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 28,350.00 USD | 7,990.00 USD | 9,420.00 USD |
| `7D` | `8.11` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 36,560.00 USD | 10,160.00 USD | 7,520.00 USD |
| `1D` | `8.13` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 17,040.00 USD | 693.45 USD | 8,610.00 USD |
| `7D` | `8.13` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 32,750.00 USD | 11,560.00 USD | 20,710.00 USD |
| `1D` | `8.15` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 31,480.00 USD | 662.47 USD | 4,970.00 USD |
| `7D` | `8.15` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 91,880.00 USD | 5,090.00 USD | 46,670.00 USD |
| `1D` | `8.17` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 3,360.00 USD | 2,120.00 USD | 101.31 USD |
| `7D` | `8.17` | 7,900,000.00 USD | 0.00 USD | 7,900,000.00 USD | 6,560.00 USD | 7,770.00 USD | 9,880.00 USD |
| `1D` | `8.19` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 5,590.00 USD | 1,980.00 USD | 898.09 USD |
| `7D` | `8.19` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 30,780.00 USD | 3,170.00 USD | 2,970.00 USD |
| `1D` | `8.21` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 9,600.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `8.21` | 7,840,000.00 USD | 0.00 USD | 7,840,000.00 USD | 23,630.00 USD | 0.00 USD | 17,700.00 USD |
| `1D` | `8.23` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 26,450.00 USD | 4,080.00 USD | 43,560.00 USD |
| `7D` | `8.23` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 21,610.00 USD | 3,480.00 USD | 115,930.00 USD |
| `1D` | `8.25` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 18,270.00 USD | 1,150.00 USD | 9,590.00 USD |
| `7D` | `8.25` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 55,820.00 USD | 5,750.00 USD | 9,340.00 USD |
| `1D` | `8.27` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 11,740.00 USD | 14,210.00 USD | 22.02 USD |
| `7D` | `8.27` | 7,590,000.00 USD | 0.00 USD | 7,590,000.00 USD | 65,020.00 USD | 14,400.00 USD | 8,870.00 USD |
| `1D` | `8.29` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 109,640.00 USD | 16,540.00 USD | 45,420.00 USD |
| `7D` | `8.29` | 7,500,000.00 USD | 0.00 USD | 7,500,000.00 USD | 116,340.00 USD | 19,520.00 USD | 52,950.00 USD |
| `1D` | `8.31` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 109,200.00 USD | 24,540.00 USD | 20,590.00 USD |
| `7D` | `8.31` | 7,310,000.00 USD | 0.00 USD | 7,310,000.00 USD | 80,550.00 USD | 13,500.00 USD | 10,760.00 USD |
| `1D` | `8.33` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 23,170.00 USD | 26,770.00 USD | 17,260.00 USD |
| `7D` | `8.33` | 7,210,000.00 USD | 0.00 USD | 7,210,000.00 USD | 58,510.00 USD | 36,210.00 USD | 19,880.00 USD |
| `1D` | `8.35` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 21,290.00 USD | 16,080.00 USD | 22,330.00 USD |
| `7D` | `8.35` | 7,090,000.00 USD | 0.00 USD | 7,090,000.00 USD | 95,370.00 USD | 5,340.00 USD | 82,090.00 USD |
| `1D` | `8.37` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 26,200.00 USD | 10,400.00 USD | 30,140.00 USD |
| `7D` | `8.37` | 6,910,000.00 USD | 0.00 USD | 6,910,000.00 USD | 92,990.00 USD | 31,220.00 USD | 24,200.00 USD |
| `1D` | `8.39` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 99,840.00 USD | 14,620.00 USD | 90,350.00 USD |
| `7D` | `8.39` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 197,900.00 USD | 8,930.00 USD | 68,930.00 USD |
| `1D` | `8.41` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 100,840.00 USD | 26,510.00 USD | 88,900.00 USD |
| `7D` | `8.41` | 6,490,000.00 USD | 0.00 USD | 6,490,000.00 USD | 122,320.00 USD | 32,690.00 USD | 244,780.00 USD |
| `1D` | `8.43` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 63,890.00 USD | 47,320.00 USD | 32,900.00 USD |
| `7D` | `8.43` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 179,770.00 USD | 62,350.00 USD | 73,050.00 USD |
| `1D` | `8.45` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 108,980.00 USD | 23,170.00 USD | 51,160.00 USD |
| `7D` | `8.45` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 210,670.00 USD | 59,180.00 USD | 89,430.00 USD |
| `1D` | `8.47` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 236,730.00 USD | 38,320.00 USD | 63,070.00 USD |
| `7D` | `8.47` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 384,150.00 USD | 70,760.00 USD | 190,090.00 USD |
| `1D` | `8.49` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 248,190.00 USD | 70,410.00 USD | 51,540.00 USD |
| `7D` | `8.49` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 268,080.00 USD | 54,550.00 USD | 118,450.00 USD |
| `1D` | `8.51` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 71,960.00 USD | 62,080.00 USD | 48,040.00 USD |
| `7D` | `8.51` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 202,090.00 USD | 129,490.00 USD | 139,280.00 USD |
| `1D` | `8.53` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 68,760.00 USD | 48,570.00 USD | 65,220.00 USD |
| `7D` | `8.53` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 415,280.00 USD | 66,260.00 USD | 317,370.00 USD |
| `1D` | `8.55` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 84,030.00 USD | 25,290.00 USD | 62,840.00 USD |
| `7D` | `8.55` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 279,560.00 USD | 136,440.00 USD | 16,520.00 USD |
| `1D` | `8.57` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 142,880.00 USD | 23,160.00 USD | 141,420.00 USD |
| `7D` | `8.57` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 709,710.00 USD | 94,290.00 USD | 76,290.00 USD |
| `1D` | `8.59` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 158,140.00 USD | 51,270.00 USD | 65,290.00 USD |
| `7D` | `8.59` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 279,060.00 USD | 118,220.00 USD | 87,630.00 USD |
| `1D` | `8.61` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 103,430.00 USD | 36,000.00 USD | 66,500.00 USD |
| `7D` | `8.61` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 88,710.00 USD | 35,810.00 USD | 229,070.00 USD |
| `1D` | `8.63` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 140,670.00 USD | 19,620.00 USD | 32,560.00 USD |
| `7D` | `8.63` | 904,370.00 USD | 0.00 USD | 904,370.00 USD | 51,260.00 USD | 25,450.00 USD | 23,830.00 USD |
| `1D` | `8.65` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 119,470.00 USD | 38,180.00 USD | 30,200.00 USD |
| `7D` | `8.65` | 803,820.00 USD | 0.00 USD | 803,820.00 USD | 45,780.00 USD | 16,520.00 USD | 37,080.00 USD |
| `1D` | `8.67` | 866,850.00 USD | 0.00 USD | 866,850.00 USD | 69,760.00 USD | 25,380.00 USD | 28,580.00 USD |
| `7D` | `8.67` | 704,440.00 USD | 0.00 USD | 704,440.00 USD | 23,440.00 USD | 24,870.00 USD | 173,920.00 USD |
| `1D` | `8.69` | 743,130.00 USD | 0.00 USD | 743,130.00 USD | 39,070.00 USD | 5,700.00 USD | 22,180.00 USD |
| `7D` | `8.69` | 482,220.00 USD | 0.00 USD | 482,220.00 USD | 70,540.00 USD | 0.00 USD | 270.26 USD |
| `1D` | `8.71` | 676,180.00 USD | 0.00 USD | 676,180.00 USD | 42,290.00 USD | 11,690.00 USD | 18,980.00 USD |
| `1D` | `8.73` | 603,230.00 USD | 0.00 USD | 603,230.00 USD | 44,990.00 USD | 2,720.00 USD | 5,120.00 USD |
| `1D` | `8.75` | 550,390.00 USD | 0.00 USD | 550,390.00 USD | 32,080.00 USD | 16,010.00 USD | 35,830.00 USD |
| `7D` | `8.75` | 411,400.00 USD | 0.00 USD | 411,400.00 USD | 144,660.00 USD | 19,690.00 USD | 56,610.00 USD |
| `1D` | `8.77` | 466,480.00 USD | 0.00 USD | 466,480.00 USD | 132,830.00 USD | 23,560.00 USD | 25,720.00 USD |
| `7D` | `8.77` | 190,450.00 USD | 0.00 USD | 190,450.00 USD | 26,810.00 USD | 0.00 USD | 81,240.00 USD |
| `1D` | `8.79` | 284,370.00 USD | 0.00 USD | 284,370.00 USD | 32,240.00 USD | 12,000.00 USD | 9,880.00 USD |
| `7D` | `8.79` | 82,400.00 USD | 0.00 USD | 82,400.00 USD | 27,360.00 USD | 25,300.00 USD | 0.00 USD |
| `1D` | `8.81` | 230,250.00 USD | 0.00 USD | 230,250.00 USD | 57,590.00 USD | 5,690.00 USD | 17,540.00 USD |
| `7D` | `8.81` | 29,750.00 USD | 0.00 USD | 29,750.00 USD | 0.00 USD | 8,450.00 USD | 21,290.00 USD |
| `1D` | `8.83` | 149,420.00 USD | 0.00 USD | 149,420.00 USD | 30,220.00 USD | 0.00 USD | 21,070.00 USD |
| `1D` | `8.85` | 98,130.00 USD | 0.00 USD | 98,130.00 USD | 29,490.00 USD | 0.00 USD | 68,640.00 USD |
| `1D` | `8.87` | 67,380.00 USD | 67,380.00 USD | 0.00 USD | 67,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.87` | 134,760.00 USD | 134,760.00 USD | 0.00 USD | 67,380.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.87` | 78,770.00 USD | 78,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78,770.00 USD |
| `7D` | `8.87` | 157,550.00 USD | 157,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78,770.00 USD |
| `7D` | `8.89` | 202,030.00 USD | 202,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44,480.00 USD |
| `1D` | `8.91` | 212,520.00 USD | 212,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 77,770.00 USD |
| `7D` | `8.91` | 273,030.00 USD | 273,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 71,000.00 USD |
| `1D` | `8.93` | 224,090.00 USD | 224,090.00 USD | 0.00 USD | 8,060.00 USD | 0.00 USD | 3,500.00 USD |
| `1D` | `8.99` | 236,210.00 USD | 236,210.00 USD | 0.00 USD | 643.50 USD | 11,480.00 USD | 0.00 USD |
| `7D` | `8.99` | 367,270.00 USD | 367,270.00 USD | 0.00 USD | 94,240.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.01` | 237,290.00 USD | 237,290.00 USD | 0.00 USD | 1,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.01` | 470,770.00 USD | 470,770.00 USD | 0.00 USD | 67,320.00 USD | 36,180.00 USD | 0.00 USD |
| `1D` | `9.03` | 342,480.00 USD | 342,480.00 USD | 0.00 USD | 29,210.00 USD | 57,580.00 USD | 18,390.00 USD |
| `7D` | `9.03` | 591,340.00 USD | 591,340.00 USD | 0.00 USD | 4,290.00 USD | 101,140.00 USD | 15,140.00 USD |
| `1D` | `9.05` | 424,990.00 USD | 424,990.00 USD | 0.00 USD | 3,520.00 USD | 31,340.00 USD | 47,660.00 USD |
| `7D` | `9.05` | 648,800.00 USD | 648,800.00 USD | 0.00 USD | 35,710.00 USD | 4,910.00 USD | 16,840.00 USD |
| `1D` | `9.07` | 533,390.00 USD | 533,390.00 USD | 0.00 USD | 31,360.00 USD | 27,950.00 USD | 49,080.00 USD |
| `7D` | `9.07` | 689,170.00 USD | 689,170.00 USD | 0.00 USD | 3,990.00 USD | 14,140.00 USD | 22,240.00 USD |
| `1D` | `9.09` | 733,560.00 USD | 733,560.00 USD | 0.00 USD | 101,210.00 USD | 23,610.00 USD | 75,360.00 USD |
| `7D` | `9.09` | 983,450.00 USD | 983,450.00 USD | 0.00 USD | 150,640.00 USD | 8,680.00 USD | 134,960.00 USD |
| `1D` | `9.11` | 960,710.00 USD | 960,710.00 USD | 0.00 USD | 118,620.00 USD | 32,050.00 USD | 76,470.00 USD |
| `7D` | `9.11` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 847,950.00 USD | 37,620.00 USD | 546,100.00 USD |
| `1D` | `9.13` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 190,770.00 USD | 51,740.00 USD | 46,370.00 USD |
| `7D` | `9.13` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 690,230.00 USD | 26,540.00 USD | 484,570.00 USD |
| `1D` | `9.15` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 91,780.00 USD | 27,820.00 USD | 46,120.00 USD |
| `7D` | `9.15` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 357,020.00 USD | 38,700.00 USD | 249,190.00 USD |
| `1D` | `9.17` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 132,370.00 USD | 28,140.00 USD | 83,470.00 USD |
| `7D` | `9.17` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 365,640.00 USD | 133,490.00 USD | 274,710.00 USD |
| `1D` | `9.19` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 230,710.00 USD | 75,410.00 USD | 73,090.00 USD |
| `7D` | `9.19` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 487,090.00 USD | 101,150.00 USD | 193,560.00 USD |
| `1D` | `9.21` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 158,120.00 USD | 20,080.00 USD | 74,380.00 USD |
| `7D` | `9.21` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 527,540.00 USD | 132,850.00 USD | 277,380.00 USD |
| `1D` | `9.23` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 158,550.00 USD | 13,360.00 USD | 45,020.00 USD |
| `7D` | `9.23` | 7,760,000.00 USD | 7,760,000.00 USD | 0.00 USD | 562,300.00 USD | 82,070.00 USD | 360,220.00 USD |
| `1D` | `9.25` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 44,000.00 USD | 20,640.00 USD | 9,530.00 USD |
| `7D` | `9.25` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 277,290.00 USD | 73,690.00 USD | 141,060.00 USD |
| `1D` | `9.27` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 39,370.00 USD | 14,380.00 USD | 2,560.00 USD |
| `7D` | `9.27` | 8,580,000.00 USD | 8,580,000.00 USD | 0.00 USD | 156,190.00 USD | 118,550.00 USD | 54,650.00 USD |
| `1D` | `9.29` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 69,190.00 USD | 22,120.00 USD | 41,430.00 USD |
| `7D` | `9.29` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 468,150.00 USD | 100,200.00 USD | 290,580.00 USD |
| `1D` | `9.31` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 98,430.00 USD | 20,310.00 USD | 32,290.00 USD |
| `7D` | `9.31` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 307,520.00 USD | 55,090.00 USD | 329,420.00 USD |
| `1D` | `9.33` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 26,620.00 USD | 8,530.00 USD | 26,550.00 USD |
| `7D` | `9.33` | 10,500,000.00 USD | 10,500,000.00 USD | 0.00 USD | 124,660.00 USD | 64,710.00 USD | 178,910.00 USD |
| `1D` | `9.35` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 44,830.00 USD | 8,000.00 USD | 37,880.00 USD |
| `7D` | `9.35` | 10,980,000.00 USD | 10,980,000.00 USD | 0.00 USD | 289,480.00 USD | 93,460.00 USD | 96,160.00 USD |
| `1D` | `9.37` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 103,920.00 USD | 27,030.00 USD | 31,040.00 USD |
| `7D` | `9.37` | 11,490,000.00 USD | 11,490,000.00 USD | 0.00 USD | 369,360.00 USD | 34,660.00 USD | 108,520.00 USD |
| `1D` | `9.39` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 64,010.00 USD | 5,770.00 USD | 30,260.00 USD |
| `7D` | `9.39` | 11,850,000.00 USD | 11,850,000.00 USD | 0.00 USD | 206,980.00 USD | 62,160.00 USD | 87,830.00 USD |
| `1D` | `9.41` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 74,750.00 USD | 2,860.00 USD | 16,990.00 USD |
| `7D` | `9.41` | 12,300,000.00 USD | 12,300,000.00 USD | 0.00 USD | 265,320.00 USD | 41,500.00 USD | 147,960.00 USD |
| `1D` | `9.43` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 21,010.00 USD | 7,570.00 USD | 16,400.00 USD |
| `7D` | `9.43` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 101,970.00 USD | 43,920.00 USD | 95,770.00 USD |
| `1D` | `9.45` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 3,120.00 USD | 4,940.00 USD | 2,500.00 USD |
| `7D` | `9.45` | 12,680,000.00 USD | 12,680,000.00 USD | 0.00 USD | 105,560.00 USD | 16,970.00 USD | 9,710.00 USD |
| `1D` | `9.47` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 19,830.00 USD | 11,450.00 USD | 302.82 USD |
| `7D` | `9.47` | 12,790,000.00 USD | 12,790,000.00 USD | 0.00 USD | 53,420.00 USD | 32,300.00 USD | 25,670.00 USD |
| `1D` | `9.49` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 22,590.00 USD | 572.85 USD | 10,750.00 USD |
| `7D` | `9.49` | 12,900,000.00 USD | 12,900,000.00 USD | 0.00 USD | 26,920.00 USD | 36,710.00 USD | 42,990.00 USD |
| `1D` | `9.51` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 12,280.00 USD | 3,160.00 USD | 6,390.00 USD |
| `7D` | `9.51` | 13,230,000.00 USD | 13,230,000.00 USD | 0.00 USD | 148,110.00 USD | 43,360.00 USD | 142,340.00 USD |
| `1D` | `9.53` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 36,770.00 USD | 7,630.00 USD | 5,520.00 USD |
| `7D` | `9.53` | 13,440,000.00 USD | 13,440,000.00 USD | 0.00 USD | 187,750.00 USD | 15,360.00 USD | 6,760.00 USD |
| `1D` | `9.55` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 8,810.00 USD | 7,800.00 USD | 6,030.00 USD |
| `7D` | `9.55` | 13,510,000.00 USD | 13,510,000.00 USD | 0.00 USD | 28,850.00 USD | 19,960.00 USD | 20,010.00 USD |
| `1D` | `9.57` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 6,850.00 USD | 4,390.00 USD | 7,390.00 USD |
| `7D` | `9.57` | 13,670,000.00 USD | 13,670,000.00 USD | 0.00 USD | 116,450.00 USD | 14,280.00 USD | 33,320.00 USD |
| `1D` | `9.59` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 6,340.00 USD | 1,820.00 USD | 8,900.00 USD |
| `7D` | `9.59` | 13,740,000.00 USD | 13,740,000.00 USD | 0.00 USD | 29,010.00 USD | 15,650.00 USD | 23,150.00 USD |
| `1D` | `9.61` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 24,500.00 USD | 3,090.00 USD | 22,890.00 USD |
| `7D` | `9.61` | 13,860,000.00 USD | 13,860,000.00 USD | 0.00 USD | 82,080.00 USD | 13,850.00 USD | 28,920.00 USD |
| `1D` | `9.63` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 11,660.00 USD | 4,370.00 USD | 1,230.00 USD |
| `7D` | `9.63` | 13,920,000.00 USD | 13,920,000.00 USD | 0.00 USD | 42,830.00 USD | 4,500.00 USD | 6,980.00 USD |
| `1D` | `9.65` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 11,790.00 USD | 4,150.00 USD | 5,130.00 USD |
| `7D` | `9.65` | 13,990,000.00 USD | 13,990,000.00 USD | 0.00 USD | 33,020.00 USD | 20,230.00 USD | 18,210.00 USD |
| `1D` | `9.67` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 11,920.00 USD | 3,480.00 USD | 8,020.00 USD |
| `7D` | `9.67` | 14,060,000.00 USD | 14,060,000.00 USD | 0.00 USD | 31,000.00 USD | 24,380.00 USD | 18,390.00 USD |
| `1D` | `9.69` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 12,900.00 USD | 2,950.00 USD | 4,060.00 USD |
| `7D` | `9.69` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 121,550.00 USD | 17,380.00 USD | 33,860.00 USD |
| `1D` | `9.71` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 7,790.00 USD | 8,290.00 USD | 4,160.00 USD |
| `7D` | `9.71` | 14,370,000.00 USD | 14,370,000.00 USD | 0.00 USD | 81,870.00 USD | 9,500.00 USD | 42,550.00 USD |
| `1D` | `9.73` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 133.15 USD | 1,790.00 USD | 0.00 USD |
| `7D` | `9.73` | 14,390,000.00 USD | 14,390,000.00 USD | 0.00 USD | 5,340.00 USD | 3,160.00 USD | 11,740.00 USD |
| `1D` | `9.75` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 8,370.00 USD | 661.94 USD | 3,640.00 USD |
| `7D` | `9.75` | 14,460,000.00 USD | 14,460,000.00 USD | 0.00 USD | 25,630.00 USD | 15,540.00 USD | 29,890.00 USD |
| `1D` | `9.77` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 6,860.00 USD | 2,050.00 USD | 4,440.00 USD |
| `7D` | `9.77` | 14,570,000.00 USD | 14,570,000.00 USD | 0.00 USD | 51,320.00 USD | 7,410.00 USD | 46,350.00 USD |
| `1D` | `9.79` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 5,790.00 USD | 1,840.00 USD | 1,800.00 USD |
| `7D` | `9.79` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 48,830.00 USD | 17,990.00 USD | 729.68 USD |
| `1D` | `9.81` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 16,020.00 USD | 2,310.00 USD | 4,140.00 USD |
| `7D` | `9.81` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 103,830.00 USD | 23,930.00 USD | 48,340.00 USD |
| `1D` | `9.83` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 23,460.00 USD | 4,800.00 USD | 13,380.00 USD |
| `7D` | `9.83` | 14,930,000.00 USD | 14,930,000.00 USD | 0.00 USD | 31,840.00 USD | 29,270.00 USD | 62,530.00 USD |
| `1D` | `9.85` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 11,610.00 USD | 1,700.00 USD | 3,530.00 USD |
| `7D` | `9.85` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 50,490.00 USD | 2,210.00 USD | 49,830.00 USD |
| `1D` | `9.87` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 4,540.00 USD | 2,400.00 USD | 8,380.00 USD |
| `7D` | `9.87` | 15,090,000.00 USD | 15,090,000.00 USD | 0.00 USD | 15,580.00 USD | 8,710.00 USD | 25,970.00 USD |
| `1D` | `9.89` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 12,790.00 USD | 2,630.00 USD | 9,600.00 USD |
| `7D` | `9.89` | 15,170,000.00 USD | 15,170,000.00 USD | 0.00 USD | 33,970.00 USD | 16,210.00 USD | 27,630.00 USD |
| `1D` | `9.91` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 26,230.00 USD | 7,990.00 USD | 9,420.00 USD |
| `7D` | `9.91` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 32,670.00 USD | 10,160.00 USD | 7,620.00 USD |
| `1D` | `9.93` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 15,840.00 USD | 693.45 USD | 8,590.00 USD |
| `7D` | `9.93` | 15,280,000.00 USD | 15,280,000.00 USD | 0.00 USD | 31,960.00 USD | 11,560.00 USD | 20,650.00 USD |
| `1D` | `9.95` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 16,900.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.95` | 15,360,000.00 USD | 15,360,000.00 USD | 0.00 USD | 55,780.00 USD | 3,730.00 USD | 24,820.00 USD |
| `1D` | `9.97` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 12,840.00 USD | 662.47 USD | 4,940.00 USD |
| `7D` | `9.97` | 15,420,000.00 USD | 15,420,000.00 USD | 0.00 USD | 29,800.00 USD | 1,360.00 USD | 21,720.00 USD |
| `1D` | `9.99` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 2,120.00 USD | 45.06 USD |
| `7D` | `9.99` | 15,430,000.00 USD | 15,430,000.00 USD | 0.00 USD | 840.10 USD | 7,770.00 USD | 8,430.00 USD |
| `7D` | `10.01` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 15,960.00 USD | 3,170.00 USD | 0.00 USD |
| `7D` | `10.03` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,800.00 USD |
| `7D` | `10.04` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 6,740.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `383.85M` | Total OI Tokens: `43,279,389.5 AVAX`
  * 1h OI Change: `-0.07%` | 4h OI Change: `+0.43%` | 24h OI Change: `-1.51%`
  * Exchange Breakdown: Binance=`89.46M` | Bybit=`59.63M` | OKX=`12.78M` | Hyperliquid=`17.69M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `15.63K` | Last 24h: `33.77K` | Last 3d: `72.05K` | Last 7d: `92.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0092%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `53.00%` | `47.00%` | `1.13` | 4,960,000.00 USD |
| `15M` | `Binance` | `58.07%` | `41.93%` | `1.38` | 1,140,000.00 USD |
| `15M` | `OKX` | `66.86%` | `33.14%` | `2.02` | 421,440.00 USD |
| `15M` | `Bybit` | `65.26%` | `34.74%` | `1.88` | 394,340.00 USD |
| `15M` | `KuCoin` | `52.14%` | `47.86%` | `1.09` | 66,090.00 USD |
| `15M` | `Gate` | `16.23%` | `83.77%` | `0.19` | 49,660.00 USD |
| `15M` | `Bitget` | `62.22%` | `37.78%` | `1.65` | 82,580.00 USD |
| `15M` | `BingX` | `44.16%` | `55.84%` | `0.79` | 204,460.00 USD |
| `15M` | `MEXC` | `50.34%` | `49.66%` | `1.01` | 2,180,000.00 USD |
| `15M` | `Bitunix` | `55.5%` | `44.5%` | `1.25` | 87,010.00 USD |
| `15M` | `Hyperliquid` | `32.28%` | `67.72%` | `0.48` | 52,320.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `53.01%` | `46.99%` | `1.13` | 117,180.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 143,870.00 USD |
| `15M` | `HTX` | `73.81%` | `26.19%` | `2.82` | 570.88 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `89.51%` | `10.49%` | `8.53` | 26,490.00 USD |
| `15M` | `Aster` | `9.08%` | `90.92%` | `0.10` | 372.28 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `8.38%` | `91.62%` | `0.09` | 4,370.00 USD |
| `15M` | `Whale Positions` | `58.07%` | `41.93%` | `1.38` | 1,140,000.00 USD |
| `15M` | `Global Accounts` | `53.00%` | `47.00%` | `1.13` | 4,960,000.00 USD |
| `1H` | `AVAX` | `41.33%` | `58.67%` | `0.70` | 21,850,000.00 USD |
| `1H` | `Binance` | `40.21%` | `59.79%` | `0.67` | 6,720,000.00 USD |
| `1H` | `OKX` | `31.15%` | `68.85%` | `0.45` | 1,850,000.00 USD |
| `1H` | `Bybit` | `51.31%` | `48.69%` | `1.05` | 1,380,000.00 USD |
| `1H` | `KuCoin` | `53.56%` | `46.44%` | `1.15` | 104,370.00 USD |
| `1H` | `Gate` | `51.51%` | `48.49%` | `1.06` | 473,970.00 USD |
| `1H` | `Bitget` | `30.3%` | `69.7%` | `0.43` | 538,770.00 USD |
| `1H` | `BingX` | `45.05%` | `54.95%` | `0.82` | 3,460,000.00 USD |
| `1H` | `MEXC` | `56.63%` | `43.37%` | `1.31` | 1,340,000.00 USD |
| `1H` | `Bitunix` | `56.74%` | `43.26%` | `1.31` | 1,060,000.00 USD |
| `1H` | `Hyperliquid` | `39.01%` | `60.99%` | `0.64` | 72,100.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.33%` | `52.67%` | `0.90` | 3,260,000.00 USD |
| `1H` | `Crypto.com` | `44.96%` | `55.04%` | `0.82` | 3,890.00 USD |
| `1H` | `WhiteBIT` | `0%` | `100%` | `0.00` | 1,420,000.00 USD |
| `1H` | `HTX` | `45.17%` | `54.83%` | `0.82` | 3,210.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `41.61%` | `58.39%` | `0.71` | 88,460.00 USD |
| `1H` | `Aster` | `68.48%` | `31.52%` | `2.17` | 63,950.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `44.4%` | `55.6%` | `0.80` | 18,920.00 USD |
| `1H` | `Whale Positions` | `40.21%` | `59.79%` | `0.67` | 6,720,000.00 USD |
| `1H` | `Global Accounts` | `41.33%` | `58.67%` | `0.70` | 21,850,000.00 USD |
| `4H` | `AVAX` | `45.06%` | `54.94%` | `0.82` | 90,780,000.00 USD |
| `4H` | `Binance` | `46.09%` | `53.91%` | `0.85` | 30,480,000.00 USD |
| `4H` | `OKX` | `45.74%` | `54.26%` | `0.84` | 6,410,000.00 USD |
| `4H` | `Bybit` | `48.93%` | `51.07%` | `0.96` | 5,150,000.00 USD |
| `4H` | `KuCoin` | `51.44%` | `48.56%` | `1.06` | 644,990.00 USD |
| `4H` | `Gate` | `45.49%` | `54.51%` | `0.83` | 2,090,000.00 USD |
| `4H` | `Bitget` | `45.75%` | `54.25%` | `0.84` | 1,810,000.00 USD |
| `4H` | `BingX` | `46.38%` | `53.62%` | `0.86` | 13,970,000.00 USD |
| `4H` | `MEXC` | `45.25%` | `54.75%` | `0.83` | 5,340,000.00 USD |
| `4H` | `Bitunix` | `56.31%` | `43.69%` | `1.29` | 3,530,000.00 USD |
| `4H` | `Hyperliquid` | `64.27%` | `35.73%` | `1.80` | 937,020.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.41%` | `48.59%` | `1.06` | 14,550,000.00 USD |
| `4H` | `Crypto.com` | `82.71%` | `17.29%` | `4.78` | 12,950.00 USD |
| `4H` | `WhiteBIT` | `0.09%` | `99.91%` | `0.00` | 5,210,000.00 USD |
| `4H` | `HTX` | `27.22%` | `72.78%` | `0.37` | 25,750.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.53%` | `54.47%` | `0.84` | 304,920.00 USD |
| `4H` | `Aster` | `58.75%` | `41.25%` | `1.42` | 129,320.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `54.15%` | `45.85%` | `1.18` | 156,450.00 USD |
| `4H` | `Whale Positions` | `46.09%` | `53.91%` | `0.85` | 30,480,000.00 USD |
| `4H` | `Global Accounts` | `45.06%` | `54.94%` | `0.82` | 90,780,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `9.00` | `8.99` | `9.00` | `9.02` | `8.97` | 1,973,140.24 USD | 1,143,345.57 USD | 829,794.67 USD | 313,550.89 USD | `+15.89%` | `8B / 6S` |
| `0:00 UTC` | `9.03` | `9.03` | `9.03` | `9.08` | `8.98` | 3,148,369.91 USD | 1,756,400.23 USD | 1,391,969.68 USD | 364,430.55 USD | `+11.58%` | `25B / 11S` |
| `5:00 UTC` | `8.97` | `8.99` | `8.97` | `9.03` | `8.96` | 2,070,720.90 USD | 687,717.97 USD | 1,383,002.93 USD | -695,284.97 USD | `-33.58%` | `10B / 24S` |
| `0:00 UTC` | `8.94` | `8.95` | `8.94` | `8.97` | `8.93` | 1,552,686.03 USD | 580,933.43 USD | 971,752.60 USD | -390,819.17 USD | `-25.17%` | `3B / 11S` |
| `5:00 UTC` | `8.95` | `8.95` | `8.95` | `8.96` | `8.93` | 786,504.93 USD | 221,063.85 USD | 565,441.08 USD | -344,377.23 USD | `-43.79%` | `0B / 11S` |
| `0:00 UTC` | `8.93` | `8.93` | `8.93` | `8.96` | `8.91` | 1,932,405.67 USD | 423,821.82 USD | 1,508,583.84 USD | -1,084,762.02 USD | `-56.14%` | `2B / 26S` |
| `5:00 UTC` | `8.91` | `8.92` | `8.91` | `8.94` | `8.90` | 1,295,523.82 USD | 616,181.90 USD | 679,341.92 USD | -63,160.02 USD | `-4.88%` | `3B / 6S` |
| `0:00 UTC` | `8.94` | `8.90` | `8.94` | `8.94` | `8.85` | 1,871,719.04 USD | 766,811.36 USD | 1,104,907.68 USD | -338,096.31 USD | `-18.06%` | `8B / 28S` |
| `5:00 UTC` | `8.85` | `8.85` | `8.85` | `8.87` | `8.82` | 1,418,137.84 USD | 651,843.02 USD | 766,294.83 USD | -114,451.81 USD | `-8.07%` | `11B / 12S` |
| `0:00 UTC` | `8.87` | `8.87` | `8.87` | `8.88` | `8.86` | 188,017.82 USD | 102,384.30 USD | 85,633.52 USD | 16,750.78 USD | `+8.91%` | `2B / 3S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:30` | `Range 0.025` | `Divergence` | **`BEARISH`** | Rally without taker buying | `8.88` | 0.00 USD | 0.00 USD |
| `10-28 20:17` | `Volume 200K AVAX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `8.88` | 0.00 USD | 0.00 USD |
| `10-28 19:50` | `Volume 200K AVAX` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `8.79` | 0.00 USD | 0.00 USD |
| `10-28 19:17` | `Volume 200K AVAX` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `8.81` | 35,000.00 USD | 0.00 USD |
| `10-28 19:17` | `Range 0.025` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `8.81` | 35,000.00 USD | 0.00 USD |
| `10-28 19:17` | `Range 0.025` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `8.81` | 28,000.00 USD | 0.00 USD |
| `10-28 19:05` | `Volume 200K AVAX` | `Divergence` | **`BULLISH`** | Drop without taker selling | `8.86` | 0.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.025` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `8.85` | 15,000.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.025` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `8.85` | 15,000.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 200K AVAX` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `8.90` | 0.00 USD | 0.00 USD |
| `10-28 17:35` | `Volume 200K AVAX` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `8.96` | 41,000.00 USD | 0.00 USD |
| `10-28 15:02` | `Range 0.025` | `Divergence` | **`BEARISH`** | Rally without taker buying | `9.02` | 0.00 USD | 0.00 USD |
| `10-28 15:02` | `Range 0.025` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `8.99` | 0.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.025` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `9.08` | 114,000.00 USD | 0.00 USD |
| `10-28 14:01` | `Volume 200K AVAX` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `9.08` | 125,000.00 USD | 0.00 USD |
| `10-28 13:57` | `Range 0.025` | `Divergence` | **`BULLISH`** | Drop without taker selling | `9.03` | 0.00 USD | 0.00 USD |
| `10-28 13:44` | `Range 0.025` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `9.00` | 16,000.00 USD | 0.00 USD |
| `10-28 12:46` | `Range 0.025` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `8.95` | 0.00 USD | 0.00 USD |
| `10-28 09:02` | `Volume 200K AVAX` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `9.08` | 38,000.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.025` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `9.07` | 0.00 USD | 0.00 USD |
| `10-28 06:13` | `Range 0.025` | `Divergence` | **`BEARISH`** | Rally without taker buying | `8.98` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 24,830.00 USD | 124,980.00 USD | **`ACCUMULATION`** |
| `15m` | -18,090.00 USD | 332,260.00 USD | **`ACCUMULATION`** |
| `30m` | -163,440.00 USD | -1,260,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -156,890.00 USD | -2,110,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -235,040.00 USD | -4,070,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 237,580.00 USD | -3,130,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -19,150.00 USD | -2,370,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -145,060.00 USD | -3,270,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -273,780.00 USD | -2,820,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -135,030.00 USD | -4,840,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,710,000.00 USD | -42,680,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -52,650,000.00 USD | -274,760,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+24.83K` | 15m=`-18.09K` | 1h=`-156.89K` | 24h=`-135.03K`
* Futures Capital Netflows: 5m=`+124.98K` | 15m=`+332.26K` | 1h=`-2.11M` | 24h=`-4.84M`
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
  * `2026-10-29 23:31:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:35 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:35 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:35 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:35 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:35 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:35 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `8.54` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `8.43` (Risk Distance: `0.1131` pts)
  * +2.5R Take Profit: `8.82`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.89` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `9.00` (Risk Distance: `0.1131` pts)
  * +2.5R Take Profit: `8.61`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.95`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
