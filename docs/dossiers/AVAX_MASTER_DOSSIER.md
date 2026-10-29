# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 03:49:31 IST` (`2026-10-29 22:19:31 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.35` | **Live Ask Quote**: `8.38` | **Mid Price**: `8.37`
- **Spread Points**: `3.00` | **Spread BPS**: `35.86 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.68` | VWAP Z-Score: `-1.81` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0992` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `28.91` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `9.22` | Lower -3.00σ Band: `8.15`
  * Upper +2.51σ Band: `9.13` | Lower -2.51σ Band: `8.23`
  * Upper +2.01σ Band: `9.05` | Lower -2.01σ Band: `8.32`
  * Upper +2.00σ Band: `9.04` | Lower -2.00σ Band: `8.33`
  * Upper +1.28σ Band: `8.91` | Lower -1.28σ Band: `8.46`
  * Upper +1.00σ Band: `8.86` | Lower -1.00σ Band: `8.51`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.49` | EMA-20=`8.61` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.71` (Slope: `+0.0000`) | EMA-100=`8.76`
  * Institutional Anchors: EMA-144=`8.78` | EMA-200=`8.79` (Slope: `-0.3389`) | EMA-233=`8.80`
- **Range Boundaries**: 24H High=`9.06` | 24H Low=`8.24` | Weekly High=`9.14` | Weekly Low=`8.24`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.47` (Distance: `-1.17%`)
  * Point of Control (POC) = `8.44` (Distance: `-0.83%`)
  * Value Area Low (VAL) = `8.29` (Distance: `+0.95%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`8.90` | POC=`8.74` | VAL=`8.55`
  * Prior Day Extremes: PDH=`9.06` | PDL=`8.24` | PDC=`8.33`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`8.98` | Weekly POC=`8.91` | Weekly VAL=`8.74`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`8.58` | Low=`8.29`
  * London Session (08:00-16:00 UTC): High=`8.40` | Low=`8.33`
  * New York Session (13:00-21:00 UTC): High=`8.42` | Low=`8.31`
  * Initial Balance (First Hour): IB High=`8.39` | IB Low=`8.34`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.33` - `8.40`
  * Optimal Trade Entry (OTE 0.705): `8.38`
  * Structural Invalidation Anchor (0.786): `8.43`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.38` | `8.39` | `8.32` | `8.37` | `195,009` | 1,629,912.68 USD | 25,992.47 USD | `+1.59%` | -9,452,268.32 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `8.37` | `8.45` | `8.36` | `8.38` | `313,920` | 2,637,141.02 USD | 1,441,648.65 USD | `+54.67%` | -8,010,619.67 USD | `+1.68` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `8.38` | `8.39` | `8.37` | `8.39` | `5,671` | 47,521.49 USD | 3,769.84 USD | `+7.93%` | -8,006,849.83 USD | `+0.15` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `8.47` | `8.48` | `8.42` | `8.43` | `326,871` | 2,763,123.34 USD | 393,046.81 USD | `+14.22%` | -9,431,777.17 USD | `+0.66` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `8.43` | `8.45` | `8.32` | `8.38` | `760,789` | 6,384,975.85 USD | 1,516,824.48 USD | `+23.76%` | -7,914,952.69 USD | `+1.49` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `8.38` | `8.38` | `8.37` | `8.38` | `4,233` | 35,465.48 USD | -7,649.06 USD | `-21.57%` | -7,922,601.75 USD | `+0.16` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `8.85` | `8.86` | `8.25` | `8.35` | `4,480,707` | 38,039,389.45 USD | -6,440,743.86 USD | `-16.93%` | -10,832,699.15 USD | `-4.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `8.35` | `8.60` | `8.31` | `8.43` | `1,902,791` | 16,105,514.90 USD | 1,294,377.61 USD | `+8.04%` | -9,538,321.54 USD | `+1.16` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `8.43` | `8.45` | `8.32` | `8.38` | `767,462` | 6,440,898.76 USD | 1,512,192.91 USD | `+23.48%` | -8,026,128.63 USD | `+1.18` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -2,154,015.33 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -4,666,010.97 USD | `-1.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.25` | `8.38` | `7,148,520` | 60,565,345.68 USD | -3,637,190.83 USD | `-6.01%` | -8,303,201.80 USD | `-1.48` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.59` | `8.80` | `8.57` | `8.62` | `1,816,830` | 15,790,058.74 USD | 58,580.54 USD | `+0.37%` | -2,364,450.84 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | -2,100,193.35 USD | `+0.79` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -2,154,015.33 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -4,666,010.97 USD | `-1.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.25` | `8.38` | `7,148,520` | 60,565,345.68 USD | -3,637,190.83 USD | `-6.01%` | -8,303,201.80 USD | `-1.48` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`8.37`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `8.37` | `35.3500` | 296.05 USD | 8,739.31 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.37` | `955.2900` | 7,999.69 USD | 16,739.01 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.37` | `105.2800` | 881.61 USD | 17,620.62 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.37` | `120.0800` | 1,005.50 USD | 18,626.12 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.37` | `105.2800` | 881.56 USD | 19,507.69 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.37` | `105.2400` | 881.21 USD | 20,388.89 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.37` | `1659.8200` | 13,898.00 USD | 34,286.90 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.37` | `5.8000` | 48.56 USD | 34,335.46 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.37` | `12.0000` | 100.47 USD | 34,435.93 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.37` | `505.8300` | 4,234.76 USD | 38,670.69 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `8.37` | `20.0000` | 167.44 USD | 38,838.12 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.37` | `18.0000` | 150.69 USD | 38,988.81 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.37` | `105.2300` | 880.90 USD | 39,869.71 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.37` | `105.2400` | 880.96 USD | 40,750.67 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `8.37` | `298.6800` | 2,499.98 USD | 43,250.66 USD | `1 orders` | `-0.09%` | `-` |
| `BID` | `8.37` | `105.3000` | 881.35 USD | 44,132.01 USD | `1 orders` | `-0.09%` | `-` |
| `ASK` | `8.38` | `105.2500` | 882.50 USD | 34,994.85 USD | `1 orders` | `+0.09%` | `-` |
| `ASK` | `8.38` | `124.8400` | 1,046.75 USD | 34,112.35 USD | `2 orders` | `+0.09%` | `-` |
| `ASK` | `8.38` | `403.4100` | 3,382.31 USD | 33,065.60 USD | `3 orders` | `+0.08%` | `-` |
| `ASK` | `8.38` | `1659.8200` | 13,916.26 USD | 29,683.29 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `8.38` | `105.2700` | 882.55 USD | 15,767.03 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `8.38` | `60.3400` | 505.86 USD | 14,884.48 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.38` | `105.2600` | 882.39 USD | 14,378.62 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.38` | `293.0700` | 2,456.63 USD | 13,496.22 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.38` | `5.8000` | 48.62 USD | 11,039.59 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `8.38` | `233.3900` | 1,956.20 USD | 10,990.98 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `8.38` | `105.2500` | 882.10 USD | 9,034.77 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.38` | `105.2700` | 882.26 USD | 8,152.67 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.38` | `120.0800` | 1,006.34 USD | 7,270.42 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.38` | `225.3300` | 1,888.29 USD | 6,264.07 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `8.38` | `105.2500` | 881.98 USD | 4,375.79 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.38` | `78.9300` | 661.37 USD | 3,493.80 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.38` | `45.0000` | 377.05 USD | 2,832.43 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.38` | `105.2500` | 881.84 USD | 2,455.38 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `8.38` | `187.8100` | 1,573.55 USD | 1,573.55 USD | `1 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `8.38` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.38` | `0.00%` | `-` |
| `BID` | `8.38` | `16.0000` | 134.02 USD | 134.02 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.38` | `5.5800` | 46.74 USD | 180.76 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.38` | `270.1700` | 2,262.92 USD | 2,443.68 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `8.38` | `716.3600` | 5,999.59 USD | 8,443.27 USD | `1 orders` | `-0.03%` | `-` |
| `ASK` | `8.39` | `29.6300` | 248.46 USD | 35,243.31 USD | `1 orders` | `+0.10%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:45:41 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1509` | `0x7737...bf66` | `SHORT` | 1,452,975.59 USD | `171,568.06` | `7.43` | `8.32` | `106.45` | -177,430.57 USD | `-12.21%` | `10X Cross` |
| `1601` | `0xeadc...9d55` | `LONG` | 1,350,147.15 USD | `160,070.56` | `8.11` | `8.32` | `0.000000` | 52,509.58 USD | `+3.89%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `8.87` | 7,970.62 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 7.97K USD at 8.8660 USD [API] | `2026-10-28 13:19:55` |
| `ANNOUNCEMENT` | `INFO` | `8.87` | 5,999.22 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 6.00K USD at 8.8675 USD [API] | `2026-10-28 13:19:55` |
| `ANNOUNCEMENT` | `INFO` | `8.87` | 8,000.78 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 8.00K USD at 8.8730 USD [API] | `2026-10-28 16:04:47` |
| `ANNOUNCEMENT` | `INFO` | `8.97` | 14,951.28 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 14.95K USD at 8.9658 USD [API] | `2026-10-28 18:44:15` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`9.10` (Vol: 233,400.00 USD, Dist: `+7.37%`) | Long MP=`8.25` (Vol: 29,200.00 USD, Dist: `--2.62%`)
  * 48H Horizon: Short MP=`9.10` (Vol: 233,400.00 USD, Dist: `+7.39%`) | Long MP=`8.26` (Vol: 29,200.00 USD, Dist: `--2.59%`)
  * 3D Horizon: Short MP=`9.22` (Vol: 251,900.00 USD, Dist: `+8.84%`) | Long MP=`8.26` (Vol: 29,200.00 USD, Dist: `--2.59%`)
  * 7D Horizon: Short MP=`9.28` (Vol: 426,900.00 USD, Dist: `+9.54%`) | Long MP=`8.25` (Vol: 29,200.00 USD, Dist: `--2.62%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `1.76` | 900.15 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 7,430.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.82` | 202.23 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 129.85 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 1,920.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.94` | 212.85 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 159.60 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 281.85 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 179.62 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 814.80 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 413.80 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 275.55 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 144.82 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 19,890.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 232.67 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111.12 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 359.99 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 229.95 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 6,650.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 151.88 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 1,310.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 570.75 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 891.25 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 120.55 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 109.95 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.98` | 254.04 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 159.29 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.18` | 174.89 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.21` | 442.57 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.33` | 186.71 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.36` | 185.83 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.41` | 1,820.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 110.77 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.53` | 422.27 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 486.93 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 2,680.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 105.11 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 8,380.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.70` | 7,040.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.71` | 110.61 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.82` | 2,890.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 467.01 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.86` | 15,950.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.89` | 146.85 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 527.19 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,740.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.93` | 244.87 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 5,160.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.03` | 167.78 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 314.59 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 504.74 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 318.46 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.11` | 118.44 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 250.20 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 5,800.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.14` | 2,570.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 2,510.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 2,250.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 1,050.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.28` | 160,550.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 640.70 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.30` | 509.55 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.32` | 232.85 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 716.11 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 660.46 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 21,630.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.47` | 1,320.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 20,330.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.51` | 367.41 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 121.38 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 2,760.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.57` | 967.98 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.59` | 34,430.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 468.55 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.68` | 274.13 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.72` | 2,390.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 238.86 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 2,890.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 736.72 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 58,750.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 106.65 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.83` | 145.88 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.84` | 561.53 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.86` | 2,110.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.88` | 128.94 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 984.70 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.93` | 147.19 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 11,720.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.99` | 447.98 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 432.77 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 105.61 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 1,680.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 405.14 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,130.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.11` | 1,090.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 1,140.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 137.02 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.13` | 2,030.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 4,390.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 187.29 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 3,390.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.32` | 277.04 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 5,900.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 284,770.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 6,590.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 6,430.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 367,520.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 1,050.00 USD | 784,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 3,620.00 USD | 783,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 779,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 1,770.00 USD | 770,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.59` | 1,100.00 USD | 768,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 767,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.67` | 1,640.00 USD | 765,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.70` | 506.54 USD | 764,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 16,610.00 USD | 763,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 746,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 6,780.00 USD | 745,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 16,960.00 USD | 738,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 4,930.00 USD | 721,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 1,500.00 USD | 716,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 2,670.00 USD | 715,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 158.14 USD | 712,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 4,410.00 USD | 712,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.86` | 19,810.00 USD | 708,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,340.00 USD | 688,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 1,580.00 USD | 685,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.89` | 5,250.00 USD | 683,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.91` | 269.30 USD | 678,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.92` | 1,840.00 USD | 678,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 3,760.00 USD | 676,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 3,480.00 USD | 672,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 636.74 USD | 668,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.97` | 961.64 USD | 668,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.99` | 1,100.00 USD | 667,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 746.58 USD | 666,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 20,860.00 USD | 665,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.01` | 281.86 USD | 644,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.04` | 704.50 USD | 644,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 354.23 USD | 643,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.07` | 9,860.00 USD | 643,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 6,700.00 USD | 633,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,420.00 USD | 626,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 28,230.00 USD | 625,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 597,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 2,300.00 USD | 596,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,270.00 USD | 594,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.16` | 4,800.00 USD | 574,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.17` | 215.59 USD | 569,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.17` | 28,700.00 USD | 569,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 540,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 9,400.00 USD | 538,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 791.63 USD | 529,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.24` | 179.65 USD | 528,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 185.83 USD | 528,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.26` | 419.41 USD | 528,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.28` | 243.64 USD | 528,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,420.00 USD | 527,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 1,680.00 USD | 491,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 4,910.00 USD | 489,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.34` | 4,370.00 USD | 484,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.36` | 3,000,000.00 USD | 3,000,000.00 USD | 6,810.00 USD | 2,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.37` | 5,720.00 USD | 480,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 5,020.00 USD | 474,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.39` | 1,550.00 USD | 469,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.40` | 2,990,000.00 USD | 2,990,000.00 USD | 6,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.41` | 854.02 USD | 468,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.42` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 62.56 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.42` | 2,950.00 USD | 467,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.43` | 19,480.00 USD | 464,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.44` | 2,980,000.00 USD | 2,980,000.00 USD | 331.70 USD | 1,680.00 USD | 15.01 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.45` | 210.99 USD | 444,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.46` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 1,410.00 USD | 3,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.46` | 5,630.00 USD | 444,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.47` | 2,230,000.00 USD | 2,230,000.00 USD | 723.17 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.47` | 2,740.00 USD | 438,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.48` | 2,980,000.00 USD | 2,980,000.00 USD | 9,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 962.81 USD | 436,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 421.78 USD | 435,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.51` | 2,230,000.00 USD | 2,230,000.00 USD | 1,020.00 USD | 2,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.52` | 2,970,000.00 USD | 2,970,000.00 USD | 1,150.00 USD | 7,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.53` | 2,230,000.00 USD | 2,230,000.00 USD | 9,830.00 USD | 7,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.54` | 5,720.00 USD | 434,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.54` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 4,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.55` | 2,210,000.00 USD | 2,210,000.00 USD | 306.57 USD | 4,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.55` | 572.67 USD | 429,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.56` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 4,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.57` | 25,060.00 USD | 428,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.58` | 1,850.00 USD | 403,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.59` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 175.24 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.59` | 24,760.00 USD | 401,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.61` | 1,520.00 USD | 376,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.61` | 2,210,000.00 USD | 2,210,000.00 USD | 989.00 USD | 3,770.00 USD | 11,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 375,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.63` | 2,190,000.00 USD | 2,190,000.00 USD | 986.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.63` | 378.93 USD | 374,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.64` | 2,950,000.00 USD | 2,950,000.00 USD | 812.40 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.65` | 2,190,000.00 USD | 2,190,000.00 USD | 16,880.00 USD | 0.00 USD | 9,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.66` | 1,410.00 USD | 374,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.66` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 23,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 1,740.00 USD | 372,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.67` | 140.45 USD | 371,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.68` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.68` | 1,120.00 USD | 370,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.70` | 1,460.00 USD | 369,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.71` | 2,160,000.00 USD | 2,160,000.00 USD | 3,940.00 USD | 4,030.00 USD | 26,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.72` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.73` | 2,130,000.00 USD | 2,130,000.00 USD | 2,170.00 USD | 0.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.74` | 2,880,000.00 USD | 2,880,000.00 USD | 976.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.75` | 2,120,000.00 USD | 2,120,000.00 USD | 1,320.00 USD | 5,690.00 USD | 192.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.76` | 2,880,000.00 USD | 2,880,000.00 USD | 812.95 USD | 5,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 368,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.77` | 2,110,000.00 USD | 2,110,000.00 USD | 34,420.00 USD | 572.85 USD | 14,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.78` | 695.32 USD | 367,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.78` | 2,880,000.00 USD | 2,880,000.00 USD | 43,620.00 USD | 4,900.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 2,870.00 USD | 367,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.79` | 2,070,000.00 USD | 2,070,000.00 USD | 45,170.00 USD | 12,560.00 USD | 5,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 12,800.00 USD | 364,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.80` | 2,810,000.00 USD | 2,810,000.00 USD | 14,770.00 USD | 12,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.81` | 2,000,000.00 USD | 2,000,000.00 USD | 6,750.00 USD | 7,800.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.82` | 3,720.00 USD | 351,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.82` | 2,780,000.00 USD | 2,780,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.83` | 1,980,000.00 USD | 1,980,000.00 USD | 5,390.00 USD | 4,390.00 USD | 7,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.84` | 2,770,000.00 USD | 2,770,000.00 USD | 30,950.00 USD | 2,380.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 24,340.00 USD | 347,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.85` | 1,970,000.00 USD | 1,970,000.00 USD | 5,240.00 USD | 3,060.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.86` | 2,710,000.00 USD | 2,710,000.00 USD | 25,770.00 USD | 5,460.00 USD | 17,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.87` | 1,950,000.00 USD | 1,950,000.00 USD | 31,020.00 USD | 4,570.00 USD | 28,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 323,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.88` | 2,660,000.00 USD | 2,660,000.00 USD | 58,120.00 USD | 12,780.00 USD | 30,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.89` | 1,880,000.00 USD | 1,880,000.00 USD | 30,650.00 USD | 9,580.00 USD | 9,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.90` | 2,560,000.00 USD | 2,560,000.00 USD | 33,680.00 USD | 12,890.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 505.13 USD | 322,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.91` | 1,830,000.00 USD | 1,830,000.00 USD | 17,770.00 USD | 3,480.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 9,330.00 USD | 322,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.92` | 2,500,000.00 USD | 2,500,000.00 USD | 55,490.00 USD | 8,420.00 USD | 14,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.93` | 1,800,000.00 USD | 1,800,000.00 USD | 23,780.00 USD | 5,660.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 16,340.00 USD | 313,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.94` | 2,420,000.00 USD | 2,420,000.00 USD | 51,390.00 USD | 9,960.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 127,110.00 USD | 296,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 1,770,000.00 USD | 1,770,000.00 USD | 12,440.00 USD | 9,310.00 USD | 8,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 2,180.00 USD | 169,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.96` | 2,320,000.00 USD | 2,320,000.00 USD | 21,840.00 USD | 6,920.00 USD | 26,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 4,520.00 USD | 167,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.97` | 1,740,000.00 USD | 1,740,000.00 USD | 14,420.00 USD | 5,620.00 USD | 4,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.97` | 1,580.00 USD | 162,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.98` | 2,270,000.00 USD | 2,270,000.00 USD | 56,660.00 USD | 19,680.00 USD | 70,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 8,100.00 USD | 161,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 1,710,000.00 USD | 1,710,000.00 USD | 4,980.00 USD | 1,380.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 2,560.00 USD | 153,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `8.00` | 2,120,000.00 USD | 2,120,000.00 USD | 61,850.00 USD | 10,300.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.01` | 284.42 USD | 150,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.01` | 1,700,000.00 USD | 1,700,000.00 USD | 7,530.00 USD | 9,110.00 USD | 2,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.02` | 1,880.00 USD | 150,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `8.02` | 2,040,000.00 USD | 2,040,000.00 USD | 20,910.00 USD | 46,670.00 USD | 11,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 1,070.00 USD | 148,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.03` | 1,690,000.00 USD | 1,690,000.00 USD | 44,660.00 USD | 22,490.00 USD | 446.01 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 87,460.00 USD | 147,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `8.04` | 1,970,000.00 USD | 1,970,000.00 USD | 123,080.00 USD | 38,980.00 USD | 86,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 10,010.00 USD | 59,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.05` | 1,620,000.00 USD | 1,620,000.00 USD | 25,230.00 USD | 20,600.00 USD | 6,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.05` | 1,230.00 USD | 49,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `8.06` | 1,720,000.00 USD | 1,720,000.00 USD | 73,280.00 USD | 20,850.00 USD | 86,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.07` | 1,570,000.00 USD | 1,570,000.00 USD | 45,920.00 USD | 4,100.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.07` | 232.96 USD | 48,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `8.08` | 1,540,000.00 USD | 1,540,000.00 USD | 7,170.00 USD | 8,710.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.09` | 3,400.00 USD | 48,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.09` | 1,510,000.00 USD | 1,510,000.00 USD | 13,650.00 USD | 2,630.00 USD | 7,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.10` | 2,040.00 USD | 45,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `8.10` | 1,500,000.00 USD | 1,500,000.00 USD | 61,500.00 USD | 19,700.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.11` | 7,100.00 USD | 43,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.11` | 1,490,000.00 USD | 1,490,000.00 USD | 47,180.00 USD | 15,540.00 USD | 33,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 241.26 USD | 35,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `8.12` | 1,400,000.00 USD | 1,400,000.00 USD | 27,520.00 USD | 10,810.00 USD | 22,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 843.86 USD | 35,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.13` | 1,390,000.00 USD | 1,390,000.00 USD | 55,540.00 USD | 4,640.00 USD | 3,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.13` | 855.64 USD | 34,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `8.14` | 1,340,000.00 USD | 1,340,000.00 USD | 72,460.00 USD | 11,150.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.15` | 1,320,000.00 USD | 1,320,000.00 USD | 52,860.00 USD | 0.00 USD | 204.31 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.16` | 1,220,000.00 USD | 1,220,000.00 USD | 38,430.00 USD | 5,510.00 USD | 30,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.16` | 11,540.00 USD | 33,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.17` | 1,270,000.00 USD | 1,270,000.00 USD | 3,360.00 USD | 14,530.00 USD | 49,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.18` | 1,150,000.00 USD | 1,150,000.00 USD | 39,830.00 USD | 43,260.00 USD | 84,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.19` | 1,200,000.00 USD | 1,200,000.00 USD | 56,520.00 USD | 40,360.00 USD | 469.45 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.20` | 8,590.00 USD | 22,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `8.20` | 978,050.00 USD | 978,050.00 USD | 33,800.00 USD | 22,240.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 1,910.00 USD | 13,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.21` | 1,110,000.00 USD | 1,110,000.00 USD | 3,540.00 USD | 0.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 147.87 USD | 11,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `8.22` | 912,150.00 USD | 912,150.00 USD | 19,610.00 USD | 21,570.00 USD | 10,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.22` | 2,100.00 USD | 11,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.23` | 1,080,000.00 USD | 1,080,000.00 USD | 26,390.00 USD | 43,740.00 USD | 41,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.24` | 860,180.00 USD | 860,180.00 USD | 39,950.00 USD | 3,480.00 USD | 107,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.25` | 966,820.00 USD | 966,820.00 USD | 73,710.00 USD | 1,150.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.26` | 9,710.00 USD | 9,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `8.26` | 709,660.00 USD | 709,660.00 USD | 30,490.00 USD | 5,750.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.27` | 882,360.00 USD | 882,360.00 USD | 48,820.00 USD | 33,090.00 USD | 21.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.28` | 671,710.00 USD | 671,710.00 USD | 122,850.00 USD | 33,920.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.29` | 800,430.00 USD | 800,430.00 USD | 267,700.00 USD | 25,810.00 USD | 115,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.30` | 465,080.00 USD | 465,080.00 USD | 152,370.00 USD | 11,360.00 USD | 48,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.31` | 391,550.00 USD | 391,550.00 USD | 107,430.00 USD | 28,950.00 USD | 20,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.32` | 253,290.00 USD | 253,290.00 USD | 42,900.00 USD | 0.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.33` | 234,430.00 USD | 234,430.00 USD | 96,630.00 USD | 0.00 USD | 94,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.34` | 205,330.00 USD | 205,330.00 USD | 58,620.00 USD | 0.00 USD | 146,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.35` | 43,730.00 USD | 43,730.00 USD | 0.00 USD | 0.00 USD | 43,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.36` | 209,880.00 USD | 209,880.00 USD | 78,130.00 USD | 0.00 USD | 131,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.36` | 419,760.00 USD | 419,760.00 USD | 78,130.00 USD | 0.00 USD | 131,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.37` | 34,500.00 USD | 34,500.00 USD | 691.75 USD | 0.00 USD | 33,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.37` | 69,000.00 USD | 69,000.00 USD | 691.75 USD | 0.00 USD | 33,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.38` | 606,650.00 USD | 606,650.00 USD | 120,320.00 USD | 0.00 USD | 66,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.39` | 222,740.00 USD | 222,740.00 USD | 0.00 USD | 0.00 USD | 153,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.40` | 797,170.00 USD | 797,170.00 USD | 155,410.00 USD | 0.00 USD | 35,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.42` | 964,470.00 USD | 964,470.00 USD | 166,020.00 USD | 0.00 USD | 1,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.43` | 223,530.00 USD | 223,530.00 USD | 788.46 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.44` | 1,120,000.00 USD | 1,120,000.00 USD | 155,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.46` | 445.41 USD | 445.41 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `8.46` | 1,490,000.00 USD | 1,490,000.00 USD | 365,050.00 USD | 0.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.46` | 279.34 USD | 724.75 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.47` | 223,550.00 USD | 223,550.00 USD | 0.00 USD | 0.00 USD | 18.78 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.47` | 456.29 USD | 1,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `8.48` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 35,130.00 USD | 1,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.48` | 1,850.00 USD | 3,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.49` | 309,090.00 USD | 309,090.00 USD | 0.00 USD | 85,530.00 USD | 12.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.50` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 100,070.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.51` | 479,410.00 USD | 479,410.00 USD | 92,450.00 USD | 77,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.52` | 1,770,000.00 USD | 1,770,000.00 USD | 2,990.00 USD | 135,400.00 USD | 1,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.53` | 632,950.00 USD | 632,950.00 USD | 113,180.00 USD | 40,360.00 USD | 1.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.54` | 1,880,000.00 USD | 1,880,000.00 USD | 13,020.00 USD | 100,610.00 USD | 2,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.55` | 715,420.00 USD | 715,420.00 USD | 82,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.56` | 2,600,000.00 USD | 2,600,000.00 USD | 593,510.00 USD | 122,650.00 USD | 790.79 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.57` | 1,030,000.00 USD | 1,030,000.00 USD | 197,600.00 USD | 33,670.00 USD | 87,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.58` | 3,360,000.00 USD | 3,360,000.00 USD | 599,490.00 USD | 164,810.00 USD | 801.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.59` | 1,200,000.00 USD | 1,200,000.00 USD | 58,280.00 USD | 29,830.00 USD | 82,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.60` | 3,480,000.00 USD | 3,480,000.00 USD | 75,040.00 USD | 39,160.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.61` | 1,330,000.00 USD | 1,330,000.00 USD | 28,330.00 USD | 54,870.00 USD | 39,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.62` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 43,670.00 USD | 26,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.63` | 1,570,000.00 USD | 1,570,000.00 USD | 126,840.00 USD | 53,490.00 USD | 58,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.64` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 5,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.65` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 33,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.66` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 16,520.00 USD | 992.53 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.67` | 1,800,000.00 USD | 1,800,000.00 USD | 78,620.00 USD | 7,270.00 USD | 119,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.68` | 4,110,000.00 USD | 4,110,000.00 USD | 207,090.00 USD | 43,100.00 USD | 290,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.69` | 1,950.00 USD | 4,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.69` | 1,900,000.00 USD | 1,900,000.00 USD | 24,580.00 USD | 20,180.00 USD | 48,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.70` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 23,910.00 USD | 46,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.71` | 1,950,000.00 USD | 1,950,000.00 USD | 54,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.73` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 28,810.00 USD | 50,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.74` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 30,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.75` | 2,060,000.00 USD | 2,060,000.00 USD | 33,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.76` | 373.93 USD | 5,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `8.76` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 22,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.77` | 2,240,000.00 USD | 2,240,000.00 USD | 153,570.00 USD | 0.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.78` | 4,300,000.00 USD | 4,300,000.00 USD | 2,300.00 USD | 0.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.79` | 2,370,000.00 USD | 2,370,000.00 USD | 65,930.00 USD | 21,430.00 USD | 38,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.80` | 4,390,000.00 USD | 4,390,000.00 USD | 27,360.00 USD | 33,750.00 USD | 31,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.81` | 2,510,000.00 USD | 2,510,000.00 USD | 110,240.00 USD | 10,330.00 USD | 23,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.82` | 4,490,000.00 USD | 4,490,000.00 USD | 103,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.82` | 6,000.00 USD | 11,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.83` | 2,560,000.00 USD | 2,560,000.00 USD | 40,210.00 USD | 8,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.85` | 2,670,000.00 USD | 2,670,000.00 USD | 13,330.00 USD | 2,250.00 USD | 94,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.86` | 4,600,000.00 USD | 4,600,000.00 USD | 29,310.00 USD | 0.00 USD | 82,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.87` | 2,680,000.00 USD | 2,680,000.00 USD | 2,380.00 USD | 0.00 USD | 148.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.88` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 28,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.89` | 2,720,000.00 USD | 2,720,000.00 USD | 3,280.00 USD | 11,100.00 USD | 32,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.90` | 4,750,000.00 USD | 4,750,000.00 USD | 2,440.00 USD | 0.00 USD | 115,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.91` | 2,900,000.00 USD | 2,900,000.00 USD | 60,600.00 USD | 13,350.00 USD | 103,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.91` | 126.41 USD | 11,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `8.92` | 4,770,000.00 USD | 4,770,000.00 USD | 1,730.00 USD | 0.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.93` | 2,960,000.00 USD | 2,960,000.00 USD | 40,520.00 USD | 0.00 USD | 21,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.94` | 4,830,000.00 USD | 4,830,000.00 USD | 58,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.95` | 2,980,000.00 USD | 2,980,000.00 USD | 10,600.00 USD | 12,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.96` | 4,830,000.00 USD | 4,830,000.00 USD | 1,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.97` | 2,990,000.00 USD | 2,990,000.00 USD | 670.84 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.98` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 9,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 3,120,000.00 USD | 3,120,000.00 USD | 73,440.00 USD | 36,070.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.00` | 5,170,000.00 USD | 5,170,000.00 USD | 297,650.00 USD | 11,360.00 USD | 20,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 3,190,000.00 USD | 3,190,000.00 USD | 38,950.00 USD | 9,530.00 USD | 22,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.02` | 5,260,000.00 USD | 5,260,000.00 USD | 34,650.00 USD | 56,120.00 USD | 749.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 3,390,000.00 USD | 3,390,000.00 USD | 107,510.00 USD | 66,510.00 USD | 32,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.04` | 5,440,000.00 USD | 5,440,000.00 USD | 90,520.00 USD | 74,750.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 3,510,000.00 USD | 3,510,000.00 USD | 25,720.00 USD | 37,250.00 USD | 49,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.06` | 5,520,000.00 USD | 5,520,000.00 USD | 7,440.00 USD | 14,960.00 USD | 53,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.07` | 3,630,000.00 USD | 3,630,000.00 USD | 43,430.00 USD | 30,110.00 USD | 52,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.08` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 3,880,000.00 USD | 3,880,000.00 USD | 129,020.00 USD | 27,290.00 USD | 88,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.10` | 6,790,000.00 USD | 6,790,000.00 USD | 826,500.00 USD | 35,760.00 USD | 334,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.11` | 4,120,000.00 USD | 4,120,000.00 USD | 134,540.00 USD | 38,180.00 USD | 64,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.12` | 7,780,000.00 USD | 7,780,000.00 USD | 490,020.00 USD | 24,170.00 USD | 479,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 4,410,000.00 USD | 4,410,000.00 USD | 192,240.00 USD | 51,740.00 USD | 46,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.14` | 8,820,000.00 USD | 8,820,000.00 USD | 536,560.00 USD | 18,540.00 USD | 479,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.15` | 4,570,000.00 USD | 4,570,000.00 USD | 92,380.00 USD | 25,540.00 USD | 42,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.16` | 9,420,000.00 USD | 9,420,000.00 USD | 358,370.00 USD | 44,360.00 USD | 195,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 4,850,000.00 USD | 4,850,000.00 USD | 171,770.00 USD | 40,560.00 USD | 71,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.18` | 10,420,000.00 USD | 10,420,000.00 USD | 565,140.00 USD | 162,460.00 USD | 273,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 5,140,000.00 USD | 5,140,000.00 USD | 162,530.00 USD | 72,140.00 USD | 58,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.20` | 11,330,000.00 USD | 11,330,000.00 USD | 549,250.00 USD | 127,380.00 USD | 238,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 5,320,000.00 USD | 5,320,000.00 USD | 109,250.00 USD | 17,130.00 USD | 46,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.21` | 1,870.00 USD | 13,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.22` | 12,480,000.00 USD | 12,480,000.00 USD | 585,170.00 USD | 144,840.00 USD | 416,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.23` | 5,390,000.00 USD | 5,390,000.00 USD | 54,700.00 USD | 11,900.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.24` | 13,030,000.00 USD | 13,030,000.00 USD | 316,220.00 USD | 56,410.00 USD | 174,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 5,460,000.00 USD | 5,460,000.00 USD | 49,760.00 USD | 7,080.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.26` | 13,460,000.00 USD | 13,460,000.00 USD | 273,920.00 USD | 96,980.00 USD | 60,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 5,510,000.00 USD | 5,510,000.00 USD | 39,860.00 USD | 4,490.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.28` | 14,160,000.00 USD | 14,160,000.00 USD | 428,160.00 USD | 103,490.00 USD | 170,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 100.93 USD | 13,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.29` | 5,570,000.00 USD | 5,570,000.00 USD | 37,550.00 USD | 11,780.00 USD | 18,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.30` | 14,720,000.00 USD | 14,720,000.00 USD | 199,810.00 USD | 97,780.00 USD | 262,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 5,680,000.00 USD | 5,680,000.00 USD | 70,620.00 USD | 13,670.00 USD | 24,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.32` | 15,390,000.00 USD | 15,390,000.00 USD | 271,660.00 USD | 59,310.00 USD | 337,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 5,720,000.00 USD | 5,720,000.00 USD | 17,610.00 USD | 6,000.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.34` | 15,720,000.00 USD | 15,720,000.00 USD | 204,260.00 USD | 53,150.00 USD | 70,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.35` | 5,830,000.00 USD | 5,830,000.00 USD | 61,720.00 USD | 8,000.00 USD | 38,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.36` | 16,140,000.00 USD | 16,140,000.00 USD | 247,120.00 USD | 73,430.00 USD | 97,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 5,920,000.00 USD | 5,920,000.00 USD | 54,310.00 USD | 20,710.00 USD | 19,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.38` | 16,670,000.00 USD | 16,670,000.00 USD | 383,530.00 USD | 55,400.00 USD | 94,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.39` | 5,970,000.00 USD | 5,970,000.00 USD | 31,180.00 USD | 2,720.00 USD | 15,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.40` | 17,070,000.00 USD | 17,070,000.00 USD | 234,760.00 USD | 42,520.00 USD | 124,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.41` | 6,000,000.00 USD | 6,000,000.00 USD | 24,200.00 USD | 0.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 440.06 USD | 13,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.42` | 17,350,000.00 USD | 17,350,000.00 USD | 176,920.00 USD | 19,780.00 USD | 84,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.43` | 6,040,000.00 USD | 6,040,000.00 USD | 18,750.00 USD | 4,030.00 USD | 16,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.44` | 17,470,000.00 USD | 17,470,000.00 USD | 41,250.00 USD | 19,420.00 USD | 56,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.45` | 6,050,000.00 USD | 6,050,000.00 USD | 1,360.00 USD | 0.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.46` | 17,580,000.00 USD | 17,580,000.00 USD | 60,020.00 USD | 29,830.00 USD | 19,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.47` | 6,050,000.00 USD | 6,050,000.00 USD | 2,380.00 USD | 5,690.00 USD | 192.20 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.48` | 17,650,000.00 USD | 17,650,000.00 USD | 12,180.00 USD | 27,840.00 USD | 25,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.49` | 6,100,000.00 USD | 6,100,000.00 USD | 31,340.00 USD | 572.85 USD | 14,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.50` | 17,850,000.00 USD | 17,850,000.00 USD | 89,460.00 USD | 33,210.00 USD | 83,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.51` | 6,120,000.00 USD | 6,120,000.00 USD | 12,280.00 USD | 3,160.00 USD | 124.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.52` | 18,040,000.00 USD | 18,040,000.00 USD | 102,150.00 USD | 29,320.00 USD | 51,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.53` | 6,170,000.00 USD | 6,170,000.00 USD | 35,250.00 USD | 9,400.00 USD | 5,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.54` | 18,250,000.00 USD | 18,250,000.00 USD | 192,090.00 USD | 25,090.00 USD | 930.52 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.55` | 6,190,000.00 USD | 6,190,000.00 USD | 7,860.00 USD | 7,800.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.56` | 18,360,000.00 USD | 18,360,000.00 USD | 88,510.00 USD | 5,260.00 USD | 13,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.57` | 6,210,000.00 USD | 6,210,000.00 USD | 5,780.00 USD | 4,390.00 USD | 7,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.58` | 18,440,000.00 USD | 18,440,000.00 USD | 35,340.00 USD | 14,530.00 USD | 27,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.59` | 6,220,000.00 USD | 6,220,000.00 USD | 5,320.00 USD | 3,060.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.60` | 18,500,000.00 USD | 18,500,000.00 USD | 38,740.00 USD | 5,460.00 USD | 18,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.61` | 6,290,000.00 USD | 6,290,000.00 USD | 29,510.00 USD | 4,570.00 USD | 28,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.62` | 18,590,000.00 USD | 18,590,000.00 USD | 70,470.00 USD | 1,540.00 USD | 17,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.63` | 6,310,000.00 USD | 6,310,000.00 USD | 17,350.00 USD | 4,370.00 USD | 4,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.64` | 18,660,000.00 USD | 18,660,000.00 USD | 35,210.00 USD | 17,650.00 USD | 19,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.65` | 6,330,000.00 USD | 6,330,000.00 USD | 11,050.00 USD | 5,210.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.66` | 18,740,000.00 USD | 18,740,000.00 USD | 37,340.00 USD | 21,280.00 USD | 18,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.67` | 6,360,000.00 USD | 6,360,000.00 USD | 11,920.00 USD | 3,480.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.68` | 18,860,000.00 USD | 18,860,000.00 USD | 68,230.00 USD | 20,310.00 USD | 34,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.69` | 6,390,000.00 USD | 6,390,000.00 USD | 21,130.00 USD | 5,660.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.70` | 18,990,000.00 USD | 18,990,000.00 USD | 77,860.00 USD | 12,990.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.71` | 6,420,000.00 USD | 6,420,000.00 USD | 11,360.00 USD | 9,310.00 USD | 8,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.72` | 19,090,000.00 USD | 19,090,000.00 USD | 70,300.00 USD | 6,920.00 USD | 26,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 14,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.74` | 19,140,000.00 USD | 19,140,000.00 USD | 21,230.00 USD | 7,200.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.76` | 19,240,000.00 USD | 19,240,000.00 USD | 35,520.00 USD | 12,480.00 USD | 52,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.78` | 19,320,000.00 USD | 19,320,000.00 USD | 65,390.00 USD | 10,300.00 USD | 5,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.79` | 240,270.00 USD | 254,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.80` | 19,380,000.00 USD | 19,380,000.00 USD | 18,630.00 USD | 28,440.00 USD | 10,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.82` | 19,610,000.00 USD | 19,610,000.00 USD | 121,860.00 USD | 27,860.00 USD | 86,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.84` | 19,640,000.00 USD | 19,640,000.00 USD | 9,730.00 USD | 7,850.00 USD | 14,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.86` | 19,780,000.00 USD | 19,780,000.00 USD | 58,130.00 USD | 2,210.00 USD | 71,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.88` | 19,810,000.00 USD | 19,810,000.00 USD | 7,170.00 USD | 8,710.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.90` | 19,900,000.00 USD | 19,900,000.00 USD | 55,970.00 USD | 19,700.00 USD | 14,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.92` | 19,950,000.00 USD | 19,950,000.00 USD | 27,710.00 USD | 10,810.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.94` | 298,060.00 USD | 552,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.94` | 20,070,000.00 USD | 20,070,000.00 USD | 69,320.00 USD | 11,150.00 USD | 39,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.96` | 20,110,000.00 USD | 20,110,000.00 USD | 29,800.00 USD | 1,360.00 USD | 11,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.98` | 20,140,000.00 USD | 20,140,000.00 USD | 840.10 USD | 4,150.00 USD | 18,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.00` | 20,140,000.00 USD | 20,140,000.00 USD | 0.00 USD | 6,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.02` | 20,170,000.00 USD | 20,170,000.00 USD | 16,100.00 USD | 3,650.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.04` | 20,180,000.00 USD | 20,180,000.00 USD | 1,080.00 USD | 0.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.06` | 20,200,000.00 USD | 20,200,000.00 USD | 0.00 USD | 3,480.00 USD | 17,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.08` | 20,230,000.00 USD | 20,230,000.00 USD | 23,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.10` | 568.25 USD | 552,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.12` | 486.53 USD | 553,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.21` | 3,230.00 USD | 556,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.35` | 2,650.00 USD | 559,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 559,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.71` | 218.91 USD | 560,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.96` | 1,920.00 USD | 562,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 568,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 11,670.00 USD | 580,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.54` | 39,980.00 USD | 620,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 632,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.66` | 58,320.00 USD | 691,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.69` | 296,760.00 USD | 987,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.93` | 505.74 USD | 988,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.95` | 1,050.00 USD | 989,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.04` | 801.53 USD | 990,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 991,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 992,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.82` | 1,460.00 USD | 993,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.03` | 444.15 USD | 994,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.89` | 40,010.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.12` | 15,820.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.21` | 280.46 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.80` | 4,110.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.84` | 243.44 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.23` | 2,530.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.26` | 328.75 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.38` | 20,000.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.29` | 115.79 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.34` | 264,920.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.36` | 186,130.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.76` | 2,310,000.00 USD | 0.00 USD | 900.15 USD | `-79.07%` | `510.00` |
| `Live` | `Long` | `1.81` | 2,310,000.00 USD | 0.00 USD | 7,430.00 USD | `-78.48%` | `4,091.48` |
| `Live` | `Long` | `1.82` | 2,300,000.00 USD | 0.00 USD | 202.23 USD | `-78.36%` | `110.81` |
| `Live` | `Long` | `1.85` | 2,300,000.00 USD | 0.00 USD | 129.85 USD | `-78.00%` | `70.00` |
| `Live` | `Long` | `1.90` | 2,300,000.00 USD | 0.00 USD | 1,920.00 USD | `-77.53%` | `1,010.81` |
| `Live` | `Long` | `1.94` | 2,300,000.00 USD | 0.00 USD | 212.85 USD | `-77.05%` | `110.00` |
| `Live` | `Long` | `2.00` | 2,300,000.00 USD | 0.00 USD | 159.60 USD | `-76.34%` | `80.00` |
| `Live` | `Long` | `2.04` | 2,300,000.00 USD | 0.00 USD | 110.52 USD | `-75.87%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,300,000.00 USD | 0.00 USD | 4,920.00 USD | `-75.51%` | `2,382.76` |
| `Live` | `Long` | `2.31` | 2,290,000.00 USD | 0.00 USD | 281.85 USD | `-72.55%` | `121.75` |
| `Live` | `Long` | `2.40` | 2,290,000.00 USD | 0.00 USD | 179.62 USD | `-71.60%` | `75.00` |
| `Live` | `Long` | `2.42` | 2,290,000.00 USD | 0.00 USD | 814.80 USD | `-71.24%` | `336.00` |
| `Live` | `Long` | `2.44` | 2,290,000.00 USD | 0.00 USD | 413.80 USD | `-71.12%` | `169.94` |
| `Live` | `Long` | `2.50` | 2,290,000.00 USD | 0.00 USD | 275.55 USD | `-70.29%` | `110.00` |
| `Live` | `Long` | `2.79` | 2,290,000.00 USD | 0.00 USD | 144.82 USD | `-66.97%` | `52.00` |
| `Live` | `Long` | `2.85` | 2,290,000.00 USD | 0.00 USD | 19,890.00 USD | `-66.26%` | `6,990.57` |
| `Live` | `Long` | `2.87` | 2,270,000.00 USD | 0.00 USD | 232.67 USD | `-66.03%` | `81.21` |
| `Live` | `Long` | `2.94` | 2,270,000.00 USD | 0.00 USD | 44,510.00 USD | `-65.20%` | `15,165.76` |
| `Live` | `Long` | `2.98` | 2,220,000.00 USD | 0.00 USD | 111.12 USD | `-64.72%` | `37.35` |
| `Live` | `Long` | `3.15` | 2,220,000.00 USD | 0.00 USD | 359.99 USD | `-62.59%` | `114.10` |
| `Live` | `Long` | `3.29` | 2,220,000.00 USD | 0.00 USD | 229.95 USD | `-61.04%` | `70.00` |
| `Live` | `Long` | `3.33` | 2,220,000.00 USD | 0.00 USD | 6,650.00 USD | `-60.57%` | `2,000.00` |
| `Live` | `Long` | `3.37` | 2,220,000.00 USD | 0.00 USD | 389.53 USD | `-60.10%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,220,000.00 USD | 0.00 USD | 151.88 USD | `-59.98%` | `45.00` |
| `Live` | `Long` | `3.46` | 2,220,000.00 USD | 0.00 USD | 1,310.00 USD | `-58.91%` | `377.71` |
| `Live` | `Long` | `3.50` | 2,210,000.00 USD | 0.00 USD | 570.75 USD | `-58.44%` | `162.84` |
| `Live` | `Long` | `3.56` | 2,210,000.00 USD | 0.00 USD | 891.25 USD | `-57.72%` | `250.00` |
| `Live` | `Long` | `3.58` | 2,210,000.00 USD | 0.00 USD | 120.55 USD | `-57.61%` | `33.72` |
| `Live` | `Long` | `3.67` | 2,210,000.00 USD | 0.00 USD | 109.95 USD | `-56.54%` | `30.00` |
| `Live` | `Long` | `3.75` | 2,210,000.00 USD | 0.00 USD | 1,500.00 USD | `-55.47%` | `400.00` |
| `Live` | `Long` | `3.90` | 2,210,000.00 USD | 0.00 USD | 131.73 USD | `-53.81%` | `33.82` |
| `Live` | `Long` | `3.98` | 2,210,000.00 USD | 0.00 USD | 254.04 USD | `-52.74%` | `63.75` |
| `Live` | `Long` | `4.03` | 2,210,000.00 USD | 0.00 USD | 402.70 USD | `-52.27%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,210,000.00 USD | 0.00 USD | 152.29 USD | `-52.03%` | `37.65` |
| `Live` | `Long` | `4.14` | 2,210,000.00 USD | 0.00 USD | 159.29 USD | `-50.85%` | `38.43` |
| `Live` | `Long` | `4.18` | 2,210,000.00 USD | 0.00 USD | 174.89 USD | `-50.37%` | `41.79` |
| `Live` | `Long` | `4.21` | 2,210,000.00 USD | 0.00 USD | 442.57 USD | `-50.02%` | `105.00` |
| `Live` | `Long` | `4.24` | 2,210,000.00 USD | 0.00 USD | 169.40 USD | `-49.78%` | `40.00` |
| `Live` | `Long` | `4.33` | 2,210,000.00 USD | 0.00 USD | 186.71 USD | `-48.59%` | `43.07` |
| `Live` | `Long` | `4.36` | 2,210,000.00 USD | 0.00 USD | 185.83 USD | `-48.36%` | `42.67` |
| `Live` | `Long` | `4.41` | 2,210,000.00 USD | 0.00 USD | 1,820.00 USD | `-47.76%` | `413.09` |
| `Live` | `Long` | `4.45` | 2,210,000.00 USD | 0.00 USD | 110.77 USD | `-47.29%` | `24.92` |
| `Live` | `Long` | `4.53` | 2,210,000.00 USD | 0.00 USD | 422.27 USD | `-46.34%` | `93.32` |
| `Live` | `Long` | `4.59` | 2,210,000.00 USD | 0.00 USD | 30,970.00 USD | `-45.51%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,180,000.00 USD | 0.00 USD | 486.93 USD | `-45.27%` | `105.51` |
| `Live` | `Long` | `4.62` | 2,180,000.00 USD | 0.00 USD | 2,680.00 USD | `-45.15%` | `579.06` |
| `Live` | `Long` | `4.66` | 2,170,000.00 USD | 0.00 USD | 105.11 USD | `-44.80%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,170,000.00 USD | 0.00 USD | 3,280.00 USD | `-44.68%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,170,000.00 USD | 0.00 USD | 1,490.00 USD | `-44.56%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,170,000.00 USD | 0.00 USD | 8,380.00 USD | `-44.44%` | `1,787.97` |
| `Live` | `Long` | `4.70` | 2,160,000.00 USD | 0.00 USD | 7,040.00 USD | `-44.32%` | `1,500.00` |
| `Live` | `Long` | `4.71` | 2,150,000.00 USD | 0.00 USD | 110.61 USD | `-44.09%` | `23.46` |
| `Live` | `Long` | `4.76` | 2,150,000.00 USD | 0.00 USD | 105.64 USD | `-43.49%` | `22.17` |
| `Live` | `Long` | `4.82` | 2,150,000.00 USD | 0.00 USD | 2,890.00 USD | `-42.90%` | `600.00` |
| `Live` | `Long` | `4.83` | 2,150,000.00 USD | 0.00 USD | 467.01 USD | `-42.66%` | `96.59` |
| `Live` | `Long` | `4.86` | 2,150,000.00 USD | 0.00 USD | 15,950.00 USD | `-42.43%` | `3,286.00` |
| `Live` | `Long` | `4.89` | 2,130,000.00 USD | 0.00 USD | 146.85 USD | `-41.95%` | `30.00` |
| `Live` | `Long` | `4.91` | 2,130,000.00 USD | 0.00 USD | 527.19 USD | `-41.83%` | `107.48` |
| `Live` | `Long` | `4.92` | 2,130,000.00 USD | 0.00 USD | 1,740.00 USD | `-41.72%` | `354.73` |
| `Live` | `Long` | `4.93` | 2,130,000.00 USD | 0.00 USD | 244.87 USD | `-41.48%` | `49.62` |
| `Live` | `Long` | `4.96` | 2,130,000.00 USD | 0.00 USD | 945.36 USD | `-41.24%` | `190.79` |
| `Live` | `Long` | `4.96` | 2,130,000.00 USD | 0.00 USD | 5,160.00 USD | `-41.12%` | `1,039.23` |
| `Live` | `Long` | `4.97` | 2,120,000.00 USD | 0.00 USD | 282.23 USD | `-41.00%` | `56.73` |
| `Live` | `Long` | `5.01` | 2,120,000.00 USD | 0.00 USD | 56,390.00 USD | `-40.53%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,070,000.00 USD | 0.00 USD | 167.78 USD | `-40.41%` | `33.39` |
| `Live` | `Long` | `5.04` | 2,070,000.00 USD | 0.00 USD | 314.59 USD | `-40.29%` | `62.48` |
| `Live` | `Long` | `5.05` | 2,070,000.00 USD | 0.00 USD | 504.74 USD | `-40.06%` | `99.85` |
| `Live` | `Long` | `5.08` | 2,070,000.00 USD | 0.00 USD | 318.46 USD | `-39.82%` | `62.75` |
| `Live` | `Long` | `5.11` | 2,070,000.00 USD | 0.00 USD | 118.44 USD | `-39.46%` | `23.20` |
| `Live` | `Long` | `5.12` | 2,070,000.00 USD | 0.00 USD | 250.20 USD | `-39.23%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,070,000.00 USD | 0.00 USD | 5,800.00 USD | `-39.11%` | `1,130.13` |
| `Live` | `Long` | `5.14` | 2,060,000.00 USD | 0.00 USD | 2,570.00 USD | `-38.99%` | `500.00` |
| `Live` | `Long` | `5.17` | 2,060,000.00 USD | 0.00 USD | 2,510.00 USD | `-38.75%` | `485.77` |
| `Live` | `Long` | `5.17` | 2,060,000.00 USD | 0.00 USD | 1,620.00 USD | `-38.63%` | `312.94` |
| `Live` | `Long` | `5.18` | 2,050,000.00 USD | 0.00 USD | 150.57 USD | `-38.51%` | `29.04` |
| `Live` | `Long` | `5.21` | 2,050,000.00 USD | 0.00 USD | 2,250.00 USD | `-38.16%` | `431.24` |
| `Live` | `Long` | `5.25` | 2,050,000.00 USD | 0.00 USD | 1,050.00 USD | `-37.68%` | `200.00` |
| `Live` | `Long` | `5.28` | 2,050,000.00 USD | 0.00 USD | 160,550.00 USD | `-37.45%` | `30,435.20` |
| `Live` | `Long` | `5.29` | 1,890,000.00 USD | 0.00 USD | 640.70 USD | `-37.33%` | `121.23` |
| `Live` | `Long` | `5.30` | 1,890,000.00 USD | 0.00 USD | 509.55 USD | `-37.09%` | `96.05` |
| `Live` | `Long` | `5.32` | 1,890,000.00 USD | 0.00 USD | 232.85 USD | `-36.97%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,890,000.00 USD | 0.00 USD | 716.11 USD | `-36.85%` | `134.48` |
| `Live` | `Long` | `5.39` | 1,890,000.00 USD | 0.00 USD | 660.46 USD | `-36.02%` | `122.42` |
| `Live` | `Long` | `5.42` | 1,890,000.00 USD | 0.00 USD | 21,630.00 USD | `-35.79%` | `3,993.69` |
| `Live` | `Long` | `5.42` | 1,870,000.00 USD | 0.00 USD | 160,400.00 USD | `-35.67%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,700,000.00 USD | 0.00 USD | 1,360.00 USD | `-35.55%` | `250.00` |
| `Live` | `Long` | `5.46` | 1,700,000.00 USD | 0.00 USD | 264.72 USD | `-35.19%` | `48.44` |
| `Live` | `Long` | `5.47` | 1,700,000.00 USD | 0.00 USD | 1,320.00 USD | `-35.07%` | `240.95` |
| `Live` | `Long` | `5.49` | 1,700,000.00 USD | 0.00 USD | 354.06 USD | `-34.96%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,700,000.00 USD | 0.00 USD | 20,330.00 USD | `-34.84%` | `3,700.40` |
| `Live` | `Long` | `5.51` | 1,680,000.00 USD | 0.00 USD | 367.41 USD | `-34.60%` | `66.62` |
| `Live` | `Long` | `5.54` | 1,680,000.00 USD | 0.00 USD | 121.38 USD | `-34.36%` | `21.93` |
| `Live` | `Long` | `5.54` | 1,680,000.00 USD | 0.00 USD | 2,760.00 USD | `-34.24%` | `497.70` |
| `Live` | `Long` | `5.57` | 1,680,000.00 USD | 0.00 USD | 967.98 USD | `-34.01%` | `173.94` |
| `Live` | `Long` | `5.58` | 1,680,000.00 USD | 0.00 USD | 63,260.00 USD | `-33.89%` | `11,347.58` |
| `Live` | `Long` | `5.59` | 1,610,000.00 USD | 0.00 USD | 34,430.00 USD | `-33.65%` | `6,153.60` |
| `Live` | `Long` | `5.63` | 1,580,000.00 USD | 0.00 USD | 468.55 USD | `-33.18%` | `83.15` |
| `Live` | `Long` | `5.68` | 1,580,000.00 USD | 0.00 USD | 274.13 USD | `-32.58%` | `48.22` |
| `Live` | `Long` | `5.72` | 1,580,000.00 USD | 0.00 USD | 2,390.00 USD | `-32.11%` | `417.17` |
| `Live` | `Long` | `5.74` | 1,580,000.00 USD | 0.00 USD | 238.86 USD | `-31.99%` | `41.65` |
| `Live` | `Long` | `5.75` | 1,580,000.00 USD | 0.00 USD | 125.70 USD | `-31.87%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,580,000.00 USD | 0.00 USD | 3,190.00 USD | `-31.75%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,570,000.00 USD | 0.00 USD | 10,850.00 USD | `-31.64%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,560,000.00 USD | 0.00 USD | 801.40 USD | `-31.52%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,560,000.00 USD | 0.00 USD | 2,890.00 USD | `-31.40%` | `500.00` |
| `Live` | `Long` | `5.79` | 1,560,000.00 USD | 0.00 USD | 736.72 USD | `-31.28%` | `127.13` |
| `Live` | `Long` | `5.80` | 1,560,000.00 USD | 0.00 USD | 58,750.00 USD | `-31.16%` | `10,120.00` |
| `Live` | `Long` | `5.82` | 1,500,000.00 USD | 0.00 USD | 106.65 USD | `-31.04%` | `18.34` |
| `Live` | `Long` | `5.83` | 1,500,000.00 USD | 0.00 USD | 145.88 USD | `-30.81%` | `25.00` |
| `Live` | `Long` | `5.84` | 1,500,000.00 USD | 0.00 USD | 561.53 USD | `-30.69%` | `96.07` |
| `Live` | `Long` | `5.86` | 1,500,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.57%` | `360.33` |
| `Live` | `Long` | `5.88` | 1,500,000.00 USD | 0.00 USD | 128.94 USD | `-30.21%` | `21.91` |
| `Live` | `Long` | `5.89` | 1,500,000.00 USD | 0.00 USD | 984.70 USD | `-30.09%` | `167.04` |
| `Live` | `Long` | `5.91` | 1,490,000.00 USD | 0.00 USD | 399.18 USD | `-29.98%` | `67.60` |
| `Live` | `Long` | `5.93` | 1,490,000.00 USD | 0.00 USD | 147.19 USD | `-29.62%` | `24.80` |
| `Live` | `Long` | `5.96` | 1,490,000.00 USD | 0.00 USD | 11,720.00 USD | `-29.38%` | `1,968.19` |
| `Live` | `Long` | `5.97` | 1,480,000.00 USD | 0.00 USD | 585.97 USD | `-29.15%` | `98.07` |
| `Live` | `Long` | `5.99` | 1,480,000.00 USD | 0.00 USD | 447.98 USD | `-29.03%` | `74.85` |
| `Live` | `Long` | `6.00` | 1,480,000.00 USD | 0.00 USD | 341.56 USD | `-28.79%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,480,000.00 USD | 0.00 USD | 446.85 USD | `-28.67%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,480,000.00 USD | 0.00 USD | 432.77 USD | `-28.43%` | `71.71` |
| `Live` | `Long` | `6.04` | 1,480,000.00 USD | 0.00 USD | 105.61 USD | `-28.32%` | `17.47` |
| `Live` | `Long` | `6.05` | 1,480,000.00 USD | 0.00 USD | 1,310.00 USD | `-28.20%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,480,000.00 USD | 0.00 USD | 1,680.00 USD | `-28.08%` | `277.31` |
| `Live` | `Long` | `6.08` | 1,480,000.00 USD | 0.00 USD | 1,690.00 USD | `-27.96%` | `278.94` |
| `Live` | `Long` | `6.08` | 1,480,000.00 USD | 0.00 USD | 405.14 USD | `-27.84%` | `66.58` |
| `Live` | `Long` | `6.09` | 1,470,000.00 USD | 0.00 USD | 3,130.00 USD | `-27.72%` | `512.81` |
| `Live` | `Long` | `6.11` | 1,470,000.00 USD | 0.00 USD | 1,090.00 USD | `-27.60%` | `178.97` |
| `Live` | `Long` | `6.12` | 1,470,000.00 USD | 0.00 USD | 1,140.00 USD | `-27.49%` | `185.96` |
| `Live` | `Long` | `6.12` | 1,470,000.00 USD | 0.00 USD | 137.02 USD | `-27.37%` | `22.37` |
| `Live` | `Long` | `6.13` | 1,470,000.00 USD | 0.00 USD | 2,030.00 USD | `-27.25%` | `330.65` |
| `Live` | `Long` | `6.14` | 1,470,000.00 USD | 0.00 USD | 238.61 USD | `-27.13%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,470,000.00 USD | 0.00 USD | 4,390.00 USD | `-27.01%` | `713.75` |
| `Live` | `Long` | `6.17` | 1,460,000.00 USD | 0.00 USD | 187.29 USD | `-26.89%` | `30.38` |
| `Live` | `Long` | `6.17` | 1,460,000.00 USD | 0.00 USD | 104.36 USD | `-26.77%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,460,000.00 USD | 0.00 USD | 310.25 USD | `-26.42%` | `50.00` |
| `Live` | `Long` | `6.25` | 1,460,000.00 USD | 0.00 USD | 3,390.00 USD | `-25.83%` | `541.96` |
| `Live` | `Long` | `6.28` | 1,460,000.00 USD | 0.00 USD | 2,510.00 USD | `-25.59%` | `400.00` |
| `Live` | `Long` | `6.32` | 1,460,000.00 USD | 0.00 USD | 277.04 USD | `-25.11%` | `43.87` |
| `Live` | `Long` | `6.36` | 1,460,000.00 USD | 0.00 USD | 5,900.00 USD | `-24.64%` | `928.47` |
| `Live` | `Long` | `6.37` | 1,450,000.00 USD | 0.00 USD | 284,770.00 USD | `-24.52%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 1,170,000.00 USD | 0.00 USD | 6,590.00 USD | `-24.40%` | `1,033.48` |
| `Live` | `Long` | `6.38` | 1,160,000.00 USD | 0.00 USD | 6,430.00 USD | `-24.28%` | `1,006.81` |
| `Live` | `Long` | `6.42` | 1,150,000.00 USD | 0.00 USD | 306.32 USD | `-23.93%` | `47.75` |
| `Live` | `Long` | `6.43` | 1,150,000.00 USD | 0.00 USD | 367,520.00 USD | `-23.69%` | `57,112.29` |
| `Live` | `Long` | `6.46` | 784,370.00 USD | 0.00 USD | 1,050.00 USD | `-23.34%` | `162.75` |
| `Live` | `Long` | `6.54` | 783,320.00 USD | 0.00 USD | 3,620.00 USD | `-22.50%` | `554.55` |
| `Live` | `Long` | `6.54` | 779,690.00 USD | 0.00 USD | 8,970.00 USD | `-22.39%` | `1,370.89` |
| `Live` | `Long` | `6.58` | 770,720.00 USD | 0.00 USD | 1,770.00 USD | `-21.91%` | `269.14` |
| `Live` | `Long` | `6.59` | 768,950.00 USD | 0.00 USD | 1,100.00 USD | `-21.79%` | `166.55` |
| `Live` | `Long` | `6.62` | 767,850.00 USD | 0.00 USD | 2,110.00 USD | `-21.56%` | `318.57` |
| `Live` | `Long` | `6.67` | 765,740.00 USD | 0.00 USD | 1,640.00 USD | `-20.84%` | `245.42` |
| `Live` | `Long` | `6.70` | 764,100.00 USD | 0.00 USD | 506.54 USD | `-20.61%` | `75.66` |
| `Live` | `Long` | `6.71` | 763,600.00 USD | 0.00 USD | 16,610.00 USD | `-20.49%` | `2,477.79` |
| `Live` | `Long` | `6.75` | 746,980.00 USD | 0.00 USD | 1,330.00 USD | `-20.01%` | `196.95` |
| `Live` | `Long` | `6.78` | 745,660.00 USD | 0.00 USD | 6,780.00 USD | `-19.66%` | `1,000.00` |
| `Live` | `Long` | `6.79` | 738,880.00 USD | 0.00 USD | 16,960.00 USD | `-19.54%` | `2,500.00` |
| `Live` | `Long` | `6.79` | 721,920.00 USD | 0.00 USD | 4,930.00 USD | `-19.42%` | `726.24` |
| `Live` | `Long` | `6.80` | 716,980.00 USD | 0.00 USD | 1,500.00 USD | `-19.30%` | `220.95` |
| `Live` | `Long` | `6.82` | 715,480.00 USD | 0.00 USD | 2,670.00 USD | `-19.18%` | `391.11` |
| `Live` | `Long` | `6.83` | 712,810.00 USD | 0.00 USD | 158.14 USD | `-19.07%` | `23.17` |
| `Live` | `Long` | `6.83` | 712,660.00 USD | 0.00 USD | 4,410.00 USD | `-18.95%` | `644.73` |
| `Live` | `Long` | `6.86` | 708,250.00 USD | 0.00 USD | 19,810.00 USD | `-18.71%` | `2,889.24` |
| `Live` | `Long` | `6.87` | 688,440.00 USD | 0.00 USD | 3,340.00 USD | `-18.59%` | `486.46` |
| `Live` | `Long` | `6.88` | 685,100.00 USD | 0.00 USD | 1,580.00 USD | `-18.35%` | `229.18` |
| `Live` | `Long` | `6.89` | 683,530.00 USD | 0.00 USD | 5,250.00 USD | `-18.24%` | `761.63` |
| `Live` | `Long` | `6.91` | 678,270.00 USD | 0.00 USD | 269.30 USD | `-18.12%` | `39.00` |
| `Live` | `Long` | `6.92` | 678,010.00 USD | 0.00 USD | 1,840.00 USD | `-17.88%` | `265.15` |
| `Live` | `Long` | `6.95` | 676,170.00 USD | 0.00 USD | 3,760.00 USD | `-17.64%` | `541.68` |
| `Live` | `Long` | `6.96` | 672,410.00 USD | 0.00 USD | 3,480.00 USD | `-17.52%` | `500.00` |
| `Live` | `Long` | `6.96` | 668,930.00 USD | 0.00 USD | 636.74 USD | `-17.41%` | `91.42` |
| `Live` | `Long` | `6.97` | 668,290.00 USD | 0.00 USD | 961.64 USD | `-17.29%` | `137.87` |
| `Live` | `Long` | `6.99` | 667,330.00 USD | 0.00 USD | 1,100.00 USD | `-17.17%` | `157.09` |
| `Live` | `Long` | `7.00` | 666,230.00 USD | 0.00 USD | 746.58 USD | `-17.05%` | `106.73` |
| `Live` | `Long` | `7.00` | 665,490.00 USD | 0.00 USD | 20,860.00 USD | `-16.93%` | `2,978.11` |
| `Live` | `Long` | `7.01` | 644,630.00 USD | 0.00 USD | 281.86 USD | `-16.81%` | `40.18` |
| `Live` | `Long` | `7.04` | 644,340.00 USD | 0.00 USD | 704.50 USD | `-16.46%` | `100.00` |
| `Live` | `Long` | `7.05` | 643,640.00 USD | 0.00 USD | 354.23 USD | `-16.34%` | `50.21` |
| `Live` | `Long` | `7.07` | 643,290.00 USD | 0.00 USD | 9,860.00 USD | `-16.22%` | `1,395.39` |
| `Live` | `Long` | `7.08` | 633,430.00 USD | 0.00 USD | 6,700.00 USD | `-16.10%` | `947.44` |
| `Live` | `Long` | `7.08` | 626,720.00 USD | 0.00 USD | 1,420.00 USD | `-15.98%` | `201.02` |
| `Live` | `Long` | `7.11` | 625,300.00 USD | 0.00 USD | 28,230.00 USD | `-15.75%` | `3,972.61` |
| `Live` | `Long` | `7.12` | 597,070.00 USD | 0.00 USD | 379.66 USD | `-15.63%` | `53.36` |
| `Live` | `Long` | `7.13` | 596,690.00 USD | 0.00 USD | 2,300.00 USD | `-15.39%` | `322.72` |
| `Live` | `Long` | `7.14` | 594,390.00 USD | 0.00 USD | 20,270.00 USD | `-15.27%` | `2,837.00` |
| `Live` | `Long` | `7.16` | 574,120.00 USD | 0.00 USD | 4,800.00 USD | `-15.15%` | `670.32` |
| `Live` | `Long` | `7.17` | 569,330.00 USD | 0.00 USD | 215.59 USD | `-15.03%` | `30.09` |
| `Live` | `Long` | `7.17` | 569,110.00 USD | 0.00 USD | 28,700.00 USD | `-14.92%` | `4,000.00` |
| `Live` | `Long` | `7.18` | 540,410.00 USD | 0.00 USD | 1,440.00 USD | `-14.80%` | `200.00` |
| `Live` | `Long` | `7.21` | 538,970.00 USD | 0.00 USD | 9,400.00 USD | `-14.56%` | `1,303.97` |
| `Live` | `Long` | `7.21` | 529,580.00 USD | 0.00 USD | 791.63 USD | `-14.44%` | `109.72` |
| `Live` | `Long` | `7.24` | 528,790.00 USD | 0.00 USD | 179.65 USD | `-14.20%` | `24.83` |
| `Live` | `Long` | `7.25` | 528,610.00 USD | 0.00 USD | 185.83 USD | `-14.09%` | `25.65` |
| `Live` | `Long` | `7.26` | 528,420.00 USD | 0.00 USD | 419.41 USD | `-13.85%` | `57.73` |
| `Live` | `Long` | `7.28` | 528,000.00 USD | 0.00 USD | 243.64 USD | `-13.73%` | `33.49` |
| `Live` | `Long` | `7.29` | 527,760.00 USD | 0.00 USD | 36,420.00 USD | `-13.61%` | `5,000.00` |
| `Live` | `Long` | `7.29` | 491,330.00 USD | 0.00 USD | 1,680.00 USD | `-13.49%` | `230.97` |
| `Live` | `Long` | `7.33` | 489,650.00 USD | 0.00 USD | 4,910.00 USD | `-13.14%` | `669.93` |
| `Live` | `Long` | `7.34` | 484,740.00 USD | 0.00 USD | 4,370.00 USD | `-12.90%` | `594.84` |
| `Live` | `Long` | `7.37` | 480,370.00 USD | 0.00 USD | 5,720.00 USD | `-12.66%` | `776.95` |
| `Live` | `Long` | `7.38` | 474,650.00 USD | 0.00 USD | 5,020.00 USD | `-12.54%` | `680.40` |
| `Live` | `Long` | `7.39` | 469,630.00 USD | 0.00 USD | 1,550.00 USD | `-12.31%` | `210.17` |
| `Live` | `Long` | `7.41` | 468,080.00 USD | 0.00 USD | 854.02 USD | `-12.19%` | `115.33` |
| `Live` | `Long` | `7.42` | 467,220.00 USD | 0.00 USD | 2,950.00 USD | `-11.95%` | `397.34` |
| `Live` | `Long` | `7.43` | 464,270.00 USD | 0.00 USD | 19,480.00 USD | `-11.83%` | `2,620.00` |
| `Live` | `Long` | `7.45` | 444,790.00 USD | 0.00 USD | 210.99 USD | `-11.71%` | `28.34` |
| `Live` | `Long` | `7.46` | 444,580.00 USD | 0.00 USD | 5,630.00 USD | `-11.48%` | `754.36` |
| `Live` | `Long` | `7.47` | 438,950.00 USD | 0.00 USD | 2,740.00 USD | `-11.36%` | `367.22` |
| `Live` | `Long` | `7.50` | 436,210.00 USD | 0.00 USD | 962.81 USD | `-11.12%` | `128.46` |
| `Live` | `Long` | `7.50` | 435,240.00 USD | 0.00 USD | 421.78 USD | `-11.00%` | `56.20` |
| `Live` | `Long` | `7.54` | 434,820.00 USD | 0.00 USD | 5,720.00 USD | `-10.65%` | `759.01` |
| `Live` | `Long` | `7.55` | 429,100.00 USD | 0.00 USD | 572.67 USD | `-10.41%` | `75.80` |
| `Live` | `Long` | `7.57` | 428,530.00 USD | 0.00 USD | 25,060.00 USD | `-10.29%` | `3,312.23` |
| `Live` | `Long` | `7.58` | 403,470.00 USD | 0.00 USD | 1,850.00 USD | `-10.17%` | `244.02` |
| `Live` | `Long` | `7.59` | 401,620.00 USD | 0.00 USD | 24,760.00 USD | `-9.94%` | `3,260.14` |
| `Live` | `Long` | `7.61` | 376,860.00 USD | 0.00 USD | 1,520.00 USD | `-9.82%` | `199.85` |
| `Live` | `Long` | `7.62` | 375,340.00 USD | 0.00 USD | 787.51 USD | `-9.58%` | `103.28` |
| `Live` | `Long` | `7.63` | 374,560.00 USD | 0.00 USD | 378.93 USD | `-9.46%` | `49.63` |
| `Live` | `Long` | `7.66` | 374,180.00 USD | 0.00 USD | 1,410.00 USD | `-9.22%` | `184.81` |
| `Live` | `Long` | `7.67` | 372,760.00 USD | 0.00 USD | 1,740.00 USD | `-9.10%` | `226.45` |
| `Live` | `Long` | `7.67` | 371,030.00 USD | 0.00 USD | 140.45 USD | `-8.99%` | `18.30` |
| `Live` | `Long` | `7.68` | 370,890.00 USD | 0.00 USD | 1,120.00 USD | `-8.87%` | `145.25` |
| `Live` | `Long` | `7.70` | 369,770.00 USD | 0.00 USD | 1,460.00 USD | `-8.75%` | `190.36` |
| `Live` | `Long` | `7.76` | 368,300.00 USD | 0.00 USD | 455.73 USD | `-7.92%` | `58.69` |
| `Live` | `Long` | `7.78` | 367,850.00 USD | 0.00 USD | 695.32 USD | `-7.80%` | `89.43` |
| `Live` | `Long` | `7.79` | 367,150.00 USD | 0.00 USD | 2,870.00 USD | `-7.68%` | `368.38` |
| `Live` | `Long` | `7.79` | 364,290.00 USD | 0.00 USD | 12,800.00 USD | `-7.56%` | `1,642.37` |
| `Live` | `Long` | `7.82` | 351,480.00 USD | 0.00 USD | 3,720.00 USD | `-7.33%` | `475.43` |
| `Live` | `Long` | `7.84` | 347,770.00 USD | 0.00 USD | 24,340.00 USD | `-6.97%` | `3,102.56` |
| `Live` | `Long` | `7.88` | 323,430.00 USD | 0.00 USD | 555.19 USD | `-6.61%` | `70.50` |
| `Live` | `Long` | `7.91` | 322,870.00 USD | 0.00 USD | 505.13 USD | `-6.26%` | `63.90` |
| `Live` | `Long` | `7.92` | 322,370.00 USD | 0.00 USD | 9,330.00 USD | `-6.14%` | `1,179.30` |
| `Live` | `Long` | `7.93` | 313,030.00 USD | 0.00 USD | 16,340.00 USD | `-5.90%` | `2,059.56` |
| `Live` | `Long` | `7.95` | 296,690.00 USD | 0.00 USD | 127,110.00 USD | `-5.78%` | `15,999.24` |
| `Live` | `Long` | `7.96` | 169,580.00 USD | 0.00 USD | 2,180.00 USD | `-5.67%` | `273.47` |
| `Live` | `Long` | `7.96` | 167,400.00 USD | 0.00 USD | 4,520.00 USD | `-5.55%` | `567.62` |
| `Live` | `Long` | `7.97` | 162,880.00 USD | 0.00 USD | 1,580.00 USD | `-5.43%` | `198.26` |
| `Live` | `Long` | `7.99` | 161,300.00 USD | 0.00 USD | 8,100.00 USD | `-5.31%` | `1,013.93` |
| `Live` | `Long` | `8.00` | 153,200.00 USD | 0.00 USD | 2,560.00 USD | `-5.19%` | `320.65` |
| `Live` | `Long` | `8.01` | 150,640.00 USD | 0.00 USD | 284.42 USD | `-5.07%` | `35.53` |
| `Live` | `Long` | `8.02` | 150,360.00 USD | 0.00 USD | 1,880.00 USD | `-4.95%` | `234.69` |
| `Live` | `Long` | `8.03` | 148,470.00 USD | 0.00 USD | 1,070.00 USD | `-4.84%` | `133.32` |
| `Live` | `Long` | `8.04` | 147,400.00 USD | 0.00 USD | 87,460.00 USD | `-4.72%` | `10,884.58` |
| `Live` | `Long` | `8.04` | 59,950.00 USD | 0.00 USD | 10,010.00 USD | `-4.60%` | `1,243.91` |
| `Live` | `Long` | `8.05` | 49,940.00 USD | 0.00 USD | 1,230.00 USD | `-4.48%` | `152.49` |
| `Live` | `Long` | `8.07` | 48,710.00 USD | 0.00 USD | 232.96 USD | `-4.24%` | `28.85` |
| `Live` | `Long` | `8.09` | 48,480.00 USD | 0.00 USD | 3,400.00 USD | `-4.12%` | `420.79` |
| `Live` | `Long` | `8.10` | 45,080.00 USD | 0.00 USD | 2,040.00 USD | `-4.01%` | `251.72` |
| `Live` | `Long` | `8.11` | 43,040.00 USD | 0.00 USD | 7,100.00 USD | `-3.89%` | `876.44` |
| `Live` | `Long` | `8.12` | 35,940.00 USD | 0.00 USD | 241.26 USD | `-3.77%` | `29.73` |
| `Live` | `Long` | `8.12` | 35,690.00 USD | 0.00 USD | 843.86 USD | `-3.65%` | `103.86` |
| `Live` | `Long` | `8.13` | 34,850.00 USD | 0.00 USD | 855.64 USD | `-3.53%` | `105.18` |
| `Live` | `Long` | `8.16` | 33,990.00 USD | 0.00 USD | 11,540.00 USD | `-3.18%` | `1,412.95` |
| `Live` | `Long` | `8.20` | 22,460.00 USD | 0.00 USD | 8,590.00 USD | `-2.82%` | `1,048.60` |
| `Live` | `Long` | `8.21` | 13,860.00 USD | 0.00 USD | 1,910.00 USD | `-2.70%` | `232.19` |
| `Live` | `Long` | `8.21` | 11,960.00 USD | 0.00 USD | 147.87 USD | `-2.58%` | `18.00` |
| `Live` | `Long` | `8.22` | 11,810.00 USD | 0.00 USD | 2,100.00 USD | `-2.46%` | `255.16` |
| `Live` | `Long` | `8.26` | 9,710.00 USD | 0.00 USD | 9,710.00 USD | `-2.11%` | `1,176.61` |
| `Live` | `Short` | `8.46` | 445.41 USD | 445.41 USD | 0.00 USD | `+0.26%` | `52.68` |
| `Live` | `Short` | `8.46` | 724.75 USD | 279.34 USD | 0.00 USD | `+0.38%` | `33.00` |
| `Live` | `Short` | `8.47` | 1,180.00 USD | 456.29 USD | 0.00 USD | `+0.50%` | `53.84` |
| `Live` | `Short` | `8.48` | 3,030.00 USD | 1,850.00 USD | 0.00 USD | `+0.62%` | `217.45` |
| `Live` | `Short` | `8.69` | 4,970.00 USD | 1,950.00 USD | 0.00 USD | `+2.99%` | `224.13` |
| `Live` | `Short` | `8.76` | 5,350.00 USD | 373.93 USD | 0.00 USD | `+3.82%` | `42.71` |
| `Live` | `Short` | `8.82` | 11,350.00 USD | 6,000.00 USD | 0.00 USD | `+4.65%` | `680.16` |
| `Live` | `Short` | `8.91` | 11,480.00 USD | 126.41 USD | 0.00 USD | `+5.72%` | `14.18` |
| `Live` | `Short` | `9.21` | 13,340.00 USD | 1,870.00 USD | 0.00 USD | `+9.28%` | `202.76` |
| `Live` | `Short` | `9.29` | 13,440.00 USD | 100.93 USD | 0.00 USD | `+10.11%` | `10.87` |
| `Live` | `Short` | `9.41` | 13,880.00 USD | 440.06 USD | 0.00 USD | `+11.65%` | `46.74` |
| `Live` | `Short` | `9.73` | 14,080.00 USD | 192.95 USD | 0.00 USD | `+15.44%` | `19.82` |
| `Live` | `Short` | `9.79` | 254,340.00 USD | 240,270.00 USD | 0.00 USD | `+16.15%` | `24,529.43` |
| `Live` | `Short` | `9.94` | 552,400.00 USD | 298,060.00 USD | 0.00 USD | `+17.81%` | `30,000.94` |
| `Live` | `Short` | `10.10` | 552,970.00 USD | 568.25 USD | 0.00 USD | `+19.71%` | `56.29` |
| `Live` | `Short` | `10.12` | 553,460.00 USD | 486.53 USD | 0.00 USD | `+19.95%` | `48.10` |
| `Live` | `Short` | `10.21` | 556,690.00 USD | 3,230.00 USD | 0.00 USD | `+21.13%` | `316.22` |
| `Live` | `Short` | `10.35` | 559,340.00 USD | 2,650.00 USD | 0.00 USD | `+22.68%` | `256.58` |
| `Live` | `Short` | `10.56` | 559,870.00 USD | 523.81 USD | 0.00 USD | `+25.28%` | `49.58` |
| `Live` | `Short` | `10.71` | 560,080.00 USD | 218.91 USD | 0.00 USD | `+27.06%` | `20.43` |
| `Live` | `Short` | `10.96` | 562,000.00 USD | 1,920.00 USD | 0.00 USD | `+30.03%` | `174.67` |
| `Live` | `Short` | `11.01` | 568,970.00 USD | 6,970.00 USD | 0.00 USD | `+30.50%` | `633.00` |
| `Live` | `Short` | `11.27` | 580,640.00 USD | 11,670.00 USD | 0.00 USD | `+33.59%` | `1,035.87` |
| `Live` | `Short` | `11.54` | 620,610.00 USD | 39,980.00 USD | 0.00 USD | `+36.91%` | `3,462.73` |
| `Live` | `Short` | `11.62` | 632,750.00 USD | 12,140.00 USD | 0.00 USD | `+37.85%` | `1,043.90` |
| `Live` | `Short` | `11.66` | 691,070.00 USD | 58,320.00 USD | 0.00 USD | `+38.33%` | `5,000.00` |
| `Live` | `Short` | `11.69` | 987,840.00 USD | 296,760.00 USD | 0.00 USD | `+38.57%` | `25,397.02` |
| `Live` | `Short` | `11.93` | 988,340.00 USD | 505.74 USD | 0.00 USD | `+41.41%` | `42.41` |
| `Live` | `Short` | `11.95` | 989,390.00 USD | 1,050.00 USD | 0.00 USD | `+41.65%` | `87.54` |
| `Live` | `Short` | `12.04` | 990,190.00 USD | 801.53 USD | 0.00 USD | `+42.72%` | `66.60` |
| `Live` | `Short` | `12.30` | 991,920.00 USD | 1,730.00 USD | 0.00 USD | `+45.92%` | `140.71` |
| `Live` | `Short` | `12.40` | 992,270.00 USD | 343.62 USD | 0.00 USD | `+47.10%` | `27.70` |
| `Live` | `Short` | `12.82` | 993,720.00 USD | 1,460.00 USD | 0.00 USD | `+52.08%` | `113.77` |
| `Live` | `Short` | `13.03` | 994,170.00 USD | 444.15 USD | 0.00 USD | `+54.46%` | `34.10` |
| `Live` | `Short` | `13.20` | 1,080,000.00 USD | 87,940.00 USD | 0.00 USD | `+56.47%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 1,090,000.00 USD | 3,810.00 USD | 0.00 USD | `+57.66%` | `286.56` |
| `Live` | `Short` | `13.46` | 1,090,000.00 USD | 430.34 USD | 0.00 USD | `+59.67%` | `31.96` |
| `Live` | `Short` | `13.69` | 1,090,000.00 USD | 172.29 USD | 0.00 USD | `+62.28%` | `12.59` |
| `Live` | `Short` | `13.89` | 1,130,000.00 USD | 40,010.00 USD | 0.00 USD | `+64.77%` | `2,879.71` |
| `Live` | `Short` | `14.12` | 1,140,000.00 USD | 15,820.00 USD | 0.00 USD | `+67.50%` | `1,120.14` |
| `Live` | `Short` | `14.21` | 1,140,000.00 USD | 280.46 USD | 0.00 USD | `+68.57%` | `19.73` |
| `Live` | `Short` | `14.66` | 1,140,000.00 USD | 823.29 USD | 0.00 USD | `+73.90%` | `56.14` |
| `Live` | `Short` | `14.80` | 1,150,000.00 USD | 4,110.00 USD | 0.00 USD | `+75.56%` | `277.54` |
| `Live` | `Short` | `14.84` | 1,150,000.00 USD | 243.44 USD | 0.00 USD | `+75.92%` | `16.41` |
| `Live` | `Short` | `15.23` | 1,150,000.00 USD | 2,530.00 USD | 0.00 USD | `+80.66%` | `166.16` |
| `Live` | `Short` | `15.26` | 1,150,000.00 USD | 328.75 USD | 0.00 USD | `+80.90%` | `21.55` |
| `Live` | `Short` | `15.29` | 1,150,000.00 USD | 229.43 USD | 0.00 USD | `+81.38%` | `15.00` |
| `Live` | `Short` | `15.35` | 1,150,000.00 USD | 230.17 USD | 0.00 USD | `+81.97%` | `15.00` |
| `Live` | `Short` | `15.38` | 1,170,000.00 USD | 20,000.00 USD | 0.00 USD | `+82.44%` | `1,300.00` |
| `Live` | `Short` | `16.29` | 1,170,000.00 USD | 115.79 USD | 0.00 USD | `+93.11%` | `7.11` |
| `Live` | `Short` | `16.34` | 1,440,000.00 USD | 264,920.00 USD | 0.00 USD | `+93.83%` | `16,208.00` |
| `Live` | `Short` | `16.36` | 1,620,000.00 USD | 186,130.00 USD | 0.00 USD | `+94.06%` | `11,373.91` |
| `Live` | `Short` | `16.52` | 1,620,000.00 USD | 190.91 USD | 0.00 USD | `+95.84%` | `11.56` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 245,510.00 USD | 0.00 USD | 611.73 USD | `-72.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 244,900.00 USD | 0.00 USD | 793.75 USD | `-52.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.49` | 244,110.00 USD | 0.00 USD | 105.04 USD | `-46.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 244,000.00 USD | 0.00 USD | 67,970.00 USD | `-40.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 176,030.00 USD | 0.00 USD | 205.30 USD | `-37.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 175,830.00 USD | 0.00 USD | 465.42 USD | `-35.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 175,360.00 USD | 0.00 USD | 349.35 USD | `-34.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.54` | 175,010.00 USD | 0.00 USD | 1,020.00 USD | `-34.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 174,000.00 USD | 0.00 USD | 1,330.00 USD | `-31.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 172,670.00 USD | 0.00 USD | 493.50 USD | `-29.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 172,180.00 USD | 0.00 USD | 100.98 USD | `-29.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 172,070.00 USD | 0.00 USD | 500.70 USD | `-28.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 171,570.00 USD | 0.00 USD | 4,160.00 USD | `-27.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 167,420.00 USD | 0.00 USD | 6,500.00 USD | `-26.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 160,920.00 USD | 0.00 USD | 864.38 USD | `-25.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 160,050.00 USD | 0.00 USD | 1,760.00 USD | `-22.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 158,300.00 USD | 0.00 USD | 4,340.00 USD | `-22.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 153,960.00 USD | 0.00 USD | 5,520.00 USD | `-20.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 148,430.00 USD | 0.00 USD | 100.72 USD | `-20.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 148,330.00 USD | 0.00 USD | 296.34 USD | `-19.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 148,040.00 USD | 0.00 USD | 921.19 USD | `-19.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 147,120.00 USD | 0.00 USD | 709.98 USD | `-18.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.92` | 146,410.00 USD | 0.00 USD | 691.50 USD | `-18.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 145,710.00 USD | 0.00 USD | 262.44 USD | `-17.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 145,450.00 USD | 0.00 USD | 1,820.00 USD | `-16.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 143,630.00 USD | 0.00 USD | 6,790.00 USD | `-15.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 136,840.00 USD | 0.00 USD | 9,770.00 USD | `-14.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 127,070.00 USD | 0.00 USD | 103.46 USD | `-14.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 126,970.00 USD | 0.00 USD | 603.44 USD | `-14.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 126,370.00 USD | 0.00 USD | 891.57 USD | `-13.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 125,480.00 USD | 0.00 USD | 2,090.00 USD | `-13.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 123,380.00 USD | 0.00 USD | 129.58 USD | `-13.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 123,250.00 USD | 0.00 USD | 114.65 USD | `-13.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 123,140.00 USD | 0.00 USD | 199.39 USD | `-11.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 122,940.00 USD | 0.00 USD | 4,730.00 USD | `-11.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 118,210.00 USD | 0.00 USD | 37,420.00 USD | `-11.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 80,780.00 USD | 0.00 USD | 2,120.00 USD | `-11.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 78,660.00 USD | 0.00 USD | 799.83 USD | `-10.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.54` | 77,860.00 USD | 0.00 USD | 820.44 USD | `-10.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.57` | 77,040.00 USD | 0.00 USD | 103.41 USD | `-10.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 76,940.00 USD | 0.00 USD | 1,370.00 USD | `-10.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.62` | 75,560.00 USD | 0.00 USD | 915.17 USD | `-9.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 74,650.00 USD | 0.00 USD | 360.13 USD | `-8.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 74,290.00 USD | 0.00 USD | 578.04 USD | `-8.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 73,710.00 USD | 0.00 USD | 175.42 USD | `-8.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 73,530.00 USD | 0.00 USD | 3,390.00 USD | `-7.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 70,150.00 USD | 0.00 USD | 143.51 USD | `-6.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 70,010.00 USD | 0.00 USD | 183.33 USD | `-6.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.88` | 69,820.00 USD | 0.00 USD | 194.52 USD | `-6.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 69,630.00 USD | 0.00 USD | 552.65 USD | `-6.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 69,080.00 USD | 0.00 USD | 2,050.00 USD | `-6.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 67,030.00 USD | 0.00 USD | 1,590.00 USD | `-6.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 65,440.00 USD | 0.00 USD | 898.42 USD | `-5.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.99` | 64,550.00 USD | 0.00 USD | 3,990.00 USD | `-5.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 60,550.00 USD | 0.00 USD | 1,350.00 USD | `-5.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 59,210.00 USD | 0.00 USD | 8,780.00 USD | `-5.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 50,430.00 USD | 0.00 USD | 123.58 USD | `-4.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 50,300.00 USD | 0.00 USD | 2,110.00 USD | `-4.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 48,190.00 USD | 0.00 USD | 563.85 USD | `-4.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 47,630.00 USD | 0.00 USD | 121.69 USD | `-4.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 47,510.00 USD | 0.00 USD | 477.36 USD | `-4.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 47,030.00 USD | 0.00 USD | 2,330.00 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 44,700.00 USD | 0.00 USD | 184.13 USD | `-3.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 44,510.00 USD | 0.00 USD | 6,500.00 USD | `-3.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 38,010.00 USD | 0.00 USD | 968.39 USD | `-3.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 37,040.00 USD | 0.00 USD | 654.53 USD | `-3.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 36,390.00 USD | 0.00 USD | 3,080.00 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 33,310.00 USD | 0.00 USD | 520.75 USD | `-3.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 32,790.00 USD | 0.00 USD | 3,020.00 USD | `-2.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 29,760.00 USD | 0.00 USD | 141.04 USD | `-2.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 29,620.00 USD | 0.00 USD | 3,840.00 USD | `-2.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 25,780.00 USD | 0.00 USD | 515.66 USD | `-2.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 25,270.00 USD | 0.00 USD | 629.15 USD | `-2.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.26` | 24,640.00 USD | 0.00 USD | 9,110.00 USD | `-2.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.27` | 15,530.00 USD | 0.00 USD | 353.00 USD | `-1.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 15,170.00 USD | 0.00 USD | 168.64 USD | `-1.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 15,000.00 USD | 0.00 USD | 201.49 USD | `-1.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 14,800.00 USD | 0.00 USD | 242.42 USD | `-1.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 14,560.00 USD | 0.00 USD | 2,920.00 USD | `-1.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 11,640.00 USD | 0.00 USD | 2,000.00 USD | `-1.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 9,640.00 USD | 0.00 USD | 756.06 USD | `-1.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 8,880.00 USD | 0.00 USD | 970.35 USD | `-0.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 7,910.00 USD | 0.00 USD | 419.25 USD | `-0.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 7,500.00 USD | 0.00 USD | 1,970.00 USD | `-0.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 5,530.00 USD | 0.00 USD | 3,290.00 USD | `-0.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 2,240.00 USD | 0.00 USD | 358.56 USD | `-0.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 1,880.00 USD | 0.00 USD | 1,880.00 USD | `-0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.44` | 140.36 USD | 140.36 USD | 0.00 USD | `+0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.45` | 278.60 USD | 138.24 USD | 0.00 USD | `+0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.46` | 1,230.00 USD | 954.23 USD | 0.00 USD | `+0.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.47` | 2,000.00 USD | 769.61 USD | 0.00 USD | `+0.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.48` | 2,490.00 USD | 489.58 USD | 0.00 USD | `+0.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.51` | 3,940.00 USD | 1,440.00 USD | 0.00 USD | `+0.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.52` | 4,130.00 USD | 198.74 USD | 0.00 USD | `+0.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.53` | 5,260.00 USD | 1,130.00 USD | 0.00 USD | `+1.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 5,770.00 USD | 510.39 USD | 0.00 USD | `+1.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 10,180.00 USD | 4,400.00 USD | 0.00 USD | `+1.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.55` | 10,420.00 USD | 243.82 USD | 0.00 USD | `+1.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.57` | 10,850.00 USD | 428.58 USD | 0.00 USD | `+1.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.59` | 13,350.00 USD | 2,500.00 USD | 0.00 USD | `+1.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.60` | 14,480.00 USD | 1,130.00 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 15,560.00 USD | 1,080.00 USD | 0.00 USD | `+2.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 17,540.00 USD | 1,980.00 USD | 0.00 USD | `+2.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 20,280.00 USD | 2,740.00 USD | 0.00 USD | `+2.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.63` | 21,990.00 USD | 1,710.00 USD | 0.00 USD | `+2.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.64` | 22,090.00 USD | 103.31 USD | 0.00 USD | `+2.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 24,000.00 USD | 1,900.00 USD | 0.00 USD | `+2.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 24,300.00 USD | 307.87 USD | 0.00 USD | `+2.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.68` | 24,530.00 USD | 223.82 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.69` | 25,520.00 USD | 990.09 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.70` | 30,530.00 USD | 5,010.00 USD | 0.00 USD | `+3.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 30,840.00 USD | 309.29 USD | 0.00 USD | `+3.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 30,970.00 USD | 134.30 USD | 0.00 USD | `+3.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.72` | 31,790.00 USD | 819.28 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.73` | 32,130.00 USD | 333.07 USD | 0.00 USD | `+3.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.74` | 36,500.00 USD | 4,370.00 USD | 0.00 USD | `+3.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.76` | 42,800.00 USD | 6,300.00 USD | 0.00 USD | `+3.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 82,610.00 USD | 39,810.00 USD | 0.00 USD | `+3.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.78` | 82,910.00 USD | 307.39 USD | 0.00 USD | `+4.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 83,300.00 USD | 388.12 USD | 0.00 USD | `+4.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 84,010.00 USD | 711.78 USD | 0.00 USD | `+4.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 104,850.00 USD | 20,840.00 USD | 0.00 USD | `+4.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.81` | 105,560.00 USD | 705.20 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.82` | 107,590.00 USD | 2,030.00 USD | 0.00 USD | `+4.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.84` | 107,830.00 USD | 243.40 USD | 0.00 USD | `+4.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 113,600.00 USD | 5,760.00 USD | 0.00 USD | `+4.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 113,790.00 USD | 192.86 USD | 0.00 USD | `+5.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 114,410.00 USD | 614.88 USD | 0.00 USD | `+5.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 114,520.00 USD | 110.58 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 115,620.00 USD | 1,100.00 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 115,810.00 USD | 188.66 USD | 0.00 USD | `+5.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 116,600.00 USD | 788.72 USD | 0.00 USD | `+5.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 118,530.00 USD | 1,940.00 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 118,700.00 USD | 163.33 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 119,480.00 USD | 782.17 USD | 0.00 USD | `+5.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 119,700.00 USD | 223.62 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 119,880.00 USD | 180.53 USD | 0.00 USD | `+6.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 120,290.00 USD | 401.63 USD | 0.00 USD | `+6.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 435,440.00 USD | 315,150.00 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 435,540.00 USD | 104.59 USD | 0.00 USD | `+6.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 435,810.00 USD | 262.56 USD | 0.00 USD | `+6.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 435,940.00 USD | 130.03 USD | 0.00 USD | `+6.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 437,310.00 USD | 1,380.00 USD | 0.00 USD | `+6.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 438,400.00 USD | 1,090.00 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 439,020.00 USD | 616.37 USD | 0.00 USD | `+7.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 439,120.00 USD | 102.03 USD | 0.00 USD | `+7.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 439,570.00 USD | 453.84 USD | 0.00 USD | `+7.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 439,730.00 USD | 160.99 USD | 0.00 USD | `+7.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 440,150.00 USD | 415.00 USD | 0.00 USD | `+7.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 441,660.00 USD | 1,510.00 USD | 0.00 USD | `+7.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 442,280.00 USD | 619.64 USD | 0.00 USD | `+7.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 669,910.00 USD | 227,630.00 USD | 0.00 USD | `+7.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 674,470.00 USD | 4,560.00 USD | 0.00 USD | `+8.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 676,470.00 USD | 2,000.00 USD | 0.00 USD | `+8.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 1,070,000.00 USD | 394,210.00 USD | 0.00 USD | `+8.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,070,000.00 USD | 119.24 USD | 0.00 USD | `+8.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.20` | 1,070,000.00 USD | 1,590.00 USD | 0.00 USD | `+9.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,080,000.00 USD | 2,660.00 USD | 0.00 USD | `+9.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,080,000.00 USD | 131.87 USD | 0.00 USD | `+9.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,080,000.00 USD | 687.91 USD | 0.00 USD | `+9.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,080,000.00 USD | 954.71 USD | 0.00 USD | `+9.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,350,000.00 USD | 277,660.00 USD | 0.00 USD | `+9.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.27` | 1,350,000.00 USD | 205.87 USD | 0.00 USD | `+9.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,360,000.00 USD | 1,960.00 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,360,000.00 USD | 434.45 USD | 0.00 USD | `+10.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,380,000.00 USD | 18,610.00 USD | 0.00 USD | `+10.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,380,000.00 USD | 166.83 USD | 0.00 USD | `+10.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,380,000.00 USD | 2,180.00 USD | 0.00 USD | `+10.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,380,000.00 USD | 579.86 USD | 0.00 USD | `+10.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,380,000.00 USD | 109.36 USD | 0.00 USD | `+10.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,380,000.00 USD | 116.69 USD | 0.00 USD | `+11.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,380,000.00 USD | 163.41 USD | 0.00 USD | `+11.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,380,000.00 USD | 1,150.00 USD | 0.00 USD | `+11.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,380,000.00 USD | 660.84 USD | 0.00 USD | `+11.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,380,000.00 USD | 820.59 USD | 0.00 USD | `+11.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,380,000.00 USD | 928.13 USD | 0.00 USD | `+11.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 1,380,000.00 USD | 102.45 USD | 0.00 USD | `+11.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,380,000.00 USD | 219.84 USD | 0.00 USD | `+11.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.45` | 1,380,000.00 USD | 140.35 USD | 0.00 USD | `+12.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,380,000.00 USD | 1,890.00 USD | 0.00 USD | `+12.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.47` | 1,390,000.00 USD | 1,780.00 USD | 0.00 USD | `+12.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,390,000.00 USD | 2,210.00 USD | 0.00 USD | `+12.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,390,000.00 USD | 288.46 USD | 0.00 USD | `+12.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.51` | 1,390,000.00 USD | 1,600.00 USD | 0.00 USD | `+12.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,390,000.00 USD | 223.46 USD | 0.00 USD | `+12.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,390,000.00 USD | 231.00 USD | 0.00 USD | `+13.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,390,000.00 USD | 221.07 USD | 0.00 USD | `+13.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,390,000.00 USD | 1,470.00 USD | 0.00 USD | `+13.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,390,000.00 USD | 148.48 USD | 0.00 USD | `+14.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,390,000.00 USD | 191.36 USD | 0.00 USD | `+14.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,390,000.00 USD | 446.58 USD | 0.00 USD | `+14.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,390,000.00 USD | 108.21 USD | 0.00 USD | `+15.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,390,000.00 USD | 169.68 USD | 0.00 USD | `+15.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.74` | 1,390,000.00 USD | 574.66 USD | 0.00 USD | `+15.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,390,000.00 USD | 121.87 USD | 0.00 USD | `+15.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.80` | 1,400,000.00 USD | 619.28 USD | 0.00 USD | `+16.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,400,000.00 USD | 5,030.00 USD | 0.00 USD | `+16.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,400,000.00 USD | 340.05 USD | 0.00 USD | `+16.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,400,000.00 USD | 742.12 USD | 0.00 USD | `+17.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,400,000.00 USD | 899.47 USD | 0.00 USD | `+17.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,470,000.00 USD | 70,020.00 USD | 0.00 USD | `+17.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,470,000.00 USD | 373.97 USD | 0.00 USD | `+17.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,480,000.00 USD | 5,050.00 USD | 0.00 USD | `+18.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,480,000.00 USD | 6,370.00 USD | 0.00 USD | `+19.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,480,000.00 USD | 202.10 USD | 0.00 USD | `+19.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,700,000.00 USD | 210,980.00 USD | 0.00 USD | `+19.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,700,000.00 USD | 1,150.00 USD | 0.00 USD | `+20.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 1,700,000.00 USD | 172.16 USD | 0.00 USD | `+21.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 1,700,000.00 USD | 895.21 USD | 0.00 USD | `+21.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 1,700,000.00 USD | 489.40 USD | 0.00 USD | `+22.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 1,700,000.00 USD | 1,200.00 USD | 0.00 USD | `+22.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 1,700,000.00 USD | 118.01 USD | 0.00 USD | `+23.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 1,700,000.00 USD | 312.31 USD | 0.00 USD | `+24.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 1,700,000.00 USD | 2,290.00 USD | 0.00 USD | `+24.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 1,700,000.00 USD | 178.46 USD | 0.00 USD | `+25.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.62` | 1,700,000.00 USD | 153.11 USD | 0.00 USD | `+26.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 1,700,000.00 USD | 173.42 USD | 0.00 USD | `+27.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 1,700,000.00 USD | 184.75 USD | 0.00 USD | `+27.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 1,700,000.00 USD | 135.78 USD | 0.00 USD | `+27.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 1,700,000.00 USD | 127.96 USD | 0.00 USD | `+28.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 1,700,000.00 USD | 476.43 USD | 0.00 USD | `+28.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 1,700,000.00 USD | 667.39 USD | 0.00 USD | `+29.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 1,700,000.00 USD | 118.97 USD | 0.00 USD | `+29.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 1,700,000.00 USD | 251.06 USD | 0.00 USD | `+29.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 1,700,000.00 USD | 552.44 USD | 0.00 USD | `+29.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 1,710,000.00 USD | 537.26 USD | 0.00 USD | `+30.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 1,710,000.00 USD | 320.29 USD | 0.00 USD | `+31.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 1,710,000.00 USD | 1,100.00 USD | 0.00 USD | `+32.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 1,710,000.00 USD | 2,610.00 USD | 0.00 USD | `+32.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 1,710,000.00 USD | 1,270.00 USD | 0.00 USD | `+33.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 1,710,000.00 USD | 1,380.00 USD | 0.00 USD | `+34.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 1,710,000.00 USD | 2,410.00 USD | 0.00 USD | `+35.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 1,720,000.00 USD | 9,520.00 USD | 0.00 USD | `+35.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.48` | 1,730,000.00 USD | 3,250.00 USD | 0.00 USD | `+36.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 1,730,000.00 USD | 316.04 USD | 0.00 USD | `+36.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 1,740,000.00 USD | 7,700.00 USD | 0.00 USD | `+37.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 1,740,000.00 USD | 1,130.00 USD | 0.00 USD | `+40.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 1,740,000.00 USD | 434.61 USD | 0.00 USD | `+40.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 1,740,000.00 USD | 163.52 USD | 0.00 USD | `+40.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 1,860,000.00 USD | 123,650.00 USD | 0.00 USD | `+42.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.51` | 1,860,000.00 USD | 2,770.00 USD | 0.00 USD | `+48.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 1,870,000.00 USD | 3,350.00 USD | 0.00 USD | `+50.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 1,870,000.00 USD | 197.97 USD | 0.00 USD | `+51.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 1,870,000.00 USD | 3,200.00 USD | 0.00 USD | `+53.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 1,870,000.00 USD | 179.58 USD | 0.00 USD | `+53.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 1,870,000.00 USD | 720.74 USD | 0.00 USD | `+54.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.07` | 1,870,000.00 USD | 504.17 USD | 0.00 USD | `+55.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 1,870,000.00 USD | 169.57 USD | 0.00 USD | `+55.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.30` | 1,870,000.00 USD | 159.66 USD | 0.00 USD | `+57.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 1,870,000.00 USD | 446.52 USD | 0.00 USD | `+58.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.46` | 1,870,000.00 USD | 1,710.00 USD | 0.00 USD | `+59.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 1,880,000.00 USD | 5,320.00 USD | 0.00 USD | `+59.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,090,000.00 USD | 207,980.00 USD | 0.00 USD | `+60.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,090,000.00 USD | 407.95 USD | 0.00 USD | `+62.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,090,000.00 USD | 174.91 USD | 0.00 USD | `+63.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,100,000.00 USD | 8,370.00 USD | 0.00 USD | `+66.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,100,000.00 USD | 960.26 USD | 0.00 USD | `+68.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,100,000.00 USD | 2,710.00 USD | 0.00 USD | `+70.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,100,000.00 USD | 805.90 USD | 0.00 USD | `+72.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,100,000.00 USD | 655.55 USD | 0.00 USD | `+74.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,110,000.00 USD | 4,890.00 USD | 0.00 USD | `+75.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,110,000.00 USD | 471.09 USD | 0.00 USD | `+76.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,110,000.00 USD | 383.85 USD | 0.00 USD | `+77.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 2,760,000.00 USD | 652,670.00 USD | 0.00 USD | `+77.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.06` | 2,760,000.00 USD | 1,510.00 USD | 0.00 USD | `+78.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 2,760,000.00 USD | 111.87 USD | 0.00 USD | `+87.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 2,760,000.00 USD | 219.91 USD | 0.00 USD | `+89.79%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.36` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 6,810.00 USD | 2,430.00 USD | 0.00 USD |
| `7D` | `7.40` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 6,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.42` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 62.56 USD |
| `7D` | `7.44` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 331.70 USD | 1,680.00 USD | 15.01 USD |
| `7D` | `7.46` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 0.00 USD | 1,410.00 USD | 3,860.00 USD |
| `1D` | `7.47` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 723.17 USD | 0.00 USD | 67.94 USD |
| `7D` | `7.48` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 9,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.51` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 1,020.00 USD | 4,920.00 USD | 0.00 USD |
| `7D` | `7.52` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 1,150.00 USD | 7,290.00 USD | 0.00 USD |
| `1D` | `7.53` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 17,820.00 USD | 9,580.00 USD | 3,350.00 USD |
| `7D` | `7.54` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 0.00 USD | 4,450.00 USD | 0.00 USD |
| `1D` | `7.55` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 306.57 USD | 4,270.00 USD | 0.00 USD |
| `7D` | `7.56` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 0.00 USD | 4,310.00 USD | 0.00 USD |
| `1D` | `7.57` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 14,710.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.59` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 266.89 USD |
| `1D` | `7.61` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 989.00 USD | 3,770.00 USD | 11,740.00 USD |
| `1D` | `7.63` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 986.95 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.64` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 812.40 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.65` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 16,880.00 USD | 0.00 USD | 9,430.00 USD |
| `7D` | `7.66` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 23,280.00 USD |
| `7D` | `7.68` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 9,280.00 USD |
| `1D` | `7.71` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 3,940.00 USD | 4,030.00 USD | 26,510.00 USD |
| `7D` | `7.72` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 32,590.00 USD |
| `1D` | `7.73` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 2,170.00 USD | 0.00 USD | 2,430.00 USD |
| `7D` | `7.74` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 976.80 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.75` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 1,320.00 USD | 5,690.00 USD | 344.99 USD |
| `7D` | `7.76` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 812.95 USD | 5,760.00 USD | 0.00 USD |
| `1D` | `7.77` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 34,420.00 USD | 572.85 USD | 14,130.00 USD |
| `7D` | `7.78` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 43,620.00 USD | 4,900.00 USD | 20,150.00 USD |
| `1D` | `7.79` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 45,170.00 USD | 12,560.00 USD | 5,400.00 USD |
| `7D` | `7.80` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 14,770.00 USD | 12,980.00 USD | 0.00 USD |
| `1D` | `7.81` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 6,750.00 USD | 7,800.00 USD | 6,020.00 USD |
| `7D` | `7.82` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,280.00 USD |
| `1D` | `7.83` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 5,390.00 USD | 4,390.00 USD | 7,390.00 USD |
| `7D` | `7.84` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 30,950.00 USD | 2,380.00 USD | 25,450.00 USD |
| `1D` | `7.85` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 5,240.00 USD | 3,060.00 USD | 10,340.00 USD |
| `7D` | `7.86` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 25,770.00 USD | 5,460.00 USD | 17,740.00 USD |
| `1D` | `7.87` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 31,020.00 USD | 4,570.00 USD | 28,710.00 USD |
| `7D` | `7.88` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 58,120.00 USD | 12,780.00 USD | 30,160.00 USD |
| `1D` | `7.89` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 30,650.00 USD | 9,580.00 USD | 10,120.00 USD |
| `7D` | `7.90` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 33,680.00 USD | 12,890.00 USD | 17,650.00 USD |
| `1D` | `7.91` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 17,770.00 USD | 3,480.00 USD | 7,980.00 USD |
| `7D` | `7.92` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 55,490.00 USD | 8,420.00 USD | 14,900.00 USD |
| `1D` | `7.93` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 23,780.00 USD | 5,660.00 USD | 3,970.00 USD |
| `7D` | `7.94` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 51,390.00 USD | 9,960.00 USD | 31,670.00 USD |
| `1D` | `7.95` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 12,440.00 USD | 9,310.00 USD | 8,590.00 USD |
| `7D` | `7.96` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 21,840.00 USD | 6,920.00 USD | 26,390.00 USD |
| `1D` | `7.97` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 14,420.00 USD | 5,620.00 USD | 4,050.00 USD |
| `7D` | `7.98` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 56,660.00 USD | 19,680.00 USD | 70,210.00 USD |
| `1D` | `7.99` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 4,980.00 USD | 1,380.00 USD | 4,440.00 USD |
| `7D` | `8.00` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 61,850.00 USD | 10,300.00 USD | 5,130.00 USD |
| `1D` | `8.01` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 7,530.00 USD | 14,140.00 USD | 2,500.00 USD |
| `7D` | `8.02` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 20,910.00 USD | 46,670.00 USD | 11,370.00 USD |
| `1D` | `8.03` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 64,640.00 USD | 28,390.00 USD | 8,820.00 USD |
| `7D` | `8.04` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 123,080.00 USD | 38,980.00 USD | 86,550.00 USD |
| `1D` | `8.05` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 38,290.00 USD | 20,600.00 USD | 6,710.00 USD |
| `7D` | `8.06` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 73,280.00 USD | 20,850.00 USD | 86,170.00 USD |
| `1D` | `8.07` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 82,700.00 USD | 4,100.00 USD | 11,220.00 USD |
| `7D` | `8.08` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 7,170.00 USD | 8,710.00 USD | 20,860.00 USD |
| `1D` | `8.09` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 13,650.00 USD | 4,700.00 USD | 13,070.00 USD |
| `7D` | `8.10` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 61,500.00 USD | 19,700.00 USD | 14,170.00 USD |
| `1D` | `8.11` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 47,180.00 USD | 15,090.00 USD | 33,610.00 USD |
| `7D` | `8.12` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 27,520.00 USD | 10,810.00 USD | 22,640.00 USD |
| `1D` | `8.13` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 55,540.00 USD | 4,640.00 USD | 1,900.00 USD |
| `7D` | `8.14` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 72,460.00 USD | 11,150.00 USD | 39,780.00 USD |
| `1D` | `8.15` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 52,860.00 USD | 0.00 USD | 204.31 USD |
| `7D` | `8.16` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 38,430.00 USD | 5,510.00 USD | 30,810.00 USD |
| `1D` | `8.17` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 3,360.00 USD | 24,600.00 USD | 49,150.00 USD |
| `7D` | `8.18` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 39,830.00 USD | 43,260.00 USD | 84,290.00 USD |
| `1D` | `8.19` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 96,460.00 USD | 52,150.00 USD | 17,220.00 USD |
| `7D` | `8.20` | 978,050.00 USD | 0.00 USD | 978,050.00 USD | 33,800.00 USD | 22,240.00 USD | 9,870.00 USD |
| `1D` | `8.21` | 976,100.00 USD | 0.00 USD | 976,100.00 USD | 29,670.00 USD | 0.00 USD | 25,720.00 USD |
| `7D` | `8.22` | 912,150.00 USD | 0.00 USD | 912,150.00 USD | 19,610.00 USD | 21,570.00 USD | 10,790.00 USD |
| `1D` | `8.23` | 920,720.00 USD | 0.00 USD | 920,720.00 USD | 99,940.00 USD | 43,740.00 USD | 51,730.00 USD |
| `7D` | `8.24` | 860,180.00 USD | 0.00 USD | 860,180.00 USD | 39,950.00 USD | 3,480.00 USD | 107,080.00 USD |
| `1D` | `8.25` | 725,310.00 USD | 0.00 USD | 725,310.00 USD | 73,710.00 USD | 1,150.00 USD | 20,120.00 USD |
| `7D` | `8.26` | 709,660.00 USD | 0.00 USD | 709,660.00 USD | 30,490.00 USD | 5,750.00 USD | 1,710.00 USD |
| `1D` | `8.27` | 630,330.00 USD | 0.00 USD | 630,330.00 USD | 48,820.00 USD | 37,210.00 USD | 21.52 USD |
| `7D` | `8.28` | 671,710.00 USD | 0.00 USD | 671,710.00 USD | 122,850.00 USD | 33,920.00 USD | 49,860.00 USD |
| `1D` | `8.29` | 544,270.00 USD | 0.00 USD | 544,270.00 USD | 267,700.00 USD | 25,810.00 USD | 115,360.00 USD |
| `7D` | `8.30` | 465,080.00 USD | 0.00 USD | 465,080.00 USD | 152,370.00 USD | 11,360.00 USD | 48,060.00 USD |
| `1D` | `8.31` | 135,400.00 USD | 0.00 USD | 135,400.00 USD | 107,430.00 USD | 0.00 USD | 20,510.00 USD |
| `7D` | `8.32` | 253,290.00 USD | 0.00 USD | 253,290.00 USD | 42,900.00 USD | 0.00 USD | 5,060.00 USD |
| `1D` | `8.33` | 7,460.00 USD | 0.00 USD | 7,460.00 USD | 0.00 USD | 0.00 USD | 7,430.00 USD |
| `7D` | `8.34` | 205,330.00 USD | 0.00 USD | 205,330.00 USD | 58,620.00 USD | 0.00 USD | 146,710.00 USD |
| `1D` | `8.35` | 31.64 USD | 0.00 USD | 31.64 USD | 0.00 USD | 0.00 USD | 31.64 USD |
| `7D` | `8.36` | 209,880.00 USD | 209,880.00 USD | 0.00 USD | 78,130.00 USD | 0.00 USD | 131,750.00 USD |
| `7D` | `8.36` | 419,760.00 USD | 419,760.00 USD | 0.00 USD | 78,130.00 USD | 0.00 USD | 131,750.00 USD |
| `1D` | `8.37` | 709.59 USD | 709.59 USD | 0.00 USD | 691.75 USD | 0.00 USD | 17.84 USD |
| `1D` | `8.37` | 1,420.00 USD | 1,420.00 USD | 0.00 USD | 691.75 USD | 0.00 USD | 17.84 USD |
| `7D` | `8.38` | 606,650.00 USD | 606,650.00 USD | 0.00 USD | 120,320.00 USD | 0.00 USD | 66,570.00 USD |
| `1D` | `8.39` | 1,470.00 USD | 1,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 47.78 USD |
| `7D` | `8.40` | 797,170.00 USD | 797,170.00 USD | 0.00 USD | 155,410.00 USD | 0.00 USD | 35,110.00 USD |
| `7D` | `8.42` | 964,470.00 USD | 964,470.00 USD | 0.00 USD | 166,020.00 USD | 0.00 USD | 1,270.00 USD |
| `1D` | `8.43` | 2,260.00 USD | 2,260.00 USD | 0.00 USD | 788.46 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.44` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 155,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.46` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 365,050.00 USD | 0.00 USD | 3,300.00 USD |
| `1D` | `8.47` | 2,270.00 USD | 2,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18.78 USD |
| `7D` | `8.48` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 35,130.00 USD | 1,380.00 USD |
| `1D` | `8.49` | 87,820.00 USD | 87,820.00 USD | 0.00 USD | 0.00 USD | 85,530.00 USD | 12.70 USD |
| `7D` | `8.50` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 100,070.00 USD | 1,470.00 USD |
| `1D` | `8.51` | 268,200.00 USD | 268,200.00 USD | 0.00 USD | 92,450.00 USD | 87,920.00 USD | 0.00 USD |
| `7D` | `8.52` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 2,990.00 USD | 135,400.00 USD | 1,210.00 USD |
| `1D` | `8.53` | 490,230.00 USD | 490,230.00 USD | 0.00 USD | 153,130.00 USD | 52,150.00 USD | 16,760.00 USD |
| `7D` | `8.54` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 13,020.00 USD | 100,610.00 USD | 2,010.00 USD |
| `1D` | `8.55` | 598,840.00 USD | 598,840.00 USD | 0.00 USD | 108,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.56` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 593,510.00 USD | 122,650.00 USD | 790.79 USD |
| `1D` | `8.57` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 271,150.00 USD | 33,670.00 USD | 97,760.00 USD |
| `7D` | `8.58` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 599,490.00 USD | 164,810.00 USD | 801.88 USD |
| `1D` | `8.59` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 58,280.00 USD | 29,830.00 USD | 93,310.00 USD |
| `7D` | `8.60` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 75,040.00 USD | 39,160.00 USD | 1,110.00 USD |
| `1D` | `8.61` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 28,330.00 USD | 59,000.00 USD | 39,710.00 USD |
| `7D` | `8.62` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 43,670.00 USD | 26,750.00 USD |
| `1D` | `8.63` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 126,840.00 USD | 53,490.00 USD | 58,020.00 USD |
| `7D` | `8.64` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 5,680.00 USD | 0.00 USD |
| `1D` | `8.65` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33,010.00 USD |
| `7D` | `8.66` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 16,520.00 USD | 992.53 USD |
| `1D` | `8.67` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 78,620.00 USD | 12,300.00 USD | 119,250.00 USD |
| `7D` | `8.68` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 207,090.00 USD | 43,100.00 USD | 290,060.00 USD |
| `1D` | `8.69` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 44,550.00 USD | 26,070.00 USD | 56,450.00 USD |
| `7D` | `8.70` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 23,910.00 USD | 46,400.00 USD |
| `1D` | `8.71` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 67,860.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.73` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 28,810.00 USD | 50,740.00 USD |
| `7D` | `8.74` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD | 0.00 USD |
| `1D` | `8.75` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 70,290.00 USD | 0.00 USD | 5,340.00 USD |
| `7D` | `8.76` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,400.00 USD |
| `1D` | `8.77` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 153,570.00 USD | 2,060.00 USD | 30,980.00 USD |
| `7D` | `8.78` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 2,300.00 USD | 0.00 USD | 58,840.00 USD |
| `1D` | `8.79` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 65,930.00 USD | 21,430.00 USD | 38,890.00 USD |
| `7D` | `8.80` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 27,360.00 USD | 33,750.00 USD | 31,560.00 USD |
| `1D` | `8.81` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 110,240.00 USD | 10,330.00 USD | 23,840.00 USD |
| `7D` | `8.82` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 103,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.83` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 40,210.00 USD | 8,820.00 USD | 0.00 USD |
| `1D` | `8.85` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 13,330.00 USD | 2,250.00 USD | 84,780.00 USD |
| `7D` | `8.86` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 29,310.00 USD | 0.00 USD | 82,390.00 USD |
| `1D` | `8.87` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 2,380.00 USD | 0.00 USD | 301.25 USD |
| `7D` | `8.88` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,570.00 USD |
| `1D` | `8.89` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 3,280.00 USD | 11,100.00 USD | 32,830.00 USD |
| `7D` | `8.90` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 2,440.00 USD | 0.00 USD | 115,480.00 USD |
| `1D` | `8.91` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 60,600.00 USD | 13,350.00 USD | 103,480.00 USD |
| `7D` | `8.92` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 1,730.00 USD | 0.00 USD | 17,620.00 USD |
| `1D` | `8.93` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 40,520.00 USD | 0.00 USD | 21,000.00 USD |
| `7D` | `8.94` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 58,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.95` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 10,600.00 USD | 12,260.00 USD | 0.00 USD |
| `7D` | `8.96` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.97` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 670.84 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.98` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,090.00 USD |
| `1D` | `8.99` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 73,440.00 USD | 36,070.00 USD | 22,980.00 USD |
| `7D` | `9.00` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 297,650.00 USD | 11,360.00 USD | 20,780.00 USD |
| `1D` | `9.01` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 38,950.00 USD | 9,530.00 USD | 22,120.00 USD |
| `7D` | `9.02` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 34,650.00 USD | 56,120.00 USD | 749.72 USD |
| `1D` | `9.03` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 107,510.00 USD | 66,510.00 USD | 32,380.00 USD |
| `7D` | `9.04` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 90,520.00 USD | 74,750.00 USD | 15,140.00 USD |
| `1D` | `9.05` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 25,720.00 USD | 37,250.00 USD | 49,400.00 USD |
| `7D` | `9.06` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 7,440.00 USD | 14,960.00 USD | 53,420.00 USD |
| `1D` | `9.07` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 43,430.00 USD | 30,110.00 USD | 52,770.00 USD |
| `7D` | `9.08` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD |
| `1D` | `9.09` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 129,020.00 USD | 27,290.00 USD | 88,210.00 USD |
| `7D` | `9.10` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 826,500.00 USD | 35,760.00 USD | 334,020.00 USD |
| `1D` | `9.11` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 134,540.00 USD | 38,180.00 USD | 64,530.00 USD |
| `7D` | `9.12` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 490,020.00 USD | 24,170.00 USD | 479,410.00 USD |
| `1D` | `9.13` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 192,240.00 USD | 51,740.00 USD | 46,440.00 USD |
| `7D` | `9.14` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 536,560.00 USD | 18,540.00 USD | 479,710.00 USD |
| `1D` | `9.15` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 92,380.00 USD | 25,540.00 USD | 42,220.00 USD |
| `7D` | `9.16` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 358,370.00 USD | 44,360.00 USD | 195,800.00 USD |
| `1D` | `9.17` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 171,770.00 USD | 42,570.00 USD | 71,120.00 USD |
| `7D` | `9.18` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 565,140.00 USD | 162,460.00 USD | 273,760.00 USD |
| `1D` | `9.19` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 170,520.00 USD | 68,530.00 USD | 58,200.00 USD |
| `7D` | `9.20` | 11,330,000.00 USD | 11,330,000.00 USD | 0.00 USD | 549,250.00 USD | 127,380.00 USD | 238,840.00 USD |
| `1D` | `9.21` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 96,500.00 USD | 15,410.00 USD | 40,150.00 USD |
| `7D` | `9.22` | 12,480,000.00 USD | 12,480,000.00 USD | 0.00 USD | 585,170.00 USD | 144,840.00 USD | 416,230.00 USD |
| `1D` | `9.23` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 54,700.00 USD | 11,900.00 USD | 11,110.00 USD |
| `7D` | `9.24` | 13,030,000.00 USD | 13,030,000.00 USD | 0.00 USD | 316,220.00 USD | 56,410.00 USD | 174,910.00 USD |
| `1D` | `9.25` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 64,470.00 USD | 7,080.00 USD | 9,510.00 USD |
| `7D` | `9.26` | 13,460,000.00 USD | 13,460,000.00 USD | 0.00 USD | 273,920.00 USD | 96,980.00 USD | 60,730.00 USD |
| `1D` | `9.27` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 39,860.00 USD | 4,490.00 USD | 2,880.00 USD |
| `7D` | `9.28` | 14,160,000.00 USD | 14,160,000.00 USD | 0.00 USD | 428,160.00 USD | 103,490.00 USD | 170,610.00 USD |
| `1D` | `9.29` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 37,550.00 USD | 11,780.00 USD | 18,030.00 USD |
| `7D` | `9.30` | 14,720,000.00 USD | 14,720,000.00 USD | 0.00 USD | 199,810.00 USD | 97,780.00 USD | 262,830.00 USD |
| `1D` | `9.31` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 70,620.00 USD | 13,670.00 USD | 24,560.00 USD |
| `7D` | `9.32` | 15,390,000.00 USD | 15,390,000.00 USD | 0.00 USD | 271,660.00 USD | 59,310.00 USD | 337,940.00 USD |
| `1D` | `9.33` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 17,610.00 USD | 6,000.00 USD | 11,600.00 USD |
| `7D` | `9.34` | 15,720,000.00 USD | 15,720,000.00 USD | 0.00 USD | 204,260.00 USD | 53,150.00 USD | 70,540.00 USD |
| `1D` | `9.35` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 61,720.00 USD | 8,000.00 USD | 38,330.00 USD |
| `7D` | `9.36` | 16,140,000.00 USD | 16,140,000.00 USD | 0.00 USD | 247,120.00 USD | 73,430.00 USD | 97,710.00 USD |
| `1D` | `9.37` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 54,310.00 USD | 18,910.00 USD | 19,020.00 USD |
| `7D` | `9.38` | 16,670,000.00 USD | 16,670,000.00 USD | 0.00 USD | 383,530.00 USD | 55,400.00 USD | 94,530.00 USD |
| `1D` | `9.39` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 24,810.00 USD | 683.54 USD | 10,210.00 USD |
| `7D` | `9.40` | 17,070,000.00 USD | 17,070,000.00 USD | 0.00 USD | 234,760.00 USD | 42,520.00 USD | 124,730.00 USD |
| `1D` | `9.41` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 24,200.00 USD | 0.00 USD | 10,160.00 USD |
| `7D` | `9.42` | 17,350,000.00 USD | 17,350,000.00 USD | 0.00 USD | 176,920.00 USD | 19,780.00 USD | 84,120.00 USD |
| `1D` | `9.43` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 18,750.00 USD | 4,030.00 USD | 16,420.00 USD |
| `7D` | `9.44` | 17,470,000.00 USD | 17,470,000.00 USD | 0.00 USD | 41,250.00 USD | 19,420.00 USD | 56,670.00 USD |
| `1D` | `9.45` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 1,360.00 USD | 0.00 USD | 2,430.00 USD |
| `7D` | `9.46` | 17,580,000.00 USD | 17,580,000.00 USD | 0.00 USD | 60,020.00 USD | 29,830.00 USD | 19,460.00 USD |
| `1D` | `9.47` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 2,380.00 USD | 5,690.00 USD | 192.20 USD |
| `7D` | `9.48` | 17,650,000.00 USD | 17,650,000.00 USD | 0.00 USD | 12,180.00 USD | 27,840.00 USD | 25,250.00 USD |
| `1D` | `9.49` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 31,340.00 USD | 572.85 USD | 14,130.00 USD |
| `7D` | `9.50` | 17,850,000.00 USD | 17,850,000.00 USD | 0.00 USD | 89,460.00 USD | 33,210.00 USD | 83,550.00 USD |
| `1D` | `9.51` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 12,280.00 USD | 3,160.00 USD | 124.70 USD |
| `7D` | `9.52` | 18,040,000.00 USD | 18,040,000.00 USD | 0.00 USD | 102,150.00 USD | 29,320.00 USD | 51,740.00 USD |
| `1D` | `9.53` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 35,250.00 USD | 9,400.00 USD | 5,400.00 USD |
| `7D` | `9.54` | 18,250,000.00 USD | 18,250,000.00 USD | 0.00 USD | 192,090.00 USD | 25,090.00 USD | 930.52 USD |
| `1D` | `9.55` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 7,860.00 USD | 7,800.00 USD | 6,030.00 USD |
| `7D` | `9.56` | 18,360,000.00 USD | 18,360,000.00 USD | 0.00 USD | 88,510.00 USD | 5,260.00 USD | 13,550.00 USD |
| `1D` | `9.57` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 5,780.00 USD | 4,390.00 USD | 7,390.00 USD |
| `7D` | `9.58` | 18,440,000.00 USD | 18,440,000.00 USD | 0.00 USD | 35,340.00 USD | 14,530.00 USD | 27,300.00 USD |
| `1D` | `9.59` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 5,320.00 USD | 3,060.00 USD | 10,340.00 USD |
| `7D` | `9.60` | 18,500,000.00 USD | 18,500,000.00 USD | 0.00 USD | 38,740.00 USD | 5,460.00 USD | 18,930.00 USD |
| `1D` | `9.61` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 29,510.00 USD | 4,570.00 USD | 28,070.00 USD |
| `7D` | `9.62` | 18,590,000.00 USD | 18,590,000.00 USD | 0.00 USD | 70,470.00 USD | 1,540.00 USD | 17,720.00 USD |
| `1D` | `9.63` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 17,350.00 USD | 4,370.00 USD | 4,650.00 USD |
| `7D` | `9.64` | 18,660,000.00 USD | 18,660,000.00 USD | 0.00 USD | 35,210.00 USD | 17,650.00 USD | 19,940.00 USD |
| `1D` | `9.65` | 6,390,000.00 USD | 6,390,000.00 USD | 0.00 USD | 11,050.00 USD | 5,210.00 USD | 5,130.00 USD |
| `7D` | `9.66` | 18,740,000.00 USD | 18,740,000.00 USD | 0.00 USD | 37,340.00 USD | 21,280.00 USD | 18,480.00 USD |
| `1D` | `9.67` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 11,920.00 USD | 3,480.00 USD | 8,060.00 USD |
| `7D` | `9.68` | 18,860,000.00 USD | 18,860,000.00 USD | 0.00 USD | 68,230.00 USD | 20,310.00 USD | 34,130.00 USD |
| `1D` | `9.69` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 21,130.00 USD | 5,660.00 USD | 3,970.00 USD |
| `7D` | `9.70` | 18,990,000.00 USD | 18,990,000.00 USD | 0.00 USD | 77,860.00 USD | 12,990.00 USD | 31,670.00 USD |
| `1D` | `9.71` | 6,480,000.00 USD | 6,480,000.00 USD | 0.00 USD | 11,360.00 USD | 9,310.00 USD | 8,590.00 USD |
| `7D` | `9.72` | 19,090,000.00 USD | 19,090,000.00 USD | 0.00 USD | 70,300.00 USD | 6,920.00 USD | 26,680.00 USD |
| `7D` | `9.74` | 19,140,000.00 USD | 19,140,000.00 USD | 0.00 USD | 21,230.00 USD | 7,200.00 USD | 19,560.00 USD |
| `7D` | `9.76` | 19,240,000.00 USD | 19,240,000.00 USD | 0.00 USD | 35,520.00 USD | 12,480.00 USD | 52,240.00 USD |
| `7D` | `9.78` | 19,320,000.00 USD | 19,320,000.00 USD | 0.00 USD | 65,390.00 USD | 10,300.00 USD | 5,270.00 USD |
| `7D` | `9.80` | 19,380,000.00 USD | 19,380,000.00 USD | 0.00 USD | 18,630.00 USD | 28,440.00 USD | 10,630.00 USD |
| `7D` | `9.82` | 19,610,000.00 USD | 19,610,000.00 USD | 0.00 USD | 121,860.00 USD | 27,860.00 USD | 86,290.00 USD |
| `7D` | `9.84` | 19,640,000.00 USD | 19,640,000.00 USD | 0.00 USD | 9,730.00 USD | 7,850.00 USD | 14,230.00 USD |
| `7D` | `9.86` | 19,780,000.00 USD | 19,780,000.00 USD | 0.00 USD | 58,130.00 USD | 2,210.00 USD | 71,950.00 USD |
| `7D` | `9.88` | 19,810,000.00 USD | 19,810,000.00 USD | 0.00 USD | 7,170.00 USD | 8,710.00 USD | 20,860.00 USD |
| `7D` | `9.90` | 19,900,000.00 USD | 19,900,000.00 USD | 0.00 USD | 55,970.00 USD | 19,700.00 USD | 14,360.00 USD |
| `7D` | `9.92` | 19,950,000.00 USD | 19,950,000.00 USD | 0.00 USD | 27,710.00 USD | 10,810.00 USD | 9,370.00 USD |
| `7D` | `9.94` | 20,070,000.00 USD | 20,070,000.00 USD | 0.00 USD | 69,320.00 USD | 11,150.00 USD | 39,810.00 USD |
| `7D` | `9.96` | 20,110,000.00 USD | 20,110,000.00 USD | 0.00 USD | 29,800.00 USD | 1,360.00 USD | 11,160.00 USD |
| `7D` | `9.98` | 20,140,000.00 USD | 20,140,000.00 USD | 0.00 USD | 840.10 USD | 4,150.00 USD | 18,990.00 USD |
| `7D` | `10.00` | 20,140,000.00 USD | 20,140,000.00 USD | 0.00 USD | 0.00 USD | 6,790.00 USD | 0.00 USD |
| `7D` | `10.02` | 20,170,000.00 USD | 20,170,000.00 USD | 0.00 USD | 16,100.00 USD | 3,650.00 USD | 5,890.00 USD |
| `7D` | `10.04` | 20,180,000.00 USD | 20,180,000.00 USD | 0.00 USD | 1,080.00 USD | 0.00 USD | 9,540.00 USD |
| `7D` | `10.06` | 20,200,000.00 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 3,480.00 USD | 17,230.00 USD |
| `7D` | `10.08` | 20,230,000.00 USD | 20,230,000.00 USD | 0.00 USD | 23,580.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `352.61M` | Total OI Tokens: `42,417,929.8 AVAX`
  * 1h OI Change: `-2.57%` | 4h OI Change: `-8.18%` | 24h OI Change: `-11.17%`
  * Exchange Breakdown: Binance=`81.86M` | Bybit=`55.54M` | OKX=`11.68M` | Hyperliquid=`16.48M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `231.52` | Last 24h: `33.77K` | Last 3d: `72.05K` | Last 7d: `92.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0002%` | **USDT OKX** | `0.0017%` |
| **USDT Bybit** | `0.0002%` | **USDT KuCoin** | `0.0012%` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `0.0021%` |
| **USDT Gate** | `-0.0069%` | **USDT Bitget** | `0.0011%` |
| **CoinM Binance** | `0.0068%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `44.20%` | `55.80%` | `0.79` | 26,540,000.00 USD |
| `15M` | `Binance` | `41.34%` | `58.66%` | `0.70` | 10,370,000.00 USD |
| `15M` | `OKX` | `47.08%` | `52.92%` | `0.89` | 2,380,000.00 USD |
| `15M` | `Bybit` | `45.66%` | `54.34%` | `0.84` | 2,000,000.00 USD |
| `15M` | `KuCoin` | `37.84%` | `62.16%` | `0.61` | 123,980.00 USD |
| `15M` | `Gate` | `44.37%` | `55.63%` | `0.80` | 413,950.00 USD |
| `15M` | `Bitget` | `37.54%` | `62.46%` | `0.60` | 1,200,000.00 USD |
| `15M` | `BingX` | `55.24%` | `44.76%` | `1.23` | 551,470.00 USD |
| `15M` | `MEXC` | `48.66%` | `51.34%` | `0.95` | 5,330,000.00 USD |
| `15M` | `Bitunix` | `45.01%` | `54.99%` | `0.82` | 1,630,000.00 USD |
| `15M` | `Hyperliquid` | `25.59%` | `74.41%` | `0.34` | 1,210,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.02%` | `53.98%` | `0.85` | 596,040.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `99.11%` | `0.89%` | `111.36` | 457,360.00 USD |
| `15M` | `HTX` | `34.73%` | `65.27%` | `0.53` | 3,830.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `24.5%` | `75.5%` | `0.32` | 174,060.00 USD |
| `15M` | `Aster` | `6.35%` | `93.65%` | `0.07` | 31,780.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `24.8%` | `75.2%` | `0.33` | 75,910.00 USD |
| `15M` | `Whale Positions` | `41.34%` | `58.66%` | `0.70` | 10,370,000.00 USD |
| `15M` | `Global Accounts` | `44.20%` | `55.80%` | `0.79` | 26,540,000.00 USD |
| `1H` | `AVAX` | `49.83%` | `50.17%` | `0.99` | 321,220,000.00 USD |
| `1H` | `Binance` | `51.86%` | `48.14%` | `1.08` | 128,220,000.00 USD |
| `1H` | `OKX` | `51.11%` | `48.89%` | `1.05` | 34,490,000.00 USD |
| `1H` | `Bybit` | `50.28%` | `49.72%` | `1.01` | 71,470,000.00 USD |
| `1H` | `KuCoin` | `55.74%` | `44.26%` | `1.26` | 1,590,000.00 USD |
| `1H` | `Gate` | `43.48%` | `56.52%` | `0.77` | 12,900,000.00 USD |
| `1H` | `Bitget` | `53.46%` | `46.54%` | `1.15` | 8,380,000.00 USD |
| `1H` | `BingX` | `43.93%` | `56.07%` | `0.78` | 4,270,000.00 USD |
| `1H` | `MEXC` | `42.43%` | `57.57%` | `0.74` | 4,770,000.00 USD |
| `1H` | `Bitunix` | `57.68%` | `42.32%` | `1.36` | 5,380,000.00 USD |
| `1H` | `Hyperliquid` | `51.38%` | `48.62%` | `1.06` | 17,640,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `55.61%` | `44.39%` | `1.25` | 6,260,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `28.79%` | `71.21%` | `0.40` | 19,640,000.00 USD |
| `1H` | `HTX` | `55.05%` | `44.95%` | `1.22` | 1,240,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `67.03%` | `32.97%` | `2.03` | 1,820,000.00 USD |
| `1H` | `Aster` | `66.43%` | `33.57%` | `1.98` | 1,840,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `54.89%` | `45.11%` | `1.22` | 1,330,000.00 USD |
| `1H` | `Whale Positions` | `51.86%` | `48.14%` | `1.08` | 128,220,000.00 USD |
| `1H` | `Global Accounts` | `49.83%` | `50.17%` | `0.99` | 321,220,000.00 USD |
| `4H` | `AVAX` | `46.34%` | `53.66%` | `0.86` | 268,850,000.00 USD |
| `4H` | `Binance` | `45.28%` | `54.72%` | `0.83` | 92,360,000.00 USD |
| `4H` | `OKX` | `48.86%` | `51.14%` | `0.96` | 30,250,000.00 USD |
| `4H` | `Bybit` | `44.74%` | `55.26%` | `0.81` | 25,970,000.00 USD |
| `4H` | `KuCoin` | `49.24%` | `50.76%` | `0.97` | 1,850,000.00 USD |
| `4H` | `Gate` | `46.77%` | `53.23%` | `0.88` | 3,460,000.00 USD |
| `4H` | `Bitget` | `45.08%` | `54.92%` | `0.82` | 11,220,000.00 USD |
| `4H` | `BingX` | `45.96%` | `54.04%` | `0.85` | 7,010,000.00 USD |
| `4H` | `MEXC` | `49.41%` | `50.59%` | `0.98` | 57,550,000.00 USD |
| `4H` | `Bitunix` | `45.87%` | `54.13%` | `0.85` | 11,180,000.00 USD |
| `4H` | `Hyperliquid` | `39.08%` | `60.92%` | `0.64` | 13,010,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.29%` | `49.71%` | `1.01` | 6,500,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `45%` | `55%` | `0.82` | 4,800,000.00 USD |
| `4H` | `HTX` | `43.57%` | `56.43%` | `0.77` | 152,760.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `44.37%` | `55.63%` | `0.80` | 2,020,000.00 USD |
| `4H` | `Aster` | `32.21%` | `67.79%` | `0.48` | 824,230.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `36.1%` | `63.9%` | `0.56` | 687,480.00 USD |
| `4H` | `Whale Positions` | `45.28%` | `54.72%` | `0.83` | 92,360,000.00 USD |
| `4H` | `Global Accounts` | `46.34%` | `53.66%` | `0.86` | 268,850,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `8.85` | `8.85` | `8.85` | `8.87` | `8.84` | 431,773.06 USD | 190,520.19 USD | 241,252.88 USD | -50,732.69 USD | `-11.75%` | `8B / 6S` |
| `0:00 UTC` | `8.73` | `8.73` | `8.73` | `8.86` | `8.66` | 5,568,654.06 USD | 2,589,240.15 USD | 2,979,413.92 USD | -390,173.77 USD | `-7.01%` | `5B / 25S` |
| `5:00 UTC` | `8.77` | `8.75` | `8.77` | `8.78` | `8.73` | 2,097,434.25 USD | 1,386,379.16 USD | 711,055.10 USD | 675,324.06 USD | `+32.20%` | `14B / 3S` |
| `0:00 UTC` | `8.61` | `8.53` | `8.61` | `8.76` | `8.39` | 13,163,243.09 USD | 4,547,421.99 USD | 8,615,821.10 USD | -4,068,399.10 USD | `-30.91%` | `4B / 57S` |
| `5:00 UTC` | `8.26` | `8.35` | `8.26` | `8.48` | `8.25` | 17,210,058.04 USD | 7,276,281.50 USD | 9,933,776.55 USD | -2,657,495.05 USD | `-15.44%` | `5B / 17S` |
| `0:00 UTC` | `8.44` | `8.39` | `8.44` | `8.47` | `8.31` | 5,735,994.33 USD | 3,091,126.19 USD | 2,644,868.14 USD | 446,258.06 USD | `+7.78%` | `31B / 8S` |
| `5:00 UTC` | `8.57` | `8.52` | `8.57` | `8.60` | `8.44` | 5,418,565.28 USD | 2,882,511.31 USD | 2,536,053.98 USD | 346,457.33 USD | `+6.39%` | `29B / 7S` |
| `0:00 UTC` | `8.49` | `8.53` | `8.49` | `8.57` | `8.47` | 2,187,831.94 USD | 1,148,223.68 USD | 1,039,608.27 USD | 108,615.41 USD | `+4.96%` | `15B / 18S` |
| `5:00 UTC` | `8.46` | `8.45` | `8.46` | `8.48` | `8.42` | 2,763,123.34 USD | 1,578,085.08 USD | 1,185,038.26 USD | 393,046.81 USD | `+14.22%` | `14B / 6S` |
| `0:00 UTC` | `8.38` | `8.39` | `8.38` | `8.45` | `8.32` | 5,876,949.58 USD | 3,723,399.54 USD | 2,153,550.04 USD | 1,569,849.50 USD | `+26.71%` | `26B / 5S` |

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
| `5m` | 110,520.00 USD | 1,470,000.00 USD | **`ACCUMULATION`** |
| `15m` | 197,560.00 USD | 1,080,000.00 USD | **`ACCUMULATION`** |
| `30m` | 258,580.00 USD | 1,450,000.00 USD | **`ACCUMULATION`** |
| `1h` | 61,640.00 USD | 2,150,000.00 USD | **`ACCUMULATION`** |
| `2h` | -1,600,000.00 USD | -4,090,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,870,000.00 USD | -4,720,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -2,160,000.00 USD | -8,950,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,620,000.00 USD | -7,700,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,000,000.00 USD | -7,550,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,690,000.00 USD | -10,970,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,850,000.00 USD | -47,860,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -55,800,000.00 USD | -274,530,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+110.52K` | 15m=`+197.56K` | 1h=`+61.64K` | 24h=`-1.69M`
* Futures Capital Netflows: 5m=`+1.47M` | 15m=`+1.08M` | 1h=`+2.15M` | 24h=`-10.97M`
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
  * `2026-10-30 03:29:57 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:57 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:40:57 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:41:57 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:41:57 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:57 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `8.29` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `8.13` (Risk Distance: `0.1641` pts)
  * +2.5R Take Profit: `8.70`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.47` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `8.63` (Risk Distance: `0.1641` pts)
  * +2.5R Take Profit: `8.06`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.43`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
