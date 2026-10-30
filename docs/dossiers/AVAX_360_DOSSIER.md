# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 11:20:15 IST` (`2026-10-30 05:50:15 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.59` | **Live Ask Quote**: `8.62` | **Mid Price**: `8.61`
- **Spread Points**: `3.00` | **Spread BPS**: `34.86 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.24` | VWAP Z-Score: `+2.07` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0711` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `65.23` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `8.67` | Lower -3.00σ Band: `7.80`
  * Upper +2.51σ Band: `8.60` | Lower -2.51σ Band: `7.87`
  * Upper +2.01σ Band: `8.53` | Lower -2.01σ Band: `7.95`
  * Upper +2.00σ Band: `8.53` | Lower -2.00σ Band: `7.95`
  * Upper +1.28σ Band: `8.42` | Lower -1.28σ Band: `8.05`
  * Upper +1.00σ Band: `8.38` | Lower -1.00σ Band: `8.09`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.46` | EMA-20=`8.40` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.46` (Slope: `+0.0000`) | EMA-100=`8.57`
  * Institutional Anchors: EMA-144=`8.62` | EMA-200=`8.67` (Slope: `-0.3678`) | EMA-233=`8.70`
- **Range Boundaries**: 24H High=`9.06` | 24H Low=`7.97` | Weekly High=`9.14` | Weekly Low=`7.97`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.46` (Distance: `+1.67%`)
  * Point of Control (POC) = `8.32` (Distance: `+3.43%`)
  * Value Area Low (VAL) = `8.16` (Distance: `+5.48%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`8.90` | POC=`8.74` | VAL=`8.55`
  * Prior Day Extremes: PDH=`9.06` | PDL=`8.24` | PDC=`8.33`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`9.02` | Weekly POC=`8.92` | Weekly VAL=`8.72`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`8.58` | Low=`7.97`
  * London Session (08:00-16:00 UTC): High=`8.59` | Low=`8.50`
  * New York Session (13:00-21:00 UTC): High=`8.66` | Low=`8.55`
  * Initial Balance (First Hour): IB High=`8.59` | IB Low=`8.50`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.57` - `8.64`
  * Optimal Trade Entry (OTE 0.705): `8.62`
  * Structural Invalidation Anchor (0.786): `8.67`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.58` | `8.59` | `8.57` | `8.58` | `28,875` | 247,705.04 USD | 4,468.63 USD | `+1.80%` | -4,508,221.91 USD | `-0.27` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `8.58` | `8.61` | `8.58` | `8.60` | `37,351` | 321,256.58 USD | -1,221.14 USD | `-0.38%` | -4,509,443.05 USD | `-0.29` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `8.60` | `8.62` | `8.59` | `8.62` | `20,431` | 175,848.07 USD | -12,158.23 USD | `-6.91%` | -4,521,601.27 USD | `-0.36` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `8.54` | `8.61` | `8.53` | `8.56` | `272,718` | 2,341,070.35 USD | 887,600.49 USD | `+37.91%` | -4,349,577.26 USD | `+1.04` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.56` | `8.58` | `8.56` | `8.57` | `105,632` | 905,120.57 USD | -163,113.28 USD | `-18.02%` | -4,512,690.54 USD | `-0.78` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `8.58` | `8.62` | `8.57` | `8.62` | `86,324` | 741,939.91 USD | -6,040.95 USD | `-0.81%` | -4,518,731.49 USD | `-0.43` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `8.31` | `8.48` | `8.31` | `8.45` | `689,044` | 5,789,252.19 USD | 234,770.73 USD | `+4.06%` | -5,773,198.54 USD | `+0.33` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `8.45` | `8.56` | `8.40` | `8.54` | `706,146` | 6,001,742.64 USD | 647,379.02 USD | `+10.79%` | -5,125,819.51 USD | `+0.57` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `8.54` | `8.62` | `8.53` | `8.62` | `465,007` | 3,991,000.62 USD | 715,576.47 USD | `+17.93%` | -4,410,243.04 USD | `+0.58` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,637,505.96 USD | `-1.25` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -5,927,287.94 USD | `+0.62` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.62` | `8.40` | `8.62` | `1,171,153` | 9,992,743.26 USD | 1,362,955.50 USD | `+13.64%` | -4,564,332.44 USD | `+1.30` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | 210,435.51 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -2,301,560.13 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,637,505.96 USD | `-1.25` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -5,927,287.94 USD | `+0.62` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.62` | `8.40` | `8.62` | `1,171,153` | 9,992,743.26 USD | 1,362,955.50 USD | `+13.64%` | -4,564,332.44 USD | `+1.30` | **`BULLISH`** | `DELTA ALIGNED` |

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
| --- | **`8.61`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `8.61` | `115.9800` | 999.10 USD | 10,552.47 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.61` | `111.0100` | 956.21 USD | 11,508.68 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.61` | `111.0100` | 956.13 USD | 12,464.81 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.61` | `96.6000` | 832.01 USD | 13,296.82 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.61` | `1643.1500` | 14,151.30 USD | 27,448.12 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `8.61` | `110.5600` | 952.16 USD | 28,400.28 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `8.61` | `586.3700` | 5,049.88 USD | 33,450.16 USD | `3 orders` | `-0.08%` | `-` |
| `ASK` | `8.62` | `120.0800` | 1,035.58 USD | 50,929.22 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.62` | `315.7300` | 2,722.86 USD | 49,893.64 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.62` | `1270.2900` | 10,954.85 USD | 47,170.79 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.62` | `110.5400` | 953.27 USD | 36,215.93 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.62` | `9.5000` | 81.92 USD | 35,262.66 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.62` | `56.6000` | 488.08 USD | 35,180.73 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.62` | `110.5400` | 953.20 USD | 34,692.66 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.62` | `200.0000` | 1,724.58 USD | 33,739.46 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.62` | `5.8000` | 50.01 USD | 32,014.88 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.62` | `132.4400` | 1,141.95 USD | 31,964.87 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `8.62` | `110.5500` | 953.15 USD | 30,822.92 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.62` | `1.2800` | 11.04 USD | 29,869.77 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.62` | `927.9600` | 8,000.22 USD | 29,858.73 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.62` | `1197.9600` | 10,327.37 USD | 21,858.51 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.62` | `113.7500` | 980.60 USD | 11,531.13 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.62` | `82.9100` | 714.73 USD | 10,550.53 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.62` | `151.2700` | 1,304.01 USD | 9,835.80 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.62` | `768.6500` | 6,625.92 USD | 8,531.79 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `8.62` | `110.5500` | 952.95 USD | 1,905.87 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `8.62` | `110.5500` | 952.92 USD | 952.92 USD | `1 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `8.62` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.62` | `0.00%` | `-` |
| `BID` | `8.62` | `146.5500` | 1,263.01 USD | 1,263.01 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.62` | `110.5500` | 952.65 USD | 2,215.67 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.62` | `44.8500` | 386.49 USD | 2,602.15 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `8.62` | `110.5700` | 952.76 USD | 3,554.91 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.62` | `120.0800` | 1,034.62 USD | 4,589.53 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.62` | `110.5300` | 952.32 USD | 5,541.85 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.62` | `82.9100` | 714.34 USD | 6,256.18 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.62` | `50.0000` | 430.78 USD | 6,686.96 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.62` | `7.9900` | 68.84 USD | 6,755.80 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.62` | `16.0000` | 137.84 USD | 6,893.64 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.62` | `50.0000` | 430.76 USD | 7,324.40 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.62` | `171.5400` | 1,477.83 USD | 8,802.23 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.62` | `87.1900` | 751.14 USD | 9,553.38 USD | `1 orders` | `-0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:13:49 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1466` | `0x7737...bf66` | `SHORT` | 1,479,191.19 USD | `171,568.06` | `7.43` | `8.61` | `108.43` | -203,646.17 USD | `-13.77%` | `10X Cross` |
| `1561` | `0xeadc...9d55` | `LONG` | 1,380,064.34 USD | `160,070.56` | `8.11` | `8.61` | `0.000000` | 82,426.77 USD | `+5.97%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `8.60` | 6,000.31 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 6.00K USD at 8.6005 USD [API] | `2026-10-29 02:47:02` |
| `ANNOUNCEMENT` | `INFO` | `8.67` | 5,999.89 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 6.00K USD at 8.6676 USD [API] | `2026-10-29 02:58:40` |
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
| `Live` | `Long Liquidation` | `1.84` | 212.18 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 212.20 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 160.40 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 8,580.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 244.38 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 109.60 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 254.72 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 110.07 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 138.58 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 942.44 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 320.28 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 232.67 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 20,100.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111.12 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 23,550.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 1,320.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 1,260.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 151.88 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 392.22 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 582.15 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 109.95 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 9,010.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.96` | 2,640.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 159.29 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.21` | 195.03 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 564.61 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 110.77 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.49` | 285.92 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 486.93 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 2,930.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 587.97 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 8,380.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.70` | 7,040.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.71` | 202.64 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 467.01 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 3,880.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,230.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 16,180.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 352.68 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 4,090.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.99` | 1,280.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.00` | 2,770.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.03` | 167.78 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 314.59 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 504.74 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 213.20 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 223.43 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.09` | 651.75 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 915.43 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 250.20 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 396.06 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 726.25 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.20` | 601.94 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 5,480.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 300.91 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 503.78 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 1,050.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.26` | 162,470.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 640.70 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.32` | 232.85 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 716.11 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 660.46 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.41` | 1,090.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 20,160.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 1,470.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.47` | 1,320.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.51` | 367.41 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 557.76 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 2,880.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 269.31 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.59` | 34,430.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.62` | 2,810.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 468.55 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.71` | 147.33 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.72` | 2,390.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 661.65 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 1,350.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 635.31 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 580.50 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 106.65 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.83` | 145.88 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.86` | 2,110.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 984.70 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.92` | 277.35 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 11,720.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 6,320.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 331.68 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 105.61 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 265.10 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 405.14 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,130.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 1,140.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 137.02 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.13` | 2,030.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 7,810.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 972.65 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.29` | 3,890.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 1,700.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 284,770.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 6,410.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 357,940.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 806,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 484.64 USD | 806,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 805,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 1,050.00 USD | 798,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 852.03 USD | 797,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 796,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 1,770.00 USD | 787,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.59` | 1,100.00 USD | 786,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 784,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 364.90 USD | 782,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.63` | 245.89 USD | 782,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.67` | 1,320.00 USD | 782,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.68` | 4,680.00 USD | 780,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 16,570.00 USD | 776,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 6,180.00 USD | 759,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 753,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 6,780.00 USD | 752,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 21,580.00 USD | 745,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 4,720.00 USD | 723,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 1,500.00 USD | 719,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 7,230.00 USD | 717,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 1,140.00 USD | 710,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,710.00 USD | 709,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 1,580.00 USD | 705,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.92` | 579.62 USD | 703,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.93` | 3,500.00 USD | 703,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 3,980.00 USD | 699,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 3,480.00 USD | 695,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 636.74 USD | 692,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.97` | 128,810.00 USD | 691,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.99` | 297.49 USD | 562,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 746.58 USD | 562,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 21,040.00 USD | 561,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.03` | 1,370.00 USD | 540,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 354.23 USD | 539,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.07` | 23,600.00 USD | 539,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 7,420.00 USD | 515,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,050.00 USD | 508,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.09` | 2,130.00 USD | 507,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 28,530.00 USD | 504,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 476,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 28,500.00 USD | 476,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.13` | 7,560,000.00 USD | 7,560,000.00 USD | 18,640.00 USD | 15,550.00 USD | 22,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.13` | 777.50 USD | 447,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,270.00 USD | 446,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.15` | 7,500,000.00 USD | 7,500,000.00 USD | 48,450.00 USD | 13,490.00 USD | 43,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.17` | 7,400,000.00 USD | 7,400,000.00 USD | 28,970.00 USD | 1,110.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.17` | 2,380.00 USD | 426,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 424,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.19` | 7,340,000.00 USD | 7,340,000.00 USD | 1,420.00 USD | 11,080.00 USD | 10,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.21` | 7,320,000.00 USD | 7,320,000.00 USD | 11,990.00 USD | 2,530.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.21` | 322.94 USD | 422,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.23` | 7,300,000.00 USD | 7,300,000.00 USD | 37,070.00 USD | 4,000.00 USD | 14,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.24` | 1,480.00 USD | 422,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 185.83 USD | 420,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.25` | 7,240,000.00 USD | 7,240,000.00 USD | 14,900.00 USD | 0.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.25` | 21,280.00 USD | 420,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.27` | 7,220,000.00 USD | 7,220,000.00 USD | 420.05 USD | 1,810.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,420.00 USD | 399,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.29` | 7,210,000.00 USD | 7,210,000.00 USD | 7,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.29` | 1,680.00 USD | 363,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.31` | 7,210,000.00 USD | 7,210,000.00 USD | 252.80 USD | 0.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.32` | 900.18 USD | 361,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.33` | 7,190,000.00 USD | 7,190,000.00 USD | 7,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.34` | 4,370.00 USD | 360,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.36` | 13,140.00 USD | 356,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.37` | 2,940.00 USD | 342,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.37` | 7,180,000.00 USD | 7,180,000.00 USD | 45,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.38` | 2,130.00 USD | 339,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 227.97 USD | 337,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.39` | 7,140,000.00 USD | 7,140,000.00 USD | 46,200.00 USD | 0.00 USD | 503.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.41` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 0.00 USD | 457.98 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.42` | 147.61 USD | 337,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.43` | 2,430.00 USD | 337,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 2,410.00 USD | 335,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.45` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.46` | 10,390.00 USD | 332,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 4,590.00 USD | 322,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 1,120.00 USD | 317,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.49` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 962.81 USD | 316,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 421.78 USD | 315,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.51` | 7,050,000.00 USD | 7,050,000.00 USD | 2,070.00 USD | 0.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.51` | 1,710.00 USD | 315,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.53` | 1,570.00 USD | 313,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.53` | 7,030,000.00 USD | 7,030,000.00 USD | 35,990.00 USD | 18,910.00 USD | 609.73 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 311,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.55` | 6,370,000.00 USD | 6,370,000.00 USD | 8,130.00 USD | 4,270.00 USD | 169.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.55` | 6,970,000.00 USD | 6,970,000.00 USD | 20,150.00 USD | 4,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.55` | 1,930.00 USD | 307,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.56` | 6,360,000.00 USD | 6,360,000.00 USD | 14,910.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.57` | 25,060.00 USD | 305,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.57` | 6,340,000.00 USD | 6,340,000.00 USD | 342.65 USD | 0.00 USD | 156.94 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.58` | 118.25 USD | 280,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.58` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.59` | 6,330,000.00 USD | 6,330,000.00 USD | 1,390.00 USD | 0.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.59` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 0.00 USD | 301.55 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.59` | 26,390.00 USD | 280,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.60` | 6,330,000.00 USD | 6,330,000.00 USD | 629.05 USD | 4,900.00 USD | 249.50 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.61` | 6,320,000.00 USD | 6,320,000.00 USD | 1,190.00 USD | 761.26 USD | 11,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 754.04 USD | 254,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.62` | 6,310,000.00 USD | 6,310,000.00 USD | 916.10 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 253,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.63` | 6,310,000.00 USD | 6,310,000.00 USD | 986.95 USD | 0.00 USD | 8,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.63` | 6,950,000.00 USD | 6,950,000.00 USD | 41,300.00 USD | 0.00 USD | 957.01 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.63` | 378.93 USD | 252,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.64` | 6,300,000.00 USD | 6,300,000.00 USD | 33,010.00 USD | 812.96 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.65` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 0.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.65` | 6,900,000.00 USD | 6,900,000.00 USD | 4,870.00 USD | 0.00 USD | 754.30 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 252,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.66` | 6,250,000.00 USD | 6,250,000.00 USD | 3,030.00 USD | 0.00 USD | 99.94 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 256.09 USD | 252,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.67` | 6,250,000.00 USD | 6,250,000.00 USD | 1,140.00 USD | 0.00 USD | 947.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.67` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 34,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 4,480.00 USD | 251,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.68` | 6,250,000.00 USD | 6,250,000.00 USD | 749.80 USD | 0.00 USD | 3,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.68` | 739.30 USD | 247,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.69` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 42.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.69` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 0.00 USD | 263.97 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.70` | 6,690.00 USD | 246,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.70` | 6,250,000.00 USD | 6,250,000.00 USD | 551.10 USD | 2,390.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.71` | 6,230,000.00 USD | 6,230,000.00 USD | 660.12 USD | 5,040.00 USD | 7,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.71` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 0.00 USD | 33,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.72` | 6,210,000.00 USD | 6,210,000.00 USD | 440.78 USD | 0.00 USD | 81.16 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.73` | 6,210,000.00 USD | 6,210,000.00 USD | 4,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.73` | 6,830,000.00 USD | 6,830,000.00 USD | 38,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.74` | 6,210,000.00 USD | 6,210,000.00 USD | 9,310.00 USD | 0.00 USD | 169.01 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.75` | 6,200,000.00 USD | 6,200,000.00 USD | 775.36 USD | 4,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.75` | 6,790,000.00 USD | 6,790,000.00 USD | 976.80 USD | 13,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.75` | 500.12 USD | 239,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.76` | 6,190,000.00 USD | 6,190,000.00 USD | 188.00 USD | 0.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 239,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.77` | 6,190,000.00 USD | 6,190,000.00 USD | 23,890.00 USD | 572.85 USD | 5,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.77` | 6,780,000.00 USD | 6,780,000.00 USD | 20,120.00 USD | 4,900.00 USD | 5,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.78` | 8,670.00 USD | 238,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.78` | 6,160,000.00 USD | 6,160,000.00 USD | 7,400.00 USD | 7,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 1,380.00 USD | 230,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.79` | 6,150,000.00 USD | 6,150,000.00 USD | 8,050.00 USD | 2,910.00 USD | 23.89 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.79` | 6,750,000.00 USD | 6,750,000.00 USD | 42,100.00 USD | 4,540.00 USD | 16,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 4,480.00 USD | 228,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.80` | 6,130,000.00 USD | 6,130,000.00 USD | 9,300.00 USD | 9,380.00 USD | 3,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.80` | 6,380.00 USD | 224,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.81` | 6,110,000.00 USD | 6,110,000.00 USD | 809.15 USD | 728.43 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.81` | 6,680,000.00 USD | 6,680,000.00 USD | 3,970.00 USD | 11,570.00 USD | 915.96 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.82` | 775.80 USD | 218,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.82` | 6,110,000.00 USD | 6,110,000.00 USD | 4,270.00 USD | 2,970.00 USD | 2,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.83` | 2,270.00 USD | 217,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.83` | 6,100,000.00 USD | 6,100,000.00 USD | 27,230.00 USD | 6,330.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.83` | 6,670,000.00 USD | 6,670,000.00 USD | 29,530.00 USD | 2,130.00 USD | 24,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.84` | 6,070,000.00 USD | 6,070,000.00 USD | 1,060.00 USD | 1,800.00 USD | 11.01 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 22,560.00 USD | 215,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.85` | 6,060,000.00 USD | 6,060,000.00 USD | 5,210.00 USD | 1,250.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.85` | 6,610,000.00 USD | 6,610,000.00 USD | 17,330.00 USD | 7,840.00 USD | 12,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.86` | 6,050,000.00 USD | 6,050,000.00 USD | 5,060.00 USD | 6,690.00 USD | 18,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.87` | 233.83 USD | 192,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.87` | 6,020,000.00 USD | 6,020,000.00 USD | 13,690.00 USD | 10,860.00 USD | 23,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.87` | 6,570,000.00 USD | 6,570,000.00 USD | 150,960.00 USD | 1,540.00 USD | 21,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 192,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.88` | 5,970,000.00 USD | 5,970,000.00 USD | 161,620.00 USD | 5,890.00 USD | 34,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.89` | 5,770,000.00 USD | 5,770,000.00 USD | 60,180.00 USD | 4,950.00 USD | 27,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.89` | 6,400,000.00 USD | 6,400,000.00 USD | 149,100.00 USD | 18,320.00 USD | 24,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.89` | 15,880.00 USD | 191,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.90` | 5,680,000.00 USD | 5,680,000.00 USD | 59,500.00 USD | 6,970.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 2,360.00 USD | 175,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.91` | 5,610,000.00 USD | 5,610,000.00 USD | 14,100.00 USD | 10,370.00 USD | 28,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.91` | 6,210,000.00 USD | 6,210,000.00 USD | 31,740.00 USD | 26,330.00 USD | 44,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.92` | 5,550,000.00 USD | 5,550,000.00 USD | 15,980.00 USD | 2,950.00 USD | 8,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 4,600.00 USD | 173,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.93` | 5,530,000.00 USD | 5,530,000.00 USD | 7,960.00 USD | 6,570.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.93` | 6,100,000.00 USD | 6,100,000.00 USD | 78,470.00 USD | 7,330.00 USD | 15,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 16,340.00 USD | 168,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 5,510,000.00 USD | 5,510,000.00 USD | 17,720.00 USD | 20,510.00 USD | 61,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 127,110.00 USD | 152,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 5,410,000.00 USD | 5,410,000.00 USD | 27,800.00 USD | 9,190.00 USD | 86,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.95` | 6,000,000.00 USD | 6,000,000.00 USD | 43,890.00 USD | 9,500.00 USD | 102,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.96` | 5,280,000.00 USD | 5,280,000.00 USD | 2,760.00 USD | 15,680.00 USD | 62,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.97` | 5,200,000.00 USD | 5,200,000.00 USD | 12,860.00 USD | 9,820.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.97` | 5,850,000.00 USD | 5,850,000.00 USD | 37,150.00 USD | 18,700.00 USD | 40,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.97` | 1,580.00 USD | 25,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.98` | 5,180,000.00 USD | 5,180,000.00 USD | 5,050.00 USD | 2,060.00 USD | 42,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,600.00 USD | 23,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 5,130,000.00 USD | 5,130,000.00 USD | 3,230.00 USD | 10,180.00 USD | 4,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.99` | 5,750,000.00 USD | 5,750,000.00 USD | 51,690.00 USD | 20,640.00 USD | 121,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 210.99 USD | 22,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 5,110,000.00 USD | 5,110,000.00 USD | 50,430.00 USD | 8,950.00 USD | 21,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.01` | 5,030,000.00 USD | 5,030,000.00 USD | 6,010.00 USD | 3,750.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.01` | 5,560,000.00 USD | 5,560,000.00 USD | 46,190.00 USD | 17,990.00 USD | 46,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 5,010,000.00 USD | 5,010,000.00 USD | 75,000.00 USD | 0.00 USD | 274.70 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 248.37 USD | 21,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.03` | 4,940,000.00 USD | 4,940,000.00 USD | 8,820.00 USD | 12,540.00 USD | 13,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.03` | 5,450,000.00 USD | 5,450,000.00 USD | 352,180.00 USD | 35,720.00 USD | 47,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.04` | 4,900,000.00 USD | 4,900,000.00 USD | 49,080.00 USD | 0.00 USD | 10,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.05` | 4,840,000.00 USD | 4,840,000.00 USD | 317,540.00 USD | 6,430.00 USD | 53,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.05` | 5,010,000.00 USD | 5,010,000.00 USD | 388,880.00 USD | 0.00 USD | 62,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.06` | 4,470,000.00 USD | 4,470,000.00 USD | 155,240.00 USD | 0.00 USD | 67,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.07` | 4,240,000.00 USD | 4,240,000.00 USD | 130,100.00 USD | 9,310.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.07` | 4,560,000.00 USD | 4,560,000.00 USD | 60,670.00 USD | 0.00 USD | 76,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.07` | 21,710.00 USD | 21,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.08` | 4,100,000.00 USD | 4,100,000.00 USD | 14,440.00 USD | 0.00 USD | 65,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.09` | 4,020,000.00 USD | 4,020,000.00 USD | 3,110.00 USD | 0.00 USD | 29,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.09` | 4,420,000.00 USD | 4,420,000.00 USD | 30,090.00 USD | 0.00 USD | 80,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.10` | 3,990,000.00 USD | 3,990,000.00 USD | 31,110.00 USD | 6,770.00 USD | 122,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.11` | 3,830,000.00 USD | 3,830,000.00 USD | 77,850.00 USD | 0.00 USD | 192,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.11` | 4,310,000.00 USD | 4,310,000.00 USD | 33,000.00 USD | 0.00 USD | 141,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.12` | 3,560,000.00 USD | 3,560,000.00 USD | 7,380.00 USD | 10,020.00 USD | 126,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.13` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 4,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.13` | 4,140,000.00 USD | 4,140,000.00 USD | 25,980.00 USD | 7,420.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.13` | 213.79 USD | 213.79 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.14` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 4,120.00 USD | 96,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.15` | 3,310,000.00 USD | 3,310,000.00 USD | 39,880.00 USD | 11,230.00 USD | 46,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.15` | 4,090,000.00 USD | 4,090,000.00 USD | 179,060.00 USD | 31,560.00 USD | 198,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.16` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 17,890.00 USD | 165,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.17` | 3,030,000.00 USD | 3,030,000.00 USD | 11,100.00 USD | 8,610.00 USD | 183,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.17` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 7,770.00 USD | 157,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.18` | 2,820,000.00 USD | 2,820,000.00 USD | 7,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.19` | 2,820,000.00 USD | 2,820,000.00 USD | 17,640.00 USD | 0.00 USD | 15,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.19` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 75,510.00 USD | 23,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.20` | 2,780,000.00 USD | 2,780,000.00 USD | 25,530.00 USD | 0.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.21` | 2,750,000.00 USD | 2,750,000.00 USD | 33,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.21` | 3,410,000.00 USD | 3,410,000.00 USD | 174,220.00 USD | 22,240.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.22` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.23` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 1,750.00 USD | 47.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.23` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 40,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.24` | 2,700,000.00 USD | 2,700,000.00 USD | 277.44 USD | 1,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.25` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 20,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.25` | 3,170,000.00 USD | 3,170,000.00 USD | 129,670.00 USD | 5,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.26` | 2,670,000.00 USD | 2,670,000.00 USD | 32,580.00 USD | 12,510.00 USD | 23,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.27` | 2,610,000.00 USD | 2,610,000.00 USD | 13,860.00 USD | 5,640.00 USD | 75.54 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.27` | 3,030,000.00 USD | 3,030,000.00 USD | 51,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.28` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 9,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.29` | 2,580,000.00 USD | 2,580,000.00 USD | 14,380.00 USD | 8,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.29` | 2,980,000.00 USD | 2,980,000.00 USD | 166,800.00 USD | 0.00 USD | 270.17 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.30` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 4,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.31` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 39,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.31` | 2,820,000.00 USD | 2,820,000.00 USD | 257,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.32` | 2,510,000.00 USD | 2,510,000.00 USD | 66,820.00 USD | 4,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.33` | 2,560,000.00 USD | 2,560,000.00 USD | 14,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.34` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 2,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.35` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 16,880.00 USD | 16,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.35` | 2,540,000.00 USD | 2,540,000.00 USD | 223,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.36` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 17,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.37` | 2,390,000.00 USD | 2,390,000.00 USD | 691.75 USD | 6,430.00 USD | 33.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.37` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 36,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.38` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 3,420.00 USD | 50,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.39` | 2,330,000.00 USD | 2,330,000.00 USD | 100,740.00 USD | 13,620.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.39` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 7,600.00 USD | 70,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.40` | 2,180,000.00 USD | 2,180,000.00 USD | 10,500.00 USD | 7,000.00 USD | 51,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.41` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 2,050.00 USD | 82.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.41` | 2,200,000.00 USD | 2,200,000.00 USD | 194,850.00 USD | 0.00 USD | 57,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.42` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 6,250.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.43` | 2,090,000.00 USD | 2,090,000.00 USD | 45,340.00 USD | 7,730.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.43` | 1,950,000.00 USD | 1,950,000.00 USD | 22,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.44` | 2,030,000.00 USD | 2,030,000.00 USD | 11,130.00 USD | 19,130.00 USD | 120,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.45` | 1,880,000.00 USD | 1,880,000.00 USD | 54,790.00 USD | 0.00 USD | 163,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.45` | 1,930,000.00 USD | 1,930,000.00 USD | 156,410.00 USD | 0.00 USD | 119,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.46` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 124,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.47` | 1,540,000.00 USD | 1,540,000.00 USD | 663.00 USD | 0.00 USD | 135.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.47` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 813.38 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.48` | 1,540,000.00 USD | 1,540,000.00 USD | 749.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.49` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 12.70 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.49` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 81,010.00 USD | 152,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.50` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 68,460.00 USD | 127,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.51` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 21,730.00 USD | 172,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.51` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 129,490.00 USD | 91,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.52` | 1,150,000.00 USD | 1,150,000.00 USD | 183,950.00 USD | 25,890.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.53` | 933,330.00 USD | 933,330.00 USD | 33,590.00 USD | 32,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.53` | 1,200,000.00 USD | 1,200,000.00 USD | 176,360.00 USD | 144,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.54` | 867,210.00 USD | 867,210.00 USD | 202,800.00 USD | 3,210.00 USD | 217.56 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.55` | 660,980.00 USD | 660,980.00 USD | 152,290.00 USD | 1,710.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.55` | 877,050.00 USD | 877,050.00 USD | 441,870.00 USD | 158,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.55` | 3,220.00 USD | 3,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.56` | 481,860.00 USD | 481,860.00 USD | 139,040.00 USD | 38,320.00 USD | 110.62 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.57` | 304,390.00 USD | 304,390.00 USD | 181,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.57` | 276,500.00 USD | 276,500.00 USD | 9,740.00 USD | 115,860.00 USD | 26,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.58` | 122,730.00 USD | 122,730.00 USD | 59,120.00 USD | 5,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.59` | 58,550.00 USD | 58,550.00 USD | 0.00 USD | 27,510.00 USD | 118.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.59` | 124,000.00 USD | 124,000.00 USD | 5,020.00 USD | 118,220.00 USD | 761.26 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.60` | 30,920.00 USD | 30,920.00 USD | 2,040.00 USD | 28,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.61` | 123,480.00 USD | 123,480.00 USD | 497.00 USD | 41,300.00 USD | 81,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.61` | 246,970.00 USD | 246,970.00 USD | 497.00 USD | 41,300.00 USD | 81,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.61` | 101,060.00 USD | 101,060.00 USD | 2,810.00 USD | 35,810.00 USD | 62,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.61` | 202,120.00 USD | 202,120.00 USD | 2,810.00 USD | 35,810.00 USD | 62,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.62` | 435,370.00 USD | 435,370.00 USD | 41,980.00 USD | 26,090.00 USD | 120,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.63` | 580,420.00 USD | 580,420.00 USD | 104,180.00 USD | 39,780.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.63` | 255,240.00 USD | 255,240.00 USD | 0.00 USD | 25,450.00 USD | 27,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.64` | 625,490.00 USD | 625,490.00 USD | 0.00 USD | 6,540.00 USD | 38,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.65` | 731,630.00 USD | 731,630.00 USD | 3,580.00 USD | 6,810.00 USD | 95,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.65` | 552,750.00 USD | 552,750.00 USD | 191,350.00 USD | 29,750.00 USD | 76,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.66` | 987,380.00 USD | 987,380.00 USD | 145,440.00 USD | 31,810.00 USD | 78,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.67` | 1,190,000.00 USD | 1,190,000.00 USD | 6,430.00 USD | 3,750.00 USD | 190,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.67` | 874,560.00 USD | 874,560.00 USD | 77,920.00 USD | 24,870.00 USD | 219,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.68` | 1,290,000.00 USD | 1,290,000.00 USD | 68,460.00 USD | 12,020.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.69` | 209.31 USD | 3,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.69` | 1,360,000.00 USD | 1,360,000.00 USD | 10,820.00 USD | 16,260.00 USD | 33,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.69` | 1,240,000.00 USD | 1,240,000.00 USD | 158,430.00 USD | 48,960.00 USD | 162,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.70` | 1,440,000.00 USD | 1,440,000.00 USD | 62,600.00 USD | 0.00 USD | 23,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.71` | 1,460,000.00 USD | 1,460,000.00 USD | 18,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.71` | 1,340,000.00 USD | 1,340,000.00 USD | 87,110.00 USD | 11,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.72` | 1,530,000.00 USD | 1,530,000.00 USD | 16,840.00 USD | 0.00 USD | 50,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.72` | 145.62 USD | 3,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.73` | 1,600,000.00 USD | 1,600,000.00 USD | 12,580.00 USD | 28,810.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.73` | 1,410,000.00 USD | 1,410,000.00 USD | 51,030.00 USD | 10,790.00 USD | 570.66 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.74` | 1,660,000.00 USD | 1,660,000.00 USD | 38,500.00 USD | 3,500.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.75` | 1,700,000.00 USD | 1,700,000.00 USD | 33,520.00 USD | 4,580.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.75` | 1,620,000.00 USD | 1,620,000.00 USD | 196,960.00 USD | 19,690.00 USD | 754.30 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.76` | 1,800,000.00 USD | 1,800,000.00 USD | 82,470.00 USD | 0.00 USD | 21,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.77` | 1,970,000.00 USD | 1,970,000.00 USD | 119,730.00 USD | 2,060.00 USD | 43,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.77` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 82,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.78` | 2,030,000.00 USD | 2,030,000.00 USD | 41,500.00 USD | 12,260.00 USD | 9,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.79` | 2,110,000.00 USD | 2,110,000.00 USD | 31,710.00 USD | 12,000.00 USD | 29,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.79` | 1,770,000.00 USD | 1,770,000.00 USD | 29,660.00 USD | 25,300.00 USD | 13,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.80` | 2,240,000.00 USD | 2,240,000.00 USD | 100,610.00 USD | 14,490.00 USD | 24,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.80` | 858.75 USD | 4,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.81` | 2,270,000.00 USD | 2,270,000.00 USD | 18,670.00 USD | 2,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.81` | 1,900,000.00 USD | 1,900,000.00 USD | 102,790.00 USD | 8,450.00 USD | 18,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.82` | 2,290,000.00 USD | 2,290,000.00 USD | 2,200.00 USD | 0.00 USD | 19,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.82` | 6,000.00 USD | 10,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.83` | 2,370,000.00 USD | 2,370,000.00 USD | 73,290.00 USD | 12,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.83` | 2,000,000.00 USD | 2,000,000.00 USD | 98,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.84` | 2,450,000.00 USD | 2,450,000.00 USD | 1,500.00 USD | 0.00 USD | 73,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.85` | 2,480,000.00 USD | 2,480,000.00 USD | 13,040.00 USD | 3,360.00 USD | 10,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.85` | 2,090,000.00 USD | 2,090,000.00 USD | 29,310.00 USD | 0.00 USD | 58,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 2,480,000.00 USD | 2,480,000.00 USD | 1,910.00 USD | 0.00 USD | 443.71 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.87` | 2,490,000.00 USD | 2,490,000.00 USD | 1,350.00 USD | 0.00 USD | 9,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.87` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 23,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.88` | 2,500,000.00 USD | 2,500,000.00 USD | 803.70 USD | 10,670.00 USD | 427.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.89` | 2,540,000.00 USD | 2,540,000.00 USD | 3,660.00 USD | 2,150.00 USD | 32,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.89` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 73,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.90` | 2,670,000.00 USD | 2,670,000.00 USD | 28,580.00 USD | 5,990.00 USD | 96,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.91` | 2,730,000.00 USD | 2,730,000.00 USD | 32,240.00 USD | 11,620.00 USD | 13,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.91` | 2,280,000.00 USD | 2,280,000.00 USD | 2,440.00 USD | 0.00 USD | 89,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 2,730,000.00 USD | 2,730,000.00 USD | 1,110.00 USD | 1,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.93` | 2,780,000.00 USD | 2,780,000.00 USD | 31,830.00 USD | 1,810.00 USD | 21,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.93` | 2,440,000.00 USD | 2,440,000.00 USD | 157,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.94` | 2,830,000.00 USD | 2,830,000.00 USD | 32,580.00 USD | 12,260.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.95` | 2,840,000.00 USD | 2,840,000.00 USD | 2,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.95` | 2,440,000.00 USD | 2,440,000.00 USD | 1,390.00 USD | 0.00 USD | 432.56 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.96` | 2,840,000.00 USD | 2,840,000.00 USD | 978.04 USD | 0.00 USD | 404.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.97` | 2,440,000.00 USD | 2,440,000.00 USD | 1,930.00 USD | 0.00 USD | 791.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.98` | 2,900,000.00 USD | 2,900,000.00 USD | 35,320.00 USD | 7,700.00 USD | 19,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 2,980,000.00 USD | 2,980,000.00 USD | 48,100.00 USD | 24,940.00 USD | 3,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.99` | 2,600,000.00 USD | 2,600,000.00 USD | 144,700.00 USD | 0.00 USD | 9,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.99` | 539,710.00 USD | 550,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.00` | 3,020,000.00 USD | 3,020,000.00 USD | 36,960.00 USD | 0.00 USD | 8,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 3,050,000.00 USD | 3,050,000.00 USD | 1,460.00 USD | 12,030.00 USD | 16,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.01` | 2,880,000.00 USD | 2,880,000.00 USD | 230,880.00 USD | 36,180.00 USD | 21,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 3,130,000.00 USD | 3,130,000.00 USD | 38,930.00 USD | 33,630.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 3,300,000.00 USD | 3,300,000.00 USD | 125,760.00 USD | 14,810.00 USD | 34,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.03` | 3,110,000.00 USD | 3,110,000.00 USD | 104,960.00 USD | 101,140.00 USD | 15,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 3,380,000.00 USD | 3,380,000.00 USD | 40,880.00 USD | 10,710.00 USD | 21,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 3,440,000.00 USD | 3,440,000.00 USD | 21,500.00 USD | 13,500.00 USD | 29,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.05` | 3,200,000.00 USD | 3,200,000.00 USD | 37,540.00 USD | 17,700.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.06` | 3,490,000.00 USD | 3,490,000.00 USD | 27,800.00 USD | 6,890.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.07` | 3,550,000.00 USD | 3,550,000.00 USD | 13,580.00 USD | 18,880.00 USD | 30,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.07` | 3,260,000.00 USD | 3,260,000.00 USD | 3,990.00 USD | 14,140.00 USD | 36,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 3,610,000.00 USD | 3,610,000.00 USD | 13,510.00 USD | 3,370.00 USD | 39,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 3,740,000.00 USD | 3,740,000.00 USD | 88,250.00 USD | 11,440.00 USD | 31,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.09` | 3,560,000.00 USD | 3,560,000.00 USD | 150,640.00 USD | 8,680.00 USD | 144,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.10` | 3,810,000.00 USD | 3,810,000.00 USD | 16,220.00 USD | 16,280.00 USD | 37,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.11` | 3,970,000.00 USD | 3,970,000.00 USD | 61,080.00 USD | 15,740.00 USD | 82,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.11` | 5,040,000.00 USD | 5,040,000.00 USD | 877,120.00 USD | 37,620.00 USD | 570,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 4,120,000.00 USD | 4,120,000.00 USD | 102,100.00 USD | 25,490.00 USD | 26,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 4,260,000.00 USD | 4,260,000.00 USD | 83,710.00 USD | 17,230.00 USD | 40,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.13` | 6,220,000.00 USD | 6,220,000.00 USD | 666,000.00 USD | 26,540.00 USD | 484,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.14` | 4,330,000.00 USD | 4,330,000.00 USD | 30,520.00 USD | 3,380.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.15` | 4,430,000.00 USD | 4,430,000.00 USD | 56,750.00 USD | 23,170.00 USD | 23,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.15` | 6,890,000.00 USD | 6,890,000.00 USD | 357,020.00 USD | 38,700.00 USD | 270,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 4,550,000.00 USD | 4,550,000.00 USD | 63,930.00 USD | 23,900.00 USD | 32,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 4,680,000.00 USD | 4,680,000.00 USD | 80,480.00 USD | 3,200.00 USD | 49,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.17` | 7,730,000.00 USD | 7,730,000.00 USD | 408,450.00 USD | 133,490.00 USD | 302,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 4,770,000.00 USD | 4,770,000.00 USD | 28,620.00 USD | 26,430.00 USD | 31,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.19` | 1,590.00 USD | 551,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.19` | 4,880,000.00 USD | 4,880,000.00 USD | 77,850.00 USD | 29,140.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.19` | 8,540,000.00 USD | 8,540,000.00 USD | 503,250.00 USD | 108,440.00 USD | 193,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.20` | 5,000,000.00 USD | 5,000,000.00 USD | 64,620.00 USD | 11,090.00 USD | 37,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 5,040,000.00 USD | 5,040,000.00 USD | 30,610.00 USD | 2,950.00 USD | 4,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.21` | 9,550,000.00 USD | 9,550,000.00 USD | 590,780.00 USD | 144,470.00 USD | 278,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.21` | 1,870.00 USD | 553,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.22` | 5,110,000.00 USD | 5,110,000.00 USD | 58,850.00 USD | 2,850.00 USD | 11,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.23` | 5,110,000.00 USD | 5,110,000.00 USD | 883.09 USD | 4,270.00 USD | 17.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.23` | 10,600,000.00 USD | 10,600,000.00 USD | 582,450.00 USD | 92,780.00 USD | 369,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 5,160,000.00 USD | 5,160,000.00 USD | 45,960.00 USD | 0.00 USD | 3,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 5,200,000.00 USD | 5,200,000.00 USD | 17,320.00 USD | 5,840.00 USD | 9,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.25` | 11,090,000.00 USD | 11,090,000.00 USD | 277,290.00 USD | 73,690.00 USD | 141,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 5,200,000.00 USD | 5,200,000.00 USD | 1,260.00 USD | 0.00 USD | 3,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 5,230,000.00 USD | 5,230,000.00 USD | 23,580.00 USD | 1,360.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.27` | 11,420,000.00 USD | 11,420,000.00 USD | 156,190.00 USD | 118,550.00 USD | 55,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 5,240,000.00 USD | 5,240,000.00 USD | 1,530.00 USD | 8,760.00 USD | 94.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.29` | 5,280,000.00 USD | 5,280,000.00 USD | 16,190.00 USD | 4,140.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.29` | 12,280,000.00 USD | 12,280,000.00 USD | 468,150.00 USD | 100,200.00 USD | 291,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.30` | 5,340,000.00 USD | 5,340,000.00 USD | 39,850.00 USD | 7,520.00 USD | 11,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 5,380,000.00 USD | 5,380,000.00 USD | 27,750.00 USD | 5,020.00 USD | 12,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.31` | 12,920,000.00 USD | 12,920,000.00 USD | 307,520.00 USD | 55,090.00 USD | 273,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 5,400,000.00 USD | 5,400,000.00 USD | 9,610.00 USD | 0.00 USD | 4,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 5,420,000.00 USD | 5,420,000.00 USD | 7,990.00 USD | 6,000.00 USD | 8,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.33` | 13,320,000.00 USD | 13,320,000.00 USD | 163,740.00 USD | 64,710.00 USD | 180,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 5,470,000.00 USD | 5,470,000.00 USD | 46,210.00 USD | 3,660.00 USD | 3,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.35` | 5,500,000.00 USD | 5,500,000.00 USD | 13,620.00 USD | 0.00 USD | 15,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.35` | 13,800,000.00 USD | 13,800,000.00 USD | 289,480.00 USD | 88,340.00 USD | 98,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 5,520,000.00 USD | 5,520,000.00 USD | 5,400.00 USD | 6,760.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 5,540,000.00 USD | 5,540,000.00 USD | 12,900.00 USD | 5,670.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.37` | 14,220,000.00 USD | 14,220,000.00 USD | 304,360.00 USD | 34,660.00 USD | 84,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 5,570,000.00 USD | 5,570,000.00 USD | 15,140.00 USD | 0.00 USD | 13,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.39` | 5,580,000.00 USD | 5,580,000.00 USD | 9,080.00 USD | 0.00 USD | 12.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.39` | 14,550,000.00 USD | 14,550,000.00 USD | 206,980.00 USD | 32,960.00 USD | 85,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.40` | 5,600,000.00 USD | 5,600,000.00 USD | 22,270.00 USD | 0.00 USD | 24.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.41` | 5,620,000.00 USD | 5,620,000.00 USD | 963.73 USD | 0.00 USD | 10,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.41` | 14,970,000.00 USD | 14,970,000.00 USD | 265,320.00 USD | 30,790.00 USD | 119,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 440.06 USD | 554,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 5,630,000.00 USD | 5,630,000.00 USD | 9,100.00 USD | 2,390.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.43` | 5,640,000.00 USD | 5,640,000.00 USD | 5,380.00 USD | 700.38 USD | 20.54 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.43` | 15,100,000.00 USD | 15,100,000.00 USD | 33,890.00 USD | 19,300.00 USD | 81,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 5,640,000.00 USD | 5,640,000.00 USD | 534.79 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.45` | 15,200,000.00 USD | 15,200,000.00 USD | 67,880.00 USD | 16,970.00 USD | 12,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.46` | 5,650,000.00 USD | 5,650,000.00 USD | 9,070.00 USD | 0.00 USD | 110.62 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.46` | 138.85 USD | 554,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.47` | 5,650,000.00 USD | 5,650,000.00 USD | 1,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.47` | 15,290,000.00 USD | 15,290,000.00 USD | 53,420.00 USD | 14,840.00 USD | 25,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.48` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.49` | 5,680,000.00 USD | 5,680,000.00 USD | 20,610.00 USD | 572.85 USD | 5,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.49` | 15,340,000.00 USD | 15,340,000.00 USD | 26,920.00 USD | 10,200.00 USD | 15,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.50` | 5,690,000.00 USD | 5,690,000.00 USD | 4,500.00 USD | 930.34 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.51` | 15,520,000.00 USD | 15,520,000.00 USD | 71,980.00 USD | 23,250.00 USD | 84,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.53` | 15,640,000.00 USD | 15,640,000.00 USD | 96,550.00 USD | 15,360.00 USD | 6,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.55` | 15,690,000.00 USD | 15,690,000.00 USD | 28,850.00 USD | 17,400.00 USD | 534.24 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.57` | 15,800,000.00 USD | 15,800,000.00 USD | 81,570.00 USD | 2,130.00 USD | 24,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.59` | 15,850,000.00 USD | 15,850,000.00 USD | 26,920.00 USD | 7,840.00 USD | 14,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.61` | 15,920,000.00 USD | 15,920,000.00 USD | 48,040.00 USD | 1,540.00 USD | 23,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.62` | 138.98 USD | 554,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.63` | 15,950,000.00 USD | 15,950,000.00 USD | 16,170.00 USD | 4,500.00 USD | 6,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.64` | 1,930.00 USD | 556,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.65` | 16,010,000.00 USD | 16,010,000.00 USD | 31,780.00 USD | 13,820.00 USD | 18,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.67` | 16,070,000.00 USD | 16,070,000.00 USD | 31,000.00 USD | 11,120.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.69` | 16,170,000.00 USD | 16,170,000.00 USD | 80,910.00 USD | 7,330.00 USD | 15,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.71` | 16,270,000.00 USD | 16,270,000.00 USD | 44,510.00 USD | 9,500.00 USD | 42,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.73` | 16,290,000.00 USD | 16,290,000.00 USD | 3,060.00 USD | 3,160.00 USD | 10,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 556,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.75` | 16,370,000.00 USD | 16,370,000.00 USD | 34,630.00 USD | 15,540.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.77` | 16,470,000.00 USD | 16,470,000.00 USD | 50,040.00 USD | 7,410.00 USD | 46,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.79` | 16,540,000.00 USD | 16,540,000.00 USD | 47,490.00 USD | 17,990.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.81` | 16,710,000.00 USD | 16,710,000.00 USD | 102,900.00 USD | 23,930.00 USD | 47,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.83` | 16,860,000.00 USD | 16,860,000.00 USD | 54,150.00 USD | 29,270.00 USD | 62,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.85` | 16,980,000.00 USD | 16,980,000.00 USD | 70,400.00 USD | 2,210.00 USD | 49,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.35` | 2,650.00 USD | 559,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 559,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.60` | 21,190.00 USD | 581,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.65` | 255.29 USD | 581,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.81` | 1,150.00 USD | 582,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.89` | 100.13 USD | 582,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.90` | 306.98 USD | 582,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 589,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.07` | 55,380.00 USD | 645,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 124,320.00 USD | 769,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.56` | 4,350.00 USD | 773,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 785,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.69` | 296,760.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.80` | 114.27 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.93` | 505.74 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.95` | 1,050.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.84` | 63,020.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.48` | 285.79 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 1,350.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.07` | 247.38 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.21` | 4,220.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.38` | 20,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.40` | 331.98 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.72` | 167.79 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.77` | 185.55 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.82` | 1,700.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.38` | 265,410.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.45` | 23,260.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.50` | 24,080.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.59` | 109.53 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.64` | 118.27 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.98` | 1,690.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.00` | 1,940.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.02` | 191.87 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.04` | 85,820.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.05` | 207.78 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.07` | 6,740.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.84` | 2,290,000.00 USD | 0.00 USD | 212.18 USD | `-78.40%` | `115.00` |
| `Live` | `Long` | `1.92` | 2,290,000.00 USD | 0.00 USD | 212.20 USD | `-77.58%` | `110.81` |
| `Live` | `Long` | `2.00` | 2,290,000.00 USD | 0.00 USD | 160.40 USD | `-76.52%` | `80.00` |
| `Live` | `Long` | `2.04` | 2,290,000.00 USD | 0.00 USD | 110.52 USD | `-76.17%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,290,000.00 USD | 0.00 USD | 4,920.00 USD | `-75.82%` | `2,382.76` |
| `Live` | `Long` | `2.10` | 2,280,000.00 USD | 0.00 USD | 8,580.00 USD | `-75.47%` | `4,096.48` |
| `Live` | `Long` | `2.12` | 2,270,000.00 USD | 0.00 USD | 244.38 USD | `-75.12%` | `115.00` |
| `Live` | `Long` | `2.19` | 2,270,000.00 USD | 0.00 USD | 109.60 USD | `-74.41%` | `50.16` |
| `Live` | `Long` | `2.21` | 2,270,000.00 USD | 0.00 USD | 254.72 USD | `-74.06%` | `115.00` |
| `Live` | `Long` | `2.35` | 2,270,000.00 USD | 0.00 USD | 110.07 USD | `-72.54%` | `46.94` |
| `Live` | `Long` | `2.67` | 2,270,000.00 USD | 0.00 USD | 138.58 USD | `-68.79%` | `52.00` |
| `Live` | `Long` | `2.69` | 2,270,000.00 USD | 0.00 USD | 942.44 USD | `-68.56%` | `351.00` |
| `Live` | `Long` | `2.79` | 2,270,000.00 USD | 0.00 USD | 320.28 USD | `-67.39%` | `115.00` |
| `Live` | `Long` | `2.87` | 2,270,000.00 USD | 0.00 USD | 232.67 USD | `-66.45%` | `81.21` |
| `Live` | `Long` | `2.88` | 2,270,000.00 USD | 0.00 USD | 20,100.00 USD | `-66.33%` | `6,990.57` |
| `Live` | `Long` | `2.94` | 2,250,000.00 USD | 0.00 USD | 44,510.00 USD | `-65.63%` | `15,165.76` |
| `Live` | `Long` | `2.98` | 2,210,000.00 USD | 0.00 USD | 111.12 USD | `-65.16%` | `37.35` |
| `Live` | `Long` | `3.15` | 2,210,000.00 USD | 0.00 USD | 23,550.00 USD | `-63.06%` | `7,465.11` |
| `Live` | `Long` | `3.29` | 2,180,000.00 USD | 0.00 USD | 1,320.00 USD | `-61.42%` | `400.00` |
| `Live` | `Long` | `3.33` | 2,180,000.00 USD | 0.00 USD | 1,260.00 USD | `-60.95%` | `377.71` |
| `Live` | `Long` | `3.37` | 2,180,000.00 USD | 0.00 USD | 389.53 USD | `-60.60%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,180,000.00 USD | 0.00 USD | 151.88 USD | `-60.48%` | `45.00` |
| `Live` | `Long` | `3.54` | 2,180,000.00 USD | 0.00 USD | 392.22 USD | `-58.49%` | `110.64` |
| `Live` | `Long` | `3.58` | 2,180,000.00 USD | 0.00 USD | 582.15 USD | `-58.14%` | `162.84` |
| `Live` | `Long` | `3.67` | 2,180,000.00 USD | 0.00 USD | 109.95 USD | `-57.08%` | `30.00` |
| `Live` | `Long` | `3.75` | 2,180,000.00 USD | 0.00 USD | 9,010.00 USD | `-56.03%` | `2,400.00` |
| `Live` | `Long` | `3.90` | 2,170,000.00 USD | 0.00 USD | 131.73 USD | `-54.39%` | `33.82` |
| `Live` | `Long` | `3.96` | 2,170,000.00 USD | 0.00 USD | 2,640.00 USD | `-53.57%` | `666.20` |
| `Live` | `Long` | `4.03` | 2,170,000.00 USD | 0.00 USD | 402.70 USD | `-52.87%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,170,000.00 USD | 0.00 USD | 152.29 USD | `-52.63%` | `37.65` |
| `Live` | `Long` | `4.14` | 2,170,000.00 USD | 0.00 USD | 159.29 USD | `-51.46%` | `38.43` |
| `Live` | `Long` | `4.21` | 2,170,000.00 USD | 0.00 USD | 195.03 USD | `-50.64%` | `46.27` |
| `Live` | `Long` | `4.24` | 2,170,000.00 USD | 0.00 USD | 564.61 USD | `-50.41%` | `133.32` |
| `Live` | `Long` | `4.45` | 2,170,000.00 USD | 0.00 USD | 110.77 USD | `-47.95%` | `24.92` |
| `Live` | `Long` | `4.49` | 2,170,000.00 USD | 0.00 USD | 285.92 USD | `-47.48%` | `63.75` |
| `Live` | `Long` | `4.59` | 2,170,000.00 USD | 0.00 USD | 30,970.00 USD | `-46.19%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,130,000.00 USD | 0.00 USD | 486.93 USD | `-45.96%` | `105.51` |
| `Live` | `Long` | `4.62` | 2,130,000.00 USD | 0.00 USD | 2,930.00 USD | `-45.84%` | `634.06` |
| `Live` | `Long` | `4.66` | 2,130,000.00 USD | 0.00 USD | 587.97 USD | `-45.49%` | `126.31` |
| `Live` | `Long` | `4.67` | 2,130,000.00 USD | 0.00 USD | 3,280.00 USD | `-45.37%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,130,000.00 USD | 0.00 USD | 1,490.00 USD | `-45.26%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,130,000.00 USD | 0.00 USD | 8,380.00 USD | `-45.14%` | `1,787.97` |
| `Live` | `Long` | `4.70` | 2,120,000.00 USD | 0.00 USD | 7,040.00 USD | `-45.02%` | `1,500.00` |
| `Live` | `Long` | `4.71` | 2,110,000.00 USD | 0.00 USD | 202.64 USD | `-44.91%` | `43.07` |
| `Live` | `Long` | `4.76` | 2,110,000.00 USD | 0.00 USD | 105.64 USD | `-44.20%` | `22.17` |
| `Live` | `Long` | `4.83` | 2,110,000.00 USD | 0.00 USD | 467.01 USD | `-43.38%` | `96.59` |
| `Live` | `Long` | `4.91` | 2,110,000.00 USD | 0.00 USD | 3,880.00 USD | `-42.56%` | `790.61` |
| `Live` | `Long` | `4.92` | 2,110,000.00 USD | 0.00 USD | 1,230.00 USD | `-42.45%` | `251.00` |
| `Live` | `Long` | `4.92` | 2,100,000.00 USD | 0.00 USD | 16,180.00 USD | `-42.33%` | `3,286.00` |
| `Live` | `Long` | `4.95` | 2,090,000.00 USD | 0.00 USD | 352.68 USD | `-42.10%` | `71.32` |
| `Live` | `Long` | `4.96` | 2,090,000.00 USD | 0.00 USD | 945.36 USD | `-41.98%` | `190.79` |
| `Live` | `Long` | `4.96` | 2,090,000.00 USD | 0.00 USD | 4,090.00 USD | `-41.86%` | `824.62` |
| `Live` | `Long` | `4.97` | 2,080,000.00 USD | 0.00 USD | 282.23 USD | `-41.74%` | `56.73` |
| `Live` | `Long` | `4.99` | 2,080,000.00 USD | 0.00 USD | 1,280.00 USD | `-41.63%` | `255.98` |
| `Live` | `Long` | `5.00` | 2,080,000.00 USD | 0.00 USD | 2,770.00 USD | `-41.51%` | `553.96` |
| `Live` | `Long` | `5.01` | 2,080,000.00 USD | 0.00 USD | 56,390.00 USD | `-41.28%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,020,000.00 USD | 0.00 USD | 167.78 USD | `-41.16%` | `33.39` |
| `Live` | `Long` | `5.04` | 2,020,000.00 USD | 0.00 USD | 314.59 USD | `-41.04%` | `62.48` |
| `Live` | `Long` | `5.05` | 2,020,000.00 USD | 0.00 USD | 504.74 USD | `-40.81%` | `99.85` |
| `Live` | `Long` | `5.08` | 2,020,000.00 USD | 0.00 USD | 213.20 USD | `-40.57%` | `42.01` |
| `Live` | `Long` | `5.08` | 2,020,000.00 USD | 0.00 USD | 223.43 USD | `-40.46%` | `43.94` |
| `Live` | `Long` | `5.09` | 2,020,000.00 USD | 0.00 USD | 651.75 USD | `-40.34%` | `127.92` |
| `Live` | `Long` | `5.12` | 2,020,000.00 USD | 0.00 USD | 915.43 USD | `-40.10%` | `178.97` |
| `Live` | `Long` | `5.12` | 2,020,000.00 USD | 0.00 USD | 250.20 USD | `-39.99%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,020,000.00 USD | 0.00 USD | 396.06 USD | `-39.87%` | `77.13` |
| `Live` | `Long` | `5.17` | 2,020,000.00 USD | 0.00 USD | 726.25 USD | `-39.52%` | `140.61` |
| `Live` | `Long` | `5.17` | 2,020,000.00 USD | 0.00 USD | 1,620.00 USD | `-39.40%` | `312.94` |
| `Live` | `Long` | `5.18` | 2,020,000.00 USD | 0.00 USD | 150.57 USD | `-39.29%` | `29.04` |
| `Live` | `Long` | `5.20` | 2,020,000.00 USD | 0.00 USD | 601.94 USD | `-39.17%` | `115.87` |
| `Live` | `Long` | `5.21` | 2,010,000.00 USD | 0.00 USD | 5,480.00 USD | `-39.05%` | `1,053.00` |
| `Live` | `Long` | `5.21` | 2,010,000.00 USD | 0.00 USD | 300.91 USD | `-38.93%` | `57.70` |
| `Live` | `Long` | `5.25` | 2,010,000.00 USD | 0.00 USD | 503.78 USD | `-38.58%` | `96.05` |
| `Live` | `Long` | `5.25` | 2,010,000.00 USD | 0.00 USD | 1,050.00 USD | `-38.47%` | `200.00` |
| `Live` | `Long` | `5.26` | 2,010,000.00 USD | 0.00 USD | 162,470.00 USD | `-38.35%` | `30,858.74` |
| `Live` | `Long` | `5.29` | 1,850,000.00 USD | 0.00 USD | 640.70 USD | `-38.11%` | `121.23` |
| `Live` | `Long` | `5.32` | 1,840,000.00 USD | 0.00 USD | 232.85 USD | `-37.76%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,840,000.00 USD | 0.00 USD | 716.11 USD | `-37.65%` | `134.48` |
| `Live` | `Long` | `5.39` | 1,840,000.00 USD | 0.00 USD | 660.46 USD | `-36.83%` | `122.42` |
| `Live` | `Long` | `5.41` | 1,840,000.00 USD | 0.00 USD | 1,090.00 USD | `-36.71%` | `200.95` |
| `Live` | `Long` | `5.42` | 1,840,000.00 USD | 0.00 USD | 20,160.00 USD | `-36.59%` | `3,723.69` |
| `Live` | `Long` | `5.42` | 1,820,000.00 USD | 0.00 USD | 160,400.00 USD | `-36.47%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,660,000.00 USD | 0.00 USD | 1,360.00 USD | `-36.36%` | `250.00` |
| `Live` | `Long` | `5.45` | 1,660,000.00 USD | 0.00 USD | 1,470.00 USD | `-36.24%` | `270.00` |
| `Live` | `Long` | `5.46` | 1,660,000.00 USD | 0.00 USD | 264.72 USD | `-36.01%` | `48.44` |
| `Live` | `Long` | `5.47` | 1,660,000.00 USD | 0.00 USD | 1,320.00 USD | `-35.89%` | `240.95` |
| `Live` | `Long` | `5.49` | 1,660,000.00 USD | 0.00 USD | 354.06 USD | `-35.77%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,660,000.00 USD | 0.00 USD | 19,290.00 USD | `-35.65%` | `3,510.41` |
| `Live` | `Long` | `5.51` | 1,640,000.00 USD | 0.00 USD | 367.41 USD | `-35.42%` | `66.62` |
| `Live` | `Long` | `5.54` | 1,640,000.00 USD | 0.00 USD | 557.76 USD | `-35.19%` | `100.77` |
| `Live` | `Long` | `5.54` | 1,640,000.00 USD | 0.00 USD | 2,880.00 USD | `-35.07%` | `519.63` |
| `Live` | `Long` | `5.58` | 1,630,000.00 USD | 0.00 USD | 63,260.00 USD | `-34.72%` | `11,347.58` |
| `Live` | `Long` | `5.58` | 1,570,000.00 USD | 0.00 USD | 269.31 USD | `-34.60%` | `48.22` |
| `Live` | `Long` | `5.59` | 1,570,000.00 USD | 0.00 USD | 34,430.00 USD | `-34.48%` | `6,153.60` |
| `Live` | `Long` | `5.62` | 1,540,000.00 USD | 0.00 USD | 2,810.00 USD | `-34.25%` | `500.00` |
| `Live` | `Long` | `5.63` | 1,530,000.00 USD | 0.00 USD | 468.55 USD | `-34.02%` | `83.15` |
| `Live` | `Long` | `5.71` | 1,530,000.00 USD | 0.00 USD | 147.33 USD | `-33.08%` | `25.78` |
| `Live` | `Long` | `5.72` | 1,530,000.00 USD | 0.00 USD | 2,390.00 USD | `-32.96%` | `417.17` |
| `Live` | `Long` | `5.74` | 1,530,000.00 USD | 0.00 USD | 661.65 USD | `-32.84%` | `115.37` |
| `Live` | `Long` | `5.75` | 1,530,000.00 USD | 0.00 USD | 125.70 USD | `-32.73%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,530,000.00 USD | 0.00 USD | 3,190.00 USD | `-32.61%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,530,000.00 USD | 0.00 USD | 10,850.00 USD | `-32.49%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,510,000.00 USD | 0.00 USD | 801.40 USD | `-32.38%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,510,000.00 USD | 0.00 USD | 1,350.00 USD | `-32.26%` | `233.60` |
| `Live` | `Long` | `5.79` | 1,510,000.00 USD | 0.00 USD | 635.31 USD | `-32.14%` | `109.63` |
| `Live` | `Long` | `5.80` | 1,510,000.00 USD | 0.00 USD | 580.50 USD | `-32.02%` | `100.00` |
| `Live` | `Long` | `5.82` | 1,510,000.00 USD | 0.00 USD | 106.65 USD | `-31.91%` | `18.34` |
| `Live` | `Long` | `5.83` | 1,510,000.00 USD | 0.00 USD | 145.88 USD | `-31.67%` | `25.00` |
| `Live` | `Long` | `5.86` | 1,510,000.00 USD | 0.00 USD | 2,110.00 USD | `-31.44%` | `360.33` |
| `Live` | `Long` | `5.89` | 1,510,000.00 USD | 0.00 USD | 984.70 USD | `-30.97%` | `167.04` |
| `Live` | `Long` | `5.91` | 1,510,000.00 USD | 0.00 USD | 399.18 USD | `-30.85%` | `67.60` |
| `Live` | `Long` | `5.92` | 1,510,000.00 USD | 0.00 USD | 277.35 USD | `-30.74%` | `46.89` |
| `Live` | `Long` | `5.96` | 1,510,000.00 USD | 0.00 USD | 11,720.00 USD | `-30.27%` | `1,968.19` |
| `Live` | `Long` | `5.96` | 1,500,000.00 USD | 0.00 USD | 6,320.00 USD | `-30.15%` | `1,060.32` |
| `Live` | `Long` | `5.97` | 1,490,000.00 USD | 0.00 USD | 585.97 USD | `-30.03%` | `98.07` |
| `Live` | `Long` | `6.00` | 1,490,000.00 USD | 0.00 USD | 341.56 USD | `-29.68%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,490,000.00 USD | 0.00 USD | 446.85 USD | `-29.57%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,490,000.00 USD | 0.00 USD | 331.68 USD | `-29.33%` | `54.96` |
| `Live` | `Long` | `6.04` | 1,490,000.00 USD | 0.00 USD | 105.61 USD | `-29.21%` | `17.47` |
| `Live` | `Long` | `6.05` | 1,490,000.00 USD | 0.00 USD | 1,310.00 USD | `-29.10%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,490,000.00 USD | 0.00 USD | 265.10 USD | `-28.98%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,490,000.00 USD | 0.00 USD | 1,690.00 USD | `-28.86%` | `278.94` |
| `Live` | `Long` | `6.08` | 1,480,000.00 USD | 0.00 USD | 405.14 USD | `-28.75%` | `66.58` |
| `Live` | `Long` | `6.09` | 1,480,000.00 USD | 0.00 USD | 3,130.00 USD | `-28.63%` | `512.81` |
| `Live` | `Long` | `6.12` | 1,480,000.00 USD | 0.00 USD | 1,140.00 USD | `-28.39%` | `185.96` |
| `Live` | `Long` | `6.12` | 1,480,000.00 USD | 0.00 USD | 137.02 USD | `-28.28%` | `22.37` |
| `Live` | `Long` | `6.13` | 1,480,000.00 USD | 0.00 USD | 2,030.00 USD | `-28.16%` | `330.65` |
| `Live` | `Long` | `6.14` | 1,480,000.00 USD | 0.00 USD | 238.61 USD | `-28.04%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,480,000.00 USD | 0.00 USD | 7,810.00 USD | `-27.93%` | `1,268.30` |
| `Live` | `Long` | `6.17` | 1,470,000.00 USD | 0.00 USD | 104.36 USD | `-27.69%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,470,000.00 USD | 0.00 USD | 310.25 USD | `-27.34%` | `50.00` |
| `Live` | `Long` | `6.25` | 1,470,000.00 USD | 0.00 USD | 972.65 USD | `-26.76%` | `155.50` |
| `Live` | `Long` | `6.28` | 1,470,000.00 USD | 0.00 USD | 2,510.00 USD | `-26.52%` | `400.00` |
| `Live` | `Long` | `6.29` | 1,470,000.00 USD | 0.00 USD | 3,890.00 USD | `-26.40%` | `618.63` |
| `Live` | `Long` | `6.33` | 1,460,000.00 USD | 0.00 USD | 1,700.00 USD | `-25.94%` | `269.01` |
| `Live` | `Long` | `6.36` | 1,460,000.00 USD | 0.00 USD | 4,470.00 USD | `-25.58%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,460,000.00 USD | 0.00 USD | 284,770.00 USD | `-25.47%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 1,170,000.00 USD | 0.00 USD | 6,410.00 USD | `-25.35%` | `1,006.23` |
| `Live` | `Long` | `6.38` | 1,160,000.00 USD | 0.00 USD | 357,940.00 USD | `-25.23%` | `56,059.40` |
| `Live` | `Long` | `6.42` | 806,310.00 USD | 0.00 USD | 306.32 USD | `-24.88%` | `47.75` |
| `Live` | `Long` | `6.42` | 806,000.00 USD | 0.00 USD | 484.64 USD | `-24.76%` | `75.43` |
| `Live` | `Long` | `6.43` | 805,510.00 USD | 0.00 USD | 6,780.00 USD | `-24.65%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 798,740.00 USD | 0.00 USD | 1,050.00 USD | `-24.30%` | `162.75` |
| `Live` | `Long` | `6.54` | 797,690.00 USD | 0.00 USD | 852.03 USD | `-23.48%` | `130.38` |
| `Live` | `Long` | `6.54` | 796,830.00 USD | 0.00 USD | 8,970.00 USD | `-23.36%` | `1,370.89` |
| `Live` | `Long` | `6.58` | 787,860.00 USD | 0.00 USD | 1,770.00 USD | `-22.89%` | `269.14` |
| `Live` | `Long` | `6.59` | 786,090.00 USD | 0.00 USD | 1,100.00 USD | `-22.77%` | `166.55` |
| `Live` | `Long` | `6.62` | 784,990.00 USD | 0.00 USD | 2,110.00 USD | `-22.54%` | `318.57` |
| `Live` | `Long` | `6.62` | 782,880.00 USD | 0.00 USD | 364.90 USD | `-22.42%` | `55.08` |
| `Live` | `Long` | `6.63` | 782,520.00 USD | 0.00 USD | 245.89 USD | `-22.31%` | `37.06` |
| `Live` | `Long` | `6.67` | 782,270.00 USD | 0.00 USD | 1,320.00 USD | `-21.84%` | `198.12` |
| `Live` | `Long` | `6.68` | 780,950.00 USD | 0.00 USD | 4,680.00 USD | `-21.72%` | `700.69` |
| `Live` | `Long` | `6.71` | 776,270.00 USD | 0.00 USD | 16,570.00 USD | `-21.49%` | `2,471.72` |
| `Live` | `Long` | `6.71` | 759,690.00 USD | 0.00 USD | 6,180.00 USD | `-21.37%` | `920.74` |
| `Live` | `Long` | `6.75` | 753,510.00 USD | 0.00 USD | 1,330.00 USD | `-21.02%` | `196.95` |
| `Live` | `Long` | `6.78` | 752,180.00 USD | 0.00 USD | 6,780.00 USD | `-20.67%` | `1,000.00` |
| `Live` | `Long` | `6.79` | 745,410.00 USD | 0.00 USD | 21,580.00 USD | `-20.55%` | `3,180.66` |
| `Live` | `Long` | `6.79` | 723,830.00 USD | 0.00 USD | 4,720.00 USD | `-20.43%` | `694.73` |
| `Live` | `Long` | `6.80` | 719,110.00 USD | 0.00 USD | 1,500.00 USD | `-20.32%` | `220.95` |
| `Live` | `Long` | `6.82` | 717,600.00 USD | 0.00 USD | 7,230.00 USD | `-20.20%` | `1,061.04` |
| `Live` | `Long` | `6.83` | 710,370.00 USD | 0.00 USD | 1,140.00 USD | `-20.08%` | `167.75` |
| `Live` | `Long` | `6.87` | 709,230.00 USD | 0.00 USD | 3,710.00 USD | `-19.61%` | `540.58` |
| `Live` | `Long` | `6.88` | 705,520.00 USD | 0.00 USD | 1,580.00 USD | `-19.38%` | `229.18` |
| `Live` | `Long` | `6.92` | 703,940.00 USD | 0.00 USD | 579.62 USD | `-18.91%` | `83.70` |
| `Live` | `Long` | `6.93` | 703,360.00 USD | 0.00 USD | 3,500.00 USD | `-18.79%` | `504.07` |
| `Live` | `Long` | `6.95` | 699,860.00 USD | 0.00 USD | 3,980.00 USD | `-18.68%` | `572.68` |
| `Live` | `Long` | `6.96` | 695,890.00 USD | 0.00 USD | 3,480.00 USD | `-18.56%` | `500.00` |
| `Live` | `Long` | `6.96` | 692,410.00 USD | 0.00 USD | 636.74 USD | `-18.44%` | `91.42` |
| `Live` | `Long` | `6.97` | 691,770.00 USD | 0.00 USD | 128,810.00 USD | `-18.32%` | `18,466.99` |
| `Live` | `Long` | `6.99` | 562,960.00 USD | 0.00 USD | 297.49 USD | `-18.21%` | `42.59` |
| `Live` | `Long` | `7.00` | 562,670.00 USD | 0.00 USD | 746.58 USD | `-18.09%` | `106.73` |
| `Live` | `Long` | `7.00` | 561,920.00 USD | 0.00 USD | 21,040.00 USD | `-17.97%` | `3,003.11` |
| `Live` | `Long` | `7.03` | 540,880.00 USD | 0.00 USD | 1,370.00 USD | `-17.74%` | `194.51` |
| `Live` | `Long` | `7.05` | 539,520.00 USD | 0.00 USD | 354.23 USD | `-17.39%` | `50.21` |
| `Live` | `Long` | `7.07` | 539,160.00 USD | 0.00 USD | 23,600.00 USD | `-17.27%` | `3,340.54` |
| `Live` | `Long` | `7.08` | 515,560.00 USD | 0.00 USD | 7,420.00 USD | `-17.15%` | `1,048.27` |
| `Live` | `Long` | `7.08` | 508,140.00 USD | 0.00 USD | 1,050.00 USD | `-17.04%` | `148.63` |
| `Live` | `Long` | `7.09` | 507,090.00 USD | 0.00 USD | 2,130.00 USD | `-16.92%` | `300.00` |
| `Live` | `Long` | `7.11` | 504,960.00 USD | 0.00 USD | 28,530.00 USD | `-16.80%` | `4,015.35` |
| `Live` | `Long` | `7.12` | 476,430.00 USD | 0.00 USD | 379.66 USD | `-16.69%` | `53.36` |
| `Live` | `Long` | `7.12` | 476,050.00 USD | 0.00 USD | 28,500.00 USD | `-16.57%` | `4,000.00` |
| `Live` | `Long` | `7.13` | 447,550.00 USD | 0.00 USD | 777.50 USD | `-16.45%` | `108.97` |
| `Live` | `Long` | `7.14` | 446,780.00 USD | 0.00 USD | 20,270.00 USD | `-16.33%` | `2,837.00` |
| `Live` | `Long` | `7.17` | 426,510.00 USD | 0.00 USD | 2,380.00 USD | `-15.98%` | `331.12` |
| `Live` | `Long` | `7.18` | 424,130.00 USD | 0.00 USD | 1,440.00 USD | `-15.87%` | `200.00` |
| `Live` | `Long` | `7.21` | 422,690.00 USD | 0.00 USD | 322.94 USD | `-15.51%` | `44.76` |
| `Live` | `Long` | `7.24` | 422,370.00 USD | 0.00 USD | 1,480.00 USD | `-15.28%` | `205.21` |
| `Live` | `Long` | `7.25` | 420,890.00 USD | 0.00 USD | 185.83 USD | `-15.16%` | `25.65` |
| `Live` | `Long` | `7.25` | 420,700.00 USD | 0.00 USD | 21,280.00 USD | `-15.05%` | `2,933.17` |
| `Live` | `Long` | `7.29` | 399,420.00 USD | 0.00 USD | 36,420.00 USD | `-14.69%` | `5,000.00` |
| `Live` | `Long` | `7.29` | 363,000.00 USD | 0.00 USD | 1,680.00 USD | `-14.58%` | `230.97` |
| `Live` | `Long` | `7.32` | 361,310.00 USD | 0.00 USD | 900.18 USD | `-14.34%` | `123.06` |
| `Live` | `Long` | `7.34` | 360,410.00 USD | 0.00 USD | 4,370.00 USD | `-13.99%` | `594.84` |
| `Live` | `Long` | `7.36` | 356,040.00 USD | 0.00 USD | 13,140.00 USD | `-13.87%` | `1,787.05` |
| `Live` | `Long` | `7.37` | 342,900.00 USD | 0.00 USD | 2,940.00 USD | `-13.76%` | `399.15` |
| `Live` | `Long` | `7.38` | 339,960.00 USD | 0.00 USD | 2,130.00 USD | `-13.64%` | `288.75` |
| `Live` | `Long` | `7.38` | 337,830.00 USD | 0.00 USD | 227.97 USD | `-13.52%` | `30.87` |
| `Live` | `Long` | `7.42` | 337,600.00 USD | 0.00 USD | 147.61 USD | `-13.06%` | `19.88` |
| `Live` | `Long` | `7.43` | 337,450.00 USD | 0.00 USD | 2,430.00 USD | `-12.94%` | `327.05` |
| `Live` | `Long` | `7.45` | 335,020.00 USD | 0.00 USD | 2,410.00 USD | `-12.82%` | `324.35` |
| `Live` | `Long` | `7.46` | 332,610.00 USD | 0.00 USD | 10,390.00 USD | `-12.70%` | `1,393.53` |
| `Live` | `Long` | `7.46` | 322,220.00 USD | 0.00 USD | 4,590.00 USD | `-12.59%` | `614.36` |
| `Live` | `Long` | `7.47` | 317,630.00 USD | 0.00 USD | 1,120.00 USD | `-12.47%` | `149.52` |
| `Live` | `Long` | `7.50` | 316,510.00 USD | 0.00 USD | 962.81 USD | `-12.24%` | `128.46` |
| `Live` | `Long` | `7.50` | 315,550.00 USD | 0.00 USD | 421.78 USD | `-12.12%` | `56.20` |
| `Live` | `Long` | `7.51` | 315,130.00 USD | 0.00 USD | 1,710.00 USD | `-12.00%` | `228.21` |
| `Live` | `Long` | `7.53` | 313,410.00 USD | 0.00 USD | 1,570.00 USD | `-11.88%` | `208.52` |
| `Live` | `Long` | `7.54` | 311,840.00 USD | 0.00 USD | 4,210.00 USD | `-11.77%` | `559.01` |
| `Live` | `Long` | `7.55` | 307,630.00 USD | 0.00 USD | 1,930.00 USD | `-11.53%` | `255.00` |
| `Live` | `Long` | `7.57` | 305,710.00 USD | 0.00 USD | 25,060.00 USD | `-11.42%` | `3,312.23` |
| `Live` | `Long` | `7.58` | 280,650.00 USD | 0.00 USD | 118.25 USD | `-11.30%` | `15.61` |
| `Live` | `Long` | `7.59` | 280,530.00 USD | 0.00 USD | 26,390.00 USD | `-11.06%` | `3,474.36` |
| `Live` | `Long` | `7.62` | 254,140.00 USD | 0.00 USD | 754.04 USD | `-10.83%` | `99.02` |
| `Live` | `Long` | `7.62` | 253,390.00 USD | 0.00 USD | 787.51 USD | `-10.71%` | `103.28` |
| `Live` | `Long` | `7.63` | 252,600.00 USD | 0.00 USD | 378.93 USD | `-10.60%` | `49.63` |
| `Live` | `Long` | `7.66` | 252,220.00 USD | 0.00 USD | 135.42 USD | `-10.36%` | `17.69` |
| `Live` | `Long` | `7.67` | 252,090.00 USD | 0.00 USD | 256.09 USD | `-10.24%` | `33.41` |
| `Live` | `Long` | `7.67` | 251,830.00 USD | 0.00 USD | 4,480.00 USD | `-10.13%` | `583.63` |
| `Live` | `Long` | `7.68` | 247,350.00 USD | 0.00 USD | 739.30 USD | `-10.01%` | `96.20` |
| `Live` | `Long` | `7.70` | 246,610.00 USD | 0.00 USD | 6,690.00 USD | `-9.89%` | `869.22` |
| `Live` | `Long` | `7.75` | 239,920.00 USD | 0.00 USD | 500.12 USD | `-9.19%` | `64.49` |
| `Live` | `Long` | `7.76` | 239,420.00 USD | 0.00 USD | 455.73 USD | `-9.07%` | `58.69` |
| `Live` | `Long` | `7.78` | 238,970.00 USD | 0.00 USD | 8,670.00 USD | `-8.96%` | `1,115.74` |
| `Live` | `Long` | `7.79` | 230,290.00 USD | 0.00 USD | 1,380.00 USD | `-8.84%` | `177.40` |
| `Live` | `Long` | `7.79` | 228,910.00 USD | 0.00 USD | 4,480.00 USD | `-8.72%` | `574.50` |
| `Live` | `Long` | `7.80` | 224,430.00 USD | 0.00 USD | 6,380.00 USD | `-8.61%` | `817.06` |
| `Live` | `Long` | `7.82` | 218,060.00 USD | 0.00 USD | 775.80 USD | `-8.49%` | `99.27` |
| `Live` | `Long` | `7.83` | 217,280.00 USD | 0.00 USD | 2,270.00 USD | `-8.37%` | `290.31` |
| `Live` | `Long` | `7.84` | 215,010.00 USD | 0.00 USD | 22,560.00 USD | `-8.14%` | `2,875.86` |
| `Live` | `Long` | `7.87` | 192,450.00 USD | 0.00 USD | 233.83 USD | `-7.90%` | `29.73` |
| `Live` | `Long` | `7.88` | 192,210.00 USD | 0.00 USD | 555.19 USD | `-7.79%` | `70.50` |
| `Live` | `Long` | `7.89` | 191,660.00 USD | 0.00 USD | 15,880.00 USD | `-7.55%` | `2,011.99` |
| `Live` | `Long` | `7.91` | 175,770.00 USD | 0.00 USD | 2,360.00 USD | `-7.43%` | `298.43` |
| `Live` | `Long` | `7.92` | 173,420.00 USD | 0.00 USD | 4,600.00 USD | `-7.20%` | `580.78` |
| `Live` | `Long` | `7.93` | 168,810.00 USD | 0.00 USD | 16,340.00 USD | `-7.08%` | `2,059.56` |
| `Live` | `Long` | `7.95` | 152,470.00 USD | 0.00 USD | 127,110.00 USD | `-6.97%` | `15,999.24` |
| `Live` | `Long` | `7.97` | 25,360.00 USD | 0.00 USD | 1,580.00 USD | `-6.61%` | `198.26` |
| `Live` | `Long` | `7.99` | 23,770.00 USD | 0.00 USD | 1,600.00 USD | `-6.50%` | `200.68` |
| `Live` | `Long` | `8.00` | 22,170.00 USD | 0.00 USD | 210.99 USD | `-6.38%` | `26.39` |
| `Live` | `Long` | `8.03` | 21,960.00 USD | 0.00 USD | 248.37 USD | `-6.03%` | `30.95` |
| `Live` | `Long` | `8.07` | 21,710.00 USD | 0.00 USD | 21,710.00 USD | `-5.44%` | `2,688.93` |
| `Live` | `Short` | `8.13` | 213.79 USD | 213.79 USD | 0.00 USD | `-4.74%` | `26.28` |
| `Live` | `Short` | `8.55` | 3,430.00 USD | 3,220.00 USD | 0.00 USD | `+0.18%` | `376.02` |
| `Live` | `Short` | `8.69` | 3,640.00 USD | 209.31 USD | 0.00 USD | `+1.70%` | `24.10` |
| `Live` | `Short` | `8.72` | 3,790.00 USD | 145.62 USD | 0.00 USD | `+2.17%` | `16.69` |
| `Live` | `Short` | `8.80` | 4,640.00 USD | 858.75 USD | 0.00 USD | `+3.10%` | `97.53` |
| `Live` | `Short` | `8.82` | 10,650.00 USD | 6,000.00 USD | 0.00 USD | `+3.34%` | `680.16` |
| `Live` | `Short` | `8.99` | 550,360.00 USD | 539,710.00 USD | 0.00 USD | `+5.33%` | `60,000.94` |
| `Live` | `Short` | `9.19` | 551,950.00 USD | 1,590.00 USD | 0.00 USD | `+7.55%` | `173.30` |
| `Live` | `Short` | `9.21` | 553,820.00 USD | 1,870.00 USD | 0.00 USD | `+7.91%` | `202.76` |
| `Live` | `Short` | `9.41` | 554,260.00 USD | 440.06 USD | 0.00 USD | `+10.25%` | `46.74` |
| `Live` | `Short` | `9.46` | 554,390.00 USD | 138.85 USD | 0.00 USD | `+10.83%` | `14.67` |
| `Live` | `Short` | `9.62` | 554,530.00 USD | 138.98 USD | 0.00 USD | `+12.71%` | `14.44` |
| `Live` | `Short` | `9.64` | 556,470.00 USD | 1,930.00 USD | 0.00 USD | `+12.94%` | `200.61` |
| `Live` | `Short` | `9.73` | 556,660.00 USD | 192.95 USD | 0.00 USD | `+13.99%` | `19.82` |
| `Live` | `Short` | `10.35` | 559,320.00 USD | 2,650.00 USD | 0.00 USD | `+21.14%` | `256.58` |
| `Live` | `Short` | `10.56` | 559,840.00 USD | 523.81 USD | 0.00 USD | `+23.71%` | `49.58` |
| `Live` | `Short` | `10.60` | 581,030.00 USD | 21,190.00 USD | 0.00 USD | `+24.06%` | `2,000.00` |
| `Live` | `Short` | `10.65` | 581,280.00 USD | 255.29 USD | 0.00 USD | `+24.77%` | `23.96` |
| `Live` | `Short` | `10.81` | 582,430.00 USD | 1,150.00 USD | 0.00 USD | `+26.64%` | `106.17` |
| `Live` | `Short` | `10.89` | 582,530.00 USD | 100.13 USD | 0.00 USD | `+27.58%` | `9.19` |
| `Live` | `Short` | `10.90` | 582,840.00 USD | 306.98 USD | 0.00 USD | `+27.69%` | `28.15` |
| `Live` | `Short` | `11.01` | 589,810.00 USD | 6,970.00 USD | 0.00 USD | `+28.87%` | `633.00` |
| `Live` | `Short` | `11.07` | 645,180.00 USD | 55,380.00 USD | 0.00 USD | `+29.69%` | `5,000.00` |
| `Live` | `Short` | `11.27` | 769,500.00 USD | 124,320.00 USD | 0.00 USD | `+31.91%` | `11,035.87` |
| `Live` | `Short` | `11.56` | 773,850.00 USD | 4,350.00 USD | 0.00 USD | `+35.42%` | `376.48` |
| `Live` | `Short` | `11.62` | 785,990.00 USD | 12,140.00 USD | 0.00 USD | `+36.13%` | `1,043.90` |
| `Live` | `Short` | `11.69` | 1,080,000.00 USD | 296,760.00 USD | 0.00 USD | `+36.83%` | `25,397.02` |
| `Live` | `Short` | `11.80` | 1,080,000.00 USD | 114.27 USD | 0.00 USD | `+38.23%` | `9.68` |
| `Live` | `Short` | `11.93` | 1,080,000.00 USD | 505.74 USD | 0.00 USD | `+39.64%` | `42.41` |
| `Live` | `Short` | `11.95` | 1,080,000.00 USD | 1,050.00 USD | 0.00 USD | `+39.87%` | `87.54` |
| `Live` | `Short` | `12.30` | 1,090,000.00 USD | 1,730.00 USD | 0.00 USD | `+44.09%` | `140.71` |
| `Live` | `Short` | `12.40` | 1,090,000.00 USD | 343.62 USD | 0.00 USD | `+45.26%` | `27.70` |
| `Live` | `Short` | `13.20` | 1,170,000.00 USD | 87,940.00 USD | 0.00 USD | `+54.51%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 1,180,000.00 USD | 3,810.00 USD | 0.00 USD | `+55.68%` | `286.56` |
| `Live` | `Short` | `13.46` | 1,180,000.00 USD | 430.34 USD | 0.00 USD | `+57.67%` | `31.96` |
| `Live` | `Short` | `13.69` | 1,180,000.00 USD | 172.29 USD | 0.00 USD | `+60.25%` | `12.59` |
| `Live` | `Short` | `13.84` | 1,240,000.00 USD | 63,020.00 USD | 0.00 USD | `+62.00%` | `4,555.14` |
| `Live` | `Short` | `14.48` | 1,240,000.00 USD | 285.79 USD | 0.00 USD | `+69.62%` | `19.73` |
| `Live` | `Short` | `14.66` | 1,240,000.00 USD | 1,350.00 USD | 0.00 USD | `+71.72%` | `92.03` |
| `Live` | `Short` | `15.07` | 1,240,000.00 USD | 247.38 USD | 0.00 USD | `+76.52%` | `16.41` |
| `Live` | `Short` | `15.21` | 1,250,000.00 USD | 4,220.00 USD | 0.00 USD | `+78.16%` | `277.54` |
| `Live` | `Short` | `15.29` | 1,250,000.00 USD | 229.43 USD | 0.00 USD | `+79.10%` | `15.00` |
| `Live` | `Short` | `15.35` | 1,250,000.00 USD | 230.17 USD | 0.00 USD | `+79.69%` | `15.00` |
| `Live` | `Short` | `15.38` | 1,270,000.00 USD | 20,000.00 USD | 0.00 USD | `+80.15%` | `1,300.00` |
| `Live` | `Short` | `15.40` | 1,270,000.00 USD | 331.98 USD | 0.00 USD | `+80.39%` | `21.55` |
| `Live` | `Short` | `15.72` | 1,270,000.00 USD | 167.79 USD | 0.00 USD | `+84.14%` | `10.67` |
| `Live` | `Short` | `15.77` | 1,270,000.00 USD | 185.55 USD | 0.00 USD | `+84.60%` | `11.77` |
| `Live` | `Short` | `15.82` | 1,270,000.00 USD | 1,700.00 USD | 0.00 USD | `+85.31%` | `107.48` |
| `Live` | `Short` | `16.38` | 1,540,000.00 USD | 265,410.00 USD | 0.00 USD | `+91.75%` | `16,208.00` |
| `Live` | `Short` | `16.45` | 1,560,000.00 USD | 23,260.00 USD | 0.00 USD | `+92.57%` | `1,414.55` |
| `Live` | `Short` | `16.50` | 1,580,000.00 USD | 24,080.00 USD | 0.00 USD | `+93.27%` | `1,459.25` |
| `Live` | `Short` | `16.52` | 1,580,000.00 USD | 190.91 USD | 0.00 USD | `+93.39%` | `11.56` |
| `Live` | `Short` | `16.59` | 1,580,000.00 USD | 109.53 USD | 0.00 USD | `+94.32%` | `6.60` |
| `Live` | `Short` | `16.64` | 1,580,000.00 USD | 118.27 USD | 0.00 USD | `+94.79%` | `7.11` |
| `Live` | `Short` | `16.98` | 1,590,000.00 USD | 1,690.00 USD | 0.00 USD | `+98.89%` | `99.50` |
| `Live` | `Short` | `17.00` | 1,590,000.00 USD | 1,940.00 USD | 0.00 USD | `+99.12%` | `113.93` |
| `Live` | `Short` | `17.02` | 1,590,000.00 USD | 191.87 USD | 0.00 USD | `+99.36%` | `11.27` |
| `Live` | `Short` | `17.04` | 1,670,000.00 USD | 85,820.00 USD | 0.00 USD | `+99.48%` | `5,037.66` |
| `Live` | `Short` | `17.05` | 1,670,000.00 USD | 207.78 USD | 0.00 USD | `+99.59%` | `12.19` |
| `Live` | `Short` | `17.07` | 1,680,000.00 USD | 6,740.00 USD | 0.00 USD | `+99.94%` | `395.02` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 378,050.00 USD | 0.00 USD | 611.73 USD | `-72.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 377,440.00 USD | 0.00 USD | 793.75 USD | `-53.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 376,650.00 USD | 0.00 USD | 67,970.00 USD | `-41.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 308,680.00 USD | 0.00 USD | 205.30 USD | `-37.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 308,480.00 USD | 0.00 USD | 465.42 USD | `-36.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 308,010.00 USD | 0.00 USD | 349.35 USD | `-35.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.54` | 307,660.00 USD | 0.00 USD | 1,020.00 USD | `-35.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 306,650.00 USD | 0.00 USD | 1,330.00 USD | `-31.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 305,320.00 USD | 0.00 USD | 493.50 USD | `-30.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 304,820.00 USD | 0.00 USD | 100.98 USD | `-30.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 304,720.00 USD | 0.00 USD | 500.70 USD | `-29.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 304,220.00 USD | 0.00 USD | 4,160.00 USD | `-28.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 300,070.00 USD | 0.00 USD | 6,500.00 USD | `-27.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.21` | 293,560.00 USD | 0.00 USD | 906.18 USD | `-27.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.25` | 292,660.00 USD | 0.00 USD | 127.35 USD | `-26.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 292,530.00 USD | 0.00 USD | 864.38 USD | `-26.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 291,670.00 USD | 0.00 USD | 130.10 USD | `-23.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 291,540.00 USD | 0.00 USD | 4,340.00 USD | `-23.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 287,200.00 USD | 0.00 USD | 5,520.00 USD | `-21.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 281,670.00 USD | 0.00 USD | 100.72 USD | `-21.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 281,570.00 USD | 0.00 USD | 296.34 USD | `-20.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 281,280.00 USD | 0.00 USD | 921.19 USD | `-20.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 280,360.00 USD | 0.00 USD | 709.98 USD | `-19.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.92` | 279,650.00 USD | 0.00 USD | 1,380.00 USD | `-19.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 278,260.00 USD | 0.00 USD | 262.44 USD | `-18.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 278,000.00 USD | 0.00 USD | 24,350.00 USD | `-17.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.11` | 253,650.00 USD | 0.00 USD | 187.79 USD | `-16.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 253,460.00 USD | 0.00 USD | 6,790.00 USD | `-16.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 246,670.00 USD | 0.00 USD | 9,770.00 USD | `-15.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.21` | 236,900.00 USD | 0.00 USD | 7,210.00 USD | `-15.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 229,700.00 USD | 0.00 USD | 282.74 USD | `-15.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 229,420.00 USD | 0.00 USD | 603.44 USD | `-15.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 228,810.00 USD | 0.00 USD | 464.61 USD | `-15.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 228,350.00 USD | 0.00 USD | 2,090.00 USD | `-14.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 226,250.00 USD | 0.00 USD | 129.58 USD | `-14.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 226,120.00 USD | 0.00 USD | 114.65 USD | `-14.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.39` | 226,010.00 USD | 0.00 USD | 702.75 USD | `-13.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.41` | 225,310.00 USD | 0.00 USD | 4,630.00 USD | `-13.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 220,670.00 USD | 0.00 USD | 199.39 USD | `-12.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 220,470.00 USD | 0.00 USD | 6,270.00 USD | `-12.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 214,210.00 USD | 0.00 USD | 37,420.00 USD | `-12.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 176,780.00 USD | 0.00 USD | 2,120.00 USD | `-12.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 174,660.00 USD | 0.00 USD | 799.83 USD | `-11.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.54` | 173,860.00 USD | 0.00 USD | 820.44 USD | `-11.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 173,040.00 USD | 0.00 USD | 218.24 USD | `-11.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 172,820.00 USD | 0.00 USD | 113.78 USD | `-11.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.61` | 172,710.00 USD | 0.00 USD | 152.10 USD | `-10.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.62` | 172,560.00 USD | 0.00 USD | 297.59 USD | `-10.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.68` | 172,260.00 USD | 0.00 USD | 528.88 USD | `-10.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 171,730.00 USD | 0.00 USD | 360.13 USD | `-9.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 171,370.00 USD | 0.00 USD | 578.04 USD | `-9.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.79` | 170,790.00 USD | 0.00 USD | 424.05 USD | `-8.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 170,370.00 USD | 0.00 USD | 23,320.00 USD | `-8.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.82` | 147,050.00 USD | 0.00 USD | 3,940.00 USD | `-8.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 143,110.00 USD | 0.00 USD | 115.23 USD | `-8.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 143,000.00 USD | 0.00 USD | 183.33 USD | `-7.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 142,820.00 USD | 0.00 USD | 1,890.00 USD | `-7.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 140,920.00 USD | 0.00 USD | 6,520.00 USD | `-7.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 134,410.00 USD | 0.00 USD | 5,710.00 USD | `-7.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 128,700.00 USD | 0.00 USD | 1,590.00 USD | `-7.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 127,110.00 USD | 0.00 USD | 898.42 USD | `-6.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 126,210.00 USD | 0.00 USD | 7,960.00 USD | `-6.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.99` | 118,260.00 USD | 0.00 USD | 9,160.00 USD | `-6.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 109,100.00 USD | 0.00 USD | 3,430.00 USD | `-6.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 105,660.00 USD | 0.00 USD | 123.58 USD | `-5.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 105,540.00 USD | 0.00 USD | 2,110.00 USD | `-5.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 103,430.00 USD | 0.00 USD | 152.56 USD | `-5.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.06` | 103,280.00 USD | 0.00 USD | 2,730.00 USD | `-5.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 100,550.00 USD | 0.00 USD | 121.69 USD | `-5.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.09` | 100,430.00 USD | 0.00 USD | 5,230.00 USD | `-5.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 95,190.00 USD | 0.00 USD | 477.36 USD | `-5.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 94,720.00 USD | 0.00 USD | 924.78 USD | `-5.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 93,790.00 USD | 0.00 USD | 744.88 USD | `-4.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 93,050.00 USD | 0.00 USD | 6,500.00 USD | `-4.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 86,550.00 USD | 0.00 USD | 884.60 USD | `-4.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 85,660.00 USD | 0.00 USD | 5,550.00 USD | `-4.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 80,110.00 USD | 0.00 USD | 1,430.00 USD | `-4.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 78,670.00 USD | 0.00 USD | 3,080.00 USD | `-4.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 75,590.00 USD | 0.00 USD | 520.75 USD | `-4.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 75,070.00 USD | 0.00 USD | 3,020.00 USD | `-4.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 72,050.00 USD | 0.00 USD | 141.04 USD | `-4.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 71,910.00 USD | 0.00 USD | 22,560.00 USD | `-3.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 49,340.00 USD | 0.00 USD | 515.66 USD | `-3.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.22` | 48,830.00 USD | 0.00 USD | 139.74 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 48,690.00 USD | 0.00 USD | 490.15 USD | `-3.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.24` | 48,200.00 USD | 0.00 USD | 197.96 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.26` | 48,000.00 USD | 0.00 USD | 9,110.00 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.27` | 38,890.00 USD | 0.00 USD | 535.65 USD | `-3.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 38,350.00 USD | 0.00 USD | 408.78 USD | `-3.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 37,940.00 USD | 0.00 USD | 201.49 USD | `-2.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 37,740.00 USD | 0.00 USD | 4,150.00 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 33,590.00 USD | 0.00 USD | 242.42 USD | `-2.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 33,350.00 USD | 0.00 USD | 2,920.00 USD | `-2.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.32` | 30,430.00 USD | 0.00 USD | 1,690.00 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 28,740.00 USD | 0.00 USD | 408.58 USD | `-2.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 28,330.00 USD | 0.00 USD | 756.06 USD | `-2.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 27,580.00 USD | 0.00 USD | 970.35 USD | `-2.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 26,610.00 USD | 0.00 USD | 503.59 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 26,100.00 USD | 0.00 USD | 419.25 USD | `-1.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 25,690.00 USD | 0.00 USD | 1,970.00 USD | `-1.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 23,720.00 USD | 0.00 USD | 201.80 USD | `-1.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 23,520.00 USD | 0.00 USD | 314.81 USD | `-1.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 23,200.00 USD | 0.00 USD | 1,880.00 USD | `-1.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 21,320.00 USD | 0.00 USD | 307.54 USD | `-1.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 21,010.00 USD | 0.00 USD | 138.24 USD | `-1.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 20,870.00 USD | 0.00 USD | 710.81 USD | `-0.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.47` | 20,160.00 USD | 0.00 USD | 769.61 USD | `-0.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.48` | 19,390.00 USD | 0.00 USD | 146.79 USD | `-0.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.49` | 19,240.00 USD | 0.00 USD | 408.78 USD | `-0.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.51` | 18,840.00 USD | 0.00 USD | 17,010.00 USD | `-0.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.52` | 1,830.00 USD | 0.00 USD | 408.55 USD | `-0.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.53` | 1,420.00 USD | 0.00 USD | 1,130.00 USD | `-0.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.54` | 290.10 USD | 0.00 USD | 290.10 USD | `-0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 4,400.00 USD | 4,400.00 USD | 0.00 USD | `+0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.55` | 4,650.00 USD | 243.82 USD | 0.00 USD | `+0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.56` | 6,250.00 USD | 1,600.00 USD | 0.00 USD | `+0.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.57` | 6,810.00 USD | 566.55 USD | 0.00 USD | `+0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.59` | 6,960.00 USD | 143.28 USD | 0.00 USD | `+0.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.60` | 8,090.00 USD | 1,130.00 USD | 0.00 USD | `+0.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 8,840.00 USD | 751.56 USD | 0.00 USD | `+0.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 10,330.00 USD | 1,490.00 USD | 0.00 USD | `+0.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 14,620.00 USD | 4,290.00 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.63` | 14,820.00 USD | 201.97 USD | 0.00 USD | `+1.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.64` | 14,920.00 USD | 103.31 USD | 0.00 USD | `+1.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 15,030.00 USD | 107.84 USD | 0.00 USD | `+1.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 15,140.00 USD | 107.97 USD | 0.00 USD | `+1.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.68` | 15,320.00 USD | 176.62 USD | 0.00 USD | `+1.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.69` | 16,310.00 USD | 990.09 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.70` | 21,320.00 USD | 5,010.00 USD | 0.00 USD | `+1.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 21,890.00 USD | 575.14 USD | 0.00 USD | `+1.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 22,290.00 USD | 399.67 USD | 0.00 USD | `+2.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.72` | 23,110.00 USD | 819.28 USD | 0.00 USD | `+2.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.73` | 23,440.00 USD | 333.07 USD | 0.00 USD | `+2.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.74` | 27,820.00 USD | 4,370.00 USD | 0.00 USD | `+2.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.76` | 29,590.00 USD | 1,780.00 USD | 0.00 USD | `+2.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 69,400.00 USD | 39,810.00 USD | 0.00 USD | `+2.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.78` | 69,620.00 USD | 215.16 USD | 0.00 USD | `+2.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 70,010.00 USD | 388.12 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 70,720.00 USD | 711.78 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 88,890.00 USD | 18,170.00 USD | 0.00 USD | `+3.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.82` | 90,920.00 USD | 2,030.00 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.84` | 91,170.00 USD | 243.40 USD | 0.00 USD | `+3.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 96,930.00 USD | 5,760.00 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 97,170.00 USD | 234.04 USD | 0.00 USD | `+3.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 97,330.00 USD | 163.91 USD | 0.00 USD | `+3.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 97,440.00 USD | 110.58 USD | 0.00 USD | `+3.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 98,540.00 USD | 1,100.00 USD | 0.00 USD | `+4.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 100,480.00 USD | 1,930.00 USD | 0.00 USD | `+4.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 101,270.00 USD | 788.72 USD | 0.00 USD | `+4.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 103,070.00 USD | 1,800.00 USD | 0.00 USD | `+4.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 103,230.00 USD | 163.33 USD | 0.00 USD | `+4.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 132,760.00 USD | 29,520.00 USD | 0.00 USD | `+4.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 132,980.00 USD | 223.62 USD | 0.00 USD | `+4.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 133,160.00 USD | 180.53 USD | 0.00 USD | `+4.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 133,560.00 USD | 401.63 USD | 0.00 USD | `+4.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 448,710.00 USD | 315,150.00 USD | 0.00 USD | `+5.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 448,820.00 USD | 104.59 USD | 0.00 USD | `+5.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 449,080.00 USD | 262.56 USD | 0.00 USD | `+5.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 449,210.00 USD | 130.03 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 450,590.00 USD | 1,380.00 USD | 0.00 USD | `+5.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 451,680.00 USD | 1,090.00 USD | 0.00 USD | `+5.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 452,290.00 USD | 616.37 USD | 0.00 USD | `+5.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 452,390.00 USD | 102.03 USD | 0.00 USD | `+5.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 452,850.00 USD | 453.84 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 453,010.00 USD | 160.99 USD | 0.00 USD | `+6.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 453,230.00 USD | 215.98 USD | 0.00 USD | `+6.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 454,730.00 USD | 1,510.00 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 455,340.00 USD | 606.18 USD | 0.00 USD | `+6.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 910,600.00 USD | 455,260.00 USD | 0.00 USD | `+6.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 915,160.00 USD | 4,560.00 USD | 0.00 USD | `+6.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 915,320.00 USD | 166.53 USD | 0.00 USD | `+6.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 917,320.00 USD | 2,000.00 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 1,310,000.00 USD | 394,210.00 USD | 0.00 USD | `+7.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,310,000.00 USD | 119.24 USD | 0.00 USD | `+7.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,310,000.00 USD | 2,660.00 USD | 0.00 USD | `+7.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,310,000.00 USD | 131.87 USD | 0.00 USD | `+7.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,310,000.00 USD | 149.17 USD | 0.00 USD | `+8.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,320,000.00 USD | 2,220.00 USD | 0.00 USD | `+8.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,550,000.00 USD | 231,380.00 USD | 0.00 USD | `+8.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,550,000.00 USD | 1,960.00 USD | 0.00 USD | `+8.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,550,000.00 USD | 434.45 USD | 0.00 USD | `+8.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,570,000.00 USD | 18,610.00 USD | 0.00 USD | `+8.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,570,000.00 USD | 166.83 USD | 0.00 USD | `+9.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,570,000.00 USD | 150.79 USD | 0.00 USD | `+9.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,570,000.00 USD | 101.58 USD | 0.00 USD | `+9.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,570,000.00 USD | 109.36 USD | 0.00 USD | `+9.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,570,000.00 USD | 116.69 USD | 0.00 USD | `+9.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,570,000.00 USD | 163.41 USD | 0.00 USD | `+9.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,570,000.00 USD | 102.01 USD | 0.00 USD | `+9.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,570,000.00 USD | 660.84 USD | 0.00 USD | `+10.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,570,000.00 USD | 714.59 USD | 0.00 USD | `+10.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,570,000.00 USD | 928.13 USD | 0.00 USD | `+10.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 1,570,000.00 USD | 102.45 USD | 0.00 USD | `+10.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,570,000.00 USD | 219.84 USD | 0.00 USD | `+10.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,570,000.00 USD | 1,890.00 USD | 0.00 USD | `+10.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,580,000.00 USD | 1,130.00 USD | 0.00 USD | `+11.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,580,000.00 USD | 288.46 USD | 0.00 USD | `+11.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,580,000.00 USD | 119.92 USD | 0.00 USD | `+11.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,580,000.00 USD | 231.00 USD | 0.00 USD | `+12.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,580,000.00 USD | 221.07 USD | 0.00 USD | `+12.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,580,000.00 USD | 992.00 USD | 0.00 USD | `+12.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,580,000.00 USD | 148.48 USD | 0.00 USD | `+12.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,580,000.00 USD | 191.36 USD | 0.00 USD | `+13.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,580,000.00 USD | 4,440.00 USD | 0.00 USD | `+13.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,580,000.00 USD | 108.21 USD | 0.00 USD | `+13.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,580,000.00 USD | 169.68 USD | 0.00 USD | `+13.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.74` | 1,580,000.00 USD | 574.66 USD | 0.00 USD | `+14.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,580,000.00 USD | 121.87 USD | 0.00 USD | `+14.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,580,000.00 USD | 115.88 USD | 0.00 USD | `+15.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,580,000.00 USD | 340.05 USD | 0.00 USD | `+15.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,580,000.00 USD | 742.12 USD | 0.00 USD | `+15.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,590,000.00 USD | 899.47 USD | 0.00 USD | `+15.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,660,000.00 USD | 70,020.00 USD | 0.00 USD | `+16.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,660,000.00 USD | 373.97 USD | 0.00 USD | `+16.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,660,000.00 USD | 5,050.00 USD | 0.00 USD | `+17.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,670,000.00 USD | 6,370.00 USD | 0.00 USD | `+17.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,670,000.00 USD | 404.20 USD | 0.00 USD | `+18.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,880,000.00 USD | 210,980.00 USD | 0.00 USD | `+18.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,880,000.00 USD | 1,150.00 USD | 0.00 USD | `+18.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 1,880,000.00 USD | 172.16 USD | 0.00 USD | `+19.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 1,880,000.00 USD | 922.87 USD | 0.00 USD | `+20.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 1,880,000.00 USD | 489.40 USD | 0.00 USD | `+20.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 1,880,000.00 USD | 1,200.00 USD | 0.00 USD | `+21.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 1,880,000.00 USD | 118.01 USD | 0.00 USD | `+22.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.47` | 1,880,000.00 USD | 818.31 USD | 0.00 USD | `+22.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 1,880,000.00 USD | 312.31 USD | 0.00 USD | `+23.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 1,890,000.00 USD | 2,290.00 USD | 0.00 USD | `+23.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 1,890,000.00 USD | 178.46 USD | 0.00 USD | `+23.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 1,890,000.00 USD | 173.42 USD | 0.00 USD | `+25.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 1,890,000.00 USD | 184.75 USD | 0.00 USD | `+25.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 1,890,000.00 USD | 135.78 USD | 0.00 USD | `+26.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 1,890,000.00 USD | 127.96 USD | 0.00 USD | `+26.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 1,890,000.00 USD | 476.43 USD | 0.00 USD | `+27.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 1,890,000.00 USD | 869.35 USD | 0.00 USD | `+27.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 1,890,000.00 USD | 118.97 USD | 0.00 USD | `+27.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 1,890,000.00 USD | 251.06 USD | 0.00 USD | `+27.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 1,890,000.00 USD | 552.44 USD | 0.00 USD | `+28.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 1,890,000.00 USD | 537.26 USD | 0.00 USD | `+28.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 1,890,000.00 USD | 320.29 USD | 0.00 USD | `+30.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 1,890,000.00 USD | 1,100.00 USD | 0.00 USD | `+30.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 1,890,000.00 USD | 2,270.00 USD | 0.00 USD | `+31.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 1,890,000.00 USD | 1,270.00 USD | 0.00 USD | `+31.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 1,900,000.00 USD | 1,380.00 USD | 0.00 USD | `+32.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 1,900,000.00 USD | 2,410.00 USD | 0.00 USD | `+33.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 1,910,000.00 USD | 9,520.00 USD | 0.00 USD | `+34.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.48` | 1,910,000.00 USD | 2,050.00 USD | 0.00 USD | `+34.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 1,910,000.00 USD | 529.11 USD | 0.00 USD | `+34.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 1,920,000.00 USD | 7,700.00 USD | 0.00 USD | `+35.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 1,920,000.00 USD | 906.03 USD | 0.00 USD | `+38.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 1,920,000.00 USD | 434.61 USD | 0.00 USD | `+38.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 1,920,000.00 USD | 163.52 USD | 0.00 USD | `+39.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 1,930,000.00 USD | 10,370.00 USD | 0.00 USD | `+40.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.19` | 1,940,000.00 USD | 5,270.00 USD | 0.00 USD | `+42.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.28` | 1,940,000.00 USD | 115.02 USD | 0.00 USD | `+43.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 1,940,000.00 USD | 3,350.00 USD | 0.00 USD | `+48.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 1,940,000.00 USD | 197.97 USD | 0.00 USD | `+49.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 1,940,000.00 USD | 3,200.00 USD | 0.00 USD | `+51.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 1,940,000.00 USD | 179.58 USD | 0.00 USD | `+52.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 1,940,000.00 USD | 568.45 USD | 0.00 USD | `+52.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 1,940,000.00 USD | 169.57 USD | 0.00 USD | `+53.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 1,940,000.00 USD | 446.52 USD | 0.00 USD | `+56.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 1,950,000.00 USD | 5,320.00 USD | 0.00 USD | `+57.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,160,000.00 USD | 210,750.00 USD | 0.00 USD | `+58.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,160,000.00 USD | 407.95 USD | 0.00 USD | `+60.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,160,000.00 USD | 174.91 USD | 0.00 USD | `+61.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,160,000.00 USD | 4,650.00 USD | 0.00 USD | `+63.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,170,000.00 USD | 960.26 USD | 0.00 USD | `+66.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,170,000.00 USD | 2,710.00 USD | 0.00 USD | `+68.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,170,000.00 USD | 805.90 USD | 0.00 USD | `+69.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,170,000.00 USD | 655.55 USD | 0.00 USD | `+72.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,170,000.00 USD | 4,890.00 USD | 0.00 USD | `+73.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,180,000.00 USD | 471.09 USD | 0.00 USD | `+74.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,180,000.00 USD | 383.85 USD | 0.00 USD | `+75.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 2,830,000.00 USD | 653,420.00 USD | 0.00 USD | `+75.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.06` | 2,830,000.00 USD | 3,010.00 USD | 0.00 USD | `+76.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 2,830,000.00 USD | 111.87 USD | 0.00 USD | `+85.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 2,830,000.00 USD | 219.91 USD | 0.00 USD | `+87.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 2,830,000.00 USD | 121.74 USD | 0.00 USD | `+98.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.00` | 2,830,000.00 USD | 297.59 USD | 0.00 USD | `+99.12%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.13` | 7,650,000.00 USD | 0.00 USD | 7,650,000.00 USD | 18,640.00 USD | 15,550.00 USD | 22,160.00 USD |
| `7D` | `7.15` | 7,600,000.00 USD | 0.00 USD | 7,600,000.00 USD | 48,450.00 USD | 13,490.00 USD | 43,200.00 USD |
| `7D` | `7.17` | 7,490,000.00 USD | 0.00 USD | 7,490,000.00 USD | 28,970.00 USD | 1,110.00 USD | 25,890.00 USD |
| `7D` | `7.19` | 7,440,000.00 USD | 0.00 USD | 7,440,000.00 USD | 1,420.00 USD | 11,080.00 USD | 10,640.00 USD |
| `7D` | `7.21` | 7,410,000.00 USD | 0.00 USD | 7,410,000.00 USD | 11,990.00 USD | 2,530.00 USD | 1,910.00 USD |
| `7D` | `7.23` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 37,070.00 USD | 4,000.00 USD | 14,430.00 USD |
| `7D` | `7.25` | 7,340,000.00 USD | 0.00 USD | 7,340,000.00 USD | 14,900.00 USD | 0.00 USD | 9,760.00 USD |
| `7D` | `7.27` | 7,320,000.00 USD | 0.00 USD | 7,320,000.00 USD | 420.05 USD | 1,810.00 USD | 4,200.00 USD |
| `7D` | `7.29` | 7,310,000.00 USD | 0.00 USD | 7,310,000.00 USD | 7,520.00 USD | 0.00 USD | 92.04 USD |
| `7D` | `7.31` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 252.80 USD | 0.00 USD | 13,390.00 USD |
| `7D` | `7.33` | 7,290,000.00 USD | 0.00 USD | 7,290,000.00 USD | 7,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.37` | 7,280,000.00 USD | 0.00 USD | 7,280,000.00 USD | 45,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.39` | 7,230,000.00 USD | 0.00 USD | 7,230,000.00 USD | 46,200.00 USD | 0.00 USD | 457.98 USD |
| `7D` | `7.43` | 7,190,000.00 USD | 0.00 USD | 7,190,000.00 USD | 0.00 USD | 0.00 USD | 503.12 USD |
| `7D` | `7.45` | 7,190,000.00 USD | 0.00 USD | 7,190,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD |
| `7D` | `7.49` | 7,160,000.00 USD | 0.00 USD | 7,160,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD |
| `7D` | `7.51` | 7,140,000.00 USD | 0.00 USD | 7,140,000.00 USD | 2,070.00 USD | 0.00 USD | 18,890.00 USD |
| `7D` | `7.53` | 7,120,000.00 USD | 0.00 USD | 7,120,000.00 USD | 35,990.00 USD | 18,910.00 USD | 570.66 USD |
| `1D` | `7.55` | 6,490,000.00 USD | 0.00 USD | 6,490,000.00 USD | 9,760.00 USD | 4,270.00 USD | 136.40 USD |
| `7D` | `7.55` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 20,150.00 USD | 4,310.00 USD | 0.00 USD |
| `1D` | `7.56` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 15,640.00 USD | 0.00 USD | 3,020.00 USD |
| `1D` | `7.57` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 164.75 USD | 0.00 USD | 101.23 USD |
| `1D` | `7.58` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 558.97 USD | 0.00 USD | 3,490.00 USD |
| `1D` | `7.59` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 583.80 USD | 0.00 USD | 4,070.00 USD |
| `7D` | `7.59` | 7,040,000.00 USD | 0.00 USD | 7,040,000.00 USD | 0.00 USD | 0.00 USD | 301.55 USD |
| `1D` | `7.60` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 476.16 USD | 4,900.00 USD | 351.13 USD |
| `1D` | `7.61` | 6,440,000.00 USD | 0.00 USD | 6,440,000.00 USD | 853.92 USD | 761.26 USD | 11,670.00 USD |
| `1D` | `7.62` | 6,430,000.00 USD | 0.00 USD | 6,430,000.00 USD | 0.00 USD | 0.00 USD | 133.28 USD |
| `1D` | `7.63` | 6,430,000.00 USD | 0.00 USD | 6,430,000.00 USD | 1,050.00 USD | 0.00 USD | 8,000.00 USD |
| `7D` | `7.63` | 7,040,000.00 USD | 0.00 USD | 7,040,000.00 USD | 41,300.00 USD | 0.00 USD | 386.35 USD |
| `1D` | `7.64` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 32,470.00 USD | 812.96 USD | 158.22 USD |
| `1D` | `7.65` | 6,380,000.00 USD | 0.00 USD | 6,380,000.00 USD | 2,280.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `7.65` | 7,000,000.00 USD | 0.00 USD | 7,000,000.00 USD | 4,870.00 USD | 0.00 USD | 813.38 USD |
| `1D` | `7.66` | 6,370,000.00 USD | 0.00 USD | 6,370,000.00 USD | 1,060.00 USD | 0.00 USD | 531.95 USD |
| `1D` | `7.67` | 6,370,000.00 USD | 0.00 USD | 6,370,000.00 USD | 215.07 USD | 0.00 USD | 114.38 USD |
| `7D` | `7.67` | 6,990,000.00 USD | 0.00 USD | 6,990,000.00 USD | 0.00 USD | 0.00 USD | 34,010.00 USD |
| `1D` | `7.68` | 6,370,000.00 USD | 0.00 USD | 6,370,000.00 USD | 2,140.00 USD | 0.00 USD | 3,830.00 USD |
| `1D` | `7.69` | 6,360,000.00 USD | 0.00 USD | 6,360,000.00 USD | 195.46 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.69` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 0.00 USD | 0.00 USD | 1,020.00 USD |
| `1D` | `7.70` | 6,360,000.00 USD | 0.00 USD | 6,360,000.00 USD | 1,250.00 USD | 2,390.00 USD | 16,770.00 USD |
| `1D` | `7.71` | 6,340,000.00 USD | 0.00 USD | 6,340,000.00 USD | 837.10 USD | 5,040.00 USD | 7,390.00 USD |
| `7D` | `7.71` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 0.00 USD | 0.00 USD | 33,140.00 USD |
| `1D` | `7.73` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 476.46 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.73` | 6,930,000.00 USD | 0.00 USD | 6,930,000.00 USD | 39,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.74` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 10,130.00 USD | 0.00 USD | 184.39 USD |
| `1D` | `7.75` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 625.40 USD | 5,560.00 USD | 0.00 USD |
| `7D` | `7.75` | 6,890,000.00 USD | 0.00 USD | 6,890,000.00 USD | 976.80 USD | 13,360.00 USD | 10,340.00 USD |
| `1D` | `7.76` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 440.27 USD | 0.00 USD | 2,040.00 USD |
| `1D` | `7.77` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 22,180.00 USD | 572.85 USD | 5,870.00 USD |
| `7D` | `7.77` | 6,860,000.00 USD | 0.00 USD | 6,860,000.00 USD | 20,120.00 USD | 4,900.00 USD | 4,850.00 USD |
| `1D` | `7.78` | 6,280,000.00 USD | 0.00 USD | 6,280,000.00 USD | 6,530.00 USD | 7,180.00 USD | 0.00 USD |
| `1D` | `7.79` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 11,000.00 USD | 2,910.00 USD | 589.02 USD |
| `7D` | `7.79` | 6,830,000.00 USD | 0.00 USD | 6,830,000.00 USD | 42,100.00 USD | 4,540.00 USD | 15,300.00 USD |
| `1D` | `7.80` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 5,850.00 USD | 9,380.00 USD | 3,630.00 USD |
| `1D` | `7.81` | 6,240,000.00 USD | 0.00 USD | 6,240,000.00 USD | 2,690.00 USD | 728.43 USD | 0.00 USD |
| `7D` | `7.81` | 6,770,000.00 USD | 0.00 USD | 6,770,000.00 USD | 3,970.00 USD | 11,570.00 USD | 970.74 USD |
| `1D` | `7.82` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 5,590.00 USD | 2,970.00 USD | 2,500.00 USD |
| `1D` | `7.83` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 28,610.00 USD | 6,330.00 USD | 1,350.00 USD |
| `7D` | `7.83` | 6,750,000.00 USD | 0.00 USD | 6,750,000.00 USD | 29,530.00 USD | 2,130.00 USD | 25,880.00 USD |
| `1D` | `7.84` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 2,240.00 USD | 1,800.00 USD | 10.76 USD |
| `1D` | `7.85` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 5,920.00 USD | 1,250.00 USD | 2,650.00 USD |
| `7D` | `7.85` | 6,700,000.00 USD | 0.00 USD | 6,700,000.00 USD | 17,330.00 USD | 7,840.00 USD | 12,950.00 USD |
| `1D` | `7.86` | 6,170,000.00 USD | 0.00 USD | 6,170,000.00 USD | 6,560.00 USD | 6,690.00 USD | 18,710.00 USD |
| `1D` | `7.87` | 6,140,000.00 USD | 0.00 USD | 6,140,000.00 USD | 12,770.00 USD | 10,860.00 USD | 24,540.00 USD |
| `7D` | `7.87` | 6,660,000.00 USD | 0.00 USD | 6,660,000.00 USD | 150,960.00 USD | 1,540.00 USD | 21,480.00 USD |
| `1D` | `7.88` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 159,660.00 USD | 5,890.00 USD | 34,820.00 USD |
| `1D` | `7.89` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 59,920.00 USD | 3,720.00 USD | 27,230.00 USD |
| `7D` | `7.89` | 6,480,000.00 USD | 0.00 USD | 6,480,000.00 USD | 149,100.00 USD | 18,320.00 USD | 24,630.00 USD |
| `1D` | `7.90` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 59,090.00 USD | 6,970.00 USD | 5,960.00 USD |
| `1D` | `7.91` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 8,600.00 USD | 10,370.00 USD | 28,300.00 USD |
| `7D` | `7.91` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 31,740.00 USD | 26,330.00 USD | 44,290.00 USD |
| `1D` | `7.92` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 13,870.00 USD | 2,950.00 USD | 8,760.00 USD |
| `1D` | `7.93` | 5,650,000.00 USD | 0.00 USD | 5,650,000.00 USD | 9,090.00 USD | 6,570.00 USD | 4,480.00 USD |
| `7D` | `7.93` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 78,470.00 USD | 7,330.00 USD | 15,150.00 USD |
| `1D` | `7.94` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 16,530.00 USD | 20,510.00 USD | 61,750.00 USD |
| `1D` | `7.95` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 30,230.00 USD | 9,190.00 USD | 86,980.00 USD |
| `7D` | `7.95` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 43,890.00 USD | 9,500.00 USD | 102,900.00 USD |
| `1D` | `7.96` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 2,980.00 USD | 15,680.00 USD | 62,330.00 USD |
| `1D` | `7.97` | 5,330,000.00 USD | 0.00 USD | 5,330,000.00 USD | 14,930.00 USD | 9,820.00 USD | 4,040.00 USD |
| `7D` | `7.97` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 37,150.00 USD | 18,700.00 USD | 41,650.00 USD |
| `1D` | `7.98` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 8,200.00 USD | 2,060.00 USD | 42,970.00 USD |
| `1D` | `7.99` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 3,790.00 USD | 10,180.00 USD | 4,660.00 USD |
| `7D` | `7.99` | 5,830,000.00 USD | 0.00 USD | 5,830,000.00 USD | 51,690.00 USD | 20,640.00 USD | 121,910.00 USD |
| `1D` | `8.00` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 54,330.00 USD | 8,950.00 USD | 21,810.00 USD |
| `1D` | `8.01` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 5,550.00 USD | 3,750.00 USD | 3,970.00 USD |
| `7D` | `8.01` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 47,370.00 USD | 17,990.00 USD | 46,300.00 USD |
| `1D` | `8.02` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 74,550.00 USD | 0.00 USD | 274.70 USD |
| `1D` | `8.03` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 9,590.00 USD | 12,540.00 USD | 12,890.00 USD |
| `7D` | `8.03` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 352,180.00 USD | 35,720.00 USD | 47,000.00 USD |
| `1D` | `8.04` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 48,750.00 USD | 0.00 USD | 10,010.00 USD |
| `1D` | `8.05` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 317,540.00 USD | 6,430.00 USD | 53,800.00 USD |
| `7D` | `8.05` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 388,880.00 USD | 0.00 USD | 62,840.00 USD |
| `1D` | `8.06` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 155,460.00 USD | 0.00 USD | 66,970.00 USD |
| `1D` | `8.07` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 129,880.00 USD | 9,310.00 USD | 4,540.00 USD |
| `7D` | `8.07` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 60,670.00 USD | 0.00 USD | 75,410.00 USD |
| `1D` | `8.08` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 14,660.00 USD | 0.00 USD | 65,310.00 USD |
| `1D` | `8.09` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 2,670.00 USD | 0.00 USD | 29,580.00 USD |
| `7D` | `8.09` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 30,090.00 USD | 0.00 USD | 80,490.00 USD |
| `1D` | `8.10` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 32,050.00 USD | 6,770.00 USD | 122,420.00 USD |
| `1D` | `8.11` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 78,170.00 USD | 0.00 USD | 192,180.00 USD |
| `7D` | `8.11` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 33,000.00 USD | 0.00 USD | 141,050.00 USD |
| `1D` | `8.12` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 9,950.00 USD | 10,020.00 USD | 126,250.00 USD |
| `1D` | `8.13` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 731.93 USD | 4,510.00 USD | 0.00 USD |
| `7D` | `8.13` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 25,980.00 USD | 7,420.00 USD | 20,570.00 USD |
| `1D` | `8.14` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 346.86 USD | 4,120.00 USD | 96,680.00 USD |
| `1D` | `8.15` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 40,580.00 USD | 11,230.00 USD | 46,550.00 USD |
| `7D` | `8.15` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 179,060.00 USD | 31,560.00 USD | 198,630.00 USD |
| `1D` | `8.16` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 0.00 USD | 17,890.00 USD | 165,460.00 USD |
| `1D` | `8.17` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 11,380.00 USD | 8,610.00 USD | 183,140.00 USD |
| `7D` | `8.17` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 1,570.00 USD | 7,770.00 USD | 159,590.00 USD |
| `1D` | `8.18` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 7,390.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.19` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 17,640.00 USD | 0.00 USD | 15,460.00 USD |
| `7D` | `8.19` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 0.00 USD | 75,510.00 USD | 26,640.00 USD |
| `1D` | `8.20` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 25,530.00 USD | 0.00 USD | 11,410.00 USD |
| `1D` | `8.21` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 33,010.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.21` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 174,220.00 USD | 22,240.00 USD | 5,890.00 USD |
| `1D` | `8.22` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 16,310.00 USD |
| `1D` | `8.23` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 0.00 USD | 1,750.00 USD | 35.82 USD |
| `7D` | `8.23` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 0.00 USD | 40,260.00 USD | 0.00 USD |
| `1D` | `8.24` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 0.00 USD | 1,020.00 USD | 0.98 USD |
| `1D` | `8.25` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 24,160.00 USD |
| `7D` | `8.25` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 129,670.00 USD | 5,750.00 USD | 0.00 USD |
| `1D` | `8.26` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 32,580.00 USD | 12,510.00 USD | 23,300.00 USD |
| `1D` | `8.27` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 15,350.00 USD | 9,880.00 USD | 21.52 USD |
| `7D` | `8.27` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 43,320.00 USD | 4,000.00 USD | 27,210.00 USD |
| `1D` | `8.28` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 881.90 USD | 9,050.00 USD | 0.50 USD |
| `1D` | `8.29` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 14,780.00 USD | 8,320.00 USD | 0.00 USD |
| `7D` | `8.29` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 166,800.00 USD | 0.00 USD | 1,800.00 USD |
| `1D` | `8.30` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 889.10 USD | 4,480.00 USD | 0.00 USD |
| `1D` | `8.31` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 208.40 USD | 0.00 USD | 39,240.00 USD |
| `7D` | `8.31` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 257,860.00 USD | 0.00 USD | 2,470.00 USD |
| `1D` | `8.32` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 68,600.00 USD | 4,060.00 USD | 16.44 USD |
| `1D` | `8.33` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 109.14 USD |
| `7D` | `8.33` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 14,600.00 USD | 0.00 USD | 4,950.00 USD |
| `1D` | `8.34` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 0.00 USD | 2,210.00 USD | 13.84 USD |
| `1D` | `8.35` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 0.00 USD | 16,880.00 USD | 16,970.00 USD |
| `7D` | `8.35` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 223,170.00 USD | 0.00 USD | 4,970.00 USD |
| `1D` | `8.36` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 17,800.00 USD |
| `1D` | `8.37` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 0.00 USD | 6,430.00 USD | 16.86 USD |
| `7D` | `8.37` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 38,420.00 USD |
| `1D` | `8.38` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 0.00 USD | 3,420.00 USD | 50,290.00 USD |
| `1D` | `8.39` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 100,740.00 USD | 13,620.00 USD | 32,610.00 USD |
| `7D` | `8.39` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 0.00 USD | 7,600.00 USD | 68,640.00 USD |
| `1D` | `8.40` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 10,500.00 USD | 7,000.00 USD | 51,900.00 USD |
| `1D` | `8.41` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 0.00 USD | 2,050.00 USD | 0.00 USD |
| `7D` | `8.41` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 194,850.00 USD | 0.00 USD | 55,630.00 USD |
| `1D` | `8.42` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 0.00 USD | 6,250.00 USD | 14,870.00 USD |
| `1D` | `8.43` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 45,340.00 USD | 7,730.00 USD | 7,540.00 USD |
| `7D` | `8.43` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 22,800.00 USD | 0.00 USD | 2,720.00 USD |
| `1D` | `8.44` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 12,340.00 USD | 27,610.00 USD | 120,220.00 USD |
| `1D` | `8.45` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 55,250.00 USD | 0.00 USD | 163,170.00 USD |
| `7D` | `8.45` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 156,410.00 USD | 8,000.00 USD | 173,910.00 USD |
| `1D` | `8.46` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 482.90 USD | 0.00 USD | 124,360.00 USD |
| `1D` | `8.47` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.47` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 5,530.00 USD |
| `1D` | `8.48` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 1,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.49` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 953.70 USD | 0.00 USD | 12.70 USD |
| `7D` | `8.49` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 0.00 USD | 81,010.00 USD | 153,240.00 USD |
| `1D` | `8.50` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 465.10 USD | 68,460.00 USD | 127,000.00 USD |
| `1D` | `8.51` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 0.00 USD | 21,730.00 USD | 172,440.00 USD |
| `7D` | `8.51` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 0.00 USD | 129,490.00 USD | 91,380.00 USD |
| `1D` | `8.52` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 183,450.00 USD | 25,890.00 USD | 4,800.00 USD |
| `1D` | `8.53` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 34,030.00 USD | 32,530.00 USD | 0.00 USD |
| `7D` | `8.53` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 176,360.00 USD | 144,990.00 USD | 0.00 USD |
| `1D` | `8.54` | 944,730.00 USD | 0.00 USD | 944,730.00 USD | 202,780.00 USD | 3,210.00 USD | 156.94 USD |
| `1D` | `8.55` | 738,570.00 USD | 0.00 USD | 738,570.00 USD | 150,640.00 USD | 1,710.00 USD | 25,120.00 USD |
| `7D` | `8.55` | 847,230.00 USD | 0.00 USD | 847,230.00 USD | 441,870.00 USD | 158,680.00 USD | 963.29 USD |
| `1D` | `8.56` | 561,100.00 USD | 0.00 USD | 561,100.00 USD | 138,980.00 USD | 38,320.00 USD | 0.00 USD |
| `1D` | `8.57` | 383,800.00 USD | 0.00 USD | 383,800.00 USD | 180,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.57` | 245,720.00 USD | 0.00 USD | 245,720.00 USD | 9,740.00 USD | 115,860.00 USD | 27,720.00 USD |
| `1D` | `8.58` | 203,160.00 USD | 0.00 USD | 203,160.00 USD | 60,020.00 USD | 5,060.00 USD | 118.61 USD |
| `1D` | `8.59` | 137,960.00 USD | 0.00 USD | 137,960.00 USD | 1,600.00 USD | 21,360.00 USD | 0.00 USD |
| `7D` | `8.59` | 92,400.00 USD | 0.00 USD | 92,400.00 USD | 0.00 USD | 90,970.00 USD | 1,430.00 USD |
| `1D` | `8.60` | 115,000.00 USD | 0.00 USD | 115,000.00 USD | 1,400.00 USD | 28,880.00 USD | 0.00 USD |
| `1D` | `8.61` | 84,710.00 USD | 0.00 USD | 84,710.00 USD | 2,430.00 USD | 0.00 USD | 82,280.00 USD |
| `7D` | `8.61` | 3,770.00 USD | 3,770.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD | 959.24 USD |
| `7D` | `8.61` | 7,550.00 USD | 7,550.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD | 959.24 USD |
| `1D` | `8.62` | 186,620.00 USD | 186,620.00 USD | 0.00 USD | 39,490.00 USD | 26,090.00 USD | 121,040.00 USD |
| `1D` | `8.62` | 373,240.00 USD | 373,240.00 USD | 0.00 USD | 39,490.00 USD | 26,090.00 USD | 121,040.00 USD |
| `1D` | `8.63` | 517,140.00 USD | 517,140.00 USD | 0.00 USD | 104,120.00 USD | 39,780.00 USD | 0.00 USD |
| `7D` | `8.63` | 41,060.00 USD | 41,060.00 USD | 0.00 USD | 0.00 USD | 5,680.00 USD | 27,830.00 USD |
| `1D` | `8.64` | 563,570.00 USD | 563,570.00 USD | 0.00 USD | 1,360.00 USD | 6,540.00 USD | 38,530.00 USD |
| `1D` | `8.65` | 669,370.00 USD | 669,370.00 USD | 0.00 USD | 3,350.00 USD | 6,810.00 USD | 95,630.00 USD |
| `7D` | `8.65` | 339,410.00 USD | 339,410.00 USD | 0.00 USD | 191,350.00 USD | 29,750.00 USD | 77,250.00 USD |
| `1D` | `8.66` | 925,120.00 USD | 925,120.00 USD | 0.00 USD | 145,440.00 USD | 31,810.00 USD | 78,500.00 USD |
| `1D` | `8.67` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 6,660.00 USD | 3,750.00 USD | 190,530.00 USD |
| `7D` | `8.67` | 661,220.00 USD | 661,220.00 USD | 0.00 USD | 77,920.00 USD | 24,870.00 USD | 219,020.00 USD |
| `1D` | `8.68` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 67,870.00 USD | 12,020.00 USD | 25,890.00 USD |
| `1D` | `8.69` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 9,340.00 USD | 16,260.00 USD | 33,840.00 USD |
| `7D` | `8.69` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 158,430.00 USD | 48,960.00 USD | 162,790.00 USD |
| `1D` | `8.70` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 60,790.00 USD | 0.00 USD | 23,500.00 USD |
| `1D` | `8.71` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 18,720.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.71` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 87,110.00 USD | 11,120.00 USD | 0.00 USD |
| `1D` | `8.72` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 17,080.00 USD | 0.00 USD | 50,790.00 USD |
| `1D` | `8.73` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 13,280.00 USD | 28,810.00 USD | 32,610.00 USD |
| `7D` | `8.73` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 51,030.00 USD | 10,790.00 USD | 0.00 USD |
| `1D` | `8.74` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 37,830.00 USD | 3,500.00 USD | 12,900.00 USD |
| `1D` | `8.75` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 31,160.00 USD | 4,580.00 USD | 4,980.00 USD |
| `7D` | `8.75` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 196,960.00 USD | 19,690.00 USD | 0.00 USD |
| `1D` | `8.76` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 80,300.00 USD | 0.00 USD | 29,010.00 USD |
| `1D` | `8.77` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 120,600.00 USD | 2,060.00 USD | 43,030.00 USD |
| `7D` | `8.77` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 81,930.00 USD |
| `1D` | `8.78` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 41,340.00 USD | 20,740.00 USD | 9,880.00 USD |
| `1D` | `8.79` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 34,630.00 USD | 12,000.00 USD | 29,010.00 USD |
| `7D` | `8.79` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 29,660.00 USD | 33,300.00 USD | 65,810.00 USD |
| `1D` | `8.80` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 100,950.00 USD | 14,490.00 USD | 23,840.00 USD |
| `1D` | `8.81` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 20,700.00 USD | 2,240.00 USD | 42.52 USD |
| `7D` | `8.81` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 102,790.00 USD | 8,450.00 USD | 19,880.00 USD |
| `1D` | `8.82` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 2,580.00 USD | 0.00 USD | 19,620.00 USD |
| `1D` | `8.83` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 73,440.00 USD | 12,580.00 USD | 0.00 USD |
| `7D` | `8.83` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 98,250.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.84` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 5,070.00 USD | 0.00 USD | 73,730.00 USD |
| `1D` | `8.85` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 12,030.00 USD | 3,360.00 USD | 11,200.00 USD |
| `7D` | `8.85` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 29,310.00 USD | 0.00 USD | 58,800.00 USD |
| `1D` | `8.86` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 654.49 USD | 0.00 USD | 607.55 USD |
| `1D` | `8.87` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 1,700.00 USD | 0.00 USD | 8,900.00 USD |
| `7D` | `8.87` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23,610.00 USD |
| `1D` | `8.88` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 10,670.00 USD | 186.36 USD |
| `1D` | `8.89` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 711.75 USD | 2,150.00 USD | 32,910.00 USD |
| `7D` | `8.89` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 73,830.00 USD |
| `1D` | `8.90` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 26,760.00 USD | 5,990.00 USD | 96,540.00 USD |
| `1D` | `8.91` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 30,400.00 USD | 11,620.00 USD | 13,520.00 USD |
| `7D` | `8.91` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 2,440.00 USD | 0.00 USD | 88,620.00 USD |
| `1D` | `8.92` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 1,020.00 USD | 67.52 USD |
| `1D` | `8.93` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 33,960.00 USD | 1,810.00 USD | 24,930.00 USD |
| `7D` | `8.93` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 157,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.94` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 33,070.00 USD | 12,260.00 USD | 3,770.00 USD |
| `1D` | `8.95` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 2,970.00 USD | 4,240.00 USD | 228.76 USD |
| `7D` | `8.95` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 1,390.00 USD | 4,000.00 USD | 27,130.00 USD |
| `1D` | `8.96` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD | 175.90 USD |
| `1D` | `8.97` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 671.53 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.97` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD | 791.90 USD |
| `1D` | `8.98` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 39,670.00 USD | 7,700.00 USD | 19,670.00 USD |
| `1D` | `8.99` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 48,820.00 USD | 24,940.00 USD | 3,420.00 USD |
| `7D` | `8.99` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 144,700.00 USD | 0.00 USD | 9,550.00 USD |
| `1D` | `9.00` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 37,380.00 USD | 0.00 USD | 8,090.00 USD |
| `1D` | `9.01` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 12,030.00 USD | 16,150.00 USD |
| `7D` | `9.01` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 230,880.00 USD | 36,180.00 USD | 20,780.00 USD |
| `1D` | `9.02` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 40,250.00 USD | 33,630.00 USD | 5,010.00 USD |
| `1D` | `9.03` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 124,460.00 USD | 14,810.00 USD | 34,410.00 USD |
| `7D` | `9.03` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 106,530.00 USD | 101,140.00 USD | 15,600.00 USD |
| `1D` | `9.04` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 40,700.00 USD | 10,710.00 USD | 21,020.00 USD |
| `1D` | `9.05` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 20,930.00 USD | 13,500.00 USD | 29,630.00 USD |
| `7D` | `9.05` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 37,540.00 USD | 17,700.00 USD | 39,370.00 USD |
| `1D` | `9.06` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 27,450.00 USD | 6,890.00 USD | 12,830.00 USD |
| `1D` | `9.07` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 13,160.00 USD | 18,880.00 USD | 30,980.00 USD |
| `7D` | `9.07` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 3,990.00 USD | 14,140.00 USD | 37,030.00 USD |
| `1D` | `9.08` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 13,130.00 USD | 3,370.00 USD | 39,960.00 USD |
| `1D` | `9.09` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 88,040.00 USD | 11,440.00 USD | 31,640.00 USD |
| `7D` | `9.09` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 150,640.00 USD | 8,680.00 USD | 144,440.00 USD |
| `1D` | `9.10` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 16,430.00 USD | 16,280.00 USD | 36,960.00 USD |
| `1D` | `9.11` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 60,810.00 USD | 15,740.00 USD | 82,390.00 USD |
| `7D` | `9.11` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 877,120.00 USD | 37,620.00 USD | 570,640.00 USD |
| `1D` | `9.12` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 102,060.00 USD | 22,410.00 USD | 26,360.00 USD |
| `1D` | `9.13` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 83,970.00 USD | 17,230.00 USD | 40,180.00 USD |
| `7D` | `9.13` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 666,000.00 USD | 26,540.00 USD | 484,570.00 USD |
| `1D` | `9.14` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 30,150.00 USD | 3,380.00 USD | 29,600.00 USD |
| `1D` | `9.15` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 57,310.00 USD | 23,170.00 USD | 22,990.00 USD |
| `7D` | `9.15` | 6,760,000.00 USD | 6,760,000.00 USD | 0.00 USD | 357,020.00 USD | 38,700.00 USD | 269,880.00 USD |
| `1D` | `9.16` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 63,670.00 USD | 23,900.00 USD | 32,470.00 USD |
| `1D` | `9.17` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 79,790.00 USD | 3,200.00 USD | 49,540.00 USD |
| `7D` | `9.17` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 409,630.00 USD | 133,490.00 USD | 302,940.00 USD |
| `1D` | `9.18` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 29,050.00 USD | 26,430.00 USD | 31,220.00 USD |
| `1D` | `9.19` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 77,640.00 USD | 29,140.00 USD | 7,680.00 USD |
| `7D` | `9.19` | 8,420,000.00 USD | 8,420,000.00 USD | 0.00 USD | 503,250.00 USD | 108,440.00 USD | 193,350.00 USD |
| `1D` | `9.20` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 65,160.00 USD | 11,090.00 USD | 37,460.00 USD |
| `1D` | `9.21` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 32,470.00 USD | 2,950.00 USD | 4,650.00 USD |
| `7D` | `9.21` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 590,780.00 USD | 144,470.00 USD | 277,090.00 USD |
| `1D` | `9.22` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 57,840.00 USD | 2,850.00 USD | 11,100.00 USD |
| `1D` | `9.23` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 1,020.00 USD | 4,270.00 USD | 17.80 USD |
| `7D` | `9.23` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 582,450.00 USD | 92,780.00 USD | 371,150.00 USD |
| `1D` | `9.24` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 46,680.00 USD | 0.00 USD | 3,020.00 USD |
| `1D` | `9.25` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 18,220.00 USD | 5,840.00 USD | 9,510.00 USD |
| `7D` | `9.25` | 10,970,000.00 USD | 10,970,000.00 USD | 0.00 USD | 277,290.00 USD | 73,690.00 USD | 141,190.00 USD |
| `1D` | `9.26` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 969.99 USD | 0.00 USD | 3,540.00 USD |
| `1D` | `9.27` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 23,190.00 USD | 1,360.00 USD | 6,640.00 USD |
| `7D` | `9.27` | 11,300,000.00 USD | 11,300,000.00 USD | 0.00 USD | 156,190.00 USD | 118,550.00 USD | 55,570.00 USD |
| `1D` | `9.28` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 479.45 USD | 8,760.00 USD | 169.17 USD |
| `1D` | `9.29` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 16,580.00 USD | 4,140.00 USD | 17,930.00 USD |
| `7D` | `9.29` | 12,160,000.00 USD | 12,160,000.00 USD | 0.00 USD | 468,150.00 USD | 100,200.00 USD | 291,150.00 USD |
| `1D` | `9.30` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 40,220.00 USD | 7,520.00 USD | 11,600.00 USD |
| `1D` | `9.31` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 27,860.00 USD | 5,020.00 USD | 12,920.00 USD |
| `7D` | `9.31` | 12,790,000.00 USD | 12,790,000.00 USD | 0.00 USD | 307,520.00 USD | 55,090.00 USD | 275,010.00 USD |
| `1D` | `9.32` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | 5,070.00 USD |
| `1D` | `9.33` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 7,170.00 USD | 6,000.00 USD | 8,120.00 USD |
| `7D` | `9.33` | 13,200,000.00 USD | 13,200,000.00 USD | 0.00 USD | 163,740.00 USD | 64,710.00 USD | 179,520.00 USD |
| `1D` | `9.34` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 44,560.00 USD | 3,660.00 USD | 3,340.00 USD |
| `1D` | `9.35` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 13,810.00 USD | 0.00 USD | 14,910.00 USD |
| `7D` | `9.35` | 13,680,000.00 USD | 13,680,000.00 USD | 0.00 USD | 289,480.00 USD | 88,340.00 USD | 98,320.00 USD |
| `1D` | `9.36` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 5,220.00 USD | 6,760.00 USD | 8,030.00 USD |
| `1D` | `9.37` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 12,870.00 USD | 5,670.00 USD | 2,720.00 USD |
| `7D` | `9.37` | 14,060,000.00 USD | 14,060,000.00 USD | 0.00 USD | 262,910.00 USD | 34,660.00 USD | 84,550.00 USD |
| `1D` | `9.38` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 14,740.00 USD | 0.00 USD | 13,850.00 USD |
| `1D` | `9.39` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 9,400.00 USD | 0.00 USD | 12.70 USD |
| `7D` | `9.39` | 14,390,000.00 USD | 14,390,000.00 USD | 0.00 USD | 206,980.00 USD | 32,960.00 USD | 86,080.00 USD |
| `1D` | `9.40` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 22,070.00 USD | 0.00 USD | 12.64 USD |
| `1D` | `9.41` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 1,160.00 USD | 0.00 USD | 10,140.00 USD |
| `7D` | `9.41` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 265,320.00 USD | 30,790.00 USD | 119,560.00 USD |
| `1D` | `9.42` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 8,980.00 USD | 2,390.00 USD | 6,520.00 USD |
| `1D` | `9.43` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 5,640.00 USD | 700.38 USD | 20.54 USD |
| `7D` | `9.43` | 14,940,000.00 USD | 14,940,000.00 USD | 0.00 USD | 33,890.00 USD | 19,300.00 USD | 82,450.00 USD |
| `1D` | `9.44` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 496.10 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.45` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 1,240.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.45` | 15,030,000.00 USD | 15,030,000.00 USD | 0.00 USD | 68,670.00 USD | 16,970.00 USD | 11,190.00 USD |
| `1D` | `9.46` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 9,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.47` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 198.28 USD | 1,250.00 USD | 0.00 USD |
| `7D` | `9.47` | 15,140,000.00 USD | 15,140,000.00 USD | 0.00 USD | 53,420.00 USD | 14,840.00 USD | 35,760.00 USD |
| `1D` | `9.48` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 440.27 USD | 0.00 USD | 2,040.00 USD |
| `1D` | `9.49` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 20,610.00 USD | 572.85 USD | 5,870.00 USD |
| `7D` | `9.49` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 26,920.00 USD | 10,200.00 USD | 15,730.00 USD |
| `1D` | `9.50` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 4,500.00 USD | 930.34 USD | 0.00 USD |
| `7D` | `9.51` | 15,370,000.00 USD | 15,370,000.00 USD | 0.00 USD | 71,980.00 USD | 23,250.00 USD | 84,580.00 USD |
| `7D` | `9.53` | 15,490,000.00 USD | 15,490,000.00 USD | 0.00 USD | 96,550.00 USD | 15,360.00 USD | 6,960.00 USD |
| `7D` | `9.55` | 15,540,000.00 USD | 15,540,000.00 USD | 0.00 USD | 28,850.00 USD | 17,400.00 USD | 398.17 USD |
| `7D` | `9.57` | 15,620,000.00 USD | 15,620,000.00 USD | 0.00 USD | 60,840.00 USD | 2,130.00 USD | 25,110.00 USD |
| `7D` | `9.59` | 15,670,000.00 USD | 15,670,000.00 USD | 0.00 USD | 26,920.00 USD | 7,840.00 USD | 15,030.00 USD |
| `7D` | `9.61` | 15,750,000.00 USD | 15,750,000.00 USD | 0.00 USD | 48,040.00 USD | 1,540.00 USD | 21,980.00 USD |
| `7D` | `9.63` | 15,770,000.00 USD | 15,770,000.00 USD | 0.00 USD | 16,170.00 USD | 4,500.00 USD | 7,110.00 USD |
| `7D` | `9.65` | 15,840,000.00 USD | 15,840,000.00 USD | 0.00 USD | 31,780.00 USD | 13,820.00 USD | 18,580.00 USD |
| `7D` | `9.67` | 15,900,000.00 USD | 15,900,000.00 USD | 0.00 USD | 31,000.00 USD | 11,120.00 USD | 17,310.00 USD |
| `7D` | `9.69` | 16,000,000.00 USD | 16,000,000.00 USD | 0.00 USD | 80,910.00 USD | 7,330.00 USD | 15,280.00 USD |
| `7D` | `9.71` | 16,100,000.00 USD | 16,100,000.00 USD | 0.00 USD | 44,510.00 USD | 9,500.00 USD | 42,980.00 USD |
| `7D` | `9.73` | 16,120,000.00 USD | 16,120,000.00 USD | 0.00 USD | 3,060.00 USD | 3,160.00 USD | 11,530.00 USD |
| `7D` | `9.75` | 16,200,000.00 USD | 16,200,000.00 USD | 0.00 USD | 34,630.00 USD | 15,540.00 USD | 29,880.00 USD |
| `7D` | `9.77` | 16,300,000.00 USD | 16,300,000.00 USD | 0.00 USD | 50,040.00 USD | 7,410.00 USD | 45,920.00 USD |
| `7D` | `9.79` | 16,370,000.00 USD | 16,370,000.00 USD | 0.00 USD | 47,490.00 USD | 17,990.00 USD | 1,250.00 USD |
| `7D` | `9.81` | 16,540,000.00 USD | 16,540,000.00 USD | 0.00 USD | 102,900.00 USD | 23,930.00 USD | 47,690.00 USD |
| `7D` | `9.83` | 16,690,000.00 USD | 16,690,000.00 USD | 0.00 USD | 54,150.00 USD | 29,270.00 USD | 62,300.00 USD |
| `7D` | `9.85` | 16,810,000.00 USD | 16,810,000.00 USD | 0.00 USD | 70,400.00 USD | 2,210.00 USD | 49,650.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `357.08M` | Total OI Tokens: `41,474,930.0 AVAX`
  * 1h OI Change: `-0.02%` | 4h OI Change: `+5.07%` | 24h OI Change: `-7.26%`
  * Exchange Breakdown: Binance=`82.64M` | Bybit=`58.31M` | OKX=`11.76M` | Hyperliquid=`16.96M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-4.38K` | Last 24h: `18.18K` | Last 3d: `59.53K` | Last 7d: `106.20K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0233%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0049%` | **USDT Bitget** | `0.0062%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `45.39%` | `54.61%` | `0.83` | 5,980,000.00 USD |
| `15M` | `Binance` | `48.71%` | `51.29%` | `0.95` | 1,770,000.00 USD |
| `15M` | `OKX` | `38.22%` | `61.78%` | `0.62` | 440,980.00 USD |
| `15M` | `Bybit` | `23.75%` | `76.25%` | `0.31` | 774,480.00 USD |
| `15M` | `KuCoin` | `56.4%` | `43.6%` | `1.29` | 12,390.00 USD |
| `15M` | `Gate` | `50.96%` | `49.04%` | `1.04` | 91,780.00 USD |
| `15M` | `Bitget` | `28.06%` | `71.94%` | `0.39` | 199,030.00 USD |
| `15M` | `BingX` | `40.79%` | `59.21%` | `0.69` | 103,100.00 USD |
| `15M` | `MEXC` | `43.16%` | `56.84%` | `0.76` | 1,710,000.00 USD |
| `15M` | `Bitunix` | `44.07%` | `55.93%` | `0.79` | 261,970.00 USD |
| `15M` | `Hyperliquid` | `61.27%` | `38.73%` | `1.58` | 127,540.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `80.7%` | `19.3%` | `4.18` | 324,110.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 3,930.00 USD |
| `15M` | `HTX` | `93.25%` | `6.75%` | `13.81` | 4,560.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `98.3%` | `1.7%` | `57.82` | 147,150.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `16.26%` | `83.74%` | `0.19` | 8,620.00 USD |
| `15M` | `Whale Positions` | `48.71%` | `51.29%` | `0.95` | 1,770,000.00 USD |
| `15M` | `Global Accounts` | `45.39%` | `54.61%` | `0.83` | 5,980,000.00 USD |
| `1H` | `AVAX` | `49.18%` | `50.82%` | `0.97` | 23,220,000.00 USD |
| `1H` | `Binance` | `53.35%` | `46.65%` | `1.14` | 8,620,000.00 USD |
| `1H` | `OKX` | `48.18%` | `51.82%` | `0.93` | 2,160,000.00 USD |
| `1H` | `Bybit` | `40.24%` | `59.76%` | `0.67` | 2,340,000.00 USD |
| `1H` | `KuCoin` | `44.11%` | `55.89%` | `0.79` | 118,110.00 USD |
| `1H` | `Gate` | `40.83%` | `59.17%` | `0.69` | 308,620.00 USD |
| `1H` | `Bitget` | `42.5%` | `57.5%` | `0.74` | 637,370.00 USD |
| `1H` | `BingX` | `23.35%` | `76.65%` | `0.30` | 854,810.00 USD |
| `1H` | `MEXC` | `48.48%` | `51.52%` | `0.94` | 6,050,000.00 USD |
| `1H` | `Bitunix` | `42.23%` | `57.77%` | `0.73` | 794,170.00 USD |
| `1H` | `Hyperliquid` | `53.61%` | `46.39%` | `1.16` | 379,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `66.7%` | `33.3%` | `2.00` | 593,740.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `85.01%` | `14.99%` | `5.67` | 154,140.00 USD |
| `1H` | `HTX` | `82.73%` | `17.27%` | `4.79` | 34,730.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `94.91%` | `5.09%` | `18.65` | 170,920.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `29.88%` | `70.12%` | `0.43` | 15,820.00 USD |
| `1H` | `Whale Positions` | `53.35%` | `46.65%` | `1.14` | 8,620,000.00 USD |
| `1H` | `Global Accounts` | `49.18%` | `50.82%` | `0.97` | 23,220,000.00 USD |
| `4H` | `AVAX` | `47.02%` | `52.98%` | `0.89` | 142,300,000.00 USD |
| `4H` | `Binance` | `47.47%` | `52.53%` | `0.90` | 62,920,000.00 USD |
| `4H` | `OKX` | `46.37%` | `53.63%` | `0.86` | 19,630,000.00 USD |
| `4H` | `Bybit` | `48.82%` | `51.18%` | `0.95` | 25,970,000.00 USD |
| `4H` | `KuCoin` | `48.27%` | `51.73%` | `0.93` | 3,260,000.00 USD |
| `4H` | `Gate` | `38.86%` | `61.14%` | `0.64` | 8,440,000.00 USD |
| `4H` | `Bitget` | `44.79%` | `55.21%` | `0.81` | 5,920,000.00 USD |
| `4H` | `BingX` | `26.96%` | `73.04%` | `0.37` | 1,490,000.00 USD |
| `4H` | `MEXC` | `51.74%` | `48.26%` | `1.07` | 2,340,000.00 USD |
| `4H` | `Bitunix` | `45.4%` | `54.6%` | `0.83` | 1,980,000.00 USD |
| `4H` | `Hyperliquid` | `54.46%` | `45.54%` | `1.20` | 4,700,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.48%` | `52.52%` | `0.90` | 1,900,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `46.18%` | `53.82%` | `0.86` | 1,870,000.00 USD |
| `4H` | `HTX` | `44.48%` | `55.52%` | `0.80` | 675,170.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `43.25%` | `56.75%` | `0.76` | 319,300.00 USD |
| `4H` | `Aster` | `45.89%` | `54.11%` | `0.85` | 172,070.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `55.63%` | `44.37%` | `1.25` | 722,870.00 USD |
| `4H` | `Whale Positions` | `47.47%` | `52.53%` | `0.90` | 62,920,000.00 USD |
| `4H` | `Global Accounts` | `47.02%` | `52.98%` | `0.89` | 142,300,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `8.38` | `8.37` | `8.38` | `8.39` | `8.33` | 1,720,663.97 USD | 1,209,797.38 USD | 510,866.59 USD | 698,930.78 USD | `+40.62%` | `15B / 2S` |
| `0:00 UTC` | `8.44` | `8.42` | `8.44` | `8.46` | `8.37` | 1,398,848.87 USD | 756,591.46 USD | 642,257.41 USD | 114,334.05 USD | `+8.17%` | `18B / 13S` |
| `5:00 UTC` | `8.43` | `8.45` | `8.43` | `8.48` | `8.43` | 1,888,943.37 USD | 611,021.12 USD | 1,277,922.26 USD | -666,901.14 USD | `-35.31%` | `4B / 11S` |
| `0:00 UTC` | `8.42` | `8.42` | `8.42` | `8.47` | `8.40` | 987,610.98 USD | 453,562.40 USD | 534,048.58 USD | -80,486.17 USD | `-8.15%` | `8B / 9S` |
| `5:00 UTC` | `8.49` | `8.49` | `8.49` | `8.51` | `8.45` | 1,927,143.92 USD | 1,382,163.88 USD | 544,980.04 USD | 837,183.84 USD | `+43.44%` | `23B / 5S` |
| `0:00 UTC` | `8.51` | `8.51` | `8.51` | `8.53` | `8.49` | 1,011,410.99 USD | 608,193.60 USD | 403,217.39 USD | 204,976.20 USD | `+20.27%` | `7B / 2S` |
| `5:00 UTC` | `8.54` | `8.54` | `8.54` | `8.56` | `8.52` | 2,075,576.75 USD | 880,640.95 USD | 1,194,935.80 USD | -314,294.84 USD | `-15.14%` | `5B / 5S` |
| `0:00 UTC` | `8.60` | `8.58` | `8.60` | `8.61` | `8.53` | 2,341,070.35 USD | 1,614,335.42 USD | 726,734.93 USD | 887,600.49 USD | `+37.91%` | `23B / 4S` |
| `5:00 UTC` | `8.58` | `8.57` | `8.58` | `8.58` | `8.56` | 905,120.57 USD | 371,003.65 USD | 534,116.93 USD | -163,113.28 USD | `-18.02%` | `1B / 6S` |
| `0:00 UTC` | `8.61` | `8.59` | `8.61` | `8.61` | `8.57` | 595,695.30 USD | 295,775.49 USD | 299,919.80 USD | -4,144.31 USD | `-0.70%` | `7B / 5S` |

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
| `5m` | 12,020.00 USD | 24,140.00 USD | **`ACCUMULATION`** |
| `15m` | 32,330.00 USD | -65,290.00 USD | **`DISTRIBUTION`** |
| `30m` | 20,660.00 USD | -355,420.00 USD | **`DISTRIBUTION`** |
| `1h` | 335,480.00 USD | -1,430.00 USD | **`ACCUMULATION`** |
| `2h` | 556,900.00 USD | 37,830.00 USD | **`ACCUMULATION`** |
| `4h` | 624,190.00 USD | 2,440,000.00 USD | **`ACCUMULATION`** |
| `6h` | -899,400.00 USD | -1,010,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -121,140.00 USD | -8,080,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,230,000.00 USD | -7,250,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,510,000.00 USD | -10,340,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -8,260,000.00 USD | -53,960,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -57,060,000.00 USD | -269,930,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+12.02K` | 15m=`+32.33K` | 1h=`+335.48K` | 24h=`-2.51M`
* Futures Capital Netflows: 5m=`+24.14K` | 15m=`-65.29K` | 1h=`-1.43K` | 24h=`-10.34M`
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
  * `2026-10-30 11:03:23 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:09:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:10:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `8.16` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `8.03` (Risk Distance: `0.1303` pts)
  * +2.5R Take Profit: `8.49`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.46` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `8.59` (Risk Distance: `0.1303` pts)
  * +2.5R Take Profit: `8.13`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.67`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
