# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 22:36:53 IST` (`2026-10-29 17:06:53 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.92` | **Live Ask Quote**: `8.96` | **Mid Price**: `8.94`
- **Spread Points**: `4.00` | **Spread BPS**: `44.74 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.75` | VWAP Z-Score: `+1.42` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0571` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `59.89` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `9.13` | Lower -3.00σ Band: `8.37`
  * Upper +2.51σ Band: `9.07` | Lower -2.51σ Band: `8.43`
  * Upper +2.01σ Band: `9.00` | Lower -2.01σ Band: `8.50`
  * Upper +2.00σ Band: `9.00` | Lower -2.00σ Band: `8.50`
  * Upper +1.28σ Band: `8.91` | Lower -1.28σ Band: `8.59`
  * Upper +1.00σ Band: `8.88` | Lower -1.00σ Band: `8.62`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.93` | EMA-20=`8.87` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.81` (Slope: `+0.0000`) | EMA-100=`8.81`
  * Institutional Anchors: EMA-144=`8.82` | EMA-200=`8.82` (Slope: `+0.1336`) | EMA-233=`8.82`
- **Range Boundaries**: 24H High=`9.14` | 24H Low=`8.53` | Weekly High=`9.14` | Weekly Low=`8.53`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.89` (Distance: `+0.56%`)
  * Point of Control (POC) = `8.74` (Distance: `+2.23%`)
  * Value Area Low (VAL) = `8.54` (Distance: `+4.64%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
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
  * Golden Pocket Zone (0.618 - 0.650): `8.90` - `8.98`
  * Optimal Trade Entry (OTE 0.705): `8.96`
  * Structural Invalidation Anchor (0.786): `9.01`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.94` | `8.96` | `8.94` | `8.95` | `24,327` | 217,698.86 USD | -77,979.51 USD | `-35.82%` | -862,723.80 USD | `-0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `8.95` | `8.96` | `8.95` | `8.96` | `22,585` | 202,188.95 USD | -80,802.26 USD | `-39.96%` | -943,526.06 USD | `-0.17` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `8.96` | `8.96` | `8.94` | `8.94` | `25,811` | 231,076.40 USD | -58,953.72 USD | `-25.51%` | -1,002,479.78 USD | `-0.07` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `8.96` | `8.97` | `8.93` | `8.95` | `173,504` | 1,552,686.03 USD | -390,819.17 USD | `-25.17%` | -738,987.17 USD | `-1.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `8.95` | `8.96` | `8.93` | `8.96` | `87,893` | 786,504.93 USD | -344,377.23 USD | `-43.79%` | -1,083,364.40 USD | `-0.98` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `8.96` | `8.96` | `8.94` | `8.94` | `25,811` | 231,076.40 USD | -58,953.72 USD | `-25.51%` | -1,142,318.12 USD | `-0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `8.89` | `9.02` | `8.88` | `9.01` | `663,709` | 5,946,437.33 USD | 169,482.22 USD | `+2.85%` | -181,600.77 USD | `+0.45` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `9.01` | `9.08` | `8.93` | `8.96` | `840,436` | 7,558,281.78 USD | -1,066,050.82 USD | `-14.10%` | -1,247,651.59 USD | `-2.27` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `8.96` | `8.96` | `8.94` | `8.94` | `25,811` | 231,076.40 USD | -58,953.72 USD | `-25.51%` | -1,306,605.31 USD | `+0.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | -426,486.82 USD | `+0.25` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -480,308.79 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.93` | `8.94` | `866,693` | 7,793,346.70 USD | -1,128,993.06 USD | `-14.49%` | -1,609,301.85 USD | `-0.68` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `9.00` | `9.02` | `8.55` | `8.59` | `3,515,330` | 30,612,875.98 USD | -2,423,031.38 USD | `-7.92%` | -749,324.84 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.59` | `8.80` | `8.57` | `8.62` | `1,816,830` | 15,790,058.74 USD | 58,580.54 USD | `+0.37%` | -690,744.30 USD | `+0.17` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | -426,486.82 USD | `+0.25` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -480,308.79 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.93` | `8.94` | `866,693` | 7,793,346.70 USD | -1,128,993.06 USD | `-14.49%` | -1,609,301.85 USD | `-0.68` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`8.94`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `8.93` | `4.4700` | 39.94 USD | 49,582.82 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.93` | `5.5900` | 49.95 USD | 49,632.77 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.93` | `120.0800` | 1,072.88 USD | 50,705.65 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.93` | `4.4700` | 39.94 USD | 50,745.58 USD | `1 orders` | `-0.05%` | `-` |
| `ASK` | `8.94` | `56.5200` | 505.55 USD | 22,230.55 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.94` | `94.9000` | 848.83 USD | 21,725.00 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.94` | `235.1200` | 2,102.91 USD | 20,876.17 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `8.94` | `176.6000` | 1,579.49 USD | 18,773.25 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `8.94` | `138.2300` | 1,236.27 USD | 17,193.76 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.94` | `670.8900` | 6,000.10 USD | 15,957.49 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.94` | `527.3700` | 4,716.38 USD | 9,957.38 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `8.94` | `56.5200` | 505.44 USD | 5,241.01 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.94` | `126.1300` | 1,127.90 USD | 4,735.57 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.94` | `56.5200` | 505.40 USD | 3,607.66 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.94` | `56.5200` | 505.40 USD | 3,102.26 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.94` | `29.9900` | 268.15 USD | 2,596.86 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.94` | `56.5200` | 505.36 USD | 2,328.71 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.94` | `56.5200` | 505.32 USD | 1,823.36 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `8.94` | `147.4300` | 1,318.04 USD | 1,318.04 USD | `1 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `8.94` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.94` | `0.00%` | `-` |
| `BID` | `8.94` | `443.7700` | 3,966.55 USD | 3,966.55 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `8.94` | `671.2100` | 5,999.14 USD | 9,965.69 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.94` | `202.1900` | 1,807.11 USD | 11,772.80 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `8.94` | `42.3900` | 378.86 USD | 12,151.67 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.94` | `403.9300` | 3,610.12 USD | 15,761.79 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.94` | `42.3900` | 378.85 USD | 16,140.64 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.94` | `42.3900` | 378.84 USD | 16,519.48 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.94` | `57.6500` | 515.21 USD | 17,034.69 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `8.94` | `895.1700` | 7,999.51 USD | 25,034.20 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.94` | `173.7200` | 1,552.40 USD | 26,586.60 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.94` | `61.1600` | 546.53 USD | 27,133.12 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.94` | `56.5200` | 505.03 USD | 27,638.16 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.94` | `443.7700` | 3,965.26 USD | 31,603.42 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `8.94` | `118.1000` | 1,055.26 USD | 32,658.68 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `8.94` | `57.3100` | 512.07 USD | 33,170.75 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.94` | `1832.3600` | 16,372.14 USD | 49,542.88 USD | `3 orders` | `-0.05%` | `-` |
| `ASK` | `8.95` | `2438.6900` | 21,815.55 USD | 55,190.54 USD | `6 orders` | `+0.07%` | `-` |
| `ASK` | `8.95` | `78.7200` | 704.19 USD | 33,375.00 USD | `2 orders` | `+0.07%` | `-` |
| `ASK` | `8.95` | `211.0500` | 1,887.93 USD | 32,670.81 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.95` | `56.5200` | 505.59 USD | 30,782.88 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.95` | `899.5600` | 8,046.74 USD | 30,277.29 USD | `2 orders` | `+0.07%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:34:53 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1497` | `0x7737...bf66` | `SHORT` | 1,514,517.05 USD | `171,568.06` | `7.43` | `8.83` | `111.70` | -238,972.03 USD | `-15.78%` | `10X Cross` |
| `1582` | `0xeadc...9d55` | `LONG` | 1,413,294.99 USD | `160,070.56` | `8.11` | `8.83` | `0.000000` | 115,657.41 USD | `+8.18%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `8.87` | 13,481.68 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 13.48K USD at 8.8655 USD [API] | `2026-10-27 20:29:33` |
| `ANNOUNCEMENT` | `INFO` | `8.87` | 9,999.42 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 10.00K USD at 8.8656 USD [API] | `2026-10-27 20:29:33` |
| `ANNOUNCEMENT` | `INFO` | `8.94` | 5,181.55 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 5.18K USD at 8.9425 USD [API] | `2026-10-27 21:41:02` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`8.96` (Vol: 194,000.00 USD, Dist: `+1.37%`) | Long MP=`8.46` (Vol: 190,100.00 USD, Dist: `--4.33%`)
  * 48H Horizon: Short MP=`8.96` (Vol: 194,000.00 USD, Dist: `+1.37%`) | Long MP=`8.46` (Vol: 190,100.00 USD, Dist: `--4.33%`)
  * 3D Horizon: Short MP=`8.96` (Vol: 194,000.00 USD, Dist: `+1.37%`) | Long MP=`8.55` (Vol: 157,300.00 USD, Dist: `--3.28%`)
  * 7D Horizon: Short MP=`9.28` (Vol: 346,800.00 USD, Dist: `+4.99%`) | Long MP=`8.54` (Vol: 343,100.00 USD, Dist: `--3.44%`)
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
| `7D` | `Long Liquidation` | `7.74` | 8,640,000.00 USD | 8,640,000.00 USD | 976.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.75` | 893.76 USD | 469,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.76` | 8,640,000.00 USD | 8,640,000.00 USD | 812.95 USD | 5,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 468,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.78` | 695.32 USD | 468,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.78` | 8,630,000.00 USD | 8,630,000.00 USD | 23,430.00 USD | 4,900.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 3,900.00 USD | 467,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.79` | 1,940.00 USD | 463,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.80` | 8,580,000.00 USD | 8,580,000.00 USD | 13,050.00 USD | 12,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.80` | 633.77 USD | 461,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.82` | 5,280.00 USD | 461,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.82` | 8,550,000.00 USD | 8,550,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.84` | 8,540,000.00 USD | 8,540,000.00 USD | 29,020.00 USD | 2,380.00 USD | 19,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 10,930.00 USD | 455,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.85` | 4,180,000.00 USD | 4,180,000.00 USD | 4,700.00 USD | 1,820.00 USD | 8,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.86` | 2,110.00 USD | 445,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.86` | 4,170,000.00 USD | 4,170,000.00 USD | 10,180.00 USD | 424.36 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.86` | 8,490,000.00 USD | 8,490,000.00 USD | 25,770.00 USD | 5,460.00 USD | 17,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.87` | 4,150,000.00 USD | 4,150,000.00 USD | 13,300.00 USD | 2,670.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 442,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.88` | 4,120,000.00 USD | 4,120,000.00 USD | 16,020.00 USD | 4,370.00 USD | 4,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.88` | 8,440,000.00 USD | 8,440,000.00 USD | 46,450.00 USD | 12,780.00 USD | 29,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.89` | 4,090,000.00 USD | 4,090,000.00 USD | 5,220.00 USD | 4,150.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.90` | 4,080,000.00 USD | 4,080,000.00 USD | 9,200.00 USD | 3,480.00 USD | 5,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.90` | 8,350,000.00 USD | 8,350,000.00 USD | 33,680.00 USD | 12,890.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 2,410.00 USD | 442,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.91` | 4,060,000.00 USD | 4,060,000.00 USD | 2,990.00 USD | 0.00 USD | 2,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.92` | 4,060,000.00 USD | 4,060,000.00 USD | 12,900.00 USD | 2,950.00 USD | 3,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.92` | 8,290,000.00 USD | 8,290,000.00 USD | 53,660.00 USD | 8,420.00 USD | 14,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 923.42 USD | 439,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.93` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 831.98 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 1,820.00 USD | 439,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 4,040,000.00 USD | 4,040,000.00 USD | 11,450.00 USD | 3,900.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.94` | 8,210,000.00 USD | 8,210,000.00 USD | 38,370.00 USD | 9,960.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 127,110.00 USD | 437,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 1,420.00 USD | 2,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 12,180.00 USD | 310,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 4,020,000.00 USD | 4,020,000.00 USD | 8,450.00 USD | 2,280.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.96` | 8,130,000.00 USD | 8,130,000.00 USD | 21,840.00 USD | 4,820.00 USD | 26,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 229.31 USD | 297,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.97` | 4,000,000.00 USD | 4,000,000.00 USD | 11,690.00 USD | 5,500.00 USD | 10,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.98` | 3,970,000.00 USD | 3,970,000.00 USD | 10,080.00 USD | 1,760.00 USD | 548.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.98` | 8,080,000.00 USD | 8,080,000.00 USD | 42,740.00 USD | 19,680.00 USD | 70,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,600.00 USD | 297,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 3,960,000.00 USD | 3,960,000.00 USD | 9,190.00 USD | 2,180.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 210.99 USD | 296,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 3,950,000.00 USD | 3,950,000.00 USD | 2,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.00` | 7,950,000.00 USD | 7,950,000.00 USD | 61,850.00 USD | 10,300.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.01` | 3,940,000.00 USD | 3,940,000.00 USD | 6,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 3,940,000.00 USD | 3,940,000.00 USD | 2,230.00 USD | 770.83 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.02` | 7,870,000.00 USD | 7,870,000.00 USD | 20,050.00 USD | 28,440.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 957.70 USD | 295,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.03` | 3,930,000.00 USD | 3,930,000.00 USD | 8,800.00 USD | 0.00 USD | 4,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 88,380.00 USD | 294,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.04` | 3,920,000.00 USD | 3,920,000.00 USD | 3,240.00 USD | 0.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.04` | 7,810,000.00 USD | 7,810,000.00 USD | 94,150.00 USD | 23,930.00 USD | 75,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 6,890.00 USD | 206,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.05` | 3,910,000.00 USD | 3,910,000.00 USD | 3,700.00 USD | 1,790.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.05` | 3,340.00 USD | 199,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.06` | 3,900,000.00 USD | 3,900,000.00 USD | 7,120.00 USD | 0.00 USD | 2,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.06` | 7,620,000.00 USD | 7,620,000.00 USD | 69,980.00 USD | 10,070.00 USD | 78,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.06` | 37,830.00 USD | 196,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.07` | 3,890,000.00 USD | 3,890,000.00 USD | 944.98 USD | 0.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.08` | 3,890,000.00 USD | 3,890,000.00 USD | 769.07 USD | 269.63 USD | 3,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.08` | 7,460,000.00 USD | 7,460,000.00 USD | 7,170.00 USD | 3,650.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.09` | 617.61 USD | 158,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.09` | 3,880,000.00 USD | 3,880,000.00 USD | 6,700.00 USD | 1,220.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.10` | 3,870,000.00 USD | 3,870,000.00 USD | 23,830.00 USD | 1,620.00 USD | 6,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.10` | 7,430,000.00 USD | 7,430,000.00 USD | 61,140.00 USD | 19,700.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.11` | 3,840,000.00 USD | 3,840,000.00 USD | 144.37 USD | 1,980.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 241.26 USD | 157,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.12` | 3,840,000.00 USD | 3,840,000.00 USD | 3,730.00 USD | 0.00 USD | 5,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.12` | 7,330,000.00 USD | 7,330,000.00 USD | 27,150.00 USD | 10,810.00 USD | 9,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.13` | 3,830,000.00 USD | 3,830,000.00 USD | 4,140.00 USD | 693.45 USD | 1,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 3,820,000.00 USD | 3,820,000.00 USD | 8,480.00 USD | 0.00 USD | 26.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.14` | 7,290,000.00 USD | 7,290,000.00 USD | 57,880.00 USD | 11,150.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.15` | 3,810,000.00 USD | 3,810,000.00 USD | 11,200.00 USD | 662.47 USD | 4,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.16` | 3,790,000.00 USD | 3,790,000.00 USD | 385.98 USD | 2,120.00 USD | 47.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.16` | 7,180,000.00 USD | 7,180,000.00 USD | 38,430.00 USD | 5,510.00 USD | 30,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.16` | 871.61 USD | 157,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.17` | 3,790,000.00 USD | 3,790,000.00 USD | 2,970.00 USD | 0.00 USD | 12.32 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.18` | 3,790,000.00 USD | 3,790,000.00 USD | 1,150.00 USD | 1,980.00 USD | 466.21 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.18` | 7,100,000.00 USD | 7,100,000.00 USD | 19,550.00 USD | 6,790.00 USD | 2,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.19` | 4,030.00 USD | 156,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.19` | 3,790,000.00 USD | 3,790,000.00 USD | 4,850.00 USD | 0.00 USD | 48.71 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.20` | 2,380.00 USD | 152,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.20` | 3,780,000.00 USD | 3,780,000.00 USD | 7,720.00 USD | 2,310.00 USD | 431.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.20` | 7,070,000.00 USD | 7,070,000.00 USD | 63,560.00 USD | 0.00 USD | 16,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 577.06 USD | 150,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.21` | 3,770,000.00 USD | 3,770,000.00 USD | 1,880.00 USD | 0.00 USD | 46.18 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 6,220.00 USD | 149,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.22` | 3,770,000.00 USD | 3,770,000.00 USD | 5,330.00 USD | 0.00 USD | 12,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.22` | 6,990,000.00 USD | 6,990,000.00 USD | 35,730.00 USD | 0.00 USD | 26,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.22` | 2,100.00 USD | 143,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.23` | 3,750,000.00 USD | 3,750,000.00 USD | 20,950.00 USD | 4,080.00 USD | 31,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.23` | 1,160.00 USD | 141,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.24` | 3,690,000.00 USD | 3,690,000.00 USD | 10,020.00 USD | 1,150.00 USD | 3,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.24` | 6,930,000.00 USD | 6,930,000.00 USD | 39,950.00 USD | 3,480.00 USD | 107,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.24` | 1,120.00 USD | 140,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.25` | 3,680,000.00 USD | 3,680,000.00 USD | 8,710.00 USD | 0.00 USD | 6,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.26` | 13,810.00 USD | 139,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.26` | 3,660,000.00 USD | 3,660,000.00 USD | 192.60 USD | 11,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.26` | 6,780,000.00 USD | 6,780,000.00 USD | 29,800.00 USD | 5,750.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.27` | 3,650,000.00 USD | 3,650,000.00 USD | 11,800.00 USD | 2,760.00 USD | 36.54 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.28` | 3,360.00 USD | 125,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.28` | 3,640,000.00 USD | 3,640,000.00 USD | 74,980.00 USD | 7,070.00 USD | 40,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.28` | 6,740,000.00 USD | 6,740,000.00 USD | 122,850.00 USD | 33,920.00 USD | 14,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.29` | 498.26 USD | 121,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.29` | 3,520,000.00 USD | 3,520,000.00 USD | 34,940.00 USD | 9,470.00 USD | 4,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.29` | 23,710.00 USD | 121,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.30` | 3,470,000.00 USD | 3,470,000.00 USD | 52,980.00 USD | 13,130.00 USD | 19,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.30` | 6,570,000.00 USD | 6,570,000.00 USD | 101,180.00 USD | 13,500.00 USD | 47,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.30` | 33,500.00 USD | 97,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.31` | 3,380,000.00 USD | 3,380,000.00 USD | 55,700.00 USD | 11,410.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.31` | 4,550.00 USD | 64,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.32` | 3,310,000.00 USD | 3,310,000.00 USD | 19,320.00 USD | 4,190.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.32` | 6,400,000.00 USD | 6,400,000.00 USD | 61,070.00 USD | 26,020.00 USD | 4,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.33` | 3,280,000.00 USD | 3,280,000.00 USD | 2,670.00 USD | 22,580.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.34` | 4,630.00 USD | 59,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.34` | 3,250,000.00 USD | 3,250,000.00 USD | 14,430.00 USD | 4,810.00 USD | 6,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.34` | 6,310,000.00 USD | 6,310,000.00 USD | 36,960.00 USD | 15,520.00 USD | 30,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.35` | 3,220,000.00 USD | 3,220,000.00 USD | 6,060.00 USD | 11,270.00 USD | 16,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.36` | 3,180.00 USD | 55,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.36` | 3,190,000.00 USD | 3,190,000.00 USD | 3,900.00 USD | 2,420.00 USD | 21,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.36` | 6,230,000.00 USD | 6,230,000.00 USD | 107,010.00 USD | 13,470.00 USD | 71,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.37` | 7,160.00 USD | 51,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.37` | 3,160,000.00 USD | 3,160,000.00 USD | 21,620.00 USD | 7,980.00 USD | 8,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.38` | 670.00 USD | 44,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.38` | 3,120,000.00 USD | 3,120,000.00 USD | 36,180.00 USD | 4,080.00 USD | 33,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.38` | 6,040,000.00 USD | 6,040,000.00 USD | 143,540.00 USD | 20,560.00 USD | 66,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.39` | 3,050,000.00 USD | 3,050,000.00 USD | 62,830.00 USD | 10,540.00 USD | 56,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.39` | 1,680.00 USD | 44,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.40` | 2,920,000.00 USD | 2,920,000.00 USD | 68,490.00 USD | 22,890.00 USD | 67,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.40` | 5,810,000.00 USD | 5,810,000.00 USD | 149,520.00 USD | 19,710.00 USD | 220,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.40` | 832.52 USD | 42,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.41` | 2,760,000.00 USD | 2,760,000.00 USD | 33,190.00 USD | 3,620.00 USD | 20,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.42` | 2,700,000.00 USD | 2,700,000.00 USD | 33,460.00 USD | 12,790.00 USD | 18,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.42` | 5,420,000.00 USD | 5,420,000.00 USD | 176,550.00 USD | 57,340.00 USD | 72,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.43` | 2,640,000.00 USD | 2,640,000.00 USD | 30,620.00 USD | 34,530.00 USD | 14,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.44` | 188.61 USD | 41,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.44` | 2,560,000.00 USD | 2,560,000.00 USD | 35,960.00 USD | 8,900.00 USD | 7,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.44` | 5,110,000.00 USD | 5,110,000.00 USD | 155,040.00 USD | 68,350.00 USD | 76,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.45` | 588.70 USD | 41,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.45` | 2,500,000.00 USD | 2,500,000.00 USD | 72,750.00 USD | 14,270.00 USD | 45,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.46` | 4,100.00 USD | 40,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.46` | 2,370,000.00 USD | 2,370,000.00 USD | 138,660.00 USD | 13,720.00 USD | 49,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.46` | 4,810,000.00 USD | 4,810,000.00 USD | 391,750.00 USD | 59,170.00 USD | 107,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.46` | 1,970.00 USD | 36,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.47` | 2,170,000.00 USD | 2,170,000.00 USD | 111,460.00 USD | 29,440.00 USD | 22,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.47` | 14,370.00 USD | 34,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.48` | 2,010,000.00 USD | 2,010,000.00 USD | 115,230.00 USD | 32,510.00 USD | 47,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.48` | 4,250,000.00 USD | 4,250,000.00 USD | 306,870.00 USD | 56,420.00 USD | 220,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.48` | 1,160.00 USD | 20,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.49` | 1,810,000.00 USD | 1,810,000.00 USD | 130,130.00 USD | 29,970.00 USD | 21,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.49` | 870.23 USD | 19,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.50` | 1,630,000.00 USD | 1,630,000.00 USD | 46,010.00 USD | 19,260.00 USD | 21,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.50` | 3,670,000.00 USD | 3,670,000.00 USD | 180,050.00 USD | 87,640.00 USD | 112,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.51` | 6,380.00 USD | 18,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.51` | 1,540,000.00 USD | 1,540,000.00 USD | 55,990.00 USD | 54,280.00 USD | 43,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.52` | 2,640.00 USD | 2,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.52` | 1,390,000.00 USD | 1,390,000.00 USD | 79,750.00 USD | 22,420.00 USD | 17,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.52` | 3,290,000.00 USD | 3,290,000.00 USD | 255,070.00 USD | 92,530.00 USD | 239,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.53` | 1,270,000.00 USD | 1,270,000.00 USD | 16,630.00 USD | 23,780.00 USD | 32,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 6,350.00 USD | 11,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.54` | 1,200,000.00 USD | 1,200,000.00 USD | 18,880.00 USD | 6,040.00 USD | 43,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.54` | 2,700,000.00 USD | 2,700,000.00 USD | 378,750.00 USD | 78,380.00 USD | 152,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 1,550.00 USD | 5,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.55` | 1,130,000.00 USD | 1,130,000.00 USD | 42,130.00 USD | 17,890.00 USD | 16,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.55` | 1,060.00 USD | 4,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.56` | 1,050,000.00 USD | 1,050,000.00 USD | 69,420.00 USD | 8,150.00 USD | 67,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.56` | 2,090,000.00 USD | 2,090,000.00 USD | 520,060.00 USD | 91,230.00 USD | 60,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.57` | 907,360.00 USD | 907,360.00 USD | 56,370.00 USD | 7,000.00 USD | 55,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.58` | 788,340.00 USD | 788,340.00 USD | 48,420.00 USD | 13,910.00 USD | 39,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.58` | 1,420,000.00 USD | 1,420,000.00 USD | 527,760.00 USD | 164,810.00 USD | 34,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.59` | 686,110.00 USD | 686,110.00 USD | 43,310.00 USD | 25,580.00 USD | 12,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.60` | 604,660.00 USD | 604,660.00 USD | 58,480.00 USD | 23,230.00 USD | 34,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.60` | 693,950.00 USD | 693,950.00 USD | 75,040.00 USD | 39,160.00 USD | 176,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.61` | 2,980.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.61` | 488,290.00 USD | 488,290.00 USD | 28,830.00 USD | 6,770.00 USD | 30,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.62` | 421,840.00 USD | 421,840.00 USD | 87,140.00 USD | 14,760.00 USD | 19,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.62` | 402,980.00 USD | 402,980.00 USD | 0.00 USD | 26,800.00 USD | 78,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.63` | 300,110.00 USD | 300,110.00 USD | 24,730.00 USD | 2,010.00 USD | 3,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.64` | 269,530.00 USD | 269,530.00 USD | 64,480.00 USD | 1,540.00 USD | 3,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.64` | 297,450.00 USD | 297,450.00 USD | 73,980.00 USD | 5,680.00 USD | 58.11 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.65` | 200,340.00 USD | 200,340.00 USD | 18,440.00 USD | 7,110.00 USD | 12,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.66` | 217,730.00 USD | 217,730.00 USD | 0.00 USD | 6,040.00 USD | 37,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.68` | 162,510.00 USD | 162,510.00 USD | 0.00 USD | 0.00 USD | 56.84 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.68` | 173,790.00 USD | 173,790.00 USD | 0.00 USD | 0.00 USD | 173,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.82` | 118.36 USD | 118.36 USD | 0.00 USD | 0.00 USD | 118.36 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.84` | 162,460.00 USD | 162,460.00 USD | 97,740.00 USD | 16,450.00 USD | 48,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.85` | 74,760.00 USD | 74,760.00 USD | 0.00 USD | 48,620.00 USD | 26,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.85` | 149,520.00 USD | 149,520.00 USD | 0.00 USD | 48,620.00 USD | 26,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 199,380.00 USD | 199,380.00 USD | 25,310.00 USD | 12,040.00 USD | 12,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.86` | 119,780.00 USD | 119,780.00 USD | 119,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.87` | 297,400.00 USD | 297,400.00 USD | 9,410.00 USD | 22,550.00 USD | 66,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.88` | 350,360.00 USD | 350,360.00 USD | 4,550.00 USD | 4,830.00 USD | 43,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.88` | 202,910.00 USD | 202,910.00 USD | 0.00 USD | 4,350.00 USD | 78,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.89` | 423,710.00 USD | 423,710.00 USD | 40,760.00 USD | 15,970.00 USD | 16,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.90` | 582,870.00 USD | 582,870.00 USD | 73,240.00 USD | 8,150.00 USD | 77,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.90` | 532,330.00 USD | 532,330.00 USD | 159,560.00 USD | 54,390.00 USD | 115,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.91` | 842,000.00 USD | 842,000.00 USD | 130,250.00 USD | 25,170.00 USD | 103,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 854,710.00 USD | 854,710.00 USD | 8,060.00 USD | 1,150.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.92` | 648,960.00 USD | 648,960.00 USD | 19,230.00 USD | 7,700.00 USD | 89,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.93` | 969,640.00 USD | 969,640.00 USD | 55,830.00 USD | 40,980.00 USD | 18,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.94` | 1,050,000.00 USD | 1,050,000.00 USD | 34,120.00 USD | 14,100.00 USD | 27,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.94` | 774,510.00 USD | 774,510.00 USD | 60,190.00 USD | 32,050.00 USD | 33,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.95` | 1,150,000.00 USD | 1,150,000.00 USD | 53,880.00 USD | 28,330.00 USD | 25,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.96` | 1,300,000.00 USD | 1,300,000.00 USD | 73,070.00 USD | 26,680.00 USD | 46,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.96` | 1,040,000.00 USD | 1,040,000.00 USD | 158,650.00 USD | 92,290.00 USD | 12,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.97` | 1,350,000.00 USD | 1,350,000.00 USD | 28,830.00 USD | 6,770.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.98` | 1,550,000.00 USD | 1,550,000.00 USD | 147,050.00 USD | 18,380.00 USD | 42,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.98` | 1,180,000.00 USD | 1,180,000.00 USD | 61,300.00 USD | 39,050.00 USD | 38,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 1,630,000.00 USD | 1,630,000.00 USD | 59,440.00 USD | 11,480.00 USD | 8,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.00` | 1,810,000.00 USD | 1,810,000.00 USD | 116,720.00 USD | 31,900.00 USD | 30,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.00` | 1,400,000.00 USD | 1,400,000.00 USD | 161,560.00 USD | 17,050.00 USD | 46,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 1,920,000.00 USD | 1,920,000.00 USD | 74,700.00 USD | 18,520.00 USD | 13,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 1,950,000.00 USD | 1,950,000.00 USD | 18,000.00 USD | 4,190.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.02` | 1,520,000.00 USD | 1,520,000.00 USD | 31,620.00 USD | 45,640.00 USD | 36,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 2,020,000.00 USD | 2,020,000.00 USD | 2,970.00 USD | 44,330.00 USD | 22,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 2,110,000.00 USD | 2,110,000.00 USD | 24,830.00 USD | 4,810.00 USD | 54,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.04` | 1,580,000.00 USD | 1,580,000.00 USD | 1,950.00 USD | 49,890.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 2,150,000.00 USD | 2,150,000.00 USD | 8,220.00 USD | 20,830.00 USD | 16,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.06` | 2,200,000.00 USD | 2,200,000.00 USD | 3,490.00 USD | 16,550.00 USD | 22,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.06` | 1,780,000.00 USD | 1,780,000.00 USD | 181,600.00 USD | 2,170.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.07` | 2,240,000.00 USD | 2,240,000.00 USD | 21,880.00 USD | 10,450.00 USD | 8,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 2,340,000.00 USD | 2,340,000.00 USD | 63,740.00 USD | 6,490.00 USD | 33,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.08` | 2,000,000.00 USD | 2,000,000.00 USD | 142,630.00 USD | 11,960.00 USD | 65,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 2,450,000.00 USD | 2,450,000.00 USD | 54,960.00 USD | 14,400.00 USD | 36,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.10` | 2,550,000.00 USD | 2,550,000.00 USD | 66,840.00 USD | 14,720.00 USD | 26,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.10` | 2,940,000.00 USD | 2,940,000.00 USD | 652,680.00 USD | 16,080.00 USD | 268,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.11` | 2,590,000.00 USD | 2,590,000.00 USD | 19,700.00 USD | 1,320.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 2,640,000.00 USD | 2,640,000.00 USD | 28,220.00 USD | 16,570.00 USD | 6,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.12` | 3,880,000.00 USD | 3,880,000.00 USD | 463,210.00 USD | 24,170.00 USD | 457,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 2,700,000.00 USD | 2,700,000.00 USD | 29,720.00 USD | 11,620.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.13` | 314.34 USD | 2,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.14` | 2,740,000.00 USD | 2,740,000.00 USD | 14,660.00 USD | 8,440.00 USD | 17,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.14` | 4,860,000.00 USD | 4,860,000.00 USD | 536,560.00 USD | 18,540.00 USD | 420,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.15` | 2,810,000.00 USD | 2,810,000.00 USD | 44,870.00 USD | 7,380.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 2,850,000.00 USD | 2,850,000.00 USD | 12,360.00 USD | 9,170.00 USD | 22,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.16` | 5,400,000.00 USD | 5,400,000.00 USD | 331,010.00 USD | 10,610.00 USD | 195,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 2,990,000.00 USD | 2,990,000.00 USD | 71,740.00 USD | 18,120.00 USD | 51,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 3,190,000.00 USD | 3,190,000.00 USD | 132,750.00 USD | 19,990.00 USD | 43,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.18` | 6,290,000.00 USD | 6,290,000.00 USD | 494,640.00 USD | 157,220.00 USD | 242,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 3,300,000.00 USD | 3,300,000.00 USD | 66,110.00 USD | 22,640.00 USD | 25,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.20` | 3,430,000.00 USD | 3,430,000.00 USD | 72,570.00 USD | 18,950.00 USD | 40,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.20` | 7,150,000.00 USD | 7,150,000.00 USD | 509,140.00 USD | 107,650.00 USD | 238,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 3,550,000.00 USD | 3,550,000.00 USD | 72,580.00 USD | 12,590.00 USD | 30,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.22` | 3,630,000.00 USD | 3,630,000.00 USD | 71,070.00 USD | 8,140.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.22` | 8,180,000.00 USD | 8,180,000.00 USD | 495,210.00 USD | 134,000.00 USD | 405,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.23` | 3,730,000.00 USD | 3,730,000.00 USD | 57,020.00 USD | 3,310.00 USD | 33,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 3,760,000.00 USD | 3,760,000.00 USD | 26,080.00 USD | 8,310.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.24` | 8,730,000.00 USD | 8,730,000.00 USD | 316,220.00 USD | 52,090.00 USD | 174,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 3,780,000.00 USD | 3,780,000.00 USD | 7,640.00 USD | 11,850.00 USD | 22.09 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 3,800,000.00 USD | 3,800,000.00 USD | 16,290.00 USD | 1,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.26` | 9,160,000.00 USD | 9,160,000.00 USD | 273,920.00 USD | 96,980.00 USD | 60,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 3,810,000.00 USD | 3,810,000.00 USD | 144.37 USD | 11,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 3,840,000.00 USD | 3,840,000.00 USD | 21,090.00 USD | 0.00 USD | 10,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.28` | 9,840,000.00 USD | 9,840,000.00 USD | 451,410.00 USD | 93,640.00 USD | 142,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 100.93 USD | 3,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.29` | 3,900,000.00 USD | 3,900,000.00 USD | 32,900.00 USD | 14,120.00 USD | 13,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.30` | 3,940,000.00 USD | 3,940,000.00 USD | 19,890.00 USD | 8,530.00 USD | 6,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.30` | 10,590,000.00 USD | 10,590,000.00 USD | 314,150.00 USD | 97,780.00 USD | 335,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 3,970,000.00 USD | 3,970,000.00 USD | 13,100.00 USD | 0.00 USD | 12,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 3,970,000.00 USD | 3,970,000.00 USD | 387.00 USD | 2,530.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.32` | 11,230,000.00 USD | 11,230,000.00 USD | 271,660.00 USD | 59,310.00 USD | 308,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 4,000,000.00 USD | 4,000,000.00 USD | 9,850.00 USD | 0.00 USD | 15,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 4,010,000.00 USD | 4,010,000.00 USD | 385.98 USD | 1,350.00 USD | 9,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.34` | 11,590,000.00 USD | 11,590,000.00 USD | 189,770.00 USD | 36,270.00 USD | 129,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.35` | 4,570.00 USD | 7,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.35` | 4,050,000.00 USD | 4,050,000.00 USD | 15,350.00 USD | 3,810.00 USD | 19,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 4,140,000.00 USD | 4,140,000.00 USD | 61,640.00 USD | 6,870.00 USD | 17,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.36` | 12,010,000.00 USD | 12,010,000.00 USD | 245,070.00 USD | 78,550.00 USD | 101,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 4,170,000.00 USD | 4,170,000.00 USD | 26,010.00 USD | 7,740.00 USD | 3,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 4,230,000.00 USD | 4,230,000.00 USD | 32,400.00 USD | 4,040.00 USD | 16,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.38` | 12,540,000.00 USD | 12,540,000.00 USD | 383,530.00 USD | 55,400.00 USD | 85,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.38` | 404,120.00 USD | 411,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.39` | 4,240,000.00 USD | 4,240,000.00 USD | 8,200.00 USD | 1,730.00 USD | 3,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.40` | 4,260,000.00 USD | 4,260,000.00 USD | 22,280.00 USD | 1,210.00 USD | 12.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.40` | 12,940,000.00 USD | 12,940,000.00 USD | 196,230.00 USD | 58,130.00 USD | 152,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.41` | 4,310,000.00 USD | 4,310,000.00 USD | 29,870.00 USD | 1,660.00 USD | 16,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 2,470.00 USD | 414,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 4,320,000.00 USD | 4,320,000.00 USD | 1,520.00 USD | 622.99 USD | 4,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.42` | 13,250,000.00 USD | 13,250,000.00 USD | 176,920.00 USD | 44,410.00 USD | 84,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.43` | 4,340,000.00 USD | 4,340,000.00 USD | 5,840.00 USD | 6,940.00 USD | 12,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 4,340,000.00 USD | 4,340,000.00 USD | 992.05 USD | 0.00 USD | 48.84 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.44` | 13,390,000.00 USD | 13,390,000.00 USD | 62,040.00 USD | 19,420.00 USD | 56,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.45` | 4,350,000.00 USD | 4,350,000.00 USD | 1,860.00 USD | 4,940.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.46` | 5,040.00 USD | 419,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.46` | 4,360,000.00 USD | 4,360,000.00 USD | 1,800.00 USD | 4,580.00 USD | 21.27 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.46` | 13,620,000.00 USD | 13,620,000.00 USD | 183,340.00 USD | 32,490.00 USD | 19,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.47` | 4,380,000.00 USD | 4,380,000.00 USD | 17,460.00 USD | 6,870.00 USD | 192.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.48` | 4,390,000.00 USD | 4,390,000.00 USD | 1,510.00 USD | 0.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.48` | 13,800,000.00 USD | 13,800,000.00 USD | 76,510.00 USD | 37,930.00 USD | 67,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.49` | 4,420,000.00 USD | 4,420,000.00 USD | 20,880.00 USD | 572.85 USD | 5,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.50` | 4,440,000.00 USD | 4,440,000.00 USD | 11,770.00 USD | 3,160.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.50` | 14,040,000.00 USD | 14,040,000.00 USD | 94,930.00 USD | 33,210.00 USD | 103,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.52` | 4,460,000.00 USD | 4,460,000.00 USD | 17,120.00 USD | 3,070.00 USD | 5,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.52` | 14,230,000.00 USD | 14,230,000.00 USD | 103,000.00 USD | 29,320.00 USD | 66,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.53` | 4,490,000.00 USD | 4,490,000.00 USD | 18,480.00 USD | 4,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.54` | 4,500,000.00 USD | 4,500,000.00 USD | 5,310.00 USD | 1,470.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.54` | 14,470,000.00 USD | 14,470,000.00 USD | 192,230.00 USD | 27,650.00 USD | 15,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.55` | 4,510,000.00 USD | 4,510,000.00 USD | 2,170.00 USD | 6,330.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.56` | 4,520,000.00 USD | 4,520,000.00 USD | 5,160.00 USD | 1,280.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.56` | 14,600,000.00 USD | 14,600,000.00 USD | 89,520.00 USD | 5,260.00 USD | 32,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.57` | 4,530,000.00 USD | 4,530,000.00 USD | 1,020.00 USD | 3,100.00 USD | 4,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.58` | 4,540,000.00 USD | 4,540,000.00 USD | 1,290.00 USD | 563.17 USD | 7,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.58` | 14,680,000.00 USD | 14,680,000.00 USD | 38,860.00 USD | 16,980.00 USD | 21,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.59` | 4,540,000.00 USD | 4,540,000.00 USD | 4,670.00 USD | 1,250.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.60` | 4,570,000.00 USD | 4,570,000.00 USD | 11,210.00 USD | 424.36 USD | 11,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.60` | 14,760,000.00 USD | 14,760,000.00 USD | 38,650.00 USD | 10,820.00 USD | 33,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.61` | 4,590,000.00 USD | 4,590,000.00 USD | 13,300.00 USD | 2,670.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.62` | 4,590,000.00 USD | 4,590,000.00 USD | 675.26 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.62` | 14,860,000.00 USD | 14,860,000.00 USD | 69,630.00 USD | 13,850.00 USD | 17,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.63` | 4,610,000.00 USD | 4,610,000.00 USD | 10,190.00 USD | 4,370.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.64` | 4,620,000.00 USD | 4,620,000.00 USD | 5,830.00 USD | 0.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.64` | 14,960,000.00 USD | 14,960,000.00 USD | 61,870.00 USD | 17,650.00 USD | 19,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.65` | 4,630,000.00 USD | 4,630,000.00 USD | 5,960.00 USD | 4,150.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.66` | 4,650,000.00 USD | 4,650,000.00 USD | 9,200.00 USD | 3,480.00 USD | 5,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.66` | 15,040,000.00 USD | 15,040,000.00 USD | 37,340.00 USD | 21,280.00 USD | 18,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.67` | 4,650,000.00 USD | 4,650,000.00 USD | 2,990.00 USD | 0.00 USD | 2,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.68` | 4,670,000.00 USD | 4,670,000.00 USD | 12,900.00 USD | 2,950.00 USD | 3,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.68` | 15,160,000.00 USD | 15,160,000.00 USD | 69,470.00 USD | 20,310.00 USD | 34,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.69` | 545.17 USD | 419,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.69` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 831.98 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.70` | 466.33 USD | 420,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.70` | 4,700,000.00 USD | 4,700,000.00 USD | 11,450.00 USD | 3,900.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.70` | 15,270,000.00 USD | 15,270,000.00 USD | 69,750.00 USD | 12,990.00 USD | 31,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.71` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 1,420.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.72` | 4,720,000.00 USD | 4,720,000.00 USD | 8,450.00 USD | 2,280.00 USD | 6,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.72` | 15,380,000.00 USD | 15,380,000.00 USD | 74,210.00 USD | 4,820.00 USD | 26,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 420,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.74` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 3,560.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.74` | 15,420,000.00 USD | 15,420,000.00 USD | 11,450.00 USD | 7,200.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.75` | 4,740,000.00 USD | 4,740,000.00 USD | 11,500.00 USD | 1,940.00 USD | 7,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.76` | 4,750,000.00 USD | 4,750,000.00 USD | 9,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.76` | 15,510,000.00 USD | 15,510,000.00 USD | 31,950.00 USD | 12,480.00 USD | 51,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.77` | 15,550,000.00 USD | 15,550,000.00 USD | 28,630.00 USD | 3,270.00 USD | 4,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.04` | 263.92 USD | 420,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long` | `1.86` | 2,320,000.00 USD | 0.00 USD | 205.15 USD | `-79.17%` | `110.00` |
| `Live` | `Long` | `1.93` | 2,320,000.00 USD | 0.00 USD | 313.47 USD | `-78.50%` | `162.84` |
| `Live` | `Long` | `2.00` | 2,320,000.00 USD | 0.00 USD | 159.60 USD | `-77.71%` | `80.00` |
| `Live` | `Long` | `2.04` | 2,320,000.00 USD | 0.00 USD | 110.52 USD | `-77.27%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,320,000.00 USD | 0.00 USD | 5,130.00 USD | `-76.93%` | `2,486.49` |
| `Live` | `Long` | `2.15` | 2,310,000.00 USD | 0.00 USD | 670.96 USD | `-75.93%` | `311.35` |
| `Live` | `Long` | `2.21` | 2,310,000.00 USD | 0.00 USD | 15,410.00 USD | `-75.37%` | `6,990.57` |
| `Live` | `Long` | `2.33` | 2,290,000.00 USD | 0.00 USD | 256.85 USD | `-73.92%` | `110.00` |
| `Live` | `Long` | `2.42` | 2,290,000.00 USD | 0.00 USD | 814.80 USD | `-72.91%` | `336.00` |
| `Live` | `Long` | `2.48` | 2,290,000.00 USD | 0.00 USD | 534.35 USD | `-72.24%` | `215.03` |
| `Live` | `Long` | `2.71` | 2,290,000.00 USD | 0.00 USD | 1,540.00 USD | `-69.78%` | `568.43` |
| `Live` | `Long` | `2.77` | 2,290,000.00 USD | 0.00 USD | 1,050.00 USD | `-69.00%` | `377.71` |
| `Live` | `Long` | `2.87` | 2,290,000.00 USD | 0.00 USD | 232.67 USD | `-68.00%` | `81.21` |
| `Live` | `Long` | `2.94` | 2,290,000.00 USD | 0.00 USD | 44,510.00 USD | `-67.21%` | `15,165.76` |
| `Live` | `Long` | `2.98` | 2,240,000.00 USD | 0.00 USD | 111.12 USD | `-66.77%` | `37.35` |
| `Live` | `Long` | `3.06` | 2,240,000.00 USD | 0.00 USD | 132.01 USD | `-65.76%` | `43.07` |
| `Live` | `Long` | `3.23` | 2,240,000.00 USD | 0.00 USD | 404.38 USD | `-63.86%` | `125.00` |
| `Live` | `Long` | `3.37` | 2,240,000.00 USD | 0.00 USD | 389.53 USD | `-62.41%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,240,000.00 USD | 0.00 USD | 151.88 USD | `-62.30%` | `45.00` |
| `Live` | `Long` | `3.38` | 2,240,000.00 USD | 0.00 USD | 7,700.00 USD | `-62.19%` | `2,273.34` |
| `Live` | `Long` | `3.40` | 2,240,000.00 USD | 0.00 USD | 1,600.00 USD | `-61.96%` | `470.82` |
| `Live` | `Long` | `3.58` | 2,230,000.00 USD | 0.00 USD | 835.12 USD | `-60.07%` | `233.60` |
| `Live` | `Long` | `3.67` | 2,230,000.00 USD | 0.00 USD | 109.95 USD | `-59.06%` | `30.00` |
| `Live` | `Long` | `3.69` | 2,230,000.00 USD | 0.00 USD | 177.69 USD | `-58.84%` | `48.22` |
| `Live` | `Long` | `3.75` | 2,230,000.00 USD | 0.00 USD | 3,600.00 USD | `-58.05%` | `958.69` |
| `Live` | `Long` | `3.81` | 2,230,000.00 USD | 0.00 USD | 356.02 USD | `-57.38%` | `93.32` |
| `Live` | `Long` | `3.88` | 2,230,000.00 USD | 0.00 USD | 387.50 USD | `-56.71%` | `100.00` |
| `Live` | `Long` | `3.90` | 2,230,000.00 USD | 0.00 USD | 131.73 USD | `-56.49%` | `33.82` |
| `Live` | `Long` | `4.00` | 2,230,000.00 USD | 0.00 USD | 162.64 USD | `-55.26%` | `40.61` |
| `Live` | `Long` | `4.03` | 2,230,000.00 USD | 0.00 USD | 402.70 USD | `-55.04%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,230,000.00 USD | 0.00 USD | 152.29 USD | `-54.82%` | `37.65` |
| `Live` | `Long` | `4.14` | 2,230,000.00 USD | 0.00 USD | 159.29 USD | `-53.70%` | `38.43` |
| `Live` | `Long` | `4.18` | 2,230,000.00 USD | 0.00 USD | 174.89 USD | `-53.25%` | `41.79` |
| `Live` | `Long` | `4.24` | 2,230,000.00 USD | 0.00 USD | 169.40 USD | `-52.69%` | `40.00` |
| `Live` | `Long` | `4.25` | 2,230,000.00 USD | 0.00 USD | 466.95 USD | `-52.58%` | `110.00` |
| `Live` | `Long` | `4.25` | 2,230,000.00 USD | 0.00 USD | 2,150.00 USD | `-52.47%` | `504.56` |
| `Live` | `Long` | `4.32` | 2,230,000.00 USD | 0.00 USD | 852.47 USD | `-51.80%` | `197.56` |
| `Live` | `Long` | `4.51` | 2,220,000.00 USD | 0.00 USD | 1,220.00 USD | `-49.56%` | `270.00` |
| `Live` | `Long` | `4.54` | 2,220,000.00 USD | 0.00 USD | 662.02 USD | `-49.34%` | `145.98` |
| `Live` | `Long` | `4.54` | 2,220,000.00 USD | 0.00 USD | 4,790.00 USD | `-49.23%` | `1,053.00` |
| `Live` | `Long` | `4.59` | 2,220,000.00 USD | 0.00 USD | 30,970.00 USD | `-48.67%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,190,000.00 USD | 0.00 USD | 486.93 USD | `-48.45%` | `105.51` |
| `Live` | `Long` | `4.62` | 2,190,000.00 USD | 0.00 USD | 2,680.00 USD | `-48.34%` | `579.06` |
| `Live` | `Long` | `4.66` | 2,180,000.00 USD | 0.00 USD | 3,280.00 USD | `-48.00%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,180,000.00 USD | 0.00 USD | 1,490.00 USD | `-47.78%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,180,000.00 USD | 0.00 USD | 15,400.00 USD | `-47.67%` | `3,287.97` |
| `Live` | `Long` | `4.75` | 2,160,000.00 USD | 0.00 USD | 240.48 USD | `-47.00%` | `50.68` |
| `Live` | `Long` | `4.76` | 2,160,000.00 USD | 0.00 USD | 105.64 USD | `-46.77%` | `22.17` |
| `Live` | `Long` | `4.78` | 2,160,000.00 USD | 0.00 USD | 15,690.00 USD | `-46.66%` | `3,286.00` |
| `Live` | `Long` | `4.79` | 2,150,000.00 USD | 0.00 USD | 111.24 USD | `-46.44%` | `23.20` |
| `Live` | `Long` | `4.83` | 2,150,000.00 USD | 0.00 USD | 467.01 USD | `-45.99%` | `96.59` |
| `Live` | `Long` | `4.88` | 2,150,000.00 USD | 0.00 USD | 276.70 USD | `-45.54%` | `56.76` |
| `Live` | `Long` | `4.89` | 2,150,000.00 USD | 0.00 USD | 4,180.00 USD | `-45.32%` | `854.62` |
| `Live` | `Long` | `4.91` | 2,140,000.00 USD | 0.00 USD | 527.19 USD | `-45.21%` | `107.48` |
| `Live` | `Long` | `4.92` | 2,140,000.00 USD | 0.00 USD | 1,230.00 USD | `-45.10%` | `251.00` |
| `Live` | `Long` | `4.96` | 2,140,000.00 USD | 0.00 USD | 945.36 USD | `-44.65%` | `190.79` |
| `Live` | `Long` | `4.97` | 2,140,000.00 USD | 0.00 USD | 760.08 USD | `-44.43%` | `152.78` |
| `Live` | `Long` | `4.99` | 2,140,000.00 USD | 0.00 USD | 329.11 USD | `-44.31%` | `66.02` |
| `Live` | `Long` | `5.01` | 2,140,000.00 USD | 0.00 USD | 56,390.00 USD | `-43.98%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,080,000.00 USD | 0.00 USD | 167.78 USD | `-43.87%` | `33.39` |
| `Live` | `Long` | `5.04` | 2,080,000.00 USD | 0.00 USD | 314.59 USD | `-43.76%` | `62.48` |
| `Live` | `Long` | `5.05` | 2,080,000.00 USD | 0.00 USD | 504.74 USD | `-43.53%` | `99.85` |
| `Live` | `Long` | `5.08` | 2,080,000.00 USD | 0.00 USD | 318.46 USD | `-43.31%` | `62.75` |
| `Live` | `Long` | `5.11` | 2,080,000.00 USD | 0.00 USD | 155,370.00 USD | `-42.97%` | `30,435.20` |
| `Live` | `Long` | `5.12` | 1,930,000.00 USD | 0.00 USD | 250.20 USD | `-42.75%` | `48.82` |
| `Live` | `Long` | `5.13` | 1,930,000.00 USD | 0.00 USD | 396.06 USD | `-42.64%` | `77.13` |
| `Live` | `Long` | `5.17` | 1,920,000.00 USD | 0.00 USD | 2,300.00 USD | `-42.30%` | `445.16` |
| `Live` | `Long` | `5.17` | 1,920,000.00 USD | 0.00 USD | 1,620.00 USD | `-42.19%` | `312.94` |
| `Live` | `Long` | `5.18` | 1,920,000.00 USD | 0.00 USD | 150.57 USD | `-42.08%` | `29.04` |
| `Live` | `Long` | `5.21` | 1,920,000.00 USD | 0.00 USD | 300.91 USD | `-41.75%` | `57.70` |
| `Live` | `Long` | `5.24` | 1,920,000.00 USD | 0.00 USD | 1,730.00 USD | `-41.52%` | `330.00` |
| `Live` | `Long` | `5.29` | 1,920,000.00 USD | 0.00 USD | 640.70 USD | `-40.96%` | `121.23` |
| `Live` | `Long` | `5.29` | 1,920,000.00 USD | 0.00 USD | 1,360.00 USD | `-40.85%` | `256.20` |
| `Live` | `Long` | `5.30` | 1,920,000.00 USD | 0.00 USD | 232.41 USD | `-40.74%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,920,000.00 USD | 0.00 USD | 716.11 USD | `-40.52%` | `134.48` |
| `Live` | `Long` | `5.39` | 1,920,000.00 USD | 0.00 USD | 660.46 USD | `-39.73%` | `122.42` |
| `Live` | `Long` | `5.42` | 1,910,000.00 USD | 0.00 USD | 21,080.00 USD | `-39.51%` | `3,892.05` |
| `Live` | `Long` | `5.42` | 1,890,000.00 USD | 0.00 USD | 160,400.00 USD | `-39.40%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,730,000.00 USD | 0.00 USD | 1,720.00 USD | `-39.29%` | `317.13` |
| `Live` | `Long` | `5.46` | 1,730,000.00 USD | 0.00 USD | 264.72 USD | `-38.95%` | `48.44` |
| `Live` | `Long` | `5.49` | 1,730,000.00 USD | 0.00 USD | 354.06 USD | `-38.73%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,730,000.00 USD | 0.00 USD | 19,290.00 USD | `-38.62%` | `3,510.41` |
| `Live` | `Long` | `5.51` | 1,710,000.00 USD | 0.00 USD | 367.41 USD | `-38.39%` | `66.62` |
| `Live` | `Long` | `5.54` | 1,710,000.00 USD | 0.00 USD | 121.38 USD | `-38.17%` | `21.93` |
| `Live` | `Long` | `5.54` | 1,710,000.00 USD | 0.00 USD | 2,770.00 USD | `-38.06%` | `500.00` |
| `Live` | `Long` | `5.57` | 1,710,000.00 USD | 0.00 USD | 967.98 USD | `-37.84%` | `173.94` |
| `Live` | `Long` | `5.58` | 1,710,000.00 USD | 0.00 USD | 63,260.00 USD | `-37.72%` | `11,347.58` |
| `Live` | `Long` | `5.59` | 1,640,000.00 USD | 0.00 USD | 34,430.00 USD | `-37.50%` | `6,153.60` |
| `Live` | `Long` | `5.63` | 1,610,000.00 USD | 0.00 USD | 22,270.00 USD | `-37.05%` | `3,952.96` |
| `Live` | `Long` | `5.64` | 1,590,000.00 USD | 0.00 USD | 4,080.00 USD | `-36.94%` | `722.97` |
| `Live` | `Long` | `5.66` | 1,580,000.00 USD | 0.00 USD | 317,420.00 USD | `-36.83%` | `56,130.52` |
| `Live` | `Long` | `5.71` | 1,270,000.00 USD | 0.00 USD | 2,340.00 USD | `-36.27%` | `409.39` |
| `Live` | `Long` | `5.74` | 1,260,000.00 USD | 0.00 USD | 238.86 USD | `-35.94%` | `41.65` |
| `Live` | `Long` | `5.75` | 1,260,000.00 USD | 0.00 USD | 125.70 USD | `-35.83%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,260,000.00 USD | 0.00 USD | 3,190.00 USD | `-35.71%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,260,000.00 USD | 0.00 USD | 10,850.00 USD | `-35.60%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,250,000.00 USD | 0.00 USD | 801.40 USD | `-35.49%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,250,000.00 USD | 0.00 USD | 2,890.00 USD | `-35.38%` | `500.00` |
| `Live` | `Long` | `5.79` | 1,250,000.00 USD | 0.00 USD | 736.72 USD | `-35.27%` | `127.13` |
| `Live` | `Long` | `5.80` | 1,240,000.00 USD | 0.00 USD | 580.50 USD | `-35.15%` | `100.00` |
| `Live` | `Long` | `5.82` | 1,240,000.00 USD | 0.00 USD | 106.65 USD | `-35.04%` | `18.34` |
| `Live` | `Long` | `5.89` | 1,240,000.00 USD | 0.00 USD | 22,060.00 USD | `-34.15%` | `3,742.70` |
| `Live` | `Long` | `5.91` | 1,220,000.00 USD | 0.00 USD | 399.18 USD | `-34.04%` | `67.60` |
| `Live` | `Long` | `5.92` | 1,220,000.00 USD | 0.00 USD | 1,330.00 USD | `-33.93%` | `225.14` |
| `Live` | `Long` | `5.96` | 1,220,000.00 USD | 0.00 USD | 11,720.00 USD | `-33.48%` | `1,968.19` |
| `Live` | `Long` | `5.97` | 1,210,000.00 USD | 0.00 USD | 585.97 USD | `-33.26%` | `98.07` |
| `Live` | `Long` | `5.99` | 1,210,000.00 USD | 0.00 USD | 447.98 USD | `-33.14%` | `74.85` |
| `Live` | `Long` | `6.00` | 1,210,000.00 USD | 0.00 USD | 341.56 USD | `-32.92%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,210,000.00 USD | 0.00 USD | 446.85 USD | `-32.81%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,210,000.00 USD | 0.00 USD | 331.68 USD | `-32.59%` | `54.96` |
| `Live` | `Long` | `6.04` | 1,210,000.00 USD | 0.00 USD | 105.61 USD | `-32.47%` | `17.47` |
| `Live` | `Long` | `6.05` | 1,210,000.00 USD | 0.00 USD | 3,650.00 USD | `-32.36%` | `602.85` |
| `Live` | `Long` | `6.07` | 1,200,000.00 USD | 0.00 USD | 265.10 USD | `-32.25%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,200,000.00 USD | 0.00 USD | 1,690.00 USD | `-32.14%` | `278.94` |
| `Live` | `Long` | `6.08` | 1,200,000.00 USD | 0.00 USD | 405.14 USD | `-32.03%` | `66.58` |
| `Live` | `Long` | `6.09` | 1,200,000.00 USD | 0.00 USD | 3,550.00 USD | `-31.92%` | `582.81` |
| `Live` | `Long` | `6.11` | 1,200,000.00 USD | 0.00 USD | 3,200.00 USD | `-31.80%` | `524.73` |
| `Live` | `Long` | `6.12` | 1,190,000.00 USD | 0.00 USD | 137.02 USD | `-31.58%` | `22.37` |
| `Live` | `Long` | `6.14` | 1,190,000.00 USD | 0.00 USD | 238.61 USD | `-31.36%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,190,000.00 USD | 0.00 USD | 4,390.00 USD | `-31.25%` | `713.75` |
| `Live` | `Long` | `6.17` | 1,190,000.00 USD | 0.00 USD | 187.29 USD | `-31.13%` | `30.38` |
| `Live` | `Long` | `6.17` | 1,190,000.00 USD | 0.00 USD | 487.21 USD | `-31.02%` | `78.90` |
| `Live` | `Long` | `6.21` | 1,190,000.00 USD | 0.00 USD | 310.25 USD | `-30.69%` | `50.00` |
| `Live` | `Long` | `6.21` | 1,190,000.00 USD | 0.00 USD | 2,560.00 USD | `-30.57%` | `411.30` |
| `Live` | `Long` | `6.22` | 1,190,000.00 USD | 0.00 USD | 715.31 USD | `-30.46%` | `114.91` |
| `Live` | `Long` | `6.25` | 1,180,000.00 USD | 0.00 USD | 2,630.00 USD | `-30.24%` | `420.65` |
| `Live` | `Long` | `6.26` | 1,180,000.00 USD | 0.00 USD | 1,450.00 USD | `-30.02%` | `232.17` |
| `Live` | `Long` | `6.28` | 1,180,000.00 USD | 0.00 USD | 2,510.00 USD | `-29.90%` | `400.00` |
| `Live` | `Long` | `6.32` | 1,180,000.00 USD | 0.00 USD | 277.04 USD | `-29.46%` | `43.87` |
| `Live` | `Long` | `6.33` | 1,180,000.00 USD | 0.00 USD | 105.25 USD | `-29.35%` | `16.64` |
| `Live` | `Long` | `6.36` | 1,180,000.00 USD | 0.00 USD | 4,470.00 USD | `-29.01%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,170,000.00 USD | 0.00 USD | 284,770.00 USD | `-28.90%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 888,480.00 USD | 0.00 USD | 5,110.00 USD | `-28.79%` | `801.31` |
| `Live` | `Long` | `6.42` | 883,370.00 USD | 0.00 USD | 306.32 USD | `-28.34%` | `47.75` |
| `Live` | `Long` | `6.43` | 883,060.00 USD | 0.00 USD | 6,780.00 USD | `-28.12%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 876,290.00 USD | 0.00 USD | 3,270.00 USD | `-27.89%` | `505.90` |
| `Live` | `Long` | `6.46` | 873,020.00 USD | 0.00 USD | 1,050.00 USD | `-27.78%` | `162.75` |
| `Live` | `Long` | `6.54` | 871,970.00 USD | 0.00 USD | 3,620.00 USD | `-27.00%` | `554.55` |
| `Live` | `Long` | `6.54` | 868,340.00 USD | 0.00 USD | 8,970.00 USD | `-26.89%` | `1,370.89` |
| `Live` | `Long` | `6.58` | 859,370.00 USD | 0.00 USD | 1,100.00 USD | `-26.44%` | `166.55` |
| `Live` | `Long` | `6.62` | 858,280.00 USD | 0.00 USD | 2,110.00 USD | `-26.11%` | `318.57` |
| `Live` | `Long` | `6.70` | 856,170.00 USD | 0.00 USD | 506.54 USD | `-25.21%` | `75.66` |
| `Live` | `Long` | `6.71` | 855,660.00 USD | 0.00 USD | 16,610.00 USD | `-25.10%` | `2,477.79` |
| `Live` | `Long` | `6.75` | 839,050.00 USD | 0.00 USD | 1,330.00 USD | `-24.65%` | `196.95` |
| `Live` | `Long` | `6.78` | 837,720.00 USD | 0.00 USD | 6,780.00 USD | `-24.32%` | `1,000.00` |
| `Live` | `Long` | `6.79` | 830,940.00 USD | 0.00 USD | 16,960.00 USD | `-24.21%` | `2,500.00` |
| `Live` | `Long` | `6.79` | 813,980.00 USD | 0.00 USD | 4,260.00 USD | `-24.10%` | `626.24` |
| `Live` | `Long` | `6.80` | 809,730.00 USD | 0.00 USD | 1,500.00 USD | `-23.98%` | `220.95` |
| `Live` | `Long` | `6.82` | 808,220.00 USD | 0.00 USD | 2,820.00 USD | `-23.87%` | `414.28` |
| `Live` | `Long` | `6.83` | 805,400.00 USD | 0.00 USD | 1,360.00 USD | `-23.76%` | `200.00` |
| `Live` | `Long` | `6.83` | 804,030.00 USD | 0.00 USD | 4,410.00 USD | `-23.65%` | `644.73` |
| `Live` | `Long` | `6.84` | 799,630.00 USD | 0.00 USD | 1,490.00 USD | `-23.54%` | `217.70` |
| `Live` | `Long` | `6.86` | 798,140.00 USD | 0.00 USD | 46,350.00 USD | `-23.43%` | `6,761.63` |
| `Live` | `Long` | `6.87` | 751,790.00 USD | 0.00 USD | 3,340.00 USD | `-23.31%` | `486.46` |
| `Live` | `Long` | `6.89` | 748,450.00 USD | 0.00 USD | 5,250.00 USD | `-22.98%` | `761.63` |
| `Live` | `Long` | `6.91` | 743,200.00 USD | 0.00 USD | 269.30 USD | `-22.87%` | `39.00` |
| `Live` | `Long` | `6.95` | 742,930.00 USD | 0.00 USD | 3,760.00 USD | `-22.42%` | `541.68` |
| `Live` | `Long` | `6.96` | 739,160.00 USD | 0.00 USD | 5,070.00 USD | `-22.31%` | `728.41` |
| `Live` | `Long` | `6.96` | 734,100.00 USD | 0.00 USD | 636.74 USD | `-22.20%` | `91.42` |
| `Live` | `Long` | `6.99` | 733,460.00 USD | 0.00 USD | 805.58 USD | `-21.97%` | `115.33` |
| `Live` | `Long` | `7.00` | 732,660.00 USD | 0.00 USD | 746.58 USD | `-21.86%` | `106.73` |
| `Live` | `Long` | `7.00` | 731,910.00 USD | 0.00 USD | 20,860.00 USD | `-21.75%` | `2,978.11` |
| `Live` | `Long` | `7.04` | 711,050.00 USD | 0.00 USD | 4,100.00 USD | `-21.30%` | `581.44` |
| `Live` | `Long` | `7.08` | 706,950.00 USD | 0.00 USD | 6,700.00 USD | `-20.97%` | `947.44` |
| `Live` | `Long` | `7.08` | 700,250.00 USD | 0.00 USD | 1,670.00 USD | `-20.86%` | `236.20` |
| `Live` | `Long` | `7.11` | 698,580.00 USD | 0.00 USD | 28,230.00 USD | `-20.63%` | `3,972.61` |
| `Live` | `Long` | `7.12` | 670,350.00 USD | 0.00 USD | 379.66 USD | `-20.52%` | `53.36` |
| `Live` | `Long` | `7.13` | 669,970.00 USD | 0.00 USD | 2,300.00 USD | `-20.30%` | `322.72` |
| `Live` | `Long` | `7.14` | 667,670.00 USD | 0.00 USD | 20,950.00 USD | `-20.19%` | `2,931.56` |
| `Live` | `Long` | `7.18` | 646,720.00 USD | 0.00 USD | 1,440.00 USD | `-19.74%` | `200.00` |
| `Live` | `Long` | `7.21` | 645,280.00 USD | 0.00 USD | 718.11 USD | `-19.40%` | `99.53` |
| `Live` | `Long` | `7.24` | 644,570.00 USD | 0.00 USD | 179.65 USD | `-19.18%` | `24.83` |
| `Live` | `Long` | `7.25` | 644,390.00 USD | 0.00 USD | 185.83 USD | `-19.07%` | `25.65` |
| `Live` | `Long` | `7.25` | 644,200.00 USD | 0.00 USD | 1,020.00 USD | `-18.96%` | `140.00` |
| `Live` | `Long` | `7.29` | 643,190.00 USD | 0.00 USD | 36,420.00 USD | `-18.62%` | `5,000.00` |
| `Live` | `Long` | `7.29` | 606,760.00 USD | 0.00 USD | 19,790.00 USD | `-18.51%` | `2,712.69` |
| `Live` | `Long` | `7.32` | 586,970.00 USD | 0.00 USD | 168.76 USD | `-18.29%` | `23.07` |
| `Live` | `Long` | `7.33` | 586,800.00 USD | 0.00 USD | 4,910.00 USD | `-18.18%` | `669.93` |
| `Live` | `Long` | `7.33` | 581,900.00 USD | 0.00 USD | 2,450.00 USD | `-18.06%` | `333.54` |
| `Live` | `Long` | `7.34` | 579,450.00 USD | 0.00 USD | 4,370.00 USD | `-17.95%` | `594.84` |
| `Live` | `Long` | `7.37` | 575,080.00 USD | 0.00 USD | 5,720.00 USD | `-17.73%` | `776.95` |
| `Live` | `Long` | `7.38` | 569,360.00 USD | 0.00 USD | 5,400.00 USD | `-17.62%` | `731.65` |
| `Live` | `Long` | `7.38` | 563,960.00 USD | 0.00 USD | 17,770.00 USD | `-17.51%` | `2,406.10` |
| `Live` | `Long` | `7.39` | 546,190.00 USD | 0.00 USD | 1,550.00 USD | `-17.39%` | `210.17` |
| `Live` | `Long` | `7.42` | 544,640.00 USD | 0.00 USD | 500.00 USD | `-17.06%` | `67.34` |
| `Live` | `Long` | `7.45` | 544,140.00 USD | 0.00 USD | 210.99 USD | `-16.84%` | `28.34` |
| `Live` | `Long` | `7.46` | 543,930.00 USD | 0.00 USD | 1,370.00 USD | `-16.72%` | `183.84` |
| `Live` | `Long` | `7.46` | 542,560.00 USD | 0.00 USD | 4,590.00 USD | `-16.61%` | `614.36` |
| `Live` | `Long` | `7.47` | 537,970.00 USD | 0.00 USD | 3,210.00 USD | `-16.50%` | `430.09` |
| `Live` | `Long` | `7.50` | 534,760.00 USD | 0.00 USD | 1,580.00 USD | `-16.28%` | `211.22` |
| `Live` | `Long` | `7.50` | 533,170.00 USD | 0.00 USD | 1,080.00 USD | `-16.16%` | `143.74` |
| `Live` | `Long` | `7.53` | 532,090.00 USD | 0.00 USD | 433.52 USD | `-15.94%` | `57.61` |
| `Live` | `Long` | `7.54` | 531,660.00 USD | 0.00 USD | 4,210.00 USD | `-15.83%` | `559.01` |
| `Live` | `Long` | `7.55` | 527,450.00 USD | 0.00 USD | 157.14 USD | `-15.61%` | `20.80` |
| `Live` | `Long` | `7.57` | 527,290.00 USD | 0.00 USD | 4,380.00 USD | `-15.49%` | `578.50` |
| `Live` | `Long` | `7.59` | 522,910.00 USD | 0.00 USD | 25,140.00 USD | `-15.16%` | `3,310.14` |
| `Live` | `Long` | `7.62` | 497,770.00 USD | 0.00 USD | 312.22 USD | `-14.94%` | `41.00` |
| `Live` | `Long` | `7.62` | 497,460.00 USD | 0.00 USD | 787.51 USD | `-14.82%` | `103.28` |
| `Live` | `Long` | `7.63` | 496,670.00 USD | 0.00 USD | 514.52 USD | `-14.71%` | `67.39` |
| `Live` | `Long` | `7.66` | 496,160.00 USD | 0.00 USD | 135.42 USD | `-14.49%` | `17.69` |
| `Live` | `Long` | `7.67` | 496,020.00 USD | 0.00 USD | 1,740.00 USD | `-14.38%` | `226.45` |
| `Live` | `Long` | `7.68` | 494,290.00 USD | 0.00 USD | 1,120.00 USD | `-14.15%` | `145.25` |
| `Live` | `Long` | `7.70` | 493,170.00 USD | 0.00 USD | 1,460.00 USD | `-14.04%` | `190.36` |
| `Live` | `Long` | `7.71` | 491,710.00 USD | 0.00 USD | 19,410.00 USD | `-13.93%` | `2,518.82` |
| `Live` | `Long` | `7.72` | 472,300.00 USD | 0.00 USD | 2,550.00 USD | `-13.71%` | `330.65` |
| `Live` | `Long` | `7.75` | 469,750.00 USD | 0.00 USD | 893.76 USD | `-13.37%` | `115.25` |
| `Live` | `Long` | `7.76` | 468,850.00 USD | 0.00 USD | 455.73 USD | `-13.26%` | `58.69` |
| `Live` | `Long` | `7.78` | 468,400.00 USD | 0.00 USD | 695.32 USD | `-13.15%` | `89.43` |
| `Live` | `Long` | `7.79` | 467,700.00 USD | 0.00 USD | 3,900.00 USD | `-13.04%` | `500.57` |
| `Live` | `Long` | `7.79` | 463,800.00 USD | 0.00 USD | 1,940.00 USD | `-12.93%` | `248.84` |
| `Live` | `Long` | `7.80` | 461,860.00 USD | 0.00 USD | 633.77 USD | `-12.81%` | `81.20` |
| `Live` | `Long` | `7.82` | 461,230.00 USD | 0.00 USD | 5,280.00 USD | `-12.70%` | `675.43` |
| `Live` | `Long` | `7.84` | 455,950.00 USD | 0.00 USD | 10,930.00 USD | `-12.37%` | `1,393.53` |
| `Live` | `Long` | `7.86` | 445,020.00 USD | 0.00 USD | 2,110.00 USD | `-12.26%` | `269.14` |
| `Live` | `Long` | `7.88` | 442,910.00 USD | 0.00 USD | 555.19 USD | `-12.03%` | `70.50` |
| `Live` | `Long` | `7.91` | 442,350.00 USD | 0.00 USD | 2,410.00 USD | `-11.70%` | `304.85` |
| `Live` | `Long` | `7.92` | 439,940.00 USD | 0.00 USD | 923.42 USD | `-11.47%` | `116.52` |
| `Live` | `Long` | `7.93` | 439,020.00 USD | 0.00 USD | 1,820.00 USD | `-11.36%` | `228.88` |
| `Live` | `Long` | `7.95` | 437,200.00 USD | 0.00 USD | 127,110.00 USD | `-11.25%` | `15,999.24` |
| `Live` | `Long` | `7.96` | 310,090.00 USD | 0.00 USD | 12,180.00 USD | `-11.14%` | `1,531.25` |
| `Live` | `Long` | `7.96` | 297,910.00 USD | 0.00 USD | 229.31 USD | `-11.03%` | `28.79` |
| `Live` | `Long` | `7.99` | 297,680.00 USD | 0.00 USD | 1,600.00 USD | `-10.80%` | `200.68` |
| `Live` | `Long` | `8.00` | 296,070.00 USD | 0.00 USD | 210.99 USD | `-10.69%` | `26.39` |
| `Live` | `Long` | `8.03` | 295,860.00 USD | 0.00 USD | 957.70 USD | `-10.36%` | `119.34` |
| `Live` | `Long` | `8.04` | 294,910.00 USD | 0.00 USD | 88,380.00 USD | `-10.24%` | `10,999.50` |
| `Live` | `Long` | `8.04` | 206,520.00 USD | 0.00 USD | 6,890.00 USD | `-10.13%` | `856.44` |
| `Live` | `Long` | `8.05` | 199,630.00 USD | 0.00 USD | 3,340.00 USD | `-10.02%` | `414.27` |
| `Live` | `Long` | `8.06` | 196,300.00 USD | 0.00 USD | 37,830.00 USD | `-9.91%` | `4,690.67` |
| `Live` | `Long` | `8.09` | 158,470.00 USD | 0.00 USD | 617.61 USD | `-9.69%` | `76.39` |
| `Live` | `Long` | `8.12` | 157,850.00 USD | 0.00 USD | 241.26 USD | `-9.35%` | `29.73` |
| `Live` | `Long` | `8.16` | 157,610.00 USD | 0.00 USD | 871.61 USD | `-8.79%` | `106.75` |
| `Live` | `Long` | `8.19` | 156,740.00 USD | 0.00 USD | 4,030.00 USD | `-8.57%` | `492.37` |
| `Live` | `Long` | `8.20` | 152,710.00 USD | 0.00 USD | 2,380.00 USD | `-8.46%` | `290.16` |
| `Live` | `Long` | `8.21` | 150,330.00 USD | 0.00 USD | 577.06 USD | `-8.35%` | `70.33` |
| `Live` | `Long` | `8.21` | 149,750.00 USD | 0.00 USD | 6,220.00 USD | `-8.23%` | `757.00` |
| `Live` | `Long` | `8.22` | 143,530.00 USD | 0.00 USD | 2,100.00 USD | `-8.12%` | `255.16` |
| `Live` | `Long` | `8.23` | 141,430.00 USD | 0.00 USD | 1,160.00 USD | `-8.01%` | `140.81` |
| `Live` | `Long` | `8.24` | 140,270.00 USD | 0.00 USD | 1,120.00 USD | `-7.90%` | `135.66` |
| `Live` | `Long` | `8.26` | 139,160.00 USD | 0.00 USD | 13,810.00 USD | `-7.79%` | `1,673.14` |
| `Live` | `Long` | `8.28` | 125,340.00 USD | 0.00 USD | 3,360.00 USD | `-7.56%` | `406.51` |
| `Live` | `Long` | `8.29` | 121,980.00 USD | 0.00 USD | 498.26 USD | `-7.45%` | `60.14` |
| `Live` | `Long` | `8.29` | 121,480.00 USD | 0.00 USD | 23,710.00 USD | `-7.34%` | `2,858.11` |
| `Live` | `Long` | `8.30` | 97,770.00 USD | 0.00 USD | 33,500.00 USD | `-7.23%` | `4,033.57` |
| `Live` | `Long` | `8.31` | 64,280.00 USD | 0.00 USD | 4,550.00 USD | `-7.12%` | `547.70` |
| `Live` | `Long` | `8.34` | 59,720.00 USD | 0.00 USD | 4,630.00 USD | `-6.89%` | `555.62` |
| `Live` | `Long` | `8.36` | 55,090.00 USD | 0.00 USD | 3,180.00 USD | `-6.67%` | `380.92` |
| `Live` | `Long` | `8.37` | 51,910.00 USD | 0.00 USD | 7,160.00 USD | `-6.56%` | `856.48` |
| `Live` | `Long` | `8.38` | 44,740.00 USD | 0.00 USD | 670.00 USD | `-6.45%` | `80.00` |
| `Live` | `Long` | `8.39` | 44,070.00 USD | 0.00 USD | 1,680.00 USD | `-6.22%` | `200.00` |
| `Live` | `Long` | `8.40` | 42,390.00 USD | 0.00 USD | 832.52 USD | `-6.11%` | `99.05` |
| `Live` | `Long` | `8.44` | 41,560.00 USD | 0.00 USD | 188.61 USD | `-5.78%` | `22.36` |
| `Live` | `Long` | `8.45` | 41,370.00 USD | 0.00 USD | 588.70 USD | `-5.66%` | `69.71` |
| `Live` | `Long` | `8.46` | 40,780.00 USD | 0.00 USD | 4,100.00 USD | `-5.55%` | `485.34` |
| `Live` | `Long` | `8.46` | 36,680.00 USD | 0.00 USD | 1,970.00 USD | `-5.44%` | `232.16` |
| `Live` | `Long` | `8.47` | 34,720.00 USD | 0.00 USD | 14,370.00 USD | `-5.33%` | `1,695.90` |
| `Live` | `Long` | `8.48` | 20,340.00 USD | 0.00 USD | 1,160.00 USD | `-5.22%` | `136.39` |
| `Live` | `Long` | `8.49` | 19,190.00 USD | 0.00 USD | 870.23 USD | `-5.11%` | `102.44` |
| `Live` | `Long` | `8.51` | 18,320.00 USD | 0.00 USD | 6,380.00 USD | `-4.99%` | `750.34` |
| `Live` | `Short` | `8.52` | 2,640.00 USD | 2,640.00 USD | 0.00 USD | `-4.88%` | `310.04` |
| `Live` | `Long` | `8.54` | 11,930.00 USD | 0.00 USD | 6,350.00 USD | `-4.66%` | `743.78` |
| `Live` | `Long` | `8.54` | 5,590.00 USD | 0.00 USD | 1,550.00 USD | `-4.55%` | `180.95` |
| `Live` | `Long` | `8.55` | 4,040.00 USD | 0.00 USD | 1,060.00 USD | `-4.44%` | `123.86` |
| `Live` | `Long` | `8.61` | 2,980.00 USD | 0.00 USD | 2,980.00 USD | `-3.88%` | `346.30` |
| `Live` | `Short` | `9.13` | 2,950.00 USD | 314.34 USD | 0.00 USD | `+2.04%` | `34.41` |
| `Live` | `Short` | `9.29` | 3,060.00 USD | 100.93 USD | 0.00 USD | `+3.72%` | `10.87` |
| `Live` | `Short` | `9.35` | 7,630.00 USD | 4,570.00 USD | 0.00 USD | `+4.39%` | `489.34` |
| `Live` | `Short` | `9.38` | 411,750.00 USD | 404,120.00 USD | 0.00 USD | `+4.84%` | `43,059.94` |
| `Live` | `Short` | `9.41` | 414,220.00 USD | 2,470.00 USD | 0.00 USD | `+5.17%` | `262.71` |
| `Live` | `Short` | `9.46` | 419,250.00 USD | 5,040.00 USD | 0.00 USD | `+5.62%` | `532.59` |
| `Live` | `Short` | `9.69` | 419,800.00 USD | 545.17 USD | 0.00 USD | `+8.19%` | `56.29` |
| `Live` | `Short` | `9.70` | 420,270.00 USD | 466.33 USD | 0.00 USD | `+8.30%` | `48.10` |
| `Live` | `Short` | `9.73` | 420,460.00 USD | 192.95 USD | 0.00 USD | `+8.75%` | `19.82` |
| `Live` | `Short` | `10.04` | 420,720.00 USD | 263.92 USD | 0.00 USD | `+12.10%` | `26.30` |
| `Live` | `Short` | `10.11` | 455,710.00 USD | 34,990.00 USD | 0.00 USD | `+12.88%` | `3,462.73` |
| `Live` | `Short` | `10.21` | 463,040.00 USD | 7,330.00 USD | 0.00 USD | `+14.11%` | `717.30` |
| `Live` | `Short` | `10.35` | 466,420.00 USD | 3,380.00 USD | 0.00 USD | `+15.56%` | `326.92` |
| `Live` | `Short` | `10.56` | 466,950.00 USD | 523.81 USD | 0.00 USD | `+18.02%` | `49.58` |
| `Live` | `Short` | `10.71` | 467,170.00 USD | 218.91 USD | 0.00 USD | `+19.69%` | `20.43` |
| `Live` | `Short` | `10.96` | 469,080.00 USD | 1,920.00 USD | 0.00 USD | `+22.49%` | `174.67` |
| `Live` | `Short` | `11.01` | 476,050.00 USD | 6,970.00 USD | 0.00 USD | `+22.93%` | `633.00` |
| `Live` | `Short` | `11.27` | 487,860.00 USD | 11,810.00 USD | 0.00 USD | `+25.84%` | `1,048.25` |
| `Live` | `Short` | `11.57` | 488,630.00 USD | 770.89 USD | 0.00 USD | `+29.30%` | `66.60` |
| `Live` | `Short` | `11.62` | 500,760.00 USD | 12,140.00 USD | 0.00 USD | `+29.86%` | `1,043.90` |
| `Live` | `Short` | `11.84` | 502,110.00 USD | 1,350.00 USD | 0.00 USD | `+32.20%` | `113.77` |
| `Live` | `Short` | `11.87` | 561,430.00 USD | 59,330.00 USD | 0.00 USD | `+32.54%` | `5,000.00` |
| `Live` | `Short` | `11.90` | 562,180.00 USD | 747.28 USD | 0.00 USD | `+32.99%` | `62.77` |
| `Live` | `Short` | `11.94` | 596,550.00 USD | 34,370.00 USD | 0.00 USD | `+33.32%` | `2,879.71` |
| `Live` | `Short` | `12.04` | 610,030.00 USD | 13,480.00 USD | 0.00 USD | `+34.44%` | `1,120.14` |
| `Live` | `Short` | `12.10` | 610,170.00 USD | 140.91 USD | 0.00 USD | `+35.11%` | `11.65` |
| `Live` | `Short` | `12.30` | 611,900.00 USD | 1,730.00 USD | 0.00 USD | `+37.45%` | `140.71` |
| `Live` | `Short` | `12.40` | 612,250.00 USD | 343.62 USD | 0.00 USD | `+38.57%` | `27.70` |
| `Live` | `Short` | `12.54` | 612,670.00 USD | 427.78 USD | 0.00 USD | `+40.13%` | `34.10` |
| `Live` | `Short` | `12.79` | 613,630.00 USD | 953.38 USD | 0.00 USD | `+42.82%` | `74.57` |
| `Live` | `Short` | `12.95` | 613,770.00 USD | 144.34 USD | 0.00 USD | `+44.60%` | `11.15` |
| `Live` | `Short` | `12.96` | 613,880.00 USD | 102.68 USD | 0.00 USD | `+44.83%` | `7.92` |
| `Live` | `Short` | `13.20` | 701,820.00 USD | 87,940.00 USD | 0.00 USD | `+47.40%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 936,660.00 USD | 234,840.00 USD | 0.00 USD | `+48.40%` | `17,677.02` |
| `Live` | `Short` | `13.29` | 940,470.00 USD | 3,810.00 USD | 0.00 USD | `+48.51%` | `286.56` |
| `Live` | `Short` | `13.46` | 940,900.00 USD | 430.34 USD | 0.00 USD | `+50.41%` | `31.96` |
| `Live` | `Short` | `13.69` | 941,070.00 USD | 172.29 USD | 0.00 USD | `+52.87%` | `12.59` |
| `Live` | `Short` | `14.24` | 945,030.00 USD | 3,950.00 USD | 0.00 USD | `+59.12%` | `277.54` |
| `Live` | `Short` | `14.55` | 945,260.00 USD | 238.85 USD | 0.00 USD | `+62.59%` | `16.41` |
| `Live` | `Short` | `14.62` | 945,580.00 USD | 314.95 USD | 0.00 USD | `+63.26%` | `21.55` |
| `Live` | `Short` | `14.66` | 946,400.00 USD | 823.29 USD | 0.00 USD | `+63.82%` | `56.14` |
| `Live` | `Short` | `14.71` | 948,850.00 USD | 2,440.00 USD | 0.00 USD | `+64.26%` | `166.16` |
| `Live` | `Short` | `14.91` | 949,140.00 USD | 294.27 USD | 0.00 USD | `+66.61%` | `19.73` |
| `Live` | `Short` | `15.12` | 1,100,000.00 USD | 151,150.00 USD | 0.00 USD | `+68.84%` | `10,000.00` |
| `Live` | `Short` | `15.29` | 1,100,000.00 USD | 229.43 USD | 0.00 USD | `+70.85%` | `15.00` |
| `Live` | `Short` | `15.35` | 1,100,000.00 USD | 230.17 USD | 0.00 USD | `+71.41%` | `15.00` |
| `Live` | `Short` | `15.38` | 1,120,000.00 USD | 20,000.00 USD | 0.00 USD | `+71.86%` | `1,300.00` |
| `Live` | `Short` | `15.47` | 1,120,000.00 USD | 110.03 USD | 0.00 USD | `+72.86%` | `7.11` |
| `Live` | `Short` | `15.70` | 1,140,000.00 USD | 23,590.00 USD | 0.00 USD | `+75.32%` | `1,502.91` |
| `Live` | `Short` | `15.77` | 1,140,000.00 USD | 117.45 USD | 0.00 USD | `+76.10%` | `7.45` |
| `Live` | `Short` | `16.25` | 1,410,000.00 USD | 263,300.00 USD | 0.00 USD | `+81.47%` | `16,208.00` |
| `Live` | `Short` | `16.43` | 1,490,000.00 USD | 82,790.00 USD | 0.00 USD | `+83.59%` | `5,037.66` |
| `Live` | `Short` | `16.52` | 1,490,000.00 USD | 190.91 USD | 0.00 USD | `+84.48%` | `11.56` |
| `Live` | `Short` | `16.75` | 1,490,000.00 USD | 162.26 USD | 0.00 USD | `+87.05%` | `9.69` |
| `Live` | `Short` | `17.02` | 1,490,000.00 USD | 191.87 USD | 0.00 USD | `+90.18%` | `11.27` |
| `Live` | `Short` | `17.14` | 1,490,000.00 USD | 1,710.00 USD | 0.00 USD | `+91.41%` | `100.00` |
| `Live` | `Short` | `17.46` | 1,490,000.00 USD | 101.47 USD | 0.00 USD | `+95.09%` | `5.81` |
| `Live` | `Short` | `17.61` | 1,500,000.00 USD | 2,040.00 USD | 0.00 USD | `+96.66%` | `115.73` |
| `Live` | `Short` | `17.62` | 1,500,000.00 USD | 4,120.00 USD | 0.00 USD | `+96.88%` | `233.67` |
| `Live` | `Short` | `17.64` | 1,500,000.00 USD | 4,930.00 USD | 0.00 USD | `+97.10%` | `279.46` |
| `Live` | `Short` | `17.66` | 1,510,000.00 USD | 2,660.00 USD | 0.00 USD | `+97.33%` | `150.82` |
| `Live` | `Short` | `17.70` | 1,510,000.00 USD | 108.89 USD | 0.00 USD | `+97.77%` | `6.15` |
| `Live` | `Short` | `17.77` | 1,510,000.00 USD | 152.96 USD | 0.00 USD | `+98.45%` | `8.61` |
| `Live` | `Short` | `17.82` | 1,510,000.00 USD | 202.49 USD | 0.00 USD | `+99.12%` | `11.36` |
| `Live` | `Short` | `17.88` | 1,510,000.00 USD | 602.92 USD | 0.00 USD | `+99.67%` | `33.73` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 345,700.00 USD | 0.00 USD | 611.73 USD | `-74.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 345,090.00 USD | 0.00 USD | 793.75 USD | `-55.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.49` | 344,290.00 USD | 0.00 USD | 105.04 USD | `-49.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 344,190.00 USD | 0.00 USD | 67,970.00 USD | `-44.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 276,220.00 USD | 0.00 USD | 205.30 USD | `-40.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 276,020.00 USD | 0.00 USD | 465.42 USD | `-39.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 275,550.00 USD | 0.00 USD | 349.35 USD | `-38.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 275,200.00 USD | 0.00 USD | 1,330.00 USD | `-35.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 273,870.00 USD | 0.00 USD | 493.50 USD | `-33.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 273,380.00 USD | 0.00 USD | 100.98 USD | `-33.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 273,280.00 USD | 0.00 USD | 620.80 USD | `-32.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 272,660.00 USD | 0.00 USD | 4,160.00 USD | `-31.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 268,500.00 USD | 0.00 USD | 6,500.00 USD | `-31.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 262,000.00 USD | 0.00 USD | 864.38 USD | `-29.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 261,140.00 USD | 0.00 USD | 1,430.00 USD | `-27.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 259,710.00 USD | 0.00 USD | 4,340.00 USD | `-27.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 255,370.00 USD | 0.00 USD | 5,520.00 USD | `-25.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 249,840.00 USD | 0.00 USD | 100.72 USD | `-24.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 249,740.00 USD | 0.00 USD | 296.34 USD | `-24.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 249,450.00 USD | 0.00 USD | 921.19 USD | `-24.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 248,520.00 USD | 0.00 USD | 709.98 USD | `-22.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 247,810.00 USD | 0.00 USD | 262.44 USD | `-22.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 247,550.00 USD | 0.00 USD | 3,610.00 USD | `-21.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 243,940.00 USD | 0.00 USD | 6,790.00 USD | `-19.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 237,150.00 USD | 0.00 USD | 9,770.00 USD | `-19.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 227,380.00 USD | 0.00 USD | 103.46 USD | `-19.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 227,280.00 USD | 0.00 USD | 603.44 USD | `-19.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 226,670.00 USD | 0.00 USD | 891.57 USD | `-18.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 225,780.00 USD | 0.00 USD | 2,300.00 USD | `-18.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 223,480.00 USD | 0.00 USD | 129.58 USD | `-18.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 223,350.00 USD | 0.00 USD | 236.19 USD | `-18.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 223,110.00 USD | 0.00 USD | 199.39 USD | `-16.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 222,910.00 USD | 0.00 USD | 4,730.00 USD | `-16.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 218,180.00 USD | 0.00 USD | 37,420.00 USD | `-16.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 180,760.00 USD | 0.00 USD | 778.49 USD | `-16.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 179,980.00 USD | 0.00 USD | 799.83 USD | `-15.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.57` | 179,180.00 USD | 0.00 USD | 103.41 USD | `-15.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 179,080.00 USD | 0.00 USD | 1,370.00 USD | `-15.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 177,700.00 USD | 0.00 USD | 360.13 USD | `-13.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 177,340.00 USD | 0.00 USD | 175.42 USD | `-13.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 177,170.00 USD | 0.00 USD | 2,990.00 USD | `-12.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 174,170.00 USD | 0.00 USD | 143.51 USD | `-12.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 174,030.00 USD | 0.00 USD | 183.33 USD | `-12.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.88` | 173,840.00 USD | 0.00 USD | 194.52 USD | `-11.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 173,650.00 USD | 0.00 USD | 394.75 USD | `-11.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 173,250.00 USD | 0.00 USD | 1,350.00 USD | `-11.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 171,910.00 USD | 0.00 USD | 1,590.00 USD | `-11.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 170,320.00 USD | 0.00 USD | 898.42 USD | `-11.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.97` | 169,420.00 USD | 0.00 USD | 107.74 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 169,320.00 USD | 0.00 USD | 1,350.00 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 167,970.00 USD | 0.00 USD | 7,400.00 USD | `-10.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 160,570.00 USD | 0.00 USD | 123.58 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 160,450.00 USD | 0.00 USD | 2,110.00 USD | `-10.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 158,340.00 USD | 0.00 USD | 563.85 USD | `-10.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 157,780.00 USD | 0.00 USD | 105.14 USD | `-9.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 157,670.00 USD | 0.00 USD | 367.76 USD | `-9.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 157,300.00 USD | 0.00 USD | 2,330.00 USD | `-9.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 154,970.00 USD | 0.00 USD | 120.10 USD | `-9.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 154,850.00 USD | 0.00 USD | 6,500.00 USD | `-9.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 148,350.00 USD | 0.00 USD | 462.15 USD | `-9.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 147,880.00 USD | 0.00 USD | 654.53 USD | `-9.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 147,230.00 USD | 0.00 USD | 367.91 USD | `-8.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 146,860.00 USD | 0.00 USD | 520.75 USD | `-8.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 146,340.00 USD | 0.00 USD | 167.22 USD | `-8.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 146,170.00 USD | 0.00 USD | 141.04 USD | `-8.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 146,030.00 USD | 0.00 USD | 1,780.00 USD | `-8.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 144,250.00 USD | 0.00 USD | 515.66 USD | `-8.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.22` | 143,730.00 USD | 0.00 USD | 165.40 USD | `-8.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 143,570.00 USD | 0.00 USD | 143.54 USD | `-8.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 143,420.00 USD | 0.00 USD | 168.64 USD | `-7.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 143,260.00 USD | 0.00 USD | 201.49 USD | `-7.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 143,050.00 USD | 0.00 USD | 6,530.00 USD | `-7.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 136,530.00 USD | 0.00 USD | 1,140.00 USD | `-7.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 135,380.00 USD | 0.00 USD | 2,000.00 USD | `-6.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 133,380.00 USD | 0.00 USD | 756.06 USD | `-6.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 132,620.00 USD | 0.00 USD | 970.35 USD | `-6.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 131,650.00 USD | 0.00 USD | 5,470.00 USD | `-6.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 126,190.00 USD | 0.00 USD | 100.74 USD | `-6.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 126,090.00 USD | 0.00 USD | 3,290.00 USD | `-6.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 122,800.00 USD | 0.00 USD | 358.56 USD | `-6.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 122,440.00 USD | 0.00 USD | 1,880.00 USD | `-5.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 120,560.00 USD | 0.00 USD | 140.36 USD | `-5.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 120,420.00 USD | 0.00 USD | 138.24 USD | `-5.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 120,280.00 USD | 0.00 USD | 954.23 USD | `-5.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.47` | 119,330.00 USD | 0.00 USD | 7,030.00 USD | `-5.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.48` | 112,290.00 USD | 0.00 USD | 489.58 USD | `-5.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.51` | 111,810.00 USD | 0.00 USD | 5,630.00 USD | `-4.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.52` | 106,170.00 USD | 0.00 USD | 5,060.00 USD | `-4.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.53` | 101,110.00 USD | 0.00 USD | 1,130.00 USD | `-4.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.54` | 99,980.00 USD | 0.00 USD | 132.45 USD | `-4.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 99,850.00 USD | 0.00 USD | 7,740.00 USD | `-4.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.57` | 92,110.00 USD | 0.00 USD | 428.58 USD | `-4.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.59` | 91,680.00 USD | 0.00 USD | 2,500.00 USD | `-4.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.60` | 89,180.00 USD | 0.00 USD | 435.59 USD | `-3.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.61` | 88,750.00 USD | 0.00 USD | 1,080.00 USD | `-3.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.62` | 87,670.00 USD | 0.00 USD | 1,980.00 USD | `-3.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.62` | 85,690.00 USD | 0.00 USD | 2,740.00 USD | `-3.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.63` | 82,950.00 USD | 0.00 USD | 103.19 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.64` | 82,840.00 USD | 0.00 USD | 103.31 USD | `-3.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 82,740.00 USD | 0.00 USD | 3,810.00 USD | `-3.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.66` | 78,930.00 USD | 0.00 USD | 196.87 USD | `-3.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.68` | 78,730.00 USD | 0.00 USD | 223.82 USD | `-3.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.69` | 78,510.00 USD | 0.00 USD | 990.09 USD | `-2.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.70` | 77,520.00 USD | 0.00 USD | 5,010.00 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.71` | 72,510.00 USD | 0.00 USD | 494.27 USD | `-2.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.71` | 72,010.00 USD | 0.00 USD | 134.30 USD | `-2.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.72` | 71,880.00 USD | 0.00 USD | 315.85 USD | `-2.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.73` | 71,560.00 USD | 0.00 USD | 1,390.00 USD | `-2.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.74` | 70,170.00 USD | 0.00 USD | 933.70 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.76` | 69,240.00 USD | 0.00 USD | 6,140.00 USD | `-2.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.77` | 63,100.00 USD | 0.00 USD | 39,810.00 USD | `-2.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.78` | 23,290.00 USD | 0.00 USD | 114.25 USD | `-1.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.79` | 23,180.00 USD | 0.00 USD | 4,230.00 USD | `-1.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.79` | 18,950.00 USD | 0.00 USD | 299.65 USD | `-1.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.80` | 18,650.00 USD | 0.00 USD | 1,760.00 USD | `-1.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.81` | 16,890.00 USD | 0.00 USD | 705.20 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.82` | 16,180.00 USD | 0.00 USD | 2,030.00 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.84` | 14,150.00 USD | 0.00 USD | 243.40 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 13,910.00 USD | 0.00 USD | 5,760.00 USD | `-1.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.86` | 8,140.00 USD | 0.00 USD | 192.86 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.87` | 7,950.00 USD | 0.00 USD | 614.88 USD | `-0.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.88` | 7,340.00 USD | 0.00 USD | 543.33 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.88` | 6,790.00 USD | 0.00 USD | 1,100.00 USD | `-0.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.89` | 5,690.00 USD | 0.00 USD | 188.66 USD | `-0.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.90` | 5,500.00 USD | 0.00 USD | 788.72 USD | `-0.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.91` | 4,710.00 USD | 0.00 USD | 3,360.00 USD | `-0.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.93` | 1,350.00 USD | 0.00 USD | 110.58 USD | `-0.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.94` | 1,240.00 USD | 0.00 USD | 1,020.00 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 223.62 USD | 0.00 USD | 223.62 USD | `-0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 137.73 USD | 137.73 USD | 0.00 USD | `+0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 3,310.00 USD | 3,170.00 USD | 0.00 USD | `+0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 318,460.00 USD | 315,150.00 USD | 0.00 USD | `+0.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 318,570.00 USD | 104.59 USD | 0.00 USD | `+0.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 319,340.00 USD | 776.54 USD | 0.00 USD | `+0.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 319,880.00 USD | 531.20 USD | 0.00 USD | `+0.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 321,250.00 USD | 1,380.00 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 322,340.00 USD | 1,090.00 USD | 0.00 USD | `+0.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 322,960.00 USD | 616.37 USD | 0.00 USD | `+0.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 323,150.00 USD | 188.59 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 323,600.00 USD | 453.84 USD | 0.00 USD | `+1.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 323,760.00 USD | 160.99 USD | 0.00 USD | `+1.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 324,180.00 USD | 415.00 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 325,690.00 USD | 1,510.00 USD | 0.00 USD | `+1.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 327,730.00 USD | 2,040.00 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 555,360.00 USD | 227,630.00 USD | 0.00 USD | `+1.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 558,390.00 USD | 3,030.00 USD | 0.00 USD | `+1.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.13` | 561,890.00 USD | 3,500.00 USD | 0.00 USD | `+2.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 563,890.00 USD | 2,000.00 USD | 0.00 USD | `+2.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 958,100.00 USD | 394,210.00 USD | 0.00 USD | `+2.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 997,230.00 USD | 39,130.00 USD | 0.00 USD | `+2.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.20` | 998,820.00 USD | 1,590.00 USD | 0.00 USD | `+2.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,010,000.00 USD | 8,580.00 USD | 0.00 USD | `+2.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,010,000.00 USD | 131.87 USD | 0.00 USD | `+2.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,010,000.00 USD | 687.91 USD | 0.00 USD | `+3.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,010,000.00 USD | 954.71 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,410,000.00 USD | 398,520.00 USD | 0.00 USD | `+3.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.27` | 1,410,000.00 USD | 205.87 USD | 0.00 USD | `+3.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,410,000.00 USD | 1,960.00 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,410,000.00 USD | 434.45 USD | 0.00 USD | `+3.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,430,000.00 USD | 18,610.00 USD | 0.00 USD | `+3.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,430,000.00 USD | 354.81 USD | 0.00 USD | `+4.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,430,000.00 USD | 2,180.00 USD | 0.00 USD | `+4.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,430,000.00 USD | 579.86 USD | 0.00 USD | `+4.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,760,000.00 USD | 327,430.00 USD | 0.00 USD | `+4.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,760,000.00 USD | 233.38 USD | 0.00 USD | `+4.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,760,000.00 USD | 163.41 USD | 0.00 USD | `+4.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,760,000.00 USD | 1,150.00 USD | 0.00 USD | `+4.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,760,000.00 USD | 660.84 USD | 0.00 USD | `+4.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,760,000.00 USD | 2,480.00 USD | 0.00 USD | `+5.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,770,000.00 USD | 1,110.00 USD | 0.00 USD | `+5.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,770,000.00 USD | 109.92 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.45` | 1,770,000.00 USD | 140.35 USD | 0.00 USD | `+5.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,770,000.00 USD | 1,890.00 USD | 0.00 USD | `+5.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.47` | 1,770,000.00 USD | 1,780.00 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,770,000.00 USD | 2,210.00 USD | 0.00 USD | `+5.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,770,000.00 USD | 288.46 USD | 0.00 USD | `+6.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.51` | 1,770,000.00 USD | 1,600.00 USD | 0.00 USD | `+6.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,770,000.00 USD | 103.54 USD | 0.00 USD | `+6.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.54` | 1,770,000.00 USD | 1,320.00 USD | 0.00 USD | `+6.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.56` | 1,780,000.00 USD | 535.35 USD | 0.00 USD | `+6.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,780,000.00 USD | 231.00 USD | 0.00 USD | `+7.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,780,000.00 USD | 221.07 USD | 0.00 USD | `+7.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,780,000.00 USD | 1,470.00 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,780,000.00 USD | 148.48 USD | 0.00 USD | `+7.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,780,000.00 USD | 329.43 USD | 0.00 USD | `+7.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,780,000.00 USD | 446.58 USD | 0.00 USD | `+8.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,780,000.00 USD | 108.21 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,780,000.00 USD | 169.68 USD | 0.00 USD | `+8.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,780,000.00 USD | 121.87 USD | 0.00 USD | `+9.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.80` | 1,780,000.00 USD | 619.28 USD | 0.00 USD | `+9.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,780,000.00 USD | 5,030.00 USD | 0.00 USD | `+9.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,780,000.00 USD | 340.05 USD | 0.00 USD | `+10.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,790,000.00 USD | 742.12 USD | 0.00 USD | `+10.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,790,000.00 USD | 899.47 USD | 0.00 USD | `+10.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,860,000.00 USD | 70,020.00 USD | 0.00 USD | `+10.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,860,000.00 USD | 373.97 USD | 0.00 USD | `+10.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,860,000.00 USD | 5,280.00 USD | 0.00 USD | `+11.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,870,000.00 USD | 6,370.00 USD | 0.00 USD | `+12.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,870,000.00 USD | 202.10 USD | 0.00 USD | `+12.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 2,080,000.00 USD | 210,980.00 USD | 0.00 USD | `+12.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 2,080,000.00 USD | 1,150.00 USD | 0.00 USD | `+13.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 2,080,000.00 USD | 172.16 USD | 0.00 USD | `+14.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 2,080,000.00 USD | 868.36 USD | 0.00 USD | `+14.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 2,080,000.00 USD | 489.40 USD | 0.00 USD | `+15.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 2,080,000.00 USD | 1,200.00 USD | 0.00 USD | `+15.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 2,080,000.00 USD | 118.01 USD | 0.00 USD | `+16.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 2,080,000.00 USD | 312.31 USD | 0.00 USD | `+17.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 2,090,000.00 USD | 1,530.00 USD | 0.00 USD | `+17.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 2,090,000.00 USD | 178.46 USD | 0.00 USD | `+18.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.62` | 2,090,000.00 USD | 153.11 USD | 0.00 USD | `+18.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 2,090,000.00 USD | 173.42 USD | 0.00 USD | `+19.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 2,090,000.00 USD | 184.75 USD | 0.00 USD | `+19.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 2,090,000.00 USD | 135.78 USD | 0.00 USD | `+20.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 2,090,000.00 USD | 127.96 USD | 0.00 USD | `+21.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 2,090,000.00 USD | 476.43 USD | 0.00 USD | `+21.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 2,090,000.00 USD | 1,730.00 USD | 0.00 USD | `+21.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 2,090,000.00 USD | 118.97 USD | 0.00 USD | `+21.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 2,090,000.00 USD | 251.06 USD | 0.00 USD | `+22.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 2,090,000.00 USD | 552.44 USD | 0.00 USD | `+22.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 2,090,000.00 USD | 1,750.00 USD | 0.00 USD | `+22.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 2,090,000.00 USD | 320.29 USD | 0.00 USD | `+24.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 2,090,000.00 USD | 1,100.00 USD | 0.00 USD | `+24.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 2,100,000.00 USD | 2,610.00 USD | 0.00 USD | `+25.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 2,100,000.00 USD | 1,270.00 USD | 0.00 USD | `+25.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 2,100,000.00 USD | 1,380.00 USD | 0.00 USD | `+26.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 2,100,000.00 USD | 2,410.00 USD | 0.00 USD | `+27.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 2,110,000.00 USD | 9,520.00 USD | 0.00 USD | `+28.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 2,110,000.00 USD | 3,530.00 USD | 0.00 USD | `+28.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 2,120,000.00 USD | 7,700.00 USD | 0.00 USD | `+29.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 2,120,000.00 USD | 1,130.00 USD | 0.00 USD | `+32.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 2,120,000.00 USD | 434.61 USD | 0.00 USD | `+32.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 2,120,000.00 USD | 163.52 USD | 0.00 USD | `+32.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 2,250,000.00 USD | 124,300.00 USD | 0.00 USD | `+34.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.51` | 2,250,000.00 USD | 2,770.00 USD | 0.00 USD | `+39.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 2,250,000.00 USD | 3,350.00 USD | 0.00 USD | `+41.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 2,250,000.00 USD | 197.97 USD | 0.00 USD | `+43.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 2,260,000.00 USD | 3,200.00 USD | 0.00 USD | `+44.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 2,260,000.00 USD | 179.58 USD | 0.00 USD | `+45.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 2,260,000.00 USD | 720.74 USD | 0.00 USD | `+45.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.07` | 2,260,000.00 USD | 504.17 USD | 0.00 USD | `+46.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 2,260,000.00 USD | 169.57 USD | 0.00 USD | `+46.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.30` | 2,260,000.00 USD | 159.66 USD | 0.00 USD | `+48.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 2,260,000.00 USD | 446.52 USD | 0.00 USD | `+49.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.46` | 2,260,000.00 USD | 1,710.00 USD | 0.00 USD | `+50.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 2,270,000.00 USD | 5,320.00 USD | 0.00 USD | `+50.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,470,000.00 USD | 207,980.00 USD | 0.00 USD | `+50.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,470,000.00 USD | 407.95 USD | 0.00 USD | `+52.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,470,000.00 USD | 174.91 USD | 0.00 USD | `+54.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,480,000.00 USD | 9,230.00 USD | 0.00 USD | `+56.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,480,000.00 USD | 960.26 USD | 0.00 USD | `+58.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,490,000.00 USD | 2,710.00 USD | 0.00 USD | `+60.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,490,000.00 USD | 805.90 USD | 0.00 USD | `+62.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,490,000.00 USD | 655.55 USD | 0.00 USD | `+64.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,490,000.00 USD | 4,890.00 USD | 0.00 USD | `+65.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,490,000.00 USD | 471.09 USD | 0.00 USD | `+66.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,490,000.00 USD | 383.85 USD | 0.00 USD | `+67.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 3,150,000.00 USD | 652,070.00 USD | 0.00 USD | `+67.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 3,150,000.00 USD | 111.87 USD | 0.00 USD | `+77.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 3,150,000.00 USD | 219.91 USD | 0.00 USD | `+78.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 3,150,000.00 USD | 121.74 USD | 0.00 USD | `+89.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.00` | 3,150,000.00 USD | 297.59 USD | 0.00 USD | `+89.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.18` | 3,150,000.00 USD | 4,500.00 USD | 0.00 USD | `+91.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.20` | 3,270,000.00 USD | 120,270.00 USD | 0.00 USD | `+92.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.34` | 3,270,000.00 USD | 122.39 USD | 0.00 USD | `+93.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.50` | 3,270,000.00 USD | 586.59 USD | 0.00 USD | `+95.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.61` | 3,270,000.00 USD | 580.97 USD | 0.00 USD | `+96.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.77` | 3,270,000.00 USD | 182.73 USD | 0.00 USD | `+98.56%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.74` | 8,640,000.00 USD | 0.00 USD | 8,640,000.00 USD | 976.80 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.76` | 8,640,000.00 USD | 0.00 USD | 8,640,000.00 USD | 812.95 USD | 5,760.00 USD | 0.00 USD |
| `7D` | `7.78` | 8,630,000.00 USD | 0.00 USD | 8,630,000.00 USD | 23,430.00 USD | 4,900.00 USD | 20,150.00 USD |
| `7D` | `7.80` | 8,580,000.00 USD | 0.00 USD | 8,580,000.00 USD | 13,050.00 USD | 12,980.00 USD | 0.00 USD |
| `7D` | `7.82` | 8,550,000.00 USD | 0.00 USD | 8,550,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,280.00 USD |
| `7D` | `7.84` | 8,540,000.00 USD | 0.00 USD | 8,540,000.00 USD | 29,020.00 USD | 2,380.00 USD | 19,730.00 USD |
| `1D` | `7.85` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 4,700.00 USD | 1,820.00 USD | 8,870.00 USD |
| `1D` | `7.86` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 10,180.00 USD | 424.36 USD | 11,210.00 USD |
| `7D` | `7.86` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 25,770.00 USD | 5,460.00 USD | 17,740.00 USD |
| `1D` | `7.87` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 13,300.00 USD | 2,670.00 USD | 11,670.00 USD |
| `1D` | `7.88` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 16,020.00 USD | 4,370.00 USD | 4,550.00 USD |
| `7D` | `7.88` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 46,450.00 USD | 12,780.00 USD | 29,190.00 USD |
| `1D` | `7.89` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 5,220.00 USD | 4,150.00 USD | 1,720.00 USD |
| `1D` | `7.90` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 9,200.00 USD | 3,480.00 USD | 5,760.00 USD |
| `7D` | `7.90` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 33,680.00 USD | 12,890.00 USD | 17,650.00 USD |
| `1D` | `7.91` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 2,990.00 USD | 0.00 USD | 2,230.00 USD |
| `1D` | `7.92` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 12,900.00 USD | 2,950.00 USD | 3,980.00 USD |
| `7D` | `7.92` | 8,290,000.00 USD | 0.00 USD | 8,290,000.00 USD | 53,660.00 USD | 8,420.00 USD | 14,900.00 USD |
| `1D` | `7.93` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 0.00 USD | 831.98 USD | 0.00 USD |
| `1D` | `7.94` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 11,450.00 USD | 3,900.00 USD | 4,500.00 USD |
| `7D` | `7.94` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 38,370.00 USD | 9,960.00 USD | 31,670.00 USD |
| `1D` | `7.95` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 0.00 USD | 1,420.00 USD | 2,440.00 USD |
| `1D` | `7.96` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 8,450.00 USD | 2,280.00 USD | 6,320.00 USD |
| `7D` | `7.96` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 21,840.00 USD | 4,820.00 USD | 26,380.00 USD |
| `1D` | `7.97` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 11,690.00 USD | 5,500.00 USD | 10,350.00 USD |
| `1D` | `7.98` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 10,080.00 USD | 1,760.00 USD | 548.73 USD |
| `7D` | `7.98` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 42,740.00 USD | 19,680.00 USD | 70,210.00 USD |
| `1D` | `7.99` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 9,190.00 USD | 2,180.00 USD | 1,510.00 USD |
| `1D` | `8.00` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 2,330.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.00` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 61,850.00 USD | 10,300.00 USD | 5,130.00 USD |
| `1D` | `8.01` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 6,360.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.02` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 2,230.00 USD | 770.83 USD | 0.00 USD |
| `7D` | `8.02` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 20,050.00 USD | 28,440.00 USD | 10,280.00 USD |
| `1D` | `8.03` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 8,800.00 USD | 0.00 USD | 4,430.00 USD |
| `1D` | `8.04` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 3,240.00 USD | 0.00 USD | 5,260.00 USD |
| `7D` | `8.04` | 7,810,000.00 USD | 0.00 USD | 7,810,000.00 USD | 94,150.00 USD | 23,930.00 USD | 75,230.00 USD |
| `1D` | `8.05` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 3,700.00 USD | 1,790.00 USD | 2,240.00 USD |
| `1D` | `8.06` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 7,120.00 USD | 0.00 USD | 2,360.00 USD |
| `7D` | `8.06` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 69,980.00 USD | 10,070.00 USD | 78,860.00 USD |
| `1D` | `8.07` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 944.98 USD | 0.00 USD | 6,030.00 USD |
| `1D` | `8.08` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 769.07 USD | 269.63 USD | 3,220.00 USD |
| `7D` | `8.08` | 7,460,000.00 USD | 0.00 USD | 7,460,000.00 USD | 7,170.00 USD | 3,650.00 USD | 20,860.00 USD |
| `1D` | `8.09` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 6,700.00 USD | 1,220.00 USD | 5,350.00 USD |
| `1D` | `8.10` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 23,830.00 USD | 1,620.00 USD | 6,040.00 USD |
| `7D` | `8.10` | 7,430,000.00 USD | 0.00 USD | 7,430,000.00 USD | 61,140.00 USD | 19,700.00 USD | 14,170.00 USD |
| `1D` | `8.11` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 144.37 USD | 1,980.00 USD | 1,360.00 USD |
| `1D` | `8.12` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 3,730.00 USD | 0.00 USD | 5,360.00 USD |
| `7D` | `8.12` | 7,330,000.00 USD | 0.00 USD | 7,330,000.00 USD | 27,150.00 USD | 10,810.00 USD | 9,260.00 USD |
| `1D` | `8.13` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 4,140.00 USD | 693.45 USD | 1,310.00 USD |
| `1D` | `8.14` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 8,480.00 USD | 0.00 USD | 26.83 USD |
| `7D` | `8.14` | 7,290,000.00 USD | 0.00 USD | 7,290,000.00 USD | 57,880.00 USD | 11,150.00 USD | 39,780.00 USD |
| `1D` | `8.15` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 11,200.00 USD | 662.47 USD | 4,950.00 USD |
| `1D` | `8.16` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 385.98 USD | 2,120.00 USD | 47.18 USD |
| `7D` | `8.16` | 7,180,000.00 USD | 0.00 USD | 7,180,000.00 USD | 38,430.00 USD | 5,510.00 USD | 30,640.00 USD |
| `1D` | `8.17` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 2,970.00 USD | 0.00 USD | 12.32 USD |
| `1D` | `8.18` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 1,150.00 USD | 1,980.00 USD | 466.21 USD |
| `7D` | `8.18` | 7,100,000.00 USD | 0.00 USD | 7,100,000.00 USD | 19,550.00 USD | 6,790.00 USD | 2,750.00 USD |
| `1D` | `8.19` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 4,850.00 USD | 0.00 USD | 48.71 USD |
| `1D` | `8.20` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 7,720.00 USD | 2,310.00 USD | 431.88 USD |
| `7D` | `8.20` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 63,560.00 USD | 0.00 USD | 16,030.00 USD |
| `1D` | `8.21` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 1,880.00 USD | 0.00 USD | 46.18 USD |
| `1D` | `8.22` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 5,330.00 USD | 0.00 USD | 12,570.00 USD |
| `7D` | `8.22` | 6,990,000.00 USD | 0.00 USD | 6,990,000.00 USD | 35,730.00 USD | 0.00 USD | 26,510.00 USD |
| `1D` | `8.23` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 20,950.00 USD | 4,080.00 USD | 31,000.00 USD |
| `1D` | `8.24` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 10,020.00 USD | 1,150.00 USD | 3,510.00 USD |
| `7D` | `8.24` | 6,930,000.00 USD | 0.00 USD | 6,930,000.00 USD | 39,950.00 USD | 3,480.00 USD | 107,080.00 USD |
| `1D` | `8.25` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 8,710.00 USD | 0.00 USD | 6,100.00 USD |
| `1D` | `8.26` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 192.60 USD | 11,460.00 USD | 0.00 USD |
| `7D` | `8.26` | 6,780,000.00 USD | 0.00 USD | 6,780,000.00 USD | 29,800.00 USD | 5,750.00 USD | 9,280.00 USD |
| `1D` | `8.27` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 11,800.00 USD | 2,760.00 USD | 36.54 USD |
| `1D` | `8.28` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 74,980.00 USD | 7,070.00 USD | 40,810.00 USD |
| `7D` | `8.28` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 122,850.00 USD | 33,920.00 USD | 14,010.00 USD |
| `1D` | `8.29` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 34,940.00 USD | 9,470.00 USD | 4,640.00 USD |
| `1D` | `8.30` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 52,980.00 USD | 13,130.00 USD | 19,010.00 USD |
| `7D` | `8.30` | 6,570,000.00 USD | 0.00 USD | 6,570,000.00 USD | 101,180.00 USD | 13,500.00 USD | 47,820.00 USD |
| `1D` | `8.31` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 55,700.00 USD | 11,410.00 USD | 1,560.00 USD |
| `1D` | `8.32` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 19,320.00 USD | 4,190.00 USD | 7,320.00 USD |
| `7D` | `8.32` | 6,400,000.00 USD | 0.00 USD | 6,400,000.00 USD | 61,070.00 USD | 26,020.00 USD | 4,710.00 USD |
| `1D` | `8.33` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 2,670.00 USD | 22,580.00 USD | 9,950.00 USD |
| `1D` | `8.34` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 14,430.00 USD | 4,810.00 USD | 6,300.00 USD |
| `7D` | `8.34` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 36,960.00 USD | 15,520.00 USD | 30,170.00 USD |
| `1D` | `8.35` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 6,060.00 USD | 11,270.00 USD | 16,070.00 USD |
| `1D` | `8.36` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 3,900.00 USD | 2,420.00 USD | 21,850.00 USD |
| `7D` | `8.36` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 107,010.00 USD | 13,470.00 USD | 71,060.00 USD |
| `1D` | `8.37` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 21,620.00 USD | 7,980.00 USD | 8,340.00 USD |
| `1D` | `8.38` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 36,180.00 USD | 4,080.00 USD | 33,870.00 USD |
| `7D` | `8.38` | 6,040,000.00 USD | 0.00 USD | 6,040,000.00 USD | 143,540.00 USD | 20,560.00 USD | 66,570.00 USD |
| `1D` | `8.39` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 62,830.00 USD | 10,540.00 USD | 56,460.00 USD |
| `1D` | `8.40` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 68,490.00 USD | 22,890.00 USD | 67,990.00 USD |
| `7D` | `8.40` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 149,520.00 USD | 19,710.00 USD | 220,030.00 USD |
| `1D` | `8.41` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 33,190.00 USD | 3,620.00 USD | 20,930.00 USD |
| `1D` | `8.42` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 33,460.00 USD | 12,790.00 USD | 18,450.00 USD |
| `7D` | `8.42` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 176,550.00 USD | 57,340.00 USD | 72,790.00 USD |
| `1D` | `8.43` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 30,620.00 USD | 34,530.00 USD | 14,440.00 USD |
| `1D` | `8.44` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 35,960.00 USD | 8,900.00 USD | 7,570.00 USD |
| `7D` | `8.44` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 155,040.00 USD | 68,350.00 USD | 76,630.00 USD |
| `1D` | `8.45` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 72,750.00 USD | 14,270.00 USD | 45,560.00 USD |
| `1D` | `8.46` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 138,660.00 USD | 13,720.00 USD | 49,580.00 USD |
| `7D` | `8.46` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 391,750.00 USD | 59,170.00 USD | 107,410.00 USD |
| `1D` | `8.47` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 111,460.00 USD | 29,440.00 USD | 22,100.00 USD |
| `1D` | `8.48` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 115,230.00 USD | 32,510.00 USD | 47,200.00 USD |
| `7D` | `8.48` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 306,870.00 USD | 56,420.00 USD | 220,180.00 USD |
| `1D` | `8.49` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 130,130.00 USD | 29,970.00 USD | 21,050.00 USD |
| `1D` | `8.50` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 46,010.00 USD | 19,260.00 USD | 21,100.00 USD |
| `7D` | `8.50` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 180,050.00 USD | 87,640.00 USD | 112,330.00 USD |
| `1D` | `8.51` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 55,990.00 USD | 54,280.00 USD | 43,390.00 USD |
| `1D` | `8.52` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 79,750.00 USD | 22,420.00 USD | 17,670.00 USD |
| `7D` | `8.52` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 255,070.00 USD | 92,530.00 USD | 239,490.00 USD |
| `1D` | `8.53` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 16,630.00 USD | 23,780.00 USD | 32,180.00 USD |
| `1D` | `8.54` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 18,880.00 USD | 6,040.00 USD | 43,640.00 USD |
| `7D` | `8.54` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 378,750.00 USD | 78,380.00 USD | 152,160.00 USD |
| `1D` | `8.55` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 42,130.00 USD | 17,890.00 USD | 16,620.00 USD |
| `1D` | `8.56` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 69,420.00 USD | 8,150.00 USD | 67,740.00 USD |
| `7D` | `8.56` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 520,060.00 USD | 91,230.00 USD | 60,050.00 USD |
| `1D` | `8.57` | 907,360.00 USD | 0.00 USD | 907,360.00 USD | 56,370.00 USD | 7,000.00 USD | 55,660.00 USD |
| `1D` | `8.58` | 788,340.00 USD | 0.00 USD | 788,340.00 USD | 48,420.00 USD | 13,910.00 USD | 39,900.00 USD |
| `7D` | `8.58` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 527,760.00 USD | 164,810.00 USD | 34,110.00 USD |
| `1D` | `8.59` | 686,110.00 USD | 0.00 USD | 686,110.00 USD | 43,310.00 USD | 25,580.00 USD | 12,560.00 USD |
| `1D` | `8.60` | 604,660.00 USD | 0.00 USD | 604,660.00 USD | 58,480.00 USD | 23,230.00 USD | 34,660.00 USD |
| `7D` | `8.60` | 693,950.00 USD | 0.00 USD | 693,950.00 USD | 75,040.00 USD | 39,160.00 USD | 176,770.00 USD |
| `1D` | `8.61` | 488,290.00 USD | 0.00 USD | 488,290.00 USD | 28,830.00 USD | 6,770.00 USD | 30,850.00 USD |
| `1D` | `8.62` | 421,840.00 USD | 0.00 USD | 421,840.00 USD | 87,140.00 USD | 14,760.00 USD | 19,830.00 USD |
| `7D` | `8.62` | 402,980.00 USD | 0.00 USD | 402,980.00 USD | 0.00 USD | 26,800.00 USD | 78,730.00 USD |
| `1D` | `8.63` | 300,110.00 USD | 0.00 USD | 300,110.00 USD | 24,730.00 USD | 2,010.00 USD | 3,840.00 USD |
| `1D` | `8.64` | 269,530.00 USD | 0.00 USD | 269,530.00 USD | 64,480.00 USD | 1,540.00 USD | 3,170.00 USD |
| `7D` | `8.64` | 297,450.00 USD | 0.00 USD | 297,450.00 USD | 73,980.00 USD | 5,680.00 USD | 58.11 USD |
| `1D` | `8.65` | 200,340.00 USD | 0.00 USD | 200,340.00 USD | 18,440.00 USD | 7,110.00 USD | 12,280.00 USD |
| `7D` | `8.66` | 217,730.00 USD | 0.00 USD | 217,730.00 USD | 0.00 USD | 6,040.00 USD | 37,900.00 USD |
| `1D` | `8.68` | 162,510.00 USD | 0.00 USD | 162,510.00 USD | 0.00 USD | 0.00 USD | 56.84 USD |
| `7D` | `8.68` | 173,790.00 USD | 0.00 USD | 173,790.00 USD | 0.00 USD | 0.00 USD | 173,670.00 USD |
| `7D` | `8.82` | 118.36 USD | 0.00 USD | 118.36 USD | 0.00 USD | 0.00 USD | 118.36 USD |
| `1D` | `8.84` | 162,460.00 USD | 0.00 USD | 162,460.00 USD | 97,740.00 USD | 16,450.00 USD | 48,260.00 USD |
| `7D` | `8.84` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.85` | 74,760.00 USD | 74,760.00 USD | 0.00 USD | 0.00 USD | 48,620.00 USD | 26,140.00 USD |
| `1D` | `8.85` | 149,520.00 USD | 149,520.00 USD | 0.00 USD | 0.00 USD | 48,620.00 USD | 26,140.00 USD |
| `1D` | `8.86` | 199,380.00 USD | 199,380.00 USD | 0.00 USD | 25,310.00 USD | 12,040.00 USD | 12,510.00 USD |
| `7D` | `8.86` | 119,780.00 USD | 119,780.00 USD | 0.00 USD | 119,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.87` | 297,400.00 USD | 297,400.00 USD | 0.00 USD | 9,410.00 USD | 22,550.00 USD | 66,070.00 USD |
| `1D` | `8.88` | 350,360.00 USD | 350,360.00 USD | 0.00 USD | 4,550.00 USD | 4,830.00 USD | 43,590.00 USD |
| `7D` | `8.88` | 202,910.00 USD | 202,910.00 USD | 0.00 USD | 0.00 USD | 4,350.00 USD | 78,770.00 USD |
| `1D` | `8.89` | 423,710.00 USD | 423,710.00 USD | 0.00 USD | 40,760.00 USD | 15,970.00 USD | 16,620.00 USD |
| `1D` | `8.90` | 582,870.00 USD | 582,870.00 USD | 0.00 USD | 73,240.00 USD | 8,150.00 USD | 77,770.00 USD |
| `7D` | `8.90` | 532,330.00 USD | 532,330.00 USD | 0.00 USD | 159,560.00 USD | 54,390.00 USD | 115,480.00 USD |
| `1D` | `8.91` | 842,000.00 USD | 842,000.00 USD | 0.00 USD | 130,250.00 USD | 25,170.00 USD | 103,710.00 USD |
| `1D` | `8.92` | 854,710.00 USD | 854,710.00 USD | 0.00 USD | 8,060.00 USD | 1,150.00 USD | 3,500.00 USD |
| `7D` | `8.92` | 648,960.00 USD | 648,960.00 USD | 0.00 USD | 19,230.00 USD | 7,700.00 USD | 89,700.00 USD |
| `1D` | `8.93` | 969,640.00 USD | 969,640.00 USD | 0.00 USD | 55,830.00 USD | 40,980.00 USD | 18,120.00 USD |
| `1D` | `8.94` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 34,120.00 USD | 14,100.00 USD | 27,860.00 USD |
| `7D` | `8.94` | 774,510.00 USD | 774,510.00 USD | 0.00 USD | 60,190.00 USD | 32,050.00 USD | 33,310.00 USD |
| `1D` | `8.95` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 53,880.00 USD | 28,330.00 USD | 25,180.00 USD |
| `1D` | `8.96` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 73,070.00 USD | 26,680.00 USD | 46,590.00 USD |
| `7D` | `8.96` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 158,650.00 USD | 92,290.00 USD | 12,730.00 USD |
| `1D` | `8.97` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 28,830.00 USD | 6,770.00 USD | 11,130.00 USD |
| `1D` | `8.98` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 147,050.00 USD | 18,380.00 USD | 42,760.00 USD |
| `7D` | `8.98` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 61,300.00 USD | 39,050.00 USD | 38,480.00 USD |
| `1D` | `8.99` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 59,440.00 USD | 11,480.00 USD | 8,470.00 USD |
| `1D` | `9.00` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 116,720.00 USD | 31,900.00 USD | 30,820.00 USD |
| `7D` | `9.00` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 161,560.00 USD | 17,050.00 USD | 46,410.00 USD |
| `1D` | `9.01` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 74,700.00 USD | 18,520.00 USD | 13,690.00 USD |
| `1D` | `9.02` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 18,000.00 USD | 4,190.00 USD | 11,830.00 USD |
| `7D` | `9.02` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 31,620.00 USD | 45,640.00 USD | 36,700.00 USD |
| `1D` | `9.03` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 2,970.00 USD | 44,330.00 USD | 22,750.00 USD |
| `1D` | `9.04` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 24,830.00 USD | 4,810.00 USD | 54,070.00 USD |
| `7D` | `9.04` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 1,950.00 USD | 49,890.00 USD | 15,140.00 USD |
| `1D` | `9.05` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 8,220.00 USD | 20,830.00 USD | 16,070.00 USD |
| `1D` | `9.06` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 3,490.00 USD | 16,550.00 USD | 22,230.00 USD |
| `7D` | `9.06` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 181,600.00 USD | 2,170.00 USD | 16,840.00 USD |
| `1D` | `9.07` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 21,880.00 USD | 10,450.00 USD | 8,310.00 USD |
| `1D` | `9.08` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 63,740.00 USD | 6,490.00 USD | 33,870.00 USD |
| `7D` | `9.08` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 142,630.00 USD | 11,960.00 USD | 65,080.00 USD |
| `1D` | `9.09` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 54,960.00 USD | 14,400.00 USD | 36,370.00 USD |
| `1D` | `9.10` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 66,840.00 USD | 14,720.00 USD | 26,710.00 USD |
| `7D` | `9.10` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 652,680.00 USD | 16,080.00 USD | 268,600.00 USD |
| `1D` | `9.11` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 19,700.00 USD | 1,320.00 USD | 13,930.00 USD |
| `1D` | `9.12` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 28,220.00 USD | 16,570.00 USD | 6,270.00 USD |
| `7D` | `9.12` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 463,210.00 USD | 24,170.00 USD | 457,010.00 USD |
| `1D` | `9.13` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 29,720.00 USD | 11,620.00 USD | 14,390.00 USD |
| `1D` | `9.14` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 14,660.00 USD | 8,440.00 USD | 17,350.00 USD |
| `7D` | `9.14` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 536,560.00 USD | 18,540.00 USD | 420,870.00 USD |
| `1D` | `9.15` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 44,870.00 USD | 7,380.00 USD | 18,890.00 USD |
| `1D` | `9.16` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 12,360.00 USD | 9,170.00 USD | 22,950.00 USD |
| `7D` | `9.16` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 331,010.00 USD | 10,610.00 USD | 195,800.00 USD |
| `1D` | `9.17` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 71,740.00 USD | 18,120.00 USD | 51,710.00 USD |
| `1D` | `9.18` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 132,750.00 USD | 19,990.00 USD | 43,220.00 USD |
| `7D` | `9.18` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 494,640.00 USD | 157,220.00 USD | 242,060.00 USD |
| `1D` | `9.19` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 66,110.00 USD | 22,640.00 USD | 25,180.00 USD |
| `1D` | `9.20` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 72,570.00 USD | 18,950.00 USD | 40,140.00 USD |
| `7D` | `9.20` | 7,150,000.00 USD | 7,150,000.00 USD | 0.00 USD | 509,140.00 USD | 107,650.00 USD | 238,640.00 USD |
| `1D` | `9.21` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 72,580.00 USD | 12,590.00 USD | 30,610.00 USD |
| `1D` | `9.22` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 71,070.00 USD | 8,140.00 USD | 1,410.00 USD |
| `7D` | `9.22` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 495,210.00 USD | 134,000.00 USD | 405,090.00 USD |
| `1D` | `9.23` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 57,020.00 USD | 3,310.00 USD | 33,930.00 USD |
| `1D` | `9.24` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 26,080.00 USD | 8,310.00 USD | 3,830.00 USD |
| `7D` | `9.24` | 8,730,000.00 USD | 8,730,000.00 USD | 0.00 USD | 316,220.00 USD | 52,090.00 USD | 174,910.00 USD |
| `1D` | `9.25` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 7,640.00 USD | 11,850.00 USD | 22.09 USD |
| `1D` | `9.26` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 16,290.00 USD | 1,210.00 USD | 0.00 USD |
| `7D` | `9.26` | 9,160,000.00 USD | 9,160,000.00 USD | 0.00 USD | 273,920.00 USD | 96,980.00 USD | 60,730.00 USD |
| `1D` | `9.27` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 144.37 USD | 11,810.00 USD | 0.00 USD |
| `1D` | `9.28` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 21,090.00 USD | 0.00 USD | 10,370.00 USD |
| `7D` | `9.28` | 9,840,000.00 USD | 9,840,000.00 USD | 0.00 USD | 451,410.00 USD | 93,640.00 USD | 142,150.00 USD |
| `1D` | `9.29` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 32,900.00 USD | 14,120.00 USD | 13,170.00 USD |
| `1D` | `9.30` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 19,890.00 USD | 8,530.00 USD | 6,810.00 USD |
| `7D` | `9.30` | 10,590,000.00 USD | 10,590,000.00 USD | 0.00 USD | 314,150.00 USD | 97,780.00 USD | 335,920.00 USD |
| `1D` | `9.31` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 13,100.00 USD | 0.00 USD | 12,680.00 USD |
| `1D` | `9.32` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 387.00 USD | 2,530.00 USD | 5,890.00 USD |
| `7D` | `9.32` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 271,660.00 USD | 59,310.00 USD | 308,520.00 USD |
| `1D` | `9.33` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 9,850.00 USD | 0.00 USD | 15,710.00 USD |
| `1D` | `9.34` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 385.98 USD | 1,350.00 USD | 9,650.00 USD |
| `7D` | `9.34` | 11,590,000.00 USD | 11,590,000.00 USD | 0.00 USD | 189,770.00 USD | 36,270.00 USD | 129,810.00 USD |
| `1D` | `9.35` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 15,350.00 USD | 3,810.00 USD | 19,450.00 USD |
| `1D` | `9.36` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 61,640.00 USD | 6,870.00 USD | 17,100.00 USD |
| `7D` | `9.36` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 245,070.00 USD | 78,550.00 USD | 101,700.00 USD |
| `1D` | `9.37` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 26,010.00 USD | 7,740.00 USD | 3,430.00 USD |
| `1D` | `9.38` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 32,400.00 USD | 4,040.00 USD | 16,830.00 USD |
| `7D` | `9.38` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 383,530.00 USD | 55,400.00 USD | 85,250.00 USD |
| `1D` | `9.39` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 8,200.00 USD | 1,730.00 USD | 3,280.00 USD |
| `1D` | `9.40` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 22,280.00 USD | 1,210.00 USD | 12.64 USD |
| `7D` | `9.40` | 12,940,000.00 USD | 12,940,000.00 USD | 0.00 USD | 196,230.00 USD | 58,130.00 USD | 152,850.00 USD |
| `1D` | `9.41` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 29,870.00 USD | 1,660.00 USD | 16,970.00 USD |
| `1D` | `9.42` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 1,520.00 USD | 622.99 USD | 4,030.00 USD |
| `7D` | `9.42` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 176,920.00 USD | 44,410.00 USD | 84,120.00 USD |
| `1D` | `9.43` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 5,840.00 USD | 6,940.00 USD | 12,410.00 USD |
| `1D` | `9.44` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 992.05 USD | 0.00 USD | 48.84 USD |
| `7D` | `9.44` | 13,390,000.00 USD | 13,390,000.00 USD | 0.00 USD | 62,040.00 USD | 19,420.00 USD | 56,550.00 USD |
| `1D` | `9.45` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 1,860.00 USD | 4,940.00 USD | 2,450.00 USD |
| `1D` | `9.46` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 1,800.00 USD | 4,580.00 USD | 21.27 USD |
| `7D` | `9.46` | 13,620,000.00 USD | 13,620,000.00 USD | 0.00 USD | 183,340.00 USD | 32,490.00 USD | 19,460.00 USD |
| `1D` | `9.47` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 17,460.00 USD | 6,870.00 USD | 192.20 USD |
| `1D` | `9.48` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 1,510.00 USD | 0.00 USD | 5,190.00 USD |
| `7D` | `9.48` | 13,800,000.00 USD | 13,800,000.00 USD | 0.00 USD | 76,510.00 USD | 37,930.00 USD | 67,400.00 USD |
| `1D` | `9.49` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 20,880.00 USD | 572.85 USD | 5,600.00 USD |
| `1D` | `9.50` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 11,770.00 USD | 3,160.00 USD | 6,320.00 USD |
| `7D` | `9.50` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 94,930.00 USD | 33,210.00 USD | 103,070.00 USD |
| `1D` | `9.52` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 17,120.00 USD | 3,070.00 USD | 5,400.00 USD |
| `7D` | `9.52` | 14,230,000.00 USD | 14,230,000.00 USD | 0.00 USD | 103,000.00 USD | 29,320.00 USD | 66,250.00 USD |
| `1D` | `9.53` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 18,480.00 USD | 4,560.00 USD | 0.00 USD |
| `1D` | `9.54` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 5,310.00 USD | 1,470.00 USD | 2,920.00 USD |
| `7D` | `9.54` | 14,470,000.00 USD | 14,470,000.00 USD | 0.00 USD | 192,230.00 USD | 27,650.00 USD | 15,770.00 USD |
| `1D` | `9.55` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 2,170.00 USD | 6,330.00 USD | 3,100.00 USD |
| `1D` | `9.56` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 5,160.00 USD | 1,280.00 USD | 2,530.00 USD |
| `7D` | `9.56` | 14,600,000.00 USD | 14,600,000.00 USD | 0.00 USD | 89,520.00 USD | 5,260.00 USD | 32,840.00 USD |
| `1D` | `9.57` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 1,020.00 USD | 3,100.00 USD | 4,960.00 USD |
| `1D` | `9.58` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 1,290.00 USD | 563.17 USD | 7,730.00 USD |
| `7D` | `9.58` | 14,680,000.00 USD | 14,680,000.00 USD | 0.00 USD | 38,860.00 USD | 16,980.00 USD | 21,640.00 USD |
| `1D` | `9.59` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 4,670.00 USD | 1,250.00 USD | 1,170.00 USD |
| `1D` | `9.60` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 11,210.00 USD | 424.36 USD | 11,260.00 USD |
| `7D` | `9.60` | 14,760,000.00 USD | 14,760,000.00 USD | 0.00 USD | 38,650.00 USD | 10,820.00 USD | 33,120.00 USD |
| `1D` | `9.61` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 13,300.00 USD | 2,670.00 USD | 11,670.00 USD |
| `1D` | `9.62` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 675.26 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.62` | 14,860,000.00 USD | 14,860,000.00 USD | 0.00 USD | 69,630.00 USD | 13,850.00 USD | 17,600.00 USD |
| `1D` | `9.63` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 10,190.00 USD | 4,370.00 USD | 1,150.00 USD |
| `1D` | `9.64` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 5,830.00 USD | 0.00 USD | 3,410.00 USD |
| `7D` | `9.64` | 14,960,000.00 USD | 14,960,000.00 USD | 0.00 USD | 61,870.00 USD | 17,650.00 USD | 19,900.00 USD |
| `1D` | `9.65` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 5,960.00 USD | 4,150.00 USD | 1,740.00 USD |
| `1D` | `9.66` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 9,200.00 USD | 3,480.00 USD | 5,760.00 USD |
| `7D` | `9.66` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 37,340.00 USD | 21,280.00 USD | 18,480.00 USD |
| `1D` | `9.67` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 2,990.00 USD | 0.00 USD | 2,230.00 USD |
| `1D` | `9.68` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 12,900.00 USD | 2,950.00 USD | 3,980.00 USD |
| `7D` | `9.68` | 15,160,000.00 USD | 15,160,000.00 USD | 0.00 USD | 69,470.00 USD | 20,310.00 USD | 34,130.00 USD |
| `1D` | `9.69` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 831.98 USD | 0.00 USD |
| `1D` | `9.70` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 11,450.00 USD | 3,900.00 USD | 4,500.00 USD |
| `7D` | `9.70` | 15,270,000.00 USD | 15,270,000.00 USD | 0.00 USD | 69,750.00 USD | 12,990.00 USD | 31,760.00 USD |
| `1D` | `9.71` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 1,420.00 USD | 2,460.00 USD |
| `1D` | `9.72` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 8,450.00 USD | 2,280.00 USD | 6,360.00 USD |
| `7D` | `9.72` | 15,380,000.00 USD | 15,380,000.00 USD | 0.00 USD | 74,210.00 USD | 4,820.00 USD | 26,980.00 USD |
| `1D` | `9.74` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 3,560.00 USD | 2,580.00 USD |
| `7D` | `9.74` | 15,420,000.00 USD | 15,420,000.00 USD | 0.00 USD | 11,450.00 USD | 7,200.00 USD | 19,560.00 USD |
| `1D` | `9.75` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 11,500.00 USD | 1,940.00 USD | 7,760.00 USD |
| `1D` | `9.76` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 9,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.76` | 15,510,000.00 USD | 15,510,000.00 USD | 0.00 USD | 31,950.00 USD | 12,480.00 USD | 51,420.00 USD |
| `7D` | `9.77` | 15,550,000.00 USD | 15,550,000.00 USD | 0.00 USD | 28,630.00 USD | 3,270.00 USD | 4,650.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `381.92M` | Total OI Tokens: `43,320,504.4 AVAX`
  * 1h OI Change: `+0.32%` | 4h OI Change: `+1.10%` | 24h OI Change: `-2.04%`
  * Exchange Breakdown: Binance=`88.71M` | Bybit=`59.43M` | OKX=`12.64M` | Hyperliquid=`17.94M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `14.21K` | Last 24h: `22.13K` | Last 3d: `69.43K` | Last 7d: `58.50K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0075%` | **USDT KuCoin** | `0.0018%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0015%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `43.58%` | `56.42%` | `0.77` | 4,040,000.00 USD |
| `15M` | `Binance` | `40.42%` | `59.58%` | `0.68` | 1,020,000.00 USD |
| `15M` | `OKX` | `45.32%` | `54.68%` | `0.83` | 222,620.00 USD |
| `15M` | `Bybit` | `31.61%` | `68.39%` | `0.46` | 305,310.00 USD |
| `15M` | `KuCoin` | `39.49%` | `60.51%` | `0.65` | 48,200.00 USD |
| `15M` | `Gate` | `46.25%` | `53.75%` | `0.86` | 75,700.00 USD |
| `15M` | `Bitget` | `20.85%` | `79.15%` | `0.26` | 137,690.00 USD |
| `15M` | `BingX` | `58.98%` | `41.02%` | `1.44` | 163,620.00 USD |
| `15M` | `MEXC` | `50.63%` | `49.37%` | `1.03` | 1,560,000.00 USD |
| `15M` | `Bitunix` | `28.28%` | `71.72%` | `0.39` | 172,790.00 USD |
| `15M` | `Hyperliquid` | `86.71%` | `13.29%` | `6.52` | 53,370.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `63.49%` | `36.51%` | `1.74` | 103,390.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 149,680.00 USD |
| `15M` | `HTX` | `98.15%` | `1.85%` | `53.05` | 12,270.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `60.93%` | `39.07%` | `1.56` | 10,620.00 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 2,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `99.79%` | `0.21%` | `475.19` | 1,680.00 USD |
| `15M` | `Whale Positions` | `40.42%` | `59.58%` | `0.68` | 1,020,000.00 USD |
| `15M` | `Global Accounts` | `43.58%` | `56.42%` | `0.77` | 4,040,000.00 USD |
| `1H` | `AVAX` | `44.17%` | `55.83%` | `0.79` | 29,710,000.00 USD |
| `1H` | `Binance` | `44.36%` | `55.64%` | `0.80` | 9,400,000.00 USD |
| `1H` | `OKX` | `43.55%` | `56.45%` | `0.77` | 2,550,000.00 USD |
| `1H` | `Bybit` | `45.3%` | `54.7%` | `0.83` | 1,720,000.00 USD |
| `1H` | `KuCoin` | `47.46%` | `52.54%` | `0.90` | 334,070.00 USD |
| `1H` | `Gate` | `50.27%` | `49.73%` | `1.01` | 515,530.00 USD |
| `1H` | `Bitget` | `41.06%` | `58.94%` | `0.70` | 911,300.00 USD |
| `1H` | `BingX` | `46.2%` | `53.8%` | `0.86` | 1,130,000.00 USD |
| `1H` | `MEXC` | `47.58%` | `52.42%` | `0.91` | 9,520,000.00 USD |
| `1H` | `Bitunix` | `40.53%` | `59.47%` | `0.68` | 1,330,000.00 USD |
| `1H` | `Hyperliquid` | `47.58%` | `52.42%` | `0.91` | 782,690.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `45.93%` | `54.07%` | `0.85` | 525,420.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `0.58%` | `99.42%` | `0.01` | 628,950.00 USD |
| `1H` | `HTX` | `82.55%` | `17.45%` | `4.73` | 15,520.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `23.62%` | `76.38%` | `0.31` | 160,870.00 USD |
| `1H` | `Aster` | `4.12%` | `95.88%` | `0.04` | 185,390.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `76.8%` | `23.2%` | `3.31` | 10,510.00 USD |
| `1H` | `Whale Positions` | `44.36%` | `55.64%` | `0.80` | 9,400,000.00 USD |
| `1H` | `Global Accounts` | `44.17%` | `55.83%` | `0.79` | 29,710,000.00 USD |
| `4H` | `AVAX` | `49.83%` | `50.17%` | `0.99` | 135,920,000.00 USD |
| `4H` | `Binance` | `53.41%` | `46.59%` | `1.15` | 47,890,000.00 USD |
| `4H` | `OKX` | `47.99%` | `52.01%` | `0.92` | 12,510,000.00 USD |
| `4H` | `Bybit` | `51.87%` | `48.13%` | `1.08` | 10,580,000.00 USD |
| `4H` | `KuCoin` | `44.8%` | `55.2%` | `0.81` | 1,030,000.00 USD |
| `4H` | `Gate` | `44.22%` | `55.78%` | `0.79` | 7,540,000.00 USD |
| `4H` | `Bitget` | `45.42%` | `54.58%` | `0.83` | 5,840,000.00 USD |
| `4H` | `BingX` | `36.4%` | `63.6%` | `0.57` | 6,600,000.00 USD |
| `4H` | `MEXC` | `50.76%` | `49.24%` | `1.03` | 13,590,000.00 USD |
| `4H` | `Bitunix` | `56.97%` | `43.03%` | `1.32` | 3,550,000.00 USD |
| `4H` | `Hyperliquid` | `63.61%` | `36.39%` | `1.75` | 1,310,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.01%` | `48.99%` | `1.04` | 22,560,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `2.79%` | `97.21%` | `0.03` | 1,920,000.00 USD |
| `4H` | `HTX` | `49.64%` | `50.36%` | `0.99` | 421,040.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.57%` | `50.43%` | `0.98` | 500,560.00 USD |
| `4H` | `Aster` | `61.56%` | `38.44%` | `1.60` | 38,810.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.18%` | `58.82%` | `0.70` | 44,860.00 USD |
| `4H` | `Whale Positions` | `53.41%` | `46.59%` | `1.15` | 47,890,000.00 USD |
| `4H` | `Global Accounts` | `49.83%` | `50.17%` | `0.99` | 135,920,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `8.77` | `8.78` | `8.77` | `8.80` | `8.76` | 895,818.33 USD | 668,329.66 USD | 227,488.66 USD | 440,841.00 USD | `+49.21%` | `13B / 5S` |
| `0:00 UTC` | `8.71` | `8.74` | `8.71` | `8.78` | `8.71` | 899,092.10 USD | 311,381.85 USD | 587,710.25 USD | -276,328.40 USD | `-30.73%` | `2B / 27S` |
| `5:00 UTC` | `8.74` | `8.74` | `8.74` | `8.77` | `8.72` | 647,153.63 USD | 422,311.32 USD | 224,842.31 USD | 197,469.01 USD | `+30.51%` | `19B / 2S` |
| `0:00 UTC` | `8.77` | `8.78` | `8.77` | `8.81` | `8.75` | 1,455,460.16 USD | 791,722.04 USD | 663,738.12 USD | 127,983.92 USD | `+8.79%` | `9B / 4S` |
| `5:00 UTC` | `8.80` | `8.79` | `8.80` | `8.81` | `8.76` | 721,263.66 USD | 311,710.76 USD | 409,552.89 USD | -97,842.13 USD | `-13.57%` | `3B / 6S` |
| `0:00 UTC` | `8.80` | `8.81` | `8.80` | `8.84` | `8.78` | 1,475,500.72 USD | 733,191.17 USD | 742,309.55 USD | -9,118.38 USD | `-0.62%` | `6B / 10S` |
| `5:00 UTC` | `8.80` | `8.81` | `8.80` | `8.83` | `8.79` | 963,676.32 USD | 510,514.93 USD | 453,161.39 USD | 57,353.55 USD | `+5.95%` | `7B / 4S` |
| `0:00 UTC` | `8.77` | `8.79` | `8.77` | `8.83` | `8.76` | 2,103,704.78 USD | 974,138.09 USD | 1,129,566.68 USD | -155,428.59 USD | `-7.39%` | `4B / 14S` |
| `5:00 UTC` | `8.83` | `8.82` | `8.83` | `8.85` | `8.78` | 1,356,806.78 USD | 729,514.30 USD | 627,292.47 USD | 102,221.83 USD | `+7.53%` | `11B / 9S` |
| `0:00 UTC` | `8.82` | `8.82` | `8.82` | `8.84` | `8.80` | 849,519.07 USD | 394,689.65 USD | 454,829.42 USD | -60,139.77 USD | `-7.08%` | `3B / 5S` |

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
| `5m` | 3,190.00 USD | -223,210.00 USD | **`DISTRIBUTION`** |
| `15m` | -6,050.00 USD | -337,100.00 USD | **`DISTRIBUTION`** |
| `30m` | -141,480.00 USD | -528,250.00 USD | **`DISTRIBUTION`** |
| `1h` | -76,550.00 USD | -1,900,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 241,870.00 USD | -1,190,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 223,980.00 USD | -1,020,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 123,710.00 USD | -754,080.00 USD | **`DISTRIBUTION`** |
| `8h` | -58,910.00 USD | -723,540.00 USD | **`DISTRIBUTION`** |
| `12h` | -49,570.00 USD | -1,370,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 192,450.00 USD | -2,270,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,510,000.00 USD | -39,740,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -52,130,000.00 USD | -267,300,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+3.19K` | 15m=`-6.05K` | 1h=`-76.55K` | 24h=`+192.45K`
* Futures Capital Netflows: 5m=`-223.21K` | 15m=`-337.10K` | 1h=`-1.90M` | 24h=`-2.27M`
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
  * Execution Entry: `8.54` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `8.41` (Risk Distance: `0.1286` pts)
  * +2.5R Take Profit: `8.86`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.89` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `9.02` (Risk Distance: `0.1286` pts)
  * +2.5R Take Profit: `8.57`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`9.01`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
