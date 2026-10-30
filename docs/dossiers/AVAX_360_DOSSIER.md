# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 11:47:32 IST` (`2026-10-30 06:17:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.57` | **Live Ask Quote**: `8.60` | **Mid Price**: `8.59`
- **Spread Points**: `3.00` | **Spread BPS**: `34.94 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.25` | VWAP Z-Score: `+1.71` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0703` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `59.77` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `8.72` | Lower -3.00σ Band: `7.78`
  * Upper +2.51σ Band: `8.64` | Lower -2.51σ Band: `7.86`
  * Upper +2.01σ Band: `8.57` | Lower -2.01σ Band: `7.94`
  * Upper +2.00σ Band: `8.57` | Lower -2.00σ Band: `7.94`
  * Upper +1.28σ Band: `8.45` | Lower -1.28σ Band: `8.05`
  * Upper +1.00σ Band: `8.41` | Lower -1.00σ Band: `8.10`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.49` | EMA-20=`8.43` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.46` (Slope: `+0.0000`) | EMA-100=`8.57`
  * Institutional Anchors: EMA-144=`8.62` | EMA-200=`8.67` (Slope: `-0.3042`) | EMA-233=`8.70`
- **Range Boundaries**: 24H High=`9.06` | 24H Low=`7.97` | Weekly High=`9.14` | Weekly Low=`7.97`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.46` (Distance: `+1.55%`)
  * Point of Control (POC) = `8.32` (Distance: `+3.31%`)
  * Value Area Low (VAL) = `8.15` (Distance: `+5.52%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`8.90` | POC=`8.74` | VAL=`8.55`
  * Prior Day Extremes: PDH=`9.06` | PDL=`8.24` | PDC=`8.33`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`9.02` | Weekly POC=`8.92` | Weekly VAL=`8.72`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`8.58` | Low=`7.97`
  * London Session (08:00-16:00 UTC): High=`8.59` | Low=`8.50`
  * New York Session (13:00-21:00 UTC): High=`8.64` | Low=`8.53`
  * Initial Balance (First Hour): IB High=`8.59` | IB Low=`8.50`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.55` - `8.62`
  * Optimal Trade Entry (OTE 0.705): `8.60`
  * Structural Invalidation Anchor (0.786): `8.65`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.55` | `8.57` | `8.54` | `8.56` | `54,572` | 466,983.17 USD | -56,746.06 USD | `-12.15%` | -5,264,383.56 USD | `-0.20` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `8.56` | `8.60` | `8.56` | `8.59` | `40,850` | 350,638.76 USD | 87,021.95 USD | `+24.82%` | -5,177,361.61 USD | `+0.39` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `8.59` | `8.61` | `8.58` | `8.61` | `22,196` | 190,811.54 USD | 78,073.14 USD | `+40.92%` | -5,099,288.47 USD | `+0.38` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.58` | `8.62` | `8.57` | `8.62` | `93,151` | 800,790.84 USD | -10,116.43 USD | `-1.26%` | -4,419,793.88 USD | `-0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `8.62` | `8.62` | `8.55` | `8.55` | `207,481` | 1,779,150.79 USD | -787,843.63 USD | `-44.28%` | -5,207,637.51 USD | `-2.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `8.55` | `8.61` | `8.54` | `8.61` | `117,325` | 1,005,910.21 USD | 106,962.43 USD | `+10.63%` | -5,100,675.07 USD | `+0.11` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `8.45` | `8.56` | `8.40` | `8.54` | `706,146` | 6,001,742.64 USD | 647,379.02 USD | `+10.79%` | -5,273,064.62 USD | `+0.57` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `8.54` | `8.62` | `8.53` | `8.55` | `678,982` | 5,826,132.55 USD | -73,472.85 USD | `-1.26%` | -5,346,537.47 USD | `+0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `8.55` | `8.61` | `8.54` | `8.61` | `117,618` | 1,008,433.46 USD | 108,349.03 USD | `+10.74%` | -5,238,188.44 USD | `+0.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,637,505.96 USD | `-1.25` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -5,927,287.94 USD | `+0.62` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.62` | `8.40` | `8.61` | `1,502,453` | 12,833,785.41 USD | 680,868.61 USD | `+5.31%` | -5,246,419.33 USD | `+1.04` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | 210,435.51 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -2,301,560.13 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,637,505.96 USD | `-1.25` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -5,927,287.94 USD | `+0.62` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.62` | `8.40` | `8.61` | `1,502,453` | 12,833,785.41 USD | 680,868.61 USD | `+5.31%` | -5,246,419.33 USD | `+1.04` | **`BULLISH`** | `DELTA ALIGNED` |

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
| --- | **`8.59`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `8.60` | `929.7100` | 7,999.88 USD | 22,420.21 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.60` | `112.1800` | 965.26 USD | 23,385.48 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.60` | `87.9000` | 756.29 USD | 24,141.77 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.60` | `77.3500` | 665.51 USD | 24,807.28 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.60` | `109.3000` | 940.38 USD | 25,747.66 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.60` | `109.3000` | 940.34 USD | 26,688.00 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.60` | `1162.3900` | 9,999.69 USD | 36,687.70 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.60` | `109.3000` | 940.26 USD | 37,627.96 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.60` | `312.0500` | 2,684.32 USD | 40,312.28 USD | `1 orders` | `-0.08%` | `-` |
| `ASK` | `8.61` | `115.1000` | 991.57 USD | 31,861.53 USD | `3 orders` | `+0.07%` | `-` |
| `ASK` | `8.61` | `200.0000` | 1,722.96 USD | 30,869.96 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.61` | `158.1100` | 1,362.04 USD | 29,147.00 USD | `2 orders` | `+0.07%` | `-` |
| `ASK` | `8.61` | `56.6000` | 487.58 USD | 27,784.96 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.61` | `2070.5700` | 17,835.89 USD | 27,297.38 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.61` | `5.8000` | 49.96 USD | 9,461.49 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.61` | `109.3000` | 941.47 USD | 9,411.53 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.61` | `159.3000` | 1,372.08 USD | 8,470.07 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `8.61` | `2.5300` | 21.79 USD | 7,097.98 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.61` | `109.3000` | 941.38 USD | 7,076.19 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.61` | `60.3400` | 519.69 USD | 6,134.81 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.61` | `7.8900` | 67.95 USD | 5,615.12 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.61` | `109.2900` | 941.22 USD | 5,547.17 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.61` | `43.5100` | 374.71 USD | 4,605.95 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.61` | `88.6300` | 763.24 USD | 4,231.25 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.61` | `109.2900` | 941.14 USD | 3,468.01 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.61` | `259.7700` | 2,236.80 USD | 2,526.87 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `8.61` | `33.6900` | 290.07 USD | 290.07 USD | `2 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `8.61` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.61` | `0.00%` | `-` |
| `BID` | `8.61` | `146.8300` | 1,263.90 USD | 1,263.90 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.61` | `229.3800` | 1,974.46 USD | 3,238.36 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `8.61` | `109.2900` | 940.67 USD | 4,179.03 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.61` | `697.1000` | 5,999.66 USD | 10,178.69 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.61` | `81.9600` | 705.39 USD | 10,884.07 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.61` | `42.6900` | 367.41 USD | 11,251.48 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.61` | `16.0000` | 137.70 USD | 11,389.18 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.61` | `109.3000` | 940.61 USD | 12,329.80 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.61` | `109.3000` | 940.60 USD | 13,270.40 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.61` | `117.6300` | 1,012.25 USD | 14,282.65 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `8.61` | `16.0000` | 137.68 USD | 14,420.34 USD | `1 orders` | `-0.04%` | `-` |
| `ASK` | `8.62` | `120.0800` | 1,034.51 USD | 33,896.00 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.62` | `116.0700` | 999.95 USD | 32,861.49 USD | `1 orders` | `+0.07%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:43:56 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1458` | `0x7737...bf66` | `SHORT` | 1,476,772.08 USD | `171,568.06` | `7.43` | `8.60` | `108.22` | -201,227.06 USD | `-13.63%` | `10X Cross` |
| `1559` | `0xeadc...9d55` | `LONG` | 1,377,839.36 USD | `160,070.56` | `8.11` | `8.60` | `0.000000` | 80,201.79 USD | `+5.82%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `12.60` | 5,040.00 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Liquidated Short: 5.04K USD at 12.6000 USD [API] | `2025-11-21 07:34:12` |
| `ANNOUNCEMENT` | `INFO` | `20.20` | 2,020.00 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Liquidated Short: 2.02K USD at 20.2000 USD [API] | `2025-10-10 21:16:10` |
| `ANNOUNCEMENT` | `INFO` | `8.64` | 6,000.14 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 6.00K USD at 8.6359 USD [API] | `2026-10-29 04:41:03` |
| `ANNOUNCEMENT` | `INFO` | `8.67` | 4,004.69 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Liquidated Short: 4.00K USD at 8.6736 USD [API] | `2026-10-24 15:25:46` |
| `ANNOUNCEMENT` | `INFO` | `8.67` | 7,999.81 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 8.00K USD at 8.6670 USD [API] | `2026-10-29 04:57:34` |
| `ANNOUNCEMENT` | `INFO` | `8.67` | 10,748.68 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 10.75K USD at 8.6671 USD [API] | `2026-10-29 04:57:34` |
| `ANNOUNCEMENT` | `INFO` | `9.19` | 306.88 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Liquidated Short: 0.31K USD at 9.1879 USD [API] | `2026-10-22 08:07:57` |
| `ANNOUNCEMENT` | `INFO` | `9.26` | 203.58 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Liquidated Short: 0.20K USD at 9.2620 USD [API] | `2026-10-18 19:46:02` |
| `ANNOUNCEMENT` | `INFO` | `9.39` | 1,787.07 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Liquidated Short: 1.79K USD at 9.3928 USD [API] | `2026-10-18 19:33:08` |
| `ANNOUNCEMENT` | `INFO` | `8.77` | 5,999.84 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 6.00K USD at 8.7749 USD [API] | `2026-10-29 05:27:33` |
| `ANNOUNCEMENT` | `INFO` | `8.63` | 7,999.74 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 8.00K USD at 8.6326 USD [API] | `2026-10-29 08:06:42` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+1.81%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--6.41%`)
  * 48H Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+1.74%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--6.43%`)
  * 3D Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+1.74%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--6.43%`)
  * 7D Horizon: Short MP=`9.23` (Vol: 459,400.00 USD, Dist: `+7.22%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--6.43%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `1.78` | 205.28 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.94` | 214.42 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 160.40 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 236.32 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 5,160.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 106.59 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 248.97 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 133.38 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 942.44 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 313.38 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 19,400.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 232.67 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111.12 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 23,400.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 1,260.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 1,250.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 544.70 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 151.88 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 6,770.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 392.22 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 109.95 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.98` | 254.04 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 3,080.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.09` | 382.15 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 159.29 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.22` | 195.49 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.42` | 459.01 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 110.77 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.54` | 195.75 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 486.93 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 2,930.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 105.11 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 8,890.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.70` | 7,040.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.78` | 112.02 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 467.01 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 3,880.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,230.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.93` | 16,220.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 352.68 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 4,090.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.99` | 727.71 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.00` | 269.53 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.03` | 167.78 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 314.59 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 710.03 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 213.20 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 105.46 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.09` | 651.75 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 3,470.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 5,650.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 1,030.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.20` | 979.05 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 300.91 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 160,990.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.26` | 2,230.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 640.70 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.32` | 232.85 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 716.11 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 660.46 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.41` | 260.63 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 20,160.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 2,830.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.47` | 1,320.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.51` | 367.41 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 4,180.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.59` | 34,430.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.62` | 2,810.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 468.55 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.71` | 147.33 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.72` | 2,390.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 661.65 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 635.31 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 580.50 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 106.65 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.83` | 145.88 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.86` | 2,110.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 984.70 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.92` | 277.35 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 11,720.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 6,320.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 437.84 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 265.10 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 405.14 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,130.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 1,140.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 137.02 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.13` | 2,030.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 7,810.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 3,390.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.30` | 1,420.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 354,850.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 1,470.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 284,770.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 1,310.00 USD | 820,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 5,120.00 USD | 819,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 814,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 484.64 USD | 813,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 813,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 1,050.00 USD | 806,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.50` | 1,490.00 USD | 805,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 852.03 USD | 804,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 803,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.57` | 1,520.00 USD | 794,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 1,770.00 USD | 792,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.59` | 1,260.00 USD | 791,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 789,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 364.90 USD | 787,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.63` | 245.89 USD | 787,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.67` | 1,320.00 USD | 787,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.68` | 3,160.00 USD | 785,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 16,570.00 USD | 782,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 6,180.00 USD | 765,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 759,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 7,990.00 USD | 758,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 22,360.00 USD | 750,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 4,720.00 USD | 728,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 1,500.00 USD | 723,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 7,230.00 USD | 721,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 158.14 USD | 714,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,710.00 USD | 714,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 1,580.00 USD | 710,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.92` | 579.62 USD | 709,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.93` | 3,500.00 USD | 708,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 3,980.00 USD | 705,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 3,480.00 USD | 701,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 636.74 USD | 697,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.97` | 128,810.00 USD | 697,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.99` | 297.49 USD | 568,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 746.58 USD | 567,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 175.12 USD | 567,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.01` | 20,890.00 USD | 567,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.03` | 1,370.00 USD | 546,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.07` | 23,960.00 USD | 544,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 7,420.00 USD | 520,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,050.00 USD | 513,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.09` | 2,130.00 USD | 512,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 28,530.00 USD | 510,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 481,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 777.50 USD | 481,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.14` | 7,640,000.00 USD | 7,640,000.00 USD | 45,840.00 USD | 22,970.00 USD | 41,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,270.00 USD | 480,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.16` | 7,530,000.00 USD | 7,530,000.00 USD | 29,500.00 USD | 4,260.00 USD | 21,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.17` | 2,380.00 USD | 460,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.18` | 7,470,000.00 USD | 7,470,000.00 USD | 5,030.00 USD | 3,780.00 USD | 19,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.18` | 31,620.00 USD | 457,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.20` | 7,440,000.00 USD | 7,440,000.00 USD | 11,960.00 USD | 7,300.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.21` | 2,100.00 USD | 426,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 322.94 USD | 424,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.22` | 7,420,000.00 USD | 7,420,000.00 USD | 12,640.00 USD | 6,540.00 USD | 6,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.24` | 1,480.00 USD | 423,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.24` | 7,390,000.00 USD | 7,390,000.00 USD | 39,910.00 USD | 0.00 USD | 14,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.25` | 185.83 USD | 422,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 21,280.00 USD | 422,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.26` | 7,340,000.00 USD | 7,340,000.00 USD | 420.05 USD | 1,810.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.28` | 7,330,000.00 USD | 7,330,000.00 USD | 7,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,420.00 USD | 400,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 1,680.00 USD | 364,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.30` | 7,320,000.00 USD | 7,320,000.00 USD | 252.80 USD | 0.00 USD | 4,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.30` | 1,020.00 USD | 362,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.32` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 0.00 USD | 8,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.33` | 13,110.00 USD | 361,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.34` | 7,310,000.00 USD | 7,310,000.00 USD | 7,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.34` | 5,250.00 USD | 348,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.36` | 7,300,000.00 USD | 7,300,000.00 USD | 983.83 USD | 0.00 USD | 864.67 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.37` | 2,940.00 USD | 343,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 1,100.00 USD | 340,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.38` | 7,300,000.00 USD | 7,300,000.00 USD | 46,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.38` | 227.97 USD | 339,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.40` | 7,250,000.00 USD | 7,250,000.00 USD | 44,790.00 USD | 0.00 USD | 503.12 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.42` | 147.61 USD | 339,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.43` | 2,430.00 USD | 338,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 2,410.00 USD | 336,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 10,390.00 USD | 334,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.46` | 7,210,000.00 USD | 7,210,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.46` | 4,590.00 USD | 323,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 1,120.00 USD | 319,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.48` | 7,180,000.00 USD | 7,180,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 962.81 USD | 318,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 421.78 USD | 317,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.51` | 1,710.00 USD | 316,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.52` | 7,160,000.00 USD | 7,160,000.00 USD | 3,220.00 USD | 14,470.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.53` | 1,570.00 USD | 314,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 313,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.54` | 7,130,000.00 USD | 7,130,000.00 USD | 34,840.00 USD | 4,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.54` | 1,510.00 USD | 309,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.55` | 6,450,000.00 USD | 6,450,000.00 USD | 8,130.00 USD | 4,270.00 USD | 136.40 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.55` | 415.52 USD | 307,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.56` | 6,440,000.00 USD | 6,440,000.00 USD | 14,910.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.56` | 7,090,000.00 USD | 7,090,000.00 USD | 20,150.00 USD | 4,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.57` | 25,060.00 USD | 307,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.57` | 6,420,000.00 USD | 6,420,000.00 USD | 342.65 USD | 0.00 USD | 101.23 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.58` | 118.25 USD | 282,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.58` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 0.00 USD | 3,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.59` | 6,410,000.00 USD | 6,410,000.00 USD | 1,390.00 USD | 0.00 USD | 4,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.59` | 26,390.00 USD | 282,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.60` | 6,410,000.00 USD | 6,410,000.00 USD | 629.05 USD | 4,900.00 USD | 351.13 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.60` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 0.00 USD | 301.55 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.61` | 935.87 USD | 255,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.61` | 6,400,000.00 USD | 6,400,000.00 USD | 1,190.00 USD | 761.26 USD | 11,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 754.04 USD | 254,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.62` | 6,390,000.00 USD | 6,390,000.00 USD | 916.10 USD | 0.00 USD | 133.28 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.62` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 0.00 USD | 996.08 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 253,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.63` | 6,390,000.00 USD | 6,390,000.00 USD | 986.95 USD | 0.00 USD | 8,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.63` | 378.93 USD | 253,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.64` | 6,380,000.00 USD | 6,380,000.00 USD | 33,010.00 USD | 812.96 USD | 158.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.64` | 7,060,000.00 USD | 7,060,000.00 USD | 41,300.00 USD | 0.00 USD | 686.63 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.65` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 252,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.66` | 6,330,000.00 USD | 6,330,000.00 USD | 3,030.00 USD | 0.00 USD | 531.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.66` | 7,020,000.00 USD | 7,020,000.00 USD | 4,870.00 USD | 0.00 USD | 24,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 256.09 USD | 252,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.67` | 6,330,000.00 USD | 6,330,000.00 USD | 1,140.00 USD | 0.00 USD | 114.38 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 4,480.00 USD | 252,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.68` | 6,330,000.00 USD | 6,330,000.00 USD | 892.30 USD | 0.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.68` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 0.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.68` | 739.30 USD | 247,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.70` | 6,690.00 USD | 247,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.70` | 6,320,000.00 USD | 6,320,000.00 USD | 551.10 USD | 2,390.00 USD | 16,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.71` | 6,310,000.00 USD | 6,310,000.00 USD | 660.12 USD | 5,040.00 USD | 7,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.72` | 6,290,000.00 USD | 6,290,000.00 USD | 701.68 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.72` | 6,980,000.00 USD | 6,980,000.00 USD | 38,970.00 USD | 0.00 USD | 40,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.73` | 6,290,000.00 USD | 6,290,000.00 USD | 4,120.00 USD | 0.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.74` | 6,280,000.00 USD | 6,280,000.00 USD | 9,310.00 USD | 0.00 USD | 184.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.74` | 6,900,000.00 USD | 6,900,000.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.75` | 6,270,000.00 USD | 6,270,000.00 USD | 775.36 USD | 5,560.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.75` | 500.12 USD | 240,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.76` | 6,260,000.00 USD | 6,260,000.00 USD | 188.00 USD | 0.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.76` | 6,900,000.00 USD | 6,900,000.00 USD | 812.95 USD | 13,360.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 240,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.77` | 6,260,000.00 USD | 6,260,000.00 USD | 23,890.00 USD | 572.85 USD | 5,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.78` | 8,670.00 USD | 239,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.78` | 6,230,000.00 USD | 6,230,000.00 USD | 7,400.00 USD | 7,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.78` | 6,870,000.00 USD | 6,870,000.00 USD | 46,570.00 USD | 4,900.00 USD | 21,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 1,380.00 USD | 230,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.79` | 6,210,000.00 USD | 6,210,000.00 USD | 8,050.00 USD | 2,910.00 USD | 589.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 4,480.00 USD | 229,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.80` | 6,200,000.00 USD | 6,200,000.00 USD | 9,300.00 USD | 9,380.00 USD | 3,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.80` | 6,800,000.00 USD | 6,800,000.00 USD | 17,590.00 USD | 12,980.00 USD | 1,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.80` | 6,380.00 USD | 225,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.81` | 6,180,000.00 USD | 6,180,000.00 USD | 809.15 USD | 728.43 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.82` | 6,180,000.00 USD | 6,180,000.00 USD | 4,270.00 USD | 2,970.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.82` | 6,770,000.00 USD | 6,770,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.83` | 1,750.00 USD | 218,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.83` | 6,170,000.00 USD | 6,170,000.00 USD | 27,230.00 USD | 6,330.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.84` | 6,130,000.00 USD | 6,130,000.00 USD | 1,060.00 USD | 1,800.00 USD | 10.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.84` | 6,760,000.00 USD | 6,760,000.00 USD | 32,340.00 USD | 2,380.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 22,560.00 USD | 216,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.85` | 6,130,000.00 USD | 6,130,000.00 USD | 5,210.00 USD | 1,250.00 USD | 2,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.86` | 6,120,000.00 USD | 6,120,000.00 USD | 5,060.00 USD | 6,690.00 USD | 18,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.86` | 6,700,000.00 USD | 6,700,000.00 USD | 137,360.00 USD | 5,460.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.87` | 233.83 USD | 194,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.87` | 6,090,000.00 USD | 6,090,000.00 USD | 13,690.00 USD | 10,860.00 USD | 24,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 194,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.88` | 6,040,000.00 USD | 6,040,000.00 USD | 161,620.00 USD | 5,890.00 USD | 34,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.88` | 6,540,000.00 USD | 6,540,000.00 USD | 170,100.00 USD | 12,780.00 USD | 30,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 575.53 USD | 193,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.89` | 5,840,000.00 USD | 5,840,000.00 USD | 59,740.00 USD | 3,720.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.89` | 15,880.00 USD | 192,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.90` | 5,750,000.00 USD | 5,750,000.00 USD | 56,040.00 USD | 6,970.00 USD | 5,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.90` | 6,320,000.00 USD | 6,320,000.00 USD | 33,680.00 USD | 12,890.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 2,930.00 USD | 177,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.91` | 5,680,000.00 USD | 5,680,000.00 USD | 14,100.00 USD | 10,370.00 USD | 28,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.92` | 5,620,000.00 USD | 5,620,000.00 USD | 15,980.00 USD | 2,950.00 USD | 8,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.92` | 6,260,000.00 USD | 6,260,000.00 USD | 55,490.00 USD | 23,630.00 USD | 41,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 4,600.00 USD | 174,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.93` | 5,600,000.00 USD | 5,600,000.00 USD | 7,960.00 USD | 6,570.00 USD | 4,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 16,340.00 USD | 169,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 5,580,000.00 USD | 5,580,000.00 USD | 17,720.00 USD | 20,510.00 USD | 61,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.94` | 6,140,000.00 USD | 6,140,000.00 USD | 51,390.00 USD | 9,960.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 127,110.00 USD | 153,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 5,480,000.00 USD | 5,480,000.00 USD | 27,800.00 USD | 9,190.00 USD | 86,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.96` | 5,350,000.00 USD | 5,350,000.00 USD | 2,970.00 USD | 15,680.00 USD | 62,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.96` | 6,040,000.00 USD | 6,040,000.00 USD | 21,840.00 USD | 6,920.00 USD | 87,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.97` | 5,270,000.00 USD | 5,270,000.00 USD | 12,860.00 USD | 9,820.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.97` | 1,580.00 USD | 26,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.98` | 5,250,000.00 USD | 5,250,000.00 USD | 5,050.00 USD | 2,060.00 USD | 42,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.98` | 5,930,000.00 USD | 5,930,000.00 USD | 58,520.00 USD | 26,790.00 USD | 146,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,600.00 USD | 24,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 5,200,000.00 USD | 5,200,000.00 USD | 3,230.00 USD | 10,180.00 USD | 4,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 210.99 USD | 22,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 5,180,000.00 USD | 5,180,000.00 USD | 50,430.00 USD | 8,950.00 USD | 21,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.00` | 5,700,000.00 USD | 5,700,000.00 USD | 60,980.00 USD | 16,420.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.01` | 5,100,000.00 USD | 5,100,000.00 USD | 6,540.00 USD | 3,750.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 5,080,000.00 USD | 5,080,000.00 USD | 75,000.00 USD | 0.00 USD | 274.70 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.02` | 5,610,000.00 USD | 5,610,000.00 USD | 15,300.00 USD | 46,670.00 USD | 57,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 248.37 USD | 22,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.03` | 5,010,000.00 USD | 5,010,000.00 USD | 8,820.00 USD | 12,540.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.04` | 4,970,000.00 USD | 4,970,000.00 USD | 49,080.00 USD | 0.00 USD | 10,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.04` | 5,490,000.00 USD | 5,490,000.00 USD | 460,090.00 USD | 0.00 USD | 86,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.05` | 4,910,000.00 USD | 4,910,000.00 USD | 317,540.00 USD | 6,430.00 USD | 53,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.06` | 4,540,000.00 USD | 4,540,000.00 USD | 155,240.00 USD | 0.00 USD | 66,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.06` | 4,950,000.00 USD | 4,950,000.00 USD | 336,530.00 USD | 0.00 USD | 86,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.07` | 4,310,000.00 USD | 4,310,000.00 USD | 130,100.00 USD | 9,310.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.07` | 21,710.00 USD | 22,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.08` | 4,170,000.00 USD | 4,170,000.00 USD | 14,440.00 USD | 0.00 USD | 65,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.08` | 4,520,000.00 USD | 4,520,000.00 USD | 5,100.00 USD | 0.00 USD | 73,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.09` | 4,090,000.00 USD | 4,090,000.00 USD | 3,110.00 USD | 0.00 USD | 29,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.10` | 4,060,000.00 USD | 4,060,000.00 USD | 31,390.00 USD | 6,770.00 USD | 122,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.10` | 4,450,000.00 USD | 4,450,000.00 USD | 56,590.00 USD | 0.00 USD | 14,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.11` | 3,900,000.00 USD | 3,900,000.00 USD | 77,850.00 USD | 0.00 USD | 192,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 738.14 USD | 738.14 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.12` | 3,630,000.00 USD | 3,630,000.00 USD | 7,380.00 USD | 10,020.00 USD | 126,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.12` | 4,370,000.00 USD | 4,370,000.00 USD | 22,060.00 USD | 0.00 USD | 141,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.13` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 4,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 4,120.00 USD | 96,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.14` | 4,210,000.00 USD | 4,210,000.00 USD | 160,410.00 USD | 25,370.00 USD | 191,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.15` | 3,380,000.00 USD | 3,380,000.00 USD | 40,400.00 USD | 11,230.00 USD | 46,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.16` | 3,280,000.00 USD | 3,280,000.00 USD | 192.50 USD | 17,890.00 USD | 165,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.16` | 3,830,000.00 USD | 3,830,000.00 USD | 30,670.00 USD | 17,750.00 USD | 29,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.17` | 3,100,000.00 USD | 3,100,000.00 USD | 11,100.00 USD | 8,610.00 USD | 183,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.18` | 2,890,000.00 USD | 2,890,000.00 USD | 6,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.18` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 43,260.00 USD | 172,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.19` | 2,890,000.00 USD | 2,890,000.00 USD | 17,640.00 USD | 0.00 USD | 15,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.20` | 2,850,000.00 USD | 2,850,000.00 USD | 25,530.00 USD | 0.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.20` | 3,540,000.00 USD | 3,540,000.00 USD | 174,220.00 USD | 58,100.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.21` | 2,820,000.00 USD | 2,820,000.00 USD | 33,010.00 USD | 1,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.22` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.22` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 21,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.23` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 1,750.00 USD | 35.82 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.24` | 2,760,000.00 USD | 2,760,000.00 USD | 277.44 USD | 1,020.00 USD | 0.98 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.24` | 3,280,000.00 USD | 3,280,000.00 USD | 107,610.00 USD | 18,690.00 USD | 17,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.25` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 38,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.26` | 2,720,000.00 USD | 2,720,000.00 USD | 32,580.00 USD | 12,510.00 USD | 23,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.26` | 3,130,000.00 USD | 3,130,000.00 USD | 30,070.00 USD | 5,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.27` | 2,660,000.00 USD | 2,660,000.00 USD | 13,860.00 USD | 9,880.00 USD | 20,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.28` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 9,050.00 USD | 0.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.28` | 3,100,000.00 USD | 3,100,000.00 USD | 101,560.00 USD | 4,000.00 USD | 27,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.29` | 2,600,000.00 USD | 2,600,000.00 USD | 14,380.00 USD | 8,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.30` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 4,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.30` | 2,970,000.00 USD | 2,970,000.00 USD | 152,370.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.31` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 39,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.32` | 2,540,000.00 USD | 2,540,000.00 USD | 66,820.00 USD | 4,060.00 USD | 16.44 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.32` | 2,810,000.00 USD | 2,810,000.00 USD | 220,640.00 USD | 0.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.33` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 109.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.34` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 2,210.00 USD | 13.84 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.34` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 4,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.35` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 16,880.00 USD | 16,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.36` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 17,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.36` | 2,580,000.00 USD | 2,580,000.00 USD | 223,170.00 USD | 0.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.37` | 2,410,000.00 USD | 2,410,000.00 USD | 691.75 USD | 6,430.00 USD | 16.86 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.38` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 5,940.00 USD | 50,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.38` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.39` | 2,350,000.00 USD | 2,350,000.00 USD | 100,740.00 USD | 13,620.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.40` | 2,200,000.00 USD | 2,200,000.00 USD | 10,500.00 USD | 7,000.00 USD | 51,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.40` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 7,600.00 USD | 86,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.41` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 2,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.42` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 6,250.00 USD | 42,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.42` | 2,190,000.00 USD | 2,190,000.00 USD | 210,920.00 USD | 0.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.43` | 2,080,000.00 USD | 2,080,000.00 USD | 45,340.00 USD | 7,730.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.44` | 2,020,000.00 USD | 2,020,000.00 USD | 11,130.00 USD | 27,610.00 USD | 160,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.44` | 1,940,000.00 USD | 1,940,000.00 USD | 10,480.00 USD | 8,000.00 USD | 51,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.45` | 1,820,000.00 USD | 1,820,000.00 USD | 54,790.00 USD | 0.00 USD | 163,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.46` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 124,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.46` | 1,870,000.00 USD | 1,870,000.00 USD | 152,650.00 USD | 0.00 USD | 119,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.47` | 1,480,000.00 USD | 1,480,000.00 USD | 663.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.48` | 1,480,000.00 USD | 1,480,000.00 USD | 749.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.48` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 49,360.00 USD | 152,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.49` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 12.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.50` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 68,460.00 USD | 127,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.50` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 112,310.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.51` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 21,730.00 USD | 172,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.52` | 1,090,000.00 USD | 1,090,000.00 USD | 183,950.00 USD | 25,890.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.52` | 1,280,000.00 USD | 1,280,000.00 USD | 114,580.00 USD | 135,400.00 USD | 92,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.53` | 873,020.00 USD | 873,020.00 USD | 33,590.00 USD | 32,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.54` | 806,900.00 USD | 806,900.00 USD | 202,800.00 USD | 3,210.00 USD | 156.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.54` | 941,740.00 USD | 941,740.00 USD | 357,740.00 USD | 136,470.00 USD | 2,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.55` | 600,730.00 USD | 600,730.00 USD | 152,290.00 USD | 0.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.56` | 423,320.00 USD | 423,320.00 USD | 139,040.00 USD | 38,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.56` | 445,520.00 USD | 445,520.00 USD | 151,290.00 USD | 122,650.00 USD | 790.79 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.57` | 245,960.00 USD | 245,960.00 USD | 181,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.58` | 64,300.00 USD | 64,300.00 USD | 59,120.00 USD | 5,060.00 USD | 118.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.58` | 170,790.00 USD | 170,790.00 USD | 4,370.00 USD | 164,810.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.59` | 21,360.00 USD | 21,360.00 USD | 0.00 USD | 21,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.59` | 42,720.00 USD | 42,720.00 USD | 0.00 USD | 21,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.60` | 71,090.00 USD | 71,090.00 USD | 2,040.00 USD | 26,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.60` | 2,020.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.61` | 72,280.00 USD | 72,280.00 USD | 497.00 USD | 0.00 USD | 699.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.62` | 261,400.00 USD | 261,400.00 USD | 41,980.00 USD | 26,090.00 USD | 121,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.62` | 33,350.00 USD | 33,350.00 USD | 2,810.00 USD | 0.00 USD | 28,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.63` | 405,370.00 USD | 405,370.00 USD | 104,180.00 USD | 39,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.64` | 450,440.00 USD | 450,440.00 USD | 0.00 USD | 6,540.00 USD | 38,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.64` | 122,390.00 USD | 122,390.00 USD | 0.00 USD | 12,800.00 USD | 76,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.65` | 556,460.00 USD | 556,460.00 USD | 3,580.00 USD | 6,810.00 USD | 95,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.66` | 812,210.00 USD | 812,210.00 USD | 145,440.00 USD | 31,810.00 USD | 78,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.66` | 337,190.00 USD | 337,190.00 USD | 191,350.00 USD | 22,640.00 USD | 804.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.67` | 1,010,000.00 USD | 1,010,000.00 USD | 6,430.00 USD | 3,750.00 USD | 190,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.68` | 1,120,000.00 USD | 1,120,000.00 USD | 68,460.00 USD | 12,020.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.68` | 923,760.00 USD | 923,760.00 USD | 207,090.00 USD | 43,100.00 USD | 336,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.69` | 209.31 USD | 209.31 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.69` | 1,180,000.00 USD | 1,180,000.00 USD | 10,820.00 USD | 16,260.00 USD | 33,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.70` | 1,270,000.00 USD | 1,270,000.00 USD | 62,600.00 USD | 0.00 USD | 23,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.70` | 1,130,000.00 USD | 1,130,000.00 USD | 116,370.00 USD | 41,840.00 USD | 46,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.71` | 1,290,000.00 USD | 1,290,000.00 USD | 18,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.72` | 1,360,000.00 USD | 1,360,000.00 USD | 16,840.00 USD | 2,520.00 USD | 50,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.72` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 609.73 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.73` | 1,430,000.00 USD | 1,430,000.00 USD | 12,580.00 USD | 28,810.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.74` | 1,480,000.00 USD | 1,480,000.00 USD | 38,500.00 USD | 3,500.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.74` | 1,210,000.00 USD | 1,210,000.00 USD | 51,030.00 USD | 30,470.00 USD | 686.63 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.75` | 1,530,000.00 USD | 1,530,000.00 USD | 33,520.00 USD | 4,580.00 USD | 4,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.76` | 1,670,000.00 USD | 1,670,000.00 USD | 82,470.00 USD | 0.00 USD | 57,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.76` | 1,470,000.00 USD | 1,470,000.00 USD | 196,960.00 USD | 0.00 USD | 58,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.77` | 1,830,000.00 USD | 1,830,000.00 USD | 119,730.00 USD | 2,060.00 USD | 43,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.78` | 1,940,000.00 USD | 1,940,000.00 USD | 41,500.00 USD | 20,740.00 USD | 50,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.78` | 1,590,000.00 USD | 1,590,000.00 USD | 2,300.00 USD | 8,000.00 USD | 110,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.79` | 2,020,000.00 USD | 2,020,000.00 USD | 31,710.00 USD | 12,000.00 USD | 29,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.80` | 2,160,000.00 USD | 2,160,000.00 USD | 100,610.00 USD | 14,490.00 USD | 23,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.80` | 1,680,000.00 USD | 1,680,000.00 USD | 27,360.00 USD | 33,750.00 USD | 32,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.81` | 2,180,000.00 USD | 2,180,000.00 USD | 18,670.00 USD | 2,240.00 USD | 42.52 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.82` | 2,200,000.00 USD | 2,200,000.00 USD | 2,200.00 USD | 0.00 USD | 19,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.82` | 1,880,000.00 USD | 1,880,000.00 USD | 201,040.00 USD | 0.00 USD | 547.66 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.82` | 6,000.00 USD | 6,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.83` | 2,280,000.00 USD | 2,280,000.00 USD | 73,290.00 USD | 12,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.84` | 2,360,000.00 USD | 2,360,000.00 USD | 1,500.00 USD | 0.00 USD | 73,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.85` | 2,390,000.00 USD | 2,390,000.00 USD | 13,040.00 USD | 3,360.00 USD | 11,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 2,390,000.00 USD | 2,390,000.00 USD | 1,910.00 USD | 0.00 USD | 607.55 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.86` | 2,000,000.00 USD | 2,000,000.00 USD | 29,310.00 USD | 0.00 USD | 83,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.87` | 2,400,000.00 USD | 2,400,000.00 USD | 1,350.00 USD | 0.00 USD | 8,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.88` | 2,410,000.00 USD | 2,410,000.00 USD | 803.70 USD | 10,670.00 USD | 186.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.88` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 28,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.89` | 2,450,000.00 USD | 2,450,000.00 USD | 3,660.00 USD | 3,410.00 USD | 32,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.90` | 2,580,000.00 USD | 2,580,000.00 USD | 28,580.00 USD | 5,990.00 USD | 96,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.90` | 2,140,000.00 USD | 2,140,000.00 USD | 2,440.00 USD | 0.00 USD | 116,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.91` | 2,640,000.00 USD | 2,640,000.00 USD | 32,240.00 USD | 11,620.00 USD | 13,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 2,640,000.00 USD | 2,640,000.00 USD | 1,110.00 USD | 1,020.00 USD | 67.52 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.92` | 2,280,000.00 USD | 2,280,000.00 USD | 99,150.00 USD | 0.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.93` | 2,710,000.00 USD | 2,710,000.00 USD | 31,830.00 USD | 1,810.00 USD | 38,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.94` | 2,760,000.00 USD | 2,760,000.00 USD | 32,580.00 USD | 12,260.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.94` | 2,340,000.00 USD | 2,340,000.00 USD | 58,330.00 USD | 0.00 USD | 433.10 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.95` | 235.07 USD | 6,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.95` | 2,790,000.00 USD | 2,790,000.00 USD | 2,540.00 USD | 4,240.00 USD | 20,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.96` | 2,790,000.00 USD | 2,790,000.00 USD | 1,260.00 USD | 0.00 USD | 175.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.96` | 2,370,000.00 USD | 2,370,000.00 USD | 3,320.00 USD | 4,000.00 USD | 26,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.98` | 2,850,000.00 USD | 2,850,000.00 USD | 35,320.00 USD | 7,700.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.98` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 9,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 2,930,000.00 USD | 2,930,000.00 USD | 48,100.00 USD | 24,940.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.99` | 539,710.00 USD | 546,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.00` | 2,980,000.00 USD | 2,980,000.00 USD | 36,960.00 USD | 0.00 USD | 8,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.00` | 2,710,000.00 USD | 2,710,000.00 USD | 298,640.00 USD | 11,360.00 USD | 21,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 3,010,000.00 USD | 3,010,000.00 USD | 1,980.00 USD | 12,030.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 3,080,000.00 USD | 3,080,000.00 USD | 39,120.00 USD | 33,630.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.02` | 2,850,000.00 USD | 2,850,000.00 USD | 82,280.00 USD | 56,120.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 3,260,000.00 USD | 3,260,000.00 USD | 125,760.00 USD | 14,810.00 USD | 34,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 3,330,000.00 USD | 3,330,000.00 USD | 40,880.00 USD | 10,710.00 USD | 21,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.04` | 3,080,000.00 USD | 3,080,000.00 USD | 135,320.00 USD | 74,750.00 USD | 16,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 3,400,000.00 USD | 3,400,000.00 USD | 21,500.00 USD | 13,500.00 USD | 29,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.06` | 3,440,000.00 USD | 3,440,000.00 USD | 27,800.00 USD | 6,890.00 USD | 12,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.06` | 3,150,000.00 USD | 3,150,000.00 USD | 7,440.00 USD | 14,960.00 USD | 53,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.07` | 3,510,000.00 USD | 3,510,000.00 USD | 13,580.00 USD | 18,880.00 USD | 30,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 3,560,000.00 USD | 3,560,000.00 USD | 13,510.00 USD | 3,370.00 USD | 39,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.08` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.09` | 880.34 USD | 547,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.09` | 3,700,000.00 USD | 3,700,000.00 USD | 88,250.00 USD | 11,440.00 USD | 31,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.10` | 3,760,000.00 USD | 3,760,000.00 USD | 16,430.00 USD | 16,280.00 USD | 36,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.10` | 4,430,000.00 USD | 4,430,000.00 USD | 826,500.00 USD | 35,760.00 USD | 334,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.11` | 3,920,000.00 USD | 3,920,000.00 USD | 61,080.00 USD | 14,420.00 USD | 82,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 4,070,000.00 USD | 4,070,000.00 USD | 102,100.00 USD | 22,410.00 USD | 26,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.12` | 5,420,000.00 USD | 5,420,000.00 USD | 465,780.00 USD | 24,170.00 USD | 503,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 4,200,000.00 USD | 4,200,000.00 USD | 75,050.00 USD | 15,960.00 USD | 40,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.14` | 4,270,000.00 USD | 4,270,000.00 USD | 30,520.00 USD | 3,380.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.14` | 6,470,000.00 USD | 6,470,000.00 USD | 536,560.00 USD | 18,540.00 USD | 500,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.15` | 4,370,000.00 USD | 4,370,000.00 USD | 57,140.00 USD | 23,170.00 USD | 22,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 4,490,000.00 USD | 4,490,000.00 USD | 63,930.00 USD | 23,900.00 USD | 32,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.16` | 7,070,000.00 USD | 7,070,000.00 USD | 358,370.00 USD | 44,360.00 USD | 195,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 4,630,000.00 USD | 4,630,000.00 USD | 80,620.00 USD | 3,200.00 USD | 49,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 4,710,000.00 USD | 4,710,000.00 USD | 28,620.00 USD | 26,430.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.18` | 8,090,000.00 USD | 8,090,000.00 USD | 566,340.00 USD | 162,460.00 USD | 292,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 4,830,000.00 USD | 4,830,000.00 USD | 77,850.00 USD | 29,140.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.20` | 4,940,000.00 USD | 4,940,000.00 USD | 64,620.00 USD | 11,090.00 USD | 37,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.20` | 9,020,000.00 USD | 9,020,000.00 USD | 549,250.00 USD | 134,550.00 USD | 238,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 4,980,000.00 USD | 4,980,000.00 USD | 29,720.00 USD | 2,950.00 USD | 4,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.21` | 1,870.00 USD | 548,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.22` | 5,050,000.00 USD | 5,050,000.00 USD | 58,850.00 USD | 2,850.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.22` | 10,200,000.00 USD | 10,200,000.00 USD | 620,010.00 USD | 144,840.00 USD | 416,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.23` | 5,050,000.00 USD | 5,050,000.00 USD | 883.09 USD | 4,270.00 USD | 17.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 5,100,000.00 USD | 5,100,000.00 USD | 45,960.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.24` | 10,770,000.00 USD | 10,770,000.00 USD | 336,360.00 USD | 56,410.00 USD | 174,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 5,140,000.00 USD | 5,140,000.00 USD | 17,320.00 USD | 5,840.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 5,140,000.00 USD | 5,140,000.00 USD | 1,260.00 USD | 0.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.26` | 11,200,000.00 USD | 11,200,000.00 USD | 273,920.00 USD | 96,980.00 USD | 60,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 5,170,000.00 USD | 5,170,000.00 USD | 23,580.00 USD | 1,360.00 USD | 6,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 5,180,000.00 USD | 5,180,000.00 USD | 1,530.00 USD | 8,760.00 USD | 169.17 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.28` | 11,900,000.00 USD | 11,900,000.00 USD | 428,160.00 USD | 103,490.00 USD | 170,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.29` | 5,220,000.00 USD | 5,220,000.00 USD | 16,190.00 USD | 4,140.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 3,860.00 USD | 552,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.30` | 5,280,000.00 USD | 5,280,000.00 USD | 39,850.00 USD | 7,520.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.30` | 12,460,000.00 USD | 12,460,000.00 USD | 199,810.00 USD | 97,780.00 USD | 262,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 5,330,000.00 USD | 5,330,000.00 USD | 27,750.00 USD | 5,020.00 USD | 12,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 5,340,000.00 USD | 5,340,000.00 USD | 9,610.00 USD | 0.00 USD | 5,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.32` | 13,130,000.00 USD | 13,130,000.00 USD | 271,660.00 USD | 59,310.00 USD | 338,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 5,360,000.00 USD | 5,360,000.00 USD | 7,990.00 USD | 6,000.00 USD | 8,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 5,420,000.00 USD | 5,420,000.00 USD | 46,210.00 USD | 3,660.00 USD | 3,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.34` | 13,470,000.00 USD | 13,470,000.00 USD | 216,530.00 USD | 53,150.00 USD | 70,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.35` | 5,440,000.00 USD | 5,440,000.00 USD | 13,620.00 USD | 0.00 USD | 14,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 5,460,000.00 USD | 5,460,000.00 USD | 4,730.00 USD | 6,760.00 USD | 8,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.36` | 13,890,000.00 USD | 13,890,000.00 USD | 247,120.00 USD | 73,430.00 USD | 97,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 5,490,000.00 USD | 5,490,000.00 USD | 12,900.00 USD | 5,670.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 5,510,000.00 USD | 5,510,000.00 USD | 15,290.00 USD | 0.00 USD | 13,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.38` | 14,270,000.00 USD | 14,270,000.00 USD | 277,080.00 USD | 31,100.00 USD | 77,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.39` | 5,520,000.00 USD | 5,520,000.00 USD | 9,080.00 USD | 0.00 USD | 12.70 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.40` | 5,550,000.00 USD | 5,550,000.00 USD | 22,270.00 USD | 0.00 USD | 12.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.40` | 14,680,000.00 USD | 14,680,000.00 USD | 234,760.00 USD | 42,520.00 USD | 124,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.41` | 5,560,000.00 USD | 5,560,000.00 USD | 963.73 USD | 0.00 USD | 10,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 440.06 USD | 553,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 5,580,000.00 USD | 5,580,000.00 USD | 9,100.00 USD | 2,390.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.42` | 14,870,000.00 USD | 14,870,000.00 USD | 108,840.00 USD | 19,780.00 USD | 70,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.43` | 5,580,000.00 USD | 5,580,000.00 USD | 5,380.00 USD | 700.38 USD | 20.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 5,580,000.00 USD | 5,580,000.00 USD | 795.69 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.44` | 15,040,000.00 USD | 15,040,000.00 USD | 80,230.00 USD | 19,420.00 USD | 63,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.45` | 5,590,000.00 USD | 5,590,000.00 USD | 96.25 USD | 0.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.46` | 5,600,000.00 USD | 5,600,000.00 USD | 9,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.46` | 15,140,000.00 USD | 15,140,000.00 USD | 60,810.00 USD | 17,010.00 USD | 19,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.47` | 5,610,000.00 USD | 5,610,000.00 USD | 1,050.00 USD | 1,250.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.48` | 5,610,000.00 USD | 5,610,000.00 USD | 38.30 USD | 0.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.48` | 15,190,000.00 USD | 15,190,000.00 USD | 12,180.00 USD | 11,060.00 USD | 35,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.49` | 5,640,000.00 USD | 5,640,000.00 USD | 20,610.00 USD | 572.85 USD | 5,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.50` | 5,640,000.00 USD | 5,640,000.00 USD | 4,500.00 USD | 930.34 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.50` | 15,310,000.00 USD | 15,310,000.00 USD | 65,230.00 USD | 9,430.00 USD | 45,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.52` | 15,440,000.00 USD | 15,440,000.00 USD | 46,900.00 USD | 23,260.00 USD | 51,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.54` | 15,550,000.00 USD | 15,550,000.00 USD | 87,890.00 USD | 25,090.00 USD | 930.52 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.56` | 15,600,000.00 USD | 15,600,000.00 USD | 35,290.00 USD | 5,260.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.58` | 15,660,000.00 USD | 15,660,000.00 USD | 35,340.00 USD | 2,380.00 USD | 27,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.60` | 15,720,000.00 USD | 15,720,000.00 USD | 38,740.00 USD | 5,460.00 USD | 18,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.62` | 15,770,000.00 USD | 15,770,000.00 USD | 36,420.00 USD | 1,540.00 USD | 10,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.62` | 138.98 USD | 553,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.64` | 15,840,000.00 USD | 15,840,000.00 USD | 33,970.00 USD | 11,240.00 USD | 19,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.64` | 1,930.00 USD | 555,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.66` | 15,910,000.00 USD | 15,910,000.00 USD | 37,340.00 USD | 12,890.00 USD | 18,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.68` | 15,990,000.00 USD | 15,990,000.00 USD | 56,110.00 USD | 8,420.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.70` | 16,080,000.00 USD | 16,080,000.00 USD | 50,240.00 USD | 9,960.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.72` | 16,140,000.00 USD | 16,140,000.00 USD | 24,700.00 USD | 6,920.00 USD | 26,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 555,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.74` | 16,180,000.00 USD | 16,180,000.00 USD | 17,650.00 USD | 7,200.00 USD | 18,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.35` | 2,650.00 USD | 558,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.48` | 20,970.00 USD | 579,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 579,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.73` | 302.19 USD | 579,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.76` | 4,050.00 USD | 583,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.77` | 257.93 USD | 584,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.81` | 1,150.00 USD | 585,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.89` | 100.13 USD | 585,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.99` | 54,980.00 USD | 640,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 647,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.13` | 111,350.00 USD | 758,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 11,670.00 USD | 770,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 782,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.69` | 296,760.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.80` | 114.27 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.93` | 505.74 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.95` | 1,050.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.78` | 62,750.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.31` | 282.43 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.53` | 521.30 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.88` | 244.10 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.02` | 4,170.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.10` | 325.30 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.38` | 20,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.72` | 167.79 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.77` | 185.55 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.82` | 1,700.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.27` | 23,750.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.32` | 23,090.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.36` | 265,080.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 117.71 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.82` | 84,760.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.98` | 1,690.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.00` | 1,940.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.02` | 191.87 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.05` | 207.78 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.07` | 6,740.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.78` | 2,280,000.00 USD | 0.00 USD | 205.28 USD | `-79.23%` | `115.00` |
| `Live` | `Long` | `1.94` | 2,280,000.00 USD | 0.00 USD | 214.42 USD | `-77.48%` | `110.81` |
| `Live` | `Long` | `2.00` | 2,280,000.00 USD | 0.00 USD | 160.40 USD | `-76.67%` | `80.00` |
| `Live` | `Long` | `2.04` | 2,280,000.00 USD | 0.00 USD | 110.52 USD | `-76.32%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,280,000.00 USD | 0.00 USD | 236.32 USD | `-76.09%` | `115.00` |
| `Live` | `Long` | `2.06` | 2,280,000.00 USD | 0.00 USD | 5,160.00 USD | `-75.97%` | `2,497.76` |
| `Live` | `Long` | `2.12` | 2,270,000.00 USD | 0.00 USD | 106.59 USD | `-75.27%` | `50.16` |
| `Live` | `Long` | `2.17` | 2,270,000.00 USD | 0.00 USD | 248.97 USD | `-74.81%` | `115.00` |
| `Live` | `Long` | `2.56` | 2,270,000.00 USD | 0.00 USD | 133.38 USD | `-70.15%` | `52.00` |
| `Live` | `Long` | `2.69` | 2,270,000.00 USD | 0.00 USD | 942.44 USD | `-68.76%` | `351.00` |
| `Live` | `Long` | `2.73` | 2,270,000.00 USD | 0.00 USD | 313.38 USD | `-68.29%` | `115.00` |
| `Live` | `Long` | `2.77` | 2,270,000.00 USD | 0.00 USD | 19,400.00 USD | `-67.71%` | `6,990.57` |
| `Live` | `Long` | `2.87` | 2,250,000.00 USD | 0.00 USD | 232.67 USD | `-66.66%` | `81.21` |
| `Live` | `Long` | `2.94` | 2,250,000.00 USD | 0.00 USD | 44,510.00 USD | `-65.85%` | `15,165.76` |
| `Live` | `Long` | `2.98` | 2,210,000.00 USD | 0.00 USD | 111.12 USD | `-65.38%` | `37.35` |
| `Live` | `Long` | `3.13` | 2,210,000.00 USD | 0.00 USD | 23,400.00 USD | `-63.52%` | `7,465.11` |
| `Live` | `Long` | `3.15` | 2,180,000.00 USD | 0.00 USD | 1,260.00 USD | `-63.29%` | `400.00` |
| `Live` | `Long` | `3.31` | 2,180,000.00 USD | 0.00 USD | 1,250.00 USD | `-61.54%` | `377.71` |
| `Live` | `Long` | `3.35` | 2,180,000.00 USD | 0.00 USD | 544.70 USD | `-61.07%` | `162.84` |
| `Live` | `Long` | `3.37` | 2,180,000.00 USD | 0.00 USD | 389.53 USD | `-60.84%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,180,000.00 USD | 0.00 USD | 151.88 USD | `-60.73%` | `45.00` |
| `Live` | `Long` | `3.38` | 2,180,000.00 USD | 0.00 USD | 6,770.00 USD | `-60.61%` | `2,000.00` |
| `Live` | `Long` | `3.54` | 2,170,000.00 USD | 0.00 USD | 392.22 USD | `-58.75%` | `110.64` |
| `Live` | `Long` | `3.67` | 2,170,000.00 USD | 0.00 USD | 109.95 USD | `-57.35%` | `30.00` |
| `Live` | `Long` | `3.75` | 2,170,000.00 USD | 0.00 USD | 1,500.00 USD | `-56.30%` | `400.00` |
| `Live` | `Long` | `3.90` | 2,170,000.00 USD | 0.00 USD | 131.73 USD | `-54.67%` | `33.82` |
| `Live` | `Long` | `3.98` | 2,170,000.00 USD | 0.00 USD | 254.04 USD | `-53.63%` | `63.75` |
| `Live` | `Long` | `4.03` | 2,170,000.00 USD | 0.00 USD | 3,080.00 USD | `-53.16%` | `766.25` |
| `Live` | `Long` | `4.04` | 2,170,000.00 USD | 0.00 USD | 152.29 USD | `-52.93%` | `37.65` |
| `Live` | `Long` | `4.09` | 2,170,000.00 USD | 0.00 USD | 382.15 USD | `-52.35%` | `93.32` |
| `Live` | `Long` | `4.14` | 2,170,000.00 USD | 0.00 USD | 159.29 USD | `-51.77%` | `38.43` |
| `Live` | `Long` | `4.22` | 2,170,000.00 USD | 0.00 USD | 195.49 USD | `-50.83%` | `46.27` |
| `Live` | `Long` | `4.24` | 2,170,000.00 USD | 0.00 USD | 169.40 USD | `-50.72%` | `40.00` |
| `Live` | `Long` | `4.42` | 2,170,000.00 USD | 0.00 USD | 459.01 USD | `-48.51%` | `103.73` |
| `Live` | `Long` | `4.45` | 2,170,000.00 USD | 0.00 USD | 110.77 USD | `-48.27%` | `24.92` |
| `Live` | `Long` | `4.54` | 2,170,000.00 USD | 0.00 USD | 195.75 USD | `-47.11%` | `43.07` |
| `Live` | `Long` | `4.59` | 2,170,000.00 USD | 0.00 USD | 30,970.00 USD | `-46.53%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,140,000.00 USD | 0.00 USD | 486.93 USD | `-46.30%` | `105.51` |
| `Live` | `Long` | `4.62` | 2,140,000.00 USD | 0.00 USD | 2,930.00 USD | `-46.18%` | `634.06` |
| `Live` | `Long` | `4.66` | 2,130,000.00 USD | 0.00 USD | 105.11 USD | `-45.83%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,130,000.00 USD | 0.00 USD | 3,280.00 USD | `-45.71%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,130,000.00 USD | 0.00 USD | 1,490.00 USD | `-45.60%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,130,000.00 USD | 0.00 USD | 8,890.00 USD | `-45.48%` | `1,897.97` |
| `Live` | `Long` | `4.70` | 2,120,000.00 USD | 0.00 USD | 7,040.00 USD | `-45.37%` | `1,500.00` |
| `Live` | `Long` | `4.76` | 2,110,000.00 USD | 0.00 USD | 105.64 USD | `-44.55%` | `22.17` |
| `Live` | `Long` | `4.78` | 2,110,000.00 USD | 0.00 USD | 112.02 USD | `-44.43%` | `23.46` |
| `Live` | `Long` | `4.83` | 2,110,000.00 USD | 0.00 USD | 467.01 USD | `-43.74%` | `96.59` |
| `Live` | `Long` | `4.91` | 2,110,000.00 USD | 0.00 USD | 3,880.00 USD | `-42.92%` | `790.61` |
| `Live` | `Long` | `4.92` | 2,110,000.00 USD | 0.00 USD | 1,230.00 USD | `-42.80%` | `251.00` |
| `Live` | `Long` | `4.93` | 2,110,000.00 USD | 0.00 USD | 16,220.00 USD | `-42.57%` | `3,286.00` |
| `Live` | `Long` | `4.95` | 2,090,000.00 USD | 0.00 USD | 352.68 USD | `-42.46%` | `71.32` |
| `Live` | `Long` | `4.96` | 2,090,000.00 USD | 0.00 USD | 945.36 USD | `-42.34%` | `190.79` |
| `Live` | `Long` | `4.96` | 2,090,000.00 USD | 0.00 USD | 4,090.00 USD | `-42.22%` | `824.62` |
| `Live` | `Long` | `4.97` | 2,080,000.00 USD | 0.00 USD | 282.23 USD | `-42.11%` | `56.73` |
| `Live` | `Long` | `4.99` | 2,080,000.00 USD | 0.00 USD | 727.71 USD | `-41.99%` | `145.98` |
| `Live` | `Long` | `5.00` | 2,080,000.00 USD | 0.00 USD | 269.53 USD | `-41.87%` | `53.96` |
| `Live` | `Long` | `5.01` | 2,080,000.00 USD | 0.00 USD | 56,390.00 USD | `-41.64%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,030,000.00 USD | 0.00 USD | 167.78 USD | `-41.52%` | `33.39` |
| `Live` | `Long` | `5.04` | 2,030,000.00 USD | 0.00 USD | 314.59 USD | `-41.41%` | `62.48` |
| `Live` | `Long` | `5.05` | 2,030,000.00 USD | 0.00 USD | 710.03 USD | `-41.18%` | `140.46` |
| `Live` | `Long` | `5.08` | 2,030,000.00 USD | 0.00 USD | 213.20 USD | `-40.94%` | `42.01` |
| `Live` | `Long` | `5.08` | 2,030,000.00 USD | 0.00 USD | 105.46 USD | `-40.83%` | `20.74` |
| `Live` | `Long` | `5.09` | 2,030,000.00 USD | 0.00 USD | 651.75 USD | `-40.71%` | `127.92` |
| `Live` | `Long` | `5.12` | 2,020,000.00 USD | 0.00 USD | 3,470.00 USD | `-40.48%` | `678.97` |
| `Live` | `Long` | `5.12` | 2,020,000.00 USD | 0.00 USD | 5,650.00 USD | `-40.36%` | `1,101.82` |
| `Live` | `Long` | `5.13` | 2,020,000.00 USD | 0.00 USD | 1,030.00 USD | `-40.24%` | `200.33` |
| `Live` | `Long` | `5.17` | 2,010,000.00 USD | 0.00 USD | 1,620.00 USD | `-39.78%` | `312.94` |
| `Live` | `Long` | `5.18` | 2,010,000.00 USD | 0.00 USD | 150.57 USD | `-39.66%` | `29.04` |
| `Live` | `Long` | `5.20` | 2,010,000.00 USD | 0.00 USD | 979.05 USD | `-39.55%` | `188.46` |
| `Live` | `Long` | `5.21` | 2,010,000.00 USD | 0.00 USD | 300.91 USD | `-39.31%` | `57.70` |
| `Live` | `Long` | `5.25` | 2,010,000.00 USD | 0.00 USD | 160,990.00 USD | `-38.85%` | `30,635.20` |
| `Live` | `Long` | `5.26` | 1,850,000.00 USD | 0.00 USD | 2,230.00 USD | `-38.73%` | `423.54` |
| `Live` | `Long` | `5.29` | 1,850,000.00 USD | 0.00 USD | 640.70 USD | `-38.50%` | `121.23` |
| `Live` | `Long` | `5.32` | 1,850,000.00 USD | 0.00 USD | 232.85 USD | `-38.15%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,850,000.00 USD | 0.00 USD | 716.11 USD | `-38.03%` | `134.48` |
| `Live` | `Long` | `5.39` | 1,850,000.00 USD | 0.00 USD | 660.46 USD | `-37.22%` | `122.42` |
| `Live` | `Long` | `5.41` | 1,850,000.00 USD | 0.00 USD | 260.63 USD | `-37.10%` | `48.22` |
| `Live` | `Long` | `5.42` | 1,850,000.00 USD | 0.00 USD | 20,160.00 USD | `-36.99%` | `3,723.69` |
| `Live` | `Long` | `5.42` | 1,830,000.00 USD | 0.00 USD | 160,400.00 USD | `-36.87%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,660,000.00 USD | 0.00 USD | 2,830.00 USD | `-36.75%` | `520.00` |
| `Live` | `Long` | `5.46` | 1,660,000.00 USD | 0.00 USD | 264.72 USD | `-36.40%` | `48.44` |
| `Live` | `Long` | `5.47` | 1,660,000.00 USD | 0.00 USD | 1,320.00 USD | `-36.29%` | `240.95` |
| `Live` | `Long` | `5.49` | 1,660,000.00 USD | 0.00 USD | 354.06 USD | `-36.17%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,660,000.00 USD | 0.00 USD | 19,290.00 USD | `-36.06%` | `3,510.41` |
| `Live` | `Long` | `5.51` | 1,640,000.00 USD | 0.00 USD | 367.41 USD | `-35.82%` | `66.62` |
| `Live` | `Long` | `5.54` | 1,640,000.00 USD | 0.00 USD | 4,180.00 USD | `-35.47%` | `753.23` |
| `Live` | `Long` | `5.58` | 1,640,000.00 USD | 0.00 USD | 63,260.00 USD | `-35.12%` | `11,347.58` |
| `Live` | `Long` | `5.59` | 1,570,000.00 USD | 0.00 USD | 34,430.00 USD | `-34.89%` | `6,153.60` |
| `Live` | `Long` | `5.62` | 1,540,000.00 USD | 0.00 USD | 2,810.00 USD | `-34.66%` | `500.00` |
| `Live` | `Long` | `5.63` | 1,540,000.00 USD | 0.00 USD | 468.55 USD | `-34.43%` | `83.15` |
| `Live` | `Long` | `5.71` | 1,540,000.00 USD | 0.00 USD | 147.33 USD | `-33.50%` | `25.78` |
| `Live` | `Long` | `5.72` | 1,540,000.00 USD | 0.00 USD | 2,390.00 USD | `-33.38%` | `417.17` |
| `Live` | `Long` | `5.74` | 1,530,000.00 USD | 0.00 USD | 661.65 USD | `-33.26%` | `115.37` |
| `Live` | `Long` | `5.75` | 1,530,000.00 USD | 0.00 USD | 125.70 USD | `-33.15%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,530,000.00 USD | 0.00 USD | 3,190.00 USD | `-33.03%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,530,000.00 USD | 0.00 USD | 10,850.00 USD | `-32.91%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,520,000.00 USD | 0.00 USD | 801.40 USD | `-32.80%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,520,000.00 USD | 0.00 USD | 635.31 USD | `-32.56%` | `109.63` |
| `Live` | `Long` | `5.80` | 1,520,000.00 USD | 0.00 USD | 580.50 USD | `-32.45%` | `100.00` |
| `Live` | `Long` | `5.82` | 1,520,000.00 USD | 0.00 USD | 106.65 USD | `-32.33%` | `18.34` |
| `Live` | `Long` | `5.83` | 1,520,000.00 USD | 0.00 USD | 145.88 USD | `-32.10%` | `25.00` |
| `Live` | `Long` | `5.86` | 1,520,000.00 USD | 0.00 USD | 2,110.00 USD | `-31.87%` | `360.33` |
| `Live` | `Long` | `5.89` | 1,510,000.00 USD | 0.00 USD | 984.70 USD | `-31.40%` | `167.04` |
| `Live` | `Long` | `5.91` | 1,510,000.00 USD | 0.00 USD | 399.18 USD | `-31.28%` | `67.60` |
| `Live` | `Long` | `5.92` | 1,510,000.00 USD | 0.00 USD | 277.35 USD | `-31.17%` | `46.89` |
| `Live` | `Long` | `5.96` | 1,510,000.00 USD | 0.00 USD | 11,720.00 USD | `-30.70%` | `1,968.19` |
| `Live` | `Long` | `5.96` | 1,500,000.00 USD | 0.00 USD | 6,320.00 USD | `-30.59%` | `1,060.32` |
| `Live` | `Long` | `5.97` | 1,490,000.00 USD | 0.00 USD | 585.97 USD | `-30.47%` | `98.07` |
| `Live` | `Long` | `6.00` | 1,490,000.00 USD | 0.00 USD | 341.56 USD | `-30.12%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,490,000.00 USD | 0.00 USD | 446.85 USD | `-30.00%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,490,000.00 USD | 0.00 USD | 437.84 USD | `-29.66%` | `72.43` |
| `Live` | `Long` | `6.05` | 1,490,000.00 USD | 0.00 USD | 1,310.00 USD | `-29.54%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,490,000.00 USD | 0.00 USD | 265.10 USD | `-29.42%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,490,000.00 USD | 0.00 USD | 1,690.00 USD | `-29.31%` | `278.94` |
| `Live` | `Long` | `6.08` | 1,490,000.00 USD | 0.00 USD | 405.14 USD | `-29.19%` | `66.58` |
| `Live` | `Long` | `6.09` | 1,490,000.00 USD | 0.00 USD | 3,130.00 USD | `-29.07%` | `512.81` |
| `Live` | `Long` | `6.12` | 1,490,000.00 USD | 0.00 USD | 1,140.00 USD | `-28.84%` | `185.96` |
| `Live` | `Long` | `6.12` | 1,480,000.00 USD | 0.00 USD | 137.02 USD | `-28.72%` | `22.37` |
| `Live` | `Long` | `6.13` | 1,480,000.00 USD | 0.00 USD | 2,030.00 USD | `-28.61%` | `330.65` |
| `Live` | `Long` | `6.14` | 1,480,000.00 USD | 0.00 USD | 238.61 USD | `-28.49%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,480,000.00 USD | 0.00 USD | 7,810.00 USD | `-28.38%` | `1,268.30` |
| `Live` | `Long` | `6.17` | 1,470,000.00 USD | 0.00 USD | 104.36 USD | `-28.14%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,470,000.00 USD | 0.00 USD | 310.25 USD | `-27.79%` | `50.00` |
| `Live` | `Long` | `6.25` | 1,470,000.00 USD | 0.00 USD | 3,390.00 USD | `-27.21%` | `541.96` |
| `Live` | `Long` | `6.28` | 1,470,000.00 USD | 0.00 USD | 2,510.00 USD | `-26.98%` | `400.00` |
| `Live` | `Long` | `6.30` | 1,470,000.00 USD | 0.00 USD | 1,420.00 USD | `-26.63%` | `225.14` |
| `Live` | `Long` | `6.33` | 1,470,000.00 USD | 0.00 USD | 354,850.00 USD | `-26.40%` | `56,103.27` |
| `Live` | `Long` | `6.33` | 1,110,000.00 USD | 0.00 USD | 1,470.00 USD | `-26.28%` | `232.17` |
| `Live` | `Long` | `6.36` | 1,110,000.00 USD | 0.00 USD | 4,470.00 USD | `-26.05%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,110,000.00 USD | 0.00 USD | 284,770.00 USD | `-25.93%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 820,660.00 USD | 0.00 USD | 1,310.00 USD | `-25.82%` | `204.92` |
| `Live` | `Long` | `6.38` | 819,350.00 USD | 0.00 USD | 5,120.00 USD | `-25.70%` | `801.31` |
| `Live` | `Long` | `6.42` | 814,230.00 USD | 0.00 USD | 306.32 USD | `-25.35%` | `47.75` |
| `Live` | `Long` | `6.42` | 813,930.00 USD | 0.00 USD | 484.64 USD | `-25.23%` | `75.43` |
| `Live` | `Long` | `6.43` | 813,440.00 USD | 0.00 USD | 6,780.00 USD | `-25.12%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 806,670.00 USD | 0.00 USD | 1,050.00 USD | `-24.77%` | `162.75` |
| `Live` | `Long` | `6.50` | 805,620.00 USD | 0.00 USD | 1,490.00 USD | `-24.30%` | `228.41` |
| `Live` | `Long` | `6.54` | 804,130.00 USD | 0.00 USD | 852.03 USD | `-23.95%` | `130.38` |
| `Live` | `Long` | `6.54` | 803,280.00 USD | 0.00 USD | 8,970.00 USD | `-23.84%` | `1,370.89` |
| `Live` | `Long` | `6.57` | 794,310.00 USD | 0.00 USD | 1,520.00 USD | `-23.60%` | `231.02` |
| `Live` | `Long` | `6.58` | 792,790.00 USD | 0.00 USD | 1,770.00 USD | `-23.37%` | `269.14` |
| `Live` | `Long` | `6.59` | 791,020.00 USD | 0.00 USD | 1,260.00 USD | `-23.26%` | `190.72` |
| `Live` | `Long` | `6.62` | 789,760.00 USD | 0.00 USD | 2,110.00 USD | `-23.02%` | `318.57` |
| `Live` | `Long` | `6.62` | 787,650.00 USD | 0.00 USD | 364.90 USD | `-22.91%` | `55.08` |
| `Live` | `Long` | `6.63` | 787,290.00 USD | 0.00 USD | 245.89 USD | `-22.79%` | `37.06` |
| `Live` | `Long` | `6.67` | 787,040.00 USD | 0.00 USD | 1,320.00 USD | `-22.32%` | `198.12` |
| `Live` | `Long` | `6.68` | 785,720.00 USD | 0.00 USD | 3,160.00 USD | `-22.21%` | `472.28` |
| `Live` | `Long` | `6.71` | 782,560.00 USD | 0.00 USD | 16,570.00 USD | `-21.98%` | `2,471.72` |
| `Live` | `Long` | `6.71` | 765,990.00 USD | 0.00 USD | 6,180.00 USD | `-21.86%` | `920.74` |
| `Live` | `Long` | `6.75` | 759,810.00 USD | 0.00 USD | 1,330.00 USD | `-21.51%` | `196.95` |
| `Live` | `Long` | `6.78` | 758,480.00 USD | 0.00 USD | 7,990.00 USD | `-21.16%` | `1,179.83` |
| `Live` | `Long` | `6.79` | 750,480.00 USD | 0.00 USD | 22,360.00 USD | `-21.04%` | `3,295.99` |
| `Live` | `Long` | `6.79` | 728,120.00 USD | 0.00 USD | 4,720.00 USD | `-20.93%` | `694.73` |
| `Live` | `Long` | `6.80` | 723,400.00 USD | 0.00 USD | 1,500.00 USD | `-20.81%` | `220.95` |
| `Live` | `Long` | `6.82` | 721,900.00 USD | 0.00 USD | 7,230.00 USD | `-20.69%` | `1,061.04` |
| `Live` | `Long` | `6.83` | 714,670.00 USD | 0.00 USD | 158.14 USD | `-20.58%` | `23.17` |
| `Live` | `Long` | `6.87` | 714,510.00 USD | 0.00 USD | 3,710.00 USD | `-20.11%` | `540.58` |
| `Live` | `Long` | `6.88` | 710,800.00 USD | 0.00 USD | 1,580.00 USD | `-19.88%` | `229.18` |
| `Live` | `Long` | `6.92` | 709,220.00 USD | 0.00 USD | 579.62 USD | `-19.41%` | `83.70` |
| `Live` | `Long` | `6.93` | 708,640.00 USD | 0.00 USD | 3,500.00 USD | `-19.30%` | `504.07` |
| `Live` | `Long` | `6.95` | 705,140.00 USD | 0.00 USD | 3,980.00 USD | `-19.18%` | `572.68` |
| `Live` | `Long` | `6.96` | 701,170.00 USD | 0.00 USD | 3,480.00 USD | `-19.07%` | `500.00` |
| `Live` | `Long` | `6.96` | 697,690.00 USD | 0.00 USD | 636.74 USD | `-18.95%` | `91.42` |
| `Live` | `Long` | `6.97` | 697,050.00 USD | 0.00 USD | 128,810.00 USD | `-18.83%` | `18,466.99` |
| `Live` | `Long` | `6.99` | 568,240.00 USD | 0.00 USD | 297.49 USD | `-18.72%` | `42.59` |
| `Live` | `Long` | `7.00` | 567,950.00 USD | 0.00 USD | 746.58 USD | `-18.60%` | `106.73` |
| `Live` | `Long` | `7.00` | 567,200.00 USD | 0.00 USD | 175.12 USD | `-18.48%` | `25.00` |
| `Live` | `Long` | `7.01` | 567,020.00 USD | 0.00 USD | 20,890.00 USD | `-18.37%` | `2,978.11` |
| `Live` | `Long` | `7.03` | 546,130.00 USD | 0.00 USD | 1,370.00 USD | `-18.25%` | `194.51` |
| `Live` | `Long` | `7.07` | 544,770.00 USD | 0.00 USD | 23,960.00 USD | `-17.79%` | `3,390.75` |
| `Live` | `Long` | `7.08` | 520,810.00 USD | 0.00 USD | 7,420.00 USD | `-17.67%` | `1,048.27` |
| `Live` | `Long` | `7.08` | 513,390.00 USD | 0.00 USD | 1,050.00 USD | `-17.55%` | `148.63` |
| `Live` | `Long` | `7.09` | 512,340.00 USD | 0.00 USD | 2,130.00 USD | `-17.44%` | `300.00` |
| `Live` | `Long` | `7.11` | 510,210.00 USD | 0.00 USD | 28,530.00 USD | `-17.32%` | `4,015.35` |
| `Live` | `Long` | `7.12` | 481,680.00 USD | 0.00 USD | 379.66 USD | `-17.20%` | `53.36` |
| `Live` | `Long` | `7.13` | 481,300.00 USD | 0.00 USD | 777.50 USD | `-16.97%` | `108.97` |
| `Live` | `Long` | `7.14` | 480,530.00 USD | 0.00 USD | 20,270.00 USD | `-16.85%` | `2,837.00` |
| `Live` | `Long` | `7.17` | 460,260.00 USD | 0.00 USD | 2,380.00 USD | `-16.51%` | `331.12` |
| `Live` | `Long` | `7.18` | 457,880.00 USD | 0.00 USD | 31,620.00 USD | `-16.39%` | `4,400.95` |
| `Live` | `Long` | `7.21` | 426,260.00 USD | 0.00 USD | 2,100.00 USD | `-16.16%` | `291.40` |
| `Live` | `Long` | `7.21` | 424,160.00 USD | 0.00 USD | 322.94 USD | `-16.04%` | `44.76` |
| `Live` | `Long` | `7.24` | 423,840.00 USD | 0.00 USD | 1,480.00 USD | `-15.81%` | `205.21` |
| `Live` | `Long` | `7.25` | 422,350.00 USD | 0.00 USD | 185.83 USD | `-15.69%` | `25.65` |
| `Live` | `Long` | `7.25` | 422,170.00 USD | 0.00 USD | 21,280.00 USD | `-15.57%` | `2,933.17` |
| `Live` | `Long` | `7.29` | 400,890.00 USD | 0.00 USD | 36,420.00 USD | `-15.23%` | `5,000.00` |
| `Live` | `Long` | `7.29` | 364,460.00 USD | 0.00 USD | 1,680.00 USD | `-15.11%` | `230.97` |
| `Live` | `Long` | `7.30` | 362,780.00 USD | 0.00 USD | 1,020.00 USD | `-14.99%` | `140.00` |
| `Live` | `Long` | `7.33` | 361,750.00 USD | 0.00 USD | 13,110.00 USD | `-14.64%` | `1,787.05` |
| `Live` | `Long` | `7.34` | 348,650.00 USD | 0.00 USD | 5,250.00 USD | `-14.53%` | `715.45` |
| `Live` | `Long` | `7.37` | 343,390.00 USD | 0.00 USD | 2,940.00 USD | `-14.29%` | `399.15` |
| `Live` | `Long` | `7.38` | 340,450.00 USD | 0.00 USD | 1,100.00 USD | `-14.18%` | `148.75` |
| `Live` | `Long` | `7.38` | 339,350.00 USD | 0.00 USD | 227.97 USD | `-14.06%` | `30.87` |
| `Live` | `Long` | `7.42` | 339,130.00 USD | 0.00 USD | 147.61 USD | `-13.60%` | `19.88` |
| `Live` | `Long` | `7.43` | 338,980.00 USD | 0.00 USD | 2,430.00 USD | `-13.48%` | `327.05` |
| `Live` | `Long` | `7.45` | 336,550.00 USD | 0.00 USD | 2,410.00 USD | `-13.36%` | `324.35` |
| `Live` | `Long` | `7.46` | 334,130.00 USD | 0.00 USD | 10,390.00 USD | `-13.25%` | `1,393.53` |
| `Live` | `Long` | `7.46` | 323,740.00 USD | 0.00 USD | 4,590.00 USD | `-13.13%` | `614.36` |
| `Live` | `Long` | `7.47` | 319,160.00 USD | 0.00 USD | 1,120.00 USD | `-13.01%` | `149.52` |
| `Live` | `Long` | `7.50` | 318,040.00 USD | 0.00 USD | 962.81 USD | `-12.78%` | `128.46` |
| `Live` | `Long` | `7.50` | 317,080.00 USD | 0.00 USD | 421.78 USD | `-12.67%` | `56.20` |
| `Live` | `Long` | `7.51` | 316,660.00 USD | 0.00 USD | 1,710.00 USD | `-12.55%` | `228.21` |
| `Live` | `Long` | `7.53` | 314,940.00 USD | 0.00 USD | 1,570.00 USD | `-12.43%` | `208.52` |
| `Live` | `Long` | `7.54` | 313,370.00 USD | 0.00 USD | 4,210.00 USD | `-12.32%` | `559.01` |
| `Live` | `Long` | `7.54` | 309,160.00 USD | 0.00 USD | 1,510.00 USD | `-12.20%` | `200.00` |
| `Live` | `Long` | `7.55` | 307,650.00 USD | 0.00 USD | 415.52 USD | `-12.08%` | `55.00` |
| `Live` | `Long` | `7.57` | 307,230.00 USD | 0.00 USD | 25,060.00 USD | `-11.97%` | `3,312.23` |
| `Live` | `Long` | `7.58` | 282,180.00 USD | 0.00 USD | 118.25 USD | `-11.85%` | `15.61` |
| `Live` | `Long` | `7.59` | 282,060.00 USD | 0.00 USD | 26,390.00 USD | `-11.62%` | `3,474.36` |
| `Live` | `Long` | `7.61` | 255,670.00 USD | 0.00 USD | 935.87 USD | `-11.50%` | `123.06` |
| `Live` | `Long` | `7.62` | 254,740.00 USD | 0.00 USD | 754.04 USD | `-11.39%` | `99.02` |
| `Live` | `Long` | `7.62` | 253,980.00 USD | 0.00 USD | 787.51 USD | `-11.27%` | `103.28` |
| `Live` | `Long` | `7.63` | 253,190.00 USD | 0.00 USD | 378.93 USD | `-11.15%` | `49.63` |
| `Live` | `Long` | `7.66` | 252,820.00 USD | 0.00 USD | 135.42 USD | `-10.92%` | `17.69` |
| `Live` | `Long` | `7.67` | 252,680.00 USD | 0.00 USD | 256.09 USD | `-10.80%` | `33.41` |
| `Live` | `Long` | `7.67` | 252,420.00 USD | 0.00 USD | 4,480.00 USD | `-10.69%` | `583.63` |
| `Live` | `Long` | `7.68` | 247,940.00 USD | 0.00 USD | 739.30 USD | `-10.57%` | `96.20` |
| `Live` | `Long` | `7.70` | 247,200.00 USD | 0.00 USD | 6,690.00 USD | `-10.45%` | `869.22` |
| `Live` | `Long` | `7.75` | 240,520.00 USD | 0.00 USD | 500.12 USD | `-9.76%` | `64.49` |
| `Live` | `Long` | `7.76` | 240,020.00 USD | 0.00 USD | 455.73 USD | `-9.64%` | `58.69` |
| `Live` | `Long` | `7.78` | 239,560.00 USD | 0.00 USD | 8,670.00 USD | `-9.52%` | `1,115.74` |
| `Live` | `Long` | `7.79` | 230,890.00 USD | 0.00 USD | 1,380.00 USD | `-9.41%` | `177.40` |
| `Live` | `Long` | `7.79` | 229,500.00 USD | 0.00 USD | 4,480.00 USD | `-9.29%` | `574.50` |
| `Live` | `Long` | `7.80` | 225,030.00 USD | 0.00 USD | 6,380.00 USD | `-9.17%` | `817.06` |
| `Live` | `Long` | `7.83` | 218,650.00 USD | 0.00 USD | 1,750.00 USD | `-8.94%` | `224.24` |
| `Live` | `Long` | `7.84` | 216,890.00 USD | 0.00 USD | 22,560.00 USD | `-8.71%` | `2,875.86` |
| `Live` | `Long` | `7.87` | 194,330.00 USD | 0.00 USD | 233.83 USD | `-8.48%` | `29.73` |
| `Live` | `Long` | `7.88` | 194,100.00 USD | 0.00 USD | 555.19 USD | `-8.36%` | `70.50` |
| `Live` | `Long` | `7.88` | 193,540.00 USD | 0.00 USD | 575.53 USD | `-8.24%` | `72.99` |
| `Live` | `Long` | `7.89` | 192,970.00 USD | 0.00 USD | 15,880.00 USD | `-8.13%` | `2,011.99` |
| `Live` | `Long` | `7.91` | 177,080.00 USD | 0.00 USD | 2,930.00 USD | `-8.01%` | `370.74` |
| `Live` | `Long` | `7.92` | 174,150.00 USD | 0.00 USD | 4,600.00 USD | `-7.78%` | `580.78` |
| `Live` | `Long` | `7.93` | 169,550.00 USD | 0.00 USD | 16,340.00 USD | `-7.66%` | `2,059.56` |
| `Live` | `Long` | `7.95` | 153,210.00 USD | 0.00 USD | 127,110.00 USD | `-7.55%` | `15,999.24` |
| `Live` | `Long` | `7.97` | 26,090.00 USD | 0.00 USD | 1,580.00 USD | `-7.20%` | `198.26` |
| `Live` | `Long` | `7.99` | 24,510.00 USD | 0.00 USD | 1,600.00 USD | `-7.08%` | `200.68` |
| `Live` | `Long` | `8.00` | 22,910.00 USD | 0.00 USD | 210.99 USD | `-6.96%` | `26.39` |
| `Live` | `Long` | `8.03` | 22,700.00 USD | 0.00 USD | 248.37 USD | `-6.61%` | `30.95` |
| `Live` | `Long` | `8.07` | 22,450.00 USD | 0.00 USD | 21,710.00 USD | `-6.03%` | `2,688.93` |
| `Live` | `Long` | `8.12` | 738.14 USD | 0.00 USD | 738.14 USD | `-5.57%` | `90.96` |
| `Live` | `Short` | `8.69` | 209.31 USD | 209.31 USD | 0.00 USD | `+1.07%` | `24.10` |
| `Live` | `Short` | `8.82` | 6,210.00 USD | 6,000.00 USD | 0.00 USD | `+2.70%` | `680.16` |
| `Live` | `Short` | `8.95` | 6,450.00 USD | 235.07 USD | 0.00 USD | `+4.09%` | `26.28` |
| `Live` | `Short` | `8.99` | 546,160.00 USD | 539,710.00 USD | 0.00 USD | `+4.67%` | `60,000.94` |
| `Live` | `Short` | `9.09` | 547,040.00 USD | 880.34 USD | 0.00 USD | `+5.72%` | `96.90` |
| `Live` | `Short` | `9.21` | 548,900.00 USD | 1,870.00 USD | 0.00 USD | `+7.23%` | `202.76` |
| `Live` | `Short` | `9.29` | 552,760.00 USD | 3,860.00 USD | 0.00 USD | `+8.16%` | `415.00` |
| `Live` | `Short` | `9.41` | 553,200.00 USD | 440.06 USD | 0.00 USD | `+9.56%` | `46.74` |
| `Live` | `Short` | `9.62` | 553,340.00 USD | 138.98 USD | 0.00 USD | `+12.00%` | `14.44` |
| `Live` | `Short` | `9.64` | 555,280.00 USD | 1,930.00 USD | 0.00 USD | `+12.24%` | `200.61` |
| `Live` | `Short` | `9.73` | 555,470.00 USD | 192.95 USD | 0.00 USD | `+13.28%` | `19.82` |
| `Live` | `Short` | `10.35` | 558,120.00 USD | 2,650.00 USD | 0.00 USD | `+20.38%` | `256.58` |
| `Live` | `Short` | `10.48` | 579,090.00 USD | 20,970.00 USD | 0.00 USD | `+22.01%` | `2,000.00` |
| `Live` | `Short` | `10.56` | 579,620.00 USD | 523.81 USD | 0.00 USD | `+22.94%` | `49.58` |
| `Live` | `Short` | `10.73` | 579,920.00 USD | 302.19 USD | 0.00 USD | `+24.92%` | `28.15` |
| `Live` | `Short` | `10.76` | 583,970.00 USD | 4,050.00 USD | 0.00 USD | `+25.15%` | `376.48` |
| `Live` | `Short` | `10.77` | 584,230.00 USD | 257.93 USD | 0.00 USD | `+25.27%` | `23.96` |
| `Live` | `Short` | `10.81` | 585,370.00 USD | 1,150.00 USD | 0.00 USD | `+25.85%` | `106.17` |
| `Live` | `Short` | `10.89` | 585,470.00 USD | 100.13 USD | 0.00 USD | `+26.78%` | `9.19` |
| `Live` | `Short` | `10.99` | 640,450.00 USD | 54,980.00 USD | 0.00 USD | `+27.95%` | `5,000.00` |
| `Live` | `Short` | `11.01` | 647,420.00 USD | 6,970.00 USD | 0.00 USD | `+28.06%` | `633.00` |
| `Live` | `Short` | `11.13` | 758,770.00 USD | 111,350.00 USD | 0.00 USD | `+29.58%` | `10,000.00` |
| `Live` | `Short` | `11.27` | 770,430.00 USD | 11,670.00 USD | 0.00 USD | `+31.09%` | `1,035.87` |
| `Live` | `Short` | `11.62` | 782,570.00 USD | 12,140.00 USD | 0.00 USD | `+35.28%` | `1,043.90` |
| `Live` | `Short` | `11.69` | 1,080,000.00 USD | 296,760.00 USD | 0.00 USD | `+35.98%` | `25,397.02` |
| `Live` | `Short` | `11.80` | 1,080,000.00 USD | 114.27 USD | 0.00 USD | `+37.37%` | `9.68` |
| `Live` | `Short` | `11.93` | 1,080,000.00 USD | 505.74 USD | 0.00 USD | `+38.77%` | `42.41` |
| `Live` | `Short` | `11.95` | 1,080,000.00 USD | 1,050.00 USD | 0.00 USD | `+39.00%` | `87.54` |
| `Live` | `Short` | `12.30` | 1,080,000.00 USD | 1,730.00 USD | 0.00 USD | `+43.19%` | `140.71` |
| `Live` | `Short` | `12.40` | 1,080,000.00 USD | 343.62 USD | 0.00 USD | `+44.35%` | `27.70` |
| `Live` | `Short` | `13.20` | 1,170,000.00 USD | 87,940.00 USD | 0.00 USD | `+53.55%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 1,170,000.00 USD | 3,810.00 USD | 0.00 USD | `+54.71%` | `286.56` |
| `Live` | `Short` | `13.46` | 1,180,000.00 USD | 430.34 USD | 0.00 USD | `+56.69%` | `31.96` |
| `Live` | `Short` | `13.69` | 1,180,000.00 USD | 172.29 USD | 0.00 USD | `+59.25%` | `12.59` |
| `Live` | `Short` | `13.78` | 1,240,000.00 USD | 62,750.00 USD | 0.00 USD | `+60.30%` | `4,555.14` |
| `Live` | `Short` | `14.31` | 1,240,000.00 USD | 282.43 USD | 0.00 USD | `+66.58%` | `19.73` |
| `Live` | `Short` | `14.53` | 1,240,000.00 USD | 521.30 USD | 0.00 USD | `+69.03%` | `35.89` |
| `Live` | `Short` | `14.66` | 1,240,000.00 USD | 823.29 USD | 0.00 USD | `+70.65%` | `56.14` |
| `Live` | `Short` | `14.88` | 1,240,000.00 USD | 244.10 USD | 0.00 USD | `+73.10%` | `16.41` |
| `Live` | `Short` | `15.02` | 1,240,000.00 USD | 4,170.00 USD | 0.00 USD | `+74.73%` | `277.54` |
| `Live` | `Short` | `15.10` | 1,240,000.00 USD | 325.30 USD | 0.00 USD | `+75.66%` | `21.55` |
| `Live` | `Short` | `15.29` | 1,240,000.00 USD | 229.43 USD | 0.00 USD | `+77.99%` | `15.00` |
| `Live` | `Short` | `15.35` | 1,250,000.00 USD | 230.17 USD | 0.00 USD | `+78.57%` | `15.00` |
| `Live` | `Short` | `15.38` | 1,270,000.00 USD | 20,000.00 USD | 0.00 USD | `+79.03%` | `1,300.00` |
| `Live` | `Short` | `15.72` | 1,270,000.00 USD | 167.79 USD | 0.00 USD | `+82.99%` | `10.67` |
| `Live` | `Short` | `15.77` | 1,270,000.00 USD | 185.55 USD | 0.00 USD | `+83.45%` | `11.77` |
| `Live` | `Short` | `15.82` | 1,270,000.00 USD | 1,700.00 USD | 0.00 USD | `+84.15%` | `107.48` |
| `Live` | `Short` | `16.27` | 1,290,000.00 USD | 23,750.00 USD | 0.00 USD | `+89.39%` | `1,459.25` |
| `Live` | `Short` | `16.32` | 1,310,000.00 USD | 23,090.00 USD | 0.00 USD | `+89.97%` | `1,414.55` |
| `Live` | `Short` | `16.36` | 1,580,000.00 USD | 265,080.00 USD | 0.00 USD | `+90.32%` | `16,208.00` |
| `Live` | `Short` | `16.52` | 1,580,000.00 USD | 190.91 USD | 0.00 USD | `+92.18%` | `11.56` |
| `Live` | `Short` | `16.55` | 1,580,000.00 USD | 117.71 USD | 0.00 USD | `+92.65%` | `7.11` |
| `Live` | `Short` | `16.82` | 1,660,000.00 USD | 84,760.00 USD | 0.00 USD | `+95.79%` | `5,037.66` |
| `Live` | `Short` | `16.98` | 1,670,000.00 USD | 1,690.00 USD | 0.00 USD | `+97.65%` | `99.50` |
| `Live` | `Short` | `17.00` | 1,670,000.00 USD | 1,940.00 USD | 0.00 USD | `+97.88%` | `113.93` |
| `Live` | `Short` | `17.02` | 1,670,000.00 USD | 191.87 USD | 0.00 USD | `+98.12%` | `11.27` |
| `Live` | `Short` | `17.05` | 1,670,000.00 USD | 207.78 USD | 0.00 USD | `+98.35%` | `12.19` |
| `Live` | `Short` | `17.07` | 1,670,000.00 USD | 6,740.00 USD | 0.00 USD | `+98.70%` | `395.02` |
| `Live` | `Short` | `17.14` | 1,680,000.00 USD | 1,270.00 USD | 0.00 USD | `+99.40%` | `74.09` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 385,960.00 USD | 0.00 USD | 611.73 USD | `-72.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 385,350.00 USD | 0.00 USD | 793.75 USD | `-53.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 384,550.00 USD | 0.00 USD | 67,970.00 USD | `-41.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 316,580.00 USD | 0.00 USD | 205.30 USD | `-38.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 316,380.00 USD | 0.00 USD | 465.42 USD | `-36.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 315,910.00 USD | 0.00 USD | 349.35 USD | `-35.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.54` | 315,560.00 USD | 0.00 USD | 1,020.00 USD | `-35.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 314,550.00 USD | 0.00 USD | 1,330.00 USD | `-32.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 313,220.00 USD | 0.00 USD | 493.50 USD | `-30.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 312,730.00 USD | 0.00 USD | 100.98 USD | `-30.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 312,630.00 USD | 0.00 USD | 500.70 USD | `-30.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 312,120.00 USD | 0.00 USD | 4,160.00 USD | `-28.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 307,970.00 USD | 0.00 USD | 6,500.00 USD | `-28.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.21` | 301,470.00 USD | 0.00 USD | 906.18 USD | `-27.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.25` | 300,560.00 USD | 0.00 USD | 127.35 USD | `-27.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 300,430.00 USD | 0.00 USD | 864.38 USD | `-26.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 299,570.00 USD | 0.00 USD | 130.10 USD | `-24.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 299,440.00 USD | 0.00 USD | 4,340.00 USD | `-23.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 295,100.00 USD | 0.00 USD | 5,520.00 USD | `-21.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 289,580.00 USD | 0.00 USD | 100.72 USD | `-21.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 289,480.00 USD | 0.00 USD | 296.34 USD | `-21.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 289,180.00 USD | 0.00 USD | 921.19 USD | `-21.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 288,260.00 USD | 0.00 USD | 709.98 USD | `-19.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.91` | 287,550.00 USD | 0.00 USD | 4,630.00 USD | `-19.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.92` | 282,920.00 USD | 0.00 USD | 691.50 USD | `-19.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 282,230.00 USD | 0.00 USD | 262.44 USD | `-18.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 281,970.00 USD | 0.00 USD | 24,350.00 USD | `-18.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.11` | 257,620.00 USD | 0.00 USD | 187.79 USD | `-17.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 257,430.00 USD | 0.00 USD | 6,790.00 USD | `-16.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 250,640.00 USD | 0.00 USD | 4,960.00 USD | `-16.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.21` | 245,680.00 USD | 0.00 USD | 7,210.00 USD | `-16.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 238,470.00 USD | 0.00 USD | 282.74 USD | `-15.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 238,190.00 USD | 0.00 USD | 603.44 USD | `-15.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 237,590.00 USD | 0.00 USD | 464.61 USD | `-15.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 237,120.00 USD | 0.00 USD | 2,090.00 USD | `-14.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 235,030.00 USD | 0.00 USD | 129.58 USD | `-14.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 234,900.00 USD | 0.00 USD | 114.65 USD | `-14.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.39` | 234,780.00 USD | 0.00 USD | 702.75 USD | `-13.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.41` | 234,080.00 USD | 0.00 USD | 4,630.00 USD | `-13.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 229,450.00 USD | 0.00 USD | 199.39 USD | `-13.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 229,250.00 USD | 0.00 USD | 6,270.00 USD | `-13.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 222,980.00 USD | 0.00 USD | 37,420.00 USD | `-12.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 185,560.00 USD | 0.00 USD | 2,120.00 USD | `-12.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 183,440.00 USD | 0.00 USD | 799.83 USD | `-12.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.54` | 182,640.00 USD | 0.00 USD | 820.44 USD | `-12.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 181,820.00 USD | 0.00 USD | 218.24 USD | `-11.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 181,600.00 USD | 0.00 USD | 113.78 USD | `-11.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.61` | 181,490.00 USD | 0.00 USD | 152.10 USD | `-11.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.62` | 181,330.00 USD | 0.00 USD | 297.59 USD | `-11.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.68` | 181,040.00 USD | 0.00 USD | 528.88 USD | `-10.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 180,510.00 USD | 0.00 USD | 360.13 USD | `-10.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 180,150.00 USD | 0.00 USD | 578.04 USD | `-9.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.79` | 179,570.00 USD | 0.00 USD | 424.05 USD | `-9.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 179,140.00 USD | 0.00 USD | 22,630.00 USD | `-9.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.82` | 156,510.00 USD | 0.00 USD | 3,940.00 USD | `-9.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 152,570.00 USD | 0.00 USD | 115.23 USD | `-8.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 152,460.00 USD | 0.00 USD | 183.33 USD | `-8.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 152,270.00 USD | 0.00 USD | 1,890.00 USD | `-8.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 150,380.00 USD | 0.00 USD | 6,840.00 USD | `-8.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 143,540.00 USD | 0.00 USD | 5,710.00 USD | `-7.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 137,830.00 USD | 0.00 USD | 1,590.00 USD | `-7.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 136,250.00 USD | 0.00 USD | 898.42 USD | `-7.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 135,350.00 USD | 0.00 USD | 7,960.00 USD | `-7.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 127,390.00 USD | 0.00 USD | 246.52 USD | `-7.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.99` | 127,150.00 USD | 0.00 USD | 1,440.00 USD | `-7.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 125,710.00 USD | 0.00 USD | 3,430.00 USD | `-6.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 122,280.00 USD | 0.00 USD | 123.58 USD | `-6.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 122,150.00 USD | 0.00 USD | 796.62 USD | `-6.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 121,360.00 USD | 0.00 USD | 152.56 USD | `-6.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.06` | 121,200.00 USD | 0.00 USD | 2,730.00 USD | `-6.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 118,470.00 USD | 0.00 USD | 121.69 USD | `-6.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.09` | 118,350.00 USD | 0.00 USD | 5,230.00 USD | `-5.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 113,120.00 USD | 0.00 USD | 477.36 USD | `-5.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 112,640.00 USD | 0.00 USD | 924.78 USD | `-5.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 111,720.00 USD | 0.00 USD | 744.88 USD | `-5.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 110,970.00 USD | 0.00 USD | 6,500.00 USD | `-5.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 104,470.00 USD | 0.00 USD | 884.60 USD | `-5.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 103,590.00 USD | 0.00 USD | 5,550.00 USD | `-5.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 98,030.00 USD | 0.00 USD | 1,430.00 USD | `-5.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 96,600.00 USD | 0.00 USD | 3,080.00 USD | `-4.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 93,520.00 USD | 0.00 USD | 520.75 USD | `-4.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 93,000.00 USD | 0.00 USD | 3,020.00 USD | `-4.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 89,970.00 USD | 0.00 USD | 141.04 USD | `-4.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 89,830.00 USD | 0.00 USD | 27,870.00 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 61,960.00 USD | 0.00 USD | 515.66 USD | `-4.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.22` | 61,440.00 USD | 0.00 USD | 139.74 USD | `-4.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 61,300.00 USD | 0.00 USD | 490.15 USD | `-4.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.24` | 60,810.00 USD | 0.00 USD | 197.96 USD | `-4.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.26` | 60,610.00 USD | 0.00 USD | 9,110.00 USD | `-3.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.27` | 51,500.00 USD | 0.00 USD | 535.65 USD | `-3.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 50,960.00 USD | 0.00 USD | 734.99 USD | `-3.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 50,230.00 USD | 0.00 USD | 1,530.00 USD | `-3.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 48,690.00 USD | 0.00 USD | 4,150.00 USD | `-3.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 44,550.00 USD | 0.00 USD | 4,190.00 USD | `-3.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 40,360.00 USD | 0.00 USD | 2,920.00 USD | `-3.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.32` | 37,440.00 USD | 0.00 USD | 1,690.00 USD | `-3.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 35,750.00 USD | 0.00 USD | 408.58 USD | `-3.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 35,340.00 USD | 0.00 USD | 808.63 USD | `-2.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 34,540.00 USD | 0.00 USD | 970.35 USD | `-2.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 33,570.00 USD | 0.00 USD | 503.59 USD | `-2.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 33,060.00 USD | 0.00 USD | 419.25 USD | `-2.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 32,640.00 USD | 0.00 USD | 1,970.00 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 30,670.00 USD | 0.00 USD | 201.80 USD | `-2.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 30,470.00 USD | 0.00 USD | 314.81 USD | `-2.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 30,160.00 USD | 0.00 USD | 1,880.00 USD | `-1.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 28,270.00 USD | 0.00 USD | 307.54 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 27,970.00 USD | 0.00 USD | 138.24 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 27,830.00 USD | 0.00 USD | 710.81 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.47` | 27,120.00 USD | 0.00 USD | 769.61 USD | `-1.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.48` | 26,350.00 USD | 0.00 USD | 146.79 USD | `-1.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.49` | 26,200.00 USD | 0.00 USD | 408.78 USD | `-1.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.51` | 25,790.00 USD | 0.00 USD | 17,010.00 USD | `-1.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.52` | 8,780.00 USD | 0.00 USD | 408.55 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.53` | 8,370.00 USD | 0.00 USD | 1,130.00 USD | `-0.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.54` | 7,250.00 USD | 0.00 USD | 290.10 USD | `-0.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.54` | 6,960.00 USD | 0.00 USD | 4,400.00 USD | `-0.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 2,550.00 USD | 0.00 USD | 243.82 USD | `-0.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.56` | 2,310.00 USD | 0.00 USD | 1,600.00 USD | `-0.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.57` | 709.83 USD | 0.00 USD | 566.55 USD | `-0.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.59` | 143.28 USD | 0.00 USD | 143.28 USD | `-0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.60` | 1,130.00 USD | 1,130.00 USD | 0.00 USD | `+0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 1,880.00 USD | 751.56 USD | 0.00 USD | `+0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 3,370.00 USD | 1,490.00 USD | 0.00 USD | `+0.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 3,480.00 USD | 107.47 USD | 0.00 USD | `+0.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.63` | 3,680.00 USD | 201.97 USD | 0.00 USD | `+0.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.64` | 3,790.00 USD | 103.31 USD | 0.00 USD | `+0.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 3,890.00 USD | 107.84 USD | 0.00 USD | `+0.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 4,000.00 USD | 107.97 USD | 0.00 USD | `+0.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.68` | 4,180.00 USD | 176.62 USD | 0.00 USD | `+0.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.69` | 5,170.00 USD | 990.09 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.70` | 10,180.00 USD | 5,010.00 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 10,760.00 USD | 575.14 USD | 0.00 USD | `+1.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 11,160.00 USD | 399.67 USD | 0.00 USD | `+1.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.72` | 11,970.00 USD | 819.28 USD | 0.00 USD | `+1.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.73` | 12,310.00 USD | 333.07 USD | 0.00 USD | `+1.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.74` | 16,680.00 USD | 4,370.00 USD | 0.00 USD | `+1.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.76` | 18,460.00 USD | 1,780.00 USD | 0.00 USD | `+1.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 58,270.00 USD | 39,810.00 USD | 0.00 USD | `+2.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.78` | 58,480.00 USD | 215.16 USD | 0.00 USD | `+2.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 58,870.00 USD | 388.12 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 59,580.00 USD | 711.78 USD | 0.00 USD | `+2.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 79,390.00 USD | 19,810.00 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.82` | 81,420.00 USD | 2,030.00 USD | 0.00 USD | `+2.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.84` | 81,660.00 USD | 243.40 USD | 0.00 USD | `+2.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 81,830.00 USD | 168.05 USD | 0.00 USD | `+2.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 82,170.00 USD | 339.94 USD | 0.00 USD | `+3.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 82,330.00 USD | 163.91 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 82,440.00 USD | 110.58 USD | 0.00 USD | `+3.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 83,300.00 USD | 860.96 USD | 0.00 USD | `+3.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 85,240.00 USD | 1,930.00 USD | 0.00 USD | `+3.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 86,030.00 USD | 788.72 USD | 0.00 USD | `+3.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 87,830.00 USD | 1,800.00 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 87,990.00 USD | 163.33 USD | 0.00 USD | `+3.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 117,520.00 USD | 29,520.00 USD | 0.00 USD | `+3.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 117,740.00 USD | 223.62 USD | 0.00 USD | `+4.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 655,050.00 USD | 537,310.00 USD | 0.00 USD | `+4.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 655,450.00 USD | 401.63 USD | 0.00 USD | `+4.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 970,600.00 USD | 315,150.00 USD | 0.00 USD | `+4.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 970,860.00 USD | 262.56 USD | 0.00 USD | `+4.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 970,990.00 USD | 130.03 USD | 0.00 USD | `+4.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 972,370.00 USD | 1,380.00 USD | 0.00 USD | `+4.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 973,460.00 USD | 1,090.00 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 974,080.00 USD | 616.37 USD | 0.00 USD | `+5.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 974,180.00 USD | 102.03 USD | 0.00 USD | `+5.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 974,630.00 USD | 453.84 USD | 0.00 USD | `+5.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 974,790.00 USD | 160.99 USD | 0.00 USD | `+5.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 975,010.00 USD | 215.98 USD | 0.00 USD | `+5.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 976,520.00 USD | 1,510.00 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 977,120.00 USD | 606.18 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 1,430,000.00 USD | 455,260.00 USD | 0.00 USD | `+5.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 1,430,000.00 USD | 1,290.00 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 1,430,000.00 USD | 166.53 USD | 0.00 USD | `+6.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 1,440,000.00 USD | 2,000.00 USD | 0.00 USD | `+6.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 1,830,000.00 USD | 394,210.00 USD | 0.00 USD | `+6.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,830,000.00 USD | 119.24 USD | 0.00 USD | `+6.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,830,000.00 USD | 3,020.00 USD | 0.00 USD | `+7.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,830,000.00 USD | 131.87 USD | 0.00 USD | `+7.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,830,000.00 USD | 149.17 USD | 0.00 USD | `+7.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,840,000.00 USD | 2,220.00 USD | 0.00 USD | `+7.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 2,070,000.00 USD | 231,380.00 USD | 0.00 USD | `+7.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 2,070,000.00 USD | 1,960.00 USD | 0.00 USD | `+7.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 2,070,000.00 USD | 434.45 USD | 0.00 USD | `+8.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 2,090,000.00 USD | 18,610.00 USD | 0.00 USD | `+8.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 2,090,000.00 USD | 166.83 USD | 0.00 USD | `+8.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 2,090,000.00 USD | 674.29 USD | 0.00 USD | `+8.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 2,090,000.00 USD | 101.58 USD | 0.00 USD | `+8.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 2,090,000.00 USD | 109.36 USD | 0.00 USD | `+8.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 2,090,000.00 USD | 116.69 USD | 0.00 USD | `+8.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 2,090,000.00 USD | 163.41 USD | 0.00 USD | `+9.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 2,090,000.00 USD | 102.01 USD | 0.00 USD | `+9.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 2,090,000.00 USD | 660.84 USD | 0.00 USD | `+9.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 2,090,000.00 USD | 714.59 USD | 0.00 USD | `+9.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 2,090,000.00 USD | 928.13 USD | 0.00 USD | `+9.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 2,090,000.00 USD | 102.45 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 2,090,000.00 USD | 219.84 USD | 0.00 USD | `+9.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 2,090,000.00 USD | 1,890.00 USD | 0.00 USD | `+10.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 2,100,000.00 USD | 1,130.00 USD | 0.00 USD | `+10.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 2,100,000.00 USD | 288.46 USD | 0.00 USD | `+10.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 2,100,000.00 USD | 119.92 USD | 0.00 USD | `+10.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 2,100,000.00 USD | 231.00 USD | 0.00 USD | `+11.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 2,100,000.00 USD | 221.07 USD | 0.00 USD | `+11.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 2,100,000.00 USD | 992.00 USD | 0.00 USD | `+11.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 2,100,000.00 USD | 148.48 USD | 0.00 USD | `+12.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 2,100,000.00 USD | 191.36 USD | 0.00 USD | `+12.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 2,100,000.00 USD | 4,440.00 USD | 0.00 USD | `+12.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 2,100,000.00 USD | 108.21 USD | 0.00 USD | `+12.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 2,100,000.00 USD | 169.68 USD | 0.00 USD | `+13.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.74` | 2,100,000.00 USD | 574.66 USD | 0.00 USD | `+13.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 2,100,000.00 USD | 121.87 USD | 0.00 USD | `+13.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 2,100,000.00 USD | 115.88 USD | 0.00 USD | `+14.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 2,100,000.00 USD | 340.05 USD | 0.00 USD | `+14.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 2,100,000.00 USD | 742.12 USD | 0.00 USD | `+15.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 2,100,000.00 USD | 899.47 USD | 0.00 USD | `+15.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 2,170,000.00 USD | 70,020.00 USD | 0.00 USD | `+15.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 2,180,000.00 USD | 373.97 USD | 0.00 USD | `+15.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 2,180,000.00 USD | 5,050.00 USD | 0.00 USD | `+16.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 2,190,000.00 USD | 6,370.00 USD | 0.00 USD | `+17.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 2,190,000.00 USD | 404.20 USD | 0.00 USD | `+17.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 2,400,000.00 USD | 210,980.00 USD | 0.00 USD | `+17.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 2,400,000.00 USD | 1,150.00 USD | 0.00 USD | `+17.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 2,400,000.00 USD | 172.16 USD | 0.00 USD | `+18.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 2,400,000.00 USD | 922.87 USD | 0.00 USD | `+19.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 2,400,000.00 USD | 489.40 USD | 0.00 USD | `+20.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 2,400,000.00 USD | 1,200.00 USD | 0.00 USD | `+20.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 2,400,000.00 USD | 118.01 USD | 0.00 USD | `+21.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.47` | 2,400,000.00 USD | 818.31 USD | 0.00 USD | `+21.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 2,400,000.00 USD | 312.31 USD | 0.00 USD | `+22.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 2,410,000.00 USD | 2,290.00 USD | 0.00 USD | `+22.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.53` | 2,410,000.00 USD | 1,890.00 USD | 0.00 USD | `+22.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 2,410,000.00 USD | 178.46 USD | 0.00 USD | `+23.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 2,410,000.00 USD | 173.42 USD | 0.00 USD | `+24.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 2,410,000.00 USD | 184.75 USD | 0.00 USD | `+24.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 2,410,000.00 USD | 135.78 USD | 0.00 USD | `+25.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 2,410,000.00 USD | 127.96 USD | 0.00 USD | `+26.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 2,410,000.00 USD | 476.43 USD | 0.00 USD | `+26.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 2,410,000.00 USD | 869.35 USD | 0.00 USD | `+26.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 2,410,000.00 USD | 118.97 USD | 0.00 USD | `+27.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 2,410,000.00 USD | 251.06 USD | 0.00 USD | `+27.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 2,410,000.00 USD | 552.44 USD | 0.00 USD | `+27.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 2,410,000.00 USD | 537.26 USD | 0.00 USD | `+28.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 2,410,000.00 USD | 320.29 USD | 0.00 USD | `+29.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 2,410,000.00 USD | 1,100.00 USD | 0.00 USD | `+30.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 2,410,000.00 USD | 2,270.00 USD | 0.00 USD | `+30.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 2,420,000.00 USD | 1,270.00 USD | 0.00 USD | `+30.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 2,420,000.00 USD | 1,380.00 USD | 0.00 USD | `+32.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 2,420,000.00 USD | 2,410.00 USD | 0.00 USD | `+32.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 2,430,000.00 USD | 9,520.00 USD | 0.00 USD | `+33.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.48` | 2,430,000.00 USD | 2,050.00 USD | 0.00 USD | `+33.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 2,430,000.00 USD | 529.11 USD | 0.00 USD | `+33.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 2,440,000.00 USD | 7,700.00 USD | 0.00 USD | `+34.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 2,440,000.00 USD | 906.03 USD | 0.00 USD | `+37.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 2,440,000.00 USD | 434.61 USD | 0.00 USD | `+38.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 2,440,000.00 USD | 163.52 USD | 0.00 USD | `+38.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 2,450,000.00 USD | 10,370.00 USD | 0.00 USD | `+39.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.19` | 2,460,000.00 USD | 5,270.00 USD | 0.00 USD | `+41.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.28` | 2,460,000.00 USD | 115.02 USD | 0.00 USD | `+42.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 2,460,000.00 USD | 3,870.00 USD | 0.00 USD | `+47.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 2,460,000.00 USD | 197.97 USD | 0.00 USD | `+49.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 2,460,000.00 USD | 3,200.00 USD | 0.00 USD | `+50.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 2,460,000.00 USD | 179.58 USD | 0.00 USD | `+51.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 2,460,000.00 USD | 568.45 USD | 0.00 USD | `+51.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 2,470,000.00 USD | 169.57 USD | 0.00 USD | `+52.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 2,470,000.00 USD | 446.52 USD | 0.00 USD | `+55.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 2,470,000.00 USD | 5,320.00 USD | 0.00 USD | `+56.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,680,000.00 USD | 210,750.00 USD | 0.00 USD | `+57.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,680,000.00 USD | 407.95 USD | 0.00 USD | `+59.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,680,000.00 USD | 174.91 USD | 0.00 USD | `+60.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,690,000.00 USD | 4,680.00 USD | 0.00 USD | `+62.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,690,000.00 USD | 960.26 USD | 0.00 USD | `+65.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,690,000.00 USD | 2,710.00 USD | 0.00 USD | `+67.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,690,000.00 USD | 805.90 USD | 0.00 USD | `+68.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,690,000.00 USD | 655.55 USD | 0.00 USD | `+71.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,700,000.00 USD | 4,890.00 USD | 0.00 USD | `+72.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,700,000.00 USD | 471.09 USD | 0.00 USD | `+73.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,700,000.00 USD | 383.85 USD | 0.00 USD | `+74.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 3,350,000.00 USD | 654,840.00 USD | 0.00 USD | `+74.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.06` | 3,350,000.00 USD | 1,510.00 USD | 0.00 USD | `+75.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 3,350,000.00 USD | 111.87 USD | 0.00 USD | `+84.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 3,350,000.00 USD | 219.91 USD | 0.00 USD | `+86.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 3,350,000.00 USD | 121.74 USD | 0.00 USD | `+97.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.00` | 3,350,000.00 USD | 297.59 USD | 0.00 USD | `+97.88%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.14` | 7,640,000.00 USD | 0.00 USD | 7,640,000.00 USD | 45,840.00 USD | 22,970.00 USD | 41,610.00 USD |
| `7D` | `7.16` | 7,530,000.00 USD | 0.00 USD | 7,530,000.00 USD | 29,500.00 USD | 4,260.00 USD | 21,980.00 USD |
| `7D` | `7.18` | 7,470,000.00 USD | 0.00 USD | 7,470,000.00 USD | 5,030.00 USD | 3,780.00 USD | 19,650.00 USD |
| `7D` | `7.20` | 7,440,000.00 USD | 0.00 USD | 7,440,000.00 USD | 11,960.00 USD | 7,300.00 USD | 2,050.00 USD |
| `7D` | `7.22` | 7,420,000.00 USD | 0.00 USD | 7,420,000.00 USD | 12,640.00 USD | 6,540.00 USD | 6,980.00 USD |
| `7D` | `7.24` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 39,910.00 USD | 0.00 USD | 14,820.00 USD |
| `7D` | `7.26` | 7,340,000.00 USD | 0.00 USD | 7,340,000.00 USD | 420.05 USD | 1,810.00 USD | 8,050.00 USD |
| `7D` | `7.28` | 7,330,000.00 USD | 0.00 USD | 7,330,000.00 USD | 7,520.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.30` | 7,320,000.00 USD | 0.00 USD | 7,320,000.00 USD | 252.80 USD | 0.00 USD | 4,770.00 USD |
| `7D` | `7.32` | 7,320,000.00 USD | 0.00 USD | 7,320,000.00 USD | 0.00 USD | 0.00 USD | 8,620.00 USD |
| `7D` | `7.34` | 7,310,000.00 USD | 0.00 USD | 7,310,000.00 USD | 7,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.36` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 983.83 USD | 0.00 USD | 864.67 USD |
| `7D` | `7.38` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 46,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.40` | 7,250,000.00 USD | 0.00 USD | 7,250,000.00 USD | 44,790.00 USD | 0.00 USD | 503.12 USD |
| `7D` | `7.46` | 7,210,000.00 USD | 0.00 USD | 7,210,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD |
| `7D` | `7.48` | 7,180,000.00 USD | 0.00 USD | 7,180,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD |
| `7D` | `7.52` | 7,160,000.00 USD | 0.00 USD | 7,160,000.00 USD | 3,220.00 USD | 14,470.00 USD | 18,280.00 USD |
| `7D` | `7.54` | 7,130,000.00 USD | 0.00 USD | 7,130,000.00 USD | 34,840.00 USD | 4,450.00 USD | 0.00 USD |
| `1D` | `7.55` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 8,130.00 USD | 4,270.00 USD | 136.40 USD |
| `1D` | `7.56` | 6,440,000.00 USD | 0.00 USD | 6,440,000.00 USD | 14,910.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `7.56` | 7,090,000.00 USD | 0.00 USD | 7,090,000.00 USD | 20,150.00 USD | 4,310.00 USD | 0.00 USD |
| `1D` | `7.57` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 342.65 USD | 0.00 USD | 101.23 USD |
| `1D` | `7.58` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 0.00 USD | 0.00 USD | 3,490.00 USD |
| `1D` | `7.59` | 6,410,000.00 USD | 0.00 USD | 6,410,000.00 USD | 1,390.00 USD | 0.00 USD | 4,070.00 USD |
| `1D` | `7.60` | 6,410,000.00 USD | 0.00 USD | 6,410,000.00 USD | 629.05 USD | 4,900.00 USD | 351.13 USD |
| `7D` | `7.60` | 7,060,000.00 USD | 0.00 USD | 7,060,000.00 USD | 0.00 USD | 0.00 USD | 301.55 USD |
| `1D` | `7.61` | 6,400,000.00 USD | 0.00 USD | 6,400,000.00 USD | 1,190.00 USD | 761.26 USD | 11,670.00 USD |
| `1D` | `7.62` | 6,390,000.00 USD | 0.00 USD | 6,390,000.00 USD | 916.10 USD | 0.00 USD | 133.28 USD |
| `7D` | `7.62` | 7,060,000.00 USD | 0.00 USD | 7,060,000.00 USD | 0.00 USD | 0.00 USD | 996.08 USD |
| `1D` | `7.63` | 6,390,000.00 USD | 0.00 USD | 6,390,000.00 USD | 986.95 USD | 0.00 USD | 8,000.00 USD |
| `1D` | `7.64` | 6,380,000.00 USD | 0.00 USD | 6,380,000.00 USD | 33,010.00 USD | 812.96 USD | 158.22 USD |
| `7D` | `7.64` | 7,060,000.00 USD | 0.00 USD | 7,060,000.00 USD | 41,300.00 USD | 0.00 USD | 686.63 USD |
| `1D` | `7.65` | 6,340,000.00 USD | 0.00 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 9,870.00 USD |
| `1D` | `7.66` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 3,030.00 USD | 0.00 USD | 531.95 USD |
| `7D` | `7.66` | 7,020,000.00 USD | 0.00 USD | 7,020,000.00 USD | 4,870.00 USD | 0.00 USD | 24,600.00 USD |
| `1D` | `7.67` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 1,140.00 USD | 0.00 USD | 114.38 USD |
| `1D` | `7.68` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 892.30 USD | 0.00 USD | 3,830.00 USD |
| `7D` | `7.68` | 6,990,000.00 USD | 0.00 USD | 6,990,000.00 USD | 0.00 USD | 0.00 USD | 9,540.00 USD |
| `1D` | `7.70` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 551.10 USD | 2,390.00 USD | 16,770.00 USD |
| `1D` | `7.71` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 660.12 USD | 5,040.00 USD | 7,390.00 USD |
| `1D` | `7.72` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 701.68 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.72` | 6,980,000.00 USD | 0.00 USD | 6,980,000.00 USD | 38,970.00 USD | 0.00 USD | 40,180.00 USD |
| `1D` | `7.73` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 4,120.00 USD | 0.00 USD | 5,600.00 USD |
| `1D` | `7.74` | 6,280,000.00 USD | 0.00 USD | 6,280,000.00 USD | 9,310.00 USD | 0.00 USD | 184.39 USD |
| `7D` | `7.74` | 6,900,000.00 USD | 0.00 USD | 6,900,000.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.75` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 775.36 USD | 5,560.00 USD | 8,050.00 USD |
| `1D` | `7.76` | 6,260,000.00 USD | 0.00 USD | 6,260,000.00 USD | 188.00 USD | 0.00 USD | 2,040.00 USD |
| `7D` | `7.76` | 6,900,000.00 USD | 0.00 USD | 6,900,000.00 USD | 812.95 USD | 13,360.00 USD | 11,180.00 USD |
| `1D` | `7.77` | 6,260,000.00 USD | 0.00 USD | 6,260,000.00 USD | 23,890.00 USD | 572.85 USD | 5,870.00 USD |
| `1D` | `7.78` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 7,400.00 USD | 7,180.00 USD | 0.00 USD |
| `7D` | `7.78` | 6,870,000.00 USD | 0.00 USD | 6,870,000.00 USD | 46,570.00 USD | 4,900.00 USD | 21,060.00 USD |
| `1D` | `7.79` | 6,210,000.00 USD | 0.00 USD | 6,210,000.00 USD | 8,050.00 USD | 2,910.00 USD | 589.02 USD |
| `1D` | `7.80` | 6,200,000.00 USD | 0.00 USD | 6,200,000.00 USD | 9,300.00 USD | 9,380.00 USD | 3,630.00 USD |
| `7D` | `7.80` | 6,800,000.00 USD | 0.00 USD | 6,800,000.00 USD | 17,590.00 USD | 12,980.00 USD | 1,770.00 USD |
| `1D` | `7.81` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 809.15 USD | 728.43 USD | 0.00 USD |
| `1D` | `7.82` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 4,270.00 USD | 2,970.00 USD | 2,500.00 USD |
| `7D` | `7.82` | 6,770,000.00 USD | 0.00 USD | 6,770,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,710.00 USD |
| `1D` | `7.83` | 6,170,000.00 USD | 0.00 USD | 6,170,000.00 USD | 27,230.00 USD | 6,330.00 USD | 1,350.00 USD |
| `1D` | `7.84` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 1,060.00 USD | 1,800.00 USD | 10.76 USD |
| `7D` | `7.84` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 32,340.00 USD | 2,380.00 USD | 25,450.00 USD |
| `1D` | `7.85` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 5,210.00 USD | 1,250.00 USD | 2,650.00 USD |
| `1D` | `7.86` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 5,060.00 USD | 6,690.00 USD | 18,710.00 USD |
| `7D` | `7.86` | 6,700,000.00 USD | 0.00 USD | 6,700,000.00 USD | 137,360.00 USD | 5,460.00 USD | 18,470.00 USD |
| `1D` | `7.87` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 13,690.00 USD | 10,860.00 USD | 24,540.00 USD |
| `1D` | `7.88` | 6,040,000.00 USD | 0.00 USD | 6,040,000.00 USD | 161,620.00 USD | 5,890.00 USD | 34,820.00 USD |
| `7D` | `7.88` | 6,540,000.00 USD | 0.00 USD | 6,540,000.00 USD | 170,100.00 USD | 12,780.00 USD | 30,610.00 USD |
| `1D` | `7.89` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 59,740.00 USD | 3,720.00 USD | 27,230.00 USD |
| `1D` | `7.90` | 5,750,000.00 USD | 0.00 USD | 5,750,000.00 USD | 56,040.00 USD | 6,970.00 USD | 5,960.00 USD |
| `7D` | `7.90` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 33,680.00 USD | 12,890.00 USD | 18,230.00 USD |
| `1D` | `7.91` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 14,100.00 USD | 10,370.00 USD | 28,300.00 USD |
| `1D` | `7.92` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 15,980.00 USD | 2,950.00 USD | 8,760.00 USD |
| `7D` | `7.92` | 6,260,000.00 USD | 0.00 USD | 6,260,000.00 USD | 55,490.00 USD | 23,630.00 USD | 41,800.00 USD |
| `1D` | `7.93` | 5,600,000.00 USD | 0.00 USD | 5,600,000.00 USD | 7,960.00 USD | 6,570.00 USD | 4,480.00 USD |
| `1D` | `7.94` | 5,580,000.00 USD | 0.00 USD | 5,580,000.00 USD | 17,720.00 USD | 20,510.00 USD | 61,750.00 USD |
| `7D` | `7.94` | 6,140,000.00 USD | 0.00 USD | 6,140,000.00 USD | 51,390.00 USD | 9,960.00 USD | 31,670.00 USD |
| `1D` | `7.95` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 27,800.00 USD | 9,190.00 USD | 86,980.00 USD |
| `1D` | `7.96` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 2,970.00 USD | 15,680.00 USD | 62,330.00 USD |
| `7D` | `7.96` | 6,040,000.00 USD | 0.00 USD | 6,040,000.00 USD | 21,840.00 USD | 6,920.00 USD | 87,430.00 USD |
| `1D` | `7.97` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 12,860.00 USD | 9,820.00 USD | 4,040.00 USD |
| `1D` | `7.98` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 5,050.00 USD | 2,060.00 USD | 42,970.00 USD |
| `7D` | `7.98` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 58,520.00 USD | 26,790.00 USD | 146,450.00 USD |
| `1D` | `7.99` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 3,230.00 USD | 10,180.00 USD | 4,660.00 USD |
| `1D` | `8.00` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 50,430.00 USD | 8,950.00 USD | 21,810.00 USD |
| `7D` | `8.00` | 5,700,000.00 USD | 0.00 USD | 5,700,000.00 USD | 60,980.00 USD | 16,420.00 USD | 5,130.00 USD |
| `1D` | `8.01` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 6,540.00 USD | 3,750.00 USD | 3,970.00 USD |
| `1D` | `8.02` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 75,000.00 USD | 0.00 USD | 274.70 USD |
| `7D` | `8.02` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 15,300.00 USD | 46,670.00 USD | 57,670.00 USD |
| `1D` | `8.03` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 8,820.00 USD | 12,540.00 USD | 12,890.00 USD |
| `1D` | `8.04` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 49,080.00 USD | 0.00 USD | 10,010.00 USD |
| `7D` | `8.04` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 460,090.00 USD | 0.00 USD | 86,550.00 USD |
| `1D` | `8.05` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 317,540.00 USD | 6,430.00 USD | 53,800.00 USD |
| `1D` | `8.06` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 155,240.00 USD | 0.00 USD | 66,970.00 USD |
| `7D` | `8.06` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 336,530.00 USD | 0.00 USD | 86,670.00 USD |
| `1D` | `8.07` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 130,100.00 USD | 9,310.00 USD | 4,540.00 USD |
| `1D` | `8.08` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 14,440.00 USD | 0.00 USD | 65,310.00 USD |
| `7D` | `8.08` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 5,100.00 USD | 0.00 USD | 73,960.00 USD |
| `1D` | `8.09` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 3,110.00 USD | 0.00 USD | 29,580.00 USD |
| `1D` | `8.10` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 31,390.00 USD | 6,770.00 USD | 122,420.00 USD |
| `7D` | `8.10` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 56,590.00 USD | 0.00 USD | 14,820.00 USD |
| `1D` | `8.11` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 77,850.00 USD | 0.00 USD | 192,180.00 USD |
| `1D` | `8.12` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 7,380.00 USD | 10,020.00 USD | 126,250.00 USD |
| `7D` | `8.12` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 22,060.00 USD | 0.00 USD | 141,990.00 USD |
| `1D` | `8.13` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 0.00 USD | 4,510.00 USD | 0.00 USD |
| `1D` | `8.14` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 0.00 USD | 4,120.00 USD | 96,680.00 USD |
| `7D` | `8.14` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 160,410.00 USD | 25,370.00 USD | 191,670.00 USD |
| `1D` | `8.15` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 40,400.00 USD | 11,230.00 USD | 46,550.00 USD |
| `1D` | `8.16` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 192.50 USD | 17,890.00 USD | 165,460.00 USD |
| `7D` | `8.16` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 30,670.00 USD | 17,750.00 USD | 29,720.00 USD |
| `1D` | `8.17` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 11,100.00 USD | 8,610.00 USD | 183,140.00 USD |
| `1D` | `8.18` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 6,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.18` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 0.00 USD | 43,260.00 USD | 172,780.00 USD |
| `1D` | `8.19` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 17,640.00 USD | 0.00 USD | 15,460.00 USD |
| `1D` | `8.20` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 25,530.00 USD | 0.00 USD | 11,410.00 USD |
| `7D` | `8.20` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 174,220.00 USD | 58,100.00 USD | 5,890.00 USD |
| `1D` | `8.21` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 33,010.00 USD | 1,260.00 USD | 0.00 USD |
| `1D` | `8.22` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 16,310.00 USD |
| `7D` | `8.22` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 0.00 USD | 21,570.00 USD | 0.00 USD |
| `1D` | `8.23` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 0.00 USD | 1,750.00 USD | 35.82 USD |
| `1D` | `8.24` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 277.44 USD | 1,020.00 USD | 0.98 USD |
| `7D` | `8.24` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 107,610.00 USD | 18,690.00 USD | 17,610.00 USD |
| `1D` | `8.25` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 38,170.00 USD |
| `1D` | `8.26` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 32,580.00 USD | 12,510.00 USD | 23,300.00 USD |
| `7D` | `8.26` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 30,070.00 USD | 5,750.00 USD | 0.00 USD |
| `1D` | `8.27` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 13,860.00 USD | 9,880.00 USD | 20,140.00 USD |
| `1D` | `8.28` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 0.00 USD | 9,050.00 USD | 0.50 USD |
| `7D` | `8.28` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 101,560.00 USD | 4,000.00 USD | 27,800.00 USD |
| `1D` | `8.29` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 14,380.00 USD | 8,320.00 USD | 0.00 USD |
| `1D` | `8.30` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 0.00 USD | 4,480.00 USD | 0.00 USD |
| `7D` | `8.30` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 152,370.00 USD | 0.00 USD | 1,650.00 USD |
| `1D` | `8.31` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 39,240.00 USD |
| `1D` | `8.32` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 66,820.00 USD | 4,060.00 USD | 16.44 USD |
| `7D` | `8.32` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 220,640.00 USD | 0.00 USD | 5,060.00 USD |
| `1D` | `8.33` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 109.14 USD |
| `1D` | `8.34` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 0.00 USD | 2,210.00 USD | 13.84 USD |
| `7D` | `8.34` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 4,430.00 USD |
| `1D` | `8.35` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 0.00 USD | 16,880.00 USD | 16,970.00 USD |
| `1D` | `8.36` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 17,800.00 USD |
| `7D` | `8.36` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 223,170.00 USD | 0.00 USD | 17,870.00 USD |
| `1D` | `8.37` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 691.75 USD | 6,430.00 USD | 16.86 USD |
| `1D` | `8.38` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 0.00 USD | 5,940.00 USD | 50,290.00 USD |
| `7D` | `8.38` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 57,740.00 USD |
| `1D` | `8.39` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 100,740.00 USD | 13,620.00 USD | 32,610.00 USD |
| `1D` | `8.40` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 10,500.00 USD | 7,000.00 USD | 51,900.00 USD |
| `7D` | `8.40` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 0.00 USD | 7,600.00 USD | 86,940.00 USD |
| `1D` | `8.41` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 0.00 USD | 2,050.00 USD | 0.00 USD |
| `1D` | `8.42` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 0.00 USD | 6,250.00 USD | 42,890.00 USD |
| `7D` | `8.42` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 210,920.00 USD | 0.00 USD | 35,220.00 USD |
| `1D` | `8.43` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 45,340.00 USD | 7,730.00 USD | 7,540.00 USD |
| `1D` | `8.44` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 11,130.00 USD | 27,610.00 USD | 160,460.00 USD |
| `7D` | `8.44` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 10,480.00 USD | 8,000.00 USD | 51,820.00 USD |
| `1D` | `8.45` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 54,790.00 USD | 0.00 USD | 163,170.00 USD |
| `1D` | `8.46` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 124,360.00 USD |
| `7D` | `8.46` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 152,650.00 USD | 0.00 USD | 119,740.00 USD |
| `1D` | `8.47` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 663.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.48` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 749.80 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.48` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 0.00 USD | 49,360.00 USD | 152,480.00 USD |
| `1D` | `8.49` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 12.70 USD |
| `1D` | `8.50` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 0.00 USD | 68,460.00 USD | 127,000.00 USD |
| `7D` | `8.50` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | 112,310.00 USD | 1,470.00 USD |
| `1D` | `8.51` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 0.00 USD | 21,730.00 USD | 172,440.00 USD |
| `1D` | `8.52` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 183,950.00 USD | 25,890.00 USD | 4,800.00 USD |
| `7D` | `8.52` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 114,580.00 USD | 135,400.00 USD | 92,000.00 USD |
| `1D` | `8.53` | 873,020.00 USD | 0.00 USD | 873,020.00 USD | 33,590.00 USD | 32,530.00 USD | 0.00 USD |
| `1D` | `8.54` | 806,900.00 USD | 0.00 USD | 806,900.00 USD | 202,800.00 USD | 3,210.00 USD | 156.94 USD |
| `7D` | `8.54` | 941,740.00 USD | 0.00 USD | 941,740.00 USD | 357,740.00 USD | 136,470.00 USD | 2,010.00 USD |
| `1D` | `8.55` | 600,730.00 USD | 0.00 USD | 600,730.00 USD | 152,290.00 USD | 0.00 USD | 25,120.00 USD |
| `1D` | `8.56` | 423,320.00 USD | 0.00 USD | 423,320.00 USD | 139,040.00 USD | 38,320.00 USD | 0.00 USD |
| `7D` | `8.56` | 445,520.00 USD | 0.00 USD | 445,520.00 USD | 151,290.00 USD | 122,650.00 USD | 790.79 USD |
| `1D` | `8.57` | 245,960.00 USD | 0.00 USD | 245,960.00 USD | 181,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.58` | 64,300.00 USD | 0.00 USD | 64,300.00 USD | 59,120.00 USD | 5,060.00 USD | 118.61 USD |
| `7D` | `8.58` | 170,790.00 USD | 0.00 USD | 170,790.00 USD | 4,370.00 USD | 164,810.00 USD | 1,620.00 USD |
| `1D` | `8.59` | 21,360.00 USD | 21,360.00 USD | 0.00 USD | 0.00 USD | 21,360.00 USD | 0.00 USD |
| `1D` | `8.59` | 42,720.00 USD | 42,720.00 USD | 0.00 USD | 0.00 USD | 21,360.00 USD | 0.00 USD |
| `7D` | `8.59` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.60` | 71,090.00 USD | 71,090.00 USD | 0.00 USD | 2,040.00 USD | 26,330.00 USD | 0.00 USD |
| `7D` | `8.60` | 2,020.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `8.61` | 72,280.00 USD | 72,280.00 USD | 0.00 USD | 497.00 USD | 0.00 USD | 699.64 USD |
| `1D` | `8.62` | 261,400.00 USD | 261,400.00 USD | 0.00 USD | 41,980.00 USD | 26,090.00 USD | 121,040.00 USD |
| `7D` | `8.62` | 33,350.00 USD | 33,350.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD | 28,520.00 USD |
| `1D` | `8.63` | 405,370.00 USD | 405,370.00 USD | 0.00 USD | 104,180.00 USD | 39,780.00 USD | 0.00 USD |
| `1D` | `8.64` | 450,440.00 USD | 450,440.00 USD | 0.00 USD | 0.00 USD | 6,540.00 USD | 38,530.00 USD |
| `7D` | `8.64` | 122,390.00 USD | 122,390.00 USD | 0.00 USD | 0.00 USD | 12,800.00 USD | 76,240.00 USD |
| `1D` | `8.65` | 556,460.00 USD | 556,460.00 USD | 0.00 USD | 3,580.00 USD | 6,810.00 USD | 95,630.00 USD |
| `1D` | `8.66` | 812,210.00 USD | 812,210.00 USD | 0.00 USD | 145,440.00 USD | 31,810.00 USD | 78,500.00 USD |
| `7D` | `8.66` | 337,190.00 USD | 337,190.00 USD | 0.00 USD | 191,350.00 USD | 22,640.00 USD | 804.96 USD |
| `1D` | `8.67` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 6,430.00 USD | 3,750.00 USD | 190,530.00 USD |
| `1D` | `8.68` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 68,460.00 USD | 12,020.00 USD | 25,890.00 USD |
| `7D` | `8.68` | 923,760.00 USD | 923,760.00 USD | 0.00 USD | 207,090.00 USD | 43,100.00 USD | 336,380.00 USD |
| `1D` | `8.69` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 10,820.00 USD | 16,260.00 USD | 33,840.00 USD |
| `1D` | `8.70` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 62,600.00 USD | 0.00 USD | 23,500.00 USD |
| `7D` | `8.70` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 116,370.00 USD | 41,840.00 USD | 46,400.00 USD |
| `1D` | `8.71` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 18,700.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.72` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 16,840.00 USD | 2,520.00 USD | 50,790.00 USD |
| `7D` | `8.72` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 609.73 USD |
| `1D` | `8.73` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 12,580.00 USD | 28,810.00 USD | 32,610.00 USD |
| `1D` | `8.74` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 38,500.00 USD | 3,500.00 USD | 12,900.00 USD |
| `7D` | `8.74` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 51,030.00 USD | 30,470.00 USD | 686.63 USD |
| `1D` | `8.75` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 33,520.00 USD | 4,580.00 USD | 4,980.00 USD |
| `1D` | `8.76` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 82,470.00 USD | 0.00 USD | 57,030.00 USD |
| `7D` | `8.76` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 196,960.00 USD | 0.00 USD | 58,950.00 USD |
| `1D` | `8.77` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 119,730.00 USD | 2,060.00 USD | 43,030.00 USD |
| `1D` | `8.78` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 41,500.00 USD | 20,740.00 USD | 50,110.00 USD |
| `7D` | `8.78` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 2,300.00 USD | 8,000.00 USD | 110,660.00 USD |
| `1D` | `8.79` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 31,710.00 USD | 12,000.00 USD | 29,010.00 USD |
| `1D` | `8.80` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 100,610.00 USD | 14,490.00 USD | 23,840.00 USD |
| `7D` | `8.80` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 27,360.00 USD | 33,750.00 USD | 32,140.00 USD |
| `1D` | `8.81` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 18,670.00 USD | 2,240.00 USD | 42.52 USD |
| `1D` | `8.82` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 2,200.00 USD | 0.00 USD | 19,620.00 USD |
| `7D` | `8.82` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 201,040.00 USD | 0.00 USD | 547.66 USD |
| `1D` | `8.83` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 73,290.00 USD | 12,580.00 USD | 0.00 USD |
| `1D` | `8.84` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 1,500.00 USD | 0.00 USD | 73,730.00 USD |
| `1D` | `8.85` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 13,040.00 USD | 3,360.00 USD | 11,200.00 USD |
| `1D` | `8.86` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 1,910.00 USD | 0.00 USD | 607.55 USD |
| `7D` | `8.86` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 29,310.00 USD | 0.00 USD | 83,000.00 USD |
| `1D` | `8.87` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 1,350.00 USD | 0.00 USD | 8,900.00 USD |
| `1D` | `8.88` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 803.70 USD | 10,670.00 USD | 186.36 USD |
| `7D` | `8.88` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,570.00 USD |
| `1D` | `8.89` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 3,660.00 USD | 3,410.00 USD | 32,910.00 USD |
| `1D` | `8.90` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 28,580.00 USD | 5,990.00 USD | 96,540.00 USD |
| `7D` | `8.90` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 2,440.00 USD | 0.00 USD | 116,250.00 USD |
| `1D` | `8.91` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 32,240.00 USD | 11,620.00 USD | 13,520.00 USD |
| `1D` | `8.92` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 1,110.00 USD | 1,020.00 USD | 67.52 USD |
| `7D` | `8.92` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 99,150.00 USD | 0.00 USD | 35,230.00 USD |
| `1D` | `8.93` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 31,830.00 USD | 1,810.00 USD | 38,940.00 USD |
| `1D` | `8.94` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 32,580.00 USD | 12,260.00 USD | 3,770.00 USD |
| `7D` | `8.94` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 58,330.00 USD | 0.00 USD | 433.10 USD |
| `1D` | `8.95` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 2,540.00 USD | 4,240.00 USD | 20,340.00 USD |
| `1D` | `8.96` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 1,260.00 USD | 0.00 USD | 175.90 USD |
| `7D` | `8.96` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 3,320.00 USD | 4,000.00 USD | 26,700.00 USD |
| `1D` | `8.98` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 35,320.00 USD | 7,700.00 USD | 19,670.00 USD |
| `7D` | `8.98` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,090.00 USD |
| `1D` | `8.99` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 48,100.00 USD | 24,940.00 USD | 3,420.00 USD |
| `1D` | `9.00` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 36,960.00 USD | 0.00 USD | 8,090.00 USD |
| `7D` | `9.00` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 298,640.00 USD | 11,360.00 USD | 21,640.00 USD |
| `1D` | `9.01` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 1,980.00 USD | 12,030.00 USD | 16,150.00 USD |
| `1D` | `9.02` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 39,120.00 USD | 33,630.00 USD | 5,010.00 USD |
| `7D` | `9.02` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 82,280.00 USD | 56,120.00 USD | 1,200.00 USD |
| `1D` | `9.03` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 125,760.00 USD | 14,810.00 USD | 34,410.00 USD |
| `1D` | `9.04` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 40,880.00 USD | 10,710.00 USD | 21,020.00 USD |
| `7D` | `9.04` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 135,320.00 USD | 74,750.00 USD | 16,220.00 USD |
| `1D` | `9.05` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 21,500.00 USD | 13,500.00 USD | 29,630.00 USD |
| `1D` | `9.06` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 27,800.00 USD | 6,890.00 USD | 12,830.00 USD |
| `7D` | `9.06` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 7,440.00 USD | 14,960.00 USD | 53,420.00 USD |
| `1D` | `9.07` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 13,580.00 USD | 18,880.00 USD | 30,980.00 USD |
| `1D` | `9.08` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 13,510.00 USD | 3,370.00 USD | 39,960.00 USD |
| `7D` | `9.08` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD |
| `1D` | `9.09` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 88,250.00 USD | 11,440.00 USD | 31,640.00 USD |
| `1D` | `9.10` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 16,430.00 USD | 16,280.00 USD | 36,960.00 USD |
| `7D` | `9.10` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 826,500.00 USD | 35,760.00 USD | 334,610.00 USD |
| `1D` | `9.11` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 61,080.00 USD | 14,420.00 USD | 82,390.00 USD |
| `1D` | `9.12` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 102,100.00 USD | 22,410.00 USD | 26,360.00 USD |
| `7D` | `9.12` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 465,780.00 USD | 24,170.00 USD | 503,360.00 USD |
| `1D` | `9.13` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 75,050.00 USD | 15,960.00 USD | 40,180.00 USD |
| `1D` | `9.14` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 30,520.00 USD | 3,380.00 USD | 29,600.00 USD |
| `7D` | `9.14` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 536,560.00 USD | 18,540.00 USD | 500,290.00 USD |
| `1D` | `9.15` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 57,140.00 USD | 23,170.00 USD | 22,990.00 USD |
| `1D` | `9.16` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 63,930.00 USD | 23,900.00 USD | 32,470.00 USD |
| `7D` | `9.16` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 358,370.00 USD | 44,360.00 USD | 195,800.00 USD |
| `1D` | `9.17` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 80,620.00 USD | 3,200.00 USD | 49,540.00 USD |
| `1D` | `9.18` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 28,620.00 USD | 26,430.00 USD | 31,220.00 USD |
| `7D` | `9.18` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 566,340.00 USD | 162,460.00 USD | 292,040.00 USD |
| `1D` | `9.19` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 77,850.00 USD | 29,140.00 USD | 7,680.00 USD |
| `1D` | `9.20` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 64,620.00 USD | 11,090.00 USD | 37,460.00 USD |
| `7D` | `9.20` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 549,250.00 USD | 134,550.00 USD | 238,840.00 USD |
| `1D` | `9.21` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 29,720.00 USD | 2,950.00 USD | 4,650.00 USD |
| `1D` | `9.22` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 58,850.00 USD | 2,850.00 USD | 11,100.00 USD |
| `7D` | `9.22` | 10,200,000.00 USD | 10,200,000.00 USD | 0.00 USD | 620,010.00 USD | 144,840.00 USD | 416,230.00 USD |
| `1D` | `9.23` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 883.09 USD | 4,270.00 USD | 17.80 USD |
| `1D` | `9.24` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 45,960.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `9.24` | 10,770,000.00 USD | 10,770,000.00 USD | 0.00 USD | 336,360.00 USD | 56,410.00 USD | 174,910.00 USD |
| `1D` | `9.25` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 17,320.00 USD | 5,840.00 USD | 9,510.00 USD |
| `1D` | `9.26` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 1,260.00 USD | 0.00 USD | 3,540.00 USD |
| `7D` | `9.26` | 11,200,000.00 USD | 11,200,000.00 USD | 0.00 USD | 273,920.00 USD | 96,980.00 USD | 60,730.00 USD |
| `1D` | `9.27` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 23,580.00 USD | 1,360.00 USD | 6,640.00 USD |
| `1D` | `9.28` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 1,530.00 USD | 8,760.00 USD | 169.17 USD |
| `7D` | `9.28` | 11,900,000.00 USD | 11,900,000.00 USD | 0.00 USD | 428,160.00 USD | 103,490.00 USD | 170,910.00 USD |
| `1D` | `9.29` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 16,190.00 USD | 4,140.00 USD | 17,930.00 USD |
| `1D` | `9.30` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 39,850.00 USD | 7,520.00 USD | 11,600.00 USD |
| `7D` | `9.30` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 199,810.00 USD | 97,780.00 USD | 262,830.00 USD |
| `1D` | `9.31` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 27,750.00 USD | 5,020.00 USD | 12,920.00 USD |
| `1D` | `9.32` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 9,610.00 USD | 0.00 USD | 5,070.00 USD |
| `7D` | `9.32` | 13,130,000.00 USD | 13,130,000.00 USD | 0.00 USD | 271,660.00 USD | 59,310.00 USD | 338,330.00 USD |
| `1D` | `9.33` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 7,990.00 USD | 6,000.00 USD | 8,120.00 USD |
| `1D` | `9.34` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 46,210.00 USD | 3,660.00 USD | 3,340.00 USD |
| `7D` | `9.34` | 13,470,000.00 USD | 13,470,000.00 USD | 0.00 USD | 216,530.00 USD | 53,150.00 USD | 70,540.00 USD |
| `1D` | `9.35` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 13,620.00 USD | 0.00 USD | 14,910.00 USD |
| `1D` | `9.36` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 4,730.00 USD | 6,760.00 USD | 8,030.00 USD |
| `7D` | `9.36` | 13,890,000.00 USD | 13,890,000.00 USD | 0.00 USD | 247,120.00 USD | 73,430.00 USD | 97,710.00 USD |
| `1D` | `9.37` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 12,900.00 USD | 5,670.00 USD | 2,720.00 USD |
| `1D` | `9.38` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 15,290.00 USD | 0.00 USD | 13,850.00 USD |
| `7D` | `9.38` | 14,270,000.00 USD | 14,270,000.00 USD | 0.00 USD | 277,080.00 USD | 31,100.00 USD | 77,300.00 USD |
| `1D` | `9.39` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 9,080.00 USD | 0.00 USD | 12.70 USD |
| `1D` | `9.40` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 22,270.00 USD | 0.00 USD | 12.64 USD |
| `7D` | `9.40` | 14,680,000.00 USD | 14,680,000.00 USD | 0.00 USD | 234,760.00 USD | 42,520.00 USD | 124,730.00 USD |
| `1D` | `9.41` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 963.73 USD | 0.00 USD | 10,140.00 USD |
| `1D` | `9.42` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 9,100.00 USD | 2,390.00 USD | 6,520.00 USD |
| `7D` | `9.42` | 14,870,000.00 USD | 14,870,000.00 USD | 0.00 USD | 108,840.00 USD | 19,780.00 USD | 70,640.00 USD |
| `1D` | `9.43` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 5,380.00 USD | 700.38 USD | 20.54 USD |
| `1D` | `9.44` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 795.69 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.44` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 80,230.00 USD | 19,420.00 USD | 63,710.00 USD |
| `1D` | `9.45` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 96.25 USD | 0.00 USD | 5,600.00 USD |
| `1D` | `9.46` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 9,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.46` | 15,140,000.00 USD | 15,140,000.00 USD | 0.00 USD | 60,810.00 USD | 17,010.00 USD | 19,460.00 USD |
| `1D` | `9.47` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 1,050.00 USD | 1,250.00 USD | 8,050.00 USD |
| `1D` | `9.48` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 38.30 USD | 0.00 USD | 2,040.00 USD |
| `7D` | `9.48` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 12,180.00 USD | 11,060.00 USD | 35,620.00 USD |
| `1D` | `9.49` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 20,610.00 USD | 572.85 USD | 5,870.00 USD |
| `1D` | `9.50` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 4,500.00 USD | 930.34 USD | 0.00 USD |
| `7D` | `9.50` | 15,310,000.00 USD | 15,310,000.00 USD | 0.00 USD | 65,230.00 USD | 9,430.00 USD | 45,440.00 USD |
| `7D` | `9.52` | 15,440,000.00 USD | 15,440,000.00 USD | 0.00 USD | 46,900.00 USD | 23,260.00 USD | 51,740.00 USD |
| `7D` | `9.54` | 15,550,000.00 USD | 15,550,000.00 USD | 0.00 USD | 87,890.00 USD | 25,090.00 USD | 930.52 USD |
| `7D` | `9.56` | 15,600,000.00 USD | 15,600,000.00 USD | 0.00 USD | 35,290.00 USD | 5,260.00 USD | 4,800.00 USD |
| `7D` | `9.58` | 15,660,000.00 USD | 15,660,000.00 USD | 0.00 USD | 35,340.00 USD | 2,380.00 USD | 27,300.00 USD |
| `7D` | `9.60` | 15,720,000.00 USD | 15,720,000.00 USD | 0.00 USD | 38,740.00 USD | 5,460.00 USD | 18,930.00 USD |
| `7D` | `9.62` | 15,770,000.00 USD | 15,770,000.00 USD | 0.00 USD | 36,420.00 USD | 1,540.00 USD | 10,980.00 USD |
| `7D` | `9.64` | 15,840,000.00 USD | 15,840,000.00 USD | 0.00 USD | 33,970.00 USD | 11,240.00 USD | 19,940.00 USD |
| `7D` | `9.66` | 15,910,000.00 USD | 15,910,000.00 USD | 0.00 USD | 37,340.00 USD | 12,890.00 USD | 18,480.00 USD |
| `7D` | `9.68` | 15,990,000.00 USD | 15,990,000.00 USD | 0.00 USD | 56,110.00 USD | 8,420.00 USD | 15,070.00 USD |
| `7D` | `9.70` | 16,080,000.00 USD | 16,080,000.00 USD | 0.00 USD | 50,240.00 USD | 9,960.00 USD | 31,670.00 USD |
| `7D` | `9.72` | 16,140,000.00 USD | 16,140,000.00 USD | 0.00 USD | 24,700.00 USD | 6,920.00 USD | 26,680.00 USD |
| `7D` | `9.74` | 16,180,000.00 USD | 16,180,000.00 USD | 0.00 USD | 17,650.00 USD | 7,200.00 USD | 18,330.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `356.92M` | Total OI Tokens: `41,558,205.7 AVAX`
  * 1h OI Change: `-0.10%` | 4h OI Change: `+3.86%` | 24h OI Change: `-6.62%`
  * Exchange Breakdown: Binance=`81.69M` | Bybit=`58.20M` | OKX=`11.69M` | Hyperliquid=`16.92M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-1.31K` | Last 24h: `18.18K` | Last 3d: `59.53K` | Last 7d: `106.20K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0176%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0044%` | **USDT Bitget** | `0.0071%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `55.04%` | `44.96%` | `1.22` | 10,590,000.00 USD |
| `15M` | `Binance` | `55.31%` | `44.69%` | `1.24` | 3,840,000.00 USD |
| `15M` | `OKX` | `55.45%` | `44.55%` | `1.24` | 2,290,000.00 USD |
| `15M` | `Bybit` | `57.84%` | `42.16%` | `1.37` | 742,510.00 USD |
| `15M` | `KuCoin` | `80.31%` | `19.69%` | `4.08` | 40,730.00 USD |
| `15M` | `Gate` | `51.97%` | `48.03%` | `1.08` | 1,720,000.00 USD |
| `15M` | `Bitget` | `53.11%` | `46.89%` | `1.13` | 184,490.00 USD |
| `15M` | `BingX` | `52.53%` | `47.47%` | `1.11` | 310,570.00 USD |
| `15M` | `MEXC` | `63%` | `37%` | `1.70` | 870,110.00 USD |
| `15M` | `Bitunix` | `56.55%` | `43.45%` | `1.30` | 227,230.00 USD |
| `15M` | `Hyperliquid` | `51.52%` | `48.48%` | `1.06` | 33,930.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `57.38%` | `42.62%` | `1.35` | 61,220.00 USD |
| `15M` | `Crypto.com` | `1.03%` | `98.97%` | `0.01` | 3,240.00 USD |
| `15M` | `WhiteBIT` | `22.81%` | `77.19%` | `0.30` | 169,270.00 USD |
| `15M` | `HTX` | `48.03%` | `51.97%` | `0.92` | 31,750.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `54.7%` | `45.3%` | `1.21` | 65,010.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `19.85%` | `80.15%` | `0.25` | 1,740.00 USD |
| `15M` | `Whale Positions` | `55.31%` | `44.69%` | `1.24` | 3,840,000.00 USD |
| `15M` | `Global Accounts` | `55.04%` | `44.96%` | `1.22` | 10,590,000.00 USD |
| `1H` | `AVAX` | `45.20%` | `54.80%` | `0.82` | 48,320,000.00 USD |
| `1H` | `Binance` | `52.17%` | `47.83%` | `1.09` | 25,500,000.00 USD |
| `1H` | `OKX` | `41.02%` | `58.98%` | `0.70` | 6,900,000.00 USD |
| `1H` | `Bybit` | `35.55%` | `64.45%` | `0.55` | 7,170,000.00 USD |
| `1H` | `KuCoin` | `41.4%` | `58.6%` | `0.71` | 729,750.00 USD |
| `1H` | `Gate` | `35.11%` | `64.89%` | `0.54` | 949,570.00 USD |
| `1H` | `Bitget` | `38.16%` | `61.84%` | `0.62` | 1,450,000.00 USD |
| `1H` | `BingX` | `41.73%` | `58.27%` | `0.72` | 443,390.00 USD |
| `1H` | `MEXC` | `45.26%` | `54.74%` | `0.83` | 650,800.00 USD |
| `1H` | `Bitunix` | `32.27%` | `67.73%` | `0.48` | 1,440,000.00 USD |
| `1H` | `Hyperliquid` | `43.46%` | `56.54%` | `0.77` | 1,100,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `67.31%` | `32.69%` | `2.06` | 1,040,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `58.29%` | `41.71%` | `1.40` | 226,240.00 USD |
| `1H` | `HTX` | `60.23%` | `39.77%` | `1.51` | 373,330.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `80.12%` | `19.88%` | `4.03` | 134,550.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `20.09%` | `79.91%` | `0.25` | 208,040.00 USD |
| `1H` | `Whale Positions` | `52.17%` | `47.83%` | `1.09` | 25,500,000.00 USD |
| `1H` | `Global Accounts` | `45.20%` | `54.80%` | `0.82` | 48,320,000.00 USD |
| `4H` | `AVAX` | `50.88%` | `49.12%` | `1.04` | 130,350,000.00 USD |
| `4H` | `Binance` | `54.23%` | `45.77%` | `1.18` | 47,880,000.00 USD |
| `4H` | `OKX` | `46.44%` | `53.56%` | `0.87` | 13,760,000.00 USD |
| `4H` | `Bybit` | `43.49%` | `56.51%` | `0.77` | 15,270,000.00 USD |
| `4H` | `KuCoin` | `48.38%` | `51.62%` | `0.94` | 889,610.00 USD |
| `4H` | `Gate` | `44.77%` | `55.23%` | `0.81` | 2,320,000.00 USD |
| `4H` | `Bitget` | `58.99%` | `41.01%` | `1.44` | 5,830,000.00 USD |
| `4H` | `BingX` | `32.76%` | `67.24%` | `0.49` | 4,100,000.00 USD |
| `4H` | `MEXC` | `49.56%` | `50.44%` | `0.98` | 26,610,000.00 USD |
| `4H` | `Bitunix` | `38.32%` | `61.68%` | `0.62` | 4,800,000.00 USD |
| `4H` | `Hyperliquid` | `69.57%` | `30.43%` | `2.29` | 4,010,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `54.8%` | `45.2%` | `1.21` | 1,970,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `67.97%` | `32.03%` | `2.12` | 578,600.00 USD |
| `4H` | `HTX` | `52.99%` | `47.01%` | `1.13` | 90,500.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `90.95%` | `9.05%` | `10.05` | 1,310,000.00 USD |
| `4H` | `Aster` | `61.72%` | `38.28%` | `1.61` | 696,150.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `46.67%` | `53.33%` | `0.88` | 220,600.00 USD |
| `4H` | `Whale Positions` | `54.23%` | `45.77%` | `1.18` | 47,880,000.00 USD |
| `4H` | `Global Accounts` | `50.88%` | `49.12%` | `1.04` | 130,350,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `8.43` | `8.45` | `8.43` | `8.48` | `8.43` | 1,888,943.37 USD | 611,021.12 USD | 1,277,922.26 USD | -666,901.14 USD | `-35.31%` | `4B / 11S` |
| `0:00 UTC` | `8.42` | `8.42` | `8.42` | `8.47` | `8.40` | 987,610.98 USD | 453,562.40 USD | 534,048.58 USD | -80,486.17 USD | `-8.15%` | `8B / 9S` |
| `5:00 UTC` | `8.49` | `8.49` | `8.49` | `8.51` | `8.45` | 1,927,143.92 USD | 1,382,163.88 USD | 544,980.04 USD | 837,183.84 USD | `+43.44%` | `23B / 5S` |
| `0:00 UTC` | `8.51` | `8.51` | `8.51` | `8.53` | `8.49` | 1,011,410.99 USD | 608,193.60 USD | 403,217.39 USD | 204,976.20 USD | `+20.27%` | `7B / 2S` |
| `5:00 UTC` | `8.54` | `8.54` | `8.54` | `8.56` | `8.52` | 2,075,576.75 USD | 880,640.95 USD | 1,194,935.80 USD | -314,294.84 USD | `-15.14%` | `5B / 5S` |
| `0:00 UTC` | `8.60` | `8.58` | `8.60` | `8.61` | `8.53` | 2,341,070.35 USD | 1,614,335.42 USD | 726,734.93 USD | 887,600.49 USD | `+37.91%` | `23B / 4S` |
| `5:00 UTC` | `8.58` | `8.57` | `8.58` | `8.58` | `8.56` | 905,120.57 USD | 371,003.65 USD | 534,116.93 USD | -163,113.28 USD | `-18.02%` | `1B / 6S` |
| `0:00 UTC` | `8.61` | `8.60` | `8.61` | `8.62` | `8.57` | 800,790.84 USD | 395,337.20 USD | 405,453.63 USD | -10,116.43 USD | `-1.26%` | `6B / 6S` |
| `5:00 UTC` | `8.56` | `8.58` | `8.56` | `8.62` | `8.55` | 1,779,150.79 USD | 495,653.58 USD | 1,283,497.21 USD | -787,843.63 USD | `-44.28%` | `6B / 33S` |
| `0:00 UTC` | `8.59` | `8.57` | `8.59` | `8.60` | `8.54` | 815,989.24 USD | 423,948.91 USD | 392,040.33 USD | 31,908.58 USD | `+3.91%` | `8B / 6S` |

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
| `5m` | 7,870.00 USD | 222,030.00 USD | **`ACCUMULATION`** |
| `15m` | 14,630.00 USD | 350,160.00 USD | **`ACCUMULATION`** |
| `30m` | -88,610.00 USD | -898,950.00 USD | **`DISTRIBUTION`** |
| `1h` | -74,300.00 USD | -1,270,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 411,860.00 USD | 101,570.00 USD | **`ACCUMULATION`** |
| `4h` | 486,240.00 USD | 946,700.00 USD | **`ACCUMULATION`** |
| `6h` | -942,360.00 USD | -730,400.00 USD | **`DISTRIBUTION`** |
| `8h` | -417,760.00 USD | -372,510.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,290,000.00 USD | -8,330,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,520,000.00 USD | -10,980,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -8,360,000.00 USD | -54,660,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -57,050,000.00 USD | -266,160,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+7.87K` | 15m=`+14.63K` | 1h=`-74.30K` | 24h=`-2.52M`
* Futures Capital Netflows: 5m=`+222.03K` | 15m=`+350.16K` | 1h=`-1.27M` | 24h=`-10.98M`
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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `8.15` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `8.02` (Risk Distance: `0.1293` pts)
  * +2.5R Take Profit: `8.47`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.46` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `8.59` (Risk Distance: `0.1293` pts)
  * +2.5R Take Profit: `8.14`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.65`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
